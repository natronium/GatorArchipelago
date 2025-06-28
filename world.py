from typing import ClassVar, Dict, Any, List

try:
    from rule_builder import RuleWorldMixin
except ModuleNotFoundError:
    from .rule_builder import RuleWorldMixin
from .options import GatorOptions, gator_options_presets, gator_option_groups
from .items import item_name_to_id, item_table, item_name_groups, GatorItemName as I, GatorEventName as E
from .locations import location_name_to_id, location_table, location_name_groups, GatorEventLocationName as EL
from .regions import GatorRegionName as R
from .entrances import gator_entrances
from .rules import Has, set_location_rules
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from .tracker import tracker_world

gator_version = 102


class GatorItem(Item):
    game: str = "Lil Gator Game"

class GatorLocation(Location):
    game: str = "Lil Gator Game"

class GatorWeb(WebWorld):
    theme = "jungle"
    game = "Lil Gator Game"
    option_groups = gator_option_groups
    options_presets = gator_options_presets

    # tutorials = [
    #     Tutorial(
    #         tutorial_name="Multiworld Setup Guide",
    #         description="A guide to setting up the Lil Gator Game Randomizer for Archipelago multiworld games.",
    #         language="English",
    #         file_name="setup_en.md",
    #         link="setup/en",
    #         authors=[""]
    #     )
    # ]


class GatorWorld(RuleWorldMixin, World):
    """Embark on an adorable adventure, discover new friends and uncover everything the island has to offer. Climb,
    Swim, Glide and slide your way into the hearts of the many different characters you meet on your travels!
    """

    game = "Lil Gator Game"  # name of the game/world
    web = GatorWeb()
    options_dataclass = GatorOptions  # options the player can set
    options: GatorOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups


    #  UT Integration
    tracker_world: ClassVar[dict[str, Any]] = tracker_world
    ut_can_gen_without_yaml: ClassVar[bool] = True
    glitches_item_name: ClassVar[str] = E.OOL.value

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:

        # Adapted from ClassicSpeed's SADX implementation of this feature
        if "ModVersion" in slot_data and slot_data["ModVersion"] != gator_version:
            current_version = f"v{gator_version // 100}.{(gator_version // 10) % 10}.{gator_version % 10}"
            slot_version = f"v{slot_data['ModVersion'] // 100}.{(slot_data['ModVersion'] // 10) % 10}.{slot_data['ModVersion'] % 10}"

            raise Exception(
                f"Lil Gator Game version error: The version of apworld used to generate this world ({slot_version}) does not match the version of your installed apworld ({current_version}).")
        return slot_data

    ### Consider: having events for each playground construction

    def create_regions(self) -> None:
        for gator_region in R:
            region = Region(gator_region.value, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        for gator_entrance in gator_entrances:
            start_region = self.multiworld.get_region(gator_entrance.starting_region.value, self.player)
            end_region = self.multiworld.get_region(gator_entrance.ending_region.value, self.player)
            self.create_entrance(start_region, end_region, gator_entrance.rule)

        for location_data in location_table:
            region = self.multiworld.get_region(
                location_data.region.value, self.player
            )
            location = GatorLocation(self.player, location_data.name.value, location_data.location_id, region)
            region.locations.append(location)

        # Currently, only goal is complete the playground
        victory_region = self.multiworld.get_region(R.PLAYGROUND.value, self.player)
        victory_location = GatorLocation(
            self.player, EL.PLAYGROUND.value, None, victory_region
        )
        victory_region.locations.append(victory_location)
        victory_location.place_locked_item(self.create_item(E.PLAYGROUND.value))

    def create_item(self, name: str) -> GatorItem:
        # if the name provided is an event, create it as an event
        if name in [member.value for member in E]:
            return GatorItem(name, ItemClassification.progression, None, self.player)
        
        # otherwise, look up the item data
        item_data = next(data for data in item_table if data.name.value == name)
        return GatorItem(
            name, item_data.classification, self.item_name_to_id[name], self.player
        )

    def create_items(self) -> None:
        gator_items: List[GatorItem] = []
        items_to_create: Dict[str, int] = {
            data.name.value: data.base_quantity_in_item_pool for data in item_table
        }

        # If start with checkfinders on, add them into the start inventory, otherwise add them to the itempool
        if self.options.start_with_checkfinders:
            self.multiworld.push_precollected(self.create_item(I.MEGAPHONE.value))
            self.multiworld.push_precollected(self.create_item(I.TEXTING.value))
        else:
            items_to_create[I.MEGAPHONE.value] = 1
            items_to_create[I.TEXTING.value] = 1
        
        if self.options.lock_pots_behind_items:
            items_to_create[I.OAR.value] = 1
            items_to_create[I.TIGER_FORM.value] = 1
            items_to_create[I.GIANT_SOCKS.value] = 1
            items_to_create[I.SLEEP_MASK.value] = 1
            items_to_create[I.GUITAR.value] = 1
        
        if self.options.lock_chests_behind_key:
            items_to_create[I.KEY.value] = 1
        
        if self.options.lock_races_behind_flag:
            items_to_create[I.FINISH_FLAG.value] = 1
        

        for item, quantity in items_to_create.items():
            for i in range(0, quantity):
                gator_item: GatorItem = self.create_item(item)
                gator_items.append(gator_item)

        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(
            gator_items
        )
        gator_items += [
            self.create_item(self.get_filler_item_name()) for _ in range(junk)
        ]

        self.multiworld.itempool += gator_items

    def set_rules(self) -> None:
        set_location_rules(self)

        self.set_completion_rule(Has(E.PLAYGROUND))

    def fill_slot_data(self) -> Dict[str, Any]:
        # In order for our game client to handle the generated seed correctly we need to know what the user selected
        # for whether they should have access to Freeplay immediately.
        # A dictionary returned from this method gets set as the slot_data and will be sent to the client after connecting.
        # The options dataclass has a method to return a `Dict[str, Any]` of each option name provided and the relevant
        # option's value.
        slot_data = self.options.as_dict(
            "start_with_freeplay", "require_shield_jump", "harder_ranged_quests", "lock_pots_behind_items", "lock_chests_behind_key", "lock_races_behind_flag"
        )
        slot_data["ModVersion"] = gator_version
        return slot_data

    def get_filler_item_name(self) -> str:
        return self.random.choice([I.CRAFT_15.value, I.CRAFT_30.value])
