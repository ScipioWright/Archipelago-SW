from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from .. import UFO50World


spoon = "Night Manor - Spoon"
bowl = "Night Manor - Bowl"
hairpin = "Night Manor - Hairpin"



def create_night_manor_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player
    regions["Starting Room"].connect(regions["First Hallway"],
                                     rule=lambda state: state.has(hairpin, player))
    
