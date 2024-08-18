from enum import Enum


class RegionNames(str, Enum):
    def __str__(self) -> str:
        return self.value

    menu = "Menu"
    fast_travel_fake = "Fast Travel Mid-Warp"  # for the purpose of not putting all the entrances at the starting region
    starting_area = "Squirrel Main"
    bulb_bunny_spot = "Squirrel Bulb Bunny Spot"
    s_disc_area = "Squirrel S. Medal Area"
    starting_after_ghost = "Squirrel After Ghost"
    fast_travel = "Fast Travel Room"
    fast_travel_fish_teleport = "Fast Travel Fish Teleport Spot"
    bird_area = "Bird Area"  # the central portion of the map
    bird_capybara_waterfall = "Bird Capybara Waterfall"  # up and right of the ladder
    bird_below_mouse_statues = "Bird Below Mouse Statues"  # on the way to frog area, need yoyo
    candle_area = "Squirrel Candle Area"
    match_above_egg_room = "Match Above Egg Room"  # its own region since you can use the dog elevator
    bird_flute_chest = "Bird Flute Chest Room"  # since you can technically get weird with the logic here
    water_spike_bunny_spot = "Water Spike Bunny Spot"

    fish_upper = "Fish Upper"  # everything prior to the bubble wand chest
    fish_lower = "Fish Lower"
    fish_boss_1 = "Fish Boss Arena Part 1"  # just the whale
    fish_boss_2 = "Fish Boss Arena Part 2"  # whale + seahorse
    fish_wand_pit = "Fish B.Wand Chest Pit"
    fish_west = "Fish Warp Room"  # after the b. wand chest, rename
    fish_tube_room = "Fish Pipe Maze"  # rename?

    abyss = "Bone Fish Area"
    abyss_lower = "Bone Fish Arena"
    uv_lantern_spot = "UV Lantern Spot"

    bear_area_entry = "Bear Main Entry"
    bear_capybara_and_below = "Bear Main Area"
    bear_future_egg_room = "Bear Future Egg Room"
    bear_chinchilla_song_room = "Bear Chinchilla Song Room"  # where the bunny is
    bear_dark_maze = "Bear Dark Maze"
    bear_chameleon_room_1 = "Bear Chameleon Room 1"  # first chameleon encounter with the chinchilla
    bear_ladder_after_chameleon = "Bear Ladder after Chameleon 1"
    bear_slink_room = "Bear Slink Room"  # the room you get slink
    bear_transcendental = "Bear Transcendental Egg Room"
    bear_kangaroo_waterfall = "Bear Kangaroo Waterfall and adjacent rooms"  # up left from entry point, need slink
    bear_middle_phone_room = "Bear Middle Phone Room"  # after the previous region, has the fast travel, monkey room
    bear_crow_rooms = "Bear Crow Rooms"  # the room with a lot of crows, the room with 8 crows, and the room with 4 crows
    bear_shadow_egg_spot = "Bear Shadow Egg Chest Spot"  # since you can get here from above with top
    bear_hedgehog_square = "Bear Hedgehog on the Square Room"  # the one where the hedgehog presses 4 buttons
    bear_connector_passage = "Bear Connector Passage"  # connects capybara save room, upper bear
    bear_match_chest_spot = "Bear Match Chest Spot"  # where the match chest is, it's weird okay
    bear_upper_phone_room = "Bear Upper Phone Room"
    bear_above_chameleon = "Bear Above Chameleon Boss"  # right above the chameleon boss before the flame
    bear_chameleon_room_2 = "Bear Chameleon Boss Room before Flame"
    bear_razzle_egg_spot = "Bear Razzle Egg Spot"
    bear_truth_egg_spot = "Bear Truth Egg Spot"
    bear_map_bunny_spot = "Bear Map Bunny Spot"

    dog_area = "Dog Main"
    dog_chinchilla_skull = "Dog Chinchilla Skull Room"
    dog_at_mock_disc = "Dog at Mock Disc Chest"
    dog_upper = "Dog Area Upper"  # rename this variable and name
    dog_upper_past_lake = "Dog Area Upper past Lake"
    dog_upper_above_switch_lines = "Dog Area Upper above Switch Lines"  # rename, that spot where you go up the levels?
    dog_upper_above_switch_lines_to_upper_east = "Dog Area Upper above Switch Lines to Upper East"  # where the button is
    dog_upper_east = "Dog Area Upper East"  # to the right of the area above the switch lines
    bobcat_room = "Bobcat Room"
    chest_on_spikes_region = "Chest on Spikes Region"
    dog_elevator = "Dog Elevator"  # east of the flame
    dog_many_switches = "Dog Switches and Bat"  # west of spike room
    dog_upside_down_egg_spot = "Dog Upside Down Egg Spot"
    dog_bat_room = "Dog Bat Room"
    dog_under_fast_travel_room = "Dog Room under Fast Travel Door Room"
    dog_fast_travel_room = "Dog Room with Fast Travel Door"
    dog_swordfish_lake_ledge = "Dog Left side of Swordfish Lake"
    behind_kangaroo = "Vertical Passage behind Kangaroo Room"
    dog_above_fast_travel = "Dog Above Fast Travel Room"  # has some of those breakout blocks
    dog_mock_disc_shrine = "Dog Mock Disc Shrine"  # and the rooms to the left of it
    kangaroo_room = "Kangaroo Room"
    kangaroo_blocks = "Kangaroo Room Blocks"
    dog_wheel = "Dog Wheel"  # doggo getting swole af
    dog_elevator_upper = "Dog Elevator Upper"  # top of the elevator going up

    frog_near_wombat = "Frog Area near Groundhog"  # first part of the frog area after you drop down the hole
    frog_under_ostrich_statue = "Frog Area under Ostrich Statue"  # just the dark room basically
    frog_pre_ostrich_attack = "Frog before Ostrich Attack"  # left of dark room, right of ostrich, above dynamite
    frog_ostrich_attack = "Frog Ostrich Attack"  # and also the little area above it
    frog_worm_shaft_top = "Frog Worm Shaft Top"  # where the fire egg is
    frog_worm_shaft_bottom = "Frog Worm Shaft Bottom"  # save point after ostrich chase
    frog_bird_after_yoyo_1 = "Frog Bird Area after Yoyo 1"  # the first two bird rooms after you get yoyo
    frog_bird_after_yoyo_2 = "Frog Bird Area after Yoyo 2"  # the area after the previous one (rewrite comment)
    frog_dark_room = "Wave Room"  # the dark room with the frog, and also the wave room
    frog_ruby_egg_ledge = "Ruby Egg Ledge"  # the ledge with the ruby egg in the frog dark room
    frog_east_of_fast_travel = "Frog East of Fast Travel"  # one screen to the right of the fast travel spot
    frog_elevator_and_ostrich_wheel = "Frog Elevator and Ostrich Wheel Section"  # interdependent, so one big region
    frog_travel_egg_spot = "Frog Travel Egg Spot"

    hippo_entry = "Hippo Entry"  # the beginning of the end
    hippo_manticore_room = "Hippo Manticore Room"  # the 4 rooms you evade the manticore in for the first ending
    hippo_skull_room = "Hippo Skull Room"  # B. B. Wand and the skull pile
    hippo_fireworks = "Hippo Fireworks Room"  # the first ending

    home = "Home"
    barcode_bunny = "Barcode Bunny"  # barcode bunny is gotten in two places
    top_of_the_well = "Top of the Well"  # where the warp song takes you, right of the house
    chocolate_egg_spot = "Chocolate Egg Spot"
    value_egg_spot = "Value Egg Spot" 
    match_center_well_spot = "Center Well Match Spot"  # in the shaft, across from chocolate egg
    zen_egg_spot = "Zen Egg Spot"  # contains zen egg and universal basic egg


