import csv
import enum

from typing import NamedTuple, Dict, Set, List
from itertools import groupby
from BaseClasses import Item, ItemClassification

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
    item_groups: Set[ItemGroup]

class GatorItemTable(Dict[str,GatorItemData]):
    def get_by_short_name(self, short_name: str):
        for _, data in self.items():
            if data.short_name == short_name:
                return data
        return None

# Cardboard Destroyer Group
def is_destroyer(groups: Set[ItemGroup])  -> bool:
    sword_destroyer : Set[ItemGroup] = {ItemGroup["Sword"], ItemGroup["Item"]}
    shield_destroyer : Set[ItemGroup] = {ItemGroup["Shield"], ItemGroup["Item"]}
    ranged_destroyer : Set[ItemGroup] = {ItemGroup["Ranged"], ItemGroup["Item"]}
    return groups.issuperset(sword_destroyer) or groups.issuperset(shield_destroyer) or groups.issuperset(ranged_destroyer)

def load_item_csv() -> GatorItemTable:
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # type: ignore

    items : GatorItemTable = GatorItemTable()
    with files(data).joinpath("item_lookup.csv").open() as file:
        item_reader = csv.DictReader(file)
        for item in item_reader:
            id = int(item["ap_item_id"]) if item["ap_item_id"] else None
            classification = ItemClassification[item["ap_item_classification"]]
            quantity = int(item["ap_base_quantity"]) if item["ap_base_quantity"] else 0
            groups = {ItemGroup[group] for group in item["ap_item_groups"].split(",") if group}
            if is_destroyer(groups):
                groups.add(ItemGroup["Cardboard_Destroyer"])
            items[item["longname"]] = GatorItemData(item["longname"], item["shortname"], id, classification, quantity, groups)
    return items

item_table: GatorItemTable = load_item_csv()

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

# extra groups for the purpose of aliasing items
# extra_groups: Dict[str, Set[str]] = {
#     "Hats": {"Ninja Headband (Recipe)"},
#     "Cardboard Destroyer": {"Stick (Item)","Sword (Item)","Grabby Hand (Item)","Bug Net (Item)","Nunchaku (Item)","Wrench (Item)","Paleolithic Tool (Item)","Pot Lid (Item)","Platter (Item)","Martin (Item)","Big Leaf (Item)","Trampoline (Item)","Trash Can Lid (Item)","Skipping Rock (Item)","Space Blaster (Item)","Shuriken (Item)","Bowling Bomb (Item)"}
#     # Cardboard Destroyer is limited to items received in item form since it must be an item that you can use to destroy cardboard without already having sufficient Craft Stuff
# }

# item_name_groups.update(extra_groups)