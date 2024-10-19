from typing import Dict, NamedTuple, TYPE_CHECKING, List
from BaseClasses import Region

from .locations import create_locations
from .rules import create_rules

if TYPE_CHECKING:
    from ... import UFO50World


# not sure if we really need this yet, but making it in case we need it later since it's easy to remove
class RegionInfo(NamedTuple):
    rooms: List[str] = []  # rooms this region contains, for the purpose of the garden prize access rule


# keys are region names, values are the region object
# for room names, the letter is the row (top to bottom), the number is the column (left to right)
region_info: Dict[str, RegionInfo] = {
    "Menu": RegionInfo(),  # the non-existent start menu
    "Starting Area": RegionInfo(),
    "Key Room": RegionInfo(),  # the room with the key, where you can access the key
    "Platforms above D4": RegionInfo(),  # the "first" moving platforms
    "Blood Sword Room": RegionInfo(),  # E3, probably unnecessary unless we randomize switches
    "G3 and Nearby": RegionInfo(),  # idk what to call this, it's up the poison ladder and right of some balls
    "F7 and Nearby": RegionInfo(),  # lots of purple blocks here
    "Bat Altar": RegionInfo(),  # the altar at D1 and the room next to it at D2
    "Above Entrance": RegionInfo(),  # in the sign
    "Wand Trade Room": RegionInfo(),  # where you trade your sword for a wand
    "G7 and Nearby": RegionInfo(),  # down where the shield guys are, need pin to get to wand
    "Mimic Room": RegionInfo(),  # H1, where the mimic is
    "Boss Area": RegionInfo(),  # B6, point of no return unless you paid $500 to break a wall
    "C7 above Ladders": RegionInfo(),  # C7, up by the little guy who breaks the wall
}


def create_regions_and_rules(world: "UFO50World") -> Dict[str, Region]:
    barbuta_regions: Dict[str, Region] = {}
    for region_name, region_data in region_info.items():
        barbuta_regions[region_name] = Region(f"Barbuta - {region_name}", world.player, world.multiworld)

    create_locations(world, barbuta_regions)
    create_rules(world, barbuta_regions)

    return barbuta_regions
