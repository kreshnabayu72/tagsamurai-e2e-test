---
id: TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager
title: "Add: Alert Info dan Bypass Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-140
  - TC-AC-CS-141
  - TC-AC-CS-144
  - TC-AC-CS-143
coverage:
  web: automated
---

# Add: Alert Info dan Bypass Group Manager

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Group Manager scope Group `Jawa`, Distributor PT Maju Bersama (Pre-setup #5) `groupManagerSub_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`), password `Spectra.env.AC_SUB_GM_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Pre-setup #1).
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before`. Jam dipulihkan lewat fixture waktu pada langkah 27 sebelum aktor membuka Changelog (S-09) dan sekali lagi di hook `after` (kemampuan disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`): Client `Client Tanpa Subscription A+{runId}-035` dan `Client Tanpa Subscription B+{runId}-035` (padanan Pre-setup #48: binaan langsung PT Maju Bersama pada group `Jawa`, tanpa term dan tanpa trial, dengan Default User beralamat email yang dibaca lewat `Fixture.license-allocation-subscription`).
- State global yang diubah (suite serial) dan pemulihannya di hook `after` lewat fixture BE (disediakan tim FE/BE): toggle `Require Approval for Allocation` PT Maju Bersama (Pre-setup #23) diatur ON (bypass Group Manager aktif) lalu dipulihkan; saldo `Main Pocket` $25,000.00 (Pre-setup #20) berkurang oleh Capture dan Reserve pada TC-AC-CS-143 dan 144 lalu dipulihkan; harga SAMS Growth $3,000.00 per tahun (Pre-setup #27).
- Kemampuan teknis (disediakan tim FE/BE): membaca saldo `Main Pocket`, Reserve, dan Capture Wallet; membaca status App Access Client; kemampuan mail-catcher untuk membaca jumlah email per alamat (baseline sebelum aksi, R-11); fixture waktu. Efek: term dan entri Changelog Client seed ditambahkan oleh spec ini.

## Test Steps

### TC-AC-CS-140: Alert info efek langsung

1. Klik `[+ Subscription]`
2. Pilih Client `Client Tanpa Subscription A+{runId}-035`, Product `FAMS`, Plan `Professional`, Duration `1`, Start Date `19/08/26`
3. Verifikasi Alert info di atas footer "Takes effect immediately on 19/08/26." mengikuti template "Takes effect immediately on {Start Date}."

### TC-AC-CS-141: Alert info efek terjadwal

4. Ganti Start Date menjadi `15/09/26`
5. Verifikasi Alert info di atas footer "Scheduled to take effect on 15/09/26." mengikuti template "Scheduled to take effect on {Start Date}."
6. Klik `[Clear Field]`

### TC-AC-CS-144: Add mode New oleh Group Manager dengan Start Date masa depan menjadi Pending dengan Reserve ditahan

7. Catat baseline saldo `Main Pocket` dan jumlah email ke alamat Default User Client `Client Tanpa Subscription B+{runId}-035` (pembacaan lewat fixture BE dan mail-catcher)
8. Pilih Client `Client Tanpa Subscription B+{runId}-035`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `15/09/26`
9. Klik `[Submit]`
10. Verifikasi toast sukses "Success, subscription has been added." muncul
11. Ketik Search `Client Tanpa Subscription B+{runId}-035`, tekan Enter
12. Verifikasi baris baru berstatus Pending dengan Start Date `15/09/26` dan End Date `14/09/27`
13. Verifikasi Reserve $3,000.00 ditahan pada `Main Pocket` dan belum ada Capture
14. Verifikasi Activation Email belum dikirim (jumlah email ke alamat Default User sama dengan baseline)
15. Verifikasi App Access belum dikirim (dibaca lewat fixture BE)
16. Klik `(←)` pada kotak Search, lalu pulihkan saldo `Main Pocket` ke $25,000.00 tanpa Reserve lewat fixture BE

### TC-AC-CS-143: Add mode New oleh Group Manager (bypass) dengan Start Date hari ini langsung Active

17. Klik `[+ Subscription]`
18. Pilih Client `Client Tanpa Subscription A+{runId}-035`, Product `SAMS`, Plan `Growth`, Duration `1`, Start Date `19/08/26`
19. Klik `[Submit]`
20. Verifikasi toast sukses "Success, subscription has been added." muncul
21. Verifikasi modal tertutup
22. Ketik Search `Client Tanpa Subscription A+{runId}-035`, tekan Enter
23. Verifikasi baris baru di tab `Current` berstatus Active, bukan Waiting for Approval
24. Verifikasi baris baru memiliki Start Date `19/08/26` dan End Date `18/08/27`
25. Verifikasi Plan Owner `PT Maju Bersama (Distributor)`
26. Verifikasi Wallet `Main Pocket` di-Reserve lalu di-Capture $3,000.00 sehingga saldo menjadi $22,000.00 (dibaca lewat fixture BE; saldo awal $25,000.00 dipulihkan pada langkah 16)
27. Pulihkan jam server dan jam browser ke waktu nyata lewat fixture waktu
28. Klik `(←)` pada kotak Search, lalu klik `Changelog` di toolbar
29. Ketik Search `Client Tanpa Subscription A+{runId}-035` pada modal Changelog, tekan Enter
30. Verifikasi entri Changelog dengan Action `Add Subscription`
31. Verifikasi Field `Plan` pada entri itu
32. Verifikasi Old `—` pada entri itu
33. Verifikasi New `Growth` pada entri itu
34. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC-AC-CS-144 sebelum TC-AC-CS-143 agar TC dengan pembacaan Changelog dan pemulihan jam berada di akhir (S-09, S-10).
- Langkah penghubung (S-03): `[Clear Field]` (langkah 6), Search untuk menemukan baris target (R-16; langkah 11, 22, 29), `(←)` pada kotak Search (langkah 16, 28), baseline email dan saldo (langkah 7), pemulihan jam (langkah 27), dan menutup modal Changelog (langkah 34).
- Pada Expected TC-AC-CS-143 c, "tidak ada siklus approval" diasersi lewat status Active (langkah 23); Reserve lalu Capture diasersi dari saldo akhir (langkah 26).
- Baseline Changelog (S-12): entri dicari lewat nama Client seed bersuffix (baseline nol).
- Spec berada di bawah sekitar 35 langkah dengan satu kelas (fungsional Add oleh Group Manager).
- Temuan untuk QA:
  - TC-AC-CS-140 sampai 143 menyebut "Bypass GM aktif" tanpa menyatakan cara mengaturnya; toggle `Require Approval for Allocation` ON (Pre-setup #23) diatur lewat fixture BE.
  - TC-AC-CS-144 Expected d "Activation Email dan App Access belum dikirim" tidak menyebut cara cek; spec memakai mail-catcher dan pembacaan App Access lewat fixture BE.
  - TC-AC-CS-143 Expected d menulis Changelog tanpa menyebut Date entri; spec tidak mengasersi kolom Date.
