---
id: TC-AC-DS-E2E-171-resilience-bulk-delete-5xx-timeout-dan-kegagalan-parsial
title: "Resilience Bulk Delete: 5xx, Timeout, dan Kegagalan Tak Terduga Mempertahankan Item yang Sudah Terhapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-295
  - TC-AC-DS-296
  - TC-AC-DS-548
coverage:
  web: automated
---

# Resilience Bulk Delete: 5xx, Timeout, dan Kegagalan Tak Terduga Mempertahankan Item yang Sudah Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). Selection Limit (#36, nilai awal 1000) dan General Settings (#35). Target Bulk Delete `SEED-012`, `SEED-013` (blok 295 dan 296, tidak terhapus) dan `SEED-001`, `SEED-002`, `SEED-003` (blok 548; `SEED-001` dan `SEED-002` terhapus dan dipulihkan fixture BE).
- Data Dinamis: tidak ada. Pemulihan Pre-setup yang diubah spec (SKU, stok, nama master) ke keadaan awal dilakukan fixture BE yang disediakan tim FE/BE di hook `before` dan `after` serta sebagai langkah penghubung antar blok TC; entri Changelog, System Log, dan Activity Log yang terbentuk bersifat permanen (lihat Temuan untuk QA).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata (bukan `Mode: mock`) untuk memaksa respons 500 atau menunda respons sampai timeout; intercept dilepas segera setelah pemicu selesai (S-09). Plan: backend nyata dipertahankan agar tidak membutuhkan daftar endpoint mock (R-15).
- Kemampuan teknis (disediakan tim FE/BE): memicu kegagalan server tak terduga pada SKU ketiga saat eksekusi Bulk Delete lewat fixture BE (TC 548); dilepas dan dipulihkan di langkah penghubung dan hook `after`.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-295: Kegagalan server 5xx pada Bulk Delete mempertahankan bar, seleksi, dan dialog

1. Ketik Search `SEED-01`, tekan Enter, lalu centang checkbox baris `SEED-012` dan `SEED-013`
2. Klik `Bulk Action` lalu pilih `Delete`
3. Intercept request delete dengan status 500
4. Klik `[Delete]`
5. Verifikasi muncul toast error: "Error, failed to delete device SKU."
6. Verifikasi dialog konfirmasi tetap terbuka
7. Verifikasi bar bulk dan seleksi dipertahankan
8. Verifikasi tidak ada SKU terhapus
9. Hapus intercept request delete, tutup toast, lalu klik `[Cancel]`

### TC-AC-DS-296: Timeout jaringan pada Bulk Delete mempertahankan bar, seleksi, dan dialog

10. Klik `Bulk Action` lalu pilih `Delete`
11. Tunda respons delete sampai timeout dengan intercept
12. Klik `[Delete]`
13. Verifikasi muncul toast error: "Connection problem. Please try again."
14. Verifikasi dialog tetap terbuka
15. Verifikasi bar bulk dan seleksi dipertahankan
16. Hapus intercept request delete, tutup toast, klik `[Cancel]`, lalu `Unselect All` dan klik `(←)` pada kotak Search

### TC-AC-DS-548: Kegagalan server tak terduga pada Bulk Delete mempertahankan item yang sudah terhapus

17. Ketik Search `SEED-00`, tekan Enter, lalu centang baris `SEED-001`, `SEED-002`, dan `SEED-003`
18. Pilih Bulk Action > `Delete`
19. Picu kegagalan server tak terduga pada SKU ketiga saat eksekusi lewat fixture BE
20. Klik `[Delete]`
21. Verifikasi muncul toast error: "Error, failed to delete device SKU."
22. Verifikasi dialog konfirmasi tetap terbuka dan List di-refresh
23. Verifikasi seleksi hanya memuat SKU yang masih ada (`SEED-003`)
24. Lepas pemicu kegagalan lewat fixture BE, klik `[Cancel]`, lalu klik ikon Changelog
25. Verifikasi Changelog memuat entri Delete `SEED-001` dan `SEED-002`
26. Tutup modal Changelog, klik ikon Search, ketik Search `SEED-00`, tekan Enter
27. Verifikasi `SEED-001` dan `SEED-002` tetap terhapus dari List (anchor: baris `SEED-003` tampil)
28. Verifikasi tidak ada status gagal per item
29. Pulihkan `SEED-001` dan `SEED-002` lewat fixture BE, `Unselect All`, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search untuk menemukan baris target (R-16), penutupan toast dan dialog dengan `[Cancel]`, pelepasan intercept dan pemicu (langkah 9, 16, 24), dan langkah 29 (pemulihan data, S-09).
- TC 548 Expected butir c ("tercatat di log", "tidak ada status gagal per item") tidak punya langkah observasi di TC; spec menambah pembukaan Changelog sebagai observasi untuk "tercatat di log" (dicatat sebagai penghubung, S-03).
- Temuan untuk QA:
  - TC 548 tidak menyebut log mana yang dimaksud "tercatat di log"; spec memakai Changelog. "Tidak ada status gagal per item" tidak punya cara observasi di TC; diasersi sebagai tidak ada status gagal per item pada List/dialog.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
