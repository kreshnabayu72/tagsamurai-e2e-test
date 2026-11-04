---
id: TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue
title: "Penerimaan Notifikasi Borrow oleh Borrower: Konfirmasi, Handover, Due Soon, dan Overdue"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-232
  - TC-FA-NOTIF-233
  - TC-FA-NOTIF-234
  - TC-FA-NOTIF-236
coverage:
  web: automated
---
# Penerimaan Notifikasi Borrow oleh Borrower: Konfirmasi, Handover, Due Soon, dan Overdue

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Borrower Budi Santoso | #11 | `borrowerBudi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_BORROWER_PASSWORD` | `Fixture.fixedAssetNotification.borrowerBudi` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Menyelesaikan verifikasi scan dan handover fisik BRW-2026-0342.
- Login akun aktor pertama (Borrower Budi Santoso, Pre-setup #11) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): BRW-2026-0342 (aset Kamera DSLR AST-2024-0141, Borrower Budi Santoso; Pre-setup #19). Due Date 25/06/26 dan jam fixture hari ini 18/06/26. Job due soon dan overdue (F-FATX-10) hanya pemicu, bukan objek uji.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang memicu verifikasi scan, handover fisik, dan job due soon atau overdue pada BRW-2026-0342 dan AST-2024-0141 (Pre-setup #19 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); kemampuan menjalankan job latar dan menggeser jam server dan jam fixture bersama (butir "Kemampuan menjalankan job latar" di `suite.md`); jam server dan jam browser/perangkat diatur bersama, sesi UI dan sesi API aktor tetap valid selama jam digeser.
- Asersi "badge bertambah 1" memakai baseline per penerima yang dicatat tepat sebelum pemicu tiap TC (bagian 8b butir 10); format tanggal item mengikuti Date Format General Settings default `dd/MM/yy` dengan jam fixture hari ini 18/06/26 (zona Asia/Jakarta).
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi dan pemulihan jam server dan jam fixture ke 18/06/26; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_BORROWER_PASSWORD`, `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-232: Notifikasi borrow_confirmation_required diterima: verifikasi scan selesai, status Waiting for Confirmation

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): BRW-2026-0342 Ready for Verification dan Budi Santoso Borrower, lalu muat ulang halaman Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon Borrower sebagai baseline (0 bila badge tidak tampil)
3. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan BRW-2026-0342 hingga status Waiting for Confirmation tersimpan
4. Klik Bell icon
5. Verifikasi badge Bell icon Borrower bertambah 1 dari baseline langkah 2
6. Verifikasi item baru berada di posisi teratas Dropdown Panel
7. Verifikasi Title item baru bold
8. Verifikasi dot Unread tampil pada item baru
9. Verifikasi item menampilkan Title `"Please confirm your borrowed asset"` dan Body `"Kamera DSLR (AST-2024-0141)"` (dari template `"[Asset Name] ([Asset ID])"`)
10. Verifikasi icon `time-line` dengan severity `primary` pada item
11. Verifikasi tombol `[Detail]` tampil tanpa `[Mark as Read]` pada item
12. Klik `[Detail]` pada item tersebut
13. Verifikasi halaman tujuan `/fams/my-asset/task/borrow/BRW-2026-0342` terbuka
14. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 5

### TC-FA-NOTIF-233: Notifikasi borrow_handover_completed diterima: handover fisik selesai, status Borrowed

15. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): BRW-2026-0342 Ready for Handover, lalu muat ulang halaman Fixed Asset > Dashboard
16. Catat jumlah pada badge Bell icon Borrower sebagai baseline (0 bila badge tidak tampil)
17. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover fisik BRW-2026-0342 (F-BORROW-11) hingga status Borrowed tersimpan
18. Klik Bell icon
19. Verifikasi badge Bell icon Borrower bertambah 1 dari baseline langkah 16
20. Verifikasi item baru berada di posisi teratas Dropdown Panel
21. Verifikasi Title item baru bold
22. Verifikasi dot Unread tampil pada item baru
23. Verifikasi item menampilkan Title `"Asset handover completed"` dan Body `"Kamera DSLR is now officially your responsibility."` (dari template `"[Asset Name] is now officially your responsibility."`)
24. Verifikasi icon `checkbox-circle-line` dengan severity `success` pada item
25. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
26. Klik judul item tersebut (bukan tombol)
27. Verifikasi halaman tujuan `/fams/my-asset/borrowed/BRW-2026-0342` terbuka
28. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 19

### TC-FA-NOTIF-234: Notifikasi borrow_due_soon varian Borrower diterima: job harian H-3

29. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0141 Borrowed, Due Date 25/06/26, lalu muat ulang halaman Fixed Asset > Dashboard
30. Catat jumlah pada badge Bell icon Borrower sebagai baseline (0 bila badge tidak tampil)
31. Atur jam server dan jam fixture ke 22/06/26 (H-3 untuk Due Date 25/06/26)
32. Jalankan job harian due soon lewat fixture BE hingga job selesai dan notifikasi tersimpan
33. Pulihkan jam server dan jam fixture ke 18/06/26
34. Klik Bell icon
35. Verifikasi badge Bell icon Borrower bertambah 1 dari baseline langkah 30
36. Verifikasi item baru berada di posisi teratas Dropdown Panel
37. Verifikasi Title item baru bold
38. Verifikasi dot Unread tampil pada item baru
39. Verifikasi item menampilkan Title `"Your borrowed asset is due soon"` dan Body `"Kamera DSLR is due on 25/06/26."` (dari template `"[Asset Name] is due on [Due Date]."`)
40. Verifikasi icon `time-line` dengan severity `warning` pada item
41. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
42. Klik judul item tersebut (bukan tombol)
43. Verifikasi halaman tujuan `/fams/my-asset/borrowed/BRW-2026-0342` terbuka
44. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 35

### TC-FA-NOTIF-236: Notifikasi borrow_overdue varian Borrower diterima: job harian F-FATX-10 saat pengingat overdue aktif

45. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): AST-2024-0141 Borrowed, Due Date 25/06/26 terlewati; pengingat overdue aktif, lalu muat ulang halaman Fixed Asset > Dashboard
46. Catat jumlah pada badge Bell icon Borrower sebagai baseline (0 bila badge tidak tampil)
47. Atur jam server dan jam fixture ke 26/06/26 (hari pertama setelah Due Date 25/06/26)
48. Jalankan job harian overdue (F-FATX-10) lewat fixture BE hingga job selesai dan notifikasi tersimpan
49. Pulihkan jam server dan jam fixture ke 18/06/26
50. Klik Bell icon
51. Verifikasi badge Bell icon Borrower bertambah 1 dari baseline langkah 46
52. Verifikasi item baru berada di posisi teratas Dropdown Panel
53. Verifikasi Title item baru bold
54. Verifikasi dot Unread tampil pada item baru
55. Verifikasi item menampilkan Title `"Your borrowed asset is overdue"` dan Body `"Kamera DSLR was due on 25/06/26."` (dari template `"[Asset Name] was due on [Due Date]."`)
56. Verifikasi icon `time-line` dengan severity `warning` pada item
57. Verifikasi tombol `[Mark as Read]` tampil tanpa `[Detail]` pada item
58. Klik judul item tersebut (bukan tombol)
59. Verifikasi halaman tujuan `/fams/my-asset/borrowed/BRW-2026-0342` terbuka
60. Verifikasi status baca item tidak berubah: badge Bell icon tetap sama seperti pada langkah 51

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Pemicu event dijalankan di modul sumber lewat sesi API aktor atau fixture BE; asersi hanya pada Bell icon, Dropdown Panel, dan halaman tujuan klik (Catatan TC).
- Langkah penghubung (S-03): langkah 1, 15, 29, 45 (penyiapan kondisi data lewat fixture BE; pada langkah 1, 15, 29, 45 diikuti muat ulang halaman Fixed Asset > Dashboard sebelum baseline); langkah 2, 16, 30, 46 (pencatatan baseline badge Bell icon (S-12)); langkah 31, 33, 47, 49 (pengaturan dan pemulihan jam server dan jam fixture).
- Klausa "tanpa mengubah status baca" diasersi lewat badge Bell icon yang tetap sama sesudah klik, karena item tidak teramati pada halaman tujuan (S-03; cara observasi dipilih spec, bukan nilai TC).
- Alasan melewati ambang sekitar 35 langkah (60 langkah): semua blok satu kelas (fungsional penerimaan event) dan tiap blok TC berdiri sendiri dengan kondisi data dipulihkan fixture BE di awal blok; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan jumlah langkah berasal dari struktur identik per blok (penyiapan, baseline, pemicu, delapan sampai sembilan Verifikasi per klausa Expected).
- Blok TC-FA-NOTIF-234 dan 236 memakai job dan jam hanya sebagai pemicu (bukan objek uji); batas waktu job sebagai objek uji ada di spec job terjadwal.
- Spec 057 memuat penerimaan Borrower atas BRW-2026-0342; keputusan approval ada di spec 056 dan penerimaan PIC admin di spec 058.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-234 menulis "job harian due soon" tanpa menyebut kode job; spec tidak mengarang nama job.
