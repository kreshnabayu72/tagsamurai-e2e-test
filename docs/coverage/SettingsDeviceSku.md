# Coverage E2E — Admin Console > Settings > Device SKU

Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md` (606 ID `TC-AC-DS-1`–`606`, semua aktif). Suite: `specs/AdminConsole/SettingsDeviceSku/`. Prefix: `AC` + `DS` (`TC-AC-DS-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). `tc-settings-device-sku-backend.md` dipakai hanya untuk mengenali TC hanya-BE (hasil: tidak ada).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 606 TC aktif masuk 193 spec (183 nomor rencana ditambah 10 nomor cadangan: 186–195), 0 TC hanya-BE. Setiap TC terpetakan ke tepat satu spec (tidak ada TC yang terbelah lintas spec). Seluruh spec bermode FE+BE: kegagalan 5xx, timeout, dan upload gagal dipicu `Spectra.intercept()` di atas backend nyata. Spec 014 (TC-49–51, aplikasi native Android) memakai `coverage.mobile: automated`; spec lain `coverage.web: automated`.

## TC hanya-BE (tidak masuk spec)

Tidak ada. TC kelas a yang Expected-nya berupa respons API (TC 233–236, 238, 309, 494, 512–531, 583, 584, 589, 603–605) tetap masuk spec FE+BE dengan butir Notes `K-1`.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-DS-E2E-001-screening-halaman-list-dasar | Screening Halaman Device SKU List: Breadcrumb, Sub-tab, Hover SKU, dan Header Tabel | FE+BE | 32 | 1, 2, 4, 6 |
| TC-AC-DS-E2E-002-list-tooltip-klik-sku-dan-menu-aksi-keyboard | List: Tooltip Toolbar, Klik Kolom SKU Membuka Popup Detail, dan Menu Aksi Baris lewat Keyboard | FE+BE | 31 | 3, 5, 570 |
| TC-AC-DS-E2E-003-isi-kolom-baris-handheld-reader-dan-smart-fixed-reader | Isi Kolom Baris SKU Handheld Reader (Stok Lebih dari 0 dan Stok 0) dan Smart Fixed Reader | FE+BE | 26 | 7, 8, 9 |
| TC-AC-DS-E2E-004-isi-kolom-baris-ble-gateway-dan-tag | Isi Kolom Baris SKU BLE Gateway dan TAG (User TAG dan Object) | FE+BE | 25 | 10, 11, 12 |
| TC-AC-DS-E2E-005-isi-kolom-foto-stok-dan-kolom-curated | Isi Kolom Photo, Current Stock, serta Kolom Curated Hardware Type, Range Type, dan TAG Type | FE+BE | 41 | 13, 14, 15, 16, 17 |
| TC-AC-DS-E2E-006-badge-category-brand-model-dan-lebar-teks | Badge Category, Brand, dan Model/Type: Teks Penuh, Pemotongan di Atas 25 Karakter, serta Device Name dan SKU Panjang | FE+BE | 19 | 18, 19, 20, 21, 22, 23, 24, 25 |
| TC-AC-DS-E2E-007-last-modified-format-dan-tidak-berubah | Last Modified: Format Date dan Time Format General Settings, Edit Tanpa Perubahan, dan Perubahan Stok | FE+BE | 20 | 26, 27, 28 |
| TC-AC-DS-E2E-008-state-list-loading-empty-no-result-stok-nol | State List: Loading, Empty State Principal Tanpa SKU, No Result, dan SKU Stok 0 Tetap Tampil | FE+BE | 26 | 29, 30, 31, 33 |
| TC-AC-DS-E2E-009-sidebar-category-screening-dan-pilih-node | Sidebar Category: Screening, Pilih Node Induk dan Daun, Tanpa Pilihan, serta Daun Tingkat ke-4 | FE+BE | 38 | 36, 37, 38, 41, 576 |
| TC-AC-DS-E2E-010-sidebar-category-multi-select-partial-dan-filter-and | Sidebar Category: Multi-select, Parent Partial dan Full Check, serta Gabungan dengan Filter Hardware Type | FE+BE | 26 | 39, 40, 575 |
| TC-AC-DS-E2E-011-sidebar-category-pencarian-expand-collapse-toggle-dan-label-panjang | Sidebar Category: Pencarian Pohon, Expand/Collapse All, Toggle Floating, dan Label Node Panjang | FE+BE | 41 | 42, 43, 44, 557, 558 |
| TC-AC-DS-E2E-012-sidebar-category-responsif-dan-state-lintas-sub-tab | Sidebar Category: Penutupan Otomatis di Bawah 1280 px dan Pilihan serta Search/Filter Lintas Sub-tab | FE+BE | 25 | 45, 47, 48 |
| TC-AC-DS-E2E-013-sidebar-category-node-kosong-setelah-delete-dan-register | Sidebar Category: Node Terpilih Menjadi Kosong setelah Delete dan Kembali Terisi setelah Register | FE+BE | 24 | 600, 601 |
| TC-AC-DS-E2E-014-mobile-selection-mode-dan-floating-bulk-bar | Tampilan Mobile: Long-press Masuk Selection Mode, Floating Bulk Bar, dan Batal Seleksi | FE+BE | 28 | 49, 50, 51 |
| TC-AC-DS-E2E-015-role-matrix-akses-menu-positif | Role Matrix Positif: Principal, Distributor, dan Read Only Melihat Menu Device SKU dan Membuka Halaman | FE+BE | 32 | 52, 53, 59 |
| TC-AC-DS-E2E-016-role-matrix-negatif-entity-gate-partner | Role Matrix Negatif: Partner Tidak Melihat Menu Device dan Akses URL Langsung Ditolak 403 | FE+BE | 9 | 54, 55 |
| TC-AC-DS-E2E-017-role-matrix-negatif-tanpa-capability-dan-group-manager | Role Matrix Negatif: Principal Tanpa Capability dan Group Manager Tidak Melihat Menu serta URL Langsung Ditolak | FE+BE | 14 | 56, 57, 58 |
| TC-AC-DS-E2E-018-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Halaman Device SKU per Role Principal dan Distributor | FE+BE | 140 | 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 |
| TC-AC-DS-E2E-019-role-matrix-positif-register-sku | Role Matrix Positif: Create-Only Principal dan Distributor Menyelesaikan Register SKU | FE+BE | 31 | 70, 74 |
| TC-AC-DS-E2E-020-role-matrix-positif-edit-sku | Role Matrix Positif: Update-Only Principal dan Distributor Menyelesaikan Edit SKU | FE+BE | 18 | 71, 75 |
| TC-AC-DS-E2E-021-role-matrix-positif-delete-sku | Role Matrix Positif: Delete-Only Principal dan Distributor Menyelesaikan Delete Single dan Bulk Delete | FE+BE | 29 | 72, 73, 76 |
| TC-AC-DS-E2E-022-scope-baris-principal-tidak-melihat-sku-distributor | Scope Baris Principal: Tidak Melihat SKU Distributor dan Tanpa Tombol Aksi untuk SKU Distributor | FE+BE | 18 | 77, 86 |
| TC-AC-DS-E2E-023-scope-baris-distributor-sku-principal-read-only | Scope Baris Distributor: SKU Principal Read-only, Isolasi Antar Distributor, Detail, dan Pohon Category | FE+BE | 36 | 34, 46, 78, 79 |
| TC-AC-DS-E2E-024-distributor-kontrol-baris-sku-principal-disabled | Distributor: Aksi Delete Hilang dan Checkbox Disabled pada Baris SKU Principal | FE+BE | 25 | 80, 81 |
| TC-AC-DS-E2E-025-local-registration-tombol-tambah-sku-distributor | Local Registration: Tombol [+ SKU] Distributor Tampil Saat Aktif dan Tersembunyi Saat Nonaktif | FE+BE | 5 | 83, 84 |
| TC-AC-DS-E2E-026-local-registration-nonaktif-edit-dan-delete-sku-lokal | Local Registration Nonaktif: Edit, Delete, dan Bulk Delete SKU Lokal Tetap Berjalan | FE+BE | 20 | 85, 596 |
| TC-AC-DS-E2E-027-register-screening-popup-dan-picker-category | Register SKU: Screening Popup, Screening Picker Category, dan Klik Root Non-selectable | FE+BE | 28 | 87, 88, 89 |
| TC-AC-DS-E2E-028-register-picker-category-pilihan-tertunda-dan-pencarian | Register SKU: Pilihan Node Category, Pilihan Tertunda sampai Select, Pencarian Picker, dan Section Kondisional | FE+BE | 30 | 90, 91, 92, 93 |
| TC-AC-DS-E2E-029-register-category-device-name-opsi-dan-cascade | Register SKU: Opsi Device Name Mengikuti Category, Pilih Device Name Mengisi Category, dan No options available | FE+BE | 44 | 94, 95, 96, 97, 594 |
| TC-AC-DS-E2E-030-register-ganti-category-membuang-nilai-kondisional | Register SKU: Mengganti Category Mereset Device Name dan Membuang Nilai Kondisional (Range Type, Port, User TAG) | FE+BE | 37 | 98, 580, 581 |
| TC-AC-DS-E2E-031-register-dropdown-brand-dan-suggestion-model-principal | Register SKU Principal: Dropdown Brand, Suggestion Model/Type, dan Model/Type Bebas | FE+BE | 22 | 99, 101, 103 |
| TC-AC-DS-E2E-032-register-field-kondisional-per-ancestry-category | Register SKU: Field Kondisional per Ancestry Category (Range Type, Port, User TAG, BLE Gateway) | FE+BE | 28 | 104, 105, 106, 107, 108 |
| TC-AC-DS-E2E-033-register-sku-format-karakter-paste-dan-batas-120 | Register SKU: Field SKU Huruf Besar Otomatis, Blokir Karakter Invalid, Paste, dan Batas 120 Karakter | FE+BE | 30 | 109, 110, 111, 112, 113 |
| TC-AC-DS-E2E-034-register-sku-121-karakter-kosong-dan-category-kosong | Register SKU: SKU 121 Karakter, SKU Kosong, dan Category Kosong Diblokir | FE+BE | 27 | 114, 115, 129 |
| TC-AC-DS-E2E-035-register-duplikat-kode-sku-dan-daftar-ulang | Register SKU: Kode Duplikat Principal, Helper Text Kembali, Case-insensitive, dan Daftar Ulang Kode Terhapus | FE+BE | 39 | 116, 117, 118, 122 |
| TC-AC-DS-E2E-036-register-model-type-kosong-dan-batas-120 | Register SKU: Model/Type Kosong, Tepat 120 Karakter, dan 121 Karakter | FE+BE | 20 | 123, 124, 125 |
| TC-AC-DS-E2E-037-register-model-type-trim-emoji-dan-kapitalisasi | Register SKU: Model/Type Trim Spasi, Emoji Diblok, dan Pembeda Huruf Besar-Kecil | FE+BE | 37 | 126, 127, 128 |
| TC-AC-DS-E2E-038-register-device-name-brand-kosong-dan-form-kosong | Register SKU: Device Name Kosong, Brand Kosong, dan Submit Form Kosong | FE+BE | 32 | 130, 131, 132 |
| TC-AC-DS-E2E-039-register-foto-unggah-ganti-default-dan-hapus | Register SKU: Foto Unggah Satu dan Dua, Ganti Default, dan Hapus Foto Default | FE+BE | 22 | 133, 134, 135, 140 |
| TC-AC-DS-E2E-040-register-foto-batas-dua-format-dan-resize | Register SKU: Foto Batas Maksimum 2, Format File Picker, dan Resize di Atas 1 MB | FE+BE | 27 | 136, 137, 138 |
| TC-AC-DS-E2E-041-register-foto-wajib-dan-aria-error | Register SKU: Foto Wajib Diisi, Hapus Semua Foto, dan Aria Error Foto | FE+BE | 28 | 139, 141, 145 |
| TC-AC-DS-E2E-042-register-range-type-port-wajib-dan-batas-bawah | Register SKU: Range Type Wajib, Port Wajib, dan Port 0 Diblokir | FE+BE | 36 | 146, 147, 148 |
| TC-AC-DS-E2E-043-register-port-batas-minimum-maksimum-dan-digit | Register SKU: Port Batas 1 dan 65535, 65536 Diblokir, dan Hanya Digit | FE+BE | 31 | 149, 150, 151 |
| TC-AC-DS-E2E-044-register-user-tag-menentukan-tag-type-dan-default-stay | Register SKU: Checkbox This is User TAG Menentukan TAG Type dan Default Checkbox Stay on this form | FE+BE | 23 | 152, 153 |
| TC-AC-DS-E2E-045-register-stay-on-form-dua-sku-berturut-turut | Register SKU: Register Berturut-turut dengan Stay on this form Menghasilkan Dua SKU | FE+BE | 26 | 161 |
| TC-AC-DS-E2E-046-register-sukses-handheld-reader-dan-smart-fixed-reader | Register SKU Berhasil: Handheld Reader (Long Range) dan Smart Fixed Reader (Port 8080) | FE+BE | 41 | 154, 155 |
| TC-AC-DS-E2E-047-register-sukses-ble-gateway-dan-tag-user | Register SKU Berhasil: BLE Gateway dan TAG dengan This is User TAG | FE+BE | 40 | 156, 157 |
| TC-AC-DS-E2E-048-register-sukses-dua-foto-default-kedua-dan-foto-permanen | Register SKU Berhasil: Dua Foto dengan Foto Kedua sebagai Default dan Foto Menjadi Permanen Setelah Submit | FE+BE | 33 | 144, 158 |
| TC-AC-DS-E2E-049-register-saving-state-dan-klik-ganda-submit | Register SKU: Saving State selama Request dan Klik Ganda Cepat pada Submit | FE+BE | 29 | 162, 163 |
| TC-AC-DS-E2E-050-register-clear-field | Register SKU: Clear Field Mengosongkan Semua Field, Menghapus Pesan Error, dan Tidak Menutup Popup | FE+BE | 29 | 164, 165 |
| TC-AC-DS-E2E-051-register-penutupan-popup-ikon-esc-dan-unsaved | Register SKU: Penutupan Popup Kosong dan Terisi, Esc, dan Dialog Unsaved Changes | FE+BE | 33 | 166, 167, 168 |
| TC-AC-DS-E2E-052-register-refresh-route-dan-leave-cancel | Register SKU: Refresh Browser, Berpindah Route, Leave, dan Guard Dilepas Setelah Submit Sukses | FE+BE | 41 | 171, 172, 173, 572 |
| TC-AC-DS-E2E-053-aksesibilitas-popup-register-dan-edit | Aksesibilitas Popup Register dan Edit: Focus Trap, Esc, dan Atribut Aria | FE+BE | 21 | 174, 254 |
| TC-AC-DS-E2E-054-register-referensi-stale-category-device-name-brand | Register SKU: Referensi Category, Device Name, dan Brand Dihapus Pelaku Lain sebelum Submit | FE+BE | 42 | 177, 178, 179 |
| TC-AC-DS-E2E-055-register-distributor-brand-suggestion-dan-sku-lokal | Register SKU Distributor: Dropdown Brand, Suggestion Model/Type, dan Register SKU Lokal | FE+BE | 30 | 100, 102, 159 |
| TC-AC-DS-E2E-056-register-keunikan-kode-sku-lintas-scope | Register SKU: Keunikan Kode SKU Lintas Scope Principal dan Distributor | FE+BE | 35 | 119, 120, 121 |
| TC-AC-DS-E2E-057-edit-screening-popup-dan-field-stok-nol | Edit SKU: Screening Popup, Category Read-only, Stok 0 Semua Field Editable, dan Device Name Read-only Stok Berisi | FE+BE | 35 | 181, 182, 183, 187, 188 |
| TC-AC-DS-E2E-058-edit-field-terkunci-saat-stok-lebih-dari-nol | Edit SKU: Field SKU, Range Type, dan User TAG Terkunci saat Stok Lebih dari 0 serta Terbuka Kembali saat Stok Kosong | FE+BE | 30 | 184, 185, 186, 239 |
| TC-AC-DS-E2E-059-edit-opsi-device-name-brand-dan-suggestion | Edit SKU: Opsi Device Name Dibatasi Category, Dropdown Brand, dan Suggestion Model/Type | FE+BE | 20 | 189, 190, 191, 606 |
| TC-AC-DS-E2E-060-edit-distributor-brand-suggestion-dan-duplikat-principal | Edit SKU oleh Distributor: Dropdown Brand, Suggestion Model/Type, dan Kode Duplikat SKU Principal | FE+BE | 27 | 219, 582 |
| TC-AC-DS-E2E-061-edit-validasi-kosong-model-sku-foto-dan-clear-field | Edit SKU: Validasi Model/Type, SKU, Foto Kosong, dan Clear Field Lalu Save | FE+BE | 31 | 209, 210, 211, 212 |
| TC-AC-DS-E2E-062-edit-validasi-batas-120-model-type-dan-sku | Edit SKU: Model/Type dan SKU Batas 120 dan 121 Karakter | FE+BE | 25 | 213, 214, 215, 216 |
| TC-AC-DS-E2E-063-edit-validasi-duplikat-format-sku-trim-dan-emoji | Edit SKU: Duplikat SKU, SKU Sendiri, Format SKU, Trim Model/Type, dan Emoji | FE+BE | 30 | 217, 218, 220, 221, 222 |
| TC-AC-DS-E2E-064-edit-validasi-port | Edit SKU: Validasi Port Kosong, 0, 65536, 65535, dan Hanya Digit | FE+BE | 26 | 223, 224, 225 |
| TC-AC-DS-E2E-065-edit-validasi-foto | Edit SKU: Validasi Foto Batas Dua, Resize di Atas 1 MB, dan Format File Picker | FE+BE | 16 | 226, 227, 228 |
| TC-AC-DS-E2E-066-edit-sukses-model-brand-device-name-dan-sku | Edit SKU Berhasil: Model/Type, Brand, Device Name, dan Kode SKU | FE+BE | 27 | 192, 193, 194, 195 |
| TC-AC-DS-E2E-067-edit-sukses-range-type-port-user-tag-dan-tiga-field | Edit SKU Berhasil: Range Type, Port pada Stok 0 dan Stok Berisi, serta User TAG | FE+BE | 33 | 196, 197, 198, 199 |
| TC-AC-DS-E2E-068-edit-foto-ganti-tambah-hapus-dan-default | Edit SKU Berhasil: Tiga Field Sekaligus, Ganti Foto Default, dan Tambah Foto Kedua | FE+BE | 31 | 200, 201, 202 |
| TC-AC-DS-E2E-069-edit-foto-tanda-default-dan-hapus-default | Edit SKU Berhasil: Hapus Foto Bukan Default, Ganti Tanda Default, dan Hapus Foto Default Menaikkan Foto Tersisa | FE+BE | 28 | 203, 204, 205 |
| TC-AC-DS-E2E-070-edit-nilai-dikembalikan-dan-kapitalisasi | Edit SKU: Mengubah Lalu Mengembalikan Nilai Dianggap Tanpa Perubahan dan Perubahan Kapitalisasi Dicatat | FE+BE | 23 | 207, 208 |
| TC-AC-DS-E2E-071-edit-clear-field-saving-state-dan-klik-ganda | Edit SKU: Clear Field (Stok Berisi dan Stok 0) dan Reset Validasi | FE+BE | 40 | 240, 241, 242 |
| TC-AC-DS-E2E-072-edit-penutupan-popup-ikon-esc-backdrop-dan-unsaved | Edit SKU: Penutupan Popup Tanpa Perubahan dan Setelah Perubahan, Esc, Backdrop, dan Dialog Unsaved Changes | FE+BE | 47 | 243, 244, 245, 246, 247 |
| TC-AC-DS-E2E-073-edit-refresh-route-dan-cancel-leave | Edit SKU: Refresh Browser, Berpindah Route, dan Cancel pada Dialog Unsaved Changes | FE+BE | 27 | 248, 249, 573 |
| TC-AC-DS-E2E-074-edit-referensi-stale-dan-stok-masuk-setelah-form-terbuka | Edit SKU: Device Name dan Brand Dihapus Pelaku Lain serta Stok Masuk setelah Form Terbuka | FE+BE | 35 | 231, 232, 237 |
| TC-AC-DS-E2E-075-delete-single-dialog-konfirmasi-cancel-esc-backdrop | Delete SKU Single: Dialog Konfirmasi, Cancel, Esc, dan Klik Backdrop | FE+BE | 31 | 255, 257, 258, 259 |
| TC-AC-DS-E2E-076-delete-single-dialog-blok-sku-berstok | Delete SKU Single pada SKU Berstok: Dialog Blok, OK, Esc, Backdrop, dan Stok Masuk setelah Dialog Tampil | FE+BE | 32 | 260, 261, 262, 263 |
| TC-AC-DS-E2E-077-delete-single-kuota-alokasi-dan-distributor | Delete SKU: Kuota Alokasi Category, Stok Dipegang Client, serta Distributor Stok 0 dan Berstok | FE+BE | 27 | 264, 265, 266, 267 |
| TC-AC-DS-E2E-078-delete-single-berhasil-klik-ganda-dan-riwayat-transaksi | Delete SKU Single Berhasil: Klik Ganda Satu Penghapusan dan Riwayat Transaksi Tetap Terbaca | FE+BE | 31 | 256, 270, 271 |
| TC-AC-DS-E2E-079-bulk-delete-bar-counter-dan-checkbox-header | Bulk Action Bar: Screening, Counter Realtime, Checkbox Header, dan Indeterminate | FE+BE | 25 | 272, 273, 274 |
| TC-AC-DS-E2E-080-bulk-delete-select-all-unselect-all-dan-retensi-seleksi | Bulk Action Bar: Select All Lintas Halaman, Unselect All, dan Seleksi Dipertahankan | FE+BE | 30 | 275, 276, 280 |
| TC-AC-DS-E2E-081-bulk-delete-homogen-dialog-cancel-esc-dan-berhasil | Bulk Delete Homogen: Dialog dengan Daftar Scroll, Cancel, Esc, Klik Ganda, dan Berhasil | FE+BE | 37 | 281, 282, 283, 284, 297 |
| TC-AC-DS-E2E-082-bulk-delete-campuran-dialog-dua-kelompok-dan-continue | Bulk Delete Campuran: Dialog Dua Kelompok, Cancel, Esc, dan Continue Melewati SKU Berstok | FE+BE | 29 | 286, 287, 288, 555 |
| TC-AC-DS-E2E-083-bulk-delete-full-block-dan-satu-sku-terpilih | Bulk Delete Full-block dan Satu SKU Terpilih: Dialog Blok, OK, Esc, dan Dialog Single | FE+BE | 36 | 285, 289, 290, 291, 556 |
| TC-AC-DS-E2E-084-bulk-delete-preview-berubah-sebelum-confirm | Bulk Delete: Seluruh SKU Terpilih Menjadi Berstok sebelum Confirm Menampilkan Dialog Blok Tanpa Toast | FE+BE | 22 | 292 |
| TC-AC-DS-E2E-085-sku-dihapus-pelaku-lain-sebelum-save-confirm-dan-bulk | SKU Dihapus Pelaku Lain sebelum Save, Confirm Delete, dan Bulk Delete (Sebagian) | FE+BE | 33 | 544, 545, 546 |
| TC-AC-DS-E2E-086-bulk-delete-seluruh-terpilih-dihapus-pelaku-lain | Bulk Delete: Seluruh SKU Terpilih Dihapus Pelaku Lain dan Satu Terhapus Sisanya Berstok | FE+BE | 37 | 547, 574 |
| TC-AC-DS-E2E-087-search-list-kelas-teks-badge-angka-dan-curated | Search List: Pencocokan per Kelas Teks, Badge, Angka, dan Kolom Curated | FE+BE | 30 | 298, 299, 300, 301 |
| TC-AC-DS-E2E-088-search-list-kolom-hidden-tanggal-photo-trim-dan-reset-paginasi | Search List: Kolom Hidden, Kolom Tanggal dan Photo Tidak Dapat Dicari, Trim Spasi, dan Reset Paginasi | FE+BE | 29 | 302, 303, 304, 308, 310 |
| TC-AC-DS-E2E-089-search-list-siklus-interaksi-case-dan-substring | Search List: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, dan Substring | FE+BE | 31 | 305, 306, 307 |
| TC-AC-DS-E2E-090-filter-list-screening-opsi-pencarian-dropdown-dan-tutup-tanpa-apply | Filter List: Screening Panel, Isi Opsi Dropdown, Pencarian di Dalam Dropdown, dan Tutup Tanpa Apply | FE+BE | 35 | 311, 312, 313, 322 |
| TC-AC-DS-E2E-091-filter-list-multi-select-searchable-dan-logika-or-and | Filter List: Kelas Multi-select Searchable, Logika OR antar Opsi, dan AND antar Field | FE+BE | 17 | 314, 315, 316 |
| TC-AC-DS-E2E-092-filter-list-chip-dan-rentang-current-stock | Filter List: Penghapusan Chip, Overflow +N more, dan Rentang Current Stock Inklusif | FE+BE | 31 | 317, 318, 319, 320 |
| TC-AC-DS-E2E-093-filter-list-last-modified-indikator-dan-clear-field | Filter List: Rentang Last Modified Inklusif, Indikator Titik, dan Clear Field | FE+BE | 24 | 321, 323, 324 |
| TC-AC-DS-E2E-094-filter-list-kolom-hidden-reset-paginasi-dan-data-berubah | Filter List: Kolom Hidden, Reset Paginasi, serta Register dan Edit saat Filter atau Search Aktif | FE+BE | 31 | 325, 326, 333, 334 |
| TC-AC-DS-E2E-095-filter-list-opsi-live-loading-dan-tanpa-sku | Filter List: Opsi Ter-update setelah Register, State Loading Dropdown, dan No options available | FE+BE | 27 | 591, 592, 593 |
| TC-AC-DS-E2E-096-kombinasi-search-filter-sort-pagination-list-bagian-1 | Kombinasi List: Search Lalu Filter, Filter Lalu Search, dan Kombinasi Penuh dengan Sort dan Pagination | FE+BE | 23 | 327, 328, 329 |
| TC-AC-DS-E2E-097-kombinasi-search-filter-sort-pagination-list-bagian-2 | Kombinasi List: Melepas Search, Ganti Sort, serta Tanpa Hasil Lalu Pulih | FE+BE | 26 | 330, 331, 332 |
| TC-AC-DS-E2E-098-sort-list-alfabetis-tiga-tahap-dan-current-stock-numerik | Sort List: Alfabetis Tiga Tahap dan Current Stock Numerik | FE+BE | 25 | 336, 337 |
| TC-AC-DS-E2E-099-sort-list-kolom-curated-dan-photo | Sort List: Kolom Curated Ascending dan Descending serta Kolom Photo Tanpa Ikon Sort | FE+BE | 33 | 339, 340, 341 |
| TC-AC-DS-E2E-100-sort-list-default-tie-breaker-dan-pergantian-kolom | Sort List: Default SKU A-Z, Tie-breaker Deterministik, Pergantian Kolom, dan Tetap di Halaman yang Sama | FE+BE | 16 | 342, 343, 344, 345 |
| TC-AC-DS-E2E-101-setup-column-list-screening-dan-sc-a-ceklis | Setup Column List: Screening Overlay dan Popup serta Ceklis Kelas SC-A Hideable | FE+BE | 23 | 346, 347, 348 |
| TC-AC-DS-E2E-102-setup-column-list-geser-urutan | Setup Column List: Geser Urutan Kolom Kelas SC-A Hideable dan SC-B Curated | FE+BE | 20 | 349, 352 |
| TC-AC-DS-E2E-103-setup-column-list-pin-dan-batas-pin-keempat | Setup Column List: Pin dan Unpin Kelas SC-A Hideable serta Pin Keempat Diblok | FE+BE | 18 | 350, 358 |
| TC-AC-DS-E2E-104-setup-column-list-ceklis-curated-dan-pin-curated | Setup Column List: Ceklis Kelas SC-B Curated dan Pin atau Unpin Kelas SC-B Curated | FE+BE | 23 | 351, 353 |
| TC-AC-DS-E2E-105-setup-column-list-reset-tutup-dan-kolom-terakhir | Setup Column List: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck | FE+BE | 29 | 354, 355, 356 |
| TC-AC-DS-E2E-106-setup-column-list-panel-cepat-kolom-tetap-dan-isolasi | Setup Column List: Panel Cepat Tanpa Save, Kolom Checkbox dan Actions Tetap Pinned, Isolasi Konfigurasi, dan Kolom Curated Tampil | FE+BE | 25 | 357, 359, 360, 361 |
| TC-AC-DS-E2E-107-pagination-list-ukuran-halaman-dan-input-nomor | Pagination List: Default 10 per Halaman, Opsi Ukuran, Input Nomor Halaman, dan Reset ke Halaman 1 | FE+BE | 21 | 362, 363, 364, 365 |
| TC-AC-DS-E2E-108-state-list-refresh-reset-menu-dan-hapus-halaman-terakhir | State List: Refresh F5, Klik Ulang Menu Settings, Isolasi Sub-tab, dan Hapus Semua Baris Halaman Terakhir | FE+BE | 34 | 366, 367, 368, 369 |
| TC-AC-DS-E2E-109-download-list-cakupan-baris-kolom-dan-sidebar | Download List: Seluruh Baris, Mengikuti Search dan Filter, Kolom Tampil, dan Sidebar Category | FE+BE | 28 | 370, 371, 372, 602 |
| TC-AC-DS-E2E-110-download-list-nama-file-nol-baris-dan-distributor | Download List: Nama File dan Ekstensi, Nol Baris, Tanpa Toast Sukses, dan Download oleh Distributor | FE+BE | 30 | 373, 375, 377, 579 |
| TC-AC-DS-E2E-111-changelog-screening-modal-format-sel-dan-buka-tutup | Modal Changelog: Screening, Buka dan Tutup, serta Format Sel Date, Action, SKU, Old Value, dan New Value | FE+BE | 33 | 380, 381, 382 |
| TC-AC-DS-E2E-112-changelog-modified-by-photo-snapshot-dan-no-result | Modal Changelog: Modified By Format Singkat, Entri Photo Set as Default, Snapshot SKU Dihapus, Principal, dan No Result | FE+BE | 20 | 383, 384, 386, 388, 390 |
| TC-AC-DS-E2E-113-changelog-empty-state-dan-scope-distributor | Modal Changelog: Empty State Principal Tanpa SKU dan Scope Distributor Hanya Entri Miliknya | FE+BE | 13 | 385, 389 |
| TC-AC-DS-E2E-114-changelog-search-kelas-teks-campuran-dan-date | Search Changelog: Kelas Teks, Campuran Old/New Value, dan Kolom Date Tidak Dapat Dicari | FE+BE | 23 | 391, 392, 393 |
| TC-AC-DS-E2E-115-changelog-search-siklus-interaksi-case-dan-reset-paginasi | Search Changelog: Siklus Interaksi, Tidak Membedakan Huruf Besar-Kecil, Substring, dan Reset Paginasi | FE+BE | 28 | 394, 395, 396 |
| TC-AC-DS-E2E-116-changelog-filter-screening-opsi-dan-pencarian-dropdown | Filter Changelog: Screening Panel, Isi Opsi dari Data Tabel, dan Pencarian di Dalam Dropdown | FE+BE | 19 | 397, 398, 565 |
| TC-AC-DS-E2E-117-changelog-filter-multi-select-date-range-dan-satu-hari | Filter Changelog: Multi-select Action, SKU, Field, Modified By, Date Range Inklusif, dan Satu Hari | FE+BE | 19 | 399, 400, 599 |
| TC-AC-DS-E2E-118-changelog-filter-logika-or-and-dan-chip | Filter Changelog: Logika OR dan AND serta Penghapusan Chip dan Un-check Opsi | FE+BE | 25 | 401, 402, 403 |
| TC-AC-DS-E2E-119-changelog-filter-kombinasi-search-clear-dan-tanpa-hasil | Filter Changelog: Kombinasi Search dan Filter Dua Arah, Clear Field, dan Tanpa Hasil Lalu Pulih | FE+BE | 30 | 404, 405, 406, 407 |
| TC-AC-DS-E2E-120-changelog-kombinasi-penuh-dan-kosongkan-search | Changelog: Kombinasi Penuh Search, Filter, Sort, Pagination dan Mengosongkan Search saat Filter dan Sort Aktif | FE+BE | 26 | 566, 567 |
| TC-AC-DS-E2E-121-changelog-sort-alfabetis-dan-date | Sort Changelog: Alfabetis Action, SKU, Field dan Date Default Newest First Tiga Tahap | FE+BE | 28 | 408, 409 |
| TC-AC-DS-E2E-122-changelog-sort-old-new-value-dan-modified-by | Sort Changelog: Old/New Value Angka Sebelum Teks dan Modified By Memakai Nama Lengkap | FE+BE | 33 | 410, 411 |
| TC-AC-DS-E2E-123-changelog-setup-column-screening-overlay-dan-popup | Setup Column Changelog: Screening Overlay dan Popup | FE+BE | 21 | 412, 413 |
| TC-AC-DS-E2E-124-changelog-setup-column-geser-urutan-dan-reset | Setup Column Changelog: Geser Urutan Kolom dan Reset to Default | FE+BE | 25 | 415, 417 |
| TC-AC-DS-E2E-125-changelog-setup-column-pin-dan-batas-pin-keempat | Setup Column Changelog: Pin dan Unpin Kolom serta Pin Keempat Diblok | FE+BE | 18 | 416, 568 |
| TC-AC-DS-E2E-126-changelog-setup-column-tutup-kolom-terakhir-dan-isolasi | Setup Column Changelog: Tutup Tanpa Save, Kolom Terakhir Tidak Dapat Di-uncheck, dan Isolasi dari Konfigurasi List | FE+BE | 32 | 418, 419, 420 |
| TC-AC-DS-E2E-127-changelog-pagination-download-dan-kolom-tampil | Changelog: Pagination, Download Tanpa dan Dengan Filter, Nol Baris, dan Mengikuti Kolom Tampil | FE+BE | 35 | 421, 422, 425, 597 |
| TC-AC-DS-E2E-128-detail-sku-buka-screening-dan-info-grid | Popup Device SKU Detail: Jalur Buka, Screening, Backdrop, dan Info Grid | FE+BE | 25 | 426, 427, 428, 429 |
| TC-AC-DS-E2E-129-detail-usage-by-company-principal-total-stock-dan-empty | Usage by Company Principal: Seluruh Baris, Total Stock per Peran, Dua Badge, Kuota Alokasi, Empty State, dan Pembaruan Stok | FE+BE | 30 | 430, 431, 432, 433, 434, 435, 438, 441, 442 |
| TC-AC-DS-E2E-130-detail-usage-by-company-scope-distributor | Usage by Company Distributor: Baris Sendiri dan Client dalam Rantai serta Local Registration Nonaktif | FE+BE | 22 | 436, 437, 569 |
| TC-AC-DS-E2E-131-usage-search-kelas-teks-badge-angka-dan-siklus | Search Usage: Kelas Teks dan Badge, Angka Total Stock, dan Siklus Interaksi | FE+BE | 28 | 443, 444, 445 |
| TC-AC-DS-E2E-132-usage-filter-screening-entity-type-dan-total-stock | Filter Usage: Screening, Opsi Entity Type, Entity Type Dua Badge, dan OR | FE+BE | 21 | 446, 447, 448, 560 |
| TC-AC-DS-E2E-133-usage-filter-chip-pencarian-dropdown-dan-uncheck | Filter Usage: Penghapusan Chip, Un-check Opsi, Pencarian di Dalam Dropdown, dan Rentang Total Stock Inklusif | FE+BE | 34 | 449, 450, 564, 571 |
| TC-AC-DS-E2E-134-usage-sort-company-entity-type-dan-total-stock | Sort Usage: Company Default A-Z Tiga Tahap, Entity Type Badge, dan Total Stock Numerik | FE+BE | 20 | 451, 452, 453 |
| TC-AC-DS-E2E-135-usage-filter-kombinasi-and-search-dan-tanpa-hasil | Usage: Filter AND, Search Lalu Filter dan Sebaliknya, serta Empty State Tanpa Hasil | FE+BE | 32 | 439, 561, 562, 563 |
| TC-AC-DS-E2E-136-usage-kosongkan-search-dan-ganti-sort-saat-filter-aktif | Usage: Mengosongkan Search dan Mengganti Kolom Sort saat Search dan Filter Aktif | FE+BE | 31 | 587, 588 |
| TC-AC-DS-E2E-137-usage-setup-column-screening-dan-ceklis | Setup Column Usage: Screening Overlay dan Popup serta Ceklis dan Unceklis Kolom | FE+BE | 27 | 454, 455, 456 |
| TC-AC-DS-E2E-138-usage-setup-column-geser-urutan-dan-pin | Setup Column Usage: Geser Urutan Kolom serta Pin dan Unpin | FE+BE | 16 | 457, 458 |
| TC-AC-DS-E2E-139-usage-setup-column-reset-tutup-dan-kolom-terakhir | Setup Column Usage: Reset to Default, Tutup Tanpa Save, dan Kolom Terakhir Tidak Dapat Di-uncheck | FE+BE | 26 | 459, 460, 461 |
| TC-AC-DS-E2E-140-usage-pagination-lokal-kombinasi-penuh-dan-isolasi-konfigurasi | Usage: Pagination Lokal 13 Baris, Kombinasi Penuh Search/Filter/Sort, dan Isolasi Konfigurasi Kolom dari List dan Changelog | FE+BE | 37 | 462, 585, 586 |
| TC-AC-DS-E2E-141-usage-download-cakupan-baris-nol-baris-dan-kolom-tampil | Download Usage: Nama File, Ekstensi, Cakupan Baris, Nol Baris, dan Mengikuti Kolom Tampil | FE+BE | 28 | 463, 466, 598 |
| TC-AC-DS-E2E-142-log-tiga-surface-create-dan-edit-kode-device-name | Log Tiga Surface: Create SKU serta Edit Kode SKU dan Device Name | FE+BE | 49 | 467, 468, 469 |
| TC-AC-DS-E2E-143-log-tiga-surface-edit-brand-model-range-type | Log Tiga Surface: Edit Brand, Model/Type, dan Range Type | FE+BE | 18 | 470, 471, 472 |
| TC-AC-DS-E2E-144-log-tiga-surface-edit-port-user-tag-dan-photo | Log Tiga Surface: Edit Port, User TAG, dan Photo Satu Foto | FE+BE | 51 | 473, 474, 475 |
| TC-AC-DS-E2E-145-log-tiga-surface-photo-dua-foto-default-dan-kapitalisasi | Log Tiga Surface: Photo Dua Foto, Set as Default, dan Perubahan Kapitalisasi Model/Type | FE+BE | 41 | 476, 477, 483 |
| TC-AC-DS-E2E-146-log-tiga-surface-delete-bulk-delete-dan-edit-multi-field | Log Tiga Surface: Delete Single, Bulk Delete, dan Edit Beberapa Field Sekaligus | FE+BE | 47 | 479, 480, 481 |
| TC-AC-DS-E2E-147-log-system-log-aktor-create-edit-dan-delete | System Log Aktor: Create, Edit per Field, dan Delete | FE+BE | 34 | 485, 486, 487 |
| TC-AC-DS-E2E-148-log-activity-log-principal-distributor-dan-edit | Activity Log: Aksi SKU Principal sebagai Objek Non-entitas, Distributor Entity-bound, dan Edit per Field | FE+BE | 35 | 488, 489, 490 |
| TC-AC-DS-E2E-149-log-snapshot-immutability-dan-filter-identitas-sku | Log Snapshot: Device Name Rename, Edit Kode Dua Kali, dan Filter All SKUs Berkunci Identitas SKU | FE+BE | 42 | 491, 492, 493 |
| TC-AC-DS-E2E-150-log-request-api-langsung-aktor-berhak | Request API Langsung oleh Aktor Berhak Menulis Log Tiga Surface yang Sama dengan Form | FE+BE | 37 | 494, 583, 584 |
| TC-AC-DS-E2E-151-log-absence-tanpa-perubahan-ditolak-dan-promosi-default | Absence Log: Edit Tanpa Perubahan dan Edit Field Terkunci yang Ditolak Tidak Menulis Log | FE+BE | 34 | 206, 482, 484 |
| TC-AC-DS-E2E-152-log-absence-register-kode-duplikat-ditolak | Absence Log: Register Kode Duplikat yang Ditolak Tidak Menulis Log | FE+BE | 27 | 553 |
| TC-AC-DS-E2E-153-log-absence-register-gagal-5xx | Absence Log: Register Gagal 5xx Tidak Menulis Log | FE+BE | 29 | 554 |
| TC-AC-DS-E2E-154-sinkron-modul-stok-register-sku-hardware-dan-tag | Sinkron Modul Stok: Register SKU Hardware dan TAG Menjadi Pilihan Add Stock dan Baris Stock List | FE+BE | 30 | 496, 497 |
| TC-AC-DS-E2E-155-sinkron-modul-stok-edit-brand-model-photo-dan-device-name | Sinkron Modul Stok: Edit Brand, Model/Type, Photo, dan Device Name Tercermin pada Stock List dan Stock Detail Hardware Stock | FE+BE | 26 | 498, 499 |
| TC-AC-DS-E2E-156-sinkron-modul-stok-delete-dan-kunci-field | Sinkron Modul Stok: Delete dan Bulk Delete Menghilangkan Pilihan Stok serta Add Stock Mengaktifkan Kunci Field SKU | FE+BE | 26 | 501, 502, 503 |
| TC-AC-DS-E2E-157-sinkron-master-rename-dan-time-zone | Sinkron Master Data: Rename Device Name, Brand, Category dan Perubahan Time Zone General Settings | FE+BE | 35 | 504, 505, 506, 507 |
| TC-AC-DS-E2E-158-sinkron-realtime-sesi-lain-register-edit-delete | Sinkron Realtime: Register, Edit, dan Delete oleh Sesi Lain Tercermin pada List tanpa Muat Ulang | FE+BE | 14 | 509, 510, 511 |
| TC-AC-DS-E2E-159-defense-gate-entitas-capability-dan-detail-lintas-scope-via-api | Defense-in-Depth: Partner, Principal Tanpa Capability, Local Registration Nonaktif, dan Detail SKU Distributor Ditolak lewat API | FE+BE | 37 | 512, 513, 514, 519, 522, 603, 604 |
| TC-AC-DS-E2E-160-defense-tier-role-menulis-via-api | Defense-in-Depth: Read Only, Create-Only, Update-Only, dan Delete-Only Menulis lewat API Ditolak | FE+BE | 39 | 515, 516, 517, 518 |
| TC-AC-DS-E2E-161-defense-scope-distributor-via-api | Defense-in-Depth: Distributor Mengubah atau Menghapus SKU Principal, Detail Distributor Lain, Brand Entitas Lain, dan Usage Lintas Scope | FE+BE | 34 | 520, 521, 528, 605 |
| TC-AC-DS-E2E-162-defense-validasi-server-field-terkunci-device-name-dan-kondisional | Defense-in-Depth: Server Menolak Field Terkunci, Device Name Category Lain, dan Field Kondisional Tidak Sesuai Ancestry | FE+BE | 30 | 523, 524, 525 |
| TC-AC-DS-E2E-163-defense-manipulasi-dom-field-terkunci-pada-edit | Defense-in-Depth: Manipulasi DOM Field SKU, Range Type, User TAG, dan Device Name Terkunci Ditolak Seluruhnya | FE+BE | 10 | 233, 234, 235, 236 |
| TC-AC-DS-E2E-164-defense-device-name-category-lain-emoji-dan-delete-berstok | Defense-in-Depth: Device Name Category Lain pada Edit, Emoji Lolos Filter FE, dan Delete SKU Berstok lewat API | FE+BE | 39 | 238, 527, 529, 590 |
| TC-AC-DS-E2E-165-defense-injeksi-xss-sql-dan-karakter-invalid-sku | Defense-in-Depth: Payload Script, Injeksi Basis Data, dan Karakter Invalid pada SKU lewat API | FE+BE | 35 | 309, 526, 530, 531, 589 |
| TC-AC-DS-E2E-166-resilience-baca-error-load-list-changelog-dan-usage | Resilience Baca: Error Load List, Changelog, dan Usage by Company dengan Try Again | FE+BE | 19 | 32, 387, 440 |
| TC-AC-DS-E2E-167-resilience-download-gagal-list-changelog-dan-usage | Resilience Download: Kegagalan Download List, Changelog, dan Usage by Company Menampilkan Toast Error | FE+BE | 20 | 376, 424, 465 |
| TC-AC-DS-E2E-168-resilience-register-5xx-dan-timeout | Resilience Register: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input | FE+BE | 35 | 175, 176 |
| TC-AC-DS-E2E-169-resilience-upload-foto-staging-gagal-register-dan-edit | Resilience Upload Foto: Upload ke Staging Gagal pada Register dan Edit Menampilkan Error Inline | FE+BE | 21 | 142, 229 |
| TC-AC-DS-E2E-170-resilience-edit-dan-delete-5xx-timeout | Resilience Edit dan Delete: Kegagalan Server 5xx dan Timeout Jaringan Mempertahankan Input dan Dialog | FE+BE | 34 | 252, 253, 268, 269 |
| TC-AC-DS-E2E-171-resilience-bulk-delete-5xx-timeout-dan-kegagalan-parsial | Resilience Bulk Delete: 5xx, Timeout, dan Kegagalan Tak Terduga Mempertahankan Item yang Sudah Terhapus | FE+BE | 29 | 295, 296, 548 |
| TC-AC-DS-E2E-172-resilience-submit-gagal-setelah-foto-staging-tidak-permanen | Resilience Foto Staging: Submit atau Save Gagal setelah Foto di Staging Tidak Membuat Foto Permanen | FE+BE | 26 | 143, 230 |
| TC-AC-DS-E2E-173-multi-konteks-dua-sesi-register-kode-sama-dan-edit-last-write-wins | Multi-konteks: Dua Sesi Register Kode Sama Ditolak Duplikat dan Dua Sesi Edit Last-write-wins | FE+BE | 41 | 180, 542, 543 |
| TC-AC-DS-E2E-174-volume-selection-limit-dan-select-all-distributor | Volume Data: Selection Limit 100, Select All Melebihi Limit, dan Basis Hitung SKU Milik Distributor | FE+BE | 39 | 82, 277, 278, 279, 595 |
| TC-AC-DS-E2E-175-volume-download-di-atas-5000-baris-dan-tepat-5000 | Volume Data: Download 5.001 Baris Memakai Loading Screen dan Tepat 5.000 Baris Tanpa Loading | FE+BE | 13 | 378, 379 |
| TC-AC-DS-E2E-176-isi-file-export-list-changelog-dan-usage | Isi File Export: Nilai Sel List, Changelog, dan Usage by Company | FE+BE | 27 | 374, 423, 464 |
| TC-AC-DS-E2E-177-state-tenant-baca-dan-download-suspended-expired | State Tenant: Suspended dan Expired Tetap Dapat Membaca List dan Download | FE+BE | 20 | 35, 577, 578 |
| TC-AC-DS-E2E-178-state-tenant-register-ditolak-suspended-expired | State Tenant: Register SKU oleh Distributor Suspended, Distributor Expired, dan Principal Expired Ditolak | FE+BE | 28 | 532, 536, 540 |
| TC-AC-DS-E2E-179-state-tenant-edit-ditolak-suspended-expired | State Tenant: Edit SKU oleh Distributor Suspended dan Expired Ditolak | FE+BE | 18 | 533, 537 |
| TC-AC-DS-E2E-180-state-tenant-delete-ditolak-suspended-expired | State Tenant: Delete SKU oleh Distributor Suspended, Distributor Expired, dan Principal Expired Ditolak | FE+BE | 23 | 534, 538, 541 |
| TC-AC-DS-E2E-181-state-tenant-bulk-delete-ditolak-suspended-expired | State Tenant: Bulk Delete oleh Distributor Suspended dan Expired Ditolak | FE+BE | 18 | 535, 539 |
| TC-AC-DS-E2E-182-plan-tier-register-edit-delete-identik | Plan Tier: Register, Edit, dan Delete Berperilaku Identik pada Starter, Growth, Professional, dan Enterprise | FE+BE | 13 | 559 |
| TC-AC-DS-E2E-183-capability-dicabut-saat-form-terbuka | Capability atau Local Registration Dicabut saat Form atau Dialog Terbuka: Aksi Ditolak dan Form Tetap Terbuka | FE+BE | 33 | 549, 550, 551, 552 |
| TC-AC-DS-E2E-186-register-stay-on-form-mereset-field-dan-popup-tetap-terbuka | Register SKU: Submit dengan Stay on this form Mereset Semua Field termasuk Foto dan Popup Tetap Terbuka | FE+BE | 19 | 160 |
| TC-AC-DS-E2E-187-register-backdrop-dan-perubahan-dikembalikan-dianggap-bersih | Register SKU: Klik Backdrop Tidak Menutup Popup dan Perubahan yang Dikembalikan ke Nilai Awal Dianggap Bersih | FE+BE | 12 | 169, 170 |
| TC-AC-DS-E2E-188-edit-saving-state-dan-klik-ganda-save | Edit SKU: Saving State pada Tombol Save dan Klik Ganda Cepat Menghasilkan Satu Perubahan | FE+BE | 16 | 250, 251 |
| TC-AC-DS-E2E-189-bulk-delete-hasil-aktual-menentukan-toast-preview-berubah | Bulk Delete: Hasil Aktual Menentukan Toast saat Preview Campuran Menjadi Homogen dan Homogen Menjadi Campuran | FE+BE | 23 | 293, 294 |
| TC-AC-DS-E2E-190-kombinasi-list-opsi-filter-hilang-dari-data | Kombinasi List: Opsi Filter yang Dipakai Filter Aktif Hilang dari Data | FE+BE | 13 | 335 |
| TC-AC-DS-E2E-191-sort-list-last-modified-oldest-dan-newest-first | Sort List: Last Modified Oldest First dan Newest First | FE+BE | 6 | 338 |
| TC-AC-DS-E2E-192-changelog-setup-column-ceklis-dan-unceklis-kolom | Setup Column Changelog: Ceklis dan Unceklis Tujuh Kolom | FE+BE | 17 | 414 |
| TC-AC-DS-E2E-193-log-absence-api-ditolak-dan-promosi-default | Absence Log: Request API Ditolak dan Promosi Default Otomatis Tidak Menulis Log | FE+BE | 26 | 478, 495 |
| TC-AC-DS-E2E-194-sinkron-modul-stok-edit-kode-sku-range-type-dan-user-tag | Sinkron Modul Stok: Edit Kode SKU, Range Type, dan User TAG Tercermin pada Stock List Hardware Stock dan TAG Stock | FE+BE | 14 | 500 |
| TC-AC-DS-E2E-195-sinkron-sku-principal-read-only-di-distributor | Sinkron Modul Stok: SKU Principal yang Baru Didaftarkan Terlihat Read-only pada List Distributor | FE+BE | 14 | 508 |

