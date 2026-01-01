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
)


class StartWithFreeplay(Toggle):
    """Start with no barrier around Tutorial Island and thus the ability to access checks on the main island."""

    internal_name = "start_with_freeplay"
    display_name = "Start With Freeplay"


class RequireShieldJump(Toggle):
    """Logic may require you to execute a shield jump (jump, then press shield button) to progress."""

    internal_name = "require_shield_jump"
    display_name = "Require Shield Jump"


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


class MakeAwkwardCardboardDestroyersProgression(Toggle):
    """Marks Sticky Hand, Balloon, Bubble Gum, and Ragdoll as progression, which means the generator can put them as your first logical Cardboard Destroyer."""

    internal_name = "awkward_progression"
    display_name = "Make Awkward Cardboard Destroyers Progression"


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
        "Pixel Trap": 0,
    }


@dataclass
class GatorOptions(PerGameCommonOptions):
    start_with_freeplay: StartWithFreeplay
    require_shield_jump: RequireShieldJump
    harder_ranged_quests: HarderRangedQuests
    lock_pots_behind_items: LockPotsBehindItems
    lock_chests_behind_key: LockChestsBehindKey
    lock_races_behind_flag: LockRacesBehindFlag
    start_with_checkfinders: StartWithCheckFinders
    awkward_progression: MakeAwkwardCardboardDestroyersProgression
    start_inventory_from_pool: StartInventoryPool
    trap_chance: TrapChance
    trap_type_weights: TrapTypeWeights


gator_options_presets: dict[str, dict[str, Any]] = {
    "Maximal Accessibility": {
        "start_with_freeplay": True,
        "require_shield_jump": False,
        "harder_ranged_quests": False,
        "lock_pots_behind_items": False,
        "lock_chests_behind_key": False,
        "lock_races_behind_flag": False,
        "start_with_checkfinders": True,
        "awkward_progression": False,
    },
    "Locked Down": {
        "start_with_freeplay": False,
        "require_shield_jump": False,
        "harder_ranged_quests": False,
        "lock_pots_behind_items": True,
        "lock_chests_behind_key": True,
        "lock_races_behind_flag": True,
        "start_with_checkfinders": True,
        "awkward_progression": False,
    },
}

gator_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Logic Options",
        [
            StartWithFreeplay,
            RequireShieldJump,
            HarderRangedQuests,
            LockPotsBehindItems,
            LockChestsBehindKey,
            LockRacesBehindFlag,
            MakeAwkwardCardboardDestroyersProgression,
        ],
    ),
    OptionGroup("Convenience Options", [StartWithCheckFinders]),
    OptionGroup("Trap Options", [TrapChance, TrapTypeWeights]),
]
