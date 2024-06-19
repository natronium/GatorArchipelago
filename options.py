from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PerGameCommonOptions, OptionGroup

class StartWithFreeplay(Toggle):
    """Start with no barrier around Tutorial Island and thus the ability to access checks on the main island."""
    internal_name = "start_with_freeplay"
    display_name = "Start With Freeplay"

class RequireShieldJump(Toggle):
    """Logic may require you to execute a shield jump to progress."""
    internal_name = "require_shield_jump"
    display_name = "Require Shield Jump"

# class StartWithCheckFinders(Toggle):
#     """Start with Megaphone and Text Jill items in inventory for finding checks."""
#     internal_name = "start_with_check_finder"
#     display_name = "Start With Check Finders"

@dataclass
class GatorOptions(PerGameCommonOptions):
    start_with_freeplay: StartWithFreeplay
    require_shield_jump: RequireShieldJump


gator_options_presets = {
    "Maximal Accessibility" : {
        "start_with_freeplay" : True,
        "require_shield_jump" : False
    }
}

gator_option_groups = {
    OptionGroup("Logic Options", [
        StartWithFreeplay,
        RequireShieldJump
    ])
}