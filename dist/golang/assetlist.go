// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    assetlist, err := UnmarshalAssetlist(bytes)
//    bytes, err = assetlist.Marshal()

package main

import "encoding/json"

func UnmarshalAssetlist(data []byte) (Assetlist, error) {
	var r Assetlist
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Assetlist) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

// Asset lists are a similar mechanism to allow frontends and other UIs to fetch metadata
// associated with Cosmos SDK denoms, especially for assets sent over IBC.
type Assetlist struct {
	Assets    []AssetElement `json:"assets"`    
	ChainName string         `json:"chain_name"`
}

type AssetElement struct {
	Address     *string            `json:"address,omitempty"`     // [OPTIONAL] The address of the asset. Only required for type_asset : cw20, snip20
	Base        string             `json:"base"`                  // The base unit of the asset. Must be in denom_units.
	CoingeckoID *string            `json:"coingecko_id,omitempty"`// [OPTIONAL] The coingecko id to fetch asset data from coingecko v3 api. See; https://api.coingecko.com/api/v3/coins/list
	DenomUnits  []DenomUnitElement `json:"denom_units"`           
	Description *string            `json:"description,omitempty"` // [OPTIONAL] A short description of the asset
	Display     string             `json:"display"`               // The human friendly unit of the asset. Must be in denom_units.
	Ibc         *Ibc               `json:"ibc,omitempty"`         // [OPTIONAL] IBC Channel between src and dst between chain
	LogoURIs    *LogoURIs          `json:"logo_URIs,omitempty"`   
	Name        string             `json:"name"`                  // The project name of the asset. For example Bitcoin.
	Symbol      string             `json:"symbol"`                // The symbol of an asset. For example BTC.
	TypeAsset   *TypeAsset         `json:"type_asset,omitempty"`  // [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
}

type DenomUnitElement struct {
	Aliases  []string `json:"aliases,omitempty"`
	Denom    string   `json:"denom"`            
	Exponent int64    `json:"exponent"`         
}

// [OPTIONAL] IBC Channel between src and dst between chain
type Ibc struct {
	DstChannel    string `json:"dst_channel"`   
	SourceChannel string `json:"source_channel"`
	SourceDenom   string `json:"source_denom"`  
}

type LogoURIs struct {
	PNG *string `json:"png,omitempty"`
	SVG *string `json:"svg,omitempty"`
}

// [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
type TypeAsset string
const (
	Cw20 TypeAsset = "cw20"
	Erc20 TypeAsset = "erc20"
	SDKCoin TypeAsset = "sdk.coin"
	Snip20 TypeAsset = "snip20"
)
