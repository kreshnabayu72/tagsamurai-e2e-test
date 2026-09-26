---
id: TC-GS-USER-E2E-003-create-temporary-user
title: Create temporary user requires expiry date and shows it after save
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-65
  - TC-GS-USER-346
coverage:
  web: automated
---

# Create temporary user requires expiry date and shows it after save

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data
- Columns Temporary User and Temporary Until are visible via Setup Column

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with unique First Name, Last Name, and Email, and Division "Finance"
3. Select Access "Global Settings" only
4. Check `[x] Set as Temporary User` and leave Temporary Until empty
5. Click `[Save]`
6. Verify inline error "Temporary Until must not be empty" appears and the form is not submitted
7. Select Temporary Until as today + 7 days
8. Click `[Save]`
9. Verify success toast "User created successfully." appears
10. Verify the new user row appears in the User List
11. Verify Temporary User is Yes and Temporary Until shows the selected date, not "—"
12. Open the User Detail of the new user and verify it shows "Temporary until [date]" with the selected date
