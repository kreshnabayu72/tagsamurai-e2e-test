---
id: TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive
title: "Assign Total Control: Cascade Group Role, Beberapa User Satu Toast, User Pending Activation dan Inactive"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-123
  - TC-AC-RP-124
  - TC-AC-RP-127
  - TC-AC-RP-416
coverage:
  web: automated
---

# Assign Total Control: Cascade Group Role, Beberapa User Satu Toast, User Pending Activation dan Inactive

## Prerequisites

- Mode: FE+BE (backend nyata)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), dan #12 (user Standard). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan baseline: data Pre-setup (tingkat akses dan penugasan Group Manager) dipulihkan ke kondisi Tabel Data Uji Pre-setup TC; kemampuan reset dinyatakan di `suite.md` (Pemulihan baseline automation); dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC. Efek yang tidak dipulihkan: Modified By dan Last Updated baris yang disentuh serta entri audit trail (Changelog, System Log, Activity Log) bertambah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-123: Assign Total Control mengisi seluruh Group Role untuk group yang ada

1. Klik tombol "+ Assign"
2. Ketik Search `Alex Tan`, tekan Enter
3. Centang `Alex Tan`
4. Klik `[Assign]`
5. Klik tab `System`
6. Klik `⋯` pada baris `Manage distributor` di section Group Role lalu klik `Detail`
7. Ketik Search `Alex Tan`, tekan Enter
8. Verifikasi `Alex Tan` tampil satu baris per group yang ada (`Default Group`, `Region A`, `Branch 1`, `Region Jawa`, `Jakarta`, `Surabaya`, `Sumatera`) dengan C/R/U/D tercentang
9. Pulihkan baseline: `Alex Tan` kembali Standard
10. Buka halaman `Settings > Role & Permission`

### TC-AC-RP-124: Assign Total Control ke beberapa user memancarkan satu toast

11. Klik tombol "+ Assign"
12. Ketik Search `Alex Tan`, tekan Enter
13. Centang `Alex Tan`
14. Ganti isi kotak search dengan `Sarah Kimura`, tekan Enter
15. Centang `Sarah Kimura`
16. Tunggu toast lama hilang otomatis
17. Klik `[Assign]`
18. Verifikasi hanya satu toast yang tampil
19. Verifikasi teks toast "Success, Total Control has been assigned." (tanpa bentuk jamak)
20. Verifikasi `Alex Tan` dan `Sarah Kimura` muncul di Tab Total Control

### TC-AC-RP-127: Assign Total Control ke user Pending Activation

21. Klik tombol "+ Assign"
22. Ketik Search `Maya Putri`, tekan Enter
23. Centang `Maya Putri`
24. Klik `[Assign]`
25. Verifikasi toast "Success, Total Control has been assigned."
26. Verifikasi baris `Maya Putri` tampil di Tab Total Control
27. Verifikasi Status baris `Maya Putri` bernilai `Active`

### TC-AC-RP-416: Assign Total Control ke user Inactive

28. Klik tombol "+ Assign"
29. Ketik Search `Teguh Santoso`, tekan Enter
30. Centang `Teguh Santoso`
31. Klik `[Assign]`
32. Verifikasi toast "Success, Total Control has been assigned."
33. Verifikasi baris `Teguh Santoso` tampil di Tab Total Control
34. Verifikasi Status baris `Teguh Santoso` bernilai `Inactive`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 5, 9, 10, 16 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state; langkah 5 membuka tab `System` sebagai navigasi menuju Role Detail).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 2, 7, 12, 14, 22, 29.
- Pemulihan baseline: setelah TC-AC-RP-123 `Alex Tan` dipulihkan (langkah 9) karena TC-AC-RP-124 memakai user yang sama; hasil TC-AC-RP-124, 127, dan 416 (user berbeda) dipulihkan hook `after`.
- TC-AC-RP-122 ada di spec 034 (Role Detail seluruh Global Role); TC-AC-RP-123 memeriksa Role Detail Group Role `Manage distributor`.
- Temuan untuk QA:
  - TC-AC-RP-124 tidak menyatakan apakah seleksi bertahan saat isi kotak Search diganti; spec mengikuti TC dan mencentang kedua user bergantian dengan Search (S-15).
  - TC-AC-RP-127 Expected menyebut Status `Active` untuk user Pending Activation tanpa menjelaskan sumber perubahan status; spec mengikuti TC.
  - Target aksi tulis memakai data Pre-setup bersama bernama literal, bukan data bersuffix milik spec: TC tidak menyediakan data target alternatif, dan mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD (S-06, S-13); dicatat sebagai kemampuan yang disediakan tim FE/BE.
