from typing import TYPE_CHECKING, Dict, NamedTuple, Set
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.generic.Rules import add_rule

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str
    fuel_touch: int = 0  # how many tanks it took to get to the check
    fuel_get: int = 0  # how many tanks it took to get to the check and back to a base


location_table: Dict[str, LocationInfo] = {
    # Shallows
    "Shallows Upper Left - Ceiling Torpedo Upgrade": LocationInfo(0, "Shallows", 1, 2),
    "Shallows Lower Left - Fuel Tank between some Coral": LocationInfo(1, "Shallows", 1, 2),
    "Shallows Upper Left - Fuel Tank next to Coral": LocationInfo(2, "Shallows", 2, 3),
    "Shallows Lower Left - Fuel Tank above Breakable Rocks": LocationInfo(3, "Shallows - Missile"),  # missile todo amt
    "Shallows Upper Mid - Torpedo Upgrade at Surface": LocationInfo(4, "Shallows - Buster", 2, 4),  # buster
    "Shallows Upper Mid - Fuel Tank on Coral": LocationInfo(5, "Shallows", 1, 1),
    "Shallows Uppper Mid - Fuel Tank behind ! Blocks": LocationInfo(6, "Shallows - Buster", 2, 3),  # buster
    "Shallows Upper Mid - Egg at Surface": LocationInfo(7, "Shallows - Buster", 1, 2),  # buster
    "Shallows Upper Mid - Fuel Tank in Floor at Surface": LocationInfo(8, "Shallows - Buster", 1, 2),  # buster, depth
    "Shallows Mid - Torpedo Upgrade above Breakable Rocks": LocationInfo(9, "Shallows - Missile", 3, 5),  # missile
    # ship requires explosives to enter
    # using missiles, it requires 6 fuel tanks to open it and get back to base
    "Shallows Sunken Ship - Cargo Hold Egg": LocationInfo(10, "Sunken Ship", 2, 4),
    "Shallows Sunken Ship - Bow Egg": LocationInfo(11, "Sunken Ship - Buster", 2, 4),  # buster
    "Shallows Sunken Ship - Bow Torpedo Upgrade in Wall": LocationInfo(12, "Sunken Ship - Buster", 2, 4),  # buster
    "Shallows Sunken Ship - Depth Charge Module": LocationInfo(13, "Sunken Ship", 2, 4),
    "Shallows Lower Mid - Super Booster Module": LocationInfo(14, "Shallows", 3, 5),  # assumes light damage
    "Shallows Lower Mid - Fuel Tank on Coral": LocationInfo(15, "Shallows", 2, 4),
    "Shallows Lower Mid - Egg on Coral": LocationInfo(16, "Shallows", 3, 4),
    "Shallows Lower Mid - Lower Ceiling Torpedo Upgrade": LocationInfo(17, "Shallows - Missile", 2, 3),  # missile
    "Shallows Lower Mid - Upper Ceiling Torpedo Upgrade": LocationInfo(18, "Shallows", 1, 2),
    "Shallows Lower Mid - Fuel Tank in Floor": LocationInfo(19, "Shallows - Depth", 1, 2),  # depth
    "Shallows Lower Mid - Torpedo Upgrade on Coral": LocationInfo(20, "Shallows", 2, 3),
    "Shallows Upper Right - Fuel Tank under Breakable Rocks": LocationInfo(21, "Shallows - Depth", 2, 3),  # depth
    # 5.5 tanks to get from base to first maze block w/o drill, 2 tanks w/ drill
    # fuel tank: 6.5 to touch, 13 or 3 to touch w/ drill (tested), 6 w/ drill
    # torpedo: 8.5 to touch, 15 or 5 to touch w/ drill (tested), 8 w/ drill
    # egg: 10.5 to touch, 16 or 7 to touch w/ drill (tested), 9 to base w/ drill
    "Shallows Upper Right - Fuel Tank in Coral Maze": LocationInfo(22, "Shallows"),
    "Shallows Upper Right - Torpedo Upgrade in Coral Maze": LocationInfo(23, "Shallows"),
    "Shallows Upper Right - Egg in Coral Maze": LocationInfo(24, "Shallows"),

    "Shallows Lower Right - Fuel Tank under Breakable Rocks": LocationInfo(25, "Shallows - Depth", 3, 7),  # depth
    "Shallows Lower Right - Buster Torpedoes Module": LocationInfo(26, "Shallows", 2, 3),
    "Shallows Lower Right - Egg behind ! Blocks": LocationInfo(27, "Shallows - Buster", 2, 3),  # buster
    "Shallows Lower Right - Egg in Coral": LocationInfo(28, "Shallows - Buster", 3, 5),  # buster
    "Shallows Lower Right - Drill Module": LocationInfo(29, "Shallows - Buster", 3, 6),  # buster

    # Deeper
    # 1.75 from left base to non-boat deeper entrance
    # 1 from right base to deep entrance
    # from left base to boat depths entrance
    "Deeper Upper Left - Torpedo Upgrade in Wall": LocationInfo(30, "Deeper", 4, 8),  # 4 to touch, 8 total itemless
    "Deeper Upper Left - Egg by Urchins": LocationInfo(31, "Deeper", 4, 7),
    "Deeper Upper Left - Fuel Tank on Coral": LocationInfo(32, "Deeper", 4, 7),
    "Deeper Upper Left - Fuel Tank behind ! Blocks": LocationInfo(33, "Deeper", 4, 6),
    "Deeper Upper Mid - Torpedo Upgrade in Coral": LocationInfo(34, "Deeper", 3, 5),
    "Deeper Upper Mid - Torpedo Upgrade in Ceiling": LocationInfo(35, "Deeper", 3, 6),
    "Deeper Upper Mid - Egg in Dirt": LocationInfo(36, "Deeper", 3, 5),  # drill
    "Deeper Upper Mid - Spotlight Module": LocationInfo(37, "Deeper", 3, 5),  # depth
    "Deeper Upper Mid - Fuel Tank in Collapsed Structure": LocationInfo(38, "Deeper", 2, 5),
    "Deeper Upper Right - Fuel Tank in Collapsed Structure": LocationInfo(39, "Deeper", 3, 5),
    "Deeper Upper Right - Egg on Coral": LocationInfo(40, "Deeper", 4, 7),  # about the same speed with drill
    "Deeper Upper Right - Torpedo Upgrade in Wall": LocationInfo(41, "Deeper", 3, 5),
    "Deeper Right - Torpedo Upgrade on Coral": LocationInfo(42, "Deeper", 5, 8),  # same speed to blow up rocks
    "Deeper Upper Right - Targeting System Module": LocationInfo(43, "Deeper", 5, 9),
    "Deeper Lower Right - Egg behind Urchins": LocationInfo(44, "Deeper", 3, 5),
    "Deeper Lower Right - Fuel Tank in Ceiling": LocationInfo(45, "Deeper", 5, 8),
    "Deeper Lower Right - Egg on Coral": LocationInfo(46, "Deeper", 5, 8),
    "Deeper Lower Mid - Missile System Module": LocationInfo(47, "Deeper", 3, 6),
    "Deeper Lower Mid - Torpedo Upgrade on Coral": LocationInfo(48, "Deeper", 4, 7),
    "Deeper Lower Mid - Fuel Tank in Floor": LocationInfo(49, "Deeper", 4, 7),  # depth
    "Deeper Lower Left - Egg in Wall": LocationInfo(50, "Deeper", 4, 7),

    # Abyss
    # Routes to the Abyss:
    # Break rocks above abyss C: 3 tanks + buster + missile, or 3 tanks + depth
    # BCD = 3.5 tanks
    # BCC (via urchin maze) = 3.5 tanks
    # BCC (via bombed rock) = 3.5 tanks
    "Abyss Upper Left - Egg on Seaweed near Urchins": LocationInfo(51, "Abyss"),
    "Abyss Upper Left - Fuel Tank on Seaweed": LocationInfo(52, "Abyss"),
    "Abyss Upper Left - Egg on Seaweed above Torpedo Upgrade": LocationInfo(53, "Abyss"),
    "Abyss Upper Left - Torpedo Upgrade in Seaweed": LocationInfo(54, "Abyss"),
    "Abyss Lower Left - Egg in Facility": LocationInfo(55, "Abyss"),
    "Abyss Lower Left - Torpedo Upgrade in Facility": LocationInfo(56, "Abyss"),
    "Abyss Lower Left - Fuel Tank in Facility Floor": LocationInfo(57, "Abyss"),
    "Abyss Upper Mid - Torpedo Upgrade in Wall": LocationInfo(58, "Abyss"),
    "Abyss Upper Mid - Torpedo Upgrade in Cave": LocationInfo(59, "Abyss"),
    "Abyss Upper Mid - Egg on Seaweed": LocationInfo(60, "Abyss"),
    "Abyss Upper Mid - Efficient Fuel Module": LocationInfo(61, "Abyss"),
    "Abyss Upper Mid - Egg in Seaweed": LocationInfo(62, "Abyss"),  # 4 to touch, 9 to base w/ bomb,
    "Abyss Upper Mid - Torpedo Upgrade behind Seaweed": LocationInfo(63, "Abyss"),
    "Abyss Upper Right - Egg by Seaweed": LocationInfo(64, "Abyss"),
    "Abyss Upper Right - Torpedo Upgrade in Wall": LocationInfo(65, "Abyss"),
    "Abyss Lower Right - Fuel Tank in Floor": LocationInfo(66, "Abyss"),
    "Abyss Lower Right - Egg": LocationInfo(67, "Abyss"),
    "Abyss Lower Right - Radar System Module": LocationInfo(68, "Abyss"),
    "Abyss Lower Right - Armor Plating Module": LocationInfo(69, "Abyss"),

    # Bosses
    # combat logic is weird cause you can save damage done to a boss
    # my gut says 7 fuel, 5 torpedo upgrades OR 5 fuel and depth charges for the first two bosses
    "Lamia": LocationInfo(100, "Shallows"),  # shark
    "Iku Turso": LocationInfo(101, "Shallows"),  # octopus
    # 10 fuel, 8 torpedo upgrades, missile module or burst OR 8 fuel and depth charges for the second two bosses
    "Bakunawa": LocationInfo(102, "Deeper"),  # moray eel
    "Neptune": LocationInfo(103, "Deeper"),  # nautilus

    # 13 fuel, 12 torpedo upgrades, missile module, burst OR 13 fuel and depth charges
    "Dracula": LocationInfo(104, "Abyss"),  # squid-thing

    "Garden": LocationInfo(997, "Menu"),
    "Gold": LocationInfo(998, "Abyss"),
    "Cherry": LocationInfo(999, "Boss Area")
}


