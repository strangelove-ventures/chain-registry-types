// To parse this data:
//
//   import { Convert, Chain } from "./file";
//
//   const chain = Convert.toChain(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Chain {
    $defs:       Defs;
    $id:         string;
    $schema:     string;
    description: string;
    properties:  ChainProperties;
    required:    string[];
    title:       string;
    type:        string;
}

export interface Defs {
    endpoint:  Endpoint;
    explorer:  Explorer;
    fee_token: FeeToken;
    logo_URIs: LogoURIs;
    peer:      Peer;
}

export interface Endpoint {
    properties: EndpointProperties;
    required:   string[];
    type:       string;
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
    properties: ExplorerProperties;
    type:       string;
}

export interface ExplorerProperties {
    account_page: Bech32Prefix;
    kind:         Bech32Prefix;
    tx_page:      Bech32Prefix;
    url:          Bech32Prefix;
}

export interface FeeToken {
    properties: FeeTokenProperties;
    required:   string[];
    type:       string;
}

export interface FeeTokenProperties {
    denom:               Bech32Prefix;
    fixed_min_gas_price: Bech32Prefix;
}

export interface LogoURIs {
    properties: LogoURIsProperties;
    type:       string;
}

export interface LogoURIsProperties {
    png: PNG;
    svg: PNG;
}

export interface PNG {
    format: string;
    type:   Type;
}

export interface Peer {
    properties: PeerProperties;
    required:   string[];
    type:       string;
}

export interface PeerProperties {
    address:  Bech32Prefix;
    id:       Bech32Prefix;
    provider: Bech32Prefix;
}

export interface ChainProperties {
    apis:          Apis;
    bech32_prefix: Bech32Prefix;
    chain_id:      Bech32Prefix;
    chain_name:    Bech32Prefix;
    codebase:      Codebase;
    daemon_name:   Bech32Prefix;
    explorers:     Explorers;
    fees:          Fees;
    genesis:       Genesis;
    key_algos:     KeyAlgos;
    network_type:  NetworkType;
    node_home:     Bech32Prefix;
    peers:         Peers;
    pretty_name:   Bech32Prefix;
    slip44:        Bech32Prefix;
    status:        NetworkType;
}

export interface Apis {
    properties: ApisProperties;
    type:       string;
}

export interface ApisProperties {
    grpc: Explorers;
    rest: Explorers;
    rpc:  Explorers;
}

export interface Explorers {
    items: ExplorersItems;
    type:  string;
}

export interface ExplorersItems {
    $ref: string;
}

export interface Codebase {
    properties: CodebaseProperties;
    required:   string[];
    type:       string;
}

export interface CodebaseProperties {
    binaries:            Binaries;
    compatible_versions: CompatibleVersions;
    git_repo:            PNG;
    recommended_version: Bech32Prefix;
}

export interface Binaries {
    properties: BinariesProperties;
    type:       string;
}

export interface BinariesProperties {
    "linux/amd": PNG;
}

export interface CompatibleVersions {
    items: Bech32Prefix;
    type:  string;
}

export interface Fees {
    properties: FeesProperties;
    type:       string;
}

export interface FeesProperties {
    fee_tokens: Explorers;
}

export interface Genesis {
    properties: GenesisProperties;
    type:       string;
}

export interface GenesisProperties {
    genesis_url: Bech32Prefix;
}

export interface KeyAlgos {
    items: KeyAlgosItems;
    type:  string;
}

export interface KeyAlgosItems {
    enum:        string[];
    type:        Type;
    uniqueItems: boolean;
}

export interface NetworkType {
    enum: string[];
}

export interface Peers {
    properties: PeersProperties;
    type:       string;
}

