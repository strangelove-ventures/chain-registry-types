// To parse this data:
//
//   import { Convert, Assetlist } from "./file";
//
//   const assetlist = Convert.toAssetlist(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface Assetlist {
    $defs:       Defs;
    $id:         string;
    $schema:     string;
    description: string;
    properties:  AssetlistProperties;
    required:    string[];
    title:       string;
    type:        string;
}

export interface Defs {
    asset:      Asset;
    denom_unit: DenomUnit;
}

export interface Asset {
    if:         If;
    properties: AssetProperties;
    required:   string[];
    then:       Then;
    type:       string;
}

export interface If {
    properties: IfProperties;
    required:   string[];
}

export interface IfProperties {
    type_asset: PurpleTypeAsset;
}

export interface PurpleTypeAsset {
    enum: string[];
}

export interface AssetProperties {
    address:      Address;
    base:         Address;
    coingecko_id: Address;
    denom_units:  Assets;
    description:  Address;
    display:      Address;
    ibc:          Ibc;
    logo_URIs:    LogoURIs;
    name:         Address;
    symbol:       Address;
    type_asset:   FluffyTypeAsset;
}

export interface Address {
    description: string;
    type:        string;
}

export interface Assets {
    items: Items;
    type:  string;
}

export interface Items {
    $ref: string;
}

export interface Ibc {
    description: string;
    properties:  IbcProperties;
    required:    string[];
    type:        string;
}

export interface IbcProperties {
    dst_channel:    ChainName;
    source_channel: ChainName;
    source_denom:   ChainName;
}

export interface ChainName {
    type: string;
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
    type:   string;
}

export interface FluffyTypeAsset {
    default:     string;
    description: string;
    enum:        string[];
    type:        string;
}

export interface Then {
    required: string[];
}

export interface DenomUnit {
    properties: DenomUnitProperties;
    required:   string[];
    type:       string;
}

export interface DenomUnitProperties {
    aliases:  Aliases;
    denom:    ChainName;
    exponent: ChainName;
}

export interface Aliases {
    items: ChainName;
    type:  string;
}

export interface AssetlistProperties {
    assets:     Assets;
    chain_name: ChainName;
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
        { json: "$defs", js: "$defs", typ: r("Defs") },
        { json: "$id", js: "$id", typ: "" },
        { json: "$schema", js: "$schema", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("AssetlistProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "title", js: "title", typ: "" },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Defs": o([
        { json: "asset", js: "asset", typ: r("Asset") },
        { json: "denom_unit", js: "denom_unit", typ: r("DenomUnit") },
    ], false),
    "Asset": o([
        { json: "if", js: "if", typ: r("If") },
        { json: "properties", js: "properties", typ: r("AssetProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "then", js: "then", typ: r("Then") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "If": o([
        { json: "properties", js: "properties", typ: r("IfProperties") },
        { json: "required", js: "required", typ: a("") },
    ], false),
    "IfProperties": o([
        { json: "type_asset", js: "type_asset", typ: r("PurpleTypeAsset") },
    ], false),
    "PurpleTypeAsset": o([
        { json: "enum", js: "enum", typ: a("") },
    ], false),
    "AssetProperties": o([
        { json: "address", js: "address", typ: r("Address") },
        { json: "base", js: "base", typ: r("Address") },
        { json: "coingecko_id", js: "coingecko_id", typ: r("Address") },
        { json: "denom_units", js: "denom_units", typ: r("Assets") },
        { json: "description", js: "description", typ: r("Address") },
        { json: "display", js: "display", typ: r("Address") },
        { json: "ibc", js: "ibc", typ: r("Ibc") },
        { json: "logo_URIs", js: "logo_URIs", typ: r("LogoURIs") },
        { json: "name", js: "name", typ: r("Address") },
        { json: "symbol", js: "symbol", typ: r("Address") },
        { json: "type_asset", js: "type_asset", typ: r("FluffyTypeAsset") },
    ], false),
    "Address": o([
        { json: "description", js: "description", typ: "" },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Assets": o([
        { json: "items", js: "items", typ: r("Items") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Items": o([
        { json: "$ref", js: "$ref", typ: "" },
    ], false),
    "Ibc": o([
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("IbcProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "IbcProperties": o([
        { json: "dst_channel", js: "dst_channel", typ: r("ChainName") },
        { json: "source_channel", js: "source_channel", typ: r("ChainName") },
        { json: "source_denom", js: "source_denom", typ: r("ChainName") },
    ], false),
    "ChainName": o([
        { json: "type", js: "type", typ: "" },
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
        { json: "type", js: "type", typ: "" },
    ], false),
    "FluffyTypeAsset": o([
        { json: "default", js: "default", typ: "" },
        { json: "description", js: "description", typ: "" },
        { json: "enum", js: "enum", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Then": o([
        { json: "required", js: "required", typ: a("") },
    ], false),
    "DenomUnit": o([
        { json: "properties", js: "properties", typ: r("DenomUnitProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "DenomUnitProperties": o([
        { json: "aliases", js: "aliases", typ: r("Aliases") },
        { json: "denom", js: "denom", typ: r("ChainName") },
        { json: "exponent", js: "exponent", typ: r("ChainName") },
    ], false),
    "Aliases": o([
        { json: "items", js: "items", typ: r("ChainName") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "AssetlistProperties": o([
        { json: "assets", js: "assets", typ: r("Assets") },
        { json: "chain_name", js: "chain_name", typ: r("ChainName") },
    ], false),
};
