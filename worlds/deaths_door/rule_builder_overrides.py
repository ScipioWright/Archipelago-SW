import dataclasses
from typing import TYPE_CHECKING, Any, Iterable
from typing_extensions import override
from .items import ItemGroup as IG, DeathsDoorItemName as I
from .locations import DeathsDoorLocationName as L
from .events import DeathsDoorEventName as E
from .regions import DeathsDoorRegionName as R

try:
    from rule_builder import (
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
    )
except ModuleNotFoundError:
    from .rule_builder import (
        OptionFilter,
        Has as RBHas,
        HasAll as RBHasAll,
        HasAny as RBHasAny,
        HasGroup as RBHasGroup,
        CanReachLocation as RBCanReachLocation,
        CanReachRegion as RBCanReachRegion,
    )
    
# Override Has, etc. to take DeathsDoorItemName enum instead of string
@dataclasses.dataclass()
class Has(RBHas, game="Death's Door"):

    @override
    def __init__(
        self, item_name: I | E, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name.value, count=count, options=options)


@dataclasses.dataclass()
class HasAny(RBHasAny, game="Death's Door"):

    @override
    def __init__(
        self, *item_names: I | E, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasAll(RBHasAll, game="Death's Door"):

    @override
    def __init__(
        self, *item_names: I | E, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(
            *tuple(item_name.value for item_name in item_names), options=options
        )


@dataclasses.dataclass()
class HasGroup(RBHasGroup, game="Death's Door"):

    @override
    def __init__(
        self, item_name_group: IG, count=1, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(item_name_group.value, count=count, options=options)

@dataclasses.dataclass()
class CanReachLocation(RBCanReachLocation, game="Death's Door"):

    @override
    def __init__(
        self, location_name: L, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(location_name.value, options=options)

@dataclasses.dataclass()
class CanReachRegion(RBCanReachRegion, game="Death's Door"):

    @override
    def __init__(
        self, region_name: R, options: "Iterable[OptionFilter[Any]]" = ()
    ) -> None:
        super().__init__(region_name.value, options=options)