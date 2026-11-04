---
id: TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable
title: "Detail dan Klik Area Item Actionable: Navigasi Tanpa Mengubah Status Baca"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-99
  - TC-FA-NOTIF-105
  - TC-FA-NOTIF-107
  - TC-FA-NOTIF-381
  - TC-FA-NOTIF-386
coverage:
  web: automated
---

# Detail dan Klik Area Item Actionable: Navigasi Tanpa Mengubah Status Baca

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel) dan Notification Center.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Tabel "Ulangan TC-FA-NOTIF-105" (urutan baris = urutan iterasi): ulangan 1, ulangan 2, ulangan 3.
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable; N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable (task TASK-Q3-A Pre-setup #23 berstatus Completed). Badge Bell icon awal `5`. Transaksi BRW-2026-0341 masih Waiting for Approval dan Total Control memegang Transaction Role Approver (Borrowing & Assignment).
- Spec hanya membaca dan menavigasi; seed tidak diubah. Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-01 dan N-07 (Pre-setup #17) yang menjadi target `[Detail]` dan klik area item (navigasi tanpa mengubah status baca) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-99: Klik [Detail] pada transaksi masih menunggu tindakan menavigasi tanpa mengubah status baca

1. Klik Bell icon
2. Klik `[Detail]` pada item N-01
3. Verifikasi browser berpindah ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`
4. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
5. Klik Bell icon
6. Verifikasi item N-01 tetap Unread
7. Verifikasi tombol `[Detail]` pada item N-01 tetap ada

### TC-FA-NOTIF-105: Klik [Detail] berulang kali tanpa submit tidak mengubah status baca

8. Muat ulang halaman Fixed Asset > Dashboard
9. Klik Bell icon
10. Untuk setiap baris tabel "Ulangan TC-FA-NOTIF-105" (langkah 10 sampai 14): klik `[Detail]` pada item N-01
11. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
12. Klik Bell icon
13. Verifikasi item N-01 tetap Unread
14. Verifikasi badge Bell icon tetap `5`

### TC-FA-NOTIF-107: Klik area item actionable Unread berperilaku sama dengan [Detail]

15. Klik judul item N-01 (bukan tombol)
16. Verifikasi browser berpindah ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`
17. Kembali ke Fixed Asset > Dashboard (navigasi balik browser)
18. Klik Bell icon
19. Verifikasi status baca item N-01 tidak berubah (tetap Unread)

### TC-FA-NOTIF-381: Klik [Detail] di Notification Center menavigasi tanpa mengubah status baca

20. Klik `[Show All]`
21. Klik `[Detail]` pada item N-01
22. Verifikasi browser berpindah ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`
23. Kembali ke Notification Center (navigasi balik browser)
24. Verifikasi item N-01 tetap Unread
25. Verifikasi tombol `[Detail]` pada item N-01 tetap ada

### TC-FA-NOTIF-386: Klik area item actionable yang sudah Read menavigasi ke Klik -> Path

26. Klik judul item N-07 (`New audit task started`, actionable Read, bukan tombol)
27. Verifikasi browser berpindah ke `/fams/audit/task/TASK-Q3-A`
28. Verifikasi halaman tujuan berupa halaman konteks atau hasil akhir read-only (bukan form aksi)
29. Verifikasi dialog D-01 tidak muncul
30. Kembali ke Notification Center (navigasi balik browser)
31. Verifikasi item N-07 tetap Read
32. Verifikasi item N-07 tidak memiliki tombol `[Detail]`
33. Verifikasi badge Bell icon tetap `5`

## Notes

- Pengulangan (bagian 8b butir 7): langkah 10 sampai 14 diulang untuk tiga baris tabel "Ulangan TC-FA-NOTIF-105" (tiga ulangan: satu klik awal ditambah "ulangi langkah 1 dua kali lagi" pada TC; 43 langkah setelah ekspansi). Nomor langkah pada rujukan memakai nomor spec yang kontinu (R-04).
- Alasan melewati ambang 35 langkah (bila ekspansi dihitung): semua blok satu kelas (klik item dan navigasi tanpa mengubah state) dan tiap TC berdiri sendiri; kegagalan satu TC tidak membuat TC lain kehilangan makna.
- Langkah penghubung (S-03): langkah 4, 11, 17, 23, dan 30 (kembali ke daftar, sesuai langkah TC "lalu kembali"); langkah 8 dan 9 (memuat ulang agar Dropdown Panel kembali tertutup sebelum Bell icon dibuka); langkah 20 (membuka Notification Center lewat `[Show All]` karena TC tidak menyebut jalur lain); langkah 5, 12, dan 18 (membuka Dropdown Panel setelah kembali).
- Pre-check yang "berjalan di titik klik" (TC-FA-NOTIF-107) tidak teramati terpisah dari UI; yang diasersi adalah navigasi dan status baca.
- Temuan untuk QA:
  - TC-FA-NOTIF-99, 105, 107, dan 381 mensyaratkan BRW-2026-0341 masih Waiting for Approval, sedangkan seed N-06 menulis BRW-2026-0341 sebagai request yang sudah ditolak (Rejected); kedua keadaan tidak dapat berlaku bersamaan untuk transaksi yang sama. Spec mengikuti TC dan mengandalkan fixture BE.
  - TC-FA-NOTIF-386 menulis "halaman konteks atau hasil akhir read-only" menunggu pemilik modul tujuan (Open Item #5 PRD); asersi langkah 28 dapat direvisi.
  - Post Condition kelima TC kosong (`-`); tidak ada yang diasersi.
