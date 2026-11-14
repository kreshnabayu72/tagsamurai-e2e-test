# Coverage E2E — Fixed Asset > TAG

Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (1501 TC, ID `TC-FA-TAG-1`–`1508`; ID yang dihapus tidak dipakai ulang). Suite: `specs/FixedAsset/Tag/`. Prefix: `FA` + `TAG` (`TC-FA-TAG-E2E-*`). Status semua spec: `draft`, belum ada script. `tc-tag-backend.md` tidak ada dan tidak dipakai untuk suite ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 1501 TC masuk 388 spec; tidak ada TC hanya-BE yang dikeluarkan. Setiap TC terpetakan ke tepat satu spec, kecuali TC yang terbelah antara spec asal dan spec absence menurut S-05 (lihat bagian "Pembagian TC lintas spec: asersi absence log (S-05)"). TC kelas K-1 (Expected berupa respons API) tetap masuk sebagai spec FE+BE; modul ini tidak punya `openapi.yaml` dan `low-level-design.md`, sehingga tidak ada spec `Mode: mock`.

## TC hanya-BE (tidak masuk spec)

Tidak ada.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-TAG-E2E-001-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-1 | Screening Halaman TAG Tab Paired: Header, Kartu, Table Tools, Tabel Grup, Breadcrumb, dan Tab Awal | FE+BE | 31 | 1, 2, 3 |
| TC-FA-TAG-E2E-002-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-2 | Tooltip Toolbar dan Header Kolom Actions Tab Paired | FE+BE | 16 | 8, 9, 10, 11, 12 |
| TC-FA-TAG-E2E-003-state-loading-respons-ditunda-tab-paired-kartu-dan-to-be-returned | State Loading Saat Respons Ditunda pada Tab Paired, Kartu Filter, dan Tabel To Be Returned | FE+BE | 18 | 14, 29, 86 |
| TC-FA-TAG-E2E-004-empty-state-dataset-kosong-paired-to-be-returned-changelog-dan-event-log | Empty State Tab Paired, Tab To Be Returned, Modal Changelog, dan Modal Event Log Saat Dataset Kosong | FE+BE | 14 | 15, 85, 939, 1477 |
| TC-FA-TAG-E2E-005-search-tanpa-hasil-scroll-horizontal-dan-aksesibilitas-tab-paired | Search Tanpa Hasil, Scroll Horizontal pada Layar Sempit, dan Aksesibilitas Tab Paired | FE+BE | 34 | 18, 19, 20, 21, 22, 23 |
| TC-FA-TAG-E2E-006-kartu-filter-screening-dan-tooltip | Screening Kartu Filter Tab Paired dan Tooltip Ikon Info Tiap Kartu | FE+BE | 18 | 25, 26, 27, 28 |
| TC-FA-TAG-E2E-007-kartu-filter-klik-pilih-batal-dan-state-per-tab-bagian-1 | Kartu Filter: Klik untuk Memfilter, Klik Ulang untuk Membatalkan, Satu Kartu Aktif, dan Popup Detail Not Paired Yet | FE+BE | 34 | 31, 32, 33, 34, 35, 36, 37, 38 |
| TC-FA-TAG-E2E-008-kartu-filter-klik-pilih-batal-dan-state-per-tab-bagian-2 | Kartu Filter: Gabungan dengan Search, State Independen per Tab, dan Role Read Only | FE+BE | 19 | 39, 40, 41 |
| TC-FA-TAG-E2E-009-popup-detail-assets-screening-buka-dan-tutup | Screening Popup Detail Assets: Cara Buka dan Tutup serta Blok Info Reported, Non-standard, dan Not Paired Yet | FE+BE | 39 | 42, 43, 44, 45, 46, 47, 48, 49 |
| TC-FA-TAG-E2E-010-popup-detail-tombol-show-reported-non-standard-dan-not-paired-bagian-1 | Popup Detail: Tombol Show dan Close untuk Reported, Non-standard, dan Not Paired Yet | FE+BE | 28 | 50, 51, 52, 53, 54, 55 |
| TC-FA-TAG-E2E-011-popup-detail-tombol-show-reported-non-standard-dan-not-paired-bagian-2 | Popup Detail: Interaksi Show Reported dengan Not Paired Yet, Reset Saat Ditutup, dan Terpisah dari Search dan Filter | FE+BE | 25 | 56, 57, 58, 1450 |
| TC-FA-TAG-E2E-012-popup-detail-jumlah-baris-aset-dua-tag-dan-hover-group | Popup Detail: Jumlah Baris Sama dengan Total Assets, Aset dengan Dua Tag, dan Hover Badge Group | FE+BE | 12 | 59, 60, 61 |
| TC-FA-TAG-E2E-013-guided-tooltip-fa-tag-langkah-navigasi-dan-penutupan-bagian-1 | Guided Tooltip fa-tag: Kunjungan Pertama, Langkah 1 sampai 4, serta Penutupan lewat Done, Skip, dan Overlay | FE+BE | 35 | 62, 63, 64, 65, 66, 67, 68 |
| TC-FA-TAG-E2E-014-guided-tooltip-fa-tag-langkah-navigasi-dan-penutupan-bagian-2 | Guided Tooltip fa-tag: Tombol Back, Navigasi Keyboard, dan Resize Viewport Menutup Tanpa Menandai Seen | FE+BE | 26 | 69, 70, 74 |
| TC-FA-TAG-E2E-015-guided-tooltip-replay-dan-flag-seen-true | Guided Tooltip fa-tag: Tombol Replay Show Guide dan Walkthrough Tidak Muncul Otomatis Bila Flag Seen Sudah True | FE+BE | 9 | 71, 72 |
| TC-FA-TAG-E2E-016-screening-tab-to-be-returned-header-kolom-dan-format-sel-bagian-1 | Screening Tab To Be Returned: Header, Tooltip Toolbar, Kolom Tabel, Urutan Bawaan, dan Format Sel | FE+BE | 29 | 76, 77, 78, 79, 80 |
| TC-FA-TAG-E2E-017-screening-tab-to-be-returned-header-kolom-dan-format-sel-bagian-2 | Tab To Be Returned: Hover Return Group dan Current Holder, Nilai Kosong, Reason, Breadcrumb Antar Tab, Tag QR, dan Popup TAG Log | FE+BE | 31 | 81, 82, 83, 84, 88, 89, 90 |
| TC-FA-TAG-E2E-018-screening-halaman-tag-tab-paired-breadcrumb-dan-tooltip-toolbar-bagian-3 | Screening Halaman TAG: Badge Tab To Be Returned, Pindah Tab, Table Tools Tab To Be Returned, dan Placeholder Search | FE+BE | 19 | 4, 5, 6, 7 |
| TC-FA-TAG-E2E-019-guided-tooltip-fa-tag-varian-tab-to-be-returned-dan-target-langkah | Guided Tooltip fa-tag: Teks Langkah 3 dan 4 Varian Tab To Be Returned serta Target Sorotan Tiap Langkah | FE+BE | 23 | 73, 75 |
| TC-FA-TAG-E2E-020-role-matrix-visibilitas-elemen-halaman-per-role-bagian-1 | Role Matrix: Visibilitas Elemen Halaman TAG per Role (Bagian 1) | FE+BE | 21 | 91, 92 |
| TC-FA-TAG-E2E-021-role-matrix-visibilitas-elemen-halaman-per-role-bagian-2 | Role Matrix: Visibilitas Elemen Halaman TAG per Role (Bagian 2) | FE+BE | 21 | 93, 94 |
| TC-FA-TAG-E2E-022-role-matrix-negatif-menu-tag-dan-event-log-role-lain | Role Matrix: Menu TAG dan Event Log Tidak Tersedia bagi Role Lain | FE+BE | 8 | 95, 96, 121 |
| TC-FA-TAG-E2E-023-role-matrix-positif-aksi-tulis-total-control-dan-manage-read-bagian-1 | Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 1) | FE+BE | 33 | 97, 98, 99, 100, 101, 102, 115, 116 |
| TC-FA-TAG-E2E-024-role-matrix-positif-aksi-tulis-total-control-dan-manage-read-bagian-2 | Role Matrix Positif: Aksi Tulis Total Control dan Manage asset & TAG (Read + Update) (Bagian 2) | FE+BE | 22 | 117, 118, 119, 120 |
| TC-FA-TAG-E2E-025-role-matrix-negatif-aksi-tulis-read-only-bagian-1 | Role Matrix Negatif: Aksi Tulis pada Halaman TAG untuk Read Only (Bagian 1) | FE+BE | 32 | 103, 104, 105, 106, 107, 108 |
| TC-FA-TAG-E2E-026-role-matrix-negatif-aksi-tulis-read-only-bagian-2 | Role Matrix Negatif: Pemicu Report TAG Tidak Ada bagi Read Only | FE+BE | 10 | 123 |
| TC-FA-TAG-E2E-027-role-matrix-negatif-aksi-tulis-manage-asset-tag-read | Role Matrix Negatif: Aksi Tulis pada Halaman TAG untuk Manage asset & TAG (Read) | FE+BE | 32 | 109, 110, 111, 112, 113, 114 |
| TC-FA-TAG-E2E-028-role-matrix-toolbar-replace-tag-dan-print-qr-empat-role | Role Matrix: Tombol Toolbar Replace TAG dan Print QR per Role | FE+BE | 14 | 144, 145, 146, 147 |
| TC-FA-TAG-E2E-029-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard | Role Matrix: Row Action Replace TAG, Batch Replace TAG, dan Aksi Grup Replace non-standard TAGs | FE+BE | 34 | 148, 149, 150 |
| TC-FA-TAG-E2E-030-role-matrix-pair-tag-row-action-dan-bulk | Role Matrix: Pair TAG pada Row Action dan Bulk Action Bar | FE+BE | 31 | 153, 154, 155, 156 |
| TC-FA-TAG-E2E-031-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-1 | Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 1) | FE+BE | 28 | 122, 124, 125, 126, 127 |
| TC-FA-TAG-E2E-032-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-2 | Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 2) | FE+BE | 26 | 130, 162 |
| TC-FA-TAG-E2E-033-scope-group-grup-popup-detail-kartu-dan-search-bagian-1 | Scope Group: Grup, Popup Detail, dan Nilai Kartu per Role (Bagian 1) | FE+BE | 21 | 30, 131, 132, 133, 134, 135, 136, 137 |
| TC-FA-TAG-E2E-034-scope-group-grup-popup-detail-kartu-dan-search-bagian-2 | Scope Group: Search Tidak Menampilkan Grup di Luar Scope | FE+BE | 3 | 138 |
| TC-FA-TAG-E2E-035-scope-group-modal-changelog-dan-event-log | Scope Group: Modal Changelog dan Event Log | FE+BE | 14 | 139, 140, 141 |
| TC-FA-TAG-E2E-036-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-1 | Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 1) | FE+BE | 40 | 163, 164, 165, 166, 167 |
| TC-FA-TAG-E2E-037-role-matrix-aksi-receive-dan-event-log-to-be-returned-bagian-2 | Role Matrix: Aksi Receive dan Event Log To Be Returned per Role (Bagian 2) | FE+BE | 29 | 168, 169, 170, 1489, 1490 |
| TC-FA-TAG-E2E-038-pemegang-update-return-group-menyelesaikan-receive | Pemegang Update pada Return Group Menyelesaikan Receive | FE+BE | 23 | 171, 172, 173 |
| TC-FA-TAG-E2E-039-role-matrix-decline-report-row-action | Role Matrix: Row Action Decline Report | FE+BE | 28 | 174, 175, 176, 177, 178, 179 |
| TC-FA-TAG-E2E-040-role-matrix-report-tag-dan-cancel-report-dari-modul-audit | Role Matrix: Report TAG dan Cancel Report dari Modul Audit | FE+BE | 32 | 180, 181, 182, 183, 184, 185, 186 |
| TC-FA-TAG-E2E-041-aksi-tulis-oleh-pemegang-manage-read-update-pair-batch-replace-dan | Aksi Tulis oleh Pemegang Manage asset & TAG (Read + Update): Pair TAG, Batch Replace TAG, dan Print QR | FE+BE | 30 | 1431, 1432, 1433 |
| TC-FA-TAG-E2E-042-role-matrix-row-action-batch-replace-dan-aksi-grup-replace-non-standard-update-parsial | Role Matrix: Aksi Replace TAG bagi Pemegang Update pada Group Plant A dan Descendant | FE+BE | 13 | 151, 152 |
| TC-FA-TAG-E2E-043-hak-parsial-update-read-per-group-pada-aksi-halaman-bagian-3 | Hak Parsial Update dan Read per Group pada Aksi Halaman TAG (Bagian 3) | FE+BE | 22 | 157, 158, 159, 160, 161 |
| TC-FA-TAG-E2E-044-row-action-per-kondisi-aset-urutan-dan-penghitungan-ulang-bagian-1 | Row Action per Kondisi Aset di Popup Detail: Replace TAG, Decline Report, dan Pair TAG | FE+BE | 35 | 189, 190, 191, 192, 193, 194, 195, 196 |
| TC-FA-TAG-E2E-045-row-action-per-kondisi-aset-urutan-dan-penghitungan-ulang-bagian-2 | Row Action Dihitung Ulang Setelah Laporan Ditutup dan Urutan Aksi Dark Sebelum Danger | FE+BE | 8 | 197, 198 |
| TC-FA-TAG-E2E-046-bulk-action-bar-dan-kebab-aksi-grup-visibilitas-dan-seleksi-bagian-1 | Bulk Action Bar Popup Detail: Visibilitas Pair TAG dan Batch Replace TAG, serta Jumlah Terpilih | FE+BE | 32 | 199, 200, 201, 202, 203, 204, 205 |
| TC-FA-TAG-E2E-047-bulk-action-bar-dan-kebab-aksi-grup-visibilitas-dan-seleksi-bagian-2 | Seleksi Checkbox Header dan Select All, Tabel Grup Tanpa Bulk Action, serta Kebab Aksi Grup | FE+BE | 25 | 206, 207, 208, 209, 210, 211 |
| TC-FA-TAG-E2E-048-popup-tag-log-pintu-masuk-dari-tabel-paired | Popup TAG Log: Pintu Masuk dari Klik TAG Code di Popup Detail | FE+BE | 33 | 212, 213, 214, 215, 216, 217, 218 |
| TC-FA-TAG-E2E-049-download-tab-paired-pilihan-nama-berkas-search-filter-kolom-bagian-1 | Download Tab Paired: Pilihan CSV dan XLSX, Nama Berkas, serta Pengaruh Search, Filter, Kolom, dan Jumlah Baris | FE+BE | 34 | 219, 220, 221, 224, 225, 226, 227 |
| TC-FA-TAG-E2E-050-download-tab-paired-pilihan-nama-berkas-search-filter-kolom-bagian-2 | Download Tab Paired: Urutan Mengikuti Sort, Tanpa Hasil, dan Ketersediaan untuk Role Read Only dan Read | FE+BE | 21 | 228, 229, 234, 235 |
| TC-FA-TAG-E2E-051-overlay-scan-replace-screening-dan-identifikasi-aset-paired | Overlay Scan Replace TAG: Screening dan Identifikasi Aset dari Tag Paired | FE+BE | 34 | 236, 237, 238, 239, 258, 265 |
| TC-FA-TAG-E2E-052-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-1 | Overlay Scan Replace TAG: Dialog Blok D-01 Aset Disposal dan D-08 Stok RFID Habis, serta Urutan Pemeriksaan | FE+BE | 21 | 240, 241, 244, 262 |
| TC-FA-TAG-E2E-053-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-2 | Overlay Scan Replace TAG: Dialog Blok D-08 untuk Tag Combined NFC dan QR Saat Stok Habis | FE+BE | 5 | 1456 |
| TC-FA-TAG-E2E-054-overlay-scan-tag-status-dilarang-tidak-dikenal-dan-milik-bagian-1 | Overlay Scan Replace TAG: Dialog Blok D-07 untuk Tag Berstatus Tidak Paired | FE+BE | 34 | 246, 247, 248, 249, 250, 251, 252 |
| TC-FA-TAG-E2E-055-overlay-scan-tag-status-dilarang-tidak-dikenal-dan-milik-bagian-2 | Overlay Scan Replace TAG: Pesan Inline untuk Tag Tidak Dikenal dan Tag Milik Produk Lain | FE+BE | 27 | 253, 254, 255, 256, 264 |
| TC-FA-TAG-E2E-056-overlay-scan-pemblokiran-dialog-d-01-d-06-d-08-dan-urutan-bagian-3 | Overlay Scan Replace TAG: Dialog Blok D-06 Aset di Luar Scope dan Group Read-Only | FE+BE | 16 | 242, 243, 261 |
| TC-FA-TAG-E2E-058-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-1 | Dialog Replace TAG: Screening Header, Footer, Blok Info Aset, dan Status Aset (Bagian 1) | FE+BE | 38 | 266, 267, 268, 269, 270 |
| TC-FA-TAG-E2E-059-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-2 | Dialog Replace TAG: Screening Bagian TAG to replace, Replacement TAG, dan Slot per Tipe Tag (Bagian 2) | FE+BE | 30 | 271, 272, 273, 274, 275 |
| TC-FA-TAG-E2E-060-dialog-replace-tag-screening-blok-info-dan-bagian-tag-to-bagian-3 | Dialog Replace TAG: Keselarasan Layout Kolom, Lebar Kolom Scan, dan Jarak Divider | FE+BE | 10 | 1449 |
| TC-FA-TAG-E2E-061-dialog-replace-tag-pemilihan-tag-centang-dan-slot-pengganti-bagian-1 | Dialog Replace TAG: Pemilihan Tag (Centang) dan Slot Pengganti Mengikuti Pilihan (Bagian 1) | FE+BE | 32 | 276, 277, 278, 279, 280 |
| TC-FA-TAG-E2E-062-dialog-replace-tag-pemilihan-tag-centang-dan-slot-pengganti-bagian-2 | Dialog Replace TAG: Tag Non-standard Tidak Tercentang Otomatis dan Slot Tipe Wajib yang Masih Kosong (Bagian 2) | FE+BE | 18 | 281, 282 |
| TC-FA-TAG-E2E-063-dialog-replace-tag-scan-current-tag-badge-dan-penolakan-bagian-1 | Dialog Replace TAG: Scan Current TAG, Badge Scanned atau Not scanned, dan Penolakan Tag Lama Salah (Bagian 1) | FE+BE | 33 | 283, 284, 285, 286, 287 |
| TC-FA-TAG-E2E-064-dialog-replace-tag-scan-current-tag-badge-dan-penolakan-bagian-2 | Dialog Replace TAG: Scan Current TAG, Penolakan Tag Milik Aset Lain, Tidak Paired, Tidak Dikenal, dan Produk Lain (Bagian 2) | FE+BE | 38 | 288, 289, 290, 291, 292 |
| TC-FA-TAG-E2E-065-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-1 | Dialog Replace TAG: Scan Tag Pengganti, Verified, dan Penolakan Status Paired, Reserved, Retired, Damaged/Missing, Waiting for Approval (Bagian 1) | FE+BE | 33 | 293, 294, 295, 296, 297 |
| TC-FA-TAG-E2E-066-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-2 | Dialog Replace TAG: Scan Tag Pengganti, Penolakan Waiting for Approval, Tidak Dikenal, QR Tidak Pernah Dicetak, dan User TAG (Bagian 2) | FE+BE | 36 | 298, 299, 300, 301, 302 |
| TC-FA-TAG-E2E-067-dialog-replace-tag-scan-tag-pengganti-penolakan-v-07-v-08-v-23-bagian-3 | Dialog Replace TAG: Scan Tag Pengganti, Penolakan Tidak Berlaku di Client, Tipe Tidak Sesuai, Tag Sama, dan Produk Supply Asset (Bagian 3) | FE+BE | 37 | 303, 304, 305, 306, 1461 |
| TC-FA-TAG-E2E-068-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-1 | Dialog Replace TAG: Submit Normal, Submit Tanpa Tag Pengganti (V-28), dan Cancel Dialog Kosong atau Terisi (Bagian 1) | FE+BE | 30 | 309, 310, 311, 312 |
| TC-FA-TAG-E2E-069-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-2 | Dialog Replace TAG: Konfirmasi Discard (D-09) lewat Cancel, Ikon Close, dan Klik Backdrop (Bagian 2) | FE+BE | 27 | 313, 314, 315, 316 |
| TC-FA-TAG-E2E-070-dialog-replace-tag-submit-cancel-backdrop-dan-aset-non-tag-bagian-3 | Dialog Replace TAG: Esc pada Konfirmasi D-09, Submit Disabled Tanpa Tag Tercentang, dan Aset Non-TAG (Bagian 3) | FE+BE | 28 | 317, 1352, 1441 |
| TC-FA-TAG-E2E-071-replace-penutupan-laporan-terbuka-dan-alur-ujung-ke-ujung-bagian-1 | Replace: Tag Berlaporan Terbuka Wajib Ikut Diganti, Penutupan Laporan Tag QR, dan Alur Ujung ke Ujung Admin Aset | FE+BE | 37 | 324, 325, 326 |
| TC-FA-TAG-E2E-072-replace-penutupan-laporan-terbuka-dan-alur-ujung-ke-ujung-bagian-2 | Replace: Laporan Terbuka pada Tag yang Dilepas Ditutup Replaced dan Status Tag Reported Dicabut | FE+BE | 22 | 340, 1378 |
| TC-FA-TAG-E2E-073-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-1 | Replace: Nasib Tag Lama Tidak Dipindai (Damaged/Missing), Tag NFC Not scanned, Non-standard QR Keluar, dan Non-standard RFID Available (Bagian 1) | FE+BE | 32 | 332, 333, 334, 335 |
| TC-FA-TAG-E2E-074-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-2 | Replace: Nasib Tag Lama pada Aset Non-TAG, Dua Tag Dilepas Sekaligus, dan Aset Multi-Tag (Bagian 2) | FE+BE | 32 | 336, 337, 338, 339 |
| TC-FA-TAG-E2E-075-replace-efek-pada-perhitungan-non-standard-discard-dan-stok-bagian-1 | Replace: Efek pada Hitungan Non-standard, Aksi Grup Replace non-standard TAGs, dan Jumlah Slot per Tag Dicentang (Bagian 1) | FE+BE | 41 | 327, 328, 329, 341 |
| TC-FA-TAG-E2E-076-replace-efek-pada-perhitungan-non-standard-discard-dan-stok-bagian-2 | Replace: Discard Penggantian Membiarkan Aset Tetap Reported dan Non-standard, Stok Tetap Available, dan Tanpa Dokumen Approval (Bagian 2) | FE+BE | 29 | 342, 343, 344 |
| TC-FA-TAG-E2E-077-replace-tag-pengganti-to-be-returned-dan-status-aset-transaksi-bagian-1 | Replace: Tag Pengganti To be Returned Diterima bila Return Group Berhak Update dan Ditolak bila Hanya Read atau di Luar Scope (Bagian 1) | FE+BE | 29 | 345, 346, 347 |
| TC-FA-TAG-E2E-078-replace-tag-pengganti-to-be-returned-dan-status-aset-transaksi-bagian-2 | Replace: Aset Berstatus Menunggu Serah Terima atau Approval, In Transfer Process, Sesi Opname Berjalan, dan Under Maintenance Berjalan Normal (Bagian 2) | FE+BE | 12 | 350, 351, 352, 353 |
| TC-FA-TAG-E2E-079-replace-tag-pengganti-to-be-returned-dan-status-aset-transaksi-bagian-3 | Replace: Aset Berstatus Permanently Missing, Assigned, dan Borrowed Berjalan Normal (Bagian 3) | FE+BE | 12 | 354, 348, 349 |
| TC-FA-TAG-E2E-080-replace-dua-tag-non-standard-dan-slot-tipe-wajib-kosong | Replace: Dua Tag Non-standard dengan Satu atau Dua Tipe Wajib Kosong, Slot Mengikuti Urutan TAG Type Asset Name | FE+BE | 36 | 1478, 1479 |
| TC-FA-TAG-E2E-081-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-1 | Replace dengan Tag Combined: Penolakan pada Replace Satu Slot (V-25), Pindai Sebagian Slot, dan Tag Tunggal Bertabrakan (V-26) | FE+BE | 34 | 356, 359, 360 |
| TC-FA-TAG-E2E-082-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-2 | Replace dengan Tag Combined: Pindai Mengisi Semua Slot Komponen dan Penolakan Pola Tidak Cocok, Komponen Tidak Dikenal, Reserved, User TAG, atau Tidak Berlaku | FE+BE | 35 | 357, 358, 361, 362, 363, 364, 355 |
| TC-FA-TAG-E2E-083-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-bagian-3 | Replace dengan Tag Combined: Caption Tag Sama, Scan Current TAG, dan Pilih Komponen | FE+BE | 20 | 366, 369, 370 |
| TC-FA-TAG-E2E-084-replace-satu-tag-non-standard-dengan-dua-tipe-wajib-kosong | Replace: Satu Tag Non-standard dengan Dua Tipe Wajib Kosong Hanya Mendapat Satu Slot | FE+BE | 10 | 1483 |
| TC-FA-TAG-E2E-085-replace-nasib-tag-lama-available-damaged-missing-dan-keluar-bagian-3 | Tag QR yang Dilaporkan Tidak Pernah Masuk Tab To Be Returned | FE+BE | 13 | 1379 |
| TC-FA-TAG-E2E-086-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-1 | Replace TAG: Tooltip Disabled Row Action dan Bulk Batch Replace (Bagian 1) | FE+BE | 38 | 330, 331, 371, 372, 373, 374, 380 |
| TC-FA-TAG-E2E-087-replace-tooltip-disabled-dan-hidden-row-action-dan-bulk-bagian-2 | Replace TAG: Tooltip Disabled dan Hidden Bulk serta Aksi Grup (Bagian 2) | FE+BE | 15 | 381, 382, 384 |
| TC-FA-TAG-E2E-088-replace-entry-row-action-bulk-satu-aset-aksi-grup-dan-tab-tbr | Replace TAG: Pintu Masuk Row Action, Bulk Satu Aset, Aksi Grup, Tab To Be Returned, dan Overlay Scan NFC | FE+BE | 38 | 377, 378, 379, 385, 386, 387 |
| TC-FA-TAG-E2E-089-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-1 | Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 1) | FE+BE | 34 | 388, 389, 390, 391 |
| TC-FA-TAG-E2E-090-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-2 | Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 2) | FE+BE | 35 | 392, 393, 394 |
| TC-FA-TAG-E2E-091-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-3 | Batch Replace TAG: Header Sesi, Submit & next, Skip, dan Ringkasan Akhir (Bagian 3) | FE+BE | 25 | 395, 396, 397 |
| TC-FA-TAG-E2E-092-batch-replace-sesi-header-submit-next-skip-ringkasan-dan-retry-bagian-4 | Batch Replace TAG: Ikon Close pada Aset Terbuka dan Discard (Bagian 4) | FE+BE | 34 | 398, 399, 1473 |
| TC-FA-TAG-E2E-093-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-1 | Batch Replace TAG: Pilihan Tag Awal, Scan Current TAG Opsional, dan Stok Kurang (Bagian 1) | FE+BE | 35 | 400, 401, 402, 403 |
| TC-FA-TAG-E2E-094-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-2 | Batch Replace TAG: Stok Habis di Tengah Sesi dan Konflik D-03 serta D-04 (Bagian 2) | FE+BE | 37 | 404, 408, 409 |
| TC-FA-TAG-E2E-095-batch-replace-scan-opsional-stok-konflik-d-03-d-04-dan-bagian-3 | Batch Replace TAG: Tag Pengganti yang Sudah Dipakai Aset Sebelumnya Ditolak (Bagian 3) | FE+BE | 16 | 410, 1382 |
| TC-FA-TAG-E2E-096-pair-tag-screening-dialog-dan-slot-per-tipe-wajib | Pair TAG: Screening Dialog dan Slot per Tipe Wajib | FE+BE | 25 | 411, 412, 413, 414 |
| TC-FA-TAG-E2E-097-pair-tag-submit-berhasil-dan-validasi-submit-v-37 | Pair TAG: Validasi Submit V-37 dan Submit Berhasil | FE+BE | 26 | 415, 416, 417, 418 |
| TC-FA-TAG-E2E-098-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-1 | Pair TAG: Penolakan Scan Menurut Status Tag V-07 (Bagian 1) | FE+BE | 19 | 419, 420, 421, 422, 423 |
| TC-FA-TAG-E2E-099-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-2 | Pair TAG: Penolakan Scan Menurut Tipe dan Registri serta Kode QR Hasil Cetak (Bagian 2) | FE+BE | 26 | 424, 426, 427, 428, 429 |
| TC-FA-TAG-E2E-100-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-3 | Pair TAG: Tag Tidak Berlaku, Konflik D-03, dan Tag To be Returned menurut Return Group (Bagian 3) | FE+BE | 33 | 430, 431, 432, 433, 434 |
| TC-FA-TAG-E2E-101-pair-tag-scan-penolakan-status-tipe-dan-registri-bagian-4 | Pair TAG: Penolakan Pindai Ulang V-09 dan Tag Milik Supply Asset (Bagian 4) | FE+BE | 26 | 1453, 1454, 1462 |
| TC-FA-TAG-E2E-102-pair-tag-combined-slot-dan-penolakan-bagian-1 | Pair TAG: Tag Combined Mengisi Slot dan Penolakan (Bagian 1) | FE+BE | 36 | 435, 436, 437, 438, 439 |
| TC-FA-TAG-E2E-103-pair-tag-combined-slot-dan-penolakan-bagian-2 | Pair TAG: Tag Combined Sebagian, Konflik dengan Tag Tunggal, Pindai Ulang, dan Komponen Gagal (Bagian 2) | FE+BE | 33 | 440, 441, 442, 443 |
| TC-FA-TAG-E2E-104-pair-tag-cancel-ikon-close-backdrop-dan-esc-bagian-1 | Pair TAG: Cancel dan Konfirmasi Discard Pairing D-11 (Bagian 1) | FE+BE | 18 | 444, 445, 446, 447 |
| TC-FA-TAG-E2E-105-pair-tag-cancel-ikon-close-backdrop-dan-esc-bagian-2 | Pair TAG: Ikon Close, Klik Backdrop, dan Esc pada Konfirmasi D-11 (Bagian 2) | FE+BE | 17 | 448, 1439, 1442 |
| TC-FA-TAG-E2E-106-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-1 | Pair TAG: Tooltip Disabled Row Action menurut Reader, Status Aset, dan Stok (Bagian 1) | FE+BE | 32 | 449, 450, 451, 452 |
| TC-FA-TAG-E2E-107-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-2 | Pair TAG: Bulk Pair TAG Disabled, Hidden, dan Satu Aset (Bagian 2) | FE+BE | 34 | 454, 455, 456, 457, 458 |
| TC-FA-TAG-E2E-108-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-3 | Pair TAG: Urutan Prioritas Tooltip Disabled Reader, Status Aset, dan Stok (Bagian 3) | FE+BE | 34 | 1455, 1491, 1492, 1493 |
| TC-FA-TAG-E2E-109-pair-tag-tooltip-disabled-row-action-dan-bulk-urutan-bagian-4 | Pair TAG: Bulk Pair TAG Status Aset Didahulukan atas Stok (Bagian 4) | FE+BE | 8 | 1494 |
| TC-FA-TAG-E2E-110-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-1 | Sesi Pair TAG Beberapa Aset: Header, Footer, Submit & next, dan Skip (Bagian 1) | FE+BE | 21 | 459, 460, 461 |
| TC-FA-TAG-E2E-111-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-2 | Sesi Pair TAG Beberapa Aset: Ringkasan Akhir Done, Skipped, dan Tombol Retry (Bagian 2) | FE+BE | 27 | 462, 463 |
| TC-FA-TAG-E2E-112-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-3 | Sesi Pair TAG Beberapa Aset: Toast T-20 Bentuk Jamak dan Tunggal pada Close (Bagian 3) | FE+BE | 22 | 464, 465 |
| TC-FA-TAG-E2E-113-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-4 | Sesi Pair TAG Beberapa Aset: Retry skipped, Konflik D-03, dan Ikon Close Tanpa Kode (Bagian 4) | FE+BE | 35 | 466, 469, 470 |
| TC-FA-TAG-E2E-114-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-5 | Sesi Pair TAG Beberapa Aset: Ikon Close Terisi dan Kode yang Sudah Dipakai Ditolak (Bagian 5) | FE+BE | 26 | 471, 472, 1383 |
| TC-FA-TAG-E2E-115-sesi-pair-tag-beberapa-aset-submit-next-skip-ringkasan-dan-bagian-6 | Sesi Pair TAG Beberapa Aset: Tag Combined Dipindai Ulang dan Semua Aset Skipped (Bagian 6) | FE+BE | 29 | 1445, 1446, 1487 |
| TC-FA-TAG-E2E-116-pair-tag-row-action-enabled-bila-sebagian-tipe-stok-0 | Pair TAG: Row Action Tetap Enabled bila Hanya Sebagian Tipe Stok 0 | FE+BE | 8 | 453 |
| TC-FA-TAG-E2E-118-print-qr-screening-tombol-dialog-dan-preview-quantity-start-bagian-1 | Print QR: screening tombol toolbar, Dialog, dan Preview Quantity serta Start position (bagian 1) | FE+BE | 31 | 473, 474, 475, 476, 477, 478 |
| TC-FA-TAG-E2E-119-print-qr-screening-tombol-dialog-dan-preview-quantity-start-bagian-2 | Print QR: Preview berubah langsung saat Quantity atau Start position diubah dan batas 100 | FE+BE | 18 | 479, 480, 481 |
| TC-FA-TAG-E2E-120-print-qr-validasi-quantity-v-39-dan-batas-bagian-1 | Print QR: validasi Quantity V-39 untuk nilai kosong, 0, 101, desimal, dan negatif | FE+BE | 36 | 482, 483, 484, 485, 486 |
| TC-FA-TAG-E2E-121-print-qr-validasi-quantity-v-39-dan-batas-bagian-2 | Print QR: Quantity tidak menerima huruf, pulih setelah invalid, dan batas bawah 1 | FE+BE | 16 | 487, 488, 489 |
| TC-FA-TAG-E2E-122-print-qr-start-print-data-tersimpan-dialog-cetak-browser-dan-bagian-1 | Print QR: Start Print menyimpan data, membuka dialog cetak browser, dan menampilkan toast | FE+BE | 32 | 490, 491, 492, 493 |
| TC-FA-TAG-E2E-123-print-qr-start-print-data-tersimpan-dialog-cetak-browser-dan-bagian-2 | Print QR: membatalkan dialog cetak browser tidak membatalkan kode QR yang sudah dibuat | FE+BE | 18 | 498 |
| TC-FA-TAG-E2E-124-print-qr-cancel-ikon-close-backdrop-dan-nilai-bawaan | Print QR: Cancel, ikon close, backdrop, dan nilai bawaan saat dibuka ulang | FE+BE | 19 | 499, 500, 501, 502 |
| TC-FA-TAG-E2E-125-print-qr-dari-slot-qr-dialog-replace-dan-pair-lapisan-dan-bagian-1 | Print QR dari slot QR Dialog Replace TAG: lapisan di atas dialog, backdrop, Start Print, dan penutupan | FE+BE | 26 | 503, 505, 506 |
| TC-FA-TAG-E2E-126-print-qr-dari-slot-qr-dialog-replace-dan-pair-lapisan-dan-bagian-2 | Print QR: Esc menutup lapisan paling atas dan kode QR hasil cetak diterima di Dialog Pair TAG | FE+BE | 21 | 507, 1443 |
| TC-FA-TAG-E2E-127-receive-tag-screening-dialog-dan-penambahan-daftar-sesi | Receive TAG: screening Dialog dan penambahan Tag ke daftar sesi | FE+BE | 33 | 531, 532, 533, 534, 535 |
| TC-FA-TAG-E2E-128-receive-tag-berhasil-satu-dua-tag-dan-tabel-dimuat-ulang | Receive TAG: berhasil untuk satu dan dua Tag, dan tabel dimuat ulang dengan Search tetap | FE+BE | 27 | 536, 537, 538 |
| TC-FA-TAG-E2E-129-receive-tag-cancel-backdrop-ikon-close-esc-dan-receive-disabled-bagian-1 | Receive TAG: Cancel, ikon close, backdrop, dan Receive Disabled saat daftar kosong | FE+BE | 28 | 539, 540, 541, 542, 1495 |
| TC-FA-TAG-E2E-130-receive-tag-cancel-backdrop-ikon-close-esc-dan-receive-disabled-bagian-2 | Receive TAG: Esc pada dialog berisi Tag terpindai menutup tanpa konfirmasi dan membuang sesi | FE+BE | 10 | 1496 |
| TC-FA-TAG-E2E-131-receive-tag-scan-penolakan-tidak-dikenal-status-duplikat-scope-bagian-1 | Receive TAG: penolakan scan untuk kode tidak dikenal, status bukan To Be Returned, duplikat, dan scope group | FE+BE | 28 | 543, 544, 545, 546, 547, 548 |
| TC-FA-TAG-E2E-132-receive-tag-scan-penolakan-tidak-dikenal-status-duplikat-scope-bagian-2 | Receive TAG: penolakan Tag QR belum terpasang, Supply Asset, dan User TAG, lalu Tag valid tetap diproses | FE+BE | 21 | 549, 1444, 1474, 1475 |
| TC-FA-TAG-E2E-133-receive-tag-konflik-sesi-lain-tidak-dapat-dibatalkan-dan-hasil-bagian-1 | Receive TAG: Tag sudah diterima atau dipasang pengguna lain sebelum [Receive] | FE+BE | 26 | 567, 568 |
| TC-FA-TAG-E2E-134-receive-tag-konflik-sesi-lain-tidak-dapat-dibatalkan-dan-hasil-bagian-2 | Receive TAG: hasil parsial dan semua Tag gagal karena Tag diambil pengguna lain | FE+BE | 32 | 1460, 1469 |
| TC-FA-TAG-E2E-135-receive-manually-menu-screening-dan-bulk | Receive Manually: menu aksi baris, screening Dialog, dan Bulk Action | FE+BE | 35 | 573, 574, 575, 576, 577 |
| TC-FA-TAG-E2E-136-receive-manually-validasi-note-berhasil-dan-event-log | Receive Manually: validasi Note, berhasil satu dan dua Tag, dan Note tidak tampil di Event Log | FE+BE | 35 | 578, 579, 580, 581 |
| TC-FA-TAG-E2E-137-receive-manually-cancel-dan-unsaved-changes-bagian-1 | Receive Manually: Cancel kosong, backdrop, dan Unsaved Changes lewat Cancel, ikon close, dan Esc | FE+BE | 23 | 582, 586, 588, 589, 590 |
| TC-FA-TAG-E2E-138-receive-manually-cancel-dan-unsaved-changes-bagian-2 | Receive Manually: Cancel dan Leave pada Unsaved Changes, serta ikon close pada dialog belum terisi | FE+BE | 25 | 591, 592, 593, 594 |
| TC-FA-TAG-E2E-139-receive-manually-cancel-dan-unsaved-changes-bagian-3 | Receive Manually: muat ulang halaman memicu konfirmasi bawaan browser dan dialog terisi Note dianggap terisi | FE+BE | 11 | 595, 596 |
| TC-FA-TAG-E2E-140-print-qr-dari-slot-qr-dialog-pair-tag-menutup-lapisan-print-qr | Print QR dari slot QR Dialog Pair TAG: lapisan di atas dialog dan penutupan mengembalikan isian | FE+BE | 16 | 504 |
| TC-FA-TAG-E2E-141-receive-tag-pengembalian-tidak-dapat-dibatalkan-dan-hasil-receive-manually | Receive TAG: pengembalian tidak dapat dibatalkan, dan hasil Receive TAG berbeda dari Receive Manually | FE+BE | 30 | 569, 1380 |
| TC-FA-TAG-E2E-142-report-tag-screening-dialog-dan-opsi-tag-bagian-1 | Report TAG: Screening Dialog dan Opsi Tag (Bagian 1) | FE+BE | 34 | 598, 599, 600, 601, 602, 603 |
| TC-FA-TAG-E2E-143-report-tag-screening-dialog-dan-opsi-tag-bagian-2 | Report TAG: Menu Aksi pada Aset dengan Laporan Terbuka Sebagian (Bagian 2) | FE+BE | 4 | 604 |
| TC-FA-TAG-E2E-144-report-tag-validasi-submit-report-type-note-dan-tag | Report TAG: Validasi Submit Report Type, Note, dan Tag | FE+BE | 30 | 605, 606, 607, 608 |
| TC-FA-TAG-E2E-145-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-1 | Report TAG: Submit Berhasil per Report Type dan Dua Tag (Bagian 1) | FE+BE | 28 | 609, 610, 611, 612 |
| TC-FA-TAG-E2E-146-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-2 | Report TAG: Dampak Laporan pada Status Aset, Registri Global, dan Kartu Reported (Bagian 2) | FE+BE | 29 | 613, 614, 615, 616 |
| TC-FA-TAG-E2E-147-report-tag-submit-berhasil-per-report-type-dan-dampaknya-bagian-3 | Report TAG: Laporan Konflik, Dialog dari Modul Borrow, dan Changelog (Bagian 3) | FE+BE | 33 | 618, 620, 621, 1377, 1459 |
| TC-FA-TAG-E2E-148-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-1 | Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1) | FE+BE | 23 | 622, 623, 624, 625, 626 |
| TC-FA-TAG-E2E-149-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-2 | Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2) | FE+BE | 34 | 627, 628, 629, 630, 631, 632 |
| TC-FA-TAG-E2E-150-report-tag-unsaved-changes-dan-penutupan-dialog-bagian-3 | Report TAG: Esc pada Unsaved Changes dan Klik Backdrop (Bagian 3) | FE+BE | 14 | 633, 634 |
| TC-FA-TAG-E2E-151-decline-report-screening-dan-validasi-bagian-1 | Decline Report: Screening Dialog dan Validasi Reason (Bagian 1) | FE+BE | 29 | 636, 637, 638, 639 |
| TC-FA-TAG-E2E-152-decline-report-screening-dan-validasi-bagian-2 | Decline Report: Validasi Tag dan Label Opsi Tag Bertipe Sama (Bagian 2) | FE+BE | 18 | 640, 1485 |
| TC-FA-TAG-E2E-153-decline-report-submit-berhasil-dan-konflik-pengguna-lain-bagian-1 | Decline Report: Submit Berhasil (Bagian 1) | FE+BE | 25 | 641, 642, 643 |
| TC-FA-TAG-E2E-154-decline-report-submit-berhasil-dan-konflik-pengguna-lain-bagian-2 | Decline Report: Konflik dengan Pengguna Lain (Bagian 2) | FE+BE | 25 | 1457, 1470 |
| TC-FA-TAG-E2E-155-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-1 | Decline Report: Backdrop dan Unsaved Changes (Bagian 1) | FE+BE | 21 | 647, 648, 649, 650 |
| TC-FA-TAG-E2E-156-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-2 | Decline Report: Unsaved Changes dan Penutupan Dialog (Bagian 2) | FE+BE | 24 | 651, 652, 653, 654 |
| TC-FA-TAG-E2E-157-decline-report-backdrop-unsaved-changes-dan-penutupan-bagian-3 | Decline Report: Refresh dan Dialog Terisi Sebagian (Bagian 3) | FE+BE | 22 | 655, 656, 657 |
| TC-FA-TAG-E2E-158-cancel-report-tag-screening-dan-validasi | Cancel Report TAG: Screening Dialog dan Validasi | FE+BE | 31 | 658, 659, 660, 661, 1486 |
| TC-FA-TAG-E2E-159-cancel-report-tag-submit-berhasil-keep-report-dan-modul-borrow-bagian-1 | Cancel Report TAG: Submit Berhasil, Keep Report, dan Laporan Ulang (Bagian 1) | FE+BE | 28 | 662, 663, 664, 665, 666 |
| TC-FA-TAG-E2E-160-cancel-report-tag-submit-berhasil-keep-report-dan-modul-borrow-bagian-2 | Cancel Report TAG: Keep Report, Konflik Pengguna Lain, dan Dialog Borrow (Bagian 2) | FE+BE | 35 | 667, 670, 1440, 1458, 1471 |
| TC-FA-TAG-E2E-161-cancel-report-tag-unsaved-changes-dan-penutupan-bagian-1 | Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 1) | FE+BE | 23 | 671, 672, 673, 674, 675 |
| TC-FA-TAG-E2E-162-cancel-report-tag-unsaved-changes-dan-penutupan-bagian-2 | Cancel Report TAG: Unsaved Changes dan Penutupan Dialog (Bagian 2) | FE+BE | 24 | 676, 677, 678, 679 |
| TC-FA-TAG-E2E-163-batas-karakter-note-dialog-report-tag | Batas Karakter Note Dialog Report TAG | FE+BE | 31 | 1384, 1385, 1386, 1387 |
| TC-FA-TAG-E2E-164-batas-karakter-note-dialog-receive-manually | Batas Karakter Note Dialog Receive Manually | FE+BE | 35 | 1388, 1389, 1390, 1391 |
| TC-FA-TAG-E2E-165-batas-karakter-reason-dialog-decline-report-bagian-1 | Batas Karakter Reason Dialog Decline Report (Bagian 1) | FE+BE | 27 | 1392, 1393, 1394 |
| TC-FA-TAG-E2E-166-batas-karakter-reason-dialog-decline-report-bagian-2 | Batas Karakter Reason Dialog Decline Report (Bagian 2) | FE+BE | 10 | 1395 |
| TC-FA-TAG-E2E-167-batas-karakter-reason-dialog-cancel-report-tag | Batas Karakter Reason Dialog Cancel Report TAG | FE+BE | 26 | 1396, 1397, 1398, 1399 |
| TC-FA-TAG-E2E-168-report-tag-konflik-dua-tag-ketika-satu-tag-sudah-dilaporkan-pengguna-lain | Report TAG: Konflik Dua Tag Ketika Satu Tag Sudah Dilaporkan Pengguna Lain | FE+BE | 13 | 1472 |
| TC-FA-TAG-E2E-169-decline-report-tag-declined-dapat-dilaporkan-ulang | Decline Report: Tag Declined Dapat Dilaporkan Ulang | FE+BE | 13 | 644 |
| TC-FA-TAG-E2E-170-search-toolbar-halaman-input-enter-spasi-dan-popup-detail-bagian-1 | Search Toolbar Halaman: Input, Enter, dan Spasi (Bagian 1) | FE+BE | 24 | 680, 681, 682, 683, 684, 685 |
| TC-FA-TAG-E2E-171-search-toolbar-halaman-input-enter-spasi-dan-popup-detail-bagian-2 | Search Toolbar Halaman: Karakter Khusus, Reset, Halaman 1, dan Popup Detail (Bagian 2) | FE+BE | 30 | 686, 687, 688, 689, 690, 691 |
| TC-FA-TAG-E2E-172-filter-panel-toolbar-halaman-apply-draft-dan-kombinasi-bagian-1 | Filter Panel Toolbar Halaman: Buka, Screening, Apply, dan Clear Field (Bagian 1) | FE+BE | 31 | 692, 693, 694, 695, 696 |
| TC-FA-TAG-E2E-173-filter-panel-toolbar-halaman-apply-draft-dan-kombinasi-bagian-2 | Filter Panel Toolbar Halaman: Halaman 1 dan Kombinasi Search, Filter, Sort (Bagian 2) | FE+BE | 29 | 698, 699, 700, 701 |
| TC-FA-TAG-E2E-174-tabel-grup-sort-tiga-tahap-per-kolom-bagian-1 | Tabel Grup: Sort Tiga Tahap Kolom Asset Name, Group, TAG Type, Total Assets, dan Reported (Bagian 1) | FE+BE | 30 | 702, 703, 704, 705, 706 |
| TC-FA-TAG-E2E-175-tabel-grup-sort-tiga-tahap-per-kolom-bagian-2 | Tabel Grup: Sort Kolom Non-standard dan Not Paired Yet, Urutan Bawaan, dan Pindah Kolom (Bagian 2) | FE+BE | 25 | 707, 708, 709, 710, 711 |
| TC-FA-TAG-E2E-176-tabel-grup-search-per-kolom | Tabel Grup: Search per Kolom | FE+BE | 25 | 712, 713, 714, 715, 716, 717, 718, 719 |
| TC-FA-TAG-E2E-177-tabel-grup-filter-per-kolom-dan-tree-picker-group-bagian-1 | Tabel Grup: Filter per Kolom Asset Name, Total Assets, Reported, Non-standard, dan Not Paired Yet (Bagian 1) | FE+BE | 34 | 720, 721, 722, 723, 724, 725, 726 |
| TC-FA-TAG-E2E-178-tabel-grup-filter-per-kolom-dan-tree-picker-group-bagian-2 | Tabel Grup: Tree Picker Group dan Filter pada Kolom Tersembunyi (Bagian 2) | FE+BE | 29 | 727, 728, 729, 730 |
| TC-FA-TAG-E2E-179-tabel-grup-format-sel-badge-ikon-dan-severity-bagian-1 | Tabel Grup: Format Sel, Badge, Ikon, dan Severity (Bagian 1) | FE+BE | 24 | 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741 |
| TC-FA-TAG-E2E-180-tabel-grup-format-sel-badge-ikon-dan-severity-bagian-2 | Tabel Grup: Total Assets Menyertakan Aset Not Paired Yet (Bagian 2) | FE+BE | 6 | 742 |
| TC-FA-TAG-E2E-181-tabel-grup-column-visibility-per-kolom-bagian-1 | Tabel Grup: Column Visibility per Kolom (Bagian 1) | FE+BE | 32 | 743, 744, 745, 746, 747 |
| TC-FA-TAG-E2E-182-tabel-grup-column-visibility-per-kolom-bagian-2 | Tabel Grup: Column Visibility per Kolom (Bagian 2) | FE+BE | 31 | 748, 749, 750, 751 |
| TC-FA-TAG-E2E-183-tabel-grup-popup-setup-column-save-reset-reorder-dan-pin-bagian-1 | Tabel Grup: Popup Setup Column, Screening, Pratinjau, Save, dan Batal (Bagian 1) | FE+BE | 26 | 752, 753, 754, 755, 756 |
| TC-FA-TAG-E2E-184-tabel-grup-popup-setup-column-save-reset-reorder-dan-pin-bagian-2 | Tabel Grup: Popup Setup Column, Reorder dan Pin (Bagian 2) | FE+BE | 13 | 758, 759 |
| TC-FA-TAG-E2E-185-popup-setup-column-t-tag-02-screening-save-reset-reorder-dan-bagian-1 | Popup Setup Column T-TAG-02: Screening, Pratinjau, Save, dan Batal (Bagian 1) | FE+BE | 28 | 1414, 1415, 1416, 1417 |
| TC-FA-TAG-E2E-186-popup-setup-column-t-tag-02-screening-save-reset-reorder-dan-bagian-2 | Popup Setup Column T-TAG-02: Esc, Reset, Reorder, dan Pin (Bagian 2) | FE+BE | 29 | 1418, 1419, 1420, 1421 |
| TC-FA-TAG-E2E-187-popup-setup-column-tab-to-be-returned-dan-modal-event-log-bagian-1 | Popup Setup Column Tab To Be Returned dan Modal Event Log: Screening, Reorder, dan Pin (Bagian 1) | FE+BE | 30 | 1422, 1423, 1424, 1425 |
| TC-FA-TAG-E2E-188-popup-setup-column-tab-to-be-returned-dan-modal-event-log-bagian-2 | Popup Setup Column Modal Event Log: Reset, Reorder, dan Pin (Bagian 2) | FE+BE | 21 | 1426, 1427, 1428 |
| TC-FA-TAG-E2E-189-popup-setup-column-modal-changelog-reorder-dan-pin-bagian-1 | Popup Setup Column Modal Changelog: Column Visibility, Save, Reset, dan Reorder (Bagian 1) | FE+BE | 35 | 971, 972, 973, 974, 1429 |
| TC-FA-TAG-E2E-190-popup-setup-column-modal-changelog-reorder-dan-pin-bagian-2 | Popup Setup Column Modal Changelog: Pin Kolom saat Scroll Horizontal (Bagian 2) | FE+BE | 9 | 1430 |
| TC-FA-TAG-E2E-191-filter-panel-toolbar-halaman-tutup-tanpa-apply-membuang-draft | Filter Panel Toolbar Halaman: Menutup Panel tanpa Apply Membuang Draft | FE+BE | 6 | 697 |
| TC-FA-TAG-E2E-192-tabel-grup-popup-setup-column-reset-to-default-dan-save | Tabel Grup: Reset to Default pada Popup Setup Column Baru Permanen setelah Save | FE+BE | 8 | 757 |
| TC-FA-TAG-E2E-193-t-tag-02-column-visibility-kolom-bawaan-bagian-1 | Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 1) | FE+BE | 30 | 760, 761, 762, 763, 764, 765 |
| TC-FA-TAG-E2E-194-t-tag-02-column-visibility-kolom-bawaan-bagian-2 | Tabel T-TAG-02: Column Visibility Kolom Bawaan (Bagian 2) | FE+BE | 32 | 766, 767, 768, 769, 770 |
| TC-FA-TAG-E2E-195-t-tag-02-column-visibility-kolom-curated-bagian-1 | Tabel T-TAG-02: Column Visibility Kolom Curated (Bagian 1) | FE+BE | 27 | 771, 772, 773, 774, 775 |
| TC-FA-TAG-E2E-196-t-tag-02-column-visibility-kolom-curated-bagian-2 | Tabel T-TAG-02: Column Visibility Kolom Curated dan Kolom Visible Terakhir (Bagian 2) | FE+BE | 24 | 776, 777, 778, 779 |
| TC-FA-TAG-E2E-197-t-tag-02-sort-tiga-tahap-per-kolom-bagian-1 | Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 1) | FE+BE | 27 | 780, 781, 782, 783 |
| TC-FA-TAG-E2E-198-t-tag-02-sort-tiga-tahap-per-kolom-bagian-2 | Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 2) | FE+BE | 22 | 784, 785, 786 |
| TC-FA-TAG-E2E-199-t-tag-02-sort-tiga-tahap-per-kolom-bagian-3 | Tabel T-TAG-02: Sort Tiga Tahap per Kolom (Bagian 3) | FE+BE | 24 | 787, 788, 789 |
| TC-FA-TAG-E2E-200-t-tag-02-sort-tiga-tahap-per-kolom-bagian-4 | Tabel T-TAG-02: Sort Tiga Tahap per Kolom dan Nilai Sama (Bagian 4) | FE+BE | 27 | 790, 791, 792, 793 |
| TC-FA-TAG-E2E-201-t-tag-02-sort-tiga-tahap-per-kolom-bagian-5 | Tabel T-TAG-02: Sort Kolom dengan Nilai Sama dan Pindah Target Sort (Bagian 5) | FE+BE | 19 | 794, 795, 796 |
| TC-FA-TAG-E2E-202-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-1 | Tabel T-TAG-02: Search per Kolom (Bagian 1) | FE+BE | 25 | 797, 798, 799, 800 |
| TC-FA-TAG-E2E-203-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-2 | Tabel T-TAG-02: Search per Kolom (Bagian 2) | FE+BE | 28 | 801, 802, 803, 804 |
| TC-FA-TAG-E2E-204-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-3 | Tabel T-TAG-02: Search per Kolom dan Nilai Sama (Bagian 3) | FE+BE | 31 | 805, 806, 807, 808, 809 |
| TC-FA-TAG-E2E-205-t-tag-02-search-per-kolom-dan-guard-kolom-tanggal-bagian-4 | Tabel T-TAG-02: Search Transactional Policy dan Guard Kolom Tanggal (Bagian 4) | FE+BE | 16 | 810, 811, 812, 813 |
| TC-FA-TAG-E2E-206-t-tag-02-filter-per-kolom-bagian-1 | Tabel T-TAG-02: Filter per Kolom (Bagian 1) | FE+BE | 30 | 814, 815, 816, 817 |
| TC-FA-TAG-E2E-207-t-tag-02-filter-per-kolom-bagian-2 | Tabel T-TAG-02: Filter per Kolom (Bagian 2) | FE+BE | 35 | 818, 819, 820, 821 |
| TC-FA-TAG-E2E-208-t-tag-02-filter-per-kolom-bagian-3 | Tabel T-TAG-02: Filter per Kolom (Bagian 3) | FE+BE | 35 | 822, 823, 824, 825 |
| TC-FA-TAG-E2E-209-t-tag-02-filter-per-kolom-bagian-4 | Tabel T-TAG-02: Filter TAG Type, Category, Opsi Kosong, dan Field Kolom Curated (Bagian 4) | FE+BE | 35 | 826, 827, 828, 829 |
| TC-FA-TAG-E2E-210-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-1 | Tabel T-TAG-02: Format Sel Name, TAG Code, dan Aset Not Paired Yet (Bagian 1) | FE+BE | 26 | 830, 831, 832, 833, 834, 835, 836 |
| TC-FA-TAG-E2E-211-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-2 | Tabel T-TAG-02: Format Sel Badge Brand, Model/Type, dan Group (Bagian 2) | FE+BE | 17 | 837, 838, 839, 840, 841, 842 |
| TC-FA-TAG-E2E-212-t-tag-02-format-sel-link-badge-hover-dan-pemotongan-bagian-3 | Tabel T-TAG-02: Format Sel Category, Measurement, Label, dan Status (Bagian 3) | FE+BE | 18 | 843, 844, 845, 846, 847, 848 |
| TC-FA-TAG-E2E-213-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-1 | Tabel T-TAG-02: Format Sel Status, Transactional Policy, Last Scanned, dan Asset Value (Bagian 1) | FE+BE | 28 | 849, 850, 851, 852, 853, 854 |
| TC-FA-TAG-E2E-214-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-2 | Tabel T-TAG-02: Nilai Aset, Garansi, dan Sel No access per Role (Bagian 2) | FE+BE | 33 | 855, 859, 856, 858, 857 |
| TC-FA-TAG-E2E-215-t-tag-02-format-sel-status-policy-nilai-aset-garansi-dan-no-bagian-3 | Tabel T-TAG-02: Warranty Expiry, Last Updated, Name Panjang, dan Scroll Horizontal (Bagian 3) | FE+BE | 25 | 860, 861, 862, 863, 864 |
| TC-FA-TAG-E2E-216-custom-field-kolom-curated-visibilitas-urutan-dan-hak-akses | Custom Field pada Tabel T-TAG-02: Kolom Curated, Visibilitas, Urutan, dan Hak Akses | FE+BE | 32 | 865, 866, 867, 868, 869, 871, 870 |
| TC-FA-TAG-E2E-217-custom-field-search-filter-sort-per-tipe-bagian-1 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 1) | FE+BE | 31 | 872, 873, 874, 875, 876 |
| TC-FA-TAG-E2E-218-custom-field-search-filter-sort-per-tipe-bagian-2 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 2) | FE+BE | 30 | 877, 878, 879, 880 |
| TC-FA-TAG-E2E-219-custom-field-search-filter-sort-per-tipe-bagian-3 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 3) | FE+BE | 31 | 881, 882, 883, 884, 885 |
| TC-FA-TAG-E2E-220-custom-field-search-filter-sort-per-tipe-bagian-4 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 4) | FE+BE | 30 | 886, 887, 888, 889 |
| TC-FA-TAG-E2E-221-custom-field-search-filter-sort-per-tipe-bagian-5 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 5) | FE+BE | 31 | 890, 891, 892, 893 |
| TC-FA-TAG-E2E-222-custom-field-search-filter-sort-per-tipe-bagian-6 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 6) | FE+BE | 33 | 894, 895, 896, 897 |
| TC-FA-TAG-E2E-223-custom-field-search-filter-sort-per-tipe-bagian-7 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 7) | FE+BE | 34 | 898, 899, 900, 901 |
| TC-FA-TAG-E2E-224-custom-field-search-filter-sort-per-tipe-bagian-8 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 8) | FE+BE | 25 | 902, 903, 904 |
| TC-FA-TAG-E2E-225-custom-field-search-filter-sort-per-tipe-bagian-9 | Custom Field pada Tabel T-TAG-02: Search, Filter, dan Sort per Tipe (Bagian 9) | FE+BE | 32 | 908, 909, 910, 911 |
| TC-FA-TAG-E2E-226-custom-field-search-filter-sort-per-tipe-bagian-10 | Custom Field pada Tabel T-TAG-02: Filter dan Sort Tipe Formula (Bagian 10) | FE+BE | 11 | 912, 913 |
| TC-FA-TAG-E2E-229-pagination-tabel-grup-page-size-navigasi-dan-input-halaman | Pagination Tabel Grup: Page Size, Navigasi Halaman, dan Input Nomor Halaman | FE+BE | 24 | 914, 915, 916, 917, 918, 919, 920, 921 |
| TC-FA-TAG-E2E-230-pagination-popup-detail-state-sort-dan-halaman | Pagination Popup Detail Assets: Pilihan Page Size, Navigasi, Input Tidak Valid, dan State Sort | FE+BE | 32 | 922, 923, 924, 1451, 1452 |
| TC-FA-TAG-E2E-231-state-tabel-refresh-tab-sidebar-dan-kembali | State Tabel Paired: Refresh F5, Pindah Tab, dan Klik Ulang Menu TAG di Sidebar | FE+BE | 30 | 925, 926, 927, 928 |
| TC-FA-TAG-E2E-232-reload-tabel-paired-setelah-submit-replace-batch-dan-pair | Reload Tabel Paired setelah Submit Replace, Batch Replace, dan Pair dengan State Dipertahankan | FE+BE | 35 | 977, 978, 979 |
| TC-FA-TAG-E2E-233-modal-changelog-screening-penutupan-tooltip-dan-read-only-bagian-1 | Modal Changelog Paired TAG: Screening, Penutupan, Tooltip Toolbar, dan Read-only (Bagian 1) | FE+BE | 34 | 931, 932, 933, 934, 935, 936, 937, 938, 968, 975 |
| TC-FA-TAG-E2E-234-modal-changelog-screening-penutupan-tooltip-dan-read-only-bagian-2 | Modal Changelog Paired TAG: Entri Replace Tampil di Changelog Asset Detail (Bagian 2) | FE+BE | 7 | 976 |
| TC-FA-TAG-E2E-235-modal-changelog-sort-tiga-tahap-per-kolom-bagian-1 | Modal Changelog Paired TAG: Urutan Bawaan dan Sort Tiga Tahap Kolom Date, Action, Name, Field (Bagian 1) | FE+BE | 27 | 941, 942, 943, 944, 945 |
| TC-FA-TAG-E2E-236-modal-changelog-sort-tiga-tahap-per-kolom-bagian-2 | Modal Changelog Paired TAG: Sort Tiga Tahap Kolom Old Value, New Value, dan Modified By (Bagian 2) | FE+BE | 20 | 946, 947, 948 |
| TC-FA-TAG-E2E-237-modal-changelog-search-per-kolom-bagian-1 | Modal Changelog Paired TAG: Search Tanpa Hasil dan Search per Kolom Action, Name, Field, Old Value, New Value, Modified By (Bagian 1) | FE+BE | 24 | 940, 949, 950, 951, 952, 953, 954 |
| TC-FA-TAG-E2E-238-modal-changelog-search-per-kolom-bagian-2 | Modal Changelog Paired TAG: Search Tidak Mencocokkan Kolom Date dan Tidak Peka Huruf Besar-Kecil (Bagian 2) | FE+BE | 9 | 955, 956 |
| TC-FA-TAG-E2E-239-modal-changelog-filter-per-kolom-dan-kombinasi-bagian-1 | Modal Changelog Paired TAG: Screening Filter Panel dan Filter per Kolom (Bagian 1) | FE+BE | 31 | 957, 958, 959, 960, 961, 962 |
| TC-FA-TAG-E2E-240-modal-changelog-filter-per-kolom-dan-kombinasi-bagian-2 | Modal Changelog Paired TAG: Kombinasi Multi-filter, Kombinasi Search, Filter, Sort, dan Pemulihan Baris (Bagian 2) | FE+BE | 24 | 963, 964, 965 |
| TC-FA-TAG-E2E-241-modal-changelog-pagination-format-isi-dan-download | Modal Changelog Paired TAG: Format Isi Baris Replace, Download CSV, dan Pagination | FE+BE | 20 | 966, 967, 969 |
| TC-FA-TAG-E2E-242-state-tabel-refresh-tab-sidebar-dan-kembali-bagian-2 | State Tabel Paired: Kembali dari Halaman Lain (Bagian 2) | FE+BE | 8 | 930 |
| TC-FA-TAG-E2E-244-tabel-to-be-returned-search-per-kolom-bagian-1 | Tabel To Be Returned: Search per Kolom, Pembukaan Input, dan Label Ikon Tipe (Bagian 1) | FE+BE | 23 | 980, 981, 982, 983, 984, 985, 986 |
| TC-FA-TAG-E2E-245-tabel-to-be-returned-search-per-kolom-bagian-2 | Tabel To Be Returned: Search Tidak Peka Huruf, Kolom Since dan Kolom Tersembunyi, serta Kembali ke Halaman 1 (Bagian 2) | FE+BE | 34 | 987, 988, 989, 990, 991 |
| TC-FA-TAG-E2E-246-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-1 | Tabel To Be Returned: Screening Filter Panel dan Filter TAG Type, Reason, serta Return Group (Bagian 1) | FE+BE | 34 | 992, 993, 994, 995, 996 |
| TC-FA-TAG-E2E-247-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-2 | Tabel To Be Returned: Cancel Tree Picker, Filter Current Holder, Since Inklusif, dan Kombinasi Filter (Bagian 2) | FE+BE | 31 | 997, 998, 999, 1000, 1001 |
| TC-FA-TAG-E2E-248-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-3 | Tabel To Be Returned: Indikator Titik Filter, Menutup Panel Tanpa Apply, dan Kombinasi Search dengan Filter (Bagian 3) | FE+BE | 25 | 1002, 1003, 1004 |
| TC-FA-TAG-E2E-249-tabel-to-be-returned-sort-dan-column-visibility-bagian-1 | Tabel To Be Returned: Sort Tiga Tahap Kolom TAG Code, Last Asset, Since, Return Group, dan Current Holder (Bagian 1) | FE+BE | 29 | 1005, 1006, 1007, 1008, 1009 |
| TC-FA-TAG-E2E-250-tabel-to-be-returned-sort-dan-column-visibility-bagian-2 | Tabel To Be Returned: Sort Kolom Reason, Sort dengan Filter Aktif, dan Column Visibility (Bagian 2) | FE+BE | 32 | 1010, 1011, 1012, 1013 |
| TC-FA-TAG-E2E-251-tabel-to-be-returned-sort-dan-column-visibility-bagian-3 | Tabel To Be Returned: Setup Column, Ikon Close Membuang Perubahan dan Reset to Default (Bagian 3) | FE+BE | 12 | 1016, 1017 |
| TC-FA-TAG-E2E-252-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-1 | Tabel To Be Returned: Pagination, Ganti Jumlah Baris, Nomor Halaman Tidak Valid, dan Sort pada Halaman 2 (Bagian 1) | FE+BE | 20 | 1018, 1019, 1020, 1021 |
| TC-FA-TAG-E2E-253-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-2 | Tabel To Be Returned: Download XLSX, Download Tanpa Hasil, dan State Tab Setelah Pindah Tab serta Refresh (Bagian 2) | FE+BE | 34 | 1024, 1025, 1027, 1028, 1029 |
| TC-FA-TAG-E2E-254-modal-event-log-screening-format-sel-dan-penutupan-bagian-1 | Modal Event Log To Be Returned: Screening, Urutan Bawaan, Format Sel, dan Hover Tooltip (Bagian 1) | FE+BE | 25 | 1030, 1031, 1032, 1033, 1034 |
| TC-FA-TAG-E2E-255-modal-event-log-screening-format-sel-dan-penutupan-bagian-2 | Modal Event Log To Be Returned: Penutupan Modal dan Tooltip Ikon Toolbar (Bagian 2) | FE+BE | 17 | 1035, 1036 |
| TC-FA-TAG-E2E-256-modal-event-log-search-per-kolom-bagian-1 | Modal Event Log To Be Returned: Empty State dan Search per Kolom TAG Code sampai Received By (Bagian 1) | FE+BE | 21 | 1037, 1038, 1039, 1040, 1041, 1042 |
| TC-FA-TAG-E2E-257-modal-event-log-search-per-kolom-bagian-2 | Modal Event Log To Be Returned: Search Method dan Final Status, Received At Tidak Dicari, serta Handed Over By Kosong (Bagian 2) | FE+BE | 17 | 1043, 1044, 1045, 1488 |
| TC-FA-TAG-E2E-258-modal-event-log-filter-per-kolom-bagian-1 | Modal Event Log To Be Returned: Screening Filter Panel dan Filter Method, Final Status, Return Group, serta Handed Over By (Bagian 1) | FE+BE | 30 | 1046, 1047, 1048, 1049, 1050 |
| TC-FA-TAG-E2E-259-modal-event-log-filter-per-kolom-bagian-2 | Modal Event Log To Be Returned: Filter Received By, Received At Inklusif, Method Multi-pilih, dan Opsi dari Data (Bagian 2) | FE+BE | 24 | 1051, 1052, 1053, 1054 |
| TC-FA-TAG-E2E-260-modal-event-log-sort-column-visibility-dan-pagination-bagian-1 | Modal Event Log To Be Returned: Sort Tiga Tahap Kolom Received At, TAG Code, Last Asset, dan Return Group (Bagian 1) | FE+BE | 27 | 1055, 1056, 1057, 1058 |
| TC-FA-TAG-E2E-261-modal-event-log-sort-column-visibility-dan-pagination-bagian-2 | Modal Event Log To Be Returned: Sort Tiga Tahap Kolom Handed Over By, Received By, Method, dan Final Status (Bagian 2) | FE+BE | 27 | 1059, 1060, 1061, 1062 |
| TC-FA-TAG-E2E-262-modal-event-log-sort-column-visibility-dan-pagination-bagian-3 | Modal Event Log To Be Returned: Column Visibility, Setup Column, dan Pagination (Bagian 3) | FE+BE | 32 | 1063, 1064, 1065, 1066 |
| TC-FA-TAG-E2E-263-modal-event-log-download-csv-dan-xlsx | Modal Event Log To Be Returned: Download CSV Mengikuti Filter dan Kolom, Download XLSX, serta Download Tanpa Hasil | FE+BE | 32 | 1067, 1068, 1070 |
| TC-FA-TAG-E2E-264-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-1 | Seleksi Tabel To Be Returned: Select All, Selection Limit, dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 1) | FE+BE | 35 | 1371, 1372, 1373, 1374, 1375, 1376 |
| TC-FA-TAG-E2E-265-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-2 | Seleksi Tabel To Be Returned: Ikon x, Unselect All, serta Filter dan Sort Tidak Mereset Seleksi (Bagian 2) | FE+BE | 33 | 1408, 1409, 1410, 1411 |
| TC-FA-TAG-E2E-266-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-3 | Seleksi Tabel To Be Returned: Checkbox Header Indeterminate dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 3) | FE+BE | 20 | 1412, 1413 |
| TC-FA-TAG-E2E-267-seleksi-popup-detail-select-all-selection-limit-checkbox-bagian-1 | Seleksi Popup Detail: Unselect All, Checkbox Header Indeterminate, dan Selection Limit pada Seleksi Manual serta Select All (Bagian 1) | FE+BE | 31 | 1400, 1401, 1402, 1403, 1404 |
| TC-FA-TAG-E2E-268-seleksi-popup-detail-select-all-selection-limit-checkbox-bagian-2 | Seleksi Popup Detail: Checkbox Header, Seleksi Terjaga Saat Pindah Halaman dan Saat Sort Diubah (Bagian 2) | FE+BE | 22 | 1405, 1406, 1407 |
| TC-FA-TAG-E2E-269-tabel-to-be-returned-sort-dan-column-visibility-bagian-4 | Tabel To Be Returned: Kolom Visible Terakhir dan Setup Column Tersimpan Setelah Save (Bagian 4) | FE+BE | 15 | 1014, 1015 |
| TC-FA-TAG-E2E-270-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-3 | Tabel To Be Returned: Pilihan Download dan Download CSV Mengikuti Filter dan Kolom Tampil (Bagian 3) | FE+BE | 24 | 1022, 1023 |
| TC-FA-TAG-E2E-271-derivasi-tanpa-objek-tugas-changelog-immutable-dan-tag-log-sebagai | Derivasi Tanpa Objek Tugas, Changelog Tidak Dapat Diubah, dan Popup TAG Log sebagai Satu-satunya Pintu Riwayat Status Tag | FE+BE | 29 | 1072, 1073, 1074, 1075, 1076, 1077 |
| TC-FA-TAG-E2E-272-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-1 | Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 1 | FE+BE | 35 | 1078, 1079, 1080, 1081 |
| TC-FA-TAG-E2E-273-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-2 | Pencatatan Changelog Replace dan Pair: Baris Old dan New Value, Bagian 2 | FE+BE | 35 | 1082, 1083, 1084 |
| TC-FA-TAG-E2E-274-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-3 | Pencatatan Changelog Pair Satu Slot dan Format Teks Polos Old dan New Value | FE+BE | 30 | 1085, 1086, 1087 |
| TC-FA-TAG-E2E-275-pencatatan-changelog-replace-dan-pair-baris-old-new-bagian-4 | Entri Changelog Lama Tidak Berubah setelah Tag Diganti Lagi | FE+BE | 13 | 1089 |
| TC-FA-TAG-E2E-276-pencatatan-activity-log-dan-system-log-replace-dan-pair | Pencatatan Activity Log dan System Log untuk Replace dan Pair TAG | FE+BE | 30 | 1091, 1092, 1093 |
| TC-FA-TAG-E2E-277-pencatatan-tag-log-replace-dan-pair-bagian-1 | Pencatatan TAG Log Replace: Tag Lama Dipindai, Tidak Dipindai, dan Dilepas | FE+BE | 34 | 1095, 1096, 1097 |
| TC-FA-TAG-E2E-278-pencatatan-tag-log-replace-dan-pair-bagian-2 | Pencatatan TAG Log Tag Baru: Paired dan Pair TAG per Tag | FE+BE | 29 | 1099, 1100, 1101 |
| TC-FA-TAG-E2E-279-pencatatan-receive-event-log-tag-log-global-dan-assigned-paired-bagian-1 | Pencatatan Receive: Event Log dan TAG Log Global untuk Receive TAG dan Receive Manually, Bagian 1 | FE+BE | 36 | 1103, 1104, 1105, 1107 |
| TC-FA-TAG-E2E-280-pencatatan-receive-event-log-tag-log-global-dan-assigned-paired-bagian-2 | Pencatatan Receive: TAG Log Global untuk Receive Manually dan Receive Manually Bulk, Bagian 2 | FE+BE | 26 | 1108, 1109 |
| TC-FA-TAG-E2E-281-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-1 | Pencatatan Activity Log dan System Log Aksi Receive TAG dan Receive Manually | FE+BE | 35 | 1113, 1114, 1115, 1116 |
| TC-FA-TAG-E2E-282-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-2 | Pencatatan Activity Log dan System Log Aksi Report TAG dan Decline Report | FE+BE | 33 | 1117, 1118, 1119 |
| TC-FA-TAG-E2E-283-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-3 | Pencatatan Activity Log dan System Log Aksi Decline Report dan Cancel Report | FE+BE | 30 | 1120, 1121, 1122 |
| TC-FA-TAG-E2E-284-pencatatan-changelog-report-decline-cancel-bagian-1 | Pencatatan Changelog Report TAG: Report Type Damaged, Missing, dan Unreadable | FE+BE | 31 | 1123, 1124, 1125 |
| TC-FA-TAG-E2E-285-pencatatan-changelog-report-decline-cancel-bagian-2 | Pencatatan Changelog Report TAG dua Tag dan Decline Report | FE+BE | 30 | 1126, 1127, 1128 |
| TC-FA-TAG-E2E-286-pencatatan-changelog-report-decline-cancel-bagian-3 | Pencatatan Changelog Cancel Report, Asset Detail, Scope Group, dan Entri Lama Tidak Berubah | FE+BE | 35 | 1129, 1130, 1131, 1132 |
| TC-FA-TAG-E2E-287-sinkron-masuk-dari-asset-name-dan-asset-detail-non-standard-bagian-1 | Sinkron Masuk dari Asset Name dan Asset Detail: Non-standard Mengikuti TAG Type | FE+BE | 34 | 1133, 1134, 1139, 1140, 1141, 1142 |
| TC-FA-TAG-E2E-288-sinkron-masuk-dari-asset-name-dan-asset-detail-non-standard-bagian-2 | Sinkron Masuk dari Asset Detail: Tag Paired yang Dilepas Keluar dari Tab Paired | FE+BE | 8 | 1143 |
| TC-FA-TAG-E2E-289-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-1 | Notifikasi Lintas Modul: tag_replacement_needed dan tag_report_created, Bagian 1 | FE+BE | 29 | 1135, 1136, 1223, 1248, 1249 |
| TC-FA-TAG-E2E-290-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-2 | Notifikasi Lintas Modul: tag_report_declined dan tag_report_canceled | FE+BE | 33 | 1250, 1251, 1252, 1253 |
| TC-FA-TAG-E2E-291-notifikasi-lintas-modul-tag-replacement-needed-report-created-bagian-3 | Notifikasi Lintas Modul: Notifikasi Laporan Ditandai Terbaca setelah Laporan Ditutup | FE+BE | 5 | 1254 |
| TC-FA-TAG-E2E-292-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-1 | Sinkron Lintas Modul: Registri Global dan Stok setelah Replace, Bagian 1 | FE+BE | 36 | 1144, 1145, 1146, 1147 |
| TC-FA-TAG-E2E-293-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-2 | Sinkron Lintas Modul: Registri Global dan Asset Detail setelah Pair TAG dan Replace, Bagian 2 | FE+BE | 35 | 1148, 1149, 1150, 1151 |
| TC-FA-TAG-E2E-294-sinkron-lintas-modul-registri-global-asset-detail-dan-stok-bagian-3 | Sinkron Lintas Modul: Tag Combined di-Separate saat Submit Replace | FE+BE | 9 | 1153 |
| TC-FA-TAG-E2E-295-progres-kepatuhan-tag-type-asset-name-dan-definisi-kepatuhan-bagian-1 | Progres Kepatuhan TAG Type pada Detail Asset Name dan Definisi Kepatuhan, Bagian 1 | FE+BE | 34 | 1137, 1138, 1152, 1497, 1498, 1499 |
| TC-FA-TAG-E2E-296-progres-kepatuhan-tag-type-asset-name-dan-definisi-kepatuhan-bagian-2 | Progres Kepatuhan TAG Type Tidak Tampil bila Jumlah Aset N Sama dengan 0 | FE+BE | 10 | 1500 |
| TC-FA-TAG-E2E-297-derivasi-non-standard-reported-dan-not-paired-yet-bagian-1 | Derivasi Non-standard, Reported, dan Not Paired Yet: Dihitung Ulang dan Aturan Non-standard, Bagian 1 | FE+BE | 32 | 143, 1316, 1318, 1319, 1320, 1321, 1322, 1323 |
| TC-FA-TAG-E2E-298-derivasi-non-standard-reported-dan-not-paired-yet-bagian-2 | Derivasi Non-standard, Reported, dan Not Paired Yet: Reported, Not Paired Yet, dan Pembentukan Baris Grup, Bagian 2 | FE+BE | 29 | 1324, 1325, 1326, 1327, 1328, 1329, 1330, 1331 |
| TC-FA-TAG-E2E-299-derivasi-non-standard-reported-dan-not-paired-yet-bagian-3 | Derivasi Not Paired Yet: Aset Non-TAG dan Asset Name BLE dan GPS Tidak Dihitung | FE+BE | 10 | 1480, 1481 |
| TC-FA-TAG-E2E-300-sinkron-masuk-disposal-tag-masuk-to-be-returned-dan-snapshot-bagian-1 | Sinkron Masuk Disposal: Tag Masuk ke Tab To Be Returned dan Snapshot, Bagian 1 | FE+BE | 33 | 1233, 1234, 1235, 1236, 1237, 1238 |
| TC-FA-TAG-E2E-301-sinkron-masuk-disposal-tag-masuk-to-be-returned-dan-snapshot-bagian-2 | Sinkron Masuk Disposal: TAG Log Global, Penutupan Laporan, Scope Return Group, dan Receive Manually, Bagian 2 | FE+BE | 29 | 1239, 1241, 1381, 1242, 1243 |
| TC-FA-TAG-E2E-302-sinkron-masuk-global-delete-dan-tag-lama-hasil-replace | Sinkron Masuk Global: Tag Lama Hasil Replace dan Tag To Be Returned yang Dihapus di Global | FE+BE | 34 | 1244, 1245, 1246, 1247 |
| TC-FA-TAG-E2E-303-pencatatan-tag-log-replace-tag-qr-lama-keluar-dari-registri | Pencatatan TAG Log Replace: Tag QR Lama Keluar dari Registri | FE+BE | 9 | 1098 |
| TC-FA-TAG-E2E-304-pencatatan-event-log-assigned-paired-tag-to-be-returned-dipasang-lewat-pair-dan-replace | Pencatatan Event Log Assigned/Paired untuk Tag To Be Returned yang Dipasang lewat Pair TAG dan Replace | FE+BE | 23 | 1111, 1112 |
| TC-FA-TAG-E2E-305-matriks-dampak-transaksi-assignment-bagian-1 | Matriks Dampak Transaksi Assignment: Assign Kondisi T2 sampai T4 dan Return Kondisi T1 sampai T3 | FE+BE | 34 | 1156, 1157, 1158, 1159, 1160, 1161 |
| TC-FA-TAG-E2E-306-matriks-dampak-transaksi-assignment-bagian-2 | Matriks Dampak Transaksi Assignment: Return Kondisi T4 dan Offboarding Return Kondisi T1 sampai T4 | FE+BE | 37 | 1162, 1163, 1164, 1165, 1166 |
| TC-FA-TAG-E2E-307-matriks-dampak-transaksi-borrow-bagian-1 | Matriks Dampak Transaksi Borrow: Check-out Kondisi T1 sampai T4 dan Extend Kondisi T1 sampai T3 | FE+BE | 35 | 1167, 1168, 1169, 1170, 1171, 1172, 1173 |
| TC-FA-TAG-E2E-308-matriks-dampak-transaksi-borrow-bagian-2 | Matriks Dampak Transaksi Borrow: Extend Kondisi T4 dan Check-in Kondisi T1 sampai T4 | FE+BE | 33 | 1174, 1175, 1176, 1177, 1178 |
| TC-FA-TAG-E2E-309-matriks-dampak-transaksi-transfer-bagian-1 | Matriks Dampak Transaksi Transfer: Load Kondisi T2 sampai T4 dan Receive di Tujuan Kondisi T1 sampai T3 | FE+BE | 34 | 1180, 1181, 1182, 1183, 1184, 1185 |
| TC-FA-TAG-E2E-310-matriks-dampak-transaksi-transfer-bagian-2 | Matriks Dampak Transaksi Transfer: Receive di Tujuan Kondisi T4 | FE+BE | 9 | 1186 |
| TC-FA-TAG-E2E-311-matriks-dampak-transaksi-disposal-bagian-1 | Matriks Dampak Transaksi Disposal: Request Kondisi T2 sampai T4 menurut Disposal Type | FE+BE | 34 | 1188, 1189, 1190, 1191, 1192 |
| TC-FA-TAG-E2E-312-matriks-dampak-transaksi-disposal-bagian-2 | Matriks Dampak Transaksi Disposal: Execute Kondisi T1 sampai T4 dan Konfirmasi Saksi | FE+BE | 34 | 1193, 1194, 1195, 1196 |
| TC-FA-TAG-E2E-313-matriks-dampak-transaksi-stock-opname-dan-maintenance-bagian-1 | Matriks Dampak Transaksi Stock Opname: Scan Aset Kondisi T2 sampai T4 | FE+BE | 25 | 1198, 1199, 1200 |
| TC-FA-TAG-E2E-314-matriks-dampak-transaksi-stock-opname-dan-maintenance-bagian-2 | Matriks Dampak Transaksi Maintenance: Report Damage atau Complete Work Order Kondisi T1 sampai T4 | FE+BE | 28 | 1201, 1202, 1203, 1204 |
| TC-FA-TAG-E2E-315-blok-t3-pada-mulai-transaksi-role-policy-dan-laporan-terbuka | Blok T3 pada Mulai Transaksi: Role, Policy, dan Laporan Terbuka | FE+BE | 33 | 1205, 1206, 1207, 1208, 1209, 1210 |
| TC-FA-TAG-E2E-316-evaluasi-kondisi-tag-aset-dua-tag-dan-identifikasi-manual-bagian-1 | Evaluasi Kondisi Tag Aset Dua Tag dan Identifikasi Manual: Penilaian T1 sampai T3, Checkbox Bawaan, dan Report Unreadable Otomatis | FE+BE | 34 | 1211, 1212, 1213, 1214, 1215 |
| TC-FA-TAG-E2E-317-evaluasi-kondisi-tag-aset-dua-tag-dan-identifikasi-manual-bagian-2 | Identifikasi Manual: Hanya Tag yang Dipilih Dilaporkan dan Aset T4 Tanpa Report | FE+BE | 16 | 1217, 1218 |
| TC-FA-TAG-E2E-318-stock-opname-t3-dan-disposal-execute-t3-saksi-dan-pelepasan-tag | Stock Opname T3 dan Disposal Execute T3: Found (manual), Saksi, dan Pelepasan Tag | FE+BE | 30 | 1219, 1220, 1221, 1222 |
| TC-FA-TAG-E2E-319-replace-tag-saat-transaksi-berjalan-diizinkan-dan-disposal-bagian-1 | Replace TAG saat Transaksi Berjalan: Aset Assigned, Menunggu Serah Terima, In Transfer Process, dan Under Maintenance | FE+BE | 34 | 1224, 1226, 1227, 1229 |
| TC-FA-TAG-E2E-320-replace-tag-saat-transaksi-berjalan-diizinkan-dan-disposal-bagian-2 | Replace TAG saat Transaksi Berjalan: Permanently Missing Diizinkan serta In Disposal Process dan Disposed Disabled | FE+BE | 17 | 1230, 1231, 1232 |
| TC-FA-TAG-E2E-321-matriks-dampak-transaksi-kondisi-t1-dan-aset-non-tag-lintas-modul | Matriks Dampak Transaksi Kondisi T1 dan Aset Non-TAG: Assign, Load, Request, dan Scan Aset Berjalan Normal | FE+BE | 31 | 1155, 1482, 1179, 1187, 1197 |
| TC-FA-TAG-E2E-322-replace-tag-saat-borrow-dan-sesi-opname-serta-identifikasi-manual-laporan-terbuka | Identifikasi Manual pada Tag dengan Laporan Terbuka serta Replace TAG saat Borrow dan Sesi Opname | FE+BE | 31 | 1216, 1225, 1228 |
| TC-FA-TAG-E2E-323-defense-in-depth-akses-data-tab-paired-dan-isolasi-client | Defense-in-Depth: Akses Data Tab Paired Ditolak Server, Isolasi Client, dan Tombol Hidden Bukan Pengganti Pemeriksaan Server | FE+BE | 31 | 142, 1262, 1263, 1264, 1265, 1266, 1267 |
| TC-FA-TAG-E2E-324-defense-in-depth-injeksi-markup-dan-sql-pada-teks-tampil-dan-search | Defense-in-Depth: Injeksi Markup dan SQL Ditampilkan sebagai Teks pada Tabel, Changelog, Search, dan TAG Log | FE+BE | 29 | 1259, 1260, 1261, 1307, 1308 |
| TC-FA-TAG-E2E-325-defense-in-depth-submit-langsung-replace-pair-dan-start-print-bagian-1 | Defense-in-Depth: Submit Langsung Replace, Pair, dan Start Print Ditolak 403 untuk Role Tanpa Hak (Bagian 1) | FE+BE | 28 | 1268, 1269, 1270, 1271, 1272, 1273, 1274 |
| TC-FA-TAG-E2E-326-defense-in-depth-submit-langsung-replace-pair-dan-start-print-bagian-2 | Defense-in-Depth: Submit Langsung Replace dan Pair Ditolak Server karena Kondisi Aset, Stok, Status Tag, Plan, dan Return Group (Bagian 2) | FE+BE | 28 | 1275, 1276, 1277, 1278, 1279, 1280 |
| TC-FA-TAG-E2E-327-defense-in-depth-izin-dicabut-saat-dialog-atau-halaman-terbuka-bagian-1 | Defense-in-Depth: Izin Update atau Scope Group Dicabut saat Dialog Replace atau Pair Terbuka, Submit Ditolak Server (Bagian 1) | FE+BE | 29 | 1281, 1282, 1283 |
| TC-FA-TAG-E2E-328-defense-in-depth-izin-dicabut-saat-dialog-atau-halaman-terbuka-bagian-2 | Defense-in-Depth: Hak Update Dicabut saat Dialog Receive TAG, Receive Manually, atau Decline Report Terbuka, Commit Ditolak Server (Bagian 2) | FE+BE | 32 | 1303, 1304, 1305 |
| TC-FA-TAG-E2E-329-defense-in-depth-commit-langsung-receive-receive-manually-dan-bagian-1 | Defense-in-Depth: Commit Langsung Receive TAG, Receive Manually, dan Decline Report Ditolak Server (Bagian 1) | FE+BE | 28 | 1290, 1291, 1292, 1293, 1294, 1295, 1306 |
| TC-FA-TAG-E2E-330-defense-in-depth-commit-langsung-receive-receive-manually-dan-bagian-2 | Defense-in-Depth: Search dan Filter Return Group To Be Returned Tidak Menjangkau Group di Luar Scope (Bagian 2) | FE+BE | 10 | 1309, 1310 |
| TC-FA-TAG-E2E-331-resilience-error-load-try-again-halaman-tab-paired-dan-to-be-returned | Resilience: Error Load Tab Paired dan To Be Returned (5xx) dan Pemulihan lewat Try Again | FE+BE | 13 | 16, 17, 87 |
| TC-FA-TAG-E2E-332-resilience-download-gagal-toast-error-paired-changelog-to-be-returned | Resilience: Download Gagal Menampilkan Toast Error pada Paired, Changelog, To Be Returned, dan Event Log | FE+BE | 27 | 230, 970, 1026, 1069 |
| TC-FA-TAG-E2E-333-resilience-pencarian-tag-overlay-scan-gagal-dan-penggantian-atomik | Resilience: Pencarian Tag di Overlay Scan Gagal (5xx dan Timeout) dan Penggantian Atomik saat Pemasangan Tag Baru Gagal | FE+BE | 25 | 259, 260, 1350 |
| TC-FA-TAG-E2E-334-resilience-submit-replace-gagal-timeout-layanan-global-dan-retry | Resilience: Submit Replace Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) dan Retry Berhasil | FE+BE | 27 | 1340, 1341, 1342, 1343 |
| TC-FA-TAG-E2E-335-resilience-submit-pair-gagal-timeout-dan-layanan-global-tidak-terjangkau | Resilience: Submit Pair Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Slot | FE+BE | 33 | 1345, 1346, 1347 |
| TC-FA-TAG-E2E-336-resilience-sesi-batch-replace-dan-pair-kegagalan-server-satu-bagian-1 | Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Replace TAG (5xx, Timeout, Retry Failed) (Bagian 1) | FE+BE | 31 | 405, 406, 407 |
| TC-FA-TAG-E2E-337-resilience-sesi-batch-replace-dan-pair-kegagalan-server-satu-bagian-2 | Resilience: Kegagalan Server pada Satu Aset dalam Sesi Batch Pair (Toast, Dialog Tetap Terbuka, Skip) (Bagian 2) | FE+BE | 15 | 467, 468 |
| TC-FA-TAG-E2E-338-resilience-start-print-gagal-timeout-dan-retry | Resilience: Start Print Gagal (5xx dan Timeout) Mempertahankan Dialog Print QR dan Retry Berhasil | FE+BE | 31 | 495, 496, 497 |
| TC-FA-TAG-E2E-339-resilience-receive-tag-dan-receive-manually-gagal-timeout-dan-bagian-1 | Resilience: Receive TAG Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Daftar Sesi (Bagian 1) | FE+BE | 26 | 563, 564, 565 |
| TC-FA-TAG-E2E-340-resilience-receive-tag-dan-receive-manually-gagal-timeout-dan-bagian-2 | Resilience: Receive Manually dan Bulk Receive Manually Gagal (5xx, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Seleksi (Bagian 2) | FE+BE | 31 | 583, 584, 585 |
| TC-FA-TAG-E2E-341-resilience-report-tag-decline-report-dan-cancel-report-gagal-5xx | Resilience: Report TAG, Cancel Report, dan Decline Report Gagal (5xx) Mempertahankan Dialog | FE+BE | 31 | 617, 645, 668 |
| TC-FA-TAG-E2E-342-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-1 | Guard Klik Ganda: Pindaian Beruntun, Start Print, dan Receive Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 1) | FE+BE | 26 | 257, 494, 566 |
| TC-FA-TAG-E2E-343-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-2 | Guard Klik Ganda: Submit Decline Report dan Submit Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 2) | FE+BE | 22 | 646, 1344 |
| TC-FA-TAG-E2E-344-guard-submit-beruntun-klik-ganda-hanya-satu-efek-bagian-3 | Guard Klik Ganda: Submit Pair dan Submit & next Sesi Batch Replace Ditekan Beruntun Hanya Menghasilkan Satu Efek (Bagian 3) | FE+BE | 24 | 1348, 1349 |
| TC-FA-TAG-E2E-345-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-1 | State Tenant: Free Plan Mengunci Seluruh Tipe Pengganti pada Scan Replace dan Row Action Replace TAG (Bagian 1) | FE+BE | 18 | 245, 263, 375 |
| TC-FA-TAG-E2E-346-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-2 | State Tenant: Free Plan pada Tag Non-standard, Bulk Batch Replace, Tampilan Tab Paired, Menu TAG, dan Upgrade Plan (Bagian 2) | FE+BE | 30 | 376, 383, 1154, 1314, 1315 |
| TC-FA-TAG-E2E-347-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-3 | State Tenant: Plan yang Mengunci Tag NFC pada Dialog Replace TAG dan Tag Combined (Bagian 3) | FE+BE | 22 | 307, 308, 365 |
| TC-FA-TAG-E2E-348-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-1 | State Tenant: Entitas Suspended Menolak Submit Replace, Submit Pair, dan Submit & next Sesi Batch dengan Pesan V-22 (Bagian 1) | FE+BE | 28 | 1285, 1287, 1288 |
| TC-FA-TAG-E2E-349-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-2 | State Tenant: Entitas Suspended atau Expired Menolak Start Print, Receive TAG, dan Receive Manually dengan Pesan V-22 (Bagian 2) | FE+BE | 29 | 1289, 1296, 1297, 1298 |
| TC-FA-TAG-E2E-350-state-tenant-entitas-suspended-atau-expired-baca-boleh-tulis-bagian-3 | State Tenant: Entitas Suspended atau Expired Menolak Report TAG dan Cancel Report dengan Pesan V-22 (Bagian 3) | FE+BE | 28 | 1299, 1300, 1302 |
| TC-FA-TAG-E2E-351-guard-submit-report-tag-dan-cancel-report-ditekan-beruntun-hanya-satu-laporan | Guard Klik Ganda: Submit Report TAG dan Cancel Report Ditekan Beruntun Hanya Membuat dan Menutup Satu Laporan (Bagian 4) | FE+BE | 20 | 619, 669 |
| TC-FA-TAG-E2E-352-defense-in-depth-izin-dicabut-saat-dialog-print-qr-dan-halaman-terbuka | Defense-in-Depth: Izin Update Dicabut saat Dialog Print QR Terbuka dan saat Halaman Terbuka, Aksi Tulis Hidden Sesudah Muat Ulang | FE+BE | 17 | 1284, 1313 |
| TC-FA-TAG-E2E-353-absence-log-replace-pair-start-print-receive-dan-intake-bagian-1 | Absence Log: Submit Replace Ditolak dan Start Print Berhasil Tidak Menulis Changelog, Activity Log, dan System Log | FE+BE | 34 | 1088, 1090, 1094 |
| TC-FA-TAG-E2E-354-absence-log-replace-pair-start-print-receive-dan-intake-bagian-2 | Absence Log: Pair TAG Gagal 5xx dan Receive TAG Tidak Menulis Changelog atau TAG Log | FE+BE | 35 | 1102, 1106 |
| TC-FA-TAG-E2E-355-waktu-kolom-since-tag-to-be-returned-hari-kalender-dan-tanpa-bagian-1 | Waktu: Kolom Since Hari ke-0 sampai ke-14 Tanpa Peringatan dan Tanpa Notifikasi Overdue pada Hari ke-7 sampai ke-30 | FE+BE | 15 | 1255, 1256, 1257, 1258, 1353, 1354, 1355, 1356 |
| TC-FA-TAG-E2E-356-waktu-kolom-since-tag-to-be-returned-hari-kalender-dan-tanpa-bagian-2 | Waktu: Kolom Since Melewati Batas Pengembalian pada Hari ke-15 dan ke-30, Hari Kalender, dan Tanpa Aksi Otomatis | FE+BE | 26 | 1357, 1358, 1359, 1360 |
| TC-FA-TAG-E2E-357-job-pengingat-laporan-terbuka-hari-ke-8-dan-penutupan-laporan | Job Pengingat: Laporan Terbuka Mendapat Pengingat Tepat pada Hari ke-8 dan Tidak pada Kondisi Lain | FE+BE | 33 | 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370 |
| TC-FA-TAG-E2E-358-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-1 | Kondisi Reader: Tombol Replace TAG Disabled dan Dialog Blok D-10a sampai D-10e pada Toolbar dan Row Action | FE+BE | 18 | 508, 509, 510, 511, 512, 513, 514 |
| TC-FA-TAG-E2E-359-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-2 | Kondisi Reader: Dialog Blok Batch Replace dan Pair TAG serta Alert Error Inline Scan Current TAG | FE+BE | 32 | 515, 516, 517, 518, 519 |
| TC-FA-TAG-E2E-360-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-3 | Kondisi Reader: Alert Error Inline Scan Current TAG di Dialog Replace TAG untuk Reader Mati, Dua Reader, Belum Sinkron, dan Waiting for Approval | FE+BE | 22 | 520, 521, 522, 523 |
| TC-FA-TAG-E2E-361-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-4 | Kondisi Reader: Alert Error Inline Scan Replacement TAG dan Banner Reader Terputus di Dialog Replace, Pair, dan Batch Replace | FE+BE | 31 | 524, 526, 527, 525, 528 |
| TC-FA-TAG-E2E-362-reader-driver-replace-dan-pair-blokir-d-10a-sampai-d-10e-dan-bagian-5 | Kondisi Reader: Banner Reader Terputus di Dialog Pair TAG dan Urutan Pemeriksaan Reader Sebelum Driver | FE+BE | 13 | 529, 530 |
| TC-FA-TAG-E2E-363-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-1 | Kondisi Reader: Tombol Receive TAG Disabled, Banner Reader Terputus, dan Dialog Blok D-10a sampai D-10d | FE+BE | 21 | 550, 551, 552, 553, 554, 555 |
| TC-FA-TAG-E2E-364-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-2 | Kondisi Reader: Dialog Blok D-10e dan Alert Error Inline Scan di Dialog Receive TAG | FE+BE | 28 | 556, 557, 558, 559, 560 |
| TC-FA-TAG-E2E-365-reader-driver-receive-tag-blokir-dan-alert-inline-bagian-3 | Kondisi Reader: Alert Waiting for Approval di Dialog Receive TAG Hilang Setelah Scan Berikutnya Berhasil | FE+BE | 12 | 561, 562 |
| TC-FA-TAG-E2E-366-isi-berkas-unduhan-tab-paired-dan-to-be-returned-nilai-sel-bom-bagian-1 | Isi Berkas Unduhan: BOM, Nilai Sel, dan Scope Baris CSV Tab Paired, To Be Returned, dan Event Log | FE+BE | 35 | 222, 231, 223, 232, 233, 1311, 1312 |
| TC-FA-TAG-E2E-367-isi-berkas-unduhan-tab-paired-dan-to-be-returned-nilai-sel-bom-bagian-2 | Isi Berkas Unduhan: Asset Value Numerik, Transactional Policy, Category Berhierarki, dan Current Holder Nama Lengkap | FE+BE | 28 | 1434, 1435, 1436, 1437 |
| TC-FA-TAG-E2E-368-download-tab-paired-di-atas-5000-baris-loading-screen-tanpa-job-latar | Volume Data: Download Tab Paired di Atas 5.000 Baris Memakai Loading Screen Tanpa Job Latar | FE+BE | 5 | 1438 |
| TC-FA-TAG-E2E-369-aksesibilitas-dialog-fokus-trap-dan-aria-live-akun-total-bagian-1 | Aksesibilitas: Focus Trap Dialog Replace, Pair, dan Print QR, Aria-Live Hasil Pindai, dan Label Ikon Tipe Tag | FE+BE | 23 | 318, 323, 322, 321, 319, 320 |
| TC-FA-TAG-E2E-370-aksesibilitas-dialog-fokus-trap-dan-aria-live-akun-total-bagian-2 | Aksesibilitas: Focus Trap Dialog Receive TAG, Receive Manually, dan Decline Report serta Aria-Live Hasil Scan Receive TAG | FE+BE | 22 | 571, 572, 570, 597, 1447 |
| TC-FA-TAG-E2E-371-aksesibilitas-aria-live-buttonscan-dan-focus-trap-dialog-report-dan | Aksesibilitas: Aria-Live Hasil ButtonScan Overlay Scan Replace dan Focus Trap Dialog Report TAG dan Cancel Report TAG | FE+BE | 17 | 24, 635, 1448 |
| TC-FA-TAG-E2E-372-konfirmasi-bawaan-browser-saat-muat-ulang-dialog-terisi-bagian-1 | Muat Ulang: Konfirmasi Bawaan Browser Muncul pada Dialog Replace, Pair, dan Sesi Batch Replace yang Sudah Terisi | FE+BE | 29 | 1463, 1464, 1465 |
| TC-FA-TAG-E2E-373-konfirmasi-bawaan-browser-saat-muat-ulang-dialog-terisi-bagian-2 | Muat Ulang: Konfirmasi Bawaan Browser pada Dialog Receive TAG dan Sesi Pair Terisi, Tidak Muncul pada Dialog Kosong dan Setelah Submit | FE+BE | 35 | 1466, 1467, 1484, 1468 |
| TC-FA-TAG-E2E-374-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-1 | Konkurensi: Dialog D-04 Asset TAG Has Changed Saat Tag Lama Diganti, Dilepas, atau TAG Type Berubah oleh Pelaku Lain | FE+BE | 30 | 1332, 1333, 1334, 1335 |
| TC-FA-TAG-E2E-375-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-2 | Konkurensi: Plan Berubah, Tag Pengganti Direbut Pengguna Lain, dan Dua Pengguna Memindai Tag Pengganti yang Sama | FE+BE | 27 | 1336, 1337, 1338 |
| TC-FA-TAG-E2E-376-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-3 | Konkurensi: Aset In Disposal Process Setelah Dialog Replace Dibuka dan Aset Sudah Dipasangkan Pengguna Lain Sebelum Submit Pair | FE+BE | 26 | 1339, 1351 |
| TC-FA-TAG-E2E-377-absence-log-intake-disposal-receive-manually-dan-derivasi-asset-name | Absence Log: Intake Disposal, Derivasi TAG Type, dan Receive Manually Tidak Menulis Entri yang Tidak Semestinya | FE+BE | 35 | 1240, 1071, 1110 |
| TC-FA-TAG-E2E-379-screening-halaman-tag-tab-paired-tanpa-tombol-create-atau-delete-data-tag | Halaman TAG Tanpa Tombol Create atau Delete Data Tag | FE+BE | 29 | 13 |
| TC-FA-TAG-E2E-380-hak-parsial-update-read-per-group-pada-aksi-halaman-return-group-dan-descendant | Hak Parsial Update dan Read per Group pada Aksi Halaman TAG: Return Group dan Descendant | FE+BE | 13 | 128, 129 |
| TC-FA-TAG-E2E-381-role-matrix-report-tag-dan-cancel-report-dari-modul-audit-monitoring-dan-gm | Role Matrix: Cancel Report TAG dari Modul Audit untuk Monitoring dan GM | FE+BE | 11 | 187, 188 |
| TC-FA-TAG-E2E-382-replace-tag-combined-slot-validasi-v-25-v-26-dan-submit-kosongkan-slot-dan-separate-otomatis | Replace dengan Tag Combined: Kosongkan Slot Hasil Combined dan Separate Otomatis saat Submit | FE+BE | 22 | 367, 368 |
| TC-FA-TAG-E2E-383-guard-submit-receive-manually-ditekan-beruntun-hanya-satu-entri | Guard Klik Ganda: Submit Receive Manually Ditekan Beruntun Hanya Menulis Satu Entri Event Log (Bagian 5) | FE+BE | 12 | 587 |
| TC-FA-TAG-E2E-384-state-tenant-plan-nfc-terkunci-pada-pair-tag-slot-tidak-ditampilkan | State Tenant: Plan yang Mengunci Tag NFC pada Dialog Pair TAG, Slot Tidak Ditampilkan dan Submit Disabled (Bagian 4) | FE+BE | 15 | 425, 1476 |
| TC-FA-TAG-E2E-385-state-tenant-entitas-suspended-decline-report-baca-saja-dan-replace-expired | State Tenant: Decline Report Ditolak saat Suspended, Halaman TAG Tetap Dapat Dibaca, dan Submit Replace Ditolak saat Expired (Bagian 4) | FE+BE | 37 | 1286, 1301, 1317 |
| TC-FA-TAG-E2E-386-custom-field-bertipe-date-guard-search-filter-dan-sort-pada-tabel-t-tag-02 | Custom Field Bertipe Date pada Tabel T-TAG-02: Guard Search, Filter, dan Sort | FE+BE | 25 | 905, 906, 907 |
| TC-FA-TAG-E2E-387-multi-tab-tab-browser-baru-memulai-state-default-tabel-paired | Multi-Tab: Tab Browser Baru Memulai State Default Tabel Paired | FE+BE | 6 | 929 |
| TC-FA-TAG-E2E-388-absence-log-request-langsung-replace-ditolak-tidak-menulis-changelog | Absence Log: Request Langsung Replace yang Ditolak 403 Tidak Menulis Changelog | FE+BE | 18 | 1262, 1268, 1269, 1270 |
| TC-FA-TAG-E2E-389-absence-log-request-langsung-receive-dan-decline-report-ditolak-tidak-menulis-event-log-tag-log-changelog | Absence Log: Request Langsung Receive TAG, Receive Manually, dan Decline Report yang Ditolak 403 Tidak Menulis Event Log, TAG Log, dan Changelog | FE+BE | 26 | 1290, 1291, 1292, 1293, 1294 |
| TC-FA-TAG-E2E-390-replace-tag-berlaporan-terbuka-terkunci-dan-wajib-diganti | Replace: Tag Berlaporan Terbuka Tercentang dan Terkunci pada Row Action, Overlay Scan, dan Bulk Batch Replace | FE+BE | 33 | 1504, 1505, 1506, 1507 |
| TC-FA-TAG-E2E-391-replace-tag-berlaporan-terbuka-bertipe-terkunci-plan-dilepas-tanpa-pasangan | Replace: Tag Berlaporan Terbuka Bertipe Terkunci Plan Dilepas Tanpa Pasangan dan Laporan Ditutup | FE+BE | 8 | 1508 |
| TC-FA-TAG-E2E-392-modal-changelog-daftar-aset-menampilkan-entri-replace-tag | Modal Changelog Daftar Aset: Entri Changelog TAG Replace Tampil | FE+BE | 4 | 1501 |

