from typing import TYPE_CHECKING
from dataclasses import dataclass

from . import Locations
from Options import Choice, DefaultOnToggle, Toggle, Range, OptionList, StartInventoryPool, PerGameCommonOptions

if TYPE_CHECKING:
    from . import MK64World


class TwoPlayer(Toggle):
    """Start with two characters unlocked and shuffle a separate Player 2 set of item powers into the item pool.

    This is the intended way to do local multiplayer, but you can still access the 2-player grand prix mode
    with this off, and the 1-player grand prix mode with it on."""
    display_name = "Two Player Couch Co-op"


class GameMode(Choice):
    """Determines how to advance through the game. Cups is closest to the vanilla game.

    Cups: Courses are raced in sets of four, place 4th or better to advance each race. Unlock each cup progressively.
    The Cups victory condition is beating the Special Cup on 150cc.

    Courses: Each course is run individually. Unlock the final courses progressively to reach the final race.
    The Courses victory condition is winning 1st place on the last course."""
    display_name = "Game Mode"
    option_cups = 0
    option_courses = 1
    default = 0


class LogicDifficulty(Choice):
    """Scales the logic threshhold where skill is involved. Specifically, how many good items are available before you
    are expected to be able to qualify and win on tough courses.

    Basic: Balanced runs for a competent karter.

    Advanced: Low logic, high randomness, high skill. Few good items may be available early in the run.

    Generous: Makes sure you have plenty of good items early. For easier play, or skipping 50 cc.

    No Logic: If fences are enabled, THE RUN MAY BE IMPOSSIBLE!"""
    display_name = "Logic Difficulty"
    option_basic = 3
    option_advanced = 0
    option_generous = 6
    option_no_logic = -100
    default = 3


class LockedCourses(Range):
    """In Courses Game Mode, how many final courses are locked until Progressive Course Unlock items are found."""
    display_name = "Locked Courses"
    range_start = 0
    range_end = 15
    default = 4


class CourseOrder(Choice):
    """The order for the courses to be arranged in."""
    display_name = "Course Order"
    option_vanilla = 0
    option_shuffle = 1
    option_short_to_long = 2
    option_long_to_short = 3
    option_alphabetical = 4
    default = 1


class FinalCoursePool(OptionList):
    """When Course Order is set to shuffle, the final course will be chosen from the Final Course Pool.
    Leaving this blank will allow any course to come last.

    For Rainbow Road to come last use: ["Rainbow Road"].

    For Bowser's Castle to come last use: ["Bowser's Castle"].

    For any course longer than 1000 meters to come last use: ["Rainbow Road", "Wario Stadium", "Toad's Turnpike"]."""
    display_name = "Final Course Pool"
    valid_keys = frozenset({course_name.casefold() for course_name in Locations.course_locations.keys()})
    valid_keys_casefold = True


class MirrorCourseChance(Range):
    """Percent chance for a course to be mirrored."""
    display_name = "Mirror Course Chance"
    range_start = 0
    range_end = 100
    default = 25


class TwoLapCourses(Choice):
    """Reduce the number of laps in a race from 3 to 2 on long courses."""
    display_name = "Two Lap Courses"
    option_off = 0
    option_rainbow_road = 1
    option_wario_stadium = 2
    option_rainbow_road_and_wario_stadium = 3
    default = 0


class HazardLocations(DefaultOnToggle):
    """Whether to include hazards which can be destroyed or defeated by the star power as location checks."""
    display_name = "Add Hazard Locations"


class SecretLocations(DefaultOnToggle):
    """Whether to add 10 location checks as item pickups in noteworthy locations on certain courses."""
    display_name = "Add Course Secret Locations"


class ShuffleDriftAbilities(Choice):
    """Optionally shuffle into the item pool the ability to drift and the ability to use mini-turbos as progressive
    unlocks per driver. "Plentiful" shuffles a 3rd progressive unlock into the pool. "Free Drift" means drivers start
    with the ability to drift. "Free mini-turbo" means both abilities will be obtained together."""
    display_name = "Shuffle Drift Abilities"
    option_off = 0
    option_on = 1
    option_plentiful = 2
    option_free_drift = 3
    option_free_mini_turbo = 4
    alias_vanilla = 0
    alias_shuffle = 0
    alias_false = 0
    alias_on = 1
    alias_yes = 1
    alias_true = 1
    default = 1


class TractionTires(Toggle):
    """Optionally shuffle into the item pool the ability to have traction on off-road and winter surface types,
    per driver. "Off" means karts always have traction, as in the vanilla game."""
    display_name = "Add Traction Tires"


class StartingItems(DefaultOnToggle):
    """Optionally shuffle into the item pool a random item power to start each race with, per driver. For example
    Mario may be able to start each race with a blue shell. Which item is random per driver."""
    display_name = "Add Starting Items"


class ShuffleRailings(DefaultOnToggle):
    """Whether to shuffle most track railings into the item pool."""
    display_name = "Shuffle Railings"


class FencesBlockPaths(Toggle):
    """Fences Block Paths: Adds fences where the track splits to block the optimal path.

    If any fence options are on, four Fence Switch items are added to the item pool to deactivate the corresponding
    color: yellow, red, green, and blue. Fences can be vaulted with items. CPU drivers and items pass through fences."""
    display_name = "Fences Block Paths"


class FencesAsObstacles(Toggle):
    """Fences As Obstacles: Adds fences in various places to disrupt the optimal racing line.

    If any fence options are on, four Fence Switch items are added to the item pool to deactivate the corresponding
    color: yellow, red, green, and blue. Fences can be vaulted with items. CPU drivers and items pass through fences."""
    display_name = "Fences As Obstacles"


