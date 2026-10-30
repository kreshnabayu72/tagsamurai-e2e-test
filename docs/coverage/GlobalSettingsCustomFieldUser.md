# Coverage E2E — Global Settings > User > Custom Field

Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md` (565 TC `TC-GS-UCF-1`–`565`, tanpa celah dan tanpa TC retired). TC BE `tc-custom-field-user-backend.md` (`TC-GS-UCF-BE-NNN`) hanya dipakai untuk mengenali TC hanya-BE. Suite: `specs/GlobalSettings/CustomFieldUser/`. Prefix: `GS` + `UCF` (`TC-GS-UCF-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 565 TC masuk 76 spec (71 FE+BE web, 1 FE+BE mobile, 4 mock), 0 TC hanya-BE (kolom FE Test seluruh TC bernilai `UI Only` 131 atau `Need API` 434; tidak ada `-`). Setiap TC terpetakan ke tepat satu spec di `sourceTc` (lihat Pemeriksaan cakupan). 48 TC berlabel `Manual Only` tetap ditulis sebagai spec (kebutuhan dua sesi atau dialog `beforeunload` ada di `## Prerequisites` tiap spec).

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default | Screening Tab Custom Field: Layout 3 Zona, Tooltip Ikon, Nama Aksesibel, dan Urutan Default Field Name A-Z | FE+BE | 58 | 2, 5, 6, 396 |
| TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | Tampilan Sel Tabel Custom Field: Value Setting, Placeholder Efektif, Modified By, Active, Required, Data Type, dan Batas Teks Panjang | FE+BE | 88 | 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 326, 371, 440, 441, 503, 511, 512 |
| TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | Navigasi Tab Custom Field: Breadcrumb Mengikuti Tab, F5, Back dan Forward, Retensi State Pindah Tab, dan Reset lewat Klik Ulang Sidebar | FE+BE | 50 | 3, 4, 398, 399, 400 |
| TC-GS-UCF-E2E-004-empty-state-entitas-tanpa-custom-field | Empty State Entitas Tanpa Custom Field: Illustration, CTA Tidak Ada, dan Filter dengan No options available | FE+BE | 28 | 9, 543 |
| TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | Guided Tooltip Tab Custom Field: Konten 3 Step, Navigasi Keyboard, Fokus Tooltip Box, Aktor Read Only, dan Resize atau Navigasi Keluar | FE+BE | 64 | 22, 26, 27, 28, 29, 403 |
| TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | Guided Tooltip Tab Custom Field: Muncul Otomatis pada Kunjungan Pertama, Skip, Klik Overlay, Done, dan Esc Menandai Seen, serta Replay lewat Tombol [?] | FE+BE | 48 | 23, 24, 25, 401, 402 |
| TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Custom Field per Role | FE+BE | 188 | 30, 31, 32, 33, 34, 35, 36, 39, 391, 392, 513, 514 |
| TC-GS-UCF-E2E-008-role-matrix-negatif-akses-langsung-url-dan-tanpa-menu | Role Matrix Negatif: Aktor Tanpa Capability Tidak Melihat Menu User dan Akses Langsung URL Tab Custom Field Ditolak | FE+BE | 10 | 37, 38 |
| TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Eksekusi Create, Edit, Activate, Deactivate, dan Delete oleh Aktor dengan Capability Spesifik dan Default User | FE+BE | 121 | 40, 41, 42, 43, 393, 394, 395, 484, 485 |
| TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | Multi-Konteks: Capability Create, Update, atau Delete Dicabut Saat Popup atau Dialog Terbuka, Aksi Ditolak dan UI Memuat Ulang Kontrol | FE+BE | 105 | 328, 340, 342, 344, 349, 548, 551 |
| TC-GS-UCF-E2E-011-resilience-baca-loading-error-dan-try-again | Resilience Baca Tabel Custom Field: Loading State, Loading saat Search atau Pagination, dan Error Load dengan Try Again | mock | 33 | 7, 8, 11 |
| TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | Defense-in-Depth Otorisasi Server: Request Langsung Tanpa Capability Ditolak 403 dan id Custom Field Milik Entitas Lain Diperlakukan Tidak Ditemukan | FE+BE | 106 | 304, 305, 306, 557, 558, 559, 563 |
| TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | Defense-in-Depth Input: Emoji Lolos Filter FE Ditolak Server, Markup Ditampilkan sebagai Teks, dan Dropdown Tanpa Value Ditolak Server | FE+BE | 100 | 308, 309, 310, 467, 468, 469 |
| TC-GS-UCF-E2E-014-isolasi-entitas | Isolasi Entitas: Custom Field dan Changelog Client A Tidak Terlihat di Client B, dan Field Name yang Sama dengan Client A Diterima di Client B | FE+BE | 25 | 307, 421 |
| TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | Popup Create Custom Field: Screening, Aksesibilitas, Info Popover, dan Perilaku Data Type | FE+BE | 79 | 44, 45, 46, 47, 48, 49, 50, 51, 404 |
| TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | Create Custom Field: Validasi Field Name, Trim, Keunikan, Karakter Khusus, dan Data Type Wajib | FE+BE | 124 | 52, 53, 54, 55, 56, 57, 58, 59, 60, 442, 443, 541, 542 |
| TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | Create Custom Field: Validasi Placeholder, Placeholder Default, dan Value Dropdown | FE+BE | 133 | 61, 62, 63, 64, 65, 66, 67, 68, 444, 445, 446, 447, 448, 449 |
| TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | Create Custom Field Berhasil: Population, Per Data Type, Required, Stay on Form, Clear Field, dan Modified By | FE+BE | 131 | 1, 69, 70, 71, 72, 73, 74, 75, 450, 451 |
| TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | Popup Create Custom Field: Penutupan Form, Dialog Unsaved Changes, Backdrop, Navigasi, dan Konfirmasi Browser | FE+BE | 76 | 76, 77, 78, 79, 80, 81, 82, 327, 405, 452 |
| TC-GS-UCF-E2E-020-create-saving-state-guard-double-submit-dan-nama-dipakai-ulang | Create Custom Field: Saving State, Guard Klik Ganda Submit, dan Field Name Dipakai Ulang Setelah Dihapus | FE+BE | 35 | 83, 84, 455 |
| TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | Form User: Tampilan Custom Field (Placeholder, Tanda Required, Opsi Dropdown, Date Picker) dan Required Tidak Retroaktif | FE+BE | 48 | 173, 174, 186, 187, 188, 189 |
| TC-GS-UCF-E2E-022-form-user-validasi-text-dan-text-area | Form User: Validasi Batas Karakter Nilai Custom Field Text (120) dan Text Area (360) | FE+BE | 22 | 175, 176 |
| TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | Form User: Validasi Custom Field Required Kosong Ditolak untuk Dropdown, Text, Text Area, Date, dan Numeric | FE+BE | 33 | 185, 498, 499, 500, 544 |
| TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | Form User: Input Numeric (Karakter Diizinkan, Batas 15 Digit, Decimal Places) dan Simpan 15 Digit | FE+BE | 73 | 177, 178, 179, 350, 389, 476, 545, 546 |
| TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | Form User: Normalisasi Nilai Numeric yang Tersimpan (Nol di Depan, Titik, Negatif Nol, Nol di Belakang) | FE+BE | 8 | 378, 382, 383, 384, 385, 386, 387, 495, 496 |
| TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | Form User: Field Phone (Country Code Default, Validasi Number 4 sampai 15 Digit, Required, dan Penyimpanan Kode Negara) | FE+BE | 84 | 180, 181, 182, 183, 184, 369, 390, 492, 493, 494, 497 |
| TC-GS-UCF-E2E-027-master-data-count-limit-create | Master Data Count Limit: [+ Custom Field] Diblokir saat Limit Tercapai, Create di Batas, Edit di Batas, Slot Dibebaskan Delete, Limit Dibaca Dinamis, dan Limit Diturunkan di Bawah Jumlah Field | FE+BE | 93 | 87, 88, 90, 302, 364, 435, 453, 464 |
| TC-GS-UCF-E2E-028-master-data-count-limit-1000-field-termasuk-inactive | Master Data Count Limit: 1.000 Field Memuat Field Inactive Tetap Menampilkan Dialog Limit Reached | FE+BE | 6 | 454 |
| TC-GS-UCF-E2E-029-multi-konteks-create-bersamaan | Multi-Konteks: Create Bersamaan Field Name Sama oleh Dua Admin dan Dua Admin Berebut Slot Terakhir Master Data Count Limit | FE+BE | 22 | 89, 323 |
| TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | Resilience Tulis: Create dan Edit saat Kegagalan Server 5xx dan Timeout, Retry setelah Kegagalan | mock | 72 | 85, 86, 131, 132, 339 |
| TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | Edit Custom Field: Screening Popup Edit, Aksesibilitas, dan Validasi Field Name (Kosong, Hanya Spasi, Batas Panjang, Trim, Duplikat, Karakter Non-Latin, Data Type Kosong) | FE+BE | 114 | 91, 92, 93, 94, 95, 96, 331, 406, 456, 457, 465, 466 |
| TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | Edit Custom Field: Validasi Placeholder dan Value Dropdown (Batas Panjang, Trim, Hanya Spasi, Emoji, Duplikat, Pemulihan setelah Error Dropdown Kosong) | FE+BE | 99 | 97, 332, 333, 334, 335, 458, 470, 471, 472 |
| TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | Edit Custom Field: Save Tanpa Perubahan (No-Op), Kapitalisasi, Sukses Tidak Menyentuh Nilai User, Saving State, Klik Ganda Save, Field Inactive, dan Modified By Admin Lain | FE+BE | 106 | 99, 126, 127, 128, 129, 130, 133, 374, 459, 463 |
| TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | Edit Custom Field: Penutupan Popup Edit, Dialog Unsaved Changes, Clear Field, Backdrop, Esc, Navigasi Internal, dan Konfirmasi beforeunload | FE+BE | 86 | 98, 121, 122, 123, 124, 125, 329, 330, 407, 462 |
| TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | Edit Custom Field Numeric: Decimal Places Bebas pada Field Belum Bernilai, Terkunci Setelah Ada Nilai User, Clear Field, dan Pemulihan Decimal Places Tersimpan | FE+BE | 64 | 100, 101, 109, 367, 461 |
| TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | Edit Custom Field: Ganti Data Type, Dialog Change Data Type, Pengosongan Nilai User, Pemulihan Data Type Tersimpan, Validasi Inline Sebelum Dialog, dan Backdrop Dialog | FE+BE | 182 | 103, 104, 105, 106, 107, 108, 110, 372, 373, 408, 460, 473, 474, 475 |
| TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | Edit Custom Field Dropdown: Tambah, Rename, dan Hapus Value, Dialog Remove Value, Cascade ke Nilai User, Tukar Label, dan Minimal Satu Value | FE+BE | 206 | 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 336, 337, 366, 370, 376, 377 |
| TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | Multi-Konteks: Edit Bersamaan Last-Write-Wins, Form Edit Stale (Decimal Places, Data Type, Value Dropdown), Field Dihapus atau Dinonaktifkan Admin Lain di Tengah Edit | FE+BE | 127 | 102, 316, 317, 321, 368, 375, 381, 388, 540 |
| TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | Delete Custom Field Tunggal: Dialog, Accessibility, Cancel, Sukses dengan Efek ke User dan Log, Klik Ganda, dan Field Inactive | FE+BE | 60 | 134, 135, 136, 137, 139, 409 |
| TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Efek ke Form User, dan Klik Ganda | FE+BE | 57 | 156, 157, 158, 159, 160, 163, 345 |
| TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | Bulk Activate dan Bulk Deactivate: Komposisi Seleksi, Dialog, Cancel, Efek ke User, dan Klik Ganda | FE+BE | 129 | 164, 165, 166, 167, 168, 343, 346, 347, 481, 482, 483 |
| TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | Bulk Action Bar: Screening Bar, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi | FE+BE | 68 | 140, 141, 142, 143, 144, 515 |
| TC-GS-UCF-E2E-043-selection-limit-bulk | Selection Limit Bulk: Seleksi Manual ke-101 Diblok dan Select All Di-cap ke 100 dengan Toast Error Persist | FE+BE | 17 | 145, 146 |
| TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | Bulk Delete: Dialog Container Scrollable, Collapse ke Dialog Single, Cancel, Klik Ganda, dan Penghapusan Homogen | FE+BE | 50 | 147, 148, 149, 150, 155 |
| TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | Dialog Konfirmasi Aksi: Esc, Klik Backdrop, dan Perilaku Toast (Posisi, Auto-dismiss, Error Persist, Penggantian) | FE+BE | 99 | 410, 411, 488, 489, 490, 491 |
| TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | Mobile Android: Selection Mode Long-press, Keluar dari Mode Multi-select, Select All, dan Bulk Delete Custom Field | FE+BE (mobile) | 41 | 325, 436, 437, 438, 439 |
| TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | Multi-Konteks Delete: Record Sudah Dihapus atau Dinonaktifkan Admin Lain di Antara Dialog dan Konfirmasi (Single dan Bulk) | FE+BE | 60 | 151, 152, 153, 318, 322 |
| TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | Multi-Konteks Toggle Active: Record Sudah Dihapus atau Sudah Berubah Status oleh Admin Lain (Single dan Bulk) | FE+BE | 114 | 169, 170, 171, 319, 320, 477, 478, 479, 480 |
| TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | Resilience Tulis Aksi: Delete, Bulk Delete, Toggle Active, dan Bulk Toggle saat Kegagalan Server 5xx atau Timeout | mock | 120 | 138, 154, 161, 162, 172, 341, 348, 486, 487, 547, 549, 550 |
| TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | State Tenant: Client Suspended dan Expired Menolak Create, Edit, Delete, Toggle, dan Bulk Action Custom Field, Baca Tetap Tersedia | FE+BE | 146 | 312, 313, 314, 315, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434 |
| TC-GS-UCF-E2E-051-search-tabel-utama | Search Tabel Utama Custom Field: Siklus Interaksi, Scope Kolom, Substring, Trim, Hasil Kosong, Visibilitas Kolom, dan Karakter Literal | FE+BE | 95 | 10, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 311, 379, 510 |
| TC-GS-UCF-E2E-052-filter-panel-tabel-utama | Filter Panel Tabel Utama Custom Field: Screening, Logika OR dan AND, Chip, Opsi Dinamis, Draft, Clear Field, dan Retensi F5 | FE+BE | 182 | 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 221, 351, 352, 353, 354, 397 |
| TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | Kombinasi Search, Filter, Sort, dan Pagination Tabel Custom Field: Irisan, Clear, Empty State, Reset Halaman, dan Perubahan Data | FE+BE | 144 | 214, 215, 216, 217, 218, 219, 220, 231, 504, 505, 506, 507 |
| TC-GS-UCF-E2E-054-sort-tabel-utama | Sort Tabel Utama Custom Field: Siklus Tiga Klik per Kolom, Value Setting Teks Lengkap, Modified By Nama Lengkap, dan Kolom Tanpa Ikon Sort | FE+BE | 98 | 222, 223, 224, 225, 226, 227, 228, 229, 501, 502 |
| TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama | Pagination dan Ukuran Halaman Tabel Custom Field: Next/Prev, Opsi Page Size, Nomor Halaman Tidak Valid, Retensi F5, dan Hapus Baris Terakhir | FE+BE | 50 | 230, 232, 233, 234 |
| TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | Overlay Column Visibility dan Modal Setup Column Tabel Custom Field: Screening, Hide, Reorder, Pin, Reset, Penutupan, dan Independensi dari Modal Changelog | FE+BE | 111 | 235, 236, 237, 238, 239, 240, 241, 242, 243, 508, 509 |
| TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | Download CSV dan XLSX Tabel Custom Field: Overlay, Isi Berkas, Mengikuti Search dan Filter, Kolom Tersembunyi, Urutan Sort, Hasil Kosong, dan Encoding BOM | FE+BE | 70 | 244, 245, 246, 247, 248, 249, 250, 252 |
| TC-GS-UCF-E2E-058-download-di-atas-5000-baris-loading-screen | Download di Atas 5.000 Baris Tabel Custom Field: Loading Screen sampai Berkas Siap lalu Langsung Terunduh | FE+BE | 12 | 365 |
| TC-GS-UCF-E2E-059-multi-konteks-list-tidak-otomatis-dan-filter-basi | Multi-Konteks Tabel Custom Field: Kriteria Filter Basi karena Record Dihapus Sesi Lain dan List Tidak Diperbarui Otomatis | FE+BE | 22 | 355, 556 |
| TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog | Resilience Download: Toast Error saat Unduh Tabel Utama dan Modal Changelog Gagal karena 5xx atau Timeout | mock | 32 | 251, 273, 552, 553 |
| TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | Modal Changelog Custom Field: Screening, Tooltip, Hover Modified By, Klik Backdrop dan Esc, Error Load, Loading State, dan Empty State | FE+BE | 60 | 253, 254, 255, 257, 269, 526, 527 |
| TC-GS-UCF-E2E-062-changelog-search | Modal Changelog Custom Field: Search, Siklus Search Toolbar, Kolom Teks, Date Tidak Dicari, Kolom Hidden Dikecualikan, dan Empty State | FE+BE | 55 | 256, 258, 259, 260, 516, 517 |
| TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | Modal Changelog Custom Field: Screening Filter Panel, Opsi Dropdown, Chip, Filter Date Action Field Modified By, Logika AND, dan Empty State | FE+BE | 115 | 261, 262, 263, 264, 265, 266, 356, 361, 412, 518, 519, 520, 521, 522 |
| TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | Modal Changelog Custom Field: Pagination, Sort Semua Kolom, dan Entri Hasil Bulk Tanpa Duplikat Antar Halaman | FE+BE | 79 | 267, 268, 523, 524, 525 |
| TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | Modal Changelog Custom Field: Setup Column (Overlay, Hide dan Unhide, Reorder, Pin, Tutup Tanpa Simpan, Kolom Terakhir, Persistensi, dan Isolasi dari Tabel Utama) | FE+BE | 100 | 270, 271, 357, 358, 359, 360, 528, 529 |
| TC-GS-UCF-E2E-066-download-changelog-csv-xlsx | Download Changelog Custom Field CSV dan XLSX: Mengikuti Search dan Filter, Isi Sel, Seluruh Entri Lintas Halaman, dan Kolom Hidden | FE+BE | 42 | 272, 530, 531, 532 |
| TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | Pencatatan Create dan Edit Custom Field (Field Name, Data Type, Value Setting, Placeholder, Required, Decimal Places, Dua Properti, Rename Bersama Properti Lain) pada Changelog, System Log, dan Activity Log | FE+BE | 209 | 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 338, 380 |
| TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control | Pencatatan Activate, Deactivate, Delete, Bulk Activate Deactivate Delete per Field yang Diproses, dan Log Aksi Aktor Non-Total Control pada Changelog, System Log, dan Activity Log | FE+BE | 101 | 285, 286, 287, 290 |
| TC-GS-UCF-E2E-069-pencatatan-snapshot-nama-lama-dan-aktor-dihapus | Pencatatan Snapshot: Entri Log Lama Tidak Berubah Setelah Rename Kedua, Name System Log Tidak Berubah, dan Modified By Tetap Menampilkan Aktor yang Sudah Dihapus | FE+BE | 56 | 289, 554, 555 |
| TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati | Tidak Ada Pencatatan Log untuk Edit No-Op, Kapitalisasi dan Spasi Tepi, Aksi Gagal atau Dibatalkan, dan Item yang Dilewati pada Bulk Delete | FE+BE | 132 | 284, 288, 291, 533 |
| TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | Format Tanggal dan Waktu General Settings pada Last Updated, Filter, Modal Changelog, Time Zone, dan Berkas Download CSV | FE+BE | 58 | 292, 293, 413, 414, 415, 416 |
| TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | Sinkronisasi Custom Field ke Form Create User, Create Non-Login User, Detail User, dan My Profile: Field Baru, Rename, Placeholder, Required, Activate dan Deactivate, serta Form yang Sedang Terbuka | FE+BE | 91 | 294, 295, 296, 301, 362, 363, 534, 535, 537 |
| TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | Sinkronisasi Custom Field ke Kolom Curated Fixed Asset Settings User, Admin Console Settings User, dan Popup Total User Detail Admin Console Settings Group | FE+BE | 61 | 297, 298, 299, 538, 539 |
| TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | Import User Login: Kolom Custom Field di Staging Table, Kolom Tak Dikenal, Create Missing Options (Log Tiga Surface, Urutan Value, Nama Sudah Ditambahkan Admin Lain, Field Dinonaktifkan Admin Lain, Pemegang Import data Create) | FE+BE | 131 | 300, 536, 560, 561, 562, 564, 565 |
| TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | Create, Edit, dan Delete Custom Field Berperilaku Identik pada Plan Starter, Growth, Professional, dan Enterprise Tanpa Gating | FE+BE | 107 | 303, 417, 418, 419, 420 |
| TC-GS-UCF-E2E-076-multi-tab-create-bersamaan | Multi-Tab: Submit Ganda Create Field Name Sama melalui Dua Tab pada Satu Sesi Tidak Menduplikasi Definisi | FE+BE | 11 | 324 |

