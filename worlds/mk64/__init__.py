import os
import typing

import settings
from BaseClasses import Item, MultiWorld, Tutorial
from worlds.AutoWorld import World, WebWorld

from . import Items, Locations, Regions, Rom, Rules
from .Client import MarioKart64Client  # Import to register client with BizHawkClient
from .Options import mk64_options, GameMode, Opt, ShuffleDriftAbilities


class MK64Web(WebWorld):
    theme = "grass"

    setup = Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up the Archipelago Mario Kart 64 software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Edsploration"]
    )
    tutorials = [setup]


class MK64Settings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the MK64 ROM"""
        description = "Mario Kart 64 ROM File"
        copy_to = "Mario Kart 64 (U) [!].z64"
        md5s = [Rom.MK64DeltaPatch.hash]
        # "e19398a0fd1cc12df64fca7fbcaa82cc"  # byte-swapped ROM hash

    rom_file: RomFile = RomFile(RomFile.copy_to)


class MK64World(World):
    # """
    # Mario Kart 64 is the first true 3D kart racing game. Use offensive
    # and defensive items, dodge hazards, drift and mini-turbo around corners,
    # and stay on the track to win races and the gold trophy in each cup.
    # """
    """
    Mario Kart 64 is the original 3D kart racing game. Collect and fire off items,
    maneuver around hazards, execute drifts and mini-turbos, risk shortcuts but
    stay on the track, and race your way to victory in each course and cup.
    """
    game = "Mario Kart 64"
    option_definitions = mk64_options
    settings: typing.ClassVar[MK64Settings]
    topology_present = False  # Show path to required checks in spoiler log? TODO: Is this desired?

    item_name_to_id = Items.item_name_to_id
    location_name_to_id = Locations.location_name_to_id

    # item_name_groups = Items.item_name_groups  # TODO: Is this needed? Which name groups do people want to hint for?
    data_version = 1

    web = MK64Web()

    # Declare variables needed in multiple generation steps so they are tracked in MK64World state
    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)
        self.opt = None
        self.num_filler_items = None
        self.shuffle_clusters = None
        self.filler_spots = None
        self.victory_location = None
        self.course_order = None
        self.driver_unlocks = 0

    @classmethod
    def stage_assert_generate(cls, multiworld: MultiWorld):
        rom_file = Rom.get_base_rom_path()
        if not os.path.exists(rom_file):
            raise FileNotFoundError(rom_file)

    def generate_early(self) -> None:
        self.opt = opt = Opt(self.multiworld, self.player)

        # Count items without a paired location and vice versa, based on player options
        # hardcoded for speed, and because duplicating the the world generation logic here would be excessive.
        # Tests may be needed to keep this from being fragile, or it may need to be refactored to later into generation.
        num_unpaired_items = ((not opt.feather and not opt.two_player and 21)  # 20 to 155
                              + (opt.feather and not opt.two_player and 22)
                              + (not opt.feather and opt.two_player and 34)
                              + (opt.feather and opt.two_player and 36)
                              + (3 if opt.mode == GameMode.option_cups else opt.locked_courses)
                              + (0 if opt.drift == ShuffleDriftAbilities.option_off else
                                 (opt.drift == ShuffleDriftAbilities.option_on and 16) or
                                 (opt.drift == ShuffleDriftAbilities.option_plentiful and 24) or 8)
                              + (opt.traction and 16)
                              + (opt.starting_items and 8)
                              + (opt.railings and 13)
                              + ((opt.path_fences or opt.obstacle_fences or opt.item_fences) and 4)
                              + (opt.box_respawning and 1)
                              + opt.min_filler)
        num_unpaired_locations = ((67 if opt.mode == GameMode.option_cups else 47)  # 47 to 88
                                  + (opt.hazards and 11)
                                  + (opt.secrets and 10))

        num_needed_extra_locs = max(num_unpaired_items - num_unpaired_locations, 0)  # 0 to 108
        num_needed_extra_items = max(num_unpaired_locations - num_unpaired_items, 0)
        self.num_filler_items = opt.min_filler + num_needed_extra_items  # 0 to 65
        self.shuffle_clusters = ([True] * opt.clusters + [False] * (72 - opt.clusters))
        self.filler_spots = ([True] * num_needed_extra_locs + [False] * (338 - num_needed_extra_locs - opt.clusters))
        # TODO: Determine whether we can/should notify this at generation time like this.
        if num_needed_extra_locs:
            print(f"{num_needed_extra_locs} extra Mario Kart 64 locations will be made"
                  f" for {self.multiworld.get_player_name(self.player)} to match their number of items.")
        elif num_needed_extra_items:
            print(f"{num_needed_extra_items} extra Mario Kart 64 filler items will be made"
                  f" for {self.multiworld.get_player_name(self.player)} to match their number of locations.")

    def create_regions(self) -> None:
        self.victory_location, self.course_order = Regions.create_regions_locations_connections(
            self.multiworld,
            self.player,
            self.opt,
            self.shuffle_clusters,
            self.filler_spots
        )

    def create_item(self, name: str) -> Item:
        return Items.create_item(name, self.player)

    def create_items(self) -> None:
        self.driver_unlocks = Items.create_items(
            self.multiworld,
            self.player,
            self.opt,
            self.shuffle_clusters,
            self.num_filler_items,
            self.victory_location
        )

    def set_rules(self) -> None:
        Rules.create_rules(self.multiworld, self.player, self.opt, self.victory_location)

    def generate_output(self, output_directory: str) -> None:
        Rom.generate_rom_patch(
            self.multiworld,
            self.player,
            self.opt,
            output_directory,
            self.driver_unlocks,
            self.course_order
        )

    def modify_multidata(self, multidata: dict) -> None:
        player_name = self.multiworld.player_name[self.player]
        slot_name = player_name + "_" + self.multiworld.seed_name
        multidata["connect_names"][slot_name] = multidata["connect_names"][player_name]

    def fill_slot_data(self):
        return {name: getattr(self.multiworld, name)[self.player].value for name in self.option_definitions}
