from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from Options import OptionError, PlandoConnection
from ..options import DeathsDoorPlandoConnections, EntranceRandomization
from .scene_transitions import two_way_scene_transitions, one_way_scene_transitions
from entrance_rando import (
    ERPlacementState,
    EntranceRandomizationError,
    EntranceType,
    randomize_entrances,
    disconnect_entrance_for_randomization,
)
from .entrance_class import DeathsDoorEntrance, DeathsDoorConnectionGroup
from ..regions import DeathsDoorRegionName as R
from ..jefferson import create_jefferson_vanilla_connections, jefferson_tag

if TYPE_CHECKING:
    from .. import DeathsDoorWorld


def create_vanilla_entrances(world: "DeathsDoorWorld"):
    # Create vanilla entrances
    all_scene_transitions = two_way_scene_transitions + one_way_scene_transitions
    for scene_transition_pair in all_scene_transitions:
        entrance_type = (
            EntranceType.ONE_WAY
            if scene_transition_pair[1] == None
            else EntranceType.TWO_WAY
        )
        entrance_group = (
            DeathsDoorConnectionGroup.ONE_WAY
            if scene_transition_pair[1] == None
            else DeathsDoorConnectionGroup.STANDARD
        )
        for scene_transition in scene_transition_pair:
            if scene_transition is not None:
                start_region: Region = world.get_region(
                    scene_transition.starting_region.value
                )
                end_region: Region = world.get_region(
                    scene_transition.ending_region.value
                )
                new_entrance = world.create_entrance(
                    start_region, end_region, scene_transition.rule
                )
                if new_entrance is not None:
                    new_entrance.randomization_type = entrance_type
                    new_entrance.randomization_group = entrance_group

    create_jefferson_vanilla_connections(world)


def connect_plando(
    world: "DeathsDoorWorld",
    plando_connections: DeathsDoorPlandoConnections,
    coupled: bool,
) -> None:
    for plando_connection in plando_connections:
        connect_plando_connection(world, plando_connection, coupled)


def connect_plando_connection(
    world: "DeathsDoorWorld",
    plando_connection: PlandoConnection,
    coupled: bool,
) -> None:
    if plando_connection.direction == "exit":
        ## Switch connections to be in entrance direction
        temp_exit = plando_connection.exit
        plando_connection.exit = plando_connection.entrance
        plando_connection.entrance = temp_exit
    two_way_entrance = not plando_connection.entrance in [
        x[0].starting_region.value for x in one_way_scene_transitions
    ]
    two_way_exit = not plando_connection.exit in [
        x[0].ending_region.value for x in one_way_scene_transitions
    ]

    if two_way_exit != two_way_entrance:
        raise OptionError(
            f"One-ways (Avarices) cannot be plando'd to two-ways. Plando connection {plando_connection.entrance} to {plando_connection.exit} is invalid."
        )
    if (
        not getattr(world.multiworld, "re_gen_passthrough", {})
        and plando_connection.direction != "both"
        and coupled
        and two_way_entrance
    ):
        raise Warning(
            f"If entrance randomization is set to coupled, all two-way plando_connections will be forced to be both. Plando connection {plando_connection.entrance} to {plando_connection.exit} has direction {plando_connection.direction}"
        )

    if two_way_entrance:
        entrance = find_scene_transition_from_region(plando_connection.entrance, True)
        exit = find_scene_transition_from_region(plando_connection.exit, False)
    else:
        entrance = find_scene_transition_from_region(
            plando_connection.entrance, True, False
        )
        exit = find_scene_transition_from_region(plando_connection.exit, False, False)

    from_region = world.get_region(plando_connection.entrance)
    to_region = world.get_region(plando_connection.exit)

    if (create_entrance_for_regions(world, from_region, to_region, entrance)):
        if (coupled or plando_connection.direction == "both") and two_way_entrance:
            create_entrance_for_regions(world, to_region, from_region, exit)
        # Replicate connections between Jefferson regions
        connect_jefferson(world, from_region.name, to_region.name)
        if (coupled or plando_connection.direction == "both") and two_way_entrance:
            connect_jefferson(world, to_region.name, from_region.name)


def create_entrance_for_regions(
    world: "DeathsDoorWorld",
    from_region: Region,
    to_region: Region,
    entrance: DeathsDoorEntrance,
) -> bool:
    ends_exist = True
    try:
        name = remove_dangling_exit(from_region)
    except ValueError:
        ends_exist = False
    try:
        remove_dangling_entrance(to_region)
    except ValueError:
        ends_exist = False
    if ends_exist:
        world.create_entrance(from_region, to_region, entrance.rule, name)
        world.entrance_pairings[from_region.name] = to_region.name
    return ends_exist


