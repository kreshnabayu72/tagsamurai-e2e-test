---
id: TC-FA-NOTIF-E2E-001-bell-icon-screening-badge-dan-buka-tutup-panel
title: "Bell Icon: Screening, Badge Real-Time, serta Buka dan Tutup Dropdown Panel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-1
  - TC-FA-NOTIF-4
  - TC-FA-NOTIF-8
coverage:
  web: automated
---

# Bell Icon: Screening, Badge Real-Time, serta Buka dan Tutup Dropdown Panel

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (top bar).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed notifikasi N-01 sampai N-07 (Pre-setup #17) milik akun aktor: N-01 sampai N-05 Unread, N-06 dan N-07 Read. Fixture BE pemulih seed dijalankan di hook `before` dan `after` (TC-4 menambah satu notifikasi). Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pemicu TC-4: sesi API akun pemicu memicu notifikasi baru `borrow_waiting_approval` untuk akun aktor pada transaksi BRW-2026-0342 (Pre-setup #19) lewat fixture BE pemicu event. Akun pemicu tidak tertulis di Pre-setup TC; disediakan tim FE/BE (lihat Temuan untuk QA). Pelaku kedua memakai sesi API, bukan sesi UI.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih seed notifikasi.

## Test Steps

### TC-FA-NOTIF-1: Screening Bell icon pada top bar

1. Verifikasi Bell icon `NotificationLine` tampil sejajar avatar profile dengan severity `dark`
2. Verifikasi badge pojok kanan-atas Bell icon berseverity `danger` menampilkan angka `5` (jumlah Unread N-01 sampai N-05; N-06 dan N-07 sudah Read)

### TC-FA-NOTIF-8: Bell icon membuka dan menutup Dropdown Panel

3. Klik Bell icon
4. Verifikasi Dropdown Panel terbuka
5. Klik Bell icon sekali lagi
6. Verifikasi Dropdown Panel tertutup

### TC-FA-NOTIF-4: Badge Bell icon bertambah real-time via SSE tanpa reload

7. Catat nilai badge Bell icon (baseline)
8. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` (transaksi BRW-2026-0342) untuk akun aktor hingga notifikasi tersimpan
9. Verifikasi badge Bell icon menampilkan `6`, bertambah 1 dari baseline langkah 7 (dari `5` menjadi `6`), tanpa memuat ulang halaman
10. Verifikasi Dropdown Panel tetap tertutup (badge berubah tanpa membuka dropdown)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan blok: TC-1 (screening) di awal, TC-8, lalu TC-4 di akhir karena TC-4 mengubah seed notifikasi (S-10). Urutan ini menyimpang dari urutan nomor TC.
- Langkah penghubung (S-03): langkah 7 (baseline badge) dan langkah 8 bersifat pemicu; tidak ada langkah pemulihan eksplisit karena hook `after` memulihkan seed lewat fixture BE pemulih.
- Asersi tambahan di luar Expected TC (S-03): langkah 9 menyebut baseline langkah 7 agar kenaikan teramati terhadap pemicu, bukan terhadap angka tetap `5`.
- Langkah 10 menjalankan klausa "tanpa membuka dropdown" pada Expected TC-4; langkah tidak memuat muat ulang halaman sehingga klausa "tanpa reload" teramati pada langkah 9.
- Temuan untuk QA:
  - TC-4 menulis "Dari akun lain" dan "Approver submit pemicu `borrow_waiting_approval`" tanpa menyebut akun pemicu; "Approver submit" juga ambigu karena event itu dipicu saat Borrower mengirim transaksi Borrow. Spec memakai akun pemicu yang disediakan tim FE/BE.
