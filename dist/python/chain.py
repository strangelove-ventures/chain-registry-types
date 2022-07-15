# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = chain_from_dict(json.loads(json_string))

from typing import Optional, Any, List, TypeVar, Callable, Type, cast
from enum import Enum


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


class GrpcElement:
    address: str
    archive: Optional[bool]
    provider: Optional[str]

    def __init__(self, address: str, archive: Optional[bool], provider: Optional[str]) -> None:
        self.address = address
        self.archive = archive
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'GrpcElement':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        archive = from_union([from_bool, from_none], obj.get("archive"))
        provider = from_union([from_none, from_str], obj.get("provider"))
        return GrpcElement(address, archive, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["archive"] = from_union([from_bool, from_none], self.archive)
        result["provider"] = from_union([from_none, from_str], self.provider)
        return result


class Apis:
    grpc: Optional[List[GrpcElement]]
    rest: Optional[List[GrpcElement]]
    rpc: Optional[List[GrpcElement]]

    def __init__(self, grpc: Optional[List[GrpcElement]], rest: Optional[List[GrpcElement]], rpc: Optional[List[GrpcElement]]) -> None:
        self.grpc = grpc
        self.rest = rest
        self.rpc = rpc

    @staticmethod
    def from_dict(obj: Any) -> 'Apis':
        assert isinstance(obj, dict)
        grpc = from_union([lambda x: from_list(GrpcElement.from_dict, x), from_none], obj.get("grpc"))
        rest = from_union([lambda x: from_list(GrpcElement.from_dict, x), from_none], obj.get("rest"))
        rpc = from_union([lambda x: from_list(GrpcElement.from_dict, x), from_none], obj.get("rpc"))
        return Apis(grpc, rest, rpc)

    def to_dict(self) -> dict:
        result: dict = {}
        result["grpc"] = from_union([lambda x: from_list(lambda x: to_class(GrpcElement, x), x), from_none], self.grpc)
        result["rest"] = from_union([lambda x: from_list(lambda x: to_class(GrpcElement, x), x), from_none], self.rest)
        result["rpc"] = from_union([lambda x: from_list(lambda x: to_class(GrpcElement, x), x), from_none], self.rpc)
        return result


class Binaries:
    linux_amd: Optional[str]

    def __init__(self, linux_amd: Optional[str]) -> None:
        self.linux_amd = linux_amd

    @staticmethod
    def from_dict(obj: Any) -> 'Binaries':
        assert isinstance(obj, dict)
        linux_amd = from_union([from_none, from_str], obj.get("linux/amd"))
        return Binaries(linux_amd)

    def to_dict(self) -> dict:
        result: dict = {}
        result["linux/amd"] = from_union([from_none, from_str], self.linux_amd)
        return result


class Codebase:
    binaries: Optional[Binaries]
    compatible_versions: List[str]
    git_repo: str
    recommended_version: str

    def __init__(self, binaries: Optional[Binaries], compatible_versions: List[str], git_repo: str, recommended_version: str) -> None:
        self.binaries = binaries
        self.compatible_versions = compatible_versions
        self.git_repo = git_repo
        self.recommended_version = recommended_version

    @staticmethod
    def from_dict(obj: Any) -> 'Codebase':
        assert isinstance(obj, dict)
        binaries = from_union([Binaries.from_dict, from_none], obj.get("binaries"))
        compatible_versions = from_list(from_str, obj.get("compatible_versions"))
        git_repo = from_str(obj.get("git_repo"))
        recommended_version = from_str(obj.get("recommended_version"))
        return Codebase(binaries, compatible_versions, git_repo, recommended_version)

    def to_dict(self) -> dict:
        result: dict = {}
        result["binaries"] = from_union([lambda x: to_class(Binaries, x), from_none], self.binaries)
        result["compatible_versions"] = from_list(from_str, self.compatible_versions)
        result["git_repo"] = from_str(self.git_repo)
        result["recommended_version"] = from_str(self.recommended_version)
        return result


class ExplorerElement:
    account_page: Optional[str]
    kind: Optional[str]
    tx_page: Optional[str]
    url: Optional[str]

    def __init__(self, account_page: Optional[str], kind: Optional[str], tx_page: Optional[str], url: Optional[str]) -> None:
        self.account_page = account_page
        self.kind = kind
        self.tx_page = tx_page
        self.url = url

    @staticmethod
    def from_dict(obj: Any) -> 'ExplorerElement':
        assert isinstance(obj, dict)
        account_page = from_union([from_none, from_str], obj.get("account_page"))
        kind = from_union([from_none, from_str], obj.get("kind"))
        tx_page = from_union([from_none, from_str], obj.get("tx_page"))
        url = from_union([from_none, from_str], obj.get("url"))
        return ExplorerElement(account_page, kind, tx_page, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["account_page"] = from_union([from_none, from_str], self.account_page)
        result["kind"] = from_union([from_none, from_str], self.kind)
        result["tx_page"] = from_union([from_none, from_str], self.tx_page)
        result["url"] = from_union([from_none, from_str], self.url)
        return result


class FeeTokenElement:
    average_gas_price: Optional[float]
    denom: str
    fixed_min_gas_price: Optional[float]
    high_gas_price: Optional[float]
    low_gas_price: Optional[float]

    def __init__(self, average_gas_price: Optional[float], denom: str, fixed_min_gas_price: Optional[float], high_gas_price: Optional[float], low_gas_price: Optional[float]) -> None:
        self.average_gas_price = average_gas_price
        self.denom = denom
        self.fixed_min_gas_price = fixed_min_gas_price
        self.high_gas_price = high_gas_price
        self.low_gas_price = low_gas_price

    @staticmethod
    def from_dict(obj: Any) -> 'FeeTokenElement':
        assert isinstance(obj, dict)
        average_gas_price = from_union([from_float, from_none], obj.get("average_gas_price"))
        denom = from_str(obj.get("denom"))
        fixed_min_gas_price = from_union([from_float, from_none], obj.get("fixed_min_gas_price"))
        high_gas_price = from_union([from_float, from_none], obj.get("high_gas_price"))
        low_gas_price = from_union([from_float, from_none], obj.get("low_gas_price"))
        return FeeTokenElement(average_gas_price, denom, fixed_min_gas_price, high_gas_price, low_gas_price)

    def to_dict(self) -> dict:
        result: dict = {}
        result["average_gas_price"] = from_union([to_float, from_none], self.average_gas_price)
        result["denom"] = from_str(self.denom)
        result["fixed_min_gas_price"] = from_union([to_float, from_none], self.fixed_min_gas_price)
        result["high_gas_price"] = from_union([to_float, from_none], self.high_gas_price)
        result["low_gas_price"] = from_union([to_float, from_none], self.low_gas_price)
        return result


class Fees:
    fee_tokens: Optional[List[FeeTokenElement]]

    def __init__(self, fee_tokens: Optional[List[FeeTokenElement]]) -> None:
        self.fee_tokens = fee_tokens

    @staticmethod
    def from_dict(obj: Any) -> 'Fees':
        assert isinstance(obj, dict)
        fee_tokens = from_union([lambda x: from_list(FeeTokenElement.from_dict, x), from_none], obj.get("fee_tokens"))
        return Fees(fee_tokens)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fee_tokens"] = from_union([lambda x: from_list(lambda x: to_class(FeeTokenElement, x), x), from_none], self.fee_tokens)
        return result


class Genesis:
    genesis_url: Optional[str]

    def __init__(self, genesis_url: Optional[str]) -> None:
        self.genesis_url = genesis_url

    @staticmethod
    def from_dict(obj: Any) -> 'Genesis':
        assert isinstance(obj, dict)
        genesis_url = from_union([from_none, from_str], obj.get("genesis_url"))
        return Genesis(genesis_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["genesis_url"] = from_union([from_none, from_str], self.genesis_url)
        return result


class KeyAlgo(Enum):
    ED25519 = "ed25519"
    ETHSECP256_K1 = "ethsecp256k1"
    SECP256_K1 = "secp256k1"
    SR25519 = "sr25519"


class NetworkType(Enum):
    MAINNET = "mainnet"
    TESTNET = "testnet"


class PersistentPeerElement:
    address: str
    id: str
    provider: Optional[str]

    def __init__(self, address: str, id: str, provider: Optional[str]) -> None:
        self.address = address
        self.id = id
        self.provider = provider

    @staticmethod
    def from_dict(obj: Any) -> 'PersistentPeerElement':
        assert isinstance(obj, dict)
        address = from_str(obj.get("address"))
        id = from_str(obj.get("id"))
        provider = from_union([from_none, from_str], obj.get("provider"))
        return PersistentPeerElement(address, id, provider)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_str(self.address)
        result["id"] = from_str(self.id)
        result["provider"] = from_union([from_none, from_str], self.provider)
        return result


class Peers:
    persistent_peers: Optional[List[PersistentPeerElement]]
    seeds: Optional[List[PersistentPeerElement]]

    def __init__(self, persistent_peers: Optional[List[PersistentPeerElement]], seeds: Optional[List[PersistentPeerElement]]) -> None:
        self.persistent_peers = persistent_peers
        self.seeds = seeds

    @staticmethod
    def from_dict(obj: Any) -> 'Peers':
        assert isinstance(obj, dict)
        persistent_peers = from_union([lambda x: from_list(PersistentPeerElement.from_dict, x), from_none], obj.get("persistent_peers"))
        seeds = from_union([lambda x: from_list(PersistentPeerElement.from_dict, x), from_none], obj.get("seeds"))
        return Peers(persistent_peers, seeds)

    def to_dict(self) -> dict:
        result: dict = {}
        result["persistent_peers"] = from_union([lambda x: from_list(lambda x: to_class(PersistentPeerElement, x), x), from_none], self.persistent_peers)
        result["seeds"] = from_union([lambda x: from_list(lambda x: to_class(PersistentPeerElement, x), x), from_none], self.seeds)
        return result


class Status(Enum):
    KILLED = "killed"
    LIVE = "live"
    UPCOMING = "upcoming"


class Chain:
    """Cosmos Chain.json is a metadata file that contains information about a cosmos sdk based
    chain.
    """
    apis: Optional[Apis]
    bech32_prefix: str
    chain_id: str
    chain_name: str
    codebase: Optional[Codebase]
    daemon_name: Optional[str]
    explorers: Optional[List[ExplorerElement]]
    fees: Optional[Fees]
    genesis: Optional[Genesis]
    key_algos: Optional[List[KeyAlgo]]
    network_type: Optional[NetworkType]
    node_home: Optional[str]
    peers: Optional[Peers]
    pretty_name: Optional[str]
    slip44: Optional[float]
    status: Optional[Status]

    def __init__(self, apis: Optional[Apis], bech32_prefix: str, chain_id: str, chain_name: str, codebase: Optional[Codebase], daemon_name: Optional[str], explorers: Optional[List[ExplorerElement]], fees: Optional[Fees], genesis: Optional[Genesis], key_algos: Optional[List[KeyAlgo]], network_type: Optional[NetworkType], node_home: Optional[str], peers: Optional[Peers], pretty_name: Optional[str], slip44: Optional[float], status: Optional[Status]) -> None:
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
    def from_dict(obj: Any) -> 'Chain':
        assert isinstance(obj, dict)
        apis = from_union([Apis.from_dict, from_none], obj.get("apis"))
        bech32_prefix = from_str(obj.get("bech32_prefix"))
        chain_id = from_str(obj.get("chain_id"))
        chain_name = from_str(obj.get("chain_name"))
        codebase = from_union([Codebase.from_dict, from_none], obj.get("codebase"))
        daemon_name = from_union([from_none, from_str], obj.get("daemon_name"))
        explorers = from_union([lambda x: from_list(ExplorerElement.from_dict, x), from_none], obj.get("explorers"))
        fees = from_union([Fees.from_dict, from_none], obj.get("fees"))
        genesis = from_union([Genesis.from_dict, from_none], obj.get("genesis"))
        key_algos = from_union([lambda x: from_list(KeyAlgo, x), from_none], obj.get("key_algos"))
        network_type = from_union([NetworkType, from_none], obj.get("network_type"))
        node_home = from_union([from_none, from_str], obj.get("node_home"))
        peers = from_union([Peers.from_dict, from_none], obj.get("peers"))
        pretty_name = from_union([from_none, from_str], obj.get("pretty_name"))
        slip44 = from_union([from_float, from_none], obj.get("slip44"))
        status = from_union([Status, from_none], obj.get("status"))
        return Chain(apis, bech32_prefix, chain_id, chain_name, codebase, daemon_name, explorers, fees, genesis, key_algos, network_type, node_home, peers, pretty_name, slip44, status)

    def to_dict(self) -> dict:
        result: dict = {}
        result["apis"] = from_union([lambda x: to_class(Apis, x), from_none], self.apis)
        result["bech32_prefix"] = from_str(self.bech32_prefix)
        result["chain_id"] = from_str(self.chain_id)
        result["chain_name"] = from_str(self.chain_name)
        result["codebase"] = from_union([lambda x: to_class(Codebase, x), from_none], self.codebase)
        result["daemon_name"] = from_union([from_none, from_str], self.daemon_name)
        result["explorers"] = from_union([lambda x: from_list(lambda x: to_class(ExplorerElement, x), x), from_none], self.explorers)
        result["fees"] = from_union([lambda x: to_class(Fees, x), from_none], self.fees)
        result["genesis"] = from_union([lambda x: to_class(Genesis, x), from_none], self.genesis)
        result["key_algos"] = from_union([lambda x: from_list(lambda x: to_enum(KeyAlgo, x), x), from_none], self.key_algos)
        result["network_type"] = from_union([lambda x: to_enum(NetworkType, x), from_none], self.network_type)
        result["node_home"] = from_union([from_none, from_str], self.node_home)
        result["peers"] = from_union([lambda x: to_class(Peers, x), from_none], self.peers)
        result["pretty_name"] = from_union([from_none, from_str], self.pretty_name)
        result["slip44"] = from_union([to_float, from_none], self.slip44)
        result["status"] = from_union([lambda x: to_enum(Status, x), from_none], self.status)
        return result


def chain_from_dict(s: Any) -> Chain:
    return Chain.from_dict(s)


def chain_to_dict(x: Chain) -> Any:
    return to_class(Chain, x)
