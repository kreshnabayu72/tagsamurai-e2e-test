# Coverage E2E — Admin Console > Settings > Device Category

Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (308 ID `TC-AC-DC-1`–`308`, semua aktif). Suite: `specs/AdminConsole/SettingsDeviceCategory/`. Prefix: `AC` + `DC` (`TC-AC-DC-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). TC backend (`tc-settings-device-category-backend.md`) memakai namespace `TC-AC-DC-BE-*` terpisah.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 308 TC aktif masuk 98 spec; tidak ada TC hanya-BE. Setiap TC terpetakan ke tepat satu spec.

## TC hanya-BE (tidak masuk spec)

Tidak ada. Section 8 (defense-in-depth) tetap masuk spec karena Expected berupa respons API yang masih berada dalam lingkup K-1.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-DC-E2E-001-screening-sidebar-struktur-urutan | Screening Sidebar Category: Header, Body, Footer, Struktur Node Bawaan, Bold Hardcoded, dan Urutan A-Z pada Device Name dan Device SKU | FE+BE | 30 | 1, 2, 3, 4, 5 |
| TC-AC-DC-E2E-002-screening-sidebar-node-panjang-dan-klik | Screening Sidebar Category: Klik Nama dan Panah Node Hanya Expand/Collapse, Drag and Drop Tidak Mengubah Urutan, dan Nama 120 Karakter Terpotong dengan Tooltip | FE+BE | 30 | 6, 7, 8, 303 |
| TC-AC-DC-E2E-003-screening-sidebar-all-categories-dan-tooltip | Screening Sidebar Category: Baris All Categories dan Tooltip Aksi Node serta Ikon Changelog | FE+BE | 23 | 286, 287, 11 |
| TC-AC-DC-E2E-004-aksesibilitas-keyboard-tree | Aksesibilitas Tree Category: Navigasi Keyboard, Pengumuman Error Inline Polite, Fokus Dialog Terjebak, dan Tooltip Aksi saat Fokus Keyboard | FE+BE | 24 | 9, 10, 279 |
| TC-AC-DC-E2E-005-pencarian-tree-dan-expand-collapse | Sidebar Category: State Loading Tree, Toggle Expand/Collapse All, Pencarian Tree, dan Pencarian Tanpa Hasil | FE+BE (penundaan respons memakai `Spectra | 24 | 12, 14, 15, 16 |
| TC-AC-DC-E2E-006-pencarian-tree-dan-pilihan-node | Pencarian Tree Category dan Pilihan Node: Centang Parent Memilih Descendant Tersembunyi, Teks Pencarian dan Pilihan Dipertahankan antar Sub-tab | FE+BE | 23 | 299, 307 |
| TC-AC-DC-E2E-007-floating-toggle-sidebar | Floating Open/Collapse Toggle Button Sidebar Category: Tutup dan Buka, Persistensi per User, dan State Independen per Halaman | FE+BE | 31 | 17, 18, 19 |
| TC-AC-DC-E2E-008-filter-category-pilihan-node | Filter Category pada Device Name: Pilih Node Leaf, Parent, Node Tengah, Dua Cabang, Pilihan Kosong, Handheld Reader, dan Node Tanpa Data | FE+BE | 34 | 22, 23, 24, 26, 27, 28, 35 |
| TC-AC-DC-E2E-009-filter-category-persistensi-dan-all-categories | Filter Category: All Categories Melepas Pilihan, Pilihan Dipertahankan antar Sub-tab, dan Device SKU Difilter lewat Device Name Induk | FE+BE | 26 | 285, 30, 31 |
| TC-AC-DC-E2E-010-filter-category-tri-state-dasar | Filter Category Tri-State Dasar: Partial-Check Parent, Centang dan Hapus Centang Hardware, Hardware Partial-Check Dipilih Penuh | FE+BE | 30 | 25, 29, 290, 291 |
| TC-AC-DC-E2E-011-filter-category-tri-state-device-name-parent | Filter Category Tri-State: Hardware Partial-Check Dipilih Penuh, Parent Partial-Check dan Tercentang Penuh pada Device Name yang Merujuk Parent | FE+BE | 30 | 292, 294, 295, 296 |
| TC-AC-DC-E2E-012-filter-category-tri-state-bottom-up | Filter Category Tri-State Bottom-Up: Parent Tercentang Penuh bila Seluruh Anak Dipilih dan Node ber-Device Name yang Mendapat Anak | FE+BE | 30 | 297, 298, 301 |
| TC-AC-DC-E2E-013-filter-category-perubahan-tree | Filter Category saat Tree Berubah: Child Baru, Hapus Node Terpilih, Hapus Ancestor Node Terpilih, dan Rename Node Terpilih | FE+BE | 40 | 32, 33, 34, 282 |
| TC-AC-DC-E2E-014-mobile-android-sidebar-dan-filter | Mobile Android: Sidebar Category Tampil lewat Floating Toggle, Aksi per Node, Filter Langsung Berlaku, All Categories, dan Changelog sebagai Bottom Sheet | FE+BE | 26 | 37, 38, 41, 40 |
| TC-AC-DC-E2E-015-mobile-android-crud-dan-read-only | Mobile Android: Add dan Edit Memakai Input Inline, Delete dan Unsaved Changes sebagai Bottom Sheet, serta Read Only Tanpa Ikon Aksi | FE+BE | 30 | 42, 302, 39 |
| TC-AC-DC-E2E-016-role-matrix-negatif-entity-distributor | Role Matrix Negatif: Akses Entity Distributor ke Category | FE+BE | 20 | 44, 45, 280 |
| TC-AC-DC-E2E-017-role-matrix-negatif-partner-client-tanpa-capability | Role Matrix Negatif: Partner, Client, dan Principal Tanpa Capability Ditolak | FE+BE | 23 | 46, 47, 48, 49 |
| TC-AC-DC-E2E-018-role-matrix-visibilitas-aksi-per-role | Role Matrix: Visibilitas Aksi Node Category untuk Total Control, Default User, dan Full CRUD | FE+BE | 27 | 43, 50, 51, 56 |
| TC-AC-DC-E2E-019-role-matrix-positif-add-create-only | Role Matrix Positif: Add Subcategory untuk Create-Only | FE+BE | 19 | 53, 61 |
| TC-AC-DC-E2E-020-role-matrix-positif-edit-update-only | Role Matrix Positif: Edit Category untuk Update-Only | FE+BE | 11 | 54, 59 |
| TC-AC-DC-E2E-021-role-matrix-positif-delete-delete-only | Role Matrix Positif: Delete Category untuk Delete-Only | FE+BE | 11 | 55, 60 |
| TC-AC-DC-E2E-022-role-matrix-node-hardcoded | Role Matrix: Aksi pada Node Hardcoded Hardware, TAG, dan Node Perantara untuk Total Control | FE+BE | 12 | 57, 58 |
| TC-AC-DC-E2E-023-defense-request-langsung-server | Defense-in-Depth: Request Langsung terhadap Node Hardcoded Ditolak Server | FE+BE | 25 | 241, 242, 243 |
| TC-AC-DC-E2E-024-defense-bypass-filter-fe-dan-markup | Defense-in-Depth: Bypass Filter FE (Emoji) dan Markup pada Nama Category | FE+BE | 38 | 85, 106, 254 |
| TC-AC-DC-E2E-025-defense-request-langsung-per-role-dan-entity | Defense-in-Depth: Request Langsung per Role dan Entity Ditolak 403 | FE+BE | 34 | 244, 245, 246, 247, 248, 249 |
| TC-AC-DC-E2E-026-add-screening-dan-berhasil | Add Subcategory: Screening Input Inline dan Add Berhasil | FE+BE | 33 | 62, 63, 64, 65 |
| TC-AC-DC-E2E-027-add-urutan-dan-parent-hardcoded | Add Subcategory: Urutan A-Z, Parent Hardcoded, Parent Dirujuk Device Name, dan Sub-tab Device SKU | FE+BE | 30 | 66, 67, 68, 269 |
| TC-AC-DC-E2E-028-add-state-submitting-dan-pencarian-aktif | Add Subcategory: State Submitting, Klik Ganda Submit, dan Pencarian Tree Aktif | FE+BE | 25 | 95, 96, 306 |
| TC-AC-DC-E2E-029-add-validasi-wajib-dan-batas | Add Subcategory: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Enter Tidak Men-submit | FE+BE | 31 | 79, 81, 90, 78 |
| TC-AC-DC-E2E-030-add-validasi-duplikat | Add Subcategory: Validasi Nama Duplikat pada Parent yang Sama dan Nama Sama pada Parent Berbeda | FE+BE | 28 | 86, 87, 88, 89 |
| TC-AC-DC-E2E-031-add-validasi-trim-dan-karakter | Add Subcategory: Batas 120 Karakter, Auto-trim Spasi Tepi, dan Emoji Diblok | FE+BE | 28 | 80, 82, 83, 84 |
| TC-AC-DC-E2E-032-add-hierarchy-depth-limit | Add Subcategory: Batas Hierarchy Depth Limit | FE+BE | 12 | 91, 92 |
| TC-AC-DC-E2E-033-add-unsaved-clear-dan-esc | Add Subcategory: Clear Field, Esc pada Input Bersih, Input Kembali Kosong, dan Esc dengan Perubahan | FE+BE | 32 | 69, 70, 263, 71 |
| TC-AC-DC-E2E-034-add-unsaved-dialog-leave-cancel | Add Subcategory: Dialog Unsaved Changes, Leave, Cancel, dan Esc pada Dialog | FE+BE | 33 | 72, 73, 257, 265 |
| TC-AC-DC-E2E-035-add-unsaved-reload-dan-navigasi | Add Subcategory: Reload Halaman dan Navigasi Internal dengan Input Berisi Perubahan | FE+BE | 37 | 74, 75, 76, 77 |
| TC-AC-DC-E2E-036-add-unsaved-klik-aksi-lain-dan-back | Add Subcategory: Dialog Unsaved Changes saat Klik Aksi Node Lain, Klik Area Luar Tree, dan Tombol Back Browser | FE+BE | 31 | 259, 260, 267 |
| TC-AC-DC-E2E-037-edit-screening-dan-berhasil | Edit Category: Screening Input Inline dan Edit Berhasil | FE+BE | 34 | 98, 99, 308, 100 |
| TC-AC-DC-E2E-038-edit-case-only-submitting-dan-klik-ganda | Edit Category: Perubahan Huruf Besar-Kecil Saja, State Submitting, dan Klik Ganda Save | FE+BE | 31 | 114, 124, 125 |
| TC-AC-DC-E2E-039-edit-validasi-wajib-batas-duplikat | Edit Category: Validasi Nama Wajib, Batas 121 Karakter, Nama Reserved, dan Duplikat Saat Mengetik | FE+BE | 30 | 101, 103, 111, 107 |
| TC-AC-DC-E2E-040-edit-validasi-duplikat-dan-emoji | Edit Category: Duplikat Case-insensitive, Save Duplikat, Unik Mengecualikan Diri Sendiri, dan Emoji Diblok | FE+BE | 24 | 108, 109, 110, 105 |
| TC-AC-DC-E2E-041-edit-batas-trim-dan-device-sku | Edit Category: Batas 120 Karakter, Auto-trim, dan Edit lewat Sub-tab Device SKU | FE+BE | 21 | 102, 104, 270 |
| TC-AC-DC-E2E-042-edit-unsaved-clear-esc-dan-leave | Edit Category: Clear Field, Esc pada Input Bersih, Nilai Dikembalikan ke Awal, dan Dialog Unsaved Changes Leave | FE+BE | 31 | 115, 116, 264, 117 |
| TC-AC-DC-E2E-043-edit-unsaved-cancel-dan-klik-luar | Edit Category: Dialog Unsaved Changes Cancel, Esc, Klik Area Luar Tree, dan Esc Leave | FE+BE | 30 | 118, 119, 258, 262 |
| TC-AC-DC-E2E-044-edit-unsaved-reload-navigasi-klik-aksi | Edit Category: Reload, Navigasi Internal, dan Klik Aksi Node Lain dengan Input Berisi Perubahan | FE+BE | 31 | 120, 121, 261 |
| TC-AC-DC-E2E-045-delete-dialog-leaf-dan-cancel | Delete Category: Dialog Konfirmasi Leaf, Cancel, Klik Backdrop, dan Esc | FE+BE | 25 | 127, 131, 133 |
| TC-AC-DC-E2E-046-delete-dialog-family-dan-cancel | Delete Category: Dialog Konfirmasi Family dan Cancel | FE+BE | 19 | 128, 132 |
| TC-AC-DC-E2E-047-delete-diblok-referensi-langsung | Delete Category: Diblok oleh Device Name Pengacu pada Node, Descendant, dan Daftar Panjang | FE+BE | 27 | 134, 136, 137, 138 |
| TC-AC-DC-E2E-048-delete-diblok-referensi-descendant-dan-device-sku | Delete Category: Diblok oleh Referensi pada Descendant, Klik Backdrop, dan Sub-tab Device SKU | FE+BE | 35 | 135, 274, 266, 271 |
| TC-AC-DC-E2E-049-delete-berhasil-leaf-dan-state-submitting | Delete Category: Berhasil pada Leaf, State Submitting, dan Klik Ganda pada Family | FE+BE | 28 | 129, 142, 143 |
| TC-AC-DC-E2E-050-delete-berhasil-family-dan-filter-aktif | Delete Category: Node Filter Terhapus, Parent Kehilangan Anak Terakhir, dan Family Tiga Level | FE+BE | 26 | 145, 304, 130 |
| TC-AC-DC-E2E-051-multi-konteks-dua-admin-add | Dua Admin: Add Subcategory saat Parent Dihapus, Node Hasil Pencarian Dihapus, dan Hierarchy Depth Limit Turun | FE+BE | 38 | 94, 305, 93 |
| TC-AC-DC-E2E-052-multi-konteks-dua-admin-edit | Dua Admin: Edit saat Node Dihapus dan Edit Bersamaan pada Node yang Sama | FE+BE | 28 | 122, 123 |
| TC-AC-DC-E2E-053-multi-konteks-dua-admin-nama-sama-dan-family | Dua Admin: Nama Sama pada Parent yang Sama dan Family Dihapus saat Edit Descendant | FE+BE | 30 | 255, 256 |
| TC-AC-DC-E2E-054-multi-konteks-dua-admin-delete-referensi | Dua Admin: Referensi Device Name Muncul Setelah Dialog Delete Terbuka | FE+BE | 23 | 139, 275 |
| TC-AC-DC-E2E-055-multi-konteks-dua-admin-delete-ganda | Dua Admin: Delete pada Node yang Sudah Dihapus Admin Lain dan Permintaan Delete Kedua dari Tab Lain | FE+BE | 29 | 140, 141 |
| TC-AC-DC-E2E-056-resilience-tulis-add-edit | Resilience: Gagal Memuat Tree, Kegagalan Server saat Add, dan Kegagalan Server saat Edit | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) | 40 | 13, 97, 126 |
| TC-AC-DC-E2E-057-resilience-delete-changelog-download | Resilience: Kegagalan Server saat Delete, Gagal Memuat Changelog, dan Download Changelog Gagal | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) | 36 | 144, 154, 215 |
| TC-AC-DC-E2E-058-changelog-screening-format-sel | Modal Changelog Category: Screening, Tooltip Toolbar, dan Format Sel | FE+BE (backend nyata) | 33 | 146, 148, 149, 147 |
| TC-AC-DC-E2E-059-changelog-reset-state-back-dan-device-sku | Modal Changelog Category: Isi Sel, Reset State, Tombol Back, Sub-tab Device SKU, dan Nama Category 120 Karakter | FE+BE (backend nyata) | 40 | 151, 153, 268, 272, 150 |
| TC-AC-DC-E2E-060-changelog-empty-state-principal-baru | Modal Changelog Category: Empty State Principal Tanpa Riwayat dan Transisi Keluar dari Empty State | FE+BE (backend nyata) | 35 | 152, 288, 289 |
| TC-AC-DC-E2E-061-changelog-search-siklus-dan-kolom | Modal Changelog Category: Search Siklus Interaksi, Placeholder, dan Kelas Kolom Teks | FE+BE (backend nyata) | 27 | 155, 156, 157 |
| TC-AC-DC-E2E-062-changelog-search-nilai-pelaku-trim | Modal Changelog Category: Search Kolom Nilai, Modified By, Trim, Tanggal, dan Teks Literal | FE+BE (backend nyata) | 23 | 158, 159, 160, 161, 162 |
| TC-AC-DC-E2E-063-changelog-search-kosong-dan-visibilitas-kolom | Modal Changelog Category: Search Tanpa Hasil dan Keterikatan Visibilitas Kolom | FE+BE (backend nyata) | 15 | 163, 164, 165 |
| TC-AC-DC-E2E-064-changelog-filter-screening-dan-opsi | Modal Changelog Category: Screening Filter Panel dan Filter Multi-select | FE+BE (backend nyata) | 22 | 166, 167, 168, 169, 170 |
| TC-AC-DC-E2E-065-changelog-filter-date-dan-dropdown | Modal Changelog Category: Filter Date Inklusif dan Opsi Dropdown Filter | FE+BE (backend nyata) | 20 | 171, 172, 173, 174 |
| TC-AC-DC-E2E-066-changelog-filter-chip | Modal Changelog Category: Chip Filter, Sinkron Checkbox, Chip +N more, dan Kombinasi AND | FE+BE (backend nyata) | 37 | 175, 176, 177, 178 |
| TC-AC-DC-E2E-067-changelog-filter-clear-apply-dan-search | Modal Changelog Category: Clear Field, Apply, Indikator Filter, dan Kombinasi dengan Search | FE+BE (backend nyata) | 33 | 179, 180, 181, 182, 183 |
| TC-AC-DC-E2E-068-changelog-filter-kombinasi-penuh-dan-reset-halaman | Modal Changelog Category: Kombinasi Search, Filter, Sort, Pagination, dan Reset Halaman | FE+BE (backend nyata) | 37 | 184, 185, 186, 276 |
| TC-AC-DC-E2E-069-changelog-filter-opsi-dinamis | Modal Changelog Category: Loading Dropdown Filter dan Opsi Category Bertambah Setelah Add | FE+BE (backend nyata; respons data opsi dropdown Filter ditahan sebagian lewat intercept sehingga state server tetap nyata) | 18 | 278, 277 |
| TC-AC-DC-E2E-070-changelog-sorting-date-dan-teks | Modal Changelog Category: Urutan Default, Sort Date, dan Sort Kolom Teks Action dan Category | FE+BE (backend nyata) | 28 | 188, 187, 189 |
| TC-AC-DC-E2E-071-changelog-sorting-nilai-field-modified-by | Modal Changelog Category: Sort Kolom Field, Old Value, New Value, dan Modified By | FE+BE (backend nyata) | 27 | 190, 191 |
| TC-AC-DC-E2E-072-changelog-sorting-target-halaman-actions | Modal Changelog Category: Perpindahan Target Sort, Nomor Halaman, dan Kolom Actions | FE+BE (backend nyata) | 24 | 192, 193, 194, 195 |
| TC-AC-DC-E2E-073-changelog-setup-column-screening-dan-persist | Modal Changelog Category: Screening Overlay Column Visibility dan Setup Column, Hide, dan Persist | FE+BE (backend nyata) | 28 | 196, 197, 198 |
| TC-AC-DC-E2E-074-changelog-setup-column-pin-dan-reset | Modal Changelog Category: Setup Column Batas Pin Ketiga dan Reset to Default | FE+BE (backend nyata) | 19 | 201, 202 |
| TC-AC-DC-E2E-075-changelog-setup-column-tutup-guard-dan-isolasi | Modal Changelog Category: Setup Column Tutup Tanpa Save, Guard Satu Kolom, dan Isolasi Antar Tabel | FE+BE (backend nyata) | 27 | 203, 204, 205 |
| TC-AC-DC-E2E-076-changelog-pagination | Modal Changelog Category: Pagination, Navigasi Halaman, dan Page Size | FE+BE (backend nyata) | 27 | 206, 207, 208 |
| TC-AC-DC-E2E-077-changelog-download | Modal Changelog Category: Download CSV dan XLSX, Nama Berkas, dan Mengikuti Search, Filter, dan Kolom | FE+BE (backend nyata) | 30 | 209, 210, 211, 212, 214 |
| TC-AC-DC-E2E-078-changelog-isi-berkas-export | Modal Changelog Category: Isi Berkas Export Format Tanggal, Penanda Kosong, dan Kutip Ganda CSV | FE+BE (backend nyata) | 17 | 213, 284 |
| TC-AC-DC-E2E-079-log-changelog-create-edit-delete-leaf | Changelog Category Mencatat Tepat Satu Entri untuk Create, Edit, dan Delete Leaf | FE+BE | 36 | 216, 217, 218 |
| TC-AC-DC-E2E-080-log-changelog-delete-family-dan-immutability | Changelog Category: Delete Family Pre-order dan Snapshot Entri Tidak Berubah | FE+BE | 39 | 219, 227, 228 |
| TC-AC-DC-E2E-081-log-system-log-dan-activity-log | System Log Aktor dan Activity Log Admin Console Mencatat Create, Edit, dan Delete Category | FE+BE | 32 | 224, 225 |
| TC-AC-DC-E2E-082-log-sinkron-tiga-surface-dan-aktor | Satu Aksi Edit Sinkron di Tiga Surface Log dan Modified By Mengikuti Aktor | FE+BE | 28 | 226, 229 |
| TC-AC-DC-E2E-083-log-absence-no-op-dan-gagal | Absence Log: Save Tanpa Perubahan dan Edit No-op Tidak Menulis Entri | FE+BE | 28 | 112, 113, 223 |
| TC-AC-DC-E2E-084-log-absence-delete-diblok-dan-kegagalan | Absence Log: Delete Diblok Referensi dan Delete Family Gagal Tidak Menulis Entri | FE+BE | 23 | 220, 221 |
| TC-AC-DC-E2E-085-sinkron-device-name-rename-dan-hapus | Sinkron Category dengan Device Name dan Device SKU: Rename, Node Baru, dan Node Dihapus | FE+BE | 38 | 231, 232, 233 |
| TC-AC-DC-E2E-086-sinkron-device-name-dropdown-dan-guard | Sinkron Category dengan Device Name: Semantik Dropdown, Filter Parent pada Device SKU, dan Guard Delete | FE+BE | 36 | 234, 293, 300, 235, 236 |
| TC-AC-DC-E2E-087-sinkron-hierarchy-depth-limit | Hierarchy Depth Limit: Penurunan Tidak Menghapus Node dan Kenaikan Langsung Berlaku pada Add | FE+BE | 16 | 237, 238 |
| TC-AC-DC-E2E-088-sinkron-format-tanggal-general-settings | Format Tanggal General Settings Tercermin pada Kolom Date dan Date Filter Panel Changelog | FE+BE | 10 | 239, 240 |
| TC-AC-DC-E2E-089-floating-toggle-viewport-kecil-dan-localstorage | Sidebar Category: Auto-Collapse di Bawah 1280px Tidak Menimpa Preferensi dan Default Open saat localStorage Tidak Tersedia | FE+BE | 15 | 20, 21 |
| TC-AC-DC-E2E-090-filter-category-persistensi-refresh-dan-back | Filter Category: Pilihan Dipertahankan Setelah F5 atau Back, State Expand dan Pencarian Tree Direset | FE+BE | 16 | 36 |
| TC-AC-DC-E2E-091-role-matrix-visibilitas-read-only | Role Matrix: Visibilitas Aksi Node dan Kontrol Changelog untuk Read Only | FE+BE | 25 | 52, 283 |
| TC-AC-DC-E2E-092-defense-request-langsung-validasi-server | Defense-in-Depth: Request Langsung Melanggar Validasi Server Ditolak | FE+BE | 33 | 250, 251, 252, 253 |
| TC-AC-DC-E2E-093-add-unsaved-device-sku | Add Subcategory: Dialog Unsaved Changes pada Sub-tab Device SKU | FE+BE | 13 | 273 |
| TC-AC-DC-E2E-094-multi-konteks-dua-admin-edit-nama-bentrok | Dua Admin: Edit ke Nama yang Baru Dibuat Admin Lain di Parent yang Sama | FE+BE | 20 | 281 |
| TC-AC-DC-E2E-095-changelog-setup-column-drag-reorder-dan-persist | Modal Changelog Category: Setup Column Drag Reorder Kolom dan Persist Setelah Refresh | FE+BE (backend nyata) | 9 | 199 |
| TC-AC-DC-E2E-096-changelog-setup-column-pin-kolom-dan-persist | Modal Changelog Category: Setup Column Pin Kolom Membekukan Kolom dan Persist Setelah Refresh | FE+BE (backend nyata) | 14 | 200 |
| TC-AC-DC-E2E-097-log-absence-node-lain-tidak-terlibat | Absence Log: Aksi pada Satu Node Tidak Menghasilkan Entri untuk Node Lain | FE+BE | 20 | 230 |
| TC-AC-DC-E2E-098-log-absence-add-dan-edit-gagal | Absence Log: Add dan Edit yang Gagal serta Request Langsung yang Ditolak Server Tidak Menulis Entri | FE+BE | 52 | 222, 250, 251, 252, 253 |

