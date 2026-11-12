---
id: TC-FA-FAAC-E2E-122-setup-column-screening-dan-ceklis-kolom
title: "Setup Column Tabel Asset Class: Screening Panel dan Modal, Ceklis Kolom Tampil Bawaan, dan Ceklis Kolom Tersembunyi Bawaan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-395
  - TC-FA-FAAC-396
  - TC-FA-FAAC-397
  - TC-FA-FAAC-398
coverage:
  web: automated
---

# Setup Column Tabel Asset Class: Screening Panel dan Modal, Ceklis Kolom Tampil Bawaan, dan Ceklis Kolom Tersembunyi Bawaan

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (tab Asset Class pada Settings > Accounting). Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- Kondisi awal konfigurasi kolom: bawaan (sembilan kolom tampil, Modified By dan Last Updated tersembunyi); preferensi kolom browser bersih sebelum spec dimulai.
- State yang diubah spec: konfigurasi kolom tabel disimpan di browser (Column Visibility, localStorage). Dipulihkan oleh langkah 38 dan oleh hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]` (kemampuan disediakan tim FE; lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAC-395: Screening panel Column Visibility pada tabel Asset Class

1. Arahkan kursor ke ikon `⋯` pada header kolom Actions
2. Verifikasi tooltip ikon `⋯` berbunyi `Column Visibility`
3. Klik ikon `⋯` pada header kolom Actions
4. Verifikasi panel memuat daftar kolom berurutan: Active | Class Code | Class Name | Commercial | Fiscal | Capitalization Threshold | Accounts | Asset Names | Assets | Modified By | Last Updated, masing-masing dengan drag handle
5. Verifikasi checkbox Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, dan Assets tercentang dan Enabled
6. Verifikasi checkbox Modified By dan Last Updated tidak tercentang dan Enabled
7. Verifikasi item `Setup Column...` tampil di bagian bawah panel

### TC-FA-FAAC-396: Screening modal Setup Column tabel Asset Class

8. Klik `Setup Column...` pada panel
9. Verifikasi header modal memuat title `Setup Column`
10. Verifikasi header modal memuat deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`
11. Verifikasi header modal memuat tombol Close (X) di kanan atas
12. Verifikasi body modal: daftar sebelas kolom dengan status centang default (sembilan tercentang, Modified By dan Last Updated tidak tercentang), drag handle, dan icon Pin
13. Verifikasi tabel di balik modal menampilkan urutan header kolom sesuai daftar
14. Verifikasi footer modal: tombol `[Reset to Default]` dan `[Save]` rata kanan
15. Verifikasi tidak ada tombol `[Cancel]` pada footer

### TC-FA-FAAC-397: Ceklis dan unceklis kolom yang tampil secara bawaan

16. Hilangkan centang Active, Class Code, Class Name, dan Commercial pada modal Setup Column
17. Verifikasi kolom Active, Class Code, Class Name, dan Commercial sudah hilang dari tabel di balik modal sebelum Save
18. Klik `[Save]`
19. Verifikasi kolom Active, Class Code, Class Name, dan Commercial tetap hilang dari tabel setelah Save
20. Buka kembali modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
21. Centang lagi Active, Class Code, Class Name, dan Commercial, hilangkan centang Fiscal, Capitalization Threshold, Accounts, dan Asset Names, klik `[Save]`
22. Verifikasi kolom Fiscal, Capitalization Threshold, Accounts, dan Asset Names hilang
23. Verifikasi kolom Active, Class Code, Class Name, dan Commercial tampil kembali
24. Buka kembali modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
25. Centang lagi Fiscal, Capitalization Threshold, Accounts, dan Asset Names, hilangkan centang Assets, klik `[Save]`
26. Verifikasi kolom Assets hilang
27. Verifikasi kolom Fiscal, Capitalization Threshold, Accounts, dan Asset Names tampil kembali
28. Refresh halaman
29. Verifikasi kolom Class Code tampil
30. Verifikasi tabel tetap tanpa kolom Assets

### TC-FA-FAAC-398: Ceklis kolom yang tersembunyi secara bawaan

31. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
32. Centang Assets (dipulihkan), Modified By, dan Last Updated, klik `[Save]`
33. Verifikasi kolom Modified By dan Last Updated tampil di tabel setelah kolom Assets
34. Verifikasi Last Updated menjadi kolom data terakhir sebelum Actions
35. Refresh halaman
36. Verifikasi kolom Modified By dan Last Updated tetap tampil setelah refresh
37. Buka modal Setup Column (ikon `⋯` pada header kolom Actions, `Setup Column...`)
38. Hilangkan centang Modified By dan Last Updated, klik `[Save]`
39. Verifikasi kolom Modified By dan Last Updated hilang dari tabel kembali

## Notes

- Spec berlangkah 39, melewati sekitar 35 langkah; semua langkah satu topik (modal Setup Column) pada satu konfigurasi kolom browser yang dibangun berurutan, sehingga blok tidak dipisah dan tiap blok bergantung pada konfigurasi kolom blok sebelumnya.
- Langkah penghubung (S-03): langkah 16 melanjutkan modal yang masih terbuka dari langkah 8 (state sama dengan membuka modal dari awal); langkah 20, 24, 31, dan 37 membuka kembali modal; langkah 32 mengembalikan kolom Assets yang disembunyikan pada langkah 25 sebelum asersi urutan kolom (S-09); langkah 38 memulihkan konfigurasi kolom (S-09).
- Pada TC-FA-FAAC-397 langkah TC "Hilangkan centang ... lalu klik [Save]" dipisah menjadi dua langkah supaya asersi state sementara (tabel di balik modal, langkah 17) diamati sebelum Save (8b butir 5).
- Langkah 29 (`Verifikasi kolom Class Code tampil`) adalah anchor kolom lain sebelum asersi absence kolom Assets sesudah refresh (8b butir 2); langkah 30 mengasersi absence tersebut.
- Nama literal Pre-setup (sembilan kelas contoh) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan urutan kolom persis, dan data hanya dibaca (S-06, S-12).
- Temuan untuk QA: tidak ada.
