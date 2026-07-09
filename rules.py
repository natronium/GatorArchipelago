from enum import Enum, auto
from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from BaseClasses import CollectionState
from .options import (
    LocationsIncluded,
    RequireVerticalForITD,
    RequireShieldFlip,
    StartWithFreeplay,
    HarderRangedQuests,
    LockPotsBehindItems,
    LockChestsBehindKey,
    LockRacesBehindFlag,
)
from .items import ItemGroup as IG, GatorItemName as I, GatorEventName as E
from .locations import location_table, GatorLocationName as L, LocationGroup as LG

from rule_builder.rules import (
    Or,
    Rule,
    True_,
    OptionFilter,
    Has as RBHas,
    HasAll as RBHasAll,
    HasAny as RBHasAny,
    HasGroup as RBHasGroup,
    HasGroupUnique as RBHasGroupUnique,
    CanReachLocation as RBCanReachLocation,
)
from collections.abc import Iterable

if TYPE_CHECKING:
    from . import GatorWorld


@dataclasses.dataclass()
class HasEnoughFriends(Rule["GatorWorld"], game="Lil Gator Game"):
    # Surface goal requires 35 friends
    def _instantiate(self, world: "GatorWorld") -> "Resolved":
        return self.Resolved(player=world.player)

    class Resolved(Rule.Resolved):
        def _evaluate(self, state: "CollectionState") -> bool:
            friend_count = (
                state.count(I.FRIEND_1.value, self.player)
                + state.count(I.FRIEND_2.value, self.player) * 2
                + state.count(I.FRIEND_3.value, self.player) * 3
                + state.count(I.FRIEND_4.value, self.player) * 4
            )
            return friend_count >= 35

        def item_dependencies(self) -> dict[str, set[int]]:
            return {
                I.FRIEND_1.value: {id(self)},
                I.FRIEND_2.value: {id(self)},
                I.FRIEND_3.value: {id(self)},
                I.FRIEND_4.value: {id(self)},
            }


# Override Has, etc. to take GatorItemName enum instead of string
@dataclasses.dataclass()
class Has(RBHas, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        item_name: I | E,
        count=1,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(
            item_name.value,
            count=count,
            options=options,
            filtered_resolution=filtered_resolution,
        )


@dataclasses.dataclass()
class HasAny(RBHasAny, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        *item_names: I | E,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names),
            options=options,
            filtered_resolution=filtered_resolution
        )


@dataclasses.dataclass()
class HasAll(RBHasAll, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        *item_names: I | E,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names),
            options=options,
            filtered_resolution=filtered_resolution
        )


