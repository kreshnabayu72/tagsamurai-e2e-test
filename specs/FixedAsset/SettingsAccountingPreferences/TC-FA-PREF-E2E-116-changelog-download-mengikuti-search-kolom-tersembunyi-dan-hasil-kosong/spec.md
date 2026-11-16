---
id: TC-FA-PREF-E2E-116-changelog-download-mengikuti-search-kolom-tersembunyi-dan-hasil-kosong
title: "Changelog Download: mengikuti Search, tidak memuat kolom tersembunyi, memuat kembali kolom yang ditampilkan, hasil Search kosong"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-354
  - TC-FA-PREF-356
  - TC-FA-PREF-357
  - TC-FA-PREF-358
sourceRules: ["§4.1.4#b2", "§4.1.4#r4"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#b2": [6, 13, 21, 29, 30]
  "§4.1.4#r4": [13, 21, 29]
anchor: [24, 27]
coverage:
  web: automated
---

# Changelog Download: mengikuti Search, tidak memuat kolom tersembunyi, memuat kembali kolom yang ditampilkan, hasil Search kosong

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
- Pemulihan Setup Column: perubahan kolom spec ini dipulihkan dengan langkah eksplisit di spec yang sama; hook `after` menghapus preferensi kolom di browser sebagai cadangan (butir "Pemulihan Setup Column Changelog" di `suite.md`; kemampuan disediakan tim FE).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-354: Download mengikuti Search yang sedang aktif

1. Klik ikon View history di header tab Preferences
2. Ketik Search "Fiscal", tekan Enter
3. Klik ikon Download
4. Klik "Download as CSV"
5. Buka berkas yang terunduh
6. Verifikasi berkas memuat 1 baris data (baris 6, Field Fiscal Year Start)
7. Klik `✕` pada Search, tekan Enter

### TC-FA-PREF-356: Download tidak memuat kolom yang disembunyikan

8. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
9. Klik header kolom Actions (⋯), lalu hapus centang kolom Field
10. Klik ikon Download
11. Klik "Download as CSV"
12. Buka berkas yang terunduh
13. Verifikasi baris header berisi enam kolom tanpa Field: Date, Action, Section, Old Value, New Value, Modified By
14. Klik header kolom Actions (⋯), lalu centang kembali kolom Field

### TC-FA-PREF-357: Download memuat kembali kolom yang ditampilkan lagi sebelum Download

15. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
16. Klik header kolom Actions (⋯), lalu hapus centang kolom Field
17. Klik header kolom Actions (⋯), lalu centang kembali kolom Field
18. Klik ikon Download
19. Klik "Download as CSV"
20. Buka berkas yang terunduh
21. Verifikasi baris header berisi tujuh kolom termasuk Field

### TC-FA-PREF-358: Download dengan hasil Search kosong tetap aktif dan berkas hanya berisi header

22. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
23. Ketik Search "zzzz", tekan Enter
24. Verifikasi ikon Download tetap aktif
25. Klik ikon Download
26. Klik "Download as CSV"
27. Verifikasi tidak ada toast
28. Buka berkas yang terunduh
29. Verifikasi berkas memuat baris header tujuh kolom: Date, Action, Section, Field, Old Value, New Value, Modified By
30. Verifikasi berkas tidak memuat baris data
31. Klik `✕` pada Search, tekan Enter

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC.
- Pemulihan Setup Column (8b.14, R-24): langkah "centang kembali kolom Field" setelah TC-FA-PREF-356 memulihkan perubahan Column Visibility; TC-FA-PREF-357 menghapus dan mencentang kembali kolom Field dalam alurnya sendiri. Langkah `✕` pada Search di akhir TC-FA-PREF-354 dan TC-FA-PREF-358 mengosongkan Search (S-09).
- P-10: TC-FA-PREF-358 mencampur asersi UI (ikon Download tetap aktif, tidak ada toast) dengan isi berkas (baris header, tanpa baris data) pada alur unduh yang sama; klausa isi berkas ditaruh setelah klausa UI dan satu Verifikasi per klausa, dan alur unduh tidak dapat dipisah dari asersi UI. TC-FA-PREF-354, 356, dan 357 hanya mengasersi nama kolom header dan jumlah baris berkas, yang menurut bagian 3 prinsip 13 butir f adalah asersi fungsional (bukan isi sel), sehingga tetap di spec ini.
- Asersi absence toast pada TC-FA-PREF-358 ditulis segera setelah pemicu klik format dan sebelum asersi berkas (8b.11); klik format menjadi anchor positif yang buktinya menyusul pada Verifikasi header berkas.
- Asersi absence kolom Field pada header berkas TC-FA-PREF-356 didahului daftar enam kolom lain pada Verifikasi yang sama (8b.2).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-354, 356, 357, dan 358; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-354, 356, dan 357 tidak menyebut Expected tentang toast; spec tidak menambah asersi toast pada TC itu (S-02).
