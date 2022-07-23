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

/// Cosmos Chain.json is a metadata file that contains information about a cosmos sdk based
/// chain.
#[derive(Serialize, Deserialize)]
pub struct Chain {
    #[serde(rename = "apis")]
    apis: Option<Apis>,

    #[serde(rename = "bech32_prefix")]
    bech32_prefix: String,

    #[serde(rename = "chain_id")]
    chain_id: String,

    #[serde(rename = "chain_name")]
    chain_name: String,

    #[serde(rename = "codebase")]
    codebase: Option<Codebase>,

    #[serde(rename = "daemon_name")]
    daemon_name: Option<String>,

    #[serde(rename = "explorers")]
    explorers: Option<Vec<ExplorerElement>>,

    #[serde(rename = "fees")]
    fees: Option<Fees>,

    #[serde(rename = "genesis")]
    genesis: Option<Genesis>,

    #[serde(rename = "key_algos")]
    key_algos: Option<Vec<KeyAlgo>>,

    #[serde(rename = "network_type")]
    network_type: Option<NetworkType>,

    #[serde(rename = "node_home")]
    node_home: Option<String>,

    #[serde(rename = "peers")]
    peers: Option<Peers>,

    #[serde(rename = "pretty_name")]
    pretty_name: Option<String>,

    #[serde(rename = "slip44")]
    slip44: Option<f64>,

    #[serde(rename = "status")]
    status: Option<Status>,
}

#[derive(Serialize, Deserialize)]
pub struct Apis {
    #[serde(rename = "grpc")]
    grpc: Option<Vec<GrpcElement>>,

    #[serde(rename = "rest")]
    rest: Option<Vec<GrpcElement>>,

    #[serde(rename = "rpc")]
    rpc: Option<Vec<GrpcElement>>,
}

#[derive(Serialize, Deserialize)]
pub struct GrpcElement {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "archive")]
    archive: Option<bool>,

    #[serde(rename = "provider")]
    provider: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Codebase {
    #[serde(rename = "binaries")]
    binaries: Option<Binaries>,

    #[serde(rename = "compatible_versions")]
    compatible_versions: Option<Vec<String>>,

    #[serde(rename = "cosmos_sdk_version")]
    cosmos_sdk_version: Option<String>,

    #[serde(rename = "cosmwasm_enabled")]
    cosmwasm_enabled: Option<bool>,

    #[serde(rename = "cosmwasm_version")]
    cosmwasm_version: Option<String>,

    #[serde(rename = "git_repo")]
    git_repo: Option<String>,

    #[serde(rename = "recommended_version")]
    recommended_version: Option<String>,

    #[serde(rename = "tendermint_version")]
    tendermint_version: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Binaries {
    #[serde(rename = "linux/amd")]
    linux_amd: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ExplorerElement {
    #[serde(rename = "account_page")]
    account_page: Option<String>,

    #[serde(rename = "kind")]
    kind: Option<String>,

    #[serde(rename = "tx_page")]
    tx_page: Option<String>,

    #[serde(rename = "url")]
    url: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Fees {
    #[serde(rename = "fee_tokens")]
    fee_tokens: Option<Vec<FeeTokenElement>>,
}

#[derive(Serialize, Deserialize)]
pub struct FeeTokenElement {
    #[serde(rename = "average_gas_price")]
    average_gas_price: Option<f64>,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "fixed_min_gas_price")]
    fixed_min_gas_price: Option<f64>,

    #[serde(rename = "high_gas_price")]
    high_gas_price: Option<f64>,

    #[serde(rename = "low_gas_price")]
    low_gas_price: Option<f64>,
}

#[derive(Serialize, Deserialize)]
pub struct Genesis {
    #[serde(rename = "genesis_url")]
    genesis_url: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Peers {
    #[serde(rename = "persistent_peers")]
    persistent_peers: Option<Vec<PersistentPeerElement>>,

    #[serde(rename = "seeds")]
    seeds: Option<Vec<PersistentPeerElement>>,
}

#[derive(Serialize, Deserialize)]
pub struct PersistentPeerElement {
    #[serde(rename = "address")]
    address: String,

    #[serde(rename = "id")]
    id: String,

    #[serde(rename = "provider")]
    provider: Option<String>,
}

#[derive(Serialize, Deserialize)]
pub enum KeyAlgo {
    #[serde(rename = "ed25519")]
    Ed25519,

    #[serde(rename = "ethsecp256k1")]
    Ethsecp256K1,

    #[serde(rename = "secp256k1")]
    Secp256K1,

    #[serde(rename = "sr25519")]
    Sr25519,
}

#[derive(Serialize, Deserialize)]
pub enum NetworkType {
    #[serde(rename = "mainnet")]
    Mainnet,

    #[serde(rename = "testnet")]
    Testnet,
}

#[derive(Serialize, Deserialize)]
pub enum Status {
    #[serde(rename = "killed")]
    Killed,

    #[serde(rename = "live")]
    Live,

    #[serde(rename = "upcoming")]
    Upcoming,
}
