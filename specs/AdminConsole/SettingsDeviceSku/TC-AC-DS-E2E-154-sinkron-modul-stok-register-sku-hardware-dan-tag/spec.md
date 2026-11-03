---
id: TC-AC-DS-E2E-154-sinkron-modul-stok-register-sku-hardware-dan-tag
title: "Sinkron Modul Stok: Register SKU Hardware dan TAG Menjadi Pilihan Add Stock dan Baris Stock List"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-496
  - TC-AC-DS-497
coverage:
  web: automated
---

# Sinkron Modul Stok: Register SKU Hardware dan TAG Menjadi Pilihan Add Stock dan Baris Stock List

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35). Modul stok (#39): Hardware Stock dan TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima tersedia.
- Data Dinamis (kode literal pada Tabel Data Uji Dinamis TC): SKU `SYN-HHR-01` (Data Dinamis #30) dan `SYN-TAG-01` (#31). Hook `before` menghapus sisa kode itu bila ada; hook `after` menghapus keduanya.
- Kemampuan teknis: Add Stock di Hardware Stock dan TAG Stock tersedia untuk membaca pilihan SKU; sesi API aktor tidak dipakai.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-496: Register SKU Handheld Reader menjadi pilihan Add Stock dan baris Stock List Hardware Stock

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category; expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `UHF Handheld Reader`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `H-SY1` pada field Model/Type
6. Ketik `SYN-HHR-01` pada field SKU
7. Pilih Range Type `Long Range`
8. Unggah `foto-a.jpg` pada field Photo
9. Klik `[Submit]`
10. Tunggu aksi selesai (popup Register tertutup)
11. Buka Hardware Stock > Stock List, ketik Search `SYN-HHR-01`, tekan Enter
12. Verifikasi baris `SYN-HHR-01` tampil di Stock List Hardware Stock
13. Verifikasi baris `SYN-HHR-01` menampilkan metrik Total Registered dan In Use bernilai 0
14. Klik Add Stock lalu buka daftar SKU pada pilihan Add Stock
15. Verifikasi SKU `SYN-HHR-01` tersedia sebagai pilihan pada Add Stock
16. Tutup Add Stock lalu buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-497: Register SKU TAG menjadi pilihan Add Stock dan baris Stock List TAG Stock

17. Klik tombol `[+ SKU]` pada toolbar
18. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
19. Klik field Device Name lalu pilih `Asset TAG`
20. Klik field Brand lalu pilih `Arcturus`
21. Ketik `T-SY1` pada field Model/Type
22. Ketik `SYN-TAG-01` pada field SKU
23. Unggah `foto-a.jpg` pada field Photo
24. Klik `[Submit]`
25. Tunggu aksi selesai (popup Register tertutup)
26. Buka TAG Stock > Stock List, ketik Search `SYN-TAG-01`, tekan Enter
27. Verifikasi baris `SYN-TAG-01` tampil di Stock List TAG Stock dengan metrik bernilai 0
28. Klik Add Stock lalu buka daftar SKU pada pilihan Add Stock
29. Verifikasi SKU `SYN-TAG-01` tersedia sebagai pilihan pada Add Stock
30. Tutup Add Stock lalu buka halaman `Settings > Device > Device SKU`

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah menunggu aksi selesai sebelum berpindah surface (8b butir 8), langkah Search di Stock List (menemukan baris target, R-16), dan langkah menutup Add Stock.
- Temuan untuk QA:
  - Post Condition TC 496 dan 497 ("Konsumen SKU ...", "Entri log tercatat di Changelog, System Log aktor, dan Activity Log (rincian isi pada Section 5)") tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01); rincian ada di Section 5 TC.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
