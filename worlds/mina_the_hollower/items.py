from BaseClasses import Item, Location, ItemClassification, CollectionRule, Region
from rule_builder.rules import True_, Rule
from .world_base import MinaTheHollowerBase
from .constants import MINA_THE_HOLLOWER
from .data import ItemData, ItemTypeEnum, ItemFiller
from .data.items import Kear, SingleKears, AreaKears, base_items, Abilities, BoneUps, GenericBoneUp, all_filler_items, \
    PermanentUpgrades, Sidearms, PlayerUpgrades, AstralPlatforms, upgrade_items, Trinkets, BASE_ITEM_TOTAL, \
    trinket_powers, upgrade_powers, valid_power_types
from .data.rules.ability_rules import CanJumpTiles
from .data.rules.state_rules import sidearm_rules
from .options import BoneUpCap, KearRandomization

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MinaTheHollowerWorld


class MinaTheHollowerItem(Item):
    game: str = MINA_THE_HOLLOWER


def create_item(world: "MinaTheHollowerWorld", item: ItemData):
    for i in range(item.amount):
        world.itempool.append(world.create_item(item.type.value))


def create_single_item(world: "MinaTheHollowerWorld", item_type: ItemTypeEnum):
    world.itempool.append(world.create_item(item_type.value))


def create_items(world: "MinaTheHollowerWorld"):
    is_ut = world.using_ut
    all_items: list[ItemData] = []
    trinket_types = set(Trinkets)
    bone_cap_types = {*BoneUps, GenericBoneUp.ALL_BONE_UP_CAP}
    bone_cap_cap = 6 if world.options.bone_up_cap == BoneUpCap.option_perUpgrade else 2
    trinkets_selected = 0
    bags_selected = 0
    bone_caps_selected = 0

    for item in upgrade_items:
        for _ in range(item.amount):
            all_items.append(ItemData(item.type, 1))

    for item_type in PermanentUpgrades:
        all_items.append(ItemData(item_type, 1))
    for item_type in Trinkets:
        all_items.append(ItemData(item_type, 1))
    for item_type in PlayerUpgrades:
        all_items.append(ItemData(item_type, 1))

    # dont want to start
    if world.options.bone_up_cap == BoneUpCap.option_perUpgrade:
        for item_type in BoneUps:
            for _ in range(9):
                all_items.append(ItemData(item_type, 1))
    else:
        for _ in range(9):
            all_items.append(ItemData(GenericBoneUp.ALL_BONE_UP_CAP, 1))

    starting_items: list[Item] = [] if not is_ut else world.starting_items
    # starting items
    if world.options.random_starting_items:
        for item in base_items:
            for _ in range(item.amount):
                all_items.append(ItemData(item.type, 1))
        if is_ut:
            for item in starting_items:
                item_data = next(
                    (x for x in all_items if x.type.item_id == item.code),
                    None
                )

                if item_data is None:
                    continue

                item_data.amount -= 1

                if item_data.amount <= 0:
                    all_items.remove(item_data)
        else:
            for i in range(BASE_ITEM_TOTAL):
                if i < (BASE_ITEM_TOTAL * 2) // 3:
                    candidates = [
                        item
                        for item in all_items
                        if item.type in valid_power_types
                    ]
                    if bags_selected < 2:
                        candidates += [
                            item
                            for item in all_items
                            if item.type == PlayerUpgrades.TRINKET_BAG
                        ]
                else:
                    candidates = list(all_items)

                if (trinkets_selected > bags_selected):
                    filtered = [
                        item
                        for item in candidates
                        if item.type not in trinket_types
                    ]
                    if filtered:
                        candidates = filtered

                if (bone_caps_selected >= bone_cap_cap):
                    filtered = [
                        item
                        for item in candidates
                        if item.type not in bone_cap_types
                    ]
                    if filtered:
                        candidates = filtered

                item_data = world.random.choice(candidates)

                starting_items.append(world.create_item(item_data.type.value))

                if item_data.type == PlayerUpgrades.TRINKET_BAG:
                    bags_selected += 1
                elif item_data.type in trinket_types:
                    trinkets_selected += 1
                elif item_data.type in bone_cap_types:
                    bone_caps_selected += 1

                item_data.amount -= 1

                if item_data.type.value == PlayerUpgrades.TRINKET_BAG.value:
                    added_trinket_pouch = True

                if item_data.amount <= 0:
                    all_items.remove(item_data)

    else:
        for item in base_items:
            for i in range(item.amount):
                starting_items.append(world.create_item(item.type.value))

    for item_type in Abilities:
        if item_type.value in world.options.ability_rando.value:
            create_single_item(world, item_type)
        else:
            starting_items.append(world.create_item(item_type.value))

    for item in all_items:
        create_item(world, item)

    if world.options.kear_rando == KearRandomization.option_vanilla:
        create_item(world, ItemData(Kear.UNIVERSAL_KEAR, 50))
    elif world.options.kear_rando == KearRandomization.option_apItems:
        for item_type in SingleKears:
            create_single_item(world, item_type)
    elif world.options.kear_rando.value == 2:  # todo: change to KearRandomization.option_areaApItems
        for item_type in AreaKears:
            create_single_item(world, item_type)

    total_location_count = len(world.multiworld.get_unfilled_locations(world.player))
    # print(f"total locs at start {total_location_count}")
    # print(f"total Itempool at start {len(world.itempool)}")
    remaining = total_location_count - len(world.itempool)

    filler: list[ItemFiller] = world.random.choices(
        all_filler_items,
        weights=[item.weight for item in all_filler_items],
        k=remaining
    )
    for item_filler in filler:
        create_single_item(world, item_filler.type)

    world.multiworld.itempool += world.itempool

    return starting_items


