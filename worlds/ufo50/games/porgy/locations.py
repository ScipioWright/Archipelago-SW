from typing import TYPE_CHECKING, Dict, NamedTuple, Set
from BaseClasses import Region, Location, Item, ItemClassification
from worlds.generic.Rules import add_rule

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str
    fuel_tanks: int = 0  # how many tanks it took to get there and back to a base


location_table: Dict[str, LocationInfo] = {
    # Shallows
    "Shallows Upper Left - Ceiling Missile Upgrade": LocationInfo(0, "Shallows"),
    "Shallows Lower Left - Fuel Tank between some Coral": LocationInfo(1, "Shallows"),
    "Shallows Upper Left - Fuel Tank next to Coral": LocationInfo(2, "Shallows"),
    "Shallows Lower Left - Fuel Tank above Breakable Rocks": LocationInfo(3, "Shallows"),
    "Shallows Upper Mid - Missile Upgrade at Surface": LocationInfo(4, "Shallows"),
    "Shallows Upper Mid - Fuel Tank on Coral": LocationInfo(5, "Shallows"),
    "Shallows Uppper Mid - Fuel Tank behind ! Blocks": LocationInfo(6, "Shallows"),
    "Shallows Upper Mid - Egg on Coral": LocationInfo(7, "Shallows"),
    "Shallows Upper Mid - Fuel Tank in Floor": LocationInfo(8, "Shallows"),
    "Shallows Mid - Missile Upgrade above Breakable Rocks": LocationInfo(9, "Shallows"),
    "Shallows Sunken Ship - Cargo Hold Egg": LocationInfo(10, "Shallows"),
    "Shallows Sunken Ship - Bow Egg": LocationInfo(11, "Shallows"),
    "Shallows Sunken Ship - Bow Hidden Missile Upgrade": LocationInfo(12, "Shallows"),
    "Shallows Sunken Ship - Depth Charge Module": LocationInfo(13, "Shallows"),
    "Shallows Lower Mid - Super Booster Module": LocationInfo(14, "Shallows"),
    "Shallows Lower Mid - Fuel Tank on Coral": LocationInfo(15, "Shallows"),
    "Shallows Lower Mid - Egg on Coral": LocationInfo(16, "Shallows"),
    "Shallows Lower Mid - Lower Ceiling Missile Upgrade": LocationInfo(17, "Shallows"),
    "Shallows Lower Mid - Upper Ceiling Missile Upgrade": LocationInfo(18, "Shallows"),
    "Shallows Lower Mid - Fuel Tank in Floor": LocationInfo(19, "Shallows"),
    "Shallows Lower Mid - Missile Upgrade on Coral": LocationInfo(20, "Shallows"),
    "Shallows Upper Right - Fuel Tank under Breakable Rocks": LocationInfo(21, "Shallows"),
    "Shallows Upper Right - Fuel Tank in Coral Maze": LocationInfo(22, "Shallows"),
    "Shallows Upper Right - Missile Upgrade in Coral Maze": LocationInfo(23, "Shallows"),
    "Shallows Upper Right - Egg in Coral Maze": LocationInfo(24, "Shallows"),
    "Shallows Lower Right - Fuel Tank under Breakable Rocks": LocationInfo(25, "Shallows"),
    "Shallows Lower Right - Buster Torpedoes Module": LocationInfo(26, "Shallows"),
    "Shallows Lower Right - Egg behind ! Blocks": LocationInfo(27, "Shallows"),
    "Shallows Lower Right - Egg in Coral": LocationInfo(28, "Shallows"),
    "Shallows Lower Right - Drill Module": LocationInfo(29, "Shallows"),
    # todo: bosses

    # Deeper
    "Deeper Upper Left - Missile Upgrade in Wall": LocationInfo(30, "Deeper"),
    "Deeper Upper Left - Egg by Urchins": LocationInfo(31, "Deeper"),
    "Deeper Upper Left - Fuel Tank on Coral": LocationInfo(32, "Deeper"),
    "Deeper Upper Left - Fuel Tank behind ! Blocks": LocationInfo(33, "Deeper"),
    "Deeper Upper Mid - Missile Upgrade on Coral": LocationInfo(34, "Deeper"),
    "Deeper Upper Mid - Missile Upgrade in Ceiling": LocationInfo(35, "Deeper"),
    "Deeper Upper Mid - Egg in Dirt": LocationInfo(36, "Deeper"),
    "Deeper Upper Mid - Spotlight Module": LocationInfo(37, "Deeper"),
    "Deeper Upper Mid - Fuel Tank in Collapsed Structure": LocationInfo(38, "Deeper"),
    "Deeper Upper Right - Fuel Tank in Collapsed Structure": LocationInfo(39, "Deeper"),
    "Deeper Upper Right - Egg on Coral": LocationInfo(40, "Deeper"),
    "Deeper Upper Right - Missile Upgrade in Wall": LocationInfo(41, "Deeper"),
    "Deeper Right - Missile Upgrade on Coral": LocationInfo(42, "Deeper"),
    "Deeper Upper Right - Targeting System Module": LocationInfo(43, "Deeper"),
    "Deeper Lower Right - Egg behind Urchins": LocationInfo(44, "Deeper"),
    "Deeper Lower Right - Fuel Tank in Ceiling": LocationInfo(45, "Deeper"),
    "Deeper Lower Right - Egg on Coral": LocationInfo(46, "Deeper"),
    "Deeper Lower Mid - Missile System Module": LocationInfo(47, "Deeper"),
    "Deeper Lower Mid - Missile Upgrade on Coral": LocationInfo(48, "Deeper"),
    "Deeper Lower Mid - Fuel Tank in Floor": LocationInfo(49, "Deeper"),
    "Deeper Lower Left - Egg in Wall": LocationInfo(50, "Deeper"),

    # Abyss
    "Abyss Upper Left - Egg on Seaweed near Urchins": LocationInfo(47, "Abyss"),
    "Abyss Upper Left - Fuel Tank on Seaweed": LocationInfo(48, "Abyss"),
    "Abyss Upper Left - Egg on Seaweed above Missile Upgrade": LocationInfo(49, "Abyss"),
    "Abyss Upper Left - Missile Upgrade in Seaweed": LocationInfo(50, "Abyss"),
    "Abyss Lower Left - Egg in Facility": LocationInfo(51, "Abyss"),
    "Abyss Lower Left - Missile Upgrade in Facility": LocationInfo(52, "Abyss"),
    "Abyss Lower Left - Fuel Tank in Facility Floor": LocationInfo(53, "Abyss"),
    "Abyss Upper Mid - Missile Upgrade in Wall": LocationInfo(54, "Abyss"),
    "Abyss Upper Mid - Missile Upgrade in Cave": LocationInfo(55, "Abyss"),
    "Abyss Upper Mid - Egg on Seaweed": LocationInfo(56, "Abyss"),
    "Abyss Upper Mid - Efficient Fuel Module": LocationInfo(57, "Abyss"),
    "Abyss Upper Mid - Egg in Seaweed": LocationInfo(58, "Abyss"),
    "Abyss Upper Mid - Missile Upgrade behind Seaweed": LocationInfo(59, "Abyss"),
    "Abyss Upper Right - Egg by Seaweed": LocationInfo(60, "Abyss"),
    "Abyss Upper Right - Missile Upgrade in Wall": LocationInfo(61, "Abyss"),
    "Abyss Lower Right - Fuel Tank in Floor": LocationInfo(62, "Abyss"),
    "Abyss Lower Right - Egg": LocationInfo(63, "Abyss"),
    "Abyss Lower Right - Radar System Module": LocationInfo(64, "Abyss"),
    "Abyss Lower Right - Armor Plating Module": LocationInfo(65, "Abyss"),

    "Garden": LocationInfo(997, "Menu"),
    "Gold": LocationInfo(998, "Boss Area"),
    "Cherry": LocationInfo(999, "Boss Area")
}


