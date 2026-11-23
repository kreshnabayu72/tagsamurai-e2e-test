---
id: TC-FA-TDC-E2E-286-log-l-03-declining-balance-rate-dan-end-of-life-treatment-serta-log-class-hasil-request-langsung
title: "Pencatatan Log: Perubahan Declining Balance Rate dan End-of-Life Treatment (L-03) serta Log Class Hasil Request Langsung di Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-953
  - TC-FA-TDC-954
  - TC-FA-TDC-958
  - TC-FA-TDC-960
sourceRules: ["L-03", "L-01", "§8.2", "§8.3", "FATDC-LOGIC-04b.3", "FATDC-LOGIC-04b.6", "FATDC-LOGIC-03f.3", "FATDC-LOGIC-03g.5", "J-04"]
smoke: []
dependsOn: []
trace:
  "L-03": [10, 11, 12, 16, 17, 18, 21, 22, 23, 35, 36, 37, 41, 42, 43, 46, 47, 48, 78, 79, 80, 84, 85, 86, 89, 90, 91]
  "§8.2": [16, 17, 18, 41, 42, 43, 84, 85, 86]
  "§8.3": [21, 22, 23, 46, 47, 48, 89, 90, 91]
  "FATDC-LOGIC-04b.3": [10, 11, 12]
  "FATDC-LOGIC-04b.6": [35, 36, 37, 78, 79, 80]
  "FATDC-LOGIC-03f.3": [55, 56, 60, 65, 69]
  "FATDC-LOGIC-03g.5": [56, 60, 65, 69]
  "L-01": [58, 59, 60, 63, 64, 65, 67, 68, 69]
  "J-04": [73, 75, 76, 78]
coverage:
  web: automated
---

# Pencatatan Log: Perubahan Declining Balance Rate dan End-of-Life Treatment (L-03) serta Log Class Hasil Request Langsung di Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Kemampuan suite untuk TC-FA-TDC-958 dan TC-FA-TDC-960 (dinyatakan di `suite.md`): sesi API aktor Total Control untuk request langsung dan request baca. Klien HTTP untuk request langsung disediakan tim FE/BE; endpoint tidak dikarang (S-13).
- Suite berjalan serial (`parallel: false`).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat, S-12; kode berbeda antar spec; kemampuan seeding dan penghapusan disediakan tim FE/BE). Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-953 | `DBE-LG1` | Class Name `Kelompok log uji`; Non-building, Straight Line dan Declining Balance (Declining Balance Rate 12.5, End-of-Life Treatment `Charge in final period`), Regulation Reference `UU HPP 7/2021; PMK 72/2023`, versi Current Effective From Jan 2025 dengan Useful Life 16, Active, Used By 0 |
| TC-FA-TDC-954 | `DBE-LG2` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance (Declining Balance Rate 25, End-of-Life Treatment `Charge in final period`), Regulation Reference `UU HPP 7/2021; PMK 72/2023`, satu versi tanpa Effective From, Active, Used By 0 |
| TC-FA-TDC-958 | `R-API4` | belum ada; dibuat oleh request langsung langkah 52; dihapus di hook `after` |
| TC-FA-TDC-960 | `DBE-14` | Non-building, Useful Life 8, Straight Line dan Declining Balance (Declining Balance Rate 25, End-of-Life Treatment `Charge in final period`), hanya satu versi (Current tanpa Effective From), Active, Used By 0, tanpa versi Scheduled |

- Tabel memuat tujuh class seed bawaan dan tiga class milik spec (`DBE-LG1`, `DBE-LG2`, `DBE-14`; 10 baris dengan 10 baris per halaman, ditambah `R-API4` sesudah langkah 52); baris dibuka lewat Search Class Code (8b.13, R-23).
- Tahun pajak 2026 belum tertutup (Exported through belum mencapai Des 2026) sehingga Effective From "Jan 2026" ditawarkan; TC tidak menyebutnya (lihat Temuan untuk QA).

## Test Steps

