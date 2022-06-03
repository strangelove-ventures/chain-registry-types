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
	ID          string          `json:"$id"`        
	Schema      string          `json:"$schema"`    
	Title       string          `json:"title"`      
	Description string          `json:"description"`
	Type        string          `json:"type"`       
	Required    []string        `json:"required"`   
	Properties  ChainProperties `json:"properties"` 
	Defs        Defs            `json:"$defs"`      
}

type Defs struct {
	Peer     Peer     `json:"peer"`     
	Endpoint Endpoint `json:"endpoint"` 
	Explorer Explorer `json:"explorer"` 
	FeeToken FeeToken `json:"fee_token"`
	LogoURIs LogoURIs `json:"logo_URIs"`
}

type Endpoint struct {
	Type       string             `json:"type"`      
	Required   []string           `json:"required"`  
	Properties EndpointProperties `json:"properties"`
}

type EndpointProperties struct {
	Address  Bech32Prefix `json:"address"` 
	Provider Bech32Prefix `json:"provider"`
}

type Bech32Prefix struct {
	Type Type `json:"type"`
}

type Explorer struct {
	Type       string             `json:"type"`      
	Properties ExplorerProperties `json:"properties"`
}

type ExplorerProperties struct {
	Kind        Bech32Prefix `json:"kind"`        
	URL         Bech32Prefix `json:"url"`         
	TxPage      Bech32Prefix `json:"tx_page"`     
	AccountPage Bech32Prefix `json:"account_page"`
}

type FeeToken struct {
	Type       string             `json:"type"`      
	Required   []string           `json:"required"`  
	Properties FeeTokenProperties `json:"properties"`
}

type FeeTokenProperties struct {
	Denom            Bech32Prefix `json:"denom"`              
	FixedMinGasPrice Bech32Prefix `json:"fixed_min_gas_price"`
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
	Type   Type   `json:"type"`  
	Format string `json:"format"`
}

type Peer struct {
	Type       string         `json:"type"`      
	Required   []string       `json:"required"`  
	Properties PeerProperties `json:"properties"`
}

type PeerProperties struct {
	ID       Bech32Prefix `json:"id"`      
	Address  Bech32Prefix `json:"address"` 
	Provider Bech32Prefix `json:"provider"`
}

type ChainProperties struct {
	ChainName    Bech32Prefix `json:"chain_name"`   
	ChainID      Bech32Prefix `json:"chain_id"`     
	PrettyName   Bech32Prefix `json:"pretty_name"`  
	Status       NetworkType  `json:"status"`       
	NetworkType  NetworkType  `json:"network_type"` 
	Bech32Prefix Bech32Prefix `json:"bech32_prefix"`
	Genesis      Genesis      `json:"genesis"`      
	DaemonName   Bech32Prefix `json:"daemon_name"`  
	NodeHome     Bech32Prefix `json:"node_home"`    
	KeyAlgos     KeyAlgos     `json:"key_algos"`    
	Slip44       Bech32Prefix `json:"slip44"`       
	Fees         Fees         `json:"fees"`         
	Codebase     Codebase     `json:"codebase"`     
	Peers        Peers        `json:"peers"`        
	Apis         Apis         `json:"apis"`         
	Explorers    Explorers    `json:"explorers"`    
}

type Apis struct {
	Type       string         `json:"type"`      
	Properties ApisProperties `json:"properties"`
}

type ApisProperties struct {
	RPC  Explorers `json:"rpc"` 
	REST Explorers `json:"rest"`
	Grpc Explorers `json:"grpc"`
}

type Explorers struct {
	Type  string         `json:"type"` 
	Items ExplorersItems `json:"items"`
}

type ExplorersItems struct {
	Ref string `json:"$ref"`
}

type Codebase struct {
	Type       string             `json:"type"`      
	Required   []string           `json:"required"`  
	Properties CodebaseProperties `json:"properties"`
}

type CodebaseProperties struct {
	GitRepo            PNG                `json:"git_repo"`           
	RecommendedVersion Bech32Prefix       `json:"recommended_version"`
	CompatibleVersions CompatibleVersions `json:"compatible_versions"`
	Binaries           Binaries           `json:"binaries"`           
}

type Binaries struct {
	Type       string             `json:"type"`      
	Properties BinariesProperties `json:"properties"`
}

type BinariesProperties struct {
	LinuxAMD PNG `json:"linux/amd"`
}

type CompatibleVersions struct {
	Type  string       `json:"type"` 
	Items Bech32Prefix `json:"items"`
}

type Fees struct {
	Type       string         `json:"type"`      
	Properties FeesProperties `json:"properties"`
}

type FeesProperties struct {
	FeeTokens Explorers `json:"fee_tokens"`
}

type Genesis struct {
	Type       string            `json:"type"`      
	Properties GenesisProperties `json:"properties"`
}

type GenesisProperties struct {
	GenesisURL Bech32Prefix `json:"genesis_url"`
}

type KeyAlgos struct {
	Type  string        `json:"type"` 
	Items KeyAlgosItems `json:"items"`
}

type KeyAlgosItems struct {
	Type        Type     `json:"type"`       
	Enum        []string `json:"enum"`       
	UniqueItems bool     `json:"uniqueItems"`
}

type NetworkType struct {
	Enum []string `json:"enum"`
}

type Peers struct {
	Type       string          `json:"type"`      
	Properties PeersProperties `json:"properties"`
}

type PeersProperties struct {
	Seeds           Explorers `json:"seeds"`           
	PersistentPeers Explorers `json:"persistent_peers"`
}

type Type string
const (
	Number Type = "number"
	String Type = "string"
)
