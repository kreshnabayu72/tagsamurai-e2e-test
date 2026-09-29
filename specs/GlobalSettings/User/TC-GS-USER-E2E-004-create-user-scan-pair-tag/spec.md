---
id: TC-GS-USER-E2E-004-create-user-scan-pair-tag
title: Create user with Scan and Pair TAG shows a verified TAG in the list
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-475
coverage:
  web: automated
---

# Create user with Scan and Pair TAG shows a verified TAG in the list

## Prerequisites

- Login as Role: Total Control
- Column TAG is visible via Setup Column
- TAG "RFID-00321" is registered for this client and is not paired to any user
- Division "Finance" exists in master data
- The test environment can simulate an RFID scan, because a browser cannot perform a hardware scan
- TAG "RFID-00321" is unpaired at the start of every run, and cleanup unpairs it again

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill First Name "Taufik", Last Name "Hidayat", unique Email, and Division "Finance"
3. Select Access "Global Settings" only
4. Scan and pair TAG "RFID-00321"
5. Verify the pairing success toast appears
6. Click `[Submit]`
7. Verify the new user row appears in the User List
8. Verify the TAG column shows "RFID-00321"
9. Verify the TAG shows a green "Verified" badge

## Notes

- The TAG scan is a hardware RFID scan, which a browser cannot perform. The scan simulation is requested from the FE team in Prerequisites.
- TC-GS-USER-343, 344, and 345 (scan validation failures) are covered by the frontend test cases (TC-GS-USER-FE-047, 048, 049).
- The user is deleted in cleanup.
