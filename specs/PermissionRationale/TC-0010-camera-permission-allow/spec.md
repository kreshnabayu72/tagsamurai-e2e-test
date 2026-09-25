---
id: TC-0010-camera-permission-allow
title: Confirm custom rationale dialog Allow triggers real permission request and grants camera access
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: unsupported
  mobile: automated
---

# Confirm custom rationale dialog Allow triggers real permission request and grants camera access

## Test Steps
1. Navigate to the permission rationale demo route
2. Assert the initial status is "Not requested"
3. Click the request camera permission button
4. Assert the custom rationale dialog appears
5. Click Allow
6. Grant the real camera permission on demand
7. Assert the status becomes "Granted"
8. Return to the home screen
