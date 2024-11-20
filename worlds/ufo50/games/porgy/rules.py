from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState
from worlds.generic.Rules import add_rule

from .locations import location_table, Hidden
from ...options import PorgyFuelDifficulty, PorgyRadar

if TYPE_CHECKING:
    from ... import UFO50World


fuel = "Porgy - Fuel Tank"
fish_gratitude = "Porgy - Fish Gratitude"
torpedo = "Porgy - Torpedo Upgrade"
mcguffin = "Porgy - Strange Light"
buster = "Porgy - Buster Torpedoes Module"
missile = "Porgy - Missile System Module"
depth_charge = "Porgy - Depth Charge Module"
spotlight = "Porgy - Spotlight Module"
drill = "Porgy - Drill Module"
radar = "Porgy - Radar System Module"
homing = "Porgy - Targeting System Module"


def has_fuel(amount: int, state: CollectionState, world: "UFO50World") -> bool:
    # todo: factor in fuel efficiency in some fashion?
    # todo: check for lambda capture shenanigans
    if world.options.porgy_fuel_difficulty < PorgyFuelDifficulty.option_hard:
        if world.options.porgy_fuel_difficulty:
            # medium
            amount = int(amount * 1.25)
        else:
            # easy
            amount = int(amount * 1.5)
    # you start with 4 fuel tanks
    if amount <= 4:
        return True
    # max fuel is 24, requiring all fuel tanks is a pain
    amount = min(amount, 21)
    return state.has(fuel, world.player, amount - 4)


def can_open_ship(state: CollectionState, world: "UFO50World") -> bool:
    return state.has(depth_charge, world.player) or (state.has(missile, world.player) and has_fuel(6, state, world))


def has_bomb(state: CollectionState, player: int) -> bool:
    return state.has_any((depth_charge, missile), player)


def has_light(state: CollectionState, world: "UFO50World") -> bool:
    return world.options.porgy_lanternless or state.has(spotlight, world.player)


def can_combat(target_score: int, state: CollectionState, player: int) -> bool:
    score = state.count(torpedo, player)

    if score >= target_score:
        return True
    # it's low enough that the other items here won't save it, so we might as well early out
    if score < target_score - 12:
        return False

    score += state.count(fish_gratitude, player) // 5 * 2

    if score >= target_score:
        return True
    # it's low enough that the other items here won't save it, so we might as well early out
    if score < target_score - 4:
        return False

    extra_power_count: int = state.has(buster, player) + state.has(missile, player) + state.has(homing, player)
    slots = 2 + state.count(mcguffin, player) // 2

    score += min(extra_power_count, slots - 1) * 2

    if score >= target_score:
        return True
    return False


def has_abyss_combat_logic(state: CollectionState, player: int) -> bool:
    torpedo_count = state.count(torpedo, player)
    # from looking at the map and hidden items, it seems they expect you to have 8 torpedo upgrades
    # as well as the missile launcher and/or burst torpedoes and the first 2 fish helpers
    if torpedo_count < 8:
        return False
    if torpedo_count < 10:
        return state.has(fish_gratitude, player, 5)
    return True


def has_enough_slots(loc_name: str, extra_mods_needed: int, state: CollectionState,
                     world: "UFO50World") -> bool:
    mods_needed = extra_mods_needed
    abyss = location_table[loc_name].region_name == "Abyss"
    hidden_status = location_table[loc_name].concealed
    if abyss and not world.options.porgy_lanternless:
        mods_needed += 1
    if hidden_status == Hidden.has_tell and world.options.porgy_radar == PorgyRadar.option_required:
        mods_needed += 1
    elif hidden_status == Hidden.no_tell and world.options.porgy_radar >= PorgyRadar.option_required:
        mods_needed += 1

    mcguffins_needed = 2 * (mods_needed - 2)
    if mcguffins_needed <= 0:
        return True
    if mcguffins_needed > 5:
        return False
    return state.has(mcguffin, world.player, mcguffins_needed)


