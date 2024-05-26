from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import shield_items, cardboard_destroyer_items

def has_shield(state: CollectionState, player: int) -> bool:
    return state.has_any(shield_items, player)

def has_glider(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return state.has("Glider", player)

def has_cardboard_destroyer(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return state.has_any(cardboard_destroyer_items, player)

