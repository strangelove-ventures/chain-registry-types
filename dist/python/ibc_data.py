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
    description: str
    items: Items
    type: str

    def __init__(self, description: str, items: Items, type: str) -> None:
        self.description = description
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleChain':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        items = Items.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return PurpleChain(description, items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["items"] = to_class(Items, self.items)
        result["type"] = from_str(self.type)
        return result


class FluffyChain:
    items: Items
    type: str

    def __init__(self, items: Items, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'FluffyChain':
        assert isinstance(obj, dict)
        items = Items.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return FluffyChain(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(Items, self.items)
        result["type"] = from_str(self.type)
        return result


class ClientID:
    description: str
    type: str

    def __init__(self, description: str, type: str) -> None:
        self.description = description
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ClientID':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        return ClientID(description, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
        return result


class Ordering:
    description: str
    enum: List[str]

    def __init__(self, description: str, enum: List[str]) -> None:
        self.description = description
        self.enum = enum

    @staticmethod
    def from_dict(obj: Any) -> 'Ordering':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        enum = from_list(from_str, obj.get("enum"))
        return Ordering(description, enum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["enum"] = from_list(from_str, self.enum)
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
    dex: ChainName
    preferred: ChainName
    properties: ClientID
    status: Status

    def __init__(self, dex: ChainName, preferred: ChainName, properties: ClientID, status: Status) -> None:
        self.dex = dex
        self.preferred = preferred
        self.properties = properties
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'TagsProperties':
        assert isinstance(obj, dict)
        dex = ChainName.from_dict(obj.get("dex"))
        preferred = ChainName.from_dict(obj.get("preferred"))
        properties = ClientID.from_dict(obj.get("properties"))
        status = Status.from_dict(obj.get("status"))
        return TagsProperties(dex, preferred, properties, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dex"] = to_class(ChainName, self.dex)
        result["preferred"] = to_class(ChainName, self.preferred)
        result["properties"] = to_class(ClientID, self.properties)
        result["status"] = to_class(Status, self.status)
        return result


class Tags:
    description: str
    properties: TagsProperties
    type: str

    def __init__(self, description: str, properties: TagsProperties, type: str) -> None:
        self.description = description
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Tags':
        assert isinstance(obj, dict)
        description = from_str(obj.get("description"))
        properties = TagsProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Tags(description, properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_str(self.description)
        result["properties"] = to_class(TagsProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class ItemProperties:
    chain_1: FluffyChain
    chain_2: FluffyChain
    description: ClientID
    ordering: Ordering
    tags: Tags
    version: ClientID

    def __init__(self, chain_1: FluffyChain, chain_2: FluffyChain, description: ClientID, ordering: Ordering, tags: Tags, version: ClientID) -> None:
        self.chain_1 = chain_1
        self.chain_2 = chain_2
        self.description = description
        self.ordering = ordering
        self.tags = tags
        self.version = version

    @staticmethod
    def from_dict(obj: Any) -> 'ItemProperties':
        assert isinstance(obj, dict)
        chain_1 = FluffyChain.from_dict(obj.get("chain-1"))
        chain_2 = FluffyChain.from_dict(obj.get("chain-2"))
        description = ClientID.from_dict(obj.get("description"))
        ordering = Ordering.from_dict(obj.get("ordering"))
        tags = Tags.from_dict(obj.get("tags"))
        version = ClientID.from_dict(obj.get("version"))
        return ItemProperties(chain_1, chain_2, description, ordering, tags, version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain-1"] = to_class(FluffyChain, self.chain_1)
        result["chain-2"] = to_class(FluffyChain, self.chain_2)
        result["description"] = to_class(ClientID, self.description)
        result["ordering"] = to_class(Ordering, self.ordering)
        result["tags"] = to_class(Tags, self.tags)
        result["version"] = to_class(ClientID, self.version)
        return result


class Item:
    properties: ItemProperties
    required: List[str]
    type: str

    def __init__(self, properties: ItemProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        properties = ItemProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return Item(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(ItemProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class Channels:
    items: List[Item]
    type: str

    def __init__(self, items: List[Item], type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Channels':
        assert isinstance(obj, dict)
        items = from_list(Item.from_dict, obj.get("items"))
        type = from_str(obj.get("type"))
        return Channels(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = from_list(lambda x: to_class(Item, x), self.items)
        result["type"] = from_str(self.type)
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
    properties: ChainInfoProperties
    required: List[str]
    type: str

    def __init__(self, properties: ChainInfoProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ChainInfo':
        assert isinstance(obj, dict)
        properties = ChainInfoProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return ChainInfo(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(ChainInfoProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
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
    properties: ChannelInfoProperties
    required: List[str]
    type: str

    def __init__(self, properties: ChannelInfoProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelInfo':
        assert isinstance(obj, dict)
        properties = ChannelInfoProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return ChannelInfo(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(ChannelInfoProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
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
    properties: IbcDataProperties
    required: List[str]
    schema: str
    type: str

    def __init__(self, properties: IbcDataProperties, required: List[str], schema: str, type: str) -> None:
        self.properties = properties
        self.required = required
        self.schema = schema
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'IbcData':
        assert isinstance(obj, dict)
        properties = IbcDataProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        schema = from_str(obj.get("$schema"))
        type = from_str(obj.get("type"))
        return IbcData(properties, required, schema, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(IbcDataProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["$schema"] = from_str(self.schema)
        result["type"] = from_str(self.type)
        return result


def ibc_data_from_dict(s: Any) -> IbcData:
    return IbcData.from_dict(s)


def ibc_data_to_dict(x: IbcData) -> Any:
    return to_class(IbcData, x)
