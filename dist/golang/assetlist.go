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
	Defs        Defs                `json:"$defs"`      
	Description string              `json:"description"`
	ID          string              `json:"$id"`        
	Properties  AssetlistProperties `json:"properties"` 
	Required    []string            `json:"required"`   
	Schema      string              `json:"$schema"`    
	Title       string              `json:"title"`      
	Type        string              `json:"type"`       
}

type Defs struct {
	Asset     Asset     `json:"asset"`     
	DenomUnit DenomUnit `json:"denom_unit"`
}

type Asset struct {
	If         If              `json:"if"`        
	Properties AssetProperties `json:"properties"`
	Required   []string        `json:"required"`  
	Then       Then            `json:"then"`      
	Type       string          `json:"type"`      
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
	Address     Address         `json:"address"`     
	Base        Address         `json:"base"`        
	CoingeckoID Address         `json:"coingecko_id"`
	DenomUnits  Assets          `json:"denom_units"` 
	Description Address         `json:"description"` 
	Display     Address         `json:"display"`     
	Ibc         Ibc             `json:"ibc"`         
	LogoURIs    LogoURIs        `json:"logo_URIs"`   
	Name        Address         `json:"name"`        
	Symbol      Address         `json:"symbol"`      
	TypeAsset   FluffyTypeAsset `json:"type_asset"`  
}

type Address struct {
	Description string `json:"description"`
	Type        string `json:"type"`       
}

type Assets struct {
	Items Items  `json:"items"`
	Type  string `json:"type"` 
}

type Items struct {
	Ref string `json:"$ref"`
}

type Ibc struct {
	Description string        `json:"description"`
	Properties  IbcProperties `json:"properties"` 
	Required    []string      `json:"required"`   
	Type        string        `json:"type"`       
}

type IbcProperties struct {
	DstChannel    ChainName `json:"dst_channel"`   
	SourceChannel ChainName `json:"source_channel"`
	SourceDenom   ChainName `json:"source_denom"`  
}

type ChainName struct {
	Type string `json:"type"`
}

type LogoURIs struct {
	Properties LogoURIsProperties `json:"properties"`
	Type       string             `json:"type"`      
}

type LogoURIsProperties struct {
	PNG PNG `json:"png"`
	SVG PNG `json:"svg"`
}

type PNG struct {
	Format string `json:"format"`
	Type   string `json:"type"`  
}

type FluffyTypeAsset struct {
	Default     string   `json:"default"`    
	Description string   `json:"description"`
	Enum        []string `json:"enum"`       
	Type        string   `json:"type"`       
}

type Then struct {
	Required []string `json:"required"`
}

type DenomUnit struct {
	Properties DenomUnitProperties `json:"properties"`
	Required   []string            `json:"required"`  
	Type       string              `json:"type"`      
}

type DenomUnitProperties struct {
	Aliases  Aliases   `json:"aliases"` 
	Denom    ChainName `json:"denom"`   
	Exponent ChainName `json:"exponent"`
}

type Aliases struct {
	Items ChainName `json:"items"`
	Type  string    `json:"type"` 
}

type AssetlistProperties struct {
	Assets    Assets    `json:"assets"`    
	ChainName ChainName `json:"chain_name"`
}
