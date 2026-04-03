from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

stranded_sailor_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Stranded Sailor
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, R.STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_EXIT_TO_STRANDED_SAILOR_CAVES, None
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_DOOR, R.STRANDED_SAILOR, None),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR, R.STRANDED_SAILOR_DOOR, None
    ),
    DeathsDoorEntrance(R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR, Has(I.BOMB)),
    DeathsDoorEntrance(R.STRANDED_SAILOR, R.STRANDED_SAILOR_UPPER, Has(I.BOMB)),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_UPPER, R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE, None
    ),
    DeathsDoorEntrance(
        R.STRANDED_SAILOR_EXIT_TO_CASTLE_LOCKSTONE, R.STRANDED_SAILOR_UPPER, None
    ),
]