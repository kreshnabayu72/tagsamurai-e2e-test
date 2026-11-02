---
id: TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan
title: "Renew: Efek Langsung, Terjadwal, dan Change Plan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-149
  - TC-AC-CS-150
  - TC-AC-CS-152
  - TC-AC-CS-148
coverage:
  web: automated
---

# Renew: Efek Langsung, Terjadwal, dan Change Plan

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email akun dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan yang didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`); hook `beforeEach` suite, flag Guided Tooltip `seen`, sesi API aktor, dan fixture pemulihan state Pre-setup mengikuti `suite.md` (hook suite).
- Tanggal acuan uji `19/08/26` (Pre-setup #28): jam server dan jam browser diatur absolut ke `19/08/26` di hook `before`. Jam dipulihkan lewat fixture waktu pada langkah 37 sebelum aktor membuka Changelog (S-09) dan sekali lagi di hook `after` (kemampuan disediakan tim FE/BE).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`, beserta term successor yang dibuat spec):
  - TC-AC-CS-149: Client `Bengkel Maju Jaya+{runId}-040`, SAMS plan Growth, status Expired, 19/08/25 sampai 18/08/26, Grace End 17/09/26, Plan Owner CV Karya Mandiri (Partner), tanpa successor (padanan Pre-setup #50).
  - TC-AC-CS-150: Client `CV Mitra Sejati+{runId}-040`, FAMS Custom Plan `Mitra Premium` (badge Custom), status Grace, 01/08/25 sampai 31/07/26, Grace End 30/08/26, Plan Owner PT ABC (Principal), tanpa successor (padanan Pre-setup #51).
  - TC-AC-CS-152: Client `Salon Cantik Indah+{runId}-040`, SAMS plan Growth, status Active, 19/08/26 sampai 18/08/27, Plan Owner PT Maju Bersama (Distributor), tanpa successor dan tanpa trial aktif (padanan Pre-setup #63).
  - TC-AC-CS-148: Client `Warung Kopi Senja+{runId}-040`, FAMS plan Professional, status Active, 01/09/25 sampai 31/08/26, Plan Owner PT Maju Bersama (Distributor), tanpa successor (padanan Pre-setup #69).
- State global: toggle `Require Approval for Allocation` tidak berlaku untuk Principal (Pre-setup #23, tidak diubah). Tidak ada perubahan Wallet (aktor Principal).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu. Efek: entri Changelog Client seed ditambahkan oleh spec ini.

## Test Steps

### TC-AC-CS-149: Renew atas predecessor Expired mulai hari submit dan predecessor menjadi Renewed

1. Ketik Search `Bengkel Maju Jaya+{runId}-040`, tekan Enter
2. Klik ikon `⋯` pada baris term Expired, lalu pilih `Renew`
3. Pilih Renewal Option `Keep current plan`, lalu isi Duration `1`
4. Klik `[Submit]`
5. Verifikasi toast sukses "Success, subscription has been renewed." muncul
6. Verifikasi term baru berstatus Active dengan Start Date `19/08/26` (hari submit, tidak retroaktif) dan End Date `18/08/27`
7. Klik `(←)` pada kotak Search, lalu klik tab `History`
8. Ketik Search `Bengkel Maju Jaya+{runId}-040`, tekan Enter
9. Verifikasi predecessor berstatus Renewed dan tampil di tab `History`
10. Klik `(←)` pada kotak Search, lalu klik tab `Current`

### TC-AC-CS-150: Renew Change plan atas predecessor Grace memakai plan baru

11. Ketik Search `CV Mitra Sejati+{runId}-040`, tekan Enter
12. Klik ikon `⋯` pada baris term Grace, lalu pilih `Renew`
13. Pilih Renewal Option `Change plan`, pilih Plan `Growth`, lalu isi Duration `1`
14. Klik `[Submit]`
15. Verifikasi toast sukses "Success, subscription has been renewed." muncul
16. Verifikasi term baru Plan `Growth` berstatus Active mulai `19/08/26`
17. Klik `(←)` pada kotak Search, lalu klik tab `History`
18. Ketik Search `CV Mitra Sejati+{runId}-040`, tekan Enter
19. Verifikasi predecessor Custom Plan berstatus Renewed
20. Klik `(←)` pada kotak Search, lalu klik tab `Current`

### TC-AC-CS-152: Change plan ke rank lebih tinggi diizinkan

21. Ketik Search `Salon Cantik Indah+{runId}-040`, tekan Enter
22. Klik ikon `⋯` pada baris term Active, lalu pilih `Renew`
23. Pilih Renewal Option `Change plan`, pilih Plan `Enterprise`, lalu isi Duration `1`
24. Klik `[Submit]`
25. Verifikasi Submit berhasil tanpa pembatasan arah rank
26. Verifikasi toast sukses "Success, your renewal has been scheduled and will take effect on 19/08/27."
27. Verifikasi term baru memakai Plan `Enterprise` berstatus Pending dengan tanggal `19/08/27` sampai `18/08/28`
28. Verifikasi predecessor term Active tetap berstatus Active
29. Klik `(←)` pada kotak Search

### TC-AC-CS-148: Renew Keep current plan atas predecessor Active menjadi Pending terjadwal

30. Ketik Search `Warung Kopi Senja+{runId}-040`, tekan Enter
31. Klik ikon `⋯` pada baris term Active, lalu pilih `Renew`
32. Pilih Renewal Option `Keep current plan`, lalu isi Duration `1`
33. Klik `[Submit]`
34. Verifikasi toast sukses "Success, your renewal has been scheduled and will take effect on 01/09/26." mengikuti template "Success, your renewal has been scheduled and will take effect on [date]."
35. Verifikasi term baru berstatus Pending dengan Start Date `01/09/26` dan End Date `31/08/27`
36. Verifikasi predecessor tetap Active dan tidak disentuh
37. Klik `(←)` pada kotak Search, lalu pulihkan jam server dan jam browser ke waktu nyata lewat fixture waktu
38. Klik `Changelog` di toolbar, lalu ketik Search `Warung Kopi Senja+{runId}-040` pada modal Changelog, tekan Enter
39. Verifikasi entri Changelog dengan Action `Schedule Renewal (efek terjadwal, submit)`
40. Verifikasi Field `Pending Renewal` pada entri itu
41. Verifikasi Old `—` pada entri itu
42. Verifikasi New `Professional, effective 01/09/26` pada entri itu
43. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-CS-148 berada paling akhir karena memuat pembacaan Changelog yang menuntut jam dipulihkan lebih dulu (S-09); nomor TC tidak berurutan.
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16; langkah 1, 8, 11, 18, 21, 30, 38), `(←)` pada kotak Search dan pindah tab (langkah 7, 10, 17, 20, 29, 37), pemulihan jam (langkah 37), dan menutup modal Changelog (langkah 43).
- Baseline Changelog (S-12): entri dicari lewat nama Client seed bersuffix (baseline nol).
- Ukuran: 43 langkah, di atas 35 langkah. Alasan pertahanan: semua blok satu kelas (fungsional Renew oleh Principal), tiap blok memakai Client seed sendiri dan tidak bergantung pada blok lain, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; pemecahan lebih lanjut menambah login dan hook tanpa menambah isolasi.
- Temuan untuk QA:
  - TC-AC-CS-149 dan TC-AC-CS-150 Expected tidak menyebut tab tempat predecessor Renewed dan Custom Plan; TC-AC-CS-149 menyebut tab `History`, TC-AC-CS-150 tidak (spec mencarinya di tab `History`, konsisten dengan TC-AC-CS-149).
  - TC-AC-CS-148 Precondition "Toggle OFF atau bypass TC" tidak berlaku bagi Principal; tidak ada langkah pengaturan toggle.
  - TC-AC-CS-152 memakai Plan `Enterprise` untuk Product SAMS padahal Data Uji Pre-setup #27 hanya menyebut SAMS Growth dan Professional; mengikuti TC.
