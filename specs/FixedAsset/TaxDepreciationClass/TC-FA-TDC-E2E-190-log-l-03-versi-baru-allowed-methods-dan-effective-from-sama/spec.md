---
id: TC-FA-TDC-E2E-190-log-l-03-versi-baru-allowed-methods-dan-effective-from-sama
title: "Pencatatan Log L-03: Versi Baru dari Useful Life, Allowed Methods, Regulation Reference, dan Effective From Sama dengan Versi Current"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-682
  - TC-FA-TDC-683
  - TC-FA-TDC-684
  - TC-FA-TDC-932
coverage:
  web: automated
---

# Pencatatan Log L-03: Versi Baru dari Useful Life, Allowed Methods, Regulation Reference, dan Effective From Sama dengan Versi Current

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-682 | `KHS-190A` | Class Name `Kelompok log uji`; Non-building, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0; versi Current Effective From Jan 2025 dengan Useful Life 16 |
| TC-FA-TDC-683 | `KHS-190B` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance; satu versi tanpa Effective From; Used By 0 |
| TC-FA-TDC-684 | `KHS-190C` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`; satu versi tanpa Effective From; Used By 0 |
| TC-FA-TDC-932 | `KHS-190D` | Class Name `Kelompok log uji`; Non-building, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`; versi Current Effective From Jan 2026 dengan Useful Life 10; Active, Used By 0 |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah empat class milik spec (11 baris) dengan 10 baris per halaman; baris `KHS-190*` dibuka lewat Search Class Code tanpa mengandalkan urutan default Class Code A-Z (8b.13, R-23).
- Pemulihan: hook `after` menghapus `KHS-190A` sampai `KHS-190D` lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan jam serta sesi.

## Test Steps

### TC-FA-TDC-682: Log L-03: versi baru langsung Current dari perubahan Useful Life mencatat baris Useful Life dan Effective From

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Ketik Search `KHS-190A`, tekan Enter
3. Klik link Class Code `KHS-190A` pada tabel
4. Ganti Useful Life dari `16` menjadi `20`
5. Klik `[Save]`
6. Pilih Effective From `Jan 2026`
7. Klik `[Apply]` hingga versi berhasil tersimpan
8. Catat waktu aksi
9. Klik ikon Changelog di toolbar
10. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
11. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-190A" | Field "Useful Life" | Old Value "16" | New Value "20" | Modified By "Rina P"
12. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-190A" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026" | Modified By "Rina P"
13. Verifikasi tidak ada baris untuk Field "Allowed Methods", "Regulation Reference" (tidak berubah), "Straight Line Rate", atau "Declining Balance Rate" di Changelog
14. Tutup Popup Changelog
15. Buka Detail User Rina Puspita > Tab System Log
16. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
17. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190A" | Field "Useful Life" | Old Value "16" | New Value "20"
18. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190A" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026"
19. Verifikasi tidak ada baris untuk Field "Allowed Methods", "Regulation Reference" (tidak berubah), "Straight Line Rate", atau "Declining Balance Rate" di System Log Rina Puspita
20. Buka Reports & Logs > Activity Log, tab `User Action`
21. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
22. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190A" | Field "Useful Life" | Old Value "16" | New Value "20" | Modified By "Rina P"
23. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190A" | Field "Effective From" | Old Value "Jan 2025" | New Value "Jan 2026" | Modified By "Rina P"
24. Verifikasi tidak ada baris untuk Field "Allowed Methods", "Regulation Reference" (tidak berubah), "Straight Line Rate", atau "Declining Balance Rate" di Activity Log
25. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-683: Log L-03: perubahan Allowed Methods mencatat baris Allowed Methods dan Effective From

26. Catat baseline jumlah entri Changelog
27. Ketik Search `KHS-190B`, tekan Enter
28. Klik link Class Code `KHS-190B` pada tabel
29. Lepas `Declining Balance` dari Allowed Methods
30. Klik `[Save]`
31. Pilih Effective From `Jan 2026`
32. Klik `[Apply]` hingga versi berhasil tersimpan
33. Klik ikon Changelog di toolbar
34. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
35. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-190B" | Field "Allowed Methods" | Old Value "Straight Line · Declining Balance" | New Value "Straight Line" | Modified By "Rina P"
36. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-190B" | Field "Effective From" | Old Value "—" | New Value "Jan 2026" | Modified By "Rina P"
37. Verifikasi tidak ada baris untuk Field "Useful Life" di Changelog
38. Tutup Popup Changelog
39. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-684: Log L-03: Regulation Reference yang berubah bersama Useful Life ikut dicatat nilai lama dan barunya

