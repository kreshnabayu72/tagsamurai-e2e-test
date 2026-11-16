---
id: TC-FA-TDC-E2E-189-log-l-02-class-code-tidak-diperbarui-ulang-edit-sekaligus-dan-kapitalisasi
title: "Pencatatan Log L-02 pada Tiga Surface: Class Code Tidak Diperbarui Ulang, Edit Tiga Field Sekaligus, dan Perubahan Kapitalisasi"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-678
  - TC-FA-TDC-679
  - TC-FA-TDC-680
sourceRules: ["FATDC-LOGIC-04c", "L-02d", "L-02a", "§4.1.1#r31", "L-01", "L-02e", "§8.2#p1", "L-02b", "§8.2#r1", "§8.3#p1", "L-02c", "F-FATDC-02.k11d", "§8#b1", "§[F-FATDC-02] Edit Tax Depreciation Class#r43"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04c": [9, 16, 21, 34, 36, 37, 40, 41, 43, 44]
  "L-02d": [10, 11, 17, 18, 22, 23, 35, 41, 44, 52, 53, 57, 60]
  "L-02a": [10, 11, 35, 36, 37, 53]
  "§4.1.1#r31": [10, 11, 35, 36, 37, 53]
  "L-01": [13, 19, 25]
  "L-02e": [13, 19, 25]
  "§8.2#p1": [16, 40, 56]
  "L-02b": [17, 18, 41, 57]
  "§8.2#r1": [17, 18, 41, 57]
  "§8.3#p1": [21, 22, 23, 43, 44, 59, 60]
  "L-02c": [22, 23, 44, 60]
  "F-FATDC-02.k11d": 34
  "§8#b1": [52, 53, 56, 59]
  "§[F-FATDC-02] Edit Tax Depreciation Class#r43": 52
coverage:
  web: automated
---

# Pencatatan Log L-02 pada Tiga Surface: Class Code Tidak Diperbarui Ulang, Edit Tiga Field Sekaligus, dan Perubahan Kapitalisasi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol. Entri Create tiap class seed tercatat saat seeding (Changelog, System Log, dan Activity Log).

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-678 | `KHS-189A` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0, satu versi tanpa Effective From, Last Posted Tax Year kosong; `KHS-189B` dan `KHS-189C` belum ada |
| TC-FA-TDC-679 | `KHS-189D` | keadaan sama dengan `KHS-189A`; `KHS-189E` belum ada |
| TC-FA-TDC-680 | `KHS-189F` | keadaan sama dengan `KHS-189A` |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah class milik spec; baris `KHS-*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` menghapus class hasil uji (`KHS-189C`, `KHS-189E`, dan `Khs-189F`) lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan jam serta sesi.

## Test Steps

### TC-FA-TDC-678: Log L-02e: entri log yang sudah ditulis tidak diperbarui saat Class Code diubah lagi

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Klik link Class Code `KHS-189A` pada tabel
3. Ganti Class Code menjadi `KHS-189B`
4. Klik `[Save]` hingga perubahan berhasil tersimpan
5. Klik link Class Code `KHS-189B` pada tabel
6. Ganti Class Code menjadi `KHS-189C`
7. Klik `[Save]` hingga perubahan berhasil tersimpan
8. Klik ikon Changelog di toolbar
9. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
10. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-189B" | Field "Class Code" | Old Value "KHS-189A" | New Value "KHS-189B" | Modified By "Rina P"
11. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-189C" | Field "Class Code" | Old Value "KHS-189B" | New Value "KHS-189C" | Modified By "Rina P"
12. Ketik Search `KHS-189A`, tekan Enter
13. Verifikasi Changelog memuat baris Action "Create" | Class Code "KHS-189A" | Field "Class Code" | Old Value "—" | New Value "KHS-189A" yang tidak diperbarui menjadi kode baru
14. Tutup Popup Changelog
15. Buka Detail User Rina Puspita > Tab System Log
16. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
17. Verifikasi System Log Rina Puspita, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189B" | Field "Class Code" | Old Value "KHS-189A" | New Value "KHS-189B"
18. Verifikasi System Log Rina Puspita, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189C" | Field "Class Code" | Old Value "KHS-189B" | New Value "KHS-189C"
19. Verifikasi System Log Rina Puspita memuat baris Action "Create" | Object "Tax Depreciation Class" | Name "KHS-189A" yang tidak diperbarui menjadi kode baru
20. Buka Reports & Logs > Activity Log, tab `User Action`
21. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
22. Verifikasi Activity Log FAMS, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189B" | Field "Class Code" | Old Value "KHS-189A" | New Value "KHS-189B" | Modified By "Rina P"
23. Verifikasi Activity Log FAMS, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189C" | Field "Class Code" | Old Value "KHS-189B" | New Value "KHS-189C" | Modified By "Rina P"
24. Ketik Search `KHS-189A`, tekan Enter
25. Verifikasi Activity Log FAMS memuat baris Action "Create" | Object "Tax Depreciation Class" | Name "KHS-189A" yang tidak diperbarui menjadi kode baru
26. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-679: Log L-02: Edit Class Code, Class Name, dan Regulation Reference sekaligus mencatat tiga baris tanpa hilang dan tanpa duplikat

27. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
28. Klik link Class Code `KHS-189D` pada tabel
29. Ganti Class Code menjadi `KHS-189E`
30. Ganti Class Name menjadi `Kelompok log D`
31. Ganti Regulation Reference menjadi `UU HPP 7/2021`
32. Klik `[Save]` hingga perubahan berhasil tersimpan
33. Klik ikon Changelog di toolbar
34. Verifikasi jumlah entri Changelog bertambah tepat 3 dari baseline (tepat tiga baris; tidak ada baris ganda; tidak ada baris untuk record lain)
35. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-189E" | Field "Class Code" | Old Value "KHS-189D" | New Value "KHS-189E" | Modified By "Rina P"
36. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-189E" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log D" | Modified By "Rina P"
37. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-189E" | Field "Regulation Reference" | Old Value "UU HPP 7/2021; PMK 72/2023" | New Value "UU HPP 7/2021" | Modified By "Rina P"
38. Tutup Popup Changelog
39. Buka Detail User Rina Puspita > Tab System Log
40. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 3 dari baseline (tepat tiga baris; tidak ada baris ganda; tidak ada baris untuk record lain)
41. Verifikasi System Log Rina Puspita, Dicatat: tiga baris Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189E" untuk Field "Class Code" ("KHS-189D" → "KHS-189E"), "Class Name" ("Kelompok log uji" → "Kelompok log D"), dan "Regulation Reference" ("UU HPP 7/2021; PMK 72/2023" → "UU HPP 7/2021")
42. Buka Reports & Logs > Activity Log, tab `User Action`
43. Verifikasi jumlah entri Activity Log bertambah tepat 3 dari baseline (tepat tiga baris; tidak ada baris ganda; tidak ada baris untuk record lain)
44. Verifikasi Activity Log FAMS, Dicatat: tiga baris Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-189E", Modified By "Rina P" untuk Field "Class Code" ("KHS-189D" → "KHS-189E"), "Class Name" ("Kelompok log uji" → "Kelompok log D"), dan "Regulation Reference" ("UU HPP 7/2021; PMK 72/2023" → "UU HPP 7/2021")
45. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-680: Log L-02: perubahan Class Code hanya kapitalisasi dicatat sebagai perubahan nyata

46. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
47. Klik link Class Code `KHS-189F` pada tabel
48. Ganti Class Code dari `KHS-189F` menjadi `Khs-189F`
49. Klik `[Save]` hingga perubahan berhasil tersimpan
50. Catat waktu aksi
51. Klik ikon Changelog di toolbar
52. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
53. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "Khs-189F" | Field "Class Code" | Old Value "KHS-189F" | New Value "Khs-189F" | Modified By "Rina P"
54. Tutup Popup Changelog
55. Buka Detail User Rina Puspita > Tab System Log
56. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
57. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "Khs-189F" | Field "Class Code" | Old Value "KHS-189F" | New Value "Khs-189F"
58. Buka Reports & Logs > Activity Log, tab `User Action`
59. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
60. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "Khs-189F" | Field "Class Code" | Old Value "KHS-189F" | New Value "Khs-189F" | Modified By "Rina P"
61. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (61 langkah, 21 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 8 sampai 25, 33 sampai 44, 51 sampai 60 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, Search kode awal pada Changelog dan Activity Log untuk membaca entri Create (langkah penghubung, R-16), dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Tiga TC memakai class berbeda (`KHS-189A`, `KHS-189D`, `KHS-189F`) karena tiap TC mengonsumsi keadaan class; TC sumber memakai satu kode `KHS-LG`. Tabel memuat tepat 10 baris (7 seed ditambah tiga class milik spec).
- Expected TC-FA-TDC-678 b (Name pada baris perubahan pertama tetap `KHS-189B`) dipenuhi oleh `Verifikasi` baris pertama pada System Log dan Activity Log; Expected c (entri Create `KHS-189A` tidak diperbarui) ditulis sebagai `Verifikasi` tersendiri per surface.
- Temuan untuk QA:
  - TC-FA-TDC-678 (c) menyebut entri `KHS-LG` pada log Create tanpa surface dan tanpa cara menemukannya; spec menganggap seeding lewat API menulis entri Create (mekanisme tidak disebut TC, S-13) dan mencarinya lewat Search Class Code awal pada Changelog dan Activity Log; System Log dibaca tanpa Search.
  - TC-FA-TDC-679 tidak menyebut Date; spec tidak mengasersi Date. TC-FA-TDC-678 dan 679 tidak menyebut Date pada Expected.
  - TC-FA-TDC-679 memakai satu baris `Verifikasi` untuk pola tiga baris pada System Log dan Activity Log ("pola yang sama"); Old Value Class Name dan Regulation Reference mengikuti precondition TC.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
