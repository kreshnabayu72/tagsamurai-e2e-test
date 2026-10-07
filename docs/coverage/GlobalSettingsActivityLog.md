# Coverage Ledger — Global Settings > Activity Log

Dokumen ini melacak keterlacakan (*traceability*) antara **227 Test Cases granular** pada [`global-settings/activity-log/TestCases/tc-activity-log.md`](../../../global-settings/activity-log/TestCases/tc-activity-log.md) dengan **57 File Spesifikasi E2E TestSpectra** yang telah direstrukturisasi secara terisolasi dan modular.

---

## 1. Ringkasan Eksekutif

| Indikator | Nilai | Keterangan |
| :--- | :---: | :--- |
| **Total Test Case Granular Sumber** | **227** | `TC-GS-ACTLOG-01` s/d `TC-GS-ACTLOG-227` |
| **Total Spec E2E TestSpectra** | **57** | Tersimpan di `tagsamurai-e2e-test/specs/GlobalSettings/ActivityLog/` |
| **Granular TC Terpetakan** | **227 / 227** | **100.0% Coverage** |
| **Duplikasi Pemetaan** | **0** | Setiap granular TC dipetakan tepat satu kali ke 1 spec |
| **TC Tanpa Pemetaan (Uncovered)** | **0** | Tidak ada celah cakupan |
| **Status Validasi TestSpectra** | **Lolos Linter Strict** | `npx spectra lint --strict specs/GlobalSettings/ActivityLog` (0 error, 57 specs & 1 suite verified) |
| **Pembagian Mode Eksekusi** | **49 FE+BE, 8 Mock** | Mock dialokasikan untuk skeleton network throttle, empty state murni, tooltip hover, guided walkthrough, viewport mobile, bahasa i18n, download network fault 500, dan ekspor skala besar |

---

## 2. Pemisahan Modular Berdasarkan Domain Masalah

Arsitektur 57 spec E2E ini dirancang untuk memaksimalkan **stabilitas eksekusi otomatis** dan **kemudahan isolasi kegagalan (*failure isolation*)**:

1. **Screening Umum & State Dasar Tabel (Spec 001 - 010):**
   - Struktur 3 zona (header, toolbar, tabel), breadcrumb navigasi dua arah, skeleton loading & recovery 500 (`mock`), empty state data murni kosong (`mock`), no-result state pasca-pencarian, default sort & tie-break, tooltip hover cell (`mock`), guided walkthrough tooltip (`mock`), viewport responsif mobile (`mock`), dan lokalisasi bahasa i18n (`mock`).
2. **Role & Tenant Scoping (Spec 011 - 014):**
   - Role matrix positif (Total Control & Read Only), role matrix negatif (Direct URL 403 & ketiadaan menu), isolasi tenant multi-organisasi, dan batasan produk Global Settings vs produk lain.
3. **Tab Session — Pola Entri Terisolasi (Spec 015 - 017):**
   - **Spec 015 (Core Session):** Login Berhasil, Logout normal (status `—`), sesi internal GS, penanganan sel kosong `—`, dan format plain text sel Date.
   - **Spec 016 (Security Events):** Login Gagal (Bad Credentials, Account Locked, Client Suspended), alur Reset Password, dan Change Password.
   - **Spec 017 (External & Cross-Module Auth):** Admin Concurrent License Force-Logout, sesi SSO SAML/OIDC, dan sesi Mobile Native.
4. **Tab Session — Immutability, Search, Filter, Sort & Setup Column (Spec 018 - 029):**
   - Immutability data historis user (`018`), search multi-kolom toolbar (`019`), interaksi search box (`020`), struktur filter panel 6 dimensi (`021`), pengisian opsi dropdown dinamis dari data log (`022`), pencarian dropdown & chip filter (`023`), kombinasi multi-filter & recovery (`024`), sorting 3-state 10 kolom (`025`), setup column screening & guard minimal 1 kolom (`026`), setup column visibilitas checkbox (`027`), setup column drag-drop reordering (`028`), setup column sticky pin batas 3 kolom & reset (`029`).
