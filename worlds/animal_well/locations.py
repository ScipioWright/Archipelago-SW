from enum import IntEnum
from typing import Dict, NamedTuple, Set, List, Optional
from .names import LocationNames as lname


class ByteSect(IntEnum):
    items = 1
    flames = 2
    bunnies = 3
    candles = 4
    house_key = 5

class AWTracker(NamedTuple):
    tile: int
    stamp: int = 0
    stamp_x: int = 0
    stamp_y: int = 0
    index: int = 0

class AWLocationData(NamedTuple):
    offset: Optional[int]  # location ID offset
    byte_section: int  # since where it is and what the length is varies
    byte_offset: int
    location_groups: List[str] = []
    tracker: AWTracker = None


location_base_id = 11553377
# todo: add location groups for general regions
location_table: Dict[str, AWLocationData] = {
    # major items
    lname.b_wand_chest.value: AWLocationData(0, ByteSect.items, 68, ["Toys"], AWTracker(162)),
    lname.bb_wand_chest.value: AWLocationData(1, ByteSect.items, 95, ["Toys"], AWTracker(708)),
    lname.disc_spot.value: AWLocationData(2, ByteSect.items, 37, ["Toys"], AWTracker(381, 2, 2, 4)),
    lname.yoyo_chest.value: AWLocationData(3, ByteSect.items, 97, ["Toys"], AWTracker(334)),
    lname.slink_chest.value: AWLocationData(4, ByteSect.items, 30, ["Toys"], AWTracker(417)),
    lname.flute_chest.value: AWLocationData(5, ByteSect.items, 46, ["Toys", "Egg Rewards"], AWTracker(169)),
    lname.top_chest.value: AWLocationData(6, ByteSect.items, 48, ["Toys", "Egg Rewards"], AWTracker(634)),
    lname.lantern_chest.value: AWLocationData(7, ByteSect.items, 75, ["Toys"], AWTracker(109)),
    lname.uv_lantern_chest.value: AWLocationData(8, ByteSect.items, 98, ["Toys"], AWTracker(323)),
    lname.b_ball_chest.value: AWLocationData(9, ByteSect.items, 15, ["Toys"], AWTracker(637)),
    lname.remote_chest.value: AWLocationData(10, ByteSect.items, 86, ["Toys"], AWTracker(466)),
    lname.wheel_chest.value: AWLocationData(11, ByteSect.items, 79, ["Toys"], AWTracker(643)),

    lname.mock_disc_chest.value: AWLocationData(12, ByteSect.items, 27, ["Toys"], AWTracker(382)),
    lname.fanny_pack_chest.value: AWLocationData(13, ByteSect.items, 100, ["Toys"], AWTracker(780)),

    lname.match_start_ceiling.value: AWLocationData(14, ByteSect.items, 70, ["Matches"], AWTracker(41, 0, 0, 0, 7)),
    lname.match_fish_mural.value: AWLocationData(15, ByteSect.items, 56, ["Matches"], AWTracker(41, 0, 0, 0, 5)),
    lname.match_dog_switch_bounce.value: AWLocationData(16, ByteSect.items, 11, ["Matches"], AWTracker(41, 0, 0, 0, 0)),
    lname.match_dog_upper_east.value: AWLocationData(17, ByteSect.items, 19, ["Matches"], AWTracker(41, 0, 0, 0, 2)),
    lname.match_bear.value: AWLocationData(18, ByteSect.items, 13, ["Matches"], AWTracker(41, 0, 0, 0, 1)),
    lname.match_above_egg_room.value: AWLocationData(19, ByteSect.items, 38, ["Matches"], AWTracker(41, 0, 0, 0, 4)),
    lname.match_center_well.value: AWLocationData(20, ByteSect.items, 21, ["Matches"], AWTracker(41, 0, 0, 0, 3)),
    lname.match_guard_room.value: AWLocationData(21, ByteSect.items, 81, ["Matches"], AWTracker(41, 0, 0, 0, 8)),
    lname.match_under_mouse_statue.value: AWLocationData(22, ByteSect.items, 63, ["Matches"], AWTracker(41, 0, 0, 0, 6)),

    lname.key_bear_lower.value: AWLocationData(23, ByteSect.items, 54, ["Keys"], AWTracker(40, 0, 0, 0, 2)),
    lname.key_bear_upper.value: AWLocationData(24, ByteSect.items, 34, ["Keys"], AWTracker(40, 0, 0, 0, 1)),
    lname.key_chest_mouse_head_lever.value: AWLocationData(25, ByteSect.items, 62, ["Keys"], AWTracker(40, 0, 0, 0, 3)),
    lname.key_frog_guard_room_west.value: AWLocationData(26, ByteSect.items, 82, ["Keys"], AWTracker(40, 0, 0, 0, 4)),
    lname.key_frog_guard_room_east.value: AWLocationData(27, ByteSect.items, 83, ["Keys"], AWTracker(40, 0, 0, 0, 5)),
    lname.key_dog.value: AWLocationData(28, ByteSect.items, 16, ["Keys"], AWTracker(40, 0, 0, 0, 0)),

    lname.key_house.value: AWLocationData(29, ByteSect.house_key, 4, ["Keys"], AWTracker(257, 6)),
    lname.key_office.value: AWLocationData(30, ByteSect.items, 39, ["Keys"], AWTracker(617)),

    lname.medal_e.value: AWLocationData(31, ByteSect.items, 90, ["Keys", "Medals"], AWTracker(679)),
    lname.medal_s.value: AWLocationData(32, ByteSect.items, 41, ["Keys", "Medals"], AWTracker(469)),
    # lname.medal_k.value: AWLocationData(33, ["Keys", "Medals"]),

    # event only for now until modding tools maybe
    lname.flame_blue.value: AWLocationData(34, ByteSect.flames, 0x21E, ["Flames"], AWTracker(627, 5, 1, -2, 2)),
    lname.flame_pink.value: AWLocationData(37, ByteSect.flames, 0x21F, ["Flames"], AWTracker(627, 5, 1, -2, 0)),
    lname.flame_violet.value: AWLocationData(36, ByteSect.flames, 0x220, ["Flames"], AWTracker(627, 5, 1, -2, 1)),
    lname.flame_green.value: AWLocationData(35, ByteSect.flames, 0x221, ["Flames"], AWTracker(627, 5, 1, -2, 3)),

    # eggs, sorted by row top-to-bottom
    lname.egg_reference.value: AWLocationData(38, ByteSect.items, 0, ["Eggs"], AWTracker(90, 0, 0, 0, 0)),
    lname.egg_brown.value: AWLocationData(39, ByteSect.items, 1, ["Eggs"], AWTracker(90, 0, 0, 0, 1)),
    lname.egg_raw.value: AWLocationData(40, ByteSect.items, 2, ["Eggs"], AWTracker(90, 0, 0, 0, 2)),
    lname.egg_pickled.value: AWLocationData(41, ByteSect.items, 3, ["Eggs"], AWTracker(90, 0, 0, 0, 3)),
    lname.egg_big.value: AWLocationData(42, ByteSect.items, 4, ["Eggs"], AWTracker(90, 0, 0, 0, 4)),
    lname.egg_swan.value: AWLocationData(43, ByteSect.items, 5, ["Eggs"], AWTracker(90, 0, 0, 0, 5)),
    lname.egg_forbidden.value: AWLocationData(44, ByteSect.items, 6, ["Eggs"], AWTracker(90, 0, 0, 0, 6)),
    lname.egg_shadow.value: AWLocationData(45, ByteSect.items, 7, ["Eggs"], AWTracker(90, 0, 0, 0, 7)),
    lname.egg_vanity.value: AWLocationData(46, ByteSect.items, 8, ["Eggs"], AWTracker(90, 0, 0, 0, 8)),
    lname.egg_service.value: AWLocationData(47, ByteSect.items, 9, ["Eggs"], AWTracker(90, 0, 0, 0, 9)),

    lname.egg_depraved.value: AWLocationData(48, ByteSect.items, 12, ["Eggs"], AWTracker(90, 0, 0, 0, 10)),
    lname.egg_chaos.value: AWLocationData(49, ByteSect.items, 14, ["Eggs"], AWTracker(90, 0, 0, 0, 11)),
    lname.egg_upside_down.value: AWLocationData(50, ByteSect.items, 17, ["Eggs"], AWTracker(90, 0, 0, 0, 12)),
    lname.egg_evil.value: AWLocationData(51, ByteSect.items, 18, ["Eggs"], AWTracker(90, 0, 0, 0, 13)),
    lname.egg_sweet.value: AWLocationData(52, ByteSect.items, 20, ["Eggs"], AWTracker(90, 0, 0, 0, 14)),
    lname.egg_chocolate.value: AWLocationData(53, ByteSect.items, 22, ["Eggs"], AWTracker(90, 0, 0, 0, 15)),
    lname.egg_value.value: AWLocationData(54, ByteSect.items, 23, ["Eggs"], AWTracker(90, 0, 0, 0, 16)),
    lname.egg_plant.value: AWLocationData(55, ByteSect.items, 24, ["Eggs"], AWTracker(90, 0, 0, 0, 17)),
    lname.egg_red.value: AWLocationData(56, ByteSect.items, 25, ["Eggs"], AWTracker(90, 0, 0, 0, 18)),
    lname.egg_orange.value: AWLocationData(57, ByteSect.items, 26, ["Eggs"], AWTracker(90, 0, 0, 0, 19)),
    lname.egg_sour.value: AWLocationData(58, ByteSect.items, 28, ["Eggs"], AWTracker(90, 0, 0, 0, 20)),
    lname.egg_post_modern.value: AWLocationData(59, ByteSect.items, 29, ["Eggs"], AWTracker(90, 0, 0, 0, 21)),

    lname.egg_universal.value: AWLocationData(60, ByteSect.items, 31, ["Eggs"], AWTracker(90, 0, 0, 0, 22)),
    lname.egg_lf.value: AWLocationData(61, ByteSect.items, 32, ["Eggs"], AWTracker(90, 0, 0, 0, 23)),
    lname.egg_zen.value: AWLocationData(62, ByteSect.items, 33, ["Eggs"], AWTracker(90, 0, 0, 0, 24)),
    lname.egg_future.value: AWLocationData(63, ByteSect.items, 35, ["Eggs"], AWTracker(90, 0, 0, 0, 25)),
    lname.egg_friendship.value: AWLocationData(64, ByteSect.items, 36, ["Eggs"], AWTracker(90, 0, 0, 0, 26)),
    lname.egg_truth.value: AWLocationData(65, ByteSect.items, 40, ["Eggs"], AWTracker(90, 0, 0, 0, 27)),
    lname.egg_transcendental.value: AWLocationData(66, ByteSect.items, 42, ["Eggs"], AWTracker(90, 0, 0, 0, 28)),
    lname.egg_ancient.value: AWLocationData(67, ByteSect.items, 43, ["Eggs"], AWTracker(90, 0, 0, 0, 29)),
    lname.egg_magic.value: AWLocationData(68, ByteSect.items, 44, ["Eggs"], AWTracker(90, 0, 0, 0, 30)),
    lname.egg_mystic.value: AWLocationData(69, ByteSect.items, 45, ["Eggs"], AWTracker(90, 0, 0, 0, 31)),
    lname.egg_holiday.value: AWLocationData(70, ByteSect.items, 51, ["Eggs"], AWTracker(90, 0, 0, 0, 32)),
    lname.egg_rain.value: AWLocationData(71, ByteSect.items, 52, ["Eggs"], AWTracker(90, 0, 0, 0, 33)),
    lname.egg_razzle.value: AWLocationData(72, ByteSect.items, 53, ["Eggs"], AWTracker(90, 0, 0, 0, 34)),
    lname.egg_dazzle.value: AWLocationData(73, ByteSect.items, 55, ["Eggs"], AWTracker(90, 0, 0, 0, 35)),

    lname.egg_virtual.value: AWLocationData(74, ByteSect.items, 57, ["Eggs"], AWTracker(90, 0, 0, 0, 36)),
    lname.egg_normal.value: AWLocationData(75, ByteSect.items, 58, ["Eggs"], AWTracker(90, 0, 0, 0, 37)),
    lname.egg_great.value: AWLocationData(76, ByteSect.items, 59, ["Eggs"], AWTracker(90, 0, 0, 0, 38)),
    lname.egg_gorgeous.value: AWLocationData(77, ByteSect.items, 60, ["Eggs"], AWTracker(90, 0, 0, 0, 39)),
    lname.egg_planet.value: AWLocationData(78, ByteSect.items, 64, ["Eggs"], AWTracker(90, 0, 0, 0, 40)),
    lname.egg_moon.value: AWLocationData(79, ByteSect.items, 65, ["Eggs"], AWTracker(90, 0, 0, 0, 41)),
    lname.egg_galaxy.value: AWLocationData(80, ByteSect.items, 66, ["Eggs"], AWTracker(90, 0, 0, 0, 42)),
    lname.egg_sunset.value: AWLocationData(81, ByteSect.items, 67, ["Eggs"], AWTracker(90, 0, 0, 0, 43)),
    lname.egg_goodnight.value: AWLocationData(82, ByteSect.items, 69, ["Eggs"], AWTracker(90, 0, 0, 0, 44)),
    lname.egg_dream.value: AWLocationData(83, ByteSect.items, 71, ["Eggs"], AWTracker(90, 0, 0, 0, 45)),
    lname.egg_travel.value: AWLocationData(84, ByteSect.items, 72, ["Eggs"], AWTracker(90, 0, 0, 0, 46)),
    lname.egg_promise.value: AWLocationData(85, ByteSect.items, 73, ["Eggs"], AWTracker(90, 0, 0, 0, 47)),
    lname.egg_ice.value: AWLocationData(86, ByteSect.items, 74, ["Eggs"], AWTracker(90, 0, 0, 0, 48)),
    lname.egg_fire.value: AWLocationData(87, ByteSect.items, 76, ["Eggs"], AWTracker(90, 0, 0, 0, 49)),

    lname.egg_bubble.value: AWLocationData(88, ByteSect.items, 77, ["Eggs"], AWTracker(90, 0, 0, 0, 50)),
    lname.egg_desert.value: AWLocationData(89, ByteSect.items, 78, ["Eggs"], AWTracker(90, 0, 0, 0, 51)),
    lname.egg_clover.value: AWLocationData(90, ByteSect.items, 80, ["Eggs"], AWTracker(90, 0, 0, 0, 52)),
    lname.egg_brick.value: AWLocationData(91, ByteSect.items, 84, ["Eggs"], AWTracker(90, 0, 0, 0, 53)),
    lname.egg_neon.value: AWLocationData(92, ByteSect.items, 85, ["Eggs"], AWTracker(90, 0, 0, 0, 54)),
    lname.egg_iridescent.value: AWLocationData(93, ByteSect.items, 87, ["Eggs"], AWTracker(90, 0, 0, 0, 55)),
    lname.egg_rust.value: AWLocationData(94, ByteSect.items, 88, ["Eggs"], AWTracker(90, 0, 0, 0, 56)),
    lname.egg_scarlet.value: AWLocationData(95, ByteSect.items, 89, ["Eggs"], AWTracker(90, 0, 0, 0, 57)),
    lname.egg_sapphire.value: AWLocationData(96, ByteSect.items, 91, ["Eggs"], AWTracker(90, 0, 0, 0, 58)),
    lname.egg_ruby.value: AWLocationData(97, ByteSect.items, 92, ["Eggs"], AWTracker(90, 0, 0, 0, 59)),
    lname.egg_jade.value: AWLocationData(98, ByteSect.items, 93, ["Eggs"], AWTracker(90, 0, 0, 0, 60)),
    lname.egg_obsidian.value: AWLocationData(99, ByteSect.items, 94, ["Eggs"], AWTracker(90, 0, 0, 0, 61)),
    lname.egg_crystal.value: AWLocationData(100, ByteSect.items, 99, ["Eggs"], AWTracker(90, 0, 0, 0, 62)),
    lname.egg_golden.value: AWLocationData(101, ByteSect.items, 101, ["Eggs"], AWTracker(90, 0, 0, 0, 63)),

    lname.egg_65.value: AWLocationData(102, ByteSect.items, 47, ["Egg Rewards"], AWTracker(711)),

    # map things
    lname.map_chest.value: AWLocationData(103, ByteSect.items, 61, [], AWTracker(214)),
    lname.stamp_chest.value: AWLocationData(104, ByteSect.items, 50, [], AWTracker(149)),
    lname.pencil_chest.value: AWLocationData(105, ByteSect.items, 49, ["Egg Rewards"], AWTracker(442)),

    # bnnnnuyuyooooom
    lname.bunny_mural.value: AWLocationData(106, ByteSect.bunnies, 15, ["Bunnies"], AWTracker(293, 1, 0, 2)),
    lname.bunny_chinchilla_vine.value: AWLocationData(107, ByteSect.bunnies, 11, ["Bunnies"], AWTracker(0, 1, 83, 198)),
    lname.bunny_water_spike.value: AWLocationData(108, ByteSect.bunnies, 0, ["Bunnies"], AWTracker(0, 1, 402, 266)),
    lname.bunny_map.value: AWLocationData(109, ByteSect.bunnies, 7, ["Bunnies"], AWTracker(0, 1, 544, 147)),
    lname.bunny_uv.value: AWLocationData(110, ByteSect.bunnies, 9, ["Bunnies"], AWTracker(0, 1, 0, -4)),
    lname.bunny_fish.value: AWLocationData(111, ByteSect.bunnies, 6, ["Bunnies"], AWTracker(0, 1, 327, 264)),
    lname.bunny_face.value: AWLocationData(112, ByteSect.bunnies, 4, ["Bunnies"], AWTracker(117, 1, -1, 2, 10)),
    lname.bunny_crow.value: AWLocationData(113, ByteSect.bunnies, 31, ["Bunnies"], AWTracker(0, 1, 604, 112)),
    lname.bunny_duck.value: AWLocationData(114, ByteSect.bunnies, 22, ["Bunnies"], AWTracker(580, 1, 2, 1)),
    lname.bunny_dream.value: AWLocationData(115, ByteSect.bunnies, 28, ["Bunnies"], AWTracker(0, 1, 297, 335)),
    lname.bunny_file_bud.value: AWLocationData(116, ByteSect.bunnies, 10, ["Bunnies"], AWTracker(0, 1, 241, 287)),
    lname.bunny_lava.value: AWLocationData(117, ByteSect.bunnies, 30, ["Bunnies"], AWTracker(0, 1, 279, 146)),
    lname.bunny_tv.value: AWLocationData(118, ByteSect.bunnies, 8, ["Bunnies"], AWTracker(482, 1, 1, 0)),
    lname.bunny_barcode.value: AWLocationData(119, ByteSect.bunnies, 2, ["Bunnies"], AWTracker(0, 1, 269, 147)),
    lname.bunny_ghost_dog.value: AWLocationData(120, ByteSect.bunnies, 25, ["Bunnies"], AWTracker(798, 1, 2, 4)),
    lname.bunny_disc_spike.value: AWLocationData(121, ByteSect.bunnies, 3, ["Bunnies"], AWTracker(0, 1, 83, 87)),

    # candles
    lname.candle_first.value: AWLocationData(122, ByteSect.candles, 7, ["Candles"], AWTracker(37, 3, -1, -3, 7)),
    lname.candle_dog_dark.value: AWLocationData(123, ByteSect.candles, 4, ["Candles"], AWTracker(37, 3, -1, -3, 4)),
    lname.candle_dog_switch_box.value: AWLocationData(124, ByteSect.candles, 3, ["Candles"], AWTracker(37, 3, -1, -3, 3)),
    lname.candle_dog_many_switches.value: AWLocationData(125, ByteSect.candles, 2, ["Candles"], AWTracker(37, 3, -1, -3, 2)),
    lname.candle_dog_disc_switches.value: AWLocationData(126, ByteSect.candles, 1, ["Candles"], AWTracker(37, 3, -1, -3, 1)),
    lname.candle_dog_bat.value: AWLocationData(127, ByteSect.candles, 0, ["Candles"], AWTracker(37, 3, -1, -3, 0)),
    lname.candle_fish.value: AWLocationData(128, ByteSect.candles, 6, ["Candles"], AWTracker(37, 3, -1, -3, 6)),
    lname.candle_frog.value: AWLocationData(129, ByteSect.candles, 8, ["Candles"], AWTracker(37, 3, -1, -3, 8)),
    lname.candle_bear.value: AWLocationData(130, ByteSect.candles, 5, ["Candles"], AWTracker(37, 3, -1, -3, 5)),

    # extras
    lname.mama_cha.value: AWLocationData(131, ByteSect.items, 10, [], AWTracker(811)),
}

