from typing import Any

import json

try:
    from rule_builder import True_
except ModuleNotFoundError:
    from .rule_builder import True_
from .entrances.entrances import deathsdoor_internal_entrances, DeathsDoorEntrance
from .entrances.scene_transitions import two_way_scene_transitions, one_way_scene_transitions
from .locations import location_table
from .items import item_table
from .rules import deaths_door_location_rules

def generate_rule_json():
    entrance_json_accumulator: list[dict[str, Any]] = list()
    entrance_list = deathsdoor_internal_entrances
    for (A_to_B, B_to_A) in two_way_scene_transitions:
        entrance_list.append(A_to_B)
        entrance_list.append(B_to_A)
    for (A_to_B, _) in one_way_scene_transitions:
        entrance_list.append(A_to_B)

    for entrance in entrance_list:
        rule_dict = dict()
        rule_dict["starting_region"] = entrance.starting_region
        rule_dict["ending_region"] = entrance.ending_region
        if entrance.rule is not None:
            rule_dict["rule_json"] = entrance.rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        entrance_json_accumulator.append(rule_dict)

    with open("EntranceRules.json", "w") as f:
        json.dump(entrance_json_accumulator, f)

    location_json_accumulator: list[dict[str, Any]] = list()

    for location_data in location_table:
        rule = deaths_door_location_rules[location_data.name]
        rule_dict = dict()
        rule_dict["location_name"] = location_data.name.value
        rule_dict["location_id"] = location_data.location_id
        rule_dict["region"] = location_data.region
        if rule is not None:
            rule_dict["rule_json"] = rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        location_json_accumulator.append(rule_dict)

    with open("LocationRules.json", "w") as f:
        json.dump(location_json_accumulator, f)

def generate_scene_transition_json():
    def make_transition_dict(entrance: DeathsDoorEntrance, origin_scene_name: str = ""):
        transition_dict = dict ()
        transition_dict["startingRegion"] = entrance.starting_region.value
        transition_dict["endingRegion"] = entrance.ending_region.value
        transition_dict["loadingZoneId"] = entrance.loading_zone_id
        transition_dict["toSceneName"] = entrance.scene_name
        transition_dict["originSceneName"] = origin_scene_name
        return transition_dict
    scene_transition_json_accumulator: list[dict[str, Any]] = list()
    for (A_to_B, B_to_A) in two_way_scene_transitions:
        scene_transition_json_accumulator.append(make_transition_dict(A_to_B, B_to_A.scene_name))
        scene_transition_json_accumulator.append(make_transition_dict(B_to_A, A_to_B.scene_name))
    for (A_to_B, _) in one_way_scene_transitions:
        scene_transition_json_accumulator.append(make_transition_dict(A_to_B))
    with open("SceneTransitions.json", "w") as f:
        json.dump(scene_transition_json_accumulator, f)

def generate_items_json():
    items_accumulator : list[dict[str, Any]] = list()
    for item in item_table:
        item_dict = dict()
        item_dict["apItemId"] = item.item_id
        item_dict["itemChangerName"] = item.mod_string
        items_accumulator.append(item_dict)
    
    with open("Items.json", "w") as f:
        json.dump(items_accumulator, f)

def generate_locations_json():
    locations_accumulator : list[dict[str, Any]] = list()
    for location in location_table:
        location_dict = dict()
        location_dict["apLocationId"] = location.location_id
        location_dict["itemChangerName"] = location.mod_string
        locations_accumulator.append(location_dict)
    
    with open("Locations.json", "w") as f:
        json.dump(locations_accumulator, f)