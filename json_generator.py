from typing import Any, Dict, List
from .entrances import gator_entrances
from .locations import location_table
from .rules import gator_location_rules
import json

def generate_rule_json():
    entrance_json_accumulator: List[Dict[str, Any]] = list()

    for gator_entrance in gator_entrances:
        if gator_entrance.rule is not None:
            rule_dict = dict()
            rule_dict["starting_region"] = gator_entrance.starting_region
            rule_dict["ending_region"] = gator_entrance.ending_region
            rule_dict["rule_json"] = gator_entrance.rule.to_dict()
            entrance_json_accumulator.append(rule_dict)

    with open('EntranceRules.json', 'w') as f:
        json.dump(entrance_json_accumulator, f)


    location_json_accumulator: List[Dict[str, Any]] = list()

    for location_data in location_table:
            rule = gator_location_rules[location_data.name]
            if rule is not None:
                rule_dict = dict()
                rule_dict["location_name"] = location_data.name.value
                rule_dict["location_id"] = location_data.location_id
                rule_dict["region"] = location_data.region
                rule_dict["rule_json"] = rule.to_dict()
                location_json_accumulator.append(rule_dict)

    with open('LocationRules.json', 'w') as f:
        json.dump(location_json_accumulator, f)

