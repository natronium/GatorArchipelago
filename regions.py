from enum import Enum

class GatorRegionName(str, Enum):
    pass

class GatorStartingRegionName(GatorRegionName):
    TUTORIAL_ISLAND = "Tutorial Island"

class GatorSurfaceRegionName(GatorRegionName):
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
    UNDERGROUND = "Underground"
    UNDERGROUND_ENTRANCE = "Underground Entrance"
    UNDERGROUND_ENTRANCE_BREAKABLES = "Underground Entrance Breakables"
    LIGHTHOUSE = "Lighthouse"
    LIGHTHOUSE_BREAKABLES = "Lighthouse Breakables"
    MINES = "Mines"
    MINES_BREAKABLES = "Mines Breakables"
    MINES_RACES = "Mines Races"
    DRIP = "Flowstone Caverns"
    DRIP_BREAKABLES = "Flowstone Caverns Breakables"
    DRIP_RACES = "Flowstone Caverns Races"
    ROOTS = "Big Roots"
    ROOTS_BREAKABLES = "Big Roots Breakables"
    ROOTS_RACES = "Big Roots Races"

