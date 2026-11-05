---
id: TC-AC-LA-E2E-047-submit-allocation-id-top-up-dan-pay-from-partner
title: "Submit Allocate: Format Allocation ID, Top-up Berulang, dan Pay From Partner"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-168
  - TC-AC-LA-169
  - TC-AC-LA-171
coverage:
  web: automated
---

# Submit Allocate: Format Allocation ID, Top-up Berulang, dan Pay From Partner

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Partner multi kantong `partnerMultiLic_automated_{namaCompany}@qwertysystem.net` (`Budi Santoso`, Pre-setup #16), password `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), PT Abadi Jaya (#25, `SUBS-20260110-C1D2E`), kantong wallet (#33), Product Price (#34: Concurrent User $365 per unit per tahun). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Jam (nilai absolut, disediakan tim FE/BE): tanggal server uji 22 Dec 2026 di hook `before`; digeser ke 23 Dec 2026 pada langkah 9 dan tetap sampai akhir spec. Jam server dan jam browser diatur bersama dan dipulihkan di hook `after`. Counter harian Allocation ID untuk 22 Dec 2026 dan 23 Dec 2026 dalam keadaan nol (direset baseline automation sebelum spec; lihat Temuan untuk QA).
- Data Dinamis: tiga alokasi Concurrent User +1 ke PT Sejahtera (dua pada 22 Dec 2026, satu pada 23 Dec 2026), dua top-up +5 ke PT Sejahtera, dan satu alokasi +2 ke PT Abadi Jaya (Pay From `PT ABC (Principal)`). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger kuota dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: daftar Allocation ID baris di halaman pertama tab Current dan saldo kantong dicatat sebelum tiap blok.
- Kemampuan teknis: membaca saldo kedua kantong sumber Partner (disediakan tim FE/BE); menampilkan kolom Paid From lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-168: Allocation ID memakai format LALC-YYYYMMDD-XXXXX dengan counter harian

1. Klik `[+ Allocation]`
2. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
3. Klik `[Submit]`
4. Verifikasi Allocation ID baris baru `LALC-20261222-00001`
5. Klik `[+ Allocation]`
6. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
7. Klik `[Submit]`
8. Verifikasi Allocation ID baris baru `LALC-20261222-00002`
9. Geser jam server dan jam browser ke 23 Dec 2026, lalu buka ulang Allocation > License Allocation tab Current
10. Klik `[+ Allocation]`
11. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `1`
12. Klik `[Submit]`
13. Verifikasi Allocation ID baris baru `LALC-20261223-00001` (counter reset harian)

### TC-AC-LA-169: Top-up berulang pada Type yang sama menambah saldo ledger term

14. Klik `[+ Allocation]`
15. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `5`, lalu catat Current Quota
16. Klik `[Submit]`
17. Tunggu modal tertutup, lalu catat baseline Allocation ID baris di halaman pertama tab Current
18. Klik `[+ Allocation]`
19. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`
20. Verifikasi Current Quota form kedua menampilkan saldo kumulatif term (naik 5 dari nilai langkah 15)
21. Isi Additional Quantity `5`
22. Klik `[Submit]`
23. Verifikasi tidak ada penolakan duplikat (tidak ada pesan galat atau toast galat)
24. Verifikasi alokasi kedua tercatat sebagai baris baru dengan Allocation ID berbeda (tidak ada pada baseline langkah 17)

### TC-AC-LA-171: Partner dengan beberapa kantong mendebit kantong yang dipilih pada Pay From

25. Ganti akun: logout `Dewi A`, login sebagai `Budi Santoso` dengan `Spectra.env.AC_LA_PARTNER_MULTI_PASSWORD`, buka Allocation > License Allocation tab Current
26. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo kantong Principal dan kantong lain
27. Klik `[+ Allocation]`
28. Pilih Client `PT Abadi Jaya`, Target `SUBS-20260110-C1D2E`, Type `Concurrent User`, isi Additional Quantity `2`, Pay From `PT ABC (Principal)`, lalu catat Cost preview
29. Klik `[Submit]`
30. Verifikasi saldo kantong Principal berkurang sebesar Cost langkah 28
31. Verifikasi kantong lain tidak berubah
32. Tampilkan kolom Paid From lewat Setup Column
33. Verifikasi kolom Paid From baris baru (Allocation ID tidak ada pada baseline langkah 26) `PT ABC (Principal)`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 6 kali, kejadian menutup 6 (modal tertutup oleh Submit di langkah 3, 7, 12, 16, 22, dan 29).
- Langkah penghubung (S-03): langkah 9 (menggeser jam; dipulihkan di hook `after`), langkah 17 (menunggu aksi selesai dan baseline), langkah 26 (baseline), langkah 32 (menampilkan kolom Paid From).
- Verifikasi Allocation ID langkah 4, 8, dan 13 memakai nilai literal format yang disebut TC; counter harian dijamin nol oleh baseline automation.
- Temuan untuk QA:
  - TC-AC-LA-168 mengharapkan ID pertama `LALC-20261222-00001`, tetapi tanggal server uji 22 Dec 2026 dipakai banyak spec lain yang juga membuat alokasi; counter harian hanya nol bila baseline automation mereset counter, mekanisme itu tidak disebut TC dan disediakan tim FE/BE (S-13).
  - TC-AC-LA-168 Data Uji menyebut "Tiga alokasi pada dua hari" sedangkan Langkah 7 berbunyi "Ulangi sekali lagi pada hari yang sama"; spec membuat dua alokasi pada 22 Dec 2026 dan satu pada 23 Dec 2026.
  - TC-AC-LA-169 Expected a ("naik 5 dari sebelumnya") membandingkan dengan Current Quota form pertama; spec mencatatnya pada langkah 15.
  - TC-AC-LA-169 Post Condition ("Ledger term bertambah 10 total") tidak punya langkah observasi tambahan; tidak diasersi.
  - TC-AC-LA-171 Expected a ("kantong lain tidak berubah") tidak menyebut daftar kantong; spec membandingkan seluruh kantong sumber yang dicatat pada langkah 26.
