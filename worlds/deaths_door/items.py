from enum import Enum

from typing import NamedTuple
from BaseClasses import ItemClassification


class ItemGroup(str, Enum):
    SPELL = "Spell"
    WEAPON = "Weapon"
    KEY = "Key"
    GIANT_SOUL = "Giant Soul"
    SHINY_THING = "Shiny Thing"
    TABLET = "Tablet"
    LEVER = "Lever"
    DOOR = "Door"
    LOST_CROW = "Lost Crow"
    LIFE_SEED = "Life Seed"
    # SOUL_ORB = "Soul Orb"
    SHRINE = "Shrine"
    TRAP = "Trap"


class DeathsDoorItemName(str, Enum):
    def __str__(self) -> str:
        return self.value

    FIRE = "Fire"
    BOMB = "Bomb"
    HOOKSHOT = "Hookshot"
    BOW = "Arrow Upgrade"
    SWORD = "Reaper's Sword"
    ROGUE_DAGGERS = "Rogue Daggers"
    DISCARDED_UMBRELLA = "Discarded Umbrella"
    REAPERS_GREATSWORD = "Reaper's Greatsword"
    THUNDER_HAMMER = "Thunder Hammer"
    VITALITY_SHARD = "Vitality Shard"
    MAGIC_SHARD = "Magic Shard"
    LIFE_SEED = "Life Seed"
    SOULS = "Soul Orb"
    PINK_KEY = "Pink Key"
    GREEN_KEY = "Green Key"
    YELLOW_KEY = "Yellow Key"
    ENGAGEMENT_RING = "Engagement Ring"
    OLD_COMPASS = "Old Compass"
    INCENSE = "Incense"
    UNDYING_BLOSSOM = "Undying Blossom"
    OLD_PHOTOGRAPH = "Old Photograph"
    SLUDGE_FILLED_URN = "Sludge-Filled Urn"
    TOKEN_OF_DEATH = "Token of Death"
    RUSTY_GARDEN_TROWEL = "Rusty Garden Trowel"
    CAPTAINS_LOG = "Captain's Log"
    GIANT_ARROWHEAD = "Giant Arrowhead"
    MALFORMED_SEED = "Malformed Seed"
    CORRUPTED_ANTLER = "Corrupted Antler"
    MAGICAL_FOREST_HORN = "Magical Forest Horn"
    ANCIENT_CROWN = "Ancient Crown"
    GRUNTS_OLD_MASK = "Grunt's Old Mask"
    ANCIENT_DOOR_SCALE_MODEL = "Ancient Door Scale Model"
    MODERN_DOOR_SCALE_MODEL = "Modern Door Scale Model"
    RUSTY_BELLTOWER_KEY = "Rusty Belltower Key"
    SURVEILLANCE_DEVICE = "Surveillance Device"
    SHINY_MEDALLION = "Shiny Medallion"
    INK_COVERED_TEDDY_BEAR = "Ink-Covered Teddy Bear"
    DEATHS_CONTRACT = "Death's Contract"
    MAKESHIFT_SOUL_KEY = "Makeshift Soul Key"
    MYSTERIOUS_LOCKET = "Mysterious Locket"
    RED_ANCIENT_TABLET_OF_KNOWLEDGE = "Red Ancient Tablet of Knowledge"
    YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE = "Yellow Ancient Tablet of Knowledge"
    GREEN_ANCIENT_TABLET_OF_KNOWLEDGE = "Green Ancient Tablet of Knowledge"
    CYAN_ANCIENT_TABLET_OF_KNOWLEDGE = "Cyan Ancient Tablet of Knowledge"
    BLUE_ANCIENT_TABLET_OF_KNOWLEDGE = "Blue Ancient Tablet of Knowledge"
    PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE = "Purple Ancient Tablet of Knowledge"
    PINK_ANCIENT_TABLET_OF_KNOWLEDGE = "Pink Ancient Tablet of Knowledge"
    LEVER_BOMB_EXIT = "Hall of Doors - Bomb Exit Lever"
    LEVER_CEMETERY_SEWER = "Lost Cemetery - Sewer Lever"
    LEVER_GUARDIAN_OF_THE_DOOR_ACCESS = (
        "Lost Cemetery - Guardian of the Door Access Lever"
    )
    LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE = "Lost Cemetery - Shortcut to East Tree Lever"
    LEVER_CEMETERY_EAST_TREE = "Lost Cemetery - East Tree Lever"
    LEVER_CATACOMBS_TOWER = "Lost Cemetery - Catacombs Tower Lever"
    LEVER_CEMETERY_EXIT_TO_ESTATE = "Lost Cemetery - Exit to Estate Lever"
    LEVER_CATACOMBS_EXIT = "Lost Cemetery - Catacombs Exit Lever"
    LEVER_HOOKSHOT_SILENT_SERVANT = (
        "Stranded Sailor Caves - Hookshot Silent Servant Lever"
    )
    LEVER_SAILOR_TURNCAM_UPPER = "Stranded Sailor - Turncam Upper Lever"
    LEVER_SAILOR_TURNCAM_LOWER = "Stranded Sailor - Turncam Lower Lever"
    LEVER_SAILOR_GREATSWORD_GATE = "Stranded Sailor - Greatsword Gate Lever"
    LEVER_LOCKSTONE_EAST_START_SHORTCUT = "Castle Lockstone - East Start Shortcut Lever"
    LEVER_LOCKSTONE_ENTRANCE = "Castle Lockstone - Entrance Lever"
    LEVER_LOCKSTONE_EAST_LOWER = "Castle Lockstone - East Lower Lever"
    LEVER_LOCKSTONE_UPPER_SHORTCUT = "Castle Lockstone - Upper Shortcut Lever"
    LEVER_LOCKSTONE_DUAL_LASER_PUZZLE = "Castle Lockstone - Dual Laser Puzzle Lever"
    LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE = (
        "Castle Lockstone - Tracking Beam Puzzle Lever"
    )
    LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE = (
        "Castle Lockstone - Vertical Laser Puzzle Lever"
    )
    LEVER_LOCKSTONE_NORTH_PUZZLE = "Castle Lockstone - North Puzzle Lever"
    LEVER_LOCKSTONE_SHRINE = "Castle Lockstone - Shrine Lever"
    LEVER_LOCKSTONE_HOOKSHOT_PUZZLE = "Castle Lockstone - Hookshot Puzzle Lever"
    LEVER_LOCKSTONE_UPPER_PUZZLE = "Castle Lockstone - Upper Puzzle Lever"
    LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE = (
        "Castle Lockstone - Upper Dual Laser Puzzle Lever"
    )
    LEVER_WATCHTOWERS_BEFORE_ICE_ARENA = "Old Watchtowers - Before Ice Arena Lever"
    LEVER_WATCHTOWERS_AFTER_ICE_SKATING = "Old Watchtowers - After Ice Skating Lever"
    LEVER_WATCHTOWERS_AFTER_BOOMERS = "Old Watchtowers - After Boomers Lever"
    LEVER_RUINS_SETTLEMENT_GATE = "Overgrown Ruins - Settlement Gate Lever"
    LEVER_RUINS_UPPER_DUNGEON_ENTRANCE = (
        "Overgrown Ruins - Upper Dungeon Entrance Lever"
    )
    LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA = (
        "Overgrown Ruins - Ladder Left of Lord of Doors Arena Lever"
    )
    LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT = (
        "Overgrown Ruins - Entrance Ladder Shortcut Lever"
    )
    LEVER_RUINS_MAIN_GATE = "Overgrown Ruins - Main Gate Lever"
    LEVER_DUNGEON_ENTRANCE_RIGHT_GATE = "Mushroom Dungeon - Entrance Right Gate Lever"
    LEVER_DUNGEON_ENTRANCE_LEFT_GATE = "Mushroom Dungeon - Entrance Left Gate Lever"
    LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW = "Mushroom Dungeon - Above Rightmost Crow Lever"
    LEVER_FORTRESS_BOMB = "Flooded Fortress - Bomb Lever"
    LEVER_FORTRESS_MAIN_GATE = "Flooded Fortress - Main Gate Lever"
    LEVER_FORTRESS_CENTRAL_SHORTCUT = "Flooded Fortress - Central Shortcut Lever"
    LEVER_FORTRESS_STATUE = "Flooded Fortress - Statue Lever"
    LEVER_FORTRESS_WATCHTOWER_LOWER = "Flooded Fortress - Watchtower Lower Lever"
    LEVER_FORTRESS_BRIDGE = "Flooded Fortress - Bridge Lever"
    LEVER_FORTRESS_PRE_MAIN_GATE = "Flooded Fortress - Pre-Main Gate Lever"
    LEVER_FORTRESS_WATCHTOWER_UPPER = "Flooded Fortress - Watchtower Upper Lever"
    LEVER_FORTRESS_NORTH_WEST = "Flooded Fortress - North West Lever"
    LEVER_ESTATE_ELEVATOR_LEFT = "Lost Cemetery - Crypt Elevator to Estate Left Lever"
    LEVER_ESTATE_ELEVATOR_RIGHT = "Lost Cemetery - Crypt Elevator to Estate Right Lever"
    LEVER_GARDEN_OF_LOVE = "Estate of the Urn Witch - Garden of Love Lever"
    LEVER_GARDEN_OF_LIFE_END = "Estate of the Urn Witch - Garden of Life End Lever"
    LEVER_GARDEN_OF_PEACE = "Estate of the Urn Witch - Garden of Peace Lever"
    LEVER_GARDEN_OF_JOY = "Estate of the Urn Witch - Garden of Joy Lever"
    LEVER_GARDEN_OF_LOVE_TURNCAM = (
        "Estate of the Urn Witch - Garden of Love Turncam Lever"
    )
    LEVER_GARDEN_OF_LIFE_LANTERNS = (
        "Estate of the Urn Witch - Garden of Life Lanterns Lever"
    )
    LEVER_ESTATE_UNDERGROUND_URN_SHED = (
        "Estate of the Urn Witch - Underground Urn Shed Lever"
    )
    LEVER_MANOR_BIG_POT_ARENA = "Ceramic Manor - Big Pot Arena Lever"
    LEVER_MANOR_BOOKSHELF_SHORTCUT = "Ceramic Manor - Bookshelf Shortcut Lever"
    GROVE_OF_SPIRITS_DOOR = "Grove of Spirits Door"
    LOST_CEMETERY_DOOR = "Lost Cemetery Door"
    STRANDED_SAILOR_DOOR = "Stranded Sailor Door"
    CASTLE_LOCKSTONE_DOOR = "Castle Lockstone Door"
    CAMP_OF_THE_FREE_CROWS_DOOR = "Camp of the Free Crows Door"
    OLD_WATCHTOWERS_DOOR = "Old Watchtowers Door"
    BETTYS_LAIR_DOOR = "Betty's Lair Door"
    OVERGROWN_RUINS_DOOR = "Overgrown Ruins Door"
    MUSHROOM_DUNGEON_DOOR = "Mushroom Dungeon Door"
    FLOODED_FORTRESS_DOOR = "Flooded Fortress Door"
    THRONE_OF_THE_FROG_KING_DOOR = "Throne of the Frog King Door"
    ESTATE_OF_THE_URN_WITCH_DOOR = "Estate of the Urn Witch Door"
    CERAMIC_MANOR_DOOR = "Ceramic Manor Door"
    INNER_FURNACE_DOOR = "Inner Furnace Door"
    THE_URN_WITCHS_LABORATORY_DOOR = "The Urn Witch's Laboratory Door"
    GIANT_SOUL_OF_THE_URN_WITCH = "Giant Soul of The Urn Witch"
    GIANT_SOUL_OF_THE_FROG_KING = "Giant Soul of The Frog King"
    GIANT_SOUL_OF_BETTY = "Giant Soul of Betty"
    CROW_MANOR_AFTER_TORCH_PUZZLE = "Ceramic Manor - After Torch Puzzle Crow"
    CROW_MANOR_IMP_LOFT = "Ceramic Manor - Imp Loft Crow"
    CROW_MANOR_LIBRARY = "Ceramic Manor - Library Crow"
    CROW_MANOR_BEDROOM = "Ceramic Manor - Bedroom Crow"
    CROW_DUNGEON_HALL = "Mushroom Dungeon - Hall Crow"
    CROW_DUNGEON_WATER_ARENA = "Mushroom Dungeon - Water Arena Crow"
    CROW_DUNGEON_COBWEB = "Mushroom Dungeon - Cobweb Crow"
    CROW_DUNGEON_RIGHTMOST = "Mushroom Dungeon - Rightmost Crow"
    CROW_LOCKSTONE_EAST = "Castle Lockstone - East Crow"
    CROW_LOCKSTONE_WEST = "Castle Lockstone - West Crow"
    CROW_LOCKSTONE_WEST_LOCKED = "Castle Lockstone - West Locked Crow"
    CROW_LOCKSTONE_SOUTH_WEST = "Castle Lockstone - South West Crow"

    ROTATION_TRAP = "Rotation Trap"
    PLAYER_INVISIBILITY_TRAP = "Player Invisibility Trap"
    ENEMY_INVISIBILITY_TRAP = "Enemy Invisibility Trap"
    KNOCKBACK_TRAP = "Knockback Trap"


