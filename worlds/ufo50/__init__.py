from typing import ClassVar, Any, Union, List

import Utils
from BaseClasses import Tutorial, Region, Item, ItemClassification
from Options import OptionError
from settings import Group, UserFilePath, LocalFolderPath, Bool
from worlds.AutoWorld import World, WebWorld

from .constants import *
from . import options

from .general_items import cartridge_items, cartridge_item_group

from .games import barbuta, vainger, night_manor
from .games.barbuta import items, locations, regions
from .games.vainger import items, locations, regions
from .games.night_manor import items, locations, regions


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


# games with an actual implementation
# add to this list as part of your PR
# try to keep them in the same order as on the main menu
ufo50_games: Dict = {
    "Barbuta": barbuta,
    "Vainger": vainger,
    "Night Manor": night_manor,
}


# for the purpose of generically making the gift, gold, and cherry locations
unimplemented_ufo50_games: List[str] = [name for name in game_ids.keys() if name not in ufo50_games.keys()]

# doing something like this in the world class itself led to weird errors
temp_ufo50_location_name_to_id = {k: v for game in ufo50_games.values() for k, v in game.locations.get_locations().items()}
for game in unimplemented_ufo50_games:
    base_id = get_game_base_id(game)
    temp_ufo50_location_name_to_id[f"{game} - Garden"] = base_id + 997
    temp_ufo50_location_name_to_id[f"{game} - Gold"] = base_id + 998
    temp_ufo50_location_name_to_id[f"{game} - Cherry"] = base_id + 999


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
    item_name_to_id.update(cartridge_items)
    location_name_to_id = temp_ufo50_location_name_to_id

    item_name_groups = {k: v for game in ufo50_games.values() for k, v in game.items.get_item_groups().items()}
    item_name_groups.update(cartridge_item_group)
    location_name_groups = {k: v for game in ufo50_games.values() for k, v in game.locations.get_location_groups().items()}

    options_dataclass = options.UFO50Options
    options: options.UFO50Options
    settings_key = "ufo_50_settings"
    settings: ClassVar[UFO50Settings]

    # for universal tracker support
    using_ut: bool
    ut_passthrough: Dict[str, Any]

    included_games: List  # list of modules for the games that are going to be played by this player
    included_unimplemented_games: List[str]  # list of included unimplemented games being played by this player

    starting_games: List[str]  # the games you start with unlocked

    def generate_early(self) -> None:
        if not self.player_name.isascii():
            raise OptionError(f"{self.player_name}'s name must be only ASCII.")

        # for universal tracker support
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "UFO 50" in self.multiworld.re_gen_passthrough:
                self.ut_passthrough = self.multiworld.re_gen_passthrough["UFO 50"]
                # sets the games that ended up on as the always_on_games, turns off random_choice_games
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

        self.included_games = []
        self.included_unimplemented_games = []
        for game_name in included_game_names:
            if game_name in ufo50_games.keys():
                self.included_games.append(ufo50_games[game_name])
            else:
                self.included_unimplemented_games.append(game_name)

        if not self.included_games:
            raise OptionError(f"UFO 50: {self.player_name} has not selected any games that have implementations. "
                              f"Please select at least one game that has an actual implementation. "
                              f"The following games have actual implementations: {[name for name in ufo50_games]}")

        if self.options.starting_game_amount >= len(included_game_names):
            self.starting_games = included_game_names
        else:
            # need at least one game to be a fully implemented game
            self.starting_games = self.random.choices(included_game_names, k=self.options.starting_game_amount.value)
            for game_name in self.starting_games:
                if game_name in ufo50_games.keys():
                    break
            else:
                # remove a game, add an implemented game
                self.starting_games.pop()
                self.starting_games.append(self.random.choice(self.included_games).game_name)

    def create_regions(self) -> None:
        menu = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu)
        for game in self.included_games:
            game_regions = game.regions.create_regions_and_rules(self)
            for region in game_regions.values():
                self.multiworld.regions.append(region)
            game_menu = self.get_region(f"{game.game_name} - Menu")
            menu.connect(game_menu, f"Boot {game.game_name}",
                         rule=lambda state, name=game.game_name: state.has(f"{name} Cartridge", self.player))

            # temp, until we get a goal actually made, just checks cherry for the last game
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach(
                self.get_location(f"{game.game_name} - Cherry"))

        for game_name in self.included_unimplemented_games:
            # todo: make this dependent on some option so you can just turn on only garden and gold and not cherry
            locs = {
                f"{game_name} - Garden": self.location_name_to_id[f"{game_name} - Garden"],
                f"{game_name} - Gold": self.location_name_to_id[f"{game_name} - Gold"],
                f"{game_name} - Cherry": self.location_name_to_id[f"{game_name} - Cherry"],
            }
            menu.add_locations(locs)

    def create_item(self, name: str, item_class: ItemClassification = None) -> Item:
        # figure out which game it's from and call its create_item
        game_name = name.split(" - ", 1)[0]
        if game_name in ufo50_games:
            return ufo50_games[game_name].items.create_item(name, self, item_class)
        return Item(name, item_class or ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        created_items: List[Item] = []
        for game in self.included_games:
            created_items += game.items.create_items(self)
            cartridge = self.create_item(f"{game.game_name} Cartridge", ItemClassification.progression)
            if game.game_name in self.starting_games:
                self.multiworld.push_precollected(cartridge)
            else:
                created_items.append(cartridge)

        unfilled_locations = self.multiworld.get_unfilled_locations(self.player)
        extra_items_needed = len(unfilled_locations) - len(created_items)

        # debug, delete this later once it all works nicely
        if extra_items_needed < 0:
            raise Exception("Too many items for the number of games, need to fix this somehow.")

        for _ in range(extra_items_needed):
            created_items.append(self.create_item(self.get_filler_item_name(), ItemClassification.filler))

        self.multiworld.itempool += created_items

    def get_filler_item_name(self) -> str:
        return self.random.choice(self.included_games).items.get_filler_item_name()

    def fill_slot_data(self) -> Dict[str, Any]:
        included_games = [game_ids[game.game_name] for game in self.included_games]
        included_games += [game_name for game_name in self.included_unimplemented_games]
        slot_data = {
            "included_games": included_games,
        }
        return slot_data

    # for the universal tracker, doesn't get called in standard gen
    # docs: https://github.com/FarisTheAncient/Archipelago/blob/tracker/worlds/tracker/docs/re-gen-passthrough.md
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        return slot_data
