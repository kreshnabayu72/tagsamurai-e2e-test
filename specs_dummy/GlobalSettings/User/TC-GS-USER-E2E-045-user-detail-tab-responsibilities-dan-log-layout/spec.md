---
id: TC-GS-USER-E2E-045-user-detail-tab-responsibilities-dan-log-layout
title: "User Detail: Layout dan navigasi tab Responsibilities, Non-Login User, dan Log surfaces"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-381
  - TC-GS-USER-382
  - TC-GS-USER-383
  - TC-GS-USER-384
  - TC-GS-USER-385
  - TC-GS-USER-386
  - TC-GS-USER-387
  - TC-GS-USER-388
  - TC-GS-USER-389
  - TC-GS-USER-390
  - TC-GS-USER-391
  - TC-GS-USER-392
  - TC-GS-USER-393
  - TC-GS-USER-394
  - TC-GS-USER-395
  - TC-GS-USER-396
  - TC-GS-USER-397
  - TC-GS-USER-398
  - TC-GS-USER-399
  - TC-GS-USER-400
  - TC-GS-USER-401
  - TC-GS-USER-402
  - TC-GS-USER-403
  - TC-GS-USER-404
  - TC-GS-USER-405
  - TC-GS-USER-406
  - TC-GS-USER-407
  - TC-GS-USER-408
  - TC-GS-USER-409
  - TC-GS-USER-410
  - TC-GS-USER-411
  - TC-GS-USER-412
  - TC-GS-USER-1042
  - TC-GS-USER-1051
coverage:
  web: automated
---

# User Detail: Layout dan navigasi tab Responsibilities, Non-Login User, dan Log surfaces

## Prerequisites

- Buka User Detail user dengan data transaksi riil

## Test Steps

### Navigasi Antar Tab Detail

1. Klik tab 'Responsibilities', verifikasi sub-tab Borrowed Assets, Assigned Assets, Pending Approvals, Pending Tasks
2. Klik tab 'Non-Login User', verifikasi tabel peminjam yang diwakili
3. Klik tab 'Changelog', 'System Log', dan 'User Log', verifikasi masing-masing tabel log termuat rapi

## Notes

- Menggabungkan 34 test case granular (TC-GS-USER-381 s.d. TC-GS-USER-1051).
