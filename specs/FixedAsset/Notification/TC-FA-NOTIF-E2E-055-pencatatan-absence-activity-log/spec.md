---
id: TC-FA-NOTIF-E2E-055-pencatatan-absence-activity-log
title: "Absence Activity Log: Mark as Read dan Auto-Read Tidak Menambah Entri"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-351
coverage:
  web: automated
---

# Absence Activity Log: Mark as Read dan Auto-Read Tidak Menambah Entri

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Notification Center dan Reports & Logs > Activity Log.
- Akun aktor: Total Control Pre-setup #1 (`totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`; nama env usulan, belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; memegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data: seed N-01 sampai N-07 (Pre-setup #17; N-03 `Asset has been repaired` Unread view-only) milik akun aktor, notifikasi `borrow_waiting_approval` BRW-2026-0342 berstatus Unread (actionable; precondition e TC-351, disediakan fixture BE pemulih sesuai Pre-setup #17) untuk akun aktor, dan transaksi Borrow BRW-2026-0342 (Pre-setup #19) berstatus Waiting for Approval, dipulihkan fixture BE pemulih di hook `before` dan `after`. Activity Log FAMS tersedia. Nilai dibaca dari `Fixture.fixedAssetNotification.<kunci>`; fixture `fixtures/fixedAssetNotification.json` belum ada dan disediakan tim FE.
- Pemicu: aksi Approve BRW-2026-0342 dilakukan lewat sesi API akun aktor (suite.md) sebagai pemicu spec absence (P-5 butir a); Approve bukan objek uji.
- Kemampuan teknis: membaca jumlah entri Activity Log (Tab User Action) sebelum dan sesudah aksi (baseline, S-12), disediakan tim FE/BE dan dinyatakan di `suite.md`; endpoint tidak dikarang.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): notifikasi seed N-03 (Pre-setup #17) yang menjadi target `[Mark as Read]` dan langkah Approve pada transaksi BRW-2026-0342 (Pre-setup #19) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Hook suite yang berlaku (rujukan ke `suite.md`): sesi API aktor, flag Guided Tooltip (akun #1 sudah true), dan fixture BE pemulih seed notifikasi dan transaksi.

## Test Steps

### TC-FA-NOTIF-351: Mark as Read dan Auto-Read tidak menambah entri Activity Log

1. Catat jumlah entri Activity Log Tab User Action lewat kemampuan baca jumlah entri (baseline)
2. Klik Bell icon
3. Verifikasi item `borrow_waiting_approval` BRW-2026-0342 tampil Unread (dot Unread) pada Dropdown Panel sebelum aksi Approve (anchor bahwa Auto-Read dapat terjadi)
4. Lewat sesi API akun aktor, Approve BRW-2026-0342 hingga aksi Approve tersimpan (aksi sumber)
5. Klik `[Show All]`
6. Klik `[Mark as Read]` pada item N-03 (`Asset has been repaired`)
7. Tunggu aksi selesai (item N-03 berubah menjadi Read)
8. Buka Reports & Logs > Activity Log > Tab `User Action`
9. Verifikasi jumlah entri bertambah dari baseline langkah 1 (selisih dicatat)
10. Verifikasi entri aksi Approve BRW-2026-0342 dari modul sumber tampil tercatat di antara baris teratas sebanyak selisih langkah 9
11. Verifikasi tidak ada entri untuk Mark as Read maupun Auto-Read di antara entri baru (baris teratas sebanyak selisih langkah 9)
12. Pulihkan seed notifikasi dan transaksi lewat fixture BE pemulih

## Notes

- Sumber: `fixed-asset/notification/TestCases/tc-notification.md`. Spec absence (kelas g); TC-351 hanya ada di spec ini (S-05) dengan baseline sendiri. P-5: Approve dipakai sebagai pemicu yang membentuk kondisi yang diasersi tidak tercatat.
- Langkah penghubung (S-03): langkah 2 dan 5 (membuka Dropdown Panel dan Notification Center sebagai precondition `[Mark as Read]`), 7 (menunggu aksi selesai sebelum berpindah surface, 8b butir 8), 12 (pemulihan seed).
- Asersi tambahan di luar Expected TC (S-03): langkah 3 (item BRW-2026-0342 Unread sebelum Approve, anchor Auto-Read, precondition e TC-351); langkah 9 (selisih jumlah entri dari baseline, S-12 dan 8b butir 2, dibuktikan sebelum isi entri dibaca); langkah 10 dan 11 membaca entri baru sebagai himpunan baris teratas sebanyak selisih tanpa mengandalkan urutan di antaranya (S-14).
- Temuan untuk QA:
  - TC-351 Expected butir a menyebut "entri aksi Approve tercatat" tanpa menyebut jumlah entri yang dihasilkan Approve; spec tidak mengasumsikan satu entri dan membaca seluruh entri baru sebagai himpunan.
  - TC-351 langkah 2 menyebut "Approver Approve" tanpa menyebut akun; spec memakai sesi API akun aktor #1 (langkah 4) yang memegang Transaction Role Approver (Borrowing & Assignment).
  - TC-351 langkah 3 tidak menyebut Auto-Read dipicu oleh langkah mana; Auto-Read item `borrow_waiting_approval` BRW-2026-0342 terjadi akibat Approve (langkah 4), dan klausa "tidak ada entri Auto-Read" diasersi pada langkah 11.
