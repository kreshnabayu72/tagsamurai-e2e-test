# Coverage E2E — Admin Console > Hardware > Stock

Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (609 TC, ID `TC-AC-ACHS-1`–`609`, semua aktif). Suite: `specs/AdminConsole/HardwareStock/`. Prefix: `AC` + `ACHS` (`TC-AC-ACHS-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-hardware-stock-backend.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 609 TC aktif masuk 115 spec dan setiap TC terpetakan ke tepat satu spec. Nomor spec sengaja berlubang antar kelompok (mis. 011 ke 020) untuk menyisakan ruang sisipan. Spec yang menulis atau menghapus data memakai nomor 240 sampai 289 (urutan jalan di `suite.md`). Mode FE+BE berarti backend nyata; variasi intercept parsial dan seeding via API dijelaskan di `## Prerequisites` tiap spec.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-ACHS-E2E-001-screening-stock-list-toolbar-overlay-dan-tanpa-allocated | Screening Stock List: Toolbar, Overlay Row Action, dan Tanpa Kolom Allocated atau Checkbox | FE+BE | 47 | 1, 2, 10, 12, 13, 14 |
| TC-AC-ACHS-E2E-003-empty-state-genuinely-kosong-dan-no-results-detail | Empty State Genuinely Kosong dan No Results Stock Detail | FE+BE | 27 | 18, 46, 47, 48, 54 |
| TC-AC-ACHS-E2E-004-loading-state-stock-list-detail-approvals | Loading State Stock List, Stock Detail, dan Approvals | FE+BE | 22 | 19, 50, 590 |
| TC-AC-ACHS-E2E-005-retensi-state-list-detail-approvals-saat-navigasi-f5 | Retensi State List, Stock Detail, dan Approvals saat Navigasi dan Refresh | FE+BE | 65 | 21, 22, 23, 24, 56, 57 |
| TC-AC-ACHS-E2E-006-guided-tooltip-stock-list | Guided Tooltip Stock List: Isi Step, Replay, Skip, Resize, dan Keyboard | FE+BE | 65 | 25, 26, 27, 28, 29 |
| TC-AC-ACHS-E2E-007-screening-stock-detail-tab-available-semua-tipe-sku | Screening Stock Detail Tab Available untuk Semua Tipe SKU | FE+BE | 70 | 30, 31, 32, 33, 34, 35, 36 |
| TC-AC-ACHS-E2E-008-banner-waiting-for-approval-stock-detail | Banner Waiting for Approval Stock Detail: Teks, Link, dan Scope per Aktor | FE+BE | 36 | 37, 38, 39, 40, 41 |
| TC-AC-ACHS-E2E-010-screening-approvals-tab-active-history-dan-isi-sel | Screening Approvals Hardware Stock Tab Active dan Tab History, Isi Sel, dan Hover Nama Lengkap | FE+BE | 43 | 51, 52, 53, 593 |
| TC-AC-ACHS-E2E-020-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Stock List, Stock Detail, dan Approvals per Role | FE+BE | 157 | 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 197 |
| TC-AC-ACHS-E2E-021-role-matrix-negatif-sidebar-dan-direct-url | Role Matrix Negatif: Menu Sidebar Hidden dan Direct URL Ditolak | FE+BE | 24 | 58, 59, 60, 61, 62, 63, 75, 201 |
| TC-AC-ACHS-E2E-022-scope-stock-list-detail-download-per-aktor-distributor-principal | Scope Stock List, Stock Detail, dan Download per Aktor Distributor dan Principal | FE+BE | 28 | 15, 16, 17, 74, 565, 566 |
| TC-AC-ACHS-E2E-084-dialog-detail-history-badge-approval-dan-visibilitas-subject | Dialog Detail History, Badge Approval, dan Visibilitas Subject | FE+BE | 44 | 196, 198, 202, 203 |
| TC-AC-ACHS-E2E-092-hardware-log-screening-urutan-read-only-dan-scope | Hardware Log: Screening, Urutan, Read-Only, dan Scope | FE+BE | 57 | 526, 527, 528, 529, 530, 531, 552, 589 |
| TC-AC-ACHS-E2E-103-download-sukses-semua-surface-tanpa-toast | Download Sukses Semua Surface Tanpa Toast | FE+BE | 5 | 581 |
| TC-AC-ACHS-E2E-104-resilience-baca-error-load-try-again | Resilience Baca: Error Load dan Try Again | FE+BE | 35 | 20, 49, 55, 522, 588 |
| TC-AC-ACHS-E2E-105-resilience-download-gagal-semua-surface | Resilience Download: Gagal pada Semua Surface | FE+BE | 6 | 254, 313, 365, 413, 463, 511, 580 |
| TC-AC-ACHS-E2E-120-search-stock-list | Search Stock List: Siklus Kotak, Kolom Teks, Badge, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi | FE+BE | 59 | 204, 205, 206, 207, 208, 209, 210, 211 |
| TC-AC-ACHS-E2E-121-filter-stock-list-screening-opsi-dan-apply-per-field | Filter Stock List: Screening Panel, Isi Opsi, Apply per Field, Opsi Tanpa Nilai Kosong, dan State Loading Opsi | FE+BE | 49 | 212, 213, 214, 215, 216, 259, 606 |
| TC-AC-ACHS-E2E-123-sort-stock-list | Sort Stock List: Siklus 3-State Semua Kolom, Urutan Default, Nilai Kosong, Tie-Break, Kolom Non-Sortable, dan Search Tidak Direset | FE+BE | 53 | 227, 228, 229, 230, 231, 232, 233, 257, 258 |
| TC-AC-ACHS-E2E-124-column-visibility-dan-setup-column-stock-list-data-photo | Column Visibility dan Setup Column Stock List: Screening Overlay dan Popup, Kelas Data dan Photo (Uncheck, Drag, Pin) | FE+BE | 86 | 234, 235, 236, 237, 238, 239, 240, 241 |
| TC-AC-ACHS-E2E-125-setup-column-stock-list-guard-reset-tutup-dan-cache-independen | Setup Column Stock List: Batas Pin, Reset to Default, Tutup Popup, Kolom Terakhir, dan Cache Independen antar Tabel | FE+BE | 53 | 242, 243, 244, 245, 601 |
| TC-AC-ACHS-E2E-126-pagination-dan-kombinasi-stock-list | Pagination Stock List: Default, Navigasi, Input Halaman, Reset ke Halaman 1, Batas 25 Baris, dan Kombinasi Empat Kontrol | FE+BE | 49 | 246, 247, 248, 249, 250, 260 |
| TC-AC-ACHS-E2E-127-download-stock-list-nama-berkas-cakupan-dan-kolom-hidden | Download Stock List: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong | FE+BE | 36 | 251, 252, 253, 256 |
| TC-AC-ACHS-E2E-130-search-stock-detail-tab-available | Search Stock Detail Tab Available: Siklus Kotak, Kolom Teks, Badge, Pengguna, dan Angka, Empty State, Kolom Non-Searchable, Visibilitas Kolom, dan Spasi Tepi | FE+BE | 56 | 262, 263, 264, 265, 266, 267, 268, 269, 270 |
| TC-AC-ACHS-E2E-131-filter-tab-available-screening-opsi-dan-apply-per-field | Filter Stock Detail Tab Available: Screening Panel, Isi Opsi, dan Apply per Field | FE+BE | 27 | 271, 272, 273, 274 |
| TC-AC-ACHS-E2E-133-sort-tab-available | Sort Stock Detail Tab Available: Siklus 3-State Semua Kolom, Urutan Default, Kolom Non-Sortable, dan Search Tidak Direset | FE+BE | 26 | 285, 286, 287, 288, 289, 290, 291, 292 |
| TC-AC-ACHS-E2E-134-column-visibility-dan-setup-column-tab-available-data-power | Column Visibility dan Setup Column Stock Detail Tab Available: Screening Overlay dan Popup, Kelas Data dan Power (Uncheck, Drag, Pin) | FE+BE | 86 | 293, 294, 295, 296, 297, 298, 299, 300 |
| TC-AC-ACHS-E2E-135-setup-column-tab-available-guard-reset-dan-tutup | Setup Column Stock Detail Tab Available: Batas Pin, Reset to Default, Tutup Popup, dan Kolom Terakhir | FE+BE | 39 | 301, 302, 303, 304 |
| TC-AC-ACHS-E2E-137-download-tab-available-nama-berkas-cakupan-dan-kolom-hidden | Download Stock Detail Tab Available: Nama Berkas, Cakupan Search dan Seluruh Halaman, Kolom Hidden, dan Hasil Kosong | FE+BE | 38 | 310, 311, 312, 315 |
| TC-AC-ACHS-E2E-138-download-tab-available-isi-berkas-csv-xlsx | Download Stock Detail Tab Available: Isi Berkas XLSX (Transformasi Sel per Tipe Kolom) | FE+BE | 10 | 314 |
| TC-AC-ACHS-E2E-160-search-stock-detail-tab-in-use | Search Stock Detail Tab In Use | FE+BE | 61 | 318, 319, 320, 321, 322, 323, 324, 325, 326 |
| TC-AC-ACHS-E2E-161-filter-tab-in-use-screening-opsi-dan-apply-per-field | Filter Tab In Use Screening Opsi dan Apply per Field | FE+BE | 34 | 327, 328, 329, 330 |
| TC-AC-ACHS-E2E-162-filter-tab-in-use-kombinasi-chip-and-or-dan-indikator | Filter Tab In Use Kombinasi Chip AND OR dan Indikator | FE+BE | 75 | 331, 332, 333, 334, 335, 336, 337, 338, 339, 340 |
| TC-AC-ACHS-E2E-163-sort-tab-in-use | Sort Tab In Use | FE+BE | 30 | 341, 342, 343, 344, 345, 346, 347, 348 |
| TC-AC-ACHS-E2E-164-column-visibility-dan-setup-column-tab-in-use-data-power | Column Visibility dan Setup Column Tab In Use Kelas Data dan Power | FE+BE | 82 | 349, 350, 351, 352, 353, 354, 355, 356 |
| TC-AC-ACHS-E2E-165-setup-column-tab-in-use-guard-reset-dan-tutup | Setup Column Tab In Use Guard Reset dan Tutup | FE+BE | 39 | 357, 358, 359, 360 |
| TC-AC-ACHS-E2E-166-pagination-dan-kombinasi-tab-in-use | Pagination dan Kombinasi Empat Kontrol Tab In Use | FE+BE | 31 | 361, 368 |
| TC-AC-ACHS-E2E-167-download-tab-in-use-nama-berkas-cakupan-dan-kolom-hidden | Download Tab In Use Nama Berkas Cakupan dan Kolom Hidden | FE+BE | 43 | 362, 363, 364, 367 |
| TC-AC-ACHS-E2E-168-download-tab-in-use-isi-berkas-csv-xlsx | Download Tab In Use Isi Berkas XLSX Transformasi Sel | FE+BE | 8 | 366 |
| TC-AC-ACHS-E2E-180-search-approvals-tab-active | Search Approvals Tab Active | FE+BE | 61 | 369, 370, 371, 372, 373, 374, 375 |
| TC-AC-ACHS-E2E-181-filter-approvals-tab-active-screening-opsi-dan-apply-per-field | Filter Approvals Tab Active Screening Opsi dan Apply per Field | FE+BE | 34 | 376, 377, 378, 379 |
| TC-AC-ACHS-E2E-182-filter-approvals-tab-active-kombinasi-chip-and-or-dan-indikator | Filter Approvals Tab Active Kombinasi Chip AND OR dan Indikator | FE+BE | 75 | 380, 381, 382, 383, 384, 385, 386, 387, 388, 389 |
| TC-AC-ACHS-E2E-184-column-visibility-dan-setup-column-approvals-tab-active | Column Visibility dan Setup Column Approvals Tab Active | FE+BE | 50 | 396, 397, 398, 399, 400 |
| TC-AC-ACHS-E2E-185-setup-column-approvals-tab-active-guard-reset-tutup-dan-cache-independen | Setup Column Approvals Tab Active Guard Reset Tutup dan Cache Independen | FE+BE | 54 | 401, 402, 403, 404, 602 |
| TC-AC-ACHS-E2E-186-pagination-dan-kombinasi-approvals-tab-active | Pagination dan Kombinasi Empat Kontrol Approvals Tab Active | FE+BE | 44 | 405, 406, 407, 408, 409 |
| TC-AC-ACHS-E2E-187-download-approvals-tab-active-nama-berkas-cakupan-dan-kolom-hidden | Download Approvals Tab Active Nama Berkas Cakupan dan Kolom Hidden | FE+BE | 43 | 410, 411, 412, 415 |
| TC-AC-ACHS-E2E-188-download-approvals-tab-active-isi-berkas-csv-xlsx | Download Approvals Tab Active Isi Berkas XLSX Transformasi Sel | FE+BE | 7 | 414 |
| TC-AC-ACHS-E2E-200-search-approvals-tab-history | Search Approvals > Hardware Stock Tab History | FE+BE | 70 | 417, 418, 419, 420, 421, 422, 423, 424 |
| TC-AC-ACHS-E2E-201-filter-approvals-tab-history-screening-opsi-dan-apply-per-field | Filter Approvals > Hardware Stock Tab History: Screening, Opsi, dan Apply per Field | FE+BE | 43 | 425, 426, 427, 428 |
| TC-AC-ACHS-E2E-202-filter-approvals-tab-history-kombinasi-chip-and-or-dan-indikator | Filter Approvals > Hardware Stock Tab History: Kombinasi Chip, AND/OR, dan Indikator | FE+BE | 75 | 429, 430, 431, 432, 433, 434, 435, 436, 437, 438 |
| TC-AC-ACHS-E2E-203-sort-approvals-tab-history | Sort Approvals > Hardware Stock Tab History | FE+BE | 26 | 439, 440, 441, 442, 443, 444, 445 |
| TC-AC-ACHS-E2E-204-column-visibility-dan-setup-column-approvals-tab-history | Column Visibility dan Setup Column Approvals > Hardware Stock Tab History | FE+BE | 58 | 446, 447, 448, 449, 450 |
| TC-AC-ACHS-E2E-205-setup-column-approvals-tab-history-guard-reset-dan-tutup | Setup Column Approvals > Hardware Stock Tab History: Guard, Reset, dan Tutup Popup | FE+BE | 56 | 451, 452, 453, 454 |
| TC-AC-ACHS-E2E-206-pagination-dan-kombinasi-approvals-tab-history | Pagination dan Kombinasi Empat Kontrol Approvals > Hardware Stock Tab History | FE+BE | 48 | 455, 456, 457, 458, 459 |
| TC-AC-ACHS-E2E-207-download-approvals-tab-history-nama-berkas-cakupan-dan-kolom-hidden | Download Approvals > Hardware Stock Tab History: Nama Berkas, Cakupan, dan Kolom Hidden | FE+BE | 53 | 460, 461, 462, 465 |
| TC-AC-ACHS-E2E-208-download-approvals-tab-history-isi-berkas-csv-xlsx | Download Approvals > Hardware Stock Tab History: Isi Berkas XLSX per Tipe Kolom | FE+BE | 10 | 464 |
| TC-AC-ACHS-E2E-220-search-popup-event-log | Search Popup Event Log | FE+BE | 60 | 466, 467, 468, 469, 470, 471, 472 |
| TC-AC-ACHS-E2E-221-filter-popup-event-log-screening-opsi-dan-apply-per-field | Filter Popup Event Log: Screening, Opsi, dan Apply per Field | FE+BE | 38 | 473, 474, 475, 476 |
| TC-AC-ACHS-E2E-222-filter-popup-event-log-kombinasi-chip-and-or-dan-indikator | Filter Popup Event Log: Kombinasi Chip, AND/OR, dan Indikator | FE+BE | 76 | 477, 478, 479, 480, 481, 482, 483, 484, 485, 486 |
| TC-AC-ACHS-E2E-223-sort-popup-event-log | Sort Popup Event Log | FE+BE | 27 | 487, 488, 489, 490, 491, 492, 493 |
| TC-AC-ACHS-E2E-224-column-visibility-dan-setup-column-popup-event-log | Column Visibility dan Setup Column Popup Event Log | FE+BE | 65 | 494, 495, 496, 497, 498 |
| TC-AC-ACHS-E2E-225-setup-column-popup-event-log-guard-reset-dan-tutup | Setup Column Popup Event Log: Guard, Reset, dan Tutup Popup | FE+BE | 59 | 499, 500, 501, 502 |
| TC-AC-ACHS-E2E-226-pagination-dan-kombinasi-popup-event-log | Pagination dan Kombinasi Empat Kontrol Popup Event Log | FE+BE | 48 | 503, 504, 505, 506, 507 |
| TC-AC-ACHS-E2E-227-download-popup-event-log-nama-berkas-cakupan-dan-kolom-hidden | Download Popup Event Log: Nama Berkas, Cakupan, dan Kolom Hidden | FE+BE | 54 | 508, 509, 510, 513 |
| TC-AC-ACHS-E2E-228-download-popup-event-log-isi-berkas-csv-xlsx | Download Popup Event Log: Isi Berkas XLSX per Tipe Kolom | FE+BE | 11 | 512 |
| TC-AC-ACHS-E2E-240-isi-sel-stock-list-badge-hitungan-link-sku-dan-placeholder-foto | Isi Sel Stock List: Badge, Hitungan, Link SKU, dan Placeholder Foto | FE+BE | 93 | 3, 4, 5, 6, 7, 8, 9, 11, 599, 605, 609 |
| TC-AC-ACHS-E2E-241-screening-stock-detail-tab-in-use | Screening Stock Detail Tab In Use: Layout, Badge Status, Row Action Read-Only, dan Status Null | FE+BE | 32 | 42, 43, 44, 45 |
| TC-AC-ACHS-E2E-242-format-tanggal-waktu-general-settings-di-semua-surface | Format Tanggal dan Waktu General Settings di Semua Surface Hardware Stock | FE+BE | 38 | 567, 568, 569 |
| TC-AC-ACHS-E2E-243-defense-in-depth-request-langsung-dan-markup-serial-number | Defense-in-Depth: Request Langsung Ditolak dan Serial Number Berisi Markup | FE+BE | 83 | 570, 571, 572, 573, 574, 575, 576, 577, 595, 596, 597, 598 |
| TC-AC-ACHS-E2E-244-tidak-ada-plan-gating-add-stock-per-tier | Tidak Ada Plan Gating: Add Stock Identik pada Tiap Tier Plan | FE+BE | 9 | 578 |
| TC-AC-ACHS-E2E-245-state-tenant-suspended-expired-write-lockdown | State Tenant Suspended dan Expired: Write Lockdown Add Stock, Sync, Delete, dan Approvals | FE+BE | 67 | 108, 109, 158, 168, 199, 200 |
| TC-AC-ACHS-E2E-246-screening-add-stock-manual-dan-live-counter | Screening Add Stock Manual dan Live Counter Serial Numbers | FE+BE | 41 | 76, 77, 78, 79, 115 |
| TC-AC-ACHS-E2E-247-validasi-serial-number-add-stock-manual-diblokir | Validasi Serial Number Add Stock Manual Diblokir | FE+BE | 48 | 84, 88, 89, 90, 91, 92, 96 |
| TC-AC-ACHS-E2E-248-batas-register-asset-bulk-limit-add-stock-manual | Batas Register Asset Bulk Limit pada Add Stock Manual | FE+BE | 33 | 85, 86, 87 |
| TC-AC-ACHS-E2E-249-submit-sukses-add-stock-manual | Submit Sukses Add Stock Manual | FE+BE | 85 | 80, 81, 82, 83, 93, 94, 95, 600 |
| TC-AC-ACHS-E2E-250-state-saving-dan-klik-ganda-submit-add-stock-manual | State Saving dan Klik Ganda Submit Add Stock Manual | FE+BE | 21 | 98, 100 |
| TC-AC-ACHS-E2E-251-tutup-form-add-stock-manual-unsaved-changes | Tutup Form Add Stock Manual dan Dialog Unsaved Changes | FE+BE | 58 | 103, 104, 105, 106, 107 |
| TC-AC-ACHS-E2E-252-role-matrix-positif-add-stock-manual | Role Matrix: Add Stock Manual Berhasil per Role | FE+BE | 0 | 110, 111, 112 |
| TC-AC-ACHS-E2E-253-role-matrix-negatif-add-stock-distributor-local-registration | Role Matrix Negatif: Add Stock Distributor Tanpa Local Registration | FE+BE | 29 | 113, 114 |
| TC-AC-ACHS-E2E-254-blokir-kondisi-data-sku-dihapus-add-stock-manual | Blokir Kondisi Data: SKU Dihapus Sebelum Submit Add Stock Manual | FE+BE | 11 | 97 |
| TC-AC-ACHS-E2E-255-screening-add-stock-sync-dan-tanpa-input-manual | Screening Add Stock Sync dan Tanpa Input Manual | FE+BE | 34 | 116, 117, 131, 159 |
| TC-AC-ACHS-E2E-256-driver-dan-pembacaan-perangkat-sync | Driver dan Pembacaan Perangkat pada Add Stock Sync | FE+BE | 45 | 118, 119, 120, 124, 125, 126, 127 |
| TC-AC-ACHS-E2E-257-sync-berhasil-counter-remove-dan-power | Sync Berhasil, Counter, Remove, dan Nilai Power Add Stock Sync | FE+BE | 59 | 121, 122, 123, 128, 129, 160 |
| TC-AC-ACHS-E2E-258-batas-100-synced-units | Batas 100 Synced Units pada Add Stock Sync | FE+BE | 18 | 130 |
| TC-AC-ACHS-E2E-259-badge-sync-waiting-for-approval-dan-dialog-d02 | Badge Sync Waiting for Approval dan Dialog D-02 | FE+BE | 164 | 132, 133, 134, 135, 136, 137, 138, 139, 147, 148, 592 |
| TC-AC-ACHS-E2E-260-requester-tier-register-duplicate-dari-sync | Requester per Tier pada Register Duplicate dari Add Stock Sync | FE+BE | 107 | 140, 141, 143, 144, 145, 146 |
| TC-AC-ACHS-E2E-261-sync-blokir-kondisi-data-serial-aktif-dan-sku-dihapus | Sync Diblokir Kondisi Data: Serial Aktif dan SKU Dihapus | FE+BE | 31 | 142, 152 |
| TC-AC-ACHS-E2E-262-sync-klik-ganda-dan-badge-basi-akibat-sesi-lain | Sync: Klik Ganda Submit dan Badge Basi Akibat Sesi Lain | FE+BE | 37 | 151, 154, 155 |
| TC-AC-ACHS-E2E-263-tutup-form-add-stock-sync-unsaved-changes | Tutup Form Add Stock Sync dan Dialog Unsaved Changes | FE+BE | 20 | 156, 157 |
| TC-AC-ACHS-E2E-264-dialog-dan-sukses-delete-unit | Dialog dan Sukses Delete Unit | FE+BE | 64 | 161, 162, 163, 167, 172, 173, 174 |
| TC-AC-ACHS-E2E-265-role-matrix-positif-delete-unit | Role Matrix Positif: Delete Unit | FE+BE | 26 | 169, 170, 171 |
| TC-AC-ACHS-E2E-266-blokir-kondisi-data-delete-unit-sudah-in-use | Blokir Kondisi Data: Delete Unit yang Sudah In Use | FE+BE | 12 | 165 |
| TC-AC-ACHS-E2E-267-dialog-detail-approval-screening-validasi-cancel-dan-tumpukan-dialog | Dialog Detail Approval: Screening, Validasi, Cancel, dan Tumpukan Dialog | FE+BE | 74 | 175, 176, 177, 178, 179, 189, 582 |
| TC-AC-ACHS-E2E-268-approve-reject-register-duplicate | Approve dan Reject Register Duplicate | FE+BE | 48 | 180, 182, 195 |
| TC-AC-ACHS-E2E-269-approve-reject-activation-collision-state-submitting-dan-klik-ganda | Approve dan Reject Activation Collision, State Submitting, dan Klik Ganda | FE+BE | 47 | 183, 184, 591, 604 |
| TC-AC-ACHS-E2E-270-blokir-kondisi-data-approve-konflik-keunikan-aktif | Blokir Kondisi Data: Approve Ditolak karena Konflik Keunikan Aktif | FE+BE | 11 | 181 |
| TC-AC-ACHS-E2E-271-multi-konteks-race-keputusan-approval | Multi-Konteks: Race Keputusan Approval | FE+BE | 29 | 190, 191, 192, 193, 194 |
| TC-AC-ACHS-E2E-272-multi-konteks-race-add-stock-dan-delete | Multi-Konteks: Race Add Stock dan Delete | FE+BE | 39 | 99, 153, 166, 585 |
| TC-AC-ACHS-E2E-273-resilience-tulis-add-stock-delete-approve-reject | Resilience Tulis: Add Stock, Delete, Approve, dan Reject | FE+BE | 58 | 101, 102, 149, 150, 164, 185, 186, 187, 188 |
| TC-AC-ACHS-E2E-274-event-log-screening-isi-detail-snapshot-dan-scope | Event Log: Screening, Isi, Detail, Snapshot, dan Scope | FE+BE | 83 | 514, 515, 516, 517, 518, 520, 521, 523, 524, 525, 586, 587 |
| TC-AC-ACHS-E2E-275-activity-log-add-stock-dan-delete | Activity Log: Pencatatan Add Stock dan Delete | FE+BE | 27 | 532, 533, 534, 544 |
| TC-AC-ACHS-E2E-276-activity-log-approval-waiting-approved-rejected-activation | Activity Log: Waiting for Approval, Approved, Rejected, dan Aktivasi | FE+BE | 34 | 535, 536, 537, 538, 539, 540, 541 |
| TC-AC-ACHS-E2E-277-system-log-changelog-tidak-ada-dan-snapshot-immutability | System Log, Changelog Tidak Ada, dan Snapshot Immutability | FE+BE | 46 | 542, 543, 545, 564 |
| TC-AC-ACHS-E2E-278-hardware-log-event-registered-waiting-approved | Hardware Log: Event Registered, Waiting for Approval, dan Approved | FE+BE | 29 | 546, 547, 548, 549, 550 |
| TC-AC-ACHS-E2E-279-lintas-modul-status-unit-aktivasi-pelepasan-global-settings | Lintas Modul: Status Unit, Aktivasi, dan Pelepasan dari Global Settings | FE+BE | 48 | 555, 556, 557, 558, 559 |
| TC-AC-ACHS-E2E-280-sse-real-time-banner-unit-pindah-tab-dan-opsi-filter | SSE Real-Time: Banner, Unit Pindah Tab, dan Opsi Filter | FE+BE | 37 | 553, 554, 603 |
| TC-AC-ACHS-E2E-281-absence-pencatatan-event-log-hardware-log | Absence Pencatatan Event Log dan Hardware Log | FE+BE | 69 | 519, 551, 558, 594, 595, 596 |
| TC-AC-ACHS-E2E-282-activation-collision-lintas-modul-deteksi-cancel | Activation Collision Lintas Modul: Deteksi dan Cancel Request | FE+BE | 35 | 560, 561, 562 |
| TC-AC-ACHS-E2E-283-lintas-modul-device-allocation-dan-asersi-negatif | Lintas Modul: Device Allocation dan Asersi Negatif | FE+BE | 32 | 563, 583, 584 |
| TC-AC-ACHS-E2E-284-download-volume-5000-dan-5001-baris | Download Volume: 5.000 dan 5.001 Baris | FE+BE | 12 | 579 |
| TC-AC-ACHS-E2E-285-filter-stock-list-kombinasi-chip-and-or-dan-indikator | Filter Stock List: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, Overflow Chip, dan Opsi Sumber Hilang | FE+BE | 92 | 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 607, 608 |
| TC-AC-ACHS-E2E-286-download-stock-list-isi-berkas-csv-xlsx | Download Stock List: Isi Berkas CSV dan XLSX (Transformasi Sel per Tipe Kolom dan Aturan Teknis Berkas) | FE+BE | 22 | 255, 261 |
| TC-AC-ACHS-E2E-287-filter-tab-available-kombinasi-chip-and-or-dan-indikator | Filter Stock Detail Tab Available: Kombinasi Chip, OR dan AND, Search, Draft, Indikator, Kolom Tersembunyi, dan Opsi Waiting for Approval | FE+BE | 85 | 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 316 |
| TC-AC-ACHS-E2E-288-pagination-kombinasi-dan-hapus-baris-terakhir-tab-available | Pagination Stock Detail Tab Available: Default, Navigasi, Input Halaman, Kombinasi Empat Kontrol, dan Hapus Baris Terakhir di Halaman Terakhir | FE+BE | 50 | 305, 306, 307, 308, 309, 317 |
| TC-AC-ACHS-E2E-289-sort-approvals-tab-active-dan-urutan-fifo | Sort Approvals Tab Active dan Urutan FIFO | FE+BE | 44 | 390, 391, 392, 393, 394, 395, 416 |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-ACHS-1 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-2 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-3 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-4 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-5 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-6 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-7 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-8 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-9 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-10 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-11 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-12 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-13 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-14 | TC-AC-ACHS-E2E-001 | FE+BE |
| TC-AC-ACHS-15 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-16 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-17 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-18 | TC-AC-ACHS-E2E-003 | FE+BE |
| TC-AC-ACHS-19 | TC-AC-ACHS-E2E-004 | FE+BE |
| TC-AC-ACHS-20 | TC-AC-ACHS-E2E-104 | FE+BE |
| TC-AC-ACHS-21 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-22 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-23 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-24 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-25 | TC-AC-ACHS-E2E-006 | FE+BE |
| TC-AC-ACHS-26 | TC-AC-ACHS-E2E-006 | FE+BE |
| TC-AC-ACHS-27 | TC-AC-ACHS-E2E-006 | FE+BE |
| TC-AC-ACHS-28 | TC-AC-ACHS-E2E-006 | FE+BE |
| TC-AC-ACHS-29 | TC-AC-ACHS-E2E-006 | FE+BE |
| TC-AC-ACHS-30 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-31 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-32 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-33 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-34 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-35 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-36 | TC-AC-ACHS-E2E-007 | FE+BE |
| TC-AC-ACHS-37 | TC-AC-ACHS-E2E-008 | FE+BE |
| TC-AC-ACHS-38 | TC-AC-ACHS-E2E-008 | FE+BE |
| TC-AC-ACHS-39 | TC-AC-ACHS-E2E-008 | FE+BE |
| TC-AC-ACHS-40 | TC-AC-ACHS-E2E-008 | FE+BE |
| TC-AC-ACHS-41 | TC-AC-ACHS-E2E-008 | FE+BE |
| TC-AC-ACHS-42 | TC-AC-ACHS-E2E-241 | FE+BE |
| TC-AC-ACHS-43 | TC-AC-ACHS-E2E-241 | FE+BE |
| TC-AC-ACHS-44 | TC-AC-ACHS-E2E-241 | FE+BE |
| TC-AC-ACHS-45 | TC-AC-ACHS-E2E-241 | FE+BE |
| TC-AC-ACHS-46 | TC-AC-ACHS-E2E-003 | FE+BE |
| TC-AC-ACHS-47 | TC-AC-ACHS-E2E-003 | FE+BE |
| TC-AC-ACHS-48 | TC-AC-ACHS-E2E-003 | FE+BE |
| TC-AC-ACHS-49 | TC-AC-ACHS-E2E-104 | FE+BE |
| TC-AC-ACHS-50 | TC-AC-ACHS-E2E-004 | FE+BE |
| TC-AC-ACHS-51 | TC-AC-ACHS-E2E-010 | FE+BE |
| TC-AC-ACHS-52 | TC-AC-ACHS-E2E-010 | FE+BE |
| TC-AC-ACHS-53 | TC-AC-ACHS-E2E-010 | FE+BE |
| TC-AC-ACHS-54 | TC-AC-ACHS-E2E-003 | FE+BE |
| TC-AC-ACHS-55 | TC-AC-ACHS-E2E-104 | FE+BE |
| TC-AC-ACHS-56 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-57 | TC-AC-ACHS-E2E-005 | FE+BE |
| TC-AC-ACHS-58 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-59 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-60 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-61 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-62 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-63 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-64 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-65 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-66 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-67 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-68 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-69 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-70 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-71 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-72 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-73 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-74 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-75 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-76 | TC-AC-ACHS-E2E-246 | FE+BE |
| TC-AC-ACHS-77 | TC-AC-ACHS-E2E-246 | FE+BE |
| TC-AC-ACHS-78 | TC-AC-ACHS-E2E-246 | FE+BE |
| TC-AC-ACHS-79 | TC-AC-ACHS-E2E-246 | FE+BE |
| TC-AC-ACHS-80 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-81 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-82 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-83 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-84 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-85 | TC-AC-ACHS-E2E-248 | FE+BE |
| TC-AC-ACHS-86 | TC-AC-ACHS-E2E-248 | FE+BE |
| TC-AC-ACHS-87 | TC-AC-ACHS-E2E-248 | FE+BE |
| TC-AC-ACHS-88 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-89 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-90 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-91 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-92 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-93 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-94 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-95 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-96 | TC-AC-ACHS-E2E-247 | FE+BE |
| TC-AC-ACHS-97 | TC-AC-ACHS-E2E-254 | FE+BE |
| TC-AC-ACHS-98 | TC-AC-ACHS-E2E-250 | FE+BE |
| TC-AC-ACHS-99 | TC-AC-ACHS-E2E-272 | FE+BE |
| TC-AC-ACHS-100 | TC-AC-ACHS-E2E-250 | FE+BE |
| TC-AC-ACHS-101 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-102 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-103 | TC-AC-ACHS-E2E-251 | FE+BE |
| TC-AC-ACHS-104 | TC-AC-ACHS-E2E-251 | FE+BE |
| TC-AC-ACHS-105 | TC-AC-ACHS-E2E-251 | FE+BE |
| TC-AC-ACHS-106 | TC-AC-ACHS-E2E-251 | FE+BE |
| TC-AC-ACHS-107 | TC-AC-ACHS-E2E-251 | FE+BE |
| TC-AC-ACHS-108 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-109 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-110 | TC-AC-ACHS-E2E-252 | FE+BE |
| TC-AC-ACHS-111 | TC-AC-ACHS-E2E-252 | FE+BE |
| TC-AC-ACHS-112 | TC-AC-ACHS-E2E-252 | FE+BE |
| TC-AC-ACHS-113 | TC-AC-ACHS-E2E-253 | FE+BE |
| TC-AC-ACHS-114 | TC-AC-ACHS-E2E-253 | FE+BE |
| TC-AC-ACHS-115 | TC-AC-ACHS-E2E-246 | FE+BE |
| TC-AC-ACHS-116 | TC-AC-ACHS-E2E-255 | FE+BE |
| TC-AC-ACHS-117 | TC-AC-ACHS-E2E-255 | FE+BE |
| TC-AC-ACHS-118 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-119 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-120 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-121 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-122 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-123 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-124 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-125 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-126 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-127 | TC-AC-ACHS-E2E-256 | FE+BE |
| TC-AC-ACHS-128 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-129 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-130 | TC-AC-ACHS-E2E-258 | FE+BE |
| TC-AC-ACHS-131 | TC-AC-ACHS-E2E-255 | FE+BE |
| TC-AC-ACHS-132 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-133 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-134 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-135 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-136 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-137 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-138 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-139 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-140 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-141 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-142 | TC-AC-ACHS-E2E-261 | FE+BE |
| TC-AC-ACHS-143 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-144 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-145 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-146 | TC-AC-ACHS-E2E-260 | FE+BE |
| TC-AC-ACHS-147 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-148 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-149 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-150 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-151 | TC-AC-ACHS-E2E-262 | FE+BE |
| TC-AC-ACHS-152 | TC-AC-ACHS-E2E-261 | FE+BE |
| TC-AC-ACHS-153 | TC-AC-ACHS-E2E-272 | FE+BE |
| TC-AC-ACHS-154 | TC-AC-ACHS-E2E-262 | FE+BE |
| TC-AC-ACHS-155 | TC-AC-ACHS-E2E-262 | FE+BE |
| TC-AC-ACHS-156 | TC-AC-ACHS-E2E-263 | FE+BE |
| TC-AC-ACHS-157 | TC-AC-ACHS-E2E-263 | FE+BE |
| TC-AC-ACHS-158 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-159 | TC-AC-ACHS-E2E-255 | FE+BE |
| TC-AC-ACHS-160 | TC-AC-ACHS-E2E-257 | FE+BE |
| TC-AC-ACHS-161 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-162 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-163 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-164 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-165 | TC-AC-ACHS-E2E-266 | FE+BE |
| TC-AC-ACHS-166 | TC-AC-ACHS-E2E-272 | FE+BE |
| TC-AC-ACHS-167 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-168 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-169 | TC-AC-ACHS-E2E-265 | FE+BE |
| TC-AC-ACHS-170 | TC-AC-ACHS-E2E-265 | FE+BE |
| TC-AC-ACHS-171 | TC-AC-ACHS-E2E-265 | FE+BE |
| TC-AC-ACHS-172 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-173 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-174 | TC-AC-ACHS-E2E-264 | FE+BE |
| TC-AC-ACHS-175 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-176 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-177 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-178 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-179 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-180 | TC-AC-ACHS-E2E-268 | FE+BE |
| TC-AC-ACHS-181 | TC-AC-ACHS-E2E-270 | FE+BE |
| TC-AC-ACHS-182 | TC-AC-ACHS-E2E-268 | FE+BE |
| TC-AC-ACHS-183 | TC-AC-ACHS-E2E-269 | FE+BE |
| TC-AC-ACHS-184 | TC-AC-ACHS-E2E-269 | FE+BE |
| TC-AC-ACHS-185 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-186 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-187 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-188 | TC-AC-ACHS-E2E-273 | FE+BE |
| TC-AC-ACHS-189 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-190 | TC-AC-ACHS-E2E-271 | FE+BE |
| TC-AC-ACHS-191 | TC-AC-ACHS-E2E-271 | FE+BE |
| TC-AC-ACHS-192 | TC-AC-ACHS-E2E-271 | FE+BE |
| TC-AC-ACHS-193 | TC-AC-ACHS-E2E-271 | FE+BE |
| TC-AC-ACHS-194 | TC-AC-ACHS-E2E-271 | FE+BE |
| TC-AC-ACHS-195 | TC-AC-ACHS-E2E-268 | FE+BE |
| TC-AC-ACHS-196 | TC-AC-ACHS-E2E-084 | FE+BE |
| TC-AC-ACHS-197 | TC-AC-ACHS-E2E-020 | FE+BE |
| TC-AC-ACHS-198 | TC-AC-ACHS-E2E-084 | FE+BE |
| TC-AC-ACHS-199 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-200 | TC-AC-ACHS-E2E-245 | FE+BE |
| TC-AC-ACHS-201 | TC-AC-ACHS-E2E-021 | FE+BE |
| TC-AC-ACHS-202 | TC-AC-ACHS-E2E-084 | FE+BE |
| TC-AC-ACHS-203 | TC-AC-ACHS-E2E-084 | FE+BE |
| TC-AC-ACHS-204 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-205 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-206 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-207 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-208 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-209 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-210 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-211 | TC-AC-ACHS-E2E-120 | FE+BE |
| TC-AC-ACHS-212 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-213 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-214 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-215 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-216 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-217 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-218 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-219 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-220 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-221 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-222 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-223 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-224 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-225 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-226 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-227 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-228 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-229 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-230 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-231 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-232 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-233 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-234 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-235 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-236 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-237 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-238 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-239 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-240 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-241 | TC-AC-ACHS-E2E-124 | FE+BE |
| TC-AC-ACHS-242 | TC-AC-ACHS-E2E-125 | FE+BE |
| TC-AC-ACHS-243 | TC-AC-ACHS-E2E-125 | FE+BE |
| TC-AC-ACHS-244 | TC-AC-ACHS-E2E-125 | FE+BE |
| TC-AC-ACHS-245 | TC-AC-ACHS-E2E-125 | FE+BE |
| TC-AC-ACHS-246 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-247 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-248 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-249 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-250 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-251 | TC-AC-ACHS-E2E-127 | FE+BE |
| TC-AC-ACHS-252 | TC-AC-ACHS-E2E-127 | FE+BE |
| TC-AC-ACHS-253 | TC-AC-ACHS-E2E-127 | FE+BE |
| TC-AC-ACHS-254 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-255 | TC-AC-ACHS-E2E-286 | FE+BE |
| TC-AC-ACHS-256 | TC-AC-ACHS-E2E-127 | FE+BE |
| TC-AC-ACHS-257 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-258 | TC-AC-ACHS-E2E-123 | FE+BE |
| TC-AC-ACHS-259 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-260 | TC-AC-ACHS-E2E-126 | FE+BE |
| TC-AC-ACHS-261 | TC-AC-ACHS-E2E-286 | FE+BE |
| TC-AC-ACHS-262 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-263 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-264 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-265 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-266 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-267 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-268 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-269 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-270 | TC-AC-ACHS-E2E-130 | FE+BE |
| TC-AC-ACHS-271 | TC-AC-ACHS-E2E-131 | FE+BE |
| TC-AC-ACHS-272 | TC-AC-ACHS-E2E-131 | FE+BE |
| TC-AC-ACHS-273 | TC-AC-ACHS-E2E-131 | FE+BE |
| TC-AC-ACHS-274 | TC-AC-ACHS-E2E-131 | FE+BE |
| TC-AC-ACHS-275 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-276 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-277 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-278 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-279 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-280 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-281 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-282 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-283 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-284 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-285 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-286 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-287 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-288 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-289 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-290 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-291 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-292 | TC-AC-ACHS-E2E-133 | FE+BE |
| TC-AC-ACHS-293 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-294 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-295 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-296 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-297 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-298 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-299 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-300 | TC-AC-ACHS-E2E-134 | FE+BE |
| TC-AC-ACHS-301 | TC-AC-ACHS-E2E-135 | FE+BE |
| TC-AC-ACHS-302 | TC-AC-ACHS-E2E-135 | FE+BE |
| TC-AC-ACHS-303 | TC-AC-ACHS-E2E-135 | FE+BE |
| TC-AC-ACHS-304 | TC-AC-ACHS-E2E-135 | FE+BE |
| TC-AC-ACHS-305 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-306 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-307 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-308 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-309 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-310 | TC-AC-ACHS-E2E-137 | FE+BE |
| TC-AC-ACHS-311 | TC-AC-ACHS-E2E-137 | FE+BE |
| TC-AC-ACHS-312 | TC-AC-ACHS-E2E-137 | FE+BE |
| TC-AC-ACHS-313 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-314 | TC-AC-ACHS-E2E-138 | FE+BE |
| TC-AC-ACHS-315 | TC-AC-ACHS-E2E-137 | FE+BE |
| TC-AC-ACHS-316 | TC-AC-ACHS-E2E-287 | FE+BE |
| TC-AC-ACHS-317 | TC-AC-ACHS-E2E-288 | FE+BE |
| TC-AC-ACHS-318 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-319 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-320 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-321 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-322 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-323 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-324 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-325 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-326 | TC-AC-ACHS-E2E-160 | FE+BE |
| TC-AC-ACHS-327 | TC-AC-ACHS-E2E-161 | FE+BE |
| TC-AC-ACHS-328 | TC-AC-ACHS-E2E-161 | FE+BE |
| TC-AC-ACHS-329 | TC-AC-ACHS-E2E-161 | FE+BE |
| TC-AC-ACHS-330 | TC-AC-ACHS-E2E-161 | FE+BE |
| TC-AC-ACHS-331 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-332 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-333 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-334 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-335 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-336 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-337 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-338 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-339 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-340 | TC-AC-ACHS-E2E-162 | FE+BE |
| TC-AC-ACHS-341 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-342 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-343 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-344 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-345 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-346 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-347 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-348 | TC-AC-ACHS-E2E-163 | FE+BE |
| TC-AC-ACHS-349 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-350 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-351 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-352 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-353 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-354 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-355 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-356 | TC-AC-ACHS-E2E-164 | FE+BE |
| TC-AC-ACHS-357 | TC-AC-ACHS-E2E-165 | FE+BE |
| TC-AC-ACHS-358 | TC-AC-ACHS-E2E-165 | FE+BE |
| TC-AC-ACHS-359 | TC-AC-ACHS-E2E-165 | FE+BE |
| TC-AC-ACHS-360 | TC-AC-ACHS-E2E-165 | FE+BE |
| TC-AC-ACHS-361 | TC-AC-ACHS-E2E-166 | FE+BE |
| TC-AC-ACHS-362 | TC-AC-ACHS-E2E-167 | FE+BE |
| TC-AC-ACHS-363 | TC-AC-ACHS-E2E-167 | FE+BE |
| TC-AC-ACHS-364 | TC-AC-ACHS-E2E-167 | FE+BE |
| TC-AC-ACHS-365 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-366 | TC-AC-ACHS-E2E-168 | FE+BE |
| TC-AC-ACHS-367 | TC-AC-ACHS-E2E-167 | FE+BE |
| TC-AC-ACHS-368 | TC-AC-ACHS-E2E-166 | FE+BE |
| TC-AC-ACHS-369 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-370 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-371 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-372 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-373 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-374 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-375 | TC-AC-ACHS-E2E-180 | FE+BE |
| TC-AC-ACHS-376 | TC-AC-ACHS-E2E-181 | FE+BE |
| TC-AC-ACHS-377 | TC-AC-ACHS-E2E-181 | FE+BE |
| TC-AC-ACHS-378 | TC-AC-ACHS-E2E-181 | FE+BE |
| TC-AC-ACHS-379 | TC-AC-ACHS-E2E-181 | FE+BE |
| TC-AC-ACHS-380 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-381 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-382 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-383 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-384 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-385 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-386 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-387 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-388 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-389 | TC-AC-ACHS-E2E-182 | FE+BE |
| TC-AC-ACHS-390 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-391 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-392 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-393 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-394 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-395 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-396 | TC-AC-ACHS-E2E-184 | FE+BE |
| TC-AC-ACHS-397 | TC-AC-ACHS-E2E-184 | FE+BE |
| TC-AC-ACHS-398 | TC-AC-ACHS-E2E-184 | FE+BE |
| TC-AC-ACHS-399 | TC-AC-ACHS-E2E-184 | FE+BE |
| TC-AC-ACHS-400 | TC-AC-ACHS-E2E-184 | FE+BE |
| TC-AC-ACHS-401 | TC-AC-ACHS-E2E-185 | FE+BE |
| TC-AC-ACHS-402 | TC-AC-ACHS-E2E-185 | FE+BE |
| TC-AC-ACHS-403 | TC-AC-ACHS-E2E-185 | FE+BE |
| TC-AC-ACHS-404 | TC-AC-ACHS-E2E-185 | FE+BE |
| TC-AC-ACHS-405 | TC-AC-ACHS-E2E-186 | FE+BE |
| TC-AC-ACHS-406 | TC-AC-ACHS-E2E-186 | FE+BE |
| TC-AC-ACHS-407 | TC-AC-ACHS-E2E-186 | FE+BE |
| TC-AC-ACHS-408 | TC-AC-ACHS-E2E-186 | FE+BE |
| TC-AC-ACHS-409 | TC-AC-ACHS-E2E-186 | FE+BE |
| TC-AC-ACHS-410 | TC-AC-ACHS-E2E-187 | FE+BE |
| TC-AC-ACHS-411 | TC-AC-ACHS-E2E-187 | FE+BE |
| TC-AC-ACHS-412 | TC-AC-ACHS-E2E-187 | FE+BE |
| TC-AC-ACHS-413 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-414 | TC-AC-ACHS-E2E-188 | FE+BE |
| TC-AC-ACHS-415 | TC-AC-ACHS-E2E-187 | FE+BE |
| TC-AC-ACHS-416 | TC-AC-ACHS-E2E-289 | FE+BE |
| TC-AC-ACHS-417 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-418 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-419 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-420 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-421 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-422 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-423 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-424 | TC-AC-ACHS-E2E-200 | FE+BE |
| TC-AC-ACHS-425 | TC-AC-ACHS-E2E-201 | FE+BE |
| TC-AC-ACHS-426 | TC-AC-ACHS-E2E-201 | FE+BE |
| TC-AC-ACHS-427 | TC-AC-ACHS-E2E-201 | FE+BE |
| TC-AC-ACHS-428 | TC-AC-ACHS-E2E-201 | FE+BE |
| TC-AC-ACHS-429 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-430 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-431 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-432 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-433 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-434 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-435 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-436 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-437 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-438 | TC-AC-ACHS-E2E-202 | FE+BE |
| TC-AC-ACHS-439 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-440 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-441 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-442 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-443 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-444 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-445 | TC-AC-ACHS-E2E-203 | FE+BE |
| TC-AC-ACHS-446 | TC-AC-ACHS-E2E-204 | FE+BE |
| TC-AC-ACHS-447 | TC-AC-ACHS-E2E-204 | FE+BE |
| TC-AC-ACHS-448 | TC-AC-ACHS-E2E-204 | FE+BE |
| TC-AC-ACHS-449 | TC-AC-ACHS-E2E-204 | FE+BE |
| TC-AC-ACHS-450 | TC-AC-ACHS-E2E-204 | FE+BE |
| TC-AC-ACHS-451 | TC-AC-ACHS-E2E-205 | FE+BE |
| TC-AC-ACHS-452 | TC-AC-ACHS-E2E-205 | FE+BE |
| TC-AC-ACHS-453 | TC-AC-ACHS-E2E-205 | FE+BE |
| TC-AC-ACHS-454 | TC-AC-ACHS-E2E-205 | FE+BE |
| TC-AC-ACHS-455 | TC-AC-ACHS-E2E-206 | FE+BE |
| TC-AC-ACHS-456 | TC-AC-ACHS-E2E-206 | FE+BE |
| TC-AC-ACHS-457 | TC-AC-ACHS-E2E-206 | FE+BE |
| TC-AC-ACHS-458 | TC-AC-ACHS-E2E-206 | FE+BE |
| TC-AC-ACHS-459 | TC-AC-ACHS-E2E-206 | FE+BE |
| TC-AC-ACHS-460 | TC-AC-ACHS-E2E-207 | FE+BE |
| TC-AC-ACHS-461 | TC-AC-ACHS-E2E-207 | FE+BE |
| TC-AC-ACHS-462 | TC-AC-ACHS-E2E-207 | FE+BE |
| TC-AC-ACHS-463 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-464 | TC-AC-ACHS-E2E-208 | FE+BE |
| TC-AC-ACHS-465 | TC-AC-ACHS-E2E-207 | FE+BE |
| TC-AC-ACHS-466 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-467 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-468 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-469 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-470 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-471 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-472 | TC-AC-ACHS-E2E-220 | FE+BE |
| TC-AC-ACHS-473 | TC-AC-ACHS-E2E-221 | FE+BE |
| TC-AC-ACHS-474 | TC-AC-ACHS-E2E-221 | FE+BE |
| TC-AC-ACHS-475 | TC-AC-ACHS-E2E-221 | FE+BE |
| TC-AC-ACHS-476 | TC-AC-ACHS-E2E-221 | FE+BE |
| TC-AC-ACHS-477 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-478 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-479 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-480 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-481 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-482 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-483 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-484 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-485 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-486 | TC-AC-ACHS-E2E-222 | FE+BE |
| TC-AC-ACHS-487 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-488 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-489 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-490 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-491 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-492 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-493 | TC-AC-ACHS-E2E-223 | FE+BE |
| TC-AC-ACHS-494 | TC-AC-ACHS-E2E-224 | FE+BE |
| TC-AC-ACHS-495 | TC-AC-ACHS-E2E-224 | FE+BE |
| TC-AC-ACHS-496 | TC-AC-ACHS-E2E-224 | FE+BE |
| TC-AC-ACHS-497 | TC-AC-ACHS-E2E-224 | FE+BE |
| TC-AC-ACHS-498 | TC-AC-ACHS-E2E-224 | FE+BE |
| TC-AC-ACHS-499 | TC-AC-ACHS-E2E-225 | FE+BE |
| TC-AC-ACHS-500 | TC-AC-ACHS-E2E-225 | FE+BE |
| TC-AC-ACHS-501 | TC-AC-ACHS-E2E-225 | FE+BE |
| TC-AC-ACHS-502 | TC-AC-ACHS-E2E-225 | FE+BE |
| TC-AC-ACHS-503 | TC-AC-ACHS-E2E-226 | FE+BE |
| TC-AC-ACHS-504 | TC-AC-ACHS-E2E-226 | FE+BE |
| TC-AC-ACHS-505 | TC-AC-ACHS-E2E-226 | FE+BE |
| TC-AC-ACHS-506 | TC-AC-ACHS-E2E-226 | FE+BE |
| TC-AC-ACHS-507 | TC-AC-ACHS-E2E-226 | FE+BE |
| TC-AC-ACHS-508 | TC-AC-ACHS-E2E-227 | FE+BE |
| TC-AC-ACHS-509 | TC-AC-ACHS-E2E-227 | FE+BE |
| TC-AC-ACHS-510 | TC-AC-ACHS-E2E-227 | FE+BE |
| TC-AC-ACHS-511 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-512 | TC-AC-ACHS-E2E-228 | FE+BE |
| TC-AC-ACHS-513 | TC-AC-ACHS-E2E-227 | FE+BE |
| TC-AC-ACHS-514 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-515 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-516 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-517 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-518 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-519 | TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-520 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-521 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-522 | TC-AC-ACHS-E2E-104 | FE+BE |
| TC-AC-ACHS-523 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-524 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-525 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-526 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-527 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-528 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-529 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-530 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-531 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-532 | TC-AC-ACHS-E2E-275 | FE+BE |
| TC-AC-ACHS-533 | TC-AC-ACHS-E2E-275 | FE+BE |
| TC-AC-ACHS-534 | TC-AC-ACHS-E2E-275 | FE+BE |
| TC-AC-ACHS-535 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-536 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-537 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-538 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-539 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-540 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-541 | TC-AC-ACHS-E2E-276 | FE+BE |
| TC-AC-ACHS-542 | TC-AC-ACHS-E2E-277 | FE+BE |
| TC-AC-ACHS-543 | TC-AC-ACHS-E2E-277 | FE+BE |
| TC-AC-ACHS-544 | TC-AC-ACHS-E2E-275 | FE+BE |
| TC-AC-ACHS-545 | TC-AC-ACHS-E2E-277 | FE+BE |
| TC-AC-ACHS-546 | TC-AC-ACHS-E2E-278 | FE+BE |
| TC-AC-ACHS-547 | TC-AC-ACHS-E2E-278 | FE+BE |
| TC-AC-ACHS-548 | TC-AC-ACHS-E2E-278 | FE+BE |
| TC-AC-ACHS-549 | TC-AC-ACHS-E2E-278 | FE+BE |
| TC-AC-ACHS-550 | TC-AC-ACHS-E2E-278 | FE+BE |
| TC-AC-ACHS-551 | TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-552 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-553 | TC-AC-ACHS-E2E-280 | FE+BE |
| TC-AC-ACHS-554 | TC-AC-ACHS-E2E-280 | FE+BE |
| TC-AC-ACHS-555 | TC-AC-ACHS-E2E-279 | FE+BE |
| TC-AC-ACHS-556 | TC-AC-ACHS-E2E-279 | FE+BE |
| TC-AC-ACHS-557 | TC-AC-ACHS-E2E-279 | FE+BE |
| TC-AC-ACHS-558 | TC-AC-ACHS-E2E-279, TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-559 | TC-AC-ACHS-E2E-279 | FE+BE |
| TC-AC-ACHS-560 | TC-AC-ACHS-E2E-282 | FE+BE |
| TC-AC-ACHS-561 | TC-AC-ACHS-E2E-282 | FE+BE |
| TC-AC-ACHS-562 | TC-AC-ACHS-E2E-282 | FE+BE |
| TC-AC-ACHS-563 | TC-AC-ACHS-E2E-283 | FE+BE |
| TC-AC-ACHS-564 | TC-AC-ACHS-E2E-277 | FE+BE |
| TC-AC-ACHS-565 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-566 | TC-AC-ACHS-E2E-022 | FE+BE |
| TC-AC-ACHS-567 | TC-AC-ACHS-E2E-242 | FE+BE |
| TC-AC-ACHS-568 | TC-AC-ACHS-E2E-242 | FE+BE |
| TC-AC-ACHS-569 | TC-AC-ACHS-E2E-242 | FE+BE |
| TC-AC-ACHS-570 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-571 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-572 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-573 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-574 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-575 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-576 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-577 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-578 | TC-AC-ACHS-E2E-244 | FE+BE |
| TC-AC-ACHS-579 | TC-AC-ACHS-E2E-284 | FE+BE |
| TC-AC-ACHS-580 | TC-AC-ACHS-E2E-105 | FE+BE |
| TC-AC-ACHS-581 | TC-AC-ACHS-E2E-103 | FE+BE |
| TC-AC-ACHS-582 | TC-AC-ACHS-E2E-267 | FE+BE |
| TC-AC-ACHS-583 | TC-AC-ACHS-E2E-283 | FE+BE |
| TC-AC-ACHS-584 | TC-AC-ACHS-E2E-283 | FE+BE |
| TC-AC-ACHS-585 | TC-AC-ACHS-E2E-272 | FE+BE |
| TC-AC-ACHS-586 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-587 | TC-AC-ACHS-E2E-274 | FE+BE |
| TC-AC-ACHS-588 | TC-AC-ACHS-E2E-104 | FE+BE |
| TC-AC-ACHS-589 | TC-AC-ACHS-E2E-092 | FE+BE |
| TC-AC-ACHS-590 | TC-AC-ACHS-E2E-004 | FE+BE |
| TC-AC-ACHS-591 | TC-AC-ACHS-E2E-269 | FE+BE |
| TC-AC-ACHS-592 | TC-AC-ACHS-E2E-259 | FE+BE |
| TC-AC-ACHS-593 | TC-AC-ACHS-E2E-010 | FE+BE |
| TC-AC-ACHS-594 | TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-595 | TC-AC-ACHS-E2E-243, TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-596 | TC-AC-ACHS-E2E-243, TC-AC-ACHS-E2E-281 | FE+BE |
| TC-AC-ACHS-597 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-598 | TC-AC-ACHS-E2E-243 | FE+BE |
| TC-AC-ACHS-599 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-600 | TC-AC-ACHS-E2E-249 | FE+BE |
| TC-AC-ACHS-601 | TC-AC-ACHS-E2E-125 | FE+BE |
| TC-AC-ACHS-602 | TC-AC-ACHS-E2E-185 | FE+BE |
| TC-AC-ACHS-603 | TC-AC-ACHS-E2E-280 | FE+BE |
| TC-AC-ACHS-604 | TC-AC-ACHS-E2E-269 | FE+BE |
| TC-AC-ACHS-605 | TC-AC-ACHS-E2E-240 | FE+BE |
| TC-AC-ACHS-606 | TC-AC-ACHS-E2E-121 | FE+BE |
| TC-AC-ACHS-607 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-608 | TC-AC-ACHS-E2E-285 | FE+BE |
| TC-AC-ACHS-609 | TC-AC-ACHS-E2E-240 | FE+BE |

## TC hanya-BE (tidak masuk spec)

Tidak ada. Modul ini tidak punya TC backend terpisah dan semua 609 TC memuat langkah atau observasi tingkat UI (0 TC dilewati).
