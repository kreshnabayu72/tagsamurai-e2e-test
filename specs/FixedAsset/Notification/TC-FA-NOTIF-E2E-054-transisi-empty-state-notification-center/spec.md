---
id: TC-FA-NOTIF-E2E-054-transisi-empty-state-notification-center
title: "Transisi Empty State Notification Center: Tab Unread Kosong dan Notifikasi Pertama via SSE"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-382
  - TC-FA-NOTIF-383
coverage:
  web: automated
---

# Transisi Empty State Notification Center: Tab Unread Kosong dan Notifikasi Pertama via SSE

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center.
- Akun aktor pertama: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun aktor kedua (TC-383, ganti akun eksplisit pada langkah 11): Borrower Pre-setup #29 (`borrowerKosong_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_BORROWERKOSONG_PASSWORD`; nama env usulan, belum terdaftar). Akun ini Borrower client utama tanpa tier atau Transaction Role, tanpa notifikasi, flag Guided Tooltip `fa-notification` true; tidak dipakai TC lain yang memicu event ke akun ini.
- Pelaku kedua TC-383: Asset Admin Pre-setup #8 (`assetAdmin_automated_{namaCompany}@qwertysystem.net`, PIC admin transaksi; password `Spectra.env.FA_ASSETADMIN_PASSWORD`; nama env usulan, belum terdaftar) memakai sesi API aktor (suite.md), bukan sesi UI.
- Data TC-382: seed varian tepat satu notifikasi Unread view-only (Pre-setup #18, varian satu Unread) untuk akun #1, ditukar fixture BE penukar sebagai langkah penghubung; seed dipulihkan fixture BE pemulih di hook `before` dan `after`.
- Data TC-383: transaksi Borrow Ready for Handover milik akun #29 (1 aset di Gedung A > Lantai 1 > Ruang 101, setara Pre-setup #19) di-seed langsung lewat fixture BE tanpa memicu `borrow_confirmation_required`, sehingga akun #29 tanpa notifikasi; dipulihkan fixture BE pemulih di hook `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed varian satu Unread (Pre-setup #18) yang menjadi target `[Mark as Read]` dan transaksi Borrow seed akun Pre-setup #29 (setara Pre-setup #19) yang handover-nya dipicu milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (akun #1 dan #29 sudah true), fixture BE pemulih dan penukar seed notifikasi, serta fixture BE pemicu event.

## Test Steps

### TC-FA-NOTIF-382: Tab Unread: Mark as Read pada satu-satunya item Unread menampilkan empty state S-02 dan badge hilang

1. Pulihkan seed notifikasi lewat fixture BE pemulih, tukar ke varian tepat satu Unread view-only lewat fixture BE penukar, lalu muat ulang halaman
2. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
3. Klik Tab `Unread`
4. Verifikasi list memuat satu item
5. Klik `[Mark as Read]` pada satu-satunya item
6. Verifikasi item hilang dari Tab Unread seketika tanpa memuat ulang halaman
7. Verifikasi empty state tampil dengan Illustration, Title `No unread notifications`, dan Description `You're all caught up! Unread notifications will appear here.`
8. Verifikasi badge Bell icon tidak tampil (hidden)
9. Pulihkan seed notifikasi lewat fixture BE pemulih

### TC-FA-NOTIF-383: Notifikasi baru via SSE menggantikan empty state S-01 di Notification Center

10. Tunggu aksi selesai (pemulihan seed pada langkah 9 tersimpan)
11. Logout dari akun Total Control Pre-setup #1, lalu login sebagai Borrower Pre-setup #29
12. Buka Fixed Asset > Dashboard, klik Bell icon, lalu klik `[Show All]`
13. Verifikasi empty state S-01 tampil di Notification Center
14. Lewat sesi API Asset Admin Pre-setup #8, selesaikan handover transaksi Borrow akun Pre-setup #29 hingga handover tersimpan
15. Verifikasi empty state S-01 hilang tanpa memuat ulang halaman
16. Verifikasi item `Asset handover completed` tampil di list
17. Verifikasi badge Bell icon menampilkan `1`

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini memuat ganti akun eksplisit (langkah 11) dengan alasan: TC-382 memakai akun Total Control #1 dan TC-383 memakai Borrower #29 yang harus tanpa notifikasi; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Akun #1 memulihkan sesi di hook `after`.
- Langkah penghubung (S-03): langkah 1 (penukaran varian seed dan precondition), 2 (precondition TC-382), 9 (pemulihan seed), 10 (menunggu aksi selesai sebelum ganti akun, 8b butir 8), 12 (membuka layar secara eksplisit sesudah ganti akun, S-07, dan precondition d TC-383).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 (anchor satu item sebelum asersi item hilang, 8b butir 2), langkah 13 (anchor empty state S-01 sebelum asersi empty state hilang; precondition d TC-383).
- Temuan untuk QA:
  - TC-383 tidak menulis teks empty state S-01 (Illustration, Title, Description) pada Expected maupun precondition; spec hanya menulis "empty state S-01" tanpa teks.
  - TC-383 langkah 1 menyebut "dari akun Asset Admin (Pre-setup #8)" tanpa menyebut sesi; spec memakai sesi API Asset Admin dan tidak membuka sesi UI kedua.
  - Pre-setup #29 menyebut akun tidak boleh dipakai TC lain yang memicu event ke akun ini; spec memulihkan transaksi seed di hook `after`.
