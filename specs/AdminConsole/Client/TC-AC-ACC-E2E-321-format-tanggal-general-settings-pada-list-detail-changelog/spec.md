---
id: TC-AC-ACC-E2E-321-format-tanggal-general-settings-pada-list-detail-changelog
title: "Format Tanggal General Settings Diterapkan pada Last Updated List, Date Purchase History License Detail, dan Date Changelog Client"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-447
coverage:
  web: automated
---

# Format Tanggal General Settings Diterapkan pada Last Updated List, Date Purchase History License Detail, dan Date Changelog Client

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- State global: Date Format General Settings diubah dari `dd/MM/yy` (default) ke `M/d/yy` dan dikembalikan ke `dd/MM/yy` di akhir spec dan di hook `after` (jalur ubah: Global Settings > General Settings, kemampuan disediakan tim FE karena TC tidak menyebut jalurnya). Suite berjalan serial. Pre-setup C-01 `PT Sejahtera Abadi` hanya dibaca.
- Tidak butuh intercept, klien HTTP, atau jam server.

## Test Steps

### Format tanggal M/d/yy (TC-AC-ACC-447)

1. Catat format tanggal General Settings saat ini (`dd/MM/yy`), lalu ubah format tanggal di General Settings menjadi `M/d/yy` dan simpan
2. Tunggu aksi selesai (Save General Settings)
3. Buka Admin Console > Client, ketik Search `PT Sejahtera Abadi`, tekan Enter, dan lihat kolom Last Updated
4. Verifikasi bagian tanggal pada Last Updated tampil dengan pola `M/d/yy` (bulan lebih dulu, tanpa nol di depan; contoh 17 Maret 2023 tampil `3/17/23`)
5. Klik Company Name `PT Sejahtera Abadi`, buka Tab Subscription, Purchase History License, dan lihat kolom Date
6. Verifikasi bagian tanggal pada Date Purchase History License tampil dengan pola `M/d/yy`
7. Kembali ke List, klik `[Changelog]` di toolbar, dan lihat kolom Date
8. Verifikasi bagian tanggal pada Date Changelog Client tampil dengan pola `M/d/yy`
9. Tutup modal Changelog, lalu kembalikan format tanggal General Settings ke `dd/MM/yy` dan simpan

## Notes

- Langkah pertama mencatat format semula dan langkah terakhir memulihkannya (Post Condition TC); hook `after` menjadi cadangan (S-09).
- Langkah penghubung (S-03, R-16): Langkah 2 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-447: Langkah 1 tidak menyebut jalur General Settings (menu, tombol Simpan). Expected butir tunggal `bagian tanggal ... M/d/yy` untuk tiga surface; spec memecahnya menjadi tiga `Verifikasi` per surface.
