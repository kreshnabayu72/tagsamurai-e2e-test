---
id: TC-FA-TDC-E2E-193-log-deactivate-activity-log-dan-delete-single-tiga-surface
title: "Pencatatan Log L-04 Deactivate pada Activity Log dan L-05 Delete Single: Changelog, System Log, dan Activity Log"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-703
  - TC-FA-TDC-704
  - TC-FA-TDC-705
  - TC-FA-TDC-706
sourceRules: ["L-04", "§8.3#p1", "L-05", "§4.1.1#r31", "§4.1.1#r26", "§4.1.1#r29", "§4.1.1#r30", "§8.2#p1", "§8.2#r1"]
smoke: []
dependsOn: []
trace:
  "L-04": [6, 7]
  "§8.3#p1": [7, 25]
  "L-05": [15, 16, 20, 21, 24, 25]
  "§4.1.1#r31": 16
  "§4.1.1#r26": 17
  "§4.1.1#r29": 17
  "§4.1.1#r30": 17
  "§8.2#p1": 20
  "§8.2#r1": 21
coverage:
  web: automated
---

# Pencatatan Log L-04 Deactivate pada Activity Log dan L-05 Delete Single: Changelog, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Nama tampil, email, dan company uji tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam server dan jam browser sinkron (kendali jam di `suite.md`); kolom Date Changelog dibandingkan dengan waktu aksi yang dicatat sesudah aksi, toleransi satu menit, format tanggal mengikuti General Settings (S-12).
- Kemampuan teknis: baca jumlah entri Changelog, System Log, dan Activity Log lewat fixture BE (disediakan tim FE/BE; mekanismenya tidak disebut TC, S-13). Baseline dibaca tepat sebelum aksi pemicu tiap TC dan jumlah entri sesudah aksi dibandingkan terhadapnya (8b.10, S-12); entri baru dibaca pada baris teratas urutan default Date terbaru setelah selisih terbukti (S-14). System Log dibaca pada Detail User aktor; Activity Log pada `Reports & Logs > Activity Log`, tab `User Action`.
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup (dataset company khusus automation, di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND); NB-4 Active dengan Used By 0 dan tanpa Last Posted Tax Year. Tabel memuat 7 baris pada satu halaman sehingga baris target dibuka tanpa Search (8b.13, R-23).
- Pemulihan: hook `after` membuat ulang NB-4 sebagai Active lewat API (kemampuan disediakan tim FE/BE) dan mengembalikan sesi.

## Test Steps

### TC-FA-TDC-703: Deactivate class (L-04) tercatat di Activity Log

1. Catat baseline jumlah entri Activity Log (filter Object `Tax Depreciation Class`)
2. Klik toggle `Active` baris NB-4
3. Klik `[Deactivate]` pada dialog hingga status berhasil tersimpan
4. Buka Reports & Logs > Activity Log, tab `User Action`
5. Filter Object `Tax Depreciation Class`
6. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
7. Verifikasi Activity Log FAMS memuat satu baris: Action "Edit" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Status" | Old Value "Active" | New Value "Inactive" | Modified By user aktor
8. Buka Settings > Accounting > Tax Depreciation Class

### TC-FA-TDC-704, 705, 706: Delete class (L-05) tercatat di Changelog, System Log, dan Activity Log

9. Catat baseline jumlah entri Changelog, System Log user aktor, dan Activity Log (filter Object `Tax Depreciation Class`)
10. Klik tombol ⋯ baris NB-4
11. Pilih `Delete`
12. Klik `[Delete]` pada dialog hingga class berhasil dihapus
13. Catat waktu aksi
14. Klik ikon Changelog di toolbar
15. Verifikasi jumlah entri Changelog bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
16. Verifikasi Changelog memuat satu baris: Date sesuai waktu aksi (toleransi satu menit) | Action "Delete" | Class Code "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—" | Modified By berformat `[First Name] [Last Initial]` milik user aktor
17. Verifikasi kolom Action, Old Value, dan New Value Changelog ditulis sebagai teks polos tanpa badge
18. Tutup Popup Changelog
19. Buka Global Settings > User > Detail milik user aktor, tab System Log
20. Verifikasi jumlah entri System Log user aktor bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
21. Verifikasi System Log user aktor memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—"
22. Buka Reports & Logs > Activity Log, tab `User Action`
23. Filter Object `Tax Depreciation Class`
24. Verifikasi jumlah entri Activity Log bertambah tepat 1 dari baseline (satu baris; tidak ada baris log untuk class lain dari aksi ini)
25. Verifikasi Activity Log FAMS memuat satu baris: Action "Delete" | Object "Tax Depreciation Class" | Name "NB-4" | Field "Class Code" | Old Value "NB-4" | New Value "—" | Modified By user aktor
26. Buka Settings > Accounting > Tax Depreciation Class

## Notes

- Urutan: Deactivate NB-4 (TC-FA-TDC-703) lebih dulu, lalu Delete NB-4 (TC-FA-TDC-704, 705, 706) di akhir karena aksi menghapus data (S-10). NB-4 yang sudah Inactive tetap memenuhi precondition Delete TC-704 sampai 706 (Used By 0, tanpa Last Posted Tax Year).
- Pembagian TC lintas spec: TC-FA-TDC-704, 705, dan 706 (aksi Delete yang sama dibaca di tiga surface) dijalankan dengan satu aksi Delete NB-4; baseline dicatat sekali per aksi (S-12). Pembacaan Changelog dan System Log untuk Deactivate (TC-FA-TDC-701 dan 702) ada di spec 192.
- Langkah penghubung (S-03): mencatat baseline, mencatat waktu aksi, menutup Popup Changelog, dan membuka kembali Settings > Accounting > Tax Depreciation Class sesudah berpindah modul (S-14). Cara baca entri baru (S-14): setelah selisih jumlah terbukti, baris teratas urutan default Date terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya.
- Temuan untuk QA:
  - TC-FA-TDC-703 sampai 706 memakai "user aktor" tanpa nama, email, dan company; System Log dibaca pada Detail User aktor itu (R-06 butuh email bersuffix).
  - TC-FA-TDC-703 sampai 706 memakai class seed literal NB-4 sebagai target aksi tulis; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC; user pada surface admin dan log seharusnya diidentifikasi lewat email (R-06), TC hanya menyebut nama.
  - Filter produk FAMS pada Activity Log dan cara mencari entri di tiap surface tidak disebut TC; spec membaca baris teratas setelah selisih jumlah entri terbukti (S-14).
