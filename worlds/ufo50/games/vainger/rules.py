from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState
from worlds.generic.Rules import set_rule, CollectionRule

if TYPE_CHECKING:
    from ... import UFO50World

# adapted from Barbuta, thanks Scipio! <3

# name upgrades for convenience
heat_mod = "Vainger - Heat Mod"
multi_mod = "Vainger - Multi Mod"
pulse_mod = "Vainger - Pulse Mod"
force_mod = "Vainger - Force Mod"

stabilizer = "Vainger - Stabilizer"
shield_upgrade = "Vainger - Shield Upgrade"
keycode_A = "Vainger - Key Code A"
keycode_B = "Vainger - Key Code B"
keycode_C = "Vainger - Key Code C"
keycode_D = "Vainger - Key Code D"
security_clearance = "Vainger - Progressive Security Clearance"


# can the player do a given hell run?
# TODO: option for this
def hell_run(shield_upgrades_required: int, is_vanilla: bool, state: CollectionState, world: "UFO50World") -> bool:
    return state.count(shield_upgrade, world.player) >= shield_upgrades_required


# can the player beat a given boss? currently checks how many mods the player has,
# whether they have a stabilizer, and if they hit a vibes-based shield threshold.
# TODO: option for this
# difficulty must be between 0 and 4 inclusive
def boss_logic(difficulty: int, state: CollectionState, world:"UFO50World") -> bool:
    player = world.player
    if not state.has_from_list_unique([heat_mod, multi_mod, pulse_mod, force_mod], player, difficulty):
        return False
    if difficulty == 4 and not state.has(stabilizer, player):
        return False
    shield_upgrades_required = [0, 0, 5, 10, 15][difficulty]
    return state.has(shield_upgrade, player, shield_upgrades_required)


# can the player tank two hits from spikes without spike-ng?
# either there and back through one layer, or two hits in and zero out
# TODO: option for this
def spike_tank(state: CollectionState, world: "UFO50World") -> bool:
    player = world.player
    # without magmatek, there's no way to have enough shield to cross the spikes in both directions
    if not state.has(heat_mod, player):
        return False
    shield_upgrades_required = 6  # 105 shield, enough to take two hits with magmatek
    return state.has(shield_upgrade, player, shield_upgrades_required)


