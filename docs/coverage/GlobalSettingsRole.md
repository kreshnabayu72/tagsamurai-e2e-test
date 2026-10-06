# Coverage E2E — Global Settings > Role & Permission

Sumber: `global-settings/role/TestCases/tc-role.md` (323 TC aktif pasca pencabutan 34 TC BE murni/direct API, mobile web-only, dan legacy MFA/User Type) dan `global-settings/role/TestCases/tc-role-frontend.md` (45 integration test cases).
Referensi: `global-settings/role/PRD/role.md`.
Suite: `specs/GlobalSettings/Role/`.
Prefix Modul: `GS` + `ROLE` (`TC-GS-ROLE-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (56 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | Screening Struktur 3 Tab (Total Control, Read Only, System) dan Halaman Detail | FE+BE | TC-GS-ROLE-01, TC-GS-ROLE-02, TC-GS-ROLE-03, TC-GS-ROLE-04, TC-GS-ROLE-05, TC-GS-ROLE-06 |
| TC-GS-ROLE-E2E-002-loading-skeleton-no-result-dan-read-failure-resilience | Loading State, No-Result Search, dan Ketahanan Terhadap Gagal Fetch Data | mock | TC-GS-ROLE-07 |
| TC-GS-ROLE-E2E-003-empty-state-detail-role-dan-tab-read-only | Tampilan Empty State pada Halaman Detail 0-User dan Tab Read Only 0-User | mock | TC-GS-ROLE-355 |
| TC-GS-ROLE-E2E-004-landing-state-user-tanpa-role-dan-pemulihan-akses | Landing State Kosong User Tanpa Role dan Pemulihan Otomatis Saat Akses Di-assign | FE+BE | TC-GS-ROLE-08, TC-GS-ROLE-09 |
| TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | Guided Tooltip 4-Step Walkthrough, Siklus Navigasi, Trigger First-Visit, dan Replay | mock | TC-GS-ROLE-121, TC-GS-ROLE-122, TC-GS-ROLE-123, TC-GS-ROLE-124, TC-GS-ROLE-125 |
| TC-GS-ROLE-E2E-006-role-matrix-positif-total-control-dan-capability-holder | Role Matrix Positif: Visibilitas Kontrol dan Hak Akses Penuh Total Control serta Update Role | FE+BE | TC-GS-ROLE-10, TC-GS-ROLE-12, TC-GS-ROLE-354 |
| TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | Role Matrix Negatif: Hak Akses Read Only, Menu Tersembunyi No Role, dan Direct URL 403 | FE+BE | TC-GS-ROLE-11, TC-GS-ROLE-13, TC-GS-ROLE-101, TC-GS-ROLE-104 |
| TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | Matriks Guard Aktor × Target: Proteksi Self-Edit dan Pembatasan Target Total Control / Read Only | FE+BE | TC-GS-ROLE-61, TC-GS-ROLE-62, TC-GS-ROLE-63, TC-GS-ROLE-64, TC-GS-ROLE-67 |
| TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | Screening Popup Table User Picker Assign Total Control, Pencarian, Filter Kelayakan, dan Validasi Nol Pilihan | FE+BE | TC-GS-ROLE-15, TC-GS-ROLE-18, TC-GS-ROLE-19, TC-GS-ROLE-20, TC-GS-ROLE-313 |
| TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write | Penugasan Total Control Sukses, Shortcut Bulk-Write 6 Role, dan Kenaikan Counter Users | FE+BE | TC-GS-ROLE-16, TC-GS-ROLE-17, TC-GS-ROLE-82, TC-GS-ROLE-353 |
| TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi | Screening Dialog Konfirmasi Remove Total Control, Pembatalan Cancel, dan Guard Default User serta Self-Edit | FE+BE | TC-GS-ROLE-21, TC-GS-ROLE-23, TC-GS-ROLE-24, TC-GS-ROLE-26 |
| TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role | Pencabutan Total Control Sukses, Reset Akses Menjadi Null, Bulk-Delete 6 Role, dan Penurunan Counter | FE+BE | TC-GS-ROLE-22, TC-GS-ROLE-25, TC-GS-ROLE-28, TC-GS-ROLE-83 |
| TC-GS-ROLE-E2E-013-assign-dan-remove-total-control-server-failure-resilience | Ketahanan Alur Assign dan Remove Total Control Terhadap Kegagalan Server 5xx | mock | TC-GS-ROLE-27 |
| TC-GS-ROLE-E2E-014-assign-read-only-happy-path-screening-dan-filter-kelayakan | Screening Table User Picker Assign Read Only, Filter Kelayakan, dan Penugasan Sukses Bulk-Write | FE+BE | TC-GS-ROLE-29, TC-GS-ROLE-30, TC-GS-ROLE-329 |
| TC-GS-ROLE-E2E-015-remove-read-only-happy-path-dialog-cancel-dan-guard-proteksi | Pencabutan Read Only Sukses, Screening Dialog Konfirmasi, Pembatalan Cancel, dan Guard Self-Edit | FE+BE | TC-GS-ROLE-31, TC-GS-ROLE-330 |
| TC-GS-ROLE-E2E-016-assign-dan-remove-read-only-server-failure-resilience | Ketahanan Alur Assign dan Remove Read Only Terhadap Kegagalan Server 5xx Serta Notifikasi In-App | mock | TC-GS-ROLE-114 |
| TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save | Screening Checkbox CRUD Detail Role, Kunci Permanen Kolom Read, dan Auto-Save Per-Cell | FE+BE | TC-GS-ROLE-32, TC-GS-ROLE-33, TC-GS-ROLE-326, TC-GS-ROLE-328 |
| TC-GS-ROLE-E2E-018-detail-crud-checkbox-write-failure-dan-debounce | Ketahanan Auto-Save Checkbox CRUD Terhadap Kegagalan Server 5xx dan Rapid Toggle Debounce | mock | TC-GS-ROLE-35, TC-GS-ROLE-110 |
| TC-GS-ROLE-E2E-019-detail-table-user-picker-assign-role-screening-dan-empty-states | Screening Popup Table User Picker Assign Role ([+ Add User]), Counter Seleksi, dan Empty States | mock | TC-GS-ROLE-36, TC-GS-ROLE-331 |
| TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | Penugasan Role ke User Sukses, Baseline Read Otomatis, dan Pengecualian User Ter-assign | FE+BE | TC-GS-ROLE-37, TC-GS-ROLE-38, TC-GS-ROLE-39, TC-GS-ROLE-40, TC-GS-ROLE-333 |
| TC-GS-ROLE-E2E-021-detail-table-user-picker-stale-reference-resilience | Penanganan Stale Reference pada Popup Table User Picker Saat User Dihapus / Di-assign Bersamaan | mock | TC-GS-ROLE-332, TC-GS-ROLE-357 |
| TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi | Screening Dialog Remove Role Assignment Tunggal, Pembatalan Cancel, dan Guard Self-Edit serta Target TC/RO | FE+BE | TC-GS-ROLE-41, TC-GS-ROLE-43, TC-GS-ROLE-44, TC-GS-ROLE-115 |
| TC-GS-ROLE-E2E-023-detail-remove-single-happy-path-dan-penurunan-counter | Pencabutan Role Assignment Tunggal Sukses dan Refleksi Penurunan Counter Users | FE+BE | TC-GS-ROLE-42, TC-GS-ROLE-327 |
| TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit | Screening Bulk Action Bar, Counter Seleksi, Server Select All Lintas Halaman, Toggle Unselect All, dan Selection Limit 1000 | FE+BE | TC-GS-ROLE-45, TC-GS-ROLE-229, TC-GS-ROLE-320, TC-GS-ROLE-321 |
| TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | Screening Dialog Bulk Remove Role (Varian Homogen vs Campuran TC/RO), Pembatalan Cancel, dan Guard Self-Edit | FE+BE | TC-GS-ROLE-46, TC-GS-ROLE-47, TC-GS-ROLE-49, TC-GS-ROLE-50, TC-GS-ROLE-356 |
| TC-GS-ROLE-E2E-026-detail-bulk-remove-role-happy-path-uniform-dan-server-failure | Pencabutan Massal Role Assignment Sukses (Homogen Semua Aman) dan Ketahanan Terhadap Gagal Server | FE+BE | TC-GS-ROLE-48, TC-GS-ROLE-51 |
| TC-GS-ROLE-E2E-027-auto-revert-via-edit-crud-screening-dialog-dan-cancel | Screening Dialog Konfirmasi Auto-Revert Saat Mengedit CRUD User Total Control / Read Only dan Pembatalan Cancel | FE+BE | TC-GS-ROLE-52, TC-GS-ROLE-53 |
| TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | Eksekusi Auto-Revert Sukses via Edit CRUD: Pelepasan Access Level Menjadi Null dan Preservasi Sisa Role | FE+BE | TC-GS-ROLE-54, TC-GS-ROLE-55, TC-GS-ROLE-56, TC-GS-ROLE-57, TC-GS-ROLE-70 |
| TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro | Eksekusi Auto-Revert Sukses via Remove Baris Role Tunggal pada User Total Control dan Read Only | FE+BE | TC-GS-ROLE-58, TC-GS-ROLE-59, TC-GS-ROLE-60, TC-GS-ROLE-68 |
| TC-GS-ROLE-E2E-030-tabel-total-control-hover-truncation-dan-wrap-nama-panjang | Tampilan Kolom Name Tab Total Control: Wrap Natural Nama Panjang dan Tooltip Lengkap via Hover serta Keyboard Focus | mock | TC-GS-ROLE-77 |
| TC-GS-ROLE-E2E-031-tabel-total-control-search-box-cycle-dan-guard-scope | Pola Interaksi Search Box Toolbar Tab Total Control dan Guard Kolom Non-Searchable | FE+BE | TC-GS-ROLE-127, TC-GS-ROLE-315 |
| TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | Screening Filter Panel Tab Total Control dan Penerapan Filter Single 8 Field | FE+BE | TC-GS-ROLE-69, TC-GS-ROLE-131, TC-GS-ROLE-132, TC-GS-ROLE-133, TC-GS-ROLE-134, TC-GS-ROLE-135, TC-GS-ROLE-136, TC-GS-ROLE-230 |
| TC-GS-ROLE-E2E-033-tabel-total-control-filter-date-last-updated | Penerapan Filter Date Picker Kolom Last Updated Tab Total Control (Varian 1 Hari vs Rentang Tanggal) | FE+BE | TC-GS-ROLE-338, TC-GS-ROLE-339 |
| TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | Mekanisme Dropdown Filter Tab Total Control: Hardcode vs Populate, Search-Within, Logika OR, dan Siklus Chip | FE+BE | TC-GS-ROLE-231, TC-GS-ROLE-232, TC-GS-ROLE-233, TC-GS-ROLE-234, TC-GS-ROLE-235, TC-GS-ROLE-236 |
| TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | Kombinasi Penuh Search dan Multi-Filter Tab Total Control Serta Pemulihan Empty State | FE+BE | TC-GS-ROLE-145, TC-GS-ROLE-146, TC-GS-ROLE-147, TC-GS-ROLE-148, TC-GS-ROLE-149, TC-GS-ROLE-150, TC-GS-ROLE-151, TC-GS-ROLE-152, TC-GS-ROLE-153 |
| TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | Sorting 3-State (Ascending, Descending, Default) untuk Seluruh 10 Kolom Sortable Tab Total Control | FE+BE | TC-GS-ROLE-164, TC-GS-ROLE-165, TC-GS-ROLE-166, TC-GS-ROLE-167, TC-GS-ROLE-168, TC-GS-ROLE-169, TC-GS-ROLE-170, TC-GS-ROLE-171, TC-GS-ROLE-172 |
| TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | Setup Column Tab Total Control: Screening Overlay, Popup Modal Visibilitas, Urutan, Pin Kolom, dan Reset/Cancel | mock | TC-GS-ROLE-183, TC-GS-ROLE-201, TC-GS-ROLE-202, TC-GS-ROLE-203, TC-GS-ROLE-250, TC-GS-ROLE-251, TC-GS-ROLE-252, TC-GS-ROLE-253, TC-GS-ROLE-254, TC-GS-ROLE-255, TC-GS-ROLE-256, TC-GS-ROLE-258, TC-GS-ROLE-259, TC-GS-ROLE-260, TC-GS-ROLE-261, TC-GS-ROLE-263, TC-GS-ROLE-264, TC-GS-ROLE-265, TC-GS-ROLE-266, TC-GS-ROLE-267, TC-GS-ROLE-268, TC-GS-ROLE-270, TC-GS-ROLE-271, TC-GS-ROLE-272, TC-GS-ROLE-273, TC-GS-ROLE-275, TC-GS-ROLE-276, TC-GS-ROLE-277, TC-GS-ROLE-278, TC-GS-ROLE-279, TC-GS-ROLE-280, TC-GS-ROLE-282, TC-GS-ROLE-283, TC-GS-ROLE-284, TC-GS-ROLE-285, TC-GS-ROLE-287, TC-GS-ROLE-288 |
| TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | Ekspor Download CSV/XLSX dan Navigasi Pagination Tab Total Control | FE+BE | TC-GS-ROLE-74, TC-GS-ROLE-75, TC-GS-ROLE-76, TC-GS-ROLE-334, TC-GS-ROLE-346 |
| TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | Pengujian Table Tools Tab Read Only: Search, Filter 8 Field, Sort Name, Download CSV/XLSX, dan Pagination | FE+BE | TC-GS-ROLE-71, TC-GS-ROLE-128, TC-GS-ROLE-138, TC-GS-ROLE-154, TC-GS-ROLE-174, TC-GS-ROLE-184, TC-GS-ROLE-204, TC-GS-ROLE-335, TC-GS-ROLE-340, TC-GS-ROLE-347 |
| TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | Pengujian Tabel Tab System: 6 Baris Fixed, Pencarian Role Name, Download CSV/XLSX, dan Guard Ketiadaan Sort/Pagination | FE+BE | TC-GS-ROLE-72, TC-GS-ROLE-129, TC-GS-ROLE-185, TC-GS-ROLE-337, TC-GS-ROLE-348 |
| TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | Pengujian Toolbar Detail Role: Siklus Search Box dan Filter Panel 6 Field Dinamis | FE+BE | TC-GS-ROLE-73, TC-GS-ROLE-130, TC-GS-ROLE-139, TC-GS-ROLE-140, TC-GS-ROLE-141, TC-GS-ROLE-142, TC-GS-ROLE-143, TC-GS-ROLE-237 |
| TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | Kombinasi Search dan Filter pada Halaman Detail Serta Pemulihan Empty State | FE+BE | TC-GS-ROLE-155, TC-GS-ROLE-156, TC-GS-ROLE-157, TC-GS-ROLE-158, TC-GS-ROLE-159, TC-GS-ROLE-160, TC-GS-ROLE-161, TC-GS-ROLE-162, TC-GS-ROLE-163 |
| TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | Sorting 3-State 6 Kolom, Setup Column, Download CSV/XLSX Dinamis, dan Pagination Halaman Detail | FE+BE | TC-GS-ROLE-175, TC-GS-ROLE-176, TC-GS-ROLE-177, TC-GS-ROLE-178, TC-GS-ROLE-179, TC-GS-ROLE-180, TC-GS-ROLE-186, TC-GS-ROLE-205, TC-GS-ROLE-336, TC-GS-ROLE-349 |
| TC-GS-ROLE-E2E-044-changelog-total-control-screening-empty-state-dan-hover | Screening Modal Changelog Tab Total Control, Tampilan Empty State, dan Hover Tooltip | FE+BE | TC-GS-ROLE-78, TC-GS-ROLE-116, TC-GS-ROLE-209 |
| TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | Pola Interaksi Search Box dan Filter Panel Modal Changelog Total Control (Termasuk Filter Date 1 Hari & Range) | FE+BE | TC-GS-ROLE-85, TC-GS-ROLE-187, TC-GS-ROLE-188, TC-GS-ROLE-189, TC-GS-ROLE-190, TC-GS-ROLE-191, TC-GS-ROLE-192, TC-GS-ROLE-341, TC-GS-ROLE-342 |
| TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | Mekanisme Dropdown Filter Modal Changelog Total Control: Populate Scoped, Search-Within, Logika OR, dan Chip Cycles | FE+BE | TC-GS-ROLE-211, TC-GS-ROLE-212, TC-GS-ROLE-213, TC-GS-ROLE-214, TC-GS-ROLE-226 |
| TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | Kombinasi Search dan Multi-Filter Modal Changelog Total Control Serta Pemulihan Empty State | FE+BE | TC-GS-ROLE-193, TC-GS-ROLE-194, TC-GS-ROLE-195, TC-GS-ROLE-196, TC-GS-ROLE-197, TC-GS-ROLE-198, TC-GS-ROLE-199, TC-GS-ROLE-200 |
| TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | Sorting 3-State 7 Kolom, Setup Column 7 Kolom, dan Ekspor Download Modal Changelog Total Control | mock | TC-GS-ROLE-206, TC-GS-ROLE-207, TC-GS-ROLE-208, TC-GS-ROLE-210, TC-GS-ROLE-289, TC-GS-ROLE-290, TC-GS-ROLE-291, TC-GS-ROLE-292, TC-GS-ROLE-293, TC-GS-ROLE-294, TC-GS-ROLE-295, TC-GS-ROLE-296, TC-GS-ROLE-297, TC-GS-ROLE-298, TC-GS-ROLE-299, TC-GS-ROLE-300, TC-GS-ROLE-301, TC-GS-ROLE-302, TC-GS-ROLE-303, TC-GS-ROLE-304, TC-GS-ROLE-305, TC-GS-ROLE-306, TC-GS-ROLE-307, TC-GS-ROLE-308, TC-GS-ROLE-309, TC-GS-ROLE-310, TC-GS-ROLE-311, TC-GS-ROLE-312 |
| TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download | Pengujian Modal Changelog Tab Read Only: Search, Filter, Sort, Setup Column, dan Download CSV/XLSX | FE+BE | TC-GS-ROLE-79, TC-GS-ROLE-215, TC-GS-ROLE-345, TC-GS-ROLE-350 |
| TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | Pengujian Modal Changelog Tab System: Filter Unik Role, Dropdown Populate, Sorting 3-State 7 Kolom, dan Download | FE+BE | TC-GS-ROLE-80, TC-GS-ROLE-216, TC-GS-ROLE-217, TC-GS-ROLE-218, TC-GS-ROLE-219, TC-GS-ROLE-220, TC-GS-ROLE-227, TC-GS-ROLE-238, TC-GS-ROLE-239, TC-GS-ROLE-240, TC-GS-ROLE-241, TC-GS-ROLE-242, TC-GS-ROLE-243, TC-GS-ROLE-343, TC-GS-ROLE-351 |
| TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | Pengujian Modal Changelog Detail Role: Filter Dinamis Field Sesuai Hak Akses, Sorting 7 Kolom, dan Download | FE+BE | TC-GS-ROLE-81, TC-GS-ROLE-221, TC-GS-ROLE-222, TC-GS-ROLE-223, TC-GS-ROLE-224, TC-GS-ROLE-225, TC-GS-ROLE-228, TC-GS-ROLE-244, TC-GS-ROLE-245, TC-GS-ROLE-246, TC-GS-ROLE-247, TC-GS-ROLE-248, TC-GS-ROLE-249, TC-GS-ROLE-344, TC-GS-ROLE-352 |
| TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | Pencatatan Audit Log pada 3 Surface (Changelog, System Log, Activity Log) dan Verifikasi Baris Kanonik | FE+BE | TC-GS-ROLE-84, TC-GS-ROLE-86, TC-GS-ROLE-87, TC-GS-ROLE-88, TC-GS-ROLE-322, TC-GS-ROLE-323, TC-GS-ROLE-324, TC-GS-ROLE-325 |
| TC-GS-ROLE-E2E-053-sinkronisasi-dua-arah-tab-role-detail-user-dan-format-datetime | Sinkronisasi Dua Arah dengan Tab Role pada Modul User Serta Konsistensi Format Tanggal dan Waktu | FE+BE | TC-GS-ROLE-102, TC-GS-ROLE-103, TC-GS-ROLE-105 |
| TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi | Keamanan: Isolasi Multi-Tenant, Sanitasi Payload SQL Injection pada Pencarian, dan Guard Notifikasi | FE+BE | TC-GS-ROLE-108, TC-GS-ROLE-109, TC-GS-ROLE-314, TC-GS-ROLE-316 |
| TC-GS-ROLE-E2E-055-entitas-suspended-expired-dan-integritas-unique-constraint | Pemblokiran Aksi Tulis Saat Client Suspended atau Expired Serta Integritas Unique Constraint User-Role | mock | TC-GS-ROLE-112, TC-GS-ROLE-113 |
| TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove | Penanganan Konflik Konkurensi 2-Aktor: Concurrent Edit CRUD dan Cross-Action Race Assign vs Remove vs Auto-Revert | mock | TC-GS-ROLE-111, TC-GS-ROLE-317, TC-GS-ROLE-318, TC-GS-ROLE-319 |

---

## 2. Alasan TC Hanya-BE & TC Non-E2E

Dari total 357 nomor identifikasi pada dokumen `tc-role.md`, terdapat 34 nomor yang dicabut / tidak masuk ke dalam Spec E2E dengan klasifikasi sebagai berikut:

1. **TC Murni Backend / Direct API (16 TC):**
   - `TC-GS-ROLE-14`, `TC-GS-ROLE-34`, `TC-GS-ROLE-65`, `TC-GS-ROLE-66`, `TC-GS-ROLE-89` s/d `100`, `TC-GS-ROLE-106`, `TC-GS-ROLE-107`.
   - Seluruh kasus ini memvalidasi manipulasi payload HTTP langsung, UUID tampering, missing header, response body structure, dan SQL error handling yang tidak terjangkau antarmuka pengguna web. Dikelola terpisah pada dokumen `tc-role-backend.md`.

2. **Mobile Web-Only / Viewport Kecil (5 TC):**
   - `TC-GS-ROLE-117`, `TC-GS-ROLE-118`, `TC-GS-ROLE-119`, `TC-GS-ROLE-120`, `TC-GS-ROLE-126`.
   - Mengharuskan viewport mobile portrait (< 768px), drawer layout, swipe gesture yang tidak didukung pada platform web desktop TAG Samurai.

3. **Legacy MFA / User Type Deprecated (12 TC):**
   - `TC-GS-ROLE-137`, `TC-GS-ROLE-144`, `TC-GS-ROLE-173`, `TC-GS-ROLE-181`, `TC-GS-ROLE-257`, `TC-GS-ROLE-262`, `TC-GS-ROLE-269`, `TC-GS-ROLE-274`, `TC-GS-ROLE-281`, `TC-GS-ROLE-286`.
   - Telah dihapus dan dipusatkan ke modul `Auth > MFA` dan `General Settings > User Type`.

4. **Historical Gap (1 TC):**
   - `TC-GS-ROLE-182` (nomor urut dilewati dalam versi revisi dokumen TC).

Dengan demikian, seluruh **323 TC aktif** yang memiliki dampak fungsional antarmuka web tercakup **100%** ke dalam 56 E2E Specifications.

---

## 3. Lapisan per TC (Seluruh 323 TC Granular Aktif)

| TC ID | Skenario | Prioritas | Lapisan | Spec E2E | Mode | Catatan |
|---|---|:---:|:---:|---|:---:|---|
| TC-GS-ROLE-01 | Screening 3 Zona — Tab Total Control | P0 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-02 | Screening 3 Zona — Tab Read Only | P0 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-03 | Screening 3 Zona — Tab System (6 role fixed, selalu tampil meski 0 user) | P0 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-04 | Screening 3 Zona — Detail (halaman terpisah, kolom CRUD dinamis per role) | P0 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-05 | Detail — kolom CRUD dinamis berbeda per role (verifikasi 3 varian: 4-kolom, 2-kolom C+R, 2-kolom R+D, 2-kolom R+U) | P1 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-06 | Detail — dua jalur akses (klik Role Name vs row action Detail) identik | P2 | E2E | TC-GS-ROLE-E2E-001-screening-tabel-utama-dan-struktur-3-tab | FE+BE |  |
| TC-GS-ROLE-07 | Loading, Empty (Detail 0 user), No-result, Read-failure resilience | P1 | E2E | TC-GS-ROLE-E2E-002-loading-skeleton-no-result-dan-read-failure-resilience | mock |  |
| TC-GS-ROLE-08 | Landing State — user login tanpa role apa pun, sidebar kosong total | P1 | E2E | TC-GS-ROLE-E2E-004-landing-state-user-tanpa-role-dan-pemulihan-akses | FE+BE | Transisi landing state saat role di-assign |
| TC-GS-ROLE-09 | Landing State — hilang otomatis begitu admin assign akses | P2 | E2E | TC-GS-ROLE-E2E-004-landing-state-user-tanpa-role-dan-pemulihan-akses | FE+BE | Transisi landing state saat role di-assign |
| TC-GS-ROLE-121 | Guided Tooltip — Screening Konten per Step verbatim PRD | P1 | E2E | TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock |  |
| TC-GS-ROLE-122 | Guided Tooltip — Trigger Auto First Visit, tidak muncul lagi setelah seen | P1 | E2E | TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock |  |
| TC-GS-ROLE-123 | Guided Tooltip — Trigger Manual Replay `[?]`, tidak reset flag `seen` | P2 | E2E | TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock |  |
| TC-GS-ROLE-124 | Guided Tooltip — Siklus Navigasi Skip/Back/Next/Done (4 step) | P1 | E2E | TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock |  |
| TC-GS-ROLE-125 | Guided Tooltip — Exit Tanpa Selesai (resize/navigasi keluar), flag TIDAK ter-set | P1 | E2E | TC-GS-ROLE-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock |  |
| TC-GS-ROLE-10 | Matriks — Total Control (semua tab, semua aksi, termasuk target TC/RO lain) | P0 | E2E | TC-GS-ROLE-E2E-006-role-matrix-positif-total-control-dan-capability-holder | FE+BE |  |
| TC-GS-ROLE-11 | Matriks — Read Only (lihat semua data penuh, semua aksi tulis Disabled) | P0 | E2E | TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE |  |
| TC-GS-ROLE-12 | Matriks — capability holder "Manage user and role" (Update), target biasa | P0 | E2E | TC-GS-ROLE-E2E-006-role-matrix-positif-total-control-dan-capability-holder | FE+BE |  |
| TC-GS-ROLE-13 | Matriks — No Role (menu tersembunyi) | P0 | E2E | TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE |  |
| TC-GS-ROLE-15 | Screening — Popup `[+ Assign]` Table User Picker | P0 | E2E | TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | FE+BE |  |
| TC-GS-ROLE-16 | Assign Total Control — Happy Path, shortcut bulk-write 6 role | P0 | E2E | TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write | FE+BE |  |
| TC-GS-ROLE-17 | Assign Total Control — user sudah punya sebagian role, shortcut bulk-write TIDAK menghasilkan entry log per-role di Changelog System sama sekali (baik baris baru maupun existing) | P1 | E2E | TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write | FE+BE |  |
| TC-GS-ROLE-18 | Assign Total Control — user yang sedang Read Only tidak muncul di popup Assign TC | P1 | E2E | TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | FE+BE |  |
| TC-GS-ROLE-19 | Assign Total Control — user tanpa `access: global_settings` tidak pernah muncul di popup | P1 | E2E | TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | FE+BE |  |
| TC-GS-ROLE-20 | Assign Total Control — user Inactive/deactivated tidak muncul di popup; user Pending Activation TETAP muncul | P1 | E2E | TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | FE+BE |  |
| TC-GS-ROLE-21 | Screening Dialog Remove Total Control | P0 | E2E | TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-22 | Remove Total Control — Happy Path, access_level→null + bulk-delete 6 role, TANPA entry log per-role | P0 | E2E | TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role | FE+BE |  |
| TC-GS-ROLE-23 | Remove Total Control — Default User tidak pernah bisa di-Remove (disabled permanen, bukan count-check) | P0 | E2E | TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-24 | Remove Total Control — self-edit diblok bahkan untuk Total Control (aktor = target) | P0 | E2E | TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-25 | Remove Total Control — user TC lain tetap bisa di-Remove walau saat itu "kebetulan satu-satunya TC selain Default User" (tidak ada guard count tambahan) | P2 | E2E | TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role | FE+BE |  |
| TC-GS-ROLE-26 | Cancel Dialog Remove Total Control | P2 | E2E | TC-GS-ROLE-E2E-011-remove-total-control-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-27 | Assign/Remove Total Control — Write Failure Resilience | P1 | E2E | TC-GS-ROLE-E2E-013-assign-dan-remove-total-control-server-failure-resilience | mock | ROLE-LOGIC-02: Default User dilindungi |
| TC-GS-ROLE-28 | Notifikasi In-App — Remove Total Control memicu notifikasi ke target, Assign TIDAK | P1 | E2E | TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role | FE+BE | ROLE-LOGIC-02: Default User dilindungi |
| TC-GS-ROLE-314 | Notifikasi Target User — Action Tier "view-only", Tombol `[Mark as Read]` Tampil Tanpa Tombol `[Detail]` | P1 | E2E | TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi | FE+BE |  |
| TC-GS-ROLE-29 | Assign Read Only — Happy Path, shortcut bulk-write 6 role Read-only | P0 | E2E | TC-GS-ROLE-E2E-014-assign-read-only-happy-path-screening-dan-filter-kelayakan | FE+BE | ROLE-LOGIC-01: Self-edit diblokir |
| TC-GS-ROLE-30 | Assign Read Only — popup exclude user TC (harus Remove TC dulu) & user RO existing | P1 | E2E | TC-GS-ROLE-E2E-014-assign-read-only-happy-path-screening-dan-filter-kelayakan | FE+BE | ROLE-LOGIC-01: Self-edit diblokir |
| TC-GS-ROLE-31 | Remove Read Only — Happy Path & self-edit guard (identik pola TC) | P1 | E2E | TC-GS-ROLE-E2E-015-remove-read-only-happy-path-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-114 | Assign/Remove Read Only — Write Failure Resilience & Notifikasi In-App | P1 | E2E | TC-GS-ROLE-E2E-016-assign-dan-remove-read-only-server-failure-resilience | mock |  |
| TC-GS-ROLE-355 | Empty State — Tab Read Only 0 user | P2 | E2E | TC-GS-ROLE-E2E-003-empty-state-detail-role-dan-tab-read-only | mock |  |
| TC-GS-ROLE-32 | Edit CRUD inline — Read selalu checked+disabled, tidak bisa di-uncheck | P0 | E2E | TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save | FE+BE |  |
| TC-GS-ROLE-33 | Edit CRUD inline — Update independen, auto-save per cell | P0 | E2E | TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save | FE+BE |  |
| TC-GS-ROLE-35 | Edit CRUD — Write Failure Resilience, cell dipertahankan | P1 | E2E | TC-GS-ROLE-E2E-018-detail-crud-checkbox-write-failure-dan-debounce | mock |  |
| TC-GS-ROLE-36 | Screening Popup `[+ Assign]` (Detail) — Table User Picker | P0 | E2E | TC-GS-ROLE-E2E-019-detail-table-user-picker-assign-role-screening-dan-empty-states | mock |  |
| TC-GS-ROLE-331 | Popup Table User Picker — Empty States (2 varian) & Selection Counter | P2 | E2E | TC-GS-ROLE-E2E-019-detail-table-user-picker-assign-role-screening-dan-empty-states | mock |  |
| TC-GS-ROLE-313 | Search Box di Popup Table User Picker — Pencarian Multi-Kolom (Name, Email, Position, Division), Case-Insensitive, Submit on Enter & Clear via (✕) | P1 | E2E | TC-GS-ROLE-E2E-009-table-user-picker-assign-total-control-screening-dan-filter | FE+BE |  |
| TC-GS-ROLE-332 | Table User Picker — multi-select stale reference: user terpilih di-delete sebelum Submit Assign (D6) | P1 | E2E | TC-GS-ROLE-E2E-021-detail-table-user-picker-stale-reference-resilience | mock |  |
| TC-GS-ROLE-357 | Table User Picker — multi-select stale reference: DUA user terpilih sekaligus di-delete sebelum Submit Assign (D6, varian >1 user) | P2 | E2E | TC-GS-ROLE-E2E-021-detail-table-user-picker-stale-reference-resilience | mock |  |
| TC-GS-ROLE-333 | Table User Picker — user yang sedang dipilih direname di modul User sebelum Assign diklik (Rename-safe submit) | P1 | E2E | TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | FE+BE |  |
| TC-GS-ROLE-37 | Assign Role — Happy Path, Read otomatis terkunci, C/U/D default unchecked | P0 | E2E | TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | FE+BE |  |
| TC-GS-ROLE-38 | Assign Role — admin centang sebagian CRUD sebelum submit, log tambahan | P1 | E2E | TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | FE+BE |  |
| TC-GS-ROLE-39 | Assign Role — Kolom "Users" Tab System bertambah 1 setelah Assign | P1 | E2E | TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | FE+BE |  |
| TC-GS-ROLE-40 | Assign Role — Write Failure Resilience | P1 | E2E | TC-GS-ROLE-E2E-020-detail-assign-role-happy-path-dan-guard-duplikasi | FE+BE |  |
| TC-GS-ROLE-41 | Screening Dialog Remove (single) — target biasa | P0 | E2E | TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-42 | Remove (single) — Happy Path, hard delete + Users count berkurang 1 | P0 | E2E | TC-GS-ROLE-E2E-023-detail-remove-single-happy-path-dan-penurunan-counter | FE+BE |  |
| TC-GS-ROLE-115 | Remove (single) — Write Failure Resilience | P1 | E2E | TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-43 | Remove (single) — target = Default User, disabled permanen siapa pun aktornya | P0 | E2E | TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-44 | Remove (single) — idempotent, baris sudah tidak ada dianggap sukses (bukan error) | P2 | E2E | TC-GS-ROLE-E2E-022-detail-remove-single-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-320 | Selection Limit — Live-Block Seleksi Manual saat Checkbox ke-1001 Dicentang | P2 | E2E | TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit | FE+BE |  |
| TC-GS-ROLE-321 | Selection Limit — Auto-Cap saat Select All Melebihi 1000 Baris Filtered | P2 | E2E | TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit | FE+BE |  |
| TC-GS-ROLE-45 | Screening Bulk Action Bar (Detail — satu2nya tempat ada bulk) | P1 | E2E | TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit | FE+BE | ROLE-LOGIC-05: Read checkbox locked disabled |
| TC-GS-ROLE-229 | Button "Select All ({N} records)" — Detail, Server Select All Lintas Halaman, Toggle ke "Unselect All" saat 100% Terpilih, & Muncul Lagi saat Uncheck Parsial | P2 | E2E | TC-GS-ROLE-E2E-024-detail-bulk-action-bar-screening-server-select-all-dan-selection-limit | FE+BE |  |
| TC-GS-ROLE-46 | Bulk Remove — semua target biasa (tanpa TC/RO) | P0 | E2E | TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-47 | Bulk Remove — seleksi campuran regular + TC/RO (hanya bisa dicentang aktor Total Control), auto-revert per baris TC/RO | P0 | E2E | TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-48 | Bulk Remove — Partial failure, sebagian baris sudah dihapus admin lain | P1 | E2E | TC-GS-ROLE-E2E-026-detail-bulk-remove-role-happy-path-uniform-dan-server-failure | FE+BE |  |
| TC-GS-ROLE-49 | Bulk Remove — dieksekusi actor role "Manage user and role" Update (non-TC) sampai sukses, terbatas target biasa | P1 | E2E | TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-50 | Bulk Remove — Write Failure Resilience | P1 | E2E | TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-356 | Cancel Dialog Bulk Remove | P2 | E2E | TC-GS-ROLE-E2E-025-detail-bulk-remove-role-screening-dialog-cancel-dan-guard-proteksi | FE+BE |  |
| TC-GS-ROLE-353 | Tab System — Kolom "Users" bertambah 1 utk KESEMUA 6 role sekaligus setelah Assign Total Control/Read Only (shortcut bulk-write ikut dihitung, bukan hanya assign role individual — melengkapi `TC-39` yang cuma role tunggal via Detail) | P1 | E2E | TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write | FE+BE |  |
| TC-GS-ROLE-51 | Auto-Revert — hasil edit MASIH cocok pattern tier, tidak ada efek tambahan | P2 | E2E | TC-GS-ROLE-E2E-026-detail-bulk-remove-role-happy-path-uniform-dan-server-failure | FE+BE |  |
| TC-GS-ROLE-52 | Screening Dialog Auto-Revert — edit role menyimpang pattern | P0 | E2E | TC-GS-ROLE-E2E-027-auto-revert-via-edit-crud-screening-dialog-dan-cancel | FE+BE |  |
| TC-GS-ROLE-53 | Auto-Revert — Cancel, cell reset ke semula, tidak ada PATCH | P1 | E2E | TC-GS-ROLE-E2E-027-auto-revert-via-edit-crud-screening-dialog-dan-cancel | FE+BE |  |
| TC-GS-ROLE-54 | Auto-Revert — Confirm, access_level→null, 6 role TIDAK direset (tetap hasil edit terakhir) | P0 | E2E | TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-55 | Auto-Revert — user hilang dari Tab Total Control/Read Only secara real-time (SSE) | P2 | E2E | TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-56 | Auto-Revert — logging 4 surface (Changelog TC/RO, System Log, Activity Log, Changelog User) dgn Modified By = admin (bukan System) | P1 | E2E | TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-57 | Auto-Revert — notifikasi in-app ke target (Total Control & Read Only) | P1 | E2E | TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-58 | Auto-Revert via Remove Role Assignment — target TC/RO, dialog SAMA dengan auto-revert edit (bukan dialog Remove biasa) | P1 | E2E | TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-59 | Auto-Revert via Remove — Confirm, baris dihapus DAN access_level→null dalam 1 transaksi, role lain tidak ikut direset | P0 | E2E | TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-60 | Auto-Revert via Remove — hanya bisa disentuh Total Control (capability holder biasa tidak sampai ke opsi ini) | P0 | E2E | TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-61 | Guard — Total Control mengedit target TC/RO lain, DIIZINKAN | P0 | E2E | TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | FE+BE | ROLE-LOGIC-01: Self-edit diblokir |
| TC-GS-ROLE-62 | Guard — capability holder "Manage user and role" (non-TC) mencoba edit target TC/RO, DIBLOK | P0 | E2E | TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | FE+BE |  |
| TC-GS-ROLE-63 | Guard — Total Control mencoba edit role milik DIRI SENDIRI, DIBLOK (self-edit semua tier) | P0 | E2E | TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | FE+BE |  |
| TC-GS-ROLE-64 | Guard — capability holder non-TC mencoba edit role diri sendiri, DIBLOK | P1 | E2E | TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | FE+BE |  |
| TC-GS-ROLE-67 | Guard — Default User row Remove disabled di SEMUA role, siapa pun aktornya (termasuk Total Control) | P1 | E2E | TC-GS-ROLE-E2E-008-matriks-guard-aktor-target-self-edit-dan-target-privilese | FE+BE |  |
| TC-GS-ROLE-354 | Matriks — capability holder "Manage user and role" (Read only, TANPA Update) bisa melihat seluruh tab & data Role & Permission read-only, setara tier Read Only (gap PRD, sebelumnya cuma diuji visibilitas sidebar modul LAIN di `TC-104`, belum pernah diuji melihat modul ini sendiri) | P1 | E2E | TC-GS-ROLE-E2E-006-role-matrix-positif-total-control-dan-capability-holder | FE+BE |  |
| TC-GS-ROLE-68 | Search Name — Substring & Case-Insensitive, konsisten di 4 permukaan (Total Control, Read Only, System berbeda by Role Name, Detail) | P1 | E2E | TC-GS-ROLE-E2E-029-auto-revert-via-remove-role-assignment-single-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-127 | Siklus Interaksi Search Box Toolbar — Tab Total Control (Reveal, Auto-Focus, Submit-on-Enter, Clear via ✕, Collapse via ←) | P1 | E2E | TC-GS-ROLE-E2E-031-tabel-total-control-search-box-cycle-dan-guard-scope | FE+BE |  |
| TC-GS-ROLE-128 | Siklus Interaksi Search Box Toolbar — Tab Read Only (Reveal, Auto-Focus, Submit-on-Enter, Clear via ✕, Collapse via ←) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-129 | Siklus Interaksi Search Box Toolbar — Tab System (Reveal, Auto-Focus, Submit-on-Enter, Clear via ✕, Collapse via ←; search by Role Name) | P2 | E2E | TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | FE+BE |  |
| TC-GS-ROLE-130 | Siklus Interaksi Search Box Toolbar — Detail (Reveal, Auto-Focus, Submit-on-Enter, Clear via ✕, Collapse via ←; search di dalam daftar assignment) | P2 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-315 | Search Box Toolbar — Search Scope Exclusion (Must NOT), Kolom Last Updated dan Badge Status Tidak Ikut Ter-Search | P1 | E2E | TC-GS-ROLE-E2E-031-tabel-total-control-search-box-cycle-dan-guard-scope | FE+BE |  |
| TC-GS-ROLE-131 | Filter Single — Position (multi-select, dipilih 1 opsi) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-132 | Filter Single — Division (multi-select, dipilih 1 opsi) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-69 | Screening Struktur Filter Panel — Tab Total Control (8 field, 6 multi-select + 2 date) | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-70 | Filter — Status (Tab TC/RO): Active / Inactive (2 nilai) | P1 | E2E | TC-GS-ROLE-E2E-028-auto-revert-via-edit-crud-happy-path-pada-user-tc-dan-ro | FE+BE |  |
| TC-GS-ROLE-71 | Screening Struktur Filter Panel — Tab Read Only (8 field, 6 multi-select + 2 date) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-133 | Filter Single — Modified By (multi-select, dipilih 1 opsi) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-134 | Filter Single — Activation (curated, multi-select, dipilih 1 opsi) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-135 | Filter Single — Temporary User (curated, multi-select, dipilih 1 opsi) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-136 | Filter Single — Temporary Until (curated, date picker — tetap single value, bukan bagian retrofit multi-select) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-230 | Filter Single — Status (multi-select, dipilih 1 opsi) Tab Total Control — sebelumnya belum py TC dedicated | P1 | E2E | TC-GS-ROLE-E2E-032-tabel-total-control-filter-panel-screening-dan-filter-single | FE+BE |  |
| TC-GS-ROLE-231 | 5n Screening Isi Opsi Populate — Position/Division/Modified By (real-time update, loading state, empty source, stale reference) Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-232 | 5n Screening Isi Opsi Hardcode — Status/Activation/Temporary User (verbatim & urutan sesuai PRD) Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-233 | 5o Search-within-Dropdown & OR-Logic dalam 1 Field — Position Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-234 | 5o OR-Logic dalam 1 Field — Status Tab Total Control (2 opsi, tanpa search-within krn opsi sedikit) | P2 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-235 | 5p Chip Rendering & Removal 2-Arah (via `(X)` & via Uncheck Dropdown) & Overflow — Position Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-236 | Kondensasi 5n/5o/5p — Division/Modified By Identik Pola Position (Populate); Activation/Temporary User Identik Pola Status (Hardcode) Tab Total Control | P3 | E2E | TC-GS-ROLE-E2E-034-tabel-total-control-filter-dropdown-populate-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-138 | Filter Single — Tab Read Only (7 field, langkah eksplisit per field: 6 multi-select + 1 date picker) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-73 | Screening Struktur Filter Panel — Detail (5 field, 4 multi-select + 1 date) | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE | ROLE-LOGIC-04: Auto-revert parsial (5 role tersisa tetap utuh) |
| TC-GS-ROLE-139 | Filter Single — Position (multi-select, dipilih 1 opsi) Detail | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-140 | Filter Single — Division (multi-select, dipilih 1 opsi) Detail | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-141 | Filter Single — Activation (curated, multi-select, dipilih 1 opsi) Detail | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-142 | Filter Single — Temporary User (curated, multi-select, dipilih 1 opsi) Detail | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-143 | Filter Single — Temporary Until (curated, date picker — tetap single value) Detail | P1 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-237 | 5n/5o/5p — Detail (Position/Division populate, Activation/Temporary User hardcode, OR-logic, chip 2-arah & overflow — langkah eksplisit utk permukaan Detail) | P3 | E2E | TC-GS-ROLE-E2E-041-detail-table-tools-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-338 | Filter Single — Last Updated (date picker, pilih 1 hari saja = start & end tanggal yang sama) Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-033-tabel-total-control-filter-date-last-updated | FE+BE |  |
| TC-GS-ROLE-339 | Filter Range — Last Updated (beberapa hari, inklusif kedua ujung) Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-033-tabel-total-control-filter-date-last-updated | FE+BE |  |
| TC-GS-ROLE-340 | Filter Single — Last Updated (pilih 1 hari saja = start & end tanggal yang sama) Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-145 | Kombinasi Multi-Field Filter (AND) — Position + Status (Tab Total Control) | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-146 | Alur Search → Filter — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-147 | Alur Filter → Search — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-148 | Kombinasi Penuh 4 Kontrol — Search + Filter + Sort + Pagination (Tab Total Control) | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-149 | Clear Filter saat Search & Sort aktif — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-150 | Clear Search saat Filter & Sort aktif — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-151 | Transisi Target Sort saat Search & Filter aktif — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-152 | Pemulihan Empty State (Recovery) — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-153 | Retensi Seleksi Checkbox saat Search/Filter aktif — Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-035-tabel-total-control-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-154 | Kombinasi & Alur Search↔Filter — Tab Read Only (langkah eksplisit: Search→Filter, Filter→Search, Kombinasi Penuh, Clear, Recovery) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-155 | Kombinasi Multi-Field Filter (AND) — Position + Activation (Detail) | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-156 | Alur Search → Filter — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-157 | Alur Filter → Search — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-158 | Kombinasi Penuh 4 Kontrol — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-159 | Clear Filter saat Search & Sort aktif — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-160 | Clear Search saat Filter & Sort aktif — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-161 | Transisi Target Sort saat Search & Filter aktif — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-162 | Pemulihan Empty State (Recovery) — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-163 | Retensi Seleksi Checkbox (bulk) saat Search/Filter aktif — Detail | P2 | E2E | TC-GS-ROLE-E2E-042-detail-table-tools-kombinasi-search-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-72 | Sorting 3-State — kolom Name (default sort, Tab Total Control) & Guard Tab System Tidak Sortable | P1 | E2E | TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | FE+BE |  |
| TC-GS-ROLE-164 | Sorting 3-State — kolom Position (Tab Total Control), Default User selalu di akhir (ascending) | P1 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-165 | Sorting 3-State — kolom Division (Tab Total Control), Default User di akhir | P1 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-166 | Sorting 3-State — kolom Status (boolean Active First/Inactive First, Tab Total Control) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-167 | Sorting 3-State — kolom Modified By (by nama lengkap underlying, Default User di akhir) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-168 | Sorting 3-State — kolom Last Updated (Newest/Oldest First, Default User di akhir) | P1 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-169 | Sorting 3-State — kolom Activation Status (curated, A-Z) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-170 | Sorting 3-State — kolom Temporary User (boolean Yes First/No First) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-171 | Sorting 3-State — kolom Temporary Until (ascending=paling dekat expired, kosong di akhir) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-172 | Sorting 3-State — kolom TAG (A-Z by kode, kosong di akhir) | P2 | E2E | TC-GS-ROLE-E2E-036-tabel-total-control-sorting-3-state-10-kolom | FE+BE |  |
| TC-GS-ROLE-174 | Sorting 3-State — kolom Name (default sort, Tab Read Only; kolom lain pada Tab RO mengikuti pola Tab Total Control — lihat Gap Spec) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-175 | Sorting 3-State — kolom Position (Detail), Default User selalu di akhir (ascending) | P1 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-176 | Sorting 3-State — kolom Division (Detail), Default User di akhir | P1 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-177 | Sorting 3-State — kolom Activation Status (curated, A-Z, Detail) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-178 | Sorting 3-State — kolom Temporary User (boolean Yes First/No First, Detail) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-179 | Sorting 3-State — kolom Temporary Until (ascending=paling dekat expired, kosong di akhir, Detail) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-180 | Sorting 3-State — kolom TAG (A-Z by kode, kosong di akhir, Detail) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-183 | Setup Column — Screening Overlay Tab Total Control (10 kolom Hideable/Curated) | P1 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-250 | Setup Column — Screening Popup Modal & Live Preview Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-251 | Kolom `Name` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-252 | Kolom `Position` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-253 | Kolom `Division` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-254 | Kolom `Status` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-255 | Kolom `Modified By` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-256 | Kolom `Last Updated` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-258 | Kolom `Activation Status` (☐ Curated) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-259 | Kolom `Temporary User` (☐ Curated) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-260 | Kolom `Temporary Until` (☐ Curated) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-261 | Kolom `TAG` (☐ Curated) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-263 | Kolom `Name` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-264 | Kolom `Position` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-265 | Kolom `Division` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-266 | Kolom `Status` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-267 | Kolom `Modified By` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-268 | Kolom `Last Updated` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-270 | Kolom `Activation Status` (☐ Curated) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-271 | Kolom `Temporary User` (☐ Curated) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-272 | Kolom `Temporary Until` (☐ Curated) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-273 | Kolom `TAG` (☐ Curated) — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-275 | Kolom `Name` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-276 | Kolom `Position` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-277 | Kolom `Division` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-278 | Kolom `Status` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-279 | Kolom `Modified By` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-280 | Kolom `Last Updated` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-282 | Kolom `Activation Status` (☐ Curated) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-283 | Kolom `Temporary User` (☐ Curated) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-284 | Kolom `Temporary Until` (☐ Curated) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-285 | Kolom `TAG` (☐ Curated) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-287 | Tombol `[Reset to Default]` Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-288 | Tombol `[Cancel]`/Icon Silang `(X)` — Discard Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-184 | Setup Column — Tab Read Only (cache terpisah dari Tab Total Control) | P2 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-185 | Setup Column — Tab System (Role Name & Users, keduanya Hideable) | P2 | E2E | TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | FE+BE |  |
| TC-GS-ROLE-186 | Setup Column — Detail (Name/Position/Division Hideable; kolom CRUD dinamis selalu tampil, bukan kolom data; 5 curated) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-74 | Download — per tab/halaman, filename berbeda tiap permukaan | P1 | E2E | TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | FE+BE | ROLE-LOGIC-04: Auto-revert parsial (5 role tersisa tetap utuh) |
| TC-GS-ROLE-75 | Download — Gagal | P2 | E2E | TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-346 | Download per-tab — Tab Total Control (format menu CSV/XLSX, filename, konten) | P1 | E2E | TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-347 | Download per-tab — Tab Read Only (format menu CSV/XLSX, filename, konten) | P1 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-348 | Download per-tab — Tab System (6 baris role fixed) | P2 | E2E | TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | FE+BE |  |
| TC-GS-ROLE-349 | Download per-tab — Detail (filename pakai nama role aktual) | P1 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-76 | Pagination — Default, Navigasi, Persist page size — per permukaan | P1 | E2E | TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-334 | Pagination — Opsi Page Size 10/25/50/100 (dropdown persis, 100 maks tanpa "All", render baris tepat, input nomor halaman langsung) — Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-038-tabel-total-control-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-335 | Pagination — Opsi Page Size 10/25/50/100 — Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-336 | Pagination — Opsi Page Size 10/25/50/100 — Detail | P1 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-337 | Pagination — Tab System: 6 baris fixed, TIDAK ada kontrol pagination (negative) | P1 | E2E | TC-GS-ROLE-E2E-040-tabel-system-screening-search-download-dan-guard-non-table-tools | FE+BE |  |
| TC-GS-ROLE-77 | Hover — avatar bundled Name, badge Status, teks ter-truncate (termasuk nama user panjang: wrap natural + tooltip nama lengkap) | P2 | E2E | TC-GS-ROLE-E2E-030-tabel-total-control-hover-truncation-dan-wrap-nama-panjang | mock |  |
| TC-GS-ROLE-78 | Screening 3 Zona — Changelog Tab Total Control (`Assign`/`Remove`/`Auto-Revert Total Control`) | P0 | E2E | TC-GS-ROLE-E2E-044-changelog-total-control-screening-empty-state-dan-hover | FE+BE |  |
| TC-GS-ROLE-79 | Changelog Tab Read Only — struktur identik, Field value `Read Only` | P1 | E2E | TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download | FE+BE |  |
| TC-GS-ROLE-80 | Changelog Tab System — SUPERSET semua role, kolom `Role — User` gabungan | P1 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-81 | Changelog Detail — judul dinamis pakai nama role aktual; kolom Object TETAP gabungan `Role — User` (Must NOT hanya `User Name`) meski modal sudah di-scope ke 1 role | P1 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-82 | Changelog System — bulk-write Assign Total Control TIDAK menghasilkan entry per-role sama sekali (baik baris baru maupun existing) — melengkapi `TC-17` | P1 | E2E | TC-GS-ROLE-E2E-010-assign-total-control-happy-path-shortcut-bulk-write | FE+BE | role.md §8.3/§8.7: Bulk-write shortcut 0 log di Changelog System |
| TC-GS-ROLE-83 | Changelog System — bulk-delete Remove Total Control TIDAK menghasilkan entry per-role sama sekali (Remove tetap menghapus 6 baris, tapi 0 log di §8.3) | P1 | E2E | TC-GS-ROLE-E2E-012-remove-total-control-happy-path-dan-bulk-delete-6-role | FE+BE | role.md §8.3/§8.7: Bulk-write shortcut 0 log di Changelog System |
| TC-GS-ROLE-84 | Changelog — aggregate `Changelog: User` TIDAK ikut menampilkan 6 baris cascade, tetap 1 baris `Field=Access Level` | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-85 | Screening Struktur Filter Panel — Modal Changelog Total Control (3 field) | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-187 | Search per Kolom Modal Changelog Total Control — Action/User Name/Field/Old Value/New Value/Modified By (Substring & Case-Insensitive) | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-188 | Guard Kolom Non-Searchable Modal Changelog Total Control — Date | P2 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-189 | Siklus Interaksi Search Box Toolbar — Modal Changelog Total Control (Reveal, Auto-Focus, Submit-on-Enter, Clear via ✕, Collapse via ←) | P2 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-190 | Filter Modal Changelog Total Control by Action | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-191 | Filter Modal Changelog Total Control by User Name | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-192 | Filter Modal Changelog Total Control by Modified By | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-341 | Filter Modal Changelog Total Control by Date — pilih 1 hari saja (start = end) | P1 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-342 | Filter Modal Changelog Total Control by Date — range beberapa hari (inklusif ujung) | P2 | E2E | TC-GS-ROLE-E2E-045-changelog-total-control-search-box-cycle-dan-filter-panel | FE+BE |  |
| TC-GS-ROLE-193 | Kombinasi Multi-Field Filter (AND) Modal Changelog Total Control — Action + Modified By | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-194 | Alur Search → Filter Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-195 | Alur Filter → Search Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-196 | Kombinasi Penuh 4 Kontrol Modal Changelog Total Control — Search+Filter+Sort+Pagination | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-197 | Clear Filter saat Search & Sort aktif Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-198 | Clear Search saat Filter & Sort aktif Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-199 | Transisi Target Sort saat Search & Filter aktif Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-200 | Pemulihan Empty State (Recovery) Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-047-changelog-total-control-kombinasi-multi-filter-dan-recovery | FE+BE |  |
| TC-GS-ROLE-201 | Sorting 3-State — kolom Date (default sort, Modal Changelog Total Control) | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-202 | Sorting 3-State — kolom Action (Modal Changelog Total Control) | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-203 | Sorting 3-State — kolom User Name (Modal Changelog Total Control) | P2 | E2E | TC-GS-ROLE-E2E-037-tabel-total-control-setup-column-fase-1-2-3 | mock |  |
| TC-GS-ROLE-204 | Sorting 3-State — kolom Field (Modal Changelog Total Control) | P3 | E2E | TC-GS-ROLE-E2E-039-tabel-read-only-search-filter-sort-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-205 | Sorting 3-State — kolom Old Value (kolom campuran, kosong di akhir) | P2 | E2E | TC-GS-ROLE-E2E-043-detail-table-tools-sorting-setup-column-download-dan-pagination | FE+BE |  |
| TC-GS-ROLE-206 | Sorting 3-State — kolom New Value (kolom campuran, kosong di akhir) | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-207 | Sorting 3-State — kolom Modified By (Modal Changelog Total Control) | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-208 | Setup Column Modal Changelog Total Control — Screening Overlay 7 Kolom | P1 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-289 | Setup Column Modal Changelog Total Control — Screening Popup Modal & Live Preview | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-290 | Kolom `Date` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-291 | Kolom `Action` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-292 | Kolom `Name` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-293 | Kolom `Field` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-294 | Kolom `Old Value` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-295 | Kolom `New Value` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-296 | Kolom `Modified By` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-297 | Kolom `Date` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-298 | Kolom `Action` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-299 | Kolom `Name` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-300 | Kolom `Field` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-301 | Kolom `Old Value` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-302 | Kolom `New Value` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-303 | Kolom `Modified By` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-304 | Kolom `Date` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-305 | Kolom `Action` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-306 | Kolom `Name` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-307 | Kolom `Field` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-308 | Kolom `Old Value` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-309 | Kolom `New Value` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-310 | Kolom `Modified By` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-311 | Tombol `[Reset to Default]` Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-312 | Tombol `[Cancel]`/Icon Silang `(X)` Modal Changelog Total Control — Discard | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-209 | Hover — Modified By & sel ter-truncate Modal Changelog Total Control | P2 | E2E | TC-GS-ROLE-E2E-044-changelog-total-control-screening-empty-state-dan-hover | FE+BE |  |
| TC-GS-ROLE-210 | Download Modal Changelog Total Control — CSV/XLSX & Gagal | P2 | E2E | TC-GS-ROLE-E2E-048-changelog-total-control-sorting-setup-column-dan-download | mock |  |
| TC-GS-ROLE-350 | Download Modal Changelog Read Only — per-tab, format menu CSV/XLSX, filename & konten | P2 | E2E | TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download | FE+BE |  |
| TC-GS-ROLE-351 | Download Modal Changelog System — per-tab, format menu CSV/XLSX, filename & konten | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-352 | Download Modal Changelog Detail — per-tab, format menu CSV/XLSX, filename (nama role aktual) & konten | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-211 | Screening Isi Opsi Filter Modal Changelog Total Control — Action populate dari data tabel (bukan hardcode varian "via" yang tidak pernah ditulis, `role.md` §8.3/`prd-conventions.md` §9.8) & Populate User Name/Modified By scoped ke Changelog, BUKAN live-join ke master data | P2 | E2E | TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-212 | Populate Dropdown User Name/Modified By — Real-time Update, Loading State, Empty Source, Stale Reference | P2 | E2E | TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-213 | Search-within-Dropdown & Logika OR-dalam-Field Modal Changelog Total Control (Action/User Name/Modified By) | P2 | E2E | TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-214 | Chip di Dalam Field, Removal via `(X)`, & Overflow Modal Changelog Total Control (Action/User Name/Modified By) | P2 | E2E | TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-226 | Removal via Uncheck Checkbox di DALAM Dropdown Terbuka Field Action — Arah Sebaliknya dari `(X)` (Modal Changelog Total Control) | P2 | E2E | TC-GS-ROLE-E2E-046-changelog-total-control-filter-dropdown-search-dan-chip-cycles | FE+BE |  |
| TC-GS-ROLE-215 | Modal Changelog Read Only — Search Box Cycle, Filter by Action, Sort Date, Setup Column, Hover (langkah eksplisit per varian; Download diuji dedicated `TC-350`) | P2 | E2E | TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download | FE+BE |  |
| TC-GS-ROLE-345 | Filter Modal Changelog Read Only by Date — pilih 1 hari saja (start = end) | P1 | E2E | TC-GS-ROLE-E2E-049-changelog-read-only-screening-search-filter-dan-download | FE+BE |  |
| TC-GS-ROLE-216 | Filter Modal Changelog System by Role (unik permukaan ini) | P1 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-217 | Filter Modal Changelog System by Action/User Name/Field/Modified By (4 field lain) | P1 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-343 | Filter Modal Changelog System by Date — pilih 1 hari saja (start = end) | P1 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-218 | Sorting 3-State — kolom Date (default sort, Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-238 | Sorting 3-State — kolom Action (Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-239 | Sorting 3-State — kolom Role — User (sort by underlying identifier gabungan, Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-240 | Sorting 3-State — kolom Field (Modal Changelog System) | P3 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-241 | Sorting 3-State — kolom Old Value (kolom campuran, kosong di akhir, Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-242 | Sorting 3-State — kolom New Value (kolom campuran, kosong di akhir, Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-243 | Sorting 3-State — kolom Modified By (Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-219 | 5n/5o/5p Modal Changelog System — Hardcode Action/Role & Populate User Name/Modified By, Search-within-Dropdown, OR-Logic, Chip Removal | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-227 | Removal via Uncheck Checkbox di DALAM Dropdown Terbuka Field Action — Arah Sebaliknya dari `(X)` (Modal Changelog System) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-220 | Modal Changelog System — Search Box Cycle, Filter by Role, Kombinasi/Alur, Sort Date, Setup Column, Hover (langkah eksplisit per varian; Download diuji dedicated `TC-351`) | P2 | E2E | TC-GS-ROLE-E2E-050-changelog-system-screening-filter-role-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-221 | Filter Modal Changelog Detail by Field — opsi DINAMIS mengikuti CRUD applicable role ini | P1 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-222 | Filter Modal Changelog Detail by Action/User Name/Modified By (3 field lain) | P1 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-344 | Filter Modal Changelog Detail by Date — pilih 1 hari saja (start = end) | P1 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-223 | Sorting 3-State — kolom Date (default sort, Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-244 | Sorting 3-State — kolom Action (Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-245 | Sorting 3-State — kolom `Role — User` (Modal Changelog Detail), prefix role konstan jadi urutan efektif sama dgn sort by user name | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-246 | Sorting 3-State — kolom Field (A-Z dari subset dinamis role ini, Modal Changelog Detail) | P3 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-247 | Sorting 3-State — kolom Old Value (kolom campuran, kosong di akhir, Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-248 | Sorting 3-State — kolom New Value (kolom campuran, kosong di akhir, Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-249 | Sorting 3-State — kolom Modified By (Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-224 | 5n/5o/5p Modal Changelog Detail — Hardcode Action & Populate User Name/Modified By/Field-dinamis, Search-within-Dropdown, OR-Logic, Chip Removal | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-228 | Removal via Uncheck Checkbox di DALAM Dropdown Terbuka Field Action — Arah Sebaliknya dari `(X)` (Modal Changelog Detail) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-225 | Modal Changelog Detail — Search Box Cycle, Filter by Field dinamis, Kombinasi/Alur, Sort Date, Setup Column, Hover (langkah eksplisit per varian; Download diuji dedicated `TC-352`) | P2 | E2E | TC-GS-ROLE-E2E-051-changelog-detail-screening-filter-field-dinamis-sorting-7-kolom-dan-download | FE+BE |  |
| TC-GS-ROLE-116 | Empty State — Modal Changelog genuinely kosong & Search/Filter tanpa hasil (keempat varian) | P1 | E2E | TC-GS-ROLE-E2E-044-changelog-total-control-screening-empty-state-dan-hover | FE+BE |  |
| TC-GS-ROLE-86 | System Log aktor — mencatat aksi Assign/Remove/Edit/Auto-Revert dari sisi ADMIN yang melakukan (bukan target) | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-87 | Activity Log — mencatat seluruh 5 varian Action (Assign/Remove/Edit/Auto-Revert Total Control/Auto-Revert Read Only, §8.6 — bukan 8 varian "via" yang sudah dikonfirmasi tidak pernah ditulis, §8.3/§8.7) dgn Modified By | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-88 | Sinkronisasi — Edit CRUD & Remove (Detail) tercatat DUA surface User: Changelog User aggregate DAN Changelog User > Tab Role | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-322 | Changelog Tab Total Control — Assign (plain) mencatat Field Access Level | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-323 | Changelog Tab Total Control — Remove (plain) mencatat Field Access Level | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-324 | Changelog Tab Read Only — Assign (plain) mencatat Field Access Level | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-325 | Changelog Tab Read Only — Remove (plain) mencatat Field Access Level | P1 | E2E | TC-GS-ROLE-E2E-052-audit-logging-3-surface-dan-verifikasi-baris-kanonik | FE+BE |  |
| TC-GS-ROLE-326 | Changelog Detail — Edit CRUD toggle mencatat Field=[nama kolom]/Old/New (contoh Update, berlaku simetris Create/Delete — Read TIDAK applicable, checkbox selalu locked/tidak pernah ditoggle via UI, lihat Gap Spec) | P1 | E2E | TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save | FE+BE | ROLE-LOGIC-05: Read checkbox locked disabled |
| TC-GS-ROLE-327 | Changelog Detail — Remove (plain, single) mencatat Field Access | P1 | E2E | TC-GS-ROLE-E2E-023-detail-remove-single-happy-path-dan-penurunan-counter | FE+BE |  |
| TC-GS-ROLE-328 | Changelog Detail — Edit CRUD toggle Delete mencatat Field=Delete/Old/New (melengkapi `TC-326` yang cuma Update; Create/Delete sebelumnya cuma diasumsikan "simetris" tanpa dibuktikan — preseden `testcase-conventions.md` §P3b-2) | P1 | E2E | TC-GS-ROLE-E2E-017-detail-crud-checkbox-screening-read-locked-dan-auto-save | FE+BE |  |
| TC-GS-ROLE-329 | Changelog System — bulk-write Assign Read Only TIDAK menghasilkan entry per-role sama sekali (melengkapi `TC-82` yang tier Total Control — membuktikan Read Only genuinely sama, bukan cuma diasumsikan "kondensasi") | P1 | E2E | TC-GS-ROLE-E2E-014-assign-read-only-happy-path-screening-dan-filter-kelayakan | FE+BE | role.md §8.3/§8.7: Bulk-write shortcut 0 log di Changelog System |
| TC-GS-ROLE-330 | Changelog System — bulk-delete Remove Read Only TIDAK menghasilkan entry per-role sama sekali (melengkapi `TC-83`) | P1 | E2E | TC-GS-ROLE-E2E-015-remove-read-only-happy-path-dialog-cancel-dan-guard-proteksi | FE+BE | role.md §8.3/§8.7: Bulk-write shortcut 0 log di Changelog System |
| TC-GS-ROLE-101 | Date/Time/Timezone — kolom Last Updated di keempat permukaan & Modal Changelog | P1 | E2E | TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE |  |
| TC-GS-ROLE-102 | Sinkronisasi Dua Arah — edit CRUD dari Detail langsung tercermin di `User Detail > Tab Role`, dan sebaliknya | P1 | E2E | TC-GS-ROLE-E2E-053-sinkronisasi-dua-arah-tab-role-detail-user-dan-format-datetime | FE+BE |  |
| TC-GS-ROLE-103 | Sinkronisasi — Remove Access "Global Settings" di modul User men-cascade hapus semua role assignment (Role & Permission menerima, bukan menginisiasi) | P1 | E2E | TC-GS-ROLE-E2E-053-sinkronisasi-dua-arah-tab-role-detail-user-dan-format-datetime | FE+BE |  |
| TC-GS-ROLE-104 | Sinkronisasi — Sidebar Enforcement, modul GS yang role-nya tidak di-Read hidden/disabled | P1 | E2E | TC-GS-ROLE-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE |  |
| TC-GS-ROLE-105 | Sinkronisasi — perubahan permission TIDAK surut ke sesi aktif, berlaku next request | P2 | E2E | TC-GS-ROLE-E2E-053-sinkronisasi-dua-arah-tab-role-detail-user-dan-format-datetime | FE+BE |  |
| TC-GS-ROLE-108 | Tenant Isolation — akses konfigurasi role client lain | P0 | E2E | TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi | FE+BE | role.md §4.1: Isolasi multi-tenant data role |
| TC-GS-ROLE-109 | Sanitasi Input — payload SQL Injection pada Search box | P1 | E2E | TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi | FE+BE |  |
| TC-GS-ROLE-316 | Event Notification Guard — Global Settings Tidak Memiliki Event "Group Manager" (Khusus Admin Console, Must NOT) | P2 | E2E | TC-GS-ROLE-E2E-054-security-tenant-isolation-sanitasi-input-dan-guard-notifikasi | FE+BE |  |
| TC-GS-ROLE-110 | D1 — Client suspended/expired memblokir semua aksi tulis | P1 | E2E | TC-GS-ROLE-E2E-018-detail-crud-checkbox-write-failure-dan-debounce | mock |  |
| TC-GS-ROLE-111 | D6 — Concurrent Edit CRUD, 2 admin mengedit baris role sama | P1 | E2E | TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove | mock |  |
| TC-GS-ROLE-112 | D6 — Double-submit Assign/Remove/Edit CRUD (actor sama) | P1 | E2E | TC-GS-ROLE-E2E-055-entitas-suspended-expired-dan-integritas-unique-constraint | mock |  |
| TC-GS-ROLE-113 | D9 — Unique constraint, 1 user tidak bisa punya >2 baris role yang sama (DB enforce) | P2 | E2E | TC-GS-ROLE-E2E-055-entitas-suspended-expired-dan-integritas-unique-constraint | mock |  |
| TC-GS-ROLE-317 | 8b-1: Cross-action race — Assign Total Control vs Edit CRUD cell individual (role sama) bersamaan (2 aktor) | P2 | E2E | TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove | mock |  |
| TC-GS-ROLE-318 | 8b-1: Cross-action race — Assign Total Control vs Remove Total Control pada target yang sama bersamaan (2 aktor) | P2 | E2E | TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove | mock |  |
| TC-GS-ROLE-319 | 8b-1: Cross-action race — Edit CRUD trigger Auto-Revert vs Remove Role Assignment trigger Auto-Revert, baris berbeda milik target sama (2 aktor) | P2 | E2E | TC-GS-ROLE-E2E-056-cross-action-race-concurrency-assign-edit-dan-remove | mock |  |

---

## 4. Ringkasan Coverage & Matriks Statistik

| Parameter | Nilai | Keterangan |
|---|:---:|---|
| **Total TC Granular di `tc-role.md`** | 357 | Termasuk 34 nomor dicabut/non-E2E |
| **Total TC Aktif (Scope E2E)** | **323** | 100% tercakup ke dalam Spec E2E |
| **Total Spec E2E Dibuat** | **56** | Mengikuti konvensi TestSpectra `TC-GS-ROLE-E2E-*` |
| **Spec Mode FE+BE** | 43 | Dijalankan terhadap backend nyata dengan database seeding |
| **Spec Mode Mock** | 13 | UI-only, resiliency 500/timeout, dan simulasi konkurensi/race |
| **Persentase Cakupan E2E** | **100.0%** | Tidak ada TC aktif yang terlewat (0 gaps) |
| **Status Validasi TestSpectra Linter** | **PASS** | `0 lint errors found` (Strict schema verified) |
