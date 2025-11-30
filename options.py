from dataclasses import dataclass
from typing import Any

from Options import DefaultOnToggle, Toggle, StartInventoryPool, PerGameCommonOptions, OptionGroup

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
    }
}

gator_option_groups: list[OptionGroup] = [
    OptionGroup(
        "Logic Options", [StartWithFreeplay, RequireShieldJump, HarderRangedQuests, LockPotsBehindItems, LockChestsBehindKey, LockRacesBehindFlag, MakeAwkwardCardboardDestroyersProgression]
    ),
    OptionGroup(
        "Convenience Options", [StartWithCheckFinders]
    )
]
