from enum import Enum


class DeathsDoorRegionName(str, Enum):
    def __str__(self) -> str:
        return self.value

    # Hall of Doors Regions
    HALL_OF_DOORS_LOBBY = "Hall of Doors Lobby"
    DOOR_TO_GROVE_OF_SPIRITS = "Door to Grove of Spirits"
    DOOR_TO_LOST_CEMETERY = "Door to Lost Cemetery"
    DOOR_TO_ESTATE_OF_THE_URN_WITCH = "Door to Estate of the Urn Witch"
    DOOR_TO_CERAMIC_MANOR = "Door to Ceramic Manor"
    DOOR_TO_INNER_FURNACE = "Door to Inner Furnace"
    DOOR_TO_URN_WITCHS_LABORATORY = "Door to the Urn Witch's Laboratory"
    DOOR_TO_OVERGROWN_RUINS = "Door to Overgrown Ruins"
    DOOR_TO_MUSHROOM_DUNGEON = "Door to Mushroom Dungeon"
    DOOR_TO_FLOODED_FORTRESS = "Door to Flooded Fortress"
    DOOR_TO_THRONE_OF_THE_FROG_KING = "Door to Throne of the Frog King"
    DOOR_TO_STRANDED_SAILOR = "Door to Stranded Sailor"
    DOOR_TO_CASTLE_LOCKSTONE = "Door to Castle Lockstone"
    DOOR_TO_CAMP_OF_THE_FREE_CROWS = "Door to Camp of the Free Crows"
    DOOR_TO_OLD_WATCHTOWERS = "Door to Old Watchtowers"
    DOOR_TO_BETTYS_LAIR = "Door to Betty's Lair"
    FIRE_AVARICE = "Fire Avarice"
    POST_FIRE_AVARICE = "Post Fire Avarice"
    HOOKSHOT_AVARICE = "Hookshot Avarice"
    POST_HOOKSHOT_AVARICE = "Post Hookshot Avarice"
    BOMB_AVARICE = "Bomb Avarice"
    POST_BOMB_AVARICE = "Post Bomb Avarice"

    # Door Check regions
    # need to be connected to from both Hall of Doors region and region where door would appear in the world to provide access to the door check without giving logical access to the world region (future proofing for entrance rando)
    DOOR_CHECK_FOR_GROVE_OF_SPIRITS = "Door Check For Grove of Spirits"
    DOOR_CHECK_FOR_LOST_CEMETERY = "Door Check for Lost Cemetery"
    DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH = "Door Check for Estate of the Urn Witch"
    DOOR_CHECK_FOR_CERAMIC_MANOR = "Door Check for Ceramic Manor"
    DOOR_CHECK_FOR_INNER_FURNACE = "Door Check for Inner Furnace"
    DOOR_CHECK_FOR_URN_WITCHS_LABORATORY = "Door Check for Urn Witch's Laboratory"
    DOOR_CHECK_FOR_OVERGROWN_RUINS = "Door Check for Overgrown Ruins"
    DOOR_CHECK_FOR_MUSHROOM_DUNGEON = "Door Check for Mushroom Dungeon"
    DOOR_CHECK_FOR_FLOODED_FORTRESS = "Door Check for Flooded Fortress"
    DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING = "Door Check for Throne of the Frog King"
    DOOR_CHECK_FOR_STRANDED_SAILOR = "Door Check for Stranded Sailor"
    DOOR_CHECK_FOR_CASTLE_LOCKSTONE = "Door Check for Castle Lockstone"
    DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS = "Door Check for Camp of the Free Crows"
    DOOR_CHECK_FOR_OLD_WATCHTOWERS = "Door Check for Old Watchtowers"
    DOOR_CHECK_FOR_BETTYS_LAIR = "Door Check for Betty's Lair"

    # Grove of Spirits Regions
    GROVE_OF_SPIRITS = "Grove of Spirits"
    GROVE_OF_SPIRITS_DOOR = "Grove of Spirits Door"
    GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY = "Grove of Spirits Exit to Lost Cemetery"

    # Lost Cemetery Regions
    LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS = "Lost Cemetery Exit to Grove of Spirits"
    LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR = (
        "Lost Cemetery Near Grove of Spirits Door"
    )
    LOST_CEMETERY_DOOR = "Lost Cemetery Door"
    LOST_CEMETERY_CENTRAL = "Lost Cemetery Central"
    LOST_CEMETERY_STEADHONE = "Lost Cemetery Steadhone"
    LOST_CEMETERY_RIGHT_ARENA = "Lost Cemetery Right Arena"
    LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS = "Lost Cemetery Exit to Overgrown Ruins"
    LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR = (
        "Lost Cemetery Near Exit to Stranded Sailor"
    )
    LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR_CAVES = "Lost Cemetery Exit to Stranded Sailor Caves"
    LOST_CEMETERY_EXIT_TO_CRYPT = "Lost Cemetery Exit to Crypt"
    LOST_CEMETERY_BELLTOWER = "Lost Cemetery Belltower"
    LOST_CEMETERY_CATACOMBS_ROOM_1 = "Lost Cemetery Catacombs"
    LOST_CEMETERY_EAST_TREE_BRIDGE = "Lost Cemetery East Tree Bridge"
    LOST_CEMETERY_SUMMIT = "Lost Cemetery Summit"

    # Crypt Regions
    CRYPT_EXIT_TO_LOST_CEMETERY = "Crypt Exit to Lost Cemetery"
    CRYPT_MAIN_ROOM = "Crypt Main Room"
    CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH = "Crypt Exit to Estate of the Urn Witch"

    # Estate of Urn Witch Regions
    ESTATE_OF_THE_URN_WITCH_DOOR = "Estate of the Urn Witch Door"
    ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT = "Estate of the Urn Witch Exit to Crypt"
    ESTATE_OF_THE_URN_WITCH_ENTRANCE = "Estate of the Urn Witch Entrance"
    ESTATE_OF_THE_URN_WITCH_SOUTH = "Estate of the Urn Witch South"
    ESTATE_OF_THE_URN_WITCH_NORTH = "Estate of the Urn Witch North"
    ESTATE_OF_THE_URN_WITCH_URN_SHED = "Estate of the Urn Witch Urn Shed"
    ESTATE_OF_THE_URN_WITCH_GARDEN_OF_LIFE_END = (
        "Estate of the Urn Witch Garden of Life End"
    )
    ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR = (
        "Estate of the Urn Witch Exit to Ceramic Manor"
    )

    # Ceramic Manor
    CERAMIC_MANOR_DOOR = "Ceramic Manor Door"
    CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH = (
        "Ceramic Manor Exit to Estate of the Urn Witch"
    )
    CERAMIC_MANOR_MAIN_LOBBY = "Ceramic Manor Main Lobby"
    CERAMIC_MANOR_LEFT = "Ceramic Manor Left"
    CERAMIC_MANOR_LIBRARY = "Ceramic Manor Library"
    CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS = (
        "Ceramic Manor Exit to Furnace Observation Rooms"
    )
    CERAMIC_MANOR_ANCIENT_DOOR = "Ceramic Manor Ancient Door"

    # Furnace Observation Rooms Regions
    FURNACE_OBSERVATION_ROOMS = "Furnace Observation Rooms"
    FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR = (
        "Furnace Observation Rooms Exit to Ceramic Manor"
    )
    FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE = (
        "Furnace Observation Rooms Exit to Inner Furnace"
    )

    # Inner Furnace Regions
    INNER_FURNACE_DOOR = "Inner Furnace Door"
    INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS = (
        "Inner Furnace Exit to Furnace Observation Rooms"
    )
    INNER_FURNACE_ENTRANCE = "Inner Furnace Entrance"
    INNER_FURNACE_POST_BURNER_1 = "Inner Furnace Post Burner 1"
    INNER_FURNACE_POST_BURNER_2 = "Inner Furnace Post Burner 2"
    INNER_FURNACE_POST_BURNER_3 = "Inner Furnace Post Burner 3"
    INNER_FURNACE_POST_BURNER_4 = "Inner Furnace Post Burner 4"
    INNER_FURNACE_POST_BURNER_5 = "Inner Furnace Post Burner 5"
    INNER_FURNACE_POST_BURNER_6 = "Inner Furnace Post Burner 6"
    INNER_FURNACE_POST_BURNER_7 = "Inner Furnace Post Burner 7"
    INNER_FURNACE_POST_BURNER_8 = "Inner Furnace Post Burner 8"
    INNER_FURNACE_POST_BURNER_9 = "Inner Furnace Post Burner 9"
    INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY = (
        "Inner Furnace Exit to the Urn Witch's Laboratory"
    )

    # The Urn Witch's Laborator Regions
    URN_WITCHS_LABORATORY = "The Urn Witch's Laboratory"
    URN_WITCHS_LABORATORY_DOOR = "The Urn Witch's Laboratory Door"
    URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE = (
        "The Urn Witch's Laboratory Exit to Inner Furnace"
    )

    # Overgrown Ruins Regions
    OVERGROWN_RUINS_DOOR = "Overgrown Ruins Door"
    OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY = "Overgrown Ruins Exit to Lost Cemetery"
    OVERGROWN_RUINS_OUTSIDE_FRONT_GATE = "Overgrown Ruins Outside Front Gate"
    OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE = (
        "Overgrown Ruins Outside Main Dungeon Gate"
    )
    OVERGROWN_RUINS_FOREST_SETTLEMENT = "Overgrown Ruins Forest Settlement"
    # OVERGROWN_RUINS_EXIT_TO_MUSHROOM_DUNGEON_MAIN = "Overgrown Ruins Exit to Mushroom Dungeon Main" ## TODO: right now, not handling all the different entrances to mushroom dungeon

    # Mushroom Dungeon Regions
    MUSHROOM_DUNGEON_DOOR = "Mushroom Dungeon Door"
    # MUSHROOM_DUNGEON_EXIT_TO_OVERGROWN_RUINS_MAIN = "Mushroom Dungeon Exit to Overgrown Ruins Main Gate"
    MUSHROOM_DUNGEON_MAIN_HALL = "Mushroom Dungeon Main Hall"
    MUSHROOM_DUNGEON_ANCIENT_DOOR = "Mushroom Dungeon Ancient Door"
    MUSHROOM_DUNGEON_RIGHTMOST_CROW = "Mushroom Dungeon Rightmost Crow"
    MUSHROOM_DUNGEON_LOBBY = "Mushroom Dungeon Lobby"
    MUSHROOM_DUNGEON_BIG_DOOR = "Mushroom Dungeon Big Door"
    MUSHROOM_DUNGEON_WATER_ARENA = "Mushroom Dungeon Water Arena"
    MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS = (
        "Mushroom Dungeon Exit to Flooded Fortress"
    )
    MUSHROOM_DUNGEON_THUNDER_HAMMER = "Mushroom Dungeon Thunder Hammer Drop In"

    # Flooded Fortress Regions
    FLOODED_FORTRESS_DOOR = "Flooded Fortress Door"
    FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON = (
        "Flooded Fortress Exit to Mushroom Dungeon"
    )
    FLOODED_FORTRESS_ENTRANCE = "Flooded Fortress Entrance"
    FLOODED_FORTRESS_ENTRANCE_JEFFERSON = "Flooded Fortress Entrance (Jefferson)"
    FLOODED_FORTRESS_WATCHTOWER_LOWER = "Flooded Fortress Watchtower Lower"
    FLOODED_FORTRESS_FROG_KING_STATUE = "Flooded Fortress Frog King Statue"
    FLOODED_FORTRESS_PRE_MAIN_GATE = "Flooded Fortress Pre-Main Gate"
    FLOODED_FORTRESS_FROG_KING_ENCOUNTER = "Flooded Fortress Frog King Encounter"
    FLOODED_FORTRESS_INSIDE_MAIN_GATE = "Flooded Fortress Inside Main Gate"
    FLOODED_FORTRESS_U_TURN = "Flooded Fortress U Turn"
    FLOODED_FORTRESS_BREAKABLE_BRIDGES = "Flooded Fortress Breakable Bridges"
    FLOODED_FORTRESS_BRIDGE = "Flooded Fortress Bridge"
    FLOODED_FORTRESS_EXIT = "Flooded Fortress Exit"
    FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING = (
        "Flooded Fortress Exit to Throne of the Frog King"
    )

    # Throne of the Frog King Regions
    THRONE_OF_THE_FROG_KING = "Throne of the Frog King"
    THRONE_OF_THE_FROG_KING_DOOR = "Throne of the Frog King Door"
    THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS = (
        "Throne of the Frog King Exit to Flooded Fortress"
    )

    # Stranded Sailor Regions
    STRANDED_SAILOR = "Stranded Sailor"
    STRANDED_SAILOR_DOOR = "Stranded Sailor Door"
    STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES = (
        "Stranded Sailor Exit to Stranded Sailor Caves"
    )
    STRANDED_SAILOR_UPPER = "Stranded Sailor Upper"
    STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE = (
        "Stranded Sailor Exit to Castle Lockstone"
    )

    STRANDED_SAILOR_CAVES = "Stranded Sailor Caves"
    STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY = (
        "Stranded Sailor Caves Exit to Lost Cemetery"
    )
    STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR = (
        "Stranded Sailor Caves Exit to Stranded Sailor"
    )

    # Castle Lockstone Regions
    CASTLE_LOCKSTONE_DOOR = "Castle Lockstone Door"
    CASTLE_LOCKSTONE_ANCIENT_DOOR = "Castle Lockstone Ancient Door"
    CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR = (
        "Castle Lockstone Exit to Stranded Sailor"
    )
    CASTLE_LOCKSTONE_ENTRANCE = "Castle Lockstone Entrance"
    CASTLE_LOCKSTONE_CENTRAL = "Castle Lockstone Central"
    CASTLE_LOCKSTONE_SOUTHWEST_UPPER = "Castle Lockstone Southwest Upper"
    CASTLE_LOCKSTONE_SOUTHWEST_CROW = "Castle Lockstone Southwest Crow"
    CASTLE_LOCKSTONE_EAST = "Castle Lockstone East"
    CASTLE_LOCKSTONE_EAST_UPPER = "Castle Lockstone East Upper"
    CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR = "Castle Lockstone East Upper Keyed Door"
    CASTLE_LOCKSTONE_JAILED_SEED = "Castle Lockstone Jailed Seed"
    CASTLE_LOCKSTONE_LIBRARY = "Castle Lockstone Library"
    CASTLE_LOCKSTONE_ROOF = "Castle Lockstone Roof"
    CASTLE_LOCKSTONE_EXIT_TO_CAMP = (
        "Castle Lockstone Exit to Camp of the Free Crows"
    )
    CASTLE_LOCKSTONE_LORD_LOCKSTONE = "Castle Lockstone Lord Lockstone's Grave"
    CASTLE_LOCKSTONE_LORD_OPENGATE = "Castle Lockstone Lord Opengate's Grave"
    CASTLE_LOCKSTONE_LORD_DEADBOLT = "Castle Lockstone Lord Deadbolt's Grave"
    CASTLE_LOCKSTONE_LORD_THEODOOR = "Castle Lockstone Lord Theodoor's Grave"
    CASTLE_LOCKSTONE_EAST_CROW = "Castle Lockstone East Crow"

    # Camp of the Free Crows Regions
    CAMP_OF_THE_FREE_CROWS_DOOR = "Camp of the Free Crows Door"
    CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE = (
        "Camp of the Free Crows Exit to Castle Lockstone"
    )
    CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE = "Camp of the Free Crows Camp Bridge"
    CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR = "Camp of the Free Crows Castle Door"
    CAMP_OF_THE_FREE_CROWS_VILLAGE = "Camp of the Free Crows Village"
    CAMP_OF_THE_FREE_CROWS_ELEVATOR = "Camp of the Free Crows Elevator"
    CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS = (
        "Camp of the Free Crows Exit to Old Watchtowers"
    )

    # Old Watchtowers Regions
    OLD_WATCHTOWERS_DOOR = "Old Watchtowers Door"
    OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS = (
        "Old Watchtowers Exit to Camp of the Free Crows"
    )
    OLD_WATCHTOWERS_ENTRANCE = "Old Watchtowers Entrance"
    OLD_WATCHTOWERS_JAMMING_START = "Old Watchtowers Jamming Start"
    OLD_WATCHTOWERS_FIRST_POT_AREA = "Old Watchtowers First Pot Area"
    OLD_WATCHTOWERS_BARB_ELEVATOR = "Old Watchtowers Barb Elevator"
    OLD_WATCHTOWERS_LASERS_ARENA = "Old Watchtowers Lasers Arena"
    OLD_WATCHTOWERS_ICE_SKATING_START = "Old Watchtowers Ice Skating Start"
    OLD_WATCHTOWERS_ICE_SKATING_END = "Old Watchtowers Ice Skating End"
    OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS = "Old Watchtowers Headless Lord of Doors"
    OLD_WATCHTOWERS_CAVE_ENTRANCE = "Old Watchtowers Cave Entrance"
    OLD_WATCHTOWERS_BOOMERS = "Old Watchtowers Boomers"
    OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR = "Old Watchtowers Exit to Betty's Lair"

    # Betty's Lair Regions
    BETTYS_LAIR = "Betty's Lair"
    BETTYS_LAIR_DOOR = "Betty's Lair Door"
    BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS = "Betty's Lair Exit to Old Watchtowers"

