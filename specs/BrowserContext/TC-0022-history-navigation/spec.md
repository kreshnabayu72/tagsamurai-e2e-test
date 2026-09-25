---
id: TC-0022-history-navigation
title: Navigate browser/app history with Spectra.back(), forward(), and refresh()
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Navigate browser/app history with Spectra.back(), forward(), and refresh()

## Test Steps

### Web
1. Navigate to two distinct real URLs in sequence, each pushing its own genuine browser history
   entry (this demo app's in-app hash navigation does not — see the test's own comment)
2. Verify `Spectra.back()` returns to the previously visited URL
3. Verify `Spectra.forward()` replays the entry just undone
4. Verify `Spectra.refresh()` reloads the document while the current URL survives

### Mobile
1. Navigate to a native route via deep link
2. Verify `Spectra.back()` (Android hardware back key) pops back to the Home screen

`Spectra.forward()`/`Spectra.refresh()` have no native-app equivalent (no browser history, no page
reload) and are intentional no-ops on Android — only `Spectra.back()` is exercised on mobile.
