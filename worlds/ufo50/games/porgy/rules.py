from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState, Location
from worlds.generic.Rules import set_rule, add_rule

from .locations import location_table
from ...options import PorgyFuelDifficulty

if TYPE_CHECKING:
    from ... import UFO50World


fuel = "Porgy - Fuel Tank"
egg = "Porgy - Fish Gratitude"
torpedo = "Porgy - Torpedo Upgrade"
buster = "Porgy - Buster Torpedoes Module"
missile = "Porgy - Missile System Module"
depth_charge = "Porgy - Depth Charge Module"
spotlight = "Porgy - Spotlight Module"
drill = "Porgy - Drill Module"


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


# set the basic fuel requirements for spots that don't have multiple viable routes
def set_fuel_reqs(world: "UFO50World", on_touch: bool) -> None:
    for loc_name, loc_data in location_table.items():
        fuel_needed = loc_data.fuel_touch if on_touch else loc_data.fuel_get
        # if it is not set, it means it has some special requirements
        if not fuel_needed:
            continue
        set_rule(world.get_location(loc_name), lambda state, amt=fuel_needed: has_fuel(amt, state, world))


def create_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player
    check_on_touch = bool(world.options.porgy_check_on_touch)
    set_fuel_reqs(world, check_on_touch)

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
    # todo: some level of combat logic
    regions["Deeper"].connect(regions["Abyss"],
                              rule=lambda state: has_light(state, world))

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
        set_rule(world.get_location("Shallows Upper Right - Fuel Tank in Coral Maze"),
                 rule=lambda state: has_fuel(7, state, world)
                 or (has_fuel(3, state, world) and state.has(drill, player)))
        set_rule(world.get_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze"),
                 rule=lambda state: has_fuel(9, state, world)
                 or (has_fuel(5, state, world) and state.has(drill, player)))
        set_rule(world.get_location("Shallows Upper Right - Egg in Coral Maze"),
                 rule=lambda state: has_fuel(11, state, world)
                 or (has_fuel(7, state, world) and state.has(drill, player)))
    else:
        # shallows coral maze
        set_rule(world.get_location("Shallows Upper Right - Fuel Tank in Coral Maze"),
                 rule=lambda state: has_fuel(13, state, world)
                 or (has_fuel(6, state, world) and state.has(drill, player)))
        set_rule(world.get_location("Shallows Upper Right - Torpedo Upgrade in Coral Maze"),
                 rule=lambda state: has_fuel(15, state, world)
                 or (has_fuel(8, state, world) and state.has(drill, player)))
        set_rule(world.get_location("Shallows Upper Right - Egg in Coral Maze"),
                 rule=lambda state: has_fuel(16, state, world)
                 or (has_fuel(9, state, world) and state.has(drill, player)))



    set_rule(world.get_location("Barbuta - Garden"),
             rule=lambda state: state.has_any((pin, necklace), player))
    set_rule(world.get_location("Barbuta - Gold"),
             rule=lambda state: state.has_any((blood_sword, bat_orb), player) or has_wand(state, player))
    if "Porgy" in world.options.cherry_allowed_games:
        set_rule(world.get_location("Barbuta - Cherry"),
                 rule=lambda state: state.has(bat_orb, player)
                 and (state.has(blood_sword, player) or has_wand(state, player)))
