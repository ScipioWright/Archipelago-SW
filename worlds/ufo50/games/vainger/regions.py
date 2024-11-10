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
    "Menu": RegionInfo(),

    "LatomR6C3 Genepod": RegionInfo(),
    "LatomR9C3 Genepod": RegionInfo(),
    "LatomR3C4 Genepod": RegionInfo(),
    "LatomR5C4 Genepod": RegionInfo(),
    "LatomR5C6 Genepod": RegionInfo(),
    "LatomR7C6 Genepod": RegionInfo(),
    "LatomR4C9 Genepod": RegionInfo(),
    "ThetaR4C1 Genepod": RegionInfo(),
    "ThetaR9C5 Genepod": RegionInfo(),
    "ThetaR5C6 Genepod": RegionInfo(),  # starting room genepod
    "ThetaR6C6 Genepod": RegionInfo(),
    "ThetaR7C9 Genepod": RegionInfo(),
    "ThetaR9C9 Genepod": RegionInfo(),
    "VerdeR1C1 Genepod": RegionInfo(),
    "VerdeR1C5 Genepod": RegionInfo(),
    "VerdeR6C5 Genepod": RegionInfo(),
    "VerdeR7C9 Genepod": RegionInfo(),
    "VerdeR9C9 Genepod": RegionInfo(),
    "Control Genepod": RegionInfo(),
    
    "LatomR6C4 Area": RegionInfo(),
    "VerdeSW Area": RegionInfo(),
    "VerdeR7C8 Location": RegionInfo(),
    "ThetaR8C3 Location": RegionInfo(),
    "ThetaR10C3 Location": RegionInfo()
}


def create_regions_and_rules(world: "UFO50World") -> Dict[str, Region]:
    vainger_regions: Dict[str, Region] = {}
    for region_name, region_data in region_info.items():
        vainger_regions[f"Vainger - {region_name}"] = Region(f"Vainger - {region_name}", world.player, world.multiworld)

    create_locations(world, vainger_regions)
    create_rules(world, vainger_regions)

    return vainger_regions
