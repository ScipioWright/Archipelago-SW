from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import HasAll, Has
try:
    from rule_builder import (
        True_,
        OptionFilter,
    )
except ModuleNotFoundError:
    from ..rule_builder import (
        True_,
        OptionFilter,
    )
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..options import GateRollsGlitch
from ..events import DeathsDoorEventName as E

crypt_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Crypt
    DeathsDoorEntrance(R.CRYPT_EXIT_TO_LOST_CEMETERY, R.CRYPT_MAIN_ROOM, None),
    DeathsDoorEntrance(R.CRYPT_MAIN_ROOM, R.CRYPT_EXIT_TO_LOST_CEMETERY, None),
    DeathsDoorEntrance(
        R.CRYPT_MAIN_ROOM,
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        HasAll(I.LEVER_ESTATE_ELEVATOR_LEFT, I.LEVER_ESTATE_ELEVATOR_RIGHT),
    ),
    DeathsDoorEntrance(
        R.CRYPT_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.CRYPT_MAIN_ROOM,
        HasAll(I.LEVER_ESTATE_ELEVATOR_LEFT, I.LEVER_ESTATE_ELEVATOR_RIGHT) | True_(options=[OptionFilter(GateRollsGlitch, 1)]) | Has(E.OOL),
    ), 
]
