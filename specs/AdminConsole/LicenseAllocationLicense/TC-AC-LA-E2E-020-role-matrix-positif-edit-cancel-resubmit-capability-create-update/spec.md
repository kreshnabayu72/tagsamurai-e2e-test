---
id: TC-AC-LA-E2E-020-role-matrix-positif-edit-cancel-resubmit-capability-create-update
title: "Role Matrix Positif: Edit, Cancel, dan Resubmit per Capability Create dan Update"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-73
  - TC-AC-LA-74
  - TC-AC-LA-481
coverage:
  web: automated
---

# Role Matrix Positif: Edit, Cancel, dan Resubmit per Capability Create dan Update

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Read+Update tanpa Create (Pre-setup #6) `updateOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Yuni Lestari`), password `Spectra.env.AC_LA_DIST_UPDATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun berikutnya (ganti akun dengan langkah eksplisit di Test Steps): Distributor Create+Read tanpa Update (Pre-setup #5) `createOnlyLic_automated_{namaCompany}@qwertysystem.net` (`Doni Prasetyo`), password `Spectra.env.AC_LA_DIST_CREATE_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.

| Akun | Peran | Aksi | Data milik spec |
|---|---|---|---|
| `updateOnlyLic` (`Yuni Lestari`) | Distributor Read+Update tanpa Create | Edit dan Cancel record sendiri | dua alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, dibuat saat akun masih punya capability Create (menyerupai Pre-setup #43) |
| `createOnlyLic` (`Doni Prasetyo`) | Distributor Create+Read tanpa Update | Resubmit record Canceled sendiri | satu alokasi `Canceled` manual Concurrent User +5 PT Sejahtera milik `Doni P` (menyerupai Pre-setup #59) |

- Data milik spec dibuat lewat seeding backend di hook `before` dan dibersihkan di hook `after`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci ownWaitingEdit, ownWaitingCancel, ownCanceledDoni). Pre-setup lain: #19 PT Sejahtera, #33 saldo kantong wallet, #34 Product Price, #39 Require Approval OFF.
- Jam: tanggal acuan server uji `22 Dec 2026` (fixture waktu, jam server dan jam browser diatur absolut di hook `before` dan dipulihkan di hook `after`). Record hasil Resubmit (data Dinamis) dibersihkan fixture backend.
- Konfigurasi kolom Setup Column yang disimpan spec (kolom Payment) dipulihkan dengan menghapus preferensi kolom di browser di hook `after` (kemampuan disediakan tim FE).
- Kemampuan teknis: seeding record alokasi atas nama akun tertentu; mekanisme seeding tidak tertulis di TC dan disediakan tim FE/BE.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-73: Read+Update tanpa Create: Edit record sendiri sampai sukses

1. Ketik Search Allocation ID alokasi `Waiting for Approval` milik spec untuk Edit (`Fixture.license-allocation-license.ownWaitingEdit`), tekan Enter
2. Klik row action `Edit` pada record milik sendiri
3. Ubah Additional Quantity dari `5` menjadi `6`
4. Klik `[Save]`
5. Verifikasi toast sukses: "Success, license allocation has been updated."
6. Verifikasi Status tetap `Waiting for Approval`
7. Verifikasi Quantity menjadi `+6`

### TC-AC-LA-74: Read+Update tanpa Create: Cancel record sendiri sampai sukses

8. Ganti isi kotak search dengan Allocation ID alokasi `Waiting for Approval` milik spec untuk Cancel (`Fixture.license-allocation-license.ownWaitingCancel`), tekan Enter
9. Klik row action `Cancel Allocation` pada record milik sendiri
10. Klik `[Cancel Request]` pada dialog konfirmasi
11. Verifikasi toast sukses: "Success, license allocation has been canceled."
12. Verifikasi hasil Search tab Current kosong dengan empty state `No results found` (baris pindah dari tab Current)
13. Klik tab `History`
14. Verifikasi baris `Fixture.license-allocation-license.ownWaitingCancel` tampil dengan Status `Canceled`

### TC-AC-LA-481: Create-only menyelesaikan Resubmit dari record Canceled miliknya

15. Ganti akun: Logout lalu login sebagai Distributor Create+Read (`createOnlyLic`)
16. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
17. Catat baseline Allocation ID baris di halaman pertama tab Current
18. Klik tab `History`, lalu ketik Search Allocation ID alokasi `Canceled` milik `Doni P` (`Fixture.license-allocation-license.ownCanceledDoni`), tekan Enter
19. Klik row action `Resubmit` pada baris `Canceled` milik sendiri
20. Klik `[Submit]`
21. Verifikasi toast sukses: "Success, license allocation has been resubmitted."
22. Klik `(←)` pada kotak Search, lalu klik tab `Current`
23. Verifikasi baris baru tab Current (record baru dengan Allocation ID baru, tidak ada pada baseline langkah 17) berstatus `Active`
24. Verifikasi Allocated By baris baru: `Doni P`
25. Verifikasi Payment baris baru: `Wallet`
26. Klik tab `History`, lalu ketik Search Allocation ID `Fixture.license-allocation-license.ownCanceledDoni`, tekan Enter
27. Verifikasi baris `Canceled` asal tetap berada di tab History
28. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah Setup Column, langkah `Klik (←)` pada kotak Search dan pindah tab, dan ganti akun eksplisit (S-07). Record baru hasil Resubmit adalah baris di halaman pertama tab Current yang Allocation ID-nya tidak ada pada baseline langkah 17 (S-12).
- Role Matrix: ditulis per blok role karena ganti akun menuntut Step eksplisit (bagian 3a, 2026-10-30) dan tiap blok akun berdiri sendiri; hasil dan data berbeda per role.
- Aksi Edit, Cancel, dan Resubmit memakai record milik spec yang dibuat saat akun masih punya capability yang diperlukan (Pre-setup #43 dan #59 sebagai pola); Pre-setup bersama tidak diubah (S-06).
- Temuan untuk QA:
  - TC-AC-LA-73 Post Condition (`entri Edit tercatat di tiga surface`), TC-AC-LA-74 Post Condition (`Reserve dilepas`), dan TC-AC-LA-481 Post Condition (`Record baru; record asal tetap Canceled`) tidak punya langkah observasi pada TC-AC-LA-73 dan TC-AC-LA-74; hanya TC-AC-LA-481 yang punya Expected c.
  - TC-AC-LA-73 Precondition tidak menjelaskan bagaimana record milik `Yuni L` dibuat saat Create dicabut (Pre-setup #43: `dibuat ketika akunnya masih punya capability Create`); spec memakai seeding backend.
  - TC-AC-LA-481 Expected b menyebut `Status Active` dan `Payment Wallet`; asersi memakai baris baru yang Allocation ID-nya tidak ada pada baseline (S-12).
