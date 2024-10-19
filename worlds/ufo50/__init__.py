from typing import ClassVar, Any, Union, List

import Utils
from BaseClasses import Tutorial, Region
from Options import OptionError
from settings import Group, UserFilePath, LocalFolderPath, Bool
from worlds.AutoWorld import World, WebWorld

from .constants import *
from . import options
from .games import barbuta
from .games.barbuta import items, locations, regions


class UFO50Settings(Group):
    class GamePath(UserFilePath):
        """Path to the game executable from which files are extracted"""
        description = "the UFO 50 game executable"
        is_exe = True
        md5s = [GAME_HASH]

    class InstallFolder(LocalFolderPath):
        """Path to the mod installation folder"""
        description = "the folder to install UFO 50 Archipelago to"

    class LaunchGame(Bool):
        """Set this to false to never autostart the game"""

    class LaunchCommand(str):
        """
        The console command that will be used to launch the game
        The command will be executed with the installation folder as the current directory
        """

    exe_path: GamePath = GamePath("ufo50.exe")
    install_folder: InstallFolder = InstallFolder("UFO 50")
    launch_game: Union[LaunchGame, bool] = True
    launch_command: LaunchCommand = LaunchCommand("ufo50.exe" if Utils.is_windows
                                                  else "wine ufo50.exe")


class UFO50Web(WebWorld):
    theme = "partyTime"
    bug_report_page = "https://github.com/UFO-50-Archipelago/ufo-50-archipelago/issues"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up UFO 50 for Archipelago multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["LeonarthCG"]
    )
    tutorials = [setup_en]


ufo50_games: Dict = {
    "Barbuta": barbuta,
}


class UFO50World(World):
    """ 
    UFO 50 is a collection of 50 single and multiplayer games from the creators of Spelunky, Downwell, Air Land & Sea,
    Skorpulac, Catacomb Kids, and Madhouse.
    Jump in and explore a variety of genres, from platformers and shoot 'em ups to puzzle games and RPGs.
    Our goal is to combine a familiar 8-bit aesthetic with new ideas and modern game design sensibilities.
    """  # Excerpt from https://50games.fun/
    game = GAME_NAME
    web = UFO50Web()
    required_client_version = (0, 5, 0)

    topology_present = False

    item_name_to_id = {k: v for game in ufo50_games.values() for k, v in game.items.get_items().items()}
    location_name_to_id = {k: v for game in ufo50_games.values() for k, v in game.locations.get_locations().items()}

    options_dataclass = options.UFO50Options
    options: options.UFO50Options
    settings_key = "ufo_50_settings"
    settings: ClassVar[UFO50Settings]

    using_ut: bool
    ut_passthrough: Dict[str, Any]

    included_games: List  # list of modules for the games that are going to be played by this player

    def generate_early(self) -> None:
        if not self.player_name.isascii():
            raise OptionError(f"{self.player_name}'s name must be only ASCII.")

        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "UFO 50" in self.multiworld.re_gen_passthrough:
                self.ut_passthrough = self.multiworld.re_gen_passthrough["UFO 50"]
                included_game_ids = self.ut_passthrough["included_games"]
                id_to_game = {v: k for k, v in game_ids.items()}
                self.options.always_on_games.value = {id_to_game[game_id] for game_id in included_game_ids}
                self.options.random_choice_games.value.clear()
                self.options.random_choice_game_count.value = 0

        included_game_names = sorted(self.options.always_on_games.value)
        # exclude always on games from random choice games
        maybe_games = sorted(self.options.random_choice_games.value - self.options.always_on_games.value)
        # if the number of games you want is higher than the number of games you chose, enable all chosen
        if self.options.random_choice_game_count >= len(maybe_games):
            included_game_names += maybe_games
        elif self.options.random_choice_game_count and maybe_games:
            included_game_names += self.random.sample(maybe_games, self.options.random_choice_game_count.value)

        if not included_game_names:
            raise OptionError(f"UFO 50: {self.player_name} has not selected any games.")

        self.included_games = [game for name, game in ufo50_games.items() if name in included_game_names]

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for game in self.included_games:
            game_regions = game.regions.create_regions_and_rules(self)
            for region in game_regions.values():
                self.multiworld.regions.append(region)
            # !!! get menu region method
            game_menu = self.get_region(f"{game.game_name} - Menu")
            menu.connect(game_menu, f"Boot {game.game_name}")

    def create_items(self) -> None:
        for game in self.included_games:
            self.multiworld.itempool += game.items.create_items(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.included_games).items.get_filler_item_name()

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = {
            "included_games": [game_ids[game.game_name] for game in self.included_games]
        }
        return slot_data

    # for the universal tracker, doesn't get called in standard gen
    # docs: https://github.com/FarisTheAncient/Archipelago/blob/tracker/worlds/tracker/docs/re-gen-passthrough.md
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        # we are using re_gen_passthrough over modifying the world here due to complexities with ER
        return slot_data
