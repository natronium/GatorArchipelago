from enum import Enum, auto
from typing import Dict, NamedTuple, Set, List

from .regions import (
    GatorRegionName as R,
    GatorStartingRegionName as StR,
    GatorSurfaceRegionName as SR,
    GatorITDRegionName as UR,
)


class LocationGroup(Enum):
    Pot = auto()
    Chest = auto()
    Race = auto()
    Wall = auto()
    Cryptid = auto()
    Main_Quest = auto()
    Side_Quest = auto()
    Shop = auto()
    MC_Pot = auto()
    WW_Pot = auto()
    LA_Pot = auto()
    OoT_Pot = auto()
    TP_Pot = auto()
    Surface = auto()
    Underground = auto()


class GatorLocationName(str, Enum):
    AVERY_Q_ANDROMEDA_ITEM = (
        "Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion Item"
    )
    AVERY_Q_ESME_NPC = "Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion NPC"
    AVERY_Q_NERF_BLASTER = "Avery!'s Main Quest - Nerf Blaster (Andromeda's Quest)"
    AVERY_Q_NPCS = "Avery!'s Main Quest - Avery!'s Main Quest Quest Completion NPCs"
    AVERY_Q_PLASTIC_FANGS = "Avery!'s Main Quest - Plastic Fangs (Esme's Quest)"
    AVERY_Q_SORBET = "Avery!'s Main Quest - Sorbet (Esme's Quest)"
    AVERY_Q_VELMA_ITEM = (
        "Avery!'s Main Quest - Velma (Western Cow) Quest Completion Item"
    )
    BCH_CADE_NPCS = "Southeast (Beach) - Cade (Floofy Bull) Quest Completion NPCs"
    BCH_CHEST_H9 = "Southeast (Beach) - Chest (H9) on north end of Skate Pug's island"
    BCH_JOE_NPC = "Southeast (Beach) - Joe (Pose Hawk) Quest Completion NPC"
    BCH_MR_DODDLER_ITEM = (
        "Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion Item"
    )
    BCH_MR_DODDLER_NPC = (
        "Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion NPC"
    )
    BCH_POT_H8 = "Southeast (Beach) - Pot (H8) on taller section northwest of Skate Pug"
    BCH_POT_I6 = "Southeast (Beach) - Pot (I6) on small island south of Marlow's deck"
    BCH_POT_I9_E = (
        "Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (east)"
    )
    BCH_POT_I9_W = (
        "Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (west)"
    )
    BCH_POT_J6 = (
        "Southeast (Beach) - Pot (J6) on small tall island east of Leeland's peninsula"
    )
    BCH_SAM_ITEM = "Southeast (Beach) - Sam (Pencil Jackal) Quest Completion Item"
    BCH_SAM_NPC = "Southeast (Beach) - Sam (Pencil Jackal) Quest Completion NPC"
    BCH_SKATE_PUG_ITEM = (
        "Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion Item"
    )
    BCH_SKATE_PUG_NPCS = (
        "Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion NPCs"
    )
    BCH_THROWN_PENCIL_1 = "Southeast (Beach) - Thrown Pencil 1 (Sam's Quest)"
    BCH_THROWN_PENCIL_2 = "Southeast (Beach) - Thrown Pencil 2 (Sam's Quest)"
    BCH_THROWN_PENCIL_3 = "Southeast (Beach) - Thrown Pencil 3 (Sam's Quest)"
    BCH_TONY_ITEM = (
        "Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion Item"
    )
    BCH_TONY_NPC = (
        "Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion NPC"
    )
    BCH_VIRAJ_NPC = "Southeast (Beach) - Viraj (Hot Shot Elephant) Quest Completion NPC"
    BI_BILLY_ITEM = "Big Island - Billy (Whale) Quest Completion Item"
    BI_BILLY_NPC = "Big Island - Billy (Whale) Quest Completion NPC"
    BI_BRACELET_MONKEY_ALL_BRACELETS_NPC = (
        "Big Island - ??? (Bracelet Monkey) All Bracelets NPC"
    )
    BI_ROCK = "Big Island - Rock (Zhu's Quest)"
    BI_ZHU_NPC = "Big Island - Zhu (Skipping Fox) Quest Completion NPC"
    CAN_BROKEN_SCOOTER_BOARD = (
        "Northeast (Canyon) - Broken Scooter Board Pickup (Kasen's Quest)"
    )
    CAN_CHEST_D8 = "Northeast (Canyon) - Chest (D8) on peak northwest of Jada's pump"
    CAN_DARCIE_ITEM = "Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion Item"
    CAN_DARCIE_NPC = "Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion NPC"
    CAN_KASEN_ITEM = (
        "Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion Item"
    )
    CAN_KASEN_NPC = "Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion NPC"
    CAN_MOCHI_NPC = "Northeast (Canyon) - Mochi (Heights Bear) Quest Completion NPC"
    CAN_POT_A8_N = "Northeast (Canyon) - Pot (A8) on north peak accessible from Billy"
    CAN_POT_A8_W = "Northeast (Canyon) - Pot (A8) on west peak accessible from Billy"
    CAN_POT_B8 = "Northeast (Canyon) - Pot (B8) on tall rock southwest from Billy's Canyon location"
    CAN_POT_C7 = "Northeast (Canyon) - Pot (C7) on cliffside west of and below Mochi"
    CAN_POT_C8_OUTCROP = (
        "Northeast (Canyon) - Pot (C8) at end of Kasen's stone outcropping"
    )
    CAN_POT_C8_MOCHI = (
        "Northeast (Canyon) - Pot (C8) on cliffside east of and below Mochi"
    )
    CAN_POT_C9_LOWER = "Northeast (Canyon) - Pot (C9) on Ssumantha's island (lower)"
    CAN_POT_C9_UPPER = "Northeast (Canyon) - Pot (C9) on Ssumantha's island (upper)"
    CAN_POT_D6 = "Northeast (Canyon) - Pot (D6) on island in middle of pond northeast of playground"
    CAN_POT_D7_N = (
        "Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (north)"
    )
    CAN_POT_D7_S = (
        "Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (south)"
    )
    CAN_POT_D8 = "Northeast (Canyon) - Pot (D8) on peak northwest of Jada's pump"
    CAN_RACE_B6 = "Northeast (Canyon) - Race (B6) starting east of waterfall on north side of Mountain"
    CAN_RACE_C7 = "Northeast (Canyon) - Race (C7) starting west of Kasen"
    CAN_SSUMANTHA_ITEM = (
        "Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion Item"
    )
    CAN_SSUMANTHA_NPC = (
        "Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion NPC"
    )
    CRL_BECCA_NPC = "East (Creeklands) - Becca (Retainer Shark) Quest Completion NPC"
    CRL_BRACELET_MONKEY_WINDMILL = (
        "East (Creeklands) - ??? (Bracelet Monkey) Windmill Bracelet"
    )
    CRL_CHEST_G6 = "East (Creeklands) - Chest (G6) north of Junk4Trash"
    CRL_CHEST_G8 = "East (Creeklands) - Chest (G8) on peak south of Splash Pad"
    CRL_CHEST_H5 = (
        "East (Creeklands) - Chest (H5) on peak north-northwest of Tony's chessboard"
    )
    CRL_MADELINE_NPC = (
        "East (Creeklands) - Madeline (Little Thing Mouse) Quest Completion NPC"
    )
    CRL_POT_D8 = (
        "East (Creeklands) - Pot (D8) northwest of Jada's pump below taller cliffs"
    )
    CRL_POT_E7_NE = (
        "East (Creeklands) - Pot (E7) northwest of Splash Pad below cliff to northeast"
    )
    CRL_POT_E7_NW = (
        "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (northwest)"
    )
    CRL_POT_E7_SE = (
        "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southeast)"
    )
    CRL_POT_E7_SW = (
        "East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southwest)"
    )
    CRL_POT_F7 = "East (Creeklands) - Pot (F7) south of Splash Pad"
    CRL_POT_F9 = "East (Creeklands) - Pot (F9) on peak north of Duke's pump"
    CRL_POT_G5 = "East (Creeklands) - Pot (G5) west of Junk4Trash in secluded area filled with ninjas and mimics"
    CRL_POT_H5_N = "East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (north)"
    CRL_POT_H5_S = "East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (south)"
    CRL_RETAINER = "East (Creeklands) - Retainer Pickup (Becca's Quest)"
    CRL_ROBIN_ITEM = (
        "East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion Item"
    )
    CRL_ROBIN_NPC = (
        "East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion NPC"
    )
    FOR_BRACELET_MONKEY_TREE = "West (Forest) - ??? (Bracelet Monkey) Tree Bracelet"
    FOR_CHEST_H4 = "West (Forest) - Chest (H4) on tallest peak north of Pepperoni's obstacle course"
    FOR_EVA_ITEM = "West (Forest) - Eva (Photographer Cat) Quest Completion Item"
    FOR_EVA_NPC = "West (Forest) - Eva (Photographer Cat) Quest Completion NPC"
    FOR_GUNTHER_NPC = "West (Forest) - Gunther (Sidekick Hippo) Quest Completion NPC"
    FOR_NINJA_CLAN_ITEM = "West (Forest) - Ninja Clan Quest Completion Item"
    FOR_NINJA_CLAN_NPCS = "West (Forest) - Ninja Clan Quest Completion NPCs"
    FOR_PENELOPE_ITEM = (
        "West (Forest) - Penelope (Bastion Beaver) Quest Completion Item"
    )
    FOR_PENELOPE_NPC = "West (Forest) - Penelope (Bastion Beaver) Quest Completion NPC"
    FOR_PEPPERONI_ITEM = (
        "West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion Item"
    )
    FOR_PEPPERONI_NPCS = (
        "West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion NPCs"
    )
    FOR_POT_E1_LOWER_E = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and down the cliff)"
    FOR_POT_E1_UPPER_E = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and up the cliff)"
    FOR_POT_E1_UPPER_W = "West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (west and up the cliff)"
    FOR_POT_F3 = "West (Forest) - Pot (F3) on north cliff edge of pond with dead trees"
    FOR_POT_G3_CLIFF = "West (Forest) - Pot (G3) on cliff overlooking pond with dead trees from the west side"
    FOR_POT_G3_POND = "West (Forest) - Pot (G3) on west edge of pond with dead trees"
    FOR_POT_G4_DEAD_POND = (
        "West (Forest) - Pot (G4) on south edge of pond with dead trees"
    )
    FOR_POT_G4_E_E = (
        "West (Forest) - Pot (G4) on tall peak east of pond with dead trees (east)"
    )
    FOR_POT_G4_E_W = (
        "West (Forest) - Pot (G4) on tall peak east of pond with dead trees (west)"
    )
    FOR_POT_G4_S = (
        "West (Forest) - Pot (G4) south of tall peak east of pond with dead trees"
    )
    FOR_POT_H2 = "West (Forest) - Pot (H2) above Trish (Invisible Horse)"
    FOR_POT_H4_E = "West (Forest) - Pot (H4) east of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_H4_N = "West (Forest) - Pot (H4) north of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_H4_S = "West (Forest) - Pot (H4) south of tallest peak north of Pepperoni's obstacle course"
    FOR_POT_J0 = (
        "West (Forest) - Pot (J0) in tidepool in southwest corner of island (northwest)"
    )
    FOR_POT_J1_SE = (
        "West (Forest) - Pot (J1) in tidepool in southwest corner of island (southeast)"
    )
    FOR_POT_J1_SW = (
        "West (Forest) - Pot (J1) in tidepool in southwest corner of island (southwest)"
    )
    FOR_POT_J3_E = "West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (east)"
    FOR_POT_J3_W = "West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (west)"
    FOR_POT_KID_NPC = "West (Forest) - Pot Kid (Eepy Armadillo) Quest Completion NPC"
    FOR_RACE_F4 = (
        "West (Forest) - Race (F4) starting from west path exit from playground"
    )
    FOR_RACE_G0 = (
        "West (Forest) - Race (G0) starting from island west of Billy's Forest location"
    )
    FOR_RACE_H1 = "West (Forest) - Race (H1) starting from southwest of The Tree"
    FOR_ROMEO_NUNCHUCKS = "West (Forest) - Romeo (Ninja Anteater) Nunchucks"
    FOR_SIERRA_ITEM = "West (Forest) - Sierra (Origami Crane) Quest Completion Item"
    FOR_SIERRA_NPC = "West (Forest) - Sierra (Origami Crane) Quest Completion NPC"
    FOR_SORIN_ROE_BEERITNEY_ITEM = (
        "West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion Item"
    )
    FOR_SORIN_ROE_BEERITNEY_NPCS = (
        "West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion NPCs"
    )
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
    JILL_Q_GENE_ITEM = (
        "Jill's Main Quest - Gene (Merchant Beaver) Quest Completion Item"
    )
    JILL_Q_MAGIC_ORE = "Jill's Main Quest - Magic Ore Pickup (Susanne's Quest)"
    JILL_Q_NPCS = "Jill's Main Quest - Jill's Main Quest Completion NPCs"
    JILL_Q_SUSANNE = (
        "Jill's Main Quest - Susanne (Paleolithic Gazelle) Quest Completion"
    )
    MARTIN_Q_BUCKET_GIFT = "Martin's Main Quest - Bucket Gift (Jada's Quest)"
    MARTIN_Q_DUKE_ITEM = "Martin's Main Quest - Duke (Cool Goose) Quest Completion Item"
    MARTIN_Q_GRASSING_CLIPPINGS = (
        "Martin's Main Quest - Grassing Clippings Collect (Jada's Quest)"
    )
    MARTIN_Q_JADA_ITEM = "Martin's Main Quest - Jada (Cool Boar) Quest Completion Item"
    MARTIN_Q_LUCAS_ITEM = (
        "Martin's Main Quest - Lucas (Cool Wolf) Quest Completion Item"
    )
    MARTIN_Q_NPCS = "Martin's Main Quest - Martin's Main Quest Completion NPCs"
    MARTIN_Q_WATER = "Martin's Main Quest - Water Collect (Jada's Quest)"
    MTN_BOWLING_BOMB_GIFT = "North (Mountain) - Bowling Bomb Gift (Flint's Quest)"
    MTN_BRACELET_MONKEY_MOUNTAIN = (
        "North (Mountain) - ??? (Bracelet Monkey) Mountain Bracelet"
    )
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
    MTN_POT_B5_TANNER = (
        "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (next to Tanner)"
    )
    MTN_POT_B5_SW = "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (southwest of Tanner)"
    MTN_POT_B5_ROCK = "North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (up on rock formation)"
    MTN_POT_C3_CLIFFFACE = "North (Mountain) - Pot (C3) on cliff area across from Martin's deck (next to cliffface)"
    MTN_POT_C3_RAISED = "North (Mountain) - Pot (C3) on cliff area across from Martin's deck (on raised section)"
    MTN_POT_C3_DOWN_FROM_TWIG = (
        "North (Mountain) - Pot (C3) on cliff outcropping northwest and down from Twig"
    )
    MTN_POT_C3_SW = "North (Mountain) - Pot (C3) on raised area in northwest corner of Mountain (southwest)"
    MTN_POT_C4_NW_TALL = (
        "North (Mountain) - Pot (C4) on northwest tall peak, north of race"
    )
    MTN_POT_C4_NE = (
        "North (Mountain) - Pot (C4) part of Scooter's allergy quest (northeast)"
    )
    MTN_POT_C4_PEAK_E = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, east)"
    MTN_POT_C4_PEAK_W = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, west)"
    MTN_POT_C4_SW = (
        "North (Mountain) - Pot (C4) part of Scooter's allergy quest (southwest)"
    )
    MTN_POT_C4_W = "North (Mountain) - Pot (C4) part of Scooter's allergy quest (west)"
    MTN_POT_C5 = "North (Mountain) - Pot (C5) west and up from stage"
    MTN_POT_D3 = (
        "North (Mountain) - Pot (D3) on cliff outcropping west and down from Twig"
    )
    MTN_RACE_C4 = (
        "North (Mountain) - Race (C4) starting on western peak of the Mountain"
    )
    MTN_RACE_D5 = "North (Mountain) - Race (D5) starting north of the playground and heading up the Mountain"
    MTN_SCOOTER_NPC = (
        "North (Mountain) - Scooter (Ceramic-Allergy Cougar) Quest Completion NPC"
    )
    MTN_TANNER_NPC = "North (Mountain) - Tanner (Pot Mimic Elk) Quest Completion NPC"
    MTN_TWIG_NPC = "North (Mountain) - Twig (Flip Pomeranian) Quest Completion NPC"
    RAV_CHEST_E4 = "Central (Ravine) - Chest (E4) under overhang near river"
    RAV_ESTHER_NPC = "Central (Ravine) - Esther (Directions Deer) Quest Completion NPC"
    RAV_POT_E2 = (
        "Central (Ravine) - Pot (E2) on hill on path east from Penelope's waterfall"
    )
    RAV_POT_E3_BEACH = "Central (Ravine) - Pot (E3) south of beach where Esther roams"
    RAV_POT_E3_RIVER = "Central (Ravine) - Pot (E3) south of central river east of path south from Esther"
    RAV_POT_E4 = "Central (Ravine) - Pot (E4) on northern tall peak west of playground"
    RAV_POT_F4 = "Central (Ravine) - Pot (F4) on southern tall peak west of playground"
    TI_AVERY = "Tutorial Island - Avery! Quest Completion"
    TI_AVERY_HAT_RECIPE = "Tutorial Island - Avery! Hat Recipe"
    TI_BRACELET_MONKEY_TUTORIAL = (
        "Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet"
    )
    TI_CHEST_A3 = "Tutorial Island - Chest (A3) below Gerald to east"
    TI_CHEST_B1_MID_CLIFF = "Tutorial Island - Chest (B1) on mid-cliff outcropping visible from bone path on the west of Tutorial Island"
    TI_CHEST_B1_TALLEST = (
        "Tutorial Island - Chest (B1) on tallest peak of Tutorial Island"
    )
    TI_CHEST_D1 = (
        "Tutorial Island - Chest (D1) on small island south of Jill's picnic table"
    )
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
    TI_POT_B1_PEAK_N = (
        "Tutorial Island - Pot (B1) on peak north of tallest peak on Tutorial Island"
    )
    TI_POT_B1_PEAK_S = "Tutorial Island - Pot (B1) on peak south of the three ropes in northwest of Tutorial Island"
    TI_POT_B1_WATERFALL_PILLAR = "Tutorial Island - Pot (B1) on pillar by waterfalls"
    TI_POT_B1_W_ROPE = (
        "Tutorial Island - Pot (B1) west of rope to tallest peaks on Tutorial Island"
    )
    TI_POT_B2_BELOW_E = "Tutorial Island - Pot (B2) below Gerald to the south near water level (eastmost)"
    TI_POT_B2_BELOW_MIDDLE = (
        "Tutorial Island - Pot (B2) below Gerald to the south near water level (middle)"
    )
    TI_POT_B2_BELOW_W = "Tutorial Island - Pot (B2) below Gerald to the south near water level (westmost)"
    TI_POT_B2_SIMON_E = (
        "Tutorial Island - Pot (B2) on green cliff east of Simon's starting location"
    )
    TI_POT_B2_NW = (
        "Tutorial Island - Pot (B2) on green cliff northwest of Martin's lawn chairs"
    )
    TI_POT_B2_TALL = "Tutorial Island - Pot (B2) on tall peak west of Gerald"
    TI_POT_C1_HILL = (
        "Tutorial Island - Pot (C1) on hill overlooking Jill's picnic table"
    )
    TI_POT_C1_STICK = "Tutorial Island - Pot (C1) on rock near Stick pickup location"
    TI_POT_C2 = (
        "Tutorial Island - Pot (C2) on cliff overlooking rope crossing the waterfall"
    )
    TI_POT_D0 = (
        "Tutorial Island - Pot (D0) on small peninsula southwest of Jill's picnic table"
    )
    TI_POT_D1 = "Tutorial Island - Pot (D1) on small island with chest south of Jill's picnic table"
    TI_RACE_C2_CLIFF = "Tutorial Island - Race (C2) starting near grassy cliff"
    TI_RACE_C2_MARTIN = "Tutorial Island - Race (C2) starting near Martin's lawn chairs"
    TI_SIMON_ITEM = "Tutorial Island - Simon (Ragdoll Bear) Quest Completion Item"
    TI_SIMON_NPC = "Tutorial Island - Simon (Ragdoll Bear) Quest Completion NPC"
    TI_STICK = "Tutorial Island - Stick Pickup"

    # Underground
    PICKAXE_PICKUP = "Underground Entrance - Pickaxe Pickup"
    JAR_1168_H7 = (
        "Flowstone Caverns - Jar (H7) in the middle of Amberly's racetrack (small)"
    )
    JAR_801_C5 = "Mines - Jar (C5) tipped over in pool (south)"
    JAR_1161_H7 = (
        "Flowstone Caverns - Jar (H7) in the middle of Amberly's racetrack (large)"
    )
    JAR_1171_I8 = "Flowstone Caverns - Jar (I8) in cliffside nook (leftmost)"
    JAR_908_G5 = "Lighthouse - Jar (G5) on Roots and Caverns border (upper)"
    JAR_907_G5 = "Lighthouse - Jar (G5) on Roots and Caverns border (lower, large)"
    JAR_894_G5 = "Lighthouse - Jar (G5) on Roots and Caverns border (lower, small)"
    JAR_1148_H6 = "Flowstone Caverns - Jar (H6) along cliffs by water pipe (lower)"
    JAR_602_G5 = (
        "Big Roots - Jar (G5) near ceiling in cluster of jars (shortest east of chest)"
    )
    JAR_598_G5 = "Big Roots - Jar (G5) near ceiling in cluster of jars (west of chest)"
    JAR_597_G5 = (
        "Big Roots - Jar (G5) near ceiling in cluster of jars (widest east of chest)"
    )
    JAR_595_G5 = (
        "Big Roots - Jar (G5) near ceiling in cluster of jars (tallest east of chest)"
    )
    JAR_580_G8 = "Flowstone Caverns - Jar (G8) east of tallest pillar in Caverns"
    JAR_873_F4 = "Lighthouse - Jar (F4) on cliff southwest of gathering space (lower)"
    JAR_874_F4 = "Lighthouse - Jar (F4) on cliff southwest of gathering space (upper)"
    JAR_906_F4 = "Lighthouse - Jar (F4) on cliff Roots side of gathering space"
    JAR_1166_H6 = "Flowstone Caverns - Jar (H6) on cliff south of Nodd (Cryptid Hunter Axolotl)'s Flowstone Caverns site (lower)"
    JAR_1167_H6 = (
        "Flowstone Caverns - Jar (H6) along cliffs by water pipe (upper, small)"
    )
    JAR_1153_H6 = (
        "Flowstone Caverns - Jar (H6) along cliffs by water pipe (upper, large)"
    )
    JAR_1180_E5 = "Mines - Jar (E5) under boardwalks in southern path between Mines and Flowstone Caverns (large)"
    JAR_1213_E5 = "Mines - Jar (E5) under boardwalks in southern path between Mines and Flowstone Caverns (small)"
    JAR_931_G3 = "Big Roots - Jar (G3) on rock intersecting with branches between Nodd and Arlotte (small)"
    JAR_576_H6 = "Flowstone Caverns - Jar (H6) on cliff south of Nodd (Cryptid Hunter Axolotl)'s Flowstone Caverns site (upper)"
    JAR_579_I8 = "Flowstone Caverns - Jar (I8) in cliffside nook (rigthmost)"
    JAR_1170_I7 = "Flowstone Caverns - Jar (I7) fallen from cliffside nook"
    JAR_578_H8 = "Flowstone Caverns - Jar (H8) east of tallest pillar in Caverns"
    JAR_890_G4 = "Big Roots - Jar (G4) above wood slat path from Lighthouse to Roots"
    JAR_1334_E3 = "Underground Entrance - Jar (E3) on top of cliff between Esther (Directions Deer) and the entrance to the underground"
    JAR_577_I8 = "Flowstone Caverns - Jar (I8) in cliffside nook (middle)"
    JAR_875_F3 = "Big Roots - Jar (F3) on cliff edge northwest of Arlotte (thin)"
    JAR_876_F3 = "Big Roots - Jar (F3) on cliff edge northwest of Arlotte (wide)"
    JAR_945_G3 = "Big Roots - Jar (G3) on rock intersecting with branches between Nodd and Arlotte (large)"
    JAR_910_F2 = "Big Roots - Jar (F2) on cliff between two waterfalls (upper)"
    JAR_760_B4 = "Mines - Jar (B4) west of Emilio's stage"
    JAR_792_C5 = "Mines - Jar (C5) tipped over in pool (north)"
    JAR_840_F2 = "Big Roots - Jar (F2) on cliff between two waterfalls (lower)"
    JAR_981_H2 = "Big Roots - Jar (H2) up on rock at intersection of branches south-southeast from Dave Matthew Band (Marching Ants)"
    CHEST_909_G2 = "Big Roots - Chest (G2) in high crook of tree branch near ceiling overlooking Nodd (Cryptid Hunter Axolotl)"
    CHEST_594_G5 = "Big Roots - Chest (G5) near ceiling in cluster of jars"
    CHEST_604_A5 = "Mines - Chest (A5) among wires intersecting with ground, dramatically lit in red"
    CHEST_968_H3 = "Big Roots - Chest (H3) near ceiling on roots above path of pools to Val (Scaredy Clam)'s starting location"
    CHEST_610_B4 = "Mines - Chest (B4) behind fan in northwest corner of Mines"
    CHEST_601_G7 = "Flowstone Caverns - Chest (G7) hidden in a middle layer of tallest pillar in Caverns, guarded by Shielded Green Crystal Monster"
    RACE_417_B5 = "Mines - Race (B5) at bottom of rail up to Emilio's stage"
    RACE_499_H8 = "Flowstone Caverns - Race (H7) southwest of Pater (Cursed Crayfish)"
    RACE_418_G2 = "Big Roots - Race (G1) west of light beams coming from ceiling"
    RACE_491_G7 = "Flowstone Caverns - Race (G7) behind Amberly's barricade"
    RACE_484_D6 = "Flowstone Caverns - Race (D6) west of Lola (Queen Marten)"
    RACE_413_H2 = "Big Roots - Race (H2) in southwest corner of Roots"
    RACE_468_B4 = "Mines - Race (B4) starting at top of rails in north of Mines"
    RACE_503_F8 = "Flowstone Caverns - Race (F8) east-northeast of tallest pillar and pointed toward metal boardwalk"
    WALL_121_H1 = "Big Roots - Rock bridge (H1) in south section of river marched around by Dave and Matthew (Marching Band Ants)"
    WALL_132_B6 = "Flowstone Caverns - Rock wall (B6) west of Heather (Hiding Bluebird)"
    WALL_119_E6 = "Flowstone Caverns - Rock wall (E6) south of Jane (Ant Queen)"
    WALL_126_D4 = "Mines - Rock wall (D4) above waterfall south of Emilio's stage"
    WALL_130_B6 = "Mines - Rock wall (B6) east of fan at center north of Mines"
    WALL_146_B5 = "Mines - Rock wall (B5) nearest Dru (Miner Turtle) (Dru's Quest)"
    WALL_175_F8 = "Flowstone Caverns - Rock wall (F8) south of Bodie (High Concept Octopus) tucked in corner"
    WALL_148_B5 = "Mines - Rock wall (B5) blocking top segment of rails in north of Mines  (Dru's Quest)"
    WALL_117_F6 = "Flowstone Caverns - Rock wall (F6) northeast of Jessie"
    WALL_177_G8 = (
        "Flowstone Caverns - Rock wall (G8) overlooking tallest pillar from the east"
    )
    WALL_181_H6 = "Flowstone Caverns - Rock wall (H6) west of Casey (exposed)"
    WALL_135_G1 = (
        "Big Roots - Rock wall (G1) southwest of light beams coming through ceiling"
    )
    WALL_180_I6 = "Flowstone Caverns - Rock wall (I6) west of Casey (hidden)"
    WALL_209_C7 = (
        "Flowstone Caverns - Rock wall (C7) southeast of Heather (Hiding Bluebird)"
    )
    WALL_129_C6 = (
        "Flowstone Caverns - Rock wall (C6) southwest of Heather (Hiding Bluebird)"
    )
    WALL_138_F1 = (
        "Big Roots - Rock wall (F1) west of light beams coming through ceiling"
    )
    WALL_127_E4 = "Lighthouse - Rock wall (E4) overlooking central area"
    WALL_208_C7 = (
        "Flowstone Caverns - Rock wall (C7) east-southeast from Lola (Queen Marten)"
    )
    WALL_149_B5 = "Mines - Rock wall (B5) following rail line up from Dru (Miner Turtle) (Dru's Quest)"
    WALL_201_I2 = (
        "Big Roots - Rock wall (I2) top of waterfall in southern area of Roots"
    )
    WALL_137_F2 = (
        "Big Roots - Rock wall (F2) north of light beams coming through ceiling"
    )
    WALL_131_B6 = "Mines - Rock wall (B6) east of Dru's delivery route"
    WALL_128_E5 = (
        "Flowstone Caverns - Rock Wall (E5) overlooking boardwalk from Lighthouse"
    )
    WALL_134_E7 = "Flowstone Caverns - Rock Wall (E7) southeast of Jane (Ant Queen)"
    WALL_207_I1 = "Big Roots - Rock wall (I1) tucked in southwest corner of Roots"
    WALL_120_H2 = "Big Roots - Rock bridge (H2) in east section of river marched around by Dave and Matthew (Marching Band Ants)"
    WALL_147_B5 = "Mines - Rock wall (B5) blocking segment pre-ramp of rails in north of Mines (Dru's Quest)"
    WALL_179_H5 = "Big Roots - Rock wall (H5) at far end of Val (Scaredy Clam)'s path"
    WALL_133_E7 = (
        "Flowstone Caverns - Rock wall (E7) west of Bodie (High Concept Octopus)"
    )
    WALL_123_G1 = "Big Roots - Rock bridge (G1) in north section of river marched around by Dave and Matthew (Marching Band Ants)"
    WALL_118_F7 = "Flowstone Caverns - Rock wall (F7) overlooking metal boardwalk between sections of the Caverns"
    WALL_122_H2 = "Big Roots - Rock bridge (H1) in middle section of river marched around by Dave and Matthew (Marching Band Ants)"
    WALL_176_H6 = "Flowstone Caverns - Rock wall (H6) above waterfall with water pipe"
    CRYPTID_HOLY_B5 = (
        "Mines - Bird of Big Island (Cryptid) on fan at center north edge of Mines"
    )
    CRYPTID_LOOKY_C5 = (
        "Mines - Peep Goblin (Cryptid) above and south of Madson (Breaking Badger)"
    )
    CRYPTID_FLOOFY_F4 = (
        "Big Roots - Barber Worm (Cryptid) on branches near Arlotte (Tangled Spider)"
    )
    CRYPTID_DRIPPY_G5 = "Flowstone Caverns - Wellerdropple (Cryptid) on platform near ceiling with stalactites above Jessie (Fighting Xolo)"
    CRYPTID_TREEY_E2 = (
        "Big Roots - Yarrowling (Cryptid) on cliff above waterfall next to Cass Iron"
    )
    CRYPTID_FINNY_G8 = (
        "Flowstone Caverns - Gulfcoaster (Cryptid) east of tallest pillar in Caverns"
    )
    CRYPTID_BUBBLY_G7 = (
        "Flowstone Caverns - Orbhound (Cryptid) on tallest pillar in Caverns"
    )
    CRYPTID_CAKEY_B4 = (
        "Mines - Iced Liar (Cryptid) overlooking fan in northwest corner of Mines"
    )
    CRYPTID_THORNY_G2 = "Big Roots - Bramble Stalker (Cryptid) on tree branch above Dave and Matthew (Marching Band Ants)"
    NPC_VAL_NPC = "Big Roots - Val (Scaredy Clam) Quest Completion NPC"
    NPC_VAL_ITEM = "Big Roots - Val (Scaredy Clam) Quest Completion Item"
    CLAM_ITEM = "Big Roots - Clam Item (Val, Scaredy Clam)"
    NPC_NODD_NPC = "Underground - Nodd (Cryptid Hunter Axolotl) Quest Completion NPC"
    NPC_NODD_ITEM = "Underground - Nodd (Cryptid Hunter Axolotl) Quest Completion Item"
    NPC_NODD_1_CRYPTID = "Underground - Turn in 1 Cryptid to Nodd"
    NPC_NODD_3_CRYPTID = "Underground - Turn in 3 Cryptids to Nodd"
    NPC_NODD_5_CRYPTID = "Underground - Turn in 5 Cryptids to Nodd"
    NPC_NODD_7_CRYPTID = "Underground - Turn in 7 Cryptids to Nodd"
    NPC_MADSON_C5 = "Mines - Madson (Breaking Badger) Quest Completion NPC"
    NPC_MADSON_HAT = "Mines - Madson (Breaking Badger) Quest Completion Item 1"
    NPC_MADSON_HOVER = "Mines - Madson (Breaking Badger) Quest Completion Item 2"
    NPC_DAVE_NPC = "Big Roots - Dave (Marching Band Ant) Quest Completion NPC"
    NPC_MATTHEW_NPC = "Big Roots - Matthew (Marching Band Ant) Quest Completion NPC"
    NPC_DAVE_MATTHEW_ITEM = (
        "Big Roots - Dave Matthew Band (Marching Ants) Quest Completion Item"
    )
    NPC_JESSIE_NPC = "Flowstone Caverns - Jessie (Fighting Xolo) Quest Completion NPC"
    NPC_JESSIE_ITEM = "Flowstone Caverns - Jessie (Fighting Xolo) Quest Completion Item"
    NPC_TURTLE_NPC = "Mines - Dru (Miner Turtle) Quest Completion NPC"
    NPC_TURTLE_ITEM_1 = "Mines - Dru (Miner Turtle) Quest Completion Item 1"
    NPC_TURTLE_ITEM_2 = "Mines - Dru (Miner Turtle) Quest Completion Item 2"
    NPC_ARLOTTE_NPC = "Big Roots - Arlotte (Tangled Spider) Quest Completion NPC"
    NPC_ARLOTTE_ITEM_1 = "Big Roots - Arlotte (Tangled Spider) Quest Completion Item 1"
    NPC_ARLOTTE_ITEM_2 = "Big Roots - Arlotte (Tangled Spider) Quest Completion Item 2"
    NPC_JANE_D6 = "Flowstone Caverns - Jane (Queen Ant) Quest Completion NPC"
    NPC_LOLA_C7 = "Flowstone Caverns - Lola (Queen Marten) Quest Completion NPC"
    NPC_JANE_LOLA_LETTER_1 = "Flowstone Caverns - Receive Queen's Secret Letter (Queen Beef between Jane and Lola)"
    NPC_JANE_LOLA_LETTER_2 = "Flowstone Caverns - Receive Other Queen's Secret Letter (Queen Beef between Jane and Lola)"
    NPC_JANE_LOLA_ITEM = "Flowstone Caverns - Queen Beef Quest Completion Item"
    NPC_HARREN_D3 = "Mines - Harren (Behind You Beetle) and Hai (Hiding Hedgehog) Quest Completion NPCs"
    NPC_BODIE_NPC = (
        "Flowstone Caverns - Bodie (High Concept Octopus) Quest Completion NPC"
    )
    NPC_BODIE_ITEM = (
        "Flowstone Caverns - Bodie (High Concept Octopus) Quest Completion Item"
    )
    NPC_HEATHER_NPC = (
        "Flowstone Caverns - Heather (Hiding Bluebird) Quest Completion NPC"
    )
    NPC_HEATHER_ITEM = (
        "Flowstone Caverns - Heather (Hiding Bluebird) Quest Completion Item"
    )
    NPC_CRAYFISH_NPC = (
        "Flowstone Caverns - Pater (Cursed Crayfish) Quest Completion NPC"
    )
    NPC_CRAYFISH_ITEM = "Flowstone Caverns - Rubber Ball Gift (Pater, Cursed Crayfish)"
    NPC_GHOST_NPC = "Mines - o.o (Ghost) Quest Completion NPC"
    NPC_GHOST_ITEM = "Mines - o.o (Ghost) Quest Completion Item"
    NPC_CASEY_H6 = "Flowstone Caverns - Casey (Flying Squirrel) Quest Completion NPC"
    DRONE_GIFT = "Flowstone Caverns - Drone Gift (Casey, Flying Squirrel)"
    NPC_CASSIRON_NPC = (
        "Big Roots - Cass Iron (Scared-of-Disappointment Snail) Quest Completion NPC"
    )
    NPC_CASSIRON_ITEM = (
        "Big Roots - Cass Iron (Scared-of-Disappointment Snail) Quest Completion Item"
    )

    NPC_ESTHER_E3 = (
        "Underground Entrance - Esther (Directions Deer) Quest Completion NPC"
    )
    NPC_EMILIO_NPC = "Mines - Emilio Main Quest Completion NPC"
    NPC_EMILIO_ITEM = "Mines - Emilio Main Quest Completion Item"
    NPC_RUTH_NPC = "Big Roots - Ruth Main Quest Completion NPC"
    NPC_RUTH_ITEM = "Big Roots - Ruth Main Quest Completion Item"
    NPC_AMBERLY_NPC = "Flowstone Caverns - Amberly Main Quest Completion NPC"
    NPC_AMBERLY_ITEM = "Flowstone Caverns - Amberly Main Quest Completion Item"


