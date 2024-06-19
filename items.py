import csv
import enum

from typing import NamedTuple, Dict, Set, List
from itertools import groupby
from BaseClasses import Item, ItemClassification

from . import data

class Group(enum.Enum):
    Friends = enum.auto()
    Crafting_Materials = enum.auto()
    Traversal = enum.auto()
    Hats = enum.auto()
    Quest_Items = enum.auto()
    Swords = enum.auto()
    Shields = enum.auto()
    Ranged = enum.auto()
    Craft = enum.auto()
    Item = enum.auto()
    Cardboard_Destroyer = enum.auto()

class GatorItemData(NamedTuple):
    long_name: str
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: Set[Group]

# Cardboard Destroyer Group
def is_destroyer(groups: Set[Group])  -> bool:
    sword_destroyer : Set[Group] = {Group["Swords"], Group["Item"]}
    shield_destroyer : Set[Group] = {Group["Shields"], Group["Item"]}
    ranged_destroyer : Set[Group] = {Group["Ranged"], Group["Item"]}
    return groups.issuperset(sword_destroyer) or groups.issuperset(shield_destroyer) or groups.issuperset(ranged_destroyer)

def load_item_csv():
    try:
        from importlib.resources import files
    except ImportError:
        from importlib_resources import files  # type: ignore

    items : Dict[str, GatorItemData] = {}
    with files(data).joinpath("item_lookup.csv").open() as file:
        item_reader = csv.DictReader(file)
        for item in item_reader:
            id = int(item["ap_item_id"]) if item["ap_item_id"] else None
            classification = ItemClassification[item["ap_item_classification"]]
            quantity = int(item["ap_base_quantity"]) if item["ap_base_quantity"] else 0
            groups = {Group[group] for group in item["ap_item_groups"].split(",") if group}
            if is_destroyer(groups):
                groups.add(Group["Cardboard_Destroyer"])
            items[item["shortname"]] = GatorItemData(item["longname"], id, classification, quantity, groups)
    return items

item_table: Dict[str, GatorItemData] = load_item_csv()

item_name_to_id: Dict[str, int] = {name: data.item_id for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: Group) -> List[str]:
    item_names = []
    for name, data in item_table.items():
        if group in data.item_groups:
            item_names.append(name)
    return item_names

item_name_groups: Dict[str, Set[str]] = {}
for group in Group:
    item_name_groups[group.name] = items_for_group(group)

# extra groups for the purpose of aliasing items
# extra_groups: Dict[str, Set[str]] = {
#     "Hats": {"Ninja Headband (Recipe)"},
#     "Cardboard Destroyer": {"Stick (Item)","Sword (Item)","Grabby Hand (Item)","Bug Net (Item)","Nunchaku (Item)","Wrench (Item)","Paleolithic Tool (Item)","Pot Lid (Item)","Platter (Item)","Martin (Item)","Big Leaf (Item)","Trampoline (Item)","Trash Can Lid (Item)","Skipping Rock (Item)","Space Blaster (Item)","Shuriken (Item)","Bowling Bomb (Item)"}
#     # Cardboard Destroyer is limited to items received in item form since it must be an item that you can use to destroy cardboard without already having sufficient Craft Stuff
# }

# item_name_groups.update(extra_groups)