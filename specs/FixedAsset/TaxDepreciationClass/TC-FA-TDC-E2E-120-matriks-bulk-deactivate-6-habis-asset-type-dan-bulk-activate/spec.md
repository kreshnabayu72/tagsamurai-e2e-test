---
id: TC-FA-TDC-E2E-120-matriks-bulk-deactivate-6-habis-asset-type-dan-bulk-activate
title: "Matriks Bulk Deactivate 6 Habis Asset Type dan Bulk Activate"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-456
  - TC-FA-TDC-457
  - TC-FA-TDC-458
  - TC-FA-TDC-459
  - TC-FA-TDC-460
  - TC-FA-TDC-461
coverage:
  web: automated
---

# Matriks Bulk Deactivate 6 Habis Asset Type dan Bulk Activate

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun dan email disediakan tim FE (email tidak tertulis di TC); password lewat `Spectra.env.FA_TC_PASSWORD`.
- Hook suite, seeding dan pemulihan lewat API, serta flag Guided Tooltip mengikuti `suite.md`.
- Data Pre-setup (dataset spec ini, `Fixture.fixedAssetTaxDepreciationClass.dataset120`, di-seed lewat API di hook `before` dan dipulihkan di hook `after`): tabel satu halaman (9 class) berisi BLD-P dan BLD-NP (satu-satunya class Active bertipe Building, Used By 0), LAND (satu-satunya class Active bertipe Land, Used By 0), NB-1, NB-2, NB-4, dan NB-SL (Active, bertipe Non-building, Used By 0 di awal spec), serta NB-OLD dan NB-OLD2 (Inactive, Used By 0). Tidak ada Asset Class yang memakai class mana pun di awal spec (TC-FA-TDC-459). Kode class ditulis literal sesuai TC tanpa suffix `{runId}-<NNN>` (S-12): Class Code maksimal 15 karakter sehingga suffix tidak muat (lihat Temuan untuk QA). Data Dinamis: tidak ada.
- Kemampuan teknis: mencentang checkbox baris; seeding Asset Class pemakai NB-2 dan pemulihan status class lewat API di tengah spec (sesi API aktor sesuai `suite.md`); kemampuan baca jumlah entri Changelog (baseline sebelum aksi dan jumlah sesudahnya, S-12) disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- State global yang diubah: Used By NB-2 (3 sesudah langkah 20), status Active BLD-P, BLD-NP, NB-OLD, dan NB-OLD2; seluruhnya dipulihkan di hook `after` ke dataset awal.

## Test Steps

### TC-FA-TDC-456: Matriks 6a: Bulk Deactivate yang menghabiskan class Active satu Asset Type, semua lolos

1. Centang checkbox baris BLD-P dan BLD-NP
2. Klik `Deactivate` pada Bulk Action Bar
3. Verifikasi dialog "Deactivate Tax Depreciation Classes" memuat Alert `severity="warning"` dengan teks "No active Building class will remain. New asset classes of that type cannot be set up."
4. Verifikasi body dialog memuat bullet `• BLD-P – Bangunan permanen` dan `• BLD-NP – Bangunan tidak permanen`
5. Verifikasi body dialog memuat kalimat "Are you sure you want to deactivate them?"
6. Klik `[Cancel]` pada dialog
7. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-458: Bulk Deactivate yang menghabiskan class Active dua Asset Type menampilkan satu Alert per Asset Type

8. Centang checkbox baris BLD-P, BLD-NP, dan LAND
9. Klik `Deactivate` pada Bulk Action Bar
10. Verifikasi dialog "Deactivate Tax Depreciation Classes" memuat dua Alert `severity="warning"` berurutan dari atas: "No active Building class will remain. New asset classes of that type cannot be set up." lalu "No active Land class will remain. New asset classes of that type cannot be set up."
11. Verifikasi tidak ada Alert untuk Non-building
12. Klik `[Cancel]` pada dialog
13. Klik icon `×` di Bulk Action Bar

### TC-FA-TDC-459: Bulk Deactivate yang menghabiskan class Active tiga Asset Type menampilkan tiga Alert berurutan

14. Centang checkbox satu baris agar Bulk Action Bar tampil
15. Klik `Select All (9 records)` pada Bulk Action Bar
16. Klik `Deactivate` pada Bulk Action Bar
17. Verifikasi dialog "Deactivate Tax Depreciation Classes" memuat tiga Alert `severity="warning"` berurutan dari atas: "No active Non-building class will remain. New asset classes of that type cannot be set up.", lalu "No active Building class will remain. New asset classes of that type cannot be set up.", lalu "No active Land class will remain. New asset classes of that type cannot be set up."
18. Klik `[Cancel]` pada dialog
19. Klik icon `×` di Bulk Action Bar
20. Seed tiga Asset Class pemakai NB-2 lewat API sehingga Used By NB-2 bernilai 3, lalu muat ulang tabel

### TC-FA-TDC-457: Matriks 6b: Bulk Deactivate yang menghabiskan class Active satu Asset Type disertai class dipakai

