from enum import Enum
from typing import NamedTuple

from .regions import DeathsDoorRegionName as R


class LocationGroup(Enum):
    SPELL = "Spell"
    WEAPON = "Weapon"
    GIANT_SOUL = "Giant Soul"
    SHRINE = "Shrine"
    SHINY_THING = "Shiny Thing"
    LIFE_SEED = "Life Seed"
    SOUL_ORB = "Soul Orb"
    TABLET = "Tablet"
    LEVER = "Lever"
    DOOR = "Door"
    KEY = "Key"
    LOST_CROW = "Lost Crow"
    NIGHT = "Night"
    AVARICE = "Avarice"


class DeathsDoorLocationName(str, Enum):
    def __str__(self) -> str:
        return self.value

    # Spells and their upgrades
    FIRE_AVARICE = "Hall of Doors - Fire Avarice (Ceramic Manor Ancient Door)"
    BOMB_AVARICE = "Hall of Doors - Bomb Avarice (Mushroom Dungeon Ancient Door)"
    HOOKSHOT_AVARICE = (
        "Hall of Doors - Hookshot Avarice (Castle Lockstone Ancient Door)"
    )
    FIRE_SILENT_SERVANT = "Crypt - Fire Silent Servant"
    BOMB_SILENT_SERVANT = "Lost Cemetery - East Tree Bridge Bomb Silent Servant"
    HOOKSHOT_SILENT_SERVANT = "Stranded Sailor Caves - Hookshot Silent Servant"
    ARROW_SILENT_SERVANT = "Lost Cemetery - Catacombs Arrow Silent Servant"

    # Weapons
    ROGUE_DAGGERS = "Estate of the Urn Witch - Garden of Life Rogue Daggers"
    DISCARDED_UMBRELLA = "Hall of Doors - Discarded Umbrella"
    REAPERS_GREATSWORD = "Stranded Sailor - Reaper's Greatsword"
    THUNDER_HAMMER = "Mushroom Dungeon - Thunder Hammer"

    # Giant Souls
    BETTY = "Betty's Lair - Betty Giant Soul"
    FROG_KING = "Throne of the Frog King - Frog King Giant Soul"
    GRANDMA = "The Urn Witch's Laboratory - Urn Witch Giant Soul"

    # Shrines
    HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE = (
        "Lost Cemetery - Behind Entrance Vitality Shard Shrine"
    )
    MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA = (
        "Lost Cemetery - After Smough Arena Magic Shard Shrine"
    )
    HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END = (
        "Lost Cemetery - Winding Bridge End Vitality Shard Shrine"
    )
    HEART_SHRINE_HOOKSHOT_ARENA = (
        "Stranded Sailor - Hookshot Arena Vitality Shard Shrine"
    )
    MAGIC_SHRINE_SAILOR_TURNCAM = "Stranded Sailor - Turncam Magic Shard Shrine"
    MAGIC_SHRINE_LOCKSTONE_SECRET_WEST = (
        "Castle Lockstone - Secret West Magic Shard Shrine"
    )
    HEART_SHRINE_CAMP_ICE_SKATING = (
        "Camp of the Free Crows - Ice Skating Vitality Shard Shrine"
    )
    MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA = (
        "Overgrown Ruins - Hookshot Arena Magic Shard Shrine"
    )
    MAGIC_SHRINE_RUINS_TURNCAM = "Overgrown Ruins - Turncam Magic Shard Shrine"
    HEART_SHRINE_DUNGEON_WATER_ARENA = (
        "Mushroom Dungeon - Water Arena Vitality Shard Shrine"
    )
    HEART_SHRINE_RUINS_SEWER = "Overgrown Ruins - Sewer Vitality Shard Shrine"
    MAGIC_SHRINE_FORTRESS_BOW_SECRET = (
        "Flooded Fortress - Bow Secret Magic Shard Shrine"
    )
    MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR = (
        "Estate of the Urn Witch - Left of Manor Magic Shard Shrine"
    )
    HEART_SHRINE_GARDEN_OF_LIFE = (
        "Estate of the Urn Witch - Garden of Life Vitality Shard Shrine"
    )
    MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE = (
        "Ceramic Manor - Bathroom Puzzle Magic Shard Shrine"
    )
    HEART_SHRINE_FURNACE_CART_PUZZLE = (
        "Furnace Observation Rooms - Cart Puzzle Vitality Shard Shrine"
    )

    # Shiny Things
    ENGAGEMENT_RING = "Ceramic Manor - Engagement Ring"
    OLD_COMPASS = "Lost Cemetery - Catacombs Old Compass"
    INCENSE = "Lost Cemetery - Summit Incense"
    UNDYING_BLOSSOM = "Lost Cemetery - Undying Blossom (in southeast Green Roof Tower)"
    OLD_PHOTOGRAPH = "Ceramic Manor - Old Photograph"
    SLUDGE_FILLED_URN = "Estate of the Urn Witch - Sludge-Filled Urn"
    TOKEN_OF_DEATH = "Stranded Sailor Caves - Token of Death"
    RUSTY_GARDEN_TROWEL = "Estate of the Urn Witch - Rusty Garden Trowel"
    CAPTAINS_LOG = "Stranded Sailor - Captain's Log"
    GIANT_ARROWHEAD = "Throne of the Frog King - Giant Arrowhead"
    MALFORMED_SEED = "Overgrown Ruins - Malformed Seed"
    CORRUPTED_ANTLER = "Mushroom Dungeon - Corrupted Antler"
    MAGICAL_FOREST_HORN = "Overgrown Ruins - Magical Forest Horn"
    ANCIENT_CROWN = "Castle Lockstone - Ancient Crown"
    GRUNTS_OLD_MASK = "Stranded Sailor - Grunt's Old Mask"
    ANCIENT_DOOR_SCALE_MODEL = "Hall of Doors - Ancient Door Scale Model"
    MODERN_DOOR_SCALE_MODEL = "Hall of Doors - Modern Door Scale Model"
    RUSTY_BELLTOWER_KEY = "Hall of Doors - Rusty Belltower Key (Beat Lord of Doors)"
    SURVEILLANCE_DEVICE = "Hall of Doors - Surveillance Device"
    SHINY_MEDALLION = "Camp of the Free Crows - Shiny Medallion"
    INK_COVERED_TEDDY_BEAR = "Stranded Sailor - Ink-Covered Teddy Bear"
    DEATHS_CONTRACT = "Castle Lockstone - Death's Contract"
    MAKESHIFT_SOUL_KEY = "Grove of Spirits - Makeshift Soul Key"
    MYSTERIOUS_LOCKET = "Old Watchtowers - Mysterious Locket"

    # Seeds
    SEED_CEMETERY_BROKEN_BRIDGE = "Lost Cemetery - Broken Bridge Life Seed"
    SEED_CATACOMBS_TOWER = "Lost Cemetery - Catacombs Tower Life Seed"
    SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE = (
        "Lost Cemetery - Left of Main Entrance Life Seed"
    )
    SEED_CEMETERY_NEAR_TABLET_GATE = "Lost Cemetery - Near Tablet Gate Life Seed"
    SEED_BETWEEN_CEMETERY_AND_SAILOR = (
        "Stranded Sailor Caves - Between Cemetery and Sailor Life Seed"
    )
    SEED_SAILOR_UPPER = "Stranded Sailor - Upper Life Seed"
    SEED_LOCKSTONE_UPPER_EAST = "Castle Lockstone - Upper East Life Seed"
    SEED_LOCKSTONE_SOUL_DOOR = "Castle Lockstone - Soul Door Life Seed"
    SEED_LOCKSTONE_BEHIND_BARS = "Castle Lockstone - Behind Bars Life Seed"
    SEED_LOCKSTONE_ENTRANCE_WEST = "Castle Lockstone - Northwest Life Seed (Under Boxes)"
    SEED_LOCKSTONE_NORTH = "Castle Lockstone - North Life Seed"
    SEED_CAMP_LEDGE_WITH_HUTS = "Camp of the Free Crows - Ledge With Huts Life Seed"
    SEED_CAMP_STALL = "Camp of the Free Crows - Stall Life Seed"
    SEED_CAMP_ROOFTOPS = "Camp of the Free Crows - Rooftops Life Seed"
    SEED_WATCHTOWERS_ICE_SKATING = "Old Watchtowers - Ice Skating Life Seed"
    SEED_WATCHTOWERS_TABLET_DOOR = "Old Watchtowers - Tablet Door Life Seed"
    SEED_WATCHTOWERS_ARCHER_PLATFORM = "Old Watchtowers - Archer Platform Life Seed"
    SEED_WATCHTOWERS_BOXES = "Old Watchtowers - Boxes Life Seed"
    SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA = (
        "Mushroom Dungeon - Fire Puzzle Near Water Arena Life Seed"
    )
    SEED_RUINS_LORD_OF_DOORS_ARENA = "Overgrown Ruins - Lord of Doors Arena Life Seed"
    SEED_RUINS_FIRE_PLANT_CORRIDOR = "Overgrown Ruins - Fire Plant Corridor Life Seed"
    SEED_DUNGEON_WATER_ARENA_LEFT_EXIT = (
        "Mushroom Dungeon - Water Arena Left Exit Life Seed"
    )
    SEED_RUINS_RIGHT_MIDDLE = "Overgrown Ruins - Right Middle Life Seed"
    SEED_RUINS_ON_SETTLEMENT_WALL = "Overgrown Ruins - On Settlement Wall Life Seed"
    SEED_RUINS_BEHIND_BOXES = "Overgrown Ruins - Behind Boxes Life Seed"
    SEED_RUINS_DOWN_THROUGH_BOMB_WALL = (
        "Overgrown Ruins - Down Through Bomb Wall Life Seed"
    )
    SEED_DUNGEON_ABOVE_RIGHTMOST_CROW = (
        "Mushroom Dungeon - Above Rightmost Crow Life Seed"
    )
    SEED_DUNGEON_RIGHT_ABOVE_KEY = "Mushroom Dungeon - Right Above Key Life Seed"
    SEED_DUNGEON_AVARICE_BRIDGE = "Mushroom Dungeon - Avarice Bridge Life Seed"
    SEED_FORTRESS_WATCHTOWER = "Flooded Fortress - Watchtower Life Seed"
    SEED_FORTRESS_STATUE = "Flooded Fortress - Statue Life Seed"
    SEED_FORTRESS_BRIDGE = "Flooded Fortress - Bridge Life Seed"
    SEED_FORTRESS_INTRO_CRATE = "Flooded Fortress - Intro Crate Life Seed"
    SEED_FORTRESS_EAST_AFTER_STATUE = "Flooded Fortress - East After Statue Life Seed"
    SEED_ESTATE_FAMILY_TOMB = "Estate of the Urn Witch - Family Tomb Life Seed"
    SEED_ESTATE_ENTRANCE = "Estate of the Urn Witch - Entrance Life Seed"
    SEED_ESTATE_HEDGE_GAPS = "Estate of the Urn Witch - Hedge Gaps Life Seed"
    SEED_GARDEN_OF_JOY = "Estate of the Urn Witch - Garden of Joy Life Seed"
    SEED_MANOR_BOXES = "Ceramic Manor - Boxes Life Seed"
    SEED_MANOR_NEAR_BRAZIER = "Ceramic Manor - Near Brazier Life Seed"
    SEED_MANOR_BELOW_BIG_POT_ARENA = "Ceramic Manor - Southmost Edge of Big Pot Arena Life Seed"
    SEED_MANOR_RAFTERS = "Ceramic Manor - Rafters Life Seed"
    SEED_MANOR_MAIN_ROOM_UPPER = "Ceramic Manor - Main Room Upper Life Seed"
    SEED_MANOR_SPINNY_POT_ROOM = "Ceramic Manor - Spinny Pot Room Life Seed"
    SEED_MANOR_LIBRARY_SHELF = "Ceramic Manor - Library Shelf Life Seed"
    SEED_CART_PUZZLE = "Furnace Observation Rooms - Cart Puzzle Life Seed"
    SEED_FURNACE_ENTRANCE = "Furnace Observation Rooms - Entrance Life Seed"
    SEED_INNER_FURNACE_HORIZONTAL_PISTONS = (
        "Inner Furnace - Horizontal Pistons Life Seed"
    )
    SEED_INNER_FURNACE_CONVEYOR_BRIDGE = "Inner Furnace - Conveyor Bridge Life Seed"
    SEED_INNER_FURNACE_CONVEYOR_GAUNTLET = "Inner Furnace - Conveyor Gauntlet Life Seed"

    # Soul Orbs
    SOUL_ORB_FIRE_RETURN_UPPER = "Hall of Doors - Fire Return Upper Soul Orb"
    SOUL_ORB_HOOKSHOT_SECRET = "Hall of Doors - Hookshot Secret Soul Orb"
    SOUL_ORB_BOMB_RETURN = "Hall of Doors - Bomb Return Soul Orb"
    SOUL_ORB_BOMB_SECRET = "Hall of Doors - Bomb Secret Soul Orb"
    SOUL_ORB_HOOKSHOT_RETURN = "Hall of Doors - Hookshot Return Soul Orb"
    SOUL_ORB_FIRE_RETURN_LOWER = "Hall of Doors - Fire Return Lower Soul Orb"
    SOUL_ORB_FIRE_SECRET = "Hall of Doors - Fire Secret Soul Orb"
    SOUL_ORB_CATACOMBS_EXIT = "Lost Cemetery - Catacombs Exit Soul Orb"
    SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS = "Lost Cemetery - Hookshot Towers Soul Orb"
    SOUL_ORB_CEMETERY_UNDER_BRIDGE = "Lost Cemetery - Under Bridge Soul Orb"
    SOUL_ORB_CEMETERY_EAST_TREE = "Lost Cemetery - East Tree Soul Orb"
    SOUL_ORB_CEMETERY_WINDING_BRIDGE_END = "Lost Cemetery - Winding Bridge End Soul Orb"
    SOUL_ORB_CATACOMBS_ROOM_2 = "Lost Cemetery - Catacombs Room 2 Soul Orb"
    SOUL_ORB_CATACOMBS_ROOM_1 = "Lost Cemetery - Catacombs Room 1 Soul Orb"
    SOUL_ORB_CEMETERY_GATED_SEWER = "Lost Cemetery - Gated Sewer Soul Orb"
    SOUL_ORB_CATACOMBS_ENTRANCE = "Lost Cemetery - Catacombs Entrance Soul Orb"
    SOUL_ORB_CEMETERY_CAVE = "Lost Cemetery - Cave Soul Orb"
    SOUL_ORB_SAILOR_TURNCAM = "Stranded Sailor - Turncam Soul Orb"
    SOUL_ORB_NORTH_LOCKSTONE_SEWER = "Castle Lockstone - North Sewer Soul Orb"
    SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH = "Castle Lockstone - Hookshot North Soul Orb"
    SOUL_ORB_LOCKSTONE_EXIT = "Castle Lockstone - Exit Soul Orb"
    SOUL_ORB_WEST_LOCKSTONE_SEWER = "Castle Lockstone - West Sewer Soul Orb"
    SOUL_ORB_CAMP_ROOFTOPS = "Camp of the Free Crows - Rooftops Soul Orb"
    SOUL_ORB_CAMP_BROKEN_BRIDGE = "Camp of the Free Crows - Broken Bridge Soul Orb"
    SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR = (
        "Old Watchtowers - Behind Barb Elevator Soul Orb"
    )
    SOUL_ORB_DUNGEON_VINE = "Mushroom Dungeon - Vine Soul Orb"
    SOUL_ORB_RUINS_STUMP = "Overgrown Ruins - Stump Soul Orb"
    SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT = (
        "Overgrown Ruins - Outside Left Dungeon Exit Soul Orb"
    )
    SOUL_ORB_DUNGEON_COBWEB = "Mushroom Dungeon - Cobweb Soul Orb"
    SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR = (
        "Overgrown Ruins - Left After Key Door Soul Orb"
    )
    SOUL_ORB_RUINS_LOWER_BOMB_WALL = "Overgrown Ruins - Lower Bomb Wall Soul Orb"
    SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT = (
        "Overgrown Ruins - Lord of Doors Arena Hookshot Soul Orb"
    )
    SOUL_ORB_DUNGEON_LOWER_ENTRANCE = "Mushroom Dungeon - Lower Entrance Soul Orb"
    SOUL_ORB_RUINS_UPPER_ABOVE_HORN = "Overgrown Ruins - Upper Above Horn Soul Orb"
    SOUL_ORB_RUINS_ABOVE_THREE_PLANTS = "Overgrown Ruins - Above Three Plants Soul Orb"
    SOUL_ORB_RUINS_UP_TURNCAM_LADDER = "Overgrown Ruins - Up Turncam Ladder Soul Orb"
    SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE = (
        "Overgrown Ruins - Above Entrance Gate Soul Orb"
    )
    SOUL_ORB_RUINS_UPPER_BOMB_WALL = "Overgrown Ruins - Upper Bomb Wall Soul Orb"
    SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF = "Mushroom Dungeon - Left Exit Shelf Soul Orb"
    SOUL_ORB_RUINS_LOWER_HOOKSHOT = "Overgrown Ruins - Lower Hookshot Soul Orb"
    SOUL_ORB_FORTRESS_BOMB = "Flooded Fortress - Bomb Soul Orb"
    SOUL_ORB_FORTRESS_HIDDEN_SEWER = "Flooded Fortress - Hidden Sewer Soul Orb"
    SOUL_ORB_FORTRESS_DROP = "Flooded Fortress - Drop Soul Orb"
    SOUL_ORB_ESTATE_ACCESS_CRYPT = "Crypt - Soul Orb"
    SOUL_ORB_ESTATE_BALCONY = "Estate of the Urn Witch - Balcony Soul Orb"
    SOUL_ORB_GARDEN_OF_LOVE_TURNCAM = (
        "Estate of the Urn Witch - Garden of Love Turncam Soul Orb"
    )
    SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP = (
        "Estate of the Urn Witch - Garden of Life Hookshot Loop Soul Orb"
    )
    SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS = (
        "Estate of the Urn Witch - Garden of Love Bomb Walls Soul Orb"
    )
    SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL = (
        "Estate of the Urn Witch - Garden of Life Bomb Wall Soul Orb"
    )
    SOUL_ORB_ESTATE_BROKEN_BOARDWALK = (
        "Estate of the Urn Witch - Broken Boardwalk Soul Orb"
    )
    SOUL_ORB_ESTATE_SECRET_CAVE = "Estate of the Urn Witch - Secret Cave Soul Orb"
    SOUL_ORB_ESTATE_TWIN_BENCHES = "Estate of the Urn Witch - Twin Benches Soul Orb"
    SOUL_ORB_ESTATE_SEWER_MIDDLE = "Estate of the Urn Witch - Sewer Middle Soul Orb"
    SOUL_ORB_ESTATE_SEWER_END = "Estate of the Urn Witch - Sewer End Soul Orb"
    SOUL_ORB_GARDEN_OF_PEACE = "Estate of the Urn Witch - Garden of Peace Soul Orb"
    SOUL_ORB_MANOR_IMP_LOFT = "Ceramic Manor - Imp Loft Soul Orb"
    SOUL_ORB_MANOR_LIBRARY_SHELF = "Ceramic Manor - Library Shelf Soul Orb"
    SOUL_ORB_MANOR_CHANDELIER = "Ceramic Manor - Chandelier Soul Orb"
    SOUL_ORB_FURNACE_LANTERN_CHAIN = (
        "Furnace Observation Rooms - Lantern Chain Soul Orb"
    )
    SOUL_ORB_SMALL_ROOM = "Furnace Observation Rooms - Small Room Soul Orb"
    SOUL_ORB_FURNACE_ENTRANCE_SEWER = (
        "Furnace Observation Rooms - Entrance Sewer Soul Orb"
    )

    # Tablets
    RED_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Flooded Fortress - Red Ancient Tablet of Knowledge (Jefferson)"
    )
    YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Overgrown Ruins - Yellow Ancient Tablet of Knowledge (Avarice)"
    )
    GREEN_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Estate of the Urn Witch - Green Ancient Tablet of Knowledge (Life Seeds)"
    )
    CYAN_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Lost Cemetery - Cyan Ancient Tablet of Knowledge (Lord Ghosts)"
    )
    BLUE_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Old Watchtowers - Blue Ancient Tablet of Knowledge (Light Torches)"
    )
    PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE = (
        "Lost Cemetery - Purple Ancient Tablet of Knowledge (The Grave Digger)"
    )
    ESTATE_OWL = "Estate of the Urn Witch - Owl"
    RUINS_OWL = "Overgrown Ruins - Owl"
    WATCHTOWERS_OWL = "Old Watchtowers - Owl"

    # Levers
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
    LEVER_LOCKSTONE_WEST_UPPER = "Castle Lockstone - West Upper Lever"
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
    LEVER_ESTATE_ELEVATOR_LEFT = "Crypt - Elevator Left Lever"
    LEVER_ESTATE_ELEVATOR_RIGHT = "Crypt - Elevator Right Lever"
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

    # Doors
    GROVE_OF_SPIRITS_DOOR = "Grove of Spirits - Door"
    LOST_CEMETERY_DOOR = "Lost Cemetery - Door"
    STRANDED_SAILOR_DOOR = "Stranded Sailor - Door"
    CASTLE_LOCKSTONE_DOOR = "Castle Lockstone - Door"
    CAMP_OF_THE_FREE_CROWS_DOOR = "Camp of the Free Crows - Door"
    OLD_WATCHTOWERS_DOOR = "Old Watchtowers - Door"
    BETTYS_LAIR_DOOR = "Betty's Lair - Door"
    OVERGROWN_RUINS_DOOR = "Overgrown Ruins - Door"
    MUSHROOM_DUNGEON_DOOR = "Mushroom Dungeon - Door"
    FLOODED_FORTRESS_DOOR = "Flooded Fortress - Door"
    THRONE_OF_THE_FROG_KING_DOOR = "Throne of the Frog King - Door"
    ESTATE_OF_THE_URN_WITCH_DOOR = "Estate of the Urn Witch - Door"
    CERAMIC_MANOR_DOOR = "Ceramic Manor - Door"
    INNER_FURNACE_DOOR = "Inner Furnace - Door"
    THE_URN_WITCHS_LABORATORY_DOOR = "The Urn Witch's Laboratory - Door"

    # Keys
    KEY_CEMETERY_CENTRAL = "Lost Cemetery - Central Key"
    KEY_CEMETERY_GREY_CROW = "Lost Cemetery - Grey Crow Key"
    KEY_CAMP_OF_THE_FREE_CROWS = "Camp of the Free Crows - Key"
    KEY_LOCKSTONE_WEST = "Castle Lockstone - West Key"
    KEY_LOCKSTONE_NORTH = "Castle Lockstone - North Key"
    KEY_OVERGROWN_RUINS = "Overgrown Ruins - Key"
    KEY_DUNGEON_HALL = "Mushroom Dungeon - Hall Key"
    KEY_DUNGEON_RIGHT = "Mushroom Dungeon - Right Key"
    KEY_DUNGEON_NEAR_WATER_ARENA = "Mushroom Dungeon - Near Water Arena Key"
    KEY_MANOR_UNDER_DINING_ROOM = "Ceramic Manor - Under Dining Room Key"
    KEY_MANOR_AFTER_SPINNY_POT_ROOM = "Ceramic Manor - After Spinny Pot Room Key"
    KEY_MANOR_LIBRARY = "Ceramic Manor - Library Key"

    # Crow Souls
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


