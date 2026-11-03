---
id: TC-AC-DS-E2E-167-resilience-download-gagal-list-changelog-dan-usage
title: "Resilience Download: Kegagalan Download List, Changelog, dan Usage by Company Menampilkan Toast Error"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-376
  - TC-AC-DS-424
  - TC-AC-DS-465
coverage:
  web: automated
---

# Resilience Download: Kegagalan Download List, Changelog, dan Usage by Company Menampilkan Toast Error

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): SKU inti dan seed (#29, #30), Usage by Company (#32), riwayat Changelog Principal (#33), General Settings (#35).
- Data Dinamis: tidak ada.
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata (bukan `Mode: mock`) untuk memaksa respons 500 atau menunda respons sampai timeout; intercept dilepas segera setelah pemicu selesai (S-09). Plan: backend nyata dipertahankan agar tidak membutuhkan daftar endpoint mock (R-15).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-376: Download gagal menampilkan toast error

1. Intercept request export dengan status 500
2. Klik ikon Download
3. Klik `Download as CSV`
4. Verifikasi muncul toast error: "Error, failed to download Device-SKU."
5. Verifikasi tidak ada file terunduh
6. Hapus intercept request export lalu tutup toast

### TC-AC-DS-424: Download Changelog gagal menampilkan toast error

7. Klik ikon Changelog
8. Intercept request export Changelog dengan status 500
9. Klik ikon Download lalu `Download as CSV`
10. Verifikasi muncul toast error: "Error, failed to download Changelog-Device-SKU."
11. Verifikasi tidak ada file terunduh
12. Verifikasi modal Changelog tetap terbuka
13. Hapus intercept request export Changelog, tutup toast, lalu tutup modal Changelog

### TC-AC-DS-465: Download Usage gagal menampilkan toast error

14. Ketik Search `HHR-ARC-100`, tekan Enter, lalu klik SKU `HHR-ARC-100`
15. Intercept request export usage dengan status 500
16. Klik ikon Download lalu `Download as CSV`
17. Verifikasi muncul toast error: "Error, failed to download SKU-HHR-ARC-100-Usage-by-Company."
18. Verifikasi tidak ada file terunduh
19. Verifikasi popup tetap terbuka
20. Hapus intercept request export usage, tutup toast, tutup Popup Device SKU Detail, lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: pelepasan intercept dan penutupan toast sebelum blok berikutnya (R-12, S-09), penutupan modal dan popup, dan Search `HHR-ARC-100` pada langkah 14 (menemukan baris target, R-16).
- Absence `Tidak ada file terunduh` didahului toast error yang diverifikasi sebagai anchor positif (8b butir 11): respons gagal sudah diproses.
- Temuan untuk QA:
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
