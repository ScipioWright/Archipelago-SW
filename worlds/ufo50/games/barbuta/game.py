from typing import Dict, List

from BaseClasses import Region
from Options import Option
from ..base_game import UFO50Game, UFO50Item

from items import get_items, create_items, get_filler_item_name
from locations import get_locations
from regions import create_regions_and_rules


class Barbuta(UFO50Game):
    def get_items(self) -> Dict[str, int]:
        return get_items(self.base_id)

    def get_locations(self) -> Dict[str, int]:
        return get_locations(self.base_id)

    def get_options(self) -> List[Option]:
        pass

    def create_items(self) -> List[UFO50Item]:
        return create_items(self.world, self.base_id)

    def create_regions(self) -> Dict[str, Region]:
        return create_regions_and_rules(self.world, self.base_id)

    def get_filler_item_name(self):
        return get_filler_item_name()
