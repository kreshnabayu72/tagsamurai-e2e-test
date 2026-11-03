# Coverage E2E — Global Settings > User > Non-Login User

Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md` (508 TC granular `TC-GS-NLU-1`–`470` dan seterusnya sesuai file). Suite: `specs/GlobalSettings/NonLoginUser/`. Prefix: `GS` + `NLU` (`TC-GS-NLU-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: semua 508 TC masuk spec, 0 TC hanya-BE (`tc-non-login-user-backend.md` disusun per endpoint dan tidak merujuk id TC granular). 138 spec; setiap TC terpetakan ke tepat satu spec.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-NLU-E2E-001-screening-list-non-login-user-layout-breadcrumb-placeholder-search | Screening List Non-Login User: layout, breadcrumb, placeholder Search, tab, dan Login User tidak tampil | FE+BE | 31 | 1, 2, 3, 4, 5 |
| TC-GS-NLU-E2E-002-retensi-state-tabel-per-sub-tab-dan-setelah-back | Retensi state tabel per sub-tab dan setelah Back atau Refresh | FE+BE | 21 | 6, 253, 254 |
| TC-GS-NLU-E2E-003-tampilan-default-sort-loading-empty-search-dan-sel-name | Tampilan default sort, loading, empty Search, dan sel Name, Position, Employee ID, Represented By | FE+BE | 33 | 7, 8, 10, 12, 13, 14, 15 |
| TC-GS-NLU-E2E-004-tampilan-kolom-last-update-switch-active-tooltip-table-tools | Tampilan kolom Last Update, switch Active, tooltip Table Tools, dan overlay row action | FE+BE | 20 | 16, 17, 18, 19 |
| TC-GS-NLU-E2E-005-empty-state-client-tanpa-non-login-user-dan-dropdown | Empty state Client tanpa Non-Login User dan dropdown filter tanpa opsi | FE+BE | 14 | 9, 492 |
| TC-GS-NLU-E2E-006-guided-tooltip-konten-navigasi-next-back-skip-done-dan | Guided Tooltip: konten, navigasi Next Back Skip Done, dan keyboard | FE+BE | 34 | 20, 22, 24, 25, 28 |
| TC-GS-NLU-E2E-007-guided-tooltip-flag-sudah-dilihat-replay-dan-dismiss-lewat | Guided Tooltip: flag sudah dilihat, replay, dan dismiss lewat navigasi | FE+BE | 19 | 23, 26, 27 |
| TC-GS-NLU-E2E-008-role-matrix-visibilitas-menu-user-di-sidebar-dan-direct | Role Matrix: visibilitas menu User di sidebar dan direct URL tanpa capability | FE+BE | 18 | 29, 30, 31, 32, 33 |
| TC-GS-NLU-E2E-009-role-matrix-visibilitas-kontrol-tabel-total-control-read-only | Role Matrix: visibilitas kontrol tabel (Total Control, Read Only, Full CRUD) | FE+BE | 28 | 34, 35, 36 |
| TC-GS-NLU-E2E-010-role-matrix-visibilitas-kontrol-tabel-create-only-update-only | Role Matrix: visibilitas kontrol tabel (Create-Only, Update-Only) | FE+BE | 20 | 37, 38 |
| TC-GS-NLU-E2E-011-role-matrix-bulk-action-bar-per-capability | Role Matrix: Bulk Action Bar per capability | FE+BE | 23 | 41, 42, 46 |
| TC-GS-NLU-E2E-012-role-matrix-positif-eksekusi-create-update-dan-delete-per | Role Matrix positif: eksekusi Create, Update, dan Delete per capability | FE+BE | 28 | 43, 44, 45 |
| TC-GS-NLU-E2E-013-role-matrix-aksi-halaman-detail-per-capability-dan-aksi | Role Matrix: aksi halaman Detail per capability (Total Control, Update-Only, Delete-Only, Read Only) | FE+BE | 28 | 47, 48, 49, 50 |
| TC-GS-NLU-E2E-014-create-screening-popup-aksesibilitas-hover-dan-saving-state-submit | Create: screening Popup, aksesibilitas, hover dan Saving state Submit | FE+BE | 35 | 53, 54, 55 |
| TC-GS-NLU-E2E-015-create-validasi-required-dan-format-email | Create: validasi required dan format Email | FE+BE | 34 | 63, 64, 65, 69, 75 |
| TC-GS-NLU-E2E-016-create-validasi-batas-120-karakter-dan-batas-tepat-120 | Create: validasi batas 120 karakter dan batas tepat 120 | FE+BE | 25 | 66, 67 |
| TC-GS-NLU-E2E-017-create-trim-spasi-position-dan-employee-id-opsional-ukuran-foto | Create: trim spasi, Position dan Employee ID opsional, ukuran foto, dan pembatalan perubahan | FE+BE | 33 | 68, 77, 88, 89, 91 |
| TC-GS-NLU-E2E-018-create-validasi-custom-field-batas-120-required-kosong-required-terisi | Create: validasi Custom Field (batas 120, Required kosong, Required terisi) | FE+BE | 20 | 95, 456, 457 |
| TC-GS-NLU-E2E-019-create-validasi-email-sudah-dipakai-login-user-non-login-pending | Create: validasi Email sudah dipakai (Login User, Non-Login User, pending konfirmasi) | FE+BE | 34 | 70, 71, 471 |
| TC-GS-NLU-E2E-020-create-validasi-employee-id-duplikat-beda-huruf-besar-kecil-karakter-khusus | Create: validasi Employee ID duplikat, beda huruf besar kecil, dan karakter khusus | FE+BE | 25 | 72, 73, 74, 461 |
| TC-GS-NLU-E2E-021-create-temporary-user-dan-temporary-until | Create: Temporary User dan Temporary Until | FE+BE | 31 | 78, 79, 80, 90 |
| TC-GS-NLU-E2E-022-create-referensi-represented-by-dan-position-dihapus-atau-di-rename | Create: referensi Represented By dan Position dihapus atau di-rename sebelum Submit | FE+BE | 35 | 81, 82, 84 |
| TC-GS-NLU-E2E-023-create-dropdown-searchable-dan-represented-by-login-user-pending | Create: dropdown searchable dan Represented By Login User pending | FE+BE | 23 | 83, 460 |
| TC-GS-NLU-E2E-024-create-field-phone-country-code-dan-number | Create: field Phone Country Code dan Number | FE+BE | 26 | 502, 503, 504 |
| TC-GS-NLU-E2E-025-create-sukses-field-wajib-saja-dan-seluruh-field | Create sukses: field wajib saja dan seluruh field | FE+BE | 33 | 96, 97 |
| TC-GS-NLU-E2E-026-create-sukses-custom-fields-dan-stay-on-this-form | Create sukses: Custom Fields dan Stay on this form | FE+BE | 25 | 94, 98 |
| TC-GS-NLU-E2E-027-create-master-data-count-limit-tercapai-dan-kuota-gabungan | Create: Master Data Count Limit tercapai dan kuota gabungan | FE+BE | 34 | 100, 101, 430, 462 |
| TC-GS-NLU-E2E-028-create-menutup-popup-dirty-lewat-tanda-silang-esc-cancel-leave | Create: menutup Popup dirty lewat tanda silang, Esc, Cancel, dan Leave | FE+BE | 25 | 56, 57, 58, 59, 60 |
| TC-GS-NLU-E2E-029-create-klik-backdrop-clear-field-dan-klik-ganda-submit | Create: klik backdrop, Clear Field, dan klik ganda Submit | FE+BE | 29 | 61, 62, 92 |
| TC-GS-NLU-E2E-030-storage-penuh-create-dengan-foto-pada-client-storage-penuh-mb | Storage penuh: Create dengan foto pada Client Storage Penuh MB | FE+BE | 31 | 508, 509 |
| TC-GS-NLU-E2E-031-storage-penuh-edit-dan-hapus-foto-pada-client-storage-penuh-mb | Storage penuh: Edit dan hapus foto pada Client Storage Penuh MB | FE+BE | 33 | 512, 513, 514 |
| TC-GS-NLU-E2E-032-storage-format-gb-client-tanpa-kuota-batas-tepat-dan-satu-byte-di-bawah-kuota | Storage: format GB, client tanpa kuota, batas tepat, dan 1 byte di bawah kuota | FE+BE | 48 | 510, 511, 515, 516, 517 |
| TC-GS-NLU-E2E-033-popup-select-user-screening-isi-hanya-login-user-active | Popup Select User: screening, isi hanya Login User Active, pilih baris | FE+BE | 32 | 102, 103, 104 |
| TC-GS-NLU-E2E-034-popup-select-user-select-error-tanpa-pilihan-cancel-dan | Popup Select User: Select, error tanpa pilihan, Cancel dan tutup | FE+BE | 32 | 105, 106, 107 |
| TC-GS-NLU-E2E-035-popup-select-user-ikon-edit-badge-klik-badge-dan | Popup Select User: ikon edit badge, klik badge, dan Represented By Inactive | FE+BE | 27 | 108, 109, 496 |
| TC-GS-NLU-E2E-036-popup-select-user-empty-state-dan-search-per-kolom | Popup Select User: empty state dan Search per kolom | FE+BE | 35 | 111, 112, 113 |
| TC-GS-NLU-E2E-037-popup-select-user-filter-panel-dan-filter-multi-select | Popup Select User: Filter Panel dan Filter multi-select | FE+BE | 32 | 115, 116 |
| TC-GS-NLU-E2E-038-popup-select-user-search-tanggal-filter-temporary-pagination-dan-tanpa-download-changelog | Popup Select User: Search tanggal, Filter Temporary, Pagination, dan tanpa Download Changelog | FE+BE | 32 | 114, 117, 119, 120 |
| TC-GS-NLU-E2E-039-popup-select-user-column-visibility-dan-setup-column-bagian | Popup Select User: Column Visibility dan Setup Column bagian 1 | FE+BE | 35 | 121, 122, 124, 125 |
| TC-GS-NLU-E2E-040-popup-select-user-setup-column-bagian-2-pin-reset | Popup Select User: Setup Column bagian 2 (persisten, Pin, Reset) | FE+BE | 30 | 123, 126, 127 |
| TC-GS-NLU-E2E-041-popup-select-user-aksesibilitas-grid-keyboard-focus-trap | Popup Select User: aksesibilitas grid, keyboard, focus trap | FE+BE | 30 | 131, 132, 133 |
| TC-GS-NLU-E2E-042-edit-screening-popup-aksesibilitas-hover-dan-saving-state-save | Edit: screening Popup, aksesibilitas, hover dan Saving state Save | FE+BE | 35 | 134, 135, 136, 137 |
| TC-GS-NLU-E2E-043-edit-validasi-required-dan-clear-field | Edit: validasi required dan Clear Field | FE+BE | 33 | 141, 142, 143, 144 |
| TC-GS-NLU-E2E-044-edit-validasi-batas-120-karakter-dan-batas-tepat | Edit: validasi batas 120 karakter dan batas tepat | FE+BE | 27 | 145, 146 |
| TC-GS-NLU-E2E-045-edit-trim-format-email-emoji-dan-position-employee-id | Edit: trim, format Email, emoji, dan Position Employee ID opsional | FE+BE | 33 | 147, 148, 154, 156 |
| TC-GS-NLU-E2E-046-edit-validasi-email-sudah-dipakai | Edit: validasi Email sudah dipakai | FE+BE | 25 | 149, 150, 472 |
| TC-GS-NLU-E2E-047-edit-employee-id-duplikat-karakter-khusus-dan-represented-by | Edit: Employee ID duplikat, karakter khusus, dan Represented By Inactive tersimpan | FE+BE | 31 | 151, 152, 153, 481, 495 |
| TC-GS-NLU-E2E-048-edit-validasi-temporary-user-dan-temporary-until | Edit: validasi Temporary User dan Temporary Until | FE+BE | 26 | 157, 158, 159, 169 |
| TC-GS-NLU-E2E-049-edit-referensi-represented-by-position-division-custom-field-dihapus | Edit: referensi Represented By, Position, Division, Custom Field dihapus atau di-rename sebelum Save | FE+BE | 42 | 160, 161, 163, 164, 165 |
| TC-GS-NLU-E2E-050-edit-sukses-dropdown-position-division-employee-id-dan-represented | Edit sukses: dropdown, Position Division Employee ID, dan Represented By | FE+BE | 40 | 162, 173, 174 |
| TC-GS-NLU-E2E-051-edit-sukses-temporary-user-permanen-ubah-tanggal-expired | Edit sukses: Temporary User permanen, ubah tanggal, expired | FE+BE | 42 | 175, 176, 177, 178, 179 |
| TC-GS-NLU-E2E-052-edit-foto-kembali-ke-nilai-awal-klik-ganda-save | Edit: foto, kembali ke nilai awal, klik ganda Save | FE+BE | 49 | 167, 168, 170, 171, 180 |
| TC-GS-NLU-E2E-053-edit-custom-field-required-required-baru-aktif-dan-phone | Edit: Custom Field Required, Required baru aktif, dan Phone | FE+BE | 35 | 181, 458, 466, 505 |
| TC-GS-NLU-E2E-054-edit-menutup-popup-dirty-cancel-leave-backdrop | Edit: menutup Popup dirty, Cancel, Leave, backdrop | FE+BE | 27 | 138, 139, 140, 446, 447 |
| TC-GS-NLU-E2E-055-delete-single-screening-dialog-cancel-klik-ganda-dan-delete | Delete Single: Screening Dialog, Cancel, Klik Ganda, dan Delete dari Row serta Detail | FE+BE | 31 | 187, 188, 189, 191, 196 |
| TC-GS-NLU-E2E-056-delete-user-dengan-borrowed-dan-assigned-asset-aktif-dan | Delete: User dengan Borrowed dan Assigned Asset Aktif serta Pemakaian Ulang Email dan Employee ID | FE+BE | 13 | 190, 193 |
| TC-GS-NLU-E2E-057-toggle-active-single-dialog-deactivate-dan-activate-cancel-confirm | Toggle Active Single: Dialog Deactivate dan Activate, Cancel, dan Confirm | FE+BE | 22 | 197, 198, 199, 200, 201, 202 |
| TC-GS-NLU-E2E-058-toggle-active-switch-di-detail-temporary-expired-di-detail | Toggle Active: Switch di Detail, Temporary-expired di Detail, dan Klik Ganda Konfirmasi | FE+BE | 33 | 210, 211, 449, 479 |
| TC-GS-NLU-E2E-059-reactivate-temporary-expired-dialog-extend-period-make-permanent | Reactivate Temporary-expired: Dialog, Extend Period, dan Make Permanent | FE+BE | 34 | 204, 205, 206, 207 |
| TC-GS-NLU-E2E-060-reactivate-temporary-until-hari-ini-cancel-tanggal-ditolak | Reactivate: Temporary Until Hari Ini, Cancel, dan Tanggal Ditolak | FE+BE | 21 | 203, 208, 209, 467 |
| TC-GS-NLU-E2E-061-bulk-counter-checkbox-header-select-all-lintas-halaman-dan | Bulk: Counter, Checkbox Header, Select All Lintas Halaman, dan Unselect | FE+BE | 34 | 214, 215, 216, 217 |
| TC-GS-NLU-E2E-062-bulk-activate-dan-deactivate-tombol-sesuai-status-collapse-single | Bulk Activate dan Deactivate: Tombol Sesuai Status, Collapse Single, Dialog, dan Cancel | FE+BE | 33 | 220, 221, 224, 448 |
| TC-GS-NLU-E2E-063-bulk-activate-kelompok-di-skip-sebagian-gagal-seluruh-gagal | Bulk Activate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal | FE+BE | 32 | 225, 226, 229, 230, 476 |
| TC-GS-NLU-E2E-064-bulk-deactivate-kelompok-di-skip-sebagian-gagal-seluruh-gagal | Bulk Deactivate: Kelompok Di-skip, Sebagian Gagal, dan Seluruh Gagal | FE+BE | 31 | 227, 228, 470, 474, 475 |
| TC-GS-NLU-E2E-065-convert-row-dialog-cancel-confirm-status-dan-temporary-until | Convert Row: Dialog, Cancel, Confirm, serta Status dan Temporary Until | FE+BE | 27 | 232, 233, 234, 236 |
| TC-GS-NLU-E2E-066-convert-diblokir-bentrok-email-dengan-login-user | Convert Diblokir: Bentrok Email dengan Login User | FE+BE | 19 | 240, 444, 473 |
| TC-GS-NLU-E2E-067-bulk-convert-dialog-cancel-temporary-expired-satu-baris | Bulk Convert: Dialog, Cancel, Temporary-expired, dan Satu Baris | FE+BE | 33 | 242, 243, 246, 501 |
| TC-GS-NLU-E2E-068-bulk-convert-sebagian-gagal-seluruh-gagal-dan-baris-dihapus | Bulk Convert: Sebagian Gagal, Seluruh Gagal, dan Baris Dihapus Admin Lain | FE+BE | 23 | 244, 245, 442 |
| TC-GS-NLU-E2E-069-detail-screening-nilai-kosong-link-represented-by-temporary-until | Detail: Screening, Nilai Kosong, Link Represented By, Temporary Until, Custom Fields, dan Tanpa Access Level | FE+BE | 46 | 247, 248, 249, 250, 251, 252, 451, 459 |
| TC-GS-NLU-E2E-070-stale-edit-delete-dan-aksi-header-detail-pada-record | Stale: Edit, Delete, dan Aksi Header Detail pada Record Dihapus atau di-Convert Admin Lain | FE+BE | 33 | 185, 186, 194, 255, 256 |
| TC-GS-NLU-E2E-071-stale-activate-deactivate-dan-convert-pada-record-sudah-dihapus | Stale: Activate, Deactivate, dan Convert pada Record Sudah Dihapus atau di-Convert Admin Lain | FE+BE | 26 | 212, 238, 239 |
| TC-GS-NLU-E2E-072-email-aktivasi-convert-terkirim-email-terkini-dan-kegagalan-kirim | Email Aktivasi Convert: Terkirim, Email Terkini, dan Kegagalan Kirim | FE+BE | 29 | 235, 443, 463 |
| TC-GS-NLU-E2E-073-auto-deactivate-temporary-user-oleh-sistem-dan-cascade-purge | Auto-Deactivate Temporary User oleh Sistem dan Cascade Purge Foto | FE+BE | 42 | 192, 409, 410 |
| TC-GS-NLU-E2E-074-selection-limit-live-block-dan-auto-cap-select-all | Selection Limit: Live-Block dan Auto-Cap Select All | FE+BE | 16 | 218, 219 |
| TC-GS-NLU-E2E-075-download-di-atas-5-000-baris-loading-screen-lalu | Download di Atas 5.000 Baris: Loading Screen lalu Berkas Terunduh | FE+BE | 8 | 482 |
| TC-GS-NLU-E2E-076-list-search-bagian-1-substring-empty-trim-kolom-tanggal | List Search bagian 1: substring tanpa membedakan huruf besar kecil, empty state, pemangkasan spasi dan karakter khusus, kolom tanggal Last Update | FE+BE | 23 | 257, 258, 260, 261 |
| TC-GS-NLU-E2E-077-list-search-bagian-2-visibilitas-kolom-active-exact-email | List Search bagian 2: Search terikat visibilitas kolom, kolom Active exact, email bukan kolom, kolom curated dan Custom Field, nama lengkap Represented By | FE+BE | 29 | 262, 263, 264, 265, 266, 465 |
| TC-GS-NLU-E2E-078-list-filter-bagian-1-filter-panel-opsi-pencarian-opsi | List Filter bagian 1: Filter Panel, isi opsi dropdown, pencarian di dalam dropdown, dan screening kontrol | FE+BE | 21 | 267, 268, 272 |
| TC-GS-NLU-E2E-079-list-filter-bagian-2-multi-select-rentang-last-update | List Filter bagian 2: dropdown multi-select, rentang Last Update inklusif, field curated Temporary User, Temporary Until, Custom Field, dan range Numeric | FE+BE | 32 | 269, 270, 271, 468 |
| TC-GS-NLU-E2E-080-list-filter-bagian-3-kombinasi-and-lepas-kontrol-seleksi | List Filter bagian 3: kombinasi AND dengan Search, melepas satu kontrol, seleksi dipertahankan, dan Create baru yang tidak cocok | FE+BE | 45 | 275, 276, 277, 278, 279 |
| TC-GS-NLU-E2E-081-list-filter-bagian-4-opsi-dinamis-loading-opsi-chip | List Filter bagian 4: opsi dropdown dinamis, indikator loading opsi, chip +N more, dan nilai filter stale dibersihkan | FE+BE | 37 | 490, 491, 493, 500 |
| TC-GS-NLU-E2E-082-list-sort-bagian-1-tiga-tahap-per-kelas-data | List Sort bagian 1: sort tiga tahap per kelas data (teks, tanggal, boolean, curated), nilai kosong, dan ikon sort | FE+BE | 37 | 280, 281, 282, 283, 284, 285 |
| TC-GS-NLU-E2E-083-list-sort-bagian-2-kolom-curated-custom-field-per-kelas-data | List Sort bagian 2: sort tiga tahap kolom curated Custom Field per kelas data (teks, numerik, dropdown, tanggal) | FE+BE | 36 | 484, 485, 486, 489 |
| TC-GS-NLU-E2E-084-list-setup-column-bagian-1 | List Setup Column bagian 1: overlay Column Visibility, popup Setup Column, sembunyikan kolom, kolom curated, dan reorder drag | FE+BE | 29 | 286, 287, 288, 289, 290 |
| TC-GS-NLU-E2E-085-list-setup-column-bagian-2 | List Setup Column bagian 2: Pin dan Unpin, Reset to Default, tutup tanpa Save, kolom visible terakhir, cache terpisah dari Login User, dan baris yang tidak muncul | FE+BE | 38 | 291, 292, 293, 294, 295, 296 |
| TC-GS-NLU-E2E-086-list-download-fungsional-opsi-mengikuti-search-dan-filter-kolom | List Download fungsional: opsi CSV dan XLSX, mengikuti Search dan Filter, kolom visible, dan nol baris | FE+BE | 27 | 297, 299, 300, 301, 303 |
| TC-GS-NLU-E2E-087-list-download-isi-berkas-tipe-sel-bom-csv-format | List Download isi berkas: tipe sel, BOM dan escape CSV, dan format tanggal General Settings | FE+BE | 11 | 302, 304, 414 |
| TC-GS-NLU-E2E-088-list-pagination-kolom-curated-last-update-hasil-import-dan | List Pagination, kolom curated, nama panjang, Last Update hasil Import, dan hapus baris terakhir di halaman terakhir | FE+BE | 41 | 305, 306, 308, 453, 483, 307 |
| TC-GS-NLU-E2E-089-modal-changelog-agregat-screening-tutup-empty-state-format-sel | Modal Changelog Agregat: Screening, Tutup, Empty State, dan Format Sel | FE+BE | 29 | 309, 310, 311, 312 |
| TC-GS-NLU-E2E-090-modal-changelog-agregat-search | Modal Changelog Agregat: Search | FE+BE | 13 | 313, 314, 315 |
| TC-GS-NLU-E2E-091-modal-changelog-agregat-filter-dan-kombinasi | Modal Changelog Agregat: Filter dan Kombinasi | FE+BE | 29 | 316, 317, 318, 319 |
| TC-GS-NLU-E2E-092-modal-changelog-agregat-sort-pagination-download | Modal Changelog Agregat: Sort, Pagination, dan Download | FE+BE | 18 | 320, 331, 332 |
| TC-GS-NLU-E2E-093-modal-changelog-agregat-setup-column-bagian-1 | Modal Changelog Agregat: Setup Column Bagian 1 | FE+BE | 31 | 323, 324, 325, 326 |
| TC-GS-NLU-E2E-094-modal-changelog-agregat-setup-column-bagian-2 | Modal Changelog Agregat: Setup Column Bagian 2 | FE+BE | 29 | 327, 328, 329, 330 |
| TC-GS-NLU-E2E-095-tab-changelog-detail-screening-scope-entri-empty-state-search | Tab Changelog Detail: Screening, Scope Entri, Empty State, dan Search | FE+BE | 26 | 333, 334, 335, 336, 337 |
| TC-GS-NLU-E2E-096-tab-changelog-detail-filter-sort-pagination-download | Tab Changelog Detail: Filter, Sort, Pagination, dan Download | FE+BE | 29 | 338, 339, 351, 352 |
| TC-GS-NLU-E2E-097-tab-changelog-detail-setup-column-bagian-1 | Tab Changelog Detail: Setup Column Bagian 1 | FE+BE | 33 | 343, 344, 345, 346 |
| TC-GS-NLU-E2E-098-tab-changelog-detail-setup-column-bagian-2 | Tab Changelog Detail: Setup Column Bagian 2 | FE+BE | 31 | 347, 348, 349, 350 |
| TC-GS-NLU-E2E-099-responsibilities-borrowed-assets-screening-data-default-sort-scope-hanya | Responsibilities Borrowed Assets: Screening, Data, Default Sort, Scope, dan Hanya-Baca | FE+BE | 25 | 353, 354, 355, 356, 375 |
| TC-GS-NLU-E2E-100-borrowed-assets-search-dan-filter | Borrowed Assets: Search dan Filter | FE+BE | 30 | 357, 358, 359, 360 |
| TC-GS-NLU-E2E-101-borrowed-assets-sort-photo-pagination-download | Borrowed Assets: Sort, Photo, Pagination, dan Download | FE+BE | 30 | 361, 362, 363, 372, 374 |
| TC-GS-NLU-E2E-102-borrowed-assets-setup-column-bagian-1 | Borrowed Assets: Setup Column Bagian 1 | FE+BE | 33 | 364, 365, 366, 367 |
| TC-GS-NLU-E2E-103-borrowed-assets-setup-column-bagian-2 | Borrowed Assets: Setup Column Bagian 2 | FE+BE | 31 | 368, 369, 370, 371 |
| TC-GS-NLU-E2E-104-assigned-assets-screening-default-sort-search | Assigned Assets: Screening, Default Sort, dan Search | FE+BE | 17 | 377, 378, 379, 380 |
| TC-GS-NLU-E2E-105-assigned-assets-filter-sort-download-empty-state-dan-empty | Assigned Assets: Filter, Sort, Download, Empty State, dan Empty Borrowed | FE+BE | 38 | 373, 381, 382, 391, 392, 393 |
| TC-GS-NLU-E2E-106-assigned-assets-setup-column-bagian-1 | Assigned Assets: Setup Column Bagian 1 | FE+BE | 33 | 383, 384, 385, 386 |
| TC-GS-NLU-E2E-107-assigned-assets-setup-column-bagian-2 | Assigned Assets: Setup Column Bagian 2 | FE+BE | 31 | 387, 388, 389, 390 |
| TC-GS-NLU-E2E-108-log-tiga-surface-create-edit-per-field-represented-by | Log tiga surface: Create, Edit per field, Represented By, Photo | FE+BE | 85 | 394, 395, 396, 397 |
| TC-GS-NLU-E2E-109-log-tiga-surface-delete-activate-deactivate-convert-set-temporary | Log tiga surface: Delete, Activate Deactivate, Convert, Set Temporary | FE+BE | 75 | 398, 399, 400, 401 |
| TC-GS-NLU-E2E-110-log-tiga-surface-remove-temporary-reactivate-snapshot-immutability | Log tiga surface: Remove Temporary, Reactivate, snapshot immutability | FE+BE | 73 | 402, 403, 404, 405 |
| TC-GS-NLU-E2E-111-log-entri-per-baris-bulk-dan-format-kolom-changelog | Log: entri per baris Bulk dan format kolom Changelog | FE+BE | 61 | 406, 407, 408, 506, 507 |
| TC-GS-NLU-E2E-112-absence-log-edit-tanpa-perubahan-import-dan-delete-login | Absence log: Edit tanpa perubahan, Import, dan Delete Login User pointer | FE+BE | 47 | 182, 183, 425, 469 |
| TC-GS-NLU-E2E-113-sinkronisasi-format-tanggal-general-settings | Sinkronisasi format tanggal General Settings | FE+BE | 17 | 411, 412, 413 |
| TC-GS-NLU-E2E-114-sinkronisasi-login-user-delete-mengosongkan-pointer-represented-by-dan-log | Sinkronisasi Login User: Delete mengosongkan pointer Represented By, log Edit, dan pointer kosong | FE+BE | 27 | 415, 416, 417 |
| TC-GS-NLU-E2E-115-sinkronisasi-master-data-rename-position-division-dan-custom-field | Sinkronisasi master data: rename Position Division dan Custom Field | FE+BE | 33 | 420, 421, 422, 423 |
| TC-GS-NLU-E2E-116-sinkronisasi-import-dan-convert-detail-login-user-changelog-tab | Sinkronisasi Import dan Convert: Detail Login User, Changelog, tab Non-Login User | FE+BE | 34 | 424, 426, 427, 428, 429 |
| TC-GS-NLU-E2E-117-defense-in-depth-server-menolak-aksi-tulis-tanpa-capability | Defense-in-depth: server menolak aksi tulis tanpa capability | FE+BE | 23 | 431, 432, 433, 434, 435, 436 |
| TC-GS-NLU-E2E-118-defense-in-depth-payload-skrip-perubahan-tipe-user-url | Defense-in-depth: payload skrip, perubahan tipe user, URL Detail tidak valid, isolasi entitas | FE+BE | 32 | 437, 445, 452, 455 |
| TC-GS-NLU-E2E-119-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis | State tenant: Client Suspended dan Expired menolak aksi tulis, Auto-Deactivate di Suspended | FE+BE | 45 | 438, 439, 497 |
| TC-GS-NLU-E2E-120-state-tenant-plan-tier-dan-subscription-fams | State tenant: plan tier dan subscription FAMS | FE+BE | 18 | 454, 464 |
| TC-GS-NLU-E2E-121-multi-konteks-dua-admin-edit-create-email-sama-employee | Multi-konteks: dua admin Edit, Create email sama, Employee ID sama, slot terakhir limit | FE+BE | 40 | 184, 440, 441, 478 |
| TC-GS-NLU-E2E-122-resilience-baca-error-load-tabel-changelog-assigned-assets-popup | Resilience baca: error load tabel, changelog, Assigned Assets, Popup Select User, Borrowed Assets | FE+BE | 47 | 11, 376, 477 |
| TC-GS-NLU-E2E-123-resilience-tulis-kegagalan-5xx-saat-create-dan-edit-mempertahankan | Resilience tulis: kegagalan 5xx saat Create dan Edit mempertahankan isian | FE+BE | 23 | 93, 172 |
| TC-GS-NLU-E2E-124-resilience-aksi-kegagalan-server-saat-delete-toggle-bulk-convert | Resilience aksi: kegagalan server saat Delete, Toggle, Bulk Convert, Convert | FE+BE | 41 | 195, 213, 231, 241 |
| TC-GS-NLU-E2E-125-role-matrix-menu-detail-tidak-dirender-dan-aksi-tanpa-kondisi-disabled | Role Matrix: menu `⋯` Detail tidak dirender (Create-Only, Read-Only role) dan aksi tanpa kondisi Disabled | FE+BE | 26 | 51, 52 |
| TC-GS-NLU-E2E-126-role-matrix-visibilitas-kontrol-tabel-delete-only-read-only-role | Role Matrix: visibilitas kontrol tabel (Delete-Only, Read-Only role) | FE+BE | 22 | 39, 40 |
| TC-GS-NLU-E2E-127-create-referensi-division-dan-custom-field-dropdown-dihapus | Create: referensi Division dan Custom Field dropdown dihapus sebelum Submit | FE+BE | 24 | 85, 86 |
| TC-GS-NLU-E2E-128-create-beruntun-dua-belas-data-lewat-stay-on-this-form | Create beruntun: dua belas data lewat Stay on this form | FE+BE | 10 | 99 |
| TC-GS-NLU-E2E-129-popup-select-user-setup-column-bagian-3-tutup-kolom-terakhir-cache | Popup Select User: Setup Column bagian 3 (tutup tanpa Save, kolom terakhir, cache) | FE+BE | 30 | 128, 129, 130 |
| TC-GS-NLU-E2E-130-popup-select-user-sort-tiga-tahap-per-kolom | Popup Select User: Sort tiga tahap per kolom | FE+BE | 16 | 118 |
| TC-GS-NLU-E2E-131-convert-klik-ganda-dan-convert-dari-menu-detail | Convert: Klik Ganda pada Konfirmasi dan Convert dari Menu Detail | FE+BE | 18 | 450, 237 |
| TC-GS-NLU-E2E-132-bulk-deactivate-dan-activate-dialog-dua-belas-nama-tanpa-ringkasan | Bulk Deactivate dan Activate: Dialog 12 Nama Tanpa Ringkasan | FE+BE | 21 | 222, 223 |
| TC-GS-NLU-E2E-133-list-search-siklus-interaksi-reveal-clear-collapse | List Search: siklus interaksi reveal, clear, dan collapse kotak Search | FE+BE | 17 | 259 |
| TC-GS-NLU-E2E-134-list-filter-chip-opsi-dan-tutup-tanpa-apply | List Filter: chip opsi dihapus lewat tombol silang dan checkbox, serta menutup Filter Panel tanpa Apply | FE+BE | 24 | 273, 494, 274 |
| TC-GS-NLU-E2E-135-modal-changelog-agregat-sort-kelas-tanggal-dan-campuran | Modal Changelog Agregat: Sort Kelas Tanggal dan Campuran Tipe Data | FE+BE | 14 | 321, 322 |
| TC-GS-NLU-E2E-136-tab-changelog-detail-sort-tiga-kelas | Tab Changelog Detail: Sort Kelas Teks, Tanggal, dan Campuran Tipe Data | FE+BE | 21 | 340, 341, 342 |
| TC-GS-NLU-E2E-137-sinkronisasi-login-user-deactivate-remove-access-dan-rename-mempertahankan-relasi | Sinkronisasi Login User: Deactivate, Remove Access, dan rename mempertahankan relasi Represented By | FE+BE | 25 | 418, 480, 419 |
| TC-GS-NLU-E2E-138-resilience-aksi-kegagalan-server-saat-download | Resilience aksi: kegagalan server saat Download list, Changelog, Borrowed Assets, Assigned Assets | FE+BE | 26 | 298, 498 |

