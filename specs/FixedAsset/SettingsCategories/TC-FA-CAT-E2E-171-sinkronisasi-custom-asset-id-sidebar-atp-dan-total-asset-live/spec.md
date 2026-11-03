---
id: TC-FA-CAT-E2E-171-sinkronisasi-custom-asset-id-sidebar-atp-dan-total-asset-live
title: "Sinkronisasi ke Modul Konsumen: Segmen Category Code Custom Asset ID, Sidebar Asset Transactional Policy, dan Total Asset Live"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-486
  - TC-FA-CAT-487
  - TC-FA-CAT-488
coverage:
  web: automated
---

# Sinkronisasi ke Modul Konsumen: Segmen Category Code Custom Asset ID, Sidebar Asset Transactional Policy, dan Total Asset Live

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data milik spec (di-seed hook `before` lewat API; kemampuan seed disediakan tim FE/BE; dibersihkan hook `after`: aset, Asset Name, lalu kategori), nama berakhiran `{runId}-171`, client CatMain:
  - TC-FA-CAT-486: `Furniture Code {runId}-171` (Code `FC171`, leaf). Code diubah menjadi `FC171X`.
  - TC-FA-CAT-487: `Vehicle ATP {runId}-171` (Code `VA171`, leaf). Nama diubah menjadi `Vehicle ATP Renamed {runId}-171`, lalu kategori dihapus.
  - TC-FA-CAT-488: `Laptop Live {runId}-171` (Code `LL171`, leaf) dengan Asset Name `Laptop Dell {runId}-171` menunjuknya dan dua aset Active (`Laptop Dell {runId}-171 - 1` dan `Laptop Dell {runId}-171 - 2`); N awal Total Asset = 2 dari seeding. Aset baru `Laptop Dell {runId}-171 - 3` didaftarkan spec.
  - Pre-setup #20 dan #22 tidak diubah; target tulis memakai data milik spec (S-06).
- Pelaku pendaftaran aset TC-FA-CAT-488: sesi API Total Control (Pre-setup #1) yang hanya memicu penambahan aset di modul Asset Registration; mengikuti butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAT-486: Perubahan Code tercermin pada segmen Category Code Custom Asset ID

1. Klik elipsis (⋯) pada baris `Furniture Code {runId}-171` > `Edit`
2. Ganti isi Code dengan `FC171X`
3. Klik `[Save]`
4. Tunggu aksi selesai (popup Edit tertutup)
5. Buka Fixed Asset > Settings > Custom Asset ID
6. Verifikasi pratinjau segmen [Category Code] untuk kategori `Furniture Code {runId}-171` memakai `FC171X`
7. Verifikasi pratinjau segmen [Category Code] tidak kosong

### TC-FA-CAT-487: Sidebar Category Tree di Asset Transactional Policy mengikuti rename dan Delete

8. Buka Fixed Asset > Settings > Categories
9. Klik elipsis (⋯) pada baris `Vehicle ATP {runId}-171` > `Edit`
10. Ganti isi Category Name dengan `Vehicle ATP Renamed {runId}-171`
11. Klik `[Save]`
12. Tunggu aksi selesai (popup Edit tertutup)
13. Buka Fixed Asset > Settings > Asset Transactional Policy
14. Klik node `Vehicle ATP Renamed {runId}-171` di Sidebar Category Tree
15. Verifikasi Sidebar Category Tree policy menampilkan nama baru `Vehicle ATP Renamed {runId}-171`
16. Buka Fixed Asset > Settings > Categories
17. Klik elipsis (⋯) pada baris `Vehicle ATP Renamed {runId}-171` > `Delete`
18. Klik `[Delete]` pada dialog
19. Tunggu aksi selesai (dialog tertutup)
20. Buka Fixed Asset > Settings > Asset Transactional Policy
21. Muat ulang halaman Asset Transactional Policy
22. Verifikasi Sidebar Category Tree policy tampil dengan node `Default Category`
23. Verifikasi node terpilih `Vehicle ATP Renamed {runId}-171` tidak ditemukan di Sidebar Category Tree policy
24. Verifikasi filter policy kembali ke All Categories

### TC-FA-CAT-488: Total Asset mengikuti jumlah aset live

25. Buka Fixed Asset > Settings > Categories
26. Catat Total Asset kategori `Laptop Live {runId}-171`
27. Daftarkan aset baru `Laptop Dell {runId}-171 - 3` pada Asset Name `Laptop Dell {runId}-171` di modul Asset Registration lewat sesi API Total Control hingga tersimpan
28. Muat ulang halaman Categories
29. Verifikasi Total Asset kategori `Laptop Live {runId}-171` bertambah 1 dari nilai yang dicatat
30. Buka Popup Detail kategori `Laptop Live {runId}-171`
31. Verifikasi tabel Assets pada Popup Detail memuat aset baru `Laptop Dell {runId}-171 - 3`
32. Tutup Popup Detail

## Notes

- TC-FA-CAT-583 dan TC-FA-CAT-490 ada di spec 199.

- Langkah penghubung (S-03): langkah 4, 12 (menunggu aksi selesai sebelum pindah surface), langkah 8, 16, 25 (kembali ke Categories), langkah 14 (memilih node untuk menguji filter policy), langkah 19 (menunggu Delete selesai), langkah 21 (muat ulang, TC menyebut "muat ulang"), langkah 22 (anchor absence sesudah muat ulang: Sidebar Category Tree dan node lain tampil, bagian 8b butir 2), langkah 26 (mencatat nilai awal), langkah 27 (pemicu pelaku lewat sesi API, "hingga tersimpan", R-20), langkah 32 (menutup popup).
- Langkah 15 dan 23 sampai 24 memetakan Expected a dan b TC-FA-CAT-487; hasil Delete (langkah 17 sampai 18) tidak punya Expected toast di TC sehingga tidak diasersi.
- Langkah 6 dan 7 mengasersi segmen [Category Code] untuk kategori milik spec; kode pada TC adalah `FURN2` dan diganti `FC171X` karena Code `FURN` adalah baris Pre-setup (S-06).
- Langkah 27 memakai sesi API karena pendaftaran aset di modul Asset Registration hanya memicu state yang diuji (bukan objek uji spec ini) dan tidak memakai `P-2` (bagian 3 prinsip 13).
- Temuan untuk QA:
  - TC-FA-CAT-486 tidak menyebut layar dan kontrol pratinjau segmen [Category Code] untuk kategori tertentu di Settings > Custom Asset ID; spec mengasersi pratinjau untuk kategori yang diubah.
  - TC-FA-CAT-487 menyebut Delete hasil rename tanpa Expected pada langkah Delete; spec tidak mengasersi toast Delete.
  - TC-FA-CAT-488 menyebut "Registrasikan aset baru ... dari modul Asset Registration" tanpa langkah rinci; spec memakai kemampuan pendaftaran aset lewat sesi API yang disediakan tim FE/BE.
  - TC-FA-CAT-488 menyebut "Total Asset Laptop bertambah 1" pada Pre-setup #22; spec memakai kategori milik spec dengan N awal 2.
  - Nama env var password aktor tidak tertulis di TC; `FA_TC_PASSWORD` adalah usulan.
