from enum import Enum

from typing import NamedTuple, Dict, List, Set
from BaseClasses import ItemClassification

class ItemGroup(str, Enum):
    Friends = "Friends"
    Crafting_Materials = "Crafting Materials"
    Traversal = "Traversal"
    Hat = "Hat"
    Quest_Item = "Quest Item"
    Sword = "Sword"
    Shield = "Shield"
    Ranged = "Ranged"
    Craft = "Craft"
    Item = "Item"
    Cardboard_Destroyer = "Cardboard Destroyer"

class GatorItemName(str, Enum):
    FRIEND_1 = "Friend"
    FRIEND_2 = "Friend x2"
    FRIEND_3 = "Friend x3"
    FRIEND_4 = "Friend x4"
    CRAFT_15 = "Craft Stuff x15"
    CRAFT_30 = "Craft Stuff x30"
    BRACELET = "Bracelet"
    GLIDER = "Glider"
    RETAINER = "Retainer"
    ORE = "Magic Ore"
    BROKEN_SCOOTER = "Broken Scooter Board"
    SANDWICH = "Cheese Sandwich"
    POT_Q = "Pot?"
    SORBET = "Sorbet"
    CLIPPINGS = "Grass Clippings"
    WATER = "Water"
    STARTER_HAT = "Pointy Floppy Thing"
    SLIME_HAT = "Slime Hat"
    BERET_HAT = "Artsy Beret"
    DOME_HAT = "Space Dome"
    FANGS_HAT = "Plastic Fangs"
    WESTERN_HAT = "Western Wide Brim"
    BUCKET = "Bucket"
    COWL_HAT = "Detective Cowl"
    SKATER_HAT = "Skater Helmet"
    TIARA_HAT = "Princess Tiara"
    HEADBAND = "Ninja Headband"
    STICK = "Stick"
    SWORD = "Sword"
    PAINTBRUSH = "Paintbrush"
    SPEAR = "Cardboard Spear"
    GRABBY_HAND = "Grabby Hand"
    LASER_SWORD = "Laser Sword"
    BUG_NET = "Bug Net"
    NUNCHUCKS = "Nunchaku"
    THROWN_PENCIL = "Thrown Pencil"
    PENCIL_SWORD = "Oversized Pencil"
    WRENCH = "Wrench"
    PALEOLITHIC = "Paleolithic Tool"
    WAND = "Princess Wand"
    POT_LID = "Pot Lid"
    PALETTE = "Art Palette"
    TUBE = "Inner Tube"
    PLATTER = "Platter"
    SKATEBOARD = "Skateboard"
    MARTIN_SHIELD = "Martin"
    CHESSBOARD = "Chessboard"
    BIG_LEAF = "Big Leaf"
    TRAMPOLINE = "Trampoline"
    TOWER_SHIELD = "Tower Shield"
    TRASH_CAN = "Trash Can Lid"
    BLUE_SCOOTER = "Blue Scooter Board"
    RAGDOLL = "Ragdoll"
    BALLOON = "Balloon"
    ROCK = "Skipping Rock"
    BLASTER = "Space Blaster"
    SHURIKEN = "Shuriken"
    BOMB = "Bowling Bomb"
    BUBBLEGUM = "Bubble Gum"
    STICKY_HAND = "Sticky Hand"
    PAINT_GUN = "Paint Blaster"
    CAMERA = "An Actual Digital Camera"
    MEGAPHONE = "Megaphone"
    TEXTING = "Texting With Jill"

class GatorEventName(str, Enum):
    PLAYGROUND = "Playground Complete",
    OOL = "Out of Logic Item"

class GatorItemData(NamedTuple):
    name: GatorItemName
    item_id: int | None
    classification: ItemClassification
    base_quantity_in_item_pool: int 
    item_groups: List[ItemGroup]

