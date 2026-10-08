# Coverage E2E — Global Settings > User > Position

Sumber: `global-settings/position/TestCases/tc-position.md`.
Referensi kontrak: `global-settings/position/PRD/position.md` dan `global-settings/position/API/openapi.yaml`.
Suite: `specs_dummy/GlobalSettings/Position/`.
Prefix Modul: `GS` + `POS` (`TC-GS-POS-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-position.md`: 308 baris (`TC-GS-POS-1` s.d. `TC-GS-POS-308`).**
Cakupan otomasi spec E2E: **100% dari aspek UI/FE (302 dari 308 TC masuk spec, 6 TC hanya-BE)**.
Total Spec E2E yang dihasilkan: **54 spec atomik terisolasi tinggi**.

---

## 1. Pemetaan TC Granular → Spec E2E (54 spec)

302 dari 308 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | Screening tab Position, breadcrumb, visual styling, dan default sort Name A-Z | FE+BE | 1, 2, 3, 4, 5, 9, 291, 293 |
| TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | Empty state pada entitas baru tanpa record Position | FE+BE | 7, 296 |
| TC-GS-POS-E2E-003-resilience-loading-state-dan-error-try-again | Resilience: Loading skeleton dan pemulihan error load via Try Again | mock | 6, 8 |
| TC-GS-POS-E2E-004-pagination-dan-page-size-tabel-utama | Pagination default 10 baris, navigasi halaman, dan opsi page size 10/25/50/100 | FE+BE | 10, 11, 12 |
| TC-GS-POS-E2E-005-persistensi-state-tabel-f5-dan-navigasi | Persistensi state tabel saat F5, reset saat klik sidebar, dan retensi saat pindah sub-tab | FE+BE | 13, 14, 15 |
| TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | Guided Tooltip walkthrough 3-step, navigasi keyboard, resize, dan dismiss/replay | FE+BE | 16, 17, 18, 19, 20, 21, 22, 23, 24 |
| TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | Role Matrix: Visibilitas tab Position dan kontrol UI per capability Manage user and role | FE+BE | 25, 26, 27, 28, 29, 30, 31, 36 |
| TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete | Role Matrix Positif: Eksekusi Create, Edit, Delete, dan Bulk Delete oleh aktor capability spesifik | FE+BE | 32, 33, 34, 35 |
| TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | Screening form Create, aksesibilitas dialog, dan validasi inline input Position Name | FE+BE | 37, 38, 39, 40, 42, 43, 44, 45, 46, 50, 284 |
| TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | Validasi nama duplikat case-insensitive saat mengetik dan guard double-submit Save state | FE+BE | 47, 48, 49, 65, 66 |
| TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | Penutupan form Create via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes | FE+BE | 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 |
| TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | Create Position sukses, trim whitespace, Stay on this form, 1 karakter, 120 karakter, dan refresh persistence | FE+BE | 41, 51, 52, 53, 54, 73, 282, 286 |
| TC-GS-POS-E2E-013-resilience-create-position-kegagalan-server | Resilience: Form Create mempertahankan input saat kegagalan server 5xx dan timeout jaringan | mock | 67, 68 |
| TC-GS-POS-E2E-014-master-data-count-limit-create-guard | Volume Data: Penegakan Master Data Count Limit pada tombol [+ Position], submit, dan Stay on this form | FE+BE | 69, 70, 71, 72, 259, 280 |
| TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | Screening overlay Row Action, form Edit, aksesibilitas dialog, dan validasi field inline | FE+BE | 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 88, 285 |
| TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | Validasi nama duplikat saat edit, pengecualian nama sendiri, dan guard double-click Save | FE+BE | 85, 86, 87, 104, 105 |
| TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | Penutupan form Edit via ✕, Esc, backdrop, in-app navigation, dan dialog Unsaved Changes | FE+BE | 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103 |
| TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | Edit Position sukses rename, kapitalisasi, No-Op tanpa log/update, 1 karakter, 120 karakter, dan record seed | FE+BE | 79, 89, 90, 91, 92, 110, 283, 287 |
| TC-GS-POS-E2E-019-resilience-edit-position-kegagalan-server | Resilience: Form Edit mempertahankan form saat kegagalan server 5xx, timeout, dan retry No-Op | mock | 106, 107, 108 |
| TC-GS-POS-E2E-020-security-edit-position-pencabutan-capability-di-tengah-sesi | Security: Save Edit setelah capability Update dicabut di tengah sesi ditolak 403 | FE+BE | 294 |
| TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | Delete single Position bebas relasi berhasil, Cancel dialog, guard double-click, dan delete record terakhir | FE+BE | 111, 112, 113, 120, 122, 299 |
| TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use | Blokir Delete single karena Position dipakai user Login aktif, Non-Login, atau user non-aktif | FE+BE | 114, 115, 116, 117 |
| TC-GS-POS-E2E-023-resilience-delete-single-kegagalan-server | Resilience: Dialog Delete single saat kegagalan server 5xx menampilkan toast error dan record tetap ada | mock | 121 |
| TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | Screening Bulk Action Bar, counter realtime, Select All N records lintas halaman, Unselect All, dan retensi state | FE+BE | 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134 |
| TC-GS-POS-E2E-025-selection-limit-bulk-checkbox-dan-select-all | Volume Data: Penegakan Selection Limit pada checkbox manual ke-(limit+1) dan pembatasan Select All | FE+BE | 135, 136 |
| TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | Bulk Delete homogen bebas relasi berhasil, dialog collapse saat 1 item, scrollable list, dan guard double-click | FE+BE | 137, 138, 139, 140, 141, 146, 150 |
| TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | Bulk Delete campuran (sebagian in-use warn lalu continue) dan blokir total seluruhnya in-use | FE+BE | 142, 143, 144, 145, 302, 303 |
| TC-GS-POS-E2E-028-resilience-bulk-delete-atomik-pada-kegagalan-server | Resilience: Bulk Delete atomik all-or-nothing tidak menghapus record saat kegagalan server 5xx | mock | 149 |
| TC-GS-POS-E2E-029-mobile-selection-toolbar-dan-bulk-delete | Mobile: Long-press card selection mode, toolbar, menu card, dan Bulk Delete di mobile viewport | FE+BE | 151, 298, 304 |
| TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | Search tabel utama: siklus interaksi, substring, case-insensitive, trim, empty state, dan scope kolom | FE+BE | 152, 153, 154, 155, 156, 157, 158 |
| TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | Filter Panel tabel utama: rentang Last Updated inklusif, single-day, Clear, cancel, dan kolom hidden | FE+BE | 159, 160, 161, 162, 163, 164 |
| TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | Sort 3-klik Name & Last Updated, kombinasi Search + Filter + Sort, dan reset pagination | FE+BE | 165, 166, 167, 168, 169, 170, 171, 172, 173, 174 |
| TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama | Overlay Column Visibility tabel utama: uncheck instant, drag reorder, dan guard kolom terakhir | FE+BE | 177, 178, 179, 180 |
| TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | Popup Setup Column tabel utama: search, hide/unhide, drag reorder, pin, Reset to Default, dan independensi | FE+BE | 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 |
| TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | Binary Buffer: Download CSV dan XLSX tabel utama, kesesuaian query, dan pengecualian kolom tersembunyi | FE+BE | 192, 193, 194, 195, 196, 197, 198 |
| TC-GS-POS-E2E-036-resilience-download-tabel-utama-gagal | Resilience: Download tabel utama saat gagal menghasilkan toast error | mock | 199 |
| TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | Screening Popup Changelog: Position, tooltip, dismiss ✕/Esc, backdrop, hover Modified By, dan empty state | FE+BE | 200, 201, 202, 203, 204, 241, 292 |
| TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | Search Popup Changelog: siklus interaksi, pencarian lintas kolom teks, Field, Date guard, dan no-match | FE+BE | 205, 206, 207, 208, 209, 210 |
| TC-GS-POS-E2E-039-filter-panel-popup-changelog | Filter Panel Changelog: Date, multi-select (Action, Name, Modified By), chip sync, loading, dan logika AND/OR | FE+BE | 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 288, 289, 290 |
| TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | Sort 3-klik Date/teks/Modified By, pagination, Overlay Visibility, dan Setup Column Changelog (7 kolom) | FE+BE | 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236 |
| TC-GS-POS-E2E-041-download-csv-xlsx-popup-changelog | Binary Buffer: Download CSV dan XLSX Popup Changelog mengikuti filter dan kolom tampil | FE+BE | 237, 238, 239 |
| TC-GS-POS-E2E-042-resilience-download-popup-changelog-gagal | Resilience: Download Popup Changelog saat gagal menampilkan toast error | mock | 240 |
| TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | Audit Log: Pencatatan Create, Edit, Delete, Bulk Delete, snapshot, dan import omission di Changelog & Activity Log | FE+BE | 242, 243, 244, 245, 247, 248, 249, 250, 252, 253 |
| TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position | External Harness: Pencatatan mutasi Position ke System Log Tab pada Detail User aktor | FE+BE | 251, 305, 306, 307 |
| TC-GS-POS-E2E-045-absence-log-pada-edit-no-op | Asersi Absence: Edit No-Op tidak menghasilkan entri baru pada Changelog, Activity Log, maupun System Log | FE+BE | 246, 308 |
| TC-GS-POS-E2E-046-cross-module-format-tanggal-general-settings | External Harness: Kepatuhan format tanggal General Settings pada tabel, filter, changelog, dan filter date | FE+BE | 254, 255 |
| TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | External Harness: Sinkronisasi Position baru, rename, dan terhapus ke dropdown form User, Non-Login User, dan filter User List | FE+BE | 256, 257, 258, 281, 301 |
| TC-GS-POS-E2E-048-security-defense-in-depth-markup-xss-rendering | Defense-in-depth: Input Position Name berisi markup HTML/XSS dirender sebagai teks murni tanpa eksekusi | FE+BE | 266 |
| TC-GS-POS-E2E-049-security-isolasi-entitas-multi-tenant | State Tenant: Isolasi entitas — Position milik Client Lain tidak terlihat di tabel entitas aktif | FE+BE | 267 |
| TC-GS-POS-E2E-050-multi-konteks-konkurensi-dua-admin-create-dan-limit | Multi-Konteks: Create bersamaan nama yang sama dan create bersamaan pada slot limit terakhir oleh 2 admin | FE+BE | 269, 270 |
| TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | Multi-Konteks: Edit bersamaan record sama (last-write-wins), delete race, dan bulk delete race antar 2 admin | FE+BE | 109, 118, 119, 147, 148, 271, 300 |
| TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | Multi-Konteks: Record baru dan record terhapus dari sesi lain sinkron realtime tanpa reload, serta isolasi modal Edit | FE+BE | 175, 176, 278, 279, 297 |
| TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix | State Tenant: Write-lockdown pada entitas Suspended/Expired (Create, Edit, Delete ditolak) dan independensi plan | FE+BE | 268, 272, 273, 274 |
| TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing | Lifecycle & Parity: Position hasil Import Type Position (Edit, Delete in-use guard, Delete sukses) dan Create Missing Positions | FE+BE | 275, 276, 277, 295 |

---

## 2. TC Hanya-BE (Tidak Masuk Spec E2E)

Enam TC bertanda `FE Test: -` dan `PIC FE: -` di `tc-position.md` (Section 8). Kasus ini adalah validasi kontrak API dan penegakan server-side murni yang tidak terjangkau oleh UI/browser, sehingga didelegasikan ke pengujian integrasi di repo backend.

| TC ID | Section | Alasan Tidak Masuk Spec E2E |
|---|:---:|---|
| TC-GS-POS-260 | 8 | Penolakan direct API POST /positions tanpa capability dengan 403 Forbidden (Read-Only). Diuji lewat integration test backend. |
| TC-GS-POS-261 | 8 | Penolakan direct API PUT/PATCH /positions/:id tanpa capability dengan 403 Forbidden (Create-Only). Diuji lewat integration test backend. |
| TC-GS-POS-262 | 8 | Penolakan direct API DELETE /positions/:id tanpa capability dengan 403 Forbidden (Update-Only). Diuji lewat integration test backend. |
| TC-GS-POS-263 | 8 | Penolakan direct API POST /positions tanpa capability dengan 403 Forbidden (Read Only role). Diuji lewat integration test backend. |
| TC-GS-POS-264 | 8 | Penegakan guard in-use tetap ditegakkan oleh server pada direct API call DELETE. Diuji lewat integration test backend. |
| TC-GS-POS-265 | 8 | Penolakan duplikat nama tetap ditegakkan oleh server pada direct API call POST/PUT. Diuji lewat integration test backend. |

---

## 3. Sebaran per Section TC

| Section | Jumlah TC | Masuk Spec E2E | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Table List Flow | 27 | 27 | 0 |
| 2. Role & Capability Access Flow | 12 | 12 | 0 |
| 3a. Create Flow | 40 | 40 | 0 |
| 3b. Edit Flow | 42 | 42 | 0 |
| 3c. Delete Flow (Single) | 13 | 13 | 0 |
| 3d. Bulk Delete Flow | 34 | 34 | 0 |
| 4a. Tabel Utama — Search, Filter, Sort, Setup Kolom, Download | 48 | 48 | 0 |
| 4b. Popup Changelog: Position | 46 | 46 | 0 |
| 5. Pencatatan Audit Log | 16 | 16 | 0 |
| 7. Cross-Module Sync & Foundation Cascading | 8 | 8 | 0 |
| 8. Security & Defense-in-Depth | 8 | 2 | 6 |
| 9. Edge Case Matrix & Concurrency Sisa | 14 | 14 | 0 |
| **Total** | **308** | **302** | **6** |

---

## 4. Lapisan per TC (308 Baris)

| TC ID | Skenario | Spec E2E | Mode |
|---|---|---|:---:|
| TC-GS-POS-1 | Screening halaman Position — 3 zona tabel utama | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-2 | Breadcrumb halaman Position — teks dan segmen terminal | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-3 | Breadcrumb halaman Position — segmen User tidak bisa diklik | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-4 | Tooltip ikon Table Tools dan header Column Visibility tabel utama | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-5 | Urutan default tabel Position — Name A-Z case-insensitive | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-6 | Loading state saat data tabel Position sedang dimuat | TC-GS-POS-E2E-003-resilience-loading-state-dan-error-try-again | mock |
| TC-GS-POS-7 | Empty state tabel Position — entitas belum punya jabatan | TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | FE+BE |
| TC-GS-POS-8 | Error load tabel Position dan pemulihan via Try Again | TC-GS-POS-E2E-003-resilience-loading-state-dan-error-try-again | mock |
| TC-GS-POS-9 | Nama Position 120 karakter tampil utuh di tabel | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-10 | Pagination default 10 baris dan navigasi halaman | TC-GS-POS-E2E-004-pagination-dan-page-size-tabel-utama | FE+BE |
| TC-GS-POS-11 | Pilihan ukuran halaman 10/25/50/100 tabel Position | TC-GS-POS-E2E-004-pagination-dan-page-size-tabel-utama | FE+BE |
| TC-GS-POS-12 | Input nomor halaman langsung + Enter | TC-GS-POS-E2E-004-pagination-dan-page-size-tabel-utama | FE+BE |
| TC-GS-POS-13 | Refresh F5 mempertahankan Search, Sort, Filter, halaman, dan ukuran halaman | TC-GS-POS-E2E-005-persistensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-14 | Klik ulang menu sidebar User mereset kondisi List Position | TC-GS-POS-E2E-005-persistensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-15 | Pindah sub-tab User List lalu kembali ke Position — status Search/Filter/Sort/halaman | TC-GS-POS-E2E-005-persistensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-16 | Guided Tooltip muncul otomatis pada kunjungan pertama | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-17 | Guided Tooltip — navigasi Next/Back dan konten tiap step | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-18 | Guided Tooltip — Done menutup dan tidak muncul otomatis lagi | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-19 | Guided Tooltip — Skip via tombol menutup dan menandai seen | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-20 | Guided Tooltip — klik overlay gelap setara Skip | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-21 | Guided Tooltip — replay via tombol [?] | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-22 | Guided Tooltip — resize viewport di tengah walkthrough tidak menandai seen | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-23 | Accessibility Guided Tooltip — navigasi keyboard | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-24 | Guided Tooltip identik untuk aktor Read Only | TC-GS-POS-E2E-006-guided-tooltip-walkthrough-dan-interaksi | FE+BE |
| TC-GS-POS-291 | Last Updated terisi untuk record seed dan hasil Import | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-293 | State visual komponen tabel dan form Position | TC-GS-POS-E2E-001-screening-tabel-position-layout-dan-default-sort | FE+BE |
| TC-GS-POS-296 | Entitas diprovisioning tanpa Position Default User memulai katalog kosong | TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | FE+BE |
| TC-GS-POS-25 | Visibilitas elemen tab Position — System Role tanpa capability Manage user and role | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-26 | Visibilitas elemen tab Position — System Role dengan capability Manage user and role R saja | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-27 | Visibilitas elemen tab Position — System Role dengan capability C+R | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-28 | Visibilitas elemen tab Position — System Role dengan capability U+R | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-29 | Visibilitas elemen tab Position — System Role dengan capability D+R | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-30 | Visibilitas elemen tab Position — Total Control | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-31 | Visibilitas elemen tab Position — Read Only (Access Level) | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-32 | Create Position oleh aktor capability Create saja | TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete | FE+BE |
| TC-GS-POS-33 | Edit Position oleh aktor capability Update saja | TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete | FE+BE |
| TC-GS-POS-34 | Delete single Position oleh aktor capability Delete saja | TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete | FE+BE |
| TC-GS-POS-35 | Bulk Delete Position oleh aktor capability Delete saja | TC-GS-POS-E2E-008-role-matrix-positif-create-edit-delete | FE+BE |
| TC-GS-POS-36 | Akses langsung URL tab Position oleh aktor tanpa capability | TC-GS-POS-E2E-007-role-matrix-visibilitas-tab-dan-kontrol | FE+BE |
| TC-GS-POS-37 | Screening Popup Create Position — 3 zona | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-38 | Accessibility Popup Create Position — aria-required, aria-describedby, dan focus trap | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-39 | Create — Position Name kosong saat Submit | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-40 | Create — Position Name hanya berisi spasi saat Submit | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-41 | Create — Position Name tepat 120 karakter diterima | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-42 | Create — Position Name 121 karakter memunculkan error langsung | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-43 | Create — batas 120 karakter dihitung sebelum trim | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-44 | Create — mengetik emoji pada Position Name | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-45 | Create — paste teks berisi emoji pada Position Name | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-46 | Create — emoji lolos filter FE ditolak server | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-47 | Create — nama duplikat case-insensitive terdeteksi saat mengetik | TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-48 | Create — nama duplikat dengan spasi depan/belakang tetap terdeteksi | TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-49 | Create — error duplikat hilang setelah nama diubah menjadi unik | TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-50 | Create — Clear Field mengosongkan form tanpa menutup | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-51 | Create Position — Stay tidak dicentang | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-52 | Create Position — Stay dicentang untuk input berulang | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-53 | Populasi data uji Position via Stay on this form | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-54 | Create — spasi depan/belakang dibuang saat disimpan | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-55 | Create — tutup via [✕] saat form bersih | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-56 | Create — tutup via Esc saat form bersih | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-57 | Create — tutup via [✕] saat form terisi memunculkan Dialog Unsaved Changes | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-58 | Create — Cancel pada Dialog Unsaved Changes | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-59 | Create — Leave pada Dialog Unsaved Changes | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-60 | Create — Esc saat form terisi memunculkan Dialog Unsaved Changes | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-61 | Create — klik backdrop saat form terisi | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-62 | Create — reload tab saat form terisi memunculkan konfirmasi browser | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-63 | Create — reload tab saat form bersih tanpa konfirmasi browser | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-64 | Create — pindah menu in-app saat form terisi | TC-GS-POS-E2E-011-create-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-65 | Create — Saving state saat Submit diproses | TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-66 | Create — klik ganda Submit hanya membuat 1 record | TC-GS-POS-E2E-010-create-position-validasi-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-67 | Create — kegagalan server 5xx mempertahankan form | TC-GS-POS-E2E-013-resilience-create-position-kegagalan-server | mock |
| TC-GS-POS-68 | Create — timeout jaringan saat Submit | TC-GS-POS-E2E-013-resilience-create-position-kegagalan-server | mock |
| TC-GS-POS-69 | Klik [+ Position] saat Master Data Count Limit tercapai | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-70 | Dialog Limit Reached — tombol OK | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-71 | Submit Create ditolak karena limit tercapai setelah popup dibuka | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-72 | Create berulang dengan Stay hingga menyentuh Master Data Count Limit | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-73 | Create pertama dari empty state mengembalikan tabel | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-282 | Create — Position Name 1 karakter diterima | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-284 | Create — feedback hover tombol Submit dan Clear Field | TC-GS-POS-E2E-009-create-position-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-286 | Create — record tetap ada setelah refresh | TC-GS-POS-E2E-012-create-position-happy-path-stay-form-dan-populasi-data | FE+BE |
| TC-GS-POS-74 | Screening Overlay Row Action pada baris Position | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-75 | Screening Popup Edit Position — 3 zona | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-76 | Accessibility Popup Edit Position — aria-required, aria-describedby, dan focus trap | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-77 | Edit — Position Name dikosongkan saat Save | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-78 | Edit — Position Name hanya spasi saat Save | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-79 | Edit — Position Name tepat 120 karakter diterima | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-80 | Edit — Position Name 121 karakter memunculkan error langsung | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-81 | Edit — batas 120 karakter dihitung sebelum trim | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-82 | Edit — mengetik emoji pada Position Name | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-83 | Edit — paste teks berisi emoji pada Position Name | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-84 | Edit — emoji lolos filter FE ditolak server | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-85 | Edit — nama duplikat case-insensitive terdeteksi saat mengetik | TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-86 | Edit — nama duplikat dengan spasi depan/belakang ditolak saat Save | TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-87 | Edit — nama sendiri tidak dianggap duplikat | TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-88 | Edit — Clear Field mengosongkan field, bukan revert | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-89 | Edit Position — ganti nama | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-90 | Edit — perubahan kapitalisasi saja dihitung perubahan | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-91 | Edit — Save tanpa perubahan nilai (No-Op) | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-92 | Edit — hanya menambah spasi depan/belakang dihitung No-Op | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-93 | Edit — tutup via [✕] tanpa perubahan | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-94 | Edit — tutup via Esc tanpa perubahan | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-95 | Edit — tutup via [✕] setelah nilai diubah memunculkan Dialog Unsaved Changes | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-96 | Edit — Esc setelah nilai diubah memunculkan Dialog Unsaved Changes | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-97 | Edit — Cancel pada Dialog Unsaved Changes | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-98 | Edit — Leave pada Dialog Unsaved Changes | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-99 | Edit — nilai diubah lalu dikembalikan identik tidak dianggap dirty | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-100 | Edit — tutup setelah Clear Field memunculkan Dialog Unsaved Changes | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-101 | Edit — klik backdrop saat nilai diubah | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-102 | Edit — reload tab saat nilai diubah memunculkan konfirmasi browser | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-103 | Edit — pindah menu in-app saat nilai diubah | TC-GS-POS-E2E-017-edit-position-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-104 | Edit — Saving state saat Save diproses | TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-105 | Edit — klik ganda Save hanya diproses sekali | TC-GS-POS-E2E-016-edit-position-validasi-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-106 | Edit — kegagalan server 5xx mempertahankan form | TC-GS-POS-E2E-019-resilience-edit-position-kegagalan-server | mock |
| TC-GS-POS-107 | Edit — timeout jaringan saat Save | TC-GS-POS-E2E-019-resilience-edit-position-kegagalan-server | mock |
| TC-GS-POS-108 | Edit — retry setelah timeout yang ternyata sudah tersimpan diperlakukan No-Op | TC-GS-POS-E2E-019-resilience-edit-position-kegagalan-server | mock |
| TC-GS-POS-109 | Edit — record sudah dihapus admin lain saat Save | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-110 | Edit record Position hasil seed provisioning entitas | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-283 | Edit — Position Name 1 karakter diterima | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-285 | Edit — feedback hover tombol Save dan Clear Field | TC-GS-POS-E2E-015-edit-position-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-287 | Row action Edit/Delete sama untuk record seed dan record biasa | TC-GS-POS-E2E-018-edit-position-happy-path-no-op-dan-seed-record | FE+BE |
| TC-GS-POS-294 | Save Edit setelah capability Update dicabut di tengah sesi | TC-GS-POS-E2E-020-security-edit-position-pencabutan-capability-di-tengah-sesi | FE+BE |
| TC-GS-POS-297 | Popup Edit yang terbuka tidak di-refresh oleh rename dari sesi lain | TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | FE+BE |
| TC-GS-POS-111 | Screening Dialog Delete Position untuk jabatan bebas relasi | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-112 | Delete single — Cancel pada Dialog Delete Position | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-113 | Delete single Position bebas relasi | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-114 | Delete single — jabatan dipakai user Login diblokir | TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use | FE+BE |
| TC-GS-POS-115 | Dialog Cannot Delete Data — tombol OK | TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use | FE+BE |
| TC-GS-POS-116 | Delete single — jabatan dipakai user Non-Login diblokir | TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use | FE+BE |
| TC-GS-POS-117 | Delete single — jabatan hanya dipakai user non-aktif | TC-GS-POS-E2E-022-delete-single-position-diblokir-karena-in-use | FE+BE |
| TC-GS-POS-118 | Delete single — jabatan menjadi in-use di antara buka dialog dan Confirm | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-119 | Delete single — record sudah dihapus admin lain sebelum Confirm | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-120 | Delete single — klik ganda Delete hanya diproses sekali | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-121 | Delete single — kegagalan server 5xx | TC-GS-POS-E2E-023-resilience-delete-single-kegagalan-server | mock |
| TC-GS-POS-122 | Delete satu-satunya Position di entitas diizinkan | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-299 | Accessibility dialog Delete — focus trap dan Esc | TC-GS-POS-E2E-021-delete-single-position-happy-path-dan-satu-satunya-jabatan | FE+BE |
| TC-GS-POS-123 | Populasi data uji Bulk Delete via Stay on this form | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-124 | Screening Bulk Action Bar saat 1 baris dicentang | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-125 | Counter Bulk Action Bar singular/plural realtime | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-126 | Icon ✕ pada Bulk Action Bar membatalkan seluruh seleksi | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-127 | Checkbox header memilih dan membatalkan seluruh baris halaman aktif | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-128 | Checkbox header indeterminate saat sebagian baris dicentang | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-129 | Select All (N records) memilih seluruh baris lintas halaman | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-130 | Centang manual seluruh baris hingga 100% mengubah tombol menjadi Unselect All | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-131 | Unselect All membatalkan seluruh seleksi lintas halaman | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-132 | Uncheck 1 baris dari kondisi 100% terpilih | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-133 | Seleksi dipertahankan saat pindah halaman, Search, Filter, dan Sort | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-134 | Bulk Delete berlaku untuk seluruh seleksi termasuk yang tidak tampil karena filter | TC-GS-POS-E2E-024-bulk-action-bar-protokol-seleksi-dan-retensi | FE+BE |
| TC-GS-POS-135 | Selection Limit — checkbox ke-(limit+1) disabled saat seleksi manual | TC-GS-POS-E2E-025-selection-limit-bulk-checkbox-dan-select-all | FE+BE |
| TC-GS-POS-136 | Selection Limit — Select All dibatasi otomatis ke limit | TC-GS-POS-E2E-025-selection-limit-bulk-checkbox-dan-select-all | FE+BE |
| TC-GS-POS-137 | Bulk Delete 1 jabatan bebas relasi memakai dialog single | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-138 | Bulk Delete 1 jabatan in-use memakai dialog blokir single | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-139 | Screening Dialog Delete Position — seluruh terpilih bebas relasi | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-140 | Bulk Delete homogen — Cancel mempertahankan seleksi | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-141 | Bulk Delete homogen — Delete | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-142 | Screening Dialog Delete Position campuran (sebagian in-use) | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-143 | Bulk Delete campuran — Cancel mempertahankan seleksi | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-144 | Bulk Delete campuran — Continue | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-145 | Bulk Delete — seluruh terpilih in-use diblokir | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-146 | Daftar nama di Dialog Delete Position tidak diringkas | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-302 | Daftar nama di Dialog Cannot Delete Data (bulk) tidak diringkas | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-303 | Daftar nama di Dialog Delete Position campuran tidak diringkas | TC-GS-POS-E2E-027-bulk-delete-campuran-dan-seluruhnya-in-use-diblokir | FE+BE |
| TC-GS-POS-147 | Bulk Delete — item menjadi in-use di antara buka dialog dan Confirm | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-300 | Bulk Delete — seluruh item menjadi in-use di antara buka dialog dan Confirm | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-148 | Bulk Delete — item sudah dihapus admin lain sebelum Confirm | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-149 | Bulk Delete — kegagalan server 5xx | TC-GS-POS-E2E-028-resilience-bulk-delete-atomik-pada-kegagalan-server | mock |
| TC-GS-POS-150 | Bulk Delete — klik ganda Delete hanya diproses sekali | TC-GS-POS-E2E-026-bulk-delete-homogen-dan-single-dialog-collapse | FE+BE |
| TC-GS-POS-151 | Mobile — long-press card masuk selection mode dan Bulk Delete | TC-GS-POS-E2E-029-mobile-selection-toolbar-dan-bulk-delete | FE+BE |
| TC-GS-POS-298 | Mobile — aturan kolom dan menu card yang berbeda dari web | TC-GS-POS-E2E-029-mobile-selection-toolbar-dan-bulk-delete | FE+BE |
| TC-GS-POS-304 | Mobile — screening toolbar dan tombol [+ Position] | TC-GS-POS-E2E-029-mobile-selection-toolbar-dan-bulk-delete | FE+BE |
| TC-GS-POS-152 | Siklus interaksi Search toolbar tabel utama | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-153 | Search Name — potongan kata (substring) | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-154 | Search Name — tidak case-sensitive | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-155 | Search — spasi depan/belakang keyword diabaikan | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-156 | Search tanpa hasil menampilkan empty state hasil pencarian | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-157 | Search tidak mencari kolom Last Updated | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-158 | Search terikat visibilitas kolom Name | TC-GS-POS-E2E-030-search-tabel-utama-interaksi-dan-empty-state | FE+BE |
| TC-GS-POS-159 | Screening Filter Panel tabel utama | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-160 | Filter Last Updated rentang tanggal inklusif | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-161 | Filter Last Updated satu hari (Start = End) | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-162 | Clear Field Filter Panel mengembalikan seluruh data | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-163 | Menutup Filter Panel tanpa Apply membuang perubahan | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-164 | Filter tetap berlaku saat kolom Last Updated disembunyikan | TC-GS-POS-E2E-031-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-165 | Search lalu Filter menghasilkan irisan | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-166 | Filter lalu Search menghasilkan irisan yang sama | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-167 | Sort Name — siklus 3 klik | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-168 | Sort Last Updated — siklus 3 klik | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-169 | Pindah kolom sort mereset kolom sebelumnya | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-170 | Kombinasi Search + Filter + Sort + ukuran halaman | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-171 | Clear Filter saat Search dan Sort aktif | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-172 | Clear Search saat Filter dan Sort aktif | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-173 | Pemulihan dari empty state kombinasi Search + Filter | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-174 | Search dan Apply Filter mereset pagination ke halaman 1 | TC-GS-POS-E2E-032-kombinasi-search-filter-sort-dan-pagination-reset | FE+BE |
| TC-GS-POS-175 | Record baru dari sesi lain yang tidak cocok Search tidak muncul di tabel tersaring | TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | FE+BE |
| TC-GS-POS-176 | Rename yang tidak lagi cocok Search menghilangkan baris dari tampilan | TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | FE+BE |
| TC-GS-POS-177 | Screening Overlay Column Visibility tabel utama | TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-178 | Overlay Column Visibility — uncheck kolom langsung diterapkan | TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-179 | Overlay Column Visibility — drag reorder langsung diterapkan | TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-180 | Overlay Column Visibility — kolom terakhir yang tampil tidak bisa di-uncheck | TC-GS-POS-E2E-033-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-181 | Screening Popup Setup Column tabel utama | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-182 | Popup Setup Column — footer tanpa tombol Cancel | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-183 | Popup Setup Column — search nama kolom | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-184 | Popup Setup Column — hide/unhide kolom kelas Hideable (Name, Last Updated) | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-185 | Popup Setup Column — drag reorder kelas Hideable | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-186 | Popup Setup Column — pin kolom kelas Hideable | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-187 | Popup Setup Column — Reset to Default | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-188 | Popup Setup Column — tutup via ✕ atau Esc membuang perubahan | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-189 | Popup Setup Column — kolom terakhir yang tampil tidak bisa di-uncheck | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-190 | Preferensi kolom tabel utama tidak memengaruhi Popup Changelog | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-191 | Preferensi kolom Popup Changelog tidak memengaruhi tabel utama | TC-GS-POS-E2E-034-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-192 | Screening Overlay Download tabel utama | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-193 | Download CSV tabel utama | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-194 | Download XLSX tabel utama | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-195 | Download tanpa Search/Filter berisi seluruh baris lintas halaman | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-196 | Download mengikuti Search dan Filter aktif | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-197 | Download tidak menyertakan kolom yang disembunyikan | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-198 | Download kembali menyertakan kolom setelah ditampilkan lagi | TC-GS-POS-E2E-035-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-199 | Download gagal menampilkan toast error | TC-GS-POS-E2E-036-resilience-download-tabel-utama-gagal | mock |
| TC-GS-POS-200 | Screening Popup Changelog: Position — 3 zona | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-201 | Tooltip toolbar dan header Column Visibility Popup Changelog | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-202 | Menutup Popup Changelog via ✕ dan Esc | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-203 | Klik backdrop pada Popup Changelog | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-204 | Empty state Popup Changelog — belum ada riwayat | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-205 | Search Popup Changelog tanpa hasil | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-206 | Siklus interaksi Search Popup Changelog | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-207 | Search Popup Changelog — kelas kolom teks (Action, Position Name, Old Value, New Value, Modified By) | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-208 | Search Popup Changelog — kolom Field | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-209 | Search Popup Changelog tidak mencari kolom Date | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-210 | Search Popup Changelog terikat visibilitas kolom | TC-GS-POS-E2E-038-search-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-211 | Screening Filter Panel Popup Changelog | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-212 | Isi opsi dropdown filter Popup Changelog berasal dari entri log | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-213 | Filter Date Popup Changelog | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-214 | Filter dropdown kelas multi-select (Action, Position Name, Modified By) — search internal dan OR | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-215 | Hapus chip filter via ✕ menyinkronkan checkbox opsi | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-216 | Uncheck opsi di dalam dropdown menghapus chip | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-217 | Overflow chip filter Position Name | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-218 | Dropdown filter Popup Changelog tanpa sumber data | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-219 | Kombinasi field filter berbeda memakai logika AND | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-220 | Search dan Filter Popup Changelog dalam dua urutan menghasilkan irisan sama | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-221 | Sort Date Popup Changelog — siklus 3 klik | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-222 | Sort Popup Changelog — kelas alfabetis (Action, Position Name, Field) | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-223 | Sort Popup Changelog — kelas campuran (Old Value, New Value) dengan nilai kosong | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-224 | Sort Modified By berdasarkan nama lengkap | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-225 | Kombinasi Search + Filter + Sort + pagination Popup Changelog | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-226 | Clear Filter dan Clear Search Popup Changelog saling independen | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-227 | Pemulihan empty state Popup Changelog | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-228 | Pagination Popup Changelog | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-229 | Screening Overlay Column Visibility Popup Changelog | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-230 | Screening Popup Setup Column dari Popup Changelog | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-231 | Popup Setup Column Changelog — hide/unhide kelas Hideable (7 kolom) | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-232 | Popup Setup Column Changelog — drag reorder kelas Hideable | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-233 | Popup Setup Column Changelog — pin kelas Hideable dan batas 3 pin | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-234 | Popup Setup Column Changelog — Reset to Default | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-235 | Popup Setup Column Changelog — ✕ membuang perubahan | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-236 | Popup Setup Column Changelog — kolom terakhir tidak bisa di-uncheck | TC-GS-POS-E2E-040-sort-pagination-dan-setup-kolom-changelog | FE+BE |
| TC-GS-POS-237 | Download CSV Popup Changelog | TC-GS-POS-E2E-041-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-238 | Download XLSX Popup Changelog | TC-GS-POS-E2E-041-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-239 | Download Popup Changelog mengikuti filter dan kolom tampil | TC-GS-POS-E2E-041-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-240 | Download Popup Changelog gagal | TC-GS-POS-E2E-042-resilience-download-popup-changelog-gagal | mock |
| TC-GS-POS-241 | Hover Modified By menampilkan nama lengkap | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-288 | Opsi filter Position Name Changelog bertambah setelah Create baru | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-289 | Loading state dropdown filter Changelog saat opsi dimuat | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-290 | Filter Position Name aktif tetap aman setelah Position-nya dihapus | TC-GS-POS-E2E-039-filter-panel-popup-changelog | FE+BE |
| TC-GS-POS-292 | Tampilan Modified By nama depan panjang dan nama satu kata | TC-GS-POS-E2E-037-screening-popup-changelog-dan-empty-state | FE+BE |
| TC-GS-POS-242 | Changelog dan Activity Log — entri Create Position | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-243 | Changelog dan Activity Log — entri Edit Position | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-244 | Changelog dan Activity Log — entri Delete Position | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-245 | Changelog — Bulk Delete campuran mencatat hanya item yang terhapus | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-246 | Edit No-Op tidak menghasilkan entri log | TC-GS-POS-E2E-045-absence-log-pada-edit-no-op | FE+BE |
| TC-GS-POS-247 | Snapshot entri Changelog tidak berubah setelah rename kedua | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-248 | Changelog — perubahan kapitalisasi tercatat sebagai Edit | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-249 | Position hasil Import Type "Position" tidak tercatat di Changelog modul | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-250 | Position dari [Create Missing Positions] tercatat sebagai Create biasa | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-251 | System Log aktor — entri Create Position | TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position | FE+BE |
| TC-GS-POS-252 | Nilai kolom Field pada entri log Position | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-253 | Isi kolom Position Name pada entri Edit | TC-GS-POS-E2E-043-pencatatan-changelog-dan-activity-log-mutasi-position | FE+BE |
| TC-GS-POS-305 | System Log aktor — entri Edit Position | TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position | FE+BE |
| TC-GS-POS-306 | System Log aktor — entri Delete Position | TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position | FE+BE |
| TC-GS-POS-307 | System Log aktor — Bulk Delete satu entri per item yang terhapus | TC-GS-POS-E2E-044-pencatatan-system-log-aktor-mutasi-position | FE+BE |
| TC-GS-POS-308 | Edit No-Op tidak menghasilkan entri System Log aktor | TC-GS-POS-E2E-045-absence-log-pada-edit-no-op | FE+BE |
| TC-GS-POS-254 | Format tanggal General Settings pada tabel utama dan Filter Panel | TC-GS-POS-E2E-046-cross-module-format-tanggal-general-settings | FE+BE |
| TC-GS-POS-255 | Format tanggal General Settings pada Popup Changelog dan Filter Date | TC-GS-POS-E2E-046-cross-module-format-tanggal-general-settings | FE+BE |
| TC-GS-POS-256 | Position baru tersedia di dropdown Position form User dan Non-Login User | TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | FE+BE |
| TC-GS-POS-257 | Rename Position tercermin di dropdown dan data user yang memakainya | TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | FE+BE |
| TC-GS-POS-258 | Position terhapus hilang dari dropdown form User dan Non-Login User | TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | FE+BE |
| TC-GS-POS-259 | Perubahan Master Data Count Limit dibaca langsung tanpa hardcode | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-281 | Form User yang memilih Position yang baru dihapus ditolak dengan error field-level | TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | FE+BE |
| TC-GS-POS-301 | Rename Position tercermin di opsi Filter Position tabel User List | TC-GS-POS-E2E-047-cross-module-sinkronisasi-dropdown-form-user | FE+BE |
| TC-GS-POS-260 | Defense-in-depth — Create langsung tanpa capability ditolak (Manage user and role — Read-Only) | Hanya-BE | - |
| TC-GS-POS-261 | Defense-in-depth — Edit langsung tanpa capability ditolak (Manage user and role — Create-Only) | Hanya-BE | - |
| TC-GS-POS-262 | Defense-in-depth — Delete langsung tanpa capability ditolak (Manage user and role — Update-Only) | Hanya-BE | - |
| TC-GS-POS-263 | Defense-in-depth — Create langsung tanpa capability ditolak (Read Only) | Hanya-BE | - |
| TC-GS-POS-264 | Defense-in-depth — guard in-use tetap ditegakkan server | Hanya-BE | - |
| TC-GS-POS-265 | Defense-in-depth — duplikat nama ditolak server | Hanya-BE | - |
| TC-GS-POS-266 | Nama berisi markup dirender sebagai teks | TC-GS-POS-E2E-048-security-defense-in-depth-markup-xss-rendering | FE+BE |
| TC-GS-POS-267 | Isolasi entitas — Position entitas lain tidak terlihat | TC-GS-POS-E2E-049-security-isolasi-entitas-multi-tenant | FE+BE |
| TC-GS-POS-268 | Tidak ada plan gating — perilaku identik di semua plan | TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix | FE+BE |
| TC-GS-POS-269 | Create bersamaan dengan nama sama oleh 2 admin | TC-GS-POS-E2E-050-multi-konteks-konkurensi-dua-admin-create-dan-limit | FE+BE |
| TC-GS-POS-270 | Create bersamaan pada slot Master Data Count Limit terakhir | TC-GS-POS-E2E-050-multi-konteks-konkurensi-dua-admin-create-dan-limit | FE+BE |
| TC-GS-POS-271 | Edit bersamaan record yang sama — last-write-wins | TC-GS-POS-E2E-051-multi-konteks-konkurensi-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-272 | Entitas suspended/expired — Create ditolak | TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix | FE+BE |
| TC-GS-POS-273 | Entitas suspended/expired — Edit ditolak | TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix | FE+BE |
| TC-GS-POS-274 | Entitas suspended/expired — Delete ditolak | TC-GS-POS-E2E-053-state-tenant-write-lockdown-entitas-suspended-expired-dan-plan-matrix | FE+BE |
| TC-GS-POS-275 | Position hasil Import Type "Position" bisa di-Edit identik record manual | TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-276 | Position hasil Import yang dipakai user tetap diblokir saat Delete | TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-277 | Position hasil Import yang bebas relasi bisa dihapus | TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-278 | Record baru dari sesi lain muncul tanpa reload | TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | FE+BE |
| TC-GS-POS-279 | Record yang dihapus dari sesi lain hilang tanpa reload | TC-GS-POS-E2E-052-multi-konteks-realtime-sync-tabel-dan-filter-tanpa-reload | FE+BE |
| TC-GS-POS-280 | [Create Missing Positions] dihitung terhadap Master Data Count Limit | TC-GS-POS-E2E-014-master-data-count-limit-create-guard | FE+BE |
| TC-GS-POS-295 | [Create Missing Positions] untuk nama yang sudah ada ditolak sebagai duplikat | TC-GS-POS-E2E-054-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
