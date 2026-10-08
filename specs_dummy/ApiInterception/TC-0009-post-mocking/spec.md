---
id: TC-0009-post-mocking
title: Mock and assert POST API requests using browser.intercept
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
  mobile: automated
---

# Mock and assert POST API requests using browser.intercept

## Test Steps
1. Open API POST section in matchers page
2. Intercept POST /api/posts with mock response returning 201 status
3. Fill post title and post body inputs from fixture
4. Click submit POST button
5. Assert status badge displays 201 Created and response JSON contains new title
