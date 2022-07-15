// To parse this data:
//
//   import { Convert, Assetlist } from "./file";
//
//   const assetlist = Convert.toAssetlist(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

/**
 * Asset lists are a similar mechanism to allow frontends and other UIs to fetch metadata
 * associated with Cosmos SDK denoms, especially for assets sent over IBC.
 */
export interface Assetlist {
    assets:     AssetElement[];
    chain_name: string;
}

export interface AssetElement {
    /**
     * [OPTIONAL] The address of the asset. Only required for type_asset : cw20, snip20
     */
    address?: string;
    /**
     * The base unit of the asset. Must be in denom_units.
     */
    base: string;
    /**
     * [OPTIONAL] The coingecko id to fetch asset data from coingecko v3 api. See
     * https://api.coingecko.com/api/v3/coins/list
     */
    coingecko_id?: string;
    denom_units:   DenomUnitElement[];
    /**
     * [OPTIONAL] A short description of the asset
     */
    description?: string;
    /**
     * The human friendly unit of the asset. Must be in denom_units.
     */
    display: string;
    /**
     * [OPTIONAL] IBC Channel between src and dst between chain
     */
    ibc?:       Ibc;
    logo_URIs?: LogoURIs;
    /**
     * The project name of the asset. For example Bitcoin.
     */
    name: string;
    /**
     * The symbol of an asset. For example BTC.
     */
    symbol: string;
    /**
     * [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
     */
    type_asset?: TypeAsset;
}

export interface DenomUnitElement {
    aliases?: string[];
    denom:    string;
    exponent: number;
}

/**
 * [OPTIONAL] IBC Channel between src and dst between chain
 */
export interface Ibc {
    dst_channel:    string;
    source_channel: string;
    source_denom:   string;
}

export interface LogoURIs {
    png?: string;
    svg?: string;
}

/**
 * [OPTIONAL] The potential options for type of asset. By default, assumes sdk.coin
 */
export enum TypeAsset {
    Cw20 = "cw20",
    Erc20 = "erc20",
    SDKCoin = "sdk.coin",
    Snip20 = "snip20",
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toAssetlist(json: string): Assetlist {
        return cast(JSON.parse(json), r("Assetlist"));
    }

    public static assetlistToJson(value: Assetlist): string {
        return JSON.stringify(uncast(value, r("Assetlist")), null, 2);
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
    "Assetlist": o([
        { json: "assets", js: "assets", typ: a(r("AssetElement")) },
        { json: "chain_name", js: "chain_name", typ: "" },
    ], "any"),
    "AssetElement": o([
        { json: "address", js: "address", typ: u(undefined, "") },
        { json: "base", js: "base", typ: "" },
        { json: "coingecko_id", js: "coingecko_id", typ: u(undefined, "") },
        { json: "denom_units", js: "denom_units", typ: a(r("DenomUnitElement")) },
        { json: "description", js: "description", typ: u(undefined, "") },
        { json: "display", js: "display", typ: "" },
        { json: "ibc", js: "ibc", typ: u(undefined, r("Ibc")) },
        { json: "logo_URIs", js: "logo_URIs", typ: u(undefined, r("LogoURIs")) },
        { json: "name", js: "name", typ: "" },
        { json: "symbol", js: "symbol", typ: "" },
        { json: "type_asset", js: "type_asset", typ: u(undefined, r("TypeAsset")) },
    ], "any"),
    "DenomUnitElement": o([
        { json: "aliases", js: "aliases", typ: u(undefined, a("")) },
        { json: "denom", js: "denom", typ: "" },
        { json: "exponent", js: "exponent", typ: 0 },
    ], "any"),
    "Ibc": o([
        { json: "dst_channel", js: "dst_channel", typ: "" },
        { json: "source_channel", js: "source_channel", typ: "" },
        { json: "source_denom", js: "source_denom", typ: "" },
    ], "any"),
    "LogoURIs": o([
        { json: "png", js: "png", typ: u(undefined, "") },
        { json: "svg", js: "svg", typ: u(undefined, "") },
    ], "any"),
    "TypeAsset": [
        "cw20",
        "erc20",
        "sdk.coin",
        "snip20",
    ],
};
