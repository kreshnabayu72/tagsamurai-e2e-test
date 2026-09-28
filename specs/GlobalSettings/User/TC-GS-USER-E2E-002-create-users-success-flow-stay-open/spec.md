---
id: TC-GS-USER-E2E-002-create-users-success-flow-stay-open
title: Create users successfully with different access, optional fields, and temporary user in one session
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-13
  - TC-GS-USER-20
  - TC-GS-USER-469
  - TC-GS-USER-471
  - TC-GS-USER-473
  - TC-GS-USER-191
  - TC-GS-USER-440
  - TC-GS-USER-341
  - TC-GS-USER-489
  - TC-GS-USER-468
  - TC-GS-USER-470
  - TC-GS-USER-472
  - TC-GS-USER-474
  - TC-GS-USER-476
  - TC-GS-USER-420
  - TC-GS-USER-65
  - TC-GS-USER-346
  - TC-GS-USER-21
coverage:
  web: automated
---

# Create users successfully with different access, optional fields, and temporary user in one session

## Prerequisites

- Login as Role: Total Control, entity is Client
- Client is licensed for Fixed Asset (FAMS)
- Position "Staff" and Division "Finance" exist in master data
- Custom Field "Blood Type" is defined as required, so every create fills it
- Photo file smaller than 1MB is available
- Columns Toggle Active, Position, Division, Employee ID, Access, Temporary User, Temporary Until, and TAG are visible via Setup Column
- The Create request of the first user is delayed, and its first attempt is made to fail with a server error

## Test Steps

### User 1: all fields filled, Global Settings access

1. Click `[+ User]` to open the Create modal
2. Check "Stay on this form after submitting"
3. Fill First Name "Budi", Last Name "Santoso", unique Email, Position "Staff", Division "Finance", unique Employee ID, and "Blood Type"
4. Upload a photo smaller than 1MB and select Access "Global Settings" only
5. Click `[Submit]` while the Create request fails with a server error
6. Verify `[Submit]` shows a loading spinner and is disabled while the request is pending, then becomes enabled again after the failure
7. Verify the modal stays open with the filled values
8. Double-click `[Submit]` in quick succession while the Create request succeeds
9. Verify `[Submit]` shows a loading spinner and is disabled while the request is pending
10. Verify success toast "User created successfully." appears and the modal stays open with an empty form

### User 2: FAMS access, required fields only, 120 character names

11. Fill First Name with exactly 120 characters, Last Name with exactly 120 characters, unique Email, Division "Finance", and "Blood Type"
12. Leave Position, Employee ID, photo, Set as Temporary User, and User TAG untouched
13. Select Access "FAMS" only
14. Click `[Submit]`
15. Verify success toast "User created successfully." appears and the modal stays open with an empty form

### User 3: temporary user, closes the modal

16. Fill unique First Name, Last Name, and Email, Division "Finance", and "Blood Type"
17. Select Access "Global Settings" only
18. Check `[x] Set as Temporary User` and leave Temporary Until empty
19. Click `[Submit]` and verify inline error "Temporary Until must not be empty" appears and the form is not submitted
20. Select Temporary Until as today + 7 days
21. Uncheck "Stay on this form after submitting"
22. Click `[Submit]`
23. Verify success toast "User created successfully." appears and the modal closes

### Verification in the User List

24. Verify the User List contains exactly 1 row for User 1
25. Verify User 1 shows badge "Pending Activation", Toggle Active [Global] ON, role User Basic, and exactly 1 dark Access badge "Global Settings"
26. Verify User 1 shows Position "Staff", Division "Finance", Employee ID as input, Temporary User No, Temporary Until "—", TAG "—", and the uploaded photo thumbnail instead of the initials avatar
27. Verify User 2 shows exactly 1 dark Access badge "Fixed Asset", not "FAMS", and Toggle Active [Global] ON
28. Verify User 2 shows Position "—", Employee ID "—", TAG "—", Temporary User No, Temporary Until "—", and the default initials avatar
29. Open the User Detail of User 2, open Tab Role, and verify the FAMS role is "User Basic"
30. Verify User 3 shows Temporary User Yes and Temporary Until as the selected date, not "—"
31. Open the User Detail of User 3 and verify it shows "Temporary until [date]" with the selected date

## Notes

- One spec covers one modal session. "Stay on this form after submitting" stays checked for Users 1 and 2 so the modal is opened only once, and it is unchecked for User 3 so the last submit closes the modal.
- The script must not assume the Stay checkbox keeps its state after the modal is closed.
- The server error in step 5 cannot be triggered safely against the real backend, so the script simulates it. The interception must only affect the first user and must be cleared afterward.
- TC-GS-USER-420 is split across two specs. The exact 120 character acceptance is covered here and the 121 character rejection is covered in TC-GS-USER-E2E-001.
- TC-GS-USER-13 also expects the invitation email to be sent. Email delivery is outside the browser, so this spec does not assert it. It also expects no in-app notification for other users, which needs a second user session and is not covered here.
- The double-click in step 8 is timing sensitive. The script must delay the Create response deterministically.
- All 3 users must be deleted in cleanup, even if the spec fails midway.
