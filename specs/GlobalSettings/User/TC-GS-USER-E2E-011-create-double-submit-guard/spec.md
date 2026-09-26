---
id: TC-GS-USER-E2E-011-create-double-submit-guard
title: Create user Save button shows saving state and blocks double submit
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-191
  - TC-GS-USER-440
coverage:
  web: automated
---

# Create user Save button shows saving state and blocks double submit

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data
- The Create request is delayed so the saving state is observable
- The first Create attempt is made to fail with a server error, and the second attempt succeeds

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with unique First Name, Last Name, and Email, and Division "Finance"
3. Select Access "Global Settings" only
4. Click `[Save]` while the Create request fails with a server error
5. Verify `[Save]` shows a loading spinner and is disabled while the request is pending, then becomes enabled again after the failure
6. Verify the modal stays open with the filled values and no user is created
7. Double-click `[Save]` in quick succession while the Create request succeeds
8. Verify `[Save]` shows a loading spinner and is disabled while the request is pending
9. Wait for the response to finish
10. Verify success toast "User created successfully." appears and the modal closes
11. Verify the User List contains exactly 1 row for the created user

## Notes

- Timing sensitive. The script must delay the Create response deterministically instead of relying on backend speed.
- The server error in step 4 cannot be triggered safely against the real backend, so it is simulated by the script.