## Pemeriksaan cakupan

- Jumlah entri `sourceTc` seluruh spec: 565; ID unik: 565; ID yang hilang dari rentang 1–565: 0; ID yang muncul lebih dari sekali: 0. Hasil: 565/565, tepat satu spec per TC.
- Kecocokan terhadap berkas TC mentah diperiksa oleh `scripts/check-suite.py` (C1 sampai C3).
- TC hanya-BE: 0. Injeksi request (TC-GS-UCF-304 sampai 306, 310, 557 sampai 559) dan TC-GS-UCF-308, 309, 467 sampai 469 tetap spec kelas defense-in-depth lewat console atau intercept.
- Mode: FE+BE web 71 spec, FE+BE mobile 1 spec (046), mock 4 spec (011, 030, 049, 060).
- Panjang spec: 61 dari 76 spec melebihi ±35 langkah; alasan pertahanan ada di `## Notes` tiap spec. Terpanjang: 067 (209), 037 (206), 007 (188), 036 (182), 052 (182), 050 (146), 053 (144), 017 (133), 070 (132), 018 dan 074 (masing-masing 131).

## TC hanya-BE (tidak masuk spec)

Tidak ada. Seluruh 565 TC punya permukaan FE (kolom FE Test bukan `-`).

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec dan sudah terdaftar di `spectra.config.ts`: `GS_TC_PASSWORD`, `GS_TC2_PASSWORD`, `GS_RO_PASSWORD`, `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_DEFAULT_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`, `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`.
- Env var yang dipakai spec tetapi belum terdaftar di `spectra.config.ts` (nama usulan penulis spec; tim FE mendaftarkannya di `spectra.config.ts` dan `.env.example` serta mengisi email akun yang belum tertulis di Pre-setup TC): `GS_FVC_TC_PASSWORD` (spec 005); `GS_FVA_TC_PASSWORD` (spec 006); `GS_FVB_TC_PASSWORD` (spec 006); `GS_FVD_TC_PASSWORD` (spec 006); `GS_FVE_TC_PASSWORD` (spec 006); `GS_CANDRA_TC_PASSWORD` (spec 069); `GS_RAHMAT_PASSWORD` (spec 072); `GS_IMPORTCREATE_PASSWORD` (spec 012 dan 074); `GS_MONO_TC_PASSWORD` dan `GS_LONGNAME_TC_PASSWORD` (spec 018; akun Mono dan LongName untuk TC-GS-UCF-450 dan 451). Spec 070, 072, dan 074 memakai `GS_TC2_PASSWORD`, dan spec 073 memakai `GS_PRINCIPAL_TC_PASSWORD`; keduanya sudah terdaftar.
- Fixture baru (`preset14` dan `population` ditandai "fixture baru (belum ada)" di Prerequisites spec yang memakainya; `multiTab076` milik spec 076): berkas `fixtures/custom-field-user.json` (belum ada) dengan 47 kunci `Fixture.customFieldUser.*` yang dirujuk spec: `authz012`, `bulkDelete044`, `bulkToggle041`, `combinedSeed053`, `concurrent038`, `consumer073`, `createRace029`, `defense013`, `deleteSingle039`, `dialogToast045`, `display002`, `edit031`, `edit032`, `edit033`, `edit034`, `edit035`, `edit036`, `edit037`, `filterSeed052`, `import074`, `importUnknownCsv074`, `limit027`, `logAbsence070`, `logAction068`, `logCreateEdit067`, `logSnapshot069`, `mobileSelection046`, `mockList011`, `multiContext059`, `multiDelete047`, `multiTab076`, `multiToggle048`, `paginationSeed055`, `plan075`, `population`, `preset14`, `resilienceAction049`, `resilienceDownload060`, `resilienceWrite030`, `revoke010`, `roleExec009`, `searchSeed051`, `sortSeed054`, `sync072`, `tieLog064`, `toggleSingle040`, `volume365`.
- Entitas dan state yang disediakan tim FE/BE (mekanisme tidak ada di TC, PRD, atau LLD; tidak dikarang): Client tanpa Custom Field (TC-GS-UCF-9, 543; spec 004), Client B dan Client C, Client Suspended dan Expired (spec 050), entitas per plan Starter/Growth/Professional/Enterprise (spec 075), Client dengan kuota 999/1.000/5.001 Custom Field (spec 027, 028, 058), akun First Visit A sampai E (spec 005, 006), reset dan penyetelan flag Guided Tooltip, pencabutan capability role (spec 010), seeding 14 field Population dan data per spec, staging Import (spec 074).
- Tambahan dari audit E2E (hook suite, mekanisme disediakan tim FE/BE, tidak dikarang): (1) D-158 (hook `before` suite): menonaktifkan atau menghapus lewat API setiap Custom Field Required Yes Active Client A selain Cost Center, Office Phone, dan Tax ID, mencatat status awal, dan memulihkannya di hook `after` (jaminan untuk spec 021 sampai 025, 026, 041, 042, 044); (2) penghapusan lewat API field sisa Client A (bersuffix `{runId}` dan field non-Pre-setup/non-Population yang tidak dimiliki spec mana pun) di hook `before` suite; (3) Detail User untuk spec mock 030 dan 049; (4) spec 060: list Changelog `POST /v2/activity-logs/changelogs/list`, export Changelog, dan SSE tidak ada di API modul, disediakan tim FE; SSE tidak dikirim modul ini (PRD:934); (5) akun `Rina Marlina` (`GS_IMPORTCREATE_PASSWORD`) untuk empat request 403 TC-GS-UCF-563 di spec 012.
- Hook suite dan flag Guided Tooltip: lihat `suite.md`.

