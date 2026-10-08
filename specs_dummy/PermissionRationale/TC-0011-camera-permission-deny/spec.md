---
id: TC-0011-camera-permission-deny
title: Confirm custom rationale dialog Deny never triggers the real permission request
priority: High
caseType: Negative
status: ready-for-automation
coverage:
  web: unsupported
  mobile: automated
---

# Confirm custom rationale dialog Deny never triggers the real permission request

## Test Steps
1. Navigate to the permission rationale demo route
2. Click the request camera permission button
3. Assert the custom rationale dialog appears
4. Click Deny
5. Assert the status reflects the dialog's own decision without any real permission request
6. Return to the home screen
