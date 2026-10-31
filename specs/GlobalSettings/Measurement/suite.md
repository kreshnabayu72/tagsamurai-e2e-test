---
name: Global Settings Measurement
id: suite-global-settings-measurement
description: Spec e2e turunan tc-measurement.md untuk Global Settings > Master Reference > Measurement
executionOrder: 1.0
parallel: false
---

# Suite: Global Settings Measurement

Suite ini mencakup tab Measurement pada Master Reference: tabel (Search, Filter, Sort, Pagination, Setup Column, Download), Create, Edit, Delete single dan Bulk Delete, Modal Changelog, Modal Unit Detail (Item Type List dan Device Name List), Role Matrix, Guided Tooltip, pencatatan log di tiga surface (Changelog, System Log, Activity Log), sinkronisasi ke modul konsumen (Fixed Asset dan Device Name Admin Console), batas Master Data Count Limit dan Selection Limit, state tenant, konflik dua admin, defense-in-depth, tampilan mobile, serta ketahanan terhadap kegagalan server.

`parallel: false` karena spec mengubah state global (plan dan status Client, format tanggal dan zona waktu General Settings, capability role, flag Guided Tooltip, data Client Limit) dan men-seed Population D-01 dengan nama literal. Setiap spec menyiapkan dan membersihkan datanya sendiri lewat hook; urutan antar-spec tidak diasumsikan dan tidak ada spec yang bergantung pada hasil spec lain.

## Hook suite

- `before`: login akun aktor default suite (Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`). Spec yang aktor pertamanya akun lain login akun itu di hook `before` spec dan hook `after` spec mengembalikan sesi ke akun default.
- `beforeEach`: tutup dialog yang terbuka dan buka Global Settings > Master Reference > Measurement (layar awal spec). Spec 001, 011, dan 014 dikecualikan dari pembukaan layar oleh hook ini. Spec 001 membuka Master Reference sendiri dari sidebar di langkah 1 karena yang diuji adalah tab default Brand saat pertama masuk halaman (TC-GS-UOM-2); spec 011 membuka layar sendiri karena pembukaan layar dengan flag Guided Tooltip yang sudah diatur adalah objek uji; akun aktor spec 014 (Tanpa Capability) tidak dapat membuka tab Measurement dan layar awalnya adalah Global Settings. Tiap spec yang dikecualikan menulis pengecualian itu di `## Prerequisites`-nya.
- Flag Guided Tooltip halaman Measurement (`guided_tooltip_seen_gs-measurement`): hook suite `before` men-set flag itu true untuk setiap akun aktor yang dipakai spec dalam suite (nilai awal tiap akun dicatat) supaya walkthrough otomatis tidak menutupi layar, dan hook suite `after` memulihkan nilai awal. Mekanisme penyetelan flag disediakan tim FE/BE. Tab default saat Master Reference dibuka adalah Brand, sehingga hook suite juga menyetel flag `guided_tooltip_seen_gs-brand` ke true dengan cara dan pemulihan yang sama. Spec 010 dan 011 menguji flag Measurement itu sendiri sehingga dikecualikan dari penyetelan flag Measurement dan menulis pengaturan flag-nya di `## Prerequisites` masing-masing; tiap spec lain memuat satu baris rujukan ke pernyataan ini.
- Sesi API aktor: login API (password) memakai token yang tidak dihitung sebagai sesi web, termasuk untuk akun yang sama dengan sesi UI: batas satu sesi web tidak terpengaruh dan sesi UI tidak diusir. Kemampuan ini disediakan tim BE/FE; tiap spec yang memakai sesi API aktor memuat satu baris rujukan ke butir ini dan hanya menambahkan fakta spesifik spec (akun, env var, operasi).
- Pemulihan Setup Column: spec yang menyimpan konfigurasi kolom lewat Setup Column (042, 043, 051, 052, 056, 057) memulihkannya di hook `after` dengan menghapus preferensi kolom di browser, bukan lewat `[Reset to Default]`. Kemampuan itu disediakan tim FE dan ditulis di `## Prerequisites` tiap spec.

## Data bersama (Population dan Pre-setup)

- Population D-01 (12 unit, nama literal tanpa suffix `{runId}`): Centimeter, Foot, Gallon, Inch, Milliliter, Millimeter, Ounce, Pound, Roll, Set, Sheet, Ton. Dibuat oleh spec 017. Seeding idempotent: hook `before` spec yang membutuhkan Population memeriksa keberadaannya lewat API dan hanya membuat unit yang belum ada. Hook suite membersihkan sisa unit non-Population hasil run sebelumnya (mis. carat, Hectare, Kilogram Force, Barrel) agar tabel Client A berisi tepat 20 unit (8 Pre-setup + 12 Population) saat spec membaca baseline 20 unit.
- Pre-setup Client A (data baca): Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces. Baris ini hanya dibaca; target tulis dan hapus memakai unit milik spec bersuffix `{runId}-<NNN>` (S-06, S-12). Baris in-use (Box, Dozen, Gram, Kilogram, Pieces) tidak pernah menjadi target tulis.
- Data yang butuh fixture backend (referensi Supply/SAMS, Device Name, 1250 referensi, Tote dengan Crate, relasi nonaktif atau Recycle Bin) ditulis di `## Prerequisites` spec sebagai "disediakan tim FE" tanpa endpoint karangan (S-13).
- Spec `Mode: mock`: respons daftar Brand (tab default saat Master Reference dibuka) dan API pendukung halaman Master Reference (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE; tiap spec mock memuat satu baris rujukan ke butir ini.
- `fixtures/measurement.json` belum ada dan disediakan tim FE; fixture itu memuat data Pre-setup (Client A, Principal, Distributor) dan Population D-01 yang dirujuk Prerequisites tiap spec. Nama kunci ditetapkan tim FE.
