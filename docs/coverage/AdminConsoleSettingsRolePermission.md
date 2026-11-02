# Coverage E2E — Admin Console > Settings > Role & Permission

Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md` (443 TC granular aktif; seluruhnya TC FE).
File backend `tc-settings-role-permission-backend.md` hanya dicek keberadaannya untuk mengenali TC yang tidak punya antarmuka; tidak ada TC seperti itu.
Suite: `specs/AdminConsole/SettingsRolePermission/`.
Prefix Modul: `AC` + `RP` (`TC-AC-RP-E2E-*`). `executionOrder: 1.1`, suite serial (`parallel: false`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (138 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | Screening Tab Total Control: Layout Halaman, Kolom Default, Isi Baris, Badge Status, dan Hover Modified By | FE+BE | 31 | TC-AC-RP-1, TC-AC-RP-2, TC-AC-RP-3, TC-AC-RP-4, TC-AC-RP-5, TC-AC-RP-6 |
| TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled | Screening Tab Total Control: Overlay Row Action dan Remove Disabled dengan Tooltip | FE+BE | 23 | TC-AC-RP-7, TC-AC-RP-8, TC-AC-RP-9, TC-AC-RP-10 |
| TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama | Screening Tab Total Control: Tooltip Toolbar, Breadcrumb per Tab, Tanpa Bulk Action, dan Klik Name | FE+BE | 24 | TC-AC-RP-11, TC-AC-RP-12, TC-AC-RP-13, TC-AC-RP-14 |
| TC-AC-RP-E2E-004-screening-tab-read-only | Screening Tab Read Only: Toolbar, Kolom, Baris, Row Action, dan Placeholder Search | FE+BE | 16 | TC-AC-RP-15, TC-AC-RP-16, TC-AC-RP-17 |
| TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree | Screening Tab Group Manager dan Sidebar Group Tree: Baris, Hover Path, dan Node | FE+BE | 19 | TC-AC-RP-18, TC-AC-RP-19, TC-AC-RP-20, TC-AC-RP-21 |
| TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | Sidebar Group Tree: Filter Node, Node Aktif, Collapse, dan Eksklusi Pemegang Tingkat Akses | FE+BE | 31 | TC-AC-RP-22, TC-AC-RP-23, TC-AC-RP-24, TC-AC-RP-25, TC-AC-RP-26 |
| TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role | Screening Tab System: Dua Section, Urutan Katalog dan Jumlah Users, serta Link Role Detail | FE+BE | 19 | TC-AC-RP-27, TC-AC-RP-28, TC-AC-RP-29, TC-AC-RP-30 |
| TC-AC-RP-E2E-008-katalog-tab-system-distributor-dan-partner | Katalog Tab System per Entitas: Role yang Berlaku untuk Distributor dan Partner | FE+BE | 14 | TC-AC-RP-31, TC-AC-RP-32, TC-AC-RP-33 |
| TC-AC-RP-E2E-009-screening-role-detail-global-role | Screening Role Detail Global Role: Header, Kolom, Baris CRUD, Kolom R Disabled, dan Sel Tidak Berlaku | FE+BE | 27 | TC-AC-RP-34, TC-AC-RP-35, TC-AC-RP-36, TC-AC-RP-37 |
| TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | Role Detail Global Role: Breadcrumb, Manage TAG stock Principal, dan Approvers Section | FE+BE | 26 | TC-AC-RP-39, TC-AC-RP-41, TC-AC-RP-42, TC-AC-RP-43, TC-AC-RP-45 |
| TC-AC-RP-E2E-011-role-detail-varian-distributor | Role Detail Varian Entitas Distributor: Manage TAG stock, Manage hardware stock, dan Tanpa Approvers Section | FE+BE | 23 | TC-AC-RP-40, TC-AC-RP-44, TC-AC-RP-430 |
| TC-AC-RP-E2E-012-screening-role-detail-group-role | Screening Role Detail Group Role: Kolom, Sidebar Group Tree, Exact Match Node, dan Empty State | FE+BE | 22 | TC-AC-RP-46, TC-AC-RP-47, TC-AC-RP-48, TC-AC-RP-49 |
| TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | Role Detail Group Role: Approval Settings Manage allocation dan Manage wallet & pricing | FE+BE | 25 | TC-AC-RP-51, TC-AC-RP-52, TC-AC-RP-53, TC-AC-RP-54, TC-AC-RP-55 |
| TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail | Resilience Baca: Loading dan Error Load Tab Total Control dan Role Detail | FE+BE (intercept) | 32 | TC-AC-RP-56, TC-AC-RP-57, TC-AC-RP-58, TC-AC-RP-59 |
| TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | Empty State Tab Read Only, Group Manager, dan Total Control serta Search Tanpa Hasil | FE+BE | 19 | TC-AC-RP-60, TC-AC-RP-61, TC-AC-RP-62, TC-AC-RP-63, TC-AC-RP-64 |
| TC-AC-RP-E2E-016-guided-tooltip-replay-guide | Guided Tooltip: Tombol Replay Guide dan Tour per Tab Aktif | FE+BE | 21 | TC-AC-RP-65, TC-AC-RP-66, TC-AC-RP-67 |
| TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | Mobile Android: Card List, Bottom Sheet, Chip Group, dan Accordion Tab System | FE+BE | 33 | TC-AC-RP-68, TC-AC-RP-69, TC-AC-RP-70, TC-AC-RP-71, TC-AC-RP-72 |
| TC-AC-RP-E2E-018-mobile-role-detail-dan-approval-settings-android | Mobile Android: Role Detail Global (Checkbox Inline, Long Press) dan Approval Settings | FE+BE | 33 | TC-AC-RP-73, TC-AC-RP-74, TC-AC-RP-75 |
| TC-AC-RP-E2E-019-mobile-selection-mode-android | Mobile Android: Selection Mode Role Detail, Checkbox CRUD Inert dan Ketuk Card | FE+BE | 20 | TC-AC-RP-427 |
| TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | Role Matrix: Akses Menu Role & Permission per Entitas dan Role (Positif) | FE+BE | 34 | TC-AC-RP-76, TC-AC-RP-77, TC-AC-RP-78, TC-AC-RP-82, TC-AC-RP-83 |
| TC-AC-RP-E2E-021-role-matrix-akses-menu-negatif | Role Matrix: Akses Menu dan URL Langsung Ditolak 403 (Negatif) | FE+BE | 24 | TC-AC-RP-79, TC-AC-RP-80, TC-AC-RP-81 |
| TC-AC-RP-E2E-022-role-matrix-visibilitas-tab-per-role | Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Default User dan Total Control | FE+BE | 30 | TC-AC-RP-84, TC-AC-RP-87 |
| TC-AC-RP-E2E-023-role-matrix-visibilitas-role-detail-positif | Role Matrix: Visibilitas Role Detail untuk Total Control dan Manage user and role (Update) | FE+BE | 26 | TC-AC-RP-88, TC-AC-RP-94 |
| TC-AC-RP-E2E-024-role-matrix-visibilitas-role-detail-negatif | Role Matrix: Visibilitas Role Detail untuk Default User, Read Only, dan Manage user and role tanpa Update | FE+BE | 32 | TC-AC-RP-85, TC-AC-RP-91, TC-AC-RP-97 |
| TC-AC-RP-E2E-025-role-matrix-visibilitas-approval-settings-positif | Role Matrix: Visibilitas Approval Settings Manage allocation untuk Total Control dan Manage user and role (Update) | FE+BE | 24 | TC-AC-RP-89, TC-AC-RP-95 |
| TC-AC-RP-E2E-026-role-matrix-visibilitas-approval-settings-negatif | Role Matrix: Visibilitas Approval Settings Manage allocation untuk Default User, Read Only, dan Manage user and role tanpa Update | FE+BE | 39 | TC-AC-RP-86, TC-AC-RP-92, TC-AC-RP-98 |
| TC-AC-RP-E2E-027-role-matrix-approvers-section-dan-row-action-detail | Role Matrix: Approvers Section Manage TAG stock dan Row Action Detail Tab System | FE+BE | 21 | TC-AC-RP-99, TC-AC-RP-100, TC-AC-RP-101 |
| TC-AC-RP-E2E-028-gating-checkbox-crud-total-control | Gating Checkbox CRUD Aktor Total Control: Target Standard, TC, RO, GM-target, Default User, dan Diri Sendiri | FE+BE | 15 | TC-AC-RP-102, TC-AC-RP-103, TC-AC-RP-104, TC-AC-RP-105 |
| TC-AC-RP-E2E-029-checkbox-crud-in-flight-dan-keyboard | Checkbox CRUD: Nonaktif Sementara saat In-flight dan Operasi Keyboard | FE+BE (intercept) | 17 | TC-AC-RP-113, TC-AC-RP-114 |
| TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | Gating Checkbox CRUD Aktor Manage user and role: Target Standard, TC, RO, GM-target, dan Prioritas Tooltip | FE+BE | 16 | TC-AC-RP-107, TC-AC-RP-108, TC-AC-RP-109, TC-AC-RP-110, TC-AC-RP-112 |
| TC-AC-RP-E2E-031-gating-checkbox-crud-default-user-dan-read-only | Gating Checkbox CRUD Aktor Default User dan Read Only: Tooltip dan Prioritas | FE+BE | 14 | TC-AC-RP-106, TC-AC-RP-111 |
| TC-AC-RP-E2E-032-gating-remove-role-detail-dan-select-all | Gating Remove dan Select All Role Detail untuk Aktor Manage user and role | FE+BE | 35 | TC-AC-RP-115, TC-AC-RP-116, TC-AC-RP-119 |
| TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | Assign Total Control: Screening Popup, Pool Kandidat, Validasi Diblokir, Cancel, dan Escape | FE+BE | 34 | TC-AC-RP-120, TC-AC-RP-121, TC-AC-RP-128, TC-AC-RP-129, TC-AC-RP-130 |
| TC-AC-RP-E2E-034-assign-total-control-user-standard-dan-seluruh-global-role | Assign Total Control: User Standard Muncul di Tab dan di Role Detail Seluruh Global Role | FE+BE | 16 | TC-AC-RP-122 |
| TC-AC-RP-E2E-035-assign-total-control-beralih-dari-tingkat-akses-lain | Assign Total Control: Beralih dari Read Only dan dari Group Manager | FE+BE | 20 | TC-AC-RP-125, TC-AC-RP-126 |
| TC-AC-RP-E2E-036-remove-total-control | Remove Total Control: Screening Dialog, Cancel, Escape, Confirm Reset Peran, dan User Inactive | FE+BE | 37 | TC-AC-RP-132, TC-AC-RP-133, TC-AC-RP-134, TC-AC-RP-135, TC-AC-RP-136 |
| TC-AC-RP-E2E-037-assign-read-only-screening-validasi-dan-assign | Assign Read Only: Screening Popup, Total Control Tidak Dapat Dijadikan Read Only, dan Assign User Standard | FE+BE | 20 | TC-AC-RP-138, TC-AC-RP-139, TC-AC-RP-141 |
| TC-AC-RP-E2E-038-assign-read-only-dari-group-manager-dan-remove-read-only | Assign Read Only dari Group Manager dan Remove Read Only (Cancel lalu Confirm) | FE+BE | 26 | TC-AC-RP-140, TC-AC-RP-142, TC-AC-RP-143 |
| TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool | Assign Group Manager: Screening Popup, Tree Group, Pool Kandidat, dan Ganti Group | FE+BE | 26 | TC-AC-RP-146, TC-AC-RP-147, TC-AC-RP-148, TC-AC-RP-149 |
| TC-AC-RP-E2E-040-assign-group-manager-validasi-dan-empty-state | Assign Group Manager: Validasi Tanpa Group atau User dan Empty State Kandidat | FE+BE | 19 | TC-AC-RP-153, TC-AC-RP-154, TC-AC-RP-155 |
| TC-AC-RP-E2E-041-assign-group-manager-aksi-berhasil | Assign Group Manager: Happy Path, Child dengan Ancestor Ber-GM, dan User yang Sama di Group Kedua | FE+BE | 32 | TC-AC-RP-150, TC-AC-RP-151, TC-AC-RP-152 |
| TC-AC-RP-E2E-042-remove-group-manager | Remove Group Manager: Cancel, Confirm, dan Ancestor Tidak Menyentuh GM Descendant | FE+BE | 24 | TC-AC-RP-156, TC-AC-RP-157, TC-AC-RP-158 |
| TC-AC-RP-E2E-043-resilience-tulis-assign-dan-remove-total-control | Resilience Tulis: Assign Total Control Gagal 5xx atau Jaringan dan Remove Total Control Gagal 5xx | FE+BE (intercept) | 33 | TC-AC-RP-131, TC-AC-RP-137, TC-AC-RP-415 |
| TC-AC-RP-E2E-044-resilience-tulis-assign-user-edit-crud-dan-toggle | Resilience Tulis: Assign User to Role, Edit CRUD, dan Toggle Gagal 5xx | FE+BE (intercept) | 35 | TC-AC-RP-171, TC-AC-RP-175, TC-AC-RP-220 |
| TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool | Assign User to Role: Screening Popup Global Role dan Pool Kandidat per Aktor | FE+BE | 41 | TC-AC-RP-160, TC-AC-RP-161, TC-AC-RP-162, TC-AC-RP-412 |
| TC-AC-RP-E2E-046-assign-user-to-global-role-aksi-berhasil | Assign User to Global Role: Total Control, Manage user and role, dan Manage TAG stock Distributor | FE+BE | 29 | TC-AC-RP-163, TC-AC-RP-164, TC-AC-RP-431 |
| TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi | Assign User to Group Role: Field Group, Header Popup, Validasi, dan Tree Group | FE+BE | 27 | TC-AC-RP-165, TC-AC-RP-166, TC-AC-RP-167, TC-AC-RP-170 |
| TC-AC-RP-E2E-048-assign-user-to-group-role-aksi-berhasil | Assign User to Group Role: Group Berbeda dari Sidebar dan Pool per Group | FE+BE | 21 | TC-AC-RP-168, TC-AC-RP-169 |
| TC-AC-RP-E2E-049-edit-crud-autosave-target-standard | Edit CRUD Autosave: Check, Uncheck Target Standard, dan Group Role per Group | FE+BE | 19 | TC-AC-RP-172, TC-AC-RP-173, TC-AC-RP-174 |
| TC-AC-RP-E2E-050-edit-crud-auto-revert-total-control | Edit CRUD: Dialog Auto-Revert Total Control (Cancel lalu Confirm) | FE+BE | 26 | TC-AC-RP-176, TC-AC-RP-177, TC-AC-RP-178 |
| TC-AC-RP-E2E-051-edit-crud-auto-revert-read-only-dan-group-manager | Edit CRUD: Dialog Auto-Revert Read Only dan Group Manager | FE+BE | 28 | TC-AC-RP-179, TC-AC-RP-180 |
| TC-AC-RP-E2E-052-edit-crud-tanpa-auto-revert-dan-susun-ulang | Edit CRUD: Assignment Descendant, Peran Global Target GM, dan Susun Ulang Peran Manual Tanpa Auto-Revert | FE+BE | 31 | TC-AC-RP-181, TC-AC-RP-182, TC-AC-RP-183 |
| TC-AC-RP-E2E-053-remove-role-single-cancel-confirm-dan-group-role | Remove User dari Role Single: Cancel, Confirm, dan Group Role | FE+BE | 22 | TC-AC-RP-185, TC-AC-RP-186, TC-AC-RP-187 |
| TC-AC-RP-E2E-054-remove-role-single-auto-revert-tingkat-akses | Remove Role Single: Baris Total Control dan Baris GM-Target Memicu Auto-Revert dalam Satu Transaksi | FE+BE | 32 | TC-AC-RP-188, TC-AC-RP-189 |
| TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel | Bulk Remove Role Detail: Bulk Action Bar, Dialog Jamak dan Single, serta Cancel | FE+BE | 24 | TC-AC-RP-192, TC-AC-RP-193, TC-AC-RP-194, TC-AC-RP-200 |
| TC-AC-RP-E2E-056-bulk-remove-role-detail-berhasil-dan-campuran | Bulk Remove Role Detail: Dua Baris Standard dan Campuran Standard dan Total Control | FE+BE | 24 | TC-AC-RP-190, TC-AC-RP-191 |
| TC-AC-RP-E2E-057-bulk-remove-role-detail-stale-oleh-admin-lain | Bulk Remove Role Detail: Partial Success dan 0 Baris Berhasil karena Baris Berubah oleh Admin Lain | FE+BE | 26 | TC-AC-RP-195, TC-AC-RP-196 |
| TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver | Resilience Tulis: Remove Role Single dan Bulk Remove (Role Detail, Approver) Gagal 5xx atau Jaringan | FE+BE | 46 | TC-AC-RP-198, TC-AC-RP-199, TC-AC-RP-419, TC-AC-RP-420 |
| TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign | Additional Approver Global Role: Screening Popup, Pool, Assign oleh Total Control dan Manage user and role | FE+BE | 35 | TC-AC-RP-203, TC-AC-RP-204, TC-AC-RP-205, TC-AC-RP-413 |
| TC-AC-RP-E2E-060-assign-approver-group-role-dan-v09 | Additional Approver Group Role: Assign pada Group Aktif, Banyak Group, dan V-09 Sesi Lain | FE+BE | 31 | TC-AC-RP-206, TC-AC-RP-207, TC-AC-RP-422 |
| TC-AC-RP-E2E-061-remove-approver-single | Remove Additional Approver: Confirm Global Role, Cancel, Dialog Group Role, dan Aktor Me-Remove Baris Miliknya | FE+BE | 30 | TC-AC-RP-208, TC-AC-RP-209, TC-AC-RP-210, TC-AC-RP-439 |
| TC-AC-RP-E2E-062-bulk-remove-approver | Bulk Remove Approver: Banyak Baris, Satu Baris Memakai Dialog Single, dan Partial Success | FE+BE (intercept) | 25 | TC-AC-RP-211, TC-AC-RP-212, TC-AC-RP-213 |
| TC-AC-RP-E2E-063-resilience-tulis-approver | Resilience Tulis Approver: Bulk Remove, Assign, dan Remove Gagal 5xx | FE+BE (intercept) | 27 | TC-AC-RP-214, TC-AC-RP-215 |
| TC-AC-RP-E2E-064-toggle-require-approval-total-control | Toggle Require Approval oleh Total Control: Allocation dan Wallet Allocation, OFF ke ON dan Sebaliknya, Independen per Group | FE+BE (intercept) | 32 | TC-AC-RP-216, TC-AC-RP-217, TC-AC-RP-218, TC-AC-RP-219 |
| TC-AC-RP-E2E-065-toggle-require-approval-manage-user-and-role | Toggle Require Approval oleh Aktor Manage user and role (Update) | FE+BE (intercept) | 27 | TC-AC-RP-440, TC-AC-RP-441 |
| TC-AC-RP-E2E-066-table-user-picker-perilaku-umum | Table User Picker: Selection Counter, Kolom Curated, dan Eksklusi User yang Sudah Di-assign oleh Sesi Lain | FE+BE | 27 | TC-AC-RP-221, TC-AC-RP-230, TC-AC-RP-232, TC-AC-RP-411 |
| TC-AC-RP-E2E-067-picker-submit-user-stale-v08 | Picker Submit: User Dihapus Admin Lain (V-08), Alert Jamak, dan Campuran Tidak Eligible | FE+BE | 35 | TC-AC-RP-223, TC-AC-RP-224, TC-AC-RP-227 |
| TC-AC-RP-E2E-068-picker-submit-user-tidak-eligible-v09 | Picker Submit: User Tidak Eligible (V-09 Tunggal dan Jamak) dan Rename User Bukan Error | FE+BE | 32 | TC-AC-RP-225, TC-AC-RP-226, TC-AC-RP-229 |
| TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker | Volume Selection Limit: Select All dan Centang Manual pada Role Detail serta Popup Assign Total Control | FE+BE | 31 | TC-AC-RP-201, TC-AC-RP-202, TC-AC-RP-222, TC-AC-RP-432 |
| TC-AC-RP-E2E-070-tab-total-control-search | Search Tab Total Control: kolom Searchable, Hidden, curated, Last Updated | FE+BE | 25 | TC-AC-RP-233, TC-AC-RP-234, TC-AC-RP-235 |
| TC-AC-RP-E2E-071-tab-total-control-filter-dasar | Filter Tab Total Control: Position, Division, Status, dan panel Filter | FE+BE | 31 | TC-AC-RP-236, TC-AC-RP-237, TC-AC-RP-238, TC-AC-RP-239 |
| TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan | Filter Tab Total Control: Modified By, Last Updated, multi-field, kolom curated | FE+BE | 34 | TC-AC-RP-240, TC-AC-RP-241, TC-AC-RP-242, TC-AC-RP-243 |
| TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar | Sort Tab Total Control: Name, Position, Division, Status | FE+BE | 24 | TC-AC-RP-244, TC-AC-RP-245, TC-AC-RP-246, TC-AC-RP-247 |
| TC-AC-RP-E2E-074-tab-total-control-sort-kolom-lanjutan | Sort Tab Total Control: Modified By, Last Updated, kolom curated | FE+BE | 24 | TC-AC-RP-248, TC-AC-RP-249, TC-AC-RP-250 |
| TC-AC-RP-E2E-075-tab-total-control-setup-column | Setup Column Tab Total Control dan Tab Read Only, kolom curated, Custom Field | FE+BE | 30 | TC-AC-RP-251, TC-AC-RP-252, TC-AC-RP-253, TC-AC-RP-254, TC-AC-RP-255 |
| TC-AC-RP-E2E-076-tab-retensi-state-pagination | Retensi state tab: pindah tab, F5, Back, reset paginasi, Pagination | FE+BE | 27 | TC-AC-RP-259, TC-AC-RP-260, TC-AC-RP-261 |
| TC-AC-RP-E2E-077-tab-group-manager-search-filter | Tab Group Manager: Search, Filter Panel, Filter Status dengan node sidebar | FE+BE | 13 | TC-AC-RP-264, TC-AC-RP-265, TC-AC-RP-266 |
| TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | Tab Group Manager: Sort dan Setup Column | FE+BE | 29 | TC-AC-RP-267, TC-AC-RP-268, TC-AC-RP-269, TC-AC-RP-270, TC-AC-RP-271 |
| TC-AC-RP-E2E-079-tab-system-search-sort-setup-column | Tab System: Search, kolom tidak sortable, Setup Column | FE+BE | 17 | TC-AC-RP-272, TC-AC-RP-273, TC-AC-RP-274 |
| TC-AC-RP-E2E-080-role-detail-search-filter | Role Detail: Search Global Role dan Group Role, Filter Panel | FE+BE | 21 | TC-AC-RP-276, TC-AC-RP-277, TC-AC-RP-278 |
| TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | Role Detail: Sort kolom dan kolom CRUD tidak di Column Visibility | FE+BE | 31 | TC-AC-RP-279, TC-AC-RP-280, TC-AC-RP-281, TC-AC-RP-282, TC-AC-RP-283 |
| TC-AC-RP-E2E-082-tabel-approvers | Tabel Approvers: Search, Filter, Sort, tanpa Download, empty filtered | FE+BE | 23 | TC-AC-RP-286, TC-AC-RP-287, TC-AC-RP-288 |
| TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | Table User Picker: Search, Filter, Sort, Pagination, nama kembar, Position kosong | FE+BE | 38 | TC-AC-RP-289, TC-AC-RP-290, TC-AC-RP-291, TC-AC-RP-292, TC-AC-RP-423 |
| TC-AC-RP-E2E-084-picker-kolom-curated-search | Table User Picker: Search atas kolom curated saat Hidden dan setelah ditampilkan | FE+BE | 29 | TC-AC-RP-425, TC-AC-RP-428, TC-AC-RP-429 |
| TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system | Download isi berkas: Tab Total Control, Read Only, Group Manager, dan Tab System (CSV, XLSX) | FE+BE | 45 | TC-AC-RP-256, TC-AC-RP-257, TC-AC-RP-275, TC-AC-RP-424 |
| TC-AC-RP-E2E-086-download-berkas-role-detail-dan-changelog | Download Isi Berkas: Role Detail, Filename Title-Case, dan Changelog per Varian | FE+BE | 23 | TC-AC-RP-284, TC-AC-RP-285, TC-AC-RP-314 |
| TC-AC-RP-E2E-087-resilience-download-gagal | Resilience Download: Gagal pada Tabel dan Changelog Menampilkan Toast Error | FE+BE (intercept) | 12 | TC-AC-RP-258, TC-AC-RP-315 |
| TC-AC-RP-E2E-088-volume-download-changelog-di-atas-5000-baris | Volume: Download Changelog di Atas 5.000 Baris Memakai Loading Screen | FE+BE | 9 | TC-AC-RP-316 |
| TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | Modal Changelog: Screening Lima Varian (Total Control, Read Only, GM, System, Detail Role) | FE+BE | 38 | TC-AC-RP-293, TC-AC-RP-294, TC-AC-RP-295, TC-AC-RP-296, TC-AC-RP-297 |
| TC-AC-RP-E2E-090-modal-changelog-isi-per-varian | Modal Changelog: Isi Entri Tab Total Control, GM, System, dan Detail Role | FE+BE | 28 | TC-AC-RP-298, TC-AC-RP-299, TC-AC-RP-300, TC-AC-RP-301 |
| TC-AC-RP-E2E-091-modal-changelog-search-dan-filter | Modal Changelog: Search dan Filter Date, Action, Modified By, Field, Object | FE+BE | 37 | TC-AC-RP-302, TC-AC-RP-303, TC-AC-RP-304, TC-AC-RP-305 |
| TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | Modal Changelog: Sort Kolom Date, Action, Old Value, New Value, Modified By dan Hover Modified By | FE+BE | 36 | TC-AC-RP-306, TC-AC-RP-307, TC-AC-RP-308, TC-AC-RP-309, TC-AC-RP-310, TC-AC-RP-311 |
| TC-AC-RP-E2E-093-modal-changelog-setup-column-dan-empty-state | Modal Changelog: Setup Column, Pagination, dan Empty State | FE+BE | 19 | TC-AC-RP-312, TC-AC-RP-313 |
| TC-AC-RP-E2E-094-log-assign-dan-remove-total-control | Pencatatan Assign dan Remove Total Control di Changelog dan Changelog: User | FE+BE | 48 | TC-AC-RP-317, TC-AC-RP-319, TC-AC-RP-336, TC-AC-RP-433 |
| TC-AC-RP-E2E-095-log-assign-read-only-dan-group-manager | Pencatatan Assign Read Only, Assign Total Control dari Read Only, Assign dan Remove GM | FE+BE | 45 | TC-AC-RP-320, TC-AC-RP-321, TC-AC-RP-322 |
| TC-AC-RP-E2E-096-log-assign-user-to-role | Pencatatan Assign dan Remove User to Role, Termasuk Suffix Group | FE+BE | 30 | TC-AC-RP-323, TC-AC-RP-324 |
| TC-AC-RP-E2E-097-log-edit-crud-dan-bulk-remove | Pencatatan Edit CRUD Satu Entri per Perubahan, Group Role, dan Bulk Remove | FE+BE | 47 | TC-AC-RP-325, TC-AC-RP-326, TC-AC-RP-329 |
| TC-AC-RP-E2E-098-log-auto-revert | Pencatatan Auto-Revert Total Control dan Group Manager dengan Pelaku Admin Pengedit | FE+BE | 41 | TC-AC-RP-327, TC-AC-RP-328 |
| TC-AC-RP-E2E-099-log-toggle-require-approval | Pencatatan Toggle Require Approval Allocation dan Wallet, Termasuk Pelaku Manage User and Role | FE+BE | 44 | TC-AC-RP-330, TC-AC-RP-331, TC-AC-RP-442 |
| TC-AC-RP-E2E-100-log-additional-approver | Pencatatan Add dan Remove Additional Approver Global Role dan Group Role | FE+BE | 27 | TC-AC-RP-332, TC-AC-RP-333 |
| TC-AC-RP-E2E-101-absence-log-no-op-dan-cascade | Absence Log: Edit No-Op dan Cascade Role yang Sudah Di-assign | FE+BE | 26 | TC-AC-RP-318, TC-AC-RP-334 |
| TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred | Notifikasi In-App [DEFERRED]: Remove Total Control, Read Only, Group Manager, Assign GM Dua Group | FE+BE | 40 | TC-AC-RP-337, TC-AC-RP-338, TC-AC-RP-339, TC-AC-RP-417 |
| TC-AC-RP-E2E-103-notifikasi-in-app-auto-revert-deferred | Notifikasi In-App [DEFERRED]: Auto-Revert Total Control, Read Only, dan Group Manager | FE+BE | 32 | TC-AC-RP-340, TC-AC-RP-341, TC-AC-RP-342 |
| TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user | Sinkronisasi ke Settings > User: Assign User to Role, Edit CRUD, Remove, dan Switch Global Role pada Tab Role | FE+BE | 34 | TC-AC-RP-345, TC-AC-RP-346, TC-AC-RP-347, TC-AC-RP-348 |
| TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses | Sinkronisasi Settings > Group dan Settings > User: Rename dan Delete Group, Banner Tingkat Akses di Detail User, dan Group Baru | FE+BE | 31 | TC-AC-RP-349, TC-AC-RP-350, TC-AC-RP-351, TC-AC-RP-352 |
| TC-AC-RP-E2E-106-konsumen-grup-gm-dan-group-role-exact-match | Modul Konsumen: Wewenang GM atas Descendant, Group Role Exact Match, dan Peran Tanpa Penugasan Group | FE+BE | 13 | TC-AC-RP-354, TC-AC-RP-355, TC-AC-RP-356 |
| TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | Modul Konsumen Allocation: Toggle ON dan OFF, Bypass GM dan Total Control, serta Additional Approver | FE+BE | 24 | TC-AC-RP-357, TC-AC-RP-358, TC-AC-RP-359, TC-AC-RP-360, TC-AC-RP-361 |
| TC-AC-RP-E2E-108-konsumen-allocation-remove-approver-toggle-tidak-retroaktif | Modul Konsumen Allocation: Remove Approver Seketika, Toggle Tidak Retroaktif, dan Allocator Di-deactivate | FE+BE | 35 | TC-AC-RP-362, TC-AC-RP-363, TC-AC-RP-364 |
| TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission | Modul Konsumen: Total Control Fallback Reviewer, GM Baru Tanpa Snapshot, Wallet Deposit, dan Approver TAG Stock | FE+BE | 22 | TC-AC-RP-366, TC-AC-RP-367, TC-AC-RP-368, TC-AC-RP-369 |
| TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi | Multi-Konteks: Dua Reviewer Approve Bersamaan, Permission Baru pada Sesi Paralel, Dua Admin Edit Cell Sama, dan Dua Assign Bersamaan | FE+BE | 42 | TC-AC-RP-365, TC-AC-RP-370, TC-AC-RP-406, TC-AC-RP-409 |
| TC-AC-RP-E2E-111-double-submit-dan-total-control-minimal-satu | Double Submit: Klik Assign dan Confirm Ganda Tanpa Efek Ganda, serta Total Control Selalu Minimal Satu | FE+BE | 33 | TC-AC-RP-407, TC-AC-RP-408, TC-AC-RP-410 |
| TC-AC-RP-E2E-112-state-tenant-entitas-suspended | State Tenant: Entitas Suspended (Kontrol Tulis Enabled, Server Menolak Aksi Tulis, dan Data Tetap Terbaca) | FE+BE | 26 | TC-AC-RP-391, TC-AC-RP-392, TC-AC-RP-393 |
| TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | Defense-in-depth: Request Langsung oleh Read Only dan Manage user and role Ditolak | FE+BE | 32 | TC-AC-RP-371, TC-AC-RP-372, TC-AC-RP-373, TC-AC-RP-374, TC-AC-RP-375, TC-AC-RP-376, TC-AC-RP-377, TC-AC-RP-443 |
| TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | Defense-in-depth: Request Langsung atas Default User, Diri Sendiri, dan oleh Aktor Default User Ditolak | FE+BE | 29 | TC-AC-RP-378, TC-AC-RP-379, TC-AC-RP-380, TC-AC-RP-381, TC-AC-RP-382, TC-AC-RP-383, TC-AC-RP-434, TC-AC-RP-438 |
| TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | Defense-in-depth: Request Langsung atas Target Total Control, Kandidat Pending, Payload CRUD, Bulk Remove, dan Group Manager | FE+BE | 30 | TC-AC-RP-384, TC-AC-RP-385, TC-AC-RP-386, TC-AC-RP-387, TC-AC-RP-388, TC-AC-RP-389, TC-AC-RP-390 |
| TC-AC-RP-E2E-116-defense-selection-limit-request-langsung | Defense-in-depth: Selection Limit lewat Request Langsung Ditolak (Bulk Remove dan Assign Total Control) | FE+BE | 9 | TC-AC-RP-435, TC-AC-RP-436 |
| TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain | Target Berubah sejak Render: Edit CRUD, Remove Total Control, Read Only, dan Group Manager yang Sudah Diubah Admin Lain | FE+BE | 41 | TC-AC-RP-394, TC-AC-RP-395, TC-AC-RP-396, TC-AC-RP-397 |
| TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah | Target Berubah sejak Render: Remove Idempoten, Approver Sudah Hilang, dan Status Target Berubah menjadi Total Control | FE+BE | 43 | TC-AC-RP-398, TC-AC-RP-399, TC-AC-RP-400, TC-AC-RP-401 |
| TC-AC-RP-E2E-119-stale-group-terpilih-dihapus | Target Berubah sejak Render: Group Terpilih Dihapus Admin Lain sebelum Submit Assign Group Manager dan Assign User to Role | FE+BE | 29 | TC-AC-RP-402, TC-AC-RP-403 |
| TC-AC-RP-E2E-120-deskripsi-role-detail-global-role | Deskripsi Role Detail Global Role Mengikuti Katalog untuk Setiap Role | FE+BE | 4 | TC-AC-RP-38 |
| TC-AC-RP-E2E-121-deskripsi-role-detail-group-role | Deskripsi Role Detail Group Role Mengikuti Katalog untuk Setiap Role | FE+BE | 4 | TC-AC-RP-50 |
| TC-AC-RP-E2E-122-role-matrix-visibilitas-tab-per-role-tanpa-hak-tulis | Role Matrix: Visibilitas Tab Total Control, Read Only, Group Manager untuk Role tanpa Hak Tulis | FE+BE | 28 | TC-AC-RP-90, TC-AC-RP-93, TC-AC-RP-96 |
| TC-AC-RP-E2E-123-gating-remove-role-detail-total-control | Gating Remove Role Detail untuk Aktor Total Control: Diri Sendiri dan Dialog Auto-revert | FE+BE | 18 | TC-AC-RP-117, TC-AC-RP-118 |
| TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive | Assign Total Control: Cascade Group Role, Beberapa User Satu Toast, User Pending Activation dan Inactive | FE+BE | 34 | TC-AC-RP-123, TC-AC-RP-124, TC-AC-RP-127, TC-AC-RP-416 |
| TC-AC-RP-E2E-125-resilience-tulis-read-only-dan-group-manager | Resilience Tulis: Assign dan Remove Read Only serta Assign dan Remove Group Manager Gagal 5xx | FE+BE (intercept) | 38 | TC-AC-RP-144, TC-AC-RP-145, TC-AC-RP-159 |
| TC-AC-RP-E2E-126-edit-crud-auto-revert-group-manager-lewat-detail-user | Auto-Revert Group Manager: Melepas Seluruh Peran Grup dari Detail User Mencabut GM di Seluruh Group | FE+BE | 16 | TC-AC-RP-184 |
| TC-AC-RP-E2E-127-bulk-remove-role-detail-baris-sudah-dihapus-admin-lain | Bulk Remove Role Detail: Baris yang Sudah Dihapus Admin Lain Dianggap Sukses | FE+BE | 15 | TC-AC-RP-197 |
| TC-AC-RP-E2E-128-table-user-picker-aktor-dan-empty-state | Table User Picker: Aktor Tidak Muncul di Tiga Popup Assign dan Empty State Seluruh Kandidat Sudah Ter-assign | FE+BE | 24 | TC-AC-RP-437, TC-AC-RP-231 |
| TC-AC-RP-E2E-129-assign-approver-activation-status-berubah-v09 | Assign Approver: Activation Status User Berubah Menjadi Tidak Eligible (V-09) | FE+BE | 10 | TC-AC-RP-228 |
| TC-AC-RP-E2E-130-role-detail-reset-paginasi-dan-pilihan-pagination | Role Detail: Search atau Apply Filter mereset paginasi ke halaman 1 dan pilihan Pagination | FE+BE | 20 | TC-AC-RP-262, TC-AC-RP-263 |
| TC-AC-RP-E2E-132-absence-log-edit-nilai-sama-dan-delete-group | Absence Log: Edit CRUD Nilai yang Sudah Sama dan Delete Group Tanpa Log Approver dan Toggle | FE+BE | 39 | TC-AC-RP-335, TC-AC-RP-421 |
| TC-AC-RP-E2E-133-notifikasi-in-app-tanpa-notifikasi-dan-auto-revert-detail-user-deferred | Notifikasi In-App [DEFERRED]: Tanpa Notifikasi untuk Assign dan Group Deleted, dan Auto-Revert dari Detail User | FE+BE | 22 | TC-AC-RP-343, TC-AC-RP-344 |
| TC-AC-RP-E2E-134-sinkron-pindah-entitas-antar-group-dan-wewenang-gm | Sinkronisasi Settings > Group: Pemindahan Entitas Antar Group Menyesuaikan Wewenang Group Manager Tanpa Perubahan Penugasan | FE+BE | 26 | TC-AC-RP-353 |
| TC-AC-RP-E2E-135-state-tenant-entitas-expired | State Tenant: Entitas Expired (Kontrol Tulis Enabled, Aksi Tulis Ditolak dengan Toast Baku, dan Guard Diri Sendiri) | FE+BE | 14 | TC-AC-RP-414 |
| TC-AC-RP-E2E-136-defense-prioritas-pesan-403-beberapa-kondisi | Defense-in-depth: Prioritas Pesan 403 saat Beberapa Kondisi Penolakan Berlaku Sekaligus | FE+BE | 18 | TC-AC-RP-418 |
| TC-AC-RP-E2E-137-stale-node-group-dihapus-toast-netral-approver-dan-toggle | Target Berubah sejak Render: Node Group Aktif Dihapus Admin Lain sebelum Assign Approver dan Perubahan Toggle | FE+BE | 24 | TC-AC-RP-404, TC-AC-RP-405 |
| TC-AC-RP-E2E-138-absence-log-selection-limit-request-langsung | Absence Log: Selection Limit lewat Request Langsung Ditolak Tanpa Entri Changelog (Bulk Remove dan Assign Total Control) | FE+BE | 23 | TC-AC-RP-435, TC-AC-RP-436 (klausa absence; bagian presence ada di spec 116) |
| TC-AC-RP-E2E-139-mobile-volume-card-list-pagination-select-all-android | Mobile Android Volume 105 User: Pagination Card List Default 10 dan Select All Hanya Halaman Aktif Role Detail | FE+BE | 11 | TC-AC-RP-426 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Seluruh 443 TC punya antarmuka dan masuk spec. TC defense-in-depth dengan Expected respons API tetap masuk spec FE+BE dengan butir Notes `K-1`; TC `[DEFERRED]` tetap masuk spec karena hambatan teknis bukan alasan mengeluarkan TC.

| TC ID | Skenario | Alasan Dikecualikan dari E2E |
|---|---|---|
| — | — | — |

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-RP-1 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-2 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-3 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-4 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-5 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-6 | E2E | TC-AC-RP-E2E-001-screening-tab-total-control-kolom-dan-isi | FE+BE |
| TC-AC-RP-7 | E2E | TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled | FE+BE |
| TC-AC-RP-8 | E2E | TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled | FE+BE |
| TC-AC-RP-9 | E2E | TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled | FE+BE |
| TC-AC-RP-10 | E2E | TC-AC-RP-E2E-002-screening-tab-total-control-row-action-disabled | FE+BE |
| TC-AC-RP-11 | E2E | TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama | FE+BE |
| TC-AC-RP-12 | E2E | TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama | FE+BE |
| TC-AC-RP-13 | E2E | TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama | FE+BE |
| TC-AC-RP-14 | E2E | TC-AC-RP-E2E-003-screening-tab-total-control-tooltip-breadcrumb-dan-nama | FE+BE |
| TC-AC-RP-15 | E2E | TC-AC-RP-E2E-004-screening-tab-read-only | FE+BE |
| TC-AC-RP-16 | E2E | TC-AC-RP-E2E-004-screening-tab-read-only | FE+BE |
| TC-AC-RP-17 | E2E | TC-AC-RP-E2E-004-screening-tab-read-only | FE+BE |
| TC-AC-RP-18 | E2E | TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree | FE+BE |
| TC-AC-RP-19 | E2E | TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree | FE+BE |
| TC-AC-RP-20 | E2E | TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree | FE+BE |
| TC-AC-RP-21 | E2E | TC-AC-RP-E2E-005-screening-tab-group-manager-dan-group-tree | FE+BE |
| TC-AC-RP-22 | E2E | TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | FE+BE |
| TC-AC-RP-23 | E2E | TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | FE+BE |
| TC-AC-RP-24 | E2E | TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | FE+BE |
| TC-AC-RP-25 | E2E | TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | FE+BE |
| TC-AC-RP-26 | E2E | TC-AC-RP-E2E-006-sidebar-group-tree-filter-node-dan-collapse | FE+BE |
| TC-AC-RP-27 | E2E | TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role | FE+BE |
| TC-AC-RP-28 | E2E | TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role | FE+BE |
| TC-AC-RP-29 | E2E | TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role | FE+BE |
| TC-AC-RP-30 | E2E | TC-AC-RP-E2E-007-screening-tab-system-global-role-dan-group-role | FE+BE |
| TC-AC-RP-31 | E2E | TC-AC-RP-E2E-008-katalog-tab-system-distributor-dan-partner | FE+BE |
| TC-AC-RP-32 | E2E | TC-AC-RP-E2E-008-katalog-tab-system-distributor-dan-partner | FE+BE |
| TC-AC-RP-33 | E2E | TC-AC-RP-E2E-008-katalog-tab-system-distributor-dan-partner | FE+BE |
| TC-AC-RP-34 | E2E | TC-AC-RP-E2E-009-screening-role-detail-global-role | FE+BE |
| TC-AC-RP-35 | E2E | TC-AC-RP-E2E-009-screening-role-detail-global-role | FE+BE |
| TC-AC-RP-36 | E2E | TC-AC-RP-E2E-009-screening-role-detail-global-role | FE+BE |
| TC-AC-RP-37 | E2E | TC-AC-RP-E2E-009-screening-role-detail-global-role | FE+BE |
| TC-AC-RP-38 | E2E | TC-AC-RP-E2E-120-deskripsi-role-detail-global-role | FE+BE |
| TC-AC-RP-39 | E2E | TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | FE+BE |
| TC-AC-RP-40 | E2E | TC-AC-RP-E2E-011-role-detail-varian-distributor | FE+BE |
| TC-AC-RP-41 | E2E | TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | FE+BE |
| TC-AC-RP-42 | E2E | TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | FE+BE |
| TC-AC-RP-43 | E2E | TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | FE+BE |
| TC-AC-RP-44 | E2E | TC-AC-RP-E2E-011-role-detail-varian-distributor | FE+BE |
| TC-AC-RP-45 | E2E | TC-AC-RP-E2E-010-role-detail-global-breadcrumb-tag-stock-dan-approvers-section | FE+BE |
| TC-AC-RP-46 | E2E | TC-AC-RP-E2E-012-screening-role-detail-group-role | FE+BE |
| TC-AC-RP-47 | E2E | TC-AC-RP-E2E-012-screening-role-detail-group-role | FE+BE |
| TC-AC-RP-48 | E2E | TC-AC-RP-E2E-012-screening-role-detail-group-role | FE+BE |
| TC-AC-RP-49 | E2E | TC-AC-RP-E2E-012-screening-role-detail-group-role | FE+BE |
| TC-AC-RP-50 | E2E | TC-AC-RP-E2E-121-deskripsi-role-detail-group-role | FE+BE |
| TC-AC-RP-51 | E2E | TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | FE+BE |
| TC-AC-RP-52 | E2E | TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | FE+BE |
| TC-AC-RP-53 | E2E | TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | FE+BE |
| TC-AC-RP-54 | E2E | TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | FE+BE |
| TC-AC-RP-55 | E2E | TC-AC-RP-E2E-013-role-detail-group-role-approval-settings | FE+BE |
| TC-AC-RP-56 | E2E | TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail | FE+BE (intercept) |
| TC-AC-RP-57 | E2E | TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail | FE+BE (intercept) |
| TC-AC-RP-58 | E2E | TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail | FE+BE (intercept) |
| TC-AC-RP-59 | E2E | TC-AC-RP-E2E-014-resilience-baca-tab-dan-role-detail | FE+BE (intercept) |
| TC-AC-RP-60 | E2E | TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | FE+BE |
| TC-AC-RP-61 | E2E | TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | FE+BE |
| TC-AC-RP-62 | E2E | TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | FE+BE |
| TC-AC-RP-63 | E2E | TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | FE+BE |
| TC-AC-RP-64 | E2E | TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil | FE+BE |
| TC-AC-RP-65 | E2E | TC-AC-RP-E2E-016-guided-tooltip-replay-guide | FE+BE |
| TC-AC-RP-66 | E2E | TC-AC-RP-E2E-016-guided-tooltip-replay-guide | FE+BE |
| TC-AC-RP-67 | E2E | TC-AC-RP-E2E-016-guided-tooltip-replay-guide | FE+BE |
| TC-AC-RP-68 | E2E | TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | FE+BE |
| TC-AC-RP-69 | E2E | TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | FE+BE |
| TC-AC-RP-70 | E2E | TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | FE+BE |
| TC-AC-RP-71 | E2E | TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | FE+BE |
| TC-AC-RP-72 | E2E | TC-AC-RP-E2E-017-mobile-card-list-bottom-sheet-dan-tab-android | FE+BE |
| TC-AC-RP-73 | E2E | TC-AC-RP-E2E-018-mobile-role-detail-dan-approval-settings-android | FE+BE |
| TC-AC-RP-74 | E2E | TC-AC-RP-E2E-018-mobile-role-detail-dan-approval-settings-android | FE+BE |
| TC-AC-RP-75 | E2E | TC-AC-RP-E2E-018-mobile-role-detail-dan-approval-settings-android | FE+BE |
| TC-AC-RP-76 | E2E | TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | FE+BE |
| TC-AC-RP-77 | E2E | TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | FE+BE |
| TC-AC-RP-78 | E2E | TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | FE+BE |
| TC-AC-RP-79 | E2E | TC-AC-RP-E2E-021-role-matrix-akses-menu-negatif | FE+BE |
| TC-AC-RP-80 | E2E | TC-AC-RP-E2E-021-role-matrix-akses-menu-negatif | FE+BE |
| TC-AC-RP-81 | E2E | TC-AC-RP-E2E-021-role-matrix-akses-menu-negatif | FE+BE |
| TC-AC-RP-82 | E2E | TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | FE+BE |
| TC-AC-RP-83 | E2E | TC-AC-RP-E2E-020-role-matrix-akses-menu-positif | FE+BE |
| TC-AC-RP-84 | E2E | TC-AC-RP-E2E-022-role-matrix-visibilitas-tab-per-role | FE+BE |
| TC-AC-RP-85 | E2E | TC-AC-RP-E2E-024-role-matrix-visibilitas-role-detail-negatif | FE+BE |
| TC-AC-RP-86 | E2E | TC-AC-RP-E2E-026-role-matrix-visibilitas-approval-settings-negatif | FE+BE |
| TC-AC-RP-87 | E2E | TC-AC-RP-E2E-022-role-matrix-visibilitas-tab-per-role | FE+BE |
| TC-AC-RP-88 | E2E | TC-AC-RP-E2E-023-role-matrix-visibilitas-role-detail-positif | FE+BE |
| TC-AC-RP-89 | E2E | TC-AC-RP-E2E-025-role-matrix-visibilitas-approval-settings-positif | FE+BE |
| TC-AC-RP-90 | E2E | TC-AC-RP-E2E-122-role-matrix-visibilitas-tab-per-role-tanpa-hak-tulis | FE+BE |
| TC-AC-RP-91 | E2E | TC-AC-RP-E2E-024-role-matrix-visibilitas-role-detail-negatif | FE+BE |
| TC-AC-RP-92 | E2E | TC-AC-RP-E2E-026-role-matrix-visibilitas-approval-settings-negatif | FE+BE |
| TC-AC-RP-93 | E2E | TC-AC-RP-E2E-122-role-matrix-visibilitas-tab-per-role-tanpa-hak-tulis | FE+BE |
| TC-AC-RP-94 | E2E | TC-AC-RP-E2E-023-role-matrix-visibilitas-role-detail-positif | FE+BE |
| TC-AC-RP-95 | E2E | TC-AC-RP-E2E-025-role-matrix-visibilitas-approval-settings-positif | FE+BE |
| TC-AC-RP-96 | E2E | TC-AC-RP-E2E-122-role-matrix-visibilitas-tab-per-role-tanpa-hak-tulis | FE+BE |
| TC-AC-RP-97 | E2E | TC-AC-RP-E2E-024-role-matrix-visibilitas-role-detail-negatif | FE+BE |
| TC-AC-RP-98 | E2E | TC-AC-RP-E2E-026-role-matrix-visibilitas-approval-settings-negatif | FE+BE |
| TC-AC-RP-99 | E2E | TC-AC-RP-E2E-027-role-matrix-approvers-section-dan-row-action-detail | FE+BE |
| TC-AC-RP-100 | E2E | TC-AC-RP-E2E-027-role-matrix-approvers-section-dan-row-action-detail | FE+BE |
| TC-AC-RP-101 | E2E | TC-AC-RP-E2E-027-role-matrix-approvers-section-dan-row-action-detail | FE+BE |
| TC-AC-RP-102 | E2E | TC-AC-RP-E2E-028-gating-checkbox-crud-total-control | FE+BE |
| TC-AC-RP-103 | E2E | TC-AC-RP-E2E-028-gating-checkbox-crud-total-control | FE+BE |
| TC-AC-RP-104 | E2E | TC-AC-RP-E2E-028-gating-checkbox-crud-total-control | FE+BE |
| TC-AC-RP-105 | E2E | TC-AC-RP-E2E-028-gating-checkbox-crud-total-control | FE+BE |
| TC-AC-RP-106 | E2E | TC-AC-RP-E2E-031-gating-checkbox-crud-default-user-dan-read-only | FE+BE |
| TC-AC-RP-107 | E2E | TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | FE+BE |
| TC-AC-RP-108 | E2E | TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | FE+BE |
| TC-AC-RP-109 | E2E | TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | FE+BE |
| TC-AC-RP-110 | E2E | TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | FE+BE |
| TC-AC-RP-111 | E2E | TC-AC-RP-E2E-031-gating-checkbox-crud-default-user-dan-read-only | FE+BE |
| TC-AC-RP-112 | E2E | TC-AC-RP-E2E-030-gating-checkbox-crud-manage-user-and-role | FE+BE |
| TC-AC-RP-113 | E2E | TC-AC-RP-E2E-029-checkbox-crud-in-flight-dan-keyboard | FE+BE (intercept) |
| TC-AC-RP-114 | E2E | TC-AC-RP-E2E-029-checkbox-crud-in-flight-dan-keyboard | FE+BE (intercept) |
| TC-AC-RP-115 | E2E | TC-AC-RP-E2E-032-gating-remove-role-detail-dan-select-all | FE+BE |
| TC-AC-RP-116 | E2E | TC-AC-RP-E2E-032-gating-remove-role-detail-dan-select-all | FE+BE |
| TC-AC-RP-117 | E2E | TC-AC-RP-E2E-123-gating-remove-role-detail-total-control | FE+BE |
| TC-AC-RP-118 | E2E | TC-AC-RP-E2E-123-gating-remove-role-detail-total-control | FE+BE |
| TC-AC-RP-119 | E2E | TC-AC-RP-E2E-032-gating-remove-role-detail-dan-select-all | FE+BE |
| TC-AC-RP-120 | E2E | TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | FE+BE |
| TC-AC-RP-121 | E2E | TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | FE+BE |
| TC-AC-RP-122 | E2E | TC-AC-RP-E2E-034-assign-total-control-user-standard-dan-seluruh-global-role | FE+BE |
| TC-AC-RP-123 | E2E | TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive | FE+BE |
| TC-AC-RP-124 | E2E | TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive | FE+BE |
| TC-AC-RP-125 | E2E | TC-AC-RP-E2E-035-assign-total-control-beralih-dari-tingkat-akses-lain | FE+BE |
| TC-AC-RP-126 | E2E | TC-AC-RP-E2E-035-assign-total-control-beralih-dari-tingkat-akses-lain | FE+BE |
| TC-AC-RP-127 | E2E | TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive | FE+BE |
| TC-AC-RP-128 | E2E | TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | FE+BE |
| TC-AC-RP-129 | E2E | TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | FE+BE |
| TC-AC-RP-130 | E2E | TC-AC-RP-E2E-033-assign-total-control-screening-pool-dan-validasi | FE+BE |
| TC-AC-RP-131 | E2E | TC-AC-RP-E2E-043-resilience-tulis-assign-dan-remove-total-control | FE+BE (intercept) |
| TC-AC-RP-132 | E2E | TC-AC-RP-E2E-036-remove-total-control | FE+BE |
| TC-AC-RP-133 | E2E | TC-AC-RP-E2E-036-remove-total-control | FE+BE |
| TC-AC-RP-134 | E2E | TC-AC-RP-E2E-036-remove-total-control | FE+BE |
| TC-AC-RP-135 | E2E | TC-AC-RP-E2E-036-remove-total-control | FE+BE |
| TC-AC-RP-136 | E2E | TC-AC-RP-E2E-036-remove-total-control | FE+BE |
| TC-AC-RP-137 | E2E | TC-AC-RP-E2E-043-resilience-tulis-assign-dan-remove-total-control | FE+BE (intercept) |
| TC-AC-RP-138 | E2E | TC-AC-RP-E2E-037-assign-read-only-screening-validasi-dan-assign | FE+BE |
| TC-AC-RP-139 | E2E | TC-AC-RP-E2E-037-assign-read-only-screening-validasi-dan-assign | FE+BE |
| TC-AC-RP-140 | E2E | TC-AC-RP-E2E-038-assign-read-only-dari-group-manager-dan-remove-read-only | FE+BE |
| TC-AC-RP-141 | E2E | TC-AC-RP-E2E-037-assign-read-only-screening-validasi-dan-assign | FE+BE |
| TC-AC-RP-142 | E2E | TC-AC-RP-E2E-038-assign-read-only-dari-group-manager-dan-remove-read-only | FE+BE |
| TC-AC-RP-143 | E2E | TC-AC-RP-E2E-038-assign-read-only-dari-group-manager-dan-remove-read-only | FE+BE |
| TC-AC-RP-144 | E2E | TC-AC-RP-E2E-125-resilience-tulis-read-only-dan-group-manager | FE+BE (intercept) |
| TC-AC-RP-145 | E2E | TC-AC-RP-E2E-125-resilience-tulis-read-only-dan-group-manager | FE+BE (intercept) |
| TC-AC-RP-146 | E2E | TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool | FE+BE |
| TC-AC-RP-147 | E2E | TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool | FE+BE |
| TC-AC-RP-148 | E2E | TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool | FE+BE |
| TC-AC-RP-149 | E2E | TC-AC-RP-E2E-039-assign-group-manager-screening-tree-pool | FE+BE |
| TC-AC-RP-150 | E2E | TC-AC-RP-E2E-041-assign-group-manager-aksi-berhasil | FE+BE |
| TC-AC-RP-151 | E2E | TC-AC-RP-E2E-041-assign-group-manager-aksi-berhasil | FE+BE |
| TC-AC-RP-152 | E2E | TC-AC-RP-E2E-041-assign-group-manager-aksi-berhasil | FE+BE |
| TC-AC-RP-153 | E2E | TC-AC-RP-E2E-040-assign-group-manager-validasi-dan-empty-state | FE+BE |
| TC-AC-RP-154 | E2E | TC-AC-RP-E2E-040-assign-group-manager-validasi-dan-empty-state | FE+BE |
| TC-AC-RP-155 | E2E | TC-AC-RP-E2E-040-assign-group-manager-validasi-dan-empty-state | FE+BE |
| TC-AC-RP-156 | E2E | TC-AC-RP-E2E-042-remove-group-manager | FE+BE |
| TC-AC-RP-157 | E2E | TC-AC-RP-E2E-042-remove-group-manager | FE+BE |
| TC-AC-RP-158 | E2E | TC-AC-RP-E2E-042-remove-group-manager | FE+BE |
| TC-AC-RP-159 | E2E | TC-AC-RP-E2E-125-resilience-tulis-read-only-dan-group-manager | FE+BE (intercept) |
| TC-AC-RP-160 | E2E | TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool | FE+BE |
| TC-AC-RP-161 | E2E | TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool | FE+BE |
| TC-AC-RP-162 | E2E | TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool | FE+BE |
| TC-AC-RP-163 | E2E | TC-AC-RP-E2E-046-assign-user-to-global-role-aksi-berhasil | FE+BE |
| TC-AC-RP-164 | E2E | TC-AC-RP-E2E-046-assign-user-to-global-role-aksi-berhasil | FE+BE |
| TC-AC-RP-165 | E2E | TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi | FE+BE |
| TC-AC-RP-166 | E2E | TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi | FE+BE |
| TC-AC-RP-167 | E2E | TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi | FE+BE |
| TC-AC-RP-168 | E2E | TC-AC-RP-E2E-048-assign-user-to-group-role-aksi-berhasil | FE+BE |
| TC-AC-RP-169 | E2E | TC-AC-RP-E2E-048-assign-user-to-group-role-aksi-berhasil | FE+BE |
| TC-AC-RP-170 | E2E | TC-AC-RP-E2E-047-assign-user-to-group-role-screening-dan-validasi | FE+BE |
| TC-AC-RP-171 | E2E | TC-AC-RP-E2E-044-resilience-tulis-assign-user-edit-crud-dan-toggle | FE+BE (intercept) |
| TC-AC-RP-172 | E2E | TC-AC-RP-E2E-049-edit-crud-autosave-target-standard | FE+BE |
| TC-AC-RP-173 | E2E | TC-AC-RP-E2E-049-edit-crud-autosave-target-standard | FE+BE |
| TC-AC-RP-174 | E2E | TC-AC-RP-E2E-049-edit-crud-autosave-target-standard | FE+BE |
| TC-AC-RP-175 | E2E | TC-AC-RP-E2E-044-resilience-tulis-assign-user-edit-crud-dan-toggle | FE+BE (intercept) |
| TC-AC-RP-176 | E2E | TC-AC-RP-E2E-050-edit-crud-auto-revert-total-control | FE+BE |
| TC-AC-RP-177 | E2E | TC-AC-RP-E2E-050-edit-crud-auto-revert-total-control | FE+BE |
| TC-AC-RP-178 | E2E | TC-AC-RP-E2E-050-edit-crud-auto-revert-total-control | FE+BE |
| TC-AC-RP-179 | E2E | TC-AC-RP-E2E-051-edit-crud-auto-revert-read-only-dan-group-manager | FE+BE |
| TC-AC-RP-180 | E2E | TC-AC-RP-E2E-051-edit-crud-auto-revert-read-only-dan-group-manager | FE+BE |
| TC-AC-RP-181 | E2E | TC-AC-RP-E2E-052-edit-crud-tanpa-auto-revert-dan-susun-ulang | FE+BE |
| TC-AC-RP-182 | E2E | TC-AC-RP-E2E-052-edit-crud-tanpa-auto-revert-dan-susun-ulang | FE+BE |
| TC-AC-RP-183 | E2E | TC-AC-RP-E2E-052-edit-crud-tanpa-auto-revert-dan-susun-ulang | FE+BE |
| TC-AC-RP-184 | E2E | TC-AC-RP-E2E-126-edit-crud-auto-revert-group-manager-lewat-detail-user | FE+BE |
| TC-AC-RP-185 | E2E | TC-AC-RP-E2E-053-remove-role-single-cancel-confirm-dan-group-role | FE+BE |
| TC-AC-RP-186 | E2E | TC-AC-RP-E2E-053-remove-role-single-cancel-confirm-dan-group-role | FE+BE |
| TC-AC-RP-187 | E2E | TC-AC-RP-E2E-053-remove-role-single-cancel-confirm-dan-group-role | FE+BE |
| TC-AC-RP-188 | E2E | TC-AC-RP-E2E-054-remove-role-single-auto-revert-tingkat-akses | FE+BE |
| TC-AC-RP-189 | E2E | TC-AC-RP-E2E-054-remove-role-single-auto-revert-tingkat-akses | FE+BE |
| TC-AC-RP-190 | E2E | TC-AC-RP-E2E-056-bulk-remove-role-detail-berhasil-dan-campuran | FE+BE |
| TC-AC-RP-191 | E2E | TC-AC-RP-E2E-056-bulk-remove-role-detail-berhasil-dan-campuran | FE+BE |
| TC-AC-RP-192 | E2E | TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel | FE+BE |
| TC-AC-RP-193 | E2E | TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel | FE+BE |
| TC-AC-RP-194 | E2E | TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel | FE+BE |
| TC-AC-RP-195 | E2E | TC-AC-RP-E2E-057-bulk-remove-role-detail-stale-oleh-admin-lain | FE+BE |
| TC-AC-RP-196 | E2E | TC-AC-RP-E2E-057-bulk-remove-role-detail-stale-oleh-admin-lain | FE+BE |
| TC-AC-RP-197 | E2E | TC-AC-RP-E2E-127-bulk-remove-role-detail-baris-sudah-dihapus-admin-lain | FE+BE |
| TC-AC-RP-198 | E2E | TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver | FE+BE |
| TC-AC-RP-199 | E2E | TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver | FE+BE |
| TC-AC-RP-200 | E2E | TC-AC-RP-E2E-055-bulk-remove-role-detail-bar-dialog-dan-cancel | FE+BE |
| TC-AC-RP-201 | E2E | TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker | FE+BE |
| TC-AC-RP-202 | E2E | TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker | FE+BE |
| TC-AC-RP-203 | E2E | TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign | FE+BE |
| TC-AC-RP-204 | E2E | TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign | FE+BE |
| TC-AC-RP-205 | E2E | TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign | FE+BE |
| TC-AC-RP-206 | E2E | TC-AC-RP-E2E-060-assign-approver-group-role-dan-v09 | FE+BE |
| TC-AC-RP-207 | E2E | TC-AC-RP-E2E-060-assign-approver-group-role-dan-v09 | FE+BE |
| TC-AC-RP-208 | E2E | TC-AC-RP-E2E-061-remove-approver-single | FE+BE |
| TC-AC-RP-209 | E2E | TC-AC-RP-E2E-061-remove-approver-single | FE+BE |
| TC-AC-RP-210 | E2E | TC-AC-RP-E2E-061-remove-approver-single | FE+BE |
| TC-AC-RP-211 | E2E | TC-AC-RP-E2E-062-bulk-remove-approver | FE+BE (intercept) |
| TC-AC-RP-212 | E2E | TC-AC-RP-E2E-062-bulk-remove-approver | FE+BE (intercept) |
| TC-AC-RP-213 | E2E | TC-AC-RP-E2E-062-bulk-remove-approver | FE+BE (intercept) |
| TC-AC-RP-214 | E2E | TC-AC-RP-E2E-063-resilience-tulis-approver | FE+BE (intercept) |
| TC-AC-RP-215 | E2E | TC-AC-RP-E2E-063-resilience-tulis-approver | FE+BE (intercept) |
| TC-AC-RP-216 | E2E | TC-AC-RP-E2E-064-toggle-require-approval-total-control | FE+BE (intercept) |
| TC-AC-RP-217 | E2E | TC-AC-RP-E2E-064-toggle-require-approval-total-control | FE+BE (intercept) |
| TC-AC-RP-218 | E2E | TC-AC-RP-E2E-064-toggle-require-approval-total-control | FE+BE (intercept) |
| TC-AC-RP-219 | E2E | TC-AC-RP-E2E-064-toggle-require-approval-total-control | FE+BE (intercept) |
| TC-AC-RP-220 | E2E | TC-AC-RP-E2E-044-resilience-tulis-assign-user-edit-crud-dan-toggle | FE+BE (intercept) |
| TC-AC-RP-221 | E2E | TC-AC-RP-E2E-066-table-user-picker-perilaku-umum | FE+BE |
| TC-AC-RP-222 | E2E | TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker | FE+BE |
| TC-AC-RP-223 | E2E | TC-AC-RP-E2E-067-picker-submit-user-stale-v08 | FE+BE |
| TC-AC-RP-224 | E2E | TC-AC-RP-E2E-067-picker-submit-user-stale-v08 | FE+BE |
| TC-AC-RP-225 | E2E | TC-AC-RP-E2E-068-picker-submit-user-tidak-eligible-v09 | FE+BE |
| TC-AC-RP-226 | E2E | TC-AC-RP-E2E-068-picker-submit-user-tidak-eligible-v09 | FE+BE |
| TC-AC-RP-227 | E2E | TC-AC-RP-E2E-067-picker-submit-user-stale-v08 | FE+BE |
| TC-AC-RP-228 | E2E | TC-AC-RP-E2E-129-assign-approver-activation-status-berubah-v09 | FE+BE |
| TC-AC-RP-229 | E2E | TC-AC-RP-E2E-068-picker-submit-user-tidak-eligible-v09 | FE+BE |
| TC-AC-RP-230 | E2E | TC-AC-RP-E2E-066-table-user-picker-perilaku-umum | FE+BE |
| TC-AC-RP-231 | E2E | TC-AC-RP-E2E-128-table-user-picker-aktor-dan-empty-state | FE+BE |
| TC-AC-RP-232 | E2E | TC-AC-RP-E2E-066-table-user-picker-perilaku-umum | FE+BE |
| TC-AC-RP-233 | E2E | TC-AC-RP-E2E-070-tab-total-control-search | FE+BE |
| TC-AC-RP-234 | E2E | TC-AC-RP-E2E-070-tab-total-control-search | FE+BE |
| TC-AC-RP-235 | E2E | TC-AC-RP-E2E-070-tab-total-control-search | FE+BE |
| TC-AC-RP-236 | E2E | TC-AC-RP-E2E-071-tab-total-control-filter-dasar | FE+BE |
| TC-AC-RP-237 | E2E | TC-AC-RP-E2E-071-tab-total-control-filter-dasar | FE+BE |
| TC-AC-RP-238 | E2E | TC-AC-RP-E2E-071-tab-total-control-filter-dasar | FE+BE |
| TC-AC-RP-239 | E2E | TC-AC-RP-E2E-071-tab-total-control-filter-dasar | FE+BE |
| TC-AC-RP-240 | E2E | TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan | FE+BE |
| TC-AC-RP-241 | E2E | TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan | FE+BE |
| TC-AC-RP-242 | E2E | TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan | FE+BE |
| TC-AC-RP-243 | E2E | TC-AC-RP-E2E-072-tab-total-control-filter-lanjutan | FE+BE |
| TC-AC-RP-244 | E2E | TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar | FE+BE |
| TC-AC-RP-245 | E2E | TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar | FE+BE |
| TC-AC-RP-246 | E2E | TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar | FE+BE |
| TC-AC-RP-247 | E2E | TC-AC-RP-E2E-073-tab-total-control-sort-kolom-dasar | FE+BE |
| TC-AC-RP-248 | E2E | TC-AC-RP-E2E-074-tab-total-control-sort-kolom-lanjutan | FE+BE |
| TC-AC-RP-249 | E2E | TC-AC-RP-E2E-074-tab-total-control-sort-kolom-lanjutan | FE+BE |
| TC-AC-RP-250 | E2E | TC-AC-RP-E2E-074-tab-total-control-sort-kolom-lanjutan | FE+BE |
| TC-AC-RP-251 | E2E | TC-AC-RP-E2E-075-tab-total-control-setup-column | FE+BE |
| TC-AC-RP-252 | E2E | TC-AC-RP-E2E-075-tab-total-control-setup-column | FE+BE |
| TC-AC-RP-253 | E2E | TC-AC-RP-E2E-075-tab-total-control-setup-column | FE+BE |
| TC-AC-RP-254 | E2E | TC-AC-RP-E2E-075-tab-total-control-setup-column | FE+BE |
| TC-AC-RP-255 | E2E | TC-AC-RP-E2E-075-tab-total-control-setup-column | FE+BE |
| TC-AC-RP-256 | E2E | TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system | FE+BE |
| TC-AC-RP-257 | E2E | TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system | FE+BE |
| TC-AC-RP-258 | E2E | TC-AC-RP-E2E-087-resilience-download-gagal | FE+BE (intercept) |
| TC-AC-RP-259 | E2E | TC-AC-RP-E2E-076-tab-retensi-state-pagination | FE+BE |
| TC-AC-RP-260 | E2E | TC-AC-RP-E2E-076-tab-retensi-state-pagination | FE+BE |
| TC-AC-RP-261 | E2E | TC-AC-RP-E2E-076-tab-retensi-state-pagination | FE+BE |
| TC-AC-RP-262 | E2E | TC-AC-RP-E2E-130-role-detail-reset-paginasi-dan-pilihan-pagination | FE+BE |
| TC-AC-RP-263 | E2E | TC-AC-RP-E2E-130-role-detail-reset-paginasi-dan-pilihan-pagination | FE+BE |
| TC-AC-RP-264 | E2E | TC-AC-RP-E2E-077-tab-group-manager-search-filter | FE+BE |
| TC-AC-RP-265 | E2E | TC-AC-RP-E2E-077-tab-group-manager-search-filter | FE+BE |
| TC-AC-RP-266 | E2E | TC-AC-RP-E2E-077-tab-group-manager-search-filter | FE+BE |
| TC-AC-RP-267 | E2E | TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | FE+BE |
| TC-AC-RP-268 | E2E | TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | FE+BE |
| TC-AC-RP-269 | E2E | TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | FE+BE |
| TC-AC-RP-270 | E2E | TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | FE+BE |
| TC-AC-RP-271 | E2E | TC-AC-RP-E2E-078-tab-group-manager-sort-dan-setup-column | FE+BE |
| TC-AC-RP-272 | E2E | TC-AC-RP-E2E-079-tab-system-search-sort-setup-column | FE+BE |
| TC-AC-RP-273 | E2E | TC-AC-RP-E2E-079-tab-system-search-sort-setup-column | FE+BE |
| TC-AC-RP-274 | E2E | TC-AC-RP-E2E-079-tab-system-search-sort-setup-column | FE+BE |
| TC-AC-RP-275 | E2E | TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system | FE+BE |
| TC-AC-RP-276 | E2E | TC-AC-RP-E2E-080-role-detail-search-filter | FE+BE |
| TC-AC-RP-277 | E2E | TC-AC-RP-E2E-080-role-detail-search-filter | FE+BE |
| TC-AC-RP-278 | E2E | TC-AC-RP-E2E-080-role-detail-search-filter | FE+BE |
| TC-AC-RP-279 | E2E | TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | FE+BE |
| TC-AC-RP-280 | E2E | TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | FE+BE |
| TC-AC-RP-281 | E2E | TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | FE+BE |
| TC-AC-RP-282 | E2E | TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | FE+BE |
| TC-AC-RP-283 | E2E | TC-AC-RP-E2E-081-role-detail-sort-dan-column-visibility | FE+BE |
| TC-AC-RP-284 | E2E | TC-AC-RP-E2E-086-download-berkas-role-detail-dan-changelog | FE+BE |
| TC-AC-RP-285 | E2E | TC-AC-RP-E2E-086-download-berkas-role-detail-dan-changelog | FE+BE |
| TC-AC-RP-286 | E2E | TC-AC-RP-E2E-082-tabel-approvers | FE+BE |
| TC-AC-RP-287 | E2E | TC-AC-RP-E2E-082-tabel-approvers | FE+BE |
| TC-AC-RP-288 | E2E | TC-AC-RP-E2E-082-tabel-approvers | FE+BE |
| TC-AC-RP-289 | E2E | TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | FE+BE |
| TC-AC-RP-290 | E2E | TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | FE+BE |
| TC-AC-RP-291 | E2E | TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | FE+BE |
| TC-AC-RP-292 | E2E | TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | FE+BE |
| TC-AC-RP-293 | E2E | TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | FE+BE |
| TC-AC-RP-294 | E2E | TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | FE+BE |
| TC-AC-RP-295 | E2E | TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | FE+BE |
| TC-AC-RP-296 | E2E | TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | FE+BE |
| TC-AC-RP-297 | E2E | TC-AC-RP-E2E-089-modal-changelog-screening-per-varian | FE+BE |
| TC-AC-RP-298 | E2E | TC-AC-RP-E2E-090-modal-changelog-isi-per-varian | FE+BE |
| TC-AC-RP-299 | E2E | TC-AC-RP-E2E-090-modal-changelog-isi-per-varian | FE+BE |
| TC-AC-RP-300 | E2E | TC-AC-RP-E2E-090-modal-changelog-isi-per-varian | FE+BE |
| TC-AC-RP-301 | E2E | TC-AC-RP-E2E-090-modal-changelog-isi-per-varian | FE+BE |
| TC-AC-RP-302 | E2E | TC-AC-RP-E2E-091-modal-changelog-search-dan-filter | FE+BE |
| TC-AC-RP-303 | E2E | TC-AC-RP-E2E-091-modal-changelog-search-dan-filter | FE+BE |
| TC-AC-RP-304 | E2E | TC-AC-RP-E2E-091-modal-changelog-search-dan-filter | FE+BE |
| TC-AC-RP-305 | E2E | TC-AC-RP-E2E-091-modal-changelog-search-dan-filter | FE+BE |
| TC-AC-RP-306 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-307 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-308 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-309 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-310 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-311 | E2E | TC-AC-RP-E2E-092-modal-changelog-sort-dan-hover | FE+BE |
| TC-AC-RP-312 | E2E | TC-AC-RP-E2E-093-modal-changelog-setup-column-dan-empty-state | FE+BE |
| TC-AC-RP-313 | E2E | TC-AC-RP-E2E-093-modal-changelog-setup-column-dan-empty-state | FE+BE |
| TC-AC-RP-314 | E2E | TC-AC-RP-E2E-086-download-berkas-role-detail-dan-changelog | FE+BE |
| TC-AC-RP-315 | E2E | TC-AC-RP-E2E-087-resilience-download-gagal | FE+BE (intercept) |
| TC-AC-RP-316 | E2E | TC-AC-RP-E2E-088-volume-download-changelog-di-atas-5000-baris | FE+BE |
| TC-AC-RP-317 | E2E | TC-AC-RP-E2E-094-log-assign-dan-remove-total-control | FE+BE |
| TC-AC-RP-318 | E2E | TC-AC-RP-E2E-101-absence-log-no-op-dan-cascade | FE+BE |
| TC-AC-RP-319 | E2E | TC-AC-RP-E2E-094-log-assign-dan-remove-total-control | FE+BE |
| TC-AC-RP-320 | E2E | TC-AC-RP-E2E-095-log-assign-read-only-dan-group-manager | FE+BE |
| TC-AC-RP-321 | E2E | TC-AC-RP-E2E-095-log-assign-read-only-dan-group-manager | FE+BE |
| TC-AC-RP-322 | E2E | TC-AC-RP-E2E-095-log-assign-read-only-dan-group-manager | FE+BE |
| TC-AC-RP-323 | E2E | TC-AC-RP-E2E-096-log-assign-user-to-role | FE+BE |
| TC-AC-RP-324 | E2E | TC-AC-RP-E2E-096-log-assign-user-to-role | FE+BE |
| TC-AC-RP-325 | E2E | TC-AC-RP-E2E-097-log-edit-crud-dan-bulk-remove | FE+BE |
| TC-AC-RP-326 | E2E | TC-AC-RP-E2E-097-log-edit-crud-dan-bulk-remove | FE+BE |
| TC-AC-RP-327 | E2E | TC-AC-RP-E2E-098-log-auto-revert | FE+BE |
| TC-AC-RP-328 | E2E | TC-AC-RP-E2E-098-log-auto-revert | FE+BE |
| TC-AC-RP-329 | E2E | TC-AC-RP-E2E-097-log-edit-crud-dan-bulk-remove | FE+BE |
| TC-AC-RP-330 | E2E | TC-AC-RP-E2E-099-log-toggle-require-approval | FE+BE |
| TC-AC-RP-331 | E2E | TC-AC-RP-E2E-099-log-toggle-require-approval | FE+BE |
| TC-AC-RP-332 | E2E | TC-AC-RP-E2E-100-log-additional-approver | FE+BE |
| TC-AC-RP-333 | E2E | TC-AC-RP-E2E-100-log-additional-approver | FE+BE |
| TC-AC-RP-334 | E2E | TC-AC-RP-E2E-101-absence-log-no-op-dan-cascade | FE+BE |
| TC-AC-RP-335 | E2E | TC-AC-RP-E2E-132-absence-log-edit-nilai-sama-dan-delete-group | FE+BE |
| TC-AC-RP-336 | E2E | TC-AC-RP-E2E-094-log-assign-dan-remove-total-control | FE+BE |
| TC-AC-RP-337 | E2E | TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred | FE+BE |
| TC-AC-RP-338 | E2E | TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred | FE+BE |
| TC-AC-RP-339 | E2E | TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred | FE+BE |
| TC-AC-RP-340 | E2E | TC-AC-RP-E2E-103-notifikasi-in-app-auto-revert-deferred | FE+BE |
| TC-AC-RP-341 | E2E | TC-AC-RP-E2E-103-notifikasi-in-app-auto-revert-deferred | FE+BE |
| TC-AC-RP-342 | E2E | TC-AC-RP-E2E-103-notifikasi-in-app-auto-revert-deferred | FE+BE |
| TC-AC-RP-343 | E2E | TC-AC-RP-E2E-133-notifikasi-in-app-tanpa-notifikasi-dan-auto-revert-detail-user-deferred | FE+BE |
| TC-AC-RP-344 | E2E | TC-AC-RP-E2E-133-notifikasi-in-app-tanpa-notifikasi-dan-auto-revert-detail-user-deferred | FE+BE |
| TC-AC-RP-345 | E2E | TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user | FE+BE |
| TC-AC-RP-346 | E2E | TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user | FE+BE |
| TC-AC-RP-347 | E2E | TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user | FE+BE |
| TC-AC-RP-348 | E2E | TC-AC-RP-E2E-104-sinkron-tab-role-settings-user-dan-detail-user | FE+BE |
| TC-AC-RP-349 | E2E | TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses | FE+BE |
| TC-AC-RP-350 | E2E | TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses | FE+BE |
| TC-AC-RP-351 | E2E | TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses | FE+BE |
| TC-AC-RP-352 | E2E | TC-AC-RP-E2E-105-sinkron-settings-group-sidebar-delete-group-dan-banner-tingkat-akses | FE+BE |
| TC-AC-RP-353 | E2E | TC-AC-RP-E2E-134-sinkron-pindah-entitas-antar-group-dan-wewenang-gm | FE+BE |
| TC-AC-RP-354 | E2E | TC-AC-RP-E2E-106-konsumen-grup-gm-dan-group-role-exact-match | FE+BE |
| TC-AC-RP-355 | E2E | TC-AC-RP-E2E-106-konsumen-grup-gm-dan-group-role-exact-match | FE+BE |
| TC-AC-RP-356 | E2E | TC-AC-RP-E2E-106-konsumen-grup-gm-dan-group-role-exact-match | FE+BE |
| TC-AC-RP-357 | E2E | TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | FE+BE |
| TC-AC-RP-358 | E2E | TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | FE+BE |
| TC-AC-RP-359 | E2E | TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | FE+BE |
| TC-AC-RP-360 | E2E | TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | FE+BE |
| TC-AC-RP-361 | E2E | TC-AC-RP-E2E-107-konsumen-allocation-toggle-dan-bypass-approval | FE+BE |
| TC-AC-RP-362 | E2E | TC-AC-RP-E2E-108-konsumen-allocation-remove-approver-toggle-tidak-retroaktif | FE+BE |
| TC-AC-RP-363 | E2E | TC-AC-RP-E2E-108-konsumen-allocation-remove-approver-toggle-tidak-retroaktif | FE+BE |
| TC-AC-RP-364 | E2E | TC-AC-RP-E2E-108-konsumen-allocation-remove-approver-toggle-tidak-retroaktif | FE+BE |
| TC-AC-RP-365 | E2E | TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi | FE+BE |
| TC-AC-RP-366 | E2E | TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission | FE+BE |
| TC-AC-RP-367 | E2E | TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission | FE+BE |
| TC-AC-RP-368 | E2E | TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission | FE+BE |
| TC-AC-RP-369 | E2E | TC-AC-RP-E2E-109-konsumen-allocation-fallback-reviewer-wallet-dan-permission | FE+BE |
| TC-AC-RP-370 | E2E | TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi | FE+BE |
| TC-AC-RP-371 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-372 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-373 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-374 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-375 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-376 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-377 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |
| TC-AC-RP-378 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-379 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-380 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-381 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-382 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-383 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-384 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-385 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-386 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-387 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-388 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-389 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-390 | E2E | TC-AC-RP-E2E-115-defense-request-langsung-eligibility-dan-payload | FE+BE |
| TC-AC-RP-391 | E2E | TC-AC-RP-E2E-112-state-tenant-entitas-suspended | FE+BE |
| TC-AC-RP-392 | E2E | TC-AC-RP-E2E-112-state-tenant-entitas-suspended | FE+BE |
| TC-AC-RP-393 | E2E | TC-AC-RP-E2E-112-state-tenant-entitas-suspended | FE+BE |
| TC-AC-RP-394 | E2E | TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain | FE+BE |
| TC-AC-RP-395 | E2E | TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain | FE+BE |
| TC-AC-RP-396 | E2E | TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain | FE+BE |
| TC-AC-RP-397 | E2E | TC-AC-RP-E2E-117-stale-edit-remove-tingkat-akses-oleh-admin-lain | FE+BE |
| TC-AC-RP-398 | E2E | TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah | FE+BE |
| TC-AC-RP-399 | E2E | TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah | FE+BE |
| TC-AC-RP-400 | E2E | TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah | FE+BE |
| TC-AC-RP-401 | E2E | TC-AC-RP-E2E-118-stale-remove-idempoten-dan-status-target-berubah | FE+BE |
| TC-AC-RP-402 | E2E | TC-AC-RP-E2E-119-stale-group-terpilih-dihapus | FE+BE |
| TC-AC-RP-403 | E2E | TC-AC-RP-E2E-119-stale-group-terpilih-dihapus | FE+BE |
| TC-AC-RP-404 | E2E | TC-AC-RP-E2E-137-stale-node-group-dihapus-toast-netral-approver-dan-toggle | FE+BE |
| TC-AC-RP-405 | E2E | TC-AC-RP-E2E-137-stale-node-group-dihapus-toast-netral-approver-dan-toggle | FE+BE |
| TC-AC-RP-406 | E2E | TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi | FE+BE |
| TC-AC-RP-407 | E2E | TC-AC-RP-E2E-111-double-submit-dan-total-control-minimal-satu | FE+BE |
| TC-AC-RP-408 | E2E | TC-AC-RP-E2E-111-double-submit-dan-total-control-minimal-satu | FE+BE |
| TC-AC-RP-409 | E2E | TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi | FE+BE |
| TC-AC-RP-410 | E2E | TC-AC-RP-E2E-111-double-submit-dan-total-control-minimal-satu | FE+BE |
| TC-AC-RP-411 | E2E | TC-AC-RP-E2E-066-table-user-picker-perilaku-umum | FE+BE |
| TC-AC-RP-412 | E2E | TC-AC-RP-E2E-045-assign-user-to-role-screening-dan-pool | FE+BE |
| TC-AC-RP-413 | E2E | TC-AC-RP-E2E-059-assign-approver-global-role-screening-dan-assign | FE+BE |
| TC-AC-RP-414 | E2E | TC-AC-RP-E2E-135-state-tenant-entitas-expired | FE+BE |
| TC-AC-RP-415 | E2E | TC-AC-RP-E2E-043-resilience-tulis-assign-dan-remove-total-control | FE+BE (intercept) |
| TC-AC-RP-416 | E2E | TC-AC-RP-E2E-124-assign-total-control-cascade-group-role-multi-user-pending-dan-inactive | FE+BE |
| TC-AC-RP-417 | E2E | TC-AC-RP-E2E-102-notifikasi-in-app-remove-deferred | FE+BE |
| TC-AC-RP-418 | E2E | TC-AC-RP-E2E-136-defense-prioritas-pesan-403-beberapa-kondisi | FE+BE |
| TC-AC-RP-419 | E2E | TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver | FE+BE |
| TC-AC-RP-420 | E2E | TC-AC-RP-E2E-058-resilience-tulis-remove-role-detail-dan-approver | FE+BE |
| TC-AC-RP-421 | E2E | TC-AC-RP-E2E-132-absence-log-edit-nilai-sama-dan-delete-group | FE+BE |
| TC-AC-RP-422 | E2E | TC-AC-RP-E2E-060-assign-approver-group-role-dan-v09 | FE+BE |
| TC-AC-RP-423 | E2E | TC-AC-RP-E2E-083-picker-search-filter-sort-pagination | FE+BE |
| TC-AC-RP-424 | E2E | TC-AC-RP-E2E-085-download-berkas-tab-total-control-dan-system | FE+BE |
| TC-AC-RP-425 | E2E | TC-AC-RP-E2E-084-picker-kolom-curated-search | FE+BE |
| TC-AC-RP-426 | E2E | TC-AC-RP-E2E-139-mobile-volume-card-list-pagination-select-all-android | FE+BE |
| TC-AC-RP-427 | E2E | TC-AC-RP-E2E-019-mobile-selection-mode-android | FE+BE |
| TC-AC-RP-428 | E2E | TC-AC-RP-E2E-084-picker-kolom-curated-search | FE+BE |
| TC-AC-RP-429 | E2E | TC-AC-RP-E2E-084-picker-kolom-curated-search | FE+BE |
| TC-AC-RP-430 | E2E | TC-AC-RP-E2E-011-role-detail-varian-distributor | FE+BE |
| TC-AC-RP-431 | E2E | TC-AC-RP-E2E-046-assign-user-to-global-role-aksi-berhasil | FE+BE |
| TC-AC-RP-432 | E2E | TC-AC-RP-E2E-069-volume-selection-limit-role-detail-dan-picker | FE+BE |
| TC-AC-RP-433 | E2E | TC-AC-RP-E2E-094-log-assign-dan-remove-total-control | FE+BE |
| TC-AC-RP-434 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-435 | E2E | TC-AC-RP-E2E-116-defense-selection-limit-request-langsung, TC-AC-RP-E2E-138-absence-log-selection-limit-request-langsung | FE+BE |
| TC-AC-RP-436 | E2E | TC-AC-RP-E2E-116-defense-selection-limit-request-langsung, TC-AC-RP-E2E-138-absence-log-selection-limit-request-langsung | FE+BE |
| TC-AC-RP-437 | E2E | TC-AC-RP-E2E-128-table-user-picker-aktor-dan-empty-state | FE+BE |
| TC-AC-RP-438 | E2E | TC-AC-RP-E2E-114-defense-request-langsung-target-terlindungi-dan-diri-sendiri | FE+BE |
| TC-AC-RP-439 | E2E | TC-AC-RP-E2E-061-remove-approver-single | FE+BE |
| TC-AC-RP-440 | E2E | TC-AC-RP-E2E-065-toggle-require-approval-manage-user-and-role | FE+BE (intercept) |
| TC-AC-RP-441 | E2E | TC-AC-RP-E2E-065-toggle-require-approval-manage-user-and-role | FE+BE (intercept) |
| TC-AC-RP-442 | E2E | TC-AC-RP-E2E-099-log-toggle-require-approval | FE+BE |
| TC-AC-RP-443 | E2E | TC-AC-RP-E2E-113-defense-request-langsung-read-only-dan-manage-user-role | FE+BE |

---

## 4. Ringkasan Suite dan Catatan

### 4.1 Ringkasan

- 138 spec menurunkan 443 TC (TC-AC-RP-1 sampai 443); setiap TC masuk spec, TC Hanya-BE: 0. TC-AC-RP-435 dan 436 ada di `sourceTc` dua spec: 116 (presence: penolakan request langsung) dan 138 (absence: tidak ada entri Changelog); semua TC lain tepat satu spec. 131 spec `coverage.web: automated`, 3 spec notifikasi [DEFERRED] (102, 103, 133) `coverage.web: unsupported`, 0 spec `deferred`, 4 spec mobile Android (017, 018, 019, 139) `coverage.mobile: automated` tanpa `coverage.web`.
- Semua spec bermode FE+BE (backend nyata, seeding via API); 10 di antaranya memakai intercept respons (Pre-setup #23) di atas backend nyata untuk resilience dan tetap ditandai FE+BE, bukan mock. Tidak ada spec `Mode: mock`.
- Suite serial karena banyak spec mengubah Pre-setup bersama (tingkat akses, penugasan Group Manager, approver, toggle, Selection Limit, entitas Suspended atau Expired, flag Guided Tooltip). Hook, akun default, sesi API aktor, dan kemampuan reset baseline dinyatakan di `suite.md`.
- Akun aktor memakai 13 env password baru `AC_RP_*_PASSWORD` (lihat 4.5).

### 4.2 Pemecahan dari Rencana

Rencana awal 119 spec (001-119). Penulis slice memecah beberapa spec yang melewati batas dan memakai nomor cadangan 120-130 dan 132-139 (nomor 131 tidak dipakai); spec 138 memuat klausa absence TC-AC-RP-435 dan 436 (kelas harness g) dan spec 139 memuat TC-AC-RP-426 (kelas volume data, bagian 3 prinsip 13e); TC-AC-RP-427 ada di spec 019. Pemetaan sourceTc final adalah yang tertulis di frontmatter spec dan di tabel bagian 1 dan 3. Nomor tidak direnumber; nomor 131 tidak dipakai.

### 4.3 Spec di Atas ~35 Langkah (20 spec)

Dihitung dengan `grep -cE '^[0-9]+\. '` pada `spec.md` tiap spec (butir C6 `scripts/check-suite.py`, batas lebih dari 35 langkah): 026 (39); 036 (37); 045 (41); 058 (46); 083 (38); 085 (45); 089 (38); 091 (37); 092 (36); 094 (48); 095 (45); 097 (47); 098 (41); 099 (44); 102 (40); 110 (42); 117 (41); 118 (43); 125 (38); 132 (39) (nomor spec, jumlah langkah). Spec 044 dan 059 tepat 35 langkah sehingga tidak termasuk. Seluruh 20 spec punya alasan di `## Notes`: umumnya blok TC satu kelas fungsional atau satu kelas harness pada permukaan yang sama (modal Changelog, surface log, resilience satu permukaan, notifikasi, multi-konteks, stale), tiap blok berdiri sendiri dengan data dan pemulihan sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Alasan eksplisit lain: 083 (38 langkah) satu alur picker Table User yang sama; 085 (45 langkah) langkah unduh dan baca berkas yang berulang per format dan per tab. Ke-20 spec diterima dan tidak dipecah (keputusan user).

