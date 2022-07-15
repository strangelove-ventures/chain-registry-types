# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = assetlist_from_dict(json.loads(json_string))

from typing import Optional, List, Any, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class DenomUnitElement:
    aliases: Optional[List[str]]
    denom: str
    exponent: int

    def __init__(self, aliases: Optional[List[str]], denom: str, exponent: int) -> None:
        self.aliases = aliases
        self.denom = denom
        self.exponent = exponent

    @staticmethod
    def from_dict(obj: Any) -> 'DenomUnitElement':
        assert isinstance(obj, dict)
        aliases = from_union([lambda x: from_list(from_str, x), from_none], obj.get("aliases"))
        denom = from_str(obj.get("denom"))
        exponent = from_int(obj.get("exponent"))
        return DenomUnitElement(aliases, denom, exponent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["aliases"] = from_union([lambda x: from_list(from_str, x), from_none], self.aliases)
        result["denom"] = from_str(self.denom)
        result["exponent"] = from_int(self.exponent)
        return result


class Ibc:
    """[OPTIONAL] IBC Channel between src and dst between chain"""
    dst_channel: str
    source_channel: str
    source_denom: str

    def __init__(self, dst_channel: str, source_channel: str, source_denom: str) -> None:
        self.dst_channel = dst_channel
        self.source_channel = source_channel
        self.source_denom = source_denom

    @staticmethod
    def from_dict(obj: Any) -> 'Ibc':
        assert isinstance(obj, dict)
        dst_channel = from_str(obj.get("dst_channel"))
        source_channel = from_str(obj.get("source_channel"))
        source_denom = from_str(obj.get("source_denom"))
        return Ibc(dst_channel, source_channel, source_denom)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dst_channel"] = from_str(self.dst_channel)
        result["source_channel"] = from_str(self.source_channel)
        result["source_denom"] = from_str(self.source_denom)
        return result


class LogoURIs:
    png: Optional[str]
    svg: Optional[str]

    def __init__(self, png: Optional[str], svg: Optional[str]) -> None:
        self.png = png
        self.svg = svg

    @staticmethod
    def from_dict(obj: Any) -> 'LogoURIs':
        assert isinstance(obj, dict)
        png = from_union([from_none, from_str], obj.get("png"))
        svg = from_union([from_none, from_str], obj.get("svg"))
        return LogoURIs(png, svg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["png"] = from_union([from_none, from_str], self.png)
        result["svg"] = from_union([from_none, from_str], self.svg)
        return result


class TypeAsset(Enum):
    """[OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin"""
    CW20 = "cw20"
    ERC20 = "erc20"
    SDK_COIN = "sdk.coin"
    SNIP20 = "snip20"


class AssetElement:
    """[OPTIONAL] The address of the asset. Only required for type_asset : cw20, snip20"""
    address: Optional[str]
    """The base unit of the asset. Must be in denom_units."""
    base: str
    """[OPTIONAL] The coingecko id to fetch asset data from coingecko v3 api. See
    https://api.coingecko.com/api/v3/coins/list
    """
    coingecko_id: Optional[str]
    denom_units: List[DenomUnitElement]
    """[OPTIONAL] A short description of the asset"""
    description: Optional[str]
    """The human friendly unit of the asset. Must be in denom_units."""
    display: str
    """[OPTIONAL] IBC Channel between src and dst between chain"""
    ibc: Optional[Ibc]
    logo_ur_is: Optional[LogoURIs]
    """The project name of the asset. For example Bitcoin."""
    name: str
    """The symbol of an asset. For example BTC."""
    symbol: str
    """[OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin"""
    type_asset: Optional[TypeAsset]

    def __init__(self, address: Optional[str], base: str, coingecko_id: Optional[str], denom_units: List[DenomUnitElement], description: Optional[str], display: str, ibc: Optional[Ibc], logo_ur_is: Optional[LogoURIs], name: str, symbol: str, type_asset: Optional[TypeAsset]) -> None:
        self.address = address
        self.base = base
        self.coingecko_id = coingecko_id
        self.denom_units = denom_units
        self.description = description
        self.display = display
        self.ibc = ibc
        self.logo_ur_is = logo_ur_is
        self.name = name
        self.symbol = symbol
        self.type_asset = type_asset

    @staticmethod
    def from_dict(obj: Any) -> 'AssetElement':
        assert isinstance(obj, dict)
        address = from_union([from_none, from_str], obj.get("address"))
        base = from_str(obj.get("base"))
        coingecko_id = from_union([from_none, from_str], obj.get("coingecko_id"))
        denom_units = from_list(DenomUnitElement.from_dict, obj.get("denom_units"))
        description = from_union([from_none, from_str], obj.get("description"))
        display = from_str(obj.get("display"))
        ibc = from_union([Ibc.from_dict, from_none], obj.get("ibc"))
        logo_ur_is = from_union([LogoURIs.from_dict, from_none], obj.get("logo_URIs"))
        name = from_str(obj.get("name"))
        symbol = from_str(obj.get("symbol"))
        type_asset = from_union([TypeAsset, from_none], obj.get("type_asset"))
        return AssetElement(address, base, coingecko_id, denom_units, description, display, ibc, logo_ur_is, name, symbol, type_asset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([from_none, from_str], self.address)
        result["base"] = from_str(self.base)
        result["coingecko_id"] = from_union([from_none, from_str], self.coingecko_id)
        result["denom_units"] = from_list(lambda x: to_class(DenomUnitElement, x), self.denom_units)
        result["description"] = from_union([from_none, from_str], self.description)
        result["display"] = from_str(self.display)
        result["ibc"] = from_union([lambda x: to_class(Ibc, x), from_none], self.ibc)
        result["logo_URIs"] = from_union([lambda x: to_class(LogoURIs, x), from_none], self.logo_ur_is)
        result["name"] = from_str(self.name)
        result["symbol"] = from_str(self.symbol)
        result["type_asset"] = from_union([lambda x: to_enum(TypeAsset, x), from_none], self.type_asset)
        return result


class Assetlist:
    """Asset lists are a similar mechanism to allow frontends and other UIs to fetch metadata
    associated with Cosmos SDK denoms, especially for assets sent over IBC.
    """
    assets: List[AssetElement]
    chain_name: str

    def __init__(self, assets: List[AssetElement], chain_name: str) -> None:
        self.assets = assets
        self.chain_name = chain_name

    @staticmethod
    def from_dict(obj: Any) -> 'Assetlist':
        assert isinstance(obj, dict)
        assets = from_list(AssetElement.from_dict, obj.get("assets"))
        chain_name = from_str(obj.get("chain_name"))
        return Assetlist(assets, chain_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["assets"] = from_list(lambda x: to_class(AssetElement, x), self.assets)
        result["chain_name"] = from_str(self.chain_name)
        return result


def assetlist_from_dict(s: Any) -> Assetlist:
    return Assetlist.from_dict(s)


def assetlist_to_dict(x: Assetlist) -> Any:
    return to_class(Assetlist, x)
