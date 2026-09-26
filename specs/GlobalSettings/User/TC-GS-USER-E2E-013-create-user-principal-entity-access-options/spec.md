---
id: TC-GS-USER-E2E-013-create-user-principal-entity-access-options
title: Create user in Principal entity limits Access options to Admin Console
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-15
  - TC-GS-USER-467
coverage:
  web: automated
---

# Create user in Principal entity limits Access options to Admin Console

## Prerequisites

- Login as Role: Total Control, entity is Principal
- A Division exists in master data of the Principal entity

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Verify the Access options list only "Admin Console" and "Global Settings"
3. Verify the Client products "FAMS", "SAMS", and "SIEM" are not listed
4. Fill the form with First Name "Rendy", Last Name "Kurniawan", unique Email, and an existing Division
5. Select Access "Admin Console" only
6. Click `[Save]`
7. Verify success toast "User created successfully." appears
8. Verify the new user row appears in the User List
9. Verify the Access column shows exactly 1 dark badge with the text "Admin Console"
10. Verify the role of the new user is User Basic

## Notes

- TC-GS-USER-15 is split across two specs. The Client half is covered in TC-GS-USER-E2E-005 and the Principal, Distributor, and Partner half is covered here. Only entity Principal is used. Distributor and Partner are not covered.
