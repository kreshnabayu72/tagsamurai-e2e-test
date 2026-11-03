---
id: TC-AC-ACTS-E2E-120-add-stock-gps-partial-register-bentuk-tunggal-continue-dan-semua-waiting
title: "Add Stock GPS: Dialog Partial Register Bentuk Tunggal, Continue Mendaftarkan OK dan Mengirim Waiting, serta Submit Semua Waiting"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-807
  - TC-AC-ACTS-263
  - TC-AC-ACTS-264
coverage:
  web: automated
---

# Add Stock GPS: Dialog Partial Register Bentuk Tunggal, Continue Mendaftarkan OK dan Mengirim Waiting, serta Submit Semua Waiting

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Unit `356938035643815` yang didaftarkan langkah 8 dan Subject yang dibuat langkah 8 dan 15 dihapus lewat fixture BE di hook `after`.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah unit Available SKU, jumlah Subject Register Duplicate pending, dan jumlah baris Event Log SKU (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-807: Dialog Partial Register memakai bentuk tunggal untuk kedua kalimat

1. Catat baseline jumlah unit Available SKU, jumlah Subject pending, dan jumlah baris Event Log SKU
2. Tambahkan IMEI baru `356938035643815` dan IMEI existing `356938035643810` lewat Manual Entry
3. Klik `[Submit]`
4. Verifikasi dialog `Partial Register`: "1 IMEI matched an existing record and will be sent for approval. Register the remaining 1 IMEI?" dengan `[Cancel]` dan `[Continue]`
5. Verifikasi belum ada data yang ditulis pada titik ini (selisih nol terhadap baseline)
6. Klik `[Cancel]` pada dialog Partial Register

### TC-AC-ACTS-263: Partial Register, [Continue] mendaftarkan OK dan mengirim Waiting ke approval

7. Klik `[Submit]`
8. Klik `[Continue]` pada dialog Partial Register
9. Verifikasi toast "Success, TAG has been registered."
10. Verifikasi halaman menavigasi ke Detail SKU > Tab Available SKU itu
11. Verifikasi unit OK `356938035643815` terdaftar sebagai unit Available baru dengan TAG Code baru
12. Verifikasi Subject Waiting untuk `356938035643810` dibuat (jumlah Subject pending bertambah 1 terhadap baseline)

### TC-AC-ACTS-264: Submit semua baris Waiting dikirim ke approval tanpa dialog

13. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
14. Tambahkan dua IMEI existing `356938035643810` dan `356938035643815` lewat Manual Entry
15. Klik `[Submit]`
16. Verifikasi toast "Success, 2 TAGs have been sent for approval."
17. Verifikasi tidak ada dialog `Partial Register`
18. Verifikasi halaman menavigasi ke Detail SKU > Tab Available SKU itu

## Notes

- Mode: FE+BE.
- Urutan TC: TC-AC-ACTS-807 lebih dulu karena dialog bentuk tunggal tidak menulis data dan Preview campurannya dipakai ulang oleh TC-AC-ACTS-263; TC-AC-ACTS-264 terakhir karena memakai unit `356938035643815` yang didaftarkan TC-AC-ACTS-263 sebagai IMEI existing (S-10).
- Langkah penghubung tanpa Verifikasi (S-03): langkah mencatat baseline (S-12), `[Cancel]` pada dialog TC-AC-ACTS-807 sebelum TC-AC-ACTS-263 menjalankan langkahnya sendiri, dan langkah buka kembali halaman Add Stock.
- Verifikasi tanpa dialog `Partial Register` pada TC-AC-ACTS-264 didahului toast sukses sebagai anchor positif (8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-263 menyebut "Subject Waiting dibuat dalam satu transaksi"; "satu transaksi" tidak teramati dari UI sehingga hanya keberadaan unit OK dan Subject yang diasersi.
  - Distributor tidak memiliki menu Approvals; Subject dibaca lewat kemampuan baca disediakan tim FE/BE.