## Spec yang butuh kemampuan harness khusus

| Kemampuan | Spec |
|---|---|
| Intercept jaringan (5xx, timeout, tahan respons) | 011, 030, 049, 060 (mock); penahanan respons 3 detik di 020 dan 033 |
| Dua sesi browser (Admin A dan Admin B) atau sesi API pemicu | 010, 029, 038, 047, 048, 059 |
| Dua tab browser pada satu sesi (penanda `[Tab 1]` dan `[Tab 2]`) | 076 |
| Pencabutan dan pemulihan capability role | 010 |
| Dialog `beforeunload` native dan penutupan tab | 019, 034 (TC-82, 405, 330, 407); bila framework tidak menanganinya: `coverage.web: unsupported` per konvensi bagian 2 |
| Klien HTTP / console untuk request langsung | 012, 013 |
| Pembaca berkas CSV/XLSX, termasuk >5.000 baris | 057, 058, 066 |
| Emulator atau perangkat Android | 046 (`coverage.mobile`) |
| Volume data dan kuota (999/1.000/5.001 field), Master Data Count Limit, Selection Limit di Admin Console | 027, 028, 029, 043, 058 |
| State tenant (Client Suspended, Expired, plan) | 050, 075 |
| Pengubah Date Format dan Time Zone General Settings, jam server | 071 |
| Mekanisme Import (Import Type User) | 074 |
| Seeding lewat API dan penyetelan flag Guided Tooltip | seluruh suite (hook `before`) |

