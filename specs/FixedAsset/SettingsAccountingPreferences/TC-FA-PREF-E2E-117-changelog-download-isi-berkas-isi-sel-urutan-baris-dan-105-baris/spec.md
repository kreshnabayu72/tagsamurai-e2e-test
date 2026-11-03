---
id: TC-FA-PREF-E2E-117-changelog-download-isi-berkas-isi-sel-urutan-baris-dan-105-baris
title: "Changelog Download isi berkas: isi sel, urutan baris mengikuti Sort, dan 105 baris"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-355
  - TC-FA-PREF-359
  - TC-FA-PREF-360
coverage:
  web: automated
---

# Changelog Download isi berkas: isi sel, urutan baris mengikuti Sort, dan 105 baris

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
- Blok TC-FA-PREF-355 memakai Changelog Preferences berisi 105 entri (PB-C2; ukuran halaman bawaan 10); seed PB-C2 dijalankan lewat API oleh langkah penghubung sebelum blok itu, sebagai pengganti seluruh isi Changelog; disediakan tim FE/BE. Seed PB-C1 dipulihkan oleh hook `after`.
- Kemampuan membuka dan membaca berkas CSV dan XLSX hasil unduhan (nama berkas, baris header, jumlah baris data, nama sheet, isi sel) disediakan tim FE (DB-4: berkas `Changelog-Preferences.csv` dan `Changelog-Preferences.xlsx`).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-359: Isi sel berkas Download: nama lengkap user, nilai kosong, dan kutipan CSV

1. Klik ikon View history di header tab Preferences
2. Klik ikon Download
3. Klik "Download as CSV"
4. Buka berkas yang terunduh
5. Verifikasi kolom Modified By berisi nama lengkap "Budi Santoso" dan "Rina Anggraini" (bukan "Budi S" dan "Rina A")
6. Verifikasi sel Section dan Old Value pada baris Create berisi "-" (hyphen tunggal)
7. Verifikasi sel New Value baris Journal Grouping berisi "Group, Category" dibungkus tanda kutip ganda
8. Verifikasi berkas berenkode UTF-8 dengan BOM

### TC-FA-PREF-360: Urutan baris berkas Download mengikuti Sort aktif

9. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
10. Klik header kolom Date satu kali
11. Klik ikon Download
12. Klik "Download as CSV"
13. Buka berkas yang terunduh
14. Verifikasi baris berkas berurutan dari yang terlama: baris 9 lalu baris 8 lalu baris 7 lalu baris 6 lalu baris 5 lalu baris 4 lalu baris 3 lalu baris 2 lalu baris 1
15. Klik header kolom Date dua kali hingga indikator sort hilang

### TC-FA-PREF-355: Download memuat seluruh baris, bukan hanya halaman yang tampil

16. Seed ulang Changelog Preferences ke PB-C2 (105 entri) lewat API, lalu buka ulang Fixed Asset > Settings > Accounting > Preferences
17. Klik ikon View history di header tab Preferences
18. Verifikasi tabel menampilkan 10 baris pada halaman 1
19. Klik ikon Download
20. Klik "Download as CSV"
21. Buka berkas yang terunduh
22. Verifikasi berkas memuat 105 baris data

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Spec kelas f (isi berkas): TC-FA-PREF-359 dan 360 mengasersi isi sel dan urutan baris berkas; TC-FA-PREF-355 mengasersi jumlah baris berkas dengan 105 entri sebagai data pendukung, bukan objek uji volume.
- Urutan blok: TC-FA-PREF-355 ditaruh sesudah TC-FA-PREF-359 dan 360 supaya dua TC berdata PB-C1 berurutan sebelum satu kali seed ulang PB-C2 (S-10).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih; "Klik header kolom Date dua kali" mengembalikan sort netral setelah TC-FA-PREF-360 (S-09); langkah seed ulang PB-C2 sebelum TC-FA-PREF-355.
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-355, 359, dan 360; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.
  - Expected TC menyebut jumlah absolut Changelog ("105 baris data"; "tabel hanya menampilkan 10 baris"), sedangkan audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Spec mengikuti TC dan mengasumsikan seed PB-C2 menjadi seluruh isi Changelog; perlu dikonfirmasi tim FE/BE.
  - TC-FA-PREF-359 Expected b menyebut sel Section dan Old Value baris Create berisi "-" (hyphen), sedangkan UI menampilkan "—"; spec mengikuti teks TC.
