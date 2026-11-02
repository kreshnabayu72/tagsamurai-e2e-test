# Coverage E2E — Admin Console > Settings > User

Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md` (667 baris `TC-AC-SU-1`–`667`; 664 TC aktif, `TC-AC-SU-95`, `133`, dan `655` retired dan bertanda N/A). Suite: `specs/AdminConsole/SettingsUser/`. Prefix: `AC` + `SU` (`TC-AC-SU-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Berkas TC backend `tc-settings-user-backend.md` tidak menjadi sumber halaman ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 664 TC aktif masuk 209 spec (209 FE+BE, 0 mock), 0 TC hanya-BE. Setiap TC terpetakan ke satu spec (`sourceTc`), kecuali 9 TC yang terbelah antara dua spec (lihat "Pembagian TC lintas spec"). Spec 189–200 melengkapi pengelompokan tema pada spec 001–188 dan semuanya terpakai; spec 201–206 memuat TC yang dibagi dari spec 021, 090, 116, dan 143 pada batas TC, sehingga nomor 001–206 semuanya terpakai. Spec 207–209 memuat asersi absence Changelog kelas g (207) dan blok cascade tier Modal Changelog Global Role dan Group Role (208, 209).

## TC hanya-BE (tidak masuk spec)

Tidak ada. Seluruh 664 TC aktif memuat langkah dan Expected di UI atau respons server yang diamati dari sesi aktor, sehingga masuk spec.

## TC retired (tidak masuk spec)

Tiga baris bertanda **N/A, retired** di `tc-settings-user.md` (force logout tidak ada di Admin Console) dan tidak punya spec; dicatat di tabel ini sebagai TC yang tidak diotomasi:

| TC | Judul | Alasan |
|---|---|---|
| TC-AC-SU-95 | Klik `[Back to Login]` pada halaman pesan sesi berakhir | N/A, retired |
| TC-AC-SU-133 | Bulk Deactivate: force logout untuk target yang sedang login | N/A, retired |
| TC-AC-SU-655 | Deactivate gagal karena Auth gagal memutus sesi: rollback penuh | N/A, retired |

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-SU-E2E-001-screening-user-list-zona-urutan-default-dan-format-sel | Screening User List: Tiga Zona, Urutan Default Name, serta Format Sel Active dan Name | FE+BE | 35 | 1, 2, 4 |
| TC-AC-SU-E2E-002-nilai-kosong-modified-by-label-role-dan-modified-by-default-user | User List: Nilai Kosong Kolom, Format Modified By, Label Kolom Role, dan Modified By Default User | FE+BE | 26 | 5, 6, 8, 664 |
| TC-AC-SU-E2E-003-tooltip-toolbar-hover-baris-dan-klik-sel-selain-name | User List: Tooltip Ikon Toolbar, Hover Baris, dan Klik Sel Selain Name | FE+BE | 20 | 3, 13, 16 |
| TC-AC-SU-E2E-004-navigasi-ke-detail-loading-state-dan-no-result | User List: Navigasi ke Detail User, Loading State Tabel, dan No Result State Search | FE+BE | 22 | 14, 15, 17, 19 |
| TC-AC-SU-E2E-005-example-data-user-list-checkbox-switch-dan-kolom-role | Example Data User List: Checkbox, Switch Active, dan Kolom Role per Kondisi Status | FE+BE | 25 | 9 |
| TC-AC-SU-E2E-006-row-action-baris-default-user-dan-baris-self | User List: Row Action Baris Default User dan Baris Aktor Sendiri per Varian Status | FE+BE | 35 | 11, 12 |
| TC-AC-SU-E2E-007-popup-role-count | Popup Role Count: Screening, Tanpa Section Group Role, Penutupan, dan Role Switch OFF | FE+BE | 33 | 21–24 |
| TC-AC-SU-E2E-008-sidebar-group-user-list | Sidebar Group di User List: Screening, Filter Node beserta Descendant, Klik Ulang, dan Collapse | FE+BE | 31 | 25–28 |
| TC-AC-SU-E2E-009-guided-tooltip-user-list-step-next-back-dan-skip | Guided Tooltip User List: Step 1, Step 2 sampai 4 dan Done, Back, serta Skip via Tombol | FE+BE | 39 | 29–32 |
| TC-AC-SU-E2E-010-guided-tooltip-user-list-skip-overlay-replay-resize-dan-keyboard | Guided Tooltip User List: Skip via Overlay, Replay lewat [?], Penutupan karena Resize atau Navigasi, dan Navigasi Keyboard | FE+BE | 35 | 33–36 |
| TC-AC-SU-E2E-011-screening-detail-user-header-field-dan-avatar | Screening Detail User: Tiga Zona Header, Body, dan Avatar Read-only dengan atau tanpa Foto | FE+BE | 30 | 37, 40 |
| TC-AC-SU-E2E-012-screening-detail-user-user-type-temporary-until-dan-tag | Detail User: Badge User Type per Kondisi Role, Field Temporary Until, dan Field TAG | FE+BE | 40 | 42–45 |
| TC-AC-SU-E2E-013-detail-user-accordion-custom-field-label-tab-dan-state-tab | Detail User: Accordion Custom Field, Label Tab Responsibilities, State Tab, dan Breadcrumb Mempertahankan State List | FE+BE | 40 | 38, 46, 48, 49 |
| TC-AC-SU-E2E-014-entitas-baru-tanpa-user-lain-dan-tanpa-custom-field | Entitas Baru: Hanya Default User di User List dan Detail User tanpa Section Custom Field | FE+BE | 13 | 18, 47 |
| TC-AC-SU-E2E-015-aktor-default-user-tanpa-aksi-create-edit-delete | Aktor Default User: Tanpa Aksi Create, Edit, atau Delete serta Switch dan Checkbox Baris Default User Disabled | FE+BE | 25 | 50, 58, 114 |
| TC-AC-SU-E2E-016-role-matrix-menu-settings-user-dan-akses-langsung-per-aktor | Role Matrix: Menu Settings > User per Aktor, Akses Langsung via URL, dan Row Scope Seluruh User Entitas | FE+BE | 42 | 51–53, 55 |
| TC-AC-SU-E2E-017-entitas-distributor-isolasi-data-dan-baris-global-role | Entitas Distributor: Isolasi Data User Antar Entitas dan Baris Global Role Manage TAG Stock serta Manage Hardware Stock | FE+BE | 16 | 54, 192 |
| TC-AC-SU-E2E-018-role-matrix-switch-active-manage-user-and-role-dan-total-control | Role Matrix: Switch Active per Target untuk Aktor Manage user and role (Update) dan Total Control | FE+BE | 34 | 56, 57, 99 |
| TC-AC-SU-E2E-019-role-matrix-switch-active-read-only-manage-user-and-role-tanpa-update | Role Matrix: Switch Active untuk Aktor Read Only dan Manage user and role, Switch Header Detail, serta Prioritas Tooltip | FE+BE | 41 | 59–61, 79 |
| TC-AC-SU-E2E-020-switch-active-disabled-prioritas-tooltip-dan-target-nonaktif-global-settings | Switch Active Disabled: Tooltip Self pada Detail, Baris Default User, dan Target Nonaktif di Global Settings | FE+BE | 28 | 77, 98, 100, 101 |
| TC-AC-SU-E2E-021-role-matrix-tab-role-global-role-per-aktor-dan-target | Role Matrix: Tab Role Global Role, Aktor Manage user and role (Update) per Target | FE+BE | 28 | 62 |
| TC-AC-SU-E2E-022-role-matrix-group-role-target-group-manager-dan-sidebar-tanpa-restriksi | Role Matrix: Group Role Target Group Manager untuk Manage user and role dan Total Control serta Sidebar Group tanpa Restriksi Node | FE+BE | 37 | 66, 67, 78 |
| TC-AC-SU-E2E-023-role-matrix-assign-group-hidden-disabled-enabled | Role Matrix: Assign Group Hidden untuk Default User dan Self, Disabled untuk Target Total Control atau Read Only, serta Enabled pada Role tanpa Group | FE+BE | 40 | 68–70 |
| TC-AC-SU-E2E-024-role-matrix-resend-email-row-action-per-aktor | Role Matrix: Row Action Resend Activation Email dan Resend Confirmation Email per Aktor | FE+BE | 54 | 71, 72, 140, 152, 153 |
| TC-AC-SU-E2E-025-role-matrix-kolom-checkbox-dan-bulk-action-bar-per-aktor | Role Matrix: Kolom Checkbox dan Bulk Action Bar per Aktor | FE+BE | 34 | 73, 74, 136, 137 |
| TC-AC-SU-E2E-026-aktor-read-only-kontrol-baca-tabel-dan-tab-detail | Aktor Read Only: Kontrol Baca Tabel, Seluruh Tab Detail User, Tab Responsibilities, Tab Changelog, dan Prioritas Tooltip | FE+BE | 45 | 75, 76, 80, 367, 403 |
| TC-AC-SU-E2E-027-deactivate-single-via-switch-user-list-dialog-dan-hasil | Deactivate Single via Switch User List: Dialog Konfirmasi, Cancel, Penutupan, dan Hasil Confirm | FE+BE | 43 | 81–86 |
| TC-AC-SU-E2E-028-activate-single-via-switch-user-list-dan-pending-activation | Activate Single via Switch User List: Dialog, Cancel, Confirm, Aktivasi Ulang, dan Switch Pending Activation | FE+BE | 39 | 87–89, 96, 97 |
| TC-AC-SU-E2E-029-activate-deactivate-dari-switch-header-detail-user | Activate dan Deactivate dari Switch Header Detail User: Dialog, Toast, Label, Badge, dan Sinkron ke User List | FE+BE | 21 | 90, 91 |
| TC-AC-SU-E2E-030-bulk-action-bar-screening-counter-dan-overlay-bulk-action | Bulk Action Bar: Screening, Overlay Bulk Action per Komposisi Seleksi, dan Counter Realtime | FE+BE | 33 | 105–109 |
| TC-AC-SU-E2E-031-seleksi-checkbox-header-select-all-unselect-dan-uncheck-baris | Seleksi Checkbox: Checkbox Header, Select All Lintas Halaman, Unselect All, dan Uncheck Satu Baris | FE+BE | 30 | 110–112 |
| TC-AC-SU-E2E-032-seleksi-bertahan-saat-pindah-halaman-search-filter-dan-sort | Seleksi Checkbox Bertahan saat Pindah Halaman, Search, Filter, dan Sort | FE+BE | 25 | 134, 326, 327 |
| TC-AC-SU-E2E-033-selection-limit-lifecycle-settings | Selection Limit: Live-block Checkbox ke-(Limit+1) dan Select All yang Melebihi Limit di-cap Otomatis | FE+BE | 20 | 115, 116 |
| TC-AC-SU-E2E-034-bulk-activate-deactivate-seleksi-eligible-cancel-dan-confirm | Bulk Activate dan Bulk Deactivate: Seleksi Semua Eligible, Dialog, Cancel Mempertahankan Seleksi, dan Confirm | FE+BE | 29 | 117–121 |
| TC-AC-SU-E2E-035-bulk-activate-deactivate-seleksi-campuran-dan-collapse-dialog-single | Bulk Activate dan Bulk Deactivate: Dialog Dua Kelompok untuk Seleksi Campuran, Skipped, dan Collapse ke Dialog Single | FE+BE | 32 | 122, 124, 126–128 |
| TC-AC-SU-E2E-036-bulk-activate-deactivate-satu-eligible-tanpa-eligible-dan-toast-partial | Bulk Activate dan Bulk Deactivate: Satu Baris Eligible, Tanpa Baris Eligible (Dialog Blok), dan Toast Partial | FE+BE | 33 | 123, 129, 652 |
| TC-AC-SU-E2E-037-bulk-oleh-manage-user-and-role-default-user-self-target-tier-dan-log-partial | Bulk oleh Manage user and role (Update): Default User dan Self Dikecualikan, Target Total Control atau Read Only Skipped, dan Log Partial | FE+BE | 47 | 113, 125, 576, 651 |
| TC-AC-SU-E2E-038-resend-visibilitas-row-action-dan-overlay-bulk | Resend Email: Visibilitas Row Action dan Overlay Bulk Action | FE+BE | 31 | 138, 139, 141, 155, 159 |
| TC-AC-SU-E2E-039-resend-activation-email-row-action-dan-cooldown | Resend Activation Email: Row Action dan Cooldown 60 Detik | FE+BE | 31 | 142, 146–148 |
| TC-AC-SU-E2E-040-resend-confirmation-email-row-action-dan-header-detail | Resend Email: Row Action Confirmation dan Tombol Header Detail User | FE+BE | 19 | 143–145 |
| TC-AC-SU-E2E-041-bulk-resend-sukses-cooldown-dan-semua-cooldown | Bulk Resend Activation Email: Sukses, Sebagian Cooldown, dan Semua Cooldown | FE+BE | 19 | 154, 156, 157 |
| TC-AC-SU-E2E-042-entitas-suspended-tampilan-kontrol | Entitas Suspended: Tampilan Kontrol Tulis di User List dan Detail User | FE+BE | 43 | 161–164, 191, 212 |
| TC-AC-SU-E2E-043-entitas-suspended-transisi-dan-request-langsung | Entitas Suspended: Transisi Suspend/Unsuspend dan Request Tulis Langsung | FE+BE | 38 | 165–169 |
| TC-AC-SU-E2E-044-entitas-suspended-transisi-dan-request-langsung-bagian-2 | Entitas Suspended: Sesi Aktor MUR Distributor, Pemulihan Otomatis, dan Request Activate Langsung | FE+BE | 31 | 603, 604, 623 |
| TC-AC-SU-E2E-045-sub-tab-global-role-screening-toolbar-dan-sort | Sub-tab Global Role: Screening, Tooltip Changelog, dan Header Tidak Bisa Di-sort | FE+BE | 26 | 170–172 |
| TC-AC-SU-E2E-046-sub-tab-global-role-guard-checkbox-dan-dimensi-tidak-applicable | Sub-tab Global Role: Checkbox Terkunci, Read Mandatory, dan Dimensi Tidak Applicable | FE+BE | 16 | 176, 179, 180 |
| TC-AC-SU-E2E-047-sub-tab-global-role-switch-dan-autosave-crud | Sub-tab Global Role: Switch dan Autosave CRUD | FE+BE | 30 | 173–175, 177, 178 |
| TC-AC-SU-E2E-048-sub-tab-global-role-baris-default-user-dan-self-terkunci | Sub-tab Global Role: Detail Default User dan Akun Sendiri Terkunci | FE+BE | 24 | 183, 184 |
| TC-AC-SU-E2E-049-sub-tab-global-role-aktor-manage-user-and-role-per-target | Sub-tab Global Role: Aktor Manage user and role per Target (Total Control, Read Only, Standar, Group Manager) | FE+BE | 43 | 185–188, 190 |
| TC-AC-SU-E2E-050-sub-tab-global-role-aktor-read-only | Sub-tab Global Role: Aktor Read Only Melihat Kontrol Disabled | FE+BE | 8 | 189 |
| TC-AC-SU-E2E-051-sub-tab-group-role-screening-dan-sort-group | Sub-tab Group Role: Screening Kolom dan Sort Kolom Group | FE+BE | 24 | 194, 666 |
| TC-AC-SU-E2E-052-sub-tab-group-role-sort-role-name-dan-badge-group | Sub-tab Group Role: Sort Role Name dan Group Summary Badge | FE+BE | 23 | 195–197 |
| TC-AC-SU-E2E-053-sub-tab-group-role-all-groups-empty-state-dan-kolom | Sub-tab Group Role: All Groups, Role Tanpa Group, dan Kolom Tanpa Switch | FE+BE | 30 | 198–200, 645 |
| TC-AC-SU-E2E-054-sub-tab-group-role-baris-default-user-self-dan-tanpa-assignment | Sub-tab Group Role: Default User, Akun Sendiri, dan Group Role Tanpa Group Assignment | FE+BE | 31 | 205–207, 633 |
| TC-AC-SU-E2E-055-assign-group-role-tanpa-group-popup-awal-tutup-dan-leave | Assign Group pada Role Tanpa Group: Popup Awal, Tutup Bersih, dan Tutup Dirty | FE+BE | 23 | 201, 203, 204 |
| TC-AC-SU-E2E-056-assign-group-role-tanpa-group-save-satu-group-dan-log-assign | Assign Group pada Role Tanpa Group: Save Satu Group dan Changelog Assign | FE+BE | 15 | 202 |
| TC-AC-SU-E2E-057-role-matrix-sub-tab-group-role-per-aktor | Role Matrix: Sub-tab Group Role dan Global Role per Aktor (MUR, Read Only, MUR Tanpa Update) | FE+BE | 35 | 208, 210, 211, 261 |
| TC-AC-SU-E2E-058-manage-user-and-role-pada-target-group-manager-popup-terkunci | Aktor Manage user and role pada Target Group Manager: Baris Group GM Terkunci di Popup | FE+BE | 40 | 209, 242, 243 |
| TC-AC-SU-E2E-059-manage-user-and-role-memberi-group-role-dan-mengedit-baris-non-gm | Aktor Manage user and role: Memberi Group Role Target Standar dan Mengedit Baris Non-GM | FE+BE | 20 | 213, 244 |
| TC-AC-SU-E2E-060-popup-assign-group-role-screening-search-dan-select-group | Popup Assign Group Role: Screening, Search Group, dan Popup Select Group | FE+BE | 34 | 214–217 |
| TC-AC-SU-E2E-061-popup-assign-group-role-select-group-cancel-search-dan-semua-ter-assign | Popup Assign Group Role: Select Group Menambah Baris, Cancel, Search Tree, dan Semua Node Ter-assign | FE+BE | 36 | 218–221 |
| TC-AC-SU-E2E-062-popup-assign-group-role-edit-tambah-remove-dan-save | Popup Assign Group Role: Edit CRUD, Tambah Group, Remove Pending, dan Remove Lalu Add Ulang | FE+BE | 40 | 222–225 |
| TC-AC-SU-E2E-063-popup-assign-group-role-save-no-op-clear-field-dan-save-kosong | Popup Assign Group Role: Save Tanpa Perubahan, Clear Field, dan Save Tabel Kosong | FE+BE | 34 | 226–228 |
| TC-AC-SU-E2E-064-popup-assign-group-role-penolakan-server-dan-baris-stale | Popup Assign Group Role: Penolakan Server atas Group Ter-assign dan Group yang Sudah Dihapus | FE+BE | 38 | 230, 660 |
| TC-AC-SU-E2E-065-popup-assign-group-role-tutup-dirty-dan-saving-state | Popup Assign Group Role: Tutup Bersih dan Dirty, serta Saving State Tombol Save | FE+BE | 36 | 232–235 |
| TC-AC-SU-E2E-066-popup-assign-group-role-perubahan-dikembalikan-backdrop-dan-accessibility | Popup Assign Group Role: Perubahan Dikembalikan, Backdrop Tidak Menutup, dan Accessibility | FE+BE | 27 | 236, 237, 241 |
| TC-AC-SU-E2E-067-popup-assign-group-role-reload-dan-navigasi-saat-dirty | Popup Assign Group Role: Reload dan Navigasi Back saat Dirty | FE+BE | 23 | 238–240 |
| TC-AC-SU-E2E-068-detail-group-assignment-screening-search-dan-download | Detail Group Assignment: Screening Read Only, Interaksi Checkbox, serta Search dan Download | FE+BE | 39 | 245–247 |
| TC-AC-SU-E2E-069-detail-group-assignment-nama-file-dan-sort-group | Detail Group Assignment: Nama Berkas Download Dinormalisasi dan Sort Kolom Group | FE+BE | 14 | 657, 662 |
| TC-AC-SU-E2E-070-auto-revert-total-control-aktor-default-user | Auto-Revert Total Control: Dialog, Cancel, Tutup, dan Confirm oleh Default User | FE+BE | 24 | 249–252 |
| TC-AC-SU-E2E-071-auto-revert-total-control-dan-read-only-aktor-total-control | Auto-Revert Total Control dan Read Only: Pemicu Checkbox, Switch, dan Save Popup oleh Total Control | FE+BE | 38 | 253–256 |
| TC-AC-SU-E2E-072-auto-revert-group-manager-dialog-cancel-dan-confirm | Auto-Revert Group Manager: Dialog Save Popup, Cancel, dan Confirm Melepas Status Satu Group | FE+BE | 28 | 257–259 |
| TC-AC-SU-E2E-073-auto-revert-group-manager-lebih-dari-satu-group | Auto-Revert Group Manager: Save 0 Group dan Unassign Group Penopang GM | FE+BE | 29 | 260, 644 |
| TC-AC-SU-E2E-074-user-list-search-siklus-box-dan-kelas-teks | User List Search: Siklus Interaksi Search Box dan Search Kelas Teks | FE+BE | 31 | 263, 264 |
| TC-AC-SU-E2E-075-user-list-search-role-badge-modified-by-dan-trim | User List Search: Kolom Role, Badge, Modified By, Custom Field, dan Trim Query | FE+BE | 48 | 265–268, 271 |
| TC-AC-SU-E2E-076-user-list-search-kolom-hidden-non-searchable-dan-status | User List Search: Kolom Hidden, Kolom Non-Searchable, Status Active/Inactive, dan Custom Field Date | FE+BE | 39 | 269, 270, 648, 659 |
| TC-AC-SU-E2E-077-user-list-filter-panel-screening-dan-isi-opsi | User List Filter Panel: Screening dan Isi Opsi Dropdown dari Data Tabel | FE+BE | 16 | 272, 273 |
| TC-AC-SU-E2E-078-user-list-filter-panel-role-date-range-or-and-chip | User List Filter Panel: Role, Date Range, OR dan AND, Hapus Chip, dan Activation Status | FE+BE | 48 | 275–278, 649 |
| TC-AC-SU-E2E-079-user-list-filter-panel-uncheck-search-dropdown-dan-clear | User List Filter Panel: Uncheck di Dropdown, Search Dropdown, Clear Field, dan Custom Field Dropdown | FE+BE | 29 | 279–282 |
| TC-AC-SU-E2E-080-user-list-sidebar-group-digabung-search-dan-filter | User List Sidebar Group: Filter Node Beserta Descendant, Digabung dengan Search dan Filter, dan Collapse Persisten | FE+BE | 31 | 283–285 |
| TC-AC-SU-E2E-081-user-list-kombinasi-search-filter-sort-bagian-1 | User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 1) | FE+BE | 43 | 286–289 |
| TC-AC-SU-E2E-082-user-list-kombinasi-search-filter-sort-bagian-2 | User List Kombinasi Search, Filter, Sort, dan Page Size (bagian 2) | FE+BE | 43 | 290–293 |
| TC-AC-SU-E2E-083-user-list-sort-role-active-tanggal-dan-tie-breaker | User List Sort: Kolom Role, Active, Kelas Tanggal, dan Tie-Breaker Nilai Sama | FE+BE | 35 | 295–297, 656 |
| TC-AC-SU-E2E-084-user-list-sort-badge-modified-by-custom-field-dan-guard | User List Sort: Kolom Badge, Modified By, Custom Field Text, dan Guard Kolom Tanpa Sort | FE+BE | 35 | 298–302 |
| TC-AC-SU-E2E-085-user-list-column-visibility-dan-setup-column-default-visible | User List Column Visibility dan Setup Column: Kolom Default Visible | FE+BE | 52 | 303–307 |
| TC-AC-SU-E2E-086-user-list-setup-column-kolom-curated-hidden | User List Setup Column: Kolom Curated Hidden (Ceklis, Drag Reorder, Pin dan Unpin) | FE+BE | 36 | 308–310 |
| TC-AC-SU-E2E-087-user-list-setup-column-guard-reset-discard-dan-cache | User List Setup Column: Guard Satu Kolom, Reset to Default, Discard, dan Independensi Cache dengan Modal Changelog | FE+BE | 36 | 311–314 |
| TC-AC-SU-E2E-088-user-list-download-csv-xlsx-dan-konteks | User List Download: Overlay, CSV, XLSX dengan Search, Filter, Node Sidebar Group, dan Kolom Tampil | FE+BE | 35 | 315–318, 661 |
| TC-AC-SU-E2E-089-user-list-download-isi-berkas-per-tipe-kolom | User List Download: Isi Berkas XLSX (Nilai Sel per Tipe Kolom dan Keanggotaan Baris, Binary Buffer) | FE+BE | 30 | 317, 319, 661 |
| TC-AC-SU-E2E-090-user-list-pagination-dan-retensi-state | User List Pagination: Navigasi Halaman dan Reset Halaman saat Search atau Filter Berubah | FE+BE | 27 | 321, 322 |
| TC-AC-SU-E2E-091-perubahan-custom-field-global-settings-terhadap-user-list-bagian-1 | Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 1) | FE+BE | 61 | 328–330, 608, 667 |
| TC-AC-SU-E2E-092-perubahan-custom-field-global-settings-terhadap-user-list-bagian-2 | Perubahan Custom Field di Global Settings terhadap User List dan Detail User (bagian 2) | FE+BE | 67 | 609–613 |
| TC-AC-SU-E2E-093-tab-responsibilities-screening-state-dan-display-only | Tab Responsibilities: Screening, Sort Default, Display-Only, Search Kosong, Loading, dan Label 0 Pending Approvals | FE+BE | 35 | 331–334, 336, 337 |
| TC-AC-SU-E2E-094-tab-responsibilities-sort-3-state | Tab Responsibilities: Sort 3-State Kelas Teks dan Kelas Tanggal | FE+BE | 16 | 338, 339 |
| TC-AC-SU-E2E-095-tab-responsibilities-search-bagian-1 | Tab Responsibilities Search: Siklus Interaksi Search Box dan Search Kelas Teks dan Badge | FE+BE | 33 | 340–342 |
| TC-AC-SU-E2E-096-tab-responsibilities-search-bagian-2 | Tab Responsibilities Search: Kolom Non-Searchable, Trim Query, dan Kolom Hidden | FE+BE | 27 | 343–345 |
| TC-AC-SU-E2E-097-tab-responsibilities-filter-panel-bagian-1 | Tab Responsibilities Filter Panel: Screening, Isi Opsi, Satu Opsi per Field, Date Range, dan Requester Kosong | FE+BE | 37 | 346–349, 658 |
| TC-AC-SU-E2E-098-tab-responsibilities-filter-panel-bagian-2 | Tab Responsibilities Filter Panel: OR dan AND, Chip Opsi, dan Uncheck di Dropdown | FE+BE | 35 | 350–352 |
| TC-AC-SU-E2E-099-tab-responsibilities-filter-panel-bagian-3 | Tab Responsibilities Filter Panel: Search di Dropdown, Search lalu Filter, dan Filter lalu Search | FE+BE | 33 | 353–355 |
| TC-AC-SU-E2E-100-tab-responsibilities-column-visibility-dan-setup-column-bagian-1 | Tab Responsibilities Column Visibility dan Setup Column: Screening, Ceklis, dan Drag Reorder | FE+BE | 43 | 356–359 |
| TC-AC-SU-E2E-101-tab-responsibilities-column-visibility-dan-setup-column-bagian-2 | Tab Responsibilities Column Visibility dan Setup Column: Pin, Reset to Default, Discard, dan Guard Satu Kolom | FE+BE | 44 | 360–363 |
| TC-AC-SU-E2E-102-tab-responsibilities-download | Tab Responsibilities Download: CSV Seluruh Baris dan XLSX dengan Search dan Filter Aktif | FE+BE | 21 | 364, 365 |
| TC-AC-SU-E2E-103-tab-changelog-screening-dan-state | Tab Changelog: Screening, Search Kosong, Tie-breaker Auto-Revert, Loading, dan Empty State | FE+BE | 32 | 368–371, 373, 377 |
| TC-AC-SU-E2E-104-tab-changelog-sort | Tab Changelog: Sort 3-state Kelas Teks, Campuran, dan Tanggal | FE+BE | 27 | 374–376 |
| TC-AC-SU-E2E-105-tab-changelog-search-siklus-dan-per-kolom | Tab Changelog: Siklus Search Box dan Search per Kolom Teks | FE+BE | 31 | 378, 379 |
| TC-AC-SU-E2E-106-tab-changelog-search-kolom-non-searchable-dan-hidden | Tab Changelog: Search Kolom Non-searchable dan Kolom Hidden | FE+BE | 19 | 380, 381 |
| TC-AC-SU-E2E-107-tab-changelog-filter-panel-screening-opsi-dan-satu-opsi | Tab Changelog: Filter Panel (Screening, Isi Opsi, Satu Opsi per Field, Date Inklusif) | FE+BE | 36 | 382–385 |
| TC-AC-SU-E2E-108-tab-changelog-filter-panel-kombinasi-chip-dan-uncheck | Tab Changelog: Filter Panel (Kombinasi OR/AND, Chip, dan Uncheck Opsi) | FE+BE | 39 | 386–388 |
| TC-AC-SU-E2E-109-tab-changelog-filter-panel-search-dropdown-dan-irisan | Tab Changelog: Search dalam Dropdown Filter dan Irisan Search dengan Filter | FE+BE | 32 | 389–391 |
| TC-AC-SU-E2E-110-tab-changelog-column-visibility-dan-setup-column-bagian-1 | Tab Changelog: Column Visibility dan Setup Column (Screening, Toggle Kolom, Reorder) | FE+BE | 43 | 392–395 |
| TC-AC-SU-E2E-111-tab-changelog-column-visibility-dan-setup-column-bagian-2 | Tab Changelog: Setup Column (Pin, Reset to Default, Tutup tanpa Save, Satu Kolom Tersisa) | FE+BE | 47 | 396–399 |
| TC-AC-SU-E2E-112-tab-changelog-download-csv | Tab Changelog: Download CSV tanpa Search atau Filter | FE+BE | 13 | 400 |
| TC-AC-SU-E2E-113-tab-system-log-screening-dan-state | Tab System Log: Screening, Search Kosong, Loading, Hover Snapshot Group, dan Empty State | FE+BE | 38 | 404–406, 408, 654 |
| TC-AC-SU-E2E-114-tab-system-log-sort | Tab System Log: Sort 3-state Kolom Tanggal dan Kolom Teks | FE+BE | 24 | 409, 410 |
| TC-AC-SU-E2E-115-tab-system-log-search-siklus-dan-kolom-non-searchable | Tab System Log: Siklus Search Box dan Kolom Non-searchable | FE+BE | 32 | 411, 413 |
| TC-AC-SU-E2E-116-tab-system-log-filter-panel-screening-opsi-dan-kombinasi | Tab System Log: Filter Panel (Screening dan Isi Opsi Dropdown) | FE+BE | 18 | 414, 415 |
| TC-AC-SU-E2E-117-tab-system-log-filter-panel-chip-uncheck-dan-date-range | Tab System Log: Filter Panel (Chip, Uncheck Opsi, dan Date Range Inklusif) | FE+BE | 36 | 418, 419, 653 |
| TC-AC-SU-E2E-118-tab-system-log-search-dan-filter-irisan | Tab System Log: Irisan Search dengan Filter | FE+BE | 23 | 420, 421 |
| TC-AC-SU-E2E-119-tab-system-log-download-csv | Tab System Log: Download CSV tanpa Search atau Filter | FE+BE | 13 | 422 |
| TC-AC-SU-E2E-120-tab-user-log-screening-dan-state | Tab User Log: Screening, Isolasi Sesi, Search Kosong, Loading, dan Empty State | FE+BE | 30 | 425–429, 431 |
| TC-AC-SU-E2E-121-tab-user-log-sort | Tab User Log: Sort 3-state Kolom Tanggal dan Kolom Teks | FE+BE | 34 | 432, 433 |
| TC-AC-SU-E2E-122-tab-user-log-search-siklus-dan-per-kolom | Tab User Log: Siklus Search Box dan Search per Kolom Teks | FE+BE | 31 | 434, 435 |
| TC-AC-SU-E2E-123-tab-user-log-filter-panel-dan-date-range | Tab User Log: Filter Panel Hanya Field Date dan Date Range Inklusif | FE+BE | 15 | 436, 437 |
| TC-AC-SU-E2E-124-tab-user-log-download-csv | Tab User Log: Download CSV tanpa Search atau Filter | FE+BE | 13 | 438 |
| TC-AC-SU-E2E-125-detail-user-pagination-dan-retensi-state-lintas-tab | Detail User: Pagination Empat Tab dan Retensi Search atau Filter Lintas Tab | FE+BE | 30 | 441, 442 |
| TC-AC-SU-E2E-126-modal-changelog-user-screening-isi-dan-state | Modal Changelog User: Screening, Isi Lintas User, Loading, Empty Search, dan Empty State | FE+BE | 25 | 443–446, 448 |
| TC-AC-SU-E2E-127-modal-changelog-user-sort-tiga-state | Modal Changelog User: Sort 3-State Kelas Teks, Campuran, dan Tanggal | FE+BE | 25 | 449–451 |
| TC-AC-SU-E2E-128-modal-changelog-user-search-siklus-dan-per-kolom | Modal Changelog User: Siklus Search Box dan Search per Kolom Kelas Teks | FE+BE | 30 | 452, 453 |
| TC-AC-SU-E2E-129-modal-changelog-user-search-kolom-non-searchable-dan-hide | Modal Changelog User: Search atas Kolom Non-Searchable dan Kolom yang Di-hide | FE+BE | 17 | 454, 455 |
| TC-AC-SU-E2E-130-modal-changelog-user-filter-screening-dan-isi-opsi | Modal Changelog User: Screening Filter Panel dan Isi Opsi Dropdown Filter | FE+BE | 21 | 456, 457 |
| TC-AC-SU-E2E-131-modal-changelog-user-filter-user-sudah-dicabut-satu-opsi-dan-rentang-date | Modal Changelog User: Filter User Name Akses Dicabut, Satu Opsi per Field, dan Rentang Date | FE+BE | 24 | 458–460 |
| TC-AC-SU-E2E-132-modal-changelog-user-filter-or-and-chip-dan-uncheck | Modal Changelog User: Filter OR dalam Field, AND antar Field, Chip, dan Uncheck Opsi | FE+BE | 34 | 461–463 |
| TC-AC-SU-E2E-133-modal-changelog-user-filter-search-dropdown-dan-irisan-search-filter | Modal Changelog User: Search di Dropdown Filter serta Irisan Search dan Filter | FE+BE | 28 | 464–466 |
| TC-AC-SU-E2E-134-modal-changelog-user-column-visibility-screening-popup-dan-toggle-kolom | Modal Changelog User: Screening Column Visibility, Popup Setup Column, dan Toggle Kolom | FE+BE | 33 | 467–469 |
| TC-AC-SU-E2E-135-modal-changelog-user-setup-column-drag-pin-dan-reset | Modal Changelog User: Setup Column Drag Reorder, Pin, dan Reset to Default | FE+BE | 41 | 470–472 |
| TC-AC-SU-E2E-136-modal-changelog-user-setup-column-tutup-tanpa-save-dan-kolom-minimal | Modal Changelog User: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa | FE+BE | 19 | 473, 474 |
| TC-AC-SU-E2E-137-modal-changelog-user-download-csv-dan-pagination | Modal Changelog User: Download CSV tanpa Search dan Filter serta Pagination | FE+BE | 25 | 476, 479 |
| TC-AC-SU-E2E-138-modal-changelog-global-role-screening-isi-dan-state | Modal Changelog Global Role: Screening, Cakupan Entri, Search Kosong, Loading, dan Empty State | FE+BE | 29 | 480–482, 484, 504 |
| TC-AC-SU-E2E-139-modal-changelog-global-role-sort-tiga-state | Modal Changelog Global Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal | FE+BE | 30 | 485–487 |
| TC-AC-SU-E2E-140-modal-changelog-global-role-search-siklus-per-kolom-dan-non-searchable | Modal Changelog Global Role: Search Box, Search per Kolom, dan Kolom Non-Searchable | FE+BE | 37 | 488–490 |
| TC-AC-SU-E2E-141-modal-changelog-global-role-filter-panel | Modal Changelog Global Role: Screening Filter Panel, Satu Opsi per Field, Rentang Date, dan OR/AND | FE+BE | 36 | 491–494 |
| TC-AC-SU-E2E-142-modal-changelog-global-role-column-visibility-popup-toggle-dan-drag | Modal Changelog Global Role: Column Visibility, Popup Setup Column, Toggle Kolom, dan Drag Reorder | FE+BE | 46 | 495–498 |
| TC-AC-SU-E2E-143-modal-changelog-global-role-setup-column-pin-reset-tutup-dan-kolom-minimal | Modal Changelog Global Role: Setup Column Pin dan Reset to Default | FE+BE | 32 | 499, 500 |
| TC-AC-SU-E2E-144-modal-changelog-global-role-pagination-dan-download-csv | Modal Changelog Global Role: Pagination dan Download CSV | FE+BE | 11 | 503, 646 |
| TC-AC-SU-E2E-145-modal-changelog-group-role-screening-search-kosong-loading-dan-empty-state | Modal Changelog Group Role: Screening, Search Kosong, Loading, dan Empty State | FE+BE | 25 | 505, 506, 508, 530 |
| TC-AC-SU-E2E-146-modal-changelog-group-role-sort-tiga-state | Modal Changelog Group Role: Sort 3-State Kelas Teks, Campuran, dan Tanggal | FE+BE | 30 | 509–511 |
| TC-AC-SU-E2E-147-modal-changelog-group-role-search-siklus-interaksi-search-box | Modal Changelog Group Role: Siklus Interaksi Search Box | FE+BE | 25 | 512 |
| TC-AC-SU-E2E-148-modal-changelog-group-role-search-per-kolom-dan-non-searchable | Modal Changelog Group Role: Search per Kolom Kelas Teks dan Kolom Non-Searchable | FE+BE | 14 | 513, 514 |
| TC-AC-SU-E2E-149-modal-changelog-group-role-filter-panel-dua-field-and-dan-satu-opsi | Modal Changelog Group Role: Filter Panel Role Name dan Group Name, AND, Satu Opsi per Field, dan Rentang Date | FE+BE | 33 | 515–518 |
| TC-AC-SU-E2E-150-modal-changelog-group-role-filter-chip-dan-uncheck-group-name | Modal Changelog Group Role: Filter Chip Opsi Group Name dan Hapus Opsi lewat Uncheck | FE+BE | 25 | 519, 520 |
| TC-AC-SU-E2E-151-modal-changelog-group-role-column-visibility-popup-dan-toggle-kolom | Modal Changelog Group Role: Column Visibility, Popup Setup Column, dan Toggle Kolom | FE+BE | 36 | 521–523 |
| TC-AC-SU-E2E-152-modal-changelog-group-role-setup-column-drag-pin-dan-reset | Modal Changelog Group Role: Setup Column Drag Reorder, Pin, dan Reset to Default | FE+BE | 42 | 524–526 |
| TC-AC-SU-E2E-153-modal-changelog-group-role-setup-column-tutup-tanpa-save-dan-kolom-minimal | Modal Changelog Group Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa | FE+BE | 20 | 527, 528 |
| TC-AC-SU-E2E-154-modal-changelog-group-role-pagination | Modal Changelog Group Role: Pagination | FE+BE | 5 | 529 |
| TC-AC-SU-E2E-155-changelog-user-aksi-status-dan-resend | Popup Changelog: User dan Tab Changelog Detail Mencatat Aksi Activate, Deactivate, Resend Activation Email, dan Resend Confirmation Email dari Settings > User | FE+BE | 37 | 531–534 |
| TC-AC-SU-E2E-156-changelog-user-aksi-global-role | Popup Changelog User Mencatat Aksi Assign, Remove, dan Edit Permission Global Role dari Settings > User | FE+BE | 33 | 535–537 |
| TC-AC-SU-E2E-157-changelog-user-aksi-group-role | Popup Changelog User Mencatat Aksi Assign, Edit Permission, dan Remove Group Role per Group dari Settings > User | FE+BE | 37 | 538–540 |
| TC-AC-SU-E2E-158-changelog-user-tier-total-control-dan-read-only-dari-role-permission | Popup Changelog User Mencatat Assign dan Remove Total Control serta Assign Read Only yang Dipicu dari Settings > Role & Permission | FE+BE | 21 | 541–543 |
| TC-AC-SU-E2E-159-changelog-user-tier-read-only-dan-group-manager-dari-role-permission | Popup Changelog User Mencatat Remove Read Only serta Assign dan Remove Group Manager yang Dipicu dari Settings > Role & Permission | FE+BE | 21 | 544, 545, 650 |
| TC-AC-SU-E2E-160-changelog-user-auto-revert-dengan-tie-breaker | Popup Changelog User Mencatat Pasangan Edit dan Auto-Revert Total Control, Read Only, dan Group Manager dengan Urutan Tie-Breaker | FE+BE | 38 | 547–549 |
| TC-AC-SU-E2E-161-pelepasan-group-manager-akibat-delete-group | Hapus Group di Settings > Group Dicatat sebagai Remove (Group Deleted), Dicatat di Tab System Log dan Activity Log, dan Memperbarui Banner Group Manager tanpa Notifikasi | FE+BE | 23 | 546, 602, 640 |
| TC-AC-SU-E2E-162-modal-changelog-global-role-mencatat-aksi | Modal Changelog User > Global Role Mencatat Assign, Remove, dan Edit | FE+BE | 18 | 550–552 |
| TC-AC-SU-E2E-163-modal-changelog-group-role-mencatat-aksi | Modal Changelog User > Group Role Mencatat Assign, Edit, dan Remove per Group | FE+BE | 18 | 557–559 |
| TC-AC-SU-E2E-164-pencatatan-edge-snapshot-dua-permission-save-tanpa-perubahan-dan-save-nol-group | Pencatatan Edge Changelog User, Snapshot Entri Lama, Dua Permission Sekaligus, Save Popup Assign Group Role tanpa Perubahan, dan Save 0 Group | FE+BE | 34 | 564, 572–574 |
| TC-AC-SU-E2E-165-resend-dan-bulk-resend-entri-log-changelog | Resend Activation Email Menulis Entri Changelog di Background dan Bulk Resend Hanya Mencatat Baris yang Diproses | FE+BE | 14 | 575, 578 |
| TC-AC-SU-E2E-166-tab-system-log-aktor-objek-user-global-role-dan-group-role | Tab System Log Aktor Menampilkan Entri Object User, Global Role, dan Group Role dengan Name Target dan Isi Identik Popup Changelog | FE+BE | 32 | 565–567 |
| TC-AC-SU-E2E-167-tab-system-log-aktor-objek-tier-group-manager-dan-cascade | Tab System Log Aktor Menampilkan Entri Object Total Control, Read Only, Group Manager, dan Cascade Tier dengan Name Target dan Isi Identik Popup Changelog | FE+BE | 33 | 568–570 |
| TC-AC-SU-E2E-168-activity-log-entri-identik-system-log-ditambah-modified-by | Activity Log Memuat Entri Identik Tab System Log Aktor untuk Tiap Kelas Object Ditambah Kolom Modified By | FE+BE | 14 | 571, 642 |
| TC-AC-SU-E2E-169-notifikasi-in-app-view-only-ke-target | Notifikasi In-App View-Only ke Target untuk Event Remove dan Auto-Revert Tier atau Group Manager | FE+BE | 33 | 579–584, 641 |
| TC-AC-SU-E2E-170-tidak-ada-notifikasi-in-app-untuk-event-tertentu | Tidak Ada Notifikasi In-App ke Target untuk Event Deactivate dan Assign Total Control | FE+BE | 12 | 585, 587 |
| TC-AC-SU-E2E-171-sinkron-role-permission-ke-tab-role | Sinkron Dua Arah Antara Tab Role Settings > User dan Settings > Role & Permission untuk Switch Global Role, CRUD, dan Assign Group Role | FE+BE | 18 | 588–590 |
| TC-AC-SU-E2E-172-sinkron-role-permission-tier-dan-banner | Sinkron Tier Total Control, Read Only, dan Group Manager dari Settings > Role & Permission ke Banner, Badge Role, dan Tab Role | FE+BE | 26 | 591–594 |
| TC-AC-SU-E2E-173-sinkron-global-settings-foto-nama-dan-email-pending | Sinkron dari Global Settings ke Detail User untuk Foto, Nama, Email Pending, dan Pembatalan Email Pending tanpa Entri Changelog | FE+BE | 27 | 595–597 |
| TC-AC-SU-E2E-174-sinkron-global-settings-nonaktif-app-access-dan-hapus-user | Sinkron dari Global Settings untuk Nonaktif User, Aktif Kembali, Cabut App Access Admin Console, dan Hapus User | FE+BE | 35 | 598–600, 643 |
| TC-AC-SU-E2E-175-format-tanggal-dan-waktu-general-settings | Format Tanggal dan Waktu General Settings Berlaku di User List, Popup Changelog, dan Tab Detail User | FE+BE | 32 | 7, 605–607 |
| TC-AC-SU-E2E-176-resilience-activate-deactivate-dan-bulk-gagal-server | Resilience Activate, Deactivate, dan Bulk Activate atau Deactivate Gagal Server (5xx atau Timeout) Mengembalikan Switch dan Menampilkan Toast Error | FE+BE | 27 | 92, 93, 130–132 |
| TC-AC-SU-E2E-177-resilience-resend-gagal-dan-kegagalan-penulisan-log | Resilience Resend Email Gagal Layanan Email atau Server dan Kegagalan Penulisan Log tidak Membatalkan Pengiriman | FE+BE | 17 | 151, 158, 160, 635 |
| TC-AC-SU-E2E-178-resilience-tab-role-autosave-popup-assign-group-dan-auto-revert-gagal | Resilience Autosave Checkbox, Switch Global Role, Save Popup Assign Group Role, dan Auto-Revert Gagal 5xx Mengembalikan State dan Menampilkan Toast Error | FE+BE | 28 | 181, 182, 231, 262 |
| TC-AC-SU-E2E-179-resilience-error-load-user-list-dan-tab-detail | Resilience Error Load User List dan Tab Responsibilities, Changelog, System Log, dan User Log Menampilkan Pesan Error dengan Try Again | FE+BE | 26 | 20, 335, 372, 407, 430 |
| TC-AC-SU-E2E-180-resilience-download-gagal-user-list-group-assignment-responsibilities-dan-changelog | Resilience Download Gagal 5xx pada User List, Detail Group Assignment, Tab Responsibilities, dan Tab Changelog Menampilkan Toast Error tanpa Berkas | FE+BE | 21 | 248, 320, 366, 402 |
| TC-AC-SU-E2E-181-resilience-download-gagal-system-log-user-log-dan-modal-changelog | Resilience Download Gagal 5xx pada Tab System Log, Tab User Log, Popup Changelog User, dan Modal Changelog Group Role Menampilkan Toast Error tanpa Berkas | FE+BE | 21 | 424, 440, 478, 647 |
| TC-AC-SU-E2E-182-defense-in-depth-request-tulis-ditolak-server-isolasi-entitas-dan-proteksi-target | Defense-in-Depth Request Langsung ke Server Ditolak untuk Isolasi Entitas, Mutasi Default User, Mutasi Role Diri Sendiri, Target Total Control, Group di Group Manager, dan Target Nonaktif Global Settings | FE+BE | 18 | 614–619 |
| TC-AC-SU-E2E-183-defense-in-depth-cooldown-resend-read-only-dan-payload-script | Defense-in-Depth Request Langsung Ditolak untuk Group Role tanpa Assignment, Cooldown Resend, Aksi Read Only, dan Target Total Control, serta Payload Script Dirender sebagai Teks | FE+BE | 25 | 620–622, 624, 665 |
| TC-AC-SU-E2E-184-konkurensi-dua-aktor-last-write-wins-dan-request-lama-no-op | Konkurensi Dua Aktor Memakai Last-Write-Wins dan Request Lama Menjadi No-Op pada Deactivate, Activate, Save Assign Group Role, dan Dialog Auto-Revert | FE+BE | 42 | 102, 625–627, 634 |
| TC-AC-SU-E2E-185-konkurensi-deactivate-user-login-dua-aktor-cooldown-dan-request-lama | Konkurensi Deactivate User Sedang Login, Dua Aktor Mengubah Status, Resend Saat Cooldown Aktor Lain, dan Switch Role Request Lama | FE+BE | 30 | 94, 104, 150, 577 |
| TC-AC-SU-E2E-186-double-click-dan-double-submit-deactivate-dan-bulk | Double-Click dan Double-Submit pada Dialog Deactivate, Bulk Deactivate, dan Bulk Activate Hanya Memproses Satu Request | FE+BE | 28 | 103, 135, 628, 629 |
| TC-AC-SU-E2E-187-double-click-dan-double-submit-checkbox-resend-dan-save-group-role | Double-Click dan Double-Submit pada Checkbox CRUD, Resend Activation Email, dan Save Popup Assign Group Role Hanya Memproses Satu Request | FE+BE | 30 | 193, 630–632 |
| TC-AC-SU-E2E-188-mobile-android-aturan-khusus-mobile | Mobile Android Snackbar Kontrol Disabled, Countdown Cooldown Resend, Selection Mode Bulk, dan Bottom Sheet Auto-Revert | FE+BE | 23 | 636–639 |
| TC-AC-SU-E2E-189-row-action-menu-per-status-aktivasi-dan-ikon-severity | User List: Isi Row Action Menu per Status Aktivasi serta Ikon dan Severity Row Actions | FE+BE | 33 | 10, 663 |
| TC-AC-SU-E2E-190-badge-status-header-detail-user-dan-field-email-pending | Detail User: Badge Status Header per Kondisi dan Field Email saat Pending Email Confirmation | FE+BE | 23 | 39, 41 |
| TC-AC-SU-E2E-191-resend-activation-email-tanpa-batas-harian | Resend Activation Email: Pengiriman Berulang Tanpa Batas Harian | FE+BE | 12 | 149 |
| TC-AC-SU-E2E-192-popup-assign-group-role-clear-field-save-dan-changelog-remove | Popup Assign Group Role: Clear Field Lalu Save Melepas Role dan Mencatat Remove per Group | FE+BE | 16 | 229 |
| TC-AC-SU-E2E-193-user-list-filter-panel-kelas-multi-select-satu-opsi | User List Filter Panel: Filter Kelas Multi-Select Satu Opsi per Field | FE+BE | 5 | 274 |
| TC-AC-SU-E2E-194-user-list-sort-3-state-kelas-teks | User List Sort: Sort 3-State Kelas Teks dengan Nilai Kosong di Akhir dan di Awal | FE+BE | 12 | 294 |
| TC-AC-SU-E2E-195-tab-log-download-xlsx-nilai-sel | Tab Changelog, System Log, User Log, dan Responsibilities: Download XLSX dan Nilai Sel | FE+BE | 56 | 365, 401, 423, 439 |
| TC-AC-SU-E2E-196-tab-system-log-search-per-kolom | Tab System Log: Search per Kolom Teks | FE+BE | 8 | 412 |
| TC-AC-SU-E2E-197-modal-changelog-user-download-xlsx-hasil-filter-dan-nilai-sel | Modal Changelog User: Download XLSX dengan Filter Aktif dan Nilai Sel Berkas | FE+BE | 15 | 477 |
| TC-AC-SU-E2E-198-modal-changelog-user-cache-setup-column-independen-dari-tab-changelog | Modal Changelog User: Cache Setup Column Independen dari Tab Changelog Detail User | FE+BE | 15 | 475 |
| TC-AC-SU-E2E-199-hapus-group-tanpa-notifikasi-dan-assignment-group-role-terakhir | Hapus Group Tidak Mengirim Notifikasi ke Group Manager yang Dilepas dan Menonaktifkan Group Role pada Assignment Terakhir | FE+BE | 18 | 586, 601 |
| TC-AC-SU-E2E-200-resilience-error-load-modal-changelog | Resilience Error Load Modal Changelog User, Global Role, dan Group Role Menampilkan Pesan Error dengan Try Again | FE+BE | 17 | 447, 483, 507 |
| TC-AC-SU-E2E-201-role-matrix-tab-role-aktor-total-control-dan-read-only | Role Matrix: Tab Role, Aktor Total Control dan Read Only | FE+BE | 28 | 63, 64 |
| TC-AC-SU-E2E-202-role-matrix-tab-role-aktor-manage-user-and-role-tanpa-update | Role Matrix: Tab Role, Aktor Manage user and role tanpa Update | FE+BE | 9 | 65 |
| TC-AC-SU-E2E-203-user-list-retensi-state-breadcrumb-f5-dan-klik-ulang-sidebar | User List Retensi State: Breadcrumb dari Detail, F5 dengan Node Sidebar Group, dan Klik Ulang Sidebar | FE+BE | 34 | 323–325 |
| TC-AC-SU-E2E-204-tab-system-log-filter-panel-satu-opsi-per-field | Tab System Log: Filter Panel, Filter Satu Opsi per Field Multi-select | FE+BE | 12 | 416 |
| TC-AC-SU-E2E-205-tab-system-log-filter-panel-or-dalam-field-dan-antar-field | Tab System Log: Filter Panel, OR di dalam Satu Field dan AND antar Field | FE+BE | 14 | 417 |
| TC-AC-SU-E2E-206-modal-changelog-global-role-setup-column-tutup-tanpa-save-dan-kolom-minimal | Modal Changelog Global Role: Setup Column Tutup Tanpa Save dan Satu Kolom Tersisa | FE+BE | 20 | 501, 502 |
| TC-AC-SU-E2E-207-absence-changelog-user-request-langsung-ditolak-server | Absence Changelog: User untuk Request Langsung yang Ditolak Server pada Mutasi Default User, Role Diri Sendiri, Edit Role Target Total Control, Group Role tanpa Assignment, Cooldown Resend, dan Deactivate Target Total Control | FE+BE | 43 | 615–617, 620, 621, 665 |
| TC-AC-SU-E2E-208-modal-changelog-global-role-mencatat-cascade-total-control-dan-read-only | Modal Changelog User > Global Role Mencatat Assign dan Remove via Total Control atau Read Only (Cascade) | FE+BE | 28 | 553–556 |
| TC-AC-SU-E2E-209-modal-changelog-group-role-mencatat-cascade-total-control-dan-read-only | Modal Changelog User > Group Role Mencatat Assign dan Remove via Total Control atau Read Only per Group (Cascade) | FE+BE | 36 | 560–563 |