## Penyimpangan dari rencana

- Nomor cadangan terpakai: 186–195 (sepuluh dari dua belas). 184 dan 185 (cadangan slice 1) tidak dipakai. Spec cadangan hasil pecahan:

| Spec baru | Asal | TC yang dipindah |
|---|---|---|
| 186 | 044 | 160 |
| 187 | 051 | 169, 170 |
| 188 | 071 | 250, 251 |
| 189 | 084 | 293, 294 |
| 190 | 097 | 335 |
| 191 | 098 | 338 |
| 192 | 123 | 414 |
| 193 | 151 | 478, 495 |
| 194 | 155 | 500 |
| 195 | 154 | 508 |

- Spec asal yang dipecah diretitle agar sesuai isinya (044, 051, 071, 084, 097, 098, 123, 151, 154, 155). Slug folder/id berubah dari rencana pada 044, 051, 098, 123, 154, 155; slug folder 067, 068, 069, 071 belum cocok dengan judul spec setelah pemecahan (id tidak diubah selama run, menunggu keputusan). Judul 067, 068, 069, 132 diubah tanpa perubahan TC.
- Hanya TC pada tabel di atas yang pindah spec; sisa TC tetap seperti rencana.

## Pembagian TC lintas spec

- Tidak ada TC yang terbelah lintas spec.
- Asersi absence log (kelas g, S-05) ditaruh di spec asal aksinya (070, 075, 076, 084, 085, 086, 178–181), bukan dikumpulkan di satu spec kelas g; menunggu keputusan.
- Pelaku kedua untuk TC "sesi lain" (177–179, 231, 232, 544–547, 574) lewat sesi API, bukan kelas c; hanya TC 180, 542, 543 memakai dua sesi UI; TC 509–511 punya spec sendiri.

