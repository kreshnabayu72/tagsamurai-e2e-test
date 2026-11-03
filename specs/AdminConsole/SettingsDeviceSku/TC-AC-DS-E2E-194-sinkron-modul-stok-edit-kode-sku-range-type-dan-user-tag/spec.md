---
id: TC-AC-DS-E2E-194-sinkron-modul-stok-edit-kode-sku-range-type-dan-user-tag
title: "Sinkron Modul Stok: Edit Kode SKU, Range Type, dan User TAG Tercermin pada Stock List Hardware Stock dan TAG Stock"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-500
coverage:
  web: automated
---

# Sinkron Modul Stok: Edit Kode SKU, Range Type, dan User TAG Tercermin pada Stock List Hardware Stock dan TAG Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35). Modul stok (#39): Hardware Stock dan TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima tersedia.
- Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- State global: tidak ada yang diubah selain data SKU/stok di atas. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada; target Edit adalah `HHR-ARC-200` dan `TAG-ARC-OBJ` (Pre-setup #29, stok 0) dan dipulihkan fixture BE.

## Test Steps

### TC-AC-DS-500: Edit kode SKU, Range Type, dan User TAG tercermin pada Stock List Hardware Stock dan TAG Stock

1. Ketik Search `HHR-ARC-200`, tekan Enter
2. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
3. Ubah SKU menjadi `HHR-ARC-201`
4. Ubah Range Type menjadi `Long Range`
5. Klik `[Save]`
6. Tunggu aksi selesai (popup Edit tertutup)
7. Ganti isi kotak search dengan `TAG-ARC-OBJ`, tekan Enter
8. Klik ⋯ pada baris `TAG-ARC-OBJ` lalu pilih `Edit`
9. Centang `This is User TAG`
10. Klik `[Save]`
11. Tunggu aksi selesai (popup Edit tertutup)
12. Buka Hardware Stock > Stock List, ketik Search `HHR-ARC-201`, tekan Enter
13. Verifikasi Stock List Hardware Stock menampilkan baris `HHR-ARC-201` dengan Range Type `Long Range`
14. Buka TAG Stock > Stock List, ketik Search `TAG-ARC-OBJ`, tekan Enter
15. Verifikasi Stock List TAG Stock menampilkan baris `TAG-ARC-OBJ` dengan kolom Type `User TAG`
16. Pulihkan `HHR-ARC-200` dan `TAG-ARC-OBJ` ke keadaan awal Pre-setup lewat fixture BE

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 16 (pemulihan data, S-09), langkah 1 dan 7 (Search di List Device SKU untuk menemukan baris target; langkah 7 mengganti isi kotak search sesuai 8b butir 9, R-16, S-14), langkah Search di Stock List (menemukan baris target, R-16), dan langkah menunggu aksi selesai sebelum berpindah surface (8b butir 8).
- Pengecualian S-12 A-11: `HHR-ARC-200` dan `TAG-ARC-OBJ` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target Edit; `HHR-ARC-201` adalah nilai hasil rename yang dipulihkan, dan pemulihan ke keadaan awal Pre-setup dijamin fixture BE (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
