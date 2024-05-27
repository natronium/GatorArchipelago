from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import shield_items, cardboard_destroyer_items
if TYPE_CHECKING:
    from . import GatorWorld

def has_shield(state: CollectionState, player: int) -> bool:
    return state.has_any(shield_items, player)

def has_glider(state: CollectionState, player: int) -> bool:
    return state.has("Glider", player)

def has_cardboard_destroyer(state: CollectionState, player: int) -> bool:
    return state.has_any(cardboard_destroyer_items, player)

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
    set_rule(multiworld.get_location("Tutorial Island - Martin Quest Completion", player), lambda state: has_pot_with_lid(state, player))
    set_rule(multiworld.get_location("Tutorial Island - Simon (Ragdoll Bear) Quest Completion", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Avery! Hat Recipe", player),lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Avery! Quest Completion", player), lambda state: can_short_climb(state, player, options) and has_starter_hat(state, player) and has_cardboard_destroyer(state, player)) # erring on the side of requiring a way to make craft stuff?
    set_rule(multiworld.get_location("Tutorial Island - Jill Quest Completion", player), lambda state: has_cardboard_destroyer(state, player))
    set_rule(multiworld.get_location("Tutorial Island - Franny (Stick Duck) Quest Completion", player), lambda state: has_cardboard_destroyer(state, player)) # requires Jill complete, should check if actually requires stick as well (doesn't seem to)
    set_rule(multiworld.get_location("Tutorial Island - Gerald (Slime Giraffe) Quest Completion", player), lambda state: has_cardboard_destroyer(state, player) and can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - ??? (Bracelet Monkey) Tutorial Bracelet", player), lambda state: has_cardboard_destroyer(state, player)) # erring on the side of requiring a way to make craft stuff?    
    set_rule(multiworld.get_location("Tutorial Island - Pot on grassy cliff above north east", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot overlooking rope bridge (to the north)", player), lambda state: has_bracelet(state,player))
    set_rule(multiworld.get_location("Tutorial Island - Pot behind tall cliffs to north", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Chest behind Gerald", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on cliffs in front of Gerald (1)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on cliffs in front of Gerald (2)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on cliffs in front of Gerald (3)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot by three ropes (highest)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot by three ropes (middle)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot by three ropes (lowest)", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on small triangular outcropping", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on pillar", player), lambda state: can_short_climb(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on south tall cliffs, north end", player), lambda state: (has_bracelet(state, player) and has_glider(state, player)) or can_shield_jump(state, player, options))
    set_rule(multiworld.get_location("Tutorial Island - Pot on south tall cliffs, middle", player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location("Tutorial Island - Pot on south tall cliffs, south end", player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location("Tutorial Island - Chest on south tall cliffs, south end", player), lambda state: has_bracelet(state, player))
    set_rule(multiworld.get_location("Tutorial Island - Chest southeast of Jill", player), lambda state: can_short_climb(state, player) and (can_shield_jump or has_glider))
    set_rule(multiworld.get_location("Tutorial Island - Chest visible from bone path", player), lambda state: can_short_climb(state, player))



