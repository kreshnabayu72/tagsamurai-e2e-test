---
id: TC-GS-USER-E2E-064-audit-log-system-log-dan-activity-log-sync
title: "Audit Log: Pencatatan aktivitas aktor pada Tab System Log dan Activity Log level Global"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-917
  - TC-GS-USER-918
  - TC-GS-USER-919
  - TC-GS-USER-920
  - TC-GS-USER-921
  - TC-GS-USER-922
  - TC-GS-USER-923
  - TC-GS-USER-924
  - TC-GS-USER-925
  - TC-GS-USER-926
  - TC-GS-USER-927
  - TC-GS-USER-928
  - TC-GS-USER-929
  - TC-GS-USER-930
  - TC-GS-USER-931
  - TC-GS-USER-932
  - TC-GS-USER-933
  - TC-GS-USER-934
  - TC-GS-USER-935
coverage:
  web: automated
---

# Audit Log: Pencatatan aktivitas aktor pada Tab System Log dan Activity Log level Global

## Prerequisites

- Aktor melakukan aksi administrasi user

## Test Steps

### Verifikasi System Log dan Activity Log

1. Buka Detail User aktor > Tab System Log, verifikasi seluruh aksi yang dilakukan aktor tercatat rapi
2. Buka Global Settings > Activity Log, verifikasi log mutasi user tercatat di level modul global

## Notes

- Menggabungkan 19 test case granular (TC-GS-USER-917 s.d. TC-GS-USER-935).
