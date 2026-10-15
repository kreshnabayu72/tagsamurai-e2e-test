---
id: TC-GS-USER-E2E-052-modal-changelog-user-list-struktur-dan-filter
title: "Modal Changelog User List: Screening struktur modal, kolom, pencarian, dan filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-487
  - TC-GS-USER-488
  - TC-GS-USER-489
  - TC-GS-USER-490
  - TC-GS-USER-491
  - TC-GS-USER-492
  - TC-GS-USER-493
  - TC-GS-USER-494
  - TC-GS-USER-495
  - TC-GS-USER-496
  - TC-GS-USER-497
  - TC-GS-USER-498
  - TC-GS-USER-499
  - TC-GS-USER-500
  - TC-GS-USER-501
  - TC-GS-USER-502
  - TC-GS-USER-503
  - TC-GS-USER-504
  - TC-GS-USER-505
  - TC-GS-USER-506
  - TC-GS-USER-507
  - TC-GS-USER-508
  - TC-GS-USER-509
  - TC-GS-USER-510
  - TC-GS-USER-511
  - TC-GS-USER-512
  - TC-GS-USER-513
  - TC-GS-USER-514
  - TC-GS-USER-515
  - TC-GS-USER-516
  - TC-GS-USER-517
  - TC-GS-USER-518
  - TC-GS-USER-519
  - TC-GS-USER-520
  - TC-GS-USER-521
  - TC-GS-USER-522
  - TC-GS-USER-523
  - TC-GS-USER-524
  - TC-GS-USER-525
  - TC-GS-USER-526
  - TC-GS-USER-527
  - TC-GS-USER-528
  - TC-GS-USER-529
  - TC-GS-USER-530
  - TC-GS-USER-531
  - TC-GS-USER-532
  - TC-GS-USER-533
  - TC-GS-USER-534
  - TC-GS-USER-535
  - TC-GS-USER-536
  - TC-GS-USER-537
  - TC-GS-USER-538
  - TC-GS-USER-539
  - TC-GS-USER-540
  - TC-GS-USER-1053
coverage:
  web: automated
---

# Modal Changelog User List: Screening struktur modal, kolom, pencarian, dan filter

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Screening dan Filter Changelog Modal

1. Klik ikon Changelog di toolbar tabel User List
2. Verifikasi modal Changelog terbuka menampilkan kolom Date, Action, Name, Field, Old Value, New Value, Modified By
3. Ketik pencarian pada search box Changelog, verifikasi data tersaring
4. Gunakan filter panel Changelog untuk menyaring berdasarkan Action 'Edit', verifikasi hasil akurat

## Notes

- Menggabungkan 55 test case granular (TC-GS-USER-487 s.d. TC-GS-USER-1053).
