import enum

import json
from typing import NamedTuple, Dict, List, Set
from BaseClasses import ItemClassification

from . import data

class ItemGroup(enum.Enum):
    Friends = enum.auto()
    Crafting_Materials = enum.auto()
    Traversal = enum.auto()
    Hat = enum.auto()
    Quest_Item = enum.auto()
    Sword = enum.auto()
    Shield = enum.auto()
    Ranged = enum.auto()
    Craft = enum.auto()
    Item = enum.auto()
    Cardboard_Destroyer = enum.auto()

class GatorItemData(NamedTuple):
    long_name: str
    short_name: str
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: List[ItemGroup]

class GatorItemTable(Dict[str,GatorItemData]):
    def short_to_long(self, short_name: str) -> str:
        for _, data in self.items():
            if data.short_name == short_name:
                return data.long_name
        return None

# Cardboard Destroyer Group

def load_item_json() -> GatorItemTable:
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # type: ignore

    items : GatorItemTable = GatorItemTable()
    with files(data).joinpath("items.json").open() as file:
        item_reader = json.load(file)
        gator_items = item_reader[0]
        for _, item in gator_items.items():
            id = int(item["item_id"]) if item["item_id"] else None
            classification = ItemClassification[item["classification"]]
            quantity = int(item["base_quantity_in_item_pool"]) if item["base_quantity_in_item_pool"] else 0
            groups = [ItemGroup[group] for group in item["item_groups"].split(",") if group]
            items[item["long_name"]] = GatorItemData(item["long_name"], item["short_name"], id, classification, quantity, groups)
    return items

item_table: GatorItemTable = load_item_json()

item_name_to_id: Dict[str, int] = {name: data.item_id for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> List[str]:
    item_names = []
    for name, data in item_table.items():
        if group in data.item_groups:
            item_names.append(name)
    return item_names

item_name_groups: Dict[str, Set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.name] = items_for_group(group)