5. **Lintas-Tab, Paginasi & Ekspor Data Terisolasi (Spec 030 - 034):**
   - Independensi state filter/search/sort/setup column antar-tab (`030`), paginasi terisolasi & persistensi page size (`031`).
   - **Spec 032 (Export Generation & Integrity):** Validasi file CSV & XLSX, UTF-8 BOM, filter state, dan read-only idempotency guard.
   - **Spec 033 (Export Failure Resilience):** Intercept kegagalan jaringan HTTP 500 dan toast error feedback (`mock`).
   - **Spec 034 (Large Export Threshold):** Loading screen modal dan batas threshold >5.000 baris (`mock`).
6. **Tab User Action — Pola Entri CRUD & Non-CRUD (Spec 035 - 036):**
   - Pola entri Create, Edit, Delete & pemecahan multi-field edit menjadi N baris terpisah dengan timestamp identik (`035`), serta pola mutasi relasi non-CRUD & bulk import CSV (`036`).
7. **Tab User Action — Search, Filter, Sort & Setup Column (Spec 037 - 046):**
   - Search multi-kolom toolbar (`037`), interaksi search box (`038`), struktur filter panel 5 dimensi (`039`), pengisian opsi dropdown dinamis dari modul pembuat (`040`), pencarian dropdown & chip removal (`041`), sorting 3-state 8 kolom (`042`), setup column screening & guard minimal 1 kolom (`043`), setup column visibilitas checkbox (`044`), setup column drag-drop reordering (`045`), setup column sticky pin batas 3 kolom & reset (`046`).
8. **Integrasi Sistem, Streaming Real-Time, Transaksi Atomik & Keamanan Terisolasi (Spec 047 - 057):**
   - Sinkronisasi format tanggal dan waktu General Settings (`047`).
   - **Spec 048 (SSE Local Reactivity):** Penambahan baris otomatis real-time dan filter-matching guard pada kedua tab.
   - **Spec 049 (SSE Tenant Boundary Security):** Isolasi streaming event real-time lintas tenant (Alfa vs Beta).
   - **Spec 050 (Standard Master Data Ingestion):** Ingestion mutasi 9 modul Global Settings, Hardware BLE, dan TAG Registry.
   - **Spec 051 (File Manager & System Actor Audit):** Permanently Delete File Manager dan Background System Auto-Purge (`Modified By = "System"`).
   - **Spec 052 (Atomic Transaction Rollback):** Fault injection 5xx & zero phantom log pada operasi database yang gagal.
   - **Spec 053 (Immutability & Chronological Ordering):** Snapshot nama admin pada mutasi masa lalu dan pengurutan kronologis event out-of-order.
   - **Spec 054 (API Authorization 403 & Parameter Isolation):** Penolakan akses langsung endpoint API (403) dan proteksi query parameter tampering multi-produk.
   - **Spec 055 (DOM Security & Query Matching):** Sanitasi XSS di Search Box dan sel tabel (stored & reflected) serta pencocokan regex literal string.
   - **Spec 056 (Tenant Lifecycle):** Akses riwayat audit dan pencatatan aksi sistem pada Client yang berstatus Suspended/Expired.
   - **Spec 057 (Data Retention & Plan Parity):** Retensi log historis 3 tahun tanpa batas waktu dan paritas fungsional penuh 4 tier langganan (tanpa gating).

---

## 3. Matriks Pemetaan Lengkap (57 Specs)

