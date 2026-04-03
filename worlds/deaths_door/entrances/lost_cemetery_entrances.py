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

lost_cemetery_entrances: list[DeathsDoorEntrance] = [
    # Entrances in Lost Cemetery
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        R.LOST_CEMETERY_EXIT_TO_GROVE_OF_SPIRITS,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR, R.LOST_CEMETERY_CENTRAL, None
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL, R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR, Has(E.LOST_CEMETERY_OPENED_GROVE_TO_CENTRAL)
    ), # For Jefferson Backtracking
    DeathsDoorEntrance(R.LOST_CEMETERY_DOOR, R.LOST_CEMETERY_CENTRAL, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL, R.LOST_CEMETERY_DOOR, None
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE, R.LOST_CEMETERY_CENTRAL, Has(I.LEVER_CATACOMBS_TOWER)
    ),
    DeathsDoorEntrance(R.LOST_CEMETERY_RIGHT_ARENA, R.LOST_CEMETERY_CENTRAL, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_GROVE_OF_SPIRITS_DOOR,
        R.LOST_CEMETERY_RIGHT_ARENA,
        Has(I.HOOKSHOT),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        R.LOST_CEMETERY_RIGHT_ARENA,
        Has(I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_RIGHT_ARENA,
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        Has(I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT,
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_RIGHT_ARENA,
        HasAny(I.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS, I.LEVER_CATACOMBS_TOWER),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR_CAVES,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        R.LOST_CEMETERY_EXIT_TO_STRANDED_SAILOR_CAVES,
        None,
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        R.LOST_CEMETERY_STEADHONE,
        Has(E.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE,
        R.LOST_CEMETERY_NEAR_EXIT_TO_STRANDED_SAILOR,
        Has(E.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR) | True_(options=[OptionFilter(GeometryExploits,1)]) | Has(E.OOL),
    ),
    DeathsDoorEntrance(R.LOST_CEMETERY_BELLTOWER, R.LOST_CEMETERY_STEADHONE, None),
    DeathsDoorEntrance(R.LOST_CEMETERY_EXIT_TO_CRYPT, R.LOST_CEMETERY_BELLTOWER, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_BELLTOWER, Has(I.PINK_KEY, 5)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE,
        R.LOST_CEMETERY_BELLTOWER,
        Has(I.LEVER_CEMETERY_EXIT_TO_ESTATE),
    ),
    DeathsDoorEntrance(R.LOST_CEMETERY_BELLTOWER, R.LOST_CEMETERY_EXIT_TO_CRYPT, None),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_STEADHONE, Has(I.LEVER_CEMETERY_SEWER)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_STEADHONE,
        Has(I.PINK_KEY, 5) | Has(I.LEVER_CATACOMBS_TOWER),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_SUMMIT,
        Has(I.LEVER_GUARDIAN_OF_THE_DOOR_ACCESS),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_STEADHONE, R.LOST_CEMETERY_SUMMIT, Has(I.LEVER_CEMETERY_SEWER)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_EXIT_TO_OVERGROWN_RUINS,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        Has(I.LEVER_CEMETERY_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_RIGHT_ARENA,
        R.LOST_CEMETERY_EAST_TREE_BRIDGE,
        HasAll(I.LEVER_CEMETERY_EAST_TREE, I.LEVER_CEMETERY_SHORTCUT_TO_EAST_TREE),
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_SUMMIT, R.LOST_CEMETERY_EAST_TREE_BRIDGE, Has(I.FIRE)
    ),
    DeathsDoorEntrance(
        R.LOST_CEMETERY_CENTRAL,
        R.LOST_CEMETERY_CATACOMBS_ROOM_1,
        HasAny(I.FIRE, I.LEVER_CATACOMBS_EXIT),
    ),
]