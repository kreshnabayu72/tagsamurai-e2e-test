---
id: TC-FA-NOTIF-E2E-014-android-dot-real-time-dan-guided-tooltip-step-2
title: "Android: Dot Bell Icon Real-Time via SSE dan Guided Tooltip Step 2 Tanpa Notifikasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-7
  - TC-FA-NOTIF-430
coverage:
  mobile: automated
---

# Android: Dot Bell Icon Real-Time via SSE dan Guided Tooltip Step 2 Tanpa Notifikasi

## Prerequisites

- Mode: FE+BE. Platform: aplikasi native Android, Fixed Asset > Dashboard, Notification Center, dan Guided Tooltip `fa-notification`.
- Akun aktor pertama: Total Control client baru Pre-setup #16 (`newClientTotalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFEMPTY_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; flag `guided_tooltip_seen_fa-notification` = true; tanpa notifikasi). Login di aplikasi Android di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. TC-7 memakai akun ini.
- Pemulihan akun #16: TC-7 menambah notifikasi `borrow_waiting_approval` ke akun #16 (keadaan awal tanpa notifikasi). Fixture BE pemulih seed notifikasi mengembalikan #16 ke tanpa notifikasi pada langkah 5 dan di hook `after`, supaya spec yang bergantung pada #16 kosong (spec 004) tidak terpengaruh.
- Akun kedua (ganti akun eksplisit pada langkah 6): Total Control Pre-setup #31 varian tanpa notifikasi (`totalControlTour_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`; nama env usulan, belum terdaftar). TC-430 memakai akun ini. Hook `after` mengembalikan sesi ke akun default suite (Total Control Pre-setup #1).
- Pengecualian atas hook suite untuk flag Guided Tooltip: TC-430 menguji tur pada akun #31 tanpa flag sehingga hook `before` suite tidak menyetelnya true untuk akun #31. Fixture BE penukar varian seed mengosongkan notifikasi akun #31 dan menghapus flag itu pada langkah 6; hook `after` memulihkan keadaan Pre-setup #31 (tanpa flag, seed N-01 sampai N-07).
- Pemicu TC-7: sesi API akun pemicu memicu notifikasi baru `borrow_waiting_approval` untuk akun #16 pada transaksi BRW-2026-0342 (Pre-setup #19) lewat fixture BE pemicu event. Akun pemicu tidak tertulis di Pre-setup TC; disediakan tim FE/BE (lihat Temuan untuk QA). Pelaku kedua memakai sesi API, bukan sesi UI.
- Kemampuan teknis: perangkat atau emulator Android dengan aplikasi native terpasang serta kemampuan mengetuk dan membuka bottom sheet; disediakan tim FE. Spec memakai perangkat bersama sehingga suite berjalan serial (`parallel: false`).
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu notifikasi `borrow_waiting_approval` pada transaksi BRW-2026-0342 (Pre-setup #19) dan memulihkan seed notifikasi akun Pre-setup #16 milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor dan fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-7: Dot Bell icon muncul real-time via SSE saat tidak ada notifikasi Unread

1. Verifikasi Bell icon tampil pada top bar tanpa dot (baseline)
2. Lewat sesi API akun pemicu, picu satu notifikasi baru `borrow_waiting_approval` (transaksi BRW-2026-0342) untuk akun #16 hingga notifikasi tersimpan
3. Verifikasi dot berseverity `danger` muncul pada Bell icon tanpa memuat ulang halaman
4. Verifikasi Dropdown Panel tetap tertutup (dot muncul tanpa membuka dropdown)

### TC-FA-NOTIF-430: Guided tooltip Step 2 menyorot area dot Bell icon walau tidak ada notifikasi Unread

5. Pulihkan akun #16 ke keadaan tanpa notifikasi lewat fixture BE pemulih seed notifikasi
6. Ganti akun: logout dari akun #16, tukar seed akun #31 ke varian tanpa notifikasi dan hapus flag seen lewat fixture BE penukar, login sebagai Total Control Pre-setup #31 dengan `Spectra.env.FA_NOTIFTOUR_TC_PASSWORD`, lalu buka Fixed Asset > Dashboard
7. Ketuk Bell icon, lalu ketuk `[Show All]` untuk membuka Notification Center untuk pertama kali
8. Ketuk `[Next]`
9. Verifikasi spotlight menyorot area Bell icon tempat dot berada
10. Verifikasi dot Bell icon tidak tampil
11. Verifikasi tooltip tampil sebagai bottom sheet mini
12. Ketuk `[Skip]`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Asersi tambahan di luar Expected TC (S-03): langkah 1 (baseline tanpa dot agar kemunculan dot pada langkah 3 bukan dot yang sudah ada).
- Langkah penghubung (S-03): langkah 5 (pemulihan akun #16 sesudah TC-7 menambah notifikasi; spec 004 bergantung pada #16 tanpa notifikasi; S-06, R-08), langkah 6 (ganti akun, tukar seed, hapus flag, buka Fixed Asset > Dashboard; S-07), langkah 7 (TC-430 menulis "Buka Notification Center untuk pertama kali"), langkah 12 (`[Skip]` menutup tur sebelum spec berakhir; flag yang tersimpan dipulihkan hook `after`).
- Langkah 10 (dot tidak tampil) memakai spotlight Step 2 (langkah 9) sebagai anchor positif pada surface yang sama.
- Spec berjalan di aplikasi mobile; `coverage.mobile: automated` tanpa `coverage.web` (bagian 8). Bila tim FE tidak dapat menyediakan perangkat Android, `coverage.mobile` diubah menjadi `unsupported`, bukan spec dihapus. Bagian sesudah ganti akun (TC-430) tetap bermakna walau TC-7 gagal; kelas harness tunggal (fungsional).
- Temuan untuk QA:
  - TC-7 menulis "Dari akun lain, picu satu notifikasi baru" tanpa menyebut akun atau event pemicu; spec memakai event `borrow_waiting_approval` pada BRW-2026-0342 (Data Uji TC-7) dengan akun pemicu yang disediakan tim FE/BE.
  - TC-430 membutuhkan varian akun #31 tanpa notifikasi yang tidak dibedakan di Pre-setup #31 selain catatan "varian seed tanpa notifikasi"; spec menyerahkan penukaran varian ke fixture BE penukar.
