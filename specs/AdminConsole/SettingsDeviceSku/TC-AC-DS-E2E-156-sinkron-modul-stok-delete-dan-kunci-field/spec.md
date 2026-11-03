---
id: TC-AC-DS-E2E-156-sinkron-modul-stok-delete-dan-kunci-field
title: "Sinkron Modul Stok: Delete dan Bulk Delete Menghilangkan Pilihan Stok serta Add Stock Mengaktifkan Kunci Field SKU"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-501
  - TC-AC-DS-502
  - TC-AC-DS-503
coverage:
  web: automated
---

# Sinkron Modul Stok: Delete dan Bulk Delete Menghilangkan Pilihan Stok serta Add Stock Mengaktifkan Kunci Field SKU

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Konfigurasi General Settings (#35). Modul stok (#39): Hardware Stock dan TAG Stock (Add Stock dan Stock List) pada Principal PT Arunika Prima tersedia.
- Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- State global: tidak ada yang diubah selain data SKU/stok di atas. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari `Fixture.settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Data Dinamis: tidak ada; target aksi hapus `TAG-ARC-OBJ`, `SRT-ANG-01`, `SRT-APL-01` dan target Add Stock `HHR-ARC-200` (stok 0 menjadi 1) adalah data Pre-setup #29 yang dipulihkan fixture BE (stok kembali 0).

## Test Steps

### TC-AC-DS-501: Delete SKU stok 0 menghilangkan pilihan stok dan baris Stock List

1. Ketik Search `TAG-ARC-OBJ`, tekan Enter
2. Klik ⋯ pada baris `TAG-ARC-OBJ` lalu pilih `Delete`
3. Klik `[Delete]`
4. Tunggu aksi selesai (dialog tertutup)
5. Buka TAG Stock > Stock List, ketik Search `TAG-ARC-OBJ`, tekan Enter
6. Verifikasi baris `TAG-ARC-OBJ` tidak ada lagi di Stock List TAG Stock (Search menampilkan "No results found")
7. Klik Add Stock lalu buka daftar SKU
8. Verifikasi sedikitnya satu SKU lain tersedia sebagai pilihan pada Add Stock
9. Verifikasi `TAG-ARC-OBJ` tidak tersedia sebagai pilihan Add Stock
10. Tutup Add Stock; pulihkan `TAG-ARC-OBJ` lewat fixture BE; buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-502: Bulk Delete SKU stok 0 menghilangkan pilihan stok dan baris Stock List tiap SKU

11. Ketik Search `SRT-`, tekan Enter, lalu centang baris `SRT-ANG-01` dan `SRT-APL-01`
12. Pilih Bulk Action > `Delete`
13. Klik `[Delete]`
14. Tunggu aksi selesai (dialog tertutup)
15. Buka TAG Stock > Stock List, ketik Search `SRT-`, tekan Enter
16. Verifikasi baris `SRT-ANG-01` dan `SRT-APL-01` tidak ada lagi di Stock List (Search menampilkan "No results found")
17. Klik Add Stock lalu buka daftar SKU
18. Verifikasi sedikitnya satu SKU lain tersedia sebagai pilihan pada Add Stock
19. Verifikasi `SRT-ANG-01` dan `SRT-APL-01` tidak tersedia sebagai pilihan Add Stock
20. Tutup Add Stock; pulihkan `SRT-ANG-01` dan `SRT-APL-01` lewat fixture BE; buka halaman `Settings > Device > Device SKU`

### TC-AC-DS-503: Add Stock di modul stok mengaktifkan kunci field SKU

21. Buka Hardware Stock lalu tambahkan 1 unit `HHR-ARC-200` lewat Add Stock
22. Kembali ke Settings > Device > Device SKU, ketik Search `HHR-ARC-200`, tekan Enter
23. Verifikasi Current Stock baris `HHR-ARC-200` menjadi 1
24. Klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
25. Verifikasi field SKU, Device Name, dan Range Type terkunci dengan tooltip/inline info
26. Verifikasi Brand, Model/Type, dan Photo tetap dapat diedit
27. Tutup Popup Edit dengan `[✕]`; pulihkan stok `HHR-ARC-200` ke 0 lewat fixture BE

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 10, 20, dan 27 (pemulihan data dan penutupan popup, S-09), langkah Search untuk menemukan baris target (langkah 1, 11, dan 22, R-16, S-14), dan langkah menunggu aksi selesai sebelum berpindah surface (8b butir 8).
- Absence 501 dan 502 memakai empty state "No results found" pada Search sebagai anchor positif (8b butir 2) dan pilihan SKU lain pada Add Stock sebagai anchor opsi.
- Pengecualian S-12 A-11: `TAG-ARC-OBJ`, `SRT-ANG-01`, `SRT-APL-01`, dan `HHR-ARC-200` adalah SKU Pre-setup bernama literal tanpa suffix yang menjadi target aksi tulis; pemulihan ke keadaan awal dijamin fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC (dinyatakan di `suite.md`).
- Temuan untuk QA:
  - TC 503 butir b menyebut Port dapat diedit, tetapi `HHR-ARC-200` adalah Handheld Reader tanpa field Port; spec menjalankan Brand, Model/Type, dan Photo saja.
  - Penambahan stok pada TC 503 lewat Add Stock tidak dapat dibatalkan lewat UI; pemulihan stok 0 lewat fixture BE (disediakan tim FE/BE).
  - S-11/S-13: `Fixture.settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
