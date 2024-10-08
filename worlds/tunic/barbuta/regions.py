from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Region

from .rules import create_barbuta_rules

if TYPE_CHECKING:
    from .. import TunicWorld


# not sure if we really need this yet, but making it in case we need it later since it's easy to remove
class RegionInfo(NamedTuple):
    pass


# keys are region names, values are the region object
barbuta_region_info: Dict[str, RegionInfo] = {
    "A1": RegionInfo(),
    "A2": RegionInfo(),
    "A3": RegionInfo(),
    "A4": RegionInfo(),
    "A5": RegionInfo(),
    "A6": RegionInfo(),
    "A7": RegionInfo(),
    "A8": RegionInfo(),
    "B1": RegionInfo(),
    "B2": RegionInfo(),
    "B3": RegionInfo(),
    "B4": RegionInfo(),
    "B5": RegionInfo(),
    "B6": RegionInfo(),
    "B7": RegionInfo(),
    "B8": RegionInfo(),
    "C1": RegionInfo(),
    "C2": RegionInfo(),
    "C3": RegionInfo(),
    "C4": RegionInfo(),
    "C5": RegionInfo(),
    "C6": RegionInfo(),
    "C7": RegionInfo(),
    "C8": RegionInfo(),
    "D1": RegionInfo(),
    "D2": RegionInfo(),
    "D3": RegionInfo(),
    "D4": RegionInfo(),
    "D4 Upper Right": RegionInfo(),
    "D5": RegionInfo(),  # starting room
    "D5 Upper": RegionInfo(),
    "D6": RegionInfo(),
    "D6 Upper Left": RegionInfo(),
    "D7": RegionInfo(),
    "D8": RegionInfo(),
    "E1": RegionInfo(),
    "E2": RegionInfo(),
    "E3": RegionInfo(),
    "E4": RegionInfo(),
    "E5": RegionInfo(),
    "E6": RegionInfo(),
    "E7": RegionInfo(),
    "E8": RegionInfo(),
    "F1": RegionInfo(),
    "F2": RegionInfo(),
    "F3": RegionInfo(),
    "F4": RegionInfo(),
    "F5": RegionInfo(),
    "F6": RegionInfo(),
    "F7": RegionInfo(),
    "F8": RegionInfo(),
    "G1": RegionInfo(),
    "G2": RegionInfo(),
    "G3": RegionInfo(),
    "G4": RegionInfo(),
    "G5": RegionInfo(),
    "G6": RegionInfo(),
    "G7": RegionInfo(),
    "G8": RegionInfo(),
    "H1": RegionInfo(),
    "H2": RegionInfo(),
    "H3": RegionInfo(),
    "H4": RegionInfo(),
    "H5": RegionInfo(),
    "H6": RegionInfo(),
    "H7": RegionInfo(),
    "H8": RegionInfo(),
}


def create_barbuta_regions(world: "TunicWorld") -> None:
    barbuta_regions: Dict[str, Region] = {}
    for region_name, region_data in barbuta_region_info.items():
        barbuta_regions[region_name] = Region(f"Barbuta - {region_name}", world.player, world.multiworld)
    create_barbuta_rules(world, barbuta_regions)
