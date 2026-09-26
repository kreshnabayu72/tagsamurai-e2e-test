---
id: TC-GS-USER-E2E-001-create-user-full-fields-global-settings
title: Create user with all fields filled and Global Settings access
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-13
  - TC-GS-USER-20
  - TC-GS-USER-469
  - TC-GS-USER-471
  - TC-GS-USER-473
coverage:
  web: automated
---

# Create user with all fields filled and Global Settings access

## Prerequisites

- Login as Role: Total Control
- Position "Staff" and Division "Finance" exist in master data
- Photo file smaller than 1MB is available
- Columns Position, Division, Employee ID, Temporary User, Temporary Until, and TAG are visible via Setup Column

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with First Name "Budi", Last Name "Santoso", unique Email, Position "Staff", Division "Finance", and unique Employee ID
3. Upload a photo smaller than 1MB
4. Select Access "Global Settings" only
5. Click `[Save]`
6. Verify success toast "User created successfully." appears
7. Verify the new user row appears in the User List
8. Verify the new row shows badge "Pending Activation", Toggle Active [Global] is ON, and role is User Basic
9. Verify the Access column shows exactly 1 dark badge with the text "Global Settings"
10. Verify Position is "Staff", Division is "Finance", Employee ID matches the input, Temporary User is No, Temporary Until is "—", and TAG is "—"
11. Verify the Name column shows the uploaded photo thumbnail, not the initials avatar

## Notes

- TC-GS-USER-13 also expects the invitation email to be sent. Email delivery is outside the browser, so this spec does not assert it.
- TC-GS-USER-13 also expects no in-app notification to be triggered for other users. That needs a second user session and is not covered here.
