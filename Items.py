from typing import NamedTuple, Dict, Set, List
from itertools import groupby
from BaseClasses import Item, ItemClassification

class GatorItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""

item_base_id: 9999999999 #adjust this

# Items: Friends, items to pick up from ground, recipes for swords/shields/hats/left-right items, bit packets?, purchased items, bracelets

item_table: Dict[str, GatorItemData] = {
    "Friend": GatorItemData(ItemClassification.progression, 56, 0),
    "Bracelet": GatorItemData(ItemClassification.progression, 4, 1),
    "Retainer": GatorItemData(ItemClassification.progression, 1, 2, "Quest Items"),
    "Magic Ore": GatorItemData(ItemClassification.progression, 1, 3, "Quest Items"),
    "Skipping Rock": GatorItemData(ItemClassification.progression, 1, 20, "Ranged")
}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]




# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}
