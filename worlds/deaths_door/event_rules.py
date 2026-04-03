from typing import TYPE_CHECKING
from .rule_builder_overrides import Has, HasAll, CanReachRegion
from .items import DeathsDoorItemName as I
from .regions import DeathsDoorRegionName as R
from .options import StartDayOrNight, BombBellGlitch, OffscreenTargetingTricks, Goal
from .events import (
    DeathsDoorEventLocationName as EL,
    DeathsDoorEventName as E,
    event_location_table,
    pot_table,
)
from .rules import HasEnoughLifeSeeds, HasPlantedEnoughLifeSeeds

try:
    from rule_builder import (
        Rule,
        True_,
        OptionFilter,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        Rule,
        True_,
        OptionFilter,
    )

if TYPE_CHECKING:
    from . import DeathsDoorWorld


pot_specific_rules: dict[EL: Rule["DeathsDoorWorld"]] = {
    EL.POT_CATACOMBS_ROOM_2: Has(I.FIRE),
    EL.POT_BOMB_SILENT_SERVANT: Has(I.BOMB),
    EL.POT_MANOR_IMP_LOFT: Has(I.FIRE),  ##TODO: Check?
    EL.POT_HOOKSHOT_SILENT_SERVANT: Has(I.LEVER_HOOKSHOT_SILENT_SERVANT),
    EL.POT_LOCKSTONE_WEST_KEYED_CROW: Has(I.PINK_KEY, 5),
    EL.POT_FORTRESS_MAIN_GATE: Has(I.BOMB),
}


deaths_door_event_rules: dict[EL: Rule["DeathsDoorWorld"] | None] = {
    EL.LORD_OF_DOORS: HasAll(E.GREY_CROW_BOSS, I.HOOKSHOT),
    EL.TRUE_ENDING: HasAll(I.RED_ANCIENT_TABLET_OF_KNOWLEDGE, I.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE, I.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE, I.PINK_ANCIENT_TABLET_OF_KNOWLEDGE, I.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE, I.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE, I.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE) | True_(options=[OptionFilter(Goal, Goal.option_lord_of_doors)]) | True_(options=[OptionFilter(Goal, Goal.option_green_tablet)]),
    EL.LIFE_SEED_DOOR: HasPlantedEnoughLifeSeeds(),
    EL.LOST_CEMETERY_OPENED_EXIT_TO_SAILOR: Has(I.FIRE) | True_(options=[OptionFilter(OffscreenTargetingTricks, 1)]) | Has(E.OOL),
    EL.FLOODED_FORTRESS_OPENED_BRIDGE: Has(I.LEVER_FORTRESS_NORTH_WEST),
    EL.ACCESS_TO_NIGHT: True_(options=[OptionFilter(StartDayOrNight, 1)])
    | (Has(I.RUSTY_BELLTOWER_KEY) & CanReachRegion(R.LOST_CEMETERY_BELLTOWER)) | CanReachRegion(R.LOST_CEMETERY_SUMMIT, options=[OptionFilter(BombBellGlitch, 1)]),
    EL.ACCESS_TO_DAY: True_(options=[OptionFilter(StartDayOrNight, 0)])
    | (Has(I.RUSTY_BELLTOWER_KEY) & CanReachRegion(R.LOST_CEMETERY_BELLTOWER)) | CanReachRegion(R.LOST_CEMETERY_SUMMIT) & (True_(options=[OptionFilter(BombBellGlitch, 1)]) | Has(E.OOL)),
    EL.GREY_CROW_BOSS: HasAll(
        I.GIANT_SOUL_OF_BETTY,
        I.GIANT_SOUL_OF_THE_FROG_KING,
        I.GIANT_SOUL_OF_THE_URN_WITCH,
    ),
    EL.ACTIVATED_FURNACE_BURNERS: Has(I.FIRE),
    EL.WATCHTOWER_ENTRANCE_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_JAMMING_START_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BOXES_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_FIRST_POT_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BOOMERS_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.WATCHTOWER_BEFORE_ICE_SKATING_TORCH: HasAll(
        I.FIRE, E.ACCESS_TO_NIGHT
    ),
    EL.MUSHROOM_DUNGEON_MAIN_GATE: HasAll(
        I.MAGICAL_FOREST_HORN, E.ACCESS_TO_DAY
    ),
    EL.RESCUE_GRUNT: Has(I.BOMB),
    EL.CASTLE_LOCKSTONE_LORD_LOCKSTONE: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_OPENGATE: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_DEADBOLT: Has(I.FIRE),
    EL.CASTLE_LOCKSTONE_LORD_THEODOOR: Has(I.FIRE),
}

# Add in pots to existing tables to be able to use the same infrastructure
for pot in pot_table:
    pot_rule = HasEnoughLifeSeeds()
    if pot.name in pot_specific_rules.keys():
        pot_rule = pot_rule & pot_specific_rules[pot.name]
    deaths_door_event_rules[pot.name] = pot_rule


def set_event_rules(world: "DeathsDoorWorld") -> None:
    for event_location_data in event_location_table:
        if event_location_data.name in deaths_door_event_rules.keys():
            event_rule = deaths_door_event_rules[event_location_data.name]
        else:
            event_rule = None
        if event_rule is not None:
            event_location = world.get_location(
                event_location_data.name.value
            )
            world.set_rule(event_location, event_rule)
