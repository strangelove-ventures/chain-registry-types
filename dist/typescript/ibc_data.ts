// To parse this data:
//
//   import { Convert, IbcData } from "./file";
//
//   const ibcData = Convert.toIbcData(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface IbcData {
    $schema:    string;
    properties: IbcDataProperties;
    required:   string[];
    type:       string;
}

export interface IbcDataProperties {
    $defs:     Defs;
    "chain-1": PurpleChain;
    "chain-2": PurpleChain;
    channels:  Channels;
}

export interface Defs {
    chain_info:   ChainInfo;
    channel_info: ChannelInfo;
}

export interface ChainInfo {
    properties: ChainInfoProperties;
    required:   string[];
    type:       string;
}

export interface ChainInfoProperties {
    "chain-name":    ChainName;
    "client-id":     ClientID;
    "connection-id": ClientID;
}

export interface ChainName {
    type: string;
}

export interface ClientID {
    description: string;
    type:        string;
}

export interface ChannelInfo {
    properties: ChannelInfoProperties;
    required:   string[];
    type:       string;
}

export interface ChannelInfoProperties {
    "channel-id": ClientID;
    "port-id":    ClientID;
}

export interface PurpleChain {
    description: string;
    items:       Items;
    type:        string;
}

export interface Items {
    $refs: string;
}

export interface Channels {
    items: Item[];
    type:  string;
}

export interface Item {
    properties: ItemProperties;
    required:   string[];
    type:       string;
}

export interface ItemProperties {
    "chain-1":   FluffyChain;
    "chain-2":   FluffyChain;
    description: ClientID;
    ordering:    Ordering;
    tags:        Tags;
    version:     ClientID;
}

export interface FluffyChain {
    items: Items;
    type:  string;
}

export interface Ordering {
    description: string;
    enum:        string[];
}

export interface Tags {
    description: string;
    properties:  TagsProperties;
    type:        string;
}

export interface TagsProperties {
    dex:        ChainName;
    preferred:  ChainName;
    properties: ClientID;
    status:     Status;
}

export interface Status {
    enum: string[];
}

// Converts JSON strings to/from your types
// and asserts the results of JSON.parse at runtime
export class Convert {
    public static toIbcData(json: string): IbcData {
        return cast(JSON.parse(json), r("IbcData"));
    }

    public static ibcDataToJson(value: IbcData): string {
        return JSON.stringify(uncast(value, r("IbcData")), null, 2);
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
    "IbcData": o([
        { json: "$schema", js: "$schema", typ: "" },
        { json: "properties", js: "properties", typ: r("IbcDataProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "IbcDataProperties": o([
        { json: "$defs", js: "$defs", typ: r("Defs") },
        { json: "chain-1", js: "chain-1", typ: r("PurpleChain") },
        { json: "chain-2", js: "chain-2", typ: r("PurpleChain") },
        { json: "channels", js: "channels", typ: r("Channels") },
    ], false),
    "Defs": o([
        { json: "chain_info", js: "chain_info", typ: r("ChainInfo") },
        { json: "channel_info", js: "channel_info", typ: r("ChannelInfo") },
    ], false),
    "ChainInfo": o([
        { json: "properties", js: "properties", typ: r("ChainInfoProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ChainInfoProperties": o([
        { json: "chain-name", js: "chain-name", typ: r("ChainName") },
        { json: "client-id", js: "client-id", typ: r("ClientID") },
        { json: "connection-id", js: "connection-id", typ: r("ClientID") },
    ], false),
    "ChainName": o([
        { json: "type", js: "type", typ: "" },
    ], false),
    "ClientID": o([
        { json: "description", js: "description", typ: "" },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ChannelInfo": o([
        { json: "properties", js: "properties", typ: r("ChannelInfoProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ChannelInfoProperties": o([
        { json: "channel-id", js: "channel-id", typ: r("ClientID") },
        { json: "port-id", js: "port-id", typ: r("ClientID") },
    ], false),
    "PurpleChain": o([
        { json: "description", js: "description", typ: "" },
        { json: "items", js: "items", typ: r("Items") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Items": o([
        { json: "$refs", js: "$refs", typ: "" },
    ], false),
    "Channels": o([
        { json: "items", js: "items", typ: a(r("Item")) },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Item": o([
        { json: "properties", js: "properties", typ: r("ItemProperties") },
        { json: "required", js: "required", typ: a("") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "ItemProperties": o([
        { json: "chain-1", js: "chain-1", typ: r("FluffyChain") },
        { json: "chain-2", js: "chain-2", typ: r("FluffyChain") },
        { json: "description", js: "description", typ: r("ClientID") },
        { json: "ordering", js: "ordering", typ: r("Ordering") },
        { json: "tags", js: "tags", typ: r("Tags") },
        { json: "version", js: "version", typ: r("ClientID") },
    ], false),
    "FluffyChain": o([
        { json: "items", js: "items", typ: r("Items") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "Ordering": o([
        { json: "description", js: "description", typ: "" },
        { json: "enum", js: "enum", typ: a("") },
    ], false),
    "Tags": o([
        { json: "description", js: "description", typ: "" },
        { json: "properties", js: "properties", typ: r("TagsProperties") },
        { json: "type", js: "type", typ: "" },
    ], false),
    "TagsProperties": o([
        { json: "dex", js: "dex", typ: r("ChainName") },
        { json: "preferred", js: "preferred", typ: r("ChainName") },
        { json: "properties", js: "properties", typ: r("ClientID") },
        { json: "status", js: "status", typ: r("Status") },
    ], false),
    "Status": o([
        { json: "enum", js: "enum", typ: a("") },
    ], false),
};
