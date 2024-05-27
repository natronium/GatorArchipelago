from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PerGameCommonOptions

class StartWithFreeplay(Toggle):
    """Start with no barrier around Tutorial Island and thus the ability to access checks on the main island."""
    internal_name = "start_with_freeplay"
    display_name = "Start With Freeplay"

class RequireShieldJump(Toggle):
    """Logic may require you to execute a shield jump to progress."""
    internal_name = "require_shield_jump"
    display_name = "Require Shield Jump"

@dataclass
class GatorOptions(PerGameCommonOptions):
    start_with_freeplay: StartWithFreeplay
    require_shield_jump: RequireShieldJump

