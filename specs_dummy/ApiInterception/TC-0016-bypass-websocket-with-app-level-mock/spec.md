---
id: TC-0016-bypass-websocket-with-app-level-mock
title: Bypass a real WebSocket connection via an app-level test-only mock flag
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: unsupported
---

# Bypass a real WebSocket connection via an app-level test-only mock flag

**Why this isn't network-level interception like `Spectra.intercept()`:** a WebSocket connection
starts as an HTTP `Upgrade` handshake and then becomes a raw bidirectional frame stream — it's
never a single request/response CDP's `Fetch` domain can fulfill the way it fulfills a normal
`fetch()`/`XHR`/`EventSource` request. Chrome DevTools Protocol's WebSocket-related events
(`Network.webSocketCreated`, `webSocketFrameSent`/`webSocketFrameReceived`, etc.) are
observation-only — CDP has no command that mocks or rewrites a WS frame in flight. This is a
genuine protocol-level limitation, not a gap in this driver.

The practical workaround, and what this demo shows: the app itself checks for a test-only global
flag (`window.__mockWebSocketMessages`) and swaps in an in-memory fake socket when present,
instead of opening a real connection. `Spectra.browser.evaluate()` sets that flag before the app
connects. This is the same pattern used by Cypress/Playwright test suites for the same reason.

Mobile coverage is `unsupported`: React Native's WebSocket implementation is a native module,
not a page-context global reachable via a browser-style `evaluate()` call — a mobile equivalent
would need the RN app's own WebSocket client wrapper to support a comparable test-only bypass.

## Test Steps
1. Open the WebSocket matcher section
2. Set the app-level mock flag via browser.evaluate before the app connects
3. Click the connect button
4. Assert the connection status displays CONNECTED and two mocked frames render
5. Click the disconnect button
6. Assert the connection status displays DISCONNECTED
