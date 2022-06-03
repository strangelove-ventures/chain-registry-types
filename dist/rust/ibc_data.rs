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
pub struct IbcData {
    #[serde(rename = "type")]
    ibc_data_type: String,

    #[serde(rename = "properties")]
    properties: IbcDataProperties,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "$schema")]
    schema: String,
}

#[derive(Serialize, Deserialize)]
pub struct IbcDataProperties {
    #[serde(rename = "chain-1")]
    chain_1: PurpleChain,

    #[serde(rename = "chain-2")]
    chain_2: PurpleChain,

    #[serde(rename = "channels")]
    channels: Channels,

    #[serde(rename = "$defs")]
    defs: Defs,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleChain {
    #[serde(rename = "type")]
    chain_type: String,

    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "items")]
    items: Items,
}

#[derive(Serialize, Deserialize)]
pub struct Items {
    #[serde(rename = "$refs")]
    refs: String,
}

#[derive(Serialize, Deserialize)]
pub struct Channels {
    #[serde(rename = "type")]
    channels_type: String,

    #[serde(rename = "items")]
    items: Vec<Item>,
}

#[derive(Serialize, Deserialize)]
pub struct Item {
    #[serde(rename = "type")]
    item_type: String,

    #[serde(rename = "properties")]
    properties: ItemProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ItemProperties {
    #[serde(rename = "chain-1")]
    chain_1: FluffyChain,

    #[serde(rename = "chain-2")]
    chain_2: FluffyChain,

    #[serde(rename = "description")]
    description: ClientId,

    #[serde(rename = "ordering")]
    ordering: Ordering,

    #[serde(rename = "tags")]
    tags: Tags,

    #[serde(rename = "version")]
    version: ClientId,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyChain {
    #[serde(rename = "type")]
    chain_type: String,

    #[serde(rename = "items")]
    items: Items,
}

#[derive(Serialize, Deserialize)]
pub struct ClientId {
    #[serde(rename = "type")]
    client_id_type: String,

    #[serde(rename = "description")]
    description: String,
}

#[derive(Serialize, Deserialize)]
pub struct Ordering {
    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "enum")]
    ordering_enum: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Tags {
    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "properties")]
    properties: TagsProperties,

    #[serde(rename = "type")]
    tags_type: String,
}

#[derive(Serialize, Deserialize)]
pub struct TagsProperties {
    #[serde(rename = "dex")]
    dex: ChainName,

    #[serde(rename = "preferred")]
    preferred: ChainName,

    #[serde(rename = "properties")]
    properties: ClientId,

    #[serde(rename = "status")]
    status: Status,
}

#[derive(Serialize, Deserialize)]
pub struct ChainName {
    #[serde(rename = "type")]
    chain_name_type: String,
}

#[derive(Serialize, Deserialize)]
pub struct Status {
    #[serde(rename = "enum")]
    status_enum: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct Defs {
    #[serde(rename = "chain_info")]
    chain_info: ChainInfo,

    #[serde(rename = "channel_info")]
    channel_info: ChannelInfo,
}

#[derive(Serialize, Deserialize)]
pub struct ChainInfo {
    #[serde(rename = "type")]
    chain_info_type: String,

    #[serde(rename = "properties")]
    properties: ChainInfoProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ChainInfoProperties {
    #[serde(rename = "chain-name")]
    chain_name: ChainName,

    #[serde(rename = "client-id")]
    client_id: ClientId,

    #[serde(rename = "connection-id")]
    connection_id: ClientId,
}

#[derive(Serialize, Deserialize)]
pub struct ChannelInfo {
    #[serde(rename = "type")]
    channel_info_type: String,

    #[serde(rename = "properties")]
    properties: ChannelInfoProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct ChannelInfoProperties {
    #[serde(rename = "channel-id")]
    channel_id: ClientId,

    #[serde(rename = "port-id")]
    port_id: ClientId,
}
