from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

furnace_observation_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Furnace Observation Rooms
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        R.FURNACE_OBSERVATION_ROOMS,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_CERAMIC_MANOR,
        None,
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS,
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.FURNACE_OBSERVATION_ROOMS_EXIT_TO_INNER_FURNACE,
        R.FURNACE_OBSERVATION_ROOMS,
        None,
    ),
]
