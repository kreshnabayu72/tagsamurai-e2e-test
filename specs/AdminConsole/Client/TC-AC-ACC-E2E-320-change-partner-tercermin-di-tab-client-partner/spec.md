---
id: TC-AC-ACC-E2E-320-change-partner-tercermin-di-tab-client-partner
title: "Change Partner Tercermin di Tab Client Partner Lama dan Baru"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-446
coverage:
  web: automated
---

# Change Partner Tercermin di Tab Client Partner Lama dan Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE): Client `PT Ganti Mitra Uji {runId}-320` (Active; relasi Partner CV Mitra Sejati saja; Group Area Jakarta; FAMS Active) sebagai kembaran C-13 `PT Ganti Mitra` yang ditandai Pre-setup untuk Change Partner (S-06: target aksi tulis milik spec); cleanup di hook `after`. Partner lama `CV Mitra Sejati` dan Partner baru `CV Mitra Lestari` adalah fixture Pre-setup residen.
- Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Change Partner tercermin pada Tab Client Partner (TC-AC-ACC-446)

1. Ketik Search `PT Ganti Mitra Uji {runId}-320`, tekan Enter, buka `⋯` baris itu → Change Partner, ganti Partner `CV Mitra Sejati` menjadi `CV Mitra Lestari` pada dialog Change Partner, lalu konfirmasi
2. Tunggu aksi selesai
3. Buka Admin Console > Partner, ketik Search `CV Mitra Sejati`, tekan Enter, lalu buka Detail Partner `CV Mitra Sejati` dan Tab Client
4. Verifikasi Tab Client Partner lama menampilkan Client Pre-setup `PT Sejahtera Abadi` (anchor positif)
5. Verifikasi Client `PT Ganti Mitra Uji {runId}-320` hilang dari Tab Client Partner lama
6. Buka Admin Console > Partner, ketik Search `CV Mitra Lestari`, tekan Enter, lalu buka Detail Partner `CV Mitra Lestari` dan Tab Client
7. Verifikasi Client `PT Ganti Mitra Uji {runId}-320` muncul di Tab Client Partner baru

## Notes

- Langkah pertama memakai alur Change Partner sesuai nama aksi di TC; elemen dialog tidak diasersi karena TC-AC-ACC-446 tidak menyebutnya.
- Temuan untuk QA
  - TC-AC-ACC-446: Langkah `Change Partner lalu buka Detail Partner lama dan baru` tidak menyebut Client, Partner lama/baru, dan langkah di dialog Change Partner; Precondition hanya `Data Pre-setup C-01…C-14`. Spec memilih Partner lama `CV Mitra Sejati` dan baru `CV Mitra Lestari` dari Tabel A.
