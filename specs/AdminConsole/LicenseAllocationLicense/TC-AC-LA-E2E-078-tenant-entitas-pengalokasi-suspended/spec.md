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

1. Klik tab `History`, ketik Search Allocation ID seed Canceled, tekan Enter, buka Allocation Log, lalu catat jumlah entri sebagai baseline
2. Tutup modal Allocation Log
3. Klik tab `Current`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed Waiting for Approval, tekan Enter, buka Allocation Log, lalu catat jumlah entri sebagai baseline
4. Tutup modal Allocation Log
5. Atur status entitas Distributor PT Maju Bersama menjadi Suspended lewat fixture backend hingga tersimpan

### TC-AC-LA-469: Allocate ditolak terlepas capability

6. Kosongkan kotak search: klik `✕` pada Search, tekan Enter
7. Catat jumlah baris tab Current sebagai baseline
8. Klik `[+ Allocation]`
9. Pilih Client `PT Sejahtera`
10. Pilih Target `SUBS-20260101-A1B2C`
11. Pilih Type `Concurrent User`
12. Isi Additional Quantity `1`
13. Klik `[Submit]`
14. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
15. Tunggu toast hilang otomatis
16. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
17. Klik `[×]` pada form Allocate
18. Verifikasi dialog `Unsaved Changes` tampil
19. Klik `[Leave]`
20. Ketik Search Allocation ID seed Waiting for Approval, tekan Enter, lalu klik row action `Allocation Log` pada seed Waiting for Approval
21. Verifikasi List dan Allocation Log tetap dapat dibuka (aksi baca tetap tersedia)
22. Tutup modal Allocation Log

### TC-AC-LA-496: Edit ditolak terlepas capability

23. Klik row action `Edit` pada seed Waiting for Approval
24. Ubah Additional Quantity dari `5` menjadi `6`, lalu klik `[Save]`
25. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
26. Tunggu toast hilang otomatis
27. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
28. Verifikasi status seed tetap `Waiting for Approval`
29. Verifikasi jumlah entri Allocation Log seed sama dengan baseline

### TC-AC-LA-497: Cancel ditolak terlepas capability

30. Klik row action `Cancel Allocation` pada seed Waiting for Approval, lalu klik `[Cancel Request]`
31. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
32. Tunggu toast hilang otomatis
33. Verifikasi status seed tetap `Waiting for Approval`
34. Verifikasi jumlah entri Allocation Log seed sama dengan baseline

### TC-AC-LA-498: Resubmit ditolak terlepas capability

35. Klik tab `History`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, ketik Search Allocation ID seed Canceled, tekan Enter, klik row action `Resubmit` pada seed Canceled, lalu klik `[Submit]`
36. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
37. Tunggu toast hilang otomatis
38. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
39. Verifikasi status seed Canceled tetap `Canceled`
40. Verifikasi jumlah entri Allocation Log seed Canceled tidak bertambah dari baseline yang dicatat pada langkah 1

### TC-AC-LA-499: Approve ditolak terlepas capability

41. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka Approvals > License Allocation
42. Klik `[Review]` pada seed Waiting for Approval, pilih Approve, klik Submit
43. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
44. Tunggu toast hilang otomatis
45. Verifikasi status seed tetap `Waiting for Approval`
46. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Waiting for Approval, tekan Enter, lalu klik row action `Allocation Log`
47. Verifikasi jumlah entri Allocation Log seed sama dengan baseline
48. Tutup modal Allocation Log
49. Buka Approvals > License Allocation

### TC-AC-LA-500: Reject ditolak terlepas capability

50. Klik `[Review]` pada seed Waiting for Approval, pilih Reject, isi Rejection Reason `Kuota tidak sesuai`, klik Submit
51. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
52. Verifikasi status seed tetap `Waiting for Approval`
53. Buka Allocation > License Allocation tab Current, ketik Search Allocation ID seed Waiting for Approval, tekan Enter, lalu klik row action `Allocation Log`
54. Verifikasi jumlah entri Allocation Log seed sama dengan baseline
55. Tutup modal Allocation Log
56. Pulihkan status entitas Distributor PT Maju Bersama lewat fixture backend hingga tersimpan

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 6 (mengosongkan Search seed dengan klik `✕` dan Enter sebelum baseline jumlah baris, sehingga record baru ikut terhitung, S-12) dan langkah 15, 26, 32, 37, dan 44 (Tunggu toast hilang otomatis sebelum toast baku berikutnya diasersi, R-12), langkah 1, 3, 35 (Search target dan baseline, R-16, S-12; langkah 3 dan 35 mengosongkan kotak Search dengan klik `✕` lalu Enter sesudah pindah tab, S-14), 2, 4, 22 (menutup modal Allocation Log sebelum membuka surface lain, S-09), 5 dan 56 (mengatur dan memulihkan status entitas), 7 (baseline jumlah baris), 41 (ganti akun dan membuka Approvals). Pembukaan Allocation Log untuk membaca entri (langkah 29, 34, dan 40) mengikuti langkah verifikasinya; langkah 20 membukanya untuk langkah 21, sedangkan langkah 47 dan 54 dibuka eksplisit pada langkah 46 dan 53 karena akun Fajar berada di Approvals (S-14). Langkah 49 membuka Approvals kembali dan langkah 48 dan 55 menutup modal Allocation Log (S-09).
- Dialog `Unsaved Changes` pada langkah 18, 27, 38 adalah bagian S-08; form Allocate dan Edit yang ditolak server tetap terbuka dan dirty sehingga ditutup deterministik.
- Asersi absence (langkah 16, 29, 34, 40, 47, 54) beranchor toast hasil server yang sudah diasersi (8b butir 2) dan berbaseline.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (state tenant entitas Suspended), satu topik, dataset yang sama, dan tiap blok berdiri sendiri; state Suspended mahal dibangun ulang per blok.
- Temuan untuk QA:
  - TC-AC-LA-469 Langkah 1 memakai Target dan Type tanpa menyebut nilai Client lain; spec memakai Target `SUBS-20260101-A1B2C` dan Type `Concurrent User` dari Precondition d.
  - TC-AC-LA-469, 496 sampai 500 mensyaratkan entitas Distributor PT Maju Bersama Suspended tanpa akun dan mekanisme; disediakan tim FE. Entitas itu juga entitas akun aktor, sehingga login akun Distributor setelah suspend bergantung pada perilaku sistem yang tidak dijelaskan TC.
  - TC-AC-LA-496 sampai 500 Expected b ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Allocation Log.
  - TC-AC-LA-498 memakai Pre-setup #48 yang sama dengan blok lain; spec memakai seed milik spec.
