---
id: TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center
title: "Dialog D-01 Transaction Resolved dari Notification Center dan Penutupan dengan Esc"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-101
  - TC-FA-NOTIF-392
  - TC-FA-NOTIF-422
  - TC-FA-NOTIF-423
coverage:
  web: automated
---

# Dialog D-01 Transaction Resolved dari Notification Center dan Penutupan dengan Esc

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`), memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku kedua: Approver Borrowing & Assignment Gedung A (Pre-setup #4, `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Approve BRW-2026-0341. BRW-2026-0341 memakai aturan approval OR sehingga Approve Approver #4 menyelesaikan transaksi.
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): intercept stream SSE di browser untuk memblokir push (butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`). Blokir SSE adalah pemicu state basi, bukan objek uji; intercept dipasang pada langkah 2, 22, dan 31 dan dilepas pada langkah 14, 28, dan 38 (akhir tiap blok TC yang memakainya, bukan segera setelah pemicu) agar dialog D-01 dan state klien basi tetap teramati; hook `after` menjadi cadangan.
- Spec mengubah BRW-2026-0341 menjadi selesai dan N-01 menjadi Read (Auto-Read). Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap blok pemicu (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): BRW-2026-0341 (Pre-setup #19) di-Approve oleh pelaku kedua dan seed N-01 (Pre-setup #17) menjadi Read dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` dan `FA_APPROVERBA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-101: Klik [Detail] saat transaksi sudah ditindak pihak lain menampilkan dialog inline D-01 dari Notification Center

1. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
2. Blokir push SSE lewat intercept (tetap aktif sampai langkah 14)
3. Klik Bell icon
4. Klik `[Show All]`
5. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
6. Klik `[Detail]` pada item N-01
7. Verifikasi tidak ada navigasi dan tidak ada redirect (halaman tetap Notification Center)
8. Verifikasi pengguna tetap pada list Notification Center
9. Verifikasi dialog D-01 muncul dengan Title `Transaction Resolved`, Body `This transaction no longer needs your action.`, dan tombol `[Close]`

### TC-FA-NOTIF-423: Notification Center, menutup dialog D-01 menyembunyikan [Detail] dan mengurangi badge secara lokal

10. Klik `[Close]` pada dialog D-01
11. Verifikasi dialog D-01 tertutup
12. Verifikasi tombol `[Detail]` pada item N-01 hilang
13. Verifikasi badge Bell icon berkurang 1 dari `5` menjadi `4`

14. Lepas intercept push SSE

### TC-FA-NOTIF-392: Notification Center, klik area item actionable Unread menjalankan pre-check lalu navigasi atau D-01

15. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
16. Klik Bell icon
17. Klik `[Show All]`
18. Klik judul item N-01 (bukan tombol)
19. Verifikasi browser berpindah ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`
20. Kembali ke Notification Center (navigasi balik browser)
21. Verifikasi status baca item N-01 tidak berubah (tetap Unread)
22. Blokir push SSE lewat intercept (tetap aktif sampai langkah 28)
23. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
24. Klik body item N-01 (bukan tombol)
25. Verifikasi tidak ada navigasi dan tidak ada redirect (halaman tetap Notification Center)
26. Verifikasi dialog D-01 muncul dengan Title `Transaction Resolved`, Body `This transaction no longer needs your action.`, dan tombol `[Close]`
27. Verifikasi pengguna tetap pada list Notification Center
28. Lepas intercept push SSE

### TC-FA-NOTIF-422: Tombol Esc menutup dialog D-01 dengan efek yang sama dengan [Close]

29. Pulihkan seed notifikasi dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
30. Klik Bell icon
31. Blokir push SSE lewat intercept (tetap aktif sampai langkah 38)
32. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
33. Klik `[Detail]` pada item N-01
34. Tekan Esc
35. Verifikasi dialog D-01 tertutup
36. Verifikasi tombol `[Detail]` pada item N-01 hilang
37. Verifikasi badge Bell icon berkurang 1 dari `5` menjadi `4`
38. Lepas intercept push SSE

## Notes

- Urutan TC dalam spec berbeda dari urutan sumber: TC-FA-NOTIF-423 (menutup dialog) dijalankan tepat sesudah TC-FA-NOTIF-101 pada dialog D-01 yang sama (langkah 6 sampai 13), TC-FA-NOTIF-392 sesudahnya dengan pemicu sendiri, dan TC-FA-NOTIF-422 terakhir karena memakai Dropdown Panel (S-10). Langkah picu dialog TC-FA-NOTIF-423 ("Buka Notification Center; Picu dialog D-01 dari item N-01") dan TC-FA-NOTIF-422 ("Picu dialog D-01 dari item N-01 di Dropdown Panel") dipenuhi langkah 3 sampai 6 dan langkah 30 sampai 33.
- Langkah penghubung (S-03): langkah 1, 15, dan 29 (pemulihan seed dan transaksi); langkah 2, 22, dan 31 (pemblokiran SSE sebagai pemicu state basi, bukan objek uji); langkah 3 dan 4, 16 dan 17, serta 30 (membuka Notification Center lewat Bell icon dan `[Show All]` karena TC tidak menyebut jalur lain, atau membuka Dropdown Panel); langkah 5, 23, dan 32 (pemicu pelaku kedua lewat sesi API hingga tersimpan); langkah 20 (kembali ke Notification Center); langkah 14, 28, dan 38 (melepas intercept).
- Asersi tambahan (S-03): langkah 8 dan 27 memecah klausa Expected "tidak ada navigasi dan tidak ada redirect; pengguna tetap pada list Notification Center" menjadi dua `Verifikasi`.
- P-2: pemicu state basi berupa intercept SSE (blokir push, kelas b) yang bukan objek asersi; ditahan sampai akhir blok TC yang membutuhkannya (langkah 2 sampai 14, 22 sampai 28, dan 31 sampai 38; alasan di `## Prerequisites`) dan dilepas sebelum blok TC berikutnya.
- Dialog D-01 dipisah per surface pemicu (028 Dropdown Panel, 029 Notification Center) walau berbagi BRW-2026-0341 dan seed N-01, karena gabungannya jauh melampaui ~35 langkah.
- Alasan melewati ambang 35 langkah (38 langkah): semua blok satu kelas (dialog D-01) dan tiap blok berdiri sendiri pada state yang dipulihkan; tiga pasang langkah blokir dan lepas intercept menambah langkah tanpa menambah asersi.
- Temuan untuk QA:
  - TC-FA-NOTIF-101 dan 392 menulis "Approver lain" tanpa menyebut akun; spec memakai Approver Borrowing & Assignment Pre-setup #4.
  - TC-FA-NOTIF-422 memakai Dropdown Panel, sedangkan tiga TC lain di spec ini memakai Notification Center; Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
