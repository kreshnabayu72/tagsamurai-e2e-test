---
id: TC-FA-CAT-E2E-094-siklus-excess-plan-naik-melepas-excess-dan-log-restored
title: "Siklus Excess: Plan Naik Melepas Excess dan Log Restored from Excess pada Tiga Surface"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAT-314
  - TC-FA-CAT-472
  - TC-FA-CAT-471
  - TC-FA-CAT-470
  - TC-FA-CAT-315
coverage:
  web: automated
---

# Siklus Excess: Plan Naik Melepas Excess dan Log Restored from Excess pada Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini pada client CatExcess (Pre-setup #31); halaman dibuka hook `beforeEach` suite. Langkah 43 berganti akun ke Total Control client CatOver (Pre-setup #41); hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua lewat sesi API (butir hook suite di `suite.md`): Principal Automation (Pre-setup #11, akun disediakan tim FE) mengubah plan pada langkah 2 dan 46; Total Control Kedua (Pre-setup #46, akun disediakan tim FE) menghapus kategori pada langkah 33. Keduanya hanya pemicu perubahan state; tidak ada sesi UI kedua.
- Data Pre-setup #31 (CatExcess, plan Starter cap 5, 9 kategori): usable `Electronics` (anak `Laptop`, `Monitor`), `Office`, `Spare Parts` (anak `Old Parts`); Excess `Furniture`, `Heavy Equipment`, `Vehicle`, `Old Parts`. Pemulihan Pre-setup #31 (plan, status, dan kategori) lewat fixture backend yang disediakan tim FE/BE pada langkah 18 dan 29 serta di hook `after`.
- Data Pre-setup #41 (CatOver, plan Starter cap 5): 25 kategori dengan 20 node Excess. Pemulihan lewat fixture pada langkah 44.
- Parameter iterasi langkah 5 sampai 7:

  | Baris |
  |---|
  | `Heavy Equipment` |
  | `Vehicle` |
  | `Furniture` |
  | `Old Parts` |

