from enum import Enum

class GatorRegionName(str, Enum):
    pass

class GatorSurfaceRegionName(GatorRegionName):
    TUTORIAL_ISLAND = "Tutorial Island"
    PLAYGROUND = "Playground"
    POTS_SHOOTABLE_FROM_TUTORIAL_ISLAND = "Pots Shootable from Tutorial Island"
    TUTORIAL_ISLAND_RACES = "Tutorial Island Races"
    TUTORIAL_ISLAND_BREAKABLES = "Tutorial Island Breakables"
    BIG_ISLAND = "Big Island"
    BIG_ISLAND_RACES = "Big Island Races"
    BIG_ISLAND_BREAKABLES = "Big Island Breakables"
    MOUNTAIN = "Mountain"
    MOUNTAIN_BREAKABLES = "Mountain Breakables"
    JUNK_4_TRASH = "Junk 4 Trash"
    BIG_ISLAND_BRACELET_SHOPS = "Big Island Bracelet Shops"

class GatorITDRegionName(GatorRegionName):
    UNDERGROUND_ENTRANCE = "Underground Entrance"
    MINES = "Mines"
    MINES_BREAKABLES = "Mines Breakables"
    DRIP = "Flowstone Caverns"
    DRIP_BREAKABLES = "Flowstone Caverns Breakables"
    ROOTS = "Big Roots"
    ROOTS_BREAKABLES = "Big Roots Breakables"
    # TODO: split up regions more?

