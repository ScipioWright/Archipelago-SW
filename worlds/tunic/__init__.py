from typing import Dict, List, Any, Tuple, TypedDict, ClassVar, Union, Set, TextIO
from logging import warning
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld, CollectionState
from .items import (item_name_to_id, item_table, item_name_groups, fool_tiers, filler_items, slot_data_item_names,
                    combat_items)
from .locations import location_table, location_name_groups, standard_location_name_to_id, hexagon_locations
from .rules import set_location_rules, set_region_rules, randomize_ability_unlocks, gold_hexagon
from .er_rules import set_er_location_rules
from .regions import tunic_regions
from .er_scripts import create_er_regions
from .grass import grass_location_table, grass_location_name_to_id, grass_location_name_groups, excluded_grass_locations
from .er_data import portal_mapping, RegionInfo, tunic_er_regions
from .options import (TunicOptions, EntranceRando, tunic_option_groups, tunic_option_presets, TunicPlandoConnections,
                      LaurelsLocation, LogicRules, LaurelsZips, IceGrappling, LadderStorage, check_options,
                      get_hexagons_in_pool, HexagonQuestAbilityUnlockType)
from .breakables import breakable_location_name_to_id, breakable_location_groups, breakable_location_table
from .combat_logic import area_data, CombatState
from worlds.AutoWorld import WebWorld, World
from Options import PlandoConnection, OptionError
from settings import Group, Bool, FilePath


class TunicSettings(Group):
    class DisableLocalSpoiler(Bool):
        """Disallows the TUNIC client from creating a local spoiler log."""

    class LimitGrassRando(Bool):
        """Limits the impact of Grass Randomizer on the multiworld by disallowing local_fill percentages below 95."""

    class UTPoptrackerPath(FilePath):
        """Path to the user's TUNIC Poptracker Pack."""
        description = "TUNIC Poptracker Pack zip file"
        required = False

    disable_local_spoiler: Union[DisableLocalSpoiler, bool] = False
    limit_grass_rando: Union[LimitGrassRando, bool] = True
    ut_poptracker_path: Union[UTPoptrackerPath, str] = UTPoptrackerPath()


class TunicWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name="Multiworld Setup Guide",
            description="A guide to setting up the TUNIC Randomizer for Archipelago multiworld games.",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["SilentDestroyer"]
        )
    ]
    theme = "grassFlowers"
    game = "TUNIC"
    option_groups = tunic_option_groups
    options_presets = tunic_option_presets


class TunicItem(Item):
    game: str = "TUNIC"


class TunicLocation(Location):
    game: str = "TUNIC"


class SeedGroup(TypedDict):
    laurels_zips: bool  # laurels_zips value
    ice_grappling: int  # ice_grappling value
    ladder_storage: int  # ls value
    laurels_at_10_fairies: bool  # laurels location value
    fixed_shop: bool  # fixed shop value
    plando: TunicPlandoConnections  # consolidated plando connections for the seed group


