---
id: TC-FA-FAAC-E2E-001-screening-halaman-accounting-tab-asset-class-dan-navigasi
title: "Screening Halaman Settings > Accounting Tab Asset Class dan Urutan Empat Tab"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-1
  - TC-FA-FAAC-2
coverage:
  web: automated
---

# Screening Halaman Settings > Accounting Tab Asset Class dan Urutan Empat Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Spec ini menguji navigasi menu dan tab, sehingga langkah pertamanya mengklik menu Accounting dan tidak mengandalkan layar awal tab Asset Class. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_fa-asset-class` disetel true oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (hanya dibaca, tidak diubah): sembilan Asset Class contoh Example Data PRD §4.1.1 dengan nama literal dari Tabel Data Uji Pre-setup TC: HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Seed disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-FA-FAAC-1: Screening halaman Settings > Accounting tab Asset Class

1. Klik menu Accounting di sidebar
2. Klik tab Asset Class
3. Verifikasi breadcrumb `Settings > Accounting > Asset Class`
4. Verifikasi tab bar berurutan `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, `Asset Class` dengan tab `Asset Class` aktif
5. Verifikasi Table Tools memuat Search, Filter, Download, Changelog, dan tombol `[+ Asset Class]`
6. Arahkan kursor ke icon Search
7. Verifikasi tooltip `Search`
8. Arahkan kursor ke icon Filter
9. Verifikasi tooltip `Filter`
10. Arahkan kursor ke icon Download
11. Verifikasi tooltip `Download`
12. Arahkan kursor ke icon Changelog
13. Verifikasi tooltip `Changelog`
14. Klik icon Search
15. Verifikasi placeholder kotak Search `Search asset class...`
16. Verifikasi kolom tabel berurutan Checkbox, Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, Assets, Column Visibility (⋯)
17. Verifikasi kolom Active, Class Code, Class Name, Commercial, Fiscal, Capitalization Threshold, Accounts, Asset Names, dan Assets sortable dan kolom Column Visibility (⋯) unsortable
18. Verifikasi kolom Modified By dan Last Updated tidak tampil
19. Verifikasi chip filter aktif dan `Clear all` tidak tampil
20. Verifikasi footer paginasi dengan ukuran halaman 10
21. Verifikasi pilihan ukuran halaman 10 / 25 / 50 / 100

### TC-FA-FAAC-2: Urutan empat tab halaman Accounting

22. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
23. Klik menu Accounting di sidebar
24. Verifikasi tab bar memuat empat tab berurutan `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, `Asset Class`
25. Klik tab Chart of Accounts
26. Verifikasi tab `Chart of Accounts` aktif dan isi tab berganti
27. Klik tab Tax Depreciation Class
28. Verifikasi tab `Tax Depreciation Class` aktif dan isi tab berganti
29. Klik tab Asset Class
30. Verifikasi tab `Asset Class` aktif dan isi tab berganti
31. Verifikasi empat tab tetap tampil dengan urutan `Preferences`, `Chart of Accounts`, `Tax Depreciation Class`, `Asset Class` pada satu halaman Settings > Accounting

## Notes

- Langkah penghubung (S-03): langkah 22 (menutup input Search dan mereset tabel sebelum TC berikutnya, S-09; R-16).
- TC-FA-FAAC-1 butir c memuat keterangan fungsi kolom Column Visibility (⋯) (klik header membuka panel Column Visibility, body per baris adalah row action menu); TC tidak memberi langkah klik untuk keterangan itu, sehingga spec hanya mengasersi urutan kolom dan status sortable/unsortable (langkah 16 dan 17).
- Temuan untuk QA:
  - TC-FA-FAAC-1 langkah 3 ("Perhatikan halaman dari atas ke bawah") tidak memberi aksi; asersi mengikuti butir Expected a sampai e.
  - TC-FA-FAAC-1 langkah 1 mengawali dari klik menu Accounting, tetapi precondition TC menyatakan user sudah berada di Asset Class; spec mengikuti langkah TC.
- TC-FA-FAAC-3, TC-FA-FAAC-4, dan TC-FA-FAAC-587 (navigasi sidebar dan breadcrumb dari Detail) ada di spec 019.
