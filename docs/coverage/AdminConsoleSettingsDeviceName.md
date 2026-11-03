# Coverage E2E — Admin Console > Settings > Device > Device Name

Sumber: `admin-console/settings-device-name/TestCases/tc-settings-device-name.md` (662 ID `TC-AC-DN-1`–`662`). Suite: `specs/AdminConsole/SettingsDeviceName/`. Prefix: `AC` + `DN` (`TC-AC-DN-E2E-*`). Status semua spec: `draft`, belum ada script. `tc-settings-device-name-backend.md` tidak dipakai untuk suite ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 662 TC masuk 181 spec; tidak ada TC hanya-BE yang dikeluarkan. Setiap TC terpetakan ke tepat satu spec. TC kelas K-1 (Expected berupa respons API) tetap masuk sebagai spec FE+BE.

## TC hanya-BE (tidak masuk spec)

Tidak ada.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-DN-E2E-001-screening-halaman-list | Screening Halaman Device Name List: Header, Body, Footer, Selector, Breadcrumb, Sub-tab, Row Action | FE+BE | 33 | 1, 2, 3, 4, 8 |
| TC-AC-DN-E2E-002-tooltip-dan-hover-list | Tooltip Toolbar, Header Actions, Hover Device Name, dan Klik Area Baris pada List | FE+BE | 21 | 5, 6, 7 |
| TC-AC-DN-E2E-003-kolom-category-badge | Kolom Category: Urutan Default, Badge, Hover Jalur Penuh, Pemotongan 25 Karakter, Fokus Keyboard | FE+BE | 19 | 9, 10, 11, 12, 597 |
| TC-AC-DN-E2E-004-kolom-brand-model-chip | Kolom Brand dan Model/Type: Chip, +N more, Em Dash, Tooltip Fokus Keyboard | FE+BE | 22 | 13, 14, 15, 16, 642 |
| TC-AC-DN-E2E-005-chip-panjang-dan-popup-more-bagian-1 | Chip Panjang, Brand/Model Turunan SKU, dan Popup +N more (Brand, Model/Type) | FE+BE | 29 | 17, 23, 267, 268 |
| TC-AC-DN-E2E-006-popup-more-keyboard-dan-tutup | Popup +N more: Keyboard, Klik Luar, Hover, dan Daftar Polos | FE+BE | 32 | 269, 270, 271, 596 |
| TC-AC-DN-E2E-007-kolom-measurement-last-modified-dan-header | Kolom Measurement, Last Modified, Nama 120 Karakter, Header Layar Sempit, Tanpa Agregat Stok | FE+BE | 25 | 18, 19, 20, 21, 22 |
| TC-AC-DN-E2E-008-loading-dan-empty-state-list | Loading State dan Empty State Search/Filter/Sidebar pada List | FE+BE | 33 | 24, 26, 27, 28 |
| TC-AC-DN-E2E-009-principal-tanpa-riwayat | Principal Tanpa Riwayat: List Kosong, Opsi Filter Kosong, Changelog Tanpa Entri | FE+BE | 22 | 25, 294, 403, 449 |
| TC-AC-DN-E2E-010-transisi-empty-state-sidebar | Transisi Empty State Sidebar saat Device Name Terakhir pada Node Dibuat dan Dihapus | FE+BE | 22 | 623, 622 |
| TC-AC-DN-E2E-011-sidebar-default-collapse-dan-viewport | Category Sidebar: Default Terbuka, Collapse, Open Kembali, Persistensi per User, dan Viewport 1279/1280 px | FE+BE | 39 | 31, 32, 33, 34, 628 |
| TC-AC-DN-E2E-012-filter-sidebar-category-rekursif | Filter Category Sidebar: Leaf, Parent, Multi-pilih, Hapus Pilihan, dan Filter Panel Tanpa Field Category | FE+BE | 32 | 35, 36, 37, 38, 39, 40, 41 |
| TC-AC-DN-E2E-013-sidebar-irisan-dengan-search-filter | Category Sidebar sebagai Irisan dengan Search dan Filter Panel, Reset Halaman, dan Konsistensi Node | FE+BE | 33 | 42, 43, 46, 598 |
| TC-AC-DN-E2E-014-sidebar-persistensi-state | Pilihan Node Sidebar: Refresh, Sub-tab, dan Setelah Edit | FE+BE | 32 | 44, 45, 629 |
| TC-AC-DN-E2E-015-guided-tooltip-konten-dan-kunjungan-pertama | Guided Tooltip: Konten Tiap Step dan Kunjungan Pertama | FE+BE | 35 | 644, 645 |
| TC-AC-DN-E2E-016-guided-tooltip-navigasi-interupsi-aksesibilitas | Guided Tooltip: Siklus Navigasi, Interupsi, dan Aksesibilitas Keyboard | FE+BE | 46 | 647, 648, 649 |
| TC-AC-DN-E2E-017-guided-tooltip-lewati-step-sidebar | Guided Tooltip: Step 2 Dilewati saat Sidebar Tertutup atau Tersembunyi pada 1279 px | FE+BE | 44 | 653, 654 |
| TC-AC-DN-E2E-018-mobile-card-list-dan-seleksi-massal | Mobile: Card List, Long Press, dan Floating Bottom Bulk Bar | FE+BE | 17 | 47, 48, 49 |
| TC-AC-DN-E2E-019-mobile-bulk-bar-dan-detail | Mobile: Ketuk Card pada Mode Seleksi, Tutup Bulk Bar, Nol Terpilih, dan Detail Bottom Sheet | FE+BE | 25 | 50, 51, 52, 53 |
| TC-AC-DN-E2E-020-mobile-toolbar-filter-sidebar | Mobile: Toolbar, Changelog, Filter Bottom Sheet, dan Category Sidebar | FE+BE | 40 | 54, 55, 56, 57 |
| TC-AC-DN-E2E-021-mobile-popup-bottom-sheet | Mobile: Popup Create, Edit, Changelog, Delete, Blok, dan Unsaved Changes sebagai Bottom Sheet | FE+BE | 36 | 599, 619, 620 |
| TC-AC-DN-E2E-022-sidebar-dan-subtab-direset-menu-tab-baru-login | Sidebar dan Sub-tab: Reset oleh Klik Ulang Menu, Tab Browser Baru, dan Login Ulang | FE+BE | 23 | 626 |
| TC-AC-DN-E2E-023-guided-tooltip-tombol-bantuan | Guided Tooltip: Tombol [?] di Sebelah Kanan Breadcrumb Memulai Ulang Walkthrough | FE+BE | 7 | 646 |
| TC-AC-DN-E2E-024-role-matrix-visibilitas-menu-per-entitas | Role Matrix: Visibilitas Menu Device Name per Entitas dan Capability, serta Dropdown Distributor | FE+BE | 44 | 58, 62, 60, 61, 59, 526 |
| TC-AC-DN-E2E-025-role-matrix-akses-url-langsung | Role Matrix: Akses URL Langsung Halaman Device Name per Entitas dan Role | FE+BE | 36 | 600, 601, 257, 549, 548, 547 |
| TC-AC-DN-E2E-026-role-matrix-visibilitas-elemen-per-capability | Role Matrix: Visibilitas Kontrol List per Capability (Total Control, Read Only, Create-Only) | FE+BE | 34 | 64, 65, 63, 66 |
| TC-AC-DN-E2E-027-role-matrix-positif-create-edit-per-capability | Role Matrix Positif: Create dan Edit Berhasil per Capability | FE+BE | 43 | 70, 107, 71, 161 |
| TC-AC-DN-E2E-028-role-matrix-positif-delete-per-capability | Role Matrix Positif: Delete dan Bulk Delete Berhasil oleh Delete-Only | FE+BE | 22 | 72, 201, 238 |
| TC-AC-DN-E2E-029-defense-request-baca-tulis-distributor-partner | Defense-in-Depth: Request Baca dan Tulis oleh Distributor dan Partner Ditolak Server | FE+BE | 51 | 539, 540, 541, 542, 627 |
| TC-AC-DN-E2E-030-defense-request-baca-tulis-client-dan-dropdown-read-only | Defense-in-Depth: Request Baca dan Tulis oleh Client Ditolak Server, serta Dropdown Read-only Client | FE+BE | 39 | 543, 544, 655 |
| TC-AC-DN-E2E-031-defense-request-tulis-per-capability-bagian-1 | Defense-in-Depth: Request Tulis Ditolak untuk Read Only dan Create-Only | FE+BE | 36 | 550, 551, 552, 553, 554 |
| TC-AC-DN-E2E-032-defense-request-tulis-per-capability-bagian-2 | Defense-in-Depth: Request Tulis Ditolak untuk Update-Only dan Delete-Only | FE+BE | 30 | 555, 556, 557, 558 |
| TC-AC-DN-E2E-033-defense-xss-dan-search-literal | Defense-in-Depth: Nama berisi Tag Script Dirender sebagai Teks dan Search Karakter Khusus Literal | FE+BE | 28 | 561, 562, 563, 564 |
| TC-AC-DN-E2E-034-defense-validasi-dan-guard-server | Defense-in-Depth: Server Menolak Emoji, Duplikat, dan Delete/Edit yang Melanggar Guard | FE+BE | 37 | 565, 566, 567, 568, 569, 570 |
| TC-AC-DN-E2E-035-resilience-gagal-memuat | Resilience: Gagal Memuat List, Usage by Company, dan Changelog, serta Try Again | FE+BE | 33 | 29, 30, 618, 404 |
| TC-AC-DN-E2E-036-resilience-create-gagal | Resilience: Create Gagal karena Error Server, Retry, dan Timeout | FE+BE | 42 | 112, 113, 114 |
| TC-AC-DN-E2E-037-resilience-edit-gagal-dan-retry-timeout | Resilience: Edit Gagal, Timeout, dan Retry Create Setelah Timeout Tidak Membuat Ganda | FE+BE | 42 | 167, 168, 578 |
| TC-AC-DN-E2E-038-resilience-delete-gagal | Resilience: Delete Single Gagal, Retry, dan Tanpa Respons | FE+BE | 27 | 196, 198, 197 |
| TC-AC-DN-E2E-039-resilience-bulk-delete-dan-download-gagal | Resilience: Bulk Delete Gagal/Tanpa Respons dan Download List/Changelog Gagal | FE+BE | 47 | 235, 236, 368, 487 |
| TC-AC-DN-E2E-040-role-matrix-visibilitas-elemen-per-capability-bagian-2 | Role Matrix: Visibilitas Kontrol List per Capability (Update-Only, Delete-Only, Full CRUD) | FE+BE | 35 | 67, 68, 69 |
| TC-AC-DN-E2E-041-defense-request-baca-tulis-tanpa-capability | Defense-in-Depth: Request Baca dan Tulis oleh Principal Tanpa Capability Ditolak Server | FE+BE | 24 | 545, 546 |
| TC-AC-DN-E2E-042-create-screening-dan-dropdown | Create Device Name: Screening Popup dan Dropdown Measurement/Category | FE+BE | 37 | 73, 74, 586, 75, 76, 77, 78 |
| TC-AC-DN-E2E-043-create-validasi-wajib-diisi | Create Device Name: Validasi Wajib Diisi (Device Name, Measurement, Category) | FE+BE | 40 | 87, 88, 101, 102, 103 |
| TC-AC-DN-E2E-044-create-validasi-batas-karakter-dan-paste | Create Device Name: Batas 120 Karakter (121 Karakter dan Paste 121) dan Paste Dua Baris | FE+BE | 22 | 91, 583, 584 |
| TC-AC-DN-E2E-045-create-validasi-emoji | Create Device Name: Emoji Diketik, Ditempel, dan Lolos Filter FE | FE+BE | 20 | 97, 98, 99 |
| TC-AC-DN-E2E-046-create-validasi-duplikat | Create Device Name: Error Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Duplikat setelah Create Berurutan | FE+BE | 37 | 93, 94, 95, 577 |
| TC-AC-DN-E2E-047-create-berhasil-variasi-category-measurement | Create Device Name Berhasil: Variasi Category dan Measurement | FE+BE | 32 | 79, 80, 81 |
| TC-AC-DN-E2E-048-create-berhasil-trim-batas-dan-simbol | Create Device Name Berhasil: Trim Spasi, 120 Karakter, Spasi Melewati Batas, dan Simbol Umum | FE+BE | 37 | 89, 90, 92, 100 |
| TC-AC-DN-E2E-049-create-checkbox-stay-on-form | Create Device Name: Checkbox Stay on this form, Form Dikosongkan, dan Create Dua Device Name Berurutan | FE+BE | 36 | 84, 85, 86 |
| TC-AC-DN-E2E-050-create-toast-baris-baru-dan-klik-ganda | Create Device Name: Toast 4 Detik, Baris Baru pada List, dan Klik Ganda Submit | FE+BE | 26 | 82, 83, 111 |
| TC-AC-DN-E2E-051-create-clear-field-dan-saving-state | Create Device Name: Clear Field dan Saving State | FE+BE | 30 | 108, 109 |
| TC-AC-DN-E2E-052-create-tutup-form-dirty-dan-unsaved-changes | Create Device Name: Menutup Form Dirty, Dialog Unsaved Changes (Cancel, Leave, Esc) | FE+BE | 26 | 117, 121, 118, 119, 120 |
| TC-AC-DN-E2E-053-create-tutup-form-bersih-backdrop-dan-reload | Create Device Name: Backdrop, Navigasi In-app, Reload, dan Menutup Form Bersih | FE+BE | 32 | 123, 124, 125, 115, 116, 122, 126 |
| TC-AC-DN-E2E-054-create-hover-tombol-dan-aksesibilitas-popup | Create Device Name: Hover Tombol dan Aksesibilitas Popup | FE+BE | 15 | 110, 127 |
| TC-AC-DN-E2E-055-create-berhasil-satu-karakter | Create Device Name Berhasil: Satu Karakter | FE+BE | 11 | 585 |
| TC-AC-DN-E2E-056-edit-screening-dan-ubah-satu-field | Edit Device Name: Screening Popup dan Ubah Nama, Measurement, Category, serta Rename Memindahkan Baris | FE+BE | 40 | 128, 129, 130, 131, 587 |
| TC-AC-DN-E2E-057-edit-ubah-banyak-field-dan-device-name-ber-sku | Edit Device Name: Ubah Tiga Field, Device Name ber-SKU (Nama, Measurement, Category), dan Category node Induk | FE+BE | 44 | 132, 133, 588, 157, 158 |
| TC-AC-DN-E2E-058-edit-no-op-kapitalisasi-spasi-dan-aksesibilitas | Edit Device Name: Save Tanpa Perubahan, Hanya Huruf Besar-Kecil atau Spasi Ujung, dan Aksesibilitas Popup | FE+BE | 33 | 134, 135, 136, 180 |
| TC-AC-DN-E2E-059-edit-validasi-wajib-diisi | Edit Device Name: Validasi Wajib Diisi dan Klik Root Hardware/TAG | FE+BE | 41 | 137, 138, 152, 153, 154 |
| TC-AC-DN-E2E-060-edit-batas-karakter-trim | Edit Device Name: Trim, 120 dan 121 Karakter, serta Spasi Melewati Batas | FE+BE | 28 | 139, 140, 141, 142 |
| TC-AC-DN-E2E-061-edit-emoji-dan-simbol | Edit Device Name: Emoji Diketik, Ditempel, Lolos Filter FE, dan Simbol Umum | FE+BE | 20 | 148, 149, 150, 151 |
| TC-AC-DN-E2E-062-edit-validasi-duplikat | Edit Device Name: Duplikat (Persis, Huruf Besar-Kecil, Spasi Ujung) dan Nama Sendiri Bukan Duplikat | FE+BE | 24 | 143, 144, 145, 146 |
| TC-AC-DN-E2E-063-edit-clear-field-saving-hover-klik-ganda | Edit Device Name: Clear Field, Saving State, Hover Tombol, dan Klik Ganda Save | FE+BE | 38 | 162, 163, 164, 165, 166 |
| TC-AC-DN-E2E-064-edit-tutup-form-dirty-unsaved-changes | Edit Device Name: Menutup Form Dirty dan Dialog Unsaved Changes | FE+BE | 22 | 171, 172, 173, 174 |
| TC-AC-DN-E2E-065-edit-revert-esc-category-backdrop-reload | Edit Device Name: Kembali ke Nilai Awal, Esc setelah Ubah Category, Backdrop, Navigasi In-app, dan Reload | FE+BE | 35 | 175, 589, 590, 177, 178, 179 |
| TC-AC-DN-E2E-066-edit-tutup-form-bersih | Edit Device Name: Menutup Form Edit yang Belum Diubah (Icon Close, Esc, Backdrop) | FE+BE | 14 | 169, 170, 176 |
| TC-AC-DN-E2E-069-delete-screening-dialog-dan-cancel | Delete Device Name: Screening Row Action dan Dialog Konfirmasi, Backdrop, Esc, dan Cancel | FE+BE | 24 | 181, 182, 183, 184, 185 |
| TC-AC-DN-E2E-070-delete-berhasil-loading-klik-ganda-dan-toast | Delete Device Name: Loading, Klik Ganda, dan Toast 4 Detik | FE+BE | 28 | 199, 200, 187 |
| TC-AC-DN-E2E-071-delete-blok-karena-sku | Delete Device Name Diblok karena SKU: Dialog Blok, Tutup, SKU Tunggal, dan Stok Nol | FE+BE | 36 | 188, 189, 192, 591 |
| TC-AC-DN-E2E-072-delete-blok-karena-unit-byo-bagian-1 | Delete Device Name Diblok karena Unit BYO: Hardware, TAG, dan Gabungan | FE+BE | 30 | 190, 191, 609 |
| TC-AC-DN-E2E-073-delete-blok-karena-unit-byo-bagian-2 | Delete Device Name Diblok: Unit BYO Lintas Company dan SKU Milik Distributor | FE+BE | 24 | 610, 611 |
| TC-AC-DN-E2E-074-fokus-dialog-delete-blok-detail-dan-bulk | Aksesibilitas Dialog: Fokus Terkunci dan Label Aksi Eksplisit (Delete, Blok, Detail, dan Unsaved Changes) | FE+BE | 27 | 621 |
| TC-AC-DN-E2E-075-bulk-action-bar-dan-seleksi-dasar | Bulk Action Bar: Screening, Overlay Aksi, Counter, Tutup, dan Indeterminate | FE+BE | 25 | 202, 203, 204, 205, 208 |
| TC-AC-DN-E2E-076-bulk-seleksi-dipertahankan | Bulk Delete: Checkbox Header dan Seleksi Dipertahankan saat Halaman, Search, Filter, dan Sort Berubah | FE+BE | 30 | 206, 207, 213, 214, 215, 216 |
| TC-AC-DN-E2E-077-bulk-select-all-lintas-halaman | Bulk Delete: Select All dan Unselect All Lintas Halaman | FE+BE | 24 | 209, 211, 210, 212 |
| TC-AC-DN-E2E-078-bulk-selection-limit | Bulk Delete: Selection Limit (Checkbox Disabled dan Select All Dipotong) | FE+BE | 27 | 537, 217, 218 |
| TC-AC-DN-E2E-079-bulk-dialog-konfirmasi-bersih-cancel | Bulk Delete: Dialog Konfirmasi Item Bersih, Cancel, Esc, dan Backdrop | FE+BE | 24 | 219, 220, 221, 222 |
| TC-AC-DN-E2E-080-bulk-delete-bersih-berhasil | Bulk Delete Item Bersih: Satu Baris, Klik Ganda, Seleksi di Luar Search, dan Berhasil | FE+BE | 40 | 224, 237, 239, 223 |
| TC-AC-DN-E2E-081-bulk-delete-campuran-dialog-dua-kelompok | Bulk Delete Campuran: Dialog Dua Kelompok, Satu Item Bersih, dan Cancel | FE+BE | 23 | 225, 612, 227 |
| TC-AC-DN-E2E-082-bulk-delete-campuran-continue | Bulk Delete Campuran: Continue Menghapus Item Bersih dan Kelompok Skip Unit BYO Saja | FE+BE | 29 | 613, 226 |
| TC-AC-DN-E2E-083-bulk-delete-blok-seluruh-item | Bulk Delete: Dialog Blok Seluruh Item Diblok dan Seleksi Dipertahankan | FE+BE | 20 | 228, 229 |
| TC-AC-DN-E2E-084-bulk-delete-satu-item-diblok | Bulk Delete: Satu Item Diblok Memakai Dialog Blok Single (SKU dan Unit BYO) | FE+BE | 21 | 230, 614 |
| TC-AC-DN-E2E-085-delete-berhasil-hapus-permanen-dan-pilihan-device-sku | Delete Device Name Berhasil: Konfirmasi, List Di-refresh, dan Pilihan Device SKU | FE+BE | 11 | 186 |
| TC-AC-DN-E2E-086-fokus-dialog-bulk-delete-dua-kelompok-dan-blok | Aksesibilitas Dialog Bulk Delete: Fokus Terkunci dan Label Aksi Eksplisit (Dua Kelompok D-04 dan Blok D-05) | FE+BE | 17 | 643 |
| TC-AC-DN-E2E-087-detail-buka-tutup-dan-screening | Dialog Detail: Buka (Nama dan Row Action), Screening, Tutup X/Esc, dan Backdrop | FE+BE | 35 | 242, 240, 243, 244, 245, 241 |
| TC-AC-DN-E2E-088-usage-urutan-entity-type-dan-total | Usage by Company: Urutan Company, Entity Type, Total SKU, dan Total Stock | FE+BE | 16 | 246, 247, 248, 249, 250 |
| TC-AC-DN-E2E-089-usage-company-khusus-dan-empty | Usage by Company: Company Client Total SKU 1, BYO Tanpa SKU, Partner Murni, Agregat Stok, dan Empty | FE+BE | 29 | 252, 253, 254, 255, 256, 251 |
| TC-AC-DN-E2E-090-usage-total-sku-distributor-dan-lintas-entitas | Usage by Company: Total SKU Distributor/Client Tanpa Hitung Ganda dan Principal Lintas Entitas | FE+BE | 32 | 560, 659, 660, 662 |
| TC-AC-DN-E2E-091-usage-sort | Usage by Company: Sort Company, Entity Type, Total SKU, dan Total Stock | FE+BE | 24 | 258, 259, 260, 261 |
| TC-AC-DN-E2E-092-usage-filter-bagian-1 | Usage by Company: Screening Filter, Opsi Entity Type, dan Filter Entity Type | FE+BE | 20 | 630, 606, 262 |
| TC-AC-DN-E2E-093-usage-search-dan-filter-kombinasi | Usage by Company: Kombinasi AND Filter dan Search Nama Company/Entity Type/Total | FE+BE | 26 | 631, 264, 593 |
| TC-AC-DN-E2E-094-usage-setup-column-bagian-1 | Usage by Company: Screening Column Visibility/Setup Column, Setup Kolom, dan Kolom Tersisa Satu | FE+BE | 37 | 632, 266, 616 |
| TC-AC-DN-E2E-095-usage-setup-column-urutan-dan-pin | Usage by Company: Geser Urutan dan Pin/Unpin Kolom di Setup Column | FE+BE | 37 | 633, 634 |
| TC-AC-DN-E2E-096-usage-setup-column-reset-tutup-dan-independensi | Usage by Company: Reset to Default, Tutup Modal Membuang Perubahan, dan Independensi dari List | FE+BE | 28 | 636, 635, 595 |
| TC-AC-DN-E2E-097-usage-pagination-reset-state-dan-klik-baris | Usage by Company: Pagination, Klik Baris, dan Dialog Dibuka Kembali Mereset State | FE+BE | 35 | 617, 592, 652 |
| TC-AC-DN-E2E-098-usage-filter-bagian-2 | Usage by Company: Sinkron Chip Entity Type dan Filter Rentang Total SKU/Total Stock | FE+BE | 23 | 639, 263 |
| TC-AC-DN-E2E-099-usage-search-siklus-clear-dan-empty-state | Usage by Company: Siklus Clear Search dan Empty State Tanpa Hasil | FE+BE | 13 | 594, 265 |
| TC-AC-DN-E2E-100-search-siklus-interaksi-dan-kolom | Search List: Siklus Interaksi, Placeholder, dan Kolom Device Name/Category | FE+BE | 40 | 272, 273, 274, 275, 276 |
| TC-AC-DN-E2E-101-search-kolom-lintas-halaman-dan-trim | Search List: Brand/Model/Measurement, Lintas Halaman, Empty, Trim, dan Spasi Saja | FE+BE | 31 | 277, 278, 279, 280, 281, 282 |
| TC-AC-DN-E2E-102-search-karakter-khusus-last-modified-kolom-tersembunyi | Search List: Karakter Khusus, Last Modified Tidak Dicari, Kolom Tersembunyi, dan Reset Halaman | FE+BE | 26 | 283, 284, 285, 286, 287 |
| TC-AC-DN-E2E-103-filter-screening-dan-opsi | Filter Panel List: Screening, Tooltip Ikon, dan Opsi Dropdown dari Data Tabel | FE+BE | 33 | 288, 289, 290, 291, 292, 602 |
| TC-AC-DN-E2E-104-filter-opsi-loading-dan-satu-nilai | Filter Panel List: Loading Opsi, Pencarian Opsi, dan Filter Satu Nilai (Brand, Model/Type, Measurement) | FE+BE | 34 | 293, 295, 296, 297, 298 |
| TC-AC-DN-E2E-105-filter-logika-dan-last-modified | Filter Panel List: Logika OR/AND dan Filter Last Modified (Rentang, Satu Hari, Inklusif, Format) | FE+BE | 30 | 299, 300, 301, 302, 303, 304 |
| TC-AC-DN-E2E-106-filter-chip-dan-sinkron-dua-arah | Filter Panel List: Chip, Hapus Chip, Centang Dropdown, +N more, dan Sinkron Dua Arah | FE+BE | 45 | 305, 306, 307, 308, 637 |
| TC-AC-DN-E2E-107-filter-apply-clear-dan-penutupan-panel | Filter Panel List: Reset Halaman, Clear Field, Tutup Panel Tanpa Apply, dan Indikator Titik | FE+BE | 32 | 310, 311, 312, 313, 314 |
| TC-AC-DN-E2E-108-filter-empty-dan-nilai-tidak-ada | Filter Panel List: Empty State Kombinasi dan Nilai Filter yang Hilang dari Data | FE+BE | 27 | 315, 309, 316 |
| TC-AC-DN-E2E-109-sort-siklus-dan-urutan-awal | Sort List: Urutan Awal dan Siklus Tiga Tahap Kolom Teks serta Hitungan | FE+BE | 35 | 317, 318, 319 |
| TC-AC-DN-E2E-110-sort-aturan-seri-kosong-dan-last-modified | Sort List: Seri Brand, Posisi Baris Kosong, Last Modified, dan Urutan Badge | FE+BE | 32 | 320, 321, 322, 323 |
| TC-AC-DN-E2E-111-sort-perpindahan-kolom-dan-independensi | Sort List: Pindah Kolom, Tanpa Ikon Sort, Collation en-US, dan Tidak Mereset Search/Filter | FE+BE | 38 | 324, 325, 326, 327 |
| TC-AC-DN-E2E-112-setup-column-screening-dan-ceklis | Setup Column List: Screening Overlay dan Modal, Live Preview, dan Ceklis/Unceklis Tiap Kolom | FE+BE | 23 | 328, 329, 603, 330 |
| TC-AC-DN-E2E-113-setup-column-geser-reset-dan-persistensi | Setup Column List: Geser Urutan, Reset to Default, dan Persistensi setelah F5 | FE+BE | 31 | 331, 335, 341 |
| TC-AC-DN-E2E-114-setup-column-pin | Setup Column List: Pin dan Unpin Tiap Kolom | FE+BE | 9 | 332 |
| TC-AC-DN-E2E-115-setup-column-tutup-kolom-terakhir-dan-visibility | Setup Column List: Tutup Modal Membuang Perubahan, Kolom Terakhir, Column Visibility, dan Independensi Changelog | FE+BE | 41 | 336, 337, 338, 339, 340, 342 |
| TC-AC-DN-E2E-116-kombinasi-search-filter-sort-bagian-1 | Kombinasi Search, Filter, Sort, dan Page Size: Irisan dan Clear Field | FE+BE | 37 | 343, 344, 345, 346 |
| TC-AC-DN-E2E-117-kombinasi-independensi-kontrol | Independensi Kontrol: Mengosongkan Search, Pindah Sort, Page Size, dan Empty State Pulih | FE+BE | 37 | 347, 348, 349, 353 |
| TC-AC-DN-E2E-118-kombinasi-seleksi-baris-baru-dan-edit | Kombinasi: Seleksi Bertahan, Logika AND Sidebar, Baris Baru Tidak Cocok Filter, dan Edit Hilang dari Search | FE+BE | 40 | 350, 354, 351, 352 |
| TC-AC-DN-E2E-119-pagination-dasar-dan-seluruh-baris | Pagination List: Awal 10 Baris, Opsi Page Size, Navigasi, Input Nomor, dan Principal Melihat Seluruh Device Name | FE+BE | 29 | 355, 356, 357, 358, 359, 559 |
| TC-AC-DN-E2E-120-pagination-reset-dan-hapus-baris-terakhir | Pagination List: Nomor Tidak Valid, Reset Halaman, 130 Baris, dan Hapus Baris Terakhir | FE+BE | 35 | 360, 361, 362, 363, 364 |
| TC-AC-DN-E2E-121-state-preservation-refresh | State List: Refresh F5 Mempertahankan Search, Sort, Filter, Halaman, dan Page Size | FE+BE | 21 | 381, 382, 383, 384 |
| TC-AC-DN-E2E-122-state-preservation-navigasi-dan-sub-tab | State List: Klik Ulang Menu, Pindah Sub-tab, Node Sidebar, dan Filter Bertahan | FE+BE | 40 | 385, 386, 387, 604 |
| TC-AC-DN-E2E-123-setup-column-pin-gulir-dan-batas | Setup Column List: Kolom Terpin saat Gulir, Persistensi F5, dan Pin Ke-4 Diblok | FE+BE | 19 | 333, 334 |
| TC-AC-DN-E2E-125-changelog-screening-tooltip-dan-tutup | Modal Changelog: Screening, Tooltip, Tutup X/Esc, dan Backdrop | FE+BE | 32 | 388, 389, 390, 391, 392 |
| TC-AC-DN-E2E-126-changelog-urutan-default-format-tanggal-action | Modal Changelog: Urutan Default, Format Date, Kolom Action, dan Field | FE+BE | 26 | 393, 394, 395, 396 |
| TC-AC-DN-E2E-127-changelog-nilai-kosong-modified-by | Modal Changelog: Old/New Value Edit, Nama Setelah Rename, Penanda Nilai Kosong, dan Modified By | FE+BE | 19 | 397, 398, 399, 400, 401 |
| TC-AC-DN-E2E-128-changelog-hover-modified-by-dan-buka-kembali | Modal Changelog: Hover Modified By dan Dibuka Kembali Mereset State | FE+BE | 27 | 402, 405 |
| TC-AC-DN-E2E-129-changelog-search-bagian-1 | Modal Changelog Search: Siklus Interaksi dan Pencarian per Kolom | FE+BE | 36 | 406, 407, 408, 409, 410 |
| TC-AC-DN-E2E-130-changelog-search-bagian-2 | Modal Changelog Search: Old/New Value, Modified By, Huruf Besar-Kecil, dan Trim | FE+BE | 22 | 411, 412, 413, 414, 415 |
| TC-AC-DN-E2E-131-changelog-search-bagian-3 | Modal Changelog Search: Tanggal Tidak Dicocokkan, Tanpa Hasil, Reset Halaman, dan Kolom Tersembunyi | FE+BE | 27 | 416, 417, 418, 419 |
| TC-AC-DN-E2E-132-changelog-filter-screening-dan-opsi | Modal Changelog Filter: Screening, Isi Opsi, Device Name Terhapus, dan Indikator Pemuatan Opsi | FE+BE | 30 | 420, 421, 422, 448 |
| TC-AC-DN-E2E-133-changelog-filter-date-dan-field-tunggal | Modal Changelog Filter: Date Inklusif, Satu Hari, Format Tanggal, Action, dan Device Name | FE+BE | 21 | 423, 424, 425, 426, 427 |
| TC-AC-DN-E2E-134-changelog-filter-field-modifiedby-dan-logika | Modal Changelog Filter: Field, Modified By, dan Logika OR/AND | FE+BE | 25 | 428, 429, 430, 431, 432 |
| TC-AC-DN-E2E-135-changelog-filter-chip | Modal Changelog Filter: Pencarian Opsi, Hapus Chip, Uncheck Opsi, dan +N more | FE+BE | 32 | 433, 434, 435, 436, 437 |
| TC-AC-DN-E2E-136-changelog-filter-clear-tutup-dan-kombinasi | Modal Changelog Filter: Clear Field, Tutup Tanpa Apply, Indikator Titik, dan Kombinasi dengan Search | FE+BE | 42 | 438, 439, 440, 441, 442 |
| TC-AC-DN-E2E-137-changelog-kombinasi-search-filter-sort-pagination | Modal Changelog: Kombinasi Search, Filter, Sort, dan Pagination serta Empty State Pulih | FE+BE | 19 | 443, 444 |
| TC-AC-DN-E2E-138-changelog-reset-halaman-kolom-tersembunyi-dan-opsi-baru | Modal Changelog: Reset Halaman saat Apply, Filter Kolom Tersembunyi, dan Opsi Baru | FE+BE | 28 | 445, 446, 447 |
| TC-AC-DN-E2E-139-changelog-filter-sinkron-dua-arah | Modal Changelog Filter: Sinkron Dua Arah Chip dan Checkbox (Action, Field, Modified By) | FE+BE | 29 | 638 |
| TC-AC-DN-E2E-140-changelog-sort-bagian-1 | Modal Changelog Sort: Date, Kolom Teks, dan Nilai Kosong Old/New Value | FE+BE | 36 | 450, 451, 452, 453 |
| TC-AC-DN-E2E-141-changelog-sort-bagian-2 | Modal Changelog Sort: Modified By, Pindah Kolom, Tanpa Ikon pada Column Visibility, dan Halaman 2 | FE+BE | 22 | 454, 455, 456, 457 |
| TC-AC-DN-E2E-142-changelog-setup-column-screening-dan-ceklis | Modal Changelog Setup Column: Screening Overlay/Popup dan Ceklis Kolom Date, Action, Device Name, Field | FE+BE | 37 | 458, 459, 460 |
| TC-AC-DN-E2E-143-changelog-setup-column-ceklis-urutan | Modal Changelog Setup Column: Ceklis Old/New Value/Modified By dan Geser Urutan | FE+BE | 27 | 461, 462 |
| TC-AC-DN-E2E-144-changelog-setup-column-pin-reset-tutup | Modal Changelog Setup Column: Pin Old Value/New Value/Modified By, Pin Ke-4, Reset to Default, dan Tutup | FE+BE | 39 | 464, 465, 466, 467 |
| TC-AC-DN-E2E-145-changelog-setup-column-visibility-dan-independensi | Modal Changelog Setup Column: Kolom Terakhir, Column Visibility Tanpa Save, dan Independensi dari List | FE+BE | 25 | 468, 469, 470, 471 |
| TC-AC-DN-E2E-146-changelog-pagination | Modal Changelog Pagination: Default 10, Page Size 25, Input Nomor, dan Nomor Tidak Valid | FE+BE | 24 | 472, 473, 474, 475 |
| TC-AC-DN-E2E-147-changelog-download-fungsional | Modal Changelog Download: Overlay Format, CSV Tanpa Toast, Mengikuti Search dan Filter Aktif | FE+BE | 19 | 476, 477, 480, 481 |
| TC-AC-DN-E2E-148-changelog-download-kolom-dan-kosong | Modal Changelog Download: Kolom yang Tampil dan Hasil Search Kosong (Hanya Header) | FE+BE | 16 | 482, 486 |
| TC-AC-DN-E2E-149-changelog-download-isi-berkas | Modal Changelog Download: Isi Berkas (Sheet1 XLSX, BOM CSV, Hyphen, Format Date, Modified By Nama Lengkap) | FE+BE | 22 | 478, 479, 483, 484, 485 |
| TC-AC-DN-E2E-150-changelog-setup-column-pin-date-field | Modal Changelog Setup Column: Pin dan Unpin Kolom Date, Action, Device Name, Field | FE+BE | 26 | 463 |
| TC-AC-DN-E2E-152-log-create-changelog-activity-log | Pencatatan Create: Changelog dan Activity Log (Satu Entri Field Device Name, Tanpa Duplikat, Object Non-entitas) | FE+BE | 45 | 488, 491, 506 |
| TC-AC-DN-E2E-153-log-edit-changelog-activity-log | Pencatatan Edit: Satu Entri per Field yang Berubah di Changelog dan Activity Log | FE+BE | 52 | 492, 493, 494 |
| TC-AC-DN-E2E-154-log-edit-tiga-field-dan-last-modified | Pencatatan Edit: Tiga Field Sekaligus dan Last Modified Diperbarui atau Tetap | FE+BE | 38 | 495, 507, 508 |
| TC-AC-DN-E2E-155-log-delete-dan-bulk-delete | Pencatatan Delete dan Bulk Delete: Entri Hanya untuk Item yang Terhapus | FE+BE | 48 | 496, 499, 500 |
| TC-AC-DN-E2E-156-log-bulk-delete-campuran | Pencatatan Bulk Delete Campuran di Activity Log dan System Log Aktor | FE+BE | 25 | 615 |
| TC-AC-DN-E2E-157-log-absence-create | Absence Log: Create Tidak Mencatat Field Measurement atau Category | FE+BE | 41 | 489, 490 |
| TC-AC-DN-E2E-158-log-absence-delete | Absence Log: Delete Tidak Mencatat Field Measurement atau Category | FE+BE | 33 | 497, 498 |
| TC-AC-DN-E2E-159-log-absence-no-op-dan-system-log | Absence Log: Edit Tanpa Perubahan atau Hanya Kapitalisasi Tidak Menulis Entri (Changelog, Activity Log, System Log) | FE+BE | 44 | 501, 502, 512 |
| TC-AC-DN-E2E-160-log-absence-aksi-gagal | Absence Log: Create, Edit, dan Delete yang Gagal karena Error Server Tidak Menulis Entri | FE+BE | 53 | 503, 504, 505 |
| TC-AC-DN-E2E-161-log-system-log-aktor | System Log Aktor: Entri Edit, Create, dan Delete Device Name | FE+BE | 41 | 509, 510, 511 |
| TC-AC-DN-E2E-162-log-sinkron-dan-pelaku | Pencatatan Sinkron Changelog/Activity Log/System Log, Entri Tetap setelah Delete, dan Pelaku Entri | FE+BE | 42 | 513, 517, 516 |
| TC-AC-DN-E2E-163-log-snapshot-immutability | Snapshot Immutability: Rename Dua Kali dan Rename Tidak Mengubah Entri Lama | FE+BE | 40 | 514, 515 |
| TC-AC-DN-E2E-164-download-list-fungsional | Download List: Tooltip, Overlay Format, Nama Berkas CSV/XLSX Tanpa Toast, Seluruh Baris, dan Filter Kosong | FE+BE | 27 | 365, 366, 367, 369, 378 |
| TC-AC-DN-E2E-165-download-list-mengikuti-filter-dan-kolom | Download List: Mengikuti Search, Filter, Sidebar, dan Kolom yang Tampil | FE+BE | 30 | 370, 371, 372, 373 |
| TC-AC-DN-E2E-166-download-list-isi-berkas | Download List: Isi Berkas (Category Jalur Penuh, Brand/Model, Hyphen, Last Modified, BOM CSV, Sheet1 XLSX) | FE+BE | 41 | 374, 375, 376, 377, 379, 380 |
| TC-AC-DN-E2E-167-download-volume-besar-dan-limit | Download di Atas 5.000 Baris (List dan Changelog) dan Create Tidak Ikut Master Data Count Limit | FE+BE | 37 | 607, 608, 605 |
| TC-AC-DN-E2E-170-sinkron-device-sku-dropdown-dan-baris | Sinkronisasi ke Device SKU: Create, Rename, dan Delete Device Name pada Dropdown dan Baris SKU | FE+BE | 46 | 518, 519, 520, 521 |
| TC-AC-DN-E2E-171-sinkron-device-sku-brand-model-dan-guard | Sinkronisasi dari Device SKU: Brand/Model Terisi, Kembali ke Em Dash, Changelog Tidak Bertambah, dan Delete Diblok | FE+BE | 40 | 522, 523, 524, 525 |
| TC-AC-DN-E2E-172-sinkron-master-data-category-measurement | Sinkronisasi Master Data: Unit BYO Hardware, Node Category, dan Measurement Baru/Dihapus pada Dropdown Create | FE+BE | 38 | 527, 528, 529, 530, 531 |
| TC-AC-DN-E2E-173-sinkron-rename-master-data-pada-list | Rename Master Data (Measurement, Category, Brand): Baris Device Name Tetap Tampil dengan Nama Terkini | FE+BE | 47 | 532, 533, 624 |
| TC-AC-DN-E2E-174-guard-delete-setelah-penghapusan-relasi | Guard Delete: Lolos setelah Unit BYO atau SKU Terakhir Dihapus | FE+BE | 31 | 640, 641 |
| TC-AC-DN-E2E-175-rename-device-name-dengan-unit-byo | Rename Device Name yang Memiliki Unit BYO Hardware atau TAG Tidak Memutus Relasi | FE+BE | 30 | 650, 651 |
| TC-AC-DN-E2E-176-sinkron-general-settings-dan-capability | General Settings (Date Format) dan Capability Delete yang Dicabut | FE+BE | 28 | 534, 535, 536, 538 |
| TC-AC-DN-E2E-177-jalur-b-handheld-reader-usb | Pemilih Device Name Aktivasi Jalur B Handheld Reader oleh Client (Simulator USB) | FE+BE | 39 | 656, 658 |
| TC-AC-DN-E2E-178-all-tags-self-purchased-dan-registri | All TAGs: Pemilih Device Name Self-Purchased Template dan Registri Tag Jalur A/B setelah Rename | FE+BE | 30 | 657, 661 |
| TC-AC-DN-E2E-179-konkurensi-create-duplikat-dan-referensi | Konkurensi Create: Duplikat setelah Pengecekan Lolos dan Measurement Dihapus Admin Lain | FE+BE | 29 | 96, 104 |
| TC-AC-DN-E2E-180-konkurensi-category-berubah-dan-sku-baru | Konkurensi: Category Dihapus atau Mendapat Subcategory (Create) dan SKU Baru dari Sesi Lain saat Edit Category | FE+BE | 43 | 105, 106, 582 |
| TC-AC-DN-E2E-181-konkurensi-edit-bagian-1 | Konkurensi Edit: Duplikat, Device Name Dihapus Admin Lain, dan Save setelah Device Name Terhapus | FE+BE | 27 | 147, 573, 159 |
| TC-AC-DN-E2E-182-konkurensi-edit-bagian-2 | Konkurensi Edit: Measurement atau Category Dihapus Admin Lain saat Form Edit Terbuka | FE+BE | 30 | 155, 156 |
| TC-AC-DN-E2E-183-konkurensi-delete | Konkurensi Delete: SKU atau Unit BYO Ditambah, Dihapus Admin Lain, dan Konfirmasi setelah Perubahan | FE+BE | 40 | 193, 194, 195, 574, 575 |
| TC-AC-DN-E2E-184-konkurensi-bulk-delete-bagian-1 | Konkurensi Bulk Delete: Item Menjadi Berelasi atau Dihapus Admin Lain saat Dialog Terbuka | FE+BE | 40 | 231, 232, 233, 234 |
| TC-AC-DN-E2E-185-konkurensi-bulk-delete-bagian-2 | Konkurensi Bulk Delete: Seleksi Campuran SKU dan Hapus dari Sesi Lain | FE+BE | 42 | 579, 580, 581, 625 |
| TC-AC-DN-E2E-186-konkurensi-dua-sesi-ui-duplikat-nama | Konkurensi Dua Sesi UI: Create dan Edit ke Nama yang Sama, Submit Kedua Ditolak | FE+BE | 35 | 576, 572 |
| TC-AC-DN-E2E-187-konkurensi-dua-sesi-ui-last-write-wins | Konkurensi Dua Sesi UI: Edit Record yang Sama, Save Kedua Menimpa Save Pertama | FE+BE | 31 | 160, 571 |

