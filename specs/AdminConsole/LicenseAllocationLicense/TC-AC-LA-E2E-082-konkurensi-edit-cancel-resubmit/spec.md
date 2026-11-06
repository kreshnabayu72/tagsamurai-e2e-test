---
id: TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit
title: "Konkurensi Edit, Cancel, dan Resubmit: Alokasi Diputus Pihak Lain dan Target Berubah"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-LA-201
  - TC-AC-LA-202
  - TC-AC-LA-203
  - TC-AC-LA-225
  - TC-AC-LA-235
coverage:
  web: automated
---

# Konkurensi Edit, Cancel, dan Resubmit: Alokasi Diputus Pihak Lain dan Target Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Create+Read+Update `dewiFullLic_automated_{namaCompany}@qwertysystem.net` (`Dewi Anggraini`, Pre-setup #4), password `Spectra.env.AC_LA_DIST_FULL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: `beforeEach` suite menjadi jaring pengaman S-09 dan flag Guided Tooltip diset `seen`, sesuai `suite.md`.
- `Fixture.license-allocation-license` belum ada (disediakan tim FE): memuat identitas akun, nama Client, ID Subscription, dan harga.
- Data Pre-setup: Klinik Harapan Bunda (#24) yang Subscription Paid Active-nya di-Cancel sesi lain pada TC-AC-LA-202 (dipulihkan oleh fixture backend yang disediakan tim FE/BE di langkah penghubung 31 dan hook `after`, S-06 pengecualian 2026-10-30; term `SUBS-20260101-A1B2C` Client seed dipulihkan di langkah penghubung 43 dan hook `after`), kantong wallet (#33), Product Price (#34), toggle Require Approval for Allocation ON (#38).
- Data Dinamis (seeding lewat API di hook `before`, milik spec ini): satu Client bersuffix `PT Sejahtera {runId}-082` binaan Distributor PT Maju Bersama dengan term FAMS Professional Paid Active `SUBS-20260101-A1B2C` (bentuk PT Sejahtera #19) yang term-nya di-Cancel pada TC-AC-LA-203 dan TC-AC-LA-235; alokasi `Waiting for Approval` Concurrent User +5 oleh `Dewi A` (bentuk #41) untuk TC-AC-LA-201 (di-Reject sesi lain), TC-AC-LA-203, dan TC-AC-LA-225 (di-Approve sesi lain), masing-masing satu seed; alokasi `Waiting for Approval` Asset Control Station +2 `Client-wide` dan Storage +50 GB `Client-wide` Klinik Harapan Bunda (bentuk #45) untuk TC-AC-LA-202; alokasi `Canceled` manual Concurrent User +5 (bentuk #48) pada Client seed untuk TC-AC-LA-235. Allocation ID dibaca dari hasil seeding.
- Pelaku kedua: sesi API aktor (Reject, Approve, Cancel Subscription); akun pelaku tidak ditulis di TC (disediakan tim FE). Login API tidak dihitung sebagai sesi web (`suite.md`).
- State global yang diubah: status Subscription Klinik Harapan Bunda dan Client seed. Dipulihkan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-LA-201: Edit pada alokasi yang sudah di-Reject sesi lain, dialog D-01

1. Ketik Search Allocation ID seed 201 di tab Current, tekan Enter
2. Klik row action `Edit` pada baris seed 201 (Form Edit terbuka)
3. Pelaku kedua (sesi API) me-Reject alokasi itu dengan Rejection Reason `Kuota tidak sesuai` hingga tersimpan
4. Tunggu aksi selesai
5. Ubah Quantity, lalu klik `[Save]`
6. Verifikasi dialog D-01 dengan Title `Request No Longer Available`, Body `This allocation has already been decided or canceled. The latest status has been loaded.`, dan tombol `[OK]`
7. Klik `[OK]`
8. Verifikasi data alokasi seed 201 tidak berubah
9. Verifikasi List dimuat ulang

### TC-AC-LA-202: Station atau Storage pada Edit, gate Paid Active dicek ulang

10. Ganti isi kotak search dengan Allocation ID seed Station di tab Current, tekan Enter, lalu klik row action `Edit` pada record Asset Control Station
11. Pelaku kedua (sesi API) meng-Cancel seluruh Subscription Paid Active Klinik Harapan Bunda hingga tersimpan
12. Tunggu aksi selesai
13. Ubah Quantity, lalu klik `[Save]`
14. Verifikasi pesan `Asset Control Station requires at least one active paid subscription.`
15. Verifikasi Target dikosongkan
16. Verifikasi Client dipertahankan
17. Verifikasi Quantity dipertahankan
18. Klik `[×]`
19. Verifikasi dialog `Unsaved Changes`
20. Klik `[Leave]`
21. Verifikasi data lama alokasi Station utuh
22. Ganti isi kotak search dengan Allocation ID seed Storage, tekan Enter, klik row action `Edit` pada record Storage, ubah Quantity, lalu klik `[Save]`
23. Verifikasi pesan `Storage requires at least one active paid subscription.`
24. Verifikasi Target dikosongkan
25. Verifikasi Client dipertahankan
26. Verifikasi Quantity dipertahankan
27. Klik `[×]`
28. Verifikasi dialog `Unsaved Changes`
29. Klik `[Leave]`
30. Verifikasi data lama alokasi Storage utuh
31. Pulihkan Subscription Klinik Harapan Bunda lewat fixture backend hingga tersimpan

### TC-AC-LA-203: Edit memvalidasi ulang Target dan kombinasi Type terhadap Product

32. Ganti isi kotak search dengan Allocation ID seed 203 di tab Current, tekan Enter, lalu klik row action `Edit` pada baris seed 203
33. Pelaku kedua (sesi API) meng-Cancel Subscription term Target hingga tersimpan
34. Tunggu aksi selesai
35. Ubah Quantity, lalu klik `[Save]`
36. Verifikasi pesan `This target no longer exists. Please select another.`
37. Verifikasi Target dikosongkan
38. Verifikasi Quantity dipertahankan
39. Klik `[×]`
40. Verifikasi dialog `Unsaved Changes`
41. Klik `[Leave]`
42. Verifikasi data lama alokasi seed 203 utuh
43. Pulihkan term Subscription `SUBS-20260101-A1B2C` Client seed lewat fixture backend hingga tersimpan

### TC-AC-LA-225: Cancel pada alokasi yang sudah di-Approve sesi lain, D-01

44. Ganti isi kotak search dengan Allocation ID seed 225 di tab Current, tekan Enter (List dimuat)
45. Pelaku kedua (sesi API) meng-Approve alokasi seed 225 hingga tersimpan
46. Tunggu aksi selesai
47. Klik row action `Cancel Allocation` pada baris seed 225
48. Klik `[Cancel Request]`
49. Verifikasi dialog D-01 `Request No Longer Available` dengan `[OK]`
50. Verifikasi status terbaru dimuat
51. Verifikasi alokasi seed 225 tidak dibatalkan
52. Klik `[OK]` untuk menutup dialog D-01

### TC-AC-LA-235: Resubmit memvalidasi ulang Target, V-07

53. Klik tab `Current`, kosongkan kotak search: klik `✕` pada Search, tekan Enter, lalu catat baseline Allocation ID baris di halaman pertama
54. Klik tab `History`, ketik Search Allocation ID seed 235, tekan Enter, lalu klik row action `Resubmit` pada baris Canceled milik sendiri
55. Pelaku kedua (sesi API) meng-Cancel Subscription term Target `SUBS-20260101-A1B2C` Client seed hingga tersimpan
56. Tunggu aksi selesai
57. Klik `[Submit]`
58. Verifikasi pesan `This target no longer exists. Please select another.`
59. Verifikasi Target dikosongkan
60. Verifikasi Type ikut di-reset
61. Verifikasi Client dipertahankan
62. Verifikasi Additional Quantity `5` dipertahankan
63. Klik `[×]`
64. Verifikasi dialog `Unsaved Changes`
65. Klik `[Leave]`
66. Klik `(←)` pada kotak Search
67. Verifikasi record asal seed 235 tetap `Canceled` di tab History (anchor)
68. Klik tab `Current`, kosongkan kotak search: klik `✕` pada Search, tekan Enter
69. Verifikasi tidak ada record baru (Allocation ID baris di halaman pertama sama dengan baseline langkah 53)

## Notes

- Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 10, 22, 32, 44, 54 (Search dan tab untuk menemukan baris target, R-16), 53 (mengosongkan Search lalu baseline Allocation ID halaman pertama tab Current sebelum Resubmit, S-12), 66 (`(←)` pada kotak Search tab History), 68 (pindah ke tab Current dan mengosongkan Search dengan klik `✕` lalu Enter; spec tidak mengandalkan apakah kotak Search dipertahankan saat pindah tab), 4, 12, 34, 46, 56 (menunggu aksi selesai karena berganti sesi, 8b butir 8), 31 dan 43 (memulihkan Pre-setup dan term Client seed lewat fixture backend; langkah 43 memastikan blok TC-AC-LA-225 dan TC-AC-LA-235 berjalan pada term aktif, bukan term yang sudah di-Cancel di langkah 33), 7 dan 52 (menutup dialog D-01 dengan `[OK]` sebelum langkah berikutnya, S-09), langkah dialog `Unsaved Changes` (S-08).
- Penyimpangan data (S-06): TC memakai Pre-setup #41, #45, #48, dan PT Sejahtera (#19) yang term-nya di-Cancel; spec memakai seed dan Client milik spec dengan bentuk yang sama.
- Asersi tidak ada record baru (langkah 69) berbaseline (S-12): baseline langkah 53 dicatat sebelum Resubmit, Search dikosongkan secara eksplisit dengan klik `✕` lalu Enter pada langkah 53 sebelum baseline dicatat dan pada langkah 68 sebelum pembanding, dan anchor positif langkah 67 (record asal seed 235 tetap `Canceled` di tab History) mendahului absence.
- Pelaku kedua lewat sesi API (langkah 3, 11, 33, 45, 55) tidak memakai butir `P-2` (bagian 3).
- Pemulihan term (S-09, S-06): term `SUBS-20260101-A1B2C` Client seed di-Cancel pelaku kedua di langkah 33 (TC-AC-LA-203); langkah 43 memulihkannya lewat fixture backend (pola langkah 31) sebelum blok TC-AC-LA-225, agar hasil blok itu bukan akibat sisa state blok sebelumnya. Langkah 55 (TC-AC-LA-235) kembali meng-Cancel term yang sama dan dipulihkan hook `after`.
- Spec melewati sekitar 35 langkah (69 langkah). Alasan pertahanan: seluruh blok satu kelas harness (multi-konteks dengan pelaku kedua sesi API) dan satu pola alur (aksi UI terbuka lalu sesi lain mengubah state); tiap blok berdiri sendiri dengan seed sendiri.
- Temuan untuk QA:
  - TC-AC-LA-201, 202, 203, 225, 235 tidak menyebut akun dan mekanisme pelaku "sesi lain"; disediakan tim FE.
  - TC-AC-LA-225 menyebut `[OK]` pada D-01 tanpa langkah menutup dialog; langkah 52 menutup dialog sebelum blok TC-AC-LA-235 membuka tab `History`.
  - TC-AC-LA-201 Expected tidak menyebut keadaan form Edit sesudah `[OK]`; tidak diasersi.
  - TC-AC-LA-225 Langkah 1 menyebut baris yang sudah di-Approve sebelum klik tanpa menyebut bahwa List belum dimuat ulang; spec memuat List sebelum Approve sesi lain.
  - TC-AC-LA-203 Expected b ("Target dikosongkan, Quantity dipertahankan") menyebut kombinasi Type tidak diasersi; hanya Target dan Quantity.
  - TC-AC-LA-202 Langkah 3 ("Ulangi untuk record Storage") tidak menyebut apakah Cancel sesi lain diulang; spec tidak mengulang karena gate sudah gugur.