- State yang diubah spec: plan client CatExcess dan CatOver, kategori CatExcess (penghapusan pada langkah 20 dan 33). Suite berjalan serial (`parallel: false`).
- Kemampuan teknis (disediakan tim FE/BE): membaca jumlah baris Modal Changelog per Action (NR untuk `Restored from Excess (Category Consolidation)`), Activity Log (NA), dan System Log akun (NS) sebelum aksi (S-12, 8b.10) pada langkah 1, 19, 30, dan 45.
- Seed dan pemulihan client Pre-setup mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite.
- Env var `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-FA-CAT-314: Plan naik dengan cap sama atau di atas jumlah kategori melepas seluruh Excess (System)

1. Catat baseline NR, NA, dan NS (System Log Total Control)
2. Principal Automation (sesi API) menaikkan plan client CatExcess dari Starter ke Professional (cap 100) hingga tersimpan
3. Muat ulang halaman Categories
4. Verifikasi `Heavy Equipment`, `Vehicle`, `Furniture`, dan `Old Parts` berstatus usable (tidak redup)
5. Untuk setiap baris di tabel parameter (langkah 5 sampai 7): klik elipsis (⋯) pada baris
6. Verifikasi menu baris memuat Edit dan + Add Subcategory
7. Tutup menu baris
8. Verifikasi Alert Category Consolidation hilang
9. Buka Modal Changelog dan filter Modified By `System`
10. Verifikasi Changelog bertambah tepat empat baris `Restored from Excess (Category Consolidation)` (NR + 4) untuk `Heavy Equipment`, `Vehicle`, `Furniture`, dan `Old Parts`
11. Verifikasi tiap baris baru berisi Field `Excess`, Old Value `Excess`, dan New Value `Usable`
12. Verifikasi Modified By tiap baris baru adalah `System`
13. Hapus filter Modified By dan tutup Modal Changelog

### TC-FA-CAT-472: Log Restored from Excess akibat plan naik, System pada Changelog dan Activity Log saja

14. Buka Activity Log
15. Verifikasi Activity Log bertambah tepat empat baris `Restored from Excess (Category Consolidation)` (NA + 4) dengan Modified By `System`
16. Buka Detail User Total Control > Tab System Log
17. Verifikasi jumlah baris System Log Total Control sama dengan NS (tidak memuat baris `Restored from Excess (Category Consolidation)`)

### TC-FA-CAT-471: Log Restored from Excess akibat Delete, aktor Delete pada tiga surface

18. Pulihkan Pre-setup #31 (plan Starter, status awal) lewat fixture dan muat ulang halaman Categories
19. Catat baseline NR, NA, dan NS (System Log Total Control)
20. Hapus `Heavy Equipment`, `Vehicle`, dan `Spare Parts` (beserta `Old Parts`) berurutan sehingga jumlah kategori mencapai cap 5
21. Buka Modal Changelog
22. Verifikasi Changelog bertambah tepat satu baris `Restored from Excess (Category Consolidation)` untuk `Furniture` (NR + 1)
23. Verifikasi baris itu berisi Field `Excess`, Old Value `Excess`, dan New Value `Usable`
24. Verifikasi Modified By baris itu adalah aktor Total Control
25. Tutup Modal Changelog dan buka Detail User Total Control > Tab System Log
26. Verifikasi System Log Total Control memuat baris yang sama dengan Object `Categories` dan Name `Furniture` (NS + 1)
27. Buka Activity Log
28. Verifikasi Activity Log memuat baris yang sama dengan Modified By aktor Total Control (NA + 1)

### TC-FA-CAT-470: Log Restored from Excess saat Delete sesi lain mendahului Wizard Submit, aktor Delete pada tiga surface

29. Pulihkan Pre-setup #31 (plan Starter, status awal) lewat fixture dan muat ulang halaman Categories
30. Catat baseline NR, NA, dan NS2 (System Log Total Control Kedua)
31. Klik `[Choose Categories]` pada Alert Category Consolidation
32. Centang `Keep usable` pada `Furniture`, `Electronics`, `Laptop`, `Monitor`, dan `Office`
33. Total Control Kedua (sesi API) menghapus `Heavy Equipment`, `Vehicle`, dan `Spare Parts` (beserta `Old Parts`) hingga tersimpan sehingga jumlah sama dengan cap
34. Tunggu aksi selesai
35. Klik `[Save Selection]`
36. Buka Modal Changelog
37. Verifikasi Changelog bertambah tepat satu baris `Restored from Excess (Category Consolidation)` untuk `Furniture` (NR + 1) dengan Field `Excess`, Old Value `Excess`, dan New Value `Usable`
38. Verifikasi Modified By baris itu adalah Total Control Kedua (aktor Delete), bukan aktor Wizard
39. Tutup Modal Changelog dan buka Detail User Total Control Kedua > Tab System Log
40. Verifikasi System Log Total Control Kedua memuat baris yang sama dengan Object `Categories` dan Name `Furniture` (NS2 + 1)
41. Buka Activity Log
42. Verifikasi Activity Log memuat baris yang sama dengan Modified By Total Control Kedua (NA + 1)

### TC-FA-CAT-315: Plan naik dengan cap baru yang masih di bawah jumlah kategori tidak melepas Excess

43. Ganti akun: logout, lalu login sebagai Total Control client CatOver (Pre-setup #41) dengan `Spectra.env.FA_TC_PASSWORD`
44. Pulihkan Pre-setup #41 (plan Starter, 20 node Excess) lewat fixture dan muat ulang halaman Categories
45. Catat baseline N jumlah baris Modal Changelog
46. Principal Automation (sesi API) menaikkan plan client CatOver dari Starter ke Growth (cap Category count 20; jumlah kategori 25) hingga tersimpan
47. Muat ulang halaman Categories
48. Verifikasi status Excess kedua puluh node tidak berubah (tidak ada pelepasan sebagian)
49. Verifikasi Alert Category Consolidation tampil dengan `Your plan allows 20 categories`
50. Verifikasi Alert Category Consolidation tampil dengan `You have 25 categories. Choose which categories stay active.`
51. Buka Modal Changelog
52. Verifikasi jumlah baris Changelog sama dengan N (tidak ada baris Changelog baru)
53. Tutup Modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md`.
- Spec melewati sekitar 35 langkah (53 langkah nominal, sekitar 62 dengan ekspansi langkah 5 sampai 7 untuk empat baris). Alasan: seluruh blok satu kelas (harness eksternal: perubahan plan oleh Principal dan Delete oleh pelaku kedua yang diamati lewat tiga surface log) dan berdiri sendiri; tiap blok memulai dari seed yang dipulihkan, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-FA-CAT-472 memakai state hasil TC-FA-CAT-314 sebagai preconditionnya sendiri ("plan telah dinaikkan Principal"), `P-1`: state berat dibangun langkah sebelumnya di spec asal. TC-FA-CAT-315 diletakkan terakhir karena berganti client (S-10).
- Pelaku kedua memakai sesi API sehingga bukan konteks UI kedua (konvensi bagian 3, P-2 butir 2026-10-30); tidak ada butir `P-2`.
- Pembagian TC lintas spec: Expected a TC-FA-CAT-472 (Changelog memuat baris `Restored` Modified By `System`) dibuktikan pada langkah 10 sampai 12 karena state-nya identik dengan TC-FA-CAT-314.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 19, 30, 45 (baseline), 2, 33, 46 (pemicu), 3, 47 (muat ulang), 7 (menutup menu), 13, 25, 39, 53 (menutup Modal Changelog), 18, 29, 44 (pemulihan seed), 34 (menunggu aksi selesai).
- Asersi jumlah langkah 17 dan 52 (tidak ada baris baru) memakai selisih terhadap baseline dan langkah 15 serta 48 sebagai anchor positif (8b.2).
- Temuan untuk QA:
  - TC-FA-CAT-472 Expected b menyebut "System Log user mana pun"; spec hanya dapat membaca System Log aktor Total Control (langkah 16 dan 17).
  - TC-FA-CAT-470 menyebut "mencentang 5 kategori" tanpa nama; spec mencentang lima kategori yang tersisa setelah Delete (`Furniture`, `Electronics`, `Laptop`, `Monitor`, `Office`).
  - TC-FA-CAT-315 Expected b menyebut "Tidak ada Wizard baru" tanpa kriteria yang dapat diamati; spec mengasersi Alert tetap tampil dengan teksnya.
  - TC-FA-CAT-314, 315, dan 470 berlabel "Manual Only, dua sesi paralel" tetapi pelaku kedua hanya memicu perubahan state; spec memakai sesi API.
