---
id: TC-AC-LA-E2E-001-screening-list-tab-current-history-dan-tooltip
title: "Screening List License Allocation: Tab Current, Tab History, dan Tooltip Table Tools"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-1
  - TC-AC-LA-2
  - TC-AC-LA-3
coverage:
  web: automated
---

# Screening List License Allocation: Tab Current, Tab History, dan Tooltip Table Tools

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Kemampuan teknis: tidak ada selain seed Pre-setup #54 yang sudah tersedia.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-1: Screening halaman List tab Current

1. Susuri Zona 1 (Header), Zona 2 (Body), dan Zona 3 (Footer) halaman Allocation > License Allocation tab Current dari atas ke bawah
2. Amati baris pertama tabel
3. Verifikasi Header: Breadcrumb `Allocation > License Allocation` (2 segmen, keduanya teks statis tidak bisa diklik)
4. Verifikasi Header: Tab `Current (aktif) | History`
5. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Allocation]` tampil
6. Verifikasi Body: kolom default `Allocation ID (sortable) | License Type (sortable) | Product (sortable) | Client (sortable) | Subscription ID (sortable) | Quantity (sortable) | Plan Owner (sortable) | Allocated By (sortable) | Status (sortable) | Last Updated (sortable) | Column Visibility (⋯)`; header Column Visibility (⋯) unsortable, klik header membuka overlay Column Visibility, dan body per baris adalah row action menu
7. Verifikasi Body: kolom Plan, Payment, Paid From, dan Cost tidak tampil secara default
8. Verifikasi Body: tidak ada kolom checkbox seleksi baris dan tidak ada bar aksi massal
9. Verifikasi Body: tidak ada Page Title terpisah di bawah Breadcrumb
10. Verifikasi Footer: pagination default 10 data per halaman

### TC-AC-LA-2: Screening halaman List tab History

11. Klik tab `History`
12. Amati Zona 1, Zona 2, dan Zona 3 tab History
13. Verifikasi Header: Breadcrumb `Allocation > License Allocation`
14. Verifikasi Header: Tab `Current | History (aktif)`
15. Verifikasi Header: Table Tools `Search | Filter | Download` tampil
16. Verifikasi Header: ikon Changelog dan tombol `[+ Allocation]` tidak dirender
17. Verifikasi Body: kolom sama dengan tab Current: `Allocation ID (sortable) | License Type (sortable) | Product (sortable) | Client (sortable) | Subscription ID (sortable) | Quantity (sortable) | Plan Owner (sortable) | Allocated By (sortable) | Status (sortable) | Last Updated (sortable) | Column Visibility (⋯)`
18. Verifikasi Body: sedikitnya satu baris tampil pada tabel tab History
19. Verifikasi Body: seluruh baris hanya berstatus `Expired`, `Rejected`, dan `Canceled`
20. Verifikasi Footer: pagination default 10 data per halaman

### TC-AC-LA-3: Tooltip ikon Table Tools dan header Column Visibility

21. Klik tab `Current`
22. Hover ikon Search
23. Verifikasi tooltip ikon Search: `Search`
24. Hover ikon Filter
25. Verifikasi tooltip ikon Filter: `Filter`
26. Hover ikon Download
27. Verifikasi tooltip ikon Download: `Download`
28. Hover ikon Changelog
29. Verifikasi tooltip ikon Changelog: `Changelog`
30. Hover ikon `⋯` pada header kolom Actions
31. Verifikasi tooltip header kolom Actions `⋯`: `Column Visibility`

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah susur halaman, langkah `Amati`, dan langkah pindah tab (`Klik tab`). Langkah 1 TC-AC-LA-1 dan TC-AC-LA-2 (`Buka Allocation > License Allocation`) dilakukan hook `beforeEach` suite.
- Daftar kolom, daftar ikon Table Tools, dan pasangan tab ditulis sebagai satu `Verifikasi` karena Expected TC menyebutnya utuh dalam satu butir (S-01).
- Jumlah langkah di bawah 35; tidak ada TC sumber yang ditangani di spec lain.
- Temuan untuk QA:
  - TC-AC-LA-1 menamai kolom terakhir `Column Visibility (⋯)`, sedangkan TC-AC-LA-3 langkah 5 menyebutnya `header kolom Actions`; nama kolom tidak konsisten antar TC.
  - TC-AC-LA-2 Expected b.ii (`Hanya baris berstatus Expired, Rejected, dan Canceled`) adalah asersi universal atas halaman pertama tabel; spec menambah `Verifikasi` pembanding (sedikitnya satu baris tampil) sesuai bagian 8b butir 2.
