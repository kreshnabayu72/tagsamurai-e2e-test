---
id: TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403
title: "Resilience Mark as Read: Gagal 5xx, Timeout Jaringan, dan Respons 403"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-76
  - TC-FA-NOTIF-77
  - TC-FA-NOTIF-354
  - TC-FA-NOTIF-379
coverage:
  web: automated
---

# Resilience Mark as Read: Gagal 5xx, Timeout Jaringan, dan Respons 403

## Prerequisites

- Mode: FE+BE (kegagalan dipaksa lewat `Spectra.intercept()` di atas backend nyata; asersi memuat state server: item N-03 tetap Unread dan badge tetap `5`).
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread, badge `5`; N-03 `Asset has been repaired` view-only Unread). Spec tidak mengubah status baca N-03 karena seluruh aksi Mark as Read digagalkan; fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after`.
- Kemampuan teknis: intercept respons HTTP pada browser (`Spectra.intercept()`, butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`) untuk memaksa respons Mark as Read berstatus 500, timeout tanpa respons, dan 403; intercept dilepas segera setelah pemicu selesai (S-09). Endpoint tidak dikarang (S-13).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-03 (Pre-setup #17) yang menjadi target `[Mark as Read]` yang digagalkan intercept, status baca tidak diubah milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-76: Mark as Read gagal 5xx menampilkan toast T-FANOTIF-01

1. Klik Bell icon
2. Paksa respons Mark as Read gagal 500 lewat intercept
3. Klik `[Mark as Read]` pada item N-03
4. Verifikasi muncul toast error `"Error, failed to mark notification as read."`
5. Verifikasi item N-03 tetap Unread dengan tombol `[Mark as Read]`
6. Verifikasi badge Bell icon tetap `5`
7. Lepas intercept, tunggu toast hilang otomatis, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-77: Mark as Read timeout jaringan menampilkan toast koneksi

8. Klik Bell icon
9. Paksa Mark as Read timeout lewat intercept tanpa respons
10. Klik `[Mark as Read]` pada item N-03
11. Verifikasi muncul toast error `"Connection problem. Please try again."`
12. Verifikasi toast error tanpa tombol
13. Verifikasi item N-03 tetap Unread
14. Verifikasi badge Bell icon tetap `5`
15. Lepas intercept, tunggu toast hilang otomatis, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-354: Respons 403 pada Mark as Read ditolak dengan toast T-FANOTIF-02

16. Klik Bell icon
17. Paksa respons Mark as Read 403 untuk N-03 lewat intercept
18. Klik `[Mark as Read]` pada item N-03
19. Verifikasi muncul toast error `"You don't have permission to do this."`
20. Verifikasi item N-03 tetap Unread
21. Lepas intercept, tunggu toast hilang otomatis, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-379: Mark as Read gagal 5xx di Notification Center menampilkan toast T-FANOTIF-01

22. Klik Bell icon lalu klik `[Show All]` untuk membuka Notification Center
23. Paksa respons Mark as Read gagal 500 lewat intercept
24. Klik `[Mark as Read]` pada item N-03
25. Verifikasi muncul toast error `"Error, failed to mark notification as read."`
26. Verifikasi item N-03 tetap Unread dengan tombol `[Mark as Read]`
27. Verifikasi badge Bell icon tetap `5`
28. Lepas intercept

## Notes

- Langkah penghubung (S-03): langkah 7, 15, dan 21 (melepas intercept, menunggu toast lama hilang, dan memuat ulang halaman antar TC, S-09 dan R-12); langkah 28 (melepas intercept di akhir spec); langkah 22 (jalur Notification Center lewat Bell icon dan `[Show All]`, karena TC hanya menulis "Buka Notification Center").
- Pada TC-FA-NOTIF-76 dan 379 klausa Expected "Item N-03 tetap Unread dengan tombol `[Mark as Read]`, badge tetap `5`" dipecah per klausa (item Unread dengan tombol, badge). Tidak ada asersi absence yang butuh anchor selain status Unread yang diamati langsung pada item yang sama.
- Temuan untuk QA:
  - TC-FA-NOTIF-354: judul "Akses notifikasi user lain lewat UI ditolak" berbeda dari langkahnya, yang memaksa respons Mark as Read 403 lewat intercept (kelas b) tanpa user lain yang sebenarnya; spec mengikuti langkah TC. Intercept tidak membuktikan penolakan kepemilikan oleh server (dicakup spec 100, TC-FA-NOTIF-353).
  - TC-FA-NOTIF-354: Expected tidak menulis badge; tidak diasersi.
  - TC-FA-NOTIF-76, 77, 354, dan 379: Post Condition kosong (`-`); tidak ada asersi tambahan.
  - TC-FA-NOTIF-77: tidak menyebut durasi timeout yang dipicu; spec menahan respons tanpa membalas lewat intercept.
