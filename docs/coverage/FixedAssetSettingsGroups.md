# Coverage E2E — Fixed Asset > Settings > Groups

Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md` (1070 TC granular aktif). Berkas `tc-settings-groups-backend.md` tidak ada (0 TC hanya-BE).
Suite: `specs/FixedAsset/SettingsGroups/`.
Prefix Modul: `FA` + `GRP` (`TC-FA-GRP-E2E-*`).
Status semua spec: `draft`.

Catatan penomoran: spec 001 sampai 276 mengikuti rencana (`plan-e2e-generate-spec.md`); tujuh nomor cadangan terpakai untuk pemecahan spec (277, 278, 279, 281, 282, 283, 284), sedangkan nomor cadangan 280 tidak dipakai. Spec 285 sampai 289 menambah cakupan baris pola Group Role dan Transaction Role Total Control/Read Only (TC-FA-GRP-1289 sampai 1292); nomor cadangan 290 dan 291 tidak dipakai. Spec 290 sampai 297 menambah cakupan pola Group Manager (GM) pada Create Subgroup/Group, Delete, Total User, dan Import (TC-FA-GRP-1293 sampai 1300); dua nomor cadangan terpakai untuk pemecahan (298 untuk TC-FA-GRP-1296 dari rencana spec 290, 300 untuk TC-FA-GRP-1298 dari rencana spec 293), sedangkan 299 tidak dipakai. Spec 301 sampai 306 menambah cakupan Transaction Role yang mencakup node beserta descendant-nya pada Create Subgroup, Import, dan Delete (TC-FA-GRP-1301 sampai 1303; fungsional dan absence per TC); nomor cadangan 307 terpakai untuk TC-FA-GRP-1304 (guard Delete kondisi 5 tidak menghitung baris pola GM ancestor; keputusan NC-12), sedangkan 308 tidak dipakai. Total 304 spec atomik. Spec 057 (dialog Change Function varian Disposal Group, TC-FA-GRP-177 sampai 182) dihapus karena seluruh TC sumbernya dihapus dari TestCases pada sinkron 2026-11-12 (konsep Disposal Group dihapus; Function hanya None dan Assignable); nomor 057 tidak dipakai lagi.

Kolom Mode dibaca dari butir `Mode:` pada `## Prerequisites` tiap spec. Kolom Langkah adalah jumlah langkah bernomor nominal pada `## Test Steps` (perulangan atas tabel Prerequisites belum diekspansi). Spec berlabel `mock` berjumlah 0; seluruh spec lain memakai backend nyata (`FE+BE`), termasuk spec fault injection yang hanya mencegat sebagian respons di atas backend nyata.

---