class GatorEventLocationName(str, Enum):
    PLAYGROUND = "Complete the Playground"
    DARKLORD = "Confront Darklord"


class GatorLocationData(NamedTuple):
    name: GatorLocationName
    location_id: int
    region: R
    location_groups: List[LocationGroup]


surface_location_table: List[GatorLocationData] = [
    GatorLocationData(
        GatorLocationName.AVERY_Q_ANDROMEDA_ITEM,
        100002280,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_ESME_NPC,
        100002284,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_NERF_BLASTER,
        100002279,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_NPCS,
        100002285,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_PLASTIC_FANGS,
        100002283,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_SORBET,
        100002282,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.AVERY_Q_VELMA_ITEM,
        100002281,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_CADE_NPCS,
        100002221,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_CHEST_H9,
        100000201,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_JOE_NPC,
        100002224,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_MR_DODDLER_ITEM,
        100002220,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_MR_DODDLER_NPC,
        100002219,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_POT_H8,
        100000082,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.BCH_POT_I6,
        100000115,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.BCH_POT_I9_E,
        100000077,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.BCH_POT_I9_W,
        100000069,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.BCH_POT_J6,
        100000101,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.BCH_SAM_ITEM,
        100002217,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_SAM_NPC,
        100002216,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_SKATE_PUG_ITEM,
        100002223,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_SKATE_PUG_NPCS,
        100002222,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_1,
        100002213,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_2,
        100002214,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_THROWN_PENCIL_3,
        100002215,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_TONY_ITEM,
        100002212,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_TONY_NPC,
        100002211,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BCH_VIRAJ_NPC,
        100002218,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BI_BILLY_ITEM,
        100002288,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BI_BILLY_NPC,
        100002287,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BI_BRACELET_MONKEY_ALL_BRACELETS_NPC,
        100002295,
        SR.BIG_ISLAND_BRACELET_SHOPS,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BI_ROCK,
        100002289,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.BI_ZHU_NPC,
        100002290,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_BROKEN_SCOOTER_BOARD,
        100002205,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_CHEST_D8,
        100001360,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_DARCIE_ITEM,
        100002204,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_DARCIE_NPC,
        100002203,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_KASEN_ITEM,
        100002207,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_KASEN_NPC,
        100002206,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_MOCHI_NPC,
        100002210,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_A8_N,
        100001463,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_A8_W,
        100001456,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_B8,
        100002070,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_C7,
        100001350,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_C8_MOCHI,
        100001351,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_C8_OUTCROP,
        100001349,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_C9_LOWER,
        100002071,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_C9_UPPER,
        100002072,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_D6,
        100000006,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_D7_N,
        100001362,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_D7_S,
        100001363,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_POT_D8,
        100001361,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CAN_RACE_B6,
        100000813,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.CAN_RACE_C7,
        100000753,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.CAN_SSUMANTHA_ITEM,
        100002209,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CAN_SSUMANTHA_NPC,
        100002208,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_BECCA_NPC,
        100002229,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_BRACELET_MONKEY_WINDMILL,
        100002292,
        SR.BIG_ISLAND_BRACELET_SHOPS,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_G6,
        100002026,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_G8,
        100000153,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_CHEST_H5,
        100000766,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_MADELINE_NPC,
        100002225,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_D8,
        100000491,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_NE,
        100000062,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_NW,
        100001431,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_SE,
        100001444,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_E7_SW,
        100000655,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_F7,
        100000117,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_F9,
        100000651,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_G5,
        100002012,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_H5_N,
        100000722,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_POT_H5_S,
        100000721,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.CRL_RETAINER,
        100002228,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_ROBIN_ITEM,
        100002227,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CRL_ROBIN_NPC,
        100002226,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_BRACELET_MONKEY_TREE,
        100002293,
        SR.BIG_ISLAND_BRACELET_SHOPS,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_CHEST_H4,
        100001518,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_EVA_ITEM,
        100002259,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_EVA_NPC,
        100002258,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_GUNTHER_NPC,
        100002260,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_NINJA_CLAN_ITEM,
        100002250,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_NINJA_CLAN_NPCS,
        100002249,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_PENELOPE_ITEM,
        100002257,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_PENELOPE_NPC,
        100002256,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_PEPPERONI_ITEM,
        100002252,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_PEPPERONI_NPCS,
        100002251,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_LOWER_E,
        100001381,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_UPPER_E,
        100001382,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_E1_UPPER_W,
        100001380,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_F3,
        100000025,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G3_CLIFF,
        100001450,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G3_POND,
        100000545,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_DEAD_POND,
        100000546,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_E_E,
        100001540,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_E_W,
        100001541,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_G4_S,
        100001542,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_H2,
        100000094,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_E,
        100001520,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_N,
        100001532,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_H4_S,
        100001517,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_J0,
        100001593,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_J1_SE,
        100001596,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_J1_SW,
        100001594,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_J3_E,
        100001584,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_J3_W,
        100001583,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.FOR_POT_KID_NPC,
        100002255,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_RACE_F4,
        100001409,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.FOR_RACE_G0,
        100000072,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.FOR_RACE_H1,
        100001399,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.FOR_ROMEO_NUNCHUCKS,
        100002248,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_SIERRA_ITEM,
        100002247,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_SIERRA_NPC,
        100002246,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_SORIN_ROE_BEERITNEY_ITEM,
        100002254,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_SORIN_ROE_BEERITNEY_NPCS,
        100002253,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_TIFFANY_ITEM,
        100002263,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_TIFFANY_NPCS,
        100002262,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.FOR_TRISH_NPC,
        100002261,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.J4T_GRABBY_HAND,
        100002242,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_PAINT_GUN,
        100002241,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_ROY_ALL_PURCHASES_NPC,
        100002243,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_STICKY_HAND,
        100002237,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_TRAMPOLINE,
        100002238,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_TRASH_CAN_LID,
        100002239,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.J4T_WRENCH,
        100002240,
        SR.JUNK_4_TRASH,
        [LocationGroup.Surface, LocationGroup.Shop],
    ),
    GatorLocationData(
        GatorLocationName.JET_LEELAND_ITEM,
        100002245,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JET_LEELAND_NPC,
        100002244,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_BUG_NET_GIFT,
        100002268,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_CHEESE_SANDWICH,
        100002266,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_GENE_ITEM,
        100002267,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_MAGIC_ORE,
        100002264,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_NPCS,
        100002269,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.JILL_Q_SUSANNE,
        100002265,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_BUCKET_GIFT,
        100002232,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_DUKE_ITEM,
        100002235,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_GRASSING_CLIPPINGS,
        100002231,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_JADA_ITEM,
        100002234,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_LUCAS_ITEM,
        100002230,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_NPCS,
        100002236,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MARTIN_Q_WATER,
        100002233,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_BOWLING_BOMB_GIFT,
        100002270,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_BRACELET_MONKEY_MOUNTAIN,
        100002294,
        SR.BIG_ISLAND_BRACELET_SHOPS,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_CHEST_B3,
        100000493,
        SR.MOUNTAIN_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_CHEST_C5,
        100001650,
        SR.MOUNTAIN_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_FLINT_NPC,
        100002271,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_LUISA_ITEM,
        100002278,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_LUISA_NPC,
        100002277,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_NEIL_ITEM,
        100002275,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_NEIL_NPC,
        100002274,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_CENTER,
        100000694,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_E,
        100000199,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_NE,
        100000692,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B4_W,
        100000216,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_ROCK,
        100001694,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_SW,
        100001711,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_B5_TANNER,
        100001708,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_CLIFFFACE,
        100001166,
        SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_DOWN_FROM_TWIG,
        100001158,
        SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_RAISED,
        100001156,
        SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C3_SW,
        100000695,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_NE,
        100000242,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_NW_TALL,
        100001624,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_PEAK_E,
        100000079,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_SW,
        100000100,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_W,
        100000051,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C4_PEAK_W,
        100000087,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.Side_Quest,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_C5,
        100001661,
        SR.MOUNTAIN_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_POT_D3,
        100001194,
        SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.MTN_RACE_C4,
        100000303,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.MTN_RACE_D5,
        100001745,
        SR.BIG_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.MTN_SCOOTER_NPC,
        100002276,
        SR.MOUNTAIN_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_TANNER_NPC,
        100002272,
        SR.MOUNTAIN_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.MTN_TWIG_NPC,
        100002273,
        SR.MOUNTAIN,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.RAV_CHEST_E4,
        100000241,
        SR.BIG_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.RAV_ESTHER_NPC,
        100002286,
        SR.BIG_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.RAV_POT_E2,
        100001123,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.RAV_POT_E3_BEACH,
        100001126,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.RAV_POT_E3_RIVER,
        100001145,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.RAV_POT_E4,
        100002074,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.RAV_POT_F4,
        100002073,
        SR.BIG_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_AVERY,
        100002193,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_AVERY_HAT_RECIPE,
        100002192,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_BRACELET_MONKEY_TUTORIAL,
        100002291,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_CHEST_A3,
        100000184,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.TI_CHEST_B1_MID_CLIFF,
        100000372,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.TI_CHEST_B1_TALLEST,
        100000432,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.TI_CHEST_D1,
        100000183,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [LocationGroup.Surface, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.TI_FRANNY_ITEM,
        100002200,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_FRANNY_NPC,
        100002199,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_GERALD_ITEM,
        100002202,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_GERALD_NPC,
        100002201,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_MARTIN,
        100002196,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_A1,
        100000561,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_A3_BELOW_E,
        100000422,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_A3_WITHIN_CLIFFS,
        100000425,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B0_BONE_PATH,
        100000179,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B0_SW,
        100000234,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_MIDDLE_ROPE,
        100000237,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_PEAK_N,
        100000406,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_PEAK_S,
        100000424,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_BELOW,
        100000225,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_NEXT_TO,
        100000167,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_WATERFALL_PILLAR,
        100000168,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B1_W_ROPE,
        100000411,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_E,
        100000219,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_MIDDLE,
        100000228,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_BELOW_W,
        100000189,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_NW,
        100000202,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_SIMON_E,
        100000175,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_B2_TALL,
        100000426,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.WW_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_C1_HILL,
        100000366,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.LA_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_C1_STICK,
        100000365,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.OoT_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_C2,
        100000371,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_D0,
        100000190,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.TP_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_D1,
        100000232,
        SR.TUTORIAL_ISLAND_BREAKABLES,
        [
            LocationGroup.Surface,
            LocationGroup.Pot,
            LocationGroup.MC_Pot,
        ],
    ),
    GatorLocationData(
        GatorLocationName.TI_POT_Q,
        100002195,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_RACE_C2_CLIFF,
        100000391,
        SR.TUTORIAL_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.TI_RACE_C2_MARTIN,
        100000382,
        SR.TUTORIAL_ISLAND_RACES,
        [LocationGroup.Surface, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.TI_SIMON_ITEM,
        100002198,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_SIMON_NPC,
        100002197,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.TI_STICK,
        100002194,
        StR.TUTORIAL_ISLAND,
        [LocationGroup.Surface, LocationGroup.Main_Quest],
    ),
]

underground_location_table: List[GatorLocationData] = [
    GatorLocationData(
        GatorLocationName.PICKAXE_PICKUP,
        200010001,
        UR.UNDERGROUND_ENTRANCE,
        [LocationGroup.Underground],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1168_H7,
        200001168,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_801_C5,
        200000801,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1161_H7,
        200001161,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1171_I8,
        200001171,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_908_G5,
        200000908,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_907_G5,
        200000907,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_894_G5,
        200000894,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1148_H6,
        200001148,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_602_G5,
        200000602,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_595_G5,
        200000595,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_598_G5,
        200000598,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_597_G5,
        200000597,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_580_G8,
        200000580,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_873_F4,
        200000873,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_874_F4,
        200000874,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_906_F4,
        200000906,
        UR.LIGHTHOUSE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_981_H2,
        200000981,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1166_H6,
        200001166,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1167_H6,
        200001167,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1153_H6,
        200001153,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1180_E5,
        200001180,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1213_E5,
        200001213,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.TP_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_931_G3,
        200000931,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_576_H6,
        200000576,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_579_I8,
        200000579,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1170_I7,
        200001170,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_578_H8,
        200000578,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_890_G4,
        200000890,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_1334_E3,
        200001334,
        UR.UNDERGROUND_ENTRANCE_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_577_I8,
        200000577,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_875_F3,
        200000875,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_876_F3,
        200000876,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_945_G3,
        200000945,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_910_F2,
        200000910,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_760_B4,
        200000760,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.LA_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_792_C5,
        200000792,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.WW_Pot],
    ),
    GatorLocationData(
        GatorLocationName.JAR_840_F2,
        200000840,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Pot, LocationGroup.OoT_Pot],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_909_G2,
        200000909,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_594_G5,
        200000594,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_604_A5,
        200000604,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_968_H3,
        200000968,
        UR.ROOTS_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_610_B4,
        200000610,
        UR.MINES_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.CHEST_601_G7,
        200000601,
        UR.DRIP_BREAKABLES,
        [LocationGroup.Underground, LocationGroup.Chest],
    ),
    GatorLocationData(
        GatorLocationName.RACE_417_B5,
        200000417,
        UR.MINES_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_499_H8,
        200000499,
        UR.DRIP_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_418_G2,
        200000418,
        UR.ROOTS_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_491_G7,
        200000491,
        UR.DRIP_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_484_D6,
        200000484,
        UR.DRIP_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_413_H2,
        200000413,
        UR.ROOTS_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_468_B4,
        200000468,
        UR.MINES_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.RACE_503_F8,
        200000503,
        UR.DRIP_RACES,
        [LocationGroup.Underground, LocationGroup.Race],
    ),
    GatorLocationData(
        GatorLocationName.WALL_121_H1,
        200000121,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_132_B6,
        200000132,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_119_E6,
        200000119,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_126_D4,
        200000126,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_130_B6,
        200000130,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_146_B5,
        200000146,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_175_F8,
        200000175,
        UR.UNDERGROUND_ENTRANCE,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_148_B5,
        200000148,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_117_F6,
        200000117,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_177_G8,
        200000177,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_181_H6,
        200000181,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_135_G1,
        200000135,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_180_I6,
        200000180,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_209_C7,
        200000209,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_129_C6,
        200000129,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_138_F1,
        200000138,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_127_E4,
        200000127,
        UR.LIGHTHOUSE,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_208_C7,
        200000208,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_149_B5,
        200000149,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_201_I2,
        200000201,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_137_F2,
        200000137,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_131_B6,
        200000131,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_128_E5,
        200000128,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    # GatorLocationData(
    #     GatorLocationName.WALL_136_E1,
    #     200000136,
    #     UR.UNDERGROUND_ENTRANCE,
    #     [LocationGroup.Underground, LocationGroup.Wall],
    # ), # for Darklord area
    GatorLocationData(
        GatorLocationName.WALL_134_E7,
        200000134,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_207_I1,
        200000207,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_120_H2,
        200000120,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_147_B5,
        200000147,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_179_H5,
        200000179,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_133_E7,
        200000133,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_123_G1,
        200000123,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_118_F7,
        200000118,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_122_H2,
        200000122,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.WALL_176_H6,
        200000176,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Wall],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_HOLY_B5,
        200010002,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_LOOKY_C5,
        200010003,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_FLOOFY_F4,
        200010004,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_DRIPPY_G5,
        200010005,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_TREEY_E2,
        200010006,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_FINNY_G8,
        200010007,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_BUBBLY_G7,
        200010008,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_CAKEY_B4,
        200010009,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.CRYPTID_THORNY_G2,
        200010010,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Cryptid],
    ),
    GatorLocationData(
        GatorLocationName.NPC_VAL_NPC,
        200010011,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_VAL_ITEM,
        200010012,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.CLAM_ITEM,
        200010042,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_NPC,
        200020001,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_ITEM,
        200020000,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_1_CRYPTID,
        200020002,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_3_CRYPTID,
        200020003,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_5_CRYPTID,
        200020004,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_NODD_7_CRYPTID,
        200020005,
        UR.UNDERGROUND,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_MADSON_C5,
        200010014,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_MADSON_HAT,
        200010040,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_MADSON_HOVER,
        200010041,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_DAVE_NPC,
        200010015,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JESSIE_NPC,
        200010016,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JESSIE_ITEM,
        200010070,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_TURTLE_NPC,
        200010017,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_TURTLE_ITEM_1,
        200010077,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_TURTLE_ITEM_2,
        200010078,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_ARLOTTE_NPC,
        200010018,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_ARLOTTE_ITEM_1,
        200010073,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_ARLOTTE_ITEM_2,
        200010074,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JANE_D6,
        200010019,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_LOLA_C7,
        200010021,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JANE_LOLA_LETTER_1,
        200010061,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JANE_LOLA_LETTER_2,
        200010062,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_JANE_LOLA_ITEM,
        200010063,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_HARREN_D3,
        200010022,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_BODIE_NPC,
        200010024,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_BODIE_ITEM,
        200010025,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_HEATHER_NPC,
        200010026,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_HEATHER_ITEM,
        200010013,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_MATTHEW_NPC,
        200010027,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_DAVE_MATTHEW_ITEM,
        200010076,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_CRAYFISH_NPC,
        200010028,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_CRAYFISH_ITEM,
        200010072,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_GHOST_NPC,
        200010029,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_GHOST_ITEM,
        200010079,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_CASEY_H6,
        200010030,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.DRONE_GIFT,
        200010071,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_CASSIRON_NPC,
        200010031,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_CASSIRON_ITEM,
        200010075,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_ESTHER_E3,
        200010032,
        UR.UNDERGROUND_ENTRANCE,
        [LocationGroup.Underground, LocationGroup.Side_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_EMILIO_NPC,
        200010033,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_EMILIO_ITEM,
        200010050,
        UR.MINES,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_RUTH_NPC,
        200010034,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_RUTH_ITEM,
        200010052,
        UR.ROOTS,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_AMBERLY_NPC,
        200010035,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
    GatorLocationData(
        GatorLocationName.NPC_AMBERLY_ITEM,
        200010051,
        UR.DRIP,
        [LocationGroup.Underground, LocationGroup.Main_Quest],
    ),
]

location_table = surface_location_table + underground_location_table


def locations_for_group(group: LocationGroup) -> Set[str]:
    location_names = set()
    for data in location_table:
        if group in data.location_groups:
            location_names.add(data.name.value)
    return location_names


location_name_to_id: Dict[str, int] = {
    data.name.value: data.location_id for data in location_table
}

location_name_groups: Dict[str, Set[str]] = {}
for loc_data in location_table:
    loc_group_name = loc_data.name.value.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_data.name.value)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)
