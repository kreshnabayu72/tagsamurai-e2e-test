# Coverage E2E — Fixed Asset > Settings > Asset Labeling

Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md` (593 TC granular aktif); `tc-settings-asset-labeling-backend.md` hanya dibaca untuk menandai TC hanya-BE (hasil: tidak ada).
Suite: `specs/FixedAsset/AssetLabeling/`.
Prefix Modul: `FA` + `LBL` (`TC-FA-LBL-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (180 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | Screening Tab Labels: Layout, Breadcrumb, Tab Aktif, dan Format Sel Baris (bagian 1/2) | FE+BE | 41 | TC-FA-LBL-1, TC-FA-LBL-2, TC-FA-LBL-3, TC-FA-LBL-4, TC-FA-LBL-5, TC-FA-LBL-6, TC-FA-LBL-7 |
| TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | Screening Tab Labels: Kontras Chip, Urutan Default, Tooltip, Menu Row Action, Shimmer, dan Chip Panjang (bagian 2/2) | FE+BE | 37 | TC-FA-LBL-8, TC-FA-LBL-9, TC-FA-LBL-10, TC-FA-LBL-13, TC-FA-LBL-14, TC-FA-LBL-15, TC-FA-LBL-16 |
| TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong | Empty State Tabel dan Changelog (Company Kosong) | FE+BE | 31 | TC-FA-LBL-11, TC-FA-LBL-287, TC-FA-LBL-530, TC-FA-LBL-531 |
| TC-FA-LBL-E2E-004-pagination-labels-list-company-volume | Pagination Labels List (Company Volume) | FE+BE | 24 | TC-FA-LBL-17, TC-FA-LBL-278, TC-FA-LBL-279, TC-FA-LBL-280 |
| TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume | Retensi State Labels List dan Pagination Changelog (Company Volume) | FE+BE | 34 | TC-FA-LBL-18, TC-FA-LBL-19, TC-FA-LBL-20, TC-FA-LBL-324 |
| TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | Mobile: Card List Labels List, Menu Card per Role, Long-Press, Bottom Sheet Toolbar, dan Tooltip Disabled | FE+BE | 40 | TC-FA-LBL-21, TC-FA-LBL-22, TC-FA-LBL-23, TC-FA-LBL-24, TC-FA-LBL-503, TC-FA-LBL-525 |
| TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | Mobile: Modal Create/Edit, Delete, Bulk Delete, Modal Changelog, dan Drawer | FE+BE | 39 | TC-FA-LBL-110, TC-FA-LBL-156, TC-FA-LBL-177, TC-FA-LBL-207, TC-FA-LBL-326, TC-FA-LBL-375 |
| TC-FA-LBL-E2E-008-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-1-dari-3 | Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 1/3) | FE+BE | 30 | TC-FA-LBL-25, TC-FA-LBL-26, TC-FA-LBL-27 |
| TC-FA-LBL-E2E-009-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-2-dari-3 | Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 2/3) | FE+BE | 26 | TC-FA-LBL-28, TC-FA-LBL-29, TC-FA-LBL-30 |
| TC-FA-LBL-E2E-010-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-3-dari-3 | Role Matrix: Visibilitas Kontrol Tab Labels per Role (bagian 3/3) | FE+BE | 19 | TC-FA-LBL-31, TC-FA-LBL-506 |
| TC-FA-LBL-E2E-011-role-matrix-negatif-tab-labels-hidden-dan-akses-url-langsung-tanpa-capability | Role Matrix Negatif: Tab Labels Hidden dan Akses URL Langsung tanpa Capability | FE+BE | 12 | TC-FA-LBL-32, TC-FA-LBL-33, TC-FA-LBL-511 |
| TC-FA-LBL-E2E-012-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role | Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 1/2) | FE+BE | 24 | TC-FA-LBL-34, TC-FA-LBL-35, TC-FA-LBL-43 |
| TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | Role Matrix Positif: Aksi Baca (Download, Changelog, Drawer) per Role | FE+BE | 26 | TC-FA-LBL-38, TC-FA-LBL-39, TC-FA-LBL-40, TC-FA-LBL-41, TC-FA-LBL-44 |
| TC-FA-LBL-E2E-014-role-matrix-negatif-kolom-checkbox-bulk-action-bar-dan-tombol-plus-asset-name-per-role | Role Matrix Negatif: Kolom Checkbox, Bulk Action Bar, dan Tombol [➕] Asset Name per Role | FE+BE | 17 | TC-FA-LBL-205, TC-FA-LBL-524 |
| TC-FA-LBL-E2E-015-hak-akses-dicabut-saat-modal-atau-dialog-terbuka | Hak Akses Dicabut Saat Modal atau Dialog Terbuka | FE+BE | 38 | TC-FA-LBL-109, TC-FA-LBL-155, TC-FA-LBL-176 |
| TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | State Tenant: Write Lockdown Client Suspended (Create, Edit, Delete, Bulk Delete, dan Permintaan Langsung) | FE+BE | 40 | TC-FA-LBL-107, TC-FA-LBL-154, TC-FA-LBL-175, TC-FA-LBL-206, TC-FA-LBL-459 |
| TC-FA-LBL-E2E-017-state-tenant-perilaku-create-edit-delete-di-plan-terendah-dan-enterprise | State Tenant: Perilaku Create/Edit/Delete di Plan Terendah dan Enterprise | FE+BE | 40 | TC-FA-LBL-106, TC-FA-LBL-476 |
| TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 1/2) | FE+BE | 33 | TC-FA-LBL-45, TC-FA-LBL-46, TC-FA-LBL-47, TC-FA-LBL-48, TC-FA-LBL-504 |
| TC-FA-LBL-E2E-019-screening-popup-create-label-palet-preset-16-swatch | Screening Popup Create Label, Color Picker Overlay, dan Palet Preset (bagian 2/2) | FE+BE | 7 | TC-FA-LBL-510 |
| TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste | Color Picker Create: Input Warna Valid (Kanvas, Hex, dan Paste) | FE+BE | 21 | TC-FA-LBL-50, TC-FA-LBL-51, TC-FA-LBL-52, TC-FA-LBL-53 |
| TC-FA-LBL-E2E-021-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-1 | Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 1/2) | FE+BE | 27 | TC-FA-LBL-54, TC-FA-LBL-55, TC-FA-LBL-56 |
| TC-FA-LBL-E2E-022-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-2 | Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 2/2) | FE+BE | 18 | TC-FA-LBL-57, TC-FA-LBL-58 |
| TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1 | Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 1/2) | FE+BE | 31 | TC-FA-LBL-59, TC-FA-LBL-60, TC-FA-LBL-61, TC-FA-LBL-62 |
| TC-FA-LBL-E2E-024-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-2 | Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 2/2) | FE+BE | 18 | TC-FA-LBL-512 |
| TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | Live Preview Label: Nama, Warna, dan Warna Teks Kontras | FE+BE | 22 | TC-FA-LBL-63, TC-FA-LBL-64, TC-FA-LBL-65, TC-FA-LBL-66, TC-FA-LBL-67, TC-FA-LBL-68 |
| TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 1/2) | FE+BE | 32 | TC-FA-LBL-69, TC-FA-LBL-70, TC-FA-LBL-71, TC-FA-LBL-73, TC-FA-LBL-80, TC-FA-LBL-81 |
| TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2 | Validasi Label Name Create: Kosong, Spasi, Panjang, Emoji, dan Trim (bagian 2/2) | FE+BE | 27 | TC-FA-LBL-72, TC-FA-LBL-74, TC-FA-LBL-75, TC-FA-LBL-82 |
| TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal | Duplikat Nama Label Create (Debounce, Case-Insensitive, dan Cek Keunikan Gagal) | FE+BE | 32 | TC-FA-LBL-76, TC-FA-LBL-77, TC-FA-LBL-78, TC-FA-LBL-79 |
| TC-FA-LBL-E2E-029-submit-create-clear-field-saving-state-dan-klik-ganda | Submit Create: Clear Field, Saving State, dan Klik Ganda | FE+BE | 28 | TC-FA-LBL-83, TC-FA-LBL-91, TC-FA-LBL-90 |
| TC-FA-LBL-E2E-030-submit-create-duplikat-ditolak-server-simpan-stay-tidak-dicentang-dan-warna-huruf-kapital | Submit Create: Duplikat Ditolak Server, Simpan dengan Stay Tidak Dicentang, dan Warna Huruf Kapital | FE+BE | 43 | TC-FA-LBL-87, TC-FA-LBL-84, TC-FA-LBL-85 |
| TC-FA-LBL-E2E-031-create-dari-tombol-plus-pada-tab-asset-name | Create dari Tombol [+] pada Tab Asset Name | FE+BE | 18 | TC-FA-LBL-100, TC-FA-LBL-502 |
| TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default | Menutup Form Create: Form Bersih, Unsaved Changes, Esc, dan Warna Default (bagian 1/2) | FE+BE | 32 | TC-FA-LBL-92, TC-FA-LBL-93, TC-FA-LBL-94, TC-FA-LBL-95 |
| TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route | Menutup Form Create: Form Dikembalikan, Backdrop, Reload, dan Pindah Route (bagian 2/2) | FE+BE | 32 | TC-FA-LBL-96, TC-FA-LBL-97, TC-FA-LBL-98, TC-FA-LBL-99 |
| TC-FA-LBL-E2E-034-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-1 | Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 1/2) | FE+BE | 37 | TC-FA-LBL-103, TC-FA-LBL-102, TC-FA-LBL-104 |
| TC-FA-LBL-E2E-035-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-2 | Batas Katalog Master Data Count Limit (D-06) pada Create (bagian 2/2) | FE+BE | 23 | TC-FA-LBL-101, TC-FA-LBL-505, TC-FA-LBL-105 |
| TC-FA-LBL-E2E-036-screening-dan-accessibility-popup-edit-label | Screening dan Accessibility Popup Edit Label | FE+BE | 21 | TC-FA-LBL-111, TC-FA-LBL-112 |
| TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 1/2) | FE+BE | 32 | TC-FA-LBL-114, TC-FA-LBL-115, TC-FA-LBL-117, TC-FA-LBL-123, TC-FA-LBL-124, TC-FA-LBL-485 |
| TC-FA-LBL-E2E-038-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-2 | Validasi Label Name Edit: Kosong, Spasi, Panjang, Trim, dan Emoji (bagian 2/2) | FE+BE | 18 | TC-FA-LBL-116, TC-FA-LBL-118, TC-FA-LBL-486 |
| TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri | Duplikat Nama Label Edit: Deteksi Setelah Debounce dan Kapitalisasi Sendiri | FE+BE | 19 | TC-FA-LBL-119, TC-FA-LBL-120, TC-FA-LBL-121, TC-FA-LBL-122 |
| TC-FA-LBL-E2E-040-duplikat-nama-label-edit-debounce-500-ms-cek-gagal-dan-save-ditolak-server | Duplikat Nama Label Edit: Debounce 500 ms, Cek Gagal, dan Save Ditolak Server | FE+BE | 32 | TC-FA-LBL-140, TC-FA-LBL-487, TC-FA-LBL-488 |
| TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay | Edit: Validasi Kode Hex Tidak Valid pada Color Picker Overlay | FE+BE | 25 | TC-FA-LBL-125, TC-FA-LBL-126, TC-FA-LBL-127, TC-FA-LBL-128 |
| TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil | Edit: Pemilihan Warna Valid pada Color Picker dan Simpan Hex Huruf Kecil | FE+BE | 29 | TC-FA-LBL-129, TC-FA-LBL-130, TC-FA-LBL-131, TC-FA-LBL-489 |
| TC-FA-LBL-E2E-043-edit-penutupan-color-picker-overlay-tanpa-menutup-modal-edit | Edit: Penutupan Color Picker Overlay Tanpa Menutup Modal Edit | FE+BE | 27 | TC-FA-LBL-526 |
| TC-FA-LBL-E2E-044-edit-save-zero-delta-tanpa-perubahan-spasi-tepi-hex-huruf-kecil | Edit: Save Zero-Delta (Tanpa Perubahan, Spasi Tepi, Hex Huruf Kecil) | FE+BE | 23 | TC-FA-LBL-134, TC-FA-LBL-135, TC-FA-LBL-136 |
| TC-FA-LBL-E2E-045-edit-simpan-perubahan-nama-warna-dan-keduanya | Edit: Simpan Perubahan Nama, Warna, dan Keduanya | FE+BE | 28 | TC-FA-LBL-137, TC-FA-LBL-138, TC-FA-LBL-139 |
| TC-FA-LBL-E2E-046-edit-klik-ganda-save-dan-saving-state | Edit: Klik Ganda Save dan Saving State | FE+BE | 15 | TC-FA-LBL-145, TC-FA-LBL-146 |
| TC-FA-LBL-E2E-047-menutup-form-edit-penutupan-bersih-dan-dialog-unsaved-changes-lewat-tombol-tutup | Menutup Form Edit: Penutupan Bersih dan Dialog Unsaved Changes lewat Tombol Tutup | FE+BE | 25 | TC-FA-LBL-147, TC-FA-LBL-148, TC-FA-LBL-150 |
| TC-FA-LBL-E2E-048-menutup-form-edit-reload-dan-pindah-route-saat-form-berubah | Menutup Form Edit: Reload dan Pindah Route Saat Form Berubah | FE+BE | 20 | TC-FA-LBL-152, TC-FA-LBL-153 |
| TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | Edit dan Buka Edit Saat Label Diubah atau Dihapus Admin Lain (Sesi API Admin Kedua) | FE+BE | 36 | TC-FA-LBL-113, TC-FA-LBL-469, TC-FA-LBL-470, TC-FA-LBL-482, TC-FA-LBL-483 |
| TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda | Dialog Delete D-01: Screening, Cancel, Esc/Backdrop, dan Klik Ganda | FE+BE | 24 | TC-FA-LBL-157, TC-FA-LBL-158, TC-FA-LBL-159, TC-FA-LBL-172 |
| TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2 | Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 1/2) | FE+BE | 31 | TC-FA-LBL-162, TC-FA-LBL-163, TC-FA-LBL-164, TC-FA-LBL-165 |
| TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2 | Dialog D-02 Label Dipakai atau Default Label (Hitungan Jamak/Tunggal, Status Aset) (bagian 2/2) | FE+BE | 32 | TC-FA-LBL-166, TC-FA-LBL-169, TC-FA-LBL-186, TC-FA-LBL-195 |
| TC-FA-LBL-E2E-053-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-1-2 | Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 1/2) | FE+BE | 32 | TC-FA-LBL-173, TC-FA-LBL-174, TC-FA-LBL-197 |
| TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2 | Delete Saat Label Berubah Antara Dialog dan Konfirmasi (Sesi API Admin Kedua) (bagian 2/2) | FE+BE | 34 | TC-FA-LBL-196, TC-FA-LBL-198, TC-FA-LBL-199, TC-FA-LBL-468 |
| TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | Bulk Delete: Dialog D-03 Homogen Bersih dan Seleksi | FE+BE | 34 | TC-FA-LBL-185, TC-FA-LBL-187, TC-FA-LBL-188, TC-FA-LBL-189, TC-FA-LBL-203, TC-FA-LBL-498 |
| TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai | Bulk Delete: Dialog D-04 Campuran (Label Bersih dan Label Dipakai) | FE+BE | 30 | TC-FA-LBL-191, TC-FA-LBL-192, TC-FA-LBL-193, TC-FA-LBL-194 |
| TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3 | Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 1/3) | FE+BE | 32 | TC-FA-LBL-178, TC-FA-LBL-179, TC-FA-LBL-181, TC-FA-LBL-182 |
| TC-FA-LBL-E2E-058-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-2-3 | Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 2/3) | FE+BE | 31 | TC-FA-LBL-180, TC-FA-LBL-190, TC-FA-LBL-204 |
| TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir | Delete dan Bulk Delete Berhasil: Pembersihan Relasi Aset Deleted dan Halaman Terakhir | FE+BE | 24 | TC-FA-LBL-160, TC-FA-LBL-161, TC-FA-LBL-281, TC-FA-LBL-499 |
| TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | Search Labels List: Toolbar, Kelas Label dan Color Hex, serta Empty State | FE+BE | 39 | TC-FA-LBL-208, TC-FA-LBL-209, TC-FA-LBL-210, TC-FA-LBL-211, TC-FA-LBL-212 |
| TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | Search Labels List: Modified By, Guard Kolom, Trim, dan Visibilitas Kolom | FE+BE | 35 | TC-FA-LBL-213, TC-FA-LBL-214, TC-FA-LBL-215, TC-FA-LBL-216, TC-FA-LBL-217, TC-FA-LBL-218, TC-FA-LBL-219, TC-FA-LBL-507 |
| TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | Filter Labels List: Panel, Total Asset, dan Dropdown Modified By | FE+BE | 31 | TC-FA-LBL-220, TC-FA-LBL-221, TC-FA-LBL-222, TC-FA-LBL-223, TC-FA-LBL-224, TC-FA-LBL-225 |
| TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | Filter Labels List: Modified By Multi-Pilih, Chip, dan Last Updated | FE+BE | 33 | TC-FA-LBL-226, TC-FA-LBL-227, TC-FA-LBL-228, TC-FA-LBL-229, TC-FA-LBL-230, TC-FA-LBL-231 |
| TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel | Filter Labels List: Kombinasi Field, Search dan Filter, serta Draft Panel | FE+BE | 32 | TC-FA-LBL-232, TC-FA-LBL-233, TC-FA-LBL-234, TC-FA-LBL-235 |
| TC-FA-LBL-E2E-065-filter-labels-list-independen-kolom-clear-field-dan-opsi-baru | Filter Labels List: Independen dari Visibilitas Kolom, Clear Field, dan Opsi Modified By Baru | FE+BE | 28 | TC-FA-LBL-237, TC-FA-LBL-238, TC-FA-LBL-240 |
| TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | Sort Labels List: Tiga Tahap per Kolom dan Perpindahan Kolom Sort | FE+BE | 12 | TC-FA-LBL-241, TC-FA-LBL-242, TC-FA-LBL-243, TC-FA-LBL-244, TC-FA-LBL-245, TC-FA-LBL-246 |
| TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan | Kombinasi Search, Filter, Sort, dan Pagination Labels List serta Pemulihan Saringan | FE+BE | 39 | TC-FA-LBL-247, TC-FA-LBL-249, TC-FA-LBL-250, TC-FA-LBL-251 |
| TC-FA-LBL-E2E-068-kombinasi-search-filter-sort-empty-state-create-dan-edit | Kombinasi Search dan Filter Labels List: Empty State, Create, dan Edit saat Search Aktif | FE+BE | 26 | TC-FA-LBL-252, TC-FA-LBL-253, TC-FA-LBL-254 |
| TC-FA-LBL-E2E-069-setup-column-labels-list-overlay-popup-dan-ceklis | Setup Column Labels List: Overlay, Popup, dan Ceklis Kolom Hideable | FE+BE | 26 | TC-FA-LBL-255, TC-FA-LBL-256, TC-FA-LBL-257 |
| TC-FA-LBL-E2E-070-setup-column-labels-list-guard-satu-kolom-dan-konfigurasi-per-tabel | Setup Column Labels List: Guard Satu Kolom Tersisa dan Konfigurasi per Tabel | FE+BE | 19 | TC-FA-LBL-263, TC-FA-LBL-264 |
| TC-FA-LBL-E2E-071-setup-column-labels-list-drag-reorder-dan-pin | Setup Column Labels List: Drag Reorder dan Pin | FE+BE | 30 | TC-FA-LBL-258, TC-FA-LBL-259, TC-FA-LBL-260 |
| TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | Download Labels List: CSV dan XLSX, Nama Berkas, Kolom, dan Filter Aktif | FE+BE | 34 | TC-FA-LBL-266, TC-FA-LBL-267, TC-FA-LBL-268, TC-FA-LBL-269, TC-FA-LBL-271, TC-FA-LBL-272 |
| TC-FA-LBL-E2E-073-download-labels-list-nol-baris-dan-urutan-sort | Download Labels List: Nol Baris Hasil dan Urutan Baris Mengikuti Sort | FE+BE | 12 | TC-FA-LBL-274, TC-FA-LBL-276 |
| TC-FA-LBL-E2E-074-volume-download-seluruh-baris-dan-di-atas-5000-baris | Volume: Download Seluruh Baris dan di Atas 5.000 Baris | FE+BE | 13 | TC-FA-LBL-265, TC-FA-LBL-277 |
| TC-FA-LBL-E2E-075-isi-berkas-ekspor-labels-list-dan-changelog | Isi Berkas Ekspor Labels List dan Changelog: Nilai Sel, Escaping CSV, dan BOM | FE+BE | 27 | TC-FA-LBL-273, TC-FA-LBL-275, TC-FA-LBL-323 |
| TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup | Screening Modal Changelog: Labels, Format Sel, Shimmer, dan Menutup | FE+BE | 34 | TC-FA-LBL-284, TC-FA-LBL-285, TC-FA-LBL-286, TC-FA-LBL-289 |
| TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | Search Modal Changelog (bagian 1/2) | FE+BE | 27 | TC-FA-LBL-290, TC-FA-LBL-291, TC-FA-LBL-292, TC-FA-LBL-293, TC-FA-LBL-294 |
| TC-FA-LBL-E2E-078-search-modal-changelog-bagian-2-2 | Search Modal Changelog (bagian 2/2) | FE+BE | 31 | TC-FA-LBL-295, TC-FA-LBL-492, TC-FA-LBL-508 |
| TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | Filter Modal Changelog (bagian 1/2) | FE+BE | 35 | TC-FA-LBL-296, TC-FA-LBL-297, TC-FA-LBL-298, TC-FA-LBL-299, TC-FA-LBL-300 |
| TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2 | Filter Modal Changelog (bagian 2/2) | FE+BE | 34 | TC-FA-LBL-301, TC-FA-LBL-302, TC-FA-LBL-303, TC-FA-LBL-304 |
| TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | Sort Modal Changelog (bagian 1/2) | FE+BE | 34 | TC-FA-LBL-305, TC-FA-LBL-306, TC-FA-LBL-307, TC-FA-LBL-308, TC-FA-LBL-309 |
| TC-FA-LBL-E2E-082-sort-modal-changelog-bagian-2-2 | Sort Modal Changelog (bagian 2/2) | FE+BE | 27 | TC-FA-LBL-310, TC-FA-LBL-311, TC-FA-LBL-325 |
| TC-FA-LBL-E2E-083-setup-column-modal-changelog-bagian-1-3 | Setup Column Modal Changelog (bagian 1/3) | FE+BE | 15 | TC-FA-LBL-312, TC-FA-LBL-313 |
| TC-FA-LBL-E2E-084-setup-column-modal-changelog-bagian-2-3 | Setup Column Modal Changelog (bagian 2/3) | FE+BE | 33 | TC-FA-LBL-315, TC-FA-LBL-316 |
| TC-FA-LBL-E2E-085-setup-column-modal-changelog-bagian-3-3 | Setup Column Modal Changelog (bagian 3/3) | FE+BE | 16 | TC-FA-LBL-317, TC-FA-LBL-318 |
| TC-FA-LBL-E2E-086-download-modal-changelog-csv-xlsx-dan-filter-aktif | Download Modal Changelog: CSV, XLSX, dan Filter Aktif | FE+BE | 27 | TC-FA-LBL-319, TC-FA-LBL-320, TC-FA-LBL-321 |
| TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | Membuka dan Screening Drawer Tagged Asset (bagian 1/2) | FE+BE | 34 | TC-FA-LBL-327, TC-FA-LBL-328, TC-FA-LBL-329, TC-FA-LBL-330, TC-FA-LBL-331 |
| TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | Membuka dan Screening Drawer Tagged Asset (bagian 2/2) | FE+BE | 28 | TC-FA-LBL-334, TC-FA-LBL-336, TC-FA-LBL-373, TC-FA-LBL-374, TC-FA-LBL-509 |
| TC-FA-LBL-E2E-089-kolom-label-dan-badge-label-panjang-di-drawer | Kolom Label dan Badge Label Panjang di Drawer | FE+BE | 25 | TC-FA-LBL-370, TC-FA-LBL-371, TC-FA-LBL-501 |
| TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2 | Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 1/2) | FE+BE | 26 | TC-FA-LBL-513, TC-FA-LBL-514, TC-FA-LBL-515, TC-FA-LBL-516 |
| TC-FA-LBL-E2E-091-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-2-2 | Sel Multi-Nilai Status dan Label di Drawer (Sort, Search, Filter) (bagian 2/2) | FE+BE | 20 | TC-FA-LBL-517, TC-FA-LBL-518 |
| TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | Search Drawer Tagged Asset (bagian 1/2) | FE+BE | 26 | TC-FA-LBL-338, TC-FA-LBL-339, TC-FA-LBL-340, TC-FA-LBL-341, TC-FA-LBL-342, TC-FA-LBL-343 |
| TC-FA-LBL-E2E-093-search-drawer-tagged-asset-bagian-2-2 | Search Drawer Tagged Asset (bagian 2/2) | FE+BE | 33 | TC-FA-LBL-344, TC-FA-LBL-345, TC-FA-LBL-493 |
| TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2 | Filter Drawer Tagged Asset (bagian 1/2) | FE+BE | 22 | TC-FA-LBL-346, TC-FA-LBL-347, TC-FA-LBL-348, TC-FA-LBL-349 |
| TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | Filter Drawer Tagged Asset (bagian 2/2) | FE+BE | 29 | TC-FA-LBL-351, TC-FA-LBL-352, TC-FA-LBL-353, TC-FA-LBL-354, TC-FA-LBL-575 |
| TC-FA-LBL-E2E-096-filter-category-modal-tree-picker | Filter Category: Modal Tree Picker | FE+BE | 33 | TC-FA-LBL-350, TC-FA-LBL-527, TC-FA-LBL-528, TC-FA-LBL-529 |
| TC-FA-LBL-E2E-097-sort-drawer-tagged-asset-asset-id-dan-kolom-badge | Sort Drawer Tagged Asset: Asset ID dan Kolom Badge | FE+BE | 16 | TC-FA-LBL-356, TC-FA-LBL-357 |
| TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker | Sort Drawer Tagged Asset: Status, Last Updated, Label, dan Tie-Breaker | FE+BE | 28 | TC-FA-LBL-358, TC-FA-LBL-359, TC-FA-LBL-360, TC-FA-LBL-361 |
| TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated | Setup Column Drawer: Overlay, Popup, Guard, dan Kolom Curated | FE+BE | 29 | TC-FA-LBL-362, TC-FA-LBL-363, TC-FA-LBL-365, TC-FA-LBL-369 |
| TC-FA-LBL-E2E-100-setup-column-drawer-reset-to-default-discard-dan-pin | Setup Column Drawer: Reset to Default, Discard, dan Pin | FE+BE | 35 | TC-FA-LBL-367, TC-FA-LBL-368 |
| TC-FA-LBL-E2E-101-setup-column-drawer-drag-reorder | Setup Column Drawer: Drag Reorder | FE+BE | 11 | TC-FA-LBL-366 |
| TC-FA-LBL-E2E-102-empty-state-drawer-dan-filter-panel-drawer-pada-sumber-0-baris | Empty State Drawer dan Filter Panel Drawer pada Sumber 0 Baris | FE+BE | 19 | TC-FA-LBL-335, TC-FA-LBL-532 |
| TC-FA-LBL-E2E-103-volume-drawer-label-500-aset-d-02-500-aset-sort-natural-pagination | Volume: Drawer Label 500 Aset (D-02 500 Aset, Sort Natural, Pagination) | FE+BE | 31 | TC-FA-LBL-167, TC-FA-LBL-355, TC-FA-LBL-372 |
| TC-FA-LBL-E2E-104-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-1-2 | Drawer Kolom Baru: TAG, Measurement, Last Scanned, dan Transactional Policy (bagian 1/2) | FE+BE | 33 | TC-FA-LBL-536, TC-FA-LBL-538, TC-FA-LBL-543 |
| TC-FA-LBL-E2E-105-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-2-2 | Drawer Kolom Baru: TAG, Measurement, Last Scanned, dan Transactional Policy (bagian 2/2) | FE+BE | 15 | TC-FA-LBL-544 |
| TC-FA-LBL-E2E-106-drawer-kolom-baru-setup-column-guard-dan-search-bagian-1-2 | Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 1/2) | FE+BE | 34 | TC-FA-LBL-533, TC-FA-LBL-537, TC-FA-LBL-539 |
| TC-FA-LBL-E2E-107-drawer-kolom-baru-setup-column-guard-dan-search-bagian-2-2 | Drawer Kolom Baru: Setup Column, Guard, dan Search (bagian 2/2) | FE+BE | 19 | TC-FA-LBL-567 |
| TC-FA-LBL-E2E-108-drawer-kolom-baru-sort-measurement-transactional-policy-last-scanned-dan-tag | Drawer Kolom Baru: Sort Measurement, Transactional Policy, Last Scanned, dan TAG | FE+BE | 36 | TC-FA-LBL-540, TC-FA-LBL-574 |
| TC-FA-LBL-E2E-109-drawer-kolom-baru-filter-sumber-0-baris-dan-sort-tag-awalan-pendek | Drawer Kolom Baru: Filter Sumber 0 Baris dan Sort TAG Awalan Pendek | FE+BE | 21 | TC-FA-LBL-542, TC-FA-LBL-588 |
| TC-FA-LBL-E2E-110-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-1-2 | Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 1/2) | FE+BE | 44 | TC-FA-LBL-577, TC-FA-LBL-578 |
| TC-FA-LBL-E2E-111-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-2-2 | Drawer Kolom Custom Field Tipe Dasar (Company Fields) (bagian 2/2) | FE+BE | 35 | TC-FA-LBL-579, TC-FA-LBL-580 |
| TC-FA-LBL-E2E-112-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-1-2 | Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 1/2) | FE+BE | 31 | TC-FA-LBL-589, TC-FA-LBL-590, TC-FA-LBL-592 |
| TC-FA-LBL-E2E-113-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-2-2 | Drawer Kolom Asset Value Commercial dan Fiscal (Company Depreciation) (bagian 2/2) | FE+BE | 35 | TC-FA-LBL-591, TC-FA-LBL-593 |
| TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | Penanda Masa Garansi Warranty Expiry (Company Warranty) | FE+BE | 44 | TC-FA-LBL-582, TC-FA-LBL-583, TC-FA-LBL-584, TC-FA-LBL-585, TC-FA-LBL-587 |
| TC-FA-LBL-E2E-115-warranty-expiry-hari-ini-mengikuti-time-zone-general-settings | Warranty Expiry: Hari Ini Mengikuti Time Zone General Settings | FE+BE | 7 | TC-FA-LBL-586 |
| TC-FA-LBL-E2E-116-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-1-2 | Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 1/2) | FE+BE | 50 | TC-FA-LBL-534, TC-FA-LBL-535, TC-FA-LBL-553 |
| TC-FA-LBL-E2E-117-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-2-2 | Gate-Full: Kolom Custom Field, Setup Column, dan Pin (bagian 2/2) | FE+BE | 15 | TC-FA-LBL-560 |
| TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2 | Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 1/2) | FE+BE | 39 | TC-FA-LBL-546, TC-FA-LBL-557, TC-FA-LBL-559, TC-FA-LBL-576 |
| TC-FA-LBL-E2E-119-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-2-2 | Gate-Value: Asset Value dan Sel No access (Sort, Filter, Search, Tooltip, Request Langsung) (bagian 2/2) | FE+BE | 22 | TC-FA-LBL-551, TC-FA-LBL-566 |
| TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | Gate-Purchase: Warranty Expiry dan Custom Field Purchasing | FE+BE | 40 | TC-FA-LBL-549, TC-FA-LBL-555, TC-FA-LBL-558, TC-FA-LBL-562, TC-FA-LBL-570 |
| TC-FA-LBL-E2E-121-gate-accounting-asset-value-dan-custom-field-accounting | Gate-Accounting: Asset Value dan Custom Field Accounting | FE+BE | 19 | TC-FA-LBL-545, TC-FA-LBL-556 |
| TC-FA-LBL-E2E-122-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-1-2 | Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 1/2) | FE+BE | 21 | TC-FA-LBL-547, TC-FA-LBL-554 |
| TC-FA-LBL-E2E-123-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-2-2 | Gate-None: Pemegang View Tagged Assets tanpa Hak Nilai (bagian 2/2) | FE+BE | 9 | TC-FA-LBL-561 |
| TC-FA-LBL-E2E-124-gate-tier-group-branch-total-control-default-user-read-only-dan-group-manager | Gate Tier: Group Branch, Total Control, Default User, Read Only, dan Group Manager | FE+BE | 32 | TC-FA-LBL-548, TC-FA-LBL-568, TC-FA-LBL-569 |
| TC-FA-LBL-E2E-125-lisensi-fa-7-kolom-custom-field-accounting-grace-period-dan-tidak-aktif | Lisensi FA-7: Kolom Custom Field Accounting (Grace Period dan Tidak Aktif) | FE+BE | 19 | TC-FA-LBL-571, TC-FA-LBL-572, TC-FA-LBL-573 |
| TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | Pencatatan Create di Changelog, System Log, dan Activity Log | FE+BE | 54 | TC-FA-LBL-376, TC-FA-LBL-377, TC-FA-LBL-378, TC-FA-LBL-389, TC-FA-LBL-408 |
| TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | Pencatatan Edit Nama di Tiga Surface dan Pembaruan Modified By | FE+BE | 53 | TC-FA-LBL-379, TC-FA-LBL-380, TC-FA-LBL-381, TC-FA-LBL-388, TC-FA-LBL-406 |
| TC-FA-LBL-E2E-128-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface | Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 1/2) | FE+BE | 30 | TC-FA-LBL-382, TC-FA-LBL-383, TC-FA-LBL-384 |
| TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | Pencatatan Delete dan Bulk Delete di Tiga Surface | FE+BE | 54 | TC-FA-LBL-390, TC-FA-LBL-391, TC-FA-LBL-392, TC-FA-LBL-393, TC-FA-LBL-394, TC-FA-LBL-395 |
| TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface | Snapshot Log Immutable, Label Hasil Import, dan Kolom Tiap Surface | FE+BE | 61 | TC-FA-LBL-404, TC-FA-LBL-405, TC-FA-LBL-407, TC-FA-LBL-411 |
| TC-FA-LBL-E2E-131-pencatatan-lewat-request-langsung-create-edit-dan-delete | Pencatatan Lewat Request Langsung: Create, Edit, dan Delete | FE+BE | 37 | TC-FA-LBL-409, TC-FA-LBL-494, TC-FA-LBL-495 |
| TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard | Absence Log: Bulk Delete Campuran atau Gagal, Dialog OK Tanpa Mutasi, dan Penolakan Guard | FE+BE | 41 | TC-FA-LBL-168, TC-FA-LBL-396, TC-FA-LBL-397, TC-FA-LBL-400 |
| TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain | Absence Log: Edit Zero-Delta, Spasi Tepi, Request Langsung, dan Label Lain | FE+BE | 28 | TC-FA-LBL-398, TC-FA-LBL-399, TC-FA-LBL-403, TC-FA-LBL-410 |
| TC-FA-LBL-E2E-134-absence-log-batas-katalog-dan-import-di-batas-company-limit | Absence Log: Batas Katalog dan Import di Batas (Company Limit) | FE+BE | 27 | TC-FA-LBL-401, TC-FA-LBL-458, TC-FA-LBL-484 |
| TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | Resilience Baca dan Ekspor: Error Load Tabel, Changelog, Drawer, dan Download Gagal | FE+BE | 37 | TC-FA-LBL-12, TC-FA-LBL-270, TC-FA-LBL-288, TC-FA-LBL-322, TC-FA-LBL-337 |
| TC-FA-LBL-E2E-136-resilience-create-5xx-dan-timeout | Resilience Create: 5xx dan Timeout | FE+BE | 29 | TC-FA-LBL-88, TC-FA-LBL-89 |
| TC-FA-LBL-E2E-137-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-1-2 | Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 1/2) | FE+BE | 35 | TC-FA-LBL-170, TC-FA-LBL-171, TC-FA-LBL-200 |
| TC-FA-LBL-E2E-138-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-2-2 | Resilience Delete dan Bulk Delete: 5xx dan Timeout di Tengah Proses (Bagian 2/2) | FE+BE | 28 | TC-FA-LBL-201, TC-FA-LBL-202 |
| TC-FA-LBL-E2E-139-sinkron-label-baru-ke-asset-detail-reports-dan-default-label-asset-name | Sinkron Label Baru ke Asset Detail, Reports, dan Default Label Asset Name | FE+BE | 21 | TC-FA-LBL-412, TC-FA-LBL-413, TC-FA-LBL-414 |
| TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy | Sinkron Rename Label ke Asset List, Asset Detail, Reports, dan Asset Transactional Policy | FE+BE | 30 | TC-FA-LBL-415, TC-FA-LBL-416, TC-FA-LBL-417, TC-FA-LBL-418 |
| TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen | Sinkron Delete Label (Single dan Bulk) ke Konsumen | FE+BE | 31 | TC-FA-LBL-420, TC-FA-LBL-421, TC-FA-LBL-422, TC-FA-LBL-522 |
| TC-FA-LBL-E2E-142-total-asset-realtime-dan-aset-deleted | Total Asset Realtime dan Aset Deleted | FE+BE | 27 | TC-FA-LBL-423, TC-FA-LBL-424, TC-FA-LBL-434 |
| TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label | Provenance Label Default dan Manual di Asset Detail serta Bulk Add dan Bulk Remove Label | FE+BE | 23 | TC-FA-LBL-425, TC-FA-LBL-426, TC-FA-LBL-427, TC-FA-LBL-428 |
| TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed | Cascade Default Label pada Asset Name (Draft, Waiting for Approval, Active, Disposed) | FE+BE | 38 | TC-FA-LBL-429, TC-FA-LBL-430, TC-FA-LBL-431, TC-FA-LBL-432 |
| TC-FA-LBL-E2E-145-label-hasil-import-edit-dan-delete-identik-dengan-create-manual | Label Hasil Import: Edit dan Delete Identik dengan Create Manual | FE+BE | 18 | TC-FA-LBL-435, TC-FA-LBL-436 |
| TC-FA-LBL-E2E-146-format-tanggal-jam-dan-timezone-general-settings-di-labels-list-changelog-dan-drawer | Format Tanggal, Jam, dan Timezone General Settings di Labels List, Changelog, dan Drawer | FE+BE | 20 | TC-FA-LBL-437, TC-FA-LBL-438, TC-FA-LBL-439 |
| TC-FA-LBL-E2E-147-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot | Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 1/2) | FE+BE | 22 | TC-FA-LBL-440, TC-FA-LBL-478 |
| TC-FA-LBL-E2E-148-sinkron-kolom-drawer-dari-modul-lain-transactional-policy-custom-field-last-scanned | Sinkron Kolom Drawer dari Modul Lain (Transactional Policy, Custom Field, Last Scanned) | FE+BE | 26 | TC-FA-LBL-563, TC-FA-LBL-564, TC-FA-LBL-565 |
| TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | Request Langsung Ditolak per Role (Aksi Tulis): Read Only, Create-Only, dan Update-Only | FE+BE | 32 | TC-FA-LBL-441, TC-FA-LBL-442, TC-FA-LBL-443, TC-FA-LBL-444, TC-FA-LBL-445, TC-FA-LBL-446, TC-FA-LBL-447 |
| TC-FA-LBL-E2E-150-request-langsung-ditolak-per-role-aksi-tulis-delete-only-dan-read-capability | Request Langsung Ditolak per Role (Aksi Tulis): Delete-Only dan Read-Capability | FE+BE | 20 | TC-FA-LBL-448, TC-FA-LBL-449, TC-FA-LBL-450 |
| TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label | Request Langsung: Tanpa Capability, Jalur Baca Hanya-Baca, dan Pelepasan Relasi Label | FE+BE | 36 | TC-FA-LBL-451, TC-FA-LBL-452, TC-FA-LBL-460, TC-FA-LBL-481 |
| TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | Request Langsung Total Control: Validasi Warna, Validasi Nama, dan Delete Label yang Dipakai | FE+BE | 25 | TC-FA-LBL-453, TC-FA-LBL-454, TC-FA-LBL-455, TC-FA-LBL-456, TC-FA-LBL-457 |
| TC-FA-LBL-E2E-153-defense-in-depth-ui-payload-script-dan-sql-serta-isolasi-tenant | Defense-in-Depth UI: Payload Script dan SQL serta Isolasi Tenant | FE+BE | 39 | TC-FA-LBL-461, TC-FA-LBL-462, TC-FA-LBL-463 |
| TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form | Race Dua Sesi: Create dan Edit Nama Sama serta Import versus Form | FE+BE | 37 | TC-FA-LBL-465, TC-FA-LBL-466, TC-FA-LBL-467, TC-FA-LBL-477 |
| TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete | Race Dua Sesi: Penempelan Label versus Delete dan Bulk Delete | FE+BE | 31 | TC-FA-LBL-464, TC-FA-LBL-472, TC-FA-LBL-473, TC-FA-LBL-474 |
| TC-FA-LBL-E2E-156-race-dua-sesi-slot-terakhir-master-data-count-limit | Race Dua Sesi: Slot Terakhir Master Data Count Limit | FE+BE | 13 | TC-FA-LBL-471 |
| TC-FA-LBL-E2E-157-state-tenant-write-lockdown-client-expired-create-dan-seluruh-aksi-tulis-dengan-baca-tetap-diizinkan | State Tenant: Write Lockdown Client Expired (Create dan Seluruh Aksi Tulis dengan Baca Tetap Diizinkan) | FE+BE | 36 | TC-FA-LBL-108, TC-FA-LBL-475 |
| TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume | Pagination bersama Filter, Search, Sort, dan Urutan Tie-Break (Company Volume) | FE+BE | 22 | TC-FA-LBL-239, TC-FA-LBL-248, TC-FA-LBL-282, TC-FA-LBL-283 |
| TC-FA-LBL-E2E-159-color-picker-create-klik-tiap-swatch-preset | Color Picker Create: Klik Tiap Swatch Preset Menyetel Hex, Swatch Trigger, dan Live Preview | FE+BE | 10 | TC-FA-LBL-49 |
| TC-FA-LBL-E2E-160-submit-create-stay-dicentang-form-direset-dan-modal-tetap-terbuka | Submit Create dengan Stay Dicentang: Form Direset dan Modal Tetap Terbuka | FE+BE | 22 | TC-FA-LBL-86 |
| TC-FA-LBL-E2E-161-menutup-form-edit-klik-backdrop-dan-esc-saat-form-berubah | Menutup Form Edit: Klik Backdrop dan Esc Saat Form Berubah | FE+BE | 20 | TC-FA-LBL-149, TC-FA-LBL-151 |
| TC-FA-LBL-E2E-162-edit-live-preview-dan-clear-field | Edit: Live Preview dan Clear Field | FE+BE | 17 | TC-FA-LBL-132, TC-FA-LBL-133 |
| TC-FA-LBL-E2E-164-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-3-3 | Volume: Bulk Action Bar, Select All, Selection Limit, dan Seleksi Lintas Halaman (bagian 3/3) | FE+BE | 18 | TC-FA-LBL-183, TC-FA-LBL-184 |
| TC-FA-LBL-E2E-165-filter-labels-list-opsi-tanpa-nilai-kosong-dan-indikator-titik | Filter Labels List: Opsi Tanpa Nilai Kosong dan Indikator Titik | FE+BE | 12 | TC-FA-LBL-236 |
| TC-FA-LBL-E2E-166-setup-column-labels-list-reset-to-default-dan-tutup-tanpa-simpan | Setup Column Labels List: Reset to Default dan Tutup Tanpa Simpan | FE+BE | 19 | TC-FA-LBL-261, TC-FA-LBL-262 |
| TC-FA-LBL-E2E-167-setup-column-modal-changelog-ceklis-dan-unceklis-kolom | Setup Column Modal Changelog: Ceklis dan Unceklis Kolom Hideable | FE+BE | 18 | TC-FA-LBL-314 |
| TC-FA-LBL-E2E-168-sort-modal-changelog-old-value-dan-new-value-campuran | Sort Modal Changelog: Old Value dan New Value Campuran Angka dan Teks | FE+BE | 14 | TC-FA-LBL-519 |
| TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset | Jumlah Baris, Format Sel, dan Truncation Badge di Drawer Tagged Asset | FE+BE | 34 | TC-FA-LBL-332, TC-FA-LBL-333, TC-FA-LBL-490, TC-FA-LBL-491 |
| TC-FA-LBL-E2E-170-setup-column-drawer-ceklis-dan-unceklis-kolom-hideable | Setup Column Drawer: Ceklis dan Unceklis Kolom Hideable | FE+BE | 14 | TC-FA-LBL-364 |
| TC-FA-LBL-E2E-171-drawer-kolom-baru-filter-tag-measurement-transactional-policy-dan-last-scanned | Drawer Kolom Baru: Filter TAG, Measurement, Transactional Policy, dan Last Scanned | FE+BE | 22 | TC-FA-LBL-541 |
| TC-FA-LBL-E2E-172-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role | Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 1/2) | FE+BE | 23 | TC-FA-LBL-550 |
| TC-FA-LBL-E2E-173-absence-log-aksi-gagal-5xx-pada-edit-create-dan-delete | Absence Log: Aksi Gagal 5xx pada Edit, Create, dan Delete | FE+BE | 38 | TC-FA-LBL-402, TC-FA-LBL-520, TC-FA-LBL-521 |
| TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal | Resilience Edit: 5xx dan Timeout pada Save dan Fetch Pembuka Modal | FE+BE | 41 | TC-FA-LBL-141, TC-FA-LBL-142, TC-FA-LBL-143, TC-FA-LBL-144 |
| TC-FA-LBL-E2E-175-perubahan-warna-label-tercermin-di-asset-list-asset-detail-reports-dan-asset-transactional-policy | Perubahan Warna Label Tercermin di Asset List, Asset Detail, Reports, dan Asset Transactional Policy | FE+BE | 27 | TC-FA-LBL-419, TC-FA-LBL-496, TC-FA-LBL-497 |
| TC-FA-LBL-E2E-176-label-default-terkunci-bulk-add-form-edit-aset-dan-form-register-asset | Label Default Terkunci: Bulk Add, Form Edit Aset, dan Form Register Asset | FE+BE | 35 | TC-FA-LBL-433, TC-FA-LBL-500, TC-FA-LBL-523 |
| TC-FA-LBL-E2E-177-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role-bagian-2-2 | Role Matrix Positif: Aksi Tulis Berhasil Sampai Tuntas per Role (bagian 2/2) | FE+BE | 28 | TC-FA-LBL-36, TC-FA-LBL-37, TC-FA-LBL-42 |
| TC-FA-LBL-E2E-178-drawer-kolom-custom-field-formula-company-fields | Drawer Kolom Custom Field Formula (Company Fields) | FE+BE | 14 | TC-FA-LBL-581 |
| TC-FA-LBL-E2E-179-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface-bagian-2-2 | Pencatatan Edit Warna dan Edit Nama dengan Warna di Tiga Surface (bagian 2/2) | FE+BE | 34 | TC-FA-LBL-385, TC-FA-LBL-386, TC-FA-LBL-387 |
| TC-FA-LBL-E2E-180-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot-bagian-2-2 | Siklus Slot Master Data Count Limit: Nilai System Limits, Delete, dan Bulk Delete Membebaskan Slot (bagian 2/2) | FE+BE | 24 | TC-FA-LBL-479, TC-FA-LBL-480 |
| TC-FA-LBL-E2E-181-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role-bagian-2-2 | Role Matrix Gate: Ketersediaan Kolom Warranty Expiry dan Custom Field per Role (bagian 2/2) | FE+BE | 46 | TC-FA-LBL-552 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua TC masuk tepat satu spec E2E.

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-LBL-1 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-2 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-3 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-4 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-5 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-6 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-7 | E2E | TC-FA-LBL-E2E-001-screening-tab-labels-layout-breadcrumb-navigasi-tab-dan-format-sel-baris | FE+BE |
| TC-FA-LBL-8 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-9 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-10 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-11 | E2E | TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong | FE+BE |
| TC-FA-LBL-12 | E2E | TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | FE+BE |
| TC-FA-LBL-13 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-14 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-15 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-16 | E2E | TC-FA-LBL-E2E-002-screening-tab-labels-kontras-chip-urutan-default-tooltip-menu-row-action-dan-shimmer | FE+BE |
| TC-FA-LBL-17 | E2E | TC-FA-LBL-E2E-004-pagination-labels-list-company-volume | FE+BE |
| TC-FA-LBL-18 | E2E | TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume | FE+BE |
| TC-FA-LBL-19 | E2E | TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume | FE+BE |
| TC-FA-LBL-20 | E2E | TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume | FE+BE |
| TC-FA-LBL-21 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-22 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-23 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-24 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-25 | E2E | TC-FA-LBL-E2E-008-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-1-dari-3 | FE+BE |
| TC-FA-LBL-26 | E2E | TC-FA-LBL-E2E-008-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-1-dari-3 | FE+BE |
| TC-FA-LBL-27 | E2E | TC-FA-LBL-E2E-008-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-1-dari-3 | FE+BE |
| TC-FA-LBL-28 | E2E | TC-FA-LBL-E2E-009-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-2-dari-3 | FE+BE |
| TC-FA-LBL-29 | E2E | TC-FA-LBL-E2E-009-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-2-dari-3 | FE+BE |
| TC-FA-LBL-30 | E2E | TC-FA-LBL-E2E-009-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-2-dari-3 | FE+BE |
| TC-FA-LBL-31 | E2E | TC-FA-LBL-E2E-010-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-3-dari-3 | FE+BE |
| TC-FA-LBL-32 | E2E | TC-FA-LBL-E2E-011-role-matrix-negatif-tab-labels-hidden-dan-akses-url-langsung-tanpa-capability | FE+BE |
| TC-FA-LBL-33 | E2E | TC-FA-LBL-E2E-011-role-matrix-negatif-tab-labels-hidden-dan-akses-url-langsung-tanpa-capability | FE+BE |
| TC-FA-LBL-34 | E2E | TC-FA-LBL-E2E-012-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role | FE+BE |
| TC-FA-LBL-35 | E2E | TC-FA-LBL-E2E-012-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role | FE+BE |
| TC-FA-LBL-36 | E2E | TC-FA-LBL-E2E-177-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role-bagian-2-2 | FE+BE |
| TC-FA-LBL-37 | E2E | TC-FA-LBL-E2E-177-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role-bagian-2-2 | FE+BE |
| TC-FA-LBL-38 | E2E | TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | FE+BE |
| TC-FA-LBL-39 | E2E | TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | FE+BE |
| TC-FA-LBL-40 | E2E | TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | FE+BE |
| TC-FA-LBL-41 | E2E | TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | FE+BE |
| TC-FA-LBL-42 | E2E | TC-FA-LBL-E2E-177-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role-bagian-2-2 | FE+BE |
| TC-FA-LBL-43 | E2E | TC-FA-LBL-E2E-012-role-matrix-positif-aksi-tulis-berhasil-sampai-tuntas-per-role | FE+BE |
| TC-FA-LBL-44 | E2E | TC-FA-LBL-E2E-013-role-matrix-positif-aksi-baca-download-changelog-drawer-per-role | FE+BE |
| TC-FA-LBL-45 | E2E | TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | FE+BE |
| TC-FA-LBL-46 | E2E | TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | FE+BE |
| TC-FA-LBL-47 | E2E | TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | FE+BE |
| TC-FA-LBL-48 | E2E | TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | FE+BE |
| TC-FA-LBL-49 | E2E | TC-FA-LBL-E2E-159-color-picker-create-klik-tiap-swatch-preset | FE+BE |
| TC-FA-LBL-50 | E2E | TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste | FE+BE |
| TC-FA-LBL-51 | E2E | TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste | FE+BE |
| TC-FA-LBL-52 | E2E | TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste | FE+BE |
| TC-FA-LBL-53 | E2E | TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste | FE+BE |
| TC-FA-LBL-54 | E2E | TC-FA-LBL-E2E-021-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-1 | FE+BE |
| TC-FA-LBL-55 | E2E | TC-FA-LBL-E2E-021-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-1 | FE+BE |
| TC-FA-LBL-56 | E2E | TC-FA-LBL-E2E-021-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-1 | FE+BE |
| TC-FA-LBL-57 | E2E | TC-FA-LBL-E2E-022-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-2 | FE+BE |
| TC-FA-LBL-58 | E2E | TC-FA-LBL-E2E-022-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-2 | FE+BE |
| TC-FA-LBL-59 | E2E | TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1 | FE+BE |
| TC-FA-LBL-60 | E2E | TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1 | FE+BE |
| TC-FA-LBL-61 | E2E | TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1 | FE+BE |
| TC-FA-LBL-62 | E2E | TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1 | FE+BE |
| TC-FA-LBL-63 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-64 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-65 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-66 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-67 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-68 | E2E | TC-FA-LBL-E2E-025-live-preview-label-nama-warna-dan-warna-teks-kontras | FE+BE |
| TC-FA-LBL-69 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-70 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-71 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-72 | E2E | TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2 | FE+BE |
| TC-FA-LBL-73 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-74 | E2E | TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2 | FE+BE |
| TC-FA-LBL-75 | E2E | TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2 | FE+BE |
| TC-FA-LBL-76 | E2E | TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal | FE+BE |
| TC-FA-LBL-77 | E2E | TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal | FE+BE |
| TC-FA-LBL-78 | E2E | TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal | FE+BE |
| TC-FA-LBL-79 | E2E | TC-FA-LBL-E2E-028-duplikat-nama-label-create-debounce-case-insensitive-dan-cek-keunikan-gagal | FE+BE |
| TC-FA-LBL-80 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-81 | E2E | TC-FA-LBL-E2E-026-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-1 | FE+BE |
| TC-FA-LBL-82 | E2E | TC-FA-LBL-E2E-027-validasi-label-name-create-kosong-spasi-panjang-emoji-dan-trim-bagian-2 | FE+BE |
| TC-FA-LBL-83 | E2E | TC-FA-LBL-E2E-029-submit-create-clear-field-saving-state-dan-klik-ganda | FE+BE |
| TC-FA-LBL-84 | E2E | TC-FA-LBL-E2E-030-submit-create-duplikat-ditolak-server-simpan-stay-tidak-dicentang-dan-warna-huruf-kapital | FE+BE |
| TC-FA-LBL-85 | E2E | TC-FA-LBL-E2E-030-submit-create-duplikat-ditolak-server-simpan-stay-tidak-dicentang-dan-warna-huruf-kapital | FE+BE |
| TC-FA-LBL-86 | E2E | TC-FA-LBL-E2E-160-submit-create-stay-dicentang-form-direset-dan-modal-tetap-terbuka | FE+BE |
| TC-FA-LBL-87 | E2E | TC-FA-LBL-E2E-030-submit-create-duplikat-ditolak-server-simpan-stay-tidak-dicentang-dan-warna-huruf-kapital | FE+BE |
| TC-FA-LBL-88 | E2E | TC-FA-LBL-E2E-136-resilience-create-5xx-dan-timeout | FE+BE |
| TC-FA-LBL-89 | E2E | TC-FA-LBL-E2E-136-resilience-create-5xx-dan-timeout | FE+BE |
| TC-FA-LBL-90 | E2E | TC-FA-LBL-E2E-029-submit-create-clear-field-saving-state-dan-klik-ganda | FE+BE |
| TC-FA-LBL-91 | E2E | TC-FA-LBL-E2E-029-submit-create-clear-field-saving-state-dan-klik-ganda | FE+BE |
| TC-FA-LBL-92 | E2E | TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default | FE+BE |
| TC-FA-LBL-93 | E2E | TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default | FE+BE |
| TC-FA-LBL-94 | E2E | TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default | FE+BE |
| TC-FA-LBL-95 | E2E | TC-FA-LBL-E2E-032-menutup-form-create-form-bersih-unsaved-changes-esc-dan-warna-default | FE+BE |
| TC-FA-LBL-96 | E2E | TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route | FE+BE |
| TC-FA-LBL-97 | E2E | TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route | FE+BE |
| TC-FA-LBL-98 | E2E | TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route | FE+BE |
| TC-FA-LBL-99 | E2E | TC-FA-LBL-E2E-033-menutup-form-create-form-dikembalikan-backdrop-reload-dan-pindah-route | FE+BE |
| TC-FA-LBL-100 | E2E | TC-FA-LBL-E2E-031-create-dari-tombol-plus-pada-tab-asset-name | FE+BE |
| TC-FA-LBL-101 | E2E | TC-FA-LBL-E2E-035-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-2 | FE+BE |
| TC-FA-LBL-102 | E2E | TC-FA-LBL-E2E-034-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-1 | FE+BE |
| TC-FA-LBL-103 | E2E | TC-FA-LBL-E2E-034-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-1 | FE+BE |
| TC-FA-LBL-104 | E2E | TC-FA-LBL-E2E-034-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-1 | FE+BE |
| TC-FA-LBL-105 | E2E | TC-FA-LBL-E2E-035-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-2 | FE+BE |
| TC-FA-LBL-106 | E2E | TC-FA-LBL-E2E-017-state-tenant-perilaku-create-edit-delete-di-plan-terendah-dan-enterprise | FE+BE |
| TC-FA-LBL-107 | E2E | TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | FE+BE |
| TC-FA-LBL-108 | E2E | TC-FA-LBL-E2E-157-state-tenant-write-lockdown-client-expired-create-dan-seluruh-aksi-tulis-dengan-baca-tetap-diizinkan | FE+BE |
| TC-FA-LBL-109 | E2E | TC-FA-LBL-E2E-015-hak-akses-dicabut-saat-modal-atau-dialog-terbuka | FE+BE |
| TC-FA-LBL-110 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-111 | E2E | TC-FA-LBL-E2E-036-screening-dan-accessibility-popup-edit-label | FE+BE |
| TC-FA-LBL-112 | E2E | TC-FA-LBL-E2E-036-screening-dan-accessibility-popup-edit-label | FE+BE |
| TC-FA-LBL-113 | E2E | TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | FE+BE |
| TC-FA-LBL-114 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-115 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-116 | E2E | TC-FA-LBL-E2E-038-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-2 | FE+BE |
| TC-FA-LBL-117 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-118 | E2E | TC-FA-LBL-E2E-038-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-2 | FE+BE |
| TC-FA-LBL-119 | E2E | TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri | FE+BE |
| TC-FA-LBL-120 | E2E | TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri | FE+BE |
| TC-FA-LBL-121 | E2E | TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri | FE+BE |
| TC-FA-LBL-122 | E2E | TC-FA-LBL-E2E-039-duplikat-nama-label-edit-deteksi-setelah-debounce-dan-kapitalisasi-sendiri | FE+BE |
| TC-FA-LBL-123 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-124 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-125 | E2E | TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay | FE+BE |
| TC-FA-LBL-126 | E2E | TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay | FE+BE |
| TC-FA-LBL-127 | E2E | TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay | FE+BE |
| TC-FA-LBL-128 | E2E | TC-FA-LBL-E2E-041-edit-validasi-kode-hex-tidak-valid-pada-color-picker-overlay | FE+BE |
| TC-FA-LBL-129 | E2E | TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-130 | E2E | TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-131 | E2E | TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-132 | E2E | TC-FA-LBL-E2E-162-edit-live-preview-dan-clear-field | FE+BE |
| TC-FA-LBL-133 | E2E | TC-FA-LBL-E2E-162-edit-live-preview-dan-clear-field | FE+BE |
| TC-FA-LBL-134 | E2E | TC-FA-LBL-E2E-044-edit-save-zero-delta-tanpa-perubahan-spasi-tepi-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-135 | E2E | TC-FA-LBL-E2E-044-edit-save-zero-delta-tanpa-perubahan-spasi-tepi-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-136 | E2E | TC-FA-LBL-E2E-044-edit-save-zero-delta-tanpa-perubahan-spasi-tepi-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-137 | E2E | TC-FA-LBL-E2E-045-edit-simpan-perubahan-nama-warna-dan-keduanya | FE+BE |
| TC-FA-LBL-138 | E2E | TC-FA-LBL-E2E-045-edit-simpan-perubahan-nama-warna-dan-keduanya | FE+BE |
| TC-FA-LBL-139 | E2E | TC-FA-LBL-E2E-045-edit-simpan-perubahan-nama-warna-dan-keduanya | FE+BE |
| TC-FA-LBL-140 | E2E | TC-FA-LBL-E2E-040-duplikat-nama-label-edit-debounce-500-ms-cek-gagal-dan-save-ditolak-server | FE+BE |
| TC-FA-LBL-141 | E2E | TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal | FE+BE |
| TC-FA-LBL-142 | E2E | TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal | FE+BE |
| TC-FA-LBL-143 | E2E | TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal | FE+BE |
| TC-FA-LBL-144 | E2E | TC-FA-LBL-E2E-174-resilience-edit-5xx-timeout-save-dan-fetch-pembuka-modal | FE+BE |
| TC-FA-LBL-145 | E2E | TC-FA-LBL-E2E-046-edit-klik-ganda-save-dan-saving-state | FE+BE |
| TC-FA-LBL-146 | E2E | TC-FA-LBL-E2E-046-edit-klik-ganda-save-dan-saving-state | FE+BE |
| TC-FA-LBL-147 | E2E | TC-FA-LBL-E2E-047-menutup-form-edit-penutupan-bersih-dan-dialog-unsaved-changes-lewat-tombol-tutup | FE+BE |
| TC-FA-LBL-148 | E2E | TC-FA-LBL-E2E-047-menutup-form-edit-penutupan-bersih-dan-dialog-unsaved-changes-lewat-tombol-tutup | FE+BE |
| TC-FA-LBL-149 | E2E | TC-FA-LBL-E2E-161-menutup-form-edit-klik-backdrop-dan-esc-saat-form-berubah | FE+BE |
| TC-FA-LBL-150 | E2E | TC-FA-LBL-E2E-047-menutup-form-edit-penutupan-bersih-dan-dialog-unsaved-changes-lewat-tombol-tutup | FE+BE |
| TC-FA-LBL-151 | E2E | TC-FA-LBL-E2E-161-menutup-form-edit-klik-backdrop-dan-esc-saat-form-berubah | FE+BE |
| TC-FA-LBL-152 | E2E | TC-FA-LBL-E2E-048-menutup-form-edit-reload-dan-pindah-route-saat-form-berubah | FE+BE |
| TC-FA-LBL-153 | E2E | TC-FA-LBL-E2E-048-menutup-form-edit-reload-dan-pindah-route-saat-form-berubah | FE+BE |
| TC-FA-LBL-154 | E2E | TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | FE+BE |
| TC-FA-LBL-155 | E2E | TC-FA-LBL-E2E-015-hak-akses-dicabut-saat-modal-atau-dialog-terbuka | FE+BE |
| TC-FA-LBL-156 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-157 | E2E | TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda | FE+BE |
| TC-FA-LBL-158 | E2E | TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda | FE+BE |
| TC-FA-LBL-159 | E2E | TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda | FE+BE |
| TC-FA-LBL-160 | E2E | TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir | FE+BE |
| TC-FA-LBL-161 | E2E | TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir | FE+BE |
| TC-FA-LBL-162 | E2E | TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2 | FE+BE |
| TC-FA-LBL-163 | E2E | TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2 | FE+BE |
| TC-FA-LBL-164 | E2E | TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2 | FE+BE |
| TC-FA-LBL-165 | E2E | TC-FA-LBL-E2E-051-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-1-2 | FE+BE |
| TC-FA-LBL-166 | E2E | TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2 | FE+BE |
| TC-FA-LBL-167 | E2E | TC-FA-LBL-E2E-103-volume-drawer-label-500-aset-d-02-500-aset-sort-natural-pagination | FE+BE |
| TC-FA-LBL-168 | E2E | TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard | FE+BE |
| TC-FA-LBL-169 | E2E | TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2 | FE+BE |
| TC-FA-LBL-170 | E2E | TC-FA-LBL-E2E-137-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-1-2 | FE+BE |
| TC-FA-LBL-171 | E2E | TC-FA-LBL-E2E-137-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-1-2 | FE+BE |
| TC-FA-LBL-172 | E2E | TC-FA-LBL-E2E-050-dialog-delete-d-01-screening-cancel-esc-backdrop-dan-klik-ganda | FE+BE |
| TC-FA-LBL-173 | E2E | TC-FA-LBL-E2E-053-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-1-2 | FE+BE |
| TC-FA-LBL-174 | E2E | TC-FA-LBL-E2E-053-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-1-2 | FE+BE |
| TC-FA-LBL-175 | E2E | TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | FE+BE |
| TC-FA-LBL-176 | E2E | TC-FA-LBL-E2E-015-hak-akses-dicabut-saat-modal-atau-dialog-terbuka | FE+BE |
| TC-FA-LBL-177 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-178 | E2E | TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3 | FE+BE |
| TC-FA-LBL-179 | E2E | TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3 | FE+BE |
| TC-FA-LBL-180 | E2E | TC-FA-LBL-E2E-058-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-2-3 | FE+BE |
| TC-FA-LBL-181 | E2E | TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3 | FE+BE |
| TC-FA-LBL-182 | E2E | TC-FA-LBL-E2E-057-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-1-3 | FE+BE |
| TC-FA-LBL-183 | E2E | TC-FA-LBL-E2E-164-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-3-3 | FE+BE |
| TC-FA-LBL-184 | E2E | TC-FA-LBL-E2E-164-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-3-3 | FE+BE |
| TC-FA-LBL-185 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-186 | E2E | TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2 | FE+BE |
| TC-FA-LBL-187 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-188 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-189 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-190 | E2E | TC-FA-LBL-E2E-058-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-2-3 | FE+BE |
| TC-FA-LBL-191 | E2E | TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai | FE+BE |
| TC-FA-LBL-192 | E2E | TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai | FE+BE |
| TC-FA-LBL-193 | E2E | TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai | FE+BE |
| TC-FA-LBL-194 | E2E | TC-FA-LBL-E2E-056-bulk-delete-dialog-d-04-campuran-label-bersih-dan-label-dipakai | FE+BE |
| TC-FA-LBL-195 | E2E | TC-FA-LBL-E2E-052-dialog-d-02-label-dipakai-atau-default-label-hitungan-jamak-tunggal-status-aset-bagian-2-2 | FE+BE |
| TC-FA-LBL-196 | E2E | TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2 | FE+BE |
| TC-FA-LBL-197 | E2E | TC-FA-LBL-E2E-053-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-1-2 | FE+BE |
| TC-FA-LBL-198 | E2E | TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2 | FE+BE |
| TC-FA-LBL-199 | E2E | TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2 | FE+BE |
| TC-FA-LBL-200 | E2E | TC-FA-LBL-E2E-137-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-1-2 | FE+BE |
| TC-FA-LBL-201 | E2E | TC-FA-LBL-E2E-138-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-2-2 | FE+BE |
| TC-FA-LBL-202 | E2E | TC-FA-LBL-E2E-138-resilience-delete-dan-bulk-delete-5xx-dan-timeout-di-tengah-proses-bagian-2-2 | FE+BE |
| TC-FA-LBL-203 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-204 | E2E | TC-FA-LBL-E2E-058-volume-bulk-action-bar-select-all-selection-limit-dan-seleksi-lintas-halaman-bagian-2-3 | FE+BE |
| TC-FA-LBL-205 | E2E | TC-FA-LBL-E2E-014-role-matrix-negatif-kolom-checkbox-bulk-action-bar-dan-tombol-plus-asset-name-per-role | FE+BE |
| TC-FA-LBL-206 | E2E | TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | FE+BE |
| TC-FA-LBL-207 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-208 | E2E | TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | FE+BE |
| TC-FA-LBL-209 | E2E | TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | FE+BE |
| TC-FA-LBL-210 | E2E | TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | FE+BE |
| TC-FA-LBL-211 | E2E | TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | FE+BE |
| TC-FA-LBL-212 | E2E | TC-FA-LBL-E2E-060-search-labels-list-toolbar-kelas-label-color-hex-dan-empty-state | FE+BE |
| TC-FA-LBL-213 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-214 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-215 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-216 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-217 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-218 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-219 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-220 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-221 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-222 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-223 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-224 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-225 | E2E | TC-FA-LBL-E2E-062-filter-labels-list-panel-total-asset-dan-dropdown-modified-by | FE+BE |
| TC-FA-LBL-226 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-227 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-228 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-229 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-230 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-231 | E2E | TC-FA-LBL-E2E-063-filter-labels-list-modified-by-multi-pilih-chip-dan-last-updated | FE+BE |
| TC-FA-LBL-232 | E2E | TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel | FE+BE |
| TC-FA-LBL-233 | E2E | TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel | FE+BE |
| TC-FA-LBL-234 | E2E | TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel | FE+BE |
| TC-FA-LBL-235 | E2E | TC-FA-LBL-E2E-064-filter-labels-list-kombinasi-search-filter-dan-draft-panel | FE+BE |
| TC-FA-LBL-236 | E2E | TC-FA-LBL-E2E-165-filter-labels-list-opsi-tanpa-nilai-kosong-dan-indikator-titik | FE+BE |
| TC-FA-LBL-237 | E2E | TC-FA-LBL-E2E-065-filter-labels-list-independen-kolom-clear-field-dan-opsi-baru | FE+BE |
| TC-FA-LBL-238 | E2E | TC-FA-LBL-E2E-065-filter-labels-list-independen-kolom-clear-field-dan-opsi-baru | FE+BE |
| TC-FA-LBL-239 | E2E | TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume | FE+BE |
| TC-FA-LBL-240 | E2E | TC-FA-LBL-E2E-065-filter-labels-list-independen-kolom-clear-field-dan-opsi-baru | FE+BE |
| TC-FA-LBL-241 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-242 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-243 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-244 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-245 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-246 | E2E | TC-FA-LBL-E2E-066-sort-labels-list-tiga-tahap-per-kolom | FE+BE |
| TC-FA-LBL-247 | E2E | TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan | FE+BE |
| TC-FA-LBL-248 | E2E | TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume | FE+BE |
| TC-FA-LBL-249 | E2E | TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan | FE+BE |
| TC-FA-LBL-250 | E2E | TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan | FE+BE |
| TC-FA-LBL-251 | E2E | TC-FA-LBL-E2E-067-kombinasi-search-filter-sort-pagination-dan-pemulihan-saringan | FE+BE |
| TC-FA-LBL-252 | E2E | TC-FA-LBL-E2E-068-kombinasi-search-filter-sort-empty-state-create-dan-edit | FE+BE |
| TC-FA-LBL-253 | E2E | TC-FA-LBL-E2E-068-kombinasi-search-filter-sort-empty-state-create-dan-edit | FE+BE |
| TC-FA-LBL-254 | E2E | TC-FA-LBL-E2E-068-kombinasi-search-filter-sort-empty-state-create-dan-edit | FE+BE |
| TC-FA-LBL-255 | E2E | TC-FA-LBL-E2E-069-setup-column-labels-list-overlay-popup-dan-ceklis | FE+BE |
| TC-FA-LBL-256 | E2E | TC-FA-LBL-E2E-069-setup-column-labels-list-overlay-popup-dan-ceklis | FE+BE |
| TC-FA-LBL-257 | E2E | TC-FA-LBL-E2E-069-setup-column-labels-list-overlay-popup-dan-ceklis | FE+BE |
| TC-FA-LBL-258 | E2E | TC-FA-LBL-E2E-071-setup-column-labels-list-drag-reorder-dan-pin | FE+BE |
| TC-FA-LBL-259 | E2E | TC-FA-LBL-E2E-071-setup-column-labels-list-drag-reorder-dan-pin | FE+BE |
| TC-FA-LBL-260 | E2E | TC-FA-LBL-E2E-071-setup-column-labels-list-drag-reorder-dan-pin | FE+BE |
| TC-FA-LBL-261 | E2E | TC-FA-LBL-E2E-166-setup-column-labels-list-reset-to-default-dan-tutup-tanpa-simpan | FE+BE |
| TC-FA-LBL-262 | E2E | TC-FA-LBL-E2E-166-setup-column-labels-list-reset-to-default-dan-tutup-tanpa-simpan | FE+BE |
| TC-FA-LBL-263 | E2E | TC-FA-LBL-E2E-070-setup-column-labels-list-guard-satu-kolom-dan-konfigurasi-per-tabel | FE+BE |
| TC-FA-LBL-264 | E2E | TC-FA-LBL-E2E-070-setup-column-labels-list-guard-satu-kolom-dan-konfigurasi-per-tabel | FE+BE |
| TC-FA-LBL-265 | E2E | TC-FA-LBL-E2E-074-volume-download-seluruh-baris-dan-di-atas-5000-baris | FE+BE |
| TC-FA-LBL-266 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-267 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-268 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-269 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-270 | E2E | TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | FE+BE |
| TC-FA-LBL-271 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-272 | E2E | TC-FA-LBL-E2E-072-download-labels-list-csv-xlsx-nama-berkas-kolom-dan-filter-aktif | FE+BE |
| TC-FA-LBL-273 | E2E | TC-FA-LBL-E2E-075-isi-berkas-ekspor-labels-list-dan-changelog | FE+BE |
| TC-FA-LBL-274 | E2E | TC-FA-LBL-E2E-073-download-labels-list-nol-baris-dan-urutan-sort | FE+BE |
| TC-FA-LBL-275 | E2E | TC-FA-LBL-E2E-075-isi-berkas-ekspor-labels-list-dan-changelog | FE+BE |
| TC-FA-LBL-276 | E2E | TC-FA-LBL-E2E-073-download-labels-list-nol-baris-dan-urutan-sort | FE+BE |
| TC-FA-LBL-277 | E2E | TC-FA-LBL-E2E-074-volume-download-seluruh-baris-dan-di-atas-5000-baris | FE+BE |
| TC-FA-LBL-278 | E2E | TC-FA-LBL-E2E-004-pagination-labels-list-company-volume | FE+BE |
| TC-FA-LBL-279 | E2E | TC-FA-LBL-E2E-004-pagination-labels-list-company-volume | FE+BE |
| TC-FA-LBL-280 | E2E | TC-FA-LBL-E2E-004-pagination-labels-list-company-volume | FE+BE |
| TC-FA-LBL-281 | E2E | TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir | FE+BE |
| TC-FA-LBL-282 | E2E | TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume | FE+BE |
| TC-FA-LBL-283 | E2E | TC-FA-LBL-E2E-158-pagination-bersama-filter-search-sort-dan-urutan-tie-break-company-volume | FE+BE |
| TC-FA-LBL-284 | E2E | TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup | FE+BE |
| TC-FA-LBL-285 | E2E | TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup | FE+BE |
| TC-FA-LBL-286 | E2E | TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup | FE+BE |
| TC-FA-LBL-287 | E2E | TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong | FE+BE |
| TC-FA-LBL-288 | E2E | TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | FE+BE |
| TC-FA-LBL-289 | E2E | TC-FA-LBL-E2E-076-screening-modal-changelog-labels-format-sel-shimmer-dan-menutup | FE+BE |
| TC-FA-LBL-290 | E2E | TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-291 | E2E | TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-292 | E2E | TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-293 | E2E | TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-294 | E2E | TC-FA-LBL-E2E-077-search-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-295 | E2E | TC-FA-LBL-E2E-078-search-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-296 | E2E | TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-297 | E2E | TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-298 | E2E | TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-299 | E2E | TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-300 | E2E | TC-FA-LBL-E2E-079-filter-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-301 | E2E | TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-302 | E2E | TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-303 | E2E | TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-304 | E2E | TC-FA-LBL-E2E-080-filter-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-305 | E2E | TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-306 | E2E | TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-307 | E2E | TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-308 | E2E | TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-309 | E2E | TC-FA-LBL-E2E-081-sort-modal-changelog-bagian-1-2 | FE+BE |
| TC-FA-LBL-310 | E2E | TC-FA-LBL-E2E-082-sort-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-311 | E2E | TC-FA-LBL-E2E-082-sort-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-312 | E2E | TC-FA-LBL-E2E-083-setup-column-modal-changelog-bagian-1-3 | FE+BE |
| TC-FA-LBL-313 | E2E | TC-FA-LBL-E2E-083-setup-column-modal-changelog-bagian-1-3 | FE+BE |
| TC-FA-LBL-314 | E2E | TC-FA-LBL-E2E-167-setup-column-modal-changelog-ceklis-dan-unceklis-kolom | FE+BE |
| TC-FA-LBL-315 | E2E | TC-FA-LBL-E2E-084-setup-column-modal-changelog-bagian-2-3 | FE+BE |
| TC-FA-LBL-316 | E2E | TC-FA-LBL-E2E-084-setup-column-modal-changelog-bagian-2-3 | FE+BE |
| TC-FA-LBL-317 | E2E | TC-FA-LBL-E2E-085-setup-column-modal-changelog-bagian-3-3 | FE+BE |
| TC-FA-LBL-318 | E2E | TC-FA-LBL-E2E-085-setup-column-modal-changelog-bagian-3-3 | FE+BE |
| TC-FA-LBL-319 | E2E | TC-FA-LBL-E2E-086-download-modal-changelog-csv-xlsx-dan-filter-aktif | FE+BE |
| TC-FA-LBL-320 | E2E | TC-FA-LBL-E2E-086-download-modal-changelog-csv-xlsx-dan-filter-aktif | FE+BE |
| TC-FA-LBL-321 | E2E | TC-FA-LBL-E2E-086-download-modal-changelog-csv-xlsx-dan-filter-aktif | FE+BE |
| TC-FA-LBL-322 | E2E | TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | FE+BE |
| TC-FA-LBL-323 | E2E | TC-FA-LBL-E2E-075-isi-berkas-ekspor-labels-list-dan-changelog | FE+BE |
| TC-FA-LBL-324 | E2E | TC-FA-LBL-E2E-005-retensi-state-labels-list-dan-pagination-changelog-company-volume | FE+BE |
| TC-FA-LBL-325 | E2E | TC-FA-LBL-E2E-082-sort-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-326 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-327 | E2E | TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-328 | E2E | TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-329 | E2E | TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-330 | E2E | TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-331 | E2E | TC-FA-LBL-E2E-087-membuka-dan-screening-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-332 | E2E | TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset | FE+BE |
| TC-FA-LBL-333 | E2E | TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset | FE+BE |
| TC-FA-LBL-334 | E2E | TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-335 | E2E | TC-FA-LBL-E2E-102-empty-state-drawer-dan-filter-panel-drawer-pada-sumber-0-baris | FE+BE |
| TC-FA-LBL-336 | E2E | TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-337 | E2E | TC-FA-LBL-E2E-135-resilience-baca-dan-ekspor-error-load-tabel-changelog-drawer-dan-download-gagal | FE+BE |
| TC-FA-LBL-338 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-339 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-340 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-341 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-342 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-343 | E2E | TC-FA-LBL-E2E-092-search-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-344 | E2E | TC-FA-LBL-E2E-093-search-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-345 | E2E | TC-FA-LBL-E2E-093-search-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-346 | E2E | TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-347 | E2E | TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-348 | E2E | TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-349 | E2E | TC-FA-LBL-E2E-094-filter-drawer-tagged-asset-bagian-1-2 | FE+BE |
| TC-FA-LBL-350 | E2E | TC-FA-LBL-E2E-096-filter-category-modal-tree-picker | FE+BE |
| TC-FA-LBL-351 | E2E | TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-352 | E2E | TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-353 | E2E | TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-354 | E2E | TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-355 | E2E | TC-FA-LBL-E2E-103-volume-drawer-label-500-aset-d-02-500-aset-sort-natural-pagination | FE+BE |
| TC-FA-LBL-356 | E2E | TC-FA-LBL-E2E-097-sort-drawer-tagged-asset-asset-id-dan-kolom-badge | FE+BE |
| TC-FA-LBL-357 | E2E | TC-FA-LBL-E2E-097-sort-drawer-tagged-asset-asset-id-dan-kolom-badge | FE+BE |
| TC-FA-LBL-358 | E2E | TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker | FE+BE |
| TC-FA-LBL-359 | E2E | TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker | FE+BE |
| TC-FA-LBL-360 | E2E | TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker | FE+BE |
| TC-FA-LBL-361 | E2E | TC-FA-LBL-E2E-098-sort-drawer-tagged-asset-status-last-updated-label-dan-tie-breaker | FE+BE |
| TC-FA-LBL-362 | E2E | TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated | FE+BE |
| TC-FA-LBL-363 | E2E | TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated | FE+BE |
| TC-FA-LBL-364 | E2E | TC-FA-LBL-E2E-170-setup-column-drawer-ceklis-dan-unceklis-kolom-hideable | FE+BE |
| TC-FA-LBL-365 | E2E | TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated | FE+BE |
| TC-FA-LBL-366 | E2E | TC-FA-LBL-E2E-101-setup-column-drawer-drag-reorder | FE+BE |
| TC-FA-LBL-367 | E2E | TC-FA-LBL-E2E-100-setup-column-drawer-reset-to-default-discard-dan-pin | FE+BE |
| TC-FA-LBL-368 | E2E | TC-FA-LBL-E2E-100-setup-column-drawer-reset-to-default-discard-dan-pin | FE+BE |
| TC-FA-LBL-369 | E2E | TC-FA-LBL-E2E-099-setup-column-drawer-overlay-popup-guard-dan-kolom-curated | FE+BE |
| TC-FA-LBL-370 | E2E | TC-FA-LBL-E2E-089-kolom-label-dan-badge-label-panjang-di-drawer | FE+BE |
| TC-FA-LBL-371 | E2E | TC-FA-LBL-E2E-089-kolom-label-dan-badge-label-panjang-di-drawer | FE+BE |
| TC-FA-LBL-372 | E2E | TC-FA-LBL-E2E-103-volume-drawer-label-500-aset-d-02-500-aset-sort-natural-pagination | FE+BE |
| TC-FA-LBL-373 | E2E | TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-374 | E2E | TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-375 | E2E | TC-FA-LBL-E2E-007-mobile-modal-create-edit-delete-bulk-delete-modal-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-376 | E2E | TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-FA-LBL-377 | E2E | TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-FA-LBL-378 | E2E | TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-FA-LBL-379 | E2E | TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | FE+BE |
| TC-FA-LBL-380 | E2E | TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | FE+BE |
| TC-FA-LBL-381 | E2E | TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | FE+BE |
| TC-FA-LBL-382 | E2E | TC-FA-LBL-E2E-128-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface | FE+BE |
| TC-FA-LBL-383 | E2E | TC-FA-LBL-E2E-128-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface | FE+BE |
| TC-FA-LBL-384 | E2E | TC-FA-LBL-E2E-128-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface | FE+BE |
| TC-FA-LBL-385 | E2E | TC-FA-LBL-E2E-179-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface-bagian-2-2 | FE+BE |
| TC-FA-LBL-386 | E2E | TC-FA-LBL-E2E-179-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface-bagian-2-2 | FE+BE |
| TC-FA-LBL-387 | E2E | TC-FA-LBL-E2E-179-pencatatan-edit-warna-dan-edit-nama-dengan-warna-di-tiga-surface-bagian-2-2 | FE+BE |
| TC-FA-LBL-388 | E2E | TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | FE+BE |
| TC-FA-LBL-389 | E2E | TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-FA-LBL-390 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-391 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-392 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-393 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-394 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-395 | E2E | TC-FA-LBL-E2E-129-pencatatan-delete-dan-bulk-delete-di-tiga-surface | FE+BE |
| TC-FA-LBL-396 | E2E | TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard | FE+BE |
| TC-FA-LBL-397 | E2E | TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard | FE+BE |
| TC-FA-LBL-398 | E2E | TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain | FE+BE |
| TC-FA-LBL-399 | E2E | TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain | FE+BE |
| TC-FA-LBL-400 | E2E | TC-FA-LBL-E2E-132-absence-log-delete-bulk-delete-campuran-dialog-ok-dan-penolakan-guard | FE+BE |
| TC-FA-LBL-401 | E2E | TC-FA-LBL-E2E-134-absence-log-batas-katalog-dan-import-di-batas-company-limit | FE+BE |
| TC-FA-LBL-402 | E2E | TC-FA-LBL-E2E-173-absence-log-aksi-gagal-5xx-pada-edit-create-dan-delete | FE+BE |
| TC-FA-LBL-403 | E2E | TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain | FE+BE |
| TC-FA-LBL-404 | E2E | TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface | FE+BE |
| TC-FA-LBL-405 | E2E | TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface | FE+BE |
| TC-FA-LBL-406 | E2E | TC-FA-LBL-E2E-127-pencatatan-edit-nama-di-tiga-surface | FE+BE |
| TC-FA-LBL-407 | E2E | TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface | FE+BE |
| TC-FA-LBL-408 | E2E | TC-FA-LBL-E2E-126-pencatatan-create-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-FA-LBL-409 | E2E | TC-FA-LBL-E2E-131-pencatatan-lewat-request-langsung-create-edit-dan-delete | FE+BE |
| TC-FA-LBL-410 | E2E | TC-FA-LBL-E2E-133-absence-log-edit-zero-delta-spasi-tepi-request-langsung-dan-label-lain | FE+BE |
| TC-FA-LBL-411 | E2E | TC-FA-LBL-E2E-130-snapshot-log-immutable-label-hasil-import-dan-kolom-tiap-surface | FE+BE |
| TC-FA-LBL-412 | E2E | TC-FA-LBL-E2E-139-sinkron-label-baru-ke-asset-detail-reports-dan-default-label-asset-name | FE+BE |
| TC-FA-LBL-413 | E2E | TC-FA-LBL-E2E-139-sinkron-label-baru-ke-asset-detail-reports-dan-default-label-asset-name | FE+BE |
| TC-FA-LBL-414 | E2E | TC-FA-LBL-E2E-139-sinkron-label-baru-ke-asset-detail-reports-dan-default-label-asset-name | FE+BE |
| TC-FA-LBL-415 | E2E | TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-416 | E2E | TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-417 | E2E | TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-418 | E2E | TC-FA-LBL-E2E-140-sinkron-rename-label-ke-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-419 | E2E | TC-FA-LBL-E2E-175-perubahan-warna-label-tercermin-di-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-420 | E2E | TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen | FE+BE |
| TC-FA-LBL-421 | E2E | TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen | FE+BE |
| TC-FA-LBL-422 | E2E | TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen | FE+BE |
| TC-FA-LBL-423 | E2E | TC-FA-LBL-E2E-142-total-asset-realtime-dan-aset-deleted | FE+BE |
| TC-FA-LBL-424 | E2E | TC-FA-LBL-E2E-142-total-asset-realtime-dan-aset-deleted | FE+BE |
| TC-FA-LBL-425 | E2E | TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label | FE+BE |
| TC-FA-LBL-426 | E2E | TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label | FE+BE |
| TC-FA-LBL-427 | E2E | TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label | FE+BE |
| TC-FA-LBL-428 | E2E | TC-FA-LBL-E2E-143-provenance-label-default-dan-manual-di-asset-detail-serta-bulk-add-dan-bulk-remove-label | FE+BE |
| TC-FA-LBL-429 | E2E | TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed | FE+BE |
| TC-FA-LBL-430 | E2E | TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed | FE+BE |
| TC-FA-LBL-431 | E2E | TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed | FE+BE |
| TC-FA-LBL-432 | E2E | TC-FA-LBL-E2E-144-cascade-default-label-pada-asset-name-draft-waiting-for-approval-active-disposed | FE+BE |
| TC-FA-LBL-433 | E2E | TC-FA-LBL-E2E-176-label-default-terkunci-bulk-add-form-edit-aset-dan-form-register-asset | FE+BE |
| TC-FA-LBL-434 | E2E | TC-FA-LBL-E2E-142-total-asset-realtime-dan-aset-deleted | FE+BE |
| TC-FA-LBL-435 | E2E | TC-FA-LBL-E2E-145-label-hasil-import-edit-dan-delete-identik-dengan-create-manual | FE+BE |
| TC-FA-LBL-436 | E2E | TC-FA-LBL-E2E-145-label-hasil-import-edit-dan-delete-identik-dengan-create-manual | FE+BE |
| TC-FA-LBL-437 | E2E | TC-FA-LBL-E2E-146-format-tanggal-jam-dan-timezone-general-settings-di-labels-list-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-438 | E2E | TC-FA-LBL-E2E-146-format-tanggal-jam-dan-timezone-general-settings-di-labels-list-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-439 | E2E | TC-FA-LBL-E2E-146-format-tanggal-jam-dan-timezone-general-settings-di-labels-list-changelog-dan-drawer | FE+BE |
| TC-FA-LBL-440 | E2E | TC-FA-LBL-E2E-147-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot | FE+BE |
| TC-FA-LBL-441 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-442 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-443 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-444 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-445 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-446 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-447 | E2E | TC-FA-LBL-E2E-149-request-langsung-ditolak-per-role-aksi-tulis-read-only-create-only-dan-update-only | FE+BE |
| TC-FA-LBL-448 | E2E | TC-FA-LBL-E2E-150-request-langsung-ditolak-per-role-aksi-tulis-delete-only-dan-read-capability | FE+BE |
| TC-FA-LBL-449 | E2E | TC-FA-LBL-E2E-150-request-langsung-ditolak-per-role-aksi-tulis-delete-only-dan-read-capability | FE+BE |
| TC-FA-LBL-450 | E2E | TC-FA-LBL-E2E-150-request-langsung-ditolak-per-role-aksi-tulis-delete-only-dan-read-capability | FE+BE |
| TC-FA-LBL-451 | E2E | TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label | FE+BE |
| TC-FA-LBL-452 | E2E | TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label | FE+BE |
| TC-FA-LBL-453 | E2E | TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | FE+BE |
| TC-FA-LBL-454 | E2E | TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | FE+BE |
| TC-FA-LBL-455 | E2E | TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | FE+BE |
| TC-FA-LBL-456 | E2E | TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | FE+BE |
| TC-FA-LBL-457 | E2E | TC-FA-LBL-E2E-152-request-langsung-total-control-validasi-warna-validasi-nama-dan-delete-label-yang-dipakai | FE+BE |
| TC-FA-LBL-458 | E2E | TC-FA-LBL-E2E-134-absence-log-batas-katalog-dan-import-di-batas-company-limit | FE+BE |
| TC-FA-LBL-459 | E2E | TC-FA-LBL-E2E-016-state-tenant-write-lockdown-client-suspended-create-edit-delete-bulk-delete-dan-permintaan-langsung | FE+BE |
| TC-FA-LBL-460 | E2E | TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label | FE+BE |
| TC-FA-LBL-461 | E2E | TC-FA-LBL-E2E-153-defense-in-depth-ui-payload-script-dan-sql-serta-isolasi-tenant | FE+BE |
| TC-FA-LBL-462 | E2E | TC-FA-LBL-E2E-153-defense-in-depth-ui-payload-script-dan-sql-serta-isolasi-tenant | FE+BE |
| TC-FA-LBL-463 | E2E | TC-FA-LBL-E2E-153-defense-in-depth-ui-payload-script-dan-sql-serta-isolasi-tenant | FE+BE |
| TC-FA-LBL-464 | E2E | TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete | FE+BE |
| TC-FA-LBL-465 | E2E | TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form | FE+BE |
| TC-FA-LBL-466 | E2E | TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form | FE+BE |
| TC-FA-LBL-467 | E2E | TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form | FE+BE |
| TC-FA-LBL-468 | E2E | TC-FA-LBL-E2E-054-delete-saat-label-berubah-antara-dialog-dan-konfirmasi-sesi-api-admin-kedua-bagian-2-2 | FE+BE |
| TC-FA-LBL-469 | E2E | TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | FE+BE |
| TC-FA-LBL-470 | E2E | TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | FE+BE |
| TC-FA-LBL-471 | E2E | TC-FA-LBL-E2E-156-race-dua-sesi-slot-terakhir-master-data-count-limit | FE+BE |
| TC-FA-LBL-472 | E2E | TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete | FE+BE |
| TC-FA-LBL-473 | E2E | TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete | FE+BE |
| TC-FA-LBL-474 | E2E | TC-FA-LBL-E2E-155-race-dua-sesi-penempelan-label-versus-delete-dan-bulk-delete | FE+BE |
| TC-FA-LBL-475 | E2E | TC-FA-LBL-E2E-157-state-tenant-write-lockdown-client-expired-create-dan-seluruh-aksi-tulis-dengan-baca-tetap-diizinkan | FE+BE |
| TC-FA-LBL-476 | E2E | TC-FA-LBL-E2E-017-state-tenant-perilaku-create-edit-delete-di-plan-terendah-dan-enterprise | FE+BE |
| TC-FA-LBL-477 | E2E | TC-FA-LBL-E2E-154-race-dua-sesi-create-dan-edit-nama-sama-serta-import-versus-form | FE+BE |
| TC-FA-LBL-478 | E2E | TC-FA-LBL-E2E-147-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot | FE+BE |
| TC-FA-LBL-479 | E2E | TC-FA-LBL-E2E-180-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot-bagian-2-2 | FE+BE |
| TC-FA-LBL-480 | E2E | TC-FA-LBL-E2E-180-siklus-slot-master-data-count-limit-nilai-system-limits-delete-dan-bulk-delete-membebaskan-slot-bagian-2-2 | FE+BE |
| TC-FA-LBL-481 | E2E | TC-FA-LBL-E2E-151-request-langsung-tanpa-capability-jalur-baca-hanya-baca-dan-pelepasan-relasi-label | FE+BE |
| TC-FA-LBL-482 | E2E | TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | FE+BE |
| TC-FA-LBL-483 | E2E | TC-FA-LBL-E2E-049-edit-dan-buka-edit-saat-label-diubah-atau-dihapus-admin-lain-sesi-api-admin-kedua | FE+BE |
| TC-FA-LBL-484 | E2E | TC-FA-LBL-E2E-134-absence-log-batas-katalog-dan-import-di-batas-company-limit | FE+BE |
| TC-FA-LBL-485 | E2E | TC-FA-LBL-E2E-037-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-1 | FE+BE |
| TC-FA-LBL-486 | E2E | TC-FA-LBL-E2E-038-validasi-label-name-edit-kosong-spasi-panjang-trim-dan-emoji-bagian-2 | FE+BE |
| TC-FA-LBL-487 | E2E | TC-FA-LBL-E2E-040-duplikat-nama-label-edit-debounce-500-ms-cek-gagal-dan-save-ditolak-server | FE+BE |
| TC-FA-LBL-488 | E2E | TC-FA-LBL-E2E-040-duplikat-nama-label-edit-debounce-500-ms-cek-gagal-dan-save-ditolak-server | FE+BE |
| TC-FA-LBL-489 | E2E | TC-FA-LBL-E2E-042-edit-pemilihan-warna-valid-pada-color-picker-dan-simpan-hex-huruf-kecil | FE+BE |
| TC-FA-LBL-490 | E2E | TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset | FE+BE |
| TC-FA-LBL-491 | E2E | TC-FA-LBL-E2E-169-jumlah-baris-format-sel-dan-truncation-badge-di-drawer-tagged-asset | FE+BE |
| TC-FA-LBL-492 | E2E | TC-FA-LBL-E2E-078-search-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-493 | E2E | TC-FA-LBL-E2E-093-search-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-494 | E2E | TC-FA-LBL-E2E-131-pencatatan-lewat-request-langsung-create-edit-dan-delete | FE+BE |
| TC-FA-LBL-495 | E2E | TC-FA-LBL-E2E-131-pencatatan-lewat-request-langsung-create-edit-dan-delete | FE+BE |
| TC-FA-LBL-496 | E2E | TC-FA-LBL-E2E-175-perubahan-warna-label-tercermin-di-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-497 | E2E | TC-FA-LBL-E2E-175-perubahan-warna-label-tercermin-di-asset-list-asset-detail-reports-dan-asset-transactional-policy | FE+BE |
| TC-FA-LBL-498 | E2E | TC-FA-LBL-E2E-055-bulk-delete-dialog-d-03-homogen-bersih-dan-seleksi | FE+BE |
| TC-FA-LBL-499 | E2E | TC-FA-LBL-E2E-059-delete-dan-bulk-delete-berhasil-pembersihan-relasi-aset-deleted-dan-halaman-terakhir | FE+BE |
| TC-FA-LBL-500 | E2E | TC-FA-LBL-E2E-176-label-default-terkunci-bulk-add-form-edit-aset-dan-form-register-asset | FE+BE |
| TC-FA-LBL-501 | E2E | TC-FA-LBL-E2E-089-kolom-label-dan-badge-label-panjang-di-drawer | FE+BE |
| TC-FA-LBL-502 | E2E | TC-FA-LBL-E2E-031-create-dari-tombol-plus-pada-tab-asset-name | FE+BE |
| TC-FA-LBL-503 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-504 | E2E | TC-FA-LBL-E2E-018-screening-popup-create-label-color-picker-overlay-dan-aksesibilitas | FE+BE |
| TC-FA-LBL-505 | E2E | TC-FA-LBL-E2E-035-batas-katalog-master-data-count-limit-d-06-pada-create-bagian-2 | FE+BE |
| TC-FA-LBL-506 | E2E | TC-FA-LBL-E2E-010-role-matrix-visibilitas-kontrol-tab-labels-per-role-bagian-3-dari-3 | FE+BE |
| TC-FA-LBL-507 | E2E | TC-FA-LBL-E2E-061-search-labels-list-modified-by-guard-kolom-trim-dan-visibilitas-kolom | FE+BE |
| TC-FA-LBL-508 | E2E | TC-FA-LBL-E2E-078-search-modal-changelog-bagian-2-2 | FE+BE |
| TC-FA-LBL-509 | E2E | TC-FA-LBL-E2E-088-membuka-dan-screening-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-510 | E2E | TC-FA-LBL-E2E-019-screening-popup-create-label-palet-preset-16-swatch | FE+BE |
| TC-FA-LBL-511 | E2E | TC-FA-LBL-E2E-011-role-matrix-negatif-tab-labels-hidden-dan-akses-url-langsung-tanpa-capability | FE+BE |
| TC-FA-LBL-512 | E2E | TC-FA-LBL-E2E-024-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-2 | FE+BE |
| TC-FA-LBL-513 | E2E | TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2 | FE+BE |
| TC-FA-LBL-514 | E2E | TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2 | FE+BE |
| TC-FA-LBL-515 | E2E | TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2 | FE+BE |
| TC-FA-LBL-516 | E2E | TC-FA-LBL-E2E-090-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-1-2 | FE+BE |
| TC-FA-LBL-517 | E2E | TC-FA-LBL-E2E-091-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-2-2 | FE+BE |
| TC-FA-LBL-518 | E2E | TC-FA-LBL-E2E-091-sel-multi-nilai-status-dan-label-di-drawer-sort-search-filter-bagian-2-2 | FE+BE |
| TC-FA-LBL-519 | E2E | TC-FA-LBL-E2E-168-sort-modal-changelog-old-value-dan-new-value-campuran | FE+BE |
| TC-FA-LBL-520 | E2E | TC-FA-LBL-E2E-173-absence-log-aksi-gagal-5xx-pada-edit-create-dan-delete | FE+BE |
| TC-FA-LBL-521 | E2E | TC-FA-LBL-E2E-173-absence-log-aksi-gagal-5xx-pada-edit-create-dan-delete | FE+BE |
| TC-FA-LBL-522 | E2E | TC-FA-LBL-E2E-141-sinkron-delete-label-single-dan-bulk-ke-konsumen | FE+BE |
| TC-FA-LBL-523 | E2E | TC-FA-LBL-E2E-176-label-default-terkunci-bulk-add-form-edit-aset-dan-form-register-asset | FE+BE |
| TC-FA-LBL-524 | E2E | TC-FA-LBL-E2E-014-role-matrix-negatif-kolom-checkbox-bulk-action-bar-dan-tombol-plus-asset-name-per-role | FE+BE |
| TC-FA-LBL-525 | E2E | TC-FA-LBL-E2E-006-mobile-card-list-labels-list-menu-card-per-role-long-press-dan-tooltip-disabled | FE+BE |
| TC-FA-LBL-526 | E2E | TC-FA-LBL-E2E-043-edit-penutupan-color-picker-overlay-tanpa-menutup-modal-edit | FE+BE |
| TC-FA-LBL-527 | E2E | TC-FA-LBL-E2E-096-filter-category-modal-tree-picker | FE+BE |
| TC-FA-LBL-528 | E2E | TC-FA-LBL-E2E-096-filter-category-modal-tree-picker | FE+BE |
| TC-FA-LBL-529 | E2E | TC-FA-LBL-E2E-096-filter-category-modal-tree-picker | FE+BE |
| TC-FA-LBL-530 | E2E | TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong | FE+BE |
| TC-FA-LBL-531 | E2E | TC-FA-LBL-E2E-003-empty-state-tabel-dan-changelog-company-kosong | FE+BE |
| TC-FA-LBL-532 | E2E | TC-FA-LBL-E2E-102-empty-state-drawer-dan-filter-panel-drawer-pada-sumber-0-baris | FE+BE |
| TC-FA-LBL-533 | E2E | TC-FA-LBL-E2E-106-drawer-kolom-baru-setup-column-guard-dan-search-bagian-1-2 | FE+BE |
| TC-FA-LBL-534 | E2E | TC-FA-LBL-E2E-116-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-1-2 | FE+BE |
| TC-FA-LBL-535 | E2E | TC-FA-LBL-E2E-116-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-1-2 | FE+BE |
| TC-FA-LBL-536 | E2E | TC-FA-LBL-E2E-104-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-1-2 | FE+BE |
| TC-FA-LBL-537 | E2E | TC-FA-LBL-E2E-106-drawer-kolom-baru-setup-column-guard-dan-search-bagian-1-2 | FE+BE |
| TC-FA-LBL-538 | E2E | TC-FA-LBL-E2E-104-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-1-2 | FE+BE |
| TC-FA-LBL-539 | E2E | TC-FA-LBL-E2E-106-drawer-kolom-baru-setup-column-guard-dan-search-bagian-1-2 | FE+BE |
| TC-FA-LBL-540 | E2E | TC-FA-LBL-E2E-108-drawer-kolom-baru-sort-measurement-transactional-policy-last-scanned-dan-tag | FE+BE |
| TC-FA-LBL-541 | E2E | TC-FA-LBL-E2E-171-drawer-kolom-baru-filter-tag-measurement-transactional-policy-dan-last-scanned | FE+BE |
| TC-FA-LBL-542 | E2E | TC-FA-LBL-E2E-109-drawer-kolom-baru-filter-sumber-0-baris-dan-sort-tag-awalan-pendek | FE+BE |
| TC-FA-LBL-543 | E2E | TC-FA-LBL-E2E-104-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-1-2 | FE+BE |
| TC-FA-LBL-544 | E2E | TC-FA-LBL-E2E-105-drawer-kolom-baru-tag-measurement-last-scanned-dan-transactional-policy-bagian-2-2 | FE+BE |
| TC-FA-LBL-545 | E2E | TC-FA-LBL-E2E-121-gate-accounting-asset-value-dan-custom-field-accounting | FE+BE |
| TC-FA-LBL-546 | E2E | TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2 | FE+BE |
| TC-FA-LBL-547 | E2E | TC-FA-LBL-E2E-122-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-1-2 | FE+BE |
| TC-FA-LBL-548 | E2E | TC-FA-LBL-E2E-124-gate-tier-group-branch-total-control-default-user-read-only-dan-group-manager | FE+BE |
| TC-FA-LBL-549 | E2E | TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | FE+BE |
| TC-FA-LBL-550 | E2E | TC-FA-LBL-E2E-172-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role | FE+BE |
| TC-FA-LBL-551 | E2E | TC-FA-LBL-E2E-119-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-2-2 | FE+BE |
| TC-FA-LBL-552 | E2E | TC-FA-LBL-E2E-181-role-matrix-gate-ketersediaan-kolom-warranty-expiry-dan-custom-field-per-role-bagian-2-2 | FE+BE |
| TC-FA-LBL-553 | E2E | TC-FA-LBL-E2E-116-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-1-2 | FE+BE |
| TC-FA-LBL-554 | E2E | TC-FA-LBL-E2E-122-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-1-2 | FE+BE |
| TC-FA-LBL-555 | E2E | TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | FE+BE |
| TC-FA-LBL-556 | E2E | TC-FA-LBL-E2E-121-gate-accounting-asset-value-dan-custom-field-accounting | FE+BE |
| TC-FA-LBL-557 | E2E | TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2 | FE+BE |
| TC-FA-LBL-558 | E2E | TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | FE+BE |
| TC-FA-LBL-559 | E2E | TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2 | FE+BE |
| TC-FA-LBL-560 | E2E | TC-FA-LBL-E2E-117-gate-full-kolom-custom-field-setup-column-dan-pin-bagian-2-2 | FE+BE |
| TC-FA-LBL-561 | E2E | TC-FA-LBL-E2E-123-gate-none-pemegang-view-tagged-assets-tanpa-hak-nilai-bagian-2-2 | FE+BE |
| TC-FA-LBL-562 | E2E | TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | FE+BE |
| TC-FA-LBL-563 | E2E | TC-FA-LBL-E2E-148-sinkron-kolom-drawer-dari-modul-lain-transactional-policy-custom-field-last-scanned | FE+BE |
| TC-FA-LBL-564 | E2E | TC-FA-LBL-E2E-148-sinkron-kolom-drawer-dari-modul-lain-transactional-policy-custom-field-last-scanned | FE+BE |
| TC-FA-LBL-565 | E2E | TC-FA-LBL-E2E-148-sinkron-kolom-drawer-dari-modul-lain-transactional-policy-custom-field-last-scanned | FE+BE |
| TC-FA-LBL-566 | E2E | TC-FA-LBL-E2E-119-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-2-2 | FE+BE |
| TC-FA-LBL-567 | E2E | TC-FA-LBL-E2E-107-drawer-kolom-baru-setup-column-guard-dan-search-bagian-2-2 | FE+BE |
| TC-FA-LBL-568 | E2E | TC-FA-LBL-E2E-124-gate-tier-group-branch-total-control-default-user-read-only-dan-group-manager | FE+BE |
| TC-FA-LBL-569 | E2E | TC-FA-LBL-E2E-124-gate-tier-group-branch-total-control-default-user-read-only-dan-group-manager | FE+BE |
| TC-FA-LBL-570 | E2E | TC-FA-LBL-E2E-120-gate-purchase-warranty-expiry-dan-custom-field-purchasing | FE+BE |
| TC-FA-LBL-571 | E2E | TC-FA-LBL-E2E-125-lisensi-fa-7-kolom-custom-field-accounting-grace-period-dan-tidak-aktif | FE+BE |
| TC-FA-LBL-572 | E2E | TC-FA-LBL-E2E-125-lisensi-fa-7-kolom-custom-field-accounting-grace-period-dan-tidak-aktif | FE+BE |
| TC-FA-LBL-573 | E2E | TC-FA-LBL-E2E-125-lisensi-fa-7-kolom-custom-field-accounting-grace-period-dan-tidak-aktif | FE+BE |
| TC-FA-LBL-574 | E2E | TC-FA-LBL-E2E-108-drawer-kolom-baru-sort-measurement-transactional-policy-last-scanned-dan-tag | FE+BE |
| TC-FA-LBL-575 | E2E | TC-FA-LBL-E2E-095-filter-drawer-tagged-asset-bagian-2-2 | FE+BE |
| TC-FA-LBL-576 | E2E | TC-FA-LBL-E2E-118-gate-value-asset-value-dan-sel-no-access-sort-filter-search-tooltip-request-langsung-bagian-1-2 | FE+BE |
| TC-FA-LBL-577 | E2E | TC-FA-LBL-E2E-110-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-1-2 | FE+BE |
| TC-FA-LBL-578 | E2E | TC-FA-LBL-E2E-110-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-1-2 | FE+BE |
| TC-FA-LBL-579 | E2E | TC-FA-LBL-E2E-111-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-2-2 | FE+BE |
| TC-FA-LBL-580 | E2E | TC-FA-LBL-E2E-111-drawer-kolom-custom-field-tipe-dasar-company-fields-bagian-2-2 | FE+BE |
| TC-FA-LBL-581 | E2E | TC-FA-LBL-E2E-178-drawer-kolom-custom-field-formula-company-fields | FE+BE |
| TC-FA-LBL-582 | E2E | TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | FE+BE |
| TC-FA-LBL-583 | E2E | TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | FE+BE |
| TC-FA-LBL-584 | E2E | TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | FE+BE |
| TC-FA-LBL-585 | E2E | TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | FE+BE |
| TC-FA-LBL-586 | E2E | TC-FA-LBL-E2E-115-warranty-expiry-hari-ini-mengikuti-time-zone-general-settings | FE+BE |
| TC-FA-LBL-587 | E2E | TC-FA-LBL-E2E-114-penanda-masa-garansi-warranty-expiry-company-warranty | FE+BE |
| TC-FA-LBL-588 | E2E | TC-FA-LBL-E2E-109-drawer-kolom-baru-filter-sumber-0-baris-dan-sort-tag-awalan-pendek | FE+BE |
| TC-FA-LBL-589 | E2E | TC-FA-LBL-E2E-112-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-1-2 | FE+BE |
| TC-FA-LBL-590 | E2E | TC-FA-LBL-E2E-112-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-1-2 | FE+BE |
| TC-FA-LBL-591 | E2E | TC-FA-LBL-E2E-113-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-2-2 | FE+BE |
| TC-FA-LBL-592 | E2E | TC-FA-LBL-E2E-112-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-1-2 | FE+BE |
| TC-FA-LBL-593 | E2E | TC-FA-LBL-E2E-113-drawer-kolom-asset-value-commercial-dan-fiscal-company-depreciation-bagian-2-2 | FE+BE |

---

## 4. Keputusan Penulisan (2026-11-02)

- Asersi "tidak ada entri log baru" untuk TC request langsung, edit, delete, dan aksi gagal ditulis di spec asal dengan baseline jumlah entri (S-12), bukan di spec absence (S-05). Keputusan user: diterima karena spec absence tidak memiliki aksi nyata untuk TC tersebut.
- TC-321, TC-454, dan TC-461 mengasersi isi berkas ekspor (kelas f) di spec fungsional. Keputusan user: diterima.
- Spec yang tetap di atas 35 langkah punya alasan di `## Notes` masing-masing. Spec 012, 111, 128, 147, dan 172 dipecah ke nomor 177 sampai 181.
- Variabel env password Total Control Company Alpha di suite ini bernama `FA_LBL_TC_PASSWORD` (menghindari bentrok dengan `FA_TC_PASSWORD` di suite RolePermission).
