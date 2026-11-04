---
id: TC-FA-NOTIF-E2E-104-resilience-notification-center-gagal-fetch-list-awal-dan-pre-check
title: "Resilience Notification Center: Gagal Fetch List Awal, Try Again, dan Gagal Pre-check Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-27
  - TC-FA-NOTIF-28
  - TC-FA-NOTIF-380
coverage:
  web: automated
---

# Resilience Notification Center: Gagal Fetch List Awal, Try Again, dan Gagal Pre-check Detail

## Prerequisites

- Mode: FE+BE (kegagalan dipaksa lewat `Spectra.intercept()` di atas backend nyata; asersi memuat state server: list N-01 sampai N-07 dimuat ulang, N-01 tetap Unread, navigasi berhasil setelah intercept dilepas).
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable). Spec tidak mengubah status baca notifikasi; fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after`.
- Kemampuan teknis: intercept respons HTTP pada browser (`Spectra.intercept()`, butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`) untuk memaksa respons list notifikasi dan respons pre-check `[Detail]` berstatus 500; intercept dilepas segera setelah pemicu selesai (S-09). Endpoint tidak dikarang (S-13).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-01 (Pre-setup #17) yang menjadi target `[Detail]` (pre-check digagalkan lalu dibiarkan berhasil), status baca tidak diubah milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-27: Notification Center, state Error saat fetch list awal gagal

1. Paksa respons list notifikasi gagal 500 lewat intercept
2. Buka Notification Center (klik Bell icon lalu klik `[Show All]`)
3. Verifikasi muncul toast error `"Unable to load notifications."`
4. Verifikasi toast error tampil sekali
5. Verifikasi toast error tanpa tombol
6. Verifikasi state Error `"Unable to load this data."` menggantikan list
7. Verifikasi tombol `[Try Again]` tampil pada state Error
8. Verifikasi tidak tampil empty state
9. Lepas intercept respons list, tunggu toast hilang otomatis, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-28: Notification Center, `[Try Again]` memuat ulang list dari awal

10. Paksa respons list notifikasi gagal 500 lewat intercept
11. Buka Notification Center (klik Bell icon lalu klik `[Show All]`)
12. Lepas intercept respons list, lalu klik `[Try Again]`
13. Verifikasi list item N-01 sampai N-07 tampil dari awal
14. Verifikasi state Error hilang
15. Muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-380: Pre-check `[Detail]` gagal di-fetch di Notification Center membatalkan navigasi

16. Buka Notification Center (klik Bell icon lalu klik `[Show All]`)
17. Paksa respons pre-check gagal 500 lewat intercept
18. Klik `[Detail]` pada item N-01
19. Verifikasi navigasi dibatalkan (halaman tetap Notification Center)
20. Verifikasi list Notification Center tetap tampil
21. Verifikasi item N-01 tetap Unread
22. Verifikasi muncul toast error `"Unable to load this data."`
23. Verifikasi toast error tanpa tombol
24. Verifikasi state Error S-06 tidak menggantikan list (list item N-01 sampai N-07 tetap tampil)
25. Lepas intercept respons pre-check, lalu klik `[Detail]` pada item N-01 lagi
26. Verifikasi navigasi berjalan ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`

## Notes

- Langkah penghubung (S-03): langkah 9 dan 15 (melepas intercept, menunggu toast lama hilang, dan memuat ulang halaman antar TC, S-09 dan R-12); langkah 12 dan 25 (melepas intercept sesuai langkah TC "Hapus intercept"); langkah 2, 11, dan 16 (jalur Notification Center lewat Bell icon dan `[Show All]`, karena TC hanya menulis "Buka Notification Center"); langkah 1, 10, dan 17 (pemicu kegagalan lewat intercept).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 8 didahului langkah 6 dan 7 (state Error tampil pada area yang sama); langkah 14 didahului langkah 13 (list tampil); langkah 24 menjadi asersi list tampil sebagai anchor bagi klausa "state Error S-06 tidak menggantikan list".
- TC dengan fetch halaman berikutnya (TC-FA-NOTIF-222) dan refetch karena Tab/Filter/Sort/Search (TC-FA-NOTIF-223) ada di spec 123.
- Temuan untuk QA:
  - TC-FA-NOTIF-27, 28, dan 380: Post Condition kosong (`-`); tidak ada asersi tambahan.
  - TC-FA-NOTIF-27: tidak menyebut apakah toast `"Unable to load notifications."` hilang otomatis; spec tidak mengasersi durasi toast.
  - TC-FA-NOTIF-380: "state Error S-06 tidak menggantikan list" ditulis tanpa elemen konkret; spec mengasersi list item N-01 sampai N-07 tetap tampil.
