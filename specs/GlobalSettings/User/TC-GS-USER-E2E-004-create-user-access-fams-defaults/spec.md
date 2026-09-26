---
id: TC-GS-USER-E2E-004-create-user-access-fams-defaults
title: Create user with FAMS access only keeps baseline defaults
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-341
  - TC-GS-USER-489
coverage:
  web: automated
---

# Create user with FAMS access only keeps baseline defaults

## Prerequisites

- Login as Role: Total Control
- Client is licensed for Fixed Asset (FAMS)
- Division "Finance" exists in master data
- Columns Position, Employee ID, and Temporary User are visible via Setup Column

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with First Name "Wulan", Last Name "Sari", unique Email, and Division "Finance"
3. Select Access "FAMS" only, without Global Settings
4. Click `[Save]`
5. Verify success toast "User created successfully." appears
6. Verify the new user row appears in the User List
7. Verify Toggle Active [Global] is ON
8. Verify the Access column shows exactly 1 dark badge with the text "Fixed Asset", not "FAMS"
9. Verify Temporary User is No, and Position and Employee ID are "—"
10. Open the User Detail of the new user, open Tab Role, and verify the FAMS role is "User Basic"
