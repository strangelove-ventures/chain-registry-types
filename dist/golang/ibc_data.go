// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    ibcData, err := UnmarshalIbcData(bytes)
//    bytes, err = ibcData.Marshal()

package main

import "encoding/json"

func UnmarshalIbcData(data []byte) (IbcData, error) {
	var r IbcData
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *IbcData) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type IbcData struct {
	Properties IbcDataProperties `json:"properties"`
	Required   []string          `json:"required"`  
	Schema     string            `json:"$schema"`   
	Type       string            `json:"type"`      
}

type IbcDataProperties struct {
	Chain1   PurpleChain `json:"chain-1"` 
	Chain2   PurpleChain `json:"chain-2"` 
	Channels Channels    `json:"channels"`
	Defs     Defs        `json:"$defs"`   
}

type PurpleChain struct {
	Description string `json:"description"`
	Items       Items  `json:"items"`      
	Type        string `json:"type"`       
}

type Items struct {
	Refs string `json:"$refs"`
}

type Channels struct {
	Items []Item `json:"items"`
	Type  string `json:"type"` 
}

type Item struct {
	Properties ItemProperties `json:"properties"`
	Required   []string       `json:"required"`  
	Type       string         `json:"type"`      
}

type ItemProperties struct {
	Chain1      FluffyChain `json:"chain-1"`    
	Chain2      FluffyChain `json:"chain-2"`    
	Description ClientID    `json:"description"`
	Ordering    Ordering    `json:"ordering"`   
	Tags        Tags        `json:"tags"`       
	Version     ClientID    `json:"version"`    
}

type FluffyChain struct {
	Items Items  `json:"items"`
	Type  string `json:"type"` 
}

type ClientID struct {
	Description string `json:"description"`
	Type        string `json:"type"`       
}

type Ordering struct {
	Description string   `json:"description"`
	Enum        []string `json:"enum"`       
}

type Tags struct {
	Description string         `json:"description"`
	Properties  TagsProperties `json:"properties"` 
	Type        string         `json:"type"`       
}

type TagsProperties struct {
	Dex        ChainName `json:"dex"`       
	Preferred  ChainName `json:"preferred"` 
	Properties ClientID  `json:"properties"`
	Status     Status    `json:"status"`    
}

type ChainName struct {
	Type string `json:"type"`
}

type Status struct {
	Enum []string `json:"enum"`
}

type Defs struct {
	ChainInfo   ChainInfo   `json:"chain_info"`  
	ChannelInfo ChannelInfo `json:"channel_info"`
}

type ChainInfo struct {
	Properties ChainInfoProperties `json:"properties"`
	Required   []string            `json:"required"`  
	Type       string              `json:"type"`      
}

type ChainInfoProperties struct {
	ChainName    ChainName `json:"chain-name"`   
	ClientID     ClientID  `json:"client-id"`    
	ConnectionID ClientID  `json:"connection-id"`
}

type ChannelInfo struct {
	Properties ChannelInfoProperties `json:"properties"`
	Required   []string              `json:"required"`  
	Type       string                `json:"type"`      
}

type ChannelInfoProperties struct {
	ChannelID ClientID `json:"channel-id"`
	PortID    ClientID `json:"port-id"`   
}
