# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = assetlist_from_dict(json.loads(json_string))

from typing import List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class PurpleTypeAsset:
    enum: List[str]

    def __init__(self, enum: List[str]) -> None:
        self.enum = enum

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleTypeAsset':
        assert isinstance(obj, dict)
        enum = from_list(from_str, obj.get("enum"))
        return PurpleTypeAsset(enum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_str, self.enum)
        return result


class IfProperties:
    type_asset: PurpleTypeAsset

    def __init__(self, type_asset: PurpleTypeAsset) -> None:
        self.type_asset = type_asset

    @staticmethod
    def from_dict(obj: Any) -> 'IfProperties':
        assert isinstance(obj, dict)
        type_asset = PurpleTypeAsset.from_dict(obj.get("type_asset"))
        return IfProperties(type_asset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type_asset"] = to_class(PurpleTypeAsset, self.type_asset)
        return result


class If:
    properties: IfProperties
    required: List[str]

    def __init__(self, properties: IfProperties, required: List[str]) -> None:
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'If':
        assert isinstance(obj, dict)
        properties = IfProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        return If(properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(IfProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        return result


class Address:
    type: str
    description: str

    def __init__(self, type: str, description: str) -> None:
        self.type = type
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        return Address(type, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        return result


class Items:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref

    @staticmethod
    def from_dict(obj: Any) -> 'Items':
        assert isinstance(obj, dict)
        ref = from_str(obj.get("$ref"))
        return Items(ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$ref"] = from_str(self.ref)
        return result


class Assets:
    type: str
    items: Items

    def __init__(self, type: str, items: Items) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Assets':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = Items.from_dict(obj.get("items"))
        return Assets(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(Items, self.items)
        return result


class ChainName:
    type: str

    def __init__(self, type: str) -> None:
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ChainName':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        return ChainName(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        return result


class IbcProperties:
    source_channel: ChainName
    dst_channel: ChainName
    source_denom: ChainName

    def __init__(self, source_channel: ChainName, dst_channel: ChainName, source_denom: ChainName) -> None:
        self.source_channel = source_channel
        self.dst_channel = dst_channel
        self.source_denom = source_denom

    @staticmethod
    def from_dict(obj: Any) -> 'IbcProperties':
        assert isinstance(obj, dict)
        source_channel = ChainName.from_dict(obj.get("source_channel"))
        dst_channel = ChainName.from_dict(obj.get("dst_channel"))
        source_denom = ChainName.from_dict(obj.get("source_denom"))
        return IbcProperties(source_channel, dst_channel, source_denom)

    def to_dict(self) -> dict:
        result: dict = {}
        result["source_channel"] = to_class(ChainName, self.source_channel)
        result["dst_channel"] = to_class(ChainName, self.dst_channel)
        result["source_denom"] = to_class(ChainName, self.source_denom)
        return result


class Ibc:
    type: str
    description: str
    properties: IbcProperties
    required: List[str]

    def __init__(self, type: str, description: str, properties: IbcProperties, required: List[str]) -> None:
        self.type = type
        self.description = description
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'Ibc':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = IbcProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        return Ibc(type, description, properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(IbcProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        return result


class PNG:
    type: str
    format: str

    def __init__(self, type: str, format: str) -> None:
        self.type = type
        self.format = format

    @staticmethod
    def from_dict(obj: Any) -> 'PNG':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        format = from_str(obj.get("format"))
        return PNG(type, format)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["format"] = from_str(self.format)
        return result


class LogoURIsProperties:
    png: PNG
    svg: PNG

    def __init__(self, png: PNG, svg: PNG) -> None:
        self.png = png
        self.svg = svg

    @staticmethod
    def from_dict(obj: Any) -> 'LogoURIsProperties':
        assert isinstance(obj, dict)
        png = PNG.from_dict(obj.get("png"))
        svg = PNG.from_dict(obj.get("svg"))
        return LogoURIsProperties(png, svg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["png"] = to_class(PNG, self.png)
        result["svg"] = to_class(PNG, self.svg)
        return result


class LogoURIs:
    type: str
    properties: LogoURIsProperties

    def __init__(self, type: str, properties: LogoURIsProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'LogoURIs':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = LogoURIsProperties.from_dict(obj.get("properties"))
        return LogoURIs(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(LogoURIsProperties, self.properties)
        return result


class FluffyTypeAsset:
    type: str
    enum: List[str]
    default: str
    description: str

    def __init__(self, type: str, enum: List[str], default: str, description: str) -> None:
        self.type = type
        self.enum = enum
        self.default = default
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyTypeAsset':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        enum = from_list(from_str, obj.get("enum"))
        default = from_str(obj.get("default"))
        description = from_str(obj.get("description"))
        return FluffyTypeAsset(type, enum, default, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["enum"] = from_list(from_str, self.enum)
        result["default"] = from_str(self.default)
        result["description"] = from_str(self.description)
        return result


class AssetProperties:
    description: Address
    denom_units: Assets
    type_asset: FluffyTypeAsset
    address: Address
    base: Address
    name: Address
    display: Address
    symbol: Address
    ibc: Ibc
    logo_ur_is: LogoURIs
    coingecko_id: Address

    def __init__(self, description: Address, denom_units: Assets, type_asset: FluffyTypeAsset, address: Address, base: Address, name: Address, display: Address, symbol: Address, ibc: Ibc, logo_ur_is: LogoURIs, coingecko_id: Address) -> None:
        self.description = description
        self.denom_units = denom_units
        self.type_asset = type_asset
        self.address = address
        self.base = base
        self.name = name
        self.display = display
        self.symbol = symbol
        self.ibc = ibc
        self.logo_ur_is = logo_ur_is
        self.coingecko_id = coingecko_id

    @staticmethod
    def from_dict(obj: Any) -> 'AssetProperties':
        assert isinstance(obj, dict)
        description = Address.from_dict(obj.get("description"))
        denom_units = Assets.from_dict(obj.get("denom_units"))
        type_asset = FluffyTypeAsset.from_dict(obj.get("type_asset"))
        address = Address.from_dict(obj.get("address"))
        base = Address.from_dict(obj.get("base"))
        name = Address.from_dict(obj.get("name"))
        display = Address.from_dict(obj.get("display"))
        symbol = Address.from_dict(obj.get("symbol"))
        ibc = Ibc.from_dict(obj.get("ibc"))
        logo_ur_is = LogoURIs.from_dict(obj.get("logo_URIs"))
        coingecko_id = Address.from_dict(obj.get("coingecko_id"))
        return AssetProperties(description, denom_units, type_asset, address, base, name, display, symbol, ibc, logo_ur_is, coingecko_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = to_class(Address, self.description)
        result["denom_units"] = to_class(Assets, self.denom_units)
        result["type_asset"] = to_class(FluffyTypeAsset, self.type_asset)
        result["address"] = to_class(Address, self.address)
        result["base"] = to_class(Address, self.base)
        result["name"] = to_class(Address, self.name)
        result["display"] = to_class(Address, self.display)
        result["symbol"] = to_class(Address, self.symbol)
        result["ibc"] = to_class(Ibc, self.ibc)
        result["logo_URIs"] = to_class(LogoURIs, self.logo_ur_is)
        result["coingecko_id"] = to_class(Address, self.coingecko_id)
        return result


class Then:
    required: List[str]

    def __init__(self, required: List[str]) -> None:
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'Then':
        assert isinstance(obj, dict)
        required = from_list(from_str, obj.get("required"))
        return Then(required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["required"] = from_list(from_str, self.required)
        return result


class Asset:
    type: str
    required: List[str]
    properties: AssetProperties
    asset_if: If
    then: Then

    def __init__(self, type: str, required: List[str], properties: AssetProperties, asset_if: If, then: Then) -> None:
        self.type = type
        self.required = required
        self.properties = properties
        self.asset_if = asset_if
        self.then = then

    @staticmethod
    def from_dict(obj: Any) -> 'Asset':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = AssetProperties.from_dict(obj.get("properties"))
        asset_if = If.from_dict(obj.get("if"))
        then = Then.from_dict(obj.get("then"))
        return Asset(type, required, properties, asset_if, then)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(AssetProperties, self.properties)
        result["if"] = to_class(If, self.asset_if)
        result["then"] = to_class(Then, self.then)
        return result


class Aliases:
    type: str
    items: ChainName

    def __init__(self, type: str, items: ChainName) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Aliases':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = ChainName.from_dict(obj.get("items"))
        return Aliases(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(ChainName, self.items)
        return result


class DenomUnitProperties:
    denom: ChainName
    exponent: ChainName
    aliases: Aliases

    def __init__(self, denom: ChainName, exponent: ChainName, aliases: Aliases) -> None:
        self.denom = denom
        self.exponent = exponent
        self.aliases = aliases

    @staticmethod
    def from_dict(obj: Any) -> 'DenomUnitProperties':
        assert isinstance(obj, dict)
        denom = ChainName.from_dict(obj.get("denom"))
        exponent = ChainName.from_dict(obj.get("exponent"))
        aliases = Aliases.from_dict(obj.get("aliases"))
        return DenomUnitProperties(denom, exponent, aliases)

    def to_dict(self) -> dict:
        result: dict = {}
        result["denom"] = to_class(ChainName, self.denom)
        result["exponent"] = to_class(ChainName, self.exponent)
        result["aliases"] = to_class(Aliases, self.aliases)
        return result


class DenomUnit:
    type: str
    properties: DenomUnitProperties
    required: List[str]

    def __init__(self, type: str, properties: DenomUnitProperties, required: List[str]) -> None:
        self.type = type
        self.properties = properties
        self.required = required

    @staticmethod
    def from_dict(obj: Any) -> 'DenomUnit':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = DenomUnitProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        return DenomUnit(type, properties, required)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(DenomUnitProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        return result


class Defs:
    asset: Asset
    denom_unit: DenomUnit

    def __init__(self, asset: Asset, denom_unit: DenomUnit) -> None:
        self.asset = asset
        self.denom_unit = denom_unit

    @staticmethod
    def from_dict(obj: Any) -> 'Defs':
        assert isinstance(obj, dict)
        asset = Asset.from_dict(obj.get("asset"))
        denom_unit = DenomUnit.from_dict(obj.get("denom_unit"))
        return Defs(asset, denom_unit)

    def to_dict(self) -> dict:
        result: dict = {}
        result["asset"] = to_class(Asset, self.asset)
        result["denom_unit"] = to_class(DenomUnit, self.denom_unit)
        return result


class AssetlistProperties:
    chain_name: ChainName
    assets: Assets

    def __init__(self, chain_name: ChainName, assets: Assets) -> None:
        self.chain_name = chain_name
        self.assets = assets

    @staticmethod
    def from_dict(obj: Any) -> 'AssetlistProperties':
        assert isinstance(obj, dict)
        chain_name = ChainName.from_dict(obj.get("chain_name"))
        assets = Assets.from_dict(obj.get("assets"))
        return AssetlistProperties(chain_name, assets)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain_name"] = to_class(ChainName, self.chain_name)
        result["assets"] = to_class(Assets, self.assets)
        return result


class Assetlist:
    id: str
    schema: str
    title: str
    description: str
    type: str
    required: List[str]
    properties: AssetlistProperties
    defs: Defs

    def __init__(self, id: str, schema: str, title: str, description: str, type: str, required: List[str], properties: AssetlistProperties, defs: Defs) -> None:
        self.id = id
        self.schema = schema
        self.title = title
        self.description = description
        self.type = type
        self.required = required
        self.properties = properties
        self.defs = defs

    @staticmethod
    def from_dict(obj: Any) -> 'Assetlist':
        assert isinstance(obj, dict)
        id = from_str(obj.get("$id"))
        schema = from_str(obj.get("$schema"))
        title = from_str(obj.get("title"))
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = AssetlistProperties.from_dict(obj.get("properties"))
        defs = Defs.from_dict(obj.get("$defs"))
        return Assetlist(id, schema, title, description, type, required, properties, defs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$id"] = from_str(self.id)
        result["$schema"] = from_str(self.schema)
        result["title"] = from_str(self.title)
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(AssetlistProperties, self.properties)
        result["$defs"] = to_class(Defs, self.defs)
        return result


def assetlist_from_dict(s: Any) -> Assetlist:
    return Assetlist.from_dict(s)


def assetlist_to_dict(x: Assetlist) -> Any:
    return to_class(Assetlist, x)
