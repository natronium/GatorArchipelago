from typing import Dict, NamedTuple, Set, Optional
from . import location_names

from BaseClasses import Location

class GatorLocationData(NamedTuple):
    region: str
    # description: str
    location_group: Optional[str] = None
    location_id: Optional[int] = 0

# Locations: quest completions, ground pickups, races, bracelet purchases, junk 4 trash

quest_location_base_id = 2076 # used only for the npc locations, set to be above the max id of pots, chests, races

location_table: Dict[str, GatorLocationData] = {
    # Northwest (Tutorial Island)
    location_names.ti_avery_recipe: GatorLocationData("Tutorial Island"),
    location_names.ti_avery_quest: GatorLocationData("Tutorial Island"),
    location_names.ti_jill_stick: GatorLocationData("Tutorial Island"),
    location_names.ti_jill_quest: GatorLocationData("Tutorial Island"),
    location_names.ti_martin_pot: GatorLocationData("Tutorial Island"),
    location_names.ti_martin_quest: GatorLocationData("Tutorial Island"),
    location_names.ti_simon_quest: GatorLocationData("Tutorial Island"),
    location_names.ti_bracelet_tutorial: GatorLocationData("Tutorial Island"),
    location_names.ti_franny_quest: GatorLocationData("Tutorial Island"),
    location_names.ti_gerald_quest: GatorLocationData("Tutorial Island"),

    # Northeast (Canyon)
    location_names.nec_darcie_quest: GatorLocationData("Main Island"),
    location_names.nec_kasen_brokenscooter: GatorLocationData("Main Island"),
    location_names.nec_kasen_quest: GatorLocationData("Main Island"),
    location_names.nec_ssumantha_quest: GatorLocationData("Main Island"),
    location_names.nec_mochi_quest: GatorLocationData("Main Island"),


    # Southeast (Beach)
    location_names.seb_doddler_quest: GatorLocationData("Main Island"),
    location_names.seb_cade_quest: GatorLocationData("Main Island"),
    location_names.seb_skatepug_quest: GatorLocationData("Main Island"),
    location_names.seb_viraj_quest: GatorLocationData("Main Island"),
    location_names.seb_joe_quest: GatorLocationData("Main Island"),
    location_names.seb_tony_quest: GatorLocationData("Main Island"),
    location_names.seb_sam_quest: GatorLocationData("Main Island"),


    # East (Creeklands)
    location_names.ec_madeline_quest: GatorLocationData("Main Island"),
    location_names.ec_becca_retainerpickup: GatorLocationData("Main Island"),
    location_names.ec_becca_quest: GatorLocationData("Main Island"),
    location_names.ec_robin_quest: GatorLocationData("Main Island"),
    location_names.ec_bracelet_windmill: GatorLocationData("Main Island"),

    # Martin's Main Quest in East (Creeklands)
    location_names.mmq_lucas_shield: GatorLocationData("Main Island"),
    location_names.mmq_lucas_quest: GatorLocationData("Main Island"),
    location_names.mmq_jada_clippings: GatorLocationData("Main Island"),
    location_names.mmq_jada_bucket: GatorLocationData("Main Island"),
    location_names.mmq_jada_quest: GatorLocationData("Main Island"),
    location_names.mmq_duke_quest: GatorLocationData("Main Island"),
    location_names.mmq_martin_quest: GatorLocationData("Main Island"),

    # Junk 4 Trash in East (Creeklands)
    location_names.j4t_sticky_hand: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_trampoline: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_trash_lid: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_wrench: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_space_dome: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_grabby_hand: GatorLocationData("Junk 4 Trash"),
    location_names.j4t_all_purchases: GatorLocationData("Junk 4 Trash"),


    # South (Jetty)
    location_names.sj_leeland_quest: GatorLocationData("Main Island"),


    # West (Forest)
    location_names.wf_sierra_quest: GatorLocationData("Main Island"),
    location_names.wf_romeo_quest: GatorLocationData("Main Island"),
    location_names.wf_oscar_quest: GatorLocationData("Main Island"),
    location_names.wf_eva_quest: GatorLocationData("Main Island"),
    location_names.wf_potkid_quest: GatorLocationData("Main Island"),
    location_names.wf_trish_quest: GatorLocationData("Main Island"),
    location_names.wf_pepperoni_quest: GatorLocationData("Main Island"),
    location_names.wf_lunch_quest: GatorLocationData("Main Island"),
    location_names.wf_gunther_quest: GatorLocationData("Main Island"),
    location_names.wf_tiffany_quest: GatorLocationData("Main Island"),
    location_names.wf_penelope_quest: GatorLocationData("Main Island"),
    location_names.wf_bracelet_tree: GatorLocationData("Main Island"),

    # Jill's Main Quest in West (Forest)
    location_names.jmq_susanne_ore: GatorLocationData("Main Island"),
    location_names.jmq_susanne_quest: GatorLocationData("Main Island"),
    location_names.jmq_gene_sandwich: GatorLocationData("Main Island"),
    location_names.jmq_gene_quest: GatorLocationData("Main Island"),
    location_names.jmq_antone_bugnet: GatorLocationData("Main Island"),
    location_names.jmq_antone_quest: GatorLocationData("Main Island"),
    location_names.jmq_jill_quest: GatorLocationData("Main Island"),


    # North (Mountain)
    location_names.nm_luisa_quest: GatorLocationData("Main Island"),
    location_names.nm_twig_quest: GatorLocationData("Main Island"),
    location_names.nm_flint_bomb: GatorLocationData("Main Island"),
    location_names.nm_flint_quest: GatorLocationData("Main Island"),
    location_names.nm_scooter_quest: GatorLocationData("Main Island"),
    location_names.nm_neil_quest: GatorLocationData("Main Island"),
    location_names.nm_tanner_quest: GatorLocationData("Main Island"),
    location_names.nm_bracelet_mountain: GatorLocationData("Main Island"),

    # Avery!'s Main Quest
    location_names.amq_andromeda_blaster: GatorLocationData("Main Island"), 
    location_names.amq_andromeda_quest: GatorLocationData("Main Island"), 
    location_names.amq_velma_quest: GatorLocationData("Main Island"),
    location_names.amq_esme_sorbet: GatorLocationData("Main Island"),
    location_names.amq_esme_fangs: GatorLocationData("Main Island"),
    location_names.amq_esme_quest: GatorLocationData("Main Island"),
    location_names.amq_avery_quest: GatorLocationData("Main Island"),


    # Central (Ravine)
    location_names.cr_esther_quest: GatorLocationData("Main Island"),

    # Multiple Locations
    location_names.mi_billy_quest: GatorLocationData("Main Island"),
    location_names.mi_zhu_rock: GatorLocationData("Main Island"),
    location_names.mi_zhu_quest: GatorLocationData("Main Island"),
    
    # Pots, Chests, and Races
    location_names.nwt_pot_A1_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 235),
    location_names.nwt_pot_A1_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 238),
    location_names.nwt_pot_A1_3 : GatorLocationData("Tutorial Island Breakables", "Pot", 562),
    location_names.nwt_pot_A1_4 : GatorLocationData("Tutorial Island Breakables", "Pot", 425),
    location_names.nwt_pot_A2_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 229),
    location_names.nwt_pot_A2_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 423),
    location_names.nwt_pot_A2_3 : GatorLocationData("Tutorial Island Breakables", "Pot", 426),
    location_names.nwt_pot_A2_4 : GatorLocationData("Tutorial Island Breakables", "Pot", 427),
    location_names.nwt_pot_A2B2_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 190),
    location_names.nwt_pot_A3_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 220),
    location_names.nwt_chest_A3_1 : GatorLocationData("Main Island Breakables", "Chest", 185),
    location_names.nec_pot_A8_1 : GatorLocationData("Main Island Breakables", "Pot", 1457),
    location_names.nec_pot_A8_2 : GatorLocationData("Main Island Breakables", "Pot", 1464),
    location_names.nwt_pot_B0_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 180),
    location_names.nwt_chest_B1_1 : GatorLocationData("Main Island Breakables", "Chest", 373),
    location_names.nwt_chest_B1_2 : GatorLocationData("Main Island Breakables", "Chest", 433),
    location_names.nwt_pot_B1_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 407),
    location_names.nwt_pot_B1_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 412),
    location_names.nwt_pot_B2_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 168),
    location_names.nwt_pot_B2_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 169),
    location_names.nwt_pot_B2_3 : GatorLocationData("Tutorial Island Breakables", "Pot", 176),
    location_names.nwt_pot_B2_4 : GatorLocationData("Tutorial Island Breakables", "Pot", 203),
    location_names.nwt_pot_B2_5 : GatorLocationData("Tutorial Island Breakables", "Pot", 226),
    location_names.nwt_race_B2_1 : GatorLocationData("Main Island Races", "Race", 392),
    location_names.nwt_race_B3_1 : GatorLocationData("Main Island Races", "Race", 383),
    location_names.nm_chest_B4_1 : GatorLocationData("Main Island Mountain Breakables", "Chest", 494),
    location_names.nm_pot_B4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot", 200),
    location_names.nm_pot_B4_2 : GatorLocationData("Main Island Mountain Breakables", "Pot", 217),
    location_names.nm_pot_B4_3 : GatorLocationData("Main Island Mountain Breakables", "Pot", 693),
    location_names.nm_pot_B4_4 : GatorLocationData("Main Island Mountain Breakables", "Pot", 695),
    location_names.nm_pot_B5_1 : GatorLocationData("Main Island Mountain Breakables", "Pot", 1695),
    location_names.nm_pot_B5_2 : GatorLocationData("Main Island Mountain Breakables", "Pot", 1709),
    location_names.nm_pot_B5_3 : GatorLocationData("Main Island Mountain Breakables", "Pot", 1712),
    location_names.nec_race_B6_1 : GatorLocationData("Main Island Races", "Race", 814),
    location_names.nec_pot_B8_1 : GatorLocationData("Main Island Breakables", "Pot", 2071),
    location_names.nwt_pot_C1_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 366),
    location_names.nwt_pot_C1_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 367),
    location_names.nwt_pot_C2_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 372),
    location_names.nm_pot_C3_1 : GatorLocationData("Main Island Breakables", "Pot", 1157),
    location_names.nm_pot_C3_2 : GatorLocationData("Main Island Breakables", "Pot", 1159),
    location_names.nm_pot_C3C4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot", 696),
    location_names.nm_pot_C4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot", 52),
    location_names.nm_pot_C4_2 : GatorLocationData("Main Island Mountain Breakables", "Pot", 80),
    location_names.nm_pot_C4_3 : GatorLocationData("Main Island Mountain Breakables", "Pot", 88),
    location_names.nm_pot_C4_4 : GatorLocationData("Main Island Mountain Breakables", "Pot", 101),
    location_names.nm_pot_C4_5 : GatorLocationData("Main Island Mountain Breakables", "Pot", 243),
    location_names.nm_pot_C4_6 : GatorLocationData("Main Island Mountain Breakables", "Pot", 1625),
    location_names.nm_pot_C4_7 : GatorLocationData("Main Island Breakables", "Pot", 1167),
    location_names.nm_race_C4_1 : GatorLocationData("Main Island Races", "Race", 304),
    location_names.nm_chest_C5_1 : GatorLocationData("Main Island Mountain Breakables", "Chest", 1651),
    location_names.nm_pot_C5_1 : GatorLocationData("Main Island Mountain Breakables", "Pot", 1662),
    location_names.nec_pot_C7_1 : GatorLocationData("Main Island Breakables", "Pot", 1351),
    location_names.nec_pot_C7_2 : GatorLocationData("Main Island Breakables", "Pot", 1352),
    location_names.nec_race_C7_1 : GatorLocationData("Main Island Races", "Race", 754),
    location_names.nec_pot_C8_1 : GatorLocationData("Main Island Breakables", "Pot", 1350),
    location_names.nec_pot_C8_2 : GatorLocationData("Main Island Breakables", "Pot", 2072),
    location_names.nec_pot_C8_3 : GatorLocationData("Main Island Breakables", "Pot", 2073),
    location_names.nwt_pot_D1_1 : GatorLocationData("Tutorial Island Breakables", "Pot", 191),
    location_names.nwt_pot_D1_2 : GatorLocationData("Tutorial Island Breakables", "Pot", 233),
    location_names.nwt_chest_D1_1 : GatorLocationData("Main Island Breakables", "Chest", 184),
    location_names.nm_pot_D3_1 : GatorLocationData("Main Island Breakables", "Pot", 1195),
    location_names.nm_race_D5_1 : GatorLocationData("Main Island Races", "Race", 1746),
    location_names.nec_pot_D6_1 : GatorLocationData("Main Island Breakables", "Pot", 7),
    location_names.nec_pot_D7_1 : GatorLocationData("Main Island Breakables", "Pot", 1363),
    location_names.nec_pot_D7_2 : GatorLocationData("Main Island Breakables", "Pot", 1364),
    location_names.nec_pot_D7D8_1 : GatorLocationData("Main Island Breakables", "Pot", 1362),
    location_names.ec_pot_D8_1 : GatorLocationData("Main Island Breakables", "Pot", 492),
    location_names.nec_chest_D8_1 : GatorLocationData("Main Island Breakables", "Chest", 1361),
    location_names.wf_pot_E1_1 : GatorLocationData("Main Island Breakables", "Pot", 1381),
    location_names.wf_pot_E1_2 : GatorLocationData("Main Island Breakables", "Pot", 1382),
    location_names.wf_pot_E1_3 : GatorLocationData("Main Island Breakables", "Pot", 1383),
    location_names.cr_pot_E3_1 : GatorLocationData("Main Island Breakables", "Pot", 1127),
    location_names.cr_pot_E3E4_1 : GatorLocationData("Main Island Breakables", "Pot", 1146),
    location_names.cr_pot_E3F3_1 : GatorLocationData("Main Island Breakables", "Pot", 1124),
    location_names.cr_pot_E4_1 : GatorLocationData("Main Island Breakables", "Pot", 2075),
    location_names.cr_chest_E4_1 : GatorLocationData("Main Island Breakables", "Chest", 242),
    location_names.ec_pot_E7_1 : GatorLocationData("Main Island Breakables", "Pot", 63),
    location_names.ec_pot_E7_2 : GatorLocationData("Main Island Breakables", "Pot", 656),
    location_names.ec_pot_E7_3 : GatorLocationData("Main Island Breakables", "Pot", 1432),
    location_names.ec_pot_E7_4 : GatorLocationData("Main Island Breakables", "Pot", 1445),
    location_names.cr_pot_F4_1 : GatorLocationData("Main Island Breakables", "Pot", 2074),
    location_names.wf_race_F4_1 : GatorLocationData("Main Island Races", "Race", 1410),
    location_names.wf_race_F4G4_1 : GatorLocationData("Main Island Races", "Race", 26),
    location_names.ec_pot_F7_1 : GatorLocationData("Main Island Breakables", "Pot", 118),
    location_names.ec_pot_F8_1 : GatorLocationData("Main Island Breakables", "Pot", 652),
    location_names.wf_race_G0_1 : GatorLocationData("Main Island Races", "Race", 73),
    location_names.wf_pot_G3_1 : GatorLocationData("Main Island Breakables", "Pot", 1451),
    location_names.wf_pot_G3G4_1 : GatorLocationData("Main Island Breakables", "Pot", 546),
    location_names.wf_pot_G4_1 : GatorLocationData("Main Island Breakables", "Pot", 547),
    location_names.wf_pot_G4_2 : GatorLocationData("Main Island Breakables", "Pot", 1541),
    location_names.wf_pot_G4_3 : GatorLocationData("Main Island Breakables", "Pot", 1542),
    location_names.wf_pot_G4_4 : GatorLocationData("Main Island Breakables", "Pot", 1543),
    location_names.ec_pot_G5_1 : GatorLocationData("Main Island Breakables", "Pot", 2013),
    location_names.ec_chest_G6_1 : GatorLocationData("Main Island Breakables", "Chest", 2027),
    location_names.ec_chest_G8_1 : GatorLocationData("Main Island Breakables", "Chest", 154),
    location_names.wf_pot_H2_1 : GatorLocationData("Main Island Breakables", "Pot", 95),
    location_names.wf_race_H2_1 : GatorLocationData("Main Island Races", "Race", 1400),
    location_names.wf_chest_H4_1 : GatorLocationData("Main Island Breakables", "Chest", 1519),
    location_names.wf_pot_H4_1 : GatorLocationData("Main Island Breakables", "Pot", 1521),
    location_names.wf_pot_H4_2 : GatorLocationData("Main Island Breakables", "Pot", 1533),
    location_names.ec_chest_H5_1 : GatorLocationData("Main Island Breakables", "Chest", 767),
    location_names.ec_pot_H5_1 : GatorLocationData("Main Island Breakables", "Pot", 722),
    location_names.ec_pot_H5_2 : GatorLocationData("Main Island Breakables", "Pot", 723),
    location_names.seb_pot_H8I8_1 : GatorLocationData("Main Island Breakables", "Pot", 83),
    location_names.seb_chest_H9_1 : GatorLocationData("Main Island Breakables", "Chest", 202),
    location_names.wf_pot_I4_1 : GatorLocationData("Main Island Breakables", "Pot", 1518),
    location_names.seb_pot_I9_1 : GatorLocationData("Main Island Breakables", "Pot", 70),
    location_names.seb_pot_I9_2 : GatorLocationData("Main Island Breakables", "Pot", 78),
    location_names.wf_pot_J1_1 : GatorLocationData("Main Island Breakables", "Pot", 1594),
    location_names.wf_pot_J1_2 : GatorLocationData("Main Island Breakables", "Pot", 1595),
    location_names.wf_pot_J1_3 : GatorLocationData("Main Island Breakables", "Pot", 1597),
    location_names.wf_pot_J3_1 : GatorLocationData("Main Island Breakables", "Pot", 1585),
    location_names.wf_pot_J3_2 : GatorLocationData("Main Island Breakables", "Pot", 1584),
    location_names.seb_pot_J6_1 : GatorLocationData("Main Island Breakables", "Pot", 116),
    location_names.seb_pot_J6_2 : GatorLocationData("Main Island Breakables", "Pot", 102)
}

# Assign ids for quest locations
location_name_to_id: Dict[str, int] = {}
for index, name in enumerate(location_table):
    data = location_table[name]
    if data.location_id == 0:
        location_id = quest_location_base_id + index
    else:
        location_id = data.location_id
    location_name_to_id[name] = location_id

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)