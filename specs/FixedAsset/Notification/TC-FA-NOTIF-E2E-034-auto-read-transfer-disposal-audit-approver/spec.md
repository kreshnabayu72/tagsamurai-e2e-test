---
id: TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver
title: "Auto-Read Approver Transfer, Disposal, dan Audit: Approve, Reject, Auto-Cancel, dan Pembatalan Requester"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-118
  - TC-FA-NOTIF-119
  - TC-FA-NOTIF-120
  - TC-FA-NOTIF-153
  - TC-FA-NOTIF-154
  - TC-FA-NOTIF-435
  - TC-FA-NOTIF-436
  - TC-FA-NOTIF-440
coverage:
  web: automated
---

# Auto-Read Approver Transfer, Disposal, dan Audit: Approve, Reject, Auto-Cancel, dan Pembatalan Requester

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon, Dropdown Panel, dan halaman Approvals.
- Spec ditulis per blok role karena tiap jenis transaksi memiliki Approver sendiri dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-118, 153, 440, 154, 435 | Approver (Transfer) | #5 | `approverTransfer_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERTRF_PASSWORD` | `Fixture.fixedAssetNotification.approverTransfer` |
  | TC-FA-NOTIF-119, 436 | Approver (Disposal) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |
  | TC-FA-NOTIF-120 | Approver (Audit) | #7 | `approverAudit_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERAUD_PASSWORD` | `Fixture.fixedAssetNotification.approverAudit` |

