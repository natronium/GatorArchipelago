from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from .options import GatorOptions
from .items import item_name_groups, item_table
from .locations import location_table

if TYPE_CHECKING:
    from . import GatorWorld


def has_sword(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Sword"], player)


def has_shield(state: CollectionState, player: int) -> bool:
    return state.has_any(
        item_name_groups["Shield"], player
    )  ##Needs to be more complicated because if is recipe shield need a different cardboard destroyer


def has_cardboard_destroyer(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Cardboard_Destroyer"], player)


def has_ranged(state: CollectionState, player: int) -> bool:
    return state.has_any(item_name_groups["Ranged"], player)


def has_glider(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("glider"), player)


def has_broken_scooter(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("broken_scooter"), player)


def has_bomb(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("bomb"), player)


def has_retainer(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("retainer"), player)


def has_sorbet(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("sorbet"), player)


def has_ore(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("ore"), player)


def has_sandwich(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("cheese_sandwich"), player)


def has_bug_net(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("bug_net"), player)


def has_clippings(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("clippings"), player)

def has_water(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("water"), player)

def has_bucket(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("bucket"), player)


def has_rock(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("rock"), player)


def has_bracelet(state: CollectionState, player: int, number: int = 1) -> bool:
    return state.has(item_table.short_to_long("bracelet"), player, number)


def has_starter_hat(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("starter_hat"), player)


def has_pot_q(state: CollectionState, player: int) -> bool:
    return state.has(item_table.short_to_long("pot_q"), player)


# def has_headband(state: CollectionState, player: int) -> bool:
#     return state.has(item_table.get_by_short_name("headband"), player) and has_cardboard_destroyer(state, player)

# def can_shield_jump(state: CollectionState, player: int, options: GatorOptions):
#     return has_shield(state, player) and options.require_shield_jump

# def can_short_climb(state: CollectionState, player: int, options: GatorOptions):
#     return can_shield_jump(state,player,options) or has_bracelet(state,player)


def can_clear_tutorial(
    state: CollectionState, player: int, options: GatorOptions
) -> bool:
    if options.start_with_freeplay:
        return True
    elif (
        has_starter_hat(state, player)
        and has_pot_q(state, player)
        and has_cardboard_destroyer(state, player)
    ):
        return True
    else:
        return False


def set_region_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    ## Need to rework entrances once the names are set rather than generated

    multiworld.get_entrance("Tutorial Island -> Main Island", player).access_rule = (
        lambda state: can_clear_tutorial(state, player, options)
    )
    multiworld.get_entrance(
        "Tutorial Island -> Tutorial Island Breakables", player
    ).access_rule = lambda state: has_cardboard_destroyer(state, player)
    multiworld.get_entrance(
        "Main Island -> Main Island Breakables", player
    ).access_rule = lambda state: has_cardboard_destroyer(state, player)
    multiworld.get_entrance("Main Island -> Junk 4 Trash", player).access_rule = (
        lambda state: has_cardboard_destroyer(state, player)
    )
    multiworld.get_entrance(
        "Main Island Breakables -> Main Island Mountain Breakables", player
    ).access_rule = lambda state: has_bracelet(state, player)


def set_location_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    # Tutorial Island
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_martin_quest_item"), player
        ),
        lambda state: has_pot_q(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_avery_quest_item"), player
        ),
        lambda state: has_starter_hat(state, player)
        and has_cardboard_destroyer(state, player),
    )  # erring on the side of requiring a way to make craft stuff?
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_franny_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )  # requires Jill complete, thus needs cardboard destroyer
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_franny_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )  # requires Jill complete
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_gerald_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_gerald_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ti_bracelet_tutorial"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )  # erring on the side of requiring a way to make craft stuff?

    # Northeast (Canyon)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_darcie_quest_npc"), player
        ),
        lambda state: has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_darcie_quest_item"), player
        ),
        lambda state: has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_kasen_quest_npc"), player
        ),
        lambda state: has_broken_scooter(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_kasen_quest_item"), player
        ),
        lambda state: has_broken_scooter(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_ssumantha_quest_npc"), player
        ),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nec_ssumantha_quest_item"), player
        ),
        lambda state: has_shield(state, player),
    )

    # Southeast (Beach)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_tony_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_tony_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_doddler_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_doddler_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_viraj_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_skatepug_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("seb_skatepug_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )

    # East (Creeklands)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ec_becca_quest_npc"), player
        ),
        lambda state: has_retainer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ec_robin_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ec_robin_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("ec_bracelet_windmill"), player
        ),
        lambda state: has_bracelet(state, player),
    )

    # Martin's Main Quest in East (Creeklands)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mmq_jada_clippings"), player
        ),
        lambda state: has_sword(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mmq_jada_bucket"), player
        ),
        lambda state: has_sword(state, player) and has_clippings(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("mmq_jada_water"), player),
        lambda state: has_sword(state, player)
        and has_clippings(state, player)
        and has_bucket(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mmq_jada_quest_item"), player
        ),
        lambda state: has_sword(state, player)
        and has_clippings(state, player)
        and has_bucket(state, player)
        and has_water(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mmq_martin_quest_npc"), player
        ),
        lambda state: has_sword(state, player)
        and has_clippings(state, player)
        and has_bucket(state, player)
        and has_water(state, player),
    )

    # South (Jetty)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("sj_leeland_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("sj_leeland_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )

    # West (Forest)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_sierra_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_sierra_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_romeo_item"), player),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_ninjaclan_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_ninjaclan_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    # ## Check Pepperoni
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_pepperoni_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_pepperoni_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_potkid_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_penelope_quest_npc"), player
        ),
        lambda state: has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_penelope_quest_item"), player
        ),
        lambda state: has_ranged(state, player),
    )
    # ## Check eva
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_eva_quest_npc"), player
        ),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_eva_quest_item"), player
        ),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_tiffany_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_tiffany_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("wf_bracelet_tree"), player
        ),
        lambda state: has_bracelet(state, player),
    )

    # Jill's Main Quest in West (Forest)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("jmq_susanne_quest_item"), player
        ),
        lambda state: has_ore(state, player)
        and (has_ranged(state, player) or has_sword(state, player)),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("jmq_gene_sandwich"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("jmq_gene_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player)
        and has_sandwich(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("jmq_antone_bugnet"), player
        ),
        lambda state: has_bug_net(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("jmq_jill_quest_npc"), player
        ),
        lambda state: has_bug_net(state, player)
        and has_cardboard_destroyer(state, player)
        and has_sandwich(state, player)
        and has_ore(state, player),
    )

    #TODO: all locations on mountain that need a bracelet should go in a region
    ## TODO: Billy at playground enables getting on Mountain with Glider only, no bracelet

    # North (Mountain)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_flint_quest_npc"), player
        ),
        lambda state: has_ranged(state, player) or has_bomb(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_tanner_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player)
        and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_twig_quest_npc"), player),
        lambda state: has_shield(state, player) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_neil_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_neil_quest_item"), player
        ),
        lambda state: has_cardboard_destroyer(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_scooter_quest_npc"), player
        ),
        lambda state: has_cardboard_destroyer(state, player)
        and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_luisa_quest_npc"), player
        ),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_luisa_quest_item"), player
        ),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("nm_bracelet_mountain"), player
        ),
        lambda state: has_bracelet(state, player),
    )

    # Avery!'s Main Quest in North (Mountain)
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("amq_andromeda_blaster"), player
        ),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("amq_andromeda_quest_item"), player
        ),
        lambda state: has_ranged(state, player) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("amq_velma_quest_item"), player
        ),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("amq_esme_sorbet"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("amq_esme_fangs"), player),
        lambda state: has_sorbet(state, player) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("amq_avery_quest_npc"), player
        ),
        lambda state: has_sorbet(state, player)
        and has_ranged(state, player)
        and has_bracelet(state, player),
    )

    # Central (Ravine)

    # Multiple Locations
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mi_zhu_quest_npc"), player
        ),
        lambda state: has_rock(state, player),
    )
    set_rule(
        multiworld.get_location(
            location_table.short_to_long("mi_bracelet_all_npc"), player
        ),
        lambda state: has_bracelet(state, player) and has_cardboard_destroyer(state, player),
    )

    # Pots, Chests, Races
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_chest_B4_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B4_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B4_2"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B4_3"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B4_4"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B5_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B5_2"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_B5_3"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C3C4_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_2"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_3"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_4"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_5"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_6"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_chest_C5_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C5_1"), player),
        lambda state: has_bracelet(state, player) and has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_pot_A1_4"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_pot_A2_4"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_chest_B1_2"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_pot_B1_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_pot_B1_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_pot_C2_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_chest_D1_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_race_B2_1"), player),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nwt_race_B3_1"), player),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_race_B6_1"), player),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_pot_B8_1"), player),
        lambda state: has_ranged(state, player) or has_bracelet(state, player, 2),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C3_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C3_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_C4_7"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_race_C4_1"), player),
        lambda state: (has_shield(state, player)) and has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_race_C7_1"), player),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_pot_D3_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nm_race_D5_1"), player),
        lambda state: has_bracelet(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_pot_D7_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_pot_D7_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_pot_D7D8_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("nec_chest_D8_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("cr_pot_E4_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("cr_pot_F4_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("ec_pot_F8_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_race_G0_1"), player),
        lambda state: has_shield(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_G4_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_G4_3"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_G4_4"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_chest_H4_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_H4_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("ec_chest_H5_1"), player),
        lambda state: has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("ec_pot_H5_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("ec_pot_H5_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_I4_1"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_J3_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("seb_pot_J6_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
    set_rule(
        multiworld.get_location(location_table.short_to_long("wf_pot_H4_2"), player),
        lambda state: has_bracelet(state, player) or has_ranged(state, player),
    )
