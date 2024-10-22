from typing import TYPE_CHECKING, Dict, NamedTuple, List, Set
from BaseClasses import Item, ItemClassification as IC
from .locations import overbold_base_id

if TYPE_CHECKING:
    from .. import UFO50World


class OverboldItem(Item):
    game: str = "UFO 50"


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int


overbold_item_table: Dict[str, ItemInfo] = {
    "Progressive HP": ItemInfo(0, IC.useful, 4),
    "Progressive Medkit": ItemInfo(1, IC.useful, 2),
    "Progressive Explosion Shield": ItemInfo(2, IC.useful, 2),
    "Progressive Projectile Shield": ItemInfo(3, IC.useful, 2),
    "Progressive Gun Speed": ItemInfo(4, IC.useful, 2),
    "Progressive Gun Power": ItemInfo(5, IC.useful, 2),
    "Progressive Gun Shots": ItemInfo(6, IC.useful, 2),
    "Progressive Gun Bounce": ItemInfo(7, IC.useful, 2),
    "Gun Knockback Increase": ItemInfo(8, IC.useful, 1),
    "Progressive Drone": ItemInfo(9, IC.useful, 2),
    "Progressive Lava Shield": ItemInfo(10, IC.useful, 2),
    "Dash Attack": ItemInfo(11, IC.useful, 1),
    "Progressive Mine Count": ItemInfo(12, IC.useful, 4),
    "Mine Remote Detonation": ItemInfo(13, IC.useful, 1),
    "Progressive Mine Shrapnel": ItemInfo(14, IC.useful, 2),
    "Mine Lures": ItemInfo(15, IC.useful, 3)
    #Maybe some money items? Was thinking either we keep prizes and money the same, or make beating a wave a location and make money another item.
}

overbold_item_groups: Dict[str, Set[str]] = {
    "Alpha Upgrades": {"Overbold - Progressive HP", 
                       "Overbold - Progressive Medkit", 
                       "Overbold - Progressive Explosion Shield", 
                       "Overbold - Progressive Projectile Shield", 
                       "Overbold - Progressive Lava Shield", 
                       "Overbold - Progressive Drone",
                       "Overbold - Dash Attack"},
    "Gun Upgrades": {"Overbold - Progressive Gun Speed", 
                     "Overbold - Progressive Gun Power", 
                     "Overbold - Progressive Gun Shots", 
                     "Overbold - Progressive Gun Bounce",
                     "Overbold - Gun Knockback Increase"}
    "Mine Upgrades": {"Overbold - Progressive Mine Count",
                      "Overbold - Mine Remote Detonation",
                      "Overbold - Progressive Mine Shrapnel",
                      "Overbold - Mine Lures"}
}


def create_overbold_item(item_name: str, world: "UFO50World") -> OverboldItem:
    item_data = overbold_item_table[item_name]
    return OverboldItem(f"Overbold - {item_name}", item_data.classification, item_data.id_offset + overbold_base_id, world.player)


def create_overbold_items(world: "UFO50World") -> List[OverboldItem]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in overbold_item_table.items()}
    overbold_items: List[OverboldItem] = []
    for item_name, quantity in items_to_create.items():
        overbold_items.append(create_overbold_item(item_name, world))
    return overbold_items