item_table: List[GatorItemData] = [
    GatorItemData(
        GatorItemName.FRIEND_1,
        100000001,
        ItemClassification.progression_skip_balancing,
        47,
        [ItemGroup.Friends]
    ),
    GatorItemData(
        GatorItemName.FRIEND_2,
        100000002,
        ItemClassification.progression_skip_balancing,
        3,
        [ItemGroup.Friends]
    ),
    GatorItemData(
        GatorItemName.FRIEND_3,
        100000003,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.Friends]
    ),
    GatorItemData(
        GatorItemName.FRIEND_4,
        100000004,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.Friends]
    ),
    GatorItemData(
        GatorItemName.CRAFT_15,
        100000005,
        ItemClassification.filler,
        0,
        [ItemGroup.Crafting_Materials]
    ),
    GatorItemData(
        GatorItemName.CRAFT_30,
        100000006,
        ItemClassification.filler,
        0,
        [ItemGroup.Crafting_Materials]
    ),
    GatorItemData(
        GatorItemName.BRACELET,
        100000007,
        ItemClassification.progression,
        4,
        [ItemGroup.Traversal]
    ),
    GatorItemData(
        GatorItemName.GLIDER,
        100000008,
        ItemClassification.progression,
        1,
        [ItemGroup.Traversal]
    ),
    GatorItemData(
        GatorItemName.RETAINER,
        100000009,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.ORE,
        100000010,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.BROKEN_SCOOTER,
        100000011,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.SANDWICH,
        100000012,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.POT_Q,
        100000013,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.SORBET,
        100000014,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.CLIPPINGS,
        100000015,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.WATER,
        100000016,
        ItemClassification.progression,
        1,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.STARTER_HAT,
        100000017,
        ItemClassification.progression,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.SLIME_HAT,
        100000018,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.BERET_HAT,
        100000019,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.DOME_HAT,
        100000020,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.FANGS_HAT,
        100000021,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.WESTERN_HAT,
        100000022,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.BUCKET,
        100000023,
        ItemClassification.progression,
        1,
        [ItemGroup.Hat,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.COWL_HAT,
        100000024,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.SKATER_HAT,
        100000025,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.TIARA_HAT,
        100000026,
        ItemClassification.filler,
        1,
        [ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.HEADBAND,
        100000027,
        ItemClassification.useful,
        1,
        [ItemGroup.Traversal,ItemGroup.Hat,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.STICK,
        100000028,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item, ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.SWORD,
        100000029,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.PAINTBRUSH,
        100000030,
        ItemClassification.progression,
        1,
        [ItemGroup.Craft,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.SPEAR,
        100000031,
        ItemClassification.progression,
        1,
        [ItemGroup.Craft,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.GRABBY_HAND,
        100000032,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.LASER_SWORD,
        100000033,
        ItemClassification.progression,
        1,
        [ItemGroup.Craft,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.BUG_NET,
        100000034,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.NUNCHUCKS,
        100000035,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.THROWN_PENCIL,
        100000036,
        ItemClassification.progression,
        3,
        [ItemGroup.Quest_Item]
    ),
    GatorItemData(
        GatorItemName.PENCIL_SWORD,
        100000037,
        ItemClassification.progression,
        1,
        [ItemGroup.Craft,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.WRENCH,
        100000038,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.PALEOLITHIC,
        100000039,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.WAND,
        100000040,
        ItemClassification.progression,
        1,
        [ItemGroup.Craft,ItemGroup.Sword]
    ),
    GatorItemData(
        GatorItemName.POT_LID,
        100000041,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.PALETTE,
        100000042,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.TUBE,
        100000043,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.PLATTER,
        100000044,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.SKATEBOARD,
        100000045,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.MARTIN_SHIELD,
        100000046,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.CHESSBOARD,
        100000047,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.BIG_LEAF,
        100000048,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.TRAMPOLINE,
        100000049,
        ItemClassification.progression,
        1,
        [ItemGroup.Traversal,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.TOWER_SHIELD,
        100000050,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.TRASH_CAN,
        100000051,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Item,ItemGroup.Cardboard_Destroyer]
    ),
    GatorItemData(
        GatorItemName.BLUE_SCOOTER,
        100000052,
        ItemClassification.progression,
        1,
        [ItemGroup.Shield,ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.RAGDOLL,
        100000053,
        ItemClassification.filler,
        1,
        [ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.BALLOON,
        100000054,
        ItemClassification.useful,
        1,
        [ItemGroup.Traversal,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.ROCK,
        100000055,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Ranged,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.BLASTER,
        100000056,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Ranged,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.SHURIKEN,
        100000057,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Ranged,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.BOMB,
        100000058,
        ItemClassification.useful,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.BUBBLEGUM,
        100000059,
        ItemClassification.useful,
        1,
        [ItemGroup.Traversal,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.STICKY_HAND,
        100000060,
        ItemClassification.filler,
        1,
        [ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.PAINT_GUN,
        100000061,
        ItemClassification.progression,
        1,
        [ItemGroup.Cardboard_Destroyer,ItemGroup.Ranged,ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.CAMERA,
        100000062,
        ItemClassification.filler,
        1,
        [ItemGroup.Craft]
    ),
    GatorItemData(
        GatorItemName.MEGAPHONE,
        100000063,
        ItemClassification.useful,
        0,
        [ItemGroup.Item]
    ),
    GatorItemData(
        GatorItemName.TEXTING,
        100000064,
        ItemClassification.useful,
        0,
        [ItemGroup.Item]
    ),
]

item_name_to_id: Dict[str, int] = {
    data.name.value: data.item_id for data in item_table
}

filler_items: List[str] = [
    data.name.value
    for data in item_table
    if data.classification == ItemClassification.filler
]


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> List[str]:
    item_names = []
    for data in item_table:
        if group in data.item_groups:
            item_names.append(data.name.value)
    return item_names


item_name_groups: Dict[str, Set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)


