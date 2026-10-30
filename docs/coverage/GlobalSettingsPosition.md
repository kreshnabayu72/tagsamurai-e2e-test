# Coverage E2E — Global Settings > User > Position

Sumber: `global-settings/position/TestCases/tc-position.md` (308 TC `TC-GS-POS-1`–`308`, tanpa TC retired). Suite: `specs/GlobalSettings/Position/`. Prefix: `GS` + `POS` (`TC-GS-POS-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 302 TC masuk 56 spec, 6 TC hanya-BE tidak masuk spec (TC-260 sampai 265, kolom FE Test `-`). Setiap TC yang masuk terpetakan ke tepat satu spec di `sourceTc`; TC yang asersinya terbelah lintas spec dicatat di bagian Pembagian TC lintas spec.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | Screening Tab Position: Layout 3 Zona, Breadcrumb, Tooltip Ikon, Urutan Name A-Z, Nama 120 Karakter, Last Updated Seed, dan State Visual | FE+BE | 92 | 1, 2, 3, 4, 5, 9, 291, 293 |
| TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | Empty State Entitas Tanpa Position dan Entitas Diprovisioning Tanpa Default User Position | FE+BE | 13 | 7, 296 |
| TC-GS-POS-E2E-003-pagination-dan-ukuran-halaman-tabel-utama | Pagination 10 Baris, Navigasi Halaman, Ukuran Halaman 10/25/50/100, dan Input Nomor Halaman Tabel Position | FE+BE | 27 | 10, 11, 12 |
| TC-GS-POS-E2E-004-retensi-state-tabel-f5-dan-navigasi | Retensi Search, Sort, Filter, dan Halaman Tabel Position saat F5, Reset saat Klik Sidebar, dan Retensi saat Pindah Sub-tab | FE+BE | 51 | 13, 14, 15 |
| TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | Guided Tooltip Tab Position: Konten Step, Navigasi Next/Back, Resize Viewport, Keyboard, dan Identik untuk Read Only | FE+BE | 67 | 17, 22, 23, 24 |
| TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | Guided Tooltip Tab Position: Muncul Otomatis pada Kunjungan Pertama, Done, Skip, dan Klik Overlay Menandai Seen, serta Replay lewat Tombol [?] | FE+BE | 46 | 16, 18, 19, 20, 21 |
| TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Position per Role | FE+BE | 84 | 25, 26, 27, 28, 29, 30, 31 |
| TC-GS-POS-E2E-008-role-matrix-negatif-akses-langsung-url | Role Matrix Negatif: Akses Langsung URL Tab Position oleh Aktor Tanpa Capability | FE+BE | 5 | 36 |
| TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Create, Edit, Delete, dan Bulk Delete Position oleh Aktor Capability Spesifik | FE+BE | 30 | 32, 33, 34, 35 |
| TC-GS-POS-E2E-010-capability-dicabut-saat-aksi-berjalan | Save Edit Position Ditolak setelah Capability Update Dicabut di Tengah Sesi | FE+BE | 12 | 294 |
| TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | Create Position: Screening Form, Aksesibilitas, Validasi Inline (Kosong, Spasi, 121 Karakter, Emoji), Clear Field, dan Hover Tombol | FE+BE | 83 | 37, 38, 39, 40, 42, 43, 44, 45, 50, 284 |
| TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | Create Position: Duplikat Case-Insensitive saat Mengetik, Spasi Tepi, Error Hilang saat Unik, Saving State, dan Klik Ganda Submit | FE+BE | 38 | 47, 48, 49, 65, 66 |
| TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | Create Position: Penutupan Form via ✕ dan Esc, Dialog Unsaved Changes (Cancel dan Leave), Backdrop, Reload, dan Pindah Menu | FE+BE | 65 | 55, 56, 57, 58, 59, 60, 61, 62, 63, 64 |
| TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | Create Position Berhasil: Stay, 1 dan 120 Karakter, Trim, Populasi Data, Persistensi setelah Refresh, dan dari Empty State | FE+BE | 71 | 41, 51, 52, 53, 54, 73, 282, 286 |
| TC-GS-POS-E2E-015-master-data-count-limit-create | Master Data Count Limit: [+ Position] Diblokir, Dialog Limit Reached, Submit Ditolak Setelah Popup Dibuka, Create Berulang hingga Batas, Baca Limit Dinamis, dan Create Missing Positions | FE+BE | 69 | 69, 70, 71, 72, 259, 280 |
| TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | Edit Position: Overlay Row Action, Screening Form, Aksesibilitas, Validasi Inline, Clear Field, dan Hover Tombol | FE+BE | 76 | 74, 75, 76, 77, 78, 80, 81, 82, 83, 88, 285 |
| TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | Edit Position: Duplikat saat Mengetik dan Save, Nama Sendiri Bukan Duplikat, Saving State, dan Klik Ganda Save | FE+BE | 35 | 85, 86, 87, 104, 105 |
| TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | Edit Position: Tutup Tanpa Perubahan, Dialog Unsaved Changes, Nilai Dikembalikan Tidak Dirty, Clear Field, Backdrop, Reload, dan Pindah Menu | FE+BE | 62 | 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103 |
| TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | Edit Position Sukses: Rename, Kapitalisasi, No-Op (Last Updated Tetap), Nama 1 dan 120 Karakter, dan Record Seed | FE+BE | 76 | 79, 89, 90, 91, 92, 110, 283, 287 |
| TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | Delete Position Tunggal: Dialog, Cancel, Esc, Sukses, Klik Ganda, dan Position Terakhir Entitas | FE+BE | 42 | 111, 112, 113, 120, 122, 299 |
| TC-GS-POS-E2E-021-delete-single-diblokir-in-use | Delete Position Tunggal Diblokir: Dipakai User Login, User Non-Login, atau Hanya User Non-Aktif | FE+BE | 27 | 114, 115, 116, 117 |
| TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | Bulk Action Bar Position: Populasi 15 Position, Screening, Counter, Icon ✕, Checkbox Header, Indeterminate, dan Seleksi Manual hingga 100% | FE+BE | 58 | 123, 124, 125, 126, 127, 128, 130 |
| TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | Bulk Selection Position: Select All (N records), Unselect All, Uncheck dari 100%, Retensi Seleksi, dan Seleksi yang Tidak Tampil karena Filter | FE+BE | 72 | 129, 131, 132, 133, 134 |
| TC-GS-POS-E2E-024-selection-limit-bulk | Selection Limit Bulk Position: Checkbox ke-(Limit+1) Disabled dan Select All Dibatasi Limit | FE+BE | 30 | 135, 136 |
| TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | Bulk Delete Homogen: Dialog Single untuk 1 Item Bebas Relasi, Screening Dialog, Cancel, Delete, Daftar Nama Tidak Diringkas, dan Klik Ganda | FE+BE | 53 | 137, 139, 140, 141, 146, 150 |
| TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | Bulk Delete Blokir In-Use (Satu Item dan Seluruhnya), Campuran (Warning lalu Continue), dan Daftar Nama Tidak Diringkas | FE+BE | 69 | 138, 142, 143, 144, 145, 302, 303 |
| TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete | Mobile Android: Aturan Card dan Menu, Screening Toolbar, dan Selection Mode Long-press untuk Bulk Delete Position | FE+BE (mobile) | 39 | 151, 298, 304 |
| TC-GS-POS-E2E-028-search-tabel-utama | Search Tabel Utama Position: Siklus Interaksi, Substring, Case-insensitive, Trim, Hasil Kosong, Scope Kolom, dan Visibilitas Name | FE+BE | 58 | 152, 153, 154, 155, 156, 157, 158 |
| TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | Filter Panel Last Updated Tabel Position: Screening, Rentang Inklusif, Satu Hari, Clear Field, Tutup Tanpa Apply, dan Kolom Hidden | FE+BE | 63 | 159, 160, 161, 162, 163, 164 |
| TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | Kombinasi Search, Filter, Sort, dan Pagination Tabel Position: Siklus Sort, Irisan, Clear, Empty State, dan Reset Halaman | FE+BE | 138 | 165, 166, 167, 168, 169, 170, 171, 172, 173, 174 |
| TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama | Overlay Column Visibility Tabel Position: Screening, Uncheck, Drag Reorder, dan Kolom Terakhir | FE+BE | 37 | 177, 178, 179, 180 |
| TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | Popup Setup Column Tabel Position: Screening, Footer, Search, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Popup Changelog | FE+BE | 148 | 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191 |
| TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | Download CSV dan XLSX Tabel Position: Screening Overlay, Isi Berkas, Mengikuti Search, dan Kolom Tersembunyi | FE+BE | 48 | 192, 193, 194, 195, 196, 197, 198 |
| TC-GS-POS-E2E-034-resilience-baca-loading-error-dan-try-again | Resilience Baca Tabel Position: Loading State dan Error Load dengan Try Again | mock | 16 | 6, 8 |
| TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout | mock | 53 | 67, 68, 106, 107, 108 |
| TC-GS-POS-E2E-036-resilience-hapus-single-dan-bulk-5xx | Resilience Hapus: Delete Single dan Bulk Delete saat Kegagalan Server 5xx | mock | 23 | 121, 149 |
| TC-GS-POS-E2E-037-resilience-download-tabel-utama-dan-changelog | Resilience Download: Toast Error saat Unduh Tabel Utama dan Popup Changelog Gagal | mock | 18 | 199, 240 |
| TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | Popup Changelog: Screening 3 Zona, Tooltip, Tutup lewat ✕ dan Esc, Klik Backdrop, Hover Modified By, Nama Panjang, dan Empty State | FE+BE | 66 | 200, 201, 202, 203, 204, 241, 292 |
| TC-GS-POS-E2E-039-changelog-search | Popup Changelog: Search (Siklus, Kolom Teks, Field, Bukan Date, Tanpa Hasil, dan Terikat Visibilitas Kolom) | FE+BE | 68 | 205, 206, 207, 208, 209, 210 |
| TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | Popup Changelog: Filter Date, Dropdown Multi-select, Sinkronisasi Chip, Overflow, Logika AND/OR, dan Opsi dari Entri Log | FE+BE | 132 | 211, 212, 213, 214, 215, 216, 217, 219, 220 |
| TC-GS-POS-E2E-041-changelog-sort-dan-pagination | Popup Changelog: Sort Date, Teks, Campuran, dan Modified By, Kombinasi dengan Search dan Filter, Clear, Pemulihan Empty State, dan Pagination | FE+BE | 124 | 221, 222, 223, 224, 225, 226, 227, 228 |
| TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | Popup Changelog: Overlay Column Visibility dan Setup Column 7 Kolom (Hide, Reorder, Pin, Reset to Default, ✕, dan Kolom Terakhir) | FE+BE | 172 | 229, 230, 231, 232, 233, 234, 235, 236 |
| TC-GS-POS-E2E-043-download-csv-xlsx-popup-changelog | Download CSV dan XLSX Popup Changelog: Isi Berkas, Sel Kosong, serta Kepatuhan pada Filter dan Kolom Tampil | FE+BE | 31 | 237, 238, 239 |
| TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | Pencatatan Create, Edit, Delete, Bulk Delete Campuran, Snapshot Rename, Kapitalisasi, Create Missing Positions, Field, dan Position Name pada Changelog dan Activity Log | FE+BE | 130 | 242, 243, 244, 245, 247, 248, 250, 252, 253 |
| TC-GS-POS-E2E-045-pencatatan-system-log-aktor | Pencatatan ke System Log Aktor di Detail User untuk Create, Edit, Delete, dan Bulk Delete Position per Item | FE+BE | 45 | 251, 305, 306, 307 |
| TC-GS-POS-E2E-046-absence-log-edit-no-op-dan-import | Tidak Ada Pencatatan Log untuk Edit No-Op dan untuk Position Hasil Import | FE+BE | 38 | 246, 249, 308 |
| TC-GS-POS-E2E-047-format-tanggal-general-settings | Format Tanggal General Settings pada Tabel Utama, Filter Panel, Popup Changelog, dan Filter Date Position | FE+BE | 51 | 254, 255 |
| TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | Sinkronisasi Position Baru, Rename, dan Terhapus ke Form User, Form Non-Login User, dan Filter User List | FE+BE | 78 | 256, 257, 258, 281, 301 |
| TC-GS-POS-E2E-049-defense-in-depth-emoji-server-dan-markup | Defense-in-Depth: Emoji Lolos Filter FE Ditolak Server pada Create dan Edit, dan Nama Berisi Markup Dirender sebagai Teks | FE+BE | 37 | 46, 84, 266 |
| TC-GS-POS-E2E-050-isolasi-entitas | Isolasi Entitas: Position Client Lain Tidak Terlihat di Tabel, Changelog, dan Validasi Nama | FE+BE | 14 | 267 |
| TC-GS-POS-E2E-051-multi-konteks-create-bersamaan-dua-admin | Multi-Konteks: Create Position Bersamaan oleh Dua Admin dengan Nama Sama dan pada Slot Limit Terakhir | FE+BE | 30 | 269, 270 |
| TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | Multi-Konteks: Edit Bersamaan Last-Write-Wins serta Record yang Dihapus atau Menjadi In-Use di Antara Dialog dan Konfirmasi (Single dan Bulk) | FE+BE | 93 | 109, 118, 119, 147, 148, 271, 300 |
| TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | Multi-Konteks: Record Baru, Terhapus, dan Rename dari Sesi Lain Tanpa Muat Ulang serta Popup Edit Tidak Ter-refresh | FE+BE | 49 | 175, 176, 278, 279, 297 |
| TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan | State Tenant: Client Suspended Menolak Create, Edit, dan Delete Position serta Perilaku Identik Lintas Plan | FE+BE | 86 | 268, 272, 273, 274 |
| TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing | Position Hasil Import: Edit, Delete In-Use Diblokir, Delete Bebas Relasi, dan Create Missing Positions Duplikat Ditolak | FE+BE | 37 | 275, 276, 277, 295 |
| TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong | Popup Changelog: Sumber Opsi Dropdown Filter (Loading, Entitas Tanpa Log, Opsi Bertambah, dan Position yang Dihapus) | FE+BE | 45 | 218, 288, 289, 290 |

## TC hanya-BE (tidak masuk spec)

Alasan: kontrak penegakan server tanpa permukaan UI; dicakup `tc-position-backend.md` (namespace `TC-GS-POS-BE-NNN`).

| TC | Judul | Alasan |
|---|---|---|
| TC-GS-POS-260 | Defense-in-depth — Create langsung tanpa capability ditolak (Manage user and role — Read-Only) | FE Test `-` (hanya validasi server, tanpa tampilan FE) |
| TC-GS-POS-261 | Defense-in-depth — Edit langsung tanpa capability ditolak (Manage user and role — Create-Only) | FE Test `-` (hanya validasi server, tanpa tampilan FE) |
| TC-GS-POS-262 | Defense-in-depth — Delete langsung tanpa capability ditolak (Manage user and role — Update-Only) | FE Test `-` (hanya validasi server, tanpa tampilan FE) |
| TC-GS-POS-263 | Defense-in-depth — Create langsung tanpa capability ditolak (Read Only) | FE Test `-` (hanya validasi server, tanpa tampilan FE) |
| TC-GS-POS-264 | Defense-in-depth — guard in-use tetap ditegakkan server | FE Test `-` (hanya validasi server, tanpa tampilan FE) |
| TC-GS-POS-265 | Defense-in-depth — duplikat nama ditolak server | FE Test `-` (hanya validasi server, tanpa tampilan FE) |

## Pembagian TC lintas spec

- **TC-GS-POS-91, 92** (Edit No-Op) dijalankan di spec `019`; asersi tidak ada entri log untuk **TC-GS-POS-246** (Changelog dan Activity Log) dan **TC-GS-POS-308** (System Log aktor) ada di spec `046` dengan aksi No-Op dan baseline sendiri (kelas g).
- **TC-GS-POS-249** (Position hasil Import tidak tercatat di Changelog) hanya di spec `046`; spec lain yang mengubah atau menghapus Position hasil Import memakai record milik spec sendiri (spec `055` memakai `Import Probe Analyst {runId}-055`).
- **TC-GS-POS-245** (Bulk Delete campuran) di spec `044`; bagian Expected "tidak ada entri `Warehouse Supervisor`" diasersi di spec `044` dengan nama bersuffix unik (baseline nol) dan anchor positif (pengecualian `P-1`).
- **TC-GS-POS-307** (Bulk Delete, satu entri per item) di spec `045`; bagian Expected "tidak ada entri untuk item yang tidak terhapus" diasersi di spec `045` dengan baseline jumlah entri dan anchor positif (pengecualian `P-1`).
- **TC-GS-POS-46, 84** (emoji lolos filter FE ditolak server) di spec `049` bersama TC-266 (kelas defense-in-depth); validasi emoji lewat keystroke ada di spec `011` dan `016`.
- **TC-GS-POS-204** (empty state Popup Changelog) di spec `038` untuk Client Kosong; spec `002` memuat empty state Changelog entitas `Client Tanpa Seed` (TC-296).
- **TC-GS-POS-175, 176** di spec `053` (sesi kedua sebagai objek asersi); **TC-GS-POS-109, 118, 119, 147, 148, 271, 300** di spec `052`.
- **TC-GS-POS-282, 283** (Position `Q` dan `R`): `Q` dibuat di spec `014` (TC-282); TC-283 di spec `019` memakai `Y` yang diubah menjadi `Z`.
- **TC-GS-POS-138** (blokir satu item in-use) berada di spec `026` sebagai blok pertama bersama blokir seluruhnya in-use (TC-145, 302) dan alur campuran; spec `025` memuat alur Bulk Delete homogen.
- **TC-GS-POS-249, 275, 277** memakai Position hasil Import milik tes `Import Probe Analyst {runId}-NNN` (diubah menjadi `Import Probe Specialist {runId}-NNN`); spec `046` memakai suffix `-046` dan spec `055` suffix `-055`; Pre-setup 15 `Field Technician` tidak diubah modul Position.
- **TC-GS-POS-73, 122, 130** memakai entitas `Client Tulis` (Pre-setup 27: spec `014`, `020`, `022`); TC-7, 204, 218 memakai `Client Kosong` baca-saja (spec `002`, `038`, `056`).

## Kebutuhan lingkungan (tim FE)

- Env var password yang sudah terdaftar di `spectra.config.ts` dan `.env.example` dan dipakai spec Position: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_NOCAP_PASSWORD`, `AC_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTEXP_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`.
- Env var baru yang perlu didaftarkan tim FE di `spectra.config.ts` dan `.env.example`: `GS_CLIENTEMPTY_TC_PASSWORD` (Total Control Client Kosong baca-saja, spec 002, 038, 056), `GS_CLIENTWRITE_TC_PASSWORD` (Total Control Client Tulis, Pre-setup 27, spec 014, 020, 022), `GS_CLIENTSEED_TC_PASSWORD` (Total Control Client Seed, spec 001, 019), `GS_CLIENTNOSEED_TC_PASSWORD` (Total Control entitas `Client Tanpa Seed {runId}-002`, spec 002).
- Akun Pre-setup TC Position (`superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan sejenisnya) berbeda dari akun suite Brand (`totalControl_automated_qaTeam1@...`); tim FE mengonfirmasi bahwa `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_NOCAP_PASSWORD` berlaku untuk akun Pre-setup Position. Email akun Client Kosong, Client Seed, Client Lain, Client Suspended, dan keempat Client plan tidak tertulis di Pre-setup TC.
- Fixture baru: berkas `fixtures/position.json` dengan kunci `Fixture.position.*` yang dirujuk spec (nama seed per spec, mis. `pagingSeed003`, `bulkBar022`, `changelogSeed040`).
- Kemampuan teknis: intercept jaringan (5xx, timeout, tahan respons) untuk spec 012, 017, 034 sampai 037, 056; dua sesi browser (Admin A dan Admin B) untuk spec 010, 015, 048, 051 sampai 053, 055; sesi API Admin B sebagai pemicu penghapusan untuk spec 056; mengubah System Limits (Master Data Count Limit, Selection Limit) lewat akun Admin Console untuk spec 015, 024, 051; mengubah capability role dan memulihkannya untuk spec 010; mengubah format tanggal General Settings untuk spec 047; menyetel dan mereset flag Guided Tooltip `guided_tooltip_seen_gs-position` untuk spec 001 sampai 006; seeding Position, user, dan entri Changelog lewat API; membaca berkas unduhan CSV/XLSX untuk spec 033 dan 043; menangani dialog `beforeunload` untuk spec 013, 018, 052, dan 054; emulator atau perangkat Android untuk spec 027; injeksi DOM untuk spec 049; kondisi Client Suspended dan keempat plan sebagai environment tetap untuk spec 054; staging Import Type "Position" dan "User Login" untuk spec 015, 044, 046, 055.
- Hook suite `beforeEach` membuka Global Settings > User > Position (layar awal spec yang tidak menguji navigasi); langkah buka tetap ditulis di spec yang objek ujinya kunjungan, visibilitas per role, atau pembukaan sesudah ganti akun.
- Seeding Client Tulis: 3 Position untuk TC-130 (kemampuan tim FE/BE).
- Suite berjalan serial (`parallel: false`). Spec yang menghapus data (020, 025, 026, 052) berjalan sesudah spec lain. Environment automation harus terisolasi dari aktivitas pengguna lain agar asersi himpunan stabil.

## Keputusan yang sudah diambil

- **Spec panjang (±35 langkah):** diterima apa adanya; alasan pertahanan ada di `## Notes` tiap spec dan titik pisah yang disarankan penulis tetap tercatat di sana sebagai opsi saat script ditulis. Spec 040 dipecah karena memuat lebih dari satu kelas harness: TC-218, 288, 289, 290 (sumber opsi dropdown filter: entitas kosong, Create, Loading, hapus oleh Admin B) berada di spec 056, filter murni tetap di spec 040. Spec terpanjang saat ini: 042 (172), 032 (148), 030 (138), 040 (132), 044 (130), 041 (124), 052 (93), 001 (92), 054 (86).
- **Position `Q`/`R` (TC-282/283):** spec 014 membuat `Q` (TC-282); spec 019 memakai nama 1 karakter `Y` yang diubah menjadi `Z` untuk TC-283 supaya tidak bentrok pada entitas yang sama (dicatat di Notes spec 019).
- **Pengecualian `P-1`:** disetujui untuk asersi absence TC-245 (spec 044) dan TC-307 (spec 045); kedua spec memuat aksi yang menghasilkan kondisi itu, dengan baseline dan anchor positif.
- **Spec 034 sampai 037:** `Mode: mock` (keputusan user); asersi yang menyangkut state backend nyata tidak teruji pada mode itu.
- **Seeding** mengikuti precondition TC, bukan angka rencana: spec 003 dan 004 memakai N = 15 sehingga ukuran halaman 100 dengan lebih dari 100 baris tidak teruji pada TC sumber.
- **Pemisahan entitas kosong (D3):** `Client Kosong` baca-saja untuk spec 002, 038, 056; `Client Tulis` (Pre-setup 27) untuk spec 014, 020, 022 yang membuat lalu menghapus Position. Changelog `Client Kosong` tidak pernah ditulis spec mana pun, sehingga TC-204 dan 218 tidak bergantung urutan.
- **Keputusan konvensi dan skill generator (D2, D4, D6, D10, D11, D13, D14, D16, D17, D20, D21, D22, D23)** sudah ditulis di `docs/e2e-conventions.md` dan skill `tagsamurai-e2e-generate-spec`; temuan audit E2E (Berat 5, Sedang 12, Ringan 11 tema) ditutup di spec sesuai keputusan, kecuali butir yang bergantung pada info di luar file (lihat bagian berikut).

## Tindak lanjut di luar stage ini

Dicatat sebagai kebutuhan atau usulan; tidak membuka stage ini.

- **PRD (tidak diubah atas permintaan user):** keadaan Filter Panel sesudah `[Apply]` (TC memakai model tetap terbuka) dan bentuk aksi Bulk Delete (TC: `Bulk Action` berisi `Delete`; PRD `position.md` menulis `[Delete]` pada Bulk Action Bar) masih perlu diseragamkan di PRD oleh pemilik PRD.
- **Usulan TC baru untuk QA:** varian Client Expired untuk TC-272 sampai 274 (precondition TC hanya Client Suspended; spec 054 hanya memuat Suspended; `GS_CLIENTEXP_TC_PASSWORD` belum dipakai).
- **Perbaikan TC sumber (QA):** Nama Data Dinamis 20–34 (15 nama bulk) tidak lengkap; spec 025 memakai `Bulk Name NN {runId}-025`. TC-47: toleransi ±500 ms tidak ditetapkan; TC-250/295/280/151/298/304 bertanda Manual Only tetapi tetap ditulis sebagai spec (bagian 2 konvensi). TC-25 tidak menyebut elemen halaman yang tetap tampil bagi akun tanpa capability (spec 007 memakai breadcrumb `User` sebagai anchor). TC-91 a menuntut asersi spinner sesudah popup tertutup (spec 019 mempertahankannya). TC-1 menamai header `⋯` tabel utama `Column Visibility`, sedangkan PRD menyebut `Actions`.
- **Penyelarasan TC yang sudah dilakukan (tanpa mengubah PRD):** Search atomik (TC-153..158, 165..174, 196, 205), header `Actions (⋯)` Popup Changelog (TC-200/201), syarat Date berselisih >= 1 menit (TC-221..224), pembanding `Name` (TC-298), N dari seeding (TC-69/71/72/259/280 dan TC-10..15), user milik tes (TC-118/147/300; Data Dinamis 36), Expected teramati TC-135/136, jumlah opsi TC-217, ukuran halaman TC-14, Expected TC-153 memuat `Sales Coordinator`, opsi General Settings nyata pada TC-254/255.
- **Konfirmasi dari aplikasi (FE/QA):** perilaku error "Position Name must not be empty" saat field dikosongkan lagi (spec 011), state Popup Edit sesudah toast netral (TC-109) dan toast error 403 (TC-294), keadaan Filter Panel Popup Changelog sesudah `[Apply]`, bentuk tombol Bulk Delete, dan apakah pelaku kedua yang hanya memicu state (spec 010, 015, 048, 051 sampai 053, 055) dijalankan lewat sesi API.
- **Tim FE:** mendaftarkan env var baru di `spectra.config.ts` dan `.env.example` (bagian Kebutuhan lingkungan) dan mengisi email akun yang belum ada di Pre-setup TC.
- **Tim FE/BE:** menyediakan mekanisme yang tidak didefinisikan di TC, PRD, atau LLD: reset flag Guided Tooltip, mencabut capability role (010), membaca URL tab Position dari sesi Total Control (008), membuat entitas `Client Tanpa Seed` (002), seeding user (026, 044, 048, 052), staging Import (015, 044, 055), menyetel Last Updated seed (029).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-POS-1 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-2 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-3 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-4 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-5 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-6 | TC-GS-POS-E2E-034-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-POS-7 | TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | FE+BE |
| TC-GS-POS-8 | TC-GS-POS-E2E-034-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-POS-9 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-10 | TC-GS-POS-E2E-003-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-POS-11 | TC-GS-POS-E2E-003-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-POS-12 | TC-GS-POS-E2E-003-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-POS-13 | TC-GS-POS-E2E-004-retensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-14 | TC-GS-POS-E2E-004-retensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-15 | TC-GS-POS-E2E-004-retensi-state-tabel-f5-dan-navigasi | FE+BE |
| TC-GS-POS-16 | TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-POS-17 | TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-POS-18 | TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-POS-19 | TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-POS-20 | TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-POS-21 | TC-GS-POS-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-POS-22 | TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-POS-23 | TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-POS-24 | TC-GS-POS-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-POS-25 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-26 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-27 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-28 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-29 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-30 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-31 | TC-GS-POS-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-POS-32 | TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-POS-33 | TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-POS-34 | TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-POS-35 | TC-GS-POS-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-POS-36 | TC-GS-POS-E2E-008-role-matrix-negatif-akses-langsung-url | FE+BE |
| TC-GS-POS-37 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-38 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-39 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-40 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-41 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-42 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-43 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-44 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-45 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-46 | TC-GS-POS-E2E-049-defense-in-depth-emoji-server-dan-markup | FE+BE |
| TC-GS-POS-47 | TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-48 | TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-49 | TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-50 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-51 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-52 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-53 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-54 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-55 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-56 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-57 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-58 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-59 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-60 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-61 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-62 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-63 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-64 | TC-GS-POS-E2E-013-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-65 | TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-66 | TC-GS-POS-E2E-012-create-duplikat-dan-guard-double-submit | FE+BE |
| TC-GS-POS-67 | TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | mock |
| TC-GS-POS-68 | TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | mock |
| TC-GS-POS-69 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-70 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-71 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-72 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-73 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-74 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-75 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-76 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-77 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-78 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-79 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-80 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-81 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-82 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-83 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-84 | TC-GS-POS-E2E-049-defense-in-depth-emoji-server-dan-markup | FE+BE |
| TC-GS-POS-85 | TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-86 | TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-87 | TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-88 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-89 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-90 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-91 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-92 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-93 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-94 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-95 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-96 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-97 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-98 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-99 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-100 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-101 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-102 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-103 | TC-GS-POS-E2E-018-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-POS-104 | TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-105 | TC-GS-POS-E2E-017-edit-duplikat-dan-guard-double-save | FE+BE |
| TC-GS-POS-106 | TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | mock |
| TC-GS-POS-107 | TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | mock |
| TC-GS-POS-108 | TC-GS-POS-E2E-035-resilience-tulis-create-edit-5xx-timeout | mock |
| TC-GS-POS-109 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-110 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-111 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-112 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-113 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-114 | TC-GS-POS-E2E-021-delete-single-diblokir-in-use | FE+BE |
| TC-GS-POS-115 | TC-GS-POS-E2E-021-delete-single-diblokir-in-use | FE+BE |
| TC-GS-POS-116 | TC-GS-POS-E2E-021-delete-single-diblokir-in-use | FE+BE |
| TC-GS-POS-117 | TC-GS-POS-E2E-021-delete-single-diblokir-in-use | FE+BE |
| TC-GS-POS-118 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-119 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-120 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-121 | TC-GS-POS-E2E-036-resilience-hapus-single-dan-bulk-5xx | mock |
| TC-GS-POS-122 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-123 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-124 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-125 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-126 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-127 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-128 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-129 | TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | FE+BE |
| TC-GS-POS-130 | TC-GS-POS-E2E-022-bulk-action-bar-protokol-seleksi-per-halaman | FE+BE |
| TC-GS-POS-131 | TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | FE+BE |
| TC-GS-POS-132 | TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | FE+BE |
| TC-GS-POS-133 | TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | FE+BE |
| TC-GS-POS-134 | TC-GS-POS-E2E-023-bulk-select-all-lintas-halaman-dan-retensi | FE+BE |
| TC-GS-POS-135 | TC-GS-POS-E2E-024-selection-limit-bulk | FE+BE |
| TC-GS-POS-136 | TC-GS-POS-E2E-024-selection-limit-bulk | FE+BE |
| TC-GS-POS-137 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-138 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-139 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-140 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-141 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-142 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-143 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-144 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-145 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-146 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-147 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-148 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-149 | TC-GS-POS-E2E-036-resilience-hapus-single-dan-bulk-5xx | mock |
| TC-GS-POS-150 | TC-GS-POS-E2E-025-bulk-delete-homogen-dan-dialog-single | FE+BE |
| TC-GS-POS-151 | TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-POS-152 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-153 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-154 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-155 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-156 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-157 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-158 | TC-GS-POS-E2E-028-search-tabel-utama | FE+BE |
| TC-GS-POS-159 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-160 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-161 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-162 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-163 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-164 | TC-GS-POS-E2E-029-filter-panel-last-updated-tabel-utama | FE+BE |
| TC-GS-POS-165 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-166 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-167 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-168 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-169 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-170 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-171 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-172 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-173 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-174 | TC-GS-POS-E2E-030-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-POS-175 | TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | FE+BE |
| TC-GS-POS-176 | TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | FE+BE |
| TC-GS-POS-177 | TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-178 | TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-179 | TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-180 | TC-GS-POS-E2E-031-overlay-column-visibility-tabel-utama | FE+BE |
| TC-GS-POS-181 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-182 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-183 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-184 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-185 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-186 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-187 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-188 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-189 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-190 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-191 | TC-GS-POS-E2E-032-setup-column-modal-tabel-utama | FE+BE |
| TC-GS-POS-192 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-193 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-194 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-195 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-196 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-197 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-198 | TC-GS-POS-E2E-033-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-POS-199 | TC-GS-POS-E2E-037-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-POS-200 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-201 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-202 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-203 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-204 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-205 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-206 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-207 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-208 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-209 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-210 | TC-GS-POS-E2E-039-changelog-search | FE+BE |
| TC-GS-POS-211 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-212 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-213 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-214 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-215 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-216 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-217 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-218 | TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong | FE+BE |
| TC-GS-POS-219 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-220 | TC-GS-POS-E2E-040-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-POS-221 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-222 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-223 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-224 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-225 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-226 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-227 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-228 | TC-GS-POS-E2E-041-changelog-sort-dan-pagination | FE+BE |
| TC-GS-POS-229 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-230 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-231 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-232 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-233 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-234 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-235 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-236 | TC-GS-POS-E2E-042-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-POS-237 | TC-GS-POS-E2E-043-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-238 | TC-GS-POS-E2E-043-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-239 | TC-GS-POS-E2E-043-download-csv-xlsx-popup-changelog | FE+BE |
| TC-GS-POS-240 | TC-GS-POS-E2E-037-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-POS-241 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-242 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-243 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-244 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-245 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-246 | TC-GS-POS-E2E-046-absence-log-edit-no-op-dan-import | FE+BE |
| TC-GS-POS-247 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-248 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-249 | TC-GS-POS-E2E-046-absence-log-edit-no-op-dan-import | FE+BE |
| TC-GS-POS-250 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-251 | TC-GS-POS-E2E-045-pencatatan-system-log-aktor | FE+BE |
| TC-GS-POS-252 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-253 | TC-GS-POS-E2E-044-pencatatan-changelog-dan-activity-log | FE+BE |
| TC-GS-POS-254 | TC-GS-POS-E2E-047-format-tanggal-general-settings | FE+BE |
| TC-GS-POS-255 | TC-GS-POS-E2E-047-format-tanggal-general-settings | FE+BE |
| TC-GS-POS-256 | TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | FE+BE |
| TC-GS-POS-257 | TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | FE+BE |
| TC-GS-POS-258 | TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | FE+BE |
| TC-GS-POS-259 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-260 | — (hanya-BE) | BE |
| TC-GS-POS-261 | — (hanya-BE) | BE |
| TC-GS-POS-262 | — (hanya-BE) | BE |
| TC-GS-POS-263 | — (hanya-BE) | BE |
| TC-GS-POS-264 | — (hanya-BE) | BE |
| TC-GS-POS-265 | — (hanya-BE) | BE |
| TC-GS-POS-266 | TC-GS-POS-E2E-049-defense-in-depth-emoji-server-dan-markup | FE+BE |
| TC-GS-POS-267 | TC-GS-POS-E2E-050-isolasi-entitas | FE+BE |
| TC-GS-POS-268 | TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan | FE+BE |
| TC-GS-POS-269 | TC-GS-POS-E2E-051-multi-konteks-create-bersamaan-dua-admin | FE+BE |
| TC-GS-POS-270 | TC-GS-POS-E2E-051-multi-konteks-create-bersamaan-dua-admin | FE+BE |
| TC-GS-POS-271 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-272 | TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan | FE+BE |
| TC-GS-POS-273 | TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan | FE+BE |
| TC-GS-POS-274 | TC-GS-POS-E2E-054-state-tenant-write-lockdown-dan-plan | FE+BE |
| TC-GS-POS-275 | TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-276 | TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-277 | TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-278 | TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | FE+BE |
| TC-GS-POS-279 | TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | FE+BE |
| TC-GS-POS-280 | TC-GS-POS-E2E-015-master-data-count-limit-create | FE+BE |
| TC-GS-POS-281 | TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | FE+BE |
| TC-GS-POS-282 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-283 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-284 | TC-GS-POS-E2E-011-create-screening-aksesibilitas-dan-validasi-field | FE+BE |
| TC-GS-POS-285 | TC-GS-POS-E2E-016-edit-screening-row-action-aksesibilitas-dan-validasi | FE+BE |
| TC-GS-POS-286 | TC-GS-POS-E2E-014-create-sukses-stay-trim-batas-dan-populasi | FE+BE |
| TC-GS-POS-287 | TC-GS-POS-E2E-019-edit-sukses-no-op-kapitalisasi-dan-record-seed | FE+BE |
| TC-GS-POS-288 | TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong | FE+BE |
| TC-GS-POS-289 | TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong | FE+BE |
| TC-GS-POS-290 | TC-GS-POS-E2E-056-changelog-filter-opsi-dinamis-loading-dan-entitas-kosong | FE+BE |
| TC-GS-POS-291 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-292 | TC-GS-POS-E2E-038-changelog-screening-hover-dan-empty-state | FE+BE |
| TC-GS-POS-293 | TC-GS-POS-E2E-001-screening-tabel-layout-urutan-default-dan-tooltip | FE+BE |
| TC-GS-POS-294 | TC-GS-POS-E2E-010-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-POS-295 | TC-GS-POS-E2E-055-lifecycle-position-hasil-import-dan-create-missing | FE+BE |
| TC-GS-POS-296 | TC-GS-POS-E2E-002-empty-state-entitas-tanpa-position | FE+BE |
| TC-GS-POS-297 | TC-GS-POS-E2E-053-multi-konteks-sinkron-realtime-tanpa-reload | FE+BE |
| TC-GS-POS-298 | TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-POS-299 | TC-GS-POS-E2E-020-delete-single-sukses-cancel-double-click-dan-satu-satunya | FE+BE |
| TC-GS-POS-300 | TC-GS-POS-E2E-052-multi-konteks-edit-dan-delete-antar-admin | FE+BE |
| TC-GS-POS-301 | TC-GS-POS-E2E-048-sinkronisasi-position-ke-form-user-dan-filter-user-list | FE+BE |
| TC-GS-POS-302 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-303 | TC-GS-POS-E2E-026-bulk-delete-campuran-dan-seluruhnya-in-use | FE+BE |
| TC-GS-POS-304 | TC-GS-POS-E2E-027-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-POS-305 | TC-GS-POS-E2E-045-pencatatan-system-log-aktor | FE+BE |
| TC-GS-POS-306 | TC-GS-POS-E2E-045-pencatatan-system-log-aktor | FE+BE |
| TC-GS-POS-307 | TC-GS-POS-E2E-045-pencatatan-system-log-aktor | FE+BE |
| TC-GS-POS-308 | TC-GS-POS-E2E-046-absence-log-edit-no-op-dan-import | FE+BE |
