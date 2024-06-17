from typing import Dict, NamedTuple, Set, Optional
from . import location_names

from BaseClasses import Location

class GatorLocationData(NamedTuple):
    region: str
    # description: str
    location_group: Optional[str] = None

# Locations: quest completions, ground pickups, races, bracelet purchases, junk 4 trash

location_base_id = 9999999999 #adjust this

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
    # location_names.ti_race_1: GatorLocationData("Tutorial Island Races","Race"),
    # location_names.ti_race_2: GatorLocationData("Tutorial Island Races","Race"),
    # location_names.ti_pot_stick_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_stick_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_waterfall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_waterfall_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_grassy_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_grassy_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_rope_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_behind_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_chest_gerald: GatorLocationData("Tutorial Island Breakables","Chest"),
    # location_names.ti_pot_gercliffs_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_gercliffs_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_gercliffs_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_3ropes_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_3ropes_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_3ropes_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_triangle_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_pillar_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_northtall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_southtall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_southtall_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_southtall_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_chest_southtall: GatorLocationData("Tutorial Island Breakables","Chest"),
    # location_names.ti_pot_southeast_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_pot_southeast_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_chest_southeast: GatorLocationData("Tutorial Island Breakables","Chest"),
    # location_names.ti_pot_jill_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    # location_names.ti_chest_bone: GatorLocationData("Tutorial Island Breakables","Chest"),
    

    # Northeast (Canyon)
    location_names.nec_darcie_quest: GatorLocationData("Main Island"),
    location_names.nec_kasen_brokenscooter: GatorLocationData("Main Island"),
    location_names.nec_kasen_quest: GatorLocationData("Main Island"),
    location_names.nec_ssumantha_quest: GatorLocationData("Main Island"),
    location_names.nec_mochi_quest: GatorLocationData("Main Island"),


    # Southeast (Beach)
    location_names.seb_doddler_quest: GatorLocationData("Main Island"),
    location_names.seb_cade_quest: GatorLocationData("Main Island"), #Note, gives 2 friends b/c Marlow!
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
    location_names.wf_tiffany_quest: GatorLocationData("Main Island"), #Note, gives 2 friends b/c Carol!
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
    location_names.amq_velma_quest: GatorLocationData("Main Island"), #Note, gives extra friends b/c kiddos!
    location_names.amq_esme_sorbet: GatorLocationData("Main Island"),
    location_names.amq_esme_fangs: GatorLocationData("Main Island"),
    location_names.amq_esme_quest: GatorLocationData("Main Island"), #Note, gives extra friend b/c ice cream Part-Timer
    location_names.amq_avery_quest: GatorLocationData("Main Island"),


    # Central (Ravine)
    location_names.cr_esther_quest: GatorLocationData("Main Island"),

    # Multiple Locations
    location_names.mi_billy_quest: GatorLocationData("Main Island"),
    location_names.mi_zhu_rock: GatorLocationData("Main Island"),
    location_names.mi_zhu_quest: GatorLocationData("Main Island"),
    
    # Pots, Chests, and Races
    location_names.nwt_pot_A1_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A1_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A1_3 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A1_4 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A2_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A2_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A2_3 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A2_4 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A2B2_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_A3_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_chest_A3_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.nec_pot_A8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_A8_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nwt_pot_B0_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_chest_B1_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.nwt_chest_B1_2 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.nwt_pot_B1_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B1_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B2_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B2_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B2_3 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B2_4 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_B2_5 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_race_B2_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nwt_race_B3_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nm_chest_B4_1 : GatorLocationData("Main Island Mountain Breakables", "Chest"),
    location_names.nm_pot_B4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B4_2 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B4_3 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B4_4 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B5_1 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B5_2 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_B5_3 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nec_race_B6_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nec_pot_B8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nwt_pot_C1_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_C1_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_C2_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nm_pot_C3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nm_pot_C3_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nm_pot_C3C4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_1 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_2 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_3 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_4 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_5 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_6 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nm_pot_C4_7 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nm_race_C4_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nm_chest_C5_1 : GatorLocationData("Main Island Mountain Breakables", "Chest"),
    location_names.nm_pot_C5_1 : GatorLocationData("Main Island Mountain Breakables", "Pot"),
    location_names.nec_pot_C7_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_C7_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_race_C7_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nec_pot_C8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_C8_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_C8_3 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nwt_pot_D1_1 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_pot_D1_2 : GatorLocationData("Tutorial Island Breakables", "Pot"),
    location_names.nwt_chest_D1_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.nm_pot_D3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nm_race_D5_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.nec_pot_D6_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_D7_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_D7_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_pot_D7D8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_D8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.nec_chest_D8_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.wf_pot_E1_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_E1_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_E1_3 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_pot_E3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_pot_E3E4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_pot_E3F3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_pot_E4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_chest_E4_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.ec_pot_E7_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_E7_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_E7_3 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_E7_4 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.cr_pot_F4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_race_F4_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.wf_race_F4G4_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.ec_pot_F7_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_F8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_race_G0_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.wf_pot_G3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_G3G4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_G4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_G4_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_G4_3 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_G4_4 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_G5_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_chest_G6_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.ec_chest_G8_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.wf_pot_H2_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_race_H2_1 : GatorLocationData("Main Island Races", "Race"),
    location_names.wf_chest_H4_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.wf_pot_H4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_H4_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_chest_H5_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.ec_pot_H5_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.ec_pot_H5_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_pot_H8I8_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_chest_H9_1 : GatorLocationData("Main Island Breakables", "Chest"),
    location_names.wf_pot_I4_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_pot_I9_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_pot_I9_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_J1_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_J1_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_J1_3 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_J3_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.wf_pot_J3_2 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_pot_J6_1 : GatorLocationData("Main Island Breakables", "Pot"),
    location_names.seb_pot_J6_2 : GatorLocationData("Main Island Breakables", "Pot"),
}


location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)