def create_event(world: "MinaTheHollowerWorld", region_name: str, item_name: str, loc_name: str | None = None,
                 rule: CollectionRule | Rule[MinaTheHollowerBase] = True_()) -> None:
    if loc_name is None:
        loc_name = "Event " + item_name
    region = world.get_region(region_name)
    event_loc = Location(world.player, loc_name, None, region)
    world.set_rule(event_loc, rule)
    event_loc.place_locked_item(
        MinaTheHollowerItem(item_name, ItemClassification.progression, None, world.player))
    region.locations.append(event_loc)


def create_events(world: "MinaTheHollowerWorld"):

    region_gen = {
        "Astral Orrery": "Starry",
        "Queensbury Crypt": "Solemn",
        "Coltrane Peak": "Frozen",
        "Septemburg": "Windy",
        "Bone Beach": "Shoreline",
        "Nox's Bayou": "Swampy"
    }
    starting_region = "Ossex City Center Main" if world.options.ossex_start else "Loner's Landing Shipwreck"

    for itemShortcut in sidearm_rules:
        create_event(world, starting_region, itemShortcut.type.value, rule=itemShortcut.access_rule)
        # starting_items.append(Item(item_type.value, item_type.classification, item_type.item_id, world.player))

    for area, name in region_gen.items():

        # if area in world.options.excluded_areas.value:
        #     region = starting_region
        # else:
        create_event(world, region_name=area + " " + name + " Generator",
                     item_name="Repair " + name + " Generator", loc_name="Repair " + area + "Generator")

    create_event(world, region_name="Astral Orrery Queensbury Mirror",
                 item_name=AstralPlatforms.BLUE_ASTRAL_PLATFORMS.value, loc_name="Blue Switch")

    create_event(world, region_name="Astral Orrery Bayou Mirror",
                 item_name=AstralPlatforms.GREEN_ASTRAL_PLATFORMS.value, loc_name="Green Switch")

    create_event(world, region_name="Astral Orrery Bone Beach Mirror",
                 item_name=AstralPlatforms.RED_ASTRAL_PLATFORMS.value, loc_name="Red Switch")

    create_event(world, region_name="Astral Orrery Septemburg Mirror",
                 item_name=AstralPlatforms.YELLOW_ASTRAL_PLATFORMS.value, loc_name="Yellow Switch")

    create_event(world, region_name="Astral Orrery Coltrane Peak Mirror",
                 item_name=AstralPlatforms.PURPLE_ASTRAL_PLATFORMS.value, loc_name="Purple Switch")

    create_event(world, region_name="Radiant Manor Prime Generator",
                 item_name="Victory", loc_name="Defeat Giga Lionel")
