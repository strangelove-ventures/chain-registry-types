// This file was generated from JSON Schema using quicktype, do not modify it directly.
// To parse and unparse this JSON data, add this code to your project and do:
//
//    chain, err := UnmarshalChain(bytes)
//    bytes, err = chain.Marshal()

package main

import "encoding/json"

func UnmarshalChain(data []byte) (Chain, error) {
	var r Chain
	err := json.Unmarshal(data, &r)
	return r, err
}

func (r *Chain) Marshal() ([]byte, error) {
	return json.Marshal(r)
}

type Chain struct {
	Defs        Defs            `json:"$defs"`      
	Description string          `json:"description"`
	ID          string          `json:"$id"`        
	Properties  ChainProperties `json:"properties"` 
	Required    []string        `json:"required"`   
	Schema      string          `json:"$schema"`    
	Title       string          `json:"title"`      
	Type        string          `json:"type"`       
}

type Defs struct {
	Endpoint Endpoint `json:"endpoint"` 
	Explorer Explorer `json:"explorer"` 
	FeeToken FeeToken `json:"fee_token"`
	LogoURIs LogoURIs `json:"logo_URIs"`
	Peer     Peer     `json:"peer"`     
}

type Endpoint struct {
	Properties EndpointProperties `json:"properties"`
	Required   []string           `json:"required"`  
	Type       string             `json:"type"`      
}

type EndpointProperties struct {
	Address  Bech32Prefix `json:"address"` 
	Provider Bech32Prefix `json:"provider"`
}

type Bech32Prefix struct {
	Type Type `json:"type"`
}

type Explorer struct {
	Properties ExplorerProperties `json:"properties"`
	Type       string             `json:"type"`      
}

type ExplorerProperties struct {
	AccountPage Bech32Prefix `json:"account_page"`
	Kind        Bech32Prefix `json:"kind"`        
	TxPage      Bech32Prefix `json:"tx_page"`     
	URL         Bech32Prefix `json:"url"`         
}

type FeeToken struct {
	Properties FeeTokenProperties `json:"properties"`
	Required   []string           `json:"required"`  
	Type       string             `json:"type"`      
}

type FeeTokenProperties struct {
	Denom            Bech32Prefix `json:"denom"`              
	FixedMinGasPrice Bech32Prefix `json:"fixed_min_gas_price"`
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
	Type   Type   `json:"type"`  
}

type Peer struct {
	Properties PeerProperties `json:"properties"`
	Required   []string       `json:"required"`  
	Type       string         `json:"type"`      
}

type PeerProperties struct {
	Address  Bech32Prefix `json:"address"` 
	ID       Bech32Prefix `json:"id"`      
	Provider Bech32Prefix `json:"provider"`
}

type ChainProperties struct {
	Apis         Apis         `json:"apis"`         
	Bech32Prefix Bech32Prefix `json:"bech32_prefix"`
	ChainID      Bech32Prefix `json:"chain_id"`     
	ChainName    Bech32Prefix `json:"chain_name"`   
	Codebase     Codebase     `json:"codebase"`     
	DaemonName   Bech32Prefix `json:"daemon_name"`  
	Explorers    Explorers    `json:"explorers"`    
	Fees         Fees         `json:"fees"`         
	Genesis      Genesis      `json:"genesis"`      
	KeyAlgos     KeyAlgos     `json:"key_algos"`    
	NetworkType  NetworkType  `json:"network_type"` 
	NodeHome     Bech32Prefix `json:"node_home"`    
	Peers        Peers        `json:"peers"`        
	PrettyName   Bech32Prefix `json:"pretty_name"`  
	Slip44       Bech32Prefix `json:"slip44"`       
	Status       NetworkType  `json:"status"`       
}

type Apis struct {
	Properties ApisProperties `json:"properties"`
	Type       string         `json:"type"`      
}

type ApisProperties struct {
	Grpc Explorers `json:"grpc"`
	REST Explorers `json:"rest"`
	RPC  Explorers `json:"rpc"` 
}

type Explorers struct {
	Items ExplorersItems `json:"items"`
	Type  string         `json:"type"` 
}

type ExplorersItems struct {
	Ref string `json:"$ref"`
}

type Codebase struct {
	Properties CodebaseProperties `json:"properties"`
	Required   []string           `json:"required"`  
	Type       string             `json:"type"`      
}

type CodebaseProperties struct {
	Binaries           Binaries           `json:"binaries"`           
	CompatibleVersions CompatibleVersions `json:"compatible_versions"`
	GitRepo            PNG                `json:"git_repo"`           
	RecommendedVersion Bech32Prefix       `json:"recommended_version"`
}

type Binaries struct {
	Properties BinariesProperties `json:"properties"`
	Type       string             `json:"type"`      
}

type BinariesProperties struct {
	LinuxAMD PNG `json:"linux/amd"`
}

type CompatibleVersions struct {
	Items Bech32Prefix `json:"items"`
	Type  string       `json:"type"` 
}

type Fees struct {
	Properties FeesProperties `json:"properties"`
	Type       string         `json:"type"`      
}

type FeesProperties struct {
	FeeTokens Explorers `json:"fee_tokens"`
}

type Genesis struct {
	Properties GenesisProperties `json:"properties"`
	Type       string            `json:"type"`      
}

type GenesisProperties struct {
	GenesisURL Bech32Prefix `json:"genesis_url"`
}

type KeyAlgos struct {
	Items KeyAlgosItems `json:"items"`
	Type  string        `json:"type"` 
}

type KeyAlgosItems struct {
	Enum        []string `json:"enum"`       
	Type        Type     `json:"type"`       
	UniqueItems bool     `json:"uniqueItems"`
}

type NetworkType struct {
	Enum []string `json:"enum"`
}

type Peers struct {
	Properties PeersProperties `json:"properties"`
	Type       string          `json:"type"`      
}

type PeersProperties struct {
	PersistentPeers Explorers `json:"persistent_peers"`
	Seeds           Explorers `json:"seeds"`           
}

type Type string
const (
	Number Type = "number"
	String Type = "string"
)
