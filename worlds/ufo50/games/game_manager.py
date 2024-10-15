from typing import List, Dict

from Options import Option
from .base_game import UFO50Game
from .. import UFO50World
from BaseClasses import Region

from .barbuta.game import Barbuta

games: List[UFO50Game] = [
    Barbuta("Barbuta", 1)
]


def get_items() -> Dict[str, int]:
    return {k: v for game in games for k, v in game.get_items().items()}


def get_locations() -> Dict[str, int]:
    return {k: v for game in games for k, v in game.get_locations().items()}


class GameManager:
    def __init__(self, world: UFO50World):
        self.world: UFO50World = world
        self.items: Dict[str, int] = {}
        self.locations: Dict[str, int] = {}
        self.games = games
        for game in games:
            game.world = world

    def create_items(self) -> None:
        for game in self.games:
            if self.world.is_game_included(game.game_name):
                self.world.multiworld.itempool += [game.create_items()]

    def create_regions(self) -> None:
        menu = Region("Menu", self.world.player, self.world.multiworld)
        self.world.multiworld.regions.append(menu)
        for game in self.games:
            if self.world.is_game_included(game.game_name):
                self.world.multiworld.regions.append(game.create_regions())
                # !!! get menu region method
                game_menu = self.world.multiworld.get_region(f"{game.game_name} Menu", self.world.player)
                menu.connect(game_menu, f"Boot {game.game_name}")

    def get_options(self) -> List[Option]:
        options = []
        for game in self.games:
            options += [game.get_options()]
        return options

    def get_filler_item_name(self) -> str:
        return self.world.random.choice(self.games).get_filler_item_name()
