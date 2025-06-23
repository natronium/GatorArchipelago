from enum import Enum
from typing import Dict, List, NamedTuple

from rule_builder import Has, HasAny, Rule

old_gator_regions: Dict[str, List[str]] = {
    "Menu": ["Tutorial Island"],
    "Tutorial Island": [
        "Big Island",
        "Tutorial Island Races",
        "Tutorial Island Breakables",
        "Pots Shootable from Tutorial Island",
    ],
    "Playground": [],
    "Pots Shootable from Tutorial Island": [],
    "Tutorial Island Races": [],
    "Tutorial Island Breakables": [],
    "Big Island": [
        "Big Island Races",
        "Big Island Breakables",
        "Mountain",
        "Junk 4 Trash",
        "Big Island Bracelet Shops",
        "Playground",
    ],
    "Big Island Races": [],
    "Big Island Breakables": [],
    "Mountain": ["Mountain Breakables"],
    "Mountain Breakables": ["Pots Shootable from Tutorial Island"],
    "Junk 4 Trash": [],
    "Big Island Bracelet Shops": [],
}
class GatorRegionName(str, Enum):
    MENU = "Menu"
    TUTORIAL_ISLAND = "Tutorial Island"
    PLAYGROUND = "Playground"
    POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND = "Pots Shootable from Tutorial Island"
    TUTORIAL_ISLAND_RACES = "Tutorial Island Races"
    TUTORIAL_ISLAND_BREAKABLES = "Tutorial Island Breakables"
    BIG_ISLAND = "Big Island"
    BIG_ISLAND_RACES = "Big Island Races"
    BIG_ISLAND_BREAKABLES = "Big Island Breakables"
    MOUNTAIN = "Mountain"
    MOUNTAIN_BREAKABLES = "Mountain Breakables"
    JUNK_4_TRASH = "Junk 4 Trash"
    BIG_ISLAND_BRACELET_SHOPS = "Big Island Bracelet Shops"

class GatorEntrance(NamedTuple):
    starting_region: GatorRegionName
    ending_region: GatorRegionName
    rule: Rule | None

gator_entrances: List[GatorEntrance] = [
    GatorEntrance(GatorRegionName.MENU, GatorRegionName.TUTORIAL_ISLAND, None),
    GatorEntrance(GatorRegionName.TUTORIAL_ISLAND, GatorRegionName.BIG_ISLAND, "can_clear_tutorial"),
    GatorEntrance(GatorRegionName.TUTORIAL_ISLAND, GatorRegionName.TUTORIAL_ISLAND_RACES, None),
    GatorEntrance(GatorRegionName.TUTORIAL_ISLAND, GatorRegionName.TUTORIAL_ISLAND_BREAKABLES, "has cardboard destroyer"),
    GatorEntrance(GatorRegionName.TUTORIAL_ISLAND, GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, "has ranged"),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.BIG_ISLAND_RACES, None),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.BIG_ISLAND_BREAKABLES, "has_cardboard_destroyer"),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.BIG_ISLAND_BRACELET_SHOPS, "has_cardboard_destroyer" & Has("Bracelet")),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.JUNK_4_TRASH, "has_cardboard_destroyer"),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.PLAYGROUND, "can_complete_the_game"),
    GatorEntrance(GatorRegionName.BIG_ISLAND, GatorRegionName.MOUNTAIN, HasAny("Glider", "Bracelet")),
    GatorEntrance(GatorRegionName.MOUNTAIN, GatorRegionName.MOUNTAIN_BREAKABLES, "has_cardboard_destroyer"),
    GatorEntrance(GatorRegionName.MOUNTAIN_BREAKABLES, GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, None),
]
