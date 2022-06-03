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

type Assetlist struct {
	ID          string              `json:"$id"`        
	Schema      string              `json:"$schema"`    
	Title       string              `json:"title"`      
	Description string              `json:"description"`
	Type        string              `json:"type"`       
	Required    []string            `json:"required"`   
	Properties  AssetlistProperties `json:"properties"` 
	Defs        Defs                `json:"$defs"`      
}

type Defs struct {
	Asset     Asset     `json:"asset"`     
	DenomUnit DenomUnit `json:"denom_unit"`
}

type Asset struct {
	Type       string          `json:"type"`      
	Required   []string        `json:"required"`  
	Properties AssetProperties `json:"properties"`
	If         If              `json:"if"`        
	Then       Then            `json:"then"`      
}

type If struct {
	Properties IfProperties `json:"properties"`
	Required   []string     `json:"required"`  
}

type IfProperties struct {
	TypeAsset PurpleTypeAsset `json:"type_asset"`
}

type PurpleTypeAsset struct {
	Enum []string `json:"enum"`
}

type AssetProperties struct {
	Description Address         `json:"description"` 
	DenomUnits  Assets          `json:"denom_units"` 
	TypeAsset   FluffyTypeAsset `json:"type_asset"`  
	Address     Address         `json:"address"`     
	Base        Address         `json:"base"`        
	Name        Address         `json:"name"`        
	Display     Address         `json:"display"`     
	Symbol      Address         `json:"symbol"`      
	Ibc         Ibc             `json:"ibc"`         
	LogoURIs    LogoURIs        `json:"logo_URIs"`   
	CoingeckoID Address         `json:"coingecko_id"`
}

type Address struct {
	Type        string `json:"type"`       
	Description string `json:"description"`
}

type Assets struct {
	Type  string `json:"type"` 
	Items Items  `json:"items"`
}

type Items struct {
	Ref string `json:"$ref"`
}

type Ibc struct {
	Type        string        `json:"type"`       
	Description string        `json:"description"`
	Properties  IbcProperties `json:"properties"` 
	Required    []string      `json:"required"`   
}

type IbcProperties struct {
	SourceChannel ChainName `json:"source_channel"`
	DstChannel    ChainName `json:"dst_channel"`   
	SourceDenom   ChainName `json:"source_denom"`  
}

type ChainName struct {
	Type string `json:"type"`
}

type LogoURIs struct {
	Type       string             `json:"type"`      
	Properties LogoURIsProperties `json:"properties"`
}

type LogoURIsProperties struct {
	PNG PNG `json:"png"`
	SVG PNG `json:"svg"`
}

type PNG struct {
	Type   string `json:"type"`  
	Format string `json:"format"`
}

type FluffyTypeAsset struct {
	Type        string   `json:"type"`       
	Enum        []string `json:"enum"`       
	Default     string   `json:"default"`    
	Description string   `json:"description"`
}

type Then struct {
	Required []string `json:"required"`
}

type DenomUnit struct {
	Type       string              `json:"type"`      
	Properties DenomUnitProperties `json:"properties"`
	Required   []string            `json:"required"`  
}

type DenomUnitProperties struct {
	Denom    ChainName `json:"denom"`   
	Exponent ChainName `json:"exponent"`
	Aliases  Aliases   `json:"aliases"` 
}

type Aliases struct {
	Type  string    `json:"type"` 
	Items ChainName `json:"items"`
}

type AssetlistProperties struct {
	ChainName ChainName `json:"chain_name"`
	Assets    Assets    `json:"assets"`    
}
