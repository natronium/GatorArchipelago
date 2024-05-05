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
    "Tutorial Island - Simon (Ragdoll Bear) Quest Completion": GatorLocationData("Game"),
    "Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet": GatorLocationData("Game"),
    "Tutorial Island - Franny (Stick Duck) Quest Completion": GatorLocationData("Game"),
    "Tutorial Island - Gerald (Slime Giraffe) Quest Completion": GatorLocationData("Game"),
    "Main Island - ??? (Bracelet Monkey) Windmill Bracelet": GatorLocationData("Game"),
    "Main Island - ??? (Bracelet Monkey) Mountain Bracelet": GatorLocationData("Game"),
    "Main Island - ??? (Bracelet Monkey) Tree Bracelet": GatorLocationData("Game"),
    "Main Island - Billy (Whale) Quest Completion": GatorLocationData("Game"),
    "Main Island - Darcie (Balloon Owl) Quest Completion": GatorLocationData("Game"),
    "Main Island - Skate Pug (Skate Pug) Quest Completion": GatorLocationData("Game"),
    "Main Island - Twig (Flip Pomeranian) Quest Completion": GatorLocationData("Game"),
    "Main Island - Viraj (Hot Shot Elephant) Quest Completion": GatorLocationData("Game"),
    "Main Island - Eva (Photographer Cat) Quest Completion": GatorLocationData("Game"),
    "Main Island - Sierra (Origami Rhea) Quest Completion": GatorLocationData("Game"),
    "Main Island - Romeo (Ninja Rat) Quest Completion": GatorLocationData("Game"),
    "Main Island - Oscar (Outcast Tiger) Quest Completion": GatorLocationData("Game"),
    "Main Island - Joe (Pose Bird) Quest Completion": GatorLocationData("Game"),
    "Main Island - Broken Scooter Board Pickup (Kasen's Quest)": GatorLocationData("Game"),
    "Main Island - Kasen (Scooter Vulture) Quest Completion": GatorLocationData("Game"),
    "Main Island - Bowling Bomb Gift (Flint's Quest)": GatorLocationData("Game"),
    "Main Island - Flint (Bomb Mole) Quest Completion": GatorLocationData("Game"),
    "Main Island - Ssumantha (Waders Opposum) Quest Completion": GatorLocationData("Game"),
    "Main Island - Pot Kid (Eepy Armadillo) Quest Completion": GatorLocationData("Game"),
    "Main Island - Scooter (Ceramic-Allegy Leopard) Quest Completion": GatorLocationData("Game"),
    "Main Island - Leeland (Painting? Rabbit) Quest Completion": GatorLocationData("Game"),
    "Main Island - Esther (Directions Deer) Quest Completion": GatorLocationData("Game"),
    "Main Island - Trish (Invisible Horse) Quest Completion": GatorLocationData("Game"),
    "Main Island - Retainer Pickup (Becca's Quest)": GatorLocationData("Game"),
    "Main Island - Becca (Retainer Shark) Quest Completion": GatorLocationData("Game"),
    "Main Island - Luisa (Tripping Lizard) Quest Completion": GatorLocationData("Game"),
    "Main Island - Madeline (Little Thing Mouse) Quest Completion": GatorLocationData("Game"),
    "Main Island - Pepperoni (Obstacle Ostrich) Quest Completion": GatorLocationData("Game"),
    "Main Island - Mochi (Heights Bear) Quest Completion": GatorLocationData("Game"),
    "Main Island - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion": GatorLocationData("Game"),
    "Main Island - Rock (Zhu's Quest)": GatorLocationData("Game"),
    "Main Island - Zhu (Skipping Fox) Quest Completion": GatorLocationData("Game"),
    "Main Island - Gunther (Sidekick Hippo) Quest Completion": GatorLocationData("Game"),
    "Main Island - Tony (Chess Strategist Eagle) Quest Completion": GatorLocationData("Game"),
    "Main Island - Neil (Peptalk Mouse) Quest Completion": GatorLocationData("Game"),
    "Main Island - Robin (Scared-to-Look Robin) Quest Completion": GatorLocationData("Game"),
    "Main Island - Penelope (Barricade Beaver) Quest Completion": GatorLocationData("Game"),
    "Main Island - Mr. Doddler (No Littering Bird) Quest Completion": GatorLocationData("Game"),
    "Main Island - Cade (Floofy Bull) Quest Completion": GatorLocationData("Game"), #Note, gives 2 friends b/c Marlow!
    "Main Island - Tiffany (Princess Cat) Quest Completion": GatorLocationData("Game"), #Note, gives 2 friends b/c Carol!
    "Avery!'s Main Quest - Nerf Blaster (Andromeda's Quest)": GatorLocationData("Game"), 
    "Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion": GatorLocationData("Game"), 
    "Avery!'s Main Quest - Velma (Western Cow) Quest Completion": GatorLocationData("Game"), #Note, gives extra friends b/c kiddos!
    "Avery!'s Main Quest - Sorbet (Esme's Quest)": GatorLocationData("Game"),
    "Avery!'s Main Quest - Plastic Fangs (Esme's Quest)": GatorLocationData("Game"),
    "Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion": GatorLocationData("Game"), #Note, gives extra friend b/c ice cream Part-Timer
    "Avery!'s Main Quest - Avery!'s Main Quest Quest Completion": GatorLocationData("Game"),
    "Jill's Main Quest - Magic Ore Pickup (Susanne's Quest)": GatorLocationData("Game"),
    "Jill's Main Quest - Susanne (Paleolithic Antelope) Quest Completion": GatorLocationData("Game"),
    "Jill's Main Quest - Cheese Sandwich Pickup (Gene's Quest)": GatorLocationData("Game"),
    "Jill's Main Quest - Gene (Merchant Beaver) Quest Completion": GatorLocationData("Game"),
    "Jill's Main Quest - Bug Net Gift (Antone's Quest)": GatorLocationData("Game"),
    "Jill's Main Quest - Antone (Beetle-Loving Iguana) Quest Completion": GatorLocationData("Game"),
    "Jill's Main Quest - Jill's Main Quest Completion": GatorLocationData("Game"),
    "Martin's Main Quest - Martin Shield (Lucas's Quest)": GatorLocationData("Game"),
    "Martin's Main Quest - Lucas (Cool Wolf) Quest Completion": GatorLocationData("Game"),
    "Martin's Main Quest - Bucket Gift (Jada's Quest)": GatorLocationData("Game"),
    "Martin's Main Quest - Big Leaf Gift (Jada's Quest)": GatorLocationData("Game"),
    "Martin's Main Quest - Jada (Cool Boar) Quest Completion": GatorLocationData("Game"),
    "Martin's Main Quest - Duke (Cool Goose) Quest Completion": GatorLocationData("Game"),
    "Martin's Main Quest - Martin's Main Quest Completion": GatorLocationData("Game"),
    "Junk 4 Trash - Sticky Hand Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Trampoline Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Trash Can Lid Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Wrench Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Space Dome Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Grabby Hand Purchase": GatorLocationData("Game"),
    "Junk 4 Trash - Roy (Trash Raccoon) All Purchases": GatorLocationData("Game")
}


location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)