---
id: TC-GS-USER-E2E-011-role-matrix-positif-total-control-actions
title: "Role Matrix Positif: Total Control mengelola baris user Normal, sesama TC, dan RO"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-49
  - TC-GS-USER-52
  - TC-GS-USER-53
coverage:
  web: automated
---

# Role Matrix Positif: Total Control mengelola baris user Normal, sesama TC, dan RO

## Prerequisites

- Login sebagai Role: Total Control
- Target user Normal, user Total Control (Andi Wijaya), dan user Read Only (Doni Pratama) tersedia

## Test Steps

### Pengelolaan Target Normal dan Tier

1. Buka Global Settings > User > User List
2. Pada baris user Normal, verifikasi tombol Edit dan Delete enabled, toggle Active dapat diklik
3. Pada baris sesama Total Control (Andi Wijaya), verifikasi tombol Edit enabled dan hak pengelolaan tersedia
4. Pada baris target Read Only (Doni Pratama), verifikasi kontrol pengelolaan enabled

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-49 s.d. TC-GS-USER-53).
