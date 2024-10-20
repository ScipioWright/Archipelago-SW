from typing import TYPE_CHECKING, Dict, NamedTuple, List
from BaseClasses import ItemClassification as IC, Item
from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World

# adapted from Barbuta, thanks Scipio! <3

class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int


item_table: Dict[str, ItemInfo] = {
    "Heat Mod": ItemInfo(0, IC.progression | IC.useful, 1),
    "Multi Mod": ItemInfo(1, IC.progression | IC.useful, 1),
    "Pulse Mod": ItemInfo(2, IC.progression | IC.useful, 1),
    "Force Mod": ItemInfo(3, IC.progression | IC.useful, 1),
    "Stabilizer": ItemInfo(10, IC.progression, 2),
    "Clone Material": ItemInfo(11, IC.useful, 3),
    "Shield Upgrade": ItemInfo(12, IC.progression_skip_balancing, 25),
    "Key Code A": ItemInfo(20, IC.progression_skip_balancing, 1),
    "Key Code B": ItemInfo(21, IC.progression_skip_balancing, 1),
    "Key Code C": ItemInfo(22, IC.progression_skip_balancing, 1),
    "Key Code D": ItemInfo(23, IC.progression_skip_balancing, 1),
    "Progressive Security Clearance": ItemInfo(24, IC.progression, 3),
    # adding some placeholders for the garden, gold and cherry locations
    "Garden Gift": ItemInfo(30, IC.filler, 1),
    "Gold Disk": ItemInfo(31, IC.filler, 1),
    "Cherry Disk": ItemInfo(32, IC.filler, 1),
}


def get_items() -> Dict[str, int]:
    return {f"Vainger - {name}": data.id_offset + get_game_base_id("Vainger") for name, data in item_table.items()}


def create_item(item_name: str, world: "UFO50World") -> Item:
    if item_name.startswith("Vainger - "):
        item_name = item_name.split(" - ", 1)[1]
    item_data = item_table[item_name]
    return Item(f"Vainger - {item_name}", item_data.classification, item_data.id_offset + get_game_base_id("Vainger"), world.player)


def create_items(world: "UFO50World") -> List[Item]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in item_table.items()}
    vainger_items: List[Item] = []
    for item_name, quantity in items_to_create.items():
        for _ in range(quantity):
            vainger_items.append(create_item(item_name, world))
    return vainger_items


def get_filler_item_name() -> str:
    return "Vainger - Shield Upgrade"
