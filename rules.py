from typing import TYPE_CHECKING, List
from functools import partial

from worlds.generic.Rules import CollectionRule, set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import item_name_groups, item_table
from .locations import location_table, GatorLocationName
from rule_builder import Has, HasAny, Rule

if TYPE_CHECKING:
    from . import GatorWorld


def remove_prefix(text: str, prefix: str) -> str:
    if text.startswith(prefix):
        return text[len(prefix) :]
    return text


def remove_suffix(text: str, suffix: str) -> str:
    if text.endswith(suffix):
        return text[: -len(suffix)]
    return text


# fmt: off
def has_sword(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return (
        state.has_any(item_name_groups["Sword"], player) and
        has_cardboard_destroyer(state, player, options)
    )
# fmt: on

# fmt: off
def has_shield(state: CollectionState, player: int, options: GatorOptions) -> bool:
    return (
        state.has_any(item_name_groups["Shield"], player) and
        has_cardboard_destroyer(state, player, options)
    )
# fmt: on


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
    return options.harder_ranged_quests


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
            rule_component = remove_prefix(rule_component, " ")
            if rule_component in special_rules:
                this_rule = this_rule and special_rules[rule_component](
                    state, player, options
                )
            elif rule_component.split("|")[-1].isnumeric():
                this_rule = this_rule and special_rules[
                    remove_suffix(rule_component, "|" + rule_component.split("|")[-1])
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
    multiworld.get_entrance(
        "Big Island -> Big Island Bracelet Shops", player
    ).access_rule = (
        lambda state: has_cardboard_destroyer(state, player, options)
        and has_item("bracelet", state, player)
    )
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




gator_location_rules: dict[GatorLocationName, Rule[GatorWorld]] = {
    GatorLocationName.AVERY_Q_ANDROMEDA_ITEM: ['$ranged', '$hard,$cardboard_destroyer'],
    GatorLocationName.AVERY_Q_ESME_NPC: ['sorbet'],
    GatorLocationName.AVERY_Q_NERF_BLASTER: ['$cardboard_destroyer'],
    GatorLocationName.AVERY_Q_NPCS: ['sorbet,$ranged', '$hard,sorbet,$cardboard_destroyer'],
    GatorLocationName.AVERY_Q_PLASTIC_FANGS: ['sorbet'],
    GatorLocationName.AVERY_Q_SORBET: [],
    GatorLocationName.AVERY_Q_VELMA_ITEM: [],
    GatorLocationName.BCH_CADE_NPCS: [],
    GatorLocationName.BCH_CHEST_H9: [],
    GatorLocationName.BCH_JOE_NPC: [],
    GatorLocationName.BCH_MR_DODDLER_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.BCH_MR_DODDLER_NPC: ['$cardboard_destroyer'],
    GatorLocationName.BCH_POT_H8: [],
    GatorLocationName.BCH_POT_I6: [],
    GatorLocationName.BCH_POT_I9_E: [],
    GatorLocationName.BCH_POT_I9_W: [],
    GatorLocationName.BCH_POT_J6: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.BCH_SAM_ITEM: ['$has_at_least_n_pencil|3'],
    GatorLocationName.BCH_SAM_NPC: ['$has_at_least_n_pencil|3'],
    GatorLocationName.BCH_SKATE_PUG_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.BCH_SKATE_PUG_NPCS: ['$cardboard_destroyer'],
    GatorLocationName.BCH_THROWN_PENCIL_1: [],
    GatorLocationName.BCH_THROWN_PENCIL_2: ['$has_at_least_n_pencil|1'],
    GatorLocationName.BCH_THROWN_PENCIL_3: ['$has_at_least_n_pencil|2'],
    GatorLocationName.BCH_TONY_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.BCH_TONY_NPC: ['$cardboard_destroyer'],
    GatorLocationName.BCH_VIRAJ_NPC: ['$cardboard_destroyer'],
    GatorLocationName.BI_BILLY_ITEM: [],
    GatorLocationName.BI_BILLY_NPC: [],
    GatorLocationName.BI_BRACELET_MONKEY_ALL_BRACELETS_NPC: [],
    GatorLocationName.BI_ROCK: [],
    GatorLocationName.BI_ZHU_NPC: ['rock'],
    GatorLocationName.CAN_BROKEN_SCOOTER_BOARD: [],
    GatorLocationName.CAN_CHEST_D8: ['$ranged', 'bracelet'],
    GatorLocationName.CAN_DARCIE_ITEM: ['$ranged'],
    GatorLocationName.CAN_DARCIE_NPC: ['$ranged'],
    GatorLocationName.CAN_KASEN_ITEM: ['broken_scooter'],
    GatorLocationName.CAN_KASEN_NPC: ['broken_scooter'],
    GatorLocationName.CAN_MOCHI_NPC: [],
    GatorLocationName.CAN_POT_A8_N: [],
    GatorLocationName.CAN_POT_A8_W: [],
    GatorLocationName.CAN_POT_B8: ['$ranged', '$has_at_least_n_bracelet|2'],
    GatorLocationName.CAN_POT_C7: [],
    GatorLocationName.CAN_POT_C8_MOCHI: [],
    GatorLocationName.CAN_POT_C8_OUTCROP: [],
    GatorLocationName.CAN_POT_C9_LOWER: [],
    GatorLocationName.CAN_POT_C9_UPPER: [],
    GatorLocationName.CAN_POT_D6: [],
    GatorLocationName.CAN_POT_D7_N: ['$ranged', 'bracelet', 'glider', '$shield_jump'],
    GatorLocationName.CAN_POT_D7_S: ['$ranged', 'bracelet', 'glider', '$shield_jump'],
    GatorLocationName.CAN_POT_D8: ['$ranged', 'bracelet'],
    GatorLocationName.CAN_RACE_B6: ['$shield'],
    GatorLocationName.CAN_RACE_C7: ['$shield'],
    GatorLocationName.CAN_SSUMANTHA_ITEM: ['$shield'],
    GatorLocationName.CAN_SSUMANTHA_NPC: ['$shield'],
    GatorLocationName.CRL_BECCA_NPC: ['retainer'],
    GatorLocationName.CRL_BRACELET_MONKEY_WINDMILL: [],
    GatorLocationName.CRL_CHEST_G6: [],
    GatorLocationName.CRL_CHEST_G8: [],
    GatorLocationName.CRL_CHEST_H5: ['$ranged', 'bracelet'],
    GatorLocationName.CRL_MADELINE_NPC: [],
    GatorLocationName.CRL_POT_D8: [],
    GatorLocationName.CRL_POT_E7_NE: [],
    GatorLocationName.CRL_POT_E7_NW: [],
    GatorLocationName.CRL_POT_E7_SE: [],
    GatorLocationName.CRL_POT_E7_SW: [],
    GatorLocationName.CRL_POT_F7: [],
    GatorLocationName.CRL_POT_F9: ['$ranged', 'bracelet'],
    GatorLocationName.CRL_POT_G5: [],
    GatorLocationName.CRL_POT_H5_N: ['$ranged', 'bracelet'],
    GatorLocationName.CRL_POT_H5_S: ['$ranged', 'bracelet'],
    GatorLocationName.CRL_RETAINER: [],
    GatorLocationName.CRL_ROBIN_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.CRL_ROBIN_NPC: ['$cardboard_destroyer'],
    GatorLocationName.FOR_BRACELET_MONKEY_TREE: [],
    GatorLocationName.FOR_CHEST_H4: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_EVA_ITEM: ['bracelet'],
    GatorLocationName.FOR_EVA_NPC: ['bracelet'],
    GatorLocationName.FOR_GUNTHER_NPC: [],
    GatorLocationName.FOR_NINJA_CLAN_ITEM: ['$cardboard_destroyer,bracelet', '$ranged'],
    GatorLocationName.FOR_NINJA_CLAN_NPCS: ['$cardboard_destroyer,bracelet', '$ranged'],
    GatorLocationName.FOR_PENELOPE_ITEM: ['$ranged', '$hard,$cardboard_destroyer'],
    GatorLocationName.FOR_PENELOPE_NPC: ['$ranged', '$hard,$cardboard_destroyer'],
    GatorLocationName.FOR_PEPPERONI_ITEM: ['$cardboard_destroyer,bracelet'],
    GatorLocationName.FOR_PEPPERONI_NPCS: ['$cardboard_destroyer,bracelet'],
    GatorLocationName.FOR_POT_E1_LOWER_E: [],
    GatorLocationName.FOR_POT_E1_UPPER_E: [],
    GatorLocationName.FOR_POT_E1_UPPER_W: [],
    GatorLocationName.FOR_POT_F3: [],
    GatorLocationName.FOR_POT_G3_CLIFF: [],
    GatorLocationName.FOR_POT_G3_POND: [],
    GatorLocationName.FOR_POT_G4_DEAD_POND: [],
    GatorLocationName.FOR_POT_G4_E_E: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_POT_G4_E_W: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_POT_G4_S: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.FOR_POT_H2: [],
    GatorLocationName.FOR_POT_H4_E: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_POT_H4_N: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_POT_H4_S: ['$ranged', 'bracelet'],
    GatorLocationName.FOR_POT_J0: [],
    GatorLocationName.FOR_POT_J1_SE: [],
    GatorLocationName.FOR_POT_J1_SW: [],
    GatorLocationName.FOR_POT_J3_E: [],
    GatorLocationName.FOR_POT_J3_W: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.FOR_POT_KID_NPC: ['$cardboard_destroyer'],
    GatorLocationName.FOR_RACE_F4: [],
    GatorLocationName.FOR_RACE_G0: ['$shield'],
    GatorLocationName.FOR_RACE_H1: [],
    GatorLocationName.FOR_ROMEO_NUNCHUCKS: ['$cardboard_destroyer,bracelet', '$ranged'],
    GatorLocationName.FOR_SIERRA_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.FOR_SIERRA_NPC: ['$cardboard_destroyer'],
    GatorLocationName.FOR_SORIN_ROE_BEERITNEY_ITEM: [],
    GatorLocationName.FOR_SORIN_ROE_BEERITNEY_NPCS: [],
    GatorLocationName.FOR_TIFFANY_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.FOR_TIFFANY_NPCS: ['$cardboard_destroyer'],
    GatorLocationName.FOR_TRISH_NPC: [],
    GatorLocationName.J4T_GRABBY_HAND: [],
    GatorLocationName.J4T_PAINT_GUN: [],
    GatorLocationName.J4T_ROY_ALL_PURCHASES_NPC: [],
    GatorLocationName.J4T_STICKY_HAND: [],
    GatorLocationName.J4T_TRAMPOLINE: [],
    GatorLocationName.J4T_TRASH_CAN_LID: [],
    GatorLocationName.J4T_WRENCH: [],
    GatorLocationName.JET_LEELAND_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.JET_LEELAND_NPC: ['$cardboard_destroyer'],
    GatorLocationName.JILL_Q_BUG_NET_GIFT: [],
    GatorLocationName.JILL_Q_CHEESE_SANDWICH: ['$cardboard_destroyer'],
    GatorLocationName.JILL_Q_GENE_ITEM: ['$cardboard_destroyer,sandwich'],
    GatorLocationName.JILL_Q_MAGIC_ORE: [],
    GatorLocationName.JILL_Q_NPCS: ['bug_net,$sword,sandwich,ore', 'bug_net,$ranged,sandwich,ore'],
    GatorLocationName.JILL_Q_SUSANNE: ['ore,$ranged', 'ore,$sword'],
    GatorLocationName.MARTIN_Q_BUCKET_GIFT: ['$sword,clippings'],
    GatorLocationName.MARTIN_Q_DUKE_ITEM: [],
    GatorLocationName.MARTIN_Q_GRASSING_CLIPPINGS: ['$sword'],
    GatorLocationName.MARTIN_Q_JADA_ITEM: ['$sword,clippings,bucket,water'],
    GatorLocationName.MARTIN_Q_LUCAS_ITEM: [],
    GatorLocationName.MARTIN_Q_NPCS: ['$sword,clippings,bucket,water'],
    GatorLocationName.MARTIN_Q_WATER: ['$sword,clippings,bucket'],
    GatorLocationName.MTN_BOWLING_BOMB_GIFT: [],
    GatorLocationName.MTN_BRACELET_MONKEY_MOUNTAIN: [],
    GatorLocationName.MTN_CHEST_B3: [],
    GatorLocationName.MTN_CHEST_C5: [],
    GatorLocationName.MTN_FLINT_NPC: ['$ranged', 'bomb'],
    GatorLocationName.MTN_LUISA_ITEM: [],
    GatorLocationName.MTN_LUISA_NPC: [],
    GatorLocationName.MTN_NEIL_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.MTN_NEIL_NPC: ['$cardboard_destroyer'],
    GatorLocationName.MTN_POT_B4_CENTER: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_B4_E: [],
    GatorLocationName.MTN_POT_B4_NE: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_B4_W: [],
    GatorLocationName.MTN_POT_B5_ROCK: [],
    GatorLocationName.MTN_POT_B5_SW: [],
    GatorLocationName.MTN_POT_B5_TANNER: [],
    GatorLocationName.MTN_POT_C3_CLIFFFACE: ['$ranged', 'bracelet', 'glider'],
    GatorLocationName.MTN_POT_C3_DOWN_FROM_TWIG: [],
    GatorLocationName.MTN_POT_C3_RAISED: [],
    GatorLocationName.MTN_POT_C3_SW: [],
    GatorLocationName.MTN_POT_C4_NE: [],
    GatorLocationName.MTN_POT_C4_NW_TALL: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_C4_PEAK_E: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_C4_SW: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_C4_W: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.MTN_POT_C4_W: ['$ranged', 'bracelet'],
    GatorLocationName.MTN_POT_C5: ['$ranged', '$has_at_least_n_bracelet|2'],
    GatorLocationName.MTN_POT_D3: ['$ranged', 'bracelet', 'glider'],
    GatorLocationName.MTN_RACE_C4: ['$shield,bracelet'],
    GatorLocationName.MTN_RACE_D5: ['bracelet'],
    GatorLocationName.MTN_SCOOTER_NPC: ['bracelet,$cardboard_destroyer', '$ranged'],
    GatorLocationName.MTN_TANNER_NPC: ['$cardboard_destroyer'],
    GatorLocationName.MTN_TWIG_NPC: ['$shield'],
    GatorLocationName.RAV_CHEST_E4: [],
    GatorLocationName.RAV_ESTHER_NPC: [],
    GatorLocationName.RAV_POT_E2: [],
    GatorLocationName.RAV_POT_E3_BEACH: [],
    GatorLocationName.RAV_POT_E3_RIVER: [],
    GatorLocationName.RAV_POT_E4: ['$ranged', 'bracelet'],
    GatorLocationName.RAV_POT_F4: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.TI_AVERY: ['starter_hat,$cardboard_destroyer'],
    GatorLocationName.TI_AVERY_HAT_RECIPE: [],
    GatorLocationName.TI_BRACELET_MONKEY_TUTORIAL: ['$cardboard_destroyer'],
    GatorLocationName.TI_CHEST_A3: [],
    GatorLocationName.TI_CHEST_B1_MID_CLIFF: [],
    GatorLocationName.TI_CHEST_B1_TALLEST: ['bracelet'],
    GatorLocationName.TI_CHEST_D1: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.TI_FRANNY_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.TI_FRANNY_NPC: ['$cardboard_destroyer'],
    GatorLocationName.TI_GERALD_ITEM: ['$cardboard_destroyer'],
    GatorLocationName.TI_GERALD_NPC: ['$cardboard_destroyer'],
    GatorLocationName.TI_MARTIN: ['pot_q'],
    GatorLocationName.TI_POT_A1: [],
    GatorLocationName.TI_POT_A3_BELOW_E: [],
    GatorLocationName.TI_POT_A3_WITHIN_CLIFFS: [],
    GatorLocationName.TI_POT_B0_BONE_PATH: [],
    GatorLocationName.TI_POT_B0_SW: [],
    GatorLocationName.TI_POT_B1_MIDDLE_ROPE: [],
    GatorLocationName.TI_POT_B1_PEAK_N: ['$ranged', 'bracelet'],
    GatorLocationName.TI_POT_B1_PEAK_S: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.TI_POT_B1_WATERFALL_BELOW: [],
    GatorLocationName.TI_POT_B1_WATERFALL_NEXT_TO: [],
    GatorLocationName.TI_POT_B1_WATERFALL_PILLAR: [],
    GatorLocationName.TI_POT_B1_W_ROPE: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.TI_POT_B2_BELOW_E: [],
    GatorLocationName.TI_POT_B2_BELOW_MIDDLE: [],
    GatorLocationName.TI_POT_B2_BELOW_W: [],
    GatorLocationName.TI_POT_B2_NW: [],
    GatorLocationName.TI_POT_B2_SIMON_E: [],
    GatorLocationName.TI_POT_B2_TALL: ['$ranged', 'bracelet'],
    GatorLocationName.TI_POT_C1_HILL: [],
    GatorLocationName.TI_POT_C1_STICK: [],
    GatorLocationName.TI_POT_C2: ['$ranged', 'bracelet', '$shield_jump'],
    GatorLocationName.TI_POT_D0: [],
    GatorLocationName.TI_POT_D1: [],
    GatorLocationName.TI_POT_Q: [],
    GatorLocationName.TI_RACE_C2_CLIFF: ['$shield'],
    GatorLocationName.TI_RACE_C2_MARTIN: ['$shield'],
    GatorLocationName.TI_SIMON_ITEM: [],
    GatorLocationName.TI_SIMON_NPC: [],
    GatorLocationName.TI_STICK: [],
}