@dataclasses.dataclass()
class HasGroup(RBHasGroup, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        item_name_group: IG,
        count=1,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(
            item_name_group.value,
            count=count,
            options=options,
            filtered_resolution=filtered_resolution,
        )


@dataclasses.dataclass()
class HasGroupUnique(RBHasGroupUnique, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        item_name_group: IG,
        count=1,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(
            item_name_group.value,
            count=count,
            options=options,
            filtered_resolution=filtered_resolution,
        )


@dataclasses.dataclass()
class CanReachLocation(RBCanReachLocation, game="Lil Gator Game"):

    @override
    def __init__(
        self,
        location_name: L,
        options: "Iterable[OptionFilter]" = (),
        filtered_resolution: bool = False,
    ) -> None:
        super().__init__(
            location_name.value,
            options=options,
            filtered_resolution=filtered_resolution,
        )


# Key items
has_cardboard_destroyer = HasGroup(IG.Cardboard_Destroyer)
# Ragdoll, Balloon, Bubble Gum, Sticky Hand, and Firework are not usually progression, so will only be required if awkward progression is on
# TODO: check for other sources of ragdoll
can_ragdoll = has_cardboard_destroyer & (
    HasAny(I.RAGDOLL, I.BALLOON, I.BUBBLEGUM, I.STICKY_HAND)
    | (HasAny(I.FIREWORK, I.SPIDER_WEB) & Has(I.CHARM_KEYCHAIN))
)

has_sword = has_cardboard_destroyer & HasGroup(IG.Sword)
has_shield = has_cardboard_destroyer & HasGroup(IG.Shield)
has_ranged = HasGroup(IG.Ranged)
has_stone_break = has_cardboard_destroyer & (
    HasAny(I.PICKAXE, I.GIANT_CLUB) | (HasAny(I.VIKING_HORNS, I.BONEHEAD) & can_ragdoll)
)

# option related
can_shield_jump = (
    True_(options=[OptionFilter(RequireShieldFlip, 1)]) | Has(E.OOL)
) & has_shield

can_do_hard_ranged_quests = (
    has_cardboard_destroyer
    & (True_(options=[OptionFilter(HarderRangedQuests, 1)]) | Has(E.OOL))
    | has_ranged
)
can_do_andromeda = has_cardboard_destroyer & (
    (Has(I.GLIDER, options=[OptionFilter(HarderRangedQuests, 1)]) | Has(E.OOL))
    | has_ranged
)

no_pot_break_item = True_(options=[OptionFilter(LockPotsBehindItems, 0)])
can_open_chests = True_(options=[OptionFilter(LockChestsBehindKey, 0)]) | Has(I.KEY)
can_race = True_(options=[OptionFilter(LockRacesBehindFlag, 0)]) | Has(I.FINISH_FLAG)


# Charm Items
def has_charm_amount(n: int) -> Rule:
    return Has(I.CHARM_KEYCHAIN) & HasGroupUnique(IG.Charm, n)


# TODO: Put this behind an option
def can_slam(n: int) -> Rule:
    return (
        has_charm_amount(n) & has_cardboard_destroyer & HasAny(I.PICKAXE, I.GIANT_CLUB)
    )


def can_spin_jump(n: int) -> Rule:
    return (
        has_charm_amount(n) & has_cardboard_destroyer & HasAny(I.RIBBON, I.BUBBLE_WAND)
    )


def can_dash(n: int) -> Rule:
    return (
        has_charm_amount(n)
        & has_cardboard_destroyer
        & HasAny(I.FLASHSTEP, I.JOUSTING_LANCE)
    )


ug_require_vertical = Or(
    Has(I.BRACELET),
    can_spin_jump(1),
    options=[OptionFilter(RequireVerticalForITD, 1)],
    filtered_resolution=True,
)  # TODO: "glitched" logic


# Main quests
can_access_mountain = HasAny(I.GLIDER, I.BRACELET) | can_spin_jump(1)
can_clear_tutorial = True_(options=[OptionFilter(StartWithFreeplay, 1)]) | (
    HasAll(I.STARTER_HAT, I.POT_Q) & has_cardboard_destroyer
)
can_complete_avery = Has(I.SORBET) & can_do_andromeda
can_complete_jill = HasAll(I.BUG_NET, I.ORE, I.SANDWICH) & (has_sword | has_ranged)
can_complete_martin = HasAll(I.WATER, I.CLIPPINGS, I.BUCKET) & has_sword
can_complete_main_game = (
    can_clear_tutorial
    & can_complete_avery
    & can_access_mountain
    & can_complete_jill
    & can_complete_martin
    & HasEnoughFriends()
    & (Has(I.BRACELET) | can_spin_jump(1))
    # needed for Flashback #TODO: test alternates
)
can_complete_emilio = Has(I.MINE_FRIEND, 4)  # TODO: anything else
can_complete_ruth = Has(
    I.ROOTS_FRIEND, 4
)  # TODO: anything else # needs sword (or shield??)
can_complete_amberly = Has(
    I.DRIP_FRIEND, 4
)  # TODO: anything else   # needs racing tools
can_complete_itd = can_complete_emilio & can_complete_ruth & can_complete_amberly


gator_location_rules: dict[L, Rule["GatorWorld"] | None] = {
    L.AVERY_Q_ANDROMEDA_ITEM: can_do_andromeda,
    L.AVERY_Q_ESME_NPC: Has(I.SORBET),
    L.AVERY_Q_NERF_BLASTER: has_cardboard_destroyer,
    L.AVERY_Q_NPCS: can_complete_avery,
    L.AVERY_Q_PLASTIC_FANGS: Has(I.SORBET),
    L.AVERY_Q_SORBET: None,
    L.AVERY_Q_VELMA_ITEM: None,
    L.BCH_CADE_NPCS: None,
    L.BCH_CHEST_H9: can_open_chests,
    L.BCH_JOE_NPC: None,
    L.BCH_MR_DODDLER_ITEM: has_cardboard_destroyer,
    L.BCH_MR_DODDLER_NPC: has_cardboard_destroyer,
    L.BCH_POT_H8: None,
    L.BCH_POT_I6: None,
    L.BCH_POT_I9_E: None,
    L.BCH_POT_I9_W: None,
    L.BCH_POT_J6: (
        has_ranged
        | Has(I.BRACELET)
        | can_spin_jump(1)
        | can_shield_jump
        | can_slam(1)
        | can_dash(1)
    ),
    L.BCH_SAM_ITEM: Has(I.THROWN_PENCIL, 3),
    L.BCH_SAM_NPC: Has(I.THROWN_PENCIL, 3),
    L.BCH_SKATE_PUG_ITEM: has_cardboard_destroyer,
    L.BCH_SKATE_PUG_NPCS: has_cardboard_destroyer,
    L.BCH_THROWN_PENCIL_1: None,
    L.BCH_THROWN_PENCIL_2: Has(I.THROWN_PENCIL, 1),
    L.BCH_THROWN_PENCIL_3: Has(I.THROWN_PENCIL, 2),
    L.BCH_TONY_ITEM: has_cardboard_destroyer,
    L.BCH_TONY_NPC: has_cardboard_destroyer,
    L.BCH_VIRAJ_NPC: has_cardboard_destroyer,
    L.BI_BILLY_ITEM: None,
    L.BI_BILLY_NPC: None,
    L.BI_BRACELET_MONKEY_ALL_BRACELETS_NPC: None,
    L.BI_ROCK: None,
    L.BI_ZHU_NPC: Has(I.ROCK),
    L.CAN_BROKEN_SCOOTER_BOARD: None,
    L.CAN_CHEST_D8: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)) & can_open_chests,
    L.CAN_DARCIE_ITEM: has_ranged | can_spin_jump(1) | can_dash(1),
    L.CAN_DARCIE_NPC: has_ranged | can_spin_jump(1) | can_dash(1),
    L.CAN_KASEN_ITEM: Has(I.BROKEN_SCOOTER),
    L.CAN_KASEN_NPC: Has(I.BROKEN_SCOOTER),
    L.CAN_MOCHI_NPC: Has(I.BRACELET) | can_shield_jump | can_spin_jump(1),
    L.CAN_POT_A8_N: None,
    L.CAN_POT_A8_W: None,
    L.CAN_POT_B8: (has_ranged | Has(I.BRACELET, 2) | can_spin_jump(1)),
    L.CAN_POT_C7: None,
    L.CAN_POT_C8_MOCHI: None,
    L.CAN_POT_C8_OUTCROP: None,
    L.CAN_POT_C9_LOWER: None,
    L.CAN_POT_C9_UPPER: None,
    L.CAN_POT_D6: None,
    L.CAN_POT_D7_N: (
        has_ranged
        | HasAny(I.BRACELET, I.GLIDER)
        | can_shield_jump
        | can_spin_jump(1)
        | can_slam(1)
    ),
    L.CAN_POT_D7_S: (
        has_ranged
        | HasAny(I.BRACELET, I.GLIDER)
        | can_shield_jump
        | can_spin_jump(1)
        | can_slam(1)
    ),
    L.CAN_POT_D8: Has(I.BRACELET) | can_spin_jump(1),
    L.CAN_RACE_B6: has_shield | can_dash(1),
    L.CAN_RACE_C7: has_shield | can_dash(1),
    L.CAN_SSUMANTHA_ITEM: has_shield,
    L.CAN_SSUMANTHA_NPC: has_shield,
    L.CRL_BECCA_NPC: Has(I.RETAINER),
    L.CRL_BRACELET_MONKEY_WINDMILL: None,
    L.CRL_CHEST_G6: can_open_chests,
    L.CRL_CHEST_G8: can_open_chests,
    L.CRL_CHEST_H5: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)) & can_open_chests,
    L.CRL_MADELINE_NPC: None,
    L.CRL_POT_D8: None,
    L.CRL_POT_E7_NE: None,
    L.CRL_POT_E7_NW: None,
    L.CRL_POT_E7_SE: None,
    L.CRL_POT_E7_SW: None,
    L.CRL_POT_F7: None,
    L.CRL_POT_F9: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.CRL_POT_G5: None,
    L.CRL_POT_H5_N: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.CRL_POT_H5_S: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.CRL_RETAINER: None,
    L.CRL_ROBIN_ITEM: has_cardboard_destroyer,
    L.CRL_ROBIN_NPC: has_cardboard_destroyer,
    L.FOR_BRACELET_MONKEY_TREE: None,
    L.FOR_CHEST_H4: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)) & can_open_chests,
    L.FOR_EVA_ITEM: Has(I.BRACELET) | can_spin_jump(4),
    L.FOR_EVA_NPC: Has(I.BRACELET) | can_spin_jump(4),
    L.FOR_GUNTHER_NPC: None,
    L.FOR_NINJA_CLAN_ITEM: (
        has_cardboard_destroyer & Has(I.BRACELET) | can_spin_jump(1)
    )
    | has_ranged,
    L.FOR_NINJA_CLAN_NPCS: (
        has_cardboard_destroyer & Has(I.BRACELET) | can_spin_jump(1)
    )
    | has_ranged,
    L.FOR_PENELOPE_ITEM: can_do_hard_ranged_quests,
    L.FOR_PENELOPE_NPC: can_do_hard_ranged_quests,
    L.FOR_PEPPERONI_ITEM: has_cardboard_destroyer & Has(I.BRACELET) | can_spin_jump(1),
    L.FOR_PEPPERONI_NPCS: has_cardboard_destroyer & Has(I.BRACELET) | can_spin_jump(1),
    L.FOR_POT_E1_LOWER_E: None,
    L.FOR_POT_E1_UPPER_E: None,
    L.FOR_POT_E1_UPPER_W: None,
    L.FOR_POT_F3: None,
    L.FOR_POT_G3_CLIFF: None,
    L.FOR_POT_G3_POND: None,
    L.FOR_POT_G4_DEAD_POND: None,
    L.FOR_POT_G4_E_E: (has_ranged | Has(I.BRACELET) | can_spin_jump(1) | can_slam(2)),
    L.FOR_POT_G4_E_W: (has_ranged | Has(I.BRACELET) | can_spin_jump(1) | can_slam(2)),
    L.FOR_POT_G4_S: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_spin_jump(1) | can_slam(2)
    ),
    L.FOR_POT_H2: None,
    L.FOR_POT_H4_E: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.FOR_POT_H4_N: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.FOR_POT_H4_S: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.FOR_POT_J0: None,
    L.FOR_POT_J1_SE: None,
    L.FOR_POT_J1_SW: None,
    L.FOR_POT_J3_E: None,
    L.FOR_POT_J3_W: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_spin_jump(1) | can_slam(1)
    ),
    L.FOR_POT_KID_NPC: has_cardboard_destroyer,
    L.FOR_RACE_F4: None,
    L.FOR_RACE_G0: has_shield | can_dash(1),
    L.FOR_RACE_H1: None,
    L.FOR_ROMEO_NUNCHUCKS: (
        has_cardboard_destroyer & Has(I.BRACELET) | can_spin_jump(1)
    )
    | has_ranged,
    L.FOR_SIERRA_ITEM: has_cardboard_destroyer,
    L.FOR_SIERRA_NPC: has_cardboard_destroyer,
    L.FOR_SORIN_ROE_BEERITNEY_ITEM: None,
    L.FOR_SORIN_ROE_BEERITNEY_NPCS: None,
    L.FOR_TIFFANY_ITEM: has_cardboard_destroyer,
    L.FOR_TIFFANY_NPCS: has_cardboard_destroyer,
    L.FOR_TRISH_NPC: None,
    L.J4T_GRABBY_HAND: None,
    L.J4T_PAINT_GUN: None,
    L.J4T_ROY_ALL_PURCHASES_NPC: None,
    L.J4T_STICKY_HAND: None,
    L.J4T_TRAMPOLINE: None,
    L.J4T_TRASH_CAN_LID: None,
    L.J4T_WRENCH: None,
    L.JET_LEELAND_ITEM: has_cardboard_destroyer,
    L.JET_LEELAND_NPC: has_cardboard_destroyer,
    L.JILL_Q_BUG_NET_GIFT: None,
    L.JILL_Q_CHEESE_SANDWICH: has_cardboard_destroyer,
    L.JILL_Q_GENE_ITEM: has_cardboard_destroyer & Has(I.SANDWICH),
    L.JILL_Q_MAGIC_ORE: None,
    L.JILL_Q_NPCS: can_complete_jill,
    L.JILL_Q_SUSANNE: Has(I.ORE) & (has_ranged | has_sword),
    L.MARTIN_Q_BUCKET_GIFT: Has(I.CLIPPINGS) & has_sword,
    L.MARTIN_Q_DUKE_ITEM: None,
    L.MARTIN_Q_GRASSING_CLIPPINGS: has_sword,
    L.MARTIN_Q_JADA_ITEM: can_complete_martin,
    L.MARTIN_Q_LUCAS_ITEM: None,
    L.MARTIN_Q_NPCS: can_complete_martin,
    L.MARTIN_Q_WATER: HasAll(I.CLIPPINGS, I.BUCKET) & has_sword,
    L.MTN_BOWLING_BOMB_GIFT: None,
    L.MTN_BRACELET_MONKEY_MOUNTAIN: None,
    L.MTN_CHEST_B3: can_open_chests,
    L.MTN_CHEST_C5: can_open_chests,
    L.MTN_FLINT_NPC: has_ranged | Has(I.BOMB),
    L.MTN_LUISA_ITEM: None,
    L.MTN_LUISA_NPC: None,
    L.MTN_NEIL_ITEM: has_cardboard_destroyer,
    L.MTN_NEIL_NPC: has_cardboard_destroyer,
    L.MTN_POT_B4_CENTER: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.MTN_POT_B4_E: None,
    L.MTN_POT_B4_NE: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.MTN_POT_B4_W: None,
    L.MTN_POT_B5_ROCK: None,
    L.MTN_POT_B5_SW: None,
    L.MTN_POT_B5_TANNER: None,
    L.MTN_POT_C3_CLIFFFACE: None,
    L.MTN_POT_C3_DOWN_FROM_TWIG: None,
    L.MTN_POT_C3_RAISED: None,
    L.MTN_POT_C3_SW: None,
    L.MTN_POT_C4_NE: None,
    L.MTN_POT_C4_NW_TALL: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.MTN_POT_C4_PEAK_E: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.MTN_POT_C4_SW: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_spin_jump(1)
    ),
    L.MTN_POT_C4_W: (has_ranged | Has(I.BRACELET) | can_shield_jump | can_spin_jump(1)),
    L.MTN_POT_C4_PEAK_W: (has_ranged | Has(I.BRACELET) | can_spin_jump(1)),
    L.MTN_POT_C5: (has_ranged | Has(I.BRACELET, 2) | can_spin_jump(1)),
    L.MTN_POT_D3: (has_ranged | HasAny(I.BRACELET, I.GLIDER) | can_spin_jump(1)),
    L.MTN_RACE_C4: (Has(I.BRACELET) | can_spin_jump(1)) & (has_shield | can_dash(1)),
    L.MTN_RACE_D5: Has(I.BRACELET) | can_spin_jump(1),
    L.MTN_SCOOTER_NPC: (
        ((Has(I.BRACELET) | can_spin_jump(1)) & has_cardboard_destroyer) | has_ranged
    )
    & (
        no_pot_break_item
        | HasAll(I.OAR, I.TIGER_FORM, I.SLEEP_MASK, I.GUITAR, I.GIANT_SOCKS)
    ),
    L.MTN_TANNER_NPC: has_cardboard_destroyer,
    L.MTN_TWIG_NPC: has_shield,
    L.RAV_CHEST_E4: can_open_chests,
    L.RAV_ESTHER_NPC: None,
    L.RAV_POT_E2: None,
    L.RAV_POT_E3_BEACH: None,
    L.RAV_POT_E3_RIVER: None,
    L.RAV_POT_E4: (has_ranged | Has(I.BRACELET) | can_spin_jump(1) | can_slam(1)),
    L.RAV_POT_F4: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_spin_jump(1) | can_slam(1)
    ),
    L.TI_AVERY: Has(I.STARTER_HAT) & has_cardboard_destroyer,
    L.TI_AVERY_HAT_RECIPE: None,
    L.TI_BRACELET_MONKEY_TUTORIAL: has_cardboard_destroyer,
    L.TI_CHEST_A3: can_open_chests,
    L.TI_CHEST_B1_MID_CLIFF: can_open_chests,
    L.TI_CHEST_B1_TALLEST: (Has(I.BRACELET) | can_slam(1) | can_spin_jump(1))
    & can_open_chests,
    L.TI_CHEST_D1: (
        has_ranged
        | Has(I.BRACELET)
        | can_shield_jump
        | (can_slam(1))
        | can_spin_jump(1)
    )
    & can_open_chests,
    L.TI_FRANNY_ITEM: has_cardboard_destroyer,
    L.TI_FRANNY_NPC: has_cardboard_destroyer,
    L.TI_GERALD_ITEM: has_cardboard_destroyer,
    L.TI_GERALD_NPC: has_cardboard_destroyer,
    L.TI_MARTIN: Has(I.POT_Q),
    L.TI_POT_A1: None,
    L.TI_POT_A3_BELOW_E: None,
    L.TI_POT_A3_WITHIN_CLIFFS: None,
    L.TI_POT_B0_BONE_PATH: None,
    L.TI_POT_B0_SW: None,
    L.TI_POT_B1_MIDDLE_ROPE: None,
    L.TI_POT_B1_PEAK_N: (has_ranged | Has(I.BRACELET) | can_slam(1) | can_spin_jump(1)),
    L.TI_POT_B1_PEAK_S: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_slam(1) | can_spin_jump(1)
    ),
    L.TI_POT_B1_WATERFALL_BELOW: None,
    L.TI_POT_B1_WATERFALL_NEXT_TO: None,
    L.TI_POT_B1_WATERFALL_PILLAR: None,
    L.TI_POT_B1_W_ROPE: (has_ranged | Has(I.BRACELET) | can_slam(1) | can_spin_jump(1)),
    L.TI_POT_B2_BELOW_E: None,
    L.TI_POT_B2_BELOW_MIDDLE: None,
    L.TI_POT_B2_BELOW_W: None,
    L.TI_POT_B2_NW: None,
    L.TI_POT_B2_SIMON_E: None,
    L.TI_POT_B2_TALL: (has_ranged | Has(I.BRACELET) | can_slam(1) | can_spin_jump(1)),
    L.TI_POT_C1_HILL: None,
    L.TI_POT_C1_STICK: None,
    L.TI_POT_C2: (
        has_ranged | Has(I.BRACELET) | can_shield_jump | can_slam(1) | can_spin_jump(1)
    ),
    L.TI_POT_D0: None,
    L.TI_POT_D1: None,
    L.TI_POT_Q: None,
    L.TI_RACE_C2_CLIFF: has_shield | can_slam(2) | can_dash(1),
    L.TI_RACE_C2_MARTIN: has_shield | can_slam(1) | can_dash(1),
    L.TI_SIMON_ITEM: None,
    L.TI_SIMON_NPC: None,
    L.TI_STICK: None,
    #######################
    # Underground locations
    #######################
    L.PICKAXE_PICKUP: None,
    L.JAR_1168_H7: None,  # no vertical needed
    L.JAR_801_C5: None,  # no vertical needed
    L.JAR_792_C5: None,  # no vertical needed
    L.JAR_1161_H7: None,  # no vertical needed
    L.JAR_579_I8: None,  # Reachable with only slam
    L.JAR_577_I8: None,  # Reachable with only slam
    L.JAR_1171_I8: None,  # Reachable with only slam
    L.JAR_908_G5: None,  # no vertical needed
    L.JAR_907_G5: None,  # no vertical needed
    L.JAR_894_G5: None,  # no vertical needed
    L.JAR_1148_H6: None,  # no vertical needed
    L.JAR_602_G5: None,  # no vertical needed
    L.JAR_595_G5: None,  # no vertical needed
    L.JAR_597_G5: None,  # no vertical needed
    L.JAR_598_G5: None,  # no vertical needed
    L.JAR_580_G8: None,  # no vertical needed
    L.JAR_873_F4: None,  # no vertical needed
    L.JAR_874_F4: None,  # no vertical needed
    L.JAR_906_F4: None,  # no vertical needed
    L.JAR_981_H2: None,  # no vertical needed
    L.JAR_1166_H6: None,  # no vertical needed
    L.JAR_1167_H6: None,  # no vertical needed
    L.JAR_1153_H6: None,  # no vertical needed
    L.JAR_1180_E5: None,  # no vertical needed
    L.JAR_1213_E5: None,  # no vertical needed
    L.JAR_931_G3: None,  # no vertical needed
    L.JAR_576_H6: None,  # no vertical needed
    L.JAR_578_H8: None,  # no vertical needed
    L.JAR_1170_I7: None,  # no vertical needed
    L.JAR_890_G4: None,  # no vertical needed
    L.JAR_1334_E3: Has(I.BRACELET)
    | can_spin_jump(
        1
    ),  # Needs vertical traversal #2 star slam, 1 star spin jump # test for 1 star slam...
    L.JAR_875_F3: None,  # no vertical needed
    L.JAR_876_F3: None,  # no vertical needed
    L.JAR_945_G3: None,  # no vertical needed
    L.JAR_910_F2: None,  # no vertical needed
    L.JAR_760_B4: None,  # needs vertical
    L.JAR_840_F2: None,  # no vertical needed
    L.CHEST_909_G2: can_open_chests,  # needs vertical--- 1 Bracelet
    L.CHEST_594_G5: can_open_chests,  # no vertical needed
    L.CHEST_604_A5: can_open_chests,  # Same as Cakey likely
    L.CHEST_968_H3: can_open_chests,  # no vertical needed
    L.CHEST_610_B4: can_open_chests,  # doesn't need vertical
    L.CHEST_601_G7: can_open_chests,  # vertical needed, 1 bracelet
    L.RACE_417_B5: None,  # Probably at least needs shield
    L.RACE_499_H8: None,  # Slam but not nothing
    L.RACE_418_G2: None,
    L.RACE_491_G7: None,  # slam, but not nothing
    L.RACE_484_D6: None,
    L.RACE_413_H2: None,
    L.RACE_468_B4: None,  # standard route blocked by rock walls, on rail line, doable with nothing through strategic falling
    L.RACE_503_F8: None,  # slam, but not nothing
    L.WALL_121_H1: has_stone_break,
    L.WALL_132_B6: has_stone_break,
    L.WALL_119_E6: has_stone_break,
    L.WALL_130_B6: has_stone_break,
    L.WALL_146_B5: has_stone_break,  # part of Dru quest, on same rail line as 146-149
    L.WALL_175_F8: has_stone_break,
    L.WALL_148_B5: has_stone_break,  # by race 468, # part of Dru quest, on same rail line as 146-149
    L.WALL_117_F6: has_stone_break,
    L.WALL_177_G8: has_stone_break,
    L.WALL_181_H6: has_stone_break,
    L.WALL_135_G1: has_stone_break,
    L.WALL_180_I6: has_stone_break,
    L.WALL_209_C7: has_stone_break,
    L.WALL_129_C6: has_stone_break,
    L.WALL_138_F1: has_stone_break,
    L.WALL_127_E4: has_stone_break,  # vertical not needed
    L.WALL_126_D4: has_stone_break,  # vertical not  needed
    L.WALL_128_E5: has_stone_break,  # vertical not  needed (access other two through this one)
    L.WALL_208_C7: has_stone_break,
    L.WALL_149_B5: has_stone_break,  # part of Dru quest, on same rail line as 146-149
    L.WALL_201_I2: has_stone_break,
    L.WALL_137_F2: has_stone_break,
    L.WALL_131_B6: has_stone_break,
    L.WALL_134_E7: has_stone_break,
    L.WALL_207_I1: has_stone_break,
    L.WALL_120_H2: has_stone_break,
    L.WALL_147_B5: has_stone_break,  # part of Dru quest, on same rail line as 146-149
    L.WALL_179_H5: has_stone_break,
    L.WALL_133_E7: has_stone_break,
    L.WALL_123_G1: has_stone_break,
    L.WALL_118_F7: has_stone_break,
    L.WALL_122_H2: has_stone_break,
    L.WALL_176_H6: has_stone_break,
    L.CRYPTID_HOLY_B5: None,
    L.CRYPTID_LOOKY_C5: None,
    L.CRYPTID_FLOOFY_F4: None,  # no vertical
    L.CRYPTID_DRIPPY_G5: None,  # ALmost definitely needs vertical traversal.... found a route without it
    L.CRYPTID_TREEY_E2: None,  # no vertical needed
    L.CRYPTID_FINNY_G8: None,  # probably vertical
    L.CRYPTID_BUBBLY_G7: None,  # Vertical
    L.CRYPTID_CAKEY_B4: None,  # needs verticalw
    L.CRYPTID_THORNY_G2: None,  # no vertical needed
    L.NPC_VAL_NPC: Has(I.CLAM),
    L.NPC_VAL_ITEM: Has(I.CLAM),
    L.CLAM_ITEM: None,
    L.NPC_NODD_NPC: HasGroupUnique(IG.Cryptid, 9),
    L.NPC_NODD_ITEM: HasGroupUnique(IG.Cryptid, 9),
    L.NPC_NODD_1_CRYPTID: HasGroup(IG.Cryptid, 1),
    L.NPC_NODD_3_CRYPTID: HasGroupUnique(IG.Cryptid, 3),
    L.NPC_NODD_5_CRYPTID: HasGroupUnique(IG.Cryptid, 5),
    L.NPC_NODD_7_CRYPTID: HasGroupUnique(IG.Cryptid, 7),
    L.NPC_MADSON_C5: has_cardboard_destroyer,  # technically doable on one trip down
    L.NPC_MADSON_HAT: has_cardboard_destroyer,
    L.NPC_MADSON_HOVER: has_cardboard_destroyer,
    L.NPC_JESSIE_NPC: None,
    L.NPC_JESSIE_ITEM: None,
    L.NPC_TURTLE_NPC: has_stone_break,
    L.NPC_TURTLE_ITEM_1: has_stone_break,
    L.NPC_TURTLE_ITEM_2: has_stone_break,
    L.NPC_ARLOTTE_NPC: has_cardboard_destroyer,
    L.NPC_ARLOTTE_ITEM_1: has_cardboard_destroyer,  # no vertical needed
    L.NPC_ARLOTTE_ITEM_2: has_cardboard_destroyer,
    L.NPC_JANE_D6: HasAll(I.QUEENS_SECRET_LETTER, I.OTHER_QUEENS_SECRET_LETTER),
    L.NPC_LOLA_C7: HasAll(I.QUEENS_SECRET_LETTER, I.OTHER_QUEENS_SECRET_LETTER),
    L.NPC_JANE_LOLA_LETTER_1: None,
    L.NPC_JANE_LOLA_LETTER_2: Has(I.QUEENS_SECRET_LETTER),
    L.NPC_JANE_LOLA_ITEM: HasAll(I.QUEENS_SECRET_LETTER, I.OTHER_QUEENS_SECRET_LETTER),
    L.NPC_HARREN_D3: None,
    L.NPC_BODIE_NPC: None,
    L.NPC_BODIE_ITEM: None,
    L.NPC_HEATHER_NPC: None,
    L.NPC_HEATHER_ITEM: None,
    L.NPC_DAVE_NPC: has_stone_break,
    L.NPC_MATTHEW_NPC: has_stone_break,
    L.NPC_DAVE_MATTHEW_ITEM: has_stone_break,
    L.NPC_CRAYFISH_NPC: has_ranged | Has(I.RUBBER_BALL),  # doable with slam
    L.NPC_CRAYFISH_ITEM: None,
    L.NPC_GHOST_NPC: Has(I.BRACELET)
    | can_spin_jump(1),  # Needs vertical traversal #doable with slam, spin jump
    L.NPC_GHOST_ITEM: Has(I.BRACELET)
    | can_spin_jump(1),  # Needs vertical traversal #doable with slam, spin jump
    L.NPC_CASEY_H6: Has(I.DRONE),
    L.DRONE_GIFT: None,
    L.NPC_CASSIRON_NPC: None,
    L.NPC_CASSIRON_ITEM: None,
    L.NPC_ESTHER_E3: None,
    L.NPC_EMILIO_NPC: can_complete_emilio,
    L.NPC_EMILIO_ITEM: can_complete_emilio,
    L.NPC_RUTH_NPC: can_complete_ruth,
    L.NPC_RUTH_ITEM: can_complete_ruth,
    L.NPC_AMBERLY_NPC: can_complete_amberly,
    L.NPC_AMBERLY_ITEM: can_complete_amberly,
}


def set_location_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    for location_data in location_table:
        rule = gator_location_rules[location_data.name]
        if rule is None:
            rule = True_()
        if LG.OoT_Pot in location_data.location_groups:
            rule = rule & (no_pot_break_item | Has(I.GUITAR))
        elif LG.MC_Pot in location_data.location_groups:
            rule = rule & (no_pot_break_item | Has(I.GIANT_SOCKS))
        elif LG.LA_Pot in location_data.location_groups:
            rule = rule & (no_pot_break_item | Has(I.SLEEP_MASK))
        elif LG.TP_Pot in location_data.location_groups:
            rule = rule & (no_pot_break_item | Has(I.TIGER_FORM))
        elif LG.WW_Pot in location_data.location_groups:
            rule = rule & (no_pot_break_item | Has(I.OAR))
        if rule is not True_():
            if (
                world.options.locations_included
                != LocationsIncluded.option_in_the_dark_locations_only
                and LG.Surface in location_data.location_groups
            ) or (
                world.options.locations_included
                != LocationsIncluded.option_main_locations_only
                and LG.Underground in location_data.location_groups
            ):
                location = multiworld.get_location(location_data.name.value, player)
                world.set_rule(location, rule)
