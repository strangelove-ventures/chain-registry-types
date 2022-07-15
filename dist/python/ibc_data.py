# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ibc_data_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, Any, Dict, List, TypeVar, Type, Callable, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Ordering(Enum):
    """Determines if packets from a sending module must be 'ordered' or 'unordered'."""
    ORDERED = "ordered"
    UNORDERED = "unordered"


class Status(Enum):
    KILLED = "killed"
    LIVE = "live"
    UPCOMING = "upcoming"


class Tags:
    """Human readable key:value pairs that help describe and distinguish channels."""
    dex: Optional[str]
    preferred: Optional[bool]
    """String that helps describe non-dex use cases ex: interchain accounts(ICA)."""
    properties: Optional[str]
    status: Optional[Status]

    def __init__(self, dex: Optional[str], preferred: Optional[bool], properties: Optional[str], status: Optional[Status]) -> None:
        self.dex = dex
        self.preferred = preferred
        self.properties = properties
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        assert isinstance(obj, dict)
        dex = from_union([from_none, from_str], obj.get("dex"))
        preferred = from_union([from_bool, from_none], obj.get("preferred"))
        properties = from_union([from_none, from_str], obj.get("properties"))
        status = from_union([Status, from_none], obj.get("status"))
        return Tags(dex, preferred, properties, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dex"] = from_union([from_none, from_str], self.dex)
        result["preferred"] = from_union([from_bool, from_none], self.preferred)
        result["properties"] = from_union([from_none, from_str], self.properties)
        result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        return result


class Channel:
    chain_1: Dict[str, Any]
    chain_2: Dict[str, Any]
    """Human readable description of the channel."""
    description: Optional[str]
    """Determines if packets from a sending module must be 'ordered' or 'unordered'."""
    ordering: Ordering
    """Human readable key:value pairs that help describe and distinguish channels."""
    tags: Optional[Tags]
    """IBC Version"""
    version: str

    def __init__(self, chain_1: Dict[str, Any], chain_2: Dict[str, Any], description: Optional[str], ordering: Ordering, tags: Optional[Tags], version: str) -> None:
        self.chain_1 = chain_1
        self.chain_2 = chain_2
        self.description = description
        self.ordering = ordering
        self.tags = tags
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        chain_1 = from_dict(lambda x: x, obj.get("chain-1"))
        chain_2 = from_dict(lambda x: x, obj.get("chain-2"))
        description = from_union([from_none, from_str], obj.get("description"))
        ordering = Ordering(obj.get("ordering"))
        tags = from_union([Tags.from_dict, from_none], obj.get("tags"))
        version = from_str(obj.get("version"))
        return Channel(chain_1, chain_2, description, ordering, tags, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-1"] = from_dict(lambda x: x, self.chain_1)
        result["chain-2"] = from_dict(lambda x: x, self.chain_2)
        result["description"] = from_union([from_none, from_str], self.description)
        result["ordering"] = to_enum(Ordering, self.ordering)
        result["tags"] = from_union([lambda x: to_class(Tags, x), from_none], self.tags)
        result["version"] = from_str(self.version)
        return result


class IbcData:
    """Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
    alphabetical order.
    """
    chain_1: Dict[str, Any]
    """Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
    alphabetical order.
    """
    chain_2: Dict[str, Any]
    channels: List[Channel]
    defs: Any

    def __init__(self, chain_1: Dict[str, Any], chain_2: Dict[str, Any], channels: List[Channel], defs: Any) -> None:
        self.chain_1 = chain_1
        self.chain_2 = chain_2
        self.channels = channels
        self.defs = defs

    @staticmethod
    def from_dict(obj: Any) -> 'IbcData':
        assert isinstance(obj, dict)
        chain_1 = from_dict(lambda x: x, obj.get("chain-1"))
        chain_2 = from_dict(lambda x: x, obj.get("chain-2"))
        channels = from_list(Channel.from_dict, obj.get("channels"))
        defs = obj.get("$defs")
        return IbcData(chain_1, chain_2, channels, defs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-1"] = from_dict(lambda x: x, self.chain_1)
        result["chain-2"] = from_dict(lambda x: x, self.chain_2)
        result["channels"] = from_list(lambda x: to_class(Channel, x), self.channels)
        result["$defs"] = self.defs
        return result


def ibc_data_from_dict(s: Any) -> IbcData:
    return IbcData.from_dict(s)


def ibc_data_to_dict(x: IbcData) -> Any:
    return to_class(IbcData, x)
