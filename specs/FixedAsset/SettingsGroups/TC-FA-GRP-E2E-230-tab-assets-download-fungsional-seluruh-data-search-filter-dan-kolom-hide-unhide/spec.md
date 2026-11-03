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
- Setup Column: spec menyembunyikan kolom lewat Column Visibility (langkah 21, 29, 31, dan 33); hook `after` menghapus preferensi kolom Tab Assets di browser (kemampuan disediakan tim FE).
- State global: tidak ada. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-GRP-722: Download tanpa search/filter, seluruh data

1. Ketik Search `Warehouse A`, tekan Enter
2. Klik angka Total Asset Warehouse A
3. Klik icon Download
4. Pilih Download as CSV
5. Verifikasi tidak ada toast sukses
6. Verifikasi file `Group-Assets.csv` terunduh
7. Verifikasi file berisi seluruh baris data (24 baris dari semua halaman), bukan hanya 10 baris halaman aktif

### TC-FA-GRP-723: Download dengan search dan filter aktif

8. Ketik Search `Fixture.settingsGroups.searchKeyword`, tekan Enter
9. Klik icon Filter
10. Pilih satu opsi Status
11. Klik [Apply]
12. Verifikasi tabel menampilkan sedikitnya satu baris hasil Search dan Filter
13. Klik icon Download
14. Pilih Download as XLSX
15. Verifikasi tanpa toast sukses
16. Verifikasi file `Group-Assets.xlsx` terunduh
17. Verifikasi file hanya berisi baris yang cocok dengan kondisi aktif (N baris data)
18. Klik `(←)` pada kotak Search
19. Klik icon Filter, hapus pilihan Status, klik [Apply]

### TC-FA-GRP-724: Kolom yang di-hide tidak ikut ter-export

20. Klik icon (⋯) pada header kolom terakhir
21. Uncheck Asset ID pada overlay Column Visibility
22. Klik icon Download
23. Pilih Download as CSV
24. Verifikasi tidak ada toast/peringatan tambahan
25. Verifikasi file CSV terunduh
26. Verifikasi header file tidak memuat kolom Asset ID
27. Verifikasi header file memuat kolom lain sesuai urutan tampilan (Name, TAG, Brand, Model/Type, Status, Last Updated)

### TC-FA-GRP-725: Kolom yang di-unhide kembali ikut ter-export

28. Klik icon (⋯) pada header kolom terakhir
29. Check Asset ID pada overlay Column Visibility
30. Klik icon (⋯) pada header kolom terakhir
31. Uncheck Asset ID pada overlay Column Visibility
32. Klik icon (⋯) pada header kolom terakhir
33. Check Asset ID pada overlay Column Visibility
34. Klik icon Download
35. Pilih Download as CSV
36. Verifikasi file CSV terunduh
37. Verifikasi header file kembali memuat kolom Asset ID

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 18 dan 19 membersihkan Search dan Filter (Filter Panel sudah menutup sesudah [Apply] langkah 11, jadi langkah 19 membukanya lagi) sebelum TC berikutnya (S-09); langkah 20, 28, 30, dan 32 membuka overlay Column Visibility; langkah 29 mengembalikan Asset ID yang di-hide TC-FA-GRP-724 sebelum Langkah 3 TC-FA-GRP-725 ("Hide kolom Asset ID, lalu tampilkan kembali") dijalankan pada langkah 31 dan 33.
- Asersi absence toast (langkah 5, 15, 24) diletakkan segera sesudah pemicu Download dan sebelum asersi berkas; berkas terunduh (langkah 6, 16, 25) menjadi bukti respons diproses (8b butir 11).
- Alasan di atas 35 langkah (37 langkah): seluruh blok satu kelas (Download Tab Assets fungsional, dataset Warehouse A), tiap blok berdiri sendiri, dan 6 langkah toggle overlay (27 sampai 32) mengikuti TC-FA-GRP-725.
- Isi sel berkas (nilai, tipe badge, tanggal, kosong) dan hierarki Category diuji di spec 231.
- Baris target dicari lewat Search nama (client memiliki lebih dari 10 node level 1 dan page size 10, sehingga posisi baris di halaman 1 tidak diandalkan). Langkah Search adalah langkah penghubung (S-03, R-16).
- Temuan untuk QA:
  - TC-FA-GRP-723 (dan 702) menulis Search `K` sebagai simbol dan Data Uji "-"; spec memakai `Fixture.settingsGroups.searchKeyword`, bukan huruf `K` literal (S-15).
  - TC-FA-GRP-723 Langkah 3 "Search K dan terapkan filter" tidak menyebut filter yang dipakai; spec memilih satu opsi Status.
  - TC-FA-GRP-724 dan 725 tidak menyebut apakah checkbox Column Visibility pada overlay (⋯) langsung berlaku tanpa `[Save]`; spec mengasumsikan berlaku langsung.
  - TC-FA-GRP-724 dan 725 tidak menyebut apakah overlay (⋯) menutup setelah satu toggle checkbox; spec membuka overlay sebelum tiap toggle.
