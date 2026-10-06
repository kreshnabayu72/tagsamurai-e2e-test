# Coverage E2E — Global Settings > Division

Sumber: `global-settings/division/TestCases/tc-division.md` (231 TC aktif pasca pencabutan 5 TC mobile web-only) dan `global-settings/division/TestCases/tc-division-backend.md` (83 TC backend).
Referensi: `global-settings/division/PRD/division.md`.
Suite: `specs/GlobalSettings/Division/`.
Prefix Modul: `GS` + `DIV` (`TC-GS-DIV-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (68 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-DIV-E2E-001-screening-tabel-utama-dan-struktur-halaman | Screening 3 Zona Tabel Division List dan Default Sort Name A-Z | FE+BE | TC-GS-DIV-01, TC-GS-DIV-02 |
| TC-GS-DIV-E2E-002-loading-skeleton-dan-read-failure-resilience | Loading State Skeleton dan Ketahanan Terhadap Gagal Fetch Data Awal | mock | TC-GS-DIV-03, TC-GS-DIV-05, TC-GS-DIV-06 |
| TC-GS-DIV-E2E-003-no-result-state-pencarian-tanpa-hasil | Tampilan No-Result State Saat Pencarian Tanpa Data Cocok | FE+BE | TC-GS-DIV-04 |
| TC-GS-DIV-E2E-004-hover-tooltip-toolbar-dan-teks-terpotong-tabel-utama | Hover Tooltip pada Table Tools dan Nama Divisi Panjang yang Terpotong | mock | TC-GS-DIV-200, TC-GS-DIV-201 |
| TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | Guided Tooltip 3-Step Walkthrough, Navigasi Tombol, Keyboard, dan Replay | mock | TC-GS-DIV-216, TC-GS-DIV-217, TC-GS-DIV-218, TC-GS-DIV-219, TC-GS-DIV-221 |
| TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | Role Matrix Positif: Total Control dan Pemegang Capability CRUD | FE+BE | TC-GS-DIV-07, TC-GS-DIV-09, TC-GS-DIV-10, TC-GS-DIV-11, TC-GS-DIV-12 |
| TC-GS-DIV-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | Role Matrix Negatif: Read Only, Pengguna Tanpa Akses, dan Direct URL 403 | FE+BE | TC-GS-DIV-08, TC-GS-DIV-13, TC-GS-DIV-14 |
| TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover | Screening Modal Create Division, Atribut Aksesibilitas, dan Feedback Tombol | mock | TC-GS-DIV-15, TC-GS-DIV-16, TC-GS-DIV-17, TC-GS-DIV-194 |
| TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | Validasi Field Name: Wajib Diisi, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Re-check Submit | FE+BE | TC-GS-DIV-19, TC-GS-DIV-20, TC-GS-DIV-22, TC-GS-DIV-23, TC-GS-DIV-192, TC-GS-DIV-276 |
| TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase | Validasi Field Code: Batas 15 Karakter, Whitelist Karakter, Duplikat Debounce, dan Auto-Uppercase | FE+BE | TC-GS-DIV-261, TC-GS-DIV-262, TC-GS-DIV-263, TC-GS-DIV-264 |
| TC-GS-DIV-E2E-011-create-modal-unsaved-changes-dialog-dan-clear-field | Pembersihan Form via `[Clear Field]` dan Dialog Konfirmasi Unsaved Changes | mock | TC-GS-DIV-27, TC-GS-DIV-190, TC-GS-DIV-191 |
| TC-GS-DIV-E2E-012-create-division-happy-path-stay-unchecked | Pembuatan Divisi Baru Sukses dengan Auto-Trim dan Stay Unchecked | FE+BE | TC-GS-DIV-21, TC-GS-DIV-24, TC-GS-DIV-193 |
| TC-GS-DIV-E2E-013-create-division-dengan-code-manual | Pembuatan Divisi Baru Sukses dengan Input Code Manual | FE+BE | TC-GS-DIV-259 |
| TC-GS-DIV-E2E-014-create-division-code-auto-generate-inisial | Pembuatan Divisi Baru dengan Code Dikosongkan Menghasilkan Auto-Generate Inisial | FE+BE | TC-GS-DIV-260 |
| TC-GS-DIV-E2E-015-create-division-batch-stay-checked-dan-preparasi-data | Pembuatan Batch Divisi Menggunakan Checkbox Stay on This Form | FE+BE | TC-GS-DIV-25, TC-GS-DIV-26 |
| TC-GS-DIV-E2E-016-create-division-oleh-actor-capability-create-only | Pembuatan Divisi Baru Sukses oleh Pengguna Ber-capability Create-Only | FE+BE | TC-GS-DIV-30 |
| TC-GS-DIV-E2E-017-create-division-limit-reached-dan-stay-checked-boundary | Pemblokiran Pembuatan Divisi Saat Master Data Count Limit Tercapai | FE+BE | TC-GS-DIV-28, TC-GS-DIV-223 |
| TC-GS-DIV-E2E-018-create-division-server-failure-resilience | Ketahanan Form Create Terhadap Kegagalan Server 5xx/Timeout | mock | TC-GS-DIV-29 |
| TC-GS-DIV-E2E-019-edit-modal-screening-prefilled-dan-hover | Screening Modal Edit Division, Nilai Terisi Awal, dan Feedback Tombol | mock | TC-GS-DIV-31, TC-GS-DIV-196 |
| TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | Validasi Field Name Edit: Required, Batas 120 Karakter, Duplikat Debounce, Keystroke Emoji, dan Submit | FE+BE | TC-GS-DIV-33, TC-GS-DIV-36, TC-GS-DIV-213, TC-GS-DIV-214, TC-GS-DIV-222, TC-GS-DIV-226 |
| TC-GS-DIV-E2E-021-edit-modal-validasi-field-code | Validasi Field Code Edit: Batas 15 Karakter, Whitelist Karakter, dan Duplikat Existing | FE+BE | TC-GS-DIV-266, TC-GS-DIV-267 |
| TC-GS-DIV-E2E-022-edit-modal-clear-field-dan-edit-no-op | Fungsi `[Clear Field]` Mengosongkan Input dan Submit Edit No-Op Tanpa Perubahan | FE+BE | TC-GS-DIV-34, TC-GS-DIV-197 |
| TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code | Penyuntingan Divisi Sukses: Perubahan Name Ter-trim dan Pembaruan Code | FE+BE | TC-GS-DIV-35, TC-GS-DIV-195, TC-GS-DIV-225, TC-GS-DIV-265 |
| TC-GS-DIV-E2E-024-edit-division-target-data-seed | Penyuntingan Divisi Seed Awal Diizinkan Mengubah Name dan Code | FE+BE | TC-GS-DIV-39 |
| TC-GS-DIV-E2E-025-edit-division-oleh-actor-capability-update-only | Penyuntingan Divisi Sukses oleh Pengguna Ber-capability Update-Only | FE+BE | TC-GS-DIV-40 |
| TC-GS-DIV-E2E-026-edit-division-server-failure-resilience | Ketahanan Form Edit Terhadap Kegagalan Server 5xx/Timeout | mock | TC-GS-DIV-37 |
| TC-GS-DIV-E2E-027-delete-single-screening-cancel-dan-double-submit | Screening Dialog Konfirmasi Delete Single, Pembatalan `[Cancel]`, dan Double-Submit | mock | TC-GS-DIV-41, TC-GS-DIV-44, TC-GS-DIV-45 |
| TC-GS-DIV-E2E-028-delete-single-guard-blocked-in-use | Pemblokiran Penghapusan Divisi yang Sedang Direferensikan Pengguna | FE+BE | TC-GS-DIV-43 |
| TC-GS-DIV-E2E-029-delete-single-happy-path-record-aman | Penghapusan Divisi Tunggal Bebas Relasi Berhasil | FE+BE | TC-GS-DIV-42 |
| TC-GS-DIV-E2E-030-delete-single-oleh-actor-capability-delete-only | Penghapusan Divisi Tunggal oleh Pengguna Ber-capability Delete-Only | FE+BE | TC-GS-DIV-46 |
| TC-GS-DIV-E2E-031-bulk-action-bar-screening-counter-dan-checkbox-header | Screening Bulk Action Bar, Counter Seleksi, dan Checkbox Header 3-State | mock | TC-GS-DIV-47, TC-GS-DIV-48, TC-GS-DIV-49 |
| TC-GS-DIV-E2E-032-bulk-selection-server-select-all-dan-selection-limit | Server Select All Lintas Halaman, Unselect All, dan Pembatasan Batas 1000 Baris | FE+BE | TC-GS-DIV-227, TC-GS-DIV-254, TC-GS-DIV-255 |
| TC-GS-DIV-E2E-033-bulk-delete-collapse-dialog-single-n-sama-dengan-1 | Penyederhanaan Dialog Bulk Delete Menjadi Dialog Single Saat N=1 (Aman vs In-Use) | FE+BE | TC-GS-DIV-257, TC-GS-DIV-258 |
| TC-GS-DIV-E2E-034-bulk-delete-blocked-total-seluruh-item-in-use | Pemblokiran Bulk Delete Total Saat Seluruh Divisi Terpilih Sedang In-Use | FE+BE | TC-GS-DIV-52 |
| TC-GS-DIV-E2E-035-bulk-delete-mixed-sebagian-aman-sebagian-in-use | Bulk Delete Campuran: Menghapus Divisi Aman dan Melewati Divisi In-Use | FE+BE | TC-GS-DIV-51 |
| TC-GS-DIV-E2E-036-bulk-delete-uniform-semua-item-aman | Bulk Delete Homogen: Menghapus Seluruh Divisi Terpilih yang Bebas Relasi | FE+BE | TC-GS-DIV-50 |
| TC-GS-DIV-E2E-037-bulk-delete-oleh-actor-capability-delete-only | Penghapusan Massal Divisi Berhasil oleh Aktor Ber-capability Delete-Only | FE+BE | TC-GS-DIV-215 |
| TC-GS-DIV-E2E-038-bulk-delete-server-failure-resilience | Ketahanan Eksekusi Bulk Delete Terhadap Kegagalan Server 5xx/Timeout | mock | TC-GS-DIV-53 |
| TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable | Pencarian Tabel Utama Berdasarkan Name dan Code serta Guard Kolom Tanggal | FE+BE | TC-GS-DIV-54, TC-GS-DIV-55, TC-GS-DIV-56, TC-GS-DIV-268 |
| TC-GS-DIV-E2E-040-tabel-utama-pola-interaksi-search-box-toolbar | Pola Interaksi Search Box Toolbar: Reveal, Auto-Focus, Enter, Clear, dan Collapse | mock | TC-GS-DIV-57 |
| TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search | Filter Panel Last Updated Tunggal dan Irisan Presisi dengan Search | FE+BE | TC-GS-DIV-58, TC-GS-DIV-59, TC-GS-DIV-60, TC-GS-DIV-61 |
| TC-GS-DIV-E2E-042-tabel-utama-sorting-3-state-name-code-dan-last-updated | Sorting 3-State (Ascending, Descending, Default) Kolom Name, Code, dan Last Updated | FE+BE | TC-GS-DIV-62, TC-GS-DIV-63, TC-GS-DIV-269 |
| TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | Kombinasi Penuh Search, Filter, Sort, Pagination, Independensi Clear, dan Pemulihan | FE+BE | TC-GS-DIV-64, TC-GS-DIV-65, TC-GS-DIV-66, TC-GS-DIV-67, TC-GS-DIV-68, TC-GS-DIV-69 |
| TC-GS-DIV-E2E-044-tabel-utama-mutasi-realtime-create-dan-edit | Refleksi Real-time Hasil Create dan Edit Terhadap Kriteria Search/Filter Aktif | FE+BE | TC-GS-DIV-70, TC-GS-DIV-71 |
| TC-GS-DIV-E2E-045-tabel-utama-setup-column-fase-1-overlay-quick-panel | Setup Column Fase 1: Screening Overlay, Toggle Kolom Hideable, dan Drag Reorder | mock | TC-GS-DIV-72, TC-GS-DIV-73, TC-GS-DIV-74 |
| TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | Setup Column Fase 2: Popup Modal, Live Preview, Toggle Ceklis, Geser, dan Pin Kolom | mock | TC-GS-DIV-75, TC-GS-DIV-76, TC-GS-DIV-77, TC-GS-DIV-228, TC-GS-DIV-229, TC-GS-DIV-230, TC-GS-DIV-231, TC-GS-DIV-270, TC-GS-DIV-271, TC-GS-DIV-272 |
| TC-GS-DIV-E2E-047-tabel-utama-setup-column-fase-3-reset-cancel-dan-cache-independen | Setup Column Fase 3: Reset to Default, Cancel Discard, dan Independensi Cache | mock | TC-GS-DIV-78, TC-GS-DIV-79, TC-GS-DIV-80 |
| TC-GS-DIV-E2E-048-tabel-utama-download-csv-xlsx-dan-penanganan-error | Ekspor Download CSV dan XLSX Mengikuti Filter Aktif Serta Penanganan Error | FE+BE | TC-GS-DIV-81, TC-GS-DIV-82, TC-GS-DIV-83 |
| TC-GS-DIV-E2E-049-tabel-utama-pagination-navigasi-dan-render-page-size | Pagination Navigasi Halaman dan Render Presisi Page Size 10/25/50/100 | FE+BE | TC-GS-DIV-84, TC-GS-DIV-85, TC-GS-DIV-274 |
| TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | Screening Modal Changelog Division, Tampilan Empty State, dan Hover Tooltip | FE+BE | TC-GS-DIV-86, TC-GS-DIV-87, TC-GS-DIV-88, TC-GS-DIV-118, TC-GS-DIV-119, TC-GS-DIV-202 |
| TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | Pencarian Modal Changelog pada 6 Kolom Teks dan Guard Kolom Date Non-Searchable | FE+BE | TC-GS-DIV-89, TC-GS-DIV-90, TC-GS-DIV-91, TC-GS-DIV-92, TC-GS-DIV-93, TC-GS-DIV-94, TC-GS-DIV-95, TC-GS-DIV-273 |
| TC-GS-DIV-E2E-052-changelog-pola-interaksi-search-box-toolbar | Pola Interaksi Search Box Toolbar Modal Changelog | mock | TC-GS-DIV-96 |
| TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | Screening Filter Panel Modal Changelog dan Penerapan Filter Individual | FE+BE | TC-GS-DIV-97, TC-GS-DIV-98, TC-GS-DIV-99, TC-GS-DIV-100, TC-GS-DIV-101 |
| TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | Sumber Opsi Dropdown Filter Changelog: Hardcode Action vs Populate Scoped dan Stale Reference | FE+BE | TC-GS-DIV-205, TC-GS-DIV-206, TC-GS-DIV-207, TC-GS-DIV-208, TC-GS-DIV-278 |
| TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | Pencarian Internal Dropdown Filter, Logika OR, Siklus Chip Removal, dan Overflow | FE+BE | TC-GS-DIV-209, TC-GS-DIV-210, TC-GS-DIV-211, TC-GS-DIV-212, TC-GS-DIV-224 |
| TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | Kombinasi Multi-Filter Changelog, Alur Search dan Filter, Serta Pemulihan Empty State | FE+BE | TC-GS-DIV-102, TC-GS-DIV-103, TC-GS-DIV-104, TC-GS-DIV-105, TC-GS-DIV-106, TC-GS-DIV-107, TC-GS-DIV-108, TC-GS-DIV-109, TC-GS-DIV-110, TC-GS-DIV-275 |
| TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | Sorting 3-State untuk 7 Kolom Modal Changelog (Date Default Newest First) | FE+BE | TC-GS-DIV-111, TC-GS-DIV-112, TC-GS-DIV-113, TC-GS-DIV-114, TC-GS-DIV-115, TC-GS-DIV-116, TC-GS-DIV-117 |
| TC-GS-DIV-E2E-058-changelog-setup-column-fase-1-overlay-quick-panel | Setup Column Modal Changelog Fase 1: Screening Overlay dan Drag Reorder | mock | TC-GS-DIV-120, TC-GS-DIV-121, TC-GS-DIV-122 |
| TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | Setup Column Modal Changelog Fase 2: Popup Modal Visibilitas, Urutan, dan Pin 7 Kolom | mock | TC-GS-DIV-123, TC-GS-DIV-124, TC-GS-DIV-125, TC-GS-DIV-232, TC-GS-DIV-233, TC-GS-DIV-234, TC-GS-DIV-235, TC-GS-DIV-236, TC-GS-DIV-237, TC-GS-DIV-238, TC-GS-DIV-239, TC-GS-DIV-240, TC-GS-DIV-241, TC-GS-DIV-242, TC-GS-DIV-243, TC-GS-DIV-244, TC-GS-DIV-245, TC-GS-DIV-246, TC-GS-DIV-247, TC-GS-DIV-248, TC-GS-DIV-249, TC-GS-DIV-250 |
| TC-GS-DIV-E2E-060-changelog-setup-column-fase-3-reset-cancel-dan-cache-independen | Setup Column Modal Changelog Fase 3: Reset Default, Cancel, dan Independensi Cache | mock | TC-GS-DIV-126, TC-GS-DIV-127, TC-GS-DIV-128 |
| TC-GS-DIV-E2E-061-changelog-download-csv-xlsx-dan-penanganan-error | Ekspor Download Changelog CSV/XLSX dan Penanganan Kegagalan Server | FE+BE | TC-GS-DIV-129, TC-GS-DIV-130 |
| TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | Sinkronisasi Pencatatan Mutasi 3 Surface (Changelog, System Log, Activity Log) dan Immutability Snapshot | FE+BE | TC-GS-DIV-131, TC-GS-DIV-132, TC-GS-DIV-133, TC-GS-DIV-134, TC-GS-DIV-135, TC-GS-DIV-204, TC-GS-DIV-277 |
| TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings | Konsistensi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings | FE+BE | TC-GS-DIV-174, TC-GS-DIV-175, TC-GS-DIV-176, TC-GS-DIV-177 |
| TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user | Sinkronisasi Dua Arah: Perubahan Katalog Division Terfleksi Instan pada Dropdown Form User | FE+BE | TC-GS-DIV-38, TC-GS-DIV-178, TC-GS-DIV-179, TC-GS-DIV-180 |
| TC-GS-DIV-E2E-065-entitas-suspended-expired-blokir-aksi-tulis | Blokir Aksi Tulis Katalog Division Saat Status Entitas Suspended atau Expired | FE+BE | TC-GS-DIV-185 |
| TC-GS-DIV-E2E-066-absennya-plan-gating-seluruh-tier-plan | Absennya Plan Gating: Seluruh Fitur Division Berlaku Identik di Semua Tier Lisensi | FE+BE | TC-GS-DIV-203 |
| TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | Penanganan Konflik Konkurensi Antar-Pengguna: Concurrent Edit, Delete, Duplicate, dan Limit | mock | TC-GS-DIV-186, TC-GS-DIV-187, TC-GS-DIV-188, TC-GS-DIV-251, TC-GS-DIV-252, TC-GS-DIV-253 |
| TC-GS-DIV-E2E-068-import-parity-operasional-edit-dan-refleksi-dropdown | Parity Operasional: Divisi Hasil Import Tampil Normal, Dapat Diedit, dan Terfleksi ke Dropdown User | FE+BE | TC-GS-DIV-189, TC-GS-DIV-256 |

---

## 2. Alasan TC Hanya-BE (Tidak Masuk Spec E2E)

Seluruh 37 TC murni API/backend pada modul Division telah dipisahkan ke `global-settings/division/TestCases/tc-division-backend.md` (`TC-GS-DIV-BE-001` s/d `083`, mencakup 7 endpoint lengkap). Oleh karena itu, seluruh **231 TC aktif** yang ada di dokumen `tc-division.md` memiliki cakupan antarmuka (`PIC FE: v`) dan dimasukkan 100% ke dalam kumpulan Spec E2E tanpa ada yang dilewati.

---

## 3. Lapisan per TC (Seluruh 231 TC Granular Aktif)

| TC ID | Skenario | Prioritas | Lapisan | Spec E2E | Mode | Catatan |
|---|---|:---:|:---:|---|:---:|---|
| TC-GS-DIV-01 | Screening — Tab Division List (Header, Body, Footer) | P0 | E2E | TC-GS-DIV-E2E-001-screening-tabel-utama-dan-struktur-halaman | FE+BE | |
| TC-GS-DIV-02 | Default sort tabel Division — Name Alphabetical A-Z | P1 | E2E | TC-GS-DIV-E2E-001-screening-tabel-utama-dan-struktur-halaman | FE+BE | |
| TC-GS-DIV-03 | Loading state — Loading component saat fetch data | P2 | E2E | TC-GS-DIV-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-DIV-04 | No-result state — Search tanpa hasil cocok (genuinely-empty tidak reachable, lihat Catatan) | P1 | E2E | TC-GS-DIV-E2E-003-no-result-state-pencarian-tanpa-hasil | FE+BE | |
| TC-GS-DIV-05 | Read-failure resilience — gagal fetch data awal | P1 | E2E | TC-GS-DIV-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-DIV-06 | Read-failure recovery — klik `[Try Again]` berhasil memuat data | P2 | E2E | TC-GS-DIV-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-DIV-216 | Guided Tooltip — Screening Konten 2 Step & Trigger Auto (First Visit) | P1 | E2E | TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock | |
| TC-GS-DIV-217 | Guided Tooltip — Kunjungan Kedua Tidak Auto-Muncul & Trigger Manual via `[?]` | P2 | E2E | TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock | |
| TC-GS-DIV-218 | Guided Tooltip — Siklus Navigasi Back/Next/Skip/Done | P2 | E2E | TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock | |
| TC-GS-DIV-219 | Guided Tooltip — Exit Tanpa Selesai (Resize/Navigasi Keluar) Tidak Set Flag | P2 | E2E | TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock | |
| TC-GS-DIV-221 | Guided Tooltip — Accessibility Keyboard Navigation | P3 | E2E | TC-GS-DIV-E2E-005-guided-tooltip-walkthrough-navigasi-dan-replay | mock | |
| TC-GS-DIV-07 | Matriks visibilitas — Total Control (semua kontrol aktif) | P0 | E2E | TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | FE+BE | |
| TC-GS-DIV-08 | Matriks visibilitas — Read Only (seluruh kontrol tulis tersembunyi) | P0 | E2E | TC-GS-DIV-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE | |
| TC-GS-DIV-09 | Matriks visibilitas — capability "Manage user and role" Full CRUD | P0 | E2E | TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | FE+BE | |
| TC-GS-DIV-10 | Matriks visibilitas — capability Create-Only (hanya opsi Create tampil) | P1 | E2E | TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | FE+BE | |
| TC-GS-DIV-11 | Matriks visibilitas — capability Update-Only (hanya opsi Edit tampil di row action) | P1 | E2E | TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | FE+BE | |
| TC-GS-DIV-12 | Matriks visibilitas — capability Delete-Only (hanya opsi Delete tampil, bulk aktif) | P1 | E2E | TC-GS-DIV-E2E-006-role-matrix-positif-visibilitas-kontrol-akses | FE+BE | |
| TC-GS-DIV-13 | Matriks visibilitas — No Capability (menu Division tersembunyi total) | P0 | E2E | TC-GS-DIV-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE | |
| TC-GS-DIV-14 | Direct URL Access — akses langsung tanpa capability | P0 | E2E | TC-GS-DIV-E2E-007-role-matrix-negatif-read-only-tanpa-akses-dan-direct-url | FE+BE | |
| TC-GS-DIV-15 | Screening — Popup Create Division | P0 | E2E | TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover | mock | |
| TC-GS-DIV-16 | Accessibility Popup Create Division — field Name punya `aria-required` & `aria-describedby` yang benar | P2 | E2E | TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover | mock | |
| TC-GS-DIV-17 | Accessibility Popup Create Division — focus trapped & Esc menutup popup | P2 | E2E | TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover | mock | |
| TC-GS-DIV-19 | Validasi Name — Required, kosong saat Submit | P0 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-20 | Validasi Name — Boundary max 120 karakter | P1 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-21 | Validasi Name — Auto-trim spasi awal/akhir saat submit | P1 | E2E | TC-GS-DIV-E2E-012-create-division-happy-path-stay-unchecked | FE+BE | |
| TC-GS-DIV-22 | Validasi Name — Debounce check keunikan (duplikat) | P0 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-276 | Validasi Name — Duplikat tetap diblokir saat `[Submit]` (re-check atomik server-side) | P0 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-23 | Validasi Name — Emoji diblok di level input (keystroke filter) | P2 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-24 | Submit Create Division — Happy Path, Stay unchecked | P0 | E2E | TC-GS-DIV-E2E-012-create-division-happy-path-stay-unchecked | FE+BE | |
| TC-GS-DIV-259 | Submit Create Division — Code diisi manual, happy path | P0 | E2E | TC-GS-DIV-E2E-013-create-division-dengan-code-manual | FE+BE | |
| TC-GS-DIV-260 | Submit Create Division — Code dikosongkan, auto-generate dari inisial Name | P1 | E2E | TC-GS-DIV-E2E-014-create-division-code-auto-generate-inisial | FE+BE | |
| TC-GS-DIV-261 | Validasi Code — Boundary max 15 karakter | P1 | E2E | TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase | FE+BE | |
| TC-GS-DIV-262 | Validasi Code — Karakter di luar whitelist ditolak | P1 | E2E | TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase | FE+BE | |
| TC-GS-DIV-263 | Validasi Code — Debounce check keunikan (duplikat, case-insensitive) | P1 | E2E | TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase | FE+BE | |
| TC-GS-DIV-264 | Validasi Code — Auto-uppercase saat mengetik | P2 | E2E | TC-GS-DIV-E2E-010-create-modal-validasi-field-code-dan-auto-uppercase | FE+BE | |
| TC-GS-DIV-25 | Submit Create Division — Happy Path, Stay checked (batch create) | P1 | E2E | TC-GS-DIV-E2E-015-create-division-batch-stay-checked-dan-preparasi-data | FE+BE | |
| TC-GS-DIV-26 | Submit Create Division — data tambahan utk skenario Bulk Mixed | P2 | E2E | TC-GS-DIV-E2E-015-create-division-batch-stay-checked-dan-preparasi-data | FE+BE | |
| TC-GS-DIV-27 | Tombol `[Clear Field]` — mengosongkan form tanpa menutup popup | P2 | E2E | TC-GS-DIV-E2E-011-create-modal-unsaved-changes-dialog-dan-clear-field | mock | |
| TC-GS-DIV-28 | Create Division — Master Data Count Limit tercapai | P1 | E2E | TC-GS-DIV-E2E-017-create-division-limit-reached-dan-stay-checked-boundary | FE+BE | |
| TC-GS-DIV-223 | Kombinasi Checkbox "Stay on this form" + Master Data Count Limit — record ke-N terakhir berhasil, ke-(N+1) ditolak dialog blok di popup yang sama | P1 | E2E | TC-GS-DIV-E2E-017-create-division-limit-reached-dan-stay-checked-boundary | FE+BE | |
| TC-GS-DIV-29 | Submit Create Division — Write Failure Resilience (5xx/timeout) | P1 | E2E | TC-GS-DIV-E2E-018-create-division-server-failure-resilience | mock | |
| TC-GS-DIV-30 | Create Division — dieksekusi oleh actor capability Create-Only sampai sukses | P1 | E2E | TC-GS-DIV-E2E-016-create-division-oleh-actor-capability-create-only | FE+BE | |
| TC-GS-DIV-190 | Close Popup Create Division dengan Unsaved Changes — dialog konfirmasi | P1 | E2E | TC-GS-DIV-E2E-011-create-modal-unsaved-changes-dialog-dan-clear-field | mock | |
| TC-GS-DIV-191 | Konfirmasi Unsaved Changes — `[Leave]` membuang perubahan, `[Cancel]` mempertahankan popup | P1 | E2E | TC-GS-DIV-E2E-011-create-modal-unsaved-changes-dialog-dan-clear-field | mock | |
| TC-GS-DIV-192 | Validasi Name — Fallback safety net emoji lolos block-input (server-side re-validate) | P2 | E2E | TC-GS-DIV-E2E-009-create-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-193 | Double-click Submit (Create) — hanya 1 record dibuat | P0 | E2E | TC-GS-DIV-E2E-012-create-division-happy-path-stay-unchecked | FE+BE | |
| TC-GS-DIV-194 | Hover/Click Feedback & Saving State — Tombol `[Submit]`/`[Clear Field]` Popup Create | P2 | E2E | TC-GS-DIV-E2E-008-create-modal-screening-accessibility-dan-hover | mock | |
| TC-GS-DIV-31 | Screening — Popup Edit Division (pre-filled) | P0 | E2E | TC-GS-DIV-E2E-019-edit-modal-screening-prefilled-dan-hover | mock | |
| TC-GS-DIV-33 | Validasi Edit — Boundary max 120 karakter, simetris Create (`TC-GS-DIV-20`) | P1 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-225 | Validasi Edit — Auto-trim spasi awal/akhir saat submit, simetris Create (`TC-GS-DIV-21`) | P1 | E2E | TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code | FE+BE | |
| TC-GS-DIV-226 | Validasi Edit — Debounce check keunikan (duplikat, case-insensitive), simetris Create (`TC-GS-DIV-22`) | P0 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-34 | Tombol `[Clear Field]` pada Edit — mengosongkan field (bukan reset ke nilai semula) | P2 | E2E | TC-GS-DIV-E2E-022-edit-modal-clear-field-dan-edit-no-op | FE+BE | |
| TC-GS-DIV-222 | Validasi Edit — Required, kosong saat Submit, simetris Create (`TC-GS-DIV-19`) | P0 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-35 | Save Edit Division — Happy Path | P0 | E2E | TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code | FE+BE | |
| TC-GS-DIV-36 | Save Edit Division — Duplikat nama existing lain | P1 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-265 | Save Edit Division — ubah Code existing, happy path | P0 | E2E | TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code | FE+BE | |
| TC-GS-DIV-266 | Save Edit Division — Code duplikat existing lain (case-insensitive) | P1 | E2E | TC-GS-DIV-E2E-021-edit-modal-validasi-field-code | FE+BE | |
| TC-GS-DIV-267 | Validasi Edit — Code Boundary max 15 karakter & whitelist, simetris Create (`TC-GS-DIV-261`/`262`) | P2 | E2E | TC-GS-DIV-E2E-021-edit-modal-validasi-field-code | FE+BE | |
| TC-GS-DIV-37 | Save Edit Division — Write Failure Resilience (5xx/timeout) | P1 | E2E | TC-GS-DIV-E2E-026-edit-division-server-failure-resilience | mock | |
| TC-GS-DIV-38 | Edit Division — refleksi instan ke dropdown Division form User | P1 | E2E | TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user | FE+BE | |
| TC-GS-DIV-39 | Edit Division — target data seed diizinkan diubah | P2 | E2E | TC-GS-DIV-E2E-024-edit-division-target-data-seed | FE+BE | |
| TC-GS-DIV-40 | Edit Division — dieksekusi oleh actor capability Update-Only sampai sukses | P1 | E2E | TC-GS-DIV-E2E-025-edit-division-oleh-actor-capability-update-only | FE+BE | |
| TC-GS-DIV-195 | Double-click Submit (Edit) — hanya 1 request diproses | P1 | E2E | TC-GS-DIV-E2E-023-edit-division-happy-path-rename-dan-update-code | FE+BE | |
| TC-GS-DIV-196 | Hover/Click Feedback & Saving State — Tombol `[Save]`/`[Clear Field]` Popup Edit | P2 | E2E | TC-GS-DIV-E2E-019-edit-modal-screening-prefilled-dan-hover | mock | |
| TC-GS-DIV-197 | Edit Division — No-Op, submit tanpa perubahan nilai | P3 | E2E | TC-GS-DIV-E2E-022-edit-modal-clear-field-dan-edit-no-op | FE+BE | |
| TC-GS-DIV-213 | Validasi Name — Emoji diblok di level input saat Edit (keystroke filter, simetris dgn Create TC-GS-DIV-23) | P2 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-214 | Validasi Name — Fallback safety net emoji lolos block-input saat Edit (server-side re-validate, simetris dgn Create TC-GS-DIV-192) | P2 | E2E | TC-GS-DIV-E2E-020-edit-modal-validasi-field-name-dan-keystroke | FE+BE | |
| TC-GS-DIV-41 | Screening Dialog Konfirmasi Delete — record aman (tidak in use) | P0 | E2E | TC-GS-DIV-E2E-027-delete-single-screening-cancel-dan-double-submit | mock | |
| TC-GS-DIV-42 | Delete Division (single) — Happy Path, record aman | P0 | E2E | TC-GS-DIV-E2E-029-delete-single-happy-path-record-aman | FE+BE | |
| TC-GS-DIV-43 | Delete Division (single) — Guard blocked, masih dipakai user | P0 | E2E | TC-GS-DIV-E2E-028-delete-single-guard-blocked-in-use | FE+BE | |
| TC-GS-DIV-44 | Cancel Dialog Konfirmasi Delete — tidak ada perubahan | P2 | E2E | TC-GS-DIV-E2E-027-delete-single-screening-cancel-dan-double-submit | mock | |
| TC-GS-DIV-45 | Double-Submit — klik ganda cepat tombol `[Delete]` oleh actor yang sama | P1 | E2E | TC-GS-DIV-E2E-027-delete-single-screening-cancel-dan-double-submit | mock | |
| TC-GS-DIV-46 | Delete Division (single) — dieksekusi oleh actor capability Delete-Only sampai sukses | P1 | E2E | TC-GS-DIV-E2E-030-delete-single-oleh-actor-capability-delete-only | FE+BE | |
| TC-GS-DIV-47 | Screening Bulk Action Bar — struktur elemen | P1 | E2E | TC-GS-DIV-E2E-031-bulk-action-bar-screening-counter-dan-checkbox-header | mock | |
| TC-GS-DIV-48 | Siklus Counter Realtime & Dismiss via `(X)` | P1 | E2E | TC-GS-DIV-E2E-031-bulk-action-bar-screening-counter-dan-checkbox-header | mock | |
| TC-GS-DIV-49 | Checkbox Header — Select All / Deselect All / Indeterminate | P1 | E2E | TC-GS-DIV-E2E-031-bulk-action-bar-screening-counter-dan-checkbox-header | mock | |
| TC-GS-DIV-227 | Button "Select All ({N} records)" — Server Select All Lintas Halaman, Toggle ke "Unselect All" saat 100% Terpilih, & Muncul Lagi saat Uncheck Parsial | P1 | E2E | TC-GS-DIV-E2E-032-bulk-selection-server-select-all-dan-selection-limit | FE+BE | |
| TC-GS-DIV-254 | Selection Limit — Live-Block Seleksi Manual saat Checkbox ke-1001 Dicentang | P2 | E2E | TC-GS-DIV-E2E-032-bulk-selection-server-select-all-dan-selection-limit | FE+BE | |
| TC-GS-DIV-255 | Selection Limit — Auto-Cap saat Select All Melebihi 1000 Baris Filtered | P2 | E2E | TC-GS-DIV-E2E-032-bulk-selection-server-select-all-dan-selection-limit | FE+BE | |
| TC-GS-DIV-50 | Bulk Delete — Uniform, semua item aman | P0 | E2E | TC-GS-DIV-E2E-036-bulk-delete-uniform-semua-item-aman | FE+BE | |
| TC-GS-DIV-51 | Bulk Delete — Mixed, sebagian aman sebagian in-use | P0 | E2E | TC-GS-DIV-E2E-035-bulk-delete-mixed-sebagian-aman-sebagian-in-use | FE+BE | |
| TC-GS-DIV-52 | Bulk Delete — Blocked total, semua item in-use | P1 | E2E | TC-GS-DIV-E2E-034-bulk-delete-blocked-total-seluruh-item-in-use | FE+BE | |
| TC-GS-DIV-53 | Bulk Delete — Write Failure Resilience (5xx/timeout) | P1 | E2E | TC-GS-DIV-E2E-038-bulk-delete-server-failure-resilience | mock | |
| TC-GS-DIV-257 | Bulk Delete Bar dgn hanya 1 item terpilih (aman) — collapse ke dialog Single, bukan varian bulk jamak | P1 | E2E | TC-GS-DIV-E2E-033-bulk-delete-collapse-dialog-single-n-sama-dengan-1 | FE+BE | |
| TC-GS-DIV-258 | Bulk Delete Bar dgn hanya 1 item terpilih (in-use) — collapse ke dialog blok Single, bukan varian bulk campuran | P1 | E2E | TC-GS-DIV-E2E-033-bulk-delete-collapse-dialog-single-n-sama-dengan-1 | FE+BE | |
| TC-GS-DIV-215 | Bulk Delete Division — actor dengan capability Delete-Only (bukan Total Control) sampai sukses | P1 | E2E | TC-GS-DIV-E2E-037-bulk-delete-oleh-actor-capability-delete-only | FE+BE | |
| TC-GS-DIV-54 | Search by Name — Substring / Partial Match | P1 | E2E | TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable | FE+BE | |
| TC-GS-DIV-55 | Search by Name — Case-Insensitive Match | P1 | E2E | TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable | FE+BE | |
| TC-GS-DIV-268 | Search by Code — Substring & Case-Insensitive Match | P1 | E2E | TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable | FE+BE | |
| TC-GS-DIV-269 | Sorting 3-State — kolom Code | P1 | E2E | TC-GS-DIV-E2E-042-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE | |
| TC-GS-DIV-56 | Guard Kolom Non-Searchable — "Last Updated" tidak ikut tersaring lewat Search Box | P2 | E2E | TC-GS-DIV-E2E-039-tabel-utama-search-name-dan-code-guard-non-searchable | FE+BE | |
| TC-GS-DIV-57 | Pola Interaksi Search Box Toolbar — Reveal, Auto-Focus, Submit-on-Enter, Clear, Collapse | P2 | E2E | TC-GS-DIV-E2E-040-tabel-utama-pola-interaksi-search-box-toolbar | mock | |
| TC-GS-DIV-58 | Screening Filter Panel — field "Last Updated" | P1 | E2E | TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search | FE+BE | |
| TC-GS-DIV-59 | Filter Single — "Last Updated" murni tanpa Search/Sort | P1 | E2E | TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search | FE+BE | |
| TC-GS-DIV-60 | Alur Search → Filter — irisan presisi | P2 | E2E | TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search | FE+BE | |
| TC-GS-DIV-61 | Alur Filter → Search — irisan presisi | P2 | E2E | TC-GS-DIV-E2E-041-tabel-utama-filter-panel-last-updated-dan-kombinasi-search | FE+BE | |
| TC-GS-DIV-62 | Sorting 3-State — kolom Name | P1 | E2E | TC-GS-DIV-E2E-042-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE | |
| TC-GS-DIV-63 | Sorting 3-State — kolom Last Updated | P1 | E2E | TC-GS-DIV-E2E-042-tabel-utama-sorting-3-state-name-code-dan-last-updated | FE+BE | |
| TC-GS-DIV-64 | Kombinasi Penuh 4 Kontrol — Search + Filter + Sort + Pagination | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-65 | Clear Filter saat Search & Sort aktif — kontrol lain tetap bertahan | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-66 | Clear Search saat Filter & Sort aktif — kontrol lain tetap bertahan | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-67 | Transisi Target Sort — ganti kolom sort saat Search & Filter aktif | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-68 | Pemulihan Empty State (Recovery) — melepas 1 kontrol setelah 0 hasil | P2 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-69 | Retensi Seleksi Checkbox — saat Search/Filter aktif | P3 | E2E | TC-GS-DIV-E2E-043-tabel-utama-kombinasi-4-kontrol-independensi-dan-recovery | FE+BE | |
| TC-GS-DIV-70 | Mutasi Real-time — Create record baru tidak cocok filter aktif | P2 | E2E | TC-GS-DIV-E2E-044-tabel-utama-mutasi-realtime-create-dan-edit | FE+BE | |
| TC-GS-DIV-71 | Mutasi Real-time — Edit record mengubah Name di luar keyword Search aktif | P2 | E2E | TC-GS-DIV-E2E-044-tabel-utama-mutasi-realtime-create-dan-edit | FE+BE | |
| TC-GS-DIV-72 | Setup Column Fase 1 — Screening Overlay Quick Panel | P1 | E2E | TC-GS-DIV-E2E-045-tabel-utama-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-73 | Setup Column Fase 1 — Toggle checkbox Overlay (semua Hideable, guard generik minimal 1 kolom visible) | P1 | E2E | TC-GS-DIV-E2E-045-tabel-utama-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-74 | Setup Column Fase 1 — Drag Reorder Overlay (semua kolom Hideable, reorder bebas) | P2 | E2E | TC-GS-DIV-E2E-045-tabel-utama-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-75 | Setup Column Fase 2 — Screening Popup Modal Setup Column & Live Preview | P1 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-76 | Setup Column Fase 2 — Toggle checkbox di Popup Modal, Live Preview & Save | P1 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-77 | Setup Column Fase 2 — Pin/Unpin kolom di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-78 | Setup Column Fase 3 — Tombol `[Reset to Default]` | P2 | E2E | TC-GS-DIV-E2E-047-tabel-utama-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-79 | Setup Column Fase 3 — `[Cancel]`/`(X)` membatalkan perubahan (Discard) | P2 | E2E | TC-GS-DIV-E2E-047-tabel-utama-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-80 | Setup Column Fase 3 — Independensi Cache Antar-Tabel | P2 | E2E | TC-GS-DIV-E2E-047-tabel-utama-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-228 | Kolom `Name` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-229 | Kolom `Name` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-230 | Kolom `Last Updated` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-231 | Kolom `Name` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-270 | Kolom `Code` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-271 | Kolom `Code` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-272 | Kolom `Code` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-046-tabel-utama-setup-column-fase-2-popup-modal-live-preview-dan-pin | mock | |
| TC-GS-DIV-81 | Download — All data (tanpa filter aktif) | P1 | E2E | TC-GS-DIV-E2E-048-tabel-utama-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-DIV-82 | Download — Data ter-filter saja | P1 | E2E | TC-GS-DIV-E2E-048-tabel-utama-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-DIV-83 | Download — Gagal | P2 | E2E | TC-GS-DIV-E2E-048-tabel-utama-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-DIV-84 | Pagination — Default page size & navigasi Next/Prev | P1 | E2E | TC-GS-DIV-E2E-049-tabel-utama-pagination-navigasi-dan-render-page-size | FE+BE | |
| TC-GS-DIV-85 | Pagination — Persist page size setelah Refresh | P2 | E2E | TC-GS-DIV-E2E-049-tabel-utama-pagination-navigasi-dan-render-page-size | FE+BE | |
| TC-GS-DIV-274 | Pagination — Page Size 25/50/100 Menampilkan Jumlah Baris Sesuai Pilihan | P1 | E2E | TC-GS-DIV-E2E-049-tabel-utama-pagination-navigasi-dan-render-page-size | FE+BE | |
| TC-GS-DIV-200 | Hover Warna Primary Identifier & Tooltip Teks Ter-truncate — Kolom Name Tabel Utama | P2 | E2E | TC-GS-DIV-E2E-004-hover-tooltip-toolbar-dan-teks-terpotong-tabel-utama | mock | |
| TC-GS-DIV-201 | Hover Tooltip — Icon Table Tools Tabel Utama (Filter, Download, Changelog, Setup Column) | P2 | E2E | TC-GS-DIV-E2E-004-hover-tooltip-toolbar-dan-teks-terpotong-tabel-utama | mock | |
| TC-GS-DIV-86 | Screening — Modal Changelog Division | P0 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-87 | Empty State — genuinely belum ada riwayat Changelog | P2 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-88 | Empty State — Search/Filter tanpa hasil di Modal Changelog | P1 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-89 | Search per Kolom — Action (substring & case-insensitive) | P2 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-90 | Search per Kolom — Name (substring & case-insensitive) | P2 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-91 | Search per Kolom — Field (substring & case-insensitive) | P3 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-273 | Changelog — Edit Code tercatat sebagai entri terpisah dengan Field = "Code" | P1 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-92 | Search per Kolom — Old Value (substring & case-insensitive) | P3 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-93 | Search per Kolom — New Value (substring & case-insensitive) | P3 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-94 | Search per Kolom — Modified By (substring & case-insensitive) | P3 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-95 | Guard Kolom Non-Searchable — Date tidak tersaring lewat Search Box Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-051-changelog-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-DIV-96 | Pola Interaksi Search Box Toolbar — Modal Changelog (Reveal, Auto-Focus, Submit-on-Enter, Clear, Collapse) | P2 | E2E | TC-GS-DIV-E2E-052-changelog-pola-interaksi-search-box-toolbar | mock | |
| TC-GS-DIV-97 | Screening Filter Panel — Modal Changelog (5 field) | P1 | E2E | TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | FE+BE | |
| TC-GS-DIV-98 | Filter Single — Date (Modal Changelog) | P1 | E2E | TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | FE+BE | |
| TC-GS-DIV-99 | Filter Single — Action (Modal Changelog) | P1 | E2E | TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | FE+BE | |
| TC-GS-DIV-100 | Filter Single — Name (Modal Changelog) | P1 | E2E | TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | FE+BE | |
| TC-GS-DIV-101 | Filter Single — Modified By (Modal Changelog) | P1 | E2E | TC-GS-DIV-E2E-053-changelog-filter-panel-screening-dan-filter-single | FE+BE | |
| TC-GS-DIV-102 | Kombinasi Multi-Field Filter — Action + Modified By (logika AND) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-103 | Alur Search → Filter — Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-104 | Alur Filter → Search — Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-105 | Kombinasi Penuh — Search + Filter + Sort + Pagination (Modal Changelog) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-275 | Popup Changelog — Page Size 25/50/100 Menampilkan Jumlah Baris Sesuai Pilihan | P1 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-106 | Independensi & Recovery Kontrol — Clear Filter (Modal Changelog) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-107 | Independensi & Recovery Kontrol — Clear Search (Modal Changelog) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-108 | Independensi & Recovery Kontrol — Ganti Target Sort (Modal Changelog) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-109 | Independensi & Recovery Kontrol — Empty State Recovery (Modal Changelog) | P2 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-110 | Independensi & Recovery Kontrol — Ganti Nilai Filter (Modal Changelog) | P3 | E2E | TC-GS-DIV-E2E-056-changelog-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-DIV-111 | Sorting 3-State — kolom Date (default sort tabel) | P1 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-112 | Sorting 3-State — kolom Action | P2 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-113 | Sorting 3-State — kolom Name | P2 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-114 | Sorting 3-State — kolom Field | P3 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-115 | Sorting 3-State — kolom Old Value | P3 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-116 | Sorting 3-State — kolom New Value | P3 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-117 | Sorting 3-State — kolom Modified By | P2 | E2E | TC-GS-DIV-E2E-057-changelog-sorting-3-state-7-kolom | FE+BE | |
| TC-GS-DIV-118 | Hover — Modified By menampilkan nama lengkap | P2 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-119 | Kolom Old Value/New Value Modal Changelog — Hug content (tampil penuh / wrap natural) | P2 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-120 | Setup Column Modal Changelog Fase 1 — Screening Overlay 7 Kolom | P1 | E2E | TC-GS-DIV-E2E-058-changelog-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-121 | Setup Column Modal Changelog Fase 1 — Toggle Overlay (semua Hideable, guard generik minimal 1 kolom visible) | P2 | E2E | TC-GS-DIV-E2E-058-changelog-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-122 | Setup Column Modal Changelog Fase 1 — Drag Reorder Overlay | P3 | E2E | TC-GS-DIV-E2E-058-changelog-setup-column-fase-1-overlay-quick-panel | mock | |
| TC-GS-DIV-123 | Setup Column Modal Changelog Fase 2 — Screening Popup Modal Setup Column & Live Preview | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-124 | Setup Column Modal Changelog Fase 2 — Toggle & Save | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-125 | Kolom `New Value` (☑ Hideable) Changelog — Geser di Popup Modal | P3 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-232 | Kolom `Date` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-233 | Kolom `Action` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-234 | Kolom `Name` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-235 | Kolom `Old Value` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-236 | Kolom `New Value` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-237 | Kolom `Modified By` (☑ Hideable) Changelog — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-238 | Kolom `Date` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-239 | Kolom `Action` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-240 | Kolom `Name` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-241 | Kolom `Field` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-242 | Kolom `Old Value` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-243 | Kolom `Modified By` (☑ Hideable) Changelog — Geser di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-244 | Kolom `Date` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-245 | Kolom `Action` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-246 | Kolom `Name` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-247 | Kolom `Field` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-248 | Kolom `Old Value` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-249 | Kolom `New Value` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-250 | Kolom `Modified By` (☑ Hideable) Changelog — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-DIV-E2E-059-changelog-setup-column-fase-2-popup-modal-per-kolom | mock | |
| TC-GS-DIV-126 | Setup Column Modal Changelog Fase 3 — Reset to Default | P2 | E2E | TC-GS-DIV-E2E-060-changelog-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-127 | Setup Column Modal Changelog Fase 3 — Cancel/`(X)` Discard | P2 | E2E | TC-GS-DIV-E2E-060-changelog-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-128 | Setup Column Modal Changelog Fase 3 — Independensi Cache (arah sebaliknya dari TC-GS-DIV-80) | P2 | E2E | TC-GS-DIV-E2E-060-changelog-setup-column-fase-3-reset-cancel-dan-cache-independen | mock | |
| TC-GS-DIV-129 | Download Changelog — CSV/XLSX | P2 | E2E | TC-GS-DIV-E2E-061-changelog-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-DIV-130 | Download Changelog — Gagal | P2 | E2E | TC-GS-DIV-E2E-061-changelog-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-DIV-202 | Hover Tooltip — Icon Table Tools Modal Changelog (Filter, Download) | P2 | E2E | TC-GS-DIV-E2E-050-changelog-screening-empty-states-dan-hover | FE+BE | |
| TC-GS-DIV-205 | Screening Isi Opsi Dropdown Filter Modal Changelog — Hardcode (Action) vs Populate (Name, Modified By) scoped ke Changelog, BUKAN live-join ke master data | P1 | E2E | TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | FE+BE | |
| TC-GS-DIV-206 | Dropdown Populate — Opsi Name update real-time mengikuti Division baru dibuat | P2 | E2E | TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | FE+BE | |
| TC-GS-DIV-207 | Dropdown Populate — Loading State saat opsi Name/Modified By masih di-fetch | P3 | E2E | TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | FE+BE | |
| TC-GS-DIV-208 | Dropdown Populate — Stale Reference, opsi Name yang sedang jadi kriteria filter aktif dihapus dari master data | P2 | E2E | TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | FE+BE | |
| TC-GS-DIV-209 | Search Internal Dropdown Filter — Action, Name, Modified By (substring, case-insensitive, empty state) | P2 | E2E | TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | FE+BE | |
| TC-GS-DIV-210 | Ceklis/Unceklis Multi-Select Dropdown Action — Logika OR-dalam-Field (berbeda dari AND-antar-Field TC-GS-DIV-102) | P1 | E2E | TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | FE+BE | |
| TC-GS-DIV-278 | Screening Changelog — Division hasil `[Create Missing Divisions]` dari modul `import/` tercatat sbg `Create` biasa, TIDAK ada qualifier khusus | P1 | E2E | TC-GS-DIV-E2E-054-changelog-filter-dropdown-populate-loading-dan-stale-reference | FE+BE | |
| TC-GS-DIV-211 | Removal Individual Chip via `(X)` di Dalam Field Action — Tanpa Buka Dropdown | P1 | E2E | TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | FE+BE | |
| TC-GS-DIV-224 | Removal via Uncheck Checkbox di DALAM Dropdown Terbuka Field Action — Arah Sebaliknya dari `(X)` | P1 | E2E | TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | FE+BE | |
| TC-GS-DIV-212 | Overflow Chip — Banyak Opsi Terpilih Sekaligus di Field Modified By | P3 | E2E | TC-GS-DIV-E2E-055-changelog-filter-search-internal-dropdown-dan-chip-cycles | FE+BE | |
| TC-GS-DIV-131 | Logging 3 Surface — Create Division | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-277 | Changelog — Create dgn Code manual hanya mencatat Field = "Name", entri Code TIDAK dibuat | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-132 | Logging 3 Surface — Edit Division | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-133 | Logging 3 Surface — Delete Division | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-134 | Logging 3 Surface — Bulk Delete (1 entry per item) | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-135 | Aturan Old/New Value — tidak pernah keduanya `—` sekaligus | P2 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-204 | Snapshot Immutability — Entri Changelog Lama Tidak Berubah Retroaktif Setelah Rename Kedua | P1 | E2E | TC-GS-DIV-E2E-062-logging-3-surface-create-edit-delete-dan-immutability | FE+BE | |
| TC-GS-DIV-174 | Date/Time/Timezone — Kolom Last Updated Tabel Utama | P1 | E2E | TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings | FE+BE | |
| TC-GS-DIV-175 | Date/Time/Timezone — Input Filter "Last Updated" Tabel Utama | P2 | E2E | TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings | FE+BE | |
| TC-GS-DIV-176 | Date/Time/Timezone — Kolom Date Modal Changelog | P1 | E2E | TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings | FE+BE | |
| TC-GS-DIV-177 | Date/Time/Timezone — Input Filter "Date" Modal Changelog | P2 | E2E | TC-GS-DIV-E2E-063-date-time-timezone-format-general-settings | FE+BE | |
| TC-GS-DIV-178 | Sinkronisasi Dua Arah — Post-Create Division muncul sebagai opsi baru di dropdown User | P1 | E2E | TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user | FE+BE | |
| TC-GS-DIV-179 | Sinkronisasi Dua Arah — Post-Edit nilai Division ter-update di dropdown User | P1 | E2E | TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user | FE+BE | |
| TC-GS-DIV-180 | Sinkronisasi Dua Arah — Post-Delete Division hilang dari dropdown User | P1 | E2E | TC-GS-DIV-E2E-064-sinkronisasi-dua-arah-dropdown-form-user | FE+BE | |
| TC-GS-DIV-185 | D1 — Entitas suspended/expired memblokir aksi tulis | P1 | E2E | TC-GS-DIV-E2E-065-entitas-suspended-expired-blokir-aksi-tulis | FE+BE | |
| TC-GS-DIV-186 | D6 — Concurrent Edit, 2 user mengedit Division yang sama | P1 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
| TC-GS-DIV-187 | D6 — Concurrent Delete/Edit, User A edit saat User B menghapus data yang sama | P1 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
| TC-GS-DIV-188 | D6 — Concurrent Create Duplicate, 2 user submit nama sama bersamaan | P1 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
| TC-GS-DIV-189 | D8 — Division hasil Import muncul di List & dropdown User | P2 | E2E | TC-GS-DIV-E2E-068-import-parity-operasional-edit-dan-refleksi-dropdown | FE+BE | |
| TC-GS-DIV-256 | Parity operasional — Division hasil Import bisa di-Edit (rename) dgn hasil identik ke Division hasil Create manual, buktikan Import tidak skip normalisasi/derivasi (`GAP-041`, §P7-7b) | P1 | E2E | TC-GS-DIV-E2E-068-import-parity-operasional-edit-dan-refleksi-dropdown | FE+BE | |
| TC-GS-DIV-203 | D2 — Plan Gating: Tidak Ada Gating Antar-Tier | P2 | E2E | TC-GS-DIV-E2E-066-absennya-plan-gating-seluruh-tier-plan | FE+BE | |
| TC-GS-DIV-251 | 8b-1: Cross-action race — Delete vs Delete bersamaan (2 aktor, record aman) | P1 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
| TC-GS-DIV-252 | 8b-1: Cross-action race — Edit vs Bulk Delete bersamaan (2 aktor) | P1 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
| TC-GS-DIV-253 | 8c-1: Concurrent Create vs Master Data Count Limit — slot terakhir | P2 | E2E | TC-GS-DIV-E2E-067-cross-action-race-concurrency-edit-delete-dan-limit | mock | |