## Kebutuhan lingkungan (tim FE)

- Env var password: 23 nama `AC_DS_*` (`AC_DS_TC_PASSWORD`, `AC_DS_TC2_PASSWORD`, `AC_DS_RO_PASSWORD`, `AC_DS_C_PASSWORD`, `AC_DS_U_PASSWORD`, `AC_DS_D_PASSWORD`, `AC_DS_CUD_PASSWORD`, `AC_DS_NOCAP_PASSWORD`, `AC_DS_GM_PASSWORD`, `AC_DS_DIST_PASSWORD`, `AC_DS_DIST_RO_PASSWORD`, `AC_DS_DIST_C_PASSWORD`, `AC_DS_DIST_U_PASSWORD`, `AC_DS_DIST_D_PASSWORD`, `AC_DS_PARTNER_PASSWORD`, `AC_DS_DIST2_PASSWORD`, `AC_DS_DISTOFF_PASSWORD`, `AC_DS_DISTSUSP_PASSWORD`, `AC_DS_DISTEXP_PASSWORD`, `AC_DS_PRIEXP_PASSWORD`, `AC_DS_FRESH_PASSWORD`, `AC_DS_BIG_PASSWORD`, `AC_DS_BIG5K_PASSWORD`). Belum terdaftar di `spectra.config.ts` dan `.env.example`; berkas itu tidak diubah oleh generate spec.
- Fixture `fixtures/settings-device-sku.json` (belum ada) memuat nilai Pre-setup #25–#43; sebagian entitas (#18/#19 nama tampil, #20–#23, #34, #38, #41–#43, `NM-01`/`MN-01`) belum diverifikasi ada di environment.
- Fixture BE: seeding idempotent data Pre-setup (SKU inti #29, seed #30, SKU Distributor #31/#43, usage #32, changelog #33/#34), pelaku kedua lewat sesi API, pengubah General Settings, Selection Limit (Plans & Licensing > System Limits), capability role, Local Registration, state tenant Suspended/Expired, plan tier (#41).
- Kemampuan teknis: `Spectra.intercept()` (5xx, timeout, upload gagal), penangkap unduhan CSV/XLSX, pembaca isi file export, perangkat atau emulator Android (spec 014), dua sesi UI (TC 180, 542, 543).
- Suite berjalan serial (`parallel: false`): spec mengubah state global (Date Format, Time Zone, Selection Limit, capability role, Local Registration) dan data SKU bersama.
- Environment automation harus terisolasi dari aktivitas pengguna lain.
- Tidak ada manipulasi jam; `Jam server dan jam browser sinkron` hanya dibaca dengan toleransi satu menit, dan jeda nyata 1 detik (debounce SKU, spec 033, 035) tertulis di Prerequisites.

## Temuan yang masih terbuka

Temuan TC sumber dicatat per spec di `## Notes` butir "Temuan untuk QA". Keputusan terbuka dicatat di `work-items/settings-device-sku/decisions-e2e-generate-spec.json`:

- S-12: asersi memakai nama literal Pre-setup #29/#30/#31 (mis. `HHR-ARC-100`, total 129 SKU, 35 entri Changelog); Lampiran A tidak memuat pengecualian untuk modul ini.
- Fixture dan env var `AC_DS_*` belum diverifikasi atau didaftarkan.
- Perangkat Android untuk TC 49–51; akun plan tier TC 559 dan 182 tanpa email/env di TC (S-15).
- Penempatan absence log, pelaku kedua lewat API, slug yang tidak cocok setelah pemecahan, mock vs FE+BE untuk Setup Column dan resilience, fixture Selection Limit (TC 277–279, 529, 595), flag walkthrough tooltip.
- Spec yang melewati batas ±35 langkah (alasan tertulis di `## Notes` tiap spec): 005 (41), 009 (38), 011 (41), 018 (140), 023 (36), 029 (44), 030 (37), 035 (39), 037 (37), 042 (36), 046 (41), 047 (40), 052 (41), 054 (42), 071 (40), 072 (47), 081 (37), 083 (36), 086 (37), 140 (37), 142 (49), 144 (51), 145 (41), 146 (47), 149 (42), 150 (37), 159 (37), 160 (39), 164 (39), 173 (41), 174 (39).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-DS-1 | TC-AC-DS-E2E-001 | FE+BE |
| TC-AC-DS-2 | TC-AC-DS-E2E-001 | FE+BE |
| TC-AC-DS-3 | TC-AC-DS-E2E-002 | FE+BE |
| TC-AC-DS-4 | TC-AC-DS-E2E-001 | FE+BE |
| TC-AC-DS-5 | TC-AC-DS-E2E-002 | FE+BE |
| TC-AC-DS-6 | TC-AC-DS-E2E-001 | FE+BE |
| TC-AC-DS-7 | TC-AC-DS-E2E-003 | FE+BE |
| TC-AC-DS-8 | TC-AC-DS-E2E-003 | FE+BE |
| TC-AC-DS-9 | TC-AC-DS-E2E-003 | FE+BE |
| TC-AC-DS-10 | TC-AC-DS-E2E-004 | FE+BE |
| TC-AC-DS-11 | TC-AC-DS-E2E-004 | FE+BE |
| TC-AC-DS-12 | TC-AC-DS-E2E-004 | FE+BE |
| TC-AC-DS-13 | TC-AC-DS-E2E-005 | FE+BE |
| TC-AC-DS-14 | TC-AC-DS-E2E-005 | FE+BE |
| TC-AC-DS-15 | TC-AC-DS-E2E-005 | FE+BE |
| TC-AC-DS-16 | TC-AC-DS-E2E-005 | FE+BE |
| TC-AC-DS-17 | TC-AC-DS-E2E-005 | FE+BE |
| TC-AC-DS-18 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-19 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-20 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-21 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-22 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-23 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-24 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-25 | TC-AC-DS-E2E-006 | FE+BE |
| TC-AC-DS-26 | TC-AC-DS-E2E-007 | FE+BE |
| TC-AC-DS-27 | TC-AC-DS-E2E-007 | FE+BE |
| TC-AC-DS-28 | TC-AC-DS-E2E-007 | FE+BE |
| TC-AC-DS-29 | TC-AC-DS-E2E-008 | FE+BE |
| TC-AC-DS-30 | TC-AC-DS-E2E-008 | FE+BE |
| TC-AC-DS-31 | TC-AC-DS-E2E-008 | FE+BE |
| TC-AC-DS-32 | TC-AC-DS-E2E-166 | FE+BE |
| TC-AC-DS-33 | TC-AC-DS-E2E-008 | FE+BE |
| TC-AC-DS-34 | TC-AC-DS-E2E-023 | FE+BE |
| TC-AC-DS-35 | TC-AC-DS-E2E-177 | FE+BE |
| TC-AC-DS-36 | TC-AC-DS-E2E-009 | FE+BE |
| TC-AC-DS-37 | TC-AC-DS-E2E-009 | FE+BE |
| TC-AC-DS-38 | TC-AC-DS-E2E-009 | FE+BE |
| TC-AC-DS-39 | TC-AC-DS-E2E-010 | FE+BE |
| TC-AC-DS-40 | TC-AC-DS-E2E-010 | FE+BE |
| TC-AC-DS-41 | TC-AC-DS-E2E-009 | FE+BE |
| TC-AC-DS-42 | TC-AC-DS-E2E-011 | FE+BE |
| TC-AC-DS-43 | TC-AC-DS-E2E-011 | FE+BE |
| TC-AC-DS-44 | TC-AC-DS-E2E-011 | FE+BE |
| TC-AC-DS-45 | TC-AC-DS-E2E-012 | FE+BE |
| TC-AC-DS-46 | TC-AC-DS-E2E-023 | FE+BE |
| TC-AC-DS-47 | TC-AC-DS-E2E-012 | FE+BE |
| TC-AC-DS-48 | TC-AC-DS-E2E-012 | FE+BE |
| TC-AC-DS-49 | TC-AC-DS-E2E-014 | FE+BE |
| TC-AC-DS-50 | TC-AC-DS-E2E-014 | FE+BE |
| TC-AC-DS-51 | TC-AC-DS-E2E-014 | FE+BE |
| TC-AC-DS-52 | TC-AC-DS-E2E-015 | FE+BE |
| TC-AC-DS-53 | TC-AC-DS-E2E-015 | FE+BE |
| TC-AC-DS-54 | TC-AC-DS-E2E-016 | FE+BE |
| TC-AC-DS-55 | TC-AC-DS-E2E-016 | FE+BE |
| TC-AC-DS-56 | TC-AC-DS-E2E-017 | FE+BE |
| TC-AC-DS-57 | TC-AC-DS-E2E-017 | FE+BE |
| TC-AC-DS-58 | TC-AC-DS-E2E-017 | FE+BE |
| TC-AC-DS-59 | TC-AC-DS-E2E-015 | FE+BE |
| TC-AC-DS-60 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-61 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-62 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-63 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-64 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-65 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-66 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-67 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-68 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-69 | TC-AC-DS-E2E-018 | FE+BE |
| TC-AC-DS-70 | TC-AC-DS-E2E-019 | FE+BE |
| TC-AC-DS-71 | TC-AC-DS-E2E-020 | FE+BE |
| TC-AC-DS-72 | TC-AC-DS-E2E-021 | FE+BE |
| TC-AC-DS-73 | TC-AC-DS-E2E-021 | FE+BE |
| TC-AC-DS-74 | TC-AC-DS-E2E-019 | FE+BE |
| TC-AC-DS-75 | TC-AC-DS-E2E-020 | FE+BE |
| TC-AC-DS-76 | TC-AC-DS-E2E-021 | FE+BE |
| TC-AC-DS-77 | TC-AC-DS-E2E-022 | FE+BE |
| TC-AC-DS-78 | TC-AC-DS-E2E-023 | FE+BE |
| TC-AC-DS-79 | TC-AC-DS-E2E-023 | FE+BE |
| TC-AC-DS-80 | TC-AC-DS-E2E-024 | FE+BE |
| TC-AC-DS-81 | TC-AC-DS-E2E-024 | FE+BE |
| TC-AC-DS-82 | TC-AC-DS-E2E-174 | FE+BE |
| TC-AC-DS-83 | TC-AC-DS-E2E-025 | FE+BE |
| TC-AC-DS-84 | TC-AC-DS-E2E-025 | FE+BE |
| TC-AC-DS-85 | TC-AC-DS-E2E-026 | FE+BE |
| TC-AC-DS-86 | TC-AC-DS-E2E-022 | FE+BE |
| TC-AC-DS-87 | TC-AC-DS-E2E-027 | FE+BE |
| TC-AC-DS-88 | TC-AC-DS-E2E-027 | FE+BE |
| TC-AC-DS-89 | TC-AC-DS-E2E-027 | FE+BE |
| TC-AC-DS-90 | TC-AC-DS-E2E-028 | FE+BE |
| TC-AC-DS-91 | TC-AC-DS-E2E-028 | FE+BE |
| TC-AC-DS-92 | TC-AC-DS-E2E-028 | FE+BE |
| TC-AC-DS-93 | TC-AC-DS-E2E-028 | FE+BE |
| TC-AC-DS-94 | TC-AC-DS-E2E-029 | FE+BE |
| TC-AC-DS-95 | TC-AC-DS-E2E-029 | FE+BE |
| TC-AC-DS-96 | TC-AC-DS-E2E-029 | FE+BE |
| TC-AC-DS-97 | TC-AC-DS-E2E-029 | FE+BE |
| TC-AC-DS-98 | TC-AC-DS-E2E-030 | FE+BE |
| TC-AC-DS-99 | TC-AC-DS-E2E-031 | FE+BE |
| TC-AC-DS-100 | TC-AC-DS-E2E-055 | FE+BE |
| TC-AC-DS-101 | TC-AC-DS-E2E-031 | FE+BE |
| TC-AC-DS-102 | TC-AC-DS-E2E-055 | FE+BE |
| TC-AC-DS-103 | TC-AC-DS-E2E-031 | FE+BE |
| TC-AC-DS-104 | TC-AC-DS-E2E-032 | FE+BE |
| TC-AC-DS-105 | TC-AC-DS-E2E-032 | FE+BE |
| TC-AC-DS-106 | TC-AC-DS-E2E-032 | FE+BE |
| TC-AC-DS-107 | TC-AC-DS-E2E-032 | FE+BE |
| TC-AC-DS-108 | TC-AC-DS-E2E-032 | FE+BE |
| TC-AC-DS-109 | TC-AC-DS-E2E-033 | FE+BE |
| TC-AC-DS-110 | TC-AC-DS-E2E-033 | FE+BE |
| TC-AC-DS-111 | TC-AC-DS-E2E-033 | FE+BE |
| TC-AC-DS-112 | TC-AC-DS-E2E-033 | FE+BE |
| TC-AC-DS-113 | TC-AC-DS-E2E-033 | FE+BE |
| TC-AC-DS-114 | TC-AC-DS-E2E-034 | FE+BE |
| TC-AC-DS-115 | TC-AC-DS-E2E-034 | FE+BE |
| TC-AC-DS-116 | TC-AC-DS-E2E-035 | FE+BE |
| TC-AC-DS-117 | TC-AC-DS-E2E-035 | FE+BE |
| TC-AC-DS-118 | TC-AC-DS-E2E-035 | FE+BE |
| TC-AC-DS-119 | TC-AC-DS-E2E-056 | FE+BE |
| TC-AC-DS-120 | TC-AC-DS-E2E-056 | FE+BE |
| TC-AC-DS-121 | TC-AC-DS-E2E-056 | FE+BE |
| TC-AC-DS-122 | TC-AC-DS-E2E-035 | FE+BE |
| TC-AC-DS-123 | TC-AC-DS-E2E-036 | FE+BE |
| TC-AC-DS-124 | TC-AC-DS-E2E-036 | FE+BE |
| TC-AC-DS-125 | TC-AC-DS-E2E-036 | FE+BE |
| TC-AC-DS-126 | TC-AC-DS-E2E-037 | FE+BE |
| TC-AC-DS-127 | TC-AC-DS-E2E-037 | FE+BE |
| TC-AC-DS-128 | TC-AC-DS-E2E-037 | FE+BE |
| TC-AC-DS-129 | TC-AC-DS-E2E-034 | FE+BE |
| TC-AC-DS-130 | TC-AC-DS-E2E-038 | FE+BE |
| TC-AC-DS-131 | TC-AC-DS-E2E-038 | FE+BE |
| TC-AC-DS-132 | TC-AC-DS-E2E-038 | FE+BE |
| TC-AC-DS-133 | TC-AC-DS-E2E-039 | FE+BE |
| TC-AC-DS-134 | TC-AC-DS-E2E-039 | FE+BE |
| TC-AC-DS-135 | TC-AC-DS-E2E-039 | FE+BE |
| TC-AC-DS-136 | TC-AC-DS-E2E-040 | FE+BE |
| TC-AC-DS-137 | TC-AC-DS-E2E-040 | FE+BE |
| TC-AC-DS-138 | TC-AC-DS-E2E-040 | FE+BE |
| TC-AC-DS-139 | TC-AC-DS-E2E-041 | FE+BE |
| TC-AC-DS-140 | TC-AC-DS-E2E-039 | FE+BE |
| TC-AC-DS-141 | TC-AC-DS-E2E-041 | FE+BE |
| TC-AC-DS-142 | TC-AC-DS-E2E-169 | FE+BE |
| TC-AC-DS-143 | TC-AC-DS-E2E-172 | FE+BE |
| TC-AC-DS-144 | TC-AC-DS-E2E-048 | FE+BE |
| TC-AC-DS-145 | TC-AC-DS-E2E-041 | FE+BE |
| TC-AC-DS-146 | TC-AC-DS-E2E-042 | FE+BE |
| TC-AC-DS-147 | TC-AC-DS-E2E-042 | FE+BE |
| TC-AC-DS-148 | TC-AC-DS-E2E-042 | FE+BE |
| TC-AC-DS-149 | TC-AC-DS-E2E-043 | FE+BE |
| TC-AC-DS-150 | TC-AC-DS-E2E-043 | FE+BE |
| TC-AC-DS-151 | TC-AC-DS-E2E-043 | FE+BE |
| TC-AC-DS-152 | TC-AC-DS-E2E-044 | FE+BE |
| TC-AC-DS-153 | TC-AC-DS-E2E-044 | FE+BE |
| TC-AC-DS-154 | TC-AC-DS-E2E-046 | FE+BE |
| TC-AC-DS-155 | TC-AC-DS-E2E-046 | FE+BE |
| TC-AC-DS-156 | TC-AC-DS-E2E-047 | FE+BE |
| TC-AC-DS-157 | TC-AC-DS-E2E-047 | FE+BE |
| TC-AC-DS-158 | TC-AC-DS-E2E-048 | FE+BE |
| TC-AC-DS-159 | TC-AC-DS-E2E-055 | FE+BE |
| TC-AC-DS-160 | TC-AC-DS-E2E-186 | FE+BE |
| TC-AC-DS-161 | TC-AC-DS-E2E-045 | FE+BE |
| TC-AC-DS-162 | TC-AC-DS-E2E-049 | FE+BE |
| TC-AC-DS-163 | TC-AC-DS-E2E-049 | FE+BE |
| TC-AC-DS-164 | TC-AC-DS-E2E-050 | FE+BE |
| TC-AC-DS-165 | TC-AC-DS-E2E-050 | FE+BE |
| TC-AC-DS-166 | TC-AC-DS-E2E-051 | FE+BE |
| TC-AC-DS-167 | TC-AC-DS-E2E-051 | FE+BE |
| TC-AC-DS-168 | TC-AC-DS-E2E-051 | FE+BE |
| TC-AC-DS-169 | TC-AC-DS-E2E-187 | FE+BE |
| TC-AC-DS-170 | TC-AC-DS-E2E-187 | FE+BE |
| TC-AC-DS-171 | TC-AC-DS-E2E-052 | FE+BE |
| TC-AC-DS-172 | TC-AC-DS-E2E-052 | FE+BE |
| TC-AC-DS-173 | TC-AC-DS-E2E-052 | FE+BE |
| TC-AC-DS-174 | TC-AC-DS-E2E-053 | FE+BE |
| TC-AC-DS-175 | TC-AC-DS-E2E-168 | FE+BE |
| TC-AC-DS-176 | TC-AC-DS-E2E-168 | FE+BE |
| TC-AC-DS-177 | TC-AC-DS-E2E-054 | FE+BE |
| TC-AC-DS-178 | TC-AC-DS-E2E-054 | FE+BE |
| TC-AC-DS-179 | TC-AC-DS-E2E-054 | FE+BE |
| TC-AC-DS-180 | TC-AC-DS-E2E-173 | FE+BE |
| TC-AC-DS-181 | TC-AC-DS-E2E-057 | FE+BE |
| TC-AC-DS-182 | TC-AC-DS-E2E-057 | FE+BE |
| TC-AC-DS-183 | TC-AC-DS-E2E-057 | FE+BE |
| TC-AC-DS-184 | TC-AC-DS-E2E-058 | FE+BE |
| TC-AC-DS-185 | TC-AC-DS-E2E-058 | FE+BE |
| TC-AC-DS-186 | TC-AC-DS-E2E-058 | FE+BE |
| TC-AC-DS-187 | TC-AC-DS-E2E-057 | FE+BE |
| TC-AC-DS-188 | TC-AC-DS-E2E-057 | FE+BE |
| TC-AC-DS-189 | TC-AC-DS-E2E-059 | FE+BE |
| TC-AC-DS-190 | TC-AC-DS-E2E-059 | FE+BE |
| TC-AC-DS-191 | TC-AC-DS-E2E-059 | FE+BE |
| TC-AC-DS-192 | TC-AC-DS-E2E-066 | FE+BE |
| TC-AC-DS-193 | TC-AC-DS-E2E-066 | FE+BE |
| TC-AC-DS-194 | TC-AC-DS-E2E-066 | FE+BE |
| TC-AC-DS-195 | TC-AC-DS-E2E-066 | FE+BE |
| TC-AC-DS-196 | TC-AC-DS-E2E-067 | FE+BE |
| TC-AC-DS-197 | TC-AC-DS-E2E-067 | FE+BE |
| TC-AC-DS-198 | TC-AC-DS-E2E-067 | FE+BE |
| TC-AC-DS-199 | TC-AC-DS-E2E-067 | FE+BE |
| TC-AC-DS-200 | TC-AC-DS-E2E-068 | FE+BE |
| TC-AC-DS-201 | TC-AC-DS-E2E-068 | FE+BE |
| TC-AC-DS-202 | TC-AC-DS-E2E-068 | FE+BE |
| TC-AC-DS-203 | TC-AC-DS-E2E-069 | FE+BE |
| TC-AC-DS-204 | TC-AC-DS-E2E-069 | FE+BE |
| TC-AC-DS-205 | TC-AC-DS-E2E-069 | FE+BE |
| TC-AC-DS-206 | TC-AC-DS-E2E-151 | FE+BE |
| TC-AC-DS-207 | TC-AC-DS-E2E-070 | FE+BE |
| TC-AC-DS-208 | TC-AC-DS-E2E-070 | FE+BE |
| TC-AC-DS-209 | TC-AC-DS-E2E-061 | FE+BE |
| TC-AC-DS-210 | TC-AC-DS-E2E-061 | FE+BE |
| TC-AC-DS-211 | TC-AC-DS-E2E-061 | FE+BE |
| TC-AC-DS-212 | TC-AC-DS-E2E-061 | FE+BE |
| TC-AC-DS-213 | TC-AC-DS-E2E-062 | FE+BE |
| TC-AC-DS-214 | TC-AC-DS-E2E-062 | FE+BE |
| TC-AC-DS-215 | TC-AC-DS-E2E-062 | FE+BE |
| TC-AC-DS-216 | TC-AC-DS-E2E-062 | FE+BE |
| TC-AC-DS-217 | TC-AC-DS-E2E-063 | FE+BE |
| TC-AC-DS-218 | TC-AC-DS-E2E-063 | FE+BE |
| TC-AC-DS-219 | TC-AC-DS-E2E-060 | FE+BE |
| TC-AC-DS-220 | TC-AC-DS-E2E-063 | FE+BE |
| TC-AC-DS-221 | TC-AC-DS-E2E-063 | FE+BE |
| TC-AC-DS-222 | TC-AC-DS-E2E-063 | FE+BE |
| TC-AC-DS-223 | TC-AC-DS-E2E-064 | FE+BE |
| TC-AC-DS-224 | TC-AC-DS-E2E-064 | FE+BE |
| TC-AC-DS-225 | TC-AC-DS-E2E-064 | FE+BE |
| TC-AC-DS-226 | TC-AC-DS-E2E-065 | FE+BE |
| TC-AC-DS-227 | TC-AC-DS-E2E-065 | FE+BE |
| TC-AC-DS-228 | TC-AC-DS-E2E-065 | FE+BE |
| TC-AC-DS-229 | TC-AC-DS-E2E-169 | FE+BE |
| TC-AC-DS-230 | TC-AC-DS-E2E-172 | FE+BE |
| TC-AC-DS-231 | TC-AC-DS-E2E-074 | FE+BE |
| TC-AC-DS-232 | TC-AC-DS-E2E-074 | FE+BE |
| TC-AC-DS-233 | TC-AC-DS-E2E-163 | FE+BE |
| TC-AC-DS-234 | TC-AC-DS-E2E-163 | FE+BE |
| TC-AC-DS-235 | TC-AC-DS-E2E-163 | FE+BE |
| TC-AC-DS-236 | TC-AC-DS-E2E-163 | FE+BE |
| TC-AC-DS-237 | TC-AC-DS-E2E-074 | FE+BE |
| TC-AC-DS-238 | TC-AC-DS-E2E-164 | FE+BE |
| TC-AC-DS-239 | TC-AC-DS-E2E-058 | FE+BE |
| TC-AC-DS-240 | TC-AC-DS-E2E-071 | FE+BE |
| TC-AC-DS-241 | TC-AC-DS-E2E-071 | FE+BE |
| TC-AC-DS-242 | TC-AC-DS-E2E-071 | FE+BE |
| TC-AC-DS-243 | TC-AC-DS-E2E-072 | FE+BE |
| TC-AC-DS-244 | TC-AC-DS-E2E-072 | FE+BE |
| TC-AC-DS-245 | TC-AC-DS-E2E-072 | FE+BE |
| TC-AC-DS-246 | TC-AC-DS-E2E-072 | FE+BE |
| TC-AC-DS-247 | TC-AC-DS-E2E-072 | FE+BE |
| TC-AC-DS-248 | TC-AC-DS-E2E-073 | FE+BE |
| TC-AC-DS-249 | TC-AC-DS-E2E-073 | FE+BE |
| TC-AC-DS-250 | TC-AC-DS-E2E-188 | FE+BE |
| TC-AC-DS-251 | TC-AC-DS-E2E-188 | FE+BE |
| TC-AC-DS-252 | TC-AC-DS-E2E-170 | FE+BE |
| TC-AC-DS-253 | TC-AC-DS-E2E-170 | FE+BE |
| TC-AC-DS-254 | TC-AC-DS-E2E-053 | FE+BE |
| TC-AC-DS-255 | TC-AC-DS-E2E-075 | FE+BE |
| TC-AC-DS-256 | TC-AC-DS-E2E-078 | FE+BE |
| TC-AC-DS-257 | TC-AC-DS-E2E-075 | FE+BE |
| TC-AC-DS-258 | TC-AC-DS-E2E-075 | FE+BE |
| TC-AC-DS-259 | TC-AC-DS-E2E-075 | FE+BE |
| TC-AC-DS-260 | TC-AC-DS-E2E-076 | FE+BE |
| TC-AC-DS-261 | TC-AC-DS-E2E-076 | FE+BE |
| TC-AC-DS-262 | TC-AC-DS-E2E-076 | FE+BE |
| TC-AC-DS-263 | TC-AC-DS-E2E-076 | FE+BE |
| TC-AC-DS-264 | TC-AC-DS-E2E-077 | FE+BE |
| TC-AC-DS-265 | TC-AC-DS-E2E-077 | FE+BE |
| TC-AC-DS-266 | TC-AC-DS-E2E-077 | FE+BE |
| TC-AC-DS-267 | TC-AC-DS-E2E-077 | FE+BE |
| TC-AC-DS-268 | TC-AC-DS-E2E-170 | FE+BE |
| TC-AC-DS-269 | TC-AC-DS-E2E-170 | FE+BE |
| TC-AC-DS-270 | TC-AC-DS-E2E-078 | FE+BE |
| TC-AC-DS-271 | TC-AC-DS-E2E-078 | FE+BE |
| TC-AC-DS-272 | TC-AC-DS-E2E-079 | FE+BE |
| TC-AC-DS-273 | TC-AC-DS-E2E-079 | FE+BE |
| TC-AC-DS-274 | TC-AC-DS-E2E-079 | FE+BE |
| TC-AC-DS-275 | TC-AC-DS-E2E-080 | FE+BE |
| TC-AC-DS-276 | TC-AC-DS-E2E-080 | FE+BE |
| TC-AC-DS-277 | TC-AC-DS-E2E-174 | FE+BE |
| TC-AC-DS-278 | TC-AC-DS-E2E-174 | FE+BE |
| TC-AC-DS-279 | TC-AC-DS-E2E-174 | FE+BE |
| TC-AC-DS-280 | TC-AC-DS-E2E-080 | FE+BE |
| TC-AC-DS-281 | TC-AC-DS-E2E-081 | FE+BE |
| TC-AC-DS-282 | TC-AC-DS-E2E-081 | FE+BE |
| TC-AC-DS-283 | TC-AC-DS-E2E-081 | FE+BE |
| TC-AC-DS-284 | TC-AC-DS-E2E-081 | FE+BE |
| TC-AC-DS-285 | TC-AC-DS-E2E-083 | FE+BE |
| TC-AC-DS-286 | TC-AC-DS-E2E-082 | FE+BE |
| TC-AC-DS-287 | TC-AC-DS-E2E-082 | FE+BE |
| TC-AC-DS-288 | TC-AC-DS-E2E-082 | FE+BE |
| TC-AC-DS-289 | TC-AC-DS-E2E-083 | FE+BE |
| TC-AC-DS-290 | TC-AC-DS-E2E-083 | FE+BE |
| TC-AC-DS-291 | TC-AC-DS-E2E-083 | FE+BE |
| TC-AC-DS-292 | TC-AC-DS-E2E-084 | FE+BE |
| TC-AC-DS-293 | TC-AC-DS-E2E-189 | FE+BE |
| TC-AC-DS-294 | TC-AC-DS-E2E-189 | FE+BE |
| TC-AC-DS-295 | TC-AC-DS-E2E-171 | FE+BE |
| TC-AC-DS-296 | TC-AC-DS-E2E-171 | FE+BE |
| TC-AC-DS-297 | TC-AC-DS-E2E-081 | FE+BE |
| TC-AC-DS-298 | TC-AC-DS-E2E-087 | FE+BE |
| TC-AC-DS-299 | TC-AC-DS-E2E-087 | FE+BE |
| TC-AC-DS-300 | TC-AC-DS-E2E-087 | FE+BE |
| TC-AC-DS-301 | TC-AC-DS-E2E-087 | FE+BE |
| TC-AC-DS-302 | TC-AC-DS-E2E-088 | FE+BE |
| TC-AC-DS-303 | TC-AC-DS-E2E-088 | FE+BE |
| TC-AC-DS-304 | TC-AC-DS-E2E-088 | FE+BE |
| TC-AC-DS-305 | TC-AC-DS-E2E-089 | FE+BE |
| TC-AC-DS-306 | TC-AC-DS-E2E-089 | FE+BE |
| TC-AC-DS-307 | TC-AC-DS-E2E-089 | FE+BE |
| TC-AC-DS-308 | TC-AC-DS-E2E-088 | FE+BE |
| TC-AC-DS-309 | TC-AC-DS-E2E-165 | FE+BE |
| TC-AC-DS-310 | TC-AC-DS-E2E-088 | FE+BE |
| TC-AC-DS-311 | TC-AC-DS-E2E-090 | FE+BE |
| TC-AC-DS-312 | TC-AC-DS-E2E-090 | FE+BE |
| TC-AC-DS-313 | TC-AC-DS-E2E-090 | FE+BE |
| TC-AC-DS-314 | TC-AC-DS-E2E-091 | FE+BE |
| TC-AC-DS-315 | TC-AC-DS-E2E-091 | FE+BE |
| TC-AC-DS-316 | TC-AC-DS-E2E-091 | FE+BE |
| TC-AC-DS-317 | TC-AC-DS-E2E-092 | FE+BE |
| TC-AC-DS-318 | TC-AC-DS-E2E-092 | FE+BE |
| TC-AC-DS-319 | TC-AC-DS-E2E-092 | FE+BE |
| TC-AC-DS-320 | TC-AC-DS-E2E-092 | FE+BE |
| TC-AC-DS-321 | TC-AC-DS-E2E-093 | FE+BE |
| TC-AC-DS-322 | TC-AC-DS-E2E-090 | FE+BE |
| TC-AC-DS-323 | TC-AC-DS-E2E-093 | FE+BE |
| TC-AC-DS-324 | TC-AC-DS-E2E-093 | FE+BE |
| TC-AC-DS-325 | TC-AC-DS-E2E-094 | FE+BE |
| TC-AC-DS-326 | TC-AC-DS-E2E-094 | FE+BE |
| TC-AC-DS-327 | TC-AC-DS-E2E-096 | FE+BE |
| TC-AC-DS-328 | TC-AC-DS-E2E-096 | FE+BE |
| TC-AC-DS-329 | TC-AC-DS-E2E-096 | FE+BE |
| TC-AC-DS-330 | TC-AC-DS-E2E-097 | FE+BE |
| TC-AC-DS-331 | TC-AC-DS-E2E-097 | FE+BE |
| TC-AC-DS-332 | TC-AC-DS-E2E-097 | FE+BE |
| TC-AC-DS-333 | TC-AC-DS-E2E-094 | FE+BE |
| TC-AC-DS-334 | TC-AC-DS-E2E-094 | FE+BE |
| TC-AC-DS-335 | TC-AC-DS-E2E-190 | FE+BE |
| TC-AC-DS-336 | TC-AC-DS-E2E-098 | FE+BE |
| TC-AC-DS-337 | TC-AC-DS-E2E-098 | FE+BE |
| TC-AC-DS-338 | TC-AC-DS-E2E-191 | FE+BE |
| TC-AC-DS-339 | TC-AC-DS-E2E-099 | FE+BE |
| TC-AC-DS-340 | TC-AC-DS-E2E-099 | FE+BE |
| TC-AC-DS-341 | TC-AC-DS-E2E-099 | FE+BE |
| TC-AC-DS-342 | TC-AC-DS-E2E-100 | FE+BE |
| TC-AC-DS-343 | TC-AC-DS-E2E-100 | FE+BE |
| TC-AC-DS-344 | TC-AC-DS-E2E-100 | FE+BE |
| TC-AC-DS-345 | TC-AC-DS-E2E-100 | FE+BE |
| TC-AC-DS-346 | TC-AC-DS-E2E-101 | FE+BE |
| TC-AC-DS-347 | TC-AC-DS-E2E-101 | FE+BE |
| TC-AC-DS-348 | TC-AC-DS-E2E-101 | FE+BE |
| TC-AC-DS-349 | TC-AC-DS-E2E-102 | FE+BE |
| TC-AC-DS-350 | TC-AC-DS-E2E-103 | FE+BE |
| TC-AC-DS-351 | TC-AC-DS-E2E-104 | FE+BE |
| TC-AC-DS-352 | TC-AC-DS-E2E-102 | FE+BE |
| TC-AC-DS-353 | TC-AC-DS-E2E-104 | FE+BE |
| TC-AC-DS-354 | TC-AC-DS-E2E-105 | FE+BE |
| TC-AC-DS-355 | TC-AC-DS-E2E-105 | FE+BE |
| TC-AC-DS-356 | TC-AC-DS-E2E-105 | FE+BE |
| TC-AC-DS-357 | TC-AC-DS-E2E-106 | FE+BE |
| TC-AC-DS-358 | TC-AC-DS-E2E-103 | FE+BE |
| TC-AC-DS-359 | TC-AC-DS-E2E-106 | FE+BE |
| TC-AC-DS-360 | TC-AC-DS-E2E-106 | FE+BE |
| TC-AC-DS-361 | TC-AC-DS-E2E-106 | FE+BE |
| TC-AC-DS-362 | TC-AC-DS-E2E-107 | FE+BE |
| TC-AC-DS-363 | TC-AC-DS-E2E-107 | FE+BE |
| TC-AC-DS-364 | TC-AC-DS-E2E-107 | FE+BE |
| TC-AC-DS-365 | TC-AC-DS-E2E-107 | FE+BE |
| TC-AC-DS-366 | TC-AC-DS-E2E-108 | FE+BE |
| TC-AC-DS-367 | TC-AC-DS-E2E-108 | FE+BE |
| TC-AC-DS-368 | TC-AC-DS-E2E-108 | FE+BE |
| TC-AC-DS-369 | TC-AC-DS-E2E-108 | FE+BE |
| TC-AC-DS-370 | TC-AC-DS-E2E-109 | FE+BE |
| TC-AC-DS-371 | TC-AC-DS-E2E-109 | FE+BE |
| TC-AC-DS-372 | TC-AC-DS-E2E-109 | FE+BE |
| TC-AC-DS-373 | TC-AC-DS-E2E-110 | FE+BE |
| TC-AC-DS-374 | TC-AC-DS-E2E-176 | FE+BE |
| TC-AC-DS-375 | TC-AC-DS-E2E-110 | FE+BE |
| TC-AC-DS-376 | TC-AC-DS-E2E-167 | FE+BE |
| TC-AC-DS-377 | TC-AC-DS-E2E-110 | FE+BE |
| TC-AC-DS-378 | TC-AC-DS-E2E-175 | FE+BE |
| TC-AC-DS-379 | TC-AC-DS-E2E-175 | FE+BE |
| TC-AC-DS-380 | TC-AC-DS-E2E-111 | FE+BE |
| TC-AC-DS-381 | TC-AC-DS-E2E-111 | FE+BE |
| TC-AC-DS-382 | TC-AC-DS-E2E-111 | FE+BE |
| TC-AC-DS-383 | TC-AC-DS-E2E-112 | FE+BE |
| TC-AC-DS-384 | TC-AC-DS-E2E-112 | FE+BE |
| TC-AC-DS-385 | TC-AC-DS-E2E-113 | FE+BE |
| TC-AC-DS-386 | TC-AC-DS-E2E-112 | FE+BE |
| TC-AC-DS-387 | TC-AC-DS-E2E-166 | FE+BE |
| TC-AC-DS-388 | TC-AC-DS-E2E-112 | FE+BE |
| TC-AC-DS-389 | TC-AC-DS-E2E-113 | FE+BE |
| TC-AC-DS-390 | TC-AC-DS-E2E-112 | FE+BE |
| TC-AC-DS-391 | TC-AC-DS-E2E-114 | FE+BE |
| TC-AC-DS-392 | TC-AC-DS-E2E-114 | FE+BE |
| TC-AC-DS-393 | TC-AC-DS-E2E-114 | FE+BE |
| TC-AC-DS-394 | TC-AC-DS-E2E-115 | FE+BE |
| TC-AC-DS-395 | TC-AC-DS-E2E-115 | FE+BE |
| TC-AC-DS-396 | TC-AC-DS-E2E-115 | FE+BE |
| TC-AC-DS-397 | TC-AC-DS-E2E-116 | FE+BE |
| TC-AC-DS-398 | TC-AC-DS-E2E-116 | FE+BE |
| TC-AC-DS-399 | TC-AC-DS-E2E-117 | FE+BE |
| TC-AC-DS-400 | TC-AC-DS-E2E-117 | FE+BE |
| TC-AC-DS-401 | TC-AC-DS-E2E-118 | FE+BE |
| TC-AC-DS-402 | TC-AC-DS-E2E-118 | FE+BE |
| TC-AC-DS-403 | TC-AC-DS-E2E-118 | FE+BE |
| TC-AC-DS-404 | TC-AC-DS-E2E-119 | FE+BE |
| TC-AC-DS-405 | TC-AC-DS-E2E-119 | FE+BE |
| TC-AC-DS-406 | TC-AC-DS-E2E-119 | FE+BE |
| TC-AC-DS-407 | TC-AC-DS-E2E-119 | FE+BE |
| TC-AC-DS-408 | TC-AC-DS-E2E-121 | FE+BE |
| TC-AC-DS-409 | TC-AC-DS-E2E-121 | FE+BE |
| TC-AC-DS-410 | TC-AC-DS-E2E-122 | FE+BE |
| TC-AC-DS-411 | TC-AC-DS-E2E-122 | FE+BE |
| TC-AC-DS-412 | TC-AC-DS-E2E-123 | FE+BE |
| TC-AC-DS-413 | TC-AC-DS-E2E-123 | FE+BE |
| TC-AC-DS-414 | TC-AC-DS-E2E-192 | FE+BE |
| TC-AC-DS-415 | TC-AC-DS-E2E-124 | FE+BE |
| TC-AC-DS-416 | TC-AC-DS-E2E-125 | FE+BE |
| TC-AC-DS-417 | TC-AC-DS-E2E-124 | FE+BE |
| TC-AC-DS-418 | TC-AC-DS-E2E-126 | FE+BE |
| TC-AC-DS-419 | TC-AC-DS-E2E-126 | FE+BE |
| TC-AC-DS-420 | TC-AC-DS-E2E-126 | FE+BE |
| TC-AC-DS-421 | TC-AC-DS-E2E-127 | FE+BE |
| TC-AC-DS-422 | TC-AC-DS-E2E-127 | FE+BE |
| TC-AC-DS-423 | TC-AC-DS-E2E-176 | FE+BE |
| TC-AC-DS-424 | TC-AC-DS-E2E-167 | FE+BE |
| TC-AC-DS-425 | TC-AC-DS-E2E-127 | FE+BE |
| TC-AC-DS-426 | TC-AC-DS-E2E-128 | FE+BE |
| TC-AC-DS-427 | TC-AC-DS-E2E-128 | FE+BE |
| TC-AC-DS-428 | TC-AC-DS-E2E-128 | FE+BE |
| TC-AC-DS-429 | TC-AC-DS-E2E-128 | FE+BE |
| TC-AC-DS-430 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-431 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-432 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-433 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-434 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-435 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-436 | TC-AC-DS-E2E-130 | FE+BE |
| TC-AC-DS-437 | TC-AC-DS-E2E-130 | FE+BE |
| TC-AC-DS-438 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-439 | TC-AC-DS-E2E-135 | FE+BE |
| TC-AC-DS-440 | TC-AC-DS-E2E-166 | FE+BE |
| TC-AC-DS-441 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-442 | TC-AC-DS-E2E-129 | FE+BE |
| TC-AC-DS-443 | TC-AC-DS-E2E-131 | FE+BE |
| TC-AC-DS-444 | TC-AC-DS-E2E-131 | FE+BE |
| TC-AC-DS-445 | TC-AC-DS-E2E-131 | FE+BE |
| TC-AC-DS-446 | TC-AC-DS-E2E-132 | FE+BE |
| TC-AC-DS-447 | TC-AC-DS-E2E-132 | FE+BE |
| TC-AC-DS-448 | TC-AC-DS-E2E-132 | FE+BE |
| TC-AC-DS-449 | TC-AC-DS-E2E-133 | FE+BE |
| TC-AC-DS-450 | TC-AC-DS-E2E-133 | FE+BE |
| TC-AC-DS-451 | TC-AC-DS-E2E-134 | FE+BE |
| TC-AC-DS-452 | TC-AC-DS-E2E-134 | FE+BE |
| TC-AC-DS-453 | TC-AC-DS-E2E-134 | FE+BE |
| TC-AC-DS-454 | TC-AC-DS-E2E-137 | FE+BE |
| TC-AC-DS-455 | TC-AC-DS-E2E-137 | FE+BE |
| TC-AC-DS-456 | TC-AC-DS-E2E-137 | FE+BE |
| TC-AC-DS-457 | TC-AC-DS-E2E-138 | FE+BE |
| TC-AC-DS-458 | TC-AC-DS-E2E-138 | FE+BE |
| TC-AC-DS-459 | TC-AC-DS-E2E-139 | FE+BE |
| TC-AC-DS-460 | TC-AC-DS-E2E-139 | FE+BE |
| TC-AC-DS-461 | TC-AC-DS-E2E-139 | FE+BE |
| TC-AC-DS-462 | TC-AC-DS-E2E-140 | FE+BE |
| TC-AC-DS-463 | TC-AC-DS-E2E-141 | FE+BE |
| TC-AC-DS-464 | TC-AC-DS-E2E-176 | FE+BE |
| TC-AC-DS-465 | TC-AC-DS-E2E-167 | FE+BE |
| TC-AC-DS-466 | TC-AC-DS-E2E-141 | FE+BE |
| TC-AC-DS-467 | TC-AC-DS-E2E-142 | FE+BE |
| TC-AC-DS-468 | TC-AC-DS-E2E-142 | FE+BE |
| TC-AC-DS-469 | TC-AC-DS-E2E-142 | FE+BE |
| TC-AC-DS-470 | TC-AC-DS-E2E-143 | FE+BE |
| TC-AC-DS-471 | TC-AC-DS-E2E-143 | FE+BE |
| TC-AC-DS-472 | TC-AC-DS-E2E-143 | FE+BE |
| TC-AC-DS-473 | TC-AC-DS-E2E-144 | FE+BE |
| TC-AC-DS-474 | TC-AC-DS-E2E-144 | FE+BE |
| TC-AC-DS-475 | TC-AC-DS-E2E-144 | FE+BE |
| TC-AC-DS-476 | TC-AC-DS-E2E-145 | FE+BE |
| TC-AC-DS-477 | TC-AC-DS-E2E-145 | FE+BE |
| TC-AC-DS-478 | TC-AC-DS-E2E-193 | FE+BE |
| TC-AC-DS-479 | TC-AC-DS-E2E-146 | FE+BE |
| TC-AC-DS-480 | TC-AC-DS-E2E-146 | FE+BE |
| TC-AC-DS-481 | TC-AC-DS-E2E-146 | FE+BE |
| TC-AC-DS-482 | TC-AC-DS-E2E-151 | FE+BE |
| TC-AC-DS-483 | TC-AC-DS-E2E-145 | FE+BE |
| TC-AC-DS-484 | TC-AC-DS-E2E-151 | FE+BE |
| TC-AC-DS-485 | TC-AC-DS-E2E-147 | FE+BE |
| TC-AC-DS-486 | TC-AC-DS-E2E-147 | FE+BE |
| TC-AC-DS-487 | TC-AC-DS-E2E-147 | FE+BE |
| TC-AC-DS-488 | TC-AC-DS-E2E-148 | FE+BE |
| TC-AC-DS-489 | TC-AC-DS-E2E-148 | FE+BE |
| TC-AC-DS-490 | TC-AC-DS-E2E-148 | FE+BE |
| TC-AC-DS-491 | TC-AC-DS-E2E-149 | FE+BE |
| TC-AC-DS-492 | TC-AC-DS-E2E-149 | FE+BE |
| TC-AC-DS-493 | TC-AC-DS-E2E-149 | FE+BE |
| TC-AC-DS-494 | TC-AC-DS-E2E-150 | FE+BE |
| TC-AC-DS-495 | TC-AC-DS-E2E-193 | FE+BE |
| TC-AC-DS-496 | TC-AC-DS-E2E-154 | FE+BE |
| TC-AC-DS-497 | TC-AC-DS-E2E-154 | FE+BE |
| TC-AC-DS-498 | TC-AC-DS-E2E-155 | FE+BE |
| TC-AC-DS-499 | TC-AC-DS-E2E-155 | FE+BE |
| TC-AC-DS-500 | TC-AC-DS-E2E-194 | FE+BE |
| TC-AC-DS-501 | TC-AC-DS-E2E-156 | FE+BE |
| TC-AC-DS-502 | TC-AC-DS-E2E-156 | FE+BE |
| TC-AC-DS-503 | TC-AC-DS-E2E-156 | FE+BE |
| TC-AC-DS-504 | TC-AC-DS-E2E-157 | FE+BE |
| TC-AC-DS-505 | TC-AC-DS-E2E-157 | FE+BE |
| TC-AC-DS-506 | TC-AC-DS-E2E-157 | FE+BE |
| TC-AC-DS-507 | TC-AC-DS-E2E-157 | FE+BE |
| TC-AC-DS-508 | TC-AC-DS-E2E-195 | FE+BE |
| TC-AC-DS-509 | TC-AC-DS-E2E-158 | FE+BE |
| TC-AC-DS-510 | TC-AC-DS-E2E-158 | FE+BE |
| TC-AC-DS-511 | TC-AC-DS-E2E-158 | FE+BE |
| TC-AC-DS-512 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-513 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-514 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-515 | TC-AC-DS-E2E-160 | FE+BE |
| TC-AC-DS-516 | TC-AC-DS-E2E-160 | FE+BE |
| TC-AC-DS-517 | TC-AC-DS-E2E-160 | FE+BE |
| TC-AC-DS-518 | TC-AC-DS-E2E-160 | FE+BE |
| TC-AC-DS-519 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-520 | TC-AC-DS-E2E-161 | FE+BE |
| TC-AC-DS-521 | TC-AC-DS-E2E-161 | FE+BE |
| TC-AC-DS-522 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-523 | TC-AC-DS-E2E-162 | FE+BE |
| TC-AC-DS-524 | TC-AC-DS-E2E-162 | FE+BE |
| TC-AC-DS-525 | TC-AC-DS-E2E-162 | FE+BE |
| TC-AC-DS-526 | TC-AC-DS-E2E-165 | FE+BE |
| TC-AC-DS-527 | TC-AC-DS-E2E-164 | FE+BE |
| TC-AC-DS-528 | TC-AC-DS-E2E-161 | FE+BE |
| TC-AC-DS-529 | TC-AC-DS-E2E-164 | FE+BE |
| TC-AC-DS-530 | TC-AC-DS-E2E-165 | FE+BE |
| TC-AC-DS-531 | TC-AC-DS-E2E-165 | FE+BE |
| TC-AC-DS-532 | TC-AC-DS-E2E-178 | FE+BE |
| TC-AC-DS-533 | TC-AC-DS-E2E-179 | FE+BE |
| TC-AC-DS-534 | TC-AC-DS-E2E-180 | FE+BE |
| TC-AC-DS-535 | TC-AC-DS-E2E-181 | FE+BE |
| TC-AC-DS-536 | TC-AC-DS-E2E-178 | FE+BE |
| TC-AC-DS-537 | TC-AC-DS-E2E-179 | FE+BE |
| TC-AC-DS-538 | TC-AC-DS-E2E-180 | FE+BE |
| TC-AC-DS-539 | TC-AC-DS-E2E-181 | FE+BE |
| TC-AC-DS-540 | TC-AC-DS-E2E-178 | FE+BE |
| TC-AC-DS-541 | TC-AC-DS-E2E-180 | FE+BE |
| TC-AC-DS-542 | TC-AC-DS-E2E-173 | FE+BE |
| TC-AC-DS-543 | TC-AC-DS-E2E-173 | FE+BE |
| TC-AC-DS-544 | TC-AC-DS-E2E-085 | FE+BE |
| TC-AC-DS-545 | TC-AC-DS-E2E-085 | FE+BE |
| TC-AC-DS-546 | TC-AC-DS-E2E-085 | FE+BE |
| TC-AC-DS-547 | TC-AC-DS-E2E-086 | FE+BE |
| TC-AC-DS-548 | TC-AC-DS-E2E-171 | FE+BE |
| TC-AC-DS-549 | TC-AC-DS-E2E-183 | FE+BE |
| TC-AC-DS-550 | TC-AC-DS-E2E-183 | FE+BE |
| TC-AC-DS-551 | TC-AC-DS-E2E-183 | FE+BE |
| TC-AC-DS-552 | TC-AC-DS-E2E-183 | FE+BE |
| TC-AC-DS-553 | TC-AC-DS-E2E-152 | FE+BE |
| TC-AC-DS-554 | TC-AC-DS-E2E-153 | FE+BE |
| TC-AC-DS-555 | TC-AC-DS-E2E-082 | FE+BE |
| TC-AC-DS-556 | TC-AC-DS-E2E-083 | FE+BE |
| TC-AC-DS-557 | TC-AC-DS-E2E-011 | FE+BE |
| TC-AC-DS-558 | TC-AC-DS-E2E-011 | FE+BE |
| TC-AC-DS-559 | TC-AC-DS-E2E-182 | FE+BE |
| TC-AC-DS-560 | TC-AC-DS-E2E-132 | FE+BE |
| TC-AC-DS-561 | TC-AC-DS-E2E-135 | FE+BE |
| TC-AC-DS-562 | TC-AC-DS-E2E-135 | FE+BE |
| TC-AC-DS-563 | TC-AC-DS-E2E-135 | FE+BE |
| TC-AC-DS-564 | TC-AC-DS-E2E-133 | FE+BE |
| TC-AC-DS-565 | TC-AC-DS-E2E-116 | FE+BE |
| TC-AC-DS-566 | TC-AC-DS-E2E-120 | FE+BE |
| TC-AC-DS-567 | TC-AC-DS-E2E-120 | FE+BE |
| TC-AC-DS-568 | TC-AC-DS-E2E-125 | FE+BE |
| TC-AC-DS-569 | TC-AC-DS-E2E-130 | FE+BE |
| TC-AC-DS-570 | TC-AC-DS-E2E-002 | FE+BE |
| TC-AC-DS-571 | TC-AC-DS-E2E-133 | FE+BE |
| TC-AC-DS-572 | TC-AC-DS-E2E-052 | FE+BE |
| TC-AC-DS-573 | TC-AC-DS-E2E-073 | FE+BE |
| TC-AC-DS-574 | TC-AC-DS-E2E-086 | FE+BE |
| TC-AC-DS-575 | TC-AC-DS-E2E-010 | FE+BE |
| TC-AC-DS-576 | TC-AC-DS-E2E-009 | FE+BE |
| TC-AC-DS-577 | TC-AC-DS-E2E-177 | FE+BE |
| TC-AC-DS-578 | TC-AC-DS-E2E-177 | FE+BE |
| TC-AC-DS-579 | TC-AC-DS-E2E-110 | FE+BE |
| TC-AC-DS-580 | TC-AC-DS-E2E-030 | FE+BE |
| TC-AC-DS-581 | TC-AC-DS-E2E-030 | FE+BE |
| TC-AC-DS-582 | TC-AC-DS-E2E-060 | FE+BE |
| TC-AC-DS-583 | TC-AC-DS-E2E-150 | FE+BE |
| TC-AC-DS-584 | TC-AC-DS-E2E-150 | FE+BE |
| TC-AC-DS-585 | TC-AC-DS-E2E-140 | FE+BE |
| TC-AC-DS-586 | TC-AC-DS-E2E-140 | FE+BE |
| TC-AC-DS-587 | TC-AC-DS-E2E-136 | FE+BE |
| TC-AC-DS-588 | TC-AC-DS-E2E-136 | FE+BE |
| TC-AC-DS-589 | TC-AC-DS-E2E-165 | FE+BE |
| TC-AC-DS-590 | TC-AC-DS-E2E-164 | FE+BE |
| TC-AC-DS-591 | TC-AC-DS-E2E-095 | FE+BE |
| TC-AC-DS-592 | TC-AC-DS-E2E-095 | FE+BE |
| TC-AC-DS-593 | TC-AC-DS-E2E-095 | FE+BE |
| TC-AC-DS-594 | TC-AC-DS-E2E-029 | FE+BE |
| TC-AC-DS-595 | TC-AC-DS-E2E-174 | FE+BE |
| TC-AC-DS-596 | TC-AC-DS-E2E-026 | FE+BE |
| TC-AC-DS-597 | TC-AC-DS-E2E-127 | FE+BE |
| TC-AC-DS-598 | TC-AC-DS-E2E-141 | FE+BE |
| TC-AC-DS-599 | TC-AC-DS-E2E-117 | FE+BE |
| TC-AC-DS-600 | TC-AC-DS-E2E-013 | FE+BE |
| TC-AC-DS-601 | TC-AC-DS-E2E-013 | FE+BE |
| TC-AC-DS-602 | TC-AC-DS-E2E-109 | FE+BE |
| TC-AC-DS-603 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-604 | TC-AC-DS-E2E-159 | FE+BE |
| TC-AC-DS-605 | TC-AC-DS-E2E-161 | FE+BE |
| TC-AC-DS-606 | TC-AC-DS-E2E-059 | FE+BE |
