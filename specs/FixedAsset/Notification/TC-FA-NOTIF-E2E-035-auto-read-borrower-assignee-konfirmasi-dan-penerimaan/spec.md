---
id: TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan
title: "Auto-Read Borrower dan Assignee: Konfirmasi, Accept, Decline, Pembatalan, Kedaluwarsa, dan Tingkat Transaksi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-130
  - TC-FA-NOTIF-131
  - TC-FA-NOTIF-132
  - TC-FA-NOTIF-133
  - TC-FA-NOTIF-134
  - TC-FA-NOTIF-135
  - TC-FA-NOTIF-367
  - TC-FA-NOTIF-368
coverage:
  web: automated
---

# Auto-Read Borrower dan Assignee: Konfirmasi, Accept, Decline, Pembatalan, Kedaluwarsa, dan Tingkat Transaksi

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena TC Borrower dan Assignee memakai akun berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-130, 131 (Borrower) | Borrower Budi Santoso | #11 | `borrowerBudi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_BORROWER_PASSWORD` | `Fixture.fixedAssetNotification.borrowerBudi` |
  | TC-FA-NOTIF-132, 133, 134, 135, 367, 368 (Assignee) | Assignee Siti Rahmawati | #12 | `assigneeSiti_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSIGNEE_PASSWORD` | `Fixture.fixedAssetNotification.assigneeSiti` |

