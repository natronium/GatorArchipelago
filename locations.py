from typing import Dict, NamedTuple, Set, Optional
import location_names

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
    location_names.ti_race_1: GatorLocationData("Tutorial Island Races","Race"),
    location_names.ti_race_2: GatorLocationData("Tutorial Island Races","Race"),
    location_names.ti_pot_stick_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_stick_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_waterfall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_waterfall_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_grassy_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_grassy_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_rope_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_behind_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_chest_gerald: GatorLocationData("Tutorial Island Breakables","Chest"),
    location_names.ti_pot_gercliffs_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_gercliffs_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_gercliffs_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_3ropes_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_3ropes_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_3ropes_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_triangle_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_pillar_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_northtall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_southtall_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_southtall_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_southtall_3: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_chest_southtall: GatorLocationData("Tutorial Island Breakables","Chest"),
    location_names.ti_pot_southeast_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_pot_southeast_2: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_chest_southeast: GatorLocationData("Tutorial Island Breakables","Chest"),
    location_names.ti_pot_jill_1: GatorLocationData("Tutorial Island Breakables","Pot"),
    location_names.ti_chest_bone: GatorLocationData("Tutorial Island Breakables","Chest"),
    
    # Central (Ravine)
    location_names.cr_esther_quest: GatorLocationData("Main Island"),
    location_names.cr_pot_south_1: GatorLocationData("Main Island Breakables", "Pot"),
    

    location_names.mi_bracelet_windmill: GatorLocationData("Main Island"),
    location_names.mi_bracelet_mountain: GatorLocationData("Main Island"),
    location_names.mi_bracelet_tree: GatorLocationData("Main Island"),
    location_names.mi_billy_quest: GatorLocationData("Main Island"),
    location_names.mi_darcie_quest: GatorLocationData("Main Island"),
    location_names.mi_skatepug_quest: GatorLocationData("Main Island"),
    location_names.mi_twig_quest: GatorLocationData("Main Island"),
    location_names.mi_viraj_quest: GatorLocationData("Main Island"),
    location_names.mi_eva_quest: GatorLocationData("Main Island"),
    location_names.mi_sam_quest: GatorLocationData("Main Island"),
    location_names.mi_sierra_quest: GatorLocationData("Main Island"),
    location_names.mi_romeo_quest: GatorLocationData("Main Island"),
    location_names.mi_oscar_quest: GatorLocationData("Main Island"),
    location_names.mi_joe_quest: GatorLocationData("Main Island"),
    location_names.mi_kasen_brokenscooter: GatorLocationData("Main Island"),
    location_names.mi_kasen_quest: GatorLocationData("Main Island"),
    location_names.mi_flint_bomb: GatorLocationData("Main Island"),
    location_names.mi_flint_quest: GatorLocationData("Main Island"),
    location_names.mi_ssumantha_quest: GatorLocationData("Main Island"),
    location_names.mi_potkid_quest: GatorLocationData("Main Island"),
    location_names.mi_scooter_quest: GatorLocationData("Main Island"),
    location_names.mi_leeland_quest: GatorLocationData("Main Island"),
    location_names.mi_trish_quest: GatorLocationData("Main Island"),
    location_names.mi_becca_retainerpickup: GatorLocationData("Main Island"),
    location_names.mi_becca_quest: GatorLocationData("Main Island"),
    location_names.mi_luisa_quest: GatorLocationData("Main Island"),
    location_names.mi_madeline_quest: GatorLocationData("Main Island"),
    location_names.mi_pepperoni_quest: GatorLocationData("Main Island"),
    location_names.mi_mochi_quest: GatorLocationData("Main Island"),
    location_names.mi_lunch_quest: GatorLocationData("Main Island"),
    location_names.mi_zhu_rock: GatorLocationData("Main Island"),
    location_names.mi_zhu_quest: GatorLocationData("Main Island"),
    location_names.mi_gunther_quest: GatorLocationData("Main Island"),
    location_names.mi_tony_quest: GatorLocationData("Main Island"),
    location_names.mi_neil_quest: GatorLocationData("Main Island"),
    location_names.mi_robin_quest: GatorLocationData("Main Island"),
    location_names.mi_penelope_quest: GatorLocationData("Main Island"),
    location_names.mi_doddler_quest: GatorLocationData("Main Island"),
    location_names.mi_cade_quest: GatorLocationData("Main Island"), #Note, gives 2 friends b/c Marlow!
    location_names.mi_tiffany_quest: GatorLocationData("Main Island"), #Note, gives 2 friends b/c Carol!
    location_names.mi_tanner_quest: GatorLocationData("Main Island"),
    location_names.amq_andromeda_blaster: GatorLocationData("Main Island"), 
    location_names.amq_andromeda_quest: GatorLocationData("Main Island"), 
    location_names.amq_velma_quest: GatorLocationData("Main Island"), #Note, gives extra friends b/c kiddos!
    location_names.amq_esme_sorbet: GatorLocationData("Main Island"),
    location_names.amq_esme_fangs: GatorLocationData("Main Island"),
    location_names.amq_esme_quest: GatorLocationData("Main Island"), #Note, gives extra friend b/c ice cream Part-Timer
    location_names.amq_avery_quest: GatorLocationData("Main Island"),
    location_names.jmq_susanne_ore: GatorLocationData("Main Island"),
    location_names.jmq_susanne_quest: GatorLocationData("Main Island"),
    location_names.jmq_gene_sandwich: GatorLocationData("Main Island"),
    location_names.jmq_gene_quest: GatorLocationData("Main Island"),
    location_names.jmq_antone_bugnet: GatorLocationData("Main Island"),
    location_names.jmq_antone_quest: GatorLocationData("Main Island"),
    location_names.jmq_jill_quest: GatorLocationData("Main Island"),
    location_names.mmq_lucas_shield: GatorLocationData("Main Island"),
    location_names.mmq_lucas_quest: GatorLocationData("Main Island"),
    location_names.mmq_jada_bucket: GatorLocationData("Main Island"),
    location_names.mmq_jada_leaf: GatorLocationData("Main Island"),
    location_names.mmq_jada_quest: GatorLocationData("Main Island"),
    location_names.mmq_duke_quest: GatorLocationData("Main Island"),
    location_names.mmq_martin_quest: GatorLocationData("Main Island"),
    location_names.j4t_sticky_hand: GatorLocationData("Main Island"),
    location_names.j4t_trampoline: GatorLocationData("Main Island"),
    location_names.j4t_trash_lid: GatorLocationData("Main Island"),
    location_names.j4t_wrench: GatorLocationData("Main Island"),
    location_names.j4t_space_dome: GatorLocationData("Main Island"),
    location_names.j4t_grabby_hand: GatorLocationData("Main Island"),
    location_names.j4t_all_purchases: GatorLocationData("Main Island")
}


location_name_to_id: Dict[str, int] = {name: location_base_id + index for index, name in enumerate(location_table)}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    loc_group_name = loc_name.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_name)
    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)