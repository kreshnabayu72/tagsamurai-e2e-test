---
id: TC-GS-BRAND-E2E-001-screening-tab-brand-layout-dan-tooltip
title: "Screening Tab Brand: Layout, Tab Default, Tooltip Table Tools, dan Layout Tablet"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-2
  - TC-GS-BRAND-3
  - TC-GS-BRAND-6
  - TC-GS-BRAND-254
coverage:
  web: automated
---

# Screening Tab Brand: Layout, Tab Default, Tooltip Table Tools, dan Layout Tablet

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture; nama env `GS_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup Client A (12 brand, data environment tetap): Acme Corp, Brightway, Duo Brand, Helix Works, Kestrel, Lumina Co, Nimbus Gear, Northwind Co, Orion Tech, Tagline Co, Vertex Labs, Zenith Corp. Brand Vertex Labs memiliki 5 Item Type (Used By (Items) = 5).
- Data Dinamis: Population D-01 (12 brand, Apex Tools sampai Linear Dynamics, nama literal tanpa suffix karena asersi jumlah dan halaman bergantung pada kumpulan nama ini) di-seed lewat API di hook `before` (setara TC-GS-BRAND-1) secara idempotent: nama yang sudah ada di Client A dilewati, sehingga total tetap 24 brand. Suite berjalan serial, jadi tidak ada spec lain yang men-seed atau menghapus Population bersamaan. Hook `after` hanya menghapus brand yang dibuat spec ini lewat API. Pembersihan tidak berasumsi seeding berhasil penuh.
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-brand` lalu menyetelnya ke true lewat API supaya walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal.
- Kemampuan teknis: mengubah lebar viewport (768px untuk TC-GS-BRAND-254); dipulihkan di langkah 35, dengan hook `after` sebagai cadangan.
- State global yang diubah: hanya flag Guided Tooltip dan viewport (dipulihkan seperti di atas). Tidak ada perubahan plan, status Client, atau format tanggal.

## Test Steps

### TC-GS-BRAND-2: Screening tab Brand oleh Total Control

1. Buka Global Settings > Master Reference dari sidebar → tab Brand tampil
2. Perhatikan tab Brand dari atas ke bawah tanpa mengisi atau mengklik apa pun
3. Verifikasi Header: Breadcrumb `Master Reference > Brand` dengan trigger Guided Tooltip `[?]`
4. Verifikasi Header: Tab `Brand (aktif) | Measurement`
5. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog | [+ Brand]` dan `[+ Brand]` bergaya filled primary
6. Verifikasi Body: header kolom `Checkbox | Brand Name (sortable, text link) | Used By (Items) (sortable, angka link) | Last Updated (sortable) | Column Visibility (⋯) (unsortable)`
7. Klik header kolom Column Visibility (⋯)
8. Verifikasi Overlay Column Visibility terbuka dengan item `Setup Column...` di dalamnya
9. Tutup Overlay Column Visibility dengan menekan Esc
10. Verifikasi Body: 10 baris pertama dari 24 brand tampil
11. Verifikasi Body: setiap baris memiliki row action menu pada kolom Column Visibility (⋯)
12. Verifikasi Footer: Pagination default 10 per halaman dan 3 halaman
13. Verifikasi Footer: opsi page size 10/25/50/100

### TC-GS-BRAND-3: Tab aktif default saat pertama masuk Master Reference adalah Brand

14. Verifikasi Tab `Brand` aktif pada tampilan Master Reference yang dibuka di langkah 1
15. Verifikasi Breadcrumb `Master Reference > Brand`
16. Klik Tab Measurement
17. Verifikasi Breadcrumb berubah menjadi `Master Reference > Measurement`
18. Klik Tab Brand untuk kembali ke tab Brand

### TC-GS-BRAND-6: Hover icon Table Tools menampilkan tooltip

19. Hover icon Search
20. Verifikasi tooltip `Search`
21. Hover icon Filter
22. Verifikasi tooltip `Filter`
23. Hover icon Download
24. Verifikasi tooltip `Download`
25. Hover icon Changelog
26. Verifikasi tooltip `Changelog`
27. Hover header kolom Column Visibility (⋯)
28. Verifikasi tooltip `Column Visibility`

### TC-GS-BRAND-254: Layout tabel pada lebar tablet

29. Ubah lebar viewport menjadi lebar tablet 768px
30. Buka Tab Brand (muat ulang Global Settings > Master Reference)
31. Pindah ke halaman 3 pada Pagination sampai baris Vertex Labs terlihat
32. Verifikasi tampilan tetap berupa tabel penuh, bukan card list
33. Verifikasi kolom Used By (Items) baris Vertex Labs menampilkan angka `5`
34. Verifikasi Toolbar tetap horizontal
35. Kembalikan lebar viewport ke ukuran awal

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan. TC-GS-BRAND-254 (ubah viewport) ditaruh terakhir karena mengubah state browser.
- TC-GS-BRAND-3 berbagi pembukaan Master Reference dengan TC-GS-BRAND-2 (langkah 1): "pertama masuk" dipenuhi oleh pembukaan awal di spec ini, jadi tidak ada pembukaan ulang.
- TC-GS-BRAND-2 pada langkah 7 sampai 9 menambah pengecekan klik header Column Visibility (⋯) karena Expected Result TC mendeskripsikan perilaku klik header itu (membuka Overlay Column Visibility); langkah 11 memeriksa row action menu per baris dari deskripsi kolom yang sama.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 9 (tutup Overlay Column Visibility dengan Esc), 18 (kembali ke Tab Brand), 31 (pindah ke halaman 3 supaya baris Vertex Labs terlihat), 35 (pulihkan viewport).
- Halaman 3 pada Pagination berisi Orion Tech, Tagline Co, Vertex Labs, dan Zenith Corp (urutan default A-Z, 10 per halaman, 24 brand).
