---
id: TC-GS-USER-E2E-005-create-modal-form-structure
title: Create modal shows expected fields, access options, and master data options
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-14
  - TC-GS-USER-15
  - TC-GS-USER-25
  - TC-GS-USER-457
coverage:
  web: automated
---

# Create modal shows expected fields, access options, and master data options

## Prerequisites

- Login as Role: Total Control, entity is Client
- Position "Intern" exists in master data and no user uses it
- Custom Field "Blood Type" is defined as required
- Division "Finance" exists in master data

## Test Steps

1. Open the Filter Panel on the User List, open the Position dropdown, and verify "Intern" is not listed
2. Close the Filter Panel
3. Click `[+ User]` to open the Create modal
4. Verify the form shows Photo (optional), First Name, Last Name, Email, Position (optional), Division, Employee ID (optional), Access checkbox group, dynamic Custom Field "Blood Type", `[Cancel]`, and `[Save]`, and that First Name, Last Name, Email, Division, and Access are marked required
5. Verify the Access options list every product licensed for the Client plus "Global Settings"
6. Open the Position dropdown in the modal and verify "Intern" is listed
7. Fill the form with unique First Name, Last Name, and Email, and Division "Finance", leaving "Blood Type" empty
8. Select Access "Global Settings" only
9. Click `[Save]`
10. Verify submit is blocked because the required Custom Field "Blood Type" is empty, and no user is created

## Notes

- Source TC-14 lists "Full Name" and does not mark Division as required, while the PRD (user.md) defines First Name and Last Name as required and Division as required in the Create modal. This spec follows the PRD. See docs/coverage/GlobalSettingsUser.md.
- TC-15 for entity Principal, Distributor, and Partner is not covered here.
