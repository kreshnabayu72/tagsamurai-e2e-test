---
id: TC-FA-CAT-E2E-147-setup-column-lisensi-fa-7-dan-dua-kolom-asset-value
title: "Kolom Custom Field Accounting menurut Lisensi FA-7 dan Dua Kolom Asset Value Commercial dan Fiscal"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-687
  - TC-FA-CAT-698
coverage:
  web: automated
---

# Kolom Custom Field Accounting menurut Lisensi FA-7 dan Dua Kolom Asset Value Commercial dan Fiscal

## Prerequisites

- Mode: FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup).
- Akun aktor: Full Sensitive (Pre-setup #50) `fullSensitive_automated_{namaCompany}@qwertysystem.net` (Manage Asset Master Data: R; Group Role View asset value dan Manage purchase pada group `Head Office` dan `Region Jawa`; Global Role Manage accounting; lisensi FA-7 aktif), client CatMain (Pre-setup #20), password `Spectra.env.FA_FS_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_FS_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup CatMain: #20 (pohon kategori; `Laptop` di bawah `Electronics`), #21 (Asset Name `Laptop Dell` dan `Laptop HP` menunjuk `Laptop`), dan #22 (12 aset terhitung pada node `Laptop`: `Laptop Dell - 1` sampai `Laptop Dell - 8` dan `Laptop HP - 1` sampai `Laptop HP - 4`; Brand `Dell` dan `HP`; satu aset ber-Brand `Hewlett Packard Enterprise Indonesia` (36 karakter), Model/Type `Elite Dragonfly G3 Notebook PC` (30 karakter), Group `Region Jawa > Jakarta Selatan Distribution Center`; aset lain ber-Group `Head Office > Floor 1 > Room 301`; `Laptop HP - 4` tanpa Brand, Model/Type, dan Group; sel Status mencakup multi-badge `Borrowed` + `Damaged`). Kebutuhan aset #22 disediakan tim FE.
- Data Pre-setup #55 (CatMain, node `Laptop`, seed API): Asset Value (Commercial) `Laptop Dell - 1` 15000000.00 dan `Laptop HP - 1` 7500000.00.
- Data Pre-setup #56: Accounting `Kode Anggaran` (Text; `Laptop Dell - 1` `ANG-01`); lisensi FA-7 aktif pada keadaan awal.
- Data Pre-setup #59 (CatMain, buku Fiscal): `Asset Value (Fiscal)` `Laptop Dell - 1` 12000000.00 (metode `Straight Line`, masa manfaat 60 bulan) dan `Laptop HP - 1` 5000000.00. Disediakan tim FE.
- Kemampuan teknis: Principal Automation (Pre-setup #11) mengubah lisensi FA-7 client CatMain ke Grace Period dan ke keadaan tidak aktif lewat sesi API (butir hook suite "Sesi API aktor" dan "Seed dan pemulihan"); pemulihan lisensi ke aktif dilakukan di hook `after`. Spectra.intercept dipakai hanya untuk membaca respons data tabel Assets (tanpa mengubah respons); disediakan tim FE.
- Seed client CatMain dan data aset Pre-setup disediakan tim FE/BE (butir hook suite "Seed dan pemulihan lewat API"); spec ini hanya membaca data dan tidak menulisnya.
- State yang diubah spec: konfigurasi Setup Column tersimpan di browser. Kemampuan menghapus preferensi kolom di browser (bukan lewat `[Reset to Default]`) dipakai sebagai langkah penghubung bila TC berikutnya membutuhkan kolom bawaan dan sebagai pemulihan di hook `after`; disediakan tim FE (butir hook suite). Spec ini tidak mengubah data Pre-setup.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Pilih node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`

### TC-FA-CAT-687: Kolom Custom Field Accounting menurut lisensi FA-7

3. Klik header Actions (⋯) > `Setup Column...`, centang `Kode Anggaran`, lalu klik `[Save]`
4. Verifikasi kolom `Kode Anggaran` tersedia dan sel `Laptop Dell - 1` menampilkan `ANG-01` pada lisensi aktif
5. Principal Automation mengubah lisensi FA-7 client ke Grace Period lewat sesi API hingga tersimpan
6. Muat ulang Popup Detail `Laptop` dan buka Setup Column
7. Verifikasi kolom `Kode Anggaran` tetap tersedia di Setup Column pada Grace Period
8. Verifikasi sel `Laptop Dell - 1` menampilkan `ANG-01` secara read-only
9. Principal Automation mengubah lisensi FA-7 ke keadaan tidak aktif lewat sesi API hingga tersimpan
10. Pasang intercept pada respons data tabel Assets
11. Muat ulang Popup Detail `Laptop` dan buka Setup Column
12. Verifikasi kolom `Kode Anggaran` tidak ada di Setup Column
13. Verifikasi kolom `Kode Anggaran` tidak ada di tabel
14. Verifikasi respons data tabel Assets untuk baris `Laptop Dell - 1` tidak memuat nilai `ANG-01`
15. Principal Automation memulihkan lisensi FA-7 ke aktif lewat sesi API hingga tersimpan

### TC-FA-CAT-698: Kolom Asset Value selalu dua kolom tetap

16. Muat ulang Popup Detail `Laptop` dan buka Setup Column
17. Verifikasi daftar Setup Column memuat tepat dua kolom Asset Value, `Asset Value (Commercial)` lalu `Asset Value (Fiscal)` (urutan tetap), pada posisi di antara `Last Scanned` dan `Warranty Expiry`
18. Verifikasi kedua kolom ☐ unchecked tetapi enabled dan tidak tampil di tabel
19. Centang `Asset Value (Commercial)` dan `Asset Value (Fiscal)`, lalu klik `[Save]`
20. Verifikasi tabel memuat dua kolom Asset Value terpisah dengan header `Asset Value (Commercial)` dan `Asset Value (Fiscal)`
21. Verifikasi `Laptop Dell - 1` menampilkan 15000000.00 pada kolom `Commercial` dan 12000000.00 pada kolom `Fiscal` (currency 2 desimal rata kanan)
22. Verifikasi `Laptop HP - 1` menampilkan 7500000.00 pada `Commercial` dan 5000000.00 pada `Fiscal`
23. Hover sel `Asset Value (Fiscal)` pada `Laptop Dell - 1`
24. Verifikasi tooltip menampilkan metode dan masa manfaat (mis. `Straight Line · 60 months`)

## Notes

- Mode: FE+BE. Langkah penghubung (S-03, S-09): langkah 1 dan 2 (membuka Popup Detail), langkah 15 (memulihkan lisensi sebelum TC berikutnya), dan langkah memuat ulang Popup Detail.
- Intercept hanya mengamati respons (tidak memaksa kegagalan); spec tetap FE+BE.
- Temuan untuk QA:
  - TC-FA-CAT-687 Expected d mengasersi respons server pada lisensi tidak aktif; langkah 5 TC (intercept) dipasang sebelum muat ulang agar respons tertangkap.
  - TC-FA-CAT-687 tidak menyebut akun Principal Automation (Pre-setup #11) dan cara mengubah lisensi; ditulis sebagai kemampuan disediakan tim FE/BE (S-13).
  - TC-FA-CAT-698 Expected e menyebut tooltip `Straight Line · 60 months` sebagai contoh (mis.); spec mengasersi isi sebagai metode dan masa manfaat.
