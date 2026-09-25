---
id: TC-0021-seed-authenticated-session
title: Seed an authenticated session via Spectra.seedSession() instead of the real login UI
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Seed an authenticated session via Spectra.seedSession() instead of the real login UI

## Test Steps
1. Call the `seedSession` support action — logs in via a direct API call instead of walking
   through a login form (web: host-side `fetch()` + `Spectra.browser.setCookies()` applies the
   resulting `HttpOnly` cookie to the browser; mobile: a deep link asks the app to log itself in
   against a known test account and persist the result itself)
2. Assert the app reflects an authenticated state
