from typing import TYPE_CHECKING, Dict, NamedTuple
from BaseClasses import Location, Region, ItemClassification
from .items import NightManorItem

if TYPE_CHECKING:
    from .. import UFO50World


class NightManorLocation(Location):
    game: str = "UFO 50"


class LocationInfo(NamedTuple):
    id_offset: int
    region_name: str


ufo_50_base_id = 21061550_00_000  # reference it from wherever it is when there's an actual world class
night_manor_base_id = 42_000 + ufo_50_base_id


night_manor_location_table: Dict[str, LocationInfo] = {
    "Starting Room - Spoon": LocationInfo(0, "Starting Room"),
    "Starting Room - Bowl": LocationInfo(1, "Starting Room"),
    "Starting Room - Yellow Note": LocationInfo(2, "Starting Room"), # in vent after you open with spoon
    "Starting Room - Hairpin": LocationInfo(3, "Starting Room") # in vent after you open with spoon
    "First Floor Bathroom - Tweezers": LocationInfo(4, "First Floor & Exterior"), #in medicine cabinet
    "Guest Bedroom - Journal Entry 2": LocationInfo(5, "First Floor & Exterior"),
    "Guest Bedroom - Journal Entry 5": LocationInfo(6, "First Floor & Exterior"),
    "Guest Bedroom - Hook": LocationInfo(7, "First Floor & Exterior"), #in closet
    "Guest Bedroom - Batteries": LocationInfo(8, "First Floor & Exterior"), #in drawer
    "Living Room - Journal Entry 1": LocationInfo(9, "First Floor & Exterior"),
    "Living Room - Coins": LocationInfo(10, "First Floor & Exterior"), #in couch
    "Living Room - Matches": LocationInfo(11, "First Floor & Exterior"), #above fireplace
    "Dining Room - Journal Entry 4": LocationInfo(12, "First Floor & Exterior"),
    "Kitchen - Journal Entry 7": LocationInfo(13, "First Floor & Exterior"), #on the fridge
    "Kitchen - Kitchen Knife": LocationInfo(14, "First Floor & Exterior"), # on counter, accessible after running from killer
    "Kitchen - Drain Cleaner": LocationInfo(15, "First Floor & Exterior"), # under sink
    "Garage - Oil Can": LocationInfo(16, "First Floor & Exterior"), # on side shelf
    "Garage - Flashlight": LocationInfo(17, "First Floor & Exterior"), # on side shelf
    "Garage - Duct Tape": LocationInfo(18, "First Floor & Exterior"), # on back shelf
    "Garage - Journal Entry 8": LocationInfo(19, "First Floor & Exterior"), # on back wall
    "Garage - Gas Can": LocationInfo(20, "First Floor & Exterior"), # In metal box after you spray with oil can
    "Garage - Crowbar": LocationInfo(21, "First Floor & Exterior"), # In metal box after you spray with oil can,
    "Dining Room - Ornamental Egg": LocationInfo(22, "First Floor & Exterior"), # In cabinet after you smash it,
    "Living Room - Red Gemstone": LocationInfo(23, "First Floor & Exterior"), # In fireplace after you burn,
    "Sunroom - Journal Entry 9": LocationInfo(24, "First Floor & Exterior"), # On table
    "Lounge - Pool Cue": LocationInfo(25, "Second Floor"), # In corner
    "Lounge - Journal Entry 10": LocationInfo(26, "Second Floor"), # On side table
    "Lounge - Sheet Music": LocationInfo(27, "Second Floor"), # Falls from jukebox after using coins
    "Pool - Copper Key": LocationInfo(28, "First Floor & Exterior"), #accessible from floating corpse after you tape hook to pool cue
    "Shed - Screwdriver": LocationInfo(29, "Shed"), #on toolbench
    "Shed - Journal Entry 11": LocationInfo(30, "Shed"), #on toolbench
    "Shed - Wrench": LocationInfo(31, "Shed"), #hanging on side wall
    "Shed - Hedge Shears": LocationInfo(32, "Shed"), #hanging on back wall
    "Shed - Shovel": LocationInfo(33, "Shed"), #in back corner
    "Shed - Bronze Key": LocationInfo(34, "Shed"), #in sack if you cut with knife
    "Shed - Gold Key": LocationInfo(35, "Shed"), #in ornamental egg if you crush with vice
    "Backyard - Motor": LocationInfo(36, "First Floor & Exterior"), #in lawnmower after you use wrench
    "Garden - Steel Key": LocationInfo(37, "First Floor & Exterior"), #in hole after you dig with shovel
    "Sunroom - Hacksaw": LocationInfo(38, "First Floor & Exterior"), #in container after you cut vines with hedge shears,
    "First Floor Bathroom - Silver Key": LocationInfo(39, "First Floor & Exterior"), #in sink after you use drain cleaner and tweezers
    "First Floor Bathroom - Ring": LocationInfo(40, "First Floor & Exterior"), #on corpse if you use hacksaw
    "Guest Bedroom - Brass Key": LocationInfo(41, "First Floor & Exterior"), #in jewelery box when opened with silver key
    "Foyer - Gear": LocationInfo(42, "First Floor & Exterior"), #in clock after used with brass key
    "Exterior Front - Green Gemstone": LocationInfo(43, "First Floor & Exterior"), #in statue if you use ring on insignia
    "Master Bedroom - Journal Entry 12": LocationInfo(44, "Master Bedroom"), #on dresser
    "Master Bedroom - Journal Entry 15": LocationInfo(45, "Master Bedroom"), #in bedside table
    "Office - Journal Entry 6": LocationInfo(46, "Master Bedroom"), #on floor near desk
    "Office - Magnifying Glass": LocationInfo(47, "Master Bedroom"), #on bottom of back shelf
    "Office - Tea Tree Oil": LocationInfo(48, "Master Bedroom"), #on back shelf
    "Master Bathroom - Hydrogen Peroxide": LocationInfo(49, "Master Bedroom"), #cabinet under sink,
    "Master Bathroom - Safe Combination": LocationInfo(50, "Master Bedroom"), #behind mirror if you smash it
    "Balcony - Journal Entry 16": LocationInfo(51, "Master Bedroom"), #on table
    "Balcony - Cigar Butt": LocationInfo(52, "Master Bedroom"), #in ashtray
    "Garden - Yellow Gemstone": LocationInfo(53, "Master Bedroom"), #after you cut the corpse down from the balcony, cut with knife
    "Kids Bedroom - Journal Entry 13": LocationInfo(54, "Second Floor"), #on side desk
    "Kids Bedroom - Computer Password": LocationInfo(55, "Second Floor"), #use magnifying glass on dollhouse
    "Attic - Journal Entry 3": LocationInfo(56, "Second Floor"),  #on floor near mannequins
    "Attic - Piano Wire": LocationInfo(57, "Second Floor"), #use sheet music on piano and play
    "Attic - Crossbow": LocationInfo(58, "Second Floor"), #in chest to the right after unlocking with bronze key
    "Play Room - Doll": LocationInfo(59, "Second Floor"), #in bottom right corner of room
    "Play Room - Aluminum Key": LocationInfo(60, "Second Floor"), #get by cutting doll with knife
    "Play Room - Journal Entry 14": LocationInfo(61, "Second Floor"), #in bottom left corner
    "Office - Fungicide Recipe": LocationInfo(62, "Master Bedroom"), #in trash on computer after using password on it
    "Crafting - Fungicide": LocationInfo(63, "Master Bedroom"), #craft in inventory after getting recipe
    "Master Bedroom - White Gemstone": LocationInfo(64, "Master Bedroom"),#get from safe behind painting above bed, use combination
    "Kids Bedroom - Glasses": LocationInfo(65, "Second Floor"), #get by using aluminum key on music box
    "Play Room - Maze Directions": LocationInfo(66, "Second Floor"), #use red glasses on scribbles on wall
    "Maze - Crossbow Bolt": LocationInfo(67, "Maze"), #open gate with gems, use directions on maze, get bolt from statue
    "Manor - Iron Key": LocationInfo(68, "Maze"), #combine crossbow and bolt, lure killer or wait, shoot him and get the key
    "Basement - Journal Entry 17": LocationInfo(69, "Maze") #on floor
 
}


def create_night_manor_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in night_manor_location_table.items():
        loc = NightManorLocation(world.player, f"Night Manor - {loc_name}", night_manor_base_id + loc_data.id_offset,
                              regions[loc_data.region_name])
        regions[loc_data.region_name].locations.add(loc)
    gold_victory_location = NightManorLocation(world.player, "Escape by Car", None, regions["First Floor & Exterior"])
    cherry_victory_location = NightManorLocation(world.player, "End the Nightmare", None, regions["Basement"])
    gold_victory_location.place_locked_item(NightManorItem("Night Manor - Gold Victory", ItemClassification.progression, None,
                                                   world.player))
    cherry_victory_location.place_locked_item(NightManorItem("Night Manor - Cherry Victory", ItemClassification.progression, None,
                                                   world.player))
    regions["First Floor & Exterior"].locations.append(gold_victory_location)
    regions["Basement"].locations.append(cherry_victory_location)