class DeathsDoorItemData(NamedTuple):
    name: DeathsDoorItemName
    mod_string: str
    item_id: int
    classification: ItemClassification
    base_quantity_in_item_pool: int
    item_groups: list[ItemGroup]


item_table: list[DeathsDoorItemData] = [
    DeathsDoorItemData(
        DeathsDoorItemName.LIFE_SEED,
        "Life Seed",
        100,
        ItemClassification.progression_skip_balancing,
        50,
        [ItemGroup.LIFE_SEED],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.FIRE,
        "Fire",
        200,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOMB,
        "Bomb",
        210,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.HOOKSHOT,
        "Hookshot",
        220,
        ItemClassification.progression,
        2,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BOW,
        "Arrow Upgrade",
        230,
        ItemClassification.useful,
        1,
        [ItemGroup.SPELL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SWORD,
        "Reaper's Sword",
        300,
        ItemClassification.progression,
        0,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ROGUE_DAGGERS,
        "Rogue Daggers",
        301,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DISCARDED_UMBRELLA,
        "Discarded Umbrella",
        302,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.REAPERS_GREATSWORD,
        "Reaper's Greatsword",
        303,
        ItemClassification.progression,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THUNDER_HAMMER,
        "Thunder Hammer",
        304,
        ItemClassification.useful,
        1,
        [ItemGroup.WEAPON],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.VITALITY_SHARD,
        "Vitality Shard",
        400,
        ItemClassification.useful,
        8,
        [ItemGroup.SHRINE],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGIC_SHARD,
        "Magic Shard",
        450,
        ItemClassification.useful,
        8,
        [ItemGroup.SHRINE],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SOULS,
        "100 Souls",
        500,
        ItemClassification.filler,
        0,
        [],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PINK_KEY,
        "Pink Key",
        600,
        ItemClassification.progression,
        5,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_KEY,
        "Green Key",
        610,
        ItemClassification.progression,
        4,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_KEY,
        "Yellow Key",
        620,
        ItemClassification.progression,
        3,
        [ItemGroup.KEY],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ENGAGEMENT_RING,
        "Engagement Ring",
        700,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_COMPASS,
        "Old Compass",
        701,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INCENSE,
        "Incense",
        702,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.UNDYING_BLOSSOM,
        "Undying Blossom",
        703,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_PHOTOGRAPH,
        "Old Photograph",
        704,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SLUDGE_FILLED_URN,
        "Sludge-Filled Urn",
        705,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.TOKEN_OF_DEATH,
        "Token of Death",
        706,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_GARDEN_TROWEL,
        "Rusty Garden Trowel",
        707,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAPTAINS_LOG,
        "Captain's Log",
        708,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_ARROWHEAD,
        "Giant Arrowhead",
        709,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MALFORMED_SEED,
        "Malformed Seed",
        710,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CORRUPTED_ANTLER,
        "Corrupted Antler",
        711,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAGICAL_FOREST_HORN,
        "Magical Forest Horn",
        712,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_CROWN,
        "Ancient Crown",
        713,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GRUNTS_OLD_MASK,
        "Grunt's Old Mask",
        714,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ANCIENT_DOOR_SCALE_MODEL,
        "Ancient Door Scale Model",
        715,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MODERN_DOOR_SCALE_MODEL,
        "Modern Door Scale Model",
        716,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RUSTY_BELLTOWER_KEY,
        "Rusty Belltower Key",
        717,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SURVEILLANCE_DEVICE,
        "Surveillance Device",
        718,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.SHINY_MEDALLION,
        "Shiny Medallion",
        719,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INK_COVERED_TEDDY_BEAR,
        "Ink-Covered Teddy Bear",
        720,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.DEATHS_CONTRACT,
        "Death's Contract",
        721,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MAKESHIFT_SOUL_KEY,
        "Makeshift Soul Key",
        722,
        ItemClassification.filler,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MYSTERIOUS_LOCKET,
        "Mysterious Locket",
        723,
        ItemClassification.progression,
        1,
        [ItemGroup.SHINY_THING],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Red Ancient Tablet of Knowledge",
        800,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Yellow Ancient Tablet of Knowledge",
        801,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Green Ancient Tablet of Knowledge",
        802,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Cyan Ancient Tablet of Knowledge",
        803,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Blue Ancient Tablet of Knowledge",
        804,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Purple Ancient Tablet of Knowledge",
        805,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PINK_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Pink Ancient Tablet of Knowledge",
        806,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.TABLET],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_BOMB_EXIT,
        "Lever-Bomb Exit",
        900,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SEWER,
        "Lever-Cemetery Sewer",
        901,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        "Lever-Guardian of the Door Access",
        902,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        "Lever-Cemetery Shortcut to East Tree",
        903,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EAST_TREE,
        "Lever-Cemetery East Tree",
        904,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_TOWER,
        "Lever-Catacombs Tower",
        905,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        "Lever-Cemetery Exit to Estate",
        906,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_CATACOMBS_EXIT,
        "Lever-Catacombs Exit",
        907,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_HOOKSHOT_SILENT_SERVANT,
        "Lever-Hookshot Silent Servant",
        908,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_UPPER,
        "Lever-Sailor Turncam Upper",
        909,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_TURNCAM_LOWER,
        "Lever-Sailor Turncam Lower",
        910,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_SAILOR_GREATSWORD_GATE,
        "Lever-Sailor Greatsword Gate",
        911,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        "Lever-Lockstone East Start Shortcut",
        912,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_ENTRANCE,
        "Lever-Lockstone Entrance",
        913,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_EAST_LOWER,
        "Lever-Lockstone East Lower",
        914,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        "Lever-Lockstone Upper Shortcut",
        915,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        "Lever-Lockstone Dual Laser Puzzle",
        916,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        "Lever-Lockstone Tracking Beam Puzzle",
        917,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        "Lever-Lockstone Vertical Laser Puzzle",
        918,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        "Lever-Lockstone North Puzzle",
        919,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_SHRINE,
        "Lever-Lockstone Shrine",
        920,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        "Lever-Lockstone Hookshot Puzzle",
        921,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        "Lever-Lockstone Upper Puzzle",
        922,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        "Lever-Lockstone Upper Dual Laser Puzzle",
        923,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        "Lever-Watchtowers Before Ice Arena",
        924,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        "Lever-Watchtowers After Ice Skating",
        925,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        "Lever-Watchtowers After Boomers",
        926,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_SETTLEMENT_GATE,
        "Lever-Ruins Settlement Gate",
        927,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        "Lever-Ruins Upper Dungeon Entrance",
        928,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        "Lever-Ruins Ladder Left of Lord of Doors Arena",
        929,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        "Lever-Ruins Entrance Ladder Shortcut",
        930,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_RUINS_MAIN_GATE,
        "Lever-Ruins Main Gate",
        931,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        "Lever-Dungeon Entrance Right Gate",
        932,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        "Lever-Dungeon Entrance Left Gate",
        933,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        "Lever-Dungeon Above Rightmost Crow",
        934,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BOMB,
        "Lever-Fortress Bomb",
        935,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_MAIN_GATE,
        "Lever-Fortress Main Gate",
        936,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        "Lever-Fortress Central Shortcut",
        937,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_STATUE,
        "Lever-Fortress Statue",
        938,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        "Lever-Fortress Watchtower Lower",
        939,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_BRIDGE,
        "Lever-Fortress Bridge",
        940,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_PRE_MAIN_GATE,
        "Lever-Fortress Pre-Main Gate",
        941,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        "Lever-Fortress Watchtower Upper",
        942,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_FORTRESS_NORTH_WEST,
        "Lever-Fortress North West",
        943,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_LEFT,
        "Lever-Estate Elevator Left",
        944,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_ELEVATOR_RIGHT,
        "Lever-Estate Elevator Right",
        945,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE,
        "Lever-Garden of Love",
        946,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_END,
        "Lever-Garden of Life End",
        947,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_PEACE,
        "Lever-Garden of Peace",
        948,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_JOY,
        "Lever-Garden of Joy",
        949,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        "Lever-Garden of Love Turncam",
        950,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        "Lever-Garden of Life Lanterns",
        951,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        "Lever-Estate Underground Urn Shed",
        952,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BIG_POT_ARENA,
        "Lever-Manor Big Pot Arena",
        953,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        "Lever-Manor Bookshelf Shortcut",
        954,
        ItemClassification.progression,
        1,
        [ItemGroup.LEVER],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GROVE_OF_SPIRITS_DOOR,
        "Grove of Spirits Door",
        1001,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.LOST_CEMETERY_DOOR,
        "Lost Cemetery Door",
        1002,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.STRANDED_SAILOR_DOOR,
        "Stranded Sailor Door",
        1003,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CASTLE_LOCKSTONE_DOOR,
        "Castle Lockstone Door",
        1004,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CAMP_OF_THE_FREE_CROWS_DOOR,
        "Camp of the Free Crows Door",
        1005,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OLD_WATCHTOWERS_DOOR,
        "Old Watchtowers Door",
        1006,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.BETTYS_LAIR_DOOR,
        "Betty's Lair Door",
        1007,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.OVERGROWN_RUINS_DOOR,
        "Overgrown Ruins Door",
        1008,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.MUSHROOM_DUNGEON_DOOR,
        "Mushroom Dungeon Door",
        1009,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.FLOODED_FORTRESS_DOOR,
        "Flooded Fortress Door",
        1010,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THRONE_OF_THE_FROG_KING_DOOR,
        "Throne of the Frog King Door",
        1011,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ESTATE_OF_THE_URN_WITCH_DOOR,
        "Estate of the Urn Witch Door",
        1012,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CERAMIC_MANOR_DOOR,
        "Ceramic Manor Door",
        1013,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.INNER_FURNACE_DOOR,
        "Inner Furnace Door",
        1014,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.THE_URN_WITCHS_LABORATORY_DOOR,
        "The Urn Witch's Laboratory Door",
        1015,
        ItemClassification.progression,
        1,
        [ItemGroup.DOOR],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_URN_WITCH,
        "Giant Soul of The Urn Witch",
        1200,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_THE_FROG_KING,
        "Giant Soul of The Frog King",
        1201,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.GIANT_SOUL_OF_BETTY,
        "Giant Soul of Betty",
        1202,
        ItemClassification.progression_skip_balancing,
        1,
        [ItemGroup.GIANT_SOUL],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        "Crow-Manor After Torch Puzzle",
        1100,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_IMP_LOFT,
        "Crow-Manor Imp Loft",
        1101,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_LIBRARY,
        "Crow-Manor Library",
        1102,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_MANOR_BEDROOM,
        "Crow-Manor Bedroom",
        1103,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_HALL,
        "Crow-Dungeon Hall",
        1104,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_WATER_ARENA,
        "Crow-Dungeon Water Arena",
        1105,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_COBWEB,
        "Crow-Dungeon Cobweb",
        1106,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_DUNGEON_RIGHTMOST,
        "Crow-Dungeon Rightmost",
        1107,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_EAST,
        "Crow-Lockstone East",
        1108,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST,
        "Crow-Lockstone West",
        1109,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_WEST_LOCKED,
        "Crow-Lockstone West Locked",
        1110,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.CROW_LOCKSTONE_SOUTH_WEST,
        "Crow-Lockstone South West",
        1111,
        ItemClassification.progression,
        1,
        [ItemGroup.LOST_CROW],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ROTATION_TRAP,
        "Rotation Trap",
        2000,
        ItemClassification.trap,
        0,
        [ItemGroup.TRAP],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.PLAYER_INVISIBILITY_TRAP,
        "Player Invisibility Trap",
        2001,
        ItemClassification.trap,
        0,
        [ItemGroup.TRAP],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.ENEMY_INVISIBILITY_TRAP,
        "Enemy Invisibility Trap",
        2002,
        ItemClassification.trap,
        0,
        [ItemGroup.TRAP],
    ),
    DeathsDoorItemData(
        DeathsDoorItemName.KNOCKBACK_TRAP,
        "Knockback Trap",
        2003,
        ItemClassification.trap,
        0,
        [ItemGroup.TRAP],
    ),
]


item_name_to_id: dict[str, int] = {data.name.value: data.item_id for data in item_table}


# Items can be grouped using their names to allow easy checking if any item
# from that group has been collected. Group names can also be used for !hint
def items_for_group(group: ItemGroup) -> set[str]:
    item_names = set()
    for data in item_table:
        if group in data.item_groups:
            item_names.add(data.name.value)
    return item_names


item_name_groups: dict[str, set[str]] = {}
for group in ItemGroup:
    item_name_groups[group.value] = items_for_group(group)
