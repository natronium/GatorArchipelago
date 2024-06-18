from typing import NamedTuple, Dict, Set, List
from itertools import groupby
from BaseClasses import Item, ItemClassification

class GatorItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id: int
    item_group: str = ""

# Items: Friends, items to pick up from ground, recipes for swords/shields/hats/left-right items, bit packets?, purchased items, bracelets

### TODO: Item IDs and match count to number of locations
item_table: Dict[str, GatorItemData] = {
    "Friend": GatorItemData(ItemClassification.progression_skip_balancing, 47, 1, "Friends"),
    "Friend x2": GatorItemData(ItemClassification.progression_skip_balancing, 3, 2, "Friends"),
    "Friend x3": GatorItemData(ItemClassification.progression_skip_balancing, 1, 3, "Friends"),
    "Friend x4": GatorItemData(ItemClassification.progression_skip_balancing, 1, 4, "Friends"),
    "Craft Stuff x15": GatorItemData(ItemClassification.filler, 1, 5, "Crafting Materials"),
    "Craft Stuff x30": GatorItemData(ItemClassification.filler, 1, 6, "Crafting Materials"),
    "Bracelet": GatorItemData(ItemClassification.progression, 4, 7, "Traversal"),
    "Glider": GatorItemData(ItemClassification.progression, 1, 8, "Traversal"),
    "Retainer": GatorItemData(ItemClassification.progression, 1, 9, "Quest Items"),
    "Magic Ore": GatorItemData(ItemClassification.progression, 1, 10, "Quest Items"),
    "Broken Scooter Board": GatorItemData(ItemClassification.progression, 1, 11, "Quest Items"),
    "Cheese Sandwich": GatorItemData(ItemClassification.progression, 1, 12, "Quest Items"),
    "Pot?": GatorItemData(ItemClassification.progression, 1, 13, "Quest Items"),
    "Sorbet": GatorItemData(ItemClassification.progression, 1, 14, "Quest Items"),
    "Grass Clippings":  GatorItemData(ItemClassification.progression, 1, 15, "Quest Items"),
    "Pointy Floppy Thing (Recipe)": GatorItemData(ItemClassification.progression, 1, 16, "Hats"),
    "Slime Hat (Recipe)": GatorItemData(ItemClassification.filler, 1, 17, "Hats"),
    "Artsy Beret (Recipe)": GatorItemData(ItemClassification.filler, 1, 18, "Hats"),
    "Space Dome (Item)": GatorItemData(ItemClassification.filler, 1, 19, "Hats"),
    "Plastic Fangs (Item)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Western Wide Brim (Item)": GatorItemData(ItemClassification.filler, 1, 21, "Hats"),
    "Bucket (Item)": GatorItemData(ItemClassification.progression, 1, 22, "Hats"),
    "Detective Cowl (Recipe)": GatorItemData(ItemClassification.filler, 1, 23, "Hats"),
    "Skater Helmet (Recipe)": GatorItemData(ItemClassification.filler, 1, 24, "Hats"),
    "Princess Tiara (Recipe)": GatorItemData(ItemClassification.filler, 1, 25, "Hats"),
    "Ninja Headband (Recipe)": GatorItemData(ItemClassification.useful, 1, 26, "Traversal"),
    "Stick (Item)": GatorItemData(ItemClassification.progression, 1, 27, "Swords"),
    "Sword (Item)": GatorItemData(ItemClassification.progression, 1, 28, "Swords"),
    "Paintbrush (Recipe)": GatorItemData(ItemClassification.progression, 1, 29, "Swords"),
    "Cardboard Spear (Recipe)": GatorItemData(ItemClassification.progression, 1, 30, "Swords"),
    "Grabby Hand (Item)": GatorItemData(ItemClassification.progression, 1, 31, "Swords"),
    "Laser Sword (Recipe)": GatorItemData(ItemClassification.progression, 1, 32, "Swords"),
    "Bug Net (Item)": GatorItemData(ItemClassification.progression, 1, 33, "Swords"),
    "Nunchaku (Item)": GatorItemData(ItemClassification.progression, 1, 34, "Swords"),
    "Oversized Pencil (Recipe)": GatorItemData(ItemClassification.progression, 1, 35, "Swords"),
    "Wrench (Item)": GatorItemData(ItemClassification.progression, 1, 36, "Swords"),
    "Paleolithic Tool (Item)": GatorItemData(ItemClassification.progression, 1, 37, "Swords"),
    "Princess Wand (Recipe)": GatorItemData(ItemClassification.progression, 1, 38, "Swords"),
    "Pot Lid (Item)": GatorItemData(ItemClassification.progression, 1, 39, "Shields"),
    "Art Palette (Recipe)": GatorItemData(ItemClassification.progression, 1, 40, "Shields"),
    "Inner Tube (Recipe)": GatorItemData(ItemClassification.progression, 1, 41, "Shields"),
    "Platter (Item)": GatorItemData(ItemClassification.progression, 1, 42, "Shields"),
    "Skateboard (Recipe)": GatorItemData(ItemClassification.progression, 1, 43, "Shields"),
    "Martin (Item)": GatorItemData(ItemClassification.progression, 1, 44, "Shields"),
    "Chessboard (Recipe)": GatorItemData(ItemClassification.progression, 1, 45, "Shields"),
    "Big Leaf (Item)": GatorItemData(ItemClassification.progression, 1, 46, "Shields"),
    "Trampoline (Item)": GatorItemData(ItemClassification.useful, 1, 47, "Traversal"), # should be excluded from has_a_shield b/c bounce
    "Tower Shield (Recipe)": GatorItemData(ItemClassification.progression, 1, 48, "Shields"),
    "Trash Can Lid (Item)": GatorItemData(ItemClassification.progression, 1, 49, "Shields"),
    "Blue Scooter Board (Recipe)": GatorItemData(ItemClassification.progression, 1, 50, "Shields"),
    "Ragdoll (Recipe)": GatorItemData(ItemClassification.filler, 1, 51),
    "Balloon (Item)": GatorItemData(ItemClassification.useful, 1, 52, "Traversal"),
    "Skipping Rock (Item)": GatorItemData(ItemClassification.progression, 1, 53, "Ranged"),
    "Space Blaster (Item)": GatorItemData(ItemClassification.progression, 1, 54, "Ranged"),
    "Shuriken (Item)": GatorItemData(ItemClassification.progression, 1, 55, "Ranged"),
    "Bowling Bomb (Item)": GatorItemData(ItemClassification.useful, 1, 56),
    "Bubble Gum (Item)": GatorItemData(ItemClassification.useful, 1, 57, "Traversal"),
    "Sticky Hand (Item)": GatorItemData(ItemClassification.filler, 1, 58),
    "Paint Blaster (Recipe)": GatorItemData(ItemClassification.progression, 1, 59, "Ranged"),
    "An Actual Digital Camera (Recipe)": GatorItemData(ItemClassification.filler, 1, 60)
}


item_name_to_id: Dict[str, int] = {name: data.item_id for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]




# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

# extra groups for the purpose of aliasing items
extra_groups: Dict[str, Set[str]] = {
    "Hats": {"Ninja Headband (Recipe)"},
    "Cardboard Destroyer": {"Stick (Item)","Sword (Item)","Grabby Hand (Item)","Bug Net (Item)","Nunchaku (Item)","Wrench (Item)","Paleolithic Tool (Item)","Pot Lid (Item)","Platter (Item)","Martin (Item)","Big Leaf (Item)","Trampoline (Item)","Trash Can Lid (Item)","Skipping Rock (Item)","Space Blaster (Item)","Shuriken (Item)","Bowling Bomb (Item)"}
    # Cardboard Destroyer is limited to items received in item form since it must be an item that you can use to destroy cardboard without already having sufficient Craft Stuff
}

item_name_groups.update(extra_groups)