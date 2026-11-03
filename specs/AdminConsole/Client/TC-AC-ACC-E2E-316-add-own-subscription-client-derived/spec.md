---
id: TC-AC-ACC-E2E-316-add-own-subscription-client-derived
title: "Add Own Subscription pada Detail Partner Membuat Satu Client Derived per Partner dengan Default User Bersama"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-443
coverage:
  web: automated
---

# Add Own Subscription pada Detail Partner Membuat Satu Client Derived per Partner dengan Default User Bersama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Fixture milik spec (Fixture BE, disediakan tim FE/BE): Partner `CV Mitra Derived {runId}-316` (Active, langsung di bawah Principal, Group Cabang Bekasi, belum memiliki Client Derived dan belum memiliki Default User bersama), karena Partner Pre-setup `CV Mitra Sejati` sudah memiliki Client Derived C-06 `PT Maju Bersama` dan tidak dapat menghasilkan satu Client Derived baru. Cleanup di hook `after`.
- Data dua subscription Add Own Subscription (Plan, Duration, Start Date): disediakan tim FE karena TC tidak memberi Data Uji. Tidak butuh jam server, intercept, atau klien HTTP.

## Test Steps

### Add Own Subscription dua kali (TC-AC-ACC-443)

1. Buka Admin Console > Partner, ketik Search `CV Mitra Derived {runId}-316`, tekan Enter, lalu klik Company Name Partner `CV Mitra Derived {runId}-316` untuk membuka Detail Partner
2. Klik Add Own Subscription lalu selesaikan subscription pertama dengan data yang disediakan
3. Klik Add Own Subscription lalu selesaikan subscription kedua dengan data yang disediakan (ulangi dengan subscription kedua)
4. Tunggu aksi selesai (Add Own Subscription)
5. Buka Admin Console > Client, klik sub-tab Active, ketik Search `CV Mitra Derived {runId}-316`, tekan Enter
6. Verifikasi tepat satu baris Client `CV Mitra Derived {runId}-316` terbentuk dengan badge `Derived`
7. Klik Company Name `CV Mitra Derived {runId}-316` dan lihat section Default User
8. Verifikasi Default User dipakai bersama (satu Default User untuk Partner dan Client Derived)
9. Buka Tab Subscription
10. Verifikasi subscription kedua masuk Client yang sama: kedua subscription muncul pada Client `CV Mitra Derived {runId}-316`

## Notes

- Penjelasan Fixture: TC-AC-ACC-443 menyebut `Detail Partner CV Mitra Sejati`, tetapi C-06 `PT Maju Bersama` sudah berupa Client Derived dari Partner itu; spec memakai Partner baru bersuffix agar `satu Client Derived terbentuk` dapat diasersi (S-06).
- Langkah penghubung (S-03, R-16): Langkah 4 `Tunggu aksi selesai (...)` menunggu hasil aksi tulis selesai sebelum muat ulang atau pindah halaman; tanpa asersi.
- Temuan untuk QA
  - TC-AC-ACC-443: Precondition `Detail Partner CV Mitra Sejati` bertentangan dengan Tabel A (C-06 sudah Derived dari CV Mitra Sejati sehingga `satu Client Derived terbentuk` tidak dapat diamati). Langkah `Ulangi dengan subscription kedua` tanpa data. Expected `Default User dipakai bersama` tidak punya langkah cek; spec memakai section Default User di Detail Client.
