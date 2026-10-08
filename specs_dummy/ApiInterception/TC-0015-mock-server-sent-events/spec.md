---
id: TC-0015-mock-server-sent-events
title: Mock a Server-Sent Events (EventSource) stream via the existing network-intercept engine
priority: Medium
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: unsupported
---

# Mock a Server-Sent Events (EventSource) stream via the existing network-intercept engine

Mobile coverage is `unsupported`: React Native has no built-in `EventSource` — a real project
targeting mobile would add a userland SSE client library, at which point whether/how it's
mockable depends entirely on that library's own networking implementation, not something
TestSpectra's driver can generalize over.

## Test Steps
1. Open the SSE matcher section
2. Intercept GET /api/sse-feed with a text/event-stream mock body
3. Click the connect button
4. Assert two SSE messages render
5. Assert the first message contains "hello from mock SSE" and the last contains "second event"
