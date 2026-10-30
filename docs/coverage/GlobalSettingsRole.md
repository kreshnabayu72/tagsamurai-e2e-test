# Coverage E2E — Global Settings > Role & Permission

Sumber: `global-settings/role/TestCases/tc-role.md` (317 ID `TC-GS-ROLE-1`–`317`, seluruhnya aktif). Referensi kontrak: `global-settings/role/PRD/role.md` dan `global-settings/role/API/openapi.yaml`. Suite: `specs/GlobalSettings/Role/`. Prefix: `GS` + `ROLE` (`TC-GS-ROLE-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 317 TC aktif masuk spec, 0 TC hanya-BE (TC-313 sampai TC-315 punya PIC FE `-` tetapi memuat langkah reload di UI, sehingga tetap masuk spec 099). 107 spec (105 FE+BE, 2 mock). Setiap TC terpetakan ke tepat satu spec.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | Screening Tab Total Control dan Tab Read Only: Urutan Default, Baris Default User, Status Inactive, dan Nama Panjang | FE+BE | 59 | 1, 2, 10, 11, 24 |
| TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | Screening Tab System: Navigasi ke Detail, Hover Role Name, dan Hitungan Kolom Users | FE+BE | 44 | 3, 6, 7, 8, 9, 14 |
| TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role | Screening Detail Role: Kolom CRUD Dinamis, Deskripsi Enam Role, dan Posisi Checkbox | FE+BE | 28 | 4, 5, 281 |
| TC-GS-ROLE-E2E-004-badge-kondisional-pending-activation-lintas-surface | Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Popup Assign Role | FE+BE | 16 | 12, 13 |
| TC-GS-ROLE-E2E-005-resilience-baca-loading-error-dan-try-again | Resilience Baca: Loading State per Surface, Error Load 5xx, dan Pulih lewat Try Again | mock | 54 | 15, 16, 17 |
| TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog | Empty State pada Client Uji B: Tab Read Only, Popup Assign, Modal Changelog, dan Tab Total Control yang Tidak Pernah Kosong | FE+BE | 28 | 18, 20, 68, 198 |
| TC-GS-ROLE-E2E-007-no-result-search-pada-tab-total-control-read-only-system-dan-detail | No-Result Search pada Tab Total Control, Tab Read Only, Tab System, dan Detail | FE+BE | 22 | 19 |
| TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-pemunculan-menu | Landing State User tanpa Access Level dan tanpa Role, serta Pemunculan Menu Setelah Mendapat Role | FE+BE | 21 | 21, 22 |
| TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | Hover Tooltip Icon Table Tools pada Tab Total Control, Tab System, dan Detail, serta Tooltip Modified By | mock | 33 | 23, 25 |
| TC-GS-ROLE-E2E-010-guided-tooltip-auto-launch-langkah-dan-done | Guided Tooltip Role & Permission: Kunjungan Pertama, Langkah 1 sampai 3, Done, dan Tab Aktif | FE+BE | 40 | 26, 27, 28 |
| TC-GS-ROLE-E2E-011-guided-tooltip-skip-back-replay-exit-dan-keyboard | Guided Tooltip Role & Permission: Skip, Back, Replay, Navigasi Keluar, dan Keyboard | FE+BE | 27 | 29, 30, 31 |
| TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | Mobile Detail Role: Header Import data, Keluar dari Selection Mode, Toggle Inert, dan Pagination Card List | FE+BE | 58 | 288, 310, 311, 312 |
| TC-GS-ROLE-E2E-013-mobile-detail-long-press-multi-select-dan-bulk-remove | Mobile Detail Role: Long Press Multi-Select, Floating Bottom Bulk Bar, dan Select All | FE+BE | 20 | 32 |
| TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar | Mobile Card List Role: Tab Total Control, Tab Read Only, Tab System, Toolbar, dan Bottom Sheet | FE+BE | 59 | 285, 286, 287 |
| TC-GS-ROLE-E2E-015-role-matrix-visibilitas-menu-sidebar-per-aktor | Role Matrix: Visibilitas Menu Sidebar Role & Permission per Aktor | FE+BE | 20 | 33, 34, 282 |
| TC-GS-ROLE-E2E-016-role-matrix-negatif-direct-url-tanpa-role-manage-user-and-role | Role Matrix Negatif: Akses Langsung URL Role & Permission Tanpa Role Manage user and role | FE+BE | 9 | 35 |
| TC-GS-ROLE-E2E-017-role-matrix-visibilitas-elemen-total-control-read-only-dan-manage-read-saja | Role Matrix: Visibilitas Elemen Role & Permission untuk Total Control, Read Only, dan Manage user and role Read Saja | FE+BE | 53 | 36, 37, 38 |
| TC-GS-ROLE-E2E-018-role-matrix-visibilitas-elemen-manage-user-and-role-tanpa-update-dan-dengan-update | Role Matrix: Visibilitas Elemen Role & Permission untuk Manage user and role Tanpa Update dan Dengan Update | FE+BE | 52 | 39, 40 |
| TC-GS-ROLE-E2E-019-guard-proteksi-default-user-dan-diri-sendiri-pada-tab-dan-detail | Guard Proteksi Default User dan Diri Sendiri pada Tab Total Control dan Detail | FE+BE | 57 | 41, 42, 43 |
| TC-GS-ROLE-E2E-020-prioritas-tooltip-elemen-non-aktif-lintas-aktor | Role Matrix: Prioritas Tooltip Elemen Non-Aktif pada Baris Default User Lintas Aktor | FE+BE | 26 | 44, 45, 46 |
| TC-GS-ROLE-E2E-021-aksesibilitas-keyboard-checkbox-detail-dan-focus-trap-dialog | Aksesibilitas Keyboard: Checkbox Detail, Tooltip Saat Fokus, dan Focus Trap Dialog Remove | FE+BE | 16 | 47, 48 |
| TC-GS-ROLE-E2E-022-role-matrix-gating-seleksi-checkbox-baris-detail | Role Matrix: Gating Seleksi Checkbox Baris Detail dan Select All per Aktor | FE+BE | 11 | 49, 50 |
| TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas | Popup Assign Total Control: Screening, Pool Kandidat, dan Aksesibilitas | FE+BE | 23 | 51, 52, 53, 77 |
| TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel | Popup Assign Total Control: Validasi Kosong, Selection Counter, Checkbox Header, dan Cancel | FE+BE | 35 | 54, 55, 56, 57 |
| TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | Popup Assign: Pencarian Name, Email, Position, Division, Status, dan No Result | FE+BE | 53 | 69, 70, 71, 72, 316 |
| TC-GS-ROLE-E2E-026-popup-assign-filter-panel | Popup Assign: Filter Panel Position, Division, Status, Activation Status, Temporary User, Temporary Until, dan Custom Field | FE+BE | 21 | 73, 74 |
| TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility | Popup Assign: Column Visibility, Sort Kolom, dan Pagination dengan Retensi Seleksi | FE+BE | 73 | 75, 76, 293, 317 |
| TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda | Assign Total Control: Sukses Satu dan Banyak User, Timpa Baris Parsial, dan Klik Ganda | FE+BE | 47 | 58, 59, 61, 63 |
| TC-GS-ROLE-E2E-029-assign-total-control-upgrade-read-only-dan-user-pending-email-confirmation | Assign Total Control: Upgrade User Read Only dan User Pending Email Confirmation | FE+BE | 23 | 60, 307 |
| TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | Konflik Assign: User Terpilih Dihapus atau Tidak Eligible Sebelum Submit (Alert Tunggal) | FE+BE | 69 | 65, 66, 67, 83, 292 |
| TC-GS-ROLE-E2E-031-konflik-assign-alert-jamak-user-dihapus | Konflik Assign: Alert Jamak User Terpilih Dihapus Admin Lain | FE+BE | 23 | 300, 304 |
| TC-GS-ROLE-E2E-032-konflik-assign-alert-jamak-user-tidak-eligible-dan-campuran | Konflik Assign: Alert Jamak User Tidak Eligible dan Campuran Dihapus dan Tidak Eligible | FE+BE | 35 | 301, 302, 305 |
| TC-GS-ROLE-E2E-033-konflik-assign-concurrent-user-sama-dua-admin | Konflik Assign: Dua Admin Meng-Assign User yang Sama Secara Bersamaan | FE+BE | 39 | 279, 280 |
| TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda | Assign Read Only: Screening Popup, Validasi, Sukses, dan Klik Ganda | FE+BE | 38 | 78, 79, 80, 82 |
| TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | Remove Access Level: Screening Dialog, Cancel, Sukses, dan Klik Ganda | FE+BE | 64 | 84, 85, 86, 87, 88, 91 |
| TC-GS-ROLE-E2E-036-popup-assign-role-screening-pool-dan-validasi | Popup Assign Role: Screening, Pool, dan Validasi Tanpa Memilih User | FE+BE | 12 | 92, 93 |
| TC-GS-ROLE-E2E-037-assign-role-role-matrix-positif | Role Matrix: Assign Role Positif oleh Total Control dan Manage user and role dengan Update | FE+BE | 26 | 94, 96 |
| TC-GS-ROLE-E2E-038-assign-role-baris-baru-default-dan-klik-ganda | Assign Role: Baris Baru Default dan Klik Ganda [Assign] | FE+BE | 16 | 95, 98 |
| TC-GS-ROLE-E2E-039-konflik-assign-role-user-dihapus-sudah-di-assign-atau-di-rename | Konflik Assign Role: User Dihapus, Sudah di-Assign, atau di-Rename oleh Admin Lain | FE+BE | 26 | 99, 100 |
| TC-GS-ROLE-E2E-040-edit-crud-role-matrix-positif | Role Matrix: Edit CRUD Positif oleh Total Control dan Manage user and role dengan Update | FE+BE | 22 | 101, 102, 103 |
| TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi | Auto-Revert saat Edit CRUD: Dialog, Cancel, dan Konfirmasi | FE+BE | 62 | 104, 105, 106, 107 |
| TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | Role Matrix: Remove Baris Role Positif (Screening, Cancel, Konfirmasi, dan Klik Ganda) | FE+BE | 51 | 110, 111, 112, 113, 119 |
| TC-GS-ROLE-E2E-043-remove-baris-auto-revert-dialog-konfirmasi-dan-cancel | Remove Baris Role Target Total Control dan Read Only: Dialog Auto-Revert, Konfirmasi, dan Cancel | FE+BE | 43 | 114, 115, 116 |
| TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | Bulk Action Bar Detail: Seleksi, Select All, dan Retensi Seleksi saat Search Dikosongkan | FE+BE | 38 | 120, 121, 122, 123, 136 |
| TC-GS-ROLE-E2E-045-selection-limit-volume-data-detail | Selection Limit Detail: Volume Data Melewati Batas Seleksi | FE+BE | 25 | 124, 125 |
| TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel | Bulk Remove: Screening Dialog Konfirmasi dan Cancel Mempertahankan Seleksi | FE+BE | 59 | 126, 127, 129, 130 |
| TC-GS-ROLE-E2E-047-bulk-remove-role-matrix-positif | Role Matrix Positif: Bulk Remove Baris Role Regular oleh Total Control dan Manage User and Role dengan Update | FE+BE | 19 | 128, 132 |
| TC-GS-ROLE-E2E-048-bulk-remove-satu-baris-dialog-single-dan-klik-ganda | Bulk Remove Satu Baris: Dialog Single dan Klik Ganda pada [Remove] | FE+BE | 43 | 135, 294, 295 |
| TC-GS-ROLE-E2E-049-bulk-remove-campuran-total-control-read-only-dan-regular | Bulk Remove Campuran Baris Regular, Total Control, dan Read Only | FE+BE | 17 | 131 |
| TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | Search Tab Total Control dan Tab Read Only: Siklus Input, Kolom Teks, Badge, TAG, dan Kolom Tanggal | FE+BE | 68 | 137, 138, 139, 140, 141 |
| TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | Filter Panel Tab Total Control dan Tab Read Only: Screening Field, Opsi Dropdown, dan Chip | FE+BE | 55 | 142, 143, 148, 149, 150 |
| TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter | Filter Fungsional: Multi-Select per Field, Date Range, OR dan AND, serta Urutan Search dan Filter | FE+BE | 78 | 144, 145, 147, 151 |
| TC-GS-ROLE-E2E-053-custom-field-aktif-search-filter-dan-sort | Custom Field Aktif Dropdown: Search, Filter, dan Sort Kolom Region | FE+BE | 22 | 146 |
| TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | Sort Kolom Tab Total Control dan Tab Read Only | FE+BE | 129 | 152, 153, 154, 155, 156 |
| TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | Kombinasi Search, Filter, Sort, Pagination, Retensi Refresh, dan Pindah Tab Total Control dan Read Only | FE+BE | 65 | 157, 158, 159, 160, 161 |
| TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | Setup Column Tab Total Control dan Read Only: Screening, Hide/Show Kolom, Tutup Tanpa Simpan, dan Kolom Visible Terakhir | FE+BE | 55 | 162, 163, 164, 165, 171, 172 |
| TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | Setup Column Tab Total Control: Reorder, Pin, Reset to Default, dan Isolasi Konfigurasi per Tabel | FE+BE | 64 | 166, 167, 168, 169, 170, 173 |
| TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | Download Tab Total Control dan Read Only: Nama File, Isi File, Cakupan Baris, Kolom Visible, dan Transformasi Nilai | FE+BE | 62 | 174, 175, 176, 177, 178 |
| TC-GS-ROLE-E2E-059-download-lebih-5000-baris-background-job | Download Tab Total Control di Atas 5.000 Baris Berjalan sebagai Background Job | FE+BE | 9 | 180 |
| TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | Tab System: Search, Sort Tidak Tersedia, Setup Column, dan Retensi Search Setelah Kembali dari Detail | FE+BE | 63 | 181, 182, 183, 184, 195 |
| TC-GS-ROLE-E2E-061-download-tab-system-dan-detail-isi-file | Download Tab System dan Detail: Nama File dan Isi File | FE+BE | 33 | 185, 194, 303 |
| TC-GS-ROLE-E2E-062-detail-search-name-position-division-dan-kolom-lain | Detail Manage TAG: Search Berdasarkan Name, Position, Division, dan Kolom Lain | FE+BE | 32 | 186, 187, 188 |
| TC-GS-ROLE-E2E-063-detail-filter-panel-screening-dan-per-field | Detail Manage TAG: Screening Panel Filter dan Filter per Field serta Kombinasi | FE+BE | 43 | 189, 190 |
| TC-GS-ROLE-E2E-064-detail-sort-dan-setup-column-kolom-crud | Detail Role: Sort per Kolom Data, Kolom CRUD Tidak Sortable, dan Setup Column Kolom CRUD | FE+BE | 98 | 191, 192, 193 |
| TC-GS-ROLE-E2E-065-modal-changelog-screening-semua-varian | Modal Changelog: Screening Varian Tab Total Control, Read Only, System, dan Detail | FE+BE | 33 | 196, 197 |
| TC-GS-ROLE-E2E-066-modal-changelog-search-dan-filter | Modal Changelog: Search per Kelas Kolom dan Filter Varian Tab Total Control, System, dan Detail | FE+BE | 64 | 199, 200, 201 |
| TC-GS-ROLE-E2E-067-modal-changelog-sort-setup-column-dan-pagination | Modal Changelog: Sort per Kolom, Setup Column, dan Pagination | FE+BE | 73 | 202, 203, 206 |
| TC-GS-ROLE-E2E-068-download-modal-changelog-isi-file-per-varian | Download Modal Changelog: Berkas CSV dan XLSX per Varian | FE+BE | 26 | 204 |
| TC-GS-ROLE-E2E-069-resilience-export-gagal-download-tabel-dan-changelog | Resilience Export: Kegagalan Download Tabel Total Control dan Modal Changelog | FE+BE | 13 | 179, 205 |
| TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role | Resilience Tulis: Assign Total Control, Read Only, dan Role Gagal 5xx atau Timeout | FE+BE | 51 | 64, 81, 97, 306 |
| TC-GS-ROLE-E2E-071-resilience-tulis-remove-access-level | Resilience Tulis: Remove Total Control dan Remove Read Only Gagal 5xx | FE+BE | 32 | 89, 90 |
| TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris | Resilience Tulis: Edit CRUD, Auto-Revert, dan Remove Baris Role Gagal 5xx | FE+BE | 58 | 108, 109, 117, 118 |
| TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial | Resilience Tulis: Bulk Remove Gagal 5xx, Timeout, dan Sukses Parsial | FE+BE | 42 | 133, 261, 309 |
| TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert | Pencatatan Changelog Tab Total Control: Assign, Upgrade dari Read Only, Remove, dan Auto-Revert | FE+BE | 36 | 207, 208, 209, 210 |
| TC-GS-ROLE-E2E-075-pencatatan-changelog-read-only-assign-remove-dan-auto-revert | Pencatatan Changelog Tab Read Only: Assign, Remove, dan Auto-Revert | FE+BE | 18 | 211 |
| TC-GS-ROLE-E2E-076-pencatatan-changelog-system-dan-detail-edit-field-create-update-delete | Pencatatan Changelog Tab System dan Detail: Edit Field Create, Update, dan Delete | FE+BE | 29 | 212, 213, 214 |
| TC-GS-ROLE-E2E-077-pencatatan-changelog-system-dan-detail-assign-remove-baris-dan-superset | Pencatatan Changelog Tab System dan Detail: Assign dan Remove Baris Role serta Tab System sebagai Superset Detail | FE+BE | 40 | 215, 216, 219 |
| TC-GS-ROLE-E2E-078-pencatatan-changelog-remove-baris-target-tc-dan-bulk-remove-per-tier | Pencatatan Changelog: Remove Baris Target Total Control dan Bulk Remove per Tier | FE+BE | 34 | 217, 218 |
| TC-GS-ROLE-E2E-079-pencatatan-log-lama-tidak-berubah-setelah-rename-dan-modified-by-last-updated | Pencatatan Log Lama Tidak Berubah setelah Rename User serta Modified By dan Last Updated oleh Assign | FE+BE | 19 | 220, 225 |
| TC-GS-ROLE-E2E-080-pencatatan-system-log-aktor-dan-activity-log-access-level | Pencatatan System Log Aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Access Level | FE+BE | 42 | 221, 289 |
| TC-GS-ROLE-E2E-081-pencatatan-system-log-aktor-dan-activity-log-baris-role | Pencatatan System Log Aktor dan Activity Log untuk Edit, Assign, dan Remove Baris Role | FE+BE | 21 | 222 |
| TC-GS-ROLE-E2E-082-pencatatan-changelog-user-dan-changelog-user-role | Pencatatan Changelog: User dan Changelog: User > Role | FE+BE | 27 | 223, 290 |
| TC-GS-ROLE-E2E-083-absence-log-assign-total-control-tidak-menulis-changelog-user-role | Absence Log: Assign Total Control Tidak Menulis Entry ke Changelog: User > Role | FE+BE | 8 | 224 |
| TC-GS-ROLE-E2E-084-sinkron-menu-modul-target-assign-remove-baris-dan-edit-crud | Sinkronisasi Menu Modul Target: Assign Role, Remove Baris, dan Edit CRUD | FE+BE | 29 | 226, 227, 228 |
| TC-GS-ROLE-E2E-085-sinkron-sidebar-target-assign-dan-remove-total-control | Sinkronisasi Sidebar Target: Assign dan Remove Total Control | FE+BE | 18 | 229, 230 |
| TC-GS-ROLE-E2E-086-sinkron-edit-crud-dengan-user-detail-tab-role | Sinkronisasi Edit CRUD antara Detail Role dan Tab Role User Detail | FE+BE | 12 | 231, 232 |
| TC-GS-ROLE-E2E-087-cascade-remove-access-global-settings-pada-tab-dan-detail | Cascade Remove Access Global Settings pada Tab dan Detail Role | FE+BE | 73 | 233, 234, 291 |
| TC-GS-ROLE-E2E-088-cascade-user-dihapus-atau-dinonaktifkan | Cascade User Dihapus atau Dinonaktifkan pada Tab dan Detail Role | FE+BE | 28 | 235, 236 |
| TC-GS-ROLE-E2E-089-sinkron-rename-position-dan-status-custom-field | Sinkronisasi Rename Position dan Status Custom Field pada Tab Total Control | FE+BE | 23 | 237, 240 |
| TC-GS-ROLE-E2E-090-format-tanggal-general-settings-tab-dan-changelog | Format Tanggal General Settings pada Tab Total Control dan Modal Changelog | FE+BE | 21 | 238, 239 |
| TC-GS-ROLE-E2E-091-notifikasi-in-app-remove-access-level-dan-assign-tanpa-notifikasi | Notifikasi In-App Remove Access Level dan Assign Total Control Tanpa Notifikasi | FE+BE | 34 | 62, 241, 242 |
| TC-GS-ROLE-E2E-092-notifikasi-in-app-auto-revert-dan-bulk-remove | Notifikasi In-App Auto-Revert dan Bulk Remove | FE+BE | 44 | 243, 244, 245 |
| TC-GS-ROLE-E2E-093-tanpa-gating-plan-role-tampil-di-semua-plan | Fitur Ber-Plan Tetap Muncul sebagai Role di Semua Plan | FE+BE | 27 | 246 |
| TC-GS-ROLE-E2E-094-isolasi-akses-produk-lain-assign-total-control | Isolasi Akses Produk Lain pada Assign Total Control Global Settings | FE+BE | 12 | 283 |
| TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level | State Tenant Suspended: Write-Lockdown Aksi Access Level pada Tab Total Control dan Read Only | FE+BE | 38 | 263, 264, 265, 266 |
| TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail | State Tenant Suspended: Write-Lockdown Aksi Tulis pada Detail Manage TAG | FE+BE | 31 | 267, 268, 269, 270 |
| TC-GS-ROLE-E2E-097-state-tenant-suspended-tetap-dapat-melihat | State Tenant Suspended: Tab dan Detail Role & Permission Tetap Dapat Dilihat | FE+BE | 8 | 271 |
| TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | Defense-in-Depth: Edit CRUD, Remove Baris Role, dan Aksi Tulis Detail Lewat Permintaan Langsung Ditolak | FE+BE | 44 | 247, 248, 249, 250, 251, 252, 257 |
| TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | Defense-in-Depth: Remove Access Level dan Assign ke Diri Sendiri Lewat Permintaan Langsung Ditolak | FE+BE | 51 | 253, 254, 255, 256, 313, 314, 315 |
| TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403 | Defense-in-Depth: Flag Payload Diabaikan, Bulk Remove Default User, dan Prioritas Pesan 403 | FE+BE | 33 | 258, 259, 260, 308 |
| TC-GS-ROLE-E2E-101-isolasi-data-entitas-lain | Isolasi Data: Permintaan List Tab Total Control dengan Identitas Client Lain Tidak Mengembalikan User Client Lain | FE+BE | 5 | 262 |
| TC-GS-ROLE-E2E-102-default-user-tetap-total-control-setelah-semua-total-control-lain-di-remove | Default User Tetap Total Control Setelah Semua Total Control Lain Di-Remove | FE+BE | 24 | 278 |
| TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus | Konflik Antar Admin pada Edit CRUD: Nilai Sama, Status Total Control Berubah, dan Baris Sudah Dihapus | FE+BE | 34 | 272, 273, 284 |
| TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control | Konflik Antar Admin pada Remove Baris Role: Sudah Dihapus Admin Lain atau Target Menjadi Total Control | FE+BE | 36 | 274, 276, 297 |
| TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda | Konflik Antar Admin pada Remove Access Level: Target Sudah di-Remove atau Tier Berbeda dari Tab yang Dirender | FE+BE | 41 | 275, 298 |
| TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil | Konflik Antar Admin pada Bulk Remove: Sebagian Baris Sudah Dihapus, Status Total Control Berubah, dan Nol Baris Berhasil | FE+BE | 62 | 134, 296, 299 |
| TC-GS-ROLE-E2E-107-realtime-auto-revert-pada-tab-total-control-sesi-admin-lain | Realtime: Auto-Revert Menghilangkan User dari Tab Total Control Sesi Admin Lain Tanpa Reload | FE+BE | 8 | 277 |

Kolom Langkah = jumlah langkah bernomor nominal; spec dengan perulangan tabel punya ekspansi lebih besar yang dihitung di `## Notes` spec itu. Spec di atas sekitar 35 langkah memuat alasan di `## Notes`.

## Pembagian TC lintas spec

Tidak ada TC yang terbelah lintas spec pada sourceTc; rujukan absence log (kelas g) ada di `## Notes` spec 083 dan spec fungsional terkait (S-05).

## Kebutuhan lingkungan (tim FE)

- Env baru belum terdaftar di `spectra.config.ts` dan `.env.example` (hanya disebut di Prerequisites spec): `GS_ROLE_MANAGE_CRUD_PASSWORD` (Hendra Wijaya), `GS_ROLE_MANAGE_READ_PASSWORD` (Fajar Nugroho), `GS_ROLE_MANAGE_CRD_PASSWORD` (Lina Marlina), `GS_ROLE_MANAGETAG_READ_PASSWORD` (Yusuf Hidayat), `GS_ROLE_TARGET_PASSWORD` (akun target yang login di sesi sendiri, mis. Agus Salim).
- Env yang sudah ada dan dipakai: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (Eko Prasetyo), `GS_RO_PASSWORD`, `GS_DEFAULT_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTSUSP_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`.
- Kemampuan teknis yang disediakan tim FE/BE (tanpa endpoint karangan): seeding dan pemulihan Given lewat API (access level, baris role, user bersuffix), aksi admin kedua lewat sesi API, membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_gs-role`, membaca berkas CSV/XLSX terunduh, mengamati request jaringan, `Spectra.intercept()` untuk kegagalan 5xx dan timeout, dua konteks browser paralel, perangkat Android uji (spec 012 sampai 014), data volume (≥101 baris eligible untuk Detail Manage hardware, >5.000 user untuk Tab Total Control), mengubah Selection Limit, Client B/C/plan, Custom Field `Region`, dan kunci flag Guided Tooltip halaman User.

## Temuan yang masih terbuka

Rincian per TC ada di sub-butir "Temuan untuk QA" pada `## Notes` tiap spec. Ringkasan lintas spec:

- TC-74 (spec 026): Expected a (hanya Rudi Hartono) bertentangan dengan Pre-setup #18 (Yoga Pratama, Pending Activation, ada di pool).
- TC-180 (spec 059): Expected (toast informasional, background job, notifikasi `[Download]`) bertentangan dengan `error-handling-convention.md` §10.1 (loading screen).
- TC-37/38/39 (spec 017, 018): Expected d menyebut checkbox Create/Update/Delete di Detail Manage TAG, padahal Manage TAG hanya punya Read dan Update.
- TC-26 (spec 010): kunci flag Guided Tooltip `gs-role-permission` berbeda dari kunci hook suite `guided_tooltip_seen_gs-role`.
- TC-144/139 (spec 050, 052): klausa "hanya Siti Nurhaliza" bertentangan dengan Pre-setup #19 (Intan Permata, Read Only, Active).
- TC-298 (spec 105): "baris keenam role" Rizal Hakim bertentangan dengan Pre-setup #18 ("tanpa baris role").
- TC-228 (spec 084): Doni Pratama "Manage files Read saja" berbeda dari Pre-setup #10 (R,D).
- TC-245 (spec 092): Rina Putri Inactive di Pre-setup #4 tetapi diminta login; TC-233 Expected d (notifikasi) tanpa langkah observasi (spec 087).
- Pre-setup #18 dan #11 hanya ber-Access Global Settings; mencabutnya ditolak V-15 sehingga spec 087 menambah Access produk lain sebagai Given.
- Post Condition tanpa langkah observasi tidak diasersi (dicatat per spec).
- Estimasi langkah di rencana lebih rendah dari hasil: banyak spec berada di atas sekitar 35 langkah (satu `Verifikasi` per klausa, S-01); alasan tertulis di Notes dan perlu ditinjau QA untuk spec dengan ekspansi >70 langkah (mis. 054, 064, 067, 035, 087).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-ROLE-1 | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | FE+BE |
| TC-GS-ROLE-2 | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | FE+BE |
| TC-GS-ROLE-3 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-4 | TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role | FE+BE |
| TC-GS-ROLE-5 | TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role | FE+BE |
| TC-GS-ROLE-6 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-7 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-8 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-9 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-10 | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | FE+BE |
| TC-GS-ROLE-11 | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | FE+BE |
| TC-GS-ROLE-12 | TC-GS-ROLE-E2E-004-badge-kondisional-pending-activation-lintas-surface | FE+BE |
| TC-GS-ROLE-13 | TC-GS-ROLE-E2E-004-badge-kondisional-pending-activation-lintas-surface | FE+BE |
| TC-GS-ROLE-14 | TC-GS-ROLE-E2E-002-screening-tab-system-navigasi-detail-dan-hitungan-users | FE+BE |
| TC-GS-ROLE-15 | TC-GS-ROLE-E2E-005-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-ROLE-16 | TC-GS-ROLE-E2E-005-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-ROLE-17 | TC-GS-ROLE-E2E-005-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-ROLE-18 | TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog | FE+BE |
| TC-GS-ROLE-19 | TC-GS-ROLE-E2E-007-no-result-search-pada-tab-total-control-read-only-system-dan-detail | FE+BE |
| TC-GS-ROLE-20 | TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog | FE+BE |
| TC-GS-ROLE-21 | TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-pemunculan-menu | FE+BE |
| TC-GS-ROLE-22 | TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-pemunculan-menu | FE+BE |
| TC-GS-ROLE-23 | TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | mock |
| TC-GS-ROLE-24 | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-read-only-urutan-default-dan-nama-panjang | FE+BE |
| TC-GS-ROLE-25 | TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | mock |
| TC-GS-ROLE-26 | TC-GS-ROLE-E2E-010-guided-tooltip-auto-launch-langkah-dan-done | FE+BE |
| TC-GS-ROLE-27 | TC-GS-ROLE-E2E-010-guided-tooltip-auto-launch-langkah-dan-done | FE+BE |
| TC-GS-ROLE-28 | TC-GS-ROLE-E2E-010-guided-tooltip-auto-launch-langkah-dan-done | FE+BE |
| TC-GS-ROLE-29 | TC-GS-ROLE-E2E-011-guided-tooltip-skip-back-replay-exit-dan-keyboard | FE+BE |
| TC-GS-ROLE-30 | TC-GS-ROLE-E2E-011-guided-tooltip-skip-back-replay-exit-dan-keyboard | FE+BE |
| TC-GS-ROLE-31 | TC-GS-ROLE-E2E-011-guided-tooltip-skip-back-replay-exit-dan-keyboard | FE+BE |
| TC-GS-ROLE-32 | TC-GS-ROLE-E2E-013-mobile-detail-long-press-multi-select-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-33 | TC-GS-ROLE-E2E-015-role-matrix-visibilitas-menu-sidebar-per-aktor | FE+BE |
| TC-GS-ROLE-34 | TC-GS-ROLE-E2E-015-role-matrix-visibilitas-menu-sidebar-per-aktor | FE+BE |
| TC-GS-ROLE-35 | TC-GS-ROLE-E2E-016-role-matrix-negatif-direct-url-tanpa-role-manage-user-and-role | FE+BE |
| TC-GS-ROLE-36 | TC-GS-ROLE-E2E-017-role-matrix-visibilitas-elemen-total-control-read-only-dan-manage-read-saja | FE+BE |
| TC-GS-ROLE-37 | TC-GS-ROLE-E2E-017-role-matrix-visibilitas-elemen-total-control-read-only-dan-manage-read-saja | FE+BE |
| TC-GS-ROLE-38 | TC-GS-ROLE-E2E-017-role-matrix-visibilitas-elemen-total-control-read-only-dan-manage-read-saja | FE+BE |
| TC-GS-ROLE-39 | TC-GS-ROLE-E2E-018-role-matrix-visibilitas-elemen-manage-user-and-role-tanpa-update-dan-dengan-update | FE+BE |
| TC-GS-ROLE-40 | TC-GS-ROLE-E2E-018-role-matrix-visibilitas-elemen-manage-user-and-role-tanpa-update-dan-dengan-update | FE+BE |
| TC-GS-ROLE-41 | TC-GS-ROLE-E2E-019-guard-proteksi-default-user-dan-diri-sendiri-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-42 | TC-GS-ROLE-E2E-019-guard-proteksi-default-user-dan-diri-sendiri-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-43 | TC-GS-ROLE-E2E-019-guard-proteksi-default-user-dan-diri-sendiri-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-44 | TC-GS-ROLE-E2E-020-prioritas-tooltip-elemen-non-aktif-lintas-aktor | FE+BE |
| TC-GS-ROLE-45 | TC-GS-ROLE-E2E-020-prioritas-tooltip-elemen-non-aktif-lintas-aktor | FE+BE |
| TC-GS-ROLE-46 | TC-GS-ROLE-E2E-020-prioritas-tooltip-elemen-non-aktif-lintas-aktor | FE+BE |
| TC-GS-ROLE-47 | TC-GS-ROLE-E2E-021-aksesibilitas-keyboard-checkbox-detail-dan-focus-trap-dialog | FE+BE |
| TC-GS-ROLE-48 | TC-GS-ROLE-E2E-021-aksesibilitas-keyboard-checkbox-detail-dan-focus-trap-dialog | FE+BE |
| TC-GS-ROLE-49 | TC-GS-ROLE-E2E-022-role-matrix-gating-seleksi-checkbox-baris-detail | FE+BE |
| TC-GS-ROLE-50 | TC-GS-ROLE-E2E-022-role-matrix-gating-seleksi-checkbox-baris-detail | FE+BE |
| TC-GS-ROLE-51 | TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas | FE+BE |
| TC-GS-ROLE-52 | TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas | FE+BE |
| TC-GS-ROLE-53 | TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas | FE+BE |
| TC-GS-ROLE-54 | TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel | FE+BE |
| TC-GS-ROLE-55 | TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel | FE+BE |
| TC-GS-ROLE-56 | TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel | FE+BE |
| TC-GS-ROLE-57 | TC-GS-ROLE-E2E-024-popup-assign-total-control-seleksi-counter-validasi-kosong-dan-cancel | FE+BE |
| TC-GS-ROLE-58 | TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-59 | TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-60 | TC-GS-ROLE-E2E-029-assign-total-control-upgrade-read-only-dan-user-pending-email-confirmation | FE+BE |
| TC-GS-ROLE-61 | TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-62 | TC-GS-ROLE-E2E-091-notifikasi-in-app-remove-access-level-dan-assign-tanpa-notifikasi | FE+BE |
| TC-GS-ROLE-63 | TC-GS-ROLE-E2E-028-assign-total-control-sukses-satu-banyak-timpa-parsial-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-64 | TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role | FE+BE |
| TC-GS-ROLE-65 | TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | FE+BE |
| TC-GS-ROLE-66 | TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | FE+BE |
| TC-GS-ROLE-67 | TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | FE+BE |
| TC-GS-ROLE-68 | TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog | FE+BE |
| TC-GS-ROLE-69 | TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | FE+BE |
| TC-GS-ROLE-70 | TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | FE+BE |
| TC-GS-ROLE-71 | TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | FE+BE |
| TC-GS-ROLE-72 | TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | FE+BE |
| TC-GS-ROLE-73 | TC-GS-ROLE-E2E-026-popup-assign-filter-panel | FE+BE |
| TC-GS-ROLE-74 | TC-GS-ROLE-E2E-026-popup-assign-filter-panel | FE+BE |
| TC-GS-ROLE-75 | TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility | FE+BE |
| TC-GS-ROLE-76 | TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility | FE+BE |
| TC-GS-ROLE-77 | TC-GS-ROLE-E2E-023-popup-assign-total-control-screening-pool-dan-aksesibilitas | FE+BE |
| TC-GS-ROLE-78 | TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-79 | TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-80 | TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-81 | TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role | FE+BE |
| TC-GS-ROLE-82 | TC-GS-ROLE-E2E-034-assign-read-only-screening-popup-validasi-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-83 | TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | FE+BE |
| TC-GS-ROLE-84 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-85 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-86 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-87 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-88 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-89 | TC-GS-ROLE-E2E-071-resilience-tulis-remove-access-level | FE+BE |
| TC-GS-ROLE-90 | TC-GS-ROLE-E2E-071-resilience-tulis-remove-access-level | FE+BE |
| TC-GS-ROLE-91 | TC-GS-ROLE-E2E-035-remove-access-level-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-92 | TC-GS-ROLE-E2E-036-popup-assign-role-screening-pool-dan-validasi | FE+BE |
| TC-GS-ROLE-93 | TC-GS-ROLE-E2E-036-popup-assign-role-screening-pool-dan-validasi | FE+BE |
| TC-GS-ROLE-94 | TC-GS-ROLE-E2E-037-assign-role-role-matrix-positif | FE+BE |
| TC-GS-ROLE-95 | TC-GS-ROLE-E2E-038-assign-role-baris-baru-default-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-96 | TC-GS-ROLE-E2E-037-assign-role-role-matrix-positif | FE+BE |
| TC-GS-ROLE-97 | TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role | FE+BE |
| TC-GS-ROLE-98 | TC-GS-ROLE-E2E-038-assign-role-baris-baru-default-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-99 | TC-GS-ROLE-E2E-039-konflik-assign-role-user-dihapus-sudah-di-assign-atau-di-rename | FE+BE |
| TC-GS-ROLE-100 | TC-GS-ROLE-E2E-039-konflik-assign-role-user-dihapus-sudah-di-assign-atau-di-rename | FE+BE |
| TC-GS-ROLE-101 | TC-GS-ROLE-E2E-040-edit-crud-role-matrix-positif | FE+BE |
| TC-GS-ROLE-102 | TC-GS-ROLE-E2E-040-edit-crud-role-matrix-positif | FE+BE |
| TC-GS-ROLE-103 | TC-GS-ROLE-E2E-040-edit-crud-role-matrix-positif | FE+BE |
| TC-GS-ROLE-104 | TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi | FE+BE |
| TC-GS-ROLE-105 | TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi | FE+BE |
| TC-GS-ROLE-106 | TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi | FE+BE |
| TC-GS-ROLE-107 | TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi | FE+BE |
| TC-GS-ROLE-108 | TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris | FE+BE |
| TC-GS-ROLE-109 | TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris | FE+BE |
| TC-GS-ROLE-110 | TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-111 | TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-112 | TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-113 | TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-114 | TC-GS-ROLE-E2E-043-remove-baris-auto-revert-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-GS-ROLE-115 | TC-GS-ROLE-E2E-043-remove-baris-auto-revert-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-GS-ROLE-116 | TC-GS-ROLE-E2E-043-remove-baris-auto-revert-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-GS-ROLE-117 | TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris | FE+BE |
| TC-GS-ROLE-118 | TC-GS-ROLE-E2E-072-resilience-tulis-edit-crud-dan-remove-baris | FE+BE |
| TC-GS-ROLE-119 | TC-GS-ROLE-E2E-042-remove-baris-role-matrix-positif-screening-cancel-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-120 | TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-ROLE-121 | TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-ROLE-122 | TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-ROLE-123 | TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-ROLE-124 | TC-GS-ROLE-E2E-045-selection-limit-volume-data-detail | FE+BE |
| TC-GS-ROLE-125 | TC-GS-ROLE-E2E-045-selection-limit-volume-data-detail | FE+BE |
| TC-GS-ROLE-126 | TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel | FE+BE |
| TC-GS-ROLE-127 | TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel | FE+BE |
| TC-GS-ROLE-128 | TC-GS-ROLE-E2E-047-bulk-remove-role-matrix-positif | FE+BE |
| TC-GS-ROLE-129 | TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel | FE+BE |
| TC-GS-ROLE-130 | TC-GS-ROLE-E2E-046-bulk-remove-dialog-screening-dan-cancel | FE+BE |
| TC-GS-ROLE-131 | TC-GS-ROLE-E2E-049-bulk-remove-campuran-total-control-read-only-dan-regular | FE+BE |
| TC-GS-ROLE-132 | TC-GS-ROLE-E2E-047-bulk-remove-role-matrix-positif | FE+BE |
| TC-GS-ROLE-133 | TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial | FE+BE |
| TC-GS-ROLE-134 | TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil | FE+BE |
| TC-GS-ROLE-135 | TC-GS-ROLE-E2E-048-bulk-remove-satu-baris-dialog-single-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-136 | TC-GS-ROLE-E2E-044-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-ROLE-137 | TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-138 | TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-139 | TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-140 | TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-141 | TC-GS-ROLE-E2E-050-search-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-142 | TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | FE+BE |
| TC-GS-ROLE-143 | TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | FE+BE |
| TC-GS-ROLE-144 | TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter | FE+BE |
| TC-GS-ROLE-145 | TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter | FE+BE |
| TC-GS-ROLE-146 | TC-GS-ROLE-E2E-053-custom-field-aktif-search-filter-dan-sort | FE+BE |
| TC-GS-ROLE-147 | TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter | FE+BE |
| TC-GS-ROLE-148 | TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | FE+BE |
| TC-GS-ROLE-149 | TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | FE+BE |
| TC-GS-ROLE-150 | TC-GS-ROLE-E2E-051-filter-panel-screening-opsi-dan-chip | FE+BE |
| TC-GS-ROLE-151 | TC-GS-ROLE-E2E-052-filter-fungsional-multi-select-date-range-dan-urutan-search-filter | FE+BE |
| TC-GS-ROLE-152 | TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-153 | TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-154 | TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-155 | TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-156 | TC-GS-ROLE-E2E-054-sort-kolom-tab-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-157 | TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | FE+BE |
| TC-GS-ROLE-158 | TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | FE+BE |
| TC-GS-ROLE-159 | TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | FE+BE |
| TC-GS-ROLE-160 | TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | FE+BE |
| TC-GS-ROLE-161 | TC-GS-ROLE-E2E-055-kombinasi-pagination-retensi-refresh-dan-pindah-tab | FE+BE |
| TC-GS-ROLE-162 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-163 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-164 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-165 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-166 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-167 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-168 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-169 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-170 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-171 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-172 | TC-GS-ROLE-E2E-056-setup-column-tab-total-control-screening-hide-show-discard-dan-kolom-terakhir | FE+BE |
| TC-GS-ROLE-173 | TC-GS-ROLE-E2E-057-setup-column-tab-total-control-reorder-pin-reset-dan-isolasi-per-tabel | FE+BE |
| TC-GS-ROLE-174 | TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | FE+BE |
| TC-GS-ROLE-175 | TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | FE+BE |
| TC-GS-ROLE-176 | TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | FE+BE |
| TC-GS-ROLE-177 | TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | FE+BE |
| TC-GS-ROLE-178 | TC-GS-ROLE-E2E-058-download-tab-total-control-dan-read-only-isi-file | FE+BE |
| TC-GS-ROLE-179 | TC-GS-ROLE-E2E-069-resilience-export-gagal-download-tabel-dan-changelog | FE+BE |
| TC-GS-ROLE-180 | TC-GS-ROLE-E2E-059-download-lebih-5000-baris-background-job | FE+BE |
| TC-GS-ROLE-181 | TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | FE+BE |
| TC-GS-ROLE-182 | TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | FE+BE |
| TC-GS-ROLE-183 | TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | FE+BE |
| TC-GS-ROLE-184 | TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | FE+BE |
| TC-GS-ROLE-185 | TC-GS-ROLE-E2E-061-download-tab-system-dan-detail-isi-file | FE+BE |
| TC-GS-ROLE-186 | TC-GS-ROLE-E2E-062-detail-search-name-position-division-dan-kolom-lain | FE+BE |
| TC-GS-ROLE-187 | TC-GS-ROLE-E2E-062-detail-search-name-position-division-dan-kolom-lain | FE+BE |
| TC-GS-ROLE-188 | TC-GS-ROLE-E2E-062-detail-search-name-position-division-dan-kolom-lain | FE+BE |
| TC-GS-ROLE-189 | TC-GS-ROLE-E2E-063-detail-filter-panel-screening-dan-per-field | FE+BE |
| TC-GS-ROLE-190 | TC-GS-ROLE-E2E-063-detail-filter-panel-screening-dan-per-field | FE+BE |
| TC-GS-ROLE-191 | TC-GS-ROLE-E2E-064-detail-sort-dan-setup-column-kolom-crud | FE+BE |
| TC-GS-ROLE-192 | TC-GS-ROLE-E2E-064-detail-sort-dan-setup-column-kolom-crud | FE+BE |
| TC-GS-ROLE-193 | TC-GS-ROLE-E2E-064-detail-sort-dan-setup-column-kolom-crud | FE+BE |
| TC-GS-ROLE-194 | TC-GS-ROLE-E2E-061-download-tab-system-dan-detail-isi-file | FE+BE |
| TC-GS-ROLE-195 | TC-GS-ROLE-E2E-060-tab-system-search-sort-setup-column-dan-retensi-dari-detail | FE+BE |
| TC-GS-ROLE-196 | TC-GS-ROLE-E2E-065-modal-changelog-screening-semua-varian | FE+BE |
| TC-GS-ROLE-197 | TC-GS-ROLE-E2E-065-modal-changelog-screening-semua-varian | FE+BE |
| TC-GS-ROLE-198 | TC-GS-ROLE-E2E-006-empty-state-client-uji-b-tab-popup-assign-dan-changelog | FE+BE |
| TC-GS-ROLE-199 | TC-GS-ROLE-E2E-066-modal-changelog-search-dan-filter | FE+BE |
| TC-GS-ROLE-200 | TC-GS-ROLE-E2E-066-modal-changelog-search-dan-filter | FE+BE |
| TC-GS-ROLE-201 | TC-GS-ROLE-E2E-066-modal-changelog-search-dan-filter | FE+BE |
| TC-GS-ROLE-202 | TC-GS-ROLE-E2E-067-modal-changelog-sort-setup-column-dan-pagination | FE+BE |
| TC-GS-ROLE-203 | TC-GS-ROLE-E2E-067-modal-changelog-sort-setup-column-dan-pagination | FE+BE |
| TC-GS-ROLE-204 | TC-GS-ROLE-E2E-068-download-modal-changelog-isi-file-per-varian | FE+BE |
| TC-GS-ROLE-205 | TC-GS-ROLE-E2E-069-resilience-export-gagal-download-tabel-dan-changelog | FE+BE |
| TC-GS-ROLE-206 | TC-GS-ROLE-E2E-067-modal-changelog-sort-setup-column-dan-pagination | FE+BE |
| TC-GS-ROLE-207 | TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-208 | TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-209 | TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-210 | TC-GS-ROLE-E2E-074-pencatatan-changelog-total-control-assign-upgrade-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-211 | TC-GS-ROLE-E2E-075-pencatatan-changelog-read-only-assign-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-212 | TC-GS-ROLE-E2E-076-pencatatan-changelog-system-dan-detail-edit-field-create-update-delete | FE+BE |
| TC-GS-ROLE-213 | TC-GS-ROLE-E2E-076-pencatatan-changelog-system-dan-detail-edit-field-create-update-delete | FE+BE |
| TC-GS-ROLE-214 | TC-GS-ROLE-E2E-076-pencatatan-changelog-system-dan-detail-edit-field-create-update-delete | FE+BE |
| TC-GS-ROLE-215 | TC-GS-ROLE-E2E-077-pencatatan-changelog-system-dan-detail-assign-remove-baris-dan-superset | FE+BE |
| TC-GS-ROLE-216 | TC-GS-ROLE-E2E-077-pencatatan-changelog-system-dan-detail-assign-remove-baris-dan-superset | FE+BE |
| TC-GS-ROLE-217 | TC-GS-ROLE-E2E-078-pencatatan-changelog-remove-baris-target-tc-dan-bulk-remove-per-tier | FE+BE |
| TC-GS-ROLE-218 | TC-GS-ROLE-E2E-078-pencatatan-changelog-remove-baris-target-tc-dan-bulk-remove-per-tier | FE+BE |
| TC-GS-ROLE-219 | TC-GS-ROLE-E2E-077-pencatatan-changelog-system-dan-detail-assign-remove-baris-dan-superset | FE+BE |
| TC-GS-ROLE-220 | TC-GS-ROLE-E2E-079-pencatatan-log-lama-tidak-berubah-setelah-rename-dan-modified-by-last-updated | FE+BE |
| TC-GS-ROLE-221 | TC-GS-ROLE-E2E-080-pencatatan-system-log-aktor-dan-activity-log-access-level | FE+BE |
| TC-GS-ROLE-222 | TC-GS-ROLE-E2E-081-pencatatan-system-log-aktor-dan-activity-log-baris-role | FE+BE |
| TC-GS-ROLE-223 | TC-GS-ROLE-E2E-082-pencatatan-changelog-user-dan-changelog-user-role | FE+BE |
| TC-GS-ROLE-224 | TC-GS-ROLE-E2E-083-absence-log-assign-total-control-tidak-menulis-changelog-user-role | FE+BE |
| TC-GS-ROLE-225 | TC-GS-ROLE-E2E-079-pencatatan-log-lama-tidak-berubah-setelah-rename-dan-modified-by-last-updated | FE+BE |
| TC-GS-ROLE-226 | TC-GS-ROLE-E2E-084-sinkron-menu-modul-target-assign-remove-baris-dan-edit-crud | FE+BE |
| TC-GS-ROLE-227 | TC-GS-ROLE-E2E-084-sinkron-menu-modul-target-assign-remove-baris-dan-edit-crud | FE+BE |
| TC-GS-ROLE-228 | TC-GS-ROLE-E2E-084-sinkron-menu-modul-target-assign-remove-baris-dan-edit-crud | FE+BE |
| TC-GS-ROLE-229 | TC-GS-ROLE-E2E-085-sinkron-sidebar-target-assign-dan-remove-total-control | FE+BE |
| TC-GS-ROLE-230 | TC-GS-ROLE-E2E-085-sinkron-sidebar-target-assign-dan-remove-total-control | FE+BE |
| TC-GS-ROLE-231 | TC-GS-ROLE-E2E-086-sinkron-edit-crud-dengan-user-detail-tab-role | FE+BE |
| TC-GS-ROLE-232 | TC-GS-ROLE-E2E-086-sinkron-edit-crud-dengan-user-detail-tab-role | FE+BE |
| TC-GS-ROLE-233 | TC-GS-ROLE-E2E-087-cascade-remove-access-global-settings-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-234 | TC-GS-ROLE-E2E-087-cascade-remove-access-global-settings-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-235 | TC-GS-ROLE-E2E-088-cascade-user-dihapus-atau-dinonaktifkan | FE+BE |
| TC-GS-ROLE-236 | TC-GS-ROLE-E2E-088-cascade-user-dihapus-atau-dinonaktifkan | FE+BE |
| TC-GS-ROLE-237 | TC-GS-ROLE-E2E-089-sinkron-rename-position-dan-status-custom-field | FE+BE |
| TC-GS-ROLE-238 | TC-GS-ROLE-E2E-090-format-tanggal-general-settings-tab-dan-changelog | FE+BE |
| TC-GS-ROLE-239 | TC-GS-ROLE-E2E-090-format-tanggal-general-settings-tab-dan-changelog | FE+BE |
| TC-GS-ROLE-240 | TC-GS-ROLE-E2E-089-sinkron-rename-position-dan-status-custom-field | FE+BE |
| TC-GS-ROLE-241 | TC-GS-ROLE-E2E-091-notifikasi-in-app-remove-access-level-dan-assign-tanpa-notifikasi | FE+BE |
| TC-GS-ROLE-242 | TC-GS-ROLE-E2E-091-notifikasi-in-app-remove-access-level-dan-assign-tanpa-notifikasi | FE+BE |
| TC-GS-ROLE-243 | TC-GS-ROLE-E2E-092-notifikasi-in-app-auto-revert-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-244 | TC-GS-ROLE-E2E-092-notifikasi-in-app-auto-revert-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-245 | TC-GS-ROLE-E2E-092-notifikasi-in-app-auto-revert-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-246 | TC-GS-ROLE-E2E-093-tanpa-gating-plan-role-tampil-di-semua-plan | FE+BE |
| TC-GS-ROLE-247 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-248 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-249 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-250 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-251 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-252 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-253 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-254 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-255 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-256 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-257 | TC-GS-ROLE-E2E-098-defense-in-depth-edit-crud-remove-baris-dan-aksi-tulis-detail | FE+BE |
| TC-GS-ROLE-258 | TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403 | FE+BE |
| TC-GS-ROLE-259 | TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403 | FE+BE |
| TC-GS-ROLE-260 | TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403 | FE+BE |
| TC-GS-ROLE-261 | TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial | FE+BE |
| TC-GS-ROLE-262 | TC-GS-ROLE-E2E-101-isolasi-data-entitas-lain | FE+BE |
| TC-GS-ROLE-263 | TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level | FE+BE |
| TC-GS-ROLE-264 | TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level | FE+BE |
| TC-GS-ROLE-265 | TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level | FE+BE |
| TC-GS-ROLE-266 | TC-GS-ROLE-E2E-095-state-tenant-suspended-write-lockdown-access-level | FE+BE |
| TC-GS-ROLE-267 | TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail | FE+BE |
| TC-GS-ROLE-268 | TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail | FE+BE |
| TC-GS-ROLE-269 | TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail | FE+BE |
| TC-GS-ROLE-270 | TC-GS-ROLE-E2E-096-state-tenant-suspended-write-lockdown-detail | FE+BE |
| TC-GS-ROLE-271 | TC-GS-ROLE-E2E-097-state-tenant-suspended-tetap-dapat-melihat | FE+BE |
| TC-GS-ROLE-272 | TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus | FE+BE |
| TC-GS-ROLE-273 | TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus | FE+BE |
| TC-GS-ROLE-274 | TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control | FE+BE |
| TC-GS-ROLE-275 | TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda | FE+BE |
| TC-GS-ROLE-276 | TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control | FE+BE |
| TC-GS-ROLE-277 | TC-GS-ROLE-E2E-107-realtime-auto-revert-pada-tab-total-control-sesi-admin-lain | FE+BE |
| TC-GS-ROLE-278 | TC-GS-ROLE-E2E-102-default-user-tetap-total-control-setelah-semua-total-control-lain-di-remove | FE+BE |
| TC-GS-ROLE-279 | TC-GS-ROLE-E2E-033-konflik-assign-concurrent-user-sama-dua-admin | FE+BE |
| TC-GS-ROLE-280 | TC-GS-ROLE-E2E-033-konflik-assign-concurrent-user-sama-dua-admin | FE+BE |
| TC-GS-ROLE-281 | TC-GS-ROLE-E2E-003-screening-detail-role-kolom-crud-dinamis-dan-deskripsi-enam-role | FE+BE |
| TC-GS-ROLE-282 | TC-GS-ROLE-E2E-015-role-matrix-visibilitas-menu-sidebar-per-aktor | FE+BE |
| TC-GS-ROLE-283 | TC-GS-ROLE-E2E-094-isolasi-akses-produk-lain-assign-total-control | FE+BE |
| TC-GS-ROLE-284 | TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus | FE+BE |
| TC-GS-ROLE-285 | TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-286 | TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-287 | TC-GS-ROLE-E2E-014-mobile-card-list-tab-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-288 | TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | FE+BE |
| TC-GS-ROLE-289 | TC-GS-ROLE-E2E-080-pencatatan-system-log-aktor-dan-activity-log-access-level | FE+BE |
| TC-GS-ROLE-290 | TC-GS-ROLE-E2E-082-pencatatan-changelog-user-dan-changelog-user-role | FE+BE |
| TC-GS-ROLE-291 | TC-GS-ROLE-E2E-087-cascade-remove-access-global-settings-pada-tab-dan-detail | FE+BE |
| TC-GS-ROLE-292 | TC-GS-ROLE-E2E-030-konflik-assign-user-dihapus-atau-tidak-eligible-tunggal | FE+BE |
| TC-GS-ROLE-293 | TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility | FE+BE |
| TC-GS-ROLE-294 | TC-GS-ROLE-E2E-048-bulk-remove-satu-baris-dialog-single-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-295 | TC-GS-ROLE-E2E-048-bulk-remove-satu-baris-dialog-single-dan-klik-ganda | FE+BE |
| TC-GS-ROLE-296 | TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil | FE+BE |
| TC-GS-ROLE-297 | TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control | FE+BE |
| TC-GS-ROLE-298 | TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda | FE+BE |
| TC-GS-ROLE-299 | TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil | FE+BE |
| TC-GS-ROLE-300 | TC-GS-ROLE-E2E-031-konflik-assign-alert-jamak-user-dihapus | FE+BE |
| TC-GS-ROLE-301 | TC-GS-ROLE-E2E-032-konflik-assign-alert-jamak-user-tidak-eligible-dan-campuran | FE+BE |
| TC-GS-ROLE-302 | TC-GS-ROLE-E2E-032-konflik-assign-alert-jamak-user-tidak-eligible-dan-campuran | FE+BE |
| TC-GS-ROLE-303 | TC-GS-ROLE-E2E-061-download-tab-system-dan-detail-isi-file | FE+BE |
| TC-GS-ROLE-304 | TC-GS-ROLE-E2E-031-konflik-assign-alert-jamak-user-dihapus | FE+BE |
| TC-GS-ROLE-305 | TC-GS-ROLE-E2E-032-konflik-assign-alert-jamak-user-tidak-eligible-dan-campuran | FE+BE |
| TC-GS-ROLE-306 | TC-GS-ROLE-E2E-070-resilience-tulis-assign-total-control-read-only-dan-role | FE+BE |
| TC-GS-ROLE-307 | TC-GS-ROLE-E2E-029-assign-total-control-upgrade-read-only-dan-user-pending-email-confirmation | FE+BE |
| TC-GS-ROLE-308 | TC-GS-ROLE-E2E-100-defense-in-depth-payload-flag-bulk-dan-prioritas-403 | FE+BE |
| TC-GS-ROLE-309 | TC-GS-ROLE-E2E-073-resilience-tulis-bulk-remove-dan-sukses-parsial | FE+BE |
| TC-GS-ROLE-310 | TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | FE+BE |
| TC-GS-ROLE-311 | TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | FE+BE |
| TC-GS-ROLE-312 | TC-GS-ROLE-E2E-012-mobile-detail-selection-mode-header-import-data-toggle-dan-pagination | FE+BE |
| TC-GS-ROLE-313 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-314 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-315 | TC-GS-ROLE-E2E-099-defense-in-depth-access-level-dan-assign-ke-diri-sendiri | FE+BE |
| TC-GS-ROLE-316 | TC-GS-ROLE-E2E-025-popup-assign-pencarian-name-email-position-division-status-dan-no-result | FE+BE |
| TC-GS-ROLE-317 | TC-GS-ROLE-E2E-027-popup-assign-sort-pagination-dan-column-visibility | FE+BE |