def find_scene_transition_from_region(
    region_name: str, from_region: bool, two_way: bool = True
) -> DeathsDoorEntrance:
    transitions = two_way_scene_transitions if two_way else one_way_scene_transitions
    if from_region:
        found = next(
            (
                transition_pair[0]
                for transition_pair in transitions
                if transition_pair[0].starting_region.value == region_name
            ),
            None,
        )
        if not found and two_way:
            found = next(
                (
                    transition_pair[1]
                    for transition_pair in transitions
                    if transition_pair[1].starting_region.value == region_name
                ),
                None,
            )
    else:
        found = next(
            (
                transition_pair[0]
                for transition_pair in transitions
                if transition_pair[0].ending_region.value == region_name
            ),
            None,
        )
        if not found and two_way:
            found = next(
                (
                    transition_pair[1]
                    for transition_pair in transitions
                    if transition_pair[1].ending_region.value == region_name
                ),
                None,
            )
    if not found:
        raise Warning(f"no transition for region name {region_name} found")
    return found


def randomize_one_ways(world: "DeathsDoorWorld"):
    # Randomize these separately so that GER doesn't choke

    from_exits = sorted(
        [
            ex
            for region in world.get_regions()
            for ex in region.exits
            if not ex.connected_region
            and ex.randomization_group == DeathsDoorConnectionGroup.ONE_WAY
        ],
        key=lambda x: x.name,
    )
    world.random.shuffle(from_exits)
    to_entrances = sorted(
        [
            entrance
            for region in world.get_regions()
            for entrance in region.entrances
            if not entrance.parent_region
            and entrance.randomization_group == DeathsDoorConnectionGroup.ONE_WAY
        ],
        key=lambda x: x.name,
    )
    world.random.shuffle(to_entrances)

    for from_exit, to_entrance in zip(from_exits, to_entrances):
        remove_dangling_exit(from_exit.parent_region)
        remove_dangling_entrance(to_entrance.connected_region)
        from_scene_transition = find_scene_transition_from_region(
            from_exit.parent_region.name, True, False
        )
        world.entrance_pairings[from_exit.parent_region.name] = (
            to_entrance.connected_region.name
        )
        entrance = world.create_entrance(
            from_exit.parent_region,
            to_entrance.connected_region,
            from_scene_transition.rule,
        )
        entrance.randomization_group = DeathsDoorConnectionGroup.ONE_WAY
        entrance.randomization_type = EntranceType.ONE_WAY


def connect_jefferson(
    world: "DeathsDoorWorld", start_region_name: str, end_region_name: str
):
    try:
        start_region_jefferson = world.get_region(start_region_name + jefferson_tag)
    except KeyError:
        start_region_jefferson = None
    try:
        end_region_jefferson = world.get_region(end_region_name + jefferson_tag)
    except KeyError:
        end_region_jefferson = None
    if start_region_jefferson:
        try:
            remove_dangling_exit(start_region_jefferson)
        except ValueError:
            pass
    if end_region_jefferson:
        try:
            remove_dangling_entrance(end_region_jefferson)
        except ValueError:
            pass

    if start_region_jefferson and end_region_jefferson:
        scene_transition = find_scene_transition_from_region(end_region_name, True)
        if not scene_transition.no_jefferson:
            new_entrance = world.create_entrance(
                start_region_jefferson, end_region_jefferson, scene_transition.rule
            )
            new_entrance.randomization_group = DeathsDoorConnectionGroup.JEFFERSON
            new_entrance.randomization_type = EntranceType.TWO_WAY


