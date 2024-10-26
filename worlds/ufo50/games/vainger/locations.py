from typing import TYPE_CHECKING, Dict, NamedTuple, Set, Optional
from BaseClasses import Region, ItemClassification, Item, Location
from ...constants import get_game_base_id

if TYPE_CHECKING:
    from ... import UFO50World

# adapted from Barbuta, thanks Scipio! <3


class LocationInfo(NamedTuple):
    id_offset: Optional[int]
    region_name: str


# the letter is the column (left to right), the number is the row (top to bottom)
# based on a map at https://steamcommunity.com/sharedfiles/filedetails/?id=3341323146
# except numbering each sector from 1 to 10.
location_table: Dict[str, LocationInfo] = {
    "LatomA4 - Shield Upgrade": LocationInfo(0, "LatomD3 Genepod"), 
    "LatomA7 - Shield Upgrade": LocationInfo(1, "LatomD3 Genepod"), 
    "LatomA9 - Shield Upgrade": LocationInfo(2, "LatomC9 Genepod"), 
    "LatomB9 - Shield Upgrade": LocationInfo(3, "LatomC9 Genepod"), 
    "LatomC4 - Shield Upgrade": LocationInfo(4, "LatomC6 Genepod"), 
    "LatomC6 - Clone Material": LocationInfo(5, "LatomC6 Genepod"), 
    "LatomD5 - Key Code": LocationInfo(6, "LatomD5 Genepod"),
    "LatomD6 - Security Clearance": LocationInfo(7, "LatomD6 Area"), 
    "LatomE4 - Shield Upgrade": LocationInfo(8, "LatomF5 Genepod"),
    "LatomG8 - Multi Mod": LocationInfo(9, "LatomF7 Genepod"), 
    "LatomI4 - Pulse Mod": LocationInfo(10, "LatomI4 Genepod"), 
    "LatomJ1 - Stabilizer": LocationInfo(11, "LatomF5 Genepod"),  # TODO: does this need to be I4 instead due to the miniboss?
    "LatomJ3 - Shield Upgrade": LocationInfo(12, "LatomF5 Genepod"),  # do it from F5 to avoid the issues with I4
    "LatomJ10 - Shield Upgrade": LocationInfo(13, "LatomC9 Genepod"), 

    "LatomD5 - Boss Defeated": LocationInfo(None, "LatomC6 Genepod"),  # alien?

    "ThetaA2 - Clone Material": LocationInfo(100, "ThetaA4 Genepod"), 
    "ThetaA3 - Shield Upgrade": LocationInfo(101, "ThetaA4 Genepod"), 
    "ThetaA9 - Shield Upgrade": LocationInfo(102, "VerdeA1 Genepod"), 
    "ThetaC5 - Clone Material": LocationInfo(103, "ThetaA4 Genepod"), 
    # the logic is different approaching these two from the left or the right.
    # I don't think it matters because both sides require hot-shot and heat mod is the only barrier to circling around?
    # but I'm going to express the difference anyway.
    "ThetaC8 - Shield Upgrade": LocationInfo(104, "ThetaC8 Location"), 
    "ThetaC10 - Shield Upgrade": LocationInfo(105, "ThetaC10 Location"), 
    "ThetaD7 - Shield Upgrade": LocationInfo(106, "ThetaA4 Genepod"), 
    "ThetaE9 - Key Code": LocationInfo(107, "ThetaE9 Genepod"),
    "ThetaH1 - Shield Upgrade": LocationInfo(108, "ThetaI7 Genepod"), 
    "ThetaH4 - Heat Mod": LocationInfo(109, "ThetaI7 Genepod"), 
    "ThetaI4 - Shield Upgrade": LocationInfo(110, "ThetaI7 Genepod"), 
    "ThetaJ7 - Shield Upgrade": LocationInfo(111, "ThetaI7 Genepod"), 

    "ThetaE9 - Boss Defeated": LocationInfo(None, "ThetaF6 Genepod"),  # I have no memory of this one lol

    "VerdeA1 - Shield Upgrade": LocationInfo(200, "VerdeA1 Genepod"), 
    "VerdeB5 - Force Mod": LocationInfo(201, "VerdeSW Area"), 
    "VerdeC4 - Shield Upgrade": LocationInfo(202, "VerdeA1 Genepod"), 
    "VerdeC5 - Shield Upgrade": LocationInfo(203, "VerdeSW Area"), 
    "VerdeE1 - Key Code": LocationInfo(204, "VerdeE1 Genepod"),
    "VerdeE5 - Security Clearance": LocationInfo(205, "VerdeSW Area"),
    "VerdeF8 - Shield Upgrade": LocationInfo(206, "VerdeSW Area"),
    "VerdeG5 - Shield Upgrade": LocationInfo(207, "VerdeI7 Genepod"),
    "VerdeG10 - Security Clearance": LocationInfo(208, "VerdeI7 Genepod"),
    # need a separate region to account for the fact that the heat armor damage boost is only possible from the right
    "VerdeH7 - Shield Upgrade": LocationInfo(209, "VerdeH7 Location"),
    "VerdeI4 - Shield Upgrade": LocationInfo(210, "VerdeI7 Genepod"),
    "VerdeI9 - Key Code": LocationInfo(211, "VerdeI9 Genepod"),
    "VerdeJ2 - Stabilizer": LocationInfo(212, "VerdeI7 Genepod"),
    "VerdeJ9 - Shield Upgrade": LocationInfo(213, "VerdeI7 Genepod"),

    "VerdeE1 - Ramses Defeated": LocationInfo(None, "VerdeA1 Genepod"), 
    "VerdeI9 - Sura Defeated": LocationInfo(None, "VerdeSW Area"),  # This might be Jorgensen, not Sura
    
    "Control - Shield Upgrade": LocationInfo(300, "Control Genepod"),

    "Control - Hooper Defeated": LocationInfo(None, "Control Genepod"),

    "Garden": LocationInfo(400, "ThetaI7 Genepod"),  # for now it's a clone of the heat mod location.
    "Gold": LocationInfo(401, "Control Genepod"), 
    "Cherry": LocationInfo(402, "Control Genepod")
}


def get_locations() -> Dict[str, int]:
    return {f"Vainger - {name}": data.id_offset + get_game_base_id("Vainger") for name, data in location_table.items()
            if data.id_offset}


def get_location_groups() -> Dict[str, Set[str]]:
    location_groups: Dict[str, Set[str]] = {"Vainger": {f"Vainger - {loc_name}" for loc_name in location_table.keys()}}
    return location_groups


def create_locations(world: "UFO50World", regions: Dict[str, Region]) -> None:
    for loc_name, loc_data in location_table.items():
        loc = Location(world.player, f"Vainger - {loc_name}", 
                       loc_data.id_offset + get_game_base_id("Vainger") if loc_data.id_offset else None,
                       regions[f"Vainger - {loc_data.region_name}"])
        if not loc_data.id_offset:      # this is an event location
            loc.place_locked_item(Item(f"Vainger - {loc_name}", ItemClassification.progression, None,
                                       world.player))
        regions[f"Vainger - {loc_data.region_name}"].locations.append(loc)
