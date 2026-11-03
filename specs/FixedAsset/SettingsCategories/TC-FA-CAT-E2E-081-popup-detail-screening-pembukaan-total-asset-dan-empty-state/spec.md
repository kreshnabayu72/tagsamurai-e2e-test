---
id: TC-FA-CAT-E2E-081-popup-detail-screening-pembukaan-total-asset-dan-empty-state
title: "Popup Detail Category: Screening Header dan Body, Tiga Jalur Pembukaan, Total Asset Header, dan Empty State Total Asset 0"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-272
  - TC-FA-CAT-273
  - TC-FA-CAT-274
  - TC-FA-CAT-275
coverage:
  web: automated
---

# Popup Detail Category: Screening Header dan Body, Tiga Jalur Pembukaan, Total Asset Header, dan Empty State Total Asset 0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca (spec read-only, tidak membuat data): #20 `Electronics` (Code `ELEC`) berisi `Laptop` (Code `ELEC-LT`, Total Asset 12) dan `Monitor` (Code `ELEC-MN`, Total Asset 0); Pre-setup #21 (Asset Name `Laptop Dell`, `Laptop HP`) dan #22 (12 aset terhitung pada `Laptop`).
- Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-272: Screening Popup Detail Category

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Verifikasi Title flat `Category Detail` (bukan nama record)
4. Verifikasi Category Name berupa full path `Electronics › Laptop`
5. Verifikasi Code `ELEC-LT`
6. Verifikasi Description tampil full-width
7. Verifikasi icon Close (✕) di kanan atas
8. Verifikasi tabel Assets (T-FACAT-03) tampil tanpa tab bar
9. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
10. Verifikasi popup berukuran besar (`lg`) dengan body scrollable
11. Verifikasi popup tanpa Breadcrumb
12. Verifikasi popup tanpa button teks `Close`
13. Verifikasi header tanpa tombol Edit atau Delete
14. Klik icon Close (✕)

### TC-FA-CAT-273: Popup Detail dibuka dari klik nama, row action Detail, dan angka Total Asset

15. Klik nama `Laptop` pada tabel
16. Verifikasi popup `Category Detail` untuk `Laptop` terbuka dengan tabel Assets berisi 12 aset
17. Klik icon Close (✕)
18. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
19. Verifikasi popup `Category Detail` untuk `Laptop` terbuka dengan tabel Assets berisi 12 aset
20. Klik icon Close (✕)
21. Klik angka Total Asset `12` pada baris `Laptop`
22. Verifikasi popup `Category Detail` untuk `Laptop` terbuka dengan tabel Assets berisi 12 aset
23. Klik icon Close (✕)

### TC-FA-CAT-274: Angka Total Asset pada Category Context Header membuka popup Detail node itu

24. Klik node `Laptop` di Sidebar Category Tree
25. Klik angka Total Asset `12` pada Category Context Header
26. Verifikasi popup `Category Detail` untuk `Laptop` terbuka dengan himpunan aset yang sama dengan angka header
27. Klik icon Close (✕)

### TC-FA-CAT-275: Total Asset 0 dapat diklik dan menampilkan empty state S-09

28. Klik node `Electronics` di Sidebar Category Tree
29. Klik angka Total Asset `0` pada baris `Monitor`
30. Verifikasi area tabel Assets menampilkan ilustrasi dengan Title `No assets assigned` dan Description `No assets are currently assigned to this category.`
31. Klik icon Close (✕)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. TC-FA-CAT-278, TC-FA-CAT-279, dan TC-FA-CAT-280 ada di spec 188.
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): klik node sidebar untuk membuka konteks, klik icon Close (✕) untuk menutup popup.
- Tiga jalur pada TC-FA-CAT-273 diasersi satu `Verifikasi` per jalur (parameter tiap iterasi berbeda).
- Temuan untuk QA:
  - TC-FA-CAT-272 tidak menyebut nilai Description `Laptop`; spec hanya meng-assert Description tampil full-width.
  - TC-FA-CAT-273 menyebut "tabel Assets berisi 12 aset" sementara pagination default 10; spec mengikuti TC dan tidak mengatur jumlah baris per halaman.
