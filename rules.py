from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import item_name_groups

import location_names

if TYPE_CHECKING:
    from . import GatorWorld

def has_sword(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Swords"], player)

def has_shield(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Shields"], player)

def has_cardboard_destroyer(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Cardboard Destroyer"], player)

def has_ranged(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Ranged"], player)

def has_glider(state: CollectionState, player: int) -> bool:
    return state.has("Glider", player)

def has_broken_scooter(state: CollectionState, player: int) -> bool:
    return state.has("Broken Scooter Board", player)

def has_bomb(state: CollectionState, player: int) -> bool:
    return state.has("Bowling Bomb (Item)", player)

def has_retainer(state: CollectionState, player: int) -> bool:
    return state.has("Retainer", player)

def has_sorbet(state: CollectionState, player: int) -> bool:
    return state.has("Sorbet", player)

def has_ore(state: CollectionState, player: int) -> bool:
    return state.has("Magic Ore", player)

def has_sandwich(state: CollectionState, player: int) -> bool:
    return state.has("Cheese Sandwich", player)

def has_bug_net(state: CollectionState, player: int) -> bool:
    return state.has("Bug Net (Item)", player)

def has_clippings(state: CollectionState, player: int) -> bool:
    return state.has("Grass Clippings", player)

def has_bucket(state: CollectionState, player: int) -> bool:
    return state.has("Bucket (Item)", player)

def has_rock(state: CollectionState, player: int) -> bool:
    return state.has("Skipping Rock (Item)", player)

def has_bracelet(state: CollectionState, player: int) -> bool:
    return state.has("Bracelet", player, 1)

def has_starter_hat(state: CollectionState, player: int) -> bool:
    return state.has("Pointy Floppy Thing (Recipe)", player)

def has_pot_with_lid(state: CollectionState, player: int) -> bool:
    return state.has("Pot?", player)

def can_shield_jump(state: CollectionState, player: int, options: GatorOptions):
    return has_shield(state, player) and options.require_shield_jump

def can_short_climb(state: CollectionState, player: int, options: GatorOptions):
    return can_shield_jump(state,player,options) or has_bracelet(state,player)

## check if all bracelets are gettable with one bracelet

def can_clear_tutorial(state: CollectionState, player: int, options: GatorOptions):
    if options.start_with_freeplay:
        return True
    elif has_starter_hat(state, player) and has_pot_with_lid(state, player) and has_cardboard_destroyer(state, player) and can_short_climb(state,player):
        return True
    else:
        return False
    
def set_region_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    multiworld.get_entrance("Tutorial Island -> Main Island", player).access_rule = lambda state: can_clear_tutorial(state,player,options)
    multiworld.get_entrance("Tutorial Island -> Tutorial Island Races", player).access_rule = lambda state: has_shield(state,player)
    multiworld.get_entrance("Main Island -> Main Island Races", player).access_rule = lambda state: has_shield(state,player)
    multiworld.get_entrance("Tutorial Island -> Tutorial Island Breakables", player).access_rule = lambda state: has_cardboard_destroyer(state,player)
    multiworld.get_entrance("Main Island -> Main Island Breakables", player).access_rule = lambda state: has_cardboard_destroyer(state,player)
    multiworld.get_entrance("Main Island -> Junk 4 Trash", player).access_rule = lambda state: has_cardboard_destroyer(state,player)

def set_location_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options


    # Tutorial Island
    set_rule(multiworld.get_location(location_names.ti_martin_quest, player), lambda state: has_pot_with_lid(state, player))
    set_rule(multiworld.get_location(location_names.ti_simon_quest, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_avery_recipe, player),lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_avery_quest, player), lambda state: can_short_climb(state, player, options) and has_starter_hat(state, player) and has_cardboard_destroyer(state, player)) # erring on the side of requiring a way to make craft stuff?
    set_rule(multiworld.get_location(location_names.ti_jill_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.ti_franny_quest, player), lambda state: has_cardboard_destroyer(state, player)) # requires Jill complete, should check if actually requires stick as well (doesn't seem to)
    set_rule(multiworld.get_location(location_names.ti_gerald_quest, player), lambda state: has_cardboard_destroyer(state, player) and can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_bracelet_tutorial, player), lambda state: has_cardboard_destroyer(state, player)) # erring on the side of requiring a way to make craft stuff?    
    set_rule(multiworld.get_location(location_names.ti_pot_grassy_2, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_rope_1, player), lambda state: has_bracelet(state,player))
    set_rule(multiworld.get_location(location_names.ti_pot_behind_1, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_chest_gerald, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_gercliffs_1, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_gercliffs_2, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_gercliffs_3, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_3ropes_1, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_3ropes_2, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_3ropes_3, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_triangle_1, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_pillar_1, player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_southtall_1, player), lambda state: (has_bracelet(state, player) and has_glider(state, player)) or can_shield_jump(state, player, options))
    set_rule(multiworld.get_location(location_names.ti_pot_southtall_2, player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location(location_names.ti_pot_southtall_3, player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location(location_names.ti_chest_southtall, player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location(location_names.ti_chest_southeast, player), lambda state: can_short_climb(state, player) and (can_shield_jump or has_glider))
    set_rule(multiworld.get_location(location_names.ti_chest_bone, player), lambda state: can_short_climb(state, player))


    # quest logic: check for physical accessibility

    # Northeast (Canyon)
    set_rule(multiworld.get_location(location_names.nec_darcie_quest, player), lambda state: has_ranged(state, player))
    set_rule(multiworld.get_location(location_names.nec_kasen_quest, player), lambda state: has_broken_scooter(state, player))
    set_rule(multiworld.get_location(location_names.nec_ssumantha_quest, player), lambda state: has_shield(state, player))
    ## Check mochi

    # Southeast (Beach)
    set_rule(multiworld.get_location(location_names.seb_doddler_quest, player), lambda state: has_cardboard_destroyer(state, player)) ## check if accessible without bracelet
    ## check skate pug
    set_rule(multiworld.get_location(location_names.seb_skatepug_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.seb_tony_quest, player), lambda state: has_cardboard_destroyer(state, player))
    ## check Viraj
    
    # East (Creeklands) in East (Creeklands)
    set_rule(multiworld.get_location(location_names.ec_becca_quest, player), lambda state: has_retainer(state, player))
    set_rule(multiworld.get_location(location_names.ec_robin_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.ec_bracelet_windmill, player), lambda state: has_bracelet(state, player))

    # Martin's Main Quest in East (Creeklands)
    set_rule(multiworld.get_location(location_names.mmq_jada_clippings, player), lambda state: has_sword(state, player))
    set_rule(multiworld.get_location(location_names.mmq_jada_bucket, player), lambda state: has_sword(state, player) and has_clippings(state, player))
    set_rule(multiworld.get_location(location_names.mmq_jada_quest, player), lambda state: has_sword(state, player) and has_clippings(state, player) and has_bucket(state, player))
    set_rule(multiworld.get_location(location_names.mmq_martin_quest, player), lambda state: has_sword(state, player) and has_clippings(state, player) and has_bucket(state, player))


    # South (Jetty)
    set_rule(multiworld.get_location(location_names.sj_leeland_quest, player), lambda state: has_cardboard_destroyer(state, player))
    

    # West (Forest)
    ## Check eva
    set_rule(multiworld.get_location(location_names.wf_eva_quest, player), lambda state: has_bracelet(state, player) or has_ranged(state, player))
    set_rule(multiworld.get_location(location_names.wf_sierra_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.wf_romeo_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.wf_oscar_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.wf_potkid_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.wf_penelope_quest, player), lambda state: has_ranged(state, player)) 
    set_rule(multiworld.get_location(location_names.wf_tiffany_quest, player), lambda state: has_cardboard_destroyer(state, player))
    ## Check Pepperoni
    set_rule(multiworld.get_location(location_names.wf_pepperoni_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.wf_bracelet_tree, player), lambda state: has_bracelet(state, player))
    ## Race by Trish is walkable

    # Jill's Main Quest in West (Forest)
    set_rule(multiworld.get_location(location_names.jmq_susanne_quest, player), lambda state: has_ore(state, player))
    set_rule(multiworld.get_location(location_names.jmq_gene_sandwich, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.jmq_gene_quest, player), lambda state: has_cardboard_destroyer(state, player) and has_sandwich(state, player))
    set_rule(multiworld.get_location(location_names.jmq_antone_quest, player), lambda state: has_bug_net(state, player))
    set_rule(multiworld.get_location(location_names.jmq_jill_quest, player), lambda state: has_bug_net(state, player) and has_cardboard_destroyer(state, player) and has_sandwich(state, player) and has_ore(state, player))
     
    
    # North (Mountain)
    set_rule(multiworld.get_location(location_names.nm_twig_quest, player), lambda state: has_shield(state, player))
    ## check flint
    set_rule(multiworld.get_location(location_names.nm_flint_quest, player), lambda state: has_ranged(state, player) or has_bomb(state, player))
    set_rule(multiworld.get_location(location_names.nm_scooter_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.nm_neil_quest, player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location(location_names.nm_tanner_quest, player), lambda state: has_cardboard_destroyer(state, player)) ## check if requires bracelet
    set_rule(multiworld.get_location(location_names.nm_bracelet_mountain, player), lambda state: has_bracelet(state, player))

    # Avery!'s Main Quest in North (Mountain)
    set_rule(multiworld.get_location(location_names.amq_andromeda_quest, player), lambda state: has_ranged(state, player))
    set_rule(multiworld.get_location(location_names.amq_esme_fangs, player), lambda state: has_sorbet(state, player))
    set_rule(multiworld.get_location(location_names.amq_esme_quest, player), lambda state: has_sorbet(state, player))
    set_rule(multiworld.get_location(location_names.amq_avery_quest, player), lambda state: has_sorbet(state, player) and has_ranged(state, player))

    
    # Central (Ravine)


    # Multiple Locations
    set_rule(multiworld.get_location(location_names.mi_zhu_quest, player), lambda state: has_rock(state, player))
    ## Billy may not need a rule?