class ItemNames(str, Enum):
    def __str__(self) -> str:
        return self.value

    # major unique items
    bubble = "B. Wand"
    flute = "Animal Flute"
    slink = "Slink"
    yoyo = "Yoyo"
    m_disc = "Mock Disc"
    disc = "Disc"
    lantern = "Lantern"
    ball = "B. Ball"
    remote = "Remote"
    uv = "UV Lantern"
    wheel = "Wheel"
    top = "Top"
    bubble_long_real = "B.B. Wand"
    firecrackers = "Firecrackers"
    house_key = "House Key"
    office_key = "Office Key"
    fanny_pack = "F. Pack"
    k_shard = "K. Shard"
    k_medal = "K. Medal"  # a fake item. 3 K. Shards exist in pool
    s_medal = "S. Medal"
    e_medal = "E. Medal"

    match = "Match"
    matchbox = "Matchbox"  # potentially an item if we want to simplify logic

    key = "Key"
    key_ring = "Key Ring"  # potentially an item if we want to simplify logic

    # flames
    blue_flame = "B. Flame"  # seahorse
    green_flame = "G. Flame"  # ostritch
    pink_flame = "P. Flame"  # ghost dog
    violet_flame = "V. Flame"  # chameleon

    # eggs, in a particular order but not one that actually matters
    egg_forbidden = "Forbidden Egg"
    egg_vanity = "Vanity Egg"
    egg_reference = "Reference Egg"
    egg_brown = "Brown Egg"
    egg_service = "Egg As A Service"
    egg_upside_down = "Upside Down Egg"
    egg_red = "Red Egg"
    egg_friendship = "Friendship Egg"
    egg_plant = "Plant Egg"
    egg_future = "Future Egg"
    egg_raw = "Raw Egg"
    egg_evil = "Evil Egg"
    egg_orange = "Orange Egg"
    egg_depraved = "Depraved Egg"
    egg_sour = "Sour Egg"
    egg_sweet = "Sweet Egg"
    egg_crystal = "Crystal Egg"
    egg_big = "Big Egg"
    egg_pickled = "Pickled Egg"
    egg_chocolate = "Chocolate Egg"
    egg_post_modern = "Post Modern Egg"
    egg_truth = "Truth Egg"
    egg_transcendental = "Transcendental Egg"
    egg_swan = "Swan Egg"
    egg_shadow = "Shadow Egg"
    egg_chaos = "Chaos Egg"
    egg_value = "Value Egg"
    egg_zen = "Zen Egg"
    egg_razzle = "Razzle Egg"
    egg_lf = "Laissez-faire Egg"
    egg_universal = "Universal Basic Egg"
    egg_rain = "Rain Egg"
    egg_holiday = "Holiday Egg"
    egg_virtual = "Virtual Egg"
    egg_great = "Great Egg"
    egg_mystic = "Mystic Egg"
    egg_normal = "Normal Egg"
    egg_dazzle = "Dazzle Egg"
    egg_magic = "Magic Egg"
    egg_ancient = "Ancient Egg"
    egg_galaxy = "Galaxy Egg"
    egg_sunset = "Sunset Egg"
    egg_goodnight = "Goodnight Egg"
    egg_brick = "Brick Egg"
    egg_clover = "Clover Egg"
    egg_neon = "Neon Egg"
    egg_ice = "Ice Egg"
    egg_iridescent = "Iridescent Egg"
    egg_gorgeous = "Gorgeous Egg"
    egg_dream = "Dream Egg"
    egg_travel = "Travel Egg"
    egg_planet = "Planet Egg"
    egg_bubble = "Bubble Egg"
    egg_moon = "Moon Egg"
    egg_promise = "Promise Egg"
    egg_fire = "Fire Egg"
    egg_sapphire = "Sapphire Egg"
    egg_ruby = "Ruby Egg"
    egg_rust = "Rust Egg"
    egg_jade = "Jade Egg"
    egg_desert = "Desert Egg"
    egg_scarlet = "Scarlet Egg"
    egg_obsidian = "Obsidian Egg"
    egg_golden = "Golden Egg"

    egg_65 = "65th Egg"

    # event items
    activated_bird_fast_travel = "Activated Bird Fast Travel"
    activated_bear_fast_travel = "Activated Bear Fast Travel"
    activated_frog_fast_travel = "Activated Frog Fast Travel"
    activated_squirrel_fast_travel = "Activated Squirrel Fast Travel"
    activated_fish_fast_travel = "Activated Fish Fast Travel"
    activated_dog_fast_travel = "Activated Dog Fast Travel"
    activated_hippo_fast_travel = "Activated Hippo Fast Travel"
    activated_bonefish_fast_travel = "Activated Bone Fish Fast Travel"
    defeated_chameleon = "Defeated Chameleon"
    switch_for_post_modern_egg = "Activated Switch for Post Modern Egg"
    switch_next_to_bat_room = "Activated Switch next to Bat Room"  # for getting up to the fast travel spot in dog area
    dog_wheel_flip = "Flipped Dog Wheel"

    victory = "Victory"

    event_candle_first = "Lit the First Candle"  # rename
    event_candle_dog_dark = "Lit the Dog Area's Dark Room Candle"
    event_candle_dog_switch_box = "Lit the Dog Area's Candle in the Switch Box"
    event_candle_dog_many_switches = "Lit the Dog Area's Candle by Many Switches"
    event_candle_dog_disc_switches = "Lit the Dog Area's Candle in Disc Switch Maze"
    event_candle_dog_bat = "Lit the Dog Area's Candle in the Bat Room"
    event_candle_penguin = "Lit the Candle by the Penguins"
    event_candle_frog = "Lit the Frog Area Candle"
    event_candle_bear = "Lit the Bear Area Candle"

    can_use_matches = "Can Use Matches"  # for when you get all of the matches, consumables logic is cool
    can_use_keys = "Can Use Keys"  # for when you get all of the keys, consumables logic is cool

    # fake items, for the purposes of rules
    bubble_short = "Bubble Jumping - Short"
    bubble_long = "Bubble Jumping - Long"
    can_break_spikes = "Can Break Spikes"
    can_break_spikes_below = "Can Break Spikes Below"  # can break spikes but without disc basically
    can_open_flame = "Can Open Flame"  # you can break this with the flute and other items, need to verify which
    disc_hop = "Disc Jumping"  # hopping on a disc in midair without it bouncing first
    disc_hop_hard = "Consecutive Disc Jumps"  # hopping on a disc multiple times, or after a bubble jump
    wheel_hop = "Wheel Hop"  # expanding and retracting wheel midair to grant a double jump
    wheel_climb = "Wheel Climb"  # hugging a wall and mashing the jump button to get vertical
    wheel_hard = "Advanced Wheel Techniques"  # using other wheel exploits, such as wall stalls, to get access to areas that wheel jumps/climbs can't do alone 
    can_distract_dogs = "Can Distract Dogs"
    can_defeat_ghost = "Can Defeat Ghost"
    # rename tanking_damage's string when we have enough spots to make it viable as an option or something
    tanking_damage = "Tanking Damage"  # for spots you can get to by taking up to 3 hearts of damage
    weird_tricks = "Weird Tricks"  # skips that are questionably in logic and may constitute a difficulty setting later
    ball_throwing = "Ball Throwing"  # logic for throwing the ball at anything other than a block or a spike
    obscure_tricks = "Obscure Tricks"  # solutions that are weird but not necessarily difficult
    precise_tricks = "Precise Tricks"  # solutions that are difficult but not necessarily weird
    water_bounce = "Water Bounce"  # tricks that use Yoyo, B.Ball, or some other way to generate a splash effect to bounce off the water


    # songs, to potentially be randomized
    song_home = "Top of the Well Song"
    song_egg = "Egg Song"
    song_chinchilla = "Chinchilla Song"  # the warp to the chinchilla vine platform bunny
    song_bobcat = "Bobcat Song"  # idk what we should do with this, but it kinda sucks as it is
    song_fish = "Skeleton Fish Song"  # teleports you to the right side of the lower screen of the fast travel room
    song_barcode = "Barcode Song"  # for barcode bunny


