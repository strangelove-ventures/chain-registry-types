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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


class TypeEnum(Enum):
    NUMBER = "number"
    STRING = "string"


class Bech32Prefix:
    type: TypeEnum

    def __init__(self, type: TypeEnum) -> None:
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Bech32Prefix':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        return Bech32Prefix(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
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
    type: str
    required: List[str]
    properties: EndpointProperties

    def __init__(self, type: str, required: List[str], properties: EndpointProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Endpoint':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = EndpointProperties.from_dict(obj.get("properties"))
        return Endpoint(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(EndpointProperties, self.properties)
        return result


class ExplorerProperties:
    kind: Bech32Prefix
    url: Bech32Prefix
    tx_page: Bech32Prefix
    account_page: Bech32Prefix

    def __init__(self, kind: Bech32Prefix, url: Bech32Prefix, tx_page: Bech32Prefix, account_page: Bech32Prefix) -> None:
        self.kind = kind
        self.url = url
        self.tx_page = tx_page
        self.account_page = account_page

    @staticmethod
    def from_dict(obj: Any) -> 'ExplorerProperties':
        assert isinstance(obj, dict)
        kind = Bech32Prefix.from_dict(obj.get("kind"))
        url = Bech32Prefix.from_dict(obj.get("url"))
        tx_page = Bech32Prefix.from_dict(obj.get("tx_page"))
        account_page = Bech32Prefix.from_dict(obj.get("account_page"))
        return ExplorerProperties(kind, url, tx_page, account_page)

    def to_dict(self) -> dict:
        result: dict = {}
        result["kind"] = to_class(Bech32Prefix, self.kind)
        result["url"] = to_class(Bech32Prefix, self.url)
        result["tx_page"] = to_class(Bech32Prefix, self.tx_page)
        result["account_page"] = to_class(Bech32Prefix, self.account_page)
        return result


class Explorer:
    type: str
    properties: ExplorerProperties

    def __init__(self, type: str, properties: ExplorerProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Explorer':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = ExplorerProperties.from_dict(obj.get("properties"))
        return Explorer(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(ExplorerProperties, self.properties)
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
    type: str
    required: List[str]
    properties: FeeTokenProperties

    def __init__(self, type: str, required: List[str], properties: FeeTokenProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'FeeToken':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = FeeTokenProperties.from_dict(obj.get("properties"))
        return FeeToken(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(FeeTokenProperties, self.properties)
        return result


class PNG:
    type: TypeEnum
    format: str

    def __init__(self, type: TypeEnum, format: str) -> None:
        self.type = type
        self.format = format

    @staticmethod
    def from_dict(obj: Any) -> 'PNG':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        format = from_str(obj.get("format"))
        return PNG(type, format)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
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


class PeerProperties:
    id: Bech32Prefix
    address: Bech32Prefix
    provider: Bech32Prefix

    def __init__(self, id: Bech32Prefix, address: Bech32Prefix, provider: Bech32Prefix) -> None:
        self.id = id
        self.address = address
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'PeerProperties':
        assert isinstance(obj, dict)
        id = Bech32Prefix.from_dict(obj.get("id"))
        address = Bech32Prefix.from_dict(obj.get("address"))
        provider = Bech32Prefix.from_dict(obj.get("provider"))
        return PeerProperties(id, address, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = to_class(Bech32Prefix, self.id)
        result["address"] = to_class(Bech32Prefix, self.address)
        result["provider"] = to_class(Bech32Prefix, self.provider)
        return result


class Peer:
    type: str
    required: List[str]
    properties: PeerProperties

    def __init__(self, type: str, required: List[str], properties: PeerProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Peer':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = PeerProperties.from_dict(obj.get("properties"))
        return Peer(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(PeerProperties, self.properties)
        return result


class Defs:
    peer: Peer
    endpoint: Endpoint
    explorer: Explorer
    fee_token: FeeToken
    logo_ur_is: LogoURIs

    def __init__(self, peer: Peer, endpoint: Endpoint, explorer: Explorer, fee_token: FeeToken, logo_ur_is: LogoURIs) -> None:
        self.peer = peer
        self.endpoint = endpoint
        self.explorer = explorer
        self.fee_token = fee_token
        self.logo_ur_is = logo_ur_is

    @staticmethod
    def from_dict(obj: Any) -> 'Defs':
        assert isinstance(obj, dict)
        peer = Peer.from_dict(obj.get("peer"))
        endpoint = Endpoint.from_dict(obj.get("endpoint"))
        explorer = Explorer.from_dict(obj.get("explorer"))
        fee_token = FeeToken.from_dict(obj.get("fee_token"))
        logo_ur_is = LogoURIs.from_dict(obj.get("logo_URIs"))
        return Defs(peer, endpoint, explorer, fee_token, logo_ur_is)

    def to_dict(self) -> dict:
        result: dict = {}
        result["peer"] = to_class(Peer, self.peer)
        result["endpoint"] = to_class(Endpoint, self.endpoint)
        result["explorer"] = to_class(Explorer, self.explorer)
        result["fee_token"] = to_class(FeeToken, self.fee_token)
        result["logo_URIs"] = to_class(LogoURIs, self.logo_ur_is)
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
    type: str
    items: ExplorersItems

    def __init__(self, type: str, items: ExplorersItems) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'Explorers':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = ExplorersItems.from_dict(obj.get("items"))
        return Explorers(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(ExplorersItems, self.items)
        return result


class ApisProperties:
    rpc: Explorers
    rest: Explorers
    grpc: Explorers

    def __init__(self, rpc: Explorers, rest: Explorers, grpc: Explorers) -> None:
        self.rpc = rpc
        self.rest = rest
        self.grpc = grpc

    @staticmethod
    def from_dict(obj: Any) -> 'ApisProperties':
        assert isinstance(obj, dict)
        rpc = Explorers.from_dict(obj.get("rpc"))
        rest = Explorers.from_dict(obj.get("rest"))
        grpc = Explorers.from_dict(obj.get("grpc"))
        return ApisProperties(rpc, rest, grpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["rpc"] = to_class(Explorers, self.rpc)
        result["rest"] = to_class(Explorers, self.rest)
        result["grpc"] = to_class(Explorers, self.grpc)
        return result


class Apis:
    type: str
    properties: ApisProperties

    def __init__(self, type: str, properties: ApisProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Apis':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = ApisProperties.from_dict(obj.get("properties"))
        return Apis(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(ApisProperties, self.properties)
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
    type: str
    properties: BinariesProperties

    def __init__(self, type: str, properties: BinariesProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Binaries':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = BinariesProperties.from_dict(obj.get("properties"))
        return Binaries(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(BinariesProperties, self.properties)
        return result


class CompatibleVersions:
    type: str
    items: Bech32Prefix

    def __init__(self, type: str, items: Bech32Prefix) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'CompatibleVersions':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = Bech32Prefix.from_dict(obj.get("items"))
        return CompatibleVersions(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(Bech32Prefix, self.items)
        return result


class CodebaseProperties:
    git_repo: PNG
    recommended_version: Bech32Prefix
    compatible_versions: CompatibleVersions
    binaries: Binaries

    def __init__(self, git_repo: PNG, recommended_version: Bech32Prefix, compatible_versions: CompatibleVersions, binaries: Binaries) -> None:
        self.git_repo = git_repo
        self.recommended_version = recommended_version
        self.compatible_versions = compatible_versions
        self.binaries = binaries

    @staticmethod
    def from_dict(obj: Any) -> 'CodebaseProperties':
        assert isinstance(obj, dict)
        git_repo = PNG.from_dict(obj.get("git_repo"))
        recommended_version = Bech32Prefix.from_dict(obj.get("recommended_version"))
        compatible_versions = CompatibleVersions.from_dict(obj.get("compatible_versions"))
        binaries = Binaries.from_dict(obj.get("binaries"))
        return CodebaseProperties(git_repo, recommended_version, compatible_versions, binaries)

    def to_dict(self) -> dict:
        result: dict = {}
        result["git_repo"] = to_class(PNG, self.git_repo)
        result["recommended_version"] = to_class(Bech32Prefix, self.recommended_version)
        result["compatible_versions"] = to_class(CompatibleVersions, self.compatible_versions)
        result["binaries"] = to_class(Binaries, self.binaries)
        return result


class Codebase:
    type: str
    required: List[str]
    properties: CodebaseProperties

    def __init__(self, type: str, required: List[str], properties: CodebaseProperties) -> None:
        self.type = type
        self.required = required
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Codebase':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = CodebaseProperties.from_dict(obj.get("properties"))
        return Codebase(type, required, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(CodebaseProperties, self.properties)
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
    type: str
    properties: FeesProperties

    def __init__(self, type: str, properties: FeesProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Fees':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = FeesProperties.from_dict(obj.get("properties"))
        return Fees(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(FeesProperties, self.properties)
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
    type: str
    properties: GenesisProperties

    def __init__(self, type: str, properties: GenesisProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Genesis':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = GenesisProperties.from_dict(obj.get("properties"))
        return Genesis(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(GenesisProperties, self.properties)
        return result


class KeyAlgosItems:
    type: TypeEnum
    enum: List[str]
    unique_items: bool

    def __init__(self, type: TypeEnum, enum: List[str], unique_items: bool) -> None:
        self.type = type
        self.enum = enum
        self.unique_items = unique_items

    @staticmethod
    def from_dict(obj: Any) -> 'KeyAlgosItems':
        assert isinstance(obj, dict)
        type = TypeEnum(obj.get("type"))
        enum = from_list(from_str, obj.get("enum"))
        unique_items = from_bool(obj.get("uniqueItems"))
        return KeyAlgosItems(type, enum, unique_items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = to_enum(TypeEnum, self.type)
        result["enum"] = from_list(from_str, self.enum)
        result["uniqueItems"] = from_bool(self.unique_items)
        return result


class KeyAlgos:
    type: str
    items: KeyAlgosItems

    def __init__(self, type: str, items: KeyAlgosItems) -> None:
        self.type = type
        self.items = items

    @staticmethod
    def from_dict(obj: Any) -> 'KeyAlgos':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        items = KeyAlgosItems.from_dict(obj.get("items"))
        return KeyAlgos(type, items)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["items"] = to_class(KeyAlgosItems, self.items)
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
    seeds: Explorers
    persistent_peers: Explorers

    def __init__(self, seeds: Explorers, persistent_peers: Explorers) -> None:
        self.seeds = seeds
        self.persistent_peers = persistent_peers

    @staticmethod
    def from_dict(obj: Any) -> 'PeersProperties':
        assert isinstance(obj, dict)
        seeds = Explorers.from_dict(obj.get("seeds"))
        persistent_peers = Explorers.from_dict(obj.get("persistent_peers"))
        return PeersProperties(seeds, persistent_peers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["seeds"] = to_class(Explorers, self.seeds)
        result["persistent_peers"] = to_class(Explorers, self.persistent_peers)
        return result


class Peers:
    type: str
    properties: PeersProperties

    def __init__(self, type: str, properties: PeersProperties) -> None:
        self.type = type
        self.properties = properties

    @staticmethod
    def from_dict(obj: Any) -> 'Peers':
        assert isinstance(obj, dict)
        type = from_str(obj.get("type"))
        properties = PeersProperties.from_dict(obj.get("properties"))
        return Peers(type, properties)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_str(self.type)
        result["properties"] = to_class(PeersProperties, self.properties)
        return result


class ChainProperties:
    chain_name: Bech32Prefix
    chain_id: Bech32Prefix
    pretty_name: Bech32Prefix
    status: NetworkType
    network_type: NetworkType
    bech32_prefix: Bech32Prefix
    genesis: Genesis
    daemon_name: Bech32Prefix
    node_home: Bech32Prefix
    key_algos: KeyAlgos
    slip44: Bech32Prefix
    fees: Fees
    codebase: Codebase
    peers: Peers
    apis: Apis
    explorers: Explorers

    def __init__(self, chain_name: Bech32Prefix, chain_id: Bech32Prefix, pretty_name: Bech32Prefix, status: NetworkType, network_type: NetworkType, bech32_prefix: Bech32Prefix, genesis: Genesis, daemon_name: Bech32Prefix, node_home: Bech32Prefix, key_algos: KeyAlgos, slip44: Bech32Prefix, fees: Fees, codebase: Codebase, peers: Peers, apis: Apis, explorers: Explorers) -> None:
        self.chain_name = chain_name
        self.chain_id = chain_id
        self.pretty_name = pretty_name
        self.status = status
        self.network_type = network_type
        self.bech32_prefix = bech32_prefix
        self.genesis = genesis
        self.daemon_name = daemon_name
        self.node_home = node_home
        self.key_algos = key_algos
        self.slip44 = slip44
        self.fees = fees
        self.codebase = codebase
        self.peers = peers
        self.apis = apis
        self.explorers = explorers

    @staticmethod
    def from_dict(obj: Any) -> 'ChainProperties':
        assert isinstance(obj, dict)
        chain_name = Bech32Prefix.from_dict(obj.get("chain_name"))
        chain_id = Bech32Prefix.from_dict(obj.get("chain_id"))
        pretty_name = Bech32Prefix.from_dict(obj.get("pretty_name"))
        status = NetworkType.from_dict(obj.get("status"))
        network_type = NetworkType.from_dict(obj.get("network_type"))
        bech32_prefix = Bech32Prefix.from_dict(obj.get("bech32_prefix"))
        genesis = Genesis.from_dict(obj.get("genesis"))
        daemon_name = Bech32Prefix.from_dict(obj.get("daemon_name"))
        node_home = Bech32Prefix.from_dict(obj.get("node_home"))
        key_algos = KeyAlgos.from_dict(obj.get("key_algos"))
        slip44 = Bech32Prefix.from_dict(obj.get("slip44"))
        fees = Fees.from_dict(obj.get("fees"))
        codebase = Codebase.from_dict(obj.get("codebase"))
        peers = Peers.from_dict(obj.get("peers"))
        apis = Apis.from_dict(obj.get("apis"))
        explorers = Explorers.from_dict(obj.get("explorers"))
        return ChainProperties(chain_name, chain_id, pretty_name, status, network_type, bech32_prefix, genesis, daemon_name, node_home, key_algos, slip44, fees, codebase, peers, apis, explorers)

    def to_dict(self) -> dict:
        result: dict = {}
        result["chain_name"] = to_class(Bech32Prefix, self.chain_name)
        result["chain_id"] = to_class(Bech32Prefix, self.chain_id)
        result["pretty_name"] = to_class(Bech32Prefix, self.pretty_name)
        result["status"] = to_class(NetworkType, self.status)
        result["network_type"] = to_class(NetworkType, self.network_type)
        result["bech32_prefix"] = to_class(Bech32Prefix, self.bech32_prefix)
        result["genesis"] = to_class(Genesis, self.genesis)
        result["daemon_name"] = to_class(Bech32Prefix, self.daemon_name)
        result["node_home"] = to_class(Bech32Prefix, self.node_home)
        result["key_algos"] = to_class(KeyAlgos, self.key_algos)
        result["slip44"] = to_class(Bech32Prefix, self.slip44)
        result["fees"] = to_class(Fees, self.fees)
        result["codebase"] = to_class(Codebase, self.codebase)
        result["peers"] = to_class(Peers, self.peers)
        result["apis"] = to_class(Apis, self.apis)
        result["explorers"] = to_class(Explorers, self.explorers)
        return result


class Chain:
    id: str
    schema: str
    title: str
    description: str
    type: str
    required: List[str]
    properties: ChainProperties
    defs: Defs

    def __init__(self, id: str, schema: str, title: str, description: str, type: str, required: List[str], properties: ChainProperties, defs: Defs) -> None:
        self.id = id
        self.schema = schema
        self.title = title
        self.description = description
        self.type = type
        self.required = required
        self.properties = properties
        self.defs = defs

    @staticmethod
    def from_dict(obj: Any) -> 'Chain':
        assert isinstance(obj, dict)
        id = from_str(obj.get("$id"))
        schema = from_str(obj.get("$schema"))
        title = from_str(obj.get("title"))
        description = from_str(obj.get("description"))
        type = from_str(obj.get("type"))
        required = from_list(from_str, obj.get("required"))
        properties = ChainProperties.from_dict(obj.get("properties"))
        defs = Defs.from_dict(obj.get("$defs"))
        return Chain(id, schema, title, description, type, required, properties, defs)

    def to_dict(self) -> dict:
        result: dict = {}
        result["$id"] = from_str(self.id)
        result["$schema"] = from_str(self.schema)
        result["title"] = from_str(self.title)
        result["description"] = from_str(self.description)
        result["type"] = from_str(self.type)
        result["required"] = from_list(from_str, self.required)
        result["properties"] = to_class(ChainProperties, self.properties)
        result["$defs"] = to_class(Defs, self.defs)
        return result


def chain_from_dict(s: Any) -> Chain:
    return Chain.from_dict(s)


def chain_to_dict(x: Chain) -> Any:
    return to_class(Chain, x)
