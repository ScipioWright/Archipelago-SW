from dataclasses import dataclass
from typing import Any

from schema import And, Schema

from Options import (
    Choice,
    OptionDict,
    StartInventoryPool,
    PerGameCommonOptions,
    OptionGroup,
    Toggle,
    Range,
    OptionSet,
    PlandoConnections
)

from .entrances.scene_transitions import scene_transition_names

class Goal(Choice):
    """Choose the goal for this run.
        - Lord of Doors: Defeat the Lord of Doors. Removes the Rusty Belltower Key location.
        - True Ending: Receive all 7 Ancient Tablets of Knowledge and go to the door in the Camp of the Free Crows
        - Green Tablet: Open the door in Family Tomb by planting enough life seeds (determined by plant_pot_number). Removes the Green Tablet location. The amount of extra Life Seeds in the pool is controlled by extra_life_seeds.
        - Any: any of the above goals are valid. Note: on minimal accessibility, not all goals may be possible. Both the Rusty Belltower Key and the Green Tablet locations are removed from randomization.
    """

    internal_name = "goal"
    display_name = "Goal"
    option_lord_of_doors = 0
    option_true_ending = 1
    option_green_tablet = 2
    option_any = 10

class StartDayOrNight(Choice):
    """Choose whether to start during the day or night. You must access the Rusty Belltower Bell to toggle the time of day."""

    internal_name = "start_day_or_night"
    display_name = "Start Day or Night"
    option_day = 0
    option_night = 1
    default = 0


class EarlyImportantItem(Choice):
    """Choose whether one random important item will be placed early in the multiworld, early and in your world, or to allow the items to be placed randomly.
    If the random placement is chosen, generation is more likely to fail with smaller multiworlds.
    Important items include non-boss doors, Hookshot, Bomb, and Fire, as these grant access to checks immediately.
    """

    internal_name = "early_important_item"
    display_name = "Early Important Item"
    option_early = 0
    option_local_early = 1
    option_random_placement = 2
    default = option_early


class ExtraLifeSeeds(Range):
    """Add extra life seeds or remove extra life seeds from the item pool, which are interchanged with Soul Orb items. Additional extra life seeds will be marked as useful.
    
    When removing life seeds (using a negative number), the number left in the pool will be at minimum the number required by plant_pot_number.
    """

    internal_name = "extra_life_seeds"
    display_name = "Adjust Extra Life Seeds"
    range_start = -49
    range_end = 20
    default = 0

class PlantedPotsRequired(Range):
    """Number of planted pots required for Green Tablet location. Also adjusts the number of Life Seeds marked as Progression."""

    internal_name = "plant_pot_number"
    display_name = "Number of Planted Pots Required for Green Tablet"
    range_start = 1
    range_end = 50
    default = 25


class ExtraMagicShards(Range):
    """Add extra magic shards to the item pool, replacing Soul Orb items. Extra magic shards can allow your magic to go over the vanilla maximum of 6. Each extra pip of magic requires 4 shards."""

    internal_name = "extra_magic_shards"
    display_name = "Extra Magic Shards"
    range_start = 0
    range_end = 8
    default = 0


class ExtraVitalityShards(Range):
    """Add extra vitality shards to the item pool, replacing Soul Orb items. Extra vitality shards can allow your health to go over the vanilla maximum of 6. Each extra pip of health requires 4 shards."""

    internal_name = "extra_magic_shards"
    display_name = "Extra Magic Shards"
    range_start = 0
    range_end = 8
    default = 0


class RemoveSpellUpgrades(Toggle):
    """Remove the spell upgrades from the pool, such that there is only 1 Fire, 1 Bomb, and 1 Hookshot in the pool (and no upgrade for Arrow)."""

    internal_name = "remove_spell_upgrades"
    display_name = "Remove Spell Upgrades"


class StartWeapon(Choice):
    """Choose which weapon you would like to start with. The others will be shuffled into the itempool as useful items. Note: Umbrella is a much worse weapon than the other 4, choose it at your own risk."""

    internal_name = "start_weapon"
    display_name = "Starting Weapon"
    option_sword = 0
    option_daggers = 1
    option_hammer = 2
    option_greatsword = 3
    option_umbrella = 4
    option_random_excluding_umbrella = 5
    default = option_sword


class SoulMultiplier(Range):
    """Multilpy the amount of souls you receive, both from enemies and received Soul Orbs. Must be an integer."""
    
    internal_name = "soul_multiplier"
    display_name = "Soul Multiplier"
    range_start = 1
    range_end = 10
    default = 2


