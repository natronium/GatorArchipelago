from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import item_name_groups

import location_names

if TYPE_CHECKING:
    from . import GatorWorld

def has_shield(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Shield"], player)

def has_glider(state: CollectionState, player: int) -> bool:
    return state.has("Glider", player)

def has_cardboard_destroyer(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Cardboard Destroyer"], player)

def has_ranged(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Ranged"], player)

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




    # quest logic: check for physical accessibility and group by region after

    ## Billy may not need a rule?
    set_rule(multiworld.get_location(location_names.mi_darcie_quest, player), lambda state: has_ranged(state, player))
    ## check skate pug
    set_rule(multiworld.get_location(location_names.mi_skatepug_quest, player), lambda state: has_cardboard_destroyer(state, player))