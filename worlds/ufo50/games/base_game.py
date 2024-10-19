from abc import ABC, abstractmethod
from typing import Dict, List, TYPE_CHECKING

from BaseClasses import Item, Location, Region
from ..constants import GAME_NAME

if TYPE_CHECKING:
    from .. import UFO50World


class UFO50Item(Item):
    game: str = GAME_NAME


class UFO50Location(Location):
    game: str = GAME_NAME


class UFO50Game(ABC):
    world: "UFO50World"  # must be set after init

    def __init__(self, game_name: str, game_id: int):
        self.game_name = game_name
        self.base_id = game_id*1000

    @abstractmethod
    def get_items(self) -> Dict[str, int]:
        pass

    @abstractmethod
    def get_locations(self) -> Dict[str, int]:
        pass

    @abstractmethod
    def create_items(self) -> List[UFO50Item]:
        pass

    @abstractmethod
    def create_regions(self) -> Dict[str, Region]:
        pass

    @abstractmethod
    def get_filler_item_name(self):
        pass
