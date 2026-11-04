---
id: TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed
title: "Auto-Read assignment_accepted dan transfer_departed: Handover, Arrival, dan Pembatalan"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-149
  - TC-FA-NOTIF-150
  - TC-FA-NOTIF-151
  - TC-FA-NOTIF-152
coverage:
  web: automated
---

# Auto-Read assignment_accepted dan transfer_departed: Handover, Arrival, dan Pembatalan

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena Group Manager dan Asset Admin memakai akun berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-149, 150 (Group Manager Gedung A) | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | TC-FA-NOTIF-151, 152 (Asset Admin Group Tujuan) | Asset Admin (PIC admin) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Login akun aktor pertama (Pre-setup #3) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu perubahan state (Handover, Cancel, Arrival) memakai sesi API aktor Asset Admin (Pre-setup #8, `Spectra.env.FA_ASSETADMIN_PASSWORD`) lewat fixture BE pemicu event; Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: transaksi Assignment ASG-2026-0120 (Laptop - 1 AST-2024-0067; Pre-setup #20), Transfer TRF-2026-0055 (1 aset; Pre-setup #21; berstatus Overdue pada TC-FA-NOTIF-152). Precondition tiap TC (notifikasi `assignment_accepted` atau `transfer_departed` Unread untuk akun aktor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE penyetel cakupan Group Tujuan untuk akun Asset Admin Pre-setup #8 (TC-FA-NOTIF-151 dan 152).
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (ASG-2026-0120, TRF-2026-0055) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-149: assignment_accepted Read saat Handover selesai

1. Lewat sesi API Asset Admin (Pre-setup #8), selesaikan Handover ASG-2026-0120 hingga tersimpan
2. Klik Bell icon
3. Verifikasi item `Assignment was accepted` ASG-2026-0120 berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-150: assignment_accepted Read saat tiket dibatalkan

5. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Cancel ASG-2026-0120 hingga pembatalan tersimpan
6. Klik Bell icon
7. Verifikasi item `Assignment was accepted` ASG-2026-0120 berstatus Read
8. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-151: transfer_departed Read saat Arrival dikonfirmasi

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Asset Admin Group Tujuan (Pre-setup #8), buka Fixed Asset > Dashboard
10. Lewat sesi API Asset Admin Group Tujuan, konfirmasi Arrival TRF-2026-0055 di tab Incoming hingga tersimpan
11. Klik Bell icon
12. Verifikasi item `Asset incoming transfer ready for arrival` TRF-2026-0055 berstatus Read
13. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-152: transfer_departed Read saat transaksi dibatalkan saat Overdue

14. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin Group Tujuan Cancel TRF-2026-0055 yang berstatus Overdue hingga pembatalan tersimpan
15. Klik Bell icon
16. Verifikasi item `Asset incoming transfer ready for arrival` TRF-2026-0055 berstatus Read
17. Verifikasi tombol `[Detail]` tidak tampil pada item itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9, 10 dan 14. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Pembagian per TC: TC-FA-NOTIF-149 (langkah 1 sampai 4), TC-FA-NOTIF-150 (langkah 5 sampai 8), TC-FA-NOTIF-151 (langkah 9 sampai 13), TC-FA-NOTIF-152 (langkah 14 sampai 17).
- Urutan TC di spec: 149, 150 (Group Manager), lalu 151, 152 (Asset Admin), dikelompokkan per akun.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat `assignment_accepted` dan `transfer_departed` milik Group Manager dan Asset Admin, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-149 dan 150 menulis Group Manager (Gedung A) tanpa nomor Pre-setup; spec memakai Pre-setup #3. TC-FA-NOTIF-151 dan 152 menulis "Asset Admin (group tujuan)" tanpa nomor Pre-setup dan tabel Pre-setup TC tidak memuat Asset Admin di Gedung B; spec memakai Pre-setup #8 (Asset Admin Gedung A) dan fixture BE yang menetapkan cakupan Group Tujuan untuk akun itu (disediakan tim FE/BE).
  - TC-FA-NOTIF-149 sampai 152 tidak menyebut pelaku Handover, Cancel, dan Arrival; spec memakai sesi API Asset Admin. TC-FA-NOTIF-151 menulis "konfirmasi Arrival di tab Incoming" sebagai aksi UI tanpa rincian langkah; spec menjalankannya lewat sesi API karena hanya memicu keadaan.