## Pembagian TC lintas spec

- TC-AC-DC-250, 251, 252, dan 253 terbelah dua spec menurut S-05: penolakan server dan state tree di spec 092 (spec utama pada tabel "Lapisan per TC"), klausa absence "Changelog tidak bertambah" (P-5 a) di spec 098 dengan baseline per TC. Tidak ada TC lain yang terbelah lintas spec.
- Nomor cadangan terpakai: 089 (TC-20, 21; dari 007), 090 (TC-36; dari 009), 091 (TC-52, 283; dari 018), 092 (TC-250 sampai 253; dari 023), 093 (TC-273; dari 036), 094 (TC-281; dari 052), 095 (TC-199; dari 073), 096 (TC-200; dari 074), 097 (TC-230; dari 083), 098 (TC-222; dari 084). Spec 036 dan 052 berubah isi/id; spec 059 dan 066 mempertahankan TC-150 dan TC-177/178.
- Asersi absence log kelas g ada di spec 083, 084, 097, 098 (kelas g); spec 098 memuat juga klausa absence TC-AC-DC-250 sampai 253. "Tidak ada entri log" pada TC validasi/cancel (mis. spec 093, 094) ditulis sebagai asersi jumlah terhadap baseline (S-05, S-12), bukan absence.

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec (belum terdaftar di `spectra.config.ts` dan `.env.example` kecuali yang sudah ada; berkas itu tidak diubah oleh generate spec): `AC_DCFRESH_TC_PASSWORD`, `AC_DC_CLIENT_PASSWORD`, `AC_DC_CREATE_PASSWORD`, `AC_DC_CUD_PASSWORD`, `AC_DC_DEFAULT_PASSWORD`, `AC_DC_DELETE_PASSWORD`, `AC_DC_DISTRIBUTOR_PASSWORD`, `AC_DC_NOCAP_PASSWORD`, `AC_DC_PARTNER_PASSWORD`, `AC_DC_RO_PASSWORD`, `AC_DC_TC2_PASSWORD`, `AC_DC_UPDATE_PASSWORD`, `AC_TC_PASSWORD`.
- Fixture `settingsDeviceCategory` (belum ada): data Pre-setup #14 (pohon), #15 (Device Name), #17 (riwayat Changelog), #19 (General Settings), entitas `Principal Tanpa Riwayat` dan akun `totalControlFresh`.
- Fixture BE: membuat/menghapus node Category dan Device Name lewat sesi API aktor; memulihkan pohon dan Changelog; mengubah Hierarchy Depth Limit (Lifecycle Settings) dan General Settings; membaca jumlah entri Changelog sebagai baseline.
- Kemampuan teknis: `Spectra.intercept()` (500 dan kegagalan lain, spec 056/057/084), dua konteks browser (spec 051-055, 094), viewport kecil dan localStorage dinonaktifkan (spec 089), emulasi/aplikasi mobile (spec 014/015), penanganan `beforeunload`, clipboard, injeksi DOM (spec 024), pembacaan isi file download (spec 078).
- Suite berjalan serial (`parallel: false`): pohon Category tunggal per entitas Principal dan state bersama.
- Hook `beforeEach` suite membuka Device Name; ini bentrok dengan akun yang ditolak di halaman itu (spec 016, 017, 025). Perlu pengecualian pada hook suite.

