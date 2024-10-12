from typing import TYPE_CHECKING, Dict, NamedTuple, List
from BaseClasses import Item, ItemClassification as IC
from .locations import barbuta_base_id

if TYPE_CHECKING:
    from .. import UFO50World


class BarbutaItem(Item):
    game: str = "UFO 50"


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int


barbuta_item_table: Dict[str, ItemInfo] = {
    "$50": ItemInfo(0, IC.progression, 5),
    "$100": ItemInfo(1, IC.progression, 5),
    "Umbrella": ItemInfo(2, IC.progression, 1),
    "Necklace": ItemInfo(3, IC.progression, 1),
    "Pin": ItemInfo(4, IC.progression | IC.useful, 1),
    "Candy": ItemInfo(5, IC.progression, 1),
    "Wand": ItemInfo(6, IC.progression | IC.useful, 1),
    "Blood Sword": ItemInfo(7, IC.progression, 1),
    "Key": ItemInfo(8, IC.progression, 1),
    "Bat Orb": ItemInfo(9, IC.progression, 1),
    "Trash": ItemInfo(10, IC.filler, 1),
    "Egg": ItemInfo(11, IC.filler, 4),  # todo: maybe something different?
    "A Broken Wall": ItemInfo(12, IC.progression, 1),
}


def create_barbuta_item(item_name: str, world: "UFO50World") -> BarbutaItem:
    item_data = barbuta_item_table[item_name]
    return BarbutaItem(item_name, item_data.classification, item_data.id_offset + barbuta_base_id, world.player)


def create_barbuta_items(world: "UFO50World") -> List[BarbutaItem]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in barbuta_item_table.items()}
    barbuta_items: List[BarbutaItem] = []
    for item_name, quantity in items_to_create.items():
        barbuta_items.append(create_barbuta_item(item_name, world))
    return barbuta_items
