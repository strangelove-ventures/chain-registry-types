// Example code that deserializes and serializes the model.
// extern crate serde;
// #[macro_use]
// extern crate serde_derive;
// extern crate serde_json;
//
// use generated_module::[object Object];
//
// fn main() {
//     let json = r#"{"answer": 42}"#;
//     let model: [object Object] = serde_json::from_str(&json).unwrap();
// }

extern crate serde_derive;

#[derive(Serialize, Deserialize)]
pub struct Chain {
    #[serde(rename = "$id")]
    id: String,

    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "title")]
    title: String,

    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "type")]
    chain_type: String,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "properties")]
    properties: ChainProperties,

    #[serde(rename = "$defs")]
    defs: Defs,
}

#[derive(Serialize, Deserialize)]
pub struct Defs {
    #[serde(rename = "peer")]
    peer: Peer,

    #[serde(rename = "endpoint")]
    endpoint: Endpoint,

    #[serde(rename = "explorer")]
    explorer: Explorer,

    #[serde(rename = "fee_token")]
    fee_token: FeeToken,

    #[serde(rename = "logo_URIs")]
    logo_ur_is: LogoUrIs,
}

#[derive(Serialize, Deserialize)]
pub struct Endpoint {
    #[serde(rename = "type")]
    endpoint_type: String,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "properties")]
    properties: EndpointProperties,
}

#[derive(Serialize, Deserialize)]
pub struct EndpointProperties {
    #[serde(rename = "address")]
    address: Bech32Prefix,

    #[serde(rename = "provider")]
    provider: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct Bech32Prefix {
    #[serde(rename = "type")]
    bech32_prefix_type: Type,
}

#[derive(Serialize, Deserialize)]
pub struct Explorer {
    #[serde(rename = "type")]
    explorer_type: String,

    #[serde(rename = "properties")]
    properties: ExplorerProperties,
}

#[derive(Serialize, Deserialize)]
pub struct ExplorerProperties {
    #[serde(rename = "kind")]
    kind: Bech32Prefix,

    #[serde(rename = "url")]
    url: Bech32Prefix,

    #[serde(rename = "tx_page")]
    tx_page: Bech32Prefix,

    #[serde(rename = "account_page")]
    account_page: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct FeeToken {
    #[serde(rename = "type")]
    fee_token_type: String,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "properties")]
    properties: FeeTokenProperties,
}

#[derive(Serialize, Deserialize)]
pub struct FeeTokenProperties {
    #[serde(rename = "denom")]
    denom: Bech32Prefix,

    #[serde(rename = "fixed_min_gas_price")]
    fixed_min_gas_price: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct LogoUrIs {
    #[serde(rename = "type")]
    logo_ur_is_type: String,

    #[serde(rename = "properties")]
    properties: LogoUrIsProperties,
}

#[derive(Serialize, Deserialize)]
pub struct LogoUrIsProperties {
    #[serde(rename = "png")]
    png: Png,

    #[serde(rename = "svg")]
    svg: Png,
}

#[derive(Serialize, Deserialize)]
pub struct Png {
    #[serde(rename = "type")]
    png_type: Type,

    #[serde(rename = "format")]
    format: String,
}

#[derive(Serialize, Deserialize)]
pub struct Peer {
    #[serde(rename = "type")]
    peer_type: String,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "properties")]
    properties: PeerProperties,
}

#[derive(Serialize, Deserialize)]
pub struct PeerProperties {
    #[serde(rename = "id")]
    id: Bech32Prefix,

    #[serde(rename = "address")]
    address: Bech32Prefix,

    #[serde(rename = "provider")]
    provider: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct ChainProperties {
    #[serde(rename = "chain_name")]
    chain_name: Bech32Prefix,

    #[serde(rename = "chain_id")]
    chain_id: Bech32Prefix,

    #[serde(rename = "pretty_name")]
    pretty_name: Bech32Prefix,

    #[serde(rename = "status")]
    status: NetworkType,

    #[serde(rename = "network_type")]
    network_type: NetworkType,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: Bech32Prefix,

    #[serde(rename = "genesis")]
    genesis: Genesis,

    #[serde(rename = "daemon_name")]
    daemon_name: Bech32Prefix,

    #[serde(rename = "node_home")]
    node_home: Bech32Prefix,

    #[serde(rename = "key_algos")]
    key_algos: KeyAlgos,

    #[serde(rename = "slip44")]
    slip44: Bech32Prefix,

    #[serde(rename = "fees")]
    fees: Fees,

    #[serde(rename = "codebase")]
    codebase: Codebase,

    #[serde(rename = "peers")]
    peers: Peers,

    #[serde(rename = "apis")]
    apis: Apis,

    #[serde(rename = "explorers")]
    explorers: Explorers,
}

#[derive(Serialize, Deserialize)]
pub struct Apis {
    #[serde(rename = "type")]
    apis_type: String,

