---
id: TC-AC-ACTS-E2E-100-approvals-duplicate-scan-ulang-identifier-rejected-dan-constraint-unique-status-live
title: "Approvals Duplicate: Scan Ulang Identifier Unit Rejected Terdaftar sebagai Unit Baru dan Constraint UNIQUE Hanya untuk Status Live"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-303
  - TC-AC-ACTS-742
coverage:
  web: automated
---

# Approvals Duplicate: Scan Ulang Identifier Unit Rejected Terdaftar sebagai Unit Baru dan Constraint UNIQUE Hanya untuk Status Live

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `NFC-CARD-BETA-N2` (dari Stock List lewat row action Add Stock), dibuka oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d (harness eksternal): simulator reader NFC (scan satu per satu, `[Add by Scan]`, `[Stop]`) disediakan tim FE; mekanismenya tidak dikarang di spec.
- SKU `NFC-CARD-BETA-N2` (Data Pre-setup #13). UID Data Dinamis #4: `A1B2C3D4E5F7` hanya dipegang unit Rejected R (TC-AC-ACTS-303 dan TC-AC-ACTS-742); UID `A1B2C3D4E5F8` dipegang unit Available A dan unit Waiting for Approval W dengan Subject pending dari scan sebelumnya (TC-AC-ACTS-742). Identifier tetap tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini; unit baru yang didaftarkan spec ini dihapus lewat fixture BE di hook `after`. Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca Total Registered SKU dan jumlah Subject Tab Active (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-303: Identifier unit Rejected terdaftar normal sebagai unit baru pada scan ulang

1. Catat baseline Total Registered SKU `NFC-CARD-BETA-N2` dan jumlah Subject di Approvals > TAG Stock > Tab Active
2. Klik `[Add by Scan]`
3. Scan UID `A1B2C3D4E5F7` lewat simulator reader NFC
4. Klik `[Stop]`
5. Verifikasi baris berstatus OK (success)
6. Hover badge OK pada baris itu
7. Verifikasi tooltip match tidak tampil
8. Klik `[Submit]`
9. Verifikasi toast "Success, TAG has been registered."
10. Verifikasi tanpa dialog `Partial Register`
11. Verifikasi unit baru berstatus Available dengan TAG Code baru
12. Verifikasi Total Registered SKU bertambah 1 terhadap baseline
13. Buka Approvals > TAG Stock > Tab Active
14. Verifikasi tidak ada Subject baru di Tab Active (jumlah Subject tidak berubah terhadap baseline)
15. Buka Tab History
16. Verifikasi Subject lama tetap di Tab History dengan Approval `Rejected`
17. Verifikasi unit Rejected tetap tanpa TAG Code (TAG Code `—`)

### TC-AC-ACTS-742: Constraint UNIQUE identifier hanya untuk status live, unit Rejected dan Waiting bukan target match

18. Ganti akun: klik Logout
19. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
20. Buka halaman Add Stock SKU `NFC-CARD-BETA-N2` dari Stock List lewat row action Add Stock
21. Klik `[Add by Scan]`, scan UID `A1B2C3D4E5F7`, klik `[Stop]`, klik `[Submit]`
22. Verifikasi toast "Success, TAG has been registered."
23. Verifikasi tidak ada toast error konflik unik ("Error, failed to register TAGs.")
24. Buka Detail SKU `NFC-CARD-BETA-N2` > Tab Available
25. Verifikasi unit baru terdaftar OK dengan TAG Code baru untuk UID `A1B2C3D4E5F7`
26. Buka kembali halaman Add Stock SKU `NFC-CARD-BETA-N2` (Stock List, row action Add Stock)
27. Klik `[Add by Scan]`, scan UID `A1B2C3D4E5F8`, klik `[Stop]`
28. Verifikasi baris berstatus Waiting for Approval
29. Klik `[Submit]`
30. Tunggu aksi selesai (Preview kosong dan tombol `[Submit]` aktif kembali atau halaman berpindah)
31. Ganti akun: klik Logout
32. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`)
33. Buka Approvals > TAG Stock > Tab Active
34. Verifikasi Subject baru dibuat untuk UID `A1B2C3D4E5F8`
35. Klik `Review` pada Subject baru
36. Verifikasi blok Existing Record menunjuk unit A (Available), bukan unit W (Waiting) maupun unit R (Rejected)
37. Klik `[Cancel]`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu kelas harness (kelas d, simulator reader NFC) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-303 (Total Control) lebih dulu dan TC-AC-ACTS-742 (Distributor, lalu Total Control untuk membaca Approvals) terakhir (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), langkah ganti akun, buka halaman, dan `[Cancel]` menutup dialog Review.
- Asersi absence tooltip match (TC-AC-ACTS-303) dan absence toast error konflik (TC-AC-ACTS-742) didahului anchor positif (baris OK tampil; toast sukses tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-742 menyebut "berdampingan dengan unit Rejected R pada UID yang sama" yang tidak teramati dari UI; spec mengasersi unit baru Available dengan TAG Code baru dan tidak adanya toast error konflik unik.
  - TC-AC-ACTS-742 menyebut Reader NFC terhubung tanpa menyebut cara simulasi.