class FencesBlockItemBoxes(Toggle):
    """Fences Block Item Boxes: Fences will be added around groups of item boxes on a few courses,
    with the matching switch handled as a prerequisite for those locations in logic.

    If any fence options are on, four Fence Switch items are added to the item pool to deactivate the corresponding
    color: yellow, red, green, and blue. Fences can be vaulted with items. CPU drivers and items pass through fences."""
    display_name = "Fences Block Item Boxes"


class FeatherItem(Toggle):
    """Adds the feather item as seen in Super Mario Kart and the early demos of Mario Kart 64. It can be used to vault
    fences. Having access to the feather also puts locations blocked by fences in logic."""
    display_name = "Feather Item"


class ShuffleItemBoxRespawning(Toggle):
    """Causes item boxes to not respawn mid-race, and shuffles one "item box respawning" item into the item pool."""
    display_name = "Shuffle Item Box Respawning"


class ConsistentItemBoxes(Choice):
    """Make each item box always give the same item. "On" will always show which item will be given instead of a
    question mark (?) inside the item boxes. "Identify" will only show which item will be given after triggering the
    item roulette once."""
    display_name = "Consistent Item Boxes"
    option_off = 0
    option_on = 1
    option_identify = 2
    default = 0


class ShuffleSpecialItemBoxes(Toggle):
    """Whether to shuffle the special item boxes which always give blue shells into the item pool. One is attached to
    the hot air balloon on Luigi Raceway, and the other is on the big rock on Koopa Troopa Beach."""
    display_name = "Shuffle Special Item Boxes"


class ShuffleItemBoxClusters(Range):
    """How many item box clusters to shuffle into the item pool. At least one item spot from each shuffled cluster will
    be used as a location check."""
    display_name = "Shuffle Item Box Clusters"
    range_start = 0
    range_end = 72
    default = 36


class FillerTrapPercentage(Range):
    """What percentage of filler items will be traps."""
    display_name = "Filler Trap Percentage"
    range_start = 0
    range_end = 100
    default = 20


class MinimumFillerItems(Range):
    """Force more filler items than needed to match the number of locations."""
    display_name = "Minimum Filler Items"
    range_start = 0
    range_end = 40
    default = 0


class FixResultsMusic(DefaultOnToggle):
    """Fixes the race win results screen music so the first section repeats 2 times, not 64 times.
    The official soundtrack uses this AABB form."""
    display_name = "Fix Winning Results Music"


class SoundMode(Choice):    # TODO: Add support for this
    """Sets the sound mode in the game's option menu ahead of time."""
    display_name = "Sound Mode"
    option_stereo = 0
    option_headphones = 1
    option_mono = 2
    default = 0


# Options as they will appear in YAML settings
@dataclass
class MK64Options(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    two_player: TwoPlayer
    game_mode: GameMode
    locked_courses: LockedCourses
    course_order: CourseOrder
    logic_difficulty: LogicDifficulty
    final_course_pool: FinalCoursePool
    mirror_course_chance: MirrorCourseChance
    two_lap_courses: TwoLapCourses
    hazard_locations: HazardLocations
    secret_locations: SecretLocations
    shuffle_drift_abilities: ShuffleDriftAbilities
    add_traction_tires: TractionTires
    add_starting_items: StartingItems
    shuffle_railings: ShuffleRailings
    fences_block_paths: FencesBlockPaths
    fences_as_obstacles: FencesAsObstacles
    fences_block_item_boxes: FencesBlockItemBoxes
    feather_item: FeatherItem
    shuffle_item_box_respawning: ShuffleItemBoxRespawning
    consistent_item_boxes: ConsistentItemBoxes
    shuffle_special_item_boxes: ShuffleSpecialItemBoxes
    shuffle_item_box_clusters: ShuffleItemBoxClusters
    filler_trap_percentage: FillerTrapPercentage
    minimum_filler_items: MinimumFillerItems
    fix_results_music: FixResultsMusic
    sound_mode: SoundMode


# Used for shorthand/faster access to relevant options during world generation
class Opt:
    def __init__(self, world: "MK64World"):
        # Relevant Options
        self.two_player =      world.options.two_player.value
        self.mode =            world.options.game_mode.value
        self.course_order =    world.options.course_order.value
        self.locked_courses =  world.options.locked_courses.value
        self.logic =           world.options.logic_difficulty.value
        self.final_pool =      world.options.final_course_pool.value
        self.mirror_chance =   world.options.mirror_course_chance.value
        self.two_lap_courses = world.options.two_lap_courses.value
        self.hazards =         world.options.hazard_locations.value
        self.secrets =         world.options.secret_locations.value
        self.drift =           world.options.shuffle_drift_abilities.value
        self.traction =        world.options.add_traction_tires.value
        self.starting_items =  world.options.add_starting_items.value
        self.railings =        world.options.shuffle_railings.value
        self.path_fences =     world.options.fences_block_paths.value
        self.obstacle_fences = world.options.fences_as_obstacles.value
        self.item_fences =     world.options.fences_block_item_boxes.value
        self.fences =          world.options.fences_block_paths.value + world.options.fences_as_obstacles.value + world.options.fences_block_item_boxes.value
        self.feather =         world.options.feather_item.value
        self.box_respawning =  world.options.shuffle_item_box_respawning.value
        self.consistent =      world.options.consistent_item_boxes.value
        self.special_boxes =   world.options.shuffle_special_item_boxes.value
        self.clusters =        world.options.shuffle_item_box_clusters.value
        self.trap_percentage = world.options.filler_trap_percentage.value
        self.min_filler =      world.options.minimum_filler_items.value
        self.fix_music =       world.options.fix_results_music.value
