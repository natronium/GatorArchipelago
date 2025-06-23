from enum import Enum, auto
from typing import Dict, NamedTuple, Set, List

from .regions import GatorRegionName


class LocationGroup(Enum):
    Pot = auto()
    Chest = auto()
    Race = auto()

class GatorLocationName(str, Enum):
    AVERY_Q_ANDROMEDA_ITEM = "Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion Item"
    AVERY_Q_ESME_NPC = "Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion NPC"
    AVERY_Q_NERF_BLASTER = "Avery!'s Main Quest - Nerf Blaster (Andromeda's Quest)"
    AVERY_Q_NPCS = "Avery!'s Main Quest - Avery!'s Main Quest Quest Completion NPCs"
    AVERY_Q_PLASTIC_FANGS = "Avery!'s Main Quest - Plastic Fangs (Esme's Quest)"
    AVERY_Q_SORBET = "Avery!'s Main Quest - Sorbet (Esme's Quest)"
    AVERY_Q_VELMA_ITEM = "Avery!'s Main Quest - Velma (Western Cow) Quest Completion Item"
    BCH_CADE_NPCS = "Southeast (Beach) - Cade (Floofy Bull) Quest Completion NPCs"
    BCH_CHEST_H9 = "Southeast (Beach) - Chest (H9) on north end of Skate Pug's island"
    BCH_JOE_NPC = "Southeast (Beach) - Joe (Pose Hawk) Quest Completion NPC"
    BCH_MR_DODDLER_ITEM = "Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion Item"
    BCH_MR_DODDLER_NPC = "Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion NPC"
    BCH_POT_H8 = "Southeast (Beach) - Pot (H8) on taller section northwest of Skate Pug"
    BCH_POT_I6 = "Southeast (Beach) - Pot (I6) on small island south of Marlow's deck"
    BCH_POT_I9_E = "Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (east)"
    BCH_POT_I9_W = "Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (west)"
    BCH_POT_J6 = "Southeast (Beach) - Pot (J6) on small tall island east of Leeland's peninsula"
    BCH_SAM_ITEM = "Southeast (Beach) - Sam (Pencil Jackal) Quest Completion Item"
    BCH_SAM_NPC = "Southeast (Beach) - Sam (Pencil Jackal) Quest Completion NPC"
    BCH_SKATE_PUG_ITEM = "Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion Item"
    BCH_SKATE_PUG_NPCS = "Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion NPCs"
    BCH_THROWN_PENCIL_1 = "Southeast (Beach) - Thrown Pencil 1 (Sam's Quest)"
    BCH_THROWN_PENCIL_2 = "Southeast (Beach) - Thrown Pencil 2 (Sam's Quest)"
    BCH_THROWN_PENCIL_3 = "Southeast (Beach) - Thrown Pencil 3 (Sam's Quest)"
    BCH_TONY_ITEM = "Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion Item"
    BCH_TONY_NPC = "Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion NPC"
    BCH_VIRAJ_NPC = "Southeast (Beach) - Viraj (Hot Shot Elephant) Quest Completion NPC"
    BI_BILLY_ITEM = "Big Island - Billy (Whale) Quest Completion Item"
    BI_BILLY_NPC = "Big Island - Billy (Whale) Quest Completion NPC"
    BI_BRACELET_MONKEY_ALL_BRACELETS_NPC = "Big Island - ??? (Bracelet Monkey) All Bracelets NPC"
    BI_ROCK = "Big Island - Rock (Zhu's Quest)"
    BI_ZHU_NPC = "Big Island - Zhu (Skipping Fox) Quest Completion NPC"
    CAN_BROKEN_SCOOTER_BOARD = "Northeast (Canyon) - Broken Scooter Board Pickup (Kasen's Quest)"
    CAN_CHEST_D8 = "Northeast (Canyon) - Chest (D8) on peak northwest of Jada's pump"
    CAN_DARCIE_ITEM = "Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion Item"
    CAN_DARCIE_NPC = "Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion NPC"
    CAN_KASEN_ITEM = "Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion Item"
    CAN_KASEN_NPC = "Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion NPC"
    CAN_MOCHI_NPC = "Northeast (Canyon) - Mochi (Heights Bear) Quest Completion NPC"
    CAN_POT_A8_N = "Northeast (Canyon) - Pot (A8) on north peak accessible from Billy"
    CAN_POT_A8_W = "Northeast (Canyon) - Pot (A8) on west peak accessible from Billy"
    CAN_POT_B8 = "Northeast (Canyon) - Pot (B8) on tall rock southwest from Billy's Canyon location"
    CAN_POT_C7 = "Northeast (Canyon) - Pot (C7) on cliffside west of and below Mochi"
    CAN_POT_C8_OUTCROP = "Northeast (Canyon) - Pot (C8) at end of Kasen's stone outcropping"
    CAN_POT_C8_MOCHI = "Northeast (Canyon) - Pot (C8) on cliffside east of and below Mochi"
    CAN_POT_C9_LOWER = "Northeast (Canyon) - Pot (C9) on Ssumantha's island (lower)"
    CAN_POT_C9_UPPER = "Northeast (Canyon) - Pot (C9) on Ssumantha's island (upper)"
    CAN_POT_D6 = "Northeast (Canyon) - Pot (D6) on island in middle of pond northeast of playground"
    CAN_POT_D7_N = "Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (north)"
    CAN_POT_D7_S = "Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (south)"
    CAN_POT_D8 = "Northeast (Canyon) - Pot (D8) on peak northwest of Jada's pump"
    CAN_RACE_B6 = "Northeast (Canyon) - Race (B6) starting east of waterfall on north side of Mountain"
    CAN_RACE_C7 = "Northeast (Canyon) - Race (C7) starting west of Kasen"
    CAN_SSUMANTHA_ITEM = "Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion Item"
    CAN_SSUMANTHA_NPC = "Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion NPC"
    CRL_BECCA_NPC = "East (Creeklands) - Becca (Retainer Shark) Quest Completion NPC"
    CRL_BRACELET_MONKEY_WINDMILL = "East (Creeklands) - ??? (Bracelet Monkey) Windmill Bracelet"
    CRL_CHEST_G6 = "East (Creeklands) - Chest (G6) north of Junk4Trash"
    CRL_CHEST_G8 = "East (Creeklands) - Chest (G8) on peak south of Splash Pad"
    CRL_CHEST_H5 = "East (Creeklands) - Chest (H5) on peak north-northwest of Tony's chessboard"
    CRL_MADELINE_NPC = "East (Creeklands) - Madeline (Little Thing Mouse) Quest Completion NPC"
    CRL_POT_D8 = "East (Creeklands) - Pot (D8) northwest of Jada's pump below taller cliffs"
    CRL_POT_E7_NE = "East (Creeklands) - Pot (E7) northwest of Splash Pad below cliff to northeast"
    CRL_POT_E7_NW = "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (northwest)"
    CRL_POT_E7_SE = "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southeast)"
    CRL_POT_E7_SW = "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southwest)"
    CRL_POT_F7 = "East (Creeklands) - Pot (F7) south of Splash Pad"
    CRL_POT_F9 = "East (Creeklands) - Pot (F9) on peak north of Duke's pump"
    CRL_POT_G5 = "East (Creeklands) - Pot (G5) west of Junk4Trash in secluded area filled with ninjas and mimics"
    CRL_POT_H5_N = "East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (north)"
    CRL_POT_H5_S = "East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (south)"
    CRL_RETAINER = "East (Creeklands) - Retainer Pickup (Becca's Quest)"
    CRL_ROBIN_ITEM = "East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion Item"
    CRL_ROBIN_NPC = "East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion NPC"
    FOR_BRACELET_MONKEY_TREE = "West (Forest) - ??? (Bracelet Monkey) Tree Bracelet"
    FOR_CHEST_H4 = "West (Forest) - Chest (H4) on tallest peak north of Pepperoni's obstacle course"
    FOR_EVA_ITEM = "West (Forest) - Eva (Photographer Cat) Quest Completion Item"
    FOR_EVA_NPC = "West (Forest) - Eva (Photographer Cat) Quest Completion NPC"
    FOR_GUNTHER_NPC = "West (Forest) - Gunther (Sidekick Hippo) Quest Completion NPC"
    FOR_NINJA_CLAN_ITEM = "West (Forest) - Ninja Clan Quest Completion Item"
    FOR_NINJA_CLAN_NPCS = "West (Forest) - Ninja Clan Quest Completion NPCs"
    FOR_PENELOPE_ITEM = "West (Forest) - Penelope (Bastion Beaver) Quest Completion Item"
    FOR_PENELOPE_NPC = "West (Forest) - Penelope (Bastion Beaver) Quest Completion NPC"
    FOR_PEPPERONI_ITEM = "West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion Item"
    FOR_PEPPERONI_NPCS = "West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion NPCs"
    FOR_POT_E1_LOWER_E = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and down the cliff)"
    FOR_POT_E1_UPPER_E = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and up the cliff)"
    FOR_POT_E1_UPPER_W = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (west and up the cliff)"
    FOR_POT_F3 = "West (Forest) - Pot (F3) on north cliff edge of pond with dead trees"
    FOR_POT_G3_CLIFF = "West (Forest) - Pot (G3) on cliff overlooking pond with dead trees from the west side"
    FOR_POT_G3_POND = "West (Forest) - Pot (G3) on west edge of pond with dead trees"
    FOR_POT_G4_DEAD_POND = "West (Forest) - Pot (G4) on south edge of pond with dead trees"
    FOR_POT_G4_E_E = "West (Forest) - Pot (G4) on tall peak east of pond with dead trees (east)"
    FOR_POT_G4_E_W = "West (Forest) - Pot (G4) on tall peak east of pond with dead trees (west)"
    FOR_POT_G4_S = "West (Forest) - Pot (G4) south of tall peak east of pond with dead trees"
    FOR_POT_H2 = "West (Forest) - Pot (H2) above Trish (Invisible Horse)"
    FOR_POT_H4_E = "West (Forest) - Pot (H4) east of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_H4_N = "West (Forest) - Pot (H4) north of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_H4_S = "West (Forest) - Pot (H4) south of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_J0 = "West (Forest) - Pot (J0) in tidepool in southwest corner of island (northwest)"
    FOR_POT_J1_SE = "West (Forest) - Pot (J1) in tidepool in southwest corner of island (southeast)"
    FOR_POT_J1_SW = "West (Forest) - Pot (J1) in tidepool in southwest corner of island (southwest)"
    FOR_POT_J3_E = "West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (east)"
    FOR_POT_J3_W = "West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (west)"
    FOR_POT_KID_NPC = "West (Forest) - Pot Kid (Eepy Armadillo) Quest Completion NPC"
    FOR_RACE_F4 = "West (Forest) - Race (F4) starting from west path exit from playground"
    FOR_RACE_G0 = "West (Forest) - Race (G0) starting from island west of Billy's Forest location"
    FOR_RACE_H1 = "West (Forest) - Race (H1) starting from southwest of The Tree"
    FOR_ROMEO_NUNCHUCKS = "West (Forest) - Romeo (Ninja Anteater) Nunchucks"
    FOR_SIERRA_ITEM = "West (Forest) - Sierra (Origami Crane) Quest Completion Item"
    FOR_SIERRA_NPC = "West (Forest) - Sierra (Origami Crane) Quest Completion NPC"
    FOR_SORIN_ROE_BEERITNEY_ITEM = "West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion Item"
    FOR_SORIN_ROE_BEERITNEY_NPCS = "West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion NPCs"
    FOR_TIFFANY_ITEM = "West (Forest) - Tiffany (Princess Cat) Quest Completion Item"
    FOR_TIFFANY_NPCS = "West (Forest) - Tiffany (Princess Cat) Quest Completion NPCs"
    FOR_TRISH_NPC = "West (Forest) - Trish (Invisible Horse) Quest Completion NPC"
    J4T_GRABBY_HAND = "Junk 4 Trash - Grabby Hand Purchase"
    J4T_PAINT_GUN = "Junk 4 Trash - Paint Gun Purchase"
    J4T_ROY_ALL_PURCHASES_NPC = "Junk 4 Trash - Roy (Trash Raccoon) All Purchases NPC"
    J4T_STICKY_HAND = "Junk 4 Trash - Sticky Hand Purchase"
    J4T_TRAMPOLINE = "Junk 4 Trash - Trampoline Purchase"
    J4T_TRASH_CAN_LID = "Junk 4 Trash - Trash Can Lid Purchase"
    J4T_WRENCH = "Junk 4 Trash - Wrench Purchase"
    JET_LEELAND_ITEM = "South (Jetty) - Leeland (Painting Rabbit) Quest Completion Item"
    JET_LEELAND_NPC = "South (Jetty) - Leeland (Painting Rabbit) Quest Completion NPC"
    JILL_Q_BUG_NET_GIFT = "Jill's Main Quest - Bug Net Gift (Antone's Quest)"
    JILL_Q_CHEESE_SANDWICH = "Jill's Main Quest - Cheese Sandwich Pickup (Gene's Quest)"
    JILL_Q_GENE_ITEM = "Jill's Main Quest - Gene (Merchant Beaver) Quest Completion Item"
    JILL_Q_MAGIC_ORE = "Jill's Main Quest - Magic Ore Pickup (Susanne's Quest)"
    JILL_Q_NPCS = "Jill's Main Quest - Jill's Main Quest Completion NPCs"
    JILL_Q_SUSANNE = "Jill's Main Quest - Susanne (Paleolithic Gazelle) Quest Completion"
    MARTIN_Q_BUCKET_GIFT = "Martin's Main Quest - Bucket Gift (Jada's Quest)"
    MARTIN_Q_DUKE_ITEM = "Martin's Main Quest - Duke (Cool Goose) Quest Completion Item"
    MARTIN_Q_GRASSING_CLIPPINGS = "Martin's Main Quest - Grassing Clippings Collect (Jada's Quest)"
    MARTIN_Q_JADA_ITEM = "Martin's Main Quest - Jada (Cool Boar) Quest Completion Item"
    MARTIN_Q_LUCAS_ITEM = "Martin's Main Quest - Lucas (Cool Wolf) Quest Completion Item"
    MARTIN_Q_NPCS = "Martin's Main Quest - Martin's Main Quest Completion NPCs"
    MARTIN_Q_WATER = "Martin's Main Quest - Water Collect (Jada's Quest)"
    MTN_BOWLING_BOMB_GIFT = "North (Mountain) - Bowling Bomb Gift (Flint's Quest)"
    MTN_BRACELET_MONKEY_MOUNTAIN = "North (Mountain) - ??? (Bracelet Monkey) Mountain Bracelet"
    MTN_CHEST_B3 = "North (Mountain) - Chest (B3) on northwest cliffside of Mountain"
    MTN_CHEST_C5 = "North (Mountain) - Chest (C5) below rope northwest of stage area"
    MTN_FLINT_NPC = "North (Mountain) - Flint (BombBowl Mole) Quest Completion NPC"
    MTN_LUISA_ITEM = "North (Mountain) - Luisa (Tripping Lizard) Quest Completion Item"
    MTN_LUISA_NPC = "North (Mountain) - Luisa (Tripping Lizard) Quest Completion NPC"
    MTN_NEIL_ITEM = "North (Mountain) - Neil (Peptalk Rat) Quest Completion Item"
    MTN_NEIL_NPC = "North (Mountain) - Neil (Peptalk Rat) Quest Completion NPC"
    MTN_POT_B4_E = "North (Mountain) - Pot (B4) on cliffside cutout east of raised area in northwest corner of Mountain (east)"
    MTN_POT_B4_W = "North (Mountain) - Pot (B4) on cliffside cutout east of raised area in northwest corner of Mountain (west)"
    MTN_POT_B4_CENTER = "North (Mountain) - Pot (B4) on raised area in northwest corner of Mountain (center)"
    MTN_POT_B4_NE = "North (Mountain) - Pot (B4) on raised area in northwest corner of Mountain (northeast)"
    MTN_POT_B5_TANNER = "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (next to Tanner)"
    MTN_POT_B5_SW = "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (southwest of Tanner)"
    MTN_POT_B5_ROCK = "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (up on rock formation)"
    MTN_POT_C3_CLIFFFACE = "North (Mountain) - Pot (C3) on cliff area across from Martin's deck (next to cliffface)"
    MTN_POT_C3_RAISED = "North (Mountain) - Pot (C3) on cliff area across from Martin's deck (on raised section)"
    MTN_POT_C3_DOWN_FROM_TWIG = "North (Mountain) - Pot (C3) on cliff outcropping northwest and down from Twig"
    MTN_POT_C3_SW = "North (Mountain) - Pot (C3) on raised area in northwest corner of Mountain (southwest)"
    MTN_POT_C4_NW_TALL = "North (Mountain) - Pot (C4) on northwest tall peak, north of race"
    MTN_POT_C4_NE = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (northeast)"
    MTN_POT_C4_PEAK_E = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, east)"
    MTN_POT_C4_PEAK_W = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, west)"
    MTN_POT_C4_SW = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (southwest)"
    MTN_POT_C4_W = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (west)"
    MTN_POT_C5 = "North (Mountain) - Pot (C5) west and up from stage"
    MTN_POT_D3 = "North (Mountain) - Pot (D3) on cliff outcropping west and down from Twig"
    MTN_RACE_C4 = "North (Mountain) - Race (C4) starting on western peak of the Mountain"
    MTN_RACE_D5 = "North (Mountain) - Race (D5) starting north of the playground and heading up the Mountain"
    MTN_SCOOTER_NPC = "North (Mountain) - Scooter (Ceramic-Allergy Cougar) Quest Completion NPC"
    MTN_TANNER_NPC = "North (Mountain) - Tanner (Pot Mimic Elk) Quest Completion NPC"
    MTN_TWIG_NPC = "North (Mountain) - Twig (Flip Pomeranian) Quest Completion NPC"
    RAV_CHEST_E4 = "Central (Ravine) - Chest (E4) under overhang near river"
    RAV_ESTHER_NPC = "Central (Ravine) - Esther (Directions Deer) Quest Completion NPC"
    RAV_POT_E2 = "Central (Ravine) - Pot (E2) on hill on path east from Penelope's waterfall"
    RAV_POT_E3_BEACH = "Central (Ravine) - Pot (E3) south of beach where Esther roams"
    RAV_POT_E3_RIVER = "Central (Ravine) - Pot (E3) south of central river east of path south from Esther"
    RAV_POT_E4 = "Central (Ravine) - Pot (E4) on northern tall peak west of playground"
    RAV_POT_F4 = "Central (Ravine) - Pot (F4) on southern tall peak west of playground"
    TI_AVERY = "Tutorial Island - Avery! Quest Completion"
    TI_AVERY_HAT_RECIPE = "Tutorial Island - Avery! Hat Recipe"
    TI_BRACELET_MONKEY_TUTORIAL = "Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet"
    TI_CHEST_A3 = "Tutorial Island - Chest (A3) below Gerald to east"
    TI_CHEST_B1_MID_CLIFF = "Tutorial Island - Chest (B1) on mid-cliff outcropping visible from bone path on the west of Tutorial Island"
    TI_CHEST_B1_TALLEST = "Tutorial Island - Chest (B1) on tallest peak of Tutorial Island"
    TI_CHEST_D1 = "Tutorial Island - Chest (D1) on small island south of Jill's picnic table"
    TI_FRANNY_ITEM = "Tutorial Island - Franny (Stick Duck) Quest Completion Item"
    TI_FRANNY_NPC = "Tutorial Island - Franny (Stick Duck) Quest Completion NPC"
    TI_GERALD_ITEM = "Tutorial Island - Gerald (Slime Giraffe) Quest Completion Item"
    TI_GERALD_NPC = "Tutorial Island - Gerald (Slime Giraffe) Quest Completion NPC"
    TI_MARTIN = "Tutorial Island - Martin Quest Completion"
    TI_POT_Q = "Tutorial Island - Pot? Pickup"
    TI_POT_A1 = "Tutorial Island - Pot (A1) near highest rope of the three ropes in northwest of Tutorial Island"
    TI_POT_A3_BELOW_E = "Tutorial Island - Pot (A3) on green outcropping below and east of cliffs east of three ropes"
    TI_POT_A3_WITHIN_CLIFFS = "Tutorial Island - Pot (A3) on green outcropping within cliffs east of three ropes"
    TI_POT_B0_BONE_PATH = "Tutorial Island - Pot (B0) at the end of the bone path on the west of Tutorial Island"
    TI_POT_B0_SW = "Tutorial Island - Pot (B0) southwest of the three ropes in northwest of Tutorial Island"
    TI_POT_B1_WATERFALL_BELOW = "Tutorial Island - Pot (B1) between two waterfalls below ???'s Tutorial Island location"
    TI_POT_B1_WATERFALL_NEXT_TO = "Tutorial Island - Pot (B1) between two waterfalls on same level as ???'s Tutorial Island location"
    TI_POT_B1_MIDDLE_ROPE = "Tutorial Island - Pot (B1) near middle rope of the three ropes in northwest of Tutorial Island"
    TI_POT_B1_PEAK_N = "Tutorial Island - Pot (B1) on peak north of tallest peak on Tutorial Island"
    TI_POT_B1_PEAK_S = "Tutorial Island - Pot (B1) on peak south of the three ropes in northwest of Tutorial Island"
    TI_POT_B1_WATERFALL_PILLAR = "Tutorial Island - Pot (B1) on pillar by waterfalls"
    TI_POT_B1_W_ROPE = "Tutorial Island - Pot (B1) west of rope to tallest peaks on Tutorial Island"
    TI_POT_B2_BELOW_E = "Tutorial Island - Pot (B2) below Gerald to the south near water level (eastmost)"
    TI_POT_B2_BELOW_MIDDLE = "Tutorial Island - Pot (B2) below Gerald to the south near water level (middle)"
    TI_POT_B2_BELOW_W = "Tutorial Island - Pot (B2) below Gerald to the south near water level (westmost)"
    TI_POT_B2_SIMON_E = "Tutorial Island - Pot (B2) on green cliff east of Simon's starting location"
    TI_POT_B2_NW = "Tutorial Island - Pot (B2) on green cliff northwest of Martin's lawn chairs"
    TI_POT_B2_TALL = "Tutorial Island - Pot (B2) on tall peak west of Gerald"
    TI_POT_C1_HILL = "Tutorial Island - Pot (C1) on hill overlooking Jill's picnic table"
    TI_POT_C1_STICK = "Tutorial Island - Pot (C1) on rock near Stick pickup location"
    TI_POT_C2 = "Tutorial Island - Pot (C2) on cliff overlooking rope crossing the waterfall"
    TI_POT_D0 = "Tutorial Island - Pot (D0) on small peninsula southwest of Jill's picnic table"
    TI_POT_D1 = "Tutorial Island - Pot (D1) on small island with chest south of Jill's picnic table"
    TI_RACE_C2_CLIFF = "Tutorial Island - Race (C2) starting near grassy cliff"
    TI_RACE_C2_MARTIN = "Tutorial Island - Race (C2) starting near Martin's lawn chairs"
    TI_SIMON_ITEM = "Tutorial Island - Simon (Ragdoll Bear) Quest Completion Item"
    TI_SIMON_NPC = "Tutorial Island - Simon (Ragdoll Bear) Quest Completion NPC"
    TI_STICK = "Tutorial Island - Stick Pickup"


