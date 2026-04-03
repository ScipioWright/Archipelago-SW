try:
    from rule_builder import True_, OptionFilter
except ModuleNotFoundError:
    from ..rule_builder import True_, OptionFilter
from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E
from ..options import GateRollsGlitch

ceramic_manor_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Ceramic Manor
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        R.CERAMIC_MANOR_MAIN_LOBBY,
        None,
    ),
    DeathsDoorEntrance(R.CERAMIC_MANOR_DOOR, R.CERAMIC_MANOR_MAIN_LOBBY, None),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_DOOR, None
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_ESTATE_OF_THE_URN_WITCH,
        True_(options=[OptionFilter(GateRollsGlitch, 1)]) | Has(E.OOL),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_LEFT,
        Has(I.YELLOW_KEY, 3) | Has(I.LEVER_MANOR_BIG_POT_ARENA),
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY, R.CERAMIC_MANOR_LIBRARY, Has(I.YELLOW_KEY, 3)
    ),
    # TODO: Base randomizer has a confusing "entrance" here from the Ancient Door back to Ceramic Manor... Omitting for now
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_ANCIENT_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CERAMIC_MANOR_MAIN_LOBBY,
        R.CERAMIC_MANOR_EXIT_TO_FURNACE_OBSERVATION_ROOMS,
        Has(I.YELLOW_KEY, 3) & Has(I.FIRE),
    ),
    ## TODO: Check if can return from furnace observation rooms without it being opened, not in base rando. Follow-up: Not without being able to use keys from the other side
]
