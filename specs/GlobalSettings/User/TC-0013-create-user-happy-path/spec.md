---
id: TC-0013-create-user-happy-path
title: Create user happy path with Global Settings access and invite email
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
---

# Create user happy path with Global Settings access and invite email

## Prerequisites
- Login as Role: Total Control

## Test Steps

1. Navigate to Global Settings > User and click `[+ User]`
2. Fill form with Full Name "Budi Santoso", Email "budi.santoso@qwertysystem.net", Position "Staff", Division "Finance", and Employee ID "EMP-001"
3. Select Access checkbox "Global Settings"
4. Click `[Save]`
5. Verify success toast "User created. Invitation email sent." appears
6. Verify new user row "Budi Santoso" is listed with "Pending Activation" badge
7. Verify default attributes: Global Toggle Active is ON, Access badge displays "Global Settings", and Temporary User is No
