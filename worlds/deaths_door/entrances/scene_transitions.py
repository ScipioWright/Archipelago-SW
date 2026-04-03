from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAll
from ..items import DeathsDoorItemName as I
from ..events import DeathsDoorEventName as E
from ..regions import DeathsDoorRegionName as R

two_way_scene_transitions: list[
    tuple[DeathsDoorEntrance, DeathsDoorEntrance | None]
] = [
    #########################
    ### SCENE TRANSITIONS ### (Separated for Entrance Rando purposes)
    #########################
    (
        DeathsDoorEntrance(
            R.DOOR_TO_GROVE_OF_SPIRITS,
            R.GROVE_OF_SPIRITS_DOOR,
            Has(I.GROVE_OF_SPIRITS_DOOR),
            "Hall of Doors Grove of Spirits Door",
            "sdoor_tutorial",
            "lvl_Tutorial",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.GROVE_OF_SPIRITS_DOOR,
            R.DOOR_TO_GROVE_OF_SPIRITS,
            Has(I.GROVE_OF_SPIRITS_DOOR),
            "Grove of Spirits Door",
            "sdoor_tutorial",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_LOST_CEMETERY,
            R.LOST_CEMETERY_DOOR,
            Has(I.LOST_CEMETERY_DOOR),
            "Hall of Doors Lost Cemetery Door",
            "sdoor_graveyard",
            "lvl_Graveyard",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.LOST_CEMETERY_DOOR,
            R.DOOR_TO_LOST_CEMETERY,
            Has(I.LOST_CEMETERY_DOOR),
            "Lost Cemetery Door",
            "sdoor_graveyard",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
            R.ESTATE_OF_THE_URN_WITCH_DOOR,
            Has(I.ESTATE_OF_THE_URN_WITCH_DOOR),
            "Hall of Doors Estate of the Urn Witch Door",
            "sdoor_gardens",
            "lvl_GrandmaGardens",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.ESTATE_OF_THE_URN_WITCH_DOOR,
            R.DOOR_TO_ESTATE_OF_THE_URN_WITCH,
            Has(I.ESTATE_OF_THE_URN_WITCH_DOOR),
            "Estate of the Urn Witch Door",
            "sdoor_gardens",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_CERAMIC_MANOR,
            R.CERAMIC_MANOR_DOOR,
            Has(I.CERAMIC_MANOR_DOOR),
            "Hall of Doors Ceramic Manor Door",
            "sdoor_mansion",
            "lvl_GrandmaMansion",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.CERAMIC_MANOR_DOOR,
            R.DOOR_TO_CERAMIC_MANOR,
            Has(I.CERAMIC_MANOR_DOOR),
            "Ceramic Manor Door",
            "sdoor_mansion",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_INNER_FURNACE,
            R.INNER_FURNACE_DOOR,
            Has(I.INNER_FURNACE_DOOR),
            "Hall of Doors Inner Furnace Door",
            "sdoor_basementromp",
            "lvl_GrandmaBasement",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.INNER_FURNACE_DOOR,
            R.DOOR_TO_INNER_FURNACE,
            Has(I.INNER_FURNACE_DOOR),
            "Inner Furnace Door",
            "sdoor_basementromp",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_URN_WITCHS_LABORATORY,
            R.URN_WITCHS_LABORATORY_DOOR,
            Has(I.THE_URN_WITCHS_LABORATORY_DOOR),
            "Hall of Doors The Urn Witch's Laboratory Door",
            "sdoor_grandmaboss",
            "boss_grandma",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.URN_WITCHS_LABORATORY_DOOR,
            R.DOOR_TO_URN_WITCHS_LABORATORY,
            Has(I.THE_URN_WITCHS_LABORATORY_DOOR),
            "The Urn Witch's Laboratory Door",
            "sdoor_grandmaboss",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_OVERGROWN_RUINS,
            R.OVERGROWN_RUINS_DOOR,
            Has(I.OVERGROWN_RUINS_DOOR),
            "Hall of Doors Overgrown Ruins Door",
            "sdoor_forest",
            "lvl_Forest",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.OVERGROWN_RUINS_DOOR,
            R.DOOR_TO_OVERGROWN_RUINS,
            Has(I.OVERGROWN_RUINS_DOOR),
            "Overgrown Ruins Door",
            "sdoor_forest",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_MUSHROOM_DUNGEON,
            R.MUSHROOM_DUNGEON_DOOR,
            Has(I.MUSHROOM_DUNGEON_DOOR),
            "Hall of Doors Mushroom Dungeon Door",
            "sdoor_forest_dung",
            "lvl_Forest",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.MUSHROOM_DUNGEON_DOOR,
            R.DOOR_TO_MUSHROOM_DUNGEON,
            Has(I.MUSHROOM_DUNGEON_DOOR),
            "Mushroom Dungeon Door",
            "sdoor_forest_dung",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_FLOODED_FORTRESS,
            R.FLOODED_FORTRESS_DOOR,
            Has(I.FLOODED_FORTRESS_DOOR),
            "Hall of Doors Flooded Fortress Door",
            "sdoor_swamp",
            "lvl_Swamp",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.FLOODED_FORTRESS_DOOR,
            R.DOOR_TO_FLOODED_FORTRESS,
            Has(I.FLOODED_FORTRESS_DOOR),
            "Flooded Fortress Door",
            "sdoor_swamp",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_THRONE_OF_THE_FROG_KING,
            R.THRONE_OF_THE_FROG_KING_DOOR,
            Has(I.THRONE_OF_THE_FROG_KING_DOOR),
            "Hall of Doors Throne of the Frog King Door",
            "sdoor_frogboss",
            "boss_frog",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.THRONE_OF_THE_FROG_KING_DOOR,
            R.DOOR_TO_THRONE_OF_THE_FROG_KING,
            Has(I.THRONE_OF_THE_FROG_KING_DOOR),
            "Throne of the Frog King Door",
            "sdoor_frogboss",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_STRANDED_SAILOR,
            R.STRANDED_SAILOR_DOOR,
            Has(I.STRANDED_SAILOR_DOOR),
            "Hall of Doors Stranded Sailor Door",
            "sdoor_sailor",
            "lvl_SailorMountain",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.STRANDED_SAILOR_DOOR,
            R.DOOR_TO_STRANDED_SAILOR,
            Has(I.STRANDED_SAILOR_DOOR),
            "Stranded Sailor Door",
            "sdoor_sailor",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_CASTLE_LOCKSTONE,
            R.CASTLE_LOCKSTONE_DOOR,
            Has(I.CASTLE_LOCKSTONE_DOOR),
            "Hall of Doors Castle Lockstone Door",
            "sdoor_fortress",
            "lvl_frozenfortress",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.CASTLE_LOCKSTONE_DOOR,
            R.DOOR_TO_CASTLE_LOCKSTONE,
            Has(I.CASTLE_LOCKSTONE_DOOR),
            "Castle Lockstone Door",
            "sdoor_fortress",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_CAMP_OF_THE_FREE_CROWS,
            R.CAMP_OF_THE_FREE_CROWS_DOOR,
            Has(I.CAMP_OF_THE_FREE_CROWS_DOOR),
            "Hall of Doors Camp of the Free Crows Door",
            "sdoor_covenant",
            "lvlConnect_Fortress_Mountaintops",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.CAMP_OF_THE_FREE_CROWS_DOOR,
            R.DOOR_TO_CAMP_OF_THE_FREE_CROWS,
            Has(I.CAMP_OF_THE_FREE_CROWS_DOOR),
            "Camp of the Free Crows Door",
            "sdoor_covenant",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_OLD_WATCHTOWERS,
            R.OLD_WATCHTOWERS_DOOR,
            Has(I.OLD_WATCHTOWERS_DOOR),
            "Hall of Doors Old Watchtowers Door",
            "sdoor_mountaintops",
            "lvl_Mountaintops",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.OLD_WATCHTOWERS_DOOR,
            R.DOOR_TO_OLD_WATCHTOWERS,
            Has(I.OLD_WATCHTOWERS_DOOR),
            "Old Watchtowers Door",
            "sdoor_mountaintops",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.DOOR_TO_BETTYS_LAIR,
            R.BETTYS_LAIR_DOOR,
            Has(I.BETTYS_LAIR_DOOR),
            "Hall of Doors Betty's Lair Door",
            "sdoor_betty",
            "boss_betty",
            no_jefferson=True,
        ),
        DeathsDoorEntrance(
            R.BETTYS_LAIR_DOOR,
            R.DOOR_TO_BETTYS_LAIR,
            Has(I.BETTYS_LAIR_DOOR),
            "Betty's Lair Door",
            "sdoor_betty",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
    ),
    (
        DeathsDoorEntrance(
            R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY,
            R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
            None,
            "Grove of Spirits to Lost Cemetery",
            "tdoor_gy",
            "lvl_Graveyard",
        ),
        DeathsDoorEntrance(
            R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
            R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY,
            None,
            "Lost Cemetery to Grove of Spirits",
            "tdoor_gy",
            "lvl_Tutorial",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.LOST_CEMETERY_EXIT_TO_CRYPT,
            R.CRYPT_EXIT_TO_LOST_CEMETERY,
            None,
            "Lost Cemetery to Crypt",
            "d_graveyardtocrypt",
            "lvlConnect_Graveyard_Gardens",
        ),
        DeathsDoorEntrance(
            R.CRYPT_EXIT_TO_LOST_CEMETERY,
            R.LOST_CEMETERY_EXIT_TO_CRYPT,
            None,
            "Crypt to Lost Cemetery",
            "d_graveyardtocrypt",
            "lvl_Graveyard",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
            R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT,
            None,
            "Crypt to Estate of the Urn Witch",
            "d_crypttogardens",
            "lvl_GrandmaGardens",
        ),
        DeathsDoorEntrance(
            R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CRYPT,
            R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
            None,
            "Estate of the Urn Witch to Crypt",
            "d_crypttogardens",
            "lvlConnect_Graveyard_Gardens",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
            R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
            None,
            "Estate of the Urn Witch to Ceramic Manor",
            "d_gardenstomansion",
            "lvl_GrandmaMansion",
        ),
        DeathsDoorEntrance(
            R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
            R.ESTATE_OF_THE_URN_WITCH_EXIT_TO_CERAMIC_MANOR,
            None,
            "Ceramic Manor to Estate of the Urn Witch",
            "d_gardenstomansion",
            "lvl_GrandmaGardens",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
            R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
            None,
            "Ceramic Manor to Furnace Observation Rooms",
            "d_mansiontobasement",
            "lvlConnect_Mansion_Basement",
        ),
        DeathsDoorEntrance(
            R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
            R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
            None,
            "Furnace Observation Rooms to Ceramic Manor",
            "d_mansiontobasement",
            "lvl_GrandmaMansion",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
            R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
            Has(I.FIRE),
            "Furnace Observation Rooms to Inner Furnace",
            "d_basementtoromp",
            "lvl_GrandmaBasement",
        ),
        DeathsDoorEntrance(
            R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
            R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
            None,
            "Inner Furnace to Furnace Observation Rooms",
            "d_basementtoromp",
            "lvlConnect_Mansion_Basement",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
            R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
            None,
            "Inner Furnace to The Urn Witch's Laboratory",
            "d_basementtoboss",
            "boss_grandma",
        ),
        DeathsDoorEntrance(
            R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
            R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
            None,
            "The Urn Witch's Laboratory to Inner Furnace",
            "d_basementtoboss",
            "lvl_GrandmaBasement",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR_CAVES,
            R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY,
            None,
            "Lost Cemetery to Stranded Sailor Caves",
            "d_graveyardtosailorcaves",
            "lvlconnect_graveyard_sailor",
        ),
        DeathsDoorEntrance(
            R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY,
            R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR_CAVES,
            None,
            "Stranded Sailor Caves to Lost Cemetery",
            "d_graveyardtosailorcaves",
            "lvl_graveyard",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR,
            R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES,
            None,
            "Stranded Sailor Caves to Stranded Sailor",
            "d_connecttosailor",
            "lvl_sailormountain",
        ),
        DeathsDoorEntrance(
            R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES,
            R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR,
            None,
            "Stranded Sailor to Stranded Sailor Caves",
            "d_connecttosailor",
            "lvlconnect_graveyard_sailor",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE,
            R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR,
            None,
            "Stranded Sailor to Castle Lockstone",
            "d_sailortofortress",
            "lvl_frozenfortress",
        ),
        DeathsDoorEntrance(
            R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR,
            R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE,
            None,
            "Castle Lockstone to Stranded Sailor",
            "d_sailortofortress",
            "lvl_sailormountain",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.CASTLE_LOCKSTONE_EXIT_TO_CAMP,
            R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
            None,
            "Castle Lockstone to Camp of the Free Crows",
            "d_fortresstoroof",
            "lvlConnect_Fortress_Mountaintops",
        ),
        DeathsDoorEntrance(
            R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
            R.CASTLE_LOCKSTONE_EXIT_TO_CAMP,
            None,
            "Camp of the Free Crows to Castle Lockstone",
            "d_fortresstoroof",
            "lvl_frozenfortress",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
            R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
            None,
            "Camp of the Free Crows to Old Watchtowers",
            "d_CrowCavestoMountaintops",
            "lvl_mountaintops",
        ),
        DeathsDoorEntrance(
            R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
            R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
            None,
            "Old Watchtowers to Camp of the Free Crows",
            "d_CrowCavestoMountaintops",
            "lvlConnect_Fortress_Mountaintops",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
            R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
            None,
            "Old Watchtowers to Betty's Lair",
            "d_mountaintopstobetty",
            "boss_betty",
        ),
        DeathsDoorEntrance(
            R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
            R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
            None,
            "Betty's Lair to Old Watchtowers",
            "d_mountaintopstobetty",
            "lvl_mountaintops",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
            R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
            Has(I.FIRE),
            "Lost Cemetery to Overgrown Ruins (Gondola)",
            "forest_buggy",
            "lvl_Forest",
        ),
        DeathsDoorEntrance(
            R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
            R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
            None,
            "Overgrown Ruins to Lost Cemetery (Gondola)",
            "forest_buggy",
            "lvl_Graveyard",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
            R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
            None,
            "Mushroom Dungeon to Flooded Fortress",
            "d_swamp_enter",
            "lvl_Swamp",
        ),
        DeathsDoorEntrance(
            R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
            R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
            None,
            "Flooded Fortress to Mushroom Dungeon",
            "d_swamp_enter",
            "lvl_Forest",
        ),
    ),
    (
        DeathsDoorEntrance(
            R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
            R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
            None,
            "Flooded Fortress to Throne of the Frog King",
            "d_frog_boss",
            "boss_frog",
        ),
        DeathsDoorEntrance(
            R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
            R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
            None,
            "Throne of the Frog King to Flooded Fortress",
            "d_frog_boss",
            "lvl_Swamp",
        ),
    ),
]

# TODO: Consider including the spell upgrade arenas
one_way_scene_transitions: list[
    tuple[DeathsDoorEntrance, DeathsDoorEntrance | None]
] = [
    # Ancient Doors
    (
        DeathsDoorEntrance(
            R.CERAMIC_MANOR_ANCIENT_DOOR,
            R.FIRE_AVARICE,
            HasAll(
                E.ACCESS_TO_DAY,
                I.CROW_MANOR_AFTER_TORCH_PUZZLE,
                I.CROW_MANOR_BEDROOM,
                I.CROW_MANOR_IMP_LOFT,
                I.CROW_MANOR_LIBRARY,
            ),
            "Ceramic Manor Ancient Door",
            "hod_anc_mansion",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
        None,
    ),  # No return journey
    (
        DeathsDoorEntrance(
            R.CASTLE_LOCKSTONE_ANCIENT_DOOR,
            R.HOOKSHOT_AVARICE,
            HasAll(
                E.ACCESS_TO_DAY,
                I.CROW_LOCKSTONE_EAST,
                I.CROW_LOCKSTONE_WEST,
                I.CROW_LOCKSTONE_SOUTH_WEST,
                I.CROW_LOCKSTONE_WEST_LOCKED,
            ),
            "Castle Lockstone Ancient Door",
            "hod_anc_fortress",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
        None,
    ),  # No return journey
    (
        DeathsDoorEntrance(
            R.MUSHROOM_DUNGEON_ANCIENT_DOOR,
            R.BOMB_AVARICE,
            HasAll(
                E.ACCESS_TO_DAY,
                I.CROW_DUNGEON_COBWEB,
                I.CROW_DUNGEON_HALL,
                I.CROW_DUNGEON_RIGHTMOST,
                I.CROW_DUNGEON_WATER_ARENA,
            ),
            "Mushroom Dungeon Ancient Door",
            "hod_anc_forest",
            "lvl_HallOfDoors",
            no_jefferson=True,
        ),
        None,
    ),  # No return journey
]

# DeathsDoorEntrance(
#     R.OVERGROWN_RUINS_EXIT_TO_MUSHROOM_DUNGEON_MAIN,
#     R.MUSHROOM_DUNGEON_EXIT_TO_OVERGROWN_RUINS_MAIN,
#     None,
# ),
# DeathsDoorEntrance(
#     R.MUSHROOM_DUNGEON_EXIT_TO_OVERGROWN_RUINS_MAIN,
#     R.OVERGROWN_RUINS_EXIT_TO_MUSHROOM_DUNGEON_MAIN,
#     None,
# ), ##TODO: set up meaningful scene transition entrances for Mushroom Dungeon <-> Overgrown Ruins


def scene_transition_names() -> set[str]:
    names: set[str] = set()
    for scene_transition_pair in two_way_scene_transitions:
        names.add(scene_transition_pair[0].name)
        if scene_transition_pair[1] is not None:
            names.add(scene_transition_pair[1].name)
    return names
