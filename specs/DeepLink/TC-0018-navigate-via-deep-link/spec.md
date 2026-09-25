---
id: TC-0018-navigate-via-deep-link
title: Navigate directly to a native route via Spectra.navigate() and an Android deep link
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: unsupported
  mobile: automated
---

# Navigate directly to a native route via Spectra.navigate() and an Android deep link

On Android, `Spectra.navigate(uri)` runs `adb shell am start -a android.intent.action.VIEW -d
<uri>` against the app's own registered scheme (`testspectra-demo://`, declared in
`app.json`/`AndroidManifest.xml`) — jumping straight to a route without walking through the UI
first, the same way a push notification or an external link would open the app in production.

Web coverage is `unsupported`: on web, `Spectra.navigate()` already does the equivalent thing
via a normal URL (see any other TC's `browser.url(...)`/`Spectra.navigate(...)` call) — there's no
separate "deep link" concept to demonstrate there.

## Test Steps
1. Wait for the app home screen to finish booting
2. Navigate via a deep link to the target route without query params
3. Assert the target marker is shown and the received message is "(none)"
4. Navigate via a deep link carrying a query-param message
5. Assert the received message matches the deep-link param
6. Return to the home screen
