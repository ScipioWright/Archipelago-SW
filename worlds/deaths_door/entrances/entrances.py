from .entrance_class import DeathsDoorEntrance
from .bettys_lair_entrances import bettys_lair_entrances
from .camp_entrances import camp_entrances
from .ceramic_manor_entrances import ceramic_manor_entrances
from .crypt_entrances import crypt_entrances
from .door_location_entrances import door_location_entrances
from .estate_entrances import estate_entrances
from .flooded_fortress_entrances import flooded_fortress_entrances
from .furnace_observation_entrances import furnace_observation_entrances
from .grove_entrances import grove_entrances
from .hall_of_doors_entrances import hall_of_doors_entrances
from .inner_furnace_entrances import inner_furnace_entrances
from .lockstone_entrances import lockstone_entrances
from .lost_cemetery_entrances import lost_cemetery_entrances
from .mushroom_dungeon_entrances import mushroom_dungeon_entrances
from .overgrown_ruins_entrances import overgrown_ruins_entrances
from .stranded_sailor_caves_entrances import stranded_sailor_caves_entrances
from .stranded_sailor_entrances import stranded_sailor_entrances
from .throne_entrances import throne_entrances
from .urn_witchs_laboratory_entrances import laboratory_entrances
from .watchtowers_entrances import watchtower_entrances

deathsdoor_internal_entrances: list[DeathsDoorEntrance] = (
    bettys_lair_entrances
    + camp_entrances
    + ceramic_manor_entrances
    + crypt_entrances
    + door_location_entrances
    + estate_entrances
    + flooded_fortress_entrances
    + furnace_observation_entrances
    + grove_entrances
    + hall_of_doors_entrances
    + inner_furnace_entrances
    + lockstone_entrances
    + lost_cemetery_entrances
    + mushroom_dungeon_entrances
    + overgrown_ruins_entrances
    + stranded_sailor_caves_entrances
    + stranded_sailor_entrances
    + throne_entrances
    + laboratory_entrances
    + watchtower_entrances
)
