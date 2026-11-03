---
id: TC-AC-PF-E2E-185-setup-column-modal-changelog-default-screening-ceklis
title: Setup Column modal Changelog Default screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-475
  - TC-AC-PF-476
  - TC-AC-PF-477
coverage:
  web: automated
---

# Setup Column modal Changelog Default screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (nama tampil Andi Wijaya; entitas Principal; Global Role Manage plans & licensing Create, Read, Update, Delete); password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env: `AC_TC_PASSWORD` (password Total Control Principal).
- Data Pre-setup: Dataset Log D, Changelog Default Principal lima entri, terbaru dahulu: `12 Aug 26, 09:00` Create `Enterprise` (Plan Name, Old `—`, New `Enterprise`, Jane S); `01 Aug 26, 08:00` Archive `Growth Plus (old)` (Status, Old `Active`, New `Archived`, Jane S); `20 Jul 26, 10:00` Push Update `PT Wahana Nusantara` (Plan Version, Old `v1`, New `v5`, Sarah T); `10 Jul 26, 12:00` Delete `Pilot Default` (Plan Name, Old `Pilot Default`, New `—`, John D); `05 Jun 26, 15:40` Edit `Growth` (Group count, Old `3`, New `5`, Jane S). Nilai data dirujuk lewat `fixtures/plans-licensing-plans-features.json` (belum ada; ditandai untuk tim FE, S-12).
- General Settings akun: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC; tidak diubah spec ini.
- Pengecualian S-06/S-12 butir A-14: dataset memakai nama literal tanpa suffix dari Pre-setup TC. Fixture BE yang disediakan tim FE/BE (idempoten) menyetel Changelog Principal tepat sama dengan Dataset Log D di hook `before` dan memulihkannya ke baseline di hook `after`; suite berjalan serial (`parallel: false`). Spec ini hanya membaca data itu.
- Kemampuan teknis (disediakan tim FE/BE): fixture BE penyetel Changelog; sesi API aktor, klien HTTP, dan flag Guided Tooltip sesuai pernyataan di `suite.md`.
- State global: blok TC-AC-PF-477 menyimpan preferensi kolom modal Changelog Default (kolom `Old Value` disembunyikan) di browser (localStorage, cache sendiri per modal). Hook `after` menghapus preferensi kolom itu di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Overlay Column Visibility (TC-AC-PF-475)

1. Klik ikon Changelog pada toolbar tab Default
2. Hover header kolom Actions (`⋯`)
3. Verifikasi tooltip header kolom Actions `Column Visibility`
4. Klik header kolom Actions (`⋯`)
5. Verifikasi Overlay Column Visibility memuat daftar kolom berurutan `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By`
6. Verifikasi tiap kolom pada overlay memiliki checkbox tercentang (Hideable, enabled)
7. Verifikasi tiap kolom pada overlay memiliki drag handle
8. Verifikasi item `Setup Column...` ada di bagian bawah overlay

### Popup Setup Column (TC-AC-PF-476)

9. Klik `Setup Column...` pada overlay
10. Verifikasi Header: Title `Setup Column`
11. Verifikasi Header: deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
12. Verifikasi Header: icon close `(X)` di kanan atas
13. Verifikasi Body: daftar kolom `Date`, `Action`, `Plan Name`, `Field`, `Old Value`, `New Value`, `Modified By` dengan checkbox tercentang
14. Verifikasi tiap kolom pada daftar memiliki drag handle
15. Verifikasi tiap kolom pada daftar memiliki icon Pin
16. Verifikasi Live Preview menampilkan urutan header kolom yang sama dengan tabel
17. Verifikasi Live Preview menampilkan data sel yang sama dengan tabel
18. Verifikasi Footer: tombol `[Reset to Default]` (text, primary) dan `[Save]` (filled, success)
19. Verifikasi Footer: tidak ada tombol `[Cancel]`

### Ceklis dan unceklis kolom (TC-AC-PF-477)

20. Uncheck kolom `Old Value`
21. Verifikasi Live Preview tidak lagi menampilkan kolom `Old Value`
22. Verifikasi tabel di belakang modal tidak lagi menampilkan kolom `Old Value`
23. Klik `[Save]`
24. Verifikasi Popup Setup Column tertutup
25. Verifikasi tabel tanpa kolom `Old Value`
26. Tekan F5
27. Klik ikon Changelog pada toolbar tab Default
28. Verifikasi kolom `Old Value` tetap tidak tampil

## Notes

- Blok TC-AC-PF-476 melanjutkan overlay yang terbuka dari blok TC-AC-PF-475 (langkah 9 membuka popup dari item `Setup Column...`); blok TC-AC-PF-477 melanjutkan popup yang terbuka.
- Langkah 27 membuka kembali modal karena F5 memuat ulang halaman.
- Temuan untuk QA:
  - TC-AC-PF-477 Expected b menulis "modal tertutup" untuk penutupan Popup Setup Column setelah `[Save]`; spec memverifikasi Popup Setup Column tertutup dan tabel di belakangnya tanpa kolom `Old Value`.
  - TC menetapkan lima baris sebagai seluruh isi Changelog Default. Changelog adalah audit trail permanen (S-12), sehingga asersi bergantung pada fixture BE penyetel log yang tidak tertulis di TC, PRD, atau LLD (S-13).
  - `suite.md` belum mendaftarkan pemulihan preferensi kolom di hook `after` (bagian 4 konvensi).
