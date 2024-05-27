from typing import Dict, NamedTuple, Set, Optional

from BaseClasses import Location

class GatorLocationData(NamedTuple):
    region: str
    # description: str
    location_group: Optional[str] = None

# Locations: quest completions, ground pickups, races, bracelet purchases, junk 4 trash

location_base_id = 9999999999 #adjust this

location_table: Dict[str, GatorLocationData] = {
    # Northwest (Tutorial Island)
    "Tutorial Island - Avery! Hat Recipe": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Avery! Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Stick Pickup": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Jill Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Pot? Pickup": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Martin Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Simon (Ragdoll Bear) Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Franny (Stick Duck) Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Gerald (Slime Giraffe) Quest Completion": GatorLocationData("Tutorial Island"),
    "Tutorial Island - Race Next to Martin": GatorLocationData("Tutorial Island Races","Race"),
    "Tutorial Island - Race Farther from Martin": GatorLocationData("Tutorial Island Races","Race"),
    "Tutorial Island - Pot on Rock near Stick Pickup": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on down path behind Stick Pickup": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot between two waterfalls below ???": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot between two waterfalls on level with ???": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on grassy cliff behind races": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on grassy cliff above north east": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot overlooking rope bridge (to the north)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot behind tall cliffs to north": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Chest behind Gerald": GatorLocationData("Tutorial Island Breakables","Chest"),
    "Tutorial Island - Pot on cliffs in front of Gerald (1)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on cliffs in front of Gerald (2)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on cliffs in front of Gerald (3)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot by three ropes (highest)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot by three ropes (middle)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot by three ropes (lowest)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on small triangular outcropping": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on pillar": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on north tall cliffs": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on south tall cliffs, north end": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on south tall cliffs, middle": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot on south tall cliffs, south end": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Chest on south tall cliffs, south end": GatorLocationData("Tutorial Island Breakables","Chest"),
    "Tutorial Island - Pot southeast of Jill at sea level (1)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Pot southeast of Jill at sea level (2)": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Chest southeast of Jill": GatorLocationData("Tutorial Island Breakables","Chest"),
    "Tutorial Island - Pot overlooking Jill": GatorLocationData("Tutorial Island Breakables","Pot"),
    "Tutorial Island - Chest visible from bone path": GatorLocationData("Tutorial Island Breakables","Chest"),
    
    # Central (Ravine)
    "Central (Ravine) - Esther (Directions Deer) Quest Completion": GatorLocationData("Main Island"),
    "Central (Ravine) - Pot south of Esther": GatorLocationData("Main Island Breakables", "Pot"),
    

    "Main Island - ??? (Bracelet Monkey) Windmill Bracelet": GatorLocationData("Main Island"),
    "Main Island - ??? (Bracelet Monkey) Mountain Bracelet": GatorLocationData("Main Island"),
    "Main Island - ??? (Bracelet Monkey) Tree Bracelet": GatorLocationData("Main Island"),
    "Main Island - Billy (Whale) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Darcie (Balloon Owl) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Skate Pug (Skate Pug) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Twig (Flip Pomeranian) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Viraj (Hot Shot Elephant) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Eva (Photographer Cat) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Sam (Pencil Jackal) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Sierra (Origami Rhea) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Romeo (Ninja Rat) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Oscar (Outcast Tiger) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Joe (Pose Hawk) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Broken Scooter Board Pickup (Kasen's Quest)": GatorLocationData("Main Island"),
    "Main Island - Kasen (Scooter Vulture) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Bowling Bomb Gift (Flint's Quest)": GatorLocationData("Main Island"),
    "Main Island - Flint (BombBowl Mole) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Ssumantha (Waders Opposum) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Pot Kid (Eepy Armadillo) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Scooter (Ceramic-Allegy Leopard) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Leeland (Painting Rabbit) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Trish (Invisible Horse) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Retainer Pickup (Becca's Quest)": GatorLocationData("Main Island"),
    "Main Island - Becca (Retainer Shark) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Luisa (Tripping Lizard) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Madeline (Little Thing Mouse) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Pepperoni (Obstacle Ostrich) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Mochi (Heights Bear) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Rock (Zhu's Quest)": GatorLocationData("Main Island"),
    "Main Island - Zhu (Skipping Fox) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Gunther (Sidekick Hippo) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Tony (Chess Strategist Eagle) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Neil (Peptalk Rat) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Robin (Scared-to-Look Robin) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Penelope (Bastion Beaver) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Mr. Doddler (No Littering Bird) Quest Completion": GatorLocationData("Main Island"),
    "Main Island - Cade (Floofy Bull) Quest Completion": GatorLocationData("Main Island"), #Note, gives 2 friends b/c Marlow!
    "Main Island - Tiffany (Princess Cat) Quest Completion": GatorLocationData("Main Island"), #Note, gives 2 friends b/c Carol!
    "Main Island - Tanner (Pot Mimic Elk) Quest Completion": GatorLocationData("Main Island"),
    "Avery!'s Main Quest - Nerf Blaster (Andromeda's Quest)": GatorLocationData("Main Island"), 
    "Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion": GatorLocationData("Main Island"), 
    "Avery!'s Main Quest - Velma (Western Cow) Quest Completion": GatorLocationData("Main Island"), #Note, gives extra friends b/c kiddos!
    "Avery!'s Main Quest - Sorbet (Esme's Quest)": GatorLocationData("Main Island"),
    "Avery!'s Main Quest - Plastic Fangs (Esme's Quest)": GatorLocationData("Main Island"),
    "Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion": GatorLocationData("Main Island"), #Note, gives extra friend b/c ice cream Part-Timer
    "Avery!'s Main Quest - Avery!'s Main Quest Quest Completion": GatorLocationData("Main Island"),
    "Jill's Main Quest - Magic Ore Pickup (Susanne's Quest)": GatorLocationData("Main Island"),
    "Jill's Main Quest - Susanne (Paleolithic Antelope) Quest Completion": GatorLocationData("Main Island"),
    "Jill's Main Quest - Cheese Sandwich Pickup (Gene's Quest)": GatorLocationData("Main Island"),
    "Jill's Main Quest - Gene (Merchant Beaver) Quest Completion": GatorLocationData("Main Island"),
    "Jill's Main Quest - Bug Net Gift (Antone's Quest)": GatorLocationData("Main Island"),
    "Jill's Main Quest - Antone (Beetle-Loving Iguana) Quest Completion": GatorLocationData("Main Island"),
    "Jill's Main Quest - Jill's Main Quest Completion": GatorLocationData("Main Island"),
    "Martin's Main Quest - Martin Shield (Lucas's Quest)": GatorLocationData("Main Island"),
    "Martin's Main Quest - Lucas (Cool Wolf) Quest Completion": GatorLocationData("Main Island"),
    "Martin's Main Quest - Bucket Gift (Jada's Quest)": GatorLocationData("Main Island"),
    "Martin's Main Quest - Big Leaf Gift (Jada's Quest)": GatorLocationData("Main Island"),
    "Martin's Main Quest - Jada (Cool Boar) Quest Completion": GatorLocationData("Main Island"),
    "Martin's Main Quest - Duke (Cool Goose) Quest Completion": GatorLocationData("Main Island"),
    "Martin's Main Quest - Martin's Main Quest Completion": GatorLocationData("Main Island"),
    "Junk 4 Trash - Sticky Hand Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Trampoline Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Trash Can Lid Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Wrench Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Space Dome Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Grabby Hand Purchase": GatorLocationData("Main Island"),
    "Junk 4 Trash - Roy (Trash Raccoon) All Purchases": GatorLocationData("Main Island")
}


location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)