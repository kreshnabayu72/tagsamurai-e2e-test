---
id: TC-AC-DS-E2E-155-sinkron-modul-stok-edit-brand-model-photo-dan-device-name
title: "Sinkron Modul Stok: Edit Brand, Model/Type, Photo, dan Device Name Tercermin pada Stock List dan Stock Detail Hardware Stock"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-498
  - TC-AC-DS-499
coverage:
  web: automated
---

# Sinkron Modul Stok: Edit Brand, Model/Type, Photo, dan Device Name Tercermin pada Stock List dan Stock Detail Hardware Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35). Modul stok (#39): Hardware Stock dan TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima tersedia.
- Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- State global: tidak ada yang diubah selain data SKU/stok di atas. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada; target Edit adalah `HHR-ARC-200` (Pre-setup #29, stok 0) dan dipulihkan fixture BE di antara blok TC sehingga tiap blok berdiri sendiri.

## Test Steps

### TC-AC-DS-498: Edit Brand, Model/Type, dan Photo tercermin pada Stock List dan Stock Detail

1. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
2. Ubah Brand menjadi `Veltrix`
3. Ubah Model/Type menjadi `H-SY2`
4. Ganti foto dengan `foto-c.jpeg`
5. Klik `[Save]`
6. Tunggu aksi selesai (popup Edit tertutup)
7. Buka Hardware Stock > Stock List tanpa memuat ulang manual, ketik Search `HHR-ARC-200`, tekan Enter
8. Verifikasi baris `HHR-ARC-200` di Stock List menampilkan Brand `Veltrix`
9. Verifikasi baris `HHR-ARC-200` di Stock List menampilkan Model/Type `H-SY2`
10. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Detail`
11. Verifikasi SKU Info Header Stock Detail menampilkan foto default `foto-c.jpeg`
12. Verifikasi SKU Info Header Stock Detail menampilkan Brand `Veltrix`
13. Verifikasi SKU Info Header Stock Detail menampilkan Model `H-SY2`
14. Pulihkan `HHR-ARC-200` ke keadaan awal Pre-setup lewat fixture BE, lalu buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-499: Edit Device Name pada SKU stok 0 tercermin pada Stock List dan opsi filter Device Name

15. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
16. Ubah Device Name menjadi `UHF Handheld Reader Pro`
17. Klik `[Save]`
18. Tunggu aksi selesai (popup Edit tertutup)
19. Buka Hardware Stock > Stock List, ketik Search `HHR-ARC-200`, tekan Enter
20. Verifikasi baris `HHR-ARC-200` di Stock List menampilkan Device Name `UHF Handheld Reader Pro`
21. Klik ikon Filter lalu klik field Device Name
22. Verifikasi opsi filter Device Name memuat `UHF Handheld Reader Pro`
23. Pilih `UHF Handheld Reader` lalu klik `[Apply]`
24. Verifikasi setelah filter `UHF Handheld Reader` diterapkan baris `HHR-ARC-200` tidak tampil
25. Verifikasi setelah filter `UHF Handheld Reader` diterapkan baris `HHR-ARC-100` tampil
26. Pulihkan `HHR-ARC-200` ke keadaan awal Pre-setup lewat fixture BE; kosongkan filter Stock List; buka halaman `Settings > Device > Device SKU`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 14 dan 26 (pemulihan data dan pembersihan filter agar blok berikutnya tidak bergantung pada state sebelumnya, S-09), langkah Search `HHR-ARC-200` di Stock List (menemukan baris target, R-16), dan langkah menunggu aksi selesai sebelum berpindah surface (8b butir 8).
- Expected 498 butir a dipecah per kolom (Brand, Model/Type) dan butir b per elemen header (foto default, Brand, Model). Expected 499 butir c dipecah menjadi absence `HHR-ARC-200` dan presence `HHR-ARC-100`; anchor absence: baris `HHR-ARC-100` pada hasil filter yang sama.
- Temuan untuk QA:
  - TC 499 langkah 6 sampai 8 membuka Filter Panel Stock List Hardware Stock, bukan List Device SKU; spec mengikuti TC.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
