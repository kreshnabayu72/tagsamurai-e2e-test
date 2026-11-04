---
id: TC-FA-NOTIF-E2E-058-penerima-pic-admin-due-soon-overdue-dan-acceptance-expired
title: "Penerimaan Notifikasi oleh PIC Admin: Due Soon, Overdue, dan Acceptance Expired"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-235
  - TC-FA-NOTIF-237
  - TC-FA-NOTIF-245
coverage:
  web: automated
---
# Penerimaan Notifikasi oleh PIC Admin: Due Soon, Overdue, dan Acceptance Expired

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |

- Login akun aktor pertama (Asset Admin (Gedung A), Pre-setup #8) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): BRW-2026-0342 (AST-2024-0141 Borrowed, Due Date 25/06/26) dan ASG-2026-0120 (Laptop - 1 AST-2024-0067) Pre-setup #19; Asset Admin Pre-setup #8 adalah PIC admin kedua transaksi. Job hanya pemicu.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu job due soon, overdue, dan auto-cancel pada BRW-2026-0342 dan ASG-2026-0120 (Pre-setup #19) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); kemampuan menjalankan job latar dan menggeser jam server dan jam fixture bersama (butir "Kemampuan menjalankan job latar" di `suite.md`); jam server dan jam browser/perangkat diatur bersama, sesi UI dan sesi API aktor tetap valid selama jam digeser.
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10); format tanggal item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi dan pemulihan jam server dan jam fixture ke 18/06/26; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-235: Notifikasi borrow_due_soon varian PIC admin diterima: job harian H-3

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0141 Borrowed, Due Date 25/06/26, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
3. Atur jam server dan jam fixture ke 22/06/26 (H-3 untuk Due Date 25/06/26)
4. Jalankan job harian due soon lewat fixture BE hingga job selesai dan notifikasi tersimpan
5. Pulihkan jam server dan jam fixture ke 18/06/26
6. Klik Bell icon
7. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 2
8. Verifikasi item baru berada di posisi teratas Dropdown Panel
9. Verifikasi Title item baru bold
10. Verifikasi dot Unread tampil pada item baru
11. Verifikasi item menampilkan Title `"Your borrowed asset is due soon"` dan Body `"Kamera DSLR is due on 25/06/26."` (dari template `"[Asset Name] is due on [Due Date]."`)
12. Verifikasi icon `time-line` dengan severity `warning` pada item
13. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
14. Klik judul item tersebut (bukan tombol)
15. Verifikasi halaman tujuan `/fams/borrow?tab=active&highlight=BRW-2026-0342` terbuka
16. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 7

### TC-FA-NOTIF-237: Notifikasi borrow_overdue varian PIC admin diterima: job harian F-FATX-10

17. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0141 Borrowed, Due Date 25/06/26 terlewati; pengingat overdue aktif, lalu muat ulang halaman Fixed Asset > Dashboard
18. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
19. Atur jam server dan jam fixture ke 26/06/26 (hari pertama setelah Due Date 25/06/26)
20. Jalankan job harian overdue (F-FATX-10) lewat fixture BE hingga job selesai dan notifikasi tersimpan
21. Pulihkan jam server dan jam fixture ke 18/06/26
22. Klik Bell icon
23. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 18
24. Verifikasi item baru berada di posisi teratas Dropdown Panel
25. Verifikasi Title item baru bold
26. Verifikasi dot Unread tampil pada item baru
27. Verifikasi item menampilkan Title `"Your borrowed asset is overdue"` dan Body `"Kamera DSLR was due on 25/06/26."` (dari template `"[Asset Name] was due on [Due Date]."`)
28. Verifikasi icon `time-line` dengan severity `warning` pada item
29. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
30. Klik `[Detail]` pada item tersebut
31. Verifikasi halaman tujuan `/fams/borrow?tab=active&highlight=BRW-2026-0342` terbuka
32. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 23

### TC-FA-NOTIF-245: Notifikasi assignment_acceptance_expired varian PIC admin diterima: auto-cancel Waiting for Acceptance lewat 48 jam

33. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): ASG-2026-0120 Waiting for Acceptance lebih dari 48 jam, lalu muat ulang halaman Fixed Asset > Dashboard
34. Catat jumlah pada badge Bell icon Asset Admin sebagai baseline (0 bila badge tidak tampil)
35. Jalankan job terjadwal auto-cancel Waiting for Acceptance (F-ASSIGN-11 langkah 5) lewat fixture BE hingga ASG-2026-0120 dibatalkan otomatis dan notifikasi tersimpan
36. Klik Bell icon
37. Verifikasi badge Bell icon Asset Admin bertambah 1 dari baseline langkah 34
38. Verifikasi item baru berada di posisi teratas Dropdown Panel
39. Verifikasi Title item baru bold
40. Verifikasi dot Unread tampil pada item baru
41. Verifikasi item menampilkan Title `"Assignment acceptance expired"` dan Body `"Laptop - 1 (AST-2024-0067) was not accepted in time."` (dari template `"[Asset Name] ([Asset ID]) was not accepted in time."`)
42. Verifikasi icon `time-line` dengan severity `warning` pada item
43. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
44. Klik judul item tersebut (bukan tombol)
45. Verifikasi halaman tujuan `/fams/transactions-assignment/ASG-2026-0120` terbuka
46. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 37

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 17, 33 (penyiapan kondisi data lewat fixture BE; pada langkah 1, 17, dan 33 diikuti muat ulang halaman Fixed Asset > Dashboard sebelum baseline); langkah 2, 18, 34 (pencatatan baseline badge Bell icon (S-12)); langkah 3, 5, 19, 21 (pengaturan dan pemulihan jam server dan jam fixture).
- Job (due soon, overdue, dan auto-cancel) hanya pemicu, bukan objek uji.
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (46 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- TC-FA-NOTIF-245 menyebut varian ini setara varian Assignee; varian Assignee ada di spec 060 (TC-FA-NOTIF-244).
- Spec 058 memuat penerimaan PIC admin atas BRW-2026-0342 dan ASG-2026-0120 lewat job; penerima lain atas transaksi yang sama ada di spec 057 (Borrower) dan 060 (Assignee).
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
