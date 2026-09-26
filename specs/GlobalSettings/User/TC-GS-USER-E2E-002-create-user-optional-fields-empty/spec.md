---
id: TC-GS-USER-E2E-002-create-user-optional-fields-empty
title: Create user with only required fields leaves optional fields empty
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-468
  - TC-GS-USER-470
  - TC-GS-USER-472
  - TC-GS-USER-474
  - TC-GS-USER-476
coverage:
  web: automated
---

# Create user with only required fields leaves optional fields empty

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data
- Columns Position, Employee ID, Temporary User, Temporary Until, and TAG are visible via Setup Column

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with First Name "Dewi", Last Name "Anggraini", unique Email, and Division "Finance"
3. Select Access "Global Settings" only
4. Leave Position, Employee ID, photo, Temporary User, and TAG untouched
5. Click `[Save]`
6. Verify success toast "User created successfully." appears
7. Verify the new user row appears in the User List
8. Verify Position is "—" and Employee ID is "—"
9. Verify TAG is "—"
10. Verify Temporary User is No and Temporary Until is "—"
11. Verify the Name column shows the default initials avatar "DA", not a photo
