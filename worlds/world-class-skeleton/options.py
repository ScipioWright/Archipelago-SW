from dataclasses import dataclass
from typing import Dict, Any
from Options import (DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, TextChoice, PlandoConnections,
                     PerGameCommonOptions, OptionGroup, Visibility)


class TestOption(DefaultOnToggle):
    """
    Enables the test option.
    """
    # internal_name is a potential convenience, nothing more
    internal_name = "test_option"
    display_name = "Test Option"


class TestOption2(Choice):
    """
    A choice between multiple options.
    """
    internal_name = "test_option_2"
    display_name = "Test Option 2"
    option_off = 0
    option_first = 1
    option_second = 2
    option_third = 3
    default = 1


class TestOption3(Range):
    """
    A range of options. Will have a slider on webhost.
    """
    internal_name = "test_option_3"
    display_name = "Test Option 3"
    range_start = 15
    range_end = 50
    default = 20


@dataclass
class GameNameOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    test_option: TestOption
    test_option_2: TestOption2
    test_option_3: TestOption3
      

game_name_option_groups = [
    OptionGroup("Test Group Options", [
        TestOption2,
        TestOption3,
    ])
]

game_name_option_presets: Dict[str, Dict[str, Any]] = {
    "Preset 1": {
        TestOption2.internal_name: 3,
    },
}
