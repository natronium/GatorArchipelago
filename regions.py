from typing import Dict, Set

gator_regions: Dict[str,Set[str]] = {
    "Menu" : {"Tutorial Island"},
    "Tutorial Island" : {"Main Island","Tutorial Island Races", "Tutorial Island Breakables"},
    "Tutorial Island Races" : set(),
    "Tutorial Island Breakables" : set(),
    "Main Island" : {"Main Island Races", "Main Island Breakables"},
    "Main Island Races": set(),
    "Main Island Breakables": set()
    }