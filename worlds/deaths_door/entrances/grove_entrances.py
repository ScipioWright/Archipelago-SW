from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

grove_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Grove of Spirits
    DeathsDoorEntrance(R.GROVE_OF_SPIRITS_DOOR, R.GROVE_OF_SPIRITS, None),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS, R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY, None
    ),
    DeathsDoorEntrance(
        R.GROVE_OF_SPIRITS_EXIT_TO_LOST_CEMETERY, R.GROVE_OF_SPIRITS, None
    ),
]