Spec 188 memakai `coverage.mobile: automated` saja (aplikasi native Android); 208 spec lain memakai `coverage.web: automated`.

## Pembagian TC lintas spec

- Setiap TC aktif muncul di `sourceTc` satu spec, kecuali 9 TC yang terbelah dan muncul di dua spec; `## Notes` kedua spec menulis butir "Pembagian TC lintas spec": TC-317 dan TC-661 antara 088 dan 089 ( nama berkas, kolom, dan jumlah baris di 088; identitas baris di dalam berkas, kelas f, di 089), TC-365 antara 102 dan 195 (nama berkas, header, jumlah baris di 102; nilai sel, kelas f, di 195), serta TC-615, 616, 617 (182 dan 207) dan TC-620, 621, 665 (183 dan 207) (respons server dan state data di spec asal; asersi "tidak dicatat di Changelog: User" di spec absence 207). Union `sourceTc` = 664 TC aktif, tanpa TC yang tidak dikenal.
- Spec 189–200 memuat TC berikut: 189 (TC-10, 663), 190 (TC-39, 41), 191 (TC-149), 192 (TC-229), 193 (TC-274), 194 (TC-294), 195 (TC-365, 401, 423, 439), 196 (TC-412), 197 (TC-477), 198 (TC-475), 199 (TC-586, 601), 200 (TC-447, 483, 507).
- Spec 207–209 memuat TC berikut: 207 (TC-615, 616, 617, 620, 621, 665), 208 (TC-553, 554, 555, 556), 209 (TC-560, 561, 562, 563). Spec 162 menyisakan TC-550, 551, 552 dan spec 163 menyisakan TC-557, 558, 559; tiap TC memakai user seed sendiri.
- Spec 201–206 memuat TC berikut: 201 (TC-63, 64), 202 (TC-65), 203 (TC-323, 324, 325), 204 (TC-416), 205 (TC-417), 206 (TC-501, 502). Spec asal mempertahankan sisa TC-nya: 021 (TC-62), 090 (TC-321, 322), 116 (TC-414, 415), 143 (TC-499, 500).
- Spec 024 (54 langkah) tidak dibagi: TC-AC-SU-71 memuat keempat blok akun (Total Control, Manage user and role Update, Read Only, Manage user and role Read saja), sehingga membagi per akun membelah satu TC.
- Asersi absence log murni (kelas g) berada di spec absence 207; spec fungsional (182, 183) mencatat rujukan di `## Notes` masing-masing.

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec (jumlah spec pemakai): `AC_DIST_MUR_PASSWORD` (4), `AC_DIST_TC_PASSWORD` (4), `AC_DU_PASSWORD` (21), `AC_E1_DU_PASSWORD` (1), `AC_E1_TC_PASSWORD` (1), `AC_GM_PASSWORD` (1), `AC_MUR_READ_PASSWORD` (7), `AC_MUR_UPDATE_PASSWORD` (16), `AC_RO_PASSWORD` (11), `AC_SU_SEEDED_PASSWORD` (6), `AC_TC_PASSWORD` (146), `AC_TS_PASSWORD` (1). Di `spectra.config.ts` dan `.env.example` baru `AC_TC_PASSWORD` yang terdaftar dari daftar ini; nama lain belum didaftarkan dan berkas itu tidak diubah oleh generate spec. `AC_DU_PASSWORD` dan `AC_RO_PASSWORD` dipakai juga oleh spec Admin Console lain tetapi belum terdaftar di `spectra.config.ts`. Password user seed memakai satu nama, `AC_SU_SEEDED_PASSWORD` (spec 054, 161, 169, 170, 185, 199).
- Akun di luar Tabel Pre-setup TC (email disediakan tim FE): Manage user and role (Update) dan (Read saja), Group Manager tanpa akses modul, Manage TAG stock saja (`Rudi Hartono`), Total Control dan Manage user and role (Update) entitas Distributor Nusantara, serta Default User dan Total Control entitas baru E1.
- Fixture BE: seeding dan pemulihan user (status aktivasi, Active/Inactive, role, tier, Group Manager), group tree, Group Role, Custom Field User, entri System Log, Changelog, User Log, dan notifikasi, flag Guided Tooltip `guided_tooltip_seen_ac-settings-user`, Selection Limit, status Suspended entitas, General Settings (Date Format, Time Format, Timezone), status email aktor; pembacaan state BE yang tidak terlihat di UI; penghapusan preferensi kolom Setup Column di browser.
- Kemampuan teknis: klien HTTP (request langsung, kelas a), intercept jaringan (5xx, timeout, respons ditahan), dua konteks browser, sesi API aktor, jam server dan jam browser (spec 039, 041, 165, 183, 185, 188, 191), mail-catcher untuk jumlah email per alamat (hanya spec 183), penangkap unduhan CSV/XLSX, drag and drop, lebar viewport, dan perangkat Android (spec 188).
- Suite berjalan serial (`parallel: false`): spec mengubah state global (Selection Limit, format General Settings, status Suspended, jam server, Custom Field User) dan Select All mengenai seluruh user eligible di entitas.
- Data Pre-setup yang diubah lalu dipulihkan lewat Fixture BE (S-06, pengecualian 2026-10-30; efek pada Last Update dan Modified By dicatat di Prerequisites tiap spec): Default User dan akun aktor Total Control (spec 006, 023), Group Role aktor Manage user and role (spec 022), email aktor Manage user and role (spec 024), status akun Default User (spec 038).
- Environment automation terisolasi dari aktivitas pengguna lain.

