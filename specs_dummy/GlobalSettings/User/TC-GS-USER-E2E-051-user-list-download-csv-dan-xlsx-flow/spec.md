---
id: TC-GS-USER-E2E-051-user-list-download-csv-dan-xlsx-flow
title: "User List: Download data tabel format CSV dan XLSX sesuai kolom terlihat dan filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-476
  - TC-GS-USER-477
  - TC-GS-USER-478
  - TC-GS-USER-479
  - TC-GS-USER-480
  - TC-GS-USER-481
  - TC-GS-USER-482
  - TC-GS-USER-483
  - TC-GS-USER-484
  - TC-GS-USER-485
  - TC-GS-USER-486
coverage:
  web: automated
---

# User List: Download data tabel format CSV dan XLSX sesuai kolom terlihat dan filter

## Prerequisites

- Berada di Global Settings > User > User List

## Test Steps

### Download Laporan

1. Klik ikon Download di toolbar
2. Pilih format 'CSV', verifikasi file CSV berhasil diunduh memuat header kolom yang terlihat dan data tersaring
3. Pilih format 'XLSX', verifikasi file spreadsheet XLSX berhasil diunduh utuh

## Notes

- Menggabungkan 11 test case granular (TC-GS-USER-476 s.d. TC-GS-USER-486).
