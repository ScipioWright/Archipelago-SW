from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R

overgrown_ruins_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Overgrown Ruins
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        R.OVERGROWN_RUINS_EXIT_TO_LOST_CEMETERY,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        Has(I.LEVER_RUINS_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_FRONT_GATE,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        Has(I.LEVER_RUINS_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_DOOR,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.OVERGROWN_RUINS_OUTSIDE_MAIN_DUNGEON_GATE,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        Has(I.GREEN_KEY, 3) | Has(I.LEVER_RUINS_ENTRANCE_LADDER_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_MAIN_HALL,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        None,
    ),
    DeathsDoorEntrance(
        R.MUSHROOM_DUNGEON_RIGHTMOST_CROW,
        R.OVERGROWN_RUINS_FOREST_SETTLEMENT,
        Has(I.LEVER_DUNGEON_ABOVE_RIGHTMOST_CROW),
    ),
]