# Coverage E2E — Global Settings > Role & Permission

Sumber: `global-settings/role/TestCases/tc-role.md`.
Referensi kontrak: `global-settings/role/PRD/role.md` dan `global-settings/role/API/openapi.yaml`.
Suite: `specs/GlobalSettings/Role/`.
Prefix Modul: `GS` + `ROLE` (`TC-GS-ROLE-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-role.md`: 305 baris (`TC-GS-ROLE-1` s.d. `TC-GS-ROLE-305`).**
Cakupan otomasi spec E2E: **100% (305 dari 305 TC tercakup penuh tanpa celah)**.
Total Spec E2E yang dihasilkan: **97 spec atomik terisolasi tinggi**.

---

## 1. Pemetaan TC Granular → Spec E2E (97 spec)

Seluruh 305 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal | Screening Halaman Role & Permission Tab Total Control, Default Sort Name A-Z, dan Nilai Baris Default User | FE+BE | TC-GS-ROLE-1, TC-GS-ROLE-10, TC-GS-ROLE-20, TC-GS-ROLE-24 |
| TC-GS-ROLE-E2E-002-screening-tab-read-only-dan-empty-state | Screening Tab Read Only, Eksklusi Default User, dan Empty State Saat Tanpa User Read Only | FE+BE | TC-GS-ROLE-2, TC-GS-ROLE-11, TC-GS-ROLE-18 |
| TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | Screening Tab System, 6 Role Alfabetis, Hitungan Users, Hover Link, dan Navigasi Detail | FE+BE | TC-GS-ROLE-3, TC-GS-ROLE-6, TC-GS-ROLE-7, TC-GS-ROLE-8, TC-GS-ROLE-9, TC-GS-ROLE-14 |
| TC-GS-ROLE-E2E-004-screening-detail-role-dan-kolom-crud-enam-role | Screening Halaman Detail Role, Deskripsi dan Kolom CRUD Dinamis untuk 6 Role Sistem | FE+BE | TC-GS-ROLE-4, TC-GS-ROLE-5, TC-GS-ROLE-281 |
| TC-GS-ROLE-E2E-005-badge-kondisional-pending-activation-lintas-surface | Tampilan Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Picker | FE+BE | TC-GS-ROLE-12, TC-GS-ROLE-13 |
| TC-GS-ROLE-E2E-006-loading-skeleton-dan-error-load-resilience | Tampilan Loading State dan Pemulihan Error Load 500 via Tombol Try Again di Seluruh Surface | mock | TC-GS-ROLE-15, TC-GS-ROLE-16, TC-GS-ROLE-17 |
| TC-GS-ROLE-E2E-007-empty-state-pencarian-no-results-found | Empty State Hasil Pencarian No Results Found pada Tab Total Control, Read Only, System, dan Detail | FE+BE | TC-GS-ROLE-19 |
| TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-aktivasi-akses | Landing State Halaman Global Settings User Tanpa Role dan Transisi Pemunculan Menu Pasca-Assign | FE+BE | TC-GS-ROLE-21, TC-GS-ROLE-22, TC-GS-ROLE-282 |
| TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | Hover Tooltip Toolbar Table Tools dan Tooltip Nama Lengkap Kolom Modified By | mock | TC-GS-ROLE-23, TC-GS-ROLE-25 |
| TC-GS-ROLE-E2E-010-guided-tooltip-walkthrough-auto-launch-dan-navigasi | Guided Tooltip Walkthrough: Auto-Launch Kunjungan Pertama, Langkah 1-3, dan Penutupan Done | FE+BE | TC-GS-ROLE-26, TC-GS-ROLE-27, TC-GS-ROLE-28 |
| TC-GS-ROLE-E2E-011-guided-tooltip-walkthrough-skip-replay-exit-keyboard | Guided Tooltip Walkthrough: Tombol Skip, Replay via [?], Pembatalan Exit Interruption, dan Navigasi Keyboard | FE+BE | TC-GS-ROLE-29, TC-GS-ROLE-30, TC-GS-ROLE-31 |
| TC-GS-ROLE-E2E-012-mobile-gesture-multi-select-dan-bulk-remove | Gesture Layar Sentuh Mobile Android: Long-Press Multi-Select dan Aksi Bulk Remove pada Detail | FE+BE | TC-GS-ROLE-32 |
| TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar | Tampilan Mobile Android: Card List Tab TC/RO/System, Bottom Sheet Picker/Changelog, dan Toolbar Mobile | FE+BE | TC-GS-ROLE-285, TC-GS-ROLE-286, TC-GS-ROLE-287, TC-GS-ROLE-288 |
| TC-GS-ROLE-E2E-014-sidebar-menu-visibility-per-role-dan-direct-url-guard | Visibilitas Menu Role & Permission pada Sidebar per Peran dan Penolakan Akses Direct URL 403 | FE+BE | TC-GS-ROLE-33, TC-GS-ROLE-34, TC-GS-ROLE-35 |
| TC-GS-ROLE-E2E-015-role-matrix-ui-visibility-aktor-total-control-dan-read-only | Role Matrix: UI Visibility Aktor Total Control, Read Only, dan Manage User and Role Read Saja | FE+BE | TC-GS-ROLE-36, TC-GS-ROLE-37, TC-GS-ROLE-38 |
| TC-GS-ROLE-E2E-016-role-matrix-ui-visibility-aktor-manage-user-and-role | Role Matrix: UI Visibility Aktor Manage User and Role Tanpa Update vs Berhak Update | FE+BE | TC-GS-ROLE-39, TC-GS-ROLE-40 |
| TC-GS-ROLE-E2E-017-guard-proteksi-default-user-dan-self-edit-pada-detail | Guard Proteksi Default User dan Self-Edit pada Halaman Detail: Checkbox dan Aksi Remove Disabled | FE+BE | TC-GS-ROLE-41, TC-GS-ROLE-42, TC-GS-ROLE-45 |
| TC-GS-ROLE-E2E-018-guard-proteksi-checkbox-read-dan-prioritas-tooltip | Guard Proteksi Checkbox Read Selalu Checked & Disabled, Serta Prioritas Tooltip Elemen Non-Aktif | FE+BE | TC-GS-ROLE-43, TC-GS-ROLE-44, TC-GS-ROLE-46 |
| TC-GS-ROLE-E2E-019-aksesibilitas-keyboard-dan-fokus-dialog | Aksesibilitas Antarmuka: Navigasi Keyboard Tab + Space Sel CRUD dan Focus Trap Modal Dialog | FE+BE | TC-GS-ROLE-47, TC-GS-ROLE-48 |
| TC-GS-ROLE-E2E-020-gating-seleksi-bulk-action-bar-per-aktor | Gating Seleksi Checkbox Baris Bulk Action Bar pada Detail Berdasarkan Tingkat Wewenang Aktor | FE+BE | TC-GS-ROLE-49, TC-GS-ROLE-50 |
| TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | Screening Modal Table User Picker Assign Total Control, Kelayakan Pool, dan Ketiadaan Column Visibility | FE+BE | TC-GS-ROLE-51, TC-GS-ROLE-52, TC-GS-ROLE-53, TC-GS-ROLE-54, TC-GS-ROLE-76 |
| TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | Interaksi Modal Picker Assign Total Control: Seleksi Multi-User, Validasi Kosong, Focus Trap, dan Dialog D-01 | FE+BE | TC-GS-ROLE-55, TC-GS-ROLE-56, TC-GS-ROLE-57, TC-GS-ROLE-61, TC-GS-ROLE-62, TC-GS-ROLE-77 |
| TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | Pencarian Modal Picker Assign Total Control: Empty States, Substring Name/Email/Position/Division, dan Scoping Kolom Hidden | FE+BE | TC-GS-ROLE-68, TC-GS-ROLE-69, TC-GS-ROLE-70, TC-GS-ROLE-71, TC-GS-ROLE-72 |
| TC-GS-ROLE-E2E-024-assign-total-control-picker-filter-panel-multi-kriteria | Penyaringan Filter Panel Modal Picker Assign Total Control: Position, Division, Status, Activation Status, Temporary, dan Custom Field | FE+BE | TC-GS-ROLE-73, TC-GS-ROLE-74 |
| TC-GS-ROLE-E2E-025-assign-total-control-picker-sorting-pagination-retensi | Pengurutan 3-State 5 Kolom, Paginasi 10/25/50/100, dan Retensi Seleksi Lintas Halaman pada Picker Assign Total Control | FE+BE | TC-GS-ROLE-75, TC-GS-ROLE-293 |
| TC-GS-ROLE-E2E-026-assign-total-control-happy-path-single-dan-multi-user | Penugasan Total Control Berhasil untuk User Tunggal dan Multi-User Serta Refleksi Rename User Sesi B | FE+BE | TC-GS-ROLE-58, TC-GS-ROLE-59, TC-GS-ROLE-67 |
| TC-GS-ROLE-E2E-027-assign-total-control-upgrade-dari-read-only | Peningkatan Hak Akses User dari Read Only Menjadi Total Control: Pemindahan Tab dan Tanpa Duplikasi Log | FE+BE | TC-GS-ROLE-60 |
| TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10 | Validasi Stale User (V-10) pada Assign Total Control: Penanganan Kandidat Dihapus atau Di-Assign Sesi Lain (Alert Tunggal & Jamak) | FE+BE | TC-GS-ROLE-63, TC-GS-ROLE-66, TC-GS-ROLE-300, TC-GS-ROLE-304 |
| TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran | Validasi User Tidak Eligible (V-11) dan Penanganan Campuran V-10 + V-11 pada Assign Total Control | FE+BE | TC-GS-ROLE-292, TC-GS-ROLE-301, TC-GS-ROLE-302, TC-GS-ROLE-305 |
| TC-GS-ROLE-E2E-030-assign-total-control-resilience-server-500-dan-double-submit | Ketahanan Form Assign Total Control: Guard Double-Submit dan Penanganan Error Server 500 | mock | TC-GS-ROLE-64, TC-GS-ROLE-65 |
| TC-GS-ROLE-E2E-031-assign-read-only-screening-dan-pool-eligibility | Screening Modal Assign Read Only, Validasi Kelayakan Pool, dan Validasi Seleksi Kosong | FE+BE | TC-GS-ROLE-78, TC-GS-ROLE-79, TC-GS-ROLE-82 |
| TC-GS-ROLE-E2E-032-assign-read-only-happy-path-single-user | Penugasan Read Only Berhasil untuk User Tunggal: Refleksi Tab Read Only dan Pencatatan Log | FE+BE | TC-GS-ROLE-80 |
| TC-GS-ROLE-E2E-033-assign-read-only-validasi-stale-user-v10 | Validasi Stale User V-10 pada Penugasan Read Only: Penolakan Alert Inline Saat Kandidat Dihapus Sesi Lain | FE+BE | TC-GS-ROLE-81 |
| TC-GS-ROLE-E2E-034-assign-read-only-resilience-server-500 | Ketahanan Form Assign Read Only: Penanganan Kegagalan Jaringan Error Server 500 | mock | TC-GS-ROLE-83 |
| TC-GS-ROLE-E2E-035-remove-total-control-screening-dialog-dan-batal | Screening Dialog Konfirmasi Remove Total Control (D-01) dan Pembatalan via Tombol Cancel | FE+BE | TC-GS-ROLE-84, TC-GS-ROLE-85 |
| TC-GS-ROLE-E2E-036-remove-total-control-happy-path-dan-user-inactive | Pencabutan Total Control Berhasil pada User Aktif dan User Inactive Tanpa Batasan Kuota Minimum | FE+BE | TC-GS-ROLE-86, TC-GS-ROLE-87 |
| TC-GS-ROLE-E2E-037-remove-read-only-happy-path-single-user | Pencabutan Read Only Berhasil pada User Aktif: Pembersihan Hak Akses dan Pencatatan Log | FE+BE | TC-GS-ROLE-88 |
| TC-GS-ROLE-E2E-038-remove-access-level-resilience-server-500-dan-double-submit | Ketahanan Dialog Remove Total Control & Read Only: Penanganan Server 500 dan Guard Klik Ganda Cepat | mock | TC-GS-ROLE-89, TC-GS-ROLE-90, TC-GS-ROLE-91 |
| TC-GS-ROLE-E2E-039-remove-access-level-tier-berbeda-toast-404-netral | Pencabutan Access Level Saat Tier Target Berubah dari Tab yang Dirender: Toast 404 Netral dan Refresh Data | FE+BE | TC-GS-ROLE-298 |
| TC-GS-ROLE-E2E-040-assign-role-detail-picker-screening-dan-zero-selection | Screening Modal Table User Picker Assign Role pada Halaman Detail dan Validasi Seleksi Kosong | FE+BE | TC-GS-ROLE-92, TC-GS-ROLE-93 |
| TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud | Penugasan Role pada Detail Berhasil: Nilai Default CRUD (Read Aktif), Eksekusi Aktor MUR, dan Refleksi Rename User | FE+BE | TC-GS-ROLE-94, TC-GS-ROLE-95, TC-GS-ROLE-96, TC-GS-ROLE-100 |
| TC-GS-ROLE-E2E-042-assign-role-detail-resilience-server-500-dan-double-submit | Ketahanan Form Assign Role Detail: Penanganan Error Server 500 dan Guard Klik Ganda Cepat | mock | TC-GS-ROLE-97, TC-GS-ROLE-98 |
| TC-GS-ROLE-E2E-043-assign-role-detail-dual-session-concurrency-stale-v10-v11 | Konkurensi Antar-Admin Assign Role Detail: Validasi Stale User V-10 Dihapus dan V-11 Sudah Di-Assign Admin Lain | FE+BE | TC-GS-ROLE-99 |
| TC-GS-ROLE-E2E-044-edit-crud-detail-happy-path-dan-rapid-toggle | Penyuntingan CRUD Inline pada Detail Berhasil: Auto-Save Instan, Debounce Klik Cepat, dan Aktor MUR | FE+BE | TC-GS-ROLE-101, TC-GS-ROLE-102, TC-GS-ROLE-103 |
| TC-GS-ROLE-E2E-045-edit-crud-detail-auto-revert-total-control-user | Auto-Revert pada Edit CRUD: Dialog D-02 Saat Uncheck Sel User Total Control dan Pencabutan Akses TC | FE+BE | TC-GS-ROLE-104, TC-GS-ROLE-105, TC-GS-ROLE-106 |
| TC-GS-ROLE-E2E-046-edit-crud-detail-auto-revert-read-only-user | Auto-Revert pada Edit CRUD: Dialog D-02 Saat Check Sel Tulis User Read Only dan Pencabutan Hak RO | FE+BE | TC-GS-ROLE-107, TC-GS-ROLE-108 |
| TC-GS-ROLE-E2E-047-edit-crud-detail-resilience-server-500 | Ketahanan Edit CRUD Inline Detail: Pemulihan State Checkbox dan Tombol Retry Pasca-Error Jaringan 500 | mock | TC-GS-ROLE-109, TC-GS-ROLE-110, TC-GS-ROLE-111 |
| TC-GS-ROLE-E2E-048-remove-role-assignment-single-happy-path-dan-dialog | Pencabutan Baris Role Assignment Single: Dialog D-03, Pembatalan Cancel, Eksekusi MUR, dan Double-Click Debounce | FE+BE | TC-GS-ROLE-112, TC-GS-ROLE-113, TC-GS-ROLE-119 |
| TC-GS-ROLE-E2E-049-remove-role-assignment-single-auto-revert-tc-dan-ro | Pencabutan Baris Role Assignment Memunculkan Dialog Auto-Revert D-04 untuk Target TC dan RO | FE+BE | TC-GS-ROLE-114, TC-GS-ROLE-115, TC-GS-ROLE-116 |
| TC-GS-ROLE-E2E-050-remove-role-assignment-single-resilience-server-500 | Ketahanan Pencabutan Baris Role Single: Penanganan Kegagalan Server 500 pada Target Biasa dan TC/RO | mock | TC-GS-ROLE-117, TC-GS-ROLE-118 |
| TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman | Screening Bulk Action Bar Detail, Seleksi Baris Halaman Aktif, Counter, Clear (X), dan Retensi Saat Saring | FE+BE | TC-GS-ROLE-120, TC-GS-ROLE-121, TC-GS-ROLE-122, TC-GS-ROLE-136 |
| TC-GS-ROLE-E2E-052-bulk-remove-select-all-lintas-halaman-dan-unselect-all | Seleksi Massal Select All Lintas Halaman, Retensi Paginasi, dan Pembatalan Massal Unselect All | FE+BE | TC-GS-ROLE-123 |
| TC-GS-ROLE-E2E-053-bulk-remove-penegakan-batas-kuota-selection-limit | Penegakan Batas Kuota Selection Limit 100 Baris: Penonaktifan Baris ke-101 dan Capping Parsial Select All | FE+BE | TC-GS-ROLE-124, TC-GS-ROLE-125 |
| TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path | Pencabutan Massal User Regular Berhasil: Dialog D-05, Pembatalan Cancel, dan Eksekusi oleh Aktor MUR | FE+BE | TC-GS-ROLE-126, TC-GS-ROLE-127, TC-GS-ROLE-128, TC-GS-ROLE-132 |
| TC-GS-ROLE-E2E-055-bulk-remove-auto-revert-single-tier-dan-campuran | Pencabutan Massal User Campuran: Dialog D-06 Auto-Revert Single Tier, Campuran TC+RO, dan Eksekusi | FE+BE | TC-GS-ROLE-129, TC-GS-ROLE-130, TC-GS-ROLE-131 |
| TC-GS-ROLE-E2E-056-bulk-remove-tepat-satu-baris-fallback-dialog-single | Fallback Bulk Remove Tepat 1 Baris: Pemakaian Otomatis Dialog Single D-03 dan Single Auto-Revert D-04 | FE+BE | TC-GS-ROLE-294, TC-GS-ROLE-295 |
| TC-GS-ROLE-E2E-057-bulk-remove-resilience-server-500-dan-double-submit | Ketahanan Pencabutan Massal: Penanganan Kegagalan Server 500 dan Guard Klik Ganda Cepat | mock | TC-GS-ROLE-133, TC-GS-ROLE-135 |
| TC-GS-ROLE-E2E-058-bulk-remove-concurrency-d6-dan-partial-zero-success | Konkurensi Pencabutan Massal: Sebagian Baris Dihapus Sesi Lain, Perubahan Status TC Parsial, dan 0 Baris Berhasil | FE+BE | TC-GS-ROLE-134, TC-GS-ROLE-296, TC-GS-ROLE-299 |
| TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | Pencarian Toolbar Tabel Utama Tab TC & RO: Ekspansi, Substring Name/Email, Case-Insensitive, dan Pengecualian Kolom Status/Role/Date | FE+BE | TC-GS-ROLE-137, TC-GS-ROLE-138, TC-GS-ROLE-139, TC-GS-ROLE-140, TC-GS-ROLE-141 |
| TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | Filter Panel Tabel Utama Tab TC & RO: Screening Multi-Select, Date Range Last Updated & Temporary Until, dan Reset Clear Field | FE+BE | TC-GS-ROLE-142, TC-GS-ROLE-143, TC-GS-ROLE-144, TC-GS-ROLE-145, TC-GS-ROLE-146 |
| TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip | Filter Tabel Utama: Evaluasi Logika OR/AND, Pencarian di Dropdown Filter, dan Siklus Hapus Chip via (X) vs Uncheck | FE+BE | TC-GS-ROLE-147, TC-GS-ROLE-148, TC-GS-ROLE-149, TC-GS-ROLE-150 |
| TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | Pengurutan 3-State Tabel Utama Tab TC & RO: Siklus A-Z / Z-A / Default pada 8 Kolom Data dan Penanganan Default User di Akhir | FE+BE | TC-GS-ROLE-152, TC-GS-ROLE-153, TC-GS-ROLE-154, TC-GS-ROLE-155, TC-GS-ROLE-156 |
| TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination | Kombinasi 4 Kontrol Tabel Utama, Pemulihan Empty Result Saat Filter Dilepas, dan Paginasi 10/25/50/100 | FE+BE | TC-GS-ROLE-151, TC-GS-ROLE-157, TC-GS-ROLE-158, TC-GS-ROLE-159 |
| TC-GS-ROLE-E2E-064-tabel-utama-state-preservation-reload-f5-dan-reset-pindah-tab | State Preservation Tabel Utama: Persistensi Filter/Sort Pasca-Reload F5 dan Reset Bersih Saat Pindah Tab | FE+BE | TC-GS-ROLE-160, TC-GS-ROLE-161 |
| TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | Setup Kolom Tabel Utama Fase 1: Overlay Visibilitas, Modal Screening, Toggles Kolom K1/K2, dan Guard 1 Kolom Terakhir | mock | TC-GS-ROLE-162, TC-GS-ROLE-163, TC-GS-ROLE-164, TC-GS-ROLE-165, TC-GS-ROLE-172 |
| TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning | Setup Kolom Tabel Utama Fase 2: Drag-and-Drop Reorder Kolom K1/K2 dan Sticky Freeze Pinning pada Scroll Horizontal | mock | TC-GS-ROLE-166, TC-GS-ROLE-167, TC-GS-ROLE-168, TC-GS-ROLE-169 |
| TC-GS-ROLE-E2E-067-setup-kolom-tabel-utama-fase-3-reset-discard-dan-isolasi-tabel | Setup Kolom Tabel Utama Fase 3: Reset to Default, Pembatalan Discard via Esc/X, dan Independensi Konfigurasi per Tabel | mock | TC-GS-ROLE-170, TC-GS-ROLE-171, TC-GS-ROLE-173 |
| TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | Download Tab Utama: Format CSV/XLSX, Cakupan Baris Filter, Kolom Tampil WYSIWYG, dan Transformasi Nilai Default User | FE+BE | TC-GS-ROLE-174, TC-GS-ROLE-175, TC-GS-ROLE-176, TC-GS-ROLE-177, TC-GS-ROLE-178 |
| TC-GS-ROLE-E2E-069-download-tabel-utama-resilience-server-500-dan-background-job | Ketahanan Download Tab Utama: Toast Error Server 500 dan Eksekusi Background Job untuk Ekspor >5.000 Baris | mock | TC-GS-ROLE-179, TC-GS-ROLE-180 |
| TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | Tabel Tab System: Pencarian Role Name, Guard Kolom Non-Sortable, Setup Kolom, dan Download Ekspor | FE+BE | TC-GS-ROLE-181, TC-GS-ROLE-182, TC-GS-ROLE-183, TC-GS-ROLE-184, TC-GS-ROLE-185 |
| TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | Tabel Halaman Detail: Pencarian, Filter Panel, Pengurutan Kolom Data, dan State Preservation Back | FE+BE | TC-GS-ROLE-186, TC-GS-ROLE-187, TC-GS-ROLE-188, TC-GS-ROLE-189, TC-GS-ROLE-190, TC-GS-ROLE-191, TC-GS-ROLE-195 |
| TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download | Tabel Halaman Detail: Setup Kolom dengan Penguncian Kolom CRUD Dinamis dan Download Format Spesifik Title-Case-hyphen | mock | TC-GS-ROLE-192, TC-GS-ROLE-193, TC-GS-ROLE-194, TC-GS-ROLE-303 |
| TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | Screening Modal Changelog pada 4 Surface, Empty State, Pencarian per Kelas Kolom, dan Paginasi Halaman | FE+BE | TC-GS-ROLE-196, TC-GS-ROLE-197, TC-GS-ROLE-198, TC-GS-ROLE-199, TC-GS-ROLE-206 |
| TC-GS-ROLE-E2E-074-modal-changelog-filter-panel-dan-sorting-delapan-kolom | Modal Changelog: Filter Panel Multi-Kriteria, Dropdown Dinamis per Role, dan Pengurutan 3-State pada 8 Kolom | FE+BE | TC-GS-ROLE-200, TC-GS-ROLE-201, TC-GS-ROLE-202 |
| TC-GS-ROLE-E2E-075-modal-changelog-setup-kolom-download-dan-resilience | Modal Changelog: Preferensi Setup Kolom, Download 4 Varian CSV/XLSX, dan Ketahanan Error Server 500 | mock | TC-GS-ROLE-203, TC-GS-ROLE-204, TC-GS-ROLE-205 |
| TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | Pencatatan Audit Trail Changelog: Assign Baru, Upgrade, Remove, dan Auto-Revert Access Level TC/RO | FE+BE | TC-GS-ROLE-207, TC-GS-ROLE-208, TC-GS-ROLE-209, TC-GS-ROLE-210, TC-GS-ROLE-211 |
| TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | Pencatatan Audit Trail Changelog Detail: Edit CRUD C/U/D, Assign Role, Remove Row, dan Bulk Remove | FE+BE | TC-GS-ROLE-212, TC-GS-ROLE-213, TC-GS-ROLE-214, TC-GS-ROLE-215, TC-GS-ROLE-216, TC-GS-ROLE-217, TC-GS-ROLE-218, TC-GS-ROLE-219 |
| TC-GS-ROLE-E2E-078-audit-log-lintas-modul-system-log-dan-activity-log | Pencatatan Log Aktor ke System Log & Activity Log untuk Mutasi Access Level dan System Role | FE+BE | TC-GS-ROLE-221, TC-GS-ROLE-222, TC-GS-ROLE-289 |
| TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | Immutability Snapshot Nama User Pasca-Rename, Segregasi Changelog User vs User > Role, dan Update Modified By | FE+BE | TC-GS-ROLE-220, TC-GS-ROLE-223, TC-GS-ROLE-224, TC-GS-ROLE-225, TC-GS-ROLE-290 |
| TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | Sinkronisasi Seketika Akses Menu Sidebar Global Settings Setelah Penugasan dan Pencabutan Role/Akses | FE+BE | TC-GS-ROLE-226, TC-GS-ROLE-227, TC-GS-ROLE-228, TC-GS-ROLE-229, TC-GS-ROLE-230 |
| TC-GS-ROLE-E2E-081-sync-dua-arah-dengan-modul-user-detail-tab-role | Sinkronisasi Dua Arah Antara Menu Role & Permission dengan Halaman User Detail Tab Role | FE+BE | TC-GS-ROLE-231, TC-GS-ROLE-232 |
| TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | Kaskade Pembersihan Hak Akses Role: Pencabutan Access GS, Penghapusan User, dan Retensi Status Inactive | FE+BE | TC-GS-ROLE-233, TC-GS-ROLE-234, TC-GS-ROLE-235, TC-GS-ROLE-236, TC-GS-ROLE-291 |
| TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field | Sinkronisasi Atribut Perubahan Posisi User, Format Tanggal General Settings, dan Kolom Custom Field | FE+BE | TC-GS-ROLE-237, TC-GS-ROLE-238, TC-GS-ROLE-239, TC-GS-ROLE-240 |
| TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | Penerbitan Notifikasi In-App pada Kejadian Pencabutan Access Level, Auto-Revert, dan Bulk Remove | FE+BE | TC-GS-ROLE-241, TC-GS-ROLE-242, TC-GS-ROLE-243, TC-GS-ROLE-244, TC-GS-ROLE-245 |
| TC-GS-ROLE-E2E-085-plan-gating-dan-isolasi-scope-produk | Ketersediaan Modul pada Semua Tier Paket Langganan dan Isolasi Hak Akses Khusus Global Settings | FE+BE | TC-GS-ROLE-246, TC-GS-ROLE-283 |
| TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | Pertahanan Mendalam (Defense-in-Depth): Penolakan API 403 untuk Mutasi pada Akun Sendiri dan Default User | FE+BE | TC-GS-ROLE-247, TC-GS-ROLE-248, TC-GS-ROLE-250, TC-GS-ROLE-251, TC-GS-ROLE-253, TC-GS-ROLE-254, TC-GS-ROLE-255 |
| TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier | Pertahanan Mendalam: Penolakan API 403 Berdasarkan Batasan Wewenang Aktor dan Proteksi Target TC/RO | FE+BE | TC-GS-ROLE-249, TC-GS-ROLE-252, TC-GS-ROLE-256, TC-GS-ROLE-257 |
| TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid | Pertahanan Mendalam: Integritas Payload Form, Proteksi Kolom Invalid, Default User Skipping, dan Partial Success | FE+BE | TC-GS-ROLE-258, TC-GS-ROLE-259, TC-GS-ROLE-260, TC-GS-ROLE-261 |
| TC-GS-ROLE-E2E-089-defense-in-depth-keamanan-isolasi-multi-tenant | Pertahanan Mendalam: Keamanan Isolasi Multi-Tenant dan Pencegahan Pembacaan Data Lintas-Client | FE+BE | TC-GS-ROLE-262 |
| TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level | Client Suspended: Pemblokiran Operasi Tulis Assign dan Remove Total Control Serta Read Only | FE+BE | TC-GS-ROLE-263, TC-GS-ROLE-264, TC-GS-ROLE-265, TC-GS-ROLE-266 |
| TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove | Client Suspended: Pemblokiran Operasi Tulis Assign Role, Edit CRUD, Remove Single, dan Bulk Remove pada Detail | FE+BE | TC-GS-ROLE-267, TC-GS-ROLE-268, TC-GS-ROLE-269, TC-GS-ROLE-270 |
| TC-GS-ROLE-E2E-092-client-suspended-akses-baca-murni-seluruh-surface | Client Suspended: Akses Baca Murni Seluruh Tab dan Detail Berfungsi Normal Tanpa Gangguan | FE+BE | TC-GS-ROLE-271 |
| TC-GS-ROLE-E2E-093-konkurensi-edit-crud-last-write-wins-dan-target-stale | Konkurensi Antar-Admin pada Edit CRUD: Mekanisme Last-Write-Wins, Penolakan 403, dan 404 Netral | FE+BE | TC-GS-ROLE-272, TC-GS-ROLE-273, TC-GS-ROLE-284 |
| TC-GS-ROLE-E2E-094-konkurensi-remove-row-detail-stale-dan-auto-revert | Konkurensi Antar-Admin Remove Baris Detail: Penolakan 403, Idempotent 200, dan Auto-Revert Target Menjadi TC | FE+BE | TC-GS-ROLE-274, TC-GS-ROLE-276, TC-GS-ROLE-297 |
| TC-GS-ROLE-E2E-095-konkurensi-remove-access-level-stale-toast-404-netral | Konkurensi Antar-Admin Remove Access Level: Toast 404 Netral Saat Target Sudah Dihapus Admin Lain | FE+BE | TC-GS-ROLE-275 |
| TC-GS-ROLE-E2E-096-konkurensi-sse-auto-revert-dan-boundary-default-user | Konkurensi Antar-Admin: Sinkronisasi SSE Realtime Auto-Revert Lintas Tab dan Batas Proteksi Default User | FE+BE | TC-GS-ROLE-277, TC-GS-ROLE-278 |
| TC-GS-ROLE-E2E-097-konkurensi-assign-concurrent-rebutan-kandidat-user | Konkurensi Antar-Admin: Rebutan Kandidat User Simultan pada Assign Role dan Assign Total Control | FE+BE | TC-GS-ROLE-279, TC-GS-ROLE-280 |

---

## 2. TC hanya-BE (tidak masuk spec)

**0 TC**. Seluruh 305 TC granular pada `tc-role.md` memiliki pertanggungjawaban `PIC FE: v` dan dampak fungsional yang dapat divalidasi pada antarmuka web/mobile atau via intersep mock API klien. Seluruh kontrak murni backend telah dipisahkan ke `tc-role-backend.md`.

---

## 3. Sebaran per section TC

| Section | TC aktif | Tercakup | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Table List Flow | 37 | 37 | 0 |
| 2. Role & Capability Access Flow | 18 | 18 | 0 |
| 3a. Assign Total Control | 34 | 34 | 0 |
| 3b. Assign Read Only | 6 | 6 | 0 |
| 3c. Remove Total Control / Read Only | 9 | 9 | 0 |
| 3d. Assign Role (Detail) | 10 | 10 | 0 |
| 3e. Edit CRUD (Detail) | 11 | 11 | 0 |
| 3f. Remove Role Assignment — single (Detail) | 9 | 9 | 0 |
| 3g. Bulk Remove Role Assignment (Detail) | 23 | 23 | 0 |
| 4a. Tabel Utama — Tab Total Control & Tab Read Only | 28 | 28 | 0 |
| 4b. Tabel Tab System | 5 | 5 | 0 |
| 4c. Tabel Detail | 10 | 10 | 0 |
| 4d. Modal Changelog | 11 | 11 | 0 |
| 5. Pencatatan Audit Log & Multi-Surface Sync | 16 | 16 | 0 |
| 7. Cross-Module Sync & Foundation Cascading | 24 | 24 | 0 |
| 8. Security & Defense-in-Depth | 16 | 16 | 0 |
| 9. Edge Case Matrix & Concurrency Sisa | 18 | 18 | 0 |
| **Total** | **305** | **305** | **0** |

---

## 4. Lapisan per TC

| TC | Skenario | Priority | Lapisan | Spec | Mode |
|---|---|:---:|:---:|---|:---:|
| TC-GS-ROLE-1 | Screening halaman Role & Permission Tab Total Control (web) | P0 | E2E | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal | FE+BE |
| TC-GS-ROLE-2 | Screening halaman Role & Permission Tab Read Only (web) | P0 | E2E | TC-GS-ROLE-E2E-002-screening-tab-read-only-dan-empty-state | FE+BE |
| TC-GS-ROLE-3 | Screening halaman Role & Permission Tab System (web) | P0 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-4 | Screening halaman Detail role "Manage user and role" (web) | P0 | E2E | TC-GS-ROLE-E2E-004-screening-detail-role-dan-kolom-crud-enam-role | FE+BE |
| TC-GS-ROLE-5 | Detail — kolom CRUD dinamis dan deskripsi per role untuk 6 role | P0 | E2E | TC-GS-ROLE-E2E-004-screening-detail-role-dan-kolom-crud-enam-role | FE+BE |
| TC-GS-ROLE-6 | Buka Detail lewat klik Role Name di Tab System | P1 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-7 | Buka Detail lewat row action Detail di Tab System | P1 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-8 | Kembali dari Detail ke Tab System lewat breadcrumb | P1 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-9 | Hover Role Name di Tab System | P2 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-10 | Default sort Tab Total Control dan posisi baris Default User | P1 | E2E | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal | FE+BE |
| TC-GS-ROLE-11 | User Inactive tetap tampil di Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-002-screening-tab-read-only-dan-empty-state | FE+BE |
| TC-GS-ROLE-12 | Badge Pending Activation di sebelah Name pada Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-005-badge-kondisional-pending-activation-lintas-surface | FE+BE |
| TC-GS-ROLE-13 | Badge Pending Activation di sebelah Name pada Detail dan Table User Picker | P3 | E2E | TC-GS-ROLE-E2E-005-badge-kondisional-pending-activation-lintas-surface | FE+BE |
| TC-GS-ROLE-14 | Kolom Users Tab System menghitung semua pemegang baris termasuk TC/RO | P1 | E2E | TC-GS-ROLE-E2E-003-screening-tab-system-dan-navigasi-detail | FE+BE |
| TC-GS-ROLE-15 | Loading state per surface | P2 | E2E | TC-GS-ROLE-E2E-006-loading-skeleton-dan-error-load-resilience | mock |
| TC-GS-ROLE-16 | Error load Tab Total Control dan pulih via Try Again | P1 | E2E | TC-GS-ROLE-E2E-006-loading-skeleton-dan-error-load-resilience | mock |
| TC-GS-ROLE-17 | Error load pada Tab Read Only, Tab System, Detail, Table User Picker, dan Modal Changelog | P2 | E2E | TC-GS-ROLE-E2E-006-loading-skeleton-dan-error-load-resilience | mock |
| TC-GS-ROLE-18 | Empty state Tab Read Only tanpa user Read Only | P1 | E2E | TC-GS-ROLE-E2E-002-screening-tab-read-only-dan-empty-state | FE+BE |
| TC-GS-ROLE-19 | No-result state pada Tab Total Control, Read Only, System, dan Detail | P1 | E2E | TC-GS-ROLE-E2E-007-empty-state-pencarian-no-results-found | FE+BE |
| TC-GS-ROLE-20 | Tab Total Control dan Detail tidak pernah kosong | P1 | E2E | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal | FE+BE |
| TC-GS-ROLE-21 | Landing page Global Settings untuk user tanpa access level dan tanpa role | P0 | E2E | TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-aktivasi-akses | FE+BE |
| TC-GS-ROLE-22 | Landing state hilang setelah user tanpa role mendapat role | P1 | E2E | TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-aktivasi-akses | FE+BE |
| TC-GS-ROLE-23 | Hover tooltip icon Table Tools pada tiap surface | P3 | E2E | TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | mock |
| TC-GS-ROLE-24 | Name panjang tidak terpotong dan avatar placeholder | P3 | E2E | TC-GS-ROLE-E2E-001-screening-tab-total-control-dan-data-awal | FE+BE |
| TC-GS-ROLE-25 | Hover Modified By menampilkan nama lengkap | P2 | E2E | TC-GS-ROLE-E2E-009-hover-tooltip-toolbar-table-tools-dan-modified-by | mock |
| TC-GS-ROLE-26 | Guided tooltip muncul otomatis pada kunjungan pertama di Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-010-guided-tooltip-walkthrough-auto-launch-dan-navigasi | FE+BE |
| TC-GS-ROLE-27 | Guided tooltip Step 2 dan Step 3 lalu Done | P2 | E2E | TC-GS-ROLE-E2E-010-guided-tooltip-walkthrough-auto-launch-dan-navigasi | FE+BE |
| TC-GS-ROLE-28 | Guided tooltip dimulai di tab yang sedang aktif tanpa berpindah tab | P3 | E2E | TC-GS-ROLE-E2E-010-guided-tooltip-walkthrough-auto-launch-dan-navigasi | FE+BE |
| TC-GS-ROLE-29 | Guided tooltip Skip, Back, dan replay via [?] | P3 | E2E | TC-GS-ROLE-E2E-011-guided-tooltip-walkthrough-skip-replay-exit-keyboard | FE+BE |
| TC-GS-ROLE-30 | Guided tooltip ditutup tanpa selesai saat navigasi keluar | P3 | E2E | TC-GS-ROLE-E2E-011-guided-tooltip-walkthrough-skip-replay-exit-keyboard | FE+BE |
| TC-GS-ROLE-31 | Guided tooltip dapat dikendalikan dengan keyboard | P3 | E2E | TC-GS-ROLE-E2E-011-guided-tooltip-walkthrough-skip-replay-exit-keyboard | FE+BE |
| TC-GS-ROLE-32 | Mobile — Detail multi-select lewat long press dan bulk Remove | P2 | E2E | TC-GS-ROLE-E2E-012-mobile-gesture-multi-select-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-33 | Menu Role & Permission tampil di sidebar untuk aktor yang punya akses baca | P0 | E2E | TC-GS-ROLE-E2E-014-sidebar-menu-visibility-per-role-dan-direct-url-guard | FE+BE |
| TC-GS-ROLE-34 | Menu Role & Permission tersembunyi untuk user tanpa role Manage user and role | P0 | E2E | TC-GS-ROLE-E2E-014-sidebar-menu-visibility-per-role-dan-direct-url-guard | FE+BE |
| TC-GS-ROLE-35 | Akses langsung URL Role & Permission tanpa role Manage user and role | P0 | E2E | TC-GS-ROLE-E2E-014-sidebar-menu-visibility-per-role-dan-direct-url-guard | FE+BE |
| TC-GS-ROLE-36 | Visibilitas elemen untuk aktor Total Control | P0 | E2E | TC-GS-ROLE-E2E-015-role-matrix-ui-visibility-aktor-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-37 | Visibilitas elemen untuk aktor Read Only | P0 | E2E | TC-GS-ROLE-E2E-015-role-matrix-ui-visibility-aktor-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-38 | Visibilitas elemen untuk aktor Manage user and role Read saja | P0 | E2E | TC-GS-ROLE-E2E-015-role-matrix-ui-visibility-aktor-total-control-dan-read-only | FE+BE |
| TC-GS-ROLE-39 | Visibilitas elemen untuk aktor Manage user and role tanpa Update | P0 | E2E | TC-GS-ROLE-E2E-016-role-matrix-ui-visibility-aktor-manage-user-and-role | FE+BE |
| TC-GS-ROLE-40 | Visibilitas elemen untuk aktor Manage user and role dengan Update | P0 | E2E | TC-GS-ROLE-E2E-016-role-matrix-ui-visibility-aktor-manage-user-and-role | FE+BE |
| TC-GS-ROLE-41 | Detail untuk aktor Total Control — baris diri sendiri, Default User, dan target TC/RO | P0 | E2E | TC-GS-ROLE-E2E-017-guard-proteksi-default-user-dan-self-edit-pada-detail | FE+BE |
| TC-GS-ROLE-42 | Remove di Tab Total Control untuk Default User dan diri sendiri | P0 | E2E | TC-GS-ROLE-E2E-017-guard-proteksi-default-user-dan-self-edit-pada-detail | FE+BE |
| TC-GS-ROLE-43 | Checkbox Read selalu checked dan terkunci untuk semua aktor | P0 | E2E | TC-GS-ROLE-E2E-018-guard-proteksi-checkbox-read-dan-prioritas-tooltip | FE+BE |
| TC-GS-ROLE-44 | Prioritas tooltip CRUD — aktor Read Only pada baris Default User | P2 | E2E | TC-GS-ROLE-E2E-018-guard-proteksi-checkbox-read-dan-prioritas-tooltip | FE+BE |
| TC-GS-ROLE-45 | Prioritas tooltip — Default User login melihat barisnya sendiri | P2 | E2E | TC-GS-ROLE-E2E-017-guard-proteksi-default-user-dan-self-edit-pada-detail | FE+BE |
| TC-GS-ROLE-46 | Prioritas tooltip — aktor Manage user and role Update pada Default User (target TC) | P2 | E2E | TC-GS-ROLE-E2E-018-guard-proteksi-checkbox-read-dan-prioritas-tooltip | FE+BE |
| TC-GS-ROLE-47 | Accessibility — checkbox Detail operable keyboard dan tooltip saat fokus | P2 | E2E | TC-GS-ROLE-E2E-019-aksesibilitas-keyboard-dan-fokus-dialog | FE+BE |
| TC-GS-ROLE-48 | Accessibility — dialog konfirmasi focus trapped dan Esc menutup | P2 | E2E | TC-GS-ROLE-E2E-019-aksesibilitas-keyboard-dan-fokus-dialog | FE+BE |
| TC-GS-ROLE-49 | Checkbox seleksi Detail untuk aktor Total Control dan Select All mengecualikan baris disabled | P1 | E2E | TC-GS-ROLE-E2E-020-gating-seleksi-bulk-action-bar-per-aktor | FE+BE |
| TC-GS-ROLE-50 | Checkbox seleksi Detail untuk aktor Manage user and role Update | P1 | E2E | TC-GS-ROLE-E2E-020-gating-seleksi-bulk-action-bar-per-aktor | FE+BE |
| TC-GS-ROLE-51 | Screening Popup Assign Total Control | P0 | E2E | TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-52 | Pool Popup Assign Total Control | P0 | E2E | TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-53 | Picker menampilkan dua user bernama sama yang dibedakan Email dan Position | P3 | E2E | TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-54 | Submit Assign Total Control tanpa memilih user | P0 | E2E | TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-55 | Selection counter Popup Assign Total Control | P2 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-56 | Checkbox header Popup Assign memilih semua baris halaman aktif | P2 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-57 | Cancel Popup Assign Total Control | P2 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-58 | Assign Total Control ke satu user | P0 | E2E | TC-GS-ROLE-E2E-026-assign-total-control-happy-path-single-dan-multi-user | FE+BE |
| TC-GS-ROLE-59 | Assign Total Control ke beberapa user sekaligus termasuk Inactive dan Pending Activation | P1 | E2E | TC-GS-ROLE-E2E-026-assign-total-control-happy-path-single-dan-multi-user | FE+BE |
| TC-GS-ROLE-60 | Assign Total Control langsung ke user Read Only (upgrade) | P1 | E2E | TC-GS-ROLE-E2E-027-assign-total-control-upgrade-dari-read-only | FE+BE |
| TC-GS-ROLE-61 | Assign Total Control menimpa baris role parsial yang sudah ada | P1 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-62 | Assign Total Control tidak memicu notifikasi ke target | P2 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-63 | Klik ganda [Assign] Popup Assign Total Control | P1 | E2E | TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10 | FE+BE |
| TC-GS-ROLE-64 | Assign Total Control gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-030-assign-total-control-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-65 | Assign Total Control saat user terpilih dihapus admin lain sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-030-assign-total-control-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-66 | Assign Total Control saat user terpilih menjadi tidak eligible sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10 | FE+BE |
| TC-GS-ROLE-67 | Assign Total Control saat user terpilih di-rename sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-026-assign-total-control-happy-path-single-dan-multi-user | FE+BE |
| TC-GS-ROLE-68 | Empty state Popup Assign saat semua user eligible sudah di-assign | P2 | E2E | TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | FE+BE |
| TC-GS-ROLE-69 | No-result Search pada Popup Assign | P2 | E2E | TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | FE+BE |
| TC-GS-ROLE-70 | Search Popup Assign berdasarkan Name dan Email | P1 | E2E | TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | FE+BE |
| TC-GS-ROLE-71 | Search Popup Assign berdasarkan Position dan Division serta kolom yang tidak dicari | P1 | E2E | TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | FE+BE |
| TC-GS-ROLE-72 | Search Popup Assign tidak mencocokkan kolom Status | P1 | E2E | TC-GS-ROLE-E2E-023-assign-total-control-picker-search-dan-scoping-kolom-tersembunyi | FE+BE |
| TC-GS-ROLE-73 | Filter Popup Assign berdasarkan Position, Division, dan Status | P1 | E2E | TC-GS-ROLE-E2E-024-assign-total-control-picker-filter-panel-multi-kriteria | FE+BE |
| TC-GS-ROLE-74 | Filter Popup Assign berdasarkan Activation Status, Temporary User, Temporary Until, Custom Field | P1 | E2E | TC-GS-ROLE-E2E-024-assign-total-control-picker-filter-panel-multi-kriteria | FE+BE |
| TC-GS-ROLE-75 | Pagination Popup Assign | P2 | E2E | TC-GS-ROLE-E2E-025-assign-total-control-picker-sorting-pagination-retensi | FE+BE |
| TC-GS-ROLE-76 | Column Visibility / Setup Column pada Popup Assign | P3 | E2E | TC-GS-ROLE-E2E-021-assign-total-control-picker-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-77 | Accessibility Popup Assign — focus trapped dan Esc menutup | P3 | E2E | TC-GS-ROLE-E2E-022-assign-total-control-picker-seleksi-dan-unsaved-dismissal | FE+BE |
| TC-GS-ROLE-78 | Screening Popup Assign Read Only dan pool-nya | P0 | E2E | TC-GS-ROLE-E2E-031-assign-read-only-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-79 | Submit Assign Read Only tanpa memilih user | P1 | E2E | TC-GS-ROLE-E2E-031-assign-read-only-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-80 | Assign Read Only ke user | P0 | E2E | TC-GS-ROLE-E2E-032-assign-read-only-happy-path-single-user | FE+BE |
| TC-GS-ROLE-81 | Assign Read Only gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-033-assign-read-only-validasi-stale-user-v10 | FE+BE |
| TC-GS-ROLE-82 | Klik ganda [Assign] Popup Assign Read Only | P1 | E2E | TC-GS-ROLE-E2E-031-assign-read-only-screening-dan-pool-eligibility | FE+BE |
| TC-GS-ROLE-83 | Assign Read Only saat user terpilih dihapus atau menjadi tidak eligible sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-034-assign-read-only-resilience-server-500 | mock |
| TC-GS-ROLE-84 | Screening dialog Remove Total Control | P0 | E2E | TC-GS-ROLE-E2E-035-remove-total-control-screening-dialog-dan-batal | FE+BE |
| TC-GS-ROLE-85 | Cancel dialog Remove Total Control | P1 | E2E | TC-GS-ROLE-E2E-035-remove-total-control-screening-dialog-dan-batal | FE+BE |
| TC-GS-ROLE-86 | Remove Total Control dari user | P0 | E2E | TC-GS-ROLE-E2E-036-remove-total-control-happy-path-dan-user-inactive | FE+BE |
| TC-GS-ROLE-87 | Remove Total Control user Inactive tanpa batasan jumlah Total Control | P2 | E2E | TC-GS-ROLE-E2E-036-remove-total-control-happy-path-dan-user-inactive | FE+BE |
| TC-GS-ROLE-88 | Screening dialog dan Remove Read Only | P0 | E2E | TC-GS-ROLE-E2E-037-remove-read-only-happy-path-single-user | FE+BE |
| TC-GS-ROLE-89 | Remove Total Control gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-038-remove-access-level-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-90 | Remove Read Only gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-038-remove-access-level-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-91 | Klik ganda [Remove] dialog Remove Total Control | P1 | E2E | TC-GS-ROLE-E2E-038-remove-access-level-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-92 | Screening Popup Assign Role dan pool-nya | P0 | E2E | TC-GS-ROLE-E2E-040-assign-role-detail-picker-screening-dan-zero-selection | FE+BE |
| TC-GS-ROLE-93 | Submit Assign Role tanpa memilih user | P1 | E2E | TC-GS-ROLE-E2E-040-assign-role-detail-picker-screening-dan-zero-selection | FE+BE |
| TC-GS-ROLE-94 | Assign Role Manage TAG ke beberapa user oleh Total Control | P0 | E2E | TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud | FE+BE |
| TC-GS-ROLE-95 | Assign Role Import data — baris baru Read aktif, Create unchecked | P1 | E2E | TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud | FE+BE |
| TC-GS-ROLE-96 | Assign Role oleh aktor Manage user and role dengan Update | P0 | E2E | TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud | FE+BE |
| TC-GS-ROLE-97 | Assign Role gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-042-assign-role-detail-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-98 | Klik ganda [Assign] Popup Assign Role | P1 | E2E | TC-GS-ROLE-E2E-042-assign-role-detail-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-99 | Assign Role saat user terpilih dihapus atau sudah di-assign admin lain sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-043-assign-role-detail-dual-session-concurrency-stale-v10-v11 | FE+BE |
| TC-GS-ROLE-100 | Assign Role saat user terpilih di-rename sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-041-assign-role-detail-happy-path-dan-default-crud | FE+BE |
| TC-GS-ROLE-101 | Edit CRUD centang Update oleh Total Control pada target biasa | P0 | E2E | TC-GS-ROLE-E2E-044-edit-crud-detail-happy-path-dan-rapid-toggle | FE+BE |
| TC-GS-ROLE-102 | Edit CRUD uncheck Delete oleh Total Control pada target biasa | P1 | E2E | TC-GS-ROLE-E2E-044-edit-crud-detail-happy-path-dan-rapid-toggle | FE+BE |
| TC-GS-ROLE-103 | Edit CRUD oleh aktor Manage user and role dengan Update | P0 | E2E | TC-GS-ROLE-E2E-044-edit-crud-detail-happy-path-dan-rapid-toggle | FE+BE |
| TC-GS-ROLE-104 | Screening dialog auto-revert saat mengedit role user Total Control | P0 | E2E | TC-GS-ROLE-E2E-045-edit-crud-detail-auto-revert-total-control-user | FE+BE |
| TC-GS-ROLE-105 | Cancel dialog auto-revert | P0 | E2E | TC-GS-ROLE-E2E-045-edit-crud-detail-auto-revert-total-control-user | FE+BE |
| TC-GS-ROLE-106 | Konfirmasi auto-revert user Total Control | P0 | E2E | TC-GS-ROLE-E2E-045-edit-crud-detail-auto-revert-total-control-user | FE+BE |
| TC-GS-ROLE-107 | Konfirmasi auto-revert user Read Only | P0 | E2E | TC-GS-ROLE-E2E-046-edit-crud-detail-auto-revert-read-only-user | FE+BE |
| TC-GS-ROLE-108 | Edit CRUD gagal 5xx pada target biasa | P1 | E2E | TC-GS-ROLE-E2E-046-edit-crud-detail-auto-revert-read-only-user | FE+BE |
| TC-GS-ROLE-109 | Auto-revert gagal 5xx memakai pesan gagal Edit CRUD | P1 | E2E | TC-GS-ROLE-E2E-047-edit-crud-detail-resilience-server-500 | mock |
| TC-GS-ROLE-110 | Screening overlay row action dan dialog Remove baris target biasa | P0 | E2E | TC-GS-ROLE-E2E-047-edit-crud-detail-resilience-server-500 | mock |
| TC-GS-ROLE-111 | Cancel dialog Remove baris target biasa | P1 | E2E | TC-GS-ROLE-E2E-047-edit-crud-detail-resilience-server-500 | mock |
| TC-GS-ROLE-112 | Remove baris role target biasa oleh Total Control | P0 | E2E | TC-GS-ROLE-E2E-048-remove-role-assignment-single-happy-path-dan-dialog | FE+BE |
| TC-GS-ROLE-113 | Remove baris role oleh aktor Manage user and role dengan Update | P0 | E2E | TC-GS-ROLE-E2E-048-remove-role-assignment-single-happy-path-dan-dialog | FE+BE |
| TC-GS-ROLE-114 | Remove baris role target Total Control memicu dialog auto-revert | P0 | E2E | TC-GS-ROLE-E2E-049-remove-role-assignment-single-auto-revert-tc-dan-ro | FE+BE |
| TC-GS-ROLE-115 | Remove baris role target Read Only memicu dialog auto-revert | P1 | E2E | TC-GS-ROLE-E2E-049-remove-role-assignment-single-auto-revert-tc-dan-ro | FE+BE |
| TC-GS-ROLE-116 | Cancel dialog auto-revert dari Remove baris | P1 | E2E | TC-GS-ROLE-E2E-049-remove-role-assignment-single-auto-revert-tc-dan-ro | FE+BE |
| TC-GS-ROLE-117 | Remove baris role gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-050-remove-role-assignment-single-resilience-server-500 | mock |
| TC-GS-ROLE-118 | Remove baris role target Total Control gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-050-remove-role-assignment-single-resilience-server-500 | mock |
| TC-GS-ROLE-119 | Klik ganda [Remove] dialog Remove baris role | P1 | E2E | TC-GS-ROLE-E2E-048-remove-role-assignment-single-happy-path-dan-dialog | FE+BE |
| TC-GS-ROLE-120 | Screening Bulk Action Bar Detail | P1 | E2E | TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman | FE+BE |
| TC-GS-ROLE-121 | Checkbox header Detail — select page, header tidak checked penuh, deselect | P2 | E2E | TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman | FE+BE |
| TC-GS-ROLE-122 | Clear seleksi via (X) di Bulk Action Bar | P2 | E2E | TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman | FE+BE |
| TC-GS-ROLE-123 | Select All lintas halaman dan Unselect All | P1 | E2E | TC-GS-ROLE-E2E-052-bulk-remove-select-all-lintas-halaman-dan-unselect-all | FE+BE |
| TC-GS-ROLE-124 | Selection Limit — centang manual melewati batas | P1 | E2E | TC-GS-ROLE-E2E-053-bulk-remove-penegakan-batas-kuota-selection-limit | FE+BE |
| TC-GS-ROLE-125 | Selection Limit — Select All di-cap otomatis | P1 | E2E | TC-GS-ROLE-E2E-053-bulk-remove-penegakan-batas-kuota-selection-limit | FE+BE |
| TC-GS-ROLE-126 | Screening dialog Bulk Remove tanpa baris Total Control/Read Only | P0 | E2E | TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path | FE+BE |
| TC-GS-ROLE-127 | Cancel dialog Bulk Remove mempertahankan seleksi | P1 | E2E | TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path | FE+BE |
| TC-GS-ROLE-128 | Bulk Remove baris regular | P0 | E2E | TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path | FE+BE |
| TC-GS-ROLE-129 | Screening dialog Bulk Remove dengan satu baris Read Only | P0 | E2E | TC-GS-ROLE-E2E-055-bulk-remove-auto-revert-single-tier-dan-campuran | FE+BE |
| TC-GS-ROLE-130 | Screening dialog Bulk Remove dengan baris Total Control dan Read Only | P1 | E2E | TC-GS-ROLE-E2E-055-bulk-remove-auto-revert-single-tier-dan-campuran | FE+BE |
| TC-GS-ROLE-131 | Bulk Remove campuran regular dan Total Control/Read Only | P0 | E2E | TC-GS-ROLE-E2E-055-bulk-remove-auto-revert-single-tier-dan-campuran | FE+BE |
| TC-GS-ROLE-132 | Bulk Remove oleh aktor Manage user and role dengan Update | P1 | E2E | TC-GS-ROLE-E2E-054-bulk-remove-regular-users-dialog-dan-happy-path | FE+BE |
| TC-GS-ROLE-133 | Bulk Remove gagal 5xx | P1 | E2E | TC-GS-ROLE-E2E-057-bulk-remove-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-134 | Bulk Remove saat sebagian baris sudah dihapus admin lain | P1 | E2E | TC-GS-ROLE-E2E-058-bulk-remove-concurrency-d6-dan-partial-zero-success | FE+BE |
| TC-GS-ROLE-135 | Klik ganda [Remove] dialog Bulk Remove | P1 | E2E | TC-GS-ROLE-E2E-057-bulk-remove-resilience-server-500-dan-double-submit | mock |
| TC-GS-ROLE-136 | Seleksi tetap bertahan saat Search dikosongkan | P2 | E2E | TC-GS-ROLE-E2E-051-bulk-remove-action-bar-screening-dan-seleksi-halaman | FE+BE |
| TC-GS-ROLE-137 | Siklus interaksi Search Tab Total Control dan Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | FE+BE |
| TC-GS-ROLE-138 | Search kolom teks visible Tab Total Control dan Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | FE+BE |
| TC-GS-ROLE-139 | Search kolom badge Status, Activation Status, Temporary User di Tab Total Control/Read Only | P1 | E2E | TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | FE+BE |
| TC-GS-ROLE-140 | Search kolom TAG saat di-hide dan setelah di-unhide | P2 | E2E | TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | FE+BE |
| TC-GS-ROLE-141 | Search tidak mencocokkan kolom tanggal Last Updated dan Temporary Until | P1 | E2E | TC-GS-ROLE-E2E-059-tabel-utama-pencarian-toolbar-dan-scoping-kolom | FE+BE |
| TC-GS-ROLE-142 | Screening Filter Panel Tab Total Control dan Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | FE+BE |
| TC-GS-ROLE-143 | Opsi dropdown filter Tab Total Control diisi dari data tab itu | P1 | E2E | TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | FE+BE |
| TC-GS-ROLE-144 | Filter multi-select per field Tab Total Control dan Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | FE+BE |
| TC-GS-ROLE-145 | Filter date range Last Updated dan Temporary Until | P1 | E2E | TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | FE+BE |
| TC-GS-ROLE-146 | Search, Filter, dan Sort Custom Field aktif bertipe Dropdown | P2 | E2E | TC-GS-ROLE-E2E-060-tabel-utama-filter-panel-screening-date-range-dan-clear | FE+BE |
| TC-GS-ROLE-147 | Filter OR dalam satu field dan AND antar field | P1 | E2E | TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip | FE+BE |
| TC-GS-ROLE-148 | Search di dalam dropdown filter dan chip terpilih | P2 | E2E | TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip | FE+BE |
| TC-GS-ROLE-149 | Hapus chip filter lewat (X) pada chip | P2 | E2E | TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip | FE+BE |
| TC-GS-ROLE-150 | Hapus pilihan filter lewat uncheck di dropdown | P2 | E2E | TC-GS-ROLE-E2E-061-tabel-utama-filter-logika-disjungsi-dan-siklus-chip | FE+BE |
| TC-GS-ROLE-151 | Search lalu Filter dan Filter lalu Search | P1 | E2E | TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination | FE+BE |
| TC-GS-ROLE-152 | Sort kolom teks Name, Position, Division, Modified By | P1 | E2E | TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | FE+BE |
| TC-GS-ROLE-153 | Sort kolom Status (Active First / Inactive First) | P1 | E2E | TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | FE+BE |
| TC-GS-ROLE-154 | Sort kolom Temporary User (Yes First / No First) | P2 | E2E | TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | FE+BE |
| TC-GS-ROLE-155 | Sort kolom tanggal Last Updated dan Temporary Until | P1 | E2E | TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | FE+BE |
| TC-GS-ROLE-156 | Sort kolom Activation Status dan TAG | P2 | E2E | TC-GS-ROLE-E2E-062-tabel-utama-sorting-tiga-keadaan-delapan-kolom | FE+BE |
| TC-GS-ROLE-157 | Kombinasi Search, Filter, Sort, dan Pagination | P1 | E2E | TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination | FE+BE |
| TC-GS-ROLE-158 | Pulih dari no-result saat satu saringan dilepas | P2 | E2E | TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination | FE+BE |
| TC-GS-ROLE-159 | Pagination Tab Total Control dan Tab Read Only | P2 | E2E | TC-GS-ROLE-E2E-063-tabel-utama-kombinasi-kontrol-dan-pagination | FE+BE |
| TC-GS-ROLE-160 | Refresh F5 mempertahankan Search, Filter, Sort, dan halaman | P1 | E2E | TC-GS-ROLE-E2E-064-tabel-utama-state-preservation-reload-f5-dan-reset-pindah-tab | FE+BE |
| TC-GS-ROLE-161 | State Search/Filter/Sort saat pindah Tab Total Control ↔ Read Only ↔ System | P1 | E2E | TC-GS-ROLE-E2E-064-tabel-utama-state-preservation-reload-f5-dan-reset-pindah-tab | FE+BE |
| TC-GS-ROLE-162 | Screening overlay Column Visibility Tab Total Control dan Tab Read Only | P2 | E2E | TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | mock |
| TC-GS-ROLE-163 | Screening popup Setup Column Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | mock |
| TC-GS-ROLE-164 | Setup Column — Hide kolom kelas K1 default tampil lalu Save | P2 | E2E | TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | mock |
| TC-GS-ROLE-165 | Setup Column — Show kolom kelas K2 kurasi tersembunyi lalu Save | P2 | E2E | TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | mock |
| TC-GS-ROLE-166 | Setup Column — drag reorder kolom kelas K1 | P3 | E2E | TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning | mock |
| TC-GS-ROLE-167 | Setup Column — pin kolom kelas K1 | P3 | E2E | TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning | mock |
| TC-GS-ROLE-168 | Setup Column — drag reorder kolom kelas K2 | P3 | E2E | TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning | mock |
| TC-GS-ROLE-169 | Setup Column — pin kolom kelas K2 | P3 | E2E | TC-GS-ROLE-E2E-066-setup-kolom-tabel-utama-fase-2-drag-reorder-dan-freeze-pinning | mock |
| TC-GS-ROLE-170 | Setup Column — Reset to Default | P3 | E2E | TC-GS-ROLE-E2E-067-setup-kolom-tabel-utama-fase-3-reset-discard-dan-isolasi-tabel | mock |
| TC-GS-ROLE-171 | Setup Column — tutup tanpa Save membatalkan perubahan | P3 | E2E | TC-GS-ROLE-E2E-067-setup-kolom-tabel-utama-fase-3-reset-discard-dan-isolasi-tabel | mock |
| TC-GS-ROLE-172 | Setup Column — kolom terakhir yang tampil tidak bisa di-uncheck | P3 | E2E | TC-GS-ROLE-E2E-065-setup-kolom-tabel-utama-fase-1-overlay-dan-modal-ceklis | mock |
| TC-GS-ROLE-173 | Setup Column — konfigurasi terpisah per tabel | P3 | E2E | TC-GS-ROLE-E2E-067-setup-kolom-tabel-utama-fase-3-reset-discard-dan-isolasi-tabel | mock |
| TC-GS-ROLE-174 | Download Tab Total Control sebagai CSV dan XLSX | P1 | E2E | TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | FE+BE |
| TC-GS-ROLE-175 | Download Tab Read Only sebagai CSV dan XLSX | P1 | E2E | TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | FE+BE |
| TC-GS-ROLE-176 | Cakupan baris Download Tab Total Control/Read Only tanpa dan dengan filter | P1 | E2E | TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | FE+BE |
| TC-GS-ROLE-177 | Download mengikuti kolom yang tampil | P1 | E2E | TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | FE+BE |
| TC-GS-ROLE-178 | Transformasi nilai pada file Download Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-068-download-tabel-utama-format-scope-dan-transformasi-wysiwyg | FE+BE |
| TC-GS-ROLE-179 | Download gagal pada Tab Total Control | P1 | E2E | TC-GS-ROLE-E2E-069-download-tabel-utama-resilience-server-500-dan-background-job | mock |
| TC-GS-ROLE-180 | Download lebih dari 5.000 baris berjalan sebagai background job | P3 | E2E | TC-GS-ROLE-E2E-069-download-tabel-utama-resilience-server-500-dan-background-job | mock |
| TC-GS-ROLE-181 | Search Tab System | P1 | E2E | TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | FE+BE |
| TC-GS-ROLE-182 | Kolom Tab System tidak dapat di-sort | P2 | E2E | TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | FE+BE |
| TC-GS-ROLE-183 | Screening overlay dan popup Setup Column Tab System | P3 | E2E | TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | FE+BE |
| TC-GS-ROLE-184 | Setup Column Tab System — hide, drag, pin, reset, discard, guard | P3 | E2E | TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | FE+BE |
| TC-GS-ROLE-185 | Download Tab System sebagai CSV dan XLSX | P1 | E2E | TC-GS-ROLE-E2E-070-tab-system-search-guard-setup-kolom-dan-download | FE+BE |
| TC-GS-ROLE-186 | Search Detail berdasarkan Name, Position, Division | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-187 | Search Detail tidak mencocokkan kolom CRUD dan Temporary Until | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-188 | Search Detail kolom Activation Status, Temporary User, TAG, dan Custom Field | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-189 | Screening Filter Panel Detail | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-190 | Filter Detail per field dan kombinasi | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-191 | Sort Detail per kolom data dan kolom CRUD tidak sortable | P1 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-192 | Setup Column Detail — kolom CRUD dinamis | P2 | E2E | TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download | mock |
| TC-GS-ROLE-193 | Setup Column Detail — hide/show kolom Name, Position, Division, dan kolom kurasi | P2 | E2E | TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download | mock |
| TC-GS-ROLE-194 | Download Detail sebagai CSV dan XLSX | P1 | E2E | TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download | mock |
| TC-GS-ROLE-195 | Back dari Detail mempertahankan Search Tab System | P2 | E2E | TC-GS-ROLE-E2E-071-tabel-detail-search-filter-sort-dan-state-preservation | FE+BE |
| TC-GS-ROLE-196 | Screening Modal Changelog Tab Total Control dan Tab Read Only | P1 | E2E | TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | FE+BE |
| TC-GS-ROLE-197 | Screening Modal Changelog Tab System dan Detail | P1 | E2E | TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | FE+BE |
| TC-GS-ROLE-198 | Empty state dan no-result Modal Changelog | P2 | E2E | TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | FE+BE |
| TC-GS-ROLE-199 | Search Modal Changelog per kelas kolom | P1 | E2E | TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | FE+BE |
| TC-GS-ROLE-200 | Filter Modal Changelog Tab Total Control/Read Only | P1 | E2E | TC-GS-ROLE-E2E-074-modal-changelog-filter-panel-dan-sorting-delapan-kolom | FE+BE |
| TC-GS-ROLE-201 | Filter Modal Changelog Tab System dan Detail | P1 | E2E | TC-GS-ROLE-E2E-074-modal-changelog-filter-panel-dan-sorting-delapan-kolom | FE+BE |
| TC-GS-ROLE-202 | Sort Modal Changelog | P2 | E2E | TC-GS-ROLE-E2E-074-modal-changelog-filter-panel-dan-sorting-delapan-kolom | FE+BE |
| TC-GS-ROLE-203 | Setup Column Modal Changelog | P3 | E2E | TC-GS-ROLE-E2E-075-modal-changelog-setup-kolom-download-dan-resilience | mock |
| TC-GS-ROLE-204 | Download Modal Changelog per varian | P1 | E2E | TC-GS-ROLE-E2E-075-modal-changelog-setup-kolom-download-dan-resilience | mock |
| TC-GS-ROLE-205 | Download Modal Changelog gagal | P1 | E2E | TC-GS-ROLE-E2E-075-modal-changelog-setup-kolom-download-dan-resilience | mock |
| TC-GS-ROLE-206 | Pagination Modal Changelog | P3 | E2E | TC-GS-ROLE-E2E-073-modal-changelog-screening-empty-state-search-pagination | FE+BE |
| TC-GS-ROLE-207 | Changelog Total Control — entry Assign user baru | P1 | E2E | TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | FE+BE |
| TC-GS-ROLE-208 | Changelog Total Control — entry Assign upgrade dari Read Only | P1 | E2E | TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | FE+BE |
| TC-GS-ROLE-209 | Changelog Total Control — entry Remove | P1 | E2E | TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | FE+BE |
| TC-GS-ROLE-210 | Changelog Total Control — entry Auto-Revert Total Control | P1 | E2E | TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | FE+BE |
| TC-GS-ROLE-211 | Changelog Read Only — entry Assign, Remove, Auto-Revert Read Only | P1 | E2E | TC-GS-ROLE-E2E-076-audit-log-changelog-access-level-tc-dan-ro | FE+BE |
| TC-GS-ROLE-212 | Changelog System dan Detail — entry Edit Field Create | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-213 | Changelog System dan Detail — entry Edit Field Update | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-214 | Changelog System dan Detail — entry Edit Field Delete | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-215 | Changelog System dan Detail — entry Assign baris role | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-216 | Changelog System dan Detail — entry Remove baris role | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-217 | Remove baris target TC mencatat Remove dan Auto-Revert terpisah | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-218 | Bulk Remove mencatat satu entry per baris dan Auto-Revert per user tier | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-219 | Changelog Detail memuat entry role itu saja, Changelog System superset | P1 | E2E | TC-GS-ROLE-E2E-077-audit-log-changelog-detail-role-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-220 | Entry log lama tidak berubah setelah user di-rename | P2 | E2E | TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | FE+BE |
| TC-GS-ROLE-221 | System Log aktor dan Activity Log untuk Assign/Remove/Auto-Revert access level | P1 | E2E | TC-GS-ROLE-E2E-078-audit-log-lintas-modul-system-log-dan-activity-log | FE+BE |
| TC-GS-ROLE-222 | System Log aktor dan Activity Log untuk Edit/Assign/Remove baris role | P1 | E2E | TC-GS-ROLE-E2E-078-audit-log-lintas-modul-system-log-dan-activity-log | FE+BE |
| TC-GS-ROLE-223 | Changelog: User mencatat aksi access level dan role; Changelog: User > Role hanya aksi per-role | P2 | E2E | TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | FE+BE |
| TC-GS-ROLE-224 | Assign Total Control tidak menulis entry ke Changelog: User > Role | P2 | E2E | TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | FE+BE |
| TC-GS-ROLE-225 | Modified By dan Last Updated hanya diperbarui oleh Assign | P2 | E2E | TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | FE+BE |
| TC-GS-ROLE-226 | Assign Role membuka menu modul untuk target pada request berikutnya | P0 | E2E | TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | FE+BE |
| TC-GS-ROLE-227 | Remove baris role menyembunyikan menu modul target | P0 | E2E | TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | FE+BE |
| TC-GS-ROLE-228 | Edit CRUD berlaku pada request berikutnya tanpa logout | P1 | E2E | TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | FE+BE |
| TC-GS-ROLE-229 | Assign Total Control menampilkan General Settings dan Activity Log untuk target | P1 | E2E | TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | FE+BE |
| TC-GS-ROLE-230 | Remove Total Control mengosongkan sidebar target | P1 | E2E | TC-GS-ROLE-E2E-080-sync-sidebar-akses-menu-realtime-pasca-mutasi | FE+BE |
| TC-GS-ROLE-231 | Edit CRUD dari Detail tercermin di User Detail Tab Role | P1 | E2E | TC-GS-ROLE-E2E-081-sync-dua-arah-dengan-modul-user-detail-tab-role | FE+BE |
| TC-GS-ROLE-232 | Edit dari User Detail Tab Role tercermin di Detail role | P1 | E2E | TC-GS-ROLE-E2E-081-sync-dua-arah-dengan-modul-user-detail-tab-role | FE+BE |
| TC-GS-ROLE-233 | Given Remove Access Global Settings di modul User untuk user Total Control | P1 | E2E | TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | FE+BE |
| TC-GS-ROLE-234 | Given Remove Access Global Settings untuk user tanpa access level | P1 | E2E | TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | FE+BE |
| TC-GS-ROLE-235 | Given user dihapus di modul User | P1 | E2E | TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | FE+BE |
| TC-GS-ROLE-236 | Given user dinonaktifkan di modul User | P1 | E2E | TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | FE+BE |
| TC-GS-ROLE-237 | Rename Position tercermin di Tab Total Control | P2 | E2E | TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field | FE+BE |
| TC-GS-ROLE-238 | Format tanggal mengikuti General Settings pada Tab Total Control dan filternya | P2 | E2E | TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field | FE+BE |
| TC-GS-ROLE-239 | Format tanggal mengikuti General Settings pada Modal Changelog dan filternya | P2 | E2E | TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field | FE+BE |
| TC-GS-ROLE-240 | Kolom Custom Field mengikuti status Custom Field | P3 | E2E | TC-GS-ROLE-E2E-083-sinkronisasi-atribut-user-format-tanggal-dan-custom-field | FE+BE |
| TC-GS-ROLE-241 | Notifikasi in-app ke target untuk Remove Total Control | P1 | E2E | TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-242 | Notifikasi in-app ke target untuk Remove Read Only | P1 | E2E | TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-243 | Notifikasi in-app ke target untuk Auto-Revert Total Control | P1 | E2E | TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-244 | Notifikasi in-app ke target untuk Auto-Revert Read Only | P1 | E2E | TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-245 | Bulk Remove campuran mengirim notifikasi per target tier | P1 | E2E | TC-GS-ROLE-E2E-084-in-app-notifications-pada-remove-dan-auto-revert | FE+BE |
| TC-GS-ROLE-246 | Fitur ber-plan tetap muncul sebagai role di semua plan | P2 | E2E | TC-GS-ROLE-E2E-085-plan-gating-dan-isolasi-scope-produk | FE+BE |
| TC-GS-ROLE-247 | Edit CRUD diri sendiri lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-248 | Edit CRUD Default User lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-249 | Edit CRUD target Total Control oleh Manage user and role lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier | FE+BE |
| TC-GS-ROLE-250 | Remove baris role Default User lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-251 | Remove baris role diri sendiri lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-252 | Remove baris role target Read Only oleh Manage user and role lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier | FE+BE |
| TC-GS-ROLE-253 | Remove access level Default User lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-254 | Remove access level diri sendiri lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-255 | Assign Role ke diri sendiri lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-086-defense-in-depth-proteksi-self-dan-default-user | FE+BE |
| TC-GS-ROLE-256 | Assign/Remove access level oleh Manage user and role lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier | FE+BE |
| TC-GS-ROLE-257 | Aksi tulis Detail oleh Read Only lewat permintaan langsung ditolak | P0 | E2E | TC-GS-ROLE-E2E-087-defense-in-depth-otorisasi-aktor-dan-target-tier | FE+BE |
| TC-GS-ROLE-258 | Nilai Read=false pada permintaan Edit CRUD diabaikan | P0 | E2E | TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid | FE+BE |
| TC-GS-ROLE-259 | Flag kolom yang tidak berlaku diabaikan | P0 | E2E | TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid | FE+BE |
| TC-GS-ROLE-260 | Bulk Remove berisi baris Default User lewat permintaan langsung | P0 | E2E | TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid | FE+BE |
| TC-GS-ROLE-261 | Partial success Bulk Remove menampilkan toast sukses parsial | P1 | E2E | TC-GS-ROLE-E2E-088-defense-in-depth-integritas-payload-dan-kolom-invalid | FE+BE |
| TC-GS-ROLE-262 | Data Role & Permission client lain tidak dapat dibaca | P1 | E2E | TC-GS-ROLE-E2E-089-defense-in-depth-keamanan-isolasi-multi-tenant | FE+BE |
| TC-GS-ROLE-263 | Assign Total Control saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level | FE+BE |
| TC-GS-ROLE-264 | Assign Read Only saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level | FE+BE |
| TC-GS-ROLE-265 | Remove Total Control saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level | FE+BE |
| TC-GS-ROLE-266 | Remove Read Only saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-090-client-suspended-blokir-operasi-tulis-access-level | FE+BE |
| TC-GS-ROLE-267 | Assign Role saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-268 | Edit CRUD saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-269 | Remove baris role saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-270 | Bulk Remove saat client suspended ditolak | P1 | E2E | TC-GS-ROLE-E2E-091-client-suspended-blokir-operasi-tulis-detail-dan-bulk-remove | FE+BE |
| TC-GS-ROLE-271 | Client suspended tetap dapat melihat Role & Permission | P2 | E2E | TC-GS-ROLE-E2E-092-client-suspended-akses-baca-murni-seluruh-surface | FE+BE |
| TC-GS-ROLE-272 | Edit CRUD pada nilai baris yang sudah diubah admin lain sejak render — last-write-wins | P1 | E2E | TC-GS-ROLE-E2E-093-konkurensi-edit-crud-last-write-wins-dan-target-stale | FE+BE |
| TC-GS-ROLE-273 | Edit CRUD target yang status Total Control-nya berubah sejak render (aktor non-Total Control) | P1 | E2E | TC-GS-ROLE-E2E-093-konkurensi-edit-crud-last-write-wins-dan-target-stale | FE+BE |
| TC-GS-ROLE-274 | Remove baris yang target-nya menjadi Total Control sejak render (aktor non-Total Control) | P1 | E2E | TC-GS-ROLE-E2E-094-konkurensi-remove-row-detail-stale-dan-auto-revert | FE+BE |
| TC-GS-ROLE-275 | Remove access level saat target sudah di-Remove admin lain sejak render | P1 | E2E | TC-GS-ROLE-E2E-095-konkurensi-remove-access-level-stale-toast-404-netral | FE+BE |
| TC-GS-ROLE-276 | Remove baris yang sudah dihapus admin lain dianggap sukses | P1 | E2E | TC-GS-ROLE-E2E-094-konkurensi-remove-row-detail-stale-dan-auto-revert | FE+BE |
| TC-GS-ROLE-277 | Auto-revert menghilangkan user dari Tab Total Control sesi admin lain secara realtime | P1 | E2E | TC-GS-ROLE-E2E-096-konkurensi-sse-auto-revert-dan-boundary-default-user | FE+BE |
| TC-GS-ROLE-278 | Default User tetap Total Control setelah semua Total Control lain di-Remove | P2 | E2E | TC-GS-ROLE-E2E-096-konkurensi-sse-auto-revert-dan-boundary-default-user | FE+BE |
| TC-GS-ROLE-279 | Assign Role concurrent ke user yang sama oleh dua admin | P1 | E2E | TC-GS-ROLE-E2E-097-konkurensi-assign-concurrent-rebutan-kandidat-user | FE+BE |
| TC-GS-ROLE-280 | Assign Total Control concurrent ke user yang sama oleh dua admin | P1 | E2E | TC-GS-ROLE-E2E-097-konkurensi-assign-concurrent-rebutan-kandidat-user | FE+BE |
| TC-GS-ROLE-281 | Detail — checkbox CRUD rata tengah di sel | P3 | E2E | TC-GS-ROLE-E2E-004-screening-detail-role-dan-kolom-crud-enam-role | FE+BE |
| TC-GS-ROLE-282 | Menu General Settings dan Activity Log tidak tampil untuk pemegang role individual tanpa access level | P1 | E2E | TC-GS-ROLE-E2E-008-landing-state-user-tanpa-role-dan-aktivasi-akses | FE+BE |
| TC-GS-ROLE-283 | Assign Total Control Global Settings tidak mengubah akses produk lain | P2 | E2E | TC-GS-ROLE-E2E-085-plan-gating-dan-isolasi-scope-produk | FE+BE |
| TC-GS-ROLE-284 | Edit CRUD pada baris yang sudah dihapus admin lain | P1 | E2E | TC-GS-ROLE-E2E-093-konkurensi-edit-crud-last-write-wins-dan-target-stale | FE+BE |
| TC-GS-ROLE-285 | Mobile — card Tab Total Control dan Tab Read Only | P2 | E2E | TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-286 | Mobile — card Tab System dan toolbar mobile | P2 | E2E | TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-287 | Mobile — Popup Table User Picker dan Modal Changelog tampil sebagai bottom sheet | P3 | E2E | TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-288 | Mobile — Detail Import data menampilkan toggle Create dan Read saja | P2 | E2E | TC-GS-ROLE-E2E-013-mobile-card-list-bottom-sheet-dan-toolbar | FE+BE |
| TC-GS-ROLE-289 | System Log aktor dan Activity Log untuk Assign/Remove/Auto-Revert Read Only | P1 | E2E | TC-GS-ROLE-E2E-078-audit-log-lintas-modul-system-log-dan-activity-log | FE+BE |
| TC-GS-ROLE-290 | Changelog: User > Role mencatat Assign/Remove baris role; Changelog: User mencatat Auto-Revert | P2 | E2E | TC-GS-ROLE-E2E-079-audit-log-immutability-rename-user-dan-fan-out-modul-user | FE+BE |
| TC-GS-ROLE-291 | Given Remove Access Global Settings untuk user Read Only | P1 | E2E | TC-GS-ROLE-E2E-082-cascade-remove-access-gs-dan-hapus-user | FE+BE |
| TC-GS-ROLE-292 | Assign Total Control saat Access Global Settings user terpilih dicabut sebelum submit | P1 | E2E | TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran | FE+BE |
| TC-GS-ROLE-293 | Sort kolom Popup Assign | P2 | E2E | TC-GS-ROLE-E2E-025-assign-total-control-picker-sorting-pagination-retensi | FE+BE |
| TC-GS-ROLE-294 | Bulk Remove tepat 1 baris memakai dialog single (target bukan Total Control/Read Only) | P1 | E2E | TC-GS-ROLE-E2E-056-bulk-remove-tepat-satu-baris-fallback-dialog-single | FE+BE |
| TC-GS-ROLE-295 | Bulk Remove tepat 1 baris target Read Only memakai dialog single auto-revert | P1 | E2E | TC-GS-ROLE-E2E-056-bulk-remove-tepat-satu-baris-fallback-dialog-single | FE+BE |
| TC-GS-ROLE-296 | Bulk Remove saat status Total Control target berubah antara render dan submit | P1 | E2E | TC-GS-ROLE-E2E-058-bulk-remove-concurrency-d6-dan-partial-zero-success | FE+BE |
| TC-GS-ROLE-297 | Remove baris oleh Total Control saat target menjadi Total Control antara render dan submit | P1 | E2E | TC-GS-ROLE-E2E-094-konkurensi-remove-row-detail-stale-dan-auto-revert | FE+BE |
| TC-GS-ROLE-298 | Remove access level saat tier target berbeda dari tab yang dirender | P1 | E2E | TC-GS-ROLE-E2E-039-remove-access-level-tier-berbeda-toast-404-netral | FE+BE |
| TC-GS-ROLE-299 | Bulk Remove saat semua baris ditolak per baris (0 berhasil) | P1 | E2E | TC-GS-ROLE-E2E-058-bulk-remove-concurrency-d6-dan-partial-zero-success | FE+BE |
| TC-GS-ROLE-300 | Assign Total Control saat dua user terpilih dihapus admin lain sebelum submit (alert jamak) | P1 | E2E | TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10 | FE+BE |
| TC-GS-ROLE-301 | Assign Total Control saat dua user terpilih menjadi tidak eligible sebelum submit (alert jamak) | P1 | E2E | TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran | FE+BE |
| TC-GS-ROLE-302 | Assign Total Control dengan campuran user dihapus dan user tidak eligible dalam satu submit | P1 | E2E | TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran | FE+BE |
| TC-GS-ROLE-303 | Download Detail "Manage user and role" memakai nama file Title-Case-hyphen | P2 | E2E | TC-GS-ROLE-E2E-072-tabel-detail-setup-kolom-kunci-crud-dan-download | mock |
| TC-GS-ROLE-304 | Assign Total Control saat tiga user terpilih dihapus admin lain sebelum submit (alert jamak ≥3) | P2 | E2E | TC-GS-ROLE-E2E-028-assign-total-control-validasi-stale-user-v10 | FE+BE |
| TC-GS-ROLE-305 | Assign Total Control saat tiga user terpilih menjadi tidak eligible sebelum submit (alert jamak ≥3) | P2 | E2E | TC-GS-ROLE-E2E-029-assign-total-control-validasi-ineligible-user-v11-dan-campuran | FE+BE |
