---
id: TC-FA-CAT-E2E-127-tabel-assets-detail-screening-overlay-column-visibility-dan-popup-setup-column
title: "Tabel Assets pada Popup Detail: Screening Overlay Column Visibility dan Popup Setup Column dengan Live Preview Tiga Zona"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-547
  - TC-FA-CAT-548
coverage:
  web: automated
---

# Tabel Assets pada Popup Detail: Screening Overlay Column Visibility dan Popup Setup Column dengan Live Preview Tiga Zona

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12); #21 (Asset Name `Laptop Dell`, `Laptop HP`); #22 (12 aset terhitung pada `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` (Model/Type `Latitude 5420`) dan `HP`; Group `Head Office > Floor 1 > Room 301`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia`, Model/Type `Elite Dragonfly G3 Notebook PC`, Group `Region Jawa > Jakarta Selatan Distribution Center`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`).
- Seed client Pre-setup dan aset (fixture backend, disediakan tim FE) mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Pre-setup #40 (label aset; dipakai bila kolom curated Label diuji) dan #56 (kolom Custom Field grup General yang Active) disediakan tim FE sebagai fixture backend; spec ini hanya membaca.
- Konfigurasi Setup Column yang disimpan spec ini dipulihkan di hook `after` dengan menghapus preferensi kolom di browser (butir "Pemulihan Setup Column" di `suite.md`), bukan lewat `[Reset to Default]`.

## Test Steps
1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-547: Screening overlay Column Visibility tabel Assets

3. Klik header kolom Actions (⋯)
4. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
5. Verifikasi daftar kolom Name, Asset ID, TAG, Brand, Model/Type, Group, Status, Last Updated masing-masing dengan checkbox ☑ Hideable (checked, enabled) dan drag handle
6. Verifikasi kolom curated Measurement, Label, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, dan kolom Custom Field grup General yang Active (Pre-setup #56) ada di daftar dengan checkbox ☐ (unchecked, enabled)
7. Verifikasi kolom Category tidak ada di daftar
8. Verifikasi Checkbox dan Actions tidak muncul sebagai baris di daftar

### TC-FA-CAT-548: Screening popup Setup Column dan Live Preview tabel Assets (3 zona)

9. Klik `Setup Column...` pada overlay Column Visibility
10. Verifikasi zona Header: Title `Setup Column`
11. Verifikasi zona Header: deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
12. Verifikasi zona Header: icon Close (✕)
13. Verifikasi zona Body: daftar kolom (Name, Asset ID, TAG, Brand, Model/Type, Measurement, Group, Label, Status, Transactional Policy, Last Scanned, Asset Value, Warranty Expiry, kolom Custom Field grup General yang Active, Last Updated) dengan checkbox, drag handle, icon Pin, dan Live Preview tabel
14. Verifikasi kolom Category tidak ada di daftar
15. Verifikasi zona Footer: `[Reset to Default]` dan `[Save]` rata kanan
16. Verifikasi tidak ada `[Cancel]`
17. Klik icon Close (✕) pada popup Setup Column, lalu klik icon Close (✕) pada popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Spec read-only; tidak ada `[Save]`.
- Langkah penghubung (S-03): langkah terakhir menutup popup Setup Column dan popup Detail tanpa Save.
- Expected TC-FA-CAT-547 butir b dipecah menjadi dua Verifikasi (kolom default, kolom curated) dan Category menjadi Verifikasi sendiri; TC-FA-CAT-548 butir a, b, c dipecah per klausa.
- Temuan untuk QA:
  - TC-FA-CAT-547 butir c ("Checkbox dan Actions tidak muncul sebagai baris") menulis "Checkbox" sebagai nama kolom; spec mengasersi kedua nama tidak muncul sebagai baris.
  - Urutan kolom daftar TC-FA-CAT-548 butir b (Measurement berada di antara Model/Type dan Group, Last Updated di akhir) berbeda dari urutan default tabel pada TC-FA-CAT-419; spec mengikuti butir b TC-FA-CAT-548 apa adanya.
