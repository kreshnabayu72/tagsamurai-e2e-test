---
id: TC-AC-RP-E2E-125-resilience-tulis-read-only-dan-group-manager
title: "Resilience Tulis: Assign dan Remove Read Only serta Assign dan Remove Group Manager Gagal 5xx"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-144
  - TC-AC-RP-145
  - TC-AC-RP-159
coverage:
  web: automated
---

# Resilience Tulis: Assign dan Remove Read Only serta Assign dan Remove Group Manager Gagal 5xx

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; respons submit dipaksa lewat `Spectra.intercept()` dan state tabel diasersi)
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (`Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal: `Default Group`, `Region A` dengan anak `Branch 1`, `Region Jawa` dengan anak `Jakarta` dan `Surabaya`, `Sumatera`), #12 (user Standard), #13 (pemegang Total Control dan Read Only), #14 (penugasan Group Manager), #15 (penugasan peran individual), dan #17 (approver dan toggle). Target aksi memakai user Pre-setup bernama literal sesuai TC karena data itu tidak dapat dimiliki spec; tidak ada Data Dinamis bersuffix `+{runId}-<NNN>` yang dibuat spec ini.
- Pemulihan state: intercept dilepas setelah tiap pemicu dan dipulihkan di hook `after`; kegagalan yang dipaksa tidak menyimpan perubahan sehingga data Pre-setup tidak berubah. Kemampuan reset baseline (suite.md) tetap dijalankan di hook `before` dan `after`.
- Failure injection lewat `Spectra.intercept()` pada respons jaringan (Tabel Data Uji Pre-setup #23): respons 5xx, penahanan respons, dan timeout atau koneksi terputus. Intercept dilepas segera setelah pemicu selesai dan dipulihkan di hook `after` bila spec gagal di tengah.
- Suite berjalan serial (`parallel: false`) karena spec mengubah state Pre-setup bersama.
- Env var `AC_RP_TC_PASSWORD` dipakai langkah login hook `before`; nama ini perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-144: Assign Read Only gagal 5xx

1. Klik tab `Read Only`
2. Klik tombol "+ Assign"
3. Ketik Search `Alex Tan`, tekan Enter
4. Centang `Alex Tan`
5. Atur intercept respons submit Assign Read Only menjadi 5xx
6. Klik `[Assign]`
7. Verifikasi toast "Error, failed to assign Read Only."
8. Verifikasi popup tetap terbuka
9. Verifikasi centangan `Alex Tan` dipertahankan
10. Lepas intercept 5xx
11. Klik `[Cancel]`

### TC-AC-RP-145: Remove Read Only gagal 5xx

12. Klik `⋯` baris `Lisa Wong` lalu klik `Remove`
13. Atur intercept respons Remove Read Only menjadi 5xx
14. Klik `[Remove]`
15. Verifikasi toast "Error, failed to remove Read Only."
16. Verifikasi dialog tetap terbuka tanpa perubahan
17. Verifikasi `[Remove]` aktif kembali
18. Lepas intercept 5xx
19. Klik `[Cancel]`

### TC-AC-RP-159: Assign dan Remove GM gagal 5xx

20. Klik tab `Group Manager`
21. Klik tombol "+ Assign"
22. Buka field Group lalu pilih node `Region A`
23. Ketik Search `John Dohan`, tekan Enter
24. Centang `John Dohan`
25. Atur intercept respons submit Assign Group Manager menjadi 5xx
26. Klik `[Assign]`
27. Verifikasi toast "Error, failed to assign Group Manager."
28. Verifikasi popup tetap terbuka
29. Verifikasi pilihan Group `Region A` dan centangan `John Dohan` dipertahankan
30. Lepas intercept 5xx
31. Klik `[Cancel]`
32. Klik `⋯` baris `Jane Smith` lalu klik `Remove`
33. Atur intercept respons Remove Group Manager menjadi 5xx
34. Klik `[Remove]`
35. Verifikasi toast "Error, failed to remove Group Manager."
36. Lepas intercept 5xx
37. Klik `[Cancel]`
38. Verifikasi baris `Jane Smith` tetap di Tab Group Manager

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, S-09): langkah 10, 11, 18, 19, 30, 31, 36, 37 (tanpa `Verifikasi`; menyiapkan, membersihkan, atau memulihkan state).
- Search untuk menemukan baris target (langkah penghubung, R-16): langkah 3, 23.
- Alasan sekitar 35 langkah: ketiga blok satu kelas harness (b, fault injection tulis Read Only dan Group Manager), berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; setiap blok membuka popup atau dialog sendiri dan menutupnya sebelum blok berikutnya.
- TC-AC-RP-159 Expected b "baris tetap" diasersi sesudah dialog ditutup (langkah penghubung `[Cancel]`) karena baris Tab Group Manager tidak dapat dibaca selama dialog menutupi halaman.
- Temuan untuk QA:
  - TC-AC-RP-144 dan 145 Expected tidak menyebut toast persisten atau tidak adanya status parsial; spec hanya mengasersi yang tertulis.
  - TC-AC-RP-159 Expected b tidak menyebut keadaan dialog sesudah Remove gagal; spec tidak mengasersi dialog dan menutupnya dengan `[Cancel]` sebagai langkah penghubung.