## Dataset tab Paired

- Dataset umum empat grup dipakai TC 1, 928, 929, dan 1028. Dataset khusus 25 grup (precondition d) dipakai TC 914 sampai 921 (spec 229) dan TC 925 (spec 231); kedua spec memulihkannya ke dataset umum empat grup di hook `after` atau langkah akhir.

## Spec multi-konteks (kelas c)

- Spec `387` memuat TC 929 (tab browser baru memulai state default). Tab browser kedua adalah objek asersi, sehingga TC ini dipisah dari spec fungsional 242 (TC 930) menurut prinsip 13c.

## Pembagian TC lintas spec: asersi absence log (S-05)

Tiap TC di bawah berada di `sourceTc` dua spec sekaligus, sehingga `check-suite.py` melaporkan satu temuan C2 tingkat [REVIEW] per TC. Ini disengaja (S-05, `P-5` butir a): klausa "tidak ada entri log baru" atas request langsung yang ditolak server (kelas a) dipisah ke spec absence kelas g dengan request langsung sebagai pemicu dan baseline sendiri, sedangkan status respons 403 dan state data tetap diasersi di spec kelas a. Id TC tetap di `sourceTc` kedua spec dan pembagian ditulis di `## Notes` keduanya. Pada tabel "Lapisan per TC", baris pertama TC adalah spec asal dan baris kedua adalah spec absence.

