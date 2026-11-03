---
id: TC-FA-FAAL-E2E-024-filter-date-hanya-mulai-atau-akhir-kedua-tab
title: "Filter Date Hanya Tanggal Mulai atau Hanya Tanggal Akhir di Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-73
  - TC-FA-FAAL-74
coverage:
  web: automated
---

# Filter Date Hanya Tanggal Mulai atau Hanya Tanggal Akhir di Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (butir "Env var" di `suite.md`); password tidak ditulis di spec atau fixture.
- Data: Tab Session SS-01 sampai SS-11 (Pre-setup #11; SS-01 sampai SS-04 pada 14/07/26, SS-05 sampai SS-09 pada 15/07/26, SS-10 dan SS-11 pada 16/07/26); Tab User Action UA-01 sampai UA-15 (Pre-setup #12) seluruhnya pada 18/06/26. Spec hanya membaca dan tidak mengubah data.
- Filter Panel dibuka dengan klik icon Filter sesudah tiap pindah tab (lihat Temuan untuk QA).
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan data Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-73: Filter Date hanya tanggal mulai di kedua tab

1. Klik icon Filter
2. Pilih hanya tanggal mulai `16/07/26` pada field Date
3. Klik `[Apply]`
4. Verifikasi hanya SS-10 dan SS-11 (16/07/26 dan sesudahnya) tampil
5. Klik tab User Action
6. Klik icon Filter
7. Pilih hanya tanggal mulai `18/06/26` pada field Date
8. Klik `[Apply]`
9. Verifikasi seluruh 15 baris tampil dengan teks pagination `Showing 1–10 of 15 entries`
10. Ganti tanggal mulai menjadi `19/06/26`
11. Klik `[Apply]`
12. Verifikasi state `No results found` tampil

### TC-FA-FAAL-74: Filter Date hanya tanggal akhir di kedua tab

13. Klik tab Session
14. Klik icon Filter
15. Klik `[Clear Field]`
16. Pilih hanya tanggal akhir `14/07/26` pada field Date
17. Klik `[Apply]`
18. Verifikasi hanya SS-01, SS-02, SS-03, dan SS-04 (14/07/26 dan sebelumnya) tampil
19. Klik tab User Action
20. Klik icon Filter
21. Klik `[Clear Field]`
22. Pilih hanya tanggal akhir `18/06/26` pada field Date
23. Klik `[Apply]`
24. Verifikasi seluruh 15 baris tampil dengan teks pagination `Showing 1–10 of 15 entries`
25. Ganti tanggal akhir menjadi `17/06/26`
26. Klik `[Apply]`
27. Verifikasi state `No results found` tampil

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 13, 15, 21 (kembali ke Tab Session dan mengosongkan field Date sisa TC-FA-FAAL-73 sebelum memilih tanggal akhir).
- TC-FA-FAAL-75 (Date picker tidak mengizinkan tanggal akhir sebelum tanggal mulai) ada di spec 068.
- Temuan untuk QA:
  - TC sumber tidak menyatakan apakah Filter Panel tetap terbuka setelah pindah tab. TC-FA-FAAL-73 langkah 4 memakai "klik tab User Action, klik icon Filter" sehingga spec membuka panel dengan klik icon Filter sesudah tiap pindah tab.
  - Pre-setup #11 menyebut tepat 11 baris Tab Session (dan #12 tepat 15 baris Tab User Action) tanpa menyatakan bahwa login aktor (dan spec lain pada client yang sama) menambah baris `Session started` pada log permanen. Asersi hitungan (`Showing 1–10 of 11 entries`, 15 baris) hanya benar bila data Pre-setup berada di client yang terisolasi dari login lain; spec mengikuti TC.
  - TC-FA-FAAL-74 tidak menyatakan keadaan field Date Tab Session sesudah TC-FA-FAAL-73; spec memakai `[Clear Field]` sebagai langkah penghubung sebelum memilih tanggal akhir.
