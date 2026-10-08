---
id: TC-0013-real-network-call-recorded
title: Make a genuine (non-intercepted) network call and verify it is recorded
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Make a genuine (non-intercepted) network call and verify it is recorded

## Test Steps
1. Open the API fetch section in the matchers page
2. Clear any active mocks left by a previous test
3. Enter a real (non-intercepted) demo-server todo endpoint URL with a cache-busting query param
4. Click the fetch API button
5. Assert the status badge displays 200 OK
6. Assert the network report records the genuine call with status 200
