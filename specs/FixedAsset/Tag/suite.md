---
name: Fixed Asset TAG
id: suite-fixed-asset-tag
description: Spec e2e turunan tc-tag.md untuk Fixed Asset > TAG
executionOrder: 6.0
parallel: false
---

# Suite: Fixed Asset TAG

Suite ini mencakup halaman Fixed Asset > TAG (menu TAG pada Fixed Asset) dengan dua tab: Paired dan To Be Returned. Tab Paired: kartu filter (Reported, Non-standard, Not Paired Yet), tabel grup T-TAG-01 dan Popup Detail Assets (tabel T-TAG-02 dengan Setup Column, Custom Field, Search, Filter, Sort, Pagination, Show), Popup TAG Log, Download CSV/XLSX, Modal Changelog Paired TAG, serta aksi Replace TAG (overlay scan, Dialog Replace TAG, Tag combined, Batch Replace), Pair TAG (satu aset dan sesi beberapa aset), dan Print QR. Tab To Be Returned: tabel, Receive TAG, Receive Manually, dan Modal Event Log. Suite juga mencakup dialog Report TAG, Decline Report, dan Cancel Report TAG, Guided Tooltip, Role Matrix per capability Manage asset & TAG (Read dan Update per group), scope group, pencatatan log (Changelog, Event Log, TAG Log, Activity Log, System Log), sinkron lintas modul (Asset Name, Asset Detail, Global, Disposal, transaksi Assignment, Borrow, Transfer, Disposal, Stock opname, Maintenance), notifikasi, request langsung dan izin dicabut di tengah aksi, state tenant (plan dan status entitas), waktu dan job pengingat, serta ketahanan terhadap kegagalan server.

`parallel: false` karena banyak spec mengubah state global: plan tier Client, status entitas (Suspended atau Expired), Selection Limit di Lifecycle Settings, jam server dan jam browser, capability role akun aktor, stok Tag per tipe di registri Global, status reader, serta flag Guided Tooltip. Tiap spec membuat dan membersihkan data miliknya sendiri lewat hook (aset, Tag, laporan, entri) dan tidak bergantung pada hasil spec lain. Spec yang mengubah state global memulihkannya di hook `after`, yang tetap jalan walau spec gagal di tengah. Nilai literal Pre-setup yang dirancang TC (Asset Name, Group, kode Tag, ID aset) tidak diberi suffix hanya bila TC membutuhkannya untuk asersi urutan atau jumlah dan seeding idempotent (dilewati bila sudah ada); data buatan spec bersuffix `{runId}-<NNN>`.

## Hook

Hook suite `beforeEach` membuka Fixed Asset > TAG sesudah akun aktor pertama login di hook `before` tiap spec. Spec yang akun aktor pertamanya tidak punya akses ke halaman TAG (Staff Auditor tanpa Manage asset & TAG, SA_NOTAG; spec 040, 085, 142-150, 158-163, 167-168, 282, 284-286, 290, 341, 350-351) tidak memakai navigasi `beforeEach` ke Fixed Asset > TAG dan membuka halaman itu (atau halaman yang diuji) di langkahnya sendiri. Hook suite juga menjadi jaring pengaman dengan mengonfirmasi dialog `beforeunload` dan menutup dialog `Unsaved Changes` bila masih terbuka; itu bukan pengganti langkah pemulihan form dirty di spec.

Flag Guided Tooltip halaman ini (`guided_tooltip_seen_fa-tag`): hook suite `before` menyetel flag itu true untuk setiap akun aktor yang dipakai suite (nilai awal dicatat) dan hook suite `after` memulihkannya. Spec 013-015 dan 019 menguji flag itu sendiri dan menulis pengaturan flag di `## Prerequisites` masing-masing; tiap spec lain memuat satu baris rujukan ke pernyataan ini.

Pemulihan konfigurasi kolom Setup Column yang disimpan spec: hook `after` spec berikut menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`: 049, 181-190, 192-196, 198-201, 203-206, 212-226, 249-251, 260-263, 269-270, 366-367.

Sesi API aktor: login API (password) untuk akun yang sama dengan sesi UI memakai token yang tidak dihitung sebagai sesi web, sehingga batas satu sesi web tidak terpengaruh dan sesi UI tidak diusir. Kemampuan itu disediakan tim BE/FE; `## Prerequisites` spec merujuknya dengan satu baris. Dipakai sebagai pelaku kedua (mengubah state tanpa asersi di sesinya) oleh spec 038, 040, 094, 100, 113, 133-134, 147, 154, 160, 168, 264, 267, 286-291, 295, 297, 300-301, 327-328, 346, 349-350, 352, 374-376, 381, 385.

## State global yang dipulihkan hook `after`

- Plan tier Client dan status entitas (Active, Suspended, Expired): spec 326, 345-350, 357, 375, 384-385.
- Selection Limit di Lifecycle Settings: spec 264, 267.
- Jam server dan jam browser: spec 356.
- Capability role akun aktor yang dicabut atau diubah: spec 327-328, 352.
- Stok Tag per tipe di registri Global, status Tag pengganti, dan status reader.
- Flag Guided Tooltip (lihat di atas) dan preferensi kolom Setup Column (lihat di atas).

## Kemampuan teknis yang dibutuhkan (disediakan tim FE/BE)

Mekanisme dan endpoint tidak didefinisikan di TC maupun PRD yang dibaca tahap ini; modul tidak punya `openapi.yaml` maupun `low-level-design.md`. Spec menulisnya sebagai kemampuan dan tahap script melengkapinya (S-13).

- Simulator reader RFID/NFC USB (pindai kode, driver belum terpasang, reader tidak merespons, lebih dari satu reader, belum sinkron, menunggu approval, reader terputus): dipakai sebagai langkah rutin oleh spec yang memindai Tag; spec 358-365 menguji kondisi reader itu sendiri.
- Seed dan pemulihan idempotent lewat fixture backend: aset, Tag per status registri (Available, Reserved, Retired, Damaged/Missing, To be Returned, Waiting for Approval, Paired), laporan Tag, entri Changelog dan Event Log, task Existence Audit atau transaksi Borrow, stok per tipe, dan Tag combined.
- Intercept jaringan (5xx, timeout, respons ditunda) di atas backend nyata; layanan Global tidak terjangkau (kelas b: spec 331-341, 354).
- Klien HTTP untuk request langsung ke server (kelas a: spec 323, 325-326, 329).
- Pembaca berkas unduhan CSV/XLSX dan dialog cetak browser (Print QR).
- Pengaturan jam server dan jam browser bersama, job latar pengingat, dan penanganan dialog `beforeunload` (spec 372-373).
- Perubahan plan Client, status entitas, Selection Limit, capability role, dan TAG Type Asset Name oleh pelaku kedua (sesi API).

## Mode

Semua spec `Mode: FE+BE` terhadap backend nyata. Kegagalan 5xx, timeout, dan respons ditunda memakai `Spectra.intercept` parsial di atas backend nyata (bagian 6 konvensi); tidak ada spec `Mode: mock`.

## Kredensial

Password aktor lewat `Spectra.env`, satu nama env satu arti. Nama usulan: Total Control `FA_TC_PASSWORD`, akun lain `FA_TAG_<KODE>_PASSWORD` (kode di rencana, bagian Akun aktor). Nama baru perlu didaftarkan di `spectra.config.ts` dan `.env.example` oleh tim FE. Akun di luar Tabel Pre-setup TC ditulis "disediakan tim FE" (pengguna Budi S., akun admin untuk plan, status entitas, Selection Limit, dan capability).
