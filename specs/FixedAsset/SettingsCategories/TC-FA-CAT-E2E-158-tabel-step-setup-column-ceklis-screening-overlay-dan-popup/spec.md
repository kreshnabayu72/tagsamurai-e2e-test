---
id: TC-FA-CAT-E2E-158-tabel-step-setup-column-ceklis-screening-overlay-dan-popup
title: "Tabel Step Category Consolidation: Screening Overlay Column Visibility dan Popup Setup Column, serta Ceklis Tiap Kolom dengan Live Preview dan Persistensi Save"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-565
  - TC-FA-CAT-566
  - TC-FA-CAT-452
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Screening Overlay Column Visibility dan Popup Setup Column, serta Ceklis Tiap Kolom dengan Live Preview dan Persistensi Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection) hanya dibaca: 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Kolom yang diuji pada langkah 15 sampai 18 (langkah diulang untuk setiap baris tabel): `Category Name`, `Code`, `Depth`, `Total Asset`, `Status`, `Modified By`, `Last Updated`.
- State yang diubah spec: konfigurasi kolom tabel Step (langkah 19). Dipulihkan dengan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) pada langkah 26 dan hook `after` suite; kemampuan disediakan tim FE.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

1. Klik `[Choose Categories]` pada Alert Category Consolidation

### TC-FA-CAT-565: Screening overlay Column Visibility tabel Step

2. Klik header kolom Actions (⋯)
3. Verifikasi overlay memuat item `Setup Column...` di bagian bawah
4. Verifikasi daftar kolom Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated masing-masing memiliki checkbox ☑ Hideable (checked, enabled)
5. Verifikasi daftar kolom Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated masing-masing memiliki drag handle
6. Verifikasi Checkbox dan Actions tidak muncul sebagai baris di daftar

### TC-FA-CAT-566: Screening popup Setup Column dan Live Preview tabel Step (3 zona)

7. Klik item `Setup Column...`
8. Verifikasi Zona Header: Title `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan icon Close (✕)
9. Verifikasi Zona Body: daftar kolom Category Name, Code, Depth, Total Asset, Status, Modified By, Last Updated masing-masing dengan checkbox
10. Verifikasi daftar kolom pada Zona Body masing-masing memiliki drag handle
11. Verifikasi daftar kolom pada Zona Body masing-masing memiliki icon Pin
12. Verifikasi Zona Body memuat Live Preview tabel
13. Verifikasi Zona Footer: `[Reset to Default]` dan `[Save]` rata kanan
14. Verifikasi Zona Footer tidak memuat `[Cancel]`

### TC-FA-CAT-452: Setup Column tabel Step, ceklis tiap kolom, Save, dan persistensi

15. Hilangkan centang kolom pada tabel Kolom yang diuji
16. Verifikasi Live Preview menyembunyikan kolom itu
17. Centang kembali kolom itu
18. Verifikasi Live Preview menampilkan kolom itu kembali
19. Hilangkan centang kolom `Depth` dan `Code`, lalu klik `[Save]`
20. Verifikasi tabel Step memuat kolom Category Name, Total Asset, Status, Modified By, dan Last Updated
21. Verifikasi tabel Step tidak memuat kolom `Depth` dan `Code`
22. Tekan F5
23. Klik `[Choose Categories]` pada Alert Category Consolidation
24. Verifikasi tabel Step memuat kolom Category Name, Total Asset, Status, Modified By, dan Last Updated
25. Verifikasi tabel Step tidak memuat kolom `Depth` dan `Code` (konfigurasi bertahan setelah F5)
26. Pulihkan konfigurasi kolom tabel Step dengan menghapus preferensi kolom di browser

## Notes

- Spec melewati sekitar 35 langkah setelah ekspansi (26 langkah nominal, ceklis tujuh kolom diulang: 4 langkah x 7 = 28, total sekitar 50). Alasan: seluruh blok satu kelas fungsional pada popup Setup Column tabel Step yang sama, berdiri sendiri, dan langkah ceklis identik per kolom dengan parameter di butir `Kolom yang diuji` (bagian 8b butir 7). Langkah yang diulang: 15 sampai 18.
- Urutan: TC-FA-CAT-565 dan TC-FA-CAT-566 (screening) mendahului TC-FA-CAT-452 yang menyimpan konfigurasi kolom (S-10); popup tetap terbuka dari langkah 7 ke langkah 15.
- Langkah penghubung (S-03, S-09): langkah 1, 23 (membuka wizard), langkah 26 (memulihkan konfigurasi kolom).
- Asersi absence pada langkah 21 dan 25 diawali anchor positif berupa kolom lain yang tampil pada tabel yang sama (langkah 20 dan 24; R-21 untuk sesudah F5).
- Daftar kolom, checkbox, drag handle, dan icon Pin pada langkah 4 sampai 5 dan 9 sampai 11 dipecah per klausa sesuai S-01.
- Pin, geser urutan, Reset to Default, dan penutupan popup tanpa Save ada di spec 159 dan 160.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
  - TC-FA-CAT-452 langkah 11 ("Tekan F5") tidak menyebut membuka kembali wizard; spec menambah langkah 23 (TC-FA-CAT-567 menyebut "buka kembali tabel").
  - TC-FA-CAT-565 Expected b menyebut "checkbox ☑ Hideable (checked, enabled) dan drag handle" untuk daftar kolom; spec memecahnya per klausa.
