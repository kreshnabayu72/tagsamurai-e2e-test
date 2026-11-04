---
id: TC-FA-NOTIF-E2E-003-variasi-data-badge-99-body-panjang-dan-tab-unread-kosong
title: "Variasi Data Seed: Badge 99 dan 99+, Body Panjang, dan Empty State Tab Unread"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-3
  - TC-FA-NOTIF-11
  - TC-FA-NOTIF-25
coverage:
  web: automated
---

# Variasi Data Seed: Badge 99 dan 99+, Body Panjang, dan Empty State Tab Unread

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel, Notification Center).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: tiap TC memakai varian seed notifikasi Pre-setup #18 sendiri pada akun aktor, ditukar fixture BE penukar varian seed lewat langkah penghubung eksplisit:
  - TC-3: tepat 99 Unread; satu notifikasi Unread tambahan di-seed lewat fixture BE sehingga total 100 Unread;
  - TC-11: `borrow_resolved` varian Rejected dengan Rejection Reason 120 karakter (N-38) sebagai item teratas;
  - TC-25: semua notifikasi berstatus Read.
- Fixture BE pemulih seed dijalankan di hook `before` dan `after`. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah yang menukar dan menambah seed notifikasi varian Pre-setup #18 (N-38, varian tepat 99 Unread, dan varian semua Read) pada akun aktor milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Hook suite yang berlaku (rujukan ke `suite.md`): flag Guided Tooltip (akun #1 sudah true), fixture BE pemulih dan penukar seed notifikasi.

## Test Steps

### TC-FA-NOTIF-3: Badge Bell icon batas 99 dan lebih dari 99

1. Tukar seed ke varian tepat 99 Unread lewat fixture BE penukar, lalu muat ulang halaman
2. Verifikasi badge Bell icon menampilkan angka `99`
3. Lewat fixture BE, seed satu notifikasi Unread tambahan sehingga total 100 Unread hingga notifikasi tersimpan
4. Verifikasi badge Bell icon menampilkan `99+`

### TC-FA-NOTIF-11: Body notifikasi panjang wrap multi-baris

5. Tukar seed ke varian dengan N-38 (Rejection Reason 120 karakter) sebagai item teratas lewat fixture BE penukar, lalu muat ulang halaman
6. Klik Bell icon
7. Verifikasi Body item teratas ditampilkan penuh dalam beberapa baris tanpa terpotong
8. Verifikasi tinggi item teratas menyesuaikan Body

### TC-FA-NOTIF-25: Empty state Tab Unread saat semua sudah dibaca

9. Klik Bell icon untuk menutup Dropdown Panel, tukar seed ke varian semua Read lewat fixture BE penukar, lalu muat ulang halaman
10. Klik Bell icon, lalu klik `[Show All]` untuk membuka Notification Center
11. Klik Tab `Unread`
12. Verifikasi Illustration tampil
13. Verifikasi Title `No unread notifications`
14. Verifikasi Description `You're all caught up! Unread notifications will appear here.`
15. Verifikasi badge Bell icon tidak tampil (hidden) walau akun punya notifikasi Read

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 5, 9 (tukar seed dan muat ulang halaman), langkah 6 (buka panel), langkah 10 (buka Notification Center; TC-25 menulis "Buka Notification Center").
- Langkah 3 memicu pertambahan notifikasi lewat fixture BE sebagai bagian Langkah TC-3 (Langkah 2: "Seed satu notifikasi Unread tambahan").
- Temuan untuk QA:
  - TC-3 tidak menyebut apakah halaman dimuat ulang sesudah seed tambahan; spec tidak memuat ulang sehingga perubahan badge teramati lewat SSE.
  - TC-11 menyebut satu notifikasi N-38 sebagai "item teratas" tanpa menyebut varian seed yang menempatkannya di urutan teratas; spec memakai varian "N-38 sebagai item teratas" dari Pre-setup #18.
