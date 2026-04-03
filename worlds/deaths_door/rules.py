import dataclasses
from typing import TYPE_CHECKING

from .items import DeathsDoorItemName as I
from .locations import location_table, DeathsDoorLocationName as L
from .events import DeathsDoorEventName as E
from .regions import DeathsDoorRegionName as R
from .options import OffscreenTargetingTricks, GeometryExploits, RollBuffers
from .vanilla_pools import vanilla_location_lookup

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
from .rule_builder_overrides import (
    Has,
    HasAny,
    HasAll,
    CanReachRegion,
)

if TYPE_CHECKING:
    from . import DeathsDoorWorld
    from BaseClasses import CollectionState


# option related
@dataclasses.dataclass()
class HasEnoughLifeSeeds(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> "Resolved":
        return self.Resolved(world.options.plant_pot_number.value, player=world.player)

    class Resolved(Rule.Resolved):
        life_seeds_required: int

        def _evaluate(self, state: "CollectionState") -> bool:
            return state.has(
                I.LIFE_SEED.value, self.player, count=self.life_seeds_required
            )

        def item_dependencies(self) -> dict[str, set[int]]:
            return {I.LIFE_SEED.value: {id(self)}}


@dataclasses.dataclass()
class HasPlantedEnoughLifeSeeds(Rule["DeathsDoorWorld"], game="Death's Door"):
    def _instantiate(self, world: "DeathsDoorWorld") -> "Resolved":
        return self.Resolved(world.options.plant_pot_number.value, player=world.player)

    class Resolved(Rule.Resolved):
        planted_seeds_required: int

        def _evaluate(self, state: "CollectionState") -> bool:
            return state.has(
                E.PLANTED_SEED.value, self.player, count=self.planted_seeds_required
            )

        def item_dependencies(self) -> dict[str, set[int]]:
            return {E.PLANTED_SEED.value: {id(self)}}


deaths_door_location_rules: dict[L, Rule["DeathsDoorWorld"] | None] = {
    L.FIRE_SILENT_SERVANT: Has(I.FIRE),
    L.BOMB_SILENT_SERVANT: Has(I.BOMB),
    L.HOOKSHOT_SILENT_SERVANT: Has(I.LEVER_HOOKSHOT_SILENT_SERVANT),
    L.ARROW_SILENT_SERVANT: HasAll(I.FIRE, I.BOMB, I.HOOKSHOT),
    L.REAPERS_GREATSWORD: HasAll(I.HOOKSHOT, I.LEVER_SAILOR_GREATSWORD_GATE),
    L.HEART_SHRINE_CEMETERY_BEHIND_ENTRANCE: Has(I.HOOKSHOT),
    L.MAGIC_SHRINE_CEMETERY_AFTER_SMOUGH_ARENA: Has(I.BOMB),
    L.HEART_SHRINE_HOOKSHOT_ARENA: Has(I.HOOKSHOT),
    L.MAGIC_SHRINE_LOCKSTONE_SECRET_WEST: Has(I.LEVER_LOCKSTONE_SHRINE),
    L.HEART_SHRINE_CAMP_ICE_SKATING: Has(I.HOOKSHOT),
    L.MAGIC_SHRINE_RUINS_HOOKSHOT_ARENA: Has(I.HOOKSHOT),
    L.HEART_SHRINE_DUNGEON_WATER_ARENA: HasAll(I.BOMB, I.FIRE),
    L.HEART_SHRINE_GARDEN_OF_LIFE: Has(I.FIRE),
    L.OLD_COMPASS: Has(I.FIRE),
    L.OLD_PHOTOGRAPH: Has(I.FIRE),
    L.TOKEN_OF_DEATH: Has(I.HOOKSHOT),
    L.MALFORMED_SEED: Has(I.HOOKSHOT),
    L.CORRUPTED_ANTLER: Has(I.BOMB) & Has(I.GREEN_KEY, 4),
    L.GRUNTS_OLD_MASK: Has(E.RESCUE_GRUNT)
    & CanReachRegion(R.THRONE_OF_THE_FROG_KING),  ##TODO: FIX THIS
    L.ANCIENT_DOOR_SCALE_MODEL: Has(I.FIRE),
    L.MODERN_DOOR_SCALE_MODEL: Has(I.HOOKSHOT)
    | CanReachRegion(R.POST_BOMB_AVARICE)
    & HasAll(I.ROGUE_DAGGERS, I.BOMB)
    & (True_(options=[OptionFilter(RollBuffers, 1)]) | Has(E.OOL)),
    L.RUSTY_BELLTOWER_KEY: HasAll(E.GREY_CROW_BOSS, I.HOOKSHOT),
    L.INK_COVERED_TEDDY_BEAR: Has(I.HOOKSHOT),
    L.SURVEILLANCE_DEVICE: Has(I.BOMB)
    | HasAny(I.SWORD, I.ROGUE_DAGGERS, I.REAPERS_GREATSWORD, I.DISCARDED_UMBRELLA)
    & (True_(options=[OptionFilter(RollBuffers, 1)]) | Has(E.OOL)),
    L.SHINY_MEDALLION: Has(I.BOMB),
    L.MAKESHIFT_SOUL_KEY: Has(I.HOOKSHOT),
    L.MYSTERIOUS_LOCKET: Has(E.ACCESS_TO_NIGHT),
    L.SOUL_ORB_CEMETERY_HOOKSHOT_TOWERS: Has(I.HOOKSHOT),
    L.SOUL_ORB_CEMETERY_WINDING_BRIDGE_END: Has(I.BOMB),
    L.SOUL_ORB_CATACOMBS_ROOM_2: Has(I.FIRE),
    L.SOUL_ORB_CEMETERY_GATED_SEWER: Has(I.LEVER_CEMETERY_SEWER),
    L.SOUL_ORB_LOCKSTONE_HOOKSHOT_NORTH: Has(I.HOOKSHOT),
    L.SOUL_ORB_CAMP_ROOFTOPS: Has(I.HOOKSHOT),
    L.SOUL_ORB_CAMP_BROKEN_BRIDGE: Has(I.HOOKSHOT),
    L.SEED_WATCHTOWERS_ARCHER_PLATFORM: Has(I.HOOKSHOT),
    L.SOUL_ORB_RUINS_STUMP: Has(I.HOOKSHOT),
    L.SOUL_ORB_DUNGEON_COBWEB: Has(I.FIRE),
    L.SOUL_ORB_DUNGEON_LOWER_ENTRANCE: Has(I.BOMB),
    L.SOUL_ORB_RUINS_LOWER_BOMB_WALL: Has(I.BOMB)
    | True_(options=[OptionFilter(OffscreenTargetingTricks, 1)])
    | Has(E.OOL),
    L.SOUL_ORB_RUINS_LORD_OF_DOORS_ARENA_HOOKSHOT: Has(I.HOOKSHOT)
    | True_(options=[OptionFilter(GeometryExploits, 1)])
    | Has(E.OOL),
    L.SOUL_ORB_RUINS_ABOVE_ENTRANCE_GATE: Has(I.HOOKSHOT),
    L.SOUL_ORB_RUINS_LOWER_HOOKSHOT: Has(I.HOOKSHOT)
    | True_(options=[OptionFilter(GeometryExploits, 1)])
    | Has(E.OOL),
    L.SEED_FORTRESS_WATCHTOWER: Has(I.LEVER_FORTRESS_WATCHTOWER_UPPER),
    L.SEED_FORTRESS_BRIDGE: HasAny(I.BOMB, I.HOOKSHOT),
    L.SOUL_ORB_FORTRESS_BOMB: Has(I.BOMB),
    L.SOUL_ORB_GARDEN_OF_LIFE_HOOKSHOT_LOOP: Has(I.HOOKSHOT),
    L.SOUL_ORB_GARDEN_OF_LOVE_BOMB_WALLS: Has(I.BOMB),
    L.SOUL_ORB_ESTATE_BROKEN_BOARDWALK: Has(I.HOOKSHOT),
    L.SOUL_ORB_ESTATE_TWIN_BENCHES: HasAll(I.BOMB, I.FIRE),
    L.SOUL_ORB_ESTATE_SEWER_MIDDLE: Has(I.HOOKSHOT),
    L.SOUL_ORB_GARDEN_OF_PEACE: Has(I.BOMB),
    L.SOUL_ORB_FURNACE_LANTERN_CHAIN: Has(I.FIRE),
    L.SOUL_ORB_SMALL_ROOM: Has(I.FIRE),
    L.SOUL_ORB_HOOKSHOT_SECRET: Has(I.HOOKSHOT)
    | CanReachRegion(R.POST_BOMB_AVARICE, options=[OptionFilter(RollBuffers, 1)])
    & HasAll(I.ROGUE_DAGGERS, I.BOMB),
    L.SOUL_ORB_BOMB_SECRET: Has(I.BOMB)
    | HasAny(I.SWORD, I.ROGUE_DAGGERS, I.REAPERS_GREATSWORD, I.DISCARDED_UMBRELLA)
    & (True_(options=[OptionFilter(RollBuffers, 1)]) | Has(E.OOL)),
    L.SOUL_ORB_FIRE_SECRET: Has(I.FIRE),
    L.YELLOW_ANCIENT_TABLET_OF_KNOWLEDGE: Has(E.ACCESS_TO_NIGHT),
    L.RUINS_OWL: Has(E.ACCESS_TO_NIGHT),
    L.GREEN_ANCIENT_TABLET_OF_KNOWLEDGE: HasPlantedEnoughLifeSeeds(),
    L.ESTATE_OWL: Has(E.ACCESS_TO_NIGHT),
    L.CYAN_ANCIENT_TABLET_OF_KNOWLEDGE: Has(E.ACCESS_TO_NIGHT)
    & CanReachRegion(R.LOST_CEMETERY_CENTRAL)
    & CanReachRegion(R.LOST_CEMETERY_STEADHONE)
    & CanReachRegion(R.LOST_CEMETERY_BELLTOWER)
    & CanReachRegion(
        R.LOST_CEMETERY_SUMMIT
    ),  ###TODO Consider changing these to events? ##TODO: FIX THIS
    L.PURPLE_ANCIENT_TABLET_OF_KNOWLEDGE: HasAll(
        E.ACCESS_TO_NIGHT, I.MYSTERIOUS_LOCKET
    ),
    L.BLUE_ANCIENT_TABLET_OF_KNOWLEDGE: Has(E.LIT_WATCHTOWER_TORCH, 6),
    L.WATCHTOWERS_OWL: Has(E.ACCESS_TO_NIGHT),
    L.LEVER_HOOKSHOT_SILENT_SERVANT: Has(I.HOOKSHOT),
    L.LEVER_SAILOR_GREATSWORD_GATE: HasAll(I.HOOKSHOT, I.BOMB),
    L.LEVER_LOCKSTONE_VERTICAL_LASER_PUZZLE: Has(
        I.LEVER_LOCKSTONE_TRACKING_BEAM_PUZZLE
    ),
    L.LEVER_LOCKSTONE_SHRINE: Has(I.HOOKSHOT),
    L.LEVER_LOCKSTONE_UPPER_PUZZLE: Has(I.HOOKSHOT),
    L.LEVER_LOCKSTONE_UPPER_DUAL_LASER_PUZZLE: Has(I.PINK_KEY, 5) & Has(I.HOOKSHOT),
    L.LEVER_FORTRESS_MAIN_GATE: HasAny(I.BOMB, I.HOOKSHOT),
    L.LEVER_FORTRESS_CENTRAL_SHORTCUT: Has(I.BOMB),
    L.KEY_LOCKSTONE_WEST: Has(I.HOOKSHOT),
    L.KEY_LOCKSTONE_NORTH: Has(I.LEVER_LOCKSTONE_NORTH_PUZZLE),
    L.KEY_DUNGEON_HALL: Has(I.FIRE),
    L.KEY_DUNGEON_NEAR_WATER_ARENA: Has(I.FIRE),
    L.KEY_DUNGEON_RIGHT: Has(I.FIRE),
    L.CROW_DUNGEON_COBWEB: Has(I.FIRE),
    L.CROW_LOCKSTONE_WEST_LOCKED: Has(I.PINK_KEY, 5)
    | HasAny(I.SWORD, I.ROGUE_DAGGERS, I.REAPERS_GREATSWORD, I.DISCARDED_UMBRELLA)
    & (True_(options=[OptionFilter(RollBuffers, 1)]) | Has(E.OOL)),
    L.RED_ANCIENT_TABLET_OF_KNOWLEDGE: HasAll(E.ACCESS_TO_NIGHT, I.HOOKSHOT),
}


def set_location_rules(world: "DeathsDoorWorld") -> None:
    for location_data in location_table:
        current_location_group_names = set(
            location_group.value for location_group in location_data.location_groups
        )
        if (
            len(
                world.options.unrandomized_pools.value.intersection(
                    current_location_group_names
                )
            )
            == 0
        ) or location_data.name in vanilla_location_lookup.keys():
            if location_data.name in deaths_door_location_rules.keys():
                rule = deaths_door_location_rules[location_data.name]
            else:
                rule = None
            if rule is not None:
                location = world.get_location(location_data.name.value)
                world.set_rule(location, rule)
