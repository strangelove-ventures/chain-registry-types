// To parse this data:
//
//   import { Convert, Chain } from "./file";
//
//   const chain = Convert.toChain(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

/**
 * Cosmos Chain.json is a metadata file that contains information about a cosmos sdk based
 * chain.
 */
export interface Chain {
    apis?:         Apis;
    bech32_prefix: string;
    chain_id:      string;
    chain_name:    string;
    codebase?:     Codebase;
    daemon_name?:  string;
    explorers?:    ExplorerElement[];
    fees?:         Fees;
    genesis?:      Genesis;
    key_algos?:    KeyAlgo[];
    network_type?: NetworkType;
    node_home?:    string;
    peers?:        Peers;
    pretty_name?:  string;
    slip44?:       number;
    status?:       Status;
}

export interface Apis {
    grpc?: GrpcElement[];
    rest?: GrpcElement[];
    rpc?:  GrpcElement[];
}

export interface GrpcElement {
    address:   string;
    archive?:  boolean;
    provider?: string;
}

export interface Codebase {
    binaries?:           Binaries;
    compatible_versions: string[];
    git_repo:            string;
    recommended_version: string;
}

export interface Binaries {
    "linux/amd"?: string;
}

export interface ExplorerElement {
    account_page?: string;
    kind?:         string;
    tx_page?:      string;
    url?:          string;
}

export interface Fees {
    fee_tokens?: FeeTokenElement[];
}

export interface FeeTokenElement {
    average_gas_price?:   number;
    denom:                string;
    fixed_min_gas_price?: number;
    high_gas_price?:      number;
    low_gas_price?:       number;
}

export interface Genesis {
    genesis_url?: string;
}

export enum KeyAlgo {
    Ed25519 = "ed25519",
    Ethsecp256K1 = "ethsecp256k1",
    Secp256K1 = "secp256k1",
    Sr25519 = "sr25519",
}

export enum NetworkType {
    Mainnet = "mainnet",
    Testnet = "testnet",
}

export interface Peers {
    persistent_peers?: PersistentPeerElement[];
    seeds?:            PersistentPeerElement[];
}

export interface PersistentPeerElement {
    address:   string;
    id:        string;
    provider?: string;
}

export enum Status {
    Killed = "killed",
    Live = "live",
    Upcoming = "upcoming",
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
        { json: "apis", js: "apis", typ: u(undefined, r("Apis")) },
        { json: "bech32_prefix", js: "bech32_prefix", typ: "" },
        { json: "chain_id", js: "chain_id", typ: "" },
        { json: "chain_name", js: "chain_name", typ: "" },
        { json: "codebase", js: "codebase", typ: u(undefined, r("Codebase")) },
        { json: "daemon_name", js: "daemon_name", typ: u(undefined, "") },
        { json: "explorers", js: "explorers", typ: u(undefined, a(r("ExplorerElement"))) },
        { json: "fees", js: "fees", typ: u(undefined, r("Fees")) },
        { json: "genesis", js: "genesis", typ: u(undefined, r("Genesis")) },
        { json: "key_algos", js: "key_algos", typ: u(undefined, a(r("KeyAlgo"))) },
        { json: "network_type", js: "network_type", typ: u(undefined, r("NetworkType")) },
        { json: "node_home", js: "node_home", typ: u(undefined, "") },
        { json: "peers", js: "peers", typ: u(undefined, r("Peers")) },
        { json: "pretty_name", js: "pretty_name", typ: u(undefined, "") },
        { json: "slip44", js: "slip44", typ: u(undefined, 3.14) },
        { json: "status", js: "status", typ: u(undefined, r("Status")) },
    ], "any"),
    "Apis": o([
        { json: "grpc", js: "grpc", typ: u(undefined, a(r("GrpcElement"))) },
        { json: "rest", js: "rest", typ: u(undefined, a(r("GrpcElement"))) },
        { json: "rpc", js: "rpc", typ: u(undefined, a(r("GrpcElement"))) },
    ], "any"),
    "GrpcElement": o([
        { json: "address", js: "address", typ: "" },
        { json: "archive", js: "archive", typ: u(undefined, true) },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], "any"),
    "Codebase": o([
        { json: "binaries", js: "binaries", typ: u(undefined, r("Binaries")) },
        { json: "compatible_versions", js: "compatible_versions", typ: a("") },
        { json: "git_repo", js: "git_repo", typ: "" },
        { json: "recommended_version", js: "recommended_version", typ: "" },
    ], "any"),
    "Binaries": o([
        { json: "linux/amd", js: "linux/amd", typ: u(undefined, "") },
    ], "any"),
    "ExplorerElement": o([
        { json: "account_page", js: "account_page", typ: u(undefined, "") },
        { json: "kind", js: "kind", typ: u(undefined, "") },
        { json: "tx_page", js: "tx_page", typ: u(undefined, "") },
        { json: "url", js: "url", typ: u(undefined, "") },
    ], "any"),
    "Fees": o([
        { json: "fee_tokens", js: "fee_tokens", typ: u(undefined, a(r("FeeTokenElement"))) },
    ], "any"),
    "FeeTokenElement": o([
        { json: "average_gas_price", js: "average_gas_price", typ: u(undefined, 3.14) },
        { json: "denom", js: "denom", typ: "" },
        { json: "fixed_min_gas_price", js: "fixed_min_gas_price", typ: u(undefined, 3.14) },
        { json: "high_gas_price", js: "high_gas_price", typ: u(undefined, 3.14) },
        { json: "low_gas_price", js: "low_gas_price", typ: u(undefined, 3.14) },
    ], "any"),
    "Genesis": o([
        { json: "genesis_url", js: "genesis_url", typ: u(undefined, "") },
    ], "any"),
    "Peers": o([
        { json: "persistent_peers", js: "persistent_peers", typ: u(undefined, a(r("PersistentPeerElement"))) },
        { json: "seeds", js: "seeds", typ: u(undefined, a(r("PersistentPeerElement"))) },
    ], "any"),
    "PersistentPeerElement": o([
        { json: "address", js: "address", typ: "" },
        { json: "id", js: "id", typ: "" },
        { json: "provider", js: "provider", typ: u(undefined, "") },
    ], "any"),
    "KeyAlgo": [
        "ed25519",
        "ethsecp256k1",
        "secp256k1",
        "sr25519",
    ],
    "NetworkType": [
        "mainnet",
        "testnet",
    ],
    "Status": [
        "killed",
        "live",
        "upcoming",
    ],
};
