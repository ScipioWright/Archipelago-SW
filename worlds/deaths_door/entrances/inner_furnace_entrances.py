from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import HasAll
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E

inner_furnace_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Inner Furnace
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        R.INNER_FURNACE_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE,
        R.INNER_FURNACE_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(R.INNER_FURNACE_DOOR, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE, R.INNER_FURNACE_DOOR, None
    ),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_1, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_2, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_3, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_4, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(R.INNER_FURNACE_POST_BURNER_7, R.INNER_FURNACE_ENTRANCE, None),
    DeathsDoorEntrance(
        R.INNER_FURNACE_ENTRANCE,
        R.INNER_FURNACE_POST_BURNER_1,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_2, R.INNER_FURNACE_POST_BURNER_1, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_1,
        R.INNER_FURNACE_POST_BURNER_2,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_2,
        R.INNER_FURNACE_POST_BURNER_3,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_3,
        R.INNER_FURNACE_POST_BURNER_4,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_5, R.INNER_FURNACE_POST_BURNER_4, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_4,
        R.INNER_FURNACE_POST_BURNER_5,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_5,
        R.INNER_FURNACE_POST_BURNER_6,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_6,
        R.INNER_FURNACE_POST_BURNER_7,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_8, R.INNER_FURNACE_POST_BURNER_7, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_7,
        R.INNER_FURNACE_POST_BURNER_8,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_9, R.INNER_FURNACE_POST_BURNER_8, None
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_8,
        R.INNER_FURNACE_POST_BURNER_9,
        HasAll(E.ACTIVATED_FURNACE_BURNERS, I.FIRE),
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        R.INNER_FURNACE_POST_BURNER_9,
        None,
    ),
    DeathsDoorEntrance(
        R.INNER_FURNACE_POST_BURNER_9,
        R.INNER_FURNACE_EXIT_TO_URN_WITCHS_LABORATORY,
        None,
    ),
]
