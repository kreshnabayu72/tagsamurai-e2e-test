---
id: TC-FA-PREF-E2E-115-changelog-download-menu-format-csv-xlsx-dan-mengikuti-filter
title: "Changelog Download: menu pilihan format, berkas CSV, berkas XLSX, dan mengikuti Filter"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-350
  - TC-FA-PREF-351
  - TC-FA-PREF-352
  - TC-FA-PREF-353
sourceRules: ["§4.1.4#b2", "§4.1.4#r1", "§4.1.4#r2", "§4.1.4#r3", "§4.1.4#r4", "§4.1.4#r5", "§4.1.4#r6", "§4.1.4#r7", "§4.1.4#r16"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#b2": [3, 8, 10, 11, 16, 19, 25]
  "§4.1.4#r1": 10
  "§4.1.4#r2": [10, 25]
  "§4.1.4#r3": 10
  "§4.1.4#r4": 10
  "§4.1.4#r5": 10
  "§4.1.4#r6": 10
  "§4.1.4#r7": 10
  "§4.1.4#r16": 25
anchor: [7, 15, 18]
coverage:
  web: automated
---

# Changelog Download: menu pilihan format, berkas CSV, berkas XLSX, dan mengikuti Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup PA-4 dan PB-U), email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, company `PT Contoh Konstruksi` (PB-1), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` (password akun Total Control) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Nama sama dengan spec lain di suite karena TC tidak menyebutnya (lihat Temuan untuk QA). Password tidak ditulis di spec atau fixture.
- Data awal (seed lewat API di hook `before`): Preferences company sesuai PB-1 (Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month; periode Mar 2026 sampai Dec 2026 Open). Changelog Preferences berisi 9 entri contoh (PB-C1) sebagai seluruh isi Changelog; seed disediakan tim FE/BE. Baris disebut "baris N" mengikuti nomor berikut (urutan tampil default Newest First; kolom Modified By tampil `Budi S` dan `Rina A`):
  - Baris 1: Date 27/10/26 16:40, Action Edit, Section Chart of Accounts, Field Default Capitalization Offset, Old Value —, New Value 1-2900 – Biaya Dikapitalisasi, Modified By Budi S
  - Baris 2: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Sell, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 3: Date 26/10/26, Action Edit, Section Disposal, Field Disposal Documents — Scrap, Old Value Optional, New Value Required, Modified By Rina A
  - Baris 4: Date tidak tertulis di TC, Action Edit, Section Journal Export, Field Journal Grouping, Old Value Group, New Value Group, Category, Modified By Budi S
  - Baris 5: Date tidak tertulis di TC, Action Edit, Section Disposal, Field Default Gain on Disposal, Old Value 4-9100 – Laba Pelepasan Aset, New Value —, Modified By Rina A
  - Baris 6: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field Fiscal Year Start, Old Value January, New Value April, Modified By Rina A
  - Baris 7: Date 22/10/26 sampai 23/10/26, Action Edit, Section General, Field First Accounting Period, Old Value Mar 2026, New Value Jan 2026, Modified By Rina A
  - Baris 8: Date 22/10/26 sampai 23/10/26, Action Edit, Section Capitalization, Field Default Capitalization Threshold, Old Value 5.000.000, New Value 10.000.000, Modified By Rina A
  - Baris 9: Date 20/10/26 09:12, Action Create, Section —, Field Preferences, Old Value —, New Value Initial values, Modified By Budi S
  - Urutan tulis seed: baris 3 ditulis sebelum baris 2 dan baris 7 sebelum baris 6 pada Date yang sama (tie-break sort).
- Kemampuan membuka dan membaca berkas CSV dan XLSX hasil unduhan (nama berkas, baris header, jumlah baris data, nama sheet, isi sel) disediakan tim FE (DB-4: berkas `Changelog-Preferences.csv` dan `Changelog-Preferences.xlsx`).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-350: Klik ikon Download menampilkan pilihan format

1. Klik ikon View history di header tab Preferences
2. Klik ikon Download pada toolbar modal
3. Verifikasi overlay menampilkan pilihan "Download as CSV" dan "Download as XLSX"

### TC-FA-PREF-351: Download CSV tanpa Search atau Filter memuat seluruh baris dengan nama Changelog-Preferences.csv

4. Tutup overlay pilihan format Download, tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
5. Klik ikon Download
6. Klik "Download as CSV"
7. Verifikasi tidak ada toast sukses
8. Verifikasi berkas terunduh bernama Changelog-Preferences.csv
9. Buka berkas yang terunduh
10. Verifikasi baris header berisi tujuh kolom: Date, Action, Section, Field, Old Value, New Value, Modified By
11. Verifikasi berkas memuat 9 baris data

### TC-FA-PREF-352: Download XLSX memuat satu sheet bernama Sheet1 dengan nama Changelog-Preferences.xlsx

12. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
13. Klik ikon Download
14. Klik "Download as XLSX"
15. Verifikasi tidak ada toast sukses
16. Verifikasi berkas terunduh bernama Changelog-Preferences.xlsx
17. Buka berkas yang terunduh
18. Verifikasi berkas memuat satu sheet bernama Sheet1
19. Verifikasi sheet Sheet1 memuat 9 baris data di bawah baris header

### TC-FA-PREF-353: Download mengikuti Filter yang sedang aktif

20. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
21. Klik ikon Filter, pilih opsi Create pada dropdown Action, lalu klik `[Apply]`
22. Klik ikon Download
23. Klik "Download as CSV"
24. Buka berkas yang terunduh
25. Verifikasi berkas memuat 1 baris data (baris 9, Action Create)
26. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup overlay pilihan format Download, tutup modal Changelog lewat `✕`, lalu klik ikon View history" menutup overlay TC-FA-PREF-350 sebelum membuka ulang modal bersih; "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal untuk TC lain; langkah `[Clear Field]` di akhir TC-FA-PREF-353 mengosongkan filter (S-09).
- P-10: TC-FA-PREF-351, 352, dan 353 mencampur asersi UI (tidak ada toast sukses, nama berkas terunduh) dengan isi berkas (baris header, jumlah baris data, nama sheet) pada alur unduh yang sama. Klausa isi berkas ditaruh setelah klausa UI TC itu dan satu Verifikasi per klausa. Alur unduh tidak dapat dipisah dari asersi UI karena berkas hanya terbentuk dari klik format di UI.
- Asersi absence toast sukses ditulis segera setelah pemicu klik format dan sebelum asersi berkas terunduh; klik format menjadi anchor positif yang buktinya menyusul pada Verifikasi nama berkas (8b.11).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-350 sampai 353; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Expected TC menyebut jumlah absolut Changelog ("9 baris data" pada TC-FA-PREF-351 dan 352), sedangkan audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Spec mengikuti TC dan mengasumsikan seed PB-C1 menjadi seluruh isi Changelog; perlu dikonfirmasi tim FE/BE.
