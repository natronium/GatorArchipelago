import settings
import typing
from .options import GatorOptions  # the options we defined earlier
from .items import item_name_to_id  # data used below to add items to the World
from .locations import location_name_to_id  # same as above
from .regions import gator_regions
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, RegionType, ItemClassification

class GatorItem(Item):
    game: str = "Lil Gator Game"

class GatorLocation(Location):
    game: str = "Lil Gator Game"

class GatorSettings(settings.Group):
    """Not sure what goes here?"""

class GatorWorld(World):
    """Insert description of the world/game here."""
    game = "Lil Gator Game"  # name of the game/world
    options_dataclass = GatorOptions  # options the player can set
    options: GatorOptions  # typing hints for option results
    settings: typing.ClassVar[GatorSettings]  # will be automatically assigned from type hint
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id


def create_regions(self) -> None:
    for region_name in gator_regions:
        region = Region(region_name, self.player, self.multiworld)
        self.multiworld.regions.append(region)

    for region_name, exits in gator_regions.items():
        region = self.multiworld.get_region(region_name, self.player)
        region.add_exits(exits)