no_jefferson_regions: list[DeathsDoorRegionName] = [
    # Hall of Doors Regions and Door Check Regions
    DeathsDoorRegionName.HALL_OF_DOORS_LOBBY,
    DeathsDoorRegionName.DOOR_TO_GROVE_OF_SPIRITS,
    DeathsDoorRegionName.DOOR_TO_LOST_CEMETERY,
    DeathsDoorRegionName.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
    DeathsDoorRegionName.DOOR_TO_CERAMIC_MANOR,
    DeathsDoorRegionName.DOOR_TO_INNER_FURNACE,
    DeathsDoorRegionName.DOOR_TO_URN_WITCHS_LABORATORY,
    DeathsDoorRegionName.DOOR_TO_OVERGROWN_RUINS,
    DeathsDoorRegionName.DOOR_TO_MUSHROOM_DUNGEON,
    DeathsDoorRegionName.DOOR_TO_FLOODED_FORTRESS,
    DeathsDoorRegionName.DOOR_TO_THRONE_OF_THE_FROG_KING,
    DeathsDoorRegionName.DOOR_TO_STRANDED_SAILOR,
    DeathsDoorRegionName.DOOR_TO_CASTLE_LOCKSTONE,
    DeathsDoorRegionName.DOOR_TO_CAMP_OF_THE_FREE_CROWS,
    DeathsDoorRegionName.DOOR_TO_OLD_WATCHTOWERS,
    DeathsDoorRegionName.DOOR_TO_BETTYS_LAIR,
    DeathsDoorRegionName.FIRE_AVARICE,
    DeathsDoorRegionName.POST_FIRE_AVARICE,
    DeathsDoorRegionName.HOOKSHOT_AVARICE,
    DeathsDoorRegionName.POST_HOOKSHOT_AVARICE,
    DeathsDoorRegionName.BOMB_AVARICE,
    DeathsDoorRegionName.POST_BOMB_AVARICE,
    DeathsDoorRegionName.DOOR_CHECK_FOR_GROVE_OF_SPIRITS,
    DeathsDoorRegionName.DOOR_CHECK_FOR_LOST_CEMETERY,
    DeathsDoorRegionName.DOOR_CHECK_FOR_ESTATE_OF_THE_URN_WITCH,
    DeathsDoorRegionName.DOOR_CHECK_FOR_CERAMIC_MANOR,
    DeathsDoorRegionName.DOOR_CHECK_FOR_INNER_FURNACE,
    DeathsDoorRegionName.DOOR_CHECK_FOR_URN_WITCHS_LABORATORY,
    DeathsDoorRegionName.DOOR_CHECK_FOR_OVERGROWN_RUINS,
    DeathsDoorRegionName.DOOR_CHECK_FOR_MUSHROOM_DUNGEON,
    DeathsDoorRegionName.DOOR_CHECK_FOR_FLOODED_FORTRESS,
    DeathsDoorRegionName.DOOR_CHECK_FOR_THRONE_OF_THE_FROG_KING,
    DeathsDoorRegionName.DOOR_CHECK_FOR_STRANDED_SAILOR,
    DeathsDoorRegionName.DOOR_CHECK_FOR_CASTLE_LOCKSTONE,
    DeathsDoorRegionName.DOOR_CHECK_FOR_CAMP_OF_THE_FREE_CROWS,
    DeathsDoorRegionName.DOOR_CHECK_FOR_OLD_WATCHTOWERS,
    DeathsDoorRegionName.DOOR_CHECK_FOR_BETTYS_LAIR,
]