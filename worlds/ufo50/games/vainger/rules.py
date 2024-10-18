from typing import TYPE_CHECKING, Dict
from BaseClasses import Region, CollectionState
from worlds.generic.Rules import set_rule

if TYPE_CHECKING:
    from ... import UFO50World

#TODO: update this

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
def hell_run(shield_upgrades_required: int, is_vanilla: bool, state: CollectionState, world: UFO50World) -> bool:
    player = world.player
    return (state.count(shield_upgrade, player) >= shield_upgrades_required)

# can the player beat a given boss? currently checks how many mods the player has,
# whether they have a stabilizer, and if they hit a vibes-based shield threshold.
# TODO: option for this
# difficulty must be between 0 and 4 inclusive
def boss_logic(difficulty: int, state: CollectionState, world: UFO50World) -> bool:
    player = world.player
    if not state.has_from_list_unique([heat_mod, multi_mod, pulse_mod, force_mod], player, difficulty):
        return False
    if (difficulty == 4) and not state.has(stabilizer):
        return False
    shield_upgrades_required = [0, 0, 5, 10, 15][difficulty]
    return (state.count(shield_upgrade, player) >= shield_upgrades_required)

# can the player tank two hits from spikes without spike-ng? (either there and back through one layer, or two hits in and zero out)
# TODO: option for this
def spike_tank(state: CollectionState, world: UFO50World) -> bool:
    player = world.player
    # without magmatek, there's no way to have enough shield to cross the spikes in both directions, so this isn't logical.
    if not state.has(heat_mod, player):
        return False
    shield_upgrades_required = 6 # 105 shield, enough to take two hits with magmatek
    return (state.count(shield_upgrade, player) >= shield_upgrades_required)


def create_rules(world: "UFO50World", regions: Dict[str, Region]) -> None:
    player = world.player

    # name genepod regions for convenience
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

    # I want each of the region connections to be based on bidirection connectivity, so you can't get stuck.
    # I don't know if that's possible, but it's what I have in mind here.
    thetaf5.connect(thetai7)
    # whether this hell run should be in logic itemless is a big question. it's possible, and it'll expand the possibilities
    # for heat mod placement a lot, but it's tricky and doing it every single time in sphere 1 could get old fast.
    # currently this is considered logical itemless
    thetaf5.connect(thetaa4,
                    rule = lambda state: state.has(heat_mod, player) or hell_run(0, False, state, world)) #itemless hell run
    thetaf5.connect(control,
                    rule = lambda state: (state.has(heat_mod, player) or hell_run(0, False, state, world)) #itemless hell run
                                         and state.has_all([keycode_A, keycode_B, keycode_C, keycode_D], player))
    thetai7.connect(thetai9)
    thetaa4.connect(latomc9,
                    rule = lambda state: state.has("Vainger - ThetaB2 - Miniboss Defeated", player))
    thetaa4.connect(verdea1)
    thetaa4.connect(thetaf6,
                    rule = lambda state: state.has(multi_mod, player)) # shadow, or drone/tri_shot with longshot
    thetaf6.connect(thetae9,
                    rule = lambda state: state.has("Vainger - ThetaE9 - Boss Defeated", player)) # genepod only exists after boss kill
    thetai9.connect(thetaa4,
                    rule = lambda state: state.has_all([multi_mod, heat_mod], player)) # shadow + hot-shot
    thetai9.connect(verdei7,
                    rule = lambda state: state.has(heat_mod, player)) # hot-shot
    # logic for the two weird locations in Theta SW
    thetai9.connect(thetac10loc,
                    rule = lambda state: state.has_all([multi_mod, heat_mod, force_mod], player)) # shadow + hot-shot + spike-ng
    thetai9.connect(thetac8loc,
                    rule = lambda state: state.has_all([multi_mod, heat_mod], player)) # shadow + hot-shot
    verdea1.connect(thetac10loc,
                    rule = lambda state: state.has(heat_mod, player)) # hot-shot
    verdea1.connect(thetac8loc,
                    rule = lambda state: state.has(heat_mod, player)) # hot-shot
    verdea1.connect(verdee1,
                    rule = lambda state: state.has("Vainger - VerdeE5 - Ramses Defeated", player)) # genepod only exists after boss kill
    verdee1.connect(verdee6)
    verdee1.connect(verdei7)
    verdee6.connect(verdeswarea,
                    rule = lambda state: state.count(security_clearance, player) >= 2
                                         or state.has(heat_mod, player)) # hot-shot for the shortcut F5 -> E5
    verdei7.connect(verdeswarea,
                    rule = lambda state: state.count(security_clearance, player) >= 1) 
    verdeswarea.connect(verdei9,
                        rule = lambda state: state.count(security_clearance, player) >= 2 
                                             and state.has("Vainger - VerdeI9 - Sura Defeated", player)) # genepod only exists after boss kill
    # the spike tank strat is unreasonable coming from the left, so the fact that a player coming from the left *might* have used hot-shot
    # to get here is irrelevant.
    verdeswarea.connect(verdeh7loc,
                        rule = lambda state: state.has(force_mod, player)) # spike-ng.
    verdei7.connect(verdeh7loc,
                    rule = lambda state: state.has(force_mod, player) or spike_tank(state, world)) # here spike tanking is reasonable

    #TODO: check how hard this hell run is
    latomc9.connect(latomf7,
                    rule = lambda state: state.has(heat_mod, player) or hell_run(10, False, state, world)) # hot-shot, magmatek, or hell run
    latomc9.connect(latomf5,
                    rule = lambda state: state.has_all([heat_mod, pulse_mod], player)) # hot-shot and thunder
    latomf7.connect(latomc6,
                    rule = lambda state: state.count(security_clearance, player) >= 3
                                         and state.has_any([pulse_mod, multi_mod], player)) # thunder or tri-shot
    latomf7.connect(latomd3,
                    rule = lambda state: state.has_any([pulse_mod, multi_mod], player)) # thunder or tri-shot
    #TODO: latomf7.connect(latomf5, rule = ???)
    #TODO: think through latom logic again, especially in light of hell run and needing pulse/multi for left route from f7
    latomd3.connect(latomf5)
    latomf5.connect(latomc6,
                    rule = lambda state: state.count(security_clearance, player) >= 2 and state.has(heat_mod, player)) # hot-shot
    latomc6.connect(latomd5,
                    rule = lambda state: state.count(security_clearance, player) >= 3 and state.has("Vainger - LatosD5 - Boss Defeated", player))
    latomf5.connect(latomi4,
                    rule = lambda state: state.has(pulse_mod, player)) # NOTE: thunder required to prevent a softlock; this means vanilla pulse mod will be impossible.
    latomc6.connect(latomd6area,
                    rule = lambda state: state.has(heat_mod, player)) # hot-shot for the shortcut C6 -> D6
    latomf5.connect(latomd6area,
                    rule = lambda state: state.count(security_clearance, player) >= 2)
    
    #TODO: location rules

    #
    #set_rule(world.get_location("Barbuta - Chest - G2"),
    #         rule=lambda state: state.has(pin, player))
    #
    ## todo: finalize this
    #set_rule(world.get_location("Barbuta - Beat the Boss"),
    #         rule=lambda state: state.has_any((blood_sword, wand, bat_orb), player))
