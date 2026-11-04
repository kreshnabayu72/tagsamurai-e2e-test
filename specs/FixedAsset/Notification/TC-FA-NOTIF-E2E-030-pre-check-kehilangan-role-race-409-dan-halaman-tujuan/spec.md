---
id: TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan
title: "Pre-check Detail: Kehilangan Role, Race 409, dan Validasi Submit di Halaman Tujuan"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-104
  - TC-FA-NOTIF-110
  - TC-FA-NOTIF-363
  - TC-FA-NOTIF-424
coverage:
  web: automated
---

# Pre-check Detail: Kehilangan Role, Race 409, dan Validasi Submit di Halaman Tujuan

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`), memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Pelaku kedua: Approver Borrowing & Assignment Gedung A (Pre-setup #4, `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Approve BRW-2026-0341. BRW-2026-0341 memakai aturan approval OR sehingga Approve Approver #4 menyelesaikan transaksi.
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`. BRW-2026-0341 Waiting for Approval.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): intercept stream SSE di browser untuk memblokir push (butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`; hanya TC-FA-NOTIF-363; blokir SSE adalah pemicu state basi, bukan objek uji, dan dilepas pada langkah 15 di akhir blok TC itu (bukan segera setelah pemicu) agar respons 409 dan dialog D-01 tetap teramati); fixture BE yang mencabut dan memulihkan Transaction Role Approver (Borrowing & Assignment) akun aktor (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`; hanya TC-FA-NOTIF-104 dan 424); membaca status respons HTTP pre-check `[Detail]` dari browser (pemantauan respons).
- State yang diubah spec: BRW-2026-0341 menjadi selesai, N-01 menjadi Read (Auto-Read), dan role Approver akun aktor dicabut. Fixture BE pemulih seed notifikasi, transaksi, dan role akun aktor (Pre-setup #1, #17 sampai #24; butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap blok TC.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): BRW-2026-0341 (Pre-setup #19) di-Approve oleh pelaku kedua dan seed N-01 (Pre-setup #17) menjadi Read dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` dan `FA_APPROVERBA_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-110: Pre-check dan navigasi tidak menggantikan validasi submit di halaman tujuan

1. Pulihkan seed, transaksi, dan Transaction Role Approver (Borrowing & Assignment) akun aktor lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
2. Klik Bell icon
3. Klik `[Detail]` pada item N-01 sehingga halaman Approvals terbuka
4. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
5. Pada halaman Approvals klik Approve
6. Verifikasi submit Approve ditolak oleh modul Approvals

### TC-FA-NOTIF-363: Race klik [Detail] dengan Approve oleh approver lain memberi 409 dan dialog inline

7. Pulihkan seed dan transaksi lewat fixture BE pemulih, lalu buka Fixed Asset > Dashboard
8. Klik Bell icon
9. Blokir push SSE lewat intercept
10. Dari akun Approver Borrowing & Assignment (Pre-setup #4, sesi API), Approve BRW-2026-0341 hingga status transaksi selesai tersimpan
11. Klik `[Detail]` pada item N-01
12. Verifikasi respons pre-check `[Detail]` berstatus `409`
13. Verifikasi Approver A (akun aktor) tidak dinavigasi
14. Verifikasi dialog D-01 tampil tanpa redirect
15. Lepas intercept push SSE

### TC-FA-NOTIF-104: Pre-check [Detail] saat user kehilangan role menampilkan D-01 dan status tetap Unread di server

16. Pulihkan seed dan transaksi lewat fixture BE pemulih, cabut Transaction Role Approver (Borrowing & Assignment) akun aktor lewat fixture BE, lalu muat ulang halaman Fixed Asset > Dashboard
17. Klik Bell icon
18. Klik `[Detail]` pada item N-01
19. Verifikasi dialog D-01 muncul
20. Verifikasi tidak ada navigasi
21. Klik `[Close]` pada dialog D-01
22. Verifikasi tombol `[Detail]` pada item N-01 tersembunyi
23. Verifikasi badge Bell icon berkurang 1 secara lokal dari `5` menjadi `4`
24. Muat ulang halaman Fixed Asset > Dashboard
25. Klik Bell icon
26. Verifikasi item N-01 kembali Unread
27. Verifikasi tombol `[Detail]` pada item N-01 tampil
28. Verifikasi badge Bell icon `5`
29. Klik `[Detail]` pada item N-01 lagi
30. Verifikasi dialog D-01 muncul lagi
31. Verifikasi tidak ada navigasi

### TC-FA-NOTIF-424: Notification Center, pre-check [Detail] saat user kehilangan role menampilkan D-01

32. Klik `[Close]` pada dialog D-01
33. Muat ulang halaman Fixed Asset > Dashboard
34. Klik Bell icon
35. Klik `[Show All]`
36. Klik `[Detail]` pada item N-01
37. Verifikasi dialog D-01 muncul
38. Verifikasi tidak ada navigasi
39. Klik `[Close]` pada dialog D-01
40. Verifikasi tombol `[Detail]` pada item N-01 tersembunyi
41. Verifikasi badge Bell icon berkurang 1 secara lokal dari `5` menjadi `4`
42. Muat ulang halaman Fixed Asset > Dashboard
43. Klik Bell icon
44. Klik `[Show All]`
45. Verifikasi item N-01 kembali Unread
46. Verifikasi tombol `[Detail]` pada item N-01 tampil
47. Verifikasi badge Bell icon `5`
48. Klik `[Detail]` pada item N-01 lagi
49. Verifikasi dialog D-01 muncul lagi
50. Verifikasi tidak ada navigasi

## Notes

- Urutan TC dalam spec berbeda dari urutan sumber: TC-FA-NOTIF-110 dan 363 (akun aktor masih memegang role Approver) dijalankan lebih dulu, lalu TC-FA-NOTIF-104 dan 424 (role dicabut) berurutan sehingga role hanya dicabut sekali (S-10). TC-FA-NOTIF-424 meneruskan state akhir TC-FA-NOTIF-104 (role masih dicabut dan N-01 Unread) sehingga langkah 32 menutup dialog sisa langkah 30.
- Alasan melewati ambang 35 langkah: semua blok satu kelas (pre-check `[Detail]` dan dialog D-01) dan tiap blok berdiri sendiri pada state yang dipulihkan; kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-NOTIF-104 dan 424 adalah pasangan Dropdown Panel dan Notification Center dengan 5 Expected yang sama.
- Langkah penghubung (S-03): langkah 1, 7, dan 16 (pemulihan state dan pencabutan role); langkah 9 (pemblokiran SSE sebagai pemicu state basi, bukan objek uji); langkah 4 dan 10 (pemicu pelaku kedua lewat sesi API hingga tersimpan); langkah 15 (melepas intercept); langkah 32 (menutup dialog sisa); langkah 24, 33, dan 42 (memuat ulang halaman, sesuai langkah TC); langkah 35 dan 44 (membuka Notification Center lewat `[Show All]` karena TC tidak menyebut jalur lain).
- P-2: pemicu state basi berupa intercept SSE (blokir push, kelas b) pada TC-FA-NOTIF-363 yang bukan objek asersi; ditahan sampai akhir blok TC itu (langkah 9 sampai 15; alasan di `## Prerequisites`) dan dilepas sebelum blok TC berikutnya.
- Topik pre-check `[Detail]` terpisah dari dialog D-01 spec 028 dan 029 walau berbagi BRW-2026-0341 dan seed N-01, karena blok di sini mengubah role akun aktor dan gabungannya jauh melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-110 hanya menulis "ditolak oleh modul Approvals sesuai aturan modul itu (asersi hasil dirujuk ke TC modul `approvals/`)" tanpa bentuk penolakan; langkah 6 mengasersi hanya bagian yang ditulis TC.
  - TC-FA-NOTIF-104 dan 424 tidak menyebut cara role dicabut; spec memakai fixture BE (disediakan tim FE/BE). Pada TC-FA-NOTIF-104 dan 424 Expected b ("badge berkurang 1 secara lokal") ditulis sesudah klik `[Close]`, sehingga langkah 22 dan 23 serta 40 dan 41 mengikutinya.
  - TC-FA-NOTIF-110 menulis "Approver lain" tanpa menyebut akun; spec memakai Approver Borrowing & Assignment Pre-setup #4.
  - Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
