from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

laboratory_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Urn Witch's Laboratory
    DeathsDoorEntrance(R.URN_WITCHS_LABORATORY_DOOR, R.URN_WITCHS_LABORATORY, None),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY,
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        None,
    ),
    DeathsDoorEntrance(
        R.URN_WITCHS_LABORATORY_EXIT_TO_INNER_FURNACE,
        R.URN_WITCHS_LABORATORY,
        None,
    ),
]