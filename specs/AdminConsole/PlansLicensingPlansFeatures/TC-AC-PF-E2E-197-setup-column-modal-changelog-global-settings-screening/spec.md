---
id: TC-AC-PF-E2E-197-setup-column-modal-changelog-global-settings-screening
title: Setup Column modal Changelog Global Settings screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-507
  - TC-AC-PF-508
  - TC-AC-PF-509
coverage:
  web: automated
---

# Setup Column modal Changelog Global Settings screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log G, Changelog Global Settings lima entri Edit (`Max depreciation methods (Multi Depreciation tier)` dan `Max custom fields per asset name`, 02 Jun 26 sampai 30 Jun 26, John D dan Sarah T). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Global Settings Principal tepat sama dengan Dataset Log G di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: blok TC-AC-PF-509 menyimpan preferensi kolom modal Changelog Global Settings (kolom `Old Value` disembunyikan) di browser (localStorage, cache sendiri per modal). Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Overlay Column Visibility (TC-AC-PF-507)

1. Klik tab Global Settings
2. Klik ikon Changelog di pojok kanan atas Card
3. Hover header kolom Actions (`⋯`)
4. Verifikasi tooltip header kolom Actions `Column Visibility`
5. Klik header kolom Actions (`⋯`)
6. Verifikasi Overlay Column Visibility memuat daftar kolom berurutan `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By`
7. Verifikasi tiap kolom pada overlay memiliki checkbox tercentang (Hideable, enabled)
8. Verifikasi tiap kolom pada overlay memiliki drag handle
9. Verifikasi item `Setup Column...` ada di bagian bawah overlay

### Popup Setup Column (TC-AC-PF-508)

10. Klik `Setup Column...` pada overlay
11. Verifikasi Header: Title `Setup Column`
12. Verifikasi Header: deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
13. Verifikasi Header: icon close `(X)` di kanan atas
14. Verifikasi Body: daftar kolom `Date`, `Action`, `Field`, `Old Value`, `New Value`, `Modified By` dengan checkbox tercentang
15. Verifikasi tiap kolom pada daftar memiliki drag handle
16. Verifikasi tiap kolom pada daftar memiliki icon Pin
17. Verifikasi Live Preview menampilkan urutan header kolom yang sama dengan tabel
18. Verifikasi Live Preview menampilkan data sel yang sama dengan tabel
19. Verifikasi Footer: tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
20. Verifikasi Footer: tidak ada tombol `[Cancel]`

### Ceklis dan unceklis kolom (TC-AC-PF-509)

21. Uncheck kolom `Old Value`
22. Verifikasi Live Preview tidak lagi menampilkan kolom `Old Value`
23. Verifikasi tabel di belakang modal tidak lagi menampilkan kolom `Old Value`
24. Klik `[Save]`
25. Verifikasi Popup Setup Column tertutup
26. Verifikasi tabel tanpa kolom `Old Value`
27. Tekan F5
28. Klik tab Global Settings
29. Klik ikon Changelog di pojok kanan atas Card
30. Verifikasi kolom `Old Value` tetap tidak tampil

## Notes

- Blok TC-AC-PF-508 melanjutkan overlay yang terbuka dari blok TC-AC-PF-507 (langkah 10 membuka popup dari item `Setup Column...`); blok TC-AC-PF-509 melanjutkan popup yang terbuka.
- Langkah 28 dan 29 membuka kembali modal karena F5 memuat ulang halaman.
- Temuan untuk QA:
  - TC-AC-PF-509 Expected b menulis "modal tertutup" untuk penutupan Popup Setup Column setelah `[Save]`; spec memverifikasi Popup Setup Column tertutup dan tabel di belakangnya tanpa kolom `Old Value`.
  - TC menetapkan lima entri sebagai seluruh isi Changelog Global Settings. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
