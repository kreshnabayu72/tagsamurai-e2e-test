---
id: TC-GS-USER-E2E-013-role-matrix-positif-default-user-actions
title: "Role Matrix Positif: Default User mengelola user Normal dan target tier"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-60
  - TC-GS-USER-61
  - TC-GS-USER-62
coverage:
  web: automated
---

# Role Matrix Positif: Default User mengelola user Normal dan target tier

## Prerequisites

- Login sebagai Default User (Hendra Gunawan)
- Target user Normal, TC, dan RO tersedia

## Test Steps

### Aksi Pengelolaan oleh Default User

1. Buka Global Settings > User > User List
2. Verifikasi Default User memiliki hak akses penuh setara Total Control terhadap user Normal dan target tier

## Notes

- Menggabungkan 3 test case granular (TC-GS-USER-60 s.d. TC-GS-USER-62).
