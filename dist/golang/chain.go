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

// Cosmos Chain.json is a metadata file that contains information about a cosmos sdk based
// chain.
type Chain struct {
	Apis         *Apis             `json:"apis,omitempty"`        
	Bech32Prefix string            `json:"bech32_prefix"`         
	ChainID      string            `json:"chain_id"`              
	ChainName    string            `json:"chain_name"`            
	Codebase     *Codebase         `json:"codebase,omitempty"`    
	DaemonName   *string           `json:"daemon_name,omitempty"` 
	Explorers    []ExplorerElement `json:"explorers,omitempty"`   
	Fees         *Fees             `json:"fees,omitempty"`        
	Genesis      *Genesis          `json:"genesis,omitempty"`     
	KeyAlgos     []KeyAlgo         `json:"key_algos,omitempty"`   
	NetworkType  *NetworkType      `json:"network_type,omitempty"`
	NodeHome     *string           `json:"node_home,omitempty"`   
	Peers        *Peers            `json:"peers,omitempty"`       
	PrettyName   *string           `json:"pretty_name,omitempty"` 
	Slip44       *float64          `json:"slip44,omitempty"`      
	Status       *Status           `json:"status,omitempty"`      
}

type Apis struct {
	Grpc []GrpcElement `json:"grpc,omitempty"`
	REST []GrpcElement `json:"rest,omitempty"`
	RPC  []GrpcElement `json:"rpc,omitempty"` 
}

type GrpcElement struct {
	Address  string  `json:"address"`           
	Archive  *bool   `json:"archive,omitempty"` 
	Provider *string `json:"provider,omitempty"`
}

type Codebase struct {
	Binaries           *Binaries `json:"binaries,omitempty"`           
	CompatibleVersions []string  `json:"compatible_versions,omitempty"`
	CosmosSDKVersion   *string   `json:"cosmos_sdk_version,omitempty"` 
	GitRepo            *string   `json:"git_repo,omitempty"`           
	RecommendedVersion *string   `json:"recommended_version,omitempty"`
	TendermintVersion  *string   `json:"tendermint_version,omitempty"` 
}

type Binaries struct {
	LinuxAMD *string `json:"linux/amd,omitempty"`
}

type ExplorerElement struct {
	AccountPage *string `json:"account_page,omitempty"`
	Kind        *string `json:"kind,omitempty"`        
	TxPage      *string `json:"tx_page,omitempty"`     
	URL         *string `json:"url,omitempty"`         
}

type Fees struct {
	FeeTokens []FeeTokenElement `json:"fee_tokens,omitempty"`
}

type FeeTokenElement struct {
	AverageGasPrice  *float64 `json:"average_gas_price,omitempty"`  
	Denom            string   `json:"denom"`                        
	FixedMinGasPrice *float64 `json:"fixed_min_gas_price,omitempty"`
	HighGasPrice     *float64 `json:"high_gas_price,omitempty"`     
	LowGasPrice      *float64 `json:"low_gas_price,omitempty"`      
}

type Genesis struct {
	GenesisURL *string `json:"genesis_url,omitempty"`
}

type Peers struct {
	PersistentPeers []PersistentPeerElement `json:"persistent_peers,omitempty"`
	Seeds           []PersistentPeerElement `json:"seeds,omitempty"`           
}

type PersistentPeerElement struct {
	Address  string  `json:"address"`           
	ID       string  `json:"id"`                
	Provider *string `json:"provider,omitempty"`
}

type KeyAlgo string
const (
	Ed25519 KeyAlgo = "ed25519"
	Ethsecp256K1 KeyAlgo = "ethsecp256k1"
	Secp256K1 KeyAlgo = "secp256k1"
	Sr25519 KeyAlgo = "sr25519"
)

type NetworkType string
const (
	Mainnet NetworkType = "mainnet"
	Testnet NetworkType = "testnet"
)

type Status string
const (
	Killed Status = "killed"
	Live Status = "live"
	Upcoming Status = "upcoming"
)
