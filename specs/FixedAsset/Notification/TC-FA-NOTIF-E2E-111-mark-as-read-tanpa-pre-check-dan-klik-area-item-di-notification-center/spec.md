---
id: TC-FA-NOTIF-E2E-111-mark-as-read-tanpa-pre-check-dan-klik-area-item-di-notification-center
title: "Mark as Read Tanpa Pre-check dan Klik Area Item View-Only di Notification Center"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-109
  - TC-FA-NOTIF-390
  - TC-FA-NOTIF-391
coverage:
  web: automated
---

# Mark as Read Tanpa Pre-check dan Klik Area Item View-Only di Notification Center

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`.
- Fixture BE pemulih seed notifikasi Pre-setup #17 sampai #24 (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum TC-FA-NOTIF-109 (spec mengubah status baca N-03).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): seed notifikasi Pre-setup #17 (N-03) menjadi target aksi Mark as Read dengan nama literal tanpa suffix karena notifikasi seed hanya ada untuk akun Pre-setup. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-390: Notification Center, klik area item view-only Unread menavigasi ke Klik -> Path

1. Klik Bell icon
2. Klik `[Show All]`
3. Klik judul item N-05 (`Your Total Control access was removed`, bukan tombol)
4. Verifikasi browser berpindah ke `/fams/profile`
5. Kembali ke Notification Center (navigasi balik browser)
6. Verifikasi item N-05 tetap Unread
7. Verifikasi item N-05 tetap memiliki tombol `[Mark as Read]`
8. Verifikasi badge Bell icon tetap `5`

### TC-FA-NOTIF-391: Notification Center, klik area item view-only yang sudah Read tetap menavigasi

9. Klik body item N-06 (`Your request has been rejected`)
10. Verifikasi browser berpindah ke `/fams/borrow/BRW-2026-0341`
11. Kembali ke Notification Center (navigasi balik browser)
12. Verifikasi item N-06 tetap Read
13. Verifikasi item N-06 tidak memiliki tombol
14. Verifikasi badge Bell icon tetap `5`

### TC-FA-NOTIF-109: Klik Mark as Read pada view-only tidak menjalankan pre-check Detail

15. Pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard
16. Klik Bell icon
17. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
18. Verifikasi item N-03 berstatus Read
19. Verifikasi tidak ada navigasi (halaman tetap Fixed Asset > Dashboard)
20. Verifikasi tidak ada dialog D-01

## Notes

- Urutan TC dalam spec: TC-FA-NOTIF-390 dan 391 dijalankan pada seed awal tanpa mengubah status baca (satu pembukaan Notification Center), lalu TC-FA-NOTIF-109 yang mengubah status baca N-03 dijalankan terakhir (S-10).
- Langkah penghubung (S-03): langkah 1 dan 2 (membuka Notification Center lewat Bell icon dan `[Show All]` karena TC tidak menyebut jalur lain); langkah 5 dan 11 (kembali ke Notification Center); langkah 15 (pemulihan seed sebelum TC yang mengubah state).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 13 didahului langkah 12 (item N-06 tampil); langkah 19 dan 20 didahului langkah 18 (item N-03 menjadi Read, bukti aksi diproses tanpa dialog).
- Asersi tambahan (S-03): langkah 6 dan 7 serta 12 dan 13 memecah klausa "tetap Unread dengan tombol" dan "tetap Read tanpa tombol" (S-01).
- Topik Mark as Read dipisah menjadi tiga spec (020 tombol `[Mark as Read]` di Dropdown Panel dan Notification Center, 021 klik area item, Tab Unread, dan severity, 111 tanpa pre-check dan klik area item di Notification Center) walau berbagi seed Pre-setup #17 dan N-03, karena tiap spec memulihkan seed atau menukar varian seed antar TC dan gabungannya melampaui ~35 langkah.
- Temuan untuk QA:
  - TC-FA-NOTIF-109 menulis "tidak menjalankan pre-check Detail" sebagai Expected "tidak ada navigasi dan tidak ada dialog D-01"; pre-check sendiri tidak teramati dari UI, hanya akibatnya.
  - Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