# mostly for the logic tracker
events_table: Dict[str, AWLocationData] = {
    lname.candle_first_event.value: AWLocationData(None, ByteSect.candles, 7, ["Candles"], AWTracker(37, 3, -1, -3, 7)),
    lname.candle_dog_dark_event.value: AWLocationData(None, ByteSect.candles, 4, ["Candles"], AWTracker(37, 3, -1, -3, 4)),
    lname.candle_dog_switch_box_event.value: AWLocationData(None, ByteSect.candles, 3, ["Candles"], AWTracker(37, 3, -1, -3, 3)),
    lname.candle_dog_many_switches_event.value: AWLocationData(None, ByteSect.candles, 2, ["Candles"], AWTracker(37, 3, -1, -3, 2)),
    lname.candle_dog_disc_switches_event.value: AWLocationData(None, ByteSect.candles, 1, ["Candles"], AWTracker(37, 3, -1, -3, 1)),
    lname.candle_dog_bat_event.value: AWLocationData(None, ByteSect.candles, 0, ["Candles"], AWTracker(37, 3, -1, -3, 0)),
    lname.candle_fish_event.value: AWLocationData(None, ByteSect.candles, 6, ["Candles"], AWTracker(37, 3, -1, -3, 6)),
    lname.candle_frog_event.value: AWLocationData(None, ByteSect.candles, 8, ["Candles"], AWTracker(37, 3, -1, -3, 8)),
    lname.candle_bear_event.value: AWLocationData(None, ByteSect.candles, 5, ["Candles"], AWTracker(37, 3, -1, -3, 5)),

    lname.flame_blue.value: AWLocationData(None, ByteSect.flames, 0x21E, ["Flames"], AWTracker(627, 5, 1, -2, 2)),
    lname.flame_pink.value: AWLocationData(None, ByteSect.flames, 0x21F, ["Flames"], AWTracker(627, 5, 1, -2, 0)),
    lname.flame_violet.value: AWLocationData(None, ByteSect.flames, 0x220, ["Flames"], AWTracker(627, 5, 1, -2, 1)),
    lname.flame_green.value: AWLocationData(None, ByteSect.flames, 0x221, ["Flames"], AWTracker(627, 5, 1, -2, 3)),
}

location_name_to_id: Dict[str, int] = {name: location_base_id + data.offset for name, data in location_table.items()}

location_name_groups: Dict[str, Set[str]] = {}
for loc_name, loc_data in location_table.items():
    for location_group in loc_data.location_groups:
        location_name_groups.setdefault(location_group, set()).add(loc_name)