- Login akun aktor pertama (Pre-setup #5) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin pembuat transaksi (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) pada TC-FA-NOTIF-435 dan 436. Pelaku kedua memakai sesi API, bukan sesi UI.
- Data Pre-setup: transaksi Transfer TRF-2026-0055 (Pre-setup #21), Disposal DSP-2026-0030 (Pre-setup #22), task audit `Task Audit Q3-Gedung A` (Pre-setup #23). Precondition tiap TC (notifikasi `transfer_waiting_approval`, `disposal_waiting_approval`, `audit_waiting_approval`, atau `transfer_almost_timeout` varian Approver Unread) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok. Alasan Reject `Budget belum tersedia` (Data Uji TC-FA-NOTIF-440) dibaca dari `Fixture.fixedAssetNotification.rejectionReason`.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job `F-FATX-07` (auto-cancel) dan pembacaan `cancel_deadline_at` TRF-2026-0055 lewat fixture BE pada TC-FA-NOTIF-154. Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (TRF-2026-0055, DSP-2026-0030, Task Audit Q3-Gedung A) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-118: transfer_waiting_approval menjadi Read saat Approver memutuskan

1. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` TRF-2026-0055
2. Pada halaman Approvals, Approve TRF-2026-0055 sampai sukses
3. Klik Bell icon
4. Verifikasi item `Waiting for your approval` TRF-2026-0055 berstatus Read
5. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-153: almost_timeout varian Approver Read saat Approve disubmit

6. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Please finish this approval — expiring soon` TRF-2026-0055
7. Pada halaman Approvals, Approve TRF-2026-0055 hingga berhasil tersimpan
8. Klik Bell icon
9. Verifikasi item `Please finish this approval — expiring soon` TRF-2026-0055 berstatus Read
10. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-440: almost_timeout varian Approver Read saat Reject disubmit

11. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Please finish this approval — expiring soon` TRF-2026-0055
12. Pada halaman Approvals, Reject TRF-2026-0055 dengan alasan dari `Fixture.fixedAssetNotification.rejectionReason` hingga berhasil tersimpan
13. Klik Bell icon
14. Verifikasi item `Please finish this approval — expiring soon` TRF-2026-0055 berstatus Read
15. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-154: almost_timeout varian Approver Read saat auto-cancel

16. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, baca `cancel_deadline_at` TRF-2026-0055 lewat fixture BE, atur jam server dan jam fixture ke setelah `cancel_deadline_at`, jalankan job `F-FATX-07` hingga auto-cancel TRF-2026-0055 tersimpan, lalu pulihkan jam
17. Klik Bell icon
18. Verifikasi item `Please finish this approval — expiring soon` TRF-2026-0055 berstatus Read
19. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-435: Cancel Transfer oleh requester membuat transfer_waiting_approval Read

20. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin pembuat (Pre-setup #8) Cancel TRF-2026-0055 (`F-XFER-05`) hingga pembatalan tersimpan
21. Klik Bell icon
22. Verifikasi item `Waiting for your approval` TRF-2026-0055 berstatus Read
23. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-119: disposal_waiting_approval menjadi Read saat Approver memutuskan

24. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver (Disposal) (Pre-setup #6), buka Fixed Asset > Dashboard
25. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` DSP-2026-0030
26. Pada halaman Approvals, Approve DSP-2026-0030 sampai sukses
27. Klik Bell icon
28. Verifikasi item `Waiting for your approval` DSP-2026-0030 berstatus Read
29. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-436: Cancel Disposal membuat disposal_waiting_approval Read

30. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin pembuat (Pre-setup #8) Cancel DSP-2026-0030 (`F-DISP-05`) hingga pembatalan tersimpan
31. Klik Bell icon
32. Verifikasi item `Waiting for your approval` DSP-2026-0030 berstatus Read
33. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-120: audit_waiting_approval menjadi Read saat Approver memutuskan

34. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Approver (Audit) (Pre-setup #7), buka Fixed Asset > Dashboard
35. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` Task Audit Q3-Gedung A
36. Pada halaman Approvals, Approve Task Audit Q3-Gedung A sampai sukses
37. Klik Bell icon
38. Verifikasi item `Waiting for your approval` Task Audit Q3-Gedung A berstatus Read
39. Verifikasi tombol `[Detail]` tidak tampil pada item itu

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 6, 11, 16, 20, 24, 25, 30, 34 dan 35. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API (ditulis "... hingga ... tersimpan"); langkah `[Detail]` adalah jalur ke halaman Approvals pada TC yang Langkahnya hanya menulis "Klik Bell icon".
- Pembagian per TC: TC-FA-NOTIF-118 (langkah 1 sampai 5), TC-FA-NOTIF-153 (langkah 6 sampai 10), TC-FA-NOTIF-440 (langkah 11 sampai 15), TC-FA-NOTIF-154 (langkah 16 sampai 19), TC-FA-NOTIF-435 (langkah 20 sampai 23), TC-FA-NOTIF-119 (langkah 24 sampai 29), TC-FA-NOTIF-436 (langkah 30 sampai 33), TC-FA-NOTIF-120 (langkah 34 sampai 39).
- Urutan TC di spec: 118, 153, 440, 154, 435 (akun #5), 119, 436 (akun #6), lalu 120 (akun #7), dikelompokkan per akun Approver supaya ganti akun hanya dua kali.
- Job `F-FATX-07` pada TC-FA-NOTIF-154 hanya pemicu keadaan (auto-cancel), bukan objek uji; batas waktu dibaca dari `cancel_deadline_at` lewat fixture BE (bagian 8b butir 3).
- Spec ini 39 langkah (di atas smell sekitar 35 langkah): kedelapan TC satu topik (Auto-Read notifikasi menunggu persetujuan atau almost_timeout milik Approver), memakai pola Langkah dan seed yang sama, dan tiap blok berdiri sendiri karena seed dipulihkan di antara blok sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat notifikasi milik Approver Transfer, Disposal, dan Audit, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-118, 153, 154, 435, dan 440 menulis Approver (Transfer) tanpa nomor Pre-setup (hanya TC-FA-NOTIF-435 menulis akun Pre-setup #5), TC-FA-NOTIF-119 dan 436 Approver (Disposal) (hanya TC-FA-NOTIF-436 menulis #6), dan TC-FA-NOTIF-120 Approver (Audit) tanpa nomor. Spec memakai Pre-setup #5, #6, dan #7.
  - TC-FA-NOTIF-118, 119, dan 120 hanya menulis "Klik Bell icon" lalu "Approve di halaman Approvals" tanpa jalur ke halaman Approvals; spec memakai `[Detail]` pada item. TC-FA-NOTIF-153 dan 440 menulis "Approve/Reject di halaman Approvals" dari notifikasi almost_timeout tanpa jalur; spec memakai `[Detail]` yang sama.
  - TC-FA-NOTIF-154 tidak menyebut jam yang diatur selain "setelah `cancel_deadline_at` terlampaui"; nilai pastinya ditetapkan tim FE/BE.
