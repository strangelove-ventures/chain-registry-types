// To parse this data:
//
//   import { Convert, Chain } from "./file";
//
//   const chain = Convert.toChain(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Chain {
    $id:         string;
    $schema:     string;
    title:       string;
    description: string;
    type:        string;
    required:    string[];
    properties:  ChainProperties;
    $defs:       Defs;
}

export interface Defs {
    peer:      Peer;
    endpoint:  Endpoint;
    explorer:  Explorer;
    fee_token: FeeToken;
    logo_URIs: LogoURIs;
}

export interface Endpoint {
    type:       string;
    required:   string[];
    properties: EndpointProperties;
}

export interface EndpointProperties {
    address:  Bech32Prefix;
    provider: Bech32Prefix;
}

export interface Bech32Prefix {
    type: Type;
}

export enum Type {
    Number = "number",
    String = "string",
}

export interface Explorer {
    type:       string;
    properties: ExplorerProperties;
}

export interface ExplorerProperties {
    kind:         Bech32Prefix;
    url:          Bech32Prefix;
    tx_page:      Bech32Prefix;
    account_page: Bech32Prefix;
}

export interface FeeToken {
    type:       string;
    required:   string[];
    properties: FeeTokenProperties;
}

export interface FeeTokenProperties {
    denom:               Bech32Prefix;
    fixed_min_gas_price: Bech32Prefix;
}

export interface LogoURIs {
    type:       string;
    properties: LogoURIsProperties;
}

export interface LogoURIsProperties {
    png: PNG;
    svg: PNG;
}

export interface PNG {
    type:   Type;
    format: string;
}

export interface Peer {
    type:       string;
    required:   string[];
    properties: PeerProperties;
}

export interface PeerProperties {
    id:       Bech32Prefix;
    address:  Bech32Prefix;
    provider: Bech32Prefix;
}

export interface ChainProperties {
    chain_name:    Bech32Prefix;
    chain_id:      Bech32Prefix;
    pretty_name:   Bech32Prefix;
    status:        NetworkType;
    network_type:  NetworkType;
    bech32_prefix: Bech32Prefix;
    genesis:       Genesis;
    daemon_name:   Bech32Prefix;
    node_home:     Bech32Prefix;
    key_algos:     KeyAlgos;
    slip44:        Bech32Prefix;
    fees:          Fees;
    codebase:      Codebase;
    peers:         Peers;
    apis:          Apis;
    explorers:     Explorers;
}

export interface Apis {
    type:       string;
    properties: ApisProperties;
}

export interface ApisProperties {
    rpc:  Explorers;
    rest: Explorers;
    grpc: Explorers;
}

export interface Explorers {
    type:  string;
    items: ExplorersItems;
}

export interface ExplorersItems {
    $ref: string;
}

export interface Codebase {
    type:       string;
    required:   string[];
    properties: CodebaseProperties;
}

export interface CodebaseProperties {
    git_repo:            PNG;
    recommended_version: Bech32Prefix;
    compatible_versions: CompatibleVersions;
    binaries:            Binaries;
}

export interface Binaries {
    type:       string;
    properties: BinariesProperties;
}

export interface BinariesProperties {
    "linux/amd": PNG;
}

export interface CompatibleVersions {
    type:  string;
    items: Bech32Prefix;
}

export interface Fees {
    type:       string;
    properties: FeesProperties;
}

export interface FeesProperties {
    fee_tokens: Explorers;
}

export interface Genesis {
    type:       string;
    properties: GenesisProperties;
}

export interface GenesisProperties {
    genesis_url: Bech32Prefix;
}

export interface KeyAlgos {
    type:  string;
    items: KeyAlgosItems;
}

export interface KeyAlgosItems {
    type:        Type;
    enum:        string[];
    uniqueItems: boolean;
}

export interface NetworkType {
    enum: string[];
}

export interface Peers {
    type:       string;
    properties: PeersProperties;
}

export interface PeersProperties {
    seeds:            Explorers;
    persistent_peers: Explorers;
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toChain(json: string): Chain {
        return cast(JSON.parse(json), r("Chain"));
    }

    public static chainToJson(value: Chain): string {
        return JSON.stringify(uncast(value, r("Chain")), null, 2);
    }
}

function invalidValue(typ: any, val: any, key: any = ''): never {
    if (key) {
        throw Error(`Invalid value for key "${key}". Expected type ${JSON.stringify(typ)} but got ${JSON.stringify(val)}`);
    }
    throw Error(`Invalid value ${JSON.stringify(val)} for type ${JSON.stringify(typ)}`, );
}

function jsonToJSProps(typ: any): any {
    if (typ.jsonToJS === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.json] = { key: p.js, typ: p.typ });
        typ.jsonToJS = map;
    }
    return typ.jsonToJS;
}

function jsToJSONProps(typ: any): any {
    if (typ.jsToJSON === undefined) {
        const map: any = {};
        typ.props.forEach((p: any) => map[p.js] = { key: p.json, typ: p.typ });
        typ.jsToJSON = map;
    }
    return typ.jsToJSON;
}

