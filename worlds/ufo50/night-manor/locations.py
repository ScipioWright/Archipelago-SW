from typing import TYPE_CHECKING, Dict, NamedTuple
from BaseClasses import Location, Region, ItemClassification
from .items import NightManorItem

if TYPE_CHECKING:
    from .. import UFO50World


class NightManorLocation(Location):
    game: str = "UFO 50"


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str


ufo_50_base_id = 21061550_00_000  # reference it from wherever it is when there's an actual world class
night_manor_base_id = 42_000 + ufo_50_base_id


night_manor_location_table: Dict[str, LocationInfo] = {
    "Starting Room - Spoon": LocationInfo(0, "Manor - Starting Room"),
    "Starting Room - Bowl": LocationInfo(1, "Manor - Starting Room"),
    "Starting Room Vent - Yellow Note", LocationInfo(2, "Manor - Starting Room"),
    "Starting Room Vent - Hairpin", LocationInfo(3, "Manor - Starting Room")
    "Corpse Bathroom - Tweezers", LocationInfo(4, "Manor - First Floor"),
    "Guest Bedroom - Journal Entry 2", LocationInfo(5, "Manor - First Floor"),
    "Guest Bedroom - Journal Entry 5", LocationInfo(6, "Manor - First Floor"),
    "Guest Bedroom - Batteries", LocationInfo(7, "Manor - First Floor"),
    "Living Room - Journal Entry 1", LocationInfo(8, "Manor - First Floor"),


}


def create_night_manor_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in night_manor_location_table.items():
        loc = NightManorLocation(world.player, f"Night Manor - {loc_name}", night_manor_base_id + loc_data.id_offset,
                              regions[loc_data.region_name])
        regions[loc_data.region_name].locations.add(loc)
    victory_location = NightManorLocation(world.player, "Beat the Boss", None, regions["Boss Area"])
    victory_location.place_locked_item(NightManorItem("Night Manor - Victory", ItemClassification.progression, None,
                                                   world.player))
    regions["Boss Area"].locations.append(victory_location)
