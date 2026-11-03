---
id: TC-AC-DS-E2E-169-resilience-upload-foto-staging-gagal-register-dan-edit
title: "Resilience Upload Foto: Upload ke Staging Gagal pada Register dan Edit Menampilkan Error Inline"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-142
  - TC-AC-DS-229
coverage:
  web: automated
---

# Resilience Upload Foto: Upload ke Staging Gagal pada Register dan Edit Menampilkan Error Inline

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca kecuali disebut lain): pohon Category (#25), Device Name (#26), Brand Principal (#27), SKU inti dan seed (#29, #30), file foto (#37). `foto-rusak.jpg` dipakai bersama intercept untuk simulasi upload gagal (Pre-setup #37).
- Data Dinamis: tidak ada; tidak ada SKU baru yang tersimpan (popup Register ditutup tanpa submit). Target Edit `HHR-ARC-200` tidak diubah (Save tidak diklik).
- Kemampuan teknis: `Spectra.intercept()` di atas backend nyata untuk memaksa respons 500 pada request upload foto; intercept dilepas segera setelah pemicu selesai (S-09).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-142: Upload foto ke staging gagal saat file dipilih menampilkan error inline dan popup tetap terbuka

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category; expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
3. Klik field Brand lalu pilih `Arcturus`
4. Ketik `T-UP1` pada field Model/Type
5. Intercept request upload foto dengan status 500
6. Unggah `foto-rusak.jpg` pada field Photo
7. Verifikasi slot Photo menampilkan error inline "Failed to upload photo. Please try again."
8. Verifikasi popup tetap terbuka
9. Verifikasi field Category, Brand, dan Model/Type tetap terisi
10. Hapus intercept lalu unggah ulang `foto-a.jpg`
11. Verifikasi setelah pilih ulang file foto tampil normal
12. Verifikasi error inline hilang
13. Klik `[✕]` untuk menutup popup
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`

### TC-AC-DS-229: Upload foto ke staging gagal pada Edit menampilkan error inline dan popup tetap terbuka

16. Ketik Search `HHR-ARC-200`, tekan Enter, klik ⋯ pada baris `HHR-ARC-200` lalu pilih `Edit`
17. Intercept request upload foto dengan status 500
18. Unggah `foto-rusak.jpg` pada slot Photo kedua
19. Verifikasi slot Photo menampilkan error inline "Failed to upload photo. Please try again."
20. Verifikasi Popup Edit tetap terbuka dengan field lain dan foto tersimpan dipertahankan
21. Hapus intercept lalu tutup popup dengan `[✕]` dan klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search `HHR-ARC-200` (menemukan baris target, R-16, langkah 16) dan langkah 21 (pelepasan intercept dan penutupan popup).
- TC 142 tidak mengisi Device Name dan SKU sebelum unggah foto; spec mengikuti TC dan menutup form dirty lewat `[✕]`, dialog `Unsaved Changes`, `[Leave]` (S-08).
- Temuan untuk QA:
  - TC 229 menutup Popup Edit tanpa perubahan field selain upload gagal; tidak pasti apakah dialog `Unsaved Changes` muncul (TC tidak menyatakannya), sehingga spec menutup popup tanpa menverifikasi dialog.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
