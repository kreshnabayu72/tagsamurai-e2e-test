---
id: TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission
title: "Modul Konsumen: Total Control Fallback Reviewer, GM Baru Tanpa Snapshot, Wallet Deposit, dan Approver TAG Stock"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-366
  - TC-AC-RP-367
  - TC-AC-RP-368
  - TC-AC-RP-369
coverage:
  web: automated
---

# Modul Konsumen: Total Control Fallback Reviewer, GM Baru Tanpa Snapshot, Wallet Deposit, dan Approver TAG Stock

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor pertama: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor ganti akun eksplisit (S-07): Standard `Alex Tan` pada langkah 9; Standard `John Dohan` (Group Role `Manage wallet & pricing` di `Region Jawa` C/R; Pre-setup #15) pada langkah 14; Standard `Sarah Kimura` (Additional Approver `Manage TAG stock`, Pre-setup #17; peran `Manage partner` tanpa penugasan group, Pre-setup #15) pada langkah 18. Email dan password ketiga akun tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal termasuk `Branch 1` tanpa GM), #12, #14, #15, #17 (`Manage TAG stock` = `Sarah Kimura`; toggle wallet seluruh group OFF), dan #26 (Device Allocation, Approvals, Wallet, TAG > Stock).
- Data Dinamis (Tabel Data Uji Dinamis #8): dua allocation `Waiting for Approval` di `Branch 1` tanpa GM (D1 untuk TC-AC-RP-366, D2 untuk TC-AC-RP-367) dibuat di hook `before` lewat seeding API (kemampuan disediakan tim BE/FE), identitas unik per run dengan suffix `+{runId}-109`; toggle `Branch 1` ON diatur di hook `before` (sesuai Precondition TC) dan toggle wallet `Region Jawa` ON diatur di hook `before` (Precondition e TC-AC-RP-368). Item Duplicate Identifier untuk TC-AC-RP-369 disediakan tim FE. Data dibersihkan di hook `after`.
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-366: Tanpa GM aktif, Total Control tetap dapat me-review

1. Buka Approvals > Device Allocation
2. Buka allocation D1 di `Branch 1`
3. Klik Approve
4. Verifikasi allocation D1 berstatus `Approved`
5. Verifikasi antrean tidak stuck: allocation D1 tidak lagi berada di antrean `Waiting for Approval`

### TC-AC-RP-367: GM baru setelah submit langsung berwenang (tanpa snapshot reviewer)

6. Buka halaman `Settings > Role & Permission`, lalu klik tab `Group Manager`
7. Assign Group Manager `Alex Tan` ke group `Branch 1`: klik `+ Assign`, pilih Group `Branch 1`, centang `Alex Tan`, lalu klik `[Assign]`
8. Tunggu aksi selesai (penugasan GM `Alex Tan` tersimpan)
9. Ganti akun: logout, lalu login sebagai `Alex Tan`
10. Buka Approvals > Device Allocation lalu buka allocation D2 di `Branch 1`
11. Klik Approve
12. Verifikasi Approve berhasil
13. Pulihkan baseline: penugasan GM `Alex Tan` di `Branch 1` dilepas

### TC-AC-RP-368: Toggle Manage wallet & pricing meng-gate Allocation Deposit

14. Ganti akun: logout, lalu login sebagai Group Role `Manage wallet & pricing` `Region Jawa` `John Dohan`
15. Buka menu Wallet
16. Ajukan Allocation Deposit ke entitas di group `Region Jawa`
17. Verifikasi pengajuan berstatus `Waiting for Approval` sebelum wallet didebit

### TC-AC-RP-369: Additional Approver Manage TAG stock mereview Duplicate Identifier tanpa akses TAG Stock

18. Ganti akun: logout, lalu login sebagai Additional Approver `Manage TAG stock` `Sarah Kimura`
19. Buka Approvals > TAG Stock
20. Verifikasi item Duplicate Identifier dapat di-Approve/Reject
21. Buka menu TAG > Stock
22. Verifikasi menu TAG > Stock tidak dapat diakses (tanpa capability terpisah)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 13 (pemulihan baseline tanpa `Verifikasi`); langkah "Tunggu aksi selesai" sebelum ganti akun (bagian 8b butir 8).
- TC-AC-RP-370 ada di spec 110 karena objek asersinya sesi `John Dohan` yang berjalan paralel (kelas c).
- Temuan untuk QA:
  - Email dan password akun Standard yang menjadi aktor (`Alex Tan`, `John Dohan`, `Sarah Kimura`) tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Data pembuatan allocation (jenis perangkat, stok, dan entitas tujuan di group yang disebut) tidak ditulis di TC; spec menulis "entitas di group X" apa adanya dan menyatakan data itu disediakan tim FE (S-11, S-13).
  - TC-AC-RP-366 Expected "antrean tidak stuck" tidak menyebut cara pengamatan; spec mengasersi allocation tidak lagi berada di antrean `Waiting for Approval`.
  - TC-AC-RP-367 dan TC-AC-RP-366 sama-sama memakai Tabel Data Uji Dinamis #8 (satu allocation); spec memakai dua allocation (D1, D2) supaya persetujuan TC-AC-RP-366 tidak menghabiskan allocation TC-AC-RP-367.
  - TC-AC-RP-368 Expected "sebelum wallet didebit" tidak punya langkah observasi saldo; spec hanya mengasersi status `Waiting for Approval`.
  - TC-AC-RP-369 tidak menyebut data Duplicate Identifier yang direview; item disediakan tim FE. Expected b "tidak dapat diakses" tidak menyebut bentuknya (menu Hidden atau halaman 403).
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
