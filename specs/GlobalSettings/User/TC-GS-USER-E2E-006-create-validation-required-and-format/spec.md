---
id: TC-GS-USER-E2E-006-create-validation-required-and-format
title: Create user validation for empty required fields, invalid email, and missing access
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-16
  - TC-GS-USER-17
  - TC-GS-USER-19
coverage:
  web: automated
---

# Create user validation for empty required fields, invalid email, and missing access

## Prerequisites

- Login as Role: Total Control
- Division "Finance" exists in master data

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Click `[Save]` without filling anything
3. Verify submit is blocked and inline errors appear: "First Name must not be empty", "Last Name must not be empty", "Email must not be empty", "Division must not be empty", "Access must not be empty"
4. Fill the form with unique First Name and Last Name, Email "budi.santoso@@invalid", and Division "Finance"
5. Select Access "Global Settings"
6. Click `[Save]`
7. Verify inline error "Invalid email format" appears and the form is not submitted
8. Replace Email with a unique valid email and uncheck every Access option
9. Click `[Save]`
10. Verify inline error "Access must not be empty" appears and the form is not submitted
11. Verify no new user was created in the User List
