---
id: TC-GS-USER-E2E-063-audit-log-changelog-user-role-dan-auto-revert
title: "Audit Log: Pencatatan mutasi role (Assign, Remove, Auto-Revert) pada Changelog User > Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-900
  - TC-GS-USER-901
  - TC-GS-USER-902
  - TC-GS-USER-903
  - TC-GS-USER-904
  - TC-GS-USER-905
  - TC-GS-USER-906
  - TC-GS-USER-907
  - TC-GS-USER-908
  - TC-GS-USER-909
  - TC-GS-USER-910
  - TC-GS-USER-911
  - TC-GS-USER-912
  - TC-GS-USER-913
  - TC-GS-USER-914
  - TC-GS-USER-915
  - TC-GS-USER-916
  - TC-GS-USER-1044
  - TC-GS-USER-1052
coverage:
  web: automated
---

# Audit Log: Pencatatan mutasi role (Assign, Remove, Auto-Revert) pada Changelog User > Role

## Prerequisites

- Lakukan perubahan role pada target di Detail > Tab Role

## Test Steps

### Verifikasi Log Mutasi Role

1. Buka ikon Changelog di toolbar Tab Role
2. Verifikasi tercatat entri 'Assign' saat role baru dicentang
3. Verifikasi tercatat entri 'Remove' saat centang role dicabut
4. Verifikasi tercatat entri 'Auto-Revert' saat pencabutan otomatis sistem terpicu

## Notes

- Menggabungkan 19 test case granular (TC-GS-USER-900 s.d. TC-GS-USER-1052).
