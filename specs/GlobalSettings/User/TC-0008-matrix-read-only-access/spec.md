---
id: TC-0008-matrix-read-only-access
title: Role Matrix verification for Read Only persona
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
---

# Role Matrix verification for Read Only persona

## Prerequisites
- Login as Role: Read Only

## Test Steps

1. Navigate to Global Settings > User, sub-tab Login User
2. Verify Create User button `[+ User]` is hidden
3. Verify bulk selection checkboxes are hidden
4. Open row action menu `[⋯]` and verify Edit, Delete, and Resend options are hidden
5. Verify Toggle Active switch is disabled with tooltip "You don't have permission to edit"
