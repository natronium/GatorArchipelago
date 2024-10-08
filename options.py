from dataclasses import dataclass
from typing import Dict, Any

from Options import Toggle, StartInventoryPool, PerGameCommonOptions, OptionGroup

class StartWithFreeplay(Toggle):
    """Start with no barrier around Tutorial Island and thus the ability to access checks on the main island."""

    internal_name = "start_with_freeplay"
    display_name = "Start With Freeplay"


class RequireShieldJump(Toggle):
    """Logic may require you to execute a shield jump to progress."""

    internal_name = "require_shield_jump"
    display_name = "Require Shield Jump"


class HarderRangedQuests(Toggle):
    """Logic may require you to complete Penelope (Bastion Beaver) and Andromeda (Space Hawk) without a ranged weapon."""

    internal_name = "harder_ranged_quests"
    display_name = "Harder Ranged Quests"


class StartWithCheckFinders(Toggle):
    """Start with Megaphone and Text Jill items in inventory for finding checks."""
    internal_name = "start_with_check_finder"
    display_name = "Start With Check Finders"


@dataclass
class GatorOptions(PerGameCommonOptions):
    start_with_freeplay: StartWithFreeplay
    require_shield_jump: RequireShieldJump
    harder_ranged_quests: HarderRangedQuests
    start_with_checkfinders: StartWithCheckFinders
    start_inventory_from_pool: StartInventoryPool


gator_options_presets = {
    "Maximal Accessibility": {
        "start_with_freeplay": True,
        "require_shield_jump": False,
        "harder_ranged_quests": False,
        "start_with_checkfinders": True,
    }
}

gator_option_groups: Dict[str, Dict[str, Any]] = [
    OptionGroup(
        "Logic Options", [StartWithFreeplay, RequireShieldJump, HarderRangedQuests]
    ),
    OptionGroup(
        "Convenience Options", [StartWithCheckFinders]
    )
]
