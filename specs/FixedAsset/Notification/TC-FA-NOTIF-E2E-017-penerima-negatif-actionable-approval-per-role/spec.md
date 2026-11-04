---
id: TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role
title: "Role Matrix: Penerima Negatif Notifikasi Actionable Approval Borrow per Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-NOTIF-63
  - TC-FA-NOTIF-65
  - TC-FA-NOTIF-67
  - TC-FA-NOTIF-69
  - TC-FA-NOTIF-410
coverage:
  web: automated
---

# Role Matrix: Penerima Negatif Notifikasi Actionable Approval Borrow per Role

## Prerequisites

- Mode: FE+BE.
- Spec Role Matrix (bagian 3a konvensi), polaritas negatif seragam: pemicu dan asersi sama untuk semua role, hanya akun login yang berbeda. Role yang diuji, urutan baris = urutan iterasi:

  | TC | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|---|
  | TC-FA-NOTIF-63 | Read Only | #2 | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | `Fixture.fixedAssetNotification.readOnly` |
  | TC-FA-NOTIF-65 | Total Control tanpa Transaction Role Approver | #26 | `totalControlNoRole_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TCNOROLE_PASSWORD` | `Fixture.fixedAssetNotification.totalControlNoRole` |
  | TC-FA-NOTIF-67 | Group Manager (Gedung A, tanpa Transaction Role Approver) | #3 | `groupManagerFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | `Fixture.fixedAssetNotification.groupManager` |
  | TC-FA-NOTIF-69 | Approver Transfer (Gedung A, bukan Approver Borrowing & Assignment) | #5 | `approverTransfer_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERTRF_PASSWORD` | `Fixture.fixedAssetNotification.approverTransfer` |
  | TC-FA-NOTIF-410 | Approver Borrowing & Assignment Gedung B (tanpa peran di Gedung A) | #32 | `approverGedungB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERGDGB_PASSWORD` | `Fixture.fixedAssetNotification.approverGedungB` |

