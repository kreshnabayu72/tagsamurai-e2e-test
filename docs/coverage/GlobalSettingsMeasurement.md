# Coverage E2E — Global Settings > Master Reference > Measurement

Sumber: `global-settings/measurement/TestCases/tc-measurement.md` (379 baris TC `TC-GS-UOM-1`–`415`; 36 nomor tidak dipakai). Suite: `specs/GlobalSettings/Measurement/`. Prefix: `GS` + `UOM` (`TC-GS-UOM-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 364 TC masuk spec, 15 TC hanya-BE dilewati (kontrak API murni; padanannya di `tc-measurement-backend.md`). 75 spec. Setiap TC terpetakan ke satu spec, kecuali TC-220 dan TC-267 yang sengaja terbelah (prinsip 10): bagian presence di spec 064, bagian absence (tidak ada entri `Box`) di spec 065.

Nomor TC tidak dipakai: 6, 128, 129, 135, 136, 137, 138, 139, 150, 201, 208, 209, 210, 211, 283, 287, 288, 289, 290, 291, 292, 294, 296, 300, 301, 325, 326, 331, 341, 342, 346, 355, 358, 359, 360, 361.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | Screening Tab Measurement: Layout, Tab Default, Tooltip Table Tools, Sticky Kolom, Katalog Flat | FE+BE | 38 | 2, 1, 249, 4, 15 |
| TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | Isi Sel Tabel: Used By (Items) sebagai Link, Hover/Fokus Link Unit Name dan Angka, Pembukaan Unit Detail | FE+BE | 58 | 367, 282, 396, 371, 8, 372 |
| TC-GS-UOM-E2E-003-used-by-items-read-only-akses-detail | Read Only Mengakses Unit Detail lewat Link Nama dan Angka Used By (Items) | FE+BE | 17 | 373, 207 |
| TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance | Used By (Items) = Total Item pada Instance Client, Principal, dan Distributor | FE+BE | 27 | 368, 369, 370 |
| TC-GS-UOM-E2E-005-used-by-items-fixture-khusus-nama-sama-dan-angka-besar | Used By (Items): Item Type Nama Sama di FAMS dan Supply (Tote) dan Angka Besar 1250 (Mass) | FE+BE | 21 | 374, 375 |
| TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | Format Tanggal dan Waktu General Settings pada Tabel, Filter Date, dan Changelog | FE+BE | 38 | 7, 234, 328, 327, 329 |
| TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | Empty State Tabel Measurement dan Modal Changelog | FE+BE | 27 | 11, 12, 175, 10, 174 |
| TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | Resilience Baca: Loading, Error Load, dan Try Again pada Tabel, Changelog, dan Unit Detail | FE+BE | 41 | 9, 13, 14, 305, 362 |
| TC-GS-UOM-E2E-009-resilience-export-gagal-download | Resilience Export: Kegagalan Download Tabel, Changelog, dan Item Types | FE+BE | 23 | 169, 189, 196 |
| TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard | Konten, Navigasi Keyboard, dan Step 1 Dilewati pada Guided Tooltip Tab Measurement | mock | 34 | 16, 21, 22 |
| TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | Flag Seen dan Dismiss Guided Tooltip: Skip, Overlay, Tombol [?], Resize, Navigasi Halaman | FE+BE | 43 | 17, 18, 19, 20, 334 |
| TC-GS-UOM-E2E-012-retensi-state-search-halaman-dan-refresh | Retensi State Tab Measurement: Pindah Tab Brand, Search, Sort, Filter, Halaman, dan F5 | FE+BE | 24 | 3, 156 |
| TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Measurement per Role | FE+BE | 80 | 24, 25, 26, 27, 28, 29 |
| TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability | Role Matrix Negatif: Tanpa Capability dan Satu Capability Men-gate Brand serta Measurement | FE+BE | 19 | 23, 30, 31 |
| TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability | FE+BE | 29 | 32, 33, 34, 35 |
| TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan | Capability Dicabut Saat Form atau Dialog Terbuka: Create, Edit, Delete Ditolak | FE+BE | 42 | 397, 92, 260 |
| TC-GS-UOM-E2E-017-create-population-12-unit-stay-checked | Create 12 Unit Berurutan dengan Stay on this form Dicentang (Population) | FE+BE | 13 | 36 |
| TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih | Screening Popup Create Unit, Focus Trap, Clear Field, dan Tutup Form Kosong | mock | 32 | 37, 38, 54, 57 |
| TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | Dialog Unsaved Changes pada Popup Create Unit | mock | 27 | 58, 59, 60, 61, 62 |
| TC-GS-UOM-E2E-020-create-validasi-diblokir | Validasi Create Unit yang Diblokir: Kosong, Spasi, Batas, Emoji, Duplikat, dan Aksesibilitas Error | FE+BE | 61 | 39, 40, 43, 44, 46, 47, 48, 51, 52, 335 |
| TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | Create Unit Berhasil: Batas Karakter, Trim, Karakter Khusus, Symbol Duplikat, Perilaku Submit, dan Toast Beruntun | FE+BE | 60 | 41, 42, 45, 50, 53, 55, 56, 340 |
| TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog | Master Data Count Limit: Create di Batas, Dialog Cannot Add Unit, dan Form Tetap Terbuka | FE+BE | 42 | 63, 64, 65, 66 |
| TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | Resilience Tulis: Create dan Edit Gagal 5xx, Timeout lalu Try Again, dan Cek Keunikan Gagal | FE+BE | 68 | 49, 67, 68, 89, 90, 343, 352 |
| TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert | Screening Popup Edit Unit, Clear Field Tanpa Revert, dan Tutup Tanpa Perubahan | mock | 19 | 69, 84, 85 |
| TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog | Dialog Unsaved Changes pada Popup Edit Unit | mock | 22 | 86, 87, 273 |
| TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | Validasi Edit yang Diblokir dan Nama Milik Sendiri | FE+BE | 38 | 76, 77, 78, 80, 81, 82, 263, 336 |
| TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | Edit Sukses, No-Op, Case-Only, Saving State, dan Klik Ganda Save | FE+BE | 78 | 70, 71, 72, 73, 74, 75, 79, 83, 88, 264 |
| TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel | Screening Row Action dan Dialog Delete Unit serta Cancel | FE+BE | 19 | 93, 94, 95, 333 |
| TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | Delete Unit Diblokir karena In-Use: FAMS, SAMS, Admin Console Principal dan Distributor, dan Breakdown | FE+BE | 35 | 97, 98, 99, 100, 101, 395 |
| TC-GS-UOM-E2E-030-delete-single-sukses-dan-urutan-default | Delete Unit Tunggal Berhasil dan Urutan Default Tabel | FE+BE | 21 | 5, 96 |
| TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | Bulk Action Bar: Screening, Checkbox Header, Select All Lintas Halaman, Unselect All, dan Retensi Seleksi | FE+BE | 67 | 109, 110, 111, 274, 275, 276, 277, 279 |
| TC-GS-UOM-E2E-032-selection-limit-100-baris | Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap | FE+BE | 26 | 112, 278 |
| TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | Dialog Bulk Delete: Homogen, Campuran, Blokir In-Use, Single, Daftar Panjang, dan Esc | FE+BE | 57 | 113, 114, 117, 119, 120, 121, 122, 258 |
| TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | Bulk Delete Berhasil: Homogen, Campuran, Seleksi Lintas Search, dan Klik Ganda | FE+BE | 43 | 115, 116, 118, 280, 281 |
| TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | Resilience Hapus: Cek Referensi Gagal, Delete Gagal, Timeout, dan Bulk Delete Gagal | FE+BE | 78 | 104, 105, 106, 107, 108, 124, 261, 262, 353, 354 |
| TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | Search Toolbar: Siklus Search, Pencocokan Unit Name dan Symbol, Kolom Hidden, dan Reset Halaman | FE+BE | 67 | 125, 126, 127, 130, 131, 132, 338, 384 |
| TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | Filter Panel: Screening, Placeholder, Last Updated, Clear Field, dan Tutup Tanpa Apply | FE+BE | 32 | 133, 134, 140, 141, 293, 378 |
| TC-GS-UOM-E2E-038-filter-used-by-items-rentang | Filter Used By (Items): Min, Max, Inklusif, Input Angka, Min > Max, dan Kombinasi dengan Last Updated | FE+BE | 54 | 379, 380, 381, 382, 383, 392 |
| TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | Kombinasi Search, Filter, Sort, dan Pagination serta Pemulihan Empty State dan Dampak Mutasi | FE+BE | 103 | 142, 143, 144, 145, 146, 147, 155, 284, 285, 286 |
| TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | Sort 3-State Unit Name, Symbol, Used By (Items), dan Last Updated | FE+BE | 44 | 148, 149, 151, 152, 376, 377 |
| TC-GS-UOM-E2E-041-pagination-default-page-size-dan-input-halaman | Pagination: Default 10 per Halaman, Ubah Page Size, dan Input Nomor Halaman | FE+BE | 19 | 153, 154, 339 |
| TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | Setup Column Tabel Measurement: Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Per User | mock | 83 | 157, 158, 162, 163, 164, 295, 385 |
| TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | Setup Column Tabel Measurement: Reorder (Modal dan Panel), Pin, dan Reset to Default | mock | 62 | 159, 160, 161, 349 |
| TC-GS-UOM-E2E-044-state-hover-fokus-backdrop-modal-dan-focus-trap | State Hover dan Fokus Komponen, Backdrop Tidak Menutup Modal, dan Focus Trap Modal Edit, Detail, Delete | FE+BE | 63 | 259, 298, 299 |
| TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | Download Tabel Measurement: Menu, Isi File CSV dan XLSX, Kolom Visible, dan Used By (Items) | FE+BE | 36 | 165, 166, 167, 168, 170, 386 |
| TC-GS-UOM-E2E-046-download-changelog-dan-item-type-list-isi-file | Download Changelog dan Item Type List: Isi dan Nama File | FE+BE | 19 | 188, 195 |
| TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | Changelog Measurement: Screening, Format Sel, Hover Modified By, Urutan Default, Tooltip, Search, dan Tutup Modal | FE+BE | 51 | 171, 172, 173, 176, 177, 186, 337 |
| TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | Changelog Measurement: Filter per Field, Opsi Dropdown, dan Logika AND/OR | FE+BE | 39 | 178, 179, 180, 181, 182 |
| TC-GS-UOM-E2E-049-changelog-filter-chip-x-uncheck-dan-overflow | Changelog Measurement: Chip Filter (X), Uncheck Opsi, dan Overflow +N more | FE+BE | 57 | 302, 303, 304 |
| TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi | Changelog Measurement: Sort, Nilai Kosong Old/New Value, Pagination, dan Kombinasi | FE+BE | 50 | 183, 184, 185, 190 |
| TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | Changelog Measurement: Setup Column Screening, Hide/Unhide, Guard Kolom Terakhir, Tutup Modal, dan Preferensi Terpisah dari Tabel Utama | mock | 56 | 187, 297, 306, 307, 311, 312 |
| TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | Changelog Measurement: Setup Column Reorder (Modal dan Panel), Pin Maksimal 3, dan Reset to Default | mock | 54 | 308, 309, 310, 350 |
| TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | Unit Detail: Screening, Item Type List, Empty State, Accordion, Klik Baris, dan Tanpa Aksi Kelola | FE+BE | 59 | 191, 192, 197, 199, 200, 206, 256, 257 |
| TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | Unit Detail: Search, Filter Product, Sort, dan Chip Item Type List | FE+BE | 56 | 193, 194, 198, 253, 254, 323, 324, 347 |
| TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | Unit Detail: Device Name List pada Principal dan Distributor (Screening, Search, Sort, Empty State) | FE+BE | 54 | 202, 203, 204, 205, 255, 348, 366 |
| TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | Unit Detail: Setup Column Item Type List (Screening, Hide, Reorder, Pin, Reset, Tutup, Guard) | mock | 84 | 212, 313, 314, 315, 316, 317, 318, 319, 351 |
| TC-GS-UOM-E2E-057-detail-setup-column-device-name-list | Unit Detail Principal: Setup Column Device Name List | mock | 37 | 320, 321, 322 |
| TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | Total Item di Header Unit Detail: Client, Principal, Nol, Relasi Nonaktif, Recycle Bin, dan Perubahan Relasi | FE+BE | 67 | 387, 388, 389, 390, 393, 394 |
| TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin | Konflik Create dan Edit Unit oleh Dua Admin | FE+BE | 25 | 91, 245, 246 |
| TC-GS-UOM-E2E-060-konflik-delete-dua-admin | Konflik Delete, Bulk Delete, dan Buka Detail pada Unit yang Dihapus Admin Lain | FE+BE | 40 | 103, 344, 345, 357, 413 |
| TC-GS-UOM-E2E-061-konflik-in-use-saat-confirm-delete | Konflik Unit Menjadi In-Use Saat Confirm Delete (Single dan Bulk) | FE+BE | 15 | 102, 123 |
| TC-GS-UOM-E2E-062-master-data-count-limit-race-slot-terakhir | Master Data Count Limit: Dua Admin Rebutan Slot Terakhir | FE+BE | 11 | 247 |
| TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | Pencatatan Log Create, Edit, Delete di Changelog, System Log, dan Activity Log serta Riwayat Rename | FE+BE | 48 | 213, 214, 215, 216, 219, 221, 222, 223, 265, 266 |
| TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control | Pencatatan Log Bulk Delete dan Modified By Aktor Non-Total Control | FE+BE | 24 | 220, 224, 267 |
| TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | Tidak Ada Pencatatan Log: Edit No-Op, Case-Only, dan Perubahan Relasi dari Produk Konsumen | FE+BE | 43 | 217, 218, 225, 330, 220, 267 |
| TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | Sinkronisasi Unit ke Fixed Asset: Opsi Dropdown Asset Name, Rename, Stale Reference, dan Hapus Referensi | FE+BE | 45 | 226, 228, 229, 230, 231, 269 |
| TC-GS-UOM-E2E-067-sync-device-name-admin-console | Sinkronisasi Unit ke Device Name Admin Console: Opsi Dropdown, Rename, Stale Reference, dan Breakdown Delete | FE+BE | 28 | 227, 232, 233, 268 |
| TC-GS-UOM-E2E-068-unit-hasil-import-edit-dan-hapus | Unit Hasil Import Type Measurement Dapat Diedit dan Dihapus seperti Unit Manual | FE+BE | 14 | 332 |
| TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | Defense-in-Depth: Request Tulis dan Baca Langsung ke Server Tanpa Capability Ditolak 403 | FE+BE | 34 | 235, 236, 237, 271, 411, 412 |
| TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | Defense-in-Depth: Emoji Lolos Validasi FE, Delete In-Use Langsung, Markup HTML, dan Payload SQL | FE+BE | 29 | 238, 242, 243, 244, 272 |
| TC-GS-UOM-E2E-071-isolasi-data-antar-client | Isolasi Data Measurement antar Client | FE+BE | 11 | 241 |
| TC-GS-UOM-E2E-072-tenant-suspended-expired-write-lockdown | Write Lockdown saat Client Suspended atau Expired | FE+BE | 19 | 239, 240 |
| TC-GS-UOM-E2E-073-tenant-plan-tier-tanpa-gating | Measurement Tidak Digate Plan: Create, Edit, Delete di Starter dan Enterprise serta Upgrade dan Downgrade | FE+BE | 20 | 248, 270 |
| TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | Mobile Android: Card List, Tap Detail, Menu Card, Search, Filter, Create, dan Delete sebagai Bottom Sheet | FE+BE (mobile) | 43 | 250, 251, 252, 356, 391 |
| TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete | Mobile Android: Selection Mode Bulk Delete (Long-Press, Cancel, Commit, Tanpa Capability Delete) | FE+BE (mobile) | 28 | 363, 364, 365 |

## TC hanya-BE (dilewati)

Kriteria: kolom FE Test `-` dan PIC FE `-` di `tc-measurement.md`, dan isinya kontrak API murni yang tidak terjangkau UI. Padanannya ada di `tc-measurement-backend.md` (dipetakan per endpoint, bukan per TC).

| TC | Alasan |
|---|---|
| TC-GS-UOM-398 | Route internal selector `GET /enterprise-management/internal/measurements` memakai `X-Service-Token` dan `X-Client-ID`; tidak terjangkau browser. |
| TC-GS-UOM-399 | Idem 398. |
| TC-GS-UOM-400 | Idem 398. |
| TC-GS-UOM-401 | Kontrak payload `GET /dropdown`. |
| TC-GS-UOM-402 | Create langsung `422` per field; perilaku FE di spec 020. |
| TC-GS-UOM-403 | Idem 402. |
| TC-GS-UOM-404 | Idem 402. |
| TC-GS-UOM-405 | Edit langsung `422` per field; perilaku FE di spec 026. |
| TC-GS-UOM-406 | Create langsung `409`; perilaku FE di spec 020. |
| TC-GS-UOM-407 | Edit langsung `409`; perilaku FE di spec 026. |
| TC-GS-UOM-408 | Create langsung `400 Invalid request body`. |
| TC-GS-UOM-409 | List/Export langsung `400`. |
| TC-GS-UOM-410 | Check References/Delete langsung `400`. |
| TC-GS-UOM-414 | List langsung `usedByItemsMin` > `usedByItemsMax` mengembalikan `200` kosong; perilaku FE di spec 038 (TC-382). |
| TC-GS-UOM-415 | Create langsung saat ceiling `409`; perilaku FE di spec 022. |

TC server-langsung lain (235, 236, 237, 238, 242, 271, 272, 411, 412) tetap masuk spec defense-in-depth 069 dan 070 (konvensi 3 prinsip 13 kelas a; preseden `TC-GS-BRAND-E2E-068`), dengan asersi hanya respons server dan state data.

## Pembagian TC lintas spec

- **TC-73, 74** (Edit No-Op, case-only): aksi dan hasil di spec 027; asersi tidak ada entri log di spec 065 (TC-217, 218) dengan aksi dan baseline sendiri.
- **TC-220, 267**: bagian presence (entri Delete) di spec 064; bagian absence (tidak ada entri `Box`) di spec 065 dengan aksi Bulk Delete campuran sendiri.
- **TC-225, 330** (relasi dari produk konsumen): spec 065. **TC-390**: spec 058.
- **TC-102, 123** (unit menjadi in-use setelah cek awal): spec 061. **TC-91, 103, 344, 345, 357, 413**: spec 059/060; resilience cek referensi/delete gagal di spec 035.
- **TC-30, 31** (tanpa capability, capability bersama Brand): spec 014; ubah capability hanya TC-31, 397, 92, 260 (dipulihkan di `after`).

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai (sebagian sudah terdaftar dari suite Brand): `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`, `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, `FA_ADMIN_PASSWORD`. Baru dan perlu didaftarkan di `spectra.config.ts` dan `.env.example`: `FA_ADMIN_CLIENTB_PASSWORD` (spec 071).
- `fixtures/measurement.json` belum ada: memuat minimal `urlTabMeasurement`, `assetName.category`, `assetName.tagType`, `supplyItem.*`, `deviceName.*`.
- Fixture akun/data yang tidak ada di Pre-setup TC: Admin B (Client A), Admin FAMS Client A dan Client B, akun pengubah plan/status Client, Client uji Suspended/Expired, referensi Supply (SAMS), Device Name, Tote dengan Crate (D-38), Mass dengan 1250 referensi (D-39), unit dengan relasi nonaktif atau Recycle Bin (TC-393, 394), unit ke-1.000 Client Limit.
- Kemampuan teknis: intercept jaringan (5xx, timeout, tahan respons), dua sesi browser paralel, ubah plan, status Client, capability role, dan General Settings (format tanggal, jam, Time Zone) lewat API, flag Guided Tooltip, `localStorage`, tangkap dan baca unduhan CSV/XLSX, dialog `beforeunload`, klien HTTP dengan token sesi, viewport 1024 dan 1280, perangkat atau emulator Android (spec 074, 075).
- Environment automation harus terisolasi dan boleh dibersihkan hook suite (baseline tepat 20 unit Client A).

## Temuan yang masih terbuka

- Daftar endpoint spec `Mode: mock` (010, 018, 019, 024, 025, 042, 043, 051, 052, 056, 057): path daftar dan Detail Measurement dikutip dari `tc-measurement-backend.md` di spec yang memakainya (042, 043, 051, 052, 056, 057); endpoint daftar Changelog serta rujukan `openapi.yaml` dan `low-level-design.md` (S-13c) disediakan tim FE (keputusan 2026-10-30, nomor 4).
- TC-382: Expected non-deterministik (perilaku bawaan komponen Range Filter); spec 038 hanya mengasersi tidak ada copy error khusus Measurement.
- Spec memakai unit milik spec bersuffix `{runId}-<NNN>` sebagai pengganti nama Pre-setup literal pada operasi tulis/hapus; baseline 20 unit bergantung pada pembersihan hook suite.
- Label header dan format tanggal berkas ekspor (BEGAP-410) perlu konfirmasi pemilik (spec 045, 046).
- TC-394 bertentangan dengan Pre-setup (Box punya 4 referensi); TC-247 menyebut 1.000 unit sedangkan Pre-setup 999; TC-163, 158, 392, 21, 84, 124, 105 punya Expected atau langkah ambigu (lihat "Temuan untuk QA" di Notes tiap spec).
- Spec 072: TC-GS-UOM-239 dan 240 tidak menyatakan apakah modal Create tertutup atau tetap terbuka sesudah penolakan tenant Suspended atau Expired; bagian Expired diakhiri muat ulang halaman (langkah 19) dengan penanganan dialog `beforeunload` yang disediakan tim FE. Menunggu keputusan QA/PM yang dicatat di Expected TC (hasil verifikasi aplikasi V3).
- Kemampuan yang disediakan tim FE/BE dan dinyatakan di `suite.md` (bagian Hook suite) dan `## Prerequisites` spec: sesi API aktor (login API dengan password memakai token yang tidak dihitung sebagai sesi web) dan penghapusan preferensi kolom Setup Column di browser (spec 042, 043, 051, 052, 056, 057).
- Spec di atas batas ±35 langkah (alasan tertulis di Notes tiap spec): 001 (38), 002 (58), 006 (38), 008 (41), 011 (43), 013 (80), 016 (42), 020 (61), 021 (60), 022 (42), 023 (68), 026 (38), 027 (78), 031 (67), 033 (57), 034 (43), 035 (78), 036 (67), 038 (54), 039 (103), 040 (44), 042 (83), 043 (62), 044 (63), 045 (36), 047 (51), 048 (39), 049 (57), 050 (50), 051 (56), 052 (54), 053 (59), 054 (56), 055 (54), 056 (84), 057 (37), 058 (67), 060 (40), 063 (48), 065 (43), 066 (45), 074 (43).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-UOM-1 | TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | FE+BE |
| TC-GS-UOM-2 | TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | FE+BE |
| TC-GS-UOM-3 | TC-GS-UOM-E2E-012-retensi-state-search-halaman-dan-refresh | FE+BE |
| TC-GS-UOM-4 | TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | FE+BE |
| TC-GS-UOM-5 | TC-GS-UOM-E2E-030-delete-single-sukses-dan-urutan-default | FE+BE |
| TC-GS-UOM-7 | TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | FE+BE |
| TC-GS-UOM-8 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-9 | TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-UOM-10 | TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | FE+BE |
| TC-GS-UOM-11 | TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | FE+BE |
| TC-GS-UOM-12 | TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | FE+BE |
| TC-GS-UOM-13 | TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-UOM-14 | TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-UOM-15 | TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | FE+BE |
| TC-GS-UOM-16 | TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-UOM-17 | TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UOM-18 | TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UOM-19 | TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UOM-20 | TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UOM-21 | TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-UOM-22 | TC-GS-UOM-E2E-010-guided-tooltip-konten-navigasi-keyboard | mock |
| TC-GS-UOM-23 | TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability | FE+BE |
| TC-GS-UOM-24 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-25 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-26 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-27 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-28 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-29 | TC-GS-UOM-E2E-013-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UOM-30 | TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability | FE+BE |
| TC-GS-UOM-31 | TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability | FE+BE |
| TC-GS-UOM-32 | TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UOM-33 | TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UOM-34 | TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UOM-35 | TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UOM-36 | TC-GS-UOM-E2E-017-create-population-12-unit-stay-checked | FE+BE |
| TC-GS-UOM-37 | TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih | mock |
| TC-GS-UOM-38 | TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih | mock |
| TC-GS-UOM-39 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-40 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-41 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-42 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-43 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-44 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-45 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-46 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-47 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-48 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-49 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-50 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-51 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-52 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-53 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-54 | TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih | mock |
| TC-GS-UOM-55 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-56 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-57 | TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih | mock |
| TC-GS-UOM-58 | TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-UOM-59 | TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-UOM-60 | TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-UOM-61 | TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-UOM-62 | TC-GS-UOM-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-UOM-63 | TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog | FE+BE |
| TC-GS-UOM-64 | TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog | FE+BE |
| TC-GS-UOM-65 | TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog | FE+BE |
| TC-GS-UOM-66 | TC-GS-UOM-E2E-022-master-data-count-limit-create-dan-dialog | FE+BE |
| TC-GS-UOM-67 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-68 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-69 | TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert | mock |
| TC-GS-UOM-70 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-71 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-72 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-73 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-74 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-75 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-76 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-77 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-78 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-79 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-80 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-81 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-82 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-83 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-84 | TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert | mock |
| TC-GS-UOM-85 | TC-GS-UOM-E2E-024-edit-screening-clear-field-dan-revert | mock |
| TC-GS-UOM-86 | TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog | mock |
| TC-GS-UOM-87 | TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog | mock |
| TC-GS-UOM-88 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-89 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-90 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-91 | TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin | FE+BE |
| TC-GS-UOM-92 | TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UOM-93 | TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel | FE+BE |
| TC-GS-UOM-94 | TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel | FE+BE |
| TC-GS-UOM-95 | TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel | FE+BE |
| TC-GS-UOM-96 | TC-GS-UOM-E2E-030-delete-single-sukses-dan-urutan-default | FE+BE |
| TC-GS-UOM-97 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-98 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-99 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-100 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-101 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-102 | TC-GS-UOM-E2E-061-konflik-in-use-saat-confirm-delete | FE+BE |
| TC-GS-UOM-103 | TC-GS-UOM-E2E-060-konflik-delete-dua-admin | FE+BE |
| TC-GS-UOM-104 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-105 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-106 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-107 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-108 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-109 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-110 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-111 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-112 | TC-GS-UOM-E2E-032-selection-limit-100-baris | FE+BE |
| TC-GS-UOM-113 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-114 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-115 | TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | FE+BE |
| TC-GS-UOM-116 | TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | FE+BE |
| TC-GS-UOM-117 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-118 | TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | FE+BE |
| TC-GS-UOM-119 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-120 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-121 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-122 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-123 | TC-GS-UOM-E2E-061-konflik-in-use-saat-confirm-delete | FE+BE |
| TC-GS-UOM-124 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-125 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-126 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-127 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-130 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-131 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-132 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-133 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-134 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-140 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-141 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-142 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-143 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-144 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-145 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-146 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-147 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-148 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-149 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-151 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-152 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-153 | TC-GS-UOM-E2E-041-pagination-default-page-size-dan-input-halaman | FE+BE |
| TC-GS-UOM-154 | TC-GS-UOM-E2E-041-pagination-default-page-size-dan-input-halaman | FE+BE |
| TC-GS-UOM-155 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-156 | TC-GS-UOM-E2E-012-retensi-state-search-halaman-dan-refresh | FE+BE |
| TC-GS-UOM-157 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-158 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-159 | TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | mock |
| TC-GS-UOM-160 | TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | mock |
| TC-GS-UOM-161 | TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | mock |
| TC-GS-UOM-162 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-163 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-164 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-165 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-166 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-167 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-168 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-169 | TC-GS-UOM-E2E-009-resilience-export-gagal-download | FE+BE |
| TC-GS-UOM-170 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-171 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-172 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-173 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-174 | TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | FE+BE |
| TC-GS-UOM-175 | TC-GS-UOM-E2E-007-empty-state-tabel-dan-changelog | FE+BE |
| TC-GS-UOM-176 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-177 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-178 | TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | FE+BE |
| TC-GS-UOM-179 | TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | FE+BE |
| TC-GS-UOM-180 | TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | FE+BE |
| TC-GS-UOM-181 | TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | FE+BE |
| TC-GS-UOM-182 | TC-GS-UOM-E2E-048-changelog-filter-dropdown-search-dan-or | FE+BE |
| TC-GS-UOM-183 | TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi | FE+BE |
| TC-GS-UOM-184 | TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi | FE+BE |
| TC-GS-UOM-185 | TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi | FE+BE |
| TC-GS-UOM-186 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-187 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-188 | TC-GS-UOM-E2E-046-download-changelog-dan-item-type-list-isi-file | FE+BE |
| TC-GS-UOM-189 | TC-GS-UOM-E2E-009-resilience-export-gagal-download | FE+BE |
| TC-GS-UOM-190 | TC-GS-UOM-E2E-050-changelog-sort-pagination-dan-kombinasi | FE+BE |
| TC-GS-UOM-191 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-192 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-193 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-194 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-195 | TC-GS-UOM-E2E-046-download-changelog-dan-item-type-list-isi-file | FE+BE |
| TC-GS-UOM-196 | TC-GS-UOM-E2E-009-resilience-export-gagal-download | FE+BE |
| TC-GS-UOM-197 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-198 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-199 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-200 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-202 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-203 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-204 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-205 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-206 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-207 | TC-GS-UOM-E2E-003-used-by-items-read-only-akses-detail | FE+BE |
| TC-GS-UOM-212 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-213 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-214 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-215 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-216 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-217 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-218 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-219 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-220 | TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control | FE+BE |
| TC-GS-UOM-220 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-221 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-222 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-223 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-224 | TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control | FE+BE |
| TC-GS-UOM-225 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-226 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-227 | TC-GS-UOM-E2E-067-sync-device-name-admin-console | FE+BE |
| TC-GS-UOM-228 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-229 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-230 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-231 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-232 | TC-GS-UOM-E2E-067-sync-device-name-admin-console | FE+BE |
| TC-GS-UOM-233 | TC-GS-UOM-E2E-067-sync-device-name-admin-console | FE+BE |
| TC-GS-UOM-234 | TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | FE+BE |
| TC-GS-UOM-235 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-236 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-237 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-238 | TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | FE+BE |
| TC-GS-UOM-239 | TC-GS-UOM-E2E-072-tenant-suspended-expired-write-lockdown | FE+BE |
| TC-GS-UOM-240 | TC-GS-UOM-E2E-072-tenant-suspended-expired-write-lockdown | FE+BE |
| TC-GS-UOM-241 | TC-GS-UOM-E2E-071-isolasi-data-antar-client | FE+BE |
| TC-GS-UOM-242 | TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | FE+BE |
| TC-GS-UOM-243 | TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | FE+BE |
| TC-GS-UOM-244 | TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | FE+BE |
| TC-GS-UOM-245 | TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin | FE+BE |
| TC-GS-UOM-246 | TC-GS-UOM-E2E-059-konflik-create-edit-dua-admin | FE+BE |
| TC-GS-UOM-247 | TC-GS-UOM-E2E-062-master-data-count-limit-race-slot-terakhir | FE+BE |
| TC-GS-UOM-248 | TC-GS-UOM-E2E-073-tenant-plan-tier-tanpa-gating | FE+BE |
| TC-GS-UOM-249 | TC-GS-UOM-E2E-001-screening-tab-measurement-layout-tooltip-dan-sticky | FE+BE |
| TC-GS-UOM-250 | TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | FE+BE (mobile) |
| TC-GS-UOM-251 | TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | FE+BE (mobile) |
| TC-GS-UOM-252 | TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | FE+BE (mobile) |
| TC-GS-UOM-253 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-254 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-255 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-256 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-257 | TC-GS-UOM-E2E-053-detail-item-type-list-screening-dan-empty | FE+BE |
| TC-GS-UOM-258 | TC-GS-UOM-E2E-033-bulk-delete-dialog-screening-cancel-dan-blokir | FE+BE |
| TC-GS-UOM-259 | TC-GS-UOM-E2E-044-state-hover-fokus-backdrop-modal-dan-focus-trap | FE+BE |
| TC-GS-UOM-260 | TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UOM-261 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-262 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-263 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-264 | TC-GS-UOM-E2E-027-edit-sukses-no-op-saving-state-dan-double-click | FE+BE |
| TC-GS-UOM-265 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-266 | TC-GS-UOM-E2E-063-log-create-edit-delete-tiga-surface-dan-rename | FE+BE |
| TC-GS-UOM-267 | TC-GS-UOM-E2E-064-log-bulk-delete-dan-aktor-non-total-control | FE+BE |
| TC-GS-UOM-267 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-268 | TC-GS-UOM-E2E-067-sync-device-name-admin-console | FE+BE |
| TC-GS-UOM-269 | TC-GS-UOM-E2E-066-sync-fams-form-dan-agregasi | FE+BE |
| TC-GS-UOM-270 | TC-GS-UOM-E2E-073-tenant-plan-tier-tanpa-gating | FE+BE |
| TC-GS-UOM-271 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-272 | TC-GS-UOM-E2E-070-defense-in-depth-bypass-validasi-in-use-xss-dan-sql | FE+BE |
| TC-GS-UOM-273 | TC-GS-UOM-E2E-025-edit-unsaved-changes-dialog | mock |
| TC-GS-UOM-274 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-275 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-276 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-277 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-278 | TC-GS-UOM-E2E-032-selection-limit-100-baris | FE+BE |
| TC-GS-UOM-279 | TC-GS-UOM-E2E-031-bulk-selection-bar-select-all-dan-retensi | FE+BE |
| TC-GS-UOM-280 | TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | FE+BE |
| TC-GS-UOM-281 | TC-GS-UOM-E2E-034-bulk-delete-sukses-homogen-campuran-dan-double-click | FE+BE |
| TC-GS-UOM-282 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-284 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-285 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-286 | TC-GS-UOM-E2E-039-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-GS-UOM-293 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-295 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-297 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-298 | TC-GS-UOM-E2E-044-state-hover-fokus-backdrop-modal-dan-focus-trap | FE+BE |
| TC-GS-UOM-299 | TC-GS-UOM-E2E-044-state-hover-fokus-backdrop-modal-dan-focus-trap | FE+BE |
| TC-GS-UOM-302 | TC-GS-UOM-E2E-049-changelog-filter-chip-x-uncheck-dan-overflow | FE+BE |
| TC-GS-UOM-303 | TC-GS-UOM-E2E-049-changelog-filter-chip-x-uncheck-dan-overflow | FE+BE |
| TC-GS-UOM-304 | TC-GS-UOM-E2E-049-changelog-filter-chip-x-uncheck-dan-overflow | FE+BE |
| TC-GS-UOM-305 | TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-UOM-306 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-307 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-308 | TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | mock |
| TC-GS-UOM-309 | TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | mock |
| TC-GS-UOM-310 | TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | mock |
| TC-GS-UOM-311 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-312 | TC-GS-UOM-E2E-051-changelog-setup-column-screening-hide-dan-tutup | mock |
| TC-GS-UOM-313 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-314 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-315 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-316 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-317 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-318 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-319 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-320 | TC-GS-UOM-E2E-057-detail-setup-column-device-name-list | mock |
| TC-GS-UOM-321 | TC-GS-UOM-E2E-057-detail-setup-column-device-name-list | mock |
| TC-GS-UOM-322 | TC-GS-UOM-E2E-057-detail-setup-column-device-name-list | mock |
| TC-GS-UOM-323 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-324 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-327 | TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | FE+BE |
| TC-GS-UOM-328 | TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | FE+BE |
| TC-GS-UOM-329 | TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings | FE+BE |
| TC-GS-UOM-330 | TC-GS-UOM-E2E-065-log-absence-no-op-case-only-dan-relasi-konsumen | FE+BE |
| TC-GS-UOM-332 | TC-GS-UOM-E2E-068-unit-hasil-import-edit-dan-hapus | FE+BE |
| TC-GS-UOM-333 | TC-GS-UOM-E2E-028-delete-row-action-dialog-screening-dan-cancel | FE+BE |
| TC-GS-UOM-334 | TC-GS-UOM-E2E-011-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UOM-335 | TC-GS-UOM-E2E-020-create-validasi-diblokir | FE+BE |
| TC-GS-UOM-336 | TC-GS-UOM-E2E-026-edit-validasi-diblokir-dan-nama-sendiri | FE+BE |
| TC-GS-UOM-337 | TC-GS-UOM-E2E-047-changelog-screening-hover-dan-search | FE+BE |
| TC-GS-UOM-338 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-339 | TC-GS-UOM-E2E-041-pagination-default-page-size-dan-input-halaman | FE+BE |
| TC-GS-UOM-340 | TC-GS-UOM-E2E-021-create-sukses-batas-trim-karakter-submit-dan-toast | FE+BE |
| TC-GS-UOM-343 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-344 | TC-GS-UOM-E2E-060-konflik-delete-dua-admin | FE+BE |
| TC-GS-UOM-345 | TC-GS-UOM-E2E-060-konflik-delete-dua-admin | FE+BE |
| TC-GS-UOM-347 | TC-GS-UOM-E2E-054-detail-item-type-list-search-filter-sort-dan-chip | FE+BE |
| TC-GS-UOM-348 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-349 | TC-GS-UOM-E2E-043-setup-column-tabel-reorder-pin-dan-reset | mock |
| TC-GS-UOM-350 | TC-GS-UOM-E2E-052-changelog-setup-column-reorder-pin-dan-reset | mock |
| TC-GS-UOM-351 | TC-GS-UOM-E2E-056-detail-setup-column-item-type-list | mock |
| TC-GS-UOM-352 | TC-GS-UOM-E2E-023-resilience-tulis-create-edit-5xx-timeout-dan-try-again | FE+BE |
| TC-GS-UOM-353 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-354 | TC-GS-UOM-E2E-035-resilience-hapus-single-bulk-dan-cek-referensi | FE+BE |
| TC-GS-UOM-356 | TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | FE+BE (mobile) |
| TC-GS-UOM-357 | TC-GS-UOM-E2E-060-konflik-delete-dua-admin | FE+BE |
| TC-GS-UOM-362 | TC-GS-UOM-E2E-008-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-UOM-363 | TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete | FE+BE (mobile) |
| TC-GS-UOM-364 | TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete | FE+BE (mobile) |
| TC-GS-UOM-365 | TC-GS-UOM-E2E-075-mobile-selection-mode-bulk-delete | FE+BE (mobile) |
| TC-GS-UOM-366 | TC-GS-UOM-E2E-055-detail-device-name-list-principal-dan-distributor | FE+BE |
| TC-GS-UOM-367 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-368 | TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance | FE+BE |
| TC-GS-UOM-369 | TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance | FE+BE |
| TC-GS-UOM-370 | TC-GS-UOM-E2E-004-used-by-items-sama-dengan-total-item-per-instance | FE+BE |
| TC-GS-UOM-371 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-372 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-373 | TC-GS-UOM-E2E-003-used-by-items-read-only-akses-detail | FE+BE |
| TC-GS-UOM-374 | TC-GS-UOM-E2E-005-used-by-items-fixture-khusus-nama-sama-dan-angka-besar | FE+BE |
| TC-GS-UOM-375 | TC-GS-UOM-E2E-005-used-by-items-fixture-khusus-nama-sama-dan-angka-besar | FE+BE |
| TC-GS-UOM-376 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-377 | TC-GS-UOM-E2E-040-sort-unit-name-symbol-used-by-dan-last-updated | FE+BE |
| TC-GS-UOM-378 | TC-GS-UOM-E2E-037-filter-panel-screening-last-updated-dan-clear | FE+BE |
| TC-GS-UOM-379 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-380 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-381 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-382 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-383 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-384 | TC-GS-UOM-E2E-036-search-toolbar-unit-name-symbol-dan-kolom-hidden | FE+BE |
| TC-GS-UOM-385 | TC-GS-UOM-E2E-042-setup-column-tabel-screening-hide-dan-tutup | mock |
| TC-GS-UOM-386 | TC-GS-UOM-E2E-045-download-tabel-utama-menu-dan-isi-file | FE+BE |
| TC-GS-UOM-387 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-388 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-389 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-390 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-391 | TC-GS-UOM-E2E-074-mobile-card-list-menu-dan-dialog | FE+BE (mobile) |
| TC-GS-UOM-392 | TC-GS-UOM-E2E-038-filter-used-by-items-rentang | FE+BE |
| TC-GS-UOM-393 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-394 | TC-GS-UOM-E2E-058-total-item-header-detail-dan-sinkron-used-by | FE+BE |
| TC-GS-UOM-395 | TC-GS-UOM-E2E-029-delete-blokir-in-use-client-dan-principal | FE+BE |
| TC-GS-UOM-396 | TC-GS-UOM-E2E-002-isi-sel-used-by-link-detail-dan-hover | FE+BE |
| TC-GS-UOM-397 | TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UOM-411 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-412 | TC-GS-UOM-E2E-069-defense-in-depth-request-langsung-tanpa-capability | FE+BE |
| TC-GS-UOM-413 | TC-GS-UOM-E2E-060-konflik-delete-dua-admin | FE+BE |
