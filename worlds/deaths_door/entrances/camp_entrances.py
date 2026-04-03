from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

camp_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Camp of the Free Crows
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_CASTLE_LOCKSTONE,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CASTLE_DOOR,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_DOOR, R.CAMP_OF_THE_FREE_CROWS_VILLAGE, None
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_CAMP_BRIDGE,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        Has(I.HOOKSHOT),
    ),  # TODO Check if keys can be used as an alternative
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_EXIT_TO_OLD_WATCHTOWERS,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CAMP_OF_THE_FREE_CROWS_VILLAGE,
        R.CAMP_OF_THE_FREE_CROWS_ELEVATOR,
        Has(I.PINK_KEY, 5),
    ),
]
