# Coverage E2E — Fixed Asset > Settings > Categories

Sumber: `fixed-asset/settings-categories/TestCases/tc-settings-categories.md` (703 TC `TC-FA-CAT-1`–`703`, semua aktif). Suite: `specs/FixedAsset/SettingsCategories/`. Prefix: `FA` + `CAT` (`TC-FA-CAT-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). `tc-settings-categories-backend.md` memakai id sendiri (`TC-FA-CAT-BE-NNN`) dan tidak merujuk id TC granular.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 703 TC aktif masuk 203 spec, tidak ada TC hanya-BE. Setiap TC yang masuk terpetakan ke satu spec; TC 497–502 dan 579 juga muncul di spec absence kelas g (`168`) dengan asersi log (S-05).

## TC hanya-BE (tidak masuk spec)

Tidak ada. TC defense-in-depth dengan Expected respons API (497–503, 579, 681) tetap masuk spec FE+BE dengan butir K-1.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-CAT-E2E-001-screening-halaman-categories-list | Screening Halaman Categories List: Breadcrumb, Sidebar Category Tree, dan Loading | FE+BE | 49 | 1, 2, 3, 4, 12, 25 |
| TC-FA-CAT-E2E-002-navigasi-sidebar-tree-dan-context-header | Perilaku Klik Node Sidebar, Category Context Header, dan Empty State Leaf | FE+BE | 30 | 5, 6, 7, 8, 9 |
| TC-FA-CAT-E2E-003-tabel-categories-list-kolom-row-action-tooltip | Tabel Categories List: Kolom, Row Action, Bulk Action Bar, Total Asset, dan Tooltip Table Tools | FE+BE | 47 | 14, 15, 16, 17, 11 |
| TC-FA-CAT-E2E-004-sidebar-collapse-state-tersimpan-tablet-aksesibilitas | Sidebar Collapse, State Tersimpan, Viewport Tablet, dan Aksesibilitas Pohon Kategori | FE+BE | 28 | 19, 18, 20, 21 |
| TC-FA-CAT-E2E-005-client-baru-onboard-seed-default-category | Client Baru Onboard: Seed Default Category, Changelog Kosong, dan Edit Seed | FE+BE | 35 | 10, 392, 616, 581 |
| TC-FA-CAT-E2E-006-node-excess-sidebar-tabel-alert-blokir-d01 | Node Excess: Sidebar, Tabel, Alert Consolidation, Menu, dan Blokir D-01 | FE+BE | 34 | 22, 23, 24, 316, 317, 320 |
| TC-FA-CAT-E2E-007-guided-tooltip-categories-walkthrough | Guided Tooltip Categories: Kunjungan Pertama, Navigasi, dan Flag Seen | FE+BE | 53 | 27, 28, 29, 30, 31 |
| TC-FA-CAT-E2E-008-walkthrough-saat-sidebar-collapsed-atau-terbuka | Walkthrough dengan Sidebar Collapsed dan Terbuka (Desktop) | FE+BE | 31 | 644, 639, 641, 643 |
| TC-FA-CAT-E2E-009-kontras-badge-dan-chip-wcag | Kontras Badge dan Chip Memenuhi WCAG 2.1 AA (Manual Only) | FE+BE | 16 | 638 |
| TC-FA-CAT-E2E-010-mobile-android-card-list-bottom-sheet-selection-walkthrough | Mobile Android: Card List, Bottom Sheet Tree, Selection Mode, dan Walkthrough | FE+BE | 33 | 26, 270, 640, 642 |
| TC-FA-CAT-E2E-011-role-matrix-visibilitas-total-control-read-only-capability-read | Role Matrix: Visibilitas Elemen Categories List (Total Control, Read Only, Capability Read) | FE+BE | 36 | 32, 33, 34 |
| TC-FA-CAT-E2E-012-role-matrix-visibilitas-create-only-update-only-delete-only | Role Matrix: Visibilitas Elemen Categories List (Create-Only, Update-Only, Delete-Only) | FE+BE | 37 | 35, 36, 37 |
| TC-FA-CAT-E2E-013-role-matrix-visibilitas-cud-gm-tanpa-capability-url-langsung | Role Matrix: Visibilitas Elemen Categories List (CUD, Group Manager CRUD), Tanpa Capability, dan URL Langsung | FE+BE | 46 | 38, 39, 40, 41, 42 |
| TC-FA-CAT-E2E-014-role-matrix-positif-create-dan-update-per-capability | Role Matrix Positif: Create dan Update Kategori per Capability | FE+BE | 38 | 43, 44, 45, 48 |
| TC-FA-CAT-E2E-015-role-matrix-positif-delete-dan-bulk-delete-delete-only | Role Matrix Positif: Delete dan Bulk Delete oleh Delete-Only | FE+BE | 20 | 46, 47 |
| TC-FA-CAT-E2E-016-role-matrix-negatif-read-only-dan-scope-group-manager | Role Matrix Negatif: Read Only Tanpa Aksi Tulis dan Group Manager Melihat Seluruh Pohon Client | FE+BE | 14 | 49, 57 |
| TC-FA-CAT-E2E-017-role-matrix-row-action-node-excess-dan-alert-consolidation | Role Matrix: Row Action Node Excess dan Alert Category Consolidation per Role | FE+BE | 32 | 50, 51, 52, 53, 54, 55, 56 |
| TC-FA-CAT-E2E-018-new-category-screening-aksesibilitas-dan-saving-state | New Category: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit | FE+BE | 28 | 58, 60, 61 |
| TC-FA-CAT-E2E-019-new-subcategory-screening-aksesibilitas-dan-saving-state | New Subcategory: Screening Popup, Aksesibilitas, dan Saving State Tombol Submit | FE+BE | 23 | 59, 624, 627 |
| TC-FA-CAT-E2E-020-new-category-clear-field-tutup-bersih-dirty-dan-backdrop | New Category: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop | FE+BE | 36 | 62, 64, 65, 66, 67 |
| TC-FA-CAT-E2E-021-new-subcategory-clear-field-tutup-bersih-dirty-dan-backdrop | New Subcategory: Clear Field, Tutup Popup Bersih dan Terisi (Unsaved Changes), serta Klik Backdrop | FE+BE | 35 | 63, 68, 69, 70, 71 |
| TC-FA-CAT-E2E-022-form-dirty-refresh-f5-dan-pindah-route-spa-category | Form New Category Dirty: Refresh F5 dan Pindah Route SPA | FE+BE | 20 | 72, 73 |
| TC-FA-CAT-E2E-023-keyboard-form-esc-enter-dan-default-checkbox-stay | Keyboard Form (Esc dan Enter) dan Default Checkbox Stay on This Form | FE+BE | 29 | 74, 75, 76, 113 |
| TC-FA-CAT-E2E-024-new-category-validasi-category-name-wajib-spasi-panjang-trim | New Category: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim | FE+BE | 34 | 77, 78, 80, 85, 79 |
| TC-FA-CAT-E2E-025-new-category-karakter-name-duplikat-sibling-case-insensitive | New Category: Karakter Category Name, Duplikat Sibling, dan Pencocokan Case-Insensitive | FE+BE | 30 | 87, 88, 89, 90, 92, 93 |
| TC-FA-CAT-E2E-026-new-category-reserved-word-dan-validasi-code | New Category: Reserved Word pada Category Name dan Validasi Code (Panjang, Whitelist, Duplikat) | FE+BE | 28 | 94, 95, 96, 97, 98, 99 |
| TC-FA-CAT-E2E-027-new-category-uppercase-code-helper-text-dan-batas-description | New Category: Helper Text Code, Uppercase Otomatis Code, dan Batas Description 360 Karakter | FE+BE | 23 | 106, 105, 100 |
| TC-FA-CAT-E2E-028-new-subcategory-validasi-category-name-wajib-spasi-panjang-trim | New Subcategory: Validasi Category Name Wajib, Hanya Spasi, Batas Panjang 120, dan Trim | FE+BE | 37 | 81, 82, 83, 84, 519 |
| TC-FA-CAT-E2E-029-new-subcategory-karakter-duplikat-dan-reserved-word-name | New Subcategory: Karakter Simbol, Duplikat Nama Tanpa Beda Huruf dan Trim, serta Reserved Word pada Category Name | FE+BE | 27 | 520, 521, 522, 523 |
| TC-FA-CAT-E2E-030-new-subcategory-validasi-code-description-dan-duplikat-sibling | New Subcategory: Duplikat Nama Sibling, Duplikat Code, Whitelist Code, serta Batas Panjang Code dan Description | FE+BE | 42 | 91, 101, 102, 103, 104 |
| TC-FA-CAT-E2E-031-new-subcategory-uppercase-code-helper-text-trim-emoji-reserved-word | New Subcategory: Uppercase Code, Helper Text, Trim, Emoji, Reserved Word, dan Description Bebas | FE+BE | 34 | 524, 525, 526, 141, 142, 143, 144 |
| TC-FA-CAT-E2E-032-create-kategori-root-code-auto-manual-dan-urutan-az | Create Kategori Root: Code Auto-generate, Code Manual, Urutan Category A-Z | FE+BE | 30 | 108, 109, 110, 164 |
| TC-FA-CAT-E2E-033-add-subcategory-sukses-leaf-ke-internal-dan-keluar-empty-state | Add Subcategory Sukses: Leaf Menjadi Internal, Aset Existing Tidak Berubah, dan Keluar dari Empty State | FE+BE | 33 | 111, 112, 530 |
| TC-FA-CAT-E2E-034-stay-on-this-form-create-dan-add-subcategory | Stay on This Form: Create Kategori Root dan Add Subcategory Mempertahankan Popup, Banner, dan Parent | FE+BE | 29 | 114, 115 |
| TC-FA-CAT-E2E-035-batas-count-plan-starter-dialog-blok-d-01 | Batas Category Count Plan Starter: Dialog Blok D-01 pada Cap dan Create Lolos di Bawah Cap | FE+BE | 22 | 117, 118, 119, 120 |
| TC-FA-CAT-E2E-036-urutan-guard-count-depth-plan-starter-dan-guard-d-05 | Urutan Guard Plan Starter: Depth D-02, Count D-01 Mendahului Depth, dan Guard Mendahului Heads-up D-05 | FE+BE | 13 | 124, 125, 650 |
| TC-FA-CAT-E2E-037-batas-depth-plan-catdeep-guard-depth-diblok-d-02 | Batas Depth Plan CatDeep: Depth 5 Lolos dan Depth Melebihi Cap Diblok D-02 | FE+BE | 19 | 122, 649, 121 |
| TC-FA-CAT-E2E-038-batas-depth-plan-growth-dan-happy-path-lintas-tier-plan | Batas Depth Plan Growth dan Happy Path Create, Edit, Delete Identik Lintas Tier Plan | FE+BE | 19 | 123, 129 |
| TC-FA-CAT-E2E-039-system-limits-master-data-count-dan-pembacaan-live | System Limits: Dialog D-03 Master Data Count Limit, Plan Enterprise, dan Pembacaan Live | FE+BE | 20 | 126, 128, 489 |
| TC-FA-CAT-E2E-040-system-limits-diturunkan-di-bawah-data-existing | System Limits Diturunkan di Bawah Data Existing: Non-retroaktif, Tanpa Excess, Hanya Add yang Diblok | FE+BE | 35 | 582 |
| TC-FA-CAT-E2E-041-heads-up-d-05-add-subcategory-pada-leaf-ditunjuk-asset-name | Heads-up D-05 pada Add Subcategory untuk Leaf yang Ditunjuk Asset Name: Isi Dialog, Cancel, Backdrop dan Esc, Daftar Panjang, dan Hasil Submit | FE+BE | 55 | 130, 131, 132, 647, 648, 134, 133 |
| TC-FA-CAT-E2E-042-klik-ganda-cepat-submit-save-delete | Klik Ganda Cepat pada Submit, Save, Delete, dan Bulk Delete Hanya Menjalankan Aksi Sekali | FE+BE | 42 | 140, 629, 208, 237, 268 |
| TC-FA-CAT-E2E-043-izin-dicabut-saat-popup-create-edit-delete-terbuka | Izin Dicabut Saat Popup Create, Popup Edit, dan Dialog Delete Terbuka: Aksi Ditolak 403 dan UI Di-refresh | FE+BE (backend nyata; pencabutan capability dilakukan Principal Automation lewat sesi API, tanpa intercept) | 38 | 527, 209, 539 |
| TC-FA-CAT-E2E-044-plan-dan-limit-berubah-saat-popup-subcategory-dan-wizard-terbuka | Plan atau Limit Berubah Saat Popup New Subcategory dan Popup Consolidation Terbuka: Submit Ditolak Server | FE+BE (backend nyata; perubahan plan, Hierarchy Depth Limit, dan cap Category count dilakukan Principal Automation lewat sesi API, tanpa intercept) | 38 | 528, 529, 301 |
| TC-FA-CAT-E2E-045-resilience-create-dan-add-subcategory-5xx-dan-timeout | Resilience Create dan Add Subcategory: Respons 5xx dan Timeout Jaringan Mempertahankan Popup dan Input | FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra | 52 | 139, 167, 577, 628 |
| TC-FA-CAT-E2E-046-resilience-baca-list-asset-popup-dan-changelog-bagian-1 | Resilience Baca Bagian 1: Error Load List Kategori, Loading dan Error Tabel Assets Popup Detail, serta Changelog | FE+BE (intercept parsial di atas backend nyata; respons baca list kategori, data aset Popup Detail, dan Changelog ditahan atau dipaksa 5xx lewat `Spectra | 33 | 13, 287, 415 |
| TC-FA-CAT-E2E-047-resilience-baca-asset-name-add-subcategory-dan-wizard-bagian-2 | Resilience Baca Bagian 2: Fetch Asset Name Saat Add Subcategory (5xx dan Timeout) serta Error Load Tabel Wizard Consolidation | FE+BE (intercept parsial di atas backend nyata; respons pengambilan daftar Asset Name dan data tabel Wizard dipaksa 5xx atau tanpa respons lewat `Spectra | 38 | 645, 646, 454 |
| TC-FA-CAT-E2E-048-race-dua-sesi-ui-create-dan-add-subcategory | Race Dua Sesi UI pada Create dan Add Subcategory: Slot Terakhir, Batas Platform, Name Sama, dan Code Sama | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) | 58 | 135, 136, 137, 138, 165, 630 |
| TC-FA-CAT-E2E-049-edit-screening-popup-dan-penutupan-bersih-dirty-backdrop | Edit Category: Screening Popup Edit, Penutupan Bersih dan Dirty, Backdrop, serta Revert Perubahan | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) | 49 | 170, 173, 174, 575, 175, 176 |
| TC-FA-CAT-E2E-050-edit-clear-field-saving-state-move-tidak-didukung-refresh-dan-route-dirty | Edit Category: Saving State, Clear Field, Move Tidak Didukung, serta Refresh F5 dan Pindah Route Saat Form Dirty | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra | 53 | 171, 172, 203, 620, 621 |
| TC-FA-CAT-E2E-051-edit-validasi-category-name | Edit Category: Validasi Category Name (Kosong, Spasi, Batas 120 Karakter, Trim) | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) | 38 | 177, 178, 179, 180, 538, 531 |
| TC-FA-CAT-E2E-052-edit-validasi-emoji-duplikat-reserved-word-dan-nama-sendiri | Edit Category: Emoji, Nama Duplikat Sibling, Reserved Word All Categories, dan Nama Sendiri | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) | 32 | 181, 182, 183, 184, 185, 533, 534 |
| TC-FA-CAT-E2E-053-edit-validasi-code-dan-description | Edit Category: Validasi Code (Helper Text, Batas 15 Karakter, Whitelist, Duplikat, Uppercase) dan Batas Description 360 Karakter | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) | 39 | 536, 186, 187, 188, 189, 190 |
| TC-FA-CAT-E2E-054-edit-karakter-spasi-tengah-description-bebas-dan-nama-sama-parent-berbeda | Edit Category: Reserved Word dengan Dua Spasi, Karakter Bebas pada Description dan Name, serta Nama Sama di Parent Berbeda | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE) | 35 | 535, 537, 532, 632 |
| TC-FA-CAT-E2E-055-edit-sukses-name-code-description-bagian-1 | Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 1) | FE+BE | 27 | 193, 194, 195 |
| TC-FA-CAT-E2E-056-edit-sukses-name-code-description-bagian-2 | Edit Sukses: Name, Code, Description, dan Snapshot Changelog (Bagian 2) | FE+BE | 34 | 196, 197, 198 |
| TC-FA-CAT-E2E-057-edit-refleksi-detail-code-kosong-modified-by-bagian-1 | Edit: Refleksi Popup Detail, Code Kosong Auto-generate, dan Dedup Edit (Bagian 1) | FE+BE | 36 | 199, 200, 202 |
| TC-FA-CAT-E2E-058-edit-refleksi-detail-code-kosong-modified-by-bagian-2 | Edit: Aksesibilitas Popup, Modified By dan Last Updated, serta Node Dihapus User Lain (Bagian 2) | FE+BE | 40 | 625, 204, 206 |
| TC-FA-CAT-E2E-059-race-dua-sesi-edit-bersamaan-dan-rename-name-sama | Race Dua Sesi UI: Edit Bersamaan pada Record Sama dan Rename ke Name yang Sama | FE+BE | 46 | 205, 578 |
| TC-FA-CAT-E2E-060-resilience-edit-dan-delete-single-5xx-dan-timeout | Resilience Edit dan Delete Single: 5xx dan Timeout | FE+BE | 44 | 207, 211, 236, 240 |
| TC-FA-CAT-E2E-061-auto-generate-code-token-whitelist-potong-15-karakter-bagian-1 | Auto-generate Code: Token Alfabetik, Numerik Murni, dan Campuran (Bagian 1) | FE+BE | 27 | 145, 146, 147 |
| TC-FA-CAT-E2E-062-auto-generate-code-token-whitelist-potong-15-karakter-bagian-2 | Auto-generate Code: Pemisah Token dan Fallback 6 Karakter (Bagian 2) | FE+BE | 18 | 148, 149 |
| TC-FA-CAT-E2E-063-auto-generate-code-karakter-khusus-beraksen-numerik-bagian-1 | Auto-generate Code: Nama Satu Karakter, Karakter Khusus, dan Huruf Beraksen (Bagian 1) | FE+BE | 27 | 150, 151, 152 |
| TC-FA-CAT-E2E-064-auto-generate-code-karakter-khusus-beraksen-numerik-bagian-2 | Auto-generate Code: Nama Numerik Murni dan Pemotongan 15 Karakter (Bagian 2) | FE+BE | 18 | 153, 154 |
| TC-FA-CAT-E2E-065-auto-generate-code-dedup-tier-1-dan-tier-2 | Auto-generate Code: Dedup Tier 1 (Suffix Angka) dan Beralih ke Tier 2 (Prefix Parent Code) | FE+BE | 42 | 155, 156, 157, 158 |
| TC-FA-CAT-E2E-066-auto-generate-code-tier-2-lanjut-root-ruang-suffix-literal-cat-bagian-1 | Auto-generate Code: Tier 2 Lanjut Suffix, Kategori Root, dan Prefix Parent Tanpa Ruang (Bagian 1) | FE+BE | 33 | 159, 160, 161 |
| TC-FA-CAT-E2E-067-auto-generate-code-tier-2-lanjut-root-ruang-suffix-literal-cat-bagian-2 | Auto-generate Code: Suffix Tidak Dipotong dan Literal CAT (Bagian 2) | FE+BE | 25 | 162, 163 |
| TC-FA-CAT-E2E-068-delete-single-dialog-cancel-elipsis-sidebar-esc-focus-trap | Delete Single: Dialog Konfirmasi, Cancel, Esc, Focus Trap, dan Delete dari Elipsis Sidebar | FE+BE | 43 | 212, 238, 626, 214, 633, 215 |
| TC-FA-CAT-E2E-069-delete-diblok-in-use-d-07-asset-name-menunjuk-saat-dialog | Delete Diblok In-Use (D-07): Bentuk Jamak dan Tunggal, Descendant, Node Excess, dan Asset Name Menunjuk Saat Dialog | FE+BE | 43 | 220, 221, 222, 226, 233, 228 |
| TC-FA-CAT-E2E-070-delete-diblok-would-empty-d-06-catfresh-dan-catdeep | Delete Diblok Would-Empty (D-06 dan D-10): Client CatFresh dan CatDeep | FE+BE | 39 | 223, 259, 225, 256, 224, 255 |
| TC-FA-CAT-E2E-071-would-empty-catthree-delete-bulk-dan-race | Would-Empty CatThree: Bulk Delete Seluruh Kategori Diblok D-10, Race Bulk Delete dan Delete Tunggal Ditolak 409 | FE+BE | 24 | 254, 235, 264 |
| TC-FA-CAT-E2E-072-delete-node-excess-cascade-reset-otomatis-batas-cap | Delete pada Node Excess: Cascade ke Descendant Excess, Reset Otomatis Excess saat Jumlah Mencapai Cap, dan Batas Cap | FE+BE | 42 | 219, 227, 231, 232, 261 |
| TC-FA-CAT-E2E-073-delete-sukses-leaf-family-cascade-pakai-ulang-code | Delete Sukses: Dialog D-08 Tunggal dan Jamak, Delete Leaf, Delete Family Tiga Level, dan Pakai Ulang Code | FE+BE | 31 | 216, 217, 218, 213, 229 |
| TC-FA-CAT-E2E-074-delete-seleksi-changelog-snapshot-empty-state-dihapus-user-lain | Delete: Seleksi Sidebar, Snapshot Path Changelog, Transisi ke Empty State, dan Node yang Dihapus User Lain | FE+BE | 37 | 230, 239, 540, 234 |
| TC-FA-CAT-E2E-075-bulk-delete-homogen-bulk-bar-dialog-d11-hitungan-descendant | Bulk Delete Homogen: Bulk Action Bar, Dialog D-11, Hitungan Descendant, dan Toast T-07 | FE+BE | 36 | 241, 247, 248, 249 |
| TC-FA-CAT-E2E-076-bulk-delete-checkbox-header-select-all-retensi-seleksi | Bulk Delete: Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi saat Pindah Halaman, Search, Filter, dan Sort | FE+BE | 36 | 242, 243, 244 |
| TC-FA-CAT-E2E-077-selection-limit-limit-plus-satu-dan-auto-cap-lintas-node | Selection Limit: Checkbox Limit+1 Disabled, Select All Melebihi Limit Di-cap Otomatis, dan Hitungan Lintas Node Sidebar | FE+BE | 30 | 245, 246, 574 |
| TC-FA-CAT-E2E-078-bulk-delete-campuran-skipped-blokir-total-collapse-single | Bulk Delete Campuran: Dialog D-12 dengan Kelompok Skipped, Blokir Total D-13, dan Collapse ke Dialog Single | FE+BE | 39 | 250, 251, 252, 253, 257 |
| TC-FA-CAT-E2E-079-bulk-delete-collapse-d07-cancel-counter-dan-log | Bulk Delete: Collapse ke Dialog D-07, Cancel Tidak Mereset Seleksi, Seleksi 0 Setelah Commit, dan Log per Node | FE+BE | 37 | 258, 634, 266, 267, 269 |
| TC-FA-CAT-E2E-080-bulk-delete-seleksi-lintas-node-baris-dihapus-user-lain-semua-terblok | Bulk Delete: Seleksi Lintas Node Sidebar, Semua Baris Menjadi Terblok saat Eksekusi, dan Baris Dihapus User Lain | FE+BE | 35 | 573, 263, 265 |
| TC-FA-CAT-E2E-081-popup-detail-screening-pembukaan-total-asset-dan-empty-state | Popup Detail Category: Screening Header dan Body, Tiga Jalur Pembukaan, Total Asset Header, dan Empty State Total Asset 0 | FE+BE | 31 | 272, 273, 274, 275 |
| TC-FA-CAT-E2E-082-popup-detail-empty-terfilter-description-kosong-excess-dan-tabel-assets | Popup Detail Category: Empty State Terfilter, Description Kosong, Node Excess, dan Isi Tabel Assets Exact-Match | FE+BE | 24 | 276, 277, 282, 281 |
| TC-FA-CAT-E2E-083-popup-detail-tautan-name-per-akses-dan-node-dihapus-user-lain | Popup Detail Category: Tautan Kolom Name per Akses Aktor dan Pembukaan Popup untuk Node yang Dihapus User Lain | FE+BE | 38 | 283, 284, 285, 635 |
| TC-FA-CAT-E2E-084-wizard-consolidation-screening-counter-save-selection-keep-usable | Wizard Category Consolidation: Screening Popup, Counter Keep usable, Save Selection, Retensi Centang, dan Klik Ganda | FE+BE | 44 | 288, 289, 290, 291, 297, 543 |
| TC-FA-CAT-E2E-085-wizard-submit-pasca-t0-diterapkan-seketika-submit-sebagian-dan-penuh | Wizard Consolidation Pasca-T-0: Save Selection Diterapkan Seketika, Submit Satu Centang, dan Submit Sebanyak Cap | FE+BE | 33 | 292, 294, 295 |
| TC-FA-CAT-E2E-086-wizard-tutup-popup-dirty-dialog-unsaved-changes-leave-dan-backdrop | Wizard Consolidation: Menutup Popup dengan Centang Berubah, Dialog Unsaved Changes, [Leave], dan Backdrop | FE+BE | 21 | 298, 576, 299 |
| TC-FA-CAT-E2E-087-wizard-refresh-f5-dan-pindah-route-spa-saat-centang-berubah | Wizard Consolidation: Refresh F5 dan Pindah Route SPA saat Centang Berubah | FE+BE | 21 | 622, 623 |
| TC-FA-CAT-E2E-088-wizard-aset-tidak-dipindahkan-submit-setelah-t0-dan-delete-sesi-lain | Wizard Consolidation: Aset Tidak Dipindahkan, Submit Setelah T-0 Diterapkan Langsung, dan Submit Setelah Delete Sesi Lain | FE+BE | 32 | 312, 304, 302 |
| TC-FA-CAT-E2E-089-wizard-pra-t0-save-selection-cap-baru-dan-penerapan-seleksi-di-t0 | Wizard Pra-T-0 CatPreT0: Batas Cap Plan Baru, Save Selection Hanya Menyimpan, dan Penerapan Seleksi di T-0 | FE+BE | 24 | 306, 305, 307 |
| TC-FA-CAT-E2E-090-wizard-pra-t0-seleksi-dibuang-atau-diubah-sebelum-t0-kategori-dihapus-dan-ditambah | Wizard Pra-T-0: Seleksi Dibuang atau Diubah Sebelum T-0 karena Kategori Dihapus atau Ditambah | FE+BE | 53 | 601, 602, 603 |
| TC-FA-CAT-E2E-091-wizard-pra-t0-seleksi-kosong-downgrade-dibatalkan-dan-plan-target-naik | Wizard Pra-T-0: Seleksi Kosong, Downgrade Dibatalkan, dan Plan Target Naik Sebelum T-0 | FE+BE | 46 | 604, 605, 606 |
| TC-FA-CAT-E2E-092-wizard-pra-t0-plan-target-turun-submit-ulang-dan-siklus-downgrade-baru | Wizard Pra-T-0: Plan Target Turun, Submit Ulang, dan Siklus Downgrade Baru | FE+BE | 65 | 607, 608, 609, 610 |
| TC-FA-CAT-E2E-093-penerapan-seleksi-di-t0-pada-suspended-expired-dan-log-penyubmit-terakhir | Penerapan Seleksi Tersimpan di T-0 pada Client Suspended atau Expired dan Log Penyubmit Terakhir | FE+BE | 42 | 611, 612 |
| TC-FA-CAT-E2E-094-siklus-excess-plan-naik-melepas-excess-dan-log-restored | Siklus Excess: Plan Naik Melepas Excess dan Log Restored from Excess pada Tiga Surface | FE+BE | 53 | 314, 472, 471, 470, 315 |
| TC-FA-CAT-E2E-095-state-tenant-suspended-expired-wizard-ditolak-fallback-t0-dan-reset-plan-naik | State Tenant Suspended: Wizard Submit Ditolak, Fallback T-0 Tetap Berjalan, dan Reset Excess saat Plan Naik | FE+BE | 37 | 303, 319, 544 |
| TC-FA-CAT-E2E-096-search-toolbar-tabel-utama-reveal-enter-kolom-teks-angka-dan-modified-by | Search Toolbar Tabel Utama: Reveal, Enter, Kolom Teks, dan Kolom Angka | FE+BE | 32 | 321, 322, 323, 324, 325 |
| TC-FA-CAT-E2E-097-search-toolbar-guard-last-updated-visibilitas-kolom-node-lokal-trim-dan-karakter-khusus | Search Toolbar: Modified By, Guard Last Updated, Visibilitas Kolom, Trim, Karakter Khusus, dan Pencarian Lokal Node | FE+BE | 25 | 326, 327, 328, 330, 331, 329 |
| TC-FA-CAT-E2E-098-filter-tabel-utama-panel-range-total-asset-modified-by-dan-chip | Filter Tabel Utama: Screening Panel, Range Total Asset, Modified By Multi-select, dan Sinkronisasi Chip | FE+BE | 46 | 332, 333, 334, 335, 336, 337 |
| TC-FA-CAT-E2E-099-filter-tabel-utama-last-updated-draft-badge-independen-kolom-dan-opsi-dinamis | Filter Tabel Utama: Chip +N more, Last Updated, Logika AND, Draft Dibuang, Badge, Independen Kolom, Reset Paginasi, dan Opsi Dinamis | FE+BE | 61 | 338, 339, 340, 341, 342, 343, 345, 344 |
| TC-FA-CAT-E2E-100-sort-3-state-tabel-utama | Sort 3-State Tabel Utama: Kolom Category, Code, Modified By, Total Asset, dan Last Updated | FE+BE | 31 | 346, 347, 348, 349 |
| TC-FA-CAT-E2E-101-sort-tie-breaker-pindah-kolom-dan-kolom-tanpa-sort | Sort: Tie-Breaker Antar Halaman, Pindah Kolom Sort, dan Kolom Tanpa Ikon Sort | FE+BE | 15 | 350, 351, 352 |
| TC-FA-CAT-E2E-102-setup-column-tabel-utama-overlay-popup-dan-ceklis-kolom | Setup Column Tabel Utama: Overlay Column Visibility, Popup Setup Column, dan Ceklis Kolom | FE+BE | 23 | 353, 354, 355 |
| TC-FA-CAT-E2E-103-setup-column-tabel-utama-geser-reset-tutup-dan-guard-satu-kolom | Setup Column Tabel Utama: Geser Urutan, Reset to Default, Tutup Tanpa Save, Guard Satu Kolom, dan Independensi Antar Tabel | FE+BE | 49 | 356, 359, 360, 361, 362 |
| TC-FA-CAT-E2E-104-setup-column-tabel-utama-pin-dan-batas-pin-keempat | Setup Column Tabel Utama: Pin Kolom Membekukan Kolom saat Scroll Horizontal dan Batas Pin Keempat | FE+BE | 22 | 357, 358 |
| TC-FA-CAT-E2E-105-pagination-ukuran-halaman-nomor-halaman-dan-perpindahan-halaman | Pagination Tabel Utama: Ukuran Halaman Default, Input Nomor Halaman, dan Perpindahan Halaman saat Ganti Sort atau Page Size | FE+BE | 21 | 363, 364, 365 |
| TC-FA-CAT-E2E-106-retensi-state-f5-klik-ulang-menu-dan-treesearchinput | Retensi State Halaman: F5, Klik Ulang Menu Settings > Categories, dan Perilaku TreeSearchInput | FE+BE | 43 | 376, 378, 380, 381, 382 |
| TC-FA-CAT-E2E-107-retensi-seleksi-checkbox-dan-hapus-baris-terakhir-halaman-terakhir | Retensi Seleksi Checkbox saat Search atau Filter Berubah dan Hapus Baris Terakhir di Halaman Terakhir | FE+BE | 24 | 386, 366 |
| TC-FA-CAT-E2E-108-download-tabel-utama-menu-nama-berkas-cakupan-hasil-nol-dan-node-leaf | Download Tabel Utama: Menu CSV dan XLSX, Nama Berkas, Cakupan Baris dan Kolom, Hasil Nol, Urutan Sort, dan Node Leaf | FE+BE | 44 | 367, 368, 369, 373, 374, 615 |
| TC-FA-CAT-E2E-109-download-tabel-utama-isi-berkas-bom-escape-transformasi-dan-format-tanggal | Download: Isi Berkas XLSX dan CSV (Tipe Sel, BOM, Escape), Berkas Changelog, dan Format Tanggal General Settings | FE+BE | 26 | 371, 372, 614, 496 |
| TC-FA-CAT-E2E-110-download-di-atas-5000-baris-loading-screen | Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background | FE+BE | 7 | 375 |
| TC-FA-CAT-E2E-111-resilience-wizard-save-selection-dan-download-5xx-dan-timeout | Resilience Wizard Save Selection dan Download (Tabel Utama, Changelog, Assets): Respons 5xx dan Timeout Jaringan | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra | 57 | 300, 313, 370, 413, 286 |
| TC-FA-CAT-E2E-112-modal-changelog-screening-isi-baris-path-snapshot-modified-by-dan-placeholder | Modal Changelog: Screening Tiga Zona, Isi Baris, Path Snapshot, Modified By, Empty State Terfilter, dan Placeholder Search | FE+BE | 35 | 388, 389, 390, 391, 393, 418 |
| TC-FA-CAT-E2E-113-modal-changelog-search-teks-modified-by-guard-date-dan-interaksi-search | Modal Changelog: Search Kolom Teks dan Modified By, Guard Kolom Date, dan Interaksi Kotak Search | FE+BE | 39 | 394, 395, 396, 584 |
| TC-FA-CAT-E2E-114-modal-changelog-search-vs-visibilitas-kolom-dan-kombinasi-search-filter | Modal Changelog: Search Terikat Visibilitas Kolom, Filter Independen, dan Kombinasi Search dengan Filter | FE+BE | 28 | 585, 405 |
| TC-FA-CAT-E2E-115-modal-changelog-sort-3-state-kolom-teks | Modal Changelog: Sort 3-State pada Kolom Action, Category Name, Field, Old Value, dan New Value | FE+BE | 9 | 397 |
| TC-FA-CAT-E2E-116-modal-changelog-filter-panel-opsi-category-name-dan-date-range | Modal Changelog: Screening Filter Panel, Logika OR dan AND, Opsi dari Data Log, Category Name Berbasis Id, dan Date Range Inklusif | FE+BE | 26 | 400, 401, 402, 403, 404 |
| TC-FA-CAT-E2E-117-modal-changelog-setup-column-screening-ceklis-dan-persist | Modal Changelog: Kolom Actions, Screening Popup Setup Column, serta Ceklis dan Persist Tujuh Kolom | FE+BE | 21 | 406, 407, 408 |
| TC-FA-CAT-E2E-118-modal-changelog-setup-column-guard-satu-kolom-dan-tutup-tanpa-save | Modal Changelog: Guard Satu Kolom Tersisa dan Penutupan Popup Setup Column Tanpa Save | FE+BE | 14 | 411, 546 |
| TC-FA-CAT-E2E-119-modal-changelog-setup-column-geser-urutan-dan-reset-to-default | Modal Changelog: Geser Urutan Tujuh Kolom Lewat Popup dengan Persist dan Reset to Default | FE+BE | 17 | 409, 410 |
| TC-FA-CAT-E2E-120-modal-changelog-pin-dan-unpin-kolom-persist | Modal Changelog: Pin dan Unpin Tujuh Kolom Lewat Popup Setup Column dengan Persist | FE+BE | 10 | 545 |
| TC-FA-CAT-E2E-121-modal-changelog-pagination-page-size-dan-download-csv-xlsx | Modal Changelog: Pagination dan Page Size, Navigasi Halaman, serta Download CSV dan XLSX | FE+BE | 48 | 412, 588, 587 |
| TC-FA-CAT-E2E-122-modal-changelog-penutupan-modal-tooltip-toolbar-dan-isolasi-state-search | Modal Changelog: Penutupan Lewat Backdrop dan Esc, Tooltip Toolbar, dan Isolasi State Search ke Tabel Utama | FE+BE | 15 | 414, 416, 417 |
| TC-FA-CAT-E2E-123-tabel-assets-detail-screening-search-guard-last-updated-dan-placeholder | Tabel Assets pada Popup Detail: Screening Kolom dan Default Sort, Search Kolom Teks dan Badge, Guard Last Updated, dan Placeholder Search | FE+BE | 31 | 419, 420, 421, 422, 423, 439 |
| TC-FA-CAT-E2E-124-tabel-assets-detail-sort-3-state-seluruh-kolom | Tabel Assets pada Popup Detail: Sort 3-State pada Kolom Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated | FE+BE | 27 | 424, 425, 426, 427 |
| TC-FA-CAT-E2E-125-tabel-assets-detail-filter-panel-field-opsi-distinct-dan-last-updated | Tabel Assets pada Popup Detail: Screening Filter Panel, Opsi DISTINCT, Logika OR dan AND, serta Date Range Last Updated Inklusif | FE+BE | 32 | 428, 429, 430, 431, 554 |
| TC-FA-CAT-E2E-126-tabel-assets-detail-setup-column-ceklis-delapan-kolom-default-dan-persist | Tabel Assets pada Popup Detail: Ceklis dan Unceklis Delapan Kolom Default Visible lewat Setup Column dengan Persist | FE+BE | 13 | 432 |
| TC-FA-CAT-E2E-127-tabel-assets-detail-screening-overlay-column-visibility-dan-popup-setup-column | Tabel Assets pada Popup Detail: Screening Overlay Column Visibility dan Popup Setup Column dengan Live Preview Tiga Zona | FE+BE | 17 | 547, 548 |
| TC-FA-CAT-E2E-128-tabel-assets-detail-setup-column-geser-urutan-reset-to-default-dan-tutup-tanpa-save | Tabel Assets pada Popup Detail: Geser Urutan Tujuh Kolom, Reset to Default, dan Penutupan Popup Setup Column Tanpa Save | FE+BE | 21 | 549, 551, 552 |
| TC-FA-CAT-E2E-129-tabel-assets-detail-setup-column-pin-unpin-tujuh-kolom-dan-guard-satu-kolom | Tabel Assets pada Popup Detail: Pin dan Unpin Tujuh Kolom lewat Setup Column dengan Persist serta Guard Satu Kolom Tersisa | FE+BE | 16 | 550, 553 |
| TC-FA-CAT-E2E-130-kolom-label-tabel-assets-setup-column-geser-dan-pin | Kolom Curated Label pada Tabel Assets: Default Tersembunyi, Ceklis, Geser Urutan, dan Pin dengan Persist | FE+BE | 26 | 555, 556, 557 |
| TC-FA-CAT-E2E-131-kolom-label-tabel-assets-sel-badge-popover-strip-dan-search | Kolom Curated Label pada Tabel Assets: Sel Badge dengan Ringkasan +N more, Popover Labels, Sel Kosong, dan Search | FE+BE | 20 | 558, 559, 560, 561 |
| TC-FA-CAT-E2E-132-kolom-label-tabel-assets-filter-download-dan-sort | Kolom Curated Label pada Tabel Assets: Filter Label, Download Hanya Saat Label Ditampilkan, dan Sort 3-State | FE+BE | 22 | 562, 563, 564 |
| TC-FA-CAT-E2E-133-tabel-assets-detail-badge-brand-group-strip-pagination-download-status | Tabel Assets Popup Detail: Badge Brand, Model/Type, dan Group, Strip Sel Kosong, Pagination, Download, serta Status Multi-Badge | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 33 | 433, 434, 435, 436, 437, 438 |
| TC-FA-CAT-E2E-134-tabel-assets-detail-interaksi-search-dan-search-vs-visibilitas-kolom | Tabel Assets Popup Detail: Interaksi Search serta Search Terikat Visibilitas Kolom dan Filter Independen | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 36 | 589, 590 |
| TC-FA-CAT-E2E-135-tabel-assets-detail-dropdown-filter-pencarian-internal-dan-chip | Tabel Assets Popup Detail: Dropdown Filter Pencarian Internal dan Sinkronisasi Chip dengan Checkbox | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 17 | 591 |
| TC-FA-CAT-E2E-136-tabel-assets-detail-download-cakupan-dan-transformasi-data | Tabel Assets Popup Detail: Download Cakupan Baris dan Kolom serta Transformasi Data pada Berkas Export | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 41 | 593, 613 |
| TC-FA-CAT-E2E-137-tabel-assets-detail-navigasi-paginasi-dan-genuine-empty | Tabel Assets Popup Detail: Navigasi Paginasi, Reset ke Halaman 1, dan Tabel Kosong (Genuine Empty) | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 42 | 594, 617 |
| TC-FA-CAT-E2E-138-kolom-tag-ikon-per-tipe-tag-dan-toggle-geser-pin-persist | Kolom TAG Tabel Assets: Ikon per Tipe Tag Aktif serta Toggle, Geser, Pin, dan Persist Setup Column | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 28 | 651, 652 |
| TC-FA-CAT-E2E-139-kolom-tag-search-dan-kolom-measurement-search-sort-filter | Kolom TAG Search Label Tipe Tag serta Kolom Measurement: Toggle, Sel Symbol UoM, Search, Sort, dan Filter | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 47 | 682, 654, 655 |
| TC-FA-CAT-E2E-140-kolom-transactional-policy-ikon-sort-filter-dan-search-nama-transaksi | Kolom Transactional Policy Tabel Assets: Ikon Transaksi On, Sort 3-State, Filter, dan Search Nama Transaksi | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 45 | 656, 657, 683 |
| TC-FA-CAT-E2E-141-kolom-last-scanned-asset-id-tidak-filterable-dan-kolom-category-tidak-ada | Kolom Last Scanned Tabel Assets serta Asset ID Tidak Filterable dan Kolom Category Tidak Ada | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 42 | 658, 659, 688, 679 |
| TC-FA-CAT-E2E-142-custom-field-dropdown-date-text-dan-formula-search-sort-filter | Kolom Custom Field Tabel Assets: Dropdown, Date, serta Text dan Formula untuk Search, Sort, dan Filter | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 48 | 689, 690, 692 |
| TC-FA-CAT-E2E-143-kolom-asset-value-commercial-full-sensitive | Kolom Asset Value (Commercial) dan Warranty Expiry Tabel Assets untuk Full Sensitive: Hidden Default, Format, Sort, Filter, dan Search | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 41 | 660, 661, 662 |
| TC-FA-CAT-E2E-144-warranty-expiry-dan-custom-field-full-sensitive | Kolom Warranty Expiry dan Custom Field Tabel Assets untuk Full Sensitive: Sort, Filter, Urutan Grup, Sel per Data Type, dan Strip | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 34 | 663, 664, 665, 666 |
| TC-FA-CAT-E2E-145-custom-field-tabel-assets-sort-filter-search-per-data-type | Custom Field Tabel Assets: Sort, Search, dan Filter per Data Type, serta Filter Numeric/Percentage | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 38 | 667, 691 |
| TC-FA-CAT-E2E-146-setup-column-matriks-kolom-bergerbang-per-role-dan-field-baru-inactive | Setup Column Tabel Assets: Matriks Kolom Bergerbang per Role serta Custom Field Baru dan Inactive | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 24 | 673, 678 |
| TC-FA-CAT-E2E-147-setup-column-lisensi-fa-7-dan-dua-kolom-asset-value | Kolom Custom Field Accounting menurut Lisensi FA-7 dan Dua Kolom Asset Value Commercial dan Fiscal | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 24 | 687, 698 |
| TC-FA-CAT-E2E-148-penanda-masa-garansi-warranty-expiry-batas-30-hari-dan-tanpa-pengaruh | Penanda Masa Garansi Kolom Warranty Expiry: Expired, Expires Soon, Batas 30 Hari, dan Tanpa Pengaruh pada Sort, Filter, Search, Download | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 34 | 694, 695, 697 |
| TC-FA-CAT-E2E-149-asset-value-fiscal-not-depreciated-reset-default-dan-perubahan-real-time | Kolom Asset Value Fiscal: Not Depreciated, Hidden Default setelah Reset to Default, dan Perubahan Policy serta Custom Field Real-Time | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 23 | 699, 700, 680 |
| TC-FA-CAT-E2E-150-gerbang-asset-value-viewer-sort-filter-dan-no-access | Gerbang Asset Value untuk Asset Value Viewer: Sel No access, Sort, dan Filter pada Asset Value dan Warranty Expiry | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 33 | 669, 674, 675 |
| TC-FA-CAT-E2E-151-gerbang-asset-value-download-no-access-kedua-kolom-dan-respons-server | Gerbang Asset Value: Download Sel No access, Gerbang pada Kedua Kolom Asset Value, Sel Pending Sort-Filter-Search-Download, dan Respons Server Tanpa Nilai | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 45 | 677, 701, 703, 681 |
| TC-FA-CAT-E2E-152-gerbang-warranty-dan-custom-field-purchasing-purchase-group-a | Gerbang Warranty dan Custom Field Purchasing untuk Purchase Group A: Group A Saja, Search Tidak Mencocokkan No access, dan Keadaan Tidak Berlaku Menang | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 41 | 671, 676, 686 |
| TC-FA-CAT-E2E-153-gerbang-warranty-dan-purchasing-purchase-group-a | Gerbang Warranty dan Custom Field Purchasing pada Popup Detail untuk Purchase Group A: Filter Tidak Mencocokkan No access dan Sel Warranty Tanpa Penanda | FE+BE | 20 | 693, 696 |
| TC-FA-CAT-E2E-154-gerbang-kolom-accounting-global-dan-tanpa-hak-sensitif | Gerbang Kolom Popup Detail: Accounting Global Melihat Nilai Client-wide dan Aktor Tanpa Hak Nilai Sensitif Melihat Seluruh Sel No access | FE+BE | 25 | 670, 672 |
| TC-FA-CAT-E2E-155-tabel-step-consolidation-screening-hierarki-excess-placeholder | Tabel Step Category Consolidation: Screening Kolom dan Sel, Toolbar, Placeholder Search, Pagination 10 Baris dengan Retensi Centang, Hierarki, Badge Excess, serta Last Updated dan Modified By | FE+BE | 29 | 440, 455, 457, 453, 441, 442, 456 |
| TC-FA-CAT-E2E-156-tabel-step-search-kolom-guard-depth-last-updated-dan-sort | Tabel Step Category Consolidation: Search pada Kolom yang Dapat Dicari, Guard Depth dan Last Updated, serta Sort Tiga State Last Updated | FE+BE | 29 | 443, 444, 445, 448 |
| TC-FA-CAT-E2E-157-tabel-step-sort-kolom-teks-dan-filter | Tabel Step Category Consolidation: Sort Tiga State Kolom Teks (Category Name, Code, Status, Modified By), Screening Filter Panel, Filter Status dan Modified By, serta Filter Last Updated | FE+BE | 27 | 446, 449, 450, 451 |
| TC-FA-CAT-E2E-158-tabel-step-setup-column-ceklis-screening-overlay-dan-popup | Tabel Step Category Consolidation: Screening Overlay Column Visibility dan Popup Setup Column, serta Ceklis Tiap Kolom dengan Live Preview dan Persistensi Save | FE+BE | 26 | 565, 566, 452 |
| TC-FA-CAT-E2E-159-tabel-step-setup-column-geser-urutan-reset-dan-tutup-tanpa-save | Tabel Step Category Consolidation: Setup Column Geser Urutan Kolom dengan Persistensi, Reset to Default, dan Penutupan Popup Tanpa Save | FE+BE | 23 | 567, 569, 570 |
| TC-FA-CAT-E2E-160-tabel-step-setup-column-pin-per-kolom-dan-guard-satu-kolom | Tabel Step Category Consolidation: Pin dan Unpin Tiap Kolom lewat Setup Column dengan Persistensi, serta Guard Satu Kolom Tersisa | FE+BE | 14 | 568, 571 |
| TC-FA-CAT-E2E-161-tabel-step-interaksi-search-dan-search-vs-visibilitas-kolom | Tabel Step Category Consolidation: Interaksi Search (Reveal, Enter, Clear, Panah Tutup) dan Search Terikat Visibilitas Kolom sedangkan Filter Independen | FE+BE | 35 | 595, 596 |
| TC-FA-CAT-E2E-162-tabel-step-dropdown-filter-clear-field-dan-kombinasi | Tabel Step Category Consolidation: Dropdown Filter (Pencarian Internal dan Sinkronisasi Chip), Clear Field, serta Kombinasi Search, Filter, dan Sort dengan Centang Keep usable Dipertahankan | FE+BE | 44 | 597, 598 |
| TC-FA-CAT-E2E-163-tabel-step-sort-angka-navigasi-paginasi-dan-reset-halaman | Tabel Step Category Consolidation: Sort Tiga State Kolom Angka (Depth, Total Asset) serta Navigasi Paginasi, Input Nomor Halaman, Page Size, dan Reset ke Halaman 1 | FE+BE | 27 | 447, 599 |
| TC-FA-CAT-E2E-164-log-create-dan-edit-tiga-surface | Log Create dan Edit Category pada Tiga Surface (Changelog, System Log, Activity Log): Create Root, Add Subcategory, Edit Name, Edit Code, dan Edit Description | FE+BE | 46 | 458, 459, 460, 461, 462 |
| TC-FA-CAT-E2E-165-log-edit-code-kosong-delete-cascade-wizard-excess-dan-timestamp | Log pada Tiga Surface: Edit Kosongkan Code, Delete, Delete Cascade Descendant Excess, Marked as Excess dari Wizard, Timestamp Sama, dan Kolom Action Teks Biasa | FE+BE | 52 | 463, 465, 479, 480, 466, 468 |
| TC-FA-CAT-E2E-166-log-hasil-import-dan-fallback-t0 | Log Kategori Hasil Import (Tab Category dan Create Missing Categories), Parity Edit dan Delete Record Hasil Import, serta Log Marked as Excess dari Fallback T-0 oleh System | FE+BE | 35 | 474, 475, 476, 469 |
| TC-FA-CAT-E2E-167-absence-log-edit-no-op-zero-delta-seed-onboarding-aksi-gagal-dan-skip | Absence Log Category: Edit Tanpa Perubahan (No-Op dan Zero-Delta), Seed Onboarding, Baris Skip Bulk Delete, Aksi Gagal 5xx atau Diblok Guard, serta Kategori Tidak Terlibat | FE+BE | 68 | 191, 192, 201, 464, 467, 477, 478, 473 |
| TC-FA-CAT-E2E-168-absence-log-request-langsung-ditolak-changelog-system-log-activity-log | Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Baris Changelog, System Log, dan Activity Log | FE+BE | 0 | 497, 498, 499, 500, 501, 502, 579 |
| TC-FA-CAT-E2E-169-atomisitas-log-rollback-create-edit-delete | Atomisitas Log: Kegagalan Penulisan Log Membatalkan Seluruh Aksi Create, Edit, dan Delete | FE+BE | 26 | 580 |
| TC-FA-CAT-E2E-170-sinkronisasi-asset-name-category-locked-rename-asset-name-dan-asset-list | Sinkronisasi ke Modul Konsumen: Category Locked di Asset Name, Rename pada Asset Name dan Asset List | FE+BE | 34 | 481, 484, 572 |
| TC-FA-CAT-E2E-171-sinkronisasi-custom-asset-id-sidebar-atp-dan-total-asset-live | Sinkronisasi ke Modul Konsumen: Segmen Category Code Custom Asset ID, Sidebar Asset Transactional Policy, dan Total Asset Live | FE+BE | 32 | 486, 487, 488 |
| TC-FA-CAT-E2E-172-format-tanggal-general-settings-di-semua-surface-categories | Format Tanggal General Settings pada Tabel Utama, Filter, Modal Changelog, Popup Detail, dan Popup Category Consolidation | FE+BE | 35 | 491, 492, 493, 494, 495 |
| TC-FA-CAT-E2E-173-defense-in-depth-request-langsung-role-dan-wizard-submit-ditolak-bagian-1 | Defense-in-Depth: Request Langsung Create, Edit, Delete, Bulk Delete, dan Wizard Submit Ditolak Server (Bagian 1) | FE+BE | 30 | 497, 498, 499, 500, 501, 502, 579 |
| TC-FA-CAT-E2E-174-defense-in-depth-validasi-server-markup-sql-isolasi-tenant-dan-capability-atp-bagian-2 | Defense-in-Depth: Validasi Server, Markup dan SQL pada Nama, Isolasi Tenant, dan Capability ATP Read (Bagian 2) | FE+BE | 53 | 503, 508, 509, 510, 637 |
| TC-FA-CAT-E2E-175-state-tenant-suspended-expired-aksi-tulis-ditolak | State Tenant Suspended dan Expired: Aksi Create, Add Subcategory, Edit, Delete, dan Bulk Delete Ditolak dengan Toast Baku | FE+BE | 58 | 504, 505, 506, 507 |
| TC-FA-CAT-E2E-176-edge-case-total-asset-lifecycle-list-diam-diam-form-edit-dialog-vs-toast-dan-f5-node-terhapus | Edge Case: Total Asset Mengikuti Lifecycle, List Diperbarui Diam-diam, Form Edit Tidak Di-refresh, Dialog Tanpa Toast, dan F5 Saat Node Terhapus | FE+BE | 34 | 511, 514, 515, 518, 377 |
| TC-FA-CAT-E2E-179-form-dirty-refresh-f5-dan-pindah-route-spa-subcategory | Form New Subcategory Dirty: Refresh F5 dan Pindah Route SPA | FE+BE | 23 | 618, 619 |
| TC-FA-CAT-E2E-180-new-category-description-bebas-dan-nama-tersimpan-ter-trim | New Category: Description Karakter Bebas dan Category Name Tersimpan Ter-trim | FE+BE | 18 | 107, 86 |
| TC-FA-CAT-E2E-181-stay-on-this-form-recheck-cap-count-server | Stay on This Form: Server Me-re-check Cap Category Count pada Submit Berikutnya | FE+BE | 32 | 116, 517 |
| TC-FA-CAT-E2E-182-create-root-tanpa-code-log-satu-baris | Create Root Tanpa Code: Code Hasil Generate dan Changelog Satu Baris per Kategori | FE+BE | 18 | 166, 169 |
| TC-FA-CAT-E2E-183-izin-dicabut-saat-bulk-delete-dan-wizard-consolidation-terbuka | Izin Dicabut Saat Dialog Bulk Delete dan Popup Consolidation Terbuka: Aksi Ditolak 403 dan UI Di-refresh | FE+BE (backend nyata; pencabutan capability dan Access Level dilakukan Principal Automation lewat sesi API, tanpa intercept) | 30 | 541, 542 |
| TC-FA-CAT-E2E-184-parent-menjadi-excess-saat-popup-subcategory-dan-edit-terbuka | Kategori Menjadi Excess Saat Popup New Subcategory atau Popup Edit Terbuka: Dialog Konflik 409 (CRU Lock) | FE+BE (backend nyata; Fallback T-0 dipicu lewat kemampuan T-0 yang disediakan tim FE/BE, tanpa intercept) | 47 | 168, 210, 600 |
| TC-FA-CAT-E2E-185-race-dua-sesi-code-sama-add-subcategory-dan-edit-vs-delete | Race Dua Sesi UI: Edit dengan Code Sama, Add Subcategory vs Delete, dan Edit vs Delete | FE+BE | 50 | 631, 512, 513 |
| TC-FA-CAT-E2E-186-resilience-bulk-delete-gagal-sebagian-dan-timeout | Resilience Bulk Delete: Gagal Sebagian dan Timeout | FE+BE | 26 | 262, 271 |
| TC-FA-CAT-E2E-187-bulk-delete-baris-excess-ikut-terhapus | Bulk Delete: Baris Excess Dapat Dicentang dan Ikut Terhapus pada Client CatExcess | FE+BE | 5 | 260 |
| TC-FA-CAT-E2E-188-popup-detail-full-path-penutupan-dan-tanpa-tab-changelog | Popup Detail Category: Category Name Full Path, Penutupan Hanya lewat Close atau Esc, dan Tanpa Tab Changelog | FE+BE | 23 | 278, 279, 280 |
| TC-FA-CAT-E2E-189-wizard-seleksi-diubah-lagi-dan-status-per-node-independen-catexcess | Wizard Consolidation CatExcess: Seleksi Diubah Lagi dan Status Usable atau Excess Independen per Node | FE+BE | 21 | 293, 296 |
| TC-FA-CAT-E2E-190-fallback-t0-kategori-terlama-urutan-nama-seleksi-di-bawah-cap-dan-downgrade-baru | Fallback T-0: Kategori Terlama Tetap Usable, Urutan Nama A-Z, Seleksi di Bawah Cap, dan Downgrade Baru Mereset Status Submit | FE+BE | 35 | 308, 309, 310, 311 |
| TC-FA-CAT-E2E-191-teks-nama-panjang-dan-klik-area-baris-tanpa-aksi | Teks Nama Panjang Tidak Di-Truncate dan Klik Area Baris di Luar Nama, Total Asset, Checkbox, dan Row Action Tidak Melakukan Aksi | FE+BE | 19 | 387, 636 |
| TC-FA-CAT-E2E-192-kombinasi-search-filter-sort-dan-pagination-tabel-utama | Kombinasi Search, Filter, Sort, dan Pagination Tabel Utama: Irisan, Urutan Penerapan, dan Pelepasan Kontrol | FE+BE | 36 | 383, 384, 385 |
| TC-FA-CAT-E2E-193-modal-changelog-dropdown-filter-pencarian-internal-dan-sinkronisasi-chip | Modal Changelog: Pencarian Internal Dropdown Filter dan Sinkronisasi Chip dengan Checkbox | FE+BE | 13 | 586 |
| TC-FA-CAT-E2E-194-modal-changelog-sort-3-state-kolom-modified-by-dan-date | Modal Changelog: Sort 3-State pada Kolom Modified By dan Date | FE+BE | 15 | 398, 399 |
| TC-FA-CAT-E2E-195-tabel-assets-detail-clear-field-dan-kombinasi-search-filter-sort | Tabel Assets Popup Detail: Clear Field Filter serta Kombinasi Search, Filter, dan Sort | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 28 | 592 |
| TC-FA-CAT-E2E-196-kolom-tag-sort-3-state-dan-filter-multi-select | Kolom TAG Tabel Assets: Sort 3-State dan Filter Multi-Select dengan Logika OR | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 20 | 653 |
| TC-FA-CAT-E2E-197-gerbang-kolom-tier-group-manager-descendant-dan-no-access | Gerbang Kolom Popup Detail Tier Group Manager: Asset Value, Warranty, dan Purchasing pada Group Ditugaskan beserta Descendant, No access di Luar, Accounting Tidak Tersedia | FE+BE | 18 | 685 |
| TC-FA-CAT-E2E-198-gerbang-kolom-tier-total-control-default-user-dan-read-only | Gerbang Kolom Popup Detail Tier Total Control, Default User, dan Read Only: Seluruh Kolom Bergerbang Berhak Client-wide Tanpa No access | FE+BE | 16 | 684 |
| TC-FA-CAT-E2E-199-sinkronisasi-dropdown-koreksi-approver-dan-kartu-category-consolidation-wizard-reconciliation | Sinkronisasi ke Modul Konsumen: Dropdown Koreksi Approver pada Registrasi Aset dan Kartu Category Consolidation di Wizard Reconciliation | FE+BE | 33 | 583, 490 |
| TC-FA-CAT-E2E-200-sinkronisasi-asset-name-delete-setelah-pengalihan-category-locked-excess-dan-dropdown-category | Sinkronisasi ke Asset Name: Delete Setelah Pengalihan Kategori, Category Locked pada Kategori Excess, dan Dropdown Category | FE+BE | 32 | 485, 482, 483 |
| TC-FA-CAT-E2E-201-system-limits-hierarchy-depth-limit-dialog-d-04-catdepthlimit | System Limits: Dialog D-04 Hierarchy Depth Limit Tercapai pada Client CatDepthLimit | FE+BE | 5 | 127 |
| TC-FA-CAT-E2E-202-cap-depth-plan-diturunkan-catdeep-tidak-menandai-excess | Cap Depth Plan CatDeep Diturunkan: Node Lebih Dalam Tidak Excess dan Tetap Berfungsi, Add Subcategory Baru Diblok D-02 | FE+BE | 13 | 318, 516 |
| TC-FA-CAT-E2E-203-tab-baru-mulai-dari-default-tanpa-state-tab-pertama | Tab Browser Baru Memulai dari Default: All Categories Tanpa Search dan Filter | FE+BE | 6 | 379 |
| TC-FA-CAT-E2E-204-isi-berkas-xlsx-download-tabel-assets-kolom-baru | Isi Berkas XLSX Download Tabel Assets: Transformasi Data Kolom Baru dan Kolom Hidden Tidak Ikut | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 19 | 668 |
| TC-FA-CAT-E2E-205-sel-asset-value-pending-tooltip-alasan-dan-prioritas | Sel Asset Value Pending Tabel Assets: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) | 12 | 702 |

Spec `009` (TC-638, kontras WCAG, Manual Only) memakai `coverage.web: automated` sampai FE menyatakan tidak bisa; 1 spec memakai `coverage.mobile: automated`; spec lain `coverage.web: automated`. Nomor 177 dan 178 tidak dipakai; spec 201–204 ditambah setelah audit (TC-127→201, TC-318/516→202, TC-379→203, TC-668→204).

## Pembagian TC lintas spec

- Asersi absence log kelas g ada di spec `168` (TC-497–502, 579); spec `173` memuat status respons dan state data untuk TC yang sama.
- TC-580 (atomisitas log) di spec `169` dengan butir P-1; pemicu kegagalan penulisan log disediakan tim BE.
- Asersi "tidak ada log" untuk banyak TC lain ditulis di spec asal dengan baseline Changelog dan butir P-1 (bukan spec kelas g).
- Pemecahan memakai nomor cadangan: 179–184, 185–200 (kecuali 177–178); lihat Notes tiap spec.

## Kebutuhan lingkungan (tim FE)

- Env var password (nama usulan; belum terdaftar di `spectra.config.ts` dan `.env.example`): `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CAPREAD_PASSWORD`, `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, `FA_DO_PASSWORD`, `FA_CUD_PASSWORD`, `FA_GMNOCAP_PASSWORD`, `FA_GMCAP_PASSWORD`, `FA_GMCRUD_PASSWORD`, `FA_NOROLE_PASSWORD`, `FA_FS_PASSWORD`, `FA_AV_PASSWORD`, `FA_PGA_PASSWORD`, `FA_ACCGL_PASSWORD`, `FA_NOSENS_PASSWORD`, `FA_DU_PASSWORD`, `FA_ATPREAD_PASSWORD`, `FA_APPROVER_PASSWORD`.
- Fixture `fixtures/settings-categories.json` (belum ada) dan seed/pemulihan client via API (CatFresh, CatThree, CatExcess, CatPostT0, CatPreT0, CatCode, dan lain-lain).
- Kemampuan teknis: kontrol jam server dan browser (T-0), sesi API pelaku kedua (Principal Automation #11), fault injection log dan intercept, pembaca berkas CSV/XLSX, pemulihan General Settings, injeksi DOM.

## Temuan yang masih terbuka

- Registry prefix menyebut 644 TC, sedangkan TC berisi 701 (baris registry usang).
- TC-638 (WCAG) ditandai `automated` sampai FE menyatakan tidak bisa; TC-580 butuh pemicu kegagalan log dari tim BE, jika tidak tersedia ditandai `unsupported`.
- Banyak spec melewati ~35 langkah dengan alasan di Notes (Expected dipecah per klausa, S-01); nomor cadangan habis.
- Detail temuan TC-sumber per spec ada di Notes "Temuan untuk QA".

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-CAT-1 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-2 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-3 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-4 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-5 | TC-FA-CAT-E2E-002 | FE+BE |
| TC-FA-CAT-6 | TC-FA-CAT-E2E-002 | FE+BE |
| TC-FA-CAT-7 | TC-FA-CAT-E2E-002 | FE+BE |
| TC-FA-CAT-8 | TC-FA-CAT-E2E-002 | FE+BE |
| TC-FA-CAT-9 | TC-FA-CAT-E2E-002 | FE+BE |
| TC-FA-CAT-10 | TC-FA-CAT-E2E-005 | FE+BE |
| TC-FA-CAT-11 | TC-FA-CAT-E2E-003 | FE+BE |
| TC-FA-CAT-12 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-13 | TC-FA-CAT-E2E-046 | FE+BE (intercept parsial di atas backend nyata; respons baca list kategori, data aset Popup Detail, dan Changelog ditahan atau dipaksa 5xx lewat `Spectra |
| TC-FA-CAT-14 | TC-FA-CAT-E2E-003 | FE+BE |
| TC-FA-CAT-15 | TC-FA-CAT-E2E-003 | FE+BE |
| TC-FA-CAT-16 | TC-FA-CAT-E2E-003 | FE+BE |
| TC-FA-CAT-17 | TC-FA-CAT-E2E-003 | FE+BE |
| TC-FA-CAT-18 | TC-FA-CAT-E2E-004 | FE+BE |
| TC-FA-CAT-19 | TC-FA-CAT-E2E-004 | FE+BE |
| TC-FA-CAT-20 | TC-FA-CAT-E2E-004 | FE+BE |
| TC-FA-CAT-21 | TC-FA-CAT-E2E-004 | FE+BE |
| TC-FA-CAT-22 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-23 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-24 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-25 | TC-FA-CAT-E2E-001 | FE+BE |
| TC-FA-CAT-26 | TC-FA-CAT-E2E-010 | FE+BE |
| TC-FA-CAT-27 | TC-FA-CAT-E2E-007 | FE+BE |
| TC-FA-CAT-28 | TC-FA-CAT-E2E-007 | FE+BE |
| TC-FA-CAT-29 | TC-FA-CAT-E2E-007 | FE+BE |
| TC-FA-CAT-30 | TC-FA-CAT-E2E-007 | FE+BE |
| TC-FA-CAT-31 | TC-FA-CAT-E2E-007 | FE+BE |
| TC-FA-CAT-32 | TC-FA-CAT-E2E-011 | FE+BE |
| TC-FA-CAT-33 | TC-FA-CAT-E2E-011 | FE+BE |
| TC-FA-CAT-34 | TC-FA-CAT-E2E-011 | FE+BE |
| TC-FA-CAT-35 | TC-FA-CAT-E2E-012 | FE+BE |
| TC-FA-CAT-36 | TC-FA-CAT-E2E-012 | FE+BE |
| TC-FA-CAT-37 | TC-FA-CAT-E2E-012 | FE+BE |
| TC-FA-CAT-38 | TC-FA-CAT-E2E-013 | FE+BE |
| TC-FA-CAT-39 | TC-FA-CAT-E2E-013 | FE+BE |
| TC-FA-CAT-40 | TC-FA-CAT-E2E-013 | FE+BE |
| TC-FA-CAT-41 | TC-FA-CAT-E2E-013 | FE+BE |
| TC-FA-CAT-42 | TC-FA-CAT-E2E-013 | FE+BE |
| TC-FA-CAT-43 | TC-FA-CAT-E2E-014 | FE+BE |
| TC-FA-CAT-44 | TC-FA-CAT-E2E-014 | FE+BE |
| TC-FA-CAT-45 | TC-FA-CAT-E2E-014 | FE+BE |
| TC-FA-CAT-46 | TC-FA-CAT-E2E-015 | FE+BE |
| TC-FA-CAT-47 | TC-FA-CAT-E2E-015 | FE+BE |
| TC-FA-CAT-48 | TC-FA-CAT-E2E-014 | FE+BE |
| TC-FA-CAT-49 | TC-FA-CAT-E2E-016 | FE+BE |
| TC-FA-CAT-50 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-51 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-52 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-53 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-54 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-55 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-56 | TC-FA-CAT-E2E-017 | FE+BE |
| TC-FA-CAT-57 | TC-FA-CAT-E2E-016 | FE+BE |
| TC-FA-CAT-58 | TC-FA-CAT-E2E-018 | FE+BE |
| TC-FA-CAT-59 | TC-FA-CAT-E2E-019 | FE+BE |
| TC-FA-CAT-60 | TC-FA-CAT-E2E-018 | FE+BE |
| TC-FA-CAT-61 | TC-FA-CAT-E2E-018 | FE+BE |
| TC-FA-CAT-62 | TC-FA-CAT-E2E-020 | FE+BE |
| TC-FA-CAT-63 | TC-FA-CAT-E2E-021 | FE+BE |
| TC-FA-CAT-64 | TC-FA-CAT-E2E-020 | FE+BE |
| TC-FA-CAT-65 | TC-FA-CAT-E2E-020 | FE+BE |
| TC-FA-CAT-66 | TC-FA-CAT-E2E-020 | FE+BE |
| TC-FA-CAT-67 | TC-FA-CAT-E2E-020 | FE+BE |
| TC-FA-CAT-68 | TC-FA-CAT-E2E-021 | FE+BE |
| TC-FA-CAT-69 | TC-FA-CAT-E2E-021 | FE+BE |
| TC-FA-CAT-70 | TC-FA-CAT-E2E-021 | FE+BE |
| TC-FA-CAT-71 | TC-FA-CAT-E2E-021 | FE+BE |
| TC-FA-CAT-72 | TC-FA-CAT-E2E-022 | FE+BE |
| TC-FA-CAT-73 | TC-FA-CAT-E2E-022 | FE+BE |
| TC-FA-CAT-74 | TC-FA-CAT-E2E-023 | FE+BE |
| TC-FA-CAT-75 | TC-FA-CAT-E2E-023 | FE+BE |
| TC-FA-CAT-76 | TC-FA-CAT-E2E-023 | FE+BE |
| TC-FA-CAT-77 | TC-FA-CAT-E2E-024 | FE+BE |
| TC-FA-CAT-78 | TC-FA-CAT-E2E-024 | FE+BE |
| TC-FA-CAT-79 | TC-FA-CAT-E2E-024 | FE+BE |
| TC-FA-CAT-80 | TC-FA-CAT-E2E-024 | FE+BE |
| TC-FA-CAT-81 | TC-FA-CAT-E2E-028 | FE+BE |
| TC-FA-CAT-82 | TC-FA-CAT-E2E-028 | FE+BE |
| TC-FA-CAT-83 | TC-FA-CAT-E2E-028 | FE+BE |
| TC-FA-CAT-84 | TC-FA-CAT-E2E-028 | FE+BE |
| TC-FA-CAT-85 | TC-FA-CAT-E2E-024 | FE+BE |
| TC-FA-CAT-86 | TC-FA-CAT-E2E-180 | FE+BE |
| TC-FA-CAT-87 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-88 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-89 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-90 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-91 | TC-FA-CAT-E2E-030 | FE+BE |
| TC-FA-CAT-92 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-93 | TC-FA-CAT-E2E-025 | FE+BE |
| TC-FA-CAT-94 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-95 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-96 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-97 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-98 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-99 | TC-FA-CAT-E2E-026 | FE+BE |
| TC-FA-CAT-100 | TC-FA-CAT-E2E-027 | FE+BE |
| TC-FA-CAT-101 | TC-FA-CAT-E2E-030 | FE+BE |
| TC-FA-CAT-102 | TC-FA-CAT-E2E-030 | FE+BE |
| TC-FA-CAT-103 | TC-FA-CAT-E2E-030 | FE+BE |
| TC-FA-CAT-104 | TC-FA-CAT-E2E-030 | FE+BE |
| TC-FA-CAT-105 | TC-FA-CAT-E2E-027 | FE+BE |
| TC-FA-CAT-106 | TC-FA-CAT-E2E-027 | FE+BE |
| TC-FA-CAT-107 | TC-FA-CAT-E2E-180 | FE+BE |
| TC-FA-CAT-108 | TC-FA-CAT-E2E-032 | FE+BE |
| TC-FA-CAT-109 | TC-FA-CAT-E2E-032 | FE+BE |
| TC-FA-CAT-110 | TC-FA-CAT-E2E-032 | FE+BE |
| TC-FA-CAT-111 | TC-FA-CAT-E2E-033 | FE+BE |
| TC-FA-CAT-112 | TC-FA-CAT-E2E-033 | FE+BE |
| TC-FA-CAT-113 | TC-FA-CAT-E2E-023 | FE+BE |
| TC-FA-CAT-114 | TC-FA-CAT-E2E-034 | FE+BE |
| TC-FA-CAT-115 | TC-FA-CAT-E2E-034 | FE+BE |
| TC-FA-CAT-116 | TC-FA-CAT-E2E-181 | FE+BE |
| TC-FA-CAT-117 | TC-FA-CAT-E2E-035 | FE+BE |
| TC-FA-CAT-118 | TC-FA-CAT-E2E-035 | FE+BE |
| TC-FA-CAT-119 | TC-FA-CAT-E2E-035 | FE+BE |
| TC-FA-CAT-120 | TC-FA-CAT-E2E-035 | FE+BE |
| TC-FA-CAT-121 | TC-FA-CAT-E2E-037 | FE+BE |
| TC-FA-CAT-122 | TC-FA-CAT-E2E-037 | FE+BE |
| TC-FA-CAT-123 | TC-FA-CAT-E2E-038 | FE+BE |
| TC-FA-CAT-124 | TC-FA-CAT-E2E-036 | FE+BE |
| TC-FA-CAT-125 | TC-FA-CAT-E2E-036 | FE+BE |
| TC-FA-CAT-126 | TC-FA-CAT-E2E-039 | FE+BE |
| TC-FA-CAT-127 | TC-FA-CAT-E2E-201 | FE+BE |
| TC-FA-CAT-128 | TC-FA-CAT-E2E-039 | FE+BE |
| TC-FA-CAT-129 | TC-FA-CAT-E2E-038 | FE+BE |
| TC-FA-CAT-130 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-131 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-132 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-133 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-134 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-135 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-136 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-137 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-138 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-139 | TC-FA-CAT-E2E-045 | FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra |
| TC-FA-CAT-140 | TC-FA-CAT-E2E-042 | FE+BE |
| TC-FA-CAT-141 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-142 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-143 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-144 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-145 | TC-FA-CAT-E2E-061 | FE+BE |
| TC-FA-CAT-146 | TC-FA-CAT-E2E-061 | FE+BE |
| TC-FA-CAT-147 | TC-FA-CAT-E2E-061 | FE+BE |
| TC-FA-CAT-148 | TC-FA-CAT-E2E-062 | FE+BE |
| TC-FA-CAT-149 | TC-FA-CAT-E2E-062 | FE+BE |
| TC-FA-CAT-150 | TC-FA-CAT-E2E-063 | FE+BE |
| TC-FA-CAT-151 | TC-FA-CAT-E2E-063 | FE+BE |
| TC-FA-CAT-152 | TC-FA-CAT-E2E-063 | FE+BE |
| TC-FA-CAT-153 | TC-FA-CAT-E2E-064 | FE+BE |
| TC-FA-CAT-154 | TC-FA-CAT-E2E-064 | FE+BE |
| TC-FA-CAT-155 | TC-FA-CAT-E2E-065 | FE+BE |
| TC-FA-CAT-156 | TC-FA-CAT-E2E-065 | FE+BE |
| TC-FA-CAT-157 | TC-FA-CAT-E2E-065 | FE+BE |
| TC-FA-CAT-158 | TC-FA-CAT-E2E-065 | FE+BE |
| TC-FA-CAT-159 | TC-FA-CAT-E2E-066 | FE+BE |
| TC-FA-CAT-160 | TC-FA-CAT-E2E-066 | FE+BE |
| TC-FA-CAT-161 | TC-FA-CAT-E2E-066 | FE+BE |
| TC-FA-CAT-162 | TC-FA-CAT-E2E-067 | FE+BE |
| TC-FA-CAT-163 | TC-FA-CAT-E2E-067 | FE+BE |
| TC-FA-CAT-164 | TC-FA-CAT-E2E-032 | FE+BE |
| TC-FA-CAT-165 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-166 | TC-FA-CAT-E2E-182 | FE+BE |
| TC-FA-CAT-167 | TC-FA-CAT-E2E-045 | FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra |
| TC-FA-CAT-168 | TC-FA-CAT-E2E-184 | FE+BE (backend nyata; Fallback T-0 dipicu lewat kemampuan T-0 yang disediakan tim FE/BE, tanpa intercept) |
| TC-FA-CAT-169 | TC-FA-CAT-E2E-182 | FE+BE |
| TC-FA-CAT-170 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-171 | TC-FA-CAT-E2E-050 | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra |
| TC-FA-CAT-172 | TC-FA-CAT-E2E-050 | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra |
| TC-FA-CAT-173 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-174 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-175 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-176 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-177 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-178 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-179 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-180 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-181 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-182 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-183 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-184 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-185 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-186 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-187 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-188 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-189 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-190 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-191 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-192 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-193 | TC-FA-CAT-E2E-055 | FE+BE |
| TC-FA-CAT-194 | TC-FA-CAT-E2E-055 | FE+BE |
| TC-FA-CAT-195 | TC-FA-CAT-E2E-055 | FE+BE |
| TC-FA-CAT-196 | TC-FA-CAT-E2E-056 | FE+BE |
| TC-FA-CAT-197 | TC-FA-CAT-E2E-056 | FE+BE |
| TC-FA-CAT-198 | TC-FA-CAT-E2E-056 | FE+BE |
| TC-FA-CAT-199 | TC-FA-CAT-E2E-057 | FE+BE |
| TC-FA-CAT-200 | TC-FA-CAT-E2E-057 | FE+BE |
| TC-FA-CAT-201 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-202 | TC-FA-CAT-E2E-057 | FE+BE |
| TC-FA-CAT-203 | TC-FA-CAT-E2E-050 | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra |
| TC-FA-CAT-204 | TC-FA-CAT-E2E-058 | FE+BE |
| TC-FA-CAT-205 | TC-FA-CAT-E2E-059 | FE+BE |
| TC-FA-CAT-206 | TC-FA-CAT-E2E-058 | FE+BE |
| TC-FA-CAT-207 | TC-FA-CAT-E2E-060 | FE+BE |
| TC-FA-CAT-208 | TC-FA-CAT-E2E-042 | FE+BE |
| TC-FA-CAT-209 | TC-FA-CAT-E2E-043 | FE+BE (backend nyata; pencabutan capability dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-210 | TC-FA-CAT-E2E-184 | FE+BE (backend nyata; Fallback T-0 dipicu lewat kemampuan T-0 yang disediakan tim FE/BE, tanpa intercept) |
| TC-FA-CAT-211 | TC-FA-CAT-E2E-060 | FE+BE |
| TC-FA-CAT-212 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-213 | TC-FA-CAT-E2E-073 | FE+BE |
| TC-FA-CAT-214 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-215 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-216 | TC-FA-CAT-E2E-073 | FE+BE |
| TC-FA-CAT-217 | TC-FA-CAT-E2E-073 | FE+BE |
| TC-FA-CAT-218 | TC-FA-CAT-E2E-073 | FE+BE |
| TC-FA-CAT-219 | TC-FA-CAT-E2E-072 | FE+BE |
| TC-FA-CAT-220 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-221 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-222 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-223 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-224 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-225 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-226 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-227 | TC-FA-CAT-E2E-072 | FE+BE |
| TC-FA-CAT-228 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-229 | TC-FA-CAT-E2E-073 | FE+BE |
| TC-FA-CAT-230 | TC-FA-CAT-E2E-074 | FE+BE |
| TC-FA-CAT-231 | TC-FA-CAT-E2E-072 | FE+BE |
| TC-FA-CAT-232 | TC-FA-CAT-E2E-072 | FE+BE |
| TC-FA-CAT-233 | TC-FA-CAT-E2E-069 | FE+BE |
| TC-FA-CAT-234 | TC-FA-CAT-E2E-074 | FE+BE |
| TC-FA-CAT-235 | TC-FA-CAT-E2E-071 | FE+BE |
| TC-FA-CAT-236 | TC-FA-CAT-E2E-060 | FE+BE |
| TC-FA-CAT-237 | TC-FA-CAT-E2E-042 | FE+BE |
| TC-FA-CAT-238 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-239 | TC-FA-CAT-E2E-074 | FE+BE |
| TC-FA-CAT-240 | TC-FA-CAT-E2E-060 | FE+BE |
| TC-FA-CAT-241 | TC-FA-CAT-E2E-075 | FE+BE |
| TC-FA-CAT-242 | TC-FA-CAT-E2E-076 | FE+BE |
| TC-FA-CAT-243 | TC-FA-CAT-E2E-076 | FE+BE |
| TC-FA-CAT-244 | TC-FA-CAT-E2E-076 | FE+BE |
| TC-FA-CAT-245 | TC-FA-CAT-E2E-077 | FE+BE |
| TC-FA-CAT-246 | TC-FA-CAT-E2E-077 | FE+BE |
| TC-FA-CAT-247 | TC-FA-CAT-E2E-075 | FE+BE |
| TC-FA-CAT-248 | TC-FA-CAT-E2E-075 | FE+BE |
| TC-FA-CAT-249 | TC-FA-CAT-E2E-075 | FE+BE |
| TC-FA-CAT-250 | TC-FA-CAT-E2E-078 | FE+BE |
| TC-FA-CAT-251 | TC-FA-CAT-E2E-078 | FE+BE |
| TC-FA-CAT-252 | TC-FA-CAT-E2E-078 | FE+BE |
| TC-FA-CAT-253 | TC-FA-CAT-E2E-078 | FE+BE |
| TC-FA-CAT-254 | TC-FA-CAT-E2E-071 | FE+BE |
| TC-FA-CAT-255 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-256 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-257 | TC-FA-CAT-E2E-078 | FE+BE |
| TC-FA-CAT-258 | TC-FA-CAT-E2E-079 | FE+BE |
| TC-FA-CAT-259 | TC-FA-CAT-E2E-070 | FE+BE |
| TC-FA-CAT-260 | TC-FA-CAT-E2E-187 | FE+BE |
| TC-FA-CAT-261 | TC-FA-CAT-E2E-072 | FE+BE |
| TC-FA-CAT-262 | TC-FA-CAT-E2E-186 | FE+BE |
| TC-FA-CAT-263 | TC-FA-CAT-E2E-080 | FE+BE |
| TC-FA-CAT-264 | TC-FA-CAT-E2E-071 | FE+BE |
| TC-FA-CAT-265 | TC-FA-CAT-E2E-080 | FE+BE |
| TC-FA-CAT-266 | TC-FA-CAT-E2E-079 | FE+BE |
| TC-FA-CAT-267 | TC-FA-CAT-E2E-079 | FE+BE |
| TC-FA-CAT-268 | TC-FA-CAT-E2E-042 | FE+BE |
| TC-FA-CAT-269 | TC-FA-CAT-E2E-079 | FE+BE |
| TC-FA-CAT-270 | TC-FA-CAT-E2E-010 | FE+BE |
| TC-FA-CAT-271 | TC-FA-CAT-E2E-186 | FE+BE |
| TC-FA-CAT-272 | TC-FA-CAT-E2E-081 | FE+BE |
| TC-FA-CAT-273 | TC-FA-CAT-E2E-081 | FE+BE |
| TC-FA-CAT-274 | TC-FA-CAT-E2E-081 | FE+BE |
| TC-FA-CAT-275 | TC-FA-CAT-E2E-081 | FE+BE |
| TC-FA-CAT-276 | TC-FA-CAT-E2E-082 | FE+BE |
| TC-FA-CAT-277 | TC-FA-CAT-E2E-082 | FE+BE |
| TC-FA-CAT-278 | TC-FA-CAT-E2E-188 | FE+BE |
| TC-FA-CAT-279 | TC-FA-CAT-E2E-188 | FE+BE |
| TC-FA-CAT-280 | TC-FA-CAT-E2E-188 | FE+BE |
| TC-FA-CAT-281 | TC-FA-CAT-E2E-082 | FE+BE |
| TC-FA-CAT-282 | TC-FA-CAT-E2E-082 | FE+BE |
| TC-FA-CAT-283 | TC-FA-CAT-E2E-083 | FE+BE |
| TC-FA-CAT-284 | TC-FA-CAT-E2E-083 | FE+BE |
| TC-FA-CAT-285 | TC-FA-CAT-E2E-083 | FE+BE |
| TC-FA-CAT-286 | TC-FA-CAT-E2E-111 | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra |
| TC-FA-CAT-287 | TC-FA-CAT-E2E-046 | FE+BE (intercept parsial di atas backend nyata; respons baca list kategori, data aset Popup Detail, dan Changelog ditahan atau dipaksa 5xx lewat `Spectra |
| TC-FA-CAT-288 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-289 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-290 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-291 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-292 | TC-FA-CAT-E2E-085 | FE+BE |
| TC-FA-CAT-293 | TC-FA-CAT-E2E-189 | FE+BE |
| TC-FA-CAT-294 | TC-FA-CAT-E2E-085 | FE+BE |
| TC-FA-CAT-295 | TC-FA-CAT-E2E-085 | FE+BE |
| TC-FA-CAT-296 | TC-FA-CAT-E2E-189 | FE+BE |
| TC-FA-CAT-297 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-298 | TC-FA-CAT-E2E-086 | FE+BE |
| TC-FA-CAT-299 | TC-FA-CAT-E2E-086 | FE+BE |
| TC-FA-CAT-300 | TC-FA-CAT-E2E-111 | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra |
| TC-FA-CAT-301 | TC-FA-CAT-E2E-044 | FE+BE (backend nyata; perubahan plan, Hierarchy Depth Limit, dan cap Category count dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-302 | TC-FA-CAT-E2E-088 | FE+BE |
| TC-FA-CAT-303 | TC-FA-CAT-E2E-095 | FE+BE |
| TC-FA-CAT-304 | TC-FA-CAT-E2E-088 | FE+BE |
| TC-FA-CAT-305 | TC-FA-CAT-E2E-089 | FE+BE |
| TC-FA-CAT-306 | TC-FA-CAT-E2E-089 | FE+BE |
| TC-FA-CAT-307 | TC-FA-CAT-E2E-089 | FE+BE |
| TC-FA-CAT-308 | TC-FA-CAT-E2E-190 | FE+BE |
| TC-FA-CAT-309 | TC-FA-CAT-E2E-190 | FE+BE |
| TC-FA-CAT-310 | TC-FA-CAT-E2E-190 | FE+BE |
| TC-FA-CAT-311 | TC-FA-CAT-E2E-190 | FE+BE |
| TC-FA-CAT-312 | TC-FA-CAT-E2E-088 | FE+BE |
| TC-FA-CAT-313 | TC-FA-CAT-E2E-111 | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra |
| TC-FA-CAT-314 | TC-FA-CAT-E2E-094 | FE+BE |
| TC-FA-CAT-315 | TC-FA-CAT-E2E-094 | FE+BE |
| TC-FA-CAT-316 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-317 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-318 | TC-FA-CAT-E2E-202 | FE+BE |
| TC-FA-CAT-319 | TC-FA-CAT-E2E-095 | FE+BE |
| TC-FA-CAT-320 | TC-FA-CAT-E2E-006 | FE+BE |
| TC-FA-CAT-321 | TC-FA-CAT-E2E-096 | FE+BE |
| TC-FA-CAT-322 | TC-FA-CAT-E2E-096 | FE+BE |
| TC-FA-CAT-323 | TC-FA-CAT-E2E-096 | FE+BE |
| TC-FA-CAT-324 | TC-FA-CAT-E2E-096 | FE+BE |
| TC-FA-CAT-325 | TC-FA-CAT-E2E-096 | FE+BE |
| TC-FA-CAT-326 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-327 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-328 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-329 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-330 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-331 | TC-FA-CAT-E2E-097 | FE+BE |
| TC-FA-CAT-332 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-333 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-334 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-335 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-336 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-337 | TC-FA-CAT-E2E-098 | FE+BE |
| TC-FA-CAT-338 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-339 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-340 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-341 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-342 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-343 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-344 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-345 | TC-FA-CAT-E2E-099 | FE+BE |
| TC-FA-CAT-346 | TC-FA-CAT-E2E-100 | FE+BE |
| TC-FA-CAT-347 | TC-FA-CAT-E2E-100 | FE+BE |
| TC-FA-CAT-348 | TC-FA-CAT-E2E-100 | FE+BE |
| TC-FA-CAT-349 | TC-FA-CAT-E2E-100 | FE+BE |
| TC-FA-CAT-350 | TC-FA-CAT-E2E-101 | FE+BE |
| TC-FA-CAT-351 | TC-FA-CAT-E2E-101 | FE+BE |
| TC-FA-CAT-352 | TC-FA-CAT-E2E-101 | FE+BE |
| TC-FA-CAT-353 | TC-FA-CAT-E2E-102 | FE+BE |
| TC-FA-CAT-354 | TC-FA-CAT-E2E-102 | FE+BE |
| TC-FA-CAT-355 | TC-FA-CAT-E2E-102 | FE+BE |
| TC-FA-CAT-356 | TC-FA-CAT-E2E-103 | FE+BE |
| TC-FA-CAT-357 | TC-FA-CAT-E2E-104 | FE+BE |
| TC-FA-CAT-358 | TC-FA-CAT-E2E-104 | FE+BE |
| TC-FA-CAT-359 | TC-FA-CAT-E2E-103 | FE+BE |
| TC-FA-CAT-360 | TC-FA-CAT-E2E-103 | FE+BE |
| TC-FA-CAT-361 | TC-FA-CAT-E2E-103 | FE+BE |
| TC-FA-CAT-362 | TC-FA-CAT-E2E-103 | FE+BE |
| TC-FA-CAT-363 | TC-FA-CAT-E2E-105 | FE+BE |
| TC-FA-CAT-364 | TC-FA-CAT-E2E-105 | FE+BE |
| TC-FA-CAT-365 | TC-FA-CAT-E2E-105 | FE+BE |
| TC-FA-CAT-366 | TC-FA-CAT-E2E-107 | FE+BE |
| TC-FA-CAT-367 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-368 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-369 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-370 | TC-FA-CAT-E2E-111 | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra |
| TC-FA-CAT-371 | TC-FA-CAT-E2E-109 | FE+BE |
| TC-FA-CAT-372 | TC-FA-CAT-E2E-109 | FE+BE |
| TC-FA-CAT-373 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-374 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-375 | TC-FA-CAT-E2E-110 | FE+BE |
| TC-FA-CAT-376 | TC-FA-CAT-E2E-106 | FE+BE |
| TC-FA-CAT-377 | TC-FA-CAT-E2E-176 | FE+BE |
| TC-FA-CAT-378 | TC-FA-CAT-E2E-106 | FE+BE |
| TC-FA-CAT-379 | TC-FA-CAT-E2E-203 | FE+BE |
| TC-FA-CAT-380 | TC-FA-CAT-E2E-106 | FE+BE |
| TC-FA-CAT-381 | TC-FA-CAT-E2E-106 | FE+BE |
| TC-FA-CAT-382 | TC-FA-CAT-E2E-106 | FE+BE |
| TC-FA-CAT-383 | TC-FA-CAT-E2E-192 | FE+BE |
| TC-FA-CAT-384 | TC-FA-CAT-E2E-192 | FE+BE |
| TC-FA-CAT-385 | TC-FA-CAT-E2E-192 | FE+BE |
| TC-FA-CAT-386 | TC-FA-CAT-E2E-107 | FE+BE |
| TC-FA-CAT-387 | TC-FA-CAT-E2E-191 | FE+BE |
| TC-FA-CAT-388 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-389 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-390 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-391 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-392 | TC-FA-CAT-E2E-005 | FE+BE |
| TC-FA-CAT-393 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-394 | TC-FA-CAT-E2E-113 | FE+BE |
| TC-FA-CAT-395 | TC-FA-CAT-E2E-113 | FE+BE |
| TC-FA-CAT-396 | TC-FA-CAT-E2E-113 | FE+BE |
| TC-FA-CAT-397 | TC-FA-CAT-E2E-115 | FE+BE |
| TC-FA-CAT-398 | TC-FA-CAT-E2E-194 | FE+BE |
| TC-FA-CAT-399 | TC-FA-CAT-E2E-194 | FE+BE |
| TC-FA-CAT-400 | TC-FA-CAT-E2E-116 | FE+BE |
| TC-FA-CAT-401 | TC-FA-CAT-E2E-116 | FE+BE |
| TC-FA-CAT-402 | TC-FA-CAT-E2E-116 | FE+BE |
| TC-FA-CAT-403 | TC-FA-CAT-E2E-116 | FE+BE |
| TC-FA-CAT-404 | TC-FA-CAT-E2E-116 | FE+BE |
| TC-FA-CAT-405 | TC-FA-CAT-E2E-114 | FE+BE |
| TC-FA-CAT-406 | TC-FA-CAT-E2E-117 | FE+BE |
| TC-FA-CAT-407 | TC-FA-CAT-E2E-117 | FE+BE |
| TC-FA-CAT-408 | TC-FA-CAT-E2E-117 | FE+BE |
| TC-FA-CAT-409 | TC-FA-CAT-E2E-119 | FE+BE |
| TC-FA-CAT-410 | TC-FA-CAT-E2E-119 | FE+BE |
| TC-FA-CAT-411 | TC-FA-CAT-E2E-118 | FE+BE |
| TC-FA-CAT-412 | TC-FA-CAT-E2E-121 | FE+BE |
| TC-FA-CAT-413 | TC-FA-CAT-E2E-111 | FE+BE (intercept parsial di atas backend nyata; respons Submit Wizard dan respons Download dipaksa lewat `Spectra |
| TC-FA-CAT-414 | TC-FA-CAT-E2E-122 | FE+BE |
| TC-FA-CAT-415 | TC-FA-CAT-E2E-046 | FE+BE (intercept parsial di atas backend nyata; respons baca list kategori, data aset Popup Detail, dan Changelog ditahan atau dipaksa 5xx lewat `Spectra |
| TC-FA-CAT-416 | TC-FA-CAT-E2E-122 | FE+BE |
| TC-FA-CAT-417 | TC-FA-CAT-E2E-122 | FE+BE |
| TC-FA-CAT-418 | TC-FA-CAT-E2E-112 | FE+BE |
| TC-FA-CAT-419 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-420 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-421 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-422 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-423 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-424 | TC-FA-CAT-E2E-124 | FE+BE |
| TC-FA-CAT-425 | TC-FA-CAT-E2E-124 | FE+BE |
| TC-FA-CAT-426 | TC-FA-CAT-E2E-124 | FE+BE |
| TC-FA-CAT-427 | TC-FA-CAT-E2E-124 | FE+BE |
| TC-FA-CAT-428 | TC-FA-CAT-E2E-125 | FE+BE |
| TC-FA-CAT-429 | TC-FA-CAT-E2E-125 | FE+BE |
| TC-FA-CAT-430 | TC-FA-CAT-E2E-125 | FE+BE |
| TC-FA-CAT-431 | TC-FA-CAT-E2E-125 | FE+BE |
| TC-FA-CAT-432 | TC-FA-CAT-E2E-126 | FE+BE |
| TC-FA-CAT-433 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-434 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-435 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-436 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-437 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-438 | TC-FA-CAT-E2E-133 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-439 | TC-FA-CAT-E2E-123 | FE+BE |
| TC-FA-CAT-440 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-441 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-442 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-443 | TC-FA-CAT-E2E-156 | FE+BE |
| TC-FA-CAT-444 | TC-FA-CAT-E2E-156 | FE+BE |
| TC-FA-CAT-445 | TC-FA-CAT-E2E-156 | FE+BE |
| TC-FA-CAT-446 | TC-FA-CAT-E2E-157 | FE+BE |
| TC-FA-CAT-447 | TC-FA-CAT-E2E-163 | FE+BE |
| TC-FA-CAT-448 | TC-FA-CAT-E2E-156 | FE+BE |
| TC-FA-CAT-449 | TC-FA-CAT-E2E-157 | FE+BE |
| TC-FA-CAT-450 | TC-FA-CAT-E2E-157 | FE+BE |
| TC-FA-CAT-451 | TC-FA-CAT-E2E-157 | FE+BE |
| TC-FA-CAT-452 | TC-FA-CAT-E2E-158 | FE+BE |
| TC-FA-CAT-453 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-454 | TC-FA-CAT-E2E-047 | FE+BE (intercept parsial di atas backend nyata; respons pengambilan daftar Asset Name dan data tabel Wizard dipaksa 5xx atau tanpa respons lewat `Spectra |
| TC-FA-CAT-455 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-456 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-457 | TC-FA-CAT-E2E-155 | FE+BE |
| TC-FA-CAT-458 | TC-FA-CAT-E2E-164 | FE+BE |
| TC-FA-CAT-459 | TC-FA-CAT-E2E-164 | FE+BE |
| TC-FA-CAT-460 | TC-FA-CAT-E2E-164 | FE+BE |
| TC-FA-CAT-461 | TC-FA-CAT-E2E-164 | FE+BE |
| TC-FA-CAT-462 | TC-FA-CAT-E2E-164 | FE+BE |
| TC-FA-CAT-463 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-464 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-465 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-466 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-467 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-468 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-469 | TC-FA-CAT-E2E-166 | FE+BE |
| TC-FA-CAT-470 | TC-FA-CAT-E2E-094 | FE+BE |
| TC-FA-CAT-471 | TC-FA-CAT-E2E-094 | FE+BE |
| TC-FA-CAT-472 | TC-FA-CAT-E2E-094 | FE+BE |
| TC-FA-CAT-473 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-474 | TC-FA-CAT-E2E-166 | FE+BE |
| TC-FA-CAT-475 | TC-FA-CAT-E2E-166 | FE+BE |
| TC-FA-CAT-476 | TC-FA-CAT-E2E-166 | FE+BE |
| TC-FA-CAT-477 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-478 | TC-FA-CAT-E2E-167 | FE+BE |
| TC-FA-CAT-479 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-480 | TC-FA-CAT-E2E-165 | FE+BE |
| TC-FA-CAT-481 | TC-FA-CAT-E2E-170 | FE+BE |
| TC-FA-CAT-482 | TC-FA-CAT-E2E-200 | FE+BE |
| TC-FA-CAT-483 | TC-FA-CAT-E2E-200 | FE+BE |
| TC-FA-CAT-484 | TC-FA-CAT-E2E-170 | FE+BE |
| TC-FA-CAT-485 | TC-FA-CAT-E2E-200 | FE+BE |
| TC-FA-CAT-486 | TC-FA-CAT-E2E-171 | FE+BE |
| TC-FA-CAT-487 | TC-FA-CAT-E2E-171 | FE+BE |
| TC-FA-CAT-488 | TC-FA-CAT-E2E-171 | FE+BE |
| TC-FA-CAT-489 | TC-FA-CAT-E2E-039 | FE+BE |
| TC-FA-CAT-490 | TC-FA-CAT-E2E-199 | FE+BE |
| TC-FA-CAT-491 | TC-FA-CAT-E2E-172 | FE+BE |
| TC-FA-CAT-492 | TC-FA-CAT-E2E-172 | FE+BE |
| TC-FA-CAT-493 | TC-FA-CAT-E2E-172 | FE+BE |
| TC-FA-CAT-494 | TC-FA-CAT-E2E-172 | FE+BE |
| TC-FA-CAT-495 | TC-FA-CAT-E2E-172 | FE+BE |
| TC-FA-CAT-496 | TC-FA-CAT-E2E-109 | FE+BE |
| TC-FA-CAT-497 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-497 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-498 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-498 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-499 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-499 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-500 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-500 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-501 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-501 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-502 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-502 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-503 | TC-FA-CAT-E2E-174 | FE+BE |
| TC-FA-CAT-504 | TC-FA-CAT-E2E-175 | FE+BE |
| TC-FA-CAT-505 | TC-FA-CAT-E2E-175 | FE+BE |
| TC-FA-CAT-506 | TC-FA-CAT-E2E-175 | FE+BE |
| TC-FA-CAT-507 | TC-FA-CAT-E2E-175 | FE+BE |
| TC-FA-CAT-508 | TC-FA-CAT-E2E-174 | FE+BE |
| TC-FA-CAT-509 | TC-FA-CAT-E2E-174 | FE+BE |
| TC-FA-CAT-510 | TC-FA-CAT-E2E-174 | FE+BE |
| TC-FA-CAT-511 | TC-FA-CAT-E2E-176 | FE+BE |
| TC-FA-CAT-512 | TC-FA-CAT-E2E-185 | FE+BE |
| TC-FA-CAT-513 | TC-FA-CAT-E2E-185 | FE+BE |
| TC-FA-CAT-514 | TC-FA-CAT-E2E-176 | FE+BE |
| TC-FA-CAT-515 | TC-FA-CAT-E2E-176 | FE+BE |
| TC-FA-CAT-516 | TC-FA-CAT-E2E-202 | FE+BE |
| TC-FA-CAT-517 | TC-FA-CAT-E2E-181 | FE+BE |
| TC-FA-CAT-518 | TC-FA-CAT-E2E-176 | FE+BE |
| TC-FA-CAT-519 | TC-FA-CAT-E2E-028 | FE+BE |
| TC-FA-CAT-520 | TC-FA-CAT-E2E-029 | FE+BE |
| TC-FA-CAT-521 | TC-FA-CAT-E2E-029 | FE+BE |
| TC-FA-CAT-522 | TC-FA-CAT-E2E-029 | FE+BE |
| TC-FA-CAT-523 | TC-FA-CAT-E2E-029 | FE+BE |
| TC-FA-CAT-524 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-525 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-526 | TC-FA-CAT-E2E-031 | FE+BE |
| TC-FA-CAT-527 | TC-FA-CAT-E2E-043 | FE+BE (backend nyata; pencabutan capability dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-528 | TC-FA-CAT-E2E-044 | FE+BE (backend nyata; perubahan plan, Hierarchy Depth Limit, dan cap Category count dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-529 | TC-FA-CAT-E2E-044 | FE+BE (backend nyata; perubahan plan, Hierarchy Depth Limit, dan cap Category count dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-530 | TC-FA-CAT-E2E-033 | FE+BE |
| TC-FA-CAT-531 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-532 | TC-FA-CAT-E2E-054 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-533 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-534 | TC-FA-CAT-E2E-052 | FE+BE (backend nyata; validasi server dan state tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-535 | TC-FA-CAT-E2E-054 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-536 | TC-FA-CAT-E2E-053 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI dan pembacaan state BE) |
| TC-FA-CAT-537 | TC-FA-CAT-E2E-054 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-538 | TC-FA-CAT-E2E-051 | FE+BE (backend nyata; nilai tersimpan diasersi lewat tabel, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-539 | TC-FA-CAT-E2E-043 | FE+BE (backend nyata; pencabutan capability dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-540 | TC-FA-CAT-E2E-074 | FE+BE |
| TC-FA-CAT-541 | TC-FA-CAT-E2E-183 | FE+BE (backend nyata; pencabutan capability dan Access Level dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-542 | TC-FA-CAT-E2E-183 | FE+BE (backend nyata; pencabutan capability dan Access Level dilakukan Principal Automation lewat sesi API, tanpa intercept) |
| TC-FA-CAT-543 | TC-FA-CAT-E2E-084 | FE+BE |
| TC-FA-CAT-544 | TC-FA-CAT-E2E-095 | FE+BE |
| TC-FA-CAT-545 | TC-FA-CAT-E2E-120 | FE+BE |
| TC-FA-CAT-546 | TC-FA-CAT-E2E-118 | FE+BE |
| TC-FA-CAT-547 | TC-FA-CAT-E2E-127 | FE+BE |
| TC-FA-CAT-548 | TC-FA-CAT-E2E-127 | FE+BE |
| TC-FA-CAT-549 | TC-FA-CAT-E2E-128 | FE+BE |
| TC-FA-CAT-550 | TC-FA-CAT-E2E-129 | FE+BE |
| TC-FA-CAT-551 | TC-FA-CAT-E2E-128 | FE+BE |
| TC-FA-CAT-552 | TC-FA-CAT-E2E-128 | FE+BE |
| TC-FA-CAT-553 | TC-FA-CAT-E2E-129 | FE+BE |
| TC-FA-CAT-554 | TC-FA-CAT-E2E-125 | FE+BE |
| TC-FA-CAT-555 | TC-FA-CAT-E2E-130 | FE+BE |
| TC-FA-CAT-556 | TC-FA-CAT-E2E-130 | FE+BE |
| TC-FA-CAT-557 | TC-FA-CAT-E2E-130 | FE+BE |
| TC-FA-CAT-558 | TC-FA-CAT-E2E-131 | FE+BE |
| TC-FA-CAT-559 | TC-FA-CAT-E2E-131 | FE+BE |
| TC-FA-CAT-560 | TC-FA-CAT-E2E-131 | FE+BE |
| TC-FA-CAT-561 | TC-FA-CAT-E2E-131 | FE+BE |
| TC-FA-CAT-562 | TC-FA-CAT-E2E-132 | FE+BE |
| TC-FA-CAT-563 | TC-FA-CAT-E2E-132 | FE+BE |
| TC-FA-CAT-564 | TC-FA-CAT-E2E-132 | FE+BE |
| TC-FA-CAT-565 | TC-FA-CAT-E2E-158 | FE+BE |
| TC-FA-CAT-566 | TC-FA-CAT-E2E-158 | FE+BE |
| TC-FA-CAT-567 | TC-FA-CAT-E2E-159 | FE+BE |
| TC-FA-CAT-568 | TC-FA-CAT-E2E-160 | FE+BE |
| TC-FA-CAT-569 | TC-FA-CAT-E2E-159 | FE+BE |
| TC-FA-CAT-570 | TC-FA-CAT-E2E-159 | FE+BE |
| TC-FA-CAT-571 | TC-FA-CAT-E2E-160 | FE+BE |
| TC-FA-CAT-572 | TC-FA-CAT-E2E-170 | FE+BE |
| TC-FA-CAT-573 | TC-FA-CAT-E2E-080 | FE+BE |
| TC-FA-CAT-574 | TC-FA-CAT-E2E-077 | FE+BE |
| TC-FA-CAT-575 | TC-FA-CAT-E2E-049 | FE+BE (backend nyata; state tersimpan diasersi lewat tabel dan pembacaan state BE) |
| TC-FA-CAT-576 | TC-FA-CAT-E2E-086 | FE+BE |
| TC-FA-CAT-577 | TC-FA-CAT-E2E-045 | FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra |
| TC-FA-CAT-578 | TC-FA-CAT-E2E-059 | FE+BE |
| TC-FA-CAT-579 | TC-FA-CAT-E2E-168 | FE+BE |
| TC-FA-CAT-579 | TC-FA-CAT-E2E-173 | FE+BE |
| TC-FA-CAT-580 | TC-FA-CAT-E2E-169 | FE+BE |
| TC-FA-CAT-581 | TC-FA-CAT-E2E-005 | FE+BE |
| TC-FA-CAT-582 | TC-FA-CAT-E2E-040 | FE+BE |
| TC-FA-CAT-583 | TC-FA-CAT-E2E-199 | FE+BE |
| TC-FA-CAT-584 | TC-FA-CAT-E2E-113 | FE+BE |
| TC-FA-CAT-585 | TC-FA-CAT-E2E-114 | FE+BE |
| TC-FA-CAT-586 | TC-FA-CAT-E2E-193 | FE+BE |
| TC-FA-CAT-587 | TC-FA-CAT-E2E-121 | FE+BE |
| TC-FA-CAT-588 | TC-FA-CAT-E2E-121 | FE+BE |
| TC-FA-CAT-589 | TC-FA-CAT-E2E-134 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-590 | TC-FA-CAT-E2E-134 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-591 | TC-FA-CAT-E2E-135 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-592 | TC-FA-CAT-E2E-195 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-593 | TC-FA-CAT-E2E-136 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-594 | TC-FA-CAT-E2E-137 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-595 | TC-FA-CAT-E2E-161 | FE+BE |
| TC-FA-CAT-596 | TC-FA-CAT-E2E-161 | FE+BE |
| TC-FA-CAT-597 | TC-FA-CAT-E2E-162 | FE+BE |
| TC-FA-CAT-598 | TC-FA-CAT-E2E-162 | FE+BE |
| TC-FA-CAT-599 | TC-FA-CAT-E2E-163 | FE+BE |
| TC-FA-CAT-600 | TC-FA-CAT-E2E-184 | FE+BE (backend nyata; Fallback T-0 dipicu lewat kemampuan T-0 yang disediakan tim FE/BE, tanpa intercept) |
| TC-FA-CAT-601 | TC-FA-CAT-E2E-090 | FE+BE |
| TC-FA-CAT-602 | TC-FA-CAT-E2E-090 | FE+BE |
| TC-FA-CAT-603 | TC-FA-CAT-E2E-090 | FE+BE |
| TC-FA-CAT-604 | TC-FA-CAT-E2E-091 | FE+BE |
| TC-FA-CAT-605 | TC-FA-CAT-E2E-091 | FE+BE |
| TC-FA-CAT-606 | TC-FA-CAT-E2E-091 | FE+BE |
| TC-FA-CAT-607 | TC-FA-CAT-E2E-092 | FE+BE |
| TC-FA-CAT-608 | TC-FA-CAT-E2E-092 | FE+BE |
| TC-FA-CAT-609 | TC-FA-CAT-E2E-092 | FE+BE |
| TC-FA-CAT-610 | TC-FA-CAT-E2E-092 | FE+BE |
| TC-FA-CAT-611 | TC-FA-CAT-E2E-093 | FE+BE |
| TC-FA-CAT-612 | TC-FA-CAT-E2E-093 | FE+BE |
| TC-FA-CAT-613 | TC-FA-CAT-E2E-136 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-614 | TC-FA-CAT-E2E-109 | FE+BE |
| TC-FA-CAT-615 | TC-FA-CAT-E2E-108 | FE+BE |
| TC-FA-CAT-616 | TC-FA-CAT-E2E-005 | FE+BE |
| TC-FA-CAT-617 | TC-FA-CAT-E2E-137 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-618 | TC-FA-CAT-E2E-179 | FE+BE |
| TC-FA-CAT-619 | TC-FA-CAT-E2E-179 | FE+BE |
| TC-FA-CAT-620 | TC-FA-CAT-E2E-050 | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra |
| TC-FA-CAT-621 | TC-FA-CAT-E2E-050 | FE+BE (backend nyata; penundaan respons Edit pada TC-FA-CAT-171 memakai `Spectra |
| TC-FA-CAT-622 | TC-FA-CAT-E2E-087 | FE+BE |
| TC-FA-CAT-623 | TC-FA-CAT-E2E-087 | FE+BE |
| TC-FA-CAT-624 | TC-FA-CAT-E2E-019 | FE+BE |
| TC-FA-CAT-625 | TC-FA-CAT-E2E-058 | FE+BE |
| TC-FA-CAT-626 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-627 | TC-FA-CAT-E2E-019 | FE+BE |
| TC-FA-CAT-628 | TC-FA-CAT-E2E-045 | FE+BE (intercept parsial di atas backend nyata; respons Create dan Add Subcategory dipaksa lewat `Spectra |
| TC-FA-CAT-629 | TC-FA-CAT-E2E-042 | FE+BE |
| TC-FA-CAT-630 | TC-FA-CAT-E2E-048 | FE+BE (backend nyata; dua sesi UI Total Control melakukan Submit hampir bersamaan, tanpa intercept) |
| TC-FA-CAT-631 | TC-FA-CAT-E2E-185 | FE+BE |
| TC-FA-CAT-632 | TC-FA-CAT-E2E-054 | FE+BE (backend nyata; nilai tersimpan diasersi lewat UI, Changelog, dan pembacaan state BE) |
| TC-FA-CAT-633 | TC-FA-CAT-E2E-068 | FE+BE |
| TC-FA-CAT-634 | TC-FA-CAT-E2E-079 | FE+BE |
| TC-FA-CAT-635 | TC-FA-CAT-E2E-083 | FE+BE |
| TC-FA-CAT-636 | TC-FA-CAT-E2E-191 | FE+BE |
| TC-FA-CAT-637 | TC-FA-CAT-E2E-174 | FE+BE |
| TC-FA-CAT-638 | TC-FA-CAT-E2E-009 | FE+BE |
| TC-FA-CAT-639 | TC-FA-CAT-E2E-008 | FE+BE |
| TC-FA-CAT-640 | TC-FA-CAT-E2E-010 | FE+BE |
| TC-FA-CAT-641 | TC-FA-CAT-E2E-008 | FE+BE |
| TC-FA-CAT-642 | TC-FA-CAT-E2E-010 | FE+BE |
| TC-FA-CAT-643 | TC-FA-CAT-E2E-008 | FE+BE |
| TC-FA-CAT-644 | TC-FA-CAT-E2E-008 | FE+BE |
| TC-FA-CAT-645 | TC-FA-CAT-E2E-047 | FE+BE (intercept parsial di atas backend nyata; respons pengambilan daftar Asset Name dan data tabel Wizard dipaksa 5xx atau tanpa respons lewat `Spectra |
| TC-FA-CAT-646 | TC-FA-CAT-E2E-047 | FE+BE (intercept parsial di atas backend nyata; respons pengambilan daftar Asset Name dan data tabel Wizard dipaksa 5xx atau tanpa respons lewat `Spectra |
| TC-FA-CAT-647 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-648 | TC-FA-CAT-E2E-041 | FE+BE |
| TC-FA-CAT-649 | TC-FA-CAT-E2E-037 | FE+BE |
| TC-FA-CAT-650 | TC-FA-CAT-E2E-036 | FE+BE |
| TC-FA-CAT-651 | TC-FA-CAT-E2E-138 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-652 | TC-FA-CAT-E2E-138 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-653 | TC-FA-CAT-E2E-196 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-654 | TC-FA-CAT-E2E-139 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-655 | TC-FA-CAT-E2E-139 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-656 | TC-FA-CAT-E2E-140 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-657 | TC-FA-CAT-E2E-140 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-658 | TC-FA-CAT-E2E-141 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-659 | TC-FA-CAT-E2E-141 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-660 | TC-FA-CAT-E2E-143 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-661 | TC-FA-CAT-E2E-143 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-662 | TC-FA-CAT-E2E-143 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-663 | TC-FA-CAT-E2E-144 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-664 | TC-FA-CAT-E2E-144 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-665 | TC-FA-CAT-E2E-144 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-666 | TC-FA-CAT-E2E-144 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-667 | TC-FA-CAT-E2E-145 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-668 | TC-FA-CAT-E2E-204 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-669 | TC-FA-CAT-E2E-150 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-670 | TC-FA-CAT-E2E-154 | FE+BE |
| TC-FA-CAT-671 | TC-FA-CAT-E2E-152 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-672 | TC-FA-CAT-E2E-154 | FE+BE |
| TC-FA-CAT-673 | TC-FA-CAT-E2E-146 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-674 | TC-FA-CAT-E2E-150 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-675 | TC-FA-CAT-E2E-150 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-676 | TC-FA-CAT-E2E-152 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-677 | TC-FA-CAT-E2E-151 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-678 | TC-FA-CAT-E2E-146 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-679 | TC-FA-CAT-E2E-141 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-680 | TC-FA-CAT-E2E-149 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-681 | TC-FA-CAT-E2E-151 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-682 | TC-FA-CAT-E2E-139 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-683 | TC-FA-CAT-E2E-140 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-684 | TC-FA-CAT-E2E-198 | FE+BE |
| TC-FA-CAT-685 | TC-FA-CAT-E2E-197 | FE+BE |
| TC-FA-CAT-686 | TC-FA-CAT-E2E-152 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-687 | TC-FA-CAT-E2E-147 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-688 | TC-FA-CAT-E2E-141 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-689 | TC-FA-CAT-E2E-142 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-690 | TC-FA-CAT-E2E-142 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-691 | TC-FA-CAT-E2E-145 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-692 | TC-FA-CAT-E2E-142 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-693 | TC-FA-CAT-E2E-153 | FE+BE |
| TC-FA-CAT-694 | TC-FA-CAT-E2E-148 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-695 | TC-FA-CAT-E2E-148 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-696 | TC-FA-CAT-E2E-153 | FE+BE |
| TC-FA-CAT-697 | TC-FA-CAT-E2E-148 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-698 | TC-FA-CAT-E2E-147 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-699 | TC-FA-CAT-E2E-149 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-700 | TC-FA-CAT-E2E-149 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-701 | TC-FA-CAT-E2E-151 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-702 | TC-FA-CAT-E2E-205 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
| TC-FA-CAT-703 | TC-FA-CAT-E2E-151 | FE+BE (backend nyata; Popup Detail Category dan tabel Assets dibaca dari data seed Pre-setup) |
