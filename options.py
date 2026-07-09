from dataclasses import dataclass
from typing import Any

from schema import And, Schema

from Options import (
    DefaultOnToggle,
    OptionDict,
    Range,
    Toggle,
    StartInventoryPool,
    PerGameCommonOptions,
    OptionGroup,
    Choice,
)

class Goal(Choice):
    """Choose whether your goal is to complete the main story, the In the Dark story, both, or either one. If you choose anything other than main story only, you must own and have installed the DLC to be able to connect to your slot."""

    internal_name = "goal"
    display_name = "Goal"

    option_main_story_only = 0
    option_in_the_dark_story_only = 1
    option_both_stories = 2
    option_either = 3
    default = 0


class ItemsIncluded(Choice):
    """Choose which items you want included in your itempool: main game, In the Dark, or both. If you choose In the Dark or both, you must own and have installed the DLC to be able to connect to your slot."""

    internal_name = "items_included"
    display_name = "Items Included"

    option_main_items_only = 0
    option_in_the_dark_items_only = 1
    option_both_items = 2
    default = 0

class LocationsIncluded(Choice):
    """Choose which locations you want included in your slot: main game, In the Dark, or both. If you choose In the Dark or both, you must own and have installed the DLC to be able to connect to your slot."""

    internal_name = "items_included"
    display_name = "Items Included"

    option_main_locations_only = 0
    option_in_the_dark_locations_only = 1
    option_both_locations = 2
    default = 0

class IncludeBraceletsIfITDOnly(Toggle):
    """If playing with only In the Dark items setting on Items Included, then this option being true will include the 4 bracelets in the itempool anyway. Does nothing if main game is included in items."""

    internal_name = "include_bracelets"
    display_name = "Include Bracelets if In the Dark Items Only"

class IncludeGliderIfITDOnly(Toggle):
    """If playing with only In the Dark items setting on Items Included, then this option being true will include the glider in the itempool anyway. Does nothing if main game is included in items."""

    internal_name = "include_glider"
    display_name = "Include Glider if In the Dark Items Only"

class StartWithFreeplay(Toggle):
    """Start with no barrier around Tutorial Island and thus the ability to access checks on the main island. This option will be forced on if only locations from the DLC are included (since Tutorial Island may not be completable under those conditions)."""

    internal_name = "start_with_freeplay"
    display_name = "Start With Freeplay"

class RequireVerticalForITD(DefaultOnToggle):
    """Require bracelet or spin jump for the majority of In the Dark to be in logic. Recommended for folks getting used to the underground layout. If false, the logic will assume that you will try lots of silly jumps and use Reset Position often in the underground. If true, and bracelets are not otherwise included via Items Included or Include Bracelets If ITD Only, then 1 bracelet will be added into the pool."""

    internal_name = "require_vertical_for_itd"
    display_name = "Require Vertical for In the Dark"


class RequireShieldFlip(Toggle):
    """Logic may require you to execute a shield flip (jump, then press shield button) to reach some high places."""

    internal_name = "require_shield_flip"
    display_name = "Require Shield Flip"


class HarderRangedQuests(Toggle):
    """Logic may require you to complete Penelope (Bastion Beaver) and Andromeda (Space Hawk) without a ranged weapon."""

    internal_name = "harder_ranged_quests"
    display_name = "Harder Ranged Quests"


class LockPotsBehindItems(Toggle):
    """Lock pots behind items for each type of pot (each corresponding item unlocks all of that style of pot)."""

    internal_name = "lock_pots_behind_items"
    display_name = "Lock Pots Behind Items"


class LockChestsBehindKey(Toggle):
    """Lock chests behind receiving a key (which unlocks all chests)."""

    internal_name = "lock_chests_behind_key"
    display_name = "Lock Chests Behind Key"


class LockRacesBehindFlag(Toggle):
    """Lock races behind receiving a finish flag (which unlocks all races)."""

    internal_name = "lock_races_behind_flag"
    display_name = "Lock Race Behind Flag"


