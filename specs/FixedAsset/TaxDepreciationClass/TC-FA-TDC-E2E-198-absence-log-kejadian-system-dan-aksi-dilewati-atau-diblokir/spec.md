---
id: TC-FA-TDC-E2E-198-absence-log-kejadian-system-dan-aksi-dilewati-atau-diblokir
title: "Absence Log: Kejadian System Tidak Ditulis ke System Log, Aksi Bulk Dilewati, dan Aksi yang Diblokir Dialog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-719
  - TC-FA-TDC-718
  - TC-FA-TDC-716
  - TC-FA-TDC-717
  - TC-FA-TDC-697
coverage:
  web: automated
---

# Absence Log: Kejadian System Tidak Ditulis ke System Log, Aksi Bulk Dilewati, dan Aksi yang Diblokir Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`. Total Control Budi Santoso dan Siti Rahmawati hanya dibaca System Log-nya lewat Detail User (tidak login).
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before`; blok TC-FA-TDC-697 mengatur jam absolut sendiri (31 Des 2026 17:00:00 UTC) dan memulihkannya sebelum membaca System Log (S-09), serta dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Spec absence (kelas g): pemicu job J-02 (tick scheduler), J-03 (posting lewat fixture BE), dialog D-14, D-15, dan D-02 hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5). Tiap TC punya baseline sendiri yang dicatat tepat sebelum pemicu (S-12). Penahanan dan penjalanan job disediakan tim FE/BE (`suite.md`).
- Time Zone entitas Asia/Jakarta (UTC+07:00). Entri log yang dibuat saat jam digeser bercap waktu masa depan; entri dicari lewat Search Class Code, bukan posisi teratas (S-12).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND); NB-1 Active dengan Used By 5; NB-2 Active dengan Used By 3 dan tanpa Last Posted Tax Year; NB-3 Active dengan Used By 0 tanpa Last Posted Tax Year; `KHS-198A` (Class Name `Kelompok log uji`, versi Scheduled Effective From Jan 2027, Last Posted Tax Year `2025`) milik spec dengan pola kode `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter (S-12). Tabel memuat 8 baris pada satu halaman sehingga baris target dicentang tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` mengembalikan NB-3 ke Active dan membuat ulang NB-3 bila terhapus, menghapus `KHS-198A`, serta mengembalikan jam dan sesi (kemampuan disediakan tim FE/BE).

## Test Steps

### TC-FA-TDC-719: Bulk Deactivate semua diblokir tidak menulis log di semua surface

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Centang baris NB-1
3. Centang baris NB-2
4. Klik `Deactivate` pada Bulk Action Bar
5. Verifikasi dialog D-02 jamak tampil
6. Klik `[OK]` pada dialog D-02 jamak
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Changelog sama dengan baseline
9. Tutup Popup Changelog
10. Buka Detail User Rina Puspita > Tab System Log
11. Verifikasi jumlah entri System Log Rina Puspita sama dengan baseline
12. Buka Reports & Logs > Activity Log, tab `User Action`
13. Verifikasi jumlah entri Activity Log sama dengan baseline
14. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-718: Aksi yang diblokir seluruhnya (dialog blok) tidak menulis log di semua surface

15. Catat baseline jumlah baris log NB-2 di Changelog, System Log Rina Puspita, dan Activity Log
16. Klik toggle `Active` baris NB-2
17. Verifikasi dialog blok tampil
18. Klik `[OK]` pada dialog blok
19. Klik tombol ⋯ baris NB-2
20. Pilih `Delete`
21. Verifikasi dialog blok tampil
22. Klik `[OK]` pada dialog blok
23. Klik ikon Changelog di toolbar
24. Ketik Search `NB-2`, tekan Enter
25. Verifikasi jumlah baris log NB-2 di Changelog sama dengan baseline
26. Tutup Popup Changelog
27. Buka Detail User Rina Puspita > Tab System Log
28. Verifikasi jumlah baris log NB-2 di System Log Rina Puspita sama dengan baseline
29. Buka Reports & Logs > Activity Log, tab `User Action`
30. Ketik Search `NB-2`, tekan Enter
31. Verifikasi jumlah baris log NB-2 di Activity Log sama dengan baseline
32. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-716: Bulk Deactivate sebagian: class yang dilewati tidak dicatat di semua surface

33. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
34. Centang baris NB-3
35. Centang baris NB-2
36. Klik `Deactivate` pada Bulk Action Bar
37. Klik `[Continue]` pada dialog D-14 hingga proses selesai
38. Klik ikon Changelog di toolbar
39. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
40. Verifikasi Changelog memuat tepat satu baris Status untuk NB-3 (Old Value "Active", New Value "Inactive")
41. Verifikasi Changelog tidak memuat baris log untuk NB-2
42. Tutup Popup Changelog
43. Buka Detail User Rina Puspita > Tab System Log
44. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
45. Verifikasi System Log Rina Puspita memuat tepat satu baris Status untuk NB-3 (Old Value "Active", New Value "Inactive")
46. Verifikasi System Log Rina Puspita tidak memuat baris log untuk NB-2
47. Buka Reports & Logs > Activity Log, tab `User Action`
48. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
49. Verifikasi Activity Log FAMS memuat tepat satu baris Status untuk NB-3 (Old Value "Active", New Value "Inactive")
50. Verifikasi Activity Log FAMS tidak memuat baris log untuk NB-2
51. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-717: Bulk Delete sebagian: class yang dilewati tidak dicatat di semua surface

52. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
53. Centang baris NB-3
54. Centang baris NB-2
55. Klik `Delete` pada Bulk Action Bar
56. Klik `[Continue]` pada dialog D-15 hingga proses selesai
57. Klik ikon Changelog di toolbar
58. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
59. Verifikasi Changelog memuat tepat satu baris Delete untuk NB-3 (Field "Class Code", Old Value "NB-3", New Value "—")
60. Verifikasi Changelog tidak memuat baris log untuk NB-2
61. Tutup Popup Changelog
62. Buka Detail User Rina Puspita > Tab System Log
63. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
64. Verifikasi System Log Rina Puspita memuat tepat satu baris Delete untuk NB-3 (Field "Class Code", Old Value "NB-3", New Value "—")
65. Verifikasi System Log Rina Puspita tidak memuat baris log untuk NB-2
66. Buka Reports & Logs > Activity Log, tab `User Action`
67. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
68. Verifikasi Activity Log FAMS memuat tepat satu baris Delete untuk NB-3 (Field "Class Code", Old Value "NB-3", New Value "—")
69. Verifikasi Activity Log FAMS tidak memuat baris log untuk NB-2
70. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-697: Kejadian dengan aktor System (J-01, J-02, J-03) tidak ditulis ke System Log user mana pun

71. Catat baseline jumlah entri System Log Rina Puspita, Budi Santoso, dan Siti Rahmawati
72. Atur jam server dan jam browser ke 31 Des 2026 17:00:00 UTC (1 Jan 2027 00:00 WIB) lalu jalankan tick scheduler J-02
73. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-198A` lewat fixture BE (J-03)
74. Klik ikon Changelog di toolbar
75. Ketik Search `KHS-198A`, tekan Enter
76. Verifikasi Changelog, Dicatat: baris L-08 (Field "Current Version") untuk Class Code "KHS-198A" dengan Modified By "System"
77. Verifikasi Changelog, Dicatat: baris L-10 (Field "Last Posted Tax Year") untuk Class Code "KHS-198A" dengan Modified By "System"
78. Tutup Popup Changelog
79. Pulihkan jam server dan jam browser ke 15 Okt 2026 10:00 WIB
80. Buka Detail User Rina Puspita > Tab System Log
81. Verifikasi jumlah entri System Log Rina Puspita sama dengan baseline
82. Buka Detail User Budi Santoso > Tab System Log
83. Verifikasi jumlah entri System Log Budi Santoso sama dengan baseline
84. Buka Detail User Siti Rahmawati > Tab System Log
85. Verifikasi jumlah entri System Log Siti Rahmawati sama dengan baseline
86. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (86 langkah, 33 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 7 sampai 13, 23 sampai 31, 38 sampai 50, 57 sampai 69, 74 sampai 78, 80 sampai 85 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- S-05 dan prinsip 13g: seluruh TC di spec ini adalah asersi absence atas log dengan aksi nyata dan baseline sendiri (S-12). Anchor positif (8b.2): dialog D-02 jamak (langkah 5), dialog blok (langkah 17 dan 21), baris NB-3 yang dicatat pada surface yang sama tepat sebelum asersi baris NB-2 yang tidak ada, serta baris L-08 dan L-10 pada Changelog (langkah 76 dan 77) untuk System Log.
- Urutan TC: 719, 718, 716, 717, 697. TC-FA-TDC-717 menghapus NB-3 yang pada TC-FA-TDC-716 sudah Inactive (Used By 0 dan tanpa Last Posted Tax Year tetap memenuhi precondition Delete); TC-FA-TDC-697 di akhir karena mengubah jam server (S-10, S-09).
- Langkah penghubung (S-03): mencatat baseline, menutup Popup Changelog, Search `NB-2` / `KHS-198A` untuk menemukan entri (R-16), memulihkan jam, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14).
- TC-FA-TDC-716 dan 717: selisih tepat 1 per surface membuktikan baris NB-3 sebagai satu-satunya entri baru sebelum `Verifikasi` tidak adanya baris NB-2 (asersi tambahan atas Expected TC untuk S-12, S-03). TC-FA-TDC-697 membandingkan jumlah entri System Log tiga user terhadap baseline per user.
- Temuan untuk QA:
  - TC-FA-TDC-697 menyebut System Log tiga user admin tanpa email; nama Rina Puspita, Budi Santoso, dan Siti Rahmawati dipakai apa adanya (R-06). Old Value dan New Value baris L-08 dan L-10 tidak disebut; spec hanya mengasersi Field dan Modified By "System". Class `KHS-198A` pada TC memakai kode `KHS-LG`.
  - TC-FA-TDC-716 dan 717 menyebut "Periksa" tiga surface tanpa langkah buka dan filter; spec memakai pola buka surface yang sama dengan TC pencatatan. TC-FA-TDC-718 dan 719 tidak menyebut cara mencari baris NB-2/jumlah total; spec memakai Search NB-2 pada Changelog dan Activity Log serta jumlah total untuk TC-719.
  - TC-FA-TDC-716 sampai 719 memakai class seed literal (NB-1, NB-2, NB-3) sebagai target aksi tulis atau diblokir; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
