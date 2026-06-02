from enum import Enum

from typing import NamedTuple, Dict, List, Set
from BaseClasses import ItemClassification


class ItemGroup(str, Enum):
    Surface = "Surface"
    Underground = "Underground"

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
    Ragdoll = "Ragdoll"
    Unlock = "Unlock Item"
    Trap = "Trap"

    # Underground effects
    Stone_Break = "Stone Breaker"
    Hover = "Hover"
    Slam = "Slam"
    Dash = "Dash"
    Spin_Jump = "Spin Jump"

    Cryptid = "Cryptid"


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
    SWORD = "Wooden Sword"
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
    OAR = "Oar"
    SLEEP_MASK = "Sleep Mask"
    GIANT_SOCKS = "Giant Socks"
    TIGER_FORM = "Tiger Form"
    GUITAR = "Guitar of Space"
    KEY = "Key"
    FINISH_FLAG = "Finish Flag"
    STUMBLE_TRAP = "Stumble Trap"
    DIALOGUE_TRAP = "Dialogue Trap"
    FLOAT_TRAP = "Float Trap"
    SNEAK_TRAP = "Sneak Trap"
    PIXEL_TRAP = "Pixel Trap"

    # Underground
    MINE_FRIEND = "Mines Friend"
    ROOTS_FRIEND = "Big Roots Friend"
    DRIP_FRIEND = "Flowstone Caverns Friend"
    BIG_SIS_SCARF = "Big Sis Scarf"
    VIKING_HORNS = "Viking Horns"
    STYLING_GEL = "Styling Gel"
    BONEHEAD = "Bonehead"
    GHOSTLY_GARB = "Ghostly Garb"
    PIRATE_CHAPEAU = "Pirate Chapeau"
    HARD_HAT = "Hard Hat"
    PROPELLER_BEANIE = "Propeller Beanie"
    WIZARD_CONE = "Wizard Cone"
    PICKAXE = "Pickaxe"
    GIANT_CLUB = "Giant Club"
    JOUSTING_LANCE = "Jousting Lance"
    FLASHSTEP = "Flashstep"
    RIBBON = "Ribbon"
    BUBBLE_WAND = "Bubble Wand"
    PROPELLER = "Propeller"
    QUARTERSTAFF = "Quarterstaff"
    DARKSWORD = "Darksword"
    MINECART = "Minecart"
    STICKY_SHIELD = "Sticky Shield"
    PAINTING = "Painting"
    BATTERING_RAM = "Battering Ram"
    RECORD = "Record"
    ROADSIGN = "Roadsign"
    SURFBOARD = "Surfboard"
    FILM_REEL = "Film Reel"
    DARKSHIELD = "Dark Shield"
    BATTLE_TOP = "Battle Top"
    DRONE = "Drone"
    FIREWORK = "Firework"
    RUBBER_BALL = "Rubber Ball"
    SPIDER_WEB = "Spider Web"
    GLOWY_GUNK = "Glowy Gunk"
    QUEENS_SECRET_LETTER = "Queen's Secret Letter"
    OTHER_QUEENS_SECRET_LETTER = "Other Queen's Secret Letter"
    CLAM = "Clam"
    THORNY = "Thorny"
    BUBBLY = "Bubbly"
    CAKEY = "Cakey"
    HOLY = "Holy"
    FINNY = "Finny"
    DRIPPY = "Drippy"
    FLOOFY = "Floofy"
    TREEY = "Treey"
    LOOKY = "Looky"

class GatorEventName(str, Enum):
    PLAYGROUND = "Playground Complete"
    OOL = "Out of Logic Item"


class GatorItemData(NamedTuple):
    name: GatorItemName
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: List[ItemGroup]