class StartingSouls(Range):
    """Amount of souls to start the game with. Each full upgrade of a stat costs 4,300 souls."""

    internal_name = "starting_souls"
    display_name = "Starting Souls"
    range_start = 0
    range_end = 17200
    default = 0

class GateRollsGlitch(Toggle):
    """Puts rolling through certain "gates" in logic.
        - Estate entrance to Crypt through metal gate
        - Mushroom Dungeon Lobby to Overgrown Ruins through vines
        - Mushroom Dungeon Ancient Door to Lobby through a metal gate and a cobweb
        - Ceramic Manor Lobby to the Manor exit to Estate through breakable-pot door"""
    
    internal_name = "gate_rolls_glitch"
    display_name = "Gate Rolls Glitch"


class BombBellGlitch(Toggle):
    """Puts bombing the Rusty Belltower's bell from a railing to toggle Day/Night in logic. Also, known as "Early Night"."""

    internal_name = "bomb_bell_glitch"
    display_name = "Bomb Bell Glitch"


class OffscreenTargetingTricks(Toggle):
    """Puts three tricks in which you must target an enemy or switch from offscreen in logic.
        - Open the switch between Lost Cemetery and Stranded Sailor caves using an Arrow through a fire source instead of Fire
        - Open a bomb wall in Overgrown Ruins lower by hitting an offscreen bomb flower with an arrow
        - Open the path backwards from Flooded Fortress Frog King Statue back to the entrance by hitting a switch offscreen"""
    
    internal_name = "offscreen_targeting_tricks"
    display_name = "Offscreen Targeting Tricks"


class GeometryExploits(Toggle):
    """Puts a series of exploits where you roll on unintended surfaces in logic.
        - Rolling across the walls near the ladder immediately outside the exit from Lost Cemetery to Stranded Sailor Caves to navigate around the switch on the Lost Cemetery side
        - Rolling behind the grate in Castle Lockstone East Upper down to East
        - Rolling onto the wall from the upper right platform in Lockstone East Upper after making it go up to get into East Upper Keyed Door without the lever
        - When coming from the Old Watchtowers Barb Elevator, the lever to Ice Skating Start can be skipped by hooking over the gate from the ledge around the top of the elevator
        - In Overgrown Ruins, access the Soul Orb in Lower that requires Hookshot by rolling onto the wall above and falling down. Standalone randomizer notes that this roll may require Haste (rolling stat) >=2.
        - In Overgrown Ruins, access the Soul Orb in the Lord of Doors Hookshot arena by ???. Standalone randomizer is missing a description of this one, but best guess it is the same as the above."""
    
    internal_name = "geometry_exploits"
    display_name = "Geometry Exploits"


class RollBuffers(Toggle):
    """Puts roll buffers in logic, where you roll in mid-air after a heavy attack. Three of these tricks can be performed with any weapon but the Thunder Hammer. Two are only doable with the Rogue Daggers. This option will cause all weapons besides the Thudner Hammer to be marked as progression.
        - Hall of Doors - Surveillance Device: Heavy to the right and roll down-right from behind the bin near the Discarded Umbrella check
        - Hall of Doors - Bomb Secret Soul Orb: Same as above
        - Hall of Doors - Hookshot Secret Soul Orb: Up-right heavy and roll from above the Lord of Doors poster by the staircase near the Bomb Avarice Chest (Rogue Daggers only)
        - Hall of Doors - Modern Door Scale Model: Same as above (Rogue Daggers only)
        - Castle Lockstone - West Locked Crow: Heavy out of the ledge above the gate then immediately roll back"""

    internal_name = "roll_buffers"
    display_name = "Roll Buffers"


# Trap Chance and Trap Type Weights from Ixrec's Outer Wilds implementation
class TrapChance(Range):
    """The probability for each filler item (including unique filler) to be replaced with a trap item.
    The exact number of trap items will still be somewhat random, so you can't know
    if you've seen the 'last trap' in your world without checking the spoiler log.
    If you don't want any traps, set this to 0."""
    display_name = "Trap Chance"
    range_start = 0
    range_end = 100
    default = 15


