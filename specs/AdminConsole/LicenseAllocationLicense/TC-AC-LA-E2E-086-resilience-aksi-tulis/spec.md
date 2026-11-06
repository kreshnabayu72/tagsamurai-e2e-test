---
id: TC-AC-LA-E2E-086-resilience-aksi-tulis
title: "Resilience Aksi Tulis: Edit, Cancel, Resubmit, Allocate, Timeout Jaringan, dan Reject Gagal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-197
  - TC-AC-LA-224
  - TC-AC-LA-236
  - TC-AC-LA-471
  - TC-AC-LA-472
  - TC-AC-LA-249
coverage:
  web: automated
---

# Resilience Aksi Tulis: Edit, Cancel, Resubmit, Allocate, Timeout Jaringan, dan Reject Gagal

## Prerequisites

- Mode: FE+BE. Spec memakai `Spectra.intercept()` parsial di atas backend nyata; intercept dilepas segera setelah pemicu selesai (S-09). TC tidak menyebut endpoint, dan openapi.yaml serta LLD modul tidak ada, sehingga pola endpoint yang di-intercept (PUT Edit, Cancel, submit Resubmit, submit Allocate, keputusan Reject) disediakan tim FE (S-13).
- Akun aktor pertama: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Akun ganti akun (langkah eksplisit): Total Control Distributor `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`, Pre-setup #10), password `Spectra.env.AC_LA_TC_DIST_PASSWORD`.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup (hanya dibaca): PT Sejahtera (#19) dengan term `SUBS-20260101-A1B2C`, kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38) dan OFF (#39) (TC-AC-LA-471 dan TC-AC-LA-472 memerlukan OFF; diatur fixture backend yang disediakan tim FE/BE di langkah penghubung 22 dan 34 dan dipulihkan di hook `after`).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini, bentuknya sama dengan Pre-setup #41 dan #48): alokasi `Waiting for Approval` Concurrent User +5 oleh `Dewi A` (Cost $150.00 di-Reserve) untuk tiap TC-AC-LA-197, 224, dan 249; alokasi `Canceled` manual Concurrent User +5 oleh `Dewi A` untuk TC-AC-LA-236. Semua aksi di spec ini gagal sehingga seed tidak berubah. Allocation ID dibaca dari hasil seeding.
- Kemampuan teknis (disediakan tim FE): intercept respons 500, intercept timeout (respons tidak pernah kembali), dan baca jumlah baris tab Current dan saldo Wallet (baseline S-12).
- State global yang diubah: toggle Require Approval for Allocation (dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-197: Edit gagal 5xx menampilkan toast error dan form tetap terbuka

1. Ketik Search Allocation ID seed 197 di tab Current, tekan Enter
2. Klik row action `Edit` pada baris seed 197
3. Ubah Quantity ke `6`
4. Pasang intercept submit Edit: respons 500
5. Klik `[Save]`
6. Verifikasi toast error "Error, failed to update license allocation."
7. Verifikasi form tetap terbuka dengan input `6` dipertahankan
8. Verifikasi `[Save]` aktif kembali
9. Lepas intercept submit Edit
10. Klik `[×]`
11. Verifikasi dialog `Unsaved Changes`
12. Klik `[Leave]`
13. Verifikasi data alokasi seed 197 tidak berubah (Quantity tetap `5`)

### TC-AC-LA-224: Cancel gagal 5xx menampilkan toast error dan status tidak berubah

14. Ganti isi kotak search dengan Allocation ID seed 224 di tab Current, tekan Enter
15. Pasang intercept Cancel: respons 500
16. Klik row action `Cancel Allocation` pada baris seed 224, lalu klik `[Cancel Request]`
17. Verifikasi toast error "Error, failed to cancel license allocation."
18. Lepas intercept Cancel
19. Verifikasi status seed 224 tetap `Waiting for Approval`
20. Buka Wallet
21. Verifikasi Reserve utuh

### TC-AC-LA-236: Resubmit gagal 5xx menampilkan toast error dan form tetap terbuka

22. Atur toggle Require Approval for Allocation ON (Pre-setup #38) lewat fixture backend hingga tersimpan
23. Buka Allocation > License Allocation (tab Current)
24. Klik tab `History`, ketik Search Allocation ID seed 236, tekan Enter
25. Klik row action `Resubmit` pada baris Canceled seed 236
26. Pasang intercept submit Resubmit: respons 500
27. Klik `[Submit]`
28. Verifikasi toast error "Error, failed to resubmit license allocation."
29. Verifikasi form tetap terbuka dengan input pre-filled utuh
30. Lepas intercept submit Resubmit
31. Klik `[×]`
32. Verifikasi dialog `Unsaved Changes`
33. Klik `[Leave]`

### TC-AC-LA-471: Allocate gagal 5xx, form tetap terbuka, all-or-nothing

34. Atur toggle Require Approval for Allocation OFF (Pre-setup #39) lewat fixture backend hingga tersimpan
35. Buka Allocation > License Allocation (tab Current)
36. Catat jumlah baris tab Current dan saldo Wallet sebagai baseline
37. Klik `[+ Allocation]`, pilih Client `PT Sejahtera`, Target `SUBS-20260101-A1B2C`, Type `Concurrent User`, dan isi Additional Quantity `2`
38. Pasang intercept submit Allocate: respons 500
39. Klik `[Submit]`
40. Verifikasi toast error "Error, failed to allocate license."
41. Verifikasi form tetap terbuka dengan input dipertahankan
42. Verifikasi `[Submit]` aktif kembali
43. Verifikasi tidak ada record baru (jumlah baris tab Current sama dengan baseline)
44. Verifikasi tidak ada mutasi wallet (saldo Wallet sama dengan baseline)
45. Lepas intercept submit Allocate

### TC-AC-LA-472: Timeout jaringan Allocate

46. Pasang intercept submit Allocate: respons tidak pernah kembali (timeout)
47. Klik `[Submit]` pada form yang sama
48. Verifikasi toast error "Connection problem. Please try again."
49. Verifikasi form tetap terbuka
50. Verifikasi `[Submit]` aktif kembali untuk retry manual
51. Lepas intercept submit Allocate
52. Klik `[×]`
53. Verifikasi dialog `Unsaved Changes`
54. Klik `[Leave]`

### TC-AC-LA-249: Reject gagal 5xx menampilkan toast error dan form keputusan tetap terbuka

55. Ganti akun: logout `Dewi A`, login sebagai `Fajar Nugroho` dengan `Spectra.env.AC_LA_TC_DIST_PASSWORD`, lalu buka Approvals > License Allocation
56. Klik `[Review]` pada alokasi seed 249, pilih Reject, dan isi alasan
57. Pasang intercept keputusan: respons 500
58. Klik Submit
59. Verifikasi toast error 5xx `Error, failed to reject transaction.`
60. Verifikasi form keputusan tetap terbuka dengan catatan utuh
61. Lepas intercept keputusan
62. Verifikasi status seed 249 tetap `Waiting for Approval`

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 14, 24 (Search dan tab untuk menemukan baris target, R-16), 4, 9, 15, 18, 26, 30, 38, 45, 46, 51, 57, 61 (memasang dan melepas intercept, S-09), 20 (membuka surface), 23 dan 35 (membuka ulang List sesudah Wallet dan sesudah mengatur toggle, sehingga tab Current aktif dan Search sebelumnya bersih; `[+ Allocation]` dan baseline jumlah baris tab Current berjalan di List yang bersih), 36 (baseline S-12), 22 dan 34 (mengatur toggle), 55 (ganti akun), 10 sampai 12, 31 sampai 33, dan 52 sampai 54 (menutup form dirty `[×]`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Spec melewati sekitar 35 langkah (62 langkah). Alasan pertahanan: seluruh blok satu kelas harness (fault injection pada aksi tulis) dengan pola pasang-intercept, aksi, amati, lepas, dan tiap blok berdiri sendiri dengan seed sendiri.
- Asersi tidak ada record baru dan tidak ada mutasi wallet pada TC-AC-LA-471 (langkah 43 dan 44) berbaseline (langkah 36). 
- Pembagian TC lintas spec: TC-AC-LA-419 (tidak ada entri log baru saat Cancel gagal) dan klausa log TC-AC-LA-471 c (tidak ada log saat Allocate gagal) ada di spec 094 (absence log).
- Temuan untuk QA:
  - Penutup form dirty ditulis `[×]` sesuai S-08 (keputusan 2026-11-02); TC-AC-LA-177 dan PRD §4.4 menulis `[✕]`, spec mengikuti konvensi.
  - TC-AC-LA-197, 224, 236, 471, 472, 249 tidak menyebut endpoint yang di-intercept; disediakan tim FE (S-13).
  - TC-AC-LA-472 Langkah 1 ("respons tidak pernah kembali") tidak menyebut batas waktu tunggu klien; spec mengasersi toast `Connection problem. Please try again.` sesudah timeout terjadi.
  - TC-AC-LA-472 melanjutkan form pada TC-AC-LA-471 (form belum ditutup); spec memakai form yang sama karena precondition identik (P-3 tidak diperlukan, form yang sama tanpa state berat).
  - TC-AC-LA-471 dan TC-AC-LA-472 Precondition d tidak menyebut Target dan Type; spec memakai Target `SUBS-20260101-A1B2C` dan Type `Concurrent User`.
