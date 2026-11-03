---
id: TC-FA-CAT-E2E-092-wizard-pra-t0-plan-target-turun-submit-ulang-dan-siklus-downgrade-baru
title: "Wizard Pra-T-0: Plan Target Turun, Submit Ulang, dan Siklus Downgrade Baru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-607
  - TC-FA-CAT-608
  - TC-FA-CAT-609
  - TC-FA-CAT-610
coverage:
  web: automated
---

# Wizard Pra-T-0: Plan Target Turun, Submit Ulang, dan Siklus Downgrade Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatPreT0Big (Pre-setup #45); halaman dibuka hook `beforeEach` suite. Langkah 34 berganti akun ke Total Control client CatCycle (Pre-setup #44); hook `after` mengembalikan sesi ke akun default suite.
- Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) mengubah plan target downgrade pada langkah 5 dan 20.
- Data Pre-setup #45 (CatPreT0Big, T-0 belum tiba; varian plan target awal Growth cap 20): 25 kategori `Bulk 01` sampai `Bulk 25`.
- Data Pre-setup #44 (CatCycle, plan target Starter cap 5): 25 kategori `Cyc 01` sampai `Cyc 25`; varian TC-FA-CAT-609: T-0 siklus baru belum tiba, hasil siklus 1 meninggalkan `Cyc 01` sampai `Cyc 05` Excess dan `Cyc 06` sampai `Cyc 25` usable; varian TC-FA-CAT-610: kondisi yang sama tanpa Submit pada siklus baru.
- State yang diubah spec: jam server, seleksi tersimpan, plan target downgrade CatPreT0Big dan status kategori CatPreT0Big dan CatCycle. Pemulihan seed, plan, dan jam dilakukan fixture backend (disediakan tim FE/BE) pada langkah 15 dan 55 serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 7, 26, 46, dan 57 (bagian 6 konvensi). Kemampuan disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action sebelum aksi (baseline NM untuk `Marked as Excess (Category Consolidation)`, NR untuk `Restored from Excess (Category Consolidation)`, S-12) pada langkah 6, 25, 45, dan 56.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-607: Plan target turun sebelum T-0 (Growth ke Starter) di bawah jumlah tercentang, seleksi dibuang dan fallback berlaku

1. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation` (plan target Growth, cap 20)
2. Centang `Keep usable` pada `Bulk 01` sampai `Bulk 06`
3. Klik `[Save Selection]`
4. Tunggu aksi selesai
5. Principal Automation (sesi API) mengubah plan target downgrade CatPreT0Big dari Growth (cap 20) menjadi Starter (cap 5) hingga tersimpan
6. Catat baseline NM dan NR jumlah baris Changelog
7. Majukan jam server dan jam browser ke T-0 (plan target berlaku, tanpa Submit ulang) hingga tersimpan
8. Buka Fixed Asset > Settings > Categories
9. Verifikasi `Bulk 01` sampai `Bulk 05` (lima kategori terlama) berstatus usable setelah seleksi dibuang dan fallback berlaku
10. Verifikasi `Bulk 06` sampai `Bulk 25` (20 kategori) berstatus Excess
11. Buka Modal Changelog
12. Verifikasi Changelog bertambah tepat 20 baris `Marked as Excess (Category Consolidation)` (NM + 20) untuk `Bulk 06` sampai `Bulk 25`
13. Verifikasi Modified By tiap baris baru adalah `System`
14. Tutup Modal Changelog

### TC-FA-CAT-608: Plan target turun sebelum T-0 lalu Total Control submit ulang, seleksi baru diterapkan bukan fallback

15. Pulihkan seed Pre-setup #45 (varian plan target awal Growth), plan, dan jam lewat fixture, lalu muat ulang halaman Categories
16. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation` (plan target Growth, cap 20)
17. Centang `Keep usable` pada `Bulk 01` sampai `Bulk 06`
18. Klik `[Save Selection]`
19. Tunggu aksi selesai
20. Principal Automation (sesi API) mengubah plan target downgrade CatPreT0Big dari Growth (cap 20) menjadi Starter (cap 5) hingga tersimpan
21. Buka kembali Wizard Reconciliation > step `Category Consolidation`
22. Atur centang `Keep usable` sehingga hanya `Bulk 01`, `Bulk 03`, `Bulk 05`, `Bulk 07`, dan `Bulk 09` yang tercentang
23. Klik `[Save Selection]`
24. Verifikasi toast sukses `Success, category consolidation has been updated.` tampil (Submit ulang diterima, 5 <= cap baru 5)
25. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
26. Majukan jam server dan jam browser ke T-0 (plan target berlaku) hingga tersimpan
27. Buka Fixed Asset > Settings > Categories
28. Verifikasi hanya `Bulk 01`, `Bulk 03`, `Bulk 05`, `Bulk 07`, dan `Bulk 09` yang berstatus usable
29. Verifikasi 20 kategori lain berstatus Excess (fallback tidak berjalan)
30. Buka Modal Changelog
31. Verifikasi Changelog bertambah tepat 20 baris `Marked as Excess (Category Consolidation)` (NM + 20) untuk 20 kategori lain
32. Verifikasi Modified By tiap baris baru adalah aktor Total Control, bukan `System`
33. Tutup Modal Changelog

