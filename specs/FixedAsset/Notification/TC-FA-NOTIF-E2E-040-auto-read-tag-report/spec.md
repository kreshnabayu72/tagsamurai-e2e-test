---
id: TC-FA-NOTIF-E2E-040-auto-read-tag-report
title: "Auto-Read Event Tag: tag_report_created dan tag_report_open_reminder Read saat Laporan Ditutup"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-468
  - TC-FA-NOTIF-469
  - TC-FA-NOTIF-470
  - TC-FA-NOTIF-471
  - TC-FA-NOTIF-478
coverage:
  web: automated
---

# Auto-Read Event Tag: tag_report_created dan tag_report_open_reminder Read saat Laporan Ditutup

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Akun aktor: Manage asset & TAG Update Dewi Anggraini Pre-setup #35 (`manageAssetTagGedungA_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_MATAGA_PASSWORD`, fixture `Fixture.fixedAssetNotification.manageAssetTagGedungA`; nama env usulan, belum terdaftar).
- Login akun aktor pertama (Pre-setup #35) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu penutupan laporan (Replace, Decline Report, Cancel Report) memakai sesi API aktor akun yang sama (Pre-setup #35) lewat fixture BE pemicu event, termasuk scan Tag dan alasan yang diisi fixture. Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: aset Proyektor AST-2024-0150 ber-Tag `RF-00150` Paired dengan laporan terbuka `RF-00150` (Pre-setup #38). Precondition tiap TC (notifikasi `tag_report_created` atau `tag_report_open_reminder` RF-00150 Unread untuk akun aktor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok. Alasan Decline dan Cancel dibaca dari `Fixture.fixedAssetNotification.tagReportReason`.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai laporan Tag RF-00150 (Pre-setup #38, butir (iii)) sebagai pemicu penutupan laporan (Replace, Decline Report, Cancel Report) oleh Fixture BE; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-468: tag_report_created Read saat laporan ditutup oleh Replace

1. Lewat sesi API Dewi Anggraini (Pre-setup #35) Replace TAG pada AST-2024-0150 sehingga laporan RF-00150 berstatus `Replaced` hingga tersimpan
2. Klik Bell icon
3. Verifikasi notifikasi `TAG reported` RF-00150 (AST-2024-0150) berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-469: tag_report_created Read saat laporan ditutup oleh Decline Report

5. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Dewi Anggraini (Pre-setup #35) Decline Report pada RF-00150 (scan Tag dan isi alasan) sehingga laporan berstatus `Declined` hingga tersimpan
6. Klik Bell icon
7. Verifikasi notifikasi `TAG reported` RF-00150 (AST-2024-0150) berstatus Read
8. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-470: tag_report_open_reminder Read saat laporan ditutup oleh Replace

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Dewi Anggraini (Pre-setup #35) Replace TAG pada AST-2024-0150 sehingga laporan RF-00150 berstatus `Replaced` hingga tersimpan
10. Klik Bell icon
11. Verifikasi notifikasi `TAG report is still open` RF-00150 (AST-2024-0150) berstatus Read
12. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-471: tag_report_open_reminder Read saat laporan ditutup oleh Decline Report

13. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Dewi Anggraini (Pre-setup #35) Decline Report pada RF-00150 (scan Tag dan isi alasan) sehingga laporan berstatus `Declined` hingga tersimpan
14. Klik Bell icon
15. Verifikasi notifikasi `TAG report is still open` RF-00150 (AST-2024-0150) berstatus Read
16. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

### TC-FA-NOTIF-478: tag_report_created Read saat laporan ditutup oleh Cancel Report

17. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Dewi Anggraini (Pre-setup #35) Cancel Report pada RF-00150 (pilih Tag dan isi alasan) sehingga laporan berstatus `Canceled` hingga tersimpan
18. Klik Bell icon
19. Verifikasi notifikasi `TAG reported` RF-00150 (AST-2024-0150) berstatus Read
20. Verifikasi tombol `[Detail]` tidak tampil pada notifikasi itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9, 13 dan 17. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Pembagian per TC: TC-FA-NOTIF-468 (langkah 1 sampai 4), TC-FA-NOTIF-469 (langkah 5 sampai 8), TC-FA-NOTIF-470 (langkah 9 sampai 12), TC-FA-NOTIF-471 (langkah 13 sampai 16), TC-FA-NOTIF-478 (langkah 17 sampai 20).
- Urutan TC di spec mengikuti urutan TC sumber (468, 469, 470, 471, 478).
- Temuan untuk QA:
  - TC-FA-NOTIF-468 sampai 471 dan 478 tidak menyebut nilai alasan Decline Report dan Cancel Report ("isi alasan") dan tag yang dipilih pada Cancel Report; spec memakai nilai dari fixture yang ditetapkan tim FE.
  - TC-FA-NOTIF-468 sampai 471 dan 478 menulis "Lakukan: Replace TAG / Decline Report / Cancel Report" sebagai aksi UI; spec menjalankannya lewat sesi API karena hanya memicu keadaan.
