---
id: TC-FA-TDC-E2E-192-log-activate-deactivate-single-tiga-surface
title: "Pencatatan Log L-04 Activate dan Deactivate Single: Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-698
  - TC-FA-TDC-699
  - TC-FA-TDC-700
  - TC-FA-TDC-701
  - TC-FA-TDC-702
sourceRules: ["L-04", "§[F-FATDC-04] Activate Tax Depreciation Class#b2", "§4.1.1#r31", "§4.1.1#r26", "§4.1.1#r29", "§4.1.1#r30", "§8.2#p1", "§8.2#r1", "§8.3#p1", "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3"]
smoke: []
dependsOn: []
trace:
  "L-04": [6, 7, 11, 12, 15, 16, 23, 24, 28, 29]
  "§[F-FATDC-04] Activate Tax Depreciation Class#b2": 6
  "§4.1.1#r31": [7, 24]
  "§4.1.1#r26": [8, 25]
  "§4.1.1#r29": [8, 25]
  "§4.1.1#r30": [8, 25]
  "§8.2#p1": [11, 28]
  "§8.2#r1": [12, 29]
  "§8.3#p1": [15, 16]
  "§[F-FATDC-05] Deactivate Tax Depreciation Class#b3": 23
coverage:
  web: automated
---

# Pencatatan Log L-04 Activate dan Deactivate Single: Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Nama tampil, email, dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser sinkron (kendali jam di `suite.md`); kolom Date Changelog dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD (Inactive, Used By 0); NB-4 Active dengan Used By 0. Tabel memuat 8 baris pada satu halaman sehingga baris target dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` mengembalikan NB-OLD ke Inactive dan NB-4 ke Active lewat API (kemampuan disediakan tim FE/BE) serta mengembalikan sesi.

## Test Steps

### TC-FA-TDC-698, 699, 700: Activate class (L-04) tercatat di Changelog, System Log, dan Activity Log

1. Catat baseline jumlah entri Changelog, System Log user aktor, dan Activity Log (filter Object `Tax Depreciation Class`)
2. Klik toggle `Active` baris NB-OLD
3. Klik `[Activate]` pada dialog hingga status berhasil tersimpan
4. Catat waktu aksi
5. Klik ikon Changelog di toolbar
6. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
7. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
8. Verifikasi kolom Action, Old Value, dan New Value Changelog ditulis sebagai teks polos tanpa badge
9. Tutup Popup Changelog
10. Buka Global Settings > User > Detail milik user aktor, tab System Log
11. Verifikasi jumlah entri System Log user aktor bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
12. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active"
13. Buka Reports & Logs > Activity Log, tab `User Action`
14. Filter Object `Tax Depreciation Class`
15. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
16. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-OLD" | Field "Status" | Old Value "Inactive" | New Value "Active" | Modified By user aktor
17. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-701, 702: Deactivate class (L-04) tercatat di Changelog dan System Log

18. Catat baseline jumlah entri Changelog dan System Log user aktor
19. Klik toggle `Active` baris NB-4
20. Klik `[Deactivate]` pada dialog hingga status berhasil tersimpan
21. Catat waktu aksi
22. Klik ikon Changelog di toolbar
23. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
24. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Edit" | Class Code "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
25. Verifikasi kolom Action, Old Value, dan New Value Changelog ditulis sebagai teks polos tanpa badge
26. Tutup Popup Changelog
27. Buka Global Settings > User > Detail milik user aktor, tab System Log
28. Verifikasi jumlah entri System Log user aktor bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
29. Verifikasi System Log user aktor memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive"
30. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Pembagian TC lintas spec: TC-FA-TDC-698, 699, dan 700 (aksi Activate yang sama dibaca di tiga surface berbeda) dijalankan dengan satu aksi Activate NB-OLD karena aksi identik dan tidak dapat diulang tanpa memulihkan status; TC-FA-TDC-701 dan 702 dengan satu aksi Deactivate NB-4. Baseline dicatat sekali per aksi (S-12). Pembacaan Activity Log untuk Deactivate (TC-FA-TDC-703) ada di spec 193.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Klausa "tidak ada baris log lain untuk class lain dari aksi ini" ditulis sebagai selisih jumlah entri tepat 1 terhadap baseline per surface (asersi jumlah, bukan absence, prinsip 13g).
- Temuan untuk QA:
  - TC-FA-TDC-698 sampai 702 memakai "user aktor" tanpa nama, email, dan company; System Log dibaca pada Detail User aktor itu (R-06 butuh email bersuffix).
  - TC-FA-TDC-698 sampai 702 memakai class seed literal (NB-OLD, NB-4) sebagai target aksi tulis; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