## 1. Pemetaan TC Granular → Spec E2E (306 Spec Atomik)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | Screening Groups List All Groups: Header, Kolom, Format Sel, Nama 120 Karakter, Hover Nama dan Table Tools, Halaman Tanpa Page Title | FE+BE | 47 | TC-FA-GRP-1, TC-FA-GRP-2, TC-FA-GRP-3, TC-FA-GRP-4, TC-FA-GRP-5, TC-FA-GRP-952 |
| TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | Interaksi Baris Groups List: Klik Area Baris, Ikon dan Urutan Row Action, Ikon dan Severity Bulk Action Delete, Tidak Ada Aksi Activate/Deactivate/Move, dan Nama All Groups Tidak Tersimpan sebagai Row | FE+BE | 33 | TC-FA-GRP-6, TC-FA-GRP-943, TC-FA-GRP-944, TC-FA-GRP-950, TC-FA-GRP-951 |
| TC-FA-GRP-E2E-003-loading-state-dan-error-load-groups-list-try-again | Loading State dan Error Load Groups List dengan [Try Again] | FE+BE | 12 | TC-FA-GRP-7, TC-FA-GRP-8 |
| TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | Client Baru: Empty State Seed Default Group, Modified By System, Seed Tidak Dicatat Changelog, dan Modal Changelog Genuine Empty | FE+BE | 40 | TC-FA-GRP-9, TC-FA-GRP-428, TC-FA-GRP-888, TC-FA-GRP-893, TC-FA-GRP-894, TC-FA-GRP-1128 |
| TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | Sidebar Group Tree: Screening, Tooltip Dot Function, Urutan A-Z, Node Excess, dan Aksesibilitas ARIA Treeitem | FE+BE | 50 | TC-FA-GRP-10, TC-FA-GRP-11, TC-FA-GRP-14, TC-FA-GRP-42, TC-FA-GRP-43, TC-FA-GRP-967 |
| TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | Sidebar Group Tree: Expand/Collapse All, Toggle Open/Collapse, State Persisten, Collapse Otomatis di Bawah 1280px, dan Label 120 Karakter | FE+BE | 30 | TC-FA-GRP-12, TC-FA-GRP-13, TC-FA-GRP-1085, TC-FA-GRP-1092, TC-FA-GRP-1093 |
| TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | Search Sidebar Group Tree: Nama, Code, Tanpa Hasil, Dikosongkan, dan Tidak Dipertahankan saat Refresh | FE+BE | 25 | TC-FA-GRP-15, TC-FA-GRP-16, TC-FA-GRP-17, TC-FA-GRP-18, TC-FA-GRP-19 |
| TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | Navigasi Node Sidebar: Direct Children, All Groups, Klik Ulang No-Op, Leaf, serta Transisi Masuk dan Keluar Empty State Subgroup | FE+BE | 34 | TC-FA-GRP-20, TC-FA-GRP-21, TC-FA-GRP-22, TC-FA-GRP-23, TC-FA-GRP-945, TC-FA-GRP-946 |
| TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | Group Context Header: Judul, Metrik Total Asset/Total User Exact-Match, dan Klik Angka Membuka Detail Group | FE+BE | 34 | TC-FA-GRP-24, TC-FA-GRP-26, TC-FA-GRP-27, TC-FA-GRP-28, TC-FA-GRP-968 |
| TC-FA-GRP-E2E-010-group-context-header-all-groups-agregat-distinct-union-scope-aktor-scoped-dan-angka-tidak-dapat-diklik | Group Context Header All Groups: Agregat Client Distinct Dedup, Union Scope Aktor Scoped (User di Luar Scope Tidak Dihitung), dan Angka Tidak Dapat Diklik | FE+BE | 19 | TC-FA-GRP-25, TC-FA-GRP-29, TC-FA-GRP-969 |
| TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | Refresh F5 Mempertahankan Node Terpilih dan State Tabel, Node Terpilih Dihapus (Langsung, Cascade, Oleh User Lain), dan Klik Ulang Menu Groups | FE+BE | 38 | TC-FA-GRP-30, TC-FA-GRP-31, TC-FA-GRP-32, TC-FA-GRP-33, TC-FA-GRP-1122 |
| TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | Guided Tooltip Groups: Kunjungan Pertama Tiga Step, [Done], [Skip], Replay [?] Tidak Mereset Flag, dan Posisi Tombol Replay | FE+BE | 46 | TC-FA-GRP-34, TC-FA-GRP-35, TC-FA-GRP-36, TC-FA-GRP-37, TC-FA-GRP-1095 |
| TC-FA-GRP-E2E-013-guided-tooltip-groups-navigasi-keluar-resize-viewport-dan-keyboard | Guided Tooltip Groups: Navigasi Keluar, Resize Viewport, dan Keyboard | FE+BE | 32 | TC-FA-GRP-38, TC-FA-GRP-39, TC-FA-GRP-1094 |
| TC-FA-GRP-E2E-014-android-guided-tooltip-drawer-dan-group-context-header-aktor-scoped | Android: Guided Tooltip Membuka Drawer Otomatis, Group Context Header di Atas Toolbar, dan [+] Group Hanya Total Control/Default User | FE+BE | 24 | TC-FA-GRP-971, TC-FA-GRP-985 |
| TC-FA-GRP-E2E-015-role-matrix-visibilitas-elemen-groups-list-total-control-dan-default-user | Role Matrix: Visibilitas Elemen Groups List per Role (Total Control dan Default User) | FE+BE | 27 | TC-FA-GRP-44, TC-FA-GRP-45 |
| TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | Role Matrix: Visibilitas Elemen Groups List per Role Scoped Region West (Group Manager, Manage Group CRUD, R, R+C, R+U, R+D) | FE+BE | 23 | TC-FA-GRP-47, TC-FA-GRP-48, TC-FA-GRP-49, TC-FA-GRP-50, TC-FA-GRP-51, TC-FA-GRP-52 |
| TC-FA-GRP-E2E-017-role-matrix-negatif-menu-groups-hidden-dan-akses-url-langsung | Role Matrix Negatif: Menu Settings > Groups Hidden dan Direct URL Ditolak untuk Role Tanpa Capability Manage Group | FE+BE | 15 | TC-FA-GRP-53, TC-FA-GRP-54, TC-FA-GRP-55 |
| TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match | Group Manager Scope Region West: Sidebar Scope + Ancestor Context, Ancestor Tidak Bisa Dipilih, Metrik Exact-Match, dan Node di Luar Scope | FE+BE | 19 | TC-FA-GRP-56, TC-FA-GRP-57, TC-FA-GRP-61, TC-FA-GRP-74 |
| TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope | Aktor Scoped Variasi Scope: Guided Tooltip Tanpa [+] Group, All Groups Level 1 Ter-assign, Empty State Tanpa Node, Dan Node Terpilih Keluar Scope | FE+BE | 27 | TC-FA-GRP-40, TC-FA-GRP-58, TC-FA-GRP-59, TC-FA-GRP-1062 |
| TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | Role Matrix Positif Create: Add Subgroup oleh Manage Group R+C dan Group Manager, [+] Group oleh Default User, Auto-Assign Creator | FE+BE | 66 | TC-FA-GRP-64, TC-FA-GRP-68, TC-FA-GRP-72, TC-FA-GRP-132, TC-FA-GRP-890 |
| TC-FA-GRP-E2E-021-role-matrix-positif-edit-manage-group-ru-dan-group-manager | Role Matrix Positif Edit: Edit Branch West 1 (R+U), Ubah Function (R+U), dan Edit Room 301 (Group Manager) | FE+BE | 26 | TC-FA-GRP-65, TC-FA-GRP-69, TC-FA-GRP-947 |
| TC-FA-GRP-E2E-022-role-matrix-positif-delete-manage-group-rd-dan-group-manager | Role Matrix Positif Delete: Delete Node Kosong dan Bulk Delete Dua Node (R+D) serta Delete oleh Group Manager | FE+BE | 21 | TC-FA-GRP-66, TC-FA-GRP-67, TC-FA-GRP-70 |
| TC-FA-GRP-E2E-023-role-matrix-gating-checkbox-bulk-aktor-d-parsial-dan-tanpa-d | Role Matrix Gating Checkbox: Disabled pada Node Tanpa D, Kolom Checkbox Hidden Tanpa D, dan Baris Disabled Tidak Ikut Select All | FE+BE | 16 | TC-FA-GRP-62, TC-FA-GRP-63, TC-FA-GRP-1123 |
| TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | Role Matrix Aksi Baris: Descendant Scope CRUD, Klik Nama oleh Read-Only/Read Saja, dan Node Excess Tanpa Edit/Add Subgroup per Role | FE+BE | 46 | TC-FA-GRP-60, TC-FA-GRP-71, TC-FA-GRP-73, TC-FA-GRP-75, TC-FA-GRP-76, TC-FA-GRP-77 |
| TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | Popup Detail Group: Buka via Nama dan Row Action, Screening Header Stacked Read-Only, Function None, dan Node Excess | FE+BE | 38 | TC-FA-GRP-270, TC-FA-GRP-271, TC-FA-GRP-272, TC-FA-GRP-273, TC-FA-GRP-274 |
| TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | Popup Detail Group: Tutup via [X] dan Esc, Backdrop Tidak Menutup, Refleksi Live Setelah Edit, Tab Awal per Jalur Akses, dan Node Dihapus (404) | FE+BE | 52 | TC-FA-GRP-284, TC-FA-GRP-285, TC-FA-GRP-986, TC-FA-GRP-1017, TC-FA-GRP-1148 |
| TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | Tab Assets Detail Group: Himpunan Aset Exact-Match Belum Disposed/Deleted, Status Aturan Resolusi, dan Nama Aset Teks Biasa | FE+BE | 35 | TC-FA-GRP-275, TC-FA-GRP-276, TC-FA-GRP-288, TC-FA-GRP-289, TC-FA-GRP-290, TC-FA-GRP-987 |
| TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime | Klik Total Asset: Membuka Tab Assets, Total Asset 0 Empty State, dan Angka Realtime Setelah Aset Ditambah | FE+BE | 26 | TC-FA-GRP-277, TC-FA-GRP-286, TC-FA-GRP-287, TC-FA-GRP-292 |
| TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets | Resilience Popup Detail: Loading per Tab dan Error Load Tab Users/Tab Assets Tidak Memengaruhi Tab Lain | FE+BE | 34 | TC-FA-GRP-282, TC-FA-GRP-283, TC-FA-GRP-291, TC-FA-GRP-298 |
| TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user | Tab Users Detail Group: Himpunan UNION Total User, Total User Tidak Pernah 0, dan User Non-Aktif/Temporary User Lewat Temporary Until | FE+BE | 31 | TC-FA-GRP-293, TC-FA-GRP-294, TC-FA-GRP-295, TC-FA-GRP-988 |
| TC-FA-GRP-E2E-031-tab-users-detail-kolom-group-role-per-jenis-user-avatar-nama-dan-realtime-assignment | Tab Users Detail Group: Kolom Group Role per Jenis User, Kolom Name Avatar + Full Name, dan Total User Realtime Setelah Assignment Role | FE+BE | 27 | TC-FA-GRP-296, TC-FA-GRP-299, TC-FA-GRP-1011 |
| TC-FA-GRP-E2E-032-popup-detail-group-state-search-filter-sort-paginasi-per-tab-dipulihkan-dan-direset | Popup Detail Group: State Search/Filter/Sort/Paginasi per Tab Dipulihkan Saat Kembali ke Tab, Tidak Memengaruhi Tab Lain, dan Direset Saat Popup Ditutup | FE+BE | 32 | TC-FA-GRP-1052, TC-FA-GRP-1053, TC-FA-GRP-1054 |
| TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | Popup New Group: Screening, Create Level 1 (Code Manual, Function Assignable), Field Opsional Kosong, dan Stay on This Form | FE+BE | 46 | TC-FA-GRP-79, TC-FA-GRP-80, TC-FA-GRP-81, TC-FA-GRP-83 |
| TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | Popup New Group: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling Case-Insensitive, dan Nama Sama di Parent Lain | FE+BE | 27 | TC-FA-GRP-85, TC-FA-GRP-86, TC-FA-GRP-87, TC-FA-GRP-88, TC-FA-GRP-89 |
| TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | Popup New Group: Nama Reserved All Groups, Emoji Diblok dan Ditolak Server, Auto-Trim Name/Code/Description, dan Name Hanya Spasi | FE+BE | 29 | TC-FA-GRP-90, TC-FA-GRP-91, TC-FA-GRP-92, TC-FA-GRP-93, TC-FA-GRP-949, TC-FA-GRP-1055 |
| TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | Popup New Group: Validasi Code 15/16 Karakter, Karakter di Luar Whitelist, Auto-Uppercase, Duplikat Case-Insensitive, dan Code Dipakai Saat Submit | FE+BE | 26 | TC-FA-GRP-94, TC-FA-GRP-95, TC-FA-GRP-96, TC-FA-GRP-97, TC-FA-GRP-98, TC-FA-GRP-99 |
| TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | Popup New Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan Tombol [Clear Field] | FE+BE | 25 | TC-FA-GRP-100, TC-FA-GRP-101, TC-FA-GRP-102, TC-FA-GRP-103, TC-FA-GRP-104 |
| TC-FA-GRP-E2E-038-new-group-hover-saving-submit-double-click-dan-aksesibilitas | Popup New Group: Hover dan Saving State [Submit], Double-Click [Submit] Hanya Satu Request, dan Aksesibilitas Focus Trap/Esc | FE+BE | 24 | TC-FA-GRP-105, TC-FA-GRP-109, TC-FA-GRP-111 |
| TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | Popup New Group: Tutup Tanpa/Dengan Perubahan (Unsaved Changes), Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser | FE+BE | 42 | TC-FA-GRP-106, TC-FA-GRP-107, TC-FA-GRP-108, TC-FA-GRP-1027, TC-FA-GRP-1030 |
| TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | Plan Gating Preemptif: Block Cap Jumlah Group (Starter 1, Growth 3), Stay on Form Sampai Cap, Urutan Cek Count Sebelum Depth, Tombol Tidak Disable, dan Cap Dihitung terhadap Semua Node Terlepas Function | FE+BE | 35 | TC-FA-GRP-84, TC-FA-GRP-112, TC-FA-GRP-113, TC-FA-GRP-117, TC-FA-GRP-118, TC-FA-GRP-120 |
| TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap | Plan Gating Preemptif: Block Depth Cap Growth, Batas Platform Count/Depth (Enterprise/Unlimited), dan Enterprise Hanya System Limits | FE+BE | 27 | TC-FA-GRP-114, TC-FA-GRP-115, TC-FA-GRP-116, TC-FA-GRP-121 |
| TC-FA-GRP-E2E-042-plan-gating-dialog-ok-esc-backdrop-dan-penurunan-cap-depth-tidak-memangkas-node | Plan Gating: Dialog Hanya [OK] Tanpa [Upgrade], Esc dan Backdrop Tidak Menutup, dan Penurunan Cap Depth Tidak Memangkas Node | FE+BE | 34 | TC-FA-GRP-122, TC-FA-GRP-972, TC-FA-GRP-973 |
| TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | Konflik Dua Admin: Create Tepat di Cap dan Re-Check Atomik Saat Submit (Plan Growth dan Batas Platform) | FE+BE | 37 | TC-FA-GRP-119, TC-FA-GRP-123, TC-FA-GRP-124, TC-FA-GRP-974 |
| TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar | Popup New Subgroup: Screening Baris Konteks Under, Create via Row Action dan Elipsis Sidebar, dan Tanpa Guard Parent Ber-Aset | FE+BE | 25 | TC-FA-GRP-125, TC-FA-GRP-126, TC-FA-GRP-127, TC-FA-GRP-128 |
| TC-FA-GRP-E2E-045-new-subgroup-parent-sesuai-node-aksi-dan-tombol-group-saat-node-dipilih | Create Subgroup: Parent = Node Tempat Aksi Dipicu dan [+] Group Saat Node Dipilih Tetap Membuat Level 1 | FE+BE | 17 | TC-FA-GRP-976, TC-FA-GRP-977 |
| TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | Create Subgroup: Row Action Hidden untuk Parent Excess, Parent Menjadi Excess Setelah Popup Dibuka (CRU Lock Sebelum Cap), dan Parent Dihapus Sebelum Submit | FE+BE | 41 | TC-FA-GRP-129, TC-FA-GRP-130, TC-FA-GRP-131, TC-FA-GRP-975 |
| TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | Popup New Subgroup: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain | FE+BE | 27 | TC-FA-GRP-133, TC-FA-GRP-134, TC-FA-GRP-135, TC-FA-GRP-136, TC-FA-GRP-137 |
| TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | Popup New Subgroup: Nama Reserved All Groups, Emoji, Auto-Trim Name/Code, dan Name Hanya Spasi | FE+BE | 23 | TC-FA-GRP-138, TC-FA-GRP-139, TC-FA-GRP-140, TC-FA-GRP-141, TC-FA-GRP-1056 |
| TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | Popup New Subgroup: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit | FE+BE | 26 | TC-FA-GRP-142, TC-FA-GRP-143, TC-FA-GRP-144, TC-FA-GRP-145, TC-FA-GRP-146, TC-FA-GRP-147 |
| TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | Popup New Subgroup: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field] | FE+BE | 26 | TC-FA-GRP-148, TC-FA-GRP-149, TC-FA-GRP-150, TC-FA-GRP-151, TC-FA-GRP-152 |
| TC-FA-GRP-E2E-051-new-subgroup-hover-saving-submit-double-click-dan-aksesibilitas | Popup New Subgroup: Hover dan Saving State [Submit], Double-Click, dan Aksesibilitas | FE+BE | 24 | TC-FA-GRP-153, TC-FA-GRP-157, TC-FA-GRP-159 |
| TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | Popup New Subgroup: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser | FE+BE | 42 | TC-FA-GRP-154, TC-FA-GRP-155, TC-FA-GRP-156, TC-FA-GRP-1028, TC-FA-GRP-1031 |
| TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | Popup Edit Group: Screening Pre-filled Tanpa Baris Under/Stay dan Ubah Name, Code, atau Description Saja | FE+BE | 39 | TC-FA-GRP-160, TC-FA-GRP-161, TC-FA-GRP-162, TC-FA-GRP-163 |
| TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi | Edit Group: Ubah Name dan Code Sekaligus, Code Dikosongkan Di-Generate Ulang, Code Identik Diperlakukan No-Op, dan Nama Sama Beda Kapitalisasi | FE+BE | 20 | TC-FA-GRP-164, TC-FA-GRP-165, TC-FA-GRP-166, TC-FA-GRP-167 |
| TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved | Edit Group: Tanpa Perubahan (No-Op), Ubah Lalu Revert, Kapitalisasi/Spasi Tepi No-Op, dan Dialog Unsaved Tidak Muncul Setelah Revert | FE+BE | 18 | TC-FA-GRP-168, TC-FA-GRP-169, TC-FA-GRP-170, TC-FA-GRP-978 |
| TC-FA-GRP-E2E-056-edit-function-assignable-ke-none-dialog-change-function | Edit Function Assignable ke None: Screening Dialog Change Function, [Save], dan [Cancel] | FE+BE | 11 | TC-FA-GRP-171, TC-FA-GRP-172, TC-FA-GRP-173 |
| TC-FA-GRP-E2E-058-edit-function-none-ke-assignable-tanpa-dialog-histori-transaksi-dan-bersamaan-name | Edit Function None ke Assignable Tanpa Dialog, Function dari Assignable dengan Histori Transaksi, dan Function Bersamaan dengan Name | FE+BE | 19 | TC-FA-GRP-183, TC-FA-GRP-185, TC-FA-GRP-186 |
| TC-FA-GRP-E2E-059-edit-function-tanpa-inheritance-dan-dialog-change-function-setelah-validasi-lolos | Edit Function Tanpa Inheritance (Parent Ber-Child) dan Dialog Change Function Hanya Muncul Setelah Validasi Form Lolos | FE+BE | 21 | TC-FA-GRP-979, TC-FA-GRP-1025 |
| TC-FA-GRP-E2E-060-edit-node-excess-node-menjadi-excess-saat-popup-terbuka-dan-node-dihapus-user-lain | Edit pada Node Excess: Row Action Edit Hidden, Node Menjadi Excess Setelah Popup Dibuka, dan Node Dihapus User Lain Sebelum Save | FE+BE | 30 | TC-FA-GRP-187, TC-FA-GRP-188, TC-FA-GRP-189 |
| TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | Popup Edit Group: Validasi Group Name Kosong, 120/121 Karakter, Duplikat Sibling, dan Nama Sama di Parent Lain | FE+BE | 28 | TC-FA-GRP-191, TC-FA-GRP-192, TC-FA-GRP-193, TC-FA-GRP-194, TC-FA-GRP-195 |
| TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | Popup Edit Group: Nama Reserved, Emoji, Auto-Trim Name/Code, dan Name Diganti Spasi Saja | FE+BE | 24 | TC-FA-GRP-196, TC-FA-GRP-197, TC-FA-GRP-198, TC-FA-GRP-199, TC-FA-GRP-1057 |
| TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | Popup Edit Group: Validasi Code 15/16 Karakter, Whitelist, Auto-Uppercase, Duplikat, dan Code Dipakai Saat Submit | FE+BE | 26 | TC-FA-GRP-200, TC-FA-GRP-201, TC-FA-GRP-202, TC-FA-GRP-203, TC-FA-GRP-204, TC-FA-GRP-205 |
| TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | Popup Edit Group: Description 360/361 Karakter, Tooltip Function, Radio Function, dan [Clear Field] | FE+BE | 25 | TC-FA-GRP-206, TC-FA-GRP-207, TC-FA-GRP-208, TC-FA-GRP-209, TC-FA-GRP-210 |
| TC-FA-GRP-E2E-065-edit-group-hover-saving-save-double-click-dan-aksesibilitas | Popup Edit Group: Hover dan Saving State [Save], Double-Click [Save], dan Aksesibilitas | FE+BE | 26 | TC-FA-GRP-211, TC-FA-GRP-215, TC-FA-GRP-217 |
| TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | Popup Edit Group: Tutup Tanpa/Dengan Perubahan, Guard Browser, Klik Backdrop, serta Navigasi Sidebar dan Back Browser | FE+BE | 40 | TC-FA-GRP-212, TC-FA-GRP-213, TC-FA-GRP-214, TC-FA-GRP-1029, TC-FA-GRP-1032 |
| TC-FA-GRP-E2E-067-resilience-form-new-group-new-subgroup-dan-edit-group-gagal-server | Resilience Form: Gagal Server (5xx/Timeout) Mempertahankan Form pada Popup New Group, New Subgroup, dan Edit Group | FE+BE | 25 | TC-FA-GRP-110, TC-FA-GRP-158, TC-FA-GRP-216 |
| TC-FA-GRP-E2E-068-code-auto-generate-token-numerik-inisial-alfabetik-dan-pemisah | Code Auto-Generate: Token Numerik Passthrough, Inisial per Token Alfabetik, dan Pemisah -, _, / | FE+BE | 7 | TC-FA-GRP-321, TC-FA-GRP-322, TC-FA-GRP-323 |
| TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | Code Auto-Generate: Token Alfanumerik, Karakter Tidak Valid, Token Tanpa Karakter Valid, dan Fallback 4 Karakter Acak | FE+BE | 11 | TC-FA-GRP-324, TC-FA-GRP-325, TC-FA-GRP-326, TC-FA-GRP-327, TC-FA-GRP-328 |
| TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | Code Auto-Generate: Dedup Tier 1 Suffix Angka, Tier 2 ParentCode, Batas 5 Percobaan, Truncate 15 Karakter, dan Keunikan Case-Insensitive | FE+BE | 22 | TC-FA-GRP-329, TC-FA-GRP-330, TC-FA-GRP-331, TC-FA-GRP-332, TC-FA-GRP-333, TC-FA-GRP-1064 |
| TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | Delete Group: Screening Dialog Konfirmasi, [Cancel], Delete via Elipsis Sidebar, Delete Node Assignable Berisi Aset Disposed, Delete Node Kosong, dan Cascade Subtree Kosong | FE+BE | 36 | TC-FA-GRP-218, TC-FA-GRP-219, TC-FA-GRP-220, TC-FA-GRP-221, TC-FA-GRP-222, TC-FA-GRP-239 |
| TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning | Delete Group: Dialog Warning User Ter-Scope, Warning User di Descendant, dan [Cancel] pada Dialog Warning | FE+BE | 36 | TC-FA-GRP-223, TC-FA-GRP-224, TC-FA-GRP-1033 |
| TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver | Delete Group: User TC/RO/Default User Saja, Home Group, User Non-Aktif/Temporary, dan Transaction Role Approver Memicu Dialog Konfirmasi Normal | FE+BE | 17 | TC-FA-GRP-225, TC-FA-GRP-226, TC-FA-GRP-980, TC-FA-GRP-1059 |
| TC-FA-GRP-E2E-074-delete-diblok-last-group-satu-satunya-group-dan-satu-satunya-root-dengan-subgroup | Delete Diblok: Last Group (Satu-Satunya Group dan Satu-Satunya Root dengan Subgroup) | FE+BE | 32 | TC-FA-GRP-227, TC-FA-GRP-228 |
| TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | Delete Diblok: Aset Aktif di Node dan Descendant, Aset Draft/Waiting for Approval, dan Guard Pertama yang Terpenuhi Menentukan Dialog | FE+BE | 40 | TC-FA-GRP-229, TC-FA-GRP-230, TC-FA-GRP-231, TC-FA-GRP-238 |
| TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-belum-tuntas | Delete Diblok: Tujuan Transfer Waiting for Approval/Departure/In Transfer Process | FE+BE | 42 | TC-FA-GRP-232, TC-FA-GRP-233, TC-FA-GRP-234 |
| TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif | Delete Diblok: Scope Aktor Scoped Menjadi Kosong, Aktor dengan Lebih dari Satu Node Scope, dan Scope Efektif Tidak Menghitung Role Non-Manage Group | FE+BE | 31 | TC-FA-GRP-236, TC-FA-GRP-237, TC-FA-GRP-961, TC-FA-GRP-1058 |
| TC-FA-GRP-E2E-078-delete-race-node-dihapus-user-lain-double-click-dan-aksesibilitas-dialog | Delete: Node Dihapus User Lain Sebelum [Delete], Double-Click [Delete], dan Aksesibilitas Dialog (Focus Trap, Esc) | FE+BE | 31 | TC-FA-GRP-242, TC-FA-GRP-244, TC-FA-GRP-245 |
| TC-FA-GRP-E2E-079-delete-dan-bulk-delete-node-excess-auto-reset-excess-saat-count-di-bawah-cap | Delete dan Bulk Delete Node Excess: Auto-Reset Excess Bila Count <= Cap dan Tidak Mereset Excess Lain Saat Count > Cap | FE+BE | 28 | TC-FA-GRP-240, TC-FA-GRP-241, TC-FA-GRP-269 |
| TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | Bulk Action Bar: Screening 1 Baris Dicentang, Counter Singular/Plural, Checkbox Header, Select All Lintas Halaman, dan Uncheck dari 100% | FE+BE | 37 | TC-FA-GRP-246, TC-FA-GRP-247, TC-FA-GRP-248, TC-FA-GRP-249, TC-FA-GRP-250 |
| TC-FA-GRP-E2E-081-bulk-seleksi-persist-lintas-halaman-search-filter-dan-reset-saat-node-berganti | Bulk Seleksi: Persist Lintas Halaman/Search/Filter, Dipertahankan di Node yang Sama dan Direset Saat Node Berganti, dan Retensi Saat Search/Filter Dikosongkan | FE+BE | 26 | TC-FA-GRP-251, TC-FA-GRP-426, TC-FA-GRP-982 |
| TC-FA-GRP-E2E-082-bulk-selection-limit-diturunkan-blok-live-dan-select-all-di-cap | Bulk Selection Limit: Centang ke-[Selection Limit]+1 Diblok Live dan Select All Di-Cap Otomatis | FE+BE | 15 | TC-FA-GRP-252, TC-FA-GRP-253 |
| TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | Bulk Delete: Dialog Homogen, Kelompok Bullet User Ter-Scope, N=1 Collapse ke Dialog Single, dan [Cancel] | FE+BE | 40 | TC-FA-GRP-254, TC-FA-GRP-255, TC-FA-GRP-261, TC-FA-GRP-263, TC-FA-GRP-1034 |
| TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total | Bulk Delete: Dialog Campuran dengan [Continue] dan Toast Ringkasan, Campuran dengan User Ter-Scope, Semua Terblok, dan N=1 Terblok | FE+BE | 43 | TC-FA-GRP-256, TC-FA-GRP-257, TC-FA-GRP-258, TC-FA-GRP-262 |
| TC-FA-GRP-E2E-085-bulk-delete-would-empty-dan-scope-aktor-jadi-kosong | Bulk Delete: Would-Empty Dicek Paling Awal dan Scope Aktor Menjadi Kosong | FE+BE | 14 | TC-FA-GRP-259, TC-FA-GRP-260 |
| TC-FA-GRP-E2E-086-bulk-delete-kondisi-berubah-setelah-dialog-semua-terskip-dan-item-sudah-dihapus | Bulk Delete: Kondisi Berubah Setelah Dialog (Re-Evaluasi per Group), Seluruh Item Terskip, dan Item Sudah Dihapus User Lain | FE+BE | 22 | TC-FA-GRP-264, TC-FA-GRP-265, TC-FA-GRP-266 |
| TC-FA-GRP-E2E-087-bulk-delete-parent-dan-descendant-tidak-sama-sama-terpilih-dan-satu-group-identik-single | Bulk Delete: Parent dan Descendant Tidak Sama-Sama Terpilih (Cascade) dan Satu Group Terpilih Identik dengan Delete Single | FE+BE | 25 | TC-FA-GRP-268, TC-FA-GRP-981 |
| TC-FA-GRP-E2E-088-resilience-delete-bulk-delete-dan-wizard-gagal-server | Resilience: Delete Single, Bulk Delete, dan Simpan Wizard Gagal Server Mempertahankan State | FE+BE | 27 | TC-FA-GRP-243, TC-FA-GRP-267, TC-FA-GRP-307 |
| TC-FA-GRP-E2E-089-android-delete-single-dan-bulk-delete-long-press-floating-bottom-bulk-bar | Android: Seleksi Massal Hanya Long-Press dengan Floating Bottom Bulk Bar dan Delete Single/Bulk Memakai Dialog dan Toast Sama dengan Desktop | FE+BE | 25 | TC-FA-GRP-983, TC-FA-GRP-984 |
| TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | Wizard Group Consolidation: Screening Step, Counter Real-Time, Melebihi Cap dan 0 Tercentang Menonaktifkan [Save Selection], dan Centang Kurang dari Cap | FE+BE | 30 | TC-FA-GRP-300, TC-FA-GRP-301, TC-FA-GRP-302, TC-FA-GRP-304, TC-FA-GRP-962 |
| TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0 | Wizard: Submit Tepat Cap Diterapkan di T-0, Submit Setelah T-0 Langsung Diterapkan, dan Submit Ulang Sebelum T-0 | FE+BE | 44 | TC-FA-GRP-303, TC-FA-GRP-305, TC-FA-GRP-306 |
| TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | Fallback T-0: Group Terlama Tetap Usable, Tie-Break Nama A-Z, Seleksi Kosong karena Group Dihapus, Fallback Tidak Jalan Setelah Submit, dan Plan Naik Auto-Reset Excess | FE+BE | 39 | TC-FA-GRP-310, TC-FA-GRP-311, TC-FA-GRP-318, TC-FA-GRP-319, TC-FA-GRP-964 |
| TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | T-0 dan Seleksi Tersimpan: Count <= Cap Dibuang, Group Baru Tidak Tercentang, Group Tercentang Dihapus, Downgrade Dibatalkan, Cap Baru Berubah, dan Penerapan Sync Satu Transaksi | FE+BE | 45 | TC-FA-GRP-312, TC-FA-GRP-313, TC-FA-GRP-314, TC-FA-GRP-315, TC-FA-GRP-316, TC-FA-GRP-317, TC-FA-GRP-1051 |
| TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | Wizard: [Cancel] Tanpa dan Dengan Perubahan (Unsaved Changes), Klik Total Asset/Total User Membuka Detail Group, dan Server Menolak Seleksi Melebihi Cap atau Kosong (Dialog D-23) | FE+BE | 54 | TC-FA-GRP-308, TC-FA-GRP-309, TC-FA-GRP-948, TC-FA-GRP-965, TC-FA-GRP-966 |
| TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan | Wizard: Sort Default dan Sort Kolom Group/Total Asset/Total User serta Search Nama dan Angka dengan Centang Dipertahankan | FE+BE | 35 | TC-FA-GRP-957, TC-FA-GRP-958, TC-FA-GRP-1043, TC-FA-GRP-1044 |
| TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | Wizard: Interaksi Search (Reveal, Enter, Clear, Collapse) serta Filter Group (Isi Opsi, Dua Opsi OR, Search Dropdown) | FE+BE | 38 | TC-FA-GRP-1037, TC-FA-GRP-1038, TC-FA-GRP-1039, TC-FA-GRP-1040 |
| TC-FA-GRP-E2E-097-wizard-filter-total-asset-total-user-chip-opsi-dan-penerapan-ke-tabel | Wizard: Filter Group/Total Asset/Total User dan Chip Opsi Filter Group (Hapus via (X) dan via Uncheck) | FE+BE | 29 | TC-FA-GRP-959, TC-FA-GRP-1041, TC-FA-GRP-1042 |
| TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir | Wizard Setup Column: Column Visibility, Screening Popup 3 Zona + Live Preview, dan Guard Kolom Terakhir yang Visible | FE+BE | 20 | TC-FA-GRP-960, TC-FA-GRP-1096, TC-FA-GRP-1097, TC-FA-GRP-1101 |
| TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | Wizard Setup Column: Uncheck Kolom Group/Total Asset/Total User, [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain | FE+BE | 36 | TC-FA-GRP-1098, TC-FA-GRP-1102, TC-FA-GRP-1103, TC-FA-GRP-1104 |
| TC-FA-GRP-E2E-100-wizard-setup-column-geser-drag-dan-pin-kolom | Wizard Setup Column: Geser (Drag) dan Pin Kolom Group, Total Asset, dan Total User | FE+BE | 23 | TC-FA-GRP-1099, TC-FA-GRP-1100 |
| TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | Alert Group Consolidation Pasca-T-0: Tampil untuk Total Control/Default User Saat Group > Cap, Hidden Saat <= Cap atau untuk Aktor Lain, Cap Turun Langsung, dan Tidak Ada Entry Point Sebelum T-0 | FE+BE | 39 | TC-FA-GRP-320, TC-FA-GRP-1107, TC-FA-GRP-1108, TC-FA-GRP-1109, TC-FA-GRP-1114, TC-FA-GRP-1115 |
| TC-FA-GRP-E2E-102-alert-group-consolidation-popup-choose-groups-save-selection-cancel-dan-counter | Alert Group Consolidation: [Choose Groups] Membuka Popup Konten Step, [Save Selection] Diterapkan Seketika, dan Counter dengan Batas Cap dan Minimal 1 | FE+BE | 31 | TC-FA-GRP-1110, TC-FA-GRP-1111, TC-FA-GRP-1117 |
| TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | Alert Group Consolidation Popup: Tutup via (X) dan Esc, Klik Backdrop Tidak Menutup, serta Dialog Unsaved Changes Saat Ada Perubahan Centang | FE+BE | 39 | TC-FA-GRP-1116, TC-FA-GRP-1124, TC-FA-GRP-1125, TC-FA-GRP-1126 |
| TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | Konflik Dua Admin: Delete Dua Group Terakhir, Create/Rename Nama Sama, Aset/User/Transfer Ditambah Setelah Dialog, dan Would-Empty/Scope-Empty Dievaluasi Ulang Saat Commit | FE+BE | 60 | TC-FA-GRP-936, TC-FA-GRP-937, TC-FA-GRP-938, TC-FA-GRP-939, TC-FA-GRP-940, TC-FA-GRP-941, TC-FA-GRP-942, TC-FA-GRP-1063 |
| TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide | Groups List Search: Interaksi (Reveal, Enter, Clear, Collapse), Last Updated Tidak Match, dan Kolom Code yang Di-Hide | FE+BE | 46 | TC-FA-GRP-336, TC-FA-GRP-343, TC-FA-GRP-344 |
| TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | Groups List Search per Kolom Group, Code, Function (Nilai Penuh None dan Assignable) | FE+BE | 21 | TC-FA-GRP-337, TC-FA-GRP-338, TC-FA-GRP-339, TC-FA-GRP-419, TC-FA-GRP-420 |
| TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node | Groups List Search per Kolom Total Asset, Total User, Modified By, dan Search Lokal Terhadap Node Terpilih | FE+BE | 18 | TC-FA-GRP-340, TC-FA-GRP-341, TC-FA-GRP-342, TC-FA-GRP-418 |
| TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | Groups List Filter Panel: Screening, Isi Opsi Function, Filter Function Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 35 | TC-FA-GRP-345, TC-FA-GRP-346, TC-FA-GRP-347, TC-FA-GRP-348, TC-FA-GRP-349 |
| TC-FA-GRP-E2E-109-groups-list-filter-function-chip-opsi-dan-kombinasi-and-antar-field | Groups List Filter: Chip Opsi Function (Hapus via X dan Uncheck) dan Kombinasi Function + Total Asset (AND) | FE+BE | 35 | TC-FA-GRP-350, TC-FA-GRP-351, TC-FA-GRP-363 |
| TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator | Groups List Filter: Tetap Berlaku Saat Kolom Function Di-Hide, Menutup Panel Tanpa [Apply] Membuang Draft, dan Indikator Filter Aktif | FE+BE | 47 | TC-FA-GRP-1118, TC-FA-GRP-1130, TC-FA-GRP-1131 |
| TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | Groups List Filter Total Asset dan Total User: Rentang Min-Max dan Hanya Min atau Hanya Max | FE+BE | 47 | TC-FA-GRP-352, TC-FA-GRP-353, TC-FA-GRP-354, TC-FA-GRP-355 |
| TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown | Groups List Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 30 | TC-FA-GRP-356, TC-FA-GRP-357, TC-FA-GRP-358, TC-FA-GRP-359 |
| TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | Groups List Filter: Chip Opsi Modified By, Rentang Last Updated, dan [Clear Field] | FE+BE | 50 | TC-FA-GRP-360, TC-FA-GRP-361, TC-FA-GRP-362, TC-FA-GRP-364 |
| TC-FA-GRP-E2E-114-groups-list-kombinasi-search-lalu-filter-dan-filter-lalu-search-irisan | Groups List Kombinasi: Search lalu Filter dan Filter lalu Search (Irisan) | FE+BE | 34 | TC-FA-GRP-365, TC-FA-GRP-366 |
| TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state | Groups List Kombinasi: Clear Search Saat Filter/Sort Aktif, Ganti Target Sort Saat Search/Filter Aktif, dan Pemulihan dari Empty State | FE+BE | 48 | TC-FA-GRP-377, TC-FA-GRP-378, TC-FA-GRP-379 |
| TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral | Groups List Sort Kolom Group, Code, Function, dan Total Asset (Asc, Desc, Netral) | FE+BE | 10 | TC-FA-GRP-367, TC-FA-GRP-368, TC-FA-GRP-369, TC-FA-GRP-370 |
| TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | Groups List Sort Kolom Total User, Modified By, Last Updated, Guard Kolom Non-Sortable, dan Tie-Breaker Deterministik | FE+BE | 33 | TC-FA-GRP-371, TC-FA-GRP-372, TC-FA-GRP-373, TC-FA-GRP-374, TC-FA-GRP-1132 |
| TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | Groups List Setup Column: Screening Overlay Column Visibility dan Popup 3 Zona, Guard Kolom Terakhir, dan Pin ke-4 Diblok | FE+BE | 35 | TC-FA-GRP-380, TC-FA-GRP-381, TC-FA-GRP-403, TC-FA-GRP-1087 |
| TC-FA-GRP-E2E-119-groups-list-setup-column-reset-to-default-esc-dan-cache-tidak-memengaruhi-tabel-lain | Groups List Setup Column: [Reset to Default], (X) dan Esc Membatalkan, dan Cache Tidak Memengaruhi Tabel Lain | FE+BE | 35 | TC-FA-GRP-404, TC-FA-GRP-405, TC-FA-GRP-406 |
| TC-FA-GRP-E2E-120-groups-list-setup-column-uncheck-kolom-group-code-function-total-asset | Groups List Setup Column: Uncheck Kolom Group, Code, Function, dan Total Asset | FE+BE | 14 | TC-FA-GRP-382, TC-FA-GRP-383, TC-FA-GRP-384, TC-FA-GRP-385 |
| TC-FA-GRP-E2E-121-groups-list-setup-column-uncheck-kolom-total-user-modified-by-last-updated | Groups List Setup Column: Uncheck Kolom Total User, Modified By, dan Last Updated | FE+BE | 14 | TC-FA-GRP-386, TC-FA-GRP-387, TC-FA-GRP-388 |
| TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset | Groups List Setup Column: Geser (Drag) Kolom Group, Code, Function, dan Total Asset | FE+BE | 13 | TC-FA-GRP-389, TC-FA-GRP-390, TC-FA-GRP-391, TC-FA-GRP-392 |
| TC-FA-GRP-E2E-123-groups-list-setup-column-geser-drag-kolom-total-user-modified-by-last-updated | Groups List Setup Column: Geser (Drag) Kolom Total User, Modified By, dan Last Updated | FE+BE | 13 | TC-FA-GRP-393, TC-FA-GRP-394, TC-FA-GRP-395 |
| TC-FA-GRP-E2E-124-groups-list-setup-column-pin-kolom-group-code-dan-function | Groups List Setup Column: Pin Kolom Group, Code, dan Function | FE+BE | 16 | TC-FA-GRP-396, TC-FA-GRP-397, TC-FA-GRP-398 |
| TC-FA-GRP-E2E-125-groups-list-setup-column-pin-kolom-total-asset-dan-total-user | Groups List Setup Column: Pin Kolom Total Asset dan Total User | FE+BE | 16 | TC-FA-GRP-399, TC-FA-GRP-400 |
| TC-FA-GRP-E2E-126-groups-list-setup-column-pin-kolom-modified-by-dan-last-updated | Groups List Setup Column: Pin Kolom Modified By dan Last Updated | FE+BE | 16 | TC-FA-GRP-401, TC-FA-GRP-402 |
| TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | Groups List Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, Kolom Hide/Unhide, Node Leaf Header Saja, dan Node Terpilih + Scope Aktor Server-Side | FE+BE | 55 | TC-FA-GRP-407, TC-FA-GRP-408, TC-FA-GRP-409, TC-FA-GRP-410, TC-FA-GRP-421, TC-FA-GRP-1127 |
| TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | Groups List Download Isi Berkas CSV/XLSX: Transformasi Tipe Badge, Number, Date, Empty, Function None/Modified By, BOM UTF-8 dan Escaping | FE+BE | 25 | TC-FA-GRP-412, TC-FA-GRP-413, TC-FA-GRP-414, TC-FA-GRP-415, TC-FA-GRP-422, TC-FA-GRP-1133 |
| TC-FA-GRP-E2E-129-groups-list-download-lebih-5000-baris-loading-screen-tanpa-job-background | Groups List Download > 5.000 Baris: Loading Screen Sampai Berkas Siap Tanpa Job Background | FE+BE | 9 | TC-FA-GRP-423 |
| TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | Groups List Pagination: Default dan Page Size, Navigasi Prev/Next dan Input Halaman, serta Reset ke Halaman 1 Saat Search/Filter | FE+BE | 38 | TC-FA-GRP-416, TC-FA-GRP-417, TC-FA-GRP-1023, TC-FA-GRP-1024 |
| TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi | Groups List: Mutasi Saat Tabel Terfilter/Ter-Search (Create dan Rename) dan Paginasi Kasus Tepi (Halaman Tidak Valid, Hapus Baris Terakhir, Ganti Page Size/Sort) | FE+BE | 37 | TC-FA-GRP-424, TC-FA-GRP-425, TC-FA-GRP-1134 |
| TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | Modal Changelog Group: Screening, Baris Marked/Restored Excess, Aktor Scoped Hanya Riwayat dalam Scope, dan Total Control/Read Only/Default User Melihat Seluruh Riwayat | FE+BE | 47 | TC-FA-GRP-427, TC-FA-GRP-429, TC-FA-GRP-430, TC-FA-GRP-991 |
| TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide | Modal Changelog Search: Interaksi, Kolom Date Tidak Match, dan Kolom Group Name yang Di-Hide | FE+BE | 47 | TC-FA-GRP-432, TC-FA-GRP-439, TC-FA-GRP-440 |
| TC-FA-GRP-E2E-134-modal-changelog-search-per-kolom-action-group-name-dan-field | Modal Changelog Search per Kolom Action, Group Name, dan Field | FE+BE | 14 | TC-FA-GRP-433, TC-FA-GRP-434, TC-FA-GRP-435 |
| TC-FA-GRP-E2E-135-modal-changelog-search-per-kolom-old-value-new-value-dan-modified-by | Modal Changelog Search per Kolom Old Value, New Value, dan Modified By | FE+BE | 14 | TC-FA-GRP-436, TC-FA-GRP-437, TC-FA-GRP-438 |
| TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and | Modal Changelog Filter: Screening Panel, Rentang Date, Kombinasi Date + Action (AND), dan [Clear Field] | FE+BE | 31 | TC-FA-GRP-441, TC-FA-GRP-442, TC-FA-GRP-467, TC-FA-GRP-468 |
| TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Modal Changelog Filter Action: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 32 | TC-FA-GRP-443, TC-FA-GRP-444, TC-FA-GRP-445, TC-FA-GRP-446 |
| TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Modal Changelog Filter Group Name: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 33 | TC-FA-GRP-449, TC-FA-GRP-450, TC-FA-GRP-451, TC-FA-GRP-452 |
| TC-FA-GRP-E2E-139-modal-changelog-filter-field-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Modal Changelog Filter Field: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 32 | TC-FA-GRP-455, TC-FA-GRP-456, TC-FA-GRP-457, TC-FA-GRP-458 |
| TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Modal Changelog Filter Modified By: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 32 | TC-FA-GRP-461, TC-FA-GRP-462, TC-FA-GRP-463, TC-FA-GRP-464 |
| TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name | Modal Changelog Filter: Chip Opsi Action dan Group Name (Hapus via X dan via Uncheck) | FE+BE | 31 | TC-FA-GRP-447, TC-FA-GRP-448, TC-FA-GRP-453, TC-FA-GRP-454 |
| TC-FA-GRP-E2E-142-modal-changelog-filter-chip-opsi-field-dan-modified-by | Modal Changelog Filter: Chip Opsi Field dan Modified By (Hapus via X dan via Uncheck) | FE+BE | 31 | TC-FA-GRP-459, TC-FA-GRP-460, TC-FA-GRP-465, TC-FA-GRP-466 |
| TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination | Modal Changelog Kombinasi: Search lalu Filter, Filter lalu Search, dan Search + Filter + Sort + Pagination | FE+BE | 46 | TC-FA-GRP-469, TC-FA-GRP-470, TC-FA-GRP-478 |
| TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | Modal Changelog Kombinasi: Clear Filter/Search Saat Lainnya Aktif, Ganti Target Sort, dan Pemulihan dari Empty State | FE+BE | 44 | TC-FA-GRP-479, TC-FA-GRP-480, TC-FA-GRP-481, TC-FA-GRP-482 |
| TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field | Modal Changelog Sort Kolom Date, Action, Group Name, dan Field (Asc, Desc, Netral) | FE+BE | 12 | TC-FA-GRP-471, TC-FA-GRP-472, TC-FA-GRP-473, TC-FA-GRP-474 |
| TC-FA-GRP-E2E-146-modal-changelog-sort-kolom-old-value-new-value-dan-modified-by | Modal Changelog Sort Kolom Old Value, New Value, dan Modified By (Asc, Desc, Netral) | FE+BE | 12 | TC-FA-GRP-475, TC-FA-GRP-476, TC-FA-GRP-477 |
| TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | Modal Changelog Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok | FE+BE | 35 | TC-FA-GRP-483, TC-FA-GRP-484, TC-FA-GRP-506, TC-FA-GRP-1088 |
| TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain | Modal Changelog Setup Column: [Reset to Default], (X) dan Esc, dan Cache Tidak Memengaruhi Tabel Lain | FE+BE | 36 | TC-FA-GRP-507, TC-FA-GRP-508, TC-FA-GRP-509 |
| TC-FA-GRP-E2E-149-modal-changelog-setup-column-uncheck-kolom-date-action-group-name-dan-field | Modal Changelog Setup Column: Uncheck Kolom Date, Action, Group Name, dan Field | FE+BE | 15 | TC-FA-GRP-485, TC-FA-GRP-486, TC-FA-GRP-487, TC-FA-GRP-488 |
| TC-FA-GRP-E2E-150-modal-changelog-setup-column-uncheck-kolom-old-value-new-value-dan-modified-by | Modal Changelog Setup Column: Uncheck Kolom Old Value, New Value, dan Modified By | FE+BE | 15 | TC-FA-GRP-489, TC-FA-GRP-490, TC-FA-GRP-491 |
| TC-FA-GRP-E2E-151-modal-changelog-setup-column-geser-drag-kolom-date-action-group-name-dan-field | Modal Changelog Setup Column: Geser (Drag) Kolom Date, Action, Group Name, dan Field | FE+BE | 14 | TC-FA-GRP-492, TC-FA-GRP-493, TC-FA-GRP-494, TC-FA-GRP-495 |
| TC-FA-GRP-E2E-152-modal-changelog-setup-column-geser-drag-kolom-old-value-new-value-dan-modified-by | Modal Changelog Setup Column: Geser (Drag) Kolom Old Value, New Value, dan Modified By | FE+BE | 14 | TC-FA-GRP-496, TC-FA-GRP-497, TC-FA-GRP-498 |
| TC-FA-GRP-E2E-153-modal-changelog-setup-column-pin-kolom-date-action-dan-group-name | Modal Changelog Setup Column: Pin Kolom Date, Action, dan Group Name | FE+BE | 17 | TC-FA-GRP-499, TC-FA-GRP-500, TC-FA-GRP-501 |
| TC-FA-GRP-E2E-154-modal-changelog-setup-column-pin-kolom-field-dan-old-value | Modal Changelog Setup Column: Pin Kolom Field dan Old Value | FE+BE | 17 | TC-FA-GRP-502, TC-FA-GRP-503 |
| TC-FA-GRP-E2E-155-modal-changelog-setup-column-pin-kolom-new-value-dan-modified-by | Modal Changelog Setup Column: Pin Kolom New Value dan Modified By | FE+BE | 17 | TC-FA-GRP-504, TC-FA-GRP-505 |
| TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | Modal Changelog Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide | FE+BE | 34 | TC-FA-GRP-510, TC-FA-GRP-511, TC-FA-GRP-512, TC-FA-GRP-513 |
| TC-FA-GRP-E2E-157-modal-changelog-download-isi-berkas-transformasi-tipe-date-dan-empty | Modal Changelog Download Isi Berkas: Transformasi Tipe Date dan Empty | FE+BE | 11 | TC-FA-GRP-515, TC-FA-GRP-516 |
| TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | Modal Changelog Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter dari Halaman 2 | FE+BE | 36 | TC-FA-GRP-517, TC-FA-GRP-518, TC-FA-GRP-1060 |
| TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | Modal Changelog Kolom Group Name: Full Path Subgroup, Path Setelah Rename, Snapshot Tidak Berubah, Dua Group Bernama Sama, dan Path Saat Delete Cascade | FE+BE | 54 | TC-FA-GRP-1018, TC-FA-GRP-1019, TC-FA-GRP-1020, TC-FA-GRP-1021, TC-FA-GRP-1022 |
| TC-FA-GRP-E2E-160-resilience-download-groups-list-modal-changelog-dan-loading-error-load-changelog | Resilience: Download Groups List Gagal, Download Modal Changelog Gagal, dan Loading/Error Load Modal Changelog | FE+BE | 23 | TC-FA-GRP-411, TC-FA-GRP-431, TC-FA-GRP-514 |
| TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | Tab Users Search: Interaksi, Temporary Until Tidak Match, Email Searchable (Tidak di Filter Panel), dan Kolom Email Di-Hide | FE+BE | 44 | TC-FA-GRP-572, TC-FA-GRP-583, TC-FA-GRP-584, TC-FA-GRP-675 |
| TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division | Tab Users Search per Kolom Name, Email, Position, dan Division | FE+BE | 10 | TC-FA-GRP-573, TC-FA-GRP-574, TC-FA-GRP-575, TC-FA-GRP-576 |
| TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field | Tab Users Search per Kolom Activation Status, Temporary User, TAG, dan Custom Field | FE+BE | 10 | TC-FA-GRP-579, TC-FA-GRP-580, TC-FA-GRP-581, TC-FA-GRP-582 |
| TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | Tab Users Kolom Group Role (Multi Role Node): Search per Kolom, Tier Mendahului Group Role, Filter Mencocokkan Setiap Pemegang Role, dan Search Hanya Teks Sel | FE+BE | 38 | TC-FA-GRP-577, TC-FA-GRP-1144, TC-FA-GRP-1145, TC-FA-GRP-1146 |
| TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | Tab Users Filter: Screening Panel dan Filter Position (Isi Opsi, Satu/Dua Opsi OR, Search Dropdown) | FE+BE | 34 | TC-FA-GRP-585, TC-FA-GRP-586, TC-FA-GRP-587, TC-FA-GRP-588, TC-FA-GRP-589 |
| TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | Tab Users Filter: Chip Opsi Position dan Filter Division (Isi Opsi, Satu Opsi, Dua Opsi OR) | FE+BE | 39 | TC-FA-GRP-590, TC-FA-GRP-591, TC-FA-GRP-592, TC-FA-GRP-593 |
| TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | Tab Users Filter Division: Dua Opsi OR, Search Dropdown, dan Chip Opsi | FE+BE | 37 | TC-FA-GRP-594, TC-FA-GRP-595, TC-FA-GRP-596, TC-FA-GRP-597 |
| TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Tab Users Filter Group Role: Isi Opsi, Satu/Dua Opsi (OR), dan Search Dropdown | FE+BE | 33 | TC-FA-GRP-598, TC-FA-GRP-599, TC-FA-GRP-600, TC-FA-GRP-601 |
| TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status | Tab Users Filter: Chip Opsi Group Role dan Filter Activation Status | FE+BE | 41 | TC-FA-GRP-602, TC-FA-GRP-603, TC-FA-GRP-1012 |
| TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown | Tab Users Filter Temporary User (Yes/No), Temporary Until (Rentang), dan Custom Field Dropdown | FE+BE | 41 | TC-FA-GRP-1013, TC-FA-GRP-1014, TC-FA-GRP-1015 |
| TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and | Tab Users Filter Custom Field Multi-Dropdown dan Date serta Kombinasi AND (Group Role + Activation Status, Position + Division) | FE+BE | 28 | TC-FA-GRP-610, TC-FA-GRP-1016, TC-FA-GRP-1105, TC-FA-GRP-1106 |
| TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide | Tab Users Filter: [Clear Field], Search lalu Filter, Filter lalu Search, dan Filter Tetap Tersedia Saat Kolom Position Di-Hide | FE+BE | 33 | TC-FA-GRP-611, TC-FA-GRP-612, TC-FA-GRP-613, TC-FA-GRP-1120 |
| TC-FA-GRP-E2E-173-tab-users-filter-menutup-panel-membuang-draft-dan-opsi-tanpa-nilai-kosong | Tab Users Filter: Menutup Panel Tanpa [Apply] Membuang Draft dan Dropdown Tanpa Opsi Nilai Kosong | FE+BE | 19 | TC-FA-GRP-1135, TC-FA-GRP-1136 |
| TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division | Tab Users Sort Kolom Name, Email, Position, dan Division | FE+BE | 8 | TC-FA-GRP-614, TC-FA-GRP-615, TC-FA-GRP-616, TC-FA-GRP-617 |
| TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until | Tab Users Sort Kolom Group Role, Activation Status, Temporary User, dan Temporary Until | FE+BE | 15 | TC-FA-GRP-618, TC-FA-GRP-620, TC-FA-GRP-621, TC-FA-GRP-622 |
| TC-FA-GRP-E2E-176-tab-users-sort-kolom-tag-custom-field-dan-nilai-kosong-tie-breaker | Tab Users Sort Kolom TAG, Custom Field, dan Nilai Kosong (Akhir Asc, Awal Desc, Tie-Breaker Name) | FE+BE | 19 | TC-FA-GRP-623, TC-FA-GRP-624, TC-FA-GRP-1137 |
| TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | Tab Users Kombinasi: Search + Filter + Sort, Clear Filter/Search, Ganti Target Sort, dan Pemulihan dari Empty State | FE+BE | 30 | TC-FA-GRP-625, TC-FA-GRP-626, TC-FA-GRP-627, TC-FA-GRP-628, TC-FA-GRP-629 |
| TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | Tab Users Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok | FE+BE | 30 | TC-FA-GRP-630, TC-FA-GRP-631, TC-FA-GRP-665, TC-FA-GRP-1089 |
| TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache | Tab Users Setup Column: Batas Max Visible Columns Kolom ke-21, [Reset to Default], (X) dan Esc, serta Cache Tidak Memengaruhi Tabel Lain | FE+BE | 33 | TC-FA-GRP-666, TC-FA-GRP-667, TC-FA-GRP-668, TC-FA-GRP-1091 |
| TC-FA-GRP-E2E-180-tab-users-setup-column-uncheck-kolom-name-email-position | Tab Users Setup Column: Uncheck Kolom Name, Email, dan Position | FE+BE | 9 | TC-FA-GRP-632, TC-FA-GRP-633, TC-FA-GRP-634 |
| TC-FA-GRP-E2E-181-tab-users-setup-column-uncheck-kolom-division-group-role-dan-centang-activation-status | Tab Users Setup Column: Uncheck Division dan Group Role serta Centang Kolom Curated Activation Status | FE+BE | 9 | TC-FA-GRP-635, TC-FA-GRP-636, TC-FA-GRP-638 |
| TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field | Tab Users Setup Column: Centang Kolom Curated Temporary User, Temporary Until, TAG, dan Custom Field | FE+BE | 8 | TC-FA-GRP-639, TC-FA-GRP-640, TC-FA-GRP-641, TC-FA-GRP-642 |
| TC-FA-GRP-E2E-183-tab-users-setup-column-geser-drag-kolom-name-email-position-dan-division | Tab Users Setup Column: Geser (Drag) Kolom Name, Email, Position, dan Division | FE+BE | 9 | TC-FA-GRP-643, TC-FA-GRP-644, TC-FA-GRP-645, TC-FA-GRP-646 |
| TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until | Tab Users Setup Column: Geser (Drag) Kolom Group Role, Activation Status, Temporary User, dan Temporary Until | FE+BE | 9 | TC-FA-GRP-647, TC-FA-GRP-649, TC-FA-GRP-650, TC-FA-GRP-651 |
| TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions | Tab Users Setup Column: Geser (Drag) Kolom TAG dan Custom Field, Satu Kolom Curated per Custom Field Aktif, dan Kolom Actions Hanya Pemicu Column Visibility | FE+BE | 18 | TC-FA-GRP-652, TC-FA-GRP-653, TC-FA-GRP-676, TC-FA-GRP-954 |
| TC-FA-GRP-E2E-186-tab-users-setup-column-pin-kolom-name-email-dan-position | Tab Users Setup Column: Pin Kolom Name, Email, dan Position | FE+BE | 15 | TC-FA-GRP-654, TC-FA-GRP-655, TC-FA-GRP-656 |
| TC-FA-GRP-E2E-187-tab-users-setup-column-pin-kolom-division-group-role-dan-activation-status | Tab Users Setup Column: Pin Kolom Division, Group Role, dan Activation Status | FE+BE | 15 | TC-FA-GRP-657, TC-FA-GRP-658, TC-FA-GRP-660 |
| TC-FA-GRP-E2E-188-tab-users-setup-column-pin-kolom-temporary-user-until-dan-tag | Tab Users Setup Column: Pin Kolom Temporary User, Temporary Until, dan TAG | FE+BE | 15 | TC-FA-GRP-661, TC-FA-GRP-662, TC-FA-GRP-663 |
| TC-FA-GRP-E2E-189-tab-users-setup-column-pin-kolom-custom-field-dan-sel-tanpa-nilai-tampil-dash | Tab Users Setup Column: Pin Kolom Custom Field dan Sel Tanpa Nilai Tampil Dash (Bukan Blank) | FE+BE | 19 | TC-FA-GRP-664, TC-FA-GRP-1061 |
| TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | Tab Users Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide | FE+BE | 26 | TC-FA-GRP-669, TC-FA-GRP-670, TC-FA-GRP-671, TC-FA-GRP-672 |
| TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | Tab Users Download Isi Berkas: Tipe Empty, Badge Activation Status, Date Temporary Until, CSV BOM/Escaping, dan Kolom Group Role [N] roles | FE+BE | 36 | TC-FA-GRP-674, TC-FA-GRP-1035, TC-FA-GRP-1036, TC-FA-GRP-1138, TC-FA-GRP-1147 |
| TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi | Tab Users Pagination: Default dan Page Size, Navigasi, Reset ke Halaman 1 Saat Search/Filter, dan Kasus Tepi | FE+BE | 39 | TC-FA-GRP-1045, TC-FA-GRP-1046, TC-FA-GRP-1139 |
| TC-FA-GRP-E2E-193-resilience-download-tab-users-dan-tab-assets-gagal-server | Resilience: Download Tab Users Gagal dan Download Tab Assets Gagal | FE+BE | 19 | TC-FA-GRP-673, TC-FA-GRP-726 |
| TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log | Pencatatan Log Create: Isi Baris Changelog, System Log, dan Activity Log untuk Create Level 1, Create Subgroup, dan Create via Import | FE+BE | 48 | TC-FA-GRP-868, TC-FA-GRP-869, TC-FA-GRP-870 |
| TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | Pencatatan Log Edit: Isi Baris Changelog, System Log, dan Activity Log untuk Edit Group Name, Code, Description, dan Function | FE+BE | 60 | TC-FA-GRP-871, TC-FA-GRP-872, TC-FA-GRP-873, TC-FA-GRP-874 |
| TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | Pencatatan Log Delete: Isi Baris untuk Delete Single, Bulk Delete, Delete Cascade, dan Bulk Delete Cascade (Hanya Group yang Berhasil) | FE+BE | 57 | TC-FA-GRP-875, TC-FA-GRP-876, TC-FA-GRP-882, TC-FA-GRP-883 |
| TC-FA-GRP-E2E-197-log-marked-restored-excess-wizard-isi-baris-changelog-system-log-activity-log | Pencatatan Log Excess via Wizard: Marked as Excess dan Restored from Excess | FE+BE | 35 | TC-FA-GRP-877, TC-FA-GRP-878 |
| TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris | Pencatatan Log Excess: Marked as Excess (Fallback T-0), Restored from Excess (Plan Naik), dan Restored from Excess (Delete) | FE+BE | 45 | TC-FA-GRP-879, TC-FA-GRP-880, TC-FA-GRP-881 |
| TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | Pencatatan Log: Edit Multi-Field Tidak Hilang/Duplikat, Snapshot Immutability Setelah Rename Dua Kali, Nama Group Terhapus Tetap Terbaca, dan Modified By/Last Updated Berubah Setelah Excess | FE+BE | 36 | TC-FA-GRP-884, TC-FA-GRP-886, TC-FA-GRP-887, TC-FA-GRP-892 |
| TC-FA-GRP-E2E-200-log-pencabutan-assignment-saat-delete-di-log-user-dan-tanpa-notifikasi-in-app | Pencatatan Log Pencabutan Assignment Saat Delete (di Log User, Bukan Changelog Group) dan Tanpa Notifikasi In-App | FE+BE | 45 | TC-FA-GRP-889, TC-FA-GRP-895 |
| TC-FA-GRP-E2E-201-absence-log-edit-no-op-aksi-batal-dan-kegagalan-tulis-log-rollback | Absence Log: Edit No-Op dan Aksi Batal Tidak Menulis Baris, dan Kegagalan Tulis Activity Log Me-Rollback Mutasi | FE+BE | 41 | TC-FA-GRP-885, TC-FA-GRP-891 |
| TC-FA-GRP-E2E-202-function-berubah-efek-ke-dropdown-register-asset-dan-transfer-dua-transisi | Perubahan Function (Dua Transisi) dan Efeknya ke Dropdown Register Asset dan Transfer | FE+BE | 39 | TC-FA-GRP-896, TC-FA-GRP-898 |
| TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | Node Excess di Modul Konsumen: Tampil Tidak Dapat Dipilih, Tetap Dapat Dipilih di Scope Role/Lisensi/Reader/Home Group, Import Parent Excess Ditolak, dan Transaksi Berjalan Tetap Selesai | FE+BE | 66 | TC-FA-GRP-902, TC-FA-GRP-903, TC-FA-GRP-992, TC-FA-GRP-993, TC-FA-GRP-994 |
| TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | Post-Create/Edit/Delete Tercermin di Modul Konsumen: Dropdown, Reader Group, Home Group/Lisensi, Aset Disposed/Deleted, dan Scope Role & Permission | FE+BE | 63 | TC-FA-GRP-904, TC-FA-GRP-905, TC-FA-GRP-906, TC-FA-GRP-907, TC-FA-GRP-908, TC-FA-GRP-909, TC-FA-GRP-910 |
| TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak | Group Hasil Import: Edit dan Delete Identik dengan Group Manual, Tanpa Auto-Assign Creator, dan Import dengan Nama All Groups Ditolak | FE+BE | 40 | TC-FA-GRP-911, TC-FA-GRP-912, TC-FA-GRP-913, TC-FA-GRP-1026 |
| TC-FA-GRP-E2E-206-format-tanggal-mengikuti-general-settings-groups-list-modal-changelog-dan-popup-detail | Format Tanggal Mengikuti General Settings: Groups List, Modal Changelog, Popup Detail Group (Tab Assets dan Tab Users) | FE+BE | 30 | TC-FA-GRP-914, TC-FA-GRP-915, TC-FA-GRP-916 |
| TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | Sinkron Lintas Modul ke Tab Assets: Policy Transaksi, Pairing/Pelepasan TAG, Pemindaian Audit, dan Nilai/Scope/Status Custom Field | FE+BE | 45 | TC-FA-GRP-1250, TC-FA-GRP-1251, TC-FA-GRP-1252, TC-FA-GRP-1253 |
| TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | Defense-in-Depth: Request Langsung ke API oleh Aktor Tanpa Capability atau di Luar Scope (Create, Add Subgroup, Edit, Delete, Baca Detail) | FE+BE | 4 | TC-FA-GRP-917, TC-FA-GRP-918, TC-FA-GRP-919, TC-FA-GRP-920, TC-FA-GRP-921, TC-FA-GRP-922, TC-FA-GRP-923, TC-FA-GRP-924, TC-FA-GRP-925 |
| TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | Defense-in-Depth: Request Langsung Wizard, Download, Node Excess, Function Ganda, Delete Guard, Isolasi Client, Nilai Bergerbang, serta Markup dan SQL sebagai Teks | FE+BE | 32 | TC-FA-GRP-926, TC-FA-GRP-927, TC-FA-GRP-928, TC-FA-GRP-929, TC-FA-GRP-930, TC-FA-GRP-931, TC-FA-GRP-932, TC-FA-GRP-933, TC-FA-GRP-963, TC-FA-GRP-934, TC-FA-GRP-935, TC-FA-GRP-1249 |
| TC-FA-GRP-E2E-210-state-tenant-suspended-expired-aksi-tulis-ditolak-403-dan-job-t0-tetap-berjalan | State Tenant: Client Suspended dan Expired Menolak Seluruh Aksi Tulis dengan 403 dan Toast Baku, serta Job Sistem T-0 pada Client Suspended Tetap Menandai Excess | FE+BE | 26 | TC-FA-GRP-995, TC-FA-GRP-996, TC-FA-GRP-1149 |
| TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide | Tab Assets Search: Interaksi, Last Updated Tidak Match, dan Kolom Asset ID Di-Hide | FE+BE | 39 | TC-FA-GRP-677, TC-FA-GRP-681, TC-FA-GRP-682 |
| TC-FA-GRP-E2E-212-tab-assets-search-per-kolom-name-asset-id-dan-status | Tab Assets Search per Kolom Name, Asset ID, dan Status | FE+BE | 13 | TC-FA-GRP-678, TC-FA-GRP-679, TC-FA-GRP-680 |
| TC-FA-GRP-E2E-213-tab-assets-search-per-kolom-brand-model-type-dan-category | Tab Assets Search per Kolom Brand, Model/Type, dan Category | FE+BE | 14 | TC-FA-GRP-1067, TC-FA-GRP-1068, TC-FA-GRP-1157 |
| TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | Tab Assets Filter: Screening Panel dan Filter Status (Isi Opsi, Satu/Dua Opsi OR) | FE+BE | 39 | TC-FA-GRP-683, TC-FA-GRP-684, TC-FA-GRP-685, TC-FA-GRP-686 |
| TC-FA-GRP-E2E-215-tab-assets-filter-status-chip-opsi-dan-search-dropdown | Tab Assets Filter Status: Search Dropdown dan Chip Opsi (Hapus via X dan Uncheck) | FE+BE | 29 | TC-FA-GRP-687, TC-FA-GRP-688, TC-FA-GRP-689 |
| TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Tab Assets Filter Asset Name: Isi Opsi, Satu Opsi (Semua Unit), Dua Opsi OR, dan Search Dropdown | FE+BE | 30 | TC-FA-GRP-1004, TC-FA-GRP-1005, TC-FA-GRP-1006, TC-FA-GRP-1007 |
| TC-FA-GRP-E2E-217-tab-assets-filter-asset-name-chip-opsi-dan-kombinasi-asset-name-status | Tab Assets Filter Asset Name: Chip Opsi dan Kombinasi Asset Name + Status (AND) | FE+BE | 27 | TC-FA-GRP-1008, TC-FA-GRP-1009, TC-FA-GRP-1010 |
| TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter | Tab Assets Filter Last Updated, Kombinasi Status + Last Updated (AND), [Clear Field], dan Search lalu Filter | FE+BE | 24 | TC-FA-GRP-690, TC-FA-GRP-691, TC-FA-GRP-692, TC-FA-GRP-693 |
| TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated | Tab Assets Sort Kolom Name, Asset ID, Status, dan Last Updated (Asc, Desc, Netral) | FE+BE | 30 | TC-FA-GRP-695, TC-FA-GRP-696, TC-FA-GRP-697, TC-FA-GRP-698 |
| TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear | Tab Assets Kombinasi: Filter lalu Search, Search + Filter + Sort, serta Clear Filter/Search Saat Lainnya Aktif | FE+BE | 25 | TC-FA-GRP-694, TC-FA-GRP-699, TC-FA-GRP-700, TC-FA-GRP-701 |
| TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | Tab Assets: Ganti Target Sort, Pemulihan dari Empty State, Filter Tetap Berlaku Saat Kolom Status Di-Hide, dan Genuine Empty State Node Tanpa Aset | FE+BE | 37 | TC-FA-GRP-702, TC-FA-GRP-703, TC-FA-GRP-1121, TC-FA-GRP-1129 |
| TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | Tab Assets Setup Column: Screening Overlay dan Popup, Guard Kolom Terakhir, dan Pin ke-4 Diblok | FE+BE | 42 | TC-FA-GRP-704, TC-FA-GRP-705, TC-FA-GRP-718, TC-FA-GRP-1090 |
| TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | Tab Assets Setup Column: [Reset to Default], (X) dan Esc, Cache Tidak Memengaruhi Tabel Lain, dan Kolom Actions Hanya Pemicu Column Visibility | FE+BE | 46 | TC-FA-GRP-719, TC-FA-GRP-720, TC-FA-GRP-721, TC-FA-GRP-955 |
| TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated | Tab Assets Setup Column: Uncheck Kolom Name, Asset ID, Status, dan Last Updated | FE+BE | 13 | TC-FA-GRP-706, TC-FA-GRP-707, TC-FA-GRP-708, TC-FA-GRP-709 |
| TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated | Tab Assets Setup Column: Geser (Drag) Kolom Name, Asset ID, Status, dan Last Updated | FE+BE | 13 | TC-FA-GRP-710, TC-FA-GRP-711, TC-FA-GRP-712, TC-FA-GRP-713 |
| TC-FA-GRP-E2E-226-tab-assets-setup-column-pin-kolom-name-asset-id-dan-status | Tab Assets Setup Column: Pin Kolom Name, Asset ID, dan Status | FE+BE | 19 | TC-FA-GRP-714, TC-FA-GRP-715, TC-FA-GRP-716 |
| TC-FA-GRP-E2E-227-tab-assets-setup-column-pin-last-updated-dan-uncheck-kolom-brand-model-type | Tab Assets Setup Column: Pin Kolom Last Updated serta Uncheck Kolom Brand dan Model/Type | FE+BE | 30 | TC-FA-GRP-717, TC-FA-GRP-1078, TC-FA-GRP-1079 |
| TC-FA-GRP-E2E-228-tab-assets-setup-column-geser-drag-brand-model-type-dan-pin-brand | Tab Assets Setup Column: Geser (Drag) Kolom Brand dan Model/Type serta Pin Kolom Brand | FE+BE | 30 | TC-FA-GRP-1080, TC-FA-GRP-1081, TC-FA-GRP-1082 |
| TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge | Tab Assets Setup Column: Pin Kolom Model/Type, Geser dan Pin Kolom Category, dan Tampilan Badge Primary Category dengan Truncation | FE+BE | 44 | TC-FA-GRP-1083, TC-FA-GRP-1168, TC-FA-GRP-1169 |
| TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | Tab Assets Download (Nama Berkas, Header, Jumlah Baris): Seluruh Data, Search + Filter Aktif, dan Kolom Hide/Unhide | FE+BE | 36 | TC-FA-GRP-722, TC-FA-GRP-723, TC-FA-GRP-724, TC-FA-GRP-725 |
| TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | Tab Assets Download Isi Berkas: Transformasi Tipe Badge, Date, Empty, Brand/Model/Type Nama Penuh, dan Category Hierarki Penuh dari Root | FE+BE | 19 | TC-FA-GRP-727, TC-FA-GRP-728, TC-FA-GRP-729, TC-FA-GRP-1086, TC-FA-GRP-1186 |
| TC-FA-GRP-E2E-232-tab-assets-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | Tab Assets Pagination: Default dan Page Size, Navigasi, serta Reset ke Halaman 1 Saat Search/Filter | FE+BE | 35 | TC-FA-GRP-1047, TC-FA-GRP-1048 |
| TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Tab Assets Filter Brand: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown | FE+BE | 27 | TC-FA-GRP-1069, TC-FA-GRP-1070, TC-FA-GRP-1071, TC-FA-GRP-1072 |
| TC-FA-GRP-E2E-234-tab-assets-filter-brand-chip-opsi-dan-kombinasi-brand-status | Tab Assets Filter Brand: Chip Opsi dan Kombinasi Brand + Status (AND) | FE+BE | 31 | TC-FA-GRP-1073, TC-FA-GRP-1074, TC-FA-GRP-1075 |
| TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | Tab Assets Filter Model/Type: Isi Opsi, Satu/Dua Opsi OR, dan Search Dropdown | FE+BE | 28 | TC-FA-GRP-1150, TC-FA-GRP-1151, TC-FA-GRP-1152, TC-FA-GRP-1153 |
| TC-FA-GRP-E2E-236-tab-assets-filter-model-type-chip-opsi-dan-kombinasi-model-type-status | Tab Assets Filter Model/Type: Chip Opsi dan Kombinasi Model/Type + Status (AND) | FE+BE | 31 | TC-FA-GRP-1154, TC-FA-GRP-1155, TC-FA-GRP-1156 |
| TC-FA-GRP-E2E-237-tab-assets-sort-brand-model-type-dan-tampilan-badge-dark-truncation-hover | Tab Assets Sort Kolom Brand dan Model/Type serta Tampilan Badge Dark dengan Truncation dan Hover Nama Penuh | FE+BE | 25 | TC-FA-GRP-1076, TC-FA-GRP-1077, TC-FA-GRP-1084 |
| TC-FA-GRP-E2E-238-tab-assets-status-multi-badge-sort-filter-dan-search-label-badge-pertama | Tab Assets Status Multi-Badge: Sort Menurut Label Badge Pertama, Filter OR, dan Search Label Badge Mana Pun | FE+BE | 29 | TC-FA-GRP-1140, TC-FA-GRP-1141, TC-FA-GRP-1142 |
| TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | Tab Assets Filter Category: Screening Modal Tree Picker, Satu Node Leaf, Dua Node Leaf (OR), dan Search Tree | FE+BE | 42 | TC-FA-GRP-1158, TC-FA-GRP-1159, TC-FA-GRP-1160, TC-FA-GRP-1161 |
| TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status | Tab Assets Filter Category: Chip Dihapus via X, Uncheck Node di Tree, dan Kombinasi Category + Status | FE+BE | 40 | TC-FA-GRP-1162, TC-FA-GRP-1163, TC-FA-GRP-1164 |
| TC-FA-GRP-E2E-241-tab-assets-filter-category-centang-parent-turunan-dan-cancel-tree-picker | Tab Assets Filter Category: Centang Parent Mencentang Turunan dan [Cancel] Membuang Pilihan Pending | FE+BE | 36 | TC-FA-GRP-1187, TC-FA-GRP-1188 |
| TC-FA-GRP-E2E-242-tab-assets-category-sort-dan-setup-column-centang-serta-geser | Tab Assets Kolom Category: Sort dan Setup Column (Centang Kolom Curated, Geser) | FE+BE | 28 | TC-FA-GRP-1165, TC-FA-GRP-1166, TC-FA-GRP-1167 |
| TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi | Tab Assets Label: Search Kolom Label (+N more), Isi Opsi Filter, Satu Opsi (Berlabel Ganda), dan Dua Opsi OR | FE+BE | 35 | TC-FA-GRP-1170, TC-FA-GRP-1171, TC-FA-GRP-1172, TC-FA-GRP-1173 |
| TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | Tab Assets Filter Label: Search Dropdown, Chip Opsi (X dan Uncheck), dan Kombinasi Label + Status | FE+BE | 43 | TC-FA-GRP-1174, TC-FA-GRP-1175, TC-FA-GRP-1176, TC-FA-GRP-1177 |
| TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | Tab Assets Label: Sort Kolom +N more dan Setup Column (Centang, Geser, Pin) | FE+BE | 54 | TC-FA-GRP-1178, TC-FA-GRP-1179, TC-FA-GRP-1180, TC-FA-GRP-1181 |
| TC-FA-GRP-E2E-246-tab-assets-label-tampilan-chip-popover-labels-dan-kolom-curated-tersembunyi-default | Tab Assets Label: Tampilan Chip 1-2 Badge + +N more, Popover Labels, dan Kolom Curated Tersembunyi Secara Default | FE+BE | 26 | TC-FA-GRP-1182, TC-FA-GRP-1183, TC-FA-GRP-1185 |
| TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement | Tab Assets Download Isi Berkas: Multi-Badge Status, Label A-Z, TAG, dan Measurement Symbol UoM | FE+BE | 35 | TC-FA-GRP-1143, TC-FA-GRP-1184, TC-FA-GRP-1195, TC-FA-GRP-1202 |
| TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku | Tab Assets Download Isi Berkas: Kolom Group Tidak Berlaku, Transactional Policy, dan Last Scanned (Format General Settings) | FE+BE | 38 | TC-FA-GRP-1190, TC-FA-GRP-1207, TC-FA-GRP-1212 |
| TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | Tab Assets Download Isi Berkas Kolom Bergerbang: Asset Value (Commercial), Warranty Expiry, Custom Field, dan Sel No Access per Aktor | FE+BE | 57 | TC-FA-GRP-1220, TC-FA-GRP-1227, TC-FA-GRP-1237, TC-FA-GRP-1247 |
| TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | Tab Assets Kolom TAG: Satu Ikon per Tipe Tag Aktif, Isi Opsi Filter, Filter OR (Pairing Tidak Aktif Tidak Dihitung), dan Sort Alfabetis Label Ikon | FE+BE | 47 | TC-FA-GRP-1191, TC-FA-GRP-1192, TC-FA-GRP-1193, TC-FA-GRP-1194 |
| TC-FA-GRP-E2E-251-tab-assets-kolom-tag-setup-column-dan-search-label-aksesibilitas-ikon | Tab Assets Kolom TAG: Setup Column (Uncheck, Geser, Pin) dan Search Label Aksesibilitas Ikon | FE+BE | 46 | TC-FA-GRP-1196, TC-FA-GRP-1254 |
| TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | Tab Assets Kolom Measurement: Tersembunyi Default Menampilkan Symbol UoM, Search, Isi Opsi Filter, dan Filter Satu/Dua Opsi | FE+BE | 49 | TC-FA-GRP-1197, TC-FA-GRP-1198, TC-FA-GRP-1199, TC-FA-GRP-1200 |
| TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy | Tab Assets Kolom Measurement: Sort dan Setup Column, serta Search Kolom Transactional Policy | FE+BE | 55 | TC-FA-GRP-1201, TC-FA-GRP-1203, TC-FA-GRP-1255 |
| TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | Tab Assets Kolom Transactional Policy: Ikon Transaksi On, Filter OR Nama Transaksi, Sort Alfabetis Label Ikon, dan Setup Column | FE+BE | 67 | TC-FA-GRP-1204, TC-FA-GRP-1205, TC-FA-GRP-1206, TC-FA-GRP-1208 |
| TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | Tab Assets Kolom Last Scanned: Tanggal Pemindaian Terbaru Mengikuti General Settings, Filter Rentang, Sort Oldest/Newest, dan Setup Column | FE+BE | 46 | TC-FA-GRP-1209, TC-FA-GRP-1210, TC-FA-GRP-1211, TC-FA-GRP-1213 |
| TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting | Tab Assets Asset Value (Commercial): Hak Pemegang View Asset Value, Pemegang Manage Accounting (Client-Wide), dan No Access di Group Lain | FE+BE | 45 | TC-FA-GRP-1214, TC-FA-GRP-1215, TC-FA-GRP-1216 |
| TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang | Tab Assets Asset Value (Commercial): Manage Purchase/Tanpa Hak No Access, Sort Numerik, dan Filter Rentang Min-Max | FE+BE | 46 | TC-FA-GRP-1217, TC-FA-GRP-1218, TC-FA-GRP-1219 |
| TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku | Tab Assets Asset Value: Setup Column (Centang, Geser, Pin), Search Nilai Tampil, dan Kedua Kolom Buku Hidden Secara Default | FE+BE | 45 | TC-FA-GRP-1221, TC-FA-GRP-1265, TC-FA-GRP-1285 |
| TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | Tab Assets Asset Value Commercial dan Fiscal: Dua Kolom Tetap dengan Tooltip, Not Depreciated Menampilkan Harga Perolehan, Gerbang AST-LOGIC-10 di Kedua Kolom, dan Sort/Filter/Search per Buku | FE+BE | 48 | TC-FA-GRP-1284, TC-FA-GRP-1286, TC-FA-GRP-1287, TC-FA-GRP-1288 |
| TC-FA-GRP-E2E-260-tab-assets-hak-sel-bergerbang-tier-total-control-dan-default-user | Tab Assets Hak Sel Bergerbang: Tier Total Control dan Default User Berhak Atas Semua Kolom Bergerbang Client-Wide | FE+BE | 45 | TC-FA-GRP-1256, TC-FA-GRP-1257 |
| TC-FA-GRP-E2E-261-tab-assets-hak-sel-bergerbang-tier-read-only-dan-group-manager | Tab Assets Hak Sel Bergerbang: Tier Read Only dan Group Manager (Group yang Di-assign + Descendant, Bukan Accounting) | FE+BE | 40 | TC-FA-GRP-1258, TC-FA-GRP-1259 |
| TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses | Tab Assets Warranty Expiry: Hak Pemegang Manage Purchase pada Group, No Access di Group Lain, dan View Asset Value/Manage Accounting Tidak Memberi Akses Warranty | FE+BE | 36 | TC-FA-GRP-1222, TC-FA-GRP-1223, TC-FA-GRP-1224 |
| TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | Tab Assets Warranty Expiry: Sort Oldest/Newest, Filter Rentang, Setup Column, dan Hak pada Group Induk Berlaku untuk Descendant | FE+BE | 46 | TC-FA-GRP-1225, TC-FA-GRP-1226, TC-FA-GRP-1228, TC-FA-GRP-1229 |
| TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30 | Tab Assets Warranty Expiry Penanda Warna: Tanggal Lewat Danger dengan Tooltip, Hari Ini Warning, dan Hari ke-30 Warning Inklusif, Hari ke-31 Normal | FE+BE | 17 | TC-FA-GRP-1277, TC-FA-GRP-1278, TC-FA-GRP-1279, TC-FA-GRP-1280 |
| TC-FA-GRP-E2E-265-tab-assets-warranty-expiry-penanda-warna-dash-no-access-time-zone-client-dan-tidak-memengaruhi-sort-filter-download | Tab Assets Warranty Expiry Penanda Warna: Sel Dash dan No Access Tanpa Warna, Hari Ini Mengikuti Time Zone General Settings, dan Tidak Memengaruhi Sort/Filter | FE+BE | 32 | TC-FA-GRP-1281, TC-FA-GRP-1282, TC-FA-GRP-1283 |
| TC-FA-GRP-E2E-266-tab-assets-custom-field-nilai-per-data-type-value-type-global-dan-hak-purchasing | Tab Assets Custom Field: Nilai Sesuai Data Type, Dash untuk Belum Diisi/Di Luar Scope, Value Type Global, dan No Access Purchasing di Group Lain | FE+BE | 29 | TC-FA-GRP-1230, TC-FA-GRP-1231, TC-FA-GRP-1232 |
| TC-FA-GRP-E2E-267-tab-assets-custom-field-accounting-client-wide-dan-dash-mengalahkan-no-access | Tab Assets Custom Field Accounting: Pemegang Manage Accounting Melihat Nilai Client-Wide dan Dash Mengalahkan No Access | FE+BE | 18 | TC-FA-GRP-1233, TC-FA-GRP-1260 |
| TC-FA-GRP-E2E-268-tab-assets-custom-field-accounting-pada-lisensi-fa-7-grace-period-dan-tidak-aktif | Tab Assets Custom Field Accounting pada Lisensi FA-7: Grace Period Tersedia Read-Only dan Tidak Aktif Tidak Tersedia (Server Tidak Mengembalikan Nilai) | FE+BE | 14 | TC-FA-GRP-1261, TC-FA-GRP-1262 |
| TC-FA-GRP-E2E-269-tab-assets-custom-field-search-sort-teks-tanggal-dan-kolom-di-hide | Tab Assets Custom Field: Search Substring dengan Kolom Di-Hide Tidak Dicari serta Sort Teks (PO Number) dan Tanggal (Purchase Date) | FE+BE | 32 | TC-FA-GRP-1234, TC-FA-GRP-1235, TC-FA-GRP-1236 |
| TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match | Tab Assets Custom Field Search: Dropdown/Multi-Dropdown, Numeric/Percentage, Email, serta Date dan DateTime Tidak Match | FE+BE | 31 | TC-FA-GRP-1266, TC-FA-GRP-1267, TC-FA-GRP-1268, TC-FA-GRP-1269 |
| TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range | Tab Assets Custom Field Filter: Dropdown, Multi-Dropdown (OR), Date dan DateTime Range Picker, serta Numeric/Currency/Percentage Min-Max | FE+BE | 30 | TC-FA-GRP-1270, TC-FA-GRP-1271, TC-FA-GRP-1273, TC-FA-GRP-1272 |
| TC-FA-GRP-E2E-272-tab-assets-custom-field-filter-tipe-tanpa-filter-formula-dan-filter-pada-kolom-bergerbang | Tab Assets Custom Field: Tipe Tanpa Field Filter, Formula Tanpa Search/Sort/Filter, dan Filter pada Kolom Bergerbang Tidak Mencocokkan No Access | FE+BE | 19 | TC-FA-GRP-1274, TC-FA-GRP-1275, TC-FA-GRP-1276 |
| TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor | Tab Assets Ketersediaan Kolom di Setup Column per Hak Aktor: View Asset Value, Manage Purchase, Manage Accounting, dan Tanpa Hak Bergerbang | FE+BE | 27 | TC-FA-GRP-1240, TC-FA-GRP-1241, TC-FA-GRP-1242, TC-FA-GRP-1243 |
| TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive | Tab Assets Setup Column: Komposisi Tanpa Group, Kolom Curated Custom Field (Centang, Geser, Pin, Reset), dan Custom Field Inactive/Baru | FE+BE | 44 | TC-FA-GRP-1189, TC-FA-GRP-1238, TC-FA-GRP-1239 |
| TC-FA-GRP-E2E-275-tab-assets-gerbang-no-access-sort-filter-dan-search-aktor-tanpa-hak-bergerbang | Tab Assets Gerbang No Access: Baris No Access Tetap Paling Akhir pada Sort, Tidak Cocok dengan Filter, dan Teks No Access Tidak Dicocokkan Search | FE+BE | 29 | TC-FA-GRP-1244, TC-FA-GRP-1245, TC-FA-GRP-1246 |
| TC-FA-GRP-E2E-276-tab-assets-gerbang-search-non-searchable-asset-id-tidak-filterable-dan-filter-asset-id | Tab Assets: Kolom Non-Searchable Warranty Expiry dan Last Scanned Tidak Match, Asset ID Tidak Filterable, dan Filter Asset ID Satu/Dua Opsi | FE+BE | 28 | TC-FA-GRP-1248, TC-FA-GRP-1263, TC-FA-GRP-1264 |
| TC-FA-GRP-E2E-277-guided-tooltip-groups-sidebar-collapsed-dibuka-otomatis-dan-step-kolom-total-asset-dilewati | Guided Tooltip Groups: Sidebar Collapsed Dibuka Otomatis dan Step Kolom Total Asset Dilewati saat Kolom Disembunyikan | FE+BE | 26 | TC-FA-GRP-41, TC-FA-GRP-970 |
| TC-FA-GRP-E2E-278-role-matrix-visibilitas-elemen-groups-list-read-only-dan-tanpa-aksi-tulis | Role Matrix: Visibilitas Elemen Groups List Role Read Only dan Read Only Tanpa Aksi Tulis | FE+BE | 24 | TC-FA-GRP-46, TC-FA-GRP-78 |
| TC-FA-GRP-E2E-279-konflik-dua-admin-edit-bersamaan-last-write-wins-dan-code-auto-generate-bentrok | Konflik Dua Admin: Edit Node yang Sama (Last-Write-Wins) dan Code Auto-Generate Bentrok dengan Retry Otomatis | FE+BE | 22 | TC-FA-GRP-190, TC-FA-GRP-334, TC-FA-GRP-335 |
| TC-FA-GRP-E2E-281-wizard-log-ditulis-saat-diterapkan-di-t0-system-log-user-submit-terakhir-dan-siklus-downgrade-berikutnya | Wizard: Submit Sebelum T-0 Tidak Menulis Log, Log dan System Log Ditulis Saat Diterapkan di T-0 (Submit Terakhir), dan Siklus Downgrade Berikutnya | FE+BE | 40 | TC-FA-GRP-989, TC-FA-GRP-990 |
| TC-FA-GRP-E2E-282-wizard-pagination-default-page-size-navigasi-dan-centang-lintas-halaman | Wizard: Pagination Step Group Consolidation (Default dan Pilihan Page Size, Navigasi, Reset ke Halaman 1, Centang dan Counter Lintas Halaman) | FE+BE | 36 | TC-FA-GRP-1065, TC-FA-GRP-1066 |
| TC-FA-GRP-E2E-283-modal-changelog-filter-tetap-berlaku-saat-kolom-action-di-hide | Modal Changelog Filter: Tetap Tersedia dan Tetap Berlaku Saat Kolom Action Di-Hide | FE+BE | 23 | TC-FA-GRP-1119 |
| TC-FA-GRP-E2E-284-groups-list-kombinasi-search-filter-sort-pagination-dan-clear-filter-saat-search-sort-aktif | Groups List Kombinasi: Search + Filter + Sort + Pagination dan Clear Filter Saat Search/Sort Aktif | FE+BE | 23 | TC-FA-GRP-375, TC-FA-GRP-376 |
| TC-FA-GRP-E2E-285-create-group-level-1-dan-subgroup-baris-pola-group-role-dan-transaction-role-tc-ro-serta-log-assign-home-group-constraint | Create Group Level 1 dan Subgroup: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk, Mengabaikan Home Group Constraint, dan Log Assign per Baris | FE+BE | 35 | TC-FA-GRP-1289, TC-FA-GRP-1291 |
| TC-FA-GRP-E2E-286-delete-group-baris-pola-group-role-dan-transaction-role-tc-ro-terhapus-log-remove-per-baris | Delete Group: Baris Pola Group Role dan Transaction Role Total Control/Read Only pada Node dan Descendant Terhapus dalam Satu Transaksi dengan Log Remove (Group Deleted) per Baris | FE+BE | 17 | TC-FA-GRP-1290 |
| TC-FA-GRP-E2E-287-group-hasil-import-baris-pola-group-role-dan-transaction-role-tc-ro-user-non-tc-ro-tidak-diturunkan | Group Hasil Import: Baris Pola Group Role dan Transaction Role Total Control/Read Only Terbentuk dengan Log Assign per Baris, User Non-TC/RO Tidak Diturunkan | FE+BE | 21 | TC-FA-GRP-1292 |
| TC-FA-GRP-E2E-288-absence-pola-group-role-tc-ro-tanpa-auto-revert-dan-tanpa-notifikasi-in-app-saat-create | Absence Pola Group Role TC/RO: Tanpa Entri Auto-Revert saat Create Group Level 1 dan Subgroup, serta Tanpa Notifikasi In-App ke User Total Control/Read Only | FE+BE | 31 | TC-FA-GRP-1289, TC-FA-GRP-1291 |
| TC-FA-GRP-E2E-289-absence-import-group-pola-tanpa-notifikasi-in-app-dan-kegagalan-tulis-baris-pola-me-rollback-group | Absence Import Group: Tanpa Notifikasi In-App ke User Total Control/Read Only, dan Kegagalan Penulisan Baris Pola Me-Rollback Group (Group Tidak Terbentuk) | FE+BE | 19 | TC-FA-GRP-1292 |
| TC-FA-GRP-E2E-290-create-subgroup-di-bawah-node-penugasan-gm-baris-pola-gm-log-assign-dan-gm-bersarang-satu-set | Create Subgroup di Bawah Node Penugasan Group Manager: Baris Pola GM Terbentuk, Log Assign Biasa, dan GM Bersarang Memegang Satu Set Baris | FE+BE | 29 | TC-FA-GRP-1293, TC-FA-GRP-1295 |
| TC-FA-GRP-E2E-291-create-subgroup-oleh-gm-sendiri-di-descendant-node-penugasan-baris-pola-gm-tetap-terbentuk-gm-lain-tidak-menerima | Create Subgroup oleh GM Sendiri di Descendant Node Penugasan: Baris Pola GM Tetap Terbentuk, GM Lain yang Tidak Mencakup Parent Tidak Menerima | FE+BE | 17 | TC-FA-GRP-1294 |
| TC-FA-GRP-E2E-292-absence-create-subgroup-dan-group-di-bawah-node-gm-tanpa-notifikasi-auto-revert-dan-entri-log-user-gm | Absence Create Subgroup dan Group di Bawah Node GM: Tanpa Notifikasi In-App, Tanpa Entri Auto-Revert, Changelog Group Hanya Create, dan Tanpa Entri Log untuk User GM | FE+BE | 35 | TC-FA-GRP-1293, TC-FA-GRP-1294, TC-FA-GRP-1296 |
| TC-FA-GRP-E2E-293-delete-node-penugasan-gm-penugasan-terlepas-baris-pola-terhapus-dan-log-remove-group-deleted-per-baris | Delete Node Penugasan GM: Penugasan GM Terlepas, Baris Pola GM pada Node dan Descendant Terhapus, dan Log Remove (Group Deleted) per Baris | FE+BE | 25 | TC-FA-GRP-1297 |
| TC-FA-GRP-E2E-294-absence-delete-node-gm-tanpa-notifikasi-in-app-tanpa-auto-revert-dan-changelog-group-hanya-delete | Absence Delete Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Action Remove (via Group Manager), Tanpa Auto-Revert, dan Changelog Group Hanya Baris Delete | FE+BE | 27 | TC-FA-GRP-1297, TC-FA-GRP-1298 |
| TC-FA-GRP-E2E-295-total-user-node-descendant-memuat-user-gm-yang-penugasannya-mencakup-node-dihitung-distinct | Total User Node Descendant Memuat User GM yang Penugasannya Mencakup Node, Dihitung Distinct, dan Tidak Memuat Node Ancestor atau Node Lain | FE+BE | 15 | TC-FA-GRP-1299 |
| TC-FA-GRP-E2E-296-group-hasil-import-di-bawah-node-tercakup-gm-baris-pola-gm-atomik-dan-group-level-1-tanpa-baris-pola | Group Hasil Import di Bawah Node Tercakup GM: Baris Pola GM Ditulis Atomik, Group Level 1 Hasil Import Tanpa Baris Pola GM | FE+BE | 20 | TC-FA-GRP-1300 |
| TC-FA-GRP-E2E-297-absence-import-group-di-bawah-node-gm-tanpa-notifikasi-tanpa-auto-revert-dan-kegagalan-tulis-baris-pola-me-rollback-group | Absence Import Group di Bawah Node GM: Tanpa Notifikasi In-App ke User GM, Tanpa Auto-Revert, dan Kegagalan Penulisan Baris Pola GM Me-Rollback Group (Group Tidak Terbentuk) | FE+BE | 20 | TC-FA-GRP-1300 |
| TC-FA-GRP-E2E-298-create-group-level-1-tanpa-baris-pola-gm-dan-total-user-hanya-tc-du-ro | Create Group Level 1: Tanpa Baris Pola GM untuk User Group Manager, Total User Hanya Total Control, Default User, dan Read Only | FE+BE | 18 | TC-FA-GRP-1296 |
| TC-FA-GRP-E2E-300-delete-descendant-node-tercakup-gm-baris-pola-di-node-terhapus-saja-ancestor-gm-tidak-terpengaruh | Delete Descendant Node Tercakup GM: Hanya Baris Pola GM di Node Terhapus dan Descendant-nya yang Dihapus, Penugasan GM di Ancestor dan Baris di Node Lain Tetap | FE+BE | 27 | TC-FA-GRP-1298 |
| TC-FA-GRP-E2E-301-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-baris-tetap-di-root-total-user-tidak-menghitung | Create Subgroup di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan untuk trxAnc, Baris Tetap di Trx Anc Root, Total User Tidak Menghitung | FE+BE | 22 | TC-FA-GRP-1301 |
| TC-FA-GRP-E2E-302-absence-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app | Absence Create Subgroup di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App | FE+BE | 13 | TC-FA-GRP-1301 |
| TC-FA-GRP-E2E-303-group-hasil-import-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-cakupan-ancestor-tetap | Group Hasil Import di Bawah Node yang Ancestor-nya Punya Penugasan Transaction Role: Tanpa Baris Salinan, Cakupan Ancestor Tetap Berlaku | FE+BE | 16 | TC-FA-GRP-1302 |
| TC-FA-GRP-E2E-304-absence-import-group-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app | Absence Import Group di Bawah Node Ber-Transaction Role Ancestor: Tanpa Entri Assign untuk trxAnc dan Tanpa Notifikasi In-App | FE+BE | 9 | TC-FA-GRP-1302 |
| TC-FA-GRP-E2E-305-delete-node-di-bawah-ancestor-ber-transaction-role-dialog-normal-penugasan-ancestor-tetap-subtree-terhapus | Delete Node di Bawah Ancestor Ber-Transaction Role: Dialog Normal (Bukan D-15), Penugasan Ancestor Tetap, Seluruh Subtree Terhapus | FE+BE | 21 | TC-FA-GRP-1303 |
| TC-FA-GRP-E2E-306-absence-delete-node-di-bawah-ancestor-ber-transaction-role-tanpa-entri-remove-dan-tanpa-notifikasi-in-app | Absence Delete Node di Bawah Ancestor Ber-Transaction Role: Tanpa Entri Remove untuk trxAnc dan Tanpa Notifikasi In-App | FE+BE | 14 | TC-FA-GRP-1303 |
| TC-FA-GRP-E2E-307-delete-leaf-yang-hanya-tercakup-baris-pola-gm-ancestor-dialog-normal-bukan-d-15 | Delete Leaf yang Hanya Tercakup Baris Pola GM Ancestor: Dialog Normal (Bukan D-15), Leaf Terhapus, Penugasan GM di Ancestor Tetap | FE+BE | 15 | TC-FA-GRP-1304 |
| TC-FA-GRP-E2E-308-tab-assets-sel-asset-value-pending-tooltip-alasan-dan-prioritas | Tab Assets Sel Asset Value Pending: Tooltip Alasan Purchase Cost Belum Diisi atau Asset Class Belum Diisi dan Prioritas Alasan | FE+BE | 15 | TC-FA-GRP-1305 |
| TC-FA-GRP-E2E-309-tab-assets-sel-asset-value-pending-search-filter-dan-download-dua-kolom | Tab Assets Sel Asset Value Pending pada Kedua Kolom Buku: Filter, Search Teks Pending Tidak Cocok, dan Download Menulis Kosong | FE+BE | 19 | TC-FA-GRP-1306 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. `tc-settings-groups-backend.md` tidak ada dan seluruh 1070 TC granular terpetakan ke minimal satu spec E2E.


---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-GRP-1 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-2 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-3 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-4 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-5 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-6 | E2E | TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | FE+BE |
| TC-FA-GRP-7 | E2E | TC-FA-GRP-E2E-003-loading-state-dan-error-load-groups-list-try-again | FE+BE |
| TC-FA-GRP-8 | E2E | TC-FA-GRP-E2E-003-loading-state-dan-error-load-groups-list-try-again | FE+BE |
| TC-FA-GRP-9 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-10 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-11 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-12 | E2E | TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | FE+BE |
| TC-FA-GRP-13 | E2E | TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | FE+BE |
| TC-FA-GRP-14 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-15 | E2E | TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | FE+BE |
| TC-FA-GRP-16 | E2E | TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | FE+BE |
| TC-FA-GRP-17 | E2E | TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | FE+BE |
| TC-FA-GRP-18 | E2E | TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | FE+BE |
| TC-FA-GRP-19 | E2E | TC-FA-GRP-E2E-007-search-sidebar-nama-code-tanpa-hasil-clear-dan-refresh | FE+BE |
| TC-FA-GRP-20 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-21 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-22 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-23 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-24 | E2E | TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | FE+BE |
| TC-FA-GRP-25 | E2E | TC-FA-GRP-E2E-010-group-context-header-all-groups-agregat-distinct-union-scope-aktor-scoped-dan-angka-tidak-dapat-diklik | FE+BE |
| TC-FA-GRP-26 | E2E | TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | FE+BE |
| TC-FA-GRP-27 | E2E | TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | FE+BE |
| TC-FA-GRP-28 | E2E | TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | FE+BE |
| TC-FA-GRP-29 | E2E | TC-FA-GRP-E2E-010-group-context-header-all-groups-agregat-distinct-union-scope-aktor-scoped-dan-angka-tidak-dapat-diklik | FE+BE |
| TC-FA-GRP-30 | E2E | TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | FE+BE |
| TC-FA-GRP-31 | E2E | TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | FE+BE |
| TC-FA-GRP-32 | E2E | TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | FE+BE |
| TC-FA-GRP-33 | E2E | TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | FE+BE |
| TC-FA-GRP-34 | E2E | TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | FE+BE |
| TC-FA-GRP-35 | E2E | TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | FE+BE |
| TC-FA-GRP-36 | E2E | TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | FE+BE |
| TC-FA-GRP-37 | E2E | TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | FE+BE |
| TC-FA-GRP-38 | E2E | TC-FA-GRP-E2E-013-guided-tooltip-groups-navigasi-keluar-resize-viewport-dan-keyboard | FE+BE |
| TC-FA-GRP-39 | E2E | TC-FA-GRP-E2E-013-guided-tooltip-groups-navigasi-keluar-resize-viewport-dan-keyboard | FE+BE |
| TC-FA-GRP-40 | E2E | TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope | FE+BE |
| TC-FA-GRP-41 | E2E | TC-FA-GRP-E2E-277-guided-tooltip-groups-sidebar-collapsed-dibuka-otomatis-dan-step-kolom-total-asset-dilewati | FE+BE |
| TC-FA-GRP-42 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-43 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-44 | E2E | TC-FA-GRP-E2E-015-role-matrix-visibilitas-elemen-groups-list-total-control-dan-default-user | FE+BE |
| TC-FA-GRP-45 | E2E | TC-FA-GRP-E2E-015-role-matrix-visibilitas-elemen-groups-list-total-control-dan-default-user | FE+BE |
| TC-FA-GRP-46 | E2E | TC-FA-GRP-E2E-278-role-matrix-visibilitas-elemen-groups-list-read-only-dan-tanpa-aksi-tulis | FE+BE |
| TC-FA-GRP-47 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-48 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-49 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-50 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-51 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-52 | E2E | TC-FA-GRP-E2E-016-role-matrix-visibilitas-elemen-groups-list-aktor-scoped-region-west | FE+BE |
| TC-FA-GRP-53 | E2E | TC-FA-GRP-E2E-017-role-matrix-negatif-menu-groups-hidden-dan-akses-url-langsung | FE+BE |
| TC-FA-GRP-54 | E2E | TC-FA-GRP-E2E-017-role-matrix-negatif-menu-groups-hidden-dan-akses-url-langsung | FE+BE |
| TC-FA-GRP-55 | E2E | TC-FA-GRP-E2E-017-role-matrix-negatif-menu-groups-hidden-dan-akses-url-langsung | FE+BE |
| TC-FA-GRP-56 | E2E | TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match | FE+BE |
| TC-FA-GRP-57 | E2E | TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match | FE+BE |
| TC-FA-GRP-58 | E2E | TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope | FE+BE |
| TC-FA-GRP-59 | E2E | TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope | FE+BE |
| TC-FA-GRP-60 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-61 | E2E | TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match | FE+BE |
| TC-FA-GRP-62 | E2E | TC-FA-GRP-E2E-023-role-matrix-gating-checkbox-bulk-aktor-d-parsial-dan-tanpa-d | FE+BE |
| TC-FA-GRP-63 | E2E | TC-FA-GRP-E2E-023-role-matrix-gating-checkbox-bulk-aktor-d-parsial-dan-tanpa-d | FE+BE |
| TC-FA-GRP-64 | E2E | TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | FE+BE |
| TC-FA-GRP-65 | E2E | TC-FA-GRP-E2E-021-role-matrix-positif-edit-manage-group-ru-dan-group-manager | FE+BE |
| TC-FA-GRP-66 | E2E | TC-FA-GRP-E2E-022-role-matrix-positif-delete-manage-group-rd-dan-group-manager | FE+BE |
| TC-FA-GRP-67 | E2E | TC-FA-GRP-E2E-022-role-matrix-positif-delete-manage-group-rd-dan-group-manager | FE+BE |
| TC-FA-GRP-68 | E2E | TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | FE+BE |
| TC-FA-GRP-69 | E2E | TC-FA-GRP-E2E-021-role-matrix-positif-edit-manage-group-ru-dan-group-manager | FE+BE |
| TC-FA-GRP-70 | E2E | TC-FA-GRP-E2E-022-role-matrix-positif-delete-manage-group-rd-dan-group-manager | FE+BE |
| TC-FA-GRP-71 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-72 | E2E | TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | FE+BE |
| TC-FA-GRP-73 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-74 | E2E | TC-FA-GRP-E2E-018-group-manager-scope-region-west-sidebar-ancestor-context-dan-metrik-exact-match | FE+BE |
| TC-FA-GRP-75 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-76 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-77 | E2E | TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | FE+BE |
| TC-FA-GRP-78 | E2E | TC-FA-GRP-E2E-278-role-matrix-visibilitas-elemen-groups-list-read-only-dan-tanpa-aksi-tulis | FE+BE |
| TC-FA-GRP-79 | E2E | TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | FE+BE |
| TC-FA-GRP-80 | E2E | TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | FE+BE |
| TC-FA-GRP-81 | E2E | TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | FE+BE |
| TC-FA-GRP-83 | E2E | TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | FE+BE |
| TC-FA-GRP-84 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-85 | E2E | TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-86 | E2E | TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-87 | E2E | TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-88 | E2E | TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-89 | E2E | TC-FA-GRP-E2E-034-new-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-90 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-91 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-92 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-93 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-94 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-95 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-96 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-97 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-98 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-99 | E2E | TC-FA-GRP-E2E-036-new-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-100 | E2E | TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-101 | E2E | TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-102 | E2E | TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-103 | E2E | TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-104 | E2E | TC-FA-GRP-E2E-037-new-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-105 | E2E | TC-FA-GRP-E2E-038-new-group-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-106 | E2E | TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-107 | E2E | TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-108 | E2E | TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-109 | E2E | TC-FA-GRP-E2E-038-new-group-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-110 | E2E | TC-FA-GRP-E2E-067-resilience-form-new-group-new-subgroup-dan-edit-group-gagal-server | FE+BE |
| TC-FA-GRP-111 | E2E | TC-FA-GRP-E2E-038-new-group-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-112 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-113 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-114 | E2E | TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap | FE+BE |
| TC-FA-GRP-115 | E2E | TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap | FE+BE |
| TC-FA-GRP-116 | E2E | TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap | FE+BE |
| TC-FA-GRP-117 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-118 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-119 | E2E | TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | FE+BE |
| TC-FA-GRP-120 | E2E | TC-FA-GRP-E2E-040-plan-gating-block-batas-jumlah-group-starter-growth-dan-stay-on-form | FE+BE |
| TC-FA-GRP-121 | E2E | TC-FA-GRP-E2E-041-plan-gating-block-batas-kedalaman-batas-platform-dan-enterprise-tanpa-cek-cap | FE+BE |
| TC-FA-GRP-122 | E2E | TC-FA-GRP-E2E-042-plan-gating-dialog-ok-esc-backdrop-dan-penurunan-cap-depth-tidak-memangkas-node | FE+BE |
| TC-FA-GRP-123 | E2E | TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | FE+BE |
| TC-FA-GRP-124 | E2E | TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | FE+BE |
| TC-FA-GRP-125 | E2E | TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar | FE+BE |
| TC-FA-GRP-126 | E2E | TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar | FE+BE |
| TC-FA-GRP-127 | E2E | TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar | FE+BE |
| TC-FA-GRP-128 | E2E | TC-FA-GRP-E2E-044-new-subgroup-screening-popup-konteks-under-dan-create-via-row-action-dan-sidebar | FE+BE |
| TC-FA-GRP-129 | E2E | TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | FE+BE |
| TC-FA-GRP-130 | E2E | TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | FE+BE |
| TC-FA-GRP-131 | E2E | TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | FE+BE |
| TC-FA-GRP-132 | E2E | TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | FE+BE |
| TC-FA-GRP-133 | E2E | TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-134 | E2E | TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-135 | E2E | TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-136 | E2E | TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-137 | E2E | TC-FA-GRP-E2E-047-new-subgroup-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-138 | E2E | TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-139 | E2E | TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-140 | E2E | TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-141 | E2E | TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-142 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-143 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-144 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-145 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-146 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-147 | E2E | TC-FA-GRP-E2E-049-new-subgroup-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-148 | E2E | TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-149 | E2E | TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-150 | E2E | TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-151 | E2E | TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-152 | E2E | TC-FA-GRP-E2E-050-new-subgroup-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-153 | E2E | TC-FA-GRP-E2E-051-new-subgroup-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-154 | E2E | TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-155 | E2E | TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-156 | E2E | TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-157 | E2E | TC-FA-GRP-E2E-051-new-subgroup-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-158 | E2E | TC-FA-GRP-E2E-067-resilience-form-new-group-new-subgroup-dan-edit-group-gagal-server | FE+BE |
| TC-FA-GRP-159 | E2E | TC-FA-GRP-E2E-051-new-subgroup-hover-saving-submit-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-160 | E2E | TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | FE+BE |
| TC-FA-GRP-161 | E2E | TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | FE+BE |
| TC-FA-GRP-162 | E2E | TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | FE+BE |
| TC-FA-GRP-163 | E2E | TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | FE+BE |
| TC-FA-GRP-164 | E2E | TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi | FE+BE |
| TC-FA-GRP-165 | E2E | TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi | FE+BE |
| TC-FA-GRP-166 | E2E | TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi | FE+BE |
| TC-FA-GRP-167 | E2E | TC-FA-GRP-E2E-054-edit-group-ubah-name-dan-code-sekaligus-code-dikosongkan-generate-ulang-dan-kapitalisasi | FE+BE |
| TC-FA-GRP-168 | E2E | TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved | FE+BE |
| TC-FA-GRP-169 | E2E | TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved | FE+BE |
| TC-FA-GRP-170 | E2E | TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved | FE+BE |
| TC-FA-GRP-171 | E2E | TC-FA-GRP-E2E-056-edit-function-assignable-ke-none-dialog-change-function | FE+BE |
| TC-FA-GRP-172 | E2E | TC-FA-GRP-E2E-056-edit-function-assignable-ke-none-dialog-change-function | FE+BE |
| TC-FA-GRP-173 | E2E | TC-FA-GRP-E2E-056-edit-function-assignable-ke-none-dialog-change-function | FE+BE |
| TC-FA-GRP-183 | E2E | TC-FA-GRP-E2E-058-edit-function-none-ke-assignable-tanpa-dialog-histori-transaksi-dan-bersamaan-name | FE+BE |
| TC-FA-GRP-185 | E2E | TC-FA-GRP-E2E-058-edit-function-none-ke-assignable-tanpa-dialog-histori-transaksi-dan-bersamaan-name | FE+BE |
| TC-FA-GRP-186 | E2E | TC-FA-GRP-E2E-058-edit-function-none-ke-assignable-tanpa-dialog-histori-transaksi-dan-bersamaan-name | FE+BE |
| TC-FA-GRP-187 | E2E | TC-FA-GRP-E2E-060-edit-node-excess-node-menjadi-excess-saat-popup-terbuka-dan-node-dihapus-user-lain | FE+BE |
| TC-FA-GRP-188 | E2E | TC-FA-GRP-E2E-060-edit-node-excess-node-menjadi-excess-saat-popup-terbuka-dan-node-dihapus-user-lain | FE+BE |
| TC-FA-GRP-189 | E2E | TC-FA-GRP-E2E-060-edit-node-excess-node-menjadi-excess-saat-popup-terbuka-dan-node-dihapus-user-lain | FE+BE |
| TC-FA-GRP-190 | E2E | TC-FA-GRP-E2E-279-konflik-dua-admin-edit-bersamaan-last-write-wins-dan-code-auto-generate-bentrok | FE+BE |
| TC-FA-GRP-191 | E2E | TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-192 | E2E | TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-193 | E2E | TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-194 | E2E | TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-195 | E2E | TC-FA-GRP-E2E-061-edit-group-validasi-group-name-kosong-batas-120-duplikat-sibling | FE+BE |
| TC-FA-GRP-196 | E2E | TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-197 | E2E | TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-198 | E2E | TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-199 | E2E | TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-200 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-201 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-202 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-203 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-204 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-205 | E2E | TC-FA-GRP-E2E-063-edit-group-validasi-code-batas-15-karakter-whitelist-uppercase-dan-duplikat | FE+BE |
| TC-FA-GRP-206 | E2E | TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-207 | E2E | TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-208 | E2E | TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-209 | E2E | TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-210 | E2E | TC-FA-GRP-E2E-064-edit-group-validasi-description-function-tooltip-radio-dan-clear-field | FE+BE |
| TC-FA-GRP-211 | E2E | TC-FA-GRP-E2E-065-edit-group-hover-saving-save-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-212 | E2E | TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-213 | E2E | TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-214 | E2E | TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-215 | E2E | TC-FA-GRP-E2E-065-edit-group-hover-saving-save-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-216 | E2E | TC-FA-GRP-E2E-067-resilience-form-new-group-new-subgroup-dan-edit-group-gagal-server | FE+BE |
| TC-FA-GRP-217 | E2E | TC-FA-GRP-E2E-065-edit-group-hover-saving-save-double-click-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-218 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-219 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-220 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-221 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-222 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-223 | E2E | TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning | FE+BE |
| TC-FA-GRP-224 | E2E | TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning | FE+BE |
| TC-FA-GRP-225 | E2E | TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver | FE+BE |
| TC-FA-GRP-226 | E2E | TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver | FE+BE |
| TC-FA-GRP-227 | E2E | TC-FA-GRP-E2E-074-delete-diblok-last-group-satu-satunya-group-dan-satu-satunya-root-dengan-subgroup | FE+BE |
| TC-FA-GRP-228 | E2E | TC-FA-GRP-E2E-074-delete-diblok-last-group-satu-satunya-group-dan-satu-satunya-root-dengan-subgroup | FE+BE |
| TC-FA-GRP-229 | E2E | TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | FE+BE |
| TC-FA-GRP-230 | E2E | TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | FE+BE |
| TC-FA-GRP-231 | E2E | TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | FE+BE |
| TC-FA-GRP-232 | E2E | TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-belum-tuntas | FE+BE |
| TC-FA-GRP-233 | E2E | TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-belum-tuntas | FE+BE |
| TC-FA-GRP-234 | E2E | TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-belum-tuntas | FE+BE |
| TC-FA-GRP-236 | E2E | TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif | FE+BE |
| TC-FA-GRP-237 | E2E | TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif | FE+BE |
| TC-FA-GRP-238 | E2E | TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | FE+BE |
| TC-FA-GRP-239 | E2E | TC-FA-GRP-E2E-071-delete-screening-dialog-konfirmasi-cancel-delete-node-kosong-cascade-dan-node-assignable-aset-disposed | FE+BE |
| TC-FA-GRP-240 | E2E | TC-FA-GRP-E2E-079-delete-dan-bulk-delete-node-excess-auto-reset-excess-saat-count-di-bawah-cap | FE+BE |
| TC-FA-GRP-241 | E2E | TC-FA-GRP-E2E-079-delete-dan-bulk-delete-node-excess-auto-reset-excess-saat-count-di-bawah-cap | FE+BE |
| TC-FA-GRP-242 | E2E | TC-FA-GRP-E2E-078-delete-race-node-dihapus-user-lain-double-click-dan-aksesibilitas-dialog | FE+BE |
| TC-FA-GRP-243 | E2E | TC-FA-GRP-E2E-088-resilience-delete-bulk-delete-dan-wizard-gagal-server | FE+BE |
| TC-FA-GRP-244 | E2E | TC-FA-GRP-E2E-078-delete-race-node-dihapus-user-lain-double-click-dan-aksesibilitas-dialog | FE+BE |
| TC-FA-GRP-245 | E2E | TC-FA-GRP-E2E-078-delete-race-node-dihapus-user-lain-double-click-dan-aksesibilitas-dialog | FE+BE |
| TC-FA-GRP-246 | E2E | TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | FE+BE |
| TC-FA-GRP-247 | E2E | TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | FE+BE |
| TC-FA-GRP-248 | E2E | TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | FE+BE |
| TC-FA-GRP-249 | E2E | TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | FE+BE |
| TC-FA-GRP-250 | E2E | TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | FE+BE |
| TC-FA-GRP-251 | E2E | TC-FA-GRP-E2E-081-bulk-seleksi-persist-lintas-halaman-search-filter-dan-reset-saat-node-berganti | FE+BE |
| TC-FA-GRP-252 | E2E | TC-FA-GRP-E2E-082-bulk-selection-limit-diturunkan-blok-live-dan-select-all-di-cap | FE+BE |
| TC-FA-GRP-253 | E2E | TC-FA-GRP-E2E-082-bulk-selection-limit-diturunkan-blok-live-dan-select-all-di-cap | FE+BE |
| TC-FA-GRP-254 | E2E | TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | FE+BE |
| TC-FA-GRP-255 | E2E | TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | FE+BE |
| TC-FA-GRP-256 | E2E | TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total | FE+BE |
| TC-FA-GRP-257 | E2E | TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total | FE+BE |
| TC-FA-GRP-258 | E2E | TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total | FE+BE |
| TC-FA-GRP-259 | E2E | TC-FA-GRP-E2E-085-bulk-delete-would-empty-dan-scope-aktor-jadi-kosong | FE+BE |
| TC-FA-GRP-260 | E2E | TC-FA-GRP-E2E-085-bulk-delete-would-empty-dan-scope-aktor-jadi-kosong | FE+BE |
| TC-FA-GRP-261 | E2E | TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | FE+BE |
| TC-FA-GRP-262 | E2E | TC-FA-GRP-E2E-084-bulk-delete-campuran-dan-semua-terblok-dialog-continue-dan-blokir-total | FE+BE |
| TC-FA-GRP-263 | E2E | TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | FE+BE |
| TC-FA-GRP-264 | E2E | TC-FA-GRP-E2E-086-bulk-delete-kondisi-berubah-setelah-dialog-semua-terskip-dan-item-sudah-dihapus | FE+BE |
| TC-FA-GRP-265 | E2E | TC-FA-GRP-E2E-086-bulk-delete-kondisi-berubah-setelah-dialog-semua-terskip-dan-item-sudah-dihapus | FE+BE |
| TC-FA-GRP-266 | E2E | TC-FA-GRP-E2E-086-bulk-delete-kondisi-berubah-setelah-dialog-semua-terskip-dan-item-sudah-dihapus | FE+BE |
| TC-FA-GRP-267 | E2E | TC-FA-GRP-E2E-088-resilience-delete-bulk-delete-dan-wizard-gagal-server | FE+BE |
| TC-FA-GRP-268 | E2E | TC-FA-GRP-E2E-087-bulk-delete-parent-dan-descendant-tidak-sama-sama-terpilih-dan-satu-group-identik-single | FE+BE |
| TC-FA-GRP-269 | E2E | TC-FA-GRP-E2E-079-delete-dan-bulk-delete-node-excess-auto-reset-excess-saat-count-di-bawah-cap | FE+BE |
| TC-FA-GRP-270 | E2E | TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | FE+BE |
| TC-FA-GRP-271 | E2E | TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | FE+BE |
| TC-FA-GRP-272 | E2E | TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | FE+BE |
| TC-FA-GRP-273 | E2E | TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | FE+BE |
| TC-FA-GRP-274 | E2E | TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | FE+BE |
| TC-FA-GRP-275 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-276 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-277 | E2E | TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime | FE+BE |
| TC-FA-GRP-282 | E2E | TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets | FE+BE |
| TC-FA-GRP-283 | E2E | TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets | FE+BE |
| TC-FA-GRP-284 | E2E | TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | FE+BE |
| TC-FA-GRP-285 | E2E | TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | FE+BE |
| TC-FA-GRP-286 | E2E | TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime | FE+BE |
| TC-FA-GRP-287 | E2E | TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime | FE+BE |
| TC-FA-GRP-288 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-289 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-290 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-291 | E2E | TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets | FE+BE |
| TC-FA-GRP-292 | E2E | TC-FA-GRP-E2E-028-klik-total-asset-header-dan-kolom-empty-state-dan-angka-realtime | FE+BE |
| TC-FA-GRP-293 | E2E | TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user | FE+BE |
| TC-FA-GRP-294 | E2E | TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user | FE+BE |
| TC-FA-GRP-295 | E2E | TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user | FE+BE |
| TC-FA-GRP-296 | E2E | TC-FA-GRP-E2E-031-tab-users-detail-kolom-group-role-per-jenis-user-avatar-nama-dan-realtime-assignment | FE+BE |
| TC-FA-GRP-298 | E2E | TC-FA-GRP-E2E-029-resilience-popup-detail-loading-per-tab-dan-error-load-tab-users-assets | FE+BE |
| TC-FA-GRP-299 | E2E | TC-FA-GRP-E2E-031-tab-users-detail-kolom-group-role-per-jenis-user-avatar-nama-dan-realtime-assignment | FE+BE |
| TC-FA-GRP-300 | E2E | TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | FE+BE |
| TC-FA-GRP-301 | E2E | TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | FE+BE |
| TC-FA-GRP-302 | E2E | TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | FE+BE |
| TC-FA-GRP-303 | E2E | TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0 | FE+BE |
| TC-FA-GRP-304 | E2E | TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | FE+BE |
| TC-FA-GRP-305 | E2E | TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0 | FE+BE |
| TC-FA-GRP-306 | E2E | TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0 | FE+BE |
| TC-FA-GRP-307 | E2E | TC-FA-GRP-E2E-088-resilience-delete-bulk-delete-dan-wizard-gagal-server | FE+BE |
| TC-FA-GRP-308 | E2E | TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | FE+BE |
| TC-FA-GRP-309 | E2E | TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | FE+BE |
| TC-FA-GRP-310 | E2E | TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | FE+BE |
| TC-FA-GRP-311 | E2E | TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | FE+BE |
| TC-FA-GRP-312 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-313 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-314 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-315 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-316 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-317 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-318 | E2E | TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | FE+BE |
| TC-FA-GRP-319 | E2E | TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | FE+BE |
| TC-FA-GRP-320 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-321 | E2E | TC-FA-GRP-E2E-068-code-auto-generate-token-numerik-inisial-alfabetik-dan-pemisah | FE+BE |
| TC-FA-GRP-322 | E2E | TC-FA-GRP-E2E-068-code-auto-generate-token-numerik-inisial-alfabetik-dan-pemisah | FE+BE |
| TC-FA-GRP-323 | E2E | TC-FA-GRP-E2E-068-code-auto-generate-token-numerik-inisial-alfabetik-dan-pemisah | FE+BE |
| TC-FA-GRP-324 | E2E | TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | FE+BE |
| TC-FA-GRP-325 | E2E | TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | FE+BE |
| TC-FA-GRP-326 | E2E | TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | FE+BE |
| TC-FA-GRP-327 | E2E | TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | FE+BE |
| TC-FA-GRP-328 | E2E | TC-FA-GRP-E2E-069-code-auto-generate-token-alfanumerik-karakter-tidak-valid-dan-fallback-empat-karakter-acak | FE+BE |
| TC-FA-GRP-329 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-330 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-331 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-332 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-333 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-334 | E2E | TC-FA-GRP-E2E-279-konflik-dua-admin-edit-bersamaan-last-write-wins-dan-code-auto-generate-bentrok | FE+BE |
| TC-FA-GRP-335 | E2E | TC-FA-GRP-E2E-279-konflik-dua-admin-edit-bersamaan-last-write-wins-dan-code-auto-generate-bentrok | FE+BE |
| TC-FA-GRP-336 | E2E | TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-337 | E2E | TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | FE+BE |
| TC-FA-GRP-338 | E2E | TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | FE+BE |
| TC-FA-GRP-339 | E2E | TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | FE+BE |
| TC-FA-GRP-340 | E2E | TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node | FE+BE |
| TC-FA-GRP-341 | E2E | TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node | FE+BE |
| TC-FA-GRP-342 | E2E | TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node | FE+BE |
| TC-FA-GRP-343 | E2E | TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-344 | E2E | TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-345 | E2E | TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | FE+BE |
| TC-FA-GRP-346 | E2E | TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | FE+BE |
| TC-FA-GRP-347 | E2E | TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | FE+BE |
| TC-FA-GRP-348 | E2E | TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | FE+BE |
| TC-FA-GRP-349 | E2E | TC-FA-GRP-E2E-108-groups-list-filter-panel-screening-dan-filter-function-opsi-search-dropdown | FE+BE |
| TC-FA-GRP-350 | E2E | TC-FA-GRP-E2E-109-groups-list-filter-function-chip-opsi-dan-kombinasi-and-antar-field | FE+BE |
| TC-FA-GRP-351 | E2E | TC-FA-GRP-E2E-109-groups-list-filter-function-chip-opsi-dan-kombinasi-and-antar-field | FE+BE |
| TC-FA-GRP-352 | E2E | TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | FE+BE |
| TC-FA-GRP-353 | E2E | TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | FE+BE |
| TC-FA-GRP-354 | E2E | TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | FE+BE |
| TC-FA-GRP-355 | E2E | TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | FE+BE |
| TC-FA-GRP-356 | E2E | TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-357 | E2E | TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-358 | E2E | TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-359 | E2E | TC-FA-GRP-E2E-112-groups-list-filter-modified-by-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-360 | E2E | TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | FE+BE |
| TC-FA-GRP-361 | E2E | TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | FE+BE |
| TC-FA-GRP-362 | E2E | TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | FE+BE |
| TC-FA-GRP-363 | E2E | TC-FA-GRP-E2E-109-groups-list-filter-function-chip-opsi-dan-kombinasi-and-antar-field | FE+BE |
| TC-FA-GRP-364 | E2E | TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | FE+BE |
| TC-FA-GRP-365 | E2E | TC-FA-GRP-E2E-114-groups-list-kombinasi-search-lalu-filter-dan-filter-lalu-search-irisan | FE+BE |
| TC-FA-GRP-366 | E2E | TC-FA-GRP-E2E-114-groups-list-kombinasi-search-lalu-filter-dan-filter-lalu-search-irisan | FE+BE |
| TC-FA-GRP-367 | E2E | TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral | FE+BE |
| TC-FA-GRP-368 | E2E | TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral | FE+BE |
| TC-FA-GRP-369 | E2E | TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral | FE+BE |
| TC-FA-GRP-370 | E2E | TC-FA-GRP-E2E-116-groups-list-sort-kolom-group-code-function-dan-total-asset-siklus-asc-desc-netral | FE+BE |
| TC-FA-GRP-371 | E2E | TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | FE+BE |
| TC-FA-GRP-372 | E2E | TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | FE+BE |
| TC-FA-GRP-373 | E2E | TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | FE+BE |
| TC-FA-GRP-374 | E2E | TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | FE+BE |
| TC-FA-GRP-375 | E2E | TC-FA-GRP-E2E-284-groups-list-kombinasi-search-filter-sort-pagination-dan-clear-filter-saat-search-sort-aktif | FE+BE |
| TC-FA-GRP-376 | E2E | TC-FA-GRP-E2E-284-groups-list-kombinasi-search-filter-sort-pagination-dan-clear-filter-saat-search-sort-aktif | FE+BE |
| TC-FA-GRP-377 | E2E | TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-378 | E2E | TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-379 | E2E | TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-380 | E2E | TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-381 | E2E | TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-382 | E2E | TC-FA-GRP-E2E-120-groups-list-setup-column-uncheck-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-383 | E2E | TC-FA-GRP-E2E-120-groups-list-setup-column-uncheck-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-384 | E2E | TC-FA-GRP-E2E-120-groups-list-setup-column-uncheck-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-385 | E2E | TC-FA-GRP-E2E-120-groups-list-setup-column-uncheck-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-386 | E2E | TC-FA-GRP-E2E-121-groups-list-setup-column-uncheck-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-387 | E2E | TC-FA-GRP-E2E-121-groups-list-setup-column-uncheck-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-388 | E2E | TC-FA-GRP-E2E-121-groups-list-setup-column-uncheck-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-389 | E2E | TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-390 | E2E | TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-391 | E2E | TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-392 | E2E | TC-FA-GRP-E2E-122-groups-list-setup-column-geser-drag-kolom-group-code-function-total-asset | FE+BE |
| TC-FA-GRP-393 | E2E | TC-FA-GRP-E2E-123-groups-list-setup-column-geser-drag-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-394 | E2E | TC-FA-GRP-E2E-123-groups-list-setup-column-geser-drag-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-395 | E2E | TC-FA-GRP-E2E-123-groups-list-setup-column-geser-drag-kolom-total-user-modified-by-last-updated | FE+BE |
| TC-FA-GRP-396 | E2E | TC-FA-GRP-E2E-124-groups-list-setup-column-pin-kolom-group-code-dan-function | FE+BE |
| TC-FA-GRP-397 | E2E | TC-FA-GRP-E2E-124-groups-list-setup-column-pin-kolom-group-code-dan-function | FE+BE |
| TC-FA-GRP-398 | E2E | TC-FA-GRP-E2E-124-groups-list-setup-column-pin-kolom-group-code-dan-function | FE+BE |
| TC-FA-GRP-399 | E2E | TC-FA-GRP-E2E-125-groups-list-setup-column-pin-kolom-total-asset-dan-total-user | FE+BE |
| TC-FA-GRP-400 | E2E | TC-FA-GRP-E2E-125-groups-list-setup-column-pin-kolom-total-asset-dan-total-user | FE+BE |
| TC-FA-GRP-401 | E2E | TC-FA-GRP-E2E-126-groups-list-setup-column-pin-kolom-modified-by-dan-last-updated | FE+BE |
| TC-FA-GRP-402 | E2E | TC-FA-GRP-E2E-126-groups-list-setup-column-pin-kolom-modified-by-dan-last-updated | FE+BE |
| TC-FA-GRP-403 | E2E | TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-404 | E2E | TC-FA-GRP-E2E-119-groups-list-setup-column-reset-to-default-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-405 | E2E | TC-FA-GRP-E2E-119-groups-list-setup-column-reset-to-default-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-406 | E2E | TC-FA-GRP-E2E-119-groups-list-setup-column-reset-to-default-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-407 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-408 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-409 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-410 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-411 | E2E | TC-FA-GRP-E2E-160-resilience-download-groups-list-modal-changelog-dan-loading-error-load-changelog | FE+BE |
| TC-FA-GRP-412 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-413 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-414 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-415 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-416 | E2E | TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-417 | E2E | TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-418 | E2E | TC-FA-GRP-E2E-107-groups-list-search-per-kolom-total-asset-total-user-modified-by-dan-lokal-terhadap-node | FE+BE |
| TC-FA-GRP-419 | E2E | TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | FE+BE |
| TC-FA-GRP-420 | E2E | TC-FA-GRP-E2E-106-groups-list-search-per-kolom-group-code-function-nilai-penuh-none-dan-assignable | FE+BE |
| TC-FA-GRP-421 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-422 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-423 | E2E | TC-FA-GRP-E2E-129-groups-list-download-lebih-5000-baris-loading-screen-tanpa-job-background | FE+BE |
| TC-FA-GRP-424 | E2E | TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi | FE+BE |
| TC-FA-GRP-425 | E2E | TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi | FE+BE |
| TC-FA-GRP-426 | E2E | TC-FA-GRP-E2E-081-bulk-seleksi-persist-lintas-halaman-search-filter-dan-reset-saat-node-berganti | FE+BE |
| TC-FA-GRP-427 | E2E | TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | FE+BE |
| TC-FA-GRP-428 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-429 | E2E | TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | FE+BE |
| TC-FA-GRP-430 | E2E | TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | FE+BE |
| TC-FA-GRP-431 | E2E | TC-FA-GRP-E2E-160-resilience-download-groups-list-modal-changelog-dan-loading-error-load-changelog | FE+BE |
| TC-FA-GRP-432 | E2E | TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide | FE+BE |
| TC-FA-GRP-433 | E2E | TC-FA-GRP-E2E-134-modal-changelog-search-per-kolom-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-434 | E2E | TC-FA-GRP-E2E-134-modal-changelog-search-per-kolom-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-435 | E2E | TC-FA-GRP-E2E-134-modal-changelog-search-per-kolom-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-436 | E2E | TC-FA-GRP-E2E-135-modal-changelog-search-per-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-437 | E2E | TC-FA-GRP-E2E-135-modal-changelog-search-per-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-438 | E2E | TC-FA-GRP-E2E-135-modal-changelog-search-per-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-439 | E2E | TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide | FE+BE |
| TC-FA-GRP-440 | E2E | TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide | FE+BE |
| TC-FA-GRP-441 | E2E | TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-442 | E2E | TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-443 | E2E | TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-444 | E2E | TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-445 | E2E | TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-446 | E2E | TC-FA-GRP-E2E-137-modal-changelog-filter-action-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-447 | E2E | TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name | FE+BE |
| TC-FA-GRP-448 | E2E | TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name | FE+BE |
| TC-FA-GRP-449 | E2E | TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-450 | E2E | TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-451 | E2E | TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-452 | E2E | TC-FA-GRP-E2E-138-modal-changelog-filter-group-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-453 | E2E | TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name | FE+BE |
| TC-FA-GRP-454 | E2E | TC-FA-GRP-E2E-141-modal-changelog-filter-chip-opsi-action-dan-group-name | FE+BE |
| TC-FA-GRP-455 | E2E | TC-FA-GRP-E2E-139-modal-changelog-filter-field-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-456 | E2E | TC-FA-GRP-E2E-139-modal-changelog-filter-field-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-457 | E2E | TC-FA-GRP-E2E-139-modal-changelog-filter-field-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-458 | E2E | TC-FA-GRP-E2E-139-modal-changelog-filter-field-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-459 | E2E | TC-FA-GRP-E2E-142-modal-changelog-filter-chip-opsi-field-dan-modified-by | FE+BE |
| TC-FA-GRP-460 | E2E | TC-FA-GRP-E2E-142-modal-changelog-filter-chip-opsi-field-dan-modified-by | FE+BE |
| TC-FA-GRP-461 | E2E | TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-462 | E2E | TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-463 | E2E | TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-464 | E2E | TC-FA-GRP-E2E-140-modal-changelog-filter-modified-by-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-465 | E2E | TC-FA-GRP-E2E-142-modal-changelog-filter-chip-opsi-field-dan-modified-by | FE+BE |
| TC-FA-GRP-466 | E2E | TC-FA-GRP-E2E-142-modal-changelog-filter-chip-opsi-field-dan-modified-by | FE+BE |
| TC-FA-GRP-467 | E2E | TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-468 | E2E | TC-FA-GRP-E2E-136-modal-changelog-filter-panel-screening-rentang-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-469 | E2E | TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination | FE+BE |
| TC-FA-GRP-470 | E2E | TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination | FE+BE |
| TC-FA-GRP-471 | E2E | TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-472 | E2E | TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-473 | E2E | TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-474 | E2E | TC-FA-GRP-E2E-145-modal-changelog-sort-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-475 | E2E | TC-FA-GRP-E2E-146-modal-changelog-sort-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-476 | E2E | TC-FA-GRP-E2E-146-modal-changelog-sort-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-477 | E2E | TC-FA-GRP-E2E-146-modal-changelog-sort-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-478 | E2E | TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination | FE+BE |
| TC-FA-GRP-479 | E2E | TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-480 | E2E | TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-481 | E2E | TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-482 | E2E | TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | FE+BE |
| TC-FA-GRP-483 | E2E | TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-484 | E2E | TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-485 | E2E | TC-FA-GRP-E2E-149-modal-changelog-setup-column-uncheck-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-486 | E2E | TC-FA-GRP-E2E-149-modal-changelog-setup-column-uncheck-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-487 | E2E | TC-FA-GRP-E2E-149-modal-changelog-setup-column-uncheck-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-488 | E2E | TC-FA-GRP-E2E-149-modal-changelog-setup-column-uncheck-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-489 | E2E | TC-FA-GRP-E2E-150-modal-changelog-setup-column-uncheck-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-490 | E2E | TC-FA-GRP-E2E-150-modal-changelog-setup-column-uncheck-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-491 | E2E | TC-FA-GRP-E2E-150-modal-changelog-setup-column-uncheck-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-492 | E2E | TC-FA-GRP-E2E-151-modal-changelog-setup-column-geser-drag-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-493 | E2E | TC-FA-GRP-E2E-151-modal-changelog-setup-column-geser-drag-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-494 | E2E | TC-FA-GRP-E2E-151-modal-changelog-setup-column-geser-drag-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-495 | E2E | TC-FA-GRP-E2E-151-modal-changelog-setup-column-geser-drag-kolom-date-action-group-name-dan-field | FE+BE |
| TC-FA-GRP-496 | E2E | TC-FA-GRP-E2E-152-modal-changelog-setup-column-geser-drag-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-497 | E2E | TC-FA-GRP-E2E-152-modal-changelog-setup-column-geser-drag-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-498 | E2E | TC-FA-GRP-E2E-152-modal-changelog-setup-column-geser-drag-kolom-old-value-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-499 | E2E | TC-FA-GRP-E2E-153-modal-changelog-setup-column-pin-kolom-date-action-dan-group-name | FE+BE |
| TC-FA-GRP-500 | E2E | TC-FA-GRP-E2E-153-modal-changelog-setup-column-pin-kolom-date-action-dan-group-name | FE+BE |
| TC-FA-GRP-501 | E2E | TC-FA-GRP-E2E-153-modal-changelog-setup-column-pin-kolom-date-action-dan-group-name | FE+BE |
| TC-FA-GRP-502 | E2E | TC-FA-GRP-E2E-154-modal-changelog-setup-column-pin-kolom-field-dan-old-value | FE+BE |
| TC-FA-GRP-503 | E2E | TC-FA-GRP-E2E-154-modal-changelog-setup-column-pin-kolom-field-dan-old-value | FE+BE |
| TC-FA-GRP-504 | E2E | TC-FA-GRP-E2E-155-modal-changelog-setup-column-pin-kolom-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-505 | E2E | TC-FA-GRP-E2E-155-modal-changelog-setup-column-pin-kolom-new-value-dan-modified-by | FE+BE |
| TC-FA-GRP-506 | E2E | TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-507 | E2E | TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-508 | E2E | TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-509 | E2E | TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain | FE+BE |
| TC-FA-GRP-510 | E2E | TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-511 | E2E | TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-512 | E2E | TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-513 | E2E | TC-FA-GRP-E2E-156-modal-changelog-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-514 | E2E | TC-FA-GRP-E2E-160-resilience-download-groups-list-modal-changelog-dan-loading-error-load-changelog | FE+BE |
| TC-FA-GRP-515 | E2E | TC-FA-GRP-E2E-157-modal-changelog-download-isi-berkas-transformasi-tipe-date-dan-empty | FE+BE |
| TC-FA-GRP-516 | E2E | TC-FA-GRP-E2E-157-modal-changelog-download-isi-berkas-transformasi-tipe-date-dan-empty | FE+BE |
| TC-FA-GRP-517 | E2E | TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-518 | E2E | TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-572 | E2E | TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | FE+BE |
| TC-FA-GRP-573 | E2E | TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-574 | E2E | TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-575 | E2E | TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-576 | E2E | TC-FA-GRP-E2E-162-tab-users-search-per-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-577 | E2E | TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | FE+BE |
| TC-FA-GRP-579 | E2E | TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-580 | E2E | TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-581 | E2E | TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-582 | E2E | TC-FA-GRP-E2E-163-tab-users-search-per-kolom-activation-status-temporary-user-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-583 | E2E | TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | FE+BE |
| TC-FA-GRP-584 | E2E | TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | FE+BE |
| TC-FA-GRP-585 | E2E | TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-586 | E2E | TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-587 | E2E | TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-588 | E2E | TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-589 | E2E | TC-FA-GRP-E2E-165-tab-users-filter-panel-screening-dan-filter-position-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-590 | E2E | TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | FE+BE |
| TC-FA-GRP-591 | E2E | TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | FE+BE |
| TC-FA-GRP-592 | E2E | TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | FE+BE |
| TC-FA-GRP-593 | E2E | TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | FE+BE |
| TC-FA-GRP-594 | E2E | TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | FE+BE |
| TC-FA-GRP-595 | E2E | TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | FE+BE |
| TC-FA-GRP-596 | E2E | TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | FE+BE |
| TC-FA-GRP-597 | E2E | TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | FE+BE |
| TC-FA-GRP-598 | E2E | TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-599 | E2E | TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-600 | E2E | TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-601 | E2E | TC-FA-GRP-E2E-168-tab-users-filter-group-role-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-602 | E2E | TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status | FE+BE |
| TC-FA-GRP-603 | E2E | TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status | FE+BE |
| TC-FA-GRP-610 | E2E | TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-611 | E2E | TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide | FE+BE |
| TC-FA-GRP-612 | E2E | TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide | FE+BE |
| TC-FA-GRP-613 | E2E | TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide | FE+BE |
| TC-FA-GRP-614 | E2E | TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-615 | E2E | TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-616 | E2E | TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-617 | E2E | TC-FA-GRP-E2E-174-tab-users-sort-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-618 | E2E | TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until | FE+BE |
| TC-FA-GRP-620 | E2E | TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until | FE+BE |
| TC-FA-GRP-621 | E2E | TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until | FE+BE |
| TC-FA-GRP-622 | E2E | TC-FA-GRP-E2E-175-tab-users-sort-kolom-group-role-activation-status-temporary-user-dan-temporary-until | FE+BE |
| TC-FA-GRP-623 | E2E | TC-FA-GRP-E2E-176-tab-users-sort-kolom-tag-custom-field-dan-nilai-kosong-tie-breaker | FE+BE |
| TC-FA-GRP-624 | E2E | TC-FA-GRP-E2E-176-tab-users-sort-kolom-tag-custom-field-dan-nilai-kosong-tie-breaker | FE+BE |
| TC-FA-GRP-625 | E2E | TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-FA-GRP-626 | E2E | TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-FA-GRP-627 | E2E | TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-FA-GRP-628 | E2E | TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-FA-GRP-629 | E2E | TC-FA-GRP-E2E-177-tab-users-kombinasi-search-filter-sort-clear-ganti-sort-dan-pemulihan-empty-state | FE+BE |
| TC-FA-GRP-630 | E2E | TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-631 | E2E | TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-632 | E2E | TC-FA-GRP-E2E-180-tab-users-setup-column-uncheck-kolom-name-email-position | FE+BE |
| TC-FA-GRP-633 | E2E | TC-FA-GRP-E2E-180-tab-users-setup-column-uncheck-kolom-name-email-position | FE+BE |
| TC-FA-GRP-634 | E2E | TC-FA-GRP-E2E-180-tab-users-setup-column-uncheck-kolom-name-email-position | FE+BE |
| TC-FA-GRP-635 | E2E | TC-FA-GRP-E2E-181-tab-users-setup-column-uncheck-kolom-division-group-role-dan-centang-activation-status | FE+BE |
| TC-FA-GRP-636 | E2E | TC-FA-GRP-E2E-181-tab-users-setup-column-uncheck-kolom-division-group-role-dan-centang-activation-status | FE+BE |
| TC-FA-GRP-638 | E2E | TC-FA-GRP-E2E-181-tab-users-setup-column-uncheck-kolom-division-group-role-dan-centang-activation-status | FE+BE |
| TC-FA-GRP-639 | E2E | TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-640 | E2E | TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-641 | E2E | TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-642 | E2E | TC-FA-GRP-E2E-182-tab-users-setup-column-centang-kolom-curated-temporary-user-until-tag-dan-custom-field | FE+BE |
| TC-FA-GRP-643 | E2E | TC-FA-GRP-E2E-183-tab-users-setup-column-geser-drag-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-644 | E2E | TC-FA-GRP-E2E-183-tab-users-setup-column-geser-drag-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-645 | E2E | TC-FA-GRP-E2E-183-tab-users-setup-column-geser-drag-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-646 | E2E | TC-FA-GRP-E2E-183-tab-users-setup-column-geser-drag-kolom-name-email-position-dan-division | FE+BE |
| TC-FA-GRP-647 | E2E | TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until | FE+BE |
| TC-FA-GRP-649 | E2E | TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until | FE+BE |
| TC-FA-GRP-650 | E2E | TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until | FE+BE |
| TC-FA-GRP-651 | E2E | TC-FA-GRP-E2E-184-tab-users-setup-column-geser-drag-kolom-group-role-activation-status-temporary-user-dan-until | FE+BE |
| TC-FA-GRP-652 | E2E | TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions | FE+BE |
| TC-FA-GRP-653 | E2E | TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions | FE+BE |
| TC-FA-GRP-654 | E2E | TC-FA-GRP-E2E-186-tab-users-setup-column-pin-kolom-name-email-dan-position | FE+BE |
| TC-FA-GRP-655 | E2E | TC-FA-GRP-E2E-186-tab-users-setup-column-pin-kolom-name-email-dan-position | FE+BE |
| TC-FA-GRP-656 | E2E | TC-FA-GRP-E2E-186-tab-users-setup-column-pin-kolom-name-email-dan-position | FE+BE |
| TC-FA-GRP-657 | E2E | TC-FA-GRP-E2E-187-tab-users-setup-column-pin-kolom-division-group-role-dan-activation-status | FE+BE |
| TC-FA-GRP-658 | E2E | TC-FA-GRP-E2E-187-tab-users-setup-column-pin-kolom-division-group-role-dan-activation-status | FE+BE |
| TC-FA-GRP-660 | E2E | TC-FA-GRP-E2E-187-tab-users-setup-column-pin-kolom-division-group-role-dan-activation-status | FE+BE |
| TC-FA-GRP-661 | E2E | TC-FA-GRP-E2E-188-tab-users-setup-column-pin-kolom-temporary-user-until-dan-tag | FE+BE |
| TC-FA-GRP-662 | E2E | TC-FA-GRP-E2E-188-tab-users-setup-column-pin-kolom-temporary-user-until-dan-tag | FE+BE |
| TC-FA-GRP-663 | E2E | TC-FA-GRP-E2E-188-tab-users-setup-column-pin-kolom-temporary-user-until-dan-tag | FE+BE |
| TC-FA-GRP-664 | E2E | TC-FA-GRP-E2E-189-tab-users-setup-column-pin-kolom-custom-field-dan-sel-tanpa-nilai-tampil-dash | FE+BE |
| TC-FA-GRP-665 | E2E | TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-666 | E2E | TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache | FE+BE |
| TC-FA-GRP-667 | E2E | TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache | FE+BE |
| TC-FA-GRP-668 | E2E | TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache | FE+BE |
| TC-FA-GRP-669 | E2E | TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-670 | E2E | TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-671 | E2E | TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-672 | E2E | TC-FA-GRP-E2E-190-tab-users-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-673 | E2E | TC-FA-GRP-E2E-193-resilience-download-tab-users-dan-tab-assets-gagal-server | FE+BE |
| TC-FA-GRP-674 | E2E | TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | FE+BE |
| TC-FA-GRP-675 | E2E | TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | FE+BE |
| TC-FA-GRP-676 | E2E | TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions | FE+BE |
| TC-FA-GRP-677 | E2E | TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide | FE+BE |
| TC-FA-GRP-678 | E2E | TC-FA-GRP-E2E-212-tab-assets-search-per-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-679 | E2E | TC-FA-GRP-E2E-212-tab-assets-search-per-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-680 | E2E | TC-FA-GRP-E2E-212-tab-assets-search-per-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-681 | E2E | TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide | FE+BE |
| TC-FA-GRP-682 | E2E | TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide | FE+BE |
| TC-FA-GRP-683 | E2E | TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-684 | E2E | TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-685 | E2E | TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-686 | E2E | TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | FE+BE |
| TC-FA-GRP-687 | E2E | TC-FA-GRP-E2E-215-tab-assets-filter-status-chip-opsi-dan-search-dropdown | FE+BE |
| TC-FA-GRP-688 | E2E | TC-FA-GRP-E2E-215-tab-assets-filter-status-chip-opsi-dan-search-dropdown | FE+BE |
| TC-FA-GRP-689 | E2E | TC-FA-GRP-E2E-215-tab-assets-filter-status-chip-opsi-dan-search-dropdown | FE+BE |
| TC-FA-GRP-690 | E2E | TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter | FE+BE |
| TC-FA-GRP-691 | E2E | TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter | FE+BE |
| TC-FA-GRP-692 | E2E | TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter | FE+BE |
| TC-FA-GRP-693 | E2E | TC-FA-GRP-E2E-218-tab-assets-filter-last-updated-kombinasi-status-clear-field-dan-irisan-search-filter | FE+BE |
| TC-FA-GRP-694 | E2E | TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear | FE+BE |
| TC-FA-GRP-695 | E2E | TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-696 | E2E | TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-697 | E2E | TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-698 | E2E | TC-FA-GRP-E2E-219-tab-assets-sort-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-699 | E2E | TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear | FE+BE |
| TC-FA-GRP-700 | E2E | TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear | FE+BE |
| TC-FA-GRP-701 | E2E | TC-FA-GRP-E2E-220-tab-assets-kombinasi-filter-lalu-search-search-filter-sort-dan-clear | FE+BE |
| TC-FA-GRP-702 | E2E | TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | FE+BE |
| TC-FA-GRP-703 | E2E | TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | FE+BE |
| TC-FA-GRP-704 | E2E | TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-705 | E2E | TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-706 | E2E | TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-707 | E2E | TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-708 | E2E | TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-709 | E2E | TC-FA-GRP-E2E-224-tab-assets-setup-column-uncheck-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-710 | E2E | TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-711 | E2E | TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-712 | E2E | TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-713 | E2E | TC-FA-GRP-E2E-225-tab-assets-setup-column-geser-drag-kolom-name-asset-id-status-dan-last-updated | FE+BE |
| TC-FA-GRP-714 | E2E | TC-FA-GRP-E2E-226-tab-assets-setup-column-pin-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-715 | E2E | TC-FA-GRP-E2E-226-tab-assets-setup-column-pin-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-716 | E2E | TC-FA-GRP-E2E-226-tab-assets-setup-column-pin-kolom-name-asset-id-dan-status | FE+BE |
| TC-FA-GRP-717 | E2E | TC-FA-GRP-E2E-227-tab-assets-setup-column-pin-last-updated-dan-uncheck-kolom-brand-model-type | FE+BE |
| TC-FA-GRP-718 | E2E | TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-719 | E2E | TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | FE+BE |
| TC-FA-GRP-720 | E2E | TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | FE+BE |
| TC-FA-GRP-721 | E2E | TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | FE+BE |
| TC-FA-GRP-722 | E2E | TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-723 | E2E | TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-724 | E2E | TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-725 | E2E | TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | FE+BE |
| TC-FA-GRP-726 | E2E | TC-FA-GRP-E2E-193-resilience-download-tab-users-dan-tab-assets-gagal-server | FE+BE |
| TC-FA-GRP-727 | E2E | TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | FE+BE |
| TC-FA-GRP-728 | E2E | TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | FE+BE |
| TC-FA-GRP-729 | E2E | TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | FE+BE |
| TC-FA-GRP-868 | E2E | TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-869 | E2E | TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-870 | E2E | TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-871 | E2E | TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-872 | E2E | TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-873 | E2E | TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-874 | E2E | TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-875 | E2E | TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-876 | E2E | TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-877 | E2E | TC-FA-GRP-E2E-197-log-marked-restored-excess-wizard-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-878 | E2E | TC-FA-GRP-E2E-197-log-marked-restored-excess-wizard-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-879 | E2E | TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris | FE+BE |
| TC-FA-GRP-880 | E2E | TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris | FE+BE |
| TC-FA-GRP-881 | E2E | TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris | FE+BE |
| TC-FA-GRP-882 | E2E | TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-883 | E2E | TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | FE+BE |
| TC-FA-GRP-884 | E2E | TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | FE+BE |
| TC-FA-GRP-885 | E2E | TC-FA-GRP-E2E-201-absence-log-edit-no-op-aksi-batal-dan-kegagalan-tulis-log-rollback | FE+BE |
| TC-FA-GRP-886 | E2E | TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | FE+BE |
| TC-FA-GRP-887 | E2E | TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | FE+BE |
| TC-FA-GRP-888 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-889 | E2E | TC-FA-GRP-E2E-200-log-pencabutan-assignment-saat-delete-di-log-user-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-FA-GRP-890 | E2E | TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | FE+BE |
| TC-FA-GRP-891 | E2E | TC-FA-GRP-E2E-201-absence-log-edit-no-op-aksi-batal-dan-kegagalan-tulis-log-rollback | FE+BE |
| TC-FA-GRP-892 | E2E | TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | FE+BE |
| TC-FA-GRP-893 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-894 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-895 | E2E | TC-FA-GRP-E2E-200-log-pencabutan-assignment-saat-delete-di-log-user-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-FA-GRP-896 | E2E | TC-FA-GRP-E2E-202-function-berubah-efek-ke-dropdown-register-asset-dan-transfer-dua-transisi | FE+BE |
| TC-FA-GRP-898 | E2E | TC-FA-GRP-E2E-202-function-berubah-efek-ke-dropdown-register-asset-dan-transfer-dua-transisi | FE+BE |
| TC-FA-GRP-902 | E2E | TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | FE+BE |
| TC-FA-GRP-903 | E2E | TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | FE+BE |
| TC-FA-GRP-904 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-905 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-906 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-907 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-908 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-909 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-910 | E2E | TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | FE+BE |
| TC-FA-GRP-911 | E2E | TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak | FE+BE |
| TC-FA-GRP-912 | E2E | TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak | FE+BE |
| TC-FA-GRP-913 | E2E | TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak | FE+BE |
| TC-FA-GRP-914 | E2E | TC-FA-GRP-E2E-206-format-tanggal-mengikuti-general-settings-groups-list-modal-changelog-dan-popup-detail | FE+BE |
| TC-FA-GRP-915 | E2E | TC-FA-GRP-E2E-206-format-tanggal-mengikuti-general-settings-groups-list-modal-changelog-dan-popup-detail | FE+BE |
| TC-FA-GRP-916 | E2E | TC-FA-GRP-E2E-206-format-tanggal-mengikuti-general-settings-groups-list-modal-changelog-dan-popup-detail | FE+BE |
| TC-FA-GRP-917 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-918 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-919 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-920 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-921 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-922 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-923 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-924 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-925 | E2E | TC-FA-GRP-E2E-208-defense-in-depth-bypass-api-capability-scope-dan-baca-detail-di-luar-scope | FE+BE |
| TC-FA-GRP-926 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-927 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-928 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-929 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-930 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-931 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-932 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-933 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-934 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-935 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-936 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-937 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-938 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-939 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-940 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-941 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-942 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-943 | E2E | TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | FE+BE |
| TC-FA-GRP-944 | E2E | TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | FE+BE |
| TC-FA-GRP-945 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-946 | E2E | TC-FA-GRP-E2E-008-navigasi-node-sidebar-direct-children-all-groups-noop-leaf-dan-transisi-empty-subgroup | FE+BE |
| TC-FA-GRP-947 | E2E | TC-FA-GRP-E2E-021-role-matrix-positif-edit-manage-group-ru-dan-group-manager | FE+BE |
| TC-FA-GRP-948 | E2E | TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | FE+BE |
| TC-FA-GRP-949 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-950 | E2E | TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | FE+BE |
| TC-FA-GRP-951 | E2E | TC-FA-GRP-E2E-002-interaksi-baris-groups-list-klik-baris-row-action-dan-bulk-action-icon | FE+BE |
| TC-FA-GRP-952 | E2E | TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | FE+BE |
| TC-FA-GRP-954 | E2E | TC-FA-GRP-E2E-185-tab-users-setup-column-geser-drag-kolom-tag-custom-field-dan-kolom-actions | FE+BE |
| TC-FA-GRP-955 | E2E | TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | FE+BE |
| TC-FA-GRP-957 | E2E | TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan | FE+BE |
| TC-FA-GRP-958 | E2E | TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan | FE+BE |
| TC-FA-GRP-959 | E2E | TC-FA-GRP-E2E-097-wizard-filter-total-asset-total-user-chip-opsi-dan-penerapan-ke-tabel | FE+BE |
| TC-FA-GRP-960 | E2E | TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir | FE+BE |
| TC-FA-GRP-961 | E2E | TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif | FE+BE |
| TC-FA-GRP-962 | E2E | TC-FA-GRP-E2E-090-wizard-group-consolidation-screening-counter-dan-validasi-save-selection | FE+BE |
| TC-FA-GRP-963 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-964 | E2E | TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | FE+BE |
| TC-FA-GRP-965 | E2E | TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | FE+BE |
| TC-FA-GRP-966 | E2E | TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | FE+BE |
| TC-FA-GRP-967 | E2E | TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | FE+BE |
| TC-FA-GRP-968 | E2E | TC-FA-GRP-E2E-009-group-context-header-metrik-exact-match-klik-angka-dan-all-groups | FE+BE |
| TC-FA-GRP-969 | E2E | TC-FA-GRP-E2E-010-group-context-header-all-groups-agregat-distinct-union-scope-aktor-scoped-dan-angka-tidak-dapat-diklik | FE+BE |
| TC-FA-GRP-970 | E2E | TC-FA-GRP-E2E-277-guided-tooltip-groups-sidebar-collapsed-dibuka-otomatis-dan-step-kolom-total-asset-dilewati | FE+BE |
| TC-FA-GRP-971 | E2E | TC-FA-GRP-E2E-014-android-guided-tooltip-drawer-dan-group-context-header-aktor-scoped | FE+BE |
| TC-FA-GRP-972 | E2E | TC-FA-GRP-E2E-042-plan-gating-dialog-ok-esc-backdrop-dan-penurunan-cap-depth-tidak-memangkas-node | FE+BE |
| TC-FA-GRP-973 | E2E | TC-FA-GRP-E2E-042-plan-gating-dialog-ok-esc-backdrop-dan-penurunan-cap-depth-tidak-memangkas-node | FE+BE |
| TC-FA-GRP-974 | E2E | TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | FE+BE |
| TC-FA-GRP-975 | E2E | TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | FE+BE |
| TC-FA-GRP-976 | E2E | TC-FA-GRP-E2E-045-new-subgroup-parent-sesuai-node-aksi-dan-tombol-group-saat-node-dipilih | FE+BE |
| TC-FA-GRP-977 | E2E | TC-FA-GRP-E2E-045-new-subgroup-parent-sesuai-node-aksi-dan-tombol-group-saat-node-dipilih | FE+BE |
| TC-FA-GRP-978 | E2E | TC-FA-GRP-E2E-055-edit-group-tanpa-perubahan-no-op-revert-ke-nilai-awal-dan-dialog-unsaved | FE+BE |
| TC-FA-GRP-979 | E2E | TC-FA-GRP-E2E-059-edit-function-tanpa-inheritance-dan-dialog-change-function-setelah-validasi-lolos | FE+BE |
| TC-FA-GRP-980 | E2E | TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver | FE+BE |
| TC-FA-GRP-981 | E2E | TC-FA-GRP-E2E-087-bulk-delete-parent-dan-descendant-tidak-sama-sama-terpilih-dan-satu-group-identik-single | FE+BE |
| TC-FA-GRP-982 | E2E | TC-FA-GRP-E2E-081-bulk-seleksi-persist-lintas-halaman-search-filter-dan-reset-saat-node-berganti | FE+BE |
| TC-FA-GRP-983 | E2E | TC-FA-GRP-E2E-089-android-delete-single-dan-bulk-delete-long-press-floating-bottom-bulk-bar | FE+BE |
| TC-FA-GRP-984 | E2E | TC-FA-GRP-E2E-089-android-delete-single-dan-bulk-delete-long-press-floating-bottom-bulk-bar | FE+BE |
| TC-FA-GRP-985 | E2E | TC-FA-GRP-E2E-014-android-guided-tooltip-drawer-dan-group-context-header-aktor-scoped | FE+BE |
| TC-FA-GRP-986 | E2E | TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | FE+BE |
| TC-FA-GRP-987 | E2E | TC-FA-GRP-E2E-027-tab-assets-detail-himpunan-aset-exact-match-status-badge-dan-nama-teks-biasa | FE+BE |
| TC-FA-GRP-988 | E2E | TC-FA-GRP-E2E-030-tab-users-detail-himpunan-union-total-user-non-aktif-dan-temporary-user | FE+BE |
| TC-FA-GRP-989 | E2E | TC-FA-GRP-E2E-281-wizard-log-ditulis-saat-diterapkan-di-t0-system-log-user-submit-terakhir-dan-siklus-downgrade-berikutnya | FE+BE |
| TC-FA-GRP-990 | E2E | TC-FA-GRP-E2E-281-wizard-log-ditulis-saat-diterapkan-di-t0-system-log-user-submit-terakhir-dan-siklus-downgrade-berikutnya | FE+BE |
| TC-FA-GRP-991 | E2E | TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | FE+BE |
| TC-FA-GRP-992 | E2E | TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | FE+BE |
| TC-FA-GRP-993 | E2E | TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | FE+BE |
| TC-FA-GRP-994 | E2E | TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | FE+BE |
| TC-FA-GRP-995 | E2E | TC-FA-GRP-E2E-210-state-tenant-suspended-expired-aksi-tulis-ditolak-403-dan-job-t0-tetap-berjalan | FE+BE |
| TC-FA-GRP-996 | E2E | TC-FA-GRP-E2E-210-state-tenant-suspended-expired-aksi-tulis-ditolak-403-dan-job-t0-tetap-berjalan | FE+BE |
| TC-FA-GRP-1004 | E2E | TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1005 | E2E | TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1006 | E2E | TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1007 | E2E | TC-FA-GRP-E2E-216-tab-assets-filter-asset-name-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1008 | E2E | TC-FA-GRP-E2E-217-tab-assets-filter-asset-name-chip-opsi-dan-kombinasi-asset-name-status | FE+BE |
| TC-FA-GRP-1009 | E2E | TC-FA-GRP-E2E-217-tab-assets-filter-asset-name-chip-opsi-dan-kombinasi-asset-name-status | FE+BE |
| TC-FA-GRP-1010 | E2E | TC-FA-GRP-E2E-217-tab-assets-filter-asset-name-chip-opsi-dan-kombinasi-asset-name-status | FE+BE |
| TC-FA-GRP-1011 | E2E | TC-FA-GRP-E2E-031-tab-users-detail-kolom-group-role-per-jenis-user-avatar-nama-dan-realtime-assignment | FE+BE |
| TC-FA-GRP-1012 | E2E | TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status | FE+BE |
| TC-FA-GRP-1013 | E2E | TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown | FE+BE |
| TC-FA-GRP-1014 | E2E | TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown | FE+BE |
| TC-FA-GRP-1015 | E2E | TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown | FE+BE |
| TC-FA-GRP-1016 | E2E | TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-1017 | E2E | TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | FE+BE |
| TC-FA-GRP-1018 | E2E | TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | FE+BE |
| TC-FA-GRP-1019 | E2E | TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | FE+BE |
| TC-FA-GRP-1020 | E2E | TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | FE+BE |
| TC-FA-GRP-1021 | E2E | TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | FE+BE |
| TC-FA-GRP-1022 | E2E | TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | FE+BE |
| TC-FA-GRP-1023 | E2E | TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-1024 | E2E | TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-1025 | E2E | TC-FA-GRP-E2E-059-edit-function-tanpa-inheritance-dan-dialog-change-function-setelah-validasi-lolos | FE+BE |
| TC-FA-GRP-1026 | E2E | TC-FA-GRP-E2E-205-group-hasil-import-edit-delete-tanpa-auto-assign-creator-dan-nama-reserved-ditolak | FE+BE |
| TC-FA-GRP-1027 | E2E | TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1028 | E2E | TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1029 | E2E | TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1030 | E2E | TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1031 | E2E | TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1032 | E2E | TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | FE+BE |
| TC-FA-GRP-1033 | E2E | TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning | FE+BE |
| TC-FA-GRP-1034 | E2E | TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | FE+BE |
| TC-FA-GRP-1035 | E2E | TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | FE+BE |
| TC-FA-GRP-1036 | E2E | TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | FE+BE |
| TC-FA-GRP-1037 | E2E | TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | FE+BE |
| TC-FA-GRP-1038 | E2E | TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | FE+BE |
| TC-FA-GRP-1039 | E2E | TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | FE+BE |
| TC-FA-GRP-1040 | E2E | TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | FE+BE |
| TC-FA-GRP-1041 | E2E | TC-FA-GRP-E2E-097-wizard-filter-total-asset-total-user-chip-opsi-dan-penerapan-ke-tabel | FE+BE |
| TC-FA-GRP-1042 | E2E | TC-FA-GRP-E2E-097-wizard-filter-total-asset-total-user-chip-opsi-dan-penerapan-ke-tabel | FE+BE |
| TC-FA-GRP-1043 | E2E | TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan | FE+BE |
| TC-FA-GRP-1044 | E2E | TC-FA-GRP-E2E-095-wizard-sort-default-sort-kolom-dan-search-nama-angka-centang-dipertahankan | FE+BE |
| TC-FA-GRP-1045 | E2E | TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi | FE+BE |
| TC-FA-GRP-1046 | E2E | TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi | FE+BE |
| TC-FA-GRP-1047 | E2E | TC-FA-GRP-E2E-232-tab-assets-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-1048 | E2E | TC-FA-GRP-E2E-232-tab-assets-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-1051 | E2E | TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | FE+BE |
| TC-FA-GRP-1052 | E2E | TC-FA-GRP-E2E-032-popup-detail-group-state-search-filter-sort-paginasi-per-tab-dipulihkan-dan-direset | FE+BE |
| TC-FA-GRP-1053 | E2E | TC-FA-GRP-E2E-032-popup-detail-group-state-search-filter-sort-paginasi-per-tab-dipulihkan-dan-direset | FE+BE |
| TC-FA-GRP-1054 | E2E | TC-FA-GRP-E2E-032-popup-detail-group-state-search-filter-sort-paginasi-per-tab-dipulihkan-dan-direset | FE+BE |
| TC-FA-GRP-1055 | E2E | TC-FA-GRP-E2E-035-new-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-1056 | E2E | TC-FA-GRP-E2E-048-new-subgroup-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-1057 | E2E | TC-FA-GRP-E2E-062-edit-group-validasi-group-name-reserved-emoji-auto-trim-dan-hanya-spasi | FE+BE |
| TC-FA-GRP-1058 | E2E | TC-FA-GRP-E2E-077-delete-diblok-scope-aktor-scoped-jadi-kosong-dan-guard-scope-efektif | FE+BE |
| TC-FA-GRP-1059 | E2E | TC-FA-GRP-E2E-073-delete-tanpa-warning-user-tc-ro-du-home-group-non-aktif-dan-transaction-role-approver | FE+BE |
| TC-FA-GRP-1060 | E2E | TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | FE+BE |
| TC-FA-GRP-1061 | E2E | TC-FA-GRP-E2E-189-tab-users-setup-column-pin-kolom-custom-field-dan-sel-tanpa-nilai-tampil-dash | FE+BE |
| TC-FA-GRP-1062 | E2E | TC-FA-GRP-E2E-019-aktor-scoped-variasi-scope-guided-tooltip-all-groups-level-1-empty-dan-union-scope | FE+BE |
| TC-FA-GRP-1063 | E2E | TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | FE+BE |
| TC-FA-GRP-1064 | E2E | TC-FA-GRP-E2E-070-code-auto-generate-dedup-tier-1-tier-2-batas-truncate-dan-case-insensitive | FE+BE |
| TC-FA-GRP-1065 | E2E | TC-FA-GRP-E2E-282-wizard-pagination-default-page-size-navigasi-dan-centang-lintas-halaman | FE+BE |
| TC-FA-GRP-1066 | E2E | TC-FA-GRP-E2E-282-wizard-pagination-default-page-size-navigasi-dan-centang-lintas-halaman | FE+BE |
| TC-FA-GRP-1067 | E2E | TC-FA-GRP-E2E-213-tab-assets-search-per-kolom-brand-model-type-dan-category | FE+BE |
| TC-FA-GRP-1068 | E2E | TC-FA-GRP-E2E-213-tab-assets-search-per-kolom-brand-model-type-dan-category | FE+BE |
| TC-FA-GRP-1069 | E2E | TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1070 | E2E | TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1071 | E2E | TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1072 | E2E | TC-FA-GRP-E2E-233-tab-assets-filter-brand-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1073 | E2E | TC-FA-GRP-E2E-234-tab-assets-filter-brand-chip-opsi-dan-kombinasi-brand-status | FE+BE |
| TC-FA-GRP-1074 | E2E | TC-FA-GRP-E2E-234-tab-assets-filter-brand-chip-opsi-dan-kombinasi-brand-status | FE+BE |
| TC-FA-GRP-1075 | E2E | TC-FA-GRP-E2E-234-tab-assets-filter-brand-chip-opsi-dan-kombinasi-brand-status | FE+BE |
| TC-FA-GRP-1076 | E2E | TC-FA-GRP-E2E-237-tab-assets-sort-brand-model-type-dan-tampilan-badge-dark-truncation-hover | FE+BE |
| TC-FA-GRP-1077 | E2E | TC-FA-GRP-E2E-237-tab-assets-sort-brand-model-type-dan-tampilan-badge-dark-truncation-hover | FE+BE |
| TC-FA-GRP-1078 | E2E | TC-FA-GRP-E2E-227-tab-assets-setup-column-pin-last-updated-dan-uncheck-kolom-brand-model-type | FE+BE |
| TC-FA-GRP-1079 | E2E | TC-FA-GRP-E2E-227-tab-assets-setup-column-pin-last-updated-dan-uncheck-kolom-brand-model-type | FE+BE |
| TC-FA-GRP-1080 | E2E | TC-FA-GRP-E2E-228-tab-assets-setup-column-geser-drag-brand-model-type-dan-pin-brand | FE+BE |
| TC-FA-GRP-1081 | E2E | TC-FA-GRP-E2E-228-tab-assets-setup-column-geser-drag-brand-model-type-dan-pin-brand | FE+BE |
| TC-FA-GRP-1082 | E2E | TC-FA-GRP-E2E-228-tab-assets-setup-column-geser-drag-brand-model-type-dan-pin-brand | FE+BE |
| TC-FA-GRP-1083 | E2E | TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge | FE+BE |
| TC-FA-GRP-1084 | E2E | TC-FA-GRP-E2E-237-tab-assets-sort-brand-model-type-dan-tampilan-badge-dark-truncation-hover | FE+BE |
| TC-FA-GRP-1085 | E2E | TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | FE+BE |
| TC-FA-GRP-1086 | E2E | TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | FE+BE |
| TC-FA-GRP-1087 | E2E | TC-FA-GRP-E2E-118-groups-list-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-1088 | E2E | TC-FA-GRP-E2E-147-modal-changelog-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-1089 | E2E | TC-FA-GRP-E2E-178-tab-users-setup-column-screening-overlay-popup-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-1090 | E2E | TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | FE+BE |
| TC-FA-GRP-1091 | E2E | TC-FA-GRP-E2E-179-tab-users-setup-column-batas-max-visible-columns-reset-esc-dan-cache | FE+BE |
| TC-FA-GRP-1092 | E2E | TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | FE+BE |
| TC-FA-GRP-1093 | E2E | TC-FA-GRP-E2E-006-sidebar-group-tree-toggle-open-collapse-persisten-responsif-dan-label-panjang | FE+BE |
| TC-FA-GRP-1094 | E2E | TC-FA-GRP-E2E-013-guided-tooltip-groups-navigasi-keluar-resize-viewport-dan-keyboard | FE+BE |
| TC-FA-GRP-1095 | E2E | TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | FE+BE |
| TC-FA-GRP-1096 | E2E | TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir | FE+BE |
| TC-FA-GRP-1097 | E2E | TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir | FE+BE |
| TC-FA-GRP-1098 | E2E | TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | FE+BE |
| TC-FA-GRP-1099 | E2E | TC-FA-GRP-E2E-100-wizard-setup-column-geser-drag-dan-pin-kolom | FE+BE |
| TC-FA-GRP-1100 | E2E | TC-FA-GRP-E2E-100-wizard-setup-column-geser-drag-dan-pin-kolom | FE+BE |
| TC-FA-GRP-1101 | E2E | TC-FA-GRP-E2E-098-wizard-setup-column-screening-overlay-popup-dan-guard-kolom-terakhir | FE+BE |
| TC-FA-GRP-1102 | E2E | TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | FE+BE |
| TC-FA-GRP-1103 | E2E | TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | FE+BE |
| TC-FA-GRP-1104 | E2E | TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | FE+BE |
| TC-FA-GRP-1105 | E2E | TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-1106 | E2E | TC-FA-GRP-E2E-171-tab-users-filter-custom-field-multi-dropdown-date-dan-kombinasi-and | FE+BE |
| TC-FA-GRP-1107 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-1108 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-1109 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-1110 | E2E | TC-FA-GRP-E2E-102-alert-group-consolidation-popup-choose-groups-save-selection-cancel-dan-counter | FE+BE |
| TC-FA-GRP-1111 | E2E | TC-FA-GRP-E2E-102-alert-group-consolidation-popup-choose-groups-save-selection-cancel-dan-counter | FE+BE |
| TC-FA-GRP-1114 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-1115 | E2E | TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | FE+BE |
| TC-FA-GRP-1116 | E2E | TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | FE+BE |
| TC-FA-GRP-1117 | E2E | TC-FA-GRP-E2E-102-alert-group-consolidation-popup-choose-groups-save-selection-cancel-dan-counter | FE+BE |
| TC-FA-GRP-1118 | E2E | TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator | FE+BE |
| TC-FA-GRP-1119 | E2E | TC-FA-GRP-E2E-283-modal-changelog-filter-tetap-berlaku-saat-kolom-action-di-hide | FE+BE |
| TC-FA-GRP-1120 | E2E | TC-FA-GRP-E2E-172-tab-users-filter-clear-field-irisan-search-filter-dan-filter-tetap-tersedia-saat-kolom-hide | FE+BE |
| TC-FA-GRP-1121 | E2E | TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | FE+BE |
| TC-FA-GRP-1122 | E2E | TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | FE+BE |
| TC-FA-GRP-1123 | E2E | TC-FA-GRP-E2E-023-role-matrix-gating-checkbox-bulk-aktor-d-parsial-dan-tanpa-d | FE+BE |
| TC-FA-GRP-1124 | E2E | TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | FE+BE |
| TC-FA-GRP-1125 | E2E | TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | FE+BE |
| TC-FA-GRP-1126 | E2E | TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | FE+BE |
| TC-FA-GRP-1127 | E2E | TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | FE+BE |
| TC-FA-GRP-1128 | E2E | TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | FE+BE |
| TC-FA-GRP-1129 | E2E | TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | FE+BE |
| TC-FA-GRP-1130 | E2E | TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator | FE+BE |
| TC-FA-GRP-1131 | E2E | TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator | FE+BE |
| TC-FA-GRP-1132 | E2E | TC-FA-GRP-E2E-117-groups-list-sort-kolom-total-user-modified-by-last-updated-guard-non-sortable-dan-tie-breaker | FE+BE |
| TC-FA-GRP-1133 | E2E | TC-FA-GRP-E2E-128-groups-list-download-isi-berkas-csv-xlsx-nilai-sel-tipe-data-bom-dan-escaping | FE+BE |
| TC-FA-GRP-1134 | E2E | TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi | FE+BE |
| TC-FA-GRP-1135 | E2E | TC-FA-GRP-E2E-173-tab-users-filter-menutup-panel-membuang-draft-dan-opsi-tanpa-nilai-kosong | FE+BE |
| TC-FA-GRP-1136 | E2E | TC-FA-GRP-E2E-173-tab-users-filter-menutup-panel-membuang-draft-dan-opsi-tanpa-nilai-kosong | FE+BE |
| TC-FA-GRP-1137 | E2E | TC-FA-GRP-E2E-176-tab-users-sort-kolom-tag-custom-field-dan-nilai-kosong-tie-breaker | FE+BE |
| TC-FA-GRP-1138 | E2E | TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | FE+BE |
| TC-FA-GRP-1139 | E2E | TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi | FE+BE |
| TC-FA-GRP-1140 | E2E | TC-FA-GRP-E2E-238-tab-assets-status-multi-badge-sort-filter-dan-search-label-badge-pertama | FE+BE |
| TC-FA-GRP-1141 | E2E | TC-FA-GRP-E2E-238-tab-assets-status-multi-badge-sort-filter-dan-search-label-badge-pertama | FE+BE |
| TC-FA-GRP-1142 | E2E | TC-FA-GRP-E2E-238-tab-assets-status-multi-badge-sort-filter-dan-search-label-badge-pertama | FE+BE |
| TC-FA-GRP-1143 | E2E | TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement | FE+BE |
| TC-FA-GRP-1144 | E2E | TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | FE+BE |
| TC-FA-GRP-1145 | E2E | TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | FE+BE |
| TC-FA-GRP-1146 | E2E | TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | FE+BE |
| TC-FA-GRP-1147 | E2E | TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | FE+BE |
| TC-FA-GRP-1148 | E2E | TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | FE+BE |
| TC-FA-GRP-1149 | E2E | TC-FA-GRP-E2E-210-state-tenant-suspended-expired-aksi-tulis-ditolak-403-dan-job-t0-tetap-berjalan | FE+BE |
| TC-FA-GRP-1150 | E2E | TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1151 | E2E | TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1152 | E2E | TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1153 | E2E | TC-FA-GRP-E2E-235-tab-assets-filter-model-type-isi-opsi-satu-dua-opsi-or-dan-search-dropdown | FE+BE |
| TC-FA-GRP-1154 | E2E | TC-FA-GRP-E2E-236-tab-assets-filter-model-type-chip-opsi-dan-kombinasi-model-type-status | FE+BE |
| TC-FA-GRP-1155 | E2E | TC-FA-GRP-E2E-236-tab-assets-filter-model-type-chip-opsi-dan-kombinasi-model-type-status | FE+BE |
| TC-FA-GRP-1156 | E2E | TC-FA-GRP-E2E-236-tab-assets-filter-model-type-chip-opsi-dan-kombinasi-model-type-status | FE+BE |
| TC-FA-GRP-1157 | E2E | TC-FA-GRP-E2E-213-tab-assets-search-per-kolom-brand-model-type-dan-category | FE+BE |
| TC-FA-GRP-1158 | E2E | TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | FE+BE |
| TC-FA-GRP-1159 | E2E | TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | FE+BE |
| TC-FA-GRP-1160 | E2E | TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | FE+BE |
| TC-FA-GRP-1161 | E2E | TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | FE+BE |
| TC-FA-GRP-1162 | E2E | TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status | FE+BE |
| TC-FA-GRP-1163 | E2E | TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status | FE+BE |
| TC-FA-GRP-1164 | E2E | TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status | FE+BE |
| TC-FA-GRP-1165 | E2E | TC-FA-GRP-E2E-242-tab-assets-category-sort-dan-setup-column-centang-serta-geser | FE+BE |
| TC-FA-GRP-1166 | E2E | TC-FA-GRP-E2E-242-tab-assets-category-sort-dan-setup-column-centang-serta-geser | FE+BE |
| TC-FA-GRP-1167 | E2E | TC-FA-GRP-E2E-242-tab-assets-category-sort-dan-setup-column-centang-serta-geser | FE+BE |
| TC-FA-GRP-1168 | E2E | TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge | FE+BE |
| TC-FA-GRP-1169 | E2E | TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge | FE+BE |
| TC-FA-GRP-1170 | E2E | TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi | FE+BE |
| TC-FA-GRP-1171 | E2E | TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi | FE+BE |
| TC-FA-GRP-1172 | E2E | TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi | FE+BE |
| TC-FA-GRP-1173 | E2E | TC-FA-GRP-E2E-243-tab-assets-filter-label-search-isi-opsi-satu-dan-dua-opsi | FE+BE |
| TC-FA-GRP-1174 | E2E | TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | FE+BE |
| TC-FA-GRP-1175 | E2E | TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | FE+BE |
| TC-FA-GRP-1176 | E2E | TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | FE+BE |
| TC-FA-GRP-1177 | E2E | TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | FE+BE |
| TC-FA-GRP-1178 | E2E | TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | FE+BE |
| TC-FA-GRP-1179 | E2E | TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | FE+BE |
| TC-FA-GRP-1180 | E2E | TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | FE+BE |
| TC-FA-GRP-1181 | E2E | TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | FE+BE |
| TC-FA-GRP-1182 | E2E | TC-FA-GRP-E2E-246-tab-assets-label-tampilan-chip-popover-labels-dan-kolom-curated-tersembunyi-default | FE+BE |
| TC-FA-GRP-1183 | E2E | TC-FA-GRP-E2E-246-tab-assets-label-tampilan-chip-popover-labels-dan-kolom-curated-tersembunyi-default | FE+BE |
| TC-FA-GRP-1184 | E2E | TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement | FE+BE |
| TC-FA-GRP-1185 | E2E | TC-FA-GRP-E2E-246-tab-assets-label-tampilan-chip-popover-labels-dan-kolom-curated-tersembunyi-default | FE+BE |
| TC-FA-GRP-1186 | E2E | TC-FA-GRP-E2E-231-tab-assets-download-isi-berkas-tipe-badge-date-empty-brand-model-type-dan-category-hierarki | FE+BE |
| TC-FA-GRP-1187 | E2E | TC-FA-GRP-E2E-241-tab-assets-filter-category-centang-parent-turunan-dan-cancel-tree-picker | FE+BE |
| TC-FA-GRP-1188 | E2E | TC-FA-GRP-E2E-241-tab-assets-filter-category-centang-parent-turunan-dan-cancel-tree-picker | FE+BE |
| TC-FA-GRP-1189 | E2E | TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive | FE+BE |
| TC-FA-GRP-1190 | E2E | TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku | FE+BE |
| TC-FA-GRP-1191 | E2E | TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | FE+BE |
| TC-FA-GRP-1192 | E2E | TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | FE+BE |
| TC-FA-GRP-1193 | E2E | TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | FE+BE |
| TC-FA-GRP-1194 | E2E | TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | FE+BE |
| TC-FA-GRP-1195 | E2E | TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement | FE+BE |
| TC-FA-GRP-1196 | E2E | TC-FA-GRP-E2E-251-tab-assets-kolom-tag-setup-column-dan-search-label-aksesibilitas-ikon | FE+BE |
| TC-FA-GRP-1197 | E2E | TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | FE+BE |
| TC-FA-GRP-1198 | E2E | TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | FE+BE |
| TC-FA-GRP-1199 | E2E | TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | FE+BE |
| TC-FA-GRP-1200 | E2E | TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | FE+BE |
| TC-FA-GRP-1201 | E2E | TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy | FE+BE |
| TC-FA-GRP-1202 | E2E | TC-FA-GRP-E2E-247-tab-assets-download-isi-berkas-kolom-multi-badge-label-tag-dan-measurement | FE+BE |
| TC-FA-GRP-1203 | E2E | TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy | FE+BE |
| TC-FA-GRP-1204 | E2E | TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | FE+BE |
| TC-FA-GRP-1205 | E2E | TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | FE+BE |
| TC-FA-GRP-1206 | E2E | TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | FE+BE |
| TC-FA-GRP-1207 | E2E | TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku | FE+BE |
| TC-FA-GRP-1208 | E2E | TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | FE+BE |
| TC-FA-GRP-1209 | E2E | TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | FE+BE |
| TC-FA-GRP-1210 | E2E | TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | FE+BE |
| TC-FA-GRP-1211 | E2E | TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | FE+BE |
| TC-FA-GRP-1212 | E2E | TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku | FE+BE |
| TC-FA-GRP-1213 | E2E | TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | FE+BE |
| TC-FA-GRP-1214 | E2E | TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting | FE+BE |
| TC-FA-GRP-1215 | E2E | TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting | FE+BE |
| TC-FA-GRP-1216 | E2E | TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting | FE+BE |
| TC-FA-GRP-1217 | E2E | TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang | FE+BE |
| TC-FA-GRP-1218 | E2E | TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang | FE+BE |
| TC-FA-GRP-1219 | E2E | TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang | FE+BE |
| TC-FA-GRP-1220 | E2E | TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | FE+BE |
| TC-FA-GRP-1221 | E2E | TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku | FE+BE |
| TC-FA-GRP-1222 | E2E | TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses | FE+BE |
| TC-FA-GRP-1223 | E2E | TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses | FE+BE |
| TC-FA-GRP-1224 | E2E | TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses | FE+BE |
| TC-FA-GRP-1225 | E2E | TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | FE+BE |
| TC-FA-GRP-1226 | E2E | TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | FE+BE |
| TC-FA-GRP-1227 | E2E | TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | FE+BE |
| TC-FA-GRP-1228 | E2E | TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | FE+BE |
| TC-FA-GRP-1229 | E2E | TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | FE+BE |
| TC-FA-GRP-1230 | E2E | TC-FA-GRP-E2E-266-tab-assets-custom-field-nilai-per-data-type-value-type-global-dan-hak-purchasing | FE+BE |
| TC-FA-GRP-1231 | E2E | TC-FA-GRP-E2E-266-tab-assets-custom-field-nilai-per-data-type-value-type-global-dan-hak-purchasing | FE+BE |
| TC-FA-GRP-1232 | E2E | TC-FA-GRP-E2E-266-tab-assets-custom-field-nilai-per-data-type-value-type-global-dan-hak-purchasing | FE+BE |
| TC-FA-GRP-1233 | E2E | TC-FA-GRP-E2E-267-tab-assets-custom-field-accounting-client-wide-dan-dash-mengalahkan-no-access | FE+BE |
| TC-FA-GRP-1234 | E2E | TC-FA-GRP-E2E-269-tab-assets-custom-field-search-sort-teks-tanggal-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-1235 | E2E | TC-FA-GRP-E2E-269-tab-assets-custom-field-search-sort-teks-tanggal-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-1236 | E2E | TC-FA-GRP-E2E-269-tab-assets-custom-field-search-sort-teks-tanggal-dan-kolom-di-hide | FE+BE |
| TC-FA-GRP-1237 | E2E | TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | FE+BE |
| TC-FA-GRP-1238 | E2E | TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive | FE+BE |
| TC-FA-GRP-1239 | E2E | TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive | FE+BE |
| TC-FA-GRP-1240 | E2E | TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor | FE+BE |
| TC-FA-GRP-1241 | E2E | TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor | FE+BE |
| TC-FA-GRP-1242 | E2E | TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor | FE+BE |
| TC-FA-GRP-1243 | E2E | TC-FA-GRP-E2E-273-tab-assets-ketersediaan-kolom-setup-column-per-hak-aktor | FE+BE |
| TC-FA-GRP-1244 | E2E | TC-FA-GRP-E2E-275-tab-assets-gerbang-no-access-sort-filter-dan-search-aktor-tanpa-hak-bergerbang | FE+BE |
| TC-FA-GRP-1245 | E2E | TC-FA-GRP-E2E-275-tab-assets-gerbang-no-access-sort-filter-dan-search-aktor-tanpa-hak-bergerbang | FE+BE |
| TC-FA-GRP-1246 | E2E | TC-FA-GRP-E2E-275-tab-assets-gerbang-no-access-sort-filter-dan-search-aktor-tanpa-hak-bergerbang | FE+BE |
| TC-FA-GRP-1247 | E2E | TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | FE+BE |
| TC-FA-GRP-1248 | E2E | TC-FA-GRP-E2E-276-tab-assets-gerbang-search-non-searchable-asset-id-tidak-filterable-dan-filter-asset-id | FE+BE |
| TC-FA-GRP-1249 | E2E | TC-FA-GRP-E2E-209-defense-in-depth-bypass-api-wizard-download-excess-delete-guard-isolasi-client-dan-markup | FE+BE |
| TC-FA-GRP-1250 | E2E | TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | FE+BE |
| TC-FA-GRP-1251 | E2E | TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | FE+BE |
| TC-FA-GRP-1252 | E2E | TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | FE+BE |
| TC-FA-GRP-1253 | E2E | TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | FE+BE |
| TC-FA-GRP-1254 | E2E | TC-FA-GRP-E2E-251-tab-assets-kolom-tag-setup-column-dan-search-label-aksesibilitas-ikon | FE+BE |
| TC-FA-GRP-1255 | E2E | TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy | FE+BE |
| TC-FA-GRP-1256 | E2E | TC-FA-GRP-E2E-260-tab-assets-hak-sel-bergerbang-tier-total-control-dan-default-user | FE+BE |
| TC-FA-GRP-1257 | E2E | TC-FA-GRP-E2E-260-tab-assets-hak-sel-bergerbang-tier-total-control-dan-default-user | FE+BE |
| TC-FA-GRP-1258 | E2E | TC-FA-GRP-E2E-261-tab-assets-hak-sel-bergerbang-tier-read-only-dan-group-manager | FE+BE |
| TC-FA-GRP-1259 | E2E | TC-FA-GRP-E2E-261-tab-assets-hak-sel-bergerbang-tier-read-only-dan-group-manager | FE+BE |
| TC-FA-GRP-1260 | E2E | TC-FA-GRP-E2E-267-tab-assets-custom-field-accounting-client-wide-dan-dash-mengalahkan-no-access | FE+BE |
| TC-FA-GRP-1261 | E2E | TC-FA-GRP-E2E-268-tab-assets-custom-field-accounting-pada-lisensi-fa-7-grace-period-dan-tidak-aktif | FE+BE |
| TC-FA-GRP-1262 | E2E | TC-FA-GRP-E2E-268-tab-assets-custom-field-accounting-pada-lisensi-fa-7-grace-period-dan-tidak-aktif | FE+BE |
| TC-FA-GRP-1263 | E2E | TC-FA-GRP-E2E-276-tab-assets-gerbang-search-non-searchable-asset-id-tidak-filterable-dan-filter-asset-id | FE+BE |
| TC-FA-GRP-1264 | E2E | TC-FA-GRP-E2E-276-tab-assets-gerbang-search-non-searchable-asset-id-tidak-filterable-dan-filter-asset-id | FE+BE |
| TC-FA-GRP-1265 | E2E | TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku | FE+BE |
| TC-FA-GRP-1266 | E2E | TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match | FE+BE |
| TC-FA-GRP-1267 | E2E | TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match | FE+BE |
| TC-FA-GRP-1268 | E2E | TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match | FE+BE |
| TC-FA-GRP-1269 | E2E | TC-FA-GRP-E2E-270-tab-assets-custom-field-search-dropdown-numeric-email-dan-date-tidak-match | FE+BE |
| TC-FA-GRP-1270 | E2E | TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range | FE+BE |
| TC-FA-GRP-1271 | E2E | TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range | FE+BE |
| TC-FA-GRP-1272 | E2E | TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range | FE+BE |
| TC-FA-GRP-1273 | E2E | TC-FA-GRP-E2E-271-tab-assets-custom-field-filter-dropdown-multi-dropdown-date-dan-numeric-range | FE+BE |
| TC-FA-GRP-1274 | E2E | TC-FA-GRP-E2E-272-tab-assets-custom-field-filter-tipe-tanpa-filter-formula-dan-filter-pada-kolom-bergerbang | FE+BE |
| TC-FA-GRP-1275 | E2E | TC-FA-GRP-E2E-272-tab-assets-custom-field-filter-tipe-tanpa-filter-formula-dan-filter-pada-kolom-bergerbang | FE+BE |
| TC-FA-GRP-1276 | E2E | TC-FA-GRP-E2E-272-tab-assets-custom-field-filter-tipe-tanpa-filter-formula-dan-filter-pada-kolom-bergerbang | FE+BE |
| TC-FA-GRP-1277 | E2E | TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30 | FE+BE |
| TC-FA-GRP-1278 | E2E | TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30 | FE+BE |
| TC-FA-GRP-1279 | E2E | TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30 | FE+BE |
| TC-FA-GRP-1280 | E2E | TC-FA-GRP-E2E-264-tab-assets-warranty-expiry-penanda-warna-expired-hari-ini-dan-hari-ke-30 | FE+BE |
| TC-FA-GRP-1281 | E2E | TC-FA-GRP-E2E-265-tab-assets-warranty-expiry-penanda-warna-dash-no-access-time-zone-client-dan-tidak-memengaruhi-sort-filter-download | FE+BE |
| TC-FA-GRP-1282 | E2E | TC-FA-GRP-E2E-265-tab-assets-warranty-expiry-penanda-warna-dash-no-access-time-zone-client-dan-tidak-memengaruhi-sort-filter-download | FE+BE |
| TC-FA-GRP-1283 | E2E | TC-FA-GRP-E2E-265-tab-assets-warranty-expiry-penanda-warna-dash-no-access-time-zone-client-dan-tidak-memengaruhi-sort-filter-download | FE+BE |
| TC-FA-GRP-1284 | E2E | TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | FE+BE |
| TC-FA-GRP-1285 | E2E | TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku | FE+BE |
| TC-FA-GRP-1286 | E2E | TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | FE+BE |
| TC-FA-GRP-1287 | E2E | TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | FE+BE |
| TC-FA-GRP-1288 | E2E | TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | FE+BE |
| TC-FA-GRP-1289 | E2E | TC-FA-GRP-E2E-285-create-group-level-1-dan-subgroup-baris-pola-group-role-dan-transaction-role-tc-ro-serta-log-assign-home-group-constraint, TC-FA-GRP-E2E-288-absence-pola-group-role-tc-ro-tanpa-auto-revert-dan-tanpa-notifikasi-in-app-saat-create | FE+BE |
| TC-FA-GRP-1290 | E2E | TC-FA-GRP-E2E-286-delete-group-baris-pola-group-role-dan-transaction-role-tc-ro-terhapus-log-remove-per-baris | FE+BE |
| TC-FA-GRP-1291 | E2E | TC-FA-GRP-E2E-285-create-group-level-1-dan-subgroup-baris-pola-group-role-dan-transaction-role-tc-ro-serta-log-assign-home-group-constraint, TC-FA-GRP-E2E-288-absence-pola-group-role-tc-ro-tanpa-auto-revert-dan-tanpa-notifikasi-in-app-saat-create | FE+BE |
| TC-FA-GRP-1292 | E2E | TC-FA-GRP-E2E-287-group-hasil-import-baris-pola-group-role-dan-transaction-role-tc-ro-user-non-tc-ro-tidak-diturunkan, TC-FA-GRP-E2E-289-absence-import-group-pola-tanpa-notifikasi-in-app-dan-kegagalan-tulis-baris-pola-me-rollback-group | FE+BE |
| TC-FA-GRP-1293 | E2E | TC-FA-GRP-E2E-290-create-subgroup-di-bawah-node-penugasan-gm-baris-pola-gm-log-assign-dan-gm-bersarang-satu-set, TC-FA-GRP-E2E-292-absence-create-subgroup-dan-group-di-bawah-node-gm-tanpa-notifikasi-auto-revert-dan-entri-log-user-gm | FE+BE |
| TC-FA-GRP-1294 | E2E | TC-FA-GRP-E2E-291-create-subgroup-oleh-gm-sendiri-di-descendant-node-penugasan-baris-pola-gm-tetap-terbentuk-gm-lain-tidak-menerima, TC-FA-GRP-E2E-292-absence-create-subgroup-dan-group-di-bawah-node-gm-tanpa-notifikasi-auto-revert-dan-entri-log-user-gm | FE+BE |
| TC-FA-GRP-1295 | E2E | TC-FA-GRP-E2E-290-create-subgroup-di-bawah-node-penugasan-gm-baris-pola-gm-log-assign-dan-gm-bersarang-satu-set | FE+BE |
| TC-FA-GRP-1296 | E2E | TC-FA-GRP-E2E-292-absence-create-subgroup-dan-group-di-bawah-node-gm-tanpa-notifikasi-auto-revert-dan-entri-log-user-gm, TC-FA-GRP-E2E-298-create-group-level-1-tanpa-baris-pola-gm-dan-total-user-hanya-tc-du-ro | FE+BE |
| TC-FA-GRP-1297 | E2E | TC-FA-GRP-E2E-293-delete-node-penugasan-gm-penugasan-terlepas-baris-pola-terhapus-dan-log-remove-group-deleted-per-baris, TC-FA-GRP-E2E-294-absence-delete-node-gm-tanpa-notifikasi-in-app-tanpa-auto-revert-dan-changelog-group-hanya-delete | FE+BE |
| TC-FA-GRP-1298 | E2E | TC-FA-GRP-E2E-294-absence-delete-node-gm-tanpa-notifikasi-in-app-tanpa-auto-revert-dan-changelog-group-hanya-delete, TC-FA-GRP-E2E-300-delete-descendant-node-tercakup-gm-baris-pola-di-node-terhapus-saja-ancestor-gm-tidak-terpengaruh | FE+BE |
| TC-FA-GRP-1299 | E2E | TC-FA-GRP-E2E-295-total-user-node-descendant-memuat-user-gm-yang-penugasannya-mencakup-node-dihitung-distinct | FE+BE |
| TC-FA-GRP-1300 | E2E | TC-FA-GRP-E2E-296-group-hasil-import-di-bawah-node-tercakup-gm-baris-pola-gm-atomik-dan-group-level-1-tanpa-baris-pola, TC-FA-GRP-E2E-297-absence-import-group-di-bawah-node-gm-tanpa-notifikasi-tanpa-auto-revert-dan-kegagalan-tulis-baris-pola-me-rollback-group | FE+BE |
| TC-FA-GRP-1301 | E2E | TC-FA-GRP-E2E-301-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-baris-tetap-di-root-total-user-tidak-menghitung, TC-FA-GRP-E2E-302-absence-create-subgroup-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-FA-GRP-1302 | E2E | TC-FA-GRP-E2E-303-group-hasil-import-di-bawah-ancestor-ber-transaction-role-tanpa-baris-salinan-cakupan-ancestor-tetap, TC-FA-GRP-E2E-304-absence-import-group-di-bawah-ancestor-ber-transaction-role-tanpa-entri-assign-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-FA-GRP-1303 | E2E | TC-FA-GRP-E2E-305-delete-node-di-bawah-ancestor-ber-transaction-role-dialog-normal-penugasan-ancestor-tetap-subtree-terhapus, TC-FA-GRP-E2E-306-absence-delete-node-di-bawah-ancestor-ber-transaction-role-tanpa-entri-remove-dan-tanpa-notifikasi-in-app | FE+BE |
| TC-FA-GRP-1304 | E2E | TC-FA-GRP-E2E-307-delete-leaf-yang-hanya-tercakup-baris-pola-gm-ancestor-dialog-normal-bukan-d-15 | FE+BE |
| TC-FA-GRP-1305 | E2E | TC-FA-GRP-E2E-308-tab-assets-sel-asset-value-pending-tooltip-alasan-dan-prioritas | FE+BE |
| TC-FA-GRP-1306 | E2E | TC-FA-GRP-E2E-309-tab-assets-sel-asset-value-pending-search-filter-dan-download-dua-kolom | FE+BE |

---

## 4. Catatan Terbuka untuk Pemilik Script dan QA

Tabel dan daftar di atas dibangkitkan dari frontmatter spec; bagian ini ditulis tangan dan merangkum hal yang masih terbuka.

### 4.1 Env password baru dan fixture yang perlu didaftarkan pemilik

- Seluruh password akun aktor memakai nama env baru berpola `Spectra.env.FA_<ROLE>_PASSWORD` (default suite: `FA_TC_PASSWORD` untuk Total Control, dipakai di hampir semua spec). Env lain mencakup antara lain `FA_DU_PASSWORD`, `FA_RO_PASSWORD`, `FA_GM_PASSWORD`, `FA_GMSEED_PASSWORD`, `FA_MGCRUD_PASSWORD`, `FA_MGR_PASSWORD`, `FA_MGRC_PASSWORD`, `FA_MGRU_PASSWORD`, `FA_MGRD_PASSWORD`, `FA_MGNR_PASSWORD`, `FA_OTHER_PASSWORD`, varian per plan (`FA_STARTER_TC_PASSWORD`, `FA_GROWTH_TC_PASSWORD`, `FA_ENTERPRISE_TC_PASSWORD`, `FA_DOWNGRADE_TC_PASSWORD`), varian wizard dan alert (`FA_WIZ_TC_PASSWORD`, `FA_WIZ25_TC_PASSWORD`, `FA_ALERT_*_PASSWORD`), varian akses nilai aset (`FA_GRP_*_PASSWORD`), serta `FA_GRP_IMPORTER_PASSWORD` dan `FA_GRP_SUBJECT_PASSWORD`. Daftar lengkap dapat dicari dengan pola `Spectra.env.` pada seluruh `spec.md` suite.
- Semua nama env tersebut belum ada. Pemilik script wajib mendaftarkannya di `executionConfig.environmentVariables` dan `.env.example` sebelum spec dapat dijalankan.
- Email beberapa akun aktor (Group Manager seed, user kedua pembuat batch, akun client khusus) tidak tertulis di Pre-setup TC; spec memakai pola Pre-setup dan menandainya di Notes. Akun tersebut disediakan tim FE.
- Kemampuan teknis berikut disediakan tim FE/BE tanpa endpoint karangan: fixture BE (seeding dan pemulihan data, pembacaan state agregat, status Client, plan, limit platform, hook uji T-0, penulisan Activity Log yang disimulasikan gagal), sesi API aktor, klien HTTP, penyetelan flag Guided Tooltip, serta alamat URL halaman Settings > Groups.

- Spec 290 sampai 298 dan 300 (pola GM) memakai akun Pre-setup No 28 sampai 32 (`gmPattern`, `gmPatternNested`, `gmPatternOther`, `gmDelete`, `gmPatternAnc`, `delGmUser`) yang email nyatanya belum ditetapkan tim FE/QA, env baru `Spectra.env.FA_GRP_GMPATTERN_PASSWORD` (usulan, login gmPattern di spec 291 dan 292; perlu didaftarkan pemilik repo e2e), fixture `Fixture.groupsGmPattern.*` (berkas Import `importSub`, `importRoot`, `importAbsen`, `importGagal`), seeding penugasan GM dan baris pola GM yang sudah terbentuk, serta pemicu kegagalan penulisan baris pola GM (spec 297; mekanismenya tidak ada di TC, PRD, atau LLD). Pertanyaan TC-source terbuka yang dicatat di Notes: NC-12 (efek baris pola GM pada Total User dan guard Delete kondisi 5), nilai sel Group Role di Tab Users untuk GM, tampilan Jenis Transaksi Addon tak berlisensi di tab Transaction Role, dan salinan node Delete untuk spec absence (294).
- Spec 285 sampai 289 memakai fixture dan kemampuan baru yang disediakan tim FE/BE: user Total Control dan Read Only dengan Home Group constraint (`Fixture.groupsPola.tcHome.email`, `Fixture.groupsPola.roHome.email`), user Standard (`Fixture.groupsPola.standard.email`), berkas Import Group `Fixture.groupsImport.branchPola`, `branchAbsen`, dan `branchGagal`, pembacaan tab Group Role dan Transaction Role per node, pembacaan jumlah notifikasi in-app per penerima, dan pemicu kegagalan penulisan baris pola (spec 289; mekanismenya tidak ada di TC, PRD, atau LLD).

### 4.2 Hook suite yang belum lengkap

- Spec 017 (Role Matrix negatif menu Groups hidden): hook `beforeEach` suite membuka Settings > Groups, padahal server menolak halaman itu untuk role yang diuji. Hook perlu dilewati untuk spec ini atau dibiarkan menghasilkan penolakan; spec 017 membuka Fixed Asset > Dashboard pada langkah 1 dan menunggu toast penolakan hilang (R-12). Pemilik script perlu memutuskan cara melewati hook di spec.
- `suite.md` memuat hook `after` pemulihan preferensi Setup Column dan sidebar serta hook `beforeEach` pembuka halaman Groups. Spec Setup Column tetap membersihkan state masing-masing di `after` bila mengubah konfigurasi kolom.

### 4.3 Spec mobile

- Spec 014 (Guided Tooltip drawer dan Group Context Header aktor-scoped) dan spec 089 (Delete single dan Bulk Delete long press, Floating Bottom Bulk Bar) menguji aplikasi native Android TAG Samurai Mobile. Keduanya tidak memakai hook web suite dan memakai perangkat atau emulator Android bersama yang disediakan tim FE, sehingga `parallel: false` (S-09).

### 4.4 Spec dengan lebih dari 35 langkah (94 spec)

Seluruh spec ini menulis alasan di `## Notes`. Pola alasannya sama: satu kelas dan satu dataset, tiap blok berdiri sendiri, memisahkannya hanya menggandakan login, hook, dan cleanup tanpa alur baru, atau langkah banyak karena perulangan atas tabel Prerequisites (8b butir 7) dan `Verifikasi` per klausa Expected. Ringkasan teks Notes tiap spec (dipotong 300 karakter):

| Spec | Langkah | Alasan |
|---|:---:|---|
| TC-FA-GRP-E2E-001-screening-groups-list-all-groups-layout-kolom-format-sel-dan-hover | 47 | Spec melewati sekitar 35 langkah (47 langkah): seluruh blok adalah screening satu kelas pada layar dan dataset yang sama (Groups List All Groups), tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan cleanup tanpa alur baru. |
| TC-FA-GRP-E2E-004-empty-state-client-baru-seed-default-group-dan-changelog-kosong | 40 | Spec melewati sekitar 35 langkah (40 langkah): seluruh TC bergantung pada keadaan client baru yang sama (hanya Default Group, log kosong) yang hanya ada sekali per client, sehingga blok TC-FA-GRP-894 yang mengubah Default Group wajib berada paling akhir dan tidak dapat dipisah tanpa menyediakan … |
| TC-FA-GRP-E2E-005-sidebar-group-tree-screening-tooltip-urutan-az-node-excess-dan-aksesibilitas | 50 | Spec melewati sekitar 35 langkah (50 langkah): seluruh blok adalah satu kelas (sidebar Group Tree) pada dataset yang sama, tiap blok berdiri sendiri, dan memisahnya hanya menggandakan login, hook, dan cleanup tanpa alur baru. Blok TC-FA-GRP-967 yang mengubah data milik spec berada paling akhir … |
| TC-FA-GRP-E2E-011-refresh-f5-dan-sinkron-seleksi-node-terpilih-setelah-hapus-dan-klik-ulang-menu | 38 | Spec melewati sekitar 35 langkah (38 langkah): seluruh blok adalah satu kelas (sinkron seleksi node di Groups List) pada dataset milik spec, tiap blok berdiri sendiri, dan blok yang menghapus data (TC-FA-GRP-32 dan 33) berada paling |
| TC-FA-GRP-E2E-012-guided-tooltip-groups-konten-tiga-step-done-skip-dan-tombol-replay | 46 | Spec melewati sekitar 35 langkah (46 langkah): seluruh blok adalah satu kelas (Guided Tooltip halaman Groups) pada layar yang sama, tiap blok berdiri sendiri dengan flag diatur ulang di awal blok (langkah 1, 15, 25), dan perulangan [Next]-[Next]-[Done] tidak dapat diringkas karena tiap klik adalah … |
| TC-FA-GRP-E2E-020-role-matrix-positif-create-subgroup-dan-group-level-1-manage-group-rc-group-manager-default-user | 66 | Spec melewati sekitar 35 langkah (66 langkah): seluruh blok adalah satu kelas (Role Matrix positif Create) pada dataset Region West yang sama, tiap blok berdiri sendiri (satu role per blok, data dibuat dan dihapus sendiri), dan memisahkannya hanya menggandakan login, hook, dan |
| TC-FA-GRP-E2E-024-role-matrix-aksi-baris-descendant-baca-saja-dan-node-excess-per-role | 46 | Spec melewati sekitar 35 langkah (46 langkah): seluruh blok adalah satu kelas (Role Matrix aksi baris, hanya membaca menu dan popup tanpa aksi tulis) pada dataset Region West yang sama, tiap blok berdiri sendiri (satu role per blok), dan memisahkannya hanya menggandakan login, hook, dan |
| TC-FA-GRP-E2E-025-popup-detail-group-buka-via-nama-dan-row-action-screening-header-dan-node-excess | 38 | Spec melewati sekitar 35 langkah (38 langkah): seluruh blok adalah satu kelas (screening Popup Detail Group, hanya membaca) pada dataset Tabel A yang sama, tiap blok berdiri sendiri, dan memisahkannya hanya menggandakan login, hook, dan |
| TC-FA-GRP-E2E-026-popup-detail-group-tutup-esc-backdrop-refleksi-edit-tab-awal-dan-node-dihapus-404 | 52 | Spec melewati sekitar 35 langkah setelah ekspansi (langkah nominal 52; ekspansi 3 iterasi langkah 45 sampai 52 menjadi 24 langkah sehingga total ekspansi 68): seluruh blok adalah satu kelas (perilaku Popup Detail Group) pada layar dan dataset Tabel A yang sama, perulangan TC-FA-GRP-986 per node … |
| TC-FA-GRP-E2E-033-new-group-screening-popup-dan-create-level-1-happy-path-stay-on-form | 46 | Alasan spec melewati ~35 langkah (46 langkah): keempat TC satu kelas (fungsional Create Group level 1), satu dataset (Plan Professional dan pohon Pre-setup), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); selisih terbesar berasal dari `Verifikasi` per … |
| TC-FA-GRP-E2E-039-new-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | 42 | Alasan spec melewati ~35 langkah (42 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup New Group), satu dataset (tanpa data tulis), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok ditutup bersih sebelum blok … |
| TC-FA-GRP-E2E-043-konflik-dua-admin-create-tepat-di-cap-dan-re-check-atomik-saat-submit | 37 | Alasan spec melewati ~35 langkah (37 langkah): seluruh blok satu kelas (multi-konteks race pada plan gating Create), tiap blok berdiri sendiri (precondition dibangun ulang lewat langkah penghubung), dan langkah banyak karena `Verifikasi` per klausa Expected |
| TC-FA-GRP-E2E-046-new-subgroup-parent-excess-dan-parent-dihapus-saat-popup-terbuka | 41 | Alasan spec melewati ~35 langkah (41 langkah): keempat TC satu kelas (Create Subgroup pada parent Excess atau dihapus, kelas h state tenant), tiap blok berdiri sendiri (precondition dibangun ulang lewat langkah penghubung), dan langkah banyak karena `Verifikasi` per klausa Expected (S-01), terutama … |
| TC-FA-GRP-E2E-052-new-subgroup-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | 42 | Alasan spec melewati ~35 langkah (42 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup New Subgroup), satu dataset (tanpa data tulis), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok ditutup bersih sebelum blok … |
| TC-FA-GRP-E2E-053-edit-group-screening-popup-prefilled-dan-ubah-name-code-description-saja | 39 | Alasan spec melewati ~35 langkah (39 langkah): keempat TC satu kelas (fungsional Edit Group), satu dataset (node `Edit Target` milik spec), dan tiap blok berdiri sendiri; langkah banyak karena `Verifikasi` per klausa Expected (S-01) dan langkah penghubung membuka |
| TC-FA-GRP-E2E-066-edit-group-tutup-popup-tanpa-dan-dengan-perubahan-guard-browser-backdrop-dan-navigasi | 40 | Alasan spec melewati ~35 langkah (40 langkah): kelima TC satu kelas (UI tutup popup dan guard Unsaved changes pada Popup Edit Group), satu dataset (node `Edit Target` milik spec, tidak berubah), dan tiap blok berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna); blok … |
| TC-FA-GRP-E2E-072-delete-warning-user-ter-scope-descendant-dan-cancel-pada-dialog-warning | 36 | Spec melewati sekitar 35 langkah (36 langkah): seluruh blok satu topik Delete dengan dialog Warning pada dataset `Del Users` yang sama dan tiap blok berdiri sendiri; Expected c baru TC-FA-GRP-224 (baris pola GM ikut terhapus beserta penugasan GM) menambah empat langkah. |
| TC-FA-GRP-E2E-075-delete-diblok-aset-aktif-di-node-descendant-draft-dan-guard-pertama-menentukan | 40 | Spec berisi lebih dari 35 langkah (empat blok blokir). Alasan: seluruhnya satu kelas dan satu topik (Delete diblok kondisi data), tiap blok berdiri sendiri dan bergantung pada data berbeda, dan tiga blok baca-log berpola (buka Modal Changelog, Verifikasi jumlah, tutup) tidak dihitung menurut bagian … |
| TC-FA-GRP-E2E-076-delete-diblok-tujuan-transfer-belum-tuntas | 42 | Spec berisi lebih dari 35 langkah (tiga blok blokir). Alasan: seluruhnya satu kelas dan satu topik (Delete diblok transaksi belum tuntas), tiap blok berdiri sendiri dengan data transaksi berbeda, dan tiga blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13. |
| TC-FA-GRP-E2E-080-bulk-action-bar-screening-counter-checkbox-header-select-all-dan-unselect-all | 37 | Spec berisi lebih dari 35 langkah. Alasan: lima TC screening Bulk Action Bar satu topik, satu dataset, dan satu kelas (fungsional UI), tiap blok berdiri sendiri; semuanya satu dataset (bagian 3 prinsip |
| TC-FA-GRP-E2E-083-bulk-delete-dialog-homogen-satu-group-collapse-single-dan-cancel | 40 | Spec berisi lebih dari 35 langkah. Alasan: lima TC satu keluarga Bulk Delete homogen dengan dataset seed berbeda per TC, satu kelas (fungsional), tiap blok berdiri sendiri; blok baca-log berpola tidak dihitung (bagian 3 prinsip |
| TC-FA-GRP-E2E-091-wizard-submit-tepat-cap-diterapkan-di-t0-submit-setelah-t0-dan-submit-ulang-sebelum-t0 | 44 | Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, penerapan seleksi Wizard) pada satu dataset dan satu alur state; langkah penghubung seeding, pemicu T-0, dan baca-log berpola bukan asersi baru (bagian 3 prinsip 13, |
| TC-FA-GRP-E2E-092-wizard-fallback-t0-client-belum-submit-tie-break-seleksi-kosong-dan-plan-naik-kembali | 39 | Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, penerapan T-0 dan fallback) dan berdiri sendiri dengan state seed berbeda; sekitar 16 langkah adalah penghubung seeding, pemicu T-0, dan pembacaan log berpola, bukan asersi |
| TC-FA-GRP-E2E-093-wizard-t0-seleksi-tersimpan-dibuang-dipakai-dan-penerapan-satu-transaksi | 45 | Spec berisi lebih dari 35 langkah. Alasan: tujuh blok satu kelas (h, penerapan T-0 atas seleksi tersimpan) dan berdiri sendiri dengan state seed berbeda; sebagian besar langkah adalah penghubung seeding dan pemicu T-0, bukan asersi |
| TC-FA-GRP-E2E-094-wizard-cancel-unsaved-klik-total-asset-user-dan-server-menolak-seleksi-d-23 | 54 | Spec berisi lebih dari 35 langkah. Alasan: seluruh blok pada satu surface (step Group Consolidation) dan satu dataset; tiap blok berdiri sendiri; sebagian besar langkah adalah penghubung buka atau tutup step dan |
| TC-FA-GRP-E2E-096-wizard-search-interaksi-reveal-enter-clear-collapse-dan-filter-group-dropdown | 38 | Spec berisi lebih dari 35 langkah. Alasan: empat TC Search dan Filter pada satu surface dan satu dataset, tiap blok berdiri sendiri; TC-1037 memuat sembilan langkah interaksi siklus input yang tiap klausanya punya `Verifikasi` |
| TC-FA-GRP-E2E-099-wizard-setup-column-uncheck-reset-to-default-esc-dan-cache | 36 | Spec berisi lebih dari 35 langkah setelah ekspansi. Alasan: satu kelas dan satu surface (Setup Column Step Group Consolidation); iterasi per kolom sah menurut 8b butir 7 dan blok tiap TC berdiri sendiri; konfigurasi dipulihkan oleh langkah penghubung dan hook |
| TC-FA-GRP-E2E-101-alert-group-consolidation-pasca-t0-visibilitas-per-role-dan-entry-point | 39 | Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (h, visibilitas Alert Group Consolidation terhadap keadaan plan dan role) dan berdiri sendiri; sekitar 14 langkah adalah penghubung ganti akun, buka halaman, dan seeding keadaan, bukan asersi |
| TC-FA-GRP-E2E-103-alert-group-consolidation-popup-tutup-x-esc-backdrop-dan-unsaved-changes | 39 | Spec berisi lebih dari 35 langkah. Alasan: empat TC satu surface (popup Alert Group Consolidation) dan satu dataset, tiap blok berdiri sendiri dan menutup popup lewat jalur berbeda; `Verifikasi` dialog dan status dipecah per klausa |
| TC-FA-GRP-E2E-104-konflik-dua-admin-delete-group-terakhir-create-rename-sama-dan-kondisi-berubah-setelah-dialog | 60 | Spec berisi lebih dari 35 langkah. Alasan: seluruh blok satu kelas (c, konflik antar admin) dan berdiri sendiri; delapan skenario race pendek, sekitar 20 langkah adalah penghubung (ganti akun, buka halaman, pemicu pelaku kedua lewat API, tutup |
| TC-FA-GRP-E2E-105-groups-list-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-di-hide | 46 | Spec 46 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-110-groups-list-filter-tetap-tersedia-saat-kolom-hide-menutup-panel-membuang-draft-dan-indikator | 47 | Spec 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. |
| TC-FA-GRP-E2E-111-groups-list-filter-total-asset-dan-total-user-rentang-min-max | 47 | Spec 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-113-groups-list-filter-modified-by-chip-last-updated-rentang-dan-clear-field | 50 | Spec 50 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-115-groups-list-kombinasi-clear-search-ganti-sort-dan-pemulihan-dari-empty-state | 48 | Spec 48 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. |
| TC-FA-GRP-E2E-127-groups-list-download-fungsional-seluruh-data-search-filter-kolom-hide-header-saja-dan-aktor-scoped | 55 | Spec 55 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-130-groups-list-pagination-default-page-size-navigasi-dan-reset-ke-halaman-1-saat-search-filter | 38 | Spec 38 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-131-groups-list-mutasi-saat-terfilter-ter-search-dan-paginasi-kasus-tepi | 37 | Spec 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-132-modal-changelog-group-screening-baris-excess-aktor-scoped-dan-read-only | 47 | Spec 47 langkah (ekspansi iterasi ± 60 langkah), di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah per kolom/field memakai tabel di … |
| TC-FA-GRP-E2E-133-modal-changelog-search-interaksi-reveal-enter-clear-collapse-date-tidak-match-dan-kolom-hide | 47 | Spec 47 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-143-modal-changelog-kombinasi-search-filter-irisan-dan-search-filter-sort-pagination | 46 | Spec 46 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-144-modal-changelog-kombinasi-clear-filter-search-ganti-sort-dan-pemulihan-dari-empty-state | 44 | Spec 44 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-148-modal-changelog-setup-column-reset-esc-dan-cache-tidak-memengaruhi-tabel-lain | 36 | Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-158-modal-changelog-pagination-default-navigasi-dan-reset-ke-halaman-1-saat-search-filter | 36 | Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-159-modal-changelog-kolom-group-name-full-path-snapshot-rename-nama-kembar-dan-delete-cascade | 54 | Spec 54 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-161-tab-users-search-interaksi-reveal-enter-clear-collapse-temporary-until-email-dan-kolom-hide | 44 | Spec memiliki 44 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Search Tab Users pada dataset yang sama), tiap TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan TC-572 sendiri memuat 25 langkah karena satu TC menguji siklus input … |
| TC-FA-GRP-E2E-164-tab-users-kolom-group-role-multi-role-node-tier-filter-dan-search-teks-sel | 38 | Spec memiliki 38 langkah, di atas smell 35 langkah. Alasan: keempat TC memakai fixture Multi Role Node yang sama dan satu topik kolom Group Role Tab Users; fixture berat (lima user subjek) tidak perlu di-seed ulang, dan tiap blok berdiri |
| TC-FA-GRP-E2E-166-tab-users-filter-position-chip-dan-filter-division-opsi | 39 | Spec memiliki 39 langkah, di atas smell 35 langkah. Alasan: dua keluarga satu topik (chip opsi dan opsi Filter Tab Users pada dataset yang sama) tanpa pemisah kelas harness, dan tiap TC berdiri sendiri; TC-590 sendiri memuat 15 langkah karena Expected b memeriksa chip dan |
| TC-FA-GRP-E2E-167-tab-users-filter-division-search-dropdown-chip-dan-opsi | 37 | Spec memiliki 37 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Filter Division Tab Users pada dataset yang sama), tiap TC berdiri sendiri, dan TC-596 memuat 12 langkah karena Expected b memeriksa chip dan |
| TC-FA-GRP-E2E-169-tab-users-filter-group-role-chip-opsi-dan-activation-status | 41 | Spec memiliki 41 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Filter Tab Users pada dataset yang sama), tiap TC berdiri sendiri, dan TC-602 memuat 15 langkah karena Expected b memeriksa chip dan |
| TC-FA-GRP-E2E-170-tab-users-filter-temporary-user-temporary-until-dan-custom-field-dropdown | 41 | Spec 41 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-191-tab-users-download-isi-berkas-csv-xlsx-tipe-empty-badge-date-bom-dan-kolom-group-role | 36 | Spec memiliki 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu kelas harness (isi berkas Download Tab Users) dan tiap TC berdiri sendiri; TC-1147 memakai fixture Multi Role Node yang tidak dipakai TC lain di spec |
| TC-FA-GRP-E2E-192-tab-users-pagination-default-navigasi-reset-ke-halaman-1-dan-kasus-tepi | 39 | Spec memiliki 39 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (Pagination Tab Users pada dataset yang sama) dan tiap TC berdiri sendiri; TC-1045 menguji empat ukuran halaman yang masing-masing punya |
| TC-FA-GRP-E2E-194-log-create-level-1-subgroup-dan-import-isi-baris-changelog-system-log-activity-log | 48 | Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, |
| TC-FA-GRP-E2E-195-log-edit-name-code-description-function-isi-baris-changelog-system-log-activity-log | 60 | Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, |
| TC-FA-GRP-E2E-196-log-delete-single-bulk-dan-cascade-isi-baris-changelog-system-log-activity-log | 57 | Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, |
| TC-FA-GRP-E2E-198-log-marked-restored-excess-fallback-t0-plan-naik-dan-delete-isi-baris | 45 | Blok membaca log berpola (buka surface, cari entri, `Verifikasi` kolom log) tidak dihitung terhadap smell 35 langkah (bagian 3 prinsip 13). Langkah baseline dan pencarian baris adalah langkah penghubung (S-03, |
| TC-FA-GRP-E2E-199-log-multi-field-edit-snapshot-immutability-nama-terhapus-dan-modified-by-setelah-excess | 36 | Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-200-log-pencabutan-assignment-saat-delete-di-log-user-dan-tanpa-notifikasi-in-app | 45 | Spec melewati sekitar 35 langkah (45 langkah): dua blok satu topik (pencatatan pencabutan assignment saat Delete dan tanpa notifikasi in-app) dengan pola baca-log yang sama pada empat surface; tiap TC berdiri sendiri. |
| TC-FA-GRP-E2E-201-absence-log-edit-no-op-aksi-batal-dan-kegagalan-tulis-log-rollback | 41 | Spec 41 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-203-node-excess-di-dropdown-konsumen-import-ditolak-dan-transaksi-berjalan-tetap-selesai | 66 | Spec memiliki 66 langkah, di atas smell 35 langkah. Alasan: lima TC kelas sama (perilaku node Excess pada modul konsumen) dengan fixture bersama; tiap TC berdiri sendiri, dan TC-903, 992, dan 994 melintasi modul Transfer, Disposal, Assignment, Role & Permission, License, dan Reader. |
| TC-FA-GRP-E2E-204-post-create-edit-delete-tercermin-di-modul-konsumen-reader-group-home-group-dan-scope-role | 63 | Spec memiliki 63 langkah, di atas smell 35 langkah. Alasan: tujuh TC satu topik (propagasi perubahan group ke modul konsumen) dengan fixture terpisah per TC; tiap TC berdiri sendiri, dan banyak langkah berasal dari Expected yang memeriksa beberapa modul konsumen |
| TC-FA-GRP-E2E-207-sync-tab-assets-policy-transaksi-tag-last-scanned-dan-custom-field-berubah | 45 | Spec memiliki 45 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik (sinkronisasi lintas modul ke Tab Assets pada fixture Value Sync Node yang sama); tiap TC berdiri sendiri dan Expected memeriksa tiga keadaan (awal, sesudah perubahan, sesudah |
| TC-FA-GRP-E2E-211-tab-assets-search-interaksi-reveal-enter-clear-collapse-last-updated-dan-kolom-hide | 39 | Spec memuat 3 TC Search Tab Assets satu kelas harness tanpa harness eksternal; tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain. Jumlah langkah (39) di atas smell 35 langkah karena TC-677 sendiri memuat 8 klausa Expected (a sampai g) yang masing-masing … |
| TC-FA-GRP-E2E-214-tab-assets-filter-panel-screening-dan-filter-status-opsi-or-search-dropdown | 39 | Spec berisi 4 TC Filter Status dan screening Filter Panel dalam satu kelas harness dan satu dataset Warehouse A; tiap blok berdiri sendiri. Melewati sekitar 35 langkah karena TC-683 memuat 11+ field dengan tipe dan placeholder masing-masing sebagai klausa terpisah |
| TC-FA-GRP-E2E-221-tab-assets-ganti-sort-pemulihan-empty-filter-tetap-tersedia-saat-status-hide-dan-genuine-empty | 37 | Jumlah langkah (37) di atas smell 35 langkah; alasan: semua blok satu kelas harness (fungsional Tab Assets) dan satu dataset Warehouse A, tiap blok berdiri sendiri sehingga kegagalan satu blok tidak menghilangkan makna blok |
| TC-FA-GRP-E2E-222-tab-assets-setup-column-screening-guard-kolom-terakhir-dan-pin-ke-4 | 42 | Alasan di atas 35 langkah: seluruh blok satu kelas (Setup Column Tab Assets, dataset Warehouse A yang sama), tiap blok berdiri sendiri (popup ditutup dan dibuka ulang antar blok), dan 6 dari langkah adalah uncheck kolom berulang (langkah 20 sampai 25) yang dibutuhkan agar tersisa satu |
| TC-FA-GRP-E2E-223-tab-assets-setup-column-reset-esc-cache-dan-kolom-actions-pemicu-column-visibility | 46 | Alasan di atas 35 langkah: seluruh blok satu kelas (Setup Column Tab Assets, dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan TC-FA-GRP-719 memerlukan satu `Verifikasi` per klausa untuk Live Preview dan tabel (default, tanpa curated, tanpa |
| TC-FA-GRP-E2E-229-tab-assets-setup-column-pin-model-type-dan-kolom-category-geser-pin-serta-tampilan-badge | 44 | Alasan di atas 35 langkah (44 langkah): semua blok satu kelas (Setup Column Tab Assets, dataset Warehouse A), tiap blok berdiri sendiri (pin diakhiri unpin), dan dua blok pin memakai urutan langkah identik dengan kolom |
| TC-FA-GRP-E2E-230-tab-assets-download-fungsional-seluruh-data-search-filter-dan-kolom-hide-unhide | 36 | Alasan di atas 35 langkah (36 langkah): seluruh blok satu kelas (Download Tab Assets fungsional, dataset Warehouse A), tiap blok berdiri sendiri, dan 6 langkah toggle overlay (27 sampai 32) mengikuti |
| TC-FA-GRP-E2E-239-tab-assets-filter-category-modal-tree-picker-screening-satu-node-dua-node-dan-search-tree | 42 | Spec melewati sekitar 35 langkah: empat TC tanpa kelas harness (semua fungsional Filter Category pada dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan langkah awal Setup Column serta langkah pemulihan antar-TC menambah panjang tanpa membuka alur baru; kegagalan satu blok tidak membuat … |
| TC-FA-GRP-E2E-240-tab-assets-filter-category-chip-uncheck-node-dan-kombinasi-category-status | 40 | Spec melewati sekitar 35 langkah: tiga TC tanpa kelas harness (semua fungsional Filter Category pada dataset Warehouse A yang sama), tiap blok berdiri sendiri, dan langkah awal Setup Column serta langkah pemulihan antar-TC menambah panjang tanpa membuka alur baru; kegagalan satu blok tidak membuat … |
| TC-FA-GRP-E2E-241-tab-assets-filter-category-centang-parent-turunan-dan-cancel-tree-picker | 36 | Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |
| TC-FA-GRP-E2E-244-tab-assets-filter-label-search-dropdown-chip-opsi-dan-kombinasi-label-status | 43 | Spec ini ([0-9]+) langkah, di atas smell 35 langkah: satu kelas (fungsional), satu dataset (Multi Label Node), tiap blok TC berdiri sendiri dan tidak bergantung pada hasil blok lain; langkah dominan berupa Verifikasi per klausa |
| TC-FA-GRP-E2E-245-tab-assets-label-sort-setup-column-centang-geser-pin | 54 | Spec ini ([0-9]+) langkah, di atas smell 35 langkah: satu kelas (fungsional Setup Column dan Sort Tab Assets), tiap blok TC berdiri sendiri (mulai dari state kolom yang dipulihkan di antara blok), dan kegagalan satu blok tidak menghilangkan makna blok lain; langkah dominan berupa Verifikasi per … |
| TC-FA-GRP-E2E-248-tab-assets-download-isi-berkas-kolom-transactional-policy-last-scanned-dan-group-tidak-berlaku | 38 | Langkah penghubung (S-03): Klik ✕ pada Popup Setup Column; Klik icon Filter untuk menutup Filter Panel; Klik `(←)` pada kotak Search untuk mengosongkan pencarian; Setup Column centang Transactional Policy dan Last Scanned adalah langkah TC. TC-1190 diletakkan pertama karena memeriksa kolom default; … |
| TC-FA-GRP-E2E-249-tab-assets-download-isi-berkas-kolom-bergerbang-asset-value-warranty-custom-field-dan-no-access | 57 | Spec ini ([0-9]+) langkah, di atas smell 35 langkah: seluruh blok satu kelas harness (isi berkas unduhan kolom bergerbang) pada dataset yang sama (Value Gate Node A) dengan alur yang sama, dan ganti akun eksplisit di antara blok (bagian sesudah ganti akun tetap bermakna walau blok sebelumnya … |
| TC-FA-GRP-E2E-250-tab-assets-kolom-tag-ikon-per-tipe-isi-opsi-filter-or-dan-sort-alfabetis | 47 | Spec ini 47 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom TAG), satu dataset (Value Gate Node A), tiap blok TC berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok lain; sebagian besar langkah adalah Verifikasi per |
| TC-FA-GRP-E2E-251-tab-assets-kolom-tag-setup-column-dan-search-label-aksesibilitas-ikon | 46 | Spec ini 46 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom TAG), satu dataset, dua blok TC yang berdiri sendiri (Setup Column lalu Search); langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh |
| TC-FA-GRP-E2E-252-tab-assets-kolom-measurement-symbol-uom-search-isi-opsi-filter-dan-sort | 49 | Spec ini ([0-9]+) langkah, di atas smell 35 langkah: satu kelas (fungsional kolom Measurement), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state pembersih di antaranya; langkah dominan berupa Verifikasi per |
| TC-FA-GRP-E2E-253-tab-assets-kolom-measurement-sort-setup-column-dan-search-transactional-policy | 55 | Spec ini 55 langkah, di atas smell 35 langkah: satu kelas (fungsional kolom Measurement dan Transactional Policy), satu dataset (Value Gate Node A), tiga blok TC yang berdiri sendiri dengan state kolom dipulihkan di antaranya; langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh |
| TC-FA-GRP-E2E-254-tab-assets-kolom-transactional-policy-ikon-filter-or-sort-alfabetis-dan-setup-column | 67 | Spec ini 67 langkah, di atas smell 35 langkah dengan ekspansi: satu kelas (fungsional kolom Transactional Policy), satu dataset (Value Gate Node A), empat blok TC yang berdiri sendiri dengan state dipulihkan di antaranya; langkah dominan berupa Verifikasi per klausa dan pengulangan Refresh |
| TC-FA-GRP-E2E-255-tab-assets-kolom-last-scanned-format-general-settings-filter-rentang-sort-dan-setup-column | 46 | Alasan di atas ~35 langkah: empat blok satu kelas dan satu dataset (Value Gate Node A, kolom Last Scanned); tiap blok berdiri sendiri dan kegagalan satu blok tidak menghilangkan makna blok |
| TC-FA-GRP-E2E-256-tab-assets-asset-value-commercial-hak-pemegang-view-asset-value-dan-manage-accounting | 45 | Alasan di atas ~35 langkah: satu kelas harness dan satu dataset; tiap blok TC berdiri sendiri dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya gagal; langkah penghubung (Search Groups List, buka Filter, tutup popup) ditambahkan tanpa asersi baru. |
| TC-FA-GRP-E2E-257-tab-assets-asset-value-commercial-manage-purchase-tanpa-hak-sort-dan-filter-rentang | 46 | Alasan di atas ~35 langkah: tiga akun pada satu dataset (Value Gate Node A, kolom Asset Value); tiap blok berdiri sendiri dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya |
| TC-FA-GRP-E2E-258-tab-assets-asset-value-setup-column-search-dan-gerbang-akses-di-dua-kolom-buku | 45 | Alasan di atas ~35 langkah: satu dataset (Value Gate Node A, kolom Asset Value); tiga blok berdiri sendiri dan blok setelah ganti akun tetap bermakna walau blok sebelumnya |
| TC-FA-GRP-E2E-259-tab-assets-asset-value-commercial-dan-fiscal-dua-kolom-tetap-not-depreciated-gerbang-dan-sort-filter | 48 | Alasan di atas ~35 langkah: satu dataset (Value Gate Node A, dua kolom buku) dengan empat blok yang berdiri sendiri; blok sesudah ganti akun tetap bermakna walau blok sebelumnya |
| TC-FA-GRP-E2E-260-tab-assets-hak-sel-bergerbang-tier-total-control-dan-default-user | 45 | Alasan di atas ~35 langkah: dua akun pada satu dataset dan satu kelas; tiap blok berdiri sendiri. |
| TC-FA-GRP-E2E-261-tab-assets-hak-sel-bergerbang-tier-read-only-dan-group-manager | 40 | Alasan di atas ~35 langkah: dua akun pada satu dataset dan satu kelas; tiap blok berdiri sendiri. |
| TC-FA-GRP-E2E-262-tab-assets-warranty-expiry-hak-manage-purchase-no-access-dan-view-asset-value-tidak-memberi-akses | 36 | Alasan di atas ~35 langkah: tiga akun pada satu dataset (kolom Warranty Expiry); tiap blok berdiri sendiri dan blok sesudah ganti akun tetap |
| TC-FA-GRP-E2E-263-tab-assets-warranty-expiry-sort-filter-setup-column-dan-hak-group-induk-ke-descendant | 46 | Alasan di atas ~35 langkah: satu kelas, tiga akun pada dataset Value Gate Node A dan Parent > Child; tiap blok berdiri sendiri, dan blok sesudah ganti akun tetap bermakna walau blok sebelumnya |
| TC-FA-GRP-E2E-274-tab-assets-setup-column-komposisi-tanpa-group-custom-field-cost-center-dan-custom-field-inactive | 44 | Alasan di atas ~35 langkah: ketiga TC satu topik (Setup Column Tab Assets, dataset Value Gate Node A), tiap blok berdiri sendiri dan tidak bergantung pada hasil blok lain; tidak ada kelas harness lain. TC-1238 sendiri berisi alur centang, geser, pin, dan reset yang sengaja |
| TC-FA-GRP-E2E-281-wizard-log-ditulis-saat-diterapkan-di-t0-system-log-user-submit-terakhir-dan-siklus-downgrade-berikutnya | 40 | Spec berisi lebih dari 35 langkah. Alasan: dua TC satu kelas (h, penerapan T-0) dan berdiri sendiri; sekitar 17 langkah adalah penghubung seeding, pemicu T-0, dan pembacaan log berpola, bukan asersi |
| TC-FA-GRP-E2E-282-wizard-pagination-default-page-size-navigasi-dan-centang-lintas-halaman | 36 | Spec 36 langkah, di atas smell 35 langkah. Alasan: seluruh blok satu topik dan satu dataset tanpa kelas harness lain; tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan |

### 4.5 Pemecahan ke nomor cadangan

| Spec asal | Spec cadangan | Isi spec cadangan |
|---|---|---|
| 013 | 277 | Guided Tooltip: sidebar collapsed dibuka otomatis dan step kolom Total Asset dilewati |
| 015 | 278 | Role Matrix visibilitas elemen Groups List untuk Read Only dan tanpa aksi tulis |
| 043 | 279 | Konflik dua admin Edit bersamaan (last-write-wins) dan Code auto-generate bentrok (TC-FA-GRP-190, 334, 335) |
| 091 | 281 | Wizard: log ditulis saat diterapkan di T-0, System Log user submit terakhir, dan siklus downgrade berikutnya |
| 097 | 282 | Wizard: pagination default page size, navigasi, dan centang lintas halaman |
| 114 | 284 | Groups List: kombinasi search, filter, sort, pagination, dan Clear Filter saat search atau sort aktif |
| 148 | 283 | Modal Changelog: filter tetap berlaku saat kolom Action di-hide |

Alasan umum pemecahan: spec asal terlalu panjang atau memuat dua kelas pengujian (misalnya konflik batas plan dan konflik Edit), sehingga bagian yang berbeda kelas dipindah ke nomor cadangan. Pemetaan TC ke spec di bagian 1 dan 3 sudah mengikuti pemecahan ini.

### 4.6 Temuan untuk QA (masalah pada sumber TC)

304 spec memuat butir `Temuan untuk QA` di `## Notes`; rincian per TC ada di spec terkait. Pola yang berulang:

- Data uji yang disebut TC tidak ada di tabel Data Uji (Pre-setup/Dinamis), misalnya group 120 karakter pada TC-FA-GRP-3 dan 1093, atau email akun peran tertentu.
- Teks Expected atau nama elemen tidak disebut (misalnya teks tooltip nama aksi ikon, mekanisme penyimpanan preferensi sidebar), sehingga spec mengasersi nama ikon atau perilaku yang terlihat saja.
- Nilai tidak tertulis (Total Asset dan Total User per baris Tabel A), sehingga spec mengasersi format, bukan nilai.
- Cara membaca agregat atau state backend (agregat distinct dedup, jumlah group) tidak disebut TC; spec memakai fixture BE.
- Kontradiksi antar TC, misalnya Code `SR` pada Pre-setup yang sudah dipakai (TC-FA-GRP-330, 331, 1064) versus TC-FA-GRP-326 yang menyebutnya belum dipakai; serta TC-983 (mobile) yang menyebut `Floor 2` kosong padahal punya child beraset.
- Kode dialog bercampur dengan teks dialog (TC-984, D-16 sampai D-18), sehingga spec mengasersi judul dan toast dari kolom Expected.
- Precondition yang bertabrakan dengan hook `beforeEach` suite (spec 017) atau pelaku kedua yang tidak punya akun di Pre-setup.
- Sinkron TestCases 2026-11-12 (Function hanya `None` / `Assignable`, tanpa `Disposal Group`): beberapa TC tidak berubah tetapi masih memuat sisa konsep itu. TC-FA-GRP-369 (urutan sort Function "Assignable → Disposal → — (None)") dan TC-FA-GRP-422 ("Assignable/Disposal sebagai label teks") belum disesuaikan; spec 116 dan 128 memakai dua nilai Function saja (dataset baris eks-Disposal Group kini Function `None`). TC-FA-GRP-303 (Expected c "dropdown assignment/disposal"), TC-FA-GRP-903, serta TC-FA-GRP-906 (dropdown Disposal sebagai modul konsumen) tidak berubah sehingga spec 091, 203 (TC-903), dan 204 mempertahankan langkah terkait modul Disposal. Spec wizard 090 sampai 100 dan 281 hanya menyeed node bernama `Disposal Yard` (Function None) mengikuti jumlah enam group pada TC-FA-GRP-303; namanya tidak lagi bermakna Disposal Group.