## Pembagian TC lintas spec

Tidak ada TC yang terbelah antar spec. Pergeseran dari rencana awal (nomor cadangan): TC-39, 40 → spec 126; TC-51, 52 → 125; TC-99 → 128; TC-118 → 130; TC-128, 129, 130 → 129; TC-259 → 133; TC-273, 274, 494 → 134; TC-321, 322 → 135; TC-340, 341, 342 → 136; TC-418, 419, 480 → 137; TC-298, 498 → 138; TC-222, 223 → 132; TC-237, 450 → 131; TC-117 → spec 038; TC-123 → spec 040; TC-85, 86 → spec 127.

## Kebutuhan lingkungan (tim FE)

- Env var baru yang diusulkan, belum didaftarkan di `spectra.config.ts` dan `.env.example`: `GS_BINTANGTIMUR_TC_PASSWORD`, `GS_FIRSTVISIT_TC_PASSWORD`, `GS_VOLUME_TC_PASSWORD`, `GS_STORAGEMB_TC_PASSWORD`, `GS_STORAGEGB_TC_PASSWORD`, `GS_STORAGENOQUOTA_TC_PASSWORD`, `GS_STORAGEEDGE_TC_PASSWORD`, `GS_STORAGENEAR_TC_PASSWORD`, `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTEXP_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`, `GS_NOFAMS_TC_PASSWORD`, `GS_TC2_PASSWORD`. Email akun-akun ini belum ada di Tabel Pre-setup; bagian `{namaCompany}` perlu dikonfirmasi tim FE.
- Fixture `fixtures/non-login-user.json` belum ada; nilai ditulis literal di tiap spec.
- Kemampuan teknis yang ditulis 'disediakan tim FE/BE': seeding dan pembersihan Non-Login User bersuffix `{runId}`, sesi API aktor kedua, penyetelan flag Guided Tooltip, pembacaan jumlah entri Changelog, Activity Log dan System Log, penyetelan Master Data Count Limit, Selection Limit, Storage dan plan Client, data FAMS, intercept jaringan, injeksi tanggal ke date picker, penghitung request, pembacaan isi berkas unduhan.

