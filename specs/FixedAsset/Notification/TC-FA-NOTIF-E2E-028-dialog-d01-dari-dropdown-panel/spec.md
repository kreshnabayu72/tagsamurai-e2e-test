---
id: TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel
title: "Dialog D-01 Transaction Resolved dari Dropdown Panel"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-100
  - TC-FA-NOTIF-102
  - TC-FA-NOTIF-103
  - TC-FA-NOTIF-108
  - TC-FA-NOTIF-421
coverage:
  web: automated
---

# Dialog D-01 Transaction Resolved dari Dropdown Panel

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`), memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku kedua: Approver Borrowing & Assignment Gedung A (Pre-setup #4, `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Approve BRW-2026-0341. BRW-2026-0341 memakai aturan approval OR sehingga Approve Approver #4 menyelesaikan transaksi.
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): intercept stream SSE di browser untuk memblokir push (butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`); blokir SSE adalah pemicu state basi, bukan objek uji, dan dilepas di akhir tiap blok yang memakainya (bukan segera setelah pemicu) agar dialog D-01 dan state klien basi tetap teramati; kemampuan membaca status baca notifikasi di BE (langkah 22).
- Spec mengubah BRW-2026-0341 menjadi selesai dan N-01 menjadi Read (Auto-Read). Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap blok pemicu (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): BRW-2026-0341 (Pre-setup #19) di-Approve oleh pelaku kedua dan seed N-01 (Pre-setup #17) menjadi Read dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` dan `FA_APPROVERBA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-100: Klik [Detail] saat transaksi sudah ditindak pihak lain menampilkan dialog inline D-01 dari Dropdown Panel

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
2. Klik Bell icon
3. Blokir push SSE lewat intercept
4. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
5. Klik `[Detail]` pada item N-01
6. Verifikasi tidak ada navigasi dan tidak ada redirect (halaman tetap Fixed Asset > Dashboard)
7. Verifikasi pengguna tetap pada Dropdown Panel
8. Verifikasi dialog D-01 muncul dengan Title `Transaction Resolved`, Body `This transaction no longer needs your action.`, dan tombol `[Close]` (primary)

### TC-FA-NOTIF-102: Screening dialog D-01

9. Verifikasi Title dialog D-01 adalah `Transaction Resolved`
10. Verifikasi Body dialog D-01 adalah `This transaction no longer needs your action.`
11. Verifikasi dialog D-01 memiliki tepat satu tombol `[Close]` bergaya primary

### TC-FA-NOTIF-421: Klik backdrop tidak menutup dialog D-01

12. Klik area backdrop di luar dialog D-01
13. Verifikasi dialog D-01 tetap terbuka
14. Verifikasi tombol `[Detail]` pada item N-01 belum disembunyikan
15. Verifikasi badge Bell icon tetap `5`

### TC-FA-NOTIF-103: Menutup dialog D-01 menyembunyikan [Detail] dan mengurangi badge secara lokal

16. Klik `[Close]` pada dialog D-01
17. Verifikasi dialog D-01 tertutup
18. Verifikasi tidak ada navigasi atau aksi lanjutan setelah dialog tertutup (halaman tetap Fixed Asset > Dashboard)
19. Verifikasi tombol `[Detail]` pada item N-01 hilang
20. Verifikasi badge Bell icon berkurang 1 dari `5` menjadi `4`
21. Muat ulang halaman Fixed Asset > Dashboard
22. Verifikasi (kemampuan baca BE) status item N-01 sudah Read di server, ditulis oleh Auto-Read
23. Lepas intercept push SSE

### TC-FA-NOTIF-108: Klik area item actionable Unread pada transaksi yang sudah ditindak menampilkan D-01

24. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
25. Klik Bell icon
26. Blokir push SSE lewat intercept
27. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
28. Klik body item N-01 (bukan tombol)
29. Verifikasi dialog D-01 muncul
30. Verifikasi tidak ada navigasi (halaman tetap Fixed Asset > Dashboard)
31. Lepas intercept push SSE

## Notes

- Urutan TC dalam spec berbeda dari urutan sumber: TC-FA-NOTIF-100, 102, dan 421 hanya mengamati satu instans dialog D-01 yang sama (langkah 1 sampai 15), lalu TC-FA-NOTIF-103 menutup dialog itu (langkah 16 sampai 23), dan TC-FA-NOTIF-108 yang memicu dialog dari klik body item dijalankan terakhir dengan pemicu sendiri (langkah 24 sampai 31). Penutupan dialog diletakkan sesudah semua TC yang membutuhkan dialog terbuka (S-10). Langkah picu dialog TC-FA-NOTIF-102, 103, dan 421 ("Picu dialog D-01 dari item N-01") dipenuhi langkah 2 sampai 5.
- Langkah penghubung (S-03): langkah 1 dan 24 (pemulihan seed dan transaksi); langkah 2 dan 25 (membuka Dropdown Panel); langkah 21 (memuat ulang halaman, sesuai langkah TC); langkah 23 dan 31 (melepas intercept); langkah 3 dan 26 (pemblokiran SSE sebagai pemicu state basi, bukan objek uji); langkah 4 dan 27 (pemicu pelaku kedua lewat sesi API hingga tersimpan).
- Asersi tambahan (S-03): langkah 7 memecah klausa Expected a TC-FA-NOTIF-100 ("tidak ada navigasi dan tidak ada redirect; pengguna tetap pada Dropdown Panel"); langkah 18 menulis klausa "menutup dialog tanpa aksi lanjutan" pada Expected c TC-FA-NOTIF-102 sesudah tombol `[Close]` diklik; langkah 9 sampai 11 menjadi `Verifikasi` Expected TC-FA-NOTIF-102 sendiri walau Title, Body, dan tombol sudah tercakup langkah 8.
- P-2: pemicu state basi berupa intercept SSE (blokir push, kelas b) yang bukan objek asersi; ditahan sampai akhir blok TC yang membutuhkannya (langkah 3 sampai 23 dan langkah 26 sampai 31; alasan di `## Prerequisites`) dan dilepas sebelum blok TC berikutnya.
- Dialog D-01 dipisah per surface pemicu (028 Dropdown Panel, 029 Notification Center) walau berbagi BRW-2026-0341 dan seed N-01, karena gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-100, 102, 103, 108, dan 421 menulis "Approver lain" tanpa menyebut akun; spec memakai Approver Borrowing & Assignment Pre-setup #4.
  - Expected c TC-FA-NOTIF-103 ("klien hanya menyinkronkan tampilan") adalah kesimpulan; spec hanya mengasersi status Read di server (langkah 22). Post Condition TC-FA-NOTIF-100, 102, 103, 108, dan 421 kosong (`-`); tidak ada yang diasersi.
