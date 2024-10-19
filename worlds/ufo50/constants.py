from typing import Dict

GAME_NAME: str = "UFO 50"
BASE_ID: int = 0x55464F3530  # UFO50

# client installation data
CLIENT_NAME = f"{GAME_NAME.replace(' ', '')}Client"
GAME_HASH = "b2408e0357ef3cb62bae6af109cd5819"  # md5 for data.win
DLL_NAME = "gm-apclientpp.dll"
DLL_URL = "https://api.github.com/repos/black-sliver/gm-apclientpp/releases"
PATCH_NAME = "ufo_50_basepatch.bsdiff4"
PATCH_URL = "https://api.github.com/repos/UFO-50-Archipelago/basepatch/releases"

game_ids: Dict[str, int] = {
    "Barbuta": 1,
    "Bug Hunter": 2,
    "Ninpek": 3,
    "Paint Chase": 4,
    "Magic Garden": 5,
    "Mortol": 6,
    "Velgress": 7,
    "Planet Zoldath": 8,
    "Attactics": 9,
    "Devilition": 10,
    "Kick Club": 11,
    "Avianos": 12,
    "Mooncat": 13,
    "Bushido Ball": 14,
    "Block Koala": 15,
    "Camouflage": 16,
    "Campanella": 17,
    "Golfaria": 18,
    "The Big Bell Race": 19,
    "Warptank": 20,
    "Waldorf's Journey": 21,
    "Porgy": 22,
    "Onion Delivery": 23,
    "Caramel Caramel": 24,
    "Party House": 25,
    "Hot Foot": 26,
    "Divers": 27,
    "Rail Heist": 28,
    "Vainger": 29,
    "Rock On! Island": 30,
    "Pingolf": 31,
    "Mortol II": 32,
    "Fist Hell": 33,
    "Overbold": 34,
    "Campanella 2": 35,
    "Hyper Contender": 36,
    "Valbrace": 37,
    "Rakshasa": 38,
    "Star Waspir": 39,
    "Grimstone": 40,
    "Lords of Diskonia": 41,
    "Night Manor": 42,
    "Elfazar's Hat": 43,
    "Pilot Quest": 44,
    "Mini & Max": 45,
    "Combatants": 46,
    "Quibble Race": 47,
    "Seaside Drive": 48,
    "Campanella 3": 49,
    "Cyber Owls": 50,
}
