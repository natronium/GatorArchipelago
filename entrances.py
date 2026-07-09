from typing import List, NamedTuple
from rule_builder.rules import Rule
from .rules import (
    can_spin_jump,
    ug_require_vertical,
    can_access_mountain,
    can_clear_tutorial,
    has_cardboard_destroyer,
    has_ranged,
    can_race,
    Has,
    HasAny,
)
from .items import GatorItemName as I
from .regions import (
    GatorRegionName as R,
    GatorStartingRegionName as StR,
    GatorSurfaceRegionName as SR,
    GatorITDRegionName as UR,
)


class GatorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule | None

surface_entrances: List[GatorEntrance] = [
    GatorEntrance(StR.TUTORIAL_ISLAND, SR.BIG_ISLAND, can_clear_tutorial),
    GatorEntrance(StR.TUTORIAL_ISLAND, SR.TUTORIAL_ISLAND_RACES, can_race),
    GatorEntrance(
        StR.TUTORIAL_ISLAND, SR.TUTORIAL_ISLAND_BREAKABLES, has_cardboard_destroyer
    ),
    GatorEntrance(
        StR.TUTORIAL_ISLAND, SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, has_ranged
    ),
    GatorEntrance(SR.BIG_ISLAND, SR.BIG_ISLAND_RACES, can_race),
    GatorEntrance(SR.BIG_ISLAND, SR.BIG_ISLAND_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(
        SR.BIG_ISLAND,
        SR.BIG_ISLAND_BRACELET_SHOPS,
        has_cardboard_destroyer & (Has(I.BRACELET) | can_spin_jump(1)),
    ),
    GatorEntrance(SR.BIG_ISLAND, SR.JUNK_4_TRASH, has_cardboard_destroyer),
    GatorEntrance(SR.BIG_ISLAND, SR.PLAYGROUND, None),
    GatorEntrance(SR.BIG_ISLAND, SR.MOUNTAIN, can_access_mountain),
    GatorEntrance(SR.MOUNTAIN, SR.MOUNTAIN_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(SR.MOUNTAIN_BREAKABLES, SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, None),
]

underground_entrances: List[GatorEntrance] = [
    GatorEntrance(
        StR.TUTORIAL_ISLAND, UR.UNDERGROUND_ENTRANCE, can_clear_tutorial
    ),
    GatorEntrance(
        UR.UNDERGROUND_ENTRANCE,
        UR.UNDERGROUND_ENTRANCE_BREAKABLES,
        has_cardboard_destroyer,
    ),
    GatorEntrance(UR.UNDERGROUND_ENTRANCE, UR.UNDERGROUND, ug_require_vertical),
    GatorEntrance(UR.UNDERGROUND_ENTRANCE, UR.LIGHTHOUSE, ug_require_vertical),
    GatorEntrance(UR.LIGHTHOUSE, UR.LIGHTHOUSE_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(UR.UNDERGROUND_ENTRANCE, UR.MINES, ug_require_vertical),
    GatorEntrance(UR.MINES, UR.MINES_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(UR.MINES, UR.MINES_RACES, can_race),
    GatorEntrance(UR.UNDERGROUND_ENTRANCE, UR.ROOTS, ug_require_vertical),
    GatorEntrance(UR.ROOTS, UR.ROOTS_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(UR.ROOTS, UR.ROOTS_RACES, can_race),
    GatorEntrance(UR.UNDERGROUND_ENTRANCE, UR.DRIP, ug_require_vertical),
    GatorEntrance(UR.DRIP, UR.DRIP_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(UR.DRIP, UR.DRIP_RACES, can_race),
]

entrances = surface_entrances + underground_entrances
