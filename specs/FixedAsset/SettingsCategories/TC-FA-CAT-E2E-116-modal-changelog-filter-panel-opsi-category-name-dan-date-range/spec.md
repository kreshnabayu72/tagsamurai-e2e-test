---
id: TC-FA-CAT-E2E-116-modal-changelog-filter-panel-opsi-category-name-dan-date-range
title: "Modal Changelog: Screening Filter Panel, Logika OR dan AND, Opsi dari Data Log, Category Name Berbasis Id, dan Date Range Inklusif"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-400
  - TC-FA-CAT-401
  - TC-FA-CAT-402
  - TC-FA-CAT-403
  - TC-FA-CAT-404
coverage:
  web: automated
---

# Modal Changelog: Screening Filter Panel, Logika OR dan AND, Opsi dari Data Log, Category Name Berbasis Id, dan Date Range Inklusif

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 (pohon kategori CatMain) dan #23 (12 baris riwayat Changelog CatMain sesuai Example Data PRD §4.1: Create `Electronics`, Create `Electronics › Laptop`, Create `Vehicle`, Edit rename `Laptop` ke `Notebook` dan Code `LAP-01` ke `NBK-01`, Edit Description `Furniture`, Delete `Kunci Locker`, Delete `Peripheral` dan `Accessory` satu batch, Marked/Restored as Excess, Marked as Excess `Heavy Equipment` oleh System). Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).

## Test Steps

### TC-FA-CAT-400: Screening Filter Panel Changelog

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di toolbar modal
3. Verifikasi field berurutan: Date (date range, placeholder `Select date`), Action (multi-select searchable, `All actions`), Category Name (multi-select searchable, `All categories`), Field (`All fields`), Modified By (`All users`)
4. Verifikasi maksimal 4 field per baris: baris pertama Date, Action, Category Name, Field dan baris kedua Modified By
5. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-FA-CAT-401: Filter Action, Field, dan Modified By (OR dalam field)

6. Pilih Action `Create` dan `Delete` lalu klik `[Apply]`
7. Verifikasi baris yang tampil ber-Action `Create` atau `Delete` (OR)
8. Klik icon Filter, tambahkan Field `Category Name` lalu klik `[Apply]`
9. Klik icon Filter, tambahkan Modified By `John D` lalu klik `[Apply]`
10. Verifikasi hasil adalah irisan ketiga kriteria (AND antar field)
11. Klik icon Filter lalu klik `[Clear Field]` pada tiap field dan klik `[Apply]`

### TC-FA-CAT-402: Opsi filter Action dan Field berasal dari data log saat ini

12. Klik icon Filter lalu buka dropdown Action dan Field
13. Verifikasi opsi Action memuat kelima Action yang ada di log
14. Verifikasi opsi Field memuat `Category Name`, `Code`, `Description`, `Excess`
15. Verifikasi nilai yang tidak pernah tercatat tidak muncul sebagai opsi

### TC-FA-CAT-403: Filter Category Name mencocokkan lewat id

16. Klik icon Filter lalu buka dropdown Category Name
17. Verifikasi opsi menampilkan full path terkini untuk kategori yang masih ada (`Electronics › Notebook`)
18. Pilih opsi untuk kategori `Notebook` (sebelumnya `Laptop`) dan klik `[Apply]`
19. Verifikasi satu opsi `Notebook` menampilkan seluruh riwayatnya (Create `Laptop` dan rename) karena dicocokkan lewat id
20. Klik icon Filter, klik `[Clear Field]` pada Category Name, lalu buka dropdown Category Name
21. Pilih opsi kategori yang sudah dihapus `Kunci Locker` lalu klik `[Apply]`
22. Verifikasi kategori yang sudah dihapus tetap muncul sebagai opsi dengan full path terakhir sebelum dihapus dan menampilkan baris Create/Delete-nya
23. Verifikasi kategori tanpa baris Changelog tidak muncul sebagai opsi

### TC-FA-CAT-404: Filter Changelog Date (date range) inklusif

24. Klik icon Filter, klik `[Clear Field]` pada Category Name, lalu pilih rentang tanggal 20 Jun sampai 22 Jun pada field Date dan klik `[Apply]`
25. Verifikasi hanya baris dengan Date di dalam rentang (inklusif) yang tampil
26. Klik icon Filter, klik `[Clear Field]` pada Date, klik `[Apply]`, lalu klik icon Close (✕) pada modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Langkah penghubung (S-03/S-09): membersihkan Filter di antara TC (langkah 11, 20, dan 24, tanpa Verifikasi) dan menutup modal di langkah 26; modal tidak dibuka ulang di antara TC karena state Filter dibersihkan.
- Rentang 20 Jun sampai 22 Jun pada TC-FA-CAT-404 mengacu pada baris contoh Pre-setup #23 (Example Data PRD §4.1).
- Temuan untuk QA:
  - TC-FA-CAT-402 menyebut "kelima Action yang ada di log" tanpa menamai kelimanya; spec mengasersi bahwa opsi Action sama dengan himpunan Action yang tercatat pada Pre-setup #23 (Create, Edit, Delete, Marked as Excess (Category Consolidation), Restored from Excess (Category Consolidation)).
  - TC-FA-CAT-403 langkah 3 dan 4 memilih dua opsi berbeda pada satu Apply; spec memisahkannya menjadi dua Apply agar Expected b dan c dapat diasersi sendiri-sendiri.
  - TC-FA-CAT-404 tidak menyebut tahun rentang tanggal.
