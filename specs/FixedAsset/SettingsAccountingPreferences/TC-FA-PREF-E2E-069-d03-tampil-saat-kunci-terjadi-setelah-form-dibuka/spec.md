---
id: TC-FA-PREF-E2E-069-d03-tampil-saat-kunci-terjadi-setelah-form-dibuka
title: "D-03 Tampil Saat Kunci Terjadi Setelah Form Dibuka (Posting Pertama, Soft Closed, Closed)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-PREF-251
  - TC-FA-PREF-252
  - TC-FA-PREF-253
coverage:
  web: automated
---

# D-03 Tampil Saat Kunci Terjadi Setelah Form Dibuka (Posting Pertama, Soft Closed, Closed)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup, company `PT Contoh Konstruksi`): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Accounting > Preferences). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`: didaftarkan tim FE. Password tidak ditulis di spec atau fixture.
- Data Pre-setup PB-1 (company `PT Contoh Konstruksi`, plan Growth, entitas Active; Preferences nilai awal: Fiscal Year Start January, First Accounting Period Mar 2026, Default Capitalization Threshold 5.000.000, In-service Date Source Activation date, Depreciation in Disposal Month Up to previous month, Default Gain/Loss on Disposal, Default Capitalization Offset dan Found Asset Credit Account kosong, Disposal Documents semua jenis Optional, Journal Grouping Group; periode Mar 2026 sampai Dec 2026 Open; belum ada penyusutan diposting) dan PB-2 (akun Chart of Accounts uji). Fiscal Year Start dan First Accounting Period tidak terkunci saat form dibuka.
- Seed dan pemulihan lewat API (Preferences ke nilai awal, Asset Class, pelepasan, akun Chart of Accounts, penguncian) disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`); tiap TC dijalankan dari keadaan awal yang dinyatakan di Precondition TC-nya.
- Identitas data Pre-setup dibaca dari `fixtures/settings-accounting-preferences.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE). Nama akun dan Asset Class ditulis seperti di TC.
- Flag Guided Tooltip halaman Preferences: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Sesi API aktor untuk pemicu perubahan state (fixture BE): kemampuan disediakan tim BE/FE (butir "Sesi API aktor" di `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-PREF-251: D-03 tampil saat posting penyusutan pertama terjadi setelah form dibuka

1. Ubah Select Fiscal Year Start dari "January" menjadi "July"
2. Klik [Save changes] sampai dialog D-01 tampil
3. Lewat sesi API (fixture BE), tandai posting penyusutan pertama pada Asset Class IT Equipment hingga status tersimpan
4. Klik [Save] pada dialog D-01
5. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tampil
6. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
7. Verifikasi dialog D-03 hanya memuat tombol [OK]
8. Verifikasi tidak ada toast yang tampil bersama D-03
9. Verifikasi dialog D-01 tidak lagi tampil
10. Klik [OK] pada dialog D-03
11. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-252: D-03 tampil saat satu periode menjadi Soft Closed setelah form dibuka

12. Ubah Select bulan First Accounting Period dari "March" menjadi "January"
13. Klik [Save changes] sampai dialog D-01 tampil
14. Lewat sesi API (fixture BE), ubah status periode Mar 2026 menjadi Soft Closed hingga status tersimpan
15. Klik [Save] pada dialog D-01
16. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tampil
17. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
18. Verifikasi dialog D-03 hanya memuat tombol [OK]
19. Verifikasi tidak ada toast yang tampil bersama D-03
20. Verifikasi dialog D-01 tidak lagi tampil
21. Klik [OK] pada dialog D-03
22. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

### TC-FA-PREF-253: D-03 tampil saat satu periode menjadi Closed setelah form dibuka

23. Ubah Select Fiscal Year Start dari "January" menjadi "April"
24. Klik [Save changes] sampai dialog D-01 tampil
25. Lewat sesi API (fixture BE), ubah status periode Mar 2026 menjadi Closed hingga status tersimpan
26. Klik [Save] pada dialog D-01
27. Verifikasi dialog D-03 berjudul "Cannot Save Preferences" tampil
28. Verifikasi body dialog D-03: "Fiscal Year Start and First Accounting Period are locked because depreciation has been posted or a period has been closed. The page has been reloaded with the latest lock status."
29. Verifikasi dialog D-03 hanya memuat tombol [OK]
30. Verifikasi tidak ada toast yang tampil bersama D-03
31. Verifikasi dialog D-01 tidak lagi tampil
32. Klik [OK] pada dialog D-03
33. Pulihkan kunci dan Preferences ke PB-1 lewat seed API, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): klik [OK] pada D-03 dan pemulihan kunci di akhir tiap TC. Pemicu kunci lewat sesi API aktor (fixture BE); dialog D-01 yang tampil menjadi wait eksplisit pada langkah Save changes sebelum pemicu.
- Asersi tidak ada toast pada D-03 didahului Verifikasi D-03 tampil sebagai anchor.
- Temuan untuk QA:
  - Post Condition "Preferences company belum berubah ..." tidak punya langkah observasi di TC ini, sehingga tidak diasersi (S-01).
