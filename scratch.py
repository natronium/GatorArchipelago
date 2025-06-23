from enum import Enum

with open("out", "w", encoding="utf-8") as f:
    f.write(repr(location_table))


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
    FOR_POT_KI = "West (Forest) - Pot Kid (Eepy Armadillo) Quest Completion NPC"
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
    TI_POT_B1_WATERFALL = "Tutorial Island - Pot (B1) on pillar by waterfalls"
    TI_POT_B1_W_ROPE = "Tutorial Island - Pot (B1) west of rope to tallest peaks on Tutorial Island"
    TI_POT_B2_BELOW_E = "Tutorial Island - Pot (B2) below Gerald to the south near water level (eastmost)"
    TI_POT_B2_BELOW_MIDDLE = "Tutorial Island - Pot (B2) below Gerald to the south near water level (middle)"
    TI_POT_B2_BELOW_W = "Tutorial Island - Pot (B2) below Gerald to the south near water level (westmost)"
    TI_POT_B2_E = "Tutorial Island - Pot (B2) on green cliff east of Simon's starting location"
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

    'Tutorial Island - Avery! Hat Recipe'
'Tutorial Island - Avery! Quest Completion'
'Tutorial Island - Stick Pickup'
'Tutorial Island - Pot? Pickup'
'Tutorial Island - Martin Quest Completion'
'Tutorial Island - Simon (Ragdoll Bear) Quest Completion NPC'
'Tutorial Island - Simon (Ragdoll Bear) Quest Completion Item'
'Tutorial Island - Franny (Stick Duck) Quest Completion NPC'
'Tutorial Island - Franny (Stick Duck) Quest Completion Item'
'Tutorial Island - Gerald (Slime Giraffe) Quest Completion NPC'
'Tutorial Island - Gerald (Slime Giraffe) Quest Completion Item'
'Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet'
'Big Island - ??? (Bracelet Monkey) All Bracelets NPC'
'Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion NPC'
'Northeast (Canyon) - Darcie (Balloon Owl) Quest Completion Item'
"Northeast (Canyon) - Broken Scooter Board Pickup (Kasen's Quest)"
'Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion NPC'
'Northeast (Canyon) - Kasen (Scooter Vulture) Quest Completion Item'
'Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion NPC'
'Northeast (Canyon) - Ssumantha (Waders Opposum) Quest Completion Item'
'Northeast (Canyon) - Mochi (Heights Bear) Quest Completion NPC'
'Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion NPC'
'Southeast (Beach) - Tony (Chess Strategist Eagle) Quest Completion Item'
"Southeast (Beach) - Thrown Pencil 1 (Sam's Quest)"
"Southeast (Beach) - Thrown Pencil 2 (Sam's Quest)"
"Southeast (Beach) - Thrown Pencil 3 (Sam's Quest)"
'Southeast (Beach) - Sam (Pencil Jackal) Quest Completion NPC'
'Southeast (Beach) - Sam (Pencil Jackal) Quest Completion Item'
'Southeast (Beach) - Viraj (Hot Shot Elephant) Quest Completion NPC'
'Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion NPC'
'Southeast (Beach) - Mr. Doddler (No Littering Sloth) Quest Completion Item'
'Southeast (Beach) - Cade (Floofy Bull) Quest Completion NPCs'
'Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion NPCs'
'Southeast (Beach) - Skate Pug (Skate Pug) Quest Completion Item'
'Southeast (Beach) - Joe (Pose Hawk) Quest Completion NPC'
'East (Creeklands) - Madeline (Little Thing Mouse) Quest Completion NPC'
'East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion NPC'
'East (Creeklands) - Robin (Scared-to-Look Robin) Quest Completion Item'
"East (Creeklands) - Retainer Pickup (Becca's Quest)"
'East (Creeklands) - Becca (Retainer Shark) Quest Completion NPC'
"Martin's Main Quest - Lucas (Cool Wolf) Quest Completion Item"
"Martin's Main Quest - Grassing Clippings Collect (Jada's Quest)"
"Martin's Main Quest - Bucket Gift (Jada's Quest)"
"Martin's Main Quest - Water Collect (Jada's Quest)"
"Martin's Main Quest - Jada (Cool Boar) Quest Completion Item"
"Martin's Main Quest - Duke (Cool Goose) Quest Completion Item"
"Martin's Main Quest - Martin's Main Quest Completion NPCs"
'South (Jetty) - Leeland (Painting Rabbit) Quest Completion NPC'
'South (Jetty) - Leeland (Painting Rabbit) Quest Completion Item'
'West (Forest) - Sierra (Origami Crane) Quest Completion NPC'
'West (Forest) - Sierra (Origami Crane) Quest Completion Item'
'West (Forest) - Romeo (Ninja Anteater) Nunchucks'
'West (Forest) - Ninja Clan Quest Completion NPCs'
'West (Forest) - Ninja Clan Quest Completion Item'
'West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion NPCs'
'West (Forest) - Pepperoni (Obstacle Ostrich) Quest Completion Item'
'West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion NPCs'
'West (Forest) - Sorin, Roe, Beeritney (Lunch Trio) Quest Completion Item'
'West (Forest) - Pot Kid (Eepy Armadillo) Quest Completion NPC'
'West (Forest) - Penelope (Bastion Beaver) Quest Completion NPC'
'West (Forest) - Penelope (Bastion Beaver) Quest Completion Item'
'West (Forest) - Eva (Photographer Cat) Quest Completion NPC'
'West (Forest) - Eva (Photographer Cat) Quest Completion Item'
'West (Forest) - Gunther (Sidekick Hippo) Quest Completion NPC'
'West (Forest) - Trish (Invisible Horse) Quest Completion NPC'
'West (Forest) - Tiffany (Princess Cat) Quest Completion NPCs'
'West (Forest) - Tiffany (Princess Cat) Quest Completion Item'
"Jill's Main Quest - Magic Ore Pickup (Susanne's Quest)"
"Jill's Main Quest - Susanne (Paleolithic Gazelle) Quest Completion"
"Jill's Main Quest - Cheese Sandwich Pickup (Gene's Quest)"
"Jill's Main Quest - Gene (Merchant Beaver) Quest Completion Item"
"Jill's Main Quest - Bug Net Gift (Antone's Quest)"
"Jill's Main Quest - Jill's Main Quest Completion NPCs"
"North (Mountain) - Bowling Bomb Gift (Flint's Quest)"
'North (Mountain) - Flint (BombBowl Mole) Quest Completion NPC'
'Central (Ravine) - Esther (Directions Deer) Quest Completion NPC'
'Big Island - Billy (Whale) Quest Completion NPC'
'Big Island - Billy (Whale) Quest Completion Item'
"Big Island - Rock (Zhu's Quest)"
'Big Island - Zhu (Skipping Fox) Quest Completion NPC'
"West (Forest) - Race (G0) starting from island west of Billy's Forest location"
'North (Mountain) - Race (C4) starting on western peak of the Mountain'
'Northeast (Canyon) - Race (C7) starting west of Kasen'
'Northeast (Canyon) - Race (B6) starting east of waterfall on north side of Mountain'
'West (Forest) - Race (H1) starting from southwest of The Tree'
'West (Forest) - Race (F4) starting from west path exit from playground'
'North (Mountain) - Race (D5) starting north of the playground and heading up the Mountain'
'Northeast (Canyon) - Pot (D6) on island in middle of pond northeast of playground'
'West (Forest) - Pot (F3) on north cliff edge of pond with dead trees'
'East (Creeklands) - Pot (E7) northwest of Splash Pad below cliff to northeast'
"Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (west)"
"Southeast (Beach) - Pot (I9) on south end of Skate Pug's island (east)"
'Southeast (Beach) - Pot (H8) on taller section northwest of Skate Pug'
'West (Forest) - Pot (H2) above Trish (Invisible Horse)'
"Southeast (Beach) - Pot (J6) on small tall island east of Leeland's peninsula"
"Southeast (Beach) - Pot (I6) on small island south of Marlow's deck"
'East (Creeklands) - Pot (F7) south of Splash Pad'
'East (Creeklands) - Chest (G8) on peak south of Splash Pad'
"Southeast (Beach) - Chest (H9) on north end of Skate Pug's island"
'Central (Ravine) - Chest (E4) under overhang near river'
"East (Creeklands) - Pot (D8) northwest of Jada's pump below taller cliffs"
'West (Forest) - Pot (G3) on west edge of pond with dead trees'
'West (Forest) - Pot (G4) on south edge of pond with dead trees'
"East (Creeklands) - Pot (F9) on peak north of Duke's pump"
'East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southwest)'
"East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (south)"
"East (Creeklands) - Pot (H5) on pair of peaks northwest of Tony's chessboard (north)"
"East (Creeklands) - Chest (H5) on peak north-northwest of Tony's chessboard"
"Central (Ravine) - Pot (E2) on hill on path east from Penelope's waterfall"
'Central (Ravine) - Pot (E3) south of beach where Esther roams'
'Central (Ravine) - Pot (E3) south of central river east of path south from Esther'
"Northeast (Canyon) - Pot (C8) at end of Kasen's stone outcropping"
'Northeast (Canyon) - Pot (C7) on cliffside west of and below Mochi'
'Northeast (Canyon) - Pot (C8) on cliffside east of and below Mochi'
"Northeast (Canyon) - Chest (D8) on peak northwest of Jada's pump"
"Northeast (Canyon) - Pot (D8) on peak northwest of Jada's pump"
'Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (north)'
'Northeast (Canyon) - Pot (D7) on peak by ropes north of Splash Pan (south)'
"West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (west and up the cliff)"
"West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and down the cliff)"
"West (Forest) - Pot (E1) on cliff side west of Penelope's waterfall (east and up the cliff)"
'East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (northwest)'
'East (Creeklands) - Pot (E7) northwest of Splash Pad on cliff (southeast)'
'West (Forest) - Pot (G3) on cliff overlooking pond with dead trees from the west side'
'Northeast (Canyon) - Pot (A8) on west peak accessible from Billy'
'Northeast (Canyon) - Pot (A8) on north peak accessible from Billy'
"West (Forest) - Pot (H4) south of tallest peak north of Pepperoni's obstacle course"
"West (Forest) - Chest (H4) on tallest peak north of Pepperoni's obstacle course"
"West (Forest) - Pot (H4) east of tallest peak north of Pepperoni's obstacle course"
"West (Forest) - Pot (H4) north of tallest peak north of Pepperoni's obstacle course"
'West (Forest) - Pot (G4) on tall peak east of pond with dead trees (east)'
'West (Forest) - Pot (G4) on tall peak east of pond with dead trees (west)'
'West (Forest) - Pot (G4) south of tall peak east of pond with dead trees'
'West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (west)'
'West (Forest) - Pot (J3) on peninsula with stumps southeast of Ninja Clan (east)'
'West (Forest) - Pot (J0) in tidepool in southwest corner of island (northwest)'
'West (Forest) - Pot (J1) in tidepool in southwest corner of island (southwest)'
'West (Forest) - Pot (J1) in tidepool in southwest corner of island (southeast)'
'East (Creeklands) - Pot (G5) west of Junk4Trash in secluded area filled with ninjas and mimics'
'East (Creeklands) - Chest (G6) north of Junk4Trash'
"Northeast (Canyon) - Pot (B8) on tall rock southwest from Billy's Canyon location"
"Northeast (Canyon) - Pot (C9) on Ssumantha's island (lower)"
"Northeast (Canyon) - Pot (C9) on Ssumantha's island (upper)"
'Central (Ravine) - Pot (F4) on southern tall peak west of playground'
'Central (Ravine) - Pot (E4) on northern tall peak west of playground'
'North (Mountain) - Twig (Flip Pomeranian) Quest Completion NPC'
'North (Mountain) - Neil (Peptalk Rat) Quest Completion NPC'
'North (Mountain) - Neil (Peptalk Rat) Quest Completion Item'
'North (Mountain) - Luisa (Tripping Lizard) Quest Completion NPC'
'North (Mountain) - Luisa (Tripping Lizard) Quest Completion Item'
"Avery!'s Main Quest - Nerf Blaster (Andromeda's Quest)"
"Avery!'s Main Quest - Andromeda (Space Hawk) Quest Completion Item"
"Avery!'s Main Quest - Velma (Western Cow) Quest Completion Item"
"Avery!'s Main Quest - Sorbet (Esme's Quest)"
"Avery!'s Main Quest - Plastic Fangs (Esme's Quest)"
"Avery!'s Main Quest - Esme (Vampire Bat) Quest Completion NPC"
"Avery!'s Main Quest - Avery!'s Main Quest Quest Completion NPC"
"North (Mountain) - Pot (C4) part of Scooter's allergy quest (west)"
"North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, east)"
"North (Mountain) - Pot (C4) part of Scooter's allergy quest (peak northwest, west)"
"North (Mountain) - Pot (C4) part of Scooter's allergy quest (southwest)"
'North (Mountain) - Pot (B4) on cliffside cutout east of raised area in northwest corner of Mountain (east)'
'North (Mountain) - Pot (B4) on cliffside cutout east of raised area in northwest corner of Mountain (west)'
"North (Mountain) - Pot (C4) part of Scooter's allergy quest (northeast)"
'North (Mountain) - Chest (B3) on northwest cliffside of Mountain'
'North (Mountain) - Pot (B4) on raised area in northwest corner of Mountain (northeast)'
'North (Mountain) - Pot (B4) on raised area in northwest corner of Mountain (center)'
'North (Mountain) - Pot (C3) on raised area in northwest corner of Mountain (southwest)'
'North (Mountain) - Pot (C4) on northwest tall peak, north of race'
'North (Mountain) - Chest (C5) below rope northwest of stage area'
'North (Mountain) - Pot (C5) west and up from stage'
"North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (up on rock formation)"
"North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (next to Tanner)"
"North (Mountain) - Pot (B5) part of Tanner's Pot Mimic quest (southwest of Tanner)"
'North (Mountain) - Tanner (Pot Mimic Elk) Quest Completion NPC'
'North (Mountain) - Scooter (Ceramic-Allergy Cougar) Quest Completion NPC'
'Junk 4 Trash - Sticky Hand Purchase'
'Junk 4 Trash - Trampoline Purchase'
'Junk 4 Trash - Trash Can Lid Purchase'
'Junk 4 Trash - Wrench Purchase'
'Junk 4 Trash - Paint Gun Purchase'
'Junk 4 Trash - Grabby Hand Purchase'
'Junk 4 Trash - Roy (Trash Raccoon) All Purchases NPC'
'East (Creeklands) - ??? (Bracelet Monkey) Windmill Bracelet'
'West (Forest) - ??? (Bracelet Monkey) Tree Bracelet'
'North (Mountain) - ??? (Bracelet Monkey) Mountain Bracelet'
"Tutorial Island - Race (C2) starting near Martin's lawn chairs"
'Tutorial Island - Race (C2) starting near grassy cliff'
"Tutorial Island - Pot (B1) between two waterfalls below ???'s Tutorial Island location"
'Tutorial Island - Pot (B1) on pillar by waterfalls'
"Tutorial Island - Pot (B2) on green cliff east of Simon's starting location"
'Tutorial Island - Pot (B0) at the end of the bone path on the west of Tutorial Island'
"Tutorial Island - Chest (D1) on small island south of Jill's picnic table"
'Tutorial Island - Chest (A3) below Gerald to east'
'Tutorial Island - Pot (B2) below Gerald to the south near water level (westmost)'
"Tutorial Island - Pot (D0) on small peninsula southwest of Jill's picnic table"
"Tutorial Island - Pot (B2) on green cliff northwest of Martin's lawn chairs"
'Tutorial Island - Pot (B2) below Gerald to the south near water level (eastmost)'
"Tutorial Island - Pot (B1) between two waterfalls on same level as ???'s Tutorial Island location"
'Tutorial Island - Pot (B2) below Gerald to the south near water level (middle)'
"Tutorial Island - Pot (D1) on small island with chest south of Jill's picnic table"
'Tutorial Island - Pot (B0) southwest of the three ropes in northwest of Tutorial Island'
'Tutorial Island - Pot (B1) near middle rope of the three ropes in northwest of Tutorial Island'
'Tutorial Island - Pot (C1) on rock near Stick pickup location'
"Tutorial Island - Pot (C1) on hill overlooking Jill's picnic table"
'Tutorial Island - Pot (C2) on cliff overlooking rope crossing the waterfall'
'Tutorial Island - Chest (B1) on mid-cliff outcropping visible from bone path on the west of Tutorial Island'
'Tutorial Island - Pot (B1) on peak north of tallest peak on Tutorial Island'
'Tutorial Island - Pot (B1) west of rope to tallest peaks on Tutorial Island'
'Tutorial Island - Pot (A3) on green outcropping below and east of cliffs east of three ropes'
'Tutorial Island - Pot (B1) on peak south of the three ropes in northwest of Tutorial Island'
'Tutorial Island - Pot (A3) on green outcropping within cliffs east of three ropes'
'Tutorial Island - Pot (B2) on tall peak west of Gerald'
'Tutorial Island - Chest (B1) on tallest peak of Tutorial Island'
'Tutorial Island - Pot (A1) near highest rope of the three ropes in northwest of Tutorial Island'
"North (Mountain) - Pot (C3) on cliff area across from Martin's deck (on raised section)"
'North (Mountain) - Pot (C3) on cliff outcropping northwest and down from Twig'
"North (Mountain) - Pot (C3) on cliff area across from Martin's deck (next to cliffface)"
'North (Mountain) - Pot (D3) on cliff outcropping west and down from Twig'