### TC-FA-TDC-953: Log L-03: perubahan Declining Balance Rate mencatat baris Declining Balance Rate dan Effective From

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Ketik Search `DBE-LG1`, tekan Enter
3. Klik link Class Code `DBE-LG1` pada tabel
4. Ganti Declining Balance Rate dari `12.5` menjadi `15`
5. Klik `[Save]`
6. Pilih Effective From "Jan 2026"
7. Klik `[Apply]` hingga versi berhasil tersimpan
8. Catat waktu aksi
9. Klik ikon Changelog di toolbar
10. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
11. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "DBE-LG1" | Field "Declining Balance Rate" | Old Value "12.5" | New Value "15" | Modified By "Rina P"
12. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "DBE-LG1" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026" | Modified By "Rina P"
13. Verifikasi tidak ada baris untuk Field "Useful Life", "Straight Line Rate", "End-of-Life Treatment", "Allowed Methods", atau "Regulation Reference" di Changelog
14. Tutup Popup Changelog
15. Buka Detail User Rina Puspita > Tab System Log
16. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
17. Verifikasi System Log Rina Puspita, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG1" | Field "Declining Balance Rate" | Old Value "12.5" | New Value "15"
18. Verifikasi System Log Rina Puspita, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG1" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026"
19. Verifikasi tidak ada baris untuk Field "Useful Life", "Straight Line Rate", "End-of-Life Treatment", "Allowed Methods", atau "Regulation Reference" di System Log Rina Puspita
20. Buka Reports & Logs > Activity Log, tab `User Action`
21. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
22. Verifikasi Activity Log FAMS, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG1" | Field "Declining Balance Rate" | Old Value "12.5" | New Value "15" | Modified By "Rina P"
23. Verifikasi Activity Log FAMS, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG1" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026" | Modified By "Rina P"
24. Verifikasi tidak ada baris untuk Field "Useful Life", "Straight Line Rate", "End-of-Life Treatment", "Allowed Methods", atau "Regulation Reference" di Activity Log
25. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-954: Log L-03: perubahan End-of-Life Treatment mencatat baris End-of-Life Treatment dan Effective From

26. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
27. Ketik Search `DBE-LG2`, tekan Enter
28. Klik link Class Code `DBE-LG2` pada tabel
29. Ganti End-of-Life Treatment menjadi `Keep depreciating`
30. Klik `[Save]`
31. Pilih Effective From "Jan 2026"
32. Klik `[Apply]` hingga versi berhasil tersimpan
33. Catat waktu aksi
34. Klik ikon Changelog di toolbar
35. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
36. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "DBE-LG2" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating" | Modified By "Rina P"
37. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "DBE-LG2" | Field "Effective From" | Old Value "—" | New Value "Jan 2026" | Modified By "Rina P"
38. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Straight Line Rate", "Allowed Methods", atau "Regulation Reference" di Changelog
39. Tutup Popup Changelog
40. Buka Detail User Rina Puspita > Tab System Log
41. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
42. Verifikasi System Log Rina Puspita, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG2" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating"
43. Verifikasi System Log Rina Puspita, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG2" | Field "Effective From" | Old Value "—" | New Value "Jan 2026"
44. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Straight Line Rate", "Allowed Methods", atau "Regulation Reference" di System Log Rina Puspita
45. Buka Reports & Logs > Activity Log, tab `User Action`
46. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
47. Verifikasi Activity Log FAMS, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG2" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating" | Modified By "Rina P"
48. Verifikasi Activity Log FAMS, Dicatat: Date | Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-LG2" | Field "Effective From" | Old Value "—" | New Value "Jan 2026" | Modified By "Rina P"
49. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Straight Line Rate", "Allowed Methods", atau "Regulation Reference" di Activity Log
50. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-958: Request langsung class Straight Line saja dengan Declining Balance Rate dan End-of-Life Treatment: nilai tidak disimpan