class LocationNames(str, Enum):
    def __str__(self) -> str:
        return self.value

    # major unique items
    map_chest = "Map Chest"
    stamp_chest = "Stamp Chest"
    pencil_chest = "Pencil Chest"

    b_wand_chest = "B. Wand Chest"
    flute_chest = "Animal Flute Chest"
    slink_chest = "Slink Chest"
    yoyo_chest = "Yoyo Chest"
    mock_disc_chest = "Mock Disc Chest"
    disc_spot = "Wolf Disc Shrine"
    lantern_chest = "Lantern Chest"
    b_ball_chest = "B. Ball Chest"
    remote_chest = "Remote Chest"
    uv_lantern_chest = "UV Lantern Chest"
    wheel_chest = "Wheel Chest"
    top_chest = "Top Chest"
    bb_wand_chest = "B.B. Wand Chest"
    # firecracker_first = "Pick Up Firecrackers"
    fanny_pack_chest = "Fanny Pack Chest"
    key_house = "House Key Drop"
    key_office = "Office Key Chest"
    # medal_k = "K. Medal Shard Bag"  # you need three to open the kangaroo door
    medal_s = "S. Medal Chest"
    medal_e = "E. Medal Chest"

    # minor unique items
    mama_cha = "Mama Cha Chest"  # the same place as the barcode bunny at grass bowl

    # match chests
    match_start_ceiling = "Match in Tutorial Chest"
    match_fish_mural = "Match in Fish Mural Room Chest"
    match_dog_switch_bounce = "Match in Switch-Bounce Room Chest"  # rename, in that spot where you throw the between the levers
    match_dog_upper_east = "Match by Dog Fish Pipe Chest"
    match_bear = "Match in Bear Area"
    match_above_egg_room = "Match Above Egg Room"  # the one to the right of the dog lower entrance
    match_center_well = "Match in Center Well Chest"  # the one high up in the shaft
    match_guard_room = "Match in Guard Room Chest"
    match_under_mouse_statue = "Match under Mouse Statue"  # east bird area, need yoyo to get in

    # candle checks
    candle_first = "Squirrel First Candle"  # the obvious first one
    candle_dog_dark = "Dog Dark Room Candle"  # the one in the dark room a few rooms after your first dog encounter
    candle_dog_switch_box = "Dog Boxed Candle"
    candle_dog_many_switches = "Dog Candle in Many Switches Room"
    candle_dog_disc_switches = "Dog Candle in Disc Switch Maze"
    candle_dog_bat = "Dog Candle in Bat Room"
    candle_fish = "Fish Candle in Penguin Room"
    candle_frog = "Frog Candle Switch Carousel"  # to screens to the right of the wombat save point
    candle_bear = "Bear Candle in Dark Maze"

    # candle checks - event versions
    candle_first_event = "Squirrel First Candle Event"  # the obvious first one
    candle_dog_dark_event = "Dog Dark Room Candle Event"  # the one in the dark room a few rooms after your first dog encounter
    candle_dog_switch_box_event = "Dog Boxed Candle Event"
    candle_dog_many_switches_event = "Dog Candle in Many Switches Room Event"
    candle_dog_disc_switches_event = "Dog Candle in Disc Switch Maze Event"
    candle_dog_bat_event = "Dog Candle in Bat Room Event"
    candle_fish_event = "Fish Candle in Penguin Room Event"
    candle_frog_event = "Frog Candle Switch Carousel Event"  # to screens to the right of the wombat save point
    candle_bear_event = "Bear Candle in Dark Maze Event"

    # key chests
    key_bear_lower = "Key Chest in Lower Bear"  # early in the green area
    key_bear_upper = "Key Chest in Upper Bear"  # get the chest to land on the chinchilla, maybe rename these two
    key_chest_mouse_head_lever = "Key Chest by Mouse Head Hitting Lever"  # rename definitely
    key_frog_guard_room_west = "Key Chest in West Frog Guard Room"
    key_frog_guard_room_east = "Key Chest in East Frog Guard Room"
    key_dog = "Key Chest in Dog with Chinchilla Crank"  # maybe rename

    # flames
    flame_blue = "B. Flame"  # fish area
    flame_green = "G. Flame"  # frog area
    flame_pink = "P. Flame"  # dog area
    flame_violet = "V. Flame"  # bear area

    # eggs, not in any particular order
    egg_forbidden = "Forbidden Egg Chest"  # swordfish lake
    egg_vanity = "Vanity Egg Chest"  # kangaroo breakout
    egg_reference = "Reference Egg Chest"  # dog region disc with fans puzzle
    egg_brown = "Brown Egg Chest"  # next to Reference Egg
    egg_service = "Egg As A Service Chest"  # behind Bat room
    egg_upside_down = "Upside Down Egg Chest"  # dog many switches room
    egg_red = "Red Egg Chest"  # dog double chinchilla puzzle
    egg_friendship = "Friendship Egg Chest"  # dark room from pipe maze
    egg_plant = "Plant Egg Chest"  # two boxes with disc puzzle
    egg_future = "Future Egg Chest"  # dark room behind chinchilla vines
    egg_raw = "Raw Egg Chest"  # dog slinky box puzzle
    egg_evil = "Evil Egg Chest"  # turtle flute pool
    egg_orange = "Orange Egg Chest"  # dog egg under telephone
    egg_depraved = "Depraved Egg Chest"  # dog switch maze
    egg_sour = "Sour Egg Chest"  # daschund tunnels
    egg_sweet = "Sweet Egg Chest"  # above dog wheel
    egg_crystal = "Crystal Egg Chest"  # dog wheel puzzle at bottom of the map
    egg_big = "Big Egg Chest"  # near Mock Disc Shrine
    egg_pickled = "Pickled Egg Chest"  # hidden spot in well wall
    egg_chocolate = "Chocolate Egg Chest"  # behind well wall switch blocks
    egg_post_modern = "Post Modern Egg Chest"  # well wall behind top dirt
    egg_truth = "Truth Egg Chest"  # bear above bottom left crow
    egg_transcendental = "Transcendental Egg Chest"  # below slink chest
    egg_swan = "Swan Egg Chest"  # bear next to Chameleon final boss entrance
    egg_shadow = "Shadow Egg Chest"  # near above arrow lift bridge
    egg_chaos = "Chaos Egg Chest"  # monke room
    egg_value = "Value Egg Chest"  # bear top hedgehog buttons
    egg_zen = "Zen Egg Chest"  # bear next to upper key
    egg_razzle = "Razzle Egg Chest"  # behind lowest chameleon
    egg_lf = "Laissez-faire Egg Chest"  # bear spook chinchilla room. Internal name may be bad but the full name is worse.
    egg_universal = "Universal Basic Egg Chest"  # next to Zen Egg
    egg_rain = "Rain Egg Chest"  # top dirt outside egg house
    egg_holiday = "Holiday Egg Chest"  # alcove outside egg house
    egg_virtual = "Virtual Egg Chest"  # behind Fish Mural switch blocks
    egg_great = "Great Egg Chest"  # after flamingos, not to be confused with Big Egg
    egg_mystic = "Mystic Egg Chest"  # top of bubble column room
    egg_normal = "Normal Egg Chest"  # betwen bubble rooms
    egg_dazzle = "Dazzle Egg Chest"  # fish bubble puzzle by top telephone
    egg_magic = "Magic Egg Chest"  # fish pipe maze
    egg_ancient = "Ancient Egg Chest"  # fish top left room
    egg_galaxy = "Galaxy Egg Chest"  # fish below warp room
    egg_sunset = "Sunset Egg Chest"  # above B Wand Chest
    egg_goodnight = "Goodnight Egg Chest"  # first penguin room
    egg_brick = "Brick Egg Chest"  # fish wheel rooms
    egg_clover = "Clover Egg Chest"  # left of start
    egg_neon = "Neon Egg Chest"  # snake area breakout reward
    egg_ice = "Ice Egg Chest"  # top of snake area
    egg_iridescent = "Iridescent Egg Chest"  # snake game reward
    egg_gorgeous = "Gorgeous Egg Chest"  # above first candle
    egg_dream = "Dream Egg Chest"  # below mouse head lever key
    egg_travel = "Travel Egg Chest"  # behind Groundhog locked door
    egg_planet = "Planet Egg Chest"  # hidden behind spikes by mouse head auto-lever
    egg_bubble = "Bubble Egg Chest"  # dark room below mouse statue
    egg_moon = "Moon Egg Chest"  # mouse head spam room
    egg_promise = "Promise Egg Chest"  # three ghost birds in mouse area
    egg_fire = "Fire Egg Chest"  # other side of chasm to frog area
    egg_sapphire = "Sapphire Egg Chest"  # below left ghost birds in frog area
    egg_ruby = "Ruby Egg Chest"  # below right ghost birds in frog area
    egg_rust = "Rust Egg Chest"  # between the sapphire and ruby eggs
    egg_jade = "Jade Egg Chest"  # annoying light curve puzzle
    egg_desert = "Desert Egg Chest"  # top of rat lab
    egg_scarlet = "Scarlet Egg Chest"  # by the momma cat, in spikes
    egg_obsidian = "Obsidian Egg Chest"  # behind fish pipe to lower rat lab
    egg_golden = "Golden Egg Chest"  # ostrich wheel puzzle

    egg_65 = "65th Egg Chest"  # move to Major Items if Eggsanity becomes a setting

    # bnuuy
    bunny_mural = "Community Bunny"
    bunny_map = "Doodle Bunny"
    bunny_uv = "Invisible Bunny"
    bunny_fish = "Fish Bunny"
    bunny_face = "Face Bunny"
    bunny_crow = "Singing Bunny"
    bunny_duck = "Illusion Bunny"
    bunny_dream = "Imaginary Bunny"
    bunny_lava = "Lava Bunny"  # floor is lava
    bunny_tv = "Flashing Bunny"
    bunny_ghost_dog = "Statue Bunny"  # ghost dog bunny
    bunny_disc_spike = "Disc Spike Bunny"
    bunny_water_spike = "Water Spike Bunny"
    bunny_barcode = "Paper Bunny"  # printer or barcode both get you it
    bunny_chinchilla_vine = "Chinchilla Bunny"  # the one where the code is covered by vines
    bunny_file_bud = "Flowering Bunny"  # bunny from file start codes

    # event locations
    activate_bird_fast_travel = "Activate Bird Fast Travel"
    activate_bear_fast_travel = "Activate Bear Fast Travel"
    activate_frog_fast_travel = "Activate Frog Fast Travel"
    activate_squirrel_fast_travel = "Activate Squirrel Fast Travel"
    activate_fish_fast_travel = "Activate Fish Fast Travel"
    activate_dog_fast_travel = "Activate Dog Fast Travel"
    activate_hippo_fast_travel = "Activate Hippo Fast Travel"
    activate_bonefish_fast_travel = "Activate Bone Fish Fast Travel"
    defeated_chameleon = "Defeated Chameleon"
    switch_for_post_modern_egg = "Switch for Post Modern Egg"
    switch_next_to_bat_room = "Switch next to Bat Room"  # for getting up to the fast travel spot in dog area
    dog_wheel_flip = "Can Flip Dog Wheel"  # item for you having access to the dog wheel
    light_all_candles = "Light All Candles"
    got_all_matches = "Received All Matches"  # for when you get all of the matches, consumables logic is cool
    got_all_keys = "Received All Keys"  # for when you get all of the keys, consumables logic is cool
    upgraded_wand = "Upgraded to B.B. Wand"  # for when you get your second b wand, this is a hack
    k_medal = "Assembled the K. Medal"
    kangaroo_first_spot = "Kangaroo First Spot"  # first spot the kangaroo appears
    victory_first = "First Victory"
