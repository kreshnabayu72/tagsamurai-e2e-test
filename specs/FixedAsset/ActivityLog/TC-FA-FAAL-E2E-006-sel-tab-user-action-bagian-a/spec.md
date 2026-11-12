---
id: TC-FA-FAAL-E2E-006-sel-tab-user-action-bagian-a
title: "Sel Tab User Action: Modified By, Name, dan Old/New Value Kosong (bagian A)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-20
  - TC-FA-FAAL-21
  - TC-FA-FAAL-22
  - TC-FA-FAAL-23
  - TC-FA-FAAL-24
coverage:
  web: automated
---

# Sel Tab User Action: Modified By, Name, dan Old/New Value Kosong (bagian A)

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log > User Action.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), 15 baris, dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan default Date terbaru di atas dengan 10 baris per halaman: halaman 1 berisi UA-01 sampai UA-10, halaman 2 berisi UA-11 sampai UA-15. Nilai baris yang diasersi:
  | Baris | Name | Old Value | New Value | Modified By |
  |---|---|---|---|---|
  | UA-01 | Budi Santoso | `—` | Total Control | Admin Alpha |
  | UA-02 | Gedung A > Lantai 3 - Renovasi | Lantai 3 | Lantai 3 - Renovasi | Admin Alpha |
  | UA-04 | Kendaraan Operasional (AST-2024-0088) | In Use | Reported Disposal | Admin Alpha |
  | UA-05 | Kamera DSLR (AST-2024-0141) | Borrowed | Damaged | Ahmad Dahlan |
  | UA-08 | `—` (aksi settings-level Settings > Transactions, seed BE) | 7 days | 14 days | Admin Beta |
  | UA-11 | Default Group | `—` | Default Group | System (seed BE) |
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); baris UA-08 dan UA-11 adalah seed BE.
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-20: Kolom Modified By tampil nama singkat dengan hover nama lengkap

1. Klik tab User Action
2. Verifikasi kolom Modified By baris UA-01 tampil `Admin A` sebagai plain text
3. Verifikasi kolom Modified By baris UA-05 tampil `Ahmad D` sebagai plain text
4. Arahkan kursor ke sel Modified By baris UA-01
5. Verifikasi tooltip `Admin Alpha` tampil
6. Arahkan kursor ke sel Modified By baris UA-05
7. Verifikasi tooltip `Ahmad Dahlan` tampil

### TC-FA-FAAL-21: Modified By aksi sistem tampil System polos tanpa hover

8. Klik `[Next →]`
9. Verifikasi kolom Modified By baris UA-11 tampil `System` sebagai plain text
10. Arahkan kursor ke sel Modified By baris UA-11
11. Verifikasi tidak ada tooltip yang tampil
12. Klik `[← Prev]`

### TC-FA-FAAL-22: Name tampil strip untuk aksi settings-level tanpa entitas bernama

13. Verifikasi kolom Name baris UA-08 tampil `—`
14. Verifikasi kolom Name baris UA-01 tampil `Budi Santoso`

### TC-FA-FAAL-23: Name entitas Group tampil sebagai path hierarki penuh

15. Verifikasi kolom Name baris UA-02 tampil `Gedung A > Lantai 3 - Renovasi` (path hierarki penuh dengan nama sesudah perubahan)
16. Verifikasi baris UA-02 tampil Old Value `Lantai 3` dan New Value `Lantai 3 - Renovasi`

### TC-FA-FAAL-24: Name entitas aset tampil sebagai Nama dan Asset ID

17. Verifikasi kolom Name baris UA-04 tampil `Kendaraan Operasional (AST-2024-0088)`
18. Verifikasi kolom Name baris UA-05 tampil `Kamera DSLR (AST-2024-0141)`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (memastikan tab User Action aktif), langkah 8 dan 12 (UA-11 berada di halaman 2 pada urutan default; `[← Prev]` mengembalikan halaman 1 sebelum TC berikutnya, S-09).
- Hover pada langkah 4, 6, dan 10 diasersi segera sebelum elemen berikutnya disentuh (bagian 8b butir 5); asersi absence tooltip pada langkah 11 berjangkar pada langkah 9 (baris UA-11 tampil).
- Kolom Modified By diasersi berformat `[First Name] [Last Initial]` (R-14).
- TC-FA-FAAL-25 sampai 29 (sel Old Value, New Value, Field, dan nilai panjang) ada di spec 007.
- Temuan untuk QA:
  - TC-FA-FAAL-20 sampai 24 menyebut baris UA-nn sebagai baris terobservasi tanpa menyebut halaman; UA-11 berada di halaman 2 pada urutan default dengan 10 baris per halaman.
  - TC-FA-FAAL-21 dan 22 menyebut baris UA-11 dan UA-08 sebagai seed BE; mekanisme seed disediakan tim FE/BE.