- Login akun aktor pertama (Pre-setup #11) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun pemicu lewat sesi API aktor: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) pada TC-FA-NOTIF-131 dan 134. Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: transaksi Borrow BRW-2026-0342 (Pre-setup #19), transaksi Assignment ASG-2026-0120 (Laptop - 1 AST-2024-0067) dan ASG-2026-0121 (2 aset) (Pre-setup #20). Precondition tiap TC (notifikasi `borrow_confirmation_required` atau `assignment_acceptance_required` Unread untuk akun aktor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job expiry Acceptance 48 jam (TC-FA-NOTIF-135) dan pembacaan waktu terbit ASG-2026-0120 lewat fixture BE. Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah item notifikasi per penerima dan per Title/Body; baseline dan pembacaan sesudah pemicu memakai kemampuan baca yang sama (bagian 8b butir 10).
- Asersi absence jumlah item TC-FA-NOTIF-367 dan 368 memakai jendela "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 34 dan 43) sebelum pembacaan BE; lamanya pilihan spec (bagian 6 konvensi), bukan nilai TC atau PRD.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0342, ASG-2026-0120, ASG-2026-0121) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-130: borrow_confirmation_required Read saat Borrower konfirmasi

1. Konfirmasi BRW-2026-0342 lewat My Asset > Task > Borrow dengan klik `[Confirm]` hingga berhasil tersimpan
2. Klik Bell icon
3. Verifikasi item `Please confirm your borrowed asset` BRW-2026-0342 berstatus Read
4. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-131: borrow_confirmation_required Read saat transaksi dibatalkan

5. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Cancel Request BRW-2026-0342 hingga pembatalan tersimpan
6. Klik Bell icon sebagai Borrower
7. Verifikasi item `Please confirm your borrowed asset` BRW-2026-0342 berstatus Read
8. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-132: assignment_acceptance_required Read saat Accept

9. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Assignee Siti Rahmawati (Pre-setup #12), buka Fixed Asset > Dashboard
10. Klik Bell icon lalu klik `[Detail]` pada item `Please accept your asset assignment` ASG-2026-0120
11. Accept ASG-2026-0120 di halaman acceptance hingga berhasil tersimpan
12. Klik Bell icon sebagai Assignee
13. Verifikasi item `Please accept your asset assignment` ASG-2026-0120 berstatus Read
14. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-133: assignment_acceptance_required Read saat Decline

15. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Please accept your asset assignment` ASG-2026-0120
16. Decline ASG-2026-0120 di halaman acceptance hingga berhasil tersimpan
17. Klik Bell icon sebagai Assignee
18. Verifikasi item `Please accept your asset assignment` ASG-2026-0120 berstatus Read
19. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-134: assignment_acceptance_required Read saat tiket dibatalkan

20. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu lewat sesi API Asset Admin (Pre-setup #8) Cancel ASG-2026-0120 hingga pembatalan tersimpan
21. Klik Bell icon sebagai Assignee
22. Verifikasi item `Please accept your asset assignment` ASG-2026-0120 berstatus Read
23. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-135: assignment_acceptance_required Read saat Acceptance kedaluwarsa

24. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, baca waktu terbit ASG-2026-0120 (T0) lewat fixture BE, atur jam server dan jam fixture ke setelah batas 48 jam sejak T0, jalankan job expiry hingga ASG-2026-0120 kedaluwarsa tersimpan, lalu pulihkan jam
25. Klik Bell icon sebagai Assignee
26. Verifikasi item `Please accept your asset assignment` ASG-2026-0120 berstatus Read
27. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-367: Auto-Read tingkat transaksi: Assignee Accept seluruh aset ASG-2026-0121

28. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Please accept your asset assignment` ASG-2026-0121 milik Assignee (baseline)
29. Klik Bell icon lalu klik `[Detail]` pada item `Please accept your asset assignment` ASG-2026-0121 (2 Assets)
30. Pada halaman acceptance, Accept seluruh aset ASG-2026-0121 hingga berhasil tersimpan
31. Klik Bell icon
32. Verifikasi item `Please accept your asset assignment` ASG-2026-0121 (2 Assets) berstatus Read
33. Verifikasi tombol `[Detail]` tidak tampil pada item itu
34. Tunggu 5 detik tanpa memuat ulang halaman
35. Verifikasi (kemampuan baca BE) jumlah item `Please accept your asset assignment` ASG-2026-0121 milik Assignee sama dengan baseline langkah 28, yaitu satu item (tidak ada keadaan Read parsial per aset)
36. Verifikasi badge Bell icon berkurang tepat 1 dari baseline langkah 28

### TC-FA-NOTIF-368: Auto-Read tingkat transaksi: Assignee Decline seluruh aset ASG-2026-0121

37. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Please accept your asset assignment` ASG-2026-0121 milik Assignee (baseline)
38. Klik Bell icon lalu klik `[Detail]` pada item `Please accept your asset assignment` ASG-2026-0121 (2 Assets)
39. Pada halaman acceptance, Decline seluruh aset ASG-2026-0121 hingga berhasil tersimpan
40. Klik Bell icon
41. Verifikasi item `Please accept your asset assignment` ASG-2026-0121 (2 Assets) berstatus Read
42. Verifikasi tombol `[Detail]` tidak tampil pada item itu
43. Tunggu 5 detik tanpa memuat ulang halaman
44. Verifikasi (kemampuan baca BE) jumlah item `Please accept your asset assignment` ASG-2026-0121 milik Assignee sama dengan baseline langkah 37, yaitu satu item (tidak ada keadaan Read parsial per aset)
45. Verifikasi badge Bell icon berkurang tepat 1 dari baseline langkah 37

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 5, 9, 10, 15, 20, 24, 28, 29, 34, 37, 38 dan 43. Langkah 34 dan 43 adalah jendela tunggu 5 detik tanpa memuat ulang halaman sebelum pembacaan BE (S-03; lamanya pilihan spec, bagian 6 konvensi, bukan nilai TC atau PRD). Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu. Langkah `[Detail]` pada TC-FA-NOTIF-132, 367, dan 368 adalah jalur ke halaman acceptance; baseline badge dicatat sebelum aksi pertama sebagai pembanding "badge berkurang tepat 1".
- Pembagian per TC: TC-FA-NOTIF-130 (langkah 1 sampai 4), TC-FA-NOTIF-131 (langkah 5 sampai 8), TC-FA-NOTIF-132 (langkah 9 sampai 14), TC-FA-NOTIF-133 (langkah 15 sampai 19), TC-FA-NOTIF-134 (langkah 20 sampai 23), TC-FA-NOTIF-135 (langkah 24 sampai 27), TC-FA-NOTIF-367 (langkah 28 sampai 36), TC-FA-NOTIF-368 (langkah 37 sampai 45).
- Job expiry pada TC-FA-NOTIF-135 (langkah 24) hanya pemicu keadaan, bukan objek uji; batas 48 jam dihitung dari T0 yang dibaca lewat fixture BE (bagian 8b butir 3), dengan jam diatur jauh melewati batas.
- Klausa "tidak ada keadaan Read parsial per aset" (Expected b TC-FA-NOTIF-367 dan 368) diasersi sebagai jumlah item untuk ASG-2026-0121 sama dengan baseline (satu item), dibaca sesudah jendela tunggu 5 detik (langkah 34 dan 43), lewat kemampuan baca BE yang sama dengan baseline (bagian 8b butir 10), bukan hitungan item Dropdown Panel; Verifikasi item itu Read mendahuluinya sebagai anchor positif (bagian 8b butir 2).
- Spec ini 45 langkah (di atas smell sekitar 35 langkah): kedelapan TC satu topik (Auto-Read notifikasi Borrower dan Assignee), memakai pola Langkah dan seed yang sama, dan tiap blok berdiri sendiri karena seed dipulihkan di antara blok sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat notifikasi Borrower dan Assignee, karena penerima kelompok lain memakai akun berbeda dan penyatuan melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-130 dan 131 menulis Borrower (Budi Santoso) tanpa nomor Pre-setup, dan TC-FA-NOTIF-132 sampai 135, 367, dan 368 menulis Assignee (Siti Rahmawati) (hanya TC-FA-NOTIF-367 dan 368 menyebut Pre-setup #20 untuk data). Spec memakai Pre-setup #11 dan #12.
  - TC-FA-NOTIF-130 tidak menyebut langkah Confirm secara rinci selain "My Asset > Task > Borrow (`[Confirm]`)"; TC-FA-NOTIF-132 dan 133 tidak menyebut jalur ke halaman acceptance ("Lakukan: Accept di halaman acceptance"); spec memakai `[Detail]` pada item sebagai jalur untuk TC-FA-NOTIF-132 dan 133 (TC-FA-NOTIF-367 dan 368 menyebutnya).
  - TC-FA-NOTIF-131 dan 134 tidak menyebut akun yang membatalkan; spec memakai Asset Admin (Pre-setup #8) mengikuti TC-FA-NOTIF-131 "akun Asset Admin". TC-FA-NOTIF-135 menulis "jalankan job expiry setelah 48 jam" tanpa nama job dan jam pasti; nilai pastinya ditetapkan tim FE/BE.
