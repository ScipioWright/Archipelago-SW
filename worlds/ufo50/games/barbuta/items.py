from typing import TYPE_CHECKING, Dict, NamedTuple, List
from BaseClasses import ItemClassification as IC, Item

from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int


item_table: Dict[str, ItemInfo] = {
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
    "Egg": ItemInfo(11, IC.filler, 7),  # todo: change this number when we have filler items figured out
    "A Broken Wall": ItemInfo(12, IC.progression, 1),
}


def get_items() -> Dict[str, int]:
    return {f"Barbuta - {name}": data.id_offset + get_game_base_id("Barbuta") for name, data in item_table.items()}


def create_item(item_name: str, world: "UFO50World", item_class: IC = None) -> Item:
    base_id = get_game_base_id("Barbuta")
    item_data = item_table[item_name]
    return Item(f"Barbuta - {item_name}", item_class or item_data.classification,
                item_data.id_offset + base_id, world.player)


def create_items(world: "UFO50World") -> List[Item]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in item_table.items()}
    barbuta_items: List[Item] = []
    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            barbuta_items.append(create_item(item_name, world))
    return barbuta_items


def get_filler_item_name() -> str:
    return "Barbuta - Egg"
