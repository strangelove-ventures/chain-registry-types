# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = ibc_data_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


class Items:
    refs: str

    def __init__(self, refs: str) -> None:
        self.refs = refs

    @staticmethod
    def from_dict(obj: Any) -> 'Items':
        assert isinstance(obj, dict)
        refs = from_str(obj.get("$refs"))
        return Items(refs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$refs"] = from_str(self.refs)
        return result


class PurpleChain:
    type: str
    description: str
    items: Items

    def __init__(self, type: str, description: str, items: Items) -> None:
        self.type = type
        self.description = description
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleChain':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        items = Items.from_dict(obj.get("items"))
        return PurpleChain(type, description, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["items"] = to_class(Items, self.items)
        return result


class FluffyChain:
    type: str
    items: Items

    def __init__(self, type: str, items: Items) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyChain':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = Items.from_dict(obj.get("items"))
        return FluffyChain(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(Items, self.items)
        return result


class ClientID:
    type: str
    description: str

    def __init__(self, type: str, description: str) -> None:
        self.type = type
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'ClientID':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        return ClientID(type, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        return result


class Ordering:
    enum: List[str]
    description: str

    def __init__(self, enum: List[str], description: str) -> None:
        self.enum = enum
        self.description = description

    @staticmethod
    def from_dict(obj: Any) -> 'Ordering':
        assert isinstance(obj, dict)
        enum = from_list(from_str, obj.get("enum"))
        description = from_str(obj.get("description"))
        return Ordering(enum, description)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_str, self.enum)
        result["description"] = from_str(self.description)
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


class Status:
    enum: List[str]

    def __init__(self, enum: List[str]) -> None:
        self.enum = enum

    @staticmethod
    def from_dict(obj: Any) -> 'Status':
        assert isinstance(obj, dict)
        enum = from_list(from_str, obj.get("enum"))
        return Status(enum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_str, self.enum)
        return result


class TagsProperties:
    status: Status
    preferred: ChainName
    dex: ChainName
    properties: ClientID

    def __init__(self, status: Status, preferred: ChainName, dex: ChainName, properties: ClientID) -> None:
        self.status = status
        self.preferred = preferred
        self.dex = dex
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'TagsProperties':
        assert isinstance(obj, dict)
        status = Status.from_dict(obj.get("status"))
        preferred = ChainName.from_dict(obj.get("preferred"))
        dex = ChainName.from_dict(obj.get("dex"))
        properties = ClientID.from_dict(obj.get("properties"))
        return TagsProperties(status, preferred, dex, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["status"] = to_class(Status, self.status)
        result["preferred"] = to_class(ChainName, self.preferred)
        result["dex"] = to_class(ChainName, self.dex)
        result["properties"] = to_class(ClientID, self.properties)
        return result


class Tags:
    type: str
    description: str
    properties: TagsProperties

    def __init__(self, type: str, description: str, properties: TagsProperties) -> None:
        self.type = type
        self.description = description
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        description = from_str(obj.get("description"))
        properties = TagsProperties.from_dict(obj.get("properties"))
        return Tags(type, description, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["description"] = from_str(self.description)
        result["properties"] = to_class(TagsProperties, self.properties)
        return result


class ItemProperties:
    chain_1: FluffyChain
    chain_2: FluffyChain
    ordering: Ordering
    version: ClientID
    description: ClientID
    tags: Tags

    def __init__(self, chain_1: FluffyChain, chain_2: FluffyChain, ordering: Ordering, version: ClientID, description: ClientID, tags: Tags) -> None:
        self.chain_1 = chain_1
        self.chain_2 = chain_2
        self.ordering = ordering
        self.version = version
        self.description = description
        self.tags = tags

    @staticmethod
    def from_dict(obj: Any) -> 'ItemProperties':
        assert isinstance(obj, dict)
        chain_1 = FluffyChain.from_dict(obj.get("chain-1"))
        chain_2 = FluffyChain.from_dict(obj.get("chain-2"))
        ordering = Ordering.from_dict(obj.get("ordering"))
        version = ClientID.from_dict(obj.get("version"))
        description = ClientID.from_dict(obj.get("description"))
        tags = Tags.from_dict(obj.get("tags"))
        return ItemProperties(chain_1, chain_2, ordering, version, description, tags)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-1"] = to_class(FluffyChain, self.chain_1)
        result["chain-2"] = to_class(FluffyChain, self.chain_2)
        result["ordering"] = to_class(Ordering, self.ordering)
        result["version"] = to_class(ClientID, self.version)
        result["description"] = to_class(ClientID, self.description)
        result["tags"] = to_class(Tags, self.tags)
        return result


class Item:
    type: str
    required: List[str]
    properties: ItemProperties

    def __init__(self, type: str, required: List[str], properties: ItemProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = ItemProperties.from_dict(obj.get("properties"))
        return Item(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(ItemProperties, self.properties)
        return result


class Channels:
    type: str
    items: List[Item]

    def __init__(self, type: str, items: List[Item]) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Channels':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = from_list(Item.from_dict, obj.get("items"))
        return Channels(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        return result


class ChainInfoProperties:
    chain_name: ChainName
    client_id: ClientID
    connection_id: ClientID

    def __init__(self, chain_name: ChainName, client_id: ClientID, connection_id: ClientID) -> None:
        self.chain_name = chain_name
        self.client_id = client_id
        self.connection_id = connection_id

    @staticmethod
    def from_dict(obj: Any) -> 'ChainInfoProperties':
        assert isinstance(obj, dict)
        chain_name = ChainName.from_dict(obj.get("chain-name"))
        client_id = ClientID.from_dict(obj.get("client-id"))
        connection_id = ClientID.from_dict(obj.get("connection-id"))
        return ChainInfoProperties(chain_name, client_id, connection_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-name"] = to_class(ChainName, self.chain_name)
        result["client-id"] = to_class(ClientID, self.client_id)
        result["connection-id"] = to_class(ClientID, self.connection_id)
        return result


class ChainInfo:
    type: str
    required: List[str]
    properties: ChainInfoProperties

    def __init__(self, type: str, required: List[str], properties: ChainInfoProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'ChainInfo':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = ChainInfoProperties.from_dict(obj.get("properties"))
        return ChainInfo(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(ChainInfoProperties, self.properties)
        return result


class ChannelInfoProperties:
    channel_id: ClientID
    port_id: ClientID

    def __init__(self, channel_id: ClientID, port_id: ClientID) -> None:
        self.channel_id = channel_id
        self.port_id = port_id

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelInfoProperties':
        assert isinstance(obj, dict)
        channel_id = ClientID.from_dict(obj.get("channel-id"))
        port_id = ClientID.from_dict(obj.get("port-id"))
        return ChannelInfoProperties(channel_id, port_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel-id"] = to_class(ClientID, self.channel_id)
        result["port-id"] = to_class(ClientID, self.port_id)
        return result


class ChannelInfo:
    type: str
    required: List[str]
    properties: ChannelInfoProperties

    def __init__(self, type: str, required: List[str], properties: ChannelInfoProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelInfo':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = ChannelInfoProperties.from_dict(obj.get("properties"))
        return ChannelInfo(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(ChannelInfoProperties, self.properties)
        return result


class Defs:
    chain_info: ChainInfo
    channel_info: ChannelInfo

    def __init__(self, chain_info: ChainInfo, channel_info: ChannelInfo) -> None:
        self.chain_info = chain_info
        self.channel_info = channel_info

    @staticmethod
    def from_dict(obj: Any) -> 'Defs':
        assert isinstance(obj, dict)
        chain_info = ChainInfo.from_dict(obj.get("chain_info"))
        channel_info = ChannelInfo.from_dict(obj.get("channel_info"))
        return Defs(chain_info, channel_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain_info"] = to_class(ChainInfo, self.chain_info)
        result["channel_info"] = to_class(ChannelInfo, self.channel_info)
        return result


class IbcDataProperties:
    chain_1: PurpleChain
    chain_2: PurpleChain
    channels: Channels
    defs: Defs

    def __init__(self, chain_1: PurpleChain, chain_2: PurpleChain, channels: Channels, defs: Defs) -> None:
        self.chain_1 = chain_1
        self.chain_2 = chain_2
        self.channels = channels
        self.defs = defs

    @staticmethod
    def from_dict(obj: Any) -> 'IbcDataProperties':
        assert isinstance(obj, dict)
        chain_1 = PurpleChain.from_dict(obj.get("chain-1"))
        chain_2 = PurpleChain.from_dict(obj.get("chain-2"))
        channels = Channels.from_dict(obj.get("channels"))
        defs = Defs.from_dict(obj.get("$defs"))
        return IbcDataProperties(chain_1, chain_2, channels, defs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-1"] = to_class(PurpleChain, self.chain_1)
        result["chain-2"] = to_class(PurpleChain, self.chain_2)
        result["channels"] = to_class(Channels, self.channels)
        result["$defs"] = to_class(Defs, self.defs)
        return result


class IbcData:
    schema: str
    type: str
    required: List[str]
    properties: IbcDataProperties

    def __init__(self, schema: str, type: str, required: List[str], properties: IbcDataProperties) -> None:
        self.schema = schema
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'IbcData':
        assert isinstance(obj, dict)
        schema = from_str(obj.get("$schema"))
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = IbcDataProperties.from_dict(obj.get("properties"))
        return IbcData(schema, type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$schema"] = from_str(self.schema)
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(IbcDataProperties, self.properties)
        return result


def ibc_data_from_dict(s: Any) -> IbcData:
    return IbcData.from_dict(s)


def ibc_data_to_dict(x: IbcData) -> Any:
    return to_class(IbcData, x)
