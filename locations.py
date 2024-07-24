import enum
import json
from typing import Dict, NamedTuple, Set, List
from . import data


class LocationGroup(enum.Enum):
    Pot = enum.auto()
    Chest = enum.auto()
    Race = enum.auto()


class GatorLocationData(NamedTuple):
    long_name: str
    location_id: int
    region: str
    location_group: LocationGroup
    access_rules: List[str]


class GatorLocationTable(Dict[str, GatorLocationData]):
    pass


def traverse(dic, path=None):
    if not path:
        path = ""
    if isinstance(dic, dict):
        try:
            name = dic["name"]
            local_path = path + "/" + name
            try:
                sections = dic["sections"]
                for section in sections:
                    for b in traverse(section, local_path):
                        yield b
            except:
                try:
                    children = dic["children"]
                    for child in children:
                        for b in traverse(child, local_path):
                            yield b
                except KeyError:
                    yield local_path, dic
        except KeyError:
            yield path, dic
    else:
        yield path, dic


def load_location_json() -> GatorLocationTable:
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # type: ignore

    locations: GatorLocationTable = GatorLocationTable()
    with files(data).joinpath("locations.json").open() as file:
        location_reader = json.load(file)
        for _, location in traverse(location_reader[0]):
            id = int(location["location_id"])
            group = (
                LocationGroup[location["location_group"]]
                if location["location_group"]
                else None
            )
            locations[location["name"]] = GatorLocationData(
                location["name"],
                id,
                location["region"],
                group,
                location["access_rules"],
            )
    return locations


def locations_for_group(group: LocationGroup) -> List[str]:
    location_names = []
    for name, data in location_table.items():
        if data.location_group == group:
            location_names.append(name)
    return location_names


location_table: GatorLocationTable = load_location_json()

location_name_to_id: Dict[str, int] = {
    name: data.location_id for name, data in location_table.items()
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)
