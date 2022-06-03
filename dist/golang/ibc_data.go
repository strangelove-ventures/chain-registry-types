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
	Schema     string            `json:"$schema"`   
	Type       string            `json:"type"`      
	Required   []string          `json:"required"`  
	Properties IbcDataProperties `json:"properties"`
}

type IbcDataProperties struct {
	Chain1   PurpleChain `json:"chain-1"` 
	Chain2   PurpleChain `json:"chain-2"` 
	Channels Channels    `json:"channels"`
	Defs     Defs        `json:"$defs"`   
}

type PurpleChain struct {
	Type        string `json:"type"`       
	Description string `json:"description"`
	Items       Items  `json:"items"`      
}

type Items struct {
	Refs string `json:"$refs"`
}

type Channels struct {
	Type  string `json:"type"` 
	Items []Item `json:"items"`
}

type Item struct {
	Type       string         `json:"type"`      
	Required   []string       `json:"required"`  
	Properties ItemProperties `json:"properties"`
}

type ItemProperties struct {
	Chain1      FluffyChain `json:"chain-1"`    
	Chain2      FluffyChain `json:"chain-2"`    
	Ordering    Ordering    `json:"ordering"`   
	Version     ClientID    `json:"version"`    
	Description ClientID    `json:"description"`
	Tags        Tags        `json:"tags"`       
}

type FluffyChain struct {
	Type  string `json:"type"` 
	Items Items  `json:"items"`
}

type ClientID struct {
	Type        string `json:"type"`       
	Description string `json:"description"`
}

type Ordering struct {
	Enum        []string `json:"enum"`       
	Description string   `json:"description"`
}

type Tags struct {
	Type        string         `json:"type"`       
	Description string         `json:"description"`
	Properties  TagsProperties `json:"properties"` 
}

type TagsProperties struct {
	Status     Status    `json:"status"`    
	Preferred  ChainName `json:"preferred"` 
	Dex        ChainName `json:"dex"`       
	Properties ClientID  `json:"properties"`
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
	Type       string              `json:"type"`      
	Required   []string            `json:"required"`  
	Properties ChainInfoProperties `json:"properties"`
}

type ChainInfoProperties struct {
	ChainName    ChainName `json:"chain-name"`   
	ClientID     ClientID  `json:"client-id"`    
	ConnectionID ClientID  `json:"connection-id"`
}

type ChannelInfo struct {
	Type       string                `json:"type"`      
	Required   []string              `json:"required"`  
	Properties ChannelInfoProperties `json:"properties"`
}

type ChannelInfoProperties struct {
	ChannelID ClientID `json:"channel-id"`
	PortID    ClientID `json:"port-id"`   
}
