---
id: TC-GS-USER-E2E-065-audit-log-user-log-sesi-dan-auth-tracking
title: "Audit Log: Pencatatan riwayat sesi login, IP address, dan perangkat pada Tab User Log"
priority: Low
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-936
  - TC-GS-USER-937
  - TC-GS-USER-938
  - TC-GS-USER-939
  - TC-GS-USER-940
  - TC-GS-USER-941
  - TC-GS-USER-942
  - TC-GS-USER-943
coverage:
  web: automated
---

# Audit Log: Pencatatan riwayat sesi login, IP address, dan perangkat pada Tab User Log

## Prerequisites

- User target melakukan login dan aktivitas sesi

## Test Steps

### Verifikasi User Log Sesi

1. Buka User Detail target > Tab User Log
2. Verifikasi tercatat entri riwayat login dengan IP address, Browser, dan OS
3. Verifikasi entri sesi berakhir (Session ended) tercatat saat logout

## Notes

- Menggabungkan 8 test case granular (TC-GS-USER-936 s.d. TC-GS-USER-943).
