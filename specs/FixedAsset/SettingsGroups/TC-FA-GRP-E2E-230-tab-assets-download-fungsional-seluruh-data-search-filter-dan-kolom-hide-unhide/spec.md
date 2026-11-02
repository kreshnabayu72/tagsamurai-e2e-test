---
id: TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide
title: "Tab Assets Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-722
  - TC-FA-GRP-723
  - TC-FA-GRP-724
  - TC-FA-GRP-725
coverage:
  web: automated
---

# Tab Assets Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup No 1) `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook suite pada `suite.md` berlaku.
- Data Pre-setup (hanya dibaca): Warehouse A (WH-A, Assignable, 24 aset aktif variasi status, ditambah 2 Disposed) pada pohon group Tabel A; page size default 10 sehingga 24 baris tersebar pada 3 halaman. Kolom Tab Assets berada pada konfigurasi default sebagai kondisi awal (Name, Asset ID, TAG, Brand, Model/Type, Status, Last Updated tampil).
- Data pencarian dan filter untuk TC-FA-GRP-723: Search `K` dan Filter Status satu opsi menyisakan sedikitnya satu baris cocok dan sedikitnya satu baris tidak cocok; N, yaitu jumlah baris yang cocok kedua kondisi, diturunkan dari seeding (8b butir 10). Keyword Search memakai `Fixture.settingsGroups.searchKeyword` (disediakan tim FE/BE; TC menulis simbol `K` tanpa nilai konkret, lihat Temuan untuk QA); opsi Status dipilih spec dari fixture Warehouse A.
- Kemampuan teknis (disediakan tim FE): membaca berkas unduhan CSV/XLSX hanya untuk nama berkas, header kolom, dan jumlah baris data. Isi sel diuji di spec lain.
- Setup Column: spec menyembunyikan kolom lewat Column Visibility (langkah 20, 28, 30, dan 32); hook `after` menghapus preferensi kolom Tab Assets di browser (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-722: Download tanpa search/filter, seluruh data

1. Klik angka Total Asset Warehouse A
2. Klik icon Download
3. Pilih Download as CSV
4. Verifikasi tidak ada toast sukses
5. Verifikasi file `Group-Assets.csv` terunduh
6. Verifikasi file berisi seluruh baris data (24 baris dari semua halaman), bukan hanya 10 baris halaman aktif

### TC-FA-GRP-723: Download dengan search dan filter aktif

7. Ketik Search `Fixture.settingsGroups.searchKeyword`, tekan Enter
8. Klik icon Filter
9. Pilih satu opsi Status
10. Klik [Apply]
11. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search dan Filter
12. Klik icon Download
13. Pilih Download as XLSX
14. Verifikasi tanpa toast sukses
15. Verifikasi file `Group-Assets.xlsx` terunduh
16. Verifikasi file hanya berisi baris yang cocok dengan kondisi aktif (N baris data)
17. Klik `(←)` pada kotak Search
18. Hapus pilihan Status pada Filter lalu klik [Apply]

### TC-FA-GRP-724: Kolom yang di-hide tidak ikut ter-export

19. Klik icon (⋯) pada header kolom terakhir
20. Uncheck Asset ID pada overlay Column Visibility
21. Klik icon Download
22. Pilih Download as CSV
23. Verifikasi tidak ada toast/peringatan tambahan
24. Verifikasi file CSV terunduh
25. Verifikasi header file tidak memuat kolom Asset ID
26. Verifikasi header file memuat kolom lain sesuai urutan tampilan (Name, TAG, Brand, Model/Type, Status, Last Updated)

### TC-FA-GRP-725: Kolom yang di-unhide kembali ikut ter-export

27. Klik icon (⋯) pada header kolom terakhir
28. Check Asset ID pada overlay Column Visibility
29. Klik icon (⋯) pada header kolom terakhir
30. Uncheck Asset ID pada overlay Column Visibility
31. Klik icon (⋯) pada header kolom terakhir
32. Check Asset ID pada overlay Column Visibility
33. Klik icon Download
34. Pilih Download as CSV
35. Verifikasi file CSV terunduh
36. Verifikasi header file kembali memuat kolom Asset ID

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 17 dan 18 membersihkan Search dan Filter sebelum TC berikutnya (S-09); langkah 19, 27, 29, dan 31 membuka overlay Column Visibility; langkah 28 mengembalikan Asset ID yang di-hide TC-FA-GRP-724 sebelum Langkah 3 TC-FA-GRP-725 ("Hide kolom Asset ID, lalu tampilkan kembali") dijalankan pada langkah 30 dan 32.
- Asersi absence toast (langkah 4, 14, 23) diletakkan segera sesudah pemicu Download dan sebelum asersi berkas; berkas terunduh (langkah 5, 15, 24) menjadi bukti respons diproses (8b butir 11).
- Alasan di atas 35 langkah (36 langkah): seluruh blok satu kelas (Download Tab Assets fungsional, dataset Warehouse A), tiap blok berdiri sendiri, dan 6 langkah toggle overlay (27 sampai 32) mengikuti TC-FA-GRP-725.
- Isi sel berkas (nilai, tipe badge, tanggal, kosong) dan hierarki Category diuji di spec 231.
- Temuan untuk QA:
  - TC-FA-GRP-723 (dan 702) menulis Search `K` sebagai simbol dan Data Uji "-"; spec memakai `Fixture.settingsGroups.searchKeyword`, bukan huruf `K` literal (S-15).
  - TC-FA-GRP-723 Langkah 3 "Search K dan terapkan filter" tidak menyebut filter yang dipakai; spec memilih satu opsi Status.
  - TC-FA-GRP-724 dan 725 tidak menyebut apakah checkbox Column Visibility pada overlay (⋯) langsung berlaku tanpa `[Save]`; spec mengasumsikan berlaku langsung.
  - TC-FA-GRP-724 dan 725 tidak menyebut apakah overlay (⋯) menutup setelah satu toggle checkbox; spec membuka overlay sebelum tiap toggle.
