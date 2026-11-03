---
id: TC-FA-FAAL-E2E-007-sel-tab-user-action-bagian-b
title: "Sel Tab User Action: Old/New Value, Field, dan Nilai Panjang (bagian B)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-FAAL-25
  - TC-FA-FAAL-26
  - TC-FA-FAAL-27
  - TC-FA-FAAL-28
  - TC-FA-FAAL-29
coverage:
  web: automated
---

# Sel Tab User Action: Old/New Value, Field, dan Nilai Panjang (bagian B)

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log > User Action.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), 15 baris, dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan default Date terbaru di atas dengan 10 baris per halaman: halaman 1 berisi UA-01 sampai UA-10, halaman 2 berisi UA-11 sampai UA-15. Nilai baris yang diasersi:
  | Baris | Field | Old Value | New Value |
  |---|---|---|---|
  | UA-01 | Access Level | `—` | Total Control |
  | UA-03 | Category Name | Electronic Devices | `—` |
  | UA-04 | Status | In Use | In Disposal Process |
  | UA-05 | Status | Borrowed | Damaged |
  | UA-06 | Status | In Audit | Waiting for Approval |
  | UA-07 | Manage asset & TAG — Gedung A | `—` | Assigned |
  | UA-12 | Manage asset & TAG — Gedung A | Assigned | `—` |
  | UA-15 | Group Name | `—` | nama sama dengan Name |
  Baris UA-15 (Create Groups) memuat Name `Gedung Serbaguna` ditambah nama 120 karakter (Pre-setup #12).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-25: Old Value kosong untuk aksi bergaya create

1. Klik tab User Action
2. Verifikasi baris UA-01 tampil Old Value `—` dan New Value `Total Control`
3. Verifikasi baris UA-07 tampil Old Value `—` dan New Value `Assigned`

### TC-FA-FAAL-26: New Value kosong untuk aksi bergaya hapus

4. Verifikasi baris UA-03 tampil Old Value `Electronic Devices` dan New Value `—`
5. Verifikasi baris UA-12 tampil Old Value `Assigned` dan New Value `—`

### TC-FA-FAAL-27: Aksi perubahan status mengisi Old Value dan New Value

6. Verifikasi baris UA-04 tampil Field `Status`, Old Value `In Use`, dan New Value `In Disposal Process`
7. Verifikasi baris UA-05 tampil Field `Status`, Old Value `Borrowed`, dan New Value `Damaged`
8. Verifikasi baris UA-06 tampil Field `Status`, Old Value `In Audit`, dan New Value `Waiting for Approval`
9. Verifikasi tidak ada sel Old Value maupun New Value bernilai `—` pada baris UA-04, UA-05, dan UA-06

### TC-FA-FAAL-28: Field tidak pernah kosong pada aksi Create maupun Delete

10. Verifikasi kolom Field setiap baris pada halaman 1 (UA-01 sampai UA-10, termasuk baris Delete UA-03) terisi dan tidak ada sel Field bernilai `—`
11. Klik `[Next →]`
12. Verifikasi kolom Field setiap baris pada halaman 2 (UA-11 sampai UA-15, termasuk baris Create UA-11) terisi dan tidak ada sel Field bernilai `—`

### TC-FA-FAAL-29: Nilai panjang tampil utuh tanpa pemotongan

13. Verifikasi nilai Name baris UA-15 tampil utuh tanpa pemotongan (tidak ada `..`)
14. Verifikasi kolom Name melebar mengikuti isi
15. Arahkan kursor ke sel Name baris UA-15
16. Verifikasi tidak ada tooltip yang tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (memastikan tab User Action aktif), langkah 11 (halaman 2 memuat UA-11 sampai UA-15; blok TC-FA-FAAL-29 berikutnya memakai UA-15 yang berada di halaman itu).
- Asersi universal pada langkah 10 dan 12 berjangkar pada baris-baris yang sudah tampil dan diasersi pada langkah 2 sampai 8 (bagian 8b butir 2).
- Hover pada langkah 15 diasersi segera sebelum elemen berikutnya disentuh (bagian 8b butir 5).
- TC-FA-FAAL-20 sampai 24 (Modified By, Name) ada di spec 006.
- Temuan untuk QA:
  - TC-FA-FAAL-29 menyebut "Baris Name dengan 120 karakter (Pre-setup #12)"; Tabel Pre-setup #12 menulis UA-15 sebagai `Gedung Serbaguna` + nama 120 karakter, sehingga tidak jelas apakah 120 karakter adalah total atau tambahan.
  - TC-FA-FAAL-25 dan 26 menyebut baris UA-01, UA-07, UA-03, dan UA-12 tanpa menyebut halaman; seluruhnya berada di halaman 1 pada urutan default dengan 10 baris per halaman.
