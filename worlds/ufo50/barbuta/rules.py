from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from .. import UFO50World


# count the value of the money items
def has_money(amount: int, state: CollectionState, player: int) -> bool:
    current_money = state.count("Barbuta - $100", player) * 100
    if current_money >= amount:
        return True
    current_money += state.count("Barbuta - $50", player) * 50
    if current_money >= amount:
        return True
    return False


pin = "Barbuta - Pin"
umbrella = "Barbuta - Umbrella"
necklace = "Barbuta - Necklace"
candy = "Barbuta - Candy"
key = "Barbuta - Key"
blood_sword = "Barbuta - Blood Sword"
broken_wall = "Barbuta - A Broken Wall"
wand = "Barbuta - Wand"
bat_orb = "Barbuta - Bat Orb"


def create_barbuta_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player
    regions["Starting Area"].connect(regions["Key Room"])
    regions["Starting Area"].connect(regions["Platforms above D4"],
                                     rule=lambda state: state.has(necklace, player))
    regions["Starting Area"].connect(regions["Blood Sword Room"])
    # pin via G2, umbrella via H3
    regions["Starting Area"].connect(regions["G3 and Nearby"],
                                     rule=lambda state: state.has_any((pin, umbrella), player))
    regions["Starting Area"].connect(regions["F7 and Nearby"],
                                     rule=lambda state: state.has(pin, player))
    regions["Starting Area"].connect(regions["Mimic Room"],
                                     rule=lambda state: state.has(wand, player))
    regions["Starting Area"].connect(regions["C7 above Ladders"],
                                     rule=lambda state: state.has(candy, player))

    regions["Platforms above D4"].connect(regions["Bat Altar"])  # drop down off the left side
    regions["Platforms above D4"].connect(regions["Above Entrance"])  # drop down off right side, need to break blocks
    regions["Platforms above D4"].connect(regions["Boss Area"],
                                          rule=lambda state: state.has(key, player))

    regions["Above Entrance"].connect(regions["Wand Trade Room"])  # walk through the fake wall after using the door

    regions["G7 and Nearby"].connect(regions["Wand Trade Room"],
                                     rule=lambda state: state.has(pin, player))

    regions["Wand Trade Room"].connect(regions["G7 and Nearby"],
                                       rule=lambda state: state.has(pin, player))

    regions["C7 above Ladders"].connect(regions["Boss Area"],
                                        rule=lambda state: state.has(broken_wall, player))

    regions["Mimic Room"].connect(regions["Boss Area"])

    set_rule(world.get_location("Barbuta - Chest - G2"),
             rule=lambda state: state.has(pin, player))
    set_rule(world.get_location("Barbuta - Egg Shop - B6"),
             rule=lambda state: has_money(100, state, player))
    set_rule(world.get_location("Barbuta - Upper Shop Candy - C1"),
             rule=lambda state: has_money(100, state, player))
    set_rule(world.get_location("Barbuta - Upper Shop Umbrella - C1"),
             rule=lambda state: has_money(50, state, player))
    set_rule(world.get_location("Barbuta - Lower Shop Umbrella - F2"),
             rule=lambda state: has_money(100, state, player))
    set_rule(world.get_location("Barbuta - Lower Shop Trash - F2"),
             rule=lambda state: has_money(50, state, player))
    set_rule(world.get_location("Barbuta - Lower Shop Pin - F2"),
             rule=lambda state: has_money(200, state, player))
    set_rule(world.get_location("Barbuta - Little Guy Breaks a Wall"),
             rule=lambda state: has_money(500, state, player))

    # todo: finalize this
    set_rule(world.get_location("Barbuta - Beat the Boss"),
             rule=lambda state: state.has_any((blood_sword, wand, bat_orb), player))
