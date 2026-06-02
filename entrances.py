from typing import List, NamedTuple
from rule_builder.rules import Rule
from .rules import can_clear_tutorial, has_cardboard_destroyer, has_ranged, can_race, Has, HasAny
from .items import GatorItemName as I
from .regions import GatorRegionName as R, GatorSurfaceRegionName as SR, GatorITDRegionName as UR

class GatorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule | None

surface_entrances: List[GatorEntrance] = [
    GatorEntrance(SR.TUTORIAL_ISLAND, SR.BIG_ISLAND, can_clear_tutorial),
    GatorEntrance(SR.TUTORIAL_ISLAND, SR.TUTORIAL_ISLAND_RACES, can_race),
    GatorEntrance(SR.TUTORIAL_ISLAND, SR.TUTORIAL_ISLAND_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(SR.TUTORIAL_ISLAND, SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, has_ranged),
    GatorEntrance(SR.BIG_ISLAND, SR.BIG_ISLAND_RACES, can_race),
    GatorEntrance(SR.BIG_ISLAND, SR.BIG_ISLAND_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(SR.BIG_ISLAND, SR.BIG_ISLAND_BRACELET_SHOPS, has_cardboard_destroyer & Has(I.BRACELET)),
    GatorEntrance(SR.BIG_ISLAND, SR.JUNK_4_TRASH, has_cardboard_destroyer),
    GatorEntrance(SR.BIG_ISLAND, SR.PLAYGROUND, None),
    GatorEntrance(SR.BIG_ISLAND, SR.MOUNTAIN, HasAny(I.GLIDER, I.BRACELET)),
    GatorEntrance(SR.MOUNTAIN, SR.MOUNTAIN_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(SR.MOUNTAIN_BREAKABLES, SR.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, None),
]

underground_entrances: List[GatorEntrance] = [
    GatorEntrance(SR.TUTORIAL_ISLAND, UR.UNDERGROUND_ENTRANCE, can_clear_tutorial) # TODO: include DLC option
]

entrances = surface_entrances + underground_entrances