40. Catat baseline jumlah entri Changelog
41. Ketik Search `KHS-190C`, tekan Enter
42. Klik link Class Code `KHS-190C` pada tabel
43. Ganti Regulation Reference menjadi `PMK 72/2023`
44. Ganti Useful Life menjadi `10`
45. Klik `[Save]`
46. Pilih Effective From `Jan 2026`
47. Klik `[Apply]` hingga versi berhasil tersimpan
48. Klik ikon Changelog di toolbar
49. Verifikasi jumlah entri Changelog bertambah tepat 3 dari baseline
50. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-190C" | Field "Regulation Reference" | Old Value "UU HPP 7/2021; PMK 72/2023" | New Value "PMK 72/2023" | Modified By "Rina P"
51. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-190C" | Field "Useful Life" | Old Value "8" | New Value "10" | Modified By "Rina P"
52. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-190C" | Field "Effective From" | Old Value "—" | New Value "Jan 2026" | Modified By "Rina P"
53. Tutup Popup Changelog
54. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-932: Log L-03: Effective From sama dengan versi Current tidak menulis baris Effective From di Changelog, System Log, dan Activity Log

55. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
56. Ketik Search `KHS-190D`, tekan Enter
57. Klik link Class Code `KHS-190D` pada tabel
58. Ganti Useful Life dari `10` menjadi `12`
59. Klik `[Save]`
60. Pilih Effective From `Jan 2026`
61. Klik `[Apply]` hingga versi berhasil tersimpan
62. Catat waktu aksi
63. Klik ikon Changelog di toolbar
64. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
65. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-190D" | Field "Useful Life" | Old Value "10" | New Value "12" | Modified By "Rina P"
66. Verifikasi tidak ada baris untuk Field "Effective From" (nilainya tidak berubah, Jan 2026 tetap Jan 2026) dan tidak ada baris untuk Field "Allowed Methods", "Regulation Reference", "Straight Line Rate", maupun "Declining Balance Rate" di Changelog
67. Tutup Popup Changelog
68. Buka Detail User Rina Puspita > Tab System Log
69. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
70. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190D" | Field "Useful Life" | Old Value "10" | New Value "12"
71. Verifikasi tidak ada baris untuk Field "Effective From" (nilainya tidak berubah, Jan 2026 tetap Jan 2026) dan tidak ada baris untuk Field "Allowed Methods", "Regulation Reference", "Straight Line Rate", maupun "Declining Balance Rate" di System Log Rina Puspita
72. Buka Reports & Logs > Activity Log, tab `User Action`
73. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
74. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-190D" | Field "Useful Life" | Old Value "10" | New Value "12" | Modified By "Rina P"
75. Verifikasi tidak ada baris untuk Field "Effective From" (nilainya tidak berubah, Jan 2026 tetap Jan 2026) dan tidak ada baris untuk Field "Allowed Methods", "Regulation Reference", "Straight Line Rate", maupun "Declining Balance Rate" di Activity Log
76. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (76 langkah, 35 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 9 sampai 24, 33 sampai 38, 48 sampai 53, 63 sampai 75 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Langkah penghubung (S-03, R-16): Search Class Code sebelum membuka tiap class (langkah 2, 27, 41, 56); Search tidak dibawa ke TC berikutnya karena klik sidebar pada langkah penutup tiap blok (langkah 25, 39, 54) membuka ulang halaman dan mereset Search (§ 4, S-09); mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Klausa "tidak ada baris untuk field lain" (TC-FA-TDC-682 d, 683 b, 932 d) ditulis sebagai `Verifikasi` tersendiri sesudah baris yang dicatat pada surface yang sama; selisih jumlah entri tepat sama dengan jumlah baris yang diasersi sehingga baris tersebut menjadi anchor (8b.2). Klausa itu diasersi di spec pencatatan karena merupakan bagian dari Expected TC pencatatan, bukan TC absence tanpa aksi (S-05).
- TC-FA-TDC-683 dan 684 hanya menyebut Changelog; System Log dan Activity Log tidak dibaca. Asersi selisih jumlah entri (2 dan 3) adalah dasar membaca baris baru (S-12), bukan Expected TC.
- TC-FA-TDC-686 (Effective From sama pada Changelog saja) ada di spec 191; TC-FA-TDC-932 mencakup ketiga surface.
- Temuan untuk QA:
  - TC-FA-TDC-682 sampai 684 dan 932 memakai satu Class Code `KHS-LG` untuk empat keadaan; spec memakai satu class per TC (S-06, S-12).
  - TC-FA-TDC-683 dan 684 tidak menyebut Regulation Reference/Date pada Expected sebagian; Date tidak diasersi pada kedua TC.
  - TC-FA-TDC-684 precondition tidak menyebut Active/Used By; spec mengikuti TC-FA-TDC-682 (Active, Used By 0).
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
