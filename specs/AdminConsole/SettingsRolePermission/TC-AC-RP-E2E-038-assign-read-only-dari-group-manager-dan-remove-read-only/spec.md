---
id: TC-AC-RP-E2E-038-assign-read-only-dari-group-manager-dan-remove-read-only
title: "Assign Read Only dari Group Manager dan Remove Read Only (Cancel lalu Confirm)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-140
  - TC-AC-RP-142
  - TC-AC-RP-143
coverage:
  web: automated
---

# Assign Read Only dari Group Manager dan Remove Read Only (Cancel lalu Confirm)

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-140: Assign Read Only ke Group Manager melepas GM

1. Klik tab `Read Only`
2. Klik tombol "+ Assign"
3. Ketik Search `Fajar Nugroho`, tekan Enter
4. Centang `Fajar Nugroho`
5. Klik `[Assign]`
6. Verifikasi toast "Success, Read Only has been assigned."
7. Klik tab `Group Manager`
8. Verifikasi Tab Group Manager masih memuat baris `Jane Smith` — `Region Jawa`
9. Verifikasi kedua baris Group Manager `Fajar Nugroho` hilang dari Tab Group Manager
10. Pulihkan baseline: penugasan Group Manager `Fajar Nugroho` di `Region Jawa` dan `Sumatera` dikembalikan

### TC-AC-RP-143: Cancel dialog Remove Read Only

11. Klik tab `Read Only`
12. Klik `⋯` baris `Lisa Wong` lalu klik `Remove`
13. Klik `[Cancel]`
14. Verifikasi dialog tertutup
15. Verifikasi `Lisa Wong` tetap di Tab Read Only

### TC-AC-RP-142: Screening dan Confirm Remove Read Only

16. Klik `⋯` baris `Lisa Wong` lalu klik `Remove`
17. Verifikasi Title dialog "Remove Read Only"
18. Verifikasi body dialog memuat bullet • Lisa W, "This will remove Read Only from this user.", "Their individual roles will be reset and they will have no role assigned.", dan "Are you sure you want to remove it?"
19. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (destructive)
20. Klik `[Remove]`
21. Verifikasi toast "Success, Read Only has been removed."
22. Verifikasi baris `Lisa Wong` hilang dari Tab Read Only
23. Klik tab `System`
24. Klik `⋯` pada baris `Manage device master data` di section Global Role lalu klik `Detail`
25. Ketik Search `Lisa Wong`, tekan Enter
26. Verifikasi peran individual `Lisa Wong` direset: `Lisa Wong` tidak tampil di Role Detail `Manage device master data`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 10, 23 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 3, 25.
- Penyimpangan urutan (S-05, S-10): TC-AC-RP-143 (Cancel) diletakkan sebelum TC-AC-RP-142 (Confirm Remove, aksi yang menghapus data) dan TC-AC-RP-140 di awal karena memulihkan datanya sendiri.
- Pembanding absence: baris `Jane Smith` — `Region Jawa` (langkah 8) dan toast sukses (langkah 21) menjadi anchor positif sebelum asersi baris hilang.
- Temuan untuk QA:
  - TC-AC-RP-142 Expected "peran individualnya direset" tanpa langkah observasi di TC; spec mengamati ketiadaan `Lisa Wong` di Role Detail `Manage device master data` (langkah 24 sampai 26).
  - TC-AC-RP-140 tidak menyebut apakah ada toast atau Expected lain selain hilangnya baris GM; spec hanya mengasersi yang tertulis.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
