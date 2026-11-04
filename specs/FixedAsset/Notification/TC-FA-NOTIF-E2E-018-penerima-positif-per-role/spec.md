---
id: TC-FA-NOTIF-E2E-018-penerima-positif-per-role
title: "Penerima Positif Notifikasi per Role: Subjek Transaksi, Approver, Group Manager, dan Borrower"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-64
  - TC-FA-NOTIF-66
  - TC-FA-NOTIF-68
  - TC-FA-NOTIF-70
coverage:
  web: automated
---

# Penerima Positif Notifikasi per Role: Subjek Transaksi, Approver, Group Manager, dan Borrower

## Prerequisites

- Mode: FE+BE.
- Spec ditulis per blok role karena pemicu event dan penerimanya berbeda per TC dan ganti akun memakai langkah eksplisit (bagian 3a, keputusan 2026-10-21). Akun yang diuji:

  | TC | Role penerima | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-64 | Read Only (Borrower pada BRW-2026-0342) | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | `Fixture.fixedAssetNotification.readOnly` |
  | TC-FA-NOTIF-66 | Total Control pemegang Transaction Role Approver (Borrowing & Assignment) pada Gedung A | #1 | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | `Fixture.fixedAssetNotification.totalControl` |
  | TC-FA-NOTIF-68 | Group Manager (Gedung A) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | TC-FA-NOTIF-70 | Borrower Budi Santoso (tanpa tier atau Transaction Role) | #11 | `borrowerBudi_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_BORROWER_PASSWORD` | `Fixture.fixedAssetNotification.borrowerBudi` |

