from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

bettys_lair_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Betty's Lair
    DeathsDoorEntrance(
        R.BETTYS_LAIR_DOOR,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        R.BETTYS_LAIR,
        None,
    ),
    DeathsDoorEntrance(
        R.BETTYS_LAIR,
        R.BETTYS_LAIR_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
]