| No | ID Spec E2E | Judul Spec | Mode | Jumlah TC | Granular TC yang Dicakup |
| :---: | :--- | :--- | :---: | :---: | :--- |
| 001 | `TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab` | Screening 3 Zona Tab Session dan User Action, Navigasi Tab, serta Tab Default | FE+BE | 4 | TC-GS-ACTLOG-01, TC-GS-ACTLOG-02, TC-GS-ACTLOG-03, TC-GS-ACTLOG-227 |
| 002 | `TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience` | Loading Skeleton dan Ketahanan Kegagalan Load Tabel di Kedua Tab | mock | 3 | TC-GS-ACTLOG-04, TC-GS-ACTLOG-08, TC-GS-ACTLOG-09 |
| 003 | `TC-GS-ACTLOG-E2E-003-empty-state-genuinely-kosong` | Tampilan Empty State Genuinely Kosong pada Tab Session dan User Action | mock | 1 | TC-GS-ACTLOG-05 |
| 004 | `TC-GS-ACTLOG-E2E-004-no-result-state-pencarian-tanpa-hasil` | Tampilan No-Result State Akibat Pencarian dan Filter Tanpa Hasil serta Pemulihan Data | FE+BE | 3 | TC-GS-ACTLOG-06, TC-GS-ACTLOG-07, TC-GS-ACTLOG-108 |
| 005 | `TC-GS-ACTLOG-E2E-005-default-sort-dan-tie-break-kedua-tab` | Default Sort Date Descending dan Tie-Break Timestamp Identik di Kedua Tab | FE+BE | 2 | TC-GS-ACTLOG-10, TC-GS-ACTLOG-11 |
| 006 | `TC-GS-ACTLOG-E2E-006-hover-tooltip-toolbar-dan-teks-terpotong` | Hover Tooltip pada Table Tools dan Nama Lengkap User serta Modified By | mock | 3 | TC-GS-ACTLOG-12, TC-GS-ACTLOG-13, TC-GS-ACTLOG-14 |
| 007 | `TC-GS-ACTLOG-E2E-007-read-only-guard-ketiadaan-kontrol-tulis-dan-format-plain-text` | Guard Read-Only Modul: Baris Non-Klik, Ketiadaan Kontrol Tulis, dan Format Plain Text | FE+BE | 3 | TC-GS-ACTLOG-15, TC-GS-ACTLOG-16, TC-GS-ACTLOG-221 |
| 008 | `TC-GS-ACTLOG-E2E-008-guided-tooltip-walkthrough` | Siklus Lengkap Guided Tooltip Walkthrough, Navigasi Tombol, Overlay, dan Keyboard | mock | 6 | TC-GS-ACTLOG-18, TC-GS-ACTLOG-19, TC-GS-ACTLOG-20, TC-GS-ACTLOG-21, TC-GS-ACTLOG-22, TC-GS-ACTLOG-23 |
| 009 | `TC-GS-ACTLOG-E2E-009-mobile-layout-card-session-user-action-dan-download` | Mobile Layout Card List Session, User Action, dan Download Seluruh Kolom | mock | 4 | TC-GS-ACTLOG-24, TC-GS-ACTLOG-25, TC-GS-ACTLOG-26, TC-GS-ACTLOG-140 |
| 010 | `TC-GS-ACTLOG-E2E-010-ganti-bahasa-kolom-verbatim-dan-translatable` | Dukungan Multibahasa: Nilai Kolom Verbatim Tetap dan Nilai Translatable Mengikuti Pilihan Bahasa | mock | 1 | TC-GS-ACTLOG-27 |
| 011 | `TC-GS-ACTLOG-E2E-011-role-matrix-positif-total-control-dan-read-only` | Role Matrix Positif: Total Control dan Read Only Memiliki Akses Penuh Identik | FE+BE | 2 | TC-GS-ACTLOG-28, TC-GS-ACTLOG-29 |
| 012 | `TC-GS-ACTLOG-E2E-012-role-matrix-negatif-pengguna-tanpa-akses` | Role Matrix Negatif: Penolakan Akses Menu dan Direct URL untuk Pengguna Tanpa Akses | FE+BE | 5 | TC-GS-ACTLOG-30, TC-GS-ACTLOG-31, TC-GS-ACTLOG-32, TC-GS-ACTLOG-33, TC-GS-ACTLOG-34 |
| 013 | `TC-GS-ACTLOG-E2E-013-tenant-scoping-dan-isolasi-data` | Isolasi Data Antar-Tenant dan Entitas (Client, Principal, Distributor, Partner) Tanpa Masking | FE+BE | 4 | TC-GS-ACTLOG-35, TC-GS-ACTLOG-36, TC-GS-ACTLOG-37, TC-GS-ACTLOG-127 |
| 014 | `TC-GS-ACTLOG-E2E-014-scope-produk-global-settings-dan-eksklusi-produk-lain` | Scope Produk Global Settings: Inklusi Login Platform & Sesi GS serta Eksklusi Modul Lain | FE+BE | 3 | TC-GS-ACTLOG-38, TC-GS-ACTLOG-39, TC-GS-ACTLOG-40 |
| 015 | `TC-GS-ACTLOG-E2E-015-tab-session-entri-dasar-login-logout-dan-status-dash` | Tab Session: Entri Dasar Login Berhasil, Logout Normal dengan Status Dash, Sesi GS, dan Format Sel Kosong | FE+BE | 6 | TC-GS-ACTLOG-41, TC-GS-ACTLOG-45, TC-GS-ACTLOG-51, TC-GS-ACTLOG-52, TC-GS-ACTLOG-53, TC-GS-ACTLOG-226 |
| 016 | `TC-GS-ACTLOG-E2E-016-tab-session-event-keamanan-gagal-login-lockout-dan-password` | Tab Session: Event Keamanan Login Gagal Bad Credentials, Account Locked, Client Suspended, dan Sesi Password | FE+BE | 5 | TC-GS-ACTLOG-42, TC-GS-ACTLOG-43, TC-GS-ACTLOG-44, TC-GS-ACTLOG-46, TC-GS-ACTLOG-47 |
| 017 | `TC-GS-ACTLOG-E2E-017-tab-session-ingestion-force-logout-sso-dan-mobile` | Tab Session: Ingestion Sesi Force-Logout oleh Admin, Login SSO SAML/OIDC, dan Mobile Device | FE+BE | 3 | TC-GS-ACTLOG-48, TC-GS-ACTLOG-49, TC-GS-ACTLOG-50 |
| 018 | `TC-GS-ACTLOG-E2E-018-tab-session-snapshot-immutability-data-historis-user` | Snapshot Immutability Tab Session: Data Historis Tidak Berubah Saat User Dimutasi atau Dihapus | FE+BE | 2 | TC-GS-ACTLOG-54, TC-GS-ACTLOG-55 |
| 019 | `TC-GS-ACTLOG-E2E-019-tab-session-search-per-kolom-dan-guard-date` | Tab Session: Search Substring, Case-Insensitive, Status Nilai Tampil, dan Guard Kolom Date | FE+BE | 9 | TC-GS-ACTLOG-56, TC-GS-ACTLOG-57, TC-GS-ACTLOG-58, TC-GS-ACTLOG-59, TC-GS-ACTLOG-60, TC-GS-ACTLOG-61, TC-GS-ACTLOG-62, TC-GS-ACTLOG-63, TC-GS-ACTLOG-64 |
| 020 | `TC-GS-ACTLOG-E2E-020-tab-session-pola-interaksi-search-box-toolbar` | Tab Session: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse) | FE+BE | 1 | TC-GS-ACTLOG-65 |
| 021 | `TC-GS-ACTLOG-E2E-021-tab-session-struktur-filter-panel-dan-filter-individual` | Tab Session: Struktur 6 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Filter Date | FE+BE | 10 | TC-GS-ACTLOG-66, TC-GS-ACTLOG-67, TC-GS-ACTLOG-68, TC-GS-ACTLOG-69, TC-GS-ACTLOG-70, TC-GS-ACTLOG-71, TC-GS-ACTLOG-74, TC-GS-ACTLOG-75, TC-GS-ACTLOG-76, TC-GS-ACTLOG-77 |
| 022 | `TC-GS-ACTLOG-E2E-022-tab-session-populate-opsi-filter-dari-data-log` | Tab Session: Opsi Filter Terpopulasi Dinamis dari Data Tabel dan Ketiadaan Opsi None | FE+BE | 6 | TC-GS-ACTLOG-78, TC-GS-ACTLOG-79, TC-GS-ACTLOG-80, TC-GS-ACTLOG-113, TC-GS-ACTLOG-114, TC-GS-ACTLOG-115 |
| 023 | `TC-GS-ACTLOG-E2E-023-tab-session-search-dropdown-logika-or-dan-chip-removal` | Tab Session: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow | FE+BE | 5 | TC-GS-ACTLOG-81, TC-GS-ACTLOG-82, TC-GS-ACTLOG-83, TC-GS-ACTLOG-84, TC-GS-ACTLOG-85 |
| 024 | `TC-GS-ACTLOG-E2E-024-tab-session-kombinasi-multi-filter-alur-search-dan-recovery` | Tab Session: Alur Kombinasi Search dan Filter, [Clear Field], dan Batalkan Perubahan | FE+BE | 10 | TC-GS-ACTLOG-72, TC-GS-ACTLOG-73, TC-GS-ACTLOG-104, TC-GS-ACTLOG-105, TC-GS-ACTLOG-106, TC-GS-ACTLOG-107, TC-GS-ACTLOG-109, TC-GS-ACTLOG-110, TC-GS-ACTLOG-111, TC-GS-ACTLOG-112 |
| 025 | `TC-GS-ACTLOG-E2E-025-tab-session-sorting-3-state-10-kolom` | Tab Session: Siklus Sorting 3-State untuk 10 Kolom dan Penanganan Nilai Kosong | FE+BE | 8 | TC-GS-ACTLOG-86, TC-GS-ACTLOG-87, TC-GS-ACTLOG-88, TC-GS-ACTLOG-89, TC-GS-ACTLOG-90, TC-GS-ACTLOG-91, TC-GS-ACTLOG-92, TC-GS-ACTLOG-116 |
| 026 | `TC-GS-ACTLOG-E2E-026-tab-session-setup-column-screening-dan-guard-minimal-1-kolom` | Tab Session Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom | FE+BE | 5 | TC-GS-ACTLOG-93, TC-GS-ACTLOG-94, TC-GS-ACTLOG-95, TC-GS-ACTLOG-102, TC-GS-ACTLOG-103 |
| 027 | `TC-GS-ACTLOG-E2E-027-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5` | Tab Session Setup Column: Pengaturan Visibilitas 10 Kolom Hideable dan Persistensi F5 | FE+BE | 1 | TC-GS-ACTLOG-96 |
| 028 | `TC-GS-ACTLOG-E2E-028-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5` | Tab Session Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5 | FE+BE | 1 | TC-GS-ACTLOG-97 |
| 029 | `TC-GS-ACTLOG-E2E-029-tab-session-setup-column-pin-sticky-reset-default-dan-cancel` | Tab Session Setup Column: Pembekuan Kolom Sticky Pin/Unpin, Batas 3 Kolom, dan Reset | FE+BE | 4 | TC-GS-ACTLOG-98, TC-GS-ACTLOG-99, TC-GS-ACTLOG-100, TC-GS-ACTLOG-101 |
| 030 | `TC-GS-ACTLOG-E2E-030-independensi-state-search-filter-sort-dan-setup-column-antar-tab` | Independensi State Search, Filter, Sort, Setup Column, dan Paginasi Antar-Tab | FE+BE | 3 | TC-GS-ACTLOG-17, TC-GS-ACTLOG-117, TC-GS-ACTLOG-126 |
| 031 | `TC-GS-ACTLOG-E2E-031-pagination-kedua-tab-page-size-navigasi-dan-persistensi` | Paginasi Kedua Tab: Pilihan Page Size 10/25/50/100, Navigasi Halaman, dan Persistensi State | FE+BE | 4 | TC-GS-ACTLOG-118, TC-GS-ACTLOG-119, TC-GS-ACTLOG-120, TC-GS-ACTLOG-121 |
| 032 | `TC-GS-ACTLOG-E2E-032-download-log-csv-xlsx-format-encoding-dan-idempotency` | Download Laporan Audit CSV dan XLSX: Validasi Format, Header, Encoding UTF-8 BOM, dan Read-Only Idempotency | FE+BE | 12 | TC-GS-ACTLOG-122, TC-GS-ACTLOG-123, TC-GS-ACTLOG-124, TC-GS-ACTLOG-125, TC-GS-ACTLOG-128, TC-GS-ACTLOG-129, TC-GS-ACTLOG-130, TC-GS-ACTLOG-131, TC-GS-ACTLOG-132, TC-GS-ACTLOG-133, TC-GS-ACTLOG-134, TC-GS-ACTLOG-135 |
| 033 | `TC-GS-ACTLOG-E2E-033-download-log-resilience-kegagalan-jaringan-dan-toast-error` | Ketahanan Ekspor Log: Penanganan Kegagalan Jaringan / HTTP 500 dan Toast Feedback Error di Kedua Tab | mock | 2 | TC-GS-ACTLOG-138, TC-GS-ACTLOG-139 |
| 034 | `TC-GS-ACTLOG-E2E-034-download-log-di-atas-5000-baris-loading-screen-dan-batas-threshold` | Download Log Skala Besar (>5.000 Baris): Loading Screen Modal dan Pengujian Batas Threshold | mock | 2 | TC-GS-ACTLOG-136, TC-GS-ACTLOG-137 |
| 035 | `TC-GS-ACTLOG-E2E-035-tab-user-action-pola-entri-crud-dan-multi-field-edit` | Tab User Action: Pola Entri CRUD (Create, Edit, Delete) dan Multi-Field Edit dalam Satu Simpan | FE+BE | 4 | TC-GS-ACTLOG-141, TC-GS-ACTLOG-142, TC-GS-ACTLOG-143, TC-GS-ACTLOG-144 |
| 036 | `TC-GS-ACTLOG-E2E-036-tab-user-action-pola-entri-non-crud-relasi-dan-import-bulk` | Tab User Action: Pola Entri Non-CRUD Relasi User, System Role, Status, dan Import Bulk | FE+BE | 5 | TC-GS-ACTLOG-145, TC-GS-ACTLOG-146, TC-GS-ACTLOG-147, TC-GS-ACTLOG-148, TC-GS-ACTLOG-149 |
| 037 | `TC-GS-ACTLOG-E2E-037-tab-user-action-search-per-kolom-dan-multi-kolom` | Tab User Action: Search Substring, Case-Insensitive, Modified By Nama Lengkap, dan Guard Date | FE+BE | 8 | TC-GS-ACTLOG-150, TC-GS-ACTLOG-151, TC-GS-ACTLOG-152, TC-GS-ACTLOG-153, TC-GS-ACTLOG-154, TC-GS-ACTLOG-155, TC-GS-ACTLOG-156, TC-GS-ACTLOG-157 |
| 038 | `TC-GS-ACTLOG-E2E-038-tab-user-action-pola-interaksi-search-box-toolbar` | Tab User Action: Siklus Interaksi Search Box Toolbar (Reveal, Clear Tanpa Reset, Submit, Collapse) | FE+BE | 1 | TC-GS-ACTLOG-158 |
| 039 | `TC-GS-ACTLOG-E2E-039-tab-user-action-struktur-filter-panel-dan-filter-individual` | Tab User Action: Struktur 5 Field Filter Panel, Logika OR Intra-Field, Logika AND, dan Alur Search-Filter | FE+BE | 6 | TC-GS-ACTLOG-159, TC-GS-ACTLOG-160, TC-GS-ACTLOG-161, TC-GS-ACTLOG-162, TC-GS-ACTLOG-163, TC-GS-ACTLOG-164 |
| 040 | `TC-GS-ACTLOG-E2E-040-tab-user-action-populate-opsi-filter-dari-data-log` | Tab User Action: Opsi Filter Terpopulasi Dinamis dari Modul Pengirim dan Penanganan Admin Dihapus | FE+BE | 5 | TC-GS-ACTLOG-165, TC-GS-ACTLOG-166, TC-GS-ACTLOG-167, TC-GS-ACTLOG-168, TC-GS-ACTLOG-169 |
| 041 | `TC-GS-ACTLOG-E2E-041-tab-user-action-search-dropdown-logika-or-dan-chip-removal` | Tab User Action: Search di Dalam Dropdown Filter, Seleksi Chip, Deselect, dan Overflow | FE+BE | 5 | TC-GS-ACTLOG-170, TC-GS-ACTLOG-171, TC-GS-ACTLOG-172, TC-GS-ACTLOG-173, TC-GS-ACTLOG-174 |
| 042 | `TC-GS-ACTLOG-E2E-042-tab-user-action-sorting-3-state-8-kolom` | Tab User Action: Sorting 3-State untuk 8 Kolom, Kolom Campuran Angka-Teks, dan Nilai Kosong | FE+BE | 5 | TC-GS-ACTLOG-175, TC-GS-ACTLOG-176, TC-GS-ACTLOG-177, TC-GS-ACTLOG-178, TC-GS-ACTLOG-179 |
| 043 | `TC-GS-ACTLOG-E2E-043-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom` | Tab User Action Setup Column: Screening Overlay & Popup, Toggle Cepat, dan Guard Minimal 1 Kolom | FE+BE | 5 | TC-GS-ACTLOG-180, TC-GS-ACTLOG-181, TC-GS-ACTLOG-182, TC-GS-ACTLOG-189, TC-GS-ACTLOG-190 |
| 044 | `TC-GS-ACTLOG-E2E-044-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5` | Tab User Action Setup Column: Pengaturan Visibilitas 8 Kolom Hideable dan Persistensi F5 | FE+BE | 1 | TC-GS-ACTLOG-183 |
| 045 | `TC-GS-ACTLOG-E2E-045-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5` | Tab User Action Setup Column: Reorder Urutan Kolom via Drag-and-Drop dan Persistensi F5 | FE+BE | 1 | TC-GS-ACTLOG-184 |
| 046 | `TC-GS-ACTLOG-E2E-046-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel` | Tab User Action Setup Column: Pembekuan Kolom Sticky Pin/Unpin, Batas 3 Kolom, dan Reset | FE+BE | 4 | TC-GS-ACTLOG-185, TC-GS-ACTLOG-186, TC-GS-ACTLOG-187, TC-GS-ACTLOG-188 |
| 047 | `TC-GS-ACTLOG-E2E-047-sinkronisasi-format-tanggal-dan-waktu-general-settings` | Sinkronisasi Format Tanggal dan Waktu Mengikuti Konfigurasi General Settings di Kedua Tab | FE+BE | 4 | TC-GS-ACTLOG-191, TC-GS-ACTLOG-192, TC-GS-ACTLOG-193, TC-GS-ACTLOG-194 |
| 048 | `TC-GS-ACTLOG-E2E-048-sinkronisasi-real-time-sse-entri-baru-dan-filter-guard` | Sinkronisasi Real-Time SSE: Kemunculan Otomatis Entri Baru dan Filter-Matching Guard di Kedua Tab | FE+BE | 3 | TC-GS-ACTLOG-195, TC-GS-ACTLOG-196, TC-GS-ACTLOG-197 |
| 049 | `TC-GS-ACTLOG-E2E-049-sinkronisasi-real-time-sse-isolasi-keamanan-lintas-tenant` | Isolasi Keamanan Real-Time SSE: Pencegahan Kebocoran Event Streaming Lintas-Tenant (Alfa vs Beta) | FE+BE | 1 | TC-GS-ACTLOG-198 |
| 050 | `TC-GS-ACTLOG-E2E-050-ingestion-user-action-lintas-modul-master-data-global-settings` | Ingestion User Action dari Mutasi Master Data 9 Modul Global Settings, Hardware, dan TAG Registry | FE+BE | 10 | TC-GS-ACTLOG-199, TC-GS-ACTLOG-200, TC-GS-ACTLOG-201, TC-GS-ACTLOG-202, TC-GS-ACTLOG-203, TC-GS-ACTLOG-204, TC-GS-ACTLOG-205, TC-GS-ACTLOG-206, TC-GS-ACTLOG-207, TC-GS-ACTLOG-208 |
| 051 | `TC-GS-ACTLOG-E2E-051-ingestion-user-action-file-manager-delete-dan-system-purge` | Ingestion User Action: File Manager Permanently Delete dan Background System Auto-Purge Actor Audit | FE+BE | 3 | TC-GS-ACTLOG-209, TC-GS-ACTLOG-210, TC-GS-ACTLOG-211 |
| 052 | `TC-GS-ACTLOG-E2E-052-integritas-ingestion-atomik-rollback-transaksi-gagal` | Atomic Rollback Ingestion: Ketiadaan Pencatatan Log pada Operasi Database yang Gagal (Zero Phantom Log) | FE+BE | 1 | TC-GS-ACTLOG-212 |
| 053 | `TC-GS-ACTLOG-E2E-053-integritas-ingestion-snapshot-immutability-dan-urutan-kronologis` | Snapshot Immutability Modified By dan Pengurutan Kronologis Berdasarkan Waktu Date untuk Event Out-of-Order | FE+BE | 2 | TC-GS-ACTLOG-213, TC-GS-ACTLOG-214 |
| 054 | `TC-GS-ACTLOG-E2E-054-security-defense-in-depth-penolakan-api-403-dan-isolasi-produk` | Security & Defense-in-Depth: Penolakan Akses Langsung Endpoint API 403 dan Isolasi Parameter Multi-Produk | FE+BE | 3 | TC-GS-ACTLOG-215, TC-GS-ACTLOG-216, TC-GS-ACTLOG-217 |
| 055 | `TC-GS-ACTLOG-E2E-055-security-defense-in-depth-sanitasi-xss-dan-regex-literal` | Security & Defense-in-Depth: Sanitasi Payload XSS di Kotak Pencarian dan Sel Tabel serta Pencocokan String Regex Literal | FE+BE | 3 | TC-GS-ACTLOG-218, TC-GS-ACTLOG-219, TC-GS-ACTLOG-220 |
| 056 | `TC-GS-ACTLOG-E2E-056-edge-case-akses-dan-ingestion-saat-client-suspended` | Edge Case Bisnis: Akses Riwayat Log dan Ingestion Audit Otomatis saat Status Client Suspended/Expired | FE+BE | 2 | TC-GS-ACTLOG-222, TC-GS-ACTLOG-223 |
| 057 | `TC-GS-ACTLOG-E2E-057-edge-case-retensi-data-tanpa-batas-dan-paritas-paket-langganan` | Edge Case Bisnis: Retensi Data Historis Lintas Tahun Tanpa Batas dan Paritas Fungsional Penuh Seluruh Tier Plan | FE+BE | 2 | TC-GS-ACTLOG-224, TC-GS-ACTLOG-225 |
