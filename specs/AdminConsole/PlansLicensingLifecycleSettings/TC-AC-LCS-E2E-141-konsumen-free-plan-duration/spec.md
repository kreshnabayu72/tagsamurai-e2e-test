---
id: TC-AC-LCS-E2E-141-konsumen-free-plan-duration
title: "Konsumen Free Plan Duration: Perubahan Memengaruhi Subscription Free Baru dan Tidak Mengubah yang Sudah Ada"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-498
coverage:
  web: automated
---

# Konsumen Free Plan Duration: Perubahan Memengaruhi Subscription Free Baru dan Tidak Mengubah yang Sudah Ada

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Client PT Rekan Mandiri (`Fixture.lifecycleSettings.clientRekanMandiri`) memiliki subscription Free yang dibuat sebelum perubahan dengan masa aktif 365 hari; Client PT Sentosa Abadi (`Fixture.lifecycleSettings.clientSentosaAbadi`) belum memiliki subscription Free. Keduanya diseed lewat Fixture BE di hook `before` spec ini.
- Tanggal pembuatan subscription Free baru PT Sentosa Abadi dicatat sesudah subscription dibuat (jam server dan jam browser sinkron).
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menyeed subscription Free dan menghapus subscription Free PT Sentosa Abadi yang dibuat spec.
- Pemulihan: subscription Free PT Sentosa Abadi yang dibuat spec dihapus lewat Fixture BE dan Free Plan Duration dipulihkan ke `365` di hook `after`; ketujuh tab dipulihkan oleh hook `beforeEach` dan `after` suite.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-498: Perubahan Free Plan Duration memengaruhi subscription Free baru dan tidak mengubah subscription Free yang sudah ada

1. Klik tab `Free Plan Settings`
2. Ubah Free Plan Duration dari `365` menjadi `400`
3. Klik `[Save]` dan tunggu toast sukses
4. Buat subscription Free baru untuk Client PT Sentosa Abadi lewat alur Client > Subscription
5. Buka Client > Subscription PT Sentosa Abadi
6. Verifikasi tanggal berakhir subscription Free PT Sentosa Abadi sama dengan tanggal pembuatan ditambah 400 hari
7. Buka Client > Subscription PT Rekan Mandiri
8. Verifikasi tanggal berakhir subscription Free PT Rekan Mandiri tidak berubah (tetap 365 hari sejak pembuatan)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Klik tab" (precondition TC: user berada di tab Free Plan Settings), langkah pembuatan subscription Free baru dan pembukaan halaman Client > Subscription (S-03).
- Temuan untuk QA: TC tidak menyebut langkah rinci alur Client > Subscription untuk membuat subscription Free; spec mengikuti teks TC tanpa menambah langkah (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
