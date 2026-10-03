import typing

from BaseClasses import Item, ItemClassification
from .Data import item_classifications


class ItemData:
    id: int
    item_name: str
    progression: ItemClassification
    rom_id: int
    frequency: int = 1

    def __init__(self, id: int | None, item_name: str, progression: str, rom_id: int = 0x0, frequency: int = 1):
        self.id = id
        self.item_name = item_name
        self.progression = item_classifications[progression]
        self.rom_id = rom_id
        self.frequency = frequency


class TTYDItem(Item):
    game: str = "Paper Mario: The Thousand-Year Door"

def import_items() -> typing.List[ItemData]:
    import json
    import pkgutil

    return json.loads(pkgutil.get_data(__name__, "json/items.json").decode("utf-8"), object_hook=lambda d: ItemData(**d))

itemList: typing.List[ItemData] = import_items()
item_table: typing.Dict[str, ItemData] = {item.item_name: item for item in itemList}
items_by_id: typing.Dict[int, ItemData] = {item.id: item for item in itemList}