class TrapTypeWeights(OptionDict):
    """When a filler item is replaced with a trap, these weights determine the
    odds for each trap type to be selected.
    If you don't want a specific trap type, set its weight to 0.
    Setting all weights to 0 is the same as setting trap_chance to 0."""
    schema = Schema({
        "Rotation Trap": And(int, lambda n: n >= 0),
        "Player Invisibility Trap": And(int, lambda n: n >= 0),
        "Enemy Invisibility Trap": And(int, lambda n: n >= 0),
        "Knockback Trap": And(int, lambda n: n >= 0),
    })
    display_name = "Trap Type Weights"
    default = {
        "Rotation Trap": 2,
        "Player Invisibility Trap": 2,
        "Enemy Invisibility Trap": 0,
        "Knockback Trap": 2,
    }

class UnrandomizedPools(OptionSet):
    """Allows sets of location-item pairs (pools) to be removed from randomization. Valid keys are:
    - Spell
    - Weapon
    - Giant Soul
    - Shrine
    - Shiny Thing
    - Life Seed
    - Soul Orb
    - Tablet
    - Lever
    - Door
    - Lost Crow
    
    Keys must be randomized because their vanilla locations can cause a softlock in rando.

    If you remove Weapons from randomization, your starting weapon will be forced to be the Reaper's Sword (default weapon).
    If you remove Shiny Things from randomization, Rusty Belltower Key will still be added to the pool for day/night access.
    If you combine this option with plando not from pool, you are very likely to encounter generation errors.
    The fewer pools randomized, the more likely you are to encounter generation errors."""

    internal_name = "unrandomized_pools"
    display_name = "Unrandomized Pools"

    valid_keys = frozenset(
        {
            "Spell",
            "Weapon",
            "Giant Soul",
            "Shrine",
            "Shiny Thing",
            "Life Seed",
            "Soul Orb",
            "Tablet",
            "Lever",
            "Door",
            "Lost Crow",
        }
    )
    default = frozenset({})

class EntranceRandomization(Choice):
    """Randomize entrances."""

    internal_name = "entrance_randomization"
    display_name = "Entrance Randomization"
    option_off = 0
    option_coupled = 1
    option_decoupled = 2

class DeathsDoorPlandoConnections(PlandoConnections):
    """
    Generic connection plando. Format is:
    - entrance: Entrance Name
      exit: Exit Name
      direction: Direction
      percentage: 100
    Direction must be one of entrance, exit, or both, and defaults to both if omitted.
    Direction entrance means the entrance leads to the exit. Direction exit means the exit leads to the entrance.
    If you do not have Decoupled enabled, you do not need the direction line, as it will only use both.
    Percentage is an integer from 0 to 100 which determines whether that connection will be made. Defaults to 100 if omitted.
    This option does nothing if Entrance Randomization is disabled."""

    entrances = frozenset(scene_transition_names())
    exits = frozenset(scene_transition_names())

    duplicate_exits = False

@dataclass
class DeathsDoorOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    start_day_or_night: StartDayOrNight
    early_important_item: EarlyImportantItem
    start_weapon: StartWeapon
    soul_multiplier: SoulMultiplier
    starting_souls: StartingSouls
    plant_pot_number: PlantedPotsRequired
    extra_life_seeds: ExtraLifeSeeds
    extra_magic_shards: ExtraMagicShards
    extra_vitality_shards: ExtraVitalityShards
    remove_spell_upgrades: RemoveSpellUpgrades
    trap_chance: TrapChance
    trap_type_weights: TrapTypeWeights
    gate_rolls_glitch: GateRollsGlitch
    bomb_bell_glitch: BombBellGlitch
    offscreen_targeting_tricks: OffscreenTargetingTricks
    geometry_exploits: GeometryExploits
    roll_buffers: RollBuffers
    unrandomized_pools: UnrandomizedPools
    goal: Goal
    entrance_randomization : EntranceRandomization
    plando_connections: DeathsDoorPlandoConnections


deathsdoor_options_presets: dict[str, dict[str, Any]] = {}

deathsdoor_option_groups: list[OptionGroup] = [
    OptionGroup("Logic Options", [Goal, EntranceRandomization, StartDayOrNight, PlantedPotsRequired, EarlyImportantItem, GateRollsGlitch,
                                  BombBellGlitch, OffscreenTargetingTricks, GeometryExploits, RollBuffers]),
    OptionGroup("Itempool Modification Options", [ExtraLifeSeeds, ExtraMagicShards, ExtraVitalityShards,
                                                  RemoveSpellUpgrades, UnrandomizedPools, TrapChance, TrapTypeWeights]),
    OptionGroup("Customization Options", [StartWeapon, SoulMultiplier, StartingSouls])
]
