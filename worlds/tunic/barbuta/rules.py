from typing import TYPE_CHECKING, Dict
from BaseClasses import Region

if TYPE_CHECKING:
    from .. import TunicWorld


def create_barbuta_rules(world: "TunicWorld", regions: Dict[str, Region]) -> None:
    # D4
    regions["D4"].connect(connecting_region=regions["D5"])

    regions["D4 Upper Right"].connect(connecting_region=regions["D5 Upper"])

    # D5, the starting room
    regions["D5"].connect(connecting_region=regions["D4"])
    regions["D5"].connect(connecting_region=regions["D6"])

    regions["D5 Upper"].connect(connecting_region=regions["D4 Upper Right"])
    regions["D5 Upper"].connect(connecting_region=regions["D6 Upper Left"])
