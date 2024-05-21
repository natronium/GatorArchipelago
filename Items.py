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
    "Friend": GatorItemData(ItemClassification.progression_skip_balancing, 48, 0, "Friends"),
    "Friend x2": GatorItemData(ItemClassification.progression_skip_balancing, 3, 0, "Friends"),
    "Friend x4": GatorItemData(ItemClassification.progression_skip_balancing, 1, 0, "Friends"),
    "Crafting Materials x???": GatorItemData(ItemClassification.filler, 1, 0, "Craft Bits"),
    "Bracelet": GatorItemData(ItemClassification.progression, 4, 1, "Traversal"),
    "Glider": GatorItemData(ItemClassification.progression, 1, 1, "Traversal"),
    "Retainer": GatorItemData(ItemClassification.progression, 1, 2, "Quest Items"),
    "Magic Ore": GatorItemData(ItemClassification.progression, 1, 3, "Quest Items"),
    "Broken Scooter Board": GatorItemData(ItemClassification.progression, 1, 3, "Quest Items"),
    "Cheese Sandwich": GatorItemData(ItemClassification.progression, 1, 3, "Quest Items"),
    "Pot?": GatorItemData(ItemClassification.progression, 1, 3, "Quest Items"),
    "Pointy Floppy Thing (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Hats"),
    "Slime Hat (Recipe)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Artsy Beret (Recipe)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Space Dome (Item)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Plastic Fangs (Item)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Western Wide Brim (Item)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Bucket (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Hats"),
    "Detective Cowl (Recipe)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Skater Helmet (Recipe)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Princess Tiara (Recipe)": GatorItemData(ItemClassification.filler, 1, 20, "Hats"),
    "Ninja Headband (Recipe)": GatorItemData(ItemClassification.useful, 1, 20, "Traversal"),
    "Stick (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Sword (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Paintbrush (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Cardboard Spear (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Grabby Hand (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Laser Sword (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Bug Net (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Nunchaku (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Oversized Pencil (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Wrench (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Paleolithic Tool (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Princess Wand (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Swords"),
    "Pot Lid (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Art Palette (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Inner Tube (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Platter (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Skateboard (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Martin (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Chessboard (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Big Leaf (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Trampoline (Item)": GatorItemData(ItemClassification.useful, 1, 20, "Traversal"), # should be excluded from has_a_shield b/c bounce
    "Tower Shield (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Trash Can Lid (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Blue Scooter Board (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Shields"),
    "Ragdoll (Recipe)": GatorItemData(ItemClassification.filler, 1, 20),
    "Balloon (Item)": GatorItemData(ItemClassification.useful, 1, 20, "Traversal"),
    "Skipping Rock (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Ranged"),
    "Space Blaster (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Ranged"),
    "Shuriken (Item)": GatorItemData(ItemClassification.progression, 1, 20, "Ranged"),
    "Bowling Bomb (Item)": GatorItemData(ItemClassification.useful, 1, 20),
    "Bubble Gum (Item)": GatorItemData(ItemClassification.useful, 1, 20, "Traversal"),
    "Sticky Hand (Item)": GatorItemData(ItemClassification.filler, 1, 20),
    "Paint Blaster (Recipe)": GatorItemData(ItemClassification.progression, 1, 20, "Ranged"),
    "An Actual Digital Camera (Recipe)": GatorItemData(ItemClassification.filler, 1, 20)
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

# extra groups for the purpose of aliasing items
extra_groups: Dict[str, Set[str]] = {
    "Hats": {"Ninja Headband (Recipe)"}
}

item_name_groups.update(extra_groups)