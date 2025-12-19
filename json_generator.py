import pkgutil
from typing import Any, Dict, List

try:
    from rule_builder import True_
except ModuleNotFoundError:
    from .rule_builder import True_
from .entrances import gator_entrances
from .locations import location_table, location_name_to_id
from .rules import gator_location_rules
import json


def pull_location_positions() -> dict[tuple[int,int], list[int]]:
    # borrowed from Universal Tracker
    locs = []
    locs += json.loads(pkgutil.get_data(__name__, "tracker/locations/locations.json").decode("utf-8-sig"))  # type: ignore
    temp_locs = [location for location in locs]
    map_locs = []
    while temp_locs:
        temp_loc = temp_locs.pop()
        if "map_locations" in temp_loc:
            if "name" not in temp_loc:
                temp_loc["name"] = ""
            map_locs.append(temp_loc)
        elif "children" in temp_loc:
            temp_locs.extend(temp_loc["children"])
    coords = {
        (map_loc["x"], map_loc["y"]): [
            location_name_to_id[section["name"]]
            for section in location["sections"]
            if "name" in section and section["name"] in location_name_to_id
        ]
        for location in map_locs
        for map_loc in location["map_locations"]
        if any(
            "name" in section and section["name"] in location_name_to_id
            for section in location["sections"]
        )
    }
    return coords


def generate_rule_json():
    entrance_json_accumulator: List[Dict[str, Any]] = list()

    for gator_entrance in gator_entrances:
        rule_dict = dict()
        rule_dict["starting_region"] = gator_entrance.starting_region
        rule_dict["ending_region"] = gator_entrance.ending_region
        if gator_entrance.rule is not None:
            rule_dict["rule_json"] = gator_entrance.rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        entrance_json_accumulator.append(rule_dict)

    with open("EntranceRules.json", "w") as f:
        json.dump(entrance_json_accumulator, f)

    coords = pull_location_positions()
    id_to_coord: dict[int, list[tuple[int,int]]] = dict()
    for id in location_name_to_id.values():
        id_to_coord[id] = list()
        for k, v in coords.items():
            if id in v:
                id_to_coord[id].append(k)

        
    # print(id_to_coord)

    location_json_accumulator: List[Dict[str, Any]] = list()

    for location_data in location_table:
        rule = gator_location_rules[location_data.name]
        rule_dict = dict()
        rule_dict["location_name"] = location_data.name.value
        rule_dict["location_id"] = location_data.location_id
        rule_dict["region"] = location_data.region
        rule_dict["coords"] = id_to_coord[location_data.location_id]
        if rule is not None:
            rule_dict["rule_json"] = rule.to_dict()
        else:
            rule_dict["rule_json"] = True_().to_dict()
        location_json_accumulator.append(rule_dict)

    with open("LocationRules.json", "w") as f:
        json.dump(location_json_accumulator, f)
