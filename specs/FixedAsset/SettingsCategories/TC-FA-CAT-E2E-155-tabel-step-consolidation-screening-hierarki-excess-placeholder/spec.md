---
id: TC-FA-CAT-E2E-155-tabel-step-consolidation-screening-hierarki-excess-placeholder
title: "Tabel Step Category Consolidation: Screening Kolom dan Sel, Toolbar, Placeholder Search, Pagination 10 Baris dengan Retensi Centang, Hierarki, Badge Excess, serta Last Updated dan Modified By"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-440
  - TC-FA-CAT-455
  - TC-FA-CAT-457
  - TC-FA-CAT-453
  - TC-FA-CAT-441
  - TC-FA-CAT-442
  - TC-FA-CAT-456
coverage:
  web: automated
---

# Tabel Step Category Consolidation: Screening Kolom dan Sel, Toolbar, Placeholder Search, Pagination 10 Baris dengan Retensi Centang, Hierarki, Badge Excess, serta Last Updated dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatPostT0 (Pre-setup #33), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua: Total Control (Pre-setup #1) pada client CatExcess (Pre-setup #31), password dari `Spectra.env.FA_TC_PASSWORD`. Login lewat langkah Ganti akun eksplisit (langkah 20). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (nama usulan, lihat Temuan untuk QA).
- Data Pre-setup #33 (CatPostT0, Starter cap 5, T-0 sudah lewat, belum pernah submit selection): 8 kategori root `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`; varian 12 kategori dengan tambahan `Extra 01` sampai `Extra 04` dipakai langkah 13 sampai 19 (TC-FA-CAT-453). Pergantian varian dan pemulihan ke 8 kategori lewat fixture backend yang disediakan tim FE/BE, dijalankan di langkah 13 dan hook `after`.
- Data Pre-setup #31 (CatExcess, Starter setelah downgrade, cap Category count 5, T-0 sudah lewat, 9 kategori): usable `Electronics` (L1) berisi `Laptop` dan `Monitor` (L2); Excess `Heavy Equipment` (Total Asset 0, Modified By System), `Vehicle`, `Furniture` (Total Asset 5). Total Control melihat Alert Category Consolidation. Data #31 hanya dibaca.
- Kemampuan teknis: membaca waktu penandaan Excess `Heavy Equipment` (Pre-setup #31) lewat kemampuan baca state BE untuk langkah 29; disediakan tim FE/BE tanpa endpoint karangan. Format Last Updated mengikuti General Settings client (format tanggal dan zona waktu).
- Spec tidak menyimpan seleksi Wizard; tidak ada state Pre-setup yang diubah kecuali varian #33 yang dipulihkan di atas. Suite berjalan serial (`parallel: false`).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Fixture `fixtures/settings-categories.json` disediakan tim FE.

## Test Steps

### TC-FA-CAT-440: Screening tabel Step, kolom dan format sel

1. Klik `[Choose Categories]` pada Alert Category Consolidation
2. Verifikasi kolom berurutan: Checkbox `Keep usable`, Category Name (sortable), Code, Depth, Total Asset, Status, Modified By, Last Updated, Column Visibility (⋯)
3. Verifikasi sel Depth baris pertama berformat `L1`
4. Verifikasi sel Total Asset baris pertama berupa angka bulat
5. Verifikasi sel Status baris pertama berupa badge `Usable` (success) atau `Excess` (warning)
6. Verifikasi Category Name baris L1 tampil sebagai nama exact tanpa indentasi
7. Verifikasi tabel berurutan Category Name A-Z (default sort) dengan baris pertama `Alpha Tech`

### TC-FA-CAT-455: Toolbar tabel Step hanya Search dan Filter tanpa Download

8. Verifikasi toolbar tabel Step memuat Search dan Filter
9. Verifikasi toolbar tidak memuat Download, Changelog, atau tombol create

### TC-FA-CAT-457: Placeholder Search tabel Step Consolidation

10. Klik icon Search di toolbar tabel Step
11. Verifikasi placeholder input Search `Search category name, code, status...`
12. Klik icon panah (←) di kiri toolbar untuk menutup kotak Search

### TC-FA-CAT-453: Pagination Step default 10 dan retensi centang lintas halaman

13. Klik `[Cancel]` pada wizard, alihkan Pre-setup #33 ke varian 12 kategori lewat fixture backend, lalu klik `[Choose Categories]` pada Alert Category Consolidation
14. Verifikasi tabel Step menampilkan 10 baris per halaman (default) pada halaman 1
15. Centang `Keep usable` pada `Alpha Tech`
16. Pindah ke halaman 2
17. Kembali ke halaman 1
18. Verifikasi centang `Keep usable` pada `Alpha Tech` dipertahankan
19. Hapus centang `Keep usable` pada `Alpha Tech` dan klik `[Cancel]` pada wizard

### TC-FA-CAT-441: Penanda hierarki, nama exact node berindentasi per level dan kolom Depth sejalan

20. Ganti akun: logout, login sebagai Total Control pada client CatExcess (Pre-setup #31) dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Categories
21. Klik `[Choose Categories]` pada Alert Category Consolidation
22. Verifikasi `Electronics` (L1) tampil tanpa indentasi
23. Verifikasi `Laptop` dan `Monitor` (L2) tampil berindentasi satu tingkat tanpa path dan tanpa prefix
24. Verifikasi kolom Depth menampilkan `L1` untuk `Electronics` dan `L2` untuk `Laptop` dan `Monitor`

### TC-FA-CAT-442: Baris Excess tampil di Step dengan badge Excess dan tetap dapat dicentang

25. Verifikasi baris `Furniture` dan `Heavy Equipment` berstatus badge `Excess` (warning)
26. Verifikasi checkbox `Keep usable` pada baris `Furniture` dan `Heavy Equipment` aktif
27. Verifikasi checkbox `Keep usable` pada baris `Furniture` dan `Heavy Equipment` tanpa pra-isi

### TC-FA-CAT-456: Last Updated dan Modified By pada tabel Step mengikuti perubahan Excess terakhir

28. Verifikasi Modified By baris `Heavy Equipment` menampilkan `System`
29. Verifikasi Last Updated baris `Heavy Equipment` sesuai waktu penandaan Excess dengan format General Settings

## Notes

- Langkah penghubung (S-03, S-09): langkah 12 (menutup kotak Search), langkah 13 (menutup wizard, mengalihkan varian #33, membuka wizard lagi), langkah 19 (membersihkan centang dan menutup wizard sebelum ganti akun).
- Urutan: TC-FA-CAT-455 dan TC-FA-CAT-457 ditaruh sesudah TC-FA-CAT-440 pada wizard yang sama; TC-FA-CAT-453 (varian 12 kategori) di akhir blok #33; blok #31 (TC-FA-CAT-441, 442, 456) memerlukan ganti akun karena client berbeda (S-10).
- TC Step Consolidation lain (Search, sort, Filter, Setup Column, paginasi lanjut) ada di spec 156 sampai 163.
- Temuan untuk QA:
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan, termasuk untuk client CatExcess dan CatPostT0.
  - TC-FA-CAT-440 Expected b dan c (Depth `L2`, Category Name bersarang berindentasi) tidak teramati pada Pre-setup #33 karena seluruh 8 kategorinya root; spec memverifikasi sel L1 dan nama tanpa indentasi, sedangkan hierarki bersarang diverifikasi di TC-FA-CAT-441 pada Pre-setup #31.
  - TC-FA-CAT-440 Expected b menyebut status `Usable` atau `Excess` tanpa menyebut kondisi tiap baris Pre-setup #33; spec memverifikasi bahwa badge salah satu dari keduanya.
  - TC-FA-CAT-456 tidak menyebut cara mengetahui "waktu penandaan Excess"; spec memakainya sebagai kemampuan baca BE yang disediakan tim FE/BE.
