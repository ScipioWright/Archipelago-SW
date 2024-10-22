from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Region

from .locations import create_night_manor_locations
from .rules import create_night_manor_rules

if TYPE_CHECKING:
    from .. import UFO50World


# not sure if we really need this yet, but making it in case we need it later since it's easy to remove
class RegionInfo(NamedTuple):
    pass


# keys are region names, values are the region object
# for room names, the letter is the row (top to bottom), the number is the column (left to right)
night_manor_region_info: Dict[str, RegionInfo] = {
    "Starting Room": RegionInfo(), # the initial room the game starts in
    "First Floor & Exterior": RegionInfo(), # the floor accessible immediately after you exit the starting area
    "Second Floor": RegionInfo(), # second floor accessible after you get powered flashlight
    "Shed": RegionInfo(), #shed accessible after you get copper key
    "Master Bedroom": RegionInfo(), #master bedroom accessible after you get gold key
    "Maze": RegionInfo(), #maze accessible after you get 4 gems
    "Basement": RegionInfo() #accessible after you get the iron key
}


def create_night_manor_regions_and_rules(world: "UFO50World") -> None:
    night_manor_regions: Dict[str, Region] = {}
    for region_name, region_data in night_manor_region_info.items():
        night_manor_regions[region_name] = Region(
            f"Night Manor - {region_name}", world.player, world.multiworld)

    create_night_manor_locations(world, night_manor_regions)
    create_night_manor_rules(world, night_manor_regions)

    for region in night_manor_regions.values():
        world.multiworld.regions.append(region)
