---
id: TC-GS-USER-E2E-007-create-validation-length-and-characters
title: Create user blocks emoji input and enforces 120 character limit
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-192
  - TC-GS-USER-420
coverage:
  web: automated
---

# Create user blocks emoji input and enforces 120 character limit

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Type "Budi 😊" into First Name and verify the emoji never enters the field and no error appears
3. Type "Budi 😊" into Last Name and verify the emoji never enters the field and no error appears
4. Type "Budi-O'Neil" into First Name and Last Name and verify the symbols are accepted and remain in both fields
5. Clear both fields
6. Fill the form with valid unique values for every required field, and Access "Global Settings"
7. For each of First Name, Last Name, and Employee ID, enter 121 characters while the other fields stay valid, click `[Save]`, and verify inline error "Max. 120 characters" appears on that field and submit is blocked
8. Set First Name, Last Name, and Employee ID to exactly 120 characters each
9. Click `[Save]`
10. Verify success toast "User created successfully." appears

## Notes

- Per prd-conventions.md "Karakter yang Diizinkan (Name Fields)", only emoji is blocked at the input. All other printable characters, including symbols, are allowed, so step 4 verifies symbols are not blocked.