class DeathsDoorLocationData(NamedTuple):
    name: DeathsDoorLocationName
    mod_string: str
    location_id: int
    region: R
    location_groups: list[LocationGroup]


location_table: list[DeathsDoorLocationData] = [
    # Spells and their upgrades
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_AVARICE,
        "Fire Avarice",
        200,
        R.FIRE_AVARICE,
        [LocationGroup.SPELL, LocationGroup.AVARICE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_AVARICE,
        "Bomb Avarice",
        210,
        R.BOMB_AVARICE,
        [LocationGroup.SPELL, LocationGroup.AVARICE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_AVARICE,
        "Hookshot Avarice",
        220,
        R.HOOKSHOT_AVARICE,
        [LocationGroup.SPELL, LocationGroup.AVARICE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FIRE_SILENT_SERVANT,
        "Fire Silent Servant",
        201,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BOMB_SILENT_SERVANT,
        "Bomb Silent Servant",
        211,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HOOKSHOT_SILENT_SERVANT,
        "Hookshot Silent Servant",
        221,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.SPELL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ARROW_SILENT_SERVANT,
        "Arrow Silent Servant",
        230,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SPELL],
    ),
    # Weapons
    DeathsDoorLocationData(
        DeathsDoorLocationName.ROGUE_DAGGERS,
        "Rogue Daggers",
        301,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DISCARDED_UMBRELLA,
        "Discarded Umbrella",
        302,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.REAPERS_GREATSWORD,
        "Reaper's Greatsword",
        303,
        R.STRANDED_SAILOR,
        [LocationGroup.WEAPON],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THUNDER_HAMMER,
        "Thunder Hammer",
        304,
        R.MUSHROOM_DUNGEON_THUNDER_HAMMER,
        [LocationGroup.WEAPON],
    ),
    # Giant Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTY,
        "Betty",
        1200,
        R.BETTYS_LAIR,
        [LocationGroup.GIANT_SOUL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FROG_KING,
        "Frog King",
        1201,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.GIANT_SOUL],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRANDMA,
        "Grandma",
        1202,
        R.URN_WITCHS_LABORATORY,
        [LocationGroup.GIANT_SOUL],
    ),
    # Shrines
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE,
        "Heart Shrine-Cemetery Behind Entrance",
        400,
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA,
        "Magic Shrine-Cemetery After Smough Arena",
        450,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CEMETERY_WINDING_BRIDGE_END,
        "Heart Shrine-Cemetery Winding Bridge End",
        401,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_HOOKSHOT_ARENA,
        "Heart Shrine-Hookshot Arena",
        402,
        R.STRANDED_SAILOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_SAILOR_TURNCAM,
        "Magic Shrine-Sailor Turncam",
        451,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_LOCKSTONE_SECRET_WEST,
        "Magic Shrine-Lockstone Secret West",
        452,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_CAMP_ICE_SKATING,
        "Heart Shrine-Camp Ice Skating",
        403,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA,
        "Magic Shrine-Ruins Hookshot Arena",
        453,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_RUINS_TURNCAM,
        "Magic Shrine-Ruins Turncam",
        454,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_DUNGEON_WATER_ARENA,
        "Heart Shrine-Dungeon Water Arena",
        404,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_RUINS_SEWER,
        "Heart Shrine-Ruins Sewer",
        405,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_FORTRESS_BOW_SECRET,
        "Magic Shrine-Fortress Bow Secret",
        455,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_ESTATE_LEFT_OF_MANOR,
        "Magic Shrine-Estate Left of Manor",
        456,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_GARDEN_OF_LIFE,
        "Heart Shrine-Garden of Life",
        406,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGIC_SHRINE_MANOR_BATHROOM_PUZZLE,
        "Magic Shrine-Manor Bathroom Puzzle",
        457,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SHRINE],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.HEART_SHRINE_FURNACE_CART_PUZZLE,
        "Heart Shrine-Furnace Cart Puzzle",
        407,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SHRINE],
    ),
    # Shiny Things
    DeathsDoorLocationData(
        DeathsDoorLocationName.ENGAGEMENT_RING,
        "Engagement Ring",
        700,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_COMPASS,
        "Old Compass",
        701,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INCENSE,
        "Incense",
        702,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.UNDYING_BLOSSOM,
        "Undying Blossom",
        703,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_PHOTOGRAPH,
        "Old Photograph",
        704,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SLUDGE_FILLED_URN,
        "Sludge-Filled Urn",
        705,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.TOKEN_OF_DEATH,
        "Token of Death",
        706,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_GARDEN_TROWEL,
        "Rusty Garden Trowel",
        707,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAPTAINS_LOG,
        "Captain's Log",
        708,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GIANT_ARROWHEAD,
        "Giant Arrowhead",
        709,
        R.THRONE_OF_THE_FROG_KING,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MALFORMED_SEED,
        "Malformed Seed",
        710,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CORRUPTED_ANTLER,
        "Corrupted Antler",
        711,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAGICAL_FOREST_HORN,
        "Magical Forest Horn",
        712,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_CROWN,
        "Ancient Crown",
        713,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GRUNTS_OLD_MASK,
        "Grunt's Old Mask",
        714,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ANCIENT_DOOR_SCALE_MODEL,
        "Ancient Door Scale Model",
        715,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MODERN_DOOR_SCALE_MODEL,
        "Modern Door Scale Model",
        716,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUSTY_BELLTOWER_KEY,
        "Rusty Belltower Key",
        717,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SURVEILLANCE_DEVICE,
        "Surveillance Device",
        718,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SHINY_MEDALLION,
        "Shiny Medallion",
        719,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INK_COVERED_TEDDY_BEAR,
        "Ink-Covered Teddy Bear",
        720,
        R.STRANDED_SAILOR,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.DEATHS_CONTRACT,
        "Death's Contract",
        721,
        R.CASTLE_LOCKSTONE_LIBRARY,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MAKESHIFT_SOUL_KEY,
        "Makeshift Soul Key",
        722,
        R.GROVE_OF_SPIRITS,
        [LocationGroup.SHINY_THING],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MYSTERIOUS_LOCKET,
        "Mysterious Locket",
        723,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        [LocationGroup.SHINY_THING, LocationGroup.NIGHT],
    ),
    # Seeds
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_BROKEN_BRIDGE,
        "Seed-Cemetery Broken Bridge",
        100,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CATACOMBS_TOWER,
        "Seed-Catacombs Tower",
        101,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_LEFT_OF_MAIN_ENTRANCE,
        "Seed-Cemetery Left of Main Entrance",
        102,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CEMETERY_NEAR_TABLET_GATE,
        "Seed-Cemetery Near Tablet Gate",
        103,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_BETWEEN_CEMETERY_AND_SAILOR,
        "Seed-Between Cemetery and Sailor",
        104,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_SAILOR_UPPER,
        "Seed-Sailor Upper",
        105,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_UPPER_EAST,
        "Seed-Lockstone Upper East",
        106,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_SOUL_DOOR,
        "Seed-Lockstone Soul Door",
        107,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_BEHIND_BARS,
        "Seed-Lockstone Behind Bars",
        108,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_ENTRANCE_WEST,
        "Seed-Lockstone Entrance West",
        109,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_LOCKSTONE_NORTH,
        "Seed-Lockstone North",
        110,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_LEDGE_WITH_HUTS,
        "Seed-Camp Ledge With Huts",
        111,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_STALL,
        "Seed-Camp Stall",
        112,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CAMP_ROOFTOPS,
        "Seed-Camp Rooftops",
        113,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ICE_SKATING,
        "Seed-Watchtowers Ice Skating",
        114,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_TABLET_DOOR,
        "Seed-Watchtowers Tablet Door",
        115,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_ARCHER_PLATFORM,
        "Seed-Watchtowers Archer Platform",
        116,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_WATCHTOWERS_BOXES,
        "Seed-Watchtowers Boxes",
        117,
        R.OLD_WATCHTOWERS_JAMMING_START,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_FIRE_PUZZLE_NEAR_WATER_ARENA,
        "Seed-Dungeon Fire Puzzle Near Water Arena",
        118,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_LORD_OF_DOORS_ARENA,
        "Seed-Ruins Lord of Doors Arena",
        119,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_FIRE_PLANT_CORRIDOR,
        "Seed-Ruins Fire Plant Corridor",
        120,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_WATER_ARENA_LEFT_EXIT,
        "Seed-Dungeon Water Arena Left Exit",
        121,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_RIGHT_MIDDLE,
        "Seed-Ruins Right Middle",
        122,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_ON_SETTLEMENT_WALL,
        "Seed-Ruins On Settlement Wall",
        123,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_BEHIND_BOXES,
        "Seed-Ruins Behind Boxes",
        124,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_RUINS_DOWN_THROUGH_BOMB_WALL,
        "Seed-Ruins Down Through Bomb Wall",
        125,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_ABOVE_RIGHTMOST_CROW,
        "Seed-Dungeon Above Rightmost Crow",
        126,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_RIGHT_ABOVE_KEY,
        "Seed-Dungeon Right Above Key",
        127,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_DUNGEON_AVARICE_BRIDGE,
        "Seed-Dungeon Avarice Bridge",
        128,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_WATCHTOWER,
        "Seed-Fortress Watchtower",
        129,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_STATUE,
        "Seed-Fortress Statue",
        130,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_BRIDGE,
        "Seed-Fortress Bridge",
        131,
        R.FLOODED_FORTRESS_BRIDGE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_INTRO_CRATE,
        "Seed-Fortress Intro Crate",
        132,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FORTRESS_EAST_AFTER_STATUE,
        "Seed-Fortress East After Statue",
        133,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_FAMILY_TOMB,
        "Seed-Estate Family Tomb",
        134,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_ENTRANCE,
        "Seed-Estate Entrance",
        135,
        R.ESTATE_OF_THE_URN_WITCH_ENTRANCE,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_ESTATE_HEDGE_GAPS,
        "Seed-Estate Hedge Gaps",
        136,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_GARDEN_OF_JOY,
        "Seed-Garden of Joy",
        137,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BOXES,
        "Seed-Manor Boxes",
        138,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_NEAR_BRAZIER,
        "Seed-Manor Near Brazier",
        139,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_BELOW_BIG_POT_ARENA,
        "Seed-Manor Below Big Pot Arena",
        140,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_RAFTERS,
        "Seed-Manor Rafters",
        141,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_MAIN_ROOM_UPPER,
        "Seed-Manor Main Room Upper",
        142,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_SPINNY_POT_ROOM,
        "Seed-Manor Spinny Pot Room",
        143,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_MANOR_LIBRARY_SHELF,
        "Seed-Manor Library Shelf",
        144,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_CART_PUZZLE,
        "Seed-Cart Puzzle",
        145,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_FURNACE_ENTRANCE,
        "Seed-Furnace Entrance",
        146,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_HORIZONTAL_PISTONS,
        "Seed-Inner Furnace Horizontal Pistons",
        147,
        R.INNER_FURNACE_POST_BURNER_6,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_BRIDGE,
        "Seed-Inner Furnace Conveyor Bridge",
        148,
        R.INNER_FURNACE_POST_BURNER_3,
        [LocationGroup.LIFE_SEED],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SEED_INNER_FURNACE_CONVEYOR_GAUNTLET,
        "Seed-Inner Furnace Conveyor Gauntlet",
        149,
        R.INNER_FURNACE_POST_BURNER_7,
        [LocationGroup.LIFE_SEED],
    ),
    # Soul Orbs
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_UPPER,
        "Soul Orb-Fire Return Upper",
        500,
        R.POST_FIRE_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_SECRET,
        "Soul Orb-Hookshot Secret",
        501,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_RETURN,
        "Soul Orb-Bomb Return",
        502,
        R.POST_BOMB_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_BOMB_SECRET,
        "Soul Orb-Bomb Secret",
        503,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_HOOKSHOT_RETURN,
        "Soul Orb-Hookshot Return",
        504,
        R.POST_HOOKSHOT_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_RETURN_LOWER,
        "Soul Orb-Fire Return Lower",
        505,
        R.POST_FIRE_AVARICE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FIRE_SECRET,
        "Soul Orb-Fire Secret",
        506,
        R.HALL_OF_DOORS_LOBBY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_EXIT,
        "Soul Orb-Catacombs Exit",
        507,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS,
        "Soul Orb-Cemetery Hookshot Towers",
        508,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_UNDER_BRIDGE,
        "Soul Orb-Cemetery Under Bridge",
        509,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_EAST_TREE,
        "Soul Orb-Cemetery East Tree",
        510,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_WINDING_BRIDGE_END,
        "Soul Orb-Cemetery Winding Bridge End",
        511,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_2,
        "Soul Orb-Catacombs Room 2",
        512,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ROOM_1,
        "Soul Orb-Catacombs Room 1",
        513,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_GATED_SEWER,
        "Soul Orb-Cemetery Gated Sewer",
        514,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CATACOMBS_ENTRANCE,
        "Soul Orb-Catacombs Entrance",
        515,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CEMETERY_CAVE,
        "Soul Orb-Cemetery Cave",
        516,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SAILOR_TURNCAM,
        "Soul Orb-Sailor Turncam",
        517,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_NORTH_LOCKSTONE_SEWER,
        "Soul Orb-North Lockstone Sewer",
        518,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH,
        "Soul Orb-Lockstone Hookshot North",
        519,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_LOCKSTONE_EXIT,
        "Soul Orb-Lockstone Exit",
        520,
        R.CASTLE_LOCKSTONE_ROOF,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WEST_LOCKSTONE_SEWER,
        "Soul Orb-West Lockstone Sewer",
        521,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_ROOFTOPS,
        "Soul Orb-Camp Rooftops",
        522,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_CAMP_BROKEN_BRIDGE,
        "Soul Orb-Camp Broken Bridge",
        523,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_WATCHTOWERS_BEHIND_BARB_ELEVATOR,
        "Soul Orb-Watchtowers Behind Barb Elevator",
        524,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_VINE,
        "Soul Orb-Dungeon Vine",
        525,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_STUMP,
        "Soul Orb-Ruins Stump",
        526,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_OUTSIDE_LEFT_DUNGEON_EXIT,
        "Soul Orb-Ruins Outside Left Dungeon Exit",
        527,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SOUL_ORB],
    ),  ## TODO: What region should this really be in???
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_COBWEB,
        "Soul Orb-Dungeon Cobweb",
        528,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LEFT_AFTER_KEY_DOOR,
        "Soul Orb-Ruins Left After Key Door",
        529,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_BOMB_WALL,
        "Soul Orb-Ruins Lower Bomb Wall",
        530,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT,
        "Soul Orb-Ruins Lord of Doors Arena Hookshot",
        531,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LOWER_ENTRANCE,
        "Soul Orb-Dungeon Lower Entrance",
        532,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.SOUL_ORB],
    ),  # TODO: Currently, this soul orb is in a Overgrown Ruins region despite being in Mushroom Dungeon
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_ABOVE_HORN,
        "Soul Orb-Ruins Upper Above Horn",
        533,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_THREE_PLANTS,
        "Soul Orb-Ruins Above Three Plants",
        534,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UP_TURNCAM_LADDER,
        "Soul Orb-Ruins Up Turncam Ladder",
        535,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE,
        "Soul Orb-Ruins Above Entrance Gate",
        536,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_UPPER_BOMB_WALL,
        "Soul Orb-Ruins Upper Bomb Wall",
        537,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_DUNGEON_LEFT_EXIT_SHELF,
        "Soul Orb-Dungeon Left Exit Shelf",
        538,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_RUINS_LOWER_HOOKSHOT,
        "Soul Orb-Ruins Lower Hookshot",
        539,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_BOMB,
        "Soul Orb-Fortress Bomb",
        540,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_HIDDEN_SEWER,
        "Soul Orb-Fortress Hidden Sewer",
        541,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FORTRESS_DROP,
        "Soul Orb-Fortress Drop",
        542,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_ACCESS_CRYPT,
        "Soul Orb-Estate Access Crypt",
        543,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BALCONY,
        "Soul Orb-Estate Balcony",
        544,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_TURNCAM,
        "Soul Orb-Garden of Love Turncam",
        545,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP,
        "Soul Orb-Garden of Life Hookshot Loop",
        546,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS,
        "Soul Orb-Garden of Love Bomb Walls",
        547,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_LIFE_BOMB_WALL,
        "Soul Orb-Garden of Life Bomb Wall",
        548,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_BROKEN_BOARDWALK,
        "Soul Orb-Estate Broken Boardwalk",
        549,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SECRET_CAVE,
        "Soul Orb-Estate Secret Cave",
        550,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_TWIN_BENCHES,
        "Soul Orb-Estate Twin Benches",
        551,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_MIDDLE,
        "Soul Orb-Estate Sewer Middle",
        552,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_ESTATE_SEWER_END,
        "Soul Orb-Estate Sewer End",
        553,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_GARDEN_OF_PEACE,
        "Soul Orb-Garden of Peace",
        554,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_IMP_LOFT,
        "Soul Orb-Manor Imp Loft",
        555,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_LIBRARY_SHELF,
        "Soul Orb-Manor Library Shelf",
        556,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_MANOR_CHANDELIER,
        "Soul Orb-Manor Chandelier",
        557,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_LANTERN_CHAIN,
        "Soul Orb-Furnace Lantern Chain",
        558,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_SMALL_ROOM,
        "Soul Orb-Small Room",
        559,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.SOUL_ORB_FURNACE_ENTRANCE_SEWER,
        "Soul Orb-Furnace Entrance Sewer",
        560,
        R.FURNACE_OBSERVATION_ROOMS,
        [LocationGroup.SOUL_ORB],
    ),
    # Tablets
    DeathsDoorLocationData(
        DeathsDoorLocationName.RED_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Red Ancient Tablet of Knowledge",
        800,
        R.FLOODED_FORTRESS_ENTRANCE_JEFFERSON,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Yellow Ancient Tablet of Knowledge",
        801,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Green Ancient Tablet of Knowledge",
        802,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.TABLET],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Cyan Ancient Tablet of Knowledge",
        803,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Blue Ancient Tablet of Knowledge",
        804,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE,
        "Purple Ancient Tablet of Knowledge",
        805,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OWL,
        "Estate Owl",
        806,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.RUINS_OWL,
        "Ruins Owl",
        807,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.WATCHTOWERS_OWL,
        "Watchtowers Owl",
        808,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.TABLET, LocationGroup.NIGHT],
    ),
    # Levers
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_BOMB_EXIT,
        "Lever-Bomb Exit",
        900,
        R.POST_BOMB_AVARICE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SEWER,
        "Lever-Cemetery Sewer",
        901,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS,
        "Lever-Guardian of the Door Access",
        902,
        R.LOST_CEMETERY_RIGHT_ARENA,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE,
        "Lever-Cemetery Shortcut to East Tree",
        903,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,  ##TODO: CHECK IF ROUTE FROM RIGHT ARENA OR EXIT TO RUINS IS DISTINCT
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EAST_TREE,
        "Lever-Cemetery East Tree",
        904,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_TOWER,
        "Lever-Catacombs Tower",
        905,
        R.LOST_CEMETERY_STEADHONE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CEMETERY_EXIT_TO_ESTATE,
        "Lever-Cemetery Exit to Estate",
        906,
        R.LOST_CEMETERY_BELLTOWER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_CATACOMBS_EXIT,
        "Lever-Catacombs Exit",
        907,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_HOOKSHOT_SILENT_SERVANT,
        "Lever-Hookshot Silent Servant",
        908,
        R.STRANDED_SAILOR_CAVES,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_UPPER,
        "Lever-Sailor Turncam Upper",
        909,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_TURNCAM_LOWER,
        "Lever-Sailor Turncam Lower",
        910,
        R.STRANDED_SAILOR_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_SAILOR_GREATSWORD_GATE,
        "Lever-Sailor Greatsword Gate",
        911,
        R.STRANDED_SAILOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_EAST_START_SHORTCUT,
        "Lever-Lockstone East Start Shortcut",
        912,
        R.CASTLE_LOCKSTONE_LIBRARY,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_ENTRANCE,
        "Lever-Lockstone Entrance",
        913,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_WEST_UPPER,
        "Lever-Lockstone East Lower",
        914,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_SHORTCUT,
        "Lever-Lockstone Upper Shortcut",
        915,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE,
        "Lever-Lockstone Dual Laser Puzzle",
        916,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        "Lever-Lockstone Tracking Beam Puzzle",
        917,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
        "Lever-Lockstone Vertical Laser Puzzle",
        918,
        R.CASTLE_LOCKSTONE_EAST,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_NORTH_PUZZLE,
        "Lever-Lockstone North Puzzle",
        919,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_SHRINE,
        "Lever-Lockstone Shrine",
        920,
        R.CASTLE_LOCKSTONE_JAILED_SEED,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE,
        "Lever-Lockstone Hookshot Puzzle",
        921,
        R.CASTLE_LOCKSTONE_SOUTHWEST_UPPER,  ##TODO: CHECK IF THIS SEPARATELY NEEDS HOOKSHOT TOO?
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_PUZZLE,
        "Lever-Lockstone Upper Puzzle",
        922,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE,
        "Lever-Lockstone Upper Dual Laser Puzzle",
        923,
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA,
        "Lever-Watchtowers Before Ice Arena",
        924,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_ICE_SKATING,
        "Lever-Watchtowers After Ice Skating",
        925,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_WATCHTOWERS_AFTER_BOOMERS,
        "Lever-Watchtowers After Boomers",
        926,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_SETTLEMENT_GATE,
        "Lever-Ruins Settlement Gate",
        927,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE,
        "Lever-Ruins Upper Dungeon Entrance",
        928,
        R.MUSHROOM_DUNGEON_MAIN_HALL,  ### TODO: Check if this is actually in ruins (if so, may need a new region)
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_LADDER_LEFT_OF_LORD_OF_DOORS_ARENA,
        "Lever-Ruins Ladder Left of Lord of Doors Arena",
        929,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT,
        "Lever-Ruins Entrance Ladder Shortcut",
        930,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_RUINS_MAIN_GATE,
        "Lever-Ruins Main Gate",
        931,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE,
        "Lever-Dungeon Entrance Right Gate",
        932,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ENTRANCE_LEFT_GATE,
        "Lever-Dungeon Entrance Left Gate",
        933,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW,
        "Lever-Dungeon Above Rightmost Crow",
        934,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BOMB,
        "Lever-Fortress Bomb",
        935,
        R.FLOODED_FORTRESS_U_TURN,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_MAIN_GATE,
        "Lever-Fortress Main Gate",
        936,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_CENTRAL_SHORTCUT,
        "Lever-Fortress Central Shortcut",
        937,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_STATUE,
        "Lever-Fortress Statue",
        938,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_LOWER,
        "Lever-Fortress Watchtower Lower",
        939,
        R.FLOODED_FORTRESS_ENTRANCE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_BRIDGE,
        "Lever-Fortress Bridge",
        940,
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_PRE_MAIN_GATE,
        "Lever-Fortress Pre-Main Gate",
        941,
        R.FLOODED_FORTRESS_PRE_MAIN_GATE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_WATCHTOWER_UPPER,
        "Lever-Fortress Watchtower Upper",
        942,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_FORTRESS_NORTH_WEST,
        "Lever-Fortress North West",
        943,
        R.FLOODED_FORTRESS_BRIDGE,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_LEFT,
        "Lever-Estate Elevator Left",
        944,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_ELEVATOR_RIGHT,
        "Lever-Estate Elevator Right",
        945,
        R.CRYPT_MAIN_ROOM,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE,
        "Lever-Garden of Love",
        946,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_END,
        "Lever-Garden of Life End",
        947,
        R.ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_PEACE,
        "Lever-Garden of Peace",
        948,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_JOY,
        "Lever-Garden of Joy",
        949,
        R.ESTATE_OF_THE_URN_WITCH_SOUTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LOVE_TURNCAM,
        "Lever-Garden of Love Turncam",
        950,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_GARDEN_OF_LIFE_LANTERNS,
        "Lever-Garden of Life Lanterns",
        951,
        R.ESTATE_OF_THE_URN_WITCH_NORTH,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_ESTATE_UNDERGROUND_URN_SHED,
        "Lever-Estate Underground Urn Shed",
        952,
        R.ESTATE_OF_THE_URN_WITCH_URN_SHED,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BIG_POT_ARENA,
        "Lever-Manor Big Pot Arena",
        953,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LEVER],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LEVER_MANOR_BOOKSHELF_SHORTCUT,
        "Lever-Manor Bookshelf Shortcut",
        954,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.LEVER],
    ),
    # Doors
    DeathsDoorLocationData(
        DeathsDoorLocationName.GROVE_OF_SPIRITS_DOOR,
        "Grove of Spirits Door",
        1001,
        R.DOOR_CHECK_FOR_GROVE_OF_SPIRITS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.LOST_CEMETERY_DOOR,
        "Lost Cemetery Door",
        1002,
        R.DOOR_CHECK_FOR_LOST_CEMETERY,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.STRANDED_SAILOR_DOOR,
        "Stranded Sailor Door",
        1003,
        R.DOOR_CHECK_FOR_STRANDED_SAILOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CASTLE_LOCKSTONE_DOOR,
        "Castle Lockstone Door",
        1004,
        R.DOOR_CHECK_FOR_CASTLE_LOCKSTONE,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CAMP_OF_THE_FREE_CROWS_DOOR,
        "Camp of the Free Crows Door",
        1005,
        R.DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OLD_WATCHTOWERS_DOOR,
        "Old Watchtowers Door",
        1006,
        R.DOOR_CHECK_FOR_OLD_WATCHTOWERS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.BETTYS_LAIR_DOOR,
        "Betty's Lair Door",
        1007,
        R.DOOR_CHECK_FOR_BETTYS_LAIR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.OVERGROWN_RUINS_DOOR,
        "Overgrown Ruins Door",
        1008,
        R.DOOR_CHECK_FOR_OVERGROWN_RUINS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.MUSHROOM_DUNGEON_DOOR,
        "Mushroom Dungeon Door",
        1009,
        R.DOOR_CHECK_FOR_MUSHROOM_DUNGEON,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.FLOODED_FORTRESS_DOOR,
        "Flooded Fortress Door",
        1010,
        R.DOOR_CHECK_FOR_FLOODED_FORTRESS,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THRONE_OF_THE_FROG_KING_DOOR,
        "Throne of the Frog King Door",
        1011,
        R.DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.ESTATE_OF_THE_URN_WITCH_DOOR,
        "Estate of the Urn Witch Door",
        1012,
        R.DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CERAMIC_MANOR_DOOR,
        "Ceramic Manor Door",
        1013,
        R.DOOR_CHECK_FOR_CERAMIC_MANOR,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.INNER_FURNACE_DOOR,
        "Inner Furnace Door",
        1014,
        R.DOOR_CHECK_FOR_INNER_FURNACE,
        [LocationGroup.DOOR],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.THE_URN_WITCHS_LABORATORY_DOOR,
        "The Urn Witch's Laboratory Door",
        1015,
        R.DOOR_CHECK_FOR_URN_WITCHS_LABORATORY,
        [LocationGroup.DOOR],
    ),
    # Keys
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_CENTRAL,
        "Key-Cemetery Central",
        600,
        R.LOST_CEMETERY_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CEMETERY_GREY_CROW,
        "Key-Cemetery Grey Crow",
        601,
        R.LOST_CEMETERY_SUMMIT,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_CAMP_OF_THE_FREE_CROWS,
        "Key-Camp of the Free Crows",
        602,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_WEST,
        "Key-Lockstone West",
        603,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_LOCKSTONE_NORTH,
        "Key-Lockstone North",
        604,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_OVERGROWN_RUINS,
        "Key-Overgrown Ruins",
        610,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_HALL,
        "Key-Dungeon Hall",
        611,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_RIGHT,
        "Key-Dungeon Right",
        612,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_DUNGEON_NEAR_WATER_ARENA,
        "Key-Dungeon Near Water Arena",
        613,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_UNDER_DINING_ROOM,
        "Key-Manor Under Dining Room",
        620,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_AFTER_SPINNY_POT_ROOM,
        "Key-Manor After Spinny Pot Room",
        621,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.KEY],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.KEY_MANOR_LIBRARY,
        "Key-Manor Library",
        622,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.KEY],
    ),
    # Crow Souls
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_AFTER_TORCH_PUZZLE,
        "Crow-Manor After Torch Puzzle",
        1100,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_IMP_LOFT,
        "Crow-Manor Imp Loft",
        1101,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_LIBRARY,
        "Crow-Manor Library",
        1102,
        R.CERAMIC_MANOR_LIBRARY,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_MANOR_BEDROOM,
        "Crow-Manor Bedroom",
        1103,
        R.CERAMIC_MANOR_LEFT,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_HALL,
        "Crow-Dungeon Hall",
        1104,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_WATER_ARENA,
        "Crow-Dungeon Water Arena",
        1105,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_COBWEB,
        "Crow-Dungeon Cobweb",
        1106,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_DUNGEON_RIGHTMOST,
        "Crow-Dungeon Rightmost",
        1107,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_EAST,
        "Crow-Lockstone East",
        1108,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST,
        "Crow-Lockstone West",
        1109,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_WEST_LOCKED,
        "Crow-Lockstone West Locked",
        1110,
        R.CASTLE_LOCKSTONE_CENTRAL,
        [LocationGroup.LOST_CROW],
    ),
    DeathsDoorLocationData(
        DeathsDoorLocationName.CROW_LOCKSTONE_SOUTH_WEST,
        "Crow-Lockstone South West",
        1111,
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW,
        [LocationGroup.LOST_CROW],
    ),
]


def locations_for_group(group: LocationGroup) -> set[str]:
    location_names: set[str] = set()
    for data in location_table:
        if group in data.location_groups:
            location_names.add(data.name.value)
    return location_names


location_name_to_id: dict[str, int] = {
    data.name.value: data.location_id for data in location_table
}

location_name_groups: dict[str, set[str]] = {}
for loc_data in location_table:
    loc_group_name = loc_data.name.value.split(" - ", 1)[0]
    location_name_groups.setdefault(loc_group_name, set()).add(loc_data.name.value)

for group in LocationGroup:
    location_name_groups[group.name] = locations_for_group(group)
