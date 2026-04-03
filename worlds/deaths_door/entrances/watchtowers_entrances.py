from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAll
try:
    from rule_builder import True_, OptionFilter
except ModuleNotFoundError:
    from ..rule_builder import True_, OptionFilter
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E
from ..options import GeometryExploits

watchtower_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Old Watchtowers
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        R.OLD_WATCHTOWERS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_EXIT_TO_CAMP_OF_THE_FREE_CROWS,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_DOOR,
        R.OLD_WATCHTOWERS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_ENTRANCE,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ENTRANCE,
        R.OLD_WATCHTOWERS_JAMMING_START,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_JAMMING_START,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_AFTER_BOOMERS),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_JAMMING_START,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_AFTER_BOOMERS),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_LASERS_ARENA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_BARB_ELEVATOR,
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        HasAll(I.HOOKSHOT, I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA) | Has(I.HOOKSHOT) & (True_(options=[OptionFilter(GeometryExploits, 1)]) | Has(E.OOL)),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        Has(I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_BOOMERS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_FIRST_POT_AREA,
        R.OLD_WATCHTOWERS_BOOMERS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_LASERS_ARENA,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_START,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_BEFORE_ICE_ARENA),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_ICE_SKATING_END,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_HEADLESS_LORD_OF_DOORS,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        Has(I.LEVER_WATCHTOWERS_AFTER_ICE_SKATING),
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.OLD_WATCHTOWERS_CAVE_ENTRANCE,
        R.OLD_WATCHTOWERS_EXIT_TO_BETTYS_LAIR,
        None,
    ),
]