## Temuan yang masih terbuka

Temuan TC sumber dicatat per spec di `## Notes` butir "Temuan untuk QA". Yang paling berdampak:

- Keputusan user (2026-11-02), Changelog vs S-12: disetujui pengecualian setara A-5 untuk modul ini. Fixture BE memulihkan Changelog ke Pre-setup #17 sebelum dan sesudah tiap spec section 4 (058-078), sehingga total absolut (12 entri, 10+2 per halaman) boleh diasersi; spec section 5 tetap memakai selisih terhadap baseline. Butir ini belum ada di Lampiran A  (di luar folder suite, tidak diubah oleh generate spec); pemilik repo e2e perlu menambahkannya.
- Keputusan user: target tulis/hapus adalah node milik spec bersufiks ; node Pre-setup #14 hanya dibaca. Simpangan yang disetujui user: node induk literal di spec 059, 060, 069, 078 (agar Changelog tidak bertambah) dan request ditolak ke node hardcoded di spec 023/092 (TC-242, 243, 251).
- Mobile (TC-37 sampai 42, 302, 39): tidak jelas viewport mobile web atau aplikasi Android nyata (spec 014, 015).
- TC-85 dan 106: cara melewati filter FE tidak dinyatakan; spec 024 memakai injeksi DOM (kemampuan tim FE), alternatif `Spectra.intercept()` dicatat di Temuan QA.
- TC-45, 241, 250, 252, 253, 247-249, 254 dan lainnya: Expected/langkah tidak spesifik (status respons, endpoint, kolom Changelog); lihat Notes spec terkait.
- Lima TC bertanda Manual Only (93, 94, 122/123/281, 139/275, 140/141, 255/256) tetap ditulis sebagai spec dua konteks (bagian 2 konvensi).
- Spec di atas batas ±35 langkah dengan alasan tertulis di Notes: 013 (40), 024 (38), 035 (37), 051 (38), 056 (40), 057 (36), 059 (40), 066 (37), 068 (37), 079 (36), 080 (39), 086 (36), 098 (52). Kandidat pemecahan bila auditor menilai kurang: 013, 051, 056, 073, 096.
- Akun #1 memakai `AC_TC_PASSWORD`; bila password berbeda dengan akun `totalControlAdminConsole`, perlu env terpisah.
- Lampiran A belum punya butir untuk modul ini.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-DC-1 | TC-AC-DC-E2E-001 | FE+BE |
| TC-AC-DC-2 | TC-AC-DC-E2E-001 | FE+BE |
| TC-AC-DC-3 | TC-AC-DC-E2E-001 | FE+BE |
| TC-AC-DC-4 | TC-AC-DC-E2E-001 | FE+BE |
| TC-AC-DC-5 | TC-AC-DC-E2E-001 | FE+BE |
| TC-AC-DC-6 | TC-AC-DC-E2E-002 | FE+BE |
| TC-AC-DC-7 | TC-AC-DC-E2E-002 | FE+BE |
| TC-AC-DC-8 | TC-AC-DC-E2E-002 | FE+BE |
| TC-AC-DC-9 | TC-AC-DC-E2E-004 | FE+BE |
| TC-AC-DC-10 | TC-AC-DC-E2E-004 | FE+BE |
| TC-AC-DC-11 | TC-AC-DC-E2E-003 | FE+BE |
| TC-AC-DC-12 | TC-AC-DC-E2E-005 | FE+BE (penundaan respons memakai `Spectra |
| TC-AC-DC-13 | TC-AC-DC-E2E-056 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-14 | TC-AC-DC-E2E-005 | FE+BE (penundaan respons memakai `Spectra |
| TC-AC-DC-15 | TC-AC-DC-E2E-005 | FE+BE (penundaan respons memakai `Spectra |
| TC-AC-DC-16 | TC-AC-DC-E2E-005 | FE+BE (penundaan respons memakai `Spectra |
| TC-AC-DC-17 | TC-AC-DC-E2E-007 | FE+BE |
| TC-AC-DC-18 | TC-AC-DC-E2E-007 | FE+BE |
| TC-AC-DC-19 | TC-AC-DC-E2E-007 | FE+BE |
| TC-AC-DC-20 | TC-AC-DC-E2E-089 | FE+BE |
| TC-AC-DC-21 | TC-AC-DC-E2E-089 | FE+BE |
| TC-AC-DC-22 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-23 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-24 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-25 | TC-AC-DC-E2E-010 | FE+BE |
| TC-AC-DC-26 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-27 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-28 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-29 | TC-AC-DC-E2E-010 | FE+BE |
| TC-AC-DC-30 | TC-AC-DC-E2E-009 | FE+BE |
| TC-AC-DC-31 | TC-AC-DC-E2E-009 | FE+BE |
| TC-AC-DC-32 | TC-AC-DC-E2E-013 | FE+BE |
| TC-AC-DC-33 | TC-AC-DC-E2E-013 | FE+BE |
| TC-AC-DC-34 | TC-AC-DC-E2E-013 | FE+BE |
| TC-AC-DC-35 | TC-AC-DC-E2E-008 | FE+BE |
| TC-AC-DC-36 | TC-AC-DC-E2E-090 | FE+BE |
| TC-AC-DC-37 | TC-AC-DC-E2E-014 | FE+BE |
| TC-AC-DC-38 | TC-AC-DC-E2E-014 | FE+BE |
| TC-AC-DC-39 | TC-AC-DC-E2E-015 | FE+BE |
| TC-AC-DC-40 | TC-AC-DC-E2E-014 | FE+BE |
| TC-AC-DC-41 | TC-AC-DC-E2E-014 | FE+BE |
| TC-AC-DC-42 | TC-AC-DC-E2E-015 | FE+BE |
| TC-AC-DC-43 | TC-AC-DC-E2E-018 | FE+BE |
| TC-AC-DC-44 | TC-AC-DC-E2E-016 | FE+BE |
| TC-AC-DC-45 | TC-AC-DC-E2E-016 | FE+BE |
| TC-AC-DC-46 | TC-AC-DC-E2E-017 | FE+BE |
| TC-AC-DC-47 | TC-AC-DC-E2E-017 | FE+BE |
| TC-AC-DC-48 | TC-AC-DC-E2E-017 | FE+BE |
| TC-AC-DC-49 | TC-AC-DC-E2E-017 | FE+BE |
| TC-AC-DC-50 | TC-AC-DC-E2E-018 | FE+BE |
| TC-AC-DC-51 | TC-AC-DC-E2E-018 | FE+BE |
| TC-AC-DC-52 | TC-AC-DC-E2E-091 | FE+BE |
| TC-AC-DC-53 | TC-AC-DC-E2E-019 | FE+BE |
| TC-AC-DC-54 | TC-AC-DC-E2E-020 | FE+BE |
| TC-AC-DC-55 | TC-AC-DC-E2E-021 | FE+BE |
| TC-AC-DC-56 | TC-AC-DC-E2E-018 | FE+BE |
| TC-AC-DC-57 | TC-AC-DC-E2E-022 | FE+BE |
| TC-AC-DC-58 | TC-AC-DC-E2E-022 | FE+BE |
| TC-AC-DC-59 | TC-AC-DC-E2E-020 | FE+BE |
| TC-AC-DC-60 | TC-AC-DC-E2E-021 | FE+BE |
| TC-AC-DC-61 | TC-AC-DC-E2E-019 | FE+BE |
| TC-AC-DC-62 | TC-AC-DC-E2E-026 | FE+BE |
| TC-AC-DC-63 | TC-AC-DC-E2E-026 | FE+BE |
| TC-AC-DC-64 | TC-AC-DC-E2E-026 | FE+BE |
| TC-AC-DC-65 | TC-AC-DC-E2E-026 | FE+BE |
| TC-AC-DC-66 | TC-AC-DC-E2E-027 | FE+BE |
| TC-AC-DC-67 | TC-AC-DC-E2E-027 | FE+BE |
| TC-AC-DC-68 | TC-AC-DC-E2E-027 | FE+BE |
| TC-AC-DC-69 | TC-AC-DC-E2E-033 | FE+BE |
| TC-AC-DC-70 | TC-AC-DC-E2E-033 | FE+BE |
| TC-AC-DC-71 | TC-AC-DC-E2E-033 | FE+BE |
| TC-AC-DC-72 | TC-AC-DC-E2E-034 | FE+BE |
| TC-AC-DC-73 | TC-AC-DC-E2E-034 | FE+BE |
| TC-AC-DC-74 | TC-AC-DC-E2E-035 | FE+BE |
| TC-AC-DC-75 | TC-AC-DC-E2E-035 | FE+BE |
| TC-AC-DC-76 | TC-AC-DC-E2E-035 | FE+BE |
| TC-AC-DC-77 | TC-AC-DC-E2E-035 | FE+BE |
| TC-AC-DC-78 | TC-AC-DC-E2E-029 | FE+BE |
| TC-AC-DC-79 | TC-AC-DC-E2E-029 | FE+BE |
| TC-AC-DC-80 | TC-AC-DC-E2E-031 | FE+BE |
| TC-AC-DC-81 | TC-AC-DC-E2E-029 | FE+BE |
| TC-AC-DC-82 | TC-AC-DC-E2E-031 | FE+BE |
| TC-AC-DC-83 | TC-AC-DC-E2E-031 | FE+BE |
| TC-AC-DC-84 | TC-AC-DC-E2E-031 | FE+BE |
| TC-AC-DC-85 | TC-AC-DC-E2E-024 | FE+BE |
| TC-AC-DC-86 | TC-AC-DC-E2E-030 | FE+BE |
| TC-AC-DC-87 | TC-AC-DC-E2E-030 | FE+BE |
| TC-AC-DC-88 | TC-AC-DC-E2E-030 | FE+BE |
| TC-AC-DC-89 | TC-AC-DC-E2E-030 | FE+BE |
| TC-AC-DC-90 | TC-AC-DC-E2E-029 | FE+BE |
| TC-AC-DC-91 | TC-AC-DC-E2E-032 | FE+BE |
| TC-AC-DC-92 | TC-AC-DC-E2E-032 | FE+BE |
| TC-AC-DC-93 | TC-AC-DC-E2E-051 | FE+BE |
| TC-AC-DC-94 | TC-AC-DC-E2E-051 | FE+BE |
| TC-AC-DC-95 | TC-AC-DC-E2E-028 | FE+BE |
| TC-AC-DC-96 | TC-AC-DC-E2E-028 | FE+BE |
| TC-AC-DC-97 | TC-AC-DC-E2E-056 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-98 | TC-AC-DC-E2E-037 | FE+BE |
| TC-AC-DC-99 | TC-AC-DC-E2E-037 | FE+BE |
| TC-AC-DC-100 | TC-AC-DC-E2E-037 | FE+BE |
| TC-AC-DC-101 | TC-AC-DC-E2E-039 | FE+BE |
| TC-AC-DC-102 | TC-AC-DC-E2E-041 | FE+BE |
| TC-AC-DC-103 | TC-AC-DC-E2E-039 | FE+BE |
| TC-AC-DC-104 | TC-AC-DC-E2E-041 | FE+BE |
| TC-AC-DC-105 | TC-AC-DC-E2E-040 | FE+BE |
| TC-AC-DC-106 | TC-AC-DC-E2E-024 | FE+BE |
| TC-AC-DC-107 | TC-AC-DC-E2E-039 | FE+BE |
| TC-AC-DC-108 | TC-AC-DC-E2E-040 | FE+BE |
| TC-AC-DC-109 | TC-AC-DC-E2E-040 | FE+BE |
| TC-AC-DC-110 | TC-AC-DC-E2E-040 | FE+BE |
| TC-AC-DC-111 | TC-AC-DC-E2E-039 | FE+BE |
| TC-AC-DC-112 | TC-AC-DC-E2E-083 | FE+BE |
| TC-AC-DC-113 | TC-AC-DC-E2E-083 | FE+BE |
| TC-AC-DC-114 | TC-AC-DC-E2E-038 | FE+BE |
| TC-AC-DC-115 | TC-AC-DC-E2E-042 | FE+BE |
| TC-AC-DC-116 | TC-AC-DC-E2E-042 | FE+BE |
| TC-AC-DC-117 | TC-AC-DC-E2E-042 | FE+BE |
| TC-AC-DC-118 | TC-AC-DC-E2E-043 | FE+BE |
| TC-AC-DC-119 | TC-AC-DC-E2E-043 | FE+BE |
| TC-AC-DC-120 | TC-AC-DC-E2E-044 | FE+BE |
| TC-AC-DC-121 | TC-AC-DC-E2E-044 | FE+BE |
| TC-AC-DC-122 | TC-AC-DC-E2E-052 | FE+BE |
| TC-AC-DC-123 | TC-AC-DC-E2E-052 | FE+BE |
| TC-AC-DC-124 | TC-AC-DC-E2E-038 | FE+BE |
| TC-AC-DC-125 | TC-AC-DC-E2E-038 | FE+BE |
| TC-AC-DC-126 | TC-AC-DC-E2E-056 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-127 | TC-AC-DC-E2E-045 | FE+BE |
| TC-AC-DC-128 | TC-AC-DC-E2E-046 | FE+BE |
| TC-AC-DC-129 | TC-AC-DC-E2E-049 | FE+BE |
| TC-AC-DC-130 | TC-AC-DC-E2E-050 | FE+BE |
| TC-AC-DC-131 | TC-AC-DC-E2E-045 | FE+BE |
| TC-AC-DC-132 | TC-AC-DC-E2E-046 | FE+BE |
| TC-AC-DC-133 | TC-AC-DC-E2E-045 | FE+BE |
| TC-AC-DC-134 | TC-AC-DC-E2E-047 | FE+BE |
| TC-AC-DC-135 | TC-AC-DC-E2E-048 | FE+BE |
| TC-AC-DC-136 | TC-AC-DC-E2E-047 | FE+BE |
| TC-AC-DC-137 | TC-AC-DC-E2E-047 | FE+BE |
| TC-AC-DC-138 | TC-AC-DC-E2E-047 | FE+BE |
| TC-AC-DC-139 | TC-AC-DC-E2E-054 | FE+BE |
| TC-AC-DC-140 | TC-AC-DC-E2E-055 | FE+BE |
| TC-AC-DC-141 | TC-AC-DC-E2E-055 | FE+BE |
| TC-AC-DC-142 | TC-AC-DC-E2E-049 | FE+BE |
| TC-AC-DC-143 | TC-AC-DC-E2E-049 | FE+BE |
| TC-AC-DC-144 | TC-AC-DC-E2E-057 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-145 | TC-AC-DC-E2E-050 | FE+BE |
| TC-AC-DC-146 | TC-AC-DC-E2E-058 | FE+BE (backend nyata) |
| TC-AC-DC-147 | TC-AC-DC-E2E-058 | FE+BE (backend nyata) |
| TC-AC-DC-148 | TC-AC-DC-E2E-058 | FE+BE (backend nyata) |
| TC-AC-DC-149 | TC-AC-DC-E2E-058 | FE+BE (backend nyata) |
| TC-AC-DC-150 | TC-AC-DC-E2E-059 | FE+BE (backend nyata) |
| TC-AC-DC-151 | TC-AC-DC-E2E-059 | FE+BE (backend nyata) |
| TC-AC-DC-152 | TC-AC-DC-E2E-060 | FE+BE (backend nyata) |
| TC-AC-DC-153 | TC-AC-DC-E2E-059 | FE+BE (backend nyata) |
| TC-AC-DC-154 | TC-AC-DC-E2E-057 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-155 | TC-AC-DC-E2E-061 | FE+BE (backend nyata) |
| TC-AC-DC-156 | TC-AC-DC-E2E-061 | FE+BE (backend nyata) |
| TC-AC-DC-157 | TC-AC-DC-E2E-061 | FE+BE (backend nyata) |
| TC-AC-DC-158 | TC-AC-DC-E2E-062 | FE+BE (backend nyata) |
| TC-AC-DC-159 | TC-AC-DC-E2E-062 | FE+BE (backend nyata) |
| TC-AC-DC-160 | TC-AC-DC-E2E-062 | FE+BE (backend nyata) |
| TC-AC-DC-161 | TC-AC-DC-E2E-062 | FE+BE (backend nyata) |
| TC-AC-DC-162 | TC-AC-DC-E2E-062 | FE+BE (backend nyata) |
| TC-AC-DC-163 | TC-AC-DC-E2E-063 | FE+BE (backend nyata) |
| TC-AC-DC-164 | TC-AC-DC-E2E-063 | FE+BE (backend nyata) |
| TC-AC-DC-165 | TC-AC-DC-E2E-063 | FE+BE (backend nyata) |
| TC-AC-DC-166 | TC-AC-DC-E2E-064 | FE+BE (backend nyata) |
| TC-AC-DC-167 | TC-AC-DC-E2E-064 | FE+BE (backend nyata) |
| TC-AC-DC-168 | TC-AC-DC-E2E-064 | FE+BE (backend nyata) |
| TC-AC-DC-169 | TC-AC-DC-E2E-064 | FE+BE (backend nyata) |
| TC-AC-DC-170 | TC-AC-DC-E2E-064 | FE+BE (backend nyata) |
| TC-AC-DC-171 | TC-AC-DC-E2E-065 | FE+BE (backend nyata) |
| TC-AC-DC-172 | TC-AC-DC-E2E-065 | FE+BE (backend nyata) |
| TC-AC-DC-173 | TC-AC-DC-E2E-065 | FE+BE (backend nyata) |
| TC-AC-DC-174 | TC-AC-DC-E2E-065 | FE+BE (backend nyata) |
| TC-AC-DC-175 | TC-AC-DC-E2E-066 | FE+BE (backend nyata) |
| TC-AC-DC-176 | TC-AC-DC-E2E-066 | FE+BE (backend nyata) |
| TC-AC-DC-177 | TC-AC-DC-E2E-066 | FE+BE (backend nyata) |
| TC-AC-DC-178 | TC-AC-DC-E2E-066 | FE+BE (backend nyata) |
| TC-AC-DC-179 | TC-AC-DC-E2E-067 | FE+BE (backend nyata) |
| TC-AC-DC-180 | TC-AC-DC-E2E-067 | FE+BE (backend nyata) |
| TC-AC-DC-181 | TC-AC-DC-E2E-067 | FE+BE (backend nyata) |
| TC-AC-DC-182 | TC-AC-DC-E2E-067 | FE+BE (backend nyata) |
| TC-AC-DC-183 | TC-AC-DC-E2E-067 | FE+BE (backend nyata) |
| TC-AC-DC-184 | TC-AC-DC-E2E-068 | FE+BE (backend nyata) |
| TC-AC-DC-185 | TC-AC-DC-E2E-068 | FE+BE (backend nyata) |
| TC-AC-DC-186 | TC-AC-DC-E2E-068 | FE+BE (backend nyata) |
| TC-AC-DC-187 | TC-AC-DC-E2E-070 | FE+BE (backend nyata) |
| TC-AC-DC-188 | TC-AC-DC-E2E-070 | FE+BE (backend nyata) |
| TC-AC-DC-189 | TC-AC-DC-E2E-070 | FE+BE (backend nyata) |
| TC-AC-DC-190 | TC-AC-DC-E2E-071 | FE+BE (backend nyata) |
| TC-AC-DC-191 | TC-AC-DC-E2E-071 | FE+BE (backend nyata) |
| TC-AC-DC-192 | TC-AC-DC-E2E-072 | FE+BE (backend nyata) |
| TC-AC-DC-193 | TC-AC-DC-E2E-072 | FE+BE (backend nyata) |
| TC-AC-DC-194 | TC-AC-DC-E2E-072 | FE+BE (backend nyata) |
| TC-AC-DC-195 | TC-AC-DC-E2E-072 | FE+BE (backend nyata) |
| TC-AC-DC-196 | TC-AC-DC-E2E-073 | FE+BE (backend nyata) |
| TC-AC-DC-197 | TC-AC-DC-E2E-073 | FE+BE (backend nyata) |
| TC-AC-DC-198 | TC-AC-DC-E2E-073 | FE+BE (backend nyata) |
| TC-AC-DC-199 | TC-AC-DC-E2E-095 | FE+BE (backend nyata) |
| TC-AC-DC-200 | TC-AC-DC-E2E-096 | FE+BE (backend nyata) |
| TC-AC-DC-201 | TC-AC-DC-E2E-074 | FE+BE (backend nyata) |
| TC-AC-DC-202 | TC-AC-DC-E2E-074 | FE+BE (backend nyata) |
| TC-AC-DC-203 | TC-AC-DC-E2E-075 | FE+BE (backend nyata) |
| TC-AC-DC-204 | TC-AC-DC-E2E-075 | FE+BE (backend nyata) |
| TC-AC-DC-205 | TC-AC-DC-E2E-075 | FE+BE (backend nyata) |
| TC-AC-DC-206 | TC-AC-DC-E2E-076 | FE+BE (backend nyata) |
| TC-AC-DC-207 | TC-AC-DC-E2E-076 | FE+BE (backend nyata) |
| TC-AC-DC-208 | TC-AC-DC-E2E-076 | FE+BE (backend nyata) |
| TC-AC-DC-209 | TC-AC-DC-E2E-077 | FE+BE (backend nyata) |
| TC-AC-DC-210 | TC-AC-DC-E2E-077 | FE+BE (backend nyata) |
| TC-AC-DC-211 | TC-AC-DC-E2E-077 | FE+BE (backend nyata) |
| TC-AC-DC-212 | TC-AC-DC-E2E-077 | FE+BE (backend nyata) |
| TC-AC-DC-213 | TC-AC-DC-E2E-078 | FE+BE (backend nyata) |
| TC-AC-DC-214 | TC-AC-DC-E2E-077 | FE+BE (backend nyata) |
| TC-AC-DC-215 | TC-AC-DC-E2E-057 | FE+BE (intercept parsial di atas backend nyata; hanya respons endpoint yang dipaksa gagal yang diganti, selebihnya backend nyata) |
| TC-AC-DC-216 | TC-AC-DC-E2E-079 | FE+BE |
| TC-AC-DC-217 | TC-AC-DC-E2E-079 | FE+BE |
| TC-AC-DC-218 | TC-AC-DC-E2E-079 | FE+BE |
| TC-AC-DC-219 | TC-AC-DC-E2E-080 | FE+BE |
| TC-AC-DC-220 | TC-AC-DC-E2E-084 | FE+BE |
| TC-AC-DC-221 | TC-AC-DC-E2E-084 | FE+BE |
| TC-AC-DC-222 | TC-AC-DC-E2E-098 | FE+BE |
| TC-AC-DC-223 | TC-AC-DC-E2E-083 | FE+BE |
| TC-AC-DC-224 | TC-AC-DC-E2E-081 | FE+BE |
| TC-AC-DC-225 | TC-AC-DC-E2E-081 | FE+BE |
| TC-AC-DC-226 | TC-AC-DC-E2E-082 | FE+BE |
| TC-AC-DC-227 | TC-AC-DC-E2E-080 | FE+BE |
| TC-AC-DC-228 | TC-AC-DC-E2E-080 | FE+BE |
| TC-AC-DC-229 | TC-AC-DC-E2E-082 | FE+BE |
| TC-AC-DC-230 | TC-AC-DC-E2E-097 | FE+BE |
| TC-AC-DC-231 | TC-AC-DC-E2E-085 | FE+BE |
| TC-AC-DC-232 | TC-AC-DC-E2E-085 | FE+BE |
| TC-AC-DC-233 | TC-AC-DC-E2E-085 | FE+BE |
| TC-AC-DC-234 | TC-AC-DC-E2E-086 | FE+BE |
| TC-AC-DC-235 | TC-AC-DC-E2E-086 | FE+BE |
| TC-AC-DC-236 | TC-AC-DC-E2E-086 | FE+BE |
| TC-AC-DC-237 | TC-AC-DC-E2E-087 | FE+BE |
| TC-AC-DC-238 | TC-AC-DC-E2E-087 | FE+BE |
| TC-AC-DC-239 | TC-AC-DC-E2E-088 | FE+BE |
| TC-AC-DC-240 | TC-AC-DC-E2E-088 | FE+BE |
| TC-AC-DC-241 | TC-AC-DC-E2E-023 | FE+BE |
| TC-AC-DC-242 | TC-AC-DC-E2E-023 | FE+BE |
| TC-AC-DC-243 | TC-AC-DC-E2E-023 | FE+BE |
| TC-AC-DC-244 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-245 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-246 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-247 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-248 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-249 | TC-AC-DC-E2E-025 | FE+BE |
| TC-AC-DC-250 | TC-AC-DC-E2E-092 | FE+BE |
| TC-AC-DC-251 | TC-AC-DC-E2E-092 | FE+BE |
| TC-AC-DC-252 | TC-AC-DC-E2E-092 | FE+BE |
| TC-AC-DC-253 | TC-AC-DC-E2E-092 | FE+BE |
| TC-AC-DC-254 | TC-AC-DC-E2E-024 | FE+BE |
| TC-AC-DC-255 | TC-AC-DC-E2E-053 | FE+BE |
| TC-AC-DC-256 | TC-AC-DC-E2E-053 | FE+BE |
| TC-AC-DC-257 | TC-AC-DC-E2E-034 | FE+BE |
| TC-AC-DC-258 | TC-AC-DC-E2E-043 | FE+BE |
| TC-AC-DC-259 | TC-AC-DC-E2E-036 | FE+BE |
| TC-AC-DC-260 | TC-AC-DC-E2E-036 | FE+BE |
| TC-AC-DC-261 | TC-AC-DC-E2E-044 | FE+BE |
| TC-AC-DC-262 | TC-AC-DC-E2E-043 | FE+BE |
| TC-AC-DC-263 | TC-AC-DC-E2E-033 | FE+BE |
| TC-AC-DC-264 | TC-AC-DC-E2E-042 | FE+BE |
| TC-AC-DC-265 | TC-AC-DC-E2E-034 | FE+BE |
| TC-AC-DC-266 | TC-AC-DC-E2E-048 | FE+BE |
| TC-AC-DC-267 | TC-AC-DC-E2E-036 | FE+BE |
| TC-AC-DC-268 | TC-AC-DC-E2E-059 | FE+BE (backend nyata) |
| TC-AC-DC-269 | TC-AC-DC-E2E-027 | FE+BE |
| TC-AC-DC-270 | TC-AC-DC-E2E-041 | FE+BE |
| TC-AC-DC-271 | TC-AC-DC-E2E-048 | FE+BE |
| TC-AC-DC-272 | TC-AC-DC-E2E-059 | FE+BE (backend nyata) |
| TC-AC-DC-273 | TC-AC-DC-E2E-093 | FE+BE |
| TC-AC-DC-274 | TC-AC-DC-E2E-048 | FE+BE |
| TC-AC-DC-275 | TC-AC-DC-E2E-054 | FE+BE |
| TC-AC-DC-276 | TC-AC-DC-E2E-068 | FE+BE (backend nyata) |
| TC-AC-DC-277 | TC-AC-DC-E2E-069 | FE+BE (backend nyata; respons data opsi dropdown Filter ditahan sebagian lewat intercept sehingga state server tetap nyata) |
| TC-AC-DC-278 | TC-AC-DC-E2E-069 | FE+BE (backend nyata; respons data opsi dropdown Filter ditahan sebagian lewat intercept sehingga state server tetap nyata) |
| TC-AC-DC-279 | TC-AC-DC-E2E-004 | FE+BE |
| TC-AC-DC-280 | TC-AC-DC-E2E-016 | FE+BE |
| TC-AC-DC-281 | TC-AC-DC-E2E-094 | FE+BE |
| TC-AC-DC-282 | TC-AC-DC-E2E-013 | FE+BE |
| TC-AC-DC-283 | TC-AC-DC-E2E-091 | FE+BE |
| TC-AC-DC-284 | TC-AC-DC-E2E-078 | FE+BE (backend nyata) |
| TC-AC-DC-285 | TC-AC-DC-E2E-009 | FE+BE |
| TC-AC-DC-286 | TC-AC-DC-E2E-003 | FE+BE |
| TC-AC-DC-287 | TC-AC-DC-E2E-003 | FE+BE |
| TC-AC-DC-288 | TC-AC-DC-E2E-060 | FE+BE (backend nyata) |
| TC-AC-DC-289 | TC-AC-DC-E2E-060 | FE+BE (backend nyata) |
| TC-AC-DC-290 | TC-AC-DC-E2E-010 | FE+BE |
| TC-AC-DC-291 | TC-AC-DC-E2E-010 | FE+BE |
| TC-AC-DC-292 | TC-AC-DC-E2E-011 | FE+BE |
| TC-AC-DC-293 | TC-AC-DC-E2E-086 | FE+BE |
| TC-AC-DC-294 | TC-AC-DC-E2E-011 | FE+BE |
| TC-AC-DC-295 | TC-AC-DC-E2E-011 | FE+BE |
| TC-AC-DC-296 | TC-AC-DC-E2E-011 | FE+BE |
| TC-AC-DC-297 | TC-AC-DC-E2E-012 | FE+BE |
| TC-AC-DC-298 | TC-AC-DC-E2E-012 | FE+BE |
| TC-AC-DC-299 | TC-AC-DC-E2E-006 | FE+BE |
| TC-AC-DC-300 | TC-AC-DC-E2E-086 | FE+BE |
| TC-AC-DC-301 | TC-AC-DC-E2E-012 | FE+BE |
| TC-AC-DC-302 | TC-AC-DC-E2E-015 | FE+BE |
| TC-AC-DC-303 | TC-AC-DC-E2E-002 | FE+BE |
| TC-AC-DC-304 | TC-AC-DC-E2E-050 | FE+BE |
| TC-AC-DC-305 | TC-AC-DC-E2E-051 | FE+BE |
| TC-AC-DC-306 | TC-AC-DC-E2E-028 | FE+BE |
| TC-AC-DC-307 | TC-AC-DC-E2E-006 | FE+BE |
| TC-AC-DC-308 | TC-AC-DC-E2E-037 | FE+BE |