# this is for filling out location_name_to_id, it should be static regardless of yaml options
def get_locations() -> Dict[str, int]:
    return {f"Barbuta - {name}": data.id_offset + get_game_base_id("Barbuta") for name, data in location_table.items()}


# this should return the location groups for this game, independent of yaml options
# you should include a group that contains all location for this game that is called the same thing as the game
def get_location_groups() -> Dict[str, Set[str]]:
    location_groups: Dict[str, Set[str]] = {"Barbuta": {f"Barbuta - {loc_name}" for loc_name in location_table.keys()}}
    return location_groups


# this is not a required function, but a recommended one -- the world class does not call this function
def create_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        if loc_name in ["Gold", "Cherry"] and "Barbuta" in world.goal_games:
            if (loc_name == "Gold" and "Barbuta" not in world.options.cherry_allowed_games) or loc_name == "Cherry":
                loc = Location(world.player, f"Barbuta - {loc_name}", None, regions[loc_data.region_name])
                loc.place_locked_item(Item("Completed Barbuta", ItemClassification.progression, None, world.player))
                add_rule(world.get_location("Completed All Games"), lambda state: state.has("Completed Barbuta", world.player))
                regions[loc_data.region_name].locations.append(loc)
                break

        loc = Location(world.player, f"Barbuta - {loc_name}", get_game_base_id("Barbuta") + loc_data.id_offset,
                       regions[loc_data.region_name])
        regions[loc_data.region_name].locations.append(loc)
