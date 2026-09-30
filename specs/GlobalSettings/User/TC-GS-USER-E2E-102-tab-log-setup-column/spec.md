---
id: TC-GS-USER-E2E-102-tab-log-setup-column
title: 'Setup Column tab log di User Detail berbeda dari Setup Column User List'
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-136
coverage:
  web: automated
---

# Setup Column tab log di User Detail berbeda dari Setup Column User List

## Prerequisites

- Login sebagai Role: Total Control biasa (`totalControl2_automated_qaTeam1`), entity Client
- Mode: mock
- Data mock untuk Tab Changelog di User Detail

## Test Steps

1. Buka User Detail lalu Tab Changelog dan klik header kolom `(⋯)`
2. Verifikasi daftar kolom berisi Date, Action, Field, Old Value, New Value, Modified By
3. Buka Setup Column di User List
4. Verifikasi daftar kolom User List (Active, Name, Email, dan seterusnya) berbeda dari daftar kolom tab log

## Notes

- Sumber `user.md` bagian 4.2a (User List Setup Column dan set kolom tab log).
