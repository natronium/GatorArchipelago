import settings
import typing
from typing import Dict, Any, List
from .options import GatorOptions  # the options we defined earlier
from .items import item_name_to_id, item_table  # data used below to add items to the World
from .locations import location_name_to_id, location_table  # same as above
from .regions import gator_regions
from .rules import set_location_rules, set_region_rules
from .presets import options_presets
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Location, Entrance, Item, ItemClassification


class GatorItem(Item):
    game: str = "Lil Gator Game"


class GatorLocation(Location):
    game: str = "Lil Gator Game"


# class GatorSettings(settings.Group):
#     """Not sure what goes here?"""

class GatorWorld(World):
    """Embark on an adorable adventure, discover new friends and uncover everything the island has to offer. Climb,
    Swim, Glide and slide your way into the hearts of the many different characters you meet on your travels!"""
    game = "Lil Gator Game"  # name of the game/world
    options_dataclass = GatorOptions  # options the player can set
    options: GatorOptions  # typing hints for option results
    # settings: typing.ClassVar[GatorSettings]  # will be automatically assigned from type hint
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

        for location_name, location_id in self.location_name_to_id.items():
            region = self.multiworld.get_region(location_table[location_name].region, self.player)
            location = GatorLocation(self.player, location_name, location_id, region)
            region.locations.append(location)

    def create_item(self, name: str) -> GatorItem:
        item_data = item_table[name]
        return GatorItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        gator_items: List[GatorItem] = []
        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        ## Need to handle: starting inventory? adding extra filler items to match location count

        for item, quantity in items_to_create.items():
            for i in range(0, quantity):
                gator_item: GatorItem = self.create_item(item)
                gator_items.append(gator_item)

        self.multiworld.itempool += gator_items

    def set_rules(self) -> None:
        set_region_rules(self)
        set_location_rules(self)

    def fill_slot_data(self) -> Dict[str, Any]:
        # In order for our game client to handle the generated seed correctly we need to know what the user selected
        # for whether they should have access to Freeplay immediately.
        # A dictionary returned from this method gets set as the slot_data and will be sent to the client after connecting.
        # The options dataclass has a method to return a `Dict[str, Any]` of each option name provided and the relevant
        # option's value.
        return self.options.as_dict("start_with_freeplay", "require_shield_jump")

class GatorWeb(WebWorld):
    options_presets = options_presets
    ## location_descriptions
    ## item_descriptions