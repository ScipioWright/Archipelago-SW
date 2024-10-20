from typing import TYPE_CHECKING, Dict, NamedTuple, List, Set
from BaseClasses import Item, ItemClassification as IC
from .locations import night_manor_base_id

if TYPE_CHECKING:
    from .. import UFO50World


class NightManorItem(Item):
    game: str = "UFO 50"


class ItemInfo(NamedTuple):
    id_offset: int
    classification: IC
    quantity: int = 1


# TODO: Add conditional item classification based on if victory type needed is gift, gold, cherry.
night_manor_item_table: Dict[str, ItemInfo] = {
    "Spoon": ItemInfo(0, IC.progression),
    "Bowl": ItemInfo(1, IC.progression),
    "Yellow Note": ItemInfo(2, IC.filler),
    "Hairpin": ItemInfo(3, IC.progression),
    "Tweezers": ItemInfo(4, IC.progression),
    "Hook": ItemInfo(7, IC.progression),
    "Batteries": ItemInfo(8, IC.progression),
    "Coins": ItemInfo(10, IC.progression),
    "Matches": ItemInfo(11, IC.progression),
    "Kitchen Knife": ItemInfo(14, IC.progression),
    "Drain Cleaner": ItemInfo(15, IC.progression),
    "Oil Can": ItemInfo(16, IC.progression),
    "Flashlight": ItemInfo(17, IC.progression),
    "Duct Tape": ItemInfo(18, IC.progression),
    "Gas Can": ItemInfo(20, IC.progression),
    "Crowbar": ItemInfo(21, IC.progression),
    "Ornamental Egg": ItemInfo(22, IC.progression),
    "Pool Cue": ItemInfo(25, IC.progression),
    "Sheet Music": ItemInfo(27, IC.progression),
    "Screwdriver": ItemInfo(29, IC.progression),
    "Wrench": ItemInfo(31, IC.progression),
    "Hedge Shears": ItemInfo(32, IC.progression),
    "Shovel": ItemInfo(33, IC.progression),
    "Motor": ItemInfo(36, IC.progression),
    "Hacksaw": ItemInfo(38, IC.progression),
    "Ring": ItemInfo(40, IC.progression),
    "Gear": ItemInfo(42, IC.progression),
    "Magnifying Glass": ItemInfo(47, IC.progression),
    "Tea Tree Oil": ItemInfo(48, IC.progression),
    "Hydrogen Peroxide": ItemInfo(49, IC.progression),
    "Safe Combination": ItemInfo(50, IC.progression),
    "Cigar Butt": ItemInfo(52, IC.progression),
    "Computer Password": ItemInfo(55, IC.progression),
    "Piano Wire": ItemInfo(57, IC.progression),
    "Crossbow": ItemInfo(58, IC.progression),
    "Doll": ItemInfo(59, IC.progression),
    "Fungicide Recipe": ItemInfo(62, IC.progression),
    "Fungicide": ItemInfo(63, IC.progression),
    "Glasses": ItemInfo(65, IC.progression),
    "Maze Directions": ItemInfo(66, IC.progression),
    "Crossbow Bolt": ItemInfo(67, IC.progression),
    
    "Red Gemstone": ItemInfo(23, IC.progression),
    "Green Gemstone": ItemInfo(43, IC.progression),
    "Yellow Gemstone": ItemInfo(53, IC.progression),
    "White Gemstone": ItemInfo(64, IC.progression),

    "Copper Key": ItemInfo(28, IC.progression),
    "Bronze Key": ItemInfo(34, IC.progression),
    "Gold Key": ItemInfo(35, IC.progression),
    "Steel Key": ItemInfo(37, IC.progression),
    "Silver Key": ItemInfo(39, IC.progression),
    "Brass Key": ItemInfo(41, IC.progression),
    "Aluminum Key": ItemInfo(60, IC.progression),
    "Iron Key": ItemInfo(68, IC.progression),

    "Journal Entry 1": ItemInfo(9, IC.filler),
    "Journal Entry 2": ItemInfo(5, IC.filler),
    "Journal Entry 3": ItemInfo(56, IC.filler),
    "Journal Entry 4": ItemInfo(12, IC.filler),
    "Journal Entry 5": ItemInfo(6, IC.filler),
    "Journal Entry 6": ItemInfo(46, IC.filler),
    "Journal Entry 7": ItemInfo(13, IC.filler),
    "Journal Entry 8": ItemInfo(19, IC.filler),
    "Journal Entry 9": ItemInfo(24, IC.filler),
    "Journal Entry 10": ItemInfo(26, IC.filler),
    "Journal Entry 11": ItemInfo(30, IC.filler),
    "Journal Entry 12": ItemInfo(44, IC.filler),
    "Journal Entry 13": ItemInfo(54, IC.filler),
    "Journal Entry 14": ItemInfo(61, IC.filler),
    "Journal Entry 15": ItemInfo(45, IC.filler),
    "Journal Entry 16": ItemInfo(51, IC.filler),
    "Journal Entry 17": ItemInfo(69, IC.filler)

}

night_manor_item_groups: Dict[str, Set[str]] = {
    "Journal Entries": {"Night Manor - Journal Entry 1",
                        "Night Manor - Journal Entry 2",
                        "Night Manor - Journal Entry 3",
                        "Night Manor - Journal Entry 4",
                        "Night Manor - Journal Entry 5",
                        "Night Manor - Journal Entry 6",
                        "Night Manor - Journal Entry 7",
                        "Night Manor - Journal Entry 8",
                        "Night Manor - Journal Entry 9",
                        "Night Manor - Journal Entry 10",
                        "Night Manor - Journal Entry 11",
                        "Night Manor - Journal Entry 12",
                        "Night Manor - Journal Entry 13",
                        "Night Manor - Journal Entry 14",
                        "Night Manor - Journal Entry 15",
                        "Night Manor - Journal Entry 16",
                        "Night Manor - Journal Entry 17"},
    "Gems": {"Night Manor - Red Gemstone",
             "Night Manor - Green Gemstone",
             "Night Manor - Yellow Gemstone",
             "Night Manor - White Gemstone"},
    "Keys": {"Night Manor - Copper Key",
             "Night Manor - Bronze Key",
             "Night Manor - Gold Key",
             "Night Manor - Steel Key",
             "Night Manor - Silver Key",
             "Night Manor - Brass Key",
             "Night Manor - Aluminum Key",
             "Night Manor - Iron Key"}
}


def create_night_manor_item(item_name: str, world: "UFO50World") -> NightManorItem:
    item_data = night_manor_item_table[item_name]
    return NightManorItem(f"Night Manor - {item_name}", item_data.classification, item_data.id_offset + night_manor_base_id, world.player)


def create_night_manor_items(world: "UFO50World") -> List[NightManorItem]:
    night_manor_items: List[NightManorItem] = []
    for item_name in night_manor_item_table.items():
        night_manor_items.append(create_night_manor_item(item_name, world))
    return night_manor_items
