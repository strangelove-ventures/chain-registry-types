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

/// Asset lists are a similar mechanism to allow frontends and other UIs to fetch metadata
/// associated with Cosmos SDK denoms, especially for assets sent over IBC.
#[derive(Serialize, Deserialize)]
pub struct Assetlist {
    #[serde(rename = "assets")]
    assets: Vec<AssetElement>,

    #[serde(rename = "chain_name")]
    chain_name: String,
}

#[derive(Serialize, Deserialize)]
pub struct AssetElement {
    /// [OPTIONAL] The address of the asset. Only required for type_asset : cw20, snip20
    #[serde(rename = "address")]
    address: Option<String>,

    /// The base unit of the asset. Must be in denom_units.
    #[serde(rename = "base")]
    base: String,

    /// [OPTIONAL] The coingecko id to fetch asset data from coingecko v3 api. See
    /// https://api.coingecko.com/api/v3/coins/list
    #[serde(rename = "coingecko_id")]
    coingecko_id: Option<String>,

    #[serde(rename = "denom_units")]
    denom_units: Vec<DenomUnitElement>,

    /// [OPTIONAL] A short description of the asset
    #[serde(rename = "description")]
    description: Option<String>,

    /// The human friendly unit of the asset. Must be in denom_units.
    #[serde(rename = "display")]
    display: String,

    /// [OPTIONAL] IBC Channel between src and dst between chain
    #[serde(rename = "ibc")]
    ibc: Option<Ibc>,

    #[serde(rename = "logo_URIs")]
    logo_ur_is: Option<LogoUrIs>,

    /// The project name of the asset. For example Bitcoin.
    #[serde(rename = "name")]
    name: String,

    /// The symbol of an asset. For example BTC.
    #[serde(rename = "symbol")]
    symbol: String,

    /// [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
    #[serde(rename = "type_asset")]
    type_asset: Option<TypeAsset>,
}

#[derive(Serialize, Deserialize)]
pub struct DenomUnitElement {
    #[serde(rename = "aliases")]
    aliases: Option<Vec<String>>,

    #[serde(rename = "denom")]
    denom: String,

    #[serde(rename = "exponent")]
    exponent: i64,
}

/// [OPTIONAL] IBC Channel between src and dst between chain
#[derive(Serialize, Deserialize)]
pub struct Ibc {
    #[serde(rename = "dst_channel")]
    dst_channel: String,

    #[serde(rename = "source_channel")]
    source_channel: String,

    #[serde(rename = "source_denom")]
    source_denom: String,
}

#[derive(Serialize, Deserialize)]
pub struct LogoUrIs {
    #[serde(rename = "png")]
    png: Option<String>,

    #[serde(rename = "svg")]
    svg: Option<String>,
}

/// [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
#[derive(Serialize, Deserialize)]
pub enum TypeAsset {
    #[serde(rename = "cw20")]
    Cw20,

    #[serde(rename = "erc20")]
    Erc20,

    #[serde(rename = "sdk.coin")]
    SdkCoin,

    #[serde(rename = "snip20")]
    Snip20,
}
