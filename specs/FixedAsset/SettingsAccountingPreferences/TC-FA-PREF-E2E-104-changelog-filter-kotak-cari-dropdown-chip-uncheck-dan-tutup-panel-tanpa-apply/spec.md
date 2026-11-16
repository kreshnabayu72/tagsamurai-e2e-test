---
id: TC-FA-PREF-E2E-104-changelog-filter-kotak-cari-dropdown-chip-uncheck-dan-tutup-panel-tanpa-apply
title: "Changelog Filter: kotak cari di dropdown, hapus chip, uncheck opsi, tutup panel tanpa Apply"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-312
  - TC-FA-PREF-313
  - TC-FA-PREF-314
  - TC-FA-PREF-315
sourceRules: ["§4.1.4#r4", "§4.1.4#r3", "§4.1.4#p2", "§4.1.4#r2"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#r4": [5, 6]
  "§4.1.4#r3": [12, 14, 15, 17, 18, 23, 24]
  "§4.1.4#p2": 29
  "§4.1.4#r2": 31
anchor: [8]
coverage:
  web: automated
---

# Changelog Filter: kotak cari di dropdown, hapus chip, uncheck opsi, tutup panel tanpa Apply

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
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-312: Kotak cari di dalam dropdown filter mempersempit daftar opsi

1. Klik ikon View history di header tab Preferences
2. Klik ikon Filter
3. Buka dropdown Field
4. Ketik "fiscal" pada kotak cari dalam dropdown
5. Verifikasi dropdown memuat opsi Fiscal Year Start
6. Verifikasi dropdown tidak memuat opsi lain (contoh: Journal Grouping)
7. Ketik "zzzz" pada kotak cari dalam dropdown
8. Verifikasi dropdown menampilkan teks "No results found"

### TC-FA-PREF-313: Hapus chip lewat (✕) meng-uncheck opsi di dropdown dan menyisakan chip lain

9. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
10. Klik ikon Filter
11. Pilih opsi General dan Disposal pada dropdown Section
12. Verifikasi field Section menampilkan chip General dan chip Disposal
13. Klik ikon (✕) pada chip General
14. Verifikasi chip General hilang
15. Verifikasi chip Disposal tetap ada
16. Buka dropdown Section
17. Verifikasi opsi General tidak tercentang
18. Verifikasi opsi Disposal tercentang

### TC-FA-PREF-314: Uncheck opsi di dalam dropdown menghapus chip yang bersangkutan dan menyisakan chip lain

19. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
20. Klik ikon Filter
21. Pilih opsi General dan Disposal pada dropdown Section
22. Buka dropdown Section, lalu hapus centang opsi General
23. Verifikasi field Section menampilkan chip Disposal saja
24. Verifikasi chip General hilang dari field

### TC-FA-PREF-315: Menutup Filter Panel tanpa [Apply] membuang pilihan yang belum diterapkan

25. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
26. Klik ikon Filter
27. Pilih opsi Create pada dropdown Action
28. Klik ikon Filter sekali lagi untuk menutup panel tanpa klik `[Apply]`
29. Verifikasi tabel tetap menampilkan 9 baris (baris 1 sampai baris 9)
30. Klik ikon Filter untuk membuka kembali panel
31. Verifikasi dropdown Action pada panel yang dibuka kembali menampilkan placeholder "All actions" (nilai ter-Apply terakhir)

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC. Tidak ada filter yang di-Apply di spec ini, sehingga tidak ada langkah pemulihan filter.
- Langkah 6: "hanya memuat opsi Fiscal Year Start" ditulis sebagai dua Verifikasi (opsi Fiscal Year Start tampil, opsi lain tidak tampil) agar asersi absence punya anchor positif (8b.2).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-312 sampai 315; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - TC-FA-PREF-312 langkah 5 ("Ketik "zzzz" pada kotak cari dalam dropdown") tidak menyebut apakah teks "fiscal" diganti atau ditambah; spec mengikuti teks TC, dan hasil "No results found" sama pada kedua tafsiran.
  - Expected TC menyebut jumlah absolut Changelog ("Tabel tetap menampilkan 9 baris" pada TC-FA-PREF-315), sedangkan audit trail permanen tidak boleh diasersi sebagai angka absolut (S-12). Spec mengikuti TC dan mengasumsikan seed PB-C1 menjadi seluruh isi Changelog; perlu dikonfirmasi tim FE/BE.
