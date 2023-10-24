from BaseClasses import MultiWorld, Location
from ..generic.Rules import add_rule, set_rule

from . import Locations
from .Options import GameMode, Opt


def set_star_access_rule(name: str, multiworld: MultiWorld, player: int, opt: Opt) -> None:
    # Relevant Option
    if opt.two_player:
        set_rule(multiworld.get_location(name, player),
                 lambda state: state.has("P1 Star Power", player) or state.has("P2 Star Power", player))
    else:
        set_rule(multiworld.get_location(name, player), lambda state: state.has("P1 Star Power", player))


def create_rules(multiworld: MultiWorld, player: int, opt: Opt, victory_location: Location) -> None:

    # Region (Entrance) Rules (handled in Regions.py instead for now)
    # if opt_game_mode == GameMode.option_cups:
    #     set_rule(multiworld.get_entrance("Flower Cup 1", player),
    #              lambda state: state.has("Progressive Cup Unlock", player, 1))
    #     set_rule(multiworld.get_entrance("Star Cup 1", player),
    #              lambda state: state.has("Progressive Cup Unlock", player, 2))
    #     set_rule(multiworld.get_entrance("Special Cup 1", player),
    #              lambda state: state.has("Progressive Cup Unlock", player, 3))
    # elif opt_game_mode == GameMode.option_courses:
    #     pass

    # Location Rules
    # for _, l in Locations.course_locations.items():
    #     for name, (_, flag) in l.items():
    #         if flag == Locations.Group.hazard and opt_hazard_locations:
    #             if opt_two_player:
    #                 set_rule(multiworld.get_location(name, player),
    #                          lambda state: state.has("P1 Star Power", player) or state.has("P2 Star Power", player))
    #             else:
    #                 set_rule(multiworld.get_location(name, player), lambda state: state.has("P1 Star Power", player))
    if opt.hazards:
        for locations in Locations.course_locations.values():
            for name, (_, group) in locations.items():
                if group == Locations.Group.hazard:
                    set_star_access_rule(name, multiworld, player, opt)
        for name, _ in Locations.shared_hazard_locations.items():
            set_star_access_rule(name, multiworld, player, opt)

    # Completion Condition (Victory Rule)
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)

    # TODO: Clean this section up:
    # Add starting drivers to sphere 0 spoiler log by adding minimum driver(s) as an access rule to the victory location
    # Technically they are needed to get past the driver select screen, but checking the rule for victory is cleaner
    # in code and runtime, and functionally identical since the starting items cannot be lost.
    if opt.two_player:
        add_rule(victory_location, lambda state: (state.has("Driver Unlock Mario", player)
                                                  + state.has("Driver Unlock Luigi", player)
                                                  + state.has("Driver Unlock Peach", player)
                                                  + state.has("Driver Unlock Toad", player)
                                                  + state.has("Driver Unlock Yoshi", player)
                                                  + state.has("Driver Unlock D.K.", player)
                                                  + state.has("Driver Unlock Wario", player)
                                                  + state.has("Driver Unlock Bowser", player)) >= 2)
    else:
        add_rule(victory_location, lambda state: state.has("Driver Unlock Mario", player)
                                                 | state.has("Driver Unlock Luigi", player)
                                                 | state.has("Driver Unlock Peach", player)
                                                 | state.has("Driver Unlock Toad", player)
                                                 | state.has("Driver Unlock Yoshi", player)
                                                 | state.has("Driver Unlock D.K.", player)
                                                 | state.has("Driver Unlock Wario", player)
                                                 | state.has("Driver Unlock Bowser", player))
