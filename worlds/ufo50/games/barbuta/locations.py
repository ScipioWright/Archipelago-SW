from typing import TYPE_CHECKING, Dict, NamedTuple, Set
from BaseClasses import Region, Location

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str


location_table: Dict[str, LocationInfo] = {
    "Green Skull - A1": LocationInfo(0, "Platforms above D4"),  # $100
    "Egg Shop - B6": LocationInfo(1, "Boss Area"),  # $100 each
    "Upper Shop Candy - C1": LocationInfo(2, "Platforms above D4"),  # costs $100
    "Upper Shop Umbrella - C1": LocationInfo(3, "Platforms above D4"),  # costs $50
    "Chest - C2": LocationInfo(4, "Platforms above D4"),  # Pin chest
    "Bat Altar - D1": LocationInfo(5, "Bat Altar"),  # bat noises
    "Coin - D4": LocationInfo(6, "Starting Area"),  # $50, breakable block
    "Little Guy Breaks a Wall - D7": LocationInfo(7, "C7 above Ladders"),  # costs $500
    "Chest - E3": LocationInfo(8, "Blood Sword Room"),  # omelette time
    "Chest - E5": LocationInfo(9, "Key Room"),  # I love climbing ladders
    "Chest - E8": LocationInfo(10, "F7 and Nearby"),  # $50
    "Green Skull - F2": LocationInfo(11, "Starting Area"),  # $100
    "Lower Shop Umbrella - F2": LocationInfo(12, "Starting Area"),  # costs $100
    "Lower Shop Trash - F2": LocationInfo(13, "Starting Area"),  # costs $50
    "Lower Shop Pin - F2": LocationInfo(14, "Starting Area"),  # costs $200
    "Chest - F3 Door": LocationInfo(15, "G3 and Nearby"),  # $100
    "Chest - F4": LocationInfo(16, "Starting Area"),  # Umbrella chest
    "Chest - F5": LocationInfo(17, "Starting Area"),  # $50
    "Chest - F6": LocationInfo(18, "F7 and Nearby"),  # $100
    "Chest - G2": LocationInfo(19, "Starting Area"),  # $50, requires pin
    "Chest - G5": LocationInfo(20, "Starting Area"),  # necklace chest
    "Chest - H5": LocationInfo(21, "Starting Area"),  # $100, be fast before the ledge breaks
    "Chest - H7": LocationInfo(22, "G7 and Nearby"),  # $50
    "Wand Trade - H7": LocationInfo(23, "Wand Trade Room"),  # probably should just have it give you the check

    "Garden": LocationInfo(997, "Boss Area"),
    "Gold": LocationInfo(998, "Menu"),
    "Cherry": LocationInfo(999, "Boss Area")
}


# this is for filling out location_name_to_id, it should be static regardless of yaml options
def get_locations() -> Dict[str, int]:
    return {name: data.id_offset + get_game_base_id("Barbuta") for name, data in location_table.items()}


# this should return the location groups for this game, independent of yaml options
# you should include a group that contains all location for this game that is called the same thing as the game
def get_location_groups() -> Dict[str, Set[str]]:
    location_groups: Dict[str, Set[str]] = {"Barbuta": {f"Barbuta - {loc_name}" for loc_name in location_table.keys()}}
    return location_groups


# this is not a required function, but a recommended one -- the world class does not call this function
def create_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        loc = Location(world.player, f"Barbuta - {loc_name}", get_game_base_id("Barbuta") + loc_data.id_offset,
                       regions[loc_data.region_name])
        regions[loc_data.region_name].locations.append(loc)