## Temuan yang masih terbuka

Temuan TC sumber (ambigu, kontradiktif, kurang precondition) dicatat per spec di `## Notes` butir "Temuan untuk QA" (200 spec memilikinya). Yang melintasi banyak spec:

- Spec melewati batas ±35 langkah (54 spec; alasan tertulis di `## Notes` tiap spec: 009 (39), 012 (40), 013 (40), 016 (42), 019 (41), 022 (37), 023 (40), 024 (54), 026 (45), 027 (43), 028 (39), 037 (47), 042 (43), 043 (38), 049 (43), 058 (40), 061 (36), 062 (40), 064 (38), 065 (36), 068 (39), 071 (38), 075 (48), 076 (39), 078 (48), 081 (43), 082 (43), 085 (52), 086 (36), 087 (36), 091 (61), 092 (67), 097 (37), 100 (43), 101 (44), 107 (36), 108 (39), 110 (43), 111 (47), 113 (38), 117 (36), 135 (41), 140 (37), 141 (36), 142 (46), 151 (36), 152 (42), 155 (37), 157 (37), 160 (38), 184 (42), 195 (56), 207 (43), 209 (36)). Spec 204 hanya 12 langkah nominal tetapi sekitar 42 dengan ekspansi empat field (satu TC, TC-AC-SU-416, tidak dibelah).
- Akun Pre-setup yang tidak punya email atau password di TC (Total Control dan Manage user and role entitas Distributor Nusantara, entitas E1, Manage TAG stock saja) disediakan tim FE; nama env var ditetapkan penulis spec.
- Spec 038 memakai akun Default User Pre-setup #1 sebagai target status Pending Email Confirmation lewat Fixture BE (TC-141); alternatifnya user Default User terpisah, menunggu keputusan pemilik.
- TC yang memakai nama Pre-setup sebagai target tulis atau hapus (Custom Field `Office Location`, `Shift`, `Blood Type`, `Shirt Size`, `Locker No`, Region B, Region C, Dedi Kurnia) dipetakan ke padanan seed bersuffix (S-06, S-12); Expected TC yang memuat nama itu memakai nama bersuffix.
- Post Condition tanpa langkah observasi (mis. TC-155, TC-651) tidak diasersi; dicatat di "Temuan untuk QA".

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-SU-1 | TC-AC-SU-E2E-001 | FE+BE |
| TC-AC-SU-2 | TC-AC-SU-E2E-001 | FE+BE |
| TC-AC-SU-3 | TC-AC-SU-E2E-003 | FE+BE |
| TC-AC-SU-4 | TC-AC-SU-E2E-001 | FE+BE |
| TC-AC-SU-5 | TC-AC-SU-E2E-002 | FE+BE |
| TC-AC-SU-6 | TC-AC-SU-E2E-002 | FE+BE |
| TC-AC-SU-7 | TC-AC-SU-E2E-175 | FE+BE |
| TC-AC-SU-8 | TC-AC-SU-E2E-002 | FE+BE |
| TC-AC-SU-9 | TC-AC-SU-E2E-005 | FE+BE |
| TC-AC-SU-10 | TC-AC-SU-E2E-189 | FE+BE |
| TC-AC-SU-11 | TC-AC-SU-E2E-006 | FE+BE |
| TC-AC-SU-12 | TC-AC-SU-E2E-006 | FE+BE |
| TC-AC-SU-13 | TC-AC-SU-E2E-003 | FE+BE |
| TC-AC-SU-14 | TC-AC-SU-E2E-004 | FE+BE |
| TC-AC-SU-15 | TC-AC-SU-E2E-004 | FE+BE |
| TC-AC-SU-16 | TC-AC-SU-E2E-003 | FE+BE |
| TC-AC-SU-17 | TC-AC-SU-E2E-004 | FE+BE |
| TC-AC-SU-18 | TC-AC-SU-E2E-014 | FE+BE |
| TC-AC-SU-19 | TC-AC-SU-E2E-004 | FE+BE |
| TC-AC-SU-20 | TC-AC-SU-E2E-179 | FE+BE |
| TC-AC-SU-21 | TC-AC-SU-E2E-007 | FE+BE |
| TC-AC-SU-22 | TC-AC-SU-E2E-007 | FE+BE |
| TC-AC-SU-23 | TC-AC-SU-E2E-007 | FE+BE |
| TC-AC-SU-24 | TC-AC-SU-E2E-007 | FE+BE |
| TC-AC-SU-25 | TC-AC-SU-E2E-008 | FE+BE |
| TC-AC-SU-26 | TC-AC-SU-E2E-008 | FE+BE |
| TC-AC-SU-27 | TC-AC-SU-E2E-008 | FE+BE |
| TC-AC-SU-28 | TC-AC-SU-E2E-008 | FE+BE |
| TC-AC-SU-29 | TC-AC-SU-E2E-009 | FE+BE |
| TC-AC-SU-30 | TC-AC-SU-E2E-009 | FE+BE |
| TC-AC-SU-31 | TC-AC-SU-E2E-009 | FE+BE |
| TC-AC-SU-32 | TC-AC-SU-E2E-009 | FE+BE |
| TC-AC-SU-33 | TC-AC-SU-E2E-010 | FE+BE |
| TC-AC-SU-34 | TC-AC-SU-E2E-010 | FE+BE |
| TC-AC-SU-35 | TC-AC-SU-E2E-010 | FE+BE |
| TC-AC-SU-36 | TC-AC-SU-E2E-010 | FE+BE |
| TC-AC-SU-37 | TC-AC-SU-E2E-011 | FE+BE |
| TC-AC-SU-38 | TC-AC-SU-E2E-013 | FE+BE |
| TC-AC-SU-39 | TC-AC-SU-E2E-190 | FE+BE |
| TC-AC-SU-40 | TC-AC-SU-E2E-011 | FE+BE |
| TC-AC-SU-41 | TC-AC-SU-E2E-190 | FE+BE |
| TC-AC-SU-42 | TC-AC-SU-E2E-012 | FE+BE |
| TC-AC-SU-43 | TC-AC-SU-E2E-012 | FE+BE |
| TC-AC-SU-44 | TC-AC-SU-E2E-012 | FE+BE |
| TC-AC-SU-45 | TC-AC-SU-E2E-012 | FE+BE |
| TC-AC-SU-46 | TC-AC-SU-E2E-013 | FE+BE |
| TC-AC-SU-47 | TC-AC-SU-E2E-014 | FE+BE |
| TC-AC-SU-48 | TC-AC-SU-E2E-013 | FE+BE |
| TC-AC-SU-49 | TC-AC-SU-E2E-013 | FE+BE |
| TC-AC-SU-50 | TC-AC-SU-E2E-015 | FE+BE |
| TC-AC-SU-51 | TC-AC-SU-E2E-016 | FE+BE |
| TC-AC-SU-52 | TC-AC-SU-E2E-016 | FE+BE |
| TC-AC-SU-53 | TC-AC-SU-E2E-016 | FE+BE |
| TC-AC-SU-54 | TC-AC-SU-E2E-017 | FE+BE |
| TC-AC-SU-55 | TC-AC-SU-E2E-016 | FE+BE |
| TC-AC-SU-56 | TC-AC-SU-E2E-018 | FE+BE |
| TC-AC-SU-57 | TC-AC-SU-E2E-018 | FE+BE |
| TC-AC-SU-58 | TC-AC-SU-E2E-015 | FE+BE |
| TC-AC-SU-59 | TC-AC-SU-E2E-019 | FE+BE |
| TC-AC-SU-60 | TC-AC-SU-E2E-019 | FE+BE |
| TC-AC-SU-61 | TC-AC-SU-E2E-019 | FE+BE |
| TC-AC-SU-62 | TC-AC-SU-E2E-021 | FE+BE |
| TC-AC-SU-63 | TC-AC-SU-E2E-201 | FE+BE |
| TC-AC-SU-64 | TC-AC-SU-E2E-201 | FE+BE |
| TC-AC-SU-65 | TC-AC-SU-E2E-202 | FE+BE |
| TC-AC-SU-66 | TC-AC-SU-E2E-022 | FE+BE |
| TC-AC-SU-67 | TC-AC-SU-E2E-022 | FE+BE |
| TC-AC-SU-68 | TC-AC-SU-E2E-023 | FE+BE |
| TC-AC-SU-69 | TC-AC-SU-E2E-023 | FE+BE |
| TC-AC-SU-70 | TC-AC-SU-E2E-023 | FE+BE |
| TC-AC-SU-71 | TC-AC-SU-E2E-024 | FE+BE |
| TC-AC-SU-72 | TC-AC-SU-E2E-024 | FE+BE |
| TC-AC-SU-73 | TC-AC-SU-E2E-025 | FE+BE |
| TC-AC-SU-74 | TC-AC-SU-E2E-025 | FE+BE |
| TC-AC-SU-75 | TC-AC-SU-E2E-026 | FE+BE |
| TC-AC-SU-76 | TC-AC-SU-E2E-026 | FE+BE |
| TC-AC-SU-77 | TC-AC-SU-E2E-020 | FE+BE |
| TC-AC-SU-78 | TC-AC-SU-E2E-022 | FE+BE |
| TC-AC-SU-79 | TC-AC-SU-E2E-019 | FE+BE |
| TC-AC-SU-80 | TC-AC-SU-E2E-026 | FE+BE |
| TC-AC-SU-81 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-82 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-83 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-84 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-85 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-86 | TC-AC-SU-E2E-027 | FE+BE |
| TC-AC-SU-87 | TC-AC-SU-E2E-028 | FE+BE |
| TC-AC-SU-88 | TC-AC-SU-E2E-028 | FE+BE |
| TC-AC-SU-89 | TC-AC-SU-E2E-028 | FE+BE |
| TC-AC-SU-90 | TC-AC-SU-E2E-029 | FE+BE |
| TC-AC-SU-91 | TC-AC-SU-E2E-029 | FE+BE |
| TC-AC-SU-92 | TC-AC-SU-E2E-176 | FE+BE |
| TC-AC-SU-93 | TC-AC-SU-E2E-176 | FE+BE |
| TC-AC-SU-94 | TC-AC-SU-E2E-185 | FE+BE |
| TC-AC-SU-96 | TC-AC-SU-E2E-028 | FE+BE |
| TC-AC-SU-97 | TC-AC-SU-E2E-028 | FE+BE |
| TC-AC-SU-98 | TC-AC-SU-E2E-020 | FE+BE |
| TC-AC-SU-99 | TC-AC-SU-E2E-018 | FE+BE |
| TC-AC-SU-100 | TC-AC-SU-E2E-020 | FE+BE |
| TC-AC-SU-101 | TC-AC-SU-E2E-020 | FE+BE |
| TC-AC-SU-102 | TC-AC-SU-E2E-184 | FE+BE |
| TC-AC-SU-103 | TC-AC-SU-E2E-186 | FE+BE |
| TC-AC-SU-104 | TC-AC-SU-E2E-185 | FE+BE |
| TC-AC-SU-105 | TC-AC-SU-E2E-030 | FE+BE |
| TC-AC-SU-106 | TC-AC-SU-E2E-030 | FE+BE |
| TC-AC-SU-107 | TC-AC-SU-E2E-030 | FE+BE |
| TC-AC-SU-108 | TC-AC-SU-E2E-030 | FE+BE |
| TC-AC-SU-109 | TC-AC-SU-E2E-030 | FE+BE |
| TC-AC-SU-110 | TC-AC-SU-E2E-031 | FE+BE |
| TC-AC-SU-111 | TC-AC-SU-E2E-031 | FE+BE |
| TC-AC-SU-112 | TC-AC-SU-E2E-031 | FE+BE |
| TC-AC-SU-113 | TC-AC-SU-E2E-037 | FE+BE |
| TC-AC-SU-114 | TC-AC-SU-E2E-015 | FE+BE |
| TC-AC-SU-115 | TC-AC-SU-E2E-033 | FE+BE |
| TC-AC-SU-116 | TC-AC-SU-E2E-033 | FE+BE |
| TC-AC-SU-117 | TC-AC-SU-E2E-034 | FE+BE |
| TC-AC-SU-118 | TC-AC-SU-E2E-034 | FE+BE |
| TC-AC-SU-119 | TC-AC-SU-E2E-034 | FE+BE |
| TC-AC-SU-120 | TC-AC-SU-E2E-034 | FE+BE |
| TC-AC-SU-121 | TC-AC-SU-E2E-034 | FE+BE |
| TC-AC-SU-122 | TC-AC-SU-E2E-035 | FE+BE |
| TC-AC-SU-123 | TC-AC-SU-E2E-036 | FE+BE |
| TC-AC-SU-124 | TC-AC-SU-E2E-035 | FE+BE |
| TC-AC-SU-125 | TC-AC-SU-E2E-037 | FE+BE |
| TC-AC-SU-126 | TC-AC-SU-E2E-035 | FE+BE |
| TC-AC-SU-127 | TC-AC-SU-E2E-035 | FE+BE |
| TC-AC-SU-128 | TC-AC-SU-E2E-035 | FE+BE |
| TC-AC-SU-129 | TC-AC-SU-E2E-036 | FE+BE |
| TC-AC-SU-130 | TC-AC-SU-E2E-176 | FE+BE |
| TC-AC-SU-131 | TC-AC-SU-E2E-176 | FE+BE |
| TC-AC-SU-132 | TC-AC-SU-E2E-176 | FE+BE |
| TC-AC-SU-134 | TC-AC-SU-E2E-032 | FE+BE |
| TC-AC-SU-135 | TC-AC-SU-E2E-186 | FE+BE |
| TC-AC-SU-136 | TC-AC-SU-E2E-025 | FE+BE |
| TC-AC-SU-137 | TC-AC-SU-E2E-025 | FE+BE |
| TC-AC-SU-138 | TC-AC-SU-E2E-038 | FE+BE |
| TC-AC-SU-139 | TC-AC-SU-E2E-038 | FE+BE |
| TC-AC-SU-140 | TC-AC-SU-E2E-024 | FE+BE |
| TC-AC-SU-141 | TC-AC-SU-E2E-038 | FE+BE |
| TC-AC-SU-142 | TC-AC-SU-E2E-039 | FE+BE |
| TC-AC-SU-143 | TC-AC-SU-E2E-040 | FE+BE |
| TC-AC-SU-144 | TC-AC-SU-E2E-040 | FE+BE |
| TC-AC-SU-145 | TC-AC-SU-E2E-040 | FE+BE |
| TC-AC-SU-146 | TC-AC-SU-E2E-039 | FE+BE |
| TC-AC-SU-147 | TC-AC-SU-E2E-039 | FE+BE |
| TC-AC-SU-148 | TC-AC-SU-E2E-039 | FE+BE |
| TC-AC-SU-149 | TC-AC-SU-E2E-191 | FE+BE |
| TC-AC-SU-150 | TC-AC-SU-E2E-185 | FE+BE |
| TC-AC-SU-151 | TC-AC-SU-E2E-177 | FE+BE |
| TC-AC-SU-152 | TC-AC-SU-E2E-024 | FE+BE |
| TC-AC-SU-153 | TC-AC-SU-E2E-024 | FE+BE |
| TC-AC-SU-154 | TC-AC-SU-E2E-041 | FE+BE |
| TC-AC-SU-155 | TC-AC-SU-E2E-038 | FE+BE |
| TC-AC-SU-156 | TC-AC-SU-E2E-041 | FE+BE |
| TC-AC-SU-157 | TC-AC-SU-E2E-041 | FE+BE |
| TC-AC-SU-158 | TC-AC-SU-E2E-177 | FE+BE |
| TC-AC-SU-159 | TC-AC-SU-E2E-038 | FE+BE |
| TC-AC-SU-160 | TC-AC-SU-E2E-177 | FE+BE |
| TC-AC-SU-161 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-162 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-163 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-164 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-165 | TC-AC-SU-E2E-043 | FE+BE |
| TC-AC-SU-166 | TC-AC-SU-E2E-043 | FE+BE |
| TC-AC-SU-167 | TC-AC-SU-E2E-043 | FE+BE |
| TC-AC-SU-168 | TC-AC-SU-E2E-043 | FE+BE |
| TC-AC-SU-169 | TC-AC-SU-E2E-043 | FE+BE |
| TC-AC-SU-170 | TC-AC-SU-E2E-045 | FE+BE |
| TC-AC-SU-171 | TC-AC-SU-E2E-045 | FE+BE |
| TC-AC-SU-172 | TC-AC-SU-E2E-045 | FE+BE |
| TC-AC-SU-173 | TC-AC-SU-E2E-047 | FE+BE |
| TC-AC-SU-174 | TC-AC-SU-E2E-047 | FE+BE |
| TC-AC-SU-175 | TC-AC-SU-E2E-047 | FE+BE |
| TC-AC-SU-176 | TC-AC-SU-E2E-046 | FE+BE |
| TC-AC-SU-177 | TC-AC-SU-E2E-047 | FE+BE |
| TC-AC-SU-178 | TC-AC-SU-E2E-047 | FE+BE |
| TC-AC-SU-179 | TC-AC-SU-E2E-046 | FE+BE |
| TC-AC-SU-180 | TC-AC-SU-E2E-046 | FE+BE |
| TC-AC-SU-181 | TC-AC-SU-E2E-178 | FE+BE |
| TC-AC-SU-182 | TC-AC-SU-E2E-178 | FE+BE |
| TC-AC-SU-183 | TC-AC-SU-E2E-048 | FE+BE |
| TC-AC-SU-184 | TC-AC-SU-E2E-048 | FE+BE |
| TC-AC-SU-185 | TC-AC-SU-E2E-049 | FE+BE |
| TC-AC-SU-186 | TC-AC-SU-E2E-049 | FE+BE |
| TC-AC-SU-187 | TC-AC-SU-E2E-049 | FE+BE |
| TC-AC-SU-188 | TC-AC-SU-E2E-049 | FE+BE |
| TC-AC-SU-189 | TC-AC-SU-E2E-050 | FE+BE |
| TC-AC-SU-190 | TC-AC-SU-E2E-049 | FE+BE |
| TC-AC-SU-191 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-192 | TC-AC-SU-E2E-017 | FE+BE |
| TC-AC-SU-193 | TC-AC-SU-E2E-187 | FE+BE |
| TC-AC-SU-194 | TC-AC-SU-E2E-051 | FE+BE |
| TC-AC-SU-195 | TC-AC-SU-E2E-052 | FE+BE |
| TC-AC-SU-196 | TC-AC-SU-E2E-052 | FE+BE |
| TC-AC-SU-197 | TC-AC-SU-E2E-052 | FE+BE |
| TC-AC-SU-198 | TC-AC-SU-E2E-053 | FE+BE |
| TC-AC-SU-199 | TC-AC-SU-E2E-053 | FE+BE |
| TC-AC-SU-200 | TC-AC-SU-E2E-053 | FE+BE |
| TC-AC-SU-201 | TC-AC-SU-E2E-055 | FE+BE |
| TC-AC-SU-202 | TC-AC-SU-E2E-056 | FE+BE |
| TC-AC-SU-203 | TC-AC-SU-E2E-055 | FE+BE |
| TC-AC-SU-204 | TC-AC-SU-E2E-055 | FE+BE |
| TC-AC-SU-205 | TC-AC-SU-E2E-054 | FE+BE |
| TC-AC-SU-206 | TC-AC-SU-E2E-054 | FE+BE |
| TC-AC-SU-207 | TC-AC-SU-E2E-054 | FE+BE |
| TC-AC-SU-208 | TC-AC-SU-E2E-057 | FE+BE |
| TC-AC-SU-209 | TC-AC-SU-E2E-058 | FE+BE |
| TC-AC-SU-210 | TC-AC-SU-E2E-057 | FE+BE |
| TC-AC-SU-211 | TC-AC-SU-E2E-057 | FE+BE |
| TC-AC-SU-212 | TC-AC-SU-E2E-042 | FE+BE |
| TC-AC-SU-213 | TC-AC-SU-E2E-059 | FE+BE |
| TC-AC-SU-214 | TC-AC-SU-E2E-060 | FE+BE |
| TC-AC-SU-215 | TC-AC-SU-E2E-060 | FE+BE |
| TC-AC-SU-216 | TC-AC-SU-E2E-060 | FE+BE |
| TC-AC-SU-217 | TC-AC-SU-E2E-060 | FE+BE |
| TC-AC-SU-218 | TC-AC-SU-E2E-061 | FE+BE |
| TC-AC-SU-219 | TC-AC-SU-E2E-061 | FE+BE |
| TC-AC-SU-220 | TC-AC-SU-E2E-061 | FE+BE |
| TC-AC-SU-221 | TC-AC-SU-E2E-061 | FE+BE |
| TC-AC-SU-222 | TC-AC-SU-E2E-062 | FE+BE |
| TC-AC-SU-223 | TC-AC-SU-E2E-062 | FE+BE |
| TC-AC-SU-224 | TC-AC-SU-E2E-062 | FE+BE |
| TC-AC-SU-225 | TC-AC-SU-E2E-062 | FE+BE |
| TC-AC-SU-226 | TC-AC-SU-E2E-063 | FE+BE |
| TC-AC-SU-227 | TC-AC-SU-E2E-063 | FE+BE |
| TC-AC-SU-228 | TC-AC-SU-E2E-063 | FE+BE |
| TC-AC-SU-229 | TC-AC-SU-E2E-192 | FE+BE |
| TC-AC-SU-230 | TC-AC-SU-E2E-064 | FE+BE |
| TC-AC-SU-231 | TC-AC-SU-E2E-178 | FE+BE |
| TC-AC-SU-232 | TC-AC-SU-E2E-065 | FE+BE |
| TC-AC-SU-233 | TC-AC-SU-E2E-065 | FE+BE |
| TC-AC-SU-234 | TC-AC-SU-E2E-065 | FE+BE |
| TC-AC-SU-235 | TC-AC-SU-E2E-065 | FE+BE |
| TC-AC-SU-236 | TC-AC-SU-E2E-066 | FE+BE |
| TC-AC-SU-237 | TC-AC-SU-E2E-066 | FE+BE |
| TC-AC-SU-238 | TC-AC-SU-E2E-067 | FE+BE |
| TC-AC-SU-239 | TC-AC-SU-E2E-067 | FE+BE |
| TC-AC-SU-240 | TC-AC-SU-E2E-067 | FE+BE |
| TC-AC-SU-241 | TC-AC-SU-E2E-066 | FE+BE |
| TC-AC-SU-242 | TC-AC-SU-E2E-058 | FE+BE |
| TC-AC-SU-243 | TC-AC-SU-E2E-058 | FE+BE |
| TC-AC-SU-244 | TC-AC-SU-E2E-059 | FE+BE |
| TC-AC-SU-245 | TC-AC-SU-E2E-068 | FE+BE |
| TC-AC-SU-246 | TC-AC-SU-E2E-068 | FE+BE |
| TC-AC-SU-247 | TC-AC-SU-E2E-068 | FE+BE |
| TC-AC-SU-248 | TC-AC-SU-E2E-180 | FE+BE |
| TC-AC-SU-249 | TC-AC-SU-E2E-070 | FE+BE |
| TC-AC-SU-250 | TC-AC-SU-E2E-070 | FE+BE |
| TC-AC-SU-251 | TC-AC-SU-E2E-070 | FE+BE |
| TC-AC-SU-252 | TC-AC-SU-E2E-070 | FE+BE |
| TC-AC-SU-253 | TC-AC-SU-E2E-071 | FE+BE |
| TC-AC-SU-254 | TC-AC-SU-E2E-071 | FE+BE |
| TC-AC-SU-255 | TC-AC-SU-E2E-071 | FE+BE |
| TC-AC-SU-256 | TC-AC-SU-E2E-071 | FE+BE |
| TC-AC-SU-257 | TC-AC-SU-E2E-072 | FE+BE |
| TC-AC-SU-258 | TC-AC-SU-E2E-072 | FE+BE |
| TC-AC-SU-259 | TC-AC-SU-E2E-072 | FE+BE |
| TC-AC-SU-260 | TC-AC-SU-E2E-073 | FE+BE |
| TC-AC-SU-261 | TC-AC-SU-E2E-057 | FE+BE |
| TC-AC-SU-262 | TC-AC-SU-E2E-178 | FE+BE |
| TC-AC-SU-263 | TC-AC-SU-E2E-074 | FE+BE |
| TC-AC-SU-264 | TC-AC-SU-E2E-074 | FE+BE |
| TC-AC-SU-265 | TC-AC-SU-E2E-075 | FE+BE |
| TC-AC-SU-266 | TC-AC-SU-E2E-075 | FE+BE |
| TC-AC-SU-267 | TC-AC-SU-E2E-075 | FE+BE |
| TC-AC-SU-268 | TC-AC-SU-E2E-075 | FE+BE |
| TC-AC-SU-269 | TC-AC-SU-E2E-076 | FE+BE |
| TC-AC-SU-270 | TC-AC-SU-E2E-076 | FE+BE |
| TC-AC-SU-271 | TC-AC-SU-E2E-075 | FE+BE |
| TC-AC-SU-272 | TC-AC-SU-E2E-077 | FE+BE |
| TC-AC-SU-273 | TC-AC-SU-E2E-077 | FE+BE |
| TC-AC-SU-274 | TC-AC-SU-E2E-193 | FE+BE |
| TC-AC-SU-275 | TC-AC-SU-E2E-078 | FE+BE |
| TC-AC-SU-276 | TC-AC-SU-E2E-078 | FE+BE |
| TC-AC-SU-277 | TC-AC-SU-E2E-078 | FE+BE |
| TC-AC-SU-278 | TC-AC-SU-E2E-078 | FE+BE |
| TC-AC-SU-279 | TC-AC-SU-E2E-079 | FE+BE |
| TC-AC-SU-280 | TC-AC-SU-E2E-079 | FE+BE |
| TC-AC-SU-281 | TC-AC-SU-E2E-079 | FE+BE |
| TC-AC-SU-282 | TC-AC-SU-E2E-079 | FE+BE |
| TC-AC-SU-283 | TC-AC-SU-E2E-080 | FE+BE |
| TC-AC-SU-284 | TC-AC-SU-E2E-080 | FE+BE |
| TC-AC-SU-285 | TC-AC-SU-E2E-080 | FE+BE |
| TC-AC-SU-286 | TC-AC-SU-E2E-081 | FE+BE |
| TC-AC-SU-287 | TC-AC-SU-E2E-081 | FE+BE |
| TC-AC-SU-288 | TC-AC-SU-E2E-081 | FE+BE |
| TC-AC-SU-289 | TC-AC-SU-E2E-081 | FE+BE |
| TC-AC-SU-290 | TC-AC-SU-E2E-082 | FE+BE |
| TC-AC-SU-291 | TC-AC-SU-E2E-082 | FE+BE |
| TC-AC-SU-292 | TC-AC-SU-E2E-082 | FE+BE |
| TC-AC-SU-293 | TC-AC-SU-E2E-082 | FE+BE |
| TC-AC-SU-294 | TC-AC-SU-E2E-194 | FE+BE |
| TC-AC-SU-295 | TC-AC-SU-E2E-083 | FE+BE |
| TC-AC-SU-296 | TC-AC-SU-E2E-083 | FE+BE |
| TC-AC-SU-297 | TC-AC-SU-E2E-083 | FE+BE |
| TC-AC-SU-298 | TC-AC-SU-E2E-084 | FE+BE |
| TC-AC-SU-299 | TC-AC-SU-E2E-084 | FE+BE |
| TC-AC-SU-300 | TC-AC-SU-E2E-084 | FE+BE |
| TC-AC-SU-301 | TC-AC-SU-E2E-084 | FE+BE |
| TC-AC-SU-302 | TC-AC-SU-E2E-084 | FE+BE |
| TC-AC-SU-303 | TC-AC-SU-E2E-085 | FE+BE |
| TC-AC-SU-304 | TC-AC-SU-E2E-085 | FE+BE |
| TC-AC-SU-305 | TC-AC-SU-E2E-085 | FE+BE |
| TC-AC-SU-306 | TC-AC-SU-E2E-085 | FE+BE |
| TC-AC-SU-307 | TC-AC-SU-E2E-085 | FE+BE |
| TC-AC-SU-308 | TC-AC-SU-E2E-086 | FE+BE |
| TC-AC-SU-309 | TC-AC-SU-E2E-086 | FE+BE |
| TC-AC-SU-310 | TC-AC-SU-E2E-086 | FE+BE |
| TC-AC-SU-311 | TC-AC-SU-E2E-087 | FE+BE |
| TC-AC-SU-312 | TC-AC-SU-E2E-087 | FE+BE |
| TC-AC-SU-313 | TC-AC-SU-E2E-087 | FE+BE |
| TC-AC-SU-314 | TC-AC-SU-E2E-087 | FE+BE |
| TC-AC-SU-315 | TC-AC-SU-E2E-088 | FE+BE |
| TC-AC-SU-316 | TC-AC-SU-E2E-088 | FE+BE |
| TC-AC-SU-317 | TC-AC-SU-E2E-088, TC-AC-SU-E2E-089 | FE+BE |
| TC-AC-SU-318 | TC-AC-SU-E2E-088 | FE+BE |
| TC-AC-SU-319 | TC-AC-SU-E2E-089 | FE+BE |
| TC-AC-SU-320 | TC-AC-SU-E2E-180 | FE+BE |
| TC-AC-SU-321 | TC-AC-SU-E2E-090 | FE+BE |
| TC-AC-SU-322 | TC-AC-SU-E2E-090 | FE+BE |
| TC-AC-SU-323 | TC-AC-SU-E2E-203 | FE+BE |
| TC-AC-SU-324 | TC-AC-SU-E2E-203 | FE+BE |
| TC-AC-SU-325 | TC-AC-SU-E2E-203 | FE+BE |
| TC-AC-SU-326 | TC-AC-SU-E2E-032 | FE+BE |
| TC-AC-SU-327 | TC-AC-SU-E2E-032 | FE+BE |
| TC-AC-SU-328 | TC-AC-SU-E2E-091 | FE+BE |
| TC-AC-SU-329 | TC-AC-SU-E2E-091 | FE+BE |
| TC-AC-SU-330 | TC-AC-SU-E2E-091 | FE+BE |
| TC-AC-SU-331 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-332 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-333 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-334 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-335 | TC-AC-SU-E2E-179 | FE+BE |
| TC-AC-SU-336 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-337 | TC-AC-SU-E2E-093 | FE+BE |
| TC-AC-SU-338 | TC-AC-SU-E2E-094 | FE+BE |
| TC-AC-SU-339 | TC-AC-SU-E2E-094 | FE+BE |
| TC-AC-SU-340 | TC-AC-SU-E2E-095 | FE+BE |
| TC-AC-SU-341 | TC-AC-SU-E2E-095 | FE+BE |
| TC-AC-SU-342 | TC-AC-SU-E2E-095 | FE+BE |
| TC-AC-SU-343 | TC-AC-SU-E2E-096 | FE+BE |
| TC-AC-SU-344 | TC-AC-SU-E2E-096 | FE+BE |
| TC-AC-SU-345 | TC-AC-SU-E2E-096 | FE+BE |
| TC-AC-SU-346 | TC-AC-SU-E2E-097 | FE+BE |
| TC-AC-SU-347 | TC-AC-SU-E2E-097 | FE+BE |
| TC-AC-SU-348 | TC-AC-SU-E2E-097 | FE+BE |
| TC-AC-SU-349 | TC-AC-SU-E2E-097 | FE+BE |
| TC-AC-SU-350 | TC-AC-SU-E2E-098 | FE+BE |
| TC-AC-SU-351 | TC-AC-SU-E2E-098 | FE+BE |
| TC-AC-SU-352 | TC-AC-SU-E2E-098 | FE+BE |
| TC-AC-SU-353 | TC-AC-SU-E2E-099 | FE+BE |
| TC-AC-SU-354 | TC-AC-SU-E2E-099 | FE+BE |
| TC-AC-SU-355 | TC-AC-SU-E2E-099 | FE+BE |
| TC-AC-SU-356 | TC-AC-SU-E2E-100 | FE+BE |
| TC-AC-SU-357 | TC-AC-SU-E2E-100 | FE+BE |
| TC-AC-SU-358 | TC-AC-SU-E2E-100 | FE+BE |
| TC-AC-SU-359 | TC-AC-SU-E2E-100 | FE+BE |
| TC-AC-SU-360 | TC-AC-SU-E2E-101 | FE+BE |
| TC-AC-SU-361 | TC-AC-SU-E2E-101 | FE+BE |
| TC-AC-SU-362 | TC-AC-SU-E2E-101 | FE+BE |
| TC-AC-SU-363 | TC-AC-SU-E2E-101 | FE+BE |
| TC-AC-SU-364 | TC-AC-SU-E2E-102 | FE+BE |
| TC-AC-SU-365 | TC-AC-SU-E2E-102, TC-AC-SU-E2E-195 | FE+BE |
| TC-AC-SU-366 | TC-AC-SU-E2E-180 | FE+BE |
| TC-AC-SU-367 | TC-AC-SU-E2E-026 | FE+BE |
| TC-AC-SU-368 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-369 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-370 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-371 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-372 | TC-AC-SU-E2E-179 | FE+BE |
| TC-AC-SU-373 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-374 | TC-AC-SU-E2E-104 | FE+BE |
| TC-AC-SU-375 | TC-AC-SU-E2E-104 | FE+BE |
| TC-AC-SU-376 | TC-AC-SU-E2E-104 | FE+BE |
| TC-AC-SU-377 | TC-AC-SU-E2E-103 | FE+BE |
| TC-AC-SU-378 | TC-AC-SU-E2E-105 | FE+BE |
| TC-AC-SU-379 | TC-AC-SU-E2E-105 | FE+BE |
| TC-AC-SU-380 | TC-AC-SU-E2E-106 | FE+BE |
| TC-AC-SU-381 | TC-AC-SU-E2E-106 | FE+BE |
| TC-AC-SU-382 | TC-AC-SU-E2E-107 | FE+BE |
| TC-AC-SU-383 | TC-AC-SU-E2E-107 | FE+BE |
| TC-AC-SU-384 | TC-AC-SU-E2E-107 | FE+BE |
| TC-AC-SU-385 | TC-AC-SU-E2E-107 | FE+BE |
| TC-AC-SU-386 | TC-AC-SU-E2E-108 | FE+BE |
| TC-AC-SU-387 | TC-AC-SU-E2E-108 | FE+BE |
| TC-AC-SU-388 | TC-AC-SU-E2E-108 | FE+BE |
| TC-AC-SU-389 | TC-AC-SU-E2E-109 | FE+BE |
| TC-AC-SU-390 | TC-AC-SU-E2E-109 | FE+BE |
| TC-AC-SU-391 | TC-AC-SU-E2E-109 | FE+BE |
| TC-AC-SU-392 | TC-AC-SU-E2E-110 | FE+BE |
| TC-AC-SU-393 | TC-AC-SU-E2E-110 | FE+BE |
| TC-AC-SU-394 | TC-AC-SU-E2E-110 | FE+BE |
| TC-AC-SU-395 | TC-AC-SU-E2E-110 | FE+BE |
| TC-AC-SU-396 | TC-AC-SU-E2E-111 | FE+BE |
| TC-AC-SU-397 | TC-AC-SU-E2E-111 | FE+BE |
| TC-AC-SU-398 | TC-AC-SU-E2E-111 | FE+BE |
| TC-AC-SU-399 | TC-AC-SU-E2E-111 | FE+BE |
| TC-AC-SU-400 | TC-AC-SU-E2E-112 | FE+BE |
| TC-AC-SU-401 | TC-AC-SU-E2E-195 | FE+BE |
| TC-AC-SU-402 | TC-AC-SU-E2E-180 | FE+BE |
| TC-AC-SU-403 | TC-AC-SU-E2E-026 | FE+BE |
| TC-AC-SU-404 | TC-AC-SU-E2E-113 | FE+BE |
| TC-AC-SU-405 | TC-AC-SU-E2E-113 | FE+BE |
| TC-AC-SU-406 | TC-AC-SU-E2E-113 | FE+BE |
| TC-AC-SU-407 | TC-AC-SU-E2E-179 | FE+BE |
| TC-AC-SU-408 | TC-AC-SU-E2E-113 | FE+BE |
| TC-AC-SU-409 | TC-AC-SU-E2E-114 | FE+BE |
| TC-AC-SU-410 | TC-AC-SU-E2E-114 | FE+BE |
| TC-AC-SU-411 | TC-AC-SU-E2E-115 | FE+BE |
| TC-AC-SU-412 | TC-AC-SU-E2E-196 | FE+BE |
| TC-AC-SU-413 | TC-AC-SU-E2E-115 | FE+BE |
| TC-AC-SU-414 | TC-AC-SU-E2E-116 | FE+BE |
| TC-AC-SU-415 | TC-AC-SU-E2E-116 | FE+BE |
| TC-AC-SU-416 | TC-AC-SU-E2E-204 | FE+BE |
| TC-AC-SU-417 | TC-AC-SU-E2E-205 | FE+BE |
| TC-AC-SU-418 | TC-AC-SU-E2E-117 | FE+BE |
| TC-AC-SU-419 | TC-AC-SU-E2E-117 | FE+BE |
| TC-AC-SU-420 | TC-AC-SU-E2E-118 | FE+BE |
| TC-AC-SU-421 | TC-AC-SU-E2E-118 | FE+BE |
| TC-AC-SU-422 | TC-AC-SU-E2E-119 | FE+BE |
| TC-AC-SU-423 | TC-AC-SU-E2E-195 | FE+BE |
| TC-AC-SU-424 | TC-AC-SU-E2E-181 | FE+BE |
| TC-AC-SU-425 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-426 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-427 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-428 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-429 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-430 | TC-AC-SU-E2E-179 | FE+BE |
| TC-AC-SU-431 | TC-AC-SU-E2E-120 | FE+BE |
| TC-AC-SU-432 | TC-AC-SU-E2E-121 | FE+BE |
| TC-AC-SU-433 | TC-AC-SU-E2E-121 | FE+BE |
| TC-AC-SU-434 | TC-AC-SU-E2E-122 | FE+BE |
| TC-AC-SU-435 | TC-AC-SU-E2E-122 | FE+BE |
| TC-AC-SU-436 | TC-AC-SU-E2E-123 | FE+BE |
| TC-AC-SU-437 | TC-AC-SU-E2E-123 | FE+BE |
| TC-AC-SU-438 | TC-AC-SU-E2E-124 | FE+BE |
| TC-AC-SU-439 | TC-AC-SU-E2E-195 | FE+BE |
| TC-AC-SU-440 | TC-AC-SU-E2E-181 | FE+BE |
| TC-AC-SU-441 | TC-AC-SU-E2E-125 | FE+BE |
| TC-AC-SU-442 | TC-AC-SU-E2E-125 | FE+BE |
| TC-AC-SU-443 | TC-AC-SU-E2E-126 | FE+BE |
| TC-AC-SU-444 | TC-AC-SU-E2E-126 | FE+BE |
| TC-AC-SU-445 | TC-AC-SU-E2E-126 | FE+BE |
| TC-AC-SU-446 | TC-AC-SU-E2E-126 | FE+BE |
| TC-AC-SU-447 | TC-AC-SU-E2E-200 | FE+BE |
| TC-AC-SU-448 | TC-AC-SU-E2E-126 | FE+BE |
| TC-AC-SU-449 | TC-AC-SU-E2E-127 | FE+BE |
| TC-AC-SU-450 | TC-AC-SU-E2E-127 | FE+BE |
| TC-AC-SU-451 | TC-AC-SU-E2E-127 | FE+BE |
| TC-AC-SU-452 | TC-AC-SU-E2E-128 | FE+BE |
| TC-AC-SU-453 | TC-AC-SU-E2E-128 | FE+BE |
| TC-AC-SU-454 | TC-AC-SU-E2E-129 | FE+BE |
| TC-AC-SU-455 | TC-AC-SU-E2E-129 | FE+BE |
| TC-AC-SU-456 | TC-AC-SU-E2E-130 | FE+BE |
| TC-AC-SU-457 | TC-AC-SU-E2E-130 | FE+BE |
| TC-AC-SU-458 | TC-AC-SU-E2E-131 | FE+BE |
| TC-AC-SU-459 | TC-AC-SU-E2E-131 | FE+BE |
| TC-AC-SU-460 | TC-AC-SU-E2E-131 | FE+BE |
| TC-AC-SU-461 | TC-AC-SU-E2E-132 | FE+BE |
| TC-AC-SU-462 | TC-AC-SU-E2E-132 | FE+BE |
| TC-AC-SU-463 | TC-AC-SU-E2E-132 | FE+BE |
| TC-AC-SU-464 | TC-AC-SU-E2E-133 | FE+BE |
| TC-AC-SU-465 | TC-AC-SU-E2E-133 | FE+BE |
| TC-AC-SU-466 | TC-AC-SU-E2E-133 | FE+BE |
| TC-AC-SU-467 | TC-AC-SU-E2E-134 | FE+BE |
| TC-AC-SU-468 | TC-AC-SU-E2E-134 | FE+BE |
| TC-AC-SU-469 | TC-AC-SU-E2E-134 | FE+BE |
| TC-AC-SU-470 | TC-AC-SU-E2E-135 | FE+BE |
| TC-AC-SU-471 | TC-AC-SU-E2E-135 | FE+BE |
| TC-AC-SU-472 | TC-AC-SU-E2E-135 | FE+BE |
| TC-AC-SU-473 | TC-AC-SU-E2E-136 | FE+BE |
| TC-AC-SU-474 | TC-AC-SU-E2E-136 | FE+BE |
| TC-AC-SU-475 | TC-AC-SU-E2E-198 | FE+BE |
| TC-AC-SU-476 | TC-AC-SU-E2E-137 | FE+BE |
| TC-AC-SU-477 | TC-AC-SU-E2E-197 | FE+BE |
| TC-AC-SU-478 | TC-AC-SU-E2E-181 | FE+BE |
| TC-AC-SU-479 | TC-AC-SU-E2E-137 | FE+BE |
| TC-AC-SU-480 | TC-AC-SU-E2E-138 | FE+BE |
| TC-AC-SU-481 | TC-AC-SU-E2E-138 | FE+BE |
| TC-AC-SU-482 | TC-AC-SU-E2E-138 | FE+BE |
| TC-AC-SU-483 | TC-AC-SU-E2E-200 | FE+BE |
| TC-AC-SU-484 | TC-AC-SU-E2E-138 | FE+BE |
| TC-AC-SU-485 | TC-AC-SU-E2E-139 | FE+BE |
| TC-AC-SU-486 | TC-AC-SU-E2E-139 | FE+BE |
| TC-AC-SU-487 | TC-AC-SU-E2E-139 | FE+BE |
| TC-AC-SU-488 | TC-AC-SU-E2E-140 | FE+BE |
| TC-AC-SU-489 | TC-AC-SU-E2E-140 | FE+BE |
| TC-AC-SU-490 | TC-AC-SU-E2E-140 | FE+BE |
| TC-AC-SU-491 | TC-AC-SU-E2E-141 | FE+BE |
| TC-AC-SU-492 | TC-AC-SU-E2E-141 | FE+BE |
| TC-AC-SU-493 | TC-AC-SU-E2E-141 | FE+BE |
| TC-AC-SU-494 | TC-AC-SU-E2E-141 | FE+BE |
| TC-AC-SU-495 | TC-AC-SU-E2E-142 | FE+BE |
| TC-AC-SU-496 | TC-AC-SU-E2E-142 | FE+BE |
| TC-AC-SU-497 | TC-AC-SU-E2E-142 | FE+BE |
| TC-AC-SU-498 | TC-AC-SU-E2E-142 | FE+BE |
| TC-AC-SU-499 | TC-AC-SU-E2E-143 | FE+BE |
| TC-AC-SU-500 | TC-AC-SU-E2E-143 | FE+BE |
| TC-AC-SU-501 | TC-AC-SU-E2E-206 | FE+BE |
| TC-AC-SU-502 | TC-AC-SU-E2E-206 | FE+BE |
| TC-AC-SU-503 | TC-AC-SU-E2E-144 | FE+BE |
| TC-AC-SU-504 | TC-AC-SU-E2E-138 | FE+BE |
| TC-AC-SU-505 | TC-AC-SU-E2E-145 | FE+BE |
| TC-AC-SU-506 | TC-AC-SU-E2E-145 | FE+BE |
| TC-AC-SU-507 | TC-AC-SU-E2E-200 | FE+BE |
| TC-AC-SU-508 | TC-AC-SU-E2E-145 | FE+BE |
| TC-AC-SU-509 | TC-AC-SU-E2E-146 | FE+BE |
| TC-AC-SU-510 | TC-AC-SU-E2E-146 | FE+BE |
| TC-AC-SU-511 | TC-AC-SU-E2E-146 | FE+BE |
| TC-AC-SU-512 | TC-AC-SU-E2E-147 | FE+BE |
| TC-AC-SU-513 | TC-AC-SU-E2E-148 | FE+BE |
| TC-AC-SU-514 | TC-AC-SU-E2E-148 | FE+BE |
| TC-AC-SU-515 | TC-AC-SU-E2E-149 | FE+BE |
| TC-AC-SU-516 | TC-AC-SU-E2E-149 | FE+BE |
| TC-AC-SU-517 | TC-AC-SU-E2E-149 | FE+BE |
| TC-AC-SU-518 | TC-AC-SU-E2E-149 | FE+BE |
| TC-AC-SU-519 | TC-AC-SU-E2E-150 | FE+BE |
| TC-AC-SU-520 | TC-AC-SU-E2E-150 | FE+BE |
| TC-AC-SU-521 | TC-AC-SU-E2E-151 | FE+BE |
| TC-AC-SU-522 | TC-AC-SU-E2E-151 | FE+BE |
| TC-AC-SU-523 | TC-AC-SU-E2E-151 | FE+BE |
| TC-AC-SU-524 | TC-AC-SU-E2E-152 | FE+BE |
| TC-AC-SU-525 | TC-AC-SU-E2E-152 | FE+BE |
| TC-AC-SU-526 | TC-AC-SU-E2E-152 | FE+BE |
| TC-AC-SU-527 | TC-AC-SU-E2E-153 | FE+BE |
| TC-AC-SU-528 | TC-AC-SU-E2E-153 | FE+BE |
| TC-AC-SU-529 | TC-AC-SU-E2E-154 | FE+BE |
| TC-AC-SU-530 | TC-AC-SU-E2E-145 | FE+BE |
| TC-AC-SU-531 | TC-AC-SU-E2E-155 | FE+BE |
| TC-AC-SU-532 | TC-AC-SU-E2E-155 | FE+BE |
| TC-AC-SU-533 | TC-AC-SU-E2E-155 | FE+BE |
| TC-AC-SU-534 | TC-AC-SU-E2E-155 | FE+BE |
| TC-AC-SU-535 | TC-AC-SU-E2E-156 | FE+BE |
| TC-AC-SU-536 | TC-AC-SU-E2E-156 | FE+BE |
| TC-AC-SU-537 | TC-AC-SU-E2E-156 | FE+BE |
| TC-AC-SU-538 | TC-AC-SU-E2E-157 | FE+BE |
| TC-AC-SU-539 | TC-AC-SU-E2E-157 | FE+BE |
| TC-AC-SU-540 | TC-AC-SU-E2E-157 | FE+BE |
| TC-AC-SU-541 | TC-AC-SU-E2E-158 | FE+BE |
| TC-AC-SU-542 | TC-AC-SU-E2E-158 | FE+BE |
| TC-AC-SU-543 | TC-AC-SU-E2E-158 | FE+BE |
| TC-AC-SU-544 | TC-AC-SU-E2E-159 | FE+BE |
| TC-AC-SU-545 | TC-AC-SU-E2E-159 | FE+BE |
| TC-AC-SU-546 | TC-AC-SU-E2E-161 | FE+BE |
| TC-AC-SU-547 | TC-AC-SU-E2E-160 | FE+BE |
| TC-AC-SU-548 | TC-AC-SU-E2E-160 | FE+BE |
| TC-AC-SU-549 | TC-AC-SU-E2E-160 | FE+BE |
| TC-AC-SU-550 | TC-AC-SU-E2E-162 | FE+BE |
| TC-AC-SU-551 | TC-AC-SU-E2E-162 | FE+BE |
| TC-AC-SU-552 | TC-AC-SU-E2E-162 | FE+BE |
| TC-AC-SU-553 | TC-AC-SU-E2E-208 | FE+BE |
| TC-AC-SU-554 | TC-AC-SU-E2E-208 | FE+BE |
| TC-AC-SU-555 | TC-AC-SU-E2E-208 | FE+BE |
| TC-AC-SU-556 | TC-AC-SU-E2E-208 | FE+BE |
| TC-AC-SU-557 | TC-AC-SU-E2E-163 | FE+BE |
| TC-AC-SU-558 | TC-AC-SU-E2E-163 | FE+BE |
| TC-AC-SU-559 | TC-AC-SU-E2E-163 | FE+BE |
| TC-AC-SU-560 | TC-AC-SU-E2E-209 | FE+BE |
| TC-AC-SU-561 | TC-AC-SU-E2E-209 | FE+BE |
| TC-AC-SU-562 | TC-AC-SU-E2E-209 | FE+BE |
| TC-AC-SU-563 | TC-AC-SU-E2E-209 | FE+BE |
| TC-AC-SU-564 | TC-AC-SU-E2E-164 | FE+BE |
| TC-AC-SU-565 | TC-AC-SU-E2E-166 | FE+BE |
| TC-AC-SU-566 | TC-AC-SU-E2E-166 | FE+BE |
| TC-AC-SU-567 | TC-AC-SU-E2E-166 | FE+BE |
| TC-AC-SU-568 | TC-AC-SU-E2E-167 | FE+BE |
| TC-AC-SU-569 | TC-AC-SU-E2E-167 | FE+BE |
| TC-AC-SU-570 | TC-AC-SU-E2E-167 | FE+BE |
| TC-AC-SU-571 | TC-AC-SU-E2E-168 | FE+BE |
| TC-AC-SU-572 | TC-AC-SU-E2E-164 | FE+BE |
| TC-AC-SU-573 | TC-AC-SU-E2E-164 | FE+BE |
| TC-AC-SU-574 | TC-AC-SU-E2E-164 | FE+BE |
| TC-AC-SU-575 | TC-AC-SU-E2E-165 | FE+BE |
| TC-AC-SU-576 | TC-AC-SU-E2E-037 | FE+BE |
| TC-AC-SU-577 | TC-AC-SU-E2E-185 | FE+BE |
| TC-AC-SU-578 | TC-AC-SU-E2E-165 | FE+BE |
| TC-AC-SU-579 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-580 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-581 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-582 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-583 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-584 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-585 | TC-AC-SU-E2E-170 | FE+BE |
| TC-AC-SU-586 | TC-AC-SU-E2E-199 | FE+BE |
| TC-AC-SU-587 | TC-AC-SU-E2E-170 | FE+BE |
| TC-AC-SU-588 | TC-AC-SU-E2E-171 | FE+BE |
| TC-AC-SU-589 | TC-AC-SU-E2E-171 | FE+BE |
| TC-AC-SU-590 | TC-AC-SU-E2E-171 | FE+BE |
| TC-AC-SU-591 | TC-AC-SU-E2E-172 | FE+BE |
| TC-AC-SU-592 | TC-AC-SU-E2E-172 | FE+BE |
| TC-AC-SU-593 | TC-AC-SU-E2E-172 | FE+BE |
| TC-AC-SU-594 | TC-AC-SU-E2E-172 | FE+BE |
| TC-AC-SU-595 | TC-AC-SU-E2E-173 | FE+BE |
| TC-AC-SU-596 | TC-AC-SU-E2E-173 | FE+BE |
| TC-AC-SU-597 | TC-AC-SU-E2E-173 | FE+BE |
| TC-AC-SU-598 | TC-AC-SU-E2E-174 | FE+BE |
| TC-AC-SU-599 | TC-AC-SU-E2E-174 | FE+BE |
| TC-AC-SU-600 | TC-AC-SU-E2E-174 | FE+BE |
| TC-AC-SU-601 | TC-AC-SU-E2E-199 | FE+BE |
| TC-AC-SU-602 | TC-AC-SU-E2E-161 | FE+BE |
| TC-AC-SU-603 | TC-AC-SU-E2E-044 | FE+BE |
| TC-AC-SU-604 | TC-AC-SU-E2E-044 | FE+BE |
| TC-AC-SU-605 | TC-AC-SU-E2E-175 | FE+BE |
| TC-AC-SU-606 | TC-AC-SU-E2E-175 | FE+BE |
| TC-AC-SU-607 | TC-AC-SU-E2E-175 | FE+BE |
| TC-AC-SU-608 | TC-AC-SU-E2E-091 | FE+BE |
| TC-AC-SU-609 | TC-AC-SU-E2E-092 | FE+BE |
| TC-AC-SU-610 | TC-AC-SU-E2E-092 | FE+BE |
| TC-AC-SU-611 | TC-AC-SU-E2E-092 | FE+BE |
| TC-AC-SU-612 | TC-AC-SU-E2E-092 | FE+BE |
| TC-AC-SU-613 | TC-AC-SU-E2E-092 | FE+BE |
| TC-AC-SU-614 | TC-AC-SU-E2E-182 | FE+BE |
| TC-AC-SU-615 | TC-AC-SU-E2E-182, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-616 | TC-AC-SU-E2E-182, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-617 | TC-AC-SU-E2E-182, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-618 | TC-AC-SU-E2E-182 | FE+BE |
| TC-AC-SU-619 | TC-AC-SU-E2E-182 | FE+BE |
| TC-AC-SU-620 | TC-AC-SU-E2E-183, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-621 | TC-AC-SU-E2E-183, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-622 | TC-AC-SU-E2E-183 | FE+BE |
| TC-AC-SU-623 | TC-AC-SU-E2E-044 | FE+BE |
| TC-AC-SU-624 | TC-AC-SU-E2E-183 | FE+BE |
| TC-AC-SU-625 | TC-AC-SU-E2E-184 | FE+BE |
| TC-AC-SU-626 | TC-AC-SU-E2E-184 | FE+BE |
| TC-AC-SU-627 | TC-AC-SU-E2E-184 | FE+BE |
| TC-AC-SU-628 | TC-AC-SU-E2E-186 | FE+BE |
| TC-AC-SU-629 | TC-AC-SU-E2E-186 | FE+BE |
| TC-AC-SU-630 | TC-AC-SU-E2E-187 | FE+BE |
| TC-AC-SU-631 | TC-AC-SU-E2E-187 | FE+BE |
| TC-AC-SU-632 | TC-AC-SU-E2E-187 | FE+BE |
| TC-AC-SU-633 | TC-AC-SU-E2E-054 | FE+BE |
| TC-AC-SU-634 | TC-AC-SU-E2E-184 | FE+BE |
| TC-AC-SU-635 | TC-AC-SU-E2E-177 | FE+BE |
| TC-AC-SU-636 | TC-AC-SU-E2E-188 | FE+BE |
| TC-AC-SU-637 | TC-AC-SU-E2E-188 | FE+BE |
| TC-AC-SU-638 | TC-AC-SU-E2E-188 | FE+BE |
| TC-AC-SU-639 | TC-AC-SU-E2E-188 | FE+BE |
| TC-AC-SU-640 | TC-AC-SU-E2E-161 | FE+BE |
| TC-AC-SU-641 | TC-AC-SU-E2E-169 | FE+BE |
| TC-AC-SU-642 | TC-AC-SU-E2E-168 | FE+BE |
| TC-AC-SU-643 | TC-AC-SU-E2E-174 | FE+BE |
| TC-AC-SU-644 | TC-AC-SU-E2E-073 | FE+BE |
| TC-AC-SU-645 | TC-AC-SU-E2E-053 | FE+BE |
| TC-AC-SU-646 | TC-AC-SU-E2E-144 | FE+BE |
| TC-AC-SU-647 | TC-AC-SU-E2E-181 | FE+BE |
| TC-AC-SU-648 | TC-AC-SU-E2E-076 | FE+BE |
| TC-AC-SU-649 | TC-AC-SU-E2E-078 | FE+BE |
| TC-AC-SU-650 | TC-AC-SU-E2E-159 | FE+BE |
| TC-AC-SU-651 | TC-AC-SU-E2E-037 | FE+BE |
| TC-AC-SU-652 | TC-AC-SU-E2E-036 | FE+BE |
| TC-AC-SU-653 | TC-AC-SU-E2E-117 | FE+BE |
| TC-AC-SU-654 | TC-AC-SU-E2E-113 | FE+BE |
| TC-AC-SU-656 | TC-AC-SU-E2E-083 | FE+BE |
| TC-AC-SU-657 | TC-AC-SU-E2E-069 | FE+BE |
| TC-AC-SU-658 | TC-AC-SU-E2E-097 | FE+BE |
| TC-AC-SU-659 | TC-AC-SU-E2E-076 | FE+BE |
| TC-AC-SU-660 | TC-AC-SU-E2E-064 | FE+BE |
| TC-AC-SU-661 | TC-AC-SU-E2E-088, TC-AC-SU-E2E-089 | FE+BE |
| TC-AC-SU-662 | TC-AC-SU-E2E-069 | FE+BE |
| TC-AC-SU-663 | TC-AC-SU-E2E-189 | FE+BE |
| TC-AC-SU-664 | TC-AC-SU-E2E-002 | FE+BE |
| TC-AC-SU-665 | TC-AC-SU-E2E-183, TC-AC-SU-E2E-207 | FE+BE |
| TC-AC-SU-666 | TC-AC-SU-E2E-051 | FE+BE |
| TC-AC-SU-667 | TC-AC-SU-E2E-091 | FE+BE |
