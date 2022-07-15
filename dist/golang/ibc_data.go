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
	Chain1   map[string]interface{} `json:"chain-1"` // Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in; alphabetical order.
	Chain2   map[string]interface{} `json:"chain-2"` // Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in; alphabetical order.
	Channels []Channel              `json:"channels"`
	Defs     interface{}            `json:"$defs"`   
}

type Channel struct {
	Chain1      map[string]interface{} `json:"chain-1"`              
	Chain2      map[string]interface{} `json:"chain-2"`              
	Description *string                `json:"description,omitempty"`// Human readable description of the channel.
	Ordering    Ordering               `json:"ordering"`             // Determines if packets from a sending module must be 'ordered' or 'unordered'.
	Tags        *Tags                  `json:"tags,omitempty"`       // Human readable key:value pairs that help describe and distinguish channels.
	Version     string                 `json:"version"`              // IBC Version
}

// Human readable key:value pairs that help describe and distinguish channels.
type Tags struct {
	Dex        *string `json:"dex,omitempty"`       
	Preferred  *bool   `json:"preferred,omitempty"` 
	Properties *string `json:"properties,omitempty"`// String that helps describe non-dex use cases ex: interchain accounts(ICA).
	Status     *Status `json:"status,omitempty"`    
}

// Determines if packets from a sending module must be 'ordered' or 'unordered'.
type Ordering string
const (
	Ordered Ordering = "ordered"
	Unordered Ordering = "unordered"
)

type Status string
const (
	Killed Status = "killed"
	Live Status = "live"
	Upcoming Status = "upcoming"
)
