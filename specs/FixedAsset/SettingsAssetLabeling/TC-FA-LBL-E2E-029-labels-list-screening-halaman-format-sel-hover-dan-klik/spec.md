---
id: TC-FA-LBL-E2E-029-labels-list-screening-halaman-format-sel-hover-dan-klik
title: "Labels List: screening halaman, format sel, hover, dan klik kolom Label dan Total Asset"
priority: Medium
caseType: Positive
status: draft
sourceRules:
  - FALB:obl/page-asset-master-tab-labels/screening
  - FALB:global-table-rules/toolbar
  - FALB:obl/T-ALB-01/screening
  - FALB:obl/T-ALB-01/cell-format
  - FALB:obl/T-ALB-01/link/FLD-01
  - FALB:obl/T-ALB-01/link/FLD-03
  - FALB:obl/T-ALB-01/hover/FLD-04
  - FALB:defaults-ordering-spec/format-hex-warna
coverage:
  web: automated
---

# Labels List: screening halaman, format sel, hover, dan klik kolom Label dan Total Asset

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control `DU-01` (env `FA_TC_EMAIL`, `FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Asset Master > tab Labels dibuka hook `beforeEach` suite.
- Data uji: `DU-56` (12 label bersuffix `Lst-{runId}-029-01` sampai `Lst-{runId}-029-12`, Total Asset 0 sampai 3 lewat aset Active bersuffix yang dilabeli, Modified By dari dua pelaku, dua kelompok Last Updated berbeda menit). `DU-31` (akun Total Control kedua, env `FA_TC2_EMAIL`, `FA_TC2_PASSWORD`) dipakai hanya sebagai pelaku kedua lewat sesi API saat seeding sebagian label `DU-56`; tidak login di UI.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor dan fixture BE untuk seeding label dan aset serta penempelan label. Hook `before` menunggu pergantian menit (maksimum 60 detik, konvensi bagian 6) di antara dua kelompok seed `DU-56`.
- Format tanggal dan jam kolom Last Updated mengikuti General Settings client yang sedang aktif.
- State global: tidak ada yang diubah. Hook `after` menghapus label seed `DU-56` beserta aset seed lewat sesi API.

## Test Steps

### FALB:obl/page-asset-master-tab-labels/screening: Screening halaman tab Labels

1. Verifikasi breadcrumb halaman menampilkan `Settings > Asset Master > Labels`
2. Verifikasi tab Asset Master berurutan `Asset Name | Custom Asset ID | Labels` dengan tab `Labels` aktif
3. Verifikasi SectionCard memuat toolbar di bagian atas, Labels List di bagian tengah, dan Pagination di bagian bawah

### FALB:global-table-rules/toolbar: Urutan elemen toolbar

4. Verifikasi toolbar rata kanan menampilkan berurutan Input Search (ikon 🔍), Filter Panel Trigger, Download, Changelog Trigger, dan tombol `[+ Label]`

### FALB:obl/T-ALB-01/screening: Screening kolom Labels List

5. Ketik Search `DU-56` (nama dasar `Lst-{runId}-029`), tekan Enter
6. Verifikasi Labels List menampilkan sedikitnya dua baris label `DU-56`
7. Verifikasi header kolom data Labels List berurutan `Label | Color Hex | Total Asset | Modified By | Last Updated` dan seluruhnya sortable
8. Verifikasi kolom Checkbox berada paling kiri dan kolom Actions (`⋯`) paling kanan pada Labels List
9. Verifikasi tidak ada kolom Hidden atau kolom lain di luar kelima kolom data yang tampil pada Labels List

### FALB:obl/T-ALB-01/cell-format: Format sel tiap kolom

10. Verifikasi kolom Label menampilkan chip badge berlatar warna label dengan teks kontras pada tiap baris `DU-56` di halaman pertama
11. Verifikasi kolom Color Hex menampilkan kode berformat `#RRGGBB` pada tiap baris `DU-56` di halaman pertama
12. Verifikasi kolom Total Asset menampilkan angka bulat rata kanan berbentuk link pada tiap baris `DU-56` di halaman pertama
13. Verifikasi kolom Modified By menampilkan format `[First Name] [Last Initial]`, bukan nama lengkap, pada tiap baris `DU-56` di halaman pertama
14. Verifikasi kolom Last Updated menampilkan tanggal dan jam sesuai format General Settings pada tiap baris `DU-56` di halaman pertama
15. Verifikasi tidak ada sel kosong pada kelima kolom data baris `DU-56` di halaman pertama

### FALB:obl/T-ALB-01/link/FLD-01: Klik kolom Label membuka Drawer Tagged Asset

16. Klik chip Label pada baris `DU-56` ke-01 (baris pertama menurut sort bawaan Label A→Z)
17. Verifikasi Drawer Tagged Asset tampil dengan judul `Tagged Assets`
18. Verifikasi blok info Drawer memuat chip Label, Color Hex, dan Total Asset baris `DU-56` ke-01
19. Klik `[✕]` pada header Drawer Tagged Asset

### FALB:obl/T-ALB-01/link/FLD-03: Klik kolom Total Asset membuka Drawer Tagged Asset

20. Klik angka Total Asset pada baris `DU-56` ke-01
21. Verifikasi Drawer Tagged Asset tampil dengan judul `Tagged Assets`
22. Verifikasi blok info Drawer memuat chip Label dan Total Asset baris `DU-56` ke-01
23. Klik `[✕]` pada header Drawer Tagged Asset

### FALB:obl/T-ALB-01/hover/FLD-04: Hover kolom Modified By menampilkan nama lengkap

24. Arahkan kursor ke sel Modified By pada baris `DU-56` yang dimodifikasi `DU-31`
25. Verifikasi tooltip menampilkan nama lengkap user `DU-31`

### FALB:defaults-ordering-spec/format-hex-warna: Format hex warna

26. Verifikasi setiap kode pada kolom Color Hex baris `DU-56` di halaman pertama terdiri atas tanda pagar diikuti 6 karakter alfanumerik huruf kapital

## Notes

- Langkah penghubung (S-03): langkah 5 (Search yang mempersempit tabel ke label `DU-56` supaya baris target ada di halaman pertama, R-16), langkah 19 dan 23 (menutup Drawer sebelum blok berikutnya).
- Anchor positif (bagian 8b butir 2): langkah 6 membuktikan baris `DU-56` sudah termuat sebelum langkah 9 dan 15 mengasersi ketiadaan kolom lain dan ketiadaan sel kosong.
- Tabel 1 PRD §4.1.1 tidak punya kolom Hidden; klausa "kolom Hidden tidak tampil" pada langkah 9 berarti tidak ada kolom lain di luar kelima kolom data.
- Langkah 16 dan 20 memakai baris `DU-56` ke-01 (urutan sort bawaan Label A→Z); isi Drawer selain blok info identitas dimiliki spec lain yang mengutip aturan Drawer.
- Nama lengkap user `DU-31` pada langkah 25 dibaca dari profil akun itu.
