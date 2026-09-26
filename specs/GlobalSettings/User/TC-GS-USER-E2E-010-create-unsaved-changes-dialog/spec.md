---
id: TC-GS-USER-E2E-010-create-unsaved-changes-dialog
title: Create modal unsaved changes dialog for clean close, Cancel, and Leave
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-22
  - TC-GS-USER-431
  - TC-GS-USER-487
coverage:
  web: automated
---

# Create modal unsaved changes dialog for clean close, Cancel, and Leave

## Prerequisites

- Login as Role: Total Control

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Click `[Cancel]` without filling any field
3. Verify the modal closes immediately and the unsaved changes dialog does not appear
4. Click `[+ User]` to open the Create modal
5. Fill First Name with a value
6. Click `X`
7. Verify dialog "You have unsaved changes. Are you sure you want to leave?" appears with `[Leave]` and `[Cancel]`
8. Click `[Cancel]` on the dialog
9. Verify the dialog closes, the modal stays open, and First Name still holds the value
10. Click `[Cancel]` on the modal and verify the same dialog appears
11. Click `[Leave]` on the dialog
12. Verify the modal closes and no new user was created
13. Click `[+ User]` again and verify all fields are empty, meaning no draft was saved
