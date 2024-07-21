from typing import TYPE_CHECKING, List
from functools import partial

from worlds.generic.Rules import CollectionRule, set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import item_name_groups, item_table
from .locations import location_table

if TYPE_CHECKING:
    from . import GatorWorld


def has_sword(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return state.has_any(item_name_groups["Sword"], player)


def has_shield(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return state.has_any(
        item_name_groups["Shield"], player
    )  ##Needs to be more complicated because if is recipe shield need a different cardboard destroyer


def has_cardboard_destroyer(
    state: CollectionState, player: int, options: GatorOptions
) -> bool:
    return state.has_any(item_name_groups["Cardboard_Destroyer"], player)


def has_ranged(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return state.has_any(item_name_groups["Ranged"], player)


# def has_headband(state: CollectionState, player: int) -> bool:
#     return state.has(item_table.get_by_short_name("headband"), player) and has_cardboard_destroyer(state, player)


def can_shield_jump(state: CollectionState, player: int, options: GatorOptions):
    return has_shield(state, player, options) and options.require_shield_jump


# def can_short_climb(state: CollectionState, player: int, options: GatorOptions):
#     return can_shield_jump(state,player,options) or has_bracelet(state,player)
def has_item(
    short_name: str,
    state: CollectionState,
    player: int,
    count: int = 1,
):
    if item_table.short_to_long(short_name):
        return state.has(item_table.short_to_long(short_name), player, count)
    else:
        print(short_name + " is not a valid item name")
        return False


def can_clear_tutorial(
    state: CollectionState, player: int, options: GatorOptions
) -> bool:
    if options.start_with_freeplay:
        return True
    elif (
        has_item("starter_hat", state, player)
        and has_item("pot_q", state, player)
        and has_cardboard_destroyer(state, player, options)
    ):
        return True
    else:
        return False


def have_enough_friends(state: CollectionState, player: int, options: GatorOptions):
    friend_count = (
        state.count("Friend", player)
        + state.count("Friend x2", player) * 2
        + state.count("Friend x3", player) * 3
        + state.count("Friend x4", player) * 4
    )
    return friend_count >= 35


def can_complete_avery(state: CollectionState, player: int, options: GatorOptions):
    return has_item("sorbet", state, player) and (
        has_cardboard_destroyer(state, player, options)
        or (
            hard_option_enabled(state, player, options)
            and has_ranged(state, player, options)
        )
    )


def can_complete_jill(state: CollectionState, player: int, options: GatorOptions):
    return (
        has_item("bug_net", state, player)
        and has_item("ore", state, player)
        and has_item("sandwich", state, player)
        and (has_sword(state, player, options) or has_shield(state, player, options))
        and has_cardboard_destroyer(state, player, options)
    )


def can_complete_martin(state: CollectionState, player: int, options: GatorOptions):
    return (
        has_item("water", state, player)
        and has_item("clippings", state, player)
        and has_item("bucket", state, player)
        and has_sword(state, player, options)
    )


def hard_option_enabled(
    state: CollectionState, player: int, options: GatorOptions
) -> bool:
    return False


def special_rules_dict():
    return {
        "$can_clear_tutorial": partial(can_clear_tutorial),
        "$sword": partial(has_sword),
        "$shield": partial(has_shield),
        "$ranged": partial(has_ranged),
        "$cardboard_destroyer": partial(has_cardboard_destroyer),
        "$hard": partial(hard_option_enabled),
        "$shield_jump": partial(can_shield_jump),
        "$has_at_least_n_bracelet": partial(has_item, "bracelet"),
        "$has_at_least_n_pencil": partial(has_item, "thrown_pencil"),
    }


def process_access_rules(
    state: CollectionState, player: int, options: GatorOptions, access_rules: List[str]
) -> bool:
    collection_rule = False
    special_rules = special_rules_dict()
    for access_rule in access_rules:
        this_rule = True
        for rule_component in access_rule.split(","):
            rule_component = rule_component.removeprefix(" ")
            if rule_component in special_rules:
                this_rule = this_rule and special_rules[rule_component](
                    state, player, options
                )
            elif rule_component.split("|")[-1].isnumeric():
                this_rule = this_rule and special_rules[
                    rule_component.removesuffix("|" + rule_component.split("|")[-1])
                ](
                    state,
                    player,
                    int(rule_component.split("|")[-1]),
                )
            else:
                this_rule = this_rule and has_item(
                    rule_component,
                    state,
                    player,
                )
        collection_rule = collection_rule or this_rule
        # print(access_rules)
        # print(collection_rule)
    return collection_rule


def set_region_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    ## Need to rework entrances once the names are set rather than generated

    # Current Victory Condition
    multiworld.get_entrance("Tutorial Island -> Playground", player).access_rule = (
        lambda state: can_clear_tutorial(state, player, options)
        and have_enough_friends(state, player, options)
        and can_complete_avery(state, player, options)
        and can_complete_jill(state, player, options)
        and can_complete_martin(state, player, options)
    )

    multiworld.get_entrance("Tutorial Island -> Big Island", player).access_rule = (
        lambda state: can_clear_tutorial(state, player, options)
    )
    multiworld.get_entrance(
        "Tutorial Island -> Tutorial Island Breakables", player
    ).access_rule = lambda state: has_cardboard_destroyer(state, player, options)
    multiworld.get_entrance(
        "Tutorial Island -> Pots Shootable from Tutorial Island", player
    ).access_rule = lambda state: has_ranged(state, player, options)
    multiworld.get_entrance(
        "Big Island -> Big Island Breakables", player
    ).access_rule = lambda state: has_cardboard_destroyer(state, player, options)
    multiworld.get_entrance("Big Island -> Junk 4 Trash", player).access_rule = (
        lambda state: has_cardboard_destroyer(state, player, options)
    )
    multiworld.get_entrance("Big Island -> Mountain", player).access_rule = (
        lambda state: has_item("bracelet", state, player)
        or has_item("glider", state, player)
    )
    multiworld.get_entrance("Mountain -> Mountain Breakables", player).access_rule = (
        lambda state: has_cardboard_destroyer(state, player, options)
    )


def set_location_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    for location_name, location_data in location_table.items():
        if location_data.access_rules:
            multiworld.get_location(location_name, player).access_rule = (
                lambda state, access_rules=location_data.access_rules: process_access_rules(
                    state, player, options, access_rules
                )
            )
