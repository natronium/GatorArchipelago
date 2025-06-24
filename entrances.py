from typing import List, NamedTuple
from rule_builder import Rule
from .rules import can_clear_tutorial, has_cardboard_destroyer, has_ranged, can_complete_game, Has, HasAny
from .items import GatorItemName as I
from .regions import GatorRegionName as R

class GatorEntrance(NamedTuple):
    starting_region: R
    ending_region: R
    rule: Rule | None

gator_entrances: List[GatorEntrance] = [
    GatorEntrance(R.MENU, R.TUTORIAL_ISLAND, None),
    GatorEntrance(R.TUTORIAL_ISLAND, R.BIG_ISLAND, can_clear_tutorial),
    GatorEntrance(R.TUTORIAL_ISLAND, R.TUTORIAL_ISLAND_RACES, None),
    GatorEntrance(R.TUTORIAL_ISLAND, R.TUTORIAL_ISLAND_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(R.TUTORIAL_ISLAND, R.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, has_ranged),
    GatorEntrance(R.BIG_ISLAND, R.BIG_ISLAND_RACES, None),
    GatorEntrance(R.BIG_ISLAND, R.BIG_ISLAND_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(R.BIG_ISLAND, R.BIG_ISLAND_BRACELET_SHOPS, has_cardboard_destroyer & Has(I.BRACELET)),
    GatorEntrance(R.BIG_ISLAND, R.JUNK_4_TRASH, has_cardboard_destroyer),
    GatorEntrance(R.BIG_ISLAND, R.PLAYGROUND, can_complete_game),
    GatorEntrance(R.BIG_ISLAND, R.MOUNTAIN, HasAny(I.GLIDER, I.BRACELET)),
    GatorEntrance(R.MOUNTAIN, R.MOUNTAIN_BREAKABLES, has_cardboard_destroyer),
    GatorEntrance(R.MOUNTAIN_BREAKABLES, R.POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND, None),
]