    #[serde(rename = "properties")]
    properties: ApisProperties,
}

#[derive(Serialize, Deserialize)]
pub struct ApisProperties {
    #[serde(rename = "rpc")]
    rpc: Explorers,

    #[serde(rename = "rest")]
    rest: Explorers,

    #[serde(rename = "grpc")]
    grpc: Explorers,
}

#[derive(Serialize, Deserialize)]
pub struct Explorers {
    #[serde(rename = "type")]
    explorers_type: String,

    #[serde(rename = "items")]
    items: ExplorersItems,
}

#[derive(Serialize, Deserialize)]
pub struct ExplorersItems {
    #[serde(rename = "$ref")]
    items_ref: String,
}

#[derive(Serialize, Deserialize)]
pub struct Codebase {
    #[serde(rename = "type")]
    codebase_type: String,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "properties")]
    properties: CodebaseProperties,
}

#[derive(Serialize, Deserialize)]
pub struct CodebaseProperties {
    #[serde(rename = "git_repo")]
    git_repo: Png,

    #[serde(rename = "recommended_version")]
    recommended_version: Bech32Prefix,

    #[serde(rename = "compatible_versions")]
    compatible_versions: CompatibleVersions,

    #[serde(rename = "binaries")]
    binaries: Binaries,
}

#[derive(Serialize, Deserialize)]
pub struct Binaries {
    #[serde(rename = "type")]
    binaries_type: String,

    #[serde(rename = "properties")]
    properties: BinariesProperties,
}

#[derive(Serialize, Deserialize)]
pub struct BinariesProperties {
    #[serde(rename = "linux/amd")]
    linux_amd: Png,
}

#[derive(Serialize, Deserialize)]
pub struct CompatibleVersions {
    #[serde(rename = "type")]
    compatible_versions_type: String,

    #[serde(rename = "items")]
    items: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct Fees {
    #[serde(rename = "type")]
    fees_type: String,

    #[serde(rename = "properties")]
    properties: FeesProperties,
}

#[derive(Serialize, Deserialize)]
pub struct FeesProperties {
    #[serde(rename = "fee_tokens")]
    fee_tokens: Explorers,
}

#[derive(Serialize, Deserialize)]
pub struct Genesis {
    #[serde(rename = "type")]
    genesis_type: String,

    #[serde(rename = "properties")]
    properties: GenesisProperties,
}

#[derive(Serialize, Deserialize)]
pub struct GenesisProperties {
    #[serde(rename = "genesis_url")]
    genesis_url: Bech32Prefix,
}

#[derive(Serialize, Deserialize)]
pub struct KeyAlgos {
    #[serde(rename = "type")]
    key_algos_type: String,

    #[serde(rename = "items")]
    items: KeyAlgosItems,
}

#[derive(Serialize, Deserialize)]
pub struct KeyAlgosItems {
    #[serde(rename = "type")]
    items_type: Type,

    #[serde(rename = "enum")]
    items_enum: Vec<String>,

    #[serde(rename = "uniqueItems")]
    unique_items: bool,
}

#[derive(Serialize, Deserialize)]
pub struct NetworkType {
    #[serde(rename = "enum")]
    network_type_enum: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Peers {
    #[serde(rename = "type")]
    peers_type: String,

    #[serde(rename = "properties")]
    properties: PeersProperties,
}

#[derive(Serialize, Deserialize)]
pub struct PeersProperties {
    #[serde(rename = "seeds")]
    seeds: Explorers,

    #[serde(rename = "persistent_peers")]
    persistent_peers: Explorers,
}

#[derive(Serialize, Deserialize)]
pub enum Type {
    #[serde(rename = "number")]
    Number,

    #[serde(rename = "string")]
    String,
}
