from typing import Dict, NamedTuple, Set, Optional

from BaseClasses import Location

class GatorLocationData(NamedTuple):
    region: str
    # description: str
    location_group: Optional[str] = None

# Locations: quest completions, ground pickups, races, bracelet purchases, junk 4 trash

location_base_id = 9999999999 #adjust this

location_table: Dict[str, GatorLocationData] = {
    "Tutorial Island - Avery! Quest Completion": GatorLocationData("Game"),
    "Tutorial Island - Jill Quest Completion": GatorLocationData("Game"),
    "Tutorial Island - Martin Quest Completion": GatorLocationData("Game"),
    "Tutorial Island - Ragdoll (Ragdoll Bear) Quest Completion": GatorLocationData("Game"),
    "Main Island - Billy (Whale) Quest Completion": GatorLocationData("Game"),
    "Main Island - Viraj (Hot Shot Elephant) Quest Completion": GatorLocationData("Game"),
    "Main Island - Cade (Floofy Bull) Quest Completion": GatorLocationData("Game"), #Note, gives 2 friends b/c Marlow!
    "Main Island - Tiffany (Princess Cat) Quest Completion": GatorLocationData("Game"), #Note, gives 2 friends b/c Carol!
    "Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion": GatorLocationData("Game"), 
    "Avery!'s Main Quest - Velma (Western Cow) Quest Completion": GatorLocationData("Game"), #Note, gives extra friends b/c kiddos!
    "Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion": GatorLocationData("Game"), #Note, gives extra friend b/c ice cream?
    "Jill's Main Quest - Susanne (Paleolithic Antelope) Quest Completion": GatorLocationData("Game"),
    "Jill's Main Quest - Gene (Merchant ) Quest Completion": GatorLocationData("Game")
}


location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)