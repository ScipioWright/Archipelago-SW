from BaseClasses import MultiWorld, Region, Location

from . import Locations
from .Options import GameMode, CourseOrder, Opt
from .Rules import course_qualify_rules


def add_location(player: int, loc_name: str, code: int, region: Region) -> Locations.MK64Location:
    location = Locations.MK64Location(player, loc_name, code, region)
    region.locations.append(location)
    return location


def create_regions_locations_connections(multiworld: MultiWorld,
                                         player: int,
                                         opt: Opt,
                                         shuffle_clusters: list[bool],
                                         filler_spots: list[bool]) -> tuple[Location, list[int]]:
    random = multiworld.random
    location_group_mask = (Locations.Group.base
                           | (opt.hazards and Locations.Group.hazard)
                           | (opt.secrets and Locations.Group.secret)
                           | (opt.special_boxes and Locations.Group.blue_shell_item_spot))

    # Prepare Region Handling
    menu_region = Region("Menu", player, multiworld)
    course_regions: list[Region] = []
    shared_hazard_regions: list[Region] = []
    cup_regions: list[Region] = []

    # Construct item_spot_locations for shuffled item clusters and extra locations
    random.shuffle(shuffle_clusters)
    random.shuffle(filler_spots)
    item_spot_data = []
    c, s, t = 0, 0, -1
    for region in Locations.item_cluster_locations:
        item_spot_data.append([])
        for cluster in region:
            if shuffle_clusters[c]:
                t = random.randrange(0, len(cluster))
            c += 1
            for i, spot_data in enumerate(cluster):
                if i == t:
                    item_spot_data[-1].append(spot_data)
                    t = -1
                else:
                    if filler_spots[s]:
                        item_spot_data[-1].append(spot_data)
                    s += 1

    # Construct Course Regions and Locations
    for (course_name, locs), spot_data_clusters in zip(Locations.course_locations.items(), item_spot_data):
        course_regions.append(Region(course_name, player, multiworld))
        for loc_name, (code, group) in locs.items():
            if group & location_group_mask:
                add_location(player, loc_name, code, course_regions[-1])
        for spot in spot_data_clusters:
            spot_location = add_location(player, spot.name, spot.code, course_regions[-1])
            if spot.access is not None:
                spot_location.access_rule = lambda state, access=spot.access: state.has_any(access, player)

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
            while order[0] in {5, 13}:  # Prevent Frappe Snowland and Yoshi Valley from coming first
                random.shuffle(order)
            if opt.final_pool:
                order.append(tuple(Locations.course_locations).index(random.choice(opt.final_pool)))
                order.remove(order[-1])
    course_regions = [course_regions[i] for i in order]

    # Create Course & Cup Connections
    if opt.mode == GameMode.option_cups:
        entrance_names = ["Mushroom Cup 1", "Mushroom Cup 2", "Mushroom Cup 3", "Mushroom Cup 4",
                          "Flower Cup 1",   "Flower Cup 2",   "Flower Cup 3",   "Flower Cup 4",
                          "Star Cup 1",     "Star Cup 2",     "Star Cup 3",     "Star Cup 4",
                          "Special Cup 1",  "Special Cup 2",  "Special Cup 3",  "Special Cup 4"]
        for c in range(16):
            if c % 4:
                course_regions[c-1].connect(
                    course_regions[c],
                    entrance_names[c],
                    lambda state, qualify_rule=course_qualify_rules[order[c-1]]: qualify_rule(state, player, opt.logic))
            else:
                menu_region.connect(course_regions[c], entrance_names[c],
                                    lambda state, count=c//4: state.has("Progressive Cup Unlock", player, count))
                course_regions[c+3].connect(cup_regions[c//4], entrance_names[c][:-1] + "Finish")
    else:  # GameMode.option_courses
        for i in range(16):
            locks = max(0, i + opt.locked_courses - 15)
            rule = (lambda state, k=locks: state.has("Progressive Course Unlock", player, k)) if locks > 0 else None
            menu_region.connect(course_regions[i], f"Course {i + 1}", rule)

    # Register regions (and locations)
    multiworld.regions += [menu_region] + course_regions + shared_hazard_regions + cup_regions

    # Write course order to spoiler log
    for i in range(16):
        entrance = course_regions[i].entrances[0]
        multiworld.spoiler.set_entrance(entrance.name, entrance.connected_region.name, "entrance", player)

    # Place Victory Event Location
    if opt.mode == GameMode.option_cups:
        cup_regions[-1].locations[-1].address = None
        cup_regions[-1].locations[-1].event = True
        victory_event_location = cup_regions[-1].locations[-1]
    else:
        course_regions[15].locations[2].address = None
        course_regions[15].locations[2].event = True
        victory_event_location = course_regions[15].locations[2]

    return victory_event_location, order
