from typing import List, Dict, TYPE_CHECKING

from BaseClasses import Region, Item, Location

from .base_game import UFO50Game

from .barbuta.game import Barbuta

if TYPE_CHECKING:
    from .. import UFO50World

ufo50_games: List[UFO50Game] = [
    Barbuta("Barbuta", 1)
]


def get_items() -> Dict[str, int]:
    return {k: v for game in ufo50_games for k, v in game.get_items().items()}


def get_locations() -> Dict[str, int]:
    return {k: v for game in ufo50_games for k, v in game.get_locations().items()}


class GameManager:
    def __init__(self, world: "UFO50World"):
        self.world: "UFO50World" = world
        self.items: Dict[str, int] = {}
        self.locations: Dict[str, int] = {}
        self.games = ufo50_games
        for game in ufo50_games:
            game.world = world
        self.included_games = [game for game in ufo50_games if game.game_name in world.included_games]

    def create_items(self) -> None:
        for game in self.included_games:
            self.world.multiworld.itempool += game.create_items()

    def create_regions(self) -> None:
        menu = Region("Menu", self.world.player, self.world.multiworld)
        self.world.multiworld.regions.append(menu)
        for game in self.included_games:
            game_regions = game.create_regions()
            for region in game_regions.values():
                self.world.multiworld.regions.append(region)
            # !!! get menu region method
            game_menu = self.world.multiworld.get_region(f"{game.game_name} - Menu", self.world.player)
            menu.connect(game_menu, f"Boot {game.game_name}")

    def get_filler_item_name(self) -> str:
        return self.world.random.choice(self.included_games).get_filler_item_name()
