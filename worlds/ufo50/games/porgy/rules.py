from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState, Location
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

ship_rocks = "Bombed Open the Ship"
urchin_rock = "Bombed the Buster Urchin Path Exit Rock"
leftmost_rock = "Bombed the Leftmost Abyss Entrance Rock"
second_left_rock = "Bombed the Second from Left Abyss Entrance Rock"
rightmost_rock = "Bombed the Rightmost Abyss Rock"


def get_porgy_location(name: str, world: "UFO50World") -> Location:
    return world.get_location(f"Porgy - {name}")


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
    abyss = loc_name == "Abyss Rock" or location_table[loc_name].region_name == "Abyss"
    hidden_status = Hidden.not_hidden if loc_name == "Abyss Rock" else location_table[loc_name].concealed
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
        loc = get_porgy_location(loc_name, world)
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
                                rule=lambda state: state.has("Porgy - Bomb Open the Ship", player))
    regions["Sunken Ship"].connect(regions["Sunken Ship - Buster"],
                                   rule=lambda state: state.has(buster, player))
    # vanilla seems to want you to have 8 torpedo upgrades, 2 fish friends, missiles, and buster before abyss
    regions["Deeper"].connect(regions["Abyss"],
                              rule=lambda state: has_light(state, world) and can_combat(16, state, player))

    # events
    add_rule(get_porgy_location("Sunken Ship", world),
             rule=lambda state: state.has(depth_charge, world.player)
             or (state.has(missile, world.player) and has_fuel(6, state, world)))

    add_rule(get_porgy_location("Rock at Buster Urchin Path", world),
             rule=lambda state: has_fuel(7, state, world)
             and (state.has_all((missile, buster), player) or state.has(depth_charge, player)))

    add_rule(get_porgy_location("Rock at Leftmost Abyss Entrance", world),
             rule=lambda state: has_fuel(7, state, world) and state.has(depth_charge, player))

    add_rule(get_porgy_location("Rock at Second from Left Abyss Entrance", world),
             rule=lambda state: (has_fuel(6, state, world) and state.has(depth_charge, player))
             or (has_fuel(7, state, world) and state.has(missile, player)))

    add_rule(get_porgy_location("Rightmost Abyss Rock", world),
             rule=lambda state: (has_fuel(8, state, world) and state.has(depth_charge, player))
             or (has_enough_slots("Abyss Rock", 2, state, world) and state.has(missile, player)
                 and (state.has(buster, player) and has_fuel(12, state, world)
                      or state.has(drill, player) and has_fuel(11, state, world))))

    # buster is covered by the region
    add_rule(get_porgy_location("Shallows Upper Mid - Fuel Tank in Floor at Surface", world),
             lambda state: state.has(depth_charge, player))

    add_rule(get_porgy_location("Deeper Upper Mid - Egg in Dirt", world),
             lambda state: state.has(drill, player))
    add_rule(get_porgy_location("Deeper Upper Mid - Spotlight Module", world),
             lambda state: state.has(depth_charge, player))
    add_rule(get_porgy_location("Deeper Lower Mid - Fuel Tank in Floor", world),
             lambda state: state.has(depth_charge, player))

    if check_on_touch:
        # shallows coral maze
        add_rule(get_porgy_location("Shallows Upper Right - Fuel Tank in Coral Maze", world),
                 rule=lambda state: has_fuel(7, state, world)
                 or (has_fuel(3, state, world) and state.has(drill, player)))
        add_rule(get_porgy_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze", world),
                 rule=lambda state: has_fuel(9, state, world)
                 or (has_fuel(5, state, world) and state.has(drill, player)))
        add_rule(get_porgy_location("Shallows Upper Right - Egg in Coral Maze", world),
                 rule=lambda state: has_fuel(11, state, world)
                 or (has_fuel(7, state, world) and state.has(drill, player)))

        # faster through the ship
        add_rule(get_porgy_location("Deeper Upper Left - Torpedo Upgrade in Wall", world),
                 rule=lambda state: has_fuel(4, state, world)
                 or (has_fuel(3, state, world) and state.has(depth_charge, player)))

        # abyss
        # unless noted otherwise, routes were added together using partial routes
        # recommended to get more accurate numbers over time
        add_rule(get_porgy_location("Abyss Upper Left - Egg on Seaweed near Urchins", world),
                 # go through the ship
                 rule=lambda state: state.has(depth_charge, player) and has_fuel(4, state, world)
                 # go around and through the dirt instead, less fuel than opening ship with missile
                 or state.has(drill, player) and has_fuel(5, state, world))

        add_rule(get_porgy_location("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", world),
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
        add_rule(get_porgy_location("Abyss Upper Left - Torpedo Upgrade in Seaweed", world),
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

        add_rule(get_porgy_location("Abyss Lower Left - Egg in Facility", world),
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

        add_rule(get_porgy_location("Abyss Lower Left - Torpedo Upgrade in Facility", world),
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

        add_rule(get_porgy_location("Abyss Lower Left - Fuel Tank in Facility Floor", world),
                 # requires buster and depth
                 # buster + depth: 7/9
                 # all others look worse
                 rule=lambda state:
                 state.has_all((buster, depth_charge) and has_fuel(7, state, world)
                               and has_enough_slots("Abyss Lower Left - Fuel Tank in Facility Floor", 2, state, world)))

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade in Wall", world),
                 # depth + drill: 3.375/6.75 (don't need to bring depth with for non-touch)
                 # drill only: 4.375/8.75
                 # drill + missile: x/7.75
                 # buster only: 4.75/9.5
                 # depth only: 4.75/9.5
                 rule=lambda state:
                 (has_fuel(4, state, world) and state.has_all((depth_charge, drill), player)
                  and has_enough_slots("Abyss Upper Mid - Torpedo Upgrade in Wall", 2, state, world))
                 or (has_fuel(5, state, world) and state.has_any((drill, buster, depth_charge), player)
                     and has_enough_slots("Abyss Upper Mid - Torpedo Upgrade in Wall", 1, state, world)))

        add_rule(get_porgy_location("Abyss Upper Mid - Efficient Fuel Module", world),
                 # depth + drill: 3.625/7.25
                 # depth only: 5.125/10.25
                 rule=lambda state: state.has(depth_charge, player)
                 and state.has_fuel(6, state, world)
                 or (state.has(drill, player) and has_fuel(4, state, world)
                     and has_enough_slots("Abyss Upper Mid - Efficient Fuel Module", 2, state, world))
                 )

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade in Cave", world),
                 # depth + drill: 4/8
                 # depth + drill + buster: same amount as depth + drill, so invalid
                 # drill + buster: 4/8
                 # drill + buster + missile (to pre-open rock, but only go down with drill): 7/8
                 # drill only: 5/10
                 rule=lambda state: state.has(drill, player)
                 and (has_enough_slots("Abyss Upper Mid - Torpedo Upgrade in Cave", 2, state, world)
                      and state.has_any((buster, depth_charge), player))
                 or has_fuel(5, state, world))

        add_rule(get_porgy_location("Abyss Upper Mid - Egg on Seaweed", world),
                 # depth only: 4.5/9
                 # buster only: 4.5/9
                 # drill only: 4.75/9.5
                 # drill + break second to left rock: x/7.5
                 rule=lambda state: has_fuel(5, state, world) and state.has_any((depth_charge, buster, drill), player))

        add_rule(get_porgy_location("Abyss Upper Mid - Egg in Seaweed", world),
                 # buster only: 4/8
                 # depth only: 4/8
                 # drill only: 5/10
                 # drill + break second to left rock: x/8
                 rule=lambda state:
                 (has_enough_slots("Abyss Upper Mid - Egg in Seaweed", 1, state, world)
                  and ((has_fuel(4, state, world) and state.has_any((depth_charge, buster), player))
                       or (has_fuel(5, state, world) and state.has(drill, player))))
                 or (state.has(urchin_rock, player)))

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade behind Seaweed", world),
                 # buster only: 4.25/8.5
                 # depth only: 4.25/8.5
                 # drill only: 5.25/10.5
                 rule=lambda state:
                 ((has_fuel(5, state, world) and state.has_any((depth_charge, buster), player))
                  or (has_fuel(6, state, world) and state.has(drill, player)))
                 or (state.has(urchin_rock, player)))

        add_rule(get_porgy_location("Abyss Upper Right - Egg by Seaweed", world),
                 # buster only: 4.75/9.5
                 # depth only: 7.75/15.5
                 # drill only: 4.5/9
                 rule=lambda state:
                 (has_fuel(5, state, world) and state.has_any((buster, drill), player))
                 or (has_fuel(8, state, world) and state.has(depth_charge, player)))

        add_rule(get_porgy_location("Abyss Lower Right - Fuel Tank in Floor", world),
                 # depth only: 4.5/9, and since it's required, this is the only viable path
                 rule=lambda state: state.has(depth_charge, player) and has_fuel(5, state, world))

        add_rule(get_porgy_location("Abyss Lower Right - Egg by Skull", world),
                 # depth only: 7/14
                 # drill only: 4.25/8.5
                 # buster only: 5.5/11
                 rule=lambda state:
                 (state.has(depth_charge, player) and has_fuel(7, state, world))
                 or (state.has(drill, player) and has_fuel(5, state, world))
                 or (state.has(buster, player) and has_fuel(6, state, world)))

        add_rule(get_porgy_location("Abyss Lower Right - Radar System Module", world),
                 # depth only: 6.5/12
                 # drill only: 5.5/10.25
                 rule=lambda state:
                 (state.has(depth_charge, player) and has_fuel(7, state, world))
                 or (state.has(drill, player) and has_fuel(6, state, world)))

        add_rule(get_porgy_location("Abyss Lower Right - Armor Plating Module", world),
                 # depth only: 5.5/11
                 # buster only: 5.625/11.25
                 # drill only: 5.375/10.75
                 rule=lambda state: state.has_any((depth_charge, drill, buster), player) and has_fuel(6, state, world))

    else:
        # shallows coral maze
        add_rule(get_porgy_location("Shallows Upper Right - Fuel Tank in Coral Maze", world),
                 rule=lambda state: has_fuel(13, state, world)
                 or (has_fuel(6, state, world) and state.has(drill, player)))
        add_rule(get_porgy_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze", world),
                 rule=lambda state: has_fuel(15, state, world)
                 or (has_fuel(8, state, world) and state.has(drill, player)))
        add_rule(get_porgy_location("Shallows Upper Right - Egg in Coral Maze", world),
                 rule=lambda state: has_fuel(16, state, world)
                 or (has_fuel(9, state, world) and state.has(drill, player)))

        # faster through the ship
        add_rule(get_porgy_location("Deeper Upper Left - Torpedo Upgrade in Wall", world),
                 rule=lambda state: has_fuel(8, state, world)
                 or (has_fuel(5, state, world) and state.has(depth_charge, player)))

        # abyss
        # unless noted otherwise, routes were added together using partial routes
        # recommended to get more accurate numbers over time
        add_rule(get_porgy_location("Abyss Upper Left - Egg on Seaweed near Urchins", world),
                 # I promise you this rule is correct, buster can't reach it
                 rule=lambda state: has_fuel(9, state, world) and state.has_any((depth_charge, drill), player))

        add_rule(get_porgy_location("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", world),
                 # see this check in the on touch section
                 rule=lambda state:
                 (has_fuel(8, state, world) and state.has(depth_charge, player))
                 or (has_fuel(8, state, world) and state.has_all((drill, missile, buster), player)
                     and has_enough_slots("Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade", 2, state, world))
                 or (has_fuel(9, state, world) and state.has_all((buster, missile), player))
                 or (has_fuel(10, state, world) and state.has(buster, player))
                 or (has_fuel(14, state, world) and state.has_all((drill, missile), player))
                 or (has_fuel(15, state, world) and state.has(drill, player)))
        add_rule(get_porgy_location("Abyss Upper Left - Torpedo Upgrade in Seaweed", world),
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

        add_rule(get_porgy_location("Abyss Lower Left - Egg in Facility", world),
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
        add_rule(get_porgy_location("Abyss Lower Left - Torpedo Upgrade in Facility", world),
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

        add_rule(get_porgy_location("Abyss Lower Left - Fuel Tank in Facility Floor", world),
                 # requires buster and depth
                 # buster + depth: 7/9
                 # all others look worse
                 rule=lambda state:
                 state.has_all((buster, depth_charge) and has_fuel(9, state, world)
                               and has_enough_slots("Abyss Lower Left - Fuel Tank in Facility Floor", 2, state, world)))

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade in Wall", world),
                 # depth + drill: 3.375/6.75 (don't need to bring depth with for non-touch)
                 # drill only: 4.375/8.75
                 # drill + missile: x/7.75 (don't need to bring missile for non-touch)
                 # buster only: 4.75/9.5
                 # depth only: 4.75/9.5
                 rule=lambda state: has_enough_slots("Abyss Upper Mid - Torpedo Upgrade in Wall", 1, state, world)
                 and ((state.has(drill, player)
                       and (state.has(depth_charge, player) and has_fuel(7, state, world))
                       or (state.has(missile, player) and has_fuel(8, state, world))
                       or (has_fuel(9, state, world)))
                      or (has_fuel(10, state, world) and state.has_any((buster, depth_charge), player)))
                 )

        add_rule(get_porgy_location("Abyss Upper Mid - Efficient Fuel Module", world),
                 # depth + drill: 3.625/7.25
                 # depth only: 5.125/10.25
                 rule=lambda state: state.has(depth_charge, player)
                 and state.has_fuel(11, state, world)
                 or (state.has(drill, player) and has_fuel(8, state, world)
                     and has_enough_slots("Abyss Upper Mid - Efficient Fuel Module", 2, state, world))
                 )

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade in Cave", world),
                 # depth + drill: 4/8
                 # depth + drill + buster: same amount as depth + drill, so invalid
                 # drill + buster: 4/8
                 # drill + buster + missile (to pre-open rock, but only go down with drill): 7/8
                 # drill only: 5/10
                 rule=lambda state: state.has(drill, player)
                 and (state.has(urchin_rock, player) and has_fuel(8, state, world))
                 or has_fuel(10, state, world))

        add_rule(get_porgy_location("Abyss Upper Mid - Egg on Seaweed", world),
                 # depth only: 4.5/9
                 # buster only: 4.5/9
                 # drill only: 4.75/9.5
                 # drill + break second to left rock: x/7.5
                 rule=lambda state:
                 (has_fuel(9, state, world) and state.has_any((depth_charge, buster), player))
                 or (state.has(drill, player)
                     and (has_fuel(10, state, world)
                          or (has_fuel(8, state, world)
                              and state.has(second_left_rock, player))))
                 )

        add_rule(get_porgy_location("Abyss Upper Mid - Egg in Seaweed", world),
                 # buster only: 4/8
                 # depth only: 4/8
                 # drill only: 5/10
                 # drill + break second to left rock: slower than breaking urchin path rock
                 rule=lambda state:
                 (has_fuel(8, state, world)
                  and (state.has(urchin_rock, player)
                       or (state.has(buster, player)
                           and has_enough_slots("Abyss Upper Mid - Egg in Seaweed", 1, state, world))))
                 or (has_fuel(10, state, world) and state.has(drill, player)))

        add_rule(get_porgy_location("Abyss Upper Mid - Torpedo Upgrade behind Seaweed", world),
                 # buster only: 4.25/8.5
                 # depth only: 4.25/8.5
                 # drill only: 5.25/10.5
                 # drill + break second to left rock: slower than breaking urchin path rock
                 rule=lambda state:
                 (has_fuel(9, state, world)
                  and (state.has(urchin_rock, player) or state.has(buster, player)))
                 or (has_fuel(11, state, world) and state.has(drill, player)))

        add_rule(get_porgy_location("Abyss Upper Right - Egg by Seaweed", world),
                 # buster only: 4.75/9.5
                 # depth only: 7.75/15.5
                 # drill only: 4.5/9
                 rule=lambda state:
                 (has_fuel(9, state, world) and state.has(drill, player))
                 or (has_fuel(10, state, world) and state.has(buster, player))
                 or (has_fuel(16, state, world) and state.has(depth_charge, player)))

        add_rule(get_porgy_location("Abyss Lower Right - Fuel Tank in Floor", world),
                 # depth only: 4.5/9, and since it's required, this is the only viable path
                 rule=lambda state: state.has(depth_charge, player) and has_fuel(9, state, world))

        add_rule(get_porgy_location("Abyss Lower Right - Egg by Skull", world),
                 # depth only: 7/14
                 # drill only: 4.25/8.5
                 # buster only: 5.5/11
                 rule=lambda state:
                 (state.has(rightmost_rock, player) and has_fuel(14, state, world))
                 or (state.has(drill, player) and has_fuel(9, state, world))
                 or (state.has(buster, player) and has_fuel(11, state, world)))

        add_rule(get_porgy_location("Abyss Lower Right - Radar System Module", world),
                 # depth only: 6.5/12
                 # drill only: 5.5/10.25
                 rule=lambda state:
                 (state.has(depth_charge, player) and has_fuel(12, state, world))
                 or (state.has(drill, player) and has_fuel(11, state, world)))

        add_rule(get_porgy_location("Abyss Lower Right - Armor Plating Module", world),
                 # depth only: 5.5/11
                 # buster only: 5.625/11.25
                 # drill only: 5.375/10.75
                 rule=lambda state:
                 (state.has_any((depth_charge, drill), player) and has_fuel(11, state, world))
                 or (state.has(buster, player) and has_fuel(12, state, world)))

    add_rule(get_porgy_location("Garden", world),
             rule=lambda state: get_porgy_location("Porgy - Lamia", world).can_reach(state))

    add_rule(get_porgy_location("Gold", world),
             rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world))
    if "Porgy" in world.options.cherry_allowed_games:
        add_rule(get_porgy_location("Cherry", world),
                 rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world)
                 and state.has_all((depth_charge, drill), player)
                 and has_light(state, world))
