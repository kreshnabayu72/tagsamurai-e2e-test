---
id: TC-FA-NOTIF-E2E-103-resilience-dropdown-panel-gagal-fetch-dan-pre-check
title: "Resilience Dropdown Panel: Gagal Fetch Snapshot, Try Again, dan Gagal Pre-check Detail"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-18
  - TC-FA-NOTIF-19
  - TC-FA-NOTIF-106
coverage:
  web: automated
---

# Resilience Dropdown Panel: Gagal Fetch Snapshot, Try Again, dan Gagal Pre-check Detail

## Prerequisites

- Mode: FE+BE (kegagalan dipaksa lewat `Spectra.intercept()` di atas backend nyata; asersi memuat state server: item N-01 tetap Unread dan navigasi berhasil setelah intercept dilepas).
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread dan tampil pada Dropdown Panel, N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable). Spec tidak mengubah status baca notifikasi; fixture BE pemulih seed notifikasi dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after`.
- Kemampuan teknis: intercept respons HTTP pada browser (`Spectra.intercept()`, butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`) untuk memaksa respons snapshot notifikasi dan respons pre-check `[Detail]` berstatus 500; intercept dilepas segera setelah pemicu selesai (S-09). Endpoint tidak dikarang (S-13).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-01 (Pre-setup #17) yang menjadi target `[Detail]` (pre-check digagalkan lalu dibiarkan berhasil), status baca tidak diubah milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-18: Dropdown Panel, state Error saat fetch snapshot gagal

1. Paksa respons snapshot notifikasi gagal 500 lewat intercept
2. Klik Bell icon
3. Verifikasi muncul toast error `"Unable to load notifications."`
4. Verifikasi toast error tampil sekali
5. Verifikasi toast error tanpa tombol
6. Verifikasi area list Dropdown Panel menampilkan state Error `"Unable to load this data."` dengan tombol `[Try Again]`
7. Verifikasi tidak tampil empty state
8. Lepas intercept respons snapshot, tutup Dropdown Panel, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-19: Dropdown Panel, `[Try Again]` memuat ulang dan menampilkan list

9. Paksa respons snapshot notifikasi gagal 500 lewat intercept
10. Klik Bell icon
11. Lepas intercept respons snapshot, lalu klik `[Try Again]`
12. Verifikasi list item N-01 sampai N-05 tampil pada Dropdown Panel
13. Verifikasi state Error hilang
14. Tutup Dropdown Panel, lalu muat ulang halaman Fixed Asset > Dashboard

### TC-FA-NOTIF-106: Pre-check `[Detail]` gagal di-fetch membatalkan navigasi dengan toast tanpa tombol

15. Klik Bell icon
16. Paksa respons pre-check gagal 500 lewat intercept
17. Klik `[Detail]` pada item N-01
18. Verifikasi navigasi dibatalkan (halaman tetap Fixed Asset > Dashboard)
19. Verifikasi Dropdown Panel tetap tampil
20. Verifikasi item N-01 tetap Unread
21. Verifikasi muncul toast error `"Unable to load this data."`
22. Verifikasi toast error tanpa tombol
23. Verifikasi state Error S-06 tidak menggantikan list (list item N-01 sampai N-05 tetap tampil)
24. Lepas intercept respons pre-check, lalu klik `[Detail]` pada item N-01 lagi
25. Verifikasi pre-check berhasil dan navigasi berjalan ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`

## Notes

- Langkah penghubung (S-03): langkah 8 dan 14 (melepas intercept, menutup panel, dan memuat ulang halaman antar TC, S-09); langkah 11 dan 24 (melepas intercept sesuai langkah TC "Hapus intercept"); langkah 1, 9, dan 16 (pemicu kegagalan lewat intercept, bukan objek asersi navigasi).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 7 didahului langkah 6 (state Error tampil pada area list yang sama); langkah 13 didahului langkah 12 (list tampil); langkah 23 menjadi asersi list tampil sebagai anchor bagi klausa "state Error S-06 tidak menggantikan list".
- TC-FA-NOTIF-18 dan 19 memakai intercept untuk memaksa respons gagal; menahan respons hanya untuk mengamati Loading tidak dipakai di spec ini.
- Temuan untuk QA:
  - TC-FA-NOTIF-18, 19, dan 106: Post Condition kosong (`-`); tidak ada asersi tambahan.
  - TC-FA-NOTIF-18: tidak menyebut apakah toast `"Unable to load notifications."` hilang otomatis; spec tidak mengasersi durasi toast.
  - TC-FA-NOTIF-106: "state Error S-06 tidak menggantikan list" ditulis tanpa elemen konkret; spec mengasersi list item N-01 sampai N-05 tetap tampil.
