# STS Mobile App — Skills Development Guide

> **Goal**: You know JS/TS. You know nothing about cross-platform mobile dev. By Monday, you will understand every tool in the STS stack well enough to read the existing codebase and write production code for the rebuild. This document is your curriculum.

---

## Table of Contents

1. [The Big Picture — How a React Native App Works](#1-the-big-picture)
2. [React Native Core — The Primitives](#2-react-native-core)
3. [Navigation — React Navigation](#3-navigation--react-navigation)
4. [State Management — Redux / Redux Toolkit](#4-state-management--redux--redux-toolkit)
5. [API Fetching — Axios](#5-api-fetching--axios)
6. [Local Storage — AsyncStorage](#6-local-storage--asyncstorage)
7. [Firebase — Auth, Messaging, Notifications](#7-firebase--auth-messaging-notifications)
8. [Notifications — @notifee/react-native](#8-notifications--notifee)
9. [UI Toolkit — React Native Elements / RNEUI](#9-ui-toolkit--react-native-elements)
10. [Icons — react-native-vector-icons](#10-icons--react-native-vector-icons)
11. [Forms & Input Masking — react-native-mask-input](#11-forms--input-masking)
12. [Media — Video, YouTube, Sound](#12-media--video-youtube-sound)
13. [Animations — Lottie](#13-animations--lottie)
14. [Layout Components — Carousels, Tabs, Pagers](#14-layout-components)
15. [Permissions — react-native-permissions](#15-permissions)
16. [Networking Info — NetInfo](#16-networking-info--netinfo)
17. [Date Handling — Moment → Day.js](#17-date-handling)
18. [Internationalization — i18n](#18-internationalization)
19. [WebView](#19-webview)
20. [Native Build System — Android & iOS](#20-native-build-system)
21. [The Mental Model — How Everything Connects](#21-the-mental-model)

---

## 1. The Big Picture

### What is React Native?

React Native lets you write mobile apps (Android + iOS) using React. Instead of rendering to the DOM (`<div>`, `<span>`), you render to **native platform views** (`<View>`, `<Text>`).

```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR JAVASCRIPT CODE                      │
│         (React components, business logic, state)            │
├─────────────────────────────────────────────────────────────┤
│                     REACT NATIVE BRIDGE                      │
│          (Serializes JS calls → Native calls)                │
│     ┌──────────────────────────────────────────────┐         │
│     │  New Architecture: JSI (direct C++ binding)  │         │
│     │  No more bridge serialization overhead        │         │
│     └──────────────────────────────────────────────┘         │
├──────────────────────┬──────────────────────────────────────┤
│   ANDROID (Java/Kt)  │           iOS (ObjC/Swift)           │
│   Real Android Views  │           Real UIKit Views           │
│   Google Play Store   │           App Store                  │
└──────────────────────┴──────────────────────────────────────┘
```

### Key Differences from Web React

| Web React | React Native |
|-----------|-------------|
| `<div>` | `<View>` |
| `<span>`, `<p>` | `<Text>` (all text MUST be inside `<Text>`) |
| `<img>` | `<Image>` |
| `<input>` | `<TextInput>` |
| `<ul>` + `<li>` | `<FlatList>` or `<ScrollView>` |
| CSS files | `StyleSheet.create({})` (JS objects, no cascading) |
| `onClick` | `onPress` |
| `window.localStorage` | `AsyncStorage` (async!) |
| `fetch()` / `axios` | Same! `axios` works identically |
| React Router | React Navigation (completely different API) |
| `yarn start` → browser | `npx react-native run-android` → phone/emulator |

### The STS App Architecture at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│                         index.js                             │
│                   AppRegistry.registerComponent              │
└──────────────────────────┬──────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────┐
│                       src/index.js                           │
│  ┌─────────┐  ┌──────────────┐  ┌──────────────────────┐    │
│  │ Redux   │  │ SafeArea     │  │ Global Overlays      │    │
│  │ Provider │  │ Provider     │  │ (Loading, Alert,     │    │
│  │         │  │              │  │  Toast)              │    │
│  └────┬────┘  └──────┬───────┘  └──────────────────────┘    │
│       │              │                                       │
│  ┌────▼──────────────▼───────────────────────────────────┐  │
│  │              Navigation Container                      │  │
│  │  ┌─────────────────────────────────────────────────┐   │  │
│  │  │            Stack Navigator                       │   │  │
│  │  │  Splash → Welcome → Login → MFA → OTP           │   │  │
│  │  │          ↓                                       │   │  │
│  │  │  ┌──────────────────────────────────────────┐    │   │  │
│  │  │  │        Tab Navigator (Bottom Tabs)       │    │   │  │
│  │  │  │  Feed | Discover | Activity | Profile    │    │   │  │
│  │  │  └──────────────────────────────────────────┘    │   │  │
│  │  │          ↓                                       │   │  │
│  │  │  Detail Screens, Quiz, Video, Settings...        │   │  │
│  │  └─────────────────────────────────────────────────┘   │  │
│  └────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. React Native Core

### The 6 Primitives You'll Use Constantly

These are your building blocks. Everything in RN is built from these:

#### `<View>` — The `<div>` of Mobile

```jsx
import { View, StyleSheet } from 'react-native';

// A View is a container. It doesn't render anything visible by itself.
const Card = () => (
  <View style={styles.card}>
    <View style={styles.cardHeader}>
      {/* ... */}
    </View>
    <View style={styles.cardBody}>
      {/* ... */}
    </View>
  </View>
);

const styles = StyleSheet.create({
  card: {
    backgroundColor: '#fff',
    borderRadius: 12,
    padding: 16,
    // Shadow (iOS)
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Shadow (Android)
    elevation: 3,
  },
  cardHeader: {
    flexDirection: 'row',       // horizontal layout (default is 'column')
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  cardBody: {
    marginTop: 12,
  },
});
```

**STS Usage**: Every single screen and component uses `<View>`. The entire layout is View-based.

#### `<Text>` — All Text Must Live Here

```jsx
import { Text, StyleSheet } from 'react-native';

// CRITICAL: In RN, all text MUST be inside a <Text> component.
// Bare text outside <Text> will crash the app.

const Title = ({ children }) => (
  <Text style={styles.title}>{children}</Text>
);

// Nesting text inherits parent styles (like CSS)
const RichText = () => (
  <Text style={styles.base}>
    Hello <Text style={styles.bold}>World</Text>
  </Text>
);

const styles = StyleSheet.create({
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#1E2A3A',
    fontFamily: 'CooperHewitt-Bold',  // custom fonts must be linked in native config
  },
  base: { fontSize: 16, color: '#333' },
  bold: { fontWeight: 'bold' },       // inherits fontSize and color from parent
});
```

**STS Usage**: The codebase uses custom fonts (CooperHewitt) and a helper `COMMON_STYLE.textStyle(size, color, weight, align)` to generate text styles.

#### `<TextInput>` — Form Inputs

```jsx
import { TextInput, StyleSheet } from 'react-native';

const EmailInput = () => {
  const [email, setEmail] = useState('');

  return (
    <TextInput
      style={styles.input}
      value={email}
      onChangeText={setEmail}          // NOT onChange! This gives you the string directly
      placeholder="Enter email"
      placeholderTextColor="#999"
      keyboardType="email-address"      // Shows @ on keyboard
      autoCapitalize="none"
      autoCorrect={false}
      returnKeyType="next"              // Shows "Next" on keyboard
      onSubmitEditing={() => {/* focus next input */}}
    />
  );
};

// Password input
<TextInput
  secureTextEntry={true}               // Hides characters
  textContentType="password"           // iOS autofill
/>

// Multiline
<TextInput
  multiline={true}
  numberOfLines={4}
  textAlignVertical="top"              // Android: text starts at top
/>
```

**STS Usage**: Login, signup, OTP, profile edit, search — every form screen uses TextInput heavily.

#### `<Image>` — Images

```jsx
import { Image, StyleSheet } from 'react-native';

// Local image (bundled with app)
<Image source={require('./assets/logo.png')} style={styles.logo} />

// Remote image (from URL) — MUST specify width & height
<Image
  source={{ uri: 'https://example.com/avatar.jpg' }}
  style={{ width: 100, height: 100, borderRadius: 50 }}
  resizeMode="cover"    // 'cover' | 'contain' | 'stretch' | 'center'
/>

// Image as background
import { ImageBackground } from 'react-native';
<ImageBackground source={require('./bg.jpg')} style={styles.bg}>
  <Text>Content on top of image</Text>
</ImageBackground>
```

**STS Usage**: Feed posts, avatars, challenge thumbnails, tab icons — images everywhere.

#### `<ScrollView>` vs `<FlatList>` — Scrolling

```jsx
import { ScrollView, FlatList, RefreshControl } from 'react-native';

// ScrollView — for SHORT, fixed content (renders everything at once)
<ScrollView>
  <Text>All content renders immediately</Text>
  <Text>Bad for long lists (renders ALL items = memory hog)</Text>
</ScrollView>

// FlatList — for LONG, dynamic lists (virtualizes = only renders visible items)
const FeedList = ({ posts }) => (
  <FlatList
    data={posts}                                    // Array of items
    keyExtractor={(item) => item.id.toString()}      // Unique key
    renderItem={({ item }) => <FeedCard post={item} />}  // Render function

    // Pull to refresh
    refreshControl={
      <RefreshControl
        refreshing={refreshing}
        onRefresh={handleRefresh}
      />
    }

    // Infinite scroll (pagination)
    onEndReached={loadMore}           // Called when near bottom
    onEndReachedThreshold={0.5}       // Trigger at 50% from bottom
    ListFooterComponent={loading ? <Spinner /> : null}

    // Empty state
    ListEmptyComponent={<EmptyState message="No posts yet" />}

    // Header
    ListHeaderComponent={<FeedHeader />}
  />
);
```

**STS Usage**: `FeedHomeScreen` uses FlatList with pull-to-refresh and infinite scroll. `DiscoverHomeScreen` uses FlatList for challenge cards. Nearly every screen with lists uses FlatList.

#### `<TouchableOpacity>` / `<Pressable>` — Buttons

```jsx
import { TouchableOpacity, Pressable } from 'react-native';

// TouchableOpacity — dims opacity on press (the classic RN button)
<TouchableOpacity
  onPress={() => handlePress()}
  activeOpacity={0.7}                  // How dim on press (0-1)
  disabled={isLoading}
>
  <Text>Press Me</Text>
</TouchableOpacity>

// Pressable — more control (newer API, recommended)
<Pressable
  onPress={handlePress}
  onLongPress={handleLongPress}
  style={({ pressed }) => [
    styles.button,
    pressed && styles.buttonPressed,   // Dynamic style based on press state
  ]}
>
  {({ pressed }) => (
    <Text style={pressed ? styles.textPressed : styles.text}>
      {pressed ? 'Pressing...' : 'Press Me'}
    </Text>
  )}
</Pressable>
```

**STS Usage**: The codebase primarily uses `TouchableOpacity` and RN Elements' `<Button>`. The rebuild should prefer `<Pressable>`.

### StyleSheet — How Styling Works in RN

```
┌──────────────────────────────────────────────────────────┐
│                    WEB CSS vs RN STYLES                    │
├──────────────────────────┬───────────────────────────────┤
│        WEB CSS           │      REACT NATIVE             │
├──────────────────────────┼───────────────────────────────┤
│ .card {                  │ card: {                       │
│   background-color: #fff;│   backgroundColor: '#fff',    │  ← camelCase
│   border-radius: 12px;  │   borderRadius: 12,           │  ← no units (dp)
│   padding: 16px;        │   padding: 16,                │
│   margin: 0 auto;       │   alignSelf: 'center',        │  ← no shorthand
│   display: flex;         │   // flexbox is DEFAULT       │
│   flex-direction: column;│   flexDirection: 'column',    │  ← already default
│ }                        │ }                             │
├──────────────────────────┼───────────────────────────────┤
│ Cascading (parent→child) │ NO cascading (except Text)    │
│ Global selectors         │ NO selectors (explicit only)  │
│ Media queries            │ Dimensions API / useWindow... │
│ Hover states             │ No hover (touch only)         │
│ CSS Grid                 │ NO Grid (Flexbox only)        │
└──────────────────────────┴───────────────────────────────┘
```

```jsx
import { StyleSheet, Dimensions } from 'react-native';

const { width, height } = Dimensions.get('window');

const styles = StyleSheet.create({
  // Flexbox is the ONLY layout system
  container: {
    flex: 1,                     // Take all available space
    flexDirection: 'column',     // Default (vertical). 'row' for horizontal
    justifyContent: 'center',    // Main axis alignment
    alignItems: 'center',        // Cross axis alignment
    padding: 20,
  },

  // Responsive sizing
  card: {
    width: width * 0.9,          // 90% of screen width
    // OR use the STS pattern:
    // width: Responsive.getWidth(90),
  },

  // Multiple styles on one component
  // <View style={[styles.base, styles.active, { opacity: 0.5 }]}>
});
```

**STS Usage**: The project has a custom `Responsive` helper (`src/helpers/responsive.js`) that converts percentage-based values to pixel dimensions. All styling goes through `COMMON_STYLE` helpers and `COLORS` constants in `src/themes/`.

---

## 3. Navigation — React Navigation

> **What it does**: React Navigation is the routing library for React Native. It controls which screen the user sees and how they move between screens. Think of it as React Router, but completely different.

### Installation (in the rebuild)

```bash
yarn add @react-navigation/native @react-navigation/stack @react-navigation/bottom-tabs
yarn add react-native-screens react-native-safe-area-context
yarn add react-native-gesture-handler
```

### Core Concepts

```
┌─────────────────────────────────────────────────────────────────┐
│                    NAVIGATION ARCHITECTURE                       │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              NavigationContainer                          │   │
│  │  (The root — wraps your entire navigation tree)           │   │
│  │                                                           │   │
│  │  ┌────────────────────────────────────────────────────┐   │   │
│  │  │           Stack Navigator                           │   │   │
│  │  │  (Screens slide in from right, like a card deck)    │   │   │
│  │  │                                                     │   │   │
│  │  │  ┌──────┐ → ┌──────┐ → ┌──────┐                   │   │   │
│  │  │  │Login │   │ MFA  │   │ OTP  │                    │   │   │
│  │  │  └──────┘   └──────┘   └──────┘                    │   │   │
│  │  │                ↓                                    │   │   │
│  │  │  ┌──────────────────────────────────────────────┐   │   │   │
│  │  │  │        Tab Navigator (Bottom Tabs)           │   │   │   │
│  │  │  │  ┌──────┬──────────┬──────────┬─────────┐    │   │   │   │
│  │  │  │  │ Feed │ Discover │ Activity │ Profile │    │   │   │   │
│  │  │  │  └──────┴──────────┴──────────┴─────────┘    │   │   │   │
│  │  │  └──────────────────────────────────────────────┘   │   │   │
│  │  └────────────────────────────────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### Stack Navigator — The Primary Pattern

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

const Stack = createStackNavigator();

function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        initialRouteName="Welcome"
        screenOptions={{
          headerStyle: { backgroundColor: '#fff', elevation: 0 },
          headerTitleAlign: 'center',
        }}
      >
        {/* Each Screen is a "route" */}
        <Stack.Screen
          name="Welcome"
          component={WelcomeScreen}
          options={{ headerShown: false }}  // Hide header for splash/welcome
        />
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{ headerTitle: '' }}     // Show header but no title
        />
        <Stack.Screen
          name="Feed"
          component={FeedScreen}
          options={({ navigation, route }) => ({
            // Dynamic options based on route params or navigation
            headerTitle: route.params?.title || 'Feed',
            headerRight: () => <FilterButton onPress={() => navigation.navigate('Filter')} />,
          })}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
```

### Navigation Actions — How to Move Between Screens

```jsx
// Every screen component receives a `navigation` prop (or use the hook)
import { useNavigation, useRoute } from '@react-navigation/native';

function LoginScreen() {
  const navigation = useNavigation();
  const route = useRoute();

  // 1. NAVIGATE — Go to a screen (pushes onto stack)
  const goToMFA = (userData) => {
    navigation.navigate('MFA_OPTION_SCREEN', {
      userData: userData,       // Pass data as params
      mfaType: 'email',
    });
  };

  // 2. GO BACK — Pop current screen off stack
  const goBack = () => {
    navigation.goBack();
  };

  // 3. RESET — Wipe the stack and start fresh (used after login/logout)
  const onLoginSuccess = () => {
    navigation.reset({
      index: 0,
      routes: [{ name: 'TAB_NAVIGATOR' }],   // User can't go "back" to login
    });
  };

  // 4. PUSH — Force a new instance (even if screen exists in stack)
  const openNewDetail = (id) => {
    navigation.push('FeedDetail', { feedId: id });
  };

  // 5. Reading params passed from previous screen
  const userData = route.params?.userData;

  return (/* ... */);
}
```

### Bottom Tab Navigator

```jsx
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

const Tab = createBottomTabNavigator();

function MainTabs() {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          // Return an icon component based on route name and focused state
          const iconName = focused ? `${route.name}_active` : `${route.name}_inactive`;
          return <Image source={IMAGES[iconName]} style={{ width: size, height: size }} />;
        },
        tabBarActiveTintColor: '#4A90D9',
        tabBarInactiveTintColor: '#999',
        tabBarStyle: { height: 80 },
        tabBarShowLabel: false,
      })}
    >
      <Tab.Screen name="FEED_TAB" component={FeedHomeScreen} />
      <Tab.Screen name="DISCOVER_TAB" component={DiscoverHomeScreen} />
      <Tab.Screen name="ACTIVITY_TAB" component={ActivityScreen} />
      <Tab.Screen name="PROFILE_TAB" component={ProfileScreen} />
    </Tab.Navigator>
  );
}
```

### STS-Specific Navigation Patterns

| Pattern | Where Used | How |
|---------|-----------|-----|
| **Auth guard** | `SplashScreen` | Checks AsyncStorage for token → navigates to Welcome or TabNavigator |
| **Stack reset on logout** | `callApiClass.js` | On 401 → clears storage → `navigation.reset({ routes: [{ name: 'WELCOME_SCREEN' }] })` |
| **Deep linking** | `AndroidManifest.xml` | `steamthestreet://` scheme opens specific screens |
| **Params for data** | Everywhere | Screens pass data via `navigation.navigate('Screen', { data })` |
| **Dynamic header** | `QuizScreen` | Shows page counter in header via `route.params?.page` |

---

## 4. State Management — Redux / Redux Toolkit

> **What it does**: Redux is a centralized state container. All shared app data lives in one "store" that any component can read from or write to.

### Why Redux Exists (The Problem It Solves)

```
WITHOUT REDUX (prop drilling):                WITH REDUX:
                                        
    App                                       App ←── Redux Store
     ├─ Header (needs user data)               ├─ Header ← useSelector(state.user)
     │    passed from App ↓                    ├─ Content
     ├─ Content                                │    ├─ Feed ← useSelector(state.feed)
     │    ├─ Feed (needs feed data)            │    └─ Detail
     │    │    passed from App ↓↓↓             └─ Footer ← useSelector(state.user)
     │    └─ Detail                            
     └─ Footer (needs user data)              Components read directly from store.
          passed from App ↓↓↓↓↓               No prop drilling.
```

### The Redux Flow

```
┌─────────────┐     dispatch(action)     ┌──────────────┐
│  Component  │ ──────────────────────►  │    Action     │
│  (Screen)   │                          │  Creator      │
└─────────────┘                          └──────┬───────┘
       ▲                                        │
       │                                        │ dispatch({ type, payload })
       │                                        ▼
┌──────┴──────┐                          ┌──────────────┐
│   Store     │ ◄─────────────────────── │   Reducer    │
│  (State)    │     returns new state    │  (Pure fn)   │
└─────────────┘                          └──────────────┘
```

### Current STS Pattern (Old Redux — What You'll Read in the Codebase)

```jsx
// ========================
// 1. ACTION TYPES (constants/reducerTypes.js)
// ========================
export const RED_TYPE = {
  API_LOADING: 'API_LOADING',
  USER_DATA: 'USER_DATA',
  ALERT_DATA: 'ALERT_DATA',
  FEED_LIST: 'FEED_LIST',
};

// ========================
// 2. ACTION CREATORS (actions/reduxAction.js)
// ========================
// This is the "thunk" pattern — actions return functions, not objects
export function showLoading(isLoading) {
  return (dispatch) => {                    // redux-thunk gives us dispatch
    dispatch({
      type: RED_TYPE.API_LOADING,
      isLoading: isLoading,
    });
  };
}

// Async action — fetches data and dispatches result
export const saveFeedList = (params, accessToken, navigation, page) => (dispatch) => {
  dispatch({ type: RED_TYPE.API_LOADING, isLoading: true });
  
  callApi([params], accessToken, navigation)
    .then((response) => {
      dispatch({ type: RED_TYPE.FEED_LIST, data: response });
      dispatch({ type: RED_TYPE.API_LOADING, isLoading: false });
    })
    .catch(() => {
      dispatch({ type: RED_TYPE.API_LOADING, isLoading: false });
    });
};

// ========================
// 3. REDUCER (reducers/storeState.js)
// ========================
const initialState = {
  isLoading: false,
  userData: {},
  feedList: null,
};

function storeReducer(state = initialState, action) {
  switch (action.type) {
    case RED_TYPE.API_LOADING:
      return { ...state, isLoading: action.isLoading };
    case RED_TYPE.USER_DATA:
      return { ...state, userData: action.userData };
    case RED_TYPE.FEED_LIST:
      return { ...state, feedList: action.data };
    default:
      return state;
  }
}

// ========================
// 4. STORE (reducers/index.js)
// ========================
import { createStore, combineReducers, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';

const rootReducer = combineReducers({
  redState: storeReducer,
  dashboardState: dashboardReducer,
});

export default () => createStore(rootReducer, applyMiddleware(thunk));

// ========================
// 5. USING IN COMPONENTS (the old class-based way in STS)
// ========================
import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';

class FeedScreen extends React.Component {
  componentDidMount() {
    this.props.saveFeedList(params, token, this.props.navigation, 1);
  }

  render() {
    const { feedList, isLoading } = this.props;
    return (/* ... */);
  }
}

// mapStateToProps: "which parts of the store does this component need?"
function mapStateToProps(state) {
  return {
    feedList: state.dashboardState.feedList,
    isLoading: state.redState.isLoading,
  };
}

// mapDispatchToProps: "which actions can this component trigger?"
function mapDispatchToProps(dispatch) {
  return bindActionCreators(ActionCreators, dispatch);
}

export default connect(mapStateToProps, mapDispatchToProps)(FeedScreen);
```

### Modern Redux Toolkit Pattern (What You'll Use in the Rebuild)

```jsx
// ========================
// 1. SLICE (replaces action types + action creators + reducer)
// ========================
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import api from '../api';

// Async thunk — handles pending/fulfilled/rejected automatically
export const fetchFeed = createAsyncThunk(
  'feed/fetchFeed',
  async ({ page, token }, { rejectWithValue }) => {
    try {
      const response = await api.get('/feed/list', {
        params: { page },
        headers: { Authorization: `Bearer ${token}` },
      });
      return { data: response.data, page };
    } catch (err) {
      return rejectWithValue(err.response?.data?.message || 'Failed to load feed');
    }
  }
);

const feedSlice = createSlice({
  name: 'feed',
  initialState: {
    items: [],
    loading: false,
    error: null,
    page: 1,
    hasMore: true,
  },
  reducers: {
    // Synchronous actions (auto-generated action creators)
    clearFeed: (state) => {
      state.items = [];
      state.page = 1;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchFeed.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchFeed.fulfilled, (state, action) => {
        state.loading = false;
        if (action.payload.page === 1) {
          state.items = action.payload.data.data;
        } else {
          state.items.push(...action.payload.data.data);  // Immer lets you "mutate"!
        }
        state.hasMore = action.payload.data.data.length > 0;
        state.page = action.payload.page;
      })
      .addCase(fetchFeed.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  },
});

export const { clearFeed } = feedSlice.actions;
export default feedSlice.reducer;

// ========================
// 2. STORE (much simpler)
// ========================
import { configureStore } from '@reduxjs/toolkit';
import feedReducer from './slices/feedSlice';
import authReducer from './slices/authSlice';

export const store = configureStore({
  reducer: {
    feed: feedReducer,
    auth: authReducer,
  },
  // Thunk middleware is included automatically!
});

// ========================
// 3. USING IN COMPONENTS (hooks — the modern way)
// ========================
import { useSelector, useDispatch } from 'react-redux';

function FeedScreen() {
  const dispatch = useDispatch();
  const { items, loading, error } = useSelector((state) => state.feed);
  const token = useSelector((state) => state.auth.token);

  useEffect(() => {
    dispatch(fetchFeed({ page: 1, token }));
  }, []);

  const loadMore = () => {
    if (!loading) {
      dispatch(fetchFeed({ page: feed.page + 1, token }));
    }
  };

  return (
    <FlatList
      data={items}
      renderItem={({ item }) => <FeedCard post={item} />}
      onEndReached={loadMore}
      refreshing={loading}
      onRefresh={() => dispatch(fetchFeed({ page: 1, token }))}
    />
  );
}
```

### STS Store Shape (What You Need to Know)

```
store
├── redState                    (app-wide concerns)
│   ├── isLoading: boolean      ← global loading spinner
│   ├── userData: object        ← current user
│   ├── alertData: object       ← global alert dialog
│   ├── toastData: object       ← global toast notification
│   ├── isOnline: boolean       ← network connectivity
│   ├── searchData: object      ← search state
│   └── notificationList: array ← notifications
│
└── dashboardState              (feature/data concerns)
    ├── feedList: object        ← feed posts (paginated)
    ├── feedDetails: object     ← current feed detail
    ├── discoveryList: object   ← challenges
    ├── leaderboardList: object ← leaderboard
    ├── badgesList: object      ← badges
    ├── rewardsList: object     ← rewards
    ├── challenge: object       ← current challenge
    └── ... (15+ more slices)
```

---

## 5. API Fetching — Axios

> **What it does**: Axios is an HTTP client. It makes API calls (GET, POST, PUT, DELETE) to the backend server. It works identically to how you'd use it on the web.

### Core Axios API

```jsx
import axios from 'axios';

// ========================
// CREATE AN INSTANCE (recommended pattern for the rebuild)
// ========================
const api = axios.create({
  baseURL: 'https://dashboard.steamthestreets.org/api/v1/',
  timeout: 10000,                        // 10 seconds
  headers: {
    'Content-Type': 'application/json',
    'app_version': '2.1.0',
  },
});

// ========================
// GET REQUEST — Fetch data
// ========================
const getFeed = async (page) => {
  const response = await api.get('feed/list', {
    params: { page, per_page: 20 },    // → ?page=1&per_page=20
  });
  return response.data;                  // { success: true, data: [...] }
};

// ========================
// POST REQUEST — Send data (JSON)
// ========================
const login = async (email, password) => {
  const response = await api.post('login', {
    email,
    password,
  });
  return response.data;                  // { success: true, user: {...}, access_token: '...' }
};

// ========================
// POST REQUEST — Send data (FormData / file upload)
// ========================
const updateAvatar = async (imageFile) => {
  const formData = new FormData();
  formData.append('avatar', {
    uri: imageFile.uri,                  // file:///path/to/image.jpg
    type: 'image/jpeg',
    name: 'avatar.jpg',
  });

  const response = await api.post('updateAvatarMultiple', formData, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
  return response.data;
};

// ========================
// PUT / PATCH / DELETE
// ========================
await api.put('updateme', { name: 'New Name' });
await api.patch('updateme', { name: 'New Name' });  // Same but partial
await api.delete('user/delete');
```

### Interceptors (The Key Pattern for the Rebuild)

Interceptors run before every request or after every response. This is how you'll handle auth tokens and 401 logouts cleanly (replacing the anti-pattern in the current STS code where `navigation` is passed to the API layer).

```jsx
// ========================
// REQUEST INTERCEPTOR — Attach token to every request
// ========================
api.interceptors.request.use(
  async (config) => {
    const token = await AsyncStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// ========================
// RESPONSE INTERCEPTOR — Handle 401 globally
// ========================
api.interceptors.response.use(
  (response) => response,    // Success: pass through
  async (error) => {
    if (error.response?.status === 401) {
      // Token expired — clear storage and redirect
      await AsyncStorage.multiRemove(['access_token', 'user_data', 'isLogin']);
      // Use a navigation ref (not passed navigation prop!)
      navigationRef.current?.reset({
        index: 0,
        routes: [{ name: 'WELCOME_SCREEN' }],
      });
    }
    return Promise.reject(error);
  }
);
```

### Error Handling

```jsx
try {
  const response = await api.post('login', { email, password });
  // Handle success
} catch (error) {
  if (error.response) {
    // Server responded with error status (4xx, 5xx)
    console.log(error.response.status);        // 401, 422, 500...
    console.log(error.response.data);          // { message: 'Invalid credentials' }
    console.log(error.response.data.message);  // 'Invalid credentials'
  } else if (error.request) {
    // Request was made but no response (network error, timeout)
    console.log('Network error — no response');
  } else {
    // Something else went wrong
    console.log('Error:', error.message);
  }
}
```

### How STS Currently Uses Axios

```
┌─────────────────────────────────────────────────────────────────┐
│  CURRENT STS PATTERN (what you'll see in the codebase)          │
│                                                                  │
│  Screen → dispatch(action)                                       │
│     ↓                                                            │
│  Action Creator → callApi([params], token, navigation)           │
│     ↓                                                            │
│  callApiClass.js → axios.all([...promises])                      │
│     ↓                                                            │
│  apiCallGetData.js → axios({ method, url, data, headers })      │
│     ↓                                                            │
│  Backend API                                                     │
│                                                                  │
│  ⚠ ANTI-PATTERNS:                                               │
│  • navigation object passed into API layer                       │
│  • axios.all / axios.spread (deprecated)                         │
│  • No interceptors                                               │
│  • No retry logic                                                │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  REBUILD PATTERN (what you'll write)                             │
│                                                                  │
│  Screen → dispatch(asyncThunk)                                   │
│     ↓                                                            │
│  RTK createAsyncThunk → api.get/post/put/delete                  │
│     ↓                                                            │
│  Axios instance with interceptors                                │
│     ↓                                                            │
│  Backend API                                                     │
│                                                                  │
│  ✅ IMPROVEMENTS:                                                │
│  • Interceptors handle auth + 401 globally                       │
│  • Navigation ref for redirects (no coupling)                    │
│  • Standard Promise.all if needed                                │
│  • Proper error typing with TypeScript                           │
└─────────────────────────────────────────────────────────────────┘
```

### All STS API Endpoints You'll Call

| Category | Endpoint | Method | Used For |
|----------|----------|--------|----------|
| **Auth** | `login` | POST | Email/password login |
| | `signup` | POST | User registration |
| | `logout` | POST | Session end |
| | `forgot` | POST | Password reset email |
| | `otp/generate` | POST | Send MFA code |
| | `otp/verify` | POST | Verify MFA code |
| **Profile** | `me` | GET | Current user profile |
| | `updateme` | POST | Update profile |
| | `updateAvatarMultiple` | POST | Upload avatar (FormData) |
| **Feed** | `feed/list` | GET | Paginated feed |
| | `feed/detail` | GET | Single post |
| | `feed/likeunlike` | POST | Toggle like |
| **Challenges** | `challenge/list` | GET | All challenges |
| | `challenge/detail` | GET | Single challenge |
| | `challenge/accept` | POST | Accept challenge |
| **Lessons** | `lesson/detail` | GET | Lesson content |
| | `lesson/completed/` | POST | Mark complete |
| **Quiz** | `questions` | GET | Quiz questions |
| | `update-user-questions-data` | POST | Submit answers |
| **Gamification** | `leaderboard` | GET | Rankings |
| | `badge-list` | GET | Available badges |
| | `reward-list` | GET | Available rewards |

---

## 6. Local Storage — AsyncStorage

> **What it does**: AsyncStorage is the React Native equivalent of `localStorage`, but it's **async** (returns Promises). It persists key-value pairs on the device.

```jsx
import AsyncStorage from '@react-native-async-storage/async-storage';

// ========================
// STORE a value
// ========================
await AsyncStorage.setItem('access_token', 'eyJhbG...');
await AsyncStorage.setItem('user_data', JSON.stringify(userObject));

// ========================
// READ a value
// ========================
const token = await AsyncStorage.getItem('access_token');     // string or null
const userData = JSON.parse(await AsyncStorage.getItem('user_data'));

// ========================
// REMOVE a value
// ========================
await AsyncStorage.removeItem('access_token');

// ========================
// MULTI-operations (the STS pattern)
// ========================
// Store multiple at once
await AsyncStorage.multiSet([
  ['access_token', token],
  ['user_data', JSON.stringify(user)],
  ['isLogin', 'true'],
]);

// Read multiple at once
const values = await AsyncStorage.multiGet(['access_token', 'user_data', 'isLogin']);
// values = [['access_token', 'eyJ...'], ['user_data', '{...}'], ['isLogin', 'true']]

// Remove multiple at once
await AsyncStorage.multiRemove(['access_token', 'user_data', 'isLogin']);
```

### STS Storage Keys

| Key | Type | Purpose |
|-----|------|---------|
| `access_token` | string | JWT Bearer token |
| `user_data` | JSON string | Full user object |
| `isLogin` | string `'true'`/`'false'` | Auth state flag |
| `FCM_TOKEN` | string | Firebase Cloud Messaging device token |
| `language` | string | Selected language |
| `isFirstTimeLogin` | string | First-time user flag |
| `isFirstTimeFeed` | string | First-time feed tooltip flag |

---

## 7. Firebase — Auth, Messaging, Notifications

> **What it does**: Firebase provides push notifications via FCM (Firebase Cloud Messaging). The STS app uses Firebase for: registering device tokens, receiving push notifications, and handling notification taps.

### Architecture

```
┌─────────────┐          ┌──────────────┐          ┌─────────────┐
│  STS Backend │ ────────►│  Firebase    │ ────────►│  User's     │
│  Server      │  sends   │  Cloud       │  delivers│  Phone      │
│              │  push    │  Messaging   │  push    │             │
└─────────────┘  payload  └──────────────┘  notif   └─────────────┘
                                                          │
                                                          ▼
                                              ┌─────────────────────┐
                                              │  App receives via    │
                                              │  onMessage (fg)      │
                                              │  setBackground (bg)  │
                                              └─────────────────────┘
```

### Key Firebase Operations in STS

```jsx
import messaging from '@react-native-firebase/messaging';

// 1. Request notification permission
const authStatus = await messaging().requestPermission();

// 2. Get FCM token (unique device identifier)
const fcmToken = await messaging().getToken();
// → Send this token to your backend: POST /user_token { token: fcmToken }

// 3. Listen for foreground messages
const unsubscribe = messaging().onMessage(async (remoteMessage) => {
  // App is OPEN — show a local notification or in-app banner
  console.log('Foreground message:', remoteMessage.notification);
});

// 4. Background message handler (registered at app entry)
messaging().setBackgroundMessageHandler(async (remoteMessage) => {
  // App is in BACKGROUND or KILLED — handle silently
  console.log('Background message:', remoteMessage.data);
});

// 5. Handle notification tap (what happens when user taps the notification)
messaging().onNotificationOpenedApp((remoteMessage) => {
  // App was in BACKGROUND → navigate to relevant screen
  navigation.navigate('FeedDetail', { feedId: remoteMessage.data.feed_id });
});

// 6. Check if app was opened from a killed state via notification
const initialNotification = await messaging().getInitialNotification();
if (initialNotification) {
  // App was KILLED → opened from notification tap
  navigation.navigate('FeedDetail', { feedId: initialNotification.data.feed_id });
}
```

### What Changes in the Rebuild

| Current (v14) | Rebuild (v22) |
|---------------|---------------|
| `@react-native-firebase/app` ^14 | `@react-native-firebase/app` ^22 |
| Namespaced API (same syntax) | Mostly same for RN Firebase |
| `react-native-push-notification` for local | `@notifee/react-native` for local |
| No Android 13 permission | Must request `POST_NOTIFICATIONS` |

---

## 8. Notifications — @notifee/react-native

> **What it does**: Notifee replaces the deprecated `react-native-push-notification` library. It handles **local notifications** (displaying them on the device), while Firebase handles the **remote delivery**.

### The Split Responsibility

```
┌──────────────────────────┐     ┌──────────────────────────┐
│     FIREBASE (FCM)        │     │     NOTIFEE              │
│                           │     │                          │
│  • Receives remote push   │     │  • Creates notification  │
│  • Delivers payload to    │ ──► │    channels (Android)    │
│    your app               │     │  • Displays local notifs │
│  • Background handling    │     │  • Handles tap actions   │
│                           │     │  • Scheduled triggers    │
│  Remote side              │     │  Local side              │
└──────────────────────────┘     └──────────────────────────┘
```

### Core Notifee Usage

```jsx
import notifee, { AndroidImportance } from '@notifee/react-native';

// 1. Create a notification channel (Android requires this)
async function createChannel() {
  await notifee.createChannel({
    id: 'default',
    name: 'Default Channel',
    importance: AndroidImportance.HIGH,    // Shows heads-up notification
    sound: 'default',
  });
}

// 2. Display a notification
async function displayNotification(title, body, data) {
  await notifee.displayNotification({
    title,
    body,
    data,                                  // Custom data for handling taps
    android: {
      channelId: 'default',
      pressAction: { id: 'default' },     // Required for tap handling
      smallIcon: 'ic_notification',        // Android requires this
    },
    ios: {
      sound: 'default',
    },
  });
}

// 3. Handle foreground notification from Firebase
messaging().onMessage(async (remoteMessage) => {
  // Use Notifee to show it (Firebase doesn't show foreground notifications)
  await displayNotification(
    remoteMessage.notification.title,
    remoteMessage.notification.body,
    remoteMessage.data,
  );
});

// 4. Handle notification tap
notifee.onForegroundEvent(({ type, detail }) => {
  if (type === EventType.PRESS) {
    // User tapped the notification
    const feedId = detail.notification.data?.feed_id;
    if (feedId) navigation.navigate('FeedDetail', { feedId });
  }
});

// 5. Request permission (Android 13+)
async function requestPermission() {
  const settings = await notifee.requestPermission();
  // settings.authorizationStatus: AUTHORIZED, DENIED, PROVISIONAL
}
```

---

## 9. UI Toolkit — React Native Elements / RNEUI

> **What it does**: Provides pre-built, styled UI components (buttons, inputs, checkboxes, avatars, etc.) so you don't build everything from scratch.

### Components Used in STS

```jsx
import { Button, CheckBox, Avatar, SearchBar, Divider } from 'react-native-elements';
// Rebuild will use: import { Button, CheckBox, ... } from '@rneui/themed';

// Button
<Button
  title="Login"
  onPress={handleLogin}
  buttonStyle={{ backgroundColor: '#4A90D9', borderRadius: 8 }}
  titleStyle={{ fontWeight: 'bold' }}
  loading={isLoading}              // Shows spinner inside button
  disabled={!isValid}
  type="solid"                     // 'solid' | 'outline' | 'clear'
/>

// CheckBox
<CheckBox
  title="I agree to Terms"
  checked={isChecked}
  onPress={() => setIsChecked(!isChecked)}
  checkedColor="#4A90D9"
/>

// SearchBar
<SearchBar
  placeholder="Search..."
  onChangeText={setSearch}
  value={search}
  platform="default"               // 'default' | 'ios' | 'android'
  lightTheme
/>
```

**STS Usage**: Buttons in headers, login/signup forms, filter screens, feed search.

---

## 10. Icons — react-native-vector-icons

> **What it does**: Gives you access to thousands of icons (FontAwesome, MaterialIcons, Ionicons, etc.) as React components.

```jsx
import Icon from 'react-native-vector-icons/MaterialIcons';
import FontAwesome from 'react-native-vector-icons/FontAwesome';

<Icon name="arrow-back" size={24} color="#333" />
<FontAwesome name="heart" size={20} color="red" />

// As a button
<Icon.Button
  name="facebook"
  backgroundColor="#3b5998"
  onPress={handleFacebookLogin}
>
  Login with Facebook
</Icon.Button>
```

**STS Usage**: Tab bar icons, header back buttons, action buttons throughout the app.

---

## 11. Forms & Input Masking

> **What it does**: `react-native-mask-input` formats user input in real-time (e.g., phone numbers: `+1 999-999-9999`).

```jsx
import MaskInput from 'react-native-mask-input';

// Phone number mask
<MaskInput
  value={phone}
  onChangeText={(masked, unmasked) => {
    setPhone(masked);                // "+1 234-567-8901"
    setRawPhone(unmasked);           // "12345678901"
  }}
  mask={['+', '1', ' ', /\d/, /\d/, /\d/, '-', /\d/, /\d/, /\d/, '-', /\d/, /\d/, /\d/, /\d/]}
  placeholder="+1 000-000-0000"
  keyboardType="phone-pad"
/>

// Date mask
<MaskInput
  value={date}
  onChangeText={(masked, unmasked) => setDate(masked)}
  mask={[/\d/, /\d/, '/', /\d/, /\d/, '/', /\d/, /\d/, /\d/, /\d/]}
  placeholder="MM/DD/YYYY"
/>
```

**STS Usage**: `SignUpScreen` uses it for phone number input. `MfaOptionScreen` currently uses the old `react-native-masked-text` (to be replaced).

---

## 12. Media — Video, YouTube, Sound

### react-native-video (Native Video Player)

```jsx
import Video from 'react-native-video';

<Video
  source={{ uri: 'https://example.com/video.mp4' }}
  style={{ width: '100%', height: 200 }}
  controls={true}                    // Show native controls
  paused={isPaused}
  resizeMode="contain"
  onProgress={({ currentTime, seekableDuration }) => {
    // Track watch progress (STS uses 80% watched rule)
    const percent = (currentTime / seekableDuration) * 100;
    if (percent >= 80) markAsWatched();
  }}
  onEnd={() => {/* Video finished */}}
  onError={(error) => {/* Handle error */}}
/>
```

### react-native-youtube-iframe

```jsx
import YoutubePlayer from 'react-native-youtube-iframe';

<YoutubePlayer
  height={200}
  videoId="dQw4w9WgXcQ"              // Extract from YouTube URL
  play={playing}
  onChangeState={(event) => {
    if (event === 'ended') handleVideoEnd();
  }}
/>
```

### react-native-sound

```jsx
import Sound from 'react-native-sound';

// Play a bundled sound
const sound = new Sound('congrats.wav', Sound.MAIN_BUNDLE, (error) => {
  if (!error) sound.play();
});
```

**STS Usage**: `VideoDetailsScreen` uses native video + YouTube. `WelcomeScreen` plays an opening sound. The contract wants to replace YouTube iframe with native player.

---

## 13. Animations — Lottie

> **What it does**: Lottie renders After Effects animations exported as JSON files. Much lighter than video, fully interactive.

```jsx
import LottieView from 'lottie-react-native';

<LottieView
  source={require('../Image/9975_fireworks.json')}  // Lottie JSON file
  autoPlay
  loop={false}
  style={{ width: 200, height: 200 }}
  onAnimationFinish={() => {/* Navigate after animation */}}
/>
```

**STS Usage**: `LoadingScreen` (assessment loading), `FinishQuiz` (celebration animation), splash transitions.

---

## 14. Layout Components

### Carousels (react-native-snap-carousel → react-native-reanimated-carousel)

```jsx
// Current STS uses snap-carousel (deprecated, will be replaced)
// The rebuild pattern with reanimated-carousel:
import Carousel from 'react-native-reanimated-carousel';

<Carousel
  data={lessons}
  renderItem={({ item }) => <LessonCard lesson={item} />}
  width={screenWidth}
  height={200}
  mode="parallax"
/>
```

### Tab View (react-native-tab-view)

```jsx
import { TabView, TabBar, SceneMap } from 'react-native-tab-view';

// Used in ActivityScreen for Leaderboard | Badges | Rewards tabs
const renderScene = SceneMap({
  leaderboard: LeaderboardTab,
  badges: BadgesTab,
  rewards: RewardsTab,
});

<TabView
  navigationState={{ index, routes }}
  renderScene={renderScene}
  onIndexChange={setIndex}
  renderTabBar={(props) => (
    <TabBar
      {...props}
      indicatorStyle={{ backgroundColor: '#4A90D9' }}
      style={{ backgroundColor: '#fff' }}
      labelStyle={{ color: '#333' }}
    />
  )}
/>
```

### Pager View & Swiper (Multi-Step Forms)

```jsx
import PagerView from 'react-native-pager-view';

// Used in SignUpScreen for the 4-step signup flow
<PagerView
  ref={pagerRef}
  initialPage={0}
  scrollEnabled={false}     // Disable swipe, control programmatically
  onPageSelected={(e) => setCurrentPage(e.nativeEvent.position)}
>
  <View key="1"><StepOne /></View>
  <View key="2"><StepTwo /></View>
  <View key="3"><StepThree /></View>
  <View key="4"><StepFour /></View>
</PagerView>

// Navigate programmatically
pagerRef.current?.setPage(nextPage);
```

### Step Indicator

```jsx
import StepIndicator from 'react-native-step-indicator';

// Used in DiscoverDetailsScreen for lesson progress
<StepIndicator
  currentPosition={currentStep}
  stepCount={totalSteps}
  labels={['Intro', 'Video', 'Quiz', 'Reflect']}
  customStyles={{
    stepIndicatorCurrentColor: '#4A90D9',
    stepIndicatorFinishedColor: '#4A90D9',
    currentStepLabelColor: '#4A90D9',
  }}
/>
```

---

## 15. Permissions — react-native-permissions

> **What it does**: Requests and checks OS-level permissions (camera, photos, location, notifications).

```jsx
import { check, request, PERMISSIONS, RESULTS } from 'react-native-permissions';
import { Platform } from 'react-native';

// Check permission status
const cameraStatus = await check(
  Platform.OS === 'ios'
    ? PERMISSIONS.IOS.CAMERA
    : PERMISSIONS.ANDROID.CAMERA
);

// Request permission
if (cameraStatus !== RESULTS.GRANTED) {
  const result = await request(
    Platform.OS === 'ios'
      ? PERMISSIONS.IOS.CAMERA
      : PERMISSIONS.ANDROID.CAMERA
  );
  
  switch (result) {
    case RESULTS.GRANTED:     // Permission granted
      break;
    case RESULTS.DENIED:      // Permission denied (can ask again)
      break;
    case RESULTS.BLOCKED:     // Permission blocked (must go to settings)
      break;
  }
}

// Android 13+ notification permission (new requirement!)
if (Platform.OS === 'android' && Platform.Version >= 33) {
  await request(PERMISSIONS.ANDROID.POST_NOTIFICATIONS);
}
```

**STS Usage**: Notification permissions, camera (avatar), location (dashboard search).

---

## 16. Networking Info — NetInfo

> **What it does**: Detects network connectivity status (online/offline).

```jsx
import NetInfo from '@react-native-community/netinfo';

// One-time check
const state = await NetInfo.fetch();
console.log('Connected?', state.isConnected);
console.log('Type:', state.type);  // 'wifi', 'cellular', 'none'

// Real-time listener
const unsubscribe = NetInfo.addEventListener((state) => {
  if (!state.isConnected) {
    showToast('No internet connection');
  }
});
```

**STS Usage**: `reduxAction.js` has a `networkListner()` that dispatches online/offline status to Redux store.

---

## 17. Date Handling

### Current: Moment.js (300KB+ — being replaced)

```jsx
import moment from 'moment';

moment('2024-01-15').format('MMM DD, YYYY');  // "Jan 15, 2024"
moment().fromNow();                            // "2 hours ago"
```

### Rebuild: Day.js (2KB — drop-in replacement)

```jsx
import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';
dayjs.extend(relativeTime);

dayjs('2024-01-15').format('MMM DD, YYYY');   // "Jan 15, 2024"
dayjs().fromNow();                             // "2 hours ago"

// Same API, 150x smaller
```

---

## 18. Internationalization

### Current: react-native-i18n (deprecated)

```jsx
// src/languages/english.js
export default {
  LOGIN_SCREEN: 'Login',
  WELCOME_SCREEN: 'Welcome',
  FEED_TAB: 'Feed',
  // ...
};

// src/languages/localize.js
export const localize = (key) => strings[key] || key;
```

### Rebuild: react-i18next

```jsx
import { useTranslation } from 'react-i18next';

function LoginScreen() {
  const { t } = useTranslation();
  return <Text>{t('login.title')}</Text>;  // "Login"
}
```

**STS Usage**: Screen titles in navigation headers, button labels, form labels, error messages.

---

## 19. WebView

> **What it does**: Renders web pages inside the app (Terms of Service, Privacy Policy, external links).

```jsx
import { WebView } from 'react-native-webview';

<WebView
  source={{ uri: 'https://steamthestreets.org/terms' }}
  // OR local HTML:
  // source={{ html: '<h1>Hello</h1>' }}
  onNavigationStateChange={(navState) => {
    // Track URL changes
    console.log('Current URL:', navState.url);
  }}
  startInLoadingState={true}
  renderLoading={() => <ActivityIndicator />}
/>
```

**STS Usage**: `WebViewScreen` displays terms, privacy policy, and external links.

---

## 20. Native Build System

### How Building Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    YOUR JS/TS SOURCE CODE                        │
│              (screens, components, logic)                         │
├──────────────────────────┬──────────────────────────────────────┤
│       METRO BUNDLER      │                                       │
│  (JS bundler, like       │  Watches files, hot reloads,         │
│   webpack for RN)        │  bundles into single JS file         │
├──────────────────────────┴──────────────────────────────────────┤
│                                                                  │
│  ┌────────────────────┐        ┌──────────────────────┐         │
│  │   ANDROID BUILD    │        │    iOS BUILD          │         │
│  │                    │        │                       │         │
│  │  Gradle (build     │        │  Xcode / CocoaPods   │         │
│  │  tool for Android) │        │  (build tools for    │         │
│  │                    │        │   iOS)                │         │
│  │  Java 17           │        │  Requires macOS      │         │
│  │  Android SDK       │        │  OR cloud build      │         │
│  │                    │        │  (EAS Build)          │         │
│  │  Output: .apk/.aab │        │  Output: .ipa        │         │
│  └────────────────────┘        └──────────────────────┘         │
└─────────────────────────────────────────────────────────────────┘
```

### Essential Commands

```bash
# ========================
# DEVELOPMENT
# ========================
npx react-native start                    # Start Metro bundler
npx react-native run-android              # Build + run on Android device/emulator
npx react-native run-ios                  # Build + run on iOS simulator (Mac only)

# ========================
# ANDROID RELEASE BUILD
# ========================
cd android
./gradlew assembleRelease                 # Creates APK
./gradlew bundleRelease                   # Creates AAB (for Play Store)
# Output: android/app/build/outputs/apk/release/app-release.apk

# ========================
# CLEAN BUILDS (when things break)
# ========================
cd android && ./gradlew clean && cd ..    # Clean Android build cache
npx react-native start --reset-cache     # Clear Metro bundler cache
rm -rf node_modules && yarn install       # Nuclear option

# ========================
# iOS (via EAS Build — no Mac needed)
# ========================
eas build --platform ios --profile development   # Dev build
eas build --platform ios --profile production     # Production build
```

### The STS Build Scripts

```bash
# From package.json
yarn android             # npx react-native run-android
yarn ios                 # npx react-native run-ios
yarn start               # npx react-native start
yarn bundle:android      # Bundle JS for Android release
yarn release:android     # Full release build
```

---

## 21. The Mental Model — How Everything Connects

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         STS MOBILE APP ARCHITECTURE                      │
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                        SCREENS (UI Layer)                        │    │
│  │                                                                  │    │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐           │    │
│  │  │  Login   │ │   Feed   │ │ Discover │ │ Profile  │   ...     │    │
│  │  │  Screen  │ │  Screen  │ │  Screen  │ │  Screen  │           │    │
│  │  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘           │    │
│  │       │             │            │             │                  │    │
│  └───────┼─────────────┼────────────┼─────────────┼──────────────────┘    │
│          │             │            │             │                       │
│  ┌───────▼─────────────▼────────────▼─────────────▼──────────────────┐    │
│  │                    NAVIGATION (React Navigation)                   │    │
│  │              Stack Navigator + Bottom Tab Navigator                 │    │
│  └───────────────────────────┬───────────────────────────────────────┘    │
│                              │                                           │
│  ┌───────────────────────────▼───────────────────────────────────────┐    │
│  │                      STATE (Redux / RTK)                           │    │
│  │                                                                    │    │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐         │    │
│  │  │  Auth    │  │  Feed    │  │ Discover │  │  UI      │         │    │
│  │  │  Slice   │  │  Slice   │  │  Slice   │  │  Slice   │         │    │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘         │    │
│  └───────┼──────────────┼────────────┼──────────────┼────────────────┘    │
│          │              │            │              │                      │
│  ┌───────▼──────────────▼────────────▼──────────────▼────────────────┐    │
│  │                        API LAYER (Axios)                           │    │
│  │           Interceptors → Auth Header → Error Handling              │    │
│  └───────────────────────────┬───────────────────────────────────────┘    │
│                              │                                           │
│  ┌───────────────────────────▼───────────────────────────────────────┐    │
│  │                    SERVICES & STORAGE                              │    │
│  │                                                                    │    │
│  │  ┌────────────┐  ┌──────────────┐  ┌──────────────┐              │    │
│  │  │ Firebase   │  │ AsyncStorage │  │ Permissions  │              │    │
│  │  │ (FCM/Auth) │  │ (Token,User) │  │ (Camera,etc) │              │    │
│  │  └────────────┘  └──────────────┘  └──────────────┘              │    │
│  └───────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐    │
│  │                      BACKEND API                                   │    │
│  │        https://dashboard.steamthestreets.org/api/v1/               │    │
│  └───────────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

### Your Learning Priority Order

| Priority | Skill | Time | Why |
|----------|-------|------|-----|
| **1** | React Native Core (View, Text, FlatList, StyleSheet) | 2-3 hours | Everything else builds on this |
| **2** | React Navigation (Stack + Tabs) | 2 hours | You can't show any screen without it |
| **3** | Redux Toolkit (slices, thunks, useSelector) | 2-3 hours | Every screen reads/writes state |
| **4** | Axios (instances, interceptors, error handling) | 1 hour | Every screen calls the API |
| **5** | AsyncStorage | 30 min | Simple key-value — very quick to learn |
| **6** | Firebase + Notifee | 2 hours | Push notifications — contract requirement |
| **7** | UI Components (Elements, Icons, Masks) | 1 hour | Learn as you build each screen |
| **8** | Media (Video, Sound, Lottie) | 1 hour | Specific screens only |
| **9** | Build System (Gradle, Metro, EAS) | 1 hour | You need this to run the app |
| **10** | TypeScript setup for RN | 1 hour | The rebuild will be TypeScript |

**Total estimated study time: ~15 hours across 3-4 days before Monday.**

---

> **Bottom line**: You already know JS/TS and React concepts (components, props, state, hooks). The "mystery" of mobile is really just learning: (1) different primitives (`View` not `div`), (2) Flexbox-only layout, (3) React Navigation instead of React Router, (4) AsyncStorage instead of localStorage, and (5) native build tools. Everything else (Redux, Axios, Firebase) works the same as on the web. Focus on priorities 1-4 and you'll be productive by Monday.