- Akun pendukung (bukan baris tabel Role): Approver Borrowing & Assignment Gedung A (Pre-setup #4, `approverBorrowingAssignment_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_APPROVERBA_PASSWORD`, `Fixture.fixedAssetNotification.approverBorrowingAssignment`) sebagai anchor positif penerima sah; Asset Admin (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`) hanya lewat sesi API aktor sebagai pemicu submit.
- Login akun aktor pertama (Read Only, Pre-setup #2) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): transaksi Borrow BRW-2026-0342 (1 aset Kamera DSLR AST-2024-0141, Gedung A > Lantai 1 > Ruang 101; Pre-setup #19 dan #24) sebelum disubmit; approval Borrow ON. Spec mengubah BRW-2026-0342 menjadi Waiting for Approval; fixture BE pemulih seed dan transaksi (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) mengembalikannya di hook `before` dan `after`.
- Kemampuan teknis: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Asset Admin; fixture BE pemicu event modul sumber (submit Borrow) disediakan tim FE/BE tanpa endpoint karangan.
- Asersi absence atas notifikasi in-app memakai baseline jumlah pada badge Bell icon per role yang dicatat sebelum pemicu, anchor positif (Approver menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Pengecualian S-06/S-12 butir A-16 (konvensi Lampiran A): transaksi Pre-setup BRW-2026-0342 disubmit sebagai pemicu dengan nama literal tanpa suffix karena ID transaksi dibangkitkan sistem dan ditulis literal di Expected TC. Pemulihannya dijamin fixture BE pemulih seed notifikasi dan transaksi di atas (butir di `suite.md`) di hook `before` dan `after` serta langkah penghubung antar blok TC; suite berjalan serial.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_RO_PASSWORD`, `FA_TCNOROLE_PASSWORD`, `FA_GM_PASSWORD`, `FA_APPROVERTRF_PASSWORD`, `FA_APPROVERGDGB_PASSWORD`, `FA_APPROVERBA_PASSWORD`, dan `FA_ASSETADMIN_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-63, TC-FA-NOTIF-65, TC-FA-NOTIF-67, TC-FA-NOTIF-69, dan TC-FA-NOTIF-410: Baseline badge tiap role

1. Untuk setiap baris tabel Role yang diuji (langkah 1 sampai 2): logout, lalu login sebagai role pada baris tabel dengan env var password baris itu, lalu buka Fixed Asset > Dashboard
2. Catat jumlah pada badge Bell icon role itu sebagai baseline (0 bila badge tidak tampil)

### Pemicu dan anchor positif pada Approver Borrowing & Assignment

3. Dari akun Asset Admin (Pre-setup #8, sesi API), submit Borrow Request BRW-2026-0342 dengan approval ON hingga status Waiting for Approval tersimpan
4. Logout, lalu login sebagai Approver (Borrowing & Assignment, akun Pre-setup #4), lalu buka Fixed Asset > Dashboard
5. Klik Bell icon
6. Verifikasi item `"Waiting for your approval"` dengan Body `"BRW-2026-0342 (1 Asset)"` tampil pada Dropdown Panel Approver (anchor positif)
7. Tunggu 5 detik tanpa memuat ulang halaman

### Penerima negatif per role

8. Untuk setiap baris tabel Role yang diuji (langkah 8 sampai 12): logout, lalu login sebagai role pada baris tabel dengan env var password baris itu, lalu buka Fixed Asset > Dashboard
9. Klik Bell icon
10. Verifikasi Dropdown Panel role itu tampil
11. Verifikasi item `"Waiting for your approval"` dengan Body `"BRW-2026-0342 (1 Asset)"` tidak tampil pada Dropdown Panel role itu
12. Verifikasi badge Bell icon role itu sama dengan baseline langkah 2 (tidak bertambah)

## Notes

- Pengulangan (bagian 8b butir 7): langkah 1 sampai 2 dan langkah 8 sampai 12 diulang untuk tiap baris tabel Role yang diuji (lima baris, 40 langkah setelah ekspansi bersama langkah 3 sampai 7). Satu pemicu (langkah 3) melayani kelima role karena submit BRW-2026-0342 yang sama menjadi kondisi tiap TC; tiap TC dibedakan oleh role penerima yang diperiksa. Langkah 1 dan 8 pada iterasi pertama melakukan logout dan login ulang akun yang sama dengan akun hook `before` supaya isi langkah identik (S-07).
- Langkah penghubung (S-03): langkah 1, 4, dan 8 (ganti akun dan buka Fixed Asset > Dashboard); langkah 2 (catat baseline, S-12); langkah 7 (jendela 5 detik, bagian 6 konvensi); langkah 10 (anchor permukaan: Dropdown Panel termuat).
- Pemetaan TC ke baris: TC-FA-NOTIF-63 Read Only, TC-FA-NOTIF-65 Total Control tanpa Transaction Role Approver, TC-FA-NOTIF-67 Group Manager, TC-FA-NOTIF-69 Approver Transfer, TC-FA-NOTIF-410 Approver Gedung B. Langkah 6 memuat Body `"BRW-2026-0342 (1 Asset)"` untuk semua role; TC-FA-NOTIF-63 menulis anchor hanya dengan judul item, dan TC-FA-NOTIF-67 serta 69 tidak menulis asersi badge; Body pada anchor dan asersi badge pada langkah 12 diterapkan seragam untuk semua role sebagai penambahan yang dicatat di sini (S-03).
- Alasan melewati ambang sekitar 35 langkah (bila ekspansi dihitung): semua blok satu kelas (Role Matrix negatif) dan tiap iterasi berdiri sendiri; kegagalan satu role tidak membuat role lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-NOTIF-63, 65, 67, 69, dan 410 menulis "melihat" dan "tidak melihat" item tanpa pembanding item lain pada Dropdown Panel akun negatif; tabel Pre-setup tidak menjamin seed notifikasi untuk akun #2, #26, #3, #5, dan #32, sehingga anchor absence hanya Dropdown Panel termuat (langkah 10).
  - Kolom Post Condition kelima TC kosong (`-`); tidak ada yang diasersi.
  - Email akun Asset Admin yang men-submit (Pre-setup #8) dan Approver (Pre-setup #4) diambil dari tabel Pre-setup; TC hanya menulis "akun Asset Admin" tanpa nomor Pre-setup.
