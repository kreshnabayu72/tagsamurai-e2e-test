---
id: TC-AC-LA-E2E-040-cost-terkunci-pembulatan-dan-cost-nol
title: "Cost Terkunci: Pembulatan Half-up, Cost Nol, dan Nominal Sama dari Preview sampai Capture"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LA-143
  - TC-AC-LA-151
  - TC-AC-LA-513
coverage:
  web: automated
---

# Cost Terkunci: Pembulatan Half-up, Cost Nol, dan Nominal Sama dari Preview sampai Capture

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > License Allocation, tab Current). Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10, approver), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen` oleh hook suite, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: PT Sejahtera (#19, `SUBS-20260101-A1B2C`, End Date 31 Dec 2026), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (#33), Product Price (#34: Addon IT Inventory $100 per unit per tahun), harga Addon Tracking $0 (#36).
- Toggle Require Approval for Allocation: OFF (#39) untuk TC-AC-LA-143 (diatur di hook `before`), ON (#38) untuk TC-AC-LA-151 dan TC-AC-LA-513 (diatur lewat langkah 10); diatur fixture backend (disediakan tim FE/BE) dan dipulihkan ke keadaan awal di hook `after`.
- Jam (nilai absolut, disediakan tim FE/BE): tanggal server uji 24 Dec 2026 untuk TC-AC-LA-143 (hook `before`) dan 25 Dec 2026 untuk TC-AC-LA-513 (langkah 19); jam server dan jam browser diatur bersama dan dipulihkan di hook `after`.
- Data Dinamis: Addon IT Inventory +3 PT Sejahtera Completed Wallet Cost $6.58 (Dinamis #6); Addon Tracking +5 Waiting for Approval Cost $0.00; Addon IT Inventory +3 Waiting for Approval lalu Completed Cost $5.75 (Dinamis #7). Alokasi tidak dapat dihapus (tanpa Delete); saldo kantong dan ledger kuota dipulihkan oleh baseline automation dan fixture backend.
- Baseline: Allocation ID baris di halaman pertama tab Current dan saldo (Available, Reserved, Balance) kantong Distributor dicatat sebelum tiap `[Submit]` (langkah 2, 11, dan 19).
- Kemampuan teknis: membaca saldo kantong Distributor (Available, Reserved, Balance) dan menampilkan kolom Cost pada List lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-143: Cost prorata non-bulat dibulatkan half-up ke dua desimal saat dikunci

1. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
2. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, Balance kantong Distributor
3. Klik `[+ Allocation]`
4. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `IT Inventory`, isi Additional Quantity `3`
5. Verifikasi baris Cost menampilkan `$6.58` (3 × 100 × 8 ÷ 365 = 6.5753 dibulatkan half-up)
6. Klik `[Submit]`
7. Tunggu modal tertutup dan baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 2)
8. Verifikasi kolom Cost baris baru di List `$6.58`
9. Verifikasi saldo kantong Distributor berkurang tepat `$6.58` terhadap baseline langkah 2

### TC-AC-LA-151: Cost nol diproses normal tanpa Reserve maupun Capture

10. Atur toggle Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend hingga tersimpan, lalu buka ulang Allocation > License Allocation tab Current
11. Catat baseline Allocation ID baris di halaman pertama tab Current dan saldo Available, Reserved, dan Balance kantong Distributor
12. Klik `[+ Allocation]`
13. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Tracking`, isi Additional Quantity `5`
14. Verifikasi section Payment menampilkan nominal Cost `$0.00`
15. Verifikasi tidak ada warning V-18 maupun V-17
16. Klik `[Submit]`
17. Verifikasi alokasi baru (Allocation ID tidak ada pada baseline langkah 11) berstatus `Waiting for Approval`
18. Verifikasi Available, Reserved, dan Balance kantong tidak berubah terhadap langkah 11 (tidak ada Reserve)

### TC-AC-LA-513: Cost dikunci hasil pembulatan half-up dari Preview sampai Capture