def create_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player

    # name regions for convenience
    latomc6 = regions["Vainger - LatomC6 Genepod"]
    latomc9 = regions["Vainger - LatomC9 Genepod"]
    latomd3 = regions["Vainger - LatomD3 Genepod"]
    latomd5 = regions["Vainger - LatomD5 Genepod"]
    latomf5 = regions["Vainger - LatomF5 Genepod"]
    latomf7 = regions["Vainger - LatomF7 Genepod"]
    latomi4 = regions["Vainger - LatomI4 Genepod"]
    latomd6area = regions["Vainger - LatomD6 Area"]

    thetaa4 = regions["Vainger - ThetaA4 Genepod"] 
    thetae9 = regions["Vainger - ThetaE9 Genepod"] 
    thetaf5 = regions["Vainger - ThetaF5 Genepod"] 
    thetaf6 = regions["Vainger - ThetaF6 Genepod"] 
    thetai7 = regions["Vainger - ThetaI7 Genepod"] 
    thetai9 = regions["Vainger - ThetaI9 Genepod"] 
    thetac8loc = regions["Vainger - ThetaC8 Location"]
    thetac10loc = regions["Vainger - ThetaC10 Location"]
    
    verdea1 = regions["Vainger - VerdeA1 Genepod"]
    verdee1 = regions["Vainger - VerdeE1 Genepod"]
    verdee6 = regions["Vainger - VerdeE6 Genepod"]
    verdei7 = regions["Vainger - VerdeI7 Genepod"]
    verdei9 = regions["Vainger - VerdeI9 Genepod"]
    verdeswarea = regions["Vainger - VerdeSW Area"]
    verdeh7loc = regions["Vainger - VerdeH7 Location"]
    
    control = regions["Vainger - Control Genepod"] 

    # ThetaF5 is the starting genepod
    regions["Vainger - Menu"].connect(thetaf5)

    thetaf5.connect(thetai7)
    # whether this hell run should be in logic itemless is a big question. it'll expand the possibilities
    # for heat mod placement a lot, but it's tricky and doing it every single time in sphere 1 could get old fast.
    # currently this is considered logical itemless
    thetaf5.connect(thetaa4,
                    rule=lambda state: state.has(heat_mod, player)
                    or hell_run(0, False, state, world))  # itemless hell run
    thetaf5.connect(control,
                    rule=lambda state: (state.has(heat_mod, player)
                                        or hell_run(0, False, state, world))  # itemless hell run
                    and state.has_all((keycode_A, keycode_B, keycode_C, keycode_D), player))
    thetai7.connect(thetai9)
    thetaa4.connect(latomc9)  # TODO: do we need logic for the miniboss in ThetaB2?
    thetaa4.connect(verdea1)
    thetaa4.connect(thetaf6,
                    rule=lambda state: state.has_any([multi_mod, force_mod], player)
                    or spike_tank(state, world))  # shadow or spike-ng or spike tank
    thetaf6.connect(thetae9,
                    rule=lambda state: state.has("Vainger - ThetaE9 - Boss Defeated", player))  # genepod only exists after boss kill
    thetai9.connect(thetaa4,
                    rule=lambda state: state.has_all((multi_mod, heat_mod), player))  # shadow + hot-shot
    thetai9.connect(verdei7,
                    rule=lambda state: state.has(heat_mod, player))  # hot-shot
    # logic for the two weird locations in Theta SW
    thetai9.connect(thetac10loc,
                    rule=lambda state: state.has_all((multi_mod, heat_mod, force_mod), player))  # shadow + hot-shot + spike-ng
    thetai9.connect(thetac8loc,
                    rule=lambda state: state.has_all((multi_mod, heat_mod), player))  # shadow + hot-shot
    verdea1.connect(thetac10loc,
                    rule=lambda state: state.has(heat_mod, player))  # hot-shot
    verdea1.connect(thetac8loc,
                    rule=lambda state: state.has(heat_mod, player))  # hot-shot
    verdea1.connect(verdee1,
                    rule=lambda state: state.has("Vainger - VerdeE1 - Ramses Defeated", player))  # genepod only exists after boss kill
    verdee1.connect(verdee6)
    verdee1.connect(verdei7)
    verdee6.connect(verdeswarea,
                    rule=lambda state: state.has(security_clearance, player, 2)
                    or state.has(heat_mod, player))  # hot-shot for the shortcut F5 -> E5
    verdei7.connect(verdeswarea,
                    rule=lambda state: state.has(security_clearance, player, 1))
    verdeswarea.connect(verdei9,
                        rule=lambda state: state.has(security_clearance, player, 2)
                        and state.has("Vainger - VerdeI9 - Sura Defeated", player))  # genepod only exists after boss
    # the spike tank strat is unreasonable coming from the left, so the fact that a player coming from the
    # left *might* have used hot-shot to get here is irrelevant.
    verdeswarea.connect(verdeh7loc,
                        rule=lambda state: state.has(force_mod, player))  # spike-ng.
    verdei7.connect(verdeh7loc,
                    rule=lambda state: state.has(force_mod, player) or spike_tank(state, world))  # here spike tanking is reasonable

    # TODO: check how hard this hell run is
    latomc9.connect(latomf7,
                    rule=lambda state: state.has(heat_mod, player)
                    or hell_run(10, False, state, world))  # hot-shot, magmatek, or hell run
    latomc9.connect(latomf5,
                    rule=lambda state: state.has_all((heat_mod, pulse_mod), player))  # hot-shot and thunder
    latomf7.connect(latomc6,
                    rule=lambda state: state.has(security_clearance, player, 3)
                    and state.has_any((pulse_mod, multi_mod), player))  # thunder or tri-shot
    latomf7.connect(latomd3,
                    rule=lambda state: state.has_any([pulse_mod, multi_mod], player))  # thunder or tri-shot
    latomf7.connect(latomf5,
                    rule=lambda state: state.has(pulse_mod, player))  # thunder or possibly tanking an electrical arc later
    latomd3.connect(latomf5)
    latomd3.connect(latomc6,
                    rule=lambda state: state.has(security_clearance, player, 3))
    latomf5.connect(latomd3)
    latomf5.connect(latomc6,
                    rule=lambda state: state.has(security_clearance, player, 2) and state.has(heat_mod, player))  # hot-shot
    latomc6.connect(latomd5,
                    rule=lambda state: state.has(security_clearance, player, 3) and state.has("Vainger - LatomD5 - Boss Defeated", player))
    # TODO: the normal route is one-way; does the miniboss block you from doing the upper route in reverse?
    latomf5.connect(latomi4,
                    rule=lambda state: state.has(pulse_mod, player))  # NOTE: thunder required to prevent a softlock; this means vanilla pulse mod will be impossible.
    latomc6.connect(latomd6area,
                    rule=lambda state: state.has(heat_mod, player))  # hot-shot for the shortcut C6 -> D6
    latomf5.connect(latomd6area,
                    rule=lambda state: state.has(security_clearance, player, 2))
    
    def sr(loc: str, rule: CollectionRule = lambda state: True):
        set_rule(world.get_location(f"Vainger - {loc}"), rule)

    # LatomD3
    # sr("LatomA4 - Shield Upgrade")
    sr("LatomA7 - Shield Upgrade")  # TODO: double-check this, I'm not exactly sure where the upgrade was
    # LatomC9
    sr("LatomA9 - Shield Upgrade", rule=lambda state: state.has(heat_mod, player)
        and hell_run(10, True, state, world))  # mandatory hell run; TODO: check difficulty
    sr("LatomB9 - Shield Upgrade", rule=lambda state: state.has(multi_mod, player))  # shadow
    sr("LatomJ10 - Shield Upgrade", rule=lambda state: state.has(heat_mod, player))  # hot-shot
    # LatomC6
    sr("LatomC4 - Shield Upgrade", rule=lambda state: state.has(security_clearance, player, 3))
    # sr("LatomC6 - Clone Material")
    # LatomD6 Area
    # sr("LatomD6 - Security Clearance") # accounted for by region logic
    # LatomF7
    # sr("LatomG8 - Multi Mod") # the fight here will be a pain itemless but it should be possible
    # LatomI4
    # sr("LatomI4 - Pulse Mod") 
    # LatomF5
    # TODO: does this need to be I4 instead due to the miniboss?
    sr("LatomJ1 - Stabilizer", rule=lambda state: boss_logic(1, state, world)  # TODO: check miniboss difficulty
        and state.has_all((pulse_mod, heat_mod), player) and hell_run(0, True, state, world))

    # sr("LatomE4 - Shield Upgrade")
    sr("LatomJ3 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player)  # including pulse mod to avoid softlocking near I4
        and (state.has(force_mod, player) or spike_tank(state, world)))  # meteor or spike-ng or spike tank
    #
    # Alien boss, from LatomC6
    sr("LatomD5 - Boss Defeated", rule=lambda state: state.has(security_clearance, player, 3)
       and boss_logic(2, state, world))  # TODO: check boss difficulty
    # sr("LatomD5 - Key Code") # relative to boss genepod
    #
    # ThetaA4
    sr("ThetaA2 - Clone Material", rule=lambda state: state.has(force_mod, player)
       or spike_tank(state, world))  # spike-ng or spike tank
    sr("ThetaA3 - Shield Upgrade", rule=lambda state: state.has(force_mod, player)
       or spike_tank(state, world))  # meteor, spike-ng or spike tank
    sr("ThetaC5 - Clone Material", rule=lambda state: state.has(pulse_mod, player))  # zap-shot
    sr("ThetaD7 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player))  # thunder
    # ThetaI7
    # sr("ThetaH1 - Shield Upgrade")
    # sr("ThetaH4 - Heat Mod")
    sr("ThetaI4 - Shield Upgrade", rule=lambda state: state.has(heat_mod, player))  # hot-shot
    sr("ThetaJ7 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player))  # thunder? check this
    #
    # Boss from ThetaF6
    sr("ThetaE9 - Boss Defeated", rule=lambda state: boss_logic(2, state, world))  # TODO: check boss difficulty
    # sr("ThetaE9 - Key Code") # relative to boss genepod
    
    # VerdeA1
    # sr("ThetaA9 - Shield Upgrade") # might be a little tough itemless?
    # sr("VerdeA1 - Shield Upgrade")
    # sr("VerdeC4 - Shield Upgrade")
    # VerdeI7
    # sr("VerdeG10 - Security Clearance")
    sr("VerdeI4 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player))  # thunder
    sr("VerdeJ2 - Stabilizer", rule=lambda state: state.has(pulse_mod, player))  # zap-shot
    sr("VerdeJ9 - Shield Upgrade", rule=lambda state: state.has(force_mod, player))  # meteor
    sr("VerdeG5 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player))  # thunder
    # VerdeSW Area - note that depending on entrance, the player *may* be required to have hot-shot equipped here
    # I found this surprisingly difficult casually, I'm giving it boss logic for now
    sr("VerdeB5 - Force Mod", rule=lambda state: boss_logic(2, state, world))
    # sr("VerdeC5 - Shield Upgrade")
    # sr("VerdeE5 - Security Clearance")
    sr("VerdeF8 - Shield Upgrade", rule=lambda state: state.has(pulse_mod, player))  # thunder

    # Ramses fight, from VerdeA1
    sr("VerdeE1 - Ramses Defeated", rule=lambda state: boss_logic(1, state, world))  # TODO: check difficulty
    # sr("VerdeE1 - Key Code") # relative to boss genepod
    # Sura fight, or maybe Jorgensen. From either E6 or I7 genepod
    sr("VerdeI9 - Sura Defeated", rule=lambda state: state.has(security_clearance, player, 2)
       and boss_logic(3, state, world))  # absolute monster
    # sr("VerdeI9 - Key Code") # relative to boss genepod

    # Control
    # sr("Control - Shield Upgrade") # yeah I was surprised this was itemless
    # boss logic has everything you could want, but be careful if that changes
    sr("Control - Hooper Defeated", rule=lambda state: boss_logic(4, state, world))
    
    # special locations; these are gated by unique regions
    # sr("ThetaC8 - Shield Upgrade")
    # sr("ThetaC10 - Shield Upgrade")
    # sr("VerdeH7 - Shield Upgrade")

    # garden: same logic as heat mod
    # sr("Garden")
    # gold: check the boss defeat state
    sr("Gold", rule=lambda state: state.has("Vainger - Control - Hooper Defeated", player))
    # cherry: beating Hooper requires everything but the security clearance, so checking those two things should be enough
    sr("Cherry", rule=lambda state: state.has("Vainger - Control - Hooper Defeated", player)
        and state.has(security_clearance, player, 3))
