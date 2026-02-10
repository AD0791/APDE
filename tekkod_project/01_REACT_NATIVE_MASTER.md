# React Native -- The Master Document

> **Purpose**: Everything you need to know about React Native and React Native CLI development to rebuild the STS Mobile App from an informed position. Written for a developer already fluent in mobile dev with React Native.

---

## Table of Contents

1. [What React Native Actually Is](#1-what-react-native-actually-is)
2. [The Runtime: How RN Executes Your Code](#2-the-runtime-how-rn-executes-your-code)
3. [The Old Architecture vs. The New Architecture](#3-the-old-architecture-vs-the-new-architecture)
4. [React Native CLI -- The Bare Workflow](#4-react-native-cli----the-bare-workflow)
5. [Environment Setup on Linux (No Mac)](#5-environment-setup-on-linux-no-mac)
6. [The iOS Problem -- And Every Solution Available to You](#6-the-ios-problem----and-every-solution-available-to-you)
7. [Project Anatomy Under RN CLI](#7-project-anatomy-under-rn-cli)
8. [Native Modules and Turbo Modules](#8-native-modules-and-turbo-modules)
9. [The Dependency Ecosystem -- What to Know for the Rebuild](#9-the-dependency-ecosystem----what-to-know-for-the-rebuild)
10. [Build, Sign, and Ship](#10-build-sign-and-ship)
11. [Debugging and Dev Tools in the New Architecture](#11-debugging-and-dev-tools-in-the-new-architecture)
12. [Key Decisions for the STS Rebuild](#12-key-decisions-for-the-sts-rebuild)

---

## 1. What React Native Actually Is

React Native is **not** a webview wrapper. It is a framework that lets you write UI in React (JSX) and renders it to **real native views** -- `UIView` on iOS, `android.view.View` on Android. Your JavaScript runs in a JavaScript engine (historically JavaScriptCore, now **Hermes** by default), and a bridge/interface connects your JS world to the native world.

Key mental model:

```
┌─────────────────────────────────────┐
│         Your React Components       │  ← JavaScript (Hermes Engine)
├─────────────────────────────────────┤
│     React Native Renderer (Fabric)  │  ← C++ layer
├─────────────────────────────────────┤
│   Native Views (UIKit / Android)    │  ← Platform-native
└─────────────────────────────────────┘
```

- **React** handles the component tree, state, reconciliation.
- **React Native** provides the `<View>`, `<Text>`, `<Image>`, `<ScrollView>` primitives that map to native counterparts.
- **Metro** is the bundler (like Webpack, but for RN). It bundles your JS into a single file that the native shell loads at runtime.

---

## 2. The Runtime: How RN Executes Your Code

### Hermes Engine

Since RN 0.70+, **Hermes** is the default JavaScript engine. It replaced JavaScriptCore (JSC).

Why Hermes matters:
- **Bytecode precompilation**: Your JS is compiled to bytecode at build time, not at runtime. This means faster startup (Time-to-Interactive drops significantly).
- **Optimized garbage collector**: Better memory usage on constrained mobile devices.
- **Smaller binary size** compared to JSC.
- **Full debugging support** via Chrome DevTools Protocol.

When you build your app, Metro bundles your JS, then Hermes compiles it to `.hbc` (Hermes bytecode). The native shell loads this bytecode directly.

### The JavaScript Thread vs. The Main (UI) Thread

React Native runs on multiple threads:

| Thread | Responsibility |
|--------|---------------|
| **JS Thread** | Runs your React code, business logic, state management |
| **Main/UI Thread** | Renders native views, handles touch events, animations |
| **Shadow Thread** (old arch) / **Background Thread** (new arch) | Layout calculation (Yoga engine) |

In the **old architecture**, communication between JS and Native was **asynchronous** and went through the **Bridge** -- a JSON serialization layer. This caused performance bottlenecks for frequent updates (animations, scrolling).

In the **new architecture**, communication is **synchronous when needed** via **JSI** (JavaScript Interface) -- a C++ layer that allows JS to directly call native functions without serialization.

---

## 3. The Old Architecture vs. The New Architecture

This is the single most important concept for the STS rebuild, since the contract explicitly calls for migrating from the Legacy Bridge to Bridgeless Mode.

### Old Architecture (what STS 0.65.1 uses)

```
JS Thread  ──── Bridge (async JSON) ────  Native Thread
                    │
              Serialization overhead
              Asynchronous only
              No direct memory sharing
```

- Every call from JS to Native (and back) serializes data to JSON, sends it across, and deserializes on the other side.
- Animations that need frequent JS-Native communication stutter.
- Native modules are registered globally at startup (even if unused), increasing startup time.

### New Architecture (0.74+ default, mandatory from 0.82)

```
JS Thread  ──── JSI (C++ direct calls) ────  Native Thread
                    │
              Synchronous when needed
              Shared memory via C++ objects
              Lazy module loading
```

Four pillars of the New Architecture:

| Pillar | Replaces | What It Does |
|--------|----------|-------------|
| **JSI** (JavaScript Interface) | Bridge | C++ API that lets JS hold references to native objects and call methods directly |
| **Fabric** | Old Renderer | New rendering system that can synchronously measure and render views |
| **Turbo Modules** | Native Modules | Lazy-loaded, type-safe native modules with codegen |
| **Codegen** | Manual typing | Generates native interfaces from TypeScript/Flow specs |

### Bridgeless Mode

Starting with 0.74, **Bridgeless Mode** is the default. This means the old Bridge is completely removed. All communication goes through JSI. If a library still depends on the Bridge, it will not work in Bridgeless Mode.

**Timeline of the transition:**

| Version | Status |
|---------|--------|
| 0.65.1 (STS current) | Old Architecture only |
| 0.74.x (contract target) | New Architecture default, Bridgeless Mode default |
| 0.76 (Oct 2024) | New Architecture declared production-ready |
| 0.78 (Feb 2025) | React 19 support |
| 0.82+ (2025) | New Architecture mandatory, old architecture frozen |

### Yoga 3.0 (Layout Engine)

The New Architecture ships with **Yoga 3.0**, a complete rewrite of the Flexbox layout engine. This matters because:
- It fixes long-standing layout bugs, especially with `row-reverse` containers and `flex` calculations.
- Layouts that "worked" in the old Yoga because of bugs may **break** in Yoga 3.0.
- You must audit every screen during the rebuild for visual regressions.

---

## 4. React Native CLI -- The Bare Workflow

When people say "React Native CLI," they mean the `react-native` CLI tool (`npx react-native init`) that scaffolds a **bare** project -- full access to `android/` and `ios/` native directories.

### What You Get

```
my-app/
├── android/          ← Full Android project (Gradle, Java/Kotlin, AndroidManifest)
├── ios/              ← Full iOS project (Xcode, Objective-C/Swift, Podfile)
├── src/              ← Your JS/TS source code
├── index.js          ← Entry point
├── metro.config.js   ← Metro bundler config
├── babel.config.js   ← Babel config
├── package.json
└── app.json
```

### What This Means

- **Full native control**: You can write custom native modules in Java/Kotlin (Android) and Objective-C/Swift (iOS).
- **Direct Gradle/Xcode access**: You configure build settings, signing, permissions, native SDKs directly.
- **No abstraction layer**: If a library needs native linking, you handle it yourself (though auto-linking covers most cases since RN 0.60+).
- **You own the native projects**: Upgrades between RN versions require manually applying diffs to your `android/` and `ios/` directories (use [React Native Upgrade Helper](https://react-native-community.github.io/upgrade-helper/)).

### Pros of CLI over Expo

- Zero restrictions on which native libraries you can use.
- Smaller bundle sizes (no Expo runtime overhead).
- Direct control over build configuration.
- Can integrate any SDK (payment processors, custom analytics, hardware APIs).
- No dependency on a third-party build service.

### Cons of CLI

- **Brutal initial setup**: Android Studio, JDK, Gradle, Xcode (macOS only for iOS), CocoaPods.
- **iOS requires macOS**: You cannot build iOS locally without a Mac. (Solutions in Section 6.)
- **Upgrade pain**: Upgrading between RN versions can be a multi-day effort.
- **No OTA updates out of the box**: You need CodePush or a similar service.

---

## 5. Environment Setup on Linux (No Mac)

You are on Manjaro Linux. Here is exactly what you can and cannot do.

### What You CAN Set Up Locally

**Android development** works perfectly on Linux:

```bash
# 1. Install Node.js 20+ (required for RN 0.74+)
# Use nvm or your package manager
nvm install 20
nvm use 20

# 2. Install JDK 17 (required for RN 0.74+)
sudo pacman -S jdk17-openjdk

# 3. Install Android Studio (for SDK, emulator, and build tools)
# Download from https://developer.android.com/studio
# Or via AUR: yay -S android-studio

# 4. Set environment variables in ~/.zshrc
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/tools
export PATH=$PATH:$ANDROID_HOME/tools/bin

# 5. Install SDK components via Android Studio:
#    - Android SDK Platform 34
#    - Android SDK Build-Tools 34.0.0
#    - Android Emulator
#    - NDK (for Hermes/New Architecture)

# 6. Create a project
npx react-native@latest init MyApp

# 7. Run on Android emulator or connected device
npx react-native run-android
```

### What You CANNOT Do Locally

- **Build for iOS**: Xcode only runs on macOS. No exceptions.
- **Run iOS Simulator**: macOS only.
- **Sign iOS apps**: Requires Xcode + Apple Developer account + provisioning profiles.

This is a hard Apple limitation, not a React Native one. See Section 6 for every workaround.

---

## 6. The iOS Problem -- And Every Solution Available to You

You don't have a Mac. You do have an iPhone. Here are your options, ranked by practicality for the STS rebuild.

### Option 1: Expo EAS Build (Recommended for the Rebuild)

Even if you use React Native CLI (bare workflow), you can **still use Expo's build service** via `expo prebuild` or by adding `expo` as a dependency.

```bash
# Install expo in a bare RN project
npx install-expo-modules@latest

# Build iOS in the cloud
eas build --platform ios
```

- **No Mac needed**: Expo's servers run macOS with Xcode.
- **Cost**: Free tier gives you 15 iOS builds/month. Starter ($19/mo) gives you more.
- **You still own the native code**: This is not the "managed" Expo workflow. You keep your `android/` and `ios/` directories.
- **Code signing**: EAS handles provisioning profiles and certificates. You provide your Apple Developer account credentials.

### Option 2: Cloud Mac Services

Rent a Mac in the cloud and SSH into it.

| Service | Cost | Notes |
|---------|------|-------|
| **MacinCloud** | ~$20-50/mo | Managed Mac VPS |
| **AWS EC2 Mac** | ~$0.65/hr (mac1.metal) | Bare metal Mac instances |
| **GitHub Actions (macOS runners)** | Free for public repos, paid for private | CI/CD only, not interactive dev |

### Option 3: CI/CD Build Pipelines

Set up a CI/CD pipeline that builds iOS on macOS runners:

- **Codemagic**: Purpose-built for mobile CI/CD. Free tier includes 500 min/mo of macOS builds.
- **GitHub Actions**: macOS runners available. Configure with Fastlane.
- **Bitrise**: Mobile-first CI/CD with Mac build agents.

### Option 4: Testing on Your Physical iPhone

Even without building locally, you can test on your iPhone:

1. **Build via EAS/CI** → Get an `.ipa` file.
2. **Distribute via TestFlight** (requires Apple Developer account, $99/year).
3. **Or use Ad Hoc distribution** with your device's UDID registered.

For development iteration:
- **Expo Dev Client**: Install a custom development build on your iPhone. Then push JS updates over the network without rebuilding.
- **EAS Update (OTA)**: Push JS-only changes to your phone instantly.

### The Practical Setup for This Project

```
Development: Linux (Manjaro)
├── Write all JS/TS code locally
├── Test Android locally (emulator + physical device)
├── Build iOS via EAS Build (cloud)
├── Test iOS via TestFlight or Dev Client on your iPhone
└── Push JS updates via EAS Update (no rebuild needed)
```

This is a perfectly viable professional setup. Many teams work this way.

---

## 7. Project Anatomy Under RN CLI

### The `android/` Directory

```
android/
├── app/
│   ├── build.gradle          ← App-level build config (SDK versions, signing, dependencies)
│   ├── src/main/
│   │   ├── AndroidManifest.xml   ← Permissions, deep links, activities
│   │   ├── java/.../
│   │   │   ├── MainActivity.java     ← Entry point (loads RN)
│   │   │   └── MainApplication.java  ← App-level config (packages, Hermes, Flipper)
│   │   └── res/              ← Native resources (icons, splash screens)
│   └── google-services.json  ← Firebase config
├── build.gradle              ← Root build config (Gradle version, Kotlin, Google Services)
├── settings.gradle           ← Project module definitions
└── gradle.properties         ← Build properties (newArchEnabled, hermesEnabled)
```

Key properties in `gradle.properties` for the New Architecture:

```properties
# Enable New Architecture
newArchEnabled=true
# Enable Hermes (default in 0.74+)
hermesEnabled=true
```

### The `ios/` Directory

```
ios/
├── Podfile                   ← CocoaPods dependency manager (like Gradle for iOS)
├── MyApp/
│   ├── AppDelegate.mm        ← Entry point (loads RN, configures modules)
│   ├── Info.plist             ← App metadata, permissions, URL schemes
│   └── GoogleService-Info.plist  ← Firebase config
├── MyApp.xcworkspace         ← Xcode workspace (open this, not .xcodeproj)
└── Pods/                     ← Installed CocoaPods (like node_modules)
```

### Metro Bundler Configuration

Metro is RN's bundler. It resolves modules, transforms code via Babel, and produces a bundle.

```javascript
// metro.config.js
const { getDefaultConfig, mergeConfig } = require('@react-native/metro-config');

const config = {
  resolver: {
    // Path aliases (if using babel-plugin-module-resolver)
    // Custom source extensions
  },
  transformer: {
    // Custom transformers
  },
};

module.exports = mergeConfig(getDefaultConfig(__dirname), config);
```

### Path Aliases (Important for the STS codebase)

The STS project uses `@` aliases (`@components`, `@screens`, `@constants`, etc.). These are configured in `babel.config.js`:

```javascript
// babel.config.js
module.exports = {
  presets: ['module:metro-react-native-babel-preset'],
  plugins: [
    ['module-resolver', {
      root: ['./src'],
      alias: {
        '@components': './src/components',
        '@screens': './src/screens',
        '@constants': './src/constants',
        '@themes': './src/themes',
        '@navigator': './src/navigator',
        '@reducers': './src/reducers',
        '@storage': './src/storage',
        '@helpers': './src/helpers',
        '@languages': './src/languages',
        '@apiCalls': './src/apiCalls',
      }
    }]
  ]
};
```

---

## 8. Native Modules and Turbo Modules

### Native Modules (Old Architecture)

In the old architecture, you write a native module by:
1. Writing Java/Kotlin (Android) or Objective-C/Swift (iOS) code.
2. Registering it via `ReactPackage` (Android) or `RCTBridgeModule` (iOS).
3. Accessing it in JS via `NativeModules.MyModule`.

All communication goes through the Bridge (async JSON).

### Turbo Modules (New Architecture)

Turbo Modules replace Native Modules. Key differences:
- **Lazy loading**: Only initialized when first accessed (faster startup).
- **Type safety**: Define a TypeScript/Flow spec, Codegen generates native interfaces.
- **Synchronous calls**: Can return values synchronously via JSI (no Bridge).

```typescript
// NativeMyModule.ts (Turbo Module spec)
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  multiply(a: number, b: number): number; // Synchronous!
}

export default TurboModuleRegistry.getEnforcing<Spec>('MyModule');
```

### What This Means for the STS Rebuild

Most third-party libraries have already migrated to support the New Architecture. When a library hasn't, you have three options:
1. **Use an interop layer** (RN 0.74+ provides backward compatibility for many old-style modules).
2. **Find an alternative library** that supports the New Architecture.
3. **Fork and migrate** the library yourself (last resort).

---

## 9. The Dependency Ecosystem -- What to Know for the Rebuild

### Auto-linking (Since RN 0.60)

Native libraries are automatically linked when you install them. No more `react-native link`. Just:

```bash
npm install @react-native-firebase/app
cd ios && pod install  # iOS only (handled by EAS if building in cloud)
```

### Common Categories of Dependencies

| Category | Old (STS 0.65.1) | Modern Equivalent |
|----------|-------------------|-------------------|
| Navigation | `@react-navigation/native` v6 | `@react-navigation/native` v7 (or Expo Router) |
| State Management | `redux` + `redux-thunk` | `@reduxjs/toolkit` (or Zustand, Jotai) |
| Firebase | `@react-native-firebase/*` v14 | `@react-native-firebase/*` v22 (Modular API) |
| Notifications | `react-native-push-notification` | `@notifee/react-native` |
| HTTP Client | `axios` | `axios` (still fine) or TanStack Query |
| Video Player | `react-native-video` v5 | `react-native-video` v6+ |
| Icons | `react-native-vector-icons` | `react-native-vector-icons` or `@expo/vector-icons` |
| Input Masking | `react-native-masked-text` | `react-native-mask-input` (already partially migrated) |

### Compatibility Checking

Before adding any library to the rebuild, check:
1. **[React Native Directory](https://reactnative.directory/)**: Filter by "New Architecture" support.
2. **Library's GitHub**: Look for `fabric` or `turbomodule` support in their docs.
3. **`npx react-native-new-arch-check`**: Validates a library against the New Architecture.

---

## 10. Build, Sign, and Ship

### Android Build (Local on Linux)

```bash
# Debug build
npx react-native run-android

# Release build (generates APK/AAB)
cd android
./gradlew assembleRelease      # APK
./gradlew bundleRelease         # AAB (for Play Store)
```

Signing requires a keystore:

```bash
keytool -genkeypair -v -storetype PKCS12 \
  -keystore my-release-key.keystore \
  -alias my-key-alias -keyalg RSA -keysize 2048 -validity 10000
```

Configure in `android/app/build.gradle`:

```groovy
signingConfigs {
    release {
        storeFile file('my-release-key.keystore')
        storePassword 'xxx'
        keyAlias 'my-key-alias'
        keyPassword 'xxx'
    }
}
```

### iOS Build (Via EAS or CI)

```bash
# Using EAS Build
eas build --platform ios --profile production

# EAS handles:
# - Provisioning profiles
# - Code signing certificates
# - Xcode build
# - IPA generation
```

### App Store / Play Store Submission

```bash
# Android: Upload AAB to Google Play Console
# iOS: Use eas submit or Transporter app
eas submit --platform ios
eas submit --platform android
```

---

## 11. Debugging and Dev Tools in the New Architecture

### Old Tools (Removed in 0.74+)

- **Flipper**: Removed. Was a desktop debugging tool. Too heavy, too many issues.
- **Remote JS Debugging** (Chrome tab): Removed. Ran JS in Chrome's V8 instead of Hermes, causing behavior differences.

### New Tools

- **React Native DevTools**: The official replacement. Accessible via `j` in the Metro terminal.
  - Component Inspector
  - Profiler
  - Network inspector
  - Console
- **Hermes Debugger**: Direct debugging of Hermes via Chrome DevTools Protocol.
- **React DevTools** (standalone): Still works for component tree inspection.

```bash
# Start Metro with debugging
npx react-native start

# Press 'j' to open DevTools
# Press 'd' to open the Dev Menu on device
```

---

## 12. Key Decisions for the STS Rebuild

Based on the contract and the codebase, here are the technical decisions you face:

### 1. Target Version

The contract says 0.74.x, but as of now 0.78+ is available. **Recommendation**: Target **0.76+** (New Architecture production-ready, latest stable tooling). Going to 0.78 gives you React 19 support.

### 2. Class Components → Functional Components

The entire STS codebase uses **class components**. The rebuild should use **functional components with hooks**. This is not optional for React 19 compatibility -- many class component lifecycle methods are deprecated.

### 3. State Management

Current: Redux + Redux Thunk with manual boilerplate. Options for the rebuild:
- **Redux Toolkit (RTK)**: If you want to keep Redux but with 80% less boilerplate. RTK Query can replace the entire API layer.
- **Zustand**: Simpler, lighter. Good if the state shape isn't deeply nested.
- **TanStack Query** (for server state) + **Zustand** (for client state): Modern split approach.

### 4. iOS Development Strategy

Since you're on Linux with an iPhone:
- Use **EAS Build** for iOS builds.
- Use **EAS Update** for OTA JS pushes during development.
- Install a **development build** on your iPhone via TestFlight.
- Test Android locally on emulator + physical device.

### 5. TypeScript

The current codebase is pure JavaScript. The rebuild should be in **TypeScript**. The New Architecture's Codegen requires TS/Flow specs for Turbo Modules anyway.

---

> **Bottom line**: React Native CLI gives you full native control at the cost of setup complexity. For the STS rebuild, the biggest hurdle is iOS builds from Linux -- solved by EAS Build or cloud CI. The New Architecture migration is not a library swap; it's a fundamental change in how JS talks to native code, and every dependency must be validated against it.