# set the basic fuel requirements for spots that don't have multiple viable routes
def set_fuel_and_radar_reqs(world: "UFO50World", on_touch: bool) -> None:
    for loc_name, loc_data in location_table.items():
        loc = world.get_location(loc_name)
        if (loc_data.concealed == Hidden.no_tell and world.options.porgy_radar >= PorgyRadar.option_required
                or loc_data.concealed == Hidden.has_tell and world.options.porgy_radar == PorgyRadar.option_required):
            add_rule(loc, lambda state: state.has(radar, world.player))

        fuel_needed = loc_data.fuel_touch if on_touch else loc_data.fuel_get
        # if it is not set, it means it has some special requirements
        if not fuel_needed:
            continue
        add_rule(loc, lambda state, amt=fuel_needed: has_fuel(amt, state, world))


def create_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player
    check_on_touch = bool(world.options.porgy_check_on_touch)
    set_fuel_and_radar_reqs(world, check_on_touch)

    regions["Menu"].connect(regions["Shallows"])
    regions["Shallows"].connect(regions["Deeper"])
    regions["Shallows"].connect(regions["Shallows - Buster"],
                                rule=lambda state: state.has(buster, player))
    regions["Shallows"].connect(regions["Shallows - Missile"],
                                rule=lambda state: has_bomb(state, player))
    regions["Shallows"].connect(regions["Shallows - Depth"],
                                rule=lambda state: state.has(depth_charge, player))
    regions["Shallows"].connect(regions["Sunken Ship"],
                                rule=lambda state: can_open_ship(state, world))
    regions["Sunken Ship"].connect(regions["Sunken Ship - Buster"],
                                   rule=lambda state: state.has(buster, player))
    # vanilla seems to want you to have 8 torpedo upgrades, 2 fish friends, missiles, and buster before abyss
    regions["Deeper"].connect(regions["Abyss"],
                              rule=lambda state: has_light(state, world) and can_combat(16, state, player))

    # buster is covered by the region
    add_rule(world.get_location("Shallows Upper Mid - Fuel Tank in Floor at Surface"),
             lambda state: state.has(depth_charge, player))

    add_rule(world.get_location("Deeper Upper Mid - Egg in Dirt"),
             lambda state: state.has(drill, player))
    add_rule(world.get_location("Deeper Upper Mid - Spotlight Module"),
             lambda state: state.has(depth_charge, player))
    add_rule(world.get_location("Deeper Lower Mid - Fuel Tank in Floor"),
             lambda state: state.has(depth_charge, player))

    if check_on_touch:
        # shallows coral maze
        add_rule(world.get_location("Shallows Upper Right - Fuel Tank in Coral Maze"),
                 rule=lambda state: has_fuel(7, state, world)
                 or (has_fuel(3, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze"),
                 rule=lambda state: has_fuel(9, state, world)
                 or (has_fuel(5, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Shallows Upper Right - Egg in Coral Maze"),
                 rule=lambda state: has_fuel(11, state, world)
                 or (has_fuel(7, state, world) and state.has(drill, player)))

        # faster through the ship
        add_rule(world.get_location("Deeper Upper Left - Torpedo Upgrade in Wall"),
                 rule=lambda state: has_fuel(4, state, world)
                 or (has_fuel(3, state, world) and state.has(depth_charge, player)))

        # abyss
        # unless noted otherwise, routes were added together using partial routes
        # recommended to get more accurate numbers over time
        add_rule(world.get_location("Abyss Upper Left - Egg on Seaweed near Urchins"),
                 # go through the ship
                 rule=lambda state: state.has(depth_charge, player) and has_fuel(4, state, world)
                 # go around and through the dirt instead, less fuel than opening ship with missile
                 or state.has(drill, player) and has_fuel(5, state, world))

        add_rule(world.get_location("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade"),
                 # itemless: not valid
                 # drill only: 8/15
                 # depth only: 4/8
                 # missile only: not valid
                 # buster only: 6/10
                 # buster + drill: 5/10
                 # drill + missile: 7/14
                 # buster + missile: x/9
                 # buster + drill + depth charge path: 4/8 (same as depth only, so not relevant)
                 # buster + drill + missile path: x/8 (7 to open the rock with missile, 8 for the more efficient path)
                 rule=lambda state:
                 (has_fuel(4, state, world) and state.has(depth_charge, player))
                 or (has_fuel(5, state, world) and state.has_all((drill, buster), player)
                     and has_enough_slots("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", 2, state, world))
                 or (has_fuel(6, state, world) and state.has(buster, player))
                 or (has_fuel(7, state, world) and state.has_all((drill, missile), player))
                 or (has_fuel(8, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Abyss Upper Left - Torpedo Upgrade in Seaweed"),
                 # see above
                 rule=lambda state:
                 (has_fuel(4, state, world) and state.has(depth_charge, player))
                 or (has_enough_slots("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", 1, state, world)
                     and ((has_fuel(6, state, world) and state.has(buster, player))
                          or (has_fuel(7, state, world) and state.has_all((drill, missile), player))
                          or (has_fuel(8, state, world) and state.has(drill, player))
                          )
                     )
                 or (has_enough_slots("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", 2, state, world)
                     and has_fuel(5, state, world) and state.has_all((drill, buster), player))
                 )

        add_rule(world.get_location("Abyss Lower Left - Egg in Facility"),
                 # hard-requires drill, depth, or buster
                 # drill only: invalid
                 # buster only: invalid
                 # depth only: 7/10, only because you can only bring 2 depth charges with you
                 # buster + drill: 9/14
                 # buster + depth: 6/12 (12 > 10)
                 # drill + depth: 6/11 (11 > 10)
                 # buster + drill + missile: 8/12 (must bring missile with you, so you need the slots for it)
                 # buster + drill + depth: worse than depth only
                 rule=lambda state:
                 (state.has(depth_charge, player) and (has_fuel(7, state, world)
                                                       or (state.has_any((buster, drill), player)
                                                           and has_fuel(6, state, world))))
                 or (state.has_all((buster, drill), player) and has_fuel(9, state, world)
                     and has_enough_slots("Abyss Lower Left - Egg in Facility", 2, state, world))
                 or (state.has_all((buster, drill, missile), player) and has_fuel(8, state, world)
                     and has_enough_slots("Abyss Lower Left - Egg in Facility", 3, state, world))
                 )

        add_rule(world.get_location("Abyss Lower Left - Torpedo Upgrade in Facility"),
                 # hard-requires drill, depth, or buster
                 # drill only: invalid
                 # buster only: invalid
                 # depth only: 7/10
                 # buster + drill: 9/15
                 # buster + depth: 6/x
                 # drill + depth: 6/x
                 # buster + drill + missile: 9/13 (must bring missile with you, so you need the slots for it)
                 # buster + drill + depth: worse than depth only
                 rule=lambda state:
                 (state.has(depth_charge, player) and (has_fuel(7, state, world)
                                                       or (state.has_any((buster, drill), player)
                                                           and has_fuel(6, state, world))))
                 or (state.has_all((buster, drill), player) and has_fuel(9, state, world)
                     and has_enough_slots("Abyss Lower Left - Torpedo Upgrade in Facility", 2, state, world))
                 or (state.has_all((buster, drill, missile), player) and has_fuel(9, state, world)
                     and has_enough_slots("Abyss Lower Left - Torpedo Upgrade in Facility", 3, state, world))
                 )

        add_rule(world.get_location("Abyss Lower Left - Fuel Tank in Facility Floor"),
                 # requires buster and depth
                 # buster + depth: 7/9
                 # all others look worse
                 rule=lambda state:
                 state.has_all((buster, depth_charge) and has_fuel(7, state, world)
                               and has_enough_slots("Abyss Lower Left - Fuel Tank in Facility Floor", 2, state, world)))

    else:
        # shallows coral maze
        add_rule(world.get_location("Shallows Upper Right - Fuel Tank in Coral Maze"),
                 rule=lambda state: has_fuel(13, state, world)
                 or (has_fuel(6, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze"),
                 rule=lambda state: has_fuel(15, state, world)
                 or (has_fuel(8, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Shallows Upper Right - Egg in Coral Maze"),
                 rule=lambda state: has_fuel(16, state, world)
                 or (has_fuel(9, state, world) and state.has(drill, player)))

        # faster through the ship
        add_rule(world.get_location("Deeper Upper Left - Torpedo Upgrade in Wall"),
                 rule=lambda state: has_fuel(8, state, world)
                 or (has_fuel(5, state, world) and state.has(depth_charge, player)))

        # abyss
        # unless noted otherwise, routes were added together using partial routes
        # recommended to get more accurate numbers over time
        add_rule(world.get_location("Abyss Upper Left - Egg on Seaweed near Urchins"),
                 # I promise you this rule is correct, buster can't reach it
                 rule=lambda state: has_fuel(9, state, world) and state.has_any((depth_charge, drill), player))

        add_rule(world.get_location("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade"),
                 # see this check in the on touch section
                 rule=lambda state:
                 (has_fuel(8, state, world) and state.has(depth_charge, player))
                 or (has_fuel(8, state, world) and state.has_all((drill, missile, buster), player)
                     and has_enough_slots("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", 2, state, world))
                 or (has_fuel(9, state, world) and state.has_all((buster, missile), player))
                 or (has_fuel(10, state, world) and state.has(buster, player))
                 or (has_fuel(14, state, world) and state.has_all((drill, missile), player))
                 or (has_fuel(15, state, world) and state.has(drill, player)))
        add_rule(world.get_location("Abyss Upper Left - Torpedo Upgrade in Seaweed"),
                 # see above
                 rule=lambda state:
                 (has_fuel(8, state, world) and state.has(depth_charge, player))
                 or (has_enough_slots("Abyss Upper Left - Torpedo Upgrade in Seaweed", 1, state, world)
                     and ((has_fuel(9, state, world) and state.has_all((buster, missile), player))
                          or (has_fuel(10, state, world) and state.has(buster, player))
                          or (has_fuel(14, state, world) and state.has_all((drill, missile), player))
                          or (has_fuel(15, state, world) and state.has(drill, player))
                          ))
                 or (has_fuel(8, state, world) and state.has_all((drill, missile, buster), player)
                     and has_enough_slots("Abyss Upper Left - Torpedo Upgrade in Seaweed", 2, state, world)))

        add_rule(world.get_location("Abyss Lower Left - Egg in Facility"),
                 # hard-requires drill, depth, or buster
                 # drill only: invalid
                 # buster only: invalid
                 # depth only: 7/10, only because you can only bring 2 depth charges with you
                 # buster + drill: 9/14
                 # buster + depth: 6/12 (12 > 10)
                 # drill + depth: 6/11 (11 > 10)
                 # buster + drill + missile: 8/12 (must bring missile with you, so you need the slots for it)
                 # buster + drill + depth: worse than depth only
                 rule=lambda state:
                 (state.has(depth_charge, player) and (has_fuel(10, state, world)))
                 or (state.has_all((buster, drill), player) and has_fuel(14, state, world)
                     and has_enough_slots("Abyss Lower Left - Egg in Facility", 2, state, world))
                 or (state.has_all((buster, drill, missile), player) and has_fuel(12, state, world)
                     and has_enough_slots("Abyss Lower Left - Egg in Facility", 3, state, world))
                 )
        add_rule(world.get_location("Abyss Lower Left - Torpedo Upgrade in Facility"),
                 # hard-requires drill, depth, or buster
                 # drill only: invalid
                 # buster only: invalid
                 # depth only: 7/10
                 # buster + drill: 9/15
                 # buster + depth: 6/x
                 # drill + depth: 6/x
                 # buster + drill + missile: 9/13 (must bring missile with you, so you need the slots for it)
                 # buster + drill + depth: worse than depth only
                 rule=lambda state:
                 (state.has(depth_charge, player) and (has_fuel(10, state, world)))
                 or (state.has_all((buster, drill), player) and has_fuel(15, state, world)
                     and has_enough_slots("Abyss Lower Left - Torpedo Upgrade in Facility", 2, state, world))
                 or (state.has_all((buster, drill, missile), player) and has_fuel(13, state, world)
                     and has_enough_slots("Abyss Lower Left - Torpedo Upgrade in Facility", 3, state, world))
                 )

        add_rule(world.get_location("Abyss Lower Left - Fuel Tank in Facility Floor"),
                 # requires buster and depth
                 # buster + depth: 7/9
                 # all others look worse
                 rule=lambda state:
                 state.has_all((buster, depth_charge) and has_fuel(9, state, world)
                               and has_enough_slots("Abyss Lower Left - Fuel Tank in Facility Floor", 2, state, world)))

    add_rule(world.get_location("Porgy - Garden"),
             rule=lambda state: world.get_location("Porgy - Lamia").can_reach(state))

    add_rule(world.get_location("Porgy - Gold"),
             rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world))
    if "Porgy" in world.options.cherry_allowed_games:
        add_rule(world.get_location("Porgy - Cherry"),
                 rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world)
                 and state.has_all((depth_charge, drill), player)
                 and has_light(state, world))
