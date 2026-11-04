---
id: TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity
title: "Mark as Read: Klik Area Item, Tab Unread, dan Severity Item"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-81
  - TC-FA-NOTIF-82
  - TC-FA-NOTIF-83
  - TC-FA-NOTIF-84
coverage:
  web: automated
---

# Mark as Read: Klik Area Item, Tab Unread, dan Severity Item

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`. TC-FA-NOTIF-82 memakai varian seed Pre-setup #17 dan #18 dengan N-06 dan N-07 (Read) menempati urutan teratas Dropdown Panel.
- Fixture BE pemulih seed notifikasi Pre-setup #17 sampai #24 dan fixture BE penukar varian seed #18 (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE penukar varian seed #18" di `suite.md`) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum tiap TC. Spec mengubah status baca N-03 (TC-FA-NOTIF-83 dan 84).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): seed notifikasi Pre-setup #17 (N-03) menjadi target aksi Mark as Read dengan nama literal tanpa suffix karena notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-81: Klik area item view-only tidak mengubah status baca dan menavigasi ke Klik -> Path

1. Klik Bell icon
2. Catat nilai badge Bell icon (baseline, `5`)
3. Klik judul item N-05 (`Your Total Control access was removed`, bukan tombol)
4. Verifikasi browser berpindah ke `/fams/profile`
5. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
6. Klik Bell icon
7. Verifikasi item N-05 tetap Unread
8. Verifikasi item N-05 tetap memiliki tombol `[Mark as Read]`
9. Verifikasi badge Bell icon sama dengan baseline langkah 2

### TC-FA-NOTIF-82: Klik area item view-only yang sudah Read tetap menavigasi

10. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, tukar ke varian dua notifikasi terbaru Read (N-06 dan N-07 teratas) lewat fixture BE penukar, lalu muat ulang halaman Fixed Asset > Dashboard
11. Klik Bell icon
12. Klik body item N-06 (`Your request has been rejected`, Read)
13. Verifikasi browser berpindah ke `/fams/borrow/BRW-2026-0341`
14. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
15. Klik Bell icon
16. Verifikasi item N-06 tetap Read
17. Verifikasi item N-06 tidak memiliki tombol

### TC-FA-NOTIF-83: Mark as Read di Tab Unread menghilangkan item secara real-time

18. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
19. Klik Bell icon
20. Klik `[Show All]`
21. Klik Tab `Unread`
22. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
23. Verifikasi item N-01 tampil pada Tab Unread (anchor: daftar Tab Unread termuat)
24. Verifikasi item N-03 hilang dari Tab Unread seketika tanpa memuat ulang halaman
25. Klik Tab `All`
26. Verifikasi item N-03 tampil sebagai Read pada Tab All

### TC-FA-NOTIF-84: Mark as Read tidak mengubah icon dan severity item

27. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
28. Klik Bell icon
29. Catat icon item N-03 (`checkbox-circle-line`, severity `success`)
30. Klik `[Mark as Read]` pada item N-03
31. Verifikasi icon `checkbox-circle-line` severity `success` pada item N-03 sama dengan yang dicatat pada langkah 29

## Notes

- Langkah penghubung (S-03): langkah 2 (baseline badge sebelum aksi, S-12); langkah 5 dan 14 (kembali dari halaman tujuan); langkah 10, 18, dan 27 (pemulihan seed dan penukaran varian antar TC); langkah 19 dan 20 (membuka Notification Center lewat Bell icon dan `[Show All]` karena TC tidak menyebut jalur lain); langkah 25 (berpindah Tab untuk membaca N-03 di Tab All, sesuai Expected b TC-FA-NOTIF-83); langkah 29 (mencatat icon sebelum aksi, sesuai TC).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 24 didahului langkah 23 (item lain pada Tab Unread tampil, daftar termuat); langkah 17 didahului langkah 16 (item N-06 tampil).
- Asersi tambahan (S-03): langkah 7 dan 8 memecah "tetap Unread dengan tombol `[Mark as Read]`" menjadi dua klausa (S-01); langkah 16 dan 17 memecah "tetap Read tanpa tombol".
- Topik Mark as Read dipisah menjadi tiga spec (020 tombol `[Mark as Read]` di Dropdown Panel dan Notification Center, 021 klik area item, Tab Unread, dan severity, 111 tanpa pre-check dan klik area item di Notification Center) walau berbagi seed Pre-setup #17 dan N-03, karena tiap spec memulihkan seed atau menukar varian seed antar TC dan gabungannya melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-82 memakai seed N-06 dan N-07 sebagai notifikasi teratas (varian Pre-setup #18), tetapi Expected b "item N-06 tetap Read tanpa tombol" tidak menyebut apakah diamati setelah kembali; spec mengamatinya setelah kembali ke Dashboard (langkah 14 sampai 17), mengikuti pola TC-FA-NOTIF-81.
  - Post Condition TC-FA-NOTIF-83 ("N-03 berstatus Read di Tab All dan hilang dari Tab Unread") sudah punya padanan Expected; Post Condition TC-FA-NOTIF-81, 82, dan 84 kosong (`-`).
