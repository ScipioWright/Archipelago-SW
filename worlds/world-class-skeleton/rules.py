from random import Random
from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item, add_rule
from BaseClasses import CollectionState
if TYPE_CHECKING:
    from . import GameNameWorld


def set_region_rules(world: "GameNameWorld") -> None:
    player = world.player

    world.get_entrance("Overworld -> Dungeon 1").access_rule = \
        lambda state: state.has("Test Item", player)

    world.get_entrance("Overworld -> Final Boss Arena").access_rule = \
        lambda state: state.has("Test Item", player, 5)


def set_location_rules(world: "GameNameWorld") -> None:
    player = world.player

    set_rule(world.get_location("Test Location"),
             lambda state: state.has("Test Item", player, 2))