## Temuan untuk QA / FE (rangkuman)

Penulis spec mencatat 420 butir di `Temuan untuk QA` pada 75 spec (rincian per spec ada di `## Notes` masing-masing; tidak disalin ke sini). Pengelompokan berbasis kata kunci sehingga jumlahnya perkiraan; satu butir dihitung pada satu tema.

| Tema | Butir (±) | Tindakan yang dibutuhkan |
|---|--:|---|
| Langkah atau Expected TC tidak menyebut halaman, state popup/dialog sesudah aksi, jumlah klik, titik klik, ukuran viewport, atau cara pengamatan; spec mengambil asumsi yang dicatat | 84 | QA: lengkapi Langkah/Expected TC |
| Post Condition tanpa langkah observasi (tidak diasersi) | 47 | QA: tambah langkah observasi atau hapus Post Condition |
| Mekanisme tidak didefinisikan di TC/PRD/LLD (seeding, state tenant, sesi kedua, flag, Import, pembacaan URL, path endpoint) | 41 | FE/BE: sediakan mekanisme; QA: dokumentasikan di TC |
| Konflik data Pre-setup/Population dan nama tanpa suffix (Pre-setup TC memuat 6 field, Population TC-GS-UCF-1 menambah 8 menjadi 14) | 40 | QA: selaraskan Pre-setup dengan Population |
| Divergensi PRD/TC dengan LLD/API (NC-01 sampai NC-27; terbanyak NC-10 pluralisasi Decimal Places, NC-06 cakupan kolom Search) | 34 | Pemilik LLD: selaraskan; asersi bisa gagal pada backend nyata |
| Nilai ditandai `PRD?` atau tidak konsisten antar bagian TC (mis. id 9999... vs 1000..., TC-307 vs TC-421, 14 baris vs paginasi 10) | 26 | QA/PRD: tetapkan nilai |
| Expected tanpa langkah observasi atau tidak merinci elemen | 19 | QA: tambah langkah |
| Env var, akun, dan email tidak ada atau berbeda dari `.env.example` | 14 | FE: daftarkan env var, isi email |
| Lainnya (teks UI yang diserahkan ke dokumen lain, label tombol tidak disebut, dsb.) | 115 | QA: tinjau per spec |

