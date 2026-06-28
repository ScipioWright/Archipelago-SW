import json
from importlib.resources import files
from typing import Any, ClassVar, Dict, Optional

from BaseClasses import ItemClassification, Location, Tutorial
from entrance_rando import bake_target_group_lookup, randomize_entrances

from Utils import visualize_regions
from rule_builder.rules import Has
from .data.rules.ability_rules import PowerLevelThreshold
from .data.rules.state_rules import HasRepairedAllGenerators

from ..AutoWorld import WebWorld
from . import items, locations, tracker
from .constants import MINA_THE_HOLLOWER
from .data import get_target_groups
from .data.items import all_filler_items, all_items
from .data.locations import all_locations
from .items import MinaTheHollowerItem
from .options import ABILITY_RANDO_SLOT_KEYS, mina_the_hollower_option_groups
from .world_base import MinaTheHollowerBase


class MinaTheHollowerWeb(WebWorld):
    theme = "partyTime"
    setup_en = Tutorial(
        tutorial_name="Multiworld Setup Guide",
        description="A guide to setting up the Mina The Hollower randomizer connected to an Archipelago Multiworld.",
        language="English",
        file_name="setup_en.md",
        link="setup/en",
        authors=["FyreDay"],
    )
    option_groups = mina_the_hollower_option_groups
    tutorials = [setup_en]


def load_manifest():
    return json.loads(
        files(__package__).joinpath("archipelago.json").read_text("utf-8")
    )


class MinaTheHollowerWorld(MinaTheHollowerBase):

    manifest = load_manifest()

    game = MINA_THE_HOLLOWER
    web = MinaTheHollowerWeb()

    item_name_to_id: ClassVar[Dict[str, int]] = {
        item.value: item.item_id for item in all_items
    }
    location_name_to_id: ClassVar[Dict[str, int]] = {
        loc_name: loc_data.location_id for loc_name, loc_data in all_locations.items()
    }

    item_lookup = {item.value: item for item in all_items}

    ut_can_gen_without_yaml = True

    tracker_world: ClassVar = {
        "map_page_folder": "tracker",
        "map_page_maps": "maps/maps.json",
        "map_page_locations": {
            "locations/eastern_heath.json",
            "locations/ossex.json",
            "locations/loners_landing.json",
            "locations/southern_outskirts.json",
            "locations/eastern_heath.json",
            "locations/backwaters.json",
            "locations/western_wilds.json",
            "locations/bayou.json",
        },
        "map_page_index": tracker.map_page_index,
        "map_page_setting_key": "MTH_level_{team}_{player}",
    }

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        return slot_data

    def __init__(self, multiworld, player):
        self.regions = {}
        self.itempool = []
        self.entrance_rando = False
        self.hints = {}
        self.starting_items = []

        super().__init__(multiworld, player)

    def generate_early(self) -> None:
        # self.options.excluded_areas.value = False
        self.handle_ut_yamless(None)
        if self.options.ability_rando.value:
            self.options.ossex_start.value = self.options.ossex_start.option_true

    def create_regions(self):
        self.regions = locations.get_regions(self)
        locations.create_regions(self, self.regions)
        items.create_events(self)
        locations.create_entrances(self, self.regions)

    def connect_entrances(self) -> None:
        if self.entrance_rando:
            target_group_lookup = bake_target_group_lookup(self, get_target_groups)
            randomize_entrances(self, False, target_group_lookup)

    def create_item(self, item: str) -> MinaTheHollowerItem:
        item_enum = self.item_lookup[item]

        return MinaTheHollowerItem(
            item,
            item_enum.classification,
            item_enum.item_id,
            self.player,
        )

    def create_items(self):
        self.starting_items = items.create_items(self)
        for item in self.starting_items:
            self.push_precollected(item)

    def set_rules(self):
        self.set_completion_rule(Has("Victory") & PowerLevelThreshold(power=60))

    def generate_output(self, output_directory: str):
        print("Generating Output")
        visualize_regions(
            self.multiworld.get_region("Menu", self.player),
            f"Player{self.player}_output.puml",
            show_entrance_names=True,
            regions_to_highlight=self.multiworld.get_all_state(
                self.player
            ).reachable_regions[self.player],
        )

    def fill_slot_data(self) -> id:
        ability_rando = self.options.ability_rando.value
        return {
            "sem_ver": self.manifest["mod_version"],
            "goal": self.options.goal.value,
            "ossex_start": self.options.ossex_start.value,
            "kear_rando": self.options.kear_rando.value,
            # "entrance_rando" : self.options.entrance_rando.value,
            "death_link": self.options.death_link.value,
            # The client disables each ability while its "*_rando" key is nonzero.
            **{
                slot_key: int(option_key in ability_rando)
                for option_key, slot_keys in ABILITY_RANDO_SLOT_KEYS.items()
                for slot_key in slot_keys
            },
            "starting_items": [
                item.name
                for item in self.starting_items
            ]
        }

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]):
        hint_data[self.player] = self.hints

    def handle_ut_yamless(
        self, slot_data: Optional[Dict[str, Any]]
    ) -> Optional[Dict[str, Any]]:

        if (
            not slot_data
            and hasattr(self.multiworld, "re_gen_passthrough")
            and isinstance(self.multiworld.re_gen_passthrough, dict)
            and self.game in self.multiworld.re_gen_passthrough
        ):
            slot_data = self.multiworld.re_gen_passthrough[self.game]

        if not slot_data:
            return None

        self.options.goal.value = slot_data["goal"]
        self.options.death_link.value = slot_data["death_link"]
        self.options.kear_rando.value = slot_data["kear_rando"]
        self.options.ossex_start.value = slot_data["ossex_start"]
        self.options.ability_rando.value = {
            option_key
            for option_key, slot_keys in ABILITY_RANDO_SLOT_KEYS.items()
            if any(slot_data.get(slot_key) for slot_key in slot_keys)
        }
        # self.options.entrance_rando.value = slot_data["entrance_rando"]
        # self.options.shuffled_sidearms.value = slot_data["shuffled_sidearms"]
        # self.options.shuffle_enemy_level.value = slot_data["shuffle_enemy_level"]
        # self.options.shuffled_items.value = slot_data["shuffled_items"]

        for item_name in slot_data["starting_items"]:
            self.starting_items.append(MinaTheHollowerItem(item_name, ItemClassification.progression, self.item_name_to_id[item_name], self.player))
        return slot_data
