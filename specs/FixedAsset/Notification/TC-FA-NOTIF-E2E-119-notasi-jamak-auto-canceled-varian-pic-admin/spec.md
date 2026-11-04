---
id: TC-FA-NOTIF-E2E-119-notasi-jamak-auto-canceled-varian-pic-admin
title: "Notasi Jamak Notifikasi Auto Canceled Varian PIC Admin: Borrow, Transfer, dan Disposal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-305
  - TC-FA-NOTIF-307
  - TC-FA-NOTIF-309
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Auto Canceled Varian PIC Admin: Borrow, Transfer, dan Disposal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`; PIC pembuat BRW-2026-0341, TRF-2026-0056, dan DSP-2026-0031). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): transaksi BRW-2026-0341 (Pre-setup #19), TRF-2026-0056 (Pre-setup #21), dan DSP-2026-0031 (Pre-setup #22), masing-masing 2 aset (Pre-setup #24), pra-komitmen dengan batas waktu terlampaui. Keadaan awal itu disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menjalankan job `F-FATX-07` langkah 3 untuk satu transaksi tertentu (butir "Kemampuan menjalankan job latar" di `suite.md`); job hanya pemicu keadaan, bukan objek uji; membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah job `F-FATX-07` langkah 3 pada BRW-2026-0341, TRF-2026-0056, dan DSP-2026-0031 (Pre-setup #19, #21, #22) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-305: borrow_auto_canceled dengan 2 aset

1. Catat jumlah item `"Your request was canceled automatically"` milik Asset Admin (baseline) lewat fixture BE
2. Jalankan job `F-FATX-07` langkah 3 untuk BRW-2026-0341 hingga notifikasi tersimpan
3. Muat ulang halaman Fixed Asset > Dashboard
4. Klik Bell icon sebagai penerima
5. Verifikasi (kemampuan baca BE) jumlah item `"Your request was canceled automatically"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
6. Verifikasi Title item teratas `"Your request was canceled automatically"`
7. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets): not completed in time"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-307: transfer_auto_canceled dengan 2 aset

8. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
9. Catat jumlah item `"Your request was canceled automatically"` milik Asset Admin (baseline) lewat fixture BE
10. Jalankan job `F-FATX-07` langkah 3 untuk TRF-2026-0056 hingga notifikasi tersimpan
11. Muat ulang halaman Fixed Asset > Dashboard
12. Klik Bell icon sebagai penerima
13. Verifikasi (kemampuan baca BE) jumlah item `"Your request was canceled automatically"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
14. Verifikasi Title item teratas `"Your request was canceled automatically"`
15. Verifikasi Body item teratas `"TRF-2026-0056 (2 Assets): not completed in time"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-309: disposal_auto_canceled dengan 2 aset

16. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
17. Catat jumlah item `"Your request was canceled automatically"` milik Asset Admin (baseline) lewat fixture BE
18. Jalankan job `F-FATX-07` langkah 3 untuk DSP-2026-0031 hingga notifikasi tersimpan
19. Muat ulang halaman Fixed Asset > Dashboard
20. Klik Bell icon sebagai penerima
21. Verifikasi (kemampuan baca BE) jumlah item `"Your request was canceled automatically"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
22. Verifikasi Title item teratas `"Your request was canceled automatically"`
23. Verifikasi Body item teratas `"DSP-2026-0031 (2 Assets): not completed in time"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

## Notes

- Langkah penghubung (S-03): langkah 3, 11, dan 19 (muat ulang agar notifikasi hasil pemicu termuat); langkah 8 dan 16 (pulihkan seed antar blok); langkah 1, 9, dan 17 (baseline per TC, bagian 8b butir 10).
- Job `F-FATX-07` (langkah 3) hanya pemicu keadaan; batas waktu auto cancel diuji di spec 087, 089, dan 097.
- Pembagian TC lintas spec: TC-FA-NOTIF-304, 306, dan 308 (varian almost timeout penerima yang sama) ada di spec 079.
- Pembagian per TC: TC-FA-NOTIF-305 (langkah 1 sampai 7), TC-FA-NOTIF-307 (langkah 8 sampai 15), TC-FA-NOTIF-309 (langkah 16 sampai 23).
- Temuan untuk QA:
  - TC-FA-NOTIF-305, 307, dan 309 tidak menyebut cara membuat transaksi pra-komitmen dengan batas waktu terlampaui; spec mengandalkan fixture BE pemulih seed menyiapkan keadaan itu.
  - Kolom Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
