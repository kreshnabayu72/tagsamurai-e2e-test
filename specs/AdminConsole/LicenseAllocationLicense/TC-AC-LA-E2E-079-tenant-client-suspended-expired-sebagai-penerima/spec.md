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
9. Tunggu toast hilang otomatis
10. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
11. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-468: Client Expired dipilih sebagai penerima

12. Klik `[+ Allocation]`
13. Pilih Client `Gudang Lawas` (badge Expired)
14. Pilih Target FAMS Professional Gudang Lawas, Type `Concurrent User`, dan isi Additional Quantity `1`
15. Klik `[Submit]`
16. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
17. Tunggu toast hilang otomatis
18. Verifikasi alokasi tidak dibuat (jumlah baris tab Current sama dengan baseline)
19. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-470: Edit pada alokasi milik Client Suspended

20. Klik row action `Edit` pada alokasi Waiting for Approval Klinik Beku
21. Ubah Additional Quantity dari `5` menjadi `6`, lalu klik `[Save]`
22. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
23. Tunggu toast hilang otomatis
24. Verifikasi data alokasi tidak berubah (Quantity tetap `5`)
25. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-501: Cancel pada alokasi milik Client Suspended

26. Klik row action `Cancel Allocation` pada alokasi Waiting for Approval Klinik Beku, lalu klik `[Cancel Request]`
27. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
28. Tunggu toast hilang otomatis
29. Verifikasi status alokasi tetap `Waiting for Approval`

### TC-AC-LA-502: Resubmit pada alokasi milik Client Suspended

30. Klik tab `History`, klik row action `Resubmit` pada baris Canceled Klinik Beku, lalu klik `[Submit]`
31. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
32. Tunggu toast hilang otomatis
33. Verifikasi status alokasi tidak berubah (tetap `Canceled`)
34. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`

### TC-AC-LA-238: Resubmit pada alokasi milik Client Expired

35. Klik tab `Current`, lalu catat jumlah baris tab Current sebagai baseline
36. Klik tab `History`, ketik Search Allocation ID seed Canceled Gudang Lawas, tekan Enter, klik row action `Resubmit` pada baris Canceled Gudang Lawas, lalu klik `[Submit]`
37. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
38. Tunggu toast hilang otomatis
39. Verifikasi alokasi asal tetap `Canceled`
40. Klik `[×]`, verifikasi dialog `Unsaved Changes`, lalu klik `[Leave]`
41. Klik `(←)` pada kotak Search
42. Klik tab `Current`
43. Verifikasi tidak ada record baru (jumlah baris tab Current sama dengan baseline langkah 35)

### TC-AC-LA-503: Approve pada alokasi milik Client Suspended

44. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka Approvals > License Allocation
45. Klik `[Review]` pada alokasi Klinik Beku, pilih Approve, klik Submit
46. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
47. Tunggu toast hilang otomatis
48. Verifikasi status alokasi tetap `Waiting for Approval`
49. Tutup dialog Review

### TC-AC-LA-504: Reject pada alokasi milik Client Suspended

50. Klik `[Review]` pada alokasi Klinik Beku, pilih Reject, isi Rejection Reason `Kuota tidak sesuai`, klik Submit
51. Verifikasi toast baku "Changes can't be saved while this workspace is suspended or expired."
52. Verifikasi status alokasi tetap `Waiting for Approval`
53. Tutup dialog Review

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC diubah dari urutan nomor agar semua aksi akun Dewi (Create, Edit, Cancel, Resubmit) berurutan sebelum satu kali ganti akun ke Fajar.
- Langkah penghubung (S-03): langkah 1 dan 35 (baseline jumlah baris, S-12), 41 dan 42 (mengosongkan Search dengan `(←)` dan pindah ke tab Current), 44 (ganti akun dan membuka Approvals). Langkah 9, 17, 23, 28, 32, 38, dan 47 (Tunggu toast hilang otomatis sebelum toast baku berikutnya diasersi, R-12) adalah langkah penghubung. Dialog `Unsaved Changes` (langkah 11, 19, 25, 34, 40) adalah bagian S-08.
- Langkah 49 dan 53 (menutup dialog Review sesudah Approve atau Reject ditolak, sebelum Review berikutnya dan di akhir spec, S-09) adalah langkah penghubung tanpa Verifikasi.
- Asersi absence (langkah 10, 18, 43) beranchor toast hasil server yang sudah diasersi (8b butir 2) dan berbaseline. Langkah 43 (TC-AC-LA-238, tidak ada record baru) dibandingkan dengan baseline langkah 35 yang dicatat sebelum `[Submit]`; langkah 39 (record asal tetap `Canceled` di tab History, anchor) ditaruh sebelum langkah 43.
- Spec melewati sekitar 35 langkah. Alasan pertahanan: seluruh blok satu kelas harness (state tenant: Client Suspended atau Expired sebagai penerima), satu topik, dan seed yang sama; tiap blok berdiri sendiri dan state status Client mahal dibangun ulang per blok.
- Temuan untuk QA:
  - TC-AC-LA-467 Langkah 1 dan TC-AC-LA-468 Langkah 1 ("isi field") tidak menyebut Target dan Type; spec memakai Type `Concurrent User` dan Target term FAMS Professional Client masing-masing.
  - TC-AC-LA-467, 468, 470, 501 sampai 504, 238 mensyaratkan status Client Suspended atau Expired yang dibuat saat Client Active; akun dan mekanisme pengubahan status tidak ditulis, disediakan tim FE.
  - TC-AC-LA-470, 501 sampai 504, 238 Expected b menyebut "License Allocation bukan aksi reaktivasi sehingga tidak dikecualikan" sebagai alasan, bukan perilaku teramati; hanya data atau status tidak berubah yang diasersi.
  - TC-AC-LA-503 dan 504 Precondition tidak menyebut alokasi Waiting for Approval Klinik Beku dibuat oleh `Dewi A`; spec memakai seed oleh `Dewi A`.
