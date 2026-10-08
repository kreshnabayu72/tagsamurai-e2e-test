---
id: TC-GS-USER-E2E-048-user-list-sort-kolom-tabel-utama
title: "User List: Pengurutan 3-state pada seluruh kolom tabel utama"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-435
  - TC-GS-USER-436
  - TC-GS-USER-437
  - TC-GS-USER-438
  - TC-GS-USER-439
  - TC-GS-USER-440
  - TC-GS-USER-441
  - TC-GS-USER-442
coverage:
  web: automated
---

# User List: Pengurutan 3-state pada seluruh kolom tabel utama

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Sort Kolom

1. Klik header kolom Name, verifikasi urutan A-Z (ascending)
2. Klik header kolom Name kedua kali, verifikasi urutan Z-A (descending)
3. Klik header kolom Name ketiga kali, verifikasi kembali ke urutan default tanpa sort
4. Uji pengurutan pada kolom Email, Division, Employee ID, dan Last Update

## Notes

- Menggabungkan 8 test case granular (TC-GS-USER-435 s.d. TC-GS-USER-442).
