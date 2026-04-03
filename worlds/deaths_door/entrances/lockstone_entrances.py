from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAny, HasAll
try:
    from rule_builder import True_, OptionFilter
except ModuleNotFoundError:
    from ..rule_builder import True_, OptionFilter
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E
from ..options import GeometryExploits

lockstone_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Castle Lockstone
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR, R.CASTLE_LOCKSTONE_ENTRANCE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE, R.CASTLE_LOCKSTONE_EXIT_TO_STRANDED_SAILOR, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        Has(I.LEVER_LOCKSTONE_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE,
        R.CASTLE_LOCKSTONE_CENTRAL,
        Has(I.LEVER_LOCKSTONE_ENTRANCE),
    ),
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_DOOR, R.CASTLE_LOCKSTONE_CENTRAL, None),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW, R.CASTLE_LOCKSTONE_ENTRANCE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_SOUTHWEST_CROW,
        Has(I.LEVER_LOCKSTONE_DUAL_LASER_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_SOUTHWEST_UPPER, Has(I.HOOKSHOT)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_OPENGATE, R.CASTLE_LOCKSTONE_SOUTHWEST_CROW, Has(I.FIRE)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_EAST,
        Has(I.LEVER_LOCKSTONE_EAST_LOWER),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        HasAny(I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        R.CASTLE_LOCKSTONE_EAST,
        True_(options=[OptionFilter(GeometryExploits,1)]) | Has(E.OOL)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER,
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        HasAll(
            I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_PUZZLE
        ) | True_(options=[OptionFilter(GeometryExploits, 1)]) | Has(E.OOL),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LIBRARY,
        R.CASTLE_LOCKSTONE_ENTRANCE,
        Has(I.LEVER_LOCKSTONE_EAST_START_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ENTRANCE,
        R.CASTLE_LOCKSTONE_LIBRARY,
        Has(I.LEVER_LOCKSTONE_EAST_START_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_DEADBOLT,
        R.CASTLE_LOCKSTONE_LIBRARY,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_JAILED_SEED, Has(I.HOOKSHOT)
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_ROOF, R.CASTLE_LOCKSTONE_CENTRAL, None
    ),  # Fall down the elevator
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ROOF,
        HasAll(
            E.CASTLE_LOCKSTONE_LORD_THEODOOR,
            E.CASTLE_LOCKSTONE_LORD_DEADBOLT,
            E.CASTLE_LOCKSTONE_LORD_LOCKSTONE,
            E.CASTLE_LOCKSTONE_LORD_OPENGATE,
        ),
    ),  # Can summon elevator
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_EXIT_TO_CAMP, R.CASTLE_LOCKSTONE_ROOF, None),
    DeathsDoorEntrance(R.CASTLE_LOCKSTONE_ROOF, R.CASTLE_LOCKSTONE_EXIT_TO_CAMP, None),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        R.CASTLE_LOCKSTONE_LORD_THEODOOR,
        Has(I.PINK_KEY, 5)
        & HasAll(I.HOOKSHOT, I.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_ANCIENT_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL, R.CASTLE_LOCKSTONE_LORD_LOCKSTONE, None
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_CENTRAL,
        R.CASTLE_LOCKSTONE_LORD_OPENGATE,
        HasAll(I.HOOKSHOT, I.LEVER_LOCKSTONE_HOOKSHOT_PUZZLE),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST_UPPER_KEYED_DOOR,
        R.CASTLE_LOCKSTONE_LORD_DEADBOLT,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_LORD_THEODOOR,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        None,
    ),
    DeathsDoorEntrance(
        R.CASTLE_LOCKSTONE_EAST,
        R.CASTLE_LOCKSTONE_EAST_CROW,
        HasAll(
            I.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE,
            I.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE,
        ),
    ),
]
