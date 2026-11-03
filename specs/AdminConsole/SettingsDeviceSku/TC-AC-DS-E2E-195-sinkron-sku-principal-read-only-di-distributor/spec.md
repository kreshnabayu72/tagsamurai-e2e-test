---
id: TC-AC-DS-E2E-195-sinkron-sku-principal-read-only-di-distributor
title: "Sinkron Modul Stok: SKU Principal yang Baru Didaftarkan Terlihat Read-only pada List Distributor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-508
coverage:
  web: automated
---

# Sinkron Modul Stok: SKU Principal yang Baru Didaftarkan Terlihat Read-only pada List Distributor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor ganti akun (langkah 10): Total Control Distributor PT Cakra Distribusi, Local Registration aktif (Dewi Lestari, Modified By `Dewi L`): `totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD` (Pre-setup #10).
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35).
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `SYN-PRI-01` (Data Dinamis #32). Hook `before` menghapus sisa kode itu bila ada; hook `after` menghapusnya.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-508: SKU Principal yang baru didaftarkan terlihat read-only pada List Distributor

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `Asset TAG`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `T-SP1` pada field Model/Type
6. Ketik `SYN-PRI-01` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Klik `[Submit]`
9. Tunggu aksi selesai (popup Register tertutup)
10. Logout lalu login sebagai Total Control Distributor PT Cakra Distribusi (`totalControlDist_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_DIST_PASSWORD`)
11. Buka halaman `Settings > Device > Device SKU`, ketik Search `SYN-PRI-01`, tekan Enter
12. Verifikasi baris `SYN-PRI-01` tampil pada List Distributor sebagai SKU Principal
13. Klik ⋯ pada baris `SYN-PRI-01`
14. Verifikasi menu ⋯ baris `SYN-PRI-01` hanya memuat `Detail`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 10 (ganti akun eksplisit ke Distributor; sesi dikembalikan ke akun default suite di hook `after`), langkah Search `SYN-PRI-01` (menemukan baris target, R-16), dan langkah menunggu aksi selesai sebelum ganti akun (8b butir 8).
- Plan menyebut akun #1 saja untuk slice ini; TC 508 langkah 4 mengganti akun ke Total Control Distributor PT Cakra Distribusi (#10), sehingga akun itu dicantumkan di Prerequisites.
- Temuan untuk QA:
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
