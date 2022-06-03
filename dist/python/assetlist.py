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
    description: str
    type: str

    def __init__(self, description: str, type: str) -> None:
        self.description = description
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Address':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        return Address(description, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
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
    items: Items
    type: str

    def __init__(self, items: Items, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Assets':
        assert isinstance(obj, dict)
        items = Items.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return Assets(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(Items, self.items)
        result["type"] = from_str(self.type)
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
    dst_channel: ChainName
    source_channel: ChainName
    source_denom: ChainName

    def __init__(self, dst_channel: ChainName, source_channel: ChainName, source_denom: ChainName) -> None:
        self.dst_channel = dst_channel
        self.source_channel = source_channel
        self.source_denom = source_denom

    @staticmethod
    def from_dict(obj: Any) -> 'IbcProperties':
        assert isinstance(obj, dict)
        dst_channel = ChainName.from_dict(obj.get("dst_channel"))
        source_channel = ChainName.from_dict(obj.get("source_channel"))
        source_denom = ChainName.from_dict(obj.get("source_denom"))
        return IbcProperties(dst_channel, source_channel, source_denom)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dst_channel"] = to_class(ChainName, self.dst_channel)
        result["source_channel"] = to_class(ChainName, self.source_channel)
        result["source_denom"] = to_class(ChainName, self.source_denom)
        return result


class Ibc:
    description: str
    properties: IbcProperties
    required: List[str]
    type: str

    def __init__(self, description: str, properties: IbcProperties, required: List[str], type: str) -> None:
        self.description = description
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Ibc':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        properties = IbcProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return Ibc(description, properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["properties"] = to_class(IbcProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class PNG:
    format: str
    type: str

    def __init__(self, format: str, type: str) -> None:
        self.format = format
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'PNG':
        assert isinstance(obj, dict)
        format = from_str(obj.get("format"))
        type = from_str(obj.get("type"))
        return PNG(format, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_str(self.format)
        result["type"] = from_str(self.type)
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
    properties: LogoURIsProperties
    type: str

    def __init__(self, properties: LogoURIsProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'LogoURIs':
        assert isinstance(obj, dict)
        properties = LogoURIsProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return LogoURIs(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(LogoURIsProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class FluffyTypeAsset:
    default: str
    description: str
    enum: List[str]
    type: str

    def __init__(self, default: str, description: str, enum: List[str], type: str) -> None:
        self.default = default
        self.description = description
        self.enum = enum
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyTypeAsset':
        assert isinstance(obj, dict)
        default = from_str(obj.get("default"))
        description = from_str(obj.get("description"))
        enum = from_list(from_str, obj.get("enum"))
        type = from_str(obj.get("type"))
        return FluffyTypeAsset(default, description, enum, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["default"] = from_str(self.default)
        result["description"] = from_str(self.description)
        result["enum"] = from_list(from_str, self.enum)
        result["type"] = from_str(self.type)
        return result


class AssetProperties:
    address: Address
    base: Address
    coingecko_id: Address
    denom_units: Assets
    description: Address
    display: Address
    ibc: Ibc
    logo_ur_is: LogoURIs
    name: Address
    symbol: Address
    type_asset: FluffyTypeAsset

    def __init__(self, address: Address, base: Address, coingecko_id: Address, denom_units: Assets, description: Address, display: Address, ibc: Ibc, logo_ur_is: LogoURIs, name: Address, symbol: Address, type_asset: FluffyTypeAsset) -> None:
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
    def from_dict(obj: Any) -> 'AssetProperties':
        assert isinstance(obj, dict)
        address = Address.from_dict(obj.get("address"))
        base = Address.from_dict(obj.get("base"))
        coingecko_id = Address.from_dict(obj.get("coingecko_id"))
        denom_units = Assets.from_dict(obj.get("denom_units"))
        description = Address.from_dict(obj.get("description"))
        display = Address.from_dict(obj.get("display"))
        ibc = Ibc.from_dict(obj.get("ibc"))
        logo_ur_is = LogoURIs.from_dict(obj.get("logo_URIs"))
        name = Address.from_dict(obj.get("name"))
        symbol = Address.from_dict(obj.get("symbol"))
        type_asset = FluffyTypeAsset.from_dict(obj.get("type_asset"))
        return AssetProperties(address, base, coingecko_id, denom_units, description, display, ibc, logo_ur_is, name, symbol, type_asset)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = to_class(Address, self.address)
        result["base"] = to_class(Address, self.base)
        result["coingecko_id"] = to_class(Address, self.coingecko_id)
        result["denom_units"] = to_class(Assets, self.denom_units)
        result["description"] = to_class(Address, self.description)
        result["display"] = to_class(Address, self.display)
        result["ibc"] = to_class(Ibc, self.ibc)
        result["logo_URIs"] = to_class(LogoURIs, self.logo_ur_is)
        result["name"] = to_class(Address, self.name)
        result["symbol"] = to_class(Address, self.symbol)
        result["type_asset"] = to_class(FluffyTypeAsset, self.type_asset)
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
    asset_if: If
    properties: AssetProperties
    required: List[str]
    then: Then
    type: str

    def __init__(self, asset_if: If, properties: AssetProperties, required: List[str], then: Then, type: str) -> None:
        self.asset_if = asset_if
        self.properties = properties
        self.required = required
        self.then = then
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Asset':
        assert isinstance(obj, dict)
        asset_if = If.from_dict(obj.get("if"))
        properties = AssetProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        then = Then.from_dict(obj.get("then"))
        type = from_str(obj.get("type"))
        return Asset(asset_if, properties, required, then, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["if"] = to_class(If, self.asset_if)
        result["properties"] = to_class(AssetProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["then"] = to_class(Then, self.then)
        result["type"] = from_str(self.type)
        return result


class Aliases:
    items: ChainName
    type: str

    def __init__(self, items: ChainName, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Aliases':
        assert isinstance(obj, dict)
        items = ChainName.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return Aliases(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(ChainName, self.items)
        result["type"] = from_str(self.type)
        return result


class DenomUnitProperties:
    aliases: Aliases
    denom: ChainName
    exponent: ChainName

    def __init__(self, aliases: Aliases, denom: ChainName, exponent: ChainName) -> None:
        self.aliases = aliases
        self.denom = denom
        self.exponent = exponent

    @staticmethod
    def from_dict(obj: Any) -> 'DenomUnitProperties':
        assert isinstance(obj, dict)
        aliases = Aliases.from_dict(obj.get("aliases"))
        denom = ChainName.from_dict(obj.get("denom"))
        exponent = ChainName.from_dict(obj.get("exponent"))
        return DenomUnitProperties(aliases, denom, exponent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["aliases"] = to_class(Aliases, self.aliases)
        result["denom"] = to_class(ChainName, self.denom)
        result["exponent"] = to_class(ChainName, self.exponent)
        return result


class DenomUnit:
    properties: DenomUnitProperties
    required: List[str]
    type: str

    def __init__(self, properties: DenomUnitProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'DenomUnit':
        assert isinstance(obj, dict)
        properties = DenomUnitProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return DenomUnit(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(DenomUnitProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
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
    assets: Assets
    chain_name: ChainName

    def __init__(self, assets: Assets, chain_name: ChainName) -> None:
        self.assets = assets
        self.chain_name = chain_name

    @staticmethod
    def from_dict(obj: Any) -> 'AssetlistProperties':
        assert isinstance(obj, dict)
        assets = Assets.from_dict(obj.get("assets"))
        chain_name = ChainName.from_dict(obj.get("chain_name"))
        return AssetlistProperties(assets, chain_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["assets"] = to_class(Assets, self.assets)
        result["chain_name"] = to_class(ChainName, self.chain_name)
        return result


class Assetlist:
    defs: Defs
    description: str
    id: str
    properties: AssetlistProperties
    required: List[str]
    schema: str
    title: str
    type: str

    def __init__(self, defs: Defs, description: str, id: str, properties: AssetlistProperties, required: List[str], schema: str, title: str, type: str) -> None:
        self.defs = defs
        self.description = description
        self.id = id
        self.properties = properties
        self.required = required
        self.schema = schema
        self.title = title
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Assetlist':
        assert isinstance(obj, dict)
        defs = Defs.from_dict(obj.get("$defs"))
        description = from_str(obj.get("description"))
        id = from_str(obj.get("$id"))
        properties = AssetlistProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        schema = from_str(obj.get("$schema"))
        title = from_str(obj.get("title"))
        type = from_str(obj.get("type"))
        return Assetlist(defs, description, id, properties, required, schema, title, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$defs"] = to_class(Defs, self.defs)
        result["description"] = from_str(self.description)
        result["$id"] = from_str(self.id)
        result["properties"] = to_class(AssetlistProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["$schema"] = from_str(self.schema)
        result["title"] = from_str(self.title)
        result["type"] = from_str(self.type)
        return result


def assetlist_from_dict(s: Any) -> Assetlist:
    return Assetlist.from_dict(s)


def assetlist_to_dict(x: Assetlist) -> Any:
    return to_class(Assetlist, x)