export interface PeersProperties {
    persistent_peers: Explorers;
    seeds:            Explorers;
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
        { json: "$defs", js: "$defs", typ: r("Defs") },
        { json: "$id", js: "$id", typ: "" },
        { json: "$schema", js: "$schema", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("ChainProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "title", js: "title", typ: "" },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Defs": o([
        { json: "endpoint", js: "endpoint", typ: r("Endpoint") },
        { json: "explorer", js: "explorer", typ: r("Explorer") },
        { json: "fee_token", js: "fee_token", typ: r("FeeToken") },
        { json: "logo_URIs", js: "logo_URIs", typ: r("LogoURIs") },
        { json: "peer", js: "peer", typ: r("Peer") },
    ], false),
    "Endpoint": o([
        { json: "properties", js: "properties", typ: r("EndpointProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "EndpointProperties": o([
        { json: "address", js: "address", typ: r("Bech32Prefix") },
        { json: "provider", js: "provider", typ: r("Bech32Prefix") },
    ], false),
    "Bech32Prefix": o([
        { json: "type", js: "type", typ: r("Type") },
    ], false),
    "Explorer": o([
        { json: "properties", js: "properties", typ: r("ExplorerProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ExplorerProperties": o([
        { json: "account_page", js: "account_page", typ: r("Bech32Prefix") },
        { json: "kind", js: "kind", typ: r("Bech32Prefix") },
        { json: "tx_page", js: "tx_page", typ: r("Bech32Prefix") },
        { json: "url", js: "url", typ: r("Bech32Prefix") },
    ], false),
    "FeeToken": o([
        { json: "properties", js: "properties", typ: r("FeeTokenProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "FeeTokenProperties": o([
        { json: "denom", js: "denom", typ: r("Bech32Prefix") },
        { json: "fixed_min_gas_price", js: "fixed_min_gas_price", typ: r("Bech32Prefix") },
    ], false),
    "LogoURIs": o([
        { json: "properties", js: "properties", typ: r("LogoURIsProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "LogoURIsProperties": o([
        { json: "png", js: "png", typ: r("PNG") },
        { json: "svg", js: "svg", typ: r("PNG") },
    ], false),
    "PNG": o([
        { json: "format", js: "format", typ: "" },
        { json: "type", js: "type", typ: r("Type") },
    ], false),
    "Peer": o([
        { json: "properties", js: "properties", typ: r("PeerProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "PeerProperties": o([
        { json: "address", js: "address", typ: r("Bech32Prefix") },
        { json: "id", js: "id", typ: r("Bech32Prefix") },
        { json: "provider", js: "provider", typ: r("Bech32Prefix") },
    ], false),
    "ChainProperties": o([
        { json: "apis", js: "apis", typ: r("Apis") },
        { json: "bech32_prefix", js: "bech32_prefix", typ: r("Bech32Prefix") },
        { json: "chain_id", js: "chain_id", typ: r("Bech32Prefix") },
        { json: "chain_name", js: "chain_name", typ: r("Bech32Prefix") },
        { json: "codebase", js: "codebase", typ: r("Codebase") },
        { json: "daemon_name", js: "daemon_name", typ: r("Bech32Prefix") },
        { json: "explorers", js: "explorers", typ: r("Explorers") },
        { json: "fees", js: "fees", typ: r("Fees") },
        { json: "genesis", js: "genesis", typ: r("Genesis") },
        { json: "key_algos", js: "key_algos", typ: r("KeyAlgos") },
        { json: "network_type", js: "network_type", typ: r("NetworkType") },
        { json: "node_home", js: "node_home", typ: r("Bech32Prefix") },
        { json: "peers", js: "peers", typ: r("Peers") },
        { json: "pretty_name", js: "pretty_name", typ: r("Bech32Prefix") },
        { json: "slip44", js: "slip44", typ: r("Bech32Prefix") },
        { json: "status", js: "status", typ: r("NetworkType") },
    ], false),
    "Apis": o([
        { json: "properties", js: "properties", typ: r("ApisProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ApisProperties": o([
        { json: "grpc", js: "grpc", typ: r("Explorers") },
        { json: "rest", js: "rest", typ: r("Explorers") },
        { json: "rpc", js: "rpc", typ: r("Explorers") },
    ], false),
    "Explorers": o([
        { json: "items", js: "items", typ: r("ExplorersItems") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ExplorersItems": o([
        { json: "$ref", js: "$ref", typ: "" },
    ], false),
    "Codebase": o([
        { json: "properties", js: "properties", typ: r("CodebaseProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "CodebaseProperties": o([
        { json: "binaries", js: "binaries", typ: r("Binaries") },
        { json: "compatible_versions", js: "compatible_versions", typ: r("CompatibleVersions") },
        { json: "git_repo", js: "git_repo", typ: r("PNG") },
        { json: "recommended_version", js: "recommended_version", typ: r("Bech32Prefix") },
    ], false),
    "Binaries": o([
        { json: "properties", js: "properties", typ: r("BinariesProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "BinariesProperties": o([
        { json: "linux/amd", js: "linux/amd", typ: r("PNG") },
    ], false),
    "CompatibleVersions": o([
        { json: "items", js: "items", typ: r("Bech32Prefix") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Fees": o([
        { json: "properties", js: "properties", typ: r("FeesProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "FeesProperties": o([
        { json: "fee_tokens", js: "fee_tokens", typ: r("Explorers") },
    ], false),
    "Genesis": o([
        { json: "properties", js: "properties", typ: r("GenesisProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "GenesisProperties": o([
        { json: "genesis_url", js: "genesis_url", typ: r("Bech32Prefix") },
    ], false),
    "KeyAlgos": o([
        { json: "items", js: "items", typ: r("KeyAlgosItems") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "KeyAlgosItems": o([
        { json: "enum", js: "enum", typ: a("") },
        { json: "type", js: "type", typ: r("Type") },
        { json: "uniqueItems", js: "uniqueItems", typ: true },
    ], false),
    "NetworkType": o([
        { json: "enum", js: "enum", typ: a("") },
    ], false),
    "Peers": o([
        { json: "properties", js: "properties", typ: r("PeersProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "PeersProperties": o([
        { json: "persistent_peers", js: "persistent_peers", typ: r("Explorers") },
        { json: "seeds", js: "seeds", typ: r("Explorers") },
    ], false),
    "Type": [
        "number",
        "string",
    ],
};
