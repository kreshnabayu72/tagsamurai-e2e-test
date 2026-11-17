---
id: TC-FA-PREF-E2E-105-changelog-filter-titik-indikator-kolom-tersembunyi-dan-clear-field-tidak-mereset-search-sort
title: "Changelog Filter: titik indikator ikon Filter, filter pada kolom tersembunyi, Clear Field tidak mereset Search dan Sort"
layer: ui-e2e
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-PREF-316
  - TC-FA-PREF-317
  - TC-FA-PREF-320
sourceRules: ["§4.1.4#r2", "§4.1.4#r7"]
smoke: []
dependsOn: []
trace:
  "§4.1.4#r2": [13, 14, 16, 17, 26]
  "§4.1.4#r7": 27
anchor: [4, 6, 8, 25]
coverage:
  web: automated
---

# Changelog Filter: titik indikator ikon Filter, filter pada kolom tersembunyi, Clear Field tidak mereset Search dan Sort

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
- Pemulihan Setup Column: perubahan kolom spec ini dipulihkan dengan langkah eksplisit di spec yang sama; hook `after` menghapus preferensi kolom di browser sebagai cadangan (butir "Pemulihan Setup Column Changelog" di `suite.md`; kemampuan disediakan tim FE).
- Format tanggal General Settings `dd/MM/yy` dengan waktu 24 jam (PB-1).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-316: Ikon Filter menampilkan titik indikator saat ada filter ter-Apply

1. Klik ikon View history di header tab Preferences
2. Klik ikon Filter
3. Pilih opsi Create pada dropdown Action, lalu klik `[Apply]`
4. Verifikasi ikon Filter menampilkan badge titik (tanpa angka) saat panel tertutup
5. Klik ikon Filter untuk membuka panel
6. Verifikasi ikon Filter menampilkan badge titik (tanpa angka) saat panel terbuka
7. Klik `[Clear Field]`, lalu klik `[Apply]`
8. Verifikasi badge titik pada ikon Filter hilang

### TC-FA-PREF-317: Filter tetap tersedia dan tetap berlaku saat kolomnya disembunyikan

9. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
10. Klik ikon Filter
11. Pilih opsi Create pada dropdown Action, lalu klik `[Apply]`
12. Klik header kolom Actions (⋯), lalu hapus centang kolom Action
13. Verifikasi tabel tetap menampilkan baris 9 setelah kolom Action disembunyikan
14. Verifikasi baris lain (contoh: baris 1) tidak tampil pada tabel
15. Klik ikon Filter dan amati dropdown Action
16. Verifikasi field Action tetap ada pada Filter Panel
17. Verifikasi field Action tetap menampilkan chip Create
18. Klik `[Clear Field]`, lalu klik `[Apply]`
19. Klik header kolom Actions (⋯), lalu centang kembali kolom Action

### TC-FA-PREF-320: Clear Field pada Filter Panel tidak mereset Search dan Sort

20. Tutup modal Changelog lewat `✕`, lalu klik ikon View history di header tab Preferences
21. Ketik Search "Rina", tekan Enter
22. Klik header kolom Action satu kali
23. Klik ikon Filter, pilih opsi Disposal pada dropdown Section, lalu klik `[Apply]`
24. Klik ikon Filter, klik `[Clear Field]`, lalu klik `[Apply]`
25. Verifikasi kata kunci Search tetap "Rina"
26. Verifikasi sort Action ascending tetap aktif
27. Verifikasi tabel menampilkan baris 2, 3, 5, 6, 7, dan 8 (hasil Search tanpa filter Section)
28. Klik `(←)` pada kotak Search
29. Klik header kolom Action dua kali hingga indikator sort hilang

## Notes

- Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Baris seed Changelog disebut "baris N" mengikuti tabel PB-C1 di Prerequisites; Modified By ditulis `Budi S` dan `Rina A` sesuai format kolom (R-14).
- Langkah penghubung (S-03): "Tutup modal Changelog lewat `✕`, lalu klik ikon View history" membuka ulang modal bersih untuk tiap TC; "Klik `[Clear Field]`, lalu klik `[Apply]`" setelah blok TC-FA-PREF-316 dan TC-FA-PREF-317 mengosongkan filter (S-09).
- Pemulihan Setup Column (8b.14, R-24): langkah "centang kembali kolom Action" memulihkan perubahan Column Visibility TC-FA-PREF-317 (diterapkan langsung tanpa `[Save]`); "Klik `(←)` pada kotak Search" dan "Klik header kolom Action dua kali" memulihkan Search dan Sort TC-FA-PREF-320 (S-09).
- Langkah "Verifikasi baris lain (contoh: baris 1) tidak tampil" pada TC-FA-PREF-317 adalah klausa "hanya baris 9" Expected a; didahului Verifikasi baris 9 tampil (8b.2).
- Temuan untuk QA:
  - Nama env var password tidak disebut TC-FA-PREF-316, 317, dan 320; `FA_TC_PASSWORD` mengikuti spec lain di suite dan perlu keputusan tim.
  - Kolom Section baris seed 1 (Chart of Accounts) dan baris 4 (Journal Export) serta Date baris seed 4 dan 5 tidak tertulis eksplisit di TC; Section disimpulkan dari urutan sort TC-FA-PREF-325 dan daftar opsi Section TC-FA-PREF-306.
