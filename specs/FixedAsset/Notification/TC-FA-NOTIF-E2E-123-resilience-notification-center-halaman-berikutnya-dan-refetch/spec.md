---
id: TC-FA-NOTIF-E2E-123-resilience-notification-center-halaman-berikutnya-dan-refetch
title: "Resilience Notification Center: Gagal Memuat Halaman Berikutnya dan Gagal Refetch Tab"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-222
  - TC-FA-NOTIF-223
coverage:
  web: automated
---

# Resilience Notification Center: Gagal Memuat Halaman Berikutnya dan Gagal Refetch Tab

## Prerequisites

- Mode: FE+BE (kegagalan dipaksa lewat `Spectra.intercept()` di atas backend nyata; asersi memuat state server: halaman berikutnya dan list Tab Unread dimuat setelah intercept dilepas).
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup: varian notifikasi N-01 sampai N-37 (Pre-setup #17 dan #18; lebih dari 10 item sehingga ada halaman berikutnya, ukuran halaman awal 10 item, dan sedikitnya satu notifikasi Unread). Varian ditukar oleh fixture BE penukar (butir "Fixture BE penukar varian seed #18" di `suite.md`) pada langkah 1; fixture BE pemulih seed (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after`. Spec tidak mengubah status baca notifikasi.
- Kemampuan teknis: intercept respons HTTP pada browser (`Spectra.intercept()`, butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`) untuk memaksa respons halaman berikutnya dan respons list berstatus 500 serta menghitung permintaan halaman pertama; intercept dilepas segera setelah pemicu selesai (S-09). Endpoint tidak dikarang (S-13).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-222: Gagal memuat halaman berikutnya, item termuat tetap dan Try Again mengulang hanya halaman gagal

1. Tukar seed notifikasi ke varian N-01 sampai N-37 (Pre-setup #17 dan #18) lewat fixture BE penukar, lalu muat ulang halaman Fixed Asset > Dashboard
2. Buka Notification Center (klik Bell icon lalu klik `[Show All]`), lalu catat jumlah permintaan halaman pertama pada intercept (baseline)
3. Paksa respons halaman berikutnya gagal 500 lewat intercept
4. Scroll mendekati akhir list
5. Verifikasi 10 item awal tetap tampil
6. Verifikasi state Error S-06 muncul inline di akhir list
7. Verifikasi muncul toast error `"Unable to load notifications."`
8. Lepas intercept respons halaman berikutnya, lalu klik `[Try Again]`
9. Verifikasi halaman berikutnya termuat
10. Verifikasi permintaan halaman pertama tidak diulang (jumlah permintaan halaman pertama sama dengan baseline langkah 2)

### TC-FA-NOTIF-223: Gagal fetch ulang karena perubahan Tab, S-06 menggantikan list

11. Tunggu toast lama hilang otomatis, lalu muat ulang halaman Fixed Asset > Dashboard
12. Buka Notification Center (klik Bell icon lalu klik `[Show All]`)
13. Paksa respons list gagal 500 lewat intercept
14. Klik Tab `Unread`
15. Verifikasi state Error S-06 `"Unable to load this data."` menggantikan list
16. Verifikasi tombol `[Try Again]` tampil pada state Error
17. Lepas intercept respons list, lalu klik `[Try Again]`
18. Verifikasi Tab `Unread` aktif
19. Verifikasi list notifikasi Unread diambil ulang dan tampil dari awal
20. Verifikasi state Error hilang

## Notes

- Langkah penghubung (S-03): langkah 2 dan 12 (jalur Notification Center lewat Bell icon dan `[Show All]`, karena TC hanya menulis "Buka Notification Center"; langkah 2 juga mencatat baseline permintaan, S-12); langkah 3 dan 13 (pemicu kegagalan lewat intercept); langkah 8 dan 17 (melepas intercept sesuai langkah TC "Hapus intercept"); langkah 11 (menunggu toast lama hilang otomatis dan memuat ulang halaman antar TC, S-09 dan R-12).
- Langkah 10 menerjemahkan klausa "tanpa mengulang halaman pertama" menjadi hitungan permintaan halaman pertama pada intercept, karena TC tidak menyebut cara pengamatannya (S-15, lihat Temuan untuk QA).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 20 didahului langkah 18 dan 19 (Tab Unread aktif dan list tampil); langkah 5 sendiri adalah asersi kehadiran 10 item.
- Pembagian TC lintas spec: TC kelas resilience Notification Center lain (list awal gagal, Try Again, pre-check Detail) ada di spec 104.
- Temuan untuk QA:
  - TC-FA-NOTIF-222: "tanpa mengulang halaman pertama" tidak teramati dari UI; spec menghitung permintaan halaman pertama lewat intercept (kemampuan tim FE/BE).
  - TC-FA-NOTIF-222 dan 223: Post Condition kosong (`-`); tidak ada asersi tambahan.
  - TC-FA-NOTIF-223: "fetch diulang dari awal dengan Tab Unread aktif" tidak menyebut item konkret; spec mengasersi Tab Unread aktif dan list Unread tampil dari awal tanpa menyebut identitas item. Judul TC menyebut Filter, Sort, dan Search tetapi langkahnya hanya Tab Unread.
