---
id: TC-AC-DS-E2E-166-resilience-baca-error-load-list-changelog-dan-usage
title: "Resilience Baca: Error Load List, Changelog, dan Usage by Company dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-32
  - TC-AC-DS-387
  - TC-AC-DS-440
coverage:
  web: automated
---

# Resilience Baca: Error Load List, Changelog, dan Usage by Company dengan Try Again

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

### TC-AC-DS-32: State error load List menampilkan pesan dan tombol Try Again lalu pulih

1. Intercept respons API list dengan status 500 lalu muat ulang halaman `Settings > Device > Device SKU`
2. Verifikasi area tabel menampilkan "Unable to load this data." dan tombol `[Try Again]`
3. Verifikasi area tabel bukan empty state
4. Hapus intercept lalu klik `[Try Again]`
5. Verifikasi setelah `[Try Again]` baris SKU tampil normal

### TC-AC-DS-387: Error load modal Changelog menampilkan pesan dan Try Again

6. Intercept request daftar Changelog dengan status 500
7. Klik ikon Changelog
8. Verifikasi modal "Changelog: Device SKU" menampilkan "Unable to load this data." dan tombol `[Try Again]`
9. Verifikasi modal bukan empty state
10. Hapus intercept lalu klik `[Try Again]`
11. Verifikasi setelah `[Try Again]` entri Changelog tampil normal
12. Tutup modal Changelog

### TC-AC-DS-440: Error load Usage by Company menampilkan pesan dan Try Again

13. Intercept request usage dengan status 500
14. Ketik Search `HHR-ARC-100`, tekan Enter, lalu klik SKU `HHR-ARC-100`
15. Verifikasi tabel Usage menampilkan "Unable to load this data." dan `[Try Again]`
16. Verifikasi tabel Usage bukan empty state
17. Hapus intercept lalu klik `[Try Again]`
18. Verifikasi setelah `[Try Again]` lima baris Usage tampil
19. Tutup Popup Device SKU Detail lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: penutupan modal dan popup, penghapusan Search, dan Search `HHR-ARC-100` pada langkah 14 (menemukan baris target, R-16). Intercept dilepas sebelum `[Try Again]`.
- Kegagalan 5xx dipaksa lewat `Spectra.intercept()` di atas backend nyata (Mode FE+BE, bagian 6); kelas b: satu spec resilience baca per modul.
- Temuan untuk QA:
  - TC 32 langkah 1 menulis "buka halaman" dengan intercept aktif; hook `beforeEach` suite sudah membuka halaman, sehingga spec memuat ulang halaman setelah intercept dipasang.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
