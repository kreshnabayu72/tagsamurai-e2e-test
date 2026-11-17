---
id: TC-FA-TDC-E2E-188-log-l-02-edit-class-name-regulation-reference-dan-class-code
title: "Pencatatan Log L-02 pada Tiga Surface: Edit Class Name, Regulation Reference, dan Class Code"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-675
  - TC-FA-TDC-676
  - TC-FA-TDC-677
sourceRules: ["FATDC-LOGIC-04c", "§4.1.1#r42", "§4.1.1#r31", "§8.2#p1", "§8.2#r1", "§8.3#p1", "F-FATDC-02.k11d", "E-FATDC-16", "L-02d", "L-02a", "L-02b", "L-02c"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04c": [7, 8, 11, 12, 14, 15, 23, 24, 27, 28, 30, 31, 40, 42, 46, 48, 51, 53]
  "§4.1.1#r42": 7
  "§4.1.1#r31": [8, 24, 41, 42]
  "§8.2#p1": [11, 27, 46]
  "§8.2#r1": [12, 28, 47]
  "§8.3#p1": [14, 15, 30, 31, 51, 52]
  "F-FATDC-02.k11d": 23
  "E-FATDC-16": 40
  "L-02d": [41, 47, 52]
  "L-02a": [41, 42, 43]
  "L-02b": [47, 48, 49]
  "L-02c": [52, 53, 54]
coverage:
  web: automated
---

# Pencatatan Log L-02 pada Tiga Surface: Edit Class Name, Regulation Reference, dan Class Code

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-675 | `KHS-188A` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`, Active, Used By 0, satu versi tanpa Effective From, Last Posted Tax Year kosong |
| TC-FA-TDC-676 | `KHS-188B` | keadaan sama dengan `KHS-188A` |
| TC-FA-TDC-677 | `KHS-188C` | keadaan sama dengan `KHS-188A`; `KHS-188D` belum ada |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah class milik spec; baris `KHS-*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` menghapus `KHS-188A`, `KHS-188B`, `KHS-188C`, dan `KHS-188D` (hasil ganti kode) lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan jam serta sesi.

## Test Steps

### TC-FA-TDC-675: Log L-02: Edit Class Name mencatat satu baris pada ketiga surface

1. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
2. Klik link Class Code `KHS-188A` pada tabel
3. Ganti Class Name dari `Kelompok log uji` menjadi `Kelompok log ubah`
4. Klik `[Save]` hingga perubahan berhasil tersimpan
5. Catat waktu aksi
6. Klik ikon Changelog di toolbar
7. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline (tepat satu baris; tidak ada baris untuk field yang tidak berubah)
8. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-188A" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah" | Modified By "Rina P"
9. Tutup Popup Changelog
10. Buka Detail User Rina Puspita > Tab System Log
11. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline (tepat satu baris; tidak ada baris untuk field yang tidak berubah)
12. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188A" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah"
13. Buka Reports & Logs > Activity Log, tab `User Action`
14. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline (tepat satu baris; tidak ada baris untuk field yang tidak berubah)
15. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188A" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah" | Modified By "Rina P"
16. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-676: Log L-02: Edit Regulation Reference mencatat satu baris pada ketiga surface

17. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
18. Klik link Class Code `KHS-188B` pada tabel
19. Ganti Regulation Reference menjadi `PMK 72/2023`
20. Klik `[Save]` hingga perubahan berhasil tersimpan
21. Catat waktu aksi
22. Klik ikon Changelog di toolbar
23. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
24. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-188B" | Field "Regulation Reference" | Old Value "UU HPP 7/2021; PMK 72/2023" | New Value "PMK 72/2023" | Modified By "Rina P"
25. Tutup Popup Changelog
26. Buka Detail User Rina Puspita > Tab System Log
27. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
28. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188B" | Field "Regulation Reference" | Old Value "UU HPP 7/2021; PMK 72/2023" | New Value "PMK 72/2023"
29. Buka Reports & Logs > Activity Log, tab `User Action`
30. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
31. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188B" | Field "Regulation Reference" | Old Value "UU HPP 7/2021; PMK 72/2023" | New Value "PMK 72/2023" | Modified By "Rina P"
32. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-677: Log L-02a-d: Edit Class Code mencatat kode lama dan baru dan memakai kode baru pada kolom identitas semua baris

33. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
34. Klik link Class Code `KHS-188C` pada tabel
35. Ganti Class Code menjadi `KHS-188D`
36. Ganti Class Name menjadi `Kelompok log ubah`
37. Klik `[Save]` hingga perubahan berhasil tersimpan
38. Catat waktu aksi
39. Klik ikon Changelog di toolbar
40. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
41. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-188D" | Field "Class Code" | Old Value "KHS-188C" | New Value "KHS-188D" | Modified By "Rina P"
42. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-188D" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah" | Modified By "Rina P"
43. Verifikasi kolom Class Code Changelog berisi "KHS-188D" (kode setelah perubahan) untuk kedua baris
44. Tutup Popup Changelog
45. Buka Detail User Rina Puspita > Tab System Log
46. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
47. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188D" | Field "Class Code" | Old Value "KHS-188C" | New Value "KHS-188D"
48. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188D" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah"
49. Verifikasi kolom Name System Log Rina Puspita berisi "KHS-188D" (kode setelah perubahan) untuk kedua baris
50. Buka Reports & Logs > Activity Log, tab `User Action`
51. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
52. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188D" | Field "Class Code" | Old Value "KHS-188C" | New Value "KHS-188D" | Modified By "Rina P"
53. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-188D" | Field "Class Name" | Old Value "Kelompok log uji" | New Value "Kelompok log ubah" | Modified By "Rina P"
54. Verifikasi kolom Name Activity Log berisi "KHS-188D" (kode setelah perubahan) untuk kedua baris
55. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (55 langkah, 19 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 6 sampai 15, 22 sampai 31, 39 sampai 54 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Asersi "tepat satu baris per surface (tidak ada baris untuk field yang tidak berubah)" pada TC-FA-TDC-675 ditulis sebagai selisih jumlah entri tepat 1 terhadap baseline (asersi jumlah, bukan absence, prinsip 13g; S-12).
- Ketiga TC memakai class berbeda (`KHS-188A`, `KHS-188B`, `KHS-188C`) karena tiap TC mengonsumsi keadaan class; TC sumber memakai satu kode `KHS-LG`.
- Temuan untuk QA:
  - TC-FA-TDC-675 sampai 677 memakai satu Class Code `KHS-LG` untuk tiga keadaan terpisah; spec memakai satu class per TC (S-06, S-12).
  - TC-FA-TDC-677 Expected d (kolom identitas berisi kode setelah perubahan) tumpang tindih dengan Expected a sampai c; spec menulisnya sebagai `Verifikasi` per surface.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
