---
id: TC-0012-direct-and-late-response
title: Intercept a direct (immediate) response and a late (delayed) response using Fixture data
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Intercept a direct (immediate) response and a late (delayed) response using Fixture data

## Test Steps
1. Open the API fetch section in the matchers page
2. Intercept GET /api/posts with mock posts fixture data
3. Click the fetch API button
4. Assert the status badge displays 200 OK and the immediate fixture items render
5. Update the mock response with an artificial 50ms delay
6. Click the fetch API button
7. Assert the loading indicator is visible while the request is held
8. Assert the status badge displays 200 OK and the delayed fixture items render
