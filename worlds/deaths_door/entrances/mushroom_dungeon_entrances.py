from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAny
try:
    from rule_builder import True_, OptionFilter
except ModuleNotFoundError:
    from ..rule_builder import True_, OptionFilter
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..events import DeathsDoorEventName as E
from ..options import GateRollsGlitch

mushroom_dungeon_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Mushroom Dungeon
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_DOOR,
        R.MUSHROOM_DUNGEON_LOBBY,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.MUSHROOM_DUNGEON_LOBBY,
        Has(E.MUSHROOM_DUNGEON_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        True_(options=[OptionFilter(GateRollsGlitch, 1)]) | Has(E.OOL),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_LOBBY,
        HasAny(I.LEVER_DUNGEON_ENTRANCE_LEFT_GATE, I.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.FIRE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_LOBBY,
        True_(options=[OptionFilter(GateRollsGlitch, 1)]) | Has(E.OOL)
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        Has(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_EXIT_TO_FLOODED_FORTRESS,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_LOBBY,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        HasAny(I.LEVER_DUNGEON_ENTRANCE_LEFT_GATE, I.LEVER_DUNGEON_ENTRANCE_RIGHT_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        HasAny(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_WATER_ARENA,
        Has(I.GREEN_KEY, 4),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_BIG_DOOR,
        R.MUSHROOM_DUNGEON_ANCIENT_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        Has(I.GREEN_KEY, 4),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        Has(I.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.MUSHROOM_DUNGEON_THUNDER_HAMMER,
        Has(I.LEVER_RUINS_UPPER_DUNGEON_ENTRANCE),
    ),  # TODO: This is a scene transition
    # TODO: In ER, this would provide new access to Mushroom Dungeon, and would need to be connected to the dungeon. Omitting for now
]