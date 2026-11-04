---
id: TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar
title: "Auto-Read Borrow: Approve, Reject, Cancel Form, Navigasi Keluar, Detail Berulang, dan Atomisitas dengan Commit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-111
  - TC-FA-NOTIF-112
  - TC-FA-NOTIF-113
  - TC-FA-NOTIF-114
  - TC-FA-NOTIF-115
  - TC-FA-NOTIF-161
coverage:
  web: automated
---

# Auto-Read Borrow: Approve, Reject, Cancel Form, Navigasi Keluar, Detail Berulang, dan Atomisitas dengan Commit

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Bell icon, Dropdown Panel, dan halaman Approvals.
- Akun aktor: Approver (Borrowing & Assignment) Pre-setup #4 (`approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_APPROVERBA_PASSWORD`, fixture `Fixture.fixedAssetNotification.approverBorrowingAssignment`; nama env usulan, belum terdaftar). TC hanya menulis role tanpa nomor Pre-setup (lihat Temuan untuk QA).
- Login akun aktor pertama (Pre-setup #4) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: transaksi Borrow BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141, Pre-setup #19 dan #24). Precondition tiap TC (notifikasi `borrow_waiting_approval` BRW-2026-0342 Unread untuk akun aktor) dibentuk fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar blok. Spec mengubah state BRW-2026-0342 (Approve dan Reject); fixture BE pemulih mengembalikannya. Alasan Reject `Budget belum tersedia` (Data Uji TC) dibaca dari `Fixture.fixedAssetNotification.rejectionReason`.
- Pemicu TC-FA-NOTIF-161: sesi API Asset Admin pembuat (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_ASSETADMIN_PASSWORD`) men-submit Borrow Request BRW-2026-0342 lewat fixture BE pemicu event; fixture BE menyiapkan keadaan awal BRW-2026-0342 sebelum submit (belum ada notifikasi untuk transaksi itu). Pelaku kedua memakai sesi API, bukan sesi UI.
- Jendela absence notifikasi: "Tunggu 5 detik tanpa memuat ulang halaman" adalah pilihan spec (bukan nilai TC atau PRD).
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (semua akun di atas sudah true), fixture BE pemulih seed notifikasi dan transaksi, fixture BE pemicu event dan penyetel state sumber.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE). Env var password didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): spec ini memakai notifikasi seed dan data Pre-setup literal (BRW-2026-0342) sebagai pemicu atau target aksi; pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` dan sebagai langkah penghubung antar blok, dan suite berjalan serial.
- Suite berjalan serial (`parallel: false`) karena state global bersama (seed notifikasi, jam server, transaksi sumber).

## Test Steps

### TC-FA-NOTIF-111: Approve sukses membuat notifikasi waiting_approval menjadi Read

1. Catat nilai badge Bell icon (baseline)
2. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0342
3. Pada halaman Approvals, Approve BRW-2026-0342 sampai sukses
4. Klik Bell icon
5. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
6. Verifikasi tombol `[Detail]` tidak tampil pada item itu
7. Verifikasi badge Bell icon berkurang 1 dari baseline langkah 1

### TC-FA-NOTIF-112: Reject sukses membuat notifikasi waiting_approval menjadi Read

8. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0342
9. Pada halaman Approvals, Reject BRW-2026-0342 dengan alasan dari `Fixture.fixedAssetNotification.rejectionReason` sampai sukses
10. Klik Bell icon
11. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
12. Verifikasi tombol `[Detail]` tidak tampil pada item itu

### TC-FA-NOTIF-113: Isi dialog konfirmasi Approve lalu Cancel tetap Unread

13. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon (baseline)
14. Klik Bell icon lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0342
15. Pada halaman Approvals pilih Approve sampai dialog konfirmasi Approve tampil, lalu klik `[Cancel]` pada dialog itu tanpa submit
16. Verifikasi tidak ada toast yang tampil
17. Klik Bell icon
18. Verifikasi item `Waiting for your approval` BRW-2026-0342 tetap Unread
19. Verifikasi tombol `[Detail]` tampil pada item itu
20. Verifikasi badge Bell icon sama dengan baseline langkah 13

### TC-FA-NOTIF-114: Navigasi keluar dari form tanpa submit tetap Unread

21. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0342
22. Pada halaman Approvals isi alasan Reject dari `Fixture.fixedAssetNotification.rejectionReason`, lalu pindah ke menu Dashboard tanpa submit
23. Klik Bell icon
24. Verifikasi item `Waiting for your approval` BRW-2026-0342 tetap Unread
25. Verifikasi tombol `[Detail]` tampil pada item itu

### TC-FA-NOTIF-115: Detail diklik berkali-kali tanpa submit tetap Unread

26. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu catat nilai badge Bell icon (baseline)
27. Klik Bell icon, klik `[Detail]` pada item `Waiting for your approval` BRW-2026-0342, lalu kembali ke Dashboard lewat tombol kembali browser
28. Klik Bell icon
29. Verifikasi item `Waiting for your approval` BRW-2026-0342 tetap Unread
30. Verifikasi badge Bell icon sama dengan baseline langkah 26
31. Ulangi langkah 27 sampai 30 dua kali lagi (total tiga kali)

### TC-FA-NOTIF-161: Auto-Read atomik dengan commit aksi penyelesaian

32. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, muat ulang halaman Fixed Asset > Dashboard, lalu klik Bell icon
33. Lewat sesi API Asset Admin pembuat (Pre-setup #8), submit Borrow Request BRW-2026-0342 hingga notifikasi `borrow_waiting_approval` untuk akun aktor tersimpan
34. Verifikasi item baru `Waiting for your approval` BRW-2026-0342 tampil pada Dropdown Panel tanpa memuat ulang halaman
35. Klik `[Detail]` pada item baru itu
36. Pada halaman Approvals, Approve BRW-2026-0342 sampai sukses
37. Klik Bell icon
38. Verifikasi item `Waiting for your approval` BRW-2026-0342 berstatus Read
39. Tunggu 5 detik tanpa memuat ulang halaman
40. Verifikasi tidak ada item `Waiting for your approval` BRW-2026-0342 berstatus Unread pada Dropdown Panel

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2, 8, 13, 14, 21, 26, 32, 35 dan 39. Awalan "Pulihkan seed ..." pada langkah pembuka blok (pemulihan fixture BE, muat ulang halaman, dan pembukaan Dropdown Panel); langkah `[Detail]` dari Dropdown Panel adalah jalur ke halaman Approvals; langkah Tunggu 5 detik adalah jendela absence (bagian 6); langkah baseline badge dicatat sebelum aksi pertama sebagai pembanding.
- Asersi tambahan di luar Expected TC (S-03): langkah 34. Langkah 34 adalah penanda bahwa notifikasi baru sudah masuk sebelum Approve (TC-FA-NOTIF-161: "segera setelah notifikasi muncul") dan menjadi anchor positif bagi asersi absence pada langkah akhir blok itu (bagian 8b butir 2 dan 11).
- Pembagian per TC: TC-FA-NOTIF-111 (langkah 1 sampai 7), TC-FA-NOTIF-112 (langkah 8 sampai 12), TC-FA-NOTIF-113 (langkah 13 sampai 20), TC-FA-NOTIF-114 (langkah 21 sampai 25), TC-FA-NOTIF-115 (langkah 26 sampai 31), TC-FA-NOTIF-161 (langkah 32 sampai 40).
- Pengulangan pada TC-FA-NOTIF-115 (langkah 27 sampai 30) dijalankan dua kali lagi sesuai Langkah TC "ulangi dua kali"; parameter tiap pengulangan identik.
- Asersi absence toast pada TC-FA-NOTIF-113 ditulis segera setelah `[Cancel]` dan sebelum asersi artefak (bagian 8b butir 11); item Unread dan badge pada langkah berikutnya adalah bukti bahwa klik `[Cancel]` sudah diproses. Klausa "tidak ada perubahan di sisi notifikasi" (Expected b) tidak punya Verifikasi terpisah: dicakup item Unread, tombol `[Detail]`, dan badge sama baseline (Expected a).
- TC-FA-NOTIF-116 (submit di satu tab, Auto-Read di tab lain) ada di spec 102.
- Spec ini 40 langkah (48 setelah ekspansi pengulangan langkah 27 sampai 30; di atas smell sekitar 35 langkah): keenam TC satu topik (Auto-Read notifikasi `borrow_waiting_approval` milik Approver yang sama), memakai akun, transaksi BRW-2026-0342, dan seed yang sama; tiap blok berdiri sendiri karena seed dipulihkan di antara blok sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Alasan pemisahan: topik Auto-Read memakai seed notifikasi dan transaksi Pre-setup yang sama; spec ini hanya memuat notifikasi `borrow_waiting_approval` milik Approver Borrow dan Assignment (Approve, Reject, Cancel form, navigasi keluar, Detail berulang), karena tiap kelompok penerima memakai akun dan pemulihan seed sendiri dan penyatuan semuanya jauh melewati sekitar 35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-111 sampai 115 dan 161 menulis "Login sbg Role: Approver (Borrowing & Assignment)" tanpa nomor Pre-setup; spec memakai Pre-setup #4 (Approver Borrow dan Assignment). TC-FA-NOTIF-111 dan 112 tidak menulis Post Condition (kolom kosong).
  - TC-FA-NOTIF-161 tidak menyebut pemicu notifikasi baru, akun pemicunya, maupun keadaan awal BRW-2026-0342; spec memakai submit Borrow Request lewat sesi API Asset Admin pembuat (Pre-setup #8, akun tidak tertulis di langkah TC) dan fixture BE penyiap keadaan awal. Kata "segera" tidak punya batas waktu; spec menunggu notifikasi tampil (langkah 34) lalu melanjutkan.
  - TC-FA-NOTIF-113 tidak menyebut label tombol Cancel pada dialog konfirmasi Approve (PRD mendefinisikan Approve sebagai dialog konfirmasi dengan `[Cancel]`); spec menulis `[Cancel]` mengikuti TC. TC-FA-NOTIF-114 tidak menyebut apakah dialog Unsaved Changes muncul saat pindah menu dengan alasan Reject terisi; spec mengikuti TC (langsung berpindah ke Dashboard). TC-FA-NOTIF-115 tidak menyebut cara "kembali"; spec memakai tombol kembali browser.
  - TC-FA-NOTIF-161 menulis Expected "tidak ada notifikasi Unread tersisa" tanpa batas waktu pengamatan; spec memakai jendela 5 detik (pilihan spec, Prerequisites).
