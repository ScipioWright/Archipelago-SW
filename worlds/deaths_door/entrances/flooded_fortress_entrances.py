from .entrance_class import DeathsDoorEntrance
from ..rule_builder_overrides import Has, HasAny, HasAll
try:
    from rule_builder import True_, OptionFilter
except ModuleNotFoundError:
    from ..rule_builder import True_, OptionFilter
from ..items import DeathsDoorItemName as I
from ..regions import DeathsDoorRegionName as R
from ..options import OffscreenTargetingTricks
from ..events import DeathsDoorEventName as E

flooded_fortress_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Flooded Fortress
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        R.FLOODED_FORTRESS_ENTRANCE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_EXIT_TO_MUSHROOM_DUNGEON,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_WATCHTOWER_LOWER,
        Has(I.LEVER_FORTRESS_WATCHTOWER_LOWER),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_ENTRANCE,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        R.FLOODED_FORTRESS_ENTRANCE,
        True_(options=[OptionFilter(OffscreenTargetingTricks, 1)]) | Has(E.OOL) | Has(E.FLOODED_FORTRESS_OPENED_FORTRESS_ENTRANCE),  # Event is for Jefferson back-tracking
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_PRE_MAIN_GATE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_PRE_MAIN_GATE,
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_DOOR,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_STATUE,
        R.FLOODED_FORTRESS_PRE_MAIN_GATE,
        HasAll(I.LEVER_FORTRESS_STATUE),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_PRE_MAIN_GATE,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        HasAll(I.LEVER_FORTRESS_PRE_MAIN_GATE),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        Has(I.LEVER_FORTRESS_MAIN_GATE) & HasAny(I.BOMB, I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        R.FLOODED_FORTRESS_FROG_KING_ENCOUNTER,
        Has(I.LEVER_FORTRESS_MAIN_GATE) & Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        R.FLOODED_FORTRESS_U_TURN,
        HasAll(I.BOMB, I.LEVER_FORTRESS_CENTRAL_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_U_TURN,
        R.FLOODED_FORTRESS_INSIDE_MAIN_GATE,
        HasAll(I.BOMB, I.LEVER_FORTRESS_CENTRAL_SHORTCUT),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_U_TURN,
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        R.FLOODED_FORTRESS_U_TURN,
        Has(I.BOMB),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_BREAKABLE_BRIDGES,
        R.FLOODED_FORTRESS_BRIDGE,
        Has(I.LEVER_FORTRESS_BRIDGE),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_BRIDGE,
        R.FLOODED_FORTRESS_EXIT,
        Has(I.LEVER_FORTRESS_NORTH_WEST),
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT,
        R.FLOODED_FORTRESS_EXIT_TO_THRONE_OF_THE_FROG_KING,
        None,
    ),
    DeathsDoorEntrance(
        R.FLOODED_FORTRESS_EXIT,
        R.FLOODED_FORTRESS_BRIDGE,
        Has(E.FLOODED_FORTRESS_OPENED_BRIDGE) # For Jefferson back-tracking
    )
]