---
id: TC-FA-NOTIF-E2E-079-notasi-jamak-almost-timeout-dan-auto-canceled
title: "Notasi Jamak Notifikasi Almost Timeout Varian PIC Admin: Borrow, Transfer, dan Disposal"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-304
  - TC-FA-NOTIF-306
  - TC-FA-NOTIF-308
coverage:
  web: automated
---

# Notasi Jamak Notifikasi Almost Timeout Varian PIC Admin: Borrow, Transfer, dan Disposal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`, `Fixture.fixedAssetNotification.assetAdmin`; PIC pembuat BRW-2026-0341, TRF-2026-0056, dan DSP-2026-0031). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): transaksi BRW-2026-0341 (Pre-setup #19), TRF-2026-0056 (Pre-setup #21), dan DSP-2026-0031 (Pre-setup #22), masing-masing 2 aset (Pre-setup #24), pra-komitmen dengan sisa 24 jam. Keadaan awal itu disiapkan fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Keadaan awal tiap blok diatur fixture BE penyetel state sumber sesudah pemulihan seed (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah job `F-FATX-07` pada BRW-2026-0341, TRF-2026-0056, dan DSP-2026-0031 (Pre-setup #19, #21, #22) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): menjalankan job `F-FATX-07` langkah 2 untuk satu transaksi tertentu (butir "Kemampuan menjalankan job latar" di `suite.md`); job hanya pemicu keadaan, bukan objek uji; membaca jumlah notifikasi per penerima dan per Title (baseline dan pembacaan sesudah pemicu lewat kemampuan baca BE yang sama, bagian 8b butir 10).
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-304: borrow_almost_timeout varian PIC admin dengan 2 aset

1. Pulihkan seed lalu atur BRW-2026-0341 dua aset pra-komitmen dengan sisa 24 jam lewat fixture BE penyetel state sumber
2. Catat jumlah item `"Please finish this transaction — expiring soon"` milik Asset Admin (baseline) lewat fixture BE
3. Jalankan job `F-FATX-07` langkah 2 untuk BRW-2026-0341 hingga notifikasi tersimpan
4. Muat ulang halaman Fixed Asset > Dashboard
5. Klik Bell icon sebagai penerima
6. Verifikasi (kemampuan baca BE) jumlah item `"Please finish this transaction — expiring soon"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
7. Verifikasi Title item teratas `"Please finish this transaction — expiring soon"`
8. Verifikasi Body item teratas `"BRW-2026-0341 (2 Assets) — 24h left or less"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-306: transfer_almost_timeout varian PIC admin dengan 2 aset

9. Pulihkan seed lalu atur TRF-2026-0056 dua aset pra-komitmen dengan sisa 24 jam lewat fixture BE penyetel state sumber
10. Catat jumlah item `"Please finish this transaction — expiring soon"` milik Asset Admin (baseline) lewat fixture BE
11. Jalankan job `F-FATX-07` langkah 2 untuk TRF-2026-0056 hingga notifikasi tersimpan
12. Muat ulang halaman Fixed Asset > Dashboard
13. Klik Bell icon sebagai penerima
14. Verifikasi (kemampuan baca BE) jumlah item `"Please finish this transaction — expiring soon"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
15. Verifikasi Title item teratas `"Please finish this transaction — expiring soon"`
16. Verifikasi Body item teratas `"TRF-2026-0056 (2 Assets) — 24h left or less"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

### TC-FA-NOTIF-308: disposal_almost_timeout varian PIC admin dengan 2 aset

17. Pulihkan seed lalu atur DSP-2026-0031 dua aset pra-komitmen dengan sisa 24 jam lewat fixture BE penyetel state sumber
18. Catat jumlah item `"Please finish this transaction — expiring soon"` milik Asset Admin (baseline) lewat fixture BE
19. Jalankan job `F-FATX-07` langkah 2 untuk DSP-2026-0031 hingga notifikasi tersimpan
20. Muat ulang halaman Fixed Asset > Dashboard
21. Klik Bell icon sebagai penerima
22. Verifikasi (kemampuan baca BE) jumlah item `"Please finish this transaction — expiring soon"` bertambah tepat 1 dari baseline (satu notifikasi, bukan satu per aset)
23. Verifikasi Title item teratas `"Please finish this transaction — expiring soon"`
24. Verifikasi Body item teratas `"DSP-2026-0031 (2 Assets) — 24h left or less"` memakai notasi jamak `"[Transaction ID] ([N] Assets)"`

## Notes

- Langkah penghubung (S-03): langkah 4, 12, dan 20 (muat ulang agar notifikasi hasil pemicu termuat); langkah 1, 9, dan 17 (pulihkan seed dan atur precondition TC lewat fixture BE penyetel state sumber); langkah 2, 10, dan 18 (baseline per TC, bagian 8b butir 10).
- Job `F-FATX-07` (langkah 2) hanya pemicu keadaan; batas waktu almost timeout diuji di spec 086, 088, 090, dan 096.
- Pembagian TC lintas spec: TC-FA-NOTIF-305, 307, dan 309 (varian auto-canceled penerima yang sama) ada di spec 119.
- Pembagian per TC: TC-FA-NOTIF-304 (langkah 1 sampai 8), TC-FA-NOTIF-306 (langkah 9 sampai 16), TC-FA-NOTIF-308 (langkah 17 sampai 24).
- Temuan untuk QA:
  - TC-FA-NOTIF-304, 306, dan 308 tidak menyebut cara membuat transaksi pra-komitmen dengan sisa 24 jam; spec mengandalkan fixture BE pemulih seed menyiapkan keadaan itu.
  - Kolom Post Condition ketiga TC kosong (`-`); tidak ada yang diasersi.
