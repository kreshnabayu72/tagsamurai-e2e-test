---
id: TC-FA-CAT-E2E-176-edge-case-total-asset-lifecycle-list-diam-diam-form-edit-dialog-vs-toast-dan-f5-node-terhapus
title: "Edge Case: Total Asset Mengikuti Lifecycle, List Diperbarui Diam-diam, Form Edit Tidak Di-refresh, Dialog Tanpa Toast, dan F5 Saat Node Terhapus"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-511
  - TC-FA-CAT-514
  - TC-FA-CAT-515
  - TC-FA-CAT-518
  - TC-FA-CAT-377
coverage:
  web: automated
---

# Edge Case: Total Asset Mengikuti Lifecycle, List Diperbarui Diam-diam, Form Edit Tidak Di-refresh, Dialog Tanpa Toast, dan F5 Saat Node Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun UI.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Pelaku kedua ("sesi B" pada TC-FA-CAT-514, TC-FA-CAT-515, TC-FA-CAT-377) dan pemicu Dispose (TC-FA-CAT-511): sesi API Total Control (Pre-setup #1) yang hanya memicu perubahan state; hasilnya diasersi di sesi UI A. Mengikuti butir "Sesi API aktor" di `suite.md` (token tidak dihitung sebagai sesi web).
- Data milik spec (di-seed hook `before` lewat API; kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`: aset, Asset Name, lalu kategori), nama berakhiran `{runId}-176`, client CatMain:
  - TC-FA-CAT-511: `Laptop Life {runId}-176` (Code `LL176`, leaf) dengan Asset Name `Laptop Life Item {runId}-176` menunjuknya; tiga aset Active (`Laptop Life Item {runId}-176 - 1` sampai `- 3`) yang terhitung, satu aset Disposed dan satu aset Deleted yang tidak terhitung. N awal Total Asset = 3 dari seeding; setelah Dispose satu aset Active menjadi 2.
  - TC-FA-CAT-514: kategori root `Live Add {runId}-176` dibuat sesi API (tidak di-seed).
  - TC-FA-CAT-515: `Furniture Edit {runId}-176` (Code `FE176`, leaf, Description kosong).
  - TC-FA-CAT-518: `Furniture Use {runId}-176` (Code `FU176`, leaf) dengan Asset Name `Office Chair {runId}-176` menunjuknya (memicu dialog blok D-07).
  - TC-FA-CAT-377: `Vehicle Del {runId}-176` (Code `VD176`, leaf).
  - Pre-setup #20, #21, dan #22 tidak diubah; baris `Default Category` hanya dicentang lalu dilepas (langkah 8 dan 15).
- Jeda nyata 5 detik pada langkah 19 adalah jendela standar asersi absence propagasi SSE (bagian 6), pilihan spec ini (bukan nilai TC atau PRD).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-511: Total Asset hanya aset belum Disposed atau Deleted dan mengikuti transisi lifecycle

1. Catat Total Asset kategori `Laptop Life {runId}-176`
2. Dispose satu aset Active `Laptop Life Item {runId}-176 - 1` lewat modul Disposal dengan sesi API Total Control hingga tersimpan
3. Muat ulang halaman Categories
4. Verifikasi Total Asset kategori `Laptop Life {runId}-176` menjadi nilai yang dicatat dikurangi 1 (2)
5. Buka Popup Detail kategori `Laptop Life {runId}-176`
6. Verifikasi tabel Assets pada Popup Detail memuat 2 aset
7. Tutup Popup Detail

### TC-FA-CAT-514: List diperbarui diam-diam saat sesi lain menambah kategori

8. Centang baris `Default Category`
9. Catat posisi scroll tabel sesi A
10. Buat kategori root `Live Add {runId}-176` dengan sesi API Total Control hingga tersimpan
11. Verifikasi baris `Live Add {runId}-176` muncul di tabel sesi A tanpa muat ulang
12. Verifikasi tidak ada dialog yang tampil
13. Verifikasi posisi scroll tabel sesi A tidak berubah
14. Verifikasi baris `Default Category` tetap tercentang
15. Hapus centang baris `Default Category`

### TC-FA-CAT-515: Form edit yang terbuka tidak di-refresh diam-diam

16. Klik elipsis (⋯) pada baris `Furniture Edit {runId}-176` > `Edit`
17. Ketik Description `Draft A`
18. Ubah Description `Furniture Edit {runId}-176` menjadi `Draft B` dengan sesi API Total Control hingga tersimpan
19. Tunggu 5 detik tanpa memuat ulang halaman
20. Verifikasi input Description pada form sesi A tetap `Draft A`
21. Verifikasi tidak ada dialog interupsi
22. Klik `✕` pada form Edit
23. Verifikasi dialog `Unsaved Changes` tampil
24. Klik `[Leave]`

### TC-FA-CAT-518: Dialog dan toast tidak tampil bersamaan

25. Klik elipsis (⋯) pada baris `Furniture Use {runId}-176` > `Delete`
26. Verifikasi dialog blok D-07 tampil
27. Verifikasi tidak ada toast yang tampil bersama dialog
28. Klik `[OK]`
29. Verifikasi tidak ada toast tambahan sesudah dialog D-07 ditutup

### TC-FA-CAT-377: F5 saat node tersimpan sudah tidak ada

30. Klik node `Vehicle Del {runId}-176` di sidebar
31. Hapus `Vehicle Del {runId}-176` dengan sesi API Total Control hingga tersimpan
32. Tekan F5
33. Verifikasi seleksi sidebar dan Category Context Header kembali ke `All Categories`
34. Verifikasi tidak ada error pada tampilan

## Notes

- Pelaku kedua lewat sesi API bukan konteks kedua (tidak ada `P-2`); TC-FA-CAT-514, TC-FA-CAT-515, dan TC-FA-CAT-377 mengasersi hasil di sesi UI A.
- Langkah penghubung (S-03): langkah 1 (mencatat nilai awal), langkah 3 (muat ulang), langkah 7 (menutup popup), langkah 9 (mencatat posisi scroll), langkah 15 (mereset seleksi, S-09), langkah 19 (jendela 5 detik tanpa `Verifikasi`), langkah 22 sampai 24 (menutup form dirty deterministik, S-08), langkah 28 (menutup dialog).
- Langkah 21 (tanpa dialog interupsi) dan langkah 12 (tanpa dialog) memakai anchor positif langkah sebelumnya: langkah 11 (baris `Live Add {runId}-176` tampil) dan langkah 20 (field tetap tampil `Draft A`) (bagian 8b butir 2).
- Langkah 27 dan 29: dialog D-07 pada langkah 26 menjadi anchor positif; langkah 29 diasersi sesudah `[OK]`.
- Langkah 4 memakai N dari seeding (3); TC menyebut 12 untuk Pre-setup #22 dan spec memakai kategori milik spec.
- Temuan untuk QA:
  - TC-FA-CAT-511 menyebut "Dispose satu aset Active di Laptop lewat modul Disposal" tanpa langkah rinci; spec memakai pemicu lewat sesi API yang disediakan tim FE/BE.
  - TC-FA-CAT-514 tidak menyebut cara mengukur "posisi scroll dan seleksi sesi A"; spec mencatat posisi scroll dan mencentang `Default Category`. Tabel All Categories dengan sedikit baris mungkin tidak memiliki scroll.
  - TC-FA-CAT-515 tidak menyebut tindakan sesi A untuk menutup form di akhir (keadaan dirty dengan `Draft A`); spec menutupnya lewat `✕` dan `[Leave]` (S-09).
  - TC-FA-CAT-515 tidak menyebut nilai Description sesi B; spec memakai `Draft B`.
  - TC-FA-CAT-377, TC-FA-CAT-514, TC-FA-CAT-515 berlabel Manual Only dua sesi paralel; sesi B diganti sesi API karena hanya memicu state.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
