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

    add_rule(world.get_location("Porgy - Garden"),
             rule=lambda state: world.get_location("Porgy - Lamia").can_reach(state))

    add_rule(world.get_location("Porgy - Gold"),
             rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world))
    if "Porgy" in world.options.cherry_allowed_games:
        add_rule(world.get_location("Porgy - Cherry"),
                 rule=lambda state: can_combat(26, state, player) and has_fuel(16, state, world)
                 and state.has_all((depth_charge, drill), player)
                 and has_light(state, world))