- Spec `388` (Changelog Paired TAG): TC 1262 (spec asal 323), TC 1268, 1269, dan 1270 (spec asal 325).
- Spec `389` (Event Log, TAG Log, dan Changelog): TC 1290, 1291, 1292, 1293, dan 1294 (spec asal 329).
- Spec absence dipisah menjadi 388 dan 389 mengikuti spec asalnya karena gabungannya (44 langkah) melewati batas ±35 langkah.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-TAG-1 | TC-FA-TAG-E2E-001 | FE+BE |
| TC-FA-TAG-2 | TC-FA-TAG-E2E-001 | FE+BE |
| TC-FA-TAG-3 | TC-FA-TAG-E2E-001 | FE+BE |
| TC-FA-TAG-4 | TC-FA-TAG-E2E-018 | FE+BE |
| TC-FA-TAG-5 | TC-FA-TAG-E2E-018 | FE+BE |
| TC-FA-TAG-6 | TC-FA-TAG-E2E-018 | FE+BE |
| TC-FA-TAG-7 | TC-FA-TAG-E2E-018 | FE+BE |
| TC-FA-TAG-8 | TC-FA-TAG-E2E-002 | FE+BE |
| TC-FA-TAG-9 | TC-FA-TAG-E2E-002 | FE+BE |
| TC-FA-TAG-10 | TC-FA-TAG-E2E-002 | FE+BE |
| TC-FA-TAG-11 | TC-FA-TAG-E2E-002 | FE+BE |
| TC-FA-TAG-12 | TC-FA-TAG-E2E-002 | FE+BE |
| TC-FA-TAG-13 | TC-FA-TAG-E2E-379 | FE+BE |
| TC-FA-TAG-14 | TC-FA-TAG-E2E-003 | FE+BE |
| TC-FA-TAG-15 | TC-FA-TAG-E2E-004 | FE+BE |
| TC-FA-TAG-16 | TC-FA-TAG-E2E-331 | FE+BE |
| TC-FA-TAG-17 | TC-FA-TAG-E2E-331 | FE+BE |
| TC-FA-TAG-18 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-19 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-20 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-21 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-22 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-23 | TC-FA-TAG-E2E-005 | FE+BE |
| TC-FA-TAG-24 | TC-FA-TAG-E2E-371 | FE+BE |
| TC-FA-TAG-25 | TC-FA-TAG-E2E-006 | FE+BE |
| TC-FA-TAG-26 | TC-FA-TAG-E2E-006 | FE+BE |
| TC-FA-TAG-27 | TC-FA-TAG-E2E-006 | FE+BE |
| TC-FA-TAG-28 | TC-FA-TAG-E2E-006 | FE+BE |
| TC-FA-TAG-29 | TC-FA-TAG-E2E-003 | FE+BE |
| TC-FA-TAG-30 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-31 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-32 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-33 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-34 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-35 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-36 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-37 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-38 | TC-FA-TAG-E2E-007 | FE+BE |
| TC-FA-TAG-39 | TC-FA-TAG-E2E-008 | FE+BE |
| TC-FA-TAG-40 | TC-FA-TAG-E2E-008 | FE+BE |
| TC-FA-TAG-41 | TC-FA-TAG-E2E-008 | FE+BE |
| TC-FA-TAG-42 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-43 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-44 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-45 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-46 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-47 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-48 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-49 | TC-FA-TAG-E2E-009 | FE+BE |
| TC-FA-TAG-50 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-51 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-52 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-53 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-54 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-55 | TC-FA-TAG-E2E-010 | FE+BE |
| TC-FA-TAG-56 | TC-FA-TAG-E2E-011 | FE+BE |
| TC-FA-TAG-57 | TC-FA-TAG-E2E-011 | FE+BE |
| TC-FA-TAG-58 | TC-FA-TAG-E2E-011 | FE+BE |
| TC-FA-TAG-59 | TC-FA-TAG-E2E-012 | FE+BE |
| TC-FA-TAG-60 | TC-FA-TAG-E2E-012 | FE+BE |
| TC-FA-TAG-61 | TC-FA-TAG-E2E-012 | FE+BE |
| TC-FA-TAG-62 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-63 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-64 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-65 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-66 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-67 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-68 | TC-FA-TAG-E2E-013 | FE+BE |
| TC-FA-TAG-69 | TC-FA-TAG-E2E-014 | FE+BE |
| TC-FA-TAG-70 | TC-FA-TAG-E2E-014 | FE+BE |
| TC-FA-TAG-71 | TC-FA-TAG-E2E-015 | FE+BE |
| TC-FA-TAG-72 | TC-FA-TAG-E2E-015 | FE+BE |
| TC-FA-TAG-73 | TC-FA-TAG-E2E-019 | FE+BE |
| TC-FA-TAG-74 | TC-FA-TAG-E2E-014 | FE+BE |
| TC-FA-TAG-75 | TC-FA-TAG-E2E-019 | FE+BE |
| TC-FA-TAG-76 | TC-FA-TAG-E2E-016 | FE+BE |
| TC-FA-TAG-77 | TC-FA-TAG-E2E-016 | FE+BE |
| TC-FA-TAG-78 | TC-FA-TAG-E2E-016 | FE+BE |
| TC-FA-TAG-79 | TC-FA-TAG-E2E-016 | FE+BE |
| TC-FA-TAG-80 | TC-FA-TAG-E2E-016 | FE+BE |
| TC-FA-TAG-81 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-82 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-83 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-84 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-85 | TC-FA-TAG-E2E-004 | FE+BE |
| TC-FA-TAG-86 | TC-FA-TAG-E2E-003 | FE+BE |
| TC-FA-TAG-87 | TC-FA-TAG-E2E-331 | FE+BE |
| TC-FA-TAG-88 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-89 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-90 | TC-FA-TAG-E2E-017 | FE+BE |
| TC-FA-TAG-91 | TC-FA-TAG-E2E-020 | FE+BE |
| TC-FA-TAG-92 | TC-FA-TAG-E2E-020 | FE+BE |
| TC-FA-TAG-93 | TC-FA-TAG-E2E-021 | FE+BE |
| TC-FA-TAG-94 | TC-FA-TAG-E2E-021 | FE+BE |
| TC-FA-TAG-95 | TC-FA-TAG-E2E-022 | FE+BE |
| TC-FA-TAG-96 | TC-FA-TAG-E2E-022 | FE+BE |
| TC-FA-TAG-97 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-98 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-99 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-100 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-101 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-102 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-103 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-104 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-105 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-106 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-107 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-108 | TC-FA-TAG-E2E-025 | FE+BE |
| TC-FA-TAG-109 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-110 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-111 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-112 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-113 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-114 | TC-FA-TAG-E2E-027 | FE+BE |
| TC-FA-TAG-115 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-116 | TC-FA-TAG-E2E-023 | FE+BE |
| TC-FA-TAG-117 | TC-FA-TAG-E2E-024 | FE+BE |
| TC-FA-TAG-118 | TC-FA-TAG-E2E-024 | FE+BE |
| TC-FA-TAG-119 | TC-FA-TAG-E2E-024 | FE+BE |
| TC-FA-TAG-120 | TC-FA-TAG-E2E-024 | FE+BE |
| TC-FA-TAG-121 | TC-FA-TAG-E2E-022 | FE+BE |
| TC-FA-TAG-122 | TC-FA-TAG-E2E-031 | FE+BE |
| TC-FA-TAG-123 | TC-FA-TAG-E2E-026 | FE+BE |
| TC-FA-TAG-124 | TC-FA-TAG-E2E-031 | FE+BE |
| TC-FA-TAG-125 | TC-FA-TAG-E2E-031 | FE+BE |
| TC-FA-TAG-126 | TC-FA-TAG-E2E-031 | FE+BE |
| TC-FA-TAG-127 | TC-FA-TAG-E2E-031 | FE+BE |
| TC-FA-TAG-128 | TC-FA-TAG-E2E-380 | FE+BE |
| TC-FA-TAG-129 | TC-FA-TAG-E2E-380 | FE+BE |
| TC-FA-TAG-130 | TC-FA-TAG-E2E-032 | FE+BE |
| TC-FA-TAG-131 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-132 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-133 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-134 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-135 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-136 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-137 | TC-FA-TAG-E2E-033 | FE+BE |
| TC-FA-TAG-138 | TC-FA-TAG-E2E-034 | FE+BE |
| TC-FA-TAG-139 | TC-FA-TAG-E2E-035 | FE+BE |
| TC-FA-TAG-140 | TC-FA-TAG-E2E-035 | FE+BE |
| TC-FA-TAG-141 | TC-FA-TAG-E2E-035 | FE+BE |
| TC-FA-TAG-142 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-143 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-144 | TC-FA-TAG-E2E-028 | FE+BE |
| TC-FA-TAG-145 | TC-FA-TAG-E2E-028 | FE+BE |
| TC-FA-TAG-146 | TC-FA-TAG-E2E-028 | FE+BE |
| TC-FA-TAG-147 | TC-FA-TAG-E2E-028 | FE+BE |
| TC-FA-TAG-148 | TC-FA-TAG-E2E-029 | FE+BE |
| TC-FA-TAG-149 | TC-FA-TAG-E2E-029 | FE+BE |
| TC-FA-TAG-150 | TC-FA-TAG-E2E-029 | FE+BE |
| TC-FA-TAG-151 | TC-FA-TAG-E2E-042 | FE+BE |
| TC-FA-TAG-152 | TC-FA-TAG-E2E-042 | FE+BE |
| TC-FA-TAG-153 | TC-FA-TAG-E2E-030 | FE+BE |
| TC-FA-TAG-154 | TC-FA-TAG-E2E-030 | FE+BE |
| TC-FA-TAG-155 | TC-FA-TAG-E2E-030 | FE+BE |
| TC-FA-TAG-156 | TC-FA-TAG-E2E-030 | FE+BE |
| TC-FA-TAG-157 | TC-FA-TAG-E2E-043 | FE+BE |
| TC-FA-TAG-158 | TC-FA-TAG-E2E-043 | FE+BE |
| TC-FA-TAG-159 | TC-FA-TAG-E2E-043 | FE+BE |
| TC-FA-TAG-160 | TC-FA-TAG-E2E-043 | FE+BE |
| TC-FA-TAG-161 | TC-FA-TAG-E2E-043 | FE+BE |
| TC-FA-TAG-162 | TC-FA-TAG-E2E-032 | FE+BE |
| TC-FA-TAG-163 | TC-FA-TAG-E2E-036 | FE+BE |
| TC-FA-TAG-164 | TC-FA-TAG-E2E-036 | FE+BE |
| TC-FA-TAG-165 | TC-FA-TAG-E2E-036 | FE+BE |
| TC-FA-TAG-166 | TC-FA-TAG-E2E-036 | FE+BE |
| TC-FA-TAG-167 | TC-FA-TAG-E2E-036 | FE+BE |
| TC-FA-TAG-168 | TC-FA-TAG-E2E-037 | FE+BE |
| TC-FA-TAG-169 | TC-FA-TAG-E2E-037 | FE+BE |
| TC-FA-TAG-170 | TC-FA-TAG-E2E-037 | FE+BE |
| TC-FA-TAG-171 | TC-FA-TAG-E2E-038 | FE+BE |
| TC-FA-TAG-172 | TC-FA-TAG-E2E-038 | FE+BE |
| TC-FA-TAG-173 | TC-FA-TAG-E2E-038 | FE+BE |
| TC-FA-TAG-174 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-175 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-176 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-177 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-178 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-179 | TC-FA-TAG-E2E-039 | FE+BE |
| TC-FA-TAG-180 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-181 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-182 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-183 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-184 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-185 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-186 | TC-FA-TAG-E2E-040 | FE+BE |
| TC-FA-TAG-187 | TC-FA-TAG-E2E-381 | FE+BE |
| TC-FA-TAG-188 | TC-FA-TAG-E2E-381 | FE+BE |
| TC-FA-TAG-189 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-190 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-191 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-192 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-193 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-194 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-195 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-196 | TC-FA-TAG-E2E-044 | FE+BE |
| TC-FA-TAG-197 | TC-FA-TAG-E2E-045 | FE+BE |
| TC-FA-TAG-198 | TC-FA-TAG-E2E-045 | FE+BE |
| TC-FA-TAG-199 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-200 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-201 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-202 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-203 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-204 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-205 | TC-FA-TAG-E2E-046 | FE+BE |
| TC-FA-TAG-206 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-207 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-208 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-209 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-210 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-211 | TC-FA-TAG-E2E-047 | FE+BE |
| TC-FA-TAG-212 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-213 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-214 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-215 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-216 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-217 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-218 | TC-FA-TAG-E2E-048 | FE+BE |
| TC-FA-TAG-219 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-220 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-221 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-222 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-223 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-224 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-225 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-226 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-227 | TC-FA-TAG-E2E-049 | FE+BE |
| TC-FA-TAG-228 | TC-FA-TAG-E2E-050 | FE+BE |
| TC-FA-TAG-229 | TC-FA-TAG-E2E-050 | FE+BE |
| TC-FA-TAG-230 | TC-FA-TAG-E2E-332 | FE+BE |
| TC-FA-TAG-231 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-232 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-233 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-234 | TC-FA-TAG-E2E-050 | FE+BE |
| TC-FA-TAG-235 | TC-FA-TAG-E2E-050 | FE+BE |
| TC-FA-TAG-236 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-237 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-238 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-239 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-240 | TC-FA-TAG-E2E-052 | FE+BE |
| TC-FA-TAG-241 | TC-FA-TAG-E2E-052 | FE+BE |
| TC-FA-TAG-242 | TC-FA-TAG-E2E-056 | FE+BE |
| TC-FA-TAG-243 | TC-FA-TAG-E2E-056 | FE+BE |
| TC-FA-TAG-244 | TC-FA-TAG-E2E-052 | FE+BE |
| TC-FA-TAG-245 | TC-FA-TAG-E2E-345 | FE+BE |
| TC-FA-TAG-246 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-247 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-248 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-249 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-250 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-251 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-252 | TC-FA-TAG-E2E-054 | FE+BE |
| TC-FA-TAG-253 | TC-FA-TAG-E2E-055 | FE+BE |
| TC-FA-TAG-254 | TC-FA-TAG-E2E-055 | FE+BE |
| TC-FA-TAG-255 | TC-FA-TAG-E2E-055 | FE+BE |
| TC-FA-TAG-256 | TC-FA-TAG-E2E-055 | FE+BE |
| TC-FA-TAG-257 | TC-FA-TAG-E2E-342 | FE+BE |
| TC-FA-TAG-258 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-259 | TC-FA-TAG-E2E-333 | FE+BE |
| TC-FA-TAG-260 | TC-FA-TAG-E2E-333 | FE+BE |
| TC-FA-TAG-261 | TC-FA-TAG-E2E-056 | FE+BE |
| TC-FA-TAG-262 | TC-FA-TAG-E2E-052 | FE+BE |
| TC-FA-TAG-263 | TC-FA-TAG-E2E-345 | FE+BE |
| TC-FA-TAG-264 | TC-FA-TAG-E2E-055 | FE+BE |
| TC-FA-TAG-265 | TC-FA-TAG-E2E-051 | FE+BE |
| TC-FA-TAG-266 | TC-FA-TAG-E2E-058 | FE+BE |
| TC-FA-TAG-267 | TC-FA-TAG-E2E-058 | FE+BE |
| TC-FA-TAG-268 | TC-FA-TAG-E2E-058 | FE+BE |
| TC-FA-TAG-269 | TC-FA-TAG-E2E-058 | FE+BE |
| TC-FA-TAG-270 | TC-FA-TAG-E2E-058 | FE+BE |
| TC-FA-TAG-271 | TC-FA-TAG-E2E-059 | FE+BE |
| TC-FA-TAG-272 | TC-FA-TAG-E2E-059 | FE+BE |
| TC-FA-TAG-273 | TC-FA-TAG-E2E-059 | FE+BE |
| TC-FA-TAG-274 | TC-FA-TAG-E2E-059 | FE+BE |
| TC-FA-TAG-275 | TC-FA-TAG-E2E-059 | FE+BE |
| TC-FA-TAG-276 | TC-FA-TAG-E2E-061 | FE+BE |
| TC-FA-TAG-277 | TC-FA-TAG-E2E-061 | FE+BE |
| TC-FA-TAG-278 | TC-FA-TAG-E2E-061 | FE+BE |
| TC-FA-TAG-279 | TC-FA-TAG-E2E-061 | FE+BE |
| TC-FA-TAG-280 | TC-FA-TAG-E2E-061 | FE+BE |
| TC-FA-TAG-281 | TC-FA-TAG-E2E-062 | FE+BE |
| TC-FA-TAG-282 | TC-FA-TAG-E2E-062 | FE+BE |
| TC-FA-TAG-283 | TC-FA-TAG-E2E-063 | FE+BE |
| TC-FA-TAG-284 | TC-FA-TAG-E2E-063 | FE+BE |
| TC-FA-TAG-285 | TC-FA-TAG-E2E-063 | FE+BE |
| TC-FA-TAG-286 | TC-FA-TAG-E2E-063 | FE+BE |
| TC-FA-TAG-287 | TC-FA-TAG-E2E-063 | FE+BE |
| TC-FA-TAG-288 | TC-FA-TAG-E2E-064 | FE+BE |
| TC-FA-TAG-289 | TC-FA-TAG-E2E-064 | FE+BE |
| TC-FA-TAG-290 | TC-FA-TAG-E2E-064 | FE+BE |
| TC-FA-TAG-291 | TC-FA-TAG-E2E-064 | FE+BE |
| TC-FA-TAG-292 | TC-FA-TAG-E2E-064 | FE+BE |
| TC-FA-TAG-293 | TC-FA-TAG-E2E-065 | FE+BE |
| TC-FA-TAG-294 | TC-FA-TAG-E2E-065 | FE+BE |
| TC-FA-TAG-295 | TC-FA-TAG-E2E-065 | FE+BE |
| TC-FA-TAG-296 | TC-FA-TAG-E2E-065 | FE+BE |
| TC-FA-TAG-297 | TC-FA-TAG-E2E-065 | FE+BE |
| TC-FA-TAG-298 | TC-FA-TAG-E2E-066 | FE+BE |
| TC-FA-TAG-299 | TC-FA-TAG-E2E-066 | FE+BE |
| TC-FA-TAG-300 | TC-FA-TAG-E2E-066 | FE+BE |
| TC-FA-TAG-301 | TC-FA-TAG-E2E-066 | FE+BE |
| TC-FA-TAG-302 | TC-FA-TAG-E2E-066 | FE+BE |
| TC-FA-TAG-303 | TC-FA-TAG-E2E-067 | FE+BE |
| TC-FA-TAG-304 | TC-FA-TAG-E2E-067 | FE+BE |
| TC-FA-TAG-305 | TC-FA-TAG-E2E-067 | FE+BE |
| TC-FA-TAG-306 | TC-FA-TAG-E2E-067 | FE+BE |
| TC-FA-TAG-307 | TC-FA-TAG-E2E-347 | FE+BE |
| TC-FA-TAG-308 | TC-FA-TAG-E2E-347 | FE+BE |
| TC-FA-TAG-309 | TC-FA-TAG-E2E-068 | FE+BE |
| TC-FA-TAG-310 | TC-FA-TAG-E2E-068 | FE+BE |
| TC-FA-TAG-311 | TC-FA-TAG-E2E-068 | FE+BE |
| TC-FA-TAG-312 | TC-FA-TAG-E2E-068 | FE+BE |
| TC-FA-TAG-313 | TC-FA-TAG-E2E-069 | FE+BE |
| TC-FA-TAG-314 | TC-FA-TAG-E2E-069 | FE+BE |
| TC-FA-TAG-315 | TC-FA-TAG-E2E-069 | FE+BE |
| TC-FA-TAG-316 | TC-FA-TAG-E2E-069 | FE+BE |
| TC-FA-TAG-317 | TC-FA-TAG-E2E-070 | FE+BE |
| TC-FA-TAG-318 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-319 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-320 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-321 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-322 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-323 | TC-FA-TAG-E2E-369 | FE+BE |
| TC-FA-TAG-324 | TC-FA-TAG-E2E-071 | FE+BE |
| TC-FA-TAG-325 | TC-FA-TAG-E2E-071 | FE+BE |
| TC-FA-TAG-326 | TC-FA-TAG-E2E-071 | FE+BE |
| TC-FA-TAG-327 | TC-FA-TAG-E2E-075 | FE+BE |
| TC-FA-TAG-328 | TC-FA-TAG-E2E-075 | FE+BE |
| TC-FA-TAG-329 | TC-FA-TAG-E2E-075 | FE+BE |
| TC-FA-TAG-330 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-331 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-332 | TC-FA-TAG-E2E-073 | FE+BE |
| TC-FA-TAG-333 | TC-FA-TAG-E2E-073 | FE+BE |
| TC-FA-TAG-334 | TC-FA-TAG-E2E-073 | FE+BE |
| TC-FA-TAG-335 | TC-FA-TAG-E2E-073 | FE+BE |
| TC-FA-TAG-336 | TC-FA-TAG-E2E-074 | FE+BE |
| TC-FA-TAG-337 | TC-FA-TAG-E2E-074 | FE+BE |
| TC-FA-TAG-338 | TC-FA-TAG-E2E-074 | FE+BE |
| TC-FA-TAG-339 | TC-FA-TAG-E2E-074 | FE+BE |
| TC-FA-TAG-340 | TC-FA-TAG-E2E-072 | FE+BE |
| TC-FA-TAG-341 | TC-FA-TAG-E2E-075 | FE+BE |
| TC-FA-TAG-342 | TC-FA-TAG-E2E-076 | FE+BE |
| TC-FA-TAG-343 | TC-FA-TAG-E2E-076 | FE+BE |
| TC-FA-TAG-344 | TC-FA-TAG-E2E-076 | FE+BE |
| TC-FA-TAG-345 | TC-FA-TAG-E2E-077 | FE+BE |
| TC-FA-TAG-346 | TC-FA-TAG-E2E-077 | FE+BE |
| TC-FA-TAG-347 | TC-FA-TAG-E2E-077 | FE+BE |
| TC-FA-TAG-348 | TC-FA-TAG-E2E-079 | FE+BE |
| TC-FA-TAG-349 | TC-FA-TAG-E2E-079 | FE+BE |
| TC-FA-TAG-350 | TC-FA-TAG-E2E-078 | FE+BE |
| TC-FA-TAG-351 | TC-FA-TAG-E2E-078 | FE+BE |
| TC-FA-TAG-352 | TC-FA-TAG-E2E-078 | FE+BE |
| TC-FA-TAG-353 | TC-FA-TAG-E2E-078 | FE+BE |
| TC-FA-TAG-354 | TC-FA-TAG-E2E-079 | FE+BE |
| TC-FA-TAG-355 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-356 | TC-FA-TAG-E2E-081 | FE+BE |
| TC-FA-TAG-357 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-358 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-359 | TC-FA-TAG-E2E-081 | FE+BE |
| TC-FA-TAG-360 | TC-FA-TAG-E2E-081 | FE+BE |
| TC-FA-TAG-361 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-362 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-363 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-364 | TC-FA-TAG-E2E-082 | FE+BE |
| TC-FA-TAG-365 | TC-FA-TAG-E2E-347 | FE+BE |
| TC-FA-TAG-366 | TC-FA-TAG-E2E-083 | FE+BE |
| TC-FA-TAG-367 | TC-FA-TAG-E2E-382 | FE+BE |
| TC-FA-TAG-368 | TC-FA-TAG-E2E-382 | FE+BE |
| TC-FA-TAG-369 | TC-FA-TAG-E2E-083 | FE+BE |
| TC-FA-TAG-370 | TC-FA-TAG-E2E-083 | FE+BE |
| TC-FA-TAG-371 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-372 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-373 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-374 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-375 | TC-FA-TAG-E2E-345 | FE+BE |
| TC-FA-TAG-376 | TC-FA-TAG-E2E-346 | FE+BE |
| TC-FA-TAG-377 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-378 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-379 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-380 | TC-FA-TAG-E2E-086 | FE+BE |
| TC-FA-TAG-381 | TC-FA-TAG-E2E-087 | FE+BE |
| TC-FA-TAG-382 | TC-FA-TAG-E2E-087 | FE+BE |
| TC-FA-TAG-383 | TC-FA-TAG-E2E-346 | FE+BE |
| TC-FA-TAG-384 | TC-FA-TAG-E2E-087 | FE+BE |
| TC-FA-TAG-385 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-386 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-387 | TC-FA-TAG-E2E-088 | FE+BE |
| TC-FA-TAG-388 | TC-FA-TAG-E2E-089 | FE+BE |
| TC-FA-TAG-389 | TC-FA-TAG-E2E-089 | FE+BE |
| TC-FA-TAG-390 | TC-FA-TAG-E2E-089 | FE+BE |
| TC-FA-TAG-391 | TC-FA-TAG-E2E-089 | FE+BE |
| TC-FA-TAG-392 | TC-FA-TAG-E2E-090 | FE+BE |
| TC-FA-TAG-393 | TC-FA-TAG-E2E-090 | FE+BE |
| TC-FA-TAG-394 | TC-FA-TAG-E2E-090 | FE+BE |
| TC-FA-TAG-395 | TC-FA-TAG-E2E-091 | FE+BE |
| TC-FA-TAG-396 | TC-FA-TAG-E2E-091 | FE+BE |
| TC-FA-TAG-397 | TC-FA-TAG-E2E-091 | FE+BE |
| TC-FA-TAG-398 | TC-FA-TAG-E2E-092 | FE+BE |
| TC-FA-TAG-399 | TC-FA-TAG-E2E-092 | FE+BE |
| TC-FA-TAG-400 | TC-FA-TAG-E2E-093 | FE+BE |
| TC-FA-TAG-401 | TC-FA-TAG-E2E-093 | FE+BE |
| TC-FA-TAG-402 | TC-FA-TAG-E2E-093 | FE+BE |
| TC-FA-TAG-403 | TC-FA-TAG-E2E-093 | FE+BE |
| TC-FA-TAG-404 | TC-FA-TAG-E2E-094 | FE+BE |
| TC-FA-TAG-405 | TC-FA-TAG-E2E-336 | FE+BE |
| TC-FA-TAG-406 | TC-FA-TAG-E2E-336 | FE+BE |
| TC-FA-TAG-407 | TC-FA-TAG-E2E-336 | FE+BE |
| TC-FA-TAG-408 | TC-FA-TAG-E2E-094 | FE+BE |
| TC-FA-TAG-409 | TC-FA-TAG-E2E-094 | FE+BE |
| TC-FA-TAG-410 | TC-FA-TAG-E2E-095 | FE+BE |
| TC-FA-TAG-411 | TC-FA-TAG-E2E-096 | FE+BE |
| TC-FA-TAG-412 | TC-FA-TAG-E2E-096 | FE+BE |
| TC-FA-TAG-413 | TC-FA-TAG-E2E-096 | FE+BE |
| TC-FA-TAG-414 | TC-FA-TAG-E2E-096 | FE+BE |
| TC-FA-TAG-415 | TC-FA-TAG-E2E-097 | FE+BE |
| TC-FA-TAG-416 | TC-FA-TAG-E2E-097 | FE+BE |
| TC-FA-TAG-417 | TC-FA-TAG-E2E-097 | FE+BE |
| TC-FA-TAG-418 | TC-FA-TAG-E2E-097 | FE+BE |
| TC-FA-TAG-419 | TC-FA-TAG-E2E-098 | FE+BE |
| TC-FA-TAG-420 | TC-FA-TAG-E2E-098 | FE+BE |
| TC-FA-TAG-421 | TC-FA-TAG-E2E-098 | FE+BE |
| TC-FA-TAG-422 | TC-FA-TAG-E2E-098 | FE+BE |
| TC-FA-TAG-423 | TC-FA-TAG-E2E-098 | FE+BE |
| TC-FA-TAG-424 | TC-FA-TAG-E2E-099 | FE+BE |
| TC-FA-TAG-425 | TC-FA-TAG-E2E-384 | FE+BE |
| TC-FA-TAG-426 | TC-FA-TAG-E2E-099 | FE+BE |
| TC-FA-TAG-427 | TC-FA-TAG-E2E-099 | FE+BE |
| TC-FA-TAG-428 | TC-FA-TAG-E2E-099 | FE+BE |
| TC-FA-TAG-429 | TC-FA-TAG-E2E-099 | FE+BE |
| TC-FA-TAG-430 | TC-FA-TAG-E2E-100 | FE+BE |
| TC-FA-TAG-431 | TC-FA-TAG-E2E-100 | FE+BE |
| TC-FA-TAG-432 | TC-FA-TAG-E2E-100 | FE+BE |
| TC-FA-TAG-433 | TC-FA-TAG-E2E-100 | FE+BE |
| TC-FA-TAG-434 | TC-FA-TAG-E2E-100 | FE+BE |
| TC-FA-TAG-435 | TC-FA-TAG-E2E-102 | FE+BE |
| TC-FA-TAG-436 | TC-FA-TAG-E2E-102 | FE+BE |
| TC-FA-TAG-437 | TC-FA-TAG-E2E-102 | FE+BE |
| TC-FA-TAG-438 | TC-FA-TAG-E2E-102 | FE+BE |
| TC-FA-TAG-439 | TC-FA-TAG-E2E-102 | FE+BE |
| TC-FA-TAG-440 | TC-FA-TAG-E2E-103 | FE+BE |
| TC-FA-TAG-441 | TC-FA-TAG-E2E-103 | FE+BE |
| TC-FA-TAG-442 | TC-FA-TAG-E2E-103 | FE+BE |
| TC-FA-TAG-443 | TC-FA-TAG-E2E-103 | FE+BE |
| TC-FA-TAG-444 | TC-FA-TAG-E2E-104 | FE+BE |
| TC-FA-TAG-445 | TC-FA-TAG-E2E-104 | FE+BE |
| TC-FA-TAG-446 | TC-FA-TAG-E2E-104 | FE+BE |
| TC-FA-TAG-447 | TC-FA-TAG-E2E-104 | FE+BE |
| TC-FA-TAG-448 | TC-FA-TAG-E2E-105 | FE+BE |
| TC-FA-TAG-449 | TC-FA-TAG-E2E-106 | FE+BE |
| TC-FA-TAG-450 | TC-FA-TAG-E2E-106 | FE+BE |
| TC-FA-TAG-451 | TC-FA-TAG-E2E-106 | FE+BE |
| TC-FA-TAG-452 | TC-FA-TAG-E2E-106 | FE+BE |
| TC-FA-TAG-453 | TC-FA-TAG-E2E-116 | FE+BE |
| TC-FA-TAG-454 | TC-FA-TAG-E2E-107 | FE+BE |
| TC-FA-TAG-455 | TC-FA-TAG-E2E-107 | FE+BE |
| TC-FA-TAG-456 | TC-FA-TAG-E2E-107 | FE+BE |
| TC-FA-TAG-457 | TC-FA-TAG-E2E-107 | FE+BE |
| TC-FA-TAG-458 | TC-FA-TAG-E2E-107 | FE+BE |
| TC-FA-TAG-459 | TC-FA-TAG-E2E-110 | FE+BE |
| TC-FA-TAG-460 | TC-FA-TAG-E2E-110 | FE+BE |
| TC-FA-TAG-461 | TC-FA-TAG-E2E-110 | FE+BE |
| TC-FA-TAG-462 | TC-FA-TAG-E2E-111 | FE+BE |
| TC-FA-TAG-463 | TC-FA-TAG-E2E-111 | FE+BE |
| TC-FA-TAG-464 | TC-FA-TAG-E2E-112 | FE+BE |
| TC-FA-TAG-465 | TC-FA-TAG-E2E-112 | FE+BE |
| TC-FA-TAG-466 | TC-FA-TAG-E2E-113 | FE+BE |
| TC-FA-TAG-467 | TC-FA-TAG-E2E-337 | FE+BE |
| TC-FA-TAG-468 | TC-FA-TAG-E2E-337 | FE+BE |
| TC-FA-TAG-469 | TC-FA-TAG-E2E-113 | FE+BE |
| TC-FA-TAG-470 | TC-FA-TAG-E2E-113 | FE+BE |
| TC-FA-TAG-471 | TC-FA-TAG-E2E-114 | FE+BE |
| TC-FA-TAG-472 | TC-FA-TAG-E2E-114 | FE+BE |
| TC-FA-TAG-473 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-474 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-475 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-476 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-477 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-478 | TC-FA-TAG-E2E-118 | FE+BE |
| TC-FA-TAG-479 | TC-FA-TAG-E2E-119 | FE+BE |
| TC-FA-TAG-480 | TC-FA-TAG-E2E-119 | FE+BE |
| TC-FA-TAG-481 | TC-FA-TAG-E2E-119 | FE+BE |
| TC-FA-TAG-482 | TC-FA-TAG-E2E-120 | FE+BE |
| TC-FA-TAG-483 | TC-FA-TAG-E2E-120 | FE+BE |
| TC-FA-TAG-484 | TC-FA-TAG-E2E-120 | FE+BE |
| TC-FA-TAG-485 | TC-FA-TAG-E2E-120 | FE+BE |
| TC-FA-TAG-486 | TC-FA-TAG-E2E-120 | FE+BE |
| TC-FA-TAG-487 | TC-FA-TAG-E2E-121 | FE+BE |
| TC-FA-TAG-488 | TC-FA-TAG-E2E-121 | FE+BE |
| TC-FA-TAG-489 | TC-FA-TAG-E2E-121 | FE+BE |
| TC-FA-TAG-490 | TC-FA-TAG-E2E-122 | FE+BE |
| TC-FA-TAG-491 | TC-FA-TAG-E2E-122 | FE+BE |
| TC-FA-TAG-492 | TC-FA-TAG-E2E-122 | FE+BE |
| TC-FA-TAG-493 | TC-FA-TAG-E2E-122 | FE+BE |
| TC-FA-TAG-494 | TC-FA-TAG-E2E-342 | FE+BE |
| TC-FA-TAG-495 | TC-FA-TAG-E2E-338 | FE+BE |
| TC-FA-TAG-496 | TC-FA-TAG-E2E-338 | FE+BE |
| TC-FA-TAG-497 | TC-FA-TAG-E2E-338 | FE+BE |
| TC-FA-TAG-498 | TC-FA-TAG-E2E-123 | FE+BE |
| TC-FA-TAG-499 | TC-FA-TAG-E2E-124 | FE+BE |
| TC-FA-TAG-500 | TC-FA-TAG-E2E-124 | FE+BE |
| TC-FA-TAG-501 | TC-FA-TAG-E2E-124 | FE+BE |
| TC-FA-TAG-502 | TC-FA-TAG-E2E-124 | FE+BE |
| TC-FA-TAG-503 | TC-FA-TAG-E2E-125 | FE+BE |
| TC-FA-TAG-504 | TC-FA-TAG-E2E-140 | FE+BE |
| TC-FA-TAG-505 | TC-FA-TAG-E2E-125 | FE+BE |
| TC-FA-TAG-506 | TC-FA-TAG-E2E-125 | FE+BE |
| TC-FA-TAG-507 | TC-FA-TAG-E2E-126 | FE+BE |
| TC-FA-TAG-508 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-509 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-510 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-511 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-512 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-513 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-514 | TC-FA-TAG-E2E-358 | FE+BE |
| TC-FA-TAG-515 | TC-FA-TAG-E2E-359 | FE+BE |
| TC-FA-TAG-516 | TC-FA-TAG-E2E-359 | FE+BE |
| TC-FA-TAG-517 | TC-FA-TAG-E2E-359 | FE+BE |
| TC-FA-TAG-518 | TC-FA-TAG-E2E-359 | FE+BE |
| TC-FA-TAG-519 | TC-FA-TAG-E2E-359 | FE+BE |
| TC-FA-TAG-520 | TC-FA-TAG-E2E-360 | FE+BE |
| TC-FA-TAG-521 | TC-FA-TAG-E2E-360 | FE+BE |
| TC-FA-TAG-522 | TC-FA-TAG-E2E-360 | FE+BE |
| TC-FA-TAG-523 | TC-FA-TAG-E2E-360 | FE+BE |
| TC-FA-TAG-524 | TC-FA-TAG-E2E-361 | FE+BE |
| TC-FA-TAG-525 | TC-FA-TAG-E2E-361 | FE+BE |
| TC-FA-TAG-526 | TC-FA-TAG-E2E-361 | FE+BE |
| TC-FA-TAG-527 | TC-FA-TAG-E2E-361 | FE+BE |
| TC-FA-TAG-528 | TC-FA-TAG-E2E-361 | FE+BE |
| TC-FA-TAG-529 | TC-FA-TAG-E2E-362 | FE+BE |
| TC-FA-TAG-530 | TC-FA-TAG-E2E-362 | FE+BE |
| TC-FA-TAG-531 | TC-FA-TAG-E2E-127 | FE+BE |
| TC-FA-TAG-532 | TC-FA-TAG-E2E-127 | FE+BE |
| TC-FA-TAG-533 | TC-FA-TAG-E2E-127 | FE+BE |
| TC-FA-TAG-534 | TC-FA-TAG-E2E-127 | FE+BE |
| TC-FA-TAG-535 | TC-FA-TAG-E2E-127 | FE+BE |
| TC-FA-TAG-536 | TC-FA-TAG-E2E-128 | FE+BE |
| TC-FA-TAG-537 | TC-FA-TAG-E2E-128 | FE+BE |
| TC-FA-TAG-538 | TC-FA-TAG-E2E-128 | FE+BE |
| TC-FA-TAG-539 | TC-FA-TAG-E2E-129 | FE+BE |
| TC-FA-TAG-540 | TC-FA-TAG-E2E-129 | FE+BE |
| TC-FA-TAG-541 | TC-FA-TAG-E2E-129 | FE+BE |
| TC-FA-TAG-542 | TC-FA-TAG-E2E-129 | FE+BE |
| TC-FA-TAG-543 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-544 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-545 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-546 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-547 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-548 | TC-FA-TAG-E2E-131 | FE+BE |
| TC-FA-TAG-549 | TC-FA-TAG-E2E-132 | FE+BE |
| TC-FA-TAG-550 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-551 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-552 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-553 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-554 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-555 | TC-FA-TAG-E2E-363 | FE+BE |
| TC-FA-TAG-556 | TC-FA-TAG-E2E-364 | FE+BE |
| TC-FA-TAG-557 | TC-FA-TAG-E2E-364 | FE+BE |
| TC-FA-TAG-558 | TC-FA-TAG-E2E-364 | FE+BE |
| TC-FA-TAG-559 | TC-FA-TAG-E2E-364 | FE+BE |
| TC-FA-TAG-560 | TC-FA-TAG-E2E-364 | FE+BE |
| TC-FA-TAG-561 | TC-FA-TAG-E2E-365 | FE+BE |
| TC-FA-TAG-562 | TC-FA-TAG-E2E-365 | FE+BE |
| TC-FA-TAG-563 | TC-FA-TAG-E2E-339 | FE+BE |
| TC-FA-TAG-564 | TC-FA-TAG-E2E-339 | FE+BE |
| TC-FA-TAG-565 | TC-FA-TAG-E2E-339 | FE+BE |
| TC-FA-TAG-566 | TC-FA-TAG-E2E-342 | FE+BE |
| TC-FA-TAG-567 | TC-FA-TAG-E2E-133 | FE+BE |
| TC-FA-TAG-568 | TC-FA-TAG-E2E-133 | FE+BE |
| TC-FA-TAG-569 | TC-FA-TAG-E2E-141 | FE+BE |
| TC-FA-TAG-570 | TC-FA-TAG-E2E-370 | FE+BE |
| TC-FA-TAG-571 | TC-FA-TAG-E2E-370 | FE+BE |
| TC-FA-TAG-572 | TC-FA-TAG-E2E-370 | FE+BE |
| TC-FA-TAG-573 | TC-FA-TAG-E2E-135 | FE+BE |
| TC-FA-TAG-574 | TC-FA-TAG-E2E-135 | FE+BE |
| TC-FA-TAG-575 | TC-FA-TAG-E2E-135 | FE+BE |
| TC-FA-TAG-576 | TC-FA-TAG-E2E-135 | FE+BE |
| TC-FA-TAG-577 | TC-FA-TAG-E2E-135 | FE+BE |
| TC-FA-TAG-578 | TC-FA-TAG-E2E-136 | FE+BE |
| TC-FA-TAG-579 | TC-FA-TAG-E2E-136 | FE+BE |
| TC-FA-TAG-580 | TC-FA-TAG-E2E-136 | FE+BE |
| TC-FA-TAG-581 | TC-FA-TAG-E2E-136 | FE+BE |
| TC-FA-TAG-582 | TC-FA-TAG-E2E-137 | FE+BE |
| TC-FA-TAG-583 | TC-FA-TAG-E2E-340 | FE+BE |
| TC-FA-TAG-584 | TC-FA-TAG-E2E-340 | FE+BE |
| TC-FA-TAG-585 | TC-FA-TAG-E2E-340 | FE+BE |
| TC-FA-TAG-586 | TC-FA-TAG-E2E-137 | FE+BE |
| TC-FA-TAG-587 | TC-FA-TAG-E2E-383 | FE+BE |
| TC-FA-TAG-588 | TC-FA-TAG-E2E-137 | FE+BE |
| TC-FA-TAG-589 | TC-FA-TAG-E2E-137 | FE+BE |
| TC-FA-TAG-590 | TC-FA-TAG-E2E-137 | FE+BE |
| TC-FA-TAG-591 | TC-FA-TAG-E2E-138 | FE+BE |
| TC-FA-TAG-592 | TC-FA-TAG-E2E-138 | FE+BE |
| TC-FA-TAG-593 | TC-FA-TAG-E2E-138 | FE+BE |
| TC-FA-TAG-594 | TC-FA-TAG-E2E-138 | FE+BE |
| TC-FA-TAG-595 | TC-FA-TAG-E2E-139 | FE+BE |
| TC-FA-TAG-596 | TC-FA-TAG-E2E-139 | FE+BE |
| TC-FA-TAG-597 | TC-FA-TAG-E2E-370 | FE+BE |
| TC-FA-TAG-598 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-599 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-600 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-601 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-602 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-603 | TC-FA-TAG-E2E-142 | FE+BE |
| TC-FA-TAG-604 | TC-FA-TAG-E2E-143 | FE+BE |
| TC-FA-TAG-605 | TC-FA-TAG-E2E-144 | FE+BE |
| TC-FA-TAG-606 | TC-FA-TAG-E2E-144 | FE+BE |
| TC-FA-TAG-607 | TC-FA-TAG-E2E-144 | FE+BE |
| TC-FA-TAG-608 | TC-FA-TAG-E2E-144 | FE+BE |
| TC-FA-TAG-609 | TC-FA-TAG-E2E-145 | FE+BE |
| TC-FA-TAG-610 | TC-FA-TAG-E2E-145 | FE+BE |
| TC-FA-TAG-611 | TC-FA-TAG-E2E-145 | FE+BE |
| TC-FA-TAG-612 | TC-FA-TAG-E2E-145 | FE+BE |
| TC-FA-TAG-613 | TC-FA-TAG-E2E-146 | FE+BE |
| TC-FA-TAG-614 | TC-FA-TAG-E2E-146 | FE+BE |
| TC-FA-TAG-615 | TC-FA-TAG-E2E-146 | FE+BE |
| TC-FA-TAG-616 | TC-FA-TAG-E2E-146 | FE+BE |
| TC-FA-TAG-617 | TC-FA-TAG-E2E-341 | FE+BE |
| TC-FA-TAG-618 | TC-FA-TAG-E2E-147 | FE+BE |
| TC-FA-TAG-619 | TC-FA-TAG-E2E-351 | FE+BE |
| TC-FA-TAG-620 | TC-FA-TAG-E2E-147 | FE+BE |
| TC-FA-TAG-621 | TC-FA-TAG-E2E-147 | FE+BE |
| TC-FA-TAG-622 | TC-FA-TAG-E2E-148 | FE+BE |
| TC-FA-TAG-623 | TC-FA-TAG-E2E-148 | FE+BE |
| TC-FA-TAG-624 | TC-FA-TAG-E2E-148 | FE+BE |
| TC-FA-TAG-625 | TC-FA-TAG-E2E-148 | FE+BE |
| TC-FA-TAG-626 | TC-FA-TAG-E2E-148 | FE+BE |
| TC-FA-TAG-627 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-628 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-629 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-630 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-631 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-632 | TC-FA-TAG-E2E-149 | FE+BE |
| TC-FA-TAG-633 | TC-FA-TAG-E2E-150 | FE+BE |
| TC-FA-TAG-634 | TC-FA-TAG-E2E-150 | FE+BE |
| TC-FA-TAG-635 | TC-FA-TAG-E2E-371 | FE+BE |
| TC-FA-TAG-636 | TC-FA-TAG-E2E-151 | FE+BE |
| TC-FA-TAG-637 | TC-FA-TAG-E2E-151 | FE+BE |
| TC-FA-TAG-638 | TC-FA-TAG-E2E-151 | FE+BE |
| TC-FA-TAG-639 | TC-FA-TAG-E2E-151 | FE+BE |
| TC-FA-TAG-640 | TC-FA-TAG-E2E-152 | FE+BE |
| TC-FA-TAG-641 | TC-FA-TAG-E2E-153 | FE+BE |
| TC-FA-TAG-642 | TC-FA-TAG-E2E-153 | FE+BE |
| TC-FA-TAG-643 | TC-FA-TAG-E2E-153 | FE+BE |
| TC-FA-TAG-644 | TC-FA-TAG-E2E-169 | FE+BE |
| TC-FA-TAG-645 | TC-FA-TAG-E2E-341 | FE+BE |
| TC-FA-TAG-646 | TC-FA-TAG-E2E-343 | FE+BE |
| TC-FA-TAG-647 | TC-FA-TAG-E2E-155 | FE+BE |
| TC-FA-TAG-648 | TC-FA-TAG-E2E-155 | FE+BE |
| TC-FA-TAG-649 | TC-FA-TAG-E2E-155 | FE+BE |
| TC-FA-TAG-650 | TC-FA-TAG-E2E-155 | FE+BE |
| TC-FA-TAG-651 | TC-FA-TAG-E2E-156 | FE+BE |
| TC-FA-TAG-652 | TC-FA-TAG-E2E-156 | FE+BE |
| TC-FA-TAG-653 | TC-FA-TAG-E2E-156 | FE+BE |
| TC-FA-TAG-654 | TC-FA-TAG-E2E-156 | FE+BE |
| TC-FA-TAG-655 | TC-FA-TAG-E2E-157 | FE+BE |
| TC-FA-TAG-656 | TC-FA-TAG-E2E-157 | FE+BE |
| TC-FA-TAG-657 | TC-FA-TAG-E2E-157 | FE+BE |
| TC-FA-TAG-658 | TC-FA-TAG-E2E-158 | FE+BE |
| TC-FA-TAG-659 | TC-FA-TAG-E2E-158 | FE+BE |
| TC-FA-TAG-660 | TC-FA-TAG-E2E-158 | FE+BE |
| TC-FA-TAG-661 | TC-FA-TAG-E2E-158 | FE+BE |
| TC-FA-TAG-662 | TC-FA-TAG-E2E-159 | FE+BE |
| TC-FA-TAG-663 | TC-FA-TAG-E2E-159 | FE+BE |
| TC-FA-TAG-664 | TC-FA-TAG-E2E-159 | FE+BE |
| TC-FA-TAG-665 | TC-FA-TAG-E2E-159 | FE+BE |
| TC-FA-TAG-666 | TC-FA-TAG-E2E-159 | FE+BE |
| TC-FA-TAG-667 | TC-FA-TAG-E2E-160 | FE+BE |
| TC-FA-TAG-668 | TC-FA-TAG-E2E-341 | FE+BE |
| TC-FA-TAG-669 | TC-FA-TAG-E2E-351 | FE+BE |
| TC-FA-TAG-670 | TC-FA-TAG-E2E-160 | FE+BE |
| TC-FA-TAG-671 | TC-FA-TAG-E2E-161 | FE+BE |
| TC-FA-TAG-672 | TC-FA-TAG-E2E-161 | FE+BE |
| TC-FA-TAG-673 | TC-FA-TAG-E2E-161 | FE+BE |
| TC-FA-TAG-674 | TC-FA-TAG-E2E-161 | FE+BE |
| TC-FA-TAG-675 | TC-FA-TAG-E2E-161 | FE+BE |
| TC-FA-TAG-676 | TC-FA-TAG-E2E-162 | FE+BE |
| TC-FA-TAG-677 | TC-FA-TAG-E2E-162 | FE+BE |
| TC-FA-TAG-678 | TC-FA-TAG-E2E-162 | FE+BE |
| TC-FA-TAG-679 | TC-FA-TAG-E2E-162 | FE+BE |
| TC-FA-TAG-680 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-681 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-682 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-683 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-684 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-685 | TC-FA-TAG-E2E-170 | FE+BE |
| TC-FA-TAG-686 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-687 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-688 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-689 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-690 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-691 | TC-FA-TAG-E2E-171 | FE+BE |
| TC-FA-TAG-692 | TC-FA-TAG-E2E-172 | FE+BE |
| TC-FA-TAG-693 | TC-FA-TAG-E2E-172 | FE+BE |
| TC-FA-TAG-694 | TC-FA-TAG-E2E-172 | FE+BE |
| TC-FA-TAG-695 | TC-FA-TAG-E2E-172 | FE+BE |
| TC-FA-TAG-696 | TC-FA-TAG-E2E-172 | FE+BE |
| TC-FA-TAG-697 | TC-FA-TAG-E2E-191 | FE+BE |
| TC-FA-TAG-698 | TC-FA-TAG-E2E-173 | FE+BE |
| TC-FA-TAG-699 | TC-FA-TAG-E2E-173 | FE+BE |
| TC-FA-TAG-700 | TC-FA-TAG-E2E-173 | FE+BE |
| TC-FA-TAG-701 | TC-FA-TAG-E2E-173 | FE+BE |
| TC-FA-TAG-702 | TC-FA-TAG-E2E-174 | FE+BE |
| TC-FA-TAG-703 | TC-FA-TAG-E2E-174 | FE+BE |
| TC-FA-TAG-704 | TC-FA-TAG-E2E-174 | FE+BE |
| TC-FA-TAG-705 | TC-FA-TAG-E2E-174 | FE+BE |
| TC-FA-TAG-706 | TC-FA-TAG-E2E-174 | FE+BE |
| TC-FA-TAG-707 | TC-FA-TAG-E2E-175 | FE+BE |
| TC-FA-TAG-708 | TC-FA-TAG-E2E-175 | FE+BE |
| TC-FA-TAG-709 | TC-FA-TAG-E2E-175 | FE+BE |
| TC-FA-TAG-710 | TC-FA-TAG-E2E-175 | FE+BE |
| TC-FA-TAG-711 | TC-FA-TAG-E2E-175 | FE+BE |
| TC-FA-TAG-712 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-713 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-714 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-715 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-716 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-717 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-718 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-719 | TC-FA-TAG-E2E-176 | FE+BE |
| TC-FA-TAG-720 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-721 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-722 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-723 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-724 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-725 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-726 | TC-FA-TAG-E2E-177 | FE+BE |
| TC-FA-TAG-727 | TC-FA-TAG-E2E-178 | FE+BE |
| TC-FA-TAG-728 | TC-FA-TAG-E2E-178 | FE+BE |
| TC-FA-TAG-729 | TC-FA-TAG-E2E-178 | FE+BE |
| TC-FA-TAG-730 | TC-FA-TAG-E2E-178 | FE+BE |
| TC-FA-TAG-731 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-732 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-733 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-734 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-735 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-736 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-737 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-738 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-739 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-740 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-741 | TC-FA-TAG-E2E-179 | FE+BE |
| TC-FA-TAG-742 | TC-FA-TAG-E2E-180 | FE+BE |
| TC-FA-TAG-743 | TC-FA-TAG-E2E-181 | FE+BE |
| TC-FA-TAG-744 | TC-FA-TAG-E2E-181 | FE+BE |
| TC-FA-TAG-745 | TC-FA-TAG-E2E-181 | FE+BE |
| TC-FA-TAG-746 | TC-FA-TAG-E2E-181 | FE+BE |
| TC-FA-TAG-747 | TC-FA-TAG-E2E-181 | FE+BE |
| TC-FA-TAG-748 | TC-FA-TAG-E2E-182 | FE+BE |
| TC-FA-TAG-749 | TC-FA-TAG-E2E-182 | FE+BE |
| TC-FA-TAG-750 | TC-FA-TAG-E2E-182 | FE+BE |
| TC-FA-TAG-751 | TC-FA-TAG-E2E-182 | FE+BE |
| TC-FA-TAG-752 | TC-FA-TAG-E2E-183 | FE+BE |
| TC-FA-TAG-753 | TC-FA-TAG-E2E-183 | FE+BE |
| TC-FA-TAG-754 | TC-FA-TAG-E2E-183 | FE+BE |
| TC-FA-TAG-755 | TC-FA-TAG-E2E-183 | FE+BE |
| TC-FA-TAG-756 | TC-FA-TAG-E2E-183 | FE+BE |
| TC-FA-TAG-757 | TC-FA-TAG-E2E-192 | FE+BE |
| TC-FA-TAG-758 | TC-FA-TAG-E2E-184 | FE+BE |
| TC-FA-TAG-759 | TC-FA-TAG-E2E-184 | FE+BE |
| TC-FA-TAG-760 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-761 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-762 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-763 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-764 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-765 | TC-FA-TAG-E2E-193 | FE+BE |
| TC-FA-TAG-766 | TC-FA-TAG-E2E-194 | FE+BE |
| TC-FA-TAG-767 | TC-FA-TAG-E2E-194 | FE+BE |
| TC-FA-TAG-768 | TC-FA-TAG-E2E-194 | FE+BE |
| TC-FA-TAG-769 | TC-FA-TAG-E2E-194 | FE+BE |
| TC-FA-TAG-770 | TC-FA-TAG-E2E-194 | FE+BE |
| TC-FA-TAG-771 | TC-FA-TAG-E2E-195 | FE+BE |
| TC-FA-TAG-772 | TC-FA-TAG-E2E-195 | FE+BE |
| TC-FA-TAG-773 | TC-FA-TAG-E2E-195 | FE+BE |
| TC-FA-TAG-774 | TC-FA-TAG-E2E-195 | FE+BE |
| TC-FA-TAG-775 | TC-FA-TAG-E2E-195 | FE+BE |
| TC-FA-TAG-776 | TC-FA-TAG-E2E-196 | FE+BE |
| TC-FA-TAG-777 | TC-FA-TAG-E2E-196 | FE+BE |
| TC-FA-TAG-778 | TC-FA-TAG-E2E-196 | FE+BE |
| TC-FA-TAG-779 | TC-FA-TAG-E2E-196 | FE+BE |
| TC-FA-TAG-780 | TC-FA-TAG-E2E-197 | FE+BE |
| TC-FA-TAG-781 | TC-FA-TAG-E2E-197 | FE+BE |
| TC-FA-TAG-782 | TC-FA-TAG-E2E-197 | FE+BE |
| TC-FA-TAG-783 | TC-FA-TAG-E2E-197 | FE+BE |
| TC-FA-TAG-784 | TC-FA-TAG-E2E-198 | FE+BE |
| TC-FA-TAG-785 | TC-FA-TAG-E2E-198 | FE+BE |
| TC-FA-TAG-786 | TC-FA-TAG-E2E-198 | FE+BE |
| TC-FA-TAG-787 | TC-FA-TAG-E2E-199 | FE+BE |
| TC-FA-TAG-788 | TC-FA-TAG-E2E-199 | FE+BE |
| TC-FA-TAG-789 | TC-FA-TAG-E2E-199 | FE+BE |
| TC-FA-TAG-790 | TC-FA-TAG-E2E-200 | FE+BE |
| TC-FA-TAG-791 | TC-FA-TAG-E2E-200 | FE+BE |
| TC-FA-TAG-792 | TC-FA-TAG-E2E-200 | FE+BE |
| TC-FA-TAG-793 | TC-FA-TAG-E2E-200 | FE+BE |
| TC-FA-TAG-794 | TC-FA-TAG-E2E-201 | FE+BE |
| TC-FA-TAG-795 | TC-FA-TAG-E2E-201 | FE+BE |
| TC-FA-TAG-796 | TC-FA-TAG-E2E-201 | FE+BE |
| TC-FA-TAG-797 | TC-FA-TAG-E2E-202 | FE+BE |
| TC-FA-TAG-798 | TC-FA-TAG-E2E-202 | FE+BE |
| TC-FA-TAG-799 | TC-FA-TAG-E2E-202 | FE+BE |
| TC-FA-TAG-800 | TC-FA-TAG-E2E-202 | FE+BE |
| TC-FA-TAG-801 | TC-FA-TAG-E2E-203 | FE+BE |
| TC-FA-TAG-802 | TC-FA-TAG-E2E-203 | FE+BE |
| TC-FA-TAG-803 | TC-FA-TAG-E2E-203 | FE+BE |
| TC-FA-TAG-804 | TC-FA-TAG-E2E-203 | FE+BE |
| TC-FA-TAG-805 | TC-FA-TAG-E2E-204 | FE+BE |
| TC-FA-TAG-806 | TC-FA-TAG-E2E-204 | FE+BE |
| TC-FA-TAG-807 | TC-FA-TAG-E2E-204 | FE+BE |
| TC-FA-TAG-808 | TC-FA-TAG-E2E-204 | FE+BE |
| TC-FA-TAG-809 | TC-FA-TAG-E2E-204 | FE+BE |
| TC-FA-TAG-810 | TC-FA-TAG-E2E-205 | FE+BE |
| TC-FA-TAG-811 | TC-FA-TAG-E2E-205 | FE+BE |
| TC-FA-TAG-812 | TC-FA-TAG-E2E-205 | FE+BE |
| TC-FA-TAG-813 | TC-FA-TAG-E2E-205 | FE+BE |
| TC-FA-TAG-814 | TC-FA-TAG-E2E-206 | FE+BE |
| TC-FA-TAG-815 | TC-FA-TAG-E2E-206 | FE+BE |
| TC-FA-TAG-816 | TC-FA-TAG-E2E-206 | FE+BE |
| TC-FA-TAG-817 | TC-FA-TAG-E2E-206 | FE+BE |
| TC-FA-TAG-818 | TC-FA-TAG-E2E-207 | FE+BE |
| TC-FA-TAG-819 | TC-FA-TAG-E2E-207 | FE+BE |
| TC-FA-TAG-820 | TC-FA-TAG-E2E-207 | FE+BE |
| TC-FA-TAG-821 | TC-FA-TAG-E2E-207 | FE+BE |
| TC-FA-TAG-822 | TC-FA-TAG-E2E-208 | FE+BE |
| TC-FA-TAG-823 | TC-FA-TAG-E2E-208 | FE+BE |
| TC-FA-TAG-824 | TC-FA-TAG-E2E-208 | FE+BE |
| TC-FA-TAG-825 | TC-FA-TAG-E2E-208 | FE+BE |
| TC-FA-TAG-826 | TC-FA-TAG-E2E-209 | FE+BE |
| TC-FA-TAG-827 | TC-FA-TAG-E2E-209 | FE+BE |
| TC-FA-TAG-828 | TC-FA-TAG-E2E-209 | FE+BE |
| TC-FA-TAG-829 | TC-FA-TAG-E2E-209 | FE+BE |
| TC-FA-TAG-830 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-831 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-832 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-833 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-834 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-835 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-836 | TC-FA-TAG-E2E-210 | FE+BE |
| TC-FA-TAG-837 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-838 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-839 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-840 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-841 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-842 | TC-FA-TAG-E2E-211 | FE+BE |
| TC-FA-TAG-843 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-844 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-845 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-846 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-847 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-848 | TC-FA-TAG-E2E-212 | FE+BE |
| TC-FA-TAG-849 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-850 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-851 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-852 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-853 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-854 | TC-FA-TAG-E2E-213 | FE+BE |
| TC-FA-TAG-855 | TC-FA-TAG-E2E-214 | FE+BE |
| TC-FA-TAG-856 | TC-FA-TAG-E2E-214 | FE+BE |
| TC-FA-TAG-857 | TC-FA-TAG-E2E-214 | FE+BE |
| TC-FA-TAG-858 | TC-FA-TAG-E2E-214 | FE+BE |
| TC-FA-TAG-859 | TC-FA-TAG-E2E-214 | FE+BE |
| TC-FA-TAG-860 | TC-FA-TAG-E2E-215 | FE+BE |
| TC-FA-TAG-861 | TC-FA-TAG-E2E-215 | FE+BE |
| TC-FA-TAG-862 | TC-FA-TAG-E2E-215 | FE+BE |
| TC-FA-TAG-863 | TC-FA-TAG-E2E-215 | FE+BE |
| TC-FA-TAG-864 | TC-FA-TAG-E2E-215 | FE+BE |
| TC-FA-TAG-865 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-866 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-867 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-868 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-869 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-870 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-871 | TC-FA-TAG-E2E-216 | FE+BE |
| TC-FA-TAG-872 | TC-FA-TAG-E2E-217 | FE+BE |
| TC-FA-TAG-873 | TC-FA-TAG-E2E-217 | FE+BE |
| TC-FA-TAG-874 | TC-FA-TAG-E2E-217 | FE+BE |
| TC-FA-TAG-875 | TC-FA-TAG-E2E-217 | FE+BE |
| TC-FA-TAG-876 | TC-FA-TAG-E2E-217 | FE+BE |
| TC-FA-TAG-877 | TC-FA-TAG-E2E-218 | FE+BE |
| TC-FA-TAG-878 | TC-FA-TAG-E2E-218 | FE+BE |
| TC-FA-TAG-879 | TC-FA-TAG-E2E-218 | FE+BE |
| TC-FA-TAG-880 | TC-FA-TAG-E2E-218 | FE+BE |
| TC-FA-TAG-881 | TC-FA-TAG-E2E-219 | FE+BE |
| TC-FA-TAG-882 | TC-FA-TAG-E2E-219 | FE+BE |
| TC-FA-TAG-883 | TC-FA-TAG-E2E-219 | FE+BE |
| TC-FA-TAG-884 | TC-FA-TAG-E2E-219 | FE+BE |
| TC-FA-TAG-885 | TC-FA-TAG-E2E-219 | FE+BE |
| TC-FA-TAG-886 | TC-FA-TAG-E2E-220 | FE+BE |
| TC-FA-TAG-887 | TC-FA-TAG-E2E-220 | FE+BE |
| TC-FA-TAG-888 | TC-FA-TAG-E2E-220 | FE+BE |
| TC-FA-TAG-889 | TC-FA-TAG-E2E-220 | FE+BE |
| TC-FA-TAG-890 | TC-FA-TAG-E2E-221 | FE+BE |
| TC-FA-TAG-891 | TC-FA-TAG-E2E-221 | FE+BE |
| TC-FA-TAG-892 | TC-FA-TAG-E2E-221 | FE+BE |
| TC-FA-TAG-893 | TC-FA-TAG-E2E-221 | FE+BE |
| TC-FA-TAG-894 | TC-FA-TAG-E2E-222 | FE+BE |
| TC-FA-TAG-895 | TC-FA-TAG-E2E-222 | FE+BE |
| TC-FA-TAG-896 | TC-FA-TAG-E2E-222 | FE+BE |
| TC-FA-TAG-897 | TC-FA-TAG-E2E-222 | FE+BE |
| TC-FA-TAG-898 | TC-FA-TAG-E2E-223 | FE+BE |
| TC-FA-TAG-899 | TC-FA-TAG-E2E-223 | FE+BE |
| TC-FA-TAG-900 | TC-FA-TAG-E2E-223 | FE+BE |
| TC-FA-TAG-901 | TC-FA-TAG-E2E-223 | FE+BE |
| TC-FA-TAG-902 | TC-FA-TAG-E2E-224 | FE+BE |
| TC-FA-TAG-903 | TC-FA-TAG-E2E-224 | FE+BE |
| TC-FA-TAG-904 | TC-FA-TAG-E2E-224 | FE+BE |
| TC-FA-TAG-905 | TC-FA-TAG-E2E-386 | FE+BE |
| TC-FA-TAG-906 | TC-FA-TAG-E2E-386 | FE+BE |
| TC-FA-TAG-907 | TC-FA-TAG-E2E-386 | FE+BE |
| TC-FA-TAG-908 | TC-FA-TAG-E2E-225 | FE+BE |
| TC-FA-TAG-909 | TC-FA-TAG-E2E-225 | FE+BE |
| TC-FA-TAG-910 | TC-FA-TAG-E2E-225 | FE+BE |
| TC-FA-TAG-911 | TC-FA-TAG-E2E-225 | FE+BE |
| TC-FA-TAG-912 | TC-FA-TAG-E2E-226 | FE+BE |
| TC-FA-TAG-913 | TC-FA-TAG-E2E-226 | FE+BE |
| TC-FA-TAG-914 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-915 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-916 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-917 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-918 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-919 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-920 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-921 | TC-FA-TAG-E2E-229 | FE+BE |
| TC-FA-TAG-922 | TC-FA-TAG-E2E-230 | FE+BE |
| TC-FA-TAG-923 | TC-FA-TAG-E2E-230 | FE+BE |
| TC-FA-TAG-924 | TC-FA-TAG-E2E-230 | FE+BE |
| TC-FA-TAG-925 | TC-FA-TAG-E2E-231 | FE+BE |
| TC-FA-TAG-926 | TC-FA-TAG-E2E-231 | FE+BE |
| TC-FA-TAG-927 | TC-FA-TAG-E2E-231 | FE+BE |
| TC-FA-TAG-928 | TC-FA-TAG-E2E-231 | FE+BE |
| TC-FA-TAG-929 | TC-FA-TAG-E2E-387 | FE+BE |
| TC-FA-TAG-930 | TC-FA-TAG-E2E-242 | FE+BE |
| TC-FA-TAG-931 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-932 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-933 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-934 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-935 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-936 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-937 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-938 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-939 | TC-FA-TAG-E2E-004 | FE+BE |
| TC-FA-TAG-940 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-941 | TC-FA-TAG-E2E-235 | FE+BE |
| TC-FA-TAG-942 | TC-FA-TAG-E2E-235 | FE+BE |
| TC-FA-TAG-943 | TC-FA-TAG-E2E-235 | FE+BE |
| TC-FA-TAG-944 | TC-FA-TAG-E2E-235 | FE+BE |
| TC-FA-TAG-945 | TC-FA-TAG-E2E-235 | FE+BE |
| TC-FA-TAG-946 | TC-FA-TAG-E2E-236 | FE+BE |
| TC-FA-TAG-947 | TC-FA-TAG-E2E-236 | FE+BE |
| TC-FA-TAG-948 | TC-FA-TAG-E2E-236 | FE+BE |
| TC-FA-TAG-949 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-950 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-951 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-952 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-953 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-954 | TC-FA-TAG-E2E-237 | FE+BE |
| TC-FA-TAG-955 | TC-FA-TAG-E2E-238 | FE+BE |
| TC-FA-TAG-956 | TC-FA-TAG-E2E-238 | FE+BE |
| TC-FA-TAG-957 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-958 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-959 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-960 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-961 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-962 | TC-FA-TAG-E2E-239 | FE+BE |
| TC-FA-TAG-963 | TC-FA-TAG-E2E-240 | FE+BE |
| TC-FA-TAG-964 | TC-FA-TAG-E2E-240 | FE+BE |
| TC-FA-TAG-965 | TC-FA-TAG-E2E-240 | FE+BE |
| TC-FA-TAG-966 | TC-FA-TAG-E2E-241 | FE+BE |
| TC-FA-TAG-967 | TC-FA-TAG-E2E-241 | FE+BE |
| TC-FA-TAG-968 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-969 | TC-FA-TAG-E2E-241 | FE+BE |
| TC-FA-TAG-970 | TC-FA-TAG-E2E-332 | FE+BE |
| TC-FA-TAG-971 | TC-FA-TAG-E2E-189 | FE+BE |
| TC-FA-TAG-972 | TC-FA-TAG-E2E-189 | FE+BE |
| TC-FA-TAG-973 | TC-FA-TAG-E2E-189 | FE+BE |
| TC-FA-TAG-974 | TC-FA-TAG-E2E-189 | FE+BE |
| TC-FA-TAG-975 | TC-FA-TAG-E2E-233 | FE+BE |
| TC-FA-TAG-976 | TC-FA-TAG-E2E-234 | FE+BE |
| TC-FA-TAG-977 | TC-FA-TAG-E2E-232 | FE+BE |
| TC-FA-TAG-978 | TC-FA-TAG-E2E-232 | FE+BE |
| TC-FA-TAG-979 | TC-FA-TAG-E2E-232 | FE+BE |
| TC-FA-TAG-980 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-981 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-982 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-983 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-984 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-985 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-986 | TC-FA-TAG-E2E-244 | FE+BE |
| TC-FA-TAG-987 | TC-FA-TAG-E2E-245 | FE+BE |
| TC-FA-TAG-988 | TC-FA-TAG-E2E-245 | FE+BE |
| TC-FA-TAG-989 | TC-FA-TAG-E2E-245 | FE+BE |
| TC-FA-TAG-990 | TC-FA-TAG-E2E-245 | FE+BE |
| TC-FA-TAG-991 | TC-FA-TAG-E2E-245 | FE+BE |
| TC-FA-TAG-992 | TC-FA-TAG-E2E-246 | FE+BE |
| TC-FA-TAG-993 | TC-FA-TAG-E2E-246 | FE+BE |
| TC-FA-TAG-994 | TC-FA-TAG-E2E-246 | FE+BE |
| TC-FA-TAG-995 | TC-FA-TAG-E2E-246 | FE+BE |
| TC-FA-TAG-996 | TC-FA-TAG-E2E-246 | FE+BE |
| TC-FA-TAG-997 | TC-FA-TAG-E2E-247 | FE+BE |
| TC-FA-TAG-998 | TC-FA-TAG-E2E-247 | FE+BE |
| TC-FA-TAG-999 | TC-FA-TAG-E2E-247 | FE+BE |
| TC-FA-TAG-1000 | TC-FA-TAG-E2E-247 | FE+BE |
| TC-FA-TAG-1001 | TC-FA-TAG-E2E-247 | FE+BE |
| TC-FA-TAG-1002 | TC-FA-TAG-E2E-248 | FE+BE |
| TC-FA-TAG-1003 | TC-FA-TAG-E2E-248 | FE+BE |
| TC-FA-TAG-1004 | TC-FA-TAG-E2E-248 | FE+BE |
| TC-FA-TAG-1005 | TC-FA-TAG-E2E-249 | FE+BE |
| TC-FA-TAG-1006 | TC-FA-TAG-E2E-249 | FE+BE |
| TC-FA-TAG-1007 | TC-FA-TAG-E2E-249 | FE+BE |
| TC-FA-TAG-1008 | TC-FA-TAG-E2E-249 | FE+BE |
| TC-FA-TAG-1009 | TC-FA-TAG-E2E-249 | FE+BE |
| TC-FA-TAG-1010 | TC-FA-TAG-E2E-250 | FE+BE |
| TC-FA-TAG-1011 | TC-FA-TAG-E2E-250 | FE+BE |
| TC-FA-TAG-1012 | TC-FA-TAG-E2E-250 | FE+BE |
| TC-FA-TAG-1013 | TC-FA-TAG-E2E-250 | FE+BE |
| TC-FA-TAG-1014 | TC-FA-TAG-E2E-269 | FE+BE |
| TC-FA-TAG-1015 | TC-FA-TAG-E2E-269 | FE+BE |
| TC-FA-TAG-1016 | TC-FA-TAG-E2E-251 | FE+BE |
| TC-FA-TAG-1017 | TC-FA-TAG-E2E-251 | FE+BE |
| TC-FA-TAG-1018 | TC-FA-TAG-E2E-252 | FE+BE |
| TC-FA-TAG-1019 | TC-FA-TAG-E2E-252 | FE+BE |
| TC-FA-TAG-1020 | TC-FA-TAG-E2E-252 | FE+BE |
| TC-FA-TAG-1021 | TC-FA-TAG-E2E-252 | FE+BE |
| TC-FA-TAG-1022 | TC-FA-TAG-E2E-270 | FE+BE |
| TC-FA-TAG-1023 | TC-FA-TAG-E2E-270 | FE+BE |
| TC-FA-TAG-1024 | TC-FA-TAG-E2E-253 | FE+BE |
| TC-FA-TAG-1025 | TC-FA-TAG-E2E-253 | FE+BE |
| TC-FA-TAG-1026 | TC-FA-TAG-E2E-332 | FE+BE |
| TC-FA-TAG-1027 | TC-FA-TAG-E2E-253 | FE+BE |
| TC-FA-TAG-1028 | TC-FA-TAG-E2E-253 | FE+BE |
| TC-FA-TAG-1029 | TC-FA-TAG-E2E-253 | FE+BE |
| TC-FA-TAG-1030 | TC-FA-TAG-E2E-254 | FE+BE |
| TC-FA-TAG-1031 | TC-FA-TAG-E2E-254 | FE+BE |
| TC-FA-TAG-1032 | TC-FA-TAG-E2E-254 | FE+BE |
| TC-FA-TAG-1033 | TC-FA-TAG-E2E-254 | FE+BE |
| TC-FA-TAG-1034 | TC-FA-TAG-E2E-254 | FE+BE |
| TC-FA-TAG-1035 | TC-FA-TAG-E2E-255 | FE+BE |
| TC-FA-TAG-1036 | TC-FA-TAG-E2E-255 | FE+BE |
| TC-FA-TAG-1037 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1038 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1039 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1040 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1041 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1042 | TC-FA-TAG-E2E-256 | FE+BE |
| TC-FA-TAG-1043 | TC-FA-TAG-E2E-257 | FE+BE |
| TC-FA-TAG-1044 | TC-FA-TAG-E2E-257 | FE+BE |
| TC-FA-TAG-1045 | TC-FA-TAG-E2E-257 | FE+BE |
| TC-FA-TAG-1046 | TC-FA-TAG-E2E-258 | FE+BE |
| TC-FA-TAG-1047 | TC-FA-TAG-E2E-258 | FE+BE |
| TC-FA-TAG-1048 | TC-FA-TAG-E2E-258 | FE+BE |
| TC-FA-TAG-1049 | TC-FA-TAG-E2E-258 | FE+BE |
| TC-FA-TAG-1050 | TC-FA-TAG-E2E-258 | FE+BE |
| TC-FA-TAG-1051 | TC-FA-TAG-E2E-259 | FE+BE |
| TC-FA-TAG-1052 | TC-FA-TAG-E2E-259 | FE+BE |
| TC-FA-TAG-1053 | TC-FA-TAG-E2E-259 | FE+BE |
| TC-FA-TAG-1054 | TC-FA-TAG-E2E-259 | FE+BE |
| TC-FA-TAG-1055 | TC-FA-TAG-E2E-260 | FE+BE |
| TC-FA-TAG-1056 | TC-FA-TAG-E2E-260 | FE+BE |
| TC-FA-TAG-1057 | TC-FA-TAG-E2E-260 | FE+BE |
| TC-FA-TAG-1058 | TC-FA-TAG-E2E-260 | FE+BE |
| TC-FA-TAG-1059 | TC-FA-TAG-E2E-261 | FE+BE |
| TC-FA-TAG-1060 | TC-FA-TAG-E2E-261 | FE+BE |
| TC-FA-TAG-1061 | TC-FA-TAG-E2E-261 | FE+BE |
| TC-FA-TAG-1062 | TC-FA-TAG-E2E-261 | FE+BE |
| TC-FA-TAG-1063 | TC-FA-TAG-E2E-262 | FE+BE |
| TC-FA-TAG-1064 | TC-FA-TAG-E2E-262 | FE+BE |
| TC-FA-TAG-1065 | TC-FA-TAG-E2E-262 | FE+BE |
| TC-FA-TAG-1066 | TC-FA-TAG-E2E-262 | FE+BE |
| TC-FA-TAG-1067 | TC-FA-TAG-E2E-263 | FE+BE |
| TC-FA-TAG-1068 | TC-FA-TAG-E2E-263 | FE+BE |
| TC-FA-TAG-1069 | TC-FA-TAG-E2E-332 | FE+BE |
| TC-FA-TAG-1070 | TC-FA-TAG-E2E-263 | FE+BE |
| TC-FA-TAG-1071 | TC-FA-TAG-E2E-377 | FE+BE |
| TC-FA-TAG-1072 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1073 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1074 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1075 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1076 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1077 | TC-FA-TAG-E2E-271 | FE+BE |
| TC-FA-TAG-1078 | TC-FA-TAG-E2E-272 | FE+BE |
| TC-FA-TAG-1079 | TC-FA-TAG-E2E-272 | FE+BE |
| TC-FA-TAG-1080 | TC-FA-TAG-E2E-272 | FE+BE |
| TC-FA-TAG-1081 | TC-FA-TAG-E2E-272 | FE+BE |
| TC-FA-TAG-1082 | TC-FA-TAG-E2E-273 | FE+BE |
| TC-FA-TAG-1083 | TC-FA-TAG-E2E-273 | FE+BE |
| TC-FA-TAG-1084 | TC-FA-TAG-E2E-273 | FE+BE |
| TC-FA-TAG-1085 | TC-FA-TAG-E2E-274 | FE+BE |
| TC-FA-TAG-1086 | TC-FA-TAG-E2E-274 | FE+BE |
| TC-FA-TAG-1087 | TC-FA-TAG-E2E-274 | FE+BE |
| TC-FA-TAG-1088 | TC-FA-TAG-E2E-353 | FE+BE |
| TC-FA-TAG-1089 | TC-FA-TAG-E2E-275 | FE+BE |
| TC-FA-TAG-1090 | TC-FA-TAG-E2E-353 | FE+BE |
| TC-FA-TAG-1091 | TC-FA-TAG-E2E-276 | FE+BE |
| TC-FA-TAG-1092 | TC-FA-TAG-E2E-276 | FE+BE |
| TC-FA-TAG-1093 | TC-FA-TAG-E2E-276 | FE+BE |
| TC-FA-TAG-1094 | TC-FA-TAG-E2E-353 | FE+BE |
| TC-FA-TAG-1095 | TC-FA-TAG-E2E-277 | FE+BE |
| TC-FA-TAG-1096 | TC-FA-TAG-E2E-277 | FE+BE |
| TC-FA-TAG-1097 | TC-FA-TAG-E2E-277 | FE+BE |
| TC-FA-TAG-1098 | TC-FA-TAG-E2E-303 | FE+BE |
| TC-FA-TAG-1099 | TC-FA-TAG-E2E-278 | FE+BE |
| TC-FA-TAG-1100 | TC-FA-TAG-E2E-278 | FE+BE |
| TC-FA-TAG-1101 | TC-FA-TAG-E2E-278 | FE+BE |
| TC-FA-TAG-1102 | TC-FA-TAG-E2E-354 | FE+BE |
| TC-FA-TAG-1103 | TC-FA-TAG-E2E-279 | FE+BE |
| TC-FA-TAG-1104 | TC-FA-TAG-E2E-279 | FE+BE |
| TC-FA-TAG-1105 | TC-FA-TAG-E2E-279 | FE+BE |
| TC-FA-TAG-1106 | TC-FA-TAG-E2E-354 | FE+BE |
| TC-FA-TAG-1107 | TC-FA-TAG-E2E-279 | FE+BE |
| TC-FA-TAG-1108 | TC-FA-TAG-E2E-280 | FE+BE |
| TC-FA-TAG-1109 | TC-FA-TAG-E2E-280 | FE+BE |
| TC-FA-TAG-1110 | TC-FA-TAG-E2E-377 | FE+BE |
| TC-FA-TAG-1111 | TC-FA-TAG-E2E-304 | FE+BE |
| TC-FA-TAG-1112 | TC-FA-TAG-E2E-304 | FE+BE |
| TC-FA-TAG-1113 | TC-FA-TAG-E2E-281 | FE+BE |
| TC-FA-TAG-1114 | TC-FA-TAG-E2E-281 | FE+BE |
| TC-FA-TAG-1115 | TC-FA-TAG-E2E-281 | FE+BE |
| TC-FA-TAG-1116 | TC-FA-TAG-E2E-281 | FE+BE |
| TC-FA-TAG-1117 | TC-FA-TAG-E2E-282 | FE+BE |
| TC-FA-TAG-1118 | TC-FA-TAG-E2E-282 | FE+BE |
| TC-FA-TAG-1119 | TC-FA-TAG-E2E-282 | FE+BE |
| TC-FA-TAG-1120 | TC-FA-TAG-E2E-283 | FE+BE |
| TC-FA-TAG-1121 | TC-FA-TAG-E2E-283 | FE+BE |
| TC-FA-TAG-1122 | TC-FA-TAG-E2E-283 | FE+BE |
| TC-FA-TAG-1123 | TC-FA-TAG-E2E-284 | FE+BE |
| TC-FA-TAG-1124 | TC-FA-TAG-E2E-284 | FE+BE |
| TC-FA-TAG-1125 | TC-FA-TAG-E2E-284 | FE+BE |
| TC-FA-TAG-1126 | TC-FA-TAG-E2E-285 | FE+BE |
| TC-FA-TAG-1127 | TC-FA-TAG-E2E-285 | FE+BE |
| TC-FA-TAG-1128 | TC-FA-TAG-E2E-285 | FE+BE |
| TC-FA-TAG-1129 | TC-FA-TAG-E2E-286 | FE+BE |
| TC-FA-TAG-1130 | TC-FA-TAG-E2E-286 | FE+BE |
| TC-FA-TAG-1131 | TC-FA-TAG-E2E-286 | FE+BE |
| TC-FA-TAG-1132 | TC-FA-TAG-E2E-286 | FE+BE |
| TC-FA-TAG-1133 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1134 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1135 | TC-FA-TAG-E2E-289 | FE+BE |
| TC-FA-TAG-1136 | TC-FA-TAG-E2E-289 | FE+BE |
| TC-FA-TAG-1137 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1138 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1139 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1140 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1141 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1142 | TC-FA-TAG-E2E-287 | FE+BE |
| TC-FA-TAG-1143 | TC-FA-TAG-E2E-288 | FE+BE |
| TC-FA-TAG-1144 | TC-FA-TAG-E2E-292 | FE+BE |
| TC-FA-TAG-1145 | TC-FA-TAG-E2E-292 | FE+BE |
| TC-FA-TAG-1146 | TC-FA-TAG-E2E-292 | FE+BE |
| TC-FA-TAG-1147 | TC-FA-TAG-E2E-292 | FE+BE |
| TC-FA-TAG-1148 | TC-FA-TAG-E2E-293 | FE+BE |
| TC-FA-TAG-1149 | TC-FA-TAG-E2E-293 | FE+BE |
| TC-FA-TAG-1150 | TC-FA-TAG-E2E-293 | FE+BE |
| TC-FA-TAG-1151 | TC-FA-TAG-E2E-293 | FE+BE |
| TC-FA-TAG-1152 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1153 | TC-FA-TAG-E2E-294 | FE+BE |
| TC-FA-TAG-1154 | TC-FA-TAG-E2E-346 | FE+BE |
| TC-FA-TAG-1155 | TC-FA-TAG-E2E-321 | FE+BE |
| TC-FA-TAG-1156 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1157 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1158 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1159 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1160 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1161 | TC-FA-TAG-E2E-305 | FE+BE |
| TC-FA-TAG-1162 | TC-FA-TAG-E2E-306 | FE+BE |
| TC-FA-TAG-1163 | TC-FA-TAG-E2E-306 | FE+BE |
| TC-FA-TAG-1164 | TC-FA-TAG-E2E-306 | FE+BE |
| TC-FA-TAG-1165 | TC-FA-TAG-E2E-306 | FE+BE |
| TC-FA-TAG-1166 | TC-FA-TAG-E2E-306 | FE+BE |
| TC-FA-TAG-1167 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1168 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1169 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1170 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1171 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1172 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1173 | TC-FA-TAG-E2E-307 | FE+BE |
| TC-FA-TAG-1174 | TC-FA-TAG-E2E-308 | FE+BE |
| TC-FA-TAG-1175 | TC-FA-TAG-E2E-308 | FE+BE |
| TC-FA-TAG-1176 | TC-FA-TAG-E2E-308 | FE+BE |
| TC-FA-TAG-1177 | TC-FA-TAG-E2E-308 | FE+BE |
| TC-FA-TAG-1178 | TC-FA-TAG-E2E-308 | FE+BE |
| TC-FA-TAG-1179 | TC-FA-TAG-E2E-321 | FE+BE |
| TC-FA-TAG-1180 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1181 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1182 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1183 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1184 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1185 | TC-FA-TAG-E2E-309 | FE+BE |
| TC-FA-TAG-1186 | TC-FA-TAG-E2E-310 | FE+BE |
| TC-FA-TAG-1187 | TC-FA-TAG-E2E-321 | FE+BE |
| TC-FA-TAG-1188 | TC-FA-TAG-E2E-311 | FE+BE |
| TC-FA-TAG-1189 | TC-FA-TAG-E2E-311 | FE+BE |
| TC-FA-TAG-1190 | TC-FA-TAG-E2E-311 | FE+BE |
| TC-FA-TAG-1191 | TC-FA-TAG-E2E-311 | FE+BE |
| TC-FA-TAG-1192 | TC-FA-TAG-E2E-311 | FE+BE |
| TC-FA-TAG-1193 | TC-FA-TAG-E2E-312 | FE+BE |
| TC-FA-TAG-1194 | TC-FA-TAG-E2E-312 | FE+BE |
| TC-FA-TAG-1195 | TC-FA-TAG-E2E-312 | FE+BE |
| TC-FA-TAG-1196 | TC-FA-TAG-E2E-312 | FE+BE |
| TC-FA-TAG-1197 | TC-FA-TAG-E2E-321 | FE+BE |
| TC-FA-TAG-1198 | TC-FA-TAG-E2E-313 | FE+BE |
| TC-FA-TAG-1199 | TC-FA-TAG-E2E-313 | FE+BE |
| TC-FA-TAG-1200 | TC-FA-TAG-E2E-313 | FE+BE |
| TC-FA-TAG-1201 | TC-FA-TAG-E2E-314 | FE+BE |
| TC-FA-TAG-1202 | TC-FA-TAG-E2E-314 | FE+BE |
| TC-FA-TAG-1203 | TC-FA-TAG-E2E-314 | FE+BE |
| TC-FA-TAG-1204 | TC-FA-TAG-E2E-314 | FE+BE |
| TC-FA-TAG-1205 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1206 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1207 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1208 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1209 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1210 | TC-FA-TAG-E2E-315 | FE+BE |
| TC-FA-TAG-1211 | TC-FA-TAG-E2E-316 | FE+BE |
| TC-FA-TAG-1212 | TC-FA-TAG-E2E-316 | FE+BE |
| TC-FA-TAG-1213 | TC-FA-TAG-E2E-316 | FE+BE |
| TC-FA-TAG-1214 | TC-FA-TAG-E2E-316 | FE+BE |
| TC-FA-TAG-1215 | TC-FA-TAG-E2E-316 | FE+BE |
| TC-FA-TAG-1216 | TC-FA-TAG-E2E-322 | FE+BE |
| TC-FA-TAG-1217 | TC-FA-TAG-E2E-317 | FE+BE |
| TC-FA-TAG-1218 | TC-FA-TAG-E2E-317 | FE+BE |
| TC-FA-TAG-1219 | TC-FA-TAG-E2E-318 | FE+BE |
| TC-FA-TAG-1220 | TC-FA-TAG-E2E-318 | FE+BE |
| TC-FA-TAG-1221 | TC-FA-TAG-E2E-318 | FE+BE |
| TC-FA-TAG-1222 | TC-FA-TAG-E2E-318 | FE+BE |
| TC-FA-TAG-1223 | TC-FA-TAG-E2E-289 | FE+BE |
| TC-FA-TAG-1224 | TC-FA-TAG-E2E-319 | FE+BE |
| TC-FA-TAG-1225 | TC-FA-TAG-E2E-322 | FE+BE |
| TC-FA-TAG-1226 | TC-FA-TAG-E2E-319 | FE+BE |
| TC-FA-TAG-1227 | TC-FA-TAG-E2E-319 | FE+BE |
| TC-FA-TAG-1228 | TC-FA-TAG-E2E-322 | FE+BE |
| TC-FA-TAG-1229 | TC-FA-TAG-E2E-319 | FE+BE |
| TC-FA-TAG-1230 | TC-FA-TAG-E2E-320 | FE+BE |
| TC-FA-TAG-1231 | TC-FA-TAG-E2E-320 | FE+BE |
| TC-FA-TAG-1232 | TC-FA-TAG-E2E-320 | FE+BE |
| TC-FA-TAG-1233 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1234 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1235 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1236 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1237 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1238 | TC-FA-TAG-E2E-300 | FE+BE |
| TC-FA-TAG-1239 | TC-FA-TAG-E2E-301 | FE+BE |
| TC-FA-TAG-1240 | TC-FA-TAG-E2E-377 | FE+BE |
| TC-FA-TAG-1241 | TC-FA-TAG-E2E-301 | FE+BE |
| TC-FA-TAG-1242 | TC-FA-TAG-E2E-301 | FE+BE |
| TC-FA-TAG-1243 | TC-FA-TAG-E2E-301 | FE+BE |
| TC-FA-TAG-1244 | TC-FA-TAG-E2E-302 | FE+BE |
| TC-FA-TAG-1245 | TC-FA-TAG-E2E-302 | FE+BE |
| TC-FA-TAG-1246 | TC-FA-TAG-E2E-302 | FE+BE |
| TC-FA-TAG-1247 | TC-FA-TAG-E2E-302 | FE+BE |
| TC-FA-TAG-1248 | TC-FA-TAG-E2E-289 | FE+BE |
| TC-FA-TAG-1249 | TC-FA-TAG-E2E-289 | FE+BE |
| TC-FA-TAG-1250 | TC-FA-TAG-E2E-290 | FE+BE |
| TC-FA-TAG-1251 | TC-FA-TAG-E2E-290 | FE+BE |
| TC-FA-TAG-1252 | TC-FA-TAG-E2E-290 | FE+BE |
| TC-FA-TAG-1253 | TC-FA-TAG-E2E-290 | FE+BE |
| TC-FA-TAG-1254 | TC-FA-TAG-E2E-291 | FE+BE |
| TC-FA-TAG-1255 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1256 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1257 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1258 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1259 | TC-FA-TAG-E2E-324 | FE+BE |
| TC-FA-TAG-1260 | TC-FA-TAG-E2E-324 | FE+BE |
| TC-FA-TAG-1261 | TC-FA-TAG-E2E-324 | FE+BE |
| TC-FA-TAG-1262 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1262 | TC-FA-TAG-E2E-388 | FE+BE |
| TC-FA-TAG-1263 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1264 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1265 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1266 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1267 | TC-FA-TAG-E2E-323 | FE+BE |
| TC-FA-TAG-1268 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1268 | TC-FA-TAG-E2E-388 | FE+BE |
| TC-FA-TAG-1269 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1269 | TC-FA-TAG-E2E-388 | FE+BE |
| TC-FA-TAG-1270 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1270 | TC-FA-TAG-E2E-388 | FE+BE |
| TC-FA-TAG-1271 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1272 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1273 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1274 | TC-FA-TAG-E2E-325 | FE+BE |
| TC-FA-TAG-1275 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1276 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1277 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1278 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1279 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1280 | TC-FA-TAG-E2E-326 | FE+BE |
| TC-FA-TAG-1281 | TC-FA-TAG-E2E-327 | FE+BE |
| TC-FA-TAG-1282 | TC-FA-TAG-E2E-327 | FE+BE |
| TC-FA-TAG-1283 | TC-FA-TAG-E2E-327 | FE+BE |
| TC-FA-TAG-1284 | TC-FA-TAG-E2E-352 | FE+BE |
| TC-FA-TAG-1285 | TC-FA-TAG-E2E-348 | FE+BE |
| TC-FA-TAG-1286 | TC-FA-TAG-E2E-385 | FE+BE |
| TC-FA-TAG-1287 | TC-FA-TAG-E2E-348 | FE+BE |
| TC-FA-TAG-1288 | TC-FA-TAG-E2E-348 | FE+BE |
| TC-FA-TAG-1289 | TC-FA-TAG-E2E-349 | FE+BE |
| TC-FA-TAG-1290 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1290 | TC-FA-TAG-E2E-389 | FE+BE |
| TC-FA-TAG-1291 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1291 | TC-FA-TAG-E2E-389 | FE+BE |
| TC-FA-TAG-1292 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1292 | TC-FA-TAG-E2E-389 | FE+BE |
| TC-FA-TAG-1293 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1293 | TC-FA-TAG-E2E-389 | FE+BE |
| TC-FA-TAG-1294 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1294 | TC-FA-TAG-E2E-389 | FE+BE |
| TC-FA-TAG-1295 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1296 | TC-FA-TAG-E2E-349 | FE+BE |
| TC-FA-TAG-1297 | TC-FA-TAG-E2E-349 | FE+BE |
| TC-FA-TAG-1298 | TC-FA-TAG-E2E-349 | FE+BE |
| TC-FA-TAG-1299 | TC-FA-TAG-E2E-350 | FE+BE |
| TC-FA-TAG-1300 | TC-FA-TAG-E2E-350 | FE+BE |
| TC-FA-TAG-1301 | TC-FA-TAG-E2E-385 | FE+BE |
| TC-FA-TAG-1302 | TC-FA-TAG-E2E-350 | FE+BE |
| TC-FA-TAG-1303 | TC-FA-TAG-E2E-328 | FE+BE |
| TC-FA-TAG-1304 | TC-FA-TAG-E2E-328 | FE+BE |
| TC-FA-TAG-1305 | TC-FA-TAG-E2E-328 | FE+BE |
| TC-FA-TAG-1306 | TC-FA-TAG-E2E-329 | FE+BE |
| TC-FA-TAG-1307 | TC-FA-TAG-E2E-324 | FE+BE |
| TC-FA-TAG-1308 | TC-FA-TAG-E2E-324 | FE+BE |
| TC-FA-TAG-1309 | TC-FA-TAG-E2E-330 | FE+BE |
| TC-FA-TAG-1310 | TC-FA-TAG-E2E-330 | FE+BE |
| TC-FA-TAG-1311 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-1312 | TC-FA-TAG-E2E-366 | FE+BE |
| TC-FA-TAG-1313 | TC-FA-TAG-E2E-352 | FE+BE |
| TC-FA-TAG-1314 | TC-FA-TAG-E2E-346 | FE+BE |
| TC-FA-TAG-1315 | TC-FA-TAG-E2E-346 | FE+BE |
| TC-FA-TAG-1316 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1317 | TC-FA-TAG-E2E-385 | FE+BE |
| TC-FA-TAG-1318 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1319 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1320 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1321 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1322 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1323 | TC-FA-TAG-E2E-297 | FE+BE |
| TC-FA-TAG-1324 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1325 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1326 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1327 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1328 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1329 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1330 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1331 | TC-FA-TAG-E2E-298 | FE+BE |
| TC-FA-TAG-1332 | TC-FA-TAG-E2E-374 | FE+BE |
| TC-FA-TAG-1333 | TC-FA-TAG-E2E-374 | FE+BE |
| TC-FA-TAG-1334 | TC-FA-TAG-E2E-374 | FE+BE |
| TC-FA-TAG-1335 | TC-FA-TAG-E2E-374 | FE+BE |
| TC-FA-TAG-1336 | TC-FA-TAG-E2E-375 | FE+BE |
| TC-FA-TAG-1337 | TC-FA-TAG-E2E-375 | FE+BE |
| TC-FA-TAG-1338 | TC-FA-TAG-E2E-375 | FE+BE |
| TC-FA-TAG-1339 | TC-FA-TAG-E2E-376 | FE+BE |
| TC-FA-TAG-1340 | TC-FA-TAG-E2E-334 | FE+BE |
| TC-FA-TAG-1341 | TC-FA-TAG-E2E-334 | FE+BE |
| TC-FA-TAG-1342 | TC-FA-TAG-E2E-334 | FE+BE |
| TC-FA-TAG-1343 | TC-FA-TAG-E2E-334 | FE+BE |
| TC-FA-TAG-1344 | TC-FA-TAG-E2E-343 | FE+BE |
| TC-FA-TAG-1345 | TC-FA-TAG-E2E-335 | FE+BE |
| TC-FA-TAG-1346 | TC-FA-TAG-E2E-335 | FE+BE |
| TC-FA-TAG-1347 | TC-FA-TAG-E2E-335 | FE+BE |
| TC-FA-TAG-1348 | TC-FA-TAG-E2E-344 | FE+BE |
| TC-FA-TAG-1349 | TC-FA-TAG-E2E-344 | FE+BE |
| TC-FA-TAG-1350 | TC-FA-TAG-E2E-333 | FE+BE |
| TC-FA-TAG-1351 | TC-FA-TAG-E2E-376 | FE+BE |
| TC-FA-TAG-1352 | TC-FA-TAG-E2E-070 | FE+BE |
| TC-FA-TAG-1353 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1354 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1355 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1356 | TC-FA-TAG-E2E-355 | FE+BE |
| TC-FA-TAG-1357 | TC-FA-TAG-E2E-356 | FE+BE |
| TC-FA-TAG-1358 | TC-FA-TAG-E2E-356 | FE+BE |
| TC-FA-TAG-1359 | TC-FA-TAG-E2E-356 | FE+BE |
| TC-FA-TAG-1360 | TC-FA-TAG-E2E-356 | FE+BE |
| TC-FA-TAG-1361 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1362 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1363 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1364 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1365 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1366 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1367 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1368 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1369 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1370 | TC-FA-TAG-E2E-357 | FE+BE |
| TC-FA-TAG-1371 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1372 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1373 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1374 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1375 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1376 | TC-FA-TAG-E2E-264 | FE+BE |
| TC-FA-TAG-1377 | TC-FA-TAG-E2E-147 | FE+BE |
| TC-FA-TAG-1378 | TC-FA-TAG-E2E-072 | FE+BE |
| TC-FA-TAG-1379 | TC-FA-TAG-E2E-085 | FE+BE |
| TC-FA-TAG-1380 | TC-FA-TAG-E2E-141 | FE+BE |
| TC-FA-TAG-1381 | TC-FA-TAG-E2E-301 | FE+BE |
| TC-FA-TAG-1382 | TC-FA-TAG-E2E-095 | FE+BE |
| TC-FA-TAG-1383 | TC-FA-TAG-E2E-114 | FE+BE |
| TC-FA-TAG-1384 | TC-FA-TAG-E2E-163 | FE+BE |
| TC-FA-TAG-1385 | TC-FA-TAG-E2E-163 | FE+BE |
| TC-FA-TAG-1386 | TC-FA-TAG-E2E-163 | FE+BE |
| TC-FA-TAG-1387 | TC-FA-TAG-E2E-163 | FE+BE |
| TC-FA-TAG-1388 | TC-FA-TAG-E2E-164 | FE+BE |
| TC-FA-TAG-1389 | TC-FA-TAG-E2E-164 | FE+BE |
| TC-FA-TAG-1390 | TC-FA-TAG-E2E-164 | FE+BE |
| TC-FA-TAG-1391 | TC-FA-TAG-E2E-164 | FE+BE |
| TC-FA-TAG-1392 | TC-FA-TAG-E2E-165 | FE+BE |
| TC-FA-TAG-1393 | TC-FA-TAG-E2E-165 | FE+BE |
| TC-FA-TAG-1394 | TC-FA-TAG-E2E-165 | FE+BE |
| TC-FA-TAG-1395 | TC-FA-TAG-E2E-166 | FE+BE |
| TC-FA-TAG-1396 | TC-FA-TAG-E2E-167 | FE+BE |
| TC-FA-TAG-1397 | TC-FA-TAG-E2E-167 | FE+BE |
| TC-FA-TAG-1398 | TC-FA-TAG-E2E-167 | FE+BE |
| TC-FA-TAG-1399 | TC-FA-TAG-E2E-167 | FE+BE |
| TC-FA-TAG-1400 | TC-FA-TAG-E2E-267 | FE+BE |
| TC-FA-TAG-1401 | TC-FA-TAG-E2E-267 | FE+BE |
| TC-FA-TAG-1402 | TC-FA-TAG-E2E-267 | FE+BE |
| TC-FA-TAG-1403 | TC-FA-TAG-E2E-267 | FE+BE |
| TC-FA-TAG-1404 | TC-FA-TAG-E2E-267 | FE+BE |
| TC-FA-TAG-1405 | TC-FA-TAG-E2E-268 | FE+BE |
| TC-FA-TAG-1406 | TC-FA-TAG-E2E-268 | FE+BE |
| TC-FA-TAG-1407 | TC-FA-TAG-E2E-268 | FE+BE |
| TC-FA-TAG-1408 | TC-FA-TAG-E2E-265 | FE+BE |
| TC-FA-TAG-1409 | TC-FA-TAG-E2E-265 | FE+BE |
| TC-FA-TAG-1410 | TC-FA-TAG-E2E-265 | FE+BE |
| TC-FA-TAG-1411 | TC-FA-TAG-E2E-265 | FE+BE |
| TC-FA-TAG-1412 | TC-FA-TAG-E2E-266 | FE+BE |
| TC-FA-TAG-1413 | TC-FA-TAG-E2E-266 | FE+BE |
| TC-FA-TAG-1414 | TC-FA-TAG-E2E-185 | FE+BE |
| TC-FA-TAG-1415 | TC-FA-TAG-E2E-185 | FE+BE |
| TC-FA-TAG-1416 | TC-FA-TAG-E2E-185 | FE+BE |
| TC-FA-TAG-1417 | TC-FA-TAG-E2E-185 | FE+BE |
| TC-FA-TAG-1418 | TC-FA-TAG-E2E-186 | FE+BE |
| TC-FA-TAG-1419 | TC-FA-TAG-E2E-186 | FE+BE |
| TC-FA-TAG-1420 | TC-FA-TAG-E2E-186 | FE+BE |
| TC-FA-TAG-1421 | TC-FA-TAG-E2E-186 | FE+BE |
| TC-FA-TAG-1422 | TC-FA-TAG-E2E-187 | FE+BE |
| TC-FA-TAG-1423 | TC-FA-TAG-E2E-187 | FE+BE |
| TC-FA-TAG-1424 | TC-FA-TAG-E2E-187 | FE+BE |
| TC-FA-TAG-1425 | TC-FA-TAG-E2E-187 | FE+BE |
| TC-FA-TAG-1426 | TC-FA-TAG-E2E-188 | FE+BE |
| TC-FA-TAG-1427 | TC-FA-TAG-E2E-188 | FE+BE |
| TC-FA-TAG-1428 | TC-FA-TAG-E2E-188 | FE+BE |
| TC-FA-TAG-1429 | TC-FA-TAG-E2E-189 | FE+BE |
| TC-FA-TAG-1430 | TC-FA-TAG-E2E-190 | FE+BE |
| TC-FA-TAG-1431 | TC-FA-TAG-E2E-041 | FE+BE |
| TC-FA-TAG-1432 | TC-FA-TAG-E2E-041 | FE+BE |
| TC-FA-TAG-1433 | TC-FA-TAG-E2E-041 | FE+BE |
| TC-FA-TAG-1434 | TC-FA-TAG-E2E-367 | FE+BE |
| TC-FA-TAG-1435 | TC-FA-TAG-E2E-367 | FE+BE |
| TC-FA-TAG-1436 | TC-FA-TAG-E2E-367 | FE+BE |
| TC-FA-TAG-1437 | TC-FA-TAG-E2E-367 | FE+BE |
| TC-FA-TAG-1438 | TC-FA-TAG-E2E-368 | FE+BE |
| TC-FA-TAG-1439 | TC-FA-TAG-E2E-105 | FE+BE |
| TC-FA-TAG-1440 | TC-FA-TAG-E2E-160 | FE+BE |
| TC-FA-TAG-1441 | TC-FA-TAG-E2E-070 | FE+BE |
| TC-FA-TAG-1442 | TC-FA-TAG-E2E-105 | FE+BE |
| TC-FA-TAG-1443 | TC-FA-TAG-E2E-126 | FE+BE |
| TC-FA-TAG-1444 | TC-FA-TAG-E2E-132 | FE+BE |
| TC-FA-TAG-1445 | TC-FA-TAG-E2E-115 | FE+BE |
| TC-FA-TAG-1446 | TC-FA-TAG-E2E-115 | FE+BE |
| TC-FA-TAG-1447 | TC-FA-TAG-E2E-370 | FE+BE |
| TC-FA-TAG-1448 | TC-FA-TAG-E2E-371 | FE+BE |
| TC-FA-TAG-1449 | TC-FA-TAG-E2E-060 | FE+BE |
| TC-FA-TAG-1450 | TC-FA-TAG-E2E-011 | FE+BE |
| TC-FA-TAG-1451 | TC-FA-TAG-E2E-230 | FE+BE |
| TC-FA-TAG-1452 | TC-FA-TAG-E2E-230 | FE+BE |
| TC-FA-TAG-1453 | TC-FA-TAG-E2E-101 | FE+BE |
| TC-FA-TAG-1454 | TC-FA-TAG-E2E-101 | FE+BE |
| TC-FA-TAG-1455 | TC-FA-TAG-E2E-108 | FE+BE |
| TC-FA-TAG-1456 | TC-FA-TAG-E2E-053 | FE+BE |
| TC-FA-TAG-1457 | TC-FA-TAG-E2E-154 | FE+BE |
| TC-FA-TAG-1458 | TC-FA-TAG-E2E-160 | FE+BE |
| TC-FA-TAG-1459 | TC-FA-TAG-E2E-147 | FE+BE |
| TC-FA-TAG-1460 | TC-FA-TAG-E2E-134 | FE+BE |
| TC-FA-TAG-1461 | TC-FA-TAG-E2E-067 | FE+BE |
| TC-FA-TAG-1462 | TC-FA-TAG-E2E-101 | FE+BE |
| TC-FA-TAG-1463 | TC-FA-TAG-E2E-372 | FE+BE |
| TC-FA-TAG-1464 | TC-FA-TAG-E2E-372 | FE+BE |
| TC-FA-TAG-1465 | TC-FA-TAG-E2E-372 | FE+BE |
| TC-FA-TAG-1466 | TC-FA-TAG-E2E-373 | FE+BE |
| TC-FA-TAG-1467 | TC-FA-TAG-E2E-373 | FE+BE |
| TC-FA-TAG-1468 | TC-FA-TAG-E2E-373 | FE+BE |
| TC-FA-TAG-1469 | TC-FA-TAG-E2E-134 | FE+BE |
| TC-FA-TAG-1470 | TC-FA-TAG-E2E-154 | FE+BE |
| TC-FA-TAG-1471 | TC-FA-TAG-E2E-160 | FE+BE |
| TC-FA-TAG-1472 | TC-FA-TAG-E2E-168 | FE+BE |
| TC-FA-TAG-1473 | TC-FA-TAG-E2E-092 | FE+BE |
| TC-FA-TAG-1474 | TC-FA-TAG-E2E-132 | FE+BE |
| TC-FA-TAG-1475 | TC-FA-TAG-E2E-132 | FE+BE |
| TC-FA-TAG-1476 | TC-FA-TAG-E2E-384 | FE+BE |
| TC-FA-TAG-1477 | TC-FA-TAG-E2E-004 | FE+BE |
| TC-FA-TAG-1478 | TC-FA-TAG-E2E-080 | FE+BE |
| TC-FA-TAG-1479 | TC-FA-TAG-E2E-080 | FE+BE |
| TC-FA-TAG-1480 | TC-FA-TAG-E2E-299 | FE+BE |
| TC-FA-TAG-1481 | TC-FA-TAG-E2E-299 | FE+BE |
| TC-FA-TAG-1482 | TC-FA-TAG-E2E-321 | FE+BE |
| TC-FA-TAG-1483 | TC-FA-TAG-E2E-084 | FE+BE |
| TC-FA-TAG-1484 | TC-FA-TAG-E2E-373 | FE+BE |
| TC-FA-TAG-1485 | TC-FA-TAG-E2E-152 | FE+BE |
| TC-FA-TAG-1486 | TC-FA-TAG-E2E-158 | FE+BE |
| TC-FA-TAG-1487 | TC-FA-TAG-E2E-115 | FE+BE |
| TC-FA-TAG-1488 | TC-FA-TAG-E2E-257 | FE+BE |
| TC-FA-TAG-1489 | TC-FA-TAG-E2E-037 | FE+BE |
| TC-FA-TAG-1490 | TC-FA-TAG-E2E-037 | FE+BE |
| TC-FA-TAG-1491 | TC-FA-TAG-E2E-108 | FE+BE |
| TC-FA-TAG-1492 | TC-FA-TAG-E2E-108 | FE+BE |
| TC-FA-TAG-1493 | TC-FA-TAG-E2E-108 | FE+BE |
| TC-FA-TAG-1494 | TC-FA-TAG-E2E-109 | FE+BE |
| TC-FA-TAG-1495 | TC-FA-TAG-E2E-129 | FE+BE |
| TC-FA-TAG-1496 | TC-FA-TAG-E2E-130 | FE+BE |
| TC-FA-TAG-1497 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1498 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1499 | TC-FA-TAG-E2E-295 | FE+BE |
| TC-FA-TAG-1500 | TC-FA-TAG-E2E-296 | FE+BE |
| TC-FA-TAG-1501 | TC-FA-TAG-E2E-392 | FE+BE |
| TC-FA-TAG-1504 | TC-FA-TAG-E2E-390 | FE+BE |
| TC-FA-TAG-1505 | TC-FA-TAG-E2E-390 | FE+BE |
| TC-FA-TAG-1506 | TC-FA-TAG-E2E-390 | FE+BE |
| TC-FA-TAG-1507 | TC-FA-TAG-E2E-390 | FE+BE |
| TC-FA-TAG-1508 | TC-FA-TAG-E2E-391 | FE+BE |
