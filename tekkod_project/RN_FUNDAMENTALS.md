# React Native Fundamentals -- Zero to Dangerous by Friday

> **Audience**: A developer who knows JavaScript/TypeScript and web React, but has never built a mobile app with React Native.
> **Goal**: By the end of this document, you understand every concept needed to read the STS codebase, make architectural decisions, and start writing production RN code.
> **Approach**: Every concept is shown in both the **Expo** way and the **RN CLI** way, side by side. Real code from the STS codebase is used to illustrate what patterns look like in the wild.

---

## Table of Contents

### Part I -- The Basics
1. [What Is React Native, Really](#1-what-is-react-native-really)
2. [Two Roads: Expo vs. RN CLI](#2-two-roads-expo-vs-rn-cli)
3. [Creating Your First Project](#3-creating-your-first-project)
4. [The Core Primitives -- View, Text, Image, and Friends](#4-the-core-primitives----view-text-image-and-friends)
5. [Styling -- CSS Is Dead, Long Live StyleSheet](#5-styling----css-is-dead-long-live-stylesheet)
6. [Flexbox -- The Only Layout System](#6-flexbox----the-only-layout-system)
7. [Handling User Input](#7-handling-user-input)
8. [Lists -- FlatList, SectionList, and Why ScrollView Will Kill You](#8-lists----flatlist-sectionlist-and-why-scrollview-will-kill-you)

### Part II -- Architecture
9. [Components: Class vs. Functional (and Why It Matters)](#9-components-class-vs-functional-and-why-it-matters)
10. [Hooks -- The Modern Foundation](#10-hooks----the-modern-foundation)
11. [Navigation and Routing](#11-navigation-and-routing)
12. [State Management -- From useState to Redux to Zustand](#12-state-management----from-usestate-to-redux-to-zustand)
13. [Talking to APIs](#13-talking-to-apis)
14. [Local Storage -- AsyncStorage and Beyond](#14-local-storage----asyncstorage-and-beyond)

### Part III -- The Platform
15. [The Bridge, JSI, and How JS Talks to Native](#15-the-bridge-jsi-and-how-js-talks-to-native)
16. [The Build Pipeline -- Metro, Gradle, Xcode](#16-the-build-pipeline----metro-gradle-xcode)
17. [Platform-Specific Code](#17-platform-specific-code)
18. [Permissions](#18-permissions)
19. [Push Notifications](#19-push-notifications)
20. [Deep Linking](#20-deep-linking)

### Part IV -- Advanced
21. [Performance -- What Makes RN Apps Slow and How to Fix It](#21-performance----what-makes-rn-apps-slow-and-how-to-fix-it)
22. [Animations -- Animated API, Reanimated, and Gesture Handler](#22-animations----animated-api-reanimated-and-gesture-handler)
23. [Native Modules -- When JS Is Not Enough](#23-native-modules----when-js-is-not-enough)
24. [Testing](#24-testing)
25. [Over-The-Air Updates](#25-over-the-air-updates)
26. [Putting It All Together -- Reading the STS Codebase](#26-putting-it-all-together----reading-the-sts-codebase)

---

# Part I -- The Basics

---

## 1. What Is React Native, Really

If you know React for the web, you know 60% of React Native. The difference:

| Web React | React Native |
|-----------|-------------|
| Renders to `<div>`, `<span>`, `<p>` | Renders to `UIView` (iOS), `android.view.View` (Android) |
| Styled with CSS files | Styled with JS objects (`StyleSheet.create`) |
| Runs in a browser | Runs in a native app shell with a JS engine (Hermes) |
| `<div>` | `<View>` |
| `<p>` or `<span>` | `<Text>` |
| `<img>` | `<Image>` |
| `<input>` | `<TextInput>` |
| `<button>` | `<Pressable>` or `<TouchableOpacity>` |
| `<ul>` + `<li>` | `<FlatList>` |

Your React knowledge transfers directly: JSX, props, state, hooks, context, effects -- all the same. What changes is the **primitives** you build with and **how styling works**.

### The Execution Model

```
Your Code (JS/TS)
    ↓
Metro Bundler (bundles into a single JS file)
    ↓
Hermes Engine (compiles to bytecode, runs in the app)
    ↓
React Native Renderer (converts your component tree to native view commands)
    ↓
Native Views (UIKit on iOS, Android Views on Android)
```

You write JS. It becomes native UI. There is no WebView, no HTML, no DOM.

---

## 2. Two Roads: Expo vs. RN CLI

When you start a React Native project, you pick one of two approaches. Think of it like choosing between a fully-loaded car (Expo) and a bare chassis you assemble yourself (RN CLI).

### Side-by-Side Comparison

| Aspect | Expo | RN CLI (Bare) |
|--------|------|---------------|
| **Init command** | `npx create-expo-app@latest` | `npx @react-native-community/cli@latest init MyApp` |
| **Project structure** | No `android/` or `ios/` dirs (until you eject) | Full `android/` and `ios/` dirs from day one |
| **Adding native libs** | Must be Expo-compatible, or use dev builds | Any native library, no restrictions |
| **Building iOS** | Cloud build via EAS (no Mac needed) | Requires Mac + Xcode locally |
| **Building Android** | Cloud build via EAS or local | Local with Android Studio/Gradle |
| **OTA Updates** | Built-in via EAS Update | Need CodePush or custom solution |
| **Dev testing** | Expo Go app (limited) or Dev Client (full) | Direct on emulator/device |
| **Ejecting** | `npx expo prebuild` generates native dirs | Already bare |
| **Config** | `app.json` / `app.config.js` | Native files (`AndroidManifest.xml`, `Info.plist`) |
| **Best for** | Most apps, teams without native devs | Apps needing deep native customization |

### The Key Insight

Expo is not a different framework. It is **React Native + managed tooling + cloud services**. Under the hood, an Expo app IS a React Native app. You can always eject from Expo to bare, and you can add Expo tools to a bare project.

For the STS rebuild, the likely path is: **Expo (bare workflow)** -- meaning you have full native control but use Expo's build service (EAS) because you're on Linux without a Mac.

---

## 3. Creating Your First Project

### The Expo Way

```bash
# Create project
npx create-expo-app@latest MyApp
cd MyApp

# Start development
npx expo start

# Scan QR code with Expo Go app on your phone
# Or press 'a' for Android emulator
```

What you get:

```
MyApp/
├── app/                    ← Your screens (file-based routing)
│   ├── _layout.tsx         ← Root layout
│   ├── index.tsx           ← Home screen
│   └── +not-found.tsx      ← 404 screen
├── assets/                 ← Images, fonts
├── components/             ← Reusable components
├── constants/              ← Colors, config
├── app.json                ← Expo config
├── package.json
└── tsconfig.json
```

### The RN CLI Way

```bash
# Create project (requires Android Studio / Xcode set up first)
npx @react-native-community/cli@latest init MyApp
cd MyApp

# Start Metro bundler
npx react-native start

# In another terminal, build and run
npx react-native run-android    # Android
npx react-native run-ios        # iOS (Mac only)
```

What you get:

```
MyApp/
├── android/                ← Full Android native project
├── ios/                    ← Full iOS native project
├── App.tsx                 ← Your starting component
├── index.js                ← Entry point
├── metro.config.js         ← Bundler config
├── babel.config.js         ← Babel config
├── package.json
└── tsconfig.json
```

### What the STS Project Looks Like (RN CLI)

The STS app was created with RN CLI. Its entry point:

```javascript
// index.js -- the very first file that runs
import {AppRegistry} from 'react-native';
import App from './src';                          // Points to src/index.js
import {name as appName} from './app.json';       // "SteamTheStreet"

AppRegistry.registerComponent(appName, () => App);
```

`AppRegistry.registerComponent` is the RN equivalent of `ReactDOM.render`. It tells the native shell: "here's the root React component."

---

## 4. The Core Primitives -- View, Text, Image, and Friends

React Native provides a small set of core components. Every UI you see is composed of these.

### View -- The Universal Container

`<View>` is the `<div>` of React Native. It's a container that supports flexbox layout, styling, touch handling, and accessibility.

```tsx
import { View, Text } from 'react-native';

function Card() {
  return (
    <View style={{ padding: 16, backgroundColor: '#fff', borderRadius: 8 }}>
      <Text>Hello from a card</Text>
    </View>
  );
}
```

### Text -- All Text Must Be Wrapped

Unlike the web where you can put text anywhere, in RN **all text must be inside a `<Text>` component**. This will crash:

```tsx
// WRONG -- will crash
<View>Hello</View>

// CORRECT
<View><Text>Hello</Text></View>
```

Text supports nesting for inline styling:

```tsx
<Text style={{ fontSize: 16 }}>
  Don't have an account?{' '}
  <Text style={{ color: '#00AEFF' }} onPress={goToSignup}>
    Sign Up
  </Text>
</Text>
```

The STS codebase uses this pattern in the login screen:

```javascript
// From STS: src/screens/3_LoginScreen/index.js
<Text style={COMMON_STYLE.headerMsgStyle}>
    {localize("DONT_HAVE_ACCOUNT") + " "}
    <Text
        style={{ color: COLORS.LIGHT_BLUE }}
        onPress={() => this.props.navigation.navigate("SIGN_UP_SCREEN")}
    >
        {localize("SIGN_UP")}
    </Text>
</Text>
```

### Image -- Local and Remote

```tsx
import { Image } from 'react-native';

// Local image (bundled with the app)
<Image source={require('./assets/logo.png')} style={{ width: 100, height: 100 }} />

// Remote image (from URL -- MUST specify width and height)
<Image source={{ uri: 'https://example.com/photo.jpg' }} style={{ width: 200, height: 200 }} />
```

Key difference from web: remote images **must** have explicit dimensions. There's no intrinsic sizing like `<img>` on the web.

### Pressable / TouchableOpacity -- Buttons

React Native has no `<button>` element. You make things tappable with:

```tsx
import { Pressable, TouchableOpacity, Text } from 'react-native';

// Modern approach (recommended)
<Pressable
  onPress={() => console.log('Pressed!')}
  style={({ pressed }) => [
    { padding: 12, backgroundColor: pressed ? '#ddd' : '#00AEFF', borderRadius: 8 }
  ]}
>
  <Text style={{ color: '#fff' }}>Tap Me</Text>
</Pressable>

// Legacy approach (still widely used, including in STS)
<TouchableOpacity onPress={() => console.log('Pressed!')} style={{ padding: 12 }}>
  <Text>Tap Me</Text>
</TouchableOpacity>
```

`Pressable` is the modern API. `TouchableOpacity` (used throughout STS) reduces opacity on press. Both work fine.

### ScrollView -- Scrollable Container

```tsx
import { ScrollView, Text } from 'react-native';

<ScrollView>
  <Text>Content that might be taller than the screen</Text>
  {/* More content... */}
</ScrollView>
```

**Critical rule**: `ScrollView` renders ALL its children at once. Fine for small content (forms, settings). Deadly for long lists. For lists, use `FlatList` (covered in Section 8).

### TextInput -- Text Fields

```tsx
import { TextInput } from 'react-native';

const [email, setEmail] = useState('');

<TextInput
  value={email}
  onChangeText={setEmail}
  placeholder="Enter your email"
  keyboardType="email-address"
  autoCapitalize="none"
  style={{ borderWidth: 1, borderColor: '#ccc', padding: 12, borderRadius: 8 }}
/>
```

Common `keyboardType` values: `'default'`, `'email-address'`, `'numeric'`, `'phone-pad'`.

### ActivityIndicator -- Loading Spinner

```tsx
import { ActivityIndicator } from 'react-native';

<ActivityIndicator size="large" color="#00AEFF" />
```

### Modal -- Native Modals

```tsx
import { Modal, View, Text } from 'react-native';

<Modal visible={isVisible} animationType="slide" transparent={true}>
  <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
    <View style={{ backgroundColor: '#fff', padding: 20, borderRadius: 12 }}>
      <Text>Modal Content</Text>
    </View>
  </View>
</Modal>
```

### SafeAreaView -- Avoiding Notches

Modern phones have notches, dynamic islands, home indicators. `SafeAreaView` ensures your content doesn't hide behind them:

```tsx
import { SafeAreaView } from 'react-native-safe-area-context'; // Use the community version

<SafeAreaView style={{ flex: 1 }}>
  {/* Your content is safe from notches */}
</SafeAreaView>
```

---

## 5. Styling -- CSS Is Dead, Long Live StyleSheet

There are no CSS files in React Native. Styling is done with JavaScript objects.

### The Basics

```tsx
import { StyleSheet, View, Text } from 'react-native';

function MyComponent() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Hello</Text>
      <Text style={[styles.subtitle, { color: 'red' }]}>World</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000',
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
  },
});
```

### Key Differences from CSS

| CSS | React Native |
|-----|-------------|
| `background-color` | `backgroundColor` (camelCase) |
| `font-size: 16px` | `fontSize: 16` (no units, always points) |
| `border: 1px solid #ccc` | `borderWidth: 1, borderColor: '#ccc'` |
| `margin: 10px 20px` | `marginVertical: 10, marginHorizontal: 20` |
| `class="foo bar"` | `style={[styles.foo, styles.bar]}` (array) |
| Inheritance | **No inheritance** (except inside `<Text>`) |
| Global styles | **No global styles** -- each component styles itself |
| `%` units | Use `flex` proportions instead |
| `vh` / `vw` | Use `Dimensions.get('window')` |

### No Style Inheritance

This is the biggest gotcha. On the web, a child `<span>` inherits `font-size` from its parent `<div>`. In RN, **nothing inherits** except within nested `<Text>` components.

```tsx
// WRONG: The inner Text does NOT inherit fontSize from the View
<View style={{ fontSize: 20 }}>
  <Text>This won't be 20pt</Text>
</View>

// CORRECT: Text inherits from parent Text
<Text style={{ fontSize: 20 }}>
  <Text style={{ fontWeight: 'bold' }}>This IS 20pt and bold</Text>
</Text>
```

### StyleSheet.create vs. Inline Objects

`StyleSheet.create` validates your styles at creation time and assigns IDs for performance. Always prefer it over inline style objects for static styles:

```tsx
// Good -- created once, validated, optimized
const styles = StyleSheet.create({
  box: { width: 100, height: 100, backgroundColor: 'red' }
});

// Fine for dynamic styles -- merged with static
<View style={[styles.box, { opacity: isVisible ? 1 : 0 }]} />
```

### How STS Does It: Style Helpers

STS builds a utility-function-based style system. Here's their approach from the codebase:

```javascript
// From STS: src/themes/commonStyles.js -- style factory functions
export const COMMON_STYLE = StyleSheet.create({
  // Dynamic text style generator
  textStyle: (size, color = COLORS.BLACK, font = "BASE", align) => {
    return {
      fontSize: Responsive.getFontSize(size),
      fontFamily: FONTS[font],
      color: color,
      textAlign: align,
      lineHeight: Responsive.getFontSize(size) + 3,
    };
  },

  // Dynamic button style generator
  fillBtnStyle: (color = COLORS.WHITE, width, height = 7) => {
    return {
      height: Responsive.getHeight(height),
      width: width ? Responsive.getWidth(width) : "100%",
      borderRadius: Responsive.getWidth(2),
      backgroundColor: color,
      justifyContent: "center",
      alignItems: "center",
    };
  },
});

// Usage throughout the app:
<Text style={COMMON_STYLE.textStyle(16, COLORS.WHITE, "BOLD")}>Sign In</Text>
```

And their responsive sizing utility:

```javascript
// From STS: src/helpers/responsive.js
import { Dimensions, PixelRatio } from 'react-native';
const { height, width } = Dimensions.get('window');

export const Responsive = {
  getHeight: function (h) {
    const screenHeight = width < height ? height : width;
    return PixelRatio.roundToNearestPixel(screenHeight * (h / 100));
  },
  getWidth: function (w) {
    const screenWidth = width < height ? width : height;
    return PixelRatio.roundToNearestPixel(screenWidth * (w / 100));
  },
  getFontSize: function (size) {
    const scale = width / (width < 450 ? 320 : 450);
    return Math.round(PixelRatio.roundToNearestPixel(size * scale));
  },
};

// Responsive.getHeight(10)  → 10% of screen height in pixels
// Responsive.getWidth(50)   → 50% of screen width in pixels
```

This gives percentage-based sizing. `Responsive.getWidth(4)` = 4% of screen width.

---

## 6. Flexbox -- The Only Layout System

React Native **only** supports Flexbox. No Grid, no `position: static`, no floats. But it's Flexbox with some differences from web CSS.

### The Crucial Difference: Column by Default

On the web, `flex-direction` defaults to `row` (horizontal). In React Native, it defaults to **`column`** (vertical). This trips up every web developer.

```tsx
// This stacks children VERTICALLY (column is default)
<View style={{ flex: 1 }}>
  <Text>Item 1</Text>   {/* Top */}
  <Text>Item 2</Text>   {/* Below Item 1 */}
  <Text>Item 3</Text>   {/* Below Item 2 */}
</View>

// This lays children HORIZONTALLY
<View style={{ flex: 1, flexDirection: 'row' }}>
  <Text>Item 1</Text>   {/* Left */}
  <Text>Item 2</Text>   {/* Right of Item 1 */}
  <Text>Item 3</Text>   {/* Right of Item 2 */}
</View>
```

### The flex Property

`flex: 1` means "take up all available space." Multiple siblings with `flex` share space proportionally:

```tsx
<View style={{ flex: 1 }}>
  <View style={{ flex: 1, backgroundColor: 'red' }} />    {/* 1/3 of space */}
  <View style={{ flex: 2, backgroundColor: 'blue' }} />   {/* 2/3 of space */}
</View>
```

### Common Layout Patterns

**Centering everything:**

```tsx
<View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
  <Text>I'm centered both ways</Text>
</View>
```

**Header + Content + Footer:**

```tsx
<View style={{ flex: 1 }}>
  <View style={{ height: 60, backgroundColor: '#333' }}>
    <Text style={{ color: '#fff' }}>Header</Text>
  </View>
  <View style={{ flex: 1 }}>
    <Text>Content fills remaining space</Text>
  </View>
  <View style={{ height: 80, backgroundColor: '#333' }}>
    <Text style={{ color: '#fff' }}>Footer</Text>
  </View>
</View>
```

**Row with spaced items (like STS feed cell):**

```tsx
// From STS: src/components/views/feedCell.js
<View style={{ flexDirection: 'row', alignItems: 'flex-end' }}>
  <Text style={{ flex: 1 }}>2 hours ago</Text>  {/* Takes remaining space, pushes others right */}
  <Text style={{ marginRight: 8 }}>42</Text>     {/* Like count */}
  <TouchableOpacity onPress={handleLike}>
    <Image source={heartIcon} style={{ width: 20, height: 20 }} />
  </TouchableOpacity>
</View>
```

### Cheat Sheet

| Property | Values | Notes |
|----------|--------|-------|
| `flexDirection` | `'column'` (default), `'row'`, `'column-reverse'`, `'row-reverse'` | Main axis direction |
| `justifyContent` | `'flex-start'`, `'center'`, `'flex-end'`, `'space-between'`, `'space-around'`, `'space-evenly'` | Distribute along **main** axis |
| `alignItems` | `'flex-start'`, `'center'`, `'flex-end'`, `'stretch'` (default), `'baseline'` | Align along **cross** axis |
| `alignSelf` | Same as alignItems | Override parent's alignItems for one child |
| `flex` | Number | How much space to take relative to siblings |
| `flexWrap` | `'nowrap'` (default), `'wrap'` | Wrap children to next line |
| `gap` | Number | Space between children (RN 0.71+) |
| `position` | `'relative'` (default), `'absolute'` | Only these two exist in RN |

### position: absolute

Works like CSS absolute positioning but there's no `position: static` or `position: fixed`. Absolute children are positioned relative to their parent.

```tsx
<View style={{ width: 200, height: 200, backgroundColor: '#eee' }}>
  {/* Badge in top-right corner */}
  <View style={{
    position: 'absolute',
    top: -5,
    right: -5,
    width: 20,
    height: 20,
    borderRadius: 10,
    backgroundColor: 'red',
  }} />
</View>
```

---

## 7. Handling User Input

### TextInput -- The Only Input Element

There is no `<select>`, `<checkbox>`, `<radio>` built into RN. Just `<TextInput>`. Everything else is built from components.

```tsx
import { useState } from 'react';
import { TextInput, View, Text } from 'react-native';

function LoginForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  return (
    <View>
      <Text>Email</Text>
      <TextInput
        value={email}
        onChangeText={setEmail}
        placeholder="you@email.com"
        keyboardType="email-address"
        autoCapitalize="none"
        autoCorrect={false}
        style={{ borderWidth: 1, borderColor: '#ccc', padding: 12, borderRadius: 8 }}
      />

      <Text>Password</Text>
      <TextInput
        value={password}
        onChangeText={setPassword}
        placeholder="********"
        secureTextEntry={true}    // Hides characters (password field)
        style={{ borderWidth: 1, borderColor: '#ccc', padding: 12, borderRadius: 8 }}
      />
    </View>
  );
}
```

### The Keyboard Problem

On mobile, the keyboard slides up and covers your inputs. Solutions:

```tsx
// Option 1: KeyboardAvoidingView (built-in)
import { KeyboardAvoidingView, Platform } from 'react-native';

<KeyboardAvoidingView
  behavior={Platform.OS === 'ios' ? 'padding' : 'height'}
  style={{ flex: 1 }}
>
  {/* Your form */}
</KeyboardAvoidingView>

// Option 2: KeyboardAwareScrollView (community, used by STS)
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';

<KeyboardAwareScrollView>
  {/* Your form scrolls automatically when keyboard appears */}
</KeyboardAwareScrollView>
```

### Touch Events

```tsx
import { Pressable, GestureResponderEvent } from 'react-native';

<Pressable
  onPress={(event: GestureResponderEvent) => {
    console.log('Tapped at:', event.nativeEvent.locationX, event.nativeEvent.locationY);
  }}
  onLongPress={() => console.log('Long pressed!')}
  onPressIn={() => console.log('Finger down')}
  onPressOut={() => console.log('Finger up')}
>
  <Text>Interactive element</Text>
</Pressable>
```

---

## 8. Lists -- FlatList, SectionList, and Why ScrollView Will Kill You

### The Problem

If you render 1,000 items inside a `<ScrollView>`, React creates 1,000 views in memory. The app crashes or freezes.

### FlatList -- Virtualized Lists

`FlatList` only renders items that are currently visible on screen (plus a small buffer). This is called **virtualization**.

```tsx
import { FlatList, View, Text } from 'react-native';

const DATA = [
  { id: '1', title: 'First Item' },
  { id: '2', title: 'Second Item' },
  // ... thousands of items
];

function MyList() {
  return (
    <FlatList
      data={DATA}
      keyExtractor={(item) => item.id}
      renderItem={({ item }) => (
        <View style={{ padding: 16, borderBottomWidth: 1, borderColor: '#eee' }}>
          <Text>{item.title}</Text>
        </View>
      )}
    />
  );
}
```

### FlatList Props You Must Know

| Prop | What It Does |
|------|-------------|
| `data` | Array of items to render |
| `renderItem` | Function that returns JSX for each item |
| `keyExtractor` | Function that returns a unique key per item |
| `onEndReached` | Called when user scrolls near the end (infinite scroll) |
| `onEndReachedThreshold` | How close to the end triggers `onEndReached` (0-1) |
| `refreshing` | Boolean for pull-to-refresh state |
| `onRefresh` | Function called on pull-to-refresh |
| `ListHeaderComponent` | Component rendered before the list |
| `ListFooterComponent` | Component rendered after the list (loading spinner) |
| `ListEmptyComponent` | Component rendered when `data` is empty |
| `ItemSeparatorComponent` | Component rendered between items |
| `initialNumToRender` | How many items to render initially (default 10) |

### Infinite Scroll + Pull to Refresh (The STS Pattern)

The STS Feed screen implements both. Here's the concept in modern code:

```tsx
function FeedScreen() {
  const [feeds, setFeeds] = useState([]);
  const [page, setPage] = useState(1);
  const [refreshing, setRefreshing] = useState(false);
  const [loadingMore, setLoadingMore] = useState(false);

  const fetchFeeds = async (pageNum: number, isRefresh = false) => {
    if (isRefresh) setRefreshing(true);
    else if (pageNum > 1) setLoadingMore(true);

    const response = await api.get(`/feed/list?page=${pageNum}`);

    if (isRefresh || pageNum === 1) {
      setFeeds(response.data);
    } else {
      setFeeds(prev => [...prev, ...response.data]); // Append
    }

    setRefreshing(false);
    setLoadingMore(false);
  };

  useEffect(() => { fetchFeeds(1); }, []);

  return (
    <FlatList
      data={feeds}
      keyExtractor={(item) => item.id.toString()}
      renderItem={({ item }) => <FeedCard item={item} />}
      // Pull to refresh
      refreshing={refreshing}
      onRefresh={() => {
        setPage(1);
        fetchFeeds(1, true);
      }}
      // Infinite scroll
      onEndReached={() => {
        if (!loadingMore) {
          const nextPage = page + 1;
          setPage(nextPage);
          fetchFeeds(nextPage);
        }
      }}
      onEndReachedThreshold={0.5}
      // Loading footer
      ListFooterComponent={loadingMore ? <ActivityIndicator /> : null}
      // Empty state
      ListEmptyComponent={<Text>No posts yet</Text>}
    />
  );
}
```

### SectionList -- Grouped Data

Like `FlatList` but with section headers:

```tsx
import { SectionList, Text, View } from 'react-native';

const DATA = [
  { title: 'Favorites', data: ['Feed A', 'Feed B'] },
  { title: 'Recent', data: ['Feed C', 'Feed D', 'Feed E'] },
];

<SectionList
  sections={DATA}
  keyExtractor={(item, index) => item + index}
  renderItem={({ item }) => <Text>{item}</Text>}
  renderSectionHeader={({ section }) => (
    <Text style={{ fontWeight: 'bold', fontSize: 18 }}>{section.title}</Text>
  )}
/>
```

### FlashList -- The Modern Alternative

`@shopify/flash-list` is a drop-in replacement for `FlatList` with better performance via cell recycling (like native `RecyclerView`/`UICollectionView`):

```bash
npm install @shopify/flash-list
```

```tsx
import { FlashList } from '@shopify/flash-list';

<FlashList
  data={feeds}
  renderItem={({ item }) => <FeedCard item={item} />}
  estimatedItemSize={200}    // Required: estimated height of each item
/>
```

---

# Part II -- Architecture

---

## 9. Components: Class vs. Functional (and Why It Matters)

### Class Components (What STS Uses)

The entire STS codebase uses class components. This is the **old** way:

```javascript
// From STS: src/screens/3_LoginScreen/index.js
class LoginScreen extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      email: { value: "", isError: false },
      password: { value: "", isError: false },
    };
  }

  componentDidMount() {
    // Runs after first render (like useEffect with [])
  }

  componentDidUpdate(prevProps) {
    // Runs after every re-render (like useEffect without deps)
  }

  componentWillUnmount() {
    // Cleanup (like useEffect's return function)
  }

  changeData(key, object) {
    this.setState({ [key]: { ...this.state[key], ...object } });
  }

  render() {
    return (
      <View>
        <TextInput
          value={this.state.email.value}
          onChangeText={(text) => this.changeData('email', { value: text })}
        />
      </View>
    );
  }
}
```

### Functional Components (What the Rebuild Should Use)

The modern equivalent:

```tsx
function LoginScreen() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    // Runs on mount
    return () => {
      // Cleanup on unmount
    };
  }, []);

  return (
    <View>
      <TextInput value={email} onChangeText={setEmail} />
      <TextInput value={password} onChangeText={setPassword} secureTextEntry />
    </View>
  );
}
```

### Why Functional Components Win

| Class | Functional |
|-------|-----------|
| `this.state` / `this.setState` | `useState` |
| `componentDidMount` | `useEffect(() => {}, [])` |
| `componentWillUnmount` | `useEffect(() => { return cleanup }, [])` |
| `shouldComponentUpdate` | `React.memo` |
| `this.props` | Function arguments |
| Verbose, boilerplate | Concise, composable |
| Lifecycle methods only | Custom hooks (reusable logic) |
| Cannot use hooks | Full hook support |

React 19 (used in latest RN) still supports class components, but **all new features target functional components exclusively**.

---

## 10. Hooks -- The Modern Foundation

Hooks are functions that let you "hook into" React features from functional components.

### useState -- Local State

```tsx
const [count, setCount] = useState(0);           // Initial value: 0
const [user, setUser] = useState<User | null>(null);  // TypeScript: nullable User
const [items, setItems] = useState<string[]>([]);      // Array

// Update:
setCount(5);                    // Direct value
setCount(prev => prev + 1);    // From previous value
setItems(prev => [...prev, 'new item']);  // Append to array
```

### useEffect -- Side Effects

```tsx
// Run once on mount (like componentDidMount)
useEffect(() => {
  fetchUserProfile();
}, []);  // Empty array = run once

// Run when a dependency changes
useEffect(() => {
  fetchFeed(selectedFilter);
}, [selectedFilter]);  // Runs whenever selectedFilter changes

// Cleanup (like componentWillUnmount)
useEffect(() => {
  const subscription = eventEmitter.addListener('event', handler);
  return () => {
    subscription.remove();  // Cleanup when component unmounts
  };
}, []);
```

### useRef -- Mutable References Without Re-renders

```tsx
const scrollViewRef = useRef<ScrollView>(null);
const timerRef = useRef<NodeJS.Timeout>();

// Scroll to top programmatically
scrollViewRef.current?.scrollTo({ y: 0, animated: true });

// Store a value that doesn't trigger re-render
timerRef.current = setTimeout(() => {}, 1000);
```

### useMemo -- Expensive Computation Caching

```tsx
const filteredFeeds = useMemo(() => {
  return feeds.filter(feed =>
    feed.tags.some(tag => selectedTags.includes(tag))
  );
}, [feeds, selectedTags]);  // Only recalculate when these change
```

### useCallback -- Stable Function References

```tsx
// Without useCallback: new function every render → children re-render
const handlePress = () => { navigation.navigate('Detail', { id: item.id }); };

// With useCallback: same function reference unless dependencies change
const handlePress = useCallback(() => {
  navigation.navigate('Detail', { id: item.id });
}, [item.id]);
```

### Custom Hooks -- Reusable Logic

This is the superpower of hooks. Extract common patterns into reusable functions:

```tsx
// Custom hook for API calls
function useApi<T>(endpoint: string) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    setLoading(true);
    api.get(endpoint)
      .then(response => setData(response.data))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, [endpoint]);

  return { data, loading, error };
}

// Usage in any component
function FeedScreen() {
  const { data: feeds, loading, error } = useApi<Feed[]>('/feed/list');

  if (loading) return <ActivityIndicator />;
  if (error) return <Text>Error: {error}</Text>;
  return <FlatList data={feeds} /* ... */ />;
}
```

---

## 11. Navigation and Routing

Navigation in RN is not built-in. You install a library. There are two main options.

### Option A: React Navigation (Imperative, Component-Based)

This is what the STS codebase uses, and it's the most mature option.

```bash
# Installation (Expo)
npx expo install @react-navigation/native @react-navigation/stack @react-navigation/bottom-tabs react-native-screens react-native-safe-area-context

# Installation (RN CLI)
npm install @react-navigation/native @react-navigation/stack @react-navigation/bottom-tabs react-native-screens react-native-safe-area-context
cd ios && pod install
```

**Basic Stack Navigator:**

```tsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Welcome">
        <Stack.Screen
          name="Welcome"
          component={WelcomeScreen}
          options={{ headerShown: false }}
        />
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerTitle: '' }}
        />
        <Stack.Screen
          name="Home"
          component={HomeScreen}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

**Navigating between screens:**

```tsx
function WelcomeScreen({ navigation }) {
  return (
    <View>
      <Button
        title="Log In"
        onPress={() => navigation.navigate('Login')}
      />
      <Button
        title="Sign Up"
        onPress={() => navigation.navigate('SignUp', { referralCode: 'ABC123' })}
      />
    </View>
  );
}

// Receiving params in the target screen:
function SignUpScreen({ route }) {
  const { referralCode } = route.params;
  // ...
}
```

**Key navigation methods:**

```tsx
navigation.navigate('ScreenName');           // Go to screen (won't duplicate if already in stack)
navigation.push('ScreenName');               // Push new instance (can duplicate)
navigation.goBack();                         // Go back one screen
navigation.reset({                           // Reset entire navigation state
  index: 0,
  routes: [{ name: 'Home' }],
});
navigation.replace('ScreenName');            // Replace current screen
navigation.setOptions({ title: 'New Title' }); // Update header
```

**Tab Navigator (Bottom Tabs) -- as STS implements it:**

```tsx
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName = 'home';
          if (route.name === 'Feed') iconName = focused ? 'home' : 'home-outline';
          if (route.name === 'Profile') iconName = focused ? 'person' : 'person-outline';
          return <Icon name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#00AEFF',
        tabBarInactiveTintColor: '#999',
      })}
    >
      <Tab.Screen name="Feed" component={FeedScreen} />
      <Tab.Screen name="Discover" component={DiscoverScreen} />
      <Tab.Screen name="Activity" component={ActivityScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
    </Tab.Navigator>
  );
}
```

**Nesting Navigators (Stack wrapping Tabs -- the STS pattern):**

STS uses a single Stack that contains a Tab Navigator as one of its screens:

```tsx
// This is exactly how STS structures navigation
function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        {/* Auth screens at the top level */}
        <Stack.Screen name="Splash" component={SplashScreen} />
        <Stack.Screen name="Welcome" component={WelcomeScreen} />
        <Stack.Screen name="Login" component={LoginScreen} />
        <Stack.Screen name="SignUp" component={SignUpScreen} />

        {/* Tab navigator is a screen within the stack */}
        <Stack.Screen
          name="MainTabs"
          component={MainTabs}
          options={{ headerShown: false }}
        />

        {/* Detail screens accessible from any tab */}
        <Stack.Screen name="FeedDetail" component={FeedDetailScreen} />
        <Stack.Screen name="VideoPlayer" component={VideoPlayerScreen} />
        <Stack.Screen name="Quiz" component={QuizScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

This means you can navigate from any tab to any detail screen, and the stack handles the back button automatically.

### Option B: Expo Router (File-Based, Declarative)

Expo Router uses your file system as the navigation structure, like Next.js.

```bash
npx create-expo-app@latest   # Comes pre-installed
```

**File structure IS the navigation:**

```
app/
├── _layout.tsx              ← Root layout (navigation container)
├── index.tsx                ← Home screen (route: /)
├── login.tsx                ← Login screen (route: /login)
├── (auth)/                  ← Group (doesn't create a URL segment)
│   ├── _layout.tsx          ← Auth layout
│   ├── sign-up.tsx          ← /sign-up
│   └── forgot-password.tsx  ← /forgot-password
├── (tabs)/                  ← Tab group
│   ├── _layout.tsx          ← Tab layout (defines the tab bar)
│   ├── feed.tsx             ← /feed (tab)
│   ├── discover.tsx         ← /discover (tab)
│   ├── activity.tsx         ← /activity (tab)
│   └── profile.tsx          ← /profile (tab)
└── feed/
    └── [id].tsx             ← /feed/123 (dynamic route)
```

**Root layout:**

```tsx
// app/_layout.tsx
import { Stack } from 'expo-router';

export default function RootLayout() {
  return (
    <Stack>
      <Stack.Screen name="index" options={{ headerShown: false }} />
      <Stack.Screen name="login" options={{ title: '' }} />
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
      <Stack.Screen name="feed/[id]" options={{ title: '' }} />
    </Stack>
  );
}
```

**Tab layout:**

```tsx
// app/(tabs)/_layout.tsx
import { Tabs } from 'expo-router';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen name="feed" options={{ title: 'Feed', tabBarIcon: /* ... */ }} />
      <Tabs.Screen name="discover" options={{ title: 'Discover' }} />
      <Tabs.Screen name="activity" options={{ title: 'Activity' }} />
      <Tabs.Screen name="profile" options={{ title: 'Profile' }} />
    </Tabs>
  );
}
```

**Navigating:**

```tsx
import { Link, router } from 'expo-router';

// Declarative (like web <a> tags)
<Link href="/login">Go to Login</Link>
<Link href="/feed/42">View Feed #42</Link>

// Programmatic
router.push('/login');
router.push('/feed/42');
router.replace('/home');     // Replace current screen
router.back();               // Go back
```

**Dynamic routes:**

```tsx
// app/feed/[id].tsx
import { useLocalSearchParams } from 'expo-router';

export default function FeedDetail() {
  const { id } = useLocalSearchParams<{ id: string }>();
  // id = "42" if navigated to /feed/42
  return <Text>Feed #{id}</Text>;
}
```

### React Navigation vs. Expo Router -- When to Use Which

| | React Navigation | Expo Router |
|---|---|---|
| Setup | Manual screen registration | Automatic from file structure |
| Deep linking | Manual configuration | Automatic (every file has a URL) |
| Type safety | Manual typing | Auto-generated route types |
| Learning curve | Medium | Lower (if you know Next.js) |
| RN CLI support | Full | Requires Expo |
| Flexibility | Maximum | Slightly opinionated |
| Maturity | 7+ years | ~3 years, stable since SDK 50 |

---

## 12. State Management -- From useState to Redux to Zustand

### Level 1: Local State (useState)

For state that lives in one component:

```tsx
const [isVisible, setIsVisible] = useState(false);
```

### Level 2: Shared State (Context + useContext)

For state shared across a subtree without prop drilling:

```tsx
// Create context
const AuthContext = createContext<AuthState | null>(null);

// Provider (wraps app)
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);

  const login = async (email, password) => {
    const response = await api.post('/login', { email, password });
    setUser(response.data.user);
    setToken(response.data.token);
  };

  return (
    <AuthContext.Provider value={{ user, token, login }}>
      {children}
    </AuthContext.Provider>
  );
}

// Consumer (any nested component)
function ProfileScreen() {
  const { user } = useContext(AuthContext);
  return <Text>Hello, {user.name}</Text>;
}
```

### Level 3: Redux (What STS Uses)

Redux is a centralized state container. STS uses it for **everything** -- auth, feeds, challenges, loading states, alerts.

**How STS wires Redux (the old way):**

```javascript
// From STS: src/reducers/index.js
import { combineReducers, createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import redState from './storeState';
import dashboardState from './dashboardState';

export default () => {
  const rootReducer = combineReducers({
    redState: redState,
    dashboardState: dashboardState
  });
  return createStore(rootReducer, applyMiddleware(thunk));
};

// From STS: src/index.js (root component)
import {Provider} from 'react-redux';
import createStore from '@reducers';
const store = createStore();

<Provider store={store}>
  <AppContainer />
</Provider>
```

**How STS connects components to Redux:**

```javascript
// From STS: Every screen uses this pattern
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

class LoginScreen extends React.Component {
  render() {
    // Access state via this.props.userData
    // Dispatch actions via this.props.showLoading(true)
  }
}

function mapStateToProps(state) {
  return {
    userData: state.redState.userData,
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(ActionCreators, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(LoginScreen);
```

**The modern Redux way (Redux Toolkit):**

```tsx
// store.ts
import { configureStore } from '@reduxjs/toolkit';
import feedReducer from './slices/feedSlice';
import authReducer from './slices/authSlice';

export const store = configureStore({
  reducer: {
    feed: feedReducer,
    auth: authReducer,
  },
});

// feedSlice.ts
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchFeeds = createAsyncThunk('feed/fetch', async (page: number) => {
  const response = await api.get(`/feed/list?page=${page}`);
  return response.data;
});

const feedSlice = createSlice({
  name: 'feed',
  initialState: { items: [], loading: false },
  reducers: {
    toggleLike: (state, action) => {
      const feed = state.items.find(f => f.id === action.payload);
      if (feed) feed.is_liked = feed.is_liked ? 0 : 1;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchFeeds.pending, (state) => { state.loading = true; })
      .addCase(fetchFeeds.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      });
  },
});

// In components (functional):
import { useSelector, useDispatch } from 'react-redux';

function FeedScreen() {
  const feeds = useSelector(state => state.feed.items);
  const loading = useSelector(state => state.feed.loading);
  const dispatch = useDispatch();

  useEffect(() => { dispatch(fetchFeeds(1)); }, []);
  // No more connect(), mapStateToProps, mapDispatchToProps
}
```

### Level 4: Zustand (Simpler Alternative)

If Redux feels like too much ceremony:

```tsx
import { create } from 'zustand';

const useAuthStore = create((set) => ({
  user: null,
  token: null,
  login: async (email, password) => {
    const response = await api.post('/login', { email, password });
    set({ user: response.data.user, token: response.data.token });
  },
  logout: () => set({ user: null, token: null }),
}));

// Usage (no Provider needed!)
function ProfileScreen() {
  const user = useAuthStore(state => state.user);
  const logout = useAuthStore(state => state.logout);

  return (
    <View>
      <Text>{user.name}</Text>
      <Button title="Logout" onPress={logout} />
    </View>
  );
}
```

### When to Use What

| Scope | Solution | Example |
|-------|----------|---------|
| One component | `useState` | Form field values, toggle visibility |
| Parent-child (2-3 levels) | Props | Pass handler down to a button |
| Subtree (auth, theme) | `useContext` | Current user, dark mode |
| Global, complex | Redux Toolkit | Feed list, notifications, rewards (like STS) |
| Global, simple | Zustand | Auth state, UI preferences |
| Server data | TanStack Query | API responses with caching + refetching |

---

## 13. Talking to APIs

### Axios (What STS Uses)

```tsx
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://dashboard.steamthestreets.org/api/v1/',
  headers: { 'Content-Type': 'application/json' },
});

// Interceptor: Attach token to every request
api.interceptors.request.use((config) => {
  const token = getStoredToken(); // from AsyncStorage
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

// Interceptor: Handle 401 globally (replaces STS's navigation-in-API pattern)
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearToken();
      // Signal auth expiry to the app (e.g., via Zustand or event emitter)
    }
    return Promise.reject(error);
  }
);

// Usage
const response = await api.get('/feed/list', { params: { page: 1 } });
const loginResponse = await api.post('/login', { email, password });
```

### The fetch API (Built-in Alternative)

```tsx
const response = await fetch('https://api.example.com/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json', Authorization: `Bearer ${token}` },
  body: JSON.stringify({ email, password }),
});
const data = await response.json();
```

### TanStack Query (Modern Server State)

Instead of manually managing loading/error/data states:

```tsx
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

function FeedScreen() {
  // Automatic loading/error/data/refetch/caching
  const { data: feeds, isLoading, error, refetch } = useQuery({
    queryKey: ['feeds', page],
    queryFn: () => api.get(`/feed/list?page=${page}`).then(r => r.data),
  });

  // Mutation with cache invalidation
  const queryClient = useQueryClient();
  const likeMutation = useMutation({
    mutationFn: (feedId) => api.post('/feed/likeunlike', { id: feedId }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['feeds'] }),
  });

  if (isLoading) return <ActivityIndicator />;
  return (
    <FlatList
      data={feeds}
      renderItem={({ item }) => (
        <FeedCard item={item} onLike={() => likeMutation.mutate(item.id)} />
      )}
      refreshing={isLoading}
      onRefresh={refetch}
    />
  );
}
```

TanStack Query replaces the entire "dispatch action → loading state → success/error" pattern that STS repeats in every action creator.

---

## 14. Local Storage -- AsyncStorage and Beyond

### AsyncStorage (Key-Value Store)

Like `localStorage` on the web, but asynchronous.

```bash
npm install @react-native-async-storage/async-storage
```

```tsx
import AsyncStorage from '@react-native-async-storage/async-storage';

// Store a value
await AsyncStorage.setItem('access_token', 'eyJhbGciOiJIUzI...');

// Read a value
const token = await AsyncStorage.getItem('access_token');

// Store an object (must stringify)
await AsyncStorage.setItem('user', JSON.stringify({ id: 1, name: 'Alex' }));
const user = JSON.parse(await AsyncStorage.getItem('user'));

// Remove
await AsyncStorage.removeItem('access_token');

// Multi-operations (what STS uses)
await AsyncStorage.multiSet([
  ['isLogin', 'true'],
  ['user_data', JSON.stringify(userData)],
  ['access_token', token],
]);

const values = await AsyncStorage.multiGet(['isLogin', 'user_data', 'access_token']);
// values = [['isLogin', 'true'], ['user_data', '{"id":1}'], ['access_token', 'eyJ...']]
```

**STS wraps AsyncStorage in a helper:**

```javascript
// From STS: src/storage/asyncStorage.js (conceptual)
export const StorageOperation = {
  setData: (data) => AsyncStorage.multiSet(data),
  getData: (keys) => AsyncStorage.multiGet(keys),
  removeData: (keys) => AsyncStorage.multiRemove(keys),
};
```

### Secure Storage (For Tokens and Secrets)

AsyncStorage is **not encrypted**. For sensitive data (tokens, passwords), use:

```bash
# Expo
npx expo install expo-secure-store

# RN CLI
npm install react-native-keychain
```

```tsx
// Expo
import * as SecureStore from 'expo-secure-store';
await SecureStore.setItemAsync('access_token', token);
const token = await SecureStore.getItemAsync('access_token');

// RN CLI
import * as Keychain from 'react-native-keychain';
await Keychain.setGenericPassword('user', token);
const credentials = await Keychain.getGenericPassword();
```

---

# Part III -- The Platform

---

## 15. The Bridge, JSI, and How JS Talks to Native

### The Old Architecture (Bridge)

In RN 0.65 (what STS uses), JS and Native communicate through a **Bridge**:

```
JS Thread  ←── JSON serialization ──→  Native Thread
             (asynchronous only)
```

Every call from JS to Native (and back) serializes data to JSON, sends it across the bridge, and deserializes on the other side. This is slow for frequent updates like animations.

### The New Architecture (JSI + Fabric + Turbo Modules)

In RN 0.74+ (the rebuild target), the Bridge is replaced by **JSI** (JavaScript Interface):

```
JS Thread  ←── C++ direct calls ──→  Native Thread
             (synchronous possible)
```

- **JSI**: JS can hold references to C++ objects and call native methods directly.
- **Fabric**: New renderer that can measure and render views synchronously.
- **Turbo Modules**: Native modules that are lazy-loaded and type-safe.

You don't interact with JSI directly. It's the plumbing. What it means for you: **faster apps, no JSON serialization bottleneck, synchronous layout calculations**.

### Hermes Engine

Hermes is the JS engine that replaced JavaScriptCore. Key difference: Hermes **precompiles** your JS to bytecode at build time. Users don't pay the cost of parsing JavaScript on every app launch.

---

## 16. The Build Pipeline -- Metro, Gradle, Xcode

### Metro Bundler

Metro is React Native's bundler (like Webpack for the web). It:
1. Resolves imports starting from `index.js`
2. Transforms code via Babel (JSX → JS, TypeScript → JS)
3. Bundles everything into a single JS file
4. Serves it to the app in dev mode (hot reload), or embeds it in the binary for production

```bash
# Start Metro dev server
npx react-native start        # RN CLI
npx expo start                 # Expo

# Key commands in the Metro terminal:
# r → Reload app
# d → Open dev menu
# j → Open debugger (React Native DevTools)
```

### Android Build (Gradle)

Gradle is the Android build system. It compiles your Java/Kotlin native code, links native libraries, packages the JS bundle, and produces an APK or AAB.

```bash
# Debug build (for development)
npx react-native run-android

# Release build (for store)
cd android && ./gradlew bundleRelease
```

Key files:
- `android/build.gradle` -- Root config (Gradle version, SDKs)
- `android/app/build.gradle` -- App config (package name, versions, signing, dependencies)
- `android/gradle.properties` -- Feature flags (`newArchEnabled=true`, `hermesEnabled=true`)

### iOS Build (Xcode)

Xcode compiles Objective-C/Swift, links CocoaPods, packages the JS bundle, and produces an IPA.

```bash
# Via EAS (from Linux)
eas build --platform ios

# Via Xcode (on Mac)
npx react-native run-ios
```

Key files:
- `ios/Podfile` -- CocoaPods dependencies (like `package.json` for iOS native libs)
- `ios/MyApp/Info.plist` -- App metadata, permissions, URL schemes
- `ios/MyApp/AppDelegate.mm` -- App entry point (native side)

---

## 17. Platform-Specific Code

Sometimes you need different behavior on iOS vs. Android.

### Platform Module

```tsx
import { Platform } from 'react-native';

// Conditional values
const styles = StyleSheet.create({
  container: {
    paddingTop: Platform.OS === 'ios' ? 44 : 0,
    ...Platform.select({
      ios: { shadowColor: '#000', shadowOffset: { width: 0, height: 2 }, shadowOpacity: 0.1 },
      android: { elevation: 4 },
    }),
  },
});

// Conditional logic
if (Platform.OS === 'android') {
  // Android-specific setup
}

// Version checks
if (Platform.OS === 'android' && Platform.Version >= 33) {
  // Android 13+ needs POST_NOTIFICATIONS permission
}
```

### Platform-Specific Files

Create separate files with `.ios.` or `.android.` extensions:

```
components/
├── VideoPlayer.ios.tsx      ← Used on iOS
├── VideoPlayer.android.tsx  ← Used on Android
```

When you `import VideoPlayer from './VideoPlayer'`, Metro automatically picks the right file.

---

## 18. Permissions

Mobile apps need explicit user permission for camera, location, notifications, etc.

### Expo Way

```bash
npx expo install expo-camera
```

```tsx
import { Camera } from 'expo-camera';

const [permission, requestPermission] = Camera.useCameraPermissions();

if (!permission?.granted) {
  return <Button title="Grant Camera Access" onPress={requestPermission} />;
}
```

### RN CLI Way

```bash
npm install react-native-permissions
```

```tsx
import { request, PERMISSIONS, RESULTS } from 'react-native-permissions';

const result = await request(
  Platform.OS === 'ios'
    ? PERMISSIONS.IOS.CAMERA
    : PERMISSIONS.ANDROID.CAMERA
);

if (result === RESULTS.GRANTED) {
  // Permission granted
}
```

Permissions must also be declared in native config:
- **Android**: `AndroidManifest.xml` (`<uses-permission android:name="android.permission.CAMERA" />`)
- **iOS**: `Info.plist` (`NSCameraUsageDescription` with a user-facing message)

---

## 19. Push Notifications

Push notifications are one of the most complex features in mobile dev. Here's the full picture.

### The Flow

```
Your Backend → Firebase Cloud Messaging (FCM) → Apple/Google Push Service → User's Device
```

1. App starts → requests notification permission from user.
2. App gets a **device token** (FCM token) from Firebase.
3. App sends this token to your backend.
4. When your backend wants to notify a user, it sends a message to FCM with the device token.
5. FCM delivers it to the device.
6. The app handles it (foreground notification, background task, or tap action).

### Expo Implementation

```bash
npx expo install expo-notifications expo-device
```

```tsx
import * as Notifications from 'expo-notifications';
import * as Device from 'expo-device';

// Request permission + get token
async function registerForPushNotifications() {
  if (!Device.isDevice) return; // Must be a real device

  const { status } = await Notifications.requestPermissionsAsync();
  if (status !== 'granted') return;

  const token = (await Notifications.getExpoPushTokenAsync()).data;
  // Send token to your backend
  await api.post('/user_token', { token });
}

// Handle received notifications
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: true,
    shouldSetBadge: true,
  }),
});

// Listen for notification taps
const subscription = Notifications.addNotificationResponseReceivedListener(response => {
  const data = response.notification.request.content.data;
  // Navigate based on notification data
  if (data.feedId) router.push(`/feed/${data.feedId}`);
});
```

### RN CLI Implementation (What STS Needs to Migrate To)

STS currently uses `@react-native-firebase/messaging` + `react-native-push-notification`. The rebuild should use `@react-native-firebase/messaging` + `@notifee/react-native`:

```tsx
import messaging from '@react-native-firebase/messaging';
import notifee from '@notifee/react-native';

// Request permission
await messaging().requestPermission();

// Get FCM token
const token = await messaging().getToken();
await api.post('/user_token', { token });

// Foreground notification display
messaging().onMessage(async (remoteMessage) => {
  await notifee.displayNotification({
    title: remoteMessage.notification?.title,
    body: remoteMessage.notification?.body,
    android: {
      channelId: 'default',
      pressAction: { id: 'default' },
    },
  });
});

// Background handler
messaging().setBackgroundMessageHandler(async (remoteMessage) => {
  // Handle silently or show notification
});
```

---

## 20. Deep Linking

Deep linking lets external URLs open specific screens in your app.

### The Concept

```
URL: steamthestreet://feed/42
                     ↓
App opens → navigates to FeedDetailScreen with id=42
```

### Configuration

**Expo Router**: Automatic. Every file in `app/` has a URL. `app/feed/[id].tsx` handles `myapp://feed/42`.

**React Navigation**: Manual configuration in the `NavigationContainer`:

```tsx
const linking = {
  prefixes: ['steamthestreet://', 'https://steamthestreets.org'],
  config: {
    screens: {
      MainTabs: {
        screens: {
          Feed: 'feed',
          Discover: 'discover',
        },
      },
      FeedDetail: 'feed/:id',
      ChallengeDetail: 'challenge/:id',
    },
  },
};

<NavigationContainer linking={linking}>
  {/* ... */}
</NavigationContainer>
```

STS uses deep linking for push notification handling -- when a notification contains a `challenge_id`, tapping it opens the challenge detail screen.

---

# Part IV -- Advanced

---

## 21. Performance -- What Makes RN Apps Slow and How to Fix It

### The Biggest Offenders

| Problem | Cause | Fix |
|---------|-------|-----|
| Slow list scrolling | Re-rendering every item on state change | `React.memo`, `useCallback`, `keyExtractor` |
| Laggy animations | Animations running on JS thread | Use `react-native-reanimated` (runs on UI thread) |
| Slow startup | Too many imports at launch | Lazy loading, code splitting |
| Memory bloat | Images not resized | Use `resizeMode`, cache images, use `expo-image` |
| Excessive re-renders | Entire subtree re-renders | `useMemo`, `useCallback`, selective context |

### Memoization

```tsx
// Memoize a list item so it only re-renders when its props change
const FeedCard = React.memo(({ item, onLike }) => {
  return (
    <View>
      <Text>{item.title}</Text>
      <Pressable onPress={() => onLike(item.id)}>
        <Text>Like</Text>
      </Pressable>
    </View>
  );
});

// Memoize the onLike callback so FeedCard doesn't re-render
function FeedList({ feeds }) {
  const onLike = useCallback((id) => {
    dispatch(toggleLike(id));
  }, [dispatch]);

  return (
    <FlatList
      data={feeds}
      renderItem={({ item }) => <FeedCard item={item} onLike={onLike} />}
      keyExtractor={item => item.id.toString()}
    />
  );
}
```

### FlatList Optimization Props

```tsx
<FlatList
  data={feeds}
  renderItem={renderItem}
  keyExtractor={keyExtractor}
  initialNumToRender={10}         // Render 10 items first
  maxToRenderPerBatch={10}        // Render 10 items per scroll batch
  windowSize={5}                  // Keep 5 screens worth of items in memory
  removeClippedSubviews={true}    // Remove offscreen items from native hierarchy
  getItemLayout={(data, index) => ({  // Skip measurement if fixed height
    length: ITEM_HEIGHT,
    offset: ITEM_HEIGHT * index,
    index,
  })}
/>
```

---

## 22. Animations -- Animated API, Reanimated, and Gesture Handler

### Built-in Animated API

```tsx
import { Animated } from 'react-native';

function FadeIn({ children }) {
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(opacity, {
      toValue: 1,
      duration: 500,
      useNativeDriver: true,  // Runs on native thread (smooth)
    }).start();
  }, []);

  return <Animated.View style={{ opacity }}>{children}</Animated.View>;
}
```

`useNativeDriver: true` is critical. It offloads the animation to the native thread so JS thread hiccups don't cause stuttering. Works for `opacity`, `transform` -- but NOT for layout properties like `width`, `height`, `margin`.

### React Native Reanimated (The Professional Choice)

For complex animations, `react-native-reanimated` v3 runs animations entirely on the UI thread using **worklets** (small JS functions compiled to run outside the JS thread):

```tsx
import Animated, { useSharedValue, useAnimatedStyle, withSpring } from 'react-native-reanimated';

function BouncyCard() {
  const scale = useSharedValue(1);

  const animatedStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
  }));

  return (
    <Animated.View style={[styles.card, animatedStyle]}>
      <Pressable
        onPressIn={() => { scale.value = withSpring(0.95); }}
        onPressOut={() => { scale.value = withSpring(1); }}
      >
        <Text>Tap me</Text>
      </Pressable>
    </Animated.View>
  );
}
```

### Gesture Handler

`react-native-gesture-handler` provides native-driven gesture recognition:

```tsx
import { GestureDetector, Gesture } from 'react-native-gesture-handler';
import Animated, { useSharedValue, useAnimatedStyle } from 'react-native-reanimated';

function Swipeable() {
  const translateX = useSharedValue(0);

  const pan = Gesture.Pan()
    .onUpdate((event) => {
      translateX.value = event.translationX;
    })
    .onEnd(() => {
      translateX.value = withSpring(0);  // Snap back
    });

  const style = useAnimatedStyle(() => ({
    transform: [{ translateX: translateX.value }],
  }));

  return (
    <GestureDetector gesture={pan}>
      <Animated.View style={style}>
        <Text>Swipe me</Text>
      </Animated.View>
    </GestureDetector>
  );
}
```

---

## 23. Native Modules -- When JS Is Not Enough

Sometimes you need functionality that doesn't exist in JavaScript -- Bluetooth, specific SDK integrations, hardware APIs.

### Using Existing Native Libraries

Most of the time, someone has already written a native module:

```bash
npm install react-native-ble-plx        # Bluetooth
npm install @react-native-camera-roll/camera-roll  # Photo gallery
npm install react-native-video           # Video player
```

These libraries include compiled native code (Java/Kotlin for Android, ObjC/Swift for iOS) that auto-links into your project.

### Writing Custom Native Modules (Turbo Modules)

If you need to write your own in the New Architecture:

```typescript
// specs/NativeMyModule.ts -- TypeScript spec
import type { TurboModule } from 'react-native';
import { TurboModuleRegistry } from 'react-native';

export interface Spec extends TurboModule {
  getDeviceId(): string;       // Synchronous!
  fetchData(url: string): Promise<string>;  // Async
}

export default TurboModuleRegistry.getEnforcing<Spec>('MyModule');
```

Then implement in Kotlin (Android) and Swift (iOS). Codegen generates the bridge code from your TypeScript spec.

---

## 24. Testing

### Unit Tests (Jest)

```tsx
// __tests__/utils.test.ts
import { isValidEmail } from '../src/utils/validations';

test('validates email correctly', () => {
  expect(isValidEmail('user@example.com')).toBe(true);
  expect(isValidEmail('not-an-email')).toBe(false);
  expect(isValidEmail('')).toBe(false);
});
```

### Component Tests (React Native Testing Library)

```tsx
import { render, fireEvent } from '@testing-library/react-native';
import LoginScreen from '../src/screens/LoginScreen';

test('shows error when email is empty', () => {
  const { getByText, getByPlaceholderText } = render(<LoginScreen />);

  fireEvent.press(getByText('Sign In'));

  expect(getByText('Please enter your email')).toBeTruthy();
});
```

### E2E Tests (Detox or Maestro)

```yaml
# Maestro (simple YAML-based E2E)
appId: com.steamthestreets.sts
---
- launchApp
- tapOn: "Sign In"
- tapOn: "Email"
- inputText: "user@example.com"
- tapOn: "Password"
- inputText: "password123"
- tapOn: "Sign In"
- assertVisible: "Feed"
```

---

## 25. Over-The-Air Updates

OTA updates let you push JS-only changes to users without going through app store review.

### With Expo (EAS Update)

```bash
# Push an update to production users
eas update --branch production --message "Fix login validation bug"
```

Users get the update next time they open the app. No App Store review, no Play Store review.

### With RN CLI (CodePush by Microsoft)

```bash
npm install react-native-code-push
appcenter codepush release-react -a MyOrg/MyApp-iOS -d Production
```

### What Can and Cannot Be Updated OTA

| Can Update | Cannot Update |
|-----------|--------------|
| JavaScript code | New native modules |
| Images bundled in JS | Native configuration |
| Styles, layouts | Permissions |
| Business logic | SDK version changes |
| Bug fixes | Splash screen |

---

## 26. Putting It All Together -- Reading the STS Codebase

Now that you have the fundamentals, here's how to read the STS codebase with understanding.

### The Data Flow (STS Pattern)

```
User taps "Sign In"
    ↓
LoginScreen.callLogin()                    // Class method
    ↓
this.props.showLoading(true)               // Redux action → sets isLoading = true → global spinner shows
    ↓
callApi([params], accessToken, navigation) // Axios call with batch support
    ↓
API responds with { success: true, data: { token, user, last_otp_verified } }
    ↓
Check last_otp_verified < 15 days?
    ├── YES → StorageOperation.setData([...]) → save to AsyncStorage
    │         → this.props.saveUserData({...}) → Redux dispatch
    │         → navigation.reset({ routes: [{ name: 'TAB_NAVIGATOR' }] })
    │
    └── NO  → navigation.navigate('MFA_OPTION_SCREEN', { accessToken, email, phone })
              → MFA flow → OTP → verify → then save user data → navigate to main app
```

### The Style System (STS Pattern)

```
COLORS.LIGHT_BLUE                          → '#00AEFF'
COMMON_STYLE.textStyle(16, COLORS.WHITE, "BOLD")  → { fontSize: calculated, fontFamily: 'Bold', color: '#fff' }
Responsive.getWidth(4)                     → 4% of screen width in pixels
Responsive.getHeight(10)                   → 10% of screen height in pixels
styles.signupBtnStyle                      → Local component-specific styles
```

### The Redux Pattern (STS Pattern)

```
Screen dispatches action → Action calls API → On success, dispatches reducer type → Reducer updates state → Screen re-renders

Screen           Action Creator        Reducer
------           ---------------       --------
this.props       saveFeedList()        case RED_TYPE.FEED_LIST:
.saveFeedList()  → callApi()             return {...state, feedList: action.data}
                 → dispatch({ type })
```

### What Each `connect()` Does

Every STS screen ends with:

```javascript
function mapStateToProps(state) {
  return {
    userData: state.redState.userData,           // User info + token
    feedList: state.dashboardState.feedList,     // Feed data
  };
}

function mapDispatchToProps(dispatch) {
  return bindActionCreators(ActionCreators, dispatch);  // All actions as props
}

export default connect(mapStateToProps, mapDispatchToProps)(ScreenName);
```

This injects Redux state as `this.props.userData` and Redux actions as `this.props.saveFeedList()`, `this.props.showLoading()`, etc.

In the rebuild with hooks, this becomes:

```tsx
function ScreenName() {
  const userData = useSelector(state => state.auth.user);
  const dispatch = useDispatch();
  // or with Zustand: const userData = useAuthStore(state => state.user);
}
```

### Quick Reference: STS File → What It Does

| When you open... | You're looking at... |
|---------|---------|
| `src/index.js` | App bootstrap: Redux Provider, SafeArea, global overlays |
| `src/navigator/stackNavigator.js` | Every screen registration and header config |
| `src/navigator/TabNavigator.js` | Bottom tab bar (Feed, Discover, Activity, Profile) |
| `src/screens/*/index.js` | A screen component (class-based, Redux-connected) |
| `src/screens/*/style.js` | That screen's StyleSheet |
| `src/actions/dashboardAction.js` | API calls + Redux dispatches for features |
| `src/reducers/storeState.js` | App-wide state shape + reducer logic |
| `src/reducers/dashboardState.js` | Feature state shape + reducer logic |
| `src/apiCalls/callApiClass.js` | Core API calling mechanism (axios.all) |
| `src/constants/apiData.js` | Every API endpoint URL |
| `src/services/firebaseServices.js` | Push notification setup |
| `src/themes/colors.js` | Color palette |
| `src/themes/commonStyles.js` | Shared style utility functions |
| `src/helpers/responsive.js` | Screen-size-relative sizing utilities |
| `src/components/views/*.js` | Reusable list cells (FeedCell, DiscoverCell, etc.) |
| `src/components/modalComponents/*.js` | Modal dialogs (alerts, rewards, badges) |

---

> **By Friday**: You've read this document. You understand how React Native renders native views, how navigation works (both React Navigation and Expo Router), how state flows through Redux (the old way) and hooks (the new way), how styling works without CSS, how the STS codebase is structured, and what every major pattern does. You're ready to start making architectural decisions for the rebuild.
