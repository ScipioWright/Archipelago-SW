from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, PerGameCommonOptions, OptionGroup


class Goal(Choice):
    """
    What you need to do to beat the game.
    Fireworks requires you to get the 4 flames and defeat the Manticore. The House Key item is removed from the item pool.
    Bunny Land requires you to find the 65th Egg, bring it to the incubator, and leave the Well.
    Egg Hunt requires you to collect the amount of eggs you need to open the 4th Egg Door, then open the chest inside.
    """
    internal_name = "goal"
    display_name = "Goal"
    option_fireworks = 1
    # option_bunny_land = 2
    # option_egg_hunt = 3
    default = 1


class FinalEggLocation(Choice):
    """
    Choose whether the 65th Egg is shuffled into the multiworld item pool or placed in its vanilla location, requiring opening the 4th Egg Door to access it.
    """
    internal_name = "final_egg_location"
    display_name = "65th Egg Location"
    option_randomized = 0
    option_vanilla = 1
    default = 1


class EggsNeeded(Range):
    """
    How many Eggs you need to open the 4th Egg Door.
    The amount of Eggs you need for the other 3 doors will scale accordingly.
    """
    internal_name = "eggs_needed"
    display_name = "Eggs Required"
    range_start = 8
    range_end = 64
    default = 48


class BunniesAsChecks(Choice):
    """
    Include the secret bunnies as checks.
    """
    internal_name = "bunnies_as_checks"
    display_name = "Bunnies as Checks"
    option_off = 0
    # option_exclude_tedious = 1
    # option_all_bunnies = 2
    default = 0


class CandleChecks(Toggle):
    """
    Lighting each of the candles sends a check.
    """
    internal_name = "candle_checks"
    display_name = "Candle Checks"


class KeyRing(DefaultOnToggle):
    """
    Have one keyring which unlocks all normal key doors instead of individual key items.
    Note: Due to how consumable key logic works, if this option is not enabled, you logically require all 6 keys to open any of the key doors.
    """
    internal_name = "key_ring"
    display_name = "Key Ring"


class Matchbox(DefaultOnToggle):
    """
    Have one matchbox which can light all candles instead of individual match items.
    Note: Due to how consumable item logic works, if this option is not enabled, you logically require all 9 matches to light any of the candles.
    """
    internal_name = "matchbox"
    display_name = "Matchbox"


class BubbleJumping(Choice):
    """
    Include using the standard Bubble Wand and chaining bubble jumps together in logic.
    Exclude Long Chains makes it so you may be required to chain a few bubble jumps before landing.
    """
    internal_name = "bubble_jumping"
    display_name = "Bubble Jumping"
    option_off = 0
    option_exclude_long_chains = 1
    option_on = 2
    default = 1


class DiscHopping(Choice):
    """
    Include jumping onto the disc without letting it bounce off of a wall first in logic.
    Single means doing it once from the ground.
    Multiple means having to chain them in midair.
    Exception: The bunny that requires you to use this tech.
    """
    internal_name = "disc_hopping"
    display_name = "Midair Disc Jumping"
    option_off = 0
    option_single = 1
    option_multiple = 2
    default = 0


class WheelHopping(Toggle):
    """
    Include toggling the wheel midair to get a double jump in logic.
    """
    internal_name = "wheel_hopping"
    display_name = "Wheel Hopping"


@dataclass
class AnimalWellOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    eggs_needed: EggsNeeded
    key_ring: KeyRing
    matchbox: Matchbox
    final_egg_location: FinalEggLocation
    bunnies_as_checks: BunniesAsChecks
    candle_checks: CandleChecks
    bubble_jumping: BubbleJumping
    disc_hopping: DiscHopping
    wheel_hopping: WheelHopping


aw_option_groups = [
    OptionGroup("Logic Options", [
        BubbleJumping,
        DiscHopping,
        WheelHopping,
    ])
]