---
id: TC-FA-TDC-E2E-196-log-entri-class-dihapus-utuh-modified-by-hover-dan-system-log-aktor
title: "Pencatatan Log: Entri Lama Tidak Berubah, Modified By Hover Nama Lengkap, dan Isolasi System Log per Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-787
  - TC-FA-TDC-723
  - TC-FA-TDC-724
  - TC-FA-TDC-722
coverage:
  web: automated
---

# Pencatatan Log: Entri Lama Tidak Berubah, Modified By Hover Nama Lengkap, dan Isolasi System Log per Aktor

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control "Rina Pratama" (tampil sebagai "Rina P" pada Modified By; nama lengkap pada tooltip). Pembanding TC-FA-TDC-724: Total Control "Budi Santoso" (bukan aktor, tidak login). Email dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini sebagai Rina Pratama; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor (dan Detail User Budi Santoso untuk TC-FA-TDC-724); Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): sembilan class Example Data PRD (BLD-NP, BLD-P, LAND, NB-1, NB-2, NB-4, NB-KHS, NB-OLD, NB-SL, `Fixture.fixedAssetTaxDepreciationClass.exampleData`); NB-SL memiliki entri Changelog Edit Class Name dari `Kelompok khusus SL` ke `Kelompok khusus Straight Line` (dibentuk fixture BE); NB-OLD Inactive dengan Used By 0; NB-4 Active dengan Used By 0 dan tanpa Last Posted Tax Year. Tabel memuat 9 baris pada satu halaman sehingga baris target dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` mengembalikan Class Name NB-SL, status NB-OLD, dan membuat ulang NB-4 sebagai Active lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan sesi.

## Test Steps

### TC-FA-TDC-787: Class Name yang diubah tidak mengubah entri Changelog lama

1. Catat baseline jumlah entri Changelog untuk Class Code `NB-SL`
2. Klik link Class Code `NB-SL` pada tabel
3. Ganti Class Name menjadi `Kelompok khusus Straight Line 2`
4. Klik `[Save]` hingga perubahan berhasil tersimpan
5. Klik ikon Changelog di toolbar
6. Filter Class Code `NB-SL`
7. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline untuk Class Code `NB-SL`
8. Verifikasi Changelog memuat baris baru: Action "Edit" | Class Code "NB-SL" | Field "Class Name" | Old Value "Kelompok khusus Straight Line" | New Value "Kelompok khusus Straight Line 2"
9. Verifikasi baris lama tetap menampilkan Old Value "Kelompok khusus SL" dan New Value "Kelompok khusus Straight Line"
10. Tutup Popup Changelog
11. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-723: Modified By pada log Activate berformat nama depan dan inisial belakang dengan hover nama lengkap

12. Catat baseline jumlah entri Changelog
13. Klik toggle `Active` baris NB-OLD
14. Klik `[Activate]` pada dialog hingga status berhasil tersimpan
15. Klik ikon Changelog di toolbar
16. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline
17. Verifikasi kolom Modified By pada baris Status NB-OLD berisi "Rina P"
18. Arahkan kursor ke nilai Modified By pada baris terbaru
19. Verifikasi tooltip hover Modified By menampilkan nama lengkap "Rina Pratama"
20. Tutup Popup Changelog
21. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-724: Baris System Log Deactivate hanya tertulis pada Detail User aktor, bukan user lain

22. Catat baseline jumlah entri System Log Rina Pratama dan System Log Budi Santoso
23. Klik toggle `Active` baris NB-4
24. Klik `[Deactivate]` pada dialog hingga status berhasil tersimpan
25. Buka Global Settings > User > Detail milik Rina Pratama, tab System Log
26. Verifikasi jumlah entri System Log Rina Pratama bertambah tepat 1 dari baseline
27. Verifikasi System Log Rina Pratama memuat satu baris Status NB-4: Action "Edit" | Field "Status" | Old Value "Active" | New Value "Inactive"
28. Buka Global Settings > User > Detail milik Budi Santoso, tab System Log
29. Verifikasi jumlah entri System Log Budi Santoso sama dengan baseline langkah 22
30. Verifikasi System Log Budi Santoso tidak memuat baris Status NB-4
31. Buka Settings > Accounting > Tax Depreciation Class
32. Pulihkan NB-4 menjadi Active lewat sesi API aktor hingga status berhasil tersimpan

### TC-FA-TDC-722: Entri log class yang dihapus tetap utuh dan tidak berubah retroaktif

33. Catat baseline jumlah entri Changelog untuk Class Code `NB-4`
34. Klik toggle `Active` baris NB-4
35. Klik `[Deactivate]` pada dialog hingga status berhasil tersimpan
36. Klik toggle `Active` baris NB-4
37. Klik `[Activate]` pada dialog hingga status berhasil tersimpan
38. Klik tombol ⋯ baris NB-4
39. Pilih `Delete`
40. Klik `[Delete]` pada dialog hingga class berhasil dihapus
41. Klik ikon Changelog di toolbar
42. Filter Class Code `NB-4`
43. Verifikasi jumlah entri Changelog bertambah tepat 3 dari baseline untuk Class Code `NB-4`
44. Verifikasi baris terbaru Changelog NB-4: Action "Delete" | Field "Class Code" | Old Value "NB-4" | New Value "—"
45. Verifikasi baris terbaru Changelog NB-4: Action "Edit" | Field "Status" | Old Value "Inactive" | New Value "Active"
46. Verifikasi baris terbaru Changelog NB-4: Action "Edit" | Field "Status" | Old Value "Active" | New Value "Inactive"
47. Verifikasi kedua baris Status yang lebih lama tetap menampilkan Old Value dan New Value semula setelah class dihapus
48. Tutup Popup Changelog
49. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (49 langkah, 23 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 5 sampai 10, 15 sampai 20, 25 sampai 30, 41 sampai 48 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Urutan TC: 787, 723, 724, 722. TC-FA-TDC-722 menghapus NB-4 sehingga diletakkan di akhir (S-10); TC-FA-TDC-724 menonaktifkan NB-4, jadi langkah 32 memulihkan NB-4 menjadi Active sebelum TC-722 (langkah penghubung, S-09).
- TC-FA-TDC-724: Expected a (System Log Budi Santoso tidak memuat baris) ditulis sesudah Expected b (baris Status NB-4 pada System Log Rina Pratama, langkah 27) karena baris aktor adalah anchor positif untuk absence (8b.2); urutan Expected dibalik demi anchor. Langkah 22 mencatat juga baseline System Log Budi Santoso, dan langkah 29 (selisih nol terhadap baseline pada surface yang sama) adalah asersi tambahan di luar Expected TC (S-03) yang menjadi anchor absence langkah 30 (8b.2, S-12). Asersi isolasi log per aktor bukan kelas g dan boleh berada di spec pencatatan (prinsip 13g).
- TC-FA-TDC-722: himpunan tiga baris teratas Changelog `NB-4` diasersi sesudah selisih tepat 3 terbukti; TC menyebut urutan, sedangkan entri yang jatuh dalam menit yang sama tidak diasersi urutannya (S-14).
- Langkah penghubung (S-03): mencatat baseline, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Temuan untuk QA:
  - TC-FA-TDC-722 sampai 724 menyebut aktor "Rina Pratama" sedangkan TC pencatatan lain (672 sampai 689, 932) menyebut "Rina Puspita"; spec ini memakai Rina Pratama sesuai TC. Email kedua user tidak tertulis (R-06).
  - TC-FA-TDC-724 mensyaratkan "Login sbg Rina Pratama" dan user kedua Budi Santoso (Total Control); spec membaca System Log Budi Santoso lewat Detail User tanpa login sebagai Budi.
  - TC-FA-TDC-787 menyebut filter Class Code pada Changelog dan entri lama `Kelompok khusus SL`; mekanisme pembentukan entri lama (fixture BE atau seed Example Data) tidak disebut, spec menganggap fixture BE (S-13). TC-722 dan 723 tidak menyebut cara membaca baris terbaru selain urutan Date.
  - TC-FA-TDC-787, 723, 724, 722 memakai class Example Data/seed literal sebagai target aksi tulis; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
