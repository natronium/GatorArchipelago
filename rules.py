from typing import TYPE_CHECKING, Any
from typing_extensions import override
import dataclasses

from BaseClasses import CollectionState
from .options import (
    RequireShieldJump,
    StartWithFreeplay,
    HarderRangedQuests,
    LockPotsBehindItems,
    LockChestsBehindKey,
    LockRacesBehindFlag,
)
from .items import ItemGroup as IG, GatorItemName as I, GatorEventName as E
from .locations import location_table, GatorLocationName

try:
    from rule_builder import (
        Rule,
        True_,
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        Rule,
        True_,
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
    )
from collections.abc import Iterable

if TYPE_CHECKING:
    from . import GatorWorld


@dataclasses.dataclass()
class HasEnoughFriends(Rule["GatorWorld"], game="Lil Gator Game"):
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
                I.FRIEND_1: {id(self)},
                I.FRIEND_2: {id(self)},
                I.FRIEND_3: {id(self)},
                I.FRIEND_4: {id(self)},
            }


# Override Has, etc. to take GatorItemName enum instead of string
@dataclasses.dataclass
class Has(RBHas, game="Lil Gator Game"):

    @override
    def __init__(
        self, item_name: I | E, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name.value, count=count, options=options)


@dataclasses.dataclass()
class HasAny(RBHasAny, game="Lil Gator Game"):

    @override
    def __init__(
        self, *item_names: I, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasAll(RBHasAll, game="Lil Gator Game"):

    @override
    def __init__(
        self, *item_names: I, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass
class HasGroup(RBHasGroup, game="Lil Gator Game"):

    @override
    def __init__(
        self, item_name_group: IG, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name_group.value, count=count, options=options)


# Key items
has_cardboard_destroyer = HasGroup(IG.Cardboard_Destroyer)

has_sword = has_cardboard_destroyer & HasGroup(IG.Sword)
has_shield = has_cardboard_destroyer & HasGroup(IG.Shield)
has_ranged = HasGroup(IG.Ranged)

# option related
can_shield_jump = (
    True_(options=[OptionFilter(RequireShieldJump, 1)]) | Has(E.OOL)
) & has_shield
can_do_hard_ranged_quests = (
    has_cardboard_destroyer
    & (True_(options=[OptionFilter(HarderRangedQuests, 1)]) | Has(E.OOL))
    | has_ranged
)

no_pot_break_item = True_(options=[OptionFilter(LockPotsBehindItems,0)])
can_open_chests = True_(options=[OptionFilter(LockChestsBehindKey, 0)]) | Has(I.KEY)
can_race = True_(options=[OptionFilter(LockRacesBehindFlag, 0)]) | Has(I.FINISH_FLAG)

# Main quests
can_clear_tutorial = True_(options=[OptionFilter(StartWithFreeplay, 1)]) | (
    HasAll(I.STARTER_HAT, I.POT_Q) & has_cardboard_destroyer
)
can_complete_avery = Has(I.SORBET) & can_do_hard_ranged_quests
can_complete_jill = HasAll(I.BUG_NET, I.ORE, I.SANDWICH) & (has_sword | has_ranged)
can_complete_martin = HasAll(I.WATER, I.CLIPPINGS, I.BUCKET) & has_sword
can_complete_game = (
    can_clear_tutorial
    & can_complete_avery
    & can_complete_jill
    & can_complete_martin
    & HasEnoughFriends()
)


gator_location_rules: dict[GatorLocationName, Rule["GatorWorld"] | None] = {
    GatorLocationName.AVERY_Q_ANDROMEDA_ITEM: can_do_hard_ranged_quests,
    GatorLocationName.AVERY_Q_ESME_NPC: Has(I.SORBET),
    GatorLocationName.AVERY_Q_NERF_BLASTER: has_cardboard_destroyer,
    GatorLocationName.AVERY_Q_NPCS: can_complete_avery,
    GatorLocationName.AVERY_Q_PLASTIC_FANGS: Has(I.SORBET),
    GatorLocationName.AVERY_Q_SORBET: None,
    GatorLocationName.AVERY_Q_VELMA_ITEM: None,
    GatorLocationName.BCH_CADE_NPCS: None,
    GatorLocationName.BCH_CHEST_H9: can_open_chests,
    GatorLocationName.BCH_JOE_NPC: None,
    GatorLocationName.BCH_MR_DODDLER_ITEM: has_cardboard_destroyer,
    GatorLocationName.BCH_MR_DODDLER_NPC: has_cardboard_destroyer,
    GatorLocationName.BCH_POT_H8: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.BCH_POT_I6: no_pot_break_item | Has(I.OAR),
    GatorLocationName.BCH_POT_I9_E: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.BCH_POT_I9_W: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.BCH_POT_J6: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.BCH_SAM_ITEM: Has(I.THROWN_PENCIL, count=3),
    GatorLocationName.BCH_SAM_NPC: Has(I.THROWN_PENCIL, count=3),
    GatorLocationName.BCH_SKATE_PUG_ITEM: has_cardboard_destroyer,
    GatorLocationName.BCH_SKATE_PUG_NPCS: has_cardboard_destroyer,
    GatorLocationName.BCH_THROWN_PENCIL_1: None,
    GatorLocationName.BCH_THROWN_PENCIL_2: Has(I.THROWN_PENCIL, count=1),
    GatorLocationName.BCH_THROWN_PENCIL_3: Has(I.THROWN_PENCIL, count=2),
    GatorLocationName.BCH_TONY_ITEM: has_cardboard_destroyer,
    GatorLocationName.BCH_TONY_NPC: has_cardboard_destroyer,
    GatorLocationName.BCH_VIRAJ_NPC: has_cardboard_destroyer,
    GatorLocationName.BI_BILLY_ITEM: None,
    GatorLocationName.BI_BILLY_NPC: None,
    GatorLocationName.BI_BRACELET_MONKEY_ALL_BRACELETS_NPC: None,
    GatorLocationName.BI_ROCK: None,
    GatorLocationName.BI_ZHU_NPC: Has(I.ROCK),
    GatorLocationName.CAN_BROKEN_SCOOTER_BOARD: None,
    GatorLocationName.CAN_CHEST_D8: (has_ranged | Has(I.BRACELET)) & can_open_chests,
    GatorLocationName.CAN_DARCIE_ITEM: has_ranged,
    GatorLocationName.CAN_DARCIE_NPC: has_ranged,
    GatorLocationName.CAN_KASEN_ITEM: Has(I.BROKEN_SCOOTER),
    GatorLocationName.CAN_KASEN_NPC: Has(I.BROKEN_SCOOTER),
    GatorLocationName.CAN_MOCHI_NPC: None,
    GatorLocationName.CAN_POT_A8_N: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.CAN_POT_A8_W: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.CAN_POT_B8: (has_ranged | Has(I.BRACELET, 2)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.CAN_POT_C7: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.CAN_POT_C8_MOCHI: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.CAN_POT_C8_OUTCROP: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.CAN_POT_C9_LOWER: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.CAN_POT_C9_UPPER: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.CAN_POT_D6: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.CAN_POT_D7_N: (has_ranged | HasAny(I.BRACELET, I.GLIDER) | can_shield_jump) & (no_pot_break_item | Has(I.TIGER_FORM)),
    GatorLocationName.CAN_POT_D7_S: (has_ranged
    | HasAny(I.BRACELET, I.GLIDER)
    | can_shield_jump) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.CAN_POT_D8: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GUITAR)),
    GatorLocationName.CAN_RACE_B6: has_shield,
    GatorLocationName.CAN_RACE_C7: has_shield,
    GatorLocationName.CAN_SSUMANTHA_ITEM: has_shield,
    GatorLocationName.CAN_SSUMANTHA_NPC: has_shield,
    GatorLocationName.CRL_BECCA_NPC: Has(I.RETAINER),
    GatorLocationName.CRL_BRACELET_MONKEY_WINDMILL: None,
    GatorLocationName.CRL_CHEST_G6: can_open_chests,
    GatorLocationName.CRL_CHEST_G8: can_open_chests,
    GatorLocationName.CRL_CHEST_H5: (has_ranged | Has(I.BRACELET)) & can_open_chests,
    GatorLocationName.CRL_MADELINE_NPC: None,
    GatorLocationName.CRL_POT_D8: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.CRL_POT_E7_NE: no_pot_break_item | Has(I.OAR),
    GatorLocationName.CRL_POT_E7_NW: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.CRL_POT_E7_SE: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.CRL_POT_E7_SW: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.CRL_POT_F7: no_pot_break_item | Has(I.OAR),
    GatorLocationName.CRL_POT_F9: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.CRL_POT_G5: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.CRL_POT_H5_N: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.CRL_POT_H5_S: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.TIGER_FORM)),
    GatorLocationName.CRL_RETAINER: None,
    GatorLocationName.CRL_ROBIN_ITEM: has_cardboard_destroyer,
    GatorLocationName.CRL_ROBIN_NPC: has_cardboard_destroyer,
    GatorLocationName.FOR_BRACELET_MONKEY_TREE: None,
    GatorLocationName.FOR_CHEST_H4: (has_ranged | Has(I.BRACELET)) & can_open_chests,
    GatorLocationName.FOR_EVA_ITEM: Has(I.BRACELET),
    GatorLocationName.FOR_EVA_NPC: Has(I.BRACELET),
    GatorLocationName.FOR_GUNTHER_NPC: None,
    GatorLocationName.FOR_NINJA_CLAN_ITEM: (has_cardboard_destroyer & Has(I.BRACELET))
    | has_ranged,
    GatorLocationName.FOR_NINJA_CLAN_NPCS: (has_cardboard_destroyer & Has(I.BRACELET))
    | has_ranged,
    GatorLocationName.FOR_PENELOPE_ITEM: can_do_hard_ranged_quests,
    GatorLocationName.FOR_PENELOPE_NPC: can_do_hard_ranged_quests,
    GatorLocationName.FOR_PEPPERONI_ITEM: has_cardboard_destroyer & Has(I.BRACELET),
    GatorLocationName.FOR_PEPPERONI_NPCS: has_cardboard_destroyer & Has(I.BRACELET),
    GatorLocationName.FOR_POT_E1_LOWER_E: no_pot_break_item | Has(I.OAR),
    GatorLocationName.FOR_POT_E1_UPPER_E: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.FOR_POT_E1_UPPER_W: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.FOR_POT_F3: no_pot_break_item | Has(I.OAR),
    GatorLocationName.FOR_POT_G3_CLIFF: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.FOR_POT_G3_POND: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.FOR_POT_G4_DEAD_POND: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.FOR_POT_G4_E_E: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.FOR_POT_G4_E_W: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.FOR_POT_G4_S: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.FOR_POT_H2: no_pot_break_item | Has(I.OAR),
    GatorLocationName.FOR_POT_H4_E: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.FOR_POT_H4_N: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.FOR_POT_H4_S: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GUITAR)),
    GatorLocationName.FOR_POT_J0: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.FOR_POT_J1_SE: no_pot_break_item | Has(I.OAR),
    GatorLocationName.FOR_POT_J1_SW: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.FOR_POT_J3_E: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.FOR_POT_J3_W: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.FOR_POT_KID_NPC: has_cardboard_destroyer,
    GatorLocationName.FOR_RACE_F4: None,
    GatorLocationName.FOR_RACE_G0: has_shield,
    GatorLocationName.FOR_RACE_H1: None,
    GatorLocationName.FOR_ROMEO_NUNCHUCKS: (has_cardboard_destroyer & Has(I.BRACELET))
    | has_ranged,
    GatorLocationName.FOR_SIERRA_ITEM: has_cardboard_destroyer,
    GatorLocationName.FOR_SIERRA_NPC: has_cardboard_destroyer,
    GatorLocationName.FOR_SORIN_ROE_BEERITNEY_ITEM: None,
    GatorLocationName.FOR_SORIN_ROE_BEERITNEY_NPCS: None,
    GatorLocationName.FOR_TIFFANY_ITEM: has_cardboard_destroyer,
    GatorLocationName.FOR_TIFFANY_NPCS: has_cardboard_destroyer,
    GatorLocationName.FOR_TRISH_NPC: None,
    GatorLocationName.J4T_GRABBY_HAND: None,
    GatorLocationName.J4T_PAINT_GUN: None,
    GatorLocationName.J4T_ROY_ALL_PURCHASES_NPC: None,
    GatorLocationName.J4T_STICKY_HAND: None,
    GatorLocationName.J4T_TRAMPOLINE: None,
    GatorLocationName.J4T_TRASH_CAN_LID: None,
    GatorLocationName.J4T_WRENCH: None,
    GatorLocationName.JET_LEELAND_ITEM: has_cardboard_destroyer,
    GatorLocationName.JET_LEELAND_NPC: has_cardboard_destroyer,
    GatorLocationName.JILL_Q_BUG_NET_GIFT: None,
    GatorLocationName.JILL_Q_CHEESE_SANDWICH: has_cardboard_destroyer,
    GatorLocationName.JILL_Q_GENE_ITEM: has_cardboard_destroyer & Has(I.SANDWICH),
    GatorLocationName.JILL_Q_MAGIC_ORE: None,
    GatorLocationName.JILL_Q_NPCS: can_complete_jill,
    GatorLocationName.JILL_Q_SUSANNE: Has(I.ORE) & (has_ranged | has_sword),
    GatorLocationName.MARTIN_Q_BUCKET_GIFT: Has(I.CLIPPINGS) & has_sword,
    GatorLocationName.MARTIN_Q_DUKE_ITEM: None,
    GatorLocationName.MARTIN_Q_GRASSING_CLIPPINGS: has_sword,
    GatorLocationName.MARTIN_Q_JADA_ITEM: can_complete_martin,
    GatorLocationName.MARTIN_Q_LUCAS_ITEM: None,
    GatorLocationName.MARTIN_Q_NPCS: can_complete_martin,
    GatorLocationName.MARTIN_Q_WATER: HasAll(I.CLIPPINGS, I.BUCKET) & has_sword,
    GatorLocationName.MTN_BOWLING_BOMB_GIFT: None,
    GatorLocationName.MTN_BRACELET_MONKEY_MOUNTAIN: None,
    GatorLocationName.MTN_CHEST_B3: can_open_chests,
    GatorLocationName.MTN_CHEST_C5: can_open_chests,
    GatorLocationName.MTN_FLINT_NPC: has_ranged | Has(I.BOMB),
    GatorLocationName.MTN_LUISA_ITEM: None,
    GatorLocationName.MTN_LUISA_NPC: None,
    GatorLocationName.MTN_NEIL_ITEM: has_cardboard_destroyer,
    GatorLocationName.MTN_NEIL_NPC: has_cardboard_destroyer,
    GatorLocationName.MTN_POT_B4_CENTER: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.MTN_POT_B4_E: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.MTN_POT_B4_NE: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GUITAR)),
    GatorLocationName.MTN_POT_B4_W: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.MTN_POT_B5_ROCK: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.MTN_POT_B5_SW: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.MTN_POT_B5_TANNER: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.MTN_POT_C3_CLIFFFACE: (has_ranged | HasAny(I.BRACELET, I.GLIDER)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.MTN_POT_C3_DOWN_FROM_TWIG: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.MTN_POT_C3_RAISED: no_pot_break_item | Has(I.OAR),
    GatorLocationName.MTN_POT_C3_SW: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.MTN_POT_C4_NE: no_pot_break_item | Has(I.OAR),
    GatorLocationName.MTN_POT_C4_NW_TALL: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.MTN_POT_C4_PEAK_E: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.MTN_POT_C4_SW: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GUITAR)),
    GatorLocationName.MTN_POT_C4_W: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.TIGER_FORM)),
    GatorLocationName.MTN_POT_C4_PEAK_W: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.MTN_POT_C5: (has_ranged | Has(I.BRACELET, count=2)) & (no_pot_break_item | Has(I.GUITAR)),
    GatorLocationName.MTN_POT_D3: (has_ranged | HasAny(I.BRACELET, I.GLIDER)) & (no_pot_break_item | Has(I.TIGER_FORM)),
    GatorLocationName.MTN_RACE_C4: Has(I.BRACELET) & has_shield,
    GatorLocationName.MTN_RACE_D5: Has(I.BRACELET),
    GatorLocationName.MTN_SCOOTER_NPC: ((Has(I.BRACELET) & has_cardboard_destroyer)
    | has_ranged) & (no_pot_break_item | HasAll(I.OAR, I.TIGER_FORM, I.SLEEP_MASK, I.GUITAR, I.GIANT_SOCKS)),
    GatorLocationName.MTN_TANNER_NPC: has_cardboard_destroyer & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.MTN_TWIG_NPC: has_shield,
    GatorLocationName.RAV_CHEST_E4: can_open_chests,
    GatorLocationName.RAV_ESTHER_NPC: None,
    GatorLocationName.RAV_POT_E2: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.RAV_POT_E3_BEACH: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.RAV_POT_E3_RIVER: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.RAV_POT_E4: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.RAV_POT_F4: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.TIGER_FORM)),
    GatorLocationName.TI_AVERY: Has(I.STARTER_HAT) & has_cardboard_destroyer,
    GatorLocationName.TI_AVERY_HAT_RECIPE: None,
    GatorLocationName.TI_BRACELET_MONKEY_TUTORIAL: has_cardboard_destroyer,
    GatorLocationName.TI_CHEST_A3: can_open_chests,
    GatorLocationName.TI_CHEST_B1_MID_CLIFF: can_open_chests,
    GatorLocationName.TI_CHEST_B1_TALLEST: Has(I.BRACELET) & can_open_chests,
    GatorLocationName.TI_CHEST_D1: (has_ranged | Has(I.BRACELET) | can_shield_jump) & can_open_chests,
    GatorLocationName.TI_FRANNY_ITEM: has_cardboard_destroyer,
    GatorLocationName.TI_FRANNY_NPC: has_cardboard_destroyer,
    GatorLocationName.TI_GERALD_ITEM: has_cardboard_destroyer,
    GatorLocationName.TI_GERALD_NPC: has_cardboard_destroyer,
    GatorLocationName.TI_MARTIN: Has(I.POT_Q),
    GatorLocationName.TI_POT_A1: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_A3_BELOW_E: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_A3_WITHIN_CLIFFS: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.TI_POT_B0_BONE_PATH: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_B0_SW: no_pot_break_item | Has(I.OAR),
    GatorLocationName.TI_POT_B1_MIDDLE_ROPE: no_pot_break_item | Has(I.OAR),
    GatorLocationName.TI_POT_B1_PEAK_N: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.TI_POT_B1_PEAK_S: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.TI_POT_B1_WATERFALL_BELOW: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.TI_POT_B1_WATERFALL_NEXT_TO: no_pot_break_item | Has(I.OAR),
    GatorLocationName.TI_POT_B1_WATERFALL_PILLAR: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_B1_W_ROPE: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.SLEEP_MASK)),
    GatorLocationName.TI_POT_B2_BELOW_E: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_B2_BELOW_MIDDLE: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.TI_POT_B2_BELOW_W: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.TI_POT_B2_NW: no_pot_break_item | Has(I.OAR),
    GatorLocationName.TI_POT_B2_SIMON_E: no_pot_break_item | Has(I.OAR),
    GatorLocationName.TI_POT_B2_TALL: (has_ranged | Has(I.BRACELET)) & (no_pot_break_item | Has(I.OAR)),
    GatorLocationName.TI_POT_C1_HILL: no_pot_break_item | Has(I.SLEEP_MASK),
    GatorLocationName.TI_POT_C1_STICK: no_pot_break_item | Has(I.GUITAR),
    GatorLocationName.TI_POT_C2: (has_ranged | Has(I.BRACELET) | can_shield_jump) & (no_pot_break_item | Has(I.GIANT_SOCKS)),
    GatorLocationName.TI_POT_D0: no_pot_break_item | Has(I.TIGER_FORM),
    GatorLocationName.TI_POT_D1: no_pot_break_item | Has(I.GIANT_SOCKS),
    GatorLocationName.TI_POT_Q: None,
    GatorLocationName.TI_RACE_C2_CLIFF: has_shield,
    GatorLocationName.TI_RACE_C2_MARTIN: has_shield,
    GatorLocationName.TI_SIMON_ITEM: None,
    GatorLocationName.TI_SIMON_NPC: None,
    GatorLocationName.TI_STICK: None,
}


def set_location_rules(world: "GatorWorld") -> None:
    multiworld = world.multiworld
    player = world.player

    for location_data in location_table:
        rule = gator_location_rules[location_data.name]
        if rule is not None:
            location = multiworld.get_location(location_data.name.value, player)
            world.set_rule(location, rule)
