---
id: TC-GS-USER-E2E-009-create-clear-field
title: Clear Field empties the Create modal and resets validation errors
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-347
  - TC-GS-USER-482
coverage:
  web: automated
---

# Clear Field empties the Create modal and resets validation errors

## Prerequisites

- Login as Role: Total Control
- Custom Field "Blood Type" is defined and visible in the Create modal
- Division "Finance" exists in master data

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with unique First Name, Last Name, and Email, Division "Finance", and a value for Custom Field "Blood Type"
3. Click `[Clear Field]`
4. Verify every field, including Custom Field "Blood Type", is emptied and the modal stays open
5. Click `[Save]` to trigger validation errors
6. Verify red borders and inline errors appear on the required fields
7. Click `[Clear Field]`
8. Verify every field is emptied, red borders and inline errors are gone, and the modal stays open
9. Verify no new user was created in the User List
