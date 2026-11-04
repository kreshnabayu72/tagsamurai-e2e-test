---
id: TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi
title: "Dua Event Bersamaan, Resubmit setelah Reject, dan Idempotensi Pembuatan Notifikasi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-169
  - TC-FA-NOTIF-170
  - TC-FA-NOTIF-171
  - TC-FA-NOTIF-359
  - TC-FA-NOTIF-362
coverage:
  web: automated
---

# Dua Event Bersamaan, Resubmit setelah Reject, dan Idempotensi Pembuatan Notifikasi

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon dan Dropdown Panel.
- Spec ditulis per blok role karena tiap TC memakai akun berbeda dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-30). Akun yang diuji:

  | Blok | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|---|
  | TC-FA-NOTIF-169, 170, 362 (Approver) | Approver (Borrowing & Assignment) | #4 | `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERBA_PASSWORD` | `Fixture.fixedAssetNotification.approverBorrowingAssignment` |
  | TC-FA-NOTIF-171 (Asset Admin yang juga Borrower dan PIC admin BRW-2026-0342) | Asset Admin (PIC admin) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | TC-FA-NOTIF-359 (Total Control yang juga Approver) | Total Control Citra Lestari (juga Approver Borrowing & Assignment) | #14 | `targetCitra_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TARGETCITRA_PASSWORD` | `Fixture.fixedAssetNotification.targetCitra` |

- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku yang hanya memicu event (Submit Borrow Request, resubmit, Remove Total Control, retry Create Notification) memakai sesi API aktor lewat fixture BE pemicu event, yaitu Asset Admin pembuat (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) dan akun pemicu Remove Total Control yang disediakan tim FE/BE. Pelaku yang hanya memicu perubahan state di modul sumber memakai sesi API aktor (butir "Sesi API aktor" di `suite.md`), bukan sesi UI.
- Data Pre-setup: transaksi Borrow BRW-2026-0341 (2 aset) dan BRW-2026-0342 (1 aset) (Pre-setup #19 dan #24); varian seed badge awal `3` (Pre-setup #18) untuk TC-FA-NOTIF-171. Fixture BE menyiapkan keadaan awal per TC: kedua transaksi siap di-submit tanpa notifikasi sebelumnya (TC-FA-NOTIF-169), BRW-2026-0342 pernah Rejected dengan notifikasi lama Read (TC-FA-NOTIF-170), dan notifikasi `borrow_waiting_approval` BRW-2026-0342 sudah dibuat satu kali (TC-FA-NOTIF-362). Asersi jumlah notifikasi memakai baseline per penerima yang dicatat tepat sebelum pemicu (bagian 8b butir 10).
- Kemampuan menjalankan job latar dan menggeser jam (butir "Kemampuan menjalankan job latar" di `suite.md`): job overdue harian (TC-FA-NOTIF-171). Jam server dan jam fixture diatur bersama; sesi UI dan sesi API aktor tetap valid selama jam digeser; jam dipulihkan pada langkah yang menjalankan job dan di hook `after` (S-09). Job hanya memicu keadaan, bukan objek uji.
- Kemampuan baca BE (disediakan tim FE/BE, tanpa endpoint karangan): membaca jumlah item notifikasi per penerima dan per Title/aset; baseline dan pembacaan sesudah pemicu TC-FA-NOTIF-362 dan TC-FA-NOTIF-171 memakai kemampuan baca yang sama, bukan hitungan item Dropdown Panel (bagian 8b butir 10).
- Asersi absence TC-FA-NOTIF-362 memakai jendela "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 14) yang merupakan pilihan spec (bagian 6 konvensi), bukan nilai TC atau PRD.
- Pemulihan Pre-setup #14: akses Total Control Citra Lestari dicabut pada TC-FA-NOTIF-359 (langkah 24) dan dipulihkan fixture BE pemulih pada langkah 29 dan di hook `after`.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A, butir (ii) untuk transaksi Pre-setup bersama dan butir (iii) untuk akses Total Control akun #14): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0341, BRW-2026-0342) sebagai pemicu atau target aksi, dan mencabut serta memulihkan akses Total Control akun Pre-setup #14 (TC-FA-NOTIF-359); pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-169: Dua event berbeda ke pengguna yang sama tetap dua notifikasi terpisah

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu atur BRW-2026-0341 dan BRW-2026-0342 siap di-submit tanpa notifikasi sebelumnya lewat fixture BE penyetel state sumber, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon (baseline)
2. Lewat sesi API Asset Admin (Pre-setup #8), submit Borrow Request BRW-2026-0341 dan BRW-2026-0342 hampir bersamaan hingga kedua notifikasi tersimpan
3. Klik Bell icon
4. Verifikasi item `Waiting for your approval` dengan Body `BRW-2026-0341 (2 Assets)` tampil
5. Verifikasi item `Waiting for your approval` dengan Body `BRW-2026-0342 (1 Asset)` tampil sebagai notifikasi terpisah
6. Verifikasi badge Bell icon bertambah 2 dari baseline langkah 1

### TC-FA-NOTIF-170: Resubmit setelah Reject menghasilkan notifikasi waiting_approval baru

7. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu atur BRW-2026-0342 pernah Rejected dengan notifikasi lama `Waiting for your approval` berstatus Read lewat fixture BE penyetel state sumber, muat ulang halaman Fixed Asset > Dashboard
8. Lewat sesi API Asset Admin pembuat (Pre-setup #8), resubmit BRW-2026-0342 yang pernah Rejected hingga notifikasi baru tersimpan
9. Klik Bell icon
10. Verifikasi notifikasi baru `Waiting for your approval` BRW-2026-0342 tampil di posisi teratas dan berstatus Unread
11. Verifikasi notifikasi lama `Waiting for your approval` BRW-2026-0342 tetap Read

### TC-FA-NOTIF-362: Pemanggilan ulang pembuatan notifikasi dengan identitas event sama diabaikan

12. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu atur BRW-2026-0342 dengan notifikasi `borrow_waiting_approval` sudah dibuat satu kali lewat fixture BE penyetel state sumber, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon dan, lewat fixture BE, jumlah item `Waiting for your approval` BRW-2026-0342 milik Approver (baseline)
13. Ulangi pemanggilan Create Notification untuk submission BRW-2026-0342 yang sama dengan identitas event yang sama (retry modul sumber lewat fixture BE) hingga pemanggilan selesai
14. Tunggu 5 detik tanpa memuat ulang halaman
15. Klik Bell icon
16. Verifikasi (kemampuan baca BE) jumlah item `Waiting for your approval` BRW-2026-0342 milik Approver sama dengan baseline langkah 12, yaitu satu item
17. Verifikasi badge Bell icon tidak bertambah dari baseline langkah 12

### TC-FA-NOTIF-171: Dedup: tampil satu item tanpa duplikat tersembunyi dan badge naik tepat 1

18. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih (varian seed badge awal `3`), logout, login sebagai Asset Admin yang juga Borrower dan PIC admin BRW-2026-0342 (Pre-setup #8), buka Fixed Asset > Dashboard, lalu catat nilai badge Bell icon (baseline badge)
19. Catat, lewat fixture BE, jumlah item `Your borrowed asset is overdue` BRW-2026-0342 milik Asset Admin (baseline jumlah item)
20. Atur jam server dan jam fixture ke setelah Due Date BRW-2026-0342, jalankan job overdue harian (event `borrow_overdue` dua peran) hingga notifikasi tersimpan, lalu pulihkan jam
21. Verifikasi badge Bell icon `4` (naik tepat 1 dari baseline badge langkah 18)
22. Verifikasi (kemampuan baca BE) jumlah item `Your borrowed asset is overdue` BRW-2026-0342 milik Asset Admin naik tepat 1 dari baseline langkah 19

### TC-FA-NOTIF-359: Dua event hampir bersamaan ke pengguna sama menghasilkan dua notifikasi terpisah

23. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, logout, login sebagai Total Control Citra Lestari yang juga Approver Borrowing & Assignment (Pre-setup #14), buka Fixed Asset > Dashboard, lalu catat nilai badge Bell icon (baseline)
24. Lewat sesi API aktor pemicu, picu Remove Total Control Citra Lestari dan Submit Borrow Request BRW-2026-0342 (aset di Gedung A, approval ON) hampir bersamaan hingga kedua notifikasi tersimpan
25. Klik Bell icon
26. Verifikasi item `Your Total Control access was removed` tampil
27. Verifikasi item `Waiting for your approval` BRW-2026-0342 tampil sebagai notifikasi terpisah
28. Verifikasi badge Bell icon bertambah 2 dari baseline langkah 23
29. Pulihkan akses Total Control Citra Lestari (Pre-setup #14) lewat fixture BE pemulih seed notifikasi dan transaksi hingga tersimpan

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 2, 7, 8, 12, 13, 14, 18, 19, 20, 23, 24 dan 29. Langkah pembuka blok memuat pemulihan fixture BE, muat ulang halaman atau ganti akun, dan pemicu keadaan lewat sesi API aktor (ditulis "... hingga ... tersimpan"); tidak ada Verifikasi pada langkah-langkah itu.
- Asersi tambahan di luar Expected TC (S-03): langkah 6 dan 10. Langkah 6 (selisih badge +2 pada TC-FA-NOTIF-169) adalah bukti jumlah "dua notifikasi" karena TC hanya menulis dua notifikasi terpisah (bagian 8b butir 10); langkah 10 (posisi teratas pada TC-FA-NOTIF-170) membedakan notifikasi baru dari notifikasi lama berjudul sama.
- Langkah 14 (jendela 5 detik tanpa memuat ulang halaman, bagian 6 konvensi) mendahului asersi tidak-bertambah TC-FA-NOTIF-362 (langkah 15 sampai 17); lamanya adalah pilihan spec, bukan nilai TC atau PRD.
- Job overdue harian (langkah 20) hanya pemicu keadaan, bukan objek uji; asersi TC-FA-NOTIF-171 (langkah 21 dan 22) memakai baseline badge dan baseline jumlah item dari kemampuan baca BE (bagian 8b butir 10).
- Pemulihan (S-11, R-08): TC-FA-NOTIF-359 mencabut Total Control Citra Lestari (Pre-setup #14); langkah 29 memulihkan akses itu lewat fixture BE pemulih dan hook `after` mengulanginya.
- Langkah 12 mencatat baseline jumlah item `Waiting for your approval` BRW-2026-0342 dan badge sebelum pemanggilan ulang, agar "hanya satu item" dan "badge tidak bertambah" (Expected TC-FA-NOTIF-362, langkah 16 dan 17) punya pembanding. Selisih badge +2 pada langkah 28 adalah Expected TC-FA-NOTIF-359.
- Pembagian per TC: TC-FA-NOTIF-169 (langkah 1 sampai 6), TC-FA-NOTIF-170 (langkah 7 sampai 11), TC-FA-NOTIF-362 (langkah 12 sampai 17), TC-FA-NOTIF-171 (langkah 18 sampai 22), TC-FA-NOTIF-359 (langkah 23 sampai 29).
- Urutan TC di spec: 169, 170, 362 (Approver), 171 (Asset Admin), lalu 359 (Total Control), dikelompokkan per akun supaya ganti akun hanya dua kali.
- TC-FA-NOTIF-377, 412, dan 413 (kejadian kedua pada aset yang sama) ada di spec 113.
- Temuan untuk QA:
  - TC-FA-NOTIF-169, 170, dan 362 menulis Approver (Borrowing & Assignment) tanpa nomor Pre-setup (hanya TC-FA-NOTIF-362 menulis Pre-setup #4), TC-FA-NOTIF-171 menulis Asset Admin (juga Borrower BRW-2026-0342) tanpa nomor Pre-setup, dan TC-FA-NOTIF-359 menulis akun Pre-setup #14 (Citra Lestari). Spec memakai Pre-setup #4, #8, dan #14.
  - TC-FA-NOTIF-169 dan 359 menyebut notifikasi seed N-01 (BRW-2026-0341 (2 Assets) Unread) pada Precondition umum tetapi mengharapkan notifikasi baru dengan Body yang sama; spec membedakannya lewat baseline badge dan keadaan awal yang disiapkan fixture BE.
  - TC-FA-NOTIF-171 menulis "Picu satu event dua peran" dan Data Uji `borrow_overdue` tanpa menyebut job; spec memakai job overdue harian dan jam yang ditetapkan tim FE/BE. TC-FA-NOTIF-171 tidak menyebut akun; Precondition umum hanya "Asset Admin (juga Borrower)".
  - TC-FA-NOTIF-359 tidak menyebut efek hilangnya Total Control pada sesi Citra Lestari yang sedang terbuka; spec mengikuti TC (membuka Bell icon sesudah kedua event).
  - TC-FA-NOTIF-170 tidak menyebut akun yang resubmit; spec memakai sesi API Asset Admin pembuat (Pre-setup #8).
