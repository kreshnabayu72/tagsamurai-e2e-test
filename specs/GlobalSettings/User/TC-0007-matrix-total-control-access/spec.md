---
id: TC-0007-matrix-total-control-access
title: Role Matrix verification for Total Control persona
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
---

# Role Matrix verification for Total Control persona

## Prerequisites
- Login as Role: Total Control

## Test Steps

1. Navigate to Global Settings > User, sub-tab Login User
2. Verify Create User button `[+ User]` is visible and enabled
3. Verify table header and row selection checkboxes are visible and enabled
4. Verify Toggle Active switch on user rows is enabled
5. Open row action menu `[⋯]` and verify Edit, Delete, and Resend options are visible and enabled
