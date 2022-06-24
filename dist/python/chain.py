# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = chain_from_dict(json.loads(json_string))

from enum import Enum
from typing import Any, List, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class Updatelink(Enum):
    NUMBER = "number"
    STRING = "string"


class Bech32Prefix:
    type: Updatelink

    def __init__(self, type: Updatelink) -> None:
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Bech32Prefix':
        assert isinstance(obj, dict)
        type = Updatelink(obj.get("type"))
        return Bech32Prefix(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(Updatelink, self.type)
        return result


class EndpointProperties:
    address: Bech32Prefix
    provider: Bech32Prefix

    def __init__(self, address: Bech32Prefix, provider: Bech32Prefix) -> None:
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'EndpointProperties':
        assert isinstance(obj, dict)
        address = Bech32Prefix.from_dict(obj.get("address"))
        provider = Bech32Prefix.from_dict(obj.get("provider"))
        return EndpointProperties(address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = to_class(Bech32Prefix, self.address)
        result["provider"] = to_class(Bech32Prefix, self.provider)
        return result


class Endpoint:
    properties: EndpointProperties
    required: List[str]
    type: str

    def __init__(self, properties: EndpointProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Endpoint':
        assert isinstance(obj, dict)
        properties = EndpointProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return Endpoint(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(EndpointProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class ExplorerProperties:
    account_page: Bech32Prefix
    kind: Bech32Prefix
    tx_page: Bech32Prefix
    url: Bech32Prefix

    def __init__(self, account_page: Bech32Prefix, kind: Bech32Prefix, tx_page: Bech32Prefix, url: Bech32Prefix) -> None:
        self.account_page = account_page
        self.kind = kind
        self.tx_page = tx_page
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'ExplorerProperties':
        assert isinstance(obj, dict)
        account_page = Bech32Prefix.from_dict(obj.get("account_page"))
        kind = Bech32Prefix.from_dict(obj.get("kind"))
        tx_page = Bech32Prefix.from_dict(obj.get("tx_page"))
        url = Bech32Prefix.from_dict(obj.get("url"))
        return ExplorerProperties(account_page, kind, tx_page, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["account_page"] = to_class(Bech32Prefix, self.account_page)
        result["kind"] = to_class(Bech32Prefix, self.kind)
        result["tx_page"] = to_class(Bech32Prefix, self.tx_page)
        result["url"] = to_class(Bech32Prefix, self.url)
        return result


class Explorer:
    properties: ExplorerProperties
    type: str

    def __init__(self, properties: ExplorerProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Explorer':
        assert isinstance(obj, dict)
        properties = ExplorerProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Explorer(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(ExplorerProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class FeeTokenProperties:
    denom: Bech32Prefix
    fixed_min_gas_price: Bech32Prefix

    def __init__(self, denom: Bech32Prefix, fixed_min_gas_price: Bech32Prefix) -> None:
        self.denom = denom
        self.fixed_min_gas_price = fixed_min_gas_price

    @staticmethod
    def from_dict(obj: Any) -> 'FeeTokenProperties':
        assert isinstance(obj, dict)
        denom = Bech32Prefix.from_dict(obj.get("denom"))
        fixed_min_gas_price = Bech32Prefix.from_dict(obj.get("fixed_min_gas_price"))
        return FeeTokenProperties(denom, fixed_min_gas_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["denom"] = to_class(Bech32Prefix, self.denom)
        result["fixed_min_gas_price"] = to_class(Bech32Prefix, self.fixed_min_gas_price)
        return result


class FeeToken:
    properties: FeeTokenProperties
    required: List[str]
    type: str

    def __init__(self, properties: FeeTokenProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'FeeToken':
        assert isinstance(obj, dict)
        properties = FeeTokenProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return FeeToken(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(FeeTokenProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class PNG:
    format: str
    type: Updatelink

    def __init__(self, format: str, type: Updatelink) -> None:
        self.format = format
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'PNG':
        assert isinstance(obj, dict)
        format = from_str(obj.get("format"))
        type = Updatelink(obj.get("type"))
        return PNG(format, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["format"] = from_str(self.format)
        result["type"] = to_enum(Updatelink, self.type)
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


class PeerProperties:
    address: Bech32Prefix
    id: Bech32Prefix
    provider: Bech32Prefix

    def __init__(self, address: Bech32Prefix, id: Bech32Prefix, provider: Bech32Prefix) -> None:
        self.address = address
        self.id = id
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'PeerProperties':
        assert isinstance(obj, dict)
        address = Bech32Prefix.from_dict(obj.get("address"))
        id = Bech32Prefix.from_dict(obj.get("id"))
        provider = Bech32Prefix.from_dict(obj.get("provider"))
        return PeerProperties(address, id, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = to_class(Bech32Prefix, self.address)
        result["id"] = to_class(Bech32Prefix, self.id)
        result["provider"] = to_class(Bech32Prefix, self.provider)
        return result


class Peer:
    properties: PeerProperties
    required: List[str]
    type: str

    def __init__(self, properties: PeerProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Peer':
        assert isinstance(obj, dict)
        properties = PeerProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return Peer(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(PeerProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class Defs:
    endpoint: Endpoint
    explorer: Explorer
    fee_token: FeeToken
    logo_ur_is: LogoURIs
    peer: Peer

    def __init__(self, endpoint: Endpoint, explorer: Explorer, fee_token: FeeToken, logo_ur_is: LogoURIs, peer: Peer) -> None:
        self.endpoint = endpoint
        self.explorer = explorer
        self.fee_token = fee_token
        self.logo_ur_is = logo_ur_is
        self.peer = peer

    @staticmethod
    def from_dict(obj: Any) -> 'Defs':
        assert isinstance(obj, dict)
        endpoint = Endpoint.from_dict(obj.get("endpoint"))
        explorer = Explorer.from_dict(obj.get("explorer"))
        fee_token = FeeToken.from_dict(obj.get("fee_token"))
        logo_ur_is = LogoURIs.from_dict(obj.get("logo_URIs"))
        peer = Peer.from_dict(obj.get("peer"))
        return Defs(endpoint, explorer, fee_token, logo_ur_is, peer)

    def to_dict(self) -> dict:
        result: dict = {}
        result["endpoint"] = to_class(Endpoint, self.endpoint)
        result["explorer"] = to_class(Explorer, self.explorer)
        result["fee_token"] = to_class(FeeToken, self.fee_token)
        result["logo_URIs"] = to_class(LogoURIs, self.logo_ur_is)
        result["peer"] = to_class(Peer, self.peer)
        return result


class ExplorersItems:
    ref: str

    def __init__(self, ref: str) -> None:
        self.ref = ref

    @staticmethod
    def from_dict(obj: Any) -> 'ExplorersItems':
        assert isinstance(obj, dict)
        ref = from_str(obj.get("$ref"))
        return ExplorersItems(ref)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$ref"] = from_str(self.ref)
        return result


class Explorers:
    items: ExplorersItems
    type: str

    def __init__(self, items: ExplorersItems, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Explorers':
        assert isinstance(obj, dict)
        items = ExplorersItems.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return Explorers(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(ExplorersItems, self.items)
        result["type"] = from_str(self.type)
        return result


class ApisProperties:
    grpc: Explorers
    rest: Explorers
    rpc: Explorers

    def __init__(self, grpc: Explorers, rest: Explorers, rpc: Explorers) -> None:
        self.grpc = grpc
        self.rest = rest
        self.rpc = rpc

    @staticmethod
    def from_dict(obj: Any) -> 'ApisProperties':
        assert isinstance(obj, dict)
        grpc = Explorers.from_dict(obj.get("grpc"))
        rest = Explorers.from_dict(obj.get("rest"))
        rpc = Explorers.from_dict(obj.get("rpc"))
        return ApisProperties(grpc, rest, rpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["grpc"] = to_class(Explorers, self.grpc)
        result["rest"] = to_class(Explorers, self.rest)
        result["rpc"] = to_class(Explorers, self.rpc)
        return result


class Apis:
    properties: ApisProperties
    type: str

    def __init__(self, properties: ApisProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Apis':
        assert isinstance(obj, dict)
        properties = ApisProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Apis(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(ApisProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class BinariesProperties:
    linux_amd: PNG

    def __init__(self, linux_amd: PNG) -> None:
        self.linux_amd = linux_amd

    @staticmethod
    def from_dict(obj: Any) -> 'BinariesProperties':
        assert isinstance(obj, dict)
        linux_amd = PNG.from_dict(obj.get("linux/amd"))
        return BinariesProperties(linux_amd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["linux/amd"] = to_class(PNG, self.linux_amd)
        return result


class Binaries:
    properties: BinariesProperties
    type: str

    def __init__(self, properties: BinariesProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Binaries':
        assert isinstance(obj, dict)
        properties = BinariesProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Binaries(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(BinariesProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class CompatibleVersions:
    items: Bech32Prefix
    type: str

    def __init__(self, items: Bech32Prefix, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'CompatibleVersions':
        assert isinstance(obj, dict)
        items = Bech32Prefix.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return CompatibleVersions(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(Bech32Prefix, self.items)
        result["type"] = from_str(self.type)
        return result


class CodebaseProperties:
    binaries: Binaries
    compatible_versions: CompatibleVersions
    git_repo: PNG
    recommended_version: Bech32Prefix

    def __init__(self, binaries: Binaries, compatible_versions: CompatibleVersions, git_repo: PNG, recommended_version: Bech32Prefix) -> None:
        self.binaries = binaries
        self.compatible_versions = compatible_versions
        self.git_repo = git_repo
        self.recommended_version = recommended_version

    @staticmethod
    def from_dict(obj: Any) -> 'CodebaseProperties':
        assert isinstance(obj, dict)
        binaries = Binaries.from_dict(obj.get("binaries"))
        compatible_versions = CompatibleVersions.from_dict(obj.get("compatible_versions"))
        git_repo = PNG.from_dict(obj.get("git_repo"))
        recommended_version = Bech32Prefix.from_dict(obj.get("recommended_version"))
        return CodebaseProperties(binaries, compatible_versions, git_repo, recommended_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["binaries"] = to_class(Binaries, self.binaries)
        result["compatible_versions"] = to_class(CompatibleVersions, self.compatible_versions)
        result["git_repo"] = to_class(PNG, self.git_repo)
        result["recommended_version"] = to_class(Bech32Prefix, self.recommended_version)
        return result


class Codebase:
    properties: CodebaseProperties
    required: List[str]
    type: str

    def __init__(self, properties: CodebaseProperties, required: List[str], type: str) -> None:
        self.properties = properties
        self.required = required
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Codebase':
        assert isinstance(obj, dict)
        properties = CodebaseProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        type = from_str(obj.get("type"))
        return Codebase(properties, required, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(CodebaseProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["type"] = from_str(self.type)
        return result


class FeesProperties:
    fee_tokens: Explorers

    def __init__(self, fee_tokens: Explorers) -> None:
        self.fee_tokens = fee_tokens

    @staticmethod
    def from_dict(obj: Any) -> 'FeesProperties':
        assert isinstance(obj, dict)
        fee_tokens = Explorers.from_dict(obj.get("fee_tokens"))
        return FeesProperties(fee_tokens)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fee_tokens"] = to_class(Explorers, self.fee_tokens)
        return result


class Fees:
    properties: FeesProperties
    type: str

    def __init__(self, properties: FeesProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Fees':
        assert isinstance(obj, dict)
        properties = FeesProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Fees(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(FeesProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class GenesisProperties:
    genesis_url: Bech32Prefix

    def __init__(self, genesis_url: Bech32Prefix) -> None:
        self.genesis_url = genesis_url

    @staticmethod
    def from_dict(obj: Any) -> 'GenesisProperties':
        assert isinstance(obj, dict)
        genesis_url = Bech32Prefix.from_dict(obj.get("genesis_url"))
        return GenesisProperties(genesis_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["genesis_url"] = to_class(Bech32Prefix, self.genesis_url)
        return result


class Genesis:
    properties: GenesisProperties
    type: str

    def __init__(self, properties: GenesisProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Genesis':
        assert isinstance(obj, dict)
        properties = GenesisProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Genesis(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(GenesisProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class KeyAlgosItems:
    enum: List[str]
    type: Updatelink
    unique_items: bool

    def __init__(self, enum: List[str], type: Updatelink, unique_items: bool) -> None:
        self.enum = enum
        self.type = type
        self.unique_items = unique_items

    @staticmethod
    def from_dict(obj: Any) -> 'KeyAlgosItems':
        assert isinstance(obj, dict)
        enum = from_list(from_str, obj.get("enum"))
        type = Updatelink(obj.get("type"))
        unique_items = from_bool(obj.get("uniqueItems"))
        return KeyAlgosItems(enum, type, unique_items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_str, self.enum)
        result["type"] = to_enum(Updatelink, self.type)
        result["uniqueItems"] = from_bool(self.unique_items)
        return result


class KeyAlgos:
    items: KeyAlgosItems
    type: str

    def __init__(self, items: KeyAlgosItems, type: str) -> None:
        self.items = items
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'KeyAlgos':
        assert isinstance(obj, dict)
        items = KeyAlgosItems.from_dict(obj.get("items"))
        type = from_str(obj.get("type"))
        return KeyAlgos(items, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["items"] = to_class(KeyAlgosItems, self.items)
        result["type"] = from_str(self.type)
        return result


class NetworkType:
    enum: List[str]

    def __init__(self, enum: List[str]) -> None:
        self.enum = enum

    @staticmethod
    def from_dict(obj: Any) -> 'NetworkType':
        assert isinstance(obj, dict)
        enum = from_list(from_str, obj.get("enum"))
        return NetworkType(enum)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enum"] = from_list(from_str, self.enum)
        return result


class PeersProperties:
    persistent_peers: Explorers
    seeds: Explorers

    def __init__(self, persistent_peers: Explorers, seeds: Explorers) -> None:
        self.persistent_peers = persistent_peers
        self.seeds = seeds

    @staticmethod
    def from_dict(obj: Any) -> 'PeersProperties':
        assert isinstance(obj, dict)
        persistent_peers = Explorers.from_dict(obj.get("persistent_peers"))
        seeds = Explorers.from_dict(obj.get("seeds"))
        return PeersProperties(persistent_peers, seeds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["persistent_peers"] = to_class(Explorers, self.persistent_peers)
        result["seeds"] = to_class(Explorers, self.seeds)
        return result


class Peers:
    properties: PeersProperties
    type: str

    def __init__(self, properties: PeersProperties, type: str) -> None:
        self.properties = properties
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Peers':
        assert isinstance(obj, dict)
        properties = PeersProperties.from_dict(obj.get("properties"))
        type = from_str(obj.get("type"))
        return Peers(properties, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["properties"] = to_class(PeersProperties, self.properties)
        result["type"] = from_str(self.type)
        return result


class ChainProperties:
    apis: Apis
    bech32_prefix: Bech32Prefix
    chain_id: Bech32Prefix
    chain_name: Bech32Prefix
    codebase: Codebase
    daemon_name: Bech32Prefix
    explorers: Explorers
    fees: Fees
    genesis: Genesis
    key_algos: KeyAlgos
    network_type: NetworkType
    node_home: Bech32Prefix
    peers: Peers
    pretty_name: Bech32Prefix
    slip44: Bech32Prefix
    status: NetworkType

    def __init__(self, apis: Apis, bech32_prefix: Bech32Prefix, chain_id: Bech32Prefix, chain_name: Bech32Prefix, codebase: Codebase, daemon_name: Bech32Prefix, explorers: Explorers, fees: Fees, genesis: Genesis, key_algos: KeyAlgos, network_type: NetworkType, node_home: Bech32Prefix, peers: Peers, pretty_name: Bech32Prefix, slip44: Bech32Prefix, status: NetworkType) -> None:
        self.apis = apis
        self.bech32_prefix = bech32_prefix
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.codebase = codebase
        self.daemon_name = daemon_name
        self.explorers = explorers
        self.fees = fees
        self.genesis = genesis
        self.key_algos = key_algos
        self.network_type = network_type
        self.node_home = node_home
        self.peers = peers
        self.pretty_name = pretty_name
        self.slip44 = slip44
        self.status = status

    @staticmethod
    def from_dict(obj: Any) -> 'ChainProperties':
        assert isinstance(obj, dict)
        apis = Apis.from_dict(obj.get("apis"))
        bech32_prefix = Bech32Prefix.from_dict(obj.get("bech32_prefix"))
        chain_id = Bech32Prefix.from_dict(obj.get("chain_id"))
        chain_name = Bech32Prefix.from_dict(obj.get("chain_name"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        daemon_name = Bech32Prefix.from_dict(obj.get("daemon_name"))
        explorers = Explorers.from_dict(obj.get("explorers"))
        fees = Fees.from_dict(obj.get("fees"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        key_algos = KeyAlgos.from_dict(obj.get("key_algos"))
        network_type = NetworkType.from_dict(obj.get("network_type"))
        node_home = Bech32Prefix.from_dict(obj.get("node_home"))
        peers = Peers.from_dict(obj.get("peers"))
        pretty_name = Bech32Prefix.from_dict(obj.get("pretty_name"))
        slip44 = Bech32Prefix.from_dict(obj.get("slip44"))
        status = NetworkType.from_dict(obj.get("status"))
        return ChainProperties(apis, bech32_prefix, chain_id, chain_name, codebase, daemon_name, explorers, fees, genesis, key_algos, network_type, node_home, peers, pretty_name, slip44, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["apis"] = to_class(Apis, self.apis)
        result["bech32_prefix"] = to_class(Bech32Prefix, self.bech32_prefix)
        result["chain_id"] = to_class(Bech32Prefix, self.chain_id)
        result["chain_name"] = to_class(Bech32Prefix, self.chain_name)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["daemon_name"] = to_class(Bech32Prefix, self.daemon_name)
        result["explorers"] = to_class(Explorers, self.explorers)
        result["fees"] = to_class(Fees, self.fees)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["key_algos"] = to_class(KeyAlgos, self.key_algos)
        result["network_type"] = to_class(NetworkType, self.network_type)
        result["node_home"] = to_class(Bech32Prefix, self.node_home)
        result["peers"] = to_class(Peers, self.peers)
        result["pretty_name"] = to_class(Bech32Prefix, self.pretty_name)
        result["slip44"] = to_class(Bech32Prefix, self.slip44)
        result["status"] = to_class(NetworkType, self.status)
        return result


class Chain:
    defs: Defs
    description: str
    id: str
    properties: ChainProperties
    required: List[str]
    schema: str
    title: str
    type: str
    updatelink: Updatelink

    def __init__(self, defs: Defs, description: str, id: str, properties: ChainProperties, required: List[str], schema: str, title: str, type: str, updatelink: Updatelink) -> None:
        self.defs = defs
        self.description = description
        self.id = id
        self.properties = properties
        self.required = required
        self.schema = schema
        self.title = title
        self.type = type
        self.updatelink = updatelink

    @staticmethod
    def from_dict(obj: Any) -> 'Chain':
        assert isinstance(obj, dict)
        defs = Defs.from_dict(obj.get("$defs"))
        description = from_str(obj.get("description"))
        id = from_str(obj.get("$id"))
        properties = ChainProperties.from_dict(obj.get("properties"))
        required = from_list(from_str, obj.get("required"))
        schema = from_str(obj.get("$schema"))
        title = from_str(obj.get("title"))
        type = from_str(obj.get("type"))
        updatelink = Updatelink(obj.get("updatelink"))
        return Chain(defs, description, id, properties, required, schema, title, type, updatelink)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$defs"] = to_class(Defs, self.defs)
        result["description"] = from_str(self.description)
        result["$id"] = from_str(self.id)
        result["properties"] = to_class(ChainProperties, self.properties)
        result["required"] = from_list(from_str, self.required)
        result["$schema"] = from_str(self.schema)
        result["title"] = from_str(self.title)
        result["type"] = from_str(self.type)
        result["updatelink"] = to_enum(Updatelink, self.updatelink)
        return result


def chain_from_dict(s: Any) -> Chain:
    return Chain.from_dict(s)


def chain_to_dict(x: Chain) -> Any:
    return to_class(Chain, x)
