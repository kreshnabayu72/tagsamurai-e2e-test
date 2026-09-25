---
id: TC-0008-fetch-mocking
title: Mock and assert GET API requests using browser.intercept
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Mock and assert GET API requests using browser.intercept

## Test Steps
1. Open API fetch section in matchers page
2. Intercept GET /api/posts with mock posts fixture data
3. Click fetch API button
4. Assert status badge displays 200 OK and rendered items match fixture
5. Update mock response dynamically and verify updated items rendered
