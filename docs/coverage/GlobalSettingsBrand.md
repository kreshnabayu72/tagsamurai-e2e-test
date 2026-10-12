# Coverage E2E — Global Settings > Master Reference > Brand

Sumber: `global-settings/brand/TestCases/tc-brand.md` (294 ID `TC-GS-BRAND-1`–`294`; 281 aktif, 13 retired). Suite: `specs/GlobalSettings/Brand/`. Prefix: `GS` + `BRAND` (`TC-GS-BRAND-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 281 TC aktif masuk spec, 0 TC hanya-BE (tidak ada `tc-brand-backend.md`; TC-226/227 dijalankan dari browser). 75 spec. Setiap TC aktif terpetakan ke satu spec, kecuali tiga TC yang sengaja terbelah (prinsip 10): TC-78 dan TC-79 (aksi Edit No-Op di spec 021, asersi tidak ada log di spec 062) dan TC-227 (Expected a di spec 068, Expected b tidak ada entri Delete di spec 075).

TC retired (tidak masuk spec): TC-GS-BRAND-9, 49, 51, 132, 136, 137, 138, 139, 140, 200, 222, 238, 250.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-BRAND-E2E-001-screening-tab-brand-layout-dan-tooltip | Screening Tab Brand: Layout, Tab Default, Tooltip Table Tools, dan Layout Tablet | FE+BE | 35 | 2, 3, 6, 254 |
| TC-GS-BRAND-E2E-002-isi-sel-brand-name-used-by-dan-last-updated | Isi Sel Tabel Brand: Used By (Items), Brand Name Link, dan Nama Panjang | FE+BE | 30 | 8, 11, 12, 261, 267 |
| TC-GS-BRAND-E2E-003-retensi-state-search-filter-sort-dan-refresh | Retensi State Tab Brand: Search, Filter, Sort, Halaman, Pindah Tab, dan Refresh | FE+BE | 28 | 4, 5, 153 |
| TC-GS-BRAND-E2E-004-empty-state-tabel-dan-changelog | Empty State Tabel Brand dan Changelog | FE+BE | 29 | 14, 15, 16, 170, 171 |
| TC-GS-BRAND-E2E-005-resilience-baca-loading-error-dan-try-again | Resilience Baca Tab Brand: Loading, Error Load, dan Try Again | FE+BE | 32 | 13, 17, 18, 172, 185 |
| TC-GS-BRAND-E2E-006-resilience-export-gagal-download | Resilience Export: Kegagalan Download Brand, Changelog, dan Accordion Detail | FE+BE | 31 | 167, 183, 195, 249 |
| TC-GS-BRAND-E2E-007-guided-tooltip-konten-navigasi-keyboard | Konten dan Navigasi Keyboard Guided Tooltip Tab Brand | mock | 51 | 19, 22, 25, 26 |
| TC-GS-BRAND-E2E-008-guided-tooltip-flag-seen-dan-dismiss | Flag Seen dan Dismiss Guided Tooltip Tab Brand | FE+BE | 27 | 20, 21, 23, 24 |
| TC-GS-BRAND-E2E-009-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Brand per Role | FE+BE | 70 | 27, 28, 29, 30, 31, 32 |
| TC-GS-BRAND-E2E-010-role-matrix-negatif-tanpa-capability | Role Matrix Negatif: Aktor Tanpa Capability Tidak Dapat Mengakses Tab Brand | FE+BE | 9 | 33, 34 |
| TC-GS-BRAND-E2E-011-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability | FE+BE | 31 | 36, 37, 38, 39 |
| TC-GS-BRAND-E2E-012-capability-dicabut-saat-aksi-berjalan | Capability Dicabut Saat Aksi Sedang Berjalan | FE+BE | 57 | 35, 68, 91, 107, 129 |
| TC-GS-BRAND-E2E-013-create-screening-clear-field-dan-tutup-bersih | Screening Popup Create Brand, Clear Field, dan Tutup Bersih | mock | 29 | 40, 41, 57, 58 |
| TC-GS-BRAND-E2E-014-create-unsaved-changes-dialog | Dialog Unsaved Changes pada Popup Create Brand | mock | 26 | 59, 60, 61, 62, 63 |
| TC-GS-BRAND-E2E-015-create-validasi-diblokir | Validasi Create Brand yang Diblokir | FE+BE | 48 | 42, 43, 45, 48, 52, 53, 54 |
| TC-GS-BRAND-E2E-016-create-sukses-batas-trim-karakter-dan-submit | Create Brand Berhasil: Batas Karakter, Trim, Karakter Khusus, dan Perilaku Submit | FE+BE | 60 | 44, 46, 47, 50, 56, 64, 65, 151 |
| TC-GS-BRAND-E2E-017-create-population-12-brand-stay-checked | Create 12 Brand Berurutan dengan Stay on this form Dicentang (Population) | FE+BE | 78 | 1 |
| TC-GS-BRAND-E2E-018-edit-screening-clear-field-dan-revert | Screening Popup Edit Brand, Clear Field, dan Revert ke Nilai Tersimpan | mock | 17 | 69, 80, 81, 82 |
| TC-GS-BRAND-E2E-019-edit-unsaved-changes-dialog | Dialog Unsaved Changes pada Popup Edit Brand | mock | 21 | 83, 84, 85, 86 |
| TC-GS-BRAND-E2E-020-edit-validasi-diblokir-dan-nama-sendiri | Validasi Edit Brand yang Diblokir dan Nama Milik Sendiri | FE+BE | 29 | 71, 72, 74, 76, 77 |
| TC-GS-BRAND-E2E-021-edit-sukses-no-op-saving-state-dan-double-click | Edit Brand Sukses, No-Op, Saving State, dan Klik Ganda Save | FE+BE | 50 | 70, 73, 75, 78, 79, 87, 88 |
| TC-GS-BRAND-E2E-022-delete-dialog-screening-dan-cancel | Screening Row Action dan Dialog Delete Brand serta Cancel | FE+BE | 20 | 92, 93, 94, 98 |
| TC-GS-BRAND-E2E-023-delete-blokir-in-use-client-dan-principal | Delete Brand Diblokir karena In-Use pada Client dan Principal | FE+BE | 28 | 96, 97, 99, 100, 101 |
| TC-GS-BRAND-E2E-024-delete-single-sukses-dan-urutan-default | Delete Brand Tunggal Berhasil dan Urutan Default Tabel | FE+BE | 18 | 7, 95, 106 |
| TC-GS-BRAND-E2E-025-konflik-create-edit-dua-admin | Konflik Create dan Edit Brand oleh Dua Admin | FE+BE | 52 | 55, 90, 236, 237 |
| TC-GS-BRAND-E2E-026-konflik-delete-dua-admin | Konflik Delete dan Bulk Delete Brand oleh Dua Admin | FE+BE | 49 | 103, 123, 291 |
| TC-GS-BRAND-E2E-027-konflik-in-use-saat-confirm-delete | Konflik Brand Menjadi In-Use Saat Confirm Delete | FE+BE | 36 | 102, 120, 121, 122 |
| TC-GS-BRAND-E2E-028-bulk-selection-bar-select-all-dan-retensi | Bulk Action Bar: Screening, Checkbox Header, Select All, dan Retensi Seleksi | FE+BE | 61 | 108, 109, 110, 111, 126 |
| TC-GS-BRAND-E2E-029-bulk-delete-dialog-screening-cancel-dan-blokir | Dialog Bulk Delete: Screening, Cancel, dan Blokir In-Use | FE+BE | 52 | 112, 113, 114, 115, 117, 119, 252 |
| TC-GS-BRAND-E2E-030-bulk-delete-sukses-homogen-campuran-dan-double-click | Bulk Delete Berhasil: Homogen, Campuran, dan Klik Ganda | FE+BE | 28 | 116, 118, 125 |
| TC-GS-BRAND-E2E-031-selection-limit-100-baris | Selection Limit 100 Baris: Centang Manual Diblokir dan Select All di-cap | FE+BE | 20 | 127, 128 |
| TC-GS-BRAND-E2E-032-master-data-count-limit-create-dan-dialog | Master Data Count Limit: Create di Batas, Dialog Limit Reached, dan Tabel Tersaring | FE+BE | 39 | 232, 233, 293 |
| TC-GS-BRAND-E2E-033-master-data-count-limit-race-slot-terakhir | Master Data Count Limit: Dua Admin Rebutan Slot Terakhir | FE+BE | 9 | 234 |
| TC-GS-BRAND-E2E-034-brand-tidak-digate-plan | Brand Tidak Digate Plan: Create Identik di Semua Plan | FE+BE | 18 | 235 |
| TC-GS-BRAND-E2E-035-search-toolbar-brand-name | Search Toolbar Tabel Brand: Siklus Search dan Pencocokan Brand Name | FE+BE | 47 | 130, 131, 133, 134, 274 |
| TC-GS-BRAND-E2E-036-filter-panel-used-by-items-rentang | Filter Panel Tabel Brand: Rentang Used By (Items) | FE+BE | 66 | 135, 145, 263, 264, 265, 266, 278 |
| TC-GS-BRAND-E2E-037-filter-kombinasi-search-last-updated-dan-clear | Filter Last Updated, Kombinasi Search dan Filter, serta Clear Filter pada Tabel Brand | FE+BE | 24 | 141, 142, 143, 144, 150 |
| TC-GS-BRAND-E2E-038-sort-brand-name-used-by-dan-last-updated | Sort Tabel Brand pada Brand Name, Used By (Items), dan Last Updated | FE+BE | 25 | 146, 147, 148, 273 |
| TC-GS-BRAND-E2E-039-pagination-dan-kombinasi-search-filter-sort | Pagination Tabel Brand dan Kombinasi Search, Filter, Sort, serta Page Size | FE+BE | 17 | 149, 152 |
| TC-GS-BRAND-E2E-040-setup-column-tabel-brand-screening-hide-dan-tutup | Setup Column Tabel Brand: Screening, Hide, dan Tutup Modal | mock | 36 | 154, 155, 156, 157, 161, 162 |
| TC-GS-BRAND-E2E-041-setup-column-tabel-brand-reorder-pin-dan-reset | Setup Column Tabel Brand: Reorder, Pin, dan Reset to Default | mock | 26 | 158, 159, 160 |
| TC-GS-BRAND-E2E-042-used-by-items-link-detail-dan-hover | Link Angka Used By (Items): Hover, Fokus, dan Pembukaan Brand Detail | FE+BE | 43 | 268, 269, 271, 280 |
| TC-GS-BRAND-E2E-043-used-by-items-read-only-akses-detail | Read Only Mengakses Brand Detail lewat Link Nama dan Angka Used By (Items) | FE+BE | 14 | 204, 270 |
| TC-GS-BRAND-E2E-044-used-by-items-principal-distributor | Used By (Items) Sama dengan Total Item di Detail pada Instance Principal dan Distributor | FE+BE | 13 | 272 |
| TC-GS-BRAND-E2E-045-used-by-items-angka-besar-1250 | Angka Besar Used By (Items) Tampil Apa Adanya dan Terurut Numerik | FE+BE | 11 | 279 |
| TC-GS-BRAND-E2E-046-format-tanggal-general-settings | Format Tanggal dan Waktu General Settings pada Tabel Brand, Filter, dan Changelog | FE+BE | 19 | 10, 223, 224 |
| TC-GS-BRAND-E2E-047-download-tabel-utama-isi-file | Download Tabel Brand: Isi File CSV dan XLSX | FE+BE | 20 | 163, 164, 165, 166 |
| TC-GS-BRAND-E2E-048-download-changelog-dan-item-type-list-isi-file | Download Changelog dan Accordion Item Type List: Isi File | FE+BE | 10 | 182, 194 |
| TC-GS-BRAND-E2E-049-download-device-sku-list-principal-isi-file | Download Accordion Device SKU List pada Instance Principal: Isi dan Nama File | FE+BE | 13 | 197, 294 |
| TC-GS-BRAND-E2E-050-changelog-screening-hover-dan-search | Changelog Brand: Screening, Hover Modified By, dan Search | FE+BE | 24 | 168, 169, 173, 174 |
| TC-GS-BRAND-E2E-051-changelog-filter-dropdown-search-dan-or | Changelog Brand: Filter per Field, Pencarian di Dropdown, dan Logika AND/OR | FE+BE | 38 | 175, 176, 177, 178, 284 |
| TC-GS-BRAND-E2E-052-changelog-filter-chip-x-uncheck-dan-overflow | Changelog Brand: Chip Filter (X), Uncheck Opsi, dan Overflow +N more | FE+BE | 45 | 281, 282, 283 |
| TC-GS-BRAND-E2E-053-changelog-sort-pagination-dan-setup-column | Changelog Brand: Sort, Pagination, dan Setup Column | FE+BE | 29 | 179, 180, 181 |
| TC-GS-BRAND-E2E-054-detail-item-type-list-screening-dan-empty | Brand Detail: Screening Item Type List, Empty State, dan Hover Chip Model/Type | FE+BE | 34 | 184, 186, 189, 193, 203, 262 |
| TC-GS-BRAND-E2E-055-detail-item-type-list-search-filter-sort-dan-chip | Brand Detail: Search, Filter, Sort, dan Chip Filter Item Type List | FE+BE | 52 | 190, 191, 192, 285, 286, 287 |
| TC-GS-BRAND-E2E-056-detail-model-type-popup-dan-esc-bertingkat | Brand Detail: Popup Model/Type dan Esc Bertingkat | FE+BE | 13 | 201, 202 |
| TC-GS-BRAND-E2E-057-detail-device-sku-list-principal-distributor-screening | Brand Detail: Device SKU List pada Instance Principal dan Distributor | FE+BE | 43 | 187, 188, 198, 199, 259 |
| TC-GS-BRAND-E2E-058-detail-device-sku-list-search-filter-sort | Brand Detail Principal: Search, Filter Category, dan Sort Accordion Device SKU List | FE+BE | 30 | 196, 251, 255, 260 |
| TC-GS-BRAND-E2E-059-detail-device-sku-list-chip-category-dan-or | Brand Detail Principal: Chip Filter Category dan Logika OR pada Device SKU List | FE+BE | 25 | 288, 289, 290 |
| TC-GS-BRAND-E2E-060-log-create-edit-delete-3-surface-dan-rename | Pencatatan Log Create, Edit, Delete Brand di Changelog, System Log, dan Activity Log serta Riwayat Rename | FE+BE | 32 | 206, 207, 208, 214 |
| TC-GS-BRAND-E2E-061-log-bulk-delete-dan-aktor-non-total-control | Pencatatan Log Bulk Delete Homogen dan Log Aktor Non-Total Control | FE+BE | 18 | 209, 215 |
| TC-GS-BRAND-E2E-062-log-absence-no-op-skip-cancel-dan-import | Tidak Ada Pencatatan Log untuk Edit No-Op, Delete Dibatalkan atau Ditolak, Import Brand, dan Brand yang Dilewati | FE+BE | 45 | 78, 79, 210, 211, 212, 292 |
| TC-GS-BRAND-E2E-063-sync-fams-form-dan-agregasi-used-by | Sinkronisasi Brand ke Fixed Asset: Opsi Form Asset Name, Rename, dan Agregasi Used By (Items) | FE+BE | 27 | 205, 216, 217, 218 |
| TC-GS-BRAND-E2E-064-sync-device-sku-admin-console-principal | Sinkronisasi Brand ke Device SKU Admin Console pada Instance Principal | FE+BE | 30 | 220, 245, 246, 248 |
| TC-GS-BRAND-E2E-065-sync-all-tags-pemilih-dan-snapshot | Sinkronisasi Brand ke All Tags: Pemilih Brand Activate TAG BYO dan Snapshot Nama Brand pada TAG | FE+BE | 22 | 221, 247, 275, 276, 277 |
| TC-GS-BRAND-E2E-066-stale-reference-form-konsumen | Stale Reference: Submit Form Konsumen dengan Brand yang Baru Dihapus Admin Lain | FE+BE | 31 | 219, 256, 257 |
| TC-GS-BRAND-E2E-067-brand-hasil-import-edit-dan-hapus | Brand Hasil Import Dapat Diedit dan Dihapus seperti Brand Manual | FE+BE | 6 | 225 |
| TC-GS-BRAND-E2E-068-defense-in-depth-bypass-server-dan-xss | Defense-in-Depth Brand: Bypass UI ke Server, Emoji Lolos Filter FE, dan Payload Script | FE+BE | 25 | 226, 227, 230, 231 |
| TC-GS-BRAND-E2E-069-isolasi-antar-client | Isolasi Data Brand antar Client dan Nama Sama di Client Berbeda | FE+BE | 9 | 228, 229 |
| TC-GS-BRAND-E2E-070-resilience-tulis-create-edit-timeout-dan-toast | Resilience Tulis Brand: Create Gagal 5xx, Timeout lalu Retry, Edit Gagal 5xx, dan Durasi Toast | FE+BE | 43 | 66, 67, 89, 253 |
| TC-GS-BRAND-E2E-071-resilience-hapus-single-bulk-dan-cek-referensi | Resilience Hapus Brand: Cek Referensi Gagal, Delete Gagal, dan Bulk Delete Gagal | FE+BE | 33 | 104, 105, 124, 258 |
| TC-GS-BRAND-E2E-072-tenant-suspended-expired-write-lockdown | Write Lockdown Brand saat Client Suspended atau Expired: Create, Edit, Delete, dan Bulk Delete Ditolak | FE+BE | 27 | 239, 240, 244 |
| TC-GS-BRAND-E2E-073-tenant-suspended-baca-tetap-tersedia | Baca Data Brand Tetap Tersedia saat Client Suspended | FE+BE | 7 | 241 |
| TC-GS-BRAND-E2E-074-mobile-card-list-dan-selection-mode | Mobile Android: Card List Brand dan Selection Mode untuk Bulk Delete | FE+BE (mobile) | 25 | 242, 243 |
| TC-GS-BRAND-E2E-075-log-absence-dua-sesi-dan-request-langsung | Tidak Ada Entri Log Kedua untuk Delete Record yang Sudah Terhapus dan Tidak Ada Entri Delete untuk Request Langsung ke Server | FE+BE | 11 | 213, 227 |

## Pembagian TC lintas spec

- **TC-GS-BRAND-78, 79**: aksi dan hasil Edit No-Op di spec `021`; asersi tidak ada entri log baru di spec `062` (kelas g).
- **TC-GS-BRAND-227**: Expected a (Acme Corp tetap ada) di spec `068`; Expected b (tidak ada entri Delete di Changelog) di spec `075` bersama TC-213.
- **TC-GS-BRAND-123, 291**: asersi log berupa hitungan (tepat 1 entri Delete per brand di tiga surface), utuh di spec `026`.
- **TC-GS-BRAND-103 butir c**: asersi jumlah entri Delete di spec `026`; TC-213 (dua sesi) di spec `075`.
- **TC-GS-BRAND-10** dijalankan di spec `046` (butuh ubah General Settings); **TC-GS-BRAND-275** di spec `065` (TC-276 bergantung padanya).
- **TC-GS-BRAND-215 b** (isolasi log per aktor) tetap di spec `061`; bukan kelas g (konvensi 13g).

## Kebutuhan lingkungan (tim FE)

- Env var password sudah didaftarkan di `spectra.config.ts` dan `.env.example`: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`, `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, `FA_ADMIN_PASSWORD`. Nilainya diisi tim FE; konfirmasi bahwa `GS_TC_PASSWORD` berlaku untuk `totalControl_automated_qaTeam1@qwertysystem.net`.
- Fixture akun baru (Tabel Pre-setup TC): Total Control Client A admin kedua, Total Control Client Limit admin kedua, Admin FAMS Client A, Total Control Distributor.
- Fixture data baru: Brand `Aero Dist` (Distributor), `Mixed One` (Principal: Item Type + Device SKU), Model/Type 30 karakter di Monitor Vertex Labs, Ten Co (10 Asset Name), Big Co (1250 Asset Name), Client Limit dengan 999 brand, `fixtures/brand.json` (nilai field wajib lain form Create Asset Name FAMS, Create Device SKU, Activate TAG BYO), pool TAG BYO per run beserta Delete TAG (unpaired) untuk cleanup.
- Kemampuan teknis: intercept jaringan (500, timeout, tahan respons), dua sesi browser paralel, ubah plan dan status Client (Suspended/Expired) lewat API, ubah capability role lewat API, membaca dan menghapus `localStorage`, menangkap dan membaca berkas unduhan (CSV/XLSX), mengirim request HTTP langsung dari konteks browser, perangkat atau emulator Android (spec 074).
- Environment automation harus terisolasi dari aktivitas pengguna lain agar asersi himpunan (mis. opsi Modified By pada TC-175) stabil.

## Temuan yang masih terbuka

- TC-237 butir a menyebut "toast sukses" tanpa teks (spec 025 mengikuti TC).
- TC-67: Expected b menerima dua hasil (sukses atau ditolak `Brand Name already exists`); spec 070 menetapkan cabang ditolak dan asersi tepat 1 baris.
- TC-195/249/63/67/226 bertanda Manual Only; tetap ditulis sebagai spec dengan kebutuhan teknis di Prerequisites (bagian 2 konvensi).
- Spec melewati batas ±35 langkah dengan satu kelas harness: 17- (78), 09- (70), 36- (66), 28- (61), 16- (60), 12- (57), 25- (52), 29- (52), 55- (52), 07- (51), 21- (50), 26- (49), 15- (48), 35- (47), 52- (45), 62- (45), 42- (43), 57- (43), 70- (43), 32- (39), 51- (38), 27- (36), 40- (36).
- Hak akun Total Control Principal untuk mengubah status Client A dan endpoint-nya belum terkonfirmasi (spec 072, 073).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-BRAND-1 | TC-GS-BRAND-E2E-017 | FE+BE |
| TC-GS-BRAND-2 | TC-GS-BRAND-E2E-001 | FE+BE |
| TC-GS-BRAND-3 | TC-GS-BRAND-E2E-001 | FE+BE |
| TC-GS-BRAND-4 | TC-GS-BRAND-E2E-003 | FE+BE |
| TC-GS-BRAND-5 | TC-GS-BRAND-E2E-003 | FE+BE |
| TC-GS-BRAND-6 | TC-GS-BRAND-E2E-001 | FE+BE |
| TC-GS-BRAND-7 | TC-GS-BRAND-E2E-024 | FE+BE |
| TC-GS-BRAND-8 | TC-GS-BRAND-E2E-002 | FE+BE |
| TC-GS-BRAND-10 | TC-GS-BRAND-E2E-046 | FE+BE |
| TC-GS-BRAND-11 | TC-GS-BRAND-E2E-002 | FE+BE |
| TC-GS-BRAND-12 | TC-GS-BRAND-E2E-002 | FE+BE |
| TC-GS-BRAND-13 | TC-GS-BRAND-E2E-005 | FE+BE |
| TC-GS-BRAND-14 | TC-GS-BRAND-E2E-004 | FE+BE |
| TC-GS-BRAND-15 | TC-GS-BRAND-E2E-004 | FE+BE |
| TC-GS-BRAND-16 | TC-GS-BRAND-E2E-004 | FE+BE |
| TC-GS-BRAND-17 | TC-GS-BRAND-E2E-005 | FE+BE |
| TC-GS-BRAND-18 | TC-GS-BRAND-E2E-005 | FE+BE |
| TC-GS-BRAND-19 | TC-GS-BRAND-E2E-007 | mock |
| TC-GS-BRAND-20 | TC-GS-BRAND-E2E-008 | FE+BE |
| TC-GS-BRAND-21 | TC-GS-BRAND-E2E-008 | FE+BE |
| TC-GS-BRAND-22 | TC-GS-BRAND-E2E-007 | mock |
| TC-GS-BRAND-23 | TC-GS-BRAND-E2E-008 | FE+BE |
| TC-GS-BRAND-24 | TC-GS-BRAND-E2E-008 | FE+BE |
| TC-GS-BRAND-25 | TC-GS-BRAND-E2E-007 | mock |
| TC-GS-BRAND-26 | TC-GS-BRAND-E2E-007 | mock |
| TC-GS-BRAND-27 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-28 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-29 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-30 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-31 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-32 | TC-GS-BRAND-E2E-009 | FE+BE |
| TC-GS-BRAND-33 | TC-GS-BRAND-E2E-010 | FE+BE |
| TC-GS-BRAND-34 | TC-GS-BRAND-E2E-010 | FE+BE |
| TC-GS-BRAND-35 | TC-GS-BRAND-E2E-012 | FE+BE |
| TC-GS-BRAND-36 | TC-GS-BRAND-E2E-011 | FE+BE |
| TC-GS-BRAND-37 | TC-GS-BRAND-E2E-011 | FE+BE |
| TC-GS-BRAND-38 | TC-GS-BRAND-E2E-011 | FE+BE |
| TC-GS-BRAND-39 | TC-GS-BRAND-E2E-011 | FE+BE |
| TC-GS-BRAND-40 | TC-GS-BRAND-E2E-013 | mock |
| TC-GS-BRAND-41 | TC-GS-BRAND-E2E-013 | mock |
| TC-GS-BRAND-42 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-43 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-44 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-45 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-46 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-47 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-48 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-50 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-52 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-53 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-54 | TC-GS-BRAND-E2E-015 | FE+BE |
| TC-GS-BRAND-55 | TC-GS-BRAND-E2E-025 | FE+BE |
| TC-GS-BRAND-56 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-57 | TC-GS-BRAND-E2E-013 | mock |
| TC-GS-BRAND-58 | TC-GS-BRAND-E2E-013 | mock |
| TC-GS-BRAND-59 | TC-GS-BRAND-E2E-014 | mock |
| TC-GS-BRAND-60 | TC-GS-BRAND-E2E-014 | mock |
| TC-GS-BRAND-61 | TC-GS-BRAND-E2E-014 | mock |
| TC-GS-BRAND-62 | TC-GS-BRAND-E2E-014 | mock |
| TC-GS-BRAND-63 | TC-GS-BRAND-E2E-014 | mock |
| TC-GS-BRAND-64 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-65 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-66 | TC-GS-BRAND-E2E-070 | FE+BE |
| TC-GS-BRAND-67 | TC-GS-BRAND-E2E-070 | FE+BE |
| TC-GS-BRAND-68 | TC-GS-BRAND-E2E-012 | FE+BE |
| TC-GS-BRAND-69 | TC-GS-BRAND-E2E-018 | mock |
| TC-GS-BRAND-70 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-71 | TC-GS-BRAND-E2E-020 | FE+BE |
| TC-GS-BRAND-72 | TC-GS-BRAND-E2E-020 | FE+BE |
| TC-GS-BRAND-73 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-74 | TC-GS-BRAND-E2E-020 | FE+BE |
| TC-GS-BRAND-75 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-76 | TC-GS-BRAND-E2E-020 | FE+BE |
| TC-GS-BRAND-77 | TC-GS-BRAND-E2E-020 | FE+BE |
| TC-GS-BRAND-78 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-78 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-79 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-79 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-80 | TC-GS-BRAND-E2E-018 | mock |
| TC-GS-BRAND-81 | TC-GS-BRAND-E2E-018 | mock |
| TC-GS-BRAND-82 | TC-GS-BRAND-E2E-018 | mock |
| TC-GS-BRAND-83 | TC-GS-BRAND-E2E-019 | mock |
| TC-GS-BRAND-84 | TC-GS-BRAND-E2E-019 | mock |
| TC-GS-BRAND-85 | TC-GS-BRAND-E2E-019 | mock |
| TC-GS-BRAND-86 | TC-GS-BRAND-E2E-019 | mock |
| TC-GS-BRAND-87 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-88 | TC-GS-BRAND-E2E-021 | FE+BE |
| TC-GS-BRAND-89 | TC-GS-BRAND-E2E-070 | FE+BE |
| TC-GS-BRAND-90 | TC-GS-BRAND-E2E-025 | FE+BE |
| TC-GS-BRAND-91 | TC-GS-BRAND-E2E-012 | FE+BE |
| TC-GS-BRAND-92 | TC-GS-BRAND-E2E-022 | FE+BE |
| TC-GS-BRAND-93 | TC-GS-BRAND-E2E-022 | FE+BE |
| TC-GS-BRAND-94 | TC-GS-BRAND-E2E-022 | FE+BE |
| TC-GS-BRAND-95 | TC-GS-BRAND-E2E-024 | FE+BE |
| TC-GS-BRAND-96 | TC-GS-BRAND-E2E-023 | FE+BE |
| TC-GS-BRAND-97 | TC-GS-BRAND-E2E-023 | FE+BE |
| TC-GS-BRAND-98 | TC-GS-BRAND-E2E-022 | FE+BE |
| TC-GS-BRAND-99 | TC-GS-BRAND-E2E-023 | FE+BE |
| TC-GS-BRAND-100 | TC-GS-BRAND-E2E-023 | FE+BE |
| TC-GS-BRAND-101 | TC-GS-BRAND-E2E-023 | FE+BE |
| TC-GS-BRAND-102 | TC-GS-BRAND-E2E-027 | FE+BE |
| TC-GS-BRAND-103 | TC-GS-BRAND-E2E-026 | FE+BE |
| TC-GS-BRAND-104 | TC-GS-BRAND-E2E-071 | FE+BE |
| TC-GS-BRAND-105 | TC-GS-BRAND-E2E-071 | FE+BE |
| TC-GS-BRAND-106 | TC-GS-BRAND-E2E-024 | FE+BE |
| TC-GS-BRAND-107 | TC-GS-BRAND-E2E-012 | FE+BE |
| TC-GS-BRAND-108 | TC-GS-BRAND-E2E-028 | FE+BE |
| TC-GS-BRAND-109 | TC-GS-BRAND-E2E-028 | FE+BE |
| TC-GS-BRAND-110 | TC-GS-BRAND-E2E-028 | FE+BE |
| TC-GS-BRAND-111 | TC-GS-BRAND-E2E-028 | FE+BE |
| TC-GS-BRAND-112 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-113 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-114 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-115 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-116 | TC-GS-BRAND-E2E-030 | FE+BE |
| TC-GS-BRAND-117 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-118 | TC-GS-BRAND-E2E-030 | FE+BE |
| TC-GS-BRAND-119 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-120 | TC-GS-BRAND-E2E-027 | FE+BE |
| TC-GS-BRAND-121 | TC-GS-BRAND-E2E-027 | FE+BE |
| TC-GS-BRAND-122 | TC-GS-BRAND-E2E-027 | FE+BE |
| TC-GS-BRAND-123 | TC-GS-BRAND-E2E-026 | FE+BE |
| TC-GS-BRAND-124 | TC-GS-BRAND-E2E-071 | FE+BE |
| TC-GS-BRAND-125 | TC-GS-BRAND-E2E-030 | FE+BE |
| TC-GS-BRAND-126 | TC-GS-BRAND-E2E-028 | FE+BE |
| TC-GS-BRAND-127 | TC-GS-BRAND-E2E-031 | FE+BE |
| TC-GS-BRAND-128 | TC-GS-BRAND-E2E-031 | FE+BE |
| TC-GS-BRAND-129 | TC-GS-BRAND-E2E-012 | FE+BE |
| TC-GS-BRAND-130 | TC-GS-BRAND-E2E-035 | FE+BE |
| TC-GS-BRAND-131 | TC-GS-BRAND-E2E-035 | FE+BE |
| TC-GS-BRAND-133 | TC-GS-BRAND-E2E-035 | FE+BE |
| TC-GS-BRAND-134 | TC-GS-BRAND-E2E-035 | FE+BE |
| TC-GS-BRAND-135 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-141 | TC-GS-BRAND-E2E-037 | FE+BE |
| TC-GS-BRAND-142 | TC-GS-BRAND-E2E-037 | FE+BE |
| TC-GS-BRAND-143 | TC-GS-BRAND-E2E-037 | FE+BE |
| TC-GS-BRAND-144 | TC-GS-BRAND-E2E-037 | FE+BE |
| TC-GS-BRAND-145 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-146 | TC-GS-BRAND-E2E-038 | FE+BE |
| TC-GS-BRAND-147 | TC-GS-BRAND-E2E-038 | FE+BE |
| TC-GS-BRAND-148 | TC-GS-BRAND-E2E-038 | FE+BE |
| TC-GS-BRAND-149 | TC-GS-BRAND-E2E-039 | FE+BE |
| TC-GS-BRAND-150 | TC-GS-BRAND-E2E-037 | FE+BE |
| TC-GS-BRAND-151 | TC-GS-BRAND-E2E-016 | FE+BE |
| TC-GS-BRAND-152 | TC-GS-BRAND-E2E-039 | FE+BE |
| TC-GS-BRAND-153 | TC-GS-BRAND-E2E-003 | FE+BE |
| TC-GS-BRAND-154 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-155 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-156 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-157 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-158 | TC-GS-BRAND-E2E-041 | mock |
| TC-GS-BRAND-159 | TC-GS-BRAND-E2E-041 | mock |
| TC-GS-BRAND-160 | TC-GS-BRAND-E2E-041 | mock |
| TC-GS-BRAND-161 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-162 | TC-GS-BRAND-E2E-040 | mock |
| TC-GS-BRAND-163 | TC-GS-BRAND-E2E-047 | FE+BE |
| TC-GS-BRAND-164 | TC-GS-BRAND-E2E-047 | FE+BE |
| TC-GS-BRAND-165 | TC-GS-BRAND-E2E-047 | FE+BE |
| TC-GS-BRAND-166 | TC-GS-BRAND-E2E-047 | FE+BE |
| TC-GS-BRAND-167 | TC-GS-BRAND-E2E-006 | FE+BE |
| TC-GS-BRAND-168 | TC-GS-BRAND-E2E-050 | FE+BE |
| TC-GS-BRAND-169 | TC-GS-BRAND-E2E-050 | FE+BE |
| TC-GS-BRAND-170 | TC-GS-BRAND-E2E-004 | FE+BE |
| TC-GS-BRAND-171 | TC-GS-BRAND-E2E-004 | FE+BE |
| TC-GS-BRAND-172 | TC-GS-BRAND-E2E-005 | FE+BE |
| TC-GS-BRAND-173 | TC-GS-BRAND-E2E-050 | FE+BE |
| TC-GS-BRAND-174 | TC-GS-BRAND-E2E-050 | FE+BE |
| TC-GS-BRAND-175 | TC-GS-BRAND-E2E-051 | FE+BE |
| TC-GS-BRAND-176 | TC-GS-BRAND-E2E-051 | FE+BE |
| TC-GS-BRAND-177 | TC-GS-BRAND-E2E-051 | FE+BE |
| TC-GS-BRAND-178 | TC-GS-BRAND-E2E-051 | FE+BE |
| TC-GS-BRAND-179 | TC-GS-BRAND-E2E-053 | FE+BE |
| TC-GS-BRAND-180 | TC-GS-BRAND-E2E-053 | FE+BE |
| TC-GS-BRAND-181 | TC-GS-BRAND-E2E-053 | FE+BE |
| TC-GS-BRAND-182 | TC-GS-BRAND-E2E-048 | FE+BE |
| TC-GS-BRAND-183 | TC-GS-BRAND-E2E-006 | FE+BE |
| TC-GS-BRAND-184 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-185 | TC-GS-BRAND-E2E-005 | FE+BE |
| TC-GS-BRAND-186 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-187 | TC-GS-BRAND-E2E-057 | FE+BE |
| TC-GS-BRAND-188 | TC-GS-BRAND-E2E-057 | FE+BE |
| TC-GS-BRAND-189 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-190 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-191 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-192 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-193 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-194 | TC-GS-BRAND-E2E-048 | FE+BE |
| TC-GS-BRAND-195 | TC-GS-BRAND-E2E-006 | FE+BE |
| TC-GS-BRAND-196 | TC-GS-BRAND-E2E-058 | FE+BE |
| TC-GS-BRAND-197 | TC-GS-BRAND-E2E-049 | FE+BE |
| TC-GS-BRAND-198 | TC-GS-BRAND-E2E-057 | FE+BE |
| TC-GS-BRAND-199 | TC-GS-BRAND-E2E-057 | FE+BE |
| TC-GS-BRAND-201 | TC-GS-BRAND-E2E-056 | FE+BE |
| TC-GS-BRAND-202 | TC-GS-BRAND-E2E-056 | FE+BE |
| TC-GS-BRAND-203 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-204 | TC-GS-BRAND-E2E-043 | FE+BE |
| TC-GS-BRAND-205 | TC-GS-BRAND-E2E-063 | FE+BE |
| TC-GS-BRAND-206 | TC-GS-BRAND-E2E-060 | FE+BE |
| TC-GS-BRAND-207 | TC-GS-BRAND-E2E-060 | FE+BE |
| TC-GS-BRAND-208 | TC-GS-BRAND-E2E-060 | FE+BE |
| TC-GS-BRAND-209 | TC-GS-BRAND-E2E-061 | FE+BE |
| TC-GS-BRAND-210 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-211 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-212 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-213 | TC-GS-BRAND-E2E-075 | FE+BE |
| TC-GS-BRAND-214 | TC-GS-BRAND-E2E-060 | FE+BE |
| TC-GS-BRAND-215 | TC-GS-BRAND-E2E-061 | FE+BE |
| TC-GS-BRAND-216 | TC-GS-BRAND-E2E-063 | FE+BE |
| TC-GS-BRAND-217 | TC-GS-BRAND-E2E-063 | FE+BE |
| TC-GS-BRAND-218 | TC-GS-BRAND-E2E-063 | FE+BE |
| TC-GS-BRAND-219 | TC-GS-BRAND-E2E-066 | FE+BE |
| TC-GS-BRAND-220 | TC-GS-BRAND-E2E-064 | FE+BE |
| TC-GS-BRAND-221 | TC-GS-BRAND-E2E-065 | FE+BE |
| TC-GS-BRAND-223 | TC-GS-BRAND-E2E-046 | FE+BE |
| TC-GS-BRAND-224 | TC-GS-BRAND-E2E-046 | FE+BE |
| TC-GS-BRAND-225 | TC-GS-BRAND-E2E-067 | FE+BE |
| TC-GS-BRAND-226 | TC-GS-BRAND-E2E-068 | FE+BE |
| TC-GS-BRAND-227 | TC-GS-BRAND-E2E-068 | FE+BE |
| TC-GS-BRAND-227 | TC-GS-BRAND-E2E-075 | FE+BE |
| TC-GS-BRAND-228 | TC-GS-BRAND-E2E-069 | FE+BE |
| TC-GS-BRAND-229 | TC-GS-BRAND-E2E-069 | FE+BE |
| TC-GS-BRAND-230 | TC-GS-BRAND-E2E-068 | FE+BE |
| TC-GS-BRAND-231 | TC-GS-BRAND-E2E-068 | FE+BE |
| TC-GS-BRAND-232 | TC-GS-BRAND-E2E-032 | FE+BE |
| TC-GS-BRAND-233 | TC-GS-BRAND-E2E-032 | FE+BE |
| TC-GS-BRAND-234 | TC-GS-BRAND-E2E-033 | FE+BE |
| TC-GS-BRAND-235 | TC-GS-BRAND-E2E-034 | FE+BE |
| TC-GS-BRAND-236 | TC-GS-BRAND-E2E-025 | FE+BE |
| TC-GS-BRAND-237 | TC-GS-BRAND-E2E-025 | FE+BE |
| TC-GS-BRAND-239 | TC-GS-BRAND-E2E-072 | FE+BE |
| TC-GS-BRAND-240 | TC-GS-BRAND-E2E-072 | FE+BE |
| TC-GS-BRAND-241 | TC-GS-BRAND-E2E-073 | FE+BE |
| TC-GS-BRAND-242 | TC-GS-BRAND-E2E-074 | FE+BE (mobile) |
| TC-GS-BRAND-243 | TC-GS-BRAND-E2E-074 | FE+BE (mobile) |
| TC-GS-BRAND-244 | TC-GS-BRAND-E2E-072 | FE+BE |
| TC-GS-BRAND-245 | TC-GS-BRAND-E2E-064 | FE+BE |
| TC-GS-BRAND-246 | TC-GS-BRAND-E2E-064 | FE+BE |
| TC-GS-BRAND-247 | TC-GS-BRAND-E2E-065 | FE+BE |
| TC-GS-BRAND-248 | TC-GS-BRAND-E2E-064 | FE+BE |
| TC-GS-BRAND-249 | TC-GS-BRAND-E2E-006 | FE+BE |
| TC-GS-BRAND-251 | TC-GS-BRAND-E2E-058 | FE+BE |
| TC-GS-BRAND-252 | TC-GS-BRAND-E2E-029 | FE+BE |
| TC-GS-BRAND-253 | TC-GS-BRAND-E2E-070 | FE+BE |
| TC-GS-BRAND-254 | TC-GS-BRAND-E2E-001 | FE+BE |
| TC-GS-BRAND-255 | TC-GS-BRAND-E2E-058 | FE+BE |
| TC-GS-BRAND-256 | TC-GS-BRAND-E2E-066 | FE+BE |
| TC-GS-BRAND-257 | TC-GS-BRAND-E2E-066 | FE+BE |
| TC-GS-BRAND-258 | TC-GS-BRAND-E2E-071 | FE+BE |
| TC-GS-BRAND-259 | TC-GS-BRAND-E2E-057 | FE+BE |
| TC-GS-BRAND-260 | TC-GS-BRAND-E2E-058 | FE+BE |
| TC-GS-BRAND-261 | TC-GS-BRAND-E2E-002 | FE+BE |
| TC-GS-BRAND-262 | TC-GS-BRAND-E2E-054 | FE+BE |
| TC-GS-BRAND-263 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-264 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-265 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-266 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-267 | TC-GS-BRAND-E2E-002 | FE+BE |
| TC-GS-BRAND-268 | TC-GS-BRAND-E2E-042 | FE+BE |
| TC-GS-BRAND-269 | TC-GS-BRAND-E2E-042 | FE+BE |
| TC-GS-BRAND-270 | TC-GS-BRAND-E2E-043 | FE+BE |
| TC-GS-BRAND-271 | TC-GS-BRAND-E2E-042 | FE+BE |
| TC-GS-BRAND-272 | TC-GS-BRAND-E2E-044 | FE+BE |
| TC-GS-BRAND-273 | TC-GS-BRAND-E2E-038 | FE+BE |
| TC-GS-BRAND-274 | TC-GS-BRAND-E2E-035 | FE+BE |
| TC-GS-BRAND-275 | TC-GS-BRAND-E2E-065 | FE+BE |
| TC-GS-BRAND-276 | TC-GS-BRAND-E2E-065 | FE+BE |
| TC-GS-BRAND-277 | TC-GS-BRAND-E2E-065 | FE+BE |
| TC-GS-BRAND-278 | TC-GS-BRAND-E2E-036 | FE+BE |
| TC-GS-BRAND-279 | TC-GS-BRAND-E2E-045 | FE+BE |
| TC-GS-BRAND-280 | TC-GS-BRAND-E2E-042 | FE+BE |
| TC-GS-BRAND-281 | TC-GS-BRAND-E2E-052 | FE+BE |
| TC-GS-BRAND-282 | TC-GS-BRAND-E2E-052 | FE+BE |
| TC-GS-BRAND-283 | TC-GS-BRAND-E2E-052 | FE+BE |
| TC-GS-BRAND-284 | TC-GS-BRAND-E2E-051 | FE+BE |
| TC-GS-BRAND-285 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-286 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-287 | TC-GS-BRAND-E2E-055 | FE+BE |
| TC-GS-BRAND-288 | TC-GS-BRAND-E2E-059 | FE+BE |
| TC-GS-BRAND-289 | TC-GS-BRAND-E2E-059 | FE+BE |
| TC-GS-BRAND-290 | TC-GS-BRAND-E2E-059 | FE+BE |
| TC-GS-BRAND-291 | TC-GS-BRAND-E2E-026 | FE+BE |
| TC-GS-BRAND-292 | TC-GS-BRAND-E2E-062 | FE+BE |
| TC-GS-BRAND-293 | TC-GS-BRAND-E2E-032 | FE+BE |
| TC-GS-BRAND-294 | TC-GS-BRAND-E2E-049 | FE+BE |
