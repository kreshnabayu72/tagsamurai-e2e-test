---
id: TC-FA-TDC-E2E-136-konflik-bulk-deactivate-activate-delete-sebagian-class-dihapus-sesi-lain
title: "Konflik Bulk: Class Diposting, Sebagian atau Seluruh Class Dihapus Sesi Lain Saat Confirm Bulk Delete, Deactivate, dan Activate"
layer: ui-e2e
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-474
  - TC-FA-TDC-475
  - TC-FA-TDC-476
  - TC-FA-TDC-477
sourceRules: ["F-FATDC-13.k9", "T-06b", "L-05", "F-FATDC-13.k12", "F-FATDC-13.k1", "L-04", "T-13", "FATDC-LOGIC-14k", "F-FATDC-13.k7", "T-04"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-13.k9": 8
  "T-06b": 9
  "L-05": 10
  "F-FATDC-13.k12": 19
  "F-FATDC-13.k1": 20
  "L-04": [21, 32, 45]
  "T-13": [30, 31]
  "FATDC-LOGIC-14k": [33, 34]
  "F-FATDC-13.k7": 43
  "T-04": 44
coverage:
  web: automated
---

# Konflik Bulk: Class Diposting, Sebagian atau Seluruh Class Dihapus Sesi Lain Saat Confirm Bulk Delete, Deactivate, dan Activate

## Prerequisites

- Mode: FE+BE.
- Akun aktor sesi A: Total Control (company uji Fixed Asset). Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) dan disediakan tim FE; password lewat `Spectra.env.FA_TC_PASSWORD`.
- Pelaku kedua (sesi B): sesi API aktor Total Control kedua (akun berbeda; email tidak tertulis di TC dan disediakan tim FE; password lewat `Spectra.env.FA_TC_B_PASSWORD`, nama env baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`) dan fixture BE untuk Last Posted Tax Year (posting penyusutan fiskal belum tersedia di UI). Sesi B hanya memicu perubahan state dan hasilnya tidak diasersi di sesi itu.
- Login sesi A di hook `before` spec ini; halaman Fixed Asset > Settings > Accounting > Tax Depreciation Class dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (termasuk class berkunci), sesi API aktor, flag Guided Tooltip disetel true oleh hook suite, hook `beforeEach` mengonfirmasi `beforeunload`. Kemampuan tambahan: pembacaan jumlah dan isi entri Changelog class lewat fixture BE (disediakan tim FE/BE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus atau dipulihkan di hook `after`; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb3` | `NB-3` | Class Name `Bukan bangunan – Kelompok 3`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nb4` | `NB-4` | Class Name `Bukan bangunan – Kelompok 4`, Active, Used By 0, tanpa Last Posted Tax Year |
| `nbOld` | `NB-OLD` | Inactive, Used By 0 |
| `nbOld2` | `NB-OLD2` | Inactive, Used By 0 |

- Class diseed ulang lewat API di antara blok (langkah 11, 22, dan 35).
- Hasil Search `NB-` memuat `NB-3` dan `NB-4`, dan hasil Search `NB-OLD` memuat `NB-OLD` dan `NB-OLD2`, pada halaman pertama (dataset company khusus automation berisi kurang dari 10 baris dengan awalan itu).
- Suite berjalan serial (`parallel: false`) karena Class Code seed bersifat literal.

## Test Steps

### TC-FA-TDC-474: Matriks 13e, Bulk Delete, class menjadi diposting antara dialog dibuka dan Confirm

1. Ketik Search `NB-`, tekan Enter
2. Catat baseline jumlah entri Changelog Delete class `NB-3` dan `NB-4` lewat fixture BE
3. Sesi A: centang checkbox baris `NB-3`
4. Sesi A: centang checkbox baris `NB-4`
5. Sesi A: klik aksi `Delete` pada Bulk Action Bar (dialog D-06 jamak terbuka, belum Confirm)
6. Sesi B (fixture BE): isi Last Posted Tax Year `NB-4` dengan `2026` hingga tersimpan
7. Sesi A: klik `[Delete]`
8. Verifikasi baris `NB-3` terhapus dan baris `NB-4` tetap ada
9. Verifikasi muncul toast: `Success, tax depreciation class has been deleted. Some items were skipped (posted or used by asset classes).`
10. Verifikasi jumlah entri Changelog Delete bertambah tepat satu untuk `NB-3` dan tidak bertambah untuk `NB-4` dari baseline langkah 2

### TC-FA-TDC-475: Matriks 14a, Bulk Deactivate, sebagian class dihapus sesi lain saat Confirm

11. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 tanpa Last Posted Tax Year
12. Ganti isi kotak search dengan `NB-`, tekan Enter
13. Catat baseline jumlah entri Changelog Status class `NB-3` dan `NB-4` lewat fixture BE
14. Sesi A: centang checkbox baris `NB-3`
15. Sesi A: centang checkbox baris `NB-4`
16. Sesi A: klik aksi `Deactivate` pada Bulk Action Bar (dialog D-01 jamak terbuka, belum Confirm)
17. Sesi B (sesi API): hapus class `NB-3` hingga class terhapus di server
18. Sesi A: klik `[Deactivate]`
19. Verifikasi toggle `NB-4` menjadi Off tanpa pesan error
20. Verifikasi muncul toast: `Success, tax depreciation class has been deactivated.`
21. Verifikasi jumlah entri Changelog Status `NB-3` sama dengan baseline langkah 13 (tidak ada entri log untuk `NB-3` setelah penghapusan oleh sesi B)

### TC-FA-TDC-476: Matriks 14b, Bulk Deactivate, semua class dihapus sesi lain saat Confirm

22. Pulihkan class `NB-3` dan `NB-4` lewat seeding API ke Active dengan Used By 0 tanpa Last Posted Tax Year
23. Ganti isi kotak search dengan `NB-`, tekan Enter
24. Catat baseline jumlah entri Changelog Status class `NB-3` dan `NB-4` lewat fixture BE
25. Sesi A: centang checkbox baris `NB-3`
26. Sesi A: centang checkbox baris `NB-4`
27. Sesi A: klik aksi `Deactivate` pada Bulk Action Bar (dialog D-01 jamak terbuka, belum Confirm)
28. Sesi B (sesi API): hapus class `NB-3` dan `NB-4` hingga keduanya terhapus di server
29. Sesi A: klik `[Deactivate]`
30. Verifikasi muncul toast netral (severity Info): `This tax depreciation class is no longer available.`
31. Verifikasi tabel sesi A disegarkan dan baris `NB-3` dan `NB-4` tidak ada
32. Verifikasi jumlah entri Changelog Status `NB-3` dan `NB-4` sama dengan baseline langkah 24 (tidak ada entri log Status)
33. Verifikasi seleksi dikosongkan
34. Verifikasi Bulk Action Bar hilang

### TC-FA-TDC-477: Matriks 14c, Bulk Activate, sebagian class dihapus sesi lain saat Confirm

35. Pulihkan class `NB-OLD` dan `NB-OLD2` lewat seeding API ke Inactive dengan Used By 0
36. Ganti isi kotak search dengan `NB-OLD`, tekan Enter
37. Catat baseline jumlah entri Changelog Status class `NB-OLD` dan `NB-OLD2` lewat fixture BE
38. Sesi A: centang checkbox baris `NB-OLD`
39. Sesi A: centang checkbox baris `NB-OLD2`
40. Sesi A: klik aksi `Activate` pada Bulk Action Bar (dialog D-03 jamak terbuka, belum Confirm)
41. Sesi B (sesi API): hapus class `NB-OLD` hingga class terhapus di server
42. Sesi A: klik `[Activate]`
43. Verifikasi toggle `NB-OLD2` menjadi On tanpa pesan error
44. Verifikasi muncul toast: `Success, tax depreciation class has been activated.`
45. Verifikasi jumlah entri Changelog Status `NB-OLD` sama dengan baseline langkah 37 (tidak ada entri log untuk `NB-OLD` setelah penghapusan oleh sesi B)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1, 12, 23, dan 36 (Search agar baris target ada di halaman teramati dan seleksi bersih; R-16, 8b.13), langkah 11, 22, dan 35 (membentuk precondition tiap blok). Langkah 2, 13, 24, dan 37 mencatat baseline Changelog (S-12, 8b.10).
- Langkah 6, 17, 28, dan 41 (pelaku kedua lewat sesi API aktor atau fixture BE) ditulis "... hingga ..." (R-20); sesi A tetap memegang dialog yang terbuka sebelum sesi B bertindak.
- Langkah 10, 21, 32, dan 45 (Expected c, jumlah entri log): ditulis sebagai selisih terhadap baseline (S-12). Asersi "tidak ada entri log" memakai baseline di spec ini (S-05) karena TC kelas c ini tidak dimuat spec absence dan keadaan dua sesi baru dibentuk pada langkah 6, 17, 28, dan 41 (P-1); toast hasil server (langkah 9, 20, 30, dan 44) menjadi anchor positif (8b.2).
- Langkah 31 (baris hilang): toast netral langkah 30 menjadi anchor positif (8b.2). Langkah 33 dan 34 (keadaan seleksi dan Bulk Action Bar) tidak memerlukan pembanding karena barisnya dibuktikan oleh aksi centang pada langkah 25 dan 26.
- Alasan spec melewati sekitar 35 langkah (45 langkah): keempat blok adalah kelas c pada dialog bulk yang sama dengan dua class, masing-masing berdiri sendiri dengan seed ulang, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah berulang per blok adalah baseline, centang, pemicu sesi B, dan `Verifikasi` per klausa (S-01).
- Temuan untuk QA:
  - Email akun Total Control sesi A dan sesi B tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - Class Code `NB-3`, `NB-4`, `NB-OLD`, dan `NB-OLD2` ditulis literal tanpa suffix `{runId}-<NNN>`; kode ini dipakai TC apa adanya dan menjadi target aksi tulis (S-06, S-12). Lampiran A konvensi belum memuat pengecualian untuk modul ini; class diseed dan dipulihkan lewat fixture pada company/state khusus automation.
  - TC-FA-TDC-474 sampai TC-FA-TDC-477 Expected log menyebut "log"; spec membaca entri Changelog lewat fixture BE karena TC tidak merinci cara membuka modal Changelog untuk asersi jumlah.
  - TC-FA-TDC-475 dan TC-FA-TDC-477 Expected a tidak menyebut keadaan seleksi sesudah aksi (berbeda dengan TC-FA-TDC-476 yang menyebut seleksi dikosongkan); spec tidak mengasersinya (S-01).
  - Kolom Automation TC-FA-TDC-474, TC-FA-TDC-475, TC-FA-TDC-476, dan TC-FA-TDC-477 memuat `Manual Only — (d) dua sesi paralel`; TC tetap masuk spec (konvensi bagian 2).
