---
id: TC-FA-CAT-E2E-083-popup-detail-tautan-name-per-akses-dan-node-dihapus-user-lain
title: "Popup Detail Category: Tautan Kolom Name per Akses Aktor dan Pembukaan Popup untuk Node yang Dihapus User Lain"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-283
  - TC-FA-CAT-284
  - TC-FA-CAT-285
  - TC-FA-CAT-635
coverage:
  web: automated
---

# Popup Detail Category: Tautan Kolom Name per Akses Aktor dan Pembukaan Popup untuk Node yang Dihapus User Lain

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` pada client CatMain (Pre-setup #20), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun lewat langkah Ganti akun pada client CatMain:

| Role yang dipakai | Pre-setup | Email | Password |
|---|---|---|---|
| Capability Read (Global Role Manage Asset Master Data: R saja; tanpa akses baca modul asset) | #3 | `capabilityRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_CAPREAD_PASSWORD` |
| Group Manager Capability CRUD (Group Role Manage Asset & TAG hanya pada group `Head Office`) | #9 | `gmCapability_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GMCAP_PASSWORD` |

  Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup yang hanya dibaca: #20 `Electronics` > `Laptop`; #22 aset `Laptop Dell - 1` dan aset ber-Brand `Hewlett Packard Enterprise Indonesia` dengan Group `Region Jawa > Jakarta Selatan Distribution Center`.
- Data milik spec untuk TC-FA-CAT-635 (di-seed hook `before` lewat API, kemampuan seed disediakan tim FE/BE; dibersihkan hook `after` bila tersisa): `Vehicle {runId}-083` (Code `V83`, leaf), `Heavy Tools {runId}-083` (Code `HT83`, leaf, Total Asset 0), `Accessory {runId}-083` (Code `A83`) berisi `Cable {runId}-083`.
- Pelaku kedua TC-FA-CAT-635: sesi API Total Control (Pre-setup #1) yang hanya memicu penghapusan; mengikuti butir "Sesi API aktor" di `suite.md`.
- Kemampuan teknis: membaca jumlah entri Changelog kategori sebelum dan sesudah aksi (baseline); disediakan tim FE/BE.
- Seed client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD`, `FA_CAPREAD_PASSWORD`, dan `FA_GMCAP_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-283: Kolom Name menjadi tautan Asset Detail bagi aktor dengan akses baca modul asset

1. Klik node `Electronics` di Sidebar Category Tree
2. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
3. Verifikasi nama aset `Laptop Dell - 1` tampil sebagai tautan
4. Klik nama aset `Laptop Dell - 1`
5. Verifikasi Asset Detail aset `Laptop Dell - 1` terbuka pada tab yang sama
6. Buka kembali Fixed Asset > Settings > Categories lewat menu

### TC-FA-CAT-284: Aktor tanpa akses baca asset melihat nama aset sebagai teks biasa tanpa tautan

7. Logout, lalu login sebagai Capability Read (`capabilityRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_CAPREAD_PASSWORD`)
8. Klik node `Electronics` di Sidebar Category Tree
9. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
10. Verifikasi kolom Name menampilkan teks biasa tanpa tautan
11. Klik nama aset `Laptop Dell - 1`
12. Verifikasi klik tidak membuka halaman apa pun
13. Klik icon Close (✕)

### TC-FA-CAT-285: Aktor dengan akses baca asset pada scope Group tertentu, tautan tampil dan penolakan oleh server

14. Logout, lalu login sebagai Group Manager Capability CRUD (`gmCapability_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_GMCAP_PASSWORD`)
15. Klik node `Electronics` di Sidebar Category Tree
16. Klik elipsis (⋯) pada baris `Laptop` > `Detail`
17. Verifikasi tautan Name tampil untuk seluruh baris, termasuk aset ber-Group `Region Jawa > Jakarta Selatan Distribution Center`
18. Klik nama aset ber-Brand `Hewlett Packard Enterprise Indonesia` (Group `Region Jawa > Jakarta Selatan Distribution Center`)
19. Verifikasi toast `You don't have permission to do this.` tampil
20. Verifikasi tidak ada redirect
21. Dismiss toast, lalu klik icon Close (✕)

### TC-FA-CAT-635: Buka Popup Detail untuk node yang sudah dihapus user lain, 404 dengan toast netral T-12

22. Logout, lalu login sebagai Total Control client CatMain (password `Spectra.env.FA_TC_PASSWORD`)
23. Buka Fixed Asset > Settings > Categories sehingga `Vehicle {runId}-083`, `Heavy Tools {runId}-083`, dan `Accessory {runId}-083` termuat
24. Sesi API Total Control menghapus `Vehicle {runId}-083`, `Heavy Tools {runId}-083`, dan `Cable {runId}-083` hingga penghapusan tersimpan
25. Catat baseline jumlah entri Changelog kategori (N1)
26. Klik nama `Vehicle {runId}-083`
27. Verifikasi toast netral `This category is no longer available.`
28. Verifikasi Popup Detail tidak terbuka
29. Dismiss toast
30. Klik angka Total Asset `0` pada baris `Heavy Tools {runId}-083`
31. Verifikasi toast netral `This category is no longer available.`
32. Verifikasi Popup Detail tidak terbuka
33. Dismiss toast
34. Klik node `Accessory {runId}-083` lalu klik elipsis (⋯) pada baris `Cable {runId}-083` > `Detail`
35. Verifikasi toast netral `This category is no longer available.`
36. Verifikasi Popup Detail tidak terbuka
37. Verifikasi tabel dan sidebar di-refresh sehingga node yang dihapus hilang
38. Verifikasi jumlah entri Changelog kategori masih N1 (tidak ada log baru)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah. Alasan: seluruh blok satu kelas (fungsional akses Popup Detail), data milik spec terpisah untuk blok berdua-sesi, dan berdiri sendiri; delapan langkah di antaranya hanya langkah Ganti akun.
- Spec ditulis per blok role karena langkah tiap role berbeda dan Ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (tanpa `Verifikasi`, S-03/S-09): membuka Categories lewat menu setelah Asset Detail, icon Close (✕), dismiss toast (R-12), pencatatan baseline.
- P-1: asersi "tidak ada baris log baru" pada TC-FA-CAT-635 berada di spec ini dengan baseline (S-12) karena konteksnya (halaman dimuat sebelum penghapusan oleh sesi lain) dibangun langkah sebelumnya.
- Temuan untuk QA:
  - TC-FA-CAT-635 mensyaratkan tiga jalur klik berurutan, tetapi Expected b menyatakan tabel dan sidebar di-refresh sehingga node yang dihapus hilang; baris `Heavy Tools {runId}-083` dan `Cable {runId}-083` mungkin sudah hilang setelah jalur pertama. Spec mengikuti urutan TC dan mengasersi refresh sesudah jalur ketiga.
  - TC-FA-CAT-635 menyebut "tidak ada baris log baru" tanpa surface; spec hanya memeriksa Changelog.
  - TC-FA-CAT-635 berlabel Manual Only (dua sesi paralel), tetapi pelaku kedua hanya memicu perubahan state sehingga memakai sesi API.
  - TC-FA-CAT-285 tidak menyebut nama aset ber-Group `Region Jawa > Jakarta Selatan Distribution Center`; spec memakai identitas lewat Brand dari Pre-setup #22.
  - TC-FA-CAT-283 tidak menyebut cara kembali ke Categories sesudah Asset Detail terbuka.
