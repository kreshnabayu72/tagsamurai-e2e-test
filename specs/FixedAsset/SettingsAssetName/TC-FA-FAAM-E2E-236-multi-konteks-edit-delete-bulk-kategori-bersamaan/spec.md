---
id: TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan
title: "Multi-Konteks: Edit-Delete-Bulk Delete Bersamaan dengan Sesi Lain (Record Dihapus, Aset Baru, Kategori Internal)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-637
  - TC-FA-FAAM-638
  - TC-FA-FAAM-639
  - TC-FA-FAAM-640
coverage:
  web: automated
---

# Multi-Konteks: Edit-Delete-Bulk Delete Bersamaan dengan Sesi Lain (Record Dihapus, Aset Baru, Kategori Internal)

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini (sesi A, satu-satunya konteks UI); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Pelaku kedua ("sesi B", Total Control yang sama) bekerja lewat sesi API aktor (suite.md) hanya sebagai pemicu perubahan state; hasilnya diasersi di sesi A. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category `IT Equipment`), No. 22c (kerangka kategori leaf).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-236`, Code literal Tabel Dinamis (batas panjang Code; hook `before` menghapus sisa Code yang sama dari run lama):
  - `Edit Target Item 637 {runId}-236` (Code `ETI637`; Tabel Dinamis No. 53), Total Asset 0.
  - `Warehouse Pallet 638 {runId}-236` (Code `PLT-WH638`; No. 98), Total Asset 0; satu aset didaftarkan oleh pelaku kedua pada langkah 12.
  - `Edit Target Item 639 {runId}-236` (Code `ETI639`; No. 103), Total Asset 0, dan kategori leaf `Temp Leaf 639 {runId}-236` (No. 85; menjadi internal oleh pelaku kedua pada langkah 4).
  - `Bulk Clean A 640 {runId}-236` dan `Bulk Clean B 640 {runId}-236` (No. 69), Total Asset 0; `Bulk Clean B 640 {runId}-236` dihapus oleh pelaku kedua pada langkah 26.
- Kemampuan teknis: sesi API aktor untuk menghapus Asset Name, mendaftarkan aset, dan menambah subcategory hingga tersimpan; Modal Changelog dan Search di dalamnya.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini dan kategori `Temp Leaf 639 {runId}-236` lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-637, 638, 639, 640: login sebagai Total Control dan berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-639: Edit saat kategori menjadi internal di sesi lain

1. Ketik Search `{runId}-236`, tekan Enter
2. Klik `⋯` baris `Edit Target Item 639 {runId}-236` lalu `Edit`
3. Pilih Category leaf `Temp Leaf 639 {runId}-236`
4. Pelaku kedua (sesi API Total Control) menambahkan subcategory ke `Temp Leaf 639 {runId}-236` hingga tersimpan
5. Klik `[Save]`
6. Verifikasi error inline `This category can no longer be selected. Please select another.`
7. Klik `✕` pada Modal Edit
8. Verifikasi dialog `Unsaved Changes`
9. Klik `[Leave]`

### TC-FA-FAAM-638: Delete bersamaan dengan pendaftaran aset baru

10. Klik `⋯` baris `Warehouse Pallet 638 {runId}-236` lalu `Delete`
11. Verifikasi dialog konfirmasi Delete tampil
12. Pelaku kedua (sesi API Total Control) mendaftarkan satu aset ke `Warehouse Pallet 638 {runId}-236` hingga tersimpan
13. Klik `[Delete]` pada dialog
14. Verifikasi dialog blok `Cannot Delete Asset Name` dengan teks `This asset name is used by 1 asset and cannot be deleted.`
15. Tutup dialog blok
16. Verifikasi baris `Warehouse Pallet 638 {runId}-236` masih ada (tanpa mutasi)

### TC-FA-FAAM-637: Edit saat sesi lain menghapus record

17. Klik `⋯` baris `Edit Target Item 637 {runId}-236` lalu `Edit`
18. Pelaku kedua (sesi API Total Control) menghapus `Edit Target Item 637 {runId}-236` hingga tersimpan
19. Klik `[Save]`
20. Verifikasi toast `This asset name is no longer available.`
21. Verifikasi Modal Edit tertutup
22. Verifikasi tabel di-refresh sehingga baris `Edit Target Item 637 {runId}-236` tidak tampil

### TC-FA-FAAM-640: Bulk Delete bersamaan dengan Delete single item yang sama

23. Ketik Search `640 {runId}-236`, tekan Enter
24. Centang `Bulk Clean A 640 {runId}-236` dan `Bulk Clean B 640 {runId}-236`
25. Klik `Bulk Action` lalu `Delete`
26. Pelaku kedua (sesi API Total Control) menghapus `Bulk Clean B 640 {runId}-236` hingga tersimpan
27. Klik `[Delete]`
28. Verifikasi toast `Success, asset name has been deleted.`
29. Ketik Search `640 {runId}-236`, tekan Enter
30. Verifikasi empty state `No results found`, sehingga item yang sudah terhapus dihitung terhapus
31. Klik icon Changelog
32. Ketik Search `640 {runId}-236`, tekan Enter
33. Verifikasi tepat satu baris Delete untuk `Bulk Clean A 640 {runId}-236` dan tepat satu baris Delete untuk `Bulk Clean B 640 {runId}-236` (tidak ada baris ganda)
34. Tutup Modal Changelog

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 1, 23, 29 (Search), langkah 15 (menutup dialog), langkah 7 sampai 9 (menutup form dirty secara deterministik; S-08), langkah 25 (membuka dialog Bulk Delete), langkah 31, 32, 34 (membuka, mencari, dan menutup Modal Changelog; S-12, S-14).
- Pelaku kedua memakai sesi API karena hanya memicu perubahan state; tidak ada konteks UI kedua (bagian 3 butir P-2, keputusan 2026-10-30). Spec tetap kelas c karena objek uji adalah race antar-sesi.
- Urutan TC: TC-FA-FAAM-639, 638, 637, lalu 640 (aksi menghapus data di akhir; S-10).
- Langkah 22 dan 30 adalah asersi absence dengan anchor toast hasil server yang sudah diasersi pada langkah 20 dan 28 (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-637 menulis "Sesi A Save" tanpa perubahan field; spec mengikuti TC (tombol `[Save]` dianggap aktif untuk record yang dibuka).
  - TC-FA-FAAM-638 dan 640 tidak menyebut tombol penutup dialog blok; spec menulis "Tutup dialog blok".
  - TC-FA-FAAM-640 butir b ("item yang sudah terhapus dihitung terhapus") tidak menyebut cara pengamatan selain toast; spec memakai Search List dan Changelog.