51. Catat baseline jumlah entri `R-API4` di Changelog, System Log Rina Puspita, dan Activity Log
52. Kirim request langsung dengan sesi API aktor Total Control untuk membuat class `R-API4` bertipe Non-building dengan Class Name `Kelompok API uji`, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Useful Life 10, Allowed Methods Straight Line, Declining Balance Rate 50, dan End-of-Life Treatment Keep depreciating tanpa melalui UI
53. Verifikasi server menerima request
54. Baca ulang class `R-API4` beserta daftar versinya lewat request baca
55. Verifikasi class `R-API4` tersimpan dengan Straight Line Rate 10
56. Verifikasi Declining Balance Rate dan End-of-Life Treatment tidak tersimpan (kosong) pada versi pertama
57. Klik ikon Changelog di toolbar, Search `R-API4`
58. Verifikasi jumlah entri `R-API4` di Changelog bertambah tepat 2 dari baseline
59. Verifikasi Changelog memuat entri L-01 untuk `R-API4` dengan baris Field "Class Code" dan Field "Asset Type"
60. Verifikasi tidak ada baris untuk Field "Declining Balance Rate" dan "End-of-Life Treatment" di Changelog
61. Tutup Popup Changelog
62. Buka Detail User Rina Puspita > Tab System Log
63. Verifikasi jumlah entri `R-API4` di System Log Rina Puspita bertambah tepat 2 dari baseline
64. Verifikasi System Log Rina Puspita memuat entri L-01 untuk `R-API4` dengan baris Field "Class Code" dan Field "Asset Type"
65. Verifikasi tidak ada baris untuk Field "Declining Balance Rate" dan "End-of-Life Treatment" di System Log Rina Puspita
66. Buka Reports & Logs > Activity Log, tab `User Action`
67. Verifikasi jumlah entri `R-API4` di Activity Log bertambah tepat 2 dari baseline
68. Verifikasi Activity Log memuat entri L-01 untuk `R-API4` dengan baris Field "Class Code" dan Field "Asset Type"
69. Verifikasi tidak ada baris untuk Field "Declining Balance Rate" dan "End-of-Life Treatment" di Activity Log
70. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-960: Request langsung Edit yang mengubah End-of-Life Treatment membentuk versi baru Current tercatat di tiga surface