19. Atur jam server dan jam browser ke 25 Dec 2026, lalu buka ulang Allocation > License Allocation tab Current, dan catat baseline Allocation ID baris di halaman pertama tab Current serta saldo Available, Reserved, dan Balance kantong Distributor
20. Klik `[+ Allocation]`
21. Pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `IT Inventory`, isi Additional Quantity `3`
22. Verifikasi baris Cost pada Preview `$5.75` (5.7534 dibulatkan half-up)
23. Klik `[Submit]`
24. Verifikasi status baris baru (Allocation ID tidak ada pada baseline langkah 19) `Waiting for Approval`
25. Verifikasi Reserved kantong bertambah tepat `$5.75`
26. Verifikasi kolom Cost baris baru `$5.75`
27. Buka Allocation Log baris tersebut
28. Verifikasi entri `Allocation created by Dewi A` memuat baris `Cost: $5.75 (Wallet)`
29. Tutup modal Allocation Log
30. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`
31. Buka Approvals > License Allocation dan Approve alokasi tersebut
32. Tunggu aksi selesai, lalu buka Allocation > License Allocation tab Current
33. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
34. Verifikasi Balance kantong berkurang `$5.75` terhadap langkah 19 (Capture tepat `$5.75` tanpa hitung ulang)
35. Verifikasi Reserved kantong turun `$5.75` terhadap nilai sesudah Submit (langkah 25)
36. Verifikasi kolom Cost baris tersebut tetap `$5.75`
37. Buka Allocation Log baris tersebut
38. Verifikasi baris Cost Allocation Log tetap `$5.75`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Buka form 3 kali, kejadian menutup 3 (modal tertutup oleh Submit sukses di langkah 6, 16, dan 23).
- Spec 38 langkah, di atas smell 35 langkah; tiga blok satu topik (Cost terkunci) yang berdiri sendiri. Setup Column diulang setelah ganti akun (langkah 33) karena kolom Cost tersembunyi secara bawaan dan tidak diandaikan tetap tampil sesudah ganti akun.
- Penyimpangan urutan (S-05, S-10): TC-AC-LA-151 dan TC-AC-LA-513 sama-sama memakai toggle ON, sehingga toggle hanya dialihkan sekali (langkah 10) dan tidak bolak-balik; TC-AC-LA-143 (toggle OFF) dijalankan lebih dahulu.
- Langkah penghubung (S-03): langkah 1 dan 33 (menampilkan kolom Cost lewat Setup Column, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 2, 11, dan 19 (baseline), langkah 7 dan 32 (menunggu aksi selesai), langkah 10 dan 19 (mengatur toggle dan jam), langkah 27 dan 37 (membuka Allocation Log), langkah 29 (menutup modal Allocation Log sebelum ganti akun), dan ganti akun pada langkah 30 (S-07).
- Temuan untuk QA:
  - TC-AC-LA-143 Langkah 7 "Buka kolom Cost di List" tidak menyatakan bahwa kolom Cost tersembunyi atau tampil secara bawaan; spec menampilkan kolom Cost lewat Setup Column pada langkah 1 (kemampuan disediakan tim FE).
  - TC-AC-LA-143 Expected b dan TC-AC-LA-513 Expected b sampai d membaca saldo kantong (Balance, Reserved, Available) yang tidak tampil di halaman License Allocation; pembacaan saldo memakai kemampuan baca yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
  - TC-AC-LA-151 memakai toggle ON (#38) sedangkan TC-AC-LA-143 memakai toggle OFF (#39); TC tidak menyebut mekanisme alih toggle, sehingga dilakukan fixture backend yang disediakan tim FE/BE.
  - TC-AC-LA-513 Langkah 4 "Login sebagai Fajar Nugroho dan Approve" tidak menjelaskan konfirmasi dialog Approve; langkah mengikuti TC (Approve alokasi) dan dialog konfirmasi bila ada ditentukan tim FE.
  - TC-AC-LA-513 Dependensi TC-AC-LA-143 tidak dimanfaatkan: spec membuat datanya sendiri (S-06).
