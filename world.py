from logging import warning
import math
from typing import ClassVar, Dict, Any, List
from typing_extensions import override

from Options import Option

# from rule_builder.rules import RuleWorldMixin
from .options import (
    GatorOptions,
    Goal,
    ItemsIncluded,
    LocationsIncluded,
    TrapTypeWeights,
    gator_options_presets,
    gator_option_groups,
)
from .items import (
    item_name_to_id,
    item_table,
    surface_goal_item_table,
    surface_goal_or_location_table,
    surface_items_for_location_table,
    surface_item_table,
    underground_items_for_goal_and_loc_table,
    underground_items_for_locations_table,
    underground_item_table,
    item_name_groups,
    GatorItemName as I,
    GatorEventName as E,
)
from .locations import (
    location_name_to_id,
    surface_location_table,
    underground_location_table,
    location_name_groups,
    GatorEventLocationName as EL,
)
from .regions import (
    GatorStartingRegionName as StR,
    GatorSurfaceRegionName as SR,
    GatorITDRegionName as UR,
)
from .entrances import surface_entrances, underground_entrances
from .rules import (
    Has,
    HasAll,
    HasAny,
    set_location_rules,
    can_complete_main_game,
    can_complete_itd,
)
from worlds.AutoWorld import World, WebWorld
from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from .tracker import tracker_world
from .json_generator import generate_rule_json


class GatorItem(Item):
    game: str = "Lil Gator Game"


class GatorLocation(Location):
    game: str = "Lil Gator Game"


class GatorWeb(WebWorld):
    theme = "jungle"
    game = "Lil Gator Game"
    option_groups = gator_option_groups
    options_presets = gator_options_presets

    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the Lil Gator Game Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["rose.as.romeo", "Natronium"],
        )
    ]
    game_info_languages = ["en"]


