---
id: TC-FA-TDC-E2E-195-log-bulk-activate-activity-log-dan-bulk-delete-satu-kejadian-per-class
title: "Pencatatan Log L-04 Bulk Activate pada Activity Log dan L-05 Bulk Delete: Satu Kejadian per Class di Tiga Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-712
  - TC-FA-TDC-713
  - TC-FA-TDC-714
  - TC-FA-TDC-715
coverage:
  web: automated
---

# Pencatatan Log L-04 Bulk Activate pada Activity Log dan L-05 Bulk Delete: Satu Kejadian per Class di Tiga Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Nama tampil, email, dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser sinkron (kendali jam di `suite.md`); kolom Date Changelog dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD dan NB-OLD2 (Inactive, Used By 0); NB-3 dan NB-4 dengan Used By 0 tanpa Last Posted Tax Year. Tabel memuat 9 baris pada satu halaman sehingga baris target dicentang tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` mengembalikan NB-OLD dan NB-OLD2 ke Inactive serta membuat ulang NB-3 dan NB-4 lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan sesi.

## Test Steps

### TC-FA-TDC-712: Bulk Activate (L-04) tercatat satu kejadian per class di Activity Log

1. Catat baseline jumlah entri Activity Log (filter Object `Tax Depreciation Class`)
2. Centang baris NB-OLD
3. Centang baris NB-OLD2
4. Klik `Activate` pada Bulk Action Bar
5. Klik `[Activate]` pada dialog hingga status berhasil tersimpan
6. Buka Reports & Logs > Activity Log, tab `User Action`
7. Filter Object `Tax Depreciation Class`
8. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
9. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By user aktor
10. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD2" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By user aktor
11. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-713, 714, 715: Bulk Delete (L-05) tercatat satu kejadian per class di Changelog, System Log, dan Activity Log

12. Catat baseline jumlah entri Changelog, System Log user aktor, dan Activity Log (filter Object `Tax Depreciation Class`)
13. Centang baris NB-3
14. Centang baris NB-4
15. Klik `Delete` pada Bulk Action Bar
16. Klik `[Delete]` pada dialog hingga class berhasil dihapus
17. Catat waktu aksi
18. Klik ikon Changelog di toolbar
19. Verifikasi jumlah entri Changelog bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
20. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Delete" | Class Code "NB-3" | Field "Class Code" | Old Value "NB-3" | New Value "—" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
21. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Delete" | Class Code "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
22. Tutup Popup Changelog
23. Buka Global Settings > User > Detail milik user aktor, tab System Log
24. Verifikasi jumlah entri System Log user aktor bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
25. Verifikasi System Log user aktor memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-3" | Field "Class Code" | Old Value "NB-3" | New Value "—"
26. Verifikasi System Log user aktor memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—"
27. Buka Reports & Logs > Activity Log, tab `User Action`
28. Filter Object `Tax Depreciation Class`
29. Verifikasi jumlah entri Activity Log bertambah tepat 2 dari baseline (jumlah baris log sama dengan jumlah class yang berhasil diproses (2); tidak ada baris untuk class lain)
30. Verifikasi Activity Log FAMS memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-3" | Field "Class Code" | Old Value "NB-3" | New Value "—" | Modified By user aktor
31. Verifikasi Activity Log FAMS memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—" | Modified By user aktor
32. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Urutan: Bulk Activate (TC-FA-TDC-712) lebih dulu, lalu Bulk Delete (TC-FA-TDC-713, 714, 715) di akhir karena aksi menghapus data (S-10). TC-FA-TDC-713 sampai 715 dijalankan dengan satu aksi Bulk Delete yang sama (aksi identik, tidak dapat diulang); baseline dicatat sekali per aksi (S-12). Pembacaan Changelog dan System Log untuk Bulk Activate (TC-FA-TDC-710 dan 711) ada di spec 194.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Klausa "jumlah baris log sama dengan jumlah class yang berhasil diproses (2) dan tidak ada baris untuk class lain" ditulis sebagai selisih jumlah entri tepat 2 terhadap baseline per surface (asersi jumlah, bukan absence, prinsip 13g).
- Temuan untuk QA:
  - TC-FA-TDC-712 sampai 715 memakai "user aktor" tanpa nama, email, dan company; System Log dibaca pada Detail User aktor itu (R-06 butuh email bersuffix).
  - TC-FA-TDC-712 sampai 715 memakai class seed literal sebagai target aksi tulis; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - TC-FA-TDC-712 memakai NB-OLD2 yang tidak ada di Example Data PRD; spec menambahkannya ke dataset fixture.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