class GatorLocationData(NamedTuple):
    name: GatorLocationName
    location_id: int
    region: GatorRegionName
    location_group: LocationGroup | None
    access_rules : List[str]
  
    def __repr__(self) -> str:
        return f"GatorLocationData(\n{self.name},\n{self.location_id},\n{self.region},\n{self.location_group},\n{self.access_rules})\n"

location_table: List[GatorLocationData] = [
    GatorLocationData(
        GatorLocationName.AVERY_Q_ANDROMEDA_ITEM,
        100002280,
        GatorRegionName.MOUNTAIN,
        None,
        ['$ranged', '$hard,$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.AVERY_Q_ESME_NPC,
        100002284,
        GatorRegionName.MOUNTAIN,
        None,
        ['sorbet']),
    GatorLocationData(
        GatorLocationName.AVERY_Q_NERF_BLASTER,
        100002279,
        GatorRegionName.MOUNTAIN,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.AVERY_Q_NPCS,
        100002285,
        GatorRegionName.MOUNTAIN,
        None,
        ['sorbet,$ranged', '$hard,sorbet,$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.AVERY_Q_PLASTIC_FANGS,
        100002283,
        GatorRegionName.MOUNTAIN,
        None,
        ['sorbet']),
    GatorLocationData(
        GatorLocationName.AVERY_Q_SORBET,
        100002282,
        GatorRegionName.MOUNTAIN,
        None,
        []),
    GatorLocationData(
        GatorLocationName.AVERY_Q_VELMA_ITEM,
        100002281,
        GatorRegionName.MOUNTAIN,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BCH_CADE_NPCS,
        100002221,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BCH_CHEST_H9,
        100000201,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.BCH_JOE_NPC,
        100002224,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BCH_MR_DODDLER_ITEM,
        100002220,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_MR_DODDLER_NPC,
        100002219,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_POT_H8,
        100000082,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.BCH_POT_I6,
        100000115,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.BCH_POT_I9_E,
        100000077,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.BCH_POT_I9_W,
        100000069,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.BCH_POT_J6,
        100000101,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.BCH_SAM_ITEM,
        100002217,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$has_at_least_n_pencil|3']),
    GatorLocationData(
        GatorLocationName.BCH_SAM_NPC,
        100002216,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$has_at_least_n_pencil|3']),
    GatorLocationData(
        GatorLocationName.BCH_SKATE_PUG_ITEM,
        100002223,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_SKATE_PUG_NPCS,
        100002222,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_1,
        100002213,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_2,
        100002214,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$has_at_least_n_pencil|1']),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_3,
        100002215,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$has_at_least_n_pencil|2']),
    GatorLocationData(
        GatorLocationName.BCH_TONY_ITEM,
        100002212,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_TONY_NPC,
        100002211,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BCH_VIRAJ_NPC,
        100002218,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.BI_BILLY_ITEM,
        100002288,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BI_BILLY_NPC,
        100002287,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BI_BRACELET_MONKEY_ALL_BRACELETS_NPC,
        100002295,
        GatorRegionName.BIG_ISLAND_BRACELET_SHOPS,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BI_ROCK,
        100002289,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.BI_ZHU_NPC,
        100002290,
        GatorRegionName.BIG_ISLAND,
        None,
        ['rock']),
    GatorLocationData(
        GatorLocationName.CAN_BROKEN_SCOOTER_BOARD,
        100002205,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.CAN_CHEST_D8,
        100001360,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CAN_DARCIE_ITEM,
        100002204,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$ranged']),
    GatorLocationData(
        GatorLocationName.CAN_DARCIE_NPC,
        100002203,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$ranged']),
    GatorLocationData(
        GatorLocationName.CAN_KASEN_ITEM,
        100002207,
        GatorRegionName.BIG_ISLAND,
        None,
        ['broken_scooter']),
    GatorLocationData(
        GatorLocationName.CAN_KASEN_NPC,
        100002206,
        GatorRegionName.BIG_ISLAND,
        None,
        ['broken_scooter']),
    GatorLocationData(
        GatorLocationName.CAN_MOCHI_NPC,
        100002210,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_A8_N,
        100001463,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_A8_W,
        100001456,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_B8,
        100002070,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', '$has_at_least_n_bracelet|2']),
    GatorLocationData(
        GatorLocationName.CAN_POT_C7,
        100001350,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_C8_MOCHI,
        100001351,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_C8_OUTCROP,
        100001349,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_C9_LOWER,
        100002071,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_C9_UPPER,
        100002072,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_D6,
        100000006,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CAN_POT_D7_N,
        100001362,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', 'glider', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.CAN_POT_D7_S,
        100001363,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', 'glider', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.CAN_POT_D8,
        100001361,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CAN_RACE_B6,
        100000813,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.CAN_RACE_C7,
        100000753,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.CAN_SSUMANTHA_ITEM,
        100002209,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.CAN_SSUMANTHA_NPC,
        100002208,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.CRL_BECCA_NPC,
        100002229,
        GatorRegionName.BIG_ISLAND,
        None,
        ['retainer']),
    GatorLocationData(
        GatorLocationName.CRL_BRACELET_MONKEY_WINDMILL,
        100002292,
        GatorRegionName.BIG_ISLAND_BRACELET_SHOPS,
        None,
        []),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_G6,
        100002026,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_G8,
        100000153,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_H5,
        100000766,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CRL_MADELINE_NPC,
        100002225,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_D8,
        100000491,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_NE,
        100000062,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_NW,
        100001431,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_SE,
        100001444,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_SW,
        100000655,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_F7,
        100000117,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_F9,
        100000651,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CRL_POT_G5,
        100002012,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.CRL_POT_H5_N,
        100000722,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CRL_POT_H5_S,
        100000721,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.CRL_RETAINER,
        100002228,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.CRL_ROBIN_ITEM,
        100002227,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.CRL_ROBIN_NPC,
        100002226,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_BRACELET_MONKEY_TREE,
        100002293,
        GatorRegionName.BIG_ISLAND_BRACELET_SHOPS,
        None,
        []),
    GatorLocationData(
        GatorLocationName.FOR_CHEST_H4,
        100001518,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_EVA_ITEM,
        100002259,
        GatorRegionName.BIG_ISLAND,
        None,
        ['bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_EVA_NPC,
        100002258,
        GatorRegionName.BIG_ISLAND,
        None,
        ['bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_GUNTHER_NPC,
        100002260,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.FOR_NINJA_CLAN_ITEM,
        100002250,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,bracelet', '$ranged']),
    GatorLocationData(
        GatorLocationName.FOR_NINJA_CLAN_NPCS,
        100002249,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,bracelet', '$ranged']),
    GatorLocationData(
        GatorLocationName.FOR_PENELOPE_ITEM,
        100002257,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$ranged', '$hard,$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_PENELOPE_NPC,
        100002256,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$ranged', '$hard,$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_PEPPERONI_ITEM,
        100002252,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_PEPPERONI_NPCS,
        100002251,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_LOWER_E,
        100001381,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_UPPER_E,
        100001382,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_UPPER_W,
        100001380,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_F3,
        100000025,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_G3_CLIFF,
        100001450,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_G3_POND,
        100000545,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_DEAD_POND,
        100000546,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_E_E,
        100001540,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_E_W,
        100001541,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_S,
        100001542,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.FOR_POT_H2,
        100000094,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_E,
        100001520,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_N,
        100001532,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_S,
        100001517,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.FOR_POT_J0,
        100001593,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_J1_SE,
        100001596,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_J1_SW,
        100001594,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_J3_E,
        100001584,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.FOR_POT_J3_W,
        100001583,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.FOR_POT_KID_NPC,
        100002255,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_RACE_F4,
        100001409,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        []),
    GatorLocationData(
        GatorLocationName.FOR_RACE_G0,
        100000072,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.FOR_RACE_H1,
        100001399,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        []),
    GatorLocationData(
        GatorLocationName.FOR_ROMEO_NUNCHUCKS,
        100002248,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,bracelet', '$ranged']),
    GatorLocationData(
        GatorLocationName.FOR_SIERRA_ITEM,
        100002247,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_SIERRA_NPC,
        100002246,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_SORIN_ROE_BEERITNEY_ITEM,
        100002254,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.FOR_SORIN_ROE_BEERITNEY_NPCS,
        100002253,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.FOR_TIFFANY_ITEM,
        100002263,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_TIFFANY_NPCS,
        100002262,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.FOR_TRISH_NPC,
        100002261,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_GRABBY_HAND,
        100002242,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_PAINT_GUN,
        100002241,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_ROY_ALL_PURCHASES_NPC,
        100002243,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_STICKY_HAND,
        100002237,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_TRAMPOLINE,
        100002238,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_TRASH_CAN_LID,
        100002239,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.J4T_WRENCH,
        100002240,
        GatorRegionName.JUNK_4_TRASH,
        None,
        []),
    GatorLocationData(
        GatorLocationName.JET_LEELAND_ITEM,
        100002245,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.JET_LEELAND_NPC,
        100002244,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.JILL_Q_BUG_NET_GIFT,
        100002268,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.JILL_Q_CHEESE_SANDWICH,
        100002266,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.JILL_Q_GENE_ITEM,
        100002267,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$cardboard_destroyer,sandwich']),
    GatorLocationData(
        GatorLocationName.JILL_Q_MAGIC_ORE,
        100002264,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.JILL_Q_NPCS,
        100002269,
        GatorRegionName.BIG_ISLAND,
        None,
        ['bug_net,$sword,sandwich,ore', 'bug_net,$ranged,sandwich,ore']),
    GatorLocationData(
        GatorLocationName.JILL_Q_SUSANNE,
        100002265,
        GatorRegionName.BIG_ISLAND,
        None,
        ['ore,$ranged', 'ore,$sword']),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_BUCKET_GIFT,
        100002232,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$sword,clippings']),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_DUKE_ITEM,
        100002235,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_GRASSING_CLIPPINGS,
        100002231,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$sword']),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_JADA_ITEM,
        100002234,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$sword,clippings,bucket,water']),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_LUCAS_ITEM,
        100002230,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_NPCS,
        100002236,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$sword,clippings,bucket,water']),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_WATER,
        100002233,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$sword,clippings,bucket']),
    GatorLocationData(
        GatorLocationName.MTN_BOWLING_BOMB_GIFT,
        100002270,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MTN_BRACELET_MONKEY_MOUNTAIN,
        100002294,
        GatorRegionName.BIG_ISLAND_BRACELET_SHOPS,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MTN_CHEST_B3,
        100000493,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.MTN_CHEST_C5,
        100001650,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.MTN_FLINT_NPC,
        100002271,
        GatorRegionName.BIG_ISLAND,
        None,
        ['$ranged', 'bomb']),
    GatorLocationData(
        GatorLocationName.MTN_LUISA_ITEM,
        100002278,
        GatorRegionName.MOUNTAIN,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MTN_LUISA_NPC,
        100002277,
        GatorRegionName.MOUNTAIN,
        None,
        []),
    GatorLocationData(
        GatorLocationName.MTN_NEIL_ITEM,
        100002275,
        GatorRegionName.MOUNTAIN,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.MTN_NEIL_NPC,
        100002274,
        GatorRegionName.MOUNTAIN,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_CENTER,
        100000694,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_E,
        100000199,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_NE,
        100000692,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_W,
        100000216,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_ROCK,
        100001694,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_SW,
        100001711,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_TANNER,
        100001708,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_CLIFFFACE,
        100001166,
        GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', 'glider']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_DOWN_FROM_TWIG,
        100001158,
        GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_RAISED,
        100001156,
        GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_SW,
        100000695,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_NE,
        100000242,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_NW_TALL,
        100001624,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_PEAK_E,
        100000079,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_SW,
        100000100,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_W,
        100000051,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_W,
        100000087,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_POT_C5,
        100001661,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', '$has_at_least_n_bracelet|2']),
    GatorLocationData(
        GatorLocationName.MTN_POT_D3,
        100001194,
        GatorRegionName.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', 'glider']),
    GatorLocationData(
        GatorLocationName.MTN_RACE_C4,
        100000303,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield,bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_RACE_D5,
        100001745,
        GatorRegionName.BIG_ISLAND_RACES,
        LocationGroup.Race,
        ['bracelet']),
    GatorLocationData(
        GatorLocationName.MTN_SCOOTER_NPC,
        100002276,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        None,
        ['bracelet,$cardboard_destroyer', '$ranged']),
    GatorLocationData(
        GatorLocationName.MTN_TANNER_NPC,
        100002272,
        GatorRegionName.MOUNTAIN_BREAKABLES,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.MTN_TWIG_NPC,
        100002273,
        GatorRegionName.MOUNTAIN,
        None,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.RAV_CHEST_E4,
        100000241,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.RAV_ESTHER_NPC,
        100002286,
        GatorRegionName.BIG_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.RAV_POT_E2,
        100001123,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.RAV_POT_E3_BEACH,
        100001126,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.RAV_POT_E3_RIVER,
        100001145,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.RAV_POT_E4,
        100002074,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.RAV_POT_F4,
        100002073,
        GatorRegionName.BIG_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.TI_AVERY,
        100002193,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['starter_hat,$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_AVERY_HAT_RECIPE,
        100002192,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.TI_BRACELET_MONKEY_TUTORIAL,
        100002291,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_CHEST_A3,
        100000184,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.TI_CHEST_B1_MID_CLIFF,
        100000372,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        []),
    GatorLocationData(
        GatorLocationName.TI_CHEST_B1_TALLEST,
        100000432,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        ['bracelet']),
    GatorLocationData(
        GatorLocationName.TI_CHEST_D1,
        100000183,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Chest,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.TI_FRANNY_ITEM,
        100002200,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_FRANNY_NPC,
        100002199,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_GERALD_ITEM,
        100002202,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_GERALD_NPC,
        100002201,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['$cardboard_destroyer']),
    GatorLocationData(
        GatorLocationName.TI_MARTIN,
        100002196,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        ['pot_q']),
    GatorLocationData(
        GatorLocationName.TI_POT_A1,
        100000561,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_A3_BELOW_E,
        100000422,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_A3_WITHIN_CLIFFS,
        100000425,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B0_BONE_PATH,
        100000179,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B0_SW,
        100000234,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_MIDDLE_ROPE,
        100000237,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_PEAK_N,
        100000406,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_PEAK_S,
        100000424,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_BELOW,
        100000225,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_NEXT_TO,
        100000167,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_PILLAR,
        100000168,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_W_ROPE,
        100000411,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_E,
        100000219,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_MIDDLE,
        100000228,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_W,
        100000189,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_NW,
        100000202,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_SIMON_E,
        100000175,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_TALL,
        100000426,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet']),
    GatorLocationData(
        GatorLocationName.TI_POT_C1_HILL,
        100000366,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_C1_STICK,
        100000365,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_C2,
        100000371,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        ['$ranged', 'bracelet', '$shield_jump']),
    GatorLocationData(
        GatorLocationName.TI_POT_D0,
        100000190,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_D1,
        100000232,
        GatorRegionName.TUTORIAL_ISLAND_BREAKABLES,
        LocationGroup.Pot,
        []),
    GatorLocationData(
        GatorLocationName.TI_POT_Q,
        100002195,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.TI_RACE_C2_CLIFF,
        100000391,
        GatorRegionName.TUTORIAL_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.TI_RACE_C2_MARTIN,
        100000382,
        GatorRegionName.TUTORIAL_ISLAND_RACES,
        LocationGroup.Race,
        ['$shield']),
    GatorLocationData(
        GatorLocationName.TI_SIMON_ITEM,
        100002198,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.TI_SIMON_NPC,
        100002197,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        []),
    GatorLocationData(
        GatorLocationName.TI_STICK,
        100002194,
        GatorRegionName.TUTORIAL_ISLAND,
        None,
        []),
]

location_table.sort(key = lambda entry: entry.name.name)

def locations_for_group(group: LocationGroup) -> List[str]:
    location_names = []
    for data in location_table:
        if data.location_group == group:
            location_names.append(data.name)
    return location_names

location_name_to_id: Dict[str, int] = {
    data.name: data.location_id for data in location_table
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_data in location_table:
    loc_group_name = loc_data.name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_data.name)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)

