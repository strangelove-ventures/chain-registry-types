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
use std::collections::HashMap;

#[derive(Serialize, Deserialize)]
pub struct IbcData {
    /// Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
    /// alphabetical order.
    #[serde(rename = "chain-1")]
    chain_1: HashMap<String, Option<serde_json::Value>>,

    /// Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
    /// alphabetical order.
    #[serde(rename = "chain-2")]
    chain_2: HashMap<String, Option<serde_json::Value>>,

    #[serde(rename = "channels")]
    channels: Vec<Channel>,

    #[serde(rename = "$defs")]
    defs: Option<serde_json::Value>,
}

#[derive(Serialize, Deserialize)]
pub struct Channel {
    #[serde(rename = "chain-1")]
    chain_1: HashMap<String, Option<serde_json::Value>>,

    #[serde(rename = "chain-2")]
    chain_2: HashMap<String, Option<serde_json::Value>>,

    /// Human readable description of the channel.
    #[serde(rename = "description")]
    description: Option<String>,

    /// Determines if packets from a sending module must be 'ordered' or 'unordered'.
    #[serde(rename = "ordering")]
    ordering: Ordering,

    /// Human readable key:value pairs that help describe and distinguish channels.
    #[serde(rename = "tags")]
    tags: Option<Tags>,

    /// IBC Version
    #[serde(rename = "version")]
    version: String,
}

/// Human readable key:value pairs that help describe and distinguish channels.
#[derive(Serialize, Deserialize)]
pub struct Tags {
    #[serde(rename = "dex")]
    dex: Option<String>,

    #[serde(rename = "preferred")]
    preferred: Option<bool>,

    /// String that helps describe non-dex use cases ex: interchain accounts(ICA).
    #[serde(rename = "properties")]
    properties: Option<String>,

    #[serde(rename = "status")]
    status: Option<Status>,
}

/// Determines if packets from a sending module must be 'ordered' or 'unordered'.
#[derive(Serialize, Deserialize)]
pub enum Ordering {
    #[serde(rename = "ordered")]
    Ordered,

    #[serde(rename = "unordered")]
    Unordered,
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