function transform(val: any, typ: any, getProps: any, key: any = ''): any {
    function transformPrimitive(typ: string, val: any): any {
        if (typeof typ === typeof val) return val;
        return invalidValue(typ, val, key);
    }

    function transformUnion(typs: any[], val: any): any {
        // val must validate against one typ in typs
        const l = typs.length;
        for (let i = 0; i < l; i++) {
            const typ = typs[i];
            try {
                return transform(val, typ, getProps);
            } catch (_) {}
        }
        return invalidValue(typs, val);
    }

    function transformEnum(cases: string[], val: any): any {
        if (cases.indexOf(val) !== -1) return val;
        return invalidValue(cases, val);
    }

    function transformArray(typ: any, val: any): any {
        // val must be an array with no invalid elements
        if (!Array.isArray(val)) return invalidValue("array", val);
        return val.map(el => transform(el, typ, getProps));
    }

    function transformDate(val: any): any {
        if (val === null) {
            return null;
        }
        const d = new Date(val);
        if (isNaN(d.valueOf())) {
            return invalidValue("Date", val);
        }
        return d;
    }

    function transformObject(props: { [k: string]: any }, additional: any, val: any): any {
        if (val === null || typeof val !== "object" || Array.isArray(val)) {
            return invalidValue("object", val);
        }
        const result: any = {};
        Object.getOwnPropertyNames(props).forEach(key => {
            const prop = props[key];
            const v = Object.prototype.hasOwnProperty.call(val, key) ? val[key] : undefined;
            result[prop.key] = transform(v, prop.typ, getProps, prop.key);
        });
        Object.getOwnPropertyNames(val).forEach(key => {
            if (!Object.prototype.hasOwnProperty.call(props, key)) {
                result[key] = transform(val[key], additional, getProps, key);
            }
        });
        return result;
    }

    if (typ === "any") return val;
    if (typ === null) {
        if (val === null) return val;
        return invalidValue(typ, val);
    }
    if (typ === false) return invalidValue(typ, val);
    while (typeof typ === "object" && typ.ref !== undefined) {
        typ = typeMap[typ.ref];
    }
    if (Array.isArray(typ)) return transformEnum(typ, val);
    if (typeof typ === "object") {
        return typ.hasOwnProperty("unionMembers") ? transformUnion(typ.unionMembers, val)
            : typ.hasOwnProperty("arrayItems")    ? transformArray(typ.arrayItems, val)
            : typ.hasOwnProperty("props")         ? transformObject(getProps(typ), typ.additional, val)
            : invalidValue(typ, val);
    }
    // Numbers can be parsed by Date but shouldn't be.
    if (typ === Date && typeof val !== "number") return transformDate(val);
    return transformPrimitive(typ, val);
}

function cast<T>(val: any, typ: any): T {
    return transform(val, typ, jsonToJSProps);
}

function uncast<T>(val: T, typ: any): any {
    return transform(val, typ, jsToJSONProps);
}

function a(typ: any) {
    return { arrayItems: typ };
}

function u(...typs: any[]) {
    return { unionMembers: typs };
}

function o(props: any[], additional: any) {
    return { props, additional };
}

function m(additional: any) {
    return { props: [], additional };
}

function r(name: string) {
    return { ref: name };
}

