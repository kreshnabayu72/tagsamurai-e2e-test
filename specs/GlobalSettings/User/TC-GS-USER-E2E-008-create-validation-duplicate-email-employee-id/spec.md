---
id: TC-GS-USER-E2E-008-create-validation-duplicate-email-employee-id
title: Create user rejects duplicate email and duplicate employee ID
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-18
  - TC-GS-USER-340
coverage:
  web: automated
---

# Create user rejects duplicate email and duplicate employee ID

## Prerequisites

- Login as Role: Total Control
- User "Doni Pratama" already exists and its email is known
- Employee ID "EMP-001" is already used by another user in this entity
- Division "Finance" exists in master data

## Test Steps

1. Click `[+ User]` to open the Create modal
2. Fill the form with unique First Name and Last Name, the existing email of "Doni Pratama", and Division "Finance"
3. Select Access "Global Settings" only
4. Click `[Save]`
5. Verify inline error "Email already exists" appears and the data is not saved
6. Replace Email with a unique valid email and enter Employee ID "EMP-001"
7. Click `[Save]`
8. Verify inline error "Employee ID already exists" appears and the data is not saved
9. Verify no new user was created in the User List
