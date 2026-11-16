---
id: TC-FA-TDC-E2E-187-log-l-01-create-seed-j-01-l-09-cancel-version-dan-l-11
title: "Pencatatan Log L-01, L-09, dan L-11 pada Changelog, System Log, dan Activity Log: Seed J-01, Create Class, Cancel Scheduled Version, dan Penggantian Versi Scheduled"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-673
  - TC-FA-TDC-672
  - TC-FA-TDC-688
  - TC-FA-TDC-689
sourceRules: ["J-01", "L-01", "§8.4#r6", "§8.3#p1", "§8.2#p1", "§4.1.1#r31", "§8.2#r1", "L-09", "FATDC-LOGIC-04ac", "L-11", "FATDC-LOGIC-04u.2"]
smoke: []
dependsOn: []
trace:
  "J-01": [3, 6, 8]
  "L-01": [3, 6, 21, 22, 23, 24, 27, 28, 29, 30, 32, 33, 34, 35]
  "§8.4#r6": 3
  "§8.3#p1": [6, 32, 33, 34, 50, 51, 71, 72, 73]
  "§8.2#p1": [8, 27, 47, 66]
  "§4.1.1#r31": [22, 23, 44, 61, 62]
  "§8.2#r1": [28, 29, 48, 67, 68]
  "L-09": [43, 44, 47, 48, 50, 51, 60, 61, 66, 67, 71, 72]
  "FATDC-LOGIC-04ac": [44, 61, 62]
  "L-11": [60, 62, 66, 68, 71, 73]
  "FATDC-LOGIC-04u.2": [63, 69, 74]
coverage:
  web: automated
---

# Pencatatan Log L-01, L-09, dan L-11 pada Changelog, System Log, dan Activity Log: Seed J-01, Create Class, Cancel Scheduled Version, dan Penggantian Versi Scheduled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Puspita" (tampil sebagai "Rina P" pada Modified By). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser diatur bersama ke 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta, UTC+07:00) di hook `before` dan dipulihkan di hook `after` (kendali jam di `suite.md`); Fiscal Year Start Januari. Kolom Date log dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Company uji spec ini: company khusus automation yang baru saja mengaktifkan modul akuntansi sehingga tujuh class seed dibuat J-01 dan riwayat log company kosong sebelum aktivasi (dibentuk fixture BE di hook `before`, disediakan tim FE/BE); akun Rina Puspita login pada company itu. Alasan: Expected TC-FA-TDC-673 menyebut 14 baris seed sebagai jumlah absolut (lihat Temuan untuk QA).
- Data Dinamis (di-seed lewat API di hook `before`, dihapus di hook `after`; nilai dari TC, kunci fixture ditetapkan tim FE, `Fixture.fixedAssetTaxDepreciationClass.regulationReference` = `UU HPP 7/2021; PMK 72/2023`): Kode class milik spec berpola `KHS-<nomor spec><huruf>` karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat (S-12); seeding idempotent (dilewati bila kode sudah ada), cleanup hanya menghapus yang dibuat spec ini, suite serial, dan kode berbeda antar spec. Karena kode bisa membawa riwayat log dari run sebelumnya, asersi entri memakai selisih terhadap baseline, bukan baseline nol.

| TC | Class Code | Keadaan |
|---|---|---|
| TC-FA-TDC-673 | tujuh seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) | dibuat J-01 saat aktivasi modul; dibaca, tidak diubah (`Fixture.fixedAssetTaxDepreciationClass.seedClasses`) |
| TC-FA-TDC-672 | `KHS-187A` | belum ada; dibuat spec (Class Name `Kelompok log 1`, Non-building, Useful Life 8, Straight Line dan Declining Balance) |
| TC-FA-TDC-688 | `KHS-187B` | Class Name `Kelompok log uji`; Non-building, Useful Life 8, Straight Line dan Declining Balance; versi Current tanpa Effective From dan versi Scheduled Effective From Jan 2027; Used By 0 |
| TC-FA-TDC-689 | `KHS-187C` | Class Name `Kelompok log uji`; Non-building, Straight Line dan Declining Balance; versi Current tanpa Effective From (Useful Life 8) dan versi Scheduled Effective From Jan 2027 (Useful Life 10); Used By 0 |

