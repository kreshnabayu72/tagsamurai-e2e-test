---
id: TC-FA-CAT-E2E-001-screening-halaman-categories-list
title: "Screening Halaman Categories List: Breadcrumb, Sidebar Category Tree, dan Loading"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-1
  - TC-FA-CAT-2
  - TC-FA-CAT-3
  - TC-FA-CAT-4
  - TC-FA-CAT-12
  - TC-FA-CAT-25
coverage:
  web: automated
---

# Screening Halaman Categories List: Breadcrumb, Sidebar Category Tree, dan Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data: client CatMain (Pre-setup #20, plan Enterprise): 15 kategori; L1 `Accessory`, `Default Category`, `Electronics` (anak `Laptop`, `Monitor`), `Furniture`, `Peripheral` (anak `Keyboard`, `Mouse`), `Spare Part`, `Tools`, `Vehicle`. Spec hanya membaca; tidak membuat atau mengubah data.
- Kemampuan teknis: `Spectra.intercept()` menunda respons list kategori selama 3 detik (TC-FA-CAT-12). Endpoint list kategori tidak tertulis di TC; disediakan tim FE (S-13). Intercept dilepas pada langkah 49 dan dipulihkan di hook `after` bila spec gagal di tengah.
- Flag Guided Tooltip halaman Categories: hook suite `before` men-set true untuk akun aktor dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Seed dan pemulihan client Pre-setup lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/settings-categories.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama data Pre-setup ditulis seperti di TC.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-1: Screening halaman Categories List saat pertama dibuka (All Categories)

1. Verifikasi Breadcrumb `Settings > Categories` tampil tanpa nama produk
2. Verifikasi tidak ada Page Title
3. Verifikasi Category Context Header menampilkan nama konteks `All Categories`
4. Verifikasi Category Context Header menampilkan Total Asset agregat
5. Verifikasi Table Tools di sisi kanan menampilkan Search, Filter, Download, dan Changelog
6. Verifikasi Table Tools tidak memiliki tombol create
7. Verifikasi header kolom berurutan: Checkbox, Category, Code, Total Asset, Modified By, Last Updated, Column Visibility (⋯)
8. Verifikasi kolom Category, Code, Total Asset, Modified By, dan Last Updated sortable
9. Verifikasi kolom Column Visibility (⋯) unsortable
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi overlay Column Visibility terbuka
12. Tutup overlay Column Visibility
13. Klik (⋯) pada baris `Accessory`
14. Verifikasi body kolom Column Visibility (⋯) pada baris `Accessory` membuka row action menu
15. Tutup row action menu
16. Verifikasi baris yang tampil adalah kategori L1 saja: `Accessory`, `Default Category`, `Electronics`, `Furniture`, `Peripheral`, `Spare Part`, `Tools`, `Vehicle`
17. Verifikasi baris berurut Category A-Z
18. Verifikasi pagination default 10 data per halaman
19. Verifikasi Sidebar Category Tree tampil di kanan (Right Panel)
20. Verifikasi root `All Categories` aktif pada Sidebar Category Tree

### TC-FA-CAT-2: Breadcrumb Categories List: teks path dan state tiap segmen

21. Verifikasi Breadcrumb tampil `Settings > Categories` (dua segmen, tanpa nama produk di depannya)
22. Hover lalu klik segmen `Settings`
23. Verifikasi segmen `Settings` berupa label statis
24. Verifikasi klik segmen `Settings` tidak berpindah halaman
25. Hover lalu klik segmen `Categories`
26. Verifikasi segmen `Categories` berupa label statis
27. Verifikasi klik segmen `Categories` tidak berpindah halaman
28. Verifikasi tidak ada segmen yang dapat diklik karena breadcrumb kurang dari tiga segmen

### TC-FA-CAT-3: Halaman Categories List tanpa Page Title terpisah dan tanpa tombol Back to

29. Verifikasi tidak ada elemen Page Title (teks `Categories` sebagai heading) di bawah Breadcrumb
30. Verifikasi tidak ada tombol atau link `← Back to`
31. Verifikasi konten utama (Table SectionCard) langsung dimulai di bawah Breadcrumb

