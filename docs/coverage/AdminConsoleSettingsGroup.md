# Coverage E2E — Admin Console > Settings > Group

Sumber: `admin-console/settings-group/TestCases/tc-settings-group.md` (404 TC granular aktif; seluruhnya TC FE).
File backend `tc-settings-group-backend.md` hanya dicek keberadaannya untuk mengenali TC yang tidak punya antarmuka; tidak ada TC seperti itu.
Suite: `specs/AdminConsole/SettingsGroup/`.
Prefix Modul: `AC` + `SG` (`TC-AC-SG-E2E-*`). `executionOrder: 1.2`, suite serial (`parallel: false`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (116 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar | Screening Halaman Settings > Group: Tabel Utama, Group Context Header, Kolom, dan Toolbar | FE+BE | 51 | TC-AC-SG-01, TC-AC-SG-02, TC-AC-SG-03, TC-AC-SG-04 |
| TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | Screening Breadcrumb, Klik Baris, Hover Path, Modified By, dan Overlay Row Action | FE+BE | 32 | TC-AC-SG-05, TC-AC-SG-06, TC-AC-SG-07, TC-AC-SG-08, TC-AC-SG-09 |
| TC-AC-SG-E2E-003-loading-state-dan-empty-state-node-tanpa-subgroup | Loading State Tabel dan Empty State Node Tanpa Subgroup | FE+BE (intercept) | 10 | TC-AC-SG-10, TC-AC-SG-13 |
| TC-AC-SG-E2E-004-empty-state-entitas-tanpa-group-dan-entitas-satu-group | Empty State Entitas Tanpa Group dan Entitas dengan Satu Group | FE+BE | 12 | TC-AC-SG-12, TC-AC-SG-14 |
| TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | Sidebar Group Tree: Screening, Default, Expand/Collapse, dan Search | FE+BE | 39 | TC-AC-SG-15, TC-AC-SG-16, TC-AC-SG-18, TC-AC-SG-19, TC-AC-SG-20 |
| TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight | Sidebar Group Tree: Hapus Search, Label Panjang, Tombol Elipsis, dan Highlight Node | FE+BE | 27 | TC-AC-SG-21, TC-AC-SG-25, TC-AC-SG-26, TC-AC-SG-27 |
| TC-AC-SG-E2E-007-sidebar-group-tree-toggle-persistensi-dan-collapse-otomatis | Sidebar Group Tree: Toggle Open/Collapsed, Persistensi per User, dan Collapse Otomatis di Bawah 1280px | FE+BE | 27 | TC-AC-SG-22, TC-AC-SG-23, TC-AC-SG-24 |
| TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | Semantik Pilih Node: Descendant Rekursif, All Groups, Exclusive, Toggle Off, dan Reset Pagination | FE+BE | 31 | TC-AC-SG-28, TC-AC-SG-29, TC-AC-SG-30, TC-AC-SG-31, TC-AC-SG-35 |
| TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header | Group Context Header: Angka Node Sendiri, Tanpa Badge, Elipsis Node Header, dan Angka Tetap saat Search atau Filter | FE+BE | 30 | TC-AC-SG-33, TC-AC-SG-34, TC-AC-SG-36, TC-AC-SG-400 |
| TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | Total User Node: Union, Dedup, Tanpa Pewarisan Ancestor, Tanpa Filter Status, dan Tidak Pernah 0 | FE+BE | 32 | TC-AC-SG-37, TC-AC-SG-38, TC-AC-SG-39, TC-AC-SG-40, TC-AC-SG-45 |
| TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived | Total Member Node: Active/Suspended Langsung, Tidak Rekursif, Nilai 0 Tetap Link, dan Archived Tidak Dihitung | FE+BE | 26 | TC-AC-SG-41, TC-AC-SG-42, TC-AC-SG-43, TC-AC-SG-44 |
| TC-AC-SG-E2E-012-guided-tooltip-kunjungan-pertama-navigasi-dan-tombol-bantuan | Guided Tooltip Settings > Group: Kunjungan Pertama, Back/Skip, dan Tombol [?] | FE+BE | 40 | TC-AC-SG-46, TC-AC-SG-47, TC-AC-SG-48 |
| TC-AC-SG-E2E-013-guided-tooltip-tidak-muncul-lagi-resize-dan-keyboard | Guided Tooltip Settings > Group: Tidak Muncul Lagi Setelah Selesai, Resize Menutup Tanpa Seen, dan Keyboard | FE+BE | 26 | TC-AC-SG-49, TC-AC-SG-50, TC-AC-SG-51 |
| TC-AC-SG-E2E-014-mobile-android-card-list-bottom-sheet-tree-dan-toolbar | Mobile Android: Card List, Bottom Sheet Tree, dan Toolbar Settings > Group | FE+BE | 23 | TC-AC-SG-52, TC-AC-SG-53, TC-AC-SG-54 |
| TC-AC-SG-E2E-015-mobile-android-long-press-selection-mode-dan-bulk-delete | Mobile Android: Long-Press Masuk Selection Mode dan Bulk Delete Tersedia | FE+BE | 22 | TC-AC-SG-393 |
| TC-AC-SG-E2E-016-role-matrix-entity-gate-distributor-partner-dan-client | Role Matrix: Entity Gate Distributor, Partner, dan Client pada Settings > Group | FE+BE | 19 | TC-AC-SG-57, TC-AC-SG-58, TC-AC-SG-59 |
| TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | Role Matrix: Total Control, Default User, dan Read Only pada Settings > Group | FE+BE | 38 | TC-AC-SG-17, TC-AC-SG-60, TC-AC-SG-61, TC-AC-SG-62, TC-AC-SG-77 |
| TC-AC-SG-E2E-018-role-matrix-group-manager-dan-role-tanpa-manage-group-tanpa-akses-menu | Role Matrix: Group Manager dan Role Lain tanpa Manage group Tidak Punya Akses Menu Settings > Group | FE+BE | 13 | TC-AC-SG-63, TC-AC-SG-64 |
| TC-AC-SG-E2E-019-role-matrix-visibilitas-kontrol-manage-group-cud-dan-create-saja | Role Matrix: Visibilitas Kontrol Manage group Create, Update, Delete dan Create Saja | FE+BE | 34 | TC-AC-SG-65, TC-AC-SG-66 |
| TC-AC-SG-E2E-020-role-matrix-visibilitas-kontrol-manage-group-delete-saja-create-update-dan-kolom-checkbox-tanpa-delete | Role Matrix: Visibilitas Kontrol Manage group Delete Saja, Create + Update, dan Kolom Checkbox tanpa Delete | FE+BE | 36 | TC-AC-SG-68, TC-AC-SG-69, TC-AC-SG-172 |
| TC-AC-SG-E2E-021-role-matrix-visibilitas-kontrol-manage-group-update-delete-dan-tanpa-capability-mutasi | Role Matrix: Visibilitas Kontrol Manage group Update + Delete dan tanpa Capability Mutasi | FE+BE | 23 | TC-AC-SG-71, TC-AC-SG-72 |
| TC-AC-SG-E2E-022-manage-group-create-add-subgroup-level-satu-dan-dalam-tanpa-penugasan-otomatis-ke-pembuat | Manage group Create: Add Subgroup Level 1 dan Dalam, tanpa Penugasan Otomatis ke Pembuat | FE+BE | 21 | TC-AC-SG-73, TC-AC-SG-97 |
| TC-AC-SG-E2E-023-manage-group-update-rename-level-satu-dan-dalam-tree-entity-wide | Manage group Update: Rename Level 1 dan Dalam, Tree Penuh Entity-Wide | FE+BE | 24 | TC-AC-SG-74, TC-AC-SG-76 |
| TC-AC-SG-E2E-024-manage-group-delete-menghapus-group-lewat-checkbox-bulk-dan-delete | Manage group Delete: Menghapus Group lewat Checkbox Bulk dan Delete | FE+BE | 12 | TC-AC-SG-75 |
| TC-AC-SG-E2E-025-popup-create-screening-new-group-dan-add-subgroup-beserta-konteks-under | Popup Create: Screening New Group dan Add Subgroup beserta Konteks Under | FE+BE | 23 | TC-AC-SG-78, TC-AC-SG-79, TC-AC-SG-80 |
| TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | Popup Create: Validasi Group Name (Kosong, 120 Karakter, Duplikat, All Groups, Clear Field) | FE+BE | 34 | TC-AC-SG-81, TC-AC-SG-82, TC-AC-SG-84, TC-AC-SG-87, TC-AC-SG-88 |
| TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | Create Group: Stay on Form, Trim, dan Nama Sama pada Parent atau Entitas Berbeda | FE+BE | 41 | TC-AC-SG-83, TC-AC-SG-85, TC-AC-SG-86, TC-AC-SG-89, TC-AC-SG-90 |
| TC-AC-SG-E2E-028-create-subgroup-parent-pemilik-aksi-elipsis-sidebar-dan-level-satu-saat-node-lain-terpilih | Create Subgroup: Parent Pemilik Aksi, Elipsis Sidebar, dan Level 1 saat Node Lain Terpilih | FE+BE | 22 | TC-AC-SG-91, TC-AC-SG-92, TC-AC-SG-93 |
| TC-AC-SG-E2E-029-create-group-scope-tabel-node-terpilih-urutan-alfabetis-sidebar-dan-total-user-member-node-baru | Create Group: Scope Tabel Node Terpilih, Urutan Alfabetis Sidebar, dan Total User/Member Node Baru | FE+BE | 25 | TC-AC-SG-94, TC-AC-SG-95, TC-AC-SG-96 |
| TC-AC-SG-E2E-030-create-group-saving-state-dan-klik-submit-ganda | Create Group: Saving State dan Klik Submit Ganda | FE+BE | 17 | TC-AC-SG-104, TC-AC-SG-106 |
| TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop | Popup Create: Unsaved Changes lewat Close, Esc, Popup Kosong, dan Backdrop | FE+BE | 29 | TC-AC-SG-98, TC-AC-SG-99, TC-AC-SG-100, TC-AC-SG-101 |
| TC-AC-SG-E2E-032-popup-create-terisi-reload-dan-navigasi-in-app | Popup Create Terisi: Reload dan Navigasi In-App | FE+BE | 28 | TC-AC-SG-102, TC-AC-SG-103 |
| TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | Create Subgroup dan Hierarchy Depth Limit: Limit-1, Sama dengan Limit, Limit+1, Level 1, Cek Ulang Server, dan Penurunan Limit | FE+BE | 42 | TC-AC-SG-107, TC-AC-SG-108, TC-AC-SG-109, TC-AC-SG-110, TC-AC-SG-111, TC-AC-SG-112 |
| TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header | Popup Edit: Screening dan Rename dari Row Action dan Elipsis Sidebar, Update Group Context Header | FE+BE | 38 | TC-AC-SG-113, TC-AC-SG-114, TC-AC-SG-115, TC-AC-SG-116 |
| TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | Edit Group: Validasi (Kosong, Lebih dari 120, Sibling Duplikat, All Groups, Clear Field) | FE+BE | 32 | TC-AC-SG-118, TC-AC-SG-119, TC-AC-SG-120, TC-AC-SG-122, TC-AC-SG-124 |
| TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group | Edit Group: Huruf Besar/Kecil, Nama Sama pada Parent Berbeda, Trim, dan Rename Default Group | FE+BE | 35 | TC-AC-SG-117, TC-AC-SG-121, TC-AC-SG-123, TC-AC-SG-128 |
| TC-AC-SG-E2E-037-edit-group-unsaved-changes-bersyarat-tanpa-pindah-parent-dan-referensi-user-entitas-tidak-putus | Edit Group: Unsaved Changes Bersyarat, Tanpa Pindah Parent, dan Referensi User/Entitas Tidak Putus | FE+BE | 29 | TC-AC-SG-126, TC-AC-SG-129, TC-AC-SG-130 |
| TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | Delete Group: Dialog Warning D-04, Cancel, Backdrop, Tooltip Full Path, dan Elipsis Sidebar | FE+BE | 33 | TC-AC-SG-131, TC-AC-SG-132, TC-AC-SG-135, TC-AC-SG-149, TC-AC-SG-150 |
| TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | Delete Group Diblok karena Entitas Menempel (D-03): Langsung, Descendant, Archived, Partner, dan Distributor Principal | FE+BE | 31 | TC-AC-SG-136, TC-AC-SG-137, TC-AC-SG-138, TC-AC-SG-139, TC-AC-SG-398 |
| TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group | Delete Group Diblok karena Group Terakhir (D-02) dan Guard Seluruh Group | FE+BE | 26 | TC-AC-SG-140, TC-AC-SG-141, TC-AC-SG-142, TC-AC-SG-143 |
| TC-AC-SG-E2E-041-delete-group-konfirmasi-hapus-subtree-pelepasan-group-role-manager-dan-klik-ganda | Delete Group: Konfirmasi Menghapus Subtree, Pelepasan Group Role dan Group Manager, dan Klik Ganda | FE+BE | 26 | TC-AC-SG-133, TC-AC-SG-146, TC-AC-SG-148 |
| TC-AC-SG-E2E-042-bulk-delete-bulk-actions-bar-select-all-unselect-all-dan-checkbox-header | Bulk Delete: Bulk Actions Bar, Select All dan Unselect All, serta Checkbox Header | FE+BE | 30 | TC-AC-SG-151, TC-AC-SG-152, TC-AC-SG-153 |
| TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel | Bulk Delete: Seleksi Lintas Halaman dan Search, Reset oleh Node, Batas Node Terpilih, dan Cancel | FE+BE | 49 | TC-AC-SG-154, TC-AC-SG-155, TC-AC-SG-156, TC-AC-SG-167 |
| TC-AC-SG-E2E-044-bulk-delete-homogen-campuran-dan-seluruh-baris-punya-member | Bulk Delete: Homogen Tanpa Entitas, Campuran dengan Skip Member, dan Seluruh Baris Punya Member | FE+BE | 25 | TC-AC-SG-157, TC-AC-SG-158, TC-AC-SG-159 |
| TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit | Bulk Delete: Collapse ke Dialog Single, Nama Baris Terpilih Saja, dan Reset Seleksi Setelah Commit | FE+BE | 35 | TC-AC-SG-160, TC-AC-SG-161, TC-AC-SG-168, TC-AC-SG-399 |
| TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08 | Bulk Delete: Guard Menghabiskan Seluruh Group per Entitas (D-08) | FE+BE | 29 | TC-AC-SG-162, TC-AC-SG-165, TC-AC-SG-166, TC-AC-SG-173 |
| TC-AC-SG-E2E-047-bulk-delete-selection-limit-100-seleksi-manual-dan-select-all | Bulk Delete: Selection Limit 100 pada Seleksi Manual dan Select All | FE+BE | 17 | TC-AC-SG-169, TC-AC-SG-170 |
| TC-AC-SG-E2E-048-search-tabel-utama-interaksi-kolom-group-dan-total-user | Search Tabel Utama: Interaksi Input, Kolom Group, dan Kolom Total User | FE+BE | 33 | TC-AC-SG-174, TC-AC-SG-175, TC-AC-SG-176 |
| TC-AC-SG-E2E-049-search-tabel-utama-kolom-total-member-modified-by-dan-last-updated | Search Tabel Utama: Kolom Total Member, Modified By, dan Last Updated | FE+BE | 17 | TC-AC-SG-177, TC-AC-SG-178, TC-AC-SG-179 |
| TC-AC-SG-E2E-050-search-tabel-utama-kolom-di-hide-trim-dan-lokal-terhadap-node-terpilih | Search Tabel Utama: Kolom Di-hide, Trim Query, dan Lokal terhadap Node Terpilih | FE+BE | 24 | TC-AC-SG-180, TC-AC-SG-181, TC-AC-SG-182 |
| TC-AC-SG-E2E-051-filter-tabel-utama-screening-panel-dan-total-user | Filter Tabel Utama: Screening Filter Panel dan Filter Total User | FE+BE | 23 | TC-AC-SG-184, TC-AC-SG-185, TC-AC-SG-186 |
| TC-AC-SG-E2E-052-filter-tabel-utama-total-member-dan-opsi-dropdown-modified-by | Filter Tabel Utama: Filter Total Member dan Opsi Dropdown Modified By | FE+BE | 25 | TC-AC-SG-187, TC-AC-SG-188, TC-AC-SG-189 |
| TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated | Filter Tabel Utama: Modified By, Search Dropdown, dan Last Updated | FE+BE | 28 | TC-AC-SG-190, TC-AC-SG-191, TC-AC-SG-192, TC-AC-SG-193 |
| TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom | Filter Tabel Utama: Logika AND, Clear Field, Tutup Tanpa Apply, dan Independen dari Visibilitas Kolom | FE+BE | 35 | TC-AC-SG-194, TC-AC-SG-195, TC-AC-SG-196, TC-AC-SG-197 |
| TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | Search dan Filter Beririsan: Empty State Kombinasi, Filter Lokal Node, dan Reset Halaman | FE+BE | 33 | TC-AC-SG-198, TC-AC-SG-199, TC-AC-SG-200, TC-AC-SG-201, TC-AC-SG-240 |
| TC-AC-SG-E2E-056-sort-tabel-utama-kolom-group-total-user-dan-total-member | Sort Tabel Utama: Kolom Group, Total User, dan Total Member | FE+BE | 23 | TC-AC-SG-202, TC-AC-SG-203, TC-AC-SG-204 |
| TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | Sort Tabel Utama: Modified By, Last Updated, Pindah Kolom, dan Independen dari Search dan Filter | FE+BE | 29 | TC-AC-SG-205, TC-AC-SG-206, TC-AC-SG-207, TC-AC-SG-208, TC-AC-SG-209 |
| TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder | Overlay Column Visibility Tabel Utama: Hide dan Unhide, Kolom Terakhir, dan Reorder | FE+BE | 22 | TC-AC-SG-210, TC-AC-SG-211, TC-AC-SG-212, TC-AC-SG-213 |
| TC-AC-SG-E2E-059-modal-setup-column-tabel-utama-screening-preview-save-dan-tutup-tanpa-save | Modal Setup Column Tabel Utama: Screening, Preview, Save, dan Tutup Tanpa Save | FE+BE | 26 | TC-AC-SG-214, TC-AC-SG-215, TC-AC-SG-216 |
| TC-AC-SG-E2E-060-setup-column-tabel-utama-reset-to-default-reorder-pin-dan-unpin | Setup Column Tabel Utama: Reset to Default, Reorder, serta Pin dan Unpin | FE+BE | 23 | TC-AC-SG-217, TC-AC-SG-218, TC-AC-SG-219 |
| TC-AC-SG-E2E-061-setup-column-tabel-utama-pin-ke-4-cache-terpisah-dari-popup-dan-max-visible-columns | Setup Column Tabel Utama: Pin ke-4 Diblok, Cache Terpisah dari Popup, dan Max Visible Columns | FE+BE | 20 | TC-AC-SG-220, TC-AC-SG-221, TC-AC-SG-222 |
| TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous | Pagination Tabel Utama: Default, Page Size, Input Nomor Halaman, dan Next/Previous | FE+BE | 19 | TC-AC-SG-223, TC-AC-SG-224, TC-AC-SG-225, TC-AC-SG-226 |
| TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu | Persistensi State List: F5, Back Browser, Search Sidebar, dan Klik Ulang Menu Group | FE+BE | 35 | TC-AC-SG-227, TC-AC-SG-228, TC-AC-SG-229, TC-AC-SG-230 |
| TC-AC-SG-E2E-064-download-tabel-utama-overlay-csv-xlsx-dan-hasil-search-filter-aktif | Download Tabel Utama: Overlay CSV dan XLSX serta Hasil Search dan Filter Aktif | FE+BE | 11 | TC-AC-SG-231, TC-AC-SG-234 |
| TC-AC-SG-E2E-065-download-tabel-utama-kolom-di-hide-node-terpilih-dan-hasil-kosong | Download Tabel Utama: Kolom Di-hide, Node Terpilih, dan Hasil Kosong | FE+BE | 18 | TC-AC-SG-235, TC-AC-SG-237, TC-AC-SG-238 |
| TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog | Isi File Export: Sel Numerik XLSX, Full Path Kolom Group, dan Snapshot Path Changelog | FE+BE | 39 | TC-AC-SG-233, TC-AC-SG-236, TC-AC-SG-395, TC-AC-SG-396 |
| TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom | Modal Changelog: Screening, Empty State, dan Tampilan Data Kolom | FE+BE | 31 | TC-AC-SG-241, TC-AC-SG-242, TC-AC-SG-243, TC-AC-SG-244 |
| TC-AC-SG-E2E-068-modal-changelog-search-kolom-action-group-name-dan-field | Modal Changelog: Search Kolom Action, Group Name, dan Field | FE+BE | 25 | TC-AC-SG-245, TC-AC-SG-246, TC-AC-SG-247 |
| TC-AC-SG-E2E-069-modal-changelog-search-kolom-old-value-new-value-dan-modified-by | Modal Changelog: Search Kolom Old Value, New Value, dan Modified By | FE+BE | 24 | TC-AC-SG-248, TC-AC-SG-249, TC-AC-SG-250 |
| TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name | Modal Changelog: Search Date, Panel Filter, dan Opsi Action serta Group Name | FE+BE | 28 | TC-AC-SG-251, TC-AC-SG-252, TC-AC-SG-253, TC-AC-SG-254 |
| TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | Modal Changelog: Filter Group Name, Modified By, Date, Kombinasi AND, dan Independensi Kontrol | FE+BE | 37 | TC-AC-SG-255, TC-AC-SG-256, TC-AC-SG-257, TC-AC-SG-258, TC-AC-SG-259 |
| TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field | Modal Changelog: Sort Kolom Date, Action, Group Name, dan Field | FE+BE | 27 | TC-AC-SG-260, TC-AC-SG-261, TC-AC-SG-262, TC-AC-SG-263 |
| TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination | Modal Changelog: Sort Kolom Old Value, New Value, Modified By, dan Pagination | FE+BE | 25 | TC-AC-SG-264, TC-AC-SG-265, TC-AC-SG-266, TC-AC-SG-268 |
| TC-AC-SG-E2E-074-modal-changelog-setup-column-tutup-modal-dan-snapshot-immutable | Modal Changelog: Setup Column, Tutup Modal, dan Snapshot Immutable | FE+BE | 29 | TC-AC-SG-267, TC-AC-SG-271, TC-AC-SG-272 |
| TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | Popup Total User Detail: Screening, Identitas Path, Group Role, Kolom Name, dan Penutupan | FE+BE | 33 | TC-AC-SG-273, TC-AC-SG-274, TC-AC-SG-275, TC-AC-SG-276, TC-AC-SG-277 |
| TC-AC-SG-E2E-076-popup-users-search-kolom-name-email-dan-position | Popup Users: Search Kolom Name, Email, dan Position | FE+BE | 25 | TC-AC-SG-278, TC-AC-SG-279, TC-AC-SG-280 |
| TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide | Popup Users: Search Kolom Division, Group Role, Curated, dan Kolom di-Hide | FE+BE | 30 | TC-AC-SG-281, TC-AC-SG-282, TC-AC-SG-283, TC-AC-SG-284 |
| TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | Popup Users: Panel Filter, Opsi dan Filter Group Role, dan Tier Tanpa Pemegang | FE+BE | 33 | TC-AC-SG-285, TC-AC-SG-286, TC-AC-SG-287, TC-AC-SG-288, TC-AC-SG-289 |
| TC-AC-SG-E2E-079-popup-users-filter-position-division-activation-status-dan-temporary-user | Popup Users: Filter Position, Division, Activation Status, dan Temporary User | FE+BE | 28 | TC-AC-SG-290, TC-AC-SG-291 |
| TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | Popup Users: Clear Field, Search Tanpa Hasil, dan Sort Name, Email, Position | FE+BE | 34 | TC-AC-SG-294, TC-AC-SG-295, TC-AC-SG-296, TC-AC-SG-297, TC-AC-SG-298 |
| TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | Popup Users: Sort Division dan Group Role, Kolom TAG, Nilai Kosong, dan Urutan Bawaan | FE+BE | 28 | TC-AC-SG-299, TC-AC-SG-300, TC-AC-SG-301, TC-AC-SG-305, TC-AC-SG-306 |
| TC-AC-SG-E2E-082-popup-users-setup-column-cache-terpisah-dan-max-visible-columns | Popup Users: Setup Column, Cache Terpisah, dan Max Visible Columns | FE+BE | 39 | TC-AC-SG-302, TC-AC-SG-303, TC-AC-SG-304 |
| TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | Popup Total Member Detail: Screening, Empty 0, Kolom Type, Penutupan, dan Tree Distributor | FE+BE | 38 | TC-AC-SG-307, TC-AC-SG-308, TC-AC-SG-309, TC-AC-SG-310, TC-AC-SG-397 |
| TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated | Popup Members: Search Kolom Entity Name, Type, Relation Status, dan Last Updated | FE+BE | 28 | TC-AC-SG-311, TC-AC-SG-312, TC-AC-SG-313, TC-AC-SG-314 |
| TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | Popup Members: Panel Filter, Type, Relation Status, Last Updated, dan Kombinasi | FE+BE | 27 | TC-AC-SG-315, TC-AC-SG-316, TC-AC-SG-317, TC-AC-SG-318, TC-AC-SG-319 |
| TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | Popup Members: Sort Keempat Kolom dan Setup Column | FE+BE | 37 | TC-AC-SG-320, TC-AC-SG-321, TC-AC-SG-322, TC-AC-SG-323, TC-AC-SG-324 |
| TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log | Pencatatan Create dan Edit Group: Changelog, System Log, dan Activity Log | FE+BE | 47 | TC-AC-SG-325, TC-AC-SG-326, TC-AC-SG-327, TC-AC-SG-340 |
| TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager | Pencatatan Delete Single dan Bulk: Satu Entri per Node dan per Group, Pelepasan Group Manager | FE+BE | 49 | TC-AC-SG-329, TC-AC-SG-330, TC-AC-SG-333, TC-AC-SG-334 |
| TC-AC-SG-E2E-089-pencatatan-seed-onboarding-dan-activity-log-entity-bound | Pencatatan Seed Onboarding Default Group dan Activity Log Entity-Bound | FE+BE | 15 | TC-AC-SG-338, TC-AC-SG-339 |
| TC-AC-SG-E2E-090-absence-log-edit-tanpa-perubahan | Absence Log Edit Group Tanpa Perubahan di Changelog, Activity Log, dan System Log | FE+BE | 44 | TC-AC-SG-125, TC-AC-SG-328 |
| TC-AC-SG-E2E-091-absence-log-delete-cancel-skip-bulk-dan-diblok-dialog | Absence Log Delete: Cancel, Skip pada Bulk, dan Diblok Dialog | FE+BE | 46 | TC-AC-SG-134, TC-AC-SG-331, TC-AC-SG-332 |
| TC-AC-SG-E2E-092-sinkron-lintas-modul-settings-user-dan-role-permission-setelah-create-dan-rename | Sinkron Lintas Modul: Group Baru dan Rename Terefleksi di Settings > User dan Role & Permission | FE+BE | 31 | TC-AC-SG-341, TC-AC-SG-343, TC-AC-SG-348 |
| TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor | Sinkron Lintas Modul: Reassign Entitas, Total User dari Group Role dan Read Only, serta Create Distributor | FE+BE | 50 | TC-AC-SG-349, TC-AC-SG-350, TC-AC-SG-353, TC-AC-SG-354 |
| TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history | Sinkron Lintas Modul setelah Delete: Settings > User, Tab Role, Group Manager List, dan Akses History | FE+BE | 45 | TC-AC-SG-344, TC-AC-SG-345, TC-AC-SG-346, TC-AC-SG-347 |
| TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | Defense-in-Depth: Isolasi Entitas dan Penolakan 403 per Role lewat Request Langsung | FE+BE | 35 | TC-AC-SG-355, TC-AC-SG-356, TC-AC-SG-357, TC-AC-SG-358, TC-AC-SG-359, TC-AC-SG-360, TC-AC-SG-361, TC-AC-SG-362 |
| TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | Defense-in-Depth: Root All Groups, Parent, Duplikat, Depth Limit, Guard Delete, dan Selection Limit lewat Request Langsung | FE+BE | 30 | TC-AC-SG-363, TC-AC-SG-364, TC-AC-SG-365, TC-AC-SG-366, TC-AC-SG-367, TC-AC-SG-368, TC-AC-SG-401, TC-AC-SG-402 |
| TC-AC-SG-E2E-097-defense-in-depth-ui-payload-script-sebagai-teks-literal-pada-search-dan-nama-group | Defense-in-Depth UI: Payload Script Dirender sebagai Teks Literal pada Search dan Nama Group | FE+BE | 20 | TC-AC-SG-183, TC-AC-SG-369 |
| TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | State Tenant: Write-Lockdown Suspended pada Create, Edit, Delete, Bulk Delete, dan Add Subgroup di Batas Kedalaman | FE+BE | 56 | TC-AC-SG-370, TC-AC-SG-371, TC-AC-SG-372, TC-AC-SG-373, TC-AC-SG-403, TC-AC-SG-404 |
| TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | State Tenant: Write-Lockdown Expired, Grace Pasca-Expired, dan Archive, serta Grace Downgrade yang Tidak Memblokir | FE+BE | 53 | TC-AC-SG-374, TC-AC-SG-375, TC-AC-SG-376, TC-AC-SG-377, TC-AC-SG-378, TC-AC-SG-379 |
| TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5 | Konkurensi Dua Admin: Create Duplikat, Edit Bersamaan, Refresh SSE, dan Fallback F5 | FE+BE | 49 | TC-AC-SG-380, TC-AC-SG-381, TC-AC-SG-390, TC-AC-SG-392 |
| TC-AC-SG-E2E-101-konkurensi-dua-admin-perubahan-saat-delete-menunggu-konfirmasi-dan-member-baru-saat-bulk | Konkurensi Dua Admin: Perubahan saat Delete Menunggu Konfirmasi dan Member Baru saat Bulk Delete | FE+BE | 29 | TC-AC-SG-383, TC-AC-SG-384, TC-AC-SG-394 |
| TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | Konkurensi Dua Admin: Target Sudah Dihapus Admin Lain pada Add Subgroup, Edit, Delete, dan Bulk Delete | FE+BE | 45 | TC-AC-SG-385, TC-AC-SG-386, TC-AC-SG-387, TC-AC-SG-388, TC-AC-SG-389 |
| TC-AC-SG-E2E-103-konkurensi-dua-admin-delete-bersamaan-menghabiskan-group-dan-invarian-minimal-satu-group | Konkurensi Dua Admin: Delete Bersamaan Menghabiskan Group dan Invarian Minimal Satu Group | FE+BE | 19 | TC-AC-SG-382, TC-AC-SG-391 |
| TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download | Resilience Principal: Error Load Tabel, Gagal Server pada Create dan Edit, serta Download Gagal | FE+BE (intercept) | 42 | TC-AC-SG-11, TC-AC-SG-105, TC-AC-SG-127, TC-AC-SG-239 |
| TC-AC-SG-E2E-105-resilience-distributor-gagal-server-delete-bulk-delete-dan-download-changelog | Resilience Distributor: Gagal Server pada Delete, Bulk Delete, dan Download Changelog | FE+BE (intercept) | 33 | TC-AC-SG-147, TC-AC-SG-171, TC-AC-SG-270 |
| TC-AC-SG-E2E-106-total-user-agregat-all-groups-user-distinct-bukan-penjumlahan-per-node | Total User dan Total Member Agregat All Groups adalah Distinct, Bukan Penjumlahan per Node | FE+BE | 5 | TC-AC-SG-32 |
| TC-AC-SG-E2E-107-mobile-android-akses-changelog-dan-popup-create-edit-delete-bottom-sheet | Mobile Android: Akses Changelog dari Header dan Popup Create, Edit, serta Delete sebagai Bottom Sheet | FE+BE | 30 | TC-AC-SG-55, TC-AC-SG-56 |
| TC-AC-SG-E2E-108-role-matrix-visibilitas-kontrol-manage-group-update-saja | Role Matrix: Visibilitas Kontrol Manage group Update Saja | FE+BE | 17 | TC-AC-SG-67 |
| TC-AC-SG-E2E-109-role-matrix-visibilitas-kontrol-manage-group-create-delete | Role Matrix: Visibilitas Kontrol Manage group Create + Delete | FE+BE | 17 | TC-AC-SG-70 |
| TC-AC-SG-E2E-110-delete-group-fallback-seleksi-ke-all-groups-setelah-node-header-atau-ancestor-terhapus | Delete Group: Fallback Seleksi ke All Groups Setelah Node Header atau Ancestor Terhapus | FE+BE | 24 | TC-AC-SG-144, TC-AC-SG-145 |
| TC-AC-SG-E2E-111-bulk-delete-guard-tiga-campur-lolos-dan-skip-member | Bulk Delete: Guard Entitas Tiga Campur, Dua dari Tiga Group Lolos dan Ketiganya Lolos karena Satu Di-skip | FE+BE | 15 | TC-AC-SG-163, TC-AC-SG-164 |
| TC-AC-SG-E2E-112-isi-file-csv-group-nilai-sel-angka-dan-format-tanggal | Isi File CSV Group: Berkas Seluruh Baris, Nilai Sel Angka, dan Format Tanggal | FE+BE | 8 | TC-AC-SG-232 |
| TC-AC-SG-E2E-114-modal-changelog-download-csv-dan-xlsx | Modal Changelog: Download CSV dan XLSX dengan Filename Changelog-Group | FE+BE | 16 | TC-AC-SG-269 |
| TC-AC-SG-E2E-115-popup-users-filter-temporary-until-dan-custom-field | Popup Users: Filter Temporary Until, Custom Field Aktif, dan Kolom Curated Custom Field | FE+BE | 21 | TC-AC-SG-292, TC-AC-SG-293 |
| TC-AC-SG-E2E-116-absence-log-pelepasan-group-role-dan-tanpa-notifikasi-in-app | Absence Log Pelepasan Group Role akibat Delete dan Tanpa Notifikasi In-App | FE+BE | 42 | TC-AC-SG-335, TC-AC-SG-336, TC-AC-SG-337 |
| TC-AC-SG-E2E-117-sinkron-lintas-modul-form-create-entitas-wallet-dan-format-tanggal | Sinkron Lintas Modul: Form Create Distributor, Partner, Client, Wallet, dan Format Tanggal General Settings | FE+BE | 25 | TC-AC-SG-342, TC-AC-SG-351, TC-AC-SG-352 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Seluruh 404 TC punya antarmuka dan masuk spec. TC defense-in-depth dengan Expected respons API tetap masuk spec FE+BE dengan butir Notes `K-1`.

| TC ID | Skenario | Alasan Dikecualikan dari E2E |
|---|---|---|
| — | — | — |

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-SG-01 | E2E | TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar | FE+BE |
| TC-AC-SG-02 | E2E | TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar | FE+BE |
| TC-AC-SG-03 | E2E | TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar | FE+BE |
| TC-AC-SG-04 | E2E | TC-AC-SG-E2E-001-screening-halaman-group-header-kolom-dan-toolbar | FE+BE |
| TC-AC-SG-05 | E2E | TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | FE+BE |
| TC-AC-SG-06 | E2E | TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | FE+BE |
| TC-AC-SG-07 | E2E | TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | FE+BE |
| TC-AC-SG-08 | E2E | TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | FE+BE |
| TC-AC-SG-09 | E2E | TC-AC-SG-E2E-002-screening-breadcrumb-klik-baris-hover-path-modified-by-dan-overlay-row-action | FE+BE |
| TC-AC-SG-10 | E2E | TC-AC-SG-E2E-003-loading-state-dan-empty-state-node-tanpa-subgroup | FE+BE (intercept) |
| TC-AC-SG-11 | E2E | TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download | FE+BE (intercept) |
| TC-AC-SG-12 | E2E | TC-AC-SG-E2E-004-empty-state-entitas-tanpa-group-dan-entitas-satu-group | FE+BE |
| TC-AC-SG-13 | E2E | TC-AC-SG-E2E-003-loading-state-dan-empty-state-node-tanpa-subgroup | FE+BE (intercept) |
| TC-AC-SG-14 | E2E | TC-AC-SG-E2E-004-empty-state-entitas-tanpa-group-dan-entitas-satu-group | FE+BE |
| TC-AC-SG-15 | E2E | TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | FE+BE |
| TC-AC-SG-16 | E2E | TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | FE+BE |
| TC-AC-SG-17 | E2E | TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | FE+BE |
| TC-AC-SG-18 | E2E | TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | FE+BE |
| TC-AC-SG-19 | E2E | TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | FE+BE |
| TC-AC-SG-20 | E2E | TC-AC-SG-E2E-005-sidebar-group-tree-screening-default-expand-collapse-dan-search | FE+BE |
| TC-AC-SG-21 | E2E | TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight | FE+BE |
| TC-AC-SG-22 | E2E | TC-AC-SG-E2E-007-sidebar-group-tree-toggle-persistensi-dan-collapse-otomatis | FE+BE |
| TC-AC-SG-23 | E2E | TC-AC-SG-E2E-007-sidebar-group-tree-toggle-persistensi-dan-collapse-otomatis | FE+BE |
| TC-AC-SG-24 | E2E | TC-AC-SG-E2E-007-sidebar-group-tree-toggle-persistensi-dan-collapse-otomatis | FE+BE |
| TC-AC-SG-25 | E2E | TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight | FE+BE |
| TC-AC-SG-26 | E2E | TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight | FE+BE |
| TC-AC-SG-27 | E2E | TC-AC-SG-E2E-006-sidebar-group-tree-hapus-search-label-panjang-elipsis-dan-highlight | FE+BE |
| TC-AC-SG-28 | E2E | TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | FE+BE |
| TC-AC-SG-29 | E2E | TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | FE+BE |
| TC-AC-SG-30 | E2E | TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | FE+BE |
| TC-AC-SG-31 | E2E | TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | FE+BE |
| TC-AC-SG-32 | E2E | TC-AC-SG-E2E-106-total-user-agregat-all-groups-user-distinct-bukan-penjumlahan-per-node | FE+BE |
| TC-AC-SG-33 | E2E | TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header | FE+BE |
| TC-AC-SG-34 | E2E | TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header | FE+BE |
| TC-AC-SG-35 | E2E | TC-AC-SG-E2E-008-semantik-pilih-node-descendant-all-groups-exclusive-toggle-off-dan-reset-pagination | FE+BE |
| TC-AC-SG-36 | E2E | TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header | FE+BE |
| TC-AC-SG-37 | E2E | TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | FE+BE |
| TC-AC-SG-38 | E2E | TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | FE+BE |
| TC-AC-SG-39 | E2E | TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | FE+BE |
| TC-AC-SG-40 | E2E | TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | FE+BE |
| TC-AC-SG-41 | E2E | TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived | FE+BE |
| TC-AC-SG-42 | E2E | TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived | FE+BE |
| TC-AC-SG-43 | E2E | TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived | FE+BE |
| TC-AC-SG-44 | E2E | TC-AC-SG-E2E-011-total-member-node-langsung-tidak-rekursif-nol-dan-archived | FE+BE |
| TC-AC-SG-45 | E2E | TC-AC-SG-E2E-010-total-user-node-union-dedup-tanpa-pewarisan-dan-tanpa-filter-status | FE+BE |
| TC-AC-SG-46 | E2E | TC-AC-SG-E2E-012-guided-tooltip-kunjungan-pertama-navigasi-dan-tombol-bantuan | FE+BE |
| TC-AC-SG-47 | E2E | TC-AC-SG-E2E-012-guided-tooltip-kunjungan-pertama-navigasi-dan-tombol-bantuan | FE+BE |
| TC-AC-SG-48 | E2E | TC-AC-SG-E2E-012-guided-tooltip-kunjungan-pertama-navigasi-dan-tombol-bantuan | FE+BE |
| TC-AC-SG-49 | E2E | TC-AC-SG-E2E-013-guided-tooltip-tidak-muncul-lagi-resize-dan-keyboard | FE+BE |
| TC-AC-SG-50 | E2E | TC-AC-SG-E2E-013-guided-tooltip-tidak-muncul-lagi-resize-dan-keyboard | FE+BE |
| TC-AC-SG-51 | E2E | TC-AC-SG-E2E-013-guided-tooltip-tidak-muncul-lagi-resize-dan-keyboard | FE+BE |
| TC-AC-SG-52 | E2E | TC-AC-SG-E2E-014-mobile-android-card-list-bottom-sheet-tree-dan-toolbar | FE+BE |
| TC-AC-SG-53 | E2E | TC-AC-SG-E2E-014-mobile-android-card-list-bottom-sheet-tree-dan-toolbar | FE+BE |
| TC-AC-SG-54 | E2E | TC-AC-SG-E2E-014-mobile-android-card-list-bottom-sheet-tree-dan-toolbar | FE+BE |
| TC-AC-SG-55 | E2E | TC-AC-SG-E2E-107-mobile-android-akses-changelog-dan-popup-create-edit-delete-bottom-sheet | FE+BE |
| TC-AC-SG-56 | E2E | TC-AC-SG-E2E-107-mobile-android-akses-changelog-dan-popup-create-edit-delete-bottom-sheet | FE+BE |
| TC-AC-SG-57 | E2E | TC-AC-SG-E2E-016-role-matrix-entity-gate-distributor-partner-dan-client | FE+BE |
| TC-AC-SG-58 | E2E | TC-AC-SG-E2E-016-role-matrix-entity-gate-distributor-partner-dan-client | FE+BE |
| TC-AC-SG-59 | E2E | TC-AC-SG-E2E-016-role-matrix-entity-gate-distributor-partner-dan-client | FE+BE |
| TC-AC-SG-60 | E2E | TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | FE+BE |
| TC-AC-SG-61 | E2E | TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | FE+BE |
| TC-AC-SG-62 | E2E | TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | FE+BE |
| TC-AC-SG-63 | E2E | TC-AC-SG-E2E-018-role-matrix-group-manager-dan-role-tanpa-manage-group-tanpa-akses-menu | FE+BE |
| TC-AC-SG-64 | E2E | TC-AC-SG-E2E-018-role-matrix-group-manager-dan-role-tanpa-manage-group-tanpa-akses-menu | FE+BE |
| TC-AC-SG-65 | E2E | TC-AC-SG-E2E-019-role-matrix-visibilitas-kontrol-manage-group-cud-dan-create-saja | FE+BE |
| TC-AC-SG-66 | E2E | TC-AC-SG-E2E-019-role-matrix-visibilitas-kontrol-manage-group-cud-dan-create-saja | FE+BE |
| TC-AC-SG-67 | E2E | TC-AC-SG-E2E-108-role-matrix-visibilitas-kontrol-manage-group-update-saja | FE+BE |
| TC-AC-SG-68 | E2E | TC-AC-SG-E2E-020-role-matrix-visibilitas-kontrol-manage-group-delete-saja-create-update-dan-kolom-checkbox-tanpa-delete | FE+BE |
| TC-AC-SG-69 | E2E | TC-AC-SG-E2E-020-role-matrix-visibilitas-kontrol-manage-group-delete-saja-create-update-dan-kolom-checkbox-tanpa-delete | FE+BE |
| TC-AC-SG-70 | E2E | TC-AC-SG-E2E-109-role-matrix-visibilitas-kontrol-manage-group-create-delete | FE+BE |
| TC-AC-SG-71 | E2E | TC-AC-SG-E2E-021-role-matrix-visibilitas-kontrol-manage-group-update-delete-dan-tanpa-capability-mutasi | FE+BE |
| TC-AC-SG-72 | E2E | TC-AC-SG-E2E-021-role-matrix-visibilitas-kontrol-manage-group-update-delete-dan-tanpa-capability-mutasi | FE+BE |
| TC-AC-SG-73 | E2E | TC-AC-SG-E2E-022-manage-group-create-add-subgroup-level-satu-dan-dalam-tanpa-penugasan-otomatis-ke-pembuat | FE+BE |
| TC-AC-SG-74 | E2E | TC-AC-SG-E2E-023-manage-group-update-rename-level-satu-dan-dalam-tree-entity-wide | FE+BE |
| TC-AC-SG-75 | E2E | TC-AC-SG-E2E-024-manage-group-delete-menghapus-group-lewat-checkbox-bulk-dan-delete | FE+BE |
| TC-AC-SG-76 | E2E | TC-AC-SG-E2E-023-manage-group-update-rename-level-satu-dan-dalam-tree-entity-wide | FE+BE |
| TC-AC-SG-77 | E2E | TC-AC-SG-E2E-017-role-matrix-total-control-default-user-dan-read-only | FE+BE |
| TC-AC-SG-78 | E2E | TC-AC-SG-E2E-025-popup-create-screening-new-group-dan-add-subgroup-beserta-konteks-under | FE+BE |
| TC-AC-SG-79 | E2E | TC-AC-SG-E2E-025-popup-create-screening-new-group-dan-add-subgroup-beserta-konteks-under | FE+BE |
| TC-AC-SG-80 | E2E | TC-AC-SG-E2E-025-popup-create-screening-new-group-dan-add-subgroup-beserta-konteks-under | FE+BE |
| TC-AC-SG-81 | E2E | TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-82 | E2E | TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-83 | E2E | TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | FE+BE |
| TC-AC-SG-84 | E2E | TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-85 | E2E | TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | FE+BE |
| TC-AC-SG-86 | E2E | TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | FE+BE |
| TC-AC-SG-87 | E2E | TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-88 | E2E | TC-AC-SG-E2E-026-popup-create-validasi-group-name-kosong-120-karakter-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-89 | E2E | TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | FE+BE |
| TC-AC-SG-90 | E2E | TC-AC-SG-E2E-027-create-group-stay-on-form-trim-dan-nama-sama-pada-parent-atau-entitas-berbeda | FE+BE |
| TC-AC-SG-91 | E2E | TC-AC-SG-E2E-028-create-subgroup-parent-pemilik-aksi-elipsis-sidebar-dan-level-satu-saat-node-lain-terpilih | FE+BE |
| TC-AC-SG-92 | E2E | TC-AC-SG-E2E-028-create-subgroup-parent-pemilik-aksi-elipsis-sidebar-dan-level-satu-saat-node-lain-terpilih | FE+BE |
| TC-AC-SG-93 | E2E | TC-AC-SG-E2E-028-create-subgroup-parent-pemilik-aksi-elipsis-sidebar-dan-level-satu-saat-node-lain-terpilih | FE+BE |
| TC-AC-SG-94 | E2E | TC-AC-SG-E2E-029-create-group-scope-tabel-node-terpilih-urutan-alfabetis-sidebar-dan-total-user-member-node-baru | FE+BE |
| TC-AC-SG-95 | E2E | TC-AC-SG-E2E-029-create-group-scope-tabel-node-terpilih-urutan-alfabetis-sidebar-dan-total-user-member-node-baru | FE+BE |
| TC-AC-SG-96 | E2E | TC-AC-SG-E2E-029-create-group-scope-tabel-node-terpilih-urutan-alfabetis-sidebar-dan-total-user-member-node-baru | FE+BE |
| TC-AC-SG-97 | E2E | TC-AC-SG-E2E-022-manage-group-create-add-subgroup-level-satu-dan-dalam-tanpa-penugasan-otomatis-ke-pembuat | FE+BE |
| TC-AC-SG-98 | E2E | TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop | FE+BE |
| TC-AC-SG-99 | E2E | TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop | FE+BE |
| TC-AC-SG-100 | E2E | TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop | FE+BE |
| TC-AC-SG-101 | E2E | TC-AC-SG-E2E-031-popup-create-unsaved-changes-lewat-close-esc-popup-kosong-dan-backdrop | FE+BE |
| TC-AC-SG-102 | E2E | TC-AC-SG-E2E-032-popup-create-terisi-reload-dan-navigasi-in-app | FE+BE |
| TC-AC-SG-103 | E2E | TC-AC-SG-E2E-032-popup-create-terisi-reload-dan-navigasi-in-app | FE+BE |
| TC-AC-SG-104 | E2E | TC-AC-SG-E2E-030-create-group-saving-state-dan-klik-submit-ganda | FE+BE |
| TC-AC-SG-105 | E2E | TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download | FE+BE (intercept) |
| TC-AC-SG-106 | E2E | TC-AC-SG-E2E-030-create-group-saving-state-dan-klik-submit-ganda | FE+BE |
| TC-AC-SG-107 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-108 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-109 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-110 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-111 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-112 | E2E | TC-AC-SG-E2E-033-create-subgroup-dan-hierarchy-depth-limit | FE+BE |
| TC-AC-SG-113 | E2E | TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header | FE+BE |
| TC-AC-SG-114 | E2E | TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header | FE+BE |
| TC-AC-SG-115 | E2E | TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header | FE+BE |
| TC-AC-SG-116 | E2E | TC-AC-SG-E2E-034-popup-edit-screening-dan-rename-dari-row-action-dan-elipsis-sidebar-update-group-context-header | FE+BE |
| TC-AC-SG-117 | E2E | TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group | FE+BE |
| TC-AC-SG-118 | E2E | TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-119 | E2E | TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-120 | E2E | TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-121 | E2E | TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group | FE+BE |
| TC-AC-SG-122 | E2E | TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-123 | E2E | TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group | FE+BE |
| TC-AC-SG-124 | E2E | TC-AC-SG-E2E-035-edit-group-validasi-kosong-lebih-dari-120-sibling-duplikat-all-groups-dan-clear-field | FE+BE |
| TC-AC-SG-125 | E2E | TC-AC-SG-E2E-090-absence-log-edit-tanpa-perubahan | FE+BE |
| TC-AC-SG-126 | E2E | TC-AC-SG-E2E-037-edit-group-unsaved-changes-bersyarat-tanpa-pindah-parent-dan-referensi-user-entitas-tidak-putus | FE+BE |
| TC-AC-SG-127 | E2E | TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download | FE+BE (intercept) |
| TC-AC-SG-128 | E2E | TC-AC-SG-E2E-036-edit-group-huruf-besar-kecil-nama-sama-pada-parent-berbeda-trim-dan-rename-default-group | FE+BE |
| TC-AC-SG-129 | E2E | TC-AC-SG-E2E-037-edit-group-unsaved-changes-bersyarat-tanpa-pindah-parent-dan-referensi-user-entitas-tidak-putus | FE+BE |
| TC-AC-SG-130 | E2E | TC-AC-SG-E2E-037-edit-group-unsaved-changes-bersyarat-tanpa-pindah-parent-dan-referensi-user-entitas-tidak-putus | FE+BE |
| TC-AC-SG-131 | E2E | TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | FE+BE |
| TC-AC-SG-132 | E2E | TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | FE+BE |
| TC-AC-SG-133 | E2E | TC-AC-SG-E2E-041-delete-group-konfirmasi-hapus-subtree-pelepasan-group-role-manager-dan-klik-ganda | FE+BE |
| TC-AC-SG-134 | E2E | TC-AC-SG-E2E-091-absence-log-delete-cancel-skip-bulk-dan-diblok-dialog | FE+BE |
| TC-AC-SG-135 | E2E | TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | FE+BE |
| TC-AC-SG-136 | E2E | TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | FE+BE |
| TC-AC-SG-137 | E2E | TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | FE+BE |
| TC-AC-SG-138 | E2E | TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | FE+BE |
| TC-AC-SG-139 | E2E | TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | FE+BE |
| TC-AC-SG-140 | E2E | TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group | FE+BE |
| TC-AC-SG-141 | E2E | TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group | FE+BE |
| TC-AC-SG-142 | E2E | TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group | FE+BE |
| TC-AC-SG-143 | E2E | TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group | FE+BE |
| TC-AC-SG-144 | E2E | TC-AC-SG-E2E-110-delete-group-fallback-seleksi-ke-all-groups-setelah-node-header-atau-ancestor-terhapus | FE+BE |
| TC-AC-SG-145 | E2E | TC-AC-SG-E2E-110-delete-group-fallback-seleksi-ke-all-groups-setelah-node-header-atau-ancestor-terhapus | FE+BE |
| TC-AC-SG-146 | E2E | TC-AC-SG-E2E-041-delete-group-konfirmasi-hapus-subtree-pelepasan-group-role-manager-dan-klik-ganda | FE+BE |
| TC-AC-SG-147 | E2E | TC-AC-SG-E2E-105-resilience-distributor-gagal-server-delete-bulk-delete-dan-download-changelog | FE+BE (intercept) |
| TC-AC-SG-148 | E2E | TC-AC-SG-E2E-041-delete-group-konfirmasi-hapus-subtree-pelepasan-group-role-manager-dan-klik-ganda | FE+BE |
| TC-AC-SG-149 | E2E | TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | FE+BE |
| TC-AC-SG-150 | E2E | TC-AC-SG-E2E-038-delete-group-dialog-warning-d04-cancel-backdrop-tooltip-path-elipsis-sidebar | FE+BE |
| TC-AC-SG-151 | E2E | TC-AC-SG-E2E-042-bulk-delete-bulk-actions-bar-select-all-unselect-all-dan-checkbox-header | FE+BE |
| TC-AC-SG-152 | E2E | TC-AC-SG-E2E-042-bulk-delete-bulk-actions-bar-select-all-unselect-all-dan-checkbox-header | FE+BE |
| TC-AC-SG-153 | E2E | TC-AC-SG-E2E-042-bulk-delete-bulk-actions-bar-select-all-unselect-all-dan-checkbox-header | FE+BE |
| TC-AC-SG-154 | E2E | TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel | FE+BE |
| TC-AC-SG-155 | E2E | TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel | FE+BE |
| TC-AC-SG-156 | E2E | TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel | FE+BE |
| TC-AC-SG-157 | E2E | TC-AC-SG-E2E-044-bulk-delete-homogen-campuran-dan-seluruh-baris-punya-member | FE+BE |
| TC-AC-SG-158 | E2E | TC-AC-SG-E2E-044-bulk-delete-homogen-campuran-dan-seluruh-baris-punya-member | FE+BE |
| TC-AC-SG-159 | E2E | TC-AC-SG-E2E-044-bulk-delete-homogen-campuran-dan-seluruh-baris-punya-member | FE+BE |
| TC-AC-SG-160 | E2E | TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit | FE+BE |
| TC-AC-SG-161 | E2E | TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit | FE+BE |
| TC-AC-SG-162 | E2E | TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08 | FE+BE |
| TC-AC-SG-163 | E2E | TC-AC-SG-E2E-111-bulk-delete-guard-tiga-campur-lolos-dan-skip-member | FE+BE |
| TC-AC-SG-164 | E2E | TC-AC-SG-E2E-111-bulk-delete-guard-tiga-campur-lolos-dan-skip-member | FE+BE |
| TC-AC-SG-165 | E2E | TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08 | FE+BE |
| TC-AC-SG-166 | E2E | TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08 | FE+BE |
| TC-AC-SG-167 | E2E | TC-AC-SG-E2E-043-bulk-delete-seleksi-lintas-halaman-search-reset-oleh-node-batas-node-terpilih-dan-cancel | FE+BE |
| TC-AC-SG-168 | E2E | TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit | FE+BE |
| TC-AC-SG-169 | E2E | TC-AC-SG-E2E-047-bulk-delete-selection-limit-100-seleksi-manual-dan-select-all | FE+BE |
| TC-AC-SG-170 | E2E | TC-AC-SG-E2E-047-bulk-delete-selection-limit-100-seleksi-manual-dan-select-all | FE+BE |
| TC-AC-SG-171 | E2E | TC-AC-SG-E2E-105-resilience-distributor-gagal-server-delete-bulk-delete-dan-download-changelog | FE+BE (intercept) |
| TC-AC-SG-172 | E2E | TC-AC-SG-E2E-020-role-matrix-visibilitas-kontrol-manage-group-delete-saja-create-update-dan-kolom-checkbox-tanpa-delete | FE+BE |
| TC-AC-SG-173 | E2E | TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08 | FE+BE |
| TC-AC-SG-174 | E2E | TC-AC-SG-E2E-048-search-tabel-utama-interaksi-kolom-group-dan-total-user | FE+BE |
| TC-AC-SG-175 | E2E | TC-AC-SG-E2E-048-search-tabel-utama-interaksi-kolom-group-dan-total-user | FE+BE |
| TC-AC-SG-176 | E2E | TC-AC-SG-E2E-048-search-tabel-utama-interaksi-kolom-group-dan-total-user | FE+BE |
| TC-AC-SG-177 | E2E | TC-AC-SG-E2E-049-search-tabel-utama-kolom-total-member-modified-by-dan-last-updated | FE+BE |
| TC-AC-SG-178 | E2E | TC-AC-SG-E2E-049-search-tabel-utama-kolom-total-member-modified-by-dan-last-updated | FE+BE |
| TC-AC-SG-179 | E2E | TC-AC-SG-E2E-049-search-tabel-utama-kolom-total-member-modified-by-dan-last-updated | FE+BE |
| TC-AC-SG-180 | E2E | TC-AC-SG-E2E-050-search-tabel-utama-kolom-di-hide-trim-dan-lokal-terhadap-node-terpilih | FE+BE |
| TC-AC-SG-181 | E2E | TC-AC-SG-E2E-050-search-tabel-utama-kolom-di-hide-trim-dan-lokal-terhadap-node-terpilih | FE+BE |
| TC-AC-SG-182 | E2E | TC-AC-SG-E2E-050-search-tabel-utama-kolom-di-hide-trim-dan-lokal-terhadap-node-terpilih | FE+BE |
| TC-AC-SG-183 | E2E | TC-AC-SG-E2E-097-defense-in-depth-ui-payload-script-sebagai-teks-literal-pada-search-dan-nama-group | FE+BE |
| TC-AC-SG-184 | E2E | TC-AC-SG-E2E-051-filter-tabel-utama-screening-panel-dan-total-user | FE+BE |
| TC-AC-SG-185 | E2E | TC-AC-SG-E2E-051-filter-tabel-utama-screening-panel-dan-total-user | FE+BE |
| TC-AC-SG-186 | E2E | TC-AC-SG-E2E-051-filter-tabel-utama-screening-panel-dan-total-user | FE+BE |
| TC-AC-SG-187 | E2E | TC-AC-SG-E2E-052-filter-tabel-utama-total-member-dan-opsi-dropdown-modified-by | FE+BE |
| TC-AC-SG-188 | E2E | TC-AC-SG-E2E-052-filter-tabel-utama-total-member-dan-opsi-dropdown-modified-by | FE+BE |
| TC-AC-SG-189 | E2E | TC-AC-SG-E2E-052-filter-tabel-utama-total-member-dan-opsi-dropdown-modified-by | FE+BE |
| TC-AC-SG-190 | E2E | TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated | FE+BE |
| TC-AC-SG-191 | E2E | TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated | FE+BE |
| TC-AC-SG-192 | E2E | TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated | FE+BE |
| TC-AC-SG-193 | E2E | TC-AC-SG-E2E-053-filter-tabel-utama-modified-by-search-dropdown-dan-last-updated | FE+BE |
| TC-AC-SG-194 | E2E | TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom | FE+BE |
| TC-AC-SG-195 | E2E | TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom | FE+BE |
| TC-AC-SG-196 | E2E | TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom | FE+BE |
| TC-AC-SG-197 | E2E | TC-AC-SG-E2E-054-filter-tabel-utama-logika-and-clear-field-tutup-tanpa-apply-dan-independen-kolom | FE+BE |
| TC-AC-SG-198 | E2E | TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | FE+BE |
| TC-AC-SG-199 | E2E | TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | FE+BE |
| TC-AC-SG-200 | E2E | TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | FE+BE |
| TC-AC-SG-201 | E2E | TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | FE+BE |
| TC-AC-SG-202 | E2E | TC-AC-SG-E2E-056-sort-tabel-utama-kolom-group-total-user-dan-total-member | FE+BE |
| TC-AC-SG-203 | E2E | TC-AC-SG-E2E-056-sort-tabel-utama-kolom-group-total-user-dan-total-member | FE+BE |
| TC-AC-SG-204 | E2E | TC-AC-SG-E2E-056-sort-tabel-utama-kolom-group-total-user-dan-total-member | FE+BE |
| TC-AC-SG-205 | E2E | TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | FE+BE |
| TC-AC-SG-206 | E2E | TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | FE+BE |
| TC-AC-SG-207 | E2E | TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | FE+BE |
| TC-AC-SG-208 | E2E | TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | FE+BE |
| TC-AC-SG-209 | E2E | TC-AC-SG-E2E-057-sort-tabel-utama-modified-by-last-updated-pindah-kolom-dan-independen-search-filter | FE+BE |
| TC-AC-SG-210 | E2E | TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder | FE+BE |
| TC-AC-SG-211 | E2E | TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder | FE+BE |
| TC-AC-SG-212 | E2E | TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder | FE+BE |
| TC-AC-SG-213 | E2E | TC-AC-SG-E2E-058-overlay-column-visibility-hide-unhide-kolom-terakhir-dan-reorder | FE+BE |
| TC-AC-SG-214 | E2E | TC-AC-SG-E2E-059-modal-setup-column-tabel-utama-screening-preview-save-dan-tutup-tanpa-save | FE+BE |
| TC-AC-SG-215 | E2E | TC-AC-SG-E2E-059-modal-setup-column-tabel-utama-screening-preview-save-dan-tutup-tanpa-save | FE+BE |
| TC-AC-SG-216 | E2E | TC-AC-SG-E2E-059-modal-setup-column-tabel-utama-screening-preview-save-dan-tutup-tanpa-save | FE+BE |
| TC-AC-SG-217 | E2E | TC-AC-SG-E2E-060-setup-column-tabel-utama-reset-to-default-reorder-pin-dan-unpin | FE+BE |
| TC-AC-SG-218 | E2E | TC-AC-SG-E2E-060-setup-column-tabel-utama-reset-to-default-reorder-pin-dan-unpin | FE+BE |
| TC-AC-SG-219 | E2E | TC-AC-SG-E2E-060-setup-column-tabel-utama-reset-to-default-reorder-pin-dan-unpin | FE+BE |
| TC-AC-SG-220 | E2E | TC-AC-SG-E2E-061-setup-column-tabel-utama-pin-ke-4-cache-terpisah-dari-popup-dan-max-visible-columns | FE+BE |
| TC-AC-SG-221 | E2E | TC-AC-SG-E2E-061-setup-column-tabel-utama-pin-ke-4-cache-terpisah-dari-popup-dan-max-visible-columns | FE+BE |
| TC-AC-SG-222 | E2E | TC-AC-SG-E2E-061-setup-column-tabel-utama-pin-ke-4-cache-terpisah-dari-popup-dan-max-visible-columns | FE+BE |
| TC-AC-SG-223 | E2E | TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous | FE+BE |
| TC-AC-SG-224 | E2E | TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous | FE+BE |
| TC-AC-SG-225 | E2E | TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous | FE+BE |
| TC-AC-SG-226 | E2E | TC-AC-SG-E2E-062-pagination-tabel-utama-default-page-size-input-halaman-dan-next-previous | FE+BE |
| TC-AC-SG-227 | E2E | TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu | FE+BE |
| TC-AC-SG-228 | E2E | TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu | FE+BE |
| TC-AC-SG-229 | E2E | TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu | FE+BE |
| TC-AC-SG-230 | E2E | TC-AC-SG-E2E-063-persistensi-state-list-f5-back-browser-search-sidebar-dan-klik-ulang-menu | FE+BE |
| TC-AC-SG-231 | E2E | TC-AC-SG-E2E-064-download-tabel-utama-overlay-csv-xlsx-dan-hasil-search-filter-aktif | FE+BE |
| TC-AC-SG-232 | E2E | TC-AC-SG-E2E-112-isi-file-csv-group-nilai-sel-angka-dan-format-tanggal | FE+BE |
| TC-AC-SG-233 | E2E | TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog | FE+BE |
| TC-AC-SG-234 | E2E | TC-AC-SG-E2E-064-download-tabel-utama-overlay-csv-xlsx-dan-hasil-search-filter-aktif | FE+BE |
| TC-AC-SG-235 | E2E | TC-AC-SG-E2E-065-download-tabel-utama-kolom-di-hide-node-terpilih-dan-hasil-kosong | FE+BE |
| TC-AC-SG-236 | E2E | TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog | FE+BE |
| TC-AC-SG-237 | E2E | TC-AC-SG-E2E-065-download-tabel-utama-kolom-di-hide-node-terpilih-dan-hasil-kosong | FE+BE |
| TC-AC-SG-238 | E2E | TC-AC-SG-E2E-065-download-tabel-utama-kolom-di-hide-node-terpilih-dan-hasil-kosong | FE+BE |
| TC-AC-SG-239 | E2E | TC-AC-SG-E2E-104-resilience-principal-error-load-gagal-server-create-edit-dan-download | FE+BE (intercept) |
| TC-AC-SG-240 | E2E | TC-AC-SG-E2E-055-search-dan-filter-beririsan-empty-state-kombinasi-filter-lokal-node-dan-reset-halaman | FE+BE |
| TC-AC-SG-241 | E2E | TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom | FE+BE |
| TC-AC-SG-242 | E2E | TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom | FE+BE |
| TC-AC-SG-243 | E2E | TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom | FE+BE |
| TC-AC-SG-244 | E2E | TC-AC-SG-E2E-067-modal-changelog-screening-empty-state-dan-tampilan-data-kolom | FE+BE |
| TC-AC-SG-245 | E2E | TC-AC-SG-E2E-068-modal-changelog-search-kolom-action-group-name-dan-field | FE+BE |
| TC-AC-SG-246 | E2E | TC-AC-SG-E2E-068-modal-changelog-search-kolom-action-group-name-dan-field | FE+BE |
| TC-AC-SG-247 | E2E | TC-AC-SG-E2E-068-modal-changelog-search-kolom-action-group-name-dan-field | FE+BE |
| TC-AC-SG-248 | E2E | TC-AC-SG-E2E-069-modal-changelog-search-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-AC-SG-249 | E2E | TC-AC-SG-E2E-069-modal-changelog-search-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-AC-SG-250 | E2E | TC-AC-SG-E2E-069-modal-changelog-search-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-AC-SG-251 | E2E | TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name | FE+BE |
| TC-AC-SG-252 | E2E | TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name | FE+BE |
| TC-AC-SG-253 | E2E | TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name | FE+BE |
| TC-AC-SG-254 | E2E | TC-AC-SG-E2E-070-modal-changelog-search-date-panel-filter-dan-opsi-action-group-name | FE+BE |
| TC-AC-SG-255 | E2E | TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | FE+BE |
| TC-AC-SG-256 | E2E | TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | FE+BE |
| TC-AC-SG-257 | E2E | TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | FE+BE |
| TC-AC-SG-258 | E2E | TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | FE+BE |
| TC-AC-SG-259 | E2E | TC-AC-SG-E2E-071-modal-changelog-filter-group-name-modified-by-date-kombinasi-and-dan-independensi-kontrol | FE+BE |
| TC-AC-SG-260 | E2E | TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-AC-SG-261 | E2E | TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-AC-SG-262 | E2E | TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-AC-SG-263 | E2E | TC-AC-SG-E2E-072-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-AC-SG-264 | E2E | TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination | FE+BE |
| TC-AC-SG-265 | E2E | TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination | FE+BE |
| TC-AC-SG-266 | E2E | TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination | FE+BE |
| TC-AC-SG-267 | E2E | TC-AC-SG-E2E-074-modal-changelog-setup-column-tutup-modal-dan-snapshot-immutable | FE+BE |
| TC-AC-SG-268 | E2E | TC-AC-SG-E2E-073-modal-changelog-sort-kolom-old-value-new-value-modified-by-dan-pagination | FE+BE |
| TC-AC-SG-269 | E2E | TC-AC-SG-E2E-114-modal-changelog-download-csv-dan-xlsx | FE+BE |
| TC-AC-SG-270 | E2E | TC-AC-SG-E2E-105-resilience-distributor-gagal-server-delete-bulk-delete-dan-download-changelog | FE+BE (intercept) |
| TC-AC-SG-271 | E2E | TC-AC-SG-E2E-074-modal-changelog-setup-column-tutup-modal-dan-snapshot-immutable | FE+BE |
| TC-AC-SG-272 | E2E | TC-AC-SG-E2E-074-modal-changelog-setup-column-tutup-modal-dan-snapshot-immutable | FE+BE |
| TC-AC-SG-273 | E2E | TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | FE+BE |
| TC-AC-SG-274 | E2E | TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | FE+BE |
| TC-AC-SG-275 | E2E | TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | FE+BE |
| TC-AC-SG-276 | E2E | TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | FE+BE |
| TC-AC-SG-277 | E2E | TC-AC-SG-E2E-075-popup-total-user-detail-screening-identitas-path-group-role-kolom-name-dan-penutupan | FE+BE |
| TC-AC-SG-278 | E2E | TC-AC-SG-E2E-076-popup-users-search-kolom-name-email-dan-position | FE+BE |
| TC-AC-SG-279 | E2E | TC-AC-SG-E2E-076-popup-users-search-kolom-name-email-dan-position | FE+BE |
| TC-AC-SG-280 | E2E | TC-AC-SG-E2E-076-popup-users-search-kolom-name-email-dan-position | FE+BE |
| TC-AC-SG-281 | E2E | TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide | FE+BE |
| TC-AC-SG-282 | E2E | TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide | FE+BE |
| TC-AC-SG-283 | E2E | TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide | FE+BE |
| TC-AC-SG-284 | E2E | TC-AC-SG-E2E-077-popup-users-search-kolom-division-group-role-curated-dan-kolom-di-hide | FE+BE |
| TC-AC-SG-285 | E2E | TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | FE+BE |
| TC-AC-SG-286 | E2E | TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | FE+BE |
| TC-AC-SG-287 | E2E | TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | FE+BE |
| TC-AC-SG-288 | E2E | TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | FE+BE |
| TC-AC-SG-289 | E2E | TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang | FE+BE |
| TC-AC-SG-290 | E2E | TC-AC-SG-E2E-079-popup-users-filter-position-division-activation-status-dan-temporary-user | FE+BE |
| TC-AC-SG-291 | E2E | TC-AC-SG-E2E-079-popup-users-filter-position-division-activation-status-dan-temporary-user | FE+BE |
| TC-AC-SG-292 | E2E | TC-AC-SG-E2E-115-popup-users-filter-temporary-until-dan-custom-field | FE+BE |
| TC-AC-SG-293 | E2E | TC-AC-SG-E2E-115-popup-users-filter-temporary-until-dan-custom-field | FE+BE |
| TC-AC-SG-294 | E2E | TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | FE+BE |
| TC-AC-SG-295 | E2E | TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | FE+BE |
| TC-AC-SG-296 | E2E | TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | FE+BE |
| TC-AC-SG-297 | E2E | TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | FE+BE |
| TC-AC-SG-298 | E2E | TC-AC-SG-E2E-080-popup-users-clear-field-filter-tanpa-hasil-dan-sort-name-email-position | FE+BE |
| TC-AC-SG-299 | E2E | TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | FE+BE |
| TC-AC-SG-300 | E2E | TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | FE+BE |
| TC-AC-SG-301 | E2E | TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | FE+BE |
| TC-AC-SG-302 | E2E | TC-AC-SG-E2E-082-popup-users-setup-column-cache-terpisah-dan-max-visible-columns | FE+BE |
| TC-AC-SG-303 | E2E | TC-AC-SG-E2E-082-popup-users-setup-column-cache-terpisah-dan-max-visible-columns | FE+BE |
| TC-AC-SG-304 | E2E | TC-AC-SG-E2E-082-popup-users-setup-column-cache-terpisah-dan-max-visible-columns | FE+BE |
| TC-AC-SG-305 | E2E | TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | FE+BE |
| TC-AC-SG-306 | E2E | TC-AC-SG-E2E-081-popup-users-sort-division-group-role-kolom-tag-nilai-kosong-dan-urutan-bawaan | FE+BE |
| TC-AC-SG-307 | E2E | TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | FE+BE |
| TC-AC-SG-308 | E2E | TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | FE+BE |
| TC-AC-SG-309 | E2E | TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | FE+BE |
| TC-AC-SG-310 | E2E | TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | FE+BE |
| TC-AC-SG-311 | E2E | TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated | FE+BE |
| TC-AC-SG-312 | E2E | TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated | FE+BE |
| TC-AC-SG-313 | E2E | TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated | FE+BE |
| TC-AC-SG-314 | E2E | TC-AC-SG-E2E-084-popup-members-search-kolom-entity-name-type-relation-status-dan-last-updated | FE+BE |
| TC-AC-SG-315 | E2E | TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | FE+BE |
| TC-AC-SG-316 | E2E | TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | FE+BE |
| TC-AC-SG-317 | E2E | TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | FE+BE |
| TC-AC-SG-318 | E2E | TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | FE+BE |
| TC-AC-SG-319 | E2E | TC-AC-SG-E2E-085-popup-members-panel-filter-type-relation-status-last-updated-dan-kombinasi | FE+BE |
| TC-AC-SG-320 | E2E | TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | FE+BE |
| TC-AC-SG-321 | E2E | TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | FE+BE |
| TC-AC-SG-322 | E2E | TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | FE+BE |
| TC-AC-SG-323 | E2E | TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | FE+BE |
| TC-AC-SG-324 | E2E | TC-AC-SG-E2E-086-popup-members-sort-keempat-kolom-dan-setup-column | FE+BE |
| TC-AC-SG-325 | E2E | TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log | FE+BE |
| TC-AC-SG-326 | E2E | TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log | FE+BE |
| TC-AC-SG-327 | E2E | TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log | FE+BE |
| TC-AC-SG-328 | E2E | TC-AC-SG-E2E-090-absence-log-edit-tanpa-perubahan | FE+BE |
| TC-AC-SG-329 | E2E | TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager | FE+BE |
| TC-AC-SG-330 | E2E | TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager | FE+BE |
| TC-AC-SG-331 | E2E | TC-AC-SG-E2E-091-absence-log-delete-cancel-skip-bulk-dan-diblok-dialog | FE+BE |
| TC-AC-SG-332 | E2E | TC-AC-SG-E2E-091-absence-log-delete-cancel-skip-bulk-dan-diblok-dialog | FE+BE |
| TC-AC-SG-333 | E2E | TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager | FE+BE |
| TC-AC-SG-334 | E2E | TC-AC-SG-E2E-088-pencatatan-delete-single-dan-bulk-satu-entri-per-node-dan-pelepasan-group-manager | FE+BE |
| TC-AC-SG-335 | E2E | TC-AC-SG-E2E-116-absence-log-pelepasan-group-role-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-AC-SG-336 | E2E | TC-AC-SG-E2E-116-absence-log-pelepasan-group-role-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-AC-SG-337 | E2E | TC-AC-SG-E2E-116-absence-log-pelepasan-group-role-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-AC-SG-338 | E2E | TC-AC-SG-E2E-089-pencatatan-seed-onboarding-dan-activity-log-entity-bound | FE+BE |
| TC-AC-SG-339 | E2E | TC-AC-SG-E2E-089-pencatatan-seed-onboarding-dan-activity-log-entity-bound | FE+BE |
| TC-AC-SG-340 | E2E | TC-AC-SG-E2E-087-pencatatan-create-dan-edit-changelog-system-log-dan-activity-log | FE+BE |
| TC-AC-SG-341 | E2E | TC-AC-SG-E2E-092-sinkron-lintas-modul-settings-user-dan-role-permission-setelah-create-dan-rename | FE+BE |
| TC-AC-SG-342 | E2E | TC-AC-SG-E2E-117-sinkron-lintas-modul-form-create-entitas-wallet-dan-format-tanggal | FE+BE |
| TC-AC-SG-343 | E2E | TC-AC-SG-E2E-092-sinkron-lintas-modul-settings-user-dan-role-permission-setelah-create-dan-rename | FE+BE |
| TC-AC-SG-344 | E2E | TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history | FE+BE |
| TC-AC-SG-345 | E2E | TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history | FE+BE |
| TC-AC-SG-346 | E2E | TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history | FE+BE |
| TC-AC-SG-347 | E2E | TC-AC-SG-E2E-094-sinkron-lintas-modul-setelah-delete-settings-user-tab-role-group-manager-list-dan-akses-history | FE+BE |
| TC-AC-SG-348 | E2E | TC-AC-SG-E2E-092-sinkron-lintas-modul-settings-user-dan-role-permission-setelah-create-dan-rename | FE+BE |
| TC-AC-SG-349 | E2E | TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor | FE+BE |
| TC-AC-SG-350 | E2E | TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor | FE+BE |
| TC-AC-SG-351 | E2E | TC-AC-SG-E2E-117-sinkron-lintas-modul-form-create-entitas-wallet-dan-format-tanggal | FE+BE |
| TC-AC-SG-352 | E2E | TC-AC-SG-E2E-117-sinkron-lintas-modul-form-create-entitas-wallet-dan-format-tanggal | FE+BE |
| TC-AC-SG-353 | E2E | TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor | FE+BE |
| TC-AC-SG-354 | E2E | TC-AC-SG-E2E-093-sinkron-lintas-modul-reassign-entitas-total-user-dan-create-distributor | FE+BE |
| TC-AC-SG-355 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-356 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-357 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-358 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-359 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-360 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-361 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-362 | E2E | TC-AC-SG-E2E-095-defense-in-depth-isolasi-entitas-dan-penolakan-403-per-role-lewat-request-langsung | FE+BE |
| TC-AC-SG-363 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-364 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-365 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-366 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-367 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-368 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-369 | E2E | TC-AC-SG-E2E-097-defense-in-depth-ui-payload-script-sebagai-teks-literal-pada-search-dan-nama-group | FE+BE |
| TC-AC-SG-370 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |
| TC-AC-SG-371 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |
| TC-AC-SG-372 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |
| TC-AC-SG-373 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |
| TC-AC-SG-374 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-375 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-376 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-377 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-378 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-379 | E2E | TC-AC-SG-E2E-099-state-tenant-expired-grace-pasca-expired-archive-dan-grace-downgrade | FE+BE |
| TC-AC-SG-380 | E2E | TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5 | FE+BE |
| TC-AC-SG-381 | E2E | TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5 | FE+BE |
| TC-AC-SG-382 | E2E | TC-AC-SG-E2E-103-konkurensi-dua-admin-delete-bersamaan-menghabiskan-group-dan-invarian-minimal-satu-group | FE+BE |
| TC-AC-SG-383 | E2E | TC-AC-SG-E2E-101-konkurensi-dua-admin-perubahan-saat-delete-menunggu-konfirmasi-dan-member-baru-saat-bulk | FE+BE |
| TC-AC-SG-384 | E2E | TC-AC-SG-E2E-101-konkurensi-dua-admin-perubahan-saat-delete-menunggu-konfirmasi-dan-member-baru-saat-bulk | FE+BE |
| TC-AC-SG-385 | E2E | TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | FE+BE |
| TC-AC-SG-386 | E2E | TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | FE+BE |
| TC-AC-SG-387 | E2E | TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | FE+BE |
| TC-AC-SG-388 | E2E | TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | FE+BE |
| TC-AC-SG-389 | E2E | TC-AC-SG-E2E-102-konkurensi-dua-admin-target-sudah-dihapus-admin-lain-add-subgroup-edit-delete-dan-bulk | FE+BE |
| TC-AC-SG-390 | E2E | TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5 | FE+BE |
| TC-AC-SG-391 | E2E | TC-AC-SG-E2E-103-konkurensi-dua-admin-delete-bersamaan-menghabiskan-group-dan-invarian-minimal-satu-group | FE+BE |
| TC-AC-SG-392 | E2E | TC-AC-SG-E2E-100-konkurensi-dua-admin-create-duplikat-edit-bersamaan-refresh-sse-dan-fallback-f5 | FE+BE |
| TC-AC-SG-393 | E2E | TC-AC-SG-E2E-015-mobile-android-long-press-selection-mode-dan-bulk-delete | FE+BE |
| TC-AC-SG-394 | E2E | TC-AC-SG-E2E-101-konkurensi-dua-admin-perubahan-saat-delete-menunggu-konfirmasi-dan-member-baru-saat-bulk | FE+BE |
| TC-AC-SG-395 | E2E | TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog | FE+BE |
| TC-AC-SG-396 | E2E | TC-AC-SG-E2E-066-isi-file-export-sel-numerik-xlsx-full-path-kolom-group-dan-snapshot-path-changelog | FE+BE |
| TC-AC-SG-397 | E2E | TC-AC-SG-E2E-083-popup-total-member-detail-screening-empty-0-kolom-type-penutupan-dan-tree-distributor | FE+BE |
| TC-AC-SG-398 | E2E | TC-AC-SG-E2E-039-delete-group-diblok-entitas-menempel-d03 | FE+BE |
| TC-AC-SG-399 | E2E | TC-AC-SG-E2E-045-bulk-delete-collapse-ke-dialog-single-nama-baris-terpilih-dan-reset-seleksi-setelah-commit | FE+BE |
| TC-AC-SG-400 | E2E | TC-AC-SG-E2E-009-group-context-header-angka-agregat-node-tanpa-badge-dan-elipsis-node-header | FE+BE |
| TC-AC-SG-401 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-402 | E2E | TC-AC-SG-E2E-096-defense-in-depth-root-parent-duplikat-depth-limit-guard-delete-dan-selection-limit | FE+BE |
| TC-AC-SG-403 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |
| TC-AC-SG-404 | E2E | TC-AC-SG-E2E-098-state-tenant-write-lockdown-suspended-create-edit-delete-bulk-dan-add-subgroup-di-batas-kedalaman | FE+BE |

---

## 4. Ringkasan Suite dan Catatan

### 4.1 Ringkasan

- 116 spec menurunkan 404 TC (TC-AC-SG-1 sampai 404); setiap TC tepat satu spec (tanpa duplikasi sourceTc), TC Hanya-BE: 0. 113 spec `coverage.web: automated`, 3 spec mobile Android (014, 015, 107) `coverage.mobile: automated`.
- Semua spec bermode FE+BE (backend nyata, seeding via API); 3 di antaranya (003, 104, 105) memakai intercept respons di atas backend nyata untuk Loading state dan kegagalan terkontrol dan tetap ditandai FE+BE, bukan mock. Tidak ada spec `Mode: mock`.
- Suite serial karena banyak spec mengubah state bersama (Hierarchy Depth Limit, Selection Limit, status entitas Suspended/Expired/Grace/Archive, pohon group yang dihapus atau diubah, flag Guided Tooltip, perangkat Android). Hook, akun default, sesi API aktor, dan kemampuan reset baseline dinyatakan di `suite.md`.
- Akun aktor memakai 38 env password baru `AC_SG_*_PASSWORD` (lihat 4.5) selain `AC_TC_PASSWORD` yang sudah terdaftar.

### 4.2 Pemecahan dari Rencana

Rencana awal 105 spec (001-105). Penulis slice memecah beberapa spec yang melewati batas dan memakai nomor cadangan: 106 (TC-32, dari 009), 107 (TC-55 dan 56, dari 014), 108 (TC-67, dari 019), 109 (TC-70, dari 020), 110 (TC-144 dan 145, dari 041), 111 (TC-163 dan 164, dari 046), 112 (TC-232, dari 064), 114 (TC-269, dari 074), 115 (TC-292 dan 293, dari 079), 116 (TC-335 sampai 337, dari 091), 117 (TC-342, 351, dan 352, dari 092). Nomor 113 tidak dipakai dan tidak direnumber. Pemetaan sourceTc final adalah yang tertulis di frontmatter spec dan di tabel bagian 1 dan 3.

### 4.3 Spec di Atas ~35 Langkah (22 spec)

Dihitung dari jumlah langkah bernomor di bagian Test Steps (butir C6 `scripts/check-suite.py`): 001 (45); 005 (39); 012 (40); 017 (36); 020 (36); 027 (41); 033 (42); 034 (38); 043 (49); 066 (36); 071 (37); 082 (36); 083 (37); 086 (37); 087 (43); 088 (49); 090 (44); 091 (46); 093 (42); 094 (45); 098 (56); 099 (53); 100 (48); 102 (45); 104 (42); 116 (40) (nomor spec, jumlah langkah). Tiap spec punya alasan di `## Notes`: umumnya blok TC satu kelas fungsional atau satu kelas harness pada permukaan yang sama, tiap blok berdiri sendiri dengan data milik spec.

### 4.4 Catatan Khusus

- Spec 014, 015, dan 107 mobile Android (perangkat fisik bersama, `coverage.mobile: automated`); spec lain web.
- TC kelas guided tooltip (012, 013) mengatur flag Guided Tooltip sendiri sesudah hook suite.
- Spec 098 dan 099 mengubah status keaktifan entitas uji (kelas h, write-lockdown) dan memulihkannya di hook `after`.

### 4.5 Temuan QA Terpenting (Berulang di Banyak Spec)

1. Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, maupun LLD. Spec menyebutnya kemampuan Fixture BE/reset yang disediakan tim FE/BE (S-13) dan menjalankannya sebagai langkah penghubung serta di hook `after`.
2. Env password `AC_SG_*_PASSWORD` baru (RO, DU, MGCUD, MGC, MGU, MGD, MGCU, MGCD, MGUD, MGNONE, GM, ML, DIST, PARTNER, CLIENT, HAPUS, HAPUSMGD, SATU, DUA, TIGA, TIGACAMPUR, POHONDALAM, SUSPENDED, SUSPENDEDDALAM, EXPIRED, GRACEEXPIRED, GRACEDOWNGRADE, ARCHIVE, RACEA, RACEB, PEMBANDING, SELEKSI, TANPAGROUP, CHANGELOG, CHANGELOGKOSONG, CUSTOMFIELD, ANGGOTA) belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; harus didaftarkan pemilik repo e2e sebelum tahap script.
3. Banyak akun dan user Pre-setup (Joko Susilo, Nina Amelia, Lia Marlina, akun Manage group Delete saja pada Distributor Hapus Utama, nama tampil Manage group CUD, akun kedua Distributor Baru) tidak punya email atau password di tabel Pre-setup; spec menyebutnya disediakan tim FE.
4. Isi tree entitas Distributor Jaringan dan Partner Jaringan, nama Client pada `Hapus Campur M1` dan `M2`, dan kode TAG, Position, Division user uji tidak tertulis di Pre-setup; spec menulisnya sebagai data tambahan yang disediakan tim FE.
5. Label tombol hapus berbeda antar TC (TC-171 menulis `[Delete]`, TC-330 dan TC-373 menulis `Bulk Action` > `Delete`); spec mengikuti Expected tiap TC dan perlu dipastikan QA (PRD §4.2).
6. TC-321: keempat baris `Region A` bertipe `Distributor` sehingga sort Type tidak teruji bermakna (S-11, S-14); usulan data atau asersi indikator sort saja.
7. Beberapa Expected tidak menyebut cara pengamatan (TC-174 membaca 14 baris dari halaman 10 baris, TC-390 refresh tidak terjadi pada Edit No-Op); spec memakai pengamatan terdekat dan perlu dikonfirmasi tim FE.
8. Hook `beforeEach` suite membuka Settings > Group lewat sidebar sehingga tidak berlaku bagi akun tanpa menu `Group` (spec 016 blok Client dan spec 018); perlu pengecualian di hook suite.
9. Spec penghapus (038-047) dan 103 memakai node Pre-setup berlabel literal (mis. `Hapus Warn A`, `Hapus Warn B`) karena TC mengasersi nama node dan jumlah user; pemulihan dicatat di `## Prerequisites` dan perlu keputusan apakah dipertahankan atau diganti node milik spec (S-06).
10. Frontmatter spec mobile 014, 015, dan 107 memakai `coverage.mobile: automated` tanpa `coverage.web`; perlu keputusan apakah web perlu `unsupported` atau cukup mobile.