surface_item_table: List[GatorItemData] = [
    GatorItemData(
        GatorItemName.FRIEND_1,
        100000001,
        ItemClassification.progression_deprioritized_skip_balancing,
        47,
        [ItemGroup.Surface, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.FRIEND_2,
        100000002,
        ItemClassification.progression_deprioritized_skip_balancing,
        3,
        [ItemGroup.Surface, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.FRIEND_3,
        100000003,
        ItemClassification.progression_deprioritized_skip_balancing,
        1,
        [ItemGroup.Surface, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.FRIEND_4,
        100000004,
        ItemClassification.progression_deprioritized_skip_balancing,
        1,
        [ItemGroup.Surface, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.CRAFT_15,
        100000005,
        ItemClassification.filler,
        0,
        [ItemGroup.Crafting_Materials],
    ),
    GatorItemData(
        GatorItemName.CRAFT_30,
        100000006,
        ItemClassification.filler,
        0,
        [ItemGroup.Crafting_Materials],
    ),
    GatorItemData(
        GatorItemName.BRACELET,
        100000007,
        ItemClassification.progression,
        4,
        [ItemGroup.Surface, ItemGroup.Traversal],
    ),
    GatorItemData(
        GatorItemName.GLIDER,
        100000008,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Traversal],
    ),
    GatorItemData(
        GatorItemName.RETAINER,
        100000009,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.ORE,
        100000010,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.BROKEN_SCOOTER,
        100000011,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.SANDWICH,
        100000012,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.POT_Q,
        100000013,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.SORBET,
        100000014,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.CLIPPINGS,
        100000015,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.WATER,
        100000016,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.STARTER_HAT,
        100000017,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.SLIME_HAT,
        100000018,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.BERET_HAT,
        100000019,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.DOME_HAT,
        100000020,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.FANGS_HAT,
        100000021,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.WESTERN_HAT,
        100000022,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.BUCKET,
        100000023,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.COWL_HAT,
        100000024,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.SKATER_HAT,
        100000025,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.TIARA_HAT,
        100000026,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Hat, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.HEADBAND,
        100000027,
        ItemClassification.useful,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Traversal,
            ItemGroup.Hat,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.STICK,
        100000028,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.SWORD,
        100000029,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.PAINTBRUSH,
        100000030,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Craft, ItemGroup.Surface, ItemGroup.Sword],
    ),
    GatorItemData(
        GatorItemName.SPEAR,
        100000031,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Craft, ItemGroup.Surface, ItemGroup.Sword],
    ),
    GatorItemData(
        GatorItemName.GRABBY_HAND,
        100000032,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.LASER_SWORD,
        100000033,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Craft, ItemGroup.Surface, ItemGroup.Sword],
    ),
    GatorItemData(
        GatorItemName.BUG_NET,
        100000034,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.NUNCHUCKS,
        100000035,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.THROWN_PENCIL,
        100000036,
        ItemClassification.progression,
        3,
        [ItemGroup.Surface, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.PENCIL_SWORD,
        100000037,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Craft, ItemGroup.Surface, ItemGroup.Sword],
    ),
    GatorItemData(
        GatorItemName.WRENCH,
        100000038,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.PALEOLITHIC,
        100000039,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Sword,
        ],
    ),
    GatorItemData(
        GatorItemName.WAND,
        100000040,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Craft, ItemGroup.Surface, ItemGroup.Sword],
    ),
    GatorItemData(
        GatorItemName.POT_LID,
        100000041,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.PALETTE,
        100000042,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.TUBE,
        100000043,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.PLATTER,
        100000044,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.SKATEBOARD,
        100000045,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.MARTIN_SHIELD,
        100000046,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.CHESSBOARD,
        100000047,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.BIG_LEAF,
        100000048,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.TRAMPOLINE,
        100000049,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Traversal,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.TOWER_SHIELD,
        100000050,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.TRASH_CAN,
        100000051,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.BLUE_SCOOTER,
        100000052,
        ItemClassification.progression,
        1,
        [ItemGroup.Surface, ItemGroup.Shield, ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.RAGDOLL,
        100000053,
        ItemClassification.filler,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Craft,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.BALLOON,
        100000054,
        ItemClassification.useful,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Traversal,
            ItemGroup.Item,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.ROCK,
        100000055,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Ranged,
            ItemGroup.Item,
        ],
    ),
    GatorItemData(
        GatorItemName.BLASTER,
        100000056,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Ranged,
            ItemGroup.Item,
        ],
    ),
    GatorItemData(
        GatorItemName.SHURIKEN,
        100000057,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Ranged,
            ItemGroup.Item,
        ],
    ),
    GatorItemData(
        GatorItemName.BOMB,
        100000058,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
        ],
    ),
    GatorItemData(
        GatorItemName.BUBBLEGUM,
        100000059,
        ItemClassification.useful,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Traversal,
            ItemGroup.Item,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.STICKY_HAND,
        100000060,
        ItemClassification.filler,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Item,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.PAINT_GUN,
        100000061,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Surface,
            ItemGroup.Cardboard_Destroyer,
            ItemGroup.Ranged,
            ItemGroup.Item,
        ],
    ),
    GatorItemData(
        GatorItemName.CAMERA,
        100000062,
        ItemClassification.filler,
        1,
        [ItemGroup.Surface, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.MEGAPHONE,
        100000063,
        ItemClassification.useful,
        0,
        [ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.TEXTING,
        100000064,
        ItemClassification.useful,
        0,
        [ItemGroup.Surface, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.OAR,
        100000065,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.SLEEP_MASK,
        100000066,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.GIANT_SOCKS,
        100000067,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.TIGER_FORM,
        100000068,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.GUITAR,
        100000069,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.KEY,
        100000070,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.FINISH_FLAG,
        100000071,
        ItemClassification.progression,
        0,
        [ItemGroup.Surface, ItemGroup.Unlock],
    ),
    GatorItemData(
        GatorItemName.STUMBLE_TRAP,
        100000171,
        ItemClassification.trap,
        0,
        [ItemGroup.Trap],
    ),
    GatorItemData(
        GatorItemName.DIALOGUE_TRAP,
        100000172,
        ItemClassification.trap,
        0,
        [ItemGroup.Trap],
    ),
    GatorItemData(
        GatorItemName.FLOAT_TRAP,
        100000173,
        ItemClassification.trap,
        0,
        [ItemGroup.Trap],
    ),
    GatorItemData(
        GatorItemName.SNEAK_TRAP,
        100000174,
        ItemClassification.trap,
        0,
        [ItemGroup.Trap],
    ),
    GatorItemData(
        GatorItemName.PIXEL_TRAP,
        100000175,
        ItemClassification.trap,
        0,
        [ItemGroup.Trap],
    ),
]

underground_item_table: List[GatorItemData] = [
    GatorItemData(
        GatorItemName.MINE_FRIEND,
        100000200,
        ItemClassification.progression_deprioritized_skip_balancing,
        8,
        [ItemGroup.Underground, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.ROOTS_FRIEND,
        100000201,
        ItemClassification.progression_deprioritized_skip_balancing,
        8,
        [ItemGroup.Underground, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.DRIP_FRIEND,
        100000202,
        ItemClassification.progression_deprioritized_skip_balancing,
        8,
        [ItemGroup.Underground, ItemGroup.Friends],
    ),
    GatorItemData(
        GatorItemName.BIG_SIS_SCARF,
        100000210,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Item],
    ),
    GatorItemData(
        GatorItemName.VIKING_HORNS,
        100000211,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Hat,
            ItemGroup.Stone_Break,
            ItemGroup.Craft,
        ],  # TODO: May only be able to stone break when combined with a source of Ragdoll?
    ),
    GatorItemData(
        GatorItemName.STYLING_GEL,
        100000212,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.BONEHEAD,
        100000213,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Stone_Break, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.GHOSTLY_GARB,
        100000214,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.PIRATE_CHAPEAU,
        100000215,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.HARD_HAT,
        100000216,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.PROPELLER_BEANIE,
        100000217,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.WIZARD_CONE,
        100000218,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Hat, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.PICKAXE,
        100000219,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Item,
            ItemGroup.Slam,
            ItemGroup.Stone_Break,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),  # Does not work for Ore, does work for clippings
    GatorItemData(
        GatorItemName.GIANT_CLUB,
        100000220,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Slam,
            ItemGroup.Stone_Break,
            ItemGroup.Craft,
        ],
    ),  # This item is not a standard sword TODO: test if this works for clippings, magic ore
    GatorItemData(
        GatorItemName.JOUSTING_LANCE,
        100000221,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Dash,
            ItemGroup.Sword,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.FLASHSTEP,
        100000222,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Dash,
            ItemGroup.Sword,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.RIBBON,
        100000223,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Spin_Jump,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.BUBBLE_WAND,
        100000224,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Spin_Jump,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.PROPELLER,
        100000225,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Hover,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.QUARTERSTAFF,
        100000226,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Hover,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.DARKSWORD,
        100000227,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Sword,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.MINECART,
        100000228,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Traversal,
            ItemGroup.Shield,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.STICKY_SHIELD,
        100000229,
        ItemClassification.filler,
        1,
        [ItemGroup.Underground, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.PAINTING,
        100000230,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Shield, ItemGroup.Craft],
    ),
    GatorItemData(
        GatorItemName.BATTERING_RAM,
        100000231,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Stone_Break,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.RECORD,
        100000232,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.ROADSIGN,
        100000233,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.SURFBOARD,
        100000234,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.FILM_REEL,
        100000235,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Craft,
        ],
    ),
    GatorItemData(
        GatorItemName.DARKSHIELD,
        100000236,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Shield,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],
    ),
    GatorItemData(
        GatorItemName.BATTLE_TOP,
        100000237,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Craft],  # Same category as Bowling Bomb?
    ),
    GatorItemData(
        GatorItemName.DRONE,
        100000238,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Item, ItemGroup.Cardboard_Destroyer],
    ),  # Note: can ore #TODO: it looks like space blaster and shuriken can too
    GatorItemData(
        GatorItemName.FIREWORK,
        100000239,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Traversal,
            ItemGroup.Craft,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.RUBBER_BALL,
        100000240,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Item,
            ItemGroup.Cardboard_Destroyer,
        ],  # TODO: How does this behave on the surface # This works for magic ore...
    ),
    GatorItemData(
        GatorItemName.SPIDER_WEB,
        100000241,
        ItemClassification.progression,
        1,
        [
            ItemGroup.Underground,
            ItemGroup.Traversal,
            ItemGroup.Craft,
            ItemGroup.Ragdoll,
        ],
    ),
    GatorItemData(
        GatorItemName.GLOWY_GUNK,
        100000242,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Craft, ItemGroup.Ranged],
    ),
    GatorItemData(
        GatorItemName.THORNY,
        100000250,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.BUBBLY,
        100000251,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.CAKEY,
        100000252,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.HOLY,
        100000253,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.FINNY,
        100000254,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.DRIPPY,
        100000255,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.FLOOFY,
        100000256,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.TREEY,
        100000257,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.LOOKY,
        100000258,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item, ItemGroup.Cryptid],
    ),
    GatorItemData(
        GatorItemName.CLAM,
        100000260,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.QUEENS_SECRET_LETTER,
        100000261,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item],
    ),
    GatorItemData(
        GatorItemName.OTHER_QUEENS_SECRET_LETTER,
        100000262,
        ItemClassification.progression,
        1,
        [ItemGroup.Underground, ItemGroup.Quest_Item],
    ),
]

item_table = surface_item_table + underground_item_table

item_name_to_id: Dict[str, int] = {data.name.value: data.item_id for data in item_table}


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> Set[str]:
    item_names = set()
    for data in item_table:
        if group in data.item_groups:
            item_names.add(data.name.value)
    return item_names


item_name_groups: Dict[str, Set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)
