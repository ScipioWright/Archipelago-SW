from typing import Dict, NamedTuple, TYPE_CHECKING
from BaseClasses import Region

from .locations import create_locations
from .rules import create_rules

if TYPE_CHECKING:
    from ... import UFO50World

# adapted from Barbuta, thanks Scipio! <3

class RegionInfo(NamedTuple):
    pass


# using genepods as the main regions instead of rooms/entrances to avoid having to use
# state logic to deal with conflicting mod allocations and damage tracking. basing everything 
# on genepods guarantees the player can recharge and alter their configuration between legs
# of logic. item rules will be based on getting to the item and back using at most two clones.
#
# the letter is the column (left to right), the number is the row (top to bottom)
# based on a map at https://steamcommunity.com/sharedfiles/filedetails/?id=3341323146
# except numbering each sector from 1 to 10.
region_info: Dict[str, RegionInfo] = {
    "LatomC6 Genepod": RegionInfo(),
    "LatomC9 Genepod": RegionInfo(),
    "LatomD3 Genepod": RegionInfo(),
    "LatomD5 Genepod": RegionInfo(),
    "LatomF5 Genepod": RegionInfo(),
    "LatomF7 Genepod": RegionInfo(),
    "LatomI4 Genepod": RegionInfo(),
    "ThetaA4 Genepod": RegionInfo(),
    "ThetaE9 Genepod": RegionInfo(),
    "ThetaF5 Genepod": RegionInfo(), # starting room genepod
    "ThetaF6 Genepod": RegionInfo(),
    "ThetaI7 Genepod": RegionInfo(),
    "ThetaI9 Genepod": RegionInfo(),
    "VerdeA1 Genepod": RegionInfo(),
    "VerdeE1 Genepod": RegionInfo(),
    "VerdeE6 Genepod": RegionInfo(),
    "VerdeI7 Genepod": RegionInfo(),
    "VerdeI9 Genepod": RegionInfo(),
    "Control Genepod": RegionInfo(),
    
    "LatomD6 Area": RegionInfo(),
    "VerdeSW Area": RegionInfo(),
    "VerdeH7 Location": RegionInfo(),
    "ThetaC8 Location": RegionInfo(),
    "ThetaC10 Location": RegionInfo()
}


def create_regions_and_rules(world: "UFO50World", base_id: int) -> Dict[str, Region]:
    vainger_regions: Dict[str, Region] = {}
    for region_name, region_data in region_info.items():
        vainger_regions[region_name] = Region(f"Vainger - {region_name}", world.player, world.multiworld)

    create_locations(world, vainger_regions, base_id)
    create_rules(world, vainger_regions)

    return vainger_regions
