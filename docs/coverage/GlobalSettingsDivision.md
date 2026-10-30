# Coverage E2E — Global Settings > User > Division

Sumber: `global-settings/division/TestCases/tc-division.md` (301 ID `TC-GS-DIV-1`–`301`, seluruhnya aktif). Referensi kontrak: `global-settings/division/PRD/division.md`. Suite: `specs/GlobalSettings/Division/`. Prefix: `GS` + `DIV` (`TC-GS-DIV-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 301 TC aktif masuk spec, 0 TC hanya-BE (kontrak API murni berada di `tc-division-backend.md` dan tidak ada di `tc-division.md`; TC-259 sampai TC-270 dijalankan dari browser). 80 spec (76 FE+BE, 4 mock). Setiap TC terpetakan ke satu spec, kecuali TC-99, TC-100, dan TC-288 yang sengaja terbelah (prinsip 10 dan S-05): aksi dan hasil Edit di spec 028, asersi tidak ada entri log baru di spec 067.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel | Screening Tab Division: Layout, Urutan Default Name A-Z, Tooltip Table Tools, dan Isi Sel | FE+BE | 41 | 1, 2, 3, 4 |
| TC-GS-DIV-E2E-002-resilience-baca-loading-error-dan-try-again | Resilience Baca Tab Division: Loading, Error Load, dan Try Again | FE+BE | 17 | 5, 8, 9 |
| TC-GS-DIV-E2E-003-empty-state-tabel-pencarian-dan-filter | Empty State Tabel Division: Search dan Filter Tanpa Hasil | FE+BE | 14 | 6, 7 |
| TC-GS-DIV-E2E-004-guided-tooltip-konten-dan-navigasi-keyboard | Guided Tooltip Tab Division: Konten 3 Step dan Navigasi Keyboard | mock | 24 | 10, 16 |
| TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | Guided Tooltip Tab Division: Flag Seen, Skip, Overlay, Done, Replay, dan Resize | FE+BE | 44 | 11, 12, 13, 14, 15 |
| TC-GS-DIV-E2E-006-guided-tooltip-step-add-division-dilewati-read-only | Guided Tooltip Tab Division: Step Add Division Dilewati bagi Read Only | FE+BE | 7 | 17 |
| TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Division per Role | FE+BE | 71 | 18, 19, 20, 21, 22, 23, 24 |
| TC-GS-DIV-E2E-008-role-matrix-negatif-direct-url-tanpa-capability | Role Matrix Negatif: Akses Langsung Tab Division Tanpa Capability | FE+BE | 8 | 25 |
| TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability | FE+BE | 32 | 26, 27, 28, 29 |
| TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | Create Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup Bersih | mock | 41 | 31, 32, 63, 64, 67 |
| TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | Create Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat) | FE+BE | 46 | 34, 35, 38, 39, 40, 41, 42 |
| TC-GS-DIV-E2E-012-create-validasi-code-batas-karakter-whitelist-dan-duplikat | Create Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat) | FE+BE | 18 | 45, 46, 48 |
| TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | Create Division Sukses: Trim Name, Batas 120/15 Karakter, Code Uppercase, dan Whitelist | FE+BE | 29 | 36, 37, 43, 44, 47 |
| TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | Create Division Sukses: Saving State, Stay on Form, Code Spasi Saja, dan Klik Ganda | FE+BE | 44 | 33, 49, 65, 66, 78 |
| TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | Auto-Generate Code: Inisial Token, Numerik, Alfanumerik Campuran, dan Delimiter | FE+BE | 29 | 50, 51, 52, 53, 54 |
| TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive | Auto-Generate Code: Fallback 6 Karakter, DIV pada Simbol dan Non-Latin, dan Unik Case-Insensitive | FE+BE | 25 | 55, 56, 57, 62 |
| TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation | Auto-Generate Code: Dedup Suffix Angka dan Pemotongan 15 Karakter | FE+BE | 24 | 58, 59, 60, 61 |
| TC-GS-DIV-E2E-018-create-population-26-division-stay-on-form | Create Population: 26 Division Berurutan dengan Stay on Form | FE+BE | 70 | 30 |
| TC-GS-DIV-E2E-019-create-unsaved-changes-dialog | Create Division: Dialog Unsaved Changes (X, Esc, Cancel, Leave, Backdrop) | mock | 33 | 68, 69, 70, 71 |
| TC-GS-DIV-E2E-020-create-limit-master-data-count-dan-dialog-limit-reached | Create Division: Master Data Count Limit dan Dialog Limit Reached | FE+BE | 40 | 72, 73, 75 |
| TC-GS-DIV-E2E-021-create-race-slot-terakhir-dua-admin | Create Division: Race Slot Terakhir antara Dua Admin | FE+BE | 42 | 74, 274 |
| TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama | Konflik Create Dua Admin: Code Auto-Generate Identik, Name Sama, dan Code Manual Sama | FE+BE | 77 | 272, 273, 80, 79 |
| TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | Edit Division: Screening Popup, Aksesibilitas, Clear Field, dan Tutup | mock | 46 | 81, 291, 105, 106, 107, 108 |
| TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | Edit Division: Validasi Name (Kosong, Spasi, 121 Karakter, Emoji, Duplikat, Nilai Sendiri) | FE+BE | 50 | 83, 84, 87, 88, 89, 90, 91, 92 |
| TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat | Edit Division: Validasi Code (16 Karakter, Simbol Terlarang, Duplikat, Nilai Sendiri) | FE+BE | 31 | 94, 95, 96, 97 |
| TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | Edit Division Sukses: Saving State, Trim Name, Batas 120 Karakter, Hanya Name, dan Klik Ganda | FE+BE | 51 | 82, 85, 86, 101, 112 |
| TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | Edit Division Sukses: Code Uppercase, Hanya Code, Name dan Code, Division Seed, dan Rename | FE+BE | 39 | 93, 102, 103, 109, 104 |
| TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op | Edit Division: Code Dikosongkan, Auto-Generate, dan Save Tanpa Perubahan | FE+BE | 38 | 99, 288, 100, 98 |
| TC-GS-DIV-E2E-029-konflik-edit-dua-admin-last-write-wins | Konflik Edit Dua Admin: Last-Write-Wins dan Field Berbeda | FE+BE | 35 | 271, 301 |
| TC-GS-DIV-E2E-030-konflik-edit-vs-delete-record-dihapus-pihak-lain | Konflik Edit vs Delete dan Bulk Delete: Record Dihapus Pihak Lain | FE+BE | 39 | 113, 275, 276 |
| TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda | Delete Division Single: Screening Dialog, Cancel, Sukses, dan Klik Ganda | FE+BE | 30 | 114, 115, 116, 124 |
| TC-GS-DIV-E2E-032-delete-single-blokir-in-use | Delete Division Single: Diblokir karena In-Use (Login Aktif, Non-Aktif, Non-Login User) | FE+BE | 33 | 117, 118, 119, 120 |
| TC-GS-DIV-E2E-033-konflik-delete-in-use-saat-confirm-dan-sudah-dihapus | Konflik Delete: Berubah In-Use Saat Confirm dan Sudah Dihapus Pihak Lain | FE+BE | 19 | 121, 122 |
| TC-GS-DIV-E2E-034-delete-katalog-terakhir-otomatis-in-use | Delete Division: Katalog Tidak Pernah Turun ke Nol | FE+BE | 9 | 279 |
| TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi | FE+BE | 37 | 125, 126, 127, 128, 160 |
| TC-GS-DIV-E2E-036-selection-limit-checkbox-dan-select-all | Selection Limit: Checkbox Disabled dan Select All Dibatasi | FE+BE | 25 | 129, 130 |
| TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel | Bulk Delete Homogen: Dialog, Confirm, Cancel, dan Satu Baris | FE+BE | 38 | 131, 132, 133, 137 |
| TC-GS-DIV-E2E-038-bulk-delete-campuran-dialog-continue-dan-cancel | Bulk Delete Campuran: Dialog Dua Kelompok, Continue, dan Cancel | FE+BE | 33 | 134, 135, 287 |
| TC-GS-DIV-E2E-039-bulk-delete-blokir-seluruhnya-atau-satu-in-use | Bulk Delete Diblokir: Seluruhnya In-Use dan Satu Baris In-Use | FE+BE | 20 | 136, 138 |
| TC-GS-DIV-E2E-040-bulk-delete-race-item-menjadi-in-use | Bulk Delete Race: Item Menjadi In-Use Setelah Pre-Check dan Saat Confirm | FE+BE | 27 | 139, 296 |
| TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | Search Toolbar Tabel Division: Reveal, Clear, Kolom Searchable, dan Reset Halaman | FE+BE | 44 | 141, 142, 143, 144, 145, 148 |
| TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman | Filter Panel Tabel Division: Screening, Last Updated, Clear Field, dan Reset Halaman | FE+BE | 28 | 149, 150, 152, 169 |
| TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | Kombinasi Search, Filter, Sort, dan Pagination Tabel Division | FE+BE | 55 | 153, 154, 155, 156, 157, 158, 159 |
| TC-GS-DIV-E2E-044-search-aktif-terhadap-create-dan-edit-division | Search Aktif terhadap Create dan Edit Division | FE+BE | 22 | 161, 162 |
| TC-GS-DIV-E2E-045-sort-3-state-name-code-last-updated | Sort 3-State Tabel Division: Name, Code, Last Updated | FE+BE | 20 | 163, 164, 165 |
| TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh | Pagination Tabel Division: Page Size, Navigasi, dan Retensi Refresh | FE+BE | 36 | 166, 167, 168, 170 |
| TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | Setup Column Tabel Division: Screening, Hide/Unhide, Tutup Tanpa Simpan, dan Kolom Visible Terakhir | FE+BE | 58 | 171, 172, 173, 177, 178 |
| TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | Setup Column Tabel Division: Reorder, Pin, Reset, dan Search terhadap Kolom Hidden | FE+BE | 64 | 174, 175, 176, 146, 147 |
| TC-GS-DIV-E2E-049-isolasi-konfigurasi-kolom-tabel-division-dan-modal-changelog | Isolasi Konfigurasi Kolom: Tabel Division dan Modal Changelog | FE+BE | 20 | 179, 234 |
| TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | Download Tabel Division: Menu, Isi File, Search/Filter Aktif, dan Kolom Visible | FE+BE | 43 | 180, 181, 182, 183, 184, 185, 187 |
| TC-GS-DIV-E2E-051-resilience-export-gagal-download-tabel-dan-changelog | Resilience Export: Kegagalan Download Tabel Division dan Changelog | FE+BE | 13 | 186, 223 |
| TC-GS-DIV-E2E-052-format-tanggal-general-settings-filter-dan-changelog | Format Tanggal General Settings pada Filter Tabel dan Modal Changelog | FE+BE | 17 | 151, 212 |
| TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | Modal Changelog: Screening, Format Sel, Urutan Default, Tooltip Toolbar, Nilai Panjang, dan Tutup | FE+BE | 40 | 188, 189, 190, 224, 211, 230 |
| TC-GS-DIV-E2E-054-changelog-empty-state | Modal Changelog: Empty State Belum Ada Riwayat dan Search Tanpa Hasil | FE+BE | 13 | 191, 192 |
| TC-GS-DIV-E2E-055-changelog-search-kolom-searchable-dan-kontrol | Modal Changelog: Search Kolom Searchable dan Kontrol Search | FE+BE | 36 | 193, 194, 225 |
| TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | Modal Changelog: Filter Panel Screening dan Sumber Opsi Dropdown | FE+BE | 47 | 195, 196, 197, 231, 232 |
| TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | Modal Changelog: Filter Date dan Multi-Select, Logika OR/AND, serta Kombinasi dengan Search dan Sort | FE+BE | 83 | 198, 199, 200, 201, 205, 226, 227, 228, 229 |
| TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | Modal Changelog: Chip Filter, Search di Dropdown, dan Overflow Chip | FE+BE | 98 | 202, 203, 204, 233, 292, 293, 294, 295 |
| TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong | Modal Changelog: Sort 3-State dan Nilai Kosong pada Old/New Value | FE+BE | 39 | 206, 207, 208, 209 |
| TC-GS-DIV-E2E-060-changelog-pagination-page-size | Modal Changelog: Pagination dan Page Size | FE+BE | 11 | 210 |
| TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | Setup Column Modal Changelog: Screening, Hide/Unhide, Tutup dengan X, dan Kolom Visible Terakhir | FE+BE | 60 | 213, 214, 215, 219, 220 |
| TC-GS-DIV-E2E-062-setup-column-changelog-reorder-pin-dan-reset | Setup Column Modal Changelog: Reorder, Pin/Unpin, dan Reset to Default | FE+BE | 76 | 216, 217, 218 |
| TC-GS-DIV-E2E-063-download-changelog-isi-file | Download Changelog: Isi File Tanpa dan Dengan Filter | FE+BE | 12 | 221, 222 |
| TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | Pencatatan Changelog: Entri Create dan Edit (Name, Code, Name+Code, Rename) | FE+BE | 54 | 235, 236, 237, 238, 239, 241, 245, 249 |
| TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete | Pencatatan Changelog: Entri Delete dan Bulk Delete | FE+BE | 14 | 242, 243 |
| TC-GS-DIV-E2E-066-modified-by-aktor-pelaksana-tiap-aksi | Pencatatan Changelog: Modified By Mencatat Aktor Pelaksana | FE+BE | 19 | 246 |
| TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | Absence Log: Edit Tanpa Perubahan dan Division In-Use Dilewati Tidak Menghasilkan Entri | FE+BE | 34 | 240, 244, 300, 99, 100, 288 |
| TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | Pencatatan Tab System Log Aktor dan Activity Log Global Settings | FE+BE | 34 | 247, 248, 297, 298, 299 |
| TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user | Sinkron Dropdown Division di Form User dan Non-Login User (Create, Rename, Delete) | FE+BE | 28 | 250, 251, 252, 253 |
| TC-GS-DIV-E2E-070-form-user-dan-non-login-user-division-dihapus-pihak-lain | Form User dan Non-Login User: Division Terpilih Dihapus Pihak Lain | FE+BE | 32 | 254, 255 |
| TC-GS-DIV-E2E-071-import-create-missing-divisions-edit-delete-dan-log | Import Create Missing Divisions: Edit, Delete In-Use, dan Pencatatan Create | FE+BE | 22 | 256, 257, 258 |
| TC-GS-DIV-E2E-072-import-create-missing-divisions-limit-dan-race | Import Create Missing Divisions: Master Data Count Limit dan Duplicate Race | FE+BE | 26 | 289, 290 |
| TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | Defense-in-Depth: Request Langsung Tanpa Capability, Guard In-Use, Validasi Server, XSS, dan SQL Injection | FE+BE | 71 | 259, 260, 261, 262, 267, 268, 269, 270 |
| TC-GS-DIV-E2E-074-state-tenant-write-lockdown-suspended-dan-expired | State Tenant: Create, Edit, dan Delete Ditolak saat Entitas Suspended atau Expired | FE+BE | 36 | 263, 264, 265 |
| TC-GS-DIV-E2E-075-isolasi-data-entitas-lain | Isolasi Data: Division Entitas Lain Tidak Terlihat | FE+BE | 15 | 266 |
| TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | Resilience Tulis: Create, Edit, Delete, dan Bulk Delete Gagal 5xx atau Timeout | FE+BE | 70 | 76, 77, 110, 111, 123, 140 |
| TC-GS-DIV-E2E-077-realtime-perubahan-admin-lain-pada-tabel-terbuka | Realtime: Create dan Rename dari Admin Lain Tampil Otomatis di Tabel Terbuka | FE+BE | 12 | 277, 278 |
| TC-GS-DIV-E2E-078-tanpa-gating-plan-create-edit-delete-semua-tier | Tanpa Gating Plan: Create, Edit, dan Delete Identik di Semua Tier | FE+BE | 20 | 280 |
| TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet | Mobile: Screening Halaman, Card List, Row Action, dan Bottom Sheet | FE+BE | 31 | 281, 282, 283, 284 |
| TC-GS-DIV-E2E-080-mobile-create-dan-edit-division | Mobile: Create dan Edit Division | FE+BE | 16 | 285, 286 |

## Pembagian TC lintas spec

- **TC-GS-DIV-99, 100, 288**: aksi dan hasil Edit (Code dikosongkan, Save tanpa perubahan) di spec `028`; asersi tidak ada entri log baru di Changelog, Activity Log, dan Tab System Log aktor di spec `067` (kelas g, dengan aksi nyata dan baseline sendiri).
- **TC-GS-DIV-240, 244, 300**: aksi dan asersi absence di spec `067`.
- **TC-GS-DIV-287 butir c** (tidak ada entri log baru) ditulis di spec `038` sebagai selisih jumlah entri Changelog terhadap baseline; TC-287 tidak ada di `sourceTc` spec `067`.
- **TC-GS-DIV-296 Post Condition** (Changelog dan Activity Log tanpa entri Delete baru) tidak punya langkah observasi di TC dan tidak diasersi (spec `040`).
- **TC-GS-DIV-299 butir b** (spec `068`) dan **TC-GS-DIV-289 butir c** (spec `072`): asersi absence ditulis sebagai `Verifikasi` berbaseline di spec asal dengan butir `P-1` di Notes; TC-nya tidak ada di `sourceTc` spec `067`.
- **TC-GS-DIV-30** (Population 26 Division lewat UI) di spec `018`; spec lain yang membutuhkan Population men-seed lewat API secara idempotent di hook `before`.
- **TC-GS-DIV-1, 3, 4** di spec `001`: tabel memuat 33 baris (6 Pre-setup + 26 Population + D-03 120 karakter) agar TC-3 dan TC-4 berjalan dalam satu spec; Name D-03 berawalan `Zzz` supaya urutan halaman 1-3 tidak bergeser.
- **TC-GS-DIV-72, 73, 75** di spec `020` dijalankan berurutan 75, 72, 73 supaya Master Data Count Limit cukup diatur sekali di hook `before`.
- **TC-GS-DIV-109** (rename tercermin di tabel) di spec `027`; Post Condition rename pada dropdown User tidak diasersi di sana dan diuji di spec `069` (TC-252).
- **TC-GS-DIV-179 dan 234** (isolasi konfigurasi kolom tabel Division dan Modal Changelog) bersama di spec `049`; Setup Column tabel di spec `047` dan `048`, Setup Column Modal Changelog di spec `061` dan `062`.
- **TC-GS-DIV-151 dan 212** (format tanggal General Settings) di spec `052`; TC-187 (format tanggal di isi file) di spec `050`.
- **TC-GS-DIV-146, 147** (Search terhadap kolom hidden) di spec `048` karena memakai konfigurasi Setup Column.

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec dan sudah terdaftar di `spectra.config.ts` dan `.env.example`: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`. Belum terdaftar: `GS_ONEDIV_TC_PASSWORD` (spec 034, TC-279).
- Akun di luar Tabel Pre-setup TC Division (mengikuti suite Brand, disediakan tim FE): Total Control admin kedua Client A (`totalControlSecond_automated_qaTeam1@qwertysystem.net`, `GS_TC2_PASSWORD`; dipakai spec konflik dua admin dan realtime), Total Control Principal, Total Control Client B (spec 075) dan Client C (spec 054), serta akun entitas dengan tepat 1 Division in-use (spec 034).
- Fixture data baru: `fixtures/division.json` (nilai field wajib lain untuk user dan Non-Login User uji, Division `soleDivision`), seeding Division dan Login User lewat API, draft Staging Table Import User Login lewat API (spec 071, 072).
- Kemampuan teknis: intercept jaringan (500, timeout, tahan respons), dua sesi browser paralel, mengubah Master Data Count Limit dan Selection Limit lewat Admin Console > Plans & Licensing > Lifecycle Settings > System Limits, mengubah plan dan status Client (Suspended, Expired) lewat API, mengubah format tanggal General Settings, membaca dan menyetel flag Guided Tooltip `guided_tooltip_seen_gs-division`, menangkap dan membaca berkas unduhan CSV/XLSX, mengirim request HTTP langsung dari konteks browser, memanipulasi viewport, perangkat atau emulator Android (spec 079, 080).
- Environment automation harus terisolasi dari aktivitas pengguna lain agar asersi himpunan (opsi filter Modified By, jumlah baris 32/33) stabil, dan suite berjalan serial.
- Baris Pre-setup tidak diubah atau dihapus spec mana pun (TC-104 mengedit Division seed `Seed Edit`); Last Updated keenam Division Pre-setup identik menurut Tabel Data Uji Pre-setup TC, dan spec 042, 043, 045, 050, dan 052 membacanya dari baris Finance.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division` diatur sekali di hook suite (`suite.md`, bagian Hook suite) untuk spec non-tooltip; kemampuan membaca dan menyetel flag disediakan tim FE/BE.

## Temuan yang masih terbuka

- Spec melewati batas ±35 langkah dengan satu kelas harness dan alasan di Notes (36 spec): 058 (98), 057 (83), 022 (77), 062 (76), 007 (71), 073 (71), 018 (70), 076 (70), 048 (64), 061 (60), 047 (58), 043 (55), 064 (54), 026 (51), 024 (50), 056 (47), 011 (46), 023 (46), 005 (44), 014 (44), 041 (44), 050 (43), 021 (42), 001 (41), 010 (41), 020 (40), 053 (40), 027 (39), 030 (39), 059 (39), 028 (38), 037 (38), 035 (37), 046 (36), 055 (36), 074 (36).
- TC-30: spec 018 mengasersi Expected b (modal tetap terbuka, field kosong, fokus, checkbox) hanya di Submit pertama dan terakhir; Expected a (toast) di tiap Submit.
- TC-1 (hanya 6 Division Pre-setup) dan TC-3 (32 baris) bertentangan pada jumlah baris; spec 001 memakai 32 baris untuk keduanya.
- Precondition atau cara pengamatan tidak dinyatakan: surface log TC-124, state awal seleksi TC-126 sampai 128, nilai awal Selection Limit TC-129 dan 130, entitas dengan tepat 1 Division TC-279; rinciannya di Notes tiap spec.
- TC-290 Expected b (baris tetap error) bertentangan dengan PRD Import `IMP-LOGIC-11` butir 3 (pulih ke pending); spec 072 mengikuti TC.
- Untuk pemilik PRD (tidak diubah): PRD `division.md` menamai header Modal Changelog `Actions (⋯)` sedangkan TC memakai `Column Visibility (⋯)` (spec mengikuti TC, spec 049 dan 053); PRD User tidak mendefinisikan pencarian di dropdown Division form Create User (spec 069 dan 070 mengamati opsi tanpa mengetik pencarian).
- Post Condition tanpa langkah observasi tidak diasersi (antara lain TC-105, 117, 118, 119, 136, 138, 245, 268, 296); dicatat di "Temuan untuk QA" tiap spec.
- Mekanisme yang tidak didefinisikan TC, PRD, atau LLD ditulis sebagai kemampuan "disediakan tim FE/BE" tanpa mengarang endpoint: membaca atau menghapus flag Guided Tooltip, mengubah System Limits, mengubah plan dan status Client, seeding yang menulis entri Changelog, menangkap berkas unduhan.
- TC-80: cara memicu bentrok Code `QRT2` antara percobaan pertama dan retry tidak disebut TC (spec 022).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-DIV-1 | TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel | FE+BE |
| TC-GS-DIV-2 | TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel | FE+BE |
| TC-GS-DIV-3 | TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel | FE+BE |
| TC-GS-DIV-4 | TC-GS-DIV-E2E-001-screening-tab-division-layout-urutan-default-dan-isi-sel | FE+BE |
| TC-GS-DIV-5 | TC-GS-DIV-E2E-002-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-DIV-6 | TC-GS-DIV-E2E-003-empty-state-tabel-pencarian-dan-filter | FE+BE |
| TC-GS-DIV-7 | TC-GS-DIV-E2E-003-empty-state-tabel-pencarian-dan-filter | FE+BE |
| TC-GS-DIV-8 | TC-GS-DIV-E2E-002-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-DIV-9 | TC-GS-DIV-E2E-002-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-DIV-10 | TC-GS-DIV-E2E-004-guided-tooltip-konten-dan-navigasi-keyboard | mock |
| TC-GS-DIV-11 | TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | FE+BE |
| TC-GS-DIV-12 | TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | FE+BE |
| TC-GS-DIV-13 | TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | FE+BE |
| TC-GS-DIV-14 | TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | FE+BE |
| TC-GS-DIV-15 | TC-GS-DIV-E2E-005-guided-tooltip-flag-seen-skip-overlay-done-replay-dan-resize | FE+BE |
| TC-GS-DIV-16 | TC-GS-DIV-E2E-004-guided-tooltip-konten-dan-navigasi-keyboard | mock |
| TC-GS-DIV-17 | TC-GS-DIV-E2E-006-guided-tooltip-step-add-division-dilewati-read-only | FE+BE |
| TC-GS-DIV-18 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-19 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-20 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-21 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-22 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-23 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-24 | TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-DIV-25 | TC-GS-DIV-E2E-008-role-matrix-negatif-direct-url-tanpa-capability | FE+BE |
| TC-GS-DIV-26 | TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-DIV-27 | TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-DIV-28 | TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-DIV-29 | TC-GS-DIV-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-DIV-30 | TC-GS-DIV-E2E-018-create-population-26-division-stay-on-form | FE+BE |
| TC-GS-DIV-31 | TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | mock |
| TC-GS-DIV-32 | TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | mock |
| TC-GS-DIV-33 | TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | FE+BE |
| TC-GS-DIV-34 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-35 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-36 | TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | FE+BE |
| TC-GS-DIV-37 | TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | FE+BE |
| TC-GS-DIV-38 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-39 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-40 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-41 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-42 | TC-GS-DIV-E2E-011-create-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-43 | TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | FE+BE |
| TC-GS-DIV-44 | TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | FE+BE |
| TC-GS-DIV-45 | TC-GS-DIV-E2E-012-create-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-46 | TC-GS-DIV-E2E-012-create-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-47 | TC-GS-DIV-E2E-013-create-sukses-name-code-trim-batas-dan-whitelist | FE+BE |
| TC-GS-DIV-48 | TC-GS-DIV-E2E-012-create-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-49 | TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | FE+BE |
| TC-GS-DIV-50 | TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | FE+BE |
| TC-GS-DIV-51 | TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | FE+BE |
| TC-GS-DIV-52 | TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | FE+BE |
| TC-GS-DIV-53 | TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | FE+BE |
| TC-GS-DIV-54 | TC-GS-DIV-E2E-015-create-auto-generate-code-inisial-numerik-dan-delimiter | FE+BE |
| TC-GS-DIV-55 | TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive | FE+BE |
| TC-GS-DIV-56 | TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive | FE+BE |
| TC-GS-DIV-57 | TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive | FE+BE |
| TC-GS-DIV-58 | TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-59 | TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-60 | TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-61 | TC-GS-DIV-E2E-017-create-auto-generate-code-dedup-suffix-dan-truncation | FE+BE |
| TC-GS-DIV-62 | TC-GS-DIV-E2E-016-create-auto-generate-code-fallback-simbol-non-latin-dan-case-insensitive | FE+BE |
| TC-GS-DIV-63 | TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | mock |
| TC-GS-DIV-64 | TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | mock |
| TC-GS-DIV-65 | TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | FE+BE |
| TC-GS-DIV-66 | TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | FE+BE |
| TC-GS-DIV-67 | TC-GS-DIV-E2E-010-create-screening-aksesibilitas-clear-field-dan-tutup-bersih | mock |
| TC-GS-DIV-68 | TC-GS-DIV-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-DIV-69 | TC-GS-DIV-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-DIV-70 | TC-GS-DIV-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-DIV-71 | TC-GS-DIV-E2E-019-create-unsaved-changes-dialog | mock |
| TC-GS-DIV-72 | TC-GS-DIV-E2E-020-create-limit-master-data-count-dan-dialog-limit-reached | FE+BE |
| TC-GS-DIV-73 | TC-GS-DIV-E2E-020-create-limit-master-data-count-dan-dialog-limit-reached | FE+BE |
| TC-GS-DIV-74 | TC-GS-DIV-E2E-021-create-race-slot-terakhir-dua-admin | FE+BE |
| TC-GS-DIV-75 | TC-GS-DIV-E2E-020-create-limit-master-data-count-dan-dialog-limit-reached | FE+BE |
| TC-GS-DIV-76 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-77 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-78 | TC-GS-DIV-E2E-014-create-sukses-saving-state-stay-on-form-code-spasi-dan-klik-ganda | FE+BE |
| TC-GS-DIV-79 | TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama | FE+BE |
| TC-GS-DIV-80 | TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama | FE+BE |
| TC-GS-DIV-81 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-82 | TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | FE+BE |
| TC-GS-DIV-83 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-84 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-85 | TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | FE+BE |
| TC-GS-DIV-86 | TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | FE+BE |
| TC-GS-DIV-87 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-88 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-89 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-90 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-91 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-92 | TC-GS-DIV-E2E-024-edit-validasi-name-batas-karakter-emoji-dan-duplikat | FE+BE |
| TC-GS-DIV-93 | TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | FE+BE |
| TC-GS-DIV-94 | TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-95 | TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-96 | TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-97 | TC-GS-DIV-E2E-025-edit-validasi-code-batas-karakter-whitelist-dan-duplikat | FE+BE |
| TC-GS-DIV-98 | TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op | FE+BE |
| TC-GS-DIV-99 | TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op | FE+BE |
| TC-GS-DIV-99 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-100 | TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op | FE+BE |
| TC-GS-DIV-100 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-101 | TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | FE+BE |
| TC-GS-DIV-102 | TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | FE+BE |
| TC-GS-DIV-103 | TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | FE+BE |
| TC-GS-DIV-104 | TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | FE+BE |
| TC-GS-DIV-105 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-106 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-107 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-108 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-109 | TC-GS-DIV-E2E-027-edit-sukses-code-name-dan-code-sekaligus-pre-setup-dan-rename | FE+BE |
| TC-GS-DIV-110 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-111 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-112 | TC-GS-DIV-E2E-026-edit-sukses-name-saving-state-trim-batas-dan-klik-ganda | FE+BE |
| TC-GS-DIV-113 | TC-GS-DIV-E2E-030-konflik-edit-vs-delete-record-dihapus-pihak-lain | FE+BE |
| TC-GS-DIV-114 | TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-DIV-115 | TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-DIV-116 | TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-DIV-117 | TC-GS-DIV-E2E-032-delete-single-blokir-in-use | FE+BE |
| TC-GS-DIV-118 | TC-GS-DIV-E2E-032-delete-single-blokir-in-use | FE+BE |
| TC-GS-DIV-119 | TC-GS-DIV-E2E-032-delete-single-blokir-in-use | FE+BE |
| TC-GS-DIV-120 | TC-GS-DIV-E2E-032-delete-single-blokir-in-use | FE+BE |
| TC-GS-DIV-121 | TC-GS-DIV-E2E-033-konflik-delete-in-use-saat-confirm-dan-sudah-dihapus | FE+BE |
| TC-GS-DIV-122 | TC-GS-DIV-E2E-033-konflik-delete-in-use-saat-confirm-dan-sudah-dihapus | FE+BE |
| TC-GS-DIV-123 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-124 | TC-GS-DIV-E2E-031-delete-single-screening-cancel-sukses-dan-klik-ganda | FE+BE |
| TC-GS-DIV-125 | TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-DIV-126 | TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-DIV-127 | TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-DIV-128 | TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-DIV-129 | TC-GS-DIV-E2E-036-selection-limit-checkbox-dan-select-all | FE+BE |
| TC-GS-DIV-130 | TC-GS-DIV-E2E-036-selection-limit-checkbox-dan-select-all | FE+BE |
| TC-GS-DIV-131 | TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel | FE+BE |
| TC-GS-DIV-132 | TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel | FE+BE |
| TC-GS-DIV-133 | TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel | FE+BE |
| TC-GS-DIV-134 | TC-GS-DIV-E2E-038-bulk-delete-campuran-dialog-continue-dan-cancel | FE+BE |
| TC-GS-DIV-135 | TC-GS-DIV-E2E-038-bulk-delete-campuran-dialog-continue-dan-cancel | FE+BE |
| TC-GS-DIV-136 | TC-GS-DIV-E2E-039-bulk-delete-blokir-seluruhnya-atau-satu-in-use | FE+BE |
| TC-GS-DIV-137 | TC-GS-DIV-E2E-037-bulk-delete-homogen-screening-confirm-dan-cancel | FE+BE |
| TC-GS-DIV-138 | TC-GS-DIV-E2E-039-bulk-delete-blokir-seluruhnya-atau-satu-in-use | FE+BE |
| TC-GS-DIV-139 | TC-GS-DIV-E2E-040-bulk-delete-race-item-menjadi-in-use | FE+BE |
| TC-GS-DIV-140 | TC-GS-DIV-E2E-076-resilience-tulis-create-edit-delete-bulk-delete-5xx-dan-timeout | FE+BE |
| TC-GS-DIV-141 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-142 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-143 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-144 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-145 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-146 | TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | FE+BE |
| TC-GS-DIV-147 | TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | FE+BE |
| TC-GS-DIV-148 | TC-GS-DIV-E2E-041-search-toolbar-reveal-clear-kolom-searchable-dan-reset-halaman | FE+BE |
| TC-GS-DIV-149 | TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman | FE+BE |
| TC-GS-DIV-150 | TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman | FE+BE |
| TC-GS-DIV-151 | TC-GS-DIV-E2E-052-format-tanggal-general-settings-filter-dan-changelog | FE+BE |
| TC-GS-DIV-152 | TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman | FE+BE |
| TC-GS-DIV-153 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-154 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-155 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-156 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-157 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-158 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-159 | TC-GS-DIV-E2E-043-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-DIV-160 | TC-GS-DIV-E2E-035-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-DIV-161 | TC-GS-DIV-E2E-044-search-aktif-terhadap-create-dan-edit-division | FE+BE |
| TC-GS-DIV-162 | TC-GS-DIV-E2E-044-search-aktif-terhadap-create-dan-edit-division | FE+BE |
| TC-GS-DIV-163 | TC-GS-DIV-E2E-045-sort-3-state-name-code-last-updated | FE+BE |
| TC-GS-DIV-164 | TC-GS-DIV-E2E-045-sort-3-state-name-code-last-updated | FE+BE |
| TC-GS-DIV-165 | TC-GS-DIV-E2E-045-sort-3-state-name-code-last-updated | FE+BE |
| TC-GS-DIV-166 | TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh | FE+BE |
| TC-GS-DIV-167 | TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh | FE+BE |
| TC-GS-DIV-168 | TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh | FE+BE |
| TC-GS-DIV-169 | TC-GS-DIV-E2E-042-filter-panel-last-updated-clear-field-dan-reset-halaman | FE+BE |
| TC-GS-DIV-170 | TC-GS-DIV-E2E-046-pagination-page-size-navigasi-dan-retensi-refresh | FE+BE |
| TC-GS-DIV-171 | TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-172 | TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-173 | TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-174 | TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | FE+BE |
| TC-GS-DIV-175 | TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | FE+BE |
| TC-GS-DIV-176 | TC-GS-DIV-E2E-048-setup-column-tabel-reorder-pin-reset-dan-search-kolom-hidden | FE+BE |
| TC-GS-DIV-177 | TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-178 | TC-GS-DIV-E2E-047-setup-column-tabel-screening-hide-unhide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-179 | TC-GS-DIV-E2E-049-isolasi-konfigurasi-kolom-tabel-division-dan-modal-changelog | FE+BE |
| TC-GS-DIV-180 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-181 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-182 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-183 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-184 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-185 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-186 | TC-GS-DIV-E2E-051-resilience-export-gagal-download-tabel-dan-changelog | FE+BE |
| TC-GS-DIV-187 | TC-GS-DIV-E2E-050-download-tabel-isi-file-menu-filter-dan-kolom-visible | FE+BE |
| TC-GS-DIV-188 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-189 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-190 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-191 | TC-GS-DIV-E2E-054-changelog-empty-state | FE+BE |
| TC-GS-DIV-192 | TC-GS-DIV-E2E-054-changelog-empty-state | FE+BE |
| TC-GS-DIV-193 | TC-GS-DIV-E2E-055-changelog-search-kolom-searchable-dan-kontrol | FE+BE |
| TC-GS-DIV-194 | TC-GS-DIV-E2E-055-changelog-search-kolom-searchable-dan-kontrol | FE+BE |
| TC-GS-DIV-195 | TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | FE+BE |
| TC-GS-DIV-196 | TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | FE+BE |
| TC-GS-DIV-197 | TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | FE+BE |
| TC-GS-DIV-198 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-199 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-200 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-201 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-202 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-203 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-204 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-205 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-206 | TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong | FE+BE |
| TC-GS-DIV-207 | TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong | FE+BE |
| TC-GS-DIV-208 | TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong | FE+BE |
| TC-GS-DIV-209 | TC-GS-DIV-E2E-059-changelog-sort-3-state-dan-nilai-kosong | FE+BE |
| TC-GS-DIV-210 | TC-GS-DIV-E2E-060-changelog-pagination-page-size | FE+BE |
| TC-GS-DIV-211 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-212 | TC-GS-DIV-E2E-052-format-tanggal-general-settings-filter-dan-changelog | FE+BE |
| TC-GS-DIV-213 | TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-214 | TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-215 | TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-216 | TC-GS-DIV-E2E-062-setup-column-changelog-reorder-pin-dan-reset | FE+BE |
| TC-GS-DIV-217 | TC-GS-DIV-E2E-062-setup-column-changelog-reorder-pin-dan-reset | FE+BE |
| TC-GS-DIV-218 | TC-GS-DIV-E2E-062-setup-column-changelog-reorder-pin-dan-reset | FE+BE |
| TC-GS-DIV-219 | TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-220 | TC-GS-DIV-E2E-061-setup-column-changelog-screening-hide-cancel-dan-kolom-terakhir | FE+BE |
| TC-GS-DIV-221 | TC-GS-DIV-E2E-063-download-changelog-isi-file | FE+BE |
| TC-GS-DIV-222 | TC-GS-DIV-E2E-063-download-changelog-isi-file | FE+BE |
| TC-GS-DIV-223 | TC-GS-DIV-E2E-051-resilience-export-gagal-download-tabel-dan-changelog | FE+BE |
| TC-GS-DIV-224 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-225 | TC-GS-DIV-E2E-055-changelog-search-kolom-searchable-dan-kontrol | FE+BE |
| TC-GS-DIV-226 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-227 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-228 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-229 | TC-GS-DIV-E2E-057-changelog-filter-fungsional-or-and-dan-kombinasi | FE+BE |
| TC-GS-DIV-230 | TC-GS-DIV-E2E-053-changelog-screening-format-sel-urutan-default-tooltip-dan-tutup | FE+BE |
| TC-GS-DIV-231 | TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | FE+BE |
| TC-GS-DIV-232 | TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown | FE+BE |
| TC-GS-DIV-233 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-234 | TC-GS-DIV-E2E-049-isolasi-konfigurasi-kolom-tabel-division-dan-modal-changelog | FE+BE |
| TC-GS-DIV-235 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-236 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-237 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-238 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-239 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-240 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-241 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-242 | TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete | FE+BE |
| TC-GS-DIV-243 | TC-GS-DIV-E2E-065-pencatatan-changelog-delete-dan-bulk-delete | FE+BE |
| TC-GS-DIV-244 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-245 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-246 | TC-GS-DIV-E2E-066-modified-by-aktor-pelaksana-tiap-aksi | FE+BE |
| TC-GS-DIV-247 | TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | FE+BE |
| TC-GS-DIV-248 | TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | FE+BE |
| TC-GS-DIV-249 | TC-GS-DIV-E2E-064-pencatatan-changelog-create-dan-edit | FE+BE |
| TC-GS-DIV-250 | TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-251 | TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-252 | TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-253 | TC-GS-DIV-E2E-069-sinkron-dropdown-division-form-user-dan-non-login-user | FE+BE |
| TC-GS-DIV-254 | TC-GS-DIV-E2E-070-form-user-dan-non-login-user-division-dihapus-pihak-lain | FE+BE |
| TC-GS-DIV-255 | TC-GS-DIV-E2E-070-form-user-dan-non-login-user-division-dihapus-pihak-lain | FE+BE |
| TC-GS-DIV-256 | TC-GS-DIV-E2E-071-import-create-missing-divisions-edit-delete-dan-log | FE+BE |
| TC-GS-DIV-257 | TC-GS-DIV-E2E-071-import-create-missing-divisions-edit-delete-dan-log | FE+BE |
| TC-GS-DIV-258 | TC-GS-DIV-E2E-071-import-create-missing-divisions-edit-delete-dan-log | FE+BE |
| TC-GS-DIV-259 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-260 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-261 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-262 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-263 | TC-GS-DIV-E2E-074-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-DIV-264 | TC-GS-DIV-E2E-074-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-DIV-265 | TC-GS-DIV-E2E-074-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-DIV-266 | TC-GS-DIV-E2E-075-isolasi-data-entitas-lain | FE+BE |
| TC-GS-DIV-267 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-268 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-269 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-270 | TC-GS-DIV-E2E-073-defense-in-depth-request-langsung-validasi-server-xss-dan-sql | FE+BE |
| TC-GS-DIV-271 | TC-GS-DIV-E2E-029-konflik-edit-dua-admin-last-write-wins | FE+BE |
| TC-GS-DIV-272 | TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama | FE+BE |
| TC-GS-DIV-273 | TC-GS-DIV-E2E-022-konflik-create-dua-admin-code-auto-generate-name-dan-code-sama | FE+BE |
| TC-GS-DIV-274 | TC-GS-DIV-E2E-021-create-race-slot-terakhir-dua-admin | FE+BE |
| TC-GS-DIV-275 | TC-GS-DIV-E2E-030-konflik-edit-vs-delete-record-dihapus-pihak-lain | FE+BE |
| TC-GS-DIV-276 | TC-GS-DIV-E2E-030-konflik-edit-vs-delete-record-dihapus-pihak-lain | FE+BE |
| TC-GS-DIV-277 | TC-GS-DIV-E2E-077-realtime-perubahan-admin-lain-pada-tabel-terbuka | FE+BE |
| TC-GS-DIV-278 | TC-GS-DIV-E2E-077-realtime-perubahan-admin-lain-pada-tabel-terbuka | FE+BE |
| TC-GS-DIV-279 | TC-GS-DIV-E2E-034-delete-katalog-terakhir-otomatis-in-use | FE+BE |
| TC-GS-DIV-280 | TC-GS-DIV-E2E-078-tanpa-gating-plan-create-edit-delete-semua-tier | FE+BE |
| TC-GS-DIV-281 | TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet | FE+BE |
| TC-GS-DIV-282 | TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet | FE+BE |
| TC-GS-DIV-283 | TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet | FE+BE |
| TC-GS-DIV-284 | TC-GS-DIV-E2E-079-mobile-screening-card-list-row-action-dan-bottom-sheet | FE+BE |
| TC-GS-DIV-285 | TC-GS-DIV-E2E-080-mobile-create-dan-edit-division | FE+BE |
| TC-GS-DIV-286 | TC-GS-DIV-E2E-080-mobile-create-dan-edit-division | FE+BE |
| TC-GS-DIV-287 | TC-GS-DIV-E2E-038-bulk-delete-campuran-dialog-continue-dan-cancel | FE+BE |
| TC-GS-DIV-288 | TC-GS-DIV-E2E-028-edit-code-dikosongkan-auto-generate-dan-no-op | FE+BE |
| TC-GS-DIV-288 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-289 | TC-GS-DIV-E2E-072-import-create-missing-divisions-limit-dan-race | FE+BE |
| TC-GS-DIV-290 | TC-GS-DIV-E2E-072-import-create-missing-divisions-limit-dan-race | FE+BE |
| TC-GS-DIV-291 | TC-GS-DIV-E2E-023-edit-screening-aksesibilitas-clear-field-dan-tutup | mock |
| TC-GS-DIV-292 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-293 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-294 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-295 | TC-GS-DIV-E2E-058-changelog-filter-chip-dropdown-search-dan-overflow | FE+BE |
| TC-GS-DIV-296 | TC-GS-DIV-E2E-040-bulk-delete-race-item-menjadi-in-use | FE+BE |
| TC-GS-DIV-297 | TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | FE+BE |
| TC-GS-DIV-298 | TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | FE+BE |
| TC-GS-DIV-299 | TC-GS-DIV-E2E-068-pencatatan-system-log-aktor-dan-activity-log | FE+BE |
| TC-GS-DIV-300 | TC-GS-DIV-E2E-067-absence-log-edit-tanpa-perubahan-dan-skip-in-use | FE+BE |
| TC-GS-DIV-301 | TC-GS-DIV-E2E-029-konflik-edit-dua-admin-last-write-wins | FE+BE |
