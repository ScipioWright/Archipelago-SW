from typing import TYPE_CHECKING, Dict, NamedTuple, List
from BaseClasses import Item, ItemClassification as IC
from .locations import night_manor_base_id

if TYPE_CHECKING:
    from .. import UFO50World


class NightManorItem(Item):
    game: str = "UFO 50"


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    item_group: str


night_manor_item_table: Dict[str, ItemInfo] = {
    "Spoon": ItemInfo(0, IC.progression), 
    "Bowl": ItemInfo(1, IC.progression),
    "Yellow Note": ItemInfo(2, IC.filler),
    "Hairpin": ItemInfo(3, IC.progression),
    "Tweezers": ItemInfo(4, IC.progression)
    "Journal Entry 2": ItemInfo(5, IC.filler, "journal_entries"),
    "Journal Entry 5": ItemInfo(6, IC.filler, "journal_entries"),
    "Hook": ItemInfo(7, IC.progression),
    "Batteries": ItemInfo(8, IC.progression),
    "Journal Entry 1": ItemInfo(9, IC.filler, "journal_entries"),
    "Coins": ItemInfo(10, IC.progression),
    "Matches": ItemInfo(11, IC.progression),
    "Journal Entry 4": ItemInfo(12, IC.filler),
    "Journal Entry 7": ItemInfo(13, IC.filler),
    "Kitchen Knife": ItemInfo(14, IC.progression),
    "Drain Cleaner": ItemInfo(15, IC.progression),
    "Oil Can": ItemInfo(16, IC.progression),
    ""


}

night_manor_item_groups; Dict[Dict[str]] = {
    "journal_entries": {"Journal Entry 1", 
                        "Journal Entry 2",
                        "Journal Entry 3",
                        "Journal Entry 4", 
                        "Journal Entry 5",
                        "Journal Entry 6",
                        "Journal Entry 7"}
    "gems"
}

def create_night_manor_item(item_name: str, world: "UFO50World") -> NightManorItem:
    item_data = night_manor_item_table[item_name]
    return NightManorItem(item_name, item_data.classification, item_data.id_offset + night_manor_base_id, world.player)


def create_night_manor_items(world: "UFO50World") -> List[NightManorItem]:
    items_to_create: Dict[str, int] = {item_name: data.quantity for item_name, data in night_manor_item_table.items()}
    night_manor_items: List[NightManorItem] = []
    for item_name, quantity in items_to_create.items():
        night_manor_items.append(create_night_manor_item(item_name, world))
    return night_manor_items
