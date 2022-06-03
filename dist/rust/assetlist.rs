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
pub struct Assetlist {
    #[serde(rename = "type")]
    assetlist_type: String,

    #[serde(rename = "$defs")]
    defs: Defs,

    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "$id")]
    id: String,

    #[serde(rename = "properties")]
    properties: AssetlistProperties,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "$schema")]
    schema: String,

    #[serde(rename = "title")]
    title: String,
}

#[derive(Serialize, Deserialize)]
pub struct Defs {
    #[serde(rename = "asset")]
    asset: Asset,

    #[serde(rename = "denom_unit")]
    denom_unit: DenomUnit,
}

#[derive(Serialize, Deserialize)]
pub struct Asset {
    #[serde(rename = "if")]
    asset_if: If,

    #[serde(rename = "type")]
    asset_type: String,

    #[serde(rename = "properties")]
    properties: AssetProperties,

    #[serde(rename = "required")]
    required: Vec<String>,

    #[serde(rename = "then")]
    then: Then,
}

#[derive(Serialize, Deserialize)]
pub struct If {
    #[serde(rename = "properties")]
    properties: IfProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct IfProperties {
    #[serde(rename = "type_asset")]
    type_asset: PurpleTypeAsset,
}

#[derive(Serialize, Deserialize)]
pub struct PurpleTypeAsset {
    #[serde(rename = "enum")]
    type_asset_enum: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct AssetProperties {
    #[serde(rename = "address")]
    address: Address,

    #[serde(rename = "base")]
    base: Address,

    #[serde(rename = "coingecko_id")]
    coingecko_id: Address,

    #[serde(rename = "denom_units")]
    denom_units: Assets,

    #[serde(rename = "description")]
    description: Address,

    #[serde(rename = "display")]
    display: Address,

    #[serde(rename = "ibc")]
    ibc: Ibc,

    #[serde(rename = "logo_URIs")]
    logo_ur_is: LogoUrIs,

    #[serde(rename = "name")]
    name: Address,

    #[serde(rename = "symbol")]
    symbol: Address,

    #[serde(rename = "type_asset")]
    type_asset: FluffyTypeAsset,
}

#[derive(Serialize, Deserialize)]
pub struct Address {
    #[serde(rename = "type")]
    address_type: String,

    #[serde(rename = "description")]
    description: String,
}

#[derive(Serialize, Deserialize)]
pub struct Assets {
    #[serde(rename = "type")]
    assets_type: String,

    #[serde(rename = "items")]
    items: Items,
}

#[derive(Serialize, Deserialize)]
pub struct Items {
    #[serde(rename = "$ref")]
    items_ref: String,
}

#[derive(Serialize, Deserialize)]
pub struct Ibc {
    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "type")]
    ibc_type: String,

    #[serde(rename = "properties")]
    properties: IbcProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct IbcProperties {
    #[serde(rename = "dst_channel")]
    dst_channel: ChainName,

    #[serde(rename = "source_channel")]
    source_channel: ChainName,

    #[serde(rename = "source_denom")]
    source_denom: ChainName,
}

#[derive(Serialize, Deserialize)]
pub struct ChainName {
    #[serde(rename = "type")]
    chain_name_type: String,
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
    #[serde(rename = "format")]
    format: String,

    #[serde(rename = "type")]
    png_type: String,
}

#[derive(Serialize, Deserialize)]
pub struct FluffyTypeAsset {
    #[serde(rename = "description")]
    description: String,

    #[serde(rename = "default")]
    type_asset_default: String,

    #[serde(rename = "enum")]
    type_asset_enum: Vec<String>,

    #[serde(rename = "type")]
    type_asset_type: String,
}

#[derive(Serialize, Deserialize)]
pub struct Then {
    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct DenomUnit {
    #[serde(rename = "type")]
    denom_unit_type: String,

    #[serde(rename = "properties")]
    properties: DenomUnitProperties,

    #[serde(rename = "required")]
    required: Vec<String>,
}

#[derive(Serialize, Deserialize)]
pub struct DenomUnitProperties {
    #[serde(rename = "aliases")]
    aliases: Aliases,

    #[serde(rename = "denom")]
    denom: ChainName,

    #[serde(rename = "exponent")]
    exponent: ChainName,
}

#[derive(Serialize, Deserialize)]
pub struct Aliases {
    #[serde(rename = "type")]
    aliases_type: String,

    #[serde(rename = "items")]
    items: ChainName,
}

#[derive(Serialize, Deserialize)]
pub struct AssetlistProperties {
    #[serde(rename = "assets")]
    assets: Assets,

    #[serde(rename = "chain_name")]
    chain_name: ChainName,
}
