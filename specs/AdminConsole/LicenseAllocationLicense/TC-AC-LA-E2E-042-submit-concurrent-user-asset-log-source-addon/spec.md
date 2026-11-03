---
id: TC-AC-LA-E2E-042-submit-concurrent-user-asset-log-source-addon
title: "Submit Allocate: Concurrent User, Asset License, dan Log Source"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-155
  - TC-AC-LA-156
  - TC-AC-LA-157
coverage:
  web: automated
---

# Submit Allocate: Concurrent User, Asset License, dan Log Source

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`), Klinik Medika Jaya (#20, SIEM Growth `SUBS-20260301-P1Q2R`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Concurrent User $365, Log Source $365, Asset License $365 per unit per tahun). Toggle Require Approval for Allocation OFF (#39), diatur fixture backend (disediakan tim FE/BE) di hook `before` dan dipulihkan di hook `after`.
- Data Dinamis: tiga alokasi Completed Active (Concurrent User +10 dan Asset License +20 ke PT Sejahtera, Log Source +10 ke Klinik Medika Jaya). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger kuota term dipulihkan oleh baseline automation dan fixture backend di hook `after`.
- Baseline: total Concurrent User term di Subscription Detail (langkah 1), daftar Allocation ID baris di halaman pertama tab Current, saldo kantong, dan Current Quota dicatat sebelum tiap `[Submit]`.
- Kemampuan teknis: membaca saldo kantong Distributor (disediakan tim FE/BE); menampilkan kolom Payment lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE); Subscription Detail > License Quota tersedia sebagai halaman modul Client Subscription.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-155: Submit Concurrent User ke Target term Active dengan toggle OFF

1. Buka Subscription Detail `SUBS-20260101-A1B2C` > License Quota, catat total Concurrent User term, lalu buka Allocation > License Allocation tab Current
2. Pastikan kolom Payment tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Payment, lalu klik `[Save]`
3. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo kantong Distributor
4. Klik `[+ Allocation]`
5. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, isi Additional Quantity `10`, lalu catat Current Quota dan Cost pada preview
6. Klik `[Submit]`
7. Verifikasi toast sukses "Success, license has been allocated."
8. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 3): License Type `Concurrent User`, Status `Active`, Quantity `+10`, Allocated By `Dewi A`
9. Verifikasi Payment baris baru: `Wallet`
10. Klik `[+ Allocation]`
11. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`
12. Verifikasi Current Quota term bertambah sebesar Quantity (nilai langkah 5 ditambah 10)
13. Klik `[✕]` pada header
14. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
15. Klik `[Leave]`
16. Verifikasi saldo kantong berkurang permanen sebesar Cost langkah 5
17. Buka Subscription Detail `SUBS-20260101-A1B2C` > License Quota
18. Verifikasi total Concurrent User term `SUBS-20260101-A1B2C` bertambah 10 terhadap langkah 1 (real-time)

### TC-AC-LA-156: Submit Asset License ke Target term Active dengan toggle OFF

19. Buka Allocation > License Allocation tab Current, lalu catat baseline Allocation ID baris di halaman pertama dan saldo kantong Distributor
20. Klik `[+ Allocation]`
21. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Asset License`, isi Additional Quantity `20`, lalu catat Current Quota dan Cost pada preview
22. Klik `[Submit]`
23. Verifikasi toast sukses "Success, license has been allocated."
24. Verifikasi baris baru tab Current (Allocation ID tidak ada pada baseline langkah 19): License Type `Asset License`, Status `Active`, Quantity `+20`, Allocated By `Dewi A`
25. Verifikasi Payment baris baru: `Wallet`
26. Klik `[+ Allocation]`
27. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Asset License`
28. Verifikasi Current Quota term bertambah sebesar Quantity (nilai langkah 21 ditambah 20)
29. Klik `[✕]` pada header
30. Verifikasi dialog `Unsaved Changes` dengan Body `You have unsaved changes. Are you sure you want to leave?` serta tombol `[Leave]` dan `[Cancel]`
31. Klik `[Leave]`
32. Verifikasi saldo kantong berkurang permanen sebesar Cost langkah 21

### TC-AC-LA-157: Submit Log Source ke Target SIEM

33. Catat baseline Allocation ID baris di halaman pertama tab Current
34. Klik `[+ Allocation]`
35. Pilih Client `Klinik Medika Jaya`, Target `SUBS-20260301-P1Q2R`, Type `Log Source`, isi Additional Quantity `10`
36. Klik `[Submit]`
37. Verifikasi toast sukses "Success, license has been allocated."
38. Verifikasi baris baru (Allocation ID tidak ada pada baseline langkah 33): License Type `Log Source`, Product `SIEM`, Status `Active`, Quantity `+10`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 5 kali, kejadian menutup 5 (modal tertutup oleh Submit di langkah 6, 22, dan 36; dialog Leave di langkah 13 sampai 15 dan 29 sampai 31).
- Spec 38 langkah, di atas 35 langkah. Alasannya: tiga blok satu topik (Submit sukses ke Target term dengan toggle OFF) yang berdiri sendiri: kegagalan satu blok tidak membuat blok lain kehilangan makna, sehingga tidak dipecah. TC-AC-LA-158 (Addon FAMS lima jenis) ada di spec 054.
- Langkah penghubung (S-03): langkah 2 (menampilkan kolom Payment lewat Setup Column, tanpa `Verifikasi`; kolom Payment tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 1, 3, 19, dan 33 (baseline dan pindah halaman), langkah 10 sampai 15 dan 26 sampai 31 (membuka form ulang untuk mengamati Current Quota lalu menutup form dirty, S-08), dan langkah 17 (membuka Subscription Detail).
- Temuan untuk QA:
  - TC-AC-LA-155 Expected c, TC-AC-LA-156 Expected c ("Current Quota term bertambah sebesar Quantity") tidak menyebut lokasi pengamatan; spec mengamati Current Quota di form Allocate berikutnya (sesuai Langkah 7 TC-AC-LA-155).
  - TC-AC-LA-155 dan TC-AC-LA-156 Expected d ("saldo kantong berkurang permanen sebesar Cost") tidak menyebut lokasi pembacaan saldo; spec memakai kemampuan baca saldo yang disediakan tim FE/BE.
  - TC-AC-LA-155 Langkah 8 menyebut "License Quota" di Subscription Detail tanpa menyebut nama tab; spec membuka halaman License Quota sesuai teks TC.
  - TC-AC-LA-157 Post Condition ("Ledger Log Source term SIEM bertambah 10") dan TC-AC-LA-155 serta TC-AC-LA-156 Post Condition ("ledger term bertambah dan kantong didebit dalam satu transaksi") tidak punya langkah observasi tambahan; hanya yang tercakup Expected yang diasersi.