## Pembagian TC lintas spec

Tidak ada TC yang terbelah lintas spec. Nomor cadangan terpakai untuk memecah spec yang melewati ~35 langkah: 022, 023, 040, 041, 054, 055, 085, 086, 098, 099, 123, 150, 186, 187. Nomor 067, 068, 124, 151, 168 dan 169 tidak terpakai.

## Kebutuhan lingkungan (tim FE)

- Fixture `Fixture.settings-device-name` (kunci akun, seeding Device Name, SKU, unit BYO, Company F–I, riwayat) belum ada.
- Variabel lingkungan perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`: `AC_TC_PASSWORD`, `AC_DN_TC2_PASSWORD`, `AC_DN_RO_PASSWORD`, `AC_DN_CREATE_PASSWORD`, `AC_DN_UPDATE_PASSWORD`, `AC_DN_DELETE_PASSWORD`, `AC_DN_CRUD_PASSWORD`, `AC_DN_NOCAP_PASSWORD`, `AC_DN_DISTRIBUTOR_PASSWORD`, `AC_DN_PARTNER_PASSWORD`, `AC_DN_CLIENT_PASSWORD`, `AC_DN_FRESH_PASSWORD`, `AC_DN_GUIDED_PASSWORD`, `AC_DN_BIG_PASSWORD`, `AC_DN_VOLUME_PASSWORD`.
- Kemampuan teknis: sesi API per akun, intercept respons, pembaca berkas unduhan (CSV/XLSX), pembaca jumlah entri Changelog/Activity Log/System Log, pemulihan state Pre-setup (Selection Limit, General Settings, capability role, nama master, Last Modified `Tag Reel`), perangkat Android untuk spec mobile 018–021 dan simulator USB untuk spec 177.

## Temuan yang masih terbuka

Temuan sumber TC (ambigu, kontradiktif, prasyarat hilang) dicatat per spec di bagian `Temuan untuk QA`. Yang perlu keputusan: nama literal `X` (spec 055) dan `Company F`–`Company I` (spec 089/090) sebagai pengecualian S-12; kategori `Antena Uji {runId}-057` pada spec 057; asumsi Filter Panel menutup setelah `[Apply]` (TC 311–315); kontradiksi isi TC 622/629 terhadap data Pre-setup; baris `DN` pada registri prefix masih 1–626 padahal TC berisi 662.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-DN-1 | TC-AC-DN-E2E-001 | FE+BE |
| TC-AC-DN-2 | TC-AC-DN-E2E-001 | FE+BE |
| TC-AC-DN-3 | TC-AC-DN-E2E-001 | FE+BE |
| TC-AC-DN-4 | TC-AC-DN-E2E-001 | FE+BE |
| TC-AC-DN-5 | TC-AC-DN-E2E-002 | FE+BE |
| TC-AC-DN-6 | TC-AC-DN-E2E-002 | FE+BE |
| TC-AC-DN-7 | TC-AC-DN-E2E-002 | FE+BE |
| TC-AC-DN-8 | TC-AC-DN-E2E-001 | FE+BE |
| TC-AC-DN-9 | TC-AC-DN-E2E-003 | FE+BE |
| TC-AC-DN-10 | TC-AC-DN-E2E-003 | FE+BE |
| TC-AC-DN-11 | TC-AC-DN-E2E-003 | FE+BE |
| TC-AC-DN-12 | TC-AC-DN-E2E-003 | FE+BE |
| TC-AC-DN-13 | TC-AC-DN-E2E-004 | FE+BE |
| TC-AC-DN-14 | TC-AC-DN-E2E-004 | FE+BE |
| TC-AC-DN-15 | TC-AC-DN-E2E-004 | FE+BE |
| TC-AC-DN-16 | TC-AC-DN-E2E-004 | FE+BE |
| TC-AC-DN-17 | TC-AC-DN-E2E-005 | FE+BE |
| TC-AC-DN-18 | TC-AC-DN-E2E-007 | FE+BE |
| TC-AC-DN-19 | TC-AC-DN-E2E-007 | FE+BE |
| TC-AC-DN-20 | TC-AC-DN-E2E-007 | FE+BE |
| TC-AC-DN-21 | TC-AC-DN-E2E-007 | FE+BE |
| TC-AC-DN-22 | TC-AC-DN-E2E-007 | FE+BE |
| TC-AC-DN-23 | TC-AC-DN-E2E-005 | FE+BE |
| TC-AC-DN-24 | TC-AC-DN-E2E-008 | FE+BE |
| TC-AC-DN-25 | TC-AC-DN-E2E-009 | FE+BE |
| TC-AC-DN-26 | TC-AC-DN-E2E-008 | FE+BE |
| TC-AC-DN-27 | TC-AC-DN-E2E-008 | FE+BE |
| TC-AC-DN-28 | TC-AC-DN-E2E-008 | FE+BE |
| TC-AC-DN-29 | TC-AC-DN-E2E-035 | FE+BE |
| TC-AC-DN-30 | TC-AC-DN-E2E-035 | FE+BE |
| TC-AC-DN-31 | TC-AC-DN-E2E-011 | FE+BE |
| TC-AC-DN-32 | TC-AC-DN-E2E-011 | FE+BE |
| TC-AC-DN-33 | TC-AC-DN-E2E-011 | FE+BE |
| TC-AC-DN-34 | TC-AC-DN-E2E-011 | FE+BE |
| TC-AC-DN-35 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-36 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-37 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-38 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-39 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-40 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-41 | TC-AC-DN-E2E-012 | FE+BE |
| TC-AC-DN-42 | TC-AC-DN-E2E-013 | FE+BE |
| TC-AC-DN-43 | TC-AC-DN-E2E-013 | FE+BE |
| TC-AC-DN-44 | TC-AC-DN-E2E-014 | FE+BE |
| TC-AC-DN-45 | TC-AC-DN-E2E-014 | FE+BE |
| TC-AC-DN-46 | TC-AC-DN-E2E-013 | FE+BE |
| TC-AC-DN-47 | TC-AC-DN-E2E-018 | FE+BE |
| TC-AC-DN-48 | TC-AC-DN-E2E-018 | FE+BE |
| TC-AC-DN-49 | TC-AC-DN-E2E-018 | FE+BE |
| TC-AC-DN-50 | TC-AC-DN-E2E-019 | FE+BE |
| TC-AC-DN-51 | TC-AC-DN-E2E-019 | FE+BE |
| TC-AC-DN-52 | TC-AC-DN-E2E-019 | FE+BE |
| TC-AC-DN-53 | TC-AC-DN-E2E-019 | FE+BE |
| TC-AC-DN-54 | TC-AC-DN-E2E-020 | FE+BE |
| TC-AC-DN-55 | TC-AC-DN-E2E-020 | FE+BE |
| TC-AC-DN-56 | TC-AC-DN-E2E-020 | FE+BE |
| TC-AC-DN-57 | TC-AC-DN-E2E-020 | FE+BE |
| TC-AC-DN-58 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-59 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-60 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-61 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-62 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-63 | TC-AC-DN-E2E-026 | FE+BE |
| TC-AC-DN-64 | TC-AC-DN-E2E-026 | FE+BE |
| TC-AC-DN-65 | TC-AC-DN-E2E-026 | FE+BE |
| TC-AC-DN-66 | TC-AC-DN-E2E-026 | FE+BE |
| TC-AC-DN-67 | TC-AC-DN-E2E-040 | FE+BE |
| TC-AC-DN-68 | TC-AC-DN-E2E-040 | FE+BE |
| TC-AC-DN-69 | TC-AC-DN-E2E-040 | FE+BE |
| TC-AC-DN-70 | TC-AC-DN-E2E-027 | FE+BE |
| TC-AC-DN-71 | TC-AC-DN-E2E-027 | FE+BE |
| TC-AC-DN-72 | TC-AC-DN-E2E-028 | FE+BE |
| TC-AC-DN-73 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-74 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-75 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-76 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-77 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-78 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-79 | TC-AC-DN-E2E-047 | FE+BE |
| TC-AC-DN-80 | TC-AC-DN-E2E-047 | FE+BE |
| TC-AC-DN-81 | TC-AC-DN-E2E-047 | FE+BE |
| TC-AC-DN-82 | TC-AC-DN-E2E-050 | FE+BE |
| TC-AC-DN-83 | TC-AC-DN-E2E-050 | FE+BE |
| TC-AC-DN-84 | TC-AC-DN-E2E-049 | FE+BE |
| TC-AC-DN-85 | TC-AC-DN-E2E-049 | FE+BE |
| TC-AC-DN-86 | TC-AC-DN-E2E-049 | FE+BE |
| TC-AC-DN-87 | TC-AC-DN-E2E-043 | FE+BE |
| TC-AC-DN-88 | TC-AC-DN-E2E-043 | FE+BE |
| TC-AC-DN-89 | TC-AC-DN-E2E-048 | FE+BE |
| TC-AC-DN-90 | TC-AC-DN-E2E-048 | FE+BE |
| TC-AC-DN-91 | TC-AC-DN-E2E-044 | FE+BE |
| TC-AC-DN-92 | TC-AC-DN-E2E-048 | FE+BE |
| TC-AC-DN-93 | TC-AC-DN-E2E-046 | FE+BE |
| TC-AC-DN-94 | TC-AC-DN-E2E-046 | FE+BE |
| TC-AC-DN-95 | TC-AC-DN-E2E-046 | FE+BE |
| TC-AC-DN-96 | TC-AC-DN-E2E-179 | FE+BE |
| TC-AC-DN-97 | TC-AC-DN-E2E-045 | FE+BE |
| TC-AC-DN-98 | TC-AC-DN-E2E-045 | FE+BE |
| TC-AC-DN-99 | TC-AC-DN-E2E-045 | FE+BE |
| TC-AC-DN-100 | TC-AC-DN-E2E-048 | FE+BE |
| TC-AC-DN-101 | TC-AC-DN-E2E-043 | FE+BE |
| TC-AC-DN-102 | TC-AC-DN-E2E-043 | FE+BE |
| TC-AC-DN-103 | TC-AC-DN-E2E-043 | FE+BE |
| TC-AC-DN-104 | TC-AC-DN-E2E-179 | FE+BE |
| TC-AC-DN-105 | TC-AC-DN-E2E-180 | FE+BE |
| TC-AC-DN-106 | TC-AC-DN-E2E-180 | FE+BE |
| TC-AC-DN-107 | TC-AC-DN-E2E-027 | FE+BE |
| TC-AC-DN-108 | TC-AC-DN-E2E-051 | FE+BE |
| TC-AC-DN-109 | TC-AC-DN-E2E-051 | FE+BE |
| TC-AC-DN-110 | TC-AC-DN-E2E-054 | FE+BE |
| TC-AC-DN-111 | TC-AC-DN-E2E-050 | FE+BE |
| TC-AC-DN-112 | TC-AC-DN-E2E-036 | FE+BE |
| TC-AC-DN-113 | TC-AC-DN-E2E-036 | FE+BE |
| TC-AC-DN-114 | TC-AC-DN-E2E-036 | FE+BE |
| TC-AC-DN-115 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-116 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-117 | TC-AC-DN-E2E-052 | FE+BE |
| TC-AC-DN-118 | TC-AC-DN-E2E-052 | FE+BE |
| TC-AC-DN-119 | TC-AC-DN-E2E-052 | FE+BE |
| TC-AC-DN-120 | TC-AC-DN-E2E-052 | FE+BE |
| TC-AC-DN-121 | TC-AC-DN-E2E-052 | FE+BE |
| TC-AC-DN-122 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-123 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-124 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-125 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-126 | TC-AC-DN-E2E-053 | FE+BE |
| TC-AC-DN-127 | TC-AC-DN-E2E-054 | FE+BE |
| TC-AC-DN-128 | TC-AC-DN-E2E-056 | FE+BE |
| TC-AC-DN-129 | TC-AC-DN-E2E-056 | FE+BE |
| TC-AC-DN-130 | TC-AC-DN-E2E-056 | FE+BE |
| TC-AC-DN-131 | TC-AC-DN-E2E-056 | FE+BE |
| TC-AC-DN-132 | TC-AC-DN-E2E-057 | FE+BE |
| TC-AC-DN-133 | TC-AC-DN-E2E-057 | FE+BE |
| TC-AC-DN-134 | TC-AC-DN-E2E-058 | FE+BE |
| TC-AC-DN-135 | TC-AC-DN-E2E-058 | FE+BE |
| TC-AC-DN-136 | TC-AC-DN-E2E-058 | FE+BE |
| TC-AC-DN-137 | TC-AC-DN-E2E-059 | FE+BE |
| TC-AC-DN-138 | TC-AC-DN-E2E-059 | FE+BE |
| TC-AC-DN-139 | TC-AC-DN-E2E-060 | FE+BE |
| TC-AC-DN-140 | TC-AC-DN-E2E-060 | FE+BE |
| TC-AC-DN-141 | TC-AC-DN-E2E-060 | FE+BE |
| TC-AC-DN-142 | TC-AC-DN-E2E-060 | FE+BE |
| TC-AC-DN-143 | TC-AC-DN-E2E-062 | FE+BE |
| TC-AC-DN-144 | TC-AC-DN-E2E-062 | FE+BE |
| TC-AC-DN-145 | TC-AC-DN-E2E-062 | FE+BE |
| TC-AC-DN-146 | TC-AC-DN-E2E-062 | FE+BE |
| TC-AC-DN-147 | TC-AC-DN-E2E-181 | FE+BE |
| TC-AC-DN-148 | TC-AC-DN-E2E-061 | FE+BE |
| TC-AC-DN-149 | TC-AC-DN-E2E-061 | FE+BE |
| TC-AC-DN-150 | TC-AC-DN-E2E-061 | FE+BE |
| TC-AC-DN-151 | TC-AC-DN-E2E-061 | FE+BE |
| TC-AC-DN-152 | TC-AC-DN-E2E-059 | FE+BE |
| TC-AC-DN-153 | TC-AC-DN-E2E-059 | FE+BE |
| TC-AC-DN-154 | TC-AC-DN-E2E-059 | FE+BE |
| TC-AC-DN-155 | TC-AC-DN-E2E-182 | FE+BE |
| TC-AC-DN-156 | TC-AC-DN-E2E-182 | FE+BE |
| TC-AC-DN-157 | TC-AC-DN-E2E-057 | FE+BE |
| TC-AC-DN-158 | TC-AC-DN-E2E-057 | FE+BE |
| TC-AC-DN-159 | TC-AC-DN-E2E-181 | FE+BE |
| TC-AC-DN-160 | TC-AC-DN-E2E-187 | FE+BE |
| TC-AC-DN-161 | TC-AC-DN-E2E-027 | FE+BE |
| TC-AC-DN-162 | TC-AC-DN-E2E-063 | FE+BE |
| TC-AC-DN-163 | TC-AC-DN-E2E-063 | FE+BE |
| TC-AC-DN-164 | TC-AC-DN-E2E-063 | FE+BE |
| TC-AC-DN-165 | TC-AC-DN-E2E-063 | FE+BE |
| TC-AC-DN-166 | TC-AC-DN-E2E-063 | FE+BE |
| TC-AC-DN-167 | TC-AC-DN-E2E-037 | FE+BE |
| TC-AC-DN-168 | TC-AC-DN-E2E-037 | FE+BE |
| TC-AC-DN-169 | TC-AC-DN-E2E-066 | FE+BE |
| TC-AC-DN-170 | TC-AC-DN-E2E-066 | FE+BE |
| TC-AC-DN-171 | TC-AC-DN-E2E-064 | FE+BE |
| TC-AC-DN-172 | TC-AC-DN-E2E-064 | FE+BE |
| TC-AC-DN-173 | TC-AC-DN-E2E-064 | FE+BE |
| TC-AC-DN-174 | TC-AC-DN-E2E-064 | FE+BE |
| TC-AC-DN-175 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-176 | TC-AC-DN-E2E-066 | FE+BE |
| TC-AC-DN-177 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-178 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-179 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-180 | TC-AC-DN-E2E-058 | FE+BE |
| TC-AC-DN-181 | TC-AC-DN-E2E-069 | FE+BE |
| TC-AC-DN-182 | TC-AC-DN-E2E-069 | FE+BE |
| TC-AC-DN-183 | TC-AC-DN-E2E-069 | FE+BE |
| TC-AC-DN-184 | TC-AC-DN-E2E-069 | FE+BE |
| TC-AC-DN-185 | TC-AC-DN-E2E-069 | FE+BE |
| TC-AC-DN-186 | TC-AC-DN-E2E-085 | FE+BE |
| TC-AC-DN-187 | TC-AC-DN-E2E-070 | FE+BE |
| TC-AC-DN-188 | TC-AC-DN-E2E-071 | FE+BE |
| TC-AC-DN-189 | TC-AC-DN-E2E-071 | FE+BE |
| TC-AC-DN-190 | TC-AC-DN-E2E-072 | FE+BE |
| TC-AC-DN-191 | TC-AC-DN-E2E-072 | FE+BE |
| TC-AC-DN-192 | TC-AC-DN-E2E-071 | FE+BE |
| TC-AC-DN-193 | TC-AC-DN-E2E-183 | FE+BE |
| TC-AC-DN-194 | TC-AC-DN-E2E-183 | FE+BE |
| TC-AC-DN-195 | TC-AC-DN-E2E-183 | FE+BE |
| TC-AC-DN-196 | TC-AC-DN-E2E-038 | FE+BE |
| TC-AC-DN-197 | TC-AC-DN-E2E-038 | FE+BE |
| TC-AC-DN-198 | TC-AC-DN-E2E-038 | FE+BE |
| TC-AC-DN-199 | TC-AC-DN-E2E-070 | FE+BE |
| TC-AC-DN-200 | TC-AC-DN-E2E-070 | FE+BE |
| TC-AC-DN-201 | TC-AC-DN-E2E-028 | FE+BE |
| TC-AC-DN-202 | TC-AC-DN-E2E-075 | FE+BE |
| TC-AC-DN-203 | TC-AC-DN-E2E-075 | FE+BE |
| TC-AC-DN-204 | TC-AC-DN-E2E-075 | FE+BE |
| TC-AC-DN-205 | TC-AC-DN-E2E-075 | FE+BE |
| TC-AC-DN-206 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-207 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-208 | TC-AC-DN-E2E-075 | FE+BE |
| TC-AC-DN-209 | TC-AC-DN-E2E-077 | FE+BE |
| TC-AC-DN-210 | TC-AC-DN-E2E-077 | FE+BE |
| TC-AC-DN-211 | TC-AC-DN-E2E-077 | FE+BE |
| TC-AC-DN-212 | TC-AC-DN-E2E-077 | FE+BE |
| TC-AC-DN-213 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-214 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-215 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-216 | TC-AC-DN-E2E-076 | FE+BE |
| TC-AC-DN-217 | TC-AC-DN-E2E-078 | FE+BE |
| TC-AC-DN-218 | TC-AC-DN-E2E-078 | FE+BE |
| TC-AC-DN-219 | TC-AC-DN-E2E-079 | FE+BE |
| TC-AC-DN-220 | TC-AC-DN-E2E-079 | FE+BE |
| TC-AC-DN-221 | TC-AC-DN-E2E-079 | FE+BE |
| TC-AC-DN-222 | TC-AC-DN-E2E-079 | FE+BE |
| TC-AC-DN-223 | TC-AC-DN-E2E-080 | FE+BE |
| TC-AC-DN-224 | TC-AC-DN-E2E-080 | FE+BE |
| TC-AC-DN-225 | TC-AC-DN-E2E-081 | FE+BE |
| TC-AC-DN-226 | TC-AC-DN-E2E-082 | FE+BE |
| TC-AC-DN-227 | TC-AC-DN-E2E-081 | FE+BE |
| TC-AC-DN-228 | TC-AC-DN-E2E-083 | FE+BE |
| TC-AC-DN-229 | TC-AC-DN-E2E-083 | FE+BE |
| TC-AC-DN-230 | TC-AC-DN-E2E-084 | FE+BE |
| TC-AC-DN-231 | TC-AC-DN-E2E-184 | FE+BE |
| TC-AC-DN-232 | TC-AC-DN-E2E-184 | FE+BE |
| TC-AC-DN-233 | TC-AC-DN-E2E-184 | FE+BE |
| TC-AC-DN-234 | TC-AC-DN-E2E-184 | FE+BE |
| TC-AC-DN-235 | TC-AC-DN-E2E-039 | FE+BE |
| TC-AC-DN-236 | TC-AC-DN-E2E-039 | FE+BE |
| TC-AC-DN-237 | TC-AC-DN-E2E-080 | FE+BE |
| TC-AC-DN-238 | TC-AC-DN-E2E-028 | FE+BE |
| TC-AC-DN-239 | TC-AC-DN-E2E-080 | FE+BE |
| TC-AC-DN-240 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-241 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-242 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-243 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-244 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-245 | TC-AC-DN-E2E-087 | FE+BE |
| TC-AC-DN-246 | TC-AC-DN-E2E-088 | FE+BE |
| TC-AC-DN-247 | TC-AC-DN-E2E-088 | FE+BE |
| TC-AC-DN-248 | TC-AC-DN-E2E-088 | FE+BE |
| TC-AC-DN-249 | TC-AC-DN-E2E-088 | FE+BE |
| TC-AC-DN-250 | TC-AC-DN-E2E-088 | FE+BE |
| TC-AC-DN-251 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-252 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-253 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-254 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-255 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-256 | TC-AC-DN-E2E-089 | FE+BE |
| TC-AC-DN-257 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-258 | TC-AC-DN-E2E-091 | FE+BE |
| TC-AC-DN-259 | TC-AC-DN-E2E-091 | FE+BE |
| TC-AC-DN-260 | TC-AC-DN-E2E-091 | FE+BE |
| TC-AC-DN-261 | TC-AC-DN-E2E-091 | FE+BE |
| TC-AC-DN-262 | TC-AC-DN-E2E-092 | FE+BE |
| TC-AC-DN-263 | TC-AC-DN-E2E-098 | FE+BE |
| TC-AC-DN-264 | TC-AC-DN-E2E-093 | FE+BE |
| TC-AC-DN-265 | TC-AC-DN-E2E-099 | FE+BE |
| TC-AC-DN-266 | TC-AC-DN-E2E-094 | FE+BE |
| TC-AC-DN-267 | TC-AC-DN-E2E-005 | FE+BE |
| TC-AC-DN-268 | TC-AC-DN-E2E-005 | FE+BE |
| TC-AC-DN-269 | TC-AC-DN-E2E-006 | FE+BE |
| TC-AC-DN-270 | TC-AC-DN-E2E-006 | FE+BE |
| TC-AC-DN-271 | TC-AC-DN-E2E-006 | FE+BE |
| TC-AC-DN-272 | TC-AC-DN-E2E-100 | FE+BE |
| TC-AC-DN-273 | TC-AC-DN-E2E-100 | FE+BE |
| TC-AC-DN-274 | TC-AC-DN-E2E-100 | FE+BE |
| TC-AC-DN-275 | TC-AC-DN-E2E-100 | FE+BE |
| TC-AC-DN-276 | TC-AC-DN-E2E-100 | FE+BE |
| TC-AC-DN-277 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-278 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-279 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-280 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-281 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-282 | TC-AC-DN-E2E-101 | FE+BE |
| TC-AC-DN-283 | TC-AC-DN-E2E-102 | FE+BE |
| TC-AC-DN-284 | TC-AC-DN-E2E-102 | FE+BE |
| TC-AC-DN-285 | TC-AC-DN-E2E-102 | FE+BE |
| TC-AC-DN-286 | TC-AC-DN-E2E-102 | FE+BE |
| TC-AC-DN-287 | TC-AC-DN-E2E-102 | FE+BE |
| TC-AC-DN-288 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-289 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-290 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-291 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-292 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-293 | TC-AC-DN-E2E-104 | FE+BE |
| TC-AC-DN-294 | TC-AC-DN-E2E-009 | FE+BE |
| TC-AC-DN-295 | TC-AC-DN-E2E-104 | FE+BE |
| TC-AC-DN-296 | TC-AC-DN-E2E-104 | FE+BE |
| TC-AC-DN-297 | TC-AC-DN-E2E-104 | FE+BE |
| TC-AC-DN-298 | TC-AC-DN-E2E-104 | FE+BE |
| TC-AC-DN-299 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-300 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-301 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-302 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-303 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-304 | TC-AC-DN-E2E-105 | FE+BE |
| TC-AC-DN-305 | TC-AC-DN-E2E-106 | FE+BE |
| TC-AC-DN-306 | TC-AC-DN-E2E-106 | FE+BE |
| TC-AC-DN-307 | TC-AC-DN-E2E-106 | FE+BE |
| TC-AC-DN-308 | TC-AC-DN-E2E-106 | FE+BE |
| TC-AC-DN-309 | TC-AC-DN-E2E-108 | FE+BE |
| TC-AC-DN-310 | TC-AC-DN-E2E-107 | FE+BE |
| TC-AC-DN-311 | TC-AC-DN-E2E-107 | FE+BE |
| TC-AC-DN-312 | TC-AC-DN-E2E-107 | FE+BE |
| TC-AC-DN-313 | TC-AC-DN-E2E-107 | FE+BE |
| TC-AC-DN-314 | TC-AC-DN-E2E-107 | FE+BE |
| TC-AC-DN-315 | TC-AC-DN-E2E-108 | FE+BE |
| TC-AC-DN-316 | TC-AC-DN-E2E-108 | FE+BE |
| TC-AC-DN-317 | TC-AC-DN-E2E-109 | FE+BE |
| TC-AC-DN-318 | TC-AC-DN-E2E-109 | FE+BE |
| TC-AC-DN-319 | TC-AC-DN-E2E-109 | FE+BE |
| TC-AC-DN-320 | TC-AC-DN-E2E-110 | FE+BE |
| TC-AC-DN-321 | TC-AC-DN-E2E-110 | FE+BE |
| TC-AC-DN-322 | TC-AC-DN-E2E-110 | FE+BE |
| TC-AC-DN-323 | TC-AC-DN-E2E-110 | FE+BE |
| TC-AC-DN-324 | TC-AC-DN-E2E-111 | FE+BE |
| TC-AC-DN-325 | TC-AC-DN-E2E-111 | FE+BE |
| TC-AC-DN-326 | TC-AC-DN-E2E-111 | FE+BE |
| TC-AC-DN-327 | TC-AC-DN-E2E-111 | FE+BE |
| TC-AC-DN-328 | TC-AC-DN-E2E-112 | FE+BE |
| TC-AC-DN-329 | TC-AC-DN-E2E-112 | FE+BE |
| TC-AC-DN-330 | TC-AC-DN-E2E-112 | FE+BE |
| TC-AC-DN-331 | TC-AC-DN-E2E-113 | FE+BE |
| TC-AC-DN-332 | TC-AC-DN-E2E-114 | FE+BE |
| TC-AC-DN-333 | TC-AC-DN-E2E-123 | FE+BE |
| TC-AC-DN-334 | TC-AC-DN-E2E-123 | FE+BE |
| TC-AC-DN-335 | TC-AC-DN-E2E-113 | FE+BE |
| TC-AC-DN-336 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-337 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-338 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-339 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-340 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-341 | TC-AC-DN-E2E-113 | FE+BE |
| TC-AC-DN-342 | TC-AC-DN-E2E-115 | FE+BE |
| TC-AC-DN-343 | TC-AC-DN-E2E-116 | FE+BE |
| TC-AC-DN-344 | TC-AC-DN-E2E-116 | FE+BE |
| TC-AC-DN-345 | TC-AC-DN-E2E-116 | FE+BE |
| TC-AC-DN-346 | TC-AC-DN-E2E-116 | FE+BE |
| TC-AC-DN-347 | TC-AC-DN-E2E-117 | FE+BE |
| TC-AC-DN-348 | TC-AC-DN-E2E-117 | FE+BE |
| TC-AC-DN-349 | TC-AC-DN-E2E-117 | FE+BE |
| TC-AC-DN-350 | TC-AC-DN-E2E-118 | FE+BE |
| TC-AC-DN-351 | TC-AC-DN-E2E-118 | FE+BE |
| TC-AC-DN-352 | TC-AC-DN-E2E-118 | FE+BE |
| TC-AC-DN-353 | TC-AC-DN-E2E-117 | FE+BE |
| TC-AC-DN-354 | TC-AC-DN-E2E-118 | FE+BE |
| TC-AC-DN-355 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-356 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-357 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-358 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-359 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-360 | TC-AC-DN-E2E-120 | FE+BE |
| TC-AC-DN-361 | TC-AC-DN-E2E-120 | FE+BE |
| TC-AC-DN-362 | TC-AC-DN-E2E-120 | FE+BE |
| TC-AC-DN-363 | TC-AC-DN-E2E-120 | FE+BE |
| TC-AC-DN-364 | TC-AC-DN-E2E-120 | FE+BE |
| TC-AC-DN-365 | TC-AC-DN-E2E-164 | FE+BE |
| TC-AC-DN-366 | TC-AC-DN-E2E-164 | FE+BE |
| TC-AC-DN-367 | TC-AC-DN-E2E-164 | FE+BE |
| TC-AC-DN-368 | TC-AC-DN-E2E-039 | FE+BE |
| TC-AC-DN-369 | TC-AC-DN-E2E-164 | FE+BE |
| TC-AC-DN-370 | TC-AC-DN-E2E-165 | FE+BE |
| TC-AC-DN-371 | TC-AC-DN-E2E-165 | FE+BE |
| TC-AC-DN-372 | TC-AC-DN-E2E-165 | FE+BE |
| TC-AC-DN-373 | TC-AC-DN-E2E-165 | FE+BE |
| TC-AC-DN-374 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-375 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-376 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-377 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-378 | TC-AC-DN-E2E-164 | FE+BE |
| TC-AC-DN-379 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-380 | TC-AC-DN-E2E-166 | FE+BE |
| TC-AC-DN-381 | TC-AC-DN-E2E-121 | FE+BE |
| TC-AC-DN-382 | TC-AC-DN-E2E-121 | FE+BE |
| TC-AC-DN-383 | TC-AC-DN-E2E-121 | FE+BE |
| TC-AC-DN-384 | TC-AC-DN-E2E-121 | FE+BE |
| TC-AC-DN-385 | TC-AC-DN-E2E-122 | FE+BE |
| TC-AC-DN-386 | TC-AC-DN-E2E-122 | FE+BE |
| TC-AC-DN-387 | TC-AC-DN-E2E-122 | FE+BE |
| TC-AC-DN-388 | TC-AC-DN-E2E-125 | FE+BE |
| TC-AC-DN-389 | TC-AC-DN-E2E-125 | FE+BE |
| TC-AC-DN-390 | TC-AC-DN-E2E-125 | FE+BE |
| TC-AC-DN-391 | TC-AC-DN-E2E-125 | FE+BE |
| TC-AC-DN-392 | TC-AC-DN-E2E-125 | FE+BE |
| TC-AC-DN-393 | TC-AC-DN-E2E-126 | FE+BE |
| TC-AC-DN-394 | TC-AC-DN-E2E-126 | FE+BE |
| TC-AC-DN-395 | TC-AC-DN-E2E-126 | FE+BE |
| TC-AC-DN-396 | TC-AC-DN-E2E-126 | FE+BE |
| TC-AC-DN-397 | TC-AC-DN-E2E-127 | FE+BE |
| TC-AC-DN-398 | TC-AC-DN-E2E-127 | FE+BE |
| TC-AC-DN-399 | TC-AC-DN-E2E-127 | FE+BE |
| TC-AC-DN-400 | TC-AC-DN-E2E-127 | FE+BE |
| TC-AC-DN-401 | TC-AC-DN-E2E-127 | FE+BE |
| TC-AC-DN-402 | TC-AC-DN-E2E-128 | FE+BE |
| TC-AC-DN-403 | TC-AC-DN-E2E-009 | FE+BE |
| TC-AC-DN-404 | TC-AC-DN-E2E-035 | FE+BE |
| TC-AC-DN-405 | TC-AC-DN-E2E-128 | FE+BE |
| TC-AC-DN-406 | TC-AC-DN-E2E-129 | FE+BE |
| TC-AC-DN-407 | TC-AC-DN-E2E-129 | FE+BE |
| TC-AC-DN-408 | TC-AC-DN-E2E-129 | FE+BE |
| TC-AC-DN-409 | TC-AC-DN-E2E-129 | FE+BE |
| TC-AC-DN-410 | TC-AC-DN-E2E-129 | FE+BE |
| TC-AC-DN-411 | TC-AC-DN-E2E-130 | FE+BE |
| TC-AC-DN-412 | TC-AC-DN-E2E-130 | FE+BE |
| TC-AC-DN-413 | TC-AC-DN-E2E-130 | FE+BE |
| TC-AC-DN-414 | TC-AC-DN-E2E-130 | FE+BE |
| TC-AC-DN-415 | TC-AC-DN-E2E-130 | FE+BE |
| TC-AC-DN-416 | TC-AC-DN-E2E-131 | FE+BE |
| TC-AC-DN-417 | TC-AC-DN-E2E-131 | FE+BE |
| TC-AC-DN-418 | TC-AC-DN-E2E-131 | FE+BE |
| TC-AC-DN-419 | TC-AC-DN-E2E-131 | FE+BE |
| TC-AC-DN-420 | TC-AC-DN-E2E-132 | FE+BE |
| TC-AC-DN-421 | TC-AC-DN-E2E-132 | FE+BE |
| TC-AC-DN-422 | TC-AC-DN-E2E-132 | FE+BE |
| TC-AC-DN-423 | TC-AC-DN-E2E-133 | FE+BE |
| TC-AC-DN-424 | TC-AC-DN-E2E-133 | FE+BE |
| TC-AC-DN-425 | TC-AC-DN-E2E-133 | FE+BE |
| TC-AC-DN-426 | TC-AC-DN-E2E-133 | FE+BE |
| TC-AC-DN-427 | TC-AC-DN-E2E-133 | FE+BE |
| TC-AC-DN-428 | TC-AC-DN-E2E-134 | FE+BE |
| TC-AC-DN-429 | TC-AC-DN-E2E-134 | FE+BE |
| TC-AC-DN-430 | TC-AC-DN-E2E-134 | FE+BE |
| TC-AC-DN-431 | TC-AC-DN-E2E-134 | FE+BE |
| TC-AC-DN-432 | TC-AC-DN-E2E-134 | FE+BE |
| TC-AC-DN-433 | TC-AC-DN-E2E-135 | FE+BE |
| TC-AC-DN-434 | TC-AC-DN-E2E-135 | FE+BE |
| TC-AC-DN-435 | TC-AC-DN-E2E-135 | FE+BE |
| TC-AC-DN-436 | TC-AC-DN-E2E-135 | FE+BE |
| TC-AC-DN-437 | TC-AC-DN-E2E-135 | FE+BE |
| TC-AC-DN-438 | TC-AC-DN-E2E-136 | FE+BE |
| TC-AC-DN-439 | TC-AC-DN-E2E-136 | FE+BE |
| TC-AC-DN-440 | TC-AC-DN-E2E-136 | FE+BE |
| TC-AC-DN-441 | TC-AC-DN-E2E-136 | FE+BE |
| TC-AC-DN-442 | TC-AC-DN-E2E-136 | FE+BE |
| TC-AC-DN-443 | TC-AC-DN-E2E-137 | FE+BE |
| TC-AC-DN-444 | TC-AC-DN-E2E-137 | FE+BE |
| TC-AC-DN-445 | TC-AC-DN-E2E-138 | FE+BE |
| TC-AC-DN-446 | TC-AC-DN-E2E-138 | FE+BE |
| TC-AC-DN-447 | TC-AC-DN-E2E-138 | FE+BE |
| TC-AC-DN-448 | TC-AC-DN-E2E-132 | FE+BE |
| TC-AC-DN-449 | TC-AC-DN-E2E-009 | FE+BE |
| TC-AC-DN-450 | TC-AC-DN-E2E-140 | FE+BE |
| TC-AC-DN-451 | TC-AC-DN-E2E-140 | FE+BE |
| TC-AC-DN-452 | TC-AC-DN-E2E-140 | FE+BE |
| TC-AC-DN-453 | TC-AC-DN-E2E-140 | FE+BE |
| TC-AC-DN-454 | TC-AC-DN-E2E-141 | FE+BE |
| TC-AC-DN-455 | TC-AC-DN-E2E-141 | FE+BE |
| TC-AC-DN-456 | TC-AC-DN-E2E-141 | FE+BE |
| TC-AC-DN-457 | TC-AC-DN-E2E-141 | FE+BE |
| TC-AC-DN-458 | TC-AC-DN-E2E-142 | FE+BE |
| TC-AC-DN-459 | TC-AC-DN-E2E-142 | FE+BE |
| TC-AC-DN-460 | TC-AC-DN-E2E-142 | FE+BE |
| TC-AC-DN-461 | TC-AC-DN-E2E-143 | FE+BE |
| TC-AC-DN-462 | TC-AC-DN-E2E-143 | FE+BE |
| TC-AC-DN-463 | TC-AC-DN-E2E-150 | FE+BE |
| TC-AC-DN-464 | TC-AC-DN-E2E-144 | FE+BE |
| TC-AC-DN-465 | TC-AC-DN-E2E-144 | FE+BE |
| TC-AC-DN-466 | TC-AC-DN-E2E-144 | FE+BE |
| TC-AC-DN-467 | TC-AC-DN-E2E-144 | FE+BE |
| TC-AC-DN-468 | TC-AC-DN-E2E-145 | FE+BE |
| TC-AC-DN-469 | TC-AC-DN-E2E-145 | FE+BE |
| TC-AC-DN-470 | TC-AC-DN-E2E-145 | FE+BE |
| TC-AC-DN-471 | TC-AC-DN-E2E-145 | FE+BE |
| TC-AC-DN-472 | TC-AC-DN-E2E-146 | FE+BE |
| TC-AC-DN-473 | TC-AC-DN-E2E-146 | FE+BE |
| TC-AC-DN-474 | TC-AC-DN-E2E-146 | FE+BE |
| TC-AC-DN-475 | TC-AC-DN-E2E-146 | FE+BE |
| TC-AC-DN-476 | TC-AC-DN-E2E-147 | FE+BE |
| TC-AC-DN-477 | TC-AC-DN-E2E-147 | FE+BE |
| TC-AC-DN-478 | TC-AC-DN-E2E-149 | FE+BE |
| TC-AC-DN-479 | TC-AC-DN-E2E-149 | FE+BE |
| TC-AC-DN-480 | TC-AC-DN-E2E-147 | FE+BE |
| TC-AC-DN-481 | TC-AC-DN-E2E-147 | FE+BE |
| TC-AC-DN-482 | TC-AC-DN-E2E-148 | FE+BE |
| TC-AC-DN-483 | TC-AC-DN-E2E-149 | FE+BE |
| TC-AC-DN-484 | TC-AC-DN-E2E-149 | FE+BE |
| TC-AC-DN-485 | TC-AC-DN-E2E-149 | FE+BE |
| TC-AC-DN-486 | TC-AC-DN-E2E-148 | FE+BE |
| TC-AC-DN-487 | TC-AC-DN-E2E-039 | FE+BE |
| TC-AC-DN-488 | TC-AC-DN-E2E-152 | FE+BE |
| TC-AC-DN-489 | TC-AC-DN-E2E-157 | FE+BE |
| TC-AC-DN-490 | TC-AC-DN-E2E-157 | FE+BE |
| TC-AC-DN-491 | TC-AC-DN-E2E-152 | FE+BE |
| TC-AC-DN-492 | TC-AC-DN-E2E-153 | FE+BE |
| TC-AC-DN-493 | TC-AC-DN-E2E-153 | FE+BE |
| TC-AC-DN-494 | TC-AC-DN-E2E-153 | FE+BE |
| TC-AC-DN-495 | TC-AC-DN-E2E-154 | FE+BE |
| TC-AC-DN-496 | TC-AC-DN-E2E-155 | FE+BE |
| TC-AC-DN-497 | TC-AC-DN-E2E-158 | FE+BE |
| TC-AC-DN-498 | TC-AC-DN-E2E-158 | FE+BE |
| TC-AC-DN-499 | TC-AC-DN-E2E-155 | FE+BE |
| TC-AC-DN-500 | TC-AC-DN-E2E-155 | FE+BE |
| TC-AC-DN-501 | TC-AC-DN-E2E-159 | FE+BE |
| TC-AC-DN-502 | TC-AC-DN-E2E-159 | FE+BE |
| TC-AC-DN-503 | TC-AC-DN-E2E-160 | FE+BE |
| TC-AC-DN-504 | TC-AC-DN-E2E-160 | FE+BE |
| TC-AC-DN-505 | TC-AC-DN-E2E-160 | FE+BE |
| TC-AC-DN-506 | TC-AC-DN-E2E-152 | FE+BE |
| TC-AC-DN-507 | TC-AC-DN-E2E-154 | FE+BE |
| TC-AC-DN-508 | TC-AC-DN-E2E-154 | FE+BE |
| TC-AC-DN-509 | TC-AC-DN-E2E-161 | FE+BE |
| TC-AC-DN-510 | TC-AC-DN-E2E-161 | FE+BE |
| TC-AC-DN-511 | TC-AC-DN-E2E-161 | FE+BE |
| TC-AC-DN-512 | TC-AC-DN-E2E-159 | FE+BE |
| TC-AC-DN-513 | TC-AC-DN-E2E-162 | FE+BE |
| TC-AC-DN-514 | TC-AC-DN-E2E-163 | FE+BE |
| TC-AC-DN-515 | TC-AC-DN-E2E-163 | FE+BE |
| TC-AC-DN-516 | TC-AC-DN-E2E-162 | FE+BE |
| TC-AC-DN-517 | TC-AC-DN-E2E-162 | FE+BE |
| TC-AC-DN-518 | TC-AC-DN-E2E-170 | FE+BE |
| TC-AC-DN-519 | TC-AC-DN-E2E-170 | FE+BE |
| TC-AC-DN-520 | TC-AC-DN-E2E-170 | FE+BE |
| TC-AC-DN-521 | TC-AC-DN-E2E-170 | FE+BE |
| TC-AC-DN-522 | TC-AC-DN-E2E-171 | FE+BE |
| TC-AC-DN-523 | TC-AC-DN-E2E-171 | FE+BE |
| TC-AC-DN-524 | TC-AC-DN-E2E-171 | FE+BE |
| TC-AC-DN-525 | TC-AC-DN-E2E-171 | FE+BE |
| TC-AC-DN-526 | TC-AC-DN-E2E-024 | FE+BE |
| TC-AC-DN-527 | TC-AC-DN-E2E-172 | FE+BE |
| TC-AC-DN-528 | TC-AC-DN-E2E-172 | FE+BE |
| TC-AC-DN-529 | TC-AC-DN-E2E-172 | FE+BE |
| TC-AC-DN-530 | TC-AC-DN-E2E-172 | FE+BE |
| TC-AC-DN-531 | TC-AC-DN-E2E-172 | FE+BE |
| TC-AC-DN-532 | TC-AC-DN-E2E-173 | FE+BE |
| TC-AC-DN-533 | TC-AC-DN-E2E-173 | FE+BE |
| TC-AC-DN-534 | TC-AC-DN-E2E-176 | FE+BE |
| TC-AC-DN-535 | TC-AC-DN-E2E-176 | FE+BE |
| TC-AC-DN-536 | TC-AC-DN-E2E-176 | FE+BE |
| TC-AC-DN-537 | TC-AC-DN-E2E-078 | FE+BE |
| TC-AC-DN-538 | TC-AC-DN-E2E-176 | FE+BE |
| TC-AC-DN-539 | TC-AC-DN-E2E-029 | FE+BE |
| TC-AC-DN-540 | TC-AC-DN-E2E-029 | FE+BE |
| TC-AC-DN-541 | TC-AC-DN-E2E-029 | FE+BE |
| TC-AC-DN-542 | TC-AC-DN-E2E-029 | FE+BE |
| TC-AC-DN-543 | TC-AC-DN-E2E-030 | FE+BE |
| TC-AC-DN-544 | TC-AC-DN-E2E-030 | FE+BE |
| TC-AC-DN-545 | TC-AC-DN-E2E-041 | FE+BE |
| TC-AC-DN-546 | TC-AC-DN-E2E-041 | FE+BE |
| TC-AC-DN-547 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-548 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-549 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-550 | TC-AC-DN-E2E-031 | FE+BE |
| TC-AC-DN-551 | TC-AC-DN-E2E-031 | FE+BE |
| TC-AC-DN-552 | TC-AC-DN-E2E-031 | FE+BE |
| TC-AC-DN-553 | TC-AC-DN-E2E-031 | FE+BE |
| TC-AC-DN-554 | TC-AC-DN-E2E-031 | FE+BE |
| TC-AC-DN-555 | TC-AC-DN-E2E-032 | FE+BE |
| TC-AC-DN-556 | TC-AC-DN-E2E-032 | FE+BE |
| TC-AC-DN-557 | TC-AC-DN-E2E-032 | FE+BE |
| TC-AC-DN-558 | TC-AC-DN-E2E-032 | FE+BE |
| TC-AC-DN-559 | TC-AC-DN-E2E-119 | FE+BE |
| TC-AC-DN-560 | TC-AC-DN-E2E-090 | FE+BE |
| TC-AC-DN-561 | TC-AC-DN-E2E-033 | FE+BE |
| TC-AC-DN-562 | TC-AC-DN-E2E-033 | FE+BE |
| TC-AC-DN-563 | TC-AC-DN-E2E-033 | FE+BE |
| TC-AC-DN-564 | TC-AC-DN-E2E-033 | FE+BE |
| TC-AC-DN-565 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-566 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-567 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-568 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-569 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-570 | TC-AC-DN-E2E-034 | FE+BE |
| TC-AC-DN-571 | TC-AC-DN-E2E-187 | FE+BE |
| TC-AC-DN-572 | TC-AC-DN-E2E-186 | FE+BE |
| TC-AC-DN-573 | TC-AC-DN-E2E-181 | FE+BE |
| TC-AC-DN-574 | TC-AC-DN-E2E-183 | FE+BE |
| TC-AC-DN-575 | TC-AC-DN-E2E-183 | FE+BE |
| TC-AC-DN-576 | TC-AC-DN-E2E-186 | FE+BE |
| TC-AC-DN-577 | TC-AC-DN-E2E-046 | FE+BE |
| TC-AC-DN-578 | TC-AC-DN-E2E-037 | FE+BE |
| TC-AC-DN-579 | TC-AC-DN-E2E-185 | FE+BE |
| TC-AC-DN-580 | TC-AC-DN-E2E-185 | FE+BE |
| TC-AC-DN-581 | TC-AC-DN-E2E-185 | FE+BE |
| TC-AC-DN-582 | TC-AC-DN-E2E-180 | FE+BE |
| TC-AC-DN-583 | TC-AC-DN-E2E-044 | FE+BE |
| TC-AC-DN-584 | TC-AC-DN-E2E-044 | FE+BE |
| TC-AC-DN-585 | TC-AC-DN-E2E-055 | FE+BE |
| TC-AC-DN-586 | TC-AC-DN-E2E-042 | FE+BE |
| TC-AC-DN-587 | TC-AC-DN-E2E-056 | FE+BE |
| TC-AC-DN-588 | TC-AC-DN-E2E-057 | FE+BE |
| TC-AC-DN-589 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-590 | TC-AC-DN-E2E-065 | FE+BE |
| TC-AC-DN-591 | TC-AC-DN-E2E-071 | FE+BE |
| TC-AC-DN-592 | TC-AC-DN-E2E-097 | FE+BE |
| TC-AC-DN-593 | TC-AC-DN-E2E-093 | FE+BE |
| TC-AC-DN-594 | TC-AC-DN-E2E-099 | FE+BE |
| TC-AC-DN-595 | TC-AC-DN-E2E-096 | FE+BE |
| TC-AC-DN-596 | TC-AC-DN-E2E-006 | FE+BE |
| TC-AC-DN-597 | TC-AC-DN-E2E-003 | FE+BE |
| TC-AC-DN-598 | TC-AC-DN-E2E-013 | FE+BE |
| TC-AC-DN-599 | TC-AC-DN-E2E-021 | FE+BE |
| TC-AC-DN-600 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-601 | TC-AC-DN-E2E-025 | FE+BE |
| TC-AC-DN-602 | TC-AC-DN-E2E-103 | FE+BE |
| TC-AC-DN-603 | TC-AC-DN-E2E-112 | FE+BE |
| TC-AC-DN-604 | TC-AC-DN-E2E-122 | FE+BE |
| TC-AC-DN-605 | TC-AC-DN-E2E-167 | FE+BE |
| TC-AC-DN-606 | TC-AC-DN-E2E-092 | FE+BE |
| TC-AC-DN-607 | TC-AC-DN-E2E-167 | FE+BE |
| TC-AC-DN-608 | TC-AC-DN-E2E-167 | FE+BE |
| TC-AC-DN-609 | TC-AC-DN-E2E-072 | FE+BE |
| TC-AC-DN-610 | TC-AC-DN-E2E-073 | FE+BE |
| TC-AC-DN-611 | TC-AC-DN-E2E-073 | FE+BE |
| TC-AC-DN-612 | TC-AC-DN-E2E-081 | FE+BE |
| TC-AC-DN-613 | TC-AC-DN-E2E-082 | FE+BE |
| TC-AC-DN-614 | TC-AC-DN-E2E-084 | FE+BE |
| TC-AC-DN-615 | TC-AC-DN-E2E-156 | FE+BE |
| TC-AC-DN-616 | TC-AC-DN-E2E-094 | FE+BE |
| TC-AC-DN-617 | TC-AC-DN-E2E-097 | FE+BE |
| TC-AC-DN-618 | TC-AC-DN-E2E-035 | FE+BE |
| TC-AC-DN-619 | TC-AC-DN-E2E-021 | FE+BE |
| TC-AC-DN-620 | TC-AC-DN-E2E-021 | FE+BE |
| TC-AC-DN-621 | TC-AC-DN-E2E-074 | FE+BE |
| TC-AC-DN-622 | TC-AC-DN-E2E-010 | FE+BE |
| TC-AC-DN-623 | TC-AC-DN-E2E-010 | FE+BE |
| TC-AC-DN-624 | TC-AC-DN-E2E-173 | FE+BE |
| TC-AC-DN-625 | TC-AC-DN-E2E-185 | FE+BE |
| TC-AC-DN-626 | TC-AC-DN-E2E-022 | FE+BE |
| TC-AC-DN-627 | TC-AC-DN-E2E-029 | FE+BE |
| TC-AC-DN-628 | TC-AC-DN-E2E-011 | FE+BE |
| TC-AC-DN-629 | TC-AC-DN-E2E-014 | FE+BE |
| TC-AC-DN-630 | TC-AC-DN-E2E-092 | FE+BE |
| TC-AC-DN-631 | TC-AC-DN-E2E-093 | FE+BE |
| TC-AC-DN-632 | TC-AC-DN-E2E-094 | FE+BE |
| TC-AC-DN-633 | TC-AC-DN-E2E-095 | FE+BE |
| TC-AC-DN-634 | TC-AC-DN-E2E-095 | FE+BE |
| TC-AC-DN-635 | TC-AC-DN-E2E-096 | FE+BE |
| TC-AC-DN-636 | TC-AC-DN-E2E-096 | FE+BE |
| TC-AC-DN-637 | TC-AC-DN-E2E-106 | FE+BE |
| TC-AC-DN-638 | TC-AC-DN-E2E-139 | FE+BE |
| TC-AC-DN-639 | TC-AC-DN-E2E-098 | FE+BE |
| TC-AC-DN-640 | TC-AC-DN-E2E-174 | FE+BE |
| TC-AC-DN-641 | TC-AC-DN-E2E-174 | FE+BE |
| TC-AC-DN-642 | TC-AC-DN-E2E-004 | FE+BE |
| TC-AC-DN-643 | TC-AC-DN-E2E-086 | FE+BE |
| TC-AC-DN-644 | TC-AC-DN-E2E-015 | FE+BE |
| TC-AC-DN-645 | TC-AC-DN-E2E-015 | FE+BE |
| TC-AC-DN-646 | TC-AC-DN-E2E-023 | FE+BE |
| TC-AC-DN-647 | TC-AC-DN-E2E-016 | FE+BE |
| TC-AC-DN-648 | TC-AC-DN-E2E-016 | FE+BE |
| TC-AC-DN-649 | TC-AC-DN-E2E-016 | FE+BE |
| TC-AC-DN-650 | TC-AC-DN-E2E-175 | FE+BE |
| TC-AC-DN-651 | TC-AC-DN-E2E-175 | FE+BE |
| TC-AC-DN-652 | TC-AC-DN-E2E-097 | FE+BE |
| TC-AC-DN-653 | TC-AC-DN-E2E-017 | FE+BE |
| TC-AC-DN-654 | TC-AC-DN-E2E-017 | FE+BE |
| TC-AC-DN-655 | TC-AC-DN-E2E-030 | FE+BE |
| TC-AC-DN-656 | TC-AC-DN-E2E-177 | FE+BE |
| TC-AC-DN-657 | TC-AC-DN-E2E-178 | FE+BE |
| TC-AC-DN-658 | TC-AC-DN-E2E-177 | FE+BE |
| TC-AC-DN-659 | TC-AC-DN-E2E-090 | FE+BE |
| TC-AC-DN-660 | TC-AC-DN-E2E-090 | FE+BE |
| TC-AC-DN-661 | TC-AC-DN-E2E-178 | FE+BE |
| TC-AC-DN-662 | TC-AC-DN-E2E-090 | FE+BE |