### 4.4 TC [DEFERRED] Notifikasi

Sembilan TC notifikasi in-app §8.8 (TC-AC-RP-337 sampai 344 dan 417) ditulis dengan awalan `[DEFERRED]`: kontrak event normatif, pengiriman masih implementasi mendatang. Spec 102 (337, 338, 339, 417), 103 (340, 341, 342), dan 133 (343, 344) kini bermarkah `coverage.web: unsupported` (keputusan user) karena modul Notification belum ada; spec diaktifkan lagi (`automated`) saat modul Notification selesai. Spec tetap ada dan TC tetap terpetakan.

### 4.5 Temuan QA Terpenting (Berulang di Banyak Spec)

1. Mekanisme "dipulihkan automation baseline" (kolom Post Condition) tidak didefinisikan di TC, PRD, maupun LLD. Spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13) dan menjalankannya sebagai langkah penghubung serta di hook `after`.
2. 13 env password `AC_RP_*_PASSWORD` (mis. `AC_RP_TC_PASSWORD`, `AC_RP_DU_PASSWORD`, `AC_RP_RO_PASSWORD`, `AC_RP_MUR_U_PASSWORD`, `AC_RP_MUR_R_PASSWORD`, `AC_RP_GM_PASSWORD`) belum terdaftar di `spectra.config.ts` (`executionConfig.environmentVariables`) dan `.env.example`; harus didaftarkan pemilik repo e2e sebelum tahap script.
3. Akun user Standard dan Admin B (Pre-setup #24) tidak punya email di tabel Pre-setup; spec menyebutnya disediakan tim FE.
4. Fixture `fixtures/settings-role-permission.json` belum ada; nama user, group, dan role pada langkah ditulis sesuai TC sampai fixture dibuat di tahap script.
5. Kontradiksi TC-AC-RP-203 terhadap TC-AC-RP-413 dan TC-AC-RP-437; spec mengikuti Expected tiap TC apa adanya dan perlu dijernihkan QA.
6. TC-AC-RP-439 (aktor yang sudah menjadi approver me-Remove baris miliknya) ada di tabel 3h file TC dan dipetakan ke spec 061.
7. TC-AC-RP-435 dan TC-AC-RP-436 ada di `sourceTc` dua spec (S-05): spec 116 menguji penolakan request langsung (presence) dan spec 138 mengasersi klausa "tidak ada entri log" (kelas g; pemicu request langsung, anchor positif status 422 dan pesan penolakan, baseline jumlah entri Changelog). Pemeriksa `check-suite.py` melaporkan pasangan ini sebagai REVIEW C2.
8. Kemampuan membaca jumlah entri audit trail (Changelog, System Log, Activity Log, Changelog: User) untuk baseline dan selisih kini dinyatakan di `suite.md` (Hook suite); spec menyebutnya kemampuan yang disediakan tim FE/BE (S-12).
9. TC-AC-RP-184 berbeda label tombol dari NC-01; spec mengikuti Expected TC dan butuh kepastian label dari QA.

### 4.6 Perbaikan Penutupan

Pada tahap penutupan: C6 spec 083 dan 085 diberi alasan di Notes; C9 spec 101 langkah 9 dikalimatkan "Verifikasi Changelog memuat entri baru ber-Action ..." sebagai anchor positif untuk asersi absence langkah 10 (anchor memang ada tetapi tidak dikenali pemeriksa); C10 spec 125 priority Low dinaikkan ke Medium mengikuti TC sumber tertinggi. `spectra lint --strict` dan `check-suite.py` bersih.

