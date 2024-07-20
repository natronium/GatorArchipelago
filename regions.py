from typing import Dict, Set

gator_regions: Dict[str, Set[str]] = {
    "Menu": {"Tutorial Island"},
    "Tutorial Island": {
        "Big Island",
        "Tutorial Island Races",
        "Tutorial Island Breakables",
        "Pots Shootable from Tutorial Island",
        "Playground"
    },
    "Playground": set(),
    "Pots Shootable from Tutorial Island": set(),
    "Tutorial Island Races": set(),
    "Tutorial Island Breakables": set(),
    "Big Island": {
        "Big Island Races",
        "Big Island Breakables",
        "Mountain",
        "Junk 4 Trash",
        "Big Island Bracelet Shops",
    },
    "Big Island Races": set(),
    "Big Island Breakables": set(),
    "Mountain": {"Mountain Breakables"},
    "Mountain Breakables": {"Pots Shootable from Tutorial Island"},
    "Junk 4 Trash": set(),
    "Big Island Bracelet Shops": set(),
}
