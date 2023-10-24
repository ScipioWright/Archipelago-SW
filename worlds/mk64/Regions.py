from BaseClasses import MultiWorld, Region, Location

from . import Locations
from .Options import GameMode, CourseOrder, Opt


def add_location(player: int, loc_name: str, code: int, region: Region) -> None:
    location = Locations.MK64Location(player, loc_name, code, region)
    region.locations.append(location)


def create_regions_locations_connections(multiworld: MultiWorld,
                                         player: int,
                                         opt: Opt,
                                         shuffle_clusters: list[bool],
                                         use_item_spots: list[bool]) -> tuple[Location, list[int]]:
    random = multiworld.random
    location_group_mask = (Locations.Group.base
                           | (opt.hazards and Locations.Group.hazard)
                           | (opt.secrets and Locations.Group.secret)
                           | (opt.shuffle_blues and Locations.Group.blue_shell_item_spot))

    # Prepare Region Handling
    menu_region = Region("Menu", player, multiworld)
    course_regions: list[Region] = []
    shared_hazard_regions: list[Region] = []
    cup_regions: list[Region] = []

    # Construct item_spot_locations for shuffled item clusters and extra locations
    random.shuffle(shuffle_clusters)
    random.shuffle(use_item_spots)
    item_spot_locations = []
    c, s, t = 0, 0, -1
    for region in Locations.item_cluster_locations:
        item_spot_locations.append([])
        for cluster in region:
            if shuffle_clusters[c]:
                t = random.randrange(0, len(cluster))
            c += 1
            for i, (spot, code) in enumerate(cluster.items()):
                if i == t:
                    item_spot_locations[-1].append((spot, code))
                    t = -1
                else:
                    if use_item_spots[s]:
                        item_spot_locations[-1].append((spot, code))
                    s += 1

    # Construct Course Regions and Locations
    for (course_name, locs), spot_locs in zip(Locations.course_locations.items(), item_spot_locations):
        course_regions.append(Region(course_name, player, multiworld))
        for loc_name, (code, group) in locs.items():
            if group & location_group_mask:
                add_location(player, loc_name, code, course_regions[-1])
        for spot_name, code in spot_locs:
            add_location(player, spot_name, code, course_regions[-1])

    # Shared Hazard Regions & Locations & Connections
    if opt.hazards:
        for name, (code, courses) in Locations.shared_hazard_locations.items():
            shared_hazard_regions.append(Region(name, player, multiworld))
            add_location(player, name, code, shared_hazard_regions[-1])
            for region in course_regions:
                if region.name in courses:
                    region.connect(name, "Use Star")

    # Cup Regions & Locations
    if opt.mode == GameMode.option_cups:
        for cup, locations in Locations.cup_locations.items():
            cup_regions.append(Region(cup, player, multiworld))
            for name, code in locations.items():
                add_location(player, name, code, cup_regions[-1])

    # Determine Course Order
    order = list(range(16))
    match opt.course_order:
        case CourseOrder.option_short_to_long:
            order = [1, 7, 6, 2, 0, 5, 14, 3, 9, 13, 11, 12, 10, 4, 8, 15]
        case CourseOrder.option_long_to_short:
            order = [15, 8, 4, 10, 12, 11, 13, 9, 3, 14, 5, 0, 2, 6, 7, 1]
        case CourseOrder.option_alphabetical:
            order = [14, 11, 6, 12, 5, 3, 2, 0, 7, 1, 15, 10, 9, 4, 8, 13]
        case CourseOrder.option_shuffle:
            random.shuffle(order)
            if opt.final_pool:
                order.append(tuple(Locations.course_locations).index(random.choice(opt.final_pool)))
                order.remove(order[-1])

    # Create Course & Cup Connections
    match opt.mode:
        case GameMode.option_cups:
            menu_region.connect(course_regions[order[0]], "Mushroom Cup 1")
            course_regions[order[0]].connect(course_regions[order[1]], "Mushroom Cup 2")
            course_regions[order[1]].connect(course_regions[order[2]], "Mushroom Cup 3")
            course_regions[order[2]].connect(course_regions[order[3]], "Mushroom Cup 4")
            course_regions[order[3]].connect(cup_regions[0], "Mushroom Cup Finish")
            menu_region.connect(course_regions[order[4]], "Flower Cup 1",
                                lambda state: state.has("Progressive Cup Unlock", player, 1))
            course_regions[order[4]].connect(course_regions[order[5]], "Flower Cup 2")
            course_regions[order[5]].connect(course_regions[order[6]], "Flower Cup 3")
            course_regions[order[6]].connect(course_regions[order[7]], "Flower Cup 4")
            course_regions[order[7]].connect(cup_regions[1], "Flower Cup Finish")
            menu_region.connect(course_regions[order[8]], "Star Cup 1",
                                lambda state: state.has("Progressive Cup Unlock", player, 2))
            course_regions[order[8]].connect(course_regions[order[9]], "Star Cup 2")
            course_regions[order[9]].connect(course_regions[order[10]], "Star Cup 3")
            course_regions[order[10]].connect(course_regions[order[11]], "Star Cup 4")
            course_regions[order[11]].connect(cup_regions[2], "Star Cup Finish")
            menu_region.connect(course_regions[order[12]], "Special Cup 1",
                                lambda state: state.has("Progressive Cup Unlock", player, 3))
            course_regions[order[12]].connect(course_regions[order[13]], "Special Cup 2")
            course_regions[order[13]].connect(course_regions[order[14]], "Special Cup 3")
            course_regions[order[14]].connect(course_regions[order[15]], "Special Cup 4")
            course_regions[order[15]].connect(cup_regions[3], "Special Cup Finish")
        case GameMode.option_courses:
            for i in range(16):
                locks = max(0, i + opt.locked_courses - 15)
                rule = (lambda state, k=locks: state.has("Progressive Course Unlock", player, k)) if locks > 0 else None
                menu_region.connect(course_regions[order[i]], f"Course {i + 1}", rule)

    # Register regions (and locations)
    multiworld.regions += [menu_region] + course_regions + shared_hazard_regions + cup_regions

    # Write course order to spoiler log
    for i in range(16):
        entrance = course_regions[order[i]].entrances[0]
        multiworld.spoiler.set_entrance(entrance.name, entrance.connected_region.name, "entrance", player)

    # Place Victory Event Location
    if opt.mode == GameMode.option_cups:
        cup_regions[-1].locations[-1].address = None    # Warning: Fragile to changes in Location indices
        cup_regions[-1].locations[-1].event = True      # Warning: Fragile to changes in Location indices
        victory_event_location = cup_regions[-1].locations[-1]
    else:
        course_regions[order[15]].locations[2].address = None   # Warning: Fragile to changes in Location indices
        course_regions[order[15]].locations[2].event = True     # Warning: Fragile to changes in Location indices
        victory_event_location = course_regions[order[15]].locations[2]

    return victory_event_location, order
