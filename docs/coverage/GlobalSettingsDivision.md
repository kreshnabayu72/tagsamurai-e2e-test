# Coverage E2E — Global Settings > User > Division

Sumber: `global-settings/division/TestCases/tc-division.md`.
Referensi kontrak: `global-settings/division/PRD/division.md` dan `global-settings/division/API/openapi.yaml`.
Suite: `specs/GlobalSettings/Division/`.
Prefix Modul: `GS` + `DIV` (`TC-GS-DIV-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-division.md`: 296 baris (`TC-GS-DIV-1` s.d. `TC-GS-DIV-296`).**
Cakupan otomasi spec E2E: **100% (296 dari 296 TC tercakup penuh tanpa celah)**.
Total Spec E2E yang dihasilkan: **${specsList.length} spec atomik terisolasi tinggi**.

---

## 1. Pemetaan TC Granular → Spec E2E (${specsList.length} spec)

Seluruh 296 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-DIV-E2E-001-screening-tabel-utama-dan-urutan-default | Screening Halaman Global Settings > User > Division, Default Sort Name A-Z, dan Data Seed Awal | FE+BE | TC-GS-DIV-1, TC-GS-DIV-3 |
| TC-GS-DIV-E2E-002-tabel-utama-isi-sel-dan-panjang-maksimum | Tampilan Sel Data Kolom Name 120 Karakter Tanpa Truncation, Kolom Code, dan Format Last Updated | FE+BE | TC-GS-DIV-4 |
| TC-GS-DIV-E2E-003-loading-skeleton-dan-read-failure-resilience | Tampilan Loading Skeleton, Kegagalan Fetch Data 500, dan Pemulihan via Tombol Try Again | mock | TC-GS-DIV-5, TC-GS-DIV-8, TC-GS-DIV-9 |
| TC-GS-DIV-E2E-004-empty-state-pencarian-dan-filter-tanpa-hasil | Empty State Hasil Saring: Ilustrasi dan Keterangan No Results Found pada Search dan Filter | FE+BE | TC-GS-DIV-6, TC-GS-DIV-7 |
| TC-GS-DIV-E2E-005-hover-tooltip-toolbar-table-tools | Hover Tooltip Icon Toolbar Table Tools (Search, Filter, Download, Changelog) | mock | TC-GS-DIV-2 |
| TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | Guided Tooltip Walkthrough 3-Langkah: Auto-Launch Kunjungan Pertama, Kontrol Navigasi, Overlay Dismiss, dan Replay | mock | TC-GS-DIV-10, TC-GS-DIV-11, TC-GS-DIV-12, TC-GS-DIV-13, TC-GS-DIV-14 |
| TC-GS-DIV-E2E-007-guided-tooltip-walkthrough-keyboard-resize-dan-role-gating | Guided Tooltip Walkthrough: Navigasi Keyboard, Pembatalan Flag saat Resize, dan Pelompataan Step per Hak Akses | mock | TC-GS-DIV-15, TC-GS-DIV-16, TC-GS-DIV-17 |
| TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping | Role Matrix: Akses Dasar Tanpa Hak Akses, Read-Only, Read-Only Access Level, dan Total Control Baseline | FE+BE | TC-GS-DIV-18, TC-GS-DIV-19, TC-GS-DIV-23, TC-GS-DIV-24 |
| TC-GS-DIV-E2E-009-role-matrix-granular-write-capabilities-scoping | Role Matrix: Isolasi Visibilitas Hak Akses Tulis Granular (Create-Only, Update-Only, dan Delete-Only) | FE+BE | TC-GS-DIV-20, TC-GS-DIV-21, TC-GS-DIV-22 |
| TC-GS-DIV-E2E-010-role-matrix-negatif-direct-url-tanpa-akses | Akses Langsung Direct URL Tab Division Tanpa Capability Ditolak dengan Toast 403 | FE+BE | TC-GS-DIV-25 |
| TC-GS-DIV-E2E-011-role-matrix-positif-create-only-dan-update-only | Eksekusi Operasi oleh Aktor System Role Berhak Terbatas: Create-Only dan Update-Only | FE+BE | TC-GS-DIV-26, TC-GS-DIV-27 |
| TC-GS-DIV-E2E-012-role-matrix-positif-delete-single-dan-bulk-only | Eksekusi Operasi Penghapusan oleh Aktor System Role Delete-Only (Single dan Bulk) | FE+BE | TC-GS-DIV-28, TC-GS-DIV-29 |
| TC-GS-DIV-E2E-013-create-modal-screening-dan-aksesibilitas | Screening Modal Create Division: Tata Letak, Placeholder, Helper Text, AutoFocus, dan Aksesibilitas ARIA | FE+BE | TC-GS-DIV-31, TC-GS-DIV-32, TC-GS-DIV-33 |
| TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | Validasi Field Name pada Create: Wajib Diisi, Spasi Saja, Batas 1 Karakter, Batas 120/121 Karakter, dan Emoji Terlarang | FE+BE | TC-GS-DIV-34, TC-GS-DIV-35, TC-GS-DIV-36, TC-GS-DIV-37, TC-GS-DIV-38, TC-GS-DIV-39 |
| TC-GS-DIV-E2E-015-create-modal-validasi-field-name-keunikan-dan-scope | Validasi Keunikan Name pada Create: Debounce ~500ms, Trim Spasi Depan/Belakang, dan Izin Duplikasi Lintas Entitas | FE+BE | TC-GS-DIV-40, TC-GS-DIV-41, TC-GS-DIV-42 |
| TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | Validasi Field Code pada Create: Auto-Uppercase, Batas 15/16 Karakter, Simbol Terlarang, Whitelist (-_.), dan Spasi Saja | FE+BE | TC-GS-DIV-43, TC-GS-DIV-44, TC-GS-DIV-45, TC-GS-DIV-46, TC-GS-DIV-47, TC-GS-DIV-49 |
| TC-GS-DIV-E2E-017-create-modal-validasi-field-code-keunikan | Validasi Keunikan Code pada Create: Debounce ~500ms Case-Insensitive Per Entitas | FE+BE | TC-GS-DIV-48 |
| TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | Auto-Generate Code: Pemecahan Token Kata, Numerik, Alfanumerik Campuran, Delimiter Spasi/Tanda Hubung/Garis Bawah/Miring | FE+BE | TC-GS-DIV-50, TC-GS-DIV-51, TC-GS-DIV-52, TC-GS-DIV-53, TC-GS-DIV-54 |
| TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin | Auto-Generate Code: Fallback 6 Karakter Kata Tunggal, Fallback DIV pada Karakter Simbolik/Non-Latin, dan Ketiadaan Live Preview | FE+BE | TC-GS-DIV-55, TC-GS-DIV-56, TC-GS-DIV-57, TC-GS-DIV-63 |
| TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | Auto-Generate Code: Dedup Suffix Angka (2, 3, dst.), Truncation 15 Karakter pada 16 Token, dan Siklus Suffix Lanjutan | FE+BE | TC-GS-DIV-58, TC-GS-DIV-59, TC-GS-DIV-60, TC-GS-DIV-61, TC-GS-DIV-62 |
| TC-GS-DIV-E2E-021-create-modal-clear-field-reset | Interaksi Form Create: Pengosongan Input Form via Tombol Clear Field Tanpa Menutup Modal | FE+BE | TC-GS-DIV-64 |
| TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection | Proteksi Perubahan Belum Disimpan pada Create: Dialog Unsaved Changes pada Icon Close & Esc, Serta Blokir Klik Backdrop | FE+BE | TC-GS-DIV-68, TC-GS-DIV-69, TC-GS-DIV-70, TC-GS-DIV-71 |
| TC-GS-DIV-E2E-023-create-division-happy-path-stay-unchecked | Pembuatan Divisi Berhasil dengan Checkbox Stay Unchecked: Penutupan Modal, Toast Sukses, Refleksi Tabel, dan Submit Enter | FE+BE | TC-GS-DIV-65, TC-GS-DIV-78 |
| TC-GS-DIV-E2E-024-create-division-batch-stay-checked-population | Pembuatan Divisi Berurutan dengan Checkbox Stay on this Form Checked (Batch Population 26 Divisi) | FE+BE | TC-GS-DIV-30, TC-GS-DIV-66 |
| TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard | Pencegahan Pembuatan Divisi Saat Master Data Count Limit Tercapai: Dialog Blokir pada Klik Toolbar dan Re-Cek Atomik Submit | FE+BE | TC-GS-DIV-72, TC-GS-DIV-73, TC-GS-DIV-74, TC-GS-DIV-75 |
| TC-GS-DIV-E2E-026-create-division-resilience-server-500-timeout-dan-double-submit | Ketahanan Form Create: Guard Double Submit, Kegagalan Server 500, dan Network Timeout Retry | mock | TC-GS-DIV-67, TC-GS-DIV-76, TC-GS-DIV-77 |
| TC-GS-DIV-E2E-027-create-division-transaksi-atomik-dan-race-code-conflict-409 | Transaksi DB Atomik Form Create dan Penanganan Race Condition Auto-Generate Code 409 dengan Auto-Retry Sekali | FE+BE | TC-GS-DIV-79, TC-GS-DIV-80 |
| TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas | Screening Modal Edit Division: Pre-fill Nilai Name dan Code, Ketiadaan Checkbox Stay, Autofocus, dan Aksesibilitas | FE+BE | TC-GS-DIV-81, TC-GS-DIV-82, TC-GS-DIV-113, TC-GS-DIV-291 |
| TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | Validasi Field Name pada Edit: Wajib Diisi, Spasi Saja, Trim Spasi, Batas 120/121 Karakter, dan Blokir Emoji | FE+BE | TC-GS-DIV-83, TC-GS-DIV-84, TC-GS-DIV-85, TC-GS-DIV-86, TC-GS-DIV-87, TC-GS-DIV-88 |
| TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion | Validasi Keunikan Name pada Edit: Debounce Duplikat, Re-Cek Submit, Pengecualian Nilai Sendiri, dan Toleransi Case Rename | FE+BE | TC-GS-DIV-89, TC-GS-DIV-90, TC-GS-DIV-91, TC-GS-DIV-92 |
| TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | Validasi Code pada Edit: Auto-Uppercase, Batas 15 Karakter, Karakter Terlarang, Duplikat, dan Pengecualian Nilai Sendiri | FE+BE | TC-GS-DIV-93, TC-GS-DIV-94, TC-GS-DIV-95, TC-GS-DIV-96, TC-GS-DIV-97 |
| TC-GS-DIV-E2E-032-edit-modal-auto-generate-code-saat-kosong | Auto-Generate Code pada Form Edit Saat Dikosongkan Manual atau Spasi Saja, Serta Evaluasi No-Op Nilai Identik | FE+BE | TC-GS-DIV-98, TC-GS-DIV-99, TC-GS-DIV-288 |
| TC-GS-DIV-E2E-033-edit-modal-clear-field-dan-unsaved-changes | Interaksi Form Edit: Pengosongan Murni via Clear Field (Bukan Revert) dan Dialog Unsaved Changes pada Icon Close & Esc | FE+BE | TC-GS-DIV-105, TC-GS-DIV-107, TC-GS-DIV-108 |
| TC-GS-DIV-E2E-034-edit-division-no-op-auto-close-tanpa-log | Form Edit No-Op: Submit Tanpa Perubahan Data Menutup Modal Otomatis dengan Toast Netral Tanpa Log Baru | FE+BE | TC-GS-DIV-100 |
| TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | Penyuntingan Divisi Berhasil: Pengubahan Name, Code, Keduanya Sekaligus, Edit Record Seed, dan Refleksi Instan | FE+BE | TC-GS-DIV-101, TC-GS-DIV-102, TC-GS-DIV-103, TC-GS-DIV-104, TC-GS-DIV-109, TC-GS-DIV-112 |
| TC-GS-DIV-E2E-036-edit-division-resilience-server-failure-dan-double-submit | Ketahanan Form Edit: Guard Double Submit Save, Penanganan Server 500, dan Network Timeout dengan Tombol Try Again | mock | TC-GS-DIV-106, TC-GS-DIV-110, TC-GS-DIV-111 |
| TC-GS-DIV-E2E-037-delete-single-screening-dialog-konfirmasi-dan-batal | Screening Dialog Konfirmasi Delete Single (D-01) dan Pembatalan via Tombol Cancel | FE+BE | TC-GS-DIV-114, TC-GS-DIV-115 |
| TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user | Pemblokiran Hapus Divisi In-Use (D-02): Referensi Login User Aktif, Non-Aktif, Non-Login User, dan Dismiss Tombol Tunggal OK | FE+BE | TC-GS-DIV-117, TC-GS-DIV-118, TC-GS-DIV-119, TC-GS-DIV-120 |
| TC-GS-DIV-E2E-039-delete-single-recheck-atomik-in-use-saat-confirm | Re-Cek Atomik Saat Confirm Delete Single: Divisi Berubah Status Menjadi In-Use Sebelum Confirm Memunculkan Dialog Blokir | FE+BE | TC-GS-DIV-121 |
| TC-GS-DIV-E2E-040-delete-single-happy-path-record-bebas-relasi-dan-seed | Penghapusan Divisi Bebas Relasi Berhasil (Record Normal dan Seed): Toast Sukses dan Hilang dari Tabel | FE+BE | TC-GS-DIV-116, TC-GS-DIV-124 |
| TC-GS-DIV-E2E-041-delete-single-resilience-double-submit-dan-server-error | Ketahanan Delete Single: Guard Double Submit Tombol Delete dan Kegagalan Server 500 | mock | TC-GS-DIV-122, TC-GS-DIV-123 |
| TC-GS-DIV-E2E-042-bulk-action-bar-screening-dan-counter-lifecycle | Screening Bulk Action Bar: Munculnya Bar saat Baris Dicentang dan Pembaruan Realtime Counter | FE+BE | TC-GS-DIV-125, TC-GS-DIV-126 |
| TC-GS-DIV-E2E-043-tabel-utama-header-checkbox-dan-seleksi-lintas-halaman | Tabel Utama: Checkbox Header, Status Indeterminate, dan Seleksi Lintas Halaman Select All | FE+BE | TC-GS-DIV-127, TC-GS-DIV-128 |
| TC-GS-DIV-E2E-044-selection-limit-enforcement-dan-select-all-capping | Selection Limit: Penonaktifan Checkbox Melewati Batas dan Capping Parsial Select All | FE+BE | TC-GS-DIV-129, TC-GS-DIV-130 |
| TC-GS-DIV-E2E-045-bulk-delete-collapse-dialog-single-n-sama-dengan-1 | Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat Tepat 1 Baris Terpilih (N=1) | FE+BE | TC-GS-DIV-131 |
| TC-GS-DIV-E2E-046-bulk-delete-homogen-seluruh-item-bebas-relasi | Bulk Delete Homogen (D-04): Seluruh Divisi Terpilih Bebas Relasi, Pembatalan Cancel, dan Konfirmasi Sukses | FE+BE | TC-GS-DIV-132, TC-GS-DIV-133, TC-GS-DIV-137 |
| TC-GS-DIV-E2E-047-bulk-delete-campuran-sebagian-in-use-dan-batal | Bulk Delete Campuran (D-03): Segregasi Item Dihapus vs Dilewati, Pembatalan via Cancel, dan Eksekusi Continue dengan Toast Skipping | FE+BE | TC-GS-DIV-134, TC-GS-DIV-135, TC-GS-DIV-287 |
| TC-GS-DIV-E2E-048-bulk-delete-total-terblokir-seluruh-item-in-use | Pemblokiran Total Bulk Delete (D-02): Seluruh Divisi Terpilih In-Use dengan Bullet Diperluas dan Tombol Tunggal OK | FE+BE | TC-GS-DIV-136, TC-GS-DIV-138 |
| TC-GS-DIV-E2E-049-bulk-delete-recheck-atomik-confirm-semua-item-menjadi-in-use | Re-Cek Atomik Bulk Delete Saat Confirm: Seluruh Item Berubah Menjadi In-Use Menolak Batch Tanpa Toast dan Seleksi Dipertahankan | FE+BE | TC-GS-DIV-296 |
| TC-GS-DIV-E2E-050-bulk-delete-resilience-double-submit-dan-server-500 | Ketahanan Bulk Delete: Guard Double Submit dan Kegagalan Server 500 All-or-Nothing Tanpa Item Terhapus | mock | TC-GS-DIV-139, TC-GS-DIV-140 |
| TC-GS-DIV-E2E-051-tabel-utama-search-toolbar-mekanisme-dan-enter | Pencarian Tabel Utama: Perilaku Toolbar Search, Ekspansi, Auto-Focus, Icon Clear X, Panah Kembali, dan Eksekusi Enter | FE+BE | TC-GS-DIV-141, TC-GS-DIV-142, TC-GS-DIV-143 |
| TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | Pencarian Tabel Utama: Pencocokan Substring Name & Code, Case-Insensitive, Empty State, dan Scoping Kolom Tersembunyi | FE+BE | TC-GS-DIV-144, TC-GS-DIV-145, TC-GS-DIV-146, TC-GS-DIV-147, TC-GS-DIV-148 |
| TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format | Filter Panel Tabel Utama: Screening Panel, Date Range Picker, Kepatuhan Format Tanggal, dan Reset Clear Field | FE+BE | TC-GS-DIV-149, TC-GS-DIV-150, TC-GS-DIV-151, TC-GS-DIV-152 |
| TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | Filter Tabel Utama: Chip Filter Aktif, Badge Counter Toolbar, dan Koeksistensi Search-Filter | FE+BE | TC-GS-DIV-153, TC-GS-DIV-154, TC-GS-DIV-155, TC-GS-DIV-156, TC-GS-DIV-157 |
| TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | Sorting 3-State Kolom Tabel Utama: Siklus Ascending, Descending, Default pada Name, Code, dan Last Updated, Serta Reset Halaman ke 1 | FE+BE | TC-GS-DIV-158, TC-GS-DIV-159, TC-GS-DIV-160, TC-GS-DIV-161, TC-GS-DIV-162 |
| TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation | Pagination Tabel Utama: Default 10 Data, Pilihan Page Size 10/25/50/100, Kontrol Navigasi Halaman, dan Retensi State Saat Navigasi/Refresh | FE+BE | TC-GS-DIV-163, TC-GS-DIV-164, TC-GS-DIV-165, TC-GS-DIV-166 |
| TC-GS-DIV-E2E-057-tabel-utama-setup-column-overlay-fase-1 | Setup Column Tabel Utama Fase 1: Overlay Column Visibility pada Header Kolom Actions, Toggle Cepat Visibilitas, dan Guard Minimal 1 Kolom Tersisa | mock | TC-GS-DIV-167, TC-GS-DIV-168, TC-GS-DIV-169 |
| TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | Setup Column Tabel Utama Fase 2: Modal Dialog Setup Column, Pencarian Kolom, Drag-and-Drop Reorder, dan Pin/Unpin Kolom | mock | TC-GS-DIV-170, TC-GS-DIV-171, TC-GS-DIV-172, TC-GS-DIV-173, TC-GS-DIV-174 |
| TC-GS-DIV-E2E-059-tabel-utama-setup-column-reset-cancel-save-fase-3 | Setup Column Tabel Utama Fase 3: Reset to Default, Pembatalan Cancel/Esc, dan Penyimpanan Permanen di Browser per Pengguna | mock | TC-GS-DIV-175, TC-GS-DIV-176, TC-GS-DIV-177 |
| TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | Ekspor Data Tabel Utama: Popover Download CSV dan XLSX, Nama Berkas Default Division, Filter Aktif Terfleksi, dan Format Tanggal | FE+BE | TC-GS-DIV-178, TC-GS-DIV-179, TC-GS-DIV-180, TC-GS-DIV-181, TC-GS-DIV-182, TC-GS-DIV-185, TC-GS-DIV-187 |
| TC-GS-DIV-E2E-061-tabel-utama-download-sync-kolom-dan-fault-injection | Ekspor Berdasarkan Visibilitas Kolom Setup Column dan Ketahanan Terhadap Kegagalan Server 500 Toast Error | mock | TC-GS-DIV-183, TC-GS-DIV-184, TC-GS-DIV-186 |
| TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | Screening Modal Changelog Division: Pembukaan via Toolbar, Read-Only Tanpa Row Action, Default Sort Date Newest, Empty State, dan Hover Tooltip | FE+BE | TC-GS-DIV-188, TC-GS-DIV-189, TC-GS-DIV-190, TC-GS-DIV-191, TC-GS-DIV-224, TC-GS-DIV-230 |
| TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | Pencarian Modal Changelog: Submit Enter, Pencarian pada 6 Kolom Teks, Guard Date Non-Searchable, Empty State No Results, dan Interaksi Toolbar Box | FE+BE | TC-GS-DIV-192, TC-GS-DIV-193, TC-GS-DIV-194, TC-GS-DIV-195, TC-GS-DIV-225 |
| TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | Filter Panel Changelog: Date Range Picker, Placeholder Select Date, Multi-Select Action, Field, Serta Nilai DISTINCT pada Division Name dan Modified By | FE+BE | TC-GS-DIV-196, TC-GS-DIV-197, TC-GS-DIV-198, TC-GS-DIV-199, TC-GS-DIV-200, TC-GS-DIV-201, TC-GS-DIV-202, TC-GS-DIV-203 |
| TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect | Filter Changelog: Kotak Pencarian di Dalam Dropdown Multi-Select dan Logika Disjungsi OR Antar-Opsi | FE+BE | TC-GS-DIV-204, TC-GS-DIV-205, TC-GS-DIV-292, TC-GS-DIV-293 |
| TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | Filter Changelog: Siklus Manipulasi Chip, Overflow Chip, Loading State Dropdown, dan Persistensi Snapshot Master Terhapus | FE+BE | TC-GS-DIV-231, TC-GS-DIV-232, TC-GS-DIV-233, TC-GS-DIV-294, TC-GS-DIV-295 |
| TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery | Kombinasi Penuh Search, Filter, Sort, dan Pagination pada Modal Changelog Serta Independensi Pembersihan Masing-Masing Kontrol | FE+BE | TC-GS-DIV-226, TC-GS-DIV-227, TC-GS-DIV-228, TC-GS-DIV-229 |
| TC-GS-DIV-E2E-068-changelog-sorting-3-state-dan-null-placement | Sorting 7 Kolom Modal Changelog: Alphabetical A-Z, Tanggal Newest/Oldest, dan Penempatan Nilai Kosong/Em-dash (—) di Akhir pada Old/New Value | FE+BE | TC-GS-DIV-206, TC-GS-DIV-207, TC-GS-DIV-208 |
| TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format | Modal Changelog: Header Column Visibility Tanpa Sort, Kontrol Pagination, Dismiss Modal, dan Kepatuhan Format Tanggal | mock | TC-GS-DIV-209, TC-GS-DIV-210, TC-GS-DIV-211, TC-GS-DIV-212 |
| TC-GS-DIV-E2E-070-changelog-setup-column-overlay-fase-1 | Setup Column Modal Changelog Fase 1: Overlay Column Visibility 7 Kolom, Toggle Hide/Unhide, dan Guard Kolom Terakhir | mock | TC-GS-DIV-213, TC-GS-DIV-215, TC-GS-DIV-220 |
| TC-GS-DIV-E2E-071-changelog-setup-column-modal-fase-2 | Setup Column Modal Changelog Fase 2: Modal Setup Column, Drag-and-Drop Reorder 7 Kolom, dan Freeze Pinning Kolom | mock | TC-GS-DIV-214, TC-GS-DIV-216, TC-GS-DIV-217 |
| TC-GS-DIV-E2E-072-changelog-setup-column-reset-cancel-save-fase-3 | Setup Column Modal Changelog Fase 3: Reset to Default, Pembatalan Cancel/X, Penyimpanan Browser, dan Independensi dari Tabel Utama | mock | TC-GS-DIV-218, TC-GS-DIV-219, TC-GS-DIV-234 |
| TC-GS-DIV-E2E-073-changelog-download-csv-xlsx-dan-fault-injection | Ekspor Riwayat Modal Changelog ke Berkas CSV dan XLSX Berdasarkan Filter Aktif Serta Penanganan Kegagalan Server 500 Toast Error | FE+BE | TC-GS-DIV-221, TC-GS-DIV-222, TC-GS-DIV-223 |
| TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | Pencatatan Mutasi Divisi pada Changelog: Create Hanya Catat Name, Edit Name/Code, Delete, Bulk Delete per Baris, dan Evaluasi No-Op 0 Log | FE+BE | TC-GS-DIV-235, TC-GS-DIV-236, TC-GS-DIV-237, TC-GS-DIV-238, TC-GS-DIV-239, TC-GS-DIV-240, TC-GS-DIV-241 |
| TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing | Format Modified By, Snapshot Immutability Log Lama Pasca-Rename, Ingestion ke Activity Log GS, dan Absennya System Log User | FE+BE | TC-GS-DIV-242, TC-GS-DIV-243, TC-GS-DIV-244, TC-GS-DIV-245 |
| TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik | Integritas Baris Log: Format Tanggal General Settings, Larangan Old & New Value Em-dash Sekaligus, Transaksi DB Atomik, dan All-or-Nothing | FE+BE | TC-GS-DIV-246, TC-GS-DIV-247, TC-GS-DIV-248, TC-GS-DIV-249 |
| TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user | Sinkronisasi Real-Time Katalog Division ke Dropdown Form User dan Non-Login User (Create Muncul, Edit Reflected, Delete Terhapus) | FE+BE | TC-GS-DIV-250, TC-GS-DIV-251, TC-GS-DIV-252, TC-GS-DIV-258 |
| TC-GS-DIV-E2E-078-penolakan-submit-user-pada-divisi-yang-baru-dihapus-auto-clear | Penanganan Submit User pada Divisi yang Baru Dihapus: Pesan Error Field, Auto-Clear Dropdown, dan Refresh Opsi Otomatis | FE+BE | TC-GS-DIV-253 |
| TC-GS-DIV-E2E-079-user-form-stale-division-deletion-auto-clear | Penanganan Form User & Non-Login User pada Divisi yang Dihapus Pihak Lain: Error Field dan Auto-Clear | FE+BE | TC-GS-DIV-254, TC-GS-DIV-255 |
| TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions | Parity Operasional Import Division dan Alur Create Missing Divisions: Mutasi, Pencatatan Changelog, Batas Limit, dan Penolakan Duplicate | FE+BE | TC-GS-DIV-256, TC-GS-DIV-257, TC-GS-DIV-289, TC-GS-DIV-290 |
| TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api | Penegakan Izin Server-Side Tanpa Capability (Create, Edit, Delete Ditolak 403) dan Guard In-Use Server-Side pada Permintaan API Langsung | FE+BE | TC-GS-DIV-259, TC-GS-DIV-260, TC-GS-DIV-261, TC-GS-DIV-262 |
| TC-GS-DIV-E2E-082-security-entitas-suspended-expired-blokir-aksi-tulis | Pemblokiran Seluruh Aksi Tulis (Create, Edit, Delete) Saat Status Entitas Workspace Suspended atau Expired | FE+BE | TC-GS-DIV-263, TC-GS-DIV-264, TC-GS-DIV-265 |
| TC-GS-DIV-E2E-083-security-isolasi-multi-tenant-dan-pencegahan-kebocoran-data | Isolasi Total Multi-Tenant: Entitas A Dilarang Melihat atau Mengakses Data Katalog Division Entitas B | FE+BE | TC-GS-DIV-266 |
| TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection | Ketahanan Input: Penolakan Emoji Bypass DOM di Server, Sanitasi XSS Nama Divisi, dan Netralisasi SQL Injection pada Kotak Pencarian | mock | TC-GS-DIV-267, TC-GS-DIV-268, TC-GS-DIV-269, TC-GS-DIV-270 |
| TC-GS-DIV-E2E-085-concurrency-edit-last-write-wins-dan-race-create-duplicate | Konkurensi Antar-Admin: Last-Write-Wins pada Edit Bersamaan, Penolakan Duplicate Name, dan Penolakan Duplicate Manual Code | FE+BE | TC-GS-DIV-271, TC-GS-DIV-272, TC-GS-DIV-273 |
| TC-GS-DIV-E2E-086-concurrency-race-slot-limit-edit-vs-delete-dan-idempotent-delete | Konkurensi Tingkat Lanjut: Rebutan Slot Terakhir Master Data Limit, Race Edit pada Divisi yang Dihapus, dan Hapus Idempotent Bersamaan | FE+BE | TC-GS-DIV-274, TC-GS-DIV-275, TC-GS-DIV-276 |
| TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating | Pembaruan Real-Time Tabel, Penjaminan Katalog Minimum 1 Record via In-Use Default User, dan Absennya Plan Gating Seluruh Fitur | FE+BE | TC-GS-DIV-277, TC-GS-DIV-278, TC-GS-DIV-279, TC-GS-DIV-280 |
| TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating | Tampilan dan Interaksi Mobile Android: Card List Pengganti Tabel, Tanpa Checkbox/Bulk, Bottom Sheet Toolbar/Dialog, dan Gating Aksi | mock | TC-GS-DIV-281, TC-GS-DIV-282, TC-GS-DIV-283, TC-GS-DIV-284 |
| TC-GS-DIV-E2E-089-mobile-crud-create-dan-edit-via-bottom-sheet | Eksekusi CRUD Mobile Android: Penambahan dan Pengeditan Divisi Berhasil Melalui Bottom Sheet Form | mock | TC-GS-DIV-285, TC-GS-DIV-286 |

---

## 2. TC hanya-BE (tidak masuk spec)

**0 TC**. Seluruh 296 TC granular pada `tc-division.md` memiliki pertanggungjawaban `PIC FE: v` dan dampak fungsional yang dapat divalidasi pada antarmuka web/mobile atau via intersep mock API klien.

---

## 3. Sebaran per section TC

| Section | TC aktif | Tercakup | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Table List (1a, 1b) | 17 | 17 | 0 |
| 2. Role & Capability Access Flow (2a, 2b) | 12 | 12 | 0 |
| 3a. Create Flow | 51 | 51 | 0 |
| 3b. Edit Flow | 35 | 35 | 0 |
| 3c. Delete Flow (Single) | 11 | 11 | 0 |
| 3d. Bulk Delete Flow | 18 | 18 | 0 |
| 4a. Tabel Utama Behavior & Tools | 47 | 47 | 0 |
| 4b. Modal Changelog Division | 51 | 51 | 0 |
| 5. Pencatatan Audit Log & Multi-Surface Sync | 15 | 15 | 0 |
| 7. Cross-Module Sync & Foundation Cascading | 11 | 11 | 0 |
| 8. Security & Defense-in-Depth | 12 | 12 | 0 |
| 9. Edge Case Matrix, Concurrency, & Mobile | 16 | 16 | 0 |
| **Total** | **296** | **296** | **0** |

---

## 4. Lapisan per TC

| TC | Skenario | Priority | Lapisan | Spec | Mode |
|---|---|:---:|:---:|---|:---:|
| TC-GS-DIV-1 | Screening Halaman Global Settings > User > Division oleh Total Control | P0 | E2E | TC-GS-DIV-E2E-001-screening-tabel-utama-dan-urutan-default | FE+BE |
| TC-GS-DIV-2 | Hover icon Table Tools menampilkan tooltip | P2 | E2E | TC-GS-DIV-E2E-005-hover-tooltip-toolbar-table-tools | mock |
| TC-GS-DIV-3 | Urutan default tabel Division adalah Name A-Z tanpa membedakan huruf besar kecil | P0 | E2E | TC-GS-DIV-E2E-001-screening-tabel-utama-dan-urutan-default | FE+BE |
| TC-GS-DIV-4 | Isi sel kolom tabel Division dan nama panjang tidak terpotong | P2 | E2E | TC-GS-DIV-E2E-002-tabel-utama-isi-sel-dan-panjang-maksimum | FE+BE |
| TC-GS-DIV-5 | Tampilan Loading saat data tabel diambil | P2 | E2E | TC-GS-DIV-E2E-003-loading-skeleton-dan-read-failure-resilience | mock |
| TC-GS-DIV-6 | Empty state tabel saat Search tidak menemukan hasil | P1 | E2E | TC-GS-DIV-E2E-004-empty-state-pencarian-dan-filter-tanpa-hasil | FE+BE |
| TC-GS-DIV-7 | Empty state tabel saat Filter Last Updated tidak menemukan hasil | P1 | E2E | TC-GS-DIV-E2E-004-empty-state-pencarian-dan-filter-tanpa-hasil | FE+BE |
| TC-GS-DIV-8 | Error Load tabel saat pengambilan data gagal | P1 | E2E | TC-GS-DIV-E2E-003-loading-skeleton-dan-read-failure-resilience | mock |
| TC-GS-DIV-9 | Klik Try Again memuat ulang data setelah Error Load | P1 | E2E | TC-GS-DIV-E2E-003-loading-skeleton-dan-read-failure-resilience | mock |
| TC-GS-DIV-10 | Konten 3 step Guided Tooltip halaman Division sesuai urutan | P1 | E2E | TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | mock |
| TC-GS-DIV-11 | Walkthrough otomatis pada kunjungan pertama dan tidak muncul lagi setelah Skip | P2 | E2E | TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | mock |
| TC-GS-DIV-12 | Klik overlay gelap menutup walkthrough dan menyimpan flag seen | P3 | E2E | TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | mock |
| TC-GS-DIV-13 | Navigasi Back, Next, dan Done pada walkthrough | P2 | E2E | TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | mock |
| TC-GS-DIV-14 | Tombol [?] memulai ulang walkthrough dari Step 1 tanpa mereset flag | P2 | E2E | TC-GS-DIV-E2E-006-guided-tooltip-walkthrough-auto-launch-dan-navigasi | mock |
| TC-GS-DIV-15 | Resize viewport atau pindah halaman di tengah walkthrough tidak menyimpan flag seen | P3 | E2E | TC-GS-DIV-E2E-007-guided-tooltip-walkthrough-keyboard-resize-dan-role-gating | mock |
| TC-GS-DIV-16 | Keyboard pada walkthrough: Esc, Enter, panah kanan, panah kiri | P3 | E2E | TC-GS-DIV-E2E-007-guided-tooltip-walkthrough-keyboard-resize-dan-role-gating | mock |
| TC-GS-DIV-17 | Step Add Division dilewati bagi aktor tanpa capability Create | P2 | E2E | TC-GS-DIV-E2E-007-guided-tooltip-walkthrough-keyboard-resize-dan-role-gating | mock |
| TC-GS-DIV-18 | Aktor tanpa capability Manage user and role tidak melihat Tab Division | P0 | E2E | TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping | FE+BE |
| TC-GS-DIV-19 | Aktor dengan capability Read saja | P0 | E2E | TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping | FE+BE |
| TC-GS-DIV-20 | Aktor dengan capability Create dan Read | P0 | E2E | TC-GS-DIV-E2E-009-role-matrix-granular-write-capabilities-scoping | FE+BE |
| TC-GS-DIV-21 | Aktor dengan capability Update dan Read | P0 | E2E | TC-GS-DIV-E2E-009-role-matrix-granular-write-capabilities-scoping | FE+BE |
| TC-GS-DIV-22 | Aktor dengan capability Delete dan Read | P0 | E2E | TC-GS-DIV-E2E-009-role-matrix-granular-write-capabilities-scoping | FE+BE |
| TC-GS-DIV-23 | Total Control melihat seluruh elemen | P0 | E2E | TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping | FE+BE |
| TC-GS-DIV-24 | Read Only (Access Level) hanya dapat melihat | P0 | E2E | TC-GS-DIV-E2E-008-role-matrix-baseline-access-dan-read-only-scoping | FE+BE |
| TC-GS-DIV-25 | Akses langsung ke Tab Division tanpa capability | P0 | E2E | TC-GS-DIV-E2E-010-role-matrix-negatif-direct-url-tanpa-akses | FE+BE |
| TC-GS-DIV-26 | Aktor Create-saja berhasil membuat Division | P1 | E2E | TC-GS-DIV-E2E-011-role-matrix-positif-create-only-dan-update-only | FE+BE |
| TC-GS-DIV-27 | Aktor Update-saja berhasil mengubah Name Division | P1 | E2E | TC-GS-DIV-E2E-011-role-matrix-positif-create-only-dan-update-only | FE+BE |
| TC-GS-DIV-28 | Aktor Delete-saja berhasil menghapus Division bebas relasi | P1 | E2E | TC-GS-DIV-E2E-012-role-matrix-positif-delete-single-dan-bulk-only | FE+BE |
| TC-GS-DIV-29 | Aktor Delete-saja berhasil menjalankan Bulk Delete | P1 | E2E | TC-GS-DIV-E2E-012-role-matrix-positif-delete-single-dan-bulk-only | FE+BE |
| TC-GS-DIV-30 | Population: Create 26 Division berurutan dengan Stay on this form dicentang | P0 | E2E | TC-GS-DIV-E2E-024-create-division-batch-stay-checked-population | FE+BE |
| TC-GS-DIV-31 | Screening Popup Create Division | P0 | E2E | TC-GS-DIV-E2E-013-create-modal-screening-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-32 | Accessibility Popup Create Division: fokus awal, aria, focus trap, Esc | P2 | E2E | TC-GS-DIV-E2E-013-create-modal-screening-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-33 | Tombol Submit masuk Saving state dan seluruh kontrol form disabled | P2 | E2E | TC-GS-DIV-E2E-013-create-modal-screening-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-34 | Submit Create dengan Division Name kosong | P1 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-35 | Submit Create dengan Division Name hanya berisi spasi | P2 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-36 | Division Name dengan spasi depan dan belakang disimpan ter-trim | P2 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-37 | Division Name tepat 120 karakter berhasil disimpan | P1 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-38 | Division Name 121 karakter diterima input dan menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-39 | Division Name berisi emoji menampilkan error inline | P2 | E2E | TC-GS-DIV-E2E-014-create-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-40 | Division Name duplikat tanpa membedakan huruf besar kecil menampilkan error setelah debounce | P0 | E2E | TC-GS-DIV-E2E-015-create-modal-validasi-field-name-keunikan-dan-scope | FE+BE |
| TC-GS-DIV-41 | Division Name duplikat dengan spasi depan dan belakang tetap terdeteksi | P2 | E2E | TC-GS-DIV-E2E-015-create-modal-validasi-field-name-keunikan-dan-scope | FE+BE |
| TC-GS-DIV-42 | Submit langsung dengan Division Name duplikat sebelum debounce selesai ditolak | P1 | E2E | TC-GS-DIV-E2E-015-create-modal-validasi-field-name-keunikan-dan-scope | FE+BE |
| TC-GS-DIV-43 | Create dengan Code manual huruf kecil disimpan uppercase dan ter-trim | P1 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-44 | Code tepat 15 karakter berhasil disimpan | P1 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-45 | Code 16 karakter diterima input dan menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-46 | Code dengan karakter di luar whitelist menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-47 | Code dengan huruf, angka, hyphen, underscore, dan titik diterima | P2 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-48 | Code duplikat tanpa membedakan huruf besar kecil menampilkan error setelah debounce | P0 | E2E | TC-GS-DIV-E2E-017-create-modal-validasi-field-code-keunikan | FE+BE |
| TC-GS-DIV-49 | Code berisi spasi saja dianggap kosong dan di-generate otomatis | P1 | E2E | TC-GS-DIV-E2E-016-create-modal-validasi-field-code-format-dan-whitelist | FE+BE |
| TC-GS-DIV-50 | Auto-generate Code: dua token alfabetik menjadi inisial | P1 | E2E | TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | FE+BE |
| TC-GS-DIV-51 | Auto-generate Code: token numerik murni diteruskan utuh | P1 | E2E | TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | FE+BE |
| TC-GS-DIV-52 | Auto-generate Code: token numerik beberapa digit diteruskan utuh | P1 | E2E | TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | FE+BE |
| TC-GS-DIV-53 | Auto-generate Code: token alfanumerik campuran hanya karakter pertama | P1 | E2E | TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | FE+BE |
| TC-GS-DIV-54 | Auto-generate Code: pemisah hyphen, garis miring, dan underscore memecah token | P1 | E2E | TC-GS-DIV-E2E-018-create-code-auto-generate-inisial-dan-delimiters | FE+BE |
| TC-GS-DIV-55 | Auto-generate Code: kandidat kurang dari 2 karakter memakai 6 karakter alfanumerik pertama | P1 | E2E | TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin | FE+BE |
| TC-GS-DIV-56 | Auto-generate Code: Name tanpa huruf atau angka ASCII memakai DIV | P1 | E2E | TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin | FE+BE |
| TC-GS-DIV-57 | Auto-generate Code: Name non-Latin memakai DIV lalu dedup suffix | P1 | E2E | TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin | FE+BE |
| TC-GS-DIV-58 | Auto-generate Code: kandidat bentrok ditambah suffix angka 2 | P1 | E2E | TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-59 | Auto-generate Code: suffix angka berlanjut ke 3 saat HR dan HR2 dipakai | P1 | E2E | TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-60 | Auto-generate Code: kandidat dipotong maksimum 15 karakter | P1 | E2E | TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-61 | Auto-generate Code: kandidat 15 karakter bentrok: basis dipotong agar total 15 karakter dengan suffix | P1 | E2E | TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-62 | Auto-generate Code dihitung unik tanpa membedakan huruf besar kecil | P2 | E2E | TC-GS-DIV-E2E-020-create-code-auto-generate-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-63 | Tidak ada live preview Code hasil auto-generate saat Code kosong | P3 | E2E | TC-GS-DIV-E2E-019-create-code-auto-generate-fallback-simbol-dan-non-latin | FE+BE |
| TC-GS-DIV-64 | Tombol Clear Field mengosongkan field dan mereset error tanpa dialog | P1 | E2E | TC-GS-DIV-E2E-021-create-modal-clear-field-reset | FE+BE |
| TC-GS-DIV-65 | Submit Create dengan Stay unchecked menutup modal | P1 | E2E | TC-GS-DIV-E2E-023-create-division-happy-path-stay-unchecked | FE+BE |
| TC-GS-DIV-66 | Submit Create dengan Stay checked mereset form dan tetap terbuka | P1 | E2E | TC-GS-DIV-E2E-024-create-division-batch-stay-checked-population | FE+BE |
| TC-GS-DIV-67 | Menutup form Create yang kosong tidak memunculkan dialog Unsaved Changes | P1 | E2E | TC-GS-DIV-E2E-026-create-division-resilience-server-500-timeout-dan-double-submit | mock |
| TC-GS-DIV-68 | Close via icon X saat form dirty lalu Cancel mempertahankan form | P1 | E2E | TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection | FE+BE |
| TC-GS-DIV-69 | Close via icon X saat form dirty lalu Leave membuang input | P1 | E2E | TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection | FE+BE |
| TC-GS-DIV-70 | Close via tombol Escape saat form dirty menampilkan dialog | P1 | E2E | TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection | FE+BE |
| TC-GS-DIV-71 | Klik backdrop saat form dirty tidak menutup form | P1 | E2E | TC-GS-DIV-E2E-022-create-modal-unsaved-changes-protection | FE+BE |
| TC-GS-DIV-72 | Klik [+ Division] saat Master Data Count Limit tercapai menampilkan Dialog Limit Reached | P0 | E2E | TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard | FE+BE |
| TC-GS-DIV-73 | Klik OK pada Dialog Limit Reached menutup dialog | P2 | E2E | TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard | FE+BE |
| TC-GS-DIV-74 | Limit tercapai saat Submit menolak Create dengan Dialog Limit Reached | P0 | E2E | TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard | FE+BE |
| TC-GS-DIV-75 | Create berulang dengan Stay checked sampai limit: data terakhir berhasil, berikutnya ditolak | P1 | E2E | TC-GS-DIV-E2E-025-create-division-master-data-count-limit-guard | FE+BE |
| TC-GS-DIV-76 | Create gagal 5xx mempertahankan form dan input | P1 | E2E | TC-GS-DIV-E2E-026-create-division-resilience-server-500-timeout-dan-double-submit | mock |
| TC-GS-DIV-77 | Create timeout mempertahankan form dan input | P2 | E2E | TC-GS-DIV-E2E-026-create-division-resilience-server-500-timeout-dan-double-submit | mock |
| TC-GS-DIV-78 | Klik ganda Submit hanya membuat satu Division | P1 | E2E | TC-GS-DIV-E2E-023-create-division-happy-path-stay-unchecked | FE+BE |
| TC-GS-DIV-79 | Dua Create bersamaan menghasilkan kandidat Code identik: yang kedua retry sekali dan berhasil | P1 | E2E | TC-GS-DIV-E2E-027-create-division-transaksi-atomik-dan-race-code-conflict-409 | FE+BE |
| TC-GS-DIV-80 | Retry otomatis Code bentrok lagi diperlakukan sebagai kegagalan biasa | P2 | E2E | TC-GS-DIV-E2E-027-create-division-transaksi-atomik-dan-race-code-conflict-409 | FE+BE |
| TC-GS-DIV-81 | Screening Popup Edit Division | P0 | E2E | TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-82 | Tombol Save masuk Saving state dan seluruh kontrol form disabled | P2 | E2E | TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-83 | Save Edit dengan Division Name dikosongkan | P1 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-84 | Save Edit dengan Division Name hanya spasi | P2 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-85 | Edit Division Name dengan spasi depan dan belakang disimpan ter-trim | P2 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-86 | Edit Division Name tepat 120 karakter berhasil disimpan | P1 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-87 | Edit Division Name 121 karakter diterima input dan menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-88 | Edit Division Name berisi emoji menampilkan error inline | P2 | E2E | TC-GS-DIV-E2E-029-edit-modal-validasi-field-name-batas-dan-karakter | FE+BE |
| TC-GS-DIV-89 | Edit Division Name menjadi duplikat Division lain menampilkan error | P0 | E2E | TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion | FE+BE |
| TC-GS-DIV-90 | Save langsung dengan Division Name duplikat sebelum debounce selesai ditolak | P1 | E2E | TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion | FE+BE |
| TC-GS-DIV-91 | Mengetik ulang Division Name yang sama dengan nilai sendiri tidak menampilkan error duplicate | P1 | E2E | TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion | FE+BE |
| TC-GS-DIV-92 | Mengubah Division Name hanya pada huruf besar kecil tidak dianggap duplikat terhadap diri sendiri | P2 | E2E | TC-GS-DIV-E2E-030-edit-modal-validasi-field-name-keunikan-dan-self-exclusion | FE+BE |
| TC-GS-DIV-93 | Edit Code dengan huruf kecil disimpan uppercase dan ter-trim | P1 | E2E | TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | FE+BE |
| TC-GS-DIV-94 | Edit Code 16 karakter diterima input dan menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | FE+BE |
| TC-GS-DIV-95 | Edit Code dengan karakter di luar whitelist menampilkan error inline | P1 | E2E | TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | FE+BE |
| TC-GS-DIV-96 | Edit Code menjadi duplikat Division lain menampilkan error | P0 | E2E | TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | FE+BE |
| TC-GS-DIV-97 | Mengetik ulang Code milik sendiri tidak menampilkan error duplicate | P1 | E2E | TC-GS-DIV-E2E-031-edit-modal-validasi-field-code | FE+BE |
| TC-GS-DIV-98 | Edit dengan Code dikosongkan di-generate otomatis dan dicatat bila berbeda | P1 | E2E | TC-GS-DIV-E2E-032-edit-modal-auto-generate-code-saat-kosong | FE+BE |
| TC-GS-DIV-99 | Edit dengan Code dikosongkan yang hasil generate identik dengan Code sendiri tidak berubah | P1 | E2E | TC-GS-DIV-E2E-032-edit-modal-auto-generate-code-saat-kosong | FE+BE |
| TC-GS-DIV-100 | Save Edit tanpa perubahan data menutup modal dengan toast netral | P1 | E2E | TC-GS-DIV-E2E-034-edit-division-no-op-auto-close-tanpa-log | FE+BE |
| TC-GS-DIV-101 | Edit hanya Division Name berhasil dan Code tidak berubah | P0 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-102 | Edit hanya Code berhasil dan Name tidak berubah | P1 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-103 | Edit Division Name dan Code sekaligus berhasil | P1 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-104 | Division Pre-setup dapat di-Edit seperti Division lain | P1 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-105 | Clear Field pada Edit mengosongkan field tanpa me-revert nilai tersimpan | P1 | E2E | TC-GS-DIV-E2E-033-edit-modal-clear-field-dan-unsaved-changes | FE+BE |
| TC-GS-DIV-106 | Menutup form Edit tanpa perubahan tidak memunculkan dialog Unsaved Changes | P1 | E2E | TC-GS-DIV-E2E-036-edit-division-resilience-server-failure-dan-double-submit | mock |
| TC-GS-DIV-107 | Close Edit saat dirty lalu Cancel mempertahankan form | P1 | E2E | TC-GS-DIV-E2E-033-edit-modal-clear-field-dan-unsaved-changes | FE+BE |
| TC-GS-DIV-108 | Close Edit saat dirty lalu Leave membuang perubahan | P1 | E2E | TC-GS-DIV-E2E-033-edit-modal-clear-field-dan-unsaved-changes | FE+BE |
| TC-GS-DIV-109 | Rename Division tercermin di Division Name pada tabel setelah Save | P1 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-110 | Edit gagal 5xx mempertahankan form dan input | P1 | E2E | TC-GS-DIV-E2E-036-edit-division-resilience-server-failure-dan-double-submit | mock |
| TC-GS-DIV-111 | Edit timeout mempertahankan form dan input | P2 | E2E | TC-GS-DIV-E2E-036-edit-division-resilience-server-failure-dan-double-submit | mock |
| TC-GS-DIV-112 | Klik ganda Save hanya menyimpan satu kali | P1 | E2E | TC-GS-DIV-E2E-035-edit-division-happy-path-mutasi-name-code-dan-seed-record | FE+BE |
| TC-GS-DIV-113 | Edit Division yang sudah dihapus pihak lain menampilkan toast tidak tersedia | P1 | E2E | TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-114 | Screening Dialog Konfirmasi Delete single | P0 | E2E | TC-GS-DIV-E2E-037-delete-single-screening-dialog-konfirmasi-dan-batal | FE+BE |
| TC-GS-DIV-115 | Cancel pada dialog Delete tidak menghapus Division | P1 | E2E | TC-GS-DIV-E2E-037-delete-single-screening-dialog-konfirmasi-dan-batal | FE+BE |
| TC-GS-DIV-116 | Delete Division bebas relasi berhasil | P0 | E2E | TC-GS-DIV-E2E-040-delete-single-happy-path-record-bebas-relasi-dan-seed | FE+BE |
| TC-GS-DIV-117 | Delete Division yang dipakai Login User aktif diblokir | P0 | E2E | TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user | FE+BE |
| TC-GS-DIV-118 | Delete Division yang dipakai Login User non-aktif diblokir | P0 | E2E | TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user | FE+BE |
| TC-GS-DIV-119 | Delete Division yang dipakai Non-Login User diblokir | P0 | E2E | TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user | FE+BE |
| TC-GS-DIV-120 | OK pada dialog blokir menutup dialog tanpa menghapus | P2 | E2E | TC-GS-DIV-E2E-038-delete-single-guard-blokir-in-use-user | FE+BE |
| TC-GS-DIV-121 | Division berubah in-use di antara cek awal dan Confirm diblokir | P1 | E2E | TC-GS-DIV-E2E-039-delete-single-recheck-atomik-in-use-saat-confirm | FE+BE |
| TC-GS-DIV-122 | Delete Division yang sudah dihapus pihak lain berhasil tanpa error | P1 | E2E | TC-GS-DIV-E2E-041-delete-single-resilience-double-submit-dan-server-error | mock |
| TC-GS-DIV-123 | Delete gagal 5xx tidak menghapus Division dan dialog tetap terbuka | P1 | E2E | TC-GS-DIV-E2E-041-delete-single-resilience-double-submit-dan-server-error | mock |
| TC-GS-DIV-124 | Klik ganda Delete hanya memproses satu penghapusan | P2 | E2E | TC-GS-DIV-E2E-040-delete-single-happy-path-record-bebas-relasi-dan-seed | FE+BE |
| TC-GS-DIV-125 | Screening Bulk Action Bar saat satu baris dicentang | P1 | E2E | TC-GS-DIV-E2E-042-bulk-action-bar-screening-dan-counter-lifecycle | FE+BE |
| TC-GS-DIV-126 | Counter Bulk Action Bar bertambah dan berkurang realtime serta clear lewat X | P2 | E2E | TC-GS-DIV-E2E-042-bulk-action-bar-screening-dan-counter-lifecycle | FE+BE |
| TC-GS-DIV-127 | Checkbox header memilih seluruh baris halaman dan status indeterminate | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-header-checkbox-dan-seleksi-lintas-halaman | FE+BE |
| TC-GS-DIV-128 | Select All lintas halaman memilih seluruh baris dan toggle menjadi Unselect All | P1 | E2E | TC-GS-DIV-E2E-043-tabel-utama-header-checkbox-dan-seleksi-lintas-halaman | FE+BE |
| TC-GS-DIV-129 | Selection Limit: checkbox melewati batas disabled saat dicentang satu per satu | P1 | E2E | TC-GS-DIV-E2E-044-selection-limit-enforcement-dan-select-all-capping | FE+BE |
| TC-GS-DIV-130 | Selection Limit: Select All di-cap ke batas dengan toast error persist | P1 | E2E | TC-GS-DIV-E2E-044-selection-limit-enforcement-dan-select-all-capping | FE+BE |
| TC-GS-DIV-131 | Bulk Delete seluruhnya bebas relasi memakai dialog homogen | P0 | E2E | TC-GS-DIV-E2E-045-bulk-delete-collapse-dialog-single-n-sama-dengan-1 | FE+BE |
| TC-GS-DIV-132 | Konfirmasi Bulk Delete homogen menghapus seluruh Division terpilih | P0 | E2E | TC-GS-DIV-E2E-046-bulk-delete-homogen-seluruh-item-bebas-relasi | FE+BE |
| TC-GS-DIV-133 | Cancel pada dialog Bulk Delete homogen tidak menghapus apa pun | P2 | E2E | TC-GS-DIV-E2E-046-bulk-delete-homogen-seluruh-item-bebas-relasi | FE+BE |
| TC-GS-DIV-134 | Bulk Delete campuran menampilkan Dialog campuran dengan dua kelompok | P0 | E2E | TC-GS-DIV-E2E-047-bulk-delete-campuran-sebagian-in-use-dan-batal | FE+BE |
| TC-GS-DIV-135 | Continue pada Bulk Delete campuran menghapus yang aman dan melewati yang in-use | P0 | E2E | TC-GS-DIV-E2E-047-bulk-delete-campuran-sebagian-in-use-dan-batal | FE+BE |
| TC-GS-DIV-136 | Bulk Delete seluruhnya in-use menampilkan Dialog blokir dengan bullet diperluas | P0 | E2E | TC-GS-DIV-E2E-048-bulk-delete-total-terblokir-seluruh-item-in-use | FE+BE |
| TC-GS-DIV-137 | Bulk Delete dengan satu baris bebas relasi memakai dialog single | P2 | E2E | TC-GS-DIV-E2E-046-bulk-delete-homogen-seluruh-item-bebas-relasi | FE+BE |
| TC-GS-DIV-138 | Bulk Delete dengan satu baris in-use memakai dialog blokir single | P2 | E2E | TC-GS-DIV-E2E-048-bulk-delete-total-terblokir-seluruh-item-in-use | FE+BE |
| TC-GS-DIV-139 | Item berubah in-use setelah pre-check di-skip diam-diam ke ringkasan | P1 | E2E | TC-GS-DIV-E2E-050-bulk-delete-resilience-double-submit-dan-server-500 | mock |
| TC-GS-DIV-140 | Bulk Delete gagal 5xx tidak menghapus satu pun Division | P1 | E2E | TC-GS-DIV-E2E-050-bulk-delete-resilience-double-submit-dan-server-500 | mock |
| TC-GS-DIV-141 | Search Toolbar: reveal, auto-focus, tooltip, icon clear, dan submit lewat Enter | P1 | E2E | TC-GS-DIV-E2E-051-tabel-utama-search-toolbar-mekanisme-dan-enter | FE+BE |
| TC-GS-DIV-142 | Search Toolbar: icon clear mengosongkan input tanpa mereset tabel hingga Enter | P1 | E2E | TC-GS-DIV-E2E-051-tabel-utama-search-toolbar-mekanisme-dan-enter | FE+BE |
| TC-GS-DIV-143 | Search Toolbar: icon panah kembali menutup search dan mereset tabel langsung | P2 | E2E | TC-GS-DIV-E2E-051-tabel-utama-search-toolbar-mekanisme-dan-enter | FE+BE |
| TC-GS-DIV-144 | Search per kolom searchable: Name dan Code (substring dan tanpa membedakan huruf besar kecil) | P0 | E2E | TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | FE+BE |
| TC-GS-DIV-145 | Last Updated tidak dapat dicari lewat Search toolbar | P2 | E2E | TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | FE+BE |
| TC-GS-DIV-146 | Search tidak mencari kolom yang di-hide | P1 | E2E | TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | FE+BE |
| TC-GS-DIV-147 | Search kembali mencari kolom setelah di-unhide | P2 | E2E | TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | FE+BE |
| TC-GS-DIV-148 | Search dari halaman lebih dari 1 mereset ke halaman 1 | P2 | E2E | TC-GS-DIV-E2E-052-tabel-utama-search-matching-logic-dan-column-scope | FE+BE |
| TC-GS-DIV-149 | Screening Filter Panel Tabel Division | P1 | E2E | TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format | FE+BE |
| TC-GS-DIV-150 | Filter Last Updated menyaring baris dalam rentang tanggal | P0 | E2E | TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format | FE+BE |
| TC-GS-DIV-151 | Teks tanggal pada input Date filter mengikuti format General Settings | P2 | E2E | TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format | FE+BE |
| TC-GS-DIV-152 | Clear Field pada Filter Panel dan Apply mengembalikan seluruh data | P1 | E2E | TC-GS-DIV-E2E-053-tabel-utama-filter-panel-screening-date-range-dan-format | FE+BE |
| TC-GS-DIV-153 | Search lalu Filter menghasilkan irisan keduanya | P1 | E2E | TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | FE+BE |
| TC-GS-DIV-154 | Filter lalu Search menghasilkan irisan keduanya | P1 | E2E | TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | FE+BE |
| TC-GS-DIV-155 | Kombinasi Search, Filter, Sort, dan Pagination bersamaan | P1 | E2E | TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | FE+BE |
| TC-GS-DIV-156 | Clear Filter saat Search dan Sort aktif mempertahankan Search dan Sort | P2 | E2E | TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | FE+BE |
| TC-GS-DIV-157 | Clear Search saat Filter dan Sort aktif mempertahankan Filter dan Sort | P2 | E2E | TC-GS-DIV-E2E-054-tabel-utama-filter-chips-badge-counter-dan-search-coexistence | FE+BE |
| TC-GS-DIV-158 | Ganti kolom sort saat Search dan Filter aktif tidak mereset saringan | P2 | E2E | TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE |
| TC-GS-DIV-159 | Empty state hasil kombinasi pulih saat salah satu saringan dilepas | P2 | E2E | TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE |
| TC-GS-DIV-160 | Seleksi checkbox bertahan saat Search dikosongkan | P3 | E2E | TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE |
| TC-GS-DIV-161 | Division baru yang tidak cocok dengan Search aktif tidak muncul | P3 | E2E | TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE |
| TC-GS-DIV-162 | Edit Name yang membuat Division tidak lagi cocok dengan Search aktif menghilangkannya dari tabel | P3 | E2E | TC-GS-DIV-E2E-055-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE |
| TC-GS-DIV-163 | Sort 3-state kolom teks Name dan Code | P1 | E2E | TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation | FE+BE |
| TC-GS-DIV-164 | Sort 3-state kolom Last Updated | P1 | E2E | TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation | FE+BE |
| TC-GS-DIV-165 | Kolom checkbox dan Column Visibility tidak memiliki ikon sort | P3 | E2E | TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation | FE+BE |
| TC-GS-DIV-166 | Pagination default 10 data per halaman dengan 4 halaman untuk 32 baris | P1 | E2E | TC-GS-DIV-E2E-056-tabel-utama-pagination-dan-state-preservation | FE+BE |
| TC-GS-DIV-167 | Ubah page size ke 25, 50, dan 100 | P1 | E2E | TC-GS-DIV-E2E-057-tabel-utama-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-168 | Navigasi Next, Previous, dan input nomor halaman lewat Enter | P2 | E2E | TC-GS-DIV-E2E-057-tabel-utama-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-169 | Apply Filter dari halaman lebih dari 1 mereset ke halaman 1 | P2 | E2E | TC-GS-DIV-E2E-057-tabel-utama-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-170 | Muat ulang halaman (F5) mempertahankan Search, Sort, Filter, dan halaman | P2 | E2E | TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-171 | Screening Overlay Column Visibility tabel Division | P1 | E2E | TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-172 | Screening Popup Setup Column tabel Division | P1 | E2E | TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-173 | Setup Column: hide dan unhide tiap kolom lewat popup lalu Save | P1 | E2E | TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-174 | Setup Column: reorder tiap kolom lewat drag lalu Save | P1 | E2E | TC-GS-DIV-E2E-058-tabel-utama-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-175 | Setup Column: pin dan unpin tiap kolom lalu Save | P2 | E2E | TC-GS-DIV-E2E-059-tabel-utama-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-176 | Setup Column: Reset to Default mengembalikan susunan default | P2 | E2E | TC-GS-DIV-E2E-059-tabel-utama-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-177 | Setup Column: Cancel dan X membuang perubahan preview | P2 | E2E | TC-GS-DIV-E2E-059-tabel-utama-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-178 | Setup Column: kolom visible terakhir tidak dapat di-uncheck | P1 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-179 | Konfigurasi kolom tabel Division tidak memengaruhi tabel Changelog | P2 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-180 | Screening menu Download tabel Division | P2 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-181 | Download tanpa Search dan Filter mengekspor seluruh baris | P1 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-182 | Download dengan Search dan Filter aktif hanya mengekspor baris yang cocok | P1 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-183 | Download hanya mengekspor kolom yang visible | P1 | E2E | TC-GS-DIV-E2E-061-tabel-utama-download-sync-kolom-dan-fault-injection | mock |
| TC-GS-DIV-184 | Kolom yang di-unhide kembali ikut diekspor | P2 | E2E | TC-GS-DIV-E2E-061-tabel-utama-download-sync-kolom-dan-fault-injection | mock |
| TC-GS-DIV-185 | Download berhasil tidak menampilkan toast sukses | P2 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-186 | Download gagal menampilkan toast error | P1 | E2E | TC-GS-DIV-E2E-061-tabel-utama-download-sync-kolom-dan-fault-injection | mock |
| TC-GS-DIV-187 | Isi file ekspor memakai format tanggal General Settings dan nilai kosong tidak ada | P3 | E2E | TC-GS-DIV-E2E-060-tabel-utama-download-format-csv-xlsx-dan-scoping | FE+BE |
| TC-GS-DIV-188 | Screening Modal Changelog: Division | P0 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-189 | Format isi sel Modal Changelog: strip, nama singkat, dan hover Modified By | P1 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-190 | Urutan default Modal Changelog adalah tanggal terbaru di atas | P1 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-191 | Empty state Modal Changelog saat belum ada riwayat | P1 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-192 | Empty state Modal Changelog saat Search tidak menemukan hasil | P1 | E2E | TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | FE+BE |
| TC-GS-DIV-193 | Search Modal Changelog per kolom searchable (substring dan tanpa membedakan huruf besar kecil) | P1 | E2E | TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | FE+BE |
| TC-GS-DIV-194 | Kolom Date tidak dapat dicari lewat Search Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | FE+BE |
| TC-GS-DIV-195 | Screening Filter Panel Modal Changelog | P1 | E2E | TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | FE+BE |
| TC-GS-DIV-196 | Opsi dropdown filter Changelog bersumber dari isi tabel Changelog | P1 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-197 | Opsi filter bertambah saat entri Changelog baru tercatat | P3 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-198 | Filter Date Modal Changelog menyaring berdasarkan rentang tanggal | P1 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-199 | Filter multi-select Modal Changelog: Action, Division Name, Field, dan Modified By | P1 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-200 | Dua opsi pada satu field filter digabung OR | P1 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-201 | Dua field filter berbeda digabung AND | P1 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-202 | Hapus chip filter lewat X menghapus centang opsi | P2 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-203 | Uncheck opsi di dalam dropdown menghapus chip | P2 | E2E | TC-GS-DIV-E2E-064-changelog-filter-panel-screening-date-dan-populated-dropdown | FE+BE |
| TC-GS-DIV-204 | Search di dalam dropdown filter mempersempit opsi | P3 | E2E | TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect | FE+BE |
| TC-GS-DIV-205 | Search dan Filter Modal Changelog dikombinasikan lalu dipulihkan | P2 | E2E | TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect | FE+BE |
| TC-GS-DIV-206 | Sort 3-state kolom teks Action, Division Name, Field, dan Modified By | P1 | E2E | TC-GS-DIV-E2E-068-changelog-sorting-3-state-dan-null-placement | FE+BE |
| TC-GS-DIV-207 | Sort 3-state kolom Date Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-068-changelog-sorting-3-state-dan-null-placement | FE+BE |
| TC-GS-DIV-208 | Sort kolom Old Value dan New Value menempatkan nilai kosong di akhir saat ascending | P2 | E2E | TC-GS-DIV-E2E-068-changelog-sorting-3-state-dan-null-placement | FE+BE |
| TC-GS-DIV-209 | Kolom Column Visibility Modal Changelog tidak memiliki ikon sort | P3 | E2E | TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format | mock |
| TC-GS-DIV-210 | Pagination Modal Changelog: default 10 dan pilihan 10, 25, 50, 100 | P2 | E2E | TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format | mock |
| TC-GS-DIV-211 | Modal Changelog ditutup lewat icon close dan klik di luar modal | P3 | E2E | TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format | mock |
| TC-GS-DIV-212 | Format tanggal Modal Changelog dan input Date filter mengikuti General Settings | P2 | E2E | TC-GS-DIV-E2E-069-changelog-modal-ui-behavior-pagination-dan-date-format | mock |
| TC-GS-DIV-213 | Screening Overlay Column Visibility Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-070-changelog-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-214 | Screening Popup Setup Column Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-071-changelog-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-215 | Setup Column Modal Changelog: hide dan unhide tiap kolom lalu Save | P2 | E2E | TC-GS-DIV-E2E-070-changelog-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-216 | Setup Column Modal Changelog: reorder tiap kolom lewat drag lalu Save | P2 | E2E | TC-GS-DIV-E2E-071-changelog-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-217 | Setup Column Modal Changelog: pin dan unpin tiap kolom lalu Save | P3 | E2E | TC-GS-DIV-E2E-071-changelog-setup-column-modal-fase-2 | mock |
| TC-GS-DIV-218 | Setup Column Modal Changelog: Reset to Default | P3 | E2E | TC-GS-DIV-E2E-072-changelog-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-219 | Setup Column Modal Changelog: Cancel dan X membuang perubahan | P3 | E2E | TC-GS-DIV-E2E-072-changelog-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-220 | Setup Column Modal Changelog: kolom visible terakhir tidak dapat di-uncheck | P2 | E2E | TC-GS-DIV-E2E-070-changelog-setup-column-overlay-fase-1 | mock |
| TC-GS-DIV-221 | Download Changelog tanpa Search dan Filter mengekspor seluruh riwayat | P1 | E2E | TC-GS-DIV-E2E-073-changelog-download-csv-xlsx-dan-fault-injection | FE+BE |
| TC-GS-DIV-222 | Download Changelog dengan Filter aktif hanya mengekspor baris yang cocok | P2 | E2E | TC-GS-DIV-E2E-073-changelog-download-csv-xlsx-dan-fault-injection | FE+BE |
| TC-GS-DIV-223 | Download Changelog gagal menampilkan toast error | P2 | E2E | TC-GS-DIV-E2E-073-changelog-download-csv-xlsx-dan-fault-injection | FE+BE |
| TC-GS-DIV-224 | Hover icon toolbar Modal Changelog menampilkan tooltip | P3 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-225 | Search Modal Changelog: reveal, auto-focus, submit lewat Enter, clear, dan collapse | P2 | E2E | TC-GS-DIV-E2E-063-changelog-search-per-kolom-dan-guard-date | FE+BE |
| TC-GS-DIV-226 | Kombinasi Search, Filter, Sort, dan Pagination pada Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery | FE+BE |
| TC-GS-DIV-227 | Clear Filter Modal Changelog saat Search dan Sort aktif mempertahankan keduanya | P3 | E2E | TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery | FE+BE |
| TC-GS-DIV-228 | Clear Search Modal Changelog saat Filter dan Sort aktif mempertahankan keduanya | P3 | E2E | TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery | FE+BE |
| TC-GS-DIV-229 | Ganti kolom sort Modal Changelog saat Search dan Filter aktif tidak mereset saringan | P3 | E2E | TC-GS-DIV-E2E-067-changelog-kombinasi-4-kontrol-dan-recovery | FE+BE |
| TC-GS-DIV-230 | Nilai panjang pada kolom Old Value dan New Value tampil penuh | P3 | E2E | TC-GS-DIV-E2E-062-changelog-screening-empty-state-dan-hover | FE+BE |
| TC-GS-DIV-231 | Dropdown filter Changelog menampilkan loading saat opsi masih diambil | P3 | E2E | TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | FE+BE |
| TC-GS-DIV-232 | Filter Division Name tetap berlaku pada snapshot setelah Division dihapus pihak lain | P2 | E2E | TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | FE+BE |
| TC-GS-DIV-233 | Banyak opsi terpilih pada field filter Changelog menampilkan overflow chip | P3 | E2E | TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | FE+BE |
| TC-GS-DIV-234 | Konfigurasi kolom Modal Changelog tidak memengaruhi tabel Division | P3 | E2E | TC-GS-DIV-E2E-072-changelog-setup-column-reset-cancel-save-fase-3 | mock |
| TC-GS-DIV-235 | Create dengan Code manual mencatat satu entri Division Name saja | P0 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-236 | Create dengan Code di-generate mencatat satu entri Division Name saja | P1 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-237 | Edit hanya Name mencatat satu entri Field Division Name | P0 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-238 | Edit hanya Code mencatat satu entri Field Code | P0 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-239 | Edit Name dan Code sekaligus mencatat dua entri terpisah | P0 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-240 | Edit tanpa perubahan tidak mencatat entri apa pun | P1 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-241 | Edit dengan Code dikosongkan mencatat entri Code bila berbeda | P2 | E2E | TC-GS-DIV-E2E-074-pencatatan-audit-log-mutasi-katalog-dan-aturan-kolom | FE+BE |
| TC-GS-DIV-242 | Delete mencatat satu entri Division Name dengan New Value strip | P0 | E2E | TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing | FE+BE |
| TC-GS-DIV-243 | Bulk Delete mencatat satu entri per Division yang berhasil dihapus | P0 | E2E | TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing | FE+BE |
| TC-GS-DIV-244 | Division yang di-skip karena in-use tidak menghasilkan entri log | P1 | E2E | TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing | FE+BE |
| TC-GS-DIV-245 | Entri Changelog lama tidak berubah setelah rename berikutnya | P0 | E2E | TC-GS-DIV-E2E-075-format-modified-by-snapshot-immutability-dan-multi-surface-routing | FE+BE |
| TC-GS-DIV-246 | Modified By mencatat aktor pelaksana tiap aksi | P2 | E2E | TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik | FE+BE |
| TC-GS-DIV-247 | Division tidak menulis System Log di Detail User | P3 | E2E | TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik | FE+BE |
| TC-GS-DIV-248 | Edit tercatat juga di Activity Log Global Settings | P2 | E2E | TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik | FE+BE |
| TC-GS-DIV-249 | Old Value dan New Value tidak pernah keduanya strip pada satu entri | P2 | E2E | TC-GS-DIV-E2E-076-integritas-log-format-tanggal-dan-transaksi-db-atomik | FE+BE |
| TC-GS-DIV-250 | Division baru muncul pada dropdown Division form Create User | P1 | E2E | TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-251 | Division baru muncul pada dropdown Division form Create Non-Login User | P1 | E2E | TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-252 | Rename Division tercermin pada dropdown Division form User | P1 | E2E | TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-253 | Division yang dihapus hilang dari dropdown Division form User | P1 | E2E | TC-GS-DIV-E2E-078-penolakan-submit-user-pada-divisi-yang-baru-dihapus-auto-clear | FE+BE |
| TC-GS-DIV-254 | Form User dengan Division terpilih yang dihapus pihak lain menampilkan error field dan auto-clear | P1 | E2E | TC-GS-DIV-E2E-079-user-form-stale-division-deletion-auto-clear | FE+BE |
| TC-GS-DIV-255 | Form Non-Login User dengan Division terpilih yang dihapus pihak lain menampilkan error field dan auto-clear | P1 | E2E | TC-GS-DIV-E2E-079-user-form-stale-division-deletion-auto-clear | FE+BE |
| TC-GS-DIV-256 | Division hasil Create Missing Divisions dari Import dapat di-Edit identik dengan Create manual | P2 | E2E | TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions | FE+BE |
| TC-GS-DIV-257 | Division hasil Create Missing Divisions mengikuti guard in-use dan Delete yang sama | P2 | E2E | TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions | FE+BE |
| TC-GS-DIV-258 | Division hasil Create Missing Divisions tercatat sebagai Create biasa | P2 | E2E | TC-GS-DIV-E2E-077-sinkronisasi-dua-arah-dropdown-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-259 | Request Create langsung tanpa capability Create ditolak server | P0 | E2E | TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api | FE+BE |
| TC-GS-DIV-260 | Request Edit langsung tanpa capability Update ditolak server | P0 | E2E | TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api | FE+BE |
| TC-GS-DIV-261 | Request Delete langsung tanpa capability Delete ditolak server | P0 | E2E | TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api | FE+BE |
| TC-GS-DIV-262 | Request Delete Division in-use langsung ke server tetap ditolak guard | P0 | E2E | TC-GS-DIV-E2E-081-security-penegakan-izin-server-side-dan-guard-in-use-api | FE+BE |
| TC-GS-DIV-263 | Create saat entitas Suspended ditolak server | P0 | E2E | TC-GS-DIV-E2E-082-security-entitas-suspended-expired-blokir-aksi-tulis | FE+BE |
| TC-GS-DIV-264 | Edit saat entitas Expired ditolak server | P0 | E2E | TC-GS-DIV-E2E-082-security-entitas-suspended-expired-blokir-aksi-tulis | FE+BE |
| TC-GS-DIV-265 | Delete saat entitas Suspended ditolak server | P0 | E2E | TC-GS-DIV-E2E-082-security-entitas-suspended-expired-blokir-aksi-tulis | FE+BE |
| TC-GS-DIV-266 | Data Division entitas lain tidak terlihat | P0 | E2E | TC-GS-DIV-E2E-083-security-isolasi-multi-tenant-dan-pencegahan-kebocoran-data | FE+BE |
| TC-GS-DIV-267 | Name berisi emoji yang lolos validasi klien tetap ditolak server | P2 | E2E | TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection | mock |
| TC-GS-DIV-268 | Division Name berisi markup HTML ditampilkan sebagai teks biasa | P1 | E2E | TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection | mock |
| TC-GS-DIV-269 | Search berisi payload SQL tidak memengaruhi hasil | P2 | E2E | TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection | mock |
| TC-GS-DIV-270 | Edit Name berisi emoji yang lolos validasi klien tetap ditolak server | P2 | E2E | TC-GS-DIV-E2E-084-security-sanitasi-input-dom-emoji-bypass-xss-dan-sql-injection | mock |
| TC-GS-DIV-271 | Dua admin mengedit Name Division yang sama: Save terakhir menimpa tanpa dialog konflik | P0 | E2E | TC-GS-DIV-E2E-085-concurrency-edit-last-write-wins-dan-race-create-duplicate | FE+BE |
| TC-GS-DIV-272 | Dua admin membuat Division dengan Name sama bersamaan: yang kedua ditolak duplicate | P0 | E2E | TC-GS-DIV-E2E-085-concurrency-edit-last-write-wins-dan-race-create-duplicate | FE+BE |
| TC-GS-DIV-273 | Dua admin membuat Division dengan Code manual sama bersamaan: yang kedua ditolak duplicate | P1 | E2E | TC-GS-DIV-E2E-085-concurrency-edit-last-write-wins-dan-race-create-duplicate | FE+BE |
| TC-GS-DIV-274 | Dua admin membuat Division pada slot terakhir: hanya satu yang berhasil | P1 | E2E | TC-GS-DIV-E2E-086-concurrency-race-slot-limit-edit-vs-delete-dan-idempotent-delete | FE+BE |
| TC-GS-DIV-275 | Edit-vs-Delete: Admin A menyimpan Edit pada Division yang baru dihapus Admin B | P2 | E2E | TC-GS-DIV-E2E-086-concurrency-race-slot-limit-edit-vs-delete-dan-idempotent-delete | FE+BE |
| TC-GS-DIV-276 | Edit-vs-Bulk Delete: Admin A menyimpan Edit pada Division yang baru dihapus lewat Bulk Delete Admin B | P2 | E2E | TC-GS-DIV-E2E-086-concurrency-race-slot-limit-edit-vs-delete-dan-idempotent-delete | FE+BE |
| TC-GS-DIV-277 | Division baru dari admin lain muncul otomatis di tabel yang sedang dibuka | P2 | E2E | TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating | FE+BE |
| TC-GS-DIV-278 | Rename Division dari admin lain tampil otomatis di tabel yang sedang dibuka | P2 | E2E | TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating | FE+BE |
| TC-GS-DIV-279 | Katalog tidak pernah turun ke nol: Division terakhir otomatis in-use | P1 | E2E | TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating | FE+BE |
| TC-GS-DIV-280 | Create, Edit, dan Delete identik di semua tier plan tanpa gating | P2 | E2E | TC-GS-DIV-E2E-087-realtime-update-katalog-minimum-dan-absennya-plan-gating | FE+BE |
| TC-GS-DIV-281 | Screening halaman Division pada aplikasi mobile | P1 | E2E | TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating | mock |
| TC-GS-DIV-282 | Card list mobile tanpa checkbox dan tanpa bulk action | P2 | E2E | TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating | mock |
| TC-GS-DIV-283 | Row action card mobile mengikuti gating capability, [⋯] tidak tampil bila semua Hidden | P1 | E2E | TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating | mock |
| TC-GS-DIV-284 | Toolbar, Filter, dan dialog mobile tampil sebagai bottom sheet | P2 | E2E | TC-GS-DIV-E2E-088-mobile-layout-android-card-list-bottom-sheet-dan-gating | mock |
| TC-GS-DIV-285 | Create Division dari mobile berhasil | P2 | E2E | TC-GS-DIV-E2E-089-mobile-crud-create-dan-edit-via-bottom-sheet | mock |
| TC-GS-DIV-286 | Edit Division dari mobile tampil sebagai bottom sheet dan berhasil disimpan | P2 | E2E | TC-GS-DIV-E2E-089-mobile-crud-create-dan-edit-via-bottom-sheet | mock |
| TC-GS-DIV-287 | Cancel pada dialog Bulk Delete campuran tidak menghapus apa pun | P2 | E2E | TC-GS-DIV-E2E-047-bulk-delete-campuran-sebagian-in-use-dan-batal | FE+BE |
| TC-GS-DIV-288 | Edit dengan Code berisi spasi saja dianggap kosong dan di-generate otomatis | P2 | E2E | TC-GS-DIV-E2E-032-edit-modal-auto-generate-code-saat-kosong | FE+BE |
| TC-GS-DIV-289 | Create Missing Divisions saat Master Data Count Limit tercapai ditolak | P1 | E2E | TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions | FE+BE |
| TC-GS-DIV-290 | Create Missing Divisions untuk nama yang sudah dibuat pihak lain ditolak sebagai duplicate | P2 | E2E | TC-GS-DIV-E2E-080-import-parity-operasional-dan-create-missing-divisions | FE+BE |
| TC-GS-DIV-291 | Accessibility Popup Edit Division: fokus awal, aria, focus trap, Esc | P2 | E2E | TC-GS-DIV-E2E-028-edit-modal-screening-prefill-dan-aksesibilitas | FE+BE |
| TC-GS-DIV-292 | Search di dalam dropdown filter Changelog: Action, Field, dan Modified By | P2 | E2E | TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect | FE+BE |
| TC-GS-DIV-293 | Dua opsi pada satu field filter digabung OR: Division Name, Field, dan Modified By | P2 | E2E | TC-GS-DIV-E2E-065-changelog-filter-dropdown-search-dan-or-multiselect | FE+BE |
| TC-GS-DIV-294 | Hapus chip lewat X pada field filter Division Name, Field, dan Modified By | P3 | E2E | TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | FE+BE |
| TC-GS-DIV-295 | Uncheck opsi di dalam dropdown menghapus chip pada Division Name, Field, dan Modified By | P3 | E2E | TC-GS-DIV-E2E-066-changelog-filter-chip-lifecycle-stale-snapshot-dan-resilience | FE+BE |
| TC-GS-DIV-296 | Bulk Delete — seluruh item menjadi in-use di antara buka dialog dan Confirm | P1 | E2E | TC-GS-DIV-E2E-049-bulk-delete-recheck-atomik-confirm-semua-item-menjadi-in-use | FE+BE |
