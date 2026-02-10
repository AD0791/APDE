# STS Mobile App -- Codebase & Project Intelligence

> **Purpose**: A complete dissection of the Steam The Streets (STS) mobile app codebase, its architecture, every dependency, every pattern, and a mapping to what needs to change for the rebuild. This is the document you read before writing a single line of code.

---

## Table of Contents

1. [Project Identity](#1-project-identity)
2. [The Contract -- What Was Agreed](#2-the-contract----what-was-agreed)
3. [Architecture Overview](#3-architecture-overview)
4. [Entry Point and App Bootstrap](#4-entry-point-and-app-bootstrap)
5. [Navigation System](#5-navigation-system)
6. [State Management (Redux)](#6-state-management-redux)
7. [API Layer](#7-api-layer)
8. [Authentication and MFA Flow](#8-authentication-and-mfa-flow)
9. [Firebase and Notifications](#9-firebase-and-notifications)
10. [Every Screen Mapped](#10-every-screen-mapped)
11. [Component Library](#11-component-library)
12. [Dependency Audit -- Every Package, Its Role, and Its Future](#12-dependency-audit----every-package-its-role-and-its-future)
13. [Native Configuration](#13-native-configuration)
14. [Patterns and Anti-Patterns in the Codebase](#14-patterns-and-anti-patterns-in-the-codebase)
15. [The Rebuild Roadmap](#15-the-rebuild-roadmap)

---

## 1. Project Identity

| Field | Value |
|-------|-------|
| **App Name** | Steam The Streets |
| **Package (Android)** | `com.steamthestreets.sts` |
| **Display Name** | "SteamTheStreet" |
| **Current RN Version** | 0.65.1 |
| **React Version** | 17.0.2 |
| **Current App Version** | 2.1.0 (Build 8) |
| **Language** | JavaScript (no TypeScript) |
| **Architecture** | Old Architecture (Bridge, no Hermes) |
| **State Management** | Redux + Redux Thunk |
| **Navigation** | React Navigation v6 (Stack + Bottom Tabs) |
| **API Client** | Axios |
| **Backend API** | `https://dashboard.steamthestreets.org/api/v1/` |
| **Firebase** | `@react-native-firebase/*` v14 (Namespaced API) |
| **Deep Link Scheme** | `steamthestreet://` |
| **Orientation** | Portrait only |
| **Min Android** | API 21 (Android 5.0) |
| **Min iOS** | 15.6 |

---

## 2. The Contract -- What Was Agreed

### Core Upgrade (Required)

| Deliverable | From | To |
|-------------|------|----|
| React Native version | 0.65.1 | 0.74.x+ (Bridgeless Mode) |
| JS Engine | JavaScriptCore | Hermes |
| Java version | 8/11 | 17 |
| Gradle version | 4.1.0 | 8.8 |
| Layout engine | Yoga 2.x | Yoga 3.0 (audit all layouts) |
| Firebase | v14 (Namespaced) | v18/v22 (Modular API) |
| Notifications | `react-native-push-notification` | `@notifee/react-native` |
| Input masking | `react-native-masked-text` | `react-native-mask-input` |
| Dev tools | Flipper | React Native DevTools |
| RewardsModal | Sync state bug | Fix for React 18 async state |

### Optional Enhancements (Phase 5)

| Feature | Description |
|---------|-------------|
| Quiz validation fix | Correct answers flagged as incorrect -- debug state logic |
| Native video player | Replace YouTube iframe with `react-native-video` -- anti-distraction, custom controls, 80% watched rule |
| Attribution query | "How did you find us?" prompt in onboarding |
| "Free First Step" UI | Updated CTA placement |
| Dashboard search | Location-based search and filter on main dashboard |

### Timeline

11 weeks. Milestones: Core Environment → Native Alignment → Dependency Logic → UI & QA → Optional.

---

## 3. Architecture Overview

```
sts-mobile-app/
│
├── index.js                          ← RN entry point, registers App
├── src/
│   ├── index.js                      ← Real App component (Redux Provider, SafeArea, Navigation)
│   │
│   ├── navigator/                    ← Navigation configuration
│   │   ├── stackNavigator.js         ← All screens registered here
│   │   ├── TabNavigator.js           ← Bottom tab bar (Feed, Discover, Activity, Profile)
│   │   └── index.js
│   │
│   ├── screens/                      ← All screen components (class-based)
│   │   ├── 0_AssessmentScreen/       ← Career assessment flow
│   │   ├── 1_SplashScreen/           ← App initialization
│   │   ├── 2_WelcomeScreen/          ← Landing page
│   │   ├── 3_LoginScreen/            ← Login
│   │   ├── 4_SignUpScreen/           ← Multi-step signup
│   │   ├── 5_ForgotPasswordScreen/
│   │   ├── 6_FeedScreen/             ← Feed (home, detail, filter)
│   │   ├── 9_ProfileScreen/          ← Profile (view, edit, settings, avatar)
│   │   ├── 10_ChangePasswordScreen/
│   │   ├── 11_FavouriteScreen/       ← Favorites (feeds + careers)
│   │   ├── 12_Loader/
│   │   ├── 13_DiscoverScreen/        ← Discovery/LMS (challenges, videos, quizzes)
│   │   ├── 14_WebViewScreen/
│   │   ├── 15_ActivityScreen/        ← Leaderboard, badges, rewards
│   │   ├── 16_NotificationScreen/
│   │   ├── MfaOptionScreen/          ← MFA method selection
│   │   └── OtpScreen/               ← OTP verification
│   │
│   ├── actions/                      ← Redux action creators
│   │   ├── reduxAction.js            ← App-wide actions (loading, alerts, user data)
│   │   └── dashboardAction.js        ← Feature actions (feed, challenges, rewards)
│   │
│   ├── reducers/                     ← Redux reducers
│   │   ├── index.js                  ← Store creation (combineReducers + thunk)
│   │   ├── storeState.js             ← App-wide state
│   │   └── dashboardState.js         ← Feature state
│   │
│   ├── apiCalls/                     ← API service layer
│   │   ├── callApiClass.js           ← Main API caller (axios.all pattern)
│   │   ├── apiCallGetData.js         ← Request builder (FormData/JSON + auth header)
│   │   ├── ApiHeader.js              ← Authorization header manager
│   │   ├── ApiCall.js                ← POST with FormData
│   │   ├── AuthApi.js                ← Profile edit API
│   │   ├── apiUtils.js               ← Query param serializer
│   │   └── stripApi.js               ← Stripe integration
│   │
│   ├── services/
│   │   └── firebaseServices.js       ← FCM push notifications
│   │
│   ├── storage/
│   │   └── asyncStorage.js           ← AsyncStorage wrapper
│   │
│   ├── components/                   ← Reusable UI components
│   │   ├── modalComponents/          ← 24 modal components
│   │   ├── views/                    ← Cell components (feed, assessment, video)
│   │   ├── inputComponents/          ← Custom inputs
│   │   ├── wrapper/                  ← SafeArea wrapper
│   │   └── Tab/                      ← Custom tab component
│   │
│   ├── constants/                    ← API endpoints, reducer types, app values
│   ├── themes/                       ← Colors, fonts, common styles, images
│   ├── helpers/                      ← Responsive sizing, share utilities
│   ├── languages/                    ← i18n (English)
│   ├── utils/                        ← Validations, deep linking, helpers
│   └── Image/                        ← Assets (Lottie JSONs, sounds, images)
│
├── android/                          ← Native Android project
└── ios/                              ← Native iOS project
```

---

## 4. Entry Point and App Bootstrap

### Root Entry (`index.js`)

```javascript
// index.js -- the very first file React Native loads
import {AppRegistry} from 'react-native';
import App from './src';
import {name as appName} from './app.json';

AppRegistry.registerComponent(appName, () => App);
```

Simple. Delegates to `src/index.js`.

### The Actual App (`src/index.js`)

This is where the app initializes. Here's the full file with annotations:

```javascript
import 'react-native-gesture-handler';           // Must be first import (gesture handler requirement)
import React from 'react';
import {StyleSheet, View, Text, TextInput} from 'react-native';
import {SafeAreaProvider} from 'react-native-safe-area-context';
import {Provider} from 'react-redux';             // Redux store provider
import createStore from '@reducers';               // Store factory
import {ASYNC_KEYS, COMMON_DATA} from '@constants';
import {ToastAlert, LoadingIndicator, AlertModel} from '@components';  // Global overlays
import {COLORS} from '@themes';
import {changeLanguage} from '@languages';
import {AppContainer} from '@navigator';           // Navigation tree
import {StorageOperation} from '@storage';

const store = createStore();                       // Single Redux store

export default class App extends React.Component {
  constructor() {
    super();
    // Disable font scaling globally (accessibility trade-off)
    if (Text.defaultProps == null) Text.defaultProps = {};
    Text.defaultProps.allowFontScaling = false;
    if (TextInput.defaultProps == null) TextInput.defaultProps = {};
    TextInput.defaultProps.allowFontScaling = false;
  }

  componentDidMount() {
    // Load saved language preference
    StorageOperation.getData([ASYNC_KEYS.LANGUAGE]).then((response) => {
      if (response[0][1] != null) {
        changeLanguage(response[0][1]);
      } else {
        changeLanguage(COMMON_DATA.ENGLISH_LANG);
      }
    });
  }

  render() {
    console.disableYellowBox = true;  // Suppress warnings in dev
    return (
      <Provider store={store}>
        <View style={styles.container}>
          <SafeAreaProvider>
            <AppContainer />           {/* Entire navigation tree */}
          </SafeAreaProvider>
        </View>
        <LoadingIndicator />           {/* Global loading spinner (Redux-driven) */}
        <AlertModel />                 {/* Global alert dialog (Redux-driven) */}
        <ToastAlert />                 {/* Global toast notification (Redux-driven) */}
      </Provider>
    );
  }
}
```

**Key observations:**
1. **Class component** -- the entire app is class-based. Rebuild with functional components.
2. **Global overlays** are rendered outside `SafeAreaProvider` -- they sit on top of everything, driven by Redux state.
3. **Font scaling disabled** -- intentional but may want to reconsider for accessibility compliance.
4. **Language loaded from AsyncStorage** at startup.
5. **Path aliases** (`@reducers`, `@constants`, `@components`, `@themes`, `@languages`, `@navigator`, `@storage`) -- configured in Babel.

---

## 5. Navigation System

### Structure

```
NavigationContainer
└── Stack.Navigator (all screens)
    ├── SPLASH_SCREEN           → SplashScreen (headerShown: false)
    ├── WELCOME_SCREEN          → WelcomeScreen (headerShown: false)
    ├── LOGIN_SCREEN            → LoginScreen
    ├── MFA_OPTION_SCREEN       → MfaOptionScreen
    ├── OTP_SCREEN              → OtpScreen
    ├── SIGN_UP_SCREEN          → SignUpScreen
    ├── FORGOT_PASS_SCREEN      → ForgotPasswordScreen
    │
    ├── TAB_NAVIGATOR           → Bottom Tabs (headerShown: false)
    │   ├── FEED_TAB            → FeedHomeScreen
    │   ├── DISCOVER_TAB        → DiscoverHomeScreen
    │   ├── ACTIVITY_TAB        → ActivityScreen
    │   └── PROFILE_TAB         → ProfileScreen
    │
    ├── FEED_DETAIL_SCREEN      → FeedDetailScreen
    ├── FILTER_SCREEN           → FeedFilterScreen
    ├── FILTER_TAGS             → FeedTagFilterScreen
    ├── EDIT_PROFILE_SCREEN     → EditProfileScreen
    ├── EDIT_NAME               → EditNameScreen
    ├── CHANGE_PASSWORD         → ChangePasswordScreen
    ├── MY_FAVOURITE            → FavouriteScreen
    ├── SETTING                 → Settings
    ├── AVATAR_EDITOR           → AvatarEditorScreen (headerShown: false)
    ├── ASSESSMENT_HOME         → Assessment (headerShown: false)
    ├── ASSESSMENT_CHOICES      → AssessmentChoices
    ├── ASSESSMENT_RESULTS      → AssessmentResults (headerShown: false)
    ├── ASSESSMENT_LOADING      → LoadingScreen (headerShown: false)
    ├── Loader                  → Loader (headerShown: false)
    ├── WebView                 → WebViewComponent
    ├── DiscoverDetailScreen    → DiscoverDetailsScreen (transparent header)
    ├── VideoDetailsScreen      → VideoDetailsScreen (transparent header)
    ├── QuizScreen              → QuizScreen (page counter in header)
    ├── FinishQuiz              → FinishQuiz (headerShown: false)
    ├── VocabChallenge          → VocabScreen (headerShown: false)
    ├── Feed_Back               → FeedbackScreen (headerShown: false)
    ├── FinishReflectQuiz       → FinishReflectQuiz (headerShown: false)
    ├── ActvityScreen           → ActivityScreen (note: typo in name)
    ├── NotificationScreen      → NotificationScreen
    └── ChallengeQuiz           → ChallengeQuiz (page counter in header)
```

**Key observations:**
1. **Everything is in one Stack** -- no nested navigators except the TabNavigator.
2. **Screen names use UPPER_CASE** constants mixed with PascalCase strings -- inconsistent.
3. **There's a typo**: `ActvityScreen` (missing 'i').
4. **Header customization** happens inline per-screen with `options` props.
5. **Mock screens** exist (MockWelcomeScreen, MockLoginScreen) -- these were used for testing and are commented out.

### The Tab Navigator

The bottom tabs are: **Feed**, **Discover**, **Activity**, **Profile**. Each tab shows a different home screen, and deeper navigation (detail screens) happens in the parent Stack.

### Navigation Pattern

Screens navigate imperatively:

```javascript
// Example: Login → MFA
this.props.navigation.navigate('MFA_OPTION_SCREEN', {
  userData: responseData,
  mfaType: 'email'
});

// Example: Hard reset to Welcome (on logout)
navigation.reset({
  index: 0,
  routes: [{ name: 'WELCOME_SCREEN' }],
});
```

### Deep Linking

- URL scheme: `steamthestreet://`
- Handles challenge IDs and feed links from push notifications.
- Configured in `AndroidManifest.xml` and `Info.plist`.

---

## 6. State Management (Redux)

### Store Shape

The store has two top-level reducers:

```javascript
// src/reducers/index.js
const rootReducer = combineReducers({
  redState: redState,            // App-wide concerns
  dashboardState: dashboardState  // Feature/data concerns
});

return createStore(rootReducer, applyMiddleware(thunk));
```

### `redState` -- App-Wide State

```javascript
{
  resServer: "",                  // Generic API response
  isLoading: false,               // Global loading spinner
  resError: "",                   // Error message
  isOnline: false,                // Network connectivity
  userData: {},                   // Current user object
  alertData: {                    // Global alert dialog state
    isShowAlert: false,
    alertTitle: "Error",
    alertMsg: "Something went wrong",
    successBtnTitle: "OK",
    cancelBtnTitle: "Cancel"
  },
  toastData: {                    // Global toast state
    isShowToast: false,
    toastTitle: "Error",
    toastMsg: "Something went wrong"
  },
  searchData: {                   // Search state
    keyword: "",
    isForceSearch: false
  },
  isFirstTimeLogin: false,        // First-time user flag
  notificationList: null          // Notification list with pagination
}
```

### `dashboardState` -- Feature State

```javascript
{
  myProfile: null,                // User profile
  feedList: null,                 // Feed posts (paginated)
  feedDetails: null,              // Current feed detail
  feedLikeUnlike: null,           // Like/unlike response
  subjects: null,                 // Feed categories
  tags: null,                     // Tag list
  updateImage: null,              // Avatar update response
  tagList: null,                  // Assessment tags
  lessonDetails: null,            // Current lesson
  assessmentList: null,           // Assessment data
  leaderboardList: null,          // Leaderboard (paginated)
  badgesList: null,               // Badges (paginated)
  rewardsList: null,              // Rewards (paginated)
  avatarList: null,               // Avatars (paginated)
  badgesShare: null,              // Badge share response
  challenge: null,                // Current challenge
  listFeedback: null,             // Feedback options
  vocabList: null,                // Vocabulary list
  discoveryList: null             // Discovery/challenges list
}
```

### Action Pattern

Actions dispatch reducer types with data:

```javascript
// Example: Loading state
export const saveIsLoading = (isLoading) => (dispatch) => {
  dispatch({ type: RED_TYPE.API_LOADING, isLoading });
};

// Example: API call + dispatch
export const saveFeedList = (params, accessToken, navigation, page) => (dispatch) => {
  dispatch({ type: RED_TYPE.API_LOADING, isLoading: true });
  callApi([params], accessToken, navigation)
    .then((response) => {
      let resp = response[API_DATA.FEED_LIST];
      if (resp.success) {
        if (page === 1) {
          dispatch({ type: RED_TYPE.FEED_LIST, data: resp });
        } else {
          dispatch({ type: RED_TYPE.FEED_LIST_LOAD_MORE, data: resp });
        }
      }
      dispatch({ type: RED_TYPE.API_LOADING, isLoading: false });
    })
    .catch(() => {
      dispatch({ type: RED_TYPE.API_LOADING, isLoading: false });
    });
};
```

**Key observations:**
1. **Manual boilerplate** -- every action has loading/success/error dispatch patterns repeated.
2. **No normalization** -- API responses stored as-is.
3. **Pagination handled in reducers** by concatenating arrays (load more = spread old + new).
4. **Global loading state** -- one spinner for everything (no per-request loading).

### What to Change in the Rebuild

Replace with **Redux Toolkit (RTK)** or **Zustand + TanStack Query**:

```typescript
// RTK equivalent of the entire action + reducer pattern
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchFeed = createAsyncThunk('feed/fetch', async ({ page }, { rejectWithValue }) => {
  const response = await api.get('/feed/list', { params: { page } });
  if (!response.success) return rejectWithValue(response.message);
  return response;
});

const feedSlice = createSlice({
  name: 'feed',
  initialState: { items: [], loading: false, page: 1 },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchFeed.pending, (state) => { state.loading = true; })
      .addCase(fetchFeed.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.meta.arg.page === 1
          ? action.payload.data
          : [...state.items, ...action.payload.data];
      });
  },
});
```

---

## 7. API Layer

### Architecture

```
Screen Component
    ↓ dispatch(action)
Redux Action
    ↓ callApi([params], token, navigation)
callApiClass.js
    ↓ axios.all([...])
apiCallGetData.js
    ↓ axios({ method, url, data, headers })
Backend API (https://dashboard.steamthestreets.org/api/v1/)
```

### The Core API Caller

```javascript
// src/apiCalls/callApiClass.js
export function callApi(api_inputs, accessToken, navigation) {
  return new Promise((resolve, reject) => {
    var api_container = [];
    api_inputs.map((item, index) => {
      api_container.push(getResponseData(item, accessToken));

      if (index == api_inputs.length - 1) {
        axios.all(api_container)
          .then(axios.spread((...responses) => {
            const result = {};
            responses.map((item, index) => {
              result[api_inputs[index].url] = item;
            });
            resolve(result);
            checkTokenExpire(responses, navigation);  // Auto-logout on 401
          }))
          .catch((e) => reject(e));
      }
    });
  });
}
```

**Key observations:**
1. **Batch API calls** via `axios.all` -- can send multiple requests and wait for all.
2. **401 handling** -- if any response is 401, auto-logout and redirect to Welcome.
3. **Navigation passed to API layer** -- tight coupling between API and navigation (anti-pattern).
4. **No retry logic**, no request caching, no request deduplication.

### All API Endpoints

```javascript
// src/constants/apiData.js
export const API_DATA = {
  BASE_URL: "https://dashboard.steamthestreets.org/api/v1/",

  // Authentication
  LOGIN: "login",
  SIGNUP: "signup",
  LOGOUT: "logout",
  FORGOT_PASSWORD: "forgot",
  CHANGE_PASSWORD: "changepassword",
  OTP_GENERATE: "otp/generate",
  OTP_VERIFY: "otp/verify",
  DELETE_ACCOUNT: "user/delete",

  // Profile
  MY_PROFILE: "me",
  UPDATE_PROFILE: "updateme",
  CHECK_USERNAME_AVAILABLE: "check_username",
  UPDATE_AVATAR: "updateAvatarMultiple",

  // Feed
  FEED_LIST: "feed/list",
  FEED_DETAIL: "feed/detail",
  FEED_LIKE_UNLIKE: "feed/likeunlike",
  MYFEEDS: "feed/my_feeds",
  SUBJECTS: "subjects",
  TAGS: "tags",

  // Assessment
  ASSESSMENT_LIST: "assessment/list",
  ASSESSMENT_LIKE_UNLIKE: "assessment/likeunlike",
  MY_TAGS_LIST: "assessment/myTags",
  MY_TAGS_LIKE_UNLIKE: "tag/likeunlike",

  // Challenges / LMS
  CHALLENGE_LIST: "challenge/list",
  CHALLENGE_DETAILS: "challenge/detail",
  ACCEPT_CHALLENGE: "challenge/accept",
  CHALLENGELIKEUNLIKE: "challenge/likeunlike",
  MYCHALLENGES: "assessment/myChallenges",

  // Lessons
  LESSON_DETAILS: "lesson/detail",
  LESSON_COMPLETE: "lesson/completed/",
  LESSON_VIDEO_COMPLETE: "lesson/video-watch",
  LESSONVOCAB: "lesson/vocab/",

  // Quiz
  QUESTIONS: "questions",
  UPDATE_QUESTINS_ANSWER: "update-user-questions-data",
  RETAKE_QUIZ: "retake",

  // Reflect
  REFLECT_LIST: "reflects",
  UPDATE_REFLECT_DATA: "update-user-reflect-data",
  CHALLENGE_REFLECT_COMPLETED: "challenge-reflect/completed/",
  REFLECTRETAKE: "reflect-retake",

  // Gamification
  LEADERBOARD: "leaderboard",
  BADGESLIST: "badge-list",
  BADGESREDEEM: "badge-redeem",
  BADGESSHARE: "badge-share",
  REWARDSLIST: "reward-list",
  REWARDSREDEEM: "reward-purchased",
  AVATARLIST: "avatar-list",

  // Feedback
  FEEDBACKADD: "feedback-option-add",
  FEEDBACKLIST: "feedback-option-list/",

  // Notifications
  NOTIFICATION_LIST: "notification-list",
  NOTIFICATION_READABLE: "notification-readable/",
  USER_TOKEN: "user_token",
  CHANGE_NOTIFICATION_STATUS: "notification_on_off",
};
```

### Authorization

Every request includes:

```javascript
// src/apiCalls/ApiHeader.js
headers: {
  'Authorization': `Bearer ${accessToken}`,
  'app_version': '2.1.0',
  'app_build': '8',
  'Content-Type': 'application/json'  // or 'multipart/form-data' for file uploads
}
```

Token is stored in AsyncStorage under `ASYNC_KEYS.ACCESS_TOKEN` and loaded at app start.

---

## 8. Authentication and MFA Flow

### Login Sequence

```
User enters email + password
    ↓
POST /login → returns user object with `last_otp_verified` timestamp
    ↓
Is last_otp_verified within 15 days?
    ├── YES → Save user data to AsyncStorage → Navigate to TAB_NAVIGATOR
    └── NO  → Navigate to MFA_OPTION_SCREEN
                ↓
            User selects SMS or Email
                ↓
            POST /otp/generate/{type} → OTP sent
                ↓
            Navigate to OTP_SCREEN
                ↓
            User enters 6-digit OTP
                ↓
            POST /otp/verify → Validates OTP
                ↓
            Save user data → Navigate to TAB_NAVIGATOR
```

### Signup Sequence

Multi-step form using `react-native-swiper-flatlist`:

```
Step 1: Email, Phone (masked +1 999-999-9999), Terms checkbox
    ↓
Step 2: Birthday (must be 13+)
    ↓
Step 3: Name, Password, Confirm Password
    ↓
Step 4: Username (availability checked via API), Pronouns
    ↓
POST /signup → User created
    ↓
Save user data → Navigate to ASSESSMENT_HOME
```

### Token Lifecycle

```
Login/Signup → Receive access_token
    ↓
Store in AsyncStorage
    ↓
Every API call → Read from AsyncStorage → Attach to header
    ↓
On 401 response → Clear AsyncStorage → Reset navigation to WELCOME_SCREEN
```

### AsyncStorage Keys

```javascript
ASYNC_KEYS = {
  LANGUAGE: 'language',
  IS_LOGIN: 'isLogin',
  USER_DATA: 'user_data',
  ACCESS_TOKEN: 'access_token',
  FCM_TOKEN: 'FCM_TOKEN',
  IS_FIRST_LOGIN: 'isFirstTimeLogin',
  IS_FIRST_FEED: 'isFirstTimeFeed',
  IS_FIRST_TIME: 'isFirstTime'
}
```

---

## 9. Firebase and Notifications

### Current Implementation

```javascript
// src/services/firebaseServices.js
class FirebaseSvc {
  async firebasePushSetup() {
    // 1. Request notification permission
    const authStatus = await messaging().requestPermission({ sound: true });

    // 2. Get FCM token and store it
    if (enabled) {
      messaging().getToken().then((fcmToken) => {
        StorageOperation.setData([[ASYNC_KEYS.FCM_TOKEN, fcmToken]]);
      });
    }

    // 3. Create Android notification channel
    PushNotification.createChannel({
      channelId: 'default-channel-id',
      channelName: 'Default channel',
    });

    // 4. Set up message listeners
    this.setNotificationListner();
  }

  setNotificationListner() {
    // Foreground: show local notification
    messaging().onMessage(async (remoteMessage) => {
      this.handleLocalNotification(remoteMessage);
    });

    // Background: handler registered
    messaging().setBackgroundMessageHandler(async (remoteMessage) => {});
  }

  handleLocalNotification(remoteMessage) {
    PushNotification.localNotification({
      channelId: 'default-channel-id',
      title: remoteMessage.notification.title,
      message: remoteMessage.notification.body,
      userInfo: { ...remoteMessage.data, is_local_notification: true },
    });
  }
}
```

### What Needs to Change

| Current | Target |
|---------|--------|
| `@react-native-firebase/messaging` v14 | `@react-native-firebase/messaging` v22 |
| `react-native-push-notification` (deprecated) | `@notifee/react-native` |
| Namespaced API: `messaging().getToken()` | Modular API: same (messaging kept namespaced in RN Firebase) |
| No Android 13+ permission handling | Add `POST_NOTIFICATIONS` permission request |

### The @notifee Migration

Notifee is the replacement for `react-native-push-notification`. Key differences:

```typescript
// Old: react-native-push-notification
PushNotification.localNotification({
  channelId: 'default-channel-id',
  title: 'Hello',
  message: 'World',
});

// New: @notifee/react-native
import notifee from '@notifee/react-native';

await notifee.displayNotification({
  title: 'Hello',
  body: 'World',
  android: {
    channelId: 'default-channel-id',
    pressAction: { id: 'default' },
  },
});
```

Notifee provides:
- **Advanced triggers** (scheduled, repeating, interval-based)
- **Android 13+ (API 33) permission handling** (`POST_NOTIFICATIONS`)
- **Notification categories** with actions
- **Active notification management** (update, cancel specific notifications)
- **Background event handling** that works reliably

---

## 10. Every Screen Mapped

### Authentication Flow

| Screen | Purpose | Key Dependencies |
|--------|---------|-----------------|
| `SplashScreen` | Check login state, load user data, route to Welcome or Main | AsyncStorage |
| `WelcomeScreen` | Landing with "Sign Up" and "Login" buttons, plays opening sound on first launch | `react-native-sound` |
| `LoginScreen` | Email + password form, MFA check | Axios, AsyncStorage |
| `SignUpScreen` | 4-step swiper form (email/phone → birthday → name/password → username/pronouns) | `react-native-swiper-flatlist`, `react-native-mask-input` |
| `ForgotPasswordScreen` | Email input → password reset request | Axios |
| `MfaOptionScreen` | Choose SMS or Email for OTP, shows masked phone/email | `react-native-masked-text` (to be replaced) |
| `OtpScreen` | 6-digit OTP input with resend timer | Axios |

### Main App (Tab Screens)

| Screen | Purpose | Key Features |
|--------|---------|-------------|
| `FeedHomeScreen` | Social feed with posts | Pull-to-refresh, infinite scroll, subject/tag filters, like/share, search |
| `DiscoverHomeScreen` | Challenge/career path list | Challenge cards, accept modal, first-time tooltips |
| `ActivityScreen` | Gamification hub | Leaderboard, badges, rewards, avatar selection (tab views) |
| `ProfileScreen` | User profile | Career assessment results, favorites, settings, share/invite |

### Feed Sub-Screens

| Screen | Purpose |
|--------|---------|
| `FeedDetailScreen` | Full post view with images, YouTube embed, like/share |
| `FeedFilterScreen` | Subject filter selection |
| `FeedTagFilterScreen` | Career tag filter selection |

### Discover/LMS Sub-Screens

| Screen | Purpose |
|--------|---------|
| `DiscoverDetailsScreen` | Challenge overview, lesson carousel, step indicators, "Free First Steps" |
| `VideoDetailsScreen` | Video player (native + YouTube), completion tracking |
| `QuizScreen` | Questions (single, multiple, scale, fill-blank, free reply, true/false) |
| `FinishQuiz` | Quiz completion with score/animation |
| `ChallengeQuiz` | Reflect quiz (post-challenge reflection) |
| `FinishReflectQuiz` | Reflect completion |
| `VocabScreen` | Vocabulary challenge |
| `FeedbackScreen` | Post-challenge feedback form |

### Profile Sub-Screens

| Screen | Purpose |
|--------|---------|
| `EditProfileScreen` | Edit user info |
| `EditNameScreen` | Edit name specifically |
| `ChangePasswordScreen` | Change password |
| `FavouriteScreen` | Favorite feeds and careers (two tabs) |
| `Settings` | App settings, delete account |
| `AvatarEditorScreen` | Avatar customization |

### Assessment Flow

| Screen | Purpose |
|--------|---------|
| `AssessmentHome` | Career assessment intro/prompt |
| `AssessmentChoices` | Tag selection (like/dislike pairs), progress bar |
| `AssessmentResults` | Results based on selections |
| `LoadingScreen` | Animated transition during assessment processing |

### Utility Screens

| Screen | Purpose |
|--------|---------|
| `WebViewScreen` | In-app browser for terms, privacy, external links |
| `Loader` | Generic loading screen |
| `NotificationScreen` | Notification list with read/unread |

---

## 11. Component Library

### Modal Components (24 total)

| Component | Purpose | Redux-Driven? |
|-----------|---------|---------------|
| `AlertModel` | Global alert dialog | Yes (`alertData`) |
| `ToastAlert` | Global toast notification | Yes (`toastData`) |
| `LoadingIndicator` | Global loading spinner | Yes (`isLoading`) |
| `DatePickerModal` | Date selection | No |
| `BadgesModal` | Badge detail with share | No |
| `RewardsModal` | Reward detail, coin check, "how to earn" | No |
| `LeaderboardModal` | Leaderboard display | No |
| `SkipModal` | Skip confirmation | No |
| `TooltipDialog` | First-time user tooltips | No |
| `QuizModal` (correct) | Correct answer animation | No |
| `QuizModal` (wrong) | Wrong answer display | No |
| `QuizModal` (seeMore) | Additional content reveal | No |
| `AlertActionDialog` | Action confirmation | No |

### Cell/View Components

| Component | Used In | Purpose |
|-----------|---------|---------|
| `feedCell.js` | FeedHome | Feed post card |
| `AssessmentCell.js` | AssessmentChoices | Assessment tag pair |
| `DiscoverCell.js` | DiscoverHome | Challenge card |
| `VideoCell.js` | DiscoverDetails | Lesson video thumbnail |
| `favoriteCell.js` | FavouriteScreen | Favorite item card |
| `EnptyCell.js` | Various | Empty state display (note: typo "Enpty") |
| `YouTubeVideoView.js` | FeedDetail, VideoDetails | YouTube iframe player |

### Input Components

| Component | Purpose |
|-----------|---------|
| `TitleTextInput` | Text input with label, supports both `TextInputMask` and `MaskInput` |

### Wrapper Components

| Component | Purpose |
|-----------|---------|
| `SafeAreaWrapper` | Safe area handling with optional background image and status bar config |

---

## 12. Dependency Audit -- Every Package, Its Role, and Its Future

### Core Framework

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `react` | 17.0.2 | UI library | **Upgrade to 18.x or 19.x** |
| `react-native` | 0.65.1 | Mobile framework | **Upgrade to 0.76+** |

### Navigation

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `@react-navigation/native` | ^6.0.2 | Navigation core | **Upgrade to v7** or replace with Expo Router |
| `@react-navigation/stack` | ^6.0.7 | Stack navigator | Upgrade with core |
| `@react-navigation/bottom-tabs` | ^6.0.5 | Tab navigator | Upgrade with core |
| `react-native-screens` | 3.25.0 | Native screen optimization | Upgrade (New Arch compatible) |
| `react-native-safe-area-context` | ^3.3.0 | Safe area insets | Upgrade to v4+ |
| `react-native-gesture-handler` | ^1.10.3 | Gesture system | **Upgrade to v2+** (breaking changes) |

### State Management

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `redux` | ^4.1.1 | State container | Replace with **@reduxjs/toolkit** or **Zustand** |
| `react-redux` | ^7.2.4 | React bindings | Upgrade to v9+ if keeping Redux |
| `redux-thunk` | ^2.3.0 | Async middleware | Built into RTK; remove if switching |

### Firebase

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `@react-native-firebase/app` | ^14.10.0 | Firebase core | **Upgrade to v22** (Modular API) |
| `@react-native-firebase/auth` | ^14.10.0 | Firebase auth | **Upgrade to v22** |
| `@react-native-firebase/messaging` | ^14.10.0 | FCM messaging | **Upgrade to v22** |

### Notifications

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `react-native-push-notification` | ^8.1.1 | Local notifications | **Replace with @notifee/react-native** |
| `@react-native-community/push-notification-ios` | ^1.10.1 | iOS notifications | Remove (Notifee handles both platforms) |
| `react-native-notifications` | ^4.1.2 | Notifications (unused?) | **Remove** |

### UI Components

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `react-native-elements` | ^3.4.2 | UI toolkit (buttons, checkboxes) | Replace with **@rneui/themed** v4+ or a modern lib |
| `react-native-elements-universe` | ^0.0.0 | Extension of above | **Remove** (v0.0.0, likely unused) |
| `react-native-vector-icons` | ^9.0.0 | Icon library | Keep, upgrade if needed |
| `react-native-svg` | ^12.1.1 | SVG rendering | Upgrade to v15+ |

### Media

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `react-native-video` | ^5.2.1 | Native video player | **Upgrade to v6+** (complete rewrite with New Arch) |
| `react-native-video-player` | ^0.12.0 | Video player wrapper | Evaluate if still needed with v6 |
| `react-native-youtube-iframe` | ^2.2.2 | YouTube playback | **May be replaced** by native player per contract |
| `react-native-sound` | ^0.11.2 | Audio playback | Keep or replace with `expo-av` |
| `react-native-media-controls` | ^2.3.0 | Video controls | May be redundant with `react-native-video` v6 |
| `react-native-image-viewing` | ^0.2.0 | Fullscreen image viewer | Keep, check New Arch compatibility |

### Input & Forms

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `react-native-masked-text` | ^1.13.0 | Phone masking (MfaOptionScreen) | **Remove** -- replace with `react-native-mask-input` |
| `react-native-mask-input` | ^1.0.3 | Phone masking (SignUpScreen) | **Keep** -- this is the replacement |
| `react-native-keyboard-aware-scroll-view` | ^0.9.4 | Keyboard avoidance | Keep, check compatibility |
| `react-native-date-picker` | ^3.4.2 | Date selection | Keep, upgrade |

### Layout & Animation

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `lottie-react-native` | ^5.0.1 | Lottie animations | Upgrade to v6+ or use `expo` build-in |
| `react-native-swiper` | ^1.6.0 | Carousel/swiper | Evaluate: replace with `react-native-pager-view` |
| `react-native-swiper-flatlist` | ^3.0.14 | FlatList-based swiper (signup) | Keep or replace |
| `react-native-snap-carousel` | ^3.9.1 | Carousel (discover lessons) | **Replace** (unmaintained) -- use `react-native-reanimated-carousel` |
| `react-native-pager-view` | ^5.4.9 | Pager view | Keep, upgrade |
| `react-native-tab-view` | ^3.1.1 | Tab view (Activity screen) | Keep, upgrade |
| `react-native-step-indicator` | ^1.0.3 | Step progress indicator | Keep, check compatibility |
| `react-native-circular-progress` | ^1.3.7 | Circular progress bar | Keep, check compatibility |
| `react-native-slider` | ^0.11.0 | Slider input | **Replace** (deprecated) -- use `@react-native-community/slider` |

### Networking & Storage

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `axios` | ^0.21.1 | HTTP client | **Upgrade to v1.x** (security fixes) |
| `@react-native-async-storage/async-storage` | ^1.17.5 | Persistent storage | Keep, upgrade |
| `@react-native-community/netinfo` | ^6.0.0 | Network status | Keep, upgrade |

### Utility

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `moment` | ^2.29.1 | Date formatting | **Replace** with `date-fns` or `dayjs` (moment is 300KB+) |
| `react-native-hyperlink` | ^0.0.19 | Linkify text | Keep or replace |
| `react-native-i18n` | 2.0.14 | Internationalization | **Replace** with `react-i18next` or `expo-localization` |
| `react-native-permissions` | ^3.0.5 | Permission handling | Keep, upgrade |
| `react-native-webview` | ^11.16.0 | In-app browser | Keep, upgrade to v13+ |
| `react-native-view-shot` | ^3.1.2 | Screenshot capture | Keep, check compatibility |
| `patch-package` | ^8.0.0 | Patch dependencies | Keep |

### Dev Dependencies

| Package | Version | Role | Rebuild Action |
|---------|---------|------|---------------|
| `metro-react-native-babel-preset` | ^0.66.0 | Babel preset | Upgrade with RN |
| `react-native-codegen` | ^0.0.7 | Code generation | Part of new RN, remove explicit dep |
| `jest` | ^26.6.3 | Testing | Upgrade |
| `eslint` | 7.14.0 | Linting | Upgrade + add TypeScript rules |

---

## 13. Native Configuration

### Android (`android/`)

**Root `build.gradle`:**
- Kotlin: 1.6.10
- Gradle plugin: 4.1.0
- Google Services plugin: 4.3.13
- Build tools: 30.0.0
- Min SDK: 21 → **Will become 23+ (Android 6.0) with 0.74+**
- Compile SDK: 34
- Target SDK: 34

**App `build.gradle`:**
- Application ID: `com.steamthestreets.sts`
- Hermes: **disabled** (`enableHermes: false`) → **Enable in rebuild**
- Signing configs: Debug + Release keystores present
- Version: 2.1.0 (code 8)

**AndroidManifest.xml:**
- Permissions: `INTERNET`, `ACCESS_NETWORK_STATE`
- Deep link: `<data android:scheme="steamthestreet" />`
- Portrait-only: `android:screenOrientation="portrait"`
- Push notification receivers configured

### iOS (`ios/`)

**Podfile:**
- Platform: iOS 15.6
- Hermes: **disabled** → **Enable in rebuild**
- Flipper: **enabled** → **Remove in rebuild** (no longer supported in 0.74+)
- Pods: RNVectorIcons, react-native-video, Permission-Notifications

**Info.plist:**
- Display Name: "Steam The Streets"
- URL Scheme: `steamthestreet`
- Custom fonts: CooperHewitt, Feather, Fontisto, and more
- Permissions: Location (when in use + always), Photo Library, Camera
- Portrait-only

---

## 14. Patterns and Anti-Patterns in the Codebase

### Patterns to KEEP

1. **Path aliases** (`@components`, `@screens`, etc.) -- good for readability and refactoring.
2. **Centralized API endpoint constants** -- all endpoints in one file is easy to maintain.
3. **Global overlay components** (loading, alert, toast) -- clean pattern for app-wide feedback.
4. **AsyncStorage abstraction** -- wrapper around multi-get/set is useful.
5. **Screen numbering convention** (`0_AssessmentScreen`, `6_FeedScreen`) -- helps with navigation order.

### Anti-Patterns to FIX

1. **Class components everywhere** -- migrate to functional components with hooks.
2. **Navigation object passed to API layer** -- API calls should not know about navigation. Use interceptors or middleware for 401 handling.
3. **Global loading state** -- one `isLoading` for the entire app means you can't show independent loaders for different requests.
4. **Manual Redux boilerplate** -- every action repeats the loading/success/error pattern. Use RTK or TanStack Query.
5. **No TypeScript** -- all `.js` files. Add TypeScript for type safety, especially important for the New Architecture's Codegen.
6. **Inconsistent naming** -- `ActvityScreen` (typo), `EnptyCell` (typo), `QUESTINS` in API constants, mixed naming conventions for screen names.
7. **`console.disableYellowBox`** -- deprecated API, use `LogBox.ignoreAllLogs()` if needed.
8. **`axios.all` / `axios.spread`** -- deprecated axios patterns. Use `Promise.all` with standard axios calls.
9. **No error boundaries** -- a crash in any component crashes the entire app.
10. **Font scaling disabled globally** -- accessibility concern. Consider per-component control.

---

## 15. The Rebuild Roadmap

Based on the contract milestones and codebase analysis:

### Phase 1: Core Environment (Weeks 1-2)

- [ ] Initialize new RN project (0.76+ or latest stable)
- [ ] Enable Hermes + New Architecture
- [ ] Configure TypeScript
- [ ] Set up path aliases in `babel.config.js` and `tsconfig.json`
- [ ] Configure EAS Build for iOS + Android
- [ ] Set up development builds on iPhone + Android device
- [ ] Set up ESLint + Prettier

### Phase 2: Foundation (Weeks 3-4)

- [ ] Set up state management (RTK or Zustand + TanStack Query)
- [ ] Build API layer with interceptors (replace callApiClass pattern)
- [ ] Set up navigation (React Navigation v7 or Expo Router)
- [ ] Migrate AsyncStorage utilities
- [ ] Set up i18n (react-i18next or expo-localization)
- [ ] Build global overlay system (loading, alerts, toasts)
- [ ] Implement theming system

### Phase 3: Authentication (Week 5)

- [ ] Splash screen + auth state check
- [ ] Login screen
- [ ] MFA option screen (use `react-native-mask-input` only)
- [ ] OTP screen
- [ ] Signup multi-step flow
- [ ] Forgot password
- [ ] Token management with auto-refresh/logout

### Phase 4: Firebase & Notifications (Week 6)

- [ ] Upgrade to `@react-native-firebase/*` v22
- [ ] Implement Modular API for Firestore (if used)
- [ ] Set up `@notifee/react-native`
- [ ] FCM token management
- [ ] Foreground/background notification handling
- [ ] Android 13+ notification permission
- [ ] Deep link handling from notifications

### Phase 5: Main App Screens (Weeks 7-8)

- [ ] Feed (home, detail, filters, like/share)
- [ ] Discover (challenge list, details, lesson carousel)
- [ ] Video player (native player with custom controls)
- [ ] Quiz system (all question types)
- [ ] Activity (leaderboard, badges, rewards)
- [ ] Profile (view, edit, avatar, settings)
- [ ] Assessment flow
- [ ] Favorites
- [ ] Notifications list

### Phase 6: UI & QA (Weeks 7-8)

- [ ] Yoga 3.0 layout audit on every screen
- [ ] Test all row-reverse containers
- [ ] Test all flex layouts
- [ ] Fix RewardsModal async state (React 18 batching)
- [ ] Cross-device testing (various Android sizes + iPhone)

### Phase 7: Optional Enhancements (Weeks 8-10)

- [ ] Quiz validation fix (correct answer logic)
- [ ] Native video player (replace YouTube iframe)
- [ ] 80% watched rule enforcement
- [ ] Attribution query in onboarding
- [ ] "Free First Step" UI update
- [ ] Dashboard location-based search

---

> **Bottom line**: The STS codebase is a standard React Native 0.65.1 app with ~30 screens, Redux state management, a REST API backend, Firebase push notifications, and gamification features. The code is functional but dated (class components, manual Redux, deprecated libraries). The rebuild is not just a version bump -- it's a modernization that touches every file. The dependency audit above is your checklist: go through every package, decide keep/upgrade/replace, and validate New Architecture compatibility before writing feature code.