def connect_entrances_function(world: "DeathsDoorWorld"):
    def on_connect(
        _: ERPlacementState,
        exits: list[Entrance],
        entrances: list[Entrance],
    ) -> bool:
        for exit, entrance in zip(exits, entrances):
            connect_jefferson(
                world, exit.parent_region.name, entrance.connected_region.name
            )
        return True

    if world.options.entrance_randomization != EntranceRandomization.option_off:
        coupled = (
            world.options.entrance_randomization == EntranceRandomization.option_coupled
        )

        # Create all the dangling ends
        for scene_transition_pair in two_way_scene_transitions:
            for scene_transition in scene_transition_pair:
                for _exit in world.get_region(
                    scene_transition.starting_region
                ).get_exits():
                    if _exit.randomization_group == DeathsDoorConnectionGroup.STANDARD:
                        entrance: Entrance = _exit
                        disconnect_entrance_for_randomization(
                            entrance, entrance.randomization_group
                        )
                if scene_transition is not None and not scene_transition.no_jefferson:
                    start_region: Region = world.get_region(
                        scene_transition.starting_region.value + jefferson_tag,
                    )
                    for _exit in start_region.get_exits():
                        if (
                            _exit.randomization_group
                            == DeathsDoorConnectionGroup.JEFFERSON
                        ):
                            entrance: Entrance = _exit
                            disconnect_entrance_for_randomization(
                                entrance, entrance.randomization_group
                            )

        for scene_transition_pair in one_way_scene_transitions:
            for _exit in world.get_region(
                scene_transition_pair[0].starting_region
            ).get_exits():
                if _exit.randomization_group == DeathsDoorConnectionGroup.ONE_WAY:
                    entrance: Entrance = _exit
                    disconnect_entrance_for_randomization(
                        entrance,
                        entrance.randomization_group,
                        scene_transition_pair[0].name,
                    )

        # Plando
        if world.options.plando_connections and (
            not getattr(world.multiworld, "re_gen_passthrough", {})
            or not getattr(world.multiworld, "enforce_deferred_connections", "on")
            != "off"
        ):
            connect_plando(world, world.options.plando_connections, coupled)

        if not getattr(world.multiworld, "re_gen_passthrough", {}):
            # If in UT, only do plando

            # Randomize specifically the one-ways
            randomize_one_ways(world)

            retry_count = 0
            RETRY_MAX = 10
            successful_ER = False
            while retry_count < RETRY_MAX and not successful_ER:
                try:
                    final_result = randomize_entrances(
                        world,
                        coupled,
                        {
                            DeathsDoorConnectionGroup.STANDARD: [
                                DeathsDoorConnectionGroup.STANDARD
                            ]
                        },
                        er_targets=sorted(
                            [
                                entrance
                                for region in world.get_regions()
                                for entrance in region.entrances
                                if not entrance.parent_region
                                and entrance.randomization_group
                                == DeathsDoorConnectionGroup.STANDARD
                            ],
                            key=lambda x: x.name,
                        ),
                        exits=sorted(
                            [
                                ex
                                for region in world.get_regions()
                                for ex in region.exits
                                if not ex.connected_region
                                and ex.randomization_group
                                == DeathsDoorConnectionGroup.STANDARD
                            ],
                            key=lambda x: x.name,
                        ),
                        on_connect=on_connect,
                    )
                    jefferson_region = world.get_region(
                        R.FLOODED_FORTRESS_ENTRANCE_JEFFERSON.value
                    )
                    if (
                        not jefferson_region
                        in world.multiworld.get_all_state().reachable_regions[
                            world.player
                        ]
                    ):
                        raise EntranceRandomizationError(
                            f"Requested reachable region {jefferson_region.name} is not reachable in current state."
                        )

                    successful_ER = True
                    # print(retry_count)
                except EntranceRandomizationError as error:
                    retry_count += 1
                    if retry_count >= RETRY_MAX:
                        raise EntranceRandomizationError(
                            f"Death's Door: failed GER after {RETRY_MAX} attempts. Final error: {error}"
                        )
                    # Undo placements
                    for region in world.get_regions():
                        for _exit in region.get_exits():
                            _exit: Entrance = _exit
                            if (
                                (
                                    _exit.randomization_group
                                    == DeathsDoorConnectionGroup.STANDARD
                                    or _exit.randomization_group
                                    == DeathsDoorConnectionGroup.JEFFERSON
                                )
                                and _exit.parent_region
                                and _exit.connected_region
                                and (
                                    _exit.parent_region
                                    not in world.entrance_pairings.keys()
                                    and _exit.connected_region
                                    not in world.entrance_pairings.values()
                                )
                            ):
                                disconnect_entrance_for_randomization(
                                    _exit, _exit.randomization_group
                                )

            for placement in final_result.placements:
                world.entrance_pairings[placement.parent_region.name] = (
                    placement.connected_region.name
                )

            i = 0
            if coupled:
                direction = "both"
            else:
                direction = "entrance"
            for entrance, exit in world.entrance_pairings.items():
                if coupled:
                    # Skip every other two-way entrance because it is redundant in the spoiler on coupled
                    if i >= 1 and exit in world.entrance_pairings.keys():
                        i = 0
                        continue
                    i += 1
                world.multiworld.spoiler.set_entrance(
                    entrance, exit, direction, world.player
                )


# remove_dangling defs Credit to alwaysintreble's Messenger code
def remove_dangling_exit(region: Region) -> str | None:
    # find the disconnected exit and remove references to it
    for _exit in region.exits:
        if not _exit.connected_region:
            break
    else:
        raise ValueError(f"Unable to find randomized transition for {region}")
    name: str = _exit.name
    region.exits.remove(_exit)
    return name


def remove_dangling_entrance(region: Region) -> None:
    # find the disconnected entrance and remove references to it
    for _entrance in region.entrances:
        if not _entrance.parent_region:
            break
    else:
        raise ValueError(f"Invalid target region {region}")
    region.entrances.remove(_entrance)