class GatorWorld(World):
    """Embark on an adorable adventure, discover new friends and uncover everything the island has to offer. Climb,
    Swim, Glide and slide your way into the hearts of the many different characters you meet on your travels!
    """

    game = "Lil Gator Game"  # name of the game/world
    web = GatorWeb()
    options_dataclass = GatorOptions  # options the player can set
    options: GatorOptions  # typing hints for option results
    topology_present = True  # show path to required location checks in spoiler
    origin_region_name = StR.TUTORIAL_ISLAND.value

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
        if "APWorldVersion" in slot_data:
            if (
                slot_data["APWorldVersion"][0] != GatorWorld.world_version.major
                or slot_data["APWorldVersion"][1] != GatorWorld.world_version.minor
            ):
                current_version = f"v{GatorWorld.world_version.as_simple_string}"
                reported_version = f"v{slot_data['APWorldVersion']}"

                raise Exception(
                    f"Lil Gator Game version error: The version of apworld used to generate this world ({reported_version}) does not match the version of your installed apworld ({current_version})."
                )
        return slot_data

    @override
    def generate_early(self) -> None:
        if (
            self.options.locations_included
            == LocationsIncluded.option_in_the_dark_locations_only
        ):
            # If only ITD locations are included, force freeplay on, since Tutorial Island may not be completable under these conditions
            self.options.start_with_freeplay.value = True
            warning(f"Lil Gator game player {self.player_name} only has DLC locations included, so freeplay is forced on")
        re_gen_passthrough = getattr(self.multiworld, "re_gen_passthrough", {})
        if re_gen_passthrough and self.game in re_gen_passthrough:
            # Get the passed through slot data from the real generation
            slot_data: dict[str, Any] = re_gen_passthrough[self.game]

            # Set all your options here instead of getting them from the yaml
            for key, value in slot_data.items():
                opt: Option[Any] | None = getattr(self.options, key, None)
                if opt is not None:
                    # You can also set .value directly but that won't work if you have OptionSets
                    setattr(self.options, key, opt.from_any(value))
            setattr(self.options, "locations_included", True) # if in UT, make all locations regardless

    ### Consider: having events for each playground construction

    def create_regions(self) -> None:
        # Always create the starting region
        region = Region(StR.TUTORIAL_ISLAND.value, self.player, self.multiworld)
        self.multiworld.regions.append(region)

        if (
            self.options.locations_included
            != LocationsIncluded.option_in_the_dark_locations_only
            or self.options.goal != Goal.option_in_the_dark_story_only
        ):
            # Include surface regions and entrances if goal or locations includes the main story
            for surface_region in SR:
                region = Region(surface_region.value, self.player, self.multiworld)
                self.multiworld.regions.append(region)
            for gator_entrance in surface_entrances:
                start_region = self.multiworld.get_region(
                    gator_entrance.starting_region.value, self.player
                )
                end_region = self.multiworld.get_region(
                    gator_entrance.ending_region.value, self.player
                )
                self.create_entrance(start_region, end_region, gator_entrance.rule)

        if (
            self.options.locations_included
            != LocationsIncluded.option_in_the_dark_locations_only
        ):
            # Surface locations are included as long as the yaml does not only include ITD locations
            for location_data in surface_location_table:
                region = self.multiworld.get_region(
                    location_data.region.value, self.player
                )
                location = GatorLocation(
                    self.player,
                    location_data.name.value,
                    location_data.location_id,
                    region,
                )
                region.locations.append(location)

        if (
            self.options.locations_included
            != LocationsIncluded.option_main_locations_only
            or self.options.goal != Goal.option_main_story_only
        ):
            # Include ITD regions and entrances if goal or locations includes ITD
            for itd_region in UR:
                region = Region(itd_region.value, self.player, self.multiworld)
                self.multiworld.regions.append(region)

            for gator_entrance in underground_entrances:
                start_region = self.multiworld.get_region(
                    gator_entrance.starting_region.value, self.player
                )
                end_region = self.multiworld.get_region(
                    gator_entrance.ending_region.value, self.player
                )
                self.create_entrance(start_region, end_region, gator_entrance.rule)

        if (
            self.options.locations_included
            != LocationsIncluded.option_main_locations_only
        ):
            # ITD locations are included as long as the yaml does not only include surface locations
            for location_data in underground_location_table:
                region = self.multiworld.get_region(
                    location_data.region.value, self.player
                )
                location = GatorLocation(
                    self.player,
                    location_data.name.value,
                    location_data.location_id,
                    region,
                )
                region.locations.append(location)

        # Set up goal events:
        if self.options.goal != Goal.option_in_the_dark_story_only:
            # Place Playground Complete Event
            playground_region = self.multiworld.get_region(
                SR.PLAYGROUND.value, self.player
            )
            playground_location = GatorLocation(
                self.player, EL.PLAYGROUND.value, None, playground_region
            )
            playground_region.locations.append(playground_location)
            self.set_rule(playground_location, can_complete_main_game)
            playground_location.place_locked_item(self.create_item(E.PLAYGROUND.value))
        if self.options.goal != Goal.option_main_story_only:
            # Place Underground Complete Event
            darklord_region = self.multiworld.get_region(
                UR.LIGHTHOUSE.value, self.player
            )
            darklord_location = GatorLocation(
                self.player, EL.DARKLORD.value, None, darklord_region
            )
            darklord_region.locations.append(darklord_location)
            self.set_rule(darklord_location, can_complete_itd)
            darklord_location.place_locked_item(self.create_item(E.DARKLORD.value))

    def create_item(self, name: str) -> GatorItem:
        # if the name provided is an event, create it as an event
        if name in [member.value for member in E]:
            return GatorItem(name, ItemClassification.progression, None, self.player)

        # otherwise, look up the item data
        item_data = next(data for data in item_table if data.name.value == name)
        if not self.options.awkward_progression and item_data.name in [
            I.BALLOON,
            I.BUBBLEGUM,
            I.RAGDOLL,
            I.STICKY_HAND,
            I.FIREWORK,
        ]:
            return GatorItem(
                name,
                ItemClassification.useful,
                self.item_name_to_id[name],
                self.player,
            )
        else:
            return GatorItem(
                name, item_data.classification, self.item_name_to_id[name], self.player
            )

    def create_items(self) -> None:
        def choose_trap(trap_weights: TrapTypeWeights) -> str:
            trap_weights_sum = sum(trap_weights.values())
            return self.random.choices(
                list(k for k in trap_weights.keys()),
                list((w / trap_weights_sum) for w in trap_weights.values()),
            )[0]

        gator_items: list[GatorItem] = []
        items_to_create: dict[str, int] = {}
        queued_filler: dict[str, int] = {}

        # starting itempools based on DLC related options
        if self.options.items_included != ItemsIncluded.option_in_the_dark_items_only:
            # Both or Main only
            for data in surface_item_table:
                if data.classification != ItemClassification.filler:
                    # hold off on adding filler in case of worst case option settings
                    items_to_create[data.name.value] = data.base_quantity_in_item_pool
                else:
                    queued_filler[data.name.value] = data.base_quantity_in_item_pool
        if self.options.items_included != ItemsIncluded.option_main_items_only:
            # Both or DLC only
            for data in underground_item_table:
                if data.classification != ItemClassification.filler:
                    # hold off on adding filler in case of worst case option settings
                    items_to_create[data.name.value] = data.base_quantity_in_item_pool
                else:
                    queued_filler[data.name.value] = data.base_quantity_in_item_pool
        if self.options.items_included == ItemsIncluded.option_in_the_dark_items_only:
            # include bracelets and/or glider based on options if only ITD items included
            if self.options.include_bracelets:
                items_to_create[I.BRACELET] = 4
            elif self.options.require_vertical_for_itd:
                items_to_create[I.BRACELET] = 1
            if self.options.include_glider:
                items_to_create[I.GLIDER] = 1

        # Include friends only if surface goal is on
        if self.options.goal != Goal.option_in_the_dark_story_only:
            # Both, Either, or Main only
            for data in surface_goal_item_table:
                items_to_create[data.name.value] = data.base_quantity_in_item_pool
        
        # Include ITD friends only if ITD goal is on or ITD locations are included (since the friends in ITD lock locations)
        if self.options.goal != Goal.option_main_story_only or self.options.locations_included != LocationsIncluded.option_main_locations_only:
            # Both, Either, or ITD only
            for data in underground_items_for_goal_and_loc_table:
                items_to_create[data.name.value] = data.base_quantity_in_item_pool

        # include items needed for surface goal or locations if main story items on, main story goal is on, or surface locations are on
        if (
            self.options.items_included != ItemsIncluded.option_in_the_dark_items_only
            or self.options.goal != Goal.option_in_the_dark_story_only
            or self.options.locations_included
            != LocationsIncluded.option_in_the_dark_locations_only
        ):
            for data in surface_goal_or_location_table:
                items_to_create[data.name.value] = data.base_quantity_in_item_pool

        # include items needed for surface quests if surface locations on or surface items on
        if (
            self.options.items_included != ItemsIncluded.option_in_the_dark_items_only
            or self.options.locations_included
            != LocationsIncluded.option_in_the_dark_locations_only
        ):
            for data in surface_items_for_location_table:
                items_to_create[data.name.value] = data.base_quantity_in_item_pool

        # include items needed for In the Dark quests if ITD locations on or ITD items on
        if (
            self.options.items_included != ItemsIncluded.option_main_items_only
            or self.options.locations_included
            != LocationsIncluded.option_main_locations_only
        ):
            for data in underground_items_for_locations_table:
                items_to_create[data.name.value] = data.base_quantity_in_item_pool
            if ItemsIncluded.option_main_items_only:
                # Add random stone break tool if DLC items in general not included
                stone_break: I = self.random.choice(
                    [I.PICKAXE, I.GIANT_CLUB, I.VIKING_HORNS, I.BONEHEAD]
                )
                items_to_create[stone_break.value] = 1
                if stone_break == I.VIKING_HORNS or stone_break == I.BONEHEAD:
                    # these two stone break tools need a source of ragdoll
                    if self.options.awkward_progression:
                        ragdoll: I = self.random.choice(
                            [
                                I.FIREWORK,
                                I.RAGDOLL,
                                I.BALLOON,
                                I.BUBBLEGUM,
                                I.SPIDER_WEB,
                                I.STICKY_HAND,
                            ]
                        )
                    else:
                        ragdoll = I.SPIDER_WEB
                    items_to_create[ragdoll.value] = 1
                    if ragdoll == I.SPIDER_WEB or ragdoll == I.FIREWORK:
                        # Spider web and firework need charm bracelet
                        items_to_create[I.CHARM_KEYCHAIN.value] = 1

        # If start with checkfinders on, add them into the start inventory, otherwise add them to the itempool
        if self.options.start_with_checkfinders:
            self.multiworld.push_precollected(self.create_item(I.MEGAPHONE.value))
            self.multiworld.push_precollected(self.create_item(I.TEXTING.value))
        else:
            items_to_create[I.MEGAPHONE.value] = 1
            items_to_create[I.TEXTING.value] = 1

        # Pots
        if self.options.lock_pots_behind_items:
            items_to_create[I.OAR.value] = 1
            items_to_create[I.TIGER_FORM.value] = 1
            if (
                self.options.locations_included
                != LocationsIncluded.option_in_the_dark_locations_only
            ):
                # DLC has no pots for this category, so only create this item if the surface has locations
                items_to_create[I.GIANT_SOCKS.value] = 1
            items_to_create[I.SLEEP_MASK.value] = 1
            items_to_create[I.GUITAR.value] = 1

        # Chests
        if self.options.lock_chests_behind_key:
            items_to_create[I.KEY.value] = 1

        # Races
        if self.options.lock_races_behind_flag:
            items_to_create[I.FINISH_FLAG.value] = 1

        # Make all the required items
        for item, quantity in items_to_create.items():
            for _ in range(0, quantity):
                gator_item: GatorItem = self.create_item(item)
                gator_items.append(gator_item)

        # Figure out how much room there is for filler and traps
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(
            gator_items
        )
        if (junk < 0):
            # if player has set up worst case scenario for too many items (which is all items, only DLC locations, but main story goal enabled)
            # remove 1x friend items and replace with 4x friend items
            friend_1: list[GatorItem] = []
            for item in gator_items:
                if item.name == I.FRIEND_1:
                    friend_1.append(item)
            
            for _ in range (0, math.ceil((-1* junk) / 4) + 2):
                if (len(friend_1) >= 4):
                    gator_items.remove(friend_1.pop())
                    gator_items.remove(friend_1.pop())
                    gator_items.remove(friend_1.pop())
                    gator_items.remove(friend_1.pop())
                    gator_items.append(self.create_item(I.FRIEND_4.value))
        
        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(
            gator_items
        )
        if (junk < 0):
            # should only occur with plando shenanigans
            friend_2: list[GatorItem] = []
            for item in gator_items:
                if item.name == I.FRIEND_2:
                    friend_2.append(item)
            
            for _ in range (0, math.ceil((-1* junk) / 2) + 2):
                if (len(friend_2) >= 2):
                    gator_items.remove(friend_2.pop())
                    gator_items.remove(friend_2.pop())
                    gator_items.append(self.create_item(I.FRIEND_4.value))

        junk = len(self.multiworld.get_unfilled_locations(self.player)) - len(
            gator_items
        )
        if (junk < 0):
            junk = 0
            warning(f"Lil Gator game player {self.player_name} has too many items for their included locations, likely due to plando or other choices")

        # Add traps
        trap_weights = self.options.trap_type_weights
        trap_chance = self.options.trap_chance / 100
        trap_number = self.random.binomialvariate(junk, trap_chance)
        gator_items += [
            self.create_item(choose_trap(trap_weights)) for _ in range(trap_number)
        ]

        # Add filler
        gator_items += [
            self.create_item(self.get_filler_item_name())
            for _ in range(junk - trap_number)
        ]

        self.multiworld.itempool += gator_items

    def set_rules(self) -> None:
        set_location_rules(self)

        if self.options.goal == Goal.option_main_story_only:
            self.set_completion_rule(Has(E.PLAYGROUND))
        elif self.options.goal == Goal.option_in_the_dark_story_only:
            self.set_completion_rule(Has(E.DARKLORD))
        elif self.options.goal == Goal.option_both_stories:
            self.set_completion_rule(HasAll(E.PLAYGROUND, E.DARKLORD))
        else:
            # Either condition
            self.set_completion_rule(HasAny(E.PLAYGROUND, E.DARKLORD))

        generate_rule_json()

    def fill_slot_data(self) -> Dict[str, Any]:
        # In order for our game client to handle the generated seed correctly we need to know what the user selected
        # for whether they should have access to Freeplay immediately.
        # A dictionary returned from this method gets set as the slot_data and will be sent to the client after connecting.
        # The options dataclass has a method to return a `Dict[str, Any]` of each option name provided and the relevant
        # option's value.
        slot_data = self.options.as_dict(
            "goal",
            "start_with_freeplay",
            "require_vertical_for_itd",
            "require_shield_flip",
            "harder_ranged_quests",
            "lock_pots_behind_items",
            "lock_chests_behind_key",
            "lock_races_behind_flag",
            "awkward_progression",
        )
        slot_data["APWorldVersion"] = self.world_version
        slot_data["DLCIncluded"] = (
            1
            if (
                self.options.goal > 0
                or self.options.items_included > 0
                or self.options.locations_included > 0
            )
            else 0
        )  # if any of the DLC options are set, this value should be 1 so that the mod can reject connecting if DLC is not installed
        return slot_data

    def get_filler_item_name(self) -> str:
        return self.random.choice([I.CRAFT_15.value, I.CRAFT_30.value])
