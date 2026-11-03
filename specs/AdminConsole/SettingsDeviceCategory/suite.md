---
name: Admin Console Settings Device Category
id: suite-admin-console-settings-device-category
description: Spec e2e turunan tc-settings-device-category.md untuk Admin Console > Settings > Device > Category
executionOrder: 1.0
parallel: false
---

# Suite: Admin Console Settings Device Category

Suite ini mencakup Sidebar Category pada Settings > Device (sub-tab Device Name dan Device SKU): screening tree, pencarian tree, Expand/Collapse All, Floating Toggle Button, semantik pilihan node dan filter Category, aturan tampilan mobile Android, entity gate dan Role Matrix capability (Create, Update, Delete, Read), Add Subcategory, Edit Category, Delete Category (single dan family, termasuk blokir referensi Device Name), dialog Unsaved Changes, modal Changelog Category (Search, Filter, Sort, Setup Column, Pagination, Download), pencatatan di Changelog, System Log, dan Activity Log, sinkron dengan Device Name, Device SKU, Lifecycle Settings dan General Settings, defense-in-depth, konkurensi dua admin, serta ketahanan terhadap kegagalan server.

`parallel: false` karena pohon Category bersifat tunggal per entitas Principal dan seluruh spec memakai state bersama: pohon Category (Pre-setup #14) dan Device Name/Device SKU yang merujuknya, Changelog dan log audit permanen, Hierarchy Depth Limit (Lifecycle Settings), General Settings (Date Format, Time Format, Time Zone), state sidebar dan preferensi Setup Column per user. Setiap spec tetap menyiapkan dan memulihkan datanya sendiri lewat hook; pemulihan pohon ke keadaan Pre-setup #14 dijamin kemampuan fixture backend yang disediakan tim FE/BE dan dirujuk satu baris di `## Prerequisites` tiap spec. Sesi API aktor (login API password untuk akun yang sama dengan sesi UI) disediakan tim BE/FE dan dinyatakan di sini sekali.

## Hook dan kemampuan suite (dinyatakan sekali di sini)

Spec merujuk pernyataan berikut dengan satu baris di `## Prerequisites`. Seluruh kemampuan ini disediakan tim FE/BE.

- **Sesi API aktor:** login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga batas satu sesi web tidak terpengaruh dan sesi UI tidak diusir. Dipakai untuk seeding dan cleanup node Category dan Device Name bersufiks `{runId}`, serta untuk aktor kedua pada spec dua admin.
- **Pemulihan pohon Pre-setup #14 (fixture BE, hook `before` dan `after`):** pohon Category dipulihkan ke keadaan Pre-setup #14 sebelum dan sesudah spec; node milik spec dibuat lewat sesi API aktor dan dihapus dari anak ke induk di `after`.
- **Pemulihan riwayat Changelog Pre-setup #17 (fixture BE):** untuk spec modal Changelog (058 sampai 078) riwayat dipulihkan ke Pre-setup #17 sebelum dan sesudah spec, sehingga total entri absolut dapat diasersi (keputusan user 2026-11-02, pengecualian setara A-5). Spec pencatatan log (section 5) memakai selisih terhadap baseline yang dicatat di hook `before` setelah seeding.
- **Pemulihan state global yang diubah spec:** Hierarchy Depth Limit (Lifecycle Settings), General Settings (Date Format, Time Format, Time Zone), dan capability role dipulihkan di `after` oleh spec yang mengubahnya.
- **Preferensi UI per browser:** state sidebar (localStorage) dan preferensi Setup Column dihapus di browser pada hook `after` spec yang menyimpannya, bukan lewat `[Reset to Default]`.
- **Pembacaan baseline:** kemampuan membaca jumlah entri Changelog Category sebelum aksi pemicu pertama yang diasersi.
- **Konteks browser kedua:** spec dua admin membuka konteks browser kedua untuk aktor kedua dan menutupnya di akhir spec.
- **Pengecualian `beforeEach`:** hook `beforeEach` suite membuka Settings > Device > Device Name; spec yang akunnya ditolak di halaman itu (016, 017, 025) mengecualikan pembukaan tersebut dan menyatakannya di `## Prerequisites`.

