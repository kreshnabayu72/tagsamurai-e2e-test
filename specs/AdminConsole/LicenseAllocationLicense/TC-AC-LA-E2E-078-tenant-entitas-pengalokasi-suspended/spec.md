---
id: TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended
title: "State Tenant: Entitas Pengalokasi Suspended Menolak Seluruh Aksi Tulis"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-469
  - TC-AC-LA-496
  - TC-AC-LA-497
  - TC-AC-LA-498
  - TC-AC-LA-499
  - TC-AC-LA-500
coverage:
  web: automated
---

# State Tenant: Entitas Pengalokasi Suspended Menolak Seluruh Aksi Tulis

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19) dengan term `SUBS-20260101-A1B2C`, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, sebelum entitas disuspend, milik spec ini, bentuknya sama dengan Pre-setup #41 dan #48): satu alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` oleh `Dewi A` (Cost $150.00 di-Reserve) dipakai TC-AC-LA-496, 497, 499, 500 (semua aksi ditolak sehingga record tidak berubah), dan satu alokasi `Canceled` manual oleh `Dewi A` untuk TC-AC-LA-498. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE/BE): mengubah status entitas Distributor PT Maju Bersama menjadi Suspended dan memulihkannya lewat fixture backend (akun dan mekanisme tidak ditulis di TC). Status dipulihkan di langkah penutup dan di hook `after`.
- State global yang diubah: status entitas Distributor PT Maju Bersama (juga entitas akun aktor lain). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search Allocation ID seed Waiting for Approval di tab Current, tekan Enter, buka Allocation Log, lalu catat jumlah entri sebagai baseline; ulangi untuk seed Canceled di tab History
2. Atur status entitas Distributor PT Maju Bersama menjadi Suspended lewat fixture backend hingga tersimpan

### TC-AC-LA-469: Allocate ditolak terlepas capability

3. Catat jumlah baris tab Current sebagai baseline
4. Klik `[+ Allocation]`
5. Pilih Client `PT Sejahtera`
6. Pilih Target `SUBS-20260101-A1B2C`
7. Pilih Type `Concurrent User`
8. Isi Additional Quantity `1`
9. Klik `[Submit]`
10. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
11. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
12. Klik `✕` pada form Allocate
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`
15. Verifikasi List dan Allocation Log tetap dapat dibuka (aksi baca tetap tersedia)

### TC-AC-LA-496: Edit ditolak terlepas capability

16. Klik row action `Edit` pada seed Waiting for Approval
17. Ubah Additional Quantity dari `5` menjadi `6`, lalu klik `[Save]`
18. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
19. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
20. Verifikasi status seed tetap `Waiting for Approval`
21. Verifikasi jumlah entri Allocation Log seed sama dengan baseline

### TC-AC-LA-497: Cancel ditolak terlepas capability

22. Klik row action `Cancel Allocation` pada seed Waiting for Approval, lalu klik `[Cancel Request]`
23. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
24. Verifikasi status seed tetap `Waiting for Approval`
25. Verifikasi jumlah entri Allocation Log seed sama dengan baseline

### TC-AC-LA-498: Resubmit ditolak terlepas capability

26. Klik tab `History`, klik row action `Resubmit` pada seed Canceled, lalu klik `[Submit]`
27. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
28. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
29. Verifikasi status seed Canceled tetap `Canceled`
30. Verifikasi jumlah entri Allocation Log seed Canceled tidak bertambah dari baseline yang dicatat pada langkah 1

### TC-AC-LA-499: Approve ditolak terlepas capability

31. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka Approvals > License Allocation
32. Klik `[Review]` pada seed Waiting for Approval, pilih Approve, klik Submit
33. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
34. Verifikasi status seed tetap `Waiting for Approval`
35. Verifikasi jumlah entri Allocation Log seed sama dengan baseline

### TC-AC-LA-500: Reject ditolak terlepas capability

36. Klik `[Review]` pada seed Waiting for Approval, pilih Reject, isi Rejection Reason `Kuota tidak sesuai`, klik Submit
37. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
38. Verifikasi status seed tetap `Waiting for Approval`
39. Verifikasi jumlah entri Allocation Log seed sama dengan baseline
40. Pulihkan status entitas Distributor PT Maju Bersama lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (Search target dan baseline, R-16, S-12), 2 dan 40 (mengatur dan memulihkan status entitas), 3 (baseline jumlah baris), 31 (ganti akun dan membuka Approvals). Pembukaan Allocation Log untuk membaca entri (langkah 21, 25, 30, 35, 39) mengikuti langkah verifikasinya.
- Dialog `Unsaved Changes` pada langkah 13, 19, 28 adalah bagian S-08; form Allocate dan Edit yang ditolak server tetap terbuka dan dirty sehingga ditutup deterministik.
- Asersi absence (langkah 11, 21, 25, 30, 35, 39) beranchor toast hasil server yang sudah diasersi (8b butir 2) dan berbaseline.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (state tenant entitas Suspended), satu topik, dataset yang sama, dan tiap blok berdiri sendiri; state Suspended mahal dibangun ulang per blok.
- Temuan untuk QA:
  - TC-AC-LA-469 Langkah 1 memakai Target dan Type tanpa menyebut nilai Client lain; spec memakai Target `SUBS-20260101-A1B2C` dan Type `Concurrent User` dari Precondition d.
  - TC-AC-LA-469, 496 sampai 500 mensyaratkan entitas Distributor PT Maju Bersama Suspended tanpa akun dan mekanisme; disediakan tim FE. Entitas itu juga entitas akun aktor, sehingga login akun Distributor setelah suspend bergantung pada perilaku sistem yang tidak dijelaskan TC.
  - TC-AC-LA-496 sampai 500 Expected b ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Allocation Log.
  - TC-AC-LA-498 memakai Pre-setup #48 yang sama dengan blok lain; spec memakai seed milik spec.