# this is for filling out location_name_to_id, it should be static regardless of yaml options
def get_locations() -> Dict[str, int]:
    return {f"Porgy - {name}": data.id_offset + get_game_base_id("Porgy") for name, data in location_table.items()}


# this should return the location groups for this game, independent of yaml options
# you should include a group that contains all location for this game that is called the same thing as the game
def get_location_groups() -> Dict[str, Set[str]]:
    location_groups: Dict[str, Set[str]] = {"Porgy": {f"Porgy - {loc_name}" for loc_name in location_table.keys()}}
    return location_groups


# this is not a required function, but a recommended one -- the world class does not call this function
def create_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        if loc_name == "Cherry" and "Porgy" not in world.options.cherry_allowed_games:
            break
        if loc_name in ["Gold", "Cherry"] and "Porgy" in world.goal_games:
            if (loc_name == "Gold" and "Porgy" not in world.options.cherry_allowed_games) or loc_name == "Cherry":
                loc = Location(world.player, f"Porgy - {loc_name}", None, regions[loc_data.region_name])
                loc.place_locked_item(Item("Completed Porgy", ItemClassification.progression, None, world.player))
                add_rule(world.get_location("Completed All Games"), lambda state: state.has("Completed Porgy", world.player))
                regions[loc_data.region_name].locations.append(loc)
                break

        loc = Location(world.player, f"Porgy - {loc_name}", get_game_base_id("Porgy") + loc_data.id_offset,
                       regions[loc_data.region_name])
        regions[loc_data.region_name].locations.append(loc)
