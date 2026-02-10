# Expo -- The Master Document

> **Purpose**: Everything you need to know about Expo, how it relates to React Native, its build system, OTA updates, pricing, and when/how to use it for the STS rebuild. Written for a developer who already knows React Native and is evaluating Expo as infrastructure.

---

## Table of Contents

1. [What Expo Actually Is (And What It Is Not)](#1-what-expo-actually-is-and-what-it-is-not)
2. [The Three Flavors of Expo](#2-the-three-flavors-of-expo)
3. [Expo's Relationship to React Native](#3-expos-relationship-to-react-native)
4. [EAS -- Expo Application Services](#4-eas----expo-application-services)
5. [EAS Build -- Cloud-Native Compilation](#5-eas-build----cloud-native-compilation)
6. [EAS Update -- Over-The-Air JS Deployments](#6-eas-update----over-the-air-js-deployments)
7. [EAS Submit -- Store Deployment](#7-eas-submit----store-deployment)
8. [Expo Dev Client -- Custom Development Builds](#8-expo-dev-client----custom-development-builds)
9. [Expo Modules API -- Writing Native Code in Expo](#9-expo-modules-api----writing-native-code-in-expo)
10. [Expo Router vs. React Navigation](#10-expo-router-vs-react-navigation)
11. [Pricing -- The Full Breakdown](#11-pricing----the-full-breakdown)
12. [Expo for the STS Rebuild -- The Decision Matrix](#12-expo-for-the-sts-rebuild----the-decision-matrix)

---

## 1. What Expo Actually Is (And What It Is Not)

### What It Is

Expo is a **platform** built on top of React Native. It provides:
- A set of **well-tested, cross-platform native modules** (camera, notifications, file system, etc.)
- A **cloud build service** (EAS Build) that compiles your app on Apple/Google infrastructure
- An **OTA update system** (EAS Update) that pushes JS changes without store review
- A **development client** (Expo Dev Client) for rapid iteration
- An **app store submission tool** (EAS Submit)

### What It Is NOT

- It is **not a separate framework**. Expo apps are React Native apps.
- It is **not a WebView wrapper**. Same native rendering as bare RN.
- It is **not just Expo Go** (the sandboxed testing app). That's one small piece.
- It is **not a lock-in**. You can eject/prebuild at any time and get a standard `android/` and `ios/` project.

### The Mental Model

```
React Native = Engine
Expo = Chassis + Tooling + Service Station

You can drive the engine bare (RN CLI),
or you can put it in the Expo chassis for convenience.
Either way, the engine is the same.
```

---

## 2. The Three Flavors of Expo

### Flavor 1: Expo Go (Sandbox -- NOT for Production)

- A pre-built app you install from the App Store / Play Store.
- Scans a QR code from your Metro dev server.
- Runs your JS code inside Expo Go's pre-bundled native modules.
- **Limitations**: Can only use libraries that Expo Go already includes. No custom native modules.
- **Use case**: Prototyping, demos, learning. **Not** for the STS rebuild.

### Flavor 2: Expo Managed Workflow (expo prebuild)

- You write only JS/TS. No `android/` or `ios/` directories in your repo.
- Native code is **generated** by `expo prebuild` based on your `app.json`/`app.config.js` and installed Expo modules.
- When you need custom native behavior, you use **config plugins** to modify the generated native code.
- **Use case**: Most production apps that don't need deeply custom native code.

How it works:

```
app.config.js  ──→  expo prebuild  ──→  android/ + ios/  ──→  Build
     │                                        │
     └── Config plugins modify                └── Generated, not manually maintained
         the native projects                      (can be gitignored)
```

### Flavor 3: Expo Bare Workflow (Expo in a CLI Project)

- You **have** `android/` and `ios/` directories that you maintain.
- You **add** Expo packages as regular dependencies (`npx install-expo-modules`).
- You **use** EAS Build, EAS Update, and Expo native modules.
- You keep full native control.
- **Use case**: Existing bare RN projects that want Expo's tooling. **This is the likely path for the STS rebuild.**

```bash
# Add Expo to an existing bare RN project
npx install-expo-modules@latest

# Now you can use:
# - expo-notifications (instead of react-native-push-notification)
# - expo-camera
# - expo-file-system
# - eas build / eas update
# - etc.
```

---

## 3. Expo's Relationship to React Native

### Versioning

Expo releases are tied to specific React Native versions via **SDK versions**:

| Expo SDK | React Native | React | Key Feature |
|----------|-------------|-------|-------------|
| SDK 50 | 0.73 | 18.2 | |
| SDK 51 | 0.74 | 18.2 | New Architecture support |
| SDK 52 | 0.76 | 18.3 | New Arch by default |
| SDK 53 | 0.77 | 19.0 | Full bridgeless support |
| SDK 54 | 0.78 | 19.0 | |
| SDK 55 | 0.83 | 19.1 | New Arch mandatory |

When you install `expo@^52.0.0`, you are implicitly pinning to React Native 0.76.x.

### What Expo Adds On Top of RN

1. **expo-* modules**: Drop-in replacements for many community packages, maintained by the Expo team with guaranteed New Architecture support.
2. **Config plugins**: Declarative native configuration (permissions, deep links, splash screens) without touching native code.
3. **Metro config integration**: Expo extends Metro's config for better module resolution.
4. **Autolinking**: Enhanced auto-linking that handles Expo modules and their native dependencies.

### Can You Mix Expo and Non-Expo Libraries?

Yes. In the bare workflow, you can use:
- Expo modules (`expo-notifications`, `expo-camera`)
- Community RN modules (`react-native-video`, `@react-native-firebase/*`)
- Custom native modules you write yourself

They all coexist.

---

## 4. EAS -- Expo Application Services

EAS is Expo's cloud platform. It's the main reason to use Expo even in a bare project. Three services:

```
EAS
├── EAS Build    → Compile native binaries in the cloud
├── EAS Update   → Push JS-only changes over-the-air
└── EAS Submit   → Upload builds to App Store / Play Store
```

All three are accessed via the `eas-cli`:

```bash
npm install -g eas-cli
eas login
eas build:configure  # Creates eas.json
```

---

## 5. EAS Build -- Cloud-Native Compilation

### What It Does

EAS Build compiles your React Native project into native binaries (`.apk`/`.aab` for Android, `.ipa` for iOS) on Expo's cloud infrastructure. This is your answer to "I don't have a Mac."

### How It Works

```
Your Code (Linux)
    │
    ├── git push / eas build
    │
    ▼
EAS Cloud (macOS for iOS, Linux for Android)
    │
    ├── Installs dependencies (npm/yarn)
    ├── Runs expo prebuild (if managed)
    ├── Runs Gradle (Android) or xcodebuild (iOS)
    ├── Signs the binary
    │
    ▼
Download .apk/.aab or .ipa
```

### Configuration (eas.json)

```json
{
  "cli": {
    "version": ">= 12.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal",
      "ios": {
        "simulator": false
      }
    },
    "preview": {
      "distribution": "internal",
      "ios": {
        "simulator": false
      }
    },
    "production": {
      "ios": {
        "resourceClass": "m-medium"
      },
      "android": {
        "resourceClass": "medium"
      }
    }
  },
  "submit": {
    "production": {
      "ios": {
        "appleId": "your@email.com",
        "ascAppId": "123456789",
        "appleTeamId": "ABCDE12345"
      }
    }
  }
}
```

### Build Profiles

| Profile | Purpose | Distribution |
|---------|---------|-------------|
| `development` | Dev builds with dev client | Internal (TestFlight / direct install) |
| `preview` | QA / staging builds | Internal |
| `production` | Store-ready builds | Store |

### Code Signing (iOS)

EAS can manage your iOS certificates and provisioning profiles automatically:

```bash
eas credentials  # Interactive credential management
```

Or you can provide your own if you already have them.

---

## 6. EAS Update -- Over-The-Air JS Deployments

### The Concept

When your app changes involve **only JavaScript** (no native module additions, no permission changes, no SDK version bumps), you can push the new JS bundle directly to users' devices **without going through the App Store or Play Store**.

```
JS Change → eas update → Expo CDN → User's App Downloads Update → New Code Running
```

### How It Works

1. You run `eas update --branch production --message "Fix login bug"`.
2. Expo bundles your JS, uploads it to their CDN.
3. Next time the app starts (or checks in the background), it downloads the new bundle.
4. On the next restart, the new code is active.

### When You CAN Use OTA

- Bug fixes in JS code
- UI changes (new screens, layout tweaks)
- Logic changes (API call modifications, state management updates)
- Text/copy changes

### When You CANNOT Use OTA

- Adding a new native module (e.g., adding `react-native-video` when it wasn't there before)
- Changing native permissions
- Upgrading the React Native version
- Any change that modifies the native binary

### Runtime Versioning

EAS Update uses **runtime versions** to ensure updates are only sent to compatible native builds:

```json
// app.json
{
  "expo": {
    "runtimeVersion": {
      "policy": "fingerprint"  // Auto-detected from native code
    }
  }
}
```

The `fingerprint` policy automatically hashes your native dependencies. If the native code changes, the runtime version changes, and old updates won't be sent to new builds (and vice versa).

### Channels and Branches

```
Channel: "production"  → Branch: "production"  → Latest update for production users
Channel: "staging"     → Branch: "staging"      → Latest update for QA
Channel: "development" → Branch: "development"  → Latest update for dev builds
```

---

## 7. EAS Submit -- Store Deployment

```bash
# Submit to Apple App Store
eas submit --platform ios --latest

# Submit to Google Play Store
eas submit --platform android --latest
```

- For iOS: Uploads the `.ipa` to App Store Connect (like using Transporter).
- For Android: Uploads the `.aab` to Google Play Console.
- Can be automated in CI/CD.

---

## 8. Expo Dev Client -- Custom Development Builds

### The Problem with Expo Go

Expo Go is limited to Expo's pre-bundled native modules. If you need `@react-native-firebase/*` or `react-native-video`, Expo Go can't load them.

### The Solution: Development Builds

A **development build** is a custom version of Expo Go that includes YOUR native modules. It's like compiling your own Expo Go.

```bash
# Build a dev client for iOS (cloud)
eas build --profile development --platform ios

# Build a dev client for Android (local or cloud)
eas build --profile development --platform android
# OR locally:
npx expo run:android
```

Once installed on your phone:
1. Start Metro on your Linux machine: `npx expo start`
2. The dev client connects to your Metro server (same WiFi or tunnel).
3. You get hot reload, fast refresh, dev menu -- everything.
4. When you change JS code, it reloads instantly (no rebuild needed).
5. When you add a native module, rebuild the dev client (takes minutes in the cloud).

### This Is Your Primary Development Loop

```
Daily work:
  Linux → Write code → Metro → Dev Client on iPhone → Hot Reload

When native code changes (rare):
  eas build --profile development --platform ios → New dev client → Continue
```

---

## 9. Expo Modules API -- Writing Native Code in Expo

If you need to write a custom native module within Expo, you use the **Expo Modules API**:

```bash
npx create-expo-module my-module
```

This generates a module with:
- Swift code for iOS
- Kotlin code for Android
- TypeScript definitions
- Auto-linking configuration

```kotlin
// android/src/main/java/expo/modules/mymodule/MyModule.kt
class MyModule : Module() {
  override fun definition() = ModuleDefinition {
    Name("MyModule")

    Function("hello") {
      "Hello from native!"
    }
  }
}
```

```typescript
// src/MyModule.ts
import { requireNativeModule } from 'expo-modules-core';
const MyModule = requireNativeModule('MyModule');
export const hello = () => MyModule.hello();
```

This API is fully compatible with the New Architecture (Turbo Modules under the hood).

---

## 10. Expo Router vs. React Navigation

### React Navigation (What STS Uses)

The STS app uses `@react-navigation/native` v6 with Stack and Bottom Tab navigators. This is the classic, imperative approach:

```javascript
<Stack.Navigator>
  <Stack.Screen name="Login" component={LoginScreen} />
  <Stack.Screen name="Home" component={HomeScreen} />
</Stack.Navigator>

// Navigate imperatively
navigation.navigate('Home');
```

### Expo Router (The New Alternative)

Expo Router is a **file-based routing** system (like Next.js for mobile):

```
app/
├── _layout.tsx        → Root layout (navigation container)
├── index.tsx          → Home screen (/)
├── login.tsx          → Login screen (/login)
├── (tabs)/
│   ├── _layout.tsx    → Tab layout
│   ├── feed.tsx       → Feed tab (/feed)
│   ├── discover.tsx   → Discover tab (/discover)
│   └── profile.tsx    → Profile tab (/profile)
└── feed/
    └── [id].tsx       → Feed detail (/feed/123)
```

```typescript
// Navigate with links (like web)
import { Link } from 'expo-router';

<Link href="/feed/123">View Feed</Link>

// Or programmatically
import { router } from 'expo-router';
router.push('/feed/123');
```

### Which to Use for the STS Rebuild?

| Factor | React Navigation | Expo Router |
|--------|-----------------|-------------|
| Familiarity | STS already uses it | New paradigm |
| Deep linking | Manual config | Automatic from file structure |
| Type safety | Manual | Automatic route types |
| Web support | Extra work | Built-in |
| Complexity | You manage the nav tree | File system IS the nav tree |
| Maturity | Battle-tested | Stable since Expo SDK 50 |

**Recommendation**: If you're doing a full rebuild anyway, Expo Router simplifies deep linking (which STS uses for notifications and sharing) and gives you automatic TypeScript route types. Worth considering.

---

## 11. Pricing -- The Full Breakdown

### Plans Overview

| | **Free** | **Starter** | **Production** | **Enterprise** |
|---|---|---|---|---|
| **Monthly Cost** | $0 | $19 | $199 | $1,999 |
| **EAS Build Credits** | -- | $45 | $225 | $1,000 |
| **iOS Builds (Free Tier)** | 15/mo | Included in credits | Included in credits | Included in credits |
| **Android Builds (Free Tier)** | 15/mo | Included in credits | Included in credits | Included in credits |
| **Build Queue Priority** | Low | High | High + 2 concurrencies | High + 5 concurrencies |
| **EAS Update MAUs** | 1,000 | 3,000 | 50,000 | 1,000,000 |
| **Large Workers** | No | Yes | Yes | Yes |
| **SSO** | No | No | Yes | Yes |
| **SLA** | No | No | No | Yes |

### Per-Build Costs (When Credits Are Exhausted)

| Platform | Resource Class | Cost Per Build |
|----------|---------------|----------------|
| Android | Medium | $1 |
| Android | Large | $2 |
| iOS | Medium | $2 |
| iOS | Large | $4 |

### EAS Update Overage Pricing

| Metric | Cost |
|--------|------|
| Extra updated users (MAU) | $0.005 per user |
| Extra global edge bandwidth | $0.10 per GiB |

### Concrete Example: STS Rebuild Development Phase

During active development (assume 2-3 months):

**Free Tier feasibility:**
- 15 iOS builds/month + 15 Android builds/month
- If you use EAS Update for JS-only iterations, you might only need 3-5 native builds per platform per week during heavy development.
- **Verdict**: Free tier might be tight. Expect to hit limits during intensive weeks.

**Starter Tier ($19/mo) feasibility:**
- $45 credit = ~11 large iOS builds or ~22 medium Android builds per month
- High-priority queue (faster builds)
- 3,000 MAU for EAS Update (more than enough for dev/QA)
- **Verdict**: Comfortable for the development phase.

**Post-launch (Production tier $199/mo):**
- $225 credit = ~56 large iOS builds
- 50,000 MAU for OTA updates
- If STS has fewer than 50K monthly active users, this covers everything.
- **Verdict**: Appropriate for a launched product with active users.

### Cost Comparison: EAS vs. Renting a Mac

| Approach | Monthly Cost | Notes |
|----------|-------------|-------|
| EAS Starter | $19 | 11+ iOS builds, managed signing |
| MacinCloud (basic) | ~$30-50 | Full macOS access, but you manage everything |
| AWS EC2 Mac | ~$470 (dedicated host, 24/7) | Overkill unless you need CI/CD at scale |
| Codemagic CI | $0-75 | 500 free min/mo, then pay per minute |

**EAS is the most cost-effective option for a small team without a Mac.**

### The Free Tier Is Enough to Start

You can validate the entire build pipeline, test on your iPhone, and develop the first features without spending a cent. Move to Starter when you're consistently building.

---

## 12. Expo for the STS Rebuild -- The Decision Matrix

### Should You Use Expo at All?

| Consideration | Analysis | Verdict |
|---------------|----------|---------|
| No Mac for iOS builds | EAS Build solves this completely | **Use Expo** |
| Firebase integration | `@react-native-firebase/*` works in bare Expo workflow | **Compatible** |
| Custom native modules | Bare workflow allows any native code | **Compatible** |
| Push notifications | `expo-notifications` or `@notifee/react-native` both work | **Compatible** |
| Video player | `react-native-video` works in Expo | **Compatible** |
| OTA updates | EAS Update gives you CodePush-like functionality | **Use Expo** |
| Deep linking | Expo Router automates this | **Use Expo** |
| Stripe payments | `@stripe/stripe-react-native` works in Expo | **Compatible** |
| App Store submission | EAS Submit from Linux | **Use Expo** |

### The Recommended Architecture

```
Expo (Bare Workflow)
├── EAS Build for iOS + Android cloud builds
├── EAS Update for OTA JS deployments
├── EAS Submit for store uploads
├── expo-notifications (replaces react-native-push-notification)
├── @react-native-firebase/* (kept, upgraded to v22)
├── react-native-video v6+ (kept, upgraded)
├── Expo Router OR React Navigation v7 (your call)
├── Development builds on your iPhone via TestFlight
└── Local Android development on Linux
```

### What You DON'T Need Expo For

- If you want to rent a Mac and do everything manually -- you don't need EAS Build.
- If you don't care about OTA updates -- you don't need EAS Update.
- If you have a CI/CD pipeline with macOS runners -- you don't need EAS.

But given your setup (Linux, no Mac, iPhone for testing), Expo's EAS services are the pragmatic choice.

---

> **Bottom line**: Expo is not a dumbed-down version of React Native. It's an infrastructure layer that solves real problems -- especially iOS builds from Linux, OTA updates, and managed code signing. The Starter plan at $19/month gives you everything needed for active development. The Free tier is enough to validate the approach before committing.
