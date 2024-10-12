from typing import Dict, NamedTuple, Set, Optional


# recommended to have some sort of data structure to make it easier to deal with your locations
class GameNameLocationData(NamedTuple):
    region: str
    location_group: Optional[str] = None


location_base_id = 509342400

location_table: Dict[str, GameNameLocationData] = {
    "Test Location": GameNameLocationData("Overworld", "Test Locations"),
    "Test Location 2": GameNameLocationData("Overworld", "Test Locations"),
    "Test Location 3": GameNameLocationData("Dungeon 1", "Test Locations"),
    "Test Location 4": GameNameLocationData("Dungeon 1", "Test Locations"),
    "Test Location 5": GameNameLocationData("Dungeon 1", "Test Locations"),
}

location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)
