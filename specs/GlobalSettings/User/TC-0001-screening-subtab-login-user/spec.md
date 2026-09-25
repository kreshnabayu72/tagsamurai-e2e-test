---
id: TC-0001-screening-subtab-login-user
title: Screening sub-tab Login User within User List tab
priority: High
caseType: Positive
status: ready-for-automation
coverage:
  web: automated
---

# Screening sub-tab Login User within User List tab

## Prerequisites
- Login as Role: Total Control
- User fixture `Doni Pratama` already exists in list

## Test Steps

1. Navigate to `Global Settings > User`
2. Verify sub-tab "Login User" is active by default
3. Verify Header elements: Breadcrumb "User > User List", Tabs ("User List", "Position", "Division", "Custom Field"), Sub-tabs ("Login User", "Non-Login User"), and Table Tools ("Search", "Filter", "Download", "Changelog", "[+ User]")
4. Verify Body columns: Checkbox, Toggle Active, Name (with avatar), Email, Position, Division, Access, Employee ID, Modified By, Last Update, and Column Visibility menu
5. Verify Footer renders pagination with default size 10
