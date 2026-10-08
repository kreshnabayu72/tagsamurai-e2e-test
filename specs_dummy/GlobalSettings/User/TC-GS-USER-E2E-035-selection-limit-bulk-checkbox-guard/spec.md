---
id: TC-GS-USER-E2E-035-selection-limit-bulk-checkbox-guard
title: "Bulk Action Bar: Pengamanan batas seleksi maksimum (Selection Limit)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-286
  - TC-GS-USER-287
  - TC-GS-USER-288
  - TC-GS-USER-289
  - TC-GS-USER-290
coverage:
  web: automated
---

# Bulk Action Bar: Pengamanan batas seleksi maksimum (Selection Limit)

## Prerequisites

- Login sebagai Role: Total Control
- Limit seleksi sistem terkonfigurasi (misal 100 user)

## Test Steps

### Uji Batas Seleksi

1. Lakukan seleksi bulk mendekati batas limit
2. Coba lakukan seleksi melebihi batas, verifikasi sistem menampilkan pesan peringatan batas seleksi tercapai dan mencegah seleksi berlebih

## Notes

- Menggabungkan 5 test case granular (TC-GS-USER-286 s.d. TC-GS-USER-290).
