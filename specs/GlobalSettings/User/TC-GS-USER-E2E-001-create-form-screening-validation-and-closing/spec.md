---
id: TC-GS-USER-E2E-001-create-form-screening-validation-and-closing
title: Create form screening, validation, and closing behavior
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-14
  - TC-GS-USER-15
  - TC-GS-USER-25
  - TC-GS-USER-457
  - TC-GS-USER-16
  - TC-GS-USER-17
  - TC-GS-USER-19
  - TC-GS-USER-192
  - TC-GS-USER-420
  - TC-GS-USER-18
  - TC-GS-USER-340
  - TC-GS-USER-347
  - TC-GS-USER-482
  - TC-GS-USER-431
  - TC-GS-USER-22
  - TC-GS-USER-487
coverage:
  web: automated
---

# Create form screening, validation, and closing behavior

## Prerequisites

- Login as Role: Total Control, entity is Client
- Position "Intern" exists in master data and no user uses it
- Division "Finance" exists in master data
- Custom Field "Blood Type" is defined as required
- User "Doni Pratama" already exists and its email is known
- Employee ID "EMP-001" is already used by another user in this entity

## Test Steps

### Screening

1. Open the Filter Panel on the User List, open the Position dropdown, and verify "Intern" is not listed
2. Close the Filter Panel
3. Click `[+ User]` to open the Create modal
4. Verify the form shows Photo (optional), First Name, Last Name, Email, Position (optional), Division, Employee ID (optional), Access checkbox group, User TAG (optional), Set as Temporary User, and Custom Field "Blood Type"
5. Verify First Name, Last Name, Email, Division, and Access are marked required
6. Verify the footer shows the checkbox "Stay on this form after submitting", `[Clear Field]`, and `[Submit]`, and that no `[Cancel]` button exists
7. Verify the Access options list every product licensed for the Client plus "Global Settings"
8. Open the Position dropdown in the modal and verify "Intern" is listed
9. Check `[x] Set as Temporary User`, verify the Temporary Until field appears, then uncheck it

### Validation

10. Click `[Submit]` without filling anything
11. Verify submit is blocked and inline errors appear: "First Name must not be empty", "Last Name must not be empty", "Email must not be empty", "Division must not be empty", "Access must not be empty", and "Blood Type must not be empty" for the required Custom Field
12. Fill First Name, Last Name, Division "Finance", Email "budi.santoso@@invalid", and select Access "Global Settings"
13. Click `[Submit]` and verify inline error "Invalid email format" appears and the form is not submitted
14. Replace Email with a unique valid email and uncheck every Access option
15. Click `[Submit]` and verify inline error "Access must not be empty" appears and the form is not submitted
16. Select Access "Global Settings" so every field is valid except Custom Field "Blood Type", which stays empty
17. Click `[Submit]` and verify inline error "Blood Type must not be empty" appears as the only error and the form is not submitted
18. Fill "Blood Type", then type "Budi 😊" into First Name and Last Name and verify the emoji never enters the fields and no error appears
19. Type "Budi-O'Neil" into First Name and Last Name and verify the symbols are accepted and remain in both fields
20. Restore valid values for First Name and Last Name
21. For each of First Name, Last Name, and Employee ID, enter 121 characters while the other fields stay valid, click `[Submit]`, and verify inline error "Max. 120 characters" appears on that field and submit is blocked
22. Restore values of at most 120 characters
23. Replace Email with the existing email of "Doni Pratama" and click `[Submit]`
24. Verify inline error "Email already exists" appears and the data is not saved
25. Replace Email with a unique valid email, enter Employee ID "EMP-001", and click `[Submit]`
26. Verify inline error "Employee ID already exists" appears and the data is not saved
27. Click `[Clear Field]` and verify every field, including Custom Field "Blood Type", is emptied and the modal stays open
28. Click `[Submit]` on the empty form to raise validation errors and verify red borders and inline errors appear
29. Click `[Clear Field]` and verify every field is emptied, red borders and inline errors are gone, and the modal stays open

### Closing

30. Fill First Name with a value
31. Click `✕`
32. Verify dialog "You have unsaved changes. Are you sure you want to leave?" appears with `[Leave]` and `[Cancel]`
33. Click `[Cancel]` on the dialog and verify the dialog closes, the modal stays open, and First Name still holds the value
34. Click `✕` again and click `[Leave]` on the dialog
35. Verify the modal closes and no new user was created in the User List by any submit above
36. Click `[+ User]` again and verify all fields are empty, meaning no draft was saved
37. Click `✕` without filling any field
38. Verify the modal closes immediately and the unsaved changes dialog does not appear

## Notes

- One spec covers two modal sessions. Steps 3 to 34 run in the first session, which ends with `[Leave]`. Steps 36 to 38 run in a second session, because the clean-close case needs a freshly opened modal.
- TC-GS-USER-15 is split across two specs. The Client half is covered here and the Principal half is covered in TC-GS-USER-E2E-003.
- TC-GS-USER-420 is split across two specs. The 121 character rejection is covered here and the exact 120 character acceptance is covered in TC-GS-USER-E2E-002.
- A required Custom Field is validated like the other required fields, so its error also appears on an empty submit (step 11) and is verified alone in step 17. The copy follows the global pattern "[Field] must not be empty" shown after Submit (prd-conventions.md, error message conventions), and TC-GS-USER-16 and TC-GS-USER-25 state it explicitly.
- The close action is `✕` in the header. `Esc` also closes the modal. The Create modal has no `[Cancel]` button (prd-conventions.md section 24.1). `[Cancel]` exists only on the unsaved changes dialog.
- The emoji rule follows prd-conventions.md "Karakter yang Diizinkan (Name Fields)": only emoji is blocked, symbols are allowed.
- No data is created by this spec, so it needs no cleanup.
