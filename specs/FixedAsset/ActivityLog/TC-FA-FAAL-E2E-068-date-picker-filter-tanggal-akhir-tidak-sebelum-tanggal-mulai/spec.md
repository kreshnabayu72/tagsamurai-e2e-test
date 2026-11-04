---
id: TC-FA-FAAL-E2E-068-date-picker-filter-tanggal-akhir-tidak-sebelum-tanggal-mulai
title: "Date Picker Filter: Tanggal Akhir Tidak Dapat Dipilih Sebelum Tanggal Mulai di Kedua Tab"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-75
coverage:
  web: automated
---

# Date Picker Filter: Tanggal Akhir Tidak Dapat Dipilih Sebelum Tanggal Mulai di Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11) dan Tab User Action UA-01 sampai UA-15 (Pre-setup #12); spec tidak menerapkan filter dan tidak mengubah data.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-75: Date picker tidak mengizinkan tanggal akhir sebelum tanggal mulai di kedua tab (Tab Session)

1. Klik icon Filter
2. Buka field Date
3. Pilih tanggal mulai `15/07/26`
4. Verifikasi tanggal `14/07/26` pada kalender untuk tanggal akhir tidak dapat dipilih
5. Verifikasi tidak ada pesan error
6. Tutup kalender field Date

### TC-FA-FAAL-75: Date picker tidak mengizinkan tanggal akhir sebelum tanggal mulai di kedua tab (Tab User Action)

7. Klik tab User Action
8. Klik icon Filter
9. Buka field Date
10. Pilih tanggal mulai `18/06/26`
11. Verifikasi tanggal `17/06/26` pada kalender untuk tanggal akhir tidak dapat dipilih
12. Verifikasi tidak ada pesan error
13. Tutup kalender field Date

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 6, 13 (menutup kalender field Date).
- TC-FA-FAAL-73 dan TC-FA-FAAL-74 (Filter Date satu tanggal dan field Date tunggal) ada di spec 024.
- Temuan untuk QA:
  - TC-FA-FAAL-75 Expected c ("Tidak ada pesan error karena pilihan tidak tersedia") berlaku untuk kedua tab; spec mengasersinya pada tiap tab sesudah Expected a atau b.
  - TC sumber tidak menyatakan apakah Filter Panel terbuka sesudah pindah tab; spec membukanya dengan klik icon Filter sesudah pindah tab (TC langkah 4).
