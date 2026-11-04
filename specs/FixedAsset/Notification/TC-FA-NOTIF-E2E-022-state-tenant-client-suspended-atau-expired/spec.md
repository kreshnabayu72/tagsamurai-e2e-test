---
id: TC-FA-NOTIF-E2E-022-state-tenant-client-suspended-atau-expired
title: "State Tenant: Client Suspended atau Expired pada Detail dan Mark as Read"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-365
  - TC-FA-NOTIF-394
coverage:
  web: automated
---

# State Tenant: Client Suspended atau Expired pada Detail dan Mark as Read

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Dashboard (Bell icon, Dropdown Panel).
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): seed notifikasi Pre-setup #17 untuk akun aktor: N-01 `Waiting for your approval` BRW-2026-0341 (2 Assets) Unread actionable (BRW-2026-0341 masih Waiting for Approval; Total Control memegang Transaction Role Approver Borrowing & Assignment); N-02 `Please confirm your borrowed asset` Kamera DSLR (AST-2024-0141) Unread actionable; N-03 `Asset has been repaired` Unread view-only; N-04 `Asset has been found` Laptop - 1 (AST-2024-0067) Unread view-only; N-05 `Your Total Control access was removed` Unread view-only; N-06 `Your request has been rejected` BRW-2026-0341 Read view-only; N-07 `New audit task started` Read actionable. Badge Bell icon awal `5`.
- State global yang diubah spec (kelas h, state tenant): status Client pemilik data menjadi Suspended lewat fixture BE (butir "Fixture BE status client Suspended dan Expired" di `suite.md`; sesi UI tetap terbuka, status diubah sesudah sesi dibuka). Pemulihan ke status Active dilakukan sebagai langkah penghubung dan di hook `after` (tetap jalan walau spec gagal di tengah). Status Expired berperilaku sama menurut TC dan tidak diuji terpisah.
- Kemampuan teknis (disediakan tim FE, tanpa endpoint karangan): membaca status respons HTTP `Mark as Read` dari browser (pemantauan respons).
- Fixture BE pemulih seed notifikasi dan transaksi (Pre-setup #17 sampai #24) dijalankan di hook `before` dan `after` serta sebagai langkah penghubung sebelum TC-FA-NOTIF-394 (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`).
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-01 dan N-03 (Pre-setup #17) yang menjadi target `[Detail]` dan `[Mark as Read]` (ditolak server saat Client Suspended) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk akun aktor: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-365: Client Suspended atau Expired, klik [Detail] tetap menavigasi tanpa dialog D-01

1. Setel status Client pemilik data menjadi Suspended lewat fixture BE
2. Klik Bell icon
3. Klik `[Detail]` pada item N-01
4. Verifikasi browser berpindah ke `/fams/approvals/borrowing-assignment/BRW-2026-0341`
5. Verifikasi tidak ada dialog D-01

### TC-FA-NOTIF-394: Client Suspended atau Expired, Mark as Read ditolak server dengan toast baku

6. Pulihkan status Client menjadi Active dan seed notifikasi Pre-setup #17 lewat fixture BE, lalu buka Fixed Asset > Dashboard
7. Setel status Client pemilik data menjadi Suspended lewat fixture BE
8. Klik Bell icon
9. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
10. Verifikasi respons Mark as Read dari server berstatus `403`
11. Verifikasi muncul toast error `Changes can't be saved while this workspace is suspended or expired.`
12. Verifikasi tidak ada toast sukses `Success, notification has been marked as read.`
13. Verifikasi item N-03 tetap Unread
14. Verifikasi item N-03 tetap memiliki tombol `[Mark as Read]`
15. Verifikasi badge Bell icon tetap `5`
16. Pulihkan status Client menjadi Active lewat fixture BE

## Notes

- Langkah penghubung (S-03): langkah 1 dan 7 (menyetel Suspended sesudah sesi UI dibuka); langkah 6 (pemulihan status dan seed antar TC serta membuka Fixed Asset > Dashboard setelah navigasi ke Approvals); langkah 16 (pemulihan status, cadangan oleh hook `after`).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 5 didahului langkah 4 (halaman Approvals tujuan tampil); langkah 12 didahului langkah 11 (toast error tampil).
- Asersi tambahan (S-03): langkah 13 dan 14 memecah "tetap Unread dengan tombol `[Mark as Read]`" menjadi dua klausa (S-01).
- Temuan untuk QA:
  - TC-FA-NOTIF-394 menulis penolakan `403` sebagai bagian Expected a; status respons tidak teramati dari tampilan, sehingga langkah 10 memakai kemampuan pemantauan respons browser (disediakan tim FE).
  - Post Condition TC-FA-NOTIF-365 dan 394 kosong (`-`); tidak ada yang diasersi. TC tidak memuat variasi Expired; hanya Suspended yang dijalankan.
