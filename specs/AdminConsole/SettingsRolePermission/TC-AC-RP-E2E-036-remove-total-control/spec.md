---
id: TC-AC-RP-E2E-036-remove-total-control
title: "Remove Total Control: Screening Dialog, Cancel, Escape, Confirm Reset Peran, dan User Inactive"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-132
  - TC-AC-RP-133
  - TC-AC-RP-134
  - TC-AC-RP-135
  - TC-AC-RP-136
coverage:
  web: automated
---

# Remove Total Control: Screening Dialog, Cancel, Escape, Confirm Reset Peran, dan User Inactive

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: kemampuan reset data Pre-setup (tingkat akses dan penugasan Group Manager) ke kondisi Tabel Data Uji Pre-setup TC disediakan tim FE/BE dan dinyatakan di `suite.md`; dijalankan di hook `before` dan `after` serta sebagai langkah penghubung "Pulihkan baseline". Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-132: Screening dialog Remove Total Control

1. Klik `⋯` baris `John Doe` lalu klik `Remove`
2. Verifikasi Title dialog "Remove Total Control"
3. Verifikasi body dialog memuat bullet • John D, "This will remove Total Control from this user.", "Their individual roles will be reset and they will have no role assigned.", dan "Are you sure you want to remove it?"
4. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` (destructive)

### TC-AC-RP-134: Cancel dialog Remove Total Control

5. Klik `[Cancel]`
6. Verifikasi dialog tertutup
7. Verifikasi `John Doe` tetap di Tab Total Control
8. Klik tab `System`
9. Catat nilai kolom Users tiap baris pada section Global Role dan Group Role sebagai baseline
10. Klik `⋯` pada baris `Manage device master data` di section Global Role lalu klik `Detail`
11. Ketik Search `John Doe`, tekan Enter
12. Verifikasi baris `John Doe` tetap tampil di Role Detail `Manage device master data` sebagai peran individualnya yang tidak berubah
13. Buka halaman `Settings > Role & Permission`

### TC-AC-RP-135: Escape pada dialog Remove sama dengan Cancel

14. Klik `⋯` baris `John Doe` lalu klik `Remove`
15. Verifikasi fokus terkunci di dalam dialog selama terbuka
16. Tekan Escape
17. Verifikasi dialog tertutup tanpa perubahan
18. Verifikasi `John Doe` tetap di Tab Total Control

### TC-AC-RP-133: Confirm Remove Total Control mereset seluruh peran individual

19. Klik `⋯` baris `John Doe` lalu klik `Remove`
20. Klik `[Remove]`
21. Verifikasi toast "Success, Total Control has been removed."
22. Verifikasi baris `John Doe` hilang dari Tab Total Control
23. Klik tab `System`
24. Klik `⋯` pada baris `Manage device master data` di section Global Role lalu klik `Detail`
25. Ketik Search `John Doe`, tekan Enter
26. Verifikasi `John Doe` tidak tampil di Role Detail `Manage device master data`
27. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
28. Klik `⋯` pada baris `Manage distributor` di section Group Role lalu klik `Detail`
29. Ketik Search `John Doe`, tekan Enter
30. Verifikasi `John Doe` tidak tampil di Role Detail `Manage distributor`
31. Buka halaman `Settings > Role & Permission`, lalu klik tab `System`
32. Verifikasi nilai kolom Users setiap baris Global Role dan Group Role berkurang 1 dibanding baseline langkah 9

### TC-AC-RP-136: Remove Total Control pada user Inactive

33. Buka halaman `Settings > Role & Permission`
34. Klik `⋯` baris `Sarah Kim` lalu klik `Remove`
35. Klik `[Remove]`
36. Verifikasi toast "Success, Total Control has been removed."
37. Verifikasi baris `Sarah Kim` hilang dari Tab Total Control

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 8, 9, 13, 23, 27, 31, 33 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 11, 25, 29.
- Penyimpangan urutan (S-05, S-10): TC-AC-RP-134 dan 135 (Cancel dan Escape) diletakkan sebelum TC-AC-RP-133 dan 136 (aksi yang menghapus data); TC-AC-RP-133 sebelum TC-AC-RP-136 agar baseline kolom Users (langkah 9) belum terpengaruh Remove `Sarah Kim`. Dialog yang dibuka di langkah 1 dipakai bersama TC-AC-RP-132 dan 134.
- Alasan sekitar 35 langkah: semua blok berpusat pada satu aksi Remove Total Control, memakai data baris Total Control Pre-setup yang sama, dan Confirm Remove (TC-AC-RP-133) dan TC-AC-RP-136 diletakkan di akhir sebagai aksi yang menghapus data.
- Penghapusan `John Doe` (TC-AC-RP-133) dan `Sarah Kim` (TC-AC-RP-136) dipulihkan hook `after`.
- Temuan untuk QA:
  - TC-AC-RP-134 Expected "peran individualnya tidak berubah" tanpa langkah observasi di TC; spec mengamati baris `John Doe` di Role Detail `Manage device master data` (langkah 10 sampai 13).
  - TC-AC-RP-133 Expected c "Kolom Users berkurang 1 untuk setiap role" butuh baseline Users yang TC tidak sediakan; spec mencatatnya di langkah 9 dan membandingkannya (S-12).
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