### TC-FA-CAT-609: Siklus downgrade baru dimulai dari nol, Wizard tanpa pra-isi dan Submit ulang menimpa seleksi

34. Ganti akun: logout, lalu login sebagai Total Control client CatCycle (Pre-setup #44) dengan `Spectra.env.FA_TC_PASSWORD`
35. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
36. Verifikasi Wizard memuat seluruh 25 kategori termasuk `Cyc 01` sampai `Cyc 05` yang Excess dari siklus 1
37. Verifikasi seluruh checkbox `Keep usable` unchecked (hasil Submit siklus 1 tidak dibawa)
38. Centang `Keep usable` pada `Cyc 01`, `Cyc 02`, dan `Cyc 03`
39. Klik `[Save Selection]`
40. Tunggu aksi selesai
41. Buka kembali Wizard Reconciliation > step `Category Consolidation`
42. Atur centang `Keep usable` sehingga hanya `Cyc 01`, `Cyc 24`, dan `Cyc 25` yang tercentang
43. Klik `[Save Selection]`
44. Tunggu aksi selesai
45. Catat baseline NM dan NR jumlah baris Changelog
46. Majukan jam server dan jam browser ke T-0 (plan target berlaku) hingga tersimpan
47. Buka Fixed Asset > Settings > Categories
48. Verifikasi hanya `Cyc 01`, `Cyc 24`, dan `Cyc 25` yang berstatus usable (Submit terakhir menimpa)
49. Buka Modal Changelog
50. Verifikasi Changelog bertambah tepat satu baris `Restored from Excess (Category Consolidation)` untuk `Cyc 01` (NR + 1)
51. Verifikasi Changelog bertambah tepat 18 baris `Marked as Excess (Category Consolidation)` (NM + 18) untuk `Cyc 06` sampai `Cyc 23`
52. Verifikasi Modified By tiap baris baru adalah aktor Total Control
53. Verifikasi tidak ada baris baru untuk `Cyc 02` sampai `Cyc 05` (tetap Excess) serta `Cyc 24` dan `Cyc 25` (tetap usable)
54. Tutup Modal Changelog

### TC-FA-CAT-610: T-0 siklus downgrade baru tanpa Submit, fallback atas seluruh Category tanpa carry-over

55. Pulihkan seed Pre-setup #44 (varian tanpa Submit pada siklus baru) dan jam lewat fixture, lalu muat ulang halaman Categories
56. Catat baseline NM dan NR jumlah baris Changelog
57. Majukan jam server dan jam browser ke T-0 (plan target berlaku) hingga tersimpan
58. Buka Fixed Asset > Settings > Categories
59. Verifikasi `Cyc 01` sampai `Cyc 05` (lima kategori terlama) berstatus usable (hasil siklus 1 tidak dibawa)
60. Verifikasi `Cyc 06` sampai `Cyc 25` (20 kategori) berstatus Excess
61. Buka Modal Changelog
62. Verifikasi Changelog bertambah tepat lima baris `Restored from Excess (Category Consolidation)` (NR + 5) untuk `Cyc 01` sampai `Cyc 05`
63. Verifikasi Changelog bertambah tepat 20 baris `Marked as Excess (Category Consolidation)` (NM + 20) untuk `Cyc 06` sampai `Cyc 25`
64. Verifikasi Modified By seluruh baris baru adalah `System`
65. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (65 langkah nominal). Alasan: seluruh blok satu kelas (harness eksternal: time-travel T-0 dengan pengubahan plan target oleh Principal) pada client berseed 25 kategori dan berdiri sendiri; tiap blok memulai dari seed yang dipulihkan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-609 dan TC-FA-CAT-610 diletakkan terakhir karena berganti client (S-10).
- Principal Automation lewat sesi API bukan konteks kedua (tidak ada `P-2`).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 19, 40, 44 (menunggu aksi selesai), 6, 25, 45, 56 (baseline), 7, 26, 46, 57 (pemicu T-0), 8, 27, 47, 58 (navigasi), 14, 33, 54, 65 (menutup Modal Changelog), 15, 55 (pemulihan seed).
- Asersi tidak ada baris langkah 53 memakai langkah 50 dan 51 (baris baru tampil di Changelog yang sama) sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-608 langkah 5 dan TC-FA-CAT-609 langkah 4 menyuruh "pastikan hanya" kategori tertentu tercentang tanpa menyebut apakah Wizard terisi dari Submit sebelumnya; spec menulis "atur centang sehingga hanya ..." untuk menutup kedua kemungkinan.
  - TC-FA-CAT-609 tidak menyebut data Pre-setup #44 untuk TC-FA-CAT-610 secara terpisah; spec memakai varian seed tanpa Submit pada siklus baru.