class StartWithCheckFinders(DefaultOnToggle):
    """Start with Megaphone and Text Jill items in inventory for finding checks."""

    internal_name = "start_with_check_finder"
    display_name = "Start With Check Finders"


class MakeAwkwardItemsProgression(Toggle):
    """Marks Sticky Hand, Balloon, Bubble Gum, Ragdoll, and Firework as progression, which means the generator can make them required for certain checks."""

    internal_name = "awkward_progression"
    display_name = "Make Awkward Items Progression"


# Trap Chance and Trap Type Weights from Ixrec's Outer Wilds implementation
class TrapChance(Range):
    """The probability for each Craft Stuff filler to be replaced with a trap item.
    The exact number of trap items will still be somewhat random, so you can't know
    if you've seen the 'last trap' in your world without checking the spoiler log.
    If you don't want any traps, set this to 0."""

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0


class TrapTypeWeights(OptionDict):
    """When a filler item is replaced with a trap, these weights determine the
    odds for each trap type to be selected.
    If you don't want a specific trap type, set its weight to 0.
    Setting all weights to 0 is the same as setting trap_chance to 0."""

    schema = Schema(
        {
            "Stumble Trap": And(int, lambda n: n >= 0),
            "Dialogue Trap": And(int, lambda n: n >= 0),
            "Float Trap": And(int, lambda n: n >= 0),
            "Sneak Trap": And(int, lambda n: n >= 0),
            "Pixel Trap": And(int, lambda n: n >= 0),
        }
    )
    display_name = "Trap Type Weights"

    default = {
        "Stumble Trap": 2,
        "Dialogue Trap": 2,
        "Float Trap": 1,
        "Sneak Trap": 1,
        "Pixel Trap": 1,
    }

@dataclass
class GatorOptions(PerGameCommonOptions):
    goal: Goal
    items_included: ItemsIncluded
    locations_included: LocationsIncluded
    include_bracelets: IncludeBraceletsIfITDOnly
    include_glider: IncludeGliderIfITDOnly
    start_with_freeplay: StartWithFreeplay
    require_vertical_for_itd: RequireVerticalForITD
    require_shield_flip: RequireShieldFlip
    harder_ranged_quests: HarderRangedQuests
    lock_pots_behind_items: LockPotsBehindItems
    lock_chests_behind_key: LockChestsBehindKey
    lock_races_behind_flag: LockRacesBehindFlag
    start_with_checkfinders: StartWithCheckFinders
    awkward_progression: MakeAwkwardItemsProgression
    start_inventory_from_pool: StartInventoryPool
    trap_chance: TrapChance
    trap_type_weights: TrapTypeWeights


gator_options_presets: dict[str, dict[str, Any]] = {
    # "Maximal Accessibility": {
    #     "start_with_freeplay": True,
    #     "require_shield_flip": False,
    #     "harder_ranged_quests": False,
    #     "lock_pots_behind_items": False,
    #     "lock_chests_behind_key": False,
    #     "lock_races_behind_flag": False,
    #     "start_with_checkfinders": True,
    #     "awkward_progression": False,
    # },
    # "Locked Down": {
    #     "start_with_freeplay": False,
    #     "require_shield_flip": False,
    #     "harder_ranged_quests": False,
    #     "lock_pots_behind_items": True,
    #     "lock_chests_behind_key": True,
    #     "lock_races_behind_flag": True,
    #     "start_with_checkfinders": True,
    #     "awkward_progression": False,
    # },
}

gator_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Logic Options",
        [
            Goal,
            ItemsIncluded,
            LocationsIncluded,
            IncludeBraceletsIfITDOnly,
            IncludeGliderIfITDOnly,
            StartWithFreeplay,
            RequireVerticalForITD,
            RequireShieldFlip,
            HarderRangedQuests,
            LockPotsBehindItems,
            LockChestsBehindKey,
            LockRacesBehindFlag,
            MakeAwkwardItemsProgression,
        ],
    ),
    OptionGroup("Convenience Options", [StartWithCheckFinders]),
    OptionGroup("Trap Options", [TrapChance, TrapTypeWeights]),
]
