# Coverage E2E — Global Settings > Import

Sumber: `global-settings/import/TestCases/tc-import.md` (964 TC unik, `TC-GS-IMPORT-1`–`971` tanpa 483–485 dan 772–775; 968 baris karena ID 868–871 dipakai dua kali). Suite: `specs/GlobalSettings/Import/`. Prefix: `GS` + `IMPORT` (`TC-GS-IMPORT-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Rencana: `work-items/gs-import/plan-e2e-generate-spec.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: seluruh 968 baris TC masuk spec; 0 TC dikeluarkan sebagai hanya-BE. 216 spec (216 FE+BE, 0 mock). Setiap baris TC terpetakan ke tepat satu spec.

## TC granular → spec e2e

Kolom TC sumber memuat nomor `TC-GS-IMPORT-<n>`. Entri berbentuk `n@Lbaris` adalah ID ganda (lihat bagian ID ganda); angka setelah `@L` adalah nomor baris di `tc-import.md`.

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-IMPORT-E2E-001-screening-halaman-import-dengan-draft-brand-sub-tab-default-skeleton | Screening Halaman Import dengan Draft Brand, Sub-Tab Default, Skeleton Loading, dan Unsaved Banner Dibaca Admin Kedua | FE+BE | 58 | 7, 8, 17, 20 |
| TC-GS-IMPORT-E2E-002-routing-import-route-per-tab-route-tanpa-tab-refresh-riwayat-back | Routing Import: Route per Tab, Route Tanpa Tab, Refresh, Riwayat Back, Breadcrumb Non-Klik, dan Detail Notifikasi | FE+BE | 50 | 9, 10, 11, 12, 13, 14 |
| TC-GS-IMPORT-E2E-003-screening-state-belum-ada-draft-tab-brand-dan-keenam-sub-tab-identik | Screening State Belum Ada Draft: Tab Brand dan Keenam Sub-Tab Identik | FE+BE | 54 | 15, 16 |
| TC-GS-IMPORT-E2E-004-unsaved-banner-pada-client-c-tampil-bersama-draft-division-tanggal | Unsaved Banner pada Client C: Tampil Bersama Draft Division, Tanggal Tetap Setelah Edit dan Append, Tidak Tampil Setelah Confirm Mapping, dan Draft Kurang dari 24 Jam Dibuang Tanpa Discard | FE+BE | 71 | 19, 21, 876, 884 |
| TC-GS-IMPORT-E2E-005-guided-tooltip-otomatis-selesai-sampai-done-keluar-halaman-di-tengah | Guided Tooltip Otomatis: Selesai Sampai Done, Keluar Halaman di Tengah, Replay, dan Keluar Tidak Menandai Ulang | FE+BE | 46 | 24, 590, 593 |
| TC-GS-IMPORT-E2E-006-guided-tooltip-otomatis-ditutup-lewat-skip-klik-overlay-dan-esc-lalu | Guided Tooltip Otomatis Ditutup Lewat Skip, Klik Overlay, dan Esc Lalu Ditandai Sudah Dilihat | FE+BE | 42 | 587, 588, 589 |
| TC-GS-IMPORT-E2E-007-guided-tooltip-replay-lewat-3-langkah-tombol-back-navigasi-keyboard-dan | Guided Tooltip Replay Lewat [?]: 3 Langkah, Tombol Back, Navigasi Keyboard, dan Target Disabled pada Read Only | FE+BE | 55 | 22, 23, 591, 592 |
| TC-GS-IMPORT-E2E-008-role-negatif-client-a-akun-tanpa-capability-tidak-melihat-menu-import | Role Negatif Client A: Akun Tanpa Capability Tidak Melihat Menu Import; Read Only dan Import data (Read Only) Tidak Dapat Memulai Sesi Edit | FE+BE | 33 | 26, 595, 596 |
| TC-GS-IMPORT-E2E-009-role-negatif-client-c-create-missing-divisions-disabled-bagi-import | Role Negatif Client C: Create Missing Divisions Disabled bagi Import data (Read Only) dan Izin Create Dicabut Saat Modal Column Mapping Terbuka | FE+BE | 31 | 44, 597 |
| TC-GS-IMPORT-E2E-010-role-positif-default-user-dan-import-data-create-menjalankan-upload | Role Positif: Default User dan Import data (Create) Menjalankan Upload, Confirm Mapping, Import, Save, Remove, Bulk Delete, AI Accept dan Dismiss, Discard, dan Create Missing Tanpa Penolakan Izin | FE+BE | 85 | 33, 598, 599, 600 |
| TC-GS-IMPORT-E2E-011-upload-csv-valid-lalu-confirm-mapping-membuat-draft-baru-brand | Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Brand, Measurement, dan Position (Plus Verifikasi Changelog) | FE+BE | 100 | 1, 2, 3 |
| TC-GS-IMPORT-E2E-012-upload-csv-valid-lalu-confirm-mapping-membuat-draft-baru-division-user | Upload CSV Valid Lalu Confirm Mapping Membuat Draft Baru: Division, User Login, dan User Non Login (Plus Verifikasi Changelog) | FE+BE | 99 | 4, 5, 6 |
| TC-GS-IMPORT-E2E-013-screening-modal-column-mapping-judul-footer-atribut-target-required | Screening Modal Column Mapping: Judul dan Footer, Atribut Target Required (*) User Login dan Non Login, Auto-Match Case-Insensitive, dan Penanda Required Lintas Client | FE+BE | 70 | 51, 52, 53, 54, 889 |
| TC-GS-IMPORT-E2E-014-dropdown-file-column-header-duplikat-tidak-di-auto-match-kolom-terpakai | Dropdown File Column: Header Duplikat Tidak Di-Auto-Match, Kolom Terpakai Disabled dan Kembali Enabled, Nilai Contoh, Ellipsis, dan Aksesibilitas | FE+BE | 79 | 55, 58, 886, 887, 888 |
| TC-GS-IMPORT-E2E-015-guard-pra-confirm-mapping-required-no-column-diblokir-lalu-optional-no | Guard Pra-Confirm Mapping: Required No Column Diblokir, Lalu Optional No Column Valid dan Kolom Tak Terpetakan Diabaikan | FE+BE | 37 | 56, 57, 59 |
| TC-GS-IMPORT-E2E-016-reupload-file-di-modal-column-mapping-berkas-pengganti-dan-berkas | Reupload File di Modal Column Mapping: Berkas Pengganti dan Berkas Tersaring | FE+BE | 21 | 60, 61 |
| TC-GS-IMPORT-E2E-017-menutup-modal-column-mapping-dialog-unsaved-changes-cancel-leave-esc | Menutup Modal Column Mapping: Dialog Unsaved Changes (Cancel, Leave, Esc) dan Tutup Bersih (Cancel, Icon Close) | FE+BE | 40 | 62, 63, 64, 65, 66, 67 |
| TC-GS-IMPORT-E2E-018-append-ke-draft-yang-sudah-ada-dialog-confirm-append-cancel-leave | Append ke Draft yang Sudah Ada: Dialog Confirm Append (Cancel, Leave, Append Records), Row Lanjut, dan Nama Lebih dari 120 Karakter Menjadi Error dengan Badge AI | FE+BE | 61 | 68, 71, 72, 73, 74 |
| TC-GS-IMPORT-E2E-019-entri-upload-drag-and-drop-tombol-browse-file-dan-dua-berkas-sekaligus | Entri Upload: Drag-and-Drop, Tombol Browse File, dan Dua Berkas Sekaligus | FE+BE | 22 | 69, 70, 563 |
| TC-GS-IMPORT-E2E-020-client-e-upload-setelah-commit-tuntas-membuat-draft-baru-dan-confirm | Client E: Upload Setelah Commit Tuntas Membuat Draft Baru, dan Confirm Mapping User Login dan User Non Login dengan Referensi Valid | FE+BE | 27 | 76, 759, 760 |
| TC-GS-IMPORT-E2E-021-penyaringan-berkas-senyap-xlsx-sheet-kosong-format-selain-csv-xlsx | Penyaringan Berkas Senyap: XLSX Sheet Kosong, Format Selain CSV/XLSX, Hanya Header, Enkoding Rusak, 0 Byte, dan Header Plus Baris Kosong | FE+BE | 43 | 89, 90, 93, 95, 96, 582 |
| TC-GS-IMPORT-E2E-022-berkas-lolos-penyaringan-csv-utf-8-tanpa-dengan-bom-xlsx-sheet-pertama | Berkas Lolos Penyaringan: CSV UTF-8 Tanpa dan Dengan BOM, XLSX Sheet Pertama, Sheet Lain Diabaikan, dan Berkas Tidak Tersimpan di File Manager Permanen | FE+BE | 38 | 85, 86, 87, 88, 97 |
| TC-GS-IMPORT-E2E-023-penyaringan-delimiter-titik-koma-tersaring-atau-lolos-ke-error-banner | Penyaringan Delimiter: Titik Koma Tersaring atau Lolos ke Error Banner Pemetaan (Measurement, Brand, Position, Division, dan Tab User Client G) | FE+BE | 58 | 94, 564, 815, 859, 867 |
| TC-GS-IMPORT-E2E-024-validasi-berkas-ditolak-seluruhnya-nama-unit-simbol-kosong-pada-brand | Validasi Berkas Ditolak Seluruhnya: Nama, Unit, dan Simbol Kosong pada Brand, Measurement, Position, dan Division | FE+BE | 11 | 98, 99, 100, 101, 102, 103 |
| TC-GS-IMPORT-E2E-025-validasi-berkas-ditolak-seluruhnya-first-name-last-name-email-division | Validasi Berkas Ditolak Seluruhnya: First Name, Last Name, Email, Division, dan Access Kosong pada User Login | FE+BE | 11 | 104, 105, 106, 107, 108 |
| TC-GS-IMPORT-E2E-026-validasi-berkas-ditolak-seluruhnya-format-email-access-di-luar-produk | Validasi Berkas Ditolak Seluruhnya: Format Email, Access di Luar Produk, Active Period (Format dan Hari Ini atau Lampau), dan Custom Field Date | FE+BE | 11 | 110, 111, 112, 113, 122 |
| TC-GS-IMPORT-E2E-027-validasi-berkas-ditolak-seluruhnya-custom-field-numeric-bukan-angka-15 | Validasi Berkas Ditolak Seluruhnya: Custom Field Numeric (Bukan Angka, Lebih dari 15 Digit, Desimal) dan Phone (Kode Negara, Non-Numerik, Kurang dari 4 dan Lebih dari 15 Digit) | FE+BE | 11 | 115, 116, 117, 118, 119, 120, 121 |
| TC-GS-IMPORT-E2E-028-validasi-berkas-ditolak-seluruhnya-custom-field-required-kosong-client | Validasi Berkas Ditolak Seluruhnya: Custom Field Required Kosong (Client G) pada User Login, User Non Login, dan Append | FE+BE | 36 | 109, 612, 948 |
| TC-GS-IMPORT-E2E-029-validasi-berkas-ditolak-seluruhnya-pada-user-non-login-represented-by | Validasi Berkas Ditolak Seluruhnya pada User Non Login: Represented By, Email, Active Period, First Name, Last Name, Division Kosong, serta Custom Field Numeric, Phone, dan Date | FE+BE | 11 | 124, 125, 126, 127, 611, 614, 615, 616 |
| TC-GS-IMPORT-E2E-030-format-error-banner-urutan-pesan-per-field-jumlah-baris-unik-potong-20 | Format Error Banner: Urutan Pesan per Field, Jumlah Baris Unik, Potong 20 Nomor (20 vs 21 vs 25 Baris), Nomor Baris dengan Baris Kosong, dan Kombinasi Dropdown Asing | FE+BE | 11 | 129, 132, 583, 621, 623, 624, 892 |
| TC-GS-IMPORT-E2E-031-custom-field-dinonaktifkan-saat-modal-column-mapping-terbuka-pesan | Custom Field Dinonaktifkan Saat Modal Column Mapping Terbuka: Pesan Level-Kolom (User Login dan User Non Login, Termasuk Kombinasi Per-Baris) | FE+BE | 54 | 123, 133, 617, 622 |
| TC-GS-IMPORT-E2E-032-berkas-diterima-dengan-baris-bermasalah-dropdown-di-luar-opsi-user | Berkas Diterima dengan Baris Bermasalah: Dropdown di Luar Opsi (User Login dan User Non Login), Duplikat, dan Panjang atau Karakter Menjadi Error | FE+BE | 53 | 114, 130, 131, 613 |
| TC-GS-IMPORT-E2E-033-berkas-diterima-normalisasi-nilai-sel-dan-nilai-batas-valid-baris | Berkas Diterima: Normalisasi Nilai Sel dan Nilai Batas Valid (Baris Kosong, Numeric, Phone, Date, Dropdown, XLSX Non-Text, Access, dan Kolom Access pada Non Login) | FE+BE | 63 | 128, 565, 618, 619, 620 |
| TC-GS-IMPORT-E2E-034-validasi-sel-brand-120-121-karakter-emoji-karakter-cetak-trim-urutan | Validasi Sel Brand: 120 dan 121 Karakter, Emoji, Karakter Cetak, Trim, dan Urutan Aturan pada Satu Sel | FE+BE | 12 | 134, 135, 136, 137, 138, 171 |
| TC-GS-IMPORT-E2E-035-validasi-sel-measurement-unit-name-dan-symbol-120-121-10-11-emoji | Validasi Sel Measurement: Unit Name dan Symbol (120 dan 121, 10 dan 11, Emoji, Symbol Duplikat Sah, dan Trim) | FE+BE | 13 | 139, 140, 141, 142, 143, 144, 635 |
| TC-GS-IMPORT-E2E-036-validasi-sel-position-name-dan-division-name-120-121-karakter-dan-emoji | Validasi Sel Position Name dan Division Name: 120 dan 121 Karakter dan Emoji | FE+BE | 13 | 145, 146, 147, 148, 636, 637 |
| TC-GS-IMPORT-E2E-037-validasi-code-division-15-16-karakter-karakter-tidak-sah-karakter-sah | Validasi Code Division: 15 dan 16 Karakter, Karakter Tidak Sah, Karakter Sah, Bentrok dengan Sistem, dan Identik Antar-Baris | FE+BE | 13 | 149, 150, 151, 152, 153, 154 |
| TC-GS-IMPORT-E2E-038-code-division-antar-baris-draft-bentrok-append-save-duplicate-pulih | Code Division Antar-Baris dan Draft: Bentrok Append, Save Duplicate, dan Pulih Saat Baris Pembanding Dihapus atau Diubah | FE+BE | 53 | 638, 639, 640, 641 |
| TC-GS-IMPORT-E2E-039-validasi-referensi-division-position-tidak-ditemukan-user-login-dan-non | Validasi Referensi Division dan Position: Tidak Ditemukan (User Login dan Non Login), Kosong Valid, dan Pencocokan Tidak Peka Huruf | FE+BE | 13 | 159, 160, 161, 162, 628 |
| TC-GS-IMPORT-E2E-040-validasi-represented-by-pada-user-non-login-bukan-user-login-aktif-non | Validasi Represented By pada User Non Login: Bukan User Login Aktif (Non-Login, Pending, Inactive, Nama Bukan Email, Draft Belum Commit) dan Cocok Tidak Peka Huruf | FE+BE | 14 | 165, 166, 167, 168, 169, 569, 629, 630 |
| TC-GS-IMPORT-E2E-041-validasi-panjang-dan-trim-pada-user-login-first-name-last-name-email | Validasi Panjang dan Trim pada User Login: First Name, Last Name, Email, dan Employee ID (121 dan 120 Karakter) | FE+BE | 13 | 155, 156, 157, 158, 631, 632 |
| TC-GS-IMPORT-E2E-042-validasi-panjang-user-non-login-dan-custom-field-text-text-area-client | Validasi Panjang User Non Login dan Custom Field Text dan Text Area (Client C; Text Client G) serta Nama Akronim Tax ID | FE+BE | 27 | 163, 164, 625, 626, 627, 633, 634 |
| TC-GS-IMPORT-E2E-043-tampilan-error-dan-penyimpanan-baris-urutan-pesan-callout-penanda-sel | Tampilan Error dan Penyimpanan Baris: Urutan Pesan Callout, Penanda Sel Bukan Warna Semata, Save Edit Baris Dropdown, dan Custom Field Dijadikan Required | FE+BE | 52 | 170, 172, 566, 872 |
| TC-GS-IMPORT-E2E-044-defense-in-depth-permintaan-langsung-ditolak-403-untuk-import-data-read | Defense-in-depth: Permintaan Langsung Ditolak 403 untuk Import data (Read Only), Read Only, dan Tanpa Capability (Confirm Mapping, Save, Remove, Bulk Delete, Discard, Import, Upload, Edit Session, Baca) | FE+BE | 73 | 35, 36, 37, 38, 39, 40, 43, 601, 604, 606 |
| TC-GS-IMPORT-E2E-045-defense-in-depth-ai-accept-delete-all-rows-dan-ai-dismiss-langsung | Defense-in-depth: AI Accept, Delete All Rows, dan AI Dismiss Langsung Ditolak 403 untuk Import data (Read Only) | FE+BE | 23 | 42, 602, 603 |
| TC-GS-IMPORT-E2E-046-defense-in-depth-client-c-create-missing-divisions-positions-ditolak | Defense-in-depth Client C: Create Missing Divisions/Positions Ditolak 403, Confirm Mapping Ulang 409, dan Pemetaan Satu Kolom ke Dua Atribut 422 | FE+BE | 35 | 41, 83, 84, 605 |
| TC-GS-IMPORT-E2E-047-resilience-kegagalan-5xx-timeout-pada-pembacaan-staging-table-upload | Resilience: Kegagalan 5xx dan Timeout pada Pembacaan Staging Table, Upload, dan Confirm Mapping (Toast, Banner Generik, Retry Tanpa Baris Ganda) | FE+BE | 66 | 18, 79, 80, 81, 578, 610 |
| TC-GS-IMPORT-E2E-048-multi-konteks-client-d-dua-admin-upload-bersamaan-dan-halaman-admin | Multi-Konteks Client D: Dua Admin Upload Bersamaan dan Halaman Admin Kedua yang Basi | FE+BE | 38 | 75, 829 |
| TC-GS-IMPORT-E2E-049-multi-konteks-client-c-halaman-basi-setelah-draft-dihapus-dibuat-admin | Multi-Konteks Client C: Halaman Basi Setelah Draft Dihapus atau Dibuat Admin Lain, Confirm Mapping Append ke Draft yang Sudah Hilang | FE+BE | 29 | 868@L738, 873, 874 |
| TC-GS-IMPORT-E2E-050-harness-worker-commit-job-committing-dihentikan-di-akhir-batch-saat | Harness Worker Commit: Job Committing Dihentikan di Akhir Batch saat Entitas Suspended atau Organisasi Turun ke Plan Free | FE+BE | 46 | 49, 50 |
| TC-GS-IMPORT-E2E-051-batas-umur-draft-24-jam-23j59m-tepat-24j-halaman-terbuka-melewati-batas | Batas Umur Draft 24 Jam: 23j59m, Tepat 24j, Halaman Terbuka Melewati Batas, dan Edit atau Append Tidak Mereset Umur | FE+BE | 47 | 877, 878, 879, 880 |
| TC-GS-IMPORT-E2E-052-draft-baru-mulai-dari-umur-0-setelah-draft-berumur-24-jam-dibuang | Draft Baru Mulai dari Umur 0 Setelah Draft Berumur 24 Jam Dibuang (Select All dan Bulk Delete, Discard, Delete All Rows) | FE+BE | 57 | 882, 883, 885 |
| TC-GS-IMPORT-E2E-053-commit-sebagian-tidak-mereset-umur-draft-job-kembali-draft-banner | Commit Sebagian Tidak Mereset Umur Draft (Job Kembali Draft, Banner Tampil 24 Jam sejak Confirm Mapping Pertama) | FE+BE | 14 | 881 |
| TC-GS-IMPORT-E2E-054-ttl-berkas-sementara-60-menit-confirm-mapping-setelah-61-menit-tepat-60 | TTL Berkas Sementara 60 Menit: Confirm Mapping Setelah 61 Menit atau Tepat 60 Menit Memunculkan Banner Kegagalan dan Reupload File Memulihkan | FE+BE | 33 | 82, 823 |
| TC-GS-IMPORT-E2E-055-kunci-sesi-edit-izin-create-dicabut-saat-sesi-edit-aktif-save-ditolak | Kunci Sesi Edit: Izin Create Dicabut saat Sesi Edit Aktif, Save Ditolak 403, Dialog Draft Is Being Edited, Kunci Dilepas lewat TTL 10 Menit | FE+BE | 27 | 607 |
| TC-GS-IMPORT-E2E-056-volume-berkas-mendekati-1-mb-1-048-576-vs-1-048-577-byte-10-000-baris | Volume: Berkas Mendekati 1 MB (1.048.576 vs 1.048.577 Byte) dan 10.000 Baris per Draft (10.001 Ditolak, 9995+6 Ditolak, 9995+5 Diterima, Baris Kosong Tidak Dihitung) | FE+BE | 57 | 77, 78, 91, 92, 584, 812 |
| TC-GS-IMPORT-E2E-057-volume-append-satu-baris-ke-draft-10-000-baris-ditolak-all-or-nothing | Volume: Append Satu Baris ke Draft 10.000 Baris Ditolak All-or-Nothing | FE+BE | 19 | 813 |
| TC-GS-IMPORT-E2E-058-volume-confirm-mapping-berkas-brand-150-baris-di-client-limit | Volume: Confirm Mapping Berkas Brand 150 Baris di Client Limit Menghasilkan 120 Pending dan 30 Error | FE+BE | 11 | 758 |
| TC-GS-IMPORT-E2E-059-plan-gating-import-free-disabled-total-dengan-chip-upgrade-growth | Plan Gating Import: Free Disabled Total dengan Chip Upgrade; Growth, Professional, dan Enterprise Aktif Penuh | FE+BE | 14 | 45, 46, 608, 609 |
| TC-GS-IMPORT-E2E-060-client-suspended-aksi-tulis-ditolak-403-dengan-toast-khusus-ui-aksi | Client Suspended: Aksi Tulis Ditolak 403 dengan Toast Khusus (UI), Aksi Baca Tetap Jalan; Permintaan Langsung dan Create Missing Options Ditolak 403 | FE+BE | 48 | 47, 816, 932 |
| TC-GS-IMPORT-E2E-061-client-expired-discard-draft-ditolak-403-dengan-toast-khusus-confirm | Client Expired: Discard Draft Ditolak 403 dengan Toast Khusus; Permintaan Langsung dan Create Missing Options Ditolak 403 | FE+BE | 43 | 48, 817 |
| TC-GS-IMPORT-E2E-062-android-guided-tooltip-melewati-step-1-download-template-masuk-bottom | Android: Guided Tooltip Melewati Step 1 (Download Template Masuk Bottom Sheet) | FE+BE | 6 | 25 |
| TC-GS-IMPORT-E2E-063-role-matrix-visibilitas-dan-state-elemen-halaman-import-untuk-total | Role Matrix: Visibilitas dan State Elemen Halaman Import untuk Total Control, Default User, dan Import data (Create) | FE+BE | 29 | 27, 28, 31 |
| TC-GS-IMPORT-E2E-064-role-matrix-elemen-disabled-hidden-untuk-read-only-dan-import-data-read | Role Matrix: Elemen Disabled dan Hidden untuk Read Only dan Import data (Read Only) pada Halaman Import | FE+BE | 34 | 29, 30 |
| TC-GS-IMPORT-E2E-065-role-matrix-state-belum-ada-draft-untuk-read-only-dan-import-data-read | Role Matrix: State Belum Ada Draft untuk Read Only dan Import data (Read Only) (Import (0), Upload, Dropzone Disabled, Berkas yang Diseret Tidak Diproses) | FE+BE | 18 | 32, 34, 594 |
| TC-GS-IMPORT-E2E-066-defense-in-depth-staging-permintaan-save-diulang-langsung-ditolak-409 | Defense-in-depth Staging: Permintaan Save Diulang Langsung Ditolak 409 dan Nilai Melebihi Batas yang Disuntikkan Melewati Validasi FE Tidak Tersimpan | FE+BE | 21 | 667, 677 |
| TC-GS-IMPORT-E2E-067-resilience-staging-save-remove-bulk-delete-delete-all-rows-dan-discard | Resilience Staging: Save, Remove, Bulk Delete, Delete All Rows, dan Discard Draft Gagal 5xx atau Tanpa Respons (Timeout atau Jaringan Putus) | FE+BE | 136 | 218, 219, 234, 261, 273, 283, 579, 681, 682, 683, 684, 685 |
| TC-GS-IMPORT-E2E-068-konflik-kunci-sesi-edit-pintu-masuk-admin-kedua-ditolak-409-dialog | Konflik Kunci Sesi Edit: Pintu Masuk Admin Kedua Ditolak 409 dengan Dialog Draft Is Being Edited, Baca Tetap Diizinkan, dan UI Tidak Menerima Status Kunci | FE+BE | 53 | 237, 248, 249, 679, 680 |
| TC-GS-IMPORT-E2E-069-aksi-admin-kedua-ditolak-409-saat-kunci-dipegang-append-confirm-mapping | Aksi Admin Kedua Ditolak 409 saat Kunci Dipegang: Append, Confirm Mapping, Remove, Bulk Delete, Discard Draft, dan Import Commit | FE+BE | 80 | 238, 239, 240, 241, 245, 246 |
| TC-GS-IMPORT-E2E-070-aksi-admin-kedua-pada-draft-ber-error-ditolak-409-delete-all-rows-ai | Aksi Admin Kedua pada Draft Ber-error Ditolak 409: Delete All Rows, AI Accept, dan AI Dismiss | FE+BE | 35 | 242, 243, 244 |
| TC-GS-IMPORT-E2E-071-create-missing-divisions-oleh-admin-kedua-ditolak-409-saat-kunci | Create Missing Divisions oleh Admin Kedua Ditolak 409 saat Kunci Dipegang (Client C) | FE+BE | 14 | 247 |
| TC-GS-IMPORT-E2E-072-kunci-dilepas-setelah-save-cancel-plus-discard-sesi-berakhir-tanpa-save | Kunci Dilepas: Setelah Save, Cancel plus Discard, Sesi Berakhir Tanpa Save, Navigasi Sidebar, Klik Sel Tanpa Mengambil Kunci, dan Tab Ditutup | FE+BE | 75 | 191, 255, 256, 661, 678, 871@L1080 |
| TC-GS-IMPORT-E2E-073-take-over-session-kunci-berpindah-save-pemegang-lama-ditolak-edit | Take Over Session: Kunci Berpindah, Save Pemegang Lama Ditolak (Edit Session Taken Over), dan Cancel pada Dialog Tidak Mengubah Kunci | FE+BE | 34 | 868@L1077, 870@L1079 |
| TC-GS-IMPORT-E2E-074-ttl-kunci-sesi-edit-10-menit-kedaluwarsa-tepat-10-menit-masih-berlaku | TTL Kunci Sesi Edit 10 Menit: Kedaluwarsa Tepat 10 Menit, Masih Berlaku pada Menit ke-9, dan Hitungan Diatur Ulang oleh Mutasi Terakhir | FE+BE | 52 | 250, 251, 252, 821 |
| TC-GS-IMPORT-E2E-075-kunci-kedaluwarsa-save-pemegang-lama-diproses-normal-bila-belum-diambil | Kunci Kedaluwarsa: Save Pemegang Lama Diproses Normal bila Belum Diambil, Ditolak 409 bila Sudah Diambil, dan Draft Tidak Ditemukan Setelah Discard Draft | FE+BE | 38 | 253, 254, 257 |
| TC-GS-IMPORT-E2E-076-pelepasan-kunci-saat-tab-ditutup-gagal-sehingga-ttl-berlaku-dan-save | Pelepasan Kunci saat Tab Ditutup Gagal sehingga TTL Berlaku, dan Save Ditolak setelah Capability Dicabut lalu Kunci Lepas setelah TTL | FE+BE | 34 | 207, 668 |
| TC-GS-IMPORT-E2E-077-kontrol-worker-commit-tooltip-permission-mengalahkan-committing-select | Kontrol Worker Commit: Tooltip Permission Mengalahkan Committing, Select All Mengecualikan Baris Batch Aktif, dan Import In Progress Ditolak Tanpa Take Over | FE+BE | 37 | 208, 692, 869@L1078 |
| TC-GS-IMPORT-E2E-078-selection-limit-100-pada-client-limit-edit-this-page-100-baris-select | Selection Limit 100 pada Client Limit: Edit this page 100 Baris, Select All Di-cap, Checkbox Tambahan Disabled, dan Bulk Delete Hanya 100 Baris | FE+BE | 35 | 194, 270, 271, 272 |
| TC-GS-IMPORT-E2E-079-batas-10000-baris-per-draft-duplicate-yang-melebihi-10000-ditolak-tepat | Batas 10000 Baris per Draft: Duplicate yang Melebihi 10000 Ditolak, Tepat 10000 Diterima | FE+BE | 30 | 233, 670 |
| TC-GS-IMPORT-E2E-080-aksi-staging-table-tidak-dicatat-di-changelog-import-system-log-dan | Aksi Staging Table Sebelum Commit Tidak Dicatat di Changelog Import, System Log, dan Activity Log | FE+BE | 17 | 669 |
| TC-GS-IMPORT-E2E-081-visibilitas-saran-represented-by-tidak-dibatasi-hak-lihat-aktor-import | Visibilitas Saran Represented By Tidak Dibatasi Hak Lihat Aktor (Import data Create dan Total Control) | FE+BE | 12 | 969 |
| TC-GS-IMPORT-E2E-082-duplicate-terhadap-data-sistem-brand-measurement-position-division | Duplicate terhadap data sistem: Brand, Measurement, Position, Division (tooltip, status, kartu Duplicates) dan nama sistem yang muncul dua kali | FE+BE | 26 | 173, 174, 175, 176, 177, 178, 828 |
| TC-GS-IMPORT-E2E-083-duplicate-email-terhadap-user-login-non-login-client-lain-dan-email | Duplicate Email terhadap User Login, Non-Login, client lain dan email pending (Tab User Login dan User Non Login) | FE+BE | 54 | 179, 180, 181, 185, 649, 819, 820, 869@L937 |
| TC-GS-IMPORT-E2E-084-duplicate-employee-id-case-sensitive-soft-deleted-pool-gabungan-client | Duplicate Employee ID: case-sensitive, soft-deleted, pool gabungan, client lain, dan urutan field tooltip | FE+BE | 29 | 182, 183, 184, 648, 650, 651, 856 |
| TC-GS-IMPORT-E2E-085-duplicate-antar-baris-dalam-satu-berkas-baris-terbawah-pending-tidak | Duplicate antar-baris dalam satu berkas: baris terbawah pending, tidak peka huruf besar-kecil, Email, Employee ID, Division Name+Code | FE+BE | 40 | 186, 642, 643, 644, 645, 646, 838 |
| TC-GS-IMPORT-E2E-086-presedensi-status-error-kolom-identitas-didahulukan-dari-duplicate-dan | Presedensi status: error kolom identitas didahulukan dari duplicate, dan duplicate didahulukan dari error non-identitas | FE+BE | 96 | 189, 837, 839, 848, 849, 850, 857, 871@L938 |
| TC-GS-IMPORT-E2E-087-re-evaluasi-status-duplicate-baris-pembanding-dihapus-atau-diubah | Re-evaluasi status duplicate: baris pembanding dihapus atau diubah, rekaman sistem dihapus atau dibuat setelah staging, Save tanpa perubahan pada baris duplicate | FE+BE | 44 | 188, 567, 568, 647, 870@L1020 |
| TC-GS-IMPORT-E2E-088-duplicate-antara-draft-lama-dan-berkas-append-client-a-d-01 | Duplicate antara draft lama dan berkas Append (Client A, D-01) | FE+BE | 10 | 187 |
| TC-GS-IMPORT-E2E-089-karakter-emoji-pada-employee-id-first-name-dan-last-name-user-login-dan | Karakter emoji pada Employee ID, First Name dan Last Name (User Login dan User Non Login) | FE+BE | 24 | 861, 862, 863, 864 |
| TC-GS-IMPORT-E2E-090-edit-mode-pintu-masuk-edit-baris-duplicate-edit-this-page-dan-kontrol | Edit Mode: pintu masuk (Edit baris, Duplicate, Edit this page) dan kontrol yang Disabled atau Hidden selama sesi edit | FE+BE | 90 | 190, 192, 193, 196, 197, 198, 199, 200, 203, 664 |
| TC-GS-IMPORT-E2E-091-edit-mode-error-callout-dan-chip-disabled-upload-file-dan-discard | Edit Mode: Error Callout dan chip Disabled, Upload File dan Discard Disabled dengan Download Template dan Changelog aktif, navigasi keyboard grid | FE+BE | 42 | 201, 202, 235 |
| TC-GS-IMPORT-E2E-092-save-sesi-edit-berhasil-edit-baris-duplicate-edit-this-page-hasil | Save sesi edit berhasil: Edit Baris, Duplicate, Edit this page, hasil duplicate setelah Save, dan Code Division jadi error | FE+BE | 57 | 209, 210, 211, 215, 216, 217, 652 |
| TC-GS-IMPORT-E2E-093-save-tanpa-perubahan-zero-delta-no-op-pengecualian-baris-error-sesi | Save tanpa perubahan (Zero-Delta): no-op, pengecualian baris error, sesi Duplicate, kapitalisasi Employee ID | FE+BE | 46 | 220, 221, 222, 223, 653, 654, 655 |
| TC-GS-IMPORT-E2E-094-save-diblokir-all-or-nothing-wajib-panjang-live-karakter-ke-121-urutan | Save diblokir all-or-nothing: wajib, panjang live (karakter ke-121), urutan pesan, tiap Import Type, dan Save ditolak karena baris dihapus admin lain | FE+BE | 79 | 212, 213, 214, 671, 673, 674, 842 |
| TC-GS-IMPORT-E2E-095-save-diblokir-karakter-terlarang-yang-lolos-filter-input-dan-format | Save diblokir: karakter terlarang yang lolos filter input dan format Email, Overtime Hours, Emergency Phone | FE+BE | 31 | 672, 675 |
| TC-GS-IMPORT-E2E-096-cancel-sesi-edit-tanpa-perubahan-tanpa-dialog-dengan-perubahan | Cancel sesi edit: tanpa perubahan tanpa dialog, dengan perubahan memunculkan dialog Discard Changes, Keep Editing mempertahankan sesi | FE+BE | 35 | 224, 225, 226, 227, 232, 656, 657, 658 |
| TC-GS-IMPORT-E2E-097-discard-changes-membuang-perubahan-sesi-duplicate-toggle-edit-this-page | Discard Changes: membuang perubahan, sesi Duplicate, toggle Edit this page OFF dan ON dengan perubahan, klik sel baris lain | FE+BE | 42 | 204, 228, 229, 230, 231 |
| TC-GS-IMPORT-E2E-098-navigasi-keluar-saat-sesi-edit-sidebar-back-forward-dengan-dan-tanpa | Navigasi keluar saat sesi edit: sidebar, Back, Forward dengan dan tanpa perubahan (dialog Unsaved Changes global, Leave, Cancel) | FE+BE | 51 | 206, 570, 660, 662, 663 |
| TC-GS-IMPORT-E2E-099-edit-mode-tab-user-jenis-kontrol-tiap-kolom-input-teks-select | Edit Mode Tab User: jenis kontrol tiap kolom (input teks, Select, MultiSelect Access, DatePicker Active Period dan Join Date) dan Tab Brand, Measurement, Position, Division hanya input teks | FE+BE | 74 | 891, 893, 895, 897, 908 |
| TC-GS-IMPORT-E2E-100-edit-mode-tab-user-pilihan-use-untuk-nilai-baru-nilai-tersimpan-invalid | Edit Mode Tab User: pilihan Use untuk nilai baru, nilai tersimpan Invalid, all-or-nothing Edit this page, opsi Dropdown dihapus admin lain | FE+BE | 72 | 900, 901, 902, 903, 970 |
| TC-GS-IMPORT-E2E-101-combobox-represented-by-client-a-minimal-2-karakter-pencocokan-email | Combobox Represented By (Client A): minimal 2 karakter, pencocokan email atau nama, maksimum 10 saran berurut, eligibility | FE+BE | 36 | 898, 964, 965, 966 |
| TC-GS-IMPORT-E2E-102-combobox-represented-by-client-c-hanya-user-login-eligible-teks-bebas | Combobox Represented By (Client C): hanya User Login eligible, teks bebas tidak menjadi nilai, nilai tersimpan tidak ditemukan memblokir Save | FE+BE | 29 | 676, 967, 968 |
| TC-GS-IMPORT-E2E-103-edit-mode-client-c-fk-division-dan-position-pada-draft-user-ai-accept | Edit Mode Client C: FK Division dan Position pada draft User, AI Accept dan Dismiss pada sel, tombol Create Missing Disabled, Division Use duplicate | FE+BE | 68 | 205, 659, 665, 835, 899, 907 |
| TC-GS-IMPORT-E2E-104-edit-mode-client-c-nilai-tersimpan-invalid-access-produk-dicabut-active | Edit Mode Client C: nilai tersimpan Invalid (Access produk dicabut, Active Period lampau, opsi Shift), keyboard Select, tombol Create Missing Options Disabled | FE+BE | 83 | 894, 896, 904, 905, 906 |
| TC-GS-IMPORT-E2E-105-custom-field-dinonaktifkan-lalu-diaktifkan-sebelum-import-banner-dan | Custom Field dinonaktifkan lalu diaktifkan sebelum Import: banner dan nilai ikut ditulis ke User | FE+BE | 16 | 971 |
| TC-GS-IMPORT-E2E-106-sel-custom-field-phone-error-tanpa-kode-negara-country-code-default | Sel Custom Field Phone error tanpa kode negara: Country Code default Indonesia lalu valid setelah Save | FE+BE | 11 | 236 |
| TC-GS-IMPORT-E2E-107-client-b-switch-edit-this-page-tanpa-baris-hapus-baris-terakhir | Client B: Switch Edit this page tanpa baris, hapus baris terakhir menghapus draft, Remove dari halaman basi setelah draft terhapus | FE+BE | 18 | 195, 276, 277 |
| TC-GS-IMPORT-E2E-108-remove-satu-baris-dialog-delete-row-cancel-hapus-dengan-penomoran-ulang | Remove satu baris: dialog Delete Row, Cancel, hapus dengan penomoran ulang, dan Remove dari halaman basi memakai identitas baris | FE+BE | 26 | 258, 259, 260, 686 |
| TC-GS-IMPORT-E2E-109-seleksi-baris-dan-bulk-action-bar-checkbox-header-select-all-unselect | Seleksi baris dan Bulk Action Bar: checkbox header, Select All, Unselect All, N-1, seleksi bertahan lintas halaman, Cancel dialog Bulk Delete | FE+BE | 57 | 262, 263, 266, 268, 269, 688, 689, 690 |
| TC-GS-IMPORT-E2E-110-bulk-delete-dialog-delete-rows-vs-delete-row-hapus-dua-baris-bulk | Bulk Delete: dialog Delete Rows vs Delete Row, hapus dua baris, Bulk Delete dari halaman basi, Select All lalu Bulk Delete menghapus draft | FE+BE | 41 | 264, 265, 267, 687 |
| TC-GS-IMPORT-E2E-111-client-f-jumlah-select-all-mengikuti-filter-kartu-dan-delete-all-rows | Client F: jumlah Select All mengikuti filter kartu dan Delete All Rows menomori ulang Row # tanpa celah | FE+BE | 19 | 691, 696 |
| TC-GS-IMPORT-E2E-112-delete-all-rows-dari-error-summary-callout-dan-penekanan-saran-ai | Delete All Rows dari Error Summary Callout dan penekanan saran AI dihapus oleh Remove dan Discard Draft | FE+BE | 37 | 274, 275, 279, 285 |
| TC-GS-IMPORT-E2E-113-menu-row-action-baris-error-fk-division-position-ganda-dan-tab-user-non | Menu row action baris error FK Division, Position, ganda, dan Tab User Non Login memuat Create Missing yang sesuai | FE+BE | 27 | 278, 693, 694 |
| TC-GS-IMPORT-E2E-114-dialog-konfirmasi-backdrop-esc-dan-discard-draft-screening-cancel | Dialog konfirmasi (backdrop, Esc) dan Discard Draft: screening, Cancel, double-submit tombol konfirmasi, halaman basi, hapus draft | FE+BE | 57 | 280, 281, 282, 284, 666, 695 |
| TC-GS-IMPORT-E2E-115-ai-field-shortening-badge-saran-tampil-pada-sel-yang-melanggar-batas | AI Field Shortening: badge saran tampil pada sel yang melanggar batas panjang di semua Tab | FE+BE | 13 | 286, 287, 288, 289, 290, 291, 292, 697 |
| TC-GS-IMPORT-E2E-116-ai-field-shortening-tanpa-badge-untuk-field-di-luar-daftar-dan-tanpa | AI Field Shortening: tanpa badge untuk field di luar daftar dan tanpa saran memadai; respons dalam batas waktu tetap bersaran | FE+BE | 43 | 299, 300, 698, 699, 703, 866 |
| TC-GS-IMPORT-E2E-117-ai-field-shortening-accept-dismiss-validasi-ulang-baris-dan-aksi-dari | AI Field Shortening: Accept, Dismiss, validasi ulang baris, dan aksi dari halaman basi setelah nilai sel diubah admin lain | FE+BE | 103 | 293, 294, 295, 296, 302, 700, 851, 852 |
| TC-GS-IMPORT-E2E-118-ai-reference-suggestion-badge-did-you-mean-per-tab-dan-field-kandidat | AI Reference Suggestion: badge Did you mean per Tab dan field, kandidat peringkat 1, ambang skor, dan kondisi tanpa saran | FE+BE | 93 | 307, 308, 309, 310, 313, 314, 315, 317, 710, 711, 825 |
| TC-GS-IMPORT-E2E-119-ai-reference-suggestion-accept-dan-dismiss-memulihkan-baris-ke-pending | AI Reference Suggestion: Accept dan Dismiss memulihkan baris ke pending, Dismiss lalu sunting, dan Save | FE+BE | 81 | 311, 312, 706, 707, 708, 709 |
| TC-GS-IMPORT-E2E-120-ai-reference-suggestion-kandidat-berskor-tertinggi-represented-by | AI Reference Suggestion: kandidat berskor tertinggi, Represented By, Accept tidak membuat record, rename Position setelah staging | FE+BE | 61 | 318, 320, 716, 826, 827 |
| TC-GS-IMPORT-E2E-121-ai-reference-suggestion-tidak-berlaku-pada-tab-brand-measurement | AI Reference Suggestion: tidak berlaku pada Tab Brand, Measurement, Position, Division, field Dropdown, dan pembaca Read Only | FE+BE | 42 | 319, 713, 714, 715, 853, 933 |
| TC-GS-IMPORT-E2E-122-create-missing-visibilitas-tombol-pada-error-summary-callout-menu-row | Create Missing: visibilitas tombol pada Error Summary Callout, menu row action, dan Bulk Action Bar (Divisions, Positions, Options) | FE+BE | 72 | 344, 349, 733, 734, 924, 925 |
| TC-GS-IMPORT-E2E-123-create-missing-divisions-dan-positions-per-baris-record-dibuat-baris | Create Missing Divisions dan Positions per-baris: record dibuat, baris pulih ke pending, Metric Cards, Code otomatis, tanpa staging | FE+BE | 98 | 323, 324, 325, 326, 336, 346, 350, 351 |
| TC-GS-IMPORT-E2E-124-create-missing-divisions-dan-positions-bulk-dari-callout-dedup-nama | Create Missing Divisions dan Positions bulk dari Callout: dedup nama tidak peka huruf besar-kecil; record tetap ada setelah Discard Draft | FE+BE | 78 | 327, 328, 329, 345, 717, 718 |
| TC-GS-IMPORT-E2E-125-create-missing-divisions-dan-positions-sebagian-atau-seluruh-record | Create Missing Divisions dan Positions: sebagian atau seluruh record gagal, kategori Callout baru, dan urutan pesan Callout | FE+BE | 69 | 330, 331, 333, 334, 854, 865 |
| TC-GS-IMPORT-E2E-126-create-missing-ditolak-dengan-dialog-draft-is-being-edited-konflik | Create Missing ditolak dengan dialog Draft Is Being Edited (konflik kunci sesi) saat admin lain memegang kunci edit | FE+BE | 74 | 338, 725, 726, 727, 919 |
| TC-GS-IMPORT-E2E-127-create-missing-divisions-dan-positions-saat-admin-lain-mengubah-data | Create Missing Divisions dan Positions saat admin lain mengubah data lebih dulu: duplicate ditolak, baris pulih, no-op dari halaman basi | FE+BE | 87 | 335, 337, 735, 855, 858, 875 |
| TC-GS-IMPORT-E2E-128-create-missing-satu-entri-create-per-record-di-changelog-modul-system | Create Missing: satu entri Create per record di Changelog modul, System Log, dan Activity Log (Division, Position, Custom Field Option) | FE+BE | 109 | 340, 341, 342, 922 |
| TC-GS-IMPORT-E2E-129-create-missing-options-per-baris-dan-bulk-dedup-ejaan-pertama-sebagian | Create Missing Options: per-baris dan bulk (dedup, ejaan pertama), sebagian atau seluruh gagal, dan tombol Disabled dengan spinner | FE+BE | 83 | 909, 910, 911, 912, 913, 926 |
| TC-GS-IMPORT-E2E-130-create-missing-options-saat-admin-lain-mengubah-data-nama-sudah-ada | Create Missing Options saat admin lain mengubah data: nama sudah ada, Custom Field dinonaktifkan atau dihapus, baris dihapus, dan Discard | FE+BE | 77 | 914, 915, 916, 917, 929 |
| TC-GS-IMPORT-E2E-131-role-negatif-import-data-read-only-accept-dismiss-ai-dan-create-missing | Role negatif Import data (Read Only): Accept, Dismiss AI, dan Create Missing (Divisions, Positions, Options) Disabled dengan tooltip izin | FE+BE | 25 | 305, 347, 921 |
| TC-GS-IMPORT-E2E-132-role-positif-import-data-create-menjalankan-create-missing-divisions | Role positif Import data (Create): menjalankan Create Missing Divisions dan Options tanpa capability Division atau Custom Field | FE+BE | 25 | 348, 920 |
| TC-GS-IMPORT-E2E-133-execute-import-sukses-brand-measurement-position-division-dan-bentuk | Execute Import sukses: Brand, Measurement, Position, Division, dan bentuk tunggal satu baris pada log, notifikasi, dan banner | FE+BE | 76 | 352, 353, 354, 355, 572 |
| TC-GS-IMPORT-E2E-134-execute-import-sukses-user-login-dan-user-non-login-pending-activation | Execute Import sukses: User Login dan User Non Login (Pending Activation, Temporary User, detail user, entri Changelog Import) | FE+BE | 56 | 356, 357 |
| TC-GS-IMPORT-E2E-135-partial-commit-baris-error-tetap-duplicate-dihapus-error-diperbaiki | Partial Commit: baris error tetap, duplicate dihapus, error diperbaiki lalu commit ulang, dan penomoran ulang padat Row # | FE+BE | 81 | 358, 359, 833, 834 |
| TC-GS-IMPORT-E2E-136-banner-hasil-commit-dapat-ditutup-tampil-tanpa-unsaved-banner-dan-batas | Banner Hasil Commit: dapat ditutup, tampil tanpa Unsaved Banner, dan batas usia 23 jam 59 menit dan tepat 24 jam | FE+BE | 43 | 360, 573, 824 |
| TC-GS-IMPORT-E2E-137-commit-hanya-menambah-record-tanpa-timpa-existing-tanpa-komit-error | Commit hanya menambah record: tanpa timpa existing, tanpa komit error/duplicate, tanpa saran AI atau master data otomatis | FE+BE | 99 | 301, 343, 369, 370, 371, 930 |
| TC-GS-IMPORT-E2E-138-guard-tombol-import-import-0-disabled-draft-sudah-dihapus-lain-dan | Guard tombol Import: Import (0) Disabled, draft sudah dihapus admin lain, dan tidak ada baris pending dari halaman basi | FE+BE | 38 | 362, 363, 738 |
| TC-GS-IMPORT-E2E-139-footer-import-n-digantikan-cancel-dan-save-selama-sesi-edit-client-a | Footer Import (N) digantikan Cancel dan Save selama sesi edit (Client A) | FE+BE | 8 | 367 |
| TC-GS-IMPORT-E2E-140-late-binding-referensi-saat-commit-division-dihapus-position-di-rename | Late-binding referensi saat commit: Division dihapus, Position di-rename, Represented By berubah, referensi hanya di draft tidak sah | FE+BE | 108 | 322, 388, 389, 390, 391, 751, 752 |
| TC-GS-IMPORT-E2E-141-late-binding-duplikat-nama-saat-commit-brand-unit-position-division | Late-binding duplikat nama saat commit (Brand, Unit, Position, Division): error retry-able lalu diperbaiki | FE+BE | 83 | 392, 393, 394, 395 |
| TC-GS-IMPORT-E2E-142-late-binding-field-user-saat-commit-email-employee-id-access-dan-active | Late-binding field User saat commit: Email, Employee ID, Access, dan Active Period menjadi tidak valid | FE+BE | 69 | 396, 397, 398, 399, 400 |
| TC-GS-IMPORT-E2E-143-late-binding-custom-field-user-saat-commit-opsi-dropdown-dihapus-custom | Late-binding Custom Field User saat commit: opsi Dropdown dihapus, Custom Field nonaktif, dan Decimal Places diganti | FE+BE | 47 | 401, 402, 403 |
| TC-GS-IMPORT-E2E-144-download-template-dan-unggah-kembali-auto-match-kolom-sheet-2-diabaikan | Download Template dan unggah kembali: auto-match kolom, Sheet 2 diabaikan, dan tidak membuat draft (Client B) | FE+BE | 34 | 455, 456, 457 |
| TC-GS-IMPORT-E2E-145-defense-in-depth-request-langsung-ke-server-saat-committing-atau-tanpa | Defense-in-depth: request langsung ke server saat committing atau tanpa draft ditolak (conflict atau not found), data tidak berubah | FE+BE | 113 | 381, 383, 384, 704, 729, 730, 739, 746, 918 |
| TC-GS-IMPORT-E2E-146-fault-injection-layanan-ai-timeout-melebihi-batas-diperlakukan-tanpa | Fault injection layanan AI: timeout melebihi batas diperlakukan tanpa saran dan hasil disimpan saat Confirm Mapping | FE+BE | 50 | 298, 316, 843, 844 |
| TC-GS-IMPORT-E2E-147-fault-injection-accept-dismiss-saran-gagal-atau-tanpa-respons-gagal | Fault injection: Accept/Dismiss saran gagal atau tanpa respons, gagal memulai commit, timeout Import, koneksi putus, gagal unduh template | FE+BE | 97 | 303, 304, 321, 366, 372, 453, 701, 702, 712, 740 |
| TC-GS-IMPORT-E2E-148-fault-injection-create-missing-divisions-positions-dan-options-tanpa | Fault injection Create Missing Divisions, Positions, dan Options: tanpa respons dan gagal 500, toast sesuai dan baris tetap error | FE+BE | 81 | 721, 722, 723, 724, 927, 928 |
| TC-GS-IMPORT-E2E-149-multi-konteks-penekanan-saran-ai-dismiss-dibagikan-ke-seluruh-admin | Multi-konteks: penekanan saran AI (Dismiss) dibagikan ke seluruh admin pada draft yang sama (Client C) | FE+BE | 13 | 297 |
| TC-GS-IMPORT-E2E-150-multi-konteks-client-e-commit-bersamaan-dua-sesi-banner-hasil-commit | Multi-konteks Client E: commit bersamaan dua sesi, Banner Hasil Commit sekali per administrator, halaman terbuka basi, commit berhenti | FE+BE | 110 | 571, 580, 585, 741, 845, 846 |
| TC-GS-IMPORT-E2E-151-multi-konteks-client-limit-balapan-dua-sesi-memperebutkan-slot-terakhir | Multi-konteks Client Limit: balapan dua sesi memperebutkan slot terakhir Master Data Count Limit (Division) | FE+BE | 36 | 410, 720 |
| TC-GS-IMPORT-E2E-152-kontrol-worker-commit-tombol-global-disabled-dengan-tooltip-selama | Kontrol worker commit: tombol global Disabled dengan tooltip selama committing, fitur baca tetap berfungsi, tanpa toast Preparing | FE+BE | 71 | 373, 374, 375, 387, 581, 736 |
| TC-GS-IMPORT-E2E-153-kontrol-worker-commit-accept-ai-dan-create-missing-divisions-positions | Kontrol worker commit: Accept AI dan Create Missing (Divisions, Positions) Disabled dengan tooltip selama committing | FE+BE | 59 | 306, 339, 728, 745 |
| TC-GS-IMPORT-E2E-154-kontrol-worker-commit-keanggotaan-batch-aktif-menentukan-remove-dan | Kontrol worker commit: keanggotaan batch aktif menentukan Remove dan checkbox Disabled atau Enabled | FE+BE | 87 | 377, 742, 743, 744 |
| TC-GS-IMPORT-E2E-155-kontrol-worker-commit-remove-bulk-delete-dan-delete-all-rows-dari | Kontrol worker commit: Remove, Bulk Delete, dan Delete All Rows dari halaman basi (partial di luar batch, ditolak di dalam batch) | FE+BE | 87 | 376, 378, 379, 380, 748 |
| TC-GS-IMPORT-E2E-156-kontrol-worker-commit-import-discard-upload-save-kunci-kedaluwarsa | Kontrol worker commit: Import, Discard, Upload, Save kunci kedaluwarsa, Confirm Mapping dari halaman basi memunculkan dialog Import In Progress | FE+BE | 86 | 365, 382, 830, 831, 832 |
| TC-GS-IMPORT-E2E-157-kontrol-worker-commit-accept-ai-dan-create-missing-dari-halaman-basi | Kontrol worker commit: Accept AI dan Create Missing dari halaman basi saat committing memunculkan dialog Import In Progress | FE+BE | 75 | 705, 731, 732, 747, 860 |
| TC-GS-IMPORT-E2E-158-kontrol-worker-commit-pelanjutan-otomatis-setelah-batas-tanpa-kemajuan | Kontrol worker commit: pelanjutan otomatis setelah batas tanpa kemajuan tanpa memproses ulang baris terkomit; di bawah batas tidak | FE+BE | 69 | 385, 386, 749, 822 |
| TC-GS-IMPORT-E2E-159-kontrol-worker-commit-commit-berhenti-tanpa-banner-hasil-commit | Kontrol worker commit: commit berhenti tanpa Banner Hasil Commit, notifikasi stopped, duplicate tetap tampil, rows remaining, Changelog | FE+BE | 49 | 361, 840 |
| TC-GS-IMPORT-E2E-160-notifikasi-progres-commit-awal-pembaruan-in-place-per-batch-selesai | Notifikasi progres commit: awal, pembaruan in-place per batch, selesai dengan Detail, selesai dengan error, dan stopped | FE+BE | 79 | 411, 412, 413, 414, 415 |
| TC-GS-IMPORT-E2E-161-notifikasi-progres-commit-penerima-read-only-tidak-total-ulang-per | Notifikasi progres commit: penerima (Read Only tidak), total ulang per batch, enam Import Type, Processed termasuk baris gagal | FE+BE | 79 | 416, 417, 418, 847 |
| TC-GS-IMPORT-E2E-162-email-aktivasi-akun-per-baris-terkirim-saat-commit-tab-user-login-mail | Email aktivasi akun per baris terkirim saat commit Tab User Login (mail-catcher) | FE+BE | 12 | 737 |
| TC-GS-IMPORT-E2E-163-volume-commit-klik-import-ganda-pada-draft-besar-mengirim-satu | Volume commit: klik Import ganda pada draft besar mengirim satu permintaan, dan baris diproses berurutan Row # lintas batch | FE+BE | 25 | 364, 368 |
| TC-GS-IMPORT-E2E-164-master-data-count-limit-saat-commit-brand-measurement-position-division | Master Data Count Limit saat commit (Brand, Measurement, Position, Division): baris melampaui kuota jadi error; limit diubah lalu commit | FE+BE | 29 | 404, 405, 406, 407, 750 |
| TC-GS-IMPORT-E2E-165-master-data-count-limit-user-login-dan-non-login-satu-pool-serta-create | Master Data Count Limit: User Login dan Non Login satu pool, serta Create Missing Divisions dan Positions di slot terakhir | FE+BE | 65 | 332, 408, 409, 719 |
| TC-GS-IMPORT-E2E-166-isi-berkas-download-template-tab-brand-measurement-position-division | Isi berkas Download Template Tab Brand, Measurement, Position, Division: Sheet 1 header dan baris contoh, Sheet Field Limit | FE+BE | 58 | 435, 436, 437, 438, 439, 440, 441, 442 |
| TC-GS-IMPORT-E2E-167-isi-berkas-download-template-tab-user-login-dan-user-non-login-sheet-1 | Isi berkas Download Template Tab User Login dan User Non Login: Sheet 1 dan Sheet Field Limit termasuk Custom Field Active Client A | FE+BE | 43 | 443, 444, 445, 446 |
| TC-GS-IMPORT-E2E-168-isi-dan-styling-berkas-template-custom-field-active-di-akhir-katalog | Isi dan styling berkas template: Custom Field Active di akhir, katalog saat diunduh, styling Sheet 1 dan Sheet 2, Custom Field Required | FE+BE | 83 | 447, 448, 449, 450, 451, 452, 762 |
| TC-GS-IMPORT-E2E-169-absence-create-missing-options-yang-tidak-menambah-opsi-apa-pun-tidak | Absence: Create Missing Options yang tidak menambah opsi apa pun tidak menulis entri log | FE+BE | 12 | 923 |
| TC-GS-IMPORT-E2E-170-role-matrix-download-template-enabled-untuk-read-only-dan-import-data | Role Matrix: Download Template Enabled untuk Read Only dan Import data (Read Only) | FE+BE | 11 | 454, 761 |
| TC-GS-IMPORT-E2E-171-defense-in-depth-izin-dan-isolasi-plan-free-403-lock-409-isolasi-tenant | Defense-in-depth: izin dan isolasi (plan Free 403, lock 409, isolasi tenant 404, Read Only 403, tanpa sesi 401, Create Missing Options 403) | FE+BE | 63 | 530, 531, 534, 538, 810, 931 |
| TC-GS-IMPORT-E2E-172-defense-in-depth-injeksi-markup-rumus-pada-sel-dan-unggahan-langsung | Defense-in-depth: injeksi markup/rumus pada sel dan unggahan langsung yang melanggar penyaringan berkas (422, tanpa berkas sementara, tanpa draft) | FE+BE | 52 | 536, 537, 547, 577, 814 |
| TC-GS-IMPORT-E2E-173-defense-in-depth-kontrak-idempoten-via-permintaan-langsung-remove-ulang | Defense-in-depth: kontrak idempoten via permintaan langsung (Remove ulang, AI Accept ulang, acquire kunci ditolak 409, AI Accept/Dismiss pada baris terhapus) | FE+BE | 54 | 545, 546, 548, 841 |
| TC-GS-IMPORT-E2E-174-resilience-koneksi-terputus-saat-confirm-mapping-tab-ditutup-saat-modal | Resilience: koneksi terputus saat Confirm Mapping, tab ditutup saat modal terbuka, gagal unduh Changelog, gagal memuat Changelog (Try Again) | FE+BE | 59 | 539, 540, 541, 793, 794 |
| TC-GS-IMPORT-E2E-175-multi-konteks-aksi-mutasi-pada-draft-yang-baru-dihapus-admin-lain-draft | Multi-konteks: aksi mutasi pada draft yang baru dihapus admin lain (Draft Tidak Ditemukan), tujuh tab, dan Delete All Rows kategori yang sudah dihapus | FE+BE | 75 | 542, 543, 544 |
| TC-GS-IMPORT-E2E-176-multi-konteks-kunci-sesi-edit-dipegang-admin-lain-dialog-draft-is-being | Multi-konteks: kunci sesi edit dipegang admin lain (dialog Draft Is Being Edited, tulis-balik evaluasi ditekan) dan tidak ada push real-time | FE+BE | 71 | 516, 552, 574, 946 |
| TC-GS-IMPORT-E2E-177-harness-eksternal-worker-commit-dijeda-atau-dihentikan-entri-rows | Harness eksternal worker commit: dijeda atau dihentikan (entri rows remaining, tanpa entri bila 0 terkomit, tulis-balik tidak jalan saat committing, 409 saat committing, job tanpa kemajuan 15 menit) | FE+BE | 111 | 426, 518, 532, 553, 755, 809, 947 |
| TC-GS-IMPORT-E2E-178-volume-draft-150-baris-client-limit-selection-limit-100-untuk-filter | Volume: draft 150 baris Client Limit (Selection Limit 100) untuk filter kartu halaman 2, retensi Sub-Tab, pagination 10/25/50/100, lompat halaman, reset halaman | FE+BE | 67 | 464, 472, 478, 479, 480, 576, 586, 763 |
| TC-GS-IMPORT-E2E-179-volume-batas-10000-baris-staging-ditegakkan-server-pada-permintaan | Volume: batas 10000 baris Staging ditegakkan server pada permintaan langsung (draft 9995 baris, +10 ditolak 422 all-or-nothing) | FE+BE | 6 | 533 |
| TC-GS-IMPORT-E2E-180-binary-buffer-isi-berkas-changelog-csv-xlsx-header-30-baris-sheet | Binary buffer: isi berkas Changelog CSV/XLSX (header, 30 baris, sheet, mengikuti Search dan kolom) dan isi Download Template tanpa Custom Field Deactivated | FE+BE | 52 | 498, 791, 792, 959 |
| TC-GS-IMPORT-E2E-181-absence-log-edit-sel-duplikasi-hapus-baris-discard-draft-tidak-mencatat | Absence log: edit sel, duplikasi, hapus baris, Discard Draft tidak mencatat Changelog Import, System Log, Activity Log (Client A) | FE+BE | 85 | 428, 429, 430, 431 |
| TC-GS-IMPORT-E2E-182-absence-log-penolakan-berkas-di-column-mapping-dan-upload-confirm | Absence log: penolakan berkas di Column Mapping dan Upload + Confirm Mapping (Append) tidak mencatat ke Changelog Import, System Log, Activity Log | FE+BE | 47 | 432, 433 |
| TC-GS-IMPORT-E2E-183-absence-log-ai-accept-dismiss-bulk-delete-delete-all-rows-tidak | Absence log: AI Accept/Dismiss, Bulk Delete, Delete All Rows tidak mencatat ke Changelog Import, System Log, Activity Log (Client C) | FE+BE | 65 | 434, 753, 754 |
| TC-GS-IMPORT-E2E-184-absence-log-aktivitas-pre-commit-edit-remove-discard-tidak-menambah | Absence log: aktivitas pre-commit (edit, remove, discard) tidak menambah entri Changelog Import (seed 30 entri) | FE+BE | 22 | 500 |
| TC-GS-IMPORT-E2E-185-state-tenant-tulis-balik-evaluasi-ditekan-saat-suspended-dan-expired | State tenant: tulis-balik evaluasi ditekan saat Suspended dan Expired, draft tersimpan saat turun ke plan Free dan naik kembali, produk Access dicabut dari organisasi | FE+BE | 40 | 526, 554, 575, 818 |
| TC-GS-IMPORT-E2E-186-android-native-checkbox-bulk-bar-toggle-edit-tidak-ada-card-list | Android native: checkbox/bulk bar/toggle Edit tidak ada, card list, Download Template di bottom sheet, form satu kolom di bottom sheet, bottom sheet layar penuh, grid kartu 2 kolom, tombol callout wrap, tooltip Disabled hilang otomatis | FE+BE | 79 | 555, 556, 557, 558, 559, 560, 561, 562, 811, 836, 935 |
| TC-GS-IMPORT-E2E-187-confirm-mapping-berkas-brand-campuran-menghasilkan-5-pending-3-error-2 | Confirm Mapping berkas Brand campuran menghasilkan 5 pending, 3 error, 2 duplicate beserta kartu, callout, footer | FE+BE | 12 | 458 |
| TC-GS-IMPORT-E2E-188-client-f-staging-metric-cards-error-summary-callout-filter-kategori-dan | Client F: Staging Metric Cards, Error Summary Callout, filter kategori, dan retensi state (sidebar, Back, F5) | FE+BE | 66 | 459, 460, 461, 462, 463, 467, 468, 469, 470, 473, 764, 765 |
| TC-GS-IMPORT-E2E-189-client-f-struktur-staging-table-kolom-badge-row-urutan-dan-ketiadaan | Client F: struktur Staging Table (kolom, badge, Row #, urutan) dan ketiadaan Search/Filter/Sort/Column Visibility/unduh laporan, kontras warna | FE+BE | 36 | 474, 475, 481, 482, 488, 771, 890 |
| TC-GS-IMPORT-E2E-190-client-f-filter-kategori-otomatis-terlepas-saat-baris-pelanggar | Client F: filter kategori otomatis terlepas saat baris pelanggar terakhir hilang, dan kartu Active berhitung 0 setelah admin kedua menghapus (race pemicu) | FE+BE | 23 | 466, 471 |
| TC-GS-IMPORT-E2E-191-client-a-row-urut-append-melanjutkan-nomor-kartu-count-0-disabled-dan | Client A: Row # urut, Append melanjutkan nomor, kartu count 0 Disabled, dan kolom Staging Table tiap Sub-Tab (Measurement, Position, Division, User Login, User Non Login) | FE+BE | 34 | 465, 477, 487, 766, 767, 768, 770 |
| TC-GS-IMPORT-E2E-192-client-c-tooltip-badge-duplicate-sistem-vs-antar-baris-dan-tampilan | Client C: tooltip badge duplicate (sistem vs antar-baris) dan tampilan nilai Tab User Login (Access, Phone, tanggal mentah, strip) hasil unggah | FE+BE | 18 | 476, 769 |
| TC-GS-IMPORT-E2E-193-client-e-kolom-tanggal-tampil-mentah-yyyy-mm-dd-dan-batas-active-period | Client E: kolom tanggal tampil mentah YYYY-MM-DD dan batas Active Period besok menurut zona waktu client | FE+BE | 24 | 486, 529 |
| TC-GS-IMPORT-E2E-194-tombol-changelog-di-header-icon-only-dan-empty-state-modal-changelog | Tombol Changelog di header (icon-only) dan empty state Modal Changelog tanpa entri | FE+BE | 10 | 491, 499 |
| TC-GS-IMPORT-E2E-195-modal-changelog-import-screening-pagination-search-action-data-modified | Modal Changelog Import: screening, pagination, Search (Action, Data, Modified By, bukan Date), hover Modified By, dan menutup modal | FE+BE | 50 | 489, 490, 492, 501, 776, 777, 778, 799 |
| TC-GS-IMPORT-E2E-196-modal-changelog-import-filter-panel-date-action-modified-by-opsi | Modal Changelog Import: Filter Panel (Date, Action, Modified By), opsi dropdown, chip +N more, filter gabungan | FE+BE | 57 | 493, 494, 495, 496, 780, 781, 782, 783 |
| TC-GS-IMPORT-E2E-197-modal-changelog-import-kombinasi-search-dan-filter-clear-field-empty | Modal Changelog Import: kombinasi Search dan Filter, Clear Field, empty state pulih | FE+BE | 48 | 784, 785, 786, 787 |
| TC-GS-IMPORT-E2E-198-modal-changelog-import-pengurutan-tiga-tahap-kolom-action-date-data | Modal Changelog Import: pengurutan tiga tahap kolom Action, Date, Data, Modified By | FE+BE | 37 | 497, 788, 789, 790 |
| TC-GS-IMPORT-E2E-199-modal-changelog-import-column-visibility-dan-setup-column-preview-save | Modal Changelog Import: Column Visibility dan Setup Column (preview, Save, Reset, F5, pemisahan dari Staging Table) | FE+BE | 69 | 502, 503, 779, 795, 796, 797, 798 |
| TC-GS-IMPORT-E2E-200-kolom-date-changelog-import-mengikuti-date-time-format-dan-time-zone | Kolom Date Changelog Import mengikuti Date, Time Format, dan Time Zone General Settings (modal seed dan entri hasil commit) | FE+BE | 28 | 757, 800 |
| TC-GS-IMPORT-E2E-201-commit-brand-measurement-position-menulis-satu-entri-ringkasan-ke | Commit Brand, Measurement, Position menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log; kolom tiap surface | FE+BE | 58 | 419, 420, 421, 425 |
| TC-GS-IMPORT-E2E-202-commit-division-user-login-user-non-login-menulis-satu-entri-ringkasan | Commit Division, User Login, User Non Login menulis satu entri ringkasan ke Changelog Import, System Log, Activity Log | FE+BE | 45 | 422, 423, 424 |
| TC-GS-IMPORT-E2E-203-entri-ringkasan-changelog-import-immutable-dan-commit-0-baris-terkomit | Entri ringkasan Changelog Import immutable, dan commit 0 baris terkomit tetap menulis satu entri | FE+BE | 34 | 427, 756 |
| TC-GS-IMPORT-E2E-204-refleksi-definisi-custom-field-pada-kolom-staging-table-user-login | Refleksi definisi Custom Field pada kolom Staging Table User Login: rename, ubah tipe, Decimal Places, nonaktif, aktif kembali, hapus | FE+BE | 55 | 504, 505, 506, 507, 508, 514 |
| TC-GS-IMPORT-E2E-205-refleksi-dropdown-option-dan-perubahan-custom-field-pada-seluruh-baris | Refleksi Dropdown option dan perubahan Custom Field pada seluruh baris draft (Save, Remove, Append, pindah Sub-Tab, field baru Optional) | FE+BE | 61 | 510, 511, 512, 515, 804, 805, 806, 949 |
| TC-GS-IMPORT-E2E-206-custom-field-required-shift-notes-overtime-evaluasi-ulang-baris | Custom Field Required (Shift Notes, Overtime): evaluasi ulang baris, pemulihan lewat Edit, Edit this page, callout per kategori | FE+BE | 49 | 509, 941, 942, 943 |
| TC-GS-IMPORT-E2E-207-custom-field-required-yang-dinonaktifkan-atau-dihapus-tidak-dievaluasi | Custom Field Required yang dinonaktifkan atau dihapus tidak dievaluasi; aktif kembali berlaku retroaktif | FE+BE | 56 | 939, 940, 952, 953 |
| TC-GS-IMPORT-E2E-208-kolom-custom-field-deactivated-tampil-seperti-active-sel-disunting | Kolom Custom Field Deactivated tampil seperti Active, sel disunting dengan Select, validasi Decimal Places, Append | FE+BE | 41 | 950, 951, 960 |
| TC-GS-IMPORT-E2E-209-banner-custom-field-deactivated-deleted-tutup-lewat-di-sisi-klien-satu | Banner Custom Field (Deactivated, Deleted): tutup lewat [×] di sisi klien, satu banner per field, kondisi tampil, label terakhir pada rename lalu hapus | FE+BE | 63 | 955, 956, 957, 961, 962 |
| TC-GS-IMPORT-E2E-210-pembaca-import-data-read-only-hasil-hitung-error-read-only-tanpa-tulis | Pembaca Import data (Read Only): hasil hitung error read-only tanpa tulis-balik, Banner Custom Field dapat ditutup tanpa mengubah draft | FE+BE | 27 | 517, 945, 958 |
| TC-GS-IMPORT-E2E-211-client-c-refleksi-opsi-dropdown-tambah-manual-hapus-tak-peka-kapital | Client C: refleksi opsi Dropdown (tambah manual, hapus, tak peka kapital) dan tipe diubah ke Phone, termasuk Custom Field Deactivated dengan Create Missing Options | FE+BE | 66 | 513, 519, 521, 934, 963 |
| TC-GS-IMPORT-E2E-212-client-c-custom-field-baru-atau-optional-dijadikan-required-lalu | Client C: Custom Field baru atau Optional dijadikan Required, lalu dikembalikan Optional | FE+BE | 30 | 936, 937, 938 |
| TC-GS-IMPORT-E2E-213-client-e-hasil-commit-setelah-custom-field-master-data-berubah-gate | Client E: hasil commit setelah Custom Field/master data berubah (gate late-binding), baris gagal tidak membatalkan baris lain, baris error tetap, Brand existing tidak diperbarui | FE+BE | 80 | 520, 549, 550, 551, 803, 944 |
| TC-GS-IMPORT-E2E-214-client-e-custom-field-nonaktif-dihapus-sebelum-import-tetap-terkomit | Client E: Custom Field nonaktif/dihapus sebelum Import tetap terkomit, nilai ditulis ke User; record hasil commit muncul di modul Brand, Division, form Create User | FE+BE | 59 | 528, 801, 802, 954 |
| TC-GS-IMPORT-E2E-215-client-e-refleksi-perubahan-master-data-division-position-dihapus-di | Client E: refleksi perubahan master data (Division/Position dihapus, di-rename, dibuat; Represented By dinonaktifkan) pada baris draft | FE+BE | 58 | 522, 523, 524, 525, 527, 807, 808 |
| TC-GS-IMPORT-E2E-216-draft-dibagikan-ke-seluruh-admin-berkapabilitas-dalam-organisasi-yang | Draft dibagikan ke seluruh admin berkapabilitas dalam organisasi yang sama (Import data Create dan Total Control melihat draft yang sama) | FE+BE | 14 | 535 |

## TC hanya-BE dan alasannya

Tidak ada TC yang dikeluarkan dari spec (0 dari 968 baris). Tabel alasan kosong:

| TC | Alasan |
|---|---|

Tiga TC berstatus kandidat hanya-BE tetapi tetap ditulis sebagai spec kelas a menunggu keputusan user (Keputusan 1 di plan): TC-GS-IMPORT-704, 729, dan 730. Ketiganya memuat asersi UI (sel tetap 121 karakter; daftar Division/Position tidak memuat nama baru) dan polanya identik dengan TC bertanda `Need API` yang sudah masuk spec.

## Pembagian TC lintas spec

- Tidak ada TC yang terbelah: satu baris TC satu spec.
- Tidak ada mode `mock`: seluruh spec FE+BE. TC-GS-IMPORT-18, 79, 578, 610 (resilience murni FE) memakai intercept di atas backend nyata dan boleh dijadikan `mock` bila user menghendaki.

## ID ganda 868–871

`tc-import.md` memuat empat ID yang dipakai dua kali dengan isi berbeda. `sourceTc` spec menulisnya sebagai `id@Lbaris` supaya tiap baris terhitung tepat satu kali:

| ID | Baris pertama | Spec | Baris kedua | Spec |
|---|---|---|---|---|
| 868 | L738 | TC-GS-IMPORT-E2E-049 | L1077 | TC-GS-IMPORT-E2E-073 |
| 869 | L937 | TC-GS-IMPORT-E2E-083 | L1078 | TC-GS-IMPORT-E2E-077 |
| 870 | L1020 | TC-GS-IMPORT-E2E-087 | L1079 | TC-GS-IMPORT-E2E-073 |
| 871 | L938 | TC-GS-IMPORT-E2E-086 | L1080 | TC-GS-IMPORT-E2E-072 |

Catatan: `scripts/check-suite.py` membaca id TC dengan regex `TC-...-\d+` sehingga akhiran `@Lbaris` diabaikan; kedua baris 868–871 dikenali sebagai satu ID yang sama. TC tidak diubah oleh stage ini; usulan di plan: QA memberi nomor baru pada empat baris kedua (blok 3g, baris 1077–1080), misalnya ID kosong 772–775.

## Temuan yang masih terbuka

Temuan TC sumber (ambigu, kontradiktif, precondition kurang) ditulis per spec di butir "Temuan untuk QA" pada `## Notes` spec yang bersangkutan dan tidak diulang di sini. Temuan lintas spec:

- ID ganda 868–871 (lihat bagian di atas): menunggu renumber QA.
- TC-GS-IMPORT-704, 729, 730: keputusan apakah dikeluarkan sebagai hanya-BE (Keputusan 1 di plan).
- Kemampuan teknis yang disediakan tim FE/BE (kontrol worker commit, hook umur draft dan jam server, mock layanan AI, skrip seed, mail-catcher, fixture Admin Console, perangkat Android) ditulis di `## Prerequisites` tiap spec.
- Spec di atas 35 langkah: alasan ditulis di `## Notes` masing-masing spec.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-IMPORT-1 | TC-GS-IMPORT-E2E-011 | FE+BE |
| TC-GS-IMPORT-2 | TC-GS-IMPORT-E2E-011 | FE+BE |
| TC-GS-IMPORT-3 | TC-GS-IMPORT-E2E-011 | FE+BE |
| TC-GS-IMPORT-4 | TC-GS-IMPORT-E2E-012 | FE+BE |
| TC-GS-IMPORT-5 | TC-GS-IMPORT-E2E-012 | FE+BE |
| TC-GS-IMPORT-6 | TC-GS-IMPORT-E2E-012 | FE+BE |
| TC-GS-IMPORT-7 | TC-GS-IMPORT-E2E-001 | FE+BE |
| TC-GS-IMPORT-8 | TC-GS-IMPORT-E2E-001 | FE+BE |
| TC-GS-IMPORT-9 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-10 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-11 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-12 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-13 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-14 | TC-GS-IMPORT-E2E-002 | FE+BE |
| TC-GS-IMPORT-15 | TC-GS-IMPORT-E2E-003 | FE+BE |
| TC-GS-IMPORT-16 | TC-GS-IMPORT-E2E-003 | FE+BE |
| TC-GS-IMPORT-17 | TC-GS-IMPORT-E2E-001 | FE+BE |
| TC-GS-IMPORT-18 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-19 | TC-GS-IMPORT-E2E-004 | FE+BE |
| TC-GS-IMPORT-20 | TC-GS-IMPORT-E2E-001 | FE+BE |
| TC-GS-IMPORT-21 | TC-GS-IMPORT-E2E-004 | FE+BE |
| TC-GS-IMPORT-22 | TC-GS-IMPORT-E2E-007 | FE+BE |
| TC-GS-IMPORT-23 | TC-GS-IMPORT-E2E-007 | FE+BE |
| TC-GS-IMPORT-24 | TC-GS-IMPORT-E2E-005 | FE+BE |
| TC-GS-IMPORT-25 | TC-GS-IMPORT-E2E-062 | FE+BE |
| TC-GS-IMPORT-26 | TC-GS-IMPORT-E2E-008 | FE+BE |
| TC-GS-IMPORT-27 | TC-GS-IMPORT-E2E-063 | FE+BE |
| TC-GS-IMPORT-28 | TC-GS-IMPORT-E2E-063 | FE+BE |
| TC-GS-IMPORT-29 | TC-GS-IMPORT-E2E-064 | FE+BE |
| TC-GS-IMPORT-30 | TC-GS-IMPORT-E2E-064 | FE+BE |
| TC-GS-IMPORT-31 | TC-GS-IMPORT-E2E-063 | FE+BE |
| TC-GS-IMPORT-32 | TC-GS-IMPORT-E2E-065 | FE+BE |
| TC-GS-IMPORT-33 | TC-GS-IMPORT-E2E-010 | FE+BE |
| TC-GS-IMPORT-34 | TC-GS-IMPORT-E2E-065 | FE+BE |
| TC-GS-IMPORT-35 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-36 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-37 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-38 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-39 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-40 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-41 | TC-GS-IMPORT-E2E-046 | FE+BE |
| TC-GS-IMPORT-42 | TC-GS-IMPORT-E2E-045 | FE+BE |
| TC-GS-IMPORT-43 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-44 | TC-GS-IMPORT-E2E-009 | FE+BE |
| TC-GS-IMPORT-45 | TC-GS-IMPORT-E2E-059 | FE+BE |
| TC-GS-IMPORT-46 | TC-GS-IMPORT-E2E-059 | FE+BE |
| TC-GS-IMPORT-47 | TC-GS-IMPORT-E2E-060 | FE+BE |
| TC-GS-IMPORT-48 | TC-GS-IMPORT-E2E-061 | FE+BE |
| TC-GS-IMPORT-49 | TC-GS-IMPORT-E2E-050 | FE+BE |
| TC-GS-IMPORT-50 | TC-GS-IMPORT-E2E-050 | FE+BE |
| TC-GS-IMPORT-51 | TC-GS-IMPORT-E2E-013 | FE+BE |
| TC-GS-IMPORT-52 | TC-GS-IMPORT-E2E-013 | FE+BE |
| TC-GS-IMPORT-53 | TC-GS-IMPORT-E2E-013 | FE+BE |
| TC-GS-IMPORT-54 | TC-GS-IMPORT-E2E-013 | FE+BE |
| TC-GS-IMPORT-55 | TC-GS-IMPORT-E2E-014 | FE+BE |
| TC-GS-IMPORT-56 | TC-GS-IMPORT-E2E-015 | FE+BE |
| TC-GS-IMPORT-57 | TC-GS-IMPORT-E2E-015 | FE+BE |
| TC-GS-IMPORT-58 | TC-GS-IMPORT-E2E-014 | FE+BE |
| TC-GS-IMPORT-59 | TC-GS-IMPORT-E2E-015 | FE+BE |
| TC-GS-IMPORT-60 | TC-GS-IMPORT-E2E-016 | FE+BE |
| TC-GS-IMPORT-61 | TC-GS-IMPORT-E2E-016 | FE+BE |
| TC-GS-IMPORT-62 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-63 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-64 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-65 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-66 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-67 | TC-GS-IMPORT-E2E-017 | FE+BE |
| TC-GS-IMPORT-68 | TC-GS-IMPORT-E2E-018 | FE+BE |
| TC-GS-IMPORT-69 | TC-GS-IMPORT-E2E-019 | FE+BE |
| TC-GS-IMPORT-70 | TC-GS-IMPORT-E2E-019 | FE+BE |
| TC-GS-IMPORT-71 | TC-GS-IMPORT-E2E-018 | FE+BE |
| TC-GS-IMPORT-72 | TC-GS-IMPORT-E2E-018 | FE+BE |
| TC-GS-IMPORT-73 | TC-GS-IMPORT-E2E-018 | FE+BE |
| TC-GS-IMPORT-74 | TC-GS-IMPORT-E2E-018 | FE+BE |
| TC-GS-IMPORT-75 | TC-GS-IMPORT-E2E-048 | FE+BE |
| TC-GS-IMPORT-76 | TC-GS-IMPORT-E2E-020 | FE+BE |
| TC-GS-IMPORT-77 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-78 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-79 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-80 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-81 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-82 | TC-GS-IMPORT-E2E-054 | FE+BE |
| TC-GS-IMPORT-83 | TC-GS-IMPORT-E2E-046 | FE+BE |
| TC-GS-IMPORT-84 | TC-GS-IMPORT-E2E-046 | FE+BE |
| TC-GS-IMPORT-85 | TC-GS-IMPORT-E2E-022 | FE+BE |
| TC-GS-IMPORT-86 | TC-GS-IMPORT-E2E-022 | FE+BE |
| TC-GS-IMPORT-87 | TC-GS-IMPORT-E2E-022 | FE+BE |
| TC-GS-IMPORT-88 | TC-GS-IMPORT-E2E-022 | FE+BE |
| TC-GS-IMPORT-89 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-90 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-91 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-92 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-93 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-94 | TC-GS-IMPORT-E2E-023 | FE+BE |
| TC-GS-IMPORT-95 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-96 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-97 | TC-GS-IMPORT-E2E-022 | FE+BE |
| TC-GS-IMPORT-98 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-99 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-100 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-101 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-102 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-103 | TC-GS-IMPORT-E2E-024 | FE+BE |
| TC-GS-IMPORT-104 | TC-GS-IMPORT-E2E-025 | FE+BE |
| TC-GS-IMPORT-105 | TC-GS-IMPORT-E2E-025 | FE+BE |
| TC-GS-IMPORT-106 | TC-GS-IMPORT-E2E-025 | FE+BE |
| TC-GS-IMPORT-107 | TC-GS-IMPORT-E2E-025 | FE+BE |
| TC-GS-IMPORT-108 | TC-GS-IMPORT-E2E-025 | FE+BE |
| TC-GS-IMPORT-109 | TC-GS-IMPORT-E2E-028 | FE+BE |
| TC-GS-IMPORT-110 | TC-GS-IMPORT-E2E-026 | FE+BE |
| TC-GS-IMPORT-111 | TC-GS-IMPORT-E2E-026 | FE+BE |
| TC-GS-IMPORT-112 | TC-GS-IMPORT-E2E-026 | FE+BE |
| TC-GS-IMPORT-113 | TC-GS-IMPORT-E2E-026 | FE+BE |
| TC-GS-IMPORT-114 | TC-GS-IMPORT-E2E-032 | FE+BE |
| TC-GS-IMPORT-115 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-116 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-117 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-118 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-119 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-120 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-121 | TC-GS-IMPORT-E2E-027 | FE+BE |
| TC-GS-IMPORT-122 | TC-GS-IMPORT-E2E-026 | FE+BE |
| TC-GS-IMPORT-123 | TC-GS-IMPORT-E2E-031 | FE+BE |
| TC-GS-IMPORT-124 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-125 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-126 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-127 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-128 | TC-GS-IMPORT-E2E-033 | FE+BE |
| TC-GS-IMPORT-129 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-130 | TC-GS-IMPORT-E2E-032 | FE+BE |
| TC-GS-IMPORT-131 | TC-GS-IMPORT-E2E-032 | FE+BE |
| TC-GS-IMPORT-132 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-133 | TC-GS-IMPORT-E2E-031 | FE+BE |
| TC-GS-IMPORT-134 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-135 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-136 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-137 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-138 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-139 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-140 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-141 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-142 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-143 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-144 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-145 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-146 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-147 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-148 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-149 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-150 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-151 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-152 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-153 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-154 | TC-GS-IMPORT-E2E-037 | FE+BE |
| TC-GS-IMPORT-155 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-156 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-157 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-158 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-159 | TC-GS-IMPORT-E2E-039 | FE+BE |
| TC-GS-IMPORT-160 | TC-GS-IMPORT-E2E-039 | FE+BE |
| TC-GS-IMPORT-161 | TC-GS-IMPORT-E2E-039 | FE+BE |
| TC-GS-IMPORT-162 | TC-GS-IMPORT-E2E-039 | FE+BE |
| TC-GS-IMPORT-163 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-164 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-165 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-166 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-167 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-168 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-169 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-170 | TC-GS-IMPORT-E2E-043 | FE+BE |
| TC-GS-IMPORT-171 | TC-GS-IMPORT-E2E-034 | FE+BE |
| TC-GS-IMPORT-172 | TC-GS-IMPORT-E2E-043 | FE+BE |
| TC-GS-IMPORT-173 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-174 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-175 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-176 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-177 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-178 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-179 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-180 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-181 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-182 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-183 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-184 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-185 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-186 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-187 | TC-GS-IMPORT-E2E-088 | FE+BE |
| TC-GS-IMPORT-188 | TC-GS-IMPORT-E2E-087 | FE+BE |
| TC-GS-IMPORT-189 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-190 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-191 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-192 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-193 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-194 | TC-GS-IMPORT-E2E-078 | FE+BE |
| TC-GS-IMPORT-195 | TC-GS-IMPORT-E2E-107 | FE+BE |
| TC-GS-IMPORT-196 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-197 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-198 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-199 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-200 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-201 | TC-GS-IMPORT-E2E-091 | FE+BE |
| TC-GS-IMPORT-202 | TC-GS-IMPORT-E2E-091 | FE+BE |
| TC-GS-IMPORT-203 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-204 | TC-GS-IMPORT-E2E-097 | FE+BE |
| TC-GS-IMPORT-205 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-206 | TC-GS-IMPORT-E2E-098 | FE+BE |
| TC-GS-IMPORT-207 | TC-GS-IMPORT-E2E-076 | FE+BE |
| TC-GS-IMPORT-208 | TC-GS-IMPORT-E2E-077 | FE+BE |
| TC-GS-IMPORT-209 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-210 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-211 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-212 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-213 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-214 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-215 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-216 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-217 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-218 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-219 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-220 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-221 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-222 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-223 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-224 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-225 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-226 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-227 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-228 | TC-GS-IMPORT-E2E-097 | FE+BE |
| TC-GS-IMPORT-229 | TC-GS-IMPORT-E2E-097 | FE+BE |
| TC-GS-IMPORT-230 | TC-GS-IMPORT-E2E-097 | FE+BE |
| TC-GS-IMPORT-231 | TC-GS-IMPORT-E2E-097 | FE+BE |
| TC-GS-IMPORT-232 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-233 | TC-GS-IMPORT-E2E-079 | FE+BE |
| TC-GS-IMPORT-234 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-235 | TC-GS-IMPORT-E2E-091 | FE+BE |
| TC-GS-IMPORT-236 | TC-GS-IMPORT-E2E-106 | FE+BE |
| TC-GS-IMPORT-237 | TC-GS-IMPORT-E2E-068 | FE+BE |
| TC-GS-IMPORT-238 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-239 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-240 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-241 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-242 | TC-GS-IMPORT-E2E-070 | FE+BE |
| TC-GS-IMPORT-243 | TC-GS-IMPORT-E2E-070 | FE+BE |
| TC-GS-IMPORT-244 | TC-GS-IMPORT-E2E-070 | FE+BE |
| TC-GS-IMPORT-245 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-246 | TC-GS-IMPORT-E2E-069 | FE+BE |
| TC-GS-IMPORT-247 | TC-GS-IMPORT-E2E-071 | FE+BE |
| TC-GS-IMPORT-248 | TC-GS-IMPORT-E2E-068 | FE+BE |
| TC-GS-IMPORT-249 | TC-GS-IMPORT-E2E-068 | FE+BE |
| TC-GS-IMPORT-250 | TC-GS-IMPORT-E2E-074 | FE+BE |
| TC-GS-IMPORT-251 | TC-GS-IMPORT-E2E-074 | FE+BE |
| TC-GS-IMPORT-252 | TC-GS-IMPORT-E2E-074 | FE+BE |
| TC-GS-IMPORT-253 | TC-GS-IMPORT-E2E-075 | FE+BE |
| TC-GS-IMPORT-254 | TC-GS-IMPORT-E2E-075 | FE+BE |
| TC-GS-IMPORT-255 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-256 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-257 | TC-GS-IMPORT-E2E-075 | FE+BE |
| TC-GS-IMPORT-258 | TC-GS-IMPORT-E2E-108 | FE+BE |
| TC-GS-IMPORT-259 | TC-GS-IMPORT-E2E-108 | FE+BE |
| TC-GS-IMPORT-260 | TC-GS-IMPORT-E2E-108 | FE+BE |
| TC-GS-IMPORT-261 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-262 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-263 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-264 | TC-GS-IMPORT-E2E-110 | FE+BE |
| TC-GS-IMPORT-265 | TC-GS-IMPORT-E2E-110 | FE+BE |
| TC-GS-IMPORT-266 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-267 | TC-GS-IMPORT-E2E-110 | FE+BE |
| TC-GS-IMPORT-268 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-269 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-270 | TC-GS-IMPORT-E2E-078 | FE+BE |
| TC-GS-IMPORT-271 | TC-GS-IMPORT-E2E-078 | FE+BE |
| TC-GS-IMPORT-272 | TC-GS-IMPORT-E2E-078 | FE+BE |
| TC-GS-IMPORT-273 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-274 | TC-GS-IMPORT-E2E-112 | FE+BE |
| TC-GS-IMPORT-275 | TC-GS-IMPORT-E2E-112 | FE+BE |
| TC-GS-IMPORT-276 | TC-GS-IMPORT-E2E-107 | FE+BE |
| TC-GS-IMPORT-277 | TC-GS-IMPORT-E2E-107 | FE+BE |
| TC-GS-IMPORT-278 | TC-GS-IMPORT-E2E-113 | FE+BE |
| TC-GS-IMPORT-279 | TC-GS-IMPORT-E2E-112 | FE+BE |
| TC-GS-IMPORT-280 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-281 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-282 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-283 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-284 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-285 | TC-GS-IMPORT-E2E-112 | FE+BE |
| TC-GS-IMPORT-286 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-287 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-288 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-289 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-290 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-291 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-292 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-293 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-294 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-295 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-296 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-297 | TC-GS-IMPORT-E2E-149 | FE+BE |
| TC-GS-IMPORT-298 | TC-GS-IMPORT-E2E-146 | FE+BE |
| TC-GS-IMPORT-299 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-300 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-301 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-302 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-303 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-304 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-305 | TC-GS-IMPORT-E2E-131 | FE+BE |
| TC-GS-IMPORT-306 | TC-GS-IMPORT-E2E-153 | FE+BE |
| TC-GS-IMPORT-307 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-308 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-309 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-310 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-311 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-312 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-313 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-314 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-315 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-316 | TC-GS-IMPORT-E2E-146 | FE+BE |
| TC-GS-IMPORT-317 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-318 | TC-GS-IMPORT-E2E-120 | FE+BE |
| TC-GS-IMPORT-319 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-320 | TC-GS-IMPORT-E2E-120 | FE+BE |
| TC-GS-IMPORT-321 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-322 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-323 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-324 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-325 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-326 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-327 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-328 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-329 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-330 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-331 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-332 | TC-GS-IMPORT-E2E-165 | FE+BE |
| TC-GS-IMPORT-333 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-334 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-335 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-336 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-337 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-338 | TC-GS-IMPORT-E2E-126 | FE+BE |
| TC-GS-IMPORT-339 | TC-GS-IMPORT-E2E-153 | FE+BE |
| TC-GS-IMPORT-340 | TC-GS-IMPORT-E2E-128 | FE+BE |
| TC-GS-IMPORT-341 | TC-GS-IMPORT-E2E-128 | FE+BE |
| TC-GS-IMPORT-342 | TC-GS-IMPORT-E2E-128 | FE+BE |
| TC-GS-IMPORT-343 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-344 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-345 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-346 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-347 | TC-GS-IMPORT-E2E-131 | FE+BE |
| TC-GS-IMPORT-348 | TC-GS-IMPORT-E2E-132 | FE+BE |
| TC-GS-IMPORT-349 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-350 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-351 | TC-GS-IMPORT-E2E-123 | FE+BE |
| TC-GS-IMPORT-352 | TC-GS-IMPORT-E2E-133 | FE+BE |
| TC-GS-IMPORT-353 | TC-GS-IMPORT-E2E-133 | FE+BE |
| TC-GS-IMPORT-354 | TC-GS-IMPORT-E2E-133 | FE+BE |
| TC-GS-IMPORT-355 | TC-GS-IMPORT-E2E-133 | FE+BE |
| TC-GS-IMPORT-356 | TC-GS-IMPORT-E2E-134 | FE+BE |
| TC-GS-IMPORT-357 | TC-GS-IMPORT-E2E-134 | FE+BE |
| TC-GS-IMPORT-358 | TC-GS-IMPORT-E2E-135 | FE+BE |
| TC-GS-IMPORT-359 | TC-GS-IMPORT-E2E-135 | FE+BE |
| TC-GS-IMPORT-360 | TC-GS-IMPORT-E2E-136 | FE+BE |
| TC-GS-IMPORT-361 | TC-GS-IMPORT-E2E-159 | FE+BE |
| TC-GS-IMPORT-362 | TC-GS-IMPORT-E2E-138 | FE+BE |
| TC-GS-IMPORT-363 | TC-GS-IMPORT-E2E-138 | FE+BE |
| TC-GS-IMPORT-364 | TC-GS-IMPORT-E2E-163 | FE+BE |
| TC-GS-IMPORT-365 | TC-GS-IMPORT-E2E-156 | FE+BE |
| TC-GS-IMPORT-366 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-367 | TC-GS-IMPORT-E2E-139 | FE+BE |
| TC-GS-IMPORT-368 | TC-GS-IMPORT-E2E-163 | FE+BE |
| TC-GS-IMPORT-369 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-370 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-371 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-372 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-373 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-374 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-375 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-376 | TC-GS-IMPORT-E2E-155 | FE+BE |
| TC-GS-IMPORT-377 | TC-GS-IMPORT-E2E-154 | FE+BE |
| TC-GS-IMPORT-378 | TC-GS-IMPORT-E2E-155 | FE+BE |
| TC-GS-IMPORT-379 | TC-GS-IMPORT-E2E-155 | FE+BE |
| TC-GS-IMPORT-380 | TC-GS-IMPORT-E2E-155 | FE+BE |
| TC-GS-IMPORT-381 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-382 | TC-GS-IMPORT-E2E-156 | FE+BE |
| TC-GS-IMPORT-383 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-384 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-385 | TC-GS-IMPORT-E2E-158 | FE+BE |
| TC-GS-IMPORT-386 | TC-GS-IMPORT-E2E-158 | FE+BE |
| TC-GS-IMPORT-387 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-388 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-389 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-390 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-391 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-392 | TC-GS-IMPORT-E2E-141 | FE+BE |
| TC-GS-IMPORT-393 | TC-GS-IMPORT-E2E-141 | FE+BE |
| TC-GS-IMPORT-394 | TC-GS-IMPORT-E2E-141 | FE+BE |
| TC-GS-IMPORT-395 | TC-GS-IMPORT-E2E-141 | FE+BE |
| TC-GS-IMPORT-396 | TC-GS-IMPORT-E2E-142 | FE+BE |
| TC-GS-IMPORT-397 | TC-GS-IMPORT-E2E-142 | FE+BE |
| TC-GS-IMPORT-398 | TC-GS-IMPORT-E2E-142 | FE+BE |
| TC-GS-IMPORT-399 | TC-GS-IMPORT-E2E-142 | FE+BE |
| TC-GS-IMPORT-400 | TC-GS-IMPORT-E2E-142 | FE+BE |
| TC-GS-IMPORT-401 | TC-GS-IMPORT-E2E-143 | FE+BE |
| TC-GS-IMPORT-402 | TC-GS-IMPORT-E2E-143 | FE+BE |
| TC-GS-IMPORT-403 | TC-GS-IMPORT-E2E-143 | FE+BE |
| TC-GS-IMPORT-404 | TC-GS-IMPORT-E2E-164 | FE+BE |
| TC-GS-IMPORT-405 | TC-GS-IMPORT-E2E-164 | FE+BE |
| TC-GS-IMPORT-406 | TC-GS-IMPORT-E2E-164 | FE+BE |
| TC-GS-IMPORT-407 | TC-GS-IMPORT-E2E-164 | FE+BE |
| TC-GS-IMPORT-408 | TC-GS-IMPORT-E2E-165 | FE+BE |
| TC-GS-IMPORT-409 | TC-GS-IMPORT-E2E-165 | FE+BE |
| TC-GS-IMPORT-410 | TC-GS-IMPORT-E2E-151 | FE+BE |
| TC-GS-IMPORT-411 | TC-GS-IMPORT-E2E-160 | FE+BE |
| TC-GS-IMPORT-412 | TC-GS-IMPORT-E2E-160 | FE+BE |
| TC-GS-IMPORT-413 | TC-GS-IMPORT-E2E-160 | FE+BE |
| TC-GS-IMPORT-414 | TC-GS-IMPORT-E2E-160 | FE+BE |
| TC-GS-IMPORT-415 | TC-GS-IMPORT-E2E-160 | FE+BE |
| TC-GS-IMPORT-416 | TC-GS-IMPORT-E2E-161 | FE+BE |
| TC-GS-IMPORT-417 | TC-GS-IMPORT-E2E-161 | FE+BE |
| TC-GS-IMPORT-418 | TC-GS-IMPORT-E2E-161 | FE+BE |
| TC-GS-IMPORT-419 | TC-GS-IMPORT-E2E-201 | FE+BE |
| TC-GS-IMPORT-420 | TC-GS-IMPORT-E2E-201 | FE+BE |
| TC-GS-IMPORT-421 | TC-GS-IMPORT-E2E-201 | FE+BE |
| TC-GS-IMPORT-422 | TC-GS-IMPORT-E2E-202 | FE+BE |
| TC-GS-IMPORT-423 | TC-GS-IMPORT-E2E-202 | FE+BE |
| TC-GS-IMPORT-424 | TC-GS-IMPORT-E2E-202 | FE+BE |
| TC-GS-IMPORT-425 | TC-GS-IMPORT-E2E-201 | FE+BE |
| TC-GS-IMPORT-426 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-427 | TC-GS-IMPORT-E2E-203 | FE+BE |
| TC-GS-IMPORT-428 | TC-GS-IMPORT-E2E-181 | FE+BE |
| TC-GS-IMPORT-429 | TC-GS-IMPORT-E2E-181 | FE+BE |
| TC-GS-IMPORT-430 | TC-GS-IMPORT-E2E-181 | FE+BE |
| TC-GS-IMPORT-431 | TC-GS-IMPORT-E2E-181 | FE+BE |
| TC-GS-IMPORT-432 | TC-GS-IMPORT-E2E-182 | FE+BE |
| TC-GS-IMPORT-433 | TC-GS-IMPORT-E2E-182 | FE+BE |
| TC-GS-IMPORT-434 | TC-GS-IMPORT-E2E-183 | FE+BE |
| TC-GS-IMPORT-435 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-436 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-437 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-438 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-439 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-440 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-441 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-442 | TC-GS-IMPORT-E2E-166 | FE+BE |
| TC-GS-IMPORT-443 | TC-GS-IMPORT-E2E-167 | FE+BE |
| TC-GS-IMPORT-444 | TC-GS-IMPORT-E2E-167 | FE+BE |
| TC-GS-IMPORT-445 | TC-GS-IMPORT-E2E-167 | FE+BE |
| TC-GS-IMPORT-446 | TC-GS-IMPORT-E2E-167 | FE+BE |
| TC-GS-IMPORT-447 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-448 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-449 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-450 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-451 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-452 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-453 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-454 | TC-GS-IMPORT-E2E-170 | FE+BE |
| TC-GS-IMPORT-455 | TC-GS-IMPORT-E2E-144 | FE+BE |
| TC-GS-IMPORT-456 | TC-GS-IMPORT-E2E-144 | FE+BE |
| TC-GS-IMPORT-457 | TC-GS-IMPORT-E2E-144 | FE+BE |
| TC-GS-IMPORT-458 | TC-GS-IMPORT-E2E-187 | FE+BE |
| TC-GS-IMPORT-459 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-460 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-461 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-462 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-463 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-464 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-465 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-466 | TC-GS-IMPORT-E2E-190 | FE+BE |
| TC-GS-IMPORT-467 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-468 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-469 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-470 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-471 | TC-GS-IMPORT-E2E-190 | FE+BE |
| TC-GS-IMPORT-472 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-473 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-474 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-475 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-476 | TC-GS-IMPORT-E2E-192 | FE+BE |
| TC-GS-IMPORT-477 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-478 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-479 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-480 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-481 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-482 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-486 | TC-GS-IMPORT-E2E-193 | FE+BE |
| TC-GS-IMPORT-487 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-488 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-489 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-490 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-491 | TC-GS-IMPORT-E2E-194 | FE+BE |
| TC-GS-IMPORT-492 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-493 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-494 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-495 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-496 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-497 | TC-GS-IMPORT-E2E-198 | FE+BE |
| TC-GS-IMPORT-498 | TC-GS-IMPORT-E2E-180 | FE+BE |
| TC-GS-IMPORT-499 | TC-GS-IMPORT-E2E-194 | FE+BE |
| TC-GS-IMPORT-500 | TC-GS-IMPORT-E2E-184 | FE+BE |
| TC-GS-IMPORT-501 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-502 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-503 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-504 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-505 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-506 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-507 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-508 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-509 | TC-GS-IMPORT-E2E-206 | FE+BE |
| TC-GS-IMPORT-510 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-511 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-512 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-513 | TC-GS-IMPORT-E2E-211 | FE+BE |
| TC-GS-IMPORT-514 | TC-GS-IMPORT-E2E-204 | FE+BE |
| TC-GS-IMPORT-515 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-516 | TC-GS-IMPORT-E2E-176 | FE+BE |
| TC-GS-IMPORT-517 | TC-GS-IMPORT-E2E-210 | FE+BE |
| TC-GS-IMPORT-518 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-519 | TC-GS-IMPORT-E2E-211 | FE+BE |
| TC-GS-IMPORT-520 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-521 | TC-GS-IMPORT-E2E-211 | FE+BE |
| TC-GS-IMPORT-522 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-523 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-524 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-525 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-526 | TC-GS-IMPORT-E2E-185 | FE+BE |
| TC-GS-IMPORT-527 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-528 | TC-GS-IMPORT-E2E-214 | FE+BE |
| TC-GS-IMPORT-529 | TC-GS-IMPORT-E2E-193 | FE+BE |
| TC-GS-IMPORT-530 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-531 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-532 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-533 | TC-GS-IMPORT-E2E-179 | FE+BE |
| TC-GS-IMPORT-534 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-535 | TC-GS-IMPORT-E2E-216 | FE+BE |
| TC-GS-IMPORT-536 | TC-GS-IMPORT-E2E-172 | FE+BE |
| TC-GS-IMPORT-537 | TC-GS-IMPORT-E2E-172 | FE+BE |
| TC-GS-IMPORT-538 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-539 | TC-GS-IMPORT-E2E-174 | FE+BE |
| TC-GS-IMPORT-540 | TC-GS-IMPORT-E2E-174 | FE+BE |
| TC-GS-IMPORT-541 | TC-GS-IMPORT-E2E-174 | FE+BE |
| TC-GS-IMPORT-542 | TC-GS-IMPORT-E2E-175 | FE+BE |
| TC-GS-IMPORT-543 | TC-GS-IMPORT-E2E-175 | FE+BE |
| TC-GS-IMPORT-544 | TC-GS-IMPORT-E2E-175 | FE+BE |
| TC-GS-IMPORT-545 | TC-GS-IMPORT-E2E-173 | FE+BE |
| TC-GS-IMPORT-546 | TC-GS-IMPORT-E2E-173 | FE+BE |
| TC-GS-IMPORT-547 | TC-GS-IMPORT-E2E-172 | FE+BE |
| TC-GS-IMPORT-548 | TC-GS-IMPORT-E2E-173 | FE+BE |
| TC-GS-IMPORT-549 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-550 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-551 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-552 | TC-GS-IMPORT-E2E-176 | FE+BE |
| TC-GS-IMPORT-553 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-554 | TC-GS-IMPORT-E2E-185 | FE+BE |
| TC-GS-IMPORT-555 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-556 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-557 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-558 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-559 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-560 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-561 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-562 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-563 | TC-GS-IMPORT-E2E-019 | FE+BE |
| TC-GS-IMPORT-564 | TC-GS-IMPORT-E2E-023 | FE+BE |
| TC-GS-IMPORT-565 | TC-GS-IMPORT-E2E-033 | FE+BE |
| TC-GS-IMPORT-566 | TC-GS-IMPORT-E2E-043 | FE+BE |
| TC-GS-IMPORT-567 | TC-GS-IMPORT-E2E-087 | FE+BE |
| TC-GS-IMPORT-568 | TC-GS-IMPORT-E2E-087 | FE+BE |
| TC-GS-IMPORT-569 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-570 | TC-GS-IMPORT-E2E-098 | FE+BE |
| TC-GS-IMPORT-571 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-572 | TC-GS-IMPORT-E2E-133 | FE+BE |
| TC-GS-IMPORT-573 | TC-GS-IMPORT-E2E-136 | FE+BE |
| TC-GS-IMPORT-574 | TC-GS-IMPORT-E2E-176 | FE+BE |
| TC-GS-IMPORT-575 | TC-GS-IMPORT-E2E-185 | FE+BE |
| TC-GS-IMPORT-576 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-577 | TC-GS-IMPORT-E2E-172 | FE+BE |
| TC-GS-IMPORT-578 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-579 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-580 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-581 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-582 | TC-GS-IMPORT-E2E-021 | FE+BE |
| TC-GS-IMPORT-583 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-584 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-585 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-586 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-587 | TC-GS-IMPORT-E2E-006 | FE+BE |
| TC-GS-IMPORT-588 | TC-GS-IMPORT-E2E-006 | FE+BE |
| TC-GS-IMPORT-589 | TC-GS-IMPORT-E2E-006 | FE+BE |
| TC-GS-IMPORT-590 | TC-GS-IMPORT-E2E-005 | FE+BE |
| TC-GS-IMPORT-591 | TC-GS-IMPORT-E2E-007 | FE+BE |
| TC-GS-IMPORT-592 | TC-GS-IMPORT-E2E-007 | FE+BE |
| TC-GS-IMPORT-593 | TC-GS-IMPORT-E2E-005 | FE+BE |
| TC-GS-IMPORT-594 | TC-GS-IMPORT-E2E-065 | FE+BE |
| TC-GS-IMPORT-595 | TC-GS-IMPORT-E2E-008 | FE+BE |
| TC-GS-IMPORT-596 | TC-GS-IMPORT-E2E-008 | FE+BE |
| TC-GS-IMPORT-597 | TC-GS-IMPORT-E2E-009 | FE+BE |
| TC-GS-IMPORT-598 | TC-GS-IMPORT-E2E-010 | FE+BE |
| TC-GS-IMPORT-599 | TC-GS-IMPORT-E2E-010 | FE+BE |
| TC-GS-IMPORT-600 | TC-GS-IMPORT-E2E-010 | FE+BE |
| TC-GS-IMPORT-601 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-602 | TC-GS-IMPORT-E2E-045 | FE+BE |
| TC-GS-IMPORT-603 | TC-GS-IMPORT-E2E-045 | FE+BE |
| TC-GS-IMPORT-604 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-605 | TC-GS-IMPORT-E2E-046 | FE+BE |
| TC-GS-IMPORT-606 | TC-GS-IMPORT-E2E-044 | FE+BE |
| TC-GS-IMPORT-607 | TC-GS-IMPORT-E2E-055 | FE+BE |
| TC-GS-IMPORT-608 | TC-GS-IMPORT-E2E-059 | FE+BE |
| TC-GS-IMPORT-609 | TC-GS-IMPORT-E2E-059 | FE+BE |
| TC-GS-IMPORT-610 | TC-GS-IMPORT-E2E-047 | FE+BE |
| TC-GS-IMPORT-611 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-612 | TC-GS-IMPORT-E2E-028 | FE+BE |
| TC-GS-IMPORT-613 | TC-GS-IMPORT-E2E-032 | FE+BE |
| TC-GS-IMPORT-614 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-615 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-616 | TC-GS-IMPORT-E2E-029 | FE+BE |
| TC-GS-IMPORT-617 | TC-GS-IMPORT-E2E-031 | FE+BE |
| TC-GS-IMPORT-618 | TC-GS-IMPORT-E2E-033 | FE+BE |
| TC-GS-IMPORT-619 | TC-GS-IMPORT-E2E-033 | FE+BE |
| TC-GS-IMPORT-620 | TC-GS-IMPORT-E2E-033 | FE+BE |
| TC-GS-IMPORT-621 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-622 | TC-GS-IMPORT-E2E-031 | FE+BE |
| TC-GS-IMPORT-623 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-624 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-625 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-626 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-627 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-628 | TC-GS-IMPORT-E2E-039 | FE+BE |
| TC-GS-IMPORT-629 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-630 | TC-GS-IMPORT-E2E-040 | FE+BE |
| TC-GS-IMPORT-631 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-632 | TC-GS-IMPORT-E2E-041 | FE+BE |
| TC-GS-IMPORT-633 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-634 | TC-GS-IMPORT-E2E-042 | FE+BE |
| TC-GS-IMPORT-635 | TC-GS-IMPORT-E2E-035 | FE+BE |
| TC-GS-IMPORT-636 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-637 | TC-GS-IMPORT-E2E-036 | FE+BE |
| TC-GS-IMPORT-638 | TC-GS-IMPORT-E2E-038 | FE+BE |
| TC-GS-IMPORT-639 | TC-GS-IMPORT-E2E-038 | FE+BE |
| TC-GS-IMPORT-640 | TC-GS-IMPORT-E2E-038 | FE+BE |
| TC-GS-IMPORT-641 | TC-GS-IMPORT-E2E-038 | FE+BE |
| TC-GS-IMPORT-642 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-643 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-644 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-645 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-646 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-647 | TC-GS-IMPORT-E2E-087 | FE+BE |
| TC-GS-IMPORT-648 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-649 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-650 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-651 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-652 | TC-GS-IMPORT-E2E-092 | FE+BE |
| TC-GS-IMPORT-653 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-654 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-655 | TC-GS-IMPORT-E2E-093 | FE+BE |
| TC-GS-IMPORT-656 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-657 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-658 | TC-GS-IMPORT-E2E-096 | FE+BE |
| TC-GS-IMPORT-659 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-660 | TC-GS-IMPORT-E2E-098 | FE+BE |
| TC-GS-IMPORT-661 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-662 | TC-GS-IMPORT-E2E-098 | FE+BE |
| TC-GS-IMPORT-663 | TC-GS-IMPORT-E2E-098 | FE+BE |
| TC-GS-IMPORT-664 | TC-GS-IMPORT-E2E-090 | FE+BE |
| TC-GS-IMPORT-665 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-666 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-667 | TC-GS-IMPORT-E2E-066 | FE+BE |
| TC-GS-IMPORT-668 | TC-GS-IMPORT-E2E-076 | FE+BE |
| TC-GS-IMPORT-669 | TC-GS-IMPORT-E2E-080 | FE+BE |
| TC-GS-IMPORT-670 | TC-GS-IMPORT-E2E-079 | FE+BE |
| TC-GS-IMPORT-671 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-672 | TC-GS-IMPORT-E2E-095 | FE+BE |
| TC-GS-IMPORT-673 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-674 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-675 | TC-GS-IMPORT-E2E-095 | FE+BE |
| TC-GS-IMPORT-676 | TC-GS-IMPORT-E2E-102 | FE+BE |
| TC-GS-IMPORT-677 | TC-GS-IMPORT-E2E-066 | FE+BE |
| TC-GS-IMPORT-678 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-679 | TC-GS-IMPORT-E2E-068 | FE+BE |
| TC-GS-IMPORT-680 | TC-GS-IMPORT-E2E-068 | FE+BE |
| TC-GS-IMPORT-681 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-682 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-683 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-684 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-685 | TC-GS-IMPORT-E2E-067 | FE+BE |
| TC-GS-IMPORT-686 | TC-GS-IMPORT-E2E-108 | FE+BE |
| TC-GS-IMPORT-687 | TC-GS-IMPORT-E2E-110 | FE+BE |
| TC-GS-IMPORT-688 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-689 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-690 | TC-GS-IMPORT-E2E-109 | FE+BE |
| TC-GS-IMPORT-691 | TC-GS-IMPORT-E2E-111 | FE+BE |
| TC-GS-IMPORT-692 | TC-GS-IMPORT-E2E-077 | FE+BE |
| TC-GS-IMPORT-693 | TC-GS-IMPORT-E2E-113 | FE+BE |
| TC-GS-IMPORT-694 | TC-GS-IMPORT-E2E-113 | FE+BE |
| TC-GS-IMPORT-695 | TC-GS-IMPORT-E2E-114 | FE+BE |
| TC-GS-IMPORT-696 | TC-GS-IMPORT-E2E-111 | FE+BE |
| TC-GS-IMPORT-697 | TC-GS-IMPORT-E2E-115 | FE+BE |
| TC-GS-IMPORT-698 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-699 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-700 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-701 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-702 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-703 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-704 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-705 | TC-GS-IMPORT-E2E-157 | FE+BE |
| TC-GS-IMPORT-706 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-707 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-708 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-709 | TC-GS-IMPORT-E2E-119 | FE+BE |
| TC-GS-IMPORT-710 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-711 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-712 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-713 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-714 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-715 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-716 | TC-GS-IMPORT-E2E-120 | FE+BE |
| TC-GS-IMPORT-717 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-718 | TC-GS-IMPORT-E2E-124 | FE+BE |
| TC-GS-IMPORT-719 | TC-GS-IMPORT-E2E-165 | FE+BE |
| TC-GS-IMPORT-720 | TC-GS-IMPORT-E2E-151 | FE+BE |
| TC-GS-IMPORT-721 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-722 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-723 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-724 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-725 | TC-GS-IMPORT-E2E-126 | FE+BE |
| TC-GS-IMPORT-726 | TC-GS-IMPORT-E2E-126 | FE+BE |
| TC-GS-IMPORT-727 | TC-GS-IMPORT-E2E-126 | FE+BE |
| TC-GS-IMPORT-728 | TC-GS-IMPORT-E2E-153 | FE+BE |
| TC-GS-IMPORT-729 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-730 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-731 | TC-GS-IMPORT-E2E-157 | FE+BE |
| TC-GS-IMPORT-732 | TC-GS-IMPORT-E2E-157 | FE+BE |
| TC-GS-IMPORT-733 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-734 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-735 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-736 | TC-GS-IMPORT-E2E-152 | FE+BE |
| TC-GS-IMPORT-737 | TC-GS-IMPORT-E2E-162 | FE+BE |
| TC-GS-IMPORT-738 | TC-GS-IMPORT-E2E-138 | FE+BE |
| TC-GS-IMPORT-739 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-740 | TC-GS-IMPORT-E2E-147 | FE+BE |
| TC-GS-IMPORT-741 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-742 | TC-GS-IMPORT-E2E-154 | FE+BE |
| TC-GS-IMPORT-743 | TC-GS-IMPORT-E2E-154 | FE+BE |
| TC-GS-IMPORT-744 | TC-GS-IMPORT-E2E-154 | FE+BE |
| TC-GS-IMPORT-745 | TC-GS-IMPORT-E2E-153 | FE+BE |
| TC-GS-IMPORT-746 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-747 | TC-GS-IMPORT-E2E-157 | FE+BE |
| TC-GS-IMPORT-748 | TC-GS-IMPORT-E2E-155 | FE+BE |
| TC-GS-IMPORT-749 | TC-GS-IMPORT-E2E-158 | FE+BE |
| TC-GS-IMPORT-750 | TC-GS-IMPORT-E2E-164 | FE+BE |
| TC-GS-IMPORT-751 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-752 | TC-GS-IMPORT-E2E-140 | FE+BE |
| TC-GS-IMPORT-753 | TC-GS-IMPORT-E2E-183 | FE+BE |
| TC-GS-IMPORT-754 | TC-GS-IMPORT-E2E-183 | FE+BE |
| TC-GS-IMPORT-755 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-756 | TC-GS-IMPORT-E2E-203 | FE+BE |
| TC-GS-IMPORT-757 | TC-GS-IMPORT-E2E-200 | FE+BE |
| TC-GS-IMPORT-758 | TC-GS-IMPORT-E2E-058 | FE+BE |
| TC-GS-IMPORT-759 | TC-GS-IMPORT-E2E-020 | FE+BE |
| TC-GS-IMPORT-760 | TC-GS-IMPORT-E2E-020 | FE+BE |
| TC-GS-IMPORT-761 | TC-GS-IMPORT-E2E-170 | FE+BE |
| TC-GS-IMPORT-762 | TC-GS-IMPORT-E2E-168 | FE+BE |
| TC-GS-IMPORT-763 | TC-GS-IMPORT-E2E-178 | FE+BE |
| TC-GS-IMPORT-764 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-765 | TC-GS-IMPORT-E2E-188 | FE+BE |
| TC-GS-IMPORT-766 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-767 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-768 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-769 | TC-GS-IMPORT-E2E-192 | FE+BE |
| TC-GS-IMPORT-770 | TC-GS-IMPORT-E2E-191 | FE+BE |
| TC-GS-IMPORT-771 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-776 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-777 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-778 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-779 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-780 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-781 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-782 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-783 | TC-GS-IMPORT-E2E-196 | FE+BE |
| TC-GS-IMPORT-784 | TC-GS-IMPORT-E2E-197 | FE+BE |
| TC-GS-IMPORT-785 | TC-GS-IMPORT-E2E-197 | FE+BE |
| TC-GS-IMPORT-786 | TC-GS-IMPORT-E2E-197 | FE+BE |
| TC-GS-IMPORT-787 | TC-GS-IMPORT-E2E-197 | FE+BE |
| TC-GS-IMPORT-788 | TC-GS-IMPORT-E2E-198 | FE+BE |
| TC-GS-IMPORT-789 | TC-GS-IMPORT-E2E-198 | FE+BE |
| TC-GS-IMPORT-790 | TC-GS-IMPORT-E2E-198 | FE+BE |
| TC-GS-IMPORT-791 | TC-GS-IMPORT-E2E-180 | FE+BE |
| TC-GS-IMPORT-792 | TC-GS-IMPORT-E2E-180 | FE+BE |
| TC-GS-IMPORT-793 | TC-GS-IMPORT-E2E-174 | FE+BE |
| TC-GS-IMPORT-794 | TC-GS-IMPORT-E2E-174 | FE+BE |
| TC-GS-IMPORT-795 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-796 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-797 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-798 | TC-GS-IMPORT-E2E-199 | FE+BE |
| TC-GS-IMPORT-799 | TC-GS-IMPORT-E2E-195 | FE+BE |
| TC-GS-IMPORT-800 | TC-GS-IMPORT-E2E-200 | FE+BE |
| TC-GS-IMPORT-801 | TC-GS-IMPORT-E2E-214 | FE+BE |
| TC-GS-IMPORT-802 | TC-GS-IMPORT-E2E-214 | FE+BE |
| TC-GS-IMPORT-803 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-804 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-805 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-806 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-807 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-808 | TC-GS-IMPORT-E2E-215 | FE+BE |
| TC-GS-IMPORT-809 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-810 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-811 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-812 | TC-GS-IMPORT-E2E-056 | FE+BE |
| TC-GS-IMPORT-813 | TC-GS-IMPORT-E2E-057 | FE+BE |
| TC-GS-IMPORT-814 | TC-GS-IMPORT-E2E-172 | FE+BE |
| TC-GS-IMPORT-815 | TC-GS-IMPORT-E2E-023 | FE+BE |
| TC-GS-IMPORT-816 | TC-GS-IMPORT-E2E-060 | FE+BE |
| TC-GS-IMPORT-817 | TC-GS-IMPORT-E2E-061 | FE+BE |
| TC-GS-IMPORT-818 | TC-GS-IMPORT-E2E-185 | FE+BE |
| TC-GS-IMPORT-819 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-820 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-821 | TC-GS-IMPORT-E2E-074 | FE+BE |
| TC-GS-IMPORT-822 | TC-GS-IMPORT-E2E-158 | FE+BE |
| TC-GS-IMPORT-823 | TC-GS-IMPORT-E2E-054 | FE+BE |
| TC-GS-IMPORT-824 | TC-GS-IMPORT-E2E-136 | FE+BE |
| TC-GS-IMPORT-825 | TC-GS-IMPORT-E2E-118 | FE+BE |
| TC-GS-IMPORT-826 | TC-GS-IMPORT-E2E-120 | FE+BE |
| TC-GS-IMPORT-827 | TC-GS-IMPORT-E2E-120 | FE+BE |
| TC-GS-IMPORT-828 | TC-GS-IMPORT-E2E-082 | FE+BE |
| TC-GS-IMPORT-829 | TC-GS-IMPORT-E2E-048 | FE+BE |
| TC-GS-IMPORT-830 | TC-GS-IMPORT-E2E-156 | FE+BE |
| TC-GS-IMPORT-831 | TC-GS-IMPORT-E2E-156 | FE+BE |
| TC-GS-IMPORT-832 | TC-GS-IMPORT-E2E-156 | FE+BE |
| TC-GS-IMPORT-833 | TC-GS-IMPORT-E2E-135 | FE+BE |
| TC-GS-IMPORT-834 | TC-GS-IMPORT-E2E-135 | FE+BE |
| TC-GS-IMPORT-835 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-836 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-837 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-838 | TC-GS-IMPORT-E2E-085 | FE+BE |
| TC-GS-IMPORT-839 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-840 | TC-GS-IMPORT-E2E-159 | FE+BE |
| TC-GS-IMPORT-841 | TC-GS-IMPORT-E2E-173 | FE+BE |
| TC-GS-IMPORT-842 | TC-GS-IMPORT-E2E-094 | FE+BE |
| TC-GS-IMPORT-843 | TC-GS-IMPORT-E2E-146 | FE+BE |
| TC-GS-IMPORT-844 | TC-GS-IMPORT-E2E-146 | FE+BE |
| TC-GS-IMPORT-845 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-846 | TC-GS-IMPORT-E2E-150 | FE+BE |
| TC-GS-IMPORT-847 | TC-GS-IMPORT-E2E-161 | FE+BE |
| TC-GS-IMPORT-848 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-849 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-850 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-851 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-852 | TC-GS-IMPORT-E2E-117 | FE+BE |
| TC-GS-IMPORT-853 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-854 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-855 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-856 | TC-GS-IMPORT-E2E-084 | FE+BE |
| TC-GS-IMPORT-857 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-858 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-859 | TC-GS-IMPORT-E2E-023 | FE+BE |
| TC-GS-IMPORT-860 | TC-GS-IMPORT-E2E-157 | FE+BE |
| TC-GS-IMPORT-861 | TC-GS-IMPORT-E2E-089 | FE+BE |
| TC-GS-IMPORT-862 | TC-GS-IMPORT-E2E-089 | FE+BE |
| TC-GS-IMPORT-863 | TC-GS-IMPORT-E2E-089 | FE+BE |
| TC-GS-IMPORT-864 | TC-GS-IMPORT-E2E-089 | FE+BE |
| TC-GS-IMPORT-865 | TC-GS-IMPORT-E2E-125 | FE+BE |
| TC-GS-IMPORT-866 | TC-GS-IMPORT-E2E-116 | FE+BE |
| TC-GS-IMPORT-867 | TC-GS-IMPORT-E2E-023 | FE+BE |
| TC-GS-IMPORT-868@L738 | TC-GS-IMPORT-E2E-049 | FE+BE |
| TC-GS-IMPORT-868@L1077 | TC-GS-IMPORT-E2E-073 | FE+BE |
| TC-GS-IMPORT-869@L937 | TC-GS-IMPORT-E2E-083 | FE+BE |
| TC-GS-IMPORT-869@L1078 | TC-GS-IMPORT-E2E-077 | FE+BE |
| TC-GS-IMPORT-870@L1020 | TC-GS-IMPORT-E2E-087 | FE+BE |
| TC-GS-IMPORT-870@L1079 | TC-GS-IMPORT-E2E-073 | FE+BE |
| TC-GS-IMPORT-871@L938 | TC-GS-IMPORT-E2E-086 | FE+BE |
| TC-GS-IMPORT-871@L1080 | TC-GS-IMPORT-E2E-072 | FE+BE |
| TC-GS-IMPORT-872 | TC-GS-IMPORT-E2E-043 | FE+BE |
| TC-GS-IMPORT-873 | TC-GS-IMPORT-E2E-049 | FE+BE |
| TC-GS-IMPORT-874 | TC-GS-IMPORT-E2E-049 | FE+BE |
| TC-GS-IMPORT-875 | TC-GS-IMPORT-E2E-127 | FE+BE |
| TC-GS-IMPORT-876 | TC-GS-IMPORT-E2E-004 | FE+BE |
| TC-GS-IMPORT-877 | TC-GS-IMPORT-E2E-051 | FE+BE |
| TC-GS-IMPORT-878 | TC-GS-IMPORT-E2E-051 | FE+BE |
| TC-GS-IMPORT-879 | TC-GS-IMPORT-E2E-051 | FE+BE |
| TC-GS-IMPORT-880 | TC-GS-IMPORT-E2E-051 | FE+BE |
| TC-GS-IMPORT-881 | TC-GS-IMPORT-E2E-053 | FE+BE |
| TC-GS-IMPORT-882 | TC-GS-IMPORT-E2E-052 | FE+BE |
| TC-GS-IMPORT-883 | TC-GS-IMPORT-E2E-052 | FE+BE |
| TC-GS-IMPORT-884 | TC-GS-IMPORT-E2E-004 | FE+BE |
| TC-GS-IMPORT-885 | TC-GS-IMPORT-E2E-052 | FE+BE |
| TC-GS-IMPORT-886 | TC-GS-IMPORT-E2E-014 | FE+BE |
| TC-GS-IMPORT-887 | TC-GS-IMPORT-E2E-014 | FE+BE |
| TC-GS-IMPORT-888 | TC-GS-IMPORT-E2E-014 | FE+BE |
| TC-GS-IMPORT-889 | TC-GS-IMPORT-E2E-013 | FE+BE |
| TC-GS-IMPORT-890 | TC-GS-IMPORT-E2E-189 | FE+BE |
| TC-GS-IMPORT-891 | TC-GS-IMPORT-E2E-099 | FE+BE |
| TC-GS-IMPORT-892 | TC-GS-IMPORT-E2E-030 | FE+BE |
| TC-GS-IMPORT-893 | TC-GS-IMPORT-E2E-099 | FE+BE |
| TC-GS-IMPORT-894 | TC-GS-IMPORT-E2E-104 | FE+BE |
| TC-GS-IMPORT-895 | TC-GS-IMPORT-E2E-099 | FE+BE |
| TC-GS-IMPORT-896 | TC-GS-IMPORT-E2E-104 | FE+BE |
| TC-GS-IMPORT-897 | TC-GS-IMPORT-E2E-099 | FE+BE |
| TC-GS-IMPORT-898 | TC-GS-IMPORT-E2E-101 | FE+BE |
| TC-GS-IMPORT-899 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-900 | TC-GS-IMPORT-E2E-100 | FE+BE |
| TC-GS-IMPORT-901 | TC-GS-IMPORT-E2E-100 | FE+BE |
| TC-GS-IMPORT-902 | TC-GS-IMPORT-E2E-100 | FE+BE |
| TC-GS-IMPORT-903 | TC-GS-IMPORT-E2E-100 | FE+BE |
| TC-GS-IMPORT-904 | TC-GS-IMPORT-E2E-104 | FE+BE |
| TC-GS-IMPORT-905 | TC-GS-IMPORT-E2E-104 | FE+BE |
| TC-GS-IMPORT-906 | TC-GS-IMPORT-E2E-104 | FE+BE |
| TC-GS-IMPORT-907 | TC-GS-IMPORT-E2E-103 | FE+BE |
| TC-GS-IMPORT-908 | TC-GS-IMPORT-E2E-099 | FE+BE |
| TC-GS-IMPORT-909 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-910 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-911 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-912 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-913 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-914 | TC-GS-IMPORT-E2E-130 | FE+BE |
| TC-GS-IMPORT-915 | TC-GS-IMPORT-E2E-130 | FE+BE |
| TC-GS-IMPORT-916 | TC-GS-IMPORT-E2E-130 | FE+BE |
| TC-GS-IMPORT-917 | TC-GS-IMPORT-E2E-130 | FE+BE |
| TC-GS-IMPORT-918 | TC-GS-IMPORT-E2E-145 | FE+BE |
| TC-GS-IMPORT-919 | TC-GS-IMPORT-E2E-126 | FE+BE |
| TC-GS-IMPORT-920 | TC-GS-IMPORT-E2E-132 | FE+BE |
| TC-GS-IMPORT-921 | TC-GS-IMPORT-E2E-131 | FE+BE |
| TC-GS-IMPORT-922 | TC-GS-IMPORT-E2E-128 | FE+BE |
| TC-GS-IMPORT-923 | TC-GS-IMPORT-E2E-169 | FE+BE |
| TC-GS-IMPORT-924 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-925 | TC-GS-IMPORT-E2E-122 | FE+BE |
| TC-GS-IMPORT-926 | TC-GS-IMPORT-E2E-129 | FE+BE |
| TC-GS-IMPORT-927 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-928 | TC-GS-IMPORT-E2E-148 | FE+BE |
| TC-GS-IMPORT-929 | TC-GS-IMPORT-E2E-130 | FE+BE |
| TC-GS-IMPORT-930 | TC-GS-IMPORT-E2E-137 | FE+BE |
| TC-GS-IMPORT-931 | TC-GS-IMPORT-E2E-171 | FE+BE |
| TC-GS-IMPORT-932 | TC-GS-IMPORT-E2E-060 | FE+BE |
| TC-GS-IMPORT-933 | TC-GS-IMPORT-E2E-121 | FE+BE |
| TC-GS-IMPORT-934 | TC-GS-IMPORT-E2E-211 | FE+BE |
| TC-GS-IMPORT-935 | TC-GS-IMPORT-E2E-186 | FE+BE |
| TC-GS-IMPORT-936 | TC-GS-IMPORT-E2E-212 | FE+BE |
| TC-GS-IMPORT-937 | TC-GS-IMPORT-E2E-212 | FE+BE |
| TC-GS-IMPORT-938 | TC-GS-IMPORT-E2E-212 | FE+BE |
| TC-GS-IMPORT-939 | TC-GS-IMPORT-E2E-207 | FE+BE |
| TC-GS-IMPORT-940 | TC-GS-IMPORT-E2E-207 | FE+BE |
| TC-GS-IMPORT-941 | TC-GS-IMPORT-E2E-206 | FE+BE |
| TC-GS-IMPORT-942 | TC-GS-IMPORT-E2E-206 | FE+BE |
| TC-GS-IMPORT-943 | TC-GS-IMPORT-E2E-206 | FE+BE |
| TC-GS-IMPORT-944 | TC-GS-IMPORT-E2E-213 | FE+BE |
| TC-GS-IMPORT-945 | TC-GS-IMPORT-E2E-210 | FE+BE |
| TC-GS-IMPORT-946 | TC-GS-IMPORT-E2E-176 | FE+BE |
| TC-GS-IMPORT-947 | TC-GS-IMPORT-E2E-177 | FE+BE |
| TC-GS-IMPORT-948 | TC-GS-IMPORT-E2E-028 | FE+BE |
| TC-GS-IMPORT-949 | TC-GS-IMPORT-E2E-205 | FE+BE |
| TC-GS-IMPORT-950 | TC-GS-IMPORT-E2E-208 | FE+BE |
| TC-GS-IMPORT-951 | TC-GS-IMPORT-E2E-208 | FE+BE |
| TC-GS-IMPORT-952 | TC-GS-IMPORT-E2E-207 | FE+BE |
| TC-GS-IMPORT-953 | TC-GS-IMPORT-E2E-207 | FE+BE |
| TC-GS-IMPORT-954 | TC-GS-IMPORT-E2E-214 | FE+BE |
| TC-GS-IMPORT-955 | TC-GS-IMPORT-E2E-209 | FE+BE |
| TC-GS-IMPORT-956 | TC-GS-IMPORT-E2E-209 | FE+BE |
| TC-GS-IMPORT-957 | TC-GS-IMPORT-E2E-209 | FE+BE |
| TC-GS-IMPORT-958 | TC-GS-IMPORT-E2E-210 | FE+BE |
| TC-GS-IMPORT-959 | TC-GS-IMPORT-E2E-180 | FE+BE |
| TC-GS-IMPORT-960 | TC-GS-IMPORT-E2E-208 | FE+BE |
| TC-GS-IMPORT-961 | TC-GS-IMPORT-E2E-209 | FE+BE |
| TC-GS-IMPORT-962 | TC-GS-IMPORT-E2E-209 | FE+BE |
| TC-GS-IMPORT-963 | TC-GS-IMPORT-E2E-211 | FE+BE |
| TC-GS-IMPORT-964 | TC-GS-IMPORT-E2E-101 | FE+BE |
| TC-GS-IMPORT-965 | TC-GS-IMPORT-E2E-101 | FE+BE |
| TC-GS-IMPORT-966 | TC-GS-IMPORT-E2E-101 | FE+BE |
| TC-GS-IMPORT-967 | TC-GS-IMPORT-E2E-102 | FE+BE |
| TC-GS-IMPORT-968 | TC-GS-IMPORT-E2E-102 | FE+BE |
| TC-GS-IMPORT-969 | TC-GS-IMPORT-E2E-081 | FE+BE |
| TC-GS-IMPORT-970 | TC-GS-IMPORT-E2E-100 | FE+BE |
| TC-GS-IMPORT-971 | TC-GS-IMPORT-E2E-105 | FE+BE |
