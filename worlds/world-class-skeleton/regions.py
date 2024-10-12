from typing import Dict, List


# this can take many forms
# the example below is a simple one that'll be used create connections between the key region and its value regions
game_name_region_table: Dict[str, List[str]] = {
    "Menu": ["Overworld"],
    "Overworld": ["Dungeon 1", "Final Boss Arena"],
    "Dungeon 1": [],
    "Final Boss Arena": [],
}
