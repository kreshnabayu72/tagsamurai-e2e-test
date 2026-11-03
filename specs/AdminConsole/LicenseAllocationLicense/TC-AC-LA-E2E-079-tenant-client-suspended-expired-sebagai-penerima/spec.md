---
id: TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima
title: "State Tenant: Client Suspended dan Expired sebagai Penerima Alokasi"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-467
  - TC-AC-LA-468
  - TC-AC-LA-470
  - TC-AC-LA-501
  - TC-AC-LA-502
  - TC-AC-LA-503
  - TC-AC-LA-504
  - TC-AC-LA-238
coverage:
  web: automated
---

# State Tenant: Client Suspended dan Expired sebagai Penerima Alokasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): Klinik Beku (#29, status Suspended), Gudang Lawas (#30, status Expired), kantong wallet (#33), Product Price (#34).
- Data Dinamis (seeding lewat API di hook `before`, saat Client masih Active, lalu fixture backend yang disediakan tim FE/BE mengubah status Client menjadi Suspended atau Expired; milik spec ini, bentuknya sama dengan Pre-setup #71 dan #80): pada Klinik Beku satu alokasi `Waiting for Approval` Concurrent User +5 (Cost $150.00 di-Reserve) dan satu alokasi `Canceled` manual Concurrent User +5 oleh `Dewi A`; pada Gudang Lawas satu alokasi `Canceled` manual Concurrent User +5 oleh `Dewi A`. Allocation ID dibaca dari hasil seeding. Semua aksi di spec ini ditolak sehingga seed tidak berubah.
- Kemampuan teknis (disediakan tim FE/BE): fixture backend untuk mengubah dan memulihkan status Client Klinik Beku dan Gudang Lawas (akun dan mekanisme tidak ditulis di TC). Status dipulihkan di hook `after`.
- State global yang diubah: status Client Klinik Beku dan Gudang Lawas. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-467: Client Suspended dipilih sebagai penerima

1. Catat jumlah baris tab Current sebagai baseline
2. Klik `[+ Allocation]`
3. Pilih Client `Klinik Beku` (badge Suspended)
4. Pilih Target term FAMS Professional Klinik Beku
5. Pilih Type `Concurrent User`
6. Isi Additional Quantity `1`
7. Klik `[Submit]`
8. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
9. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
10. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-468: Client Expired dipilih sebagai penerima

11. Klik `[+ Allocation]`
12. Pilih Client `Gudang Lawas` (badge Expired)
13. Pilih Target FAMS Professional Gudang Lawas, Type `Concurrent User`, dan isi Additional Quantity `1`
14. Klik `[Submit]`
15. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
16. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
17. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-470: Edit pada alokasi milik Client Suspended

18. Klik row action `Edit` pada alokasi Waiting for Approval Klinik Beku
19. Ubah Additional Quantity dari `5` menjadi `6`, lalu klik `[Save]`
20. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
21. Verifikasi data alokasi tidak berubah (Quantity tetap `5`)
22. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-501: Cancel pada alokasi milik Client Suspended

23. Klik row action `Cancel Allocation` pada alokasi Waiting for Approval Klinik Beku, lalu klik `[Cancel Request]`
24. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
25. Verifikasi status alokasi tetap `Waiting for Approval`

### TC-AC-LA-502: Resubmit pada alokasi milik Client Suspended

26. Klik tab `History`, klik row action `Resubmit` pada baris Canceled Klinik Beku, lalu klik `[Submit]`
27. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
28. Verifikasi status alokasi tidak berubah (tetap `Canceled`)
29. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-238: Resubmit pada alokasi milik Client Expired

30. Klik row action `Resubmit` pada baris Canceled Gudang Lawas, lalu klik `[Submit]`
31. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
32. Verifikasi tidak ada record baru
33. Verifikasi alokasi asal tetap `Canceled`
34. Klik `✕`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-503: Approve pada alokasi milik Client Suspended

35. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka Approvals > License Allocation
36. Klik `[Review]` pada alokasi Klinik Beku, pilih Approve, klik Submit
37. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
38. Verifikasi status alokasi tetap `Waiting for Approval`

### TC-AC-LA-504: Reject pada alokasi milik Client Suspended

39. Klik `[Review]` pada alokasi Klinik Beku, pilih Reject, isi Rejection Reason `Kuota tidak sesuai`, klik Submit
40. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
41. Verifikasi status alokasi tetap `Waiting for Approval`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar semua aksi akun Dewi (Create, Edit, Cancel, Resubmit) berurutan sebelum satu kali ganti akun ke Fajar.
- Langkah penghubung (S-03): langkah 1 (baseline jumlah baris, S-12), 35 (ganti akun dan membuka Approvals). Dialog `Unsaved Changes` (langkah 10, 17, 22, 29, 34) adalah bagian S-08.
- Asersi absence (langkah 9, 16, 32) beranchor toast hasil server yang sudah diasersi (8b butir 2) dan berbaseline.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (state tenant: Client Suspended atau Expired sebagai penerima), satu topik, dan seed yang sama; tiap blok berdiri sendiri dan state status Client mahal dibangun ulang per blok.
- Temuan untuk QA:
  - TC-AC-LA-467 Langkah 1 dan TC-AC-LA-468 Langkah 1 ("isi field") tidak menyebut Target dan Type; spec memakai Type `Concurrent User` dan Target term FAMS Professional Client masing-masing.
  - TC-AC-LA-467, 468, 470, 501 sampai 504, 238 mensyaratkan status Client Suspended atau Expired yang dibuat saat Client Active; akun dan mekanisme pengubahan status tidak ditulis, disediakan tim FE.
  - TC-AC-LA-470, 501 sampai 504, 238 Expected b menyebut "License Allocation bukan aksi reaktivasi sehingga tidak dikecualikan" sebagai alasan, bukan perilaku teramati; hanya data atau status tidak berubah yang diasersi.
  - TC-AC-LA-503 dan 504 Precondition tidak menyebut alokasi Waiting for Approval Klinik Beku dibuat oleh `Dewi A`; spec memakai seed oleh `Dewi A`.
