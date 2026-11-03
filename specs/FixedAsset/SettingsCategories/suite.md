---
name: Fixed Asset Settings Categories
id: suite-fixed-asset-settings-categories
description: Spec e2e turunan tc-settings-categories.md untuk Fixed Asset > Settings > Categories
executionOrder: 1.0
parallel: false
---

# Suite: Fixed Asset Settings Categories

Suite ini mencakup halaman Categories List (sidebar Category Tree, tabel utama dengan Search, Filter, Sort, Pagination, Setup Column, Download), Create Category dan Add Subcategory, Edit, Delete single dan Bulk Delete, Popup Detail Category dengan tabel Assets, Modal Changelog, Wizard dan Alert Category Consolidation (siklus Excess, Fallback T-0), pencatatan log di tiga surface (Changelog, System Log, Activity Log), sinkronisasi ke modul konsumen, Role Matrix, Guided Tooltip, tampilan mobile Android, batas plan dan System Limits, state tenant, konflik dua sesi, defense-in-depth, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah atau bergantung pada state global: plan dan status client, System Limits (Master Data Count Limit, Hierarchy Depth Limit, Selection Limit), downgrade terjadwal dan T-0, capability role, General Settings (format tanggal dan zona waktu), flag Guided Tooltip, dan pohon kategori bersama per client. Setiap spec menyiapkan dan membersihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control, Pre-setup #1, client CatMain, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env`). Spec yang aktor pertamanya akun atau client lain login akun itu di hook `before` spec, dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Fixed Asset > Settings > Categories (layar awal spec). Spec yang membuka layar sendiri (screening halaman pertama, Guided Tooltip, akun tanpa capability) menulis pengecualian itu di `## Prerequisites`.
- Jaring pengaman form dirty: hook `beforeEach` mengonfirmasi `beforeunload` dan menutup dialog `Unsaved Changes`; ini bukan pengganti langkah pemulihan eksplisit spec (S-09).
- Flag Guided Tooltip halaman Categories (`guided_tooltip_seen_*`): hook suite `before` men-set flag true untuk setiap akun aktor yang dipakai agar walkthrough tidak menutupi layar, dan `after` memulihkan nilai awal. Mekanisme disediakan tim FE/BE. Spec Guided Tooltip dan walkthrough dikecualikan dan menulis pengaturan flag-nya di `## Prerequisites` masing-masing.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI. Dipakai untuk Principal Automation (Pre-setup #11) dan pelaku kedua yang hanya memicu perubahan state. Kemampuan ini disediakan tim BE/FE; tiap spec yang memakainya memuat satu baris rujukan ke butir ini.
- Seed dan pemulihan lewat API: seed client Pre-setup (CatMain, CatMany, CatFresh, CatDeep, CatStarter, CatGrowth, CatCountLimit, CatDepthLimit, CatExcess, CatPreT0, CatPostT0, CatCode, CatSuspended, CatSelLimit, CatBig, CatThree, CatOver, CatCycle, CatPreT0Big, CatPreT0Susp) dan pemulihan plan, status client, System Limits, serta T-0 disediakan tim FE/BE; tiap spec merujuk butir ini dan hanya menulis fakta spesifik spec.
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom memulihkannya di hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]`. Kemampuan itu disediakan tim FE.

## Data bersama

- Client Pre-setup (data tabel Pre-setup #20-#49): pohon kategori tiap client dibaca; target tulis dan hapus memakai kategori milik spec bersuffix `{runId}-<NNN>` (S-06, S-12). Baris seed in-use tidak pernah menjadi target tulis kecuali TC mewajibkannya dan spec mencatatnya.
- Fixture `fixtures/settings-categories.json` belum ada dan disediakan tim FE; memuat identitas data Pre-setup yang dirujuk Prerequisites. Nama kunci ditetapkan tim FE.
- Data yang butuh fixture backend (aset Pre-setup #22, #40, #55-#59, Custom Field #56, 1.000 sampai 5.001 kategori, downgrade terjadwal dan T-0) ditulis di `## Prerequisites` spec sebagai "disediakan tim FE" tanpa endpoint karangan (S-13).
