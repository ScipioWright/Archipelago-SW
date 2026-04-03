from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

stranded_sailor_caves_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Stranded Sailor Caves
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY, R.STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR, R.STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR_CAVES_EXIT_TO_LOST_CEMETERY, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR_CAVES_EXIT_TO_STRANDED_SAILOR, None
    ),
]