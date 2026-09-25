---
id: TC-0016-create-user-validation-empty-fields
title: Form validation prevents submission when required fields are empty
priority: High
caseType: Negative
status: ready-for-automation
coverage:
  web: automated
---

# Form validation prevents submission when required fields are empty

## Prerequisites
- Login as Role: Total Control

## Test Steps

1. Navigate to Global Settings > User and click `[+ User]`
2. Leave all fields empty and click `[Save]`
3. Verify form submission is blocked
4. Verify inline error messages appear on required fields:
   - "First Name must not be empty" / "Full Name must not be empty"
   - "Email must not be empty"
   - "Division must not be empty"