71. Catat baseline jumlah entri `DBE-14` di Changelog, System Log Rina Puspita, dan Activity Log
72. Kirim request langsung dengan sesi API aktor Total Control untuk mengubah End-of-Life Treatment `DBE-14` menjadi Keep depreciating dengan Effective From Jan 2026 tanpa melalui UI
73. Verifikasi server menerima request
74. Baca ulang daftar versi `DBE-14` lewat request baca
75. Verifikasi versi baru "Jan 2026" berstatus Current
76. Verifikasi versi lama berstatus Past
77. Klik ikon Changelog di toolbar, Search `DBE-14`
78. Verifikasi jumlah entri `DBE-14` di Changelog bertambah tepat 2 dari baseline
79. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "DBE-14" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating"
80. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "DBE-14" | Field "Effective From" | Old Value "—" | New Value "Jan 2026"
81. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Allowed Methods", atau "Regulation Reference" di Changelog
82. Tutup Popup Changelog
83. Buka Detail User Rina Puspita > Tab System Log
84. Verifikasi jumlah entri `DBE-14` di System Log Rina Puspita bertambah tepat 2 dari baseline
85. Verifikasi System Log Rina Puspita, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-14" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating"
86. Verifikasi System Log Rina Puspita, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-14" | Field "Effective From" | Old Value "—" | New Value "Jan 2026"
87. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Allowed Methods", atau "Regulation Reference" di System Log Rina Puspita
88. Buka Reports & Logs > Activity Log, tab `User Action`
89. Verifikasi jumlah entri `DBE-14` di Activity Log bertambah tepat 2 dari baseline
90. Verifikasi Activity Log, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-14" | Field "End-of-Life Treatment" | Old Value "Charge in final period" | New Value "Keep depreciating"
91. Verifikasi Activity Log, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "DBE-14" | Field "Effective From" | Old Value "—" | New Value "Jan 2026"
92. Verifikasi tidak ada baris untuk Field "Useful Life", "Declining Balance Rate", "Allowed Methods", atau "Regulation Reference" di Activity Log
93. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (93 langkah, 32 di luar blok baca-log): keempat TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 9 sampai 24, 34 sampai 49, 57 sampai 69, dan 77 sampai 92 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- P-5 (butir b): TC-FA-TDC-958 dan TC-FA-TDC-960 adalah dua TC objek-uji ringan kelas a (request langsung tanpa harness eksternal dan tanpa state berat) pada surface pencatatan log yang sama dengan TC-FA-TDC-953 dan TC-FA-TDC-954; jumlahnya dua sehingga tidak melebihi batas. Pada kedua blok itu asersi hanya status penerimaan request, state data lewat request baca, dan isi log (8b.1); tidak ada tampilan UI form yang diasersi.
- Langkah penghubung (S-03): langkah 1, 26, 51, dan 71 (baseline); langkah 2, 27 (Search Class Code untuk menemukan baris target; R-16); Search tidak dibawa ke blok berikutnya karena klik sidebar pada langkah penutup tiap blok (langkah 25, 50, 70, 93) membuka ulang halaman dan mereset Search (S-09); langkah 8 dan 33 (mencatat waktu aksi); langkah 14, 39, 61, 82 (menutup Popup Changelog); langkah 25, 50, 70, 93 (membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul; S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Klausa "tidak ada baris untuk field lain" (Expected d TC-FA-TDC-953 dan TC-FA-TDC-954, Expected c TC-FA-TDC-958 dan TC-FA-TDC-960) ditulis sebagai `Verifikasi` tersendiri sesudah baris yang dicatat pada surface yang sama; selisih jumlah entri tepat sama dengan jumlah baris yang diasersi sehingga baris tersebut menjadi anchor (8b.2). Klausa itu bagian dari Expected TC pencatatan, bukan TC absence tanpa aksi (S-05).
- Selisih "tepat 2" pada langkah 58, 63, dan 67 (L-01 mencatat dua baris, Class Code dan Asset Type) berasal dari catatan TC ("Create class mencatat dua baris, Class Code dan Asset Type") dan dari Expected c TC-FA-TDC-958 ("hanya memuat baris Field Class Code dan Asset Type"); selisih "tepat 2" pada langkah 78, 84, dan 89 berasal dari Expected b TC-FA-TDC-960 (dua baris Edit). Selisih adalah dasar membaca baris baru (S-12).
- Date pada baris log TC-FA-TDC-958 dan TC-FA-TDC-960 serta Modified By TC-FA-TDC-960 tidak diasersi karena Expected TC tidak menyebutnya; hanya TC-FA-TDC-953 dan TC-FA-TDC-954 yang menyebut Date (waktu aksi) dan Modified By "Rina P".
- Temuan untuk QA:
  - TC-FA-TDC-953 dan TC-FA-TDC-954 memakai kode `DBE-LG1` dan `DBE-LG2` dengan Class Name `Kelompok log uji`; spec memakai kode itu persis (literal, Class Code maksimal 15 karakter).
  - TC-FA-TDC-953 dan TC-FA-TDC-954 memilih Effective From "Jan 2026" pada tanggal sistem uji 15 Okt 2026 tanpa menyebut Exported through; spec mengasumsikan tahun pajak 2026 belum tertutup (V-21).
  - TC-FA-TDC-958 tidak menyebut Action untuk entri L-01 dan nilai kolom lain (Old Value, New Value); spec hanya mengasersi Field "Class Code" dan "Asset Type". TC-FA-TDC-958 juga tidak menyebut status HTTP respons; spec mengasersi penerimaan request tanpa kode status.
  - TC-FA-TDC-958 dan TC-FA-TDC-960 tidak menyebut baseline jumlah entri; spec mencatatnya (S-12) karena kode `R-API4` dan `DBE-14` bisa membawa riwayat log dari run sebelumnya.
  - TC-FA-TDC-958 memberi prioritas Security tetapi Expected-nya penerimaan request dan pencatatan log; spec memakai caseType Positive untuk keseluruhan spec.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
