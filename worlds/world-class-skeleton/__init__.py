from typing import Dict, List, Any
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification
from .items import item_name_to_id, item_table, item_name_groups, filler_items
from .locations import location_table, location_name_groups, location_name_to_id
from .regions import game_name_region_table
from .rules import set_location_rules, set_region_rules
from .options import GameNameOptions, game_name_option_groups, game_name_option_presets
from worlds.AutoWorld import WebWorld, World


class GameNameWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up Game Name for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["Tutorial Author"]
        )
    ]
    theme = "grassFlowers"
    game = "Game Name"
    option_groups = game_name_option_groups
    options_presets = game_name_option_presets


class GameNameItem(Item):
    game: str = "Game Name"


class GameNameLocation(Location):
    game: str = "Game Name"


class GameNameWorld(World):
    """
    Explore a land filled with lost legends, ancient powers, and ferocious monsters in TUNIC, an isometric action game
    about a small fox on a big adventure. Stranded on a mysterious beach, armed with only your own curiosity, you will
    confront colossal beasts, collect strange and powerful items, and unravel long-lost secrets. Be brave, tiny fox!
    """
    game = "Game Name"
    web = GameNameWeb()

    options: GameNameOptions
    options_dataclass = GameNameOptions
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def generate_early(self) -> None:
        # do anything here you want to have done near the start of generation
        # this is probably the best way to check for option conflicts or change options
        pass

    def create_item(self, name: str, classification: ItemClassification = None) -> GameNameItem:
        # create_item is required
        # you should use it to do your item creation as needed
        item_data = item_table[name]
        return GameNameItem(name, classification or item_data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        # create_items is required
        game_name_items: List[GameNameItem] = []
        items_to_create = {item_name: item_data.quantity_in_item_pool for item_name, item_data in item_table.items()}
        for item, quantity in items_to_create.items():
            for _ in range(quantity):
                game_name_items.append(self.create_item(item))

        self.multiworld.itempool += game_name_items

    def create_regions(self) -> None:
        # create_regions is required
        # you should have all of your regions and locations created by the end of this function
        # you can set your rules here too if it's convenient
        game_name_regions: Dict[str, Region] = {}
        for region_name in game_name_region_table.keys():
            game_name_regions[region_name] = Region(region_name, self.player, self.multiworld)

        for region_name, connecting_regions in game_name_region_table.items():
            for connecting_region in connecting_regions:
                game_name_regions[region_name].connect(game_name_regions[connecting_region])

        for location_name, location_data in location_table.items():
            loc = GameNameLocation(self.player, location_name, self.location_name_to_id[location_name],
                                   game_name_regions[location_data.region])
            game_name_regions[location_data.region].locations.append(loc)

        # you need to set the world completion condition somewhere, it doesn't necessarily need to be here though
        victory_region = game_name_regions["Final Boss Arena"]
        victory_location = GameNameLocation(self.player, "The Final Boss", None, victory_region)
        victory_location.place_locked_item(GameNameItem("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        victory_region.locations.append(victory_location)

        for region in game_name_regions.values():
            self.multiworld.regions.append(region)

    def set_rules(self) -> None:
        # this is not required, but may be helpful for setting your rules after regions and locations have been made
        set_region_rules(self)
        set_location_rules(self)

    def get_filler_item_name(self) -> str:
        # not required by heavily recommended
        # it should return the string name of a random filler item you would be fine with the multi creating on its own
        return self.random.choice(filler_items)

    def fill_slot_data(self) -> Dict[str, Any]:
        # put "light" things you need to send to the client in slot data
        # basically whatever the client needs to know from gen that isn't in a patch nor in the multidata
        slot_data: Dict[str, Any] = {}
        return slot_data
