from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState

if TYPE_CHECKING:
    from .. import TunicWorld


def create_barbuta_rules(world: "TunicWorld", regions: Dict[str, Region]) -> None:
    player = world.player
    regions["Starting Area"].connect(regions["Key Room"])
    regions["Starting Area"].connect(regions["Platforms above D4"], rule=lambda state: state.has("Necklace", player))
    regions["Starting Area"].connect(regions["Blood Sword Room"]),
    # pin via G2, umbrella via H3
    regions["Starting Area"].connect(regions["G3 and Nearby"],
                                     rule=lambda state: state.has_any(("Pin", "Umbrella"), player))
    regions["Starting Area"].connect(regions["F7 and Nearby"],
                                     rule=lambda state: state.has("Pin", player)),

    regions["Platforms above D4"].connect(regions["Bat Altar"])  # drop down off the left side
    regions["Platforms above D4"].connect(regions["Above Entrance"])  # drop down off right side, need to break blocks

    regions["Above Entrance"].connect(regions["Wand Trade Room"])  # walk through the fake wall after using the door
