// To parse this data:
//
//   import { Convert, IbcData } from "./file";
//
//   const ibcData = Convert.toIbcData(json);
//
// These functions will throw an error if the JSON doesn't
// match the expected interface, even if the JSON is valid.

export interface IbcData {
    $defs?: any;
    /**
     * Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
     * alphabetical order.
     */
    "chain-1": { [key: string]: any };
    /**
     * Top level IBC data pertaining to the chain. `chain-1` and `chain-2` should be in
     * alphabetical order.
     */
    "chain-2": { [key: string]: any };
    channels:  Channel[];
}

export interface Channel {
    "chain-1": { [key: string]: any };
    "chain-2": { [key: string]: any };
    /**
     * Human readable description of the channel.
     */
    description?: string;
    /**
     * Determines if packets from a sending module must be 'ordered' or 'unordered'.
     */
    ordering: Ordering;
    /**
     * Human readable key:value pairs that help describe and distinguish channels.
     */
    tags?: Tags;
    /**
     * IBC Version
     */
    version: string;
}

/**
 * Determines if packets from a sending module must be 'ordered' or 'unordered'.
 */
export enum Ordering {
    Ordered = "ordered",
    Unordered = "unordered",
}

/**
 * Human readable key:value pairs that help describe and distinguish channels.
 */
export interface Tags {
    dex?:       string;
    preferred?: boolean;
    /**
     * String that helps describe non-dex use cases ex: interchain accounts(ICA).
     */
    properties?: string;
    status?:     Status;
}

export enum Status {
    Killed = "killed",
    Live = "live",
    Upcoming = "upcoming",
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
        { json: "$defs", js: "$defs", typ: u(undefined, "any") },
        { json: "chain-1", js: "chain-1", typ: m("any") },
        { json: "chain-2", js: "chain-2", typ: m("any") },
        { json: "channels", js: "channels", typ: a(r("Channel")) },
    ], "any"),
    "Channel": o([
        { json: "chain-1", js: "chain-1", typ: m("any") },
        { json: "chain-2", js: "chain-2", typ: m("any") },
        { json: "description", js: "description", typ: u(undefined, "") },
        { json: "ordering", js: "ordering", typ: r("Ordering") },
        { json: "tags", js: "tags", typ: u(undefined, r("Tags")) },
        { json: "version", js: "version", typ: "" },
    ], "any"),
    "Tags": o([
        { json: "dex", js: "dex", typ: u(undefined, "") },
        { json: "preferred", js: "preferred", typ: u(undefined, true) },
        { json: "properties", js: "properties", typ: u(undefined, "") },
        { json: "status", js: "status", typ: u(undefined, r("Status")) },
    ], "any"),
    "Ordering": [
        "ordered",
        "unordered",
    ],
    "Status": [
        "killed",
        "live",
        "upcoming",
    ],
};