21. Centang checkbox baris BLD-P, BLD-NP, dan NB-2
22. Klik `Deactivate` pada Bulk Action Bar
23. Verifikasi dialog D-14 memuat bagian "The following will be deactivated:" berisi `• BLD-P – Bangunan permanen` dan `• BLD-NP – Bangunan tidak permanen`
24. Verifikasi dialog D-14 memuat Alert `severity="warning"` dengan teks "No active Building class will remain. New asset classes of that type cannot be set up."
25. Verifikasi bagian "The following cannot be deactivated and will be skipped:" berisi `• NB-2 – Bukan bangunan – Kelompok 2 — "used by asset classes"`
26. Klik `[Continue]` pada dialog D-14
27. Verifikasi toggle `Active` baris BLD-P dan BLD-NP menjadi Off
28. Verifikasi toggle `Active` baris NB-2 tetap On
29. Verifikasi toast "Success, tax depreciation class has been deactivated. Some items were skipped (used by asset classes)." tampil

### TC-FA-TDC-461: Matriks 8: Bulk Activate seleksi campuran hanya memproses subset Inactive

30. Catat baseline jumlah entri Changelog yang memuat class NB-4 lewat kemampuan baca log
31. Centang checkbox baris NB-OLD, NB-OLD2, dan NB-4
32. Klik `Activate` pada Bulk Action Bar
33. Verifikasi dialog "Activate Tax Depreciation Classes" memuat bullet `• NB-OLD – Kelompok khusus lama` dan `• NB-OLD2 – Kelompok khusus lama 2` saja
34. Verifikasi bullet NB-4 tidak tampil di dialog dan tidak dihitung
35. Klik `[Activate]` pada dialog
36. Verifikasi toast "Success, tax depreciation class has been activated." tampil
37. Verifikasi toggle `Active` baris NB-4 tetap On
38. Verifikasi jumlah entri Changelog yang memuat class NB-4 sama dengan baseline (tidak ada entri log baru)
39. Pulihkan NB-OLD dan NB-OLD2 ke Inactive lewat API hingga tersimpan, lalu muat ulang tabel

### TC-FA-TDC-460: Matriks 7: Bulk Activate semua class Inactive

40. Centang checkbox baris NB-OLD dan NB-OLD2
41. Klik `Activate` pada Bulk Action Bar
42. Klik `[Activate]` pada dialog D-03 jamak
43. Verifikasi toggle `Active` baris NB-OLD dan NB-OLD2 menjadi On
44. Verifikasi satu toast "Success, tax depreciation class has been activated." tampil
45. Verifikasi Bulk Action Bar hilang
46. Verifikasi seleksi di-reset ke 0

## Notes

- Urutan TC dalam spec: TC-FA-TDC-456, 458, 459, 457, 461, 460. Dialog yang hanya dibuka lebih dulu (S-10); TC yang mengubah data berikutnya; TC-FA-TDC-459 (butuh Used By 0 di semua class) mendahului TC-FA-TDC-457 (butuh NB-2 Used By 3).
- Langkah penghubung (S-03, S-09): langkah 7, 13 dan 19 (klik icon `×` agar seleksi TC berikutnya bersih), langkah 6, 12 dan 18 (membatalkan dialog yang hanya screening), langkah 14 (mencentang satu baris agar Bulk Action Bar tampil, karena bar hilang bila tidak ada baris tercentang dan `Select All` hanya tersedia di bar; langkah 1 TC-FA-TDC-459 tidak menyebut cara bar muncul), langkah 20 (membentuk NB-2 Used By 3 untuk TC-FA-TDC-457), dan langkah 39 (mengembalikan NB-OLD dan NB-OLD2 ke Inactive supaya TC-FA-TDC-460 memenuhi precondition).
- Di atas sekitar 35 langkah (46 langkah): satu topik (matriks Bulk Deactivate 6 dan Bulk Activate 7 sampai 8, kelas harness `-`); seleksi dibersihkan di akhir tiap blok dan data di-seed ulang di tengah spec. Dua langkah penghubung menyambung blok: langkah 20 (seed Used By NB-2 bernilai 3) menjadi precondition blok TC-FA-TDC-457, dan langkah 39 (NB-OLD dan NB-OLD2 dikembalikan ke Inactive lewat API) menjadi precondition blok TC-FA-TDC-460. Blok 456, 458, 459, dan 461 berdiri sendiri; blok 457 bergantung pada langkah 20 dan blok 460 bergantung pada langkah 39.
- Temuan untuk QA:
  - TC-FA-TDC-459 "sampai semua class Active terpilih": `Select All (9 records)` memilih seluruh baris termasuk NB-OLD dan NB-OLD2 yang Inactive (N = 9 dari seeding); spec mengikuti teks TC dan dialog hanya diasersi memuat tiga Alert.
  - TC-FA-TDC-459 langkah 1 (`Select All`) tidak menyebut cara memunculkan Bulk Action Bar; spec mencentang satu baris lebih dulu (langkah 14). Pola sama dengan TC-FA-TDC-419 (spec 110), 420, 421 (spec 111), 905 dan 907 (spec 122).
  - TC-FA-TDC-461 Expected c "tanpa entri log baru" tidak punya langkah observasi di TC; jumlah entri Changelog class NB-4 dibaca lewat kemampuan baca log terhadap baseline. Post Condition TC-FA-TDC-460 (status Active tersimpan; log L-04) tidak diasersi (tanpa langkah observasi).
  - TC-FA-TDC-457 Expected d memuat toggle dan toast dalam satu butir; dipecah per klausa.
  - Email akun Total Control tidak tertulis di TC.
  - Class Code maksimal 15 karakter, sehingga suffix `{runId}-<NNN>` (S-12) tidak muat pada kode class milik spec; spec memakai kode literal TC pada dataset company khusus automation yang di-seed dan dipulihkan fixture. Perlu konfirmasi QA.
