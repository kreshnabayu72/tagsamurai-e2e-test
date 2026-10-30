# Coverage E2E — Global Settings > TAG > All Tags

Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (378 TC `TC-GS-TAG-1`–`379`, tanpa TC retired; nomor 353 tidak dipakai sumber). Suite: `specs/GlobalSettings/AllTags/`. Prefix: `GS` + `TAG` (`TC-GS-TAG-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 378 TC masuk 101 spec, 0 TC hanya-BE tidak masuk spec (TC backend memakai ID `TC-GS-TAG-BE-*` di `tc-all-tags-backend.md`, tidak ada rujukan granular `TC-GS-TAG-N` di sana). Setiap TC terpetakan ke tepat satu spec di `sourceTc` (378 dari 378, tanpa duplikat); TC yang ditempatkan tidak menurut urutan nomor dicatat di bagian Pembagian TC lintas spec. Spec 075, 077, 085, 100, dan 101 berstatus `Mode: mock` (keputusan D-3 pada rencana).

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default | Screening Registri TAG: Tab All, Paired, Not Paired (Header, Toolbar, Kolom, Footer) dan Urutan Default Code A-Z | FE+BE | 38 | 1, 2, 3, 4 |
| TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | Isi Sel Registri: Ikon TAG Type, Code dan Popup Combined TAG, Teks Polos, Badge Brand/Model, Badge Status, Last Scanned, dan Kolom Curated | FE+BE | 102 | 5, 6, 7, 8, 9, 10, 11, 378 |
| TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | Kartu Counter: License Counter Tab All, Health Counter Tab Not Paired, Tab Paired Tanpa Kartu, dan Klik Kartu Menyetel Filter | FE+BE | 54 | 12, 14, 15, 16, 17 |
| TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri | Empty State S-01/S-02/S-03 pada Client Tanpa Tag dan Semua Paired, serta Error Load dengan Try Again | FE+BE | 34 | 18, 19, 20, 22 |
| TC-GS-TAG-E2E-005-guided-tooltip-registri-konten-navigasi-dan-flag-seen | Guided Tooltip Registri: Empat Step, Done, Skip, Back Tersembunyi, Replay [?], dan Flag Seen | FE+BE | 0 | 23, 24 |
| TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role | Role Matrix: Visibilitas Elemen Registri per Role (Total Control, Manage TAG Update, Read Only, Manage TAG Read) | FE+BE | 43 | 25, 26, 27, 28 |
| TC-GS-TAG-E2E-007-role-matrix-negatif-sidebar-dan-akses-url-langsung | Role Matrix Negatif: Menu TAG Tidak Tampil di Sidebar dan Akses URL Registri Langsung Ditolak | FE+BE | 7 | 29, 30 |
| TC-GS-TAG-E2E-008-role-matrix-positif-activate-dan-delete-manage-tag-update | Role Matrix Positif: Manage TAG (Update) Menyelesaikan Activate TAG dan Menghapus Tag Available | FE+BE | 19 | 31, 33 |
| TC-GS-TAG-E2E-009-popup-tag-log-akses-lintas-role-dan-role-fams-tanpa-akses-registri | Popup TAG Log: Terbuka untuk Semua Role dan Status, serta Role FAMS Manage asset & TAG Tanpa Akses Registri | FE+BE | 35 | 35, 372, 373 |
| TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar | Plan Tier: Free (Activate Hidden, Tag Terkunci), Downgrade ke Free, dan Plan Berbayar Tanpa Pembatasan Antar-Tier | FE+BE | 50 | 315, 316, 317, 318 |
| TC-GS-TAG-E2E-011-plan-free-audit-dan-delete-by-scan-tag-terkunci | Plan Free: Audit atas Tipe Terkunci Tanpa Baris dan Delete by Scan atas Tag Terkunci Ditolak | FE+BE | 13 | 175 |
| TC-GS-TAG-E2E-012-tenant-suspended-expired-aksi-tulis-ditolak | State Tenant: Aktivasi dan Delete Ditolak Server saat Client Suspended atau Expired | FE+BE | 22 | 319 |
| TC-GS-TAG-E2E-013-capability-dicabut-saat-sesi-activate-terbuka | Capability Manage TAG Dicabut Saat Sesi Activate Terbuka: Commit Ditolak Server | FE+BE | 9 | 320 |
| TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | Defense-in-Depth: Request Langsung Tanpa Capability/Read Only/Read, Isolasi Tenant, Kolisi Tanpa Kebocoran, dan Markup sebagai Teks | FE+BE | 72 | 34, 323, 324, 325, 326, 374, 375 |
| TC-GS-TAG-E2E-015-mobile-registri-tanpa-bulk-activate-gps-manual-dan-visibilitas | Mobile: Tanpa Bulk Delete/Resolve/Remove, Activate GPS Hanya Entri Manual, dan Visibilitas Tombol per Tab dan Role | FE+BE (mobile) | 32 | 332, 333, 334 |
| TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc | Pintu Masuk Activate TAG: Overlay Select TAG Type, Esc, Dialog Ready to Activate, dan Tipe Terkunci | FE+BE | 26 | 36, 37, 38, 42 |
| TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu | Gate Kuota Activate TAG: Sisa 0 Fail-Fast, Terlampaui (60 of 50), dan Sisa Tepat 1 | FE+BE | 24 | 13, 39, 40, 41 |
| TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | Screening Halaman Activate TAG (RFID dan GPS), Info Box Device Communication Address, dan Urutan Tabel Staging | FE+BE | 51 | 43, 44, 45, 46, 47, 48, 166 |
| TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku | Template Self-Purchased: Screening, Locked saat Opsi Mandiri Nonaktif, dan Autofill SKU | FE+BE | 30 | 49, 50, 51, 52 |
| TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | Template Self-Purchased: Brand Baru/Case-Insensitive, Batas 120 Karakter, Emoji, Terisi Sebagian, Clear Field, dan Edit Susulan | FE+BE | 47 | 53, 54, 55, 56, 57, 58 |
| TC-GS-TAG-E2E-021-pemilih-device-name-template-terfilter-category-per-tag-type | Pemilih Device Name Template Terfilter Category per TAG Type (GPS, RFID Object/User, NFC, BLE) | FE+BE | 9 | 354 |
| TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | Pencocokan Real-Time GPS: Official, Damaged/Missing Tetap Official, Self-Purchased, Needs Info, Sudah Aktif, dan In Use Client Lain | FE+BE | 29 | 59, 60, 61, 62, 70, 71 |
| TC-GS-TAG-E2E-023-pencocokan-realtime-error-opsi-mandiri-nonaktif-dan-pool-habis | Pencocokan Real-Time: Error T-10 saat Opsi Mandiri Nonaktif dan Error T-11 saat Pool Sesi Habis | FE+BE | 20 | 63, 64 |
| TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned | Validasi Identifier GPS: Invalid Format, Daftar Preview, Duplicate in File, dan Total Scanned | FE+BE | 39 | 66, 67, 68, 337 |
| TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | Sesi Scan RFID/NFC/BLE di Staging: Pindai Ulang T-02, Format Salah T-32, Pool User TAG, Remove by Scan, Petunjuk Dialog Remove, Normalisasi BLE, dan Info Kuota Header setelah Commit | FE+BE | 50 | 65, 69, 72, 90, 93, 110, 322 |
| TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps | Unggah Berkas GPS: CSV Kolom IMEI, XLSX Sheet Pertama, Tanpa Kolom IMEI T-12, dan Berkas Tidak Valid T-33 | FE+BE | 24 | 73, 74, 75, 76 |
| TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | Row Edit Mode: Resolve Needs Info, Validasi Save, Edit Self-Purchased, Kontrol Lain Nonaktif, Cancel, dan Unsaved Changes | FE+BE | 66 | 77, 78, 79, 80, 81, 82, 83, 355 |
| TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | Bulk Action Bar Staging dan Popup Bulk Resolve: Seleksi Homogen/Campuran, Nilai Identik, Validasi, Unsaved Changes, dan Icon/Severity | FE+BE | 70 | 84, 85, 86, 87, 88, 336, 338 |
| TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error | Remove Baris Staging: Dialog Single, Bulk Remove Jamak, Collapse ke Single, dan Baris Error Tidak Memblokir Submit | FE+BE | 42 | 89, 91, 92, 94 |
| TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error | Submit Activation Diblokir: Baris Needs Info T-05, Staging Kosong T-18, Hanya Baris Error, dan Submit Setelah Dikosongkan | FE+BE | 37 | 95, 96, 97, 331 |
| TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses | Dialog Submit Activation dan Commit Sukses Official/Self-Purchased: Toast T-16, Kartu GPS, dan Last Scanned | FE+BE | 53 | 98, 99, 101, 169 |
| TC-GS-TAG-E2E-032-commit-kolisi-waiting-for-approval-dan-auto-switch-jalur-a | Commit: Self-Purchased Bertabrakan In Use Client Lain (Waiting for Approval, Dialog 8) dan Auto-Switch ke Jalur A | FE+BE | 22 | 100, 167 |
| TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | Commit Sebagian/Semua Gagal: Failed T-06/T-07, Evaluasi Ulang Submit Berikutnya, Waiting for Approval Client Lain, dan Toast T-25 | FE+BE | 51 | 102, 103, 104, 105, 176 |
| TC-GS-TAG-E2E-034-commit-kuota-pool-kurang-dan-kuota-habis-paralel | Commit: Kuota Pool Kurang Saat Submit dan Kuota Habis oleh Sesi Paralel (Rollback Penuh, Dialog 1 Varian Commit) | FE+BE | 24 | 106, 107 |
| TC-GS-TAG-E2E-035-resilience-commit-activate-gagal-server-dan-klik-ganda | Resilience Commit Activate: Gagal Server T-25 dengan Retry Tidak Ganda dan Klik Ganda Submit | FE+BE | 26 | 108, 109 |
| TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | Proteksi Keluar Halaman Activate: Konfirmasi Bawaan Browser, Dialog 9 pada Navigasi In-App, dan Definisi Dirty | FE+BE | 63 | 111, 112, 113, 183, 184, 185 |
| TC-GS-TAG-E2E-037-guided-tooltip-halaman-activate | Guided Tooltip Halaman Activate TAG: Empat Step per Tipe Sesi dan Replay [?] | FE+BE | 17 | 114 |
| TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | Sesi Scan Activate: Reader Belum Tersambung, Page-Lock dan Floating Status Widget, Reader Terputus, Timeout T-29, dan Modal Leave-Page | FE+BE | 54 | 115, 116, 178, 179, 182 |
| TC-GS-TAG-E2E-039-konflik-dua-client-aktivasi-identifier-self-purchased-bersamaan | Konflik Dua Client: Aktivasi Identifier Self-Purchased Baru yang Sama Bersamaan | FE+BE | 11 | 186 |
| TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | Audit TAG: Overlay Select TAG Type, Screening Popup Audit, Daftar Eligible, Combined, Empty State S-06, dan Tombol per Tab | FE+BE | 43 | 117, 118, 119, 120, 121, 122, 137 |
| TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | Audit: Pemindaian Mengubah Lencana ke Verified, Sibling Combined Silent, Kode Belum Aktif T-01, Di Luar Daftar, dan Page-Lock | FE+BE | 43 | 123, 124, 125, 126, 132, 180 |
| TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | Audit Submit Semua Verified: Tanpa Dialog, Recovery Damaged/Missing, Klik Ganda, Last Scanned, dan Role Manage TAG (Update) | FE+BE | 61 | 32, 127, 170, 171, 329 |
| TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | Audit: Dialog Submit Audit, Mark all as Damaged/Missing, Tanpa Centang, Retired Tetap, dan Induk Combined Not Scanned | FE+BE | 75 | 128, 129, 130, 131, 174, 339 |
| TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi | Audit: Dialog Keep Auditing/Discard, Refresh, Submit Gagal Server T-03, dan Tag Dihapus atau Tidak Eligible di Tengah Sesi T-13 | FE+BE | 46 | 133, 134, 135, 136 |
| TC-GS-TAG-E2E-045-konflik-dua-admin-delete-dan-submit-audit-bersamaan | Konflik Dua Admin: Delete Tag yang Sama dan Submit Audit Tipe yang Sama Bersamaan | FE+BE | 34 | 327, 328 |
| TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | Delete Single: Visibilitas Entri Delete per Status, Dialog dan Varian Peringatan, Cancel, dan Tag Combined | FE+BE | 51 | 138, 139, 140, 141, 172, 363 |
| TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi | Bulk Action Bar Tab Not Paired: Counter, Select All, Reserved/Combined Dilewati, Siklus Unselect All, dan Icon/Severity Row Action | FE+BE | 34 | 149, 150, 159, 335 |
| TC-GS-TAG-E2E-048-selection-limit-checkbox-diblokir-dan-select-all-di-cap | Selection Limit: Checkbox ke-(L+1) Diblokir dan Select All Lintas Halaman di-Cap | FE+BE | 16 | 157, 158 |
| TC-GS-TAG-E2E-049-bulk-delete-dialog-screening-varian-peringatan-dan-cancel | Dialog Bulk Delete: Screening, Varian Peringatan (Waiting for Approval/Retired), Collapse Satu Baris, dan Cancel | FE+BE | 31 | 151, 152, 154 |
| TC-GS-TAG-E2E-050-delete-single-sukses-per-status-dan-kuota-kartu | Delete Single Berhasil: Available, Damaged/Missing, dan Retired (Kuota Kembali / Tidak), TAG Log Ikut Terhapus | FE+BE | 20 | 142, 143 |
| TC-GS-TAG-E2E-051-delete-efek-lintas-modul-approvals-dan-tag-stock | Delete: Efek Lintas Modul (Waiting for Approval di Approvals, Unit Stok Official, Unit Self-Purchased) | FE+BE | 25 | 145, 187, 347 |
| TC-GS-TAG-E2E-052-bulk-delete-sukses-sebagian-dilewati-dan-semua-dilewati | Bulk Delete: Sukses (Toast T-22, Seleksi Reset, Kuota, Event Log), Sebagian Dilewati T-31 dengan Delete Detail, dan Semua Dilewati T-24 | FE+BE | 40 | 153, 155, 177 |
| TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | Delete: Tag Di-pair Sebelum Commit T-34, Gagal Server T-23/T-24, Sudah Dihapus Admin Lain, dan Klik Ganda | FE+BE | 48 | 146, 147, 148, 156, 330 |
| TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | Delete by Scan: Penghapusan Langsung T-35, Page-Lock/Widget, Scan Ulang T-08, Sesi Beruntun, dan Pencatatan Sesi | FE+BE | 56 | 161, 164, 165, 181, 359 |
| TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | Delete by Scan: Penolakan Paired/Reserved T-34, Waiting for Approval T-36, Combined, Tak Dikenal T-08/T-09, dan Sesi Tanpa Log | FE+BE | 66 | 162, 163, 173, 357, 362 |
| TC-GS-TAG-E2E-056-delete-by-scan-gagal-server-dan-race-pair | Delete by Scan: Gagal Server/Timeout T-23 dengan Scan Ulang Berhasil dan Tag Di-pair dari FAMS Tepat Sebelum Commit | FE+BE | 31 | 360, 361 |
| TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | Sinkronisasi FAMS: Pair (SSE), Reserved lalu Paired, Aset Ditolak, Unpair, Unpair QR, dan Identifier Belum Aktif Ditolak Modul Konsumen | FE+BE | 61 | 293, 294, 295, 296, 297, 321 |
| TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | Sinkronisasi FAMS Disposal: Tag RFID/NFC Menjadi To be Returned, Penerimaan, Disposal Aset Bertag QR, dan Disposal Aset dengan Tag Combined | FE+BE | 85 | 298, 348, 349, 370, 379 |
| TC-GS-TAG-E2E-059-sinkronisasi-fams-receive-manual-dan-pair-tag-to-be-returned | Sinkronisasi FAMS: Receive Manually Menjadi Damaged/Missing dan Pair TAG ke Tag To be Returned | FE+BE | 24 | 366, 367 |
| TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian | Sinkronisasi FAMS Replace TAG: Hasil Pemindaian Tag Lama, Pengganti To be Returned, Tag Reported, dan Tidak Pernah Retired | FE+BE | 55 | 299, 300, 368, 376 |
| TC-GS-TAG-E2E-061-sinkronisasi-retire-un-retire-combine-dan-separate | Sinkronisasi: Pemensiunan Tag (SSE), Un-Retire dari Supply Asset, serta Combine dan Separate | FE+BE | 42 | 301, 302, 303 |
| TC-GS-TAG-E2E-062-un-retire-ditolak-kuota-penuh-atau-terlampaui | Un-Retire Ditolak oleh Supply Asset saat Kuota Tipe Penuh atau Terpakai Melebihi Kuota | FE+BE | 26 | 350, 351 |
| TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | Sinkronisasi Admin Console: Pemakaian Stok, Kolisi sebagai Activation Collision, Approve, Reject, dan Perubahan Alokasi Kuota | FE+BE | 58 | 304, 305, 306, 307, 308 |
| TC-GS-TAG-E2E-064-approve-reject-kolisi-ditolak-tag-sudah-dihapus | Approve/Reject Kolisi Ditolak saat Tag Sudah Dihapus tetapi Event Delete Belum Diproses | FE+BE | 14 | 352 |
| TC-GS-TAG-E2E-065-sinkronisasi-brand-device-name-dan-sku-katalog | Sinkronisasi Katalog dan Brand: Rename/Hapus Brand, Rename Device Name, dan Perubahan Model/Type SKU Tidak Mengubah Snapshot Tag | FE+BE | 28 | 313, 314, 356 |
| TC-GS-TAG-E2E-066-search-siklus-interaksi-substring-kolom-teks-dan-tanpa-hasil | Search Registri: Siklus Interaksi, Substring Kolom Teks (Code, Device Name, SKU, Source, Type), dan Tanpa Hasil | FE+BE | 36 | 21, 188, 189 |
| TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | Search Registri: Kolom Badge, Ikon TAG Type, Last User, Kolom Tanggal Tidak Searchable, Trim, Terikat Visibilitas Kolom, dan Markup | FE+BE | 38 | 190, 191, 192, 193, 194, 195, 196 |
| TC-GS-TAG-E2E-068-search-by-scan-registri | Search by Scan Registri: Tag Dikenali di Tab Aktif, Tidak di Tab Aktif, Tak Dikenal T-09, dan Last Scanned Tidak Berubah | FE+BE | 35 | 197, 198, 199, 200 |
| TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | Filter Panel: Screening Field, Opsi Populate per Tab, Sinkronisasi Chip, Search Dropdown, Tutup Tanpa Apply, Indikator, dan Persist saat Kolom Di-hide | FE+BE | 71 | 201, 202, 206, 207, 208, 209, 210, 211 |
| TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or | Filter Registri: Nilai per Field, Rentang Last Scanned/Activated At Inklusif, dan Logika OR/AND | FE+BE | 31 | 203, 204, 205, 212 |
| TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | Kombinasi Search, Filter, Sort, dan Pagination: Irisan, Independensi Clear, Pemulihan Empty State, dan Seleksi Bertahan | FE+BE | 86 | 213, 214, 215, 216, 217 |
| TC-GS-TAG-E2E-072-retensi-state-per-tab-dan-refresh | Retensi State: Search/Filter Independen per Tab dan Dipulihkan Setelah Refresh | FE+BE | 45 | 218, 219 |
| TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions | Sort Registri: Kolom Teks (Siklus 3-State, Kosong di Akhir), Ikon TAG Type, dan Kolom Actions Tanpa Sort | FE+BE | 37 | 221, 222, 226 |
| TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user | Sort Registri: Kolom Badge Alfabetis, Kolom Tanggal Oldest/Newest First, dan Last User Berdasarkan Nama Lengkap | FE+BE | 29 | 223, 224, 225 |
| TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard | Setup Column Registri: Screening Column Visibility dan Modal, Tutup Tanpa Save, dan Guard Satu Kolom | mock | 35 | 227, 228, 237, 238 |
| TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | Setup Column Registri: Hide/Show Hideable dan Curated, Reorder, Persistensi setelah Refresh, dan Dibagi Tiga Tab | FE+BE | 59 | 220, 229, 230, 231, 232 |
| TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default | Setup Column Registri: Pin Hideable dan Curated, Batas Pin Ketiga, dan Reset to Default | mock | 60 | 233, 234, 235, 236 |
| TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | Download Registri: Isi File CSV/XLSX Mengikuti Search/Filter/Tab, Nama File, Kolom Tampil, Transformasi Sel, dan Hasil Nol | FE+BE | 58 | 239, 240, 241, 242, 244 |
| TC-GS-TAG-E2E-079-download-registri-gagal | Download Registri Gagal: Toast Error dengan Nama File Tanpa Ekstensi | FE+BE | 4 | 243 |
| TC-GS-TAG-E2E-080-download-registri-lebih-5000-baris | Download Registri lebih dari 5.000 Baris: Loading Screen sampai Berkas Siap | FE+BE | 9 | 346 |
| TC-GS-TAG-E2E-081-pagination-registri-dan-reset-halaman | Pagination Registri: Default, Pilihan Rows per Page, Reset ke Halaman 1 oleh Search/Filter, dan Sort Mempertahankan Halaman | FE+BE | 22 | 245, 246 |
| TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | Modal Event Log: Screening Tab Activate TAG dan Audit TAG, Format Sel, Tombol Hidden di Tab Paired, dan Empty State S-04 | FE+BE | 49 | 247, 248, 249, 250, 251, 252 |
| TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination | Event Log: Search Kolom Searchable, Filter per Tab, Sort 3-State per Kelas Kolom, dan Pagination | FE+BE | 55 | 253, 254, 255, 256 |
| TC-GS-TAG-E2E-084-event-log-download-nama-file-dan-ekstensi | Event Log: Download CSV dan XLSX per Tab (Nama File, Ekstensi, Tanpa Toast Sukses) | FE+BE | 16 | 257 |
| TC-GS-TAG-E2E-085-setup-column-popup-audit-detail-dan-combined-tag | Column Visibility dan Setup Column Surface Sekunder: Popup Audit, Activate TAG Detail, Delete Detail, Audit Detail, dan Popup Combined TAG | mock | 13 | 168 |
| TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | Popup Detail Event Log: Activate TAG Detail, Delete Detail, Audit Detail, Sesi Tanpa Tag Berhasil, Section Kosong, dan Empty State S-07 | FE+BE | 49 | 259, 260, 261, 262, 340, 341, 342 |
| TC-GS-TAG-E2E-087-logging-activate-event-log-activity-log-dan-tanpa-entri-saat-batal | Pencatatan Activate: Satu Event Log dan Satu Activity Log per Operasi, Per Outcome, dan Tanpa Entri saat Submit Kosong atau Dibatalkan | FE+BE | 44 | 263, 264, 269 |
| TC-GS-TAG-E2E-088-logging-audit-submit-event-log-activity-log-dan-update-tag-condition | Pencatatan Audit Submit: Event Log, Activity Log Audit TAG, dan Update TAG Condition per Tag yang Berubah | FE+BE | 33 | 265, 266 |
| TC-GS-TAG-E2E-089-logging-delete-single-dan-bulk-event-log-activity-log | Pencatatan Delete Single dan Bulk: Event Log, Activity Log, dan TAG Type Mixed | FE+BE | 29 | 267, 268 |
| TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage | Atribusi Hardware Handheld Reader: Kolom Hardware Event Log dan Tab Usage untuk Activate, Audit, dan Delete by Scan, serta Tanpa Reader | FE+BE | 50 | 270, 271, 272, 273 |
| TC-GS-TAG-E2E-091-system-log-detail-user-aktor-activate-delete-audit | System Log Detail User Aktor: Entri Activate TAG, Delete TAG, Audit TAG, dan Update TAG Condition Identik dengan Activity Log | FE+BE | 39 | 343, 344, 345 |
| TC-GS-TAG-E2E-092-tag-log-screening-header-empty-state-dan-nilai-kosong | Popup TAG Log: Screening Header dan Daftar Kronologis, Empty State S-05, dan Header Nilai Kosong | FE+BE | 33 | 274, 275, 276 |
| TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | TAG Log: Entri Activated, Waiting for Approval dan Approved, Reserved dan Released, serta Paired per Tipe Entitas (Termasuk Previous Status) | FE+BE | 30 | 277, 278, 279, 280, 369 |
| TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams | TAG Log: Entri Unpaired per Reason, To be Returned dan Received, serta Marked Damaged/Missing dari Receive Manually | FE+BE | 27 | 281, 282, 364, 365 |
| TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired | TAG Log: Entri Audit, Marked Damaged/Missing dan Recovered, Combined dan Separated, serta Retired | FE+BE | 24 | 283, 284, 285, 286 |
| TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | TAG Log: Log QR, Delete dan Scan Tidak Masuk Log, Log Ikut Terhapus, Snapshot Nama Entitas, Last User, Konsistensi Status, dan Log To be Returned Hanya RFID dan NFC | FE+BE | 70 | 287, 288, 289, 290, 291, 292, 377 |
| TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface | Format Tanggal, Waktu, dan Timezone General Settings: Tabel Registri, Filter Panel, Event Log, dan TAG Log | FE+BE | 31 | 309, 310, 311, 312 |
| TC-GS-TAG-E2E-098-delete-tag-to-be-returned-efek-di-fams-single-dan-bulk | Delete: Tag To be Returned Keluar dari Tab To Be Returned FAMS (Single dan Bulk) | FE+BE | 40 | 144, 371 |
| TC-GS-TAG-E2E-099-delete-by-scan-tooltip-dan-tag-to-be-returned-retired-lintas-fams | Delete by Scan: Tooltip dan Scan Tag To be Returned/Retired dengan Efek di FAMS | FE+BE | 29 | 160, 358 |
| TC-GS-TAG-E2E-100-setup-column-tabel-staging-activate-tag | Column Visibility dan Setup Column Tabel Staging Activate TAG GPS | mock | 15 | 168 |
| TC-GS-TAG-E2E-101-setup-column-event-log-dua-tab | Column Visibility dan Setup Column Event Log: Tab Activate TAG dan Tab Audit TAG | mock | 18 | 258 |

## TC hanya-BE (tidak masuk spec)

Tidak ada. Semua 378 TC memiliki permukaan FE; namespace `TC-GS-TAG-BE-NNN` di `tc-all-tags-backend.md` terpisah dan tidak dipetakan ke spec ini.

## Pembagian TC lintas spec

- **TC-GS-TAG-69** berada di spec `025`, bukan `022` (dipetakan menurut topik aksi, bukan urutan nomor).
- **TC-GS-TAG-32** di spec `042`; **TC-GS-TAG-31, 33** di spec `008`.
- **TC-GS-TAG-175** di spec `011`; **TC-GS-TAG-13** (kartu, Client Over) di spec `017`; **TC-GS-TAG-21** (Search tanpa hasil) di spec `066`. TC-13, 21, dan 168 tersebar di Section 1c/1d/3f TC sumber tetapi dipetakan menurut topik aksi (Q-14).
- **TC-GS-TAG-35, 372, 373** di spec `009`; TC-372 menyentuh surface Fixed Asset (selektor milik suite FA, Q-9).
- **TC-GS-TAG-168** (Setup Column surface sekunder, enam surface) dipetakan ke dua spec mock: lima surface popup di `085`, surface staging Activate TAG di `100`; **TC-GS-TAG-258** (Setup Column Event Log) di spec `101`.
- **TC-GS-TAG-110** (kuota header sesi RFID commit) di spec `025`; **TC-GS-TAG-144, 371** di spec `098`; **TC-GS-TAG-160, 358** di spec `099`; **TC-GS-TAG-378** di spec `002`; **TC-GS-TAG-379** di spec `058`.
- **TC-GS-TAG-169** di spec `031`; **TC-GS-TAG-170, 171** di spec `042` (TC-169..171 memakai jeda >= 1 menit antara entri dan Submit, Q-6).
- **Spec 075, 077, 085, 100, 101** berjalan `Mode: mock` (D-3): asersi yang menyangkut state backend nyata tidak teruji pada mode itu. Spec 015 mobile (`FE+BE (mobile)`).
- Spec yang menyentuh modul konsumen (FAMS, Approvals, Admin Console, Supply Asset) memverifikasi hanya sejauh permukaan TAG; langkah dan selektor modul itu ditulis "disediakan tim FE" (Q-9).

## Kebutuhan lingkungan (tim FE)

- Env var password yang sudah terdaftar di `.env.example` dan dipakai suite ini: `GS_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_TC2_PASSWORD`, `FA_ADMIN_PASSWORD`, `GS_CLIENTB_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_LIMIT_TC_PASSWORD`, `GS_TC_EMPTY_PASSWORD`.
- Env var baru yang perlu didaftarkan pemilik repositori di `spectra.config.ts` dan `.env.example` (tanpa nilai; dari bagian Kredensial `suite.md`; file itu tidak diubah stage ini): `GS_TAG_UPDATE_PASSWORD` (Manage TAG: Update), `GS_TAG_READ_PASSWORD` (Manage TAG: Read), `GS_FAMS_ASSETTAG_READ_PASSWORD` dan `GS_FAMS_ASSETTAG_UPDATE_PASSWORD` (Manage asset & TAG di FAMS), serta Total Control per client uji: `GS_TC_ALLPAIRED_PASSWORD`, `GS_TC_FREE_PASSWORD`, `GS_TC_DOWN_PASSWORD`, `GS_TC_NOBYO_PASSWORD`, `GS_TC_QUOTA_PASSWORD`, `GS_TC_OVER_PASSWORD`, `GS_TC_SUSP_PASSWORD`, `GS_TC_AUDIT_PASSWORD`, `GS_TC_LOG_PASSWORD`, `GS_TC_LARGE_PASSWORD`, `GS_TC_PROFESSIONAL_PASSWORD`, `GS_TC_ENTERPRISE_PASSWORD` (16 nama).
- Akun Admin Console (alokasi kuota, katalog, Communication Endpoint) tidak ada di Pre-setup TC dan ditulis "disediakan tim FE".
- Fixture baru: `fixtures/all-tags.json` (identitas saja: Seed Registri A DD-01..DD-30, stok resmi DD-S1..S10, identifier uji DD-N1..N13, Client Free DD-F1/F2, Seed Client Audit DD-31..38, fixture TAG Log DD-39..59, Event Log E-01..E-14 dan A-01..A-12, 5.200 tag Client Large). Identifier EPC/IMEI/UID bersifat tetap dan tidak dapat diberi sufiks per run.
- Kemampuan teknis: simulasi pembaca (reader) untuk sesi scan; intercept jaringan untuk spec mock (075, 077, 085, 100, 101) dan kegagalan; dua sesi browser/API untuk spec multi-konteks; jam server dan browser diatur bersama (TC-169..171); mengubah System Limits (Selection Limit) dan format tanggal/timezone General Settings lalu memulihkannya; fixture BE untuk pemicu "tepat saat commit"; viewport untuk scroll horizontal Setup Column; emulator Android untuk spec 015; membaca berkas unduhan CSV/XLSX.
- Hook suite `before`/`after` mengatur flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate`; hook `beforeEach` membuka Global Settings > TAG, Tab All.
- Suite berjalan serial (`parallel: false`, executionOrder 1.8) dengan reset fixture BE per spec; identifier tetap dan hitungan tetap valid hanya bila tidak ada spec lain yang mengubah Seed Registri A (Q-4).

## Temuan untuk QA

Indeks; rincian dan keputusan ada di `work-items/gs-all-tags/plan-e2e-generate-spec.md` (Q-1..Q-15) dan di bagian Notes tiap spec.

- **Simulasi reader (Q-1):** TC bertanda scan hardware (Manual Only) tetap ditulis sebagai spec; cara simulasi reader tidak didefinisikan di TC, PRD, atau LLD (sesi scan Activate/Audit/Delete by Scan/Search by Scan dan atribusi hardware).
- **Akun/email tidak sinkron dengan `.env.example` (Q-2):** Pre-setup TC memakai `totalControl2_automated_qaTeam1` dan `principalApprover_automated`; `.env.example` mendaftarkan `totalControlSecond_automated_qaTeam1` dan `totalControlPrincipal_automated_qaTeam1`. Spec memakai akun Pre-setup TC; kesamaan perlu dikonfirmasi (TC-327, 328, 145, 305..307, 352).
- **Identifier tetap dan suite serial (Q-4, Q-12):** EPC/IMEI/UID tidak bisa diberi sufiks per run; hitungan tetap bergantung reset fixture BE; TC-309 dan TC-312 mengubah state global Client A (format tanggal/timezone) dan dipulihkan di hook `after`.
- **Pemicu tidak deterministik (Q-5, Q-6):** pemicu "tepat saat commit"/"antara re-check dan penulisan" (TC-102, 103, 105, 107, 146, 148, 186, 328, 361) ditulis sebagai fixture BE; TC-169..171 butuh jeda >= 1 menit, jam diatur bukan menunggu.
- **Selektor modul lain tidak terdefinisi (Q-9, Q-10, Q-15):** FAMS, Approvals, Admin Console, Supply Asset, Fixed Asset > TAG (TC-372), pelaku TAG Log; ditulis "disediakan tim FE".
- **Nilai tidak ditetapkan di TC (Q-3, Q-7, Q-11, Q-12):** Domain/IP Info Box GPS (TC-44..47, 166), nilai Selection Limit `L` (TC-157, 158), viewport scroll horizontal Setup Column (TC-233, 234), timezone target TC-312.
- **Expected terlalu umum (Q-8, Q-10):** TC-292 (konsistensi status vs log), TC-318 ("UI identik" tanpa baseline), TC-321 (copy penolakan modul konsumen), TC-328 ("commit membaca ulang status terkini"); spec mengikuti TC.
- **Informasional (Q-13, Q-14):** metadata VAL/PRD? turunan dari Tabel Data Uji (TC-65, 67, 169..171, 184, 312); penempatan topik TC-13, 21, 168.

## Keputusan yang sudah diambil

- **Spec panjang:** 50 dari 101 spec memuat lebih dari 35 langkah; alasan pertahanan tercatat di `## Notes` tiap spec. Spec di atas 60 langkah (langkah tertulis; ekspansi perulangan tidak dihitung): 002 (102), 071 (86), 058 (85), 043 (75), 014 (72), 069 (71), 096 (70), 028 (70), 055 (66), 027 (66), 036 (63), 057 (61), 042 (61).
- **D-3:** spec 075, 077, 085, 100, 101 `Mode: mock`; selebihnya `FE+BE`, spec 015 mobile.
- **Pembagian slice dan D-1..D-5** mengikuti rencana yang disetujui user di `work-items/gs-all-tags/plan-e2e-generate-spec.md`.

## Tindak lanjut di luar stage ini

- **Tim FE:** mendaftarkan env var baru (16 nama) di `spectra.config.ts` dan `.env.example` (bagian Kebutuhan lingkungan), mengonfirmasi akun (Q-2), menyediakan mekanisme reader, fixture BE, akun Admin Console, dan selektor modul konsumen.
- **QA (perbaikan TC sumber):** Expected TC-292, 318, 321, 328; nilai TC-44..47 dan 166, TC-157/158, TC-233/234, TC-312.
- Tidak ada PRD atau TC yang diubah oleh stage ini.
- **Keputusan terbuka:** TC-168 muncul di `sourceTc` spec 085 dan 100 (satu TC enam surface, dipisah karena Mode mock dan ukuran); `check-suite` C2 menandainya. Putuskan: izinkan pengecualian di konvensi atau gabungkan 100 ke 085.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-TAG-1 | TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default | FE+BE |
| TC-GS-TAG-2 | TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default | FE+BE |
| TC-GS-TAG-3 | TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default | FE+BE |
| TC-GS-TAG-4 | TC-GS-TAG-E2E-001-screening-registri-tiga-tab-layout-kolom-dan-urutan-default | FE+BE |
| TC-GS-TAG-5 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-6 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-7 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-8 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-9 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-10 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-11 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-12 | TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | FE+BE |
| TC-GS-TAG-13 | TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu | FE+BE |
| TC-GS-TAG-14 | TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | FE+BE |
| TC-GS-TAG-15 | TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | FE+BE |
| TC-GS-TAG-16 | TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | FE+BE |
| TC-GS-TAG-17 | TC-GS-TAG-E2E-003-kartu-counter-lisensi-kesehatan-dan-klik-kartu | FE+BE |
| TC-GS-TAG-18 | TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri | FE+BE |
| TC-GS-TAG-19 | TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri | FE+BE |
| TC-GS-TAG-20 | TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri | FE+BE |
| TC-GS-TAG-21 | TC-GS-TAG-E2E-066-search-siklus-interaksi-substring-kolom-teks-dan-tanpa-hasil | FE+BE |
| TC-GS-TAG-22 | TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri | FE+BE |
| TC-GS-TAG-23 | TC-GS-TAG-E2E-005-guided-tooltip-registri-konten-navigasi-dan-flag-seen | FE+BE |
| TC-GS-TAG-24 | TC-GS-TAG-E2E-005-guided-tooltip-registri-konten-navigasi-dan-flag-seen | FE+BE |
| TC-GS-TAG-25 | TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role | FE+BE |
| TC-GS-TAG-26 | TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role | FE+BE |
| TC-GS-TAG-27 | TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role | FE+BE |
| TC-GS-TAG-28 | TC-GS-TAG-E2E-006-role-matrix-visibilitas-elemen-registri-per-role | FE+BE |
| TC-GS-TAG-29 | TC-GS-TAG-E2E-007-role-matrix-negatif-sidebar-dan-akses-url-langsung | FE+BE |
| TC-GS-TAG-30 | TC-GS-TAG-E2E-007-role-matrix-negatif-sidebar-dan-akses-url-langsung | FE+BE |
| TC-GS-TAG-31 | TC-GS-TAG-E2E-008-role-matrix-positif-activate-dan-delete-manage-tag-update | FE+BE |
| TC-GS-TAG-32 | TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | FE+BE |
| TC-GS-TAG-33 | TC-GS-TAG-E2E-008-role-matrix-positif-activate-dan-delete-manage-tag-update | FE+BE |
| TC-GS-TAG-34 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-35 | TC-GS-TAG-E2E-009-popup-tag-log-akses-lintas-role-dan-role-fams-tanpa-akses-registri | FE+BE |
| TC-GS-TAG-36 | TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc | FE+BE |
| TC-GS-TAG-37 | TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc | FE+BE |
| TC-GS-TAG-38 | TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc | FE+BE |
| TC-GS-TAG-39 | TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu | FE+BE |
| TC-GS-TAG-40 | TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu | FE+BE |
| TC-GS-TAG-41 | TC-GS-TAG-E2E-017-gate-kuota-sisa-nol-terlampaui-dan-sisa-satu | FE+BE |
| TC-GS-TAG-42 | TC-GS-TAG-E2E-016-pintu-masuk-overlay-select-tag-type-dialog-pengantar-dan-esc | FE+BE |
| TC-GS-TAG-43 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-44 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-45 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-46 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-47 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-48 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-49 | TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku | FE+BE |
| TC-GS-TAG-50 | TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku | FE+BE |
| TC-GS-TAG-51 | TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku | FE+BE |
| TC-GS-TAG-52 | TC-GS-TAG-E2E-019-template-self-purchased-screening-locked-dan-autofill-sku | FE+BE |
| TC-GS-TAG-53 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-54 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-55 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-56 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-57 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-58 | TC-GS-TAG-E2E-020-template-self-purchased-validasi-brand-clear-field-dan-edit-susulan | FE+BE |
| TC-GS-TAG-59 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-60 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-61 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-62 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-63 | TC-GS-TAG-E2E-023-pencocokan-realtime-error-opsi-mandiri-nonaktif-dan-pool-habis | FE+BE |
| TC-GS-TAG-64 | TC-GS-TAG-E2E-023-pencocokan-realtime-error-opsi-mandiri-nonaktif-dan-pool-habis | FE+BE |
| TC-GS-TAG-65 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-66 | TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned | FE+BE |
| TC-GS-TAG-67 | TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned | FE+BE |
| TC-GS-TAG-68 | TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned | FE+BE |
| TC-GS-TAG-69 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-70 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-71 | TC-GS-TAG-E2E-022-pencocokan-realtime-lencana-staging-gps | FE+BE |
| TC-GS-TAG-72 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-73 | TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps | FE+BE |
| TC-GS-TAG-74 | TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps | FE+BE |
| TC-GS-TAG-75 | TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps | FE+BE |
| TC-GS-TAG-76 | TC-GS-TAG-E2E-026-unggah-berkas-csv-xlsx-gps | FE+BE |
| TC-GS-TAG-77 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-78 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-79 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-80 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-81 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-82 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-83 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-84 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-85 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-86 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-87 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-88 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-89 | TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error | FE+BE |
| TC-GS-TAG-90 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-91 | TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error | FE+BE |
| TC-GS-TAG-92 | TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error | FE+BE |
| TC-GS-TAG-93 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-94 | TC-GS-TAG-E2E-029-remove-baris-staging-dialog-single-bulk-dan-baris-error | FE+BE |
| TC-GS-TAG-95 | TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error | FE+BE |
| TC-GS-TAG-96 | TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error | FE+BE |
| TC-GS-TAG-97 | TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error | FE+BE |
| TC-GS-TAG-98 | TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses | FE+BE |
| TC-GS-TAG-99 | TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses | FE+BE |
| TC-GS-TAG-100 | TC-GS-TAG-E2E-032-commit-kolisi-waiting-for-approval-dan-auto-switch-jalur-a | FE+BE |
| TC-GS-TAG-101 | TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses | FE+BE |
| TC-GS-TAG-102 | TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | FE+BE |
| TC-GS-TAG-103 | TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | FE+BE |
| TC-GS-TAG-104 | TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | FE+BE |
| TC-GS-TAG-105 | TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | FE+BE |
| TC-GS-TAG-106 | TC-GS-TAG-E2E-034-commit-kuota-pool-kurang-dan-kuota-habis-paralel | FE+BE |
| TC-GS-TAG-107 | TC-GS-TAG-E2E-034-commit-kuota-pool-kurang-dan-kuota-habis-paralel | FE+BE |
| TC-GS-TAG-108 | TC-GS-TAG-E2E-035-resilience-commit-activate-gagal-server-dan-klik-ganda | FE+BE |
| TC-GS-TAG-109 | TC-GS-TAG-E2E-035-resilience-commit-activate-gagal-server-dan-klik-ganda | FE+BE |
| TC-GS-TAG-110 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-111 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-112 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-113 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-114 | TC-GS-TAG-E2E-037-guided-tooltip-halaman-activate | FE+BE |
| TC-GS-TAG-115 | TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | FE+BE |
| TC-GS-TAG-116 | TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | FE+BE |
| TC-GS-TAG-117 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-118 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-119 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-120 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-121 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-122 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-123 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-124 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-125 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-126 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-127 | TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | FE+BE |
| TC-GS-TAG-128 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-129 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-130 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-131 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-132 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-133 | TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi | FE+BE |
| TC-GS-TAG-134 | TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi | FE+BE |
| TC-GS-TAG-135 | TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi | FE+BE |
| TC-GS-TAG-136 | TC-GS-TAG-E2E-044-audit-tutup-popup-refresh-gagal-server-dan-tag-berubah-tengah-sesi | FE+BE |
| TC-GS-TAG-137 | TC-GS-TAG-E2E-040-audit-overlay-select-tag-type-screening-popup-dan-tombol-per-tab | FE+BE |
| TC-GS-TAG-138 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-139 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-140 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-141 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-142 | TC-GS-TAG-E2E-050-delete-single-sukses-per-status-dan-kuota-kartu | FE+BE |
| TC-GS-TAG-143 | TC-GS-TAG-E2E-050-delete-single-sukses-per-status-dan-kuota-kartu | FE+BE |
| TC-GS-TAG-144 | TC-GS-TAG-E2E-098-delete-tag-to-be-returned-efek-di-fams-single-dan-bulk | FE+BE |
| TC-GS-TAG-145 | TC-GS-TAG-E2E-051-delete-efek-lintas-modul-approvals-dan-tag-stock | FE+BE |
| TC-GS-TAG-146 | TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | FE+BE |
| TC-GS-TAG-147 | TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | FE+BE |
| TC-GS-TAG-148 | TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | FE+BE |
| TC-GS-TAG-149 | TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi | FE+BE |
| TC-GS-TAG-150 | TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi | FE+BE |
| TC-GS-TAG-151 | TC-GS-TAG-E2E-049-bulk-delete-dialog-screening-varian-peringatan-dan-cancel | FE+BE |
| TC-GS-TAG-152 | TC-GS-TAG-E2E-049-bulk-delete-dialog-screening-varian-peringatan-dan-cancel | FE+BE |
| TC-GS-TAG-153 | TC-GS-TAG-E2E-052-bulk-delete-sukses-sebagian-dilewati-dan-semua-dilewati | FE+BE |
| TC-GS-TAG-154 | TC-GS-TAG-E2E-049-bulk-delete-dialog-screening-varian-peringatan-dan-cancel | FE+BE |
| TC-GS-TAG-155 | TC-GS-TAG-E2E-052-bulk-delete-sukses-sebagian-dilewati-dan-semua-dilewati | FE+BE |
| TC-GS-TAG-156 | TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | FE+BE |
| TC-GS-TAG-157 | TC-GS-TAG-E2E-048-selection-limit-checkbox-diblokir-dan-select-all-di-cap | FE+BE |
| TC-GS-TAG-158 | TC-GS-TAG-E2E-048-selection-limit-checkbox-diblokir-dan-select-all-di-cap | FE+BE |
| TC-GS-TAG-159 | TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi | FE+BE |
| TC-GS-TAG-160 | TC-GS-TAG-E2E-099-delete-by-scan-tooltip-dan-tag-to-be-returned-retired-lintas-fams | FE+BE |
| TC-GS-TAG-161 | TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | FE+BE |
| TC-GS-TAG-162 | TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | FE+BE |
| TC-GS-TAG-163 | TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | FE+BE |
| TC-GS-TAG-164 | TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | FE+BE |
| TC-GS-TAG-165 | TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | FE+BE |
| TC-GS-TAG-166 | TC-GS-TAG-E2E-018-screening-halaman-activate-rfid-gps-dan-info-box | FE+BE |
| TC-GS-TAG-167 | TC-GS-TAG-E2E-032-commit-kolisi-waiting-for-approval-dan-auto-switch-jalur-a | FE+BE |
| TC-GS-TAG-168 | TC-GS-TAG-E2E-085-setup-column-popup-audit-detail-dan-combined-tag | mock |
| TC-GS-TAG-168 | TC-GS-TAG-E2E-100-setup-column-tabel-staging-activate-tag | mock |
| TC-GS-TAG-169 | TC-GS-TAG-E2E-031-dialog-submit-activation-dan-commit-sukses | FE+BE |
| TC-GS-TAG-170 | TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | FE+BE |
| TC-GS-TAG-171 | TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | FE+BE |
| TC-GS-TAG-172 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-173 | TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | FE+BE |
| TC-GS-TAG-174 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-175 | TC-GS-TAG-E2E-011-plan-free-audit-dan-delete-by-scan-tag-terkunci | FE+BE |
| TC-GS-TAG-176 | TC-GS-TAG-E2E-033-commit-sebagian-gagal-failed-evaluasi-ulang-dan-semua-gagal | FE+BE |
| TC-GS-TAG-177 | TC-GS-TAG-E2E-052-bulk-delete-sukses-sebagian-dilewati-dan-semua-dilewati | FE+BE |
| TC-GS-TAG-178 | TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | FE+BE |
| TC-GS-TAG-179 | TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | FE+BE |
| TC-GS-TAG-180 | TC-GS-TAG-E2E-041-audit-pemindaian-lencana-verified-sibling-dan-penolakan | FE+BE |
| TC-GS-TAG-181 | TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | FE+BE |
| TC-GS-TAG-182 | TC-GS-TAG-E2E-038-sesi-scan-activate-page-lock-reader-terputus-timeout-dan-leave-page | FE+BE |
| TC-GS-TAG-183 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-184 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-185 | TC-GS-TAG-E2E-036-proteksi-keluar-halaman-activate-refresh-navigasi-dan-dirty | FE+BE |
| TC-GS-TAG-186 | TC-GS-TAG-E2E-039-konflik-dua-client-aktivasi-identifier-self-purchased-bersamaan | FE+BE |
| TC-GS-TAG-187 | TC-GS-TAG-E2E-051-delete-efek-lintas-modul-approvals-dan-tag-stock | FE+BE |
| TC-GS-TAG-188 | TC-GS-TAG-E2E-066-search-siklus-interaksi-substring-kolom-teks-dan-tanpa-hasil | FE+BE |
| TC-GS-TAG-189 | TC-GS-TAG-E2E-066-search-siklus-interaksi-substring-kolom-teks-dan-tanpa-hasil | FE+BE |
| TC-GS-TAG-190 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-191 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-192 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-193 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-194 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-195 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-196 | TC-GS-TAG-E2E-067-search-kolom-badge-ikon-last-user-tanggal-trim-visibilitas-dan-markup | FE+BE |
| TC-GS-TAG-197 | TC-GS-TAG-E2E-068-search-by-scan-registri | FE+BE |
| TC-GS-TAG-198 | TC-GS-TAG-E2E-068-search-by-scan-registri | FE+BE |
| TC-GS-TAG-199 | TC-GS-TAG-E2E-068-search-by-scan-registri | FE+BE |
| TC-GS-TAG-200 | TC-GS-TAG-E2E-068-search-by-scan-registri | FE+BE |
| TC-GS-TAG-201 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-202 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-203 | TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or | FE+BE |
| TC-GS-TAG-204 | TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or | FE+BE |
| TC-GS-TAG-205 | TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or | FE+BE |
| TC-GS-TAG-206 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-207 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-208 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-209 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-210 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-211 | TC-GS-TAG-E2E-069-filter-panel-screening-opsi-populate-chip-dan-tutup-tanpa-apply | FE+BE |
| TC-GS-TAG-212 | TC-GS-TAG-E2E-070-filter-nilai-per-field-rentang-tanggal-dan-logika-and-or | FE+BE |
| TC-GS-TAG-213 | TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | FE+BE |
| TC-GS-TAG-214 | TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | FE+BE |
| TC-GS-TAG-215 | TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | FE+BE |
| TC-GS-TAG-216 | TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | FE+BE |
| TC-GS-TAG-217 | TC-GS-TAG-E2E-071-kombinasi-search-filter-sort-pagination-dan-pemulihan-empty-state | FE+BE |
| TC-GS-TAG-218 | TC-GS-TAG-E2E-072-retensi-state-per-tab-dan-refresh | FE+BE |
| TC-GS-TAG-219 | TC-GS-TAG-E2E-072-retensi-state-per-tab-dan-refresh | FE+BE |
| TC-GS-TAG-220 | TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | FE+BE |
| TC-GS-TAG-221 | TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions | FE+BE |
| TC-GS-TAG-222 | TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions | FE+BE |
| TC-GS-TAG-223 | TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user | FE+BE |
| TC-GS-TAG-224 | TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user | FE+BE |
| TC-GS-TAG-225 | TC-GS-TAG-E2E-074-sort-kolom-badge-tanggal-dan-last-user | FE+BE |
| TC-GS-TAG-226 | TC-GS-TAG-E2E-073-sort-kolom-teks-ikon-dan-actions | FE+BE |
| TC-GS-TAG-227 | TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard | mock |
| TC-GS-TAG-228 | TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard | mock |
| TC-GS-TAG-229 | TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | FE+BE |
| TC-GS-TAG-230 | TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | FE+BE |
| TC-GS-TAG-231 | TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | FE+BE |
| TC-GS-TAG-232 | TC-GS-TAG-E2E-076-setup-column-hide-curated-reorder-persistensi-dan-lintas-tab | FE+BE |
| TC-GS-TAG-233 | TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default | mock |
| TC-GS-TAG-234 | TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default | mock |
| TC-GS-TAG-235 | TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default | mock |
| TC-GS-TAG-236 | TC-GS-TAG-E2E-077-setup-column-pin-dan-reset-to-default | mock |
| TC-GS-TAG-237 | TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard | mock |
| TC-GS-TAG-238 | TC-GS-TAG-E2E-075-setup-column-screening-overlay-modal-tutup-dan-guard | mock |
| TC-GS-TAG-239 | TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | FE+BE |
| TC-GS-TAG-240 | TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | FE+BE |
| TC-GS-TAG-241 | TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | FE+BE |
| TC-GS-TAG-242 | TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | FE+BE |
| TC-GS-TAG-243 | TC-GS-TAG-E2E-079-download-registri-gagal | FE+BE |
| TC-GS-TAG-244 | TC-GS-TAG-E2E-078-download-registri-isi-file-nama-kolom-dan-hasil-nol | FE+BE |
| TC-GS-TAG-245 | TC-GS-TAG-E2E-081-pagination-registri-dan-reset-halaman | FE+BE |
| TC-GS-TAG-246 | TC-GS-TAG-E2E-081-pagination-registri-dan-reset-halaman | FE+BE |
| TC-GS-TAG-247 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-248 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-249 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-250 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-251 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-252 | TC-GS-TAG-E2E-082-event-log-screening-dua-tab-format-sel-dan-empty-state | FE+BE |
| TC-GS-TAG-253 | TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-TAG-254 | TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-TAG-255 | TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-TAG-256 | TC-GS-TAG-E2E-083-event-log-search-filter-sort-dan-pagination | FE+BE |
| TC-GS-TAG-257 | TC-GS-TAG-E2E-084-event-log-download-nama-file-dan-ekstensi | FE+BE |
| TC-GS-TAG-258 | TC-GS-TAG-E2E-101-setup-column-event-log-dua-tab | mock |
| TC-GS-TAG-259 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-260 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-261 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-262 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-263 | TC-GS-TAG-E2E-087-logging-activate-event-log-activity-log-dan-tanpa-entri-saat-batal | FE+BE |
| TC-GS-TAG-264 | TC-GS-TAG-E2E-087-logging-activate-event-log-activity-log-dan-tanpa-entri-saat-batal | FE+BE |
| TC-GS-TAG-265 | TC-GS-TAG-E2E-088-logging-audit-submit-event-log-activity-log-dan-update-tag-condition | FE+BE |
| TC-GS-TAG-266 | TC-GS-TAG-E2E-088-logging-audit-submit-event-log-activity-log-dan-update-tag-condition | FE+BE |
| TC-GS-TAG-267 | TC-GS-TAG-E2E-089-logging-delete-single-dan-bulk-event-log-activity-log | FE+BE |
| TC-GS-TAG-268 | TC-GS-TAG-E2E-089-logging-delete-single-dan-bulk-event-log-activity-log | FE+BE |
| TC-GS-TAG-269 | TC-GS-TAG-E2E-087-logging-activate-event-log-activity-log-dan-tanpa-entri-saat-batal | FE+BE |
| TC-GS-TAG-270 | TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage | FE+BE |
| TC-GS-TAG-271 | TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage | FE+BE |
| TC-GS-TAG-272 | TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage | FE+BE |
| TC-GS-TAG-273 | TC-GS-TAG-E2E-090-atribusi-hardware-handheld-reader-dan-tab-usage | FE+BE |
| TC-GS-TAG-274 | TC-GS-TAG-E2E-092-tag-log-screening-header-empty-state-dan-nilai-kosong | FE+BE |
| TC-GS-TAG-275 | TC-GS-TAG-E2E-092-tag-log-screening-header-empty-state-dan-nilai-kosong | FE+BE |
| TC-GS-TAG-276 | TC-GS-TAG-E2E-092-tag-log-screening-header-empty-state-dan-nilai-kosong | FE+BE |
| TC-GS-TAG-277 | TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | FE+BE |
| TC-GS-TAG-278 | TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | FE+BE |
| TC-GS-TAG-279 | TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | FE+BE |
| TC-GS-TAG-280 | TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | FE+BE |
| TC-GS-TAG-281 | TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams | FE+BE |
| TC-GS-TAG-282 | TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams | FE+BE |
| TC-GS-TAG-283 | TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired | FE+BE |
| TC-GS-TAG-284 | TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired | FE+BE |
| TC-GS-TAG-285 | TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired | FE+BE |
| TC-GS-TAG-286 | TC-GS-TAG-E2E-095-tag-log-entri-audit-recovered-combined-separated-dan-retired | FE+BE |
| TC-GS-TAG-287 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-288 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-289 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-290 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-291 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-292 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-293 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-294 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-295 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-296 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-297 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-298 | TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | FE+BE |
| TC-GS-TAG-299 | TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian | FE+BE |
| TC-GS-TAG-300 | TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian | FE+BE |
| TC-GS-TAG-301 | TC-GS-TAG-E2E-061-sinkronisasi-retire-un-retire-combine-dan-separate | FE+BE |
| TC-GS-TAG-302 | TC-GS-TAG-E2E-061-sinkronisasi-retire-un-retire-combine-dan-separate | FE+BE |
| TC-GS-TAG-303 | TC-GS-TAG-E2E-061-sinkronisasi-retire-un-retire-combine-dan-separate | FE+BE |
| TC-GS-TAG-304 | TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | FE+BE |
| TC-GS-TAG-305 | TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | FE+BE |
| TC-GS-TAG-306 | TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | FE+BE |
| TC-GS-TAG-307 | TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | FE+BE |
| TC-GS-TAG-308 | TC-GS-TAG-E2E-063-sinkronisasi-admin-console-stok-kolisi-approve-reject-dan-kuota | FE+BE |
| TC-GS-TAG-309 | TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface | FE+BE |
| TC-GS-TAG-310 | TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface | FE+BE |
| TC-GS-TAG-311 | TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface | FE+BE |
| TC-GS-TAG-312 | TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface | FE+BE |
| TC-GS-TAG-313 | TC-GS-TAG-E2E-065-sinkronisasi-brand-device-name-dan-sku-katalog | FE+BE |
| TC-GS-TAG-314 | TC-GS-TAG-E2E-065-sinkronisasi-brand-device-name-dan-sku-katalog | FE+BE |
| TC-GS-TAG-315 | TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar | FE+BE |
| TC-GS-TAG-316 | TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar | FE+BE |
| TC-GS-TAG-317 | TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar | FE+BE |
| TC-GS-TAG-318 | TC-GS-TAG-E2E-010-plan-tier-free-downgrade-dan-plan-berbayar | FE+BE |
| TC-GS-TAG-319 | TC-GS-TAG-E2E-012-tenant-suspended-expired-aksi-tulis-ditolak | FE+BE |
| TC-GS-TAG-320 | TC-GS-TAG-E2E-013-capability-dicabut-saat-sesi-activate-terbuka | FE+BE |
| TC-GS-TAG-321 | TC-GS-TAG-E2E-057-sinkronisasi-fams-pair-reserve-release-unpair-dan-penolakan-konsumen | FE+BE |
| TC-GS-TAG-322 | TC-GS-TAG-E2E-025-sesi-scan-rfid-nfc-ble-staging-format-pool-remove-dan-normalisasi | FE+BE |
| TC-GS-TAG-323 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-324 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-325 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-326 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-327 | TC-GS-TAG-E2E-045-konflik-dua-admin-delete-dan-submit-audit-bersamaan | FE+BE |
| TC-GS-TAG-328 | TC-GS-TAG-E2E-045-konflik-dua-admin-delete-dan-submit-audit-bersamaan | FE+BE |
| TC-GS-TAG-329 | TC-GS-TAG-E2E-042-audit-submit-semua-verified-recovery-dan-last-scanned | FE+BE |
| TC-GS-TAG-330 | TC-GS-TAG-E2E-053-delete-konflik-dan-kegagalan-server-single-dan-bulk | FE+BE |
| TC-GS-TAG-331 | TC-GS-TAG-E2E-030-submit-activation-diblokir-needs-info-staging-kosong-dan-hanya-error | FE+BE |
| TC-GS-TAG-332 | TC-GS-TAG-E2E-015-mobile-registri-tanpa-bulk-activate-gps-manual-dan-visibilitas | FE+BE (mobile) |
| TC-GS-TAG-333 | TC-GS-TAG-E2E-015-mobile-registri-tanpa-bulk-activate-gps-manual-dan-visibilitas | FE+BE (mobile) |
| TC-GS-TAG-334 | TC-GS-TAG-E2E-015-mobile-registri-tanpa-bulk-activate-gps-manual-dan-visibilitas | FE+BE (mobile) |
| TC-GS-TAG-335 | TC-GS-TAG-E2E-047-bulk-action-bar-registri-counter-select-all-dan-icon-aksi | FE+BE |
| TC-GS-TAG-336 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-337 | TC-GS-TAG-E2E-024-validasi-identifier-gps-preview-duplicate-in-file-dan-total-scanned | FE+BE |
| TC-GS-TAG-338 | TC-GS-TAG-E2E-028-bulk-resolve-dan-bulk-action-bar-staging | FE+BE |
| TC-GS-TAG-339 | TC-GS-TAG-E2E-043-audit-dialog-submit-audit-checkbox-dan-hasil-status | FE+BE |
| TC-GS-TAG-340 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-341 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-342 | TC-GS-TAG-E2E-086-event-log-popup-detail-activate-delete-audit-dan-empty-state | FE+BE |
| TC-GS-TAG-343 | TC-GS-TAG-E2E-091-system-log-detail-user-aktor-activate-delete-audit | FE+BE |
| TC-GS-TAG-344 | TC-GS-TAG-E2E-091-system-log-detail-user-aktor-activate-delete-audit | FE+BE |
| TC-GS-TAG-345 | TC-GS-TAG-E2E-091-system-log-detail-user-aktor-activate-delete-audit | FE+BE |
| TC-GS-TAG-346 | TC-GS-TAG-E2E-080-download-registri-lebih-5000-baris | FE+BE |
| TC-GS-TAG-347 | TC-GS-TAG-E2E-051-delete-efek-lintas-modul-approvals-dan-tag-stock | FE+BE |
| TC-GS-TAG-348 | TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | FE+BE |
| TC-GS-TAG-349 | TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | FE+BE |
| TC-GS-TAG-350 | TC-GS-TAG-E2E-062-un-retire-ditolak-kuota-penuh-atau-terlampaui | FE+BE |
| TC-GS-TAG-351 | TC-GS-TAG-E2E-062-un-retire-ditolak-kuota-penuh-atau-terlampaui | FE+BE |
| TC-GS-TAG-352 | TC-GS-TAG-E2E-064-approve-reject-kolisi-ditolak-tag-sudah-dihapus | FE+BE |
| TC-GS-TAG-354 | TC-GS-TAG-E2E-021-pemilih-device-name-template-terfilter-category-per-tag-type | FE+BE |
| TC-GS-TAG-355 | TC-GS-TAG-E2E-027-row-edit-mode-resolve-needs-info-dan-edit-self-purchased | FE+BE |
| TC-GS-TAG-356 | TC-GS-TAG-E2E-065-sinkronisasi-brand-device-name-dan-sku-katalog | FE+BE |
| TC-GS-TAG-357 | TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | FE+BE |
| TC-GS-TAG-358 | TC-GS-TAG-E2E-099-delete-by-scan-tooltip-dan-tag-to-be-returned-retired-lintas-fams | FE+BE |
| TC-GS-TAG-359 | TC-GS-TAG-E2E-054-delete-by-scan-page-lock-dan-penghapusan-sukses | FE+BE |
| TC-GS-TAG-360 | TC-GS-TAG-E2E-056-delete-by-scan-gagal-server-dan-race-pair | FE+BE |
| TC-GS-TAG-361 | TC-GS-TAG-E2E-056-delete-by-scan-gagal-server-dan-race-pair | FE+BE |
| TC-GS-TAG-362 | TC-GS-TAG-E2E-055-delete-by-scan-penolakan-dan-sesi-tanpa-penghapusan | FE+BE |
| TC-GS-TAG-363 | TC-GS-TAG-E2E-046-delete-single-entri-menu-baris-dialog-cancel-dan-tag-combined | FE+BE |
| TC-GS-TAG-364 | TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams | FE+BE |
| TC-GS-TAG-365 | TC-GS-TAG-E2E-094-tag-log-entri-unpaired-to-be-returned-received-dan-damaged-missing-fams | FE+BE |
| TC-GS-TAG-366 | TC-GS-TAG-E2E-059-sinkronisasi-fams-receive-manual-dan-pair-tag-to-be-returned | FE+BE |
| TC-GS-TAG-367 | TC-GS-TAG-E2E-059-sinkronisasi-fams-receive-manual-dan-pair-tag-to-be-returned | FE+BE |
| TC-GS-TAG-368 | TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian | FE+BE |
| TC-GS-TAG-369 | TC-GS-TAG-E2E-093-tag-log-entri-activated-approval-reserved-released-dan-paired | FE+BE |
| TC-GS-TAG-370 | TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | FE+BE |
| TC-GS-TAG-371 | TC-GS-TAG-E2E-098-delete-tag-to-be-returned-efek-di-fams-single-dan-bulk | FE+BE |
| TC-GS-TAG-372 | TC-GS-TAG-E2E-009-popup-tag-log-akses-lintas-role-dan-role-fams-tanpa-akses-registri | FE+BE |
| TC-GS-TAG-373 | TC-GS-TAG-E2E-009-popup-tag-log-akses-lintas-role-dan-role-fams-tanpa-akses-registri | FE+BE |
| TC-GS-TAG-374 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-375 | TC-GS-TAG-E2E-014-defense-in-depth-request-langsung-isolasi-tenant-dan-markup | FE+BE |
| TC-GS-TAG-376 | TC-GS-TAG-E2E-060-sinkronisasi-fams-replace-tag-hasil-pemindaian | FE+BE |
| TC-GS-TAG-377 | TC-GS-TAG-E2E-096-tag-log-aturan-qr-last-user-snapshot-konsistensi-dan-hapus-tag | FE+BE |
| TC-GS-TAG-378 | TC-GS-TAG-E2E-002-isi-sel-registri-ikon-tipe-code-badge-dan-popup-combined | FE+BE |
| TC-GS-TAG-379 | TC-GS-TAG-E2E-058-sinkronisasi-fams-disposal-aset-ke-to-be-returned | FE+BE |