const typeMap: any = {
    "Chain": o([
        { json: "$id", js: "$id", typ: "" },
        { json: "$schema", js: "$schema", typ: "" },
        { json: "title", js: "title", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "properties", js: "properties", typ: r("ChainProperties") },
        { json: "$defs", js: "$defs", typ: r("Defs") },
    ], false),
    "Defs": o([
        { json: "peer", js: "peer", typ: r("Peer") },
        { json: "endpoint", js: "endpoint", typ: r("Endpoint") },
        { json: "explorer", js: "explorer", typ: r("Explorer") },
        { json: "fee_token", js: "fee_token", typ: r("FeeToken") },
        { json: "logo_URIs", js: "logo_URIs", typ: r("LogoURIs") },
    ], false),
    "Endpoint": o([
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "properties", js: "properties", typ: r("EndpointProperties") },
    ], false),
    "EndpointProperties": o([
        { json: "address", js: "address", typ: r("Bech32Prefix") },
        { json: "provider", js: "provider", typ: r("Bech32Prefix") },
    ], false),
    "Bech32Prefix": o([
        { json: "type", js: "type", typ: r("Type") },
    ], false),
    "Explorer": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("ExplorerProperties") },
    ], false),
    "ExplorerProperties": o([
        { json: "kind", js: "kind", typ: r("Bech32Prefix") },
        { json: "url", js: "url", typ: r("Bech32Prefix") },
        { json: "tx_page", js: "tx_page", typ: r("Bech32Prefix") },
        { json: "account_page", js: "account_page", typ: r("Bech32Prefix") },
    ], false),
    "FeeToken": o([
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "properties", js: "properties", typ: r("FeeTokenProperties") },
    ], false),
    "FeeTokenProperties": o([
        { json: "denom", js: "denom", typ: r("Bech32Prefix") },
        { json: "fixed_min_gas_price", js: "fixed_min_gas_price", typ: r("Bech32Prefix") },
    ], false),
    "LogoURIs": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("LogoURIsProperties") },
    ], false),
    "LogoURIsProperties": o([
        { json: "png", js: "png", typ: r("PNG") },
        { json: "svg", js: "svg", typ: r("PNG") },
    ], false),
    "PNG": o([
        { json: "type", js: "type", typ: r("Type") },
        { json: "format", js: "format", typ: "" },
    ], false),
    "Peer": o([
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "properties", js: "properties", typ: r("PeerProperties") },
    ], false),
    "PeerProperties": o([
        { json: "id", js: "id", typ: r("Bech32Prefix") },
        { json: "address", js: "address", typ: r("Bech32Prefix") },
        { json: "provider", js: "provider", typ: r("Bech32Prefix") },
    ], false),
    "ChainProperties": o([
        { json: "chain_name", js: "chain_name", typ: r("Bech32Prefix") },
        { json: "chain_id", js: "chain_id", typ: r("Bech32Prefix") },
        { json: "pretty_name", js: "pretty_name", typ: r("Bech32Prefix") },
        { json: "status", js: "status", typ: r("NetworkType") },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "bech32_prefix", js: "bech32_prefix", typ: r("Bech32Prefix") },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "daemon_name", js: "daemon_name", typ: r("Bech32Prefix") },
        { json: "node_home", js: "node_home", typ: r("Bech32Prefix") },
        { json: "key_algos", js: "key_algos", typ: r("KeyAlgos") },
        { json: "slip44", js: "slip44", typ: r("Bech32Prefix") },
        { json: "fees", js: "fees", typ: r("Fees") },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "peers", js: "peers", typ: r("Peers") },
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "explorers", js: "explorers", typ: r("Explorers") },
    ], false),
    "Apis": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("ApisProperties") },
    ], false),
    "ApisProperties": o([
        { json: "rpc", js: "rpc", typ: r("Explorers") },
        { json: "rest", js: "rest", typ: r("Explorers") },
        { json: "grpc", js: "grpc", typ: r("Explorers") },
    ], false),
    "Explorers": o([
        { json: "type", js: "type", typ: "" },
        { json: "items", js: "items", typ: r("ExplorersItems") },
    ], false),
    "ExplorersItems": o([
        { json: "$ref", js: "$ref", typ: "" },
    ], false),
    "Codebase": o([
        { json: "type", js: "type", typ: "" },
        { json: "required", js: "required", typ: a("") },
        { json: "properties", js: "properties", typ: r("CodebaseProperties") },
    ], false),
    "CodebaseProperties": o([
        { json: "git_repo", js: "git_repo", typ: r("PNG") },
        { json: "recommended_version", js: "recommended_version", typ: r("Bech32Prefix") },
        { json: "compatible_versions", js: "compatible_versions", typ: r("CompatibleVersions") },
        { json: "binaries", js: "binaries", typ: r("Binaries") },
    ], false),
    "Binaries": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("BinariesProperties") },
    ], false),
    "BinariesProperties": o([
        { json: "linux/amd", js: "linux/amd", typ: r("PNG") },
    ], false),
    "CompatibleVersions": o([
        { json: "type", js: "type", typ: "" },
        { json: "items", js: "items", typ: r("Bech32Prefix") },
    ], false),
    "Fees": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("FeesProperties") },
    ], false),
    "FeesProperties": o([
        { json: "fee_tokens", js: "fee_tokens", typ: r("Explorers") },
    ], false),
    "Genesis": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("GenesisProperties") },
    ], false),
    "GenesisProperties": o([
        { json: "genesis_url", js: "genesis_url", typ: r("Bech32Prefix") },
    ], false),
    "KeyAlgos": o([
        { json: "type", js: "type", typ: "" },
        { json: "items", js: "items", typ: r("KeyAlgosItems") },
    ], false),
    "KeyAlgosItems": o([
        { json: "type", js: "type", typ: r("Type") },
        { json: "enum", js: "enum", typ: a("") },
        { json: "uniqueItems", js: "uniqueItems", typ: true },
    ], false),
    "NetworkType": o([
        { json: "enum", js: "enum", typ: a("") },
    ], false),
    "Peers": o([
        { json: "type", js: "type", typ: "" },
        { json: "properties", js: "properties", typ: r("PeersProperties") },
    ], false),
    "PeersProperties": o([
        { json: "seeds", js: "seeds", typ: r("Explorers") },
        { json: "persistent_peers", js: "persistent_peers", typ: r("Explorers") },
    ], false),
    "Type": [
        "number",
        "string",
    ],
};
