---
id: TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar
title: "Mark as Read: Dropdown Panel dan Notification Center Dasar"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-74
  - TC-FA-NOTIF-75
  - TC-FA-NOTIF-78
  - TC-FA-NOTIF-80
coverage:
  web: automated
---

# Mark as Read: Dropdown Panel dan Notification Center Dasar

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5` (N-01 sampai N-05 Unread).
- Spec mengubah status baca N-03; fixture BE pemulih seed notifikasi Pre-setup #17 sampai #24 (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC.
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): seed notifikasi Pre-setup #17 (N-03) menjadi target aksi Mark as Read dengan nama literal tanpa suffix karena notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-74: Mark as Read notifikasi view-only dari Dropdown Panel

1. Klik Bell icon
2. Catat nilai badge Bell icon (baseline, `5`)
3. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
4. Verifikasi Title item N-03 tidak bold
5. Verifikasi dot Unread pada item N-03 hilang
6. Verifikasi tombol `[Mark as Read]` pada item N-03 hilang total (bukan disabled)
7. Verifikasi badge Bell icon berkurang 1 dari baseline langkah 2 menjadi `4`
8. Verifikasi muncul toast sukses `Success, notification has been marked as read.`
9. Verifikasi tidak ada dialog konfirmasi

### TC-FA-NOTIF-75: Mark as Read notifikasi view-only dari Notification Center

10. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman
11. Klik Bell icon
12. Klik `[Show All]`
13. Catat nilai badge Bell icon (baseline, `5`)
14. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
15. Verifikasi Title item N-03 tidak bold
16. Verifikasi dot Unread pada item N-03 hilang
17. Verifikasi tombol `[Mark as Read]` pada item N-03 hilang total (bukan disabled)
18. Verifikasi badge Bell icon berkurang 1 dari baseline langkah 13 menjadi `4`
19. Verifikasi muncul toast sukses `Success, notification has been marked as read.`
20. Verifikasi tidak ada dialog konfirmasi

### TC-FA-NOTIF-78: Mark as Read klik ganda cepat bersifat idempotent

21. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
22. Klik Bell icon
23. Catat nilai badge Bell icon (baseline, `5`)
24. Klik dua kali cepat `[Mark as Read]` pada item N-03
25. Verifikasi item N-03 berstatus Read
26. Verifikasi badge Bell icon berkurang tepat 1 dari baseline langkah 23 menjadi `4`
27. Verifikasi muncul toast sukses `Success, notification has been marked as read.`
28. Verifikasi tidak ada toast error

### TC-FA-NOTIF-80: Mark as Read tidak tersedia untuk notifikasi actionable Unread

29. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
30. Klik Bell icon
31. Verifikasi tombol `[Detail]` pada item N-01 (actionable Unread) tampil
32. Verifikasi tidak ada tombol `[Mark as Read]` pada item N-01

## Notes

- Langkah penghubung (S-03): langkah 2, 13, dan 23 (baseline badge sebelum aksi, S-12); langkah 10, 21, dan 29 (pemulihan seed antar TC); langkah 11 dan 12 (membuka Notification Center lewat Bell icon dan `[Show All]` karena TC tidak menyebut jalur lain).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 9 dan 20 didahului langkah 8 dan 19 (toast sukses tampil); langkah 28 didahului langkah 27; langkah 32 didahului langkah 31.
- Pada klik ganda (langkah 24) yang diasersi hanya toast sukses dan tidak adanya toast error (klien tidak membedakan No-Op, sesuai TC).
- Topik Mark as Read dipisah menjadi tiga spec (020 tombol `[Mark as Read]` di Dropdown Panel dan Notification Center, 021 klik area item, Tab Unread, dan severity, 111 tanpa pre-check dan klik area item di Notification Center) walau berbagi seed Pre-setup #17 dan N-03, karena tiap spec memulihkan seed atau menukar varian seed antar TC dan gabungannya melampaui ~35 langkah.
- Temuan untuk QA:
  - Post Condition TC-FA-NOTIF-74 dan 75 menulis N-03 Read di Dropdown Panel dan Notification Center tanpa langkah observasi di kedua surface; hanya surface tempat aksi dijalankan yang diasersi.
  - TC-FA-NOTIF-78 menulis status permintaan kedua `200 OK` No-Op yang tidak teramati dari UI; tidak diasersi.
  - Post Condition TC-FA-NOTIF-80 kosong (`-`).