## Temuan yang masih terbuka

- Spec di atas ~35 langkah dengan alasan di Notes masing-masing: 032 (48), 049 (42), 050 (40), 051 (42), 052 (49), 069 (46), 073 (42), 080 (45), 081 (37), 082 (37), 083 (36), 085 (38), 088 (41), 105 (38), 108 (85), 109 (75), 110 (73), 111 (61), 112 (47), 119 (45), 121 (40), 122 (47), 124 (41).
- Kolom Email/akun aktor memakai placeholder `{namaCompany}` dan `GS_TC_PASSWORD`; komentar `.env.example` memuat email lain, perlu konfirmasi tim FE.
- Download isi berkas untuk Changelog dan Assets (TC-332, 351, 372, 391) hanya diasersi sampai nama berkas, header dan jumlah baris.
- Kolom PIC pada Assigned/Borrowed Assets hanya punya satu nilai di Pre-setup, sehingga sort PIC (TC-361, 382) belum membuktikan urutan.
- TC bertanda Manual Only (mis. TC-235, 409, 410, 443, 497) tetap ditulis sebagai spec dengan kebutuhan teknis di Prerequisites.
- Masalah sumber TC lain tercatat per spec di Notes 'Temuan untuk QA'.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-NLU-1 | TC-GS-NLU-E2E-001 | FE+BE |
| TC-GS-NLU-2 | TC-GS-NLU-E2E-001 | FE+BE |
| TC-GS-NLU-3 | TC-GS-NLU-E2E-001 | FE+BE |
| TC-GS-NLU-4 | TC-GS-NLU-E2E-001 | FE+BE |
| TC-GS-NLU-5 | TC-GS-NLU-E2E-001 | FE+BE |
| TC-GS-NLU-6 | TC-GS-NLU-E2E-002 | FE+BE |
| TC-GS-NLU-7 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-8 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-9 | TC-GS-NLU-E2E-005 | FE+BE |
| TC-GS-NLU-10 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-11 | TC-GS-NLU-E2E-122 | FE+BE |
| TC-GS-NLU-12 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-13 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-14 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-15 | TC-GS-NLU-E2E-003 | FE+BE |
| TC-GS-NLU-16 | TC-GS-NLU-E2E-004 | FE+BE |
| TC-GS-NLU-17 | TC-GS-NLU-E2E-004 | FE+BE |
| TC-GS-NLU-18 | TC-GS-NLU-E2E-004 | FE+BE |
| TC-GS-NLU-19 | TC-GS-NLU-E2E-004 | FE+BE |
| TC-GS-NLU-20 | TC-GS-NLU-E2E-006 | FE+BE |
| TC-GS-NLU-22 | TC-GS-NLU-E2E-006 | FE+BE |
| TC-GS-NLU-23 | TC-GS-NLU-E2E-007 | FE+BE |
| TC-GS-NLU-24 | TC-GS-NLU-E2E-006 | FE+BE |
| TC-GS-NLU-25 | TC-GS-NLU-E2E-006 | FE+BE |
| TC-GS-NLU-26 | TC-GS-NLU-E2E-007 | FE+BE |
| TC-GS-NLU-27 | TC-GS-NLU-E2E-007 | FE+BE |
| TC-GS-NLU-28 | TC-GS-NLU-E2E-006 | FE+BE |
| TC-GS-NLU-29 | TC-GS-NLU-E2E-008 | FE+BE |
| TC-GS-NLU-30 | TC-GS-NLU-E2E-008 | FE+BE |
| TC-GS-NLU-31 | TC-GS-NLU-E2E-008 | FE+BE |
| TC-GS-NLU-32 | TC-GS-NLU-E2E-008 | FE+BE |
| TC-GS-NLU-33 | TC-GS-NLU-E2E-008 | FE+BE |
| TC-GS-NLU-34 | TC-GS-NLU-E2E-009 | FE+BE |
| TC-GS-NLU-35 | TC-GS-NLU-E2E-009 | FE+BE |
| TC-GS-NLU-36 | TC-GS-NLU-E2E-009 | FE+BE |
| TC-GS-NLU-37 | TC-GS-NLU-E2E-010 | FE+BE |
| TC-GS-NLU-38 | TC-GS-NLU-E2E-010 | FE+BE |
| TC-GS-NLU-39 | TC-GS-NLU-E2E-126 | FE+BE |
| TC-GS-NLU-40 | TC-GS-NLU-E2E-126 | FE+BE |
| TC-GS-NLU-41 | TC-GS-NLU-E2E-011 | FE+BE |
| TC-GS-NLU-42 | TC-GS-NLU-E2E-011 | FE+BE |
| TC-GS-NLU-43 | TC-GS-NLU-E2E-012 | FE+BE |
| TC-GS-NLU-44 | TC-GS-NLU-E2E-012 | FE+BE |
| TC-GS-NLU-45 | TC-GS-NLU-E2E-012 | FE+BE |
| TC-GS-NLU-46 | TC-GS-NLU-E2E-011 | FE+BE |
| TC-GS-NLU-47 | TC-GS-NLU-E2E-013 | FE+BE |
| TC-GS-NLU-48 | TC-GS-NLU-E2E-013 | FE+BE |
| TC-GS-NLU-49 | TC-GS-NLU-E2E-013 | FE+BE |
| TC-GS-NLU-50 | TC-GS-NLU-E2E-013 | FE+BE |
| TC-GS-NLU-51 | TC-GS-NLU-E2E-125 | FE+BE |
| TC-GS-NLU-52 | TC-GS-NLU-E2E-125 | FE+BE |
| TC-GS-NLU-53 | TC-GS-NLU-E2E-014 | FE+BE |
| TC-GS-NLU-54 | TC-GS-NLU-E2E-014 | FE+BE |
| TC-GS-NLU-55 | TC-GS-NLU-E2E-014 | FE+BE |
| TC-GS-NLU-56 | TC-GS-NLU-E2E-028 | FE+BE |
| TC-GS-NLU-57 | TC-GS-NLU-E2E-028 | FE+BE |
| TC-GS-NLU-58 | TC-GS-NLU-E2E-028 | FE+BE |
| TC-GS-NLU-59 | TC-GS-NLU-E2E-028 | FE+BE |
| TC-GS-NLU-60 | TC-GS-NLU-E2E-028 | FE+BE |
| TC-GS-NLU-61 | TC-GS-NLU-E2E-029 | FE+BE |
| TC-GS-NLU-62 | TC-GS-NLU-E2E-029 | FE+BE |
| TC-GS-NLU-63 | TC-GS-NLU-E2E-015 | FE+BE |
| TC-GS-NLU-64 | TC-GS-NLU-E2E-015 | FE+BE |
| TC-GS-NLU-65 | TC-GS-NLU-E2E-015 | FE+BE |
| TC-GS-NLU-66 | TC-GS-NLU-E2E-016 | FE+BE |
| TC-GS-NLU-67 | TC-GS-NLU-E2E-016 | FE+BE |
| TC-GS-NLU-68 | TC-GS-NLU-E2E-017 | FE+BE |
| TC-GS-NLU-69 | TC-GS-NLU-E2E-015 | FE+BE |
| TC-GS-NLU-70 | TC-GS-NLU-E2E-019 | FE+BE |
| TC-GS-NLU-71 | TC-GS-NLU-E2E-019 | FE+BE |
| TC-GS-NLU-72 | TC-GS-NLU-E2E-020 | FE+BE |
| TC-GS-NLU-73 | TC-GS-NLU-E2E-020 | FE+BE |
| TC-GS-NLU-74 | TC-GS-NLU-E2E-020 | FE+BE |
| TC-GS-NLU-75 | TC-GS-NLU-E2E-015 | FE+BE |
| TC-GS-NLU-77 | TC-GS-NLU-E2E-017 | FE+BE |
| TC-GS-NLU-78 | TC-GS-NLU-E2E-021 | FE+BE |
| TC-GS-NLU-79 | TC-GS-NLU-E2E-021 | FE+BE |
| TC-GS-NLU-80 | TC-GS-NLU-E2E-021 | FE+BE |
| TC-GS-NLU-81 | TC-GS-NLU-E2E-022 | FE+BE |
| TC-GS-NLU-82 | TC-GS-NLU-E2E-022 | FE+BE |
| TC-GS-NLU-83 | TC-GS-NLU-E2E-023 | FE+BE |
| TC-GS-NLU-84 | TC-GS-NLU-E2E-022 | FE+BE |
| TC-GS-NLU-85 | TC-GS-NLU-E2E-127 | FE+BE |
| TC-GS-NLU-86 | TC-GS-NLU-E2E-127 | FE+BE |
| TC-GS-NLU-88 | TC-GS-NLU-E2E-017 | FE+BE |
| TC-GS-NLU-89 | TC-GS-NLU-E2E-017 | FE+BE |
| TC-GS-NLU-90 | TC-GS-NLU-E2E-021 | FE+BE |
| TC-GS-NLU-91 | TC-GS-NLU-E2E-017 | FE+BE |
| TC-GS-NLU-92 | TC-GS-NLU-E2E-029 | FE+BE |
| TC-GS-NLU-93 | TC-GS-NLU-E2E-123 | FE+BE |
| TC-GS-NLU-94 | TC-GS-NLU-E2E-026 | FE+BE |
| TC-GS-NLU-95 | TC-GS-NLU-E2E-018 | FE+BE |
| TC-GS-NLU-96 | TC-GS-NLU-E2E-025 | FE+BE |
| TC-GS-NLU-97 | TC-GS-NLU-E2E-025 | FE+BE |
| TC-GS-NLU-98 | TC-GS-NLU-E2E-026 | FE+BE |
| TC-GS-NLU-99 | TC-GS-NLU-E2E-128 | FE+BE |
| TC-GS-NLU-100 | TC-GS-NLU-E2E-027 | FE+BE |
| TC-GS-NLU-101 | TC-GS-NLU-E2E-027 | FE+BE |
| TC-GS-NLU-102 | TC-GS-NLU-E2E-033 | FE+BE |
| TC-GS-NLU-103 | TC-GS-NLU-E2E-033 | FE+BE |
| TC-GS-NLU-104 | TC-GS-NLU-E2E-033 | FE+BE |
| TC-GS-NLU-105 | TC-GS-NLU-E2E-034 | FE+BE |
| TC-GS-NLU-106 | TC-GS-NLU-E2E-034 | FE+BE |
| TC-GS-NLU-107 | TC-GS-NLU-E2E-034 | FE+BE |
| TC-GS-NLU-108 | TC-GS-NLU-E2E-035 | FE+BE |
| TC-GS-NLU-109 | TC-GS-NLU-E2E-035 | FE+BE |
| TC-GS-NLU-111 | TC-GS-NLU-E2E-036 | FE+BE |
| TC-GS-NLU-112 | TC-GS-NLU-E2E-036 | FE+BE |
| TC-GS-NLU-113 | TC-GS-NLU-E2E-036 | FE+BE |
| TC-GS-NLU-114 | TC-GS-NLU-E2E-038 | FE+BE |
| TC-GS-NLU-115 | TC-GS-NLU-E2E-037 | FE+BE |
| TC-GS-NLU-116 | TC-GS-NLU-E2E-037 | FE+BE |
| TC-GS-NLU-117 | TC-GS-NLU-E2E-038 | FE+BE |
| TC-GS-NLU-118 | TC-GS-NLU-E2E-130 | FE+BE |
| TC-GS-NLU-119 | TC-GS-NLU-E2E-038 | FE+BE |
| TC-GS-NLU-120 | TC-GS-NLU-E2E-038 | FE+BE |
| TC-GS-NLU-121 | TC-GS-NLU-E2E-039 | FE+BE |
| TC-GS-NLU-122 | TC-GS-NLU-E2E-039 | FE+BE |
| TC-GS-NLU-123 | TC-GS-NLU-E2E-040 | FE+BE |
| TC-GS-NLU-124 | TC-GS-NLU-E2E-039 | FE+BE |
| TC-GS-NLU-125 | TC-GS-NLU-E2E-039 | FE+BE |
| TC-GS-NLU-126 | TC-GS-NLU-E2E-040 | FE+BE |
| TC-GS-NLU-127 | TC-GS-NLU-E2E-040 | FE+BE |
| TC-GS-NLU-128 | TC-GS-NLU-E2E-129 | FE+BE |
| TC-GS-NLU-129 | TC-GS-NLU-E2E-129 | FE+BE |
| TC-GS-NLU-130 | TC-GS-NLU-E2E-129 | FE+BE |
| TC-GS-NLU-131 | TC-GS-NLU-E2E-041 | FE+BE |
| TC-GS-NLU-132 | TC-GS-NLU-E2E-041 | FE+BE |
| TC-GS-NLU-133 | TC-GS-NLU-E2E-041 | FE+BE |
| TC-GS-NLU-134 | TC-GS-NLU-E2E-042 | FE+BE |
| TC-GS-NLU-135 | TC-GS-NLU-E2E-042 | FE+BE |
| TC-GS-NLU-136 | TC-GS-NLU-E2E-042 | FE+BE |
| TC-GS-NLU-137 | TC-GS-NLU-E2E-042 | FE+BE |
| TC-GS-NLU-138 | TC-GS-NLU-E2E-054 | FE+BE |
| TC-GS-NLU-139 | TC-GS-NLU-E2E-054 | FE+BE |
| TC-GS-NLU-140 | TC-GS-NLU-E2E-054 | FE+BE |
| TC-GS-NLU-141 | TC-GS-NLU-E2E-043 | FE+BE |
| TC-GS-NLU-142 | TC-GS-NLU-E2E-043 | FE+BE |
| TC-GS-NLU-143 | TC-GS-NLU-E2E-043 | FE+BE |
| TC-GS-NLU-144 | TC-GS-NLU-E2E-043 | FE+BE |
| TC-GS-NLU-145 | TC-GS-NLU-E2E-044 | FE+BE |
| TC-GS-NLU-146 | TC-GS-NLU-E2E-044 | FE+BE |
| TC-GS-NLU-147 | TC-GS-NLU-E2E-045 | FE+BE |
| TC-GS-NLU-148 | TC-GS-NLU-E2E-045 | FE+BE |
| TC-GS-NLU-149 | TC-GS-NLU-E2E-046 | FE+BE |
| TC-GS-NLU-150 | TC-GS-NLU-E2E-046 | FE+BE |
| TC-GS-NLU-151 | TC-GS-NLU-E2E-047 | FE+BE |
| TC-GS-NLU-152 | TC-GS-NLU-E2E-047 | FE+BE |
| TC-GS-NLU-153 | TC-GS-NLU-E2E-047 | FE+BE |
| TC-GS-NLU-154 | TC-GS-NLU-E2E-045 | FE+BE |
| TC-GS-NLU-156 | TC-GS-NLU-E2E-045 | FE+BE |
| TC-GS-NLU-157 | TC-GS-NLU-E2E-048 | FE+BE |
| TC-GS-NLU-158 | TC-GS-NLU-E2E-048 | FE+BE |
| TC-GS-NLU-159 | TC-GS-NLU-E2E-048 | FE+BE |
| TC-GS-NLU-160 | TC-GS-NLU-E2E-049 | FE+BE |
| TC-GS-NLU-161 | TC-GS-NLU-E2E-049 | FE+BE |
| TC-GS-NLU-162 | TC-GS-NLU-E2E-050 | FE+BE |
| TC-GS-NLU-163 | TC-GS-NLU-E2E-049 | FE+BE |
| TC-GS-NLU-164 | TC-GS-NLU-E2E-049 | FE+BE |
| TC-GS-NLU-165 | TC-GS-NLU-E2E-049 | FE+BE |
| TC-GS-NLU-167 | TC-GS-NLU-E2E-052 | FE+BE |
| TC-GS-NLU-168 | TC-GS-NLU-E2E-052 | FE+BE |
| TC-GS-NLU-169 | TC-GS-NLU-E2E-048 | FE+BE |
| TC-GS-NLU-170 | TC-GS-NLU-E2E-052 | FE+BE |
| TC-GS-NLU-171 | TC-GS-NLU-E2E-052 | FE+BE |
| TC-GS-NLU-172 | TC-GS-NLU-E2E-123 | FE+BE |
| TC-GS-NLU-173 | TC-GS-NLU-E2E-050 | FE+BE |
| TC-GS-NLU-174 | TC-GS-NLU-E2E-050 | FE+BE |
| TC-GS-NLU-175 | TC-GS-NLU-E2E-051 | FE+BE |
| TC-GS-NLU-176 | TC-GS-NLU-E2E-051 | FE+BE |
| TC-GS-NLU-177 | TC-GS-NLU-E2E-051 | FE+BE |
| TC-GS-NLU-178 | TC-GS-NLU-E2E-051 | FE+BE |
| TC-GS-NLU-179 | TC-GS-NLU-E2E-051 | FE+BE |
| TC-GS-NLU-180 | TC-GS-NLU-E2E-052 | FE+BE |
| TC-GS-NLU-181 | TC-GS-NLU-E2E-053 | FE+BE |
| TC-GS-NLU-182 | TC-GS-NLU-E2E-112 | FE+BE |
| TC-GS-NLU-183 | TC-GS-NLU-E2E-112 | FE+BE |
| TC-GS-NLU-184 | TC-GS-NLU-E2E-121 | FE+BE |
| TC-GS-NLU-185 | TC-GS-NLU-E2E-070 | FE+BE |
| TC-GS-NLU-186 | TC-GS-NLU-E2E-070 | FE+BE |
| TC-GS-NLU-187 | TC-GS-NLU-E2E-055 | FE+BE |
| TC-GS-NLU-188 | TC-GS-NLU-E2E-055 | FE+BE |
| TC-GS-NLU-189 | TC-GS-NLU-E2E-055 | FE+BE |
| TC-GS-NLU-190 | TC-GS-NLU-E2E-056 | FE+BE |
| TC-GS-NLU-191 | TC-GS-NLU-E2E-055 | FE+BE |
| TC-GS-NLU-192 | TC-GS-NLU-E2E-073 | FE+BE |
| TC-GS-NLU-193 | TC-GS-NLU-E2E-056 | FE+BE |
| TC-GS-NLU-194 | TC-GS-NLU-E2E-070 | FE+BE |
| TC-GS-NLU-195 | TC-GS-NLU-E2E-124 | FE+BE |
| TC-GS-NLU-196 | TC-GS-NLU-E2E-055 | FE+BE |
| TC-GS-NLU-197 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-198 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-199 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-200 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-201 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-202 | TC-GS-NLU-E2E-057 | FE+BE |
| TC-GS-NLU-203 | TC-GS-NLU-E2E-060 | FE+BE |
| TC-GS-NLU-204 | TC-GS-NLU-E2E-059 | FE+BE |
| TC-GS-NLU-205 | TC-GS-NLU-E2E-059 | FE+BE |
| TC-GS-NLU-206 | TC-GS-NLU-E2E-059 | FE+BE |
| TC-GS-NLU-207 | TC-GS-NLU-E2E-059 | FE+BE |
| TC-GS-NLU-208 | TC-GS-NLU-E2E-060 | FE+BE |
| TC-GS-NLU-209 | TC-GS-NLU-E2E-060 | FE+BE |
| TC-GS-NLU-210 | TC-GS-NLU-E2E-058 | FE+BE |
| TC-GS-NLU-211 | TC-GS-NLU-E2E-058 | FE+BE |
| TC-GS-NLU-212 | TC-GS-NLU-E2E-071 | FE+BE |
| TC-GS-NLU-213 | TC-GS-NLU-E2E-124 | FE+BE |
| TC-GS-NLU-214 | TC-GS-NLU-E2E-061 | FE+BE |
| TC-GS-NLU-215 | TC-GS-NLU-E2E-061 | FE+BE |
| TC-GS-NLU-216 | TC-GS-NLU-E2E-061 | FE+BE |
| TC-GS-NLU-217 | TC-GS-NLU-E2E-061 | FE+BE |
| TC-GS-NLU-218 | TC-GS-NLU-E2E-074 | FE+BE |
| TC-GS-NLU-219 | TC-GS-NLU-E2E-074 | FE+BE |
| TC-GS-NLU-220 | TC-GS-NLU-E2E-062 | FE+BE |
| TC-GS-NLU-221 | TC-GS-NLU-E2E-062 | FE+BE |
| TC-GS-NLU-222 | TC-GS-NLU-E2E-132 | FE+BE |
| TC-GS-NLU-223 | TC-GS-NLU-E2E-132 | FE+BE |
| TC-GS-NLU-224 | TC-GS-NLU-E2E-062 | FE+BE |
| TC-GS-NLU-225 | TC-GS-NLU-E2E-063 | FE+BE |
| TC-GS-NLU-226 | TC-GS-NLU-E2E-063 | FE+BE |
| TC-GS-NLU-227 | TC-GS-NLU-E2E-064 | FE+BE |
| TC-GS-NLU-228 | TC-GS-NLU-E2E-064 | FE+BE |
| TC-GS-NLU-229 | TC-GS-NLU-E2E-063 | FE+BE |
| TC-GS-NLU-230 | TC-GS-NLU-E2E-063 | FE+BE |
| TC-GS-NLU-231 | TC-GS-NLU-E2E-124 | FE+BE |
| TC-GS-NLU-232 | TC-GS-NLU-E2E-065 | FE+BE |
| TC-GS-NLU-233 | TC-GS-NLU-E2E-065 | FE+BE |
| TC-GS-NLU-234 | TC-GS-NLU-E2E-065 | FE+BE |
| TC-GS-NLU-235 | TC-GS-NLU-E2E-072 | FE+BE |
| TC-GS-NLU-236 | TC-GS-NLU-E2E-065 | FE+BE |
| TC-GS-NLU-237 | TC-GS-NLU-E2E-131 | FE+BE |
| TC-GS-NLU-238 | TC-GS-NLU-E2E-071 | FE+BE |
| TC-GS-NLU-239 | TC-GS-NLU-E2E-071 | FE+BE |
| TC-GS-NLU-240 | TC-GS-NLU-E2E-066 | FE+BE |
| TC-GS-NLU-241 | TC-GS-NLU-E2E-124 | FE+BE |
| TC-GS-NLU-242 | TC-GS-NLU-E2E-067 | FE+BE |
| TC-GS-NLU-243 | TC-GS-NLU-E2E-067 | FE+BE |
| TC-GS-NLU-244 | TC-GS-NLU-E2E-068 | FE+BE |
| TC-GS-NLU-245 | TC-GS-NLU-E2E-068 | FE+BE |
| TC-GS-NLU-246 | TC-GS-NLU-E2E-067 | FE+BE |
| TC-GS-NLU-247 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-248 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-249 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-250 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-251 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-252 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-253 | TC-GS-NLU-E2E-002 | FE+BE |
| TC-GS-NLU-254 | TC-GS-NLU-E2E-002 | FE+BE |
| TC-GS-NLU-255 | TC-GS-NLU-E2E-070 | FE+BE |
| TC-GS-NLU-256 | TC-GS-NLU-E2E-070 | FE+BE |
| TC-GS-NLU-257 | TC-GS-NLU-E2E-076 | FE+BE |
| TC-GS-NLU-258 | TC-GS-NLU-E2E-076 | FE+BE |
| TC-GS-NLU-259 | TC-GS-NLU-E2E-133 | FE+BE |
| TC-GS-NLU-260 | TC-GS-NLU-E2E-076 | FE+BE |
| TC-GS-NLU-261 | TC-GS-NLU-E2E-076 | FE+BE |
| TC-GS-NLU-262 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-263 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-264 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-265 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-266 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-267 | TC-GS-NLU-E2E-078 | FE+BE |
| TC-GS-NLU-268 | TC-GS-NLU-E2E-078 | FE+BE |
| TC-GS-NLU-269 | TC-GS-NLU-E2E-079 | FE+BE |
| TC-GS-NLU-270 | TC-GS-NLU-E2E-079 | FE+BE |
| TC-GS-NLU-271 | TC-GS-NLU-E2E-079 | FE+BE |
| TC-GS-NLU-272 | TC-GS-NLU-E2E-078 | FE+BE |
| TC-GS-NLU-273 | TC-GS-NLU-E2E-134 | FE+BE |
| TC-GS-NLU-274 | TC-GS-NLU-E2E-134 | FE+BE |
| TC-GS-NLU-275 | TC-GS-NLU-E2E-080 | FE+BE |
| TC-GS-NLU-276 | TC-GS-NLU-E2E-080 | FE+BE |
| TC-GS-NLU-277 | TC-GS-NLU-E2E-080 | FE+BE |
| TC-GS-NLU-278 | TC-GS-NLU-E2E-080 | FE+BE |
| TC-GS-NLU-279 | TC-GS-NLU-E2E-080 | FE+BE |
| TC-GS-NLU-280 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-281 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-282 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-283 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-284 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-285 | TC-GS-NLU-E2E-082 | FE+BE |
| TC-GS-NLU-286 | TC-GS-NLU-E2E-084 | FE+BE |
| TC-GS-NLU-287 | TC-GS-NLU-E2E-084 | FE+BE |
| TC-GS-NLU-288 | TC-GS-NLU-E2E-084 | FE+BE |
| TC-GS-NLU-289 | TC-GS-NLU-E2E-084 | FE+BE |
| TC-GS-NLU-290 | TC-GS-NLU-E2E-084 | FE+BE |
| TC-GS-NLU-291 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-292 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-293 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-294 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-295 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-296 | TC-GS-NLU-E2E-085 | FE+BE |
| TC-GS-NLU-297 | TC-GS-NLU-E2E-086 | FE+BE |
| TC-GS-NLU-298 | TC-GS-NLU-E2E-138 | FE+BE |
| TC-GS-NLU-299 | TC-GS-NLU-E2E-086 | FE+BE |
| TC-GS-NLU-300 | TC-GS-NLU-E2E-086 | FE+BE |
| TC-GS-NLU-301 | TC-GS-NLU-E2E-086 | FE+BE |
| TC-GS-NLU-302 | TC-GS-NLU-E2E-087 | FE+BE |
| TC-GS-NLU-303 | TC-GS-NLU-E2E-086 | FE+BE |
| TC-GS-NLU-304 | TC-GS-NLU-E2E-087 | FE+BE |
| TC-GS-NLU-305 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-306 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-307 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-308 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-309 | TC-GS-NLU-E2E-089 | FE+BE |
| TC-GS-NLU-310 | TC-GS-NLU-E2E-089 | FE+BE |
| TC-GS-NLU-311 | TC-GS-NLU-E2E-089 | FE+BE |
| TC-GS-NLU-312 | TC-GS-NLU-E2E-089 | FE+BE |
| TC-GS-NLU-313 | TC-GS-NLU-E2E-090 | FE+BE |
| TC-GS-NLU-314 | TC-GS-NLU-E2E-090 | FE+BE |
| TC-GS-NLU-315 | TC-GS-NLU-E2E-090 | FE+BE |
| TC-GS-NLU-316 | TC-GS-NLU-E2E-091 | FE+BE |
| TC-GS-NLU-317 | TC-GS-NLU-E2E-091 | FE+BE |
| TC-GS-NLU-318 | TC-GS-NLU-E2E-091 | FE+BE |
| TC-GS-NLU-319 | TC-GS-NLU-E2E-091 | FE+BE |
| TC-GS-NLU-320 | TC-GS-NLU-E2E-092 | FE+BE |
| TC-GS-NLU-321 | TC-GS-NLU-E2E-135 | FE+BE |
| TC-GS-NLU-322 | TC-GS-NLU-E2E-135 | FE+BE |
| TC-GS-NLU-323 | TC-GS-NLU-E2E-093 | FE+BE |
| TC-GS-NLU-324 | TC-GS-NLU-E2E-093 | FE+BE |
| TC-GS-NLU-325 | TC-GS-NLU-E2E-093 | FE+BE |
| TC-GS-NLU-326 | TC-GS-NLU-E2E-093 | FE+BE |
| TC-GS-NLU-327 | TC-GS-NLU-E2E-094 | FE+BE |
| TC-GS-NLU-328 | TC-GS-NLU-E2E-094 | FE+BE |
| TC-GS-NLU-329 | TC-GS-NLU-E2E-094 | FE+BE |
| TC-GS-NLU-330 | TC-GS-NLU-E2E-094 | FE+BE |
| TC-GS-NLU-331 | TC-GS-NLU-E2E-092 | FE+BE |
| TC-GS-NLU-332 | TC-GS-NLU-E2E-092 | FE+BE |
| TC-GS-NLU-333 | TC-GS-NLU-E2E-095 | FE+BE |
| TC-GS-NLU-334 | TC-GS-NLU-E2E-095 | FE+BE |
| TC-GS-NLU-335 | TC-GS-NLU-E2E-095 | FE+BE |
| TC-GS-NLU-336 | TC-GS-NLU-E2E-095 | FE+BE |
| TC-GS-NLU-337 | TC-GS-NLU-E2E-095 | FE+BE |
| TC-GS-NLU-338 | TC-GS-NLU-E2E-096 | FE+BE |
| TC-GS-NLU-339 | TC-GS-NLU-E2E-096 | FE+BE |
| TC-GS-NLU-340 | TC-GS-NLU-E2E-136 | FE+BE |
| TC-GS-NLU-341 | TC-GS-NLU-E2E-136 | FE+BE |
| TC-GS-NLU-342 | TC-GS-NLU-E2E-136 | FE+BE |
| TC-GS-NLU-343 | TC-GS-NLU-E2E-097 | FE+BE |
| TC-GS-NLU-344 | TC-GS-NLU-E2E-097 | FE+BE |
| TC-GS-NLU-345 | TC-GS-NLU-E2E-097 | FE+BE |
| TC-GS-NLU-346 | TC-GS-NLU-E2E-097 | FE+BE |
| TC-GS-NLU-347 | TC-GS-NLU-E2E-098 | FE+BE |
| TC-GS-NLU-348 | TC-GS-NLU-E2E-098 | FE+BE |
| TC-GS-NLU-349 | TC-GS-NLU-E2E-098 | FE+BE |
| TC-GS-NLU-350 | TC-GS-NLU-E2E-098 | FE+BE |
| TC-GS-NLU-351 | TC-GS-NLU-E2E-096 | FE+BE |
| TC-GS-NLU-352 | TC-GS-NLU-E2E-096 | FE+BE |
| TC-GS-NLU-353 | TC-GS-NLU-E2E-099 | FE+BE |
| TC-GS-NLU-354 | TC-GS-NLU-E2E-099 | FE+BE |
| TC-GS-NLU-355 | TC-GS-NLU-E2E-099 | FE+BE |
| TC-GS-NLU-356 | TC-GS-NLU-E2E-099 | FE+BE |
| TC-GS-NLU-357 | TC-GS-NLU-E2E-100 | FE+BE |
| TC-GS-NLU-358 | TC-GS-NLU-E2E-100 | FE+BE |
| TC-GS-NLU-359 | TC-GS-NLU-E2E-100 | FE+BE |
| TC-GS-NLU-360 | TC-GS-NLU-E2E-100 | FE+BE |
| TC-GS-NLU-361 | TC-GS-NLU-E2E-101 | FE+BE |
| TC-GS-NLU-362 | TC-GS-NLU-E2E-101 | FE+BE |
| TC-GS-NLU-363 | TC-GS-NLU-E2E-101 | FE+BE |
| TC-GS-NLU-364 | TC-GS-NLU-E2E-102 | FE+BE |
| TC-GS-NLU-365 | TC-GS-NLU-E2E-102 | FE+BE |
| TC-GS-NLU-366 | TC-GS-NLU-E2E-102 | FE+BE |
| TC-GS-NLU-367 | TC-GS-NLU-E2E-102 | FE+BE |
| TC-GS-NLU-368 | TC-GS-NLU-E2E-103 | FE+BE |
| TC-GS-NLU-369 | TC-GS-NLU-E2E-103 | FE+BE |
| TC-GS-NLU-370 | TC-GS-NLU-E2E-103 | FE+BE |
| TC-GS-NLU-371 | TC-GS-NLU-E2E-103 | FE+BE |
| TC-GS-NLU-372 | TC-GS-NLU-E2E-101 | FE+BE |
| TC-GS-NLU-373 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-374 | TC-GS-NLU-E2E-101 | FE+BE |
| TC-GS-NLU-375 | TC-GS-NLU-E2E-099 | FE+BE |
| TC-GS-NLU-376 | TC-GS-NLU-E2E-122 | FE+BE |
| TC-GS-NLU-377 | TC-GS-NLU-E2E-104 | FE+BE |
| TC-GS-NLU-378 | TC-GS-NLU-E2E-104 | FE+BE |
| TC-GS-NLU-379 | TC-GS-NLU-E2E-104 | FE+BE |
| TC-GS-NLU-380 | TC-GS-NLU-E2E-104 | FE+BE |
| TC-GS-NLU-381 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-382 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-383 | TC-GS-NLU-E2E-106 | FE+BE |
| TC-GS-NLU-384 | TC-GS-NLU-E2E-106 | FE+BE |
| TC-GS-NLU-385 | TC-GS-NLU-E2E-106 | FE+BE |
| TC-GS-NLU-386 | TC-GS-NLU-E2E-106 | FE+BE |
| TC-GS-NLU-387 | TC-GS-NLU-E2E-107 | FE+BE |
| TC-GS-NLU-388 | TC-GS-NLU-E2E-107 | FE+BE |
| TC-GS-NLU-389 | TC-GS-NLU-E2E-107 | FE+BE |
| TC-GS-NLU-390 | TC-GS-NLU-E2E-107 | FE+BE |
| TC-GS-NLU-391 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-392 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-393 | TC-GS-NLU-E2E-105 | FE+BE |
| TC-GS-NLU-394 | TC-GS-NLU-E2E-108 | FE+BE |
| TC-GS-NLU-395 | TC-GS-NLU-E2E-108 | FE+BE |
| TC-GS-NLU-396 | TC-GS-NLU-E2E-108 | FE+BE |
| TC-GS-NLU-397 | TC-GS-NLU-E2E-108 | FE+BE |
| TC-GS-NLU-398 | TC-GS-NLU-E2E-109 | FE+BE |
| TC-GS-NLU-399 | TC-GS-NLU-E2E-109 | FE+BE |
| TC-GS-NLU-400 | TC-GS-NLU-E2E-109 | FE+BE |
| TC-GS-NLU-401 | TC-GS-NLU-E2E-109 | FE+BE |
| TC-GS-NLU-402 | TC-GS-NLU-E2E-110 | FE+BE |
| TC-GS-NLU-403 | TC-GS-NLU-E2E-110 | FE+BE |
| TC-GS-NLU-404 | TC-GS-NLU-E2E-110 | FE+BE |
| TC-GS-NLU-405 | TC-GS-NLU-E2E-110 | FE+BE |
| TC-GS-NLU-406 | TC-GS-NLU-E2E-111 | FE+BE |
| TC-GS-NLU-407 | TC-GS-NLU-E2E-111 | FE+BE |
| TC-GS-NLU-408 | TC-GS-NLU-E2E-111 | FE+BE |
| TC-GS-NLU-409 | TC-GS-NLU-E2E-073 | FE+BE |
| TC-GS-NLU-410 | TC-GS-NLU-E2E-073 | FE+BE |
| TC-GS-NLU-411 | TC-GS-NLU-E2E-113 | FE+BE |
| TC-GS-NLU-412 | TC-GS-NLU-E2E-113 | FE+BE |
| TC-GS-NLU-413 | TC-GS-NLU-E2E-113 | FE+BE |
| TC-GS-NLU-414 | TC-GS-NLU-E2E-087 | FE+BE |
| TC-GS-NLU-415 | TC-GS-NLU-E2E-114 | FE+BE |
| TC-GS-NLU-416 | TC-GS-NLU-E2E-114 | FE+BE |
| TC-GS-NLU-417 | TC-GS-NLU-E2E-114 | FE+BE |
| TC-GS-NLU-418 | TC-GS-NLU-E2E-137 | FE+BE |
| TC-GS-NLU-419 | TC-GS-NLU-E2E-137 | FE+BE |
| TC-GS-NLU-420 | TC-GS-NLU-E2E-115 | FE+BE |
| TC-GS-NLU-421 | TC-GS-NLU-E2E-115 | FE+BE |
| TC-GS-NLU-422 | TC-GS-NLU-E2E-115 | FE+BE |
| TC-GS-NLU-423 | TC-GS-NLU-E2E-115 | FE+BE |
| TC-GS-NLU-424 | TC-GS-NLU-E2E-116 | FE+BE |
| TC-GS-NLU-425 | TC-GS-NLU-E2E-112 | FE+BE |
| TC-GS-NLU-426 | TC-GS-NLU-E2E-116 | FE+BE |
| TC-GS-NLU-427 | TC-GS-NLU-E2E-116 | FE+BE |
| TC-GS-NLU-428 | TC-GS-NLU-E2E-116 | FE+BE |
| TC-GS-NLU-429 | TC-GS-NLU-E2E-116 | FE+BE |
| TC-GS-NLU-430 | TC-GS-NLU-E2E-027 | FE+BE |
| TC-GS-NLU-431 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-432 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-433 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-434 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-435 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-436 | TC-GS-NLU-E2E-117 | FE+BE |
| TC-GS-NLU-437 | TC-GS-NLU-E2E-118 | FE+BE |
| TC-GS-NLU-438 | TC-GS-NLU-E2E-119 | FE+BE |
| TC-GS-NLU-439 | TC-GS-NLU-E2E-119 | FE+BE |
| TC-GS-NLU-440 | TC-GS-NLU-E2E-121 | FE+BE |
| TC-GS-NLU-441 | TC-GS-NLU-E2E-121 | FE+BE |
| TC-GS-NLU-442 | TC-GS-NLU-E2E-068 | FE+BE |
| TC-GS-NLU-443 | TC-GS-NLU-E2E-072 | FE+BE |
| TC-GS-NLU-444 | TC-GS-NLU-E2E-066 | FE+BE |
| TC-GS-NLU-445 | TC-GS-NLU-E2E-118 | FE+BE |
| TC-GS-NLU-446 | TC-GS-NLU-E2E-054 | FE+BE |
| TC-GS-NLU-447 | TC-GS-NLU-E2E-054 | FE+BE |
| TC-GS-NLU-448 | TC-GS-NLU-E2E-062 | FE+BE |
| TC-GS-NLU-449 | TC-GS-NLU-E2E-058 | FE+BE |
| TC-GS-NLU-450 | TC-GS-NLU-E2E-131 | FE+BE |
| TC-GS-NLU-451 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-452 | TC-GS-NLU-E2E-118 | FE+BE |
| TC-GS-NLU-453 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-454 | TC-GS-NLU-E2E-120 | FE+BE |
| TC-GS-NLU-455 | TC-GS-NLU-E2E-118 | FE+BE |
| TC-GS-NLU-456 | TC-GS-NLU-E2E-018 | FE+BE |
| TC-GS-NLU-457 | TC-GS-NLU-E2E-018 | FE+BE |
| TC-GS-NLU-458 | TC-GS-NLU-E2E-053 | FE+BE |
| TC-GS-NLU-459 | TC-GS-NLU-E2E-069 | FE+BE |
| TC-GS-NLU-460 | TC-GS-NLU-E2E-023 | FE+BE |
| TC-GS-NLU-461 | TC-GS-NLU-E2E-020 | FE+BE |
| TC-GS-NLU-462 | TC-GS-NLU-E2E-027 | FE+BE |
| TC-GS-NLU-463 | TC-GS-NLU-E2E-072 | FE+BE |
| TC-GS-NLU-464 | TC-GS-NLU-E2E-120 | FE+BE |
| TC-GS-NLU-465 | TC-GS-NLU-E2E-077 | FE+BE |
| TC-GS-NLU-466 | TC-GS-NLU-E2E-053 | FE+BE |
| TC-GS-NLU-467 | TC-GS-NLU-E2E-060 | FE+BE |
| TC-GS-NLU-468 | TC-GS-NLU-E2E-079 | FE+BE |
| TC-GS-NLU-469 | TC-GS-NLU-E2E-112 | FE+BE |
| TC-GS-NLU-470 | TC-GS-NLU-E2E-064 | FE+BE |
| TC-GS-NLU-471 | TC-GS-NLU-E2E-019 | FE+BE |
| TC-GS-NLU-472 | TC-GS-NLU-E2E-046 | FE+BE |
| TC-GS-NLU-473 | TC-GS-NLU-E2E-066 | FE+BE |
| TC-GS-NLU-474 | TC-GS-NLU-E2E-064 | FE+BE |
| TC-GS-NLU-475 | TC-GS-NLU-E2E-064 | FE+BE |
| TC-GS-NLU-476 | TC-GS-NLU-E2E-063 | FE+BE |
| TC-GS-NLU-477 | TC-GS-NLU-E2E-122 | FE+BE |
| TC-GS-NLU-478 | TC-GS-NLU-E2E-121 | FE+BE |
| TC-GS-NLU-479 | TC-GS-NLU-E2E-058 | FE+BE |
| TC-GS-NLU-480 | TC-GS-NLU-E2E-137 | FE+BE |
| TC-GS-NLU-481 | TC-GS-NLU-E2E-047 | FE+BE |
| TC-GS-NLU-482 | TC-GS-NLU-E2E-075 | FE+BE |
| TC-GS-NLU-483 | TC-GS-NLU-E2E-088 | FE+BE |
| TC-GS-NLU-484 | TC-GS-NLU-E2E-083 | FE+BE |
| TC-GS-NLU-485 | TC-GS-NLU-E2E-083 | FE+BE |
| TC-GS-NLU-486 | TC-GS-NLU-E2E-083 | FE+BE |
| TC-GS-NLU-489 | TC-GS-NLU-E2E-083 | FE+BE |
| TC-GS-NLU-490 | TC-GS-NLU-E2E-081 | FE+BE |
| TC-GS-NLU-491 | TC-GS-NLU-E2E-081 | FE+BE |
| TC-GS-NLU-492 | TC-GS-NLU-E2E-005 | FE+BE |
| TC-GS-NLU-493 | TC-GS-NLU-E2E-081 | FE+BE |
| TC-GS-NLU-494 | TC-GS-NLU-E2E-134 | FE+BE |
| TC-GS-NLU-495 | TC-GS-NLU-E2E-047 | FE+BE |
| TC-GS-NLU-496 | TC-GS-NLU-E2E-035 | FE+BE |
| TC-GS-NLU-497 | TC-GS-NLU-E2E-119 | FE+BE |
| TC-GS-NLU-498 | TC-GS-NLU-E2E-138 | FE+BE |
| TC-GS-NLU-500 | TC-GS-NLU-E2E-081 | FE+BE |
| TC-GS-NLU-501 | TC-GS-NLU-E2E-067 | FE+BE |
| TC-GS-NLU-502 | TC-GS-NLU-E2E-024 | FE+BE |
| TC-GS-NLU-503 | TC-GS-NLU-E2E-024 | FE+BE |
| TC-GS-NLU-504 | TC-GS-NLU-E2E-024 | FE+BE |
| TC-GS-NLU-505 | TC-GS-NLU-E2E-053 | FE+BE |
| TC-GS-NLU-506 | TC-GS-NLU-E2E-111 | FE+BE |
| TC-GS-NLU-507 | TC-GS-NLU-E2E-111 | FE+BE |
| TC-GS-NLU-508 | TC-GS-NLU-E2E-030 | FE+BE |
| TC-GS-NLU-509 | TC-GS-NLU-E2E-030 | FE+BE |
| TC-GS-NLU-510 | TC-GS-NLU-E2E-032 | FE+BE |
| TC-GS-NLU-511 | TC-GS-NLU-E2E-032 | FE+BE |
| TC-GS-NLU-512 | TC-GS-NLU-E2E-031 | FE+BE |
| TC-GS-NLU-513 | TC-GS-NLU-E2E-031 | FE+BE |
| TC-GS-NLU-514 | TC-GS-NLU-E2E-031 | FE+BE |
| TC-GS-NLU-515 | TC-GS-NLU-E2E-032 | FE+BE |
| TC-GS-NLU-516 | TC-GS-NLU-E2E-032 | FE+BE |
| TC-GS-NLU-517 | TC-GS-NLU-E2E-032 | FE+BE |
