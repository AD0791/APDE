# TypeScript Masterclass — From Compiler to Production

> **Promise**: After this document, you will never be confused by TypeScript again. You will understand what the compiler does, why the type system works the way it does, and how to wield it in React Native like a weapon. This is not a tutorial — it is the mental model.

---

## Table of Contents

**Part I — The Machine**
1. [What TypeScript Actually Is](#1-what-typescript-actually-is)
2. [The Compiler Pipeline](#2-the-compiler-pipeline)
3. [tsconfig.json — Controlling the Compiler](#3-tsconfigjson--controlling-the-compiler)

**Part II — The Type System (From Atoms to Molecules)**
4. [Primitive Types — The Atoms](#4-primitive-types--the-atoms)
5. [Object Types — Shapes of Data](#5-object-types--shapes-of-data)
6. [Union & Intersection — Combining Types](#6-union--intersection--combining-types)
7. [Type Narrowing — The Compiler Thinks With You](#7-type-narrowing--the-compiler-thinks-with-you)
8. [Literal Types & const Assertions](#8-literal-types--const-assertions)
9. [Enums vs Union Literals](#9-enums-vs-union-literals)

**Part III — Generics (The Power Tool)**
10. [Generics — Types That Take Parameters](#10-generics--types-that-take-parameters)
11. [Generic Constraints — Bounding the Unknown](#11-generic-constraints--bounding-the-unknown)
12. [Generic Inference — Let the Compiler Do the Work](#12-generic-inference--let-the-compiler-do-the-work)

**Part IV — Advanced Type System**
13. [Conditional Types — if/else for Types](#13-conditional-types--ifelse-for-types)
14. [Mapped Types — Transform Every Property](#14-mapped-types--transform-every-property)
15. [Template Literal Types — String Manipulation at Type Level](#15-template-literal-types--string-manipulation-at-type-level)
16. [Utility Types — The Standard Library](#16-utility-types--the-standard-library)
17. [Type Assertions & Escape Hatches](#17-type-assertions--escape-hatches)
18. [Declaration Files & the `declare` Keyword](#18-declaration-files--the-declare-keyword)

**Part V — TypeScript in React Native**
19. [React + TypeScript Fundamentals](#19-react--typescript-fundamentals)
20. [React Native Components — Typed from Scratch](#20-react-native-components--typed-from-scratch)
21. [Hooks — Every Hook Typed](#21-hooks--every-hook-typed)
22. [React Navigation — Full Type Safety](#22-react-navigation--full-type-safety)
23. [Redux Toolkit — Typed State Management](#23-redux-toolkit--typed-state-management)
24. [Axios — Typed API Layer](#24-axios--typed-api-layer)
25. [AsyncStorage — Typed Persistence](#25-asyncstorage--typed-persistence)
26. [Common Patterns in the STS Rebuild](#26-common-patterns-in-the-sts-rebuild)

---

# Part I — The Machine

## 1. What TypeScript Actually Is

TypeScript is **JavaScript with a type checker bolted on top**. That's it. There is no TypeScript runtime. There is no TypeScript virtual machine. Your phone, your browser, Node.js — none of them run TypeScript. They all run JavaScript.

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                   │
│   your-file.ts ──► TypeScript Compiler (tsc) ──► your-file.js    │
│                         │                                         │
│                         ├── Type checks your code                 │
│                         ├── Reports errors                        │
│                         └── Strips all type annotations           │
│                                                                   │
│   The output .js file is IDENTICAL to what you wrote,             │
│   minus every type annotation. Nothing else changes.              │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### The Key Insight

**Types exist only at compile time. They are completely erased at runtime.**

```typescript
// What you write:
function greet(name: string): string {
  return `Hello, ${name}`;
}

// What actually runs (after compilation):
function greet(name) {
  return `Hello, ${name}`;
}

// The `: string` annotations? Gone. Deleted. They never existed at runtime.
```

This has consequences:

```typescript
// You CANNOT do this — types don't exist at runtime:
function process(value: string | number) {
  if (typeof value === 'string') {  // ✅ This works — typeof is a JS operator
    console.log(value.toUpperCase());
  }

  if (value instanceof string) {    // ❌ WRONG — 'string' is a type, not a class
    // ...
  }
}

// You CANNOT check interfaces at runtime:
interface User { name: string; }

function isUser(obj: unknown): obj is User {
  // You must check the SHAPE manually — the interface doesn't exist at runtime
  return typeof obj === 'object' && obj !== null && 'name' in obj;
}
```

### TypeScript = JavaScript + Static Analysis

Think of TypeScript as a **spell-checker for code**. A spell-checker:
- Reads your document
- Highlights errors
- Does NOT change what you wrote
- Works before you publish, not while the reader reads

TypeScript:
- Reads your `.ts` files
- Highlights type errors
- Strips types to produce `.js`
- Works before you ship, not while the app runs

---

## 2. The Compiler Pipeline

When you run `tsc` (or when Metro bundler processes your RN code), here's what happens:

```
┌──────────────────────────────────────────────────────────────────┐
│                  TYPESCRIPT COMPILER PIPELINE                      │
│                                                                   │
│  ┌──────────┐                                                     │
│  │  .ts     │  YOUR SOURCE CODE                                   │
│  │  files   │  (TypeScript with type annotations)                 │
│  └────┬─────┘                                                     │
│       │                                                           │
│       ▼                                                           │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PHASE 1: SCANNER (Lexer)                                 │    │
│  │                                                           │    │
│  │  Reads raw text character by character.                    │    │
│  │  Produces TOKENS:                                         │    │
│  │                                                           │    │
│  │  "const x: number = 5;"                                   │    │
│  │    → [const] [x] [:] [number] [=] [5] [;]                │    │
│  │       kw     id  colon type   eq  lit semi                │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                          │                                        │
│                          ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PHASE 2: PARSER                                          │    │
│  │                                                           │    │
│  │  Reads tokens, produces an AST (Abstract Syntax Tree).    │    │
│  │  The AST is a tree representing the structure of code.    │    │
│  │                                                           │    │
│  │  VariableDeclaration                                      │    │
│  │  ├── name: "x"                                            │    │
│  │  ├── type: NumberKeyword                                  │    │
│  │  └── initializer: NumericLiteral(5)                       │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                          │                                        │
│                          ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PHASE 3: BINDER                                          │    │
│  │                                                           │    │
│  │  Walks the AST and creates SYMBOLS — the identity of      │    │
│  │  each named thing (variable, function, class, type).      │    │
│  │  Builds scope chains (which variable belongs where).      │    │
│  │                                                           │    │
│  │  Symbol: x                                                │    │
│  │  ├── declared in: global scope                            │    │
│  │  ├── type annotation: number                              │    │
│  │  └── flags: const (not reassignable)                      │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                          │                                        │
│                          ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PHASE 4: TYPE CHECKER  ★ THE HEART OF TYPESCRIPT ★       │    │
│  │                                                           │    │
│  │  Walks the AST again. For every expression, it:           │    │
│  │  1. Resolves the type (infers if not annotated)           │    │
│  │  2. Checks assignments (is string assignable to number?)  │    │
│  │  3. Checks function calls (do args match params?)         │    │
│  │  4. Checks property access (does this object have .foo?)  │    │
│  │  5. Narrows types in branches (if/switch/typeof)          │    │
│  │  6. Reports DIAGNOSTICS (errors + warnings)               │    │
│  │                                                           │    │
│  │  This is the single largest file in the TS codebase:      │    │
│  │  checker.ts is ~50,000 lines of code.                     │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                          │                                        │
│                          ▼                                        │
│  ┌──────────────────────────────────────────────────────────┐    │
│  │  PHASE 5: EMITTER                                         │    │
│  │                                                           │    │
│  │  Walks the AST one final time. Produces output:           │    │
│  │  • .js files (your code, with types stripped)             │    │
│  │  • .d.ts files (type declarations, for library consumers) │    │
│  │  • .js.map files (source maps, for debugging)             │    │
│  │                                                           │    │
│  │  The emitter DOES NOT CARE about type errors.             │    │
│  │  Even if the checker found 100 errors, it still emits.    │    │
│  │  (Unless you set noEmitOnError: true)                     │    │
│  └──────────────────────┬───────────────────────────────────┘    │
│                          │                                        │
│                          ▼                                        │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐                   │
│  │  .js     │  │  .d.ts   │  │  .js.map     │                   │
│  │  files   │  │  files   │  │  files       │                   │
│  └──────────┘  └──────────┘  └──────────────┘                   │
│                                                                   │
└──────────────────────────────────────────────────────────────────┘
```

### In React Native (Metro Bundler)

React Native does NOT use `tsc` to compile TypeScript. It uses **Babel** (via Metro bundler):

```
┌─────────────────────────────────────────────────────────────┐
│  RN BUILD: Metro uses Babel, NOT tsc                         │
│                                                              │
│  .tsx file                                                   │
│     │                                                        │
│     ├── Babel strips types (fast, no type checking)          │
│     │   └── Output: plain .js                                │
│     │                                                        │
│     └── tsc runs separately (--noEmit) for type checking     │
│         └── Output: errors only, no files                    │
│                                                              │
│  This means:                                                 │
│  • Your app WILL BUILD even if you have type errors          │
│  • Type errors show as IDE squiggles (Cursor) or in CI       │
│  • Run `npx tsc --noEmit` to check types manually            │
└─────────────────────────────────────────────────────────────┘
```

### What This Means for You

1. **TypeScript never slows your app** — types are deleted before execution
2. **TypeScript can't prevent runtime errors from external data** — an API can still return garbage
3. **Your IDE is your primary type-checking tool** — Cursor runs the checker in real time
4. **`npx tsc --noEmit`** is your CI safety net — catches what the IDE catches, in your pipeline

---

## 3. tsconfig.json — Controlling the Compiler

Every TypeScript project has a `tsconfig.json`. Here's the one you'll use for the STS React Native rebuild, annotated:

```jsonc
// tsconfig.json — React Native CLI project
{
  "compilerOptions": {
    // ═══════════════════════════════════════════
    // LANGUAGE & ENVIRONMENT
    // ═══════════════════════════════════════════
    "target": "esnext",              // Emit modern JS (Metro handles downleveling)
    "module": "commonjs",            // RN uses CommonJS modules (require/module.exports)
    "lib": ["es2022"],               // Available global types (Promise, Map, Array methods)
    "jsx": "react-native",           // Handle JSX for RN (preserve JSX, let Metro transform)

    // ═══════════════════════════════════════════
    // STRICTNESS — Turn ALL of these ON. Always.
    // ═══════════════════════════════════════════
    "strict": true,                  // Master switch. Enables ALL strict checks below:
    //  ├── "strictNullChecks": true       — null/undefined are their own types
    //  ├── "strictFunctionTypes": true    — function params checked correctly
    //  ├── "strictBindCallApply": true    — bind/call/apply checked
    //  ├── "strictPropertyInitialization" — class props must be initialized
    //  ├── "noImplicitAny": true          — no implicit 'any' type allowed
    //  ├── "noImplicitThis": true         — 'this' must have a type
    //  └── "alwaysStrict": true           — emit "use strict" in every file

    "noUncheckedIndexedAccess": true,  // arr[0] is T | undefined, not just T
    "noImplicitReturns": true,         // Every code path must return
    "noFallthroughCasesInSwitch": true,// switch cases must break or return
    "forceConsistentCasingInFileNames": true, // Linux is case-sensitive

    // ═══════════════════════════════════════════
    // MODULE RESOLUTION
    // ═══════════════════════════════════════════
    "moduleResolution": "node",      // Resolve modules like Node.js does
    "resolveJsonModule": true,       // Allow importing .json files
    "allowSyntheticDefaultImports": true,  // import React from 'react' (not * as React)
    "esModuleInterop": true,         // Proper interop between CJS and ESM

    // ═══════════════════════════════════════════
    // PATH ALIASES (match babel.config.js)
    // ═══════════════════════════════════════════
    "baseUrl": "./src",
    "paths": {
      "@screens/*": ["screens/*"],
      "@components/*": ["components/*"],
      "@store/*": ["store/*"],
      "@api/*": ["api/*"],
      "@navigation/*": ["navigation/*"],
      "@themes/*": ["themes/*"],
      "@utils/*": ["utils/*"],
      "@types/*": ["types/*"]
    },

    // ═══════════════════════════════════════════
    // OUTPUT
    // ═══════════════════════════════════════════
    "noEmit": true,                  // Don't emit files — Metro/Babel does that
    "skipLibCheck": true,            // Don't check node_modules .d.ts (faster)
    "isolatedModules": true          // Each file must be independently compilable
                                     // (required because Babel compiles one file at a time)
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "android", "ios", "babel.config.js"]
}
```

### The 3 Settings That Matter Most

| Setting | What It Does | Why It Matters |
|---------|-------------|----------------|
| `"strict": true` | Enables all strict checks | Without this, TypeScript is just expensive JavaScript. This is the difference between "adding types" and "type safety". |
| `"noEmit": true` | Don't produce output files | Metro/Babel compiles your code. `tsc` is ONLY for type checking. |
| `"isolatedModules": true` | Each file compiled alone | Babel can't see other files. This flag ensures you don't use patterns that require cross-file analysis (like `const enum`). |

### `strict: true` — The Non-Negotiable

```typescript
// WITHOUT strict (the old STS codebase vibe):
function getUser(id) {           // id is 'any' — no safety
  const user = users.find(u => u.id === id);
  return user.name;              // user might be undefined — RUNTIME CRASH
}

// WITH strict: true (the rebuild):
function getUser(id: number): string | undefined {
  const user = users.find(u => u.id === id);
  return user?.name;             // Forced to handle undefined — NO CRASH
}
```

---

# Part II — The Type System (From Atoms to Molecules)

## 4. Primitive Types — The Atoms

These are the building blocks. Every type in TypeScript is built from these:

```typescript
// ═══════════════════════════════════════════
// THE 7 PRIMITIVES
// ═══════════════════════════════════════════

let str: string = "hello";           // Text
let num: number = 42;                // Numbers (int and float are the same)
let bool: boolean = true;            // true or false
let nul: null = null;                // Intentional absence
let undef: undefined = undefined;    // Uninitialized
let big: bigint = 100n;              // Large integers
let sym: symbol = Symbol("id");      // Unique identifiers (rarely used)

// ═══════════════════════════════════════════
// SPECIAL TYPES
// ═══════════════════════════════════════════

let anything: any;       // ⚠️ ESCAPE HATCH — disables ALL type checking
                         // Literally: "I don't care, let me do anything"
                         // Use only when migrating JS or dealing with broken types

let unknown: unknown;    // ✅ SAFE alternative to any — "I don't know what this is"
                         // You MUST narrow it before using it

let nothing: void;       // Return type of functions that don't return a value
let impossible: never;   // A type that can never exist (exhaustive checks, thrown errors)

// ═══════════════════════════════════════════
// any vs unknown — THE CRITICAL DIFFERENCE
// ═══════════════════════════════════════════

function dangerouslyProcess(data: any) {
  data.foo.bar.baz();            // ✅ Compiles. No checking. May crash at runtime.
  return data.name.toUpperCase(); // ✅ Compiles. No checking. Probably crashes.
}

function safelyProcess(data: unknown) {
  data.foo.bar.baz();            // ❌ ERROR: Object is of type 'unknown'
  
  // You MUST narrow first:
  if (typeof data === 'object' && data !== null && 'name' in data) {
    const name = (data as { name: string }).name;
    return name.toUpperCase();   // ✅ Now safe
  }
}

// RULE: Use `unknown` for data from external sources (API responses, user input).
// RULE: Use `any` only when migrating JS code and you'll fix it later.
```

### `void` and `never` — Two Sides of Nothing

```typescript
// void = "this function returns, but with no value"
function logMessage(msg: string): void {
  console.log(msg);
  // implicitly returns undefined
}

// never = "this function NEVER returns" (throws or infinite loop)
function throwError(msg: string): never {
  throw new Error(msg);
  // code after throw is unreachable — return type is 'never'
}

// never is also used for EXHAUSTIVE CHECKS:
type Status = 'pending' | 'done';

function handleStatus(status: Status) {
  switch (status) {
    case 'pending': return '⏳';
    case 'done': return '✅';
    default:
      // If you add a new status to the union but forget to handle it here,
      // TypeScript will error because `status` is not assignable to `never`
      const exhaustiveCheck: never = status;
      return exhaustiveCheck;
  }
}
```

---

## 5. Object Types — Shapes of Data

### Interfaces vs Type Aliases

```typescript
// ═══════════════════════════════════════════
// INTERFACE — describes the shape of an object
// ═══════════════════════════════════════════
interface User {
  id: number;
  name: string;
  email: string;
  avatar?: string;          // ? means optional (string | undefined)
  readonly createdAt: Date;  // readonly — can't be reassigned after creation
}

// ═══════════════════════════════════════════
// TYPE ALIAS — gives a name to ANY type
// ═══════════════════════════════════════════
type UserID = number;
type Status = 'pending' | 'active' | 'banned';
type Coordinate = [number, number];   // tuple
type Handler = (event: Event) => void; // function type

// Can also describe object shapes (identical to interface for objects):
type Product = {
  id: number;
  name: string;
  price: number;
};
```

### When to Use Which?

```
┌────────────────────────────────────────────────────────────┐
│              INTERFACE vs TYPE — DECISION GUIDE             │
├────────────────────────────────────────────────────────────┤
│                                                             │
│  Use INTERFACE when:                                        │
│  • Defining the shape of an object or class                 │
│  • You want declaration merging (extending in .d.ts files)  │
│  • Defining component props                                 │
│  • Defining API response shapes                             │
│                                                             │
│  Use TYPE when:                                             │
│  • Creating unions:  type Status = 'a' | 'b' | 'c'         │
│  • Creating tuples:  type Pair = [string, number]           │
│  • Creating mapped/conditional types                        │
│  • Giving a name to a function signature                    │
│  • Any type that ISN'T purely an object shape               │
│                                                             │
│  In practice: Use interface for props/data shapes.          │
│  Use type for everything else. Don't overthink it.          │
└────────────────────────────────────────────────────────────┘
```

### Extending & Composing

```typescript
// INTERFACE extends interface
interface Animal {
  name: string;
  age: number;
}

interface Dog extends Animal {
  breed: string;
  bark(): void;
}

// TYPE intersects type
type Animal2 = {
  name: string;
  age: number;
};

type Dog2 = Animal2 & {
  breed: string;
  bark(): void;
};

// They produce the SAME result. The & operator is called "intersection".
```

### Index Signatures — Dynamic Keys

```typescript
// When you don't know the exact property names:
interface ApiResponse {
  [key: string]: unknown;    // Any string key, unknown value
}

// More specific:
interface StringMap {
  [key: string]: string;     // Any string key, string value
}

// Record<K, V> is the utility type equivalent:
type StringMap2 = Record<string, string>;  // Same thing

// STS pattern — API responses keyed by endpoint URL:
interface BatchApiResult {
  [endpointUrl: string]: {
    success: boolean;
    data: unknown;
    status: number;
  };
}
```

### Readonly & Immutability

```typescript
// Readonly properties
interface Config {
  readonly apiUrl: string;
  readonly timeout: number;
}

const config: Config = { apiUrl: 'https://api.example.com', timeout: 10000 };
config.apiUrl = 'nope';  // ❌ ERROR: Cannot assign to 'apiUrl' because it is read-only

// Readonly arrays
const ids: readonly number[] = [1, 2, 3];
ids.push(4);     // ❌ ERROR: Property 'push' does not exist on type 'readonly number[]'
ids[0] = 99;     // ❌ ERROR

// Deep readonly (use Readonly<T> utility):
type DeepUser = Readonly<User>;
// All properties are now readonly
```

---

## 6. Union & Intersection — Combining Types

### Union ( | ) — "this OR that"

```typescript
// A value that can be ONE of several types
type StringOrNumber = string | number;

let value: StringOrNumber;
value = "hello";  // ✅
value = 42;       // ✅
value = true;     // ❌ boolean is not string | number

// DISCRIMINATED UNIONS — the most powerful pattern in TypeScript
// (You'll use this EVERYWHERE in the STS rebuild)

type ApiResult<T> =
  | { success: true; data: T }                          // success case
  | { success: false; error: string; statusCode: number } // error case

function handleResult(result: ApiResult<User>) {
  if (result.success) {
    // TypeScript KNOWS result is { success: true; data: User } here
    console.log(result.data.name);    // ✅ Safe — data exists
    console.log(result.error);        // ❌ ERROR — error doesn't exist on success branch
  } else {
    // TypeScript KNOWS result is { success: false; error: string; ... } here
    console.log(result.error);        // ✅ Safe
    console.log(result.data);         // ❌ ERROR — data doesn't exist on error branch
  }
}
```

### Intersection ( & ) — "this AND that"

```typescript
// A value that has ALL properties from BOTH types
type HasName = { name: string };
type HasAge = { age: number };
type Person = HasName & HasAge;
// Person = { name: string; age: number }

// Practical use: extend an API response with local state
type ApiUser = {
  id: number;
  name: string;
  email: string;
};

type LocalUser = ApiUser & {
  isOnline: boolean;
  lastSeen: Date;
};
// LocalUser has all ApiUser fields PLUS isOnline and lastSeen
```

### The Mental Model

```
┌─────────────────────────────────────────────────────────────┐
│  UNION (|):   The VALUE can be ANY ONE of the types.         │
│               The TYPE is the SET OF ALL POSSIBLE values.    │
│               You can only access SHARED members.            │
│                                                              │
│  string | number                                             │
│  ┌──────────┐                                                │
│  │ "hello"  │ ← could be this                                │
│  │ "world"  │                                                │
│  │ 42       │ ← or this                                      │
│  │ 3.14     │                                                │
│  └──────────┘                                                │
│  You can call: .toString() (shared by both)                  │
│  You CANNOT call: .toUpperCase() (string only — narrow first)│
│                                                              │
│  INTERSECTION (&): The VALUE must satisfy ALL types.          │
│                    The TYPE has ALL members from BOTH.        │
│                                                              │
│  HasName & HasAge                                            │
│  ┌──────────────────────┐                                    │
│  │ { name: "Alex",     │ ← must have BOTH                   │
│  │   age: 30 }          │                                    │
│  └──────────────────────┘                                    │
│  You can access: .name AND .age (both guaranteed)            │
└─────────────────────────────────────────────────────────────┘
```

---

## 7. Type Narrowing — The Compiler Thinks With You

**Narrowing** is TypeScript's ability to refine a type based on runtime checks. This is what makes the type system feel magical — the compiler follows your `if` statements and `switch` cases.

```typescript
// ═══════════════════════════════════════════
// typeof narrowing
// ═══════════════════════════════════════════
function process(value: string | number) {
  // Here, value is: string | number

  if (typeof value === 'string') {
    // Here, value is: string ← TypeScript narrowed it!
    return value.toUpperCase();     // ✅ .toUpperCase() exists on string
  }

  // Here, value is: number ← TypeScript eliminated string
  return value.toFixed(2);          // ✅ .toFixed() exists on number
}


// ═══════════════════════════════════════════
// Truthiness narrowing
// ═══════════════════════════════════════════
function greet(name: string | null | undefined) {
  if (name) {
    // name is: string (null and undefined are falsy, eliminated)
    return `Hello, ${name}`;
  }
  return 'Hello, stranger';
}


// ═══════════════════════════════════════════
// in operator narrowing
// ═══════════════════════════════════════════
type Fish = { swim: () => void };
type Bird = { fly: () => void };

function move(animal: Fish | Bird) {
  if ('swim' in animal) {
    animal.swim();   // animal is Fish
  } else {
    animal.fly();    // animal is Bird
  }
}


// ═══════════════════════════════════════════
// instanceof narrowing
// ═══════════════════════════════════════════
function formatError(error: unknown) {
  if (error instanceof Error) {
    return error.message;    // error is Error
  }
  return String(error);
}


// ═══════════════════════════════════════════
// Discriminated union narrowing (★ MOST IMPORTANT ★)
// ═══════════════════════════════════════════
type LoadingState = { status: 'loading' };
type SuccessState<T> = { status: 'success'; data: T };
type ErrorState = { status: 'error'; message: string };

type AsyncState<T> = LoadingState | SuccessState<T> | ErrorState;

function renderState(state: AsyncState<User[]>) {
  switch (state.status) {
    case 'loading':
      return <LoadingSpinner />;          // state is LoadingState
    case 'success':
      return <UserList users={state.data} />;  // state is SuccessState<User[]>
    case 'error':
      return <ErrorBanner message={state.message} />;  // state is ErrorState
  }
}


// ═══════════════════════════════════════════
// Type predicates (custom narrowing functions)
// ═══════════════════════════════════════════
function isString(value: unknown): value is string {
  return typeof value === 'string';
}

function isUser(obj: unknown): obj is User {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'id' in obj &&
    'name' in obj &&
    'email' in obj
  );
}

// Usage:
const data: unknown = await fetchSomething();
if (isUser(data)) {
  console.log(data.name);  // ✅ TypeScript knows data is User now
}


// ═══════════════════════════════════════════
// Non-null assertion (!)  ← use SPARINGLY
// ═══════════════════════════════════════════
const element = document.getElementById('root');
// element is: HTMLElement | null

element!.style.color = 'red';
// The ! tells TypeScript: "I PROMISE this is not null"
// If you're wrong, it crashes at runtime. Use only when you truly know.
```

---

## 8. Literal Types & const Assertions

```typescript
// ═══════════════════════════════════════════
// LITERAL TYPES — a type that is ONE specific value
// ═══════════════════════════════════════════

let mutable = "hello";      // Type: string (can be reassigned to any string)
const immutable = "hello";  // Type: "hello" (literal type — this exact string)

// Why? Because `const` can never change, TS narrows to the exact value.

type Direction = 'up' | 'down' | 'left' | 'right';  // Union of literal types

function move(direction: Direction) { /* ... */ }
move('up');      // ✅
move('diagonal'); // ❌ Type '"diagonal"' is not assignable to type 'Direction'


// ═══════════════════════════════════════════
// const ASSERTIONS — make EVERYTHING literal
// ═══════════════════════════════════════════

// Without `as const`:
const config = {
  apiUrl: 'https://api.example.com',  // Type: string
  timeout: 10000,                      // Type: number
  retries: 3,                          // Type: number
};
// config type: { apiUrl: string; timeout: number; retries: number }

// With `as const`:
const config2 = {
  apiUrl: 'https://api.example.com',  // Type: "https://api.example.com"
  timeout: 10000,                      // Type: 10000
  retries: 3,                          // Type: 3
} as const;
// config2 type: {
//   readonly apiUrl: "https://api.example.com";
//   readonly timeout: 10000;
//   readonly retries: 3;
// }

// as const also works with arrays:
const STATUSES = ['pending', 'active', 'done'] as const;
// Type: readonly ["pending", "active", "done"]

type Status = typeof STATUSES[number];
// Type: "pending" | "active" | "done"
// ↑ This pattern extracts a union type from a const array. You'll use this a LOT.
```

---

## 9. Enums vs Union Literals

```typescript
// ═══════════════════════════════════════════
// ENUM (TypeScript-specific construct)
// ═══════════════════════════════════════════
enum TaskStatus {
  Pending = 'pending',
  InProgress = 'in_progress',
  Done = 'done',
}

// Usage:
let status: TaskStatus = TaskStatus.Pending;

// ⚠️ PROBLEM: Enums generate runtime JavaScript code:
// var TaskStatus;
// (function (TaskStatus) {
//     TaskStatus["Pending"] = "pending";
//     ...
// })(TaskStatus || (TaskStatus = {}));
// That's real code that ships to your users.


// ═══════════════════════════════════════════
// UNION LITERAL (preferred in modern TS)
// ═══════════════════════════════════════════
type TaskStatus2 = 'pending' | 'in_progress' | 'done';

// Usage:
let status2: TaskStatus2 = 'pending';

// ✅ ADVANTAGE: Zero runtime cost. Types are erased. Nothing ships.
// ✅ ADVANTAGE: Works with `as const` arrays for iteration:

const TASK_STATUSES = ['pending', 'in_progress', 'done'] as const;
type TaskStatus3 = typeof TASK_STATUSES[number];  // Same union type
// AND you can iterate: TASK_STATUSES.forEach(s => ...)


// ═══════════════════════════════════════════
// VERDICT
// ═══════════════════════════════════════════
// Use UNION LITERALS for the STS rebuild. Not enums.
// Enums add runtime code, can't be tree-shaken, and break isolatedModules.
// Union literals are simpler, lighter, and idiomatic modern TypeScript.
```

---

# Part III — Generics (The Power Tool)

## 10. Generics — Types That Take Parameters

Generics let you write code that works with **any type** while preserving type safety. Think of them as **type-level functions**.

```typescript
// ═══════════════════════════════════════════
// THE PROBLEM: Repeating yourself for each type
// ═══════════════════════════════════════════

// Without generics, you'd need separate functions:
function wrapString(value: string): { value: string } {
  return { value };
}
function wrapNumber(value: number): { value: number } {
  return { value };
}
// ... one for every type? Terrible.


// ═══════════════════════════════════════════
// THE SOLUTION: Generics
// ═══════════════════════════════════════════

function wrap<T>(value: T): { value: T } {
  return { value };
}
// T is a TYPE PARAMETER — a placeholder that gets filled in when you call the function.

const a = wrap("hello");    // T = string  → { value: string }
const b = wrap(42);         // T = number  → { value: number }
const c = wrap(true);       // T = boolean → { value: boolean }
// TypeScript INFERS T from the argument. You rarely need to specify it.

// You CAN be explicit:
const d = wrap<string>("hello");  // Explicit: T = string
```

### Generic Interfaces and Types

```typescript
// ═══════════════════════════════════════════
// Generic API Response (you'll use this EVERYWHERE)
// ═══════════════════════════════════════════
interface ApiResponse<T> {
  success: boolean;
  data: T;
  pagination?: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

// Now you can type every API response precisely:
type UserResponse = ApiResponse<User>;
// { success: boolean; data: User; pagination?: ... }

type FeedListResponse = ApiResponse<FeedPost[]>;
// { success: boolean; data: FeedPost[]; pagination?: ... }

type LoginResponse = ApiResponse<{ user: User; access_token: string }>;
// { success: boolean; data: { user: User; access_token: string }; ... }


// ═══════════════════════════════════════════
// Generic State Slice
// ═══════════════════════════════════════════
interface AsyncSliceState<T> {
  data: T | null;
  loading: boolean;
  error: string | null;
}

// Reuse for any feature:
type FeedState = AsyncSliceState<FeedPost[]>;
type ProfileState = AsyncSliceState<UserProfile>;
type LeaderboardState = AsyncSliceState<LeaderboardEntry[]>;
```

### Multiple Type Parameters

```typescript
// Functions can take multiple type parameters:
function createPair<A, B>(first: A, second: B): [A, B] {
  return [first, second];
}

const pair = createPair("hello", 42);  // [string, number]

// Practical example — a key-value cache:
class Cache<K, V> {
  private store = new Map<K, V>();

  set(key: K, value: V): void {
    this.store.set(key, value);
  }

  get(key: K): V | undefined {
    return this.store.get(key);
  }
}

const userCache = new Cache<number, User>();   // Cache<number, User>
userCache.set(1, { id: 1, name: 'Alex' });     // ✅
userCache.set("one", { id: 1, name: 'Alex' }); // ❌ string is not number
```

---

## 11. Generic Constraints — Bounding the Unknown

```typescript
// ═══════════════════════════════════════════
// PROBLEM: T is TOO open — any type is allowed
// ═══════════════════════════════════════════
function getLength<T>(value: T): number {
  return value.length;  // ❌ ERROR: Property 'length' does not exist on type 'T'
  // T could be `number`, which has no .length
}


// ═══════════════════════════════════════════
// SOLUTION: Constrain T with `extends`
// ═══════════════════════════════════════════
function getLength<T extends { length: number }>(value: T): number {
  return value.length;  // ✅ T is guaranteed to have .length
}

getLength("hello");       // ✅ string has .length
getLength([1, 2, 3]);     // ✅ array has .length
getLength(42);            // ❌ number doesn't have .length


// ═══════════════════════════════════════════
// keyof constraint — accessing object properties safely
// ═══════════════════════════════════════════
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: 'Alex', age: 30, email: 'alex@test.com' };

getProperty(user, 'name');    // ✅ returns string
getProperty(user, 'age');     // ✅ returns number
getProperty(user, 'address'); // ❌ '"address"' is not assignable to '"name" | "age" | "email"'

// T[K] is an INDEXED ACCESS TYPE — it gives you the type of the property at key K.
// If T is User and K is 'name', then T[K] is string.
```

---

## 12. Generic Inference — Let the Compiler Do the Work

```typescript
// TypeScript infers generic parameters from usage.
// You almost NEVER need to write them explicitly.

// Array methods infer T from the array:
const numbers = [1, 2, 3];               // number[]
const doubled = numbers.map(n => n * 2);  // number[] — T inferred as number

// Promise infers T from the resolved value:
async function fetchUser(): Promise<User> {
  const response = await api.get<User>('/me');
  return response.data;  // TypeScript knows this is User
}

// useState infers T from initial value:
const [count, setCount] = useState(0);        // useState<number>
const [name, setName] = useState('');          // useState<string>
const [user, setUser] = useState<User | null>(null);  // Must be explicit when initial is null

// RULE OF THUMB:
// If TypeScript can infer it → don't write it.
// If the initial value doesn't tell the full story (e.g., null) → specify explicitly.
```

---

# Part IV — Advanced Type System

## 13. Conditional Types — if/else for Types

```typescript
// Syntax: T extends U ? X : Y
// "If T is assignable to U, the type is X. Otherwise, Y."

type IsString<T> = T extends string ? true : false;

type A = IsString<string>;    // true
type B = IsString<number>;    // false
type C = IsString<'hello'>;   // true (literal 'hello' extends string)


// ═══════════════════════════════════════════
// PRACTICAL: Extract the return type of a function
// ═══════════════════════════════════════════
type ReturnOf<T> = T extends (...args: any[]) => infer R ? R : never;

type X = ReturnOf<() => string>;         // string
type Y = ReturnOf<(x: number) => boolean>; // boolean

// `infer R` says: "Whatever the return type is, capture it as R"
// This is how the built-in ReturnType<T> utility works.


// ═══════════════════════════════════════════
// PRACTICAL: Unwrap a Promise
// ═══════════════════════════════════════════
type Unwrap<T> = T extends Promise<infer U> ? U : T;

type P = Unwrap<Promise<User>>;   // User
type Q = Unwrap<string>;          // string (not a Promise, pass through)


// ═══════════════════════════════════════════
// PRACTICAL: API response narrowing
// ═══════════════════════════════════════════
type ExtractData<T> = T extends { success: true; data: infer D } ? D : never;

type FeedData = ExtractData<{ success: true; data: FeedPost[] }>;  // FeedPost[]
type ErrorData = ExtractData<{ success: false; error: string }>;    // never
```

---

## 14. Mapped Types — Transform Every Property

```typescript
// Mapped types iterate over keys and transform each property.

// ═══════════════════════════════════════════
// Make all properties optional
// ═══════════════════════════════════════════
type MyPartial<T> = {
  [K in keyof T]?: T[K];
};
// This is how Partial<T> works internally.

// ═══════════════════════════════════════════
// Make all properties required
// ═══════════════════════════════════════════
type MyRequired<T> = {
  [K in keyof T]-?: T[K];   // -? removes the optional modifier
};

// ═══════════════════════════════════════════
// Make all properties readonly
// ═══════════════════════════════════════════
type MyReadonly<T> = {
  readonly [K in keyof T]: T[K];
};

// ═══════════════════════════════════════════
// PRACTICAL: Form state where all fields are strings (from TextInput)
// ═══════════════════════════════════════════
interface TaskForm {
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high';
  status: 'pending' | 'in_progress' | 'done';
}

// Form errors: same keys, but values are string | undefined
type FormErrors<T> = {
  [K in keyof T]?: string;
};

type TaskFormErrors = FormErrors<TaskForm>;
// { title?: string; description?: string; priority?: string; status?: string }

// Form touched state: same keys, but values are boolean
type FormTouched<T> = {
  [K in keyof T]?: boolean;
};
```

---

## 15. Template Literal Types — String Manipulation at Type Level

```typescript
// TypeScript can manipulate strings AT THE TYPE LEVEL.

type EventName = `on${Capitalize<string>}`;
// Matches: "onClick", "onScroll", "onSubmit", etc.

// ═══════════════════════════════════════════
// PRACTICAL: API endpoint builder
// ═══════════════════════════════════════════
type ApiVersion = 'v1' | 'v2';
type Resource = 'users' | 'posts' | 'tasks';
type Endpoint = `/api/${ApiVersion}/${Resource}`;
// "/api/v1/users" | "/api/v1/posts" | "/api/v1/tasks" |
// "/api/v2/users" | "/api/v2/posts" | "/api/v2/tasks"

// ═══════════════════════════════════════════
// PRACTICAL: Redux action types
// ═══════════════════════════════════════════
type SliceName = 'feed' | 'auth' | 'ui';
type ActionSuffix = 'pending' | 'fulfilled' | 'rejected';
type ActionType = `${SliceName}/${string}/${ActionSuffix}`;
// "feed/fetchFeed/pending" | "auth/login/fulfilled" | etc.
```

---

## 16. Utility Types — The Standard Library

TypeScript ships built-in generic types that transform other types. Know these by heart:

```typescript
// ═══════════════════════════════════════════
// Partial<T> — make all properties optional
// ═══════════════════════════════════════════
interface User {
  id: number;
  name: string;
  email: string;
}

type PartialUser = Partial<User>;
// { id?: number; name?: string; email?: string }

// USE CASE: Update functions where you only send changed fields
function updateUser(id: number, updates: Partial<User>): void {
  // updates can have any subset of User fields
}
updateUser(1, { name: 'New Name' });  // ✅ Only name


// ═══════════════════════════════════════════
// Required<T> — make all properties required
// ═══════════════════════════════════════════
interface Config {
  apiUrl?: string;
  timeout?: number;
}

type RequiredConfig = Required<Config>;
// { apiUrl: string; timeout: number }


// ═══════════════════════════════════════════
// Pick<T, Keys> — select specific properties
// ═══════════════════════════════════════════
type UserPreview = Pick<User, 'id' | 'name'>;
// { id: number; name: string }


// ═══════════════════════════════════════════
// Omit<T, Keys> — remove specific properties
// ═══════════════════════════════════════════
type UserWithoutEmail = Omit<User, 'email'>;
// { id: number; name: string }

// USE CASE: API create payload (server generates id)
type CreateUserPayload = Omit<User, 'id'>;
// { name: string; email: string }


// ═══════════════════════════════════════════
// Record<Keys, Value> — object with known key type
// ═══════════════════════════════════════════
type StatusColors = Record<TaskStatus, string>;
// { pending: string; in_progress: string; done: string }

const colors: StatusColors = {
  pending: '#F59E0B',
  in_progress: '#3B82F6',
  done: '#22C55E',
};


// ═══════════════════════════════════════════
// Extract<T, U> — extract members from a union
// ═══════════════════════════════════════════
type AllTypes = string | number | boolean | null;
type OnlyStringOrNumber = Extract<AllTypes, string | number>;
// string | number


// ═══════════════════════════════════════════
// Exclude<T, U> — remove members from a union
// ═══════════════════════════════════════════
type NonNull = Exclude<AllTypes, null>;
// string | number | boolean


// ═══════════════════════════════════════════
// NonNullable<T> — remove null and undefined
// ═══════════════════════════════════════════
type MaybeUser = User | null | undefined;
type DefiniteUser = NonNullable<MaybeUser>;
// User


// ═══════════════════════════════════════════
// ReturnType<T> — get return type of a function
// ═══════════════════════════════════════════
function createUser() {
  return { id: 1, name: 'Alex', email: 'alex@test.com' };
}
type CreatedUser = ReturnType<typeof createUser>;
// { id: number; name: string; email: string }


// ═══════════════════════════════════════════
// Parameters<T> — get parameter types of a function
// ═══════════════════════════════════════════
function greet(name: string, age: number): string {
  return `${name} is ${age}`;
}
type GreetParams = Parameters<typeof greet>;
// [name: string, age: number]


// ═══════════════════════════════════════════
// Awaited<T> — unwrap Promise types
// ═══════════════════════════════════════════
type P = Awaited<Promise<Promise<string>>>;
// string (unwraps all layers)
```

### Cheat Sheet

```
┌──────────────────────────────────────────────────────────────┐
│              UTILITY TYPES — QUICK REFERENCE                  │
├──────────────────┬───────────────────────────────────────────┤
│  Utility         │  What it does                             │
├──────────────────┼───────────────────────────────────────────┤
│  Partial<T>      │  All props optional                       │
│  Required<T>     │  All props required                       │
│  Readonly<T>     │  All props readonly                       │
│  Pick<T, K>      │  Only keep listed props                   │
│  Omit<T, K>      │  Remove listed props                      │
│  Record<K, V>    │  Object with key type K, value type V     │
│  Extract<T, U>   │  Keep union members assignable to U       │
│  Exclude<T, U>   │  Remove union members assignable to U     │
│  NonNullable<T>  │  Remove null and undefined                │
│  ReturnType<T>   │  Return type of function T                │
│  Parameters<T>   │  Parameter tuple of function T            │
│  Awaited<T>      │  Unwrap Promise<T>                        │
│  InstanceType<T> │  Instance type of constructor T           │
└──────────────────┴───────────────────────────────────────────┘
```

---

## 17. Type Assertions & Escape Hatches

```typescript
// ═══════════════════════════════════════════
// Type Assertion (as) — "Trust me, I know the type"
// ═══════════════════════════════════════════
const input = document.getElementById('email') as HTMLInputElement;
input.value = 'test@example.com';  // ✅ Without assertion, TS only knows HTMLElement | null

// ⚠️ Assertions DON'T perform any runtime check. If you're wrong, it crashes.
const data = JSON.parse(rawString) as User;  // If rawString is garbage, data is garbage.


// ═══════════════════════════════════════════
// Double assertion — when TS won't let you assert directly
// ═══════════════════════════════════════════
const value = "hello" as unknown as number;  // ← This is almost always wrong.
// Only use this for testing mocks or extremely unusual interop.


// ═══════════════════════════════════════════
// @ts-ignore / @ts-expect-error — line-level escape
// ═══════════════════════════════════════════
// @ts-ignore — Suppresses the error on the next line (even if there's no error)
// @ts-expect-error — Suppresses the error, but ERRORS if there IS no error to suppress
//                     (better — tells you when the fix makes the suppression unnecessary)

// @ts-expect-error — third-party library has wrong types
const result = brokenLibrary.doThing(123);


// ═══════════════════════════════════════════
// RULE: Escape hatch hierarchy
// ═══════════════════════════════════════════
// 1. Fix the type properly                        ← Best
// 2. Use a type predicate (is guard)              ← Good
// 3. Use type assertion (as)                      ← OK if you truly know
// 4. Use @ts-expect-error with a comment          ← Last resort
// 5. Use `any`                                    ← Surrender
```

---

## 18. Declaration Files & the `declare` Keyword

```typescript
// ═══════════════════════════════════════════
// .d.ts FILES — Type-only files (no runtime code)
// ═══════════════════════════════════════════

// When you install a package like `axios`, it comes with a .d.ts file
// that tells TypeScript what types axios exports:
// node_modules/axios/index.d.ts

// When a package doesn't include types, you install them separately:
// yarn add --dev @types/react-native-vector-icons

// The @types/ packages are from DefinitelyTyped — a community repo of type definitions.


// ═══════════════════════════════════════════
// declare — tell TS about things that exist at runtime
// ═══════════════════════════════════════════

// Declare a global variable that exists (e.g., injected by native code):
declare const __DEV__: boolean;   // React Native injects this

// Declare a module that has no types:
declare module 'react-native-snap-carousel' {
  import { Component } from 'react';
  import { FlatListProps } from 'react-native';

  export interface CarouselProps<T> extends FlatListProps<T> {
    sliderWidth: number;
    itemWidth: number;
    loop?: boolean;
  }

  export default class Carousel<T> extends Component<CarouselProps<T>> {}
}

// Declare module to augment existing types:
declare module 'react-native' {
  interface TextProps {
    customProp?: string;  // Add custom prop to all Text components
  }
}


// ═══════════════════════════════════════════
// Where to put declarations in your project
// ═══════════════════════════════════════════
// Create: src/types/global.d.ts
// Add declarations for untyped modules, global variables, etc.
// TypeScript automatically picks up .d.ts files in your `include` paths.
```

---

# Part V — TypeScript in React Native

## 19. React + TypeScript Fundamentals

### The Core Types You Need

```typescript
import React from 'react';

// ═══════════════════════════════════════════
// React.FC (Function Component) — DON'T use it
// ═══════════════════════════════════════════
// React.FC<Props> was once recommended. It's now considered a bad pattern because:
// 1. It implicitly adds `children` to every component (even if you don't want them)
// 2. It breaks generic components
// 3. It provides no benefit over plain function typing

// ❌ Old pattern (don't do this):
const Bad: React.FC<{ name: string }> = ({ name }) => { /* ... */ };

// ✅ Modern pattern (do this):
interface GreetingProps {
  name: string;
  age?: number;
}

function Greeting({ name, age }: GreetingProps) {
  return <Text>{name}{age ? `, age ${age}` : ''}</Text>;
}

// Or as arrow function:
const Greeting2 = ({ name, age }: GreetingProps) => {
  return <Text>{name}{age ? `, age ${age}` : ''}</Text>;
};


// ═══════════════════════════════════════════
// Children
// ═══════════════════════════════════════════
interface CardProps {
  title: string;
  children: React.ReactNode;   // Anything renderable: string, number, JSX, array, null
}

function Card({ title, children }: CardProps) {
  return (
    <View>
      <Text>{title}</Text>
      {children}
    </View>
  );
}

// More specific children types:
interface Props {
  children: React.ReactElement;     // Must be JSX (not string/number)
  children: string;                  // Must be a string
  children: React.ReactNode;        // Anything (most common)
  children: (data: User) => React.ReactNode;  // Render prop pattern
}


// ═══════════════════════════════════════════
// Event Handlers
// ═══════════════════════════════════════════
import { GestureResponderEvent, NativeSyntheticEvent, TextInputChangeEventData } from 'react-native';

interface ButtonProps {
  onPress: (event: GestureResponderEvent) => void;
  onLongPress?: (event: GestureResponderEvent) => void;
}

interface InputProps {
  onChangeText: (text: string) => void;
  onSubmitEditing: () => void;
}


// ═══════════════════════════════════════════
// Style Props
// ═══════════════════════════════════════════
import { ViewStyle, TextStyle, ImageStyle, StyleProp } from 'react-native';

interface StyledComponentProps {
  style?: StyleProp<ViewStyle>;         // For View-based components
  textStyle?: StyleProp<TextStyle>;     // For Text-based components
  imageStyle?: StyleProp<ImageStyle>;   // For Image-based components
}
// StyleProp<T> allows: T, T[], false, null, undefined (all the things you can pass to style)
```

---

## 20. React Native Components — Typed from Scratch

### A Complete Component Example

```typescript
import React, { useState, useCallback } from 'react';
import {
  View,
  Text,
  TouchableOpacity,
  FlatList,
  StyleSheet,
  StyleProp,
  ViewStyle,
  ActivityIndicator,
  RefreshControl,
} from 'react-native';

// ═══════════════════════════════════════════
// 1. Define the data type
// ═══════════════════════════════════════════
interface Task {
  id: number;
  title: string;
  description: string;
  status: 'pending' | 'in_progress' | 'done';
  priority: 'low' | 'medium' | 'high';
}

// ═══════════════════════════════════════════
// 2. Define component props
// ═══════════════════════════════════════════
interface TaskCardProps {
  task: Task;
  onPress: (task: Task) => void;
  onDelete: (id: number) => void;
  style?: StyleProp<ViewStyle>;
}

// ═══════════════════════════════════════════
// 3. Build the component
// ═══════════════════════════════════════════
function TaskCard({ task, onPress, onDelete, style }: TaskCardProps) {
  const handlePress = useCallback(() => {
    onPress(task);
  }, [task, onPress]);

  const handleDelete = useCallback(() => {
    onDelete(task.id);
  }, [task.id, onDelete]);

  return (
    <TouchableOpacity
      style={[styles.card, style]}
      onPress={handlePress}
      activeOpacity={0.7}
    >
      <View style={styles.header}>
        <Text style={styles.title}>{task.title}</Text>
        <StatusBadge status={task.status} />
      </View>
      <Text style={styles.description}>{task.description}</Text>
      <TouchableOpacity onPress={handleDelete}>
        <Text style={styles.deleteText}>Delete</Text>
      </TouchableOpacity>
    </TouchableOpacity>
  );
}

// ═══════════════════════════════════════════
// 4. Build the list component
// ═══════════════════════════════════════════
interface TaskListProps {
  tasks: Task[];
  loading: boolean;
  onRefresh: () => void;
  onTaskPress: (task: Task) => void;
  onTaskDelete: (id: number) => void;
  onEndReached: () => void;
}

function TaskList({
  tasks,
  loading,
  onRefresh,
  onTaskPress,
  onTaskDelete,
  onEndReached,
}: TaskListProps) {
  // FlatList renderItem receives { item, index, separators }
  // The generic <Task> tells FlatList what type `item` is
  const renderItem = useCallback(
    ({ item }: { item: Task }) => (
      <TaskCard
        task={item}
        onPress={onTaskPress}
        onDelete={onTaskDelete}
      />
    ),
    [onTaskPress, onTaskDelete],
  );

  const keyExtractor = useCallback(
    (item: Task) => item.id.toString(),
    [],
  );

  return (
    <FlatList<Task>                      // ← Generic type parameter
      data={tasks}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      refreshControl={
        <RefreshControl refreshing={loading} onRefresh={onRefresh} />
      }
      onEndReached={onEndReached}
      onEndReachedThreshold={0.5}
      ListEmptyComponent={
        loading ? <ActivityIndicator /> : <Text>No tasks</Text>
      }
    />
  );
}
```

### Generic Components (Reusable Lists)

```typescript
// A generic list component that works with ANY data type:
interface GenericListProps<T> {
  data: T[];
  renderItem: (item: T, index: number) => React.ReactElement;
  keyExtractor: (item: T) => string;
  loading?: boolean;
  onRefresh?: () => void;
  emptyMessage?: string;
}

function GenericList<T>({
  data,
  renderItem,
  keyExtractor,
  loading = false,
  onRefresh,
  emptyMessage = 'No items',
}: GenericListProps<T>) {
  return (
    <FlatList
      data={data}
      renderItem={({ item, index }) => renderItem(item, index)}
      keyExtractor={keyExtractor}
      refreshControl={
        onRefresh ? <RefreshControl refreshing={loading} onRefresh={onRefresh} /> : undefined
      }
      ListEmptyComponent={<Text>{emptyMessage}</Text>}
    />
  );
}

// Usage — TypeScript infers T from the `data` prop:
<GenericList
  data={users}                           // T = User (inferred)
  renderItem={(user) => <UserCard user={user} />}  // user is User
  keyExtractor={(user) => user.id.toString()}       // user is User
/>
```

---

## 21. Hooks — Every Hook Typed

```typescript
// ═══════════════════════════════════════════
// useState
// ═══════════════════════════════════════════

// Inferred from initial value:
const [count, setCount] = useState(0);             // useState<number>
const [name, setName] = useState('');              // useState<string>
const [items, setItems] = useState<Task[]>([]);    // Must specify — [] is never[]

// Explicit when initial doesn't match eventual type:
const [user, setUser] = useState<User | null>(null);
const [error, setError] = useState<string | null>(null);

// COMMON MISTAKE:
const [data, setData] = useState([]);  // ← Type is never[] — you can never push anything!
const [data2, setData2] = useState<Task[]>([]);  // ← Correct


// ═══════════════════════════════════════════
// useRef
// ═══════════════════════════════════════════

// For DOM/native element refs:
const inputRef = useRef<TextInput>(null);
// inputRef.current is TextInput | null

// For mutable values (like instance variables):
const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null);
// OR more simply:
const timerRef2 = useRef<NodeJS.Timeout | null>(null);

// For scroll position tracking:
const scrollRef = useRef<FlatList<Task>>(null);


// ═══════════════════════════════════════════
// useEffect / useLayoutEffect
// ═══════════════════════════════════════════

// No type parameters needed — just type the cleanup function correctly:
useEffect(() => {
  const subscription = someObservable.subscribe();
  return () => {
    subscription.unsubscribe();   // Cleanup function returns void
  };
}, []);

// Async effects — you can't make the callback async directly:
useEffect(() => {
  async function fetchData() {
    const result = await api.get<User>('/me');
    setUser(result.data);
  }
  fetchData();
}, []);


// ═══════════════════════════════════════════
// useCallback
// ═══════════════════════════════════════════

// TypeScript infers the callback type:
const handlePress = useCallback((task: Task) => {
  navigation.navigate('TaskDetail', { taskId: task.id });
}, [navigation]);
// handlePress type: (task: Task) => void


// ═══════════════════════════════════════════
// useMemo
// ═══════════════════════════════════════════

// TypeScript infers the return type:
const filteredTasks = useMemo(
  () => tasks.filter(t => t.status === selectedStatus),
  [tasks, selectedStatus],
);
// filteredTasks type: Task[]


// ═══════════════════════════════════════════
// useReducer
// ═══════════════════════════════════════════

// Define state and action types:
interface FormState {
  title: string;
  description: string;
  priority: 'low' | 'medium' | 'high';
  errors: Record<string, string>;
  isSubmitting: boolean;
}

type FormAction =
  | { type: 'SET_FIELD'; field: keyof FormState; value: string }
  | { type: 'SET_ERROR'; field: string; error: string }
  | { type: 'CLEAR_ERRORS' }
  | { type: 'SUBMIT_START' }
  | { type: 'SUBMIT_END' };

function formReducer(state: FormState, action: FormAction): FormState {
  switch (action.type) {
    case 'SET_FIELD':
      return { ...state, [action.field]: action.value };
    case 'SET_ERROR':
      return { ...state, errors: { ...state.errors, [action.field]: action.error } };
    case 'CLEAR_ERRORS':
      return { ...state, errors: {} };
    case 'SUBMIT_START':
      return { ...state, isSubmitting: true };
    case 'SUBMIT_END':
      return { ...state, isSubmitting: false };
  }
}

// Usage:
const [state, dispatch] = useReducer(formReducer, {
  title: '',
  description: '',
  priority: 'medium',
  errors: {},
  isSubmitting: false,
});

dispatch({ type: 'SET_FIELD', field: 'title', value: 'New Task' });  // ✅
dispatch({ type: 'SET_FIELD', field: 'invalid' });  // ❌ Missing value, 'invalid' not in keyof
```

---

## 22. React Navigation — Full Type Safety

React Navigation's type system prevents you from navigating to non-existent screens or passing wrong params.

```typescript
// ═══════════════════════════════════════════
// 1. DEFINE YOUR PARAM LISTS
// ═══════════════════════════════════════════
import type { NativeStackScreenProps } from '@react-navigation/native-stack';
import type { BottomTabScreenProps } from '@react-navigation/bottom-tabs';
import type { CompositeScreenProps, NavigatorScreenParams } from '@react-navigation/native';

// Stack params — every screen and what params it accepts
export type RootStackParamList = {
  Splash: undefined;                           // No params
  Welcome: undefined;
  Login: undefined;
  MfaOption: { userData: User; mfaType: 'sms' | 'email' };
  Otp: { userId: number; method: 'sms' | 'email' };
  SignUp: undefined;
  ForgotPassword: undefined;
  Main: NavigatorScreenParams<MainTabParamList>;  // Nested navigator
  FeedDetail: { feedId: number };
  DiscoverDetail: { challengeId: number };
  VideoDetail: { lessonId: number; videoUrl: string };
  Quiz: { challengeId: number; lessonId: number };
  TaskForm: { task?: Task };                    // Optional = create mode
  UserDetail: { userId: number };
};

// Tab params
export type MainTabParamList = {
  Feed: undefined;
  Discover: undefined;
  Activity: undefined;
  Profile: undefined;
};


// ═══════════════════════════════════════════
// 2. DEFINE SCREEN PROPS TYPES
// ═══════════════════════════════════════════

// For Stack screens:
export type SplashScreenProps = NativeStackScreenProps<RootStackParamList, 'Splash'>;
export type LoginScreenProps = NativeStackScreenProps<RootStackParamList, 'Login'>;
export type MfaScreenProps = NativeStackScreenProps<RootStackParamList, 'MfaOption'>;
export type FeedDetailProps = NativeStackScreenProps<RootStackParamList, 'FeedDetail'>;

// For Tab screens (with access to parent Stack):
export type FeedScreenProps = CompositeScreenProps<
  BottomTabScreenProps<MainTabParamList, 'Feed'>,
  NativeStackScreenProps<RootStackParamList>
>;


// ═══════════════════════════════════════════
// 3. USE IN SCREEN COMPONENTS
// ═══════════════════════════════════════════

function LoginScreen({ navigation }: LoginScreenProps) {
  const handleLogin = async (email: string, password: string) => {
    const result = await api.post('/login', { email, password });
    
    if (result.data.needsMfa) {
      navigation.navigate('MfaOption', {
        userData: result.data.user,
        mfaType: 'email',
      });
      // ✅ TypeScript verifies:
      //    - 'MfaOption' is a valid screen name
      //    - userData and mfaType match the expected param types
    } else {
      navigation.reset({
        index: 0,
        routes: [{ name: 'Main' }],
      });
    }
  };
}

function FeedDetailScreen({ route, navigation }: FeedDetailProps) {
  const { feedId } = route.params;
  // ✅ feedId is number — TypeScript knows from the param list

  // These would be type errors:
  // navigation.navigate('NonExistentScreen');        ❌
  // navigation.navigate('Quiz');                      ❌ Missing required params
  // navigation.navigate('Quiz', { wrong: 'params' }); ❌ Wrong param shape
}


// ═══════════════════════════════════════════
// 4. TYPED useNavigation HOOK
// ═══════════════════════════════════════════

// Create a typed hook for use in non-screen components:
import { useNavigation } from '@react-navigation/native';
import type { NativeStackNavigationProp } from '@react-navigation/native-stack';

// Option A: Create a custom hook
export function useAppNavigation() {
  return useNavigation<NativeStackNavigationProp<RootStackParamList>>();
}

// Option B: Declare the type globally (recommended by React Navigation docs)
declare global {
  namespace ReactNavigation {
    interface RootParamList extends RootStackParamList {}
  }
}
// Now useNavigation() is automatically typed everywhere.


// ═══════════════════════════════════════════
// 5. USAGE IN ANY COMPONENT (not just screens)
// ═══════════════════════════════════════════

function FeedCard({ post }: { post: FeedPost }) {
  const navigation = useAppNavigation();

  return (
    <TouchableOpacity
      onPress={() => navigation.navigate('FeedDetail', { feedId: post.id })}
    >
      <Text>{post.title}</Text>
    </TouchableOpacity>
  );
}
```

---

## 23. Redux Toolkit — Typed State Management

```typescript
// ═══════════════════════════════════════════
// 1. STORE SETUP
// ═══════════════════════════════════════════
import { configureStore } from '@reduxjs/toolkit';
import feedReducer from './slices/feedSlice';
import authReducer from './slices/authSlice';
import uiReducer from './slices/uiSlice';

export const store = configureStore({
  reducer: {
    feed: feedReducer,
    auth: authReducer,
    ui: uiReducer,
  },
});

// THESE TWO TYPES ARE THE FOUNDATION OF EVERYTHING:
export type RootState = ReturnType<typeof store.getState>;
// RootState = { feed: FeedState; auth: AuthState; ui: UiState }

export type AppDispatch = typeof store.dispatch;
// AppDispatch knows about thunk middleware — can dispatch async thunks


// ═══════════════════════════════════════════
// 2. TYPED HOOKS (create once, use everywhere)
// ═══════════════════════════════════════════
import { useDispatch, useSelector, TypedUseSelectorHook } from 'react-redux';

export const useAppDispatch = () => useDispatch<AppDispatch>();
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

// WHY: useSelector and useDispatch are generic. Without typing, they return `any`.
// useAppSelector knows the shape of the entire store.
// useAppDispatch knows it can dispatch thunks.


// ═══════════════════════════════════════════
// 3. TYPED SLICE
// ═══════════════════════════════════════════
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';

// State shape:
interface FeedState {
  items: FeedPost[];
  loading: boolean;
  error: string | null;
  page: number;
  hasMore: boolean;
}

const initialState: FeedState = {
  items: [],
  loading: false,
  error: null,
  page: 1,
  hasMore: true,
};

// Async thunk — typed arguments and return value:
export const fetchFeed = createAsyncThunk<
  ApiResponse<FeedPost[]>,     // Return type (what fulfilled receives)
  { page: number },             // Argument type (what you pass to dispatch)
  { state: RootState; rejectValue: string }  // ThunkAPI config
>(
  'feed/fetchFeed',
  async ({ page }, { getState, rejectWithValue }) => {
    try {
      const token = getState().auth.token;  // ✅ Typed — getState() returns RootState
      const response = await api.get<ApiResponse<FeedPost[]>>('/feed/list', {
        params: { page },
        headers: { Authorization: `Bearer ${token}` },
      });
      return response.data;
    } catch (err) {
      return rejectWithValue('Failed to load feed');
    }
  }
);

// Slice:
const feedSlice = createSlice({
  name: 'feed',
  initialState,
  reducers: {
    // PayloadAction<T> types the action.payload
    clearFeed: (state) => {
      state.items = [];
      state.page = 1;
      state.hasMore = true;
    },
    setPage: (state, action: PayloadAction<number>) => {
      state.page = action.payload;  // ✅ payload is number
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchFeed.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchFeed.fulfilled, (state, action) => {
        // action.payload is ApiResponse<FeedPost[]> — fully typed!
        state.loading = false;
        if (action.meta.arg.page === 1) {
          state.items = action.payload.data;
        } else {
          state.items.push(...action.payload.data);
        }
        state.hasMore = action.payload.data.length > 0;
      })
      .addCase(fetchFeed.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload ?? 'Unknown error';
        // action.payload is string (from rejectValue type)
      });
  },
});

export const { clearFeed, setPage } = feedSlice.actions;
export default feedSlice.reducer;


// ═══════════════════════════════════════════
// 4. USING IN COMPONENTS
// ═══════════════════════════════════════════
function FeedScreen() {
  const dispatch = useAppDispatch();
  const { items, loading, error, page, hasMore } = useAppSelector(state => state.feed);
  // ✅ Every field is typed: items is FeedPost[], loading is boolean, etc.

  const token = useAppSelector(state => state.auth.token);
  // ✅ token is string | null

  useEffect(() => {
    dispatch(fetchFeed({ page: 1 }));
    // ✅ TypeScript verifies: { page: number } matches the thunk's argument type
  }, [dispatch]);

  const handleLoadMore = () => {
    if (!loading && hasMore) {
      dispatch(fetchFeed({ page: page + 1 }));
    }
  };
}
```

---

## 24. Axios — Typed API Layer

```typescript
import axios, { AxiosInstance, AxiosResponse, InternalAxiosRequestConfig } from 'axios';

// ═══════════════════════════════════════════
// 1. TYPE YOUR API RESPONSES
// ═══════════════════════════════════════════

interface ApiResponse<T> {
  success: boolean;
  data: T;
  message?: string;
}

interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    limit: number;
    total: number;
    totalPages: number;
  };
}

interface User {
  id: number;
  name: string;
  email: string;
  avatar: string | null;
}

interface LoginPayload {
  email: string;
  password: string;
}

interface LoginResult {
  user: User;
  access_token: string;
  last_otp_verified: string;
}


// ═══════════════════════════════════════════
// 2. CREATE A TYPED API CLIENT
// ═══════════════════════════════════════════

const api: AxiosInstance = axios.create({
  baseURL: 'https://dashboard.steamthestreets.org/api/v1/',
  timeout: 10000,
});

// Request interceptor — typed config:
api.interceptors.request.use(
  async (config: InternalAxiosRequestConfig) => {
    const token = await AsyncStorage.getItem('access_token');
    if (token && config.headers) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }
);


// ═══════════════════════════════════════════
// 3. TYPED API CALLS
// ═══════════════════════════════════════════

// axios.get<T> sets response.data to type T:
async function login(email: string, password: string): Promise<LoginResult> {
  const response = await api.post<ApiResponse<LoginResult>>('login', {
    email,
    password,
  });
  // response.data is ApiResponse<LoginResult>
  // response.data.data is LoginResult
  return response.data.data;
}

async function fetchFeed(page: number): Promise<PaginatedResponse<FeedPost>> {
  const response = await api.get<PaginatedResponse<FeedPost>>('feed/list', {
    params: { page, per_page: 20 },
  });
  return response.data;
}

// FormData upload — typed:
async function updateAvatar(uri: string): Promise<User> {
  const formData = new FormData();
  formData.append('avatar', {
    uri,
    type: 'image/jpeg',
    name: 'avatar.jpg',
  } as any);  // FormData append for RN needs `as any` — RN's FormData is not web's FormData

  const response = await api.post<ApiResponse<User>>('updateAvatarMultiple', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data.data;
}


// ═══════════════════════════════════════════
// 4. TYPED ERROR HANDLING
// ═══════════════════════════════════════════
import { AxiosError } from 'axios';

interface ApiErrorResponse {
  success: false;
  message: string;
  errors?: Record<string, string[]>;  // Validation errors
}

async function safeApiCall<T>(fn: () => Promise<T>): Promise<T> {
  try {
    return await fn();
  } catch (error) {
    if (axios.isAxiosError(error)) {
      // error is now AxiosError — fully typed
      const axiosError = error as AxiosError<ApiErrorResponse>;
      const message = axiosError.response?.data?.message ?? 'Network error';
      const status = axiosError.response?.status;

      if (status === 401) {
        // Handle token expiry
      }

      throw new Error(message);
    }
    throw error;
  }
}
```

---

## 25. AsyncStorage — Typed Persistence

```typescript
import AsyncStorage from '@react-native-async-storage/async-storage';

// ═══════════════════════════════════════════
// TYPE-SAFE STORAGE WRAPPER
// ═══════════════════════════════════════════

// Define all storage keys and their value types:
interface StorageSchema {
  access_token: string;
  user_data: User;
  isLogin: boolean;
  fcm_token: string;
  language: 'en' | 'es' | 'fr';
  isFirstTimeLogin: boolean;
  theme: 'light' | 'dark';
}

// Typed getter — knows the return type based on the key:
async function getStorageItem<K extends keyof StorageSchema>(
  key: K
): Promise<StorageSchema[K] | null> {
  const raw = await AsyncStorage.getItem(key);
  if (raw === null) return null;
  return JSON.parse(raw) as StorageSchema[K];
}

// Typed setter:
async function setStorageItem<K extends keyof StorageSchema>(
  key: K,
  value: StorageSchema[K]
): Promise<void> {
  await AsyncStorage.setItem(key, JSON.stringify(value));
}

// Typed remover:
async function removeStorageItem<K extends keyof StorageSchema>(
  key: K
): Promise<void> {
  await AsyncStorage.removeItem(key);
}

// ═══════════════════════════════════════════
// USAGE
// ═══════════════════════════════════════════

const token = await getStorageItem('access_token');
// ✅ token is string | null

const user = await getStorageItem('user_data');
// ✅ user is User | null

await setStorageItem('language', 'en');     // ✅
await setStorageItem('language', 'german'); // ❌ '"german"' not in 'en' | 'es' | 'fr'

await setStorageItem('access_token', 123);  // ❌ number not assignable to string
```

---

## 26. Common Patterns in the STS Rebuild

### Pattern 1: Discriminated Union for Screen State

```typescript
// Every screen that loads data should use this pattern:
type ScreenState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: T }
  | { status: 'error'; message: string };

function FeedScreen() {
  const [state, setState] = useState<ScreenState<FeedPost[]>>({ status: 'idle' });

  // In JSX:
  switch (state.status) {
    case 'idle':
    case 'loading':
      return <LoadingSpinner />;
    case 'error':
      return <ErrorBanner message={state.message} />;
    case 'success':
      return <FeedList posts={state.data} />;
      // ✅ state.data is FeedPost[] — guaranteed by the discriminant
  }
}
```

### Pattern 2: Typed Form Handler

```typescript
// Generic form hook that works with any form shape:
function useForm<T extends Record<string, unknown>>(initialValues: T) {
  const [values, setValues] = useState<T>(initialValues);
  const [errors, setErrors] = useState<Partial<Record<keyof T, string>>>({});
  const [touched, setTouched] = useState<Partial<Record<keyof T, boolean>>>({});

  const setValue = <K extends keyof T>(field: K, value: T[K]) => {
    setValues(prev => ({ ...prev, [field]: value }));
  };

  const setError = (field: keyof T, error: string) => {
    setErrors(prev => ({ ...prev, [field]: error }));
  };

  const touchField = (field: keyof T) => {
    setTouched(prev => ({ ...prev, [field]: true }));
  };

  return { values, errors, touched, setValue, setError, touchField };
}

// Usage:
const form = useForm({
  email: '',
  password: '',
  rememberMe: false,
});

form.setValue('email', 'test@test.com');    // ✅
form.setValue('email', 123);                // ❌ number not assignable to string
form.setValue('nonExistent', 'value');       // ❌ 'nonExistent' not a valid field
```

### Pattern 3: Exhaustive Status Handlers

```typescript
type TaskStatus = 'pending' | 'in_progress' | 'done';

// This function MUST handle every status — adding a new one forces an update:
function getStatusColor(status: TaskStatus): string {
  switch (status) {
    case 'pending': return '#F59E0B';
    case 'in_progress': return '#3B82F6';
    case 'done': return '#22C55E';
    default:
      // If you add 'cancelled' to TaskStatus but forget to handle it here,
      // TypeScript errors: "Type 'cancelled' is not assignable to type 'never'"
      const _exhaustive: never = status;
      return _exhaustive;
  }
}
```

### Pattern 4: Typed Navigation Params Across the App

```typescript
// In STS, screens often receive data from multiple sources.
// Type-safe extraction:

function QuizScreen({ route }: QuizScreenProps) {
  const { challengeId, lessonId } = route.params;
  // Both are number — guaranteed by the param list definition

  const [currentPage, setCurrentPage] = useState(1);

  // Update header with page counter (STS pattern):
  useEffect(() => {
    navigation.setOptions({
      headerRight: () => (
        <Text>{`${currentPage}/${totalPages}`}</Text>
      ),
    });
  }, [currentPage, totalPages, navigation]);
}
```

### Pattern 5: Type-Safe API Endpoint Map

```typescript
// Define ALL endpoints and their request/response types in one place:
interface ApiEndpoints {
  'login': { request: { email: string; password: string }; response: LoginResult };
  'signup': { request: SignupPayload; response: User };
  'me': { request: void; response: User };
  'feed/list': { request: { page: number }; response: FeedPost[] };
  'feed/detail': { request: { id: number }; response: FeedPost };
  'feed/likeunlike': { request: { feed_id: number }; response: { liked: boolean } };
  'challenge/list': { request: void; response: Challenge[] };
}

// Type-safe API call function:
async function apiCall<E extends keyof ApiEndpoints>(
  endpoint: E,
  data?: ApiEndpoints[E]['request'],
): Promise<ApiResponse<ApiEndpoints[E]['response']>> {
  const response = await api.post(endpoint, data);
  return response.data;
}

// Usage:
const feed = await apiCall('feed/list', { page: 1 });
// ✅ feed.data is FeedPost[]

const login = await apiCall('login', { email: 'a@b.com', password: '123' });
// ✅ login.data is LoginResult

await apiCall('login', { wrong: 'shape' });
// ❌ Type error — payload doesn't match

await apiCall('nonexistent');
// ❌ Type error — not a valid endpoint
```

---

## Quick Reference — The TypeScript Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│                    TYPESCRIPT MENTAL MODEL                            │
│                                                                      │
│  TYPES = compile-time only. Erased at runtime. Zero cost.            │
│                                                                      │
│  PRIMITIVES:  string, number, boolean, null, undefined               │
│  SPECIAL:     any (unsafe), unknown (safe), void, never              │
│                                                                      │
│  OBJECTS:     interface User { name: string }                        │
│               type User = { name: string }                           │
│                                                                      │
│  UNION:       string | number     ("this OR that")                   │
│  INTERSECT:   A & B               ("this AND that")                  │
│  LITERAL:     'pending' | 'done'  (exact values as types)            │
│                                                                      │
│  GENERIC:     function wrap<T>(v: T): { value: T }                   │
│  CONSTRAINT:  <T extends HasLength>                                  │
│  CONDITIONAL: T extends string ? X : Y                               │
│  MAPPED:      { [K in keyof T]: boolean }                            │
│                                                                      │
│  NARROWING:   typeof, instanceof, in, discriminated unions           │
│  ASSERTIONS:  value as Type  (trust me)                              │
│  PREDICATES:  function isX(v): v is X  (custom narrowing)            │
│                                                                      │
│  UTILITIES:   Partial, Required, Pick, Omit, Record,                 │
│               Extract, Exclude, ReturnType, Parameters               │
│                                                                      │
│  RN-SPECIFIC: StyleProp<ViewStyle>, React.ReactNode,                 │
│               NativeStackScreenProps, PayloadAction<T>               │
│                                                                      │
│  STRICT MODE: Always. Non-negotiable. "strict": true.                │
│                                                                      │
│  ESCAPE ORDER: Fix type > predicate > assertion > @ts-expect > any   │
└─────────────────────────────────────────────────────────────────────┘
```

---

> **You now know TypeScript**. Not just the syntax — the mental model. The compiler reads your code in 5 phases, the type checker is the heart, types are erased at runtime, generics are type-level functions, narrowing is the compiler thinking with you, and `strict: true` is the price of admission. Every React Native pattern — props, hooks, navigation, Redux, Axios — follows the same principle: define the shape of your data, and let the compiler verify everything else. Go build.
