---
id: TC-FA-CAT-E2E-091-wizard-pra-t0-seleksi-kosong-downgrade-dibatalkan-dan-plan-target-naik
title: "Wizard Pra-T-0: Seleksi Kosong, Downgrade Dibatalkan, dan Plan Target Naik Sebelum T-0"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-CAT-604
  - TC-FA-CAT-605
  - TC-FA-CAT-606
coverage:
  web: automated
---

# Wizard Pra-T-0: Seleksi Kosong, Downgrade Dibatalkan, dan Plan Target Naik Sebelum T-0

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatPreT0 (Pre-setup #32); halaman dibuka hook `beforeEach` suite. Langkah 32 berganti akun ke Total Control client CatPreT0Big (Pre-setup #45); hook `after` mengembalikan sesi ke akun default suite.
- Principal Automation (Pre-setup #11) lewat sesi API (butir hook suite di `suite.md`; akun disediakan tim FE) mengubah plan: membatalkan downgrade terjadwal (langkah 23) dan mengubah plan target downgrade (langkah 37).
- Data Pre-setup #32 (CatPreT0, downgrade terjadwal dari Professional cap 100 ke Starter cap 5, T-0 belum tiba): 8 kategori `Alpha Tech`, `Beta Tools`, `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, `Eta Furniture`, `Theta Heavy`.
- Data Pre-setup #45 (CatPreT0Big, T-0 belum tiba, plan target downgrade Starter cap 5): 25 kategori `Bulk 01` sampai `Bulk 25`.
- State yang diubah spec: jam server, seleksi tersimpan, kategori CatPreT0 (penghapusan pada langkah 6), dan plan CatPreT0 serta CatPreT0Big (Principal). Pemulihan seed, plan, dan jam dilakukan fixture backend (disediakan tim FE/BE) pada langkah 17 serta di hook `after`. Suite berjalan serial (`parallel: false`).
- Waktu: T-0 dibaca dari data downgrade terjadwal client lewat API seeding (8b.3); jam server dan jam browser diatur bersama ke T-0 pada langkah 8, 24, dan 39 (bagian 6 konvensi). Kemampuan disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action sebelum aksi (baseline NM untuk `Marked as Excess (Category Consolidation)`, S-12).
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-604: Seluruh Category tercentang dihapus sebelum T-0, seleksi kosong dibuang dan fallback berlaku

1. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
2. Centang `Keep usable` pada `Alpha Tech` dan `Beta Tools`
3. Klik `[Save Selection]`
4. Tunggu aksi selesai
5. Buka Fixed Asset > Settings > Categories
6. Hapus `Alpha Tech` dan `Beta Tools` lewat row action Delete sehingga jumlah kategori menjadi 6
7. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
8. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
9. Buka Fixed Asset > Settings > Categories
10. Verifikasi `Gamma Parts`, `Delta Supply`, `Epsilon Gear`, `Zeta Vehicle`, dan `Eta Furniture` (lima kategori terlama) berstatus usable
11. Verifikasi `Theta Heavy` berstatus Excess
12. Verifikasi Alert Category Consolidation tampil untuk Total Control (jumlah 6 melebihi cap 5)
13. Buka Modal Changelog
14. Verifikasi Changelog bertambah tepat satu baris `Marked as Excess (Category Consolidation)` (NM + 1) untuk `Theta Heavy`
15. Verifikasi Modified By baris baru itu adalah `System`
16. Tutup Modal Changelog

### TC-FA-CAT-605: Downgrade terjadwal dibatalkan sebelum T-0 membuang seleksi tersimpan

17. Pulihkan seed Pre-setup #32, plan, dan jam lewat fixture, lalu muat ulang halaman Categories
18. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation`
19. Centang `Keep usable` pada `Alpha Tech`, `Beta Tools`, `Gamma Parts`, dan `Delta Supply`
20. Klik `[Save Selection]`
21. Tunggu aksi selesai
22. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
23. Principal Automation (sesi API) membatalkan downgrade terjadwal CatPreT0 lewat support (plan tetap Professional) hingga tersimpan
24. Majukan jam server dan jam browser ke T-0 (cap plan baru 5 berlaku) hingga tersimpan
25. Buka Fixed Asset > Settings > Categories
26. Verifikasi kedelapan kategori berstatus usable (seleksi tersimpan tidak diterapkan)
27. Verifikasi tidak ada node Excess
28. Verifikasi Alert Category Consolidation tidak tampil
29. Buka Modal Changelog
30. Verifikasi jumlah baris `Marked as Excess (Category Consolidation)` sama dengan NM
31. Tutup Modal Changelog

### TC-FA-CAT-606: Plan target naik sebelum T-0 (Starter ke Growth), seleksi tersimpan dipakai bila X <= cap baru

32. Ganti akun: logout, lalu login sebagai Total Control client CatPreT0Big (Pre-setup #45) dengan `Spectra.env.FA_TC_PASSWORD`
33. Buka Fixed Asset > Wizard Reconciliation > step `Category Consolidation` (plan target Starter, cap 5)
34. Centang `Keep usable` pada `Bulk 01`, `Bulk 02`, `Bulk 03`, dan `Bulk 04`
35. Klik `[Save Selection]`
36. Tunggu aksi selesai
37. Principal Automation (sesi API) mengubah plan target downgrade CatPreT0Big dari Starter (cap 5) menjadi Growth (cap 20) hingga tersimpan
38. Catat baseline NM jumlah baris Changelog `Marked as Excess (Category Consolidation)`
39. Majukan jam server dan jam browser ke T-0 (plan target Growth berlaku) hingga tersimpan
40. Buka Fixed Asset > Settings > Categories
41. Verifikasi `Bulk 01`, `Bulk 02`, `Bulk 03`, dan `Bulk 04` berstatus usable (seleksi dipakai, 4 <= 20)
42. Verifikasi `Bulk 05` sampai `Bulk 25` (21 kategori) berstatus Excess (kuota yang tidak terpakai tidak diisi otomatis dan fallback tidak berjalan)
43. Buka Modal Changelog
44. Verifikasi Changelog bertambah tepat 21 baris `Marked as Excess (Category Consolidation)` (NM + 21) untuk `Bulk 05` sampai `Bulk 25`
45. Verifikasi Modified By tiap baris baru adalah aktor Total Control yang men-submit
46. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (46 langkah nominal). Alasan: seluruh blok satu kelas (harness eksternal: time-travel T-0 dengan pengubahan plan oleh Principal) dan berdiri sendiri; tiap blok memulai dari seed yang dipulihkan sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. TC-FA-CAT-606 diletakkan terakhir karena berganti client (S-10).
- Principal Automation lewat sesi API bukan konteks kedua (tidak ada `P-2`).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 4, 21, 36 (menunggu aksi selesai), 5, 9, 25, 40 (navigasi), 7, 22, 38 (baseline), 8, 24, 39 (pemicu T-0), 16, 31, 46 (menutup Modal Changelog), 17 (pemulihan seed).
- Asersi absence langkah 27, 28, dan 30 memakai langkah 26 (kategori usable tampil pada halaman yang sama) dan selisih terhadap baseline sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-606 tidak menyebut apakah `Bulk 01` sampai `Bulk 25` dibuat berurutan menurut waktu pembuatan; tidak berpengaruh karena fallback tidak berjalan.
  - TC-FA-CAT-605 menyebut dua perubahan sekaligus ("membatalkan downgrade lewat support"); spec memicunya sebagai satu langkah Principal tanpa mengarang mekanisme support.