- Akun pemicu: Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) hanya lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`).
- Login akun aktor pertama (Read Only, Pre-setup #2) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141, Gedung A > Lantai 1 > Ruang 101; Pre-setup #19 dan #24); aset Kamera DSLR di Ruang 101 yang dipinjam dengan Due Date terlewati untuk TC-FA-NOTIF-68 (Pre-setup #24). Spec mengubah state BRW-2026-0342 per blok; fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) mengembalikannya di hook `before` dan `after` dan sebagai langkah penghubung antar blok.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemicu event modul sumber (submit Borrow, verifikasi scan, handover) lewat sesi API Asset Admin; fixture BE yang menetapkan Borrower BRW-2026-0342 per blok (Read Only pada blok TC-FA-NOTIF-64, Budi Santoso pada blok TC-FA-NOTIF-70); kemampuan menjalankan job overdue harian dan menggeser jam server dan jam fixture bersama (butir "Kemampuan menjalankan job latar" di `suite.md`), dipulihkan di hook `after` dan langkah penghubung blok TC-FA-NOTIF-68.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_RO_PASSWORD`, `FA_TC_PASSWORD`, `FA_GM_PASSWORD`, `FA_BORROWER_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-64: Read Only menerima notifikasi actionable sebagai subjek transaksi

1. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan verifikasi scan BRW-2026-0342 (Borrower: Read Only) hingga status Waiting for Confirmation tersimpan
2. Muat ulang halaman Fixed Asset > Dashboard
3. Klik Bell icon
4. Verifikasi item `"Please confirm your borrowed asset"` tampil pada Dropdown Panel Read Only
5. Verifikasi tombol `[Detail]` pada item `"Please confirm your borrowed asset"` tampil

### TC-FA-NOTIF-66: Total Control pemegang Transaction Role Approver menerima actionable approval dalam scope group

6. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
7. Dari akun Asset Admin (Pre-setup #8, sesi API), submit Borrow Request BRW-2026-0342 untuk aset di Gedung A dengan approval ON hingga status Waiting for Approval tersimpan
8. Logout, lalu login sebagai Total Control (Pre-setup #1), lalu buka Fixed Asset > Dashboard
9. Klik Bell icon
10. Verifikasi item `"Waiting for your approval"` dengan Body `"BRW-2026-0342 (1 Asset)"` tampil pada Dropdown Panel
11. Verifikasi tombol `[Detail]` pada item `"Waiting for your approval"` tampil

### TC-FA-NOTIF-68: Group Manager menerima informasional dan actionable sesuai scope group dan descendant tiga level

12. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
13. Atur jam server dan jam fixture ke setelah Due Date aset Kamera DSLR di Ruang 101 yang dipinjam, lalu jalankan job overdue harian untuk aset di Ruang 101 hingga notifikasi tersimpan
14. Pulihkan jam server dan jam fixture ke waktu semula
15. Logout, lalu login sebagai Group Manager (Gedung A, Pre-setup #3), lalu buka Fixed Asset > Dashboard
16. Klik Bell icon sebagai Group Manager Gedung A
17. Verifikasi item `"Your borrowed asset is overdue"` tampil pada Dropdown Panel
18. Verifikasi tombol `[Detail]` pada item `"Your borrowed asset is overdue"` tampil

### TC-FA-NOTIF-70: Borrower tanpa role administratif menerima event yang menyasar dirinya

19. Pulihkan seed dan transaksi (Pre-setup #17 sampai #24) lewat fixture BE
20. Dari akun Asset Admin (Pre-setup #8, sesi API), selesaikan handover BRW-2026-0342 (Borrower: Budi Santoso) hingga status handover tersimpan
21. Logout, lalu login sebagai Budi Santoso (Pre-setup #11), lalu buka Fixed Asset > Dashboard
22. Klik Bell icon sebagai Budi Santoso
23. Verifikasi item `"Asset handover completed"` tampil pada Dropdown Panel
24. Verifikasi tombol `[Mark as Read]` pada item `"Asset handover completed"` tampil

## Notes

- Langkah penghubung (S-03): langkah 2 (muat ulang agar notifikasi hasil pemicu termuat); langkah 6, 12, dan 19 (pulihkan seed antar blok); langkah 8, 15, dan 21 (ganti akun dan buka Fixed Asset > Dashboard); langkah 14 (pulihkan jam sebelum akun penerima dibuka, S-09).
- Pemicu event dijalankan di modul sumber lewat sesi API aktor dan asersi hanya pada Dropdown Panel (Catatan TC). Job overdue harian (langkah 13) hanya pemicu keadaan, bukan objek uji. Klausa "scope group mencakup descendant tiga level" (Expected TC-FA-NOTIF-68) adalah penjelasan hasil, bukan klausa yang dapat gagal sendiri; yang diasersi adalah item dan `[Detail]` untuk aset di Ruang 101 (level 3 di bawah Gedung A).
- Pembagian per TC: TC-FA-NOTIF-64 (langkah 1 sampai 5), TC-FA-NOTIF-66 (langkah 6 sampai 11), TC-FA-NOTIF-68 (langkah 12 sampai 18), TC-FA-NOTIF-70 (langkah 19 sampai 24).
- Temuan untuk QA:
  - Kontradiksi Borrower BRW-2026-0342: TC-FA-NOTIF-64 menulis Read Only sebagai Borrower, sedangkan TC-FA-NOTIF-70 dan Pre-setup #38 menulis Budi Santoso. Spec mengikuti masing-masing TC dengan fixture BE yang menetapkan Borrower per blok (disediakan tim FE/BE).
  - Kolom Post Condition keempat TC kosong (`-`); tidak ada yang diasersi.
  - TC-FA-NOTIF-64, 66, 68, 70 tidak menyebut keadaan awal BRW-2026-0342 untuk langkah "selesaikan verifikasi scan" dan "selesaikan handover" (Ready for Verification atau Ready for Handover); spec mengandalkan fixture BE pemulih menyiapkan keadaan itu per blok.
  - TC-FA-NOTIF-68 tidak menulis akun pemicu job overdue maupun tanggal acuan Due Date; spec memakai kemampuan jam server dan job suite.
