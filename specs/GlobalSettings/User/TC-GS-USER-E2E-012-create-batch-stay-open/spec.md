---
id: TC-GS-USER-E2E-012-create-batch-stay-open
title: Create another user keeps the modal open for consecutive creation
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-21
coverage:
  web: automated
---

# Create another user keeps the modal open for consecutive creation

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with First Name "Agus", Last Name "Setiawan", unique Email, and Division "Finance"
3. Select Access "Global Settings" only
4. Check "Stay on this form after submitting"
5. Click `[Save]`
6. Verify success toast "User created successfully." appears and the modal stays open with an empty form
7. Fill the form with First Name "Maya", Last Name "Putri", unique Email, and Division "Finance"
8. Select Access "Global Settings" only
9. Uncheck "Stay on this form after submitting" and click `[Save]`
10. Verify the modal closes
11. Verify the User List contains both "Agus Setiawan" and "Maya Putri"