Tema resilience: `Mode: mock` (keputusan user) pada spec 011, 030, 049, 060; asersi yang menyangkut state backend nyata (mis. TC-GS-UCF-132, 138, 154) tidak teruji pada mode itu dan dicatat di Temuan untuk QA spec terkait.

## Keputusan yang sudah diambil

- Plan disetujui user (2026-10-29): 6 slice, 75 spec, 565 TC. Setelah audit E2E (2026-10-29) suite menjadi 76 spec: TC-GS-UCF-324 dipisah ke spec 076 (`TC-GS-UCF-E2E-076-multi-tab-create-bersamaan`); TC-GS-UCF-464 pindah dari 033 ke 027 dan TC-GS-UCF-563 pindah dari 074 ke 012; jumlah TC tetap 565.
- Mode resilience (spec 011, 030, 049, 060): `Mode: mock`, seperti Position.
- Keputusan NC yang berbeda dari API/LLD (NC-06, 08 sampai 13, 15 sampai 22): spec ditulis sesuai TC dan tiap divergensi dicatat di Temuan untuk QA; tidak ada spec ditahan.
- TC-GS-UCF-1 (Population): dibangun lewat UI di spec 018; spec lain memakai seed API idempotent di hook `before`.
- Volume 999/1.000/5.001 field: disediakan tim BE.
- K-9 B: Pre-setup Client B berisi 10 field; `Client B Eleven` bukan Pre-setup, berstatus Dinamis dan dimiliki spec 055 (seeding idempotent, dihapus sendiri); spec 052 memakai 10 field Pre-setup Client B.
- K-10 A: Filter Panel tetap terbuka sesudah `[Apply]`; spec 063 diselaraskan (langkah `Klik Filter` sesudah Apply dihapus bila panel sudah terbuka). Spec 052 sudah memakai model ini.
- K-6 B: spec `Mode: mock` hanya mengasersi perilaku FE atas respons mock. Pemecahan TC resilience yang menyangkut state backend nyata (TC-GS-UCF-132, 138, 154, 172, 348, 486, 487, 547, 549, 550) ke TC FE+BE terpisah belum dikerjakan; asersi tersebut tetap ada di spec 030 dan 049 dan dicatat di Temuan untuk QA.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-UCF-1 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-2 | TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default | FE+BE |
| TC-GS-UCF-3 | TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | FE+BE |
| TC-GS-UCF-4 | TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | FE+BE |
| TC-GS-UCF-5 | TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default | FE+BE |
| TC-GS-UCF-6 | TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default | FE+BE |
| TC-GS-UCF-7 | TC-GS-UCF-E2E-011-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-UCF-8 | TC-GS-UCF-E2E-011-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-UCF-9 | TC-GS-UCF-E2E-004-empty-state-entitas-tanpa-custom-field | FE+BE |
| TC-GS-UCF-10 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-11 | TC-GS-UCF-E2E-011-resilience-baca-loading-error-dan-try-again | mock |
| TC-GS-UCF-12 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-13 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-14 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-15 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-16 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-17 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-18 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-19 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-20 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-21 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-22 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-23 | TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UCF-24 | TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UCF-25 | TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UCF-26 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-27 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-28 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-29 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-30 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-31 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-32 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-33 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-34 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-35 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-36 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-37 | TC-GS-UCF-E2E-008-role-matrix-negatif-akses-langsung-url-dan-tanpa-menu | FE+BE |
| TC-GS-UCF-38 | TC-GS-UCF-E2E-008-role-matrix-negatif-akses-langsung-url-dan-tanpa-menu | FE+BE |
| TC-GS-UCF-39 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-40 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-41 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-42 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-43 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-44 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-45 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-46 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-47 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-48 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-49 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-50 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-51 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-52 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-53 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-54 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-55 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-56 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-57 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-58 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-59 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-60 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-61 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-62 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-63 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-64 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-65 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-66 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-67 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-68 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-69 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-70 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-71 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-72 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-73 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-74 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-75 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-76 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-77 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-78 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-79 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-80 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-81 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-82 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-83 | TC-GS-UCF-E2E-020-create-saving-state-guard-double-submit-dan-nama-dipakai-ulang | FE+BE |
| TC-GS-UCF-84 | TC-GS-UCF-E2E-020-create-saving-state-guard-double-submit-dan-nama-dipakai-ulang | FE+BE |
| TC-GS-UCF-85 | TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | mock |
| TC-GS-UCF-86 | TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | mock |
| TC-GS-UCF-87 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-88 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-89 | TC-GS-UCF-E2E-029-multi-konteks-create-bersamaan | FE+BE |
| TC-GS-UCF-90 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-91 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-92 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-93 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-94 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-95 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-96 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-97 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-98 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-99 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-100 | TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | FE+BE |
| TC-GS-UCF-101 | TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | FE+BE |
| TC-GS-UCF-102 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-103 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-104 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-105 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-106 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-107 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-108 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-109 | TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | FE+BE |
| TC-GS-UCF-110 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-111 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-112 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-113 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-114 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-115 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-116 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-117 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-118 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-119 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-120 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-121 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-122 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-123 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-124 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-125 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-126 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-127 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-128 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-129 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-130 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-131 | TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | mock |
| TC-GS-UCF-132 | TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | mock |
| TC-GS-UCF-133 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-134 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-135 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-136 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-137 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-138 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-139 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-140 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-141 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-142 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-143 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-144 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-145 | TC-GS-UCF-E2E-043-selection-limit-bulk | FE+BE |
| TC-GS-UCF-146 | TC-GS-UCF-E2E-043-selection-limit-bulk | FE+BE |
| TC-GS-UCF-147 | TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | FE+BE |
| TC-GS-UCF-148 | TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | FE+BE |
| TC-GS-UCF-149 | TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | FE+BE |
| TC-GS-UCF-150 | TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | FE+BE |
| TC-GS-UCF-151 | TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | FE+BE |
| TC-GS-UCF-152 | TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | FE+BE |
| TC-GS-UCF-153 | TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | FE+BE |
| TC-GS-UCF-154 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-155 | TC-GS-UCF-E2E-044-bulk-delete-dialog-homogen-dan-double-click | FE+BE |
| TC-GS-UCF-156 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-157 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-158 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-159 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-160 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-161 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-162 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-163 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-164 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-165 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-166 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-167 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-168 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-169 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-170 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-171 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-172 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-173 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-174 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-175 | TC-GS-UCF-E2E-022-form-user-validasi-text-dan-text-area | FE+BE |
| TC-GS-UCF-176 | TC-GS-UCF-E2E-022-form-user-validasi-text-dan-text-area | FE+BE |
| TC-GS-UCF-177 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-178 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-179 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-180 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-181 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-182 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-183 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-184 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-185 | TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | FE+BE |
| TC-GS-UCF-186 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-187 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-188 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-189 | TC-GS-UCF-E2E-021-form-user-tampilan-field-placeholder-required-dropdown-dan-date-picker | FE+BE |
| TC-GS-UCF-190 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-191 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-192 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-193 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-194 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-195 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-196 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-197 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-198 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-199 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-200 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-201 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-202 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-203 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-204 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-205 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-206 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-207 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-208 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-209 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-210 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-211 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-212 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-213 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-214 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-215 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-216 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-217 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-218 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-219 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-220 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-221 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-222 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-223 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-224 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-225 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-226 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-227 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-228 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-229 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-230 | TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-UCF-231 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-232 | TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-UCF-233 | TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-UCF-234 | TC-GS-UCF-E2E-055-pagination-dan-ukuran-halaman-tabel-utama | FE+BE |
| TC-GS-UCF-235 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-236 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-237 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-238 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-239 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-240 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-241 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-242 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-243 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-244 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-245 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-246 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-247 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-248 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-249 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-250 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-251 | TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-UCF-252 | TC-GS-UCF-E2E-057-download-csv-xlsx-tabel-utama | FE+BE |
| TC-GS-UCF-253 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-254 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-255 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-256 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-257 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-258 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-259 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-260 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-261 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-262 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-263 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-264 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-265 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-266 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-267 | TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | FE+BE |
| TC-GS-UCF-268 | TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | FE+BE |
| TC-GS-UCF-269 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-270 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-271 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-272 | TC-GS-UCF-E2E-066-download-changelog-csv-xlsx | FE+BE |
| TC-GS-UCF-273 | TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-UCF-274 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-275 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-276 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-277 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-278 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-279 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-280 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-281 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-282 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-283 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-284 | TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati | FE+BE |
| TC-GS-UCF-285 | TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control | FE+BE |
| TC-GS-UCF-286 | TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control | FE+BE |
| TC-GS-UCF-287 | TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control | FE+BE |
| TC-GS-UCF-288 | TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati | FE+BE |
| TC-GS-UCF-289 | TC-GS-UCF-E2E-069-pencatatan-snapshot-nama-lama-dan-aktor-dihapus | FE+BE |
| TC-GS-UCF-290 | TC-GS-UCF-E2E-068-pencatatan-activate-deactivate-delete-bulk-dan-log-aktor-non-total-control | FE+BE |
| TC-GS-UCF-291 | TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati | FE+BE |
| TC-GS-UCF-292 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-293 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-294 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-295 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-296 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-297 | TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | FE+BE |
| TC-GS-UCF-298 | TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | FE+BE |
| TC-GS-UCF-299 | TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | FE+BE |
| TC-GS-UCF-300 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-301 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-302 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-303 | TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | FE+BE |
| TC-GS-UCF-304 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-305 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-306 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-307 | TC-GS-UCF-E2E-014-isolasi-entitas | FE+BE |
| TC-GS-UCF-308 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-309 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-310 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-311 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-312 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-313 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-314 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-315 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-316 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-317 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-318 | TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | FE+BE |
| TC-GS-UCF-319 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-320 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-321 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-322 | TC-GS-UCF-E2E-047-multi-konteks-delete-record-sudah-berubah | FE+BE |
| TC-GS-UCF-323 | TC-GS-UCF-E2E-029-multi-konteks-create-bersamaan | FE+BE |
| TC-GS-UCF-324 | TC-GS-UCF-E2E-076-multi-tab-create-bersamaan | FE+BE |
| TC-GS-UCF-325 | TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-UCF-326 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-327 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-328 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-329 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-330 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-331 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-332 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-333 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-334 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-335 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-336 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-337 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-338 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-339 | TC-GS-UCF-E2E-030-resilience-tulis-create-dan-edit-5xx-timeout | mock |
| TC-GS-UCF-340 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-341 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-342 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-343 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-344 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-345 | TC-GS-UCF-E2E-040-toggle-active-single-dialog-activate-deactivate | FE+BE |
| TC-GS-UCF-346 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-347 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-348 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-349 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-350 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-351 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-352 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-353 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-354 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-355 | TC-GS-UCF-E2E-059-multi-konteks-list-tidak-otomatis-dan-filter-basi | FE+BE |
| TC-GS-UCF-356 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-357 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-358 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-359 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-360 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-361 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-362 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-363 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-364 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-365 | TC-GS-UCF-E2E-058-download-di-atas-5000-baris-loading-screen | FE+BE |
| TC-GS-UCF-366 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-367 | TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | FE+BE |
| TC-GS-UCF-368 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-369 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-370 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-371 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-372 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-373 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-374 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-375 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-376 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-377 | TC-GS-UCF-E2E-037-edit-value-dropdown-tambah-rename-hapus | FE+BE |
| TC-GS-UCF-378 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-379 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-380 | TC-GS-UCF-E2E-067-pencatatan-create-dan-edit-changelog-activity-log-system-log | FE+BE |
| TC-GS-UCF-381 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-382 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-383 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-384 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-385 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-386 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-387 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-388 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-389 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-390 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-391 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-392 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-393 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-394 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-395 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-396 | TC-GS-UCF-E2E-001-screening-tabel-layout-tooltip-aksesibilitas-dan-urutan-default | FE+BE |
| TC-GS-UCF-397 | TC-GS-UCF-E2E-052-filter-panel-tabel-utama | FE+BE |
| TC-GS-UCF-398 | TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | FE+BE |
| TC-GS-UCF-399 | TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | FE+BE |
| TC-GS-UCF-400 | TC-GS-UCF-E2E-003-navigasi-tab-retensi-state-dan-reset-sidebar | FE+BE |
| TC-GS-UCF-401 | TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UCF-402 | TC-GS-UCF-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-UCF-403 | TC-GS-UCF-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-UCF-404 | TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type | FE+BE |
| TC-GS-UCF-405 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-406 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-407 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-408 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-409 | TC-GS-UCF-E2E-039-delete-single-dialog-cancel-double-click-dan-sukses | FE+BE |
| TC-GS-UCF-410 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-411 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-412 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-413 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-414 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-415 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-416 | TC-GS-UCF-E2E-071-format-tanggal-dan-time-zone-general-settings | FE+BE |
| TC-GS-UCF-417 | TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | FE+BE |
| TC-GS-UCF-418 | TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | FE+BE |
| TC-GS-UCF-419 | TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | FE+BE |
| TC-GS-UCF-420 | TC-GS-UCF-E2E-075-perilaku-identik-lintas-plan | FE+BE |
| TC-GS-UCF-421 | TC-GS-UCF-E2E-014-isolasi-entitas | FE+BE |
| TC-GS-UCF-422 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-423 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-424 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-425 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-426 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-427 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-428 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-429 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-430 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-431 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-432 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-433 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-434 | TC-GS-UCF-E2E-050-state-tenant-write-lockdown-suspended-dan-expired | FE+BE |
| TC-GS-UCF-435 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-436 | TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-UCF-437 | TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-UCF-438 | TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-UCF-439 | TC-GS-UCF-E2E-046-mobile-selection-mode-dan-bulk-delete | FE+BE (mobile) |
| TC-GS-UCF-440 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-441 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-442 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-443 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-444 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-445 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-446 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-447 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-448 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-449 | TC-GS-UCF-E2E-017-create-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-450 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-451 | TC-GS-UCF-E2E-018-create-sukses-per-data-type-required-stay-dan-clear-field | FE+BE |
| TC-GS-UCF-452 | TC-GS-UCF-E2E-019-create-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-453 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-454 | TC-GS-UCF-E2E-028-master-data-count-limit-1000-field-termasuk-inactive | FE+BE |
| TC-GS-UCF-455 | TC-GS-UCF-E2E-020-create-saving-state-guard-double-submit-dan-nama-dipakai-ulang | FE+BE |
| TC-GS-UCF-456 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-457 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-458 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-459 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-460 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-461 | TC-GS-UCF-E2E-035-edit-decimal-places-terkunci | FE+BE |
| TC-GS-UCF-462 | TC-GS-UCF-E2E-034-edit-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-UCF-463 | TC-GS-UCF-E2E-033-edit-sukses-no-op-kapitalisasi-dan-guard-double-save | FE+BE |
| TC-GS-UCF-464 | TC-GS-UCF-E2E-027-master-data-count-limit-create | FE+BE |
| TC-GS-UCF-465 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-466 | TC-GS-UCF-E2E-031-edit-screening-aksesibilitas-dan-validasi-field-name | FE+BE |
| TC-GS-UCF-467 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-468 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-469 | TC-GS-UCF-E2E-013-defense-in-depth-input-emoji-markup-dan-bypass-dropdown | FE+BE |
| TC-GS-UCF-470 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-471 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-472 | TC-GS-UCF-E2E-032-edit-validasi-placeholder-dan-value-dropdown | FE+BE |
| TC-GS-UCF-473 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-474 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-475 | TC-GS-UCF-E2E-036-edit-ganti-data-type-dan-dialog-konfirmasi | FE+BE |
| TC-GS-UCF-476 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-477 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-478 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-479 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-480 | TC-GS-UCF-E2E-048-multi-konteks-toggle-record-sudah-berubah | FE+BE |
| TC-GS-UCF-481 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-482 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-483 | TC-GS-UCF-E2E-041-bulk-activate-deactivate-komposisi-seleksi-dan-dialog | FE+BE |
| TC-GS-UCF-484 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-485 | TC-GS-UCF-E2E-009-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-UCF-486 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-487 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-488 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-489 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-490 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-491 | TC-GS-UCF-E2E-045-dialog-konfirmasi-esc-backdrop-dan-toast-aksi | FE+BE |
| TC-GS-UCF-492 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-493 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-494 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-495 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-496 | TC-GS-UCF-E2E-025-form-user-numeric-normalisasi-nilai-tersimpan | FE+BE |
| TC-GS-UCF-497 | TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number | FE+BE |
| TC-GS-UCF-498 | TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | FE+BE |
| TC-GS-UCF-499 | TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | FE+BE |
| TC-GS-UCF-500 | TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | FE+BE |
| TC-GS-UCF-501 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-502 | TC-GS-UCF-E2E-054-sort-tabel-utama | FE+BE |
| TC-GS-UCF-503 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-504 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-505 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-506 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-507 | TC-GS-UCF-E2E-053-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-UCF-508 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-509 | TC-GS-UCF-E2E-056-column-visibility-dan-setup-column-tabel-utama | FE+BE |
| TC-GS-UCF-510 | TC-GS-UCF-E2E-051-search-tabel-utama | FE+BE |
| TC-GS-UCF-511 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-512 | TC-GS-UCF-E2E-002-tampilan-sel-tabel-value-setting-placeholder-modified-by-dan-badge | FE+BE |
| TC-GS-UCF-513 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-514 | TC-GS-UCF-E2E-007-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-UCF-515 | TC-GS-UCF-E2E-042-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-UCF-516 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-517 | TC-GS-UCF-E2E-062-changelog-search | FE+BE |
| TC-GS-UCF-518 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-519 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-520 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-521 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-522 | TC-GS-UCF-E2E-063-changelog-filter-dropdown-chip-dan-logika | FE+BE |
| TC-GS-UCF-523 | TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | FE+BE |
| TC-GS-UCF-524 | TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | FE+BE |
| TC-GS-UCF-525 | TC-GS-UCF-E2E-064-changelog-sort-dan-pagination | FE+BE |
| TC-GS-UCF-526 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-527 | TC-GS-UCF-E2E-061-changelog-screening-hover-empty-loading-error-dan-tutup | FE+BE |
| TC-GS-UCF-528 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-529 | TC-GS-UCF-E2E-065-changelog-column-visibility-dan-setup-column | FE+BE |
| TC-GS-UCF-530 | TC-GS-UCF-E2E-066-download-changelog-csv-xlsx | FE+BE |
| TC-GS-UCF-531 | TC-GS-UCF-E2E-066-download-changelog-csv-xlsx | FE+BE |
| TC-GS-UCF-532 | TC-GS-UCF-E2E-066-download-changelog-csv-xlsx | FE+BE |
| TC-GS-UCF-533 | TC-GS-UCF-E2E-070-absence-log-no-op-gagal-dan-item-dilewati | FE+BE |
| TC-GS-UCF-534 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-535 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-536 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-537 | TC-GS-UCF-E2E-072-sinkronisasi-ke-form-user-detail-user-dan-my-profile | FE+BE |
| TC-GS-UCF-538 | TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | FE+BE |
| TC-GS-UCF-539 | TC-GS-UCF-E2E-073-sinkronisasi-ke-fixed-asset-dan-admin-console | FE+BE |
| TC-GS-UCF-540 | TC-GS-UCF-E2E-038-multi-konteks-edit-bersamaan-dan-form-stale | FE+BE |
| TC-GS-UCF-541 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-542 | TC-GS-UCF-E2E-016-create-validasi-field-name-dan-trim | FE+BE |
| TC-GS-UCF-543 | TC-GS-UCF-E2E-004-empty-state-entitas-tanpa-custom-field | FE+BE |
| TC-GS-UCF-544 | TC-GS-UCF-E2E-023-form-user-validasi-required-semua-tipe | FE+BE |
| TC-GS-UCF-545 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-546 | TC-GS-UCF-E2E-024-form-user-numeric-input-dan-validasi-digit-desimal | FE+BE |
| TC-GS-UCF-547 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-548 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-549 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-550 | TC-GS-UCF-E2E-049-resilience-tulis-hapus-dan-toggle-5xx-timeout | mock |
| TC-GS-UCF-551 | TC-GS-UCF-E2E-010-multi-konteks-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-UCF-552 | TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-UCF-553 | TC-GS-UCF-E2E-060-resilience-download-tabel-utama-dan-changelog | mock |
| TC-GS-UCF-554 | TC-GS-UCF-E2E-069-pencatatan-snapshot-nama-lama-dan-aktor-dihapus | FE+BE |
| TC-GS-UCF-555 | TC-GS-UCF-E2E-069-pencatatan-snapshot-nama-lama-dan-aktor-dihapus | FE+BE |
| TC-GS-UCF-556 | TC-GS-UCF-E2E-059-multi-konteks-list-tidak-otomatis-dan-filter-basi | FE+BE |
| TC-GS-UCF-557 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-558 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-559 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-560 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-561 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-562 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-563 | TC-GS-UCF-E2E-012-defense-in-depth-otorisasi-server-direct-api | FE+BE |
| TC-GS-UCF-564 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
| TC-GS-UCF-565 | TC-GS-UCF-E2E-074-import-user-value-dropdown-kolom-tak-dikenal-dan-create-missing-options | FE+BE |