- Tabel memuat tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah class milik spec; baris `KHS-*` tampil di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga baris dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` menghapus `KHS-187A`, `KHS-187B`, dan `KHS-187C` lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan jam serta sesi.

## Test Steps

### TC-FA-TDC-673: Log L-01 pada seed (J-01): Changelog dan Activity Log saja dengan Modified By System

1. Catat baseline jumlah entri System Log Rina Puspita
2. Klik ikon Changelog di toolbar
3. Verifikasi Changelog, Dicatat: 14 baris (dua per class seed): Action "Create" | Class Code "[kode seed]" | Field "Class Code" | Old Value "—" | New Value "[kode seed]" | Modified By "System", dan Action "Create" | Class Code "[kode seed]" | Field "Asset Type" | Old Value "—" | New Value "[Asset Type seed]" | Modified By "System"
4. Tutup Popup Changelog
5. Buka Reports & Logs > Activity Log, tab `User Action`
6. Verifikasi Activity Log FAMS, Dicatat: 14 baris (dua per class seed): Action "Create" | Object "Tax Depreciation Class" | Name "[kode seed]" | Field "Class Code" atau "Asset Type" | Old Value "—" | New Value "[kode seed]" atau "[Asset Type seed]" | Modified By "System"
7. Buka Detail User Rina Puspita > Tab System Log
8. Verifikasi System Log Rina Puspita, Tidak dicatat: jumlah entri sama dengan baseline langkah 1
9. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-672: Log L-01: Create class mencatat baris field Class Code dan field Asset Type pada ketiga surface

10. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
11. Klik `+ Class` di toolbar
12. Isi Regulation Reference `UU HPP 7/2021; PMK 72/2023`
13. Isi Class Code `KHS-187A`
14. Isi Class Name `Kelompok log 1`
15. Pilih Asset Type `Non-building`
16. Isi Useful Life `8`
17. Pilih Allowed Methods `Straight Line` dan `Declining Balance`
18. Klik `[Submit]` hingga class berhasil tersimpan
19. Catat waktu aksi
20. Klik ikon Changelog di toolbar
21. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline
22. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Class Code "KHS-187A" | Field "Class Code" | Old Value "—" | New Value "KHS-187A" | Modified By "Rina P"
23. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Class Code "KHS-187A" | Field "Asset Type" | Old Value "—" | New Value "Non-building" | Modified By "Rina P"
24. Verifikasi tidak ada baris untuk Field "Class Name", "Useful Life", "Allowed Methods", atau "Regulation Reference" pada entri baru di Changelog
25. Tutup Popup Changelog
26. Buka Detail User Rina Puspita > Tab System Log
27. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 2 dari baseline
28. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187A" | Field "Class Code" | Old Value "—" | New Value "KHS-187A"
29. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187A" | Field "Asset Type" | Old Value "—" | New Value "Non-building"
30. Verifikasi tidak ada baris untuk Field "Class Name", "Useful Life", "Allowed Methods", atau "Regulation Reference" pada entri baru di System Log Rina Puspita
31. Buka Reports & Logs > Activity Log, tab `User Action`
32. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline
33. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187A" | Field "Class Code" | Old Value "—" | New Value "KHS-187A" | Modified By "Rina P"
34. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187A" | Field "Asset Type" | Old Value "—" | New Value "Non-building" | Modified By "Rina P"
35. Verifikasi tidak ada baris untuk Field "Class Name", "Useful Life", "Allowed Methods", atau "Regulation Reference" pada entri baru di Activity Log
36. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-688: Log L-09: Cancel Scheduled Version mencatat Scheduled Version dari Effective From menjadi —

37. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
38. Klik link Class Code `KHS-187B` pada tabel
39. Klik `[Cancel scheduled version]` pada Alert
40. Klik `[Cancel version]` hingga versi berhasil dibatalkan
41. Catat waktu aksi
42. Klik ikon Changelog di toolbar
43. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
44. Verifikasi Changelog, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "KHS-187B (Jan 2027)" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—" | Modified By "Rina P"
45. Tutup Popup Changelog
46. Buka Detail User Rina Puspita > Tab System Log
47. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 1 dari baseline
48. Verifikasi System Log Rina Puspita, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-187B" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—"
49. Buka Reports & Logs > Activity Log, tab `User Action`
50. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline
51. Verifikasi Activity Log FAMS, Dicatat: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-187B" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—" | Modified By "Rina P"
52. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-689: Log L-09 dan L-11: penggantian versi Scheduled dengan Effective From sama ditulis dalam transaksi yang sama

53. Catat baseline jumlah entri Changelog, System Log Rina Puspita, dan Activity Log
54. Klik link Class Code `KHS-187C` pada tabel
55. Ganti Useful Life menjadi `12`
56. Klik `[Save]`
57. Pilih Effective From `Jan 2027`
58. Klik `[Apply]` hingga versi berhasil tersimpan
59. Klik ikon Changelog di toolbar
60. Verifikasi jumlah entri Changelog bertambah tepat 5 dari baseline
61. Verifikasi Changelog, Dicatat: Action "Edit" | Class Code "KHS-187C (Jan 2027)" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—" | Modified By "Rina P"
62. Verifikasi Changelog, Dicatat: empat baris L-11 (Action "Create" | Class Code "KHS-187C (Jan 2027)") untuk Field "Regulation Reference", "Useful Life" (New Value "12"), "Allowed Methods", dan "Effective From" (New Value "Jan 2027"), Old Value "—", Modified By "Rina P"
63. Verifikasi satu baris L-09 dan empat baris L-11 di Changelog memiliki Date (waktu aksi) yang sama
64. Tutup Popup Changelog
65. Buka Detail User Rina Puspita > Tab System Log
66. Verifikasi jumlah entri System Log Rina Puspita bertambah tepat 5 dari baseline
67. Verifikasi System Log Rina Puspita, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-187C" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—"
68. Verifikasi System Log Rina Puspita, Dicatat: empat baris L-11 (Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187C") untuk Field "Regulation Reference", "Useful Life" (New Value "12"), "Allowed Methods", dan "Effective From" (New Value "Jan 2027")
69. Verifikasi satu baris L-09 dan empat baris L-11 di System Log Rina Puspita memiliki Date yang sama
70. Buka Reports & Logs > Activity Log, tab `User Action`
71. Verifikasi jumlah entri Activity Log bertambah tepat 5 dari baseline
72. Verifikasi Activity Log FAMS, Dicatat: Action "Edit" | Object "Tax Depreciation Class" | Name "KHS-187C" | Field "Scheduled Version" | Old Value "Jan 2027" | New Value "—" | Modified By "Rina P"
73. Verifikasi Activity Log FAMS, Dicatat: empat baris L-11 (Action "Create" | Object "Tax Depreciation Class" | Name "KHS-187C") untuk Field "Regulation Reference", "Useful Life" (New Value "12"), "Allowed Methods", dan "Effective From" (New Value "Jan 2027"), Modified By "Rina P"
74. Verifikasi satu baris L-09 dan empat baris L-11 di Activity Log memiliki Date yang sama
75. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (75 langkah, 26 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 2 sampai 8, 20 sampai 35, 42 sampai 51, 59 sampai 74 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Urutan TC: TC-FA-TDC-673, 672, 688, 689. TC-FA-TDC-673 dibaca lebih dulu karena membaca seluruh entri seed pada company yang riwayat lognya baru, sebelum aksi tulis lain menambah entri (S-10).
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Asersi "tidak dicatat" pada System Log TC-FA-TDC-673 (langkah 1 dan 8) memakai selisih jumlah entri terhadap baseline (S-12); anchor positifnya adalah 14 baris Changelog (langkah 3) dan 14 baris Activity Log (langkah 6) dari pemicu yang sama (8b.2). Asersi "tepat N baris" per surface adalah asersi jumlah, bukan absence (prinsip 13g).
- Asersi selisih jumlah entri pada TC-FA-TDC-688 dan TC-FA-TDC-689 (1 dan 5) adalah dasar membaca baris baru (S-12, S-14); Expected TC-688 tidak menyebut jumlah.
- Temuan untuk QA:
  - TC-FA-TDC-673 menyebut 14 baris seed sebagai jumlah absolut pada audit trail permanen (S-12); asersi hanya deterministik pada company yang riwayat lognya direset fixture BE (disediakan tim FE/BE). TC juga tidak menyebut company mana yang "baru" dan akun yang dipakai pada company itu.
  - TC-FA-TDC-673 tidak menyebut Asset Type tiap class seed pada Expected ([Asset Type seed]); spec merujuk `Fixture.fixedAssetTaxDepreciationClass.seedClasses`.
  - TC-FA-TDC-688 dan TC-FA-TDC-689 tidak menyebut Asset Type, Allowed Methods, dan Useful Life versi Current; spec memakai nilai TC-FA-TDC-672 (Non-building, Straight Line dan Declining Balance, Useful Life 8). TC-689 tidak menyebut Old Value dan New Value baris L-11 untuk Regulation Reference dan Allowed Methods.
  - TC-FA-TDC-688 tidak menyebut keadaan Drawer Edit sesudah `[Cancel version]`; spec langsung mengklik ikon Changelog di toolbar mengikuti TC.
  - TC-FA-TDC-672 Catatan "Ketiga log ditulis dalam satu transaksi" tidak punya Expected sendiri; tidak diasersi.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
