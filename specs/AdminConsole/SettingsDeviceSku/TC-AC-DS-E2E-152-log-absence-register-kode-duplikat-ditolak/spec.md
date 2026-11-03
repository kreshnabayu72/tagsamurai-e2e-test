---
id: TC-AC-DS-E2E-152-log-absence-register-kode-duplikat-ditolak
title: "Absence Log: Register Kode Duplikat yang Ditolak Tidak Menulis Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-553
coverage:
  web: automated
---

# Absence Log: Register Kode Duplikat yang Ditolak Tidak Menulis Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Riwayat Changelog Principal (#33).
- Data Dinamis: tidak ada; SKU `HHR-ARC-200` (Pre-setup #29) sudah ada dan dipakai sebagai kode duplikat, tidak diubah.
- Kemampuan baca (disediakan tim FE/BE): jumlah entri Changelog, System Log aktor, dan Activity Log tab User Action dicatat sebagai baseline sebelum aksi pemicu; audit trail permanen sehingga asersi memakai selisih terhadap baseline (S-12).
- Pemicu: Register dengan kode duplikat (kelas a, bukan objek uji; `P-5` butir a). Tidak ada state global yang diubah; suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-553: Register SKU dengan kode duplikat yang ditolak tidak menulis entri log

1. Klik ikon Changelog
2. Catat jumlah entri Changelog sebagai baseline N_CL, lalu tutup modal
3. Buka Settings > User, pilih user aktor `totalControlSku_automated_{namaCompany}@qwertysystem.net` (nama tampil `Jane Setiawan`), buka Detail lalu tab System Log
4. Catat jumlah entri System Log aktor sebagai baseline N_SL
5. Buka Activity Log lalu tab User Action
6. Catat jumlah entri Activity Log tab User Action sebagai baseline N_AL
7. Buka halaman `Settings > Device > Device SKU`
8. Klik tombol `[+ SKU]` pada toolbar
9. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
10. Klik field Device Name lalu pilih `Asset TAG`
11. Klik field Brand lalu pilih `Arcturus`
12. Ketik `T-DUP3` pada field Model/Type
13. Ketik `HHR-ARC-200` pada field SKU
14. Unggah `foto-a.jpg` pada field Photo
15. Tunggu 1 detik lalu klik `[Submit]`
16. Verifikasi pesan inline "SKU already exists" tampil di bawah field SKU
17. Verifikasi Popup Register SKU tetap terbuka
18. Klik `[Clear Field]` lalu tutup popup dengan `[✕]`
19. Klik ikon Changelog
20. Verifikasi jumlah entri Changelog sama dengan baseline N_CL (tidak bertambah)
21. Verifikasi tidak ada entri Create baru untuk `HHR-ARC-200` pada Changelog
22. Buka Settings > User, pilih user aktor `totalControlSku_automated_{namaCompany}@qwertysystem.net` (nama tampil `Jane Setiawan`), buka Detail lalu tab System Log
23. Verifikasi jumlah entri System Log sama dengan baseline N_SL (tabel termuat)
24. Verifikasi System Log aktor tidak memuat entri Create untuk `HHR-ARC-200`
25. Buka Activity Log lalu tab User Action
26. Verifikasi jumlah entri Activity Log tab User Action sama dengan baseline N_AL (tabel termuat)
27. Verifikasi Activity Log tidak memuat entri Create untuk `HHR-ARC-200`

## Notes

- `P-5`: spec absence (kelas g); pemicunya Register dengan kode duplikat `HHR-ARC-200` (kelas a) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji. Rujukan: spec fungsional Register mencatat TC ini sebagai absence di spec ini (S-05).
- Langkah penghubung tanpa `Verifikasi`: langkah 1 sampai 7 (pencatatan baseline tiga surface log dan membuka kembali Settings > Device > Device SKU, S-12); langkah 18 (`[Clear Field]` lalu `[✕]`, popup bersih sehingga tidak ada dialog Unsaved Changes).
- Expected butir b dipecah: jumlah entri Changelog sama dengan baseline (anchor surface agregat, menggantikan angka absolut 35 pada TC karena S-12) dan tidak ada entri Create baru. Expected butir c dipecah per surface (System Log aktor lalu Activity Log) dengan anchor jumlah entri sama dengan baseline; anchor positif tambahan: pesan penolakan inline sudah diverifikasi sebelum pembacaan log.
- Temuan untuk QA:
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
