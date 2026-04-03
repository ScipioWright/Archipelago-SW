from .entrance_class import DeathsDoorEntrance
from ..regions import DeathsDoorRegionName as R

throne_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Throne of the Frog King
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_EXIT_TO_FLOODED_FORTRESS,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING_DOOR,
        R.THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.THRONE_OF_THE_FROG_KING,
        R.THRONE_OF_THE_FROG_KING_DOOR,
        None,
    ),
]