class TunicWorld(World):
    """
    Explore a land filled with lost legends, ancient powers, and ferocious monsters in TUNIC, an isometric action game
    about a small fox on a big adventure. Stranded on a mysterious beach, armed with only your own curiosity, you will
    confront colossal beasts, collect strange and powerful items, and unravel long-lost secrets. Be brave, tiny fox!
    """
    game = "TUNIC"
    web = TunicWeb()

    def map_page_index(data: Any) -> int:
        mapping: dict[str, int] = {
            "Beneath the Earth": 1,
            "Beneath the Well": 2,
            "The Cathedral": 3,
            "Dark Tomb": 4,
            "Eastern Vault": 5,
            "Frog's Domain": 6,
            "Swamp": 7,
            "Overworld": 8,
            "The Quarry": 9,
            "Ruined Atoll": 10,
            "West Gardens": 11,
            "The Grand Library": 12,
            "East Forest": 13,
            "The Far Shore": 14,
            "The Rooted Ziggurat": 15,
        }
        return mapping.get(data, 0)

    # mapping of everything after the second to last slash and the location id
    # lua used for the name: string.match(full_name, "[^/]*/[^/]*$")
    poptracker_data: dict[str, int] = {
        "[Powered Secret Room] Chest/Follow the Purple Energy Road": 509342400,
        "[Entryway] Chest/Mind the Slorms": 509342401,
        "[Third Room] Beneath Platform Chest/Run from the tentacles!": 509342402,
        "[Third Room] Tentacle Chest/Water Sucks": 509342403,
        "[Entryway] Obscured Behind Waterfall/You can just go in there": 509342404,
        "[Save Room] Upper Floor Chest 1/Through the Power of Prayer": 509342405,
        "[Save Room] Upper Floor Chest 2/Above the Fox Shrine": 509342406,
        "[Second Room] Underwater Chest/Hidden Passage": 509342407,
        "[Back Corridor] Right Secret/Hidden Path": 509342408,
        "[Back Corridor] Left Secret/Behind the Slorms": 509342409,
        "[Second Room] Obscured Behind Waterfall/Just go in there": 509342410,
        "[Side Room] Chest By Pots/Just Climb up There": 509342411,
        "[Side Room] Chest By Phrends/So Many Phrends!": 509342412,
        "[Second Room] Page/Ruined Atoll Map": 509342413,
        "[Passage To Dark Tomb] Page Pickup/Siege Engine": 509342414,
        "[1F] Guarded By Lasers/Beside 3 Miasma Seekers": 509342415,
        "[1F] Near Spikes/Mind the Miasma Seeker": 509342416,
        "Birdcage Room/[2F] Bird Room": 509342417,
        "[2F] Entryway Upper Walkway/Overlooking Miasma": 509342418,
        "[1F] Library/By the Books": 509342419,
        "[2F] Library/Behind the Ladder": 509342420,
        "[2F] Guarded By Lasers/Before the big reveal...": 509342421,
        "Birdcage Room/[2F] Bird Room Secret": 509342422,
        "[1F] Library Secret/Pray to the Wallman": 509342423,
        "Spike Maze Near Exit/Watch out!": 509342424,
        "2nd Laser Room/Can you roll?": 509342425,
        "1st Laser Room/Use a bomb?": 509342426,
        "Spike Maze Upper Walkway/Just walk right!": 509342427,
        "Skulls Chest/Move the Grave": 509342428,
        "Spike Maze Near Stairs/In the Corner": 509342429,
        "1st Laser Room Obscured/Follow the red laser of death": 509342430,
        "Guardhouse 2 - Upper Floor/In the Mound": 509342431,
        "Guardhouse 2 - Bottom Floor Secret/Hidden Hallway": 509342432,
        "Guardhouse 1 Obscured/Upper Floor Obscured": 509342433,
        "Guardhouse 1/Upper Floor": 509342434,
        "Guardhouse 1 Ledge HC/Dancing Fox Spirit Holy Cross": 509342435,
        "Golden Obelisk Holy Cross/Use the Holy Cross": 509342436,
        "Ice Rod Grapple Chest/Freeze the Blob and ascend With Orb": 509342437,
        "Above Save Point/Chest": 509342438,
        "Above Save Point Obscured/Hidden Path": 509342439,
        "Guardhouse 1 Ledge/From Guardhouse 1 Chest": 509342440,
        "Near Save Point/Chest": 509342441,
        "Ambushed by Spiders/Beneath Spider Chest": 509342442,
        "Near Telescope/Up on the Wall": 509342443,
        "Ambushed by Spiders/Spider Chest": 509342444,
        "Lower Dash Chest/Dash Across": 509342445,
        "Lower Grapple Chest/Grapple Across": 509342446,
        "Bombable Wall/Follow the Flowers": 509342447,
        "Page On Teleporter/Page": 509342448,
        "Forest Belltower Save Point/Near Save Point": 509342449,
        "Forest Belltower - After Guard Captain/Chest": 509342450,
        "East Bell/Forest Belltower - Obscured Near Bell Top Floor": 509342451,
        "Forest Belltower Obscured/Obscured Beneath Bell Bottom Floor": 509342452,
        "Forest Belltower Page/Page Pickup": 509342453,
        "Forest Grave Path - Holy Cross Code by Grave/Single Money Chest": 509342454,
        "Forest Grave Path - Above Gate/Chest": 509342455,
        "Forest Grave Path - Obscured Chest/Behind the Trees": 509342456,
        "Forest Grave Path - Upper Walkway/From the top of the Guardhouse": 509342457,
        "The Hero's Sword/Forest Grave Path - Sword Pickup": 509342458,
        "The Hero's Sword/Hero's Grave - Tooth Relic": 509342459,
        "Fortress Courtyard - From East Belltower/Crack in the Wall": 509342460,
        "Fortress Leaf Piles - Secret Chest/Dusty": 509342461,
        "Fortress Arena/Hexagon Red": 509342462,
        "Fortress Arena/Siege Engine|Vault Key Pickup": 509342463,
        "Fortress East Shortcut - Chest Near Slimes/Mind the Custodians": 509342464,
        "[West Wing] Candles Holy Cross/Use the Holy Cross": 509342465,
        "Westmost Upper Room/[West Wing] Dark Room Chest 1": 509342466,
        "Westmost Upper Room/[West Wing] Dark Room Chest 2": 509342467,
        "[East Wing] Bombable Wall/Bomb the Wall": 509342468,
        "[West Wing] Page Pickup/He will never visit the Far Shore": 509342469,
        "Fortress Grave Path - Upper Walkway/Go Around the East Wing": 509342470,
        "Vault Hero's Grave/Fortress Grave Path - Chest Right of Grave": 509342471,
        "Vault Hero's Grave/Fortress Grave Path - Obscured Chest Left of Grave": 509342472,
        "Vault Hero's Grave/Hero's Grave - Flowers Relic": 509342473,
        "Bridge/Chest": 509342474,
        "Cell Chest 1/Drop the Shortcut Rope": 509342475,
        "Obscured Behind Waterfall/Muffling Bell": 509342476,
        "Back Room Chest/Lose the Lure or take 2 Damage": 509342477,
        "Cell Chest 2/Mind the Custodian": 509342478,
        "Near Vault/Already Stolen": 509342479,
        "Slorm Room/Tobias was Trapped Here Once...": 509342480,
        "Escape Chest/Don't Kick Fimbleton!": 509342481,
        "Grapple Above Hot Tub/Look Up": 509342482,
        "Above Vault/Obscured Doorway Ledge": 509342483,
        "Main Room Top Floor/Mind the Adult Frog": 509342484,
        "Main Room Bottom Floor/Altar Chest": 509342485,
        "Side Room Secret Passage/Upper Right Corner": 509342486,
        "Side Room Chest/Oh No! Our Frogs! They're Dead!": 509342487,
        "Side Room Grapple Secret/Grapple on Over": 509342488,
        "Magic Orb Pickup/Frult Meeting": 509342489,
        "The Librarian/Hexagon Green": 509342490,
        "Library Hall/Holy Cross Chest": 509342491,
        "Library Lab Chest by Shrine 2/Chest": 509342492,
        "Library Lab Chest by Shrine 1/Chest": 509342493,
        "Library Lab Chest by Shrine 3/Chest": 509342494,
        "Library Lab by Fuse/Behind Chalkboard": 509342495,
        "Library Lab Page 3/Page": 509342496,
        "Library Lab Page 1/Page": 509342497,
        "Library Lab Page 2/Page": 509342498,
        "Hero's Grave/Mushroom Relic": 509342499,
        "Mountain Door/Lower Mountain - Page Before Door": 509342500,
        "Changing Room/Normal Chest": 509342501,
        "Fortress Courtyard - Chest Near Cave/Next to the Obelisk": 509342502,
        "Fortress Courtyard - Near Fuse/Pray": 509342503,
        "Fortress Courtyard - Below Walkway/Under the Stairs": 509342504,
        "Fortress Courtyard - Page Near Cave/Heir-To-The-Heir": 509342505,
        "West Furnace/Lantern Pickup": 509342506,
        "Maze Cave/Maze Room Chest": 509342507,
        "Inside the Old House/Normal Chest": 509342508,
        "Inside the Old House/Shield Pickup": 509342509,
        "[West] Obscured Behind Windmill/Behind the Trees": 509342510,
        "[South] Beach Chest/Beside the Bridge": 509342511,
        "[West] Obscured Near Well/Hidden by Trees": 509342512,
        "[Central] Bombable Wall/Let the flowers guide you": 509342513,
        "[Northwest] Chest Near Turret/Mind the Autobolt...": 509342514,
        "[East] Chest Near Pots/Chest": 509342515,
        "[Northwest] Chest Near Golden Obelisk/Underneath the Staff": 509342516,
        "[Southwest] South Chest Near Guard/End of the Bridge": 509342517,
        "[Southwest] West Beach Guarded By Turret/Chest": 509342518,
        "[Southwest] Chest Guarded By Turret/Behind the Trees": 509342519,
        "[Northwest] Shadowy Corner Chest/Dark Ramps Chest": 509342520,
        "[Southwest] Obscured In Tunnel To Beach/Deep in the Wall": 509342521,
        "[Southwest] Grapple Chest Over Walkway/Jeffry": 509342522,
        "[Northwest] Chest Beneath Quarry Gate/Across the Bridge": 509342523,
        "[Southeast] Chest Near Swamp/Under the Bridge": 509342524,
        "[Southwest] From West Garden/Dash Across": 509342525,
        "[East] Grapple Chest/Grapple Across": 509342526,
        "[Southwest] West Beach Guarded By Turret 2/Get Across": 509342527,
        "Sand Hook/[Southwest] Beach Chest Near Flowers": 509342528,
        "[Southwest] Bombable Wall Near Fountain/Let the flowers guide you": 509342529,
        "[West] Chest After Bell/Post-Dong!": 509342530,
        "[Southwest] Tunnel Guarded By Turret/Below Jeffry": 509342531,
        "[East] Between ladders near Ruined Passage/Chest": 509342532,
        "[Northeast] Chest Above Patrol Cave/Behind Blue Rudelings": 509342533,
        "[Southwest] Beach Chest Beneath Guard/Under Bridge": 509342534,
        "[Central] Chest Across From Well/Across the Bridge": 509342535,
        "[Northwest] Chest Near Quarry Gate/Rudeling Camp": 509342536,
        "[East] Chest In Trees/Above Locked House": 509342537,
        "[West] Chest Behind Moss Wall/Around the Corner": 509342538,
        "[South] Beach Page/Page": 509342539,
        "[Southeast] Page on Pillar by Swamp/Dash Across": 509342540,
        "[Southwest] Key Pickup/Old House Key": 509342541,
        "[West] Key Pickup/Hero's Path Key": 509342542,
        "[East] Page Near Secret Shop/Page": 509342543,
        "Fountain/[Southwest] Fountain Page": 509342544,
        "[Northwest] Page on Pillar by Dark Tomb/A Terrible Power Rises": 509342545,
        "Magic Staff/[Northwest] Fire Wand Pickup": 509342546,
        "[West] Page on Teleporter/Treasures and Tools": 509342547,
        "[Northwest] Page By Well/If you seek to increase your power...": 509342548,
        "Patrol Cave/Normal Chest": 509342549,
        "Ruined Shop/Chest 1": 509342550,
        "Ruined Shop/Chest 2": 509342551,
        "Ruined Shop/Chest 3": 509342552,
        "Ruined Passage/Page Pickup": 509342553,
        "Shop/Potion 1": 509342554,
        "Shop/Potion 2": 509342555,
        "Shop/Coin 1": 509342556,
        "Shop/Coin 2": 509342557,
        "Special Shop/Secret Page Pickup": 509342558,
        "Stick House/Stick Chest": 509342559,
        "Sealed Temple/Page Pickup": 509342560,
        "Inside Hourglass Cave/Hourglass Chest": 509342561,
        "Secret Chest/Dash Across": 509342562,
        "Page Pickup/A Long, Long Time Ago...": 509342563,
        "Coins in the Well/10 Coins": 509342564,
        "Coins in the Well/15 Coins": 509342565,
        "Coins in the Well/3 Coins": 509342566,
        "Coins in the Well/6 Coins": 509342567,
        "Secret Gathering Place/20 Fairy Reward": 509342568,
        "Secret Gathering Place/10 Fairy Reward": 509342569,
        "[West] Moss Wall Holy Cross/Use the Holy Cross": 509342570,
        "[Southwest] Flowers Holy Cross/Use the Holy Cross": 509342571,
        "Fountain/[Southwest] Fountain Holy Cross": 509342572,
        "[Northeast] Flowers Holy Cross/Use the Holy Cross": 509342573,
        "[East] Weathervane Holy Cross/Use the Holy Cross": 509342574,
        "[West] Windmill Holy Cross/Sacred Geometry": 509342575,
        "Sand Hook/[Southwest] Haiku Holy Cross": 509342576,
        "[West] Windchimes Holy Cross/Power Up!": 509342577,
        "[South] Starting Platform Holy Cross/Back to Work": 509342578,
        "Magic Staff/[Northwest] Golden Obelisk Page": 509342579,
        "Inside the Old House/Holy Cross Door Page": 509342580,
        "Cube Cave/Holy Cross Chest": 509342581,
        "Southeast Cross Door/Chest 3": 509342582,
        "Southeast Cross Door/Chest 2": 509342583,
        "Southeast Cross Door/Chest 1": 509342584,
        "Maze Cave/Maze Room Holy Cross": 509342585,
        "Caustic Light Cave/Holy Cross Chest": 509342586,
        "Inside the Old House/Holy Cross Chest": 509342587,
        "Patrol Cave/Holy Cross Chest": 509342588,
        "Ruined Passage/Holy Cross Chest": 509342589,
        "Inside Hourglass Cave/Holy Cross Chest": 509342590,
        "Sealed Temple/Holy Cross Chest": 509342591,
        "Fountain Cross Door/Page Pickup": 509342592,
        "Secret Gathering Place/Holy Cross Chest": 509342593,
        "Mountain Door/Top of the Mountain - Page At The Peak": 509342594,
        "Monastery/Monastery Chest": 509342595,
        "[Back Entrance] Bushes Holy Cross/Use the Holy Cross": 509342596,
        "[Back Entrance] Chest/Peaceful Chest": 509342597,
        "[Central] Near Shortcut Ladder/By the Boxes": 509342598,
        "[East] Near Telescope/Spoopy": 509342599,
        "[East] Upper Floor/Reminds me of Blighttown": 509342600,
        "[Central] Below Entry Walkway/Even more Stairs!": 509342601,
        "[East] Obscured Near Winding Staircase/At the Bottom": 509342602,
        "[East] Obscured Beneath Scaffolding/In the Miasma Mound": 509342603,
        "[East] Obscured Near Telescope/Weird path?": 509342604,
        "[Back Entrance] Obscured Behind Wall/Happy Water!": 509342605,
        "[Central] Obscured Below Entry Walkway/Down the Stairs": 509342606,
        "[Central] Top Floor Overhang/End of the ruined bridge": 509342607,
        "[East] Near Bridge/Drop that Bridge!": 509342608,
        "[Central] Above Ladder/Climb Ladder": 509342609,
        "[Central] Obscured Behind Staircase/At the Bottom": 509342610,
        "[Central] Above Ladder Dash Chest/Dash Across": 509342611,
        "[West] Upper Area Bombable Wall/Boomy": 509342612,
        "[East] Bombable Wall/Flowers Guide Thee": 509342613,
        "Monastery/Hero's Grave - Ash Relic": 509342614,
        "[West] Shooting Range Secret Path/Obscured Path": 509342615,
        "[West] Near Shooting Range/End of bridge": 509342616,
        "[West] Below Shooting Range/Clever little sneak!": 509342617,
        "[Lowlands] Below Broken Ladder/Miasma Pits": 509342618,
        "[West] Upper Area Near Waterfall/Yummy Polygons": 509342619,
        "[Lowlands] Upper Walkway/Hate them Snipers": 509342620,
        "[West] Lower Area Below Bridge/Go Around": 509342621,
        "[West] Lower Area Isolated Chest/Burn Pots": 509342622,
        "[Lowlands] Near Elevator/End of the Tracks": 509342623,
        "[West] Lower Area After Bridge/Drop that Bridge!": 509342624,
        "Upper - Near Bridge Switch/You can shoot it": 509342625,
        "Upper - Beneath Bridge To Administrator/End of the First Floor": 509342626,
        "Tower - Inside Tower/I'm Scared": 509342627,
        "Lower - Near Corpses/They are Dead": 509342628,
        "Lower - Spider Ambush/Use the Gun": 509342629,
        "Lower - Left Of Checkpoint Before Fuse/Moment of Reprieve": 509342630,
        "Lower - After Guarded Fuse/Defeat those Mechs": 509342631,
        "Lower - Guarded By Double Turrets/Help": 509342632,
        "Lower - After 2nd Double Turret Chest/Haircut Time!": 509342633,
        "Lower - Guarded By Double Turrets 2/Oh god they're everywhere": 509342634,
        "Lower - Hexagon Blue/Scavenger Queen": 509342635,
        "[West] Near Kevin Block/Phonomath": 509342636,
        "[South] Upper Floor On Power Line/Hidden Ladder Chest": 509342637,
        "[South] Chest Near Big Crabs/His Name is Tom": 509342638,
        "[North] Guarded By Bird/Skraw!": 509342639,
        "[Northeast] Chest Beneath Brick Walkway/Mind the Crabbits": 509342640,
        "[Northwest] Bombable Wall/Flowers Guide Thee": 509342641,
        "[North] Obscured Beneath Bridge/In the shallow water": 509342642,
        "[South] Upper Floor On Bricks/Up the Ladder": 509342643,
        "[South] Near Birds/Danlarry and Thranmire ate Jerry!": 509342644,
        "[Northwest] Behind Envoy/Mind the Fairies": 509342645,
        "[Southwest] Obscured Behind Fuse/Saved by the Prayer": 509342646,
        "Locked Brick House/[East] Locked Room Upper Chest": 509342647,
        "[North] From Lower Overworld Entrance/Come from the Overworld": 509342648,
        "Locked Brick House/[East] Locked Room Lower Chest": 509342649,
        "[Northeast] Chest On Brick Walkway/Near Domain": 509342650,
        "[Southeast] Chest Near Fuse/Around the Tower": 509342651,
        "[Northeast] Key Pickup/Around the Hill": 509342652,
        "Cathedral Gauntlet/Gauntlet Reward": 509342653,
        "Secret Legend Trophy Chest/You can use the Holy Cross from the outside": 509342654,
        "[Upper Graveyard] Obscured Behind Hill/Between Two Hills": 509342655,
        "[South Graveyard] 4 Orange Skulls/DJ Khaled - Let's go Golfing!": 509342656,
        "[Central] Near Ramps Up/Up them Ramps": 509342657,
        "[Upper Graveyard] Near Shield Fleemers/Alternatively, Before the Cathedral": 509342658,
        "[South Graveyard] Obscured Behind Ridge/Hidden passage by ladder": 509342659,
        "[South Graveyard] Obscured Beneath Telescope/Through the Nook": 509342660,
        "[Entrance] Above Entryway/Dash Across": 509342661,
        "[Central] South Secret Passage/Wall Man Approves these Vibes": 509342662,
        "[South Graveyard] Upper Walkway On Pedestal/Gazing out over the Graves": 509342663,
        "[South Graveyard] Guarded By Tentacles/Isolated Island": 509342664,
        "[Upper Graveyard] Near Telescope/Overlooking the Graves": 509342665,
        "[Outside Cathedral] Near Moonlight Bridge Door/Down the Hidden Ladder": 509342666,
        "[Entrance] Obscured Inside Watchtower/Go Inside": 509342667,
        "[Entrance] South Near Fence/DAGGER STRAP!!!!!": 509342668,
        "[South Graveyard] Guarded By Big Skeleton/Super Clipping": 509342669,
        "[South Graveyard] Chest Near Graves/The Rest of Our Entire Life is Death": 509342670,
        "[Entrance] North Small Island/Mildly Hidden": 509342671,
        "First Hero's Grave/[Outside Cathedral] Obscured Behind Memorial": 509342672,
        "[Central] Obscured Behind Northern Mountain/Hug the Wall": 509342673,
        "[South Graveyard] Upper Walkway Dash Chest/Around the Hill": 509342674,
        "[South Graveyard] Above Big Skeleton/End of Ledge": 509342675,
        "[Central] Beneath Memorial/Do You Even Live?": 509342676,
        "First Hero's Grave/Hero's Grave - Feathers Relic": 509342677,
        "West Furnace/Chest": 509342678,
        "[West] Near Gardens Entrance/Effigy Skip": 509342679,
        "[Central Highlands] Holy Cross (Blue Lines)/Use the Holy Cross": 509342680,
        "[West Lowlands] Tree Holy Cross Chest/Use the Holy Cross": 509342681,
        "[Southeast Lowlands] Outside Cave/Mind the Chompignoms!": 509342682,
        "[Central Lowlands] Chest Beneath Faeries/As you walk by": 509342683,
        "[North] Behind Holy Cross Door/Extra Sword!": 509342684,
        "[Central Highlands] Top of Ladder Before Boss/Try to be This Strong": 509342685,
        "[Central Lowlands] Passage Beneath Bridge/Take the lower path": 509342686,
        "[North] Across From Page Pickup/I Love Fish!": 509342687,
        "[Central Lowlands] Below Left Walkway/Dash Across": 509342688,
        "[West] In Flooded Walkway/Dash through the water": 509342689,
        "[West] Past Flooded Walkway/Through the Shallow Water": 509342690,
        "[North] Obscured Beneath Hero's Memorial/Take the Long Way Around": 509342691,
        "[Central Lowlands] Chest Near Shortcut Bridge/Between a Rope and a Bridge Place": 509342692,
        "[West Highlands] Upper Left Walkway/By the Rudeling": 509342693,
        "[Central Lowlands] Chest Beneath Save Point/Behind the Way": 509342694,
        "[Central Highlands] Behind Guard Captain/Under Boss Ladder": 509342695,
        "[Central Highlands] After Garden Knight/Did Not Kill You": 509342696,
        "[South Highlands] Secret Chest Beneath Fuse/Pray to the Wall Man": 509342697,
        "[East Lowlands] Page Behind Ice Dagger House/Come from the Far Shore": 509342698,
        "[North] Page Pickup/Survival Tips": 509342699,
        "[Southeast Lowlands] Ice Dagger Pickup/Ice Dagger Cave": 509342700,
        "Hero's Grave/Effigy Relic": 509342701,
    }

    tracker_world = {
        "map_page_maps": ["maps/maps_pop.json"],
        "map_page_locations": ["locations/locations_pop_er.json"],
        "map_page_setting_key": "Slot:{player}:Current Map",
        "map_page_index": map_page_index,
        "external_pack_key": "ut_poptracker_path",
        "poptracker_name_mapping": poptracker_data
    }

    options: TunicOptions
    options_dataclass = TunicOptions
    settings: ClassVar[TunicSettings]
    item_name_groups = item_name_groups
    location_name_groups = location_name_groups
    for group_name, members in grass_location_name_groups.items():
        location_name_groups.setdefault(group_name, set()).update(members)
    for group_name, members in breakable_location_groups.items():
        location_name_groups.setdefault(group_name, set()).update(members)

    item_name_to_id = item_name_to_id
    location_name_to_id = standard_location_name_to_id.copy()
    location_name_to_id.update(grass_location_name_to_id)
    location_name_to_id.update(breakable_location_name_to_id)

    player_location_table: Dict[str, int]
    ability_unlocks: Dict[str, int]
    slot_data_items: List[TunicItem]
    tunic_portal_pairs: Dict[str, str]
    er_portal_hints: Dict[int, str]
    seed_groups: Dict[str, SeedGroup] = {}
    shop_num: int = 1  # need to make it so that you can walk out of shops, but also that they aren't all connected
    er_regions: Dict[str, RegionInfo]  # absolutely needed so outlet regions work

    # for the local_fill option
    fill_items: List[TunicItem]
    fill_locations: List[Location]
    amount_to_local_fill: int

    # so we only loop the multiworld locations once
    # if these are locations instead of their info, it gives a memory leak error
    item_link_locations: Dict[int, Dict[str, List[Tuple[int, str]]]] = {}
    player_item_link_locations: Dict[str, List[Location]]

    using_ut: bool  # so we can check if we're using UT only once
    passthrough: Dict[str, Any]
    ut_can_gen_without_yaml = True  # class var that tells it to ignore the player yaml

    def generate_early(self) -> None:
        try:
            int(self.settings.disable_local_spoiler)
        except AttributeError:
            raise Exception("You have a TUNIC APWorld in your lib/worlds folder and custom_worlds folder.\n"
                            "This would cause an error at the end of generation.\n"
                            "Please remove one of them, most likely the one in lib/worlds.")

        check_options(self)

        if self.options.logic_rules >= LogicRules.option_no_major_glitches:
            self.options.laurels_zips.value = LaurelsZips.option_true
            self.options.ice_grappling.value = IceGrappling.option_medium
            if self.options.logic_rules.value == LogicRules.option_unrestricted:
                self.options.ladder_storage.value = LadderStorage.option_medium

        self.er_regions = tunic_er_regions.copy()
        if self.options.plando_connections:
            for index, cxn in enumerate(self.options.plando_connections):
                # making shops second to simplify other things later
                if cxn.entrance.startswith("Shop"):
                    replacement = PlandoConnection(cxn.exit, "Shop Portal", "both")
                    self.options.plando_connections.value.remove(cxn)
                    self.options.plando_connections.value.insert(index, replacement)
                elif cxn.exit.startswith("Shop"):
                    replacement = PlandoConnection(cxn.entrance, "Shop Portal", "both")
                    self.options.plando_connections.value.remove(cxn)
                    self.options.plando_connections.value.insert(index, replacement)

        # Universal tracker stuff, shouldn't do anything in standard gen
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "TUNIC" in self.multiworld.re_gen_passthrough:
                self.using_ut = True
                self.passthrough = self.multiworld.re_gen_passthrough["TUNIC"]
                self.options.start_with_sword.value = self.passthrough["start_with_sword"]
                self.options.keys_behind_bosses.value = self.passthrough["keys_behind_bosses"]
                self.options.sword_progression.value = self.passthrough["sword_progression"]
                self.options.ability_shuffling.value = self.passthrough["ability_shuffling"]
                self.options.laurels_zips.value = self.passthrough["laurels_zips"]
                self.options.ice_grappling.value = self.passthrough["ice_grappling"]
                self.options.ladder_storage.value = self.passthrough["ladder_storage"]
                self.options.ladder_storage_without_items = self.passthrough["ladder_storage_without_items"]
                self.options.lanternless.value = self.passthrough["lanternless"]
                self.options.maskless.value = self.passthrough["maskless"]
                self.options.hexagon_quest.value = self.passthrough["hexagon_quest"]
                self.options.hexagon_quest_ability_type.value = self.passthrough.get("hexagon_quest_ability_type", 0)
                self.options.entrance_rando.value = self.passthrough["entrance_rando"]
                self.options.shuffle_ladders.value = self.passthrough["shuffle_ladders"]
                self.options.grass_randomizer.value = self.passthrough.get("grass_randomizer", 0)
                self.options.breakable_shuffle.value = self.passthrough.get("breakable_shuffle", 0)
                self.options.laurels_location.value = self.options.laurels_location.option_anywhere
                self.options.combat_logic.value = self.passthrough["combat_logic"]

                self.options.fixed_shop.value = self.options.fixed_shop.option_false
                if ("ziggurat2020_3, ziggurat2020_1_zig2_skip" in self.passthrough["Entrance Rando"].keys()
                        or "ziggurat2020_3, ziggurat2020_1_zig2_skip" in self.passthrough["Entrance Rando"].values()):
                    self.options.fixed_shop.value = self.options.fixed_shop.option_true

            else:
                self.using_ut = False
        else:
            self.using_ut = False

        self.player_location_table = standard_location_name_to_id.copy()

        if self.options.local_fill == -1:
            if self.options.grass_randomizer:
                if self.options.breakable_shuffle:
                    self.options.local_fill.value = 96
                else:
                    self.options.local_fill.value = 95
            elif self.options.breakable_shuffle:
                self.options.local_fill.value = 40
            else:
                self.options.local_fill.value = 0

        if self.options.grass_randomizer:
            if self.settings.limit_grass_rando and self.options.local_fill < 95 and self.multiworld.players > 1:
                raise OptionError(f"TUNIC: Player {self.player_name} has their Local Fill option set too low. "
                                  f"They must either bring it above 95% or the host needs to disable limit_grass_rando "
                                  f"in their host.yaml settings")

            self.player_location_table.update(grass_location_name_to_id)

        if self.options.breakable_shuffle:
            if self.options.entrance_rando:
                self.player_location_table.update(breakable_location_name_to_id)
            else:
                self.player_location_table.update({name: num for name, num in breakable_location_name_to_id.items()
                                                   if not name.startswith("Purgatory")})

    @classmethod
    def stage_generate_early(cls, multiworld: MultiWorld) -> None:
        tunic_worlds: Tuple[TunicWorld] = multiworld.get_game_worlds("TUNIC")
        for tunic in tunic_worlds:
            # setting up state combat logic stuff, see has_combat_reqs for its use
            # and this is magic so pycharm doesn't like it, unfortunately
            if tunic.options.combat_logic:
                multiworld.state.tunic_need_to_reset_combat_from_collect[tunic.player] = False
                multiworld.state.tunic_need_to_reset_combat_from_remove[tunic.player] = False
                multiworld.state.tunic_area_combat_state[tunic.player] = {}
                for area_name in area_data.keys():
                    multiworld.state.tunic_area_combat_state[tunic.player][area_name] = CombatState.unchecked

            # if it's one of the options, then it isn't a custom seed group
            if tunic.options.entrance_rando.value in EntranceRando.options.values():
                continue
            group = tunic.options.entrance_rando.value
            # if this is the first world in the group, set the rules equal to its rules
            if group not in cls.seed_groups:
                cls.seed_groups[group] = \
                    SeedGroup(laurels_zips=bool(tunic.options.laurels_zips),
                              ice_grappling=tunic.options.ice_grappling.value,
                              ladder_storage=tunic.options.ladder_storage.value,
                              laurels_at_10_fairies=tunic.options.laurels_location == LaurelsLocation.option_10_fairies,
                              fixed_shop=bool(tunic.options.fixed_shop),
                              plando=tunic.options.plando_connections)
                continue

            # off is more restrictive
            if not tunic.options.laurels_zips:
                cls.seed_groups[group]["laurels_zips"] = False
            # lower value is more restrictive
            if tunic.options.ice_grappling < cls.seed_groups[group]["ice_grappling"]:
                cls.seed_groups[group]["ice_grappling"] = tunic.options.ice_grappling.value
            # lower value is more restrictive
            if tunic.options.ladder_storage.value < cls.seed_groups[group]["ladder_storage"]:
                cls.seed_groups[group]["ladder_storage"] = tunic.options.ladder_storage.value
            # laurels at 10 fairies changes logic for secret gathering place placement
            if tunic.options.laurels_location == 3:
                cls.seed_groups[group]["laurels_at_10_fairies"] = True
            # more restrictive, overrides the option for others in the same group, which is better than failing imo
            if tunic.options.fixed_shop:
                cls.seed_groups[group]["fixed_shop"] = True

            if tunic.options.plando_connections:
                # loop through the connections in the player's yaml
                for cxn in tunic.options.plando_connections:
                    new_cxn = True
                    for group_cxn in cls.seed_groups[group]["plando"]:
                        # if neither entrance nor exit match anything in the group, add to group
                        if ((cxn.entrance == group_cxn.entrance and cxn.exit == group_cxn.exit)
                                or (cxn.exit == group_cxn.entrance and cxn.entrance == group_cxn.exit)):
                            new_cxn = False
                            break
                                   
                        # check if this pair is the same as a pair in the group already
                        is_mismatched = (
                            cxn.entrance == group_cxn.entrance and cxn.exit != group_cxn.exit
                            or cxn.entrance == group_cxn.exit and cxn.exit != group_cxn.entrance
                            or cxn.exit == group_cxn.entrance and cxn.entrance != group_cxn.exit
                            or cxn.exit == group_cxn.exit and cxn.entrance != group_cxn.entrance
                        )
                        if is_mismatched:
                            raise Exception(f"TUNIC: Conflict between seed group {group}'s plando "
                                            f"connection {group_cxn.entrance} <-> {group_cxn.exit} and "
                                            f"{tunic.player_name}'s plando connection {cxn.entrance} <-> {cxn.exit}")
                    if new_cxn:
                        cls.seed_groups[group]["plando"].value.append(cxn)

    def create_item(self, name: str, classification: ItemClassification = None) -> TunicItem:
        item_data = item_table[name]
        # evaluate alternate classifications based on options
        # it'll choose whichever classification isn't None first in this if else tree
        itemclass: ItemClassification = (classification
                                         or (item_data.combat_ic if self.options.combat_logic else None)
                                         or (ItemClassification.progression | ItemClassification.useful
                                             if name == "Glass Cannon"
                                             and (self.options.grass_randomizer or self.options.breakable_shuffle)
                                             and not self.options.start_with_sword else None)
                                         or (ItemClassification.progression | ItemClassification.useful
                                             if name == "Shield" and self.options.ladder_storage
                                             and not self.options.ladder_storage_without_items else None)
                                         or item_data.classification)
        return TunicItem(name, itemclass, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        tunic_items: List[TunicItem] = []
        self.slot_data_items = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        # Calculate number of hexagons in item pool
        if self.options.hexagon_quest:
            items_to_create[gold_hexagon] = get_hexagons_in_pool(self)

        for money_fool in fool_tiers[self.options.fool_traps]:
            items_to_create["Fool Trap"] += items_to_create[money_fool]
            items_to_create[money_fool] = 0

        # creating these after the fool traps are made mostly so we don't have to mess with it
        if self.options.breakable_shuffle:
            for loc_data in breakable_location_table.values():
                if not self.options.entrance_rando and loc_data.er_region == "Purgatory":
                    continue
                items_to_create[f"Money x{self.random.randint(1, 5)}"] += 1

        if self.options.start_with_sword:
            self.multiworld.push_precollected(self.create_item("Sword"))

        if self.options.sword_progression:
            items_to_create["Stick"] = 0
            items_to_create["Sword"] = 0
        else:
            items_to_create["Sword Upgrade"] = 0

        if self.options.laurels_location:
            laurels = self.create_item("Hero's Laurels")
            if self.options.laurels_location == "6_coins":
                self.get_location("Coins in the Well - 6 Coins").place_locked_item(laurels)
            elif self.options.laurels_location == "10_coins":
                self.get_location("Coins in the Well - 10 Coins").place_locked_item(laurels)
            elif self.options.laurels_location == "10_fairies":
                self.get_location("Secret Gathering Place - 10 Fairy Reward").place_locked_item(laurels)
            items_to_create["Hero's Laurels"] = 0

        if self.options.grass_randomizer:
            items_to_create["Grass"] = len(grass_location_table)
            for grass_location in excluded_grass_locations:
                self.get_location(grass_location).place_locked_item(self.create_item("Grass"))
            items_to_create["Grass"] -= len(excluded_grass_locations)

        if self.options.keys_behind_bosses:
            rgb_hexagons = list(hexagon_locations.keys())
            # shuffle these in case not all are placed in hex quest
            self.random.shuffle(rgb_hexagons)
            for rgb_hexagon in rgb_hexagons:
                location = hexagon_locations[rgb_hexagon]
                if self.options.hexagon_quest:
                    if items_to_create[gold_hexagon] > 0:
                        hex_item = self.create_item(gold_hexagon)
                        items_to_create[gold_hexagon] -= 1
                        items_to_create[rgb_hexagon] = 0
                        self.get_location(location).place_locked_item(hex_item)
                else:
                    hex_item = self.create_item(rgb_hexagon)
                    self.get_location(location).place_locked_item(hex_item)
                    items_to_create[rgb_hexagon] = 0

        # Filler items in the item pool
        available_filler: List[str] = [filler for filler in items_to_create if items_to_create[filler] > 0 and
                                       item_table[filler].classification == ItemClassification.filler]

        # Remove filler to make room for other items
        def remove_filler(amount: int) -> None:
            for _ in range(amount):
                if not available_filler:
                    fill = "Fool Trap"
                else:
                    fill = self.random.choice(available_filler)
                if items_to_create[fill] == 0:
                    raise Exception("No filler items left to accommodate options selected. Turn down fool trap amount.")
                items_to_create[fill] -= 1
                if items_to_create[fill] == 0:
                    available_filler.remove(fill)

        if self.options.shuffle_ladders:
            ladder_count = 0
            for item_name, item_data in item_table.items():
                if item_data.item_group == "Ladders":
                    items_to_create[item_name] = 1
                    ladder_count += 1
            remove_filler(ladder_count)

        if self.options.hexagon_quest:
            # Replace pages and normal hexagons with filler
            for replaced_item in list(filter(lambda item: "Pages" in item or item in hexagon_locations, items_to_create)):
                if replaced_item in item_name_groups["Abilities"] and self.options.ability_shuffling \
                        and self.options.hexagon_quest_ability_type == "pages":
                    continue
                filler_name = self.get_filler_item_name()
                items_to_create[filler_name] += items_to_create[replaced_item]
                if items_to_create[filler_name] >= 1 and filler_name not in available_filler:
                    available_filler.append(filler_name)
                items_to_create[replaced_item] = 0

            remove_filler(items_to_create[gold_hexagon])

            if not self.options.combat_logic:
                # Sort for deterministic order
                for hero_relic in sorted(item_name_groups["Hero Relics"]):
                    tunic_items.append(self.create_item(hero_relic, ItemClassification.useful))
                    items_to_create[hero_relic] = 0

        if not self.options.ability_shuffling:
            # Sort for deterministic order
            for page in sorted(item_name_groups["Abilities"]):
                if items_to_create[page] > 0:
                    tunic_items.append(self.create_item(page, ItemClassification.useful))
                    items_to_create[page] = 0
        # if ice grapple logic is on, probably really want icebolt
        elif self.options.ice_grappling:
            page = "Pages 52-53 (Icebolt)"
            if items_to_create[page] > 0:
                tunic_items.append(self.create_item(page, ItemClassification.progression | ItemClassification.useful))
                items_to_create[page] = 0

        if self.options.maskless:
            tunic_items.append(self.create_item("Scavenger Mask", ItemClassification.useful))
            items_to_create["Scavenger Mask"] = 0

        if self.options.lanternless:
            tunic_items.append(self.create_item("Lantern", ItemClassification.useful))
            items_to_create["Lantern"] = 0

        for item, quantity in items_to_create.items():
            for _ in range(quantity):
                tunic_items.append(self.create_item(item))

        for tunic_item in tunic_items:
            if tunic_item.name in slot_data_item_names:
                self.slot_data_items.append(tunic_item)

        # pull out the filler so that we can place it manually during pre_fill
        self.fill_items = []
        if self.options.local_fill > 0 and self.multiworld.players > 1:
            # skip items marked local or non-local, let fill deal with them in its own way
            # discard grass from non_local if it's meant to be limited
            if self.settings.limit_grass_rando:
                self.options.non_local_items.value.discard("Grass")
            all_filler: List[TunicItem] = []
            non_filler: List[TunicItem] = []
            for tunic_item in tunic_items:
                if (tunic_item.excludable
                        and tunic_item.name not in self.options.local_items
                        and tunic_item.name not in self.options.non_local_items):
                    all_filler.append(tunic_item)
                else:
                    non_filler.append(tunic_item)
            self.amount_to_local_fill = int(self.options.local_fill.value * len(all_filler) / 100)
            self.fill_items += all_filler[:self.amount_to_local_fill]
            del all_filler[:self.amount_to_local_fill]
            tunic_items = all_filler + non_filler

        self.multiworld.itempool += tunic_items

    def pre_fill(self) -> None:
        if self.options.local_fill > 0 and self.multiworld.players > 1:
            # we need to reserve a couple locations so that we don't fill up every sphere 1 location
            sphere_one_locs = self.multiworld.get_reachable_locations(CollectionState(self.multiworld), self.player)
            reserved_locations: Set[Location] = set(self.random.sample(sphere_one_locs, 2))
            viable_locations = [loc for loc in self.multiworld.get_unfilled_locations(self.player)
                                if loc not in reserved_locations
                                and loc.name not in self.options.priority_locations.value]

            if len(viable_locations) < self.amount_to_local_fill:
                raise OptionError(f"TUNIC: Not enough locations for local_fill option for {self.player_name}. "
                                  f"This is likely due to excess plando or priority locations.")
            self.random.shuffle(viable_locations)
            self.fill_locations = viable_locations[:self.amount_to_local_fill]

    @classmethod
    def stage_pre_fill(cls, multiworld: MultiWorld) -> None:
        tunic_fill_worlds: List[TunicWorld] = [world for world in multiworld.get_game_worlds("TUNIC")
                                               if world.options.local_fill.value > 0]
        if tunic_fill_worlds and multiworld.players > 1:
            grass_fill: List[TunicItem] = []
            non_grass_fill: List[TunicItem] = []
            grass_fill_locations: List[Location] = []
            non_grass_fill_locations: List[Location] = []
            for world in tunic_fill_worlds:
                if world.options.grass_randomizer:
                    grass_fill.extend(world.fill_items)
                    grass_fill_locations.extend(world.fill_locations)
                else:
                    non_grass_fill.extend(world.fill_items)
                    non_grass_fill_locations.extend(world.fill_locations)

            multiworld.random.shuffle(grass_fill)
            multiworld.random.shuffle(non_grass_fill)
            multiworld.random.shuffle(grass_fill_locations)
            multiworld.random.shuffle(non_grass_fill_locations)

            for filler_item in grass_fill:
                grass_fill_locations.pop().place_locked_item(filler_item)

            for filler_item in non_grass_fill:
                non_grass_fill_locations.pop().place_locked_item(filler_item)

    def create_regions(self) -> None:
        self.tunic_portal_pairs = {}
        self.er_portal_hints = {}
        self.ability_unlocks = randomize_ability_unlocks(self)

        # stuff for universal tracker support, can be ignored for standard gen
        if self.using_ut:
            self.ability_unlocks["Pages 24-25 (Prayer)"] = self.passthrough["Hexagon Quest Prayer"]
            self.ability_unlocks["Pages 42-43 (Holy Cross)"] = self.passthrough["Hexagon Quest Holy Cross"]
            self.ability_unlocks["Pages 52-53 (Icebolt)"] = self.passthrough["Hexagon Quest Icebolt"]

        # Most non-standard options use ER regions
        if (self.options.entrance_rando or self.options.shuffle_ladders or self.options.combat_logic
                or self.options.grass_randomizer or self.options.breakable_shuffle):
            portal_pairs = create_er_regions(self)
            if self.options.entrance_rando:
                # these get interpreted by the game to tell it which entrances to connect
                for portal1, portal2 in portal_pairs.items():
                    self.tunic_portal_pairs[portal1.scene_destination()] = portal2.scene_destination()
        else:
            # uses the original rules, easier to navigate and reference
            for region_name in tunic_regions:
                region = Region(region_name, self.player, self.multiworld)
                self.multiworld.regions.append(region)

            for region_name, exits in tunic_regions.items():
                region = self.get_region(region_name)
                region.add_exits(exits)

            for location_name, location_id in self.player_location_table.items():
                region = self.get_region(location_table[location_name].region)
                location = TunicLocation(self.player, location_name, location_id, region)
                region.locations.append(location)

            victory_region = self.get_region("Spirit Arena")
            victory_location = TunicLocation(self.player, "The Heir", None, victory_region)
            victory_location.place_locked_item(TunicItem("Victory", ItemClassification.progression, None, self.player))
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
            victory_region.locations.append(victory_location)

    def set_rules(self) -> None:
        # same reason as in create_regions
        if (self.options.entrance_rando or self.options.shuffle_ladders or self.options.combat_logic
                or self.options.grass_randomizer or self.options.breakable_shuffle):
            set_er_location_rules(self)
        else:
            set_region_rules(self)
            set_location_rules(self)

    def get_filler_item_name(self) -> str:
        return self.random.choice(filler_items)

    # cache whether you can get through combat logic areas
    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and self.options.combat_logic and item.name in combat_items:
            state.tunic_need_to_reset_combat_from_collect[self.player] = True
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and self.options.combat_logic and item.name in combat_items:
            state.tunic_need_to_reset_combat_from_remove[self.player] = True
        return change

    def write_spoiler_header(self, spoiler_handle: TextIO):
        if self.options.hexagon_quest and self.options.ability_shuffling\
                and self.options.hexagon_quest_ability_type == HexagonQuestAbilityUnlockType.option_hexagons:
            spoiler_handle.write("\nAbility Unlocks (Hexagon Quest):\n")
            for ability in self.ability_unlocks:
                # Remove parentheses for better readability
                spoiler_handle.write(f'{ability[ability.find("(")+1:ability.find(")")]}: {self.ability_unlocks[ability]} Gold Questagons\n')

    def extend_hint_information(self, hint_data: Dict[int, Dict[int, str]]) -> None:
        if self.options.entrance_rando:
            hint_data.update({self.player: {}})
            # all state seems to have efficient paths
            all_state = self.multiworld.get_all_state(True)
            all_state.update_reachable_regions(self.player)
            paths = all_state.path
            portal_names = [portal.name for portal in portal_mapping]
            for location in self.multiworld.get_locations(self.player):
                # skipping event locations
                if not location.address:
                    continue
                path_to_loc = []
                previous_name = "placeholder"
                try:
                    name, connection = paths[location.parent_region]
                except KeyError:
                    # logic bug, proceed with warning since it takes a long time to update AP
                    warning(f"{location.name} is not logically accessible for {self.player_name}. "
                            "Creating entrance hint Inaccessible. Please report this to the TUNIC rando devs. "
                            "If you are using Plando Items (excluding early locations), then this is likely the cause.")
                    hint_text = "Inaccessible"
                else:
                    while connection != ("Menu", None):
                        name, connection = connection
                        # for LS entrances, we just want to give the portal name
                        if "(LS)" in name:
                            name = name.split(" (LS) ", 1)[0]
                        # was getting some cases like Library Grave -> Library Grave -> other place
                        if name in portal_names and name != previous_name:
                            previous_name = name
                            path_to_loc.append(name)
                    hint_text = " -> ".join(reversed(path_to_loc))

                if hint_text:
                    hint_data[self.player][location.address] = hint_text

    def get_real_location(self, location: Location) -> Tuple[str, int]:
        # if it's not in a group, it's not in an item link
        if location.player not in self.multiworld.groups or not location.item:
            return location.name, location.player
        try:
            loc = self.player_item_link_locations[location.item.name].pop()
            return loc.name, loc.player
        except IndexError:
            warning(f"TUNIC: Failed to parse item location for in-game hints for {self.player_name}. "
                    f"Using a potentially incorrect location name instead.")
            return location.name, location.player

    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data: Dict[str, Any] = {
            "seed": self.random.randint(0, 2147483647),
            "start_with_sword": self.options.start_with_sword.value,
            "keys_behind_bosses": self.options.keys_behind_bosses.value,
            "sword_progression": self.options.sword_progression.value,
            "ability_shuffling": self.options.ability_shuffling.value,
            "hexagon_quest": self.options.hexagon_quest.value,
            "hexagon_quest_ability_type": self.options.hexagon_quest_ability_type.value,
            "fool_traps": self.options.fool_traps.value,
            "laurels_zips": self.options.laurels_zips.value,
            "ice_grappling": self.options.ice_grappling.value,
            "ladder_storage": self.options.ladder_storage.value,
            "ladder_storage_without_items": self.options.ladder_storage_without_items.value,
            "lanternless": self.options.lanternless.value,
            "maskless": self.options.maskless.value,
            "entrance_rando": int(bool(self.options.entrance_rando.value)),
            "shuffle_ladders": self.options.shuffle_ladders.value,
            "grass_randomizer": self.options.grass_randomizer.value,
            "combat_logic": self.options.combat_logic.value,
            "Hexagon Quest Prayer": self.ability_unlocks["Pages 24-25 (Prayer)"],
            "Hexagon Quest Holy Cross": self.ability_unlocks["Pages 42-43 (Holy Cross)"],
            "Hexagon Quest Icebolt": self.ability_unlocks["Pages 52-53 (Icebolt)"],
            "Hexagon Quest Goal": self.options.hexagon_goal.value,
            "Entrance Rando": self.tunic_portal_pairs,
            "disable_local_spoiler": int(self.settings.disable_local_spoiler or self.multiworld.is_race),
            "breakable_shuffle": self.options.breakable_shuffle.value,
        }

        # this would be in a stage if there was an appropriate stage for it
        self.player_item_link_locations = {}
        groups = self.multiworld.get_player_groups(self.player)
        # checking if groups so that this doesn't run if the player isn't in a group
        if groups:
            if not self.item_link_locations:
                tunic_worlds: Tuple[TunicWorld] = self.multiworld.get_game_worlds("TUNIC")
                # figure out our groups and the items in them
                for tunic in tunic_worlds:
                    for group in self.multiworld.get_player_groups(tunic.player):
                        self.item_link_locations.setdefault(group, {})
                for location in self.multiworld.get_locations():
                    if location.item and location.item.player in self.item_link_locations.keys():
                        (self.item_link_locations[location.item.player].setdefault(location.item.name, [])
                         .append((location.player, location.name)))

            # if item links are on, set up the player's personal item link locations, so we can pop them as needed
            for group, item_links in self.item_link_locations.items():
                if group in groups:
                    for item_name, locs in item_links.items():
                        self.player_item_link_locations[item_name] = \
                            [self.multiworld.get_location(location_name, player) for player, location_name in locs]

        for tunic_item in filter(lambda item: item.location is not None and item.code is not None, self.slot_data_items):
            if tunic_item.name not in slot_data:
                slot_data[tunic_item.name] = []
            if tunic_item.name == gold_hexagon and len(slot_data[gold_hexagon]) >= 6:
                continue
            slot_data[tunic_item.name].extend(self.get_real_location(tunic_item.location))

        for start_item in self.options.start_inventory_from_pool:
            if start_item in slot_data_item_names:
                if start_item not in slot_data:
                    slot_data[start_item] = []
                for _ in range(self.options.start_inventory_from_pool[start_item]):
                    slot_data[start_item].extend(["Your Pocket", self.player])

        return slot_data

    # for the universal tracker, doesn't get called in standard gen
    # docs: https://github.com/FarisTheAncient/Archipelago/blob/tracker/worlds/tracker/docs/re-gen-passthrough.md
    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:
        # returning slot_data so it regens, giving it back in multiworld.re_gen_passthrough
        # we are using re_gen_passthrough over modifying the world here due to complexities with ER
        return slot_data