### TC-FA-CAT-4: Screening Sidebar Category Tree (header, rendering node, urutan)

32. Verifikasi panel Right Panel Collapsible tampil selebar `w-64` dengan root virtual `All Categories` berstatus aktif
33. Verifikasi header baris pertama berisi Title `Categories`
34. Verifikasi header baris kedua berisi TreeSearchInput berplaceholder `Search category name or code...` sejajar tombol toggle expand/collapse-all
35. Verifikasi header baris ketiga berisi tombol `[+] Category` rata kanan
36. Verifikasi node `Electronics` menampilkan chevron expand/collapse, nama, dan elipsis (⋯)
37. Verifikasi node `Furniture` menampilkan nama dan elipsis (⋯) selalu tampil
38. Verifikasi tidak ada tombol close (✕) pada panel
39. Verifikasi tidak ada garis pembatas antara header dan pohon

### TC-FA-CAT-25: Alert Category Consolidation Hidden saat jumlah kategori tidak melebihi cap

40. Verifikasi Category Context Header tampil pada client plan Enterprise (Unlimited)
41. Verifikasi Alert Category Consolidation tidak dirender di atas Category Context Header
42. Verifikasi tombol `[Choose Categories]` tidak ada

### TC-FA-CAT-12: Loading state tabel dan sidebar menampilkan shimmer

43. Pasang intercept yang menunda respons list kategori selama 3 detik
44. Buka Fixed Asset > Settings > Categories
45. Verifikasi baris tabel menampilkan Shimmer row
46. Verifikasi node tree sidebar menampilkan Shimmer tree
47. Verifikasi data kategori tampil di tabel menggantikan shimmer setelah respons diterima
48. Verifikasi data kategori tampil di sidebar menggantikan shimmer setelah respons diterima
49. Lepas intercept

## Notes

- Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Mode: FE+BE.
- Langkah penghubung (S-03): langkah 12 dan 15 (menutup overlay Column Visibility dan row action menu), langkah 49 (melepas intercept).
- Penyimpangan urutan (S-10): TC-FA-CAT-12 diletakkan terakhir karena membuka ulang halaman dengan intercept aktif; blok lain memakai halaman yang dibuka hook `beforeEach` suite. Langkah "Buka Fixed Asset > Settings > Categories" pada TC-FA-CAT-1 dipenuhi hook itu (bagian 4); spec tidak mengulang langkah buka.
- Intercept pada TC-FA-CAT-12 hanya menahan respons untuk mengamati state UI (Shimmer); ini bukan kelas b (bagian 3 prinsip 13).
- Expected TC-FA-CAT-25 `Alert tidak dirender` didahului `Verifikasi` Category Context Header tampil sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-CAT-1 butir b.i menyebut "header klik membuka overlay Column Visibility, body per baris = row action menu" tanpa langkah uji. Spec menambah klik header (langkah 10) dan klik (⋯) baris `Accessory` (langkah 13) sebagai langkah pengamatan agar klausa itu punya `Verifikasi` (S-14).
  - TC-FA-CAT-1 butir a.ii menyebut Total Asset agregat tanpa nilai; spec hanya memverifikasi bahwa Total Asset agregat tampil.
  - TC-FA-CAT-12 tidak menyebut endpoint list kategori; kebutuhan intercept ditulis tanpa endpoint (S-13).
- Ukuran spec (49 langkah, melewati sekitar 35): tiap klausa Expected menjadi satu `Verifikasi` (S-01). Seluruh blok satu kelas harness (fungsional, baca saja), satu dataset (CatMain), tanpa aksi tulis, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; spec tidak dipecah (konvensi bagian 3, batas ukuran).
- Spec melewati 35 langkah (49 langkah). Alasan: satu kelas harness dan satu dataset; Expected dipecah per klausa (S-01) dan blok berdiri sendiri; nomor cadangan slice habis sehingga tidak dipecah lebih jauh.
