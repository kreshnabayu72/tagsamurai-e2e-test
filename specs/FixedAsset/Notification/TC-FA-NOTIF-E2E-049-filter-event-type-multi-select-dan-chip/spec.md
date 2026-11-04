---
id: TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip
title: "Filter Event Type: Multi-Select, Chip, Opsi Real-Time, dan Varian Event"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-201
  - TC-FA-NOTIF-202
  - TC-FA-NOTIF-203
  - TC-FA-NOTIF-204
  - TC-FA-NOTIF-215
  - TC-FA-NOTIF-216
coverage:
  web: automated
---

# Filter Event Type: Multi-Select, Chip, Opsi Real-Time, dan Varian Event

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; akun memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-37 (Pre-setup #17 dan #18, total 37 notifikasi; `borrow_resolved` punya varian Approved (Read, di antara N-08 sampai N-37) dan Rejected (N-06)) milik akun aktor, tanpa notifikasi `borrow_almost_timeout` (event_type di luar 11 opsi). Seed dipulihkan fixture BE pemulih di hook `before` dan `after` dan sebagai langkah penghubung antar TC. Transaksi Borrow BRW-2026-0342 (Pre-setup #19) berstatus Waiting for Approval dengan timeout snapshot 3 hari dan sisa waktu 24 jam dipakai sebagai pemicu TC-215 dan dipulihkan fixture BE pemulih. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pemicu TC-215: job `F-FATX-07` langkah 2 dijalankan lewat kemampuan job latar suite (disediakan tim FE/BE; endpoint tidak dikarang) sehingga notifikasi `borrow_almost_timeout` varian Approver terkirim ke akun aktor.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah job `F-FATX-07` langkah 2 pada transaksi BRW-2026-0342 (Pre-setup #19) dan seed notifikasi Pre-setup #17 dan #18 pada akun aktor milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih seed notifikasi dan transaksi, serta kemampuan menjalankan job latar.

## Test Steps

### TC-FA-NOTIF-201: Filter Event Type multi-select memakai logika OR dalam field

1. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
2. Klik icon Filter, centang `Damaged Repaired` dan `Missing Found`, lalu klik `[Apply]`
3. Scroll sampai akhir list hingga seluruh item termuat
4. Verifikasi list memuat item `damaged_repaired` (`Asset has been repaired`)
5. Verifikasi list memuat item `missing_found`
6. Verifikasi badge titik tampil pada icon Filter

### TC-FA-NOTIF-202: Chip opsi terpilih muncul di dalam field dan dihapus lewat (X) tersinkron ke checkbox

7. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
8. Klik icon Filter, centang `Damaged Repaired` dan `Missing Found`
9. Klik `(✕)` pada chip `Damaged Repaired`
10. Verifikasi chip `Missing Found` tetap ada
11. Verifikasi chip `Damaged Repaired` hilang
12. Buka dropdown `Event Type`
13. Verifikasi checkbox `Damaged Repaired` unchecked

### TC-FA-NOTIF-203: Menghapus opsi lewat uncheck di dalam dropdown tersinkron ke chip

14. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
15. Klik icon Filter, centang `Damaged Repaired` dan `Missing Found`
16. Buka dropdown `Event Type` lalu uncheck `Damaged Repaired`
17. Verifikasi chip `Damaged Repaired` hilang
18. Verifikasi chip `Missing Found` tetap ada

### TC-FA-NOTIF-204: Chip berlebih diringkas menjadi +N more

19. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
20. Klik icon Filter lalu centang delapan opsi Event Type: `Access Total Control Removed`, `Assignment Waiting Approval`, `Audit Resolved`, `Audit Task Started`, `Borrow Confirmation Required`, `Borrow Resolved`, `Borrow Waiting Approval`, `Damaged Repaired`
21. Verifikasi chip yang muat ditampilkan dan sisanya diringkas menjadi satu chip `+N more` (N = jumlah chip tersembunyi)
22. Verifikasi field tidak melebar dan tidak digulir horizontal

### TC-FA-NOTIF-215: Opsi Event Type bertambah real-time saat event_type baru diterima

23. Pulihkan seed notifikasi dan transaksi lewat fixture BE pemulih, muat ulang halaman, lalu klik Bell icon dan `[Show All]`
24. Lewat kemampuan job latar suite, jalankan job `F-FATX-07` langkah 2 untuk BRW-2026-0342 Waiting for Approval (timeout snapshot 3 hari, sisa waktu 24 jam) hingga notifikasi `borrow_almost_timeout` varian Approver tersimpan untuk akun aktor
25. Klik icon Filter lalu buka dropdown `Event Type`
26. Verifikasi opsi `Borrow Almost Timeout` tampil walau tidak ada pada seed awal
27. Pulihkan seed notifikasi dan transaksi lewat fixture BE pemulih, lalu muat ulang halaman

### TC-FA-NOTIF-216: Filter Event Type untuk event bervarian menyaring semua varian

28. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)
29. Klik icon Filter, pilih Event Type `Borrow Resolved`, lalu klik `[Apply]`
30. Scroll sampai akhir list hingga seluruh item termuat
31. Verifikasi list memuat varian Approved `borrow_resolved`
32. Verifikasi list memuat varian Rejected `borrow_resolved` (N-06 `Your request has been rejected`)
33. Klik Bell icon, lalu klik `[Show All]` (mereset Tab, Search, Sort, dan Filter ke default)

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 7, 14, 19, 28, 33 (masuk kembali lewat `[Show All]` yang mereset kontrol ke default; perilaku reset ini diasersi spec 114), 3 dan 30 (memuat seluruh item), 23 dan 27 (pemulihan seed dan transaksi serta muat ulang).
- Asersi tambahan: tidak ada.
- Kedelapan opsi Event Type pada langkah 20 dipilih dari daftar 11 opsi TC-197 (spec 048) karena TC-204 hanya menyebut "delapan opsi".
- Pemicu job pada langkah 24 hanya membentuk kondisi yang diuji (opsi baru muncul), bukan objek uji ambang waktu job.
- Temuan untuk QA:
  - TC-204 tidak menyebut delapan opsi yang dicentang; spec memilih delapan opsi pertama dari daftar 11 opsi TC-197.
  - TC-201 butir a ("gabungan OR") tidak menyebut judul item `missing_found`; spec menulisnya sebagai event_type.
  - TC-215 menyebut event_type `borrow_almost_timeout` "belum ada pada seed" tanpa langkah `Verifikasi` dan tanpa menunggu notifikasi tiba sebelum membuka dropdown; spec membuka dropdown sesudah notifikasi tersimpan.
