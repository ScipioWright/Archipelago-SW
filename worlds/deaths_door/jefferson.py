from typing import TYPE_CHECKING
from BaseClasses import Region
from .regions import DeathsDoorRegionName as R, no_jefferson_regions
from .entrances.entrances import deathsdoor_internal_entrances
from .rule_builder_overrides import HasAll
from .items import DeathsDoorItemName as I
from .events import DeathsDoorEventName as E
from .entrances.scene_transitions import (
    two_way_scene_transitions,
)
from entrance_rando import EntranceType
from .entrances.entrance_class import DeathsDoorConnectionGroup

if TYPE_CHECKING:
    from . import DeathsDoorWorld

jefferson_tag: str = " (Jefferson)"


def create_jefferson_regions(world: "DeathsDoorWorld"):
    # Create the Jefferson regions
    for region_name in R:
        if (
            not region_name in no_jefferson_regions
            and region_name != R.FLOODED_FORTRESS_ENTRANCE
            and region_name != R.FLOODED_FORTRESS_ENTRANCE_JEFFERSON
        ):
            # avoid double creating the specific Jefferson region for Flooded Fortress
            # don't create regions that Jefferson can't access
            region = Region(
                region_name.value + jefferson_tag, world.player, world.multiworld
            )
            world.multiworld.regions.append(region)
            # connect the region back to its non-Jefferson counterpart (just in case for entrance rando)
            end_region = world.multiworld.get_region(
                region_name.value, world.player
            )
            world.create_entrance(region, end_region)


def create_jefferson_internal_connections(world: "DeathsDoorWorld"):
    # Connect the Jefferson regions internally
    for entrance in deathsdoor_internal_entrances:
        if not entrance.no_jefferson:
            start_region = world.multiworld.get_region(
                entrance.starting_region.value + jefferson_tag, world.player
            )
            end_region = world.multiworld.get_region(
                entrance.ending_region.value + jefferson_tag, world.player
            )
            new_entrance = world.create_entrance(start_region, end_region, entrance.rule)

    # Create the ability to access the Jefferson network of regions
    jefferson_start = R.STRANDED_SAILOR
    start_region = world.multiworld.get_region(jefferson_start.value, world.player)
    end_region = world.multiworld.get_region(
        jefferson_start.value + jefferson_tag, world.player
    )
    world.create_entrance(
        start_region, end_region, HasAll(E.ACCESS_TO_NIGHT, I.INK_COVERED_TEDDY_BEAR)
    )


def create_jefferson_vanilla_connections(world: "DeathsDoorWorld"):
    # Create vanilla entrances for Jefferson
    for scene_transition_pair in two_way_scene_transitions:
        for scene_transition in scene_transition_pair:
            if scene_transition is not None and not scene_transition.no_jefferson:
                start_region = world.multiworld.get_region(
                    scene_transition.starting_region.value + jefferson_tag, world.player
                )
                end_region = world.multiworld.get_region(
                    scene_transition.ending_region.value + jefferson_tag, world.player
                )
                new_entrance = world.create_entrance(start_region, end_region, scene_transition.rule)
                new_entrance.randomization_type = EntranceType.TWO_WAY
                new_entrance.randomization_group = DeathsDoorConnectionGroup.JEFFERSON
