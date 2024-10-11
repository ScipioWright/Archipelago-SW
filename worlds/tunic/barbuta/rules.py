from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState

if TYPE_CHECKING:
    from .. import TunicWorld


def has_money(amount: int, state: CollectionState, player: int) -> bool:
    # count the value of the money items
    pass


def create_barbuta_rules(world: "TunicWorld", regions: Dict[str, Region]) -> None:
    player = world.player
    regions["Starting Area"].connect(regions["Key Room"])
    regions["Starting Area"].connect(regions["Platforms above D4"],
                                     rule=lambda state: state.has("Necklace", player))
    regions["Starting Area"].connect(regions["Blood Sword Room"])
    # pin via G2, umbrella via H3
    regions["Starting Area"].connect(regions["G3 and Nearby"],
                                     rule=lambda state: state.has_any(("Pin", "Umbrella"), player))
    regions["Starting Area"].connect(regions["F7 and Nearby"],
                                     rule=lambda state: state.has("Pin", player))
    regions["Starting Area"].connect(regions["Mimic Room"])
    regions["Starting Area"].connect(regions["C7 above Ladders"],
                                     rule=lambda state: state.has("Candy", player))

    regions["Platforms above D4"].connect(regions["Bat Altar"])  # drop down off the left side
    regions["Platforms above D4"].connect(regions["Above Entrance"])  # drop down off right side, need to break blocks
    regions["Platforms above D4"].connect(regions["Boss Area"],
                                          rule=lambda state: state.has("Barbuta Key", player))

    regions["Above Entrance"].connect(regions["Wand Trade Room"])  # walk through the fake wall after using the door

    regions["G7 and Nearby"].connect(regions["Wand Trade Room"],
                                     rule=lambda state: state.has("Pin", player))

    regions["Wand Trade Room"].connect(regions["G7 and Nearby"],
                                       rule=lambda state: state.has("Pin", player))

    regions["C7 above Ladders"].connect(regions["Boss Area"],
                                        rule=lambda state: has_money(500, state, player))
