import csv
import enum

from typing import Dict, NamedTuple, Set, Optional, List
from . import data

from BaseClasses import Location

class LocationGroup(enum.Enum):
    Pot = enum.auto()
    Chest = enum.auto()
    Race = enum.auto()

class GatorLocationData(NamedTuple):
    long_name: str
    short_name: str
    location_id: int
    region: str
    # description: str
    location_group: LocationGroup

class GatorLocationTable(Dict[str,GatorLocationData]):
    def get_by_short_name(self, short_name: str):
        for _, data in self.items():
            if data.short_name == short_name:
                return data
        return None

# Locations: quest completions, ground pickups, races, bracelet purchases, junk 4 trash
def load_location_csv():
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # type: ignore

    locations : GatorLocationTable = GatorLocationTable()
    with files(data).joinpath("location_lookup.csv").open() as file:
        item_reader = csv.DictReader(file)
        for location in item_reader:
            id = int(location["ap_location_id"]) if location["ap_location_id"] else None
            group = LocationGroup[location["ap_location_group"]] if location["ap_location_group"] else None
            locations[location["longname"]] = GatorLocationData(location["longname"], location["shortname"], id, location["ap_region"], group)
    return locations

location_table: GatorLocationTable = load_location_csv()

location_name_to_id: Dict[str, int] = {name: data.location_id for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)

def location_for_group(group: LocationGroup) -> List[str]:
    location_names = []
    for name, data in location_table.items():
        if data.location_group == group:
            location_names.append(name)
    return location_names

for group in LocationGroup:
    location_name_groups[group.name] = location_for_group(group)
        