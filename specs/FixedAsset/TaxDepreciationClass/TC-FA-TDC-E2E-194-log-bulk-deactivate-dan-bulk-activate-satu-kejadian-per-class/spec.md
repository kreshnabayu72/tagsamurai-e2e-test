---
id: TC-FA-TDC-E2E-194-log-bulk-deactivate-dan-bulk-activate-satu-kejadian-per-class
title: "Pencatatan Log L-04 Bulk Deactivate dan Bulk Activate: Satu Kejadian per Class di Tiga Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-707
  - TC-FA-TDC-708
  - TC-FA-TDC-709
  - TC-FA-TDC-710
  - TC-FA-TDC-711
coverage:
  web: automated
---

# Pencatatan Log L-04 Bulk Deactivate dan Bulk Activate: Satu Kejadian per Class di Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Nama tampil, email, dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser sinkron (kendali jam di `suite.md`); kolom Date Changelog dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD dan NB-OLD2 (Inactive, Used By 0); NB-3 dan NB-4 Active dengan Used By 0. Tabel memuat 9 baris pada satu halaman sehingga baris target dicentang tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` mengembalikan NB-3 dan NB-4 ke Active serta NB-OLD dan NB-OLD2 ke Inactive lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan sesi.

## Test Steps

### TC-FA-TDC-707, 708, 709: Bulk Deactivate (L-04) tercatat satu kejadian per class di Changelog, System Log, dan Activity Log

1. Catat baseline jumlah entri Changelog, System Log user aktor, dan Activity Log (filter Object `Tax Depreciation Class`)
2. Centang baris NB-3
3. Centang baris NB-4
4. Klik `Deactivate` pada Bulk Action Bar
5. Klik `[Deactivate]` pada dialog hingga status berhasil tersimpan
6. Catat waktu aksi
7. Klik ikon Changelog di toolbar
8. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
9. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-3" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
10. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
11. Tutup Popup Changelog
12. Buka Global Settings > User > Detail milik user aktor, tab System Log
13. Verifikasi jumlah entri System Log user aktor bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
14. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-3" | Field "Status" | Old Value "Active" | New Value "Inactive"
15. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive"
16. Buka Reports & Logs > Activity Log, tab `User Action`
17. Filter Object `Tax Depreciation Class`
18. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
19. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-3" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By user aktor
20. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By user aktor
21. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-710, 711: Bulk Activate (L-04) tercatat satu kejadian per class di Changelog dan System Log

22. Catat baseline jumlah entri Changelog dan System Log user aktor
23. Centang baris NB-OLD
24. Centang baris NB-OLD2
25. Klik `Activate` pada Bulk Action Bar
26. Klik `[Activate]` pada dialog hingga status berhasil tersimpan
27. Catat waktu aksi
28. Klik ikon Changelog di toolbar
29. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
30. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
31. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-OLD2" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
32. Tutup Popup Changelog
33. Buka Global Settings > User > Detail milik user aktor, tab System Log
34. Verifikasi jumlah entri System Log user aktor bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
35. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active"
36. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD2" | Field "Status" | Old Value "Inactive" | New Value "Active"
37. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Alasan melewati sekitar 35 langkah (37 langkah, 14 di luar blok baca-log): seluruh TC satu topik pencatatan log di tiga surface dan berdiri sendiri (kegagalan satu TC tidak membuat TC lain kehilangan makna); langkah 7 sampai 20, 28 sampai 36 adalah blok baca-log berpola (buka surface, cari entri, `Verifikasi` kolom log) yang tidak dihitung menurut prinsip 13 bagian 3.
- Pembagian TC lintas spec: TC-FA-TDC-707, 708, dan 709 dijalankan dengan satu aksi Bulk Deactivate NB-3 dan NB-4, TC-FA-TDC-710 dan 711 dengan satu aksi Bulk Activate NB-OLD dan NB-OLD2 (aksi identik, tidak dapat diulang tanpa memulihkan status); baseline dicatat sekali per aksi (S-12). Pembacaan Activity Log untuk Bulk Activate (TC-FA-TDC-712) ada di spec 195.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Klausa "jumlah baris log sama dengan jumlah class yang berhasil diproses (2) dan tidak ada baris untuk class lain" ditulis sebagai selisih jumlah entri tepat 2 terhadap baseline per surface (asersi jumlah, bukan absence, prinsip 13g).
- Temuan untuk QA:
  - TC-FA-TDC-707 sampai 711 memakai "user aktor" tanpa nama, email, dan company; System Log dibaca pada Detail User aktor itu (R-06 butuh email bersuffix).
  - TC-FA-TDC-707 sampai 711 memakai class seed literal sebagai target aksi tulis; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - TC-FA-TDC-710 dan 711 memakai NB-OLD2 yang tidak ada di Example Data PRD; spec menambahkannya ke dataset fixture.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
