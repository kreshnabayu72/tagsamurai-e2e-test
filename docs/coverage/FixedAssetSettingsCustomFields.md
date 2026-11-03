# Coverage E2E — Fixed Asset > Settings > Custom Fields

Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md` (675 TC granular aktif); tidak ada `tc-settings-custom-fields-backend.md`, jadi tidak ada TC hanya-BE.
Suite: `specs/FixedAsset/SettingsCustomFields/`.
Prefix Modul: `FA` + `CF` (`TC-FA-CF-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (176 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | Screening Halaman Custom Fields dan Isi Tabel Baseline Tab General | FE+BE | 24 | TC-FA-CF-1, TC-FA-CF-2, TC-FA-CF-5, TC-FA-CF-10, TC-FA-CF-12, TC-FA-CF-13 |
| TC-FA-CF-E2E-002-tab-accounting-terkunci-tanpa-lisensi-fa7 | Tab Accounting Terkunci pada Client Tanpa Lisensi FA-7 | FE+BE | 13 | TC-FA-CF-3, TC-FA-CF-4, TC-FA-CF-51 |
| TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | Tampilan Sel Kolom Value Setting, Scope, Placeholder, dan Modified By | FE+BE | 17 | TC-FA-CF-6, TC-FA-CF-7, TC-FA-CF-8, TC-FA-CF-9, TC-FA-CF-11 |
| TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | Pemotongan Badge, Klik Area Baris, Scrollbar Tablet, dan Tinggi Baris | FE+BE | 18 | TC-FA-CF-14, TC-FA-CF-19, TC-FA-CF-611, TC-FA-CF-614 |
| TC-FA-CF-E2E-005-popup-all-values-preview | Popup All Values Preview: Buka, Tutup, dan Varian | FE+BE | 22 | TC-FA-CF-15, TC-FA-CF-16, TC-FA-CF-17, TC-FA-CF-18 |
| TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama | Empty State Company Kosong dan Create Field Pertama | FE+BE | 16 | TC-FA-CF-20, TC-FA-CF-203, TC-FA-CF-454, TC-FA-CF-640 |
| TC-FA-CF-E2E-007-state-tabel-no-results-skeleton-dan-loading-filter | State Tabel: No Results, Skeleton Loading, dan Loading Dropdown Filter | FE+BE | 16 | TC-FA-CF-21, TC-FA-CF-23, TC-FA-CF-641 |
| TC-FA-CF-E2E-008-tooltip-toolbar-dan-guided-tooltip-kunjungan-pertama | Tooltip Toolbar dan Guided Tooltip Kunjungan Pertama | FE+BE | 37 | TC-FA-CF-24, TC-FA-CF-25, TC-FA-CF-26 |
| TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create | Guided Tooltip: Navigasi Keluar, Keyboard, Overlay, dan Pemegang Create | FE+BE | 28 | TC-FA-CF-27, TC-FA-CF-28, TC-FA-CF-615, TC-FA-CF-616 |
| TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | Mobile Android: Card List, Tooltip Disabled, Bottom Sheet, dan Selection Mode | FE+BE | 35 | TC-FA-CF-29, TC-FA-CF-30, TC-FA-CF-31, TC-FA-CF-32, TC-FA-CF-612, TC-FA-CF-613 |
| TC-FA-CF-E2E-011-role-matrix-visibilitas-total-control-default-user-read-only | Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Total Control, Default User, Read Only) | FE+BE | 37 | TC-FA-CF-33, TC-FA-CF-34, TC-FA-CF-35 |
| TC-FA-CF-E2E-012-role-matrix-visibilitas-pemegang-read-create-update | Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Read, Create, Update) | FE+BE | 32 | TC-FA-CF-36, TC-FA-CF-37, TC-FA-CF-38 |
| TC-FA-CF-E2E-013-role-matrix-visibilitas-pemegang-delete-dan-crud | Role Matrix: Visibilitas Elemen Halaman Custom Fields per Role (Delete, Create-Update-Delete) | FE+BE | 26 | TC-FA-CF-39, TC-FA-CF-40 |
| TC-FA-CF-E2E-014-role-negatif-akses-halaman-tanpa-capability | Role Negatif: Menu Hidden dan Akses URL Langsung Tanpa Capability | FE+BE | 7 | TC-FA-CF-41, TC-FA-CF-49 |
| TC-FA-CF-E2E-015-role-positif-create-pemegang-create | Role Positif: Pemegang Create Menyelesaikan Create | FE+BE | 8 | TC-FA-CF-42 |
| TC-FA-CF-E2E-016-role-positif-edit-pemegang-update | Role Positif: Pemegang Update Menyelesaikan Edit | FE+BE | 9 | TC-FA-CF-43 |
| TC-FA-CF-E2E-017-role-positif-toggle-pemegang-update | Role Positif: Pemegang Update Toggle Status dan Bulk Deactivate | FE+BE | 15 | TC-FA-CF-44, TC-FA-CF-45 |
| TC-FA-CF-E2E-018-role-positif-delete-pemegang-delete | Role Positif: Pemegang Delete Delete dan Bulk Delete | FE+BE | 15 | TC-FA-CF-46, TC-FA-CF-47 |
| TC-FA-CF-E2E-019-role-negatif-aksi-disabled-dan-bulk-per-capability | Role Negatif: Switch Disabled Read Only dan Tombol Bulk per Capability | FE+BE | 12 | TC-FA-CF-48, TC-FA-CF-50 |
| TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas | Screening Modal Create: Nilai Default, Label Radio, dan Aksesibilitas | FE+BE | 36 | TC-FA-CF-52, TC-FA-CF-53, TC-FA-CF-201, TC-FA-CF-200 |
| TC-FA-CF-E2E-021-info-popover-dan-dropdown-data-type | Info Popover dan Dropdown Data Type | FE+BE | 22 | TC-FA-CF-57, TC-FA-CF-58 |
| TC-FA-CF-E2E-022-placeholder-default-per-data-type | Placeholder Default per Data Type pada Create | FE+BE | 17 | TC-FA-CF-59, TC-FA-CF-86, TC-FA-CF-87 |
| TC-FA-CF-E2E-023-validasi-placeholder-create | Validasi Placeholder pada Create | FE+BE | 21 | TC-FA-CF-89, TC-FA-CF-90, TC-FA-CF-88 |
| TC-FA-CF-E2E-024-validasi-field-name-kosong-spasi-dan-data-type-wajib | Validasi Field Name Kosong atau Spasi Saja dan Data Type Wajib | FE+BE | 20 | TC-FA-CF-60, TC-FA-CF-61, TC-FA-CF-71 |
| TC-FA-CF-E2E-025-validasi-field-name-batas-120-karakter | Validasi Field Name Batas 120 Karakter dan Spasi di Ujung | FE+BE | 28 | TC-FA-CF-63, TC-FA-CF-62, TC-FA-CF-64 |
| TC-FA-CF-E2E-026-field-name-emoji-dan-simbol | Field Name: Emoji dan Simbol Umum | FE+BE | 23 | TC-FA-CF-65, TC-FA-CF-66, TC-FA-CF-67 |
| TC-FA-CF-E2E-027-field-name-nama-duplikat-dan-overlap-scope | Field Name: Nama Duplikat, Beda Huruf, dan Scope Overlap | FE+BE | 22 | TC-FA-CF-68, TC-FA-CF-69, TC-FA-CF-70 |
| TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | Kontrol Data Type Dropdown, Multi-Dropdown, Numeric, Percentage, dan Formula | FE+BE | 26 | TC-FA-CF-72, TC-FA-CF-73, TC-FA-CF-74, TC-FA-CF-75, TC-FA-CF-76 |
| TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | Data Type Tanpa Kontrol Tambahan (Text sampai Currency) | FE+BE | 7 | TC-FA-CF-77, TC-FA-CF-78, TC-FA-CF-79, TC-FA-CF-80, TC-FA-CF-81 |
| TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document | Data Type Tanpa Kontrol Tambahan (Phone sampai Document) | FE+BE | 7 | TC-FA-CF-82, TC-FA-CF-83, TC-FA-CF-84, TC-FA-CF-85 |
| TC-FA-CF-E2E-031-scope-specific-asset-name-create | Scope Specific Asset Name pada Create | FE+BE | 26 | TC-FA-CF-91, TC-FA-CF-92, TC-FA-CF-93, TC-FA-CF-94 |
| TC-FA-CF-E2E-032-scope-asset-name-stale-dihapus-aktor-lain | Scope: Satu Asset Name Dihapus Aktor Lain Sebelum Submit | FE+BE | 28 | TC-FA-CF-95 |
| TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | Value Type Global: Kontrol dan Validasi Nilai Kosong | FE+BE | 35 | TC-FA-CF-99, TC-FA-CF-100, TC-FA-CF-101, TC-FA-CF-102, TC-FA-CF-103, TC-FA-CF-104 |
| TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang | Builder Opsi: Tambah Enter, Duplikat Case-Insensitive, dan Batas Panjang | FE+BE | 35 | TC-FA-CF-108, TC-FA-CF-109, TC-FA-CF-110, TC-FA-CF-111 |
| TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji | Builder Opsi: Spasi, Trim, dan Emoji | FE+BE | 29 | TC-FA-CF-112, TC-FA-CF-113, TC-FA-CF-114, TC-FA-CF-115 |
| TC-FA-CF-E2E-036-builder-opsi-hapus-opsi-dan-opsi-terakhir | Builder Opsi: Hapus Opsi dan Opsi Terakhir | FE+BE | 25 | TC-FA-CF-116, TC-FA-CF-117, TC-FA-CF-118 |
| TC-FA-CF-E2E-037-builder-opsi-submit-dropdown-tanpa-opsi | Builder Opsi: Submit Dropdown dan Multi-Dropdown Tanpa Opsi | FE+BE | 16 | TC-FA-CF-119, TC-FA-CF-120 |
| TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | Create Sukses: Global Value, Required, Jumlah Opsi, dan Ubah Nama Opsi | FE+BE | 42 | TC-FA-CF-105, TC-FA-CF-106, TC-FA-CF-107, TC-FA-CF-121, TC-FA-CF-122 |
| TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create | Decimal Places Numeric dan Percentage pada Create | FE+BE | 9 | TC-FA-CF-123, TC-FA-CF-124, TC-FA-CF-125, TC-FA-CF-126 |
| TC-FA-CF-E2E-040-grup-field-terikat-ke-tab-asal | Grup Field Terikat ke Tab Asal pada Create | FE+BE | 34 | TC-FA-CF-54, TC-FA-CF-55, TC-FA-CF-56 |
| TC-FA-CF-E2E-041-global-value-text-dan-text-area | Global Value Text, Text Area, dan Phone Kurang dari Empat Digit pada Create Custom Field | FE+BE | 25 | TC-FA-CF-127, TC-FA-CF-128, TC-FA-CF-129 |
| TC-FA-CF-E2E-042-global-value-phone | Global Value Phone: Batas 15 Digit dan Input Hanya Angka | FE+BE | 13 | TC-FA-CF-130, TC-FA-CF-131 |
| TC-FA-CF-E2E-043-global-value-date-dan-numeric | Global Value Date dan Numeric: Tanggal Tidak Valid, Decimal Places, Batas 15 Digit, dan Nilai Negatif | FE+BE | 35 | TC-FA-CF-132, TC-FA-CF-133, TC-FA-CF-134, TC-FA-CF-620 |
| TC-FA-CF-E2E-044-global-value-currency | Global Value Currency: Prefix Simbol, Nilai Negatif, Batas Dua Desimal, dan Batas 15 Digit | FE+BE | 34 | TC-FA-CF-135, TC-FA-CF-618, TC-FA-CF-619 |
| TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime | Global Value Percentage, Email, URL, dan DateTime: Nilai Tidak Valid Ditolak | FE+BE | 35 | TC-FA-CF-136, TC-FA-CF-137, TC-FA-CF-138, TC-FA-CF-139 |
| TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | Global Value Document: Kontrol Unggah, Format Berkas, dan Batas Ukuran 1 MB | FE+BE | 26 | TC-FA-CF-140, TC-FA-CF-141, TC-FA-CF-142, TC-FA-CF-143, TC-FA-CF-144 |
| TC-FA-CF-E2E-047-global-value-document-ganti-dan-hapus-file | Global Value Document: Kosong Ditolak, Ganti File, dan Hapus File | FE+BE | 19 | TC-FA-CF-145, TC-FA-CF-146, TC-FA-CF-147 |
| TC-FA-CF-E2E-048-global-value-document-submit-disabled-dan-per-asset-name | Global Value Document: Submit Disabled Saat File Dikirim dan Satu Kontrol Unggah per Asset Name | FE+BE | 24 | TC-FA-CF-148, TC-FA-CF-149 |
| TC-FA-CF-E2E-049-formula-builder-validasi-token | Formula Builder: Validasi Token Kosong, Tanpa Operator, Diawali Operator, dan Dua Operator Berurutan | FE+BE | 24 | TC-FA-CF-150, TC-FA-CF-151, TC-FA-CF-152, TC-FA-CF-153 |
| TC-FA-CF-E2E-050-formula-builder-formula-valid | Formula Builder: Berakhir Operator Ditolak, Formula Valid Tersimpan, dan Konstanta Desimal | FE+BE | 26 | TC-FA-CF-154, TC-FA-CF-155, TC-FA-CF-156 |
| TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | Create Sukses per Data Type: Text, Text Area, Dropdown, Multi-Dropdown, dan Date | FE+BE | 15 | TC-FA-CF-157, TC-FA-CF-158, TC-FA-CF-159, TC-FA-CF-160, TC-FA-CF-161 |
| TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | Create Sukses per Data Type: DateTime, Currency, Numeric, Phone, dan Percentage | FE+BE | 15 | TC-FA-CF-162, TC-FA-CF-163, TC-FA-CF-164, TC-FA-CF-165, TC-FA-CF-166 |
| TC-FA-CF-E2E-053-create-sukses-email-url-document-formula | Create Sukses per Data Type: Email, URL, Document, dan Formula | FE+BE | 22 | TC-FA-CF-167, TC-FA-CF-168, TC-FA-CF-169, TC-FA-CF-170 |
| TC-FA-CF-E2E-054-perilaku-form-create-stay-on-this-form | Perilaku Form Create: Checkbox Stay on this Form Dicentang, Tidak Dicentang, dan Create Berulang | FE+BE | 40 | TC-FA-CF-171, TC-FA-CF-172, TC-FA-CF-173 |
| TC-FA-CF-E2E-055-perilaku-form-create-submit-tidak-valid-dan-clear-field | Perilaku Form Create: Submit dengan Beberapa Field Tidak Valid dan Clear Field | FE+BE | 31 | TC-FA-CF-174, TC-FA-CF-175 |
| TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | Menutup Form Create dan Dialog Unsaved Changes: Cancel, Leave, Esc, Backdrop, dan Form Kembali Bersih | FE+BE | 36 | TC-FA-CF-176, TC-FA-CF-177, TC-FA-CF-178, TC-FA-CF-179, TC-FA-CF-180, TC-FA-CF-181 |
| TC-FA-CF-E2E-057-reload-dan-navigasi-saat-form-create-dirty | Reload dan Navigasi Internal Saat Form Create Dirty | FE+BE | 23 | TC-FA-CF-182, TC-FA-CF-183 |
| TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit | Batas Plafon Total Master Data Count Limit pada Create dan Delete | FE+BE | 29 | TC-FA-CF-188, TC-FA-CF-190, TC-FA-CF-324, TC-FA-CF-627 |
| TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create | Batas Cap Per Asset Name pada Create: Scope Specific, Scope General, Batas Tepat, dan Stay on this Form | FE+BE | 27 | TC-FA-CF-191, TC-FA-CF-192, TC-FA-CF-193, TC-FA-CF-197 |
| TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan | Batas Cap: Variasi Company, Lisensi FA-7 Tidak Aktif, dan Cap Diturunkan Saat Modal Create Terbuka | FE+BE | 40 | TC-FA-CF-194, TC-FA-CF-195, TC-FA-CF-196, TC-FA-CF-605 |
| TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | Screening Modal Edit dan Validasi Field Name | FE+BE | 37 | TC-FA-CF-205, TC-FA-CF-207, TC-FA-CF-208, TC-FA-CF-209, TC-FA-CF-210, TC-FA-CF-211 |
| TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by | Edit: Rename Field Name, Trim Spasi, dan Modified By | FE+BE | 30 | TC-FA-CF-206, TC-FA-CF-212, TC-FA-CF-219, TC-FA-CF-297 |
| TC-FA-CF-E2E-063-edit-placeholder-dan-required | Edit: Placeholder dan Required | FE+BE | 29 | TC-FA-CF-213, TC-FA-CF-214, TC-FA-CF-215, TC-FA-CF-216, TC-FA-CF-217, TC-FA-CF-218, TC-FA-CF-624 |
| TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog | Ganti Data Type: Dialog Change Data Type dan Kasus Tanpa Dialog | FE+BE | 31 | TC-FA-CF-223, TC-FA-CF-224, TC-FA-CF-226, TC-FA-CF-240 |
| TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places | Ganti Data Type: Pemulihan Nilai Tersimpan dan Decimal Places | FE+BE | 32 | TC-FA-CF-229, TC-FA-CF-230, TC-FA-CF-231, TC-FA-CF-232 |
| TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global | Ganti Data Type: Dropdown, Formula, dan Field Global | FE+BE | 38 | TC-FA-CF-233, TC-FA-CF-234, TC-FA-CF-235, TC-FA-CF-236 |
| TC-FA-CF-E2E-067-cancel-dialog-change-data-type-dan-dialog-berurutan | Cancel pada Dialog Change Data Type dan Dialog Berurutan | FE+BE | 37 | TC-FA-CF-227, TC-FA-CF-239 |
| TC-FA-CF-E2E-068-cancel-remove-value-value-type-dan-change-scope | Cancel pada Dialog Remove Value, Value Type, dan Change Scope | FE+BE | 40 | TC-FA-CF-250, TC-FA-CF-267, TC-FA-CF-622 |
| TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar | Kunci Decimal Places pada Edit: Tooltip dan Syarat Kunci | FE+BE | 22 | TC-FA-CF-241, TC-FA-CF-242, TC-FA-CF-243, TC-FA-CF-244 |
| TC-FA-CF-E2E-070-kunci-decimal-places-pada-edit-lanjutan | Kunci Decimal Places pada Edit: Pembukaan Kunci dan Penolakan Server | FE+BE | 22 | TC-FA-CF-245, TC-FA-CF-246, TC-FA-CF-247 |
| TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | Edit Opsi Dropdown: Rename dan Hapus Opsi yang Dipakai Aset | FE+BE | 36 | TC-FA-CF-248, TC-FA-CF-249, TC-FA-CF-251, TC-FA-CF-252, TC-FA-CF-253 |
| TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | Edit Opsi Dropdown: Tambah, Duplikat, Opsi Terakhir, dan Validasi | FE+BE | 36 | TC-FA-CF-254, TC-FA-CF-255, TC-FA-CF-256, TC-FA-CF-257, TC-FA-CF-258, TC-FA-CF-259, TC-FA-CF-625 |
| TC-FA-CF-E2E-073-edit-konflik-opsi-dihapus-dan-asset-name-dihapus-aktor-lain | Edit: Opsi Dropdown Dihapus atau Diganti Aktor Lain Saat Modal Terbuka | FE+BE | 28 | TC-FA-CF-260, TC-FA-CF-261 |
| TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | Edit Value Type: Specific ke Global dan Sebaliknya | FE+BE | 30 | TC-FA-CF-262, TC-FA-CF-263, TC-FA-CF-264, TC-FA-CF-265, TC-FA-CF-266 |
| TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | Edit Scope: Menambah dan Mengeluarkan Asset Name | FE+BE | 35 | TC-FA-CF-268, TC-FA-CF-269, TC-FA-CF-270, TC-FA-CF-271, TC-FA-CF-272 |
| TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | Edit Scope: Scope Kosong dan Field Global | FE+BE | 46 | TC-FA-CF-273, TC-FA-CF-274, TC-FA-CF-275, TC-FA-CF-276, TC-FA-CF-277 |
| TC-FA-CF-E2E-077-edit-cap-per-asset-name | Edit: Pemeriksaan Cap Per Asset Name | FE+BE | 39 | TC-FA-CF-278, TC-FA-CF-279, TC-FA-CF-280, TC-FA-CF-281, TC-FA-CF-282 |
| TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah | Edit: Token Formula, File Document, dan Grup Field | FE+BE | 29 | TC-FA-CF-283, TC-FA-CF-284, TC-FA-CF-285, TC-FA-CF-286 |
| TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop | Menutup Form Edit: Unsaved Changes dan Backdrop | FE+BE | 27 | TC-FA-CF-291, TC-FA-CF-292, TC-FA-CF-293, TC-FA-CF-294 |
| TC-FA-CF-E2E-080-menutup-form-edit-reload-clear-field-dan-cancel-popup | Form Edit: Reload, Clear Field, dan Cancel Dialog Popup Edit | FE+BE | 34 | TC-FA-CF-295, TC-FA-CF-296, TC-FA-CF-621 |
| TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | Toggle Status Single: Dialog Konfirmasi Deactivate dan Activate, Cancel, Esc, dan Konfirmasi | FE+BE | 39 | TC-FA-CF-298, TC-FA-CF-299, TC-FA-CF-300, TC-FA-CF-301, TC-FA-CF-304, TC-FA-CF-305, TC-FA-CF-306 |
| TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula | Toggle Status: Field Required, Pemulihan Nilai, Menu Row Action, dan Field Formula | FE+BE | 27 | TC-FA-CF-312, TC-FA-CF-313, TC-FA-CF-314, TC-FA-CF-316 |
| TC-FA-CF-E2E-083-cap-per-asset-name-activate-single | Cap Per Asset Name: Activate Single Ditolak di Atas Batas, Diterima di Batas, Scope Kosong, dan Kuota Dibebaskan Deactivate | FE+BE | 34 | TC-FA-CF-309, TC-FA-CF-310, TC-FA-CF-311, TC-FA-CF-626 |
| TC-FA-CF-E2E-084-cap-per-asset-name-bulk-activate-dan-delete | Cap Per Asset Name: Bulk Activate Ditolak Tanpa Perubahan Sebagian, Hitungan Kumulatif, dan Delete Membebaskan Kuota | FE+BE | 35 | TC-FA-CF-343, TC-FA-CF-344, TC-FA-CF-323 |
| TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset | Delete Single: Dialog Konfirmasi, Cancel, Konfirmasi Hapus, dan Penghapusan Nilai Aset Tanpa Orphan | FE+BE | 29 | TC-FA-CF-317, TC-FA-CF-318, TC-FA-CF-319, TC-FA-CF-320 |
| TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi | Klik Ganda Cepat pada Submit, Save, dan Konfirmasi Bulk Deactivate serta Bulk Activate | FE+BE | 49 | TC-FA-CF-186, TC-FA-CF-290, TC-FA-CF-633, TC-FA-CF-634 |
| TC-FA-CF-E2E-087-klik-ganda-cepat-pada-konfirmasi-delete-dan-bulk-delete | Klik Ganda Cepat pada Konfirmasi Delete dan Bulk Delete | FE+BE | 26 | TC-FA-CF-628, TC-FA-CF-636 |
| TC-FA-CF-E2E-088-kontrol-terkunci-selama-request-diproses | Kontrol Terkunci Selama Request Create, Edit, dan Toggle Status Diproses | FE+BE | 26 | TC-FA-CF-187, TC-FA-CF-315, TC-FA-CF-623 |
| TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | Bulk Action Bar: Varian Tombol, Counter, Clear Seleksi, Select All, dan Retensi Seleksi | FE+BE | 37 | TC-FA-CF-325, TC-FA-CF-326, TC-FA-CF-327, TC-FA-CF-328, TC-FA-CF-329, TC-FA-CF-347, TC-FA-CF-348 |
| TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | Bulk Activate dan Deactivate: Dialog Konfirmasi, Varian Single, Seleksi Campuran, dan Konfirmasi | FE+BE | 25 | TC-FA-CF-330, TC-FA-CF-331, TC-FA-CF-332, TC-FA-CF-333, TC-FA-CF-334, TC-FA-CF-335 |
| TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated | Bulk Activate dan Deactivate: Cancel Mempertahankan Seleksi, Baris Dilewati Tanpa Entri Log, dan Last Updated | FE+BE | 38 | TC-FA-CF-336, TC-FA-CF-337, TC-FA-CF-630, TC-FA-CF-635 |
| TC-FA-CF-E2E-092-bulk-sebagian-field-dihapus-aktor-lain-saat-aksi | Bulk Deactivate dan Bulk Delete: Sebagian Field Dihapus Aktor Lain Saat Aksi dan Toast Partial | FE+BE | 34 | TC-FA-CF-341, TC-FA-CF-355 |
| TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume | Selection Limit dan Checkbox Header pada Company Volume | FE+BE | 36 | TC-FA-CF-345, TC-FA-CF-346, TC-FA-CF-631, TC-FA-CF-632 |
| TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel | Bulk Delete: Dialog Konfirmasi, Varian Single, Cancel, dan Penghapusan Atomik Beserta Nilai Aset | FE+BE | 24 | TC-FA-CF-349, TC-FA-CF-350, TC-FA-CF-351, TC-FA-CF-352 |
| TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter | Search: Siklus Input, Enter, Icon Silang, dan Panah Kembali | FE+BE | 30 | TC-FA-CF-357, TC-FA-CF-358, TC-FA-CF-359, TC-FA-CF-360 |
| TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | Search: Pencocokan Kolom Teks, Enum, Modified By, Value Setting, dan Scope | FE+BE | 29 | TC-FA-CF-361, TC-FA-CF-362, TC-FA-CF-363, TC-FA-CF-364, TC-FA-CF-365 |
| TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | Search: Tanpa Hasil, Trim, Kolom Tersembunyi, State Per Tab, dan Irisan dengan Filter | FE+BE | 37 | TC-FA-CF-366, TC-FA-CF-367, TC-FA-CF-368, TC-FA-CF-370, TC-FA-CF-371, TC-FA-CF-373 |
| TC-FA-CF-E2E-098-search-sort-literal-dan-tie-breaker-company-nama-khusus | Search Literal, Sort Tie-Breaker, dan Sort Tanpa Peka Huruf (Company Nama Khusus) | FE+BE | 21 | TC-FA-CF-369, TC-FA-CF-404, TC-FA-CF-637 |
| TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | Filter: Screening Panel, Opsi dari Tab Aktif, dan Dropdown Multi-Select | FE+BE | 27 | TC-FA-CF-374, TC-FA-CF-375, TC-FA-CF-376, TC-FA-CF-377, TC-FA-CF-392 |
| TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | Filter: Modified By, Date Range, OR, AND, Apply, dan Draft | FE+BE | 29 | TC-FA-CF-378, TC-FA-CF-379, TC-FA-CF-380, TC-FA-CF-381, TC-FA-CF-382, TC-FA-CF-383, TC-FA-CF-384 |
| TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | Filter: Clear Field, Kotak Cari Dropdown, dan Chip | FE+BE | 36 | TC-FA-CF-385, TC-FA-CF-386, TC-FA-CF-387, TC-FA-CF-388, TC-FA-CF-638 |
| TC-FA-CF-E2E-102-filter-state-per-tab-kolom-disembunyikan-dan-hasil-kosong | Filter: State Per Tab, Kolom Disembunyikan, dan Hasil Kosong | FE+BE | 25 | TC-FA-CF-389, TC-FA-CF-390, TC-FA-CF-393 |
| TC-FA-CF-E2E-103-filter-opsi-baru-kriteria-hilang-dan-format-tanggal | Filter: Opsi Baru Setelah Create, Kriteria Hilang, dan Format Tanggal | FE+BE | 21 | TC-FA-CF-639, TC-FA-CF-642, TC-FA-CF-643 |
| TC-FA-CF-E2E-104-interaksi-search-filter-sort-dengan-create-dan-edit | Interaksi Search, Filter, dan Sort dengan Create dan Edit | FE+BE | 29 | TC-FA-CF-405, TC-FA-CF-645, TC-FA-CF-646 |
| TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | Sort: Field Name, Active, Data Type, Value Type, dan Placeholder | FE+BE | 25 | TC-FA-CF-394, TC-FA-CF-395, TC-FA-CF-396, TC-FA-CF-397, TC-FA-CF-398, TC-FA-CF-406 |
| TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | Sort: Required, Value Setting, Scope, Modified By, dan Last Updated | FE+BE | 18 | TC-FA-CF-399, TC-FA-CF-400, TC-FA-CF-401, TC-FA-CF-402, TC-FA-CF-403 |
| TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | Setup Column: Overlay, Popup, Discard, dan Batas Satu Kolom | FE+BE | 39 | TC-FA-CF-407, TC-FA-CF-408, TC-FA-CF-414, TC-FA-CF-415, TC-FA-CF-417 |
| TC-FA-CF-E2E-108-setup-column-ceklis-kolom-dan-reset-to-default | Setup Column: Ceklis Tiap Kolom dan Reset to Default | FE+BE | 21 | TC-FA-CF-409, TC-FA-CF-413 |
| TC-FA-CF-E2E-109-setup-column-reorder-dan-isolasi-konfigurasi-changelog | Setup Column: Reorder Tiap Kolom dan Isolasi dari Modal Changelog | FE+BE | 18 | TC-FA-CF-410, TC-FA-CF-416 |
| TC-FA-CF-E2E-110-setup-column-pin-dan-unpin | Setup Column: Pin dan Unpin Tiap Kolom | FE+BE | 20 | TC-FA-CF-411, TC-FA-CF-412 |
| TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | Download: Opsi CSV/XLSX, Nama Berkas, Scope Baris, dan Toast | FE+BE | 36 | TC-FA-CF-418, TC-FA-CF-420, TC-FA-CF-421, TC-FA-CF-422, TC-FA-CF-423, TC-FA-CF-425, TC-FA-CF-429, TC-FA-CF-432 |
| TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | Download: Isi Sel, BOM, dan Sheet Berkas CSV dan XLSX | FE+BE | 20 | TC-FA-CF-426, TC-FA-CF-427, TC-FA-CF-428, TC-FA-CF-430, TC-FA-CF-431 |
| TC-FA-CF-E2E-113-download-dan-paginasi-volume-besar | Download pada Volume Besar: 120 Baris, 5.001 Baris, dan 5.001 Entri Changelog | FE+BE | 21 | TC-FA-CF-419, TC-FA-CF-433, TC-FA-CF-479 |
| TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | Paginasi Company Volume: Ukuran Halaman dan Navigasi | FE+BE | 28 | TC-FA-CF-434, TC-FA-CF-435, TC-FA-CF-436, TC-FA-CF-437, TC-FA-CF-438, TC-FA-CF-440 |
| TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi | Paginasi Company Volume: Reset ke Halaman 1 dan Kombinasi Search, Filter, Sort | FE+BE | 24 | TC-FA-CF-372, TC-FA-CF-391, TC-FA-CF-441, TC-FA-CF-442 |
| TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | Retensi State F5, Reset Sidebar, dan Pindah Tab | FE+BE | 37 | TC-FA-CF-443, TC-FA-CF-444, TC-FA-CF-445, TC-FA-CF-446, TC-FA-CF-447 |
| TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | Modal Changelog: Screening, Judul, Penutupan, Urutan Default, dan Tooltip | FE+BE | 34 | TC-FA-CF-450, TC-FA-CF-451, TC-FA-CF-452, TC-FA-CF-453, TC-FA-CF-456, TC-FA-CF-457 |
| TC-FA-CF-E2E-118-changelog-search | Modal Changelog: Search | FE+BE | 31 | TC-FA-CF-455, TC-FA-CF-458, TC-FA-CF-459, TC-FA-CF-460, TC-FA-CF-461, TC-FA-CF-462 |
| TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by | Modal Changelog: Filter Screening, Dropdown, dan Modified By | FE+BE | 21 | TC-FA-CF-463, TC-FA-CF-464, TC-FA-CF-465, TC-FA-CF-466 |
| TC-FA-CF-E2E-120-changelog-filter-date-irisan-dan-search | Modal Changelog: Filter Date, Irisan Dua Filter, dan Search Gabungan | FE+BE | 17 | TC-FA-CF-467, TC-FA-CF-468, TC-FA-CF-469 |
| TC-FA-CF-E2E-121-changelog-sort | Modal Changelog: Sort | FE+BE | 27 | TC-FA-CF-470, TC-FA-CF-471, TC-FA-CF-472, TC-FA-CF-473 |
| TC-FA-CF-E2E-122-changelog-setup-column | Modal Changelog: Setup Column dan Isolasi dari Tabel Utama | FE+BE | 38 | TC-FA-CF-474, TC-FA-CF-475, TC-FA-CF-644 |
| TC-FA-CF-E2E-123-changelog-download-dan-paginasi | Modal Changelog: Download dan Paginasi | FE+BE | 23 | TC-FA-CF-476, TC-FA-CF-478 |
| TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | Log Tiga Surface: Create, Activate, Deactivate, dan Bulk Activate-Deactivate | FE+BE | 73 | TC-FA-CF-480, TC-FA-CF-481, TC-FA-CF-492, TC-FA-CF-493, TC-FA-CF-497, TC-FA-CF-498 |
| TC-FA-CF-E2E-125-log-delete-dan-bulk-delete | Log Tiga Surface: Delete dan Bulk Delete | FE+BE | 51 | TC-FA-CF-494, TC-FA-CF-495, TC-FA-CF-496 |
| TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | Log Tiga Surface: Edit Properti Name, Data Type, Decimal Places, Dropdown Options, dan Scope | FE+BE | 74 | TC-FA-CF-482, TC-FA-CF-483, TC-FA-CF-484, TC-FA-CF-485, TC-FA-CF-486 |
| TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | Log Tiga Surface: Edit Properti Value Type, Global Value, Formula, Placeholder, dan Required | FE+BE | 73 | TC-FA-CF-487, TC-FA-CF-488, TC-FA-CF-489, TC-FA-CF-490, TC-FA-CF-491 |
| TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | Log Tiga Surface: Multi-Properti, Penggantian Data Type, Opsi, dan Document | FE+BE | 57 | TC-FA-CF-499, TC-FA-CF-500, TC-FA-CF-501, TC-FA-CF-502, TC-FA-CF-647 |
| TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log | Log: Snapshot Nama, Sinkron, dan Kepemilikan System Log | FE+BE | 41 | TC-FA-CF-506, TC-FA-CF-507, TC-FA-CF-508, TC-FA-CF-509 |
| TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses | Log: Activity Log, Changelog Per Tab, Entri Ganda, dan Akses | FE+BE | 30 | TC-FA-CF-510, TC-FA-CF-511, TC-FA-CF-512, TC-FA-CF-513 |
| TC-FA-CF-E2E-131-absence-log-save-no-op | Absence Log: Save No-Op Tidak Menulis Entri di Tiga Surface | FE+BE | 49 | TC-FA-CF-220, TC-FA-CF-221, TC-FA-CF-222, TC-FA-CF-504 |
| TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | Absence Log: Aksi Gagal, Ditolak Validasi, Request Ditolak, dan Ditolak Lisensi Tidak Menulis Entri | FE+BE | 73 | TC-FA-CF-505, TC-FA-CF-514, TC-FA-CF-557, TC-FA-CF-572, TC-FA-CF-575, TC-FA-CF-576 |
| TC-FA-CF-E2E-133-absence-log-request-ditolak-server-dan-suspended | Absence Log: Request Langsung Ditolak dan Aksi Saat Client Suspended | FE+BE | 50 | TC-FA-CF-555, TC-FA-CF-584, TC-FA-CF-659 |
| TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | Cascade Penghapusan Asset Name ke Scope Field dan Log | FE+BE | 39 | TC-FA-CF-503, TC-FA-CF-515, TC-FA-CF-516, TC-FA-CF-517, TC-FA-CF-518, TC-FA-CF-519, TC-FA-CF-520 |
| TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | Sinkron Asset Name: Rename, Linked Custom Fields, Opsi Scope, dan Excess | FE+BE | 47 | TC-FA-CF-521, TC-FA-CF-522, TC-FA-CF-523, TC-FA-CF-655, TC-FA-CF-656 |
| TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | Form Registrasi Aset: Field Muncul Sesuai Scope, Active, dan Value Type | FE+BE | 24 | TC-FA-CF-524, TC-FA-CF-525, TC-FA-CF-526, TC-FA-CF-527, TC-FA-CF-528, TC-FA-CF-529, TC-FA-CF-530 |
| TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field | Form dan Detail Aset: Deactivate, Rename Opsi, Hapus Opsi, dan Delete Field | FE+BE | 27 | TC-FA-CF-531, TC-FA-CF-532, TC-FA-CF-533, TC-FA-CF-534 |
| TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | Form Aset: Required Non-Retroaktif, Header Kolom Opsional, dan Kontrol Input | FE+BE | 22 | TC-FA-CF-538, TC-FA-CF-539, TC-FA-CF-544, TC-FA-CF-657, TC-FA-CF-658 |
| TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul | Formula Lintas Modul: #ERROR, Presedensi, dan Evaluasi Saat Dibaca | FE+BE | 24 | TC-FA-CF-540, TC-FA-CF-541, TC-FA-CF-542, TC-FA-CF-543 |
| TC-FA-CF-E2E-140-asset-list-search-filter-teks-dropdown-dan-tanggal | Asset List: Search dan Filter Custom Field Teks, Dropdown, dan Tanggal | FE+BE | 18 | TC-FA-CF-648, TC-FA-CF-649, TC-FA-CF-650 |
| TC-FA-CF-E2E-141-asset-list-filter-rentang-nilai-dan-custom-field-non-searchable | Asset List: Filter Rentang Nilai dan Custom Field Non-Searchable atau Non-Filterable | FE+BE | 12 | TC-FA-CF-651, TC-FA-CF-652, TC-FA-CF-653 |
| TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency | Sinkron General Settings dan Identitas Aktor: Format Tanggal, Time Zone, Currency, dan Modified By | FE+BE | 16 | TC-FA-CF-548, TC-FA-CF-549, TC-FA-CF-550, TC-FA-CF-554 |
| TC-FA-CF-E2E-143-sinkron-limit-system-dan-capability-role | Sinkron Limit Plans dan Lifecycle Settings serta Capability Role | FE+BE | 14 | TC-FA-CF-551, TC-FA-CF-552, TC-FA-CF-553 |
| TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset | Lisensi FA-7 Lapse: Field Accounting Tidak Tampil di Form, Detail, dan Ekspor Aset | FE+BE | 32 | TC-FA-CF-545, TC-FA-CF-546, TC-FA-CF-654, TC-FA-CF-675 |
| TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | Grace Period FA-7: Tab Accounting Read-Only dan Form Aset | FE+BE | 38 | TC-FA-CF-547, TC-FA-CF-662, TC-FA-CF-667, TC-FA-CF-672, TC-FA-CF-674 |
| TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali | Grace Period FA-7: Search, Changelog, Download, Ekspor Aset, dan Lisensi Aktif Kembali | FE+BE | 30 | TC-FA-CF-663, TC-FA-CF-664, TC-FA-CF-668, TC-FA-CF-669 |
| TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | Request Langsung Field Accounting Ditolak 403 Saat FA-7 Tidak Aktif dan Grace Period | FE+BE | 22 | TC-FA-CF-577, TC-FA-CF-578, TC-FA-CF-579, TC-FA-CF-580, TC-FA-CF-673 |
| TC-FA-CF-E2E-148-lisensi-fa7-dicabut-saat-dialog-terbuka | Lisensi FA-7 Dicabut Saat Modal atau Dialog Terbuka | FE+BE | 31 | TC-FA-CF-581, TC-FA-CF-582, TC-FA-CF-583 |
| TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | Request Langsung Ditolak 403 per Capability | FE+BE | 21 | TC-FA-CF-556, TC-FA-CF-558, TC-FA-CF-559, TC-FA-CF-560, TC-FA-CF-561 |
| TC-FA-CF-E2E-150-isolasi-tenant-dan-render-teks-xss | Isolasi Tenant dan Render Teks untuk Payload Skrip atau Markup | FE+BE | 42 | TC-FA-CF-562, TC-FA-CF-563, TC-FA-CF-564 |
| TC-FA-CF-E2E-151-request-langsung-validasi-422 | Request Langsung Ditolak 422 (Validasi Payload Create) | FE+BE | 29 | TC-FA-CF-565, TC-FA-CF-566, TC-FA-CF-567, TC-FA-CF-568, TC-FA-CF-569, TC-FA-CF-570, TC-FA-CF-571 |
| TC-FA-CF-E2E-152-state-tenant-suspended | State Tenant: Aksi Tulis Ditolak Saat Suspended | FE+BE | 47 | TC-FA-CF-585, TC-FA-CF-586, TC-FA-CF-587, TC-FA-CF-588, TC-FA-CF-592 |
| TC-FA-CF-E2E-153-state-tenant-expired | State Tenant: Aksi Tulis Ditolak Saat Expired | FE+BE | 31 | TC-FA-CF-589, TC-FA-CF-590, TC-FA-CF-591 |
| TC-FA-CF-E2E-154-plan-gating-happy-path-semua-tier | Plan Gating: Happy Path Create, Edit, Toggle, dan Delete di Semua Tier | FE+BE | 22 | TC-FA-CF-661 |
| TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain | Konflik: Field Dihapus Aktor Lain Saat Edit, Delete, Deactivate, atau Activate | FE+BE | 83 | TC-FA-CF-594, TC-FA-CF-595, TC-FA-CF-596, TC-FA-CF-660 |
| TC-FA-CF-E2E-156-izin-dicabut-saat-aksi-dan-deactivate-idempoten | Izin Dicabut Saat Modal atau Dialog Terbuka dan Deactivate Idempoten | FE+BE | 31 | TC-FA-CF-597, TC-FA-CF-599, TC-FA-CF-600 |
| TC-FA-CF-E2E-157-dialog-konfirmasi-baru-muncul-setelah-form-dibuka | Dialog Konfirmasi yang Baru Muncul Setelah Form Dibuka (Data Type, Global, Scope) | FE+BE | 25 | TC-FA-CF-601, TC-FA-CF-602, TC-FA-CF-603 |
| TC-FA-CF-E2E-158-multi-konteks-race-dua-sesi-pada-kuota | Multi-Konteks: Race Dua Sesi pada Kuota Plafon dan Cap per Asset Name | FE+BE | 35 | TC-FA-CF-198, TC-FA-CF-199, TC-FA-CF-604 |
| TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log | Multi-Konteks: Edit Bersamaan, Sinkron Tabel Antar Sesi, dan Urutan Log | FE+BE | 49 | TC-FA-CF-598, TC-FA-CF-606, TC-FA-CF-607, TC-FA-CF-610 |
| TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast | Resilience: Gagal Muat Tabel, Create Timeout, Retry, dan Durasi Toast | FE+BE | 43 | TC-FA-CF-22, TC-FA-CF-185, TC-FA-CF-202, TC-FA-CF-609 |
| TC-FA-CF-E2E-161-resilience-edit-dan-delete | Resilience: Edit dan Delete 5xx dan Timeout | FE+BE | 58 | TC-FA-CF-287, TC-FA-CF-288, TC-FA-CF-289, TC-FA-CF-321, TC-FA-CF-322 |
| TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | Resilience: Toggle Single dan Bulk Delete 5xx dan Timeout | FE+BE | 51 | TC-FA-CF-302, TC-FA-CF-303, TC-FA-CF-307, TC-FA-CF-308, TC-FA-CF-353, TC-FA-CF-354 |
| TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | Resilience: Bulk Activate dan Deactivate, Download, dan Download Changelog | FE+BE | 55 | TC-FA-CF-338, TC-FA-CF-339, TC-FA-CF-340, TC-FA-CF-424, TC-FA-CF-477, TC-FA-CF-629 |
| TC-FA-CF-E2E-166-placeholder-default-dari-field-name-huruf-kecil | Placeholder Default Memakai Field Name Huruf Kecil | FE+BE | 20 | TC-FA-CF-204 |
| TC-FA-CF-E2E-167-scope-asset-name-stale-dua-tiga-dan-semua-dihapus-aktor-lain | Scope: Dua, Tiga, dan Seluruh Asset Name Dihapus Aktor Lain Sebelum Submit | FE+BE | 33 | TC-FA-CF-96, TC-FA-CF-97, TC-FA-CF-98 |
| TC-FA-CF-E2E-168-batas-plafon-sisa-kuota-terakhir-dan-stay-on-this-form | Batas Plafon Total pada Sisa Kuota Terakhir: Create ke-1000 Berhasil dan Create Berikutnya Diblokir | FE+BE | 30 | TC-FA-CF-189, TC-FA-CF-617 |
| TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan | Ganti Data Type: Konfirmasi pada Field Bernilai, Value Global Wajib Diisi Ulang, dan Dialog Berurutan | FE+BE | 39 | TC-FA-CF-225, TC-FA-CF-228, TC-FA-CF-237, TC-FA-CF-238 |
| TC-FA-CF-E2E-171-edit-asset-name-dihapus-aktor-lain-company-alpha | Edit: Asset Name pada Scope Dihapus Aktor Lain Saat Modal Terbuka | FE+BE | 27 | TC-FA-CF-608 |
| TC-FA-CF-E2E-172-bulk-seluruh-field-dihapus-aktor-lain-saat-aksi | Bulk Activate dan Bulk Delete: Seluruh Field Terpilih Dihapus Aktor Lain Saat Aksi dan Toast Tidak Tersedia | FE+BE | 38 | TC-FA-CF-342, TC-FA-CF-356 |
| TC-FA-CF-E2E-174-filter-chip-opsi-terpilih-diringkas-menjadi-n-more | Filter: Chip Opsi Terpilih Diringkas Menjadi +N more | FE+BE | 11 | TC-FA-CF-671 |
| TC-FA-CF-E2E-176-paginasi-company-volume-hapus-baris-terakhir-halaman-terakhir | Paginasi Company Volume: Hapus Baris Terakhir di Halaman Terakhir (Varian 101 Field) | FE+BE | 5 | TC-FA-CF-439 |
| TC-FA-CF-E2E-177-row-action-tanpa-detail-dan-tab-accounting-berlisensi | Row Action Tanpa Detail dan Tab Accounting Berlisensi FA-7 | FE+BE | 18 | TC-FA-CF-448, TC-FA-CF-449 |
| TC-FA-CF-E2E-178-form-dan-detail-aset-ganti-data-type-scope-dan-value-type | Detail Aset: Ganti Data Type, Keluarkan Asset Name dari Scope, dan Ubah Value Type | FE+BE | 14 | TC-FA-CF-535, TC-FA-CF-536, TC-FA-CF-537 |
| TC-FA-CF-E2E-179-absence-log-request-ditolak-grace-period-dan-create-gagal-5xx | Absence Log: Request Tulis Field Accounting Ditolak Saat Grace Period dan Create Gagal 5xx | FE+BE | 60 | TC-FA-CF-184, TC-FA-CF-665, TC-FA-CF-666 |
| TC-FA-CF-E2E-180-grace-period-fa7-berakhir-tab-accounting-terkunci-dan-field-tidak-tampil | Grace Period FA-7 Berakhir: Tab Accounting Terkunci dan Field Accounting Tidak Tampil | FE+BE | 13 | TC-FA-CF-670 |
| TC-FA-CF-E2E-181-request-langsung-validasi-opsi-duplikat-panjang-dan-kode-negara | Request Langsung Ditolak: Opsi Duplikat, Panjang Field Name, dan Kode Negara | FE+BE | 10 | TC-FA-CF-573, TC-FA-CF-574, TC-FA-CF-593 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua TC masuk tepat satu spec E2E.

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-CF-1 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-2 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-3 | E2E | TC-FA-CF-E2E-002-tab-accounting-terkunci-tanpa-lisensi-fa7 | FE+BE |
| TC-FA-CF-4 | E2E | TC-FA-CF-E2E-002-tab-accounting-terkunci-tanpa-lisensi-fa7 | FE+BE |
| TC-FA-CF-5 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-6 | E2E | TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | FE+BE |
| TC-FA-CF-7 | E2E | TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | FE+BE |
| TC-FA-CF-8 | E2E | TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | FE+BE |
| TC-FA-CF-9 | E2E | TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | FE+BE |
| TC-FA-CF-10 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-11 | E2E | TC-FA-CF-E2E-003-tampilan-sel-value-setting-scope-placeholder-modified-by | FE+BE |
| TC-FA-CF-12 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-13 | E2E | TC-FA-CF-E2E-001-screening-halaman-dan-isi-tabel-baseline | FE+BE |
| TC-FA-CF-14 | E2E | TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | FE+BE |
| TC-FA-CF-15 | E2E | TC-FA-CF-E2E-005-popup-all-values-preview | FE+BE |
| TC-FA-CF-16 | E2E | TC-FA-CF-E2E-005-popup-all-values-preview | FE+BE |
| TC-FA-CF-17 | E2E | TC-FA-CF-E2E-005-popup-all-values-preview | FE+BE |
| TC-FA-CF-18 | E2E | TC-FA-CF-E2E-005-popup-all-values-preview | FE+BE |
| TC-FA-CF-19 | E2E | TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | FE+BE |
| TC-FA-CF-20 | E2E | TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama | FE+BE |
| TC-FA-CF-21 | E2E | TC-FA-CF-E2E-007-state-tabel-no-results-skeleton-dan-loading-filter | FE+BE |
| TC-FA-CF-22 | E2E | TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast | FE+BE |
| TC-FA-CF-23 | E2E | TC-FA-CF-E2E-007-state-tabel-no-results-skeleton-dan-loading-filter | FE+BE |
| TC-FA-CF-24 | E2E | TC-FA-CF-E2E-008-tooltip-toolbar-dan-guided-tooltip-kunjungan-pertama | FE+BE |
| TC-FA-CF-25 | E2E | TC-FA-CF-E2E-008-tooltip-toolbar-dan-guided-tooltip-kunjungan-pertama | FE+BE |
| TC-FA-CF-26 | E2E | TC-FA-CF-E2E-008-tooltip-toolbar-dan-guided-tooltip-kunjungan-pertama | FE+BE |
| TC-FA-CF-27 | E2E | TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create | FE+BE |
| TC-FA-CF-28 | E2E | TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create | FE+BE |
| TC-FA-CF-29 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-30 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-31 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-32 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-33 | E2E | TC-FA-CF-E2E-011-role-matrix-visibilitas-total-control-default-user-read-only | FE+BE |
| TC-FA-CF-34 | E2E | TC-FA-CF-E2E-011-role-matrix-visibilitas-total-control-default-user-read-only | FE+BE |
| TC-FA-CF-35 | E2E | TC-FA-CF-E2E-011-role-matrix-visibilitas-total-control-default-user-read-only | FE+BE |
| TC-FA-CF-36 | E2E | TC-FA-CF-E2E-012-role-matrix-visibilitas-pemegang-read-create-update | FE+BE |
| TC-FA-CF-37 | E2E | TC-FA-CF-E2E-012-role-matrix-visibilitas-pemegang-read-create-update | FE+BE |
| TC-FA-CF-38 | E2E | TC-FA-CF-E2E-012-role-matrix-visibilitas-pemegang-read-create-update | FE+BE |
| TC-FA-CF-39 | E2E | TC-FA-CF-E2E-013-role-matrix-visibilitas-pemegang-delete-dan-crud | FE+BE |
| TC-FA-CF-40 | E2E | TC-FA-CF-E2E-013-role-matrix-visibilitas-pemegang-delete-dan-crud | FE+BE |
| TC-FA-CF-41 | E2E | TC-FA-CF-E2E-014-role-negatif-akses-halaman-tanpa-capability | FE+BE |
| TC-FA-CF-42 | E2E | TC-FA-CF-E2E-015-role-positif-create-pemegang-create | FE+BE |
| TC-FA-CF-43 | E2E | TC-FA-CF-E2E-016-role-positif-edit-pemegang-update | FE+BE |
| TC-FA-CF-44 | E2E | TC-FA-CF-E2E-017-role-positif-toggle-pemegang-update | FE+BE |
| TC-FA-CF-45 | E2E | TC-FA-CF-E2E-017-role-positif-toggle-pemegang-update | FE+BE |
| TC-FA-CF-46 | E2E | TC-FA-CF-E2E-018-role-positif-delete-pemegang-delete | FE+BE |
| TC-FA-CF-47 | E2E | TC-FA-CF-E2E-018-role-positif-delete-pemegang-delete | FE+BE |
| TC-FA-CF-48 | E2E | TC-FA-CF-E2E-019-role-negatif-aksi-disabled-dan-bulk-per-capability | FE+BE |
| TC-FA-CF-49 | E2E | TC-FA-CF-E2E-014-role-negatif-akses-halaman-tanpa-capability | FE+BE |
| TC-FA-CF-50 | E2E | TC-FA-CF-E2E-019-role-negatif-aksi-disabled-dan-bulk-per-capability | FE+BE |
| TC-FA-CF-51 | E2E | TC-FA-CF-E2E-002-tab-accounting-terkunci-tanpa-lisensi-fa7 | FE+BE |
| TC-FA-CF-52 | E2E | TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas | FE+BE |
| TC-FA-CF-53 | E2E | TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas | FE+BE |
| TC-FA-CF-54 | E2E | TC-FA-CF-E2E-040-grup-field-terikat-ke-tab-asal | FE+BE |
| TC-FA-CF-55 | E2E | TC-FA-CF-E2E-040-grup-field-terikat-ke-tab-asal | FE+BE |
| TC-FA-CF-56 | E2E | TC-FA-CF-E2E-040-grup-field-terikat-ke-tab-asal | FE+BE |
| TC-FA-CF-57 | E2E | TC-FA-CF-E2E-021-info-popover-dan-dropdown-data-type | FE+BE |
| TC-FA-CF-58 | E2E | TC-FA-CF-E2E-021-info-popover-dan-dropdown-data-type | FE+BE |
| TC-FA-CF-59 | E2E | TC-FA-CF-E2E-022-placeholder-default-per-data-type | FE+BE |
| TC-FA-CF-60 | E2E | TC-FA-CF-E2E-024-validasi-field-name-kosong-spasi-dan-data-type-wajib | FE+BE |
| TC-FA-CF-61 | E2E | TC-FA-CF-E2E-024-validasi-field-name-kosong-spasi-dan-data-type-wajib | FE+BE |
| TC-FA-CF-62 | E2E | TC-FA-CF-E2E-025-validasi-field-name-batas-120-karakter | FE+BE |
| TC-FA-CF-63 | E2E | TC-FA-CF-E2E-025-validasi-field-name-batas-120-karakter | FE+BE |
| TC-FA-CF-64 | E2E | TC-FA-CF-E2E-025-validasi-field-name-batas-120-karakter | FE+BE |
| TC-FA-CF-65 | E2E | TC-FA-CF-E2E-026-field-name-emoji-dan-simbol | FE+BE |
| TC-FA-CF-66 | E2E | TC-FA-CF-E2E-026-field-name-emoji-dan-simbol | FE+BE |
| TC-FA-CF-67 | E2E | TC-FA-CF-E2E-026-field-name-emoji-dan-simbol | FE+BE |
| TC-FA-CF-68 | E2E | TC-FA-CF-E2E-027-field-name-nama-duplikat-dan-overlap-scope | FE+BE |
| TC-FA-CF-69 | E2E | TC-FA-CF-E2E-027-field-name-nama-duplikat-dan-overlap-scope | FE+BE |
| TC-FA-CF-70 | E2E | TC-FA-CF-E2E-027-field-name-nama-duplikat-dan-overlap-scope | FE+BE |
| TC-FA-CF-71 | E2E | TC-FA-CF-E2E-024-validasi-field-name-kosong-spasi-dan-data-type-wajib | FE+BE |
| TC-FA-CF-72 | E2E | TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | FE+BE |
| TC-FA-CF-73 | E2E | TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | FE+BE |
| TC-FA-CF-74 | E2E | TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | FE+BE |
| TC-FA-CF-75 | E2E | TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | FE+BE |
| TC-FA-CF-76 | E2E | TC-FA-CF-E2E-028-kontrol-data-type-dropdown-multi-numeric-percentage-formula | FE+BE |
| TC-FA-CF-77 | E2E | TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | FE+BE |
| TC-FA-CF-78 | E2E | TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | FE+BE |
| TC-FA-CF-79 | E2E | TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | FE+BE |
| TC-FA-CF-80 | E2E | TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | FE+BE |
| TC-FA-CF-81 | E2E | TC-FA-CF-E2E-029-data-type-tanpa-kontrol-tambahan-text-sampai-currency | FE+BE |
| TC-FA-CF-82 | E2E | TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document | FE+BE |
| TC-FA-CF-83 | E2E | TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document | FE+BE |
| TC-FA-CF-84 | E2E | TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document | FE+BE |
| TC-FA-CF-85 | E2E | TC-FA-CF-E2E-030-data-type-tanpa-kontrol-tambahan-phone-sampai-document | FE+BE |
| TC-FA-CF-86 | E2E | TC-FA-CF-E2E-022-placeholder-default-per-data-type | FE+BE |
| TC-FA-CF-87 | E2E | TC-FA-CF-E2E-022-placeholder-default-per-data-type | FE+BE |
| TC-FA-CF-88 | E2E | TC-FA-CF-E2E-023-validasi-placeholder-create | FE+BE |
| TC-FA-CF-89 | E2E | TC-FA-CF-E2E-023-validasi-placeholder-create | FE+BE |
| TC-FA-CF-90 | E2E | TC-FA-CF-E2E-023-validasi-placeholder-create | FE+BE |
| TC-FA-CF-91 | E2E | TC-FA-CF-E2E-031-scope-specific-asset-name-create | FE+BE |
| TC-FA-CF-92 | E2E | TC-FA-CF-E2E-031-scope-specific-asset-name-create | FE+BE |
| TC-FA-CF-93 | E2E | TC-FA-CF-E2E-031-scope-specific-asset-name-create | FE+BE |
| TC-FA-CF-94 | E2E | TC-FA-CF-E2E-031-scope-specific-asset-name-create | FE+BE |
| TC-FA-CF-95 | E2E | TC-FA-CF-E2E-032-scope-asset-name-stale-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-96 | E2E | TC-FA-CF-E2E-167-scope-asset-name-stale-dua-tiga-dan-semua-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-97 | E2E | TC-FA-CF-E2E-167-scope-asset-name-stale-dua-tiga-dan-semua-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-98 | E2E | TC-FA-CF-E2E-167-scope-asset-name-stale-dua-tiga-dan-semua-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-99 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-100 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-101 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-102 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-103 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-104 | E2E | TC-FA-CF-E2E-033-value-type-global-kontrol-dan-validasi | FE+BE |
| TC-FA-CF-105 | E2E | TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | FE+BE |
| TC-FA-CF-106 | E2E | TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | FE+BE |
| TC-FA-CF-107 | E2E | TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | FE+BE |
| TC-FA-CF-108 | E2E | TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang | FE+BE |
| TC-FA-CF-109 | E2E | TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang | FE+BE |
| TC-FA-CF-110 | E2E | TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang | FE+BE |
| TC-FA-CF-111 | E2E | TC-FA-CF-E2E-034-builder-opsi-nama-duplikat-dan-batas-panjang | FE+BE |
| TC-FA-CF-112 | E2E | TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji | FE+BE |
| TC-FA-CF-113 | E2E | TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji | FE+BE |
| TC-FA-CF-114 | E2E | TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji | FE+BE |
| TC-FA-CF-115 | E2E | TC-FA-CF-E2E-035-builder-opsi-spasi-trim-dan-emoji | FE+BE |
| TC-FA-CF-116 | E2E | TC-FA-CF-E2E-036-builder-opsi-hapus-opsi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-117 | E2E | TC-FA-CF-E2E-036-builder-opsi-hapus-opsi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-118 | E2E | TC-FA-CF-E2E-036-builder-opsi-hapus-opsi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-119 | E2E | TC-FA-CF-E2E-037-builder-opsi-submit-dropdown-tanpa-opsi | FE+BE |
| TC-FA-CF-120 | E2E | TC-FA-CF-E2E-037-builder-opsi-submit-dropdown-tanpa-opsi | FE+BE |
| TC-FA-CF-121 | E2E | TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | FE+BE |
| TC-FA-CF-122 | E2E | TC-FA-CF-E2E-038-create-sukses-global-required-jumlah-opsi-dan-ubah-nama-opsi | FE+BE |
| TC-FA-CF-123 | E2E | TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create | FE+BE |
| TC-FA-CF-124 | E2E | TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create | FE+BE |
| TC-FA-CF-125 | E2E | TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create | FE+BE |
| TC-FA-CF-126 | E2E | TC-FA-CF-E2E-039-decimal-places-numeric-dan-percentage-pada-create | FE+BE |
| TC-FA-CF-127 | E2E | TC-FA-CF-E2E-041-global-value-text-dan-text-area | FE+BE |
| TC-FA-CF-128 | E2E | TC-FA-CF-E2E-041-global-value-text-dan-text-area | FE+BE |
| TC-FA-CF-129 | E2E | TC-FA-CF-E2E-041-global-value-text-dan-text-area | FE+BE |
| TC-FA-CF-130 | E2E | TC-FA-CF-E2E-042-global-value-phone | FE+BE |
| TC-FA-CF-131 | E2E | TC-FA-CF-E2E-042-global-value-phone | FE+BE |
| TC-FA-CF-132 | E2E | TC-FA-CF-E2E-043-global-value-date-dan-numeric | FE+BE |
| TC-FA-CF-133 | E2E | TC-FA-CF-E2E-043-global-value-date-dan-numeric | FE+BE |
| TC-FA-CF-134 | E2E | TC-FA-CF-E2E-043-global-value-date-dan-numeric | FE+BE |
| TC-FA-CF-135 | E2E | TC-FA-CF-E2E-044-global-value-currency | FE+BE |
| TC-FA-CF-136 | E2E | TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime | FE+BE |
| TC-FA-CF-137 | E2E | TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime | FE+BE |
| TC-FA-CF-138 | E2E | TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime | FE+BE |
| TC-FA-CF-139 | E2E | TC-FA-CF-E2E-045-global-value-percentage-email-url-dan-datetime | FE+BE |
| TC-FA-CF-140 | E2E | TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | FE+BE |
| TC-FA-CF-141 | E2E | TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | FE+BE |
| TC-FA-CF-142 | E2E | TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | FE+BE |
| TC-FA-CF-143 | E2E | TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | FE+BE |
| TC-FA-CF-144 | E2E | TC-FA-CF-E2E-046-global-value-document-unggah-dan-batas-ukuran | FE+BE |
| TC-FA-CF-145 | E2E | TC-FA-CF-E2E-047-global-value-document-ganti-dan-hapus-file | FE+BE |
| TC-FA-CF-146 | E2E | TC-FA-CF-E2E-047-global-value-document-ganti-dan-hapus-file | FE+BE |
| TC-FA-CF-147 | E2E | TC-FA-CF-E2E-047-global-value-document-ganti-dan-hapus-file | FE+BE |
| TC-FA-CF-148 | E2E | TC-FA-CF-E2E-048-global-value-document-submit-disabled-dan-per-asset-name | FE+BE |
| TC-FA-CF-149 | E2E | TC-FA-CF-E2E-048-global-value-document-submit-disabled-dan-per-asset-name | FE+BE |
| TC-FA-CF-150 | E2E | TC-FA-CF-E2E-049-formula-builder-validasi-token | FE+BE |
| TC-FA-CF-151 | E2E | TC-FA-CF-E2E-049-formula-builder-validasi-token | FE+BE |
| TC-FA-CF-152 | E2E | TC-FA-CF-E2E-049-formula-builder-validasi-token | FE+BE |
| TC-FA-CF-153 | E2E | TC-FA-CF-E2E-049-formula-builder-validasi-token | FE+BE |
| TC-FA-CF-154 | E2E | TC-FA-CF-E2E-050-formula-builder-formula-valid | FE+BE |
| TC-FA-CF-155 | E2E | TC-FA-CF-E2E-050-formula-builder-formula-valid | FE+BE |
| TC-FA-CF-156 | E2E | TC-FA-CF-E2E-050-formula-builder-formula-valid | FE+BE |
| TC-FA-CF-157 | E2E | TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | FE+BE |
| TC-FA-CF-158 | E2E | TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | FE+BE |
| TC-FA-CF-159 | E2E | TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | FE+BE |
| TC-FA-CF-160 | E2E | TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | FE+BE |
| TC-FA-CF-161 | E2E | TC-FA-CF-E2E-051-create-sukses-text-text-area-dropdown-multi-dropdown-date | FE+BE |
| TC-FA-CF-162 | E2E | TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | FE+BE |
| TC-FA-CF-163 | E2E | TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | FE+BE |
| TC-FA-CF-164 | E2E | TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | FE+BE |
| TC-FA-CF-165 | E2E | TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | FE+BE |
| TC-FA-CF-166 | E2E | TC-FA-CF-E2E-052-create-sukses-datetime-currency-numeric-phone-percentage | FE+BE |
| TC-FA-CF-167 | E2E | TC-FA-CF-E2E-053-create-sukses-email-url-document-formula | FE+BE |
| TC-FA-CF-168 | E2E | TC-FA-CF-E2E-053-create-sukses-email-url-document-formula | FE+BE |
| TC-FA-CF-169 | E2E | TC-FA-CF-E2E-053-create-sukses-email-url-document-formula | FE+BE |
| TC-FA-CF-170 | E2E | TC-FA-CF-E2E-053-create-sukses-email-url-document-formula | FE+BE |
| TC-FA-CF-171 | E2E | TC-FA-CF-E2E-054-perilaku-form-create-stay-on-this-form | FE+BE |
| TC-FA-CF-172 | E2E | TC-FA-CF-E2E-054-perilaku-form-create-stay-on-this-form | FE+BE |
| TC-FA-CF-173 | E2E | TC-FA-CF-E2E-054-perilaku-form-create-stay-on-this-form | FE+BE |
| TC-FA-CF-174 | E2E | TC-FA-CF-E2E-055-perilaku-form-create-submit-tidak-valid-dan-clear-field | FE+BE |
| TC-FA-CF-175 | E2E | TC-FA-CF-E2E-055-perilaku-form-create-submit-tidak-valid-dan-clear-field | FE+BE |
| TC-FA-CF-176 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-177 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-178 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-179 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-180 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-181 | E2E | TC-FA-CF-E2E-056-menutup-form-create-dan-unsaved-changes | FE+BE |
| TC-FA-CF-182 | E2E | TC-FA-CF-E2E-057-reload-dan-navigasi-saat-form-create-dirty | FE+BE |
| TC-FA-CF-183 | E2E | TC-FA-CF-E2E-057-reload-dan-navigasi-saat-form-create-dirty | FE+BE |
| TC-FA-CF-184 | E2E | TC-FA-CF-E2E-179-absence-log-request-ditolak-grace-period-dan-create-gagal-5xx | FE+BE |
| TC-FA-CF-185 | E2E | TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast | FE+BE |
| TC-FA-CF-186 | E2E | TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi | FE+BE |
| TC-FA-CF-187 | E2E | TC-FA-CF-E2E-088-kontrol-terkunci-selama-request-diproses | FE+BE |
| TC-FA-CF-188 | E2E | TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit | FE+BE |
| TC-FA-CF-189 | E2E | TC-FA-CF-E2E-168-batas-plafon-sisa-kuota-terakhir-dan-stay-on-this-form | FE+BE |
| TC-FA-CF-190 | E2E | TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit | FE+BE |
| TC-FA-CF-191 | E2E | TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create | FE+BE |
| TC-FA-CF-192 | E2E | TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create | FE+BE |
| TC-FA-CF-193 | E2E | TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create | FE+BE |
| TC-FA-CF-194 | E2E | TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan | FE+BE |
| TC-FA-CF-195 | E2E | TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan | FE+BE |
| TC-FA-CF-196 | E2E | TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan | FE+BE |
| TC-FA-CF-197 | E2E | TC-FA-CF-E2E-059-batas-cap-per-asset-name-pada-create | FE+BE |
| TC-FA-CF-198 | E2E | TC-FA-CF-E2E-158-multi-konteks-race-dua-sesi-pada-kuota | FE+BE |
| TC-FA-CF-199 | E2E | TC-FA-CF-E2E-158-multi-konteks-race-dua-sesi-pada-kuota | FE+BE |
| TC-FA-CF-200 | E2E | TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas | FE+BE |
| TC-FA-CF-201 | E2E | TC-FA-CF-E2E-020-screening-modal-create-default-dan-aksesibilitas | FE+BE |
| TC-FA-CF-202 | E2E | TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast | FE+BE |
| TC-FA-CF-203 | E2E | TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama | FE+BE |
| TC-FA-CF-204 | E2E | TC-FA-CF-E2E-166-placeholder-default-dari-field-name-huruf-kecil | FE+BE |
| TC-FA-CF-205 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-206 | E2E | TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by | FE+BE |
| TC-FA-CF-207 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-208 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-209 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-210 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-211 | E2E | TC-FA-CF-E2E-061-screening-modal-edit-dan-validasi-field-name | FE+BE |
| TC-FA-CF-212 | E2E | TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by | FE+BE |
| TC-FA-CF-213 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-214 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-215 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-216 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-217 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-218 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-219 | E2E | TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by | FE+BE |
| TC-FA-CF-220 | E2E | TC-FA-CF-E2E-131-absence-log-save-no-op | FE+BE |
| TC-FA-CF-221 | E2E | TC-FA-CF-E2E-131-absence-log-save-no-op | FE+BE |
| TC-FA-CF-222 | E2E | TC-FA-CF-E2E-131-absence-log-save-no-op | FE+BE |
| TC-FA-CF-223 | E2E | TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog | FE+BE |
| TC-FA-CF-224 | E2E | TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog | FE+BE |
| TC-FA-CF-225 | E2E | TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-226 | E2E | TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog | FE+BE |
| TC-FA-CF-227 | E2E | TC-FA-CF-E2E-067-cancel-dialog-change-data-type-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-228 | E2E | TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-229 | E2E | TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places | FE+BE |
| TC-FA-CF-230 | E2E | TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places | FE+BE |
| TC-FA-CF-231 | E2E | TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places | FE+BE |
| TC-FA-CF-232 | E2E | TC-FA-CF-E2E-065-ganti-data-type-pemulihan-nilai-tersimpan-dan-decimal-places | FE+BE |
| TC-FA-CF-233 | E2E | TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global | FE+BE |
| TC-FA-CF-234 | E2E | TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global | FE+BE |
| TC-FA-CF-235 | E2E | TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global | FE+BE |
| TC-FA-CF-236 | E2E | TC-FA-CF-E2E-066-ganti-data-type-dropdown-formula-dan-global | FE+BE |
| TC-FA-CF-237 | E2E | TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-238 | E2E | TC-FA-CF-E2E-170-ganti-data-type-konfirmasi-field-bernilai-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-239 | E2E | TC-FA-CF-E2E-067-cancel-dialog-change-data-type-dan-dialog-berurutan | FE+BE |
| TC-FA-CF-240 | E2E | TC-FA-CF-E2E-064-ganti-data-type-dialog-konfirmasi-dan-tanpa-dialog | FE+BE |
| TC-FA-CF-241 | E2E | TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar | FE+BE |
| TC-FA-CF-242 | E2E | TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar | FE+BE |
| TC-FA-CF-243 | E2E | TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar | FE+BE |
| TC-FA-CF-244 | E2E | TC-FA-CF-E2E-069-kunci-decimal-places-pada-edit-dasar | FE+BE |
| TC-FA-CF-245 | E2E | TC-FA-CF-E2E-070-kunci-decimal-places-pada-edit-lanjutan | FE+BE |
| TC-FA-CF-246 | E2E | TC-FA-CF-E2E-070-kunci-decimal-places-pada-edit-lanjutan | FE+BE |
| TC-FA-CF-247 | E2E | TC-FA-CF-E2E-070-kunci-decimal-places-pada-edit-lanjutan | FE+BE |
| TC-FA-CF-248 | E2E | TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | FE+BE |
| TC-FA-CF-249 | E2E | TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | FE+BE |
| TC-FA-CF-250 | E2E | TC-FA-CF-E2E-068-cancel-remove-value-value-type-dan-change-scope | FE+BE |
| TC-FA-CF-251 | E2E | TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | FE+BE |
| TC-FA-CF-252 | E2E | TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | FE+BE |
| TC-FA-CF-253 | E2E | TC-FA-CF-E2E-071-edit-opsi-dropdown-rename-hapus-opsi-in-use | FE+BE |
| TC-FA-CF-254 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-255 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-256 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-257 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-258 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-259 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-260 | E2E | TC-FA-CF-E2E-073-edit-konflik-opsi-dihapus-dan-asset-name-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-261 | E2E | TC-FA-CF-E2E-073-edit-konflik-opsi-dihapus-dan-asset-name-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-262 | E2E | TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | FE+BE |
| TC-FA-CF-263 | E2E | TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | FE+BE |
| TC-FA-CF-264 | E2E | TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | FE+BE |
| TC-FA-CF-265 | E2E | TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | FE+BE |
| TC-FA-CF-266 | E2E | TC-FA-CF-E2E-074-edit-value-type-specific-dan-global | FE+BE |
| TC-FA-CF-267 | E2E | TC-FA-CF-E2E-068-cancel-remove-value-value-type-dan-change-scope | FE+BE |
| TC-FA-CF-268 | E2E | TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | FE+BE |
| TC-FA-CF-269 | E2E | TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | FE+BE |
| TC-FA-CF-270 | E2E | TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | FE+BE |
| TC-FA-CF-271 | E2E | TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | FE+BE |
| TC-FA-CF-272 | E2E | TC-FA-CF-E2E-075-edit-scope-menambah-dan-mengeluarkan-asset-name | FE+BE |
| TC-FA-CF-273 | E2E | TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | FE+BE |
| TC-FA-CF-274 | E2E | TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | FE+BE |
| TC-FA-CF-275 | E2E | TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | FE+BE |
| TC-FA-CF-276 | E2E | TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | FE+BE |
| TC-FA-CF-277 | E2E | TC-FA-CF-E2E-076-edit-scope-field-global-dan-scope-kosong | FE+BE |
| TC-FA-CF-278 | E2E | TC-FA-CF-E2E-077-edit-cap-per-asset-name | FE+BE |
| TC-FA-CF-279 | E2E | TC-FA-CF-E2E-077-edit-cap-per-asset-name | FE+BE |
| TC-FA-CF-280 | E2E | TC-FA-CF-E2E-077-edit-cap-per-asset-name | FE+BE |
| TC-FA-CF-281 | E2E | TC-FA-CF-E2E-077-edit-cap-per-asset-name | FE+BE |
| TC-FA-CF-282 | E2E | TC-FA-CF-E2E-077-edit-cap-per-asset-name | FE+BE |
| TC-FA-CF-283 | E2E | TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah | FE+BE |
| TC-FA-CF-284 | E2E | TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah | FE+BE |
| TC-FA-CF-285 | E2E | TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah | FE+BE |
| TC-FA-CF-286 | E2E | TC-FA-CF-E2E-078-edit-formula-document-dan-grup-tidak-dapat-diubah | FE+BE |
| TC-FA-CF-287 | E2E | TC-FA-CF-E2E-161-resilience-edit-dan-delete | FE+BE |
| TC-FA-CF-288 | E2E | TC-FA-CF-E2E-161-resilience-edit-dan-delete | FE+BE |
| TC-FA-CF-289 | E2E | TC-FA-CF-E2E-161-resilience-edit-dan-delete | FE+BE |
| TC-FA-CF-290 | E2E | TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi | FE+BE |
| TC-FA-CF-291 | E2E | TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop | FE+BE |
| TC-FA-CF-292 | E2E | TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop | FE+BE |
| TC-FA-CF-293 | E2E | TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop | FE+BE |
| TC-FA-CF-294 | E2E | TC-FA-CF-E2E-079-menutup-form-edit-unsaved-changes-dan-backdrop | FE+BE |
| TC-FA-CF-295 | E2E | TC-FA-CF-E2E-080-menutup-form-edit-reload-clear-field-dan-cancel-popup | FE+BE |
| TC-FA-CF-296 | E2E | TC-FA-CF-E2E-080-menutup-form-edit-reload-clear-field-dan-cancel-popup | FE+BE |
| TC-FA-CF-297 | E2E | TC-FA-CF-E2E-062-edit-rename-field-name-dan-modified-by | FE+BE |
| TC-FA-CF-298 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-299 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-300 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-301 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-302 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-303 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-304 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-305 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-306 | E2E | TC-FA-CF-E2E-081-toggle-single-dialog-konfirmasi-activate-dan-deactivate | FE+BE |
| TC-FA-CF-307 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-308 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-309 | E2E | TC-FA-CF-E2E-083-cap-per-asset-name-activate-single | FE+BE |
| TC-FA-CF-310 | E2E | TC-FA-CF-E2E-083-cap-per-asset-name-activate-single | FE+BE |
| TC-FA-CF-311 | E2E | TC-FA-CF-E2E-083-cap-per-asset-name-activate-single | FE+BE |
| TC-FA-CF-312 | E2E | TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula | FE+BE |
| TC-FA-CF-313 | E2E | TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula | FE+BE |
| TC-FA-CF-314 | E2E | TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula | FE+BE |
| TC-FA-CF-315 | E2E | TC-FA-CF-E2E-088-kontrol-terkunci-selama-request-diproses | FE+BE |
| TC-FA-CF-316 | E2E | TC-FA-CF-E2E-082-toggle-field-required-bernilai-row-action-dan-formula | FE+BE |
| TC-FA-CF-317 | E2E | TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset | FE+BE |
| TC-FA-CF-318 | E2E | TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset | FE+BE |
| TC-FA-CF-319 | E2E | TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset | FE+BE |
| TC-FA-CF-320 | E2E | TC-FA-CF-E2E-085-delete-single-dialog-konfirmasi-dan-nilai-aset | FE+BE |
| TC-FA-CF-321 | E2E | TC-FA-CF-E2E-161-resilience-edit-dan-delete | FE+BE |
| TC-FA-CF-322 | E2E | TC-FA-CF-E2E-161-resilience-edit-dan-delete | FE+BE |
| TC-FA-CF-323 | E2E | TC-FA-CF-E2E-084-cap-per-asset-name-bulk-activate-dan-delete | FE+BE |
| TC-FA-CF-324 | E2E | TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit | FE+BE |
| TC-FA-CF-325 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-326 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-327 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-328 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-329 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-330 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-331 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-332 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-333 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-334 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-335 | E2E | TC-FA-CF-E2E-090-bulk-activate-deactivate-dialog-dan-konfirmasi | FE+BE |
| TC-FA-CF-336 | E2E | TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated | FE+BE |
| TC-FA-CF-337 | E2E | TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated | FE+BE |
| TC-FA-CF-338 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-339 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-340 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-341 | E2E | TC-FA-CF-E2E-092-bulk-sebagian-field-dihapus-aktor-lain-saat-aksi | FE+BE |
| TC-FA-CF-342 | E2E | TC-FA-CF-E2E-172-bulk-seluruh-field-dihapus-aktor-lain-saat-aksi | FE+BE |
| TC-FA-CF-343 | E2E | TC-FA-CF-E2E-084-cap-per-asset-name-bulk-activate-dan-delete | FE+BE |
| TC-FA-CF-344 | E2E | TC-FA-CF-E2E-084-cap-per-asset-name-bulk-activate-dan-delete | FE+BE |
| TC-FA-CF-345 | E2E | TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume | FE+BE |
| TC-FA-CF-346 | E2E | TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume | FE+BE |
| TC-FA-CF-347 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-348 | E2E | TC-FA-CF-E2E-089-bulk-action-bar-seleksi-counter-dan-select-all | FE+BE |
| TC-FA-CF-349 | E2E | TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-FA-CF-350 | E2E | TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-FA-CF-351 | E2E | TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-FA-CF-352 | E2E | TC-FA-CF-E2E-094-bulk-delete-dialog-konfirmasi-dan-cancel | FE+BE |
| TC-FA-CF-353 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-354 | E2E | TC-FA-CF-E2E-162-resilience-toggle-single-dan-bulk-delete | FE+BE |
| TC-FA-CF-355 | E2E | TC-FA-CF-E2E-092-bulk-sebagian-field-dihapus-aktor-lain-saat-aksi | FE+BE |
| TC-FA-CF-356 | E2E | TC-FA-CF-E2E-172-bulk-seluruh-field-dihapus-aktor-lain-saat-aksi | FE+BE |
| TC-FA-CF-357 | E2E | TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter | FE+BE |
| TC-FA-CF-358 | E2E | TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter | FE+BE |
| TC-FA-CF-359 | E2E | TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter | FE+BE |
| TC-FA-CF-360 | E2E | TC-FA-CF-E2E-095-search-input-siklus-buka-tutup-dan-enter | FE+BE |
| TC-FA-CF-361 | E2E | TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | FE+BE |
| TC-FA-CF-362 | E2E | TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | FE+BE |
| TC-FA-CF-363 | E2E | TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | FE+BE |
| TC-FA-CF-364 | E2E | TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | FE+BE |
| TC-FA-CF-365 | E2E | TC-FA-CF-E2E-096-search-cocok-kolom-teks-enum-modified-by-value-setting-scope | FE+BE |
| TC-FA-CF-366 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-367 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-368 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-369 | E2E | TC-FA-CF-E2E-098-search-sort-literal-dan-tie-breaker-company-nama-khusus | FE+BE |
| TC-FA-CF-370 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-371 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-372 | E2E | TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi | FE+BE |
| TC-FA-CF-373 | E2E | TC-FA-CF-E2E-097-search-tanpa-hasil-trim-kolom-tersembunyi-dan-tab | FE+BE |
| TC-FA-CF-374 | E2E | TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | FE+BE |
| TC-FA-CF-375 | E2E | TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | FE+BE |
| TC-FA-CF-376 | E2E | TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | FE+BE |
| TC-FA-CF-377 | E2E | TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | FE+BE |
| TC-FA-CF-378 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-379 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-380 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-381 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-382 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-383 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-384 | E2E | TC-FA-CF-E2E-100-filter-semantik-modified-by-date-or-and-apply | FE+BE |
| TC-FA-CF-385 | E2E | TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | FE+BE |
| TC-FA-CF-386 | E2E | TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | FE+BE |
| TC-FA-CF-387 | E2E | TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | FE+BE |
| TC-FA-CF-388 | E2E | TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | FE+BE |
| TC-FA-CF-389 | E2E | TC-FA-CF-E2E-102-filter-state-per-tab-kolom-disembunyikan-dan-hasil-kosong | FE+BE |
| TC-FA-CF-390 | E2E | TC-FA-CF-E2E-102-filter-state-per-tab-kolom-disembunyikan-dan-hasil-kosong | FE+BE |
| TC-FA-CF-391 | E2E | TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi | FE+BE |
| TC-FA-CF-392 | E2E | TC-FA-CF-E2E-099-filter-screening-opsi-dan-dropdown-standar | FE+BE |
| TC-FA-CF-393 | E2E | TC-FA-CF-E2E-102-filter-state-per-tab-kolom-disembunyikan-dan-hasil-kosong | FE+BE |
| TC-FA-CF-394 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-395 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-396 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-397 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-398 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-399 | E2E | TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | FE+BE |
| TC-FA-CF-400 | E2E | TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | FE+BE |
| TC-FA-CF-401 | E2E | TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | FE+BE |
| TC-FA-CF-402 | E2E | TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | FE+BE |
| TC-FA-CF-403 | E2E | TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated | FE+BE |
| TC-FA-CF-404 | E2E | TC-FA-CF-E2E-098-search-sort-literal-dan-tie-breaker-company-nama-khusus | FE+BE |
| TC-FA-CF-405 | E2E | TC-FA-CF-E2E-104-interaksi-search-filter-sort-dengan-create-dan-edit | FE+BE |
| TC-FA-CF-406 | E2E | TC-FA-CF-E2E-105-sort-field-name-active-data-type-value-type-placeholder | FE+BE |
| TC-FA-CF-407 | E2E | TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | FE+BE |
| TC-FA-CF-408 | E2E | TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | FE+BE |
| TC-FA-CF-409 | E2E | TC-FA-CF-E2E-108-setup-column-ceklis-kolom-dan-reset-to-default | FE+BE |
| TC-FA-CF-410 | E2E | TC-FA-CF-E2E-109-setup-column-reorder-dan-isolasi-konfigurasi-changelog | FE+BE |
| TC-FA-CF-411 | E2E | TC-FA-CF-E2E-110-setup-column-pin-dan-unpin | FE+BE |
| TC-FA-CF-412 | E2E | TC-FA-CF-E2E-110-setup-column-pin-dan-unpin | FE+BE |
| TC-FA-CF-413 | E2E | TC-FA-CF-E2E-108-setup-column-ceklis-kolom-dan-reset-to-default | FE+BE |
| TC-FA-CF-414 | E2E | TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | FE+BE |
| TC-FA-CF-415 | E2E | TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | FE+BE |
| TC-FA-CF-416 | E2E | TC-FA-CF-E2E-109-setup-column-reorder-dan-isolasi-konfigurasi-changelog | FE+BE |
| TC-FA-CF-417 | E2E | TC-FA-CF-E2E-107-setup-column-overlay-popup-discard-dan-batas-kolom | FE+BE |
| TC-FA-CF-418 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-419 | E2E | TC-FA-CF-E2E-113-download-dan-paginasi-volume-besar | FE+BE |
| TC-FA-CF-420 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-421 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-422 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-423 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-424 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-425 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-426 | E2E | TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CF-427 | E2E | TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CF-428 | E2E | TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CF-429 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-430 | E2E | TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CF-431 | E2E | TC-FA-CF-E2E-112-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CF-432 | E2E | TC-FA-CF-E2E-111-download-opsi-nama-berkas-scope-baris-dan-toast | FE+BE |
| TC-FA-CF-433 | E2E | TC-FA-CF-E2E-113-download-dan-paginasi-volume-besar | FE+BE |
| TC-FA-CF-434 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-435 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-436 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-437 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-438 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-439 | E2E | TC-FA-CF-E2E-176-paginasi-company-volume-hapus-baris-terakhir-halaman-terakhir | FE+BE |
| TC-FA-CF-440 | E2E | TC-FA-CF-E2E-114-paginasi-company-volume-ukuran-halaman-dan-navigasi | FE+BE |
| TC-FA-CF-441 | E2E | TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi | FE+BE |
| TC-FA-CF-442 | E2E | TC-FA-CF-E2E-115-paginasi-company-volume-reset-halaman-dan-kombinasi | FE+BE |
| TC-FA-CF-443 | E2E | TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | FE+BE |
| TC-FA-CF-444 | E2E | TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | FE+BE |
| TC-FA-CF-445 | E2E | TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | FE+BE |
| TC-FA-CF-446 | E2E | TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | FE+BE |
| TC-FA-CF-447 | E2E | TC-FA-CF-E2E-116-retensi-state-f5-sidebar-dan-pindah-tab | FE+BE |
| TC-FA-CF-448 | E2E | TC-FA-CF-E2E-177-row-action-tanpa-detail-dan-tab-accounting-berlisensi | FE+BE |
| TC-FA-CF-449 | E2E | TC-FA-CF-E2E-177-row-action-tanpa-detail-dan-tab-accounting-berlisensi | FE+BE |
| TC-FA-CF-450 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-451 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-452 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-453 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-454 | E2E | TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama | FE+BE |
| TC-FA-CF-455 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-456 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-457 | E2E | TC-FA-CF-E2E-117-changelog-screening-judul-urutan-default-dan-tooltip | FE+BE |
| TC-FA-CF-458 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-459 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-460 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-461 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-462 | E2E | TC-FA-CF-E2E-118-changelog-search | FE+BE |
| TC-FA-CF-463 | E2E | TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by | FE+BE |
| TC-FA-CF-464 | E2E | TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by | FE+BE |
| TC-FA-CF-465 | E2E | TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by | FE+BE |
| TC-FA-CF-466 | E2E | TC-FA-CF-E2E-119-changelog-filter-screening-dropdown-dan-modified-by | FE+BE |
| TC-FA-CF-467 | E2E | TC-FA-CF-E2E-120-changelog-filter-date-irisan-dan-search | FE+BE |
| TC-FA-CF-468 | E2E | TC-FA-CF-E2E-120-changelog-filter-date-irisan-dan-search | FE+BE |
| TC-FA-CF-469 | E2E | TC-FA-CF-E2E-120-changelog-filter-date-irisan-dan-search | FE+BE |
| TC-FA-CF-470 | E2E | TC-FA-CF-E2E-121-changelog-sort | FE+BE |
| TC-FA-CF-471 | E2E | TC-FA-CF-E2E-121-changelog-sort | FE+BE |
| TC-FA-CF-472 | E2E | TC-FA-CF-E2E-121-changelog-sort | FE+BE |
| TC-FA-CF-473 | E2E | TC-FA-CF-E2E-121-changelog-sort | FE+BE |
| TC-FA-CF-474 | E2E | TC-FA-CF-E2E-122-changelog-setup-column | FE+BE |
| TC-FA-CF-475 | E2E | TC-FA-CF-E2E-122-changelog-setup-column | FE+BE |
| TC-FA-CF-476 | E2E | TC-FA-CF-E2E-123-changelog-download-dan-paginasi | FE+BE |
| TC-FA-CF-477 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-478 | E2E | TC-FA-CF-E2E-123-changelog-download-dan-paginasi | FE+BE |
| TC-FA-CF-479 | E2E | TC-FA-CF-E2E-113-download-dan-paginasi-volume-besar | FE+BE |
| TC-FA-CF-480 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-481 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-482 | E2E | TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | FE+BE |
| TC-FA-CF-483 | E2E | TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | FE+BE |
| TC-FA-CF-484 | E2E | TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | FE+BE |
| TC-FA-CF-485 | E2E | TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | FE+BE |
| TC-FA-CF-486 | E2E | TC-FA-CF-E2E-126-log-edit-properti-name-data-type-decimal-places-options-scope | FE+BE |
| TC-FA-CF-487 | E2E | TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | FE+BE |
| TC-FA-CF-488 | E2E | TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | FE+BE |
| TC-FA-CF-489 | E2E | TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | FE+BE |
| TC-FA-CF-490 | E2E | TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | FE+BE |
| TC-FA-CF-491 | E2E | TC-FA-CF-E2E-127-log-edit-properti-value-type-global-formula-placeholder-required | FE+BE |
| TC-FA-CF-492 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-493 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-494 | E2E | TC-FA-CF-E2E-125-log-delete-dan-bulk-delete | FE+BE |
| TC-FA-CF-495 | E2E | TC-FA-CF-E2E-125-log-delete-dan-bulk-delete | FE+BE |
| TC-FA-CF-496 | E2E | TC-FA-CF-E2E-125-log-delete-dan-bulk-delete | FE+BE |
| TC-FA-CF-497 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-498 | E2E | TC-FA-CF-E2E-124-log-create-activate-deactivate-dan-bulk-activate | FE+BE |
| TC-FA-CF-499 | E2E | TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | FE+BE |
| TC-FA-CF-500 | E2E | TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | FE+BE |
| TC-FA-CF-501 | E2E | TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | FE+BE |
| TC-FA-CF-502 | E2E | TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | FE+BE |
| TC-FA-CF-503 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-504 | E2E | TC-FA-CF-E2E-131-absence-log-save-no-op | FE+BE |
| TC-FA-CF-505 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-506 | E2E | TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log | FE+BE |
| TC-FA-CF-507 | E2E | TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log | FE+BE |
| TC-FA-CF-508 | E2E | TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log | FE+BE |
| TC-FA-CF-509 | E2E | TC-FA-CF-E2E-129-log-snapshot-nama-saat-kejadian-dan-kepemilikan-system-log | FE+BE |
| TC-FA-CF-510 | E2E | TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses | FE+BE |
| TC-FA-CF-511 | E2E | TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses | FE+BE |
| TC-FA-CF-512 | E2E | TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses | FE+BE |
| TC-FA-CF-513 | E2E | TC-FA-CF-E2E-130-log-activity-log-changelog-per-tab-dan-akses | FE+BE |
| TC-FA-CF-514 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-515 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-516 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-517 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-518 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-519 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-520 | E2E | TC-FA-CF-E2E-134-cascade-penghapusan-asset-name-ke-scope-field | FE+BE |
| TC-FA-CF-521 | E2E | TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | FE+BE |
| TC-FA-CF-522 | E2E | TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | FE+BE |
| TC-FA-CF-523 | E2E | TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | FE+BE |
| TC-FA-CF-524 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-525 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-526 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-527 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-528 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-529 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-530 | E2E | TC-FA-CF-E2E-136-form-registrasi-field-muncul-sesuai-scope-active-dan-value-type | FE+BE |
| TC-FA-CF-531 | E2E | TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field | FE+BE |
| TC-FA-CF-532 | E2E | TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field | FE+BE |
| TC-FA-CF-533 | E2E | TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field | FE+BE |
| TC-FA-CF-534 | E2E | TC-FA-CF-E2E-137-form-registrasi-dan-detail-aset-perubahan-konfigurasi-field | FE+BE |
| TC-FA-CF-535 | E2E | TC-FA-CF-E2E-178-form-dan-detail-aset-ganti-data-type-scope-dan-value-type | FE+BE |
| TC-FA-CF-536 | E2E | TC-FA-CF-E2E-178-form-dan-detail-aset-ganti-data-type-scope-dan-value-type | FE+BE |
| TC-FA-CF-537 | E2E | TC-FA-CF-E2E-178-form-dan-detail-aset-ganti-data-type-scope-dan-value-type | FE+BE |
| TC-FA-CF-538 | E2E | TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | FE+BE |
| TC-FA-CF-539 | E2E | TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | FE+BE |
| TC-FA-CF-540 | E2E | TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul | FE+BE |
| TC-FA-CF-541 | E2E | TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul | FE+BE |
| TC-FA-CF-542 | E2E | TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul | FE+BE |
| TC-FA-CF-543 | E2E | TC-FA-CF-E2E-139-formula-evaluasi-error-dan-presedensi-lintas-modul | FE+BE |
| TC-FA-CF-544 | E2E | TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | FE+BE |
| TC-FA-CF-545 | E2E | TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset | FE+BE |
| TC-FA-CF-546 | E2E | TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset | FE+BE |
| TC-FA-CF-547 | E2E | TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | FE+BE |
| TC-FA-CF-548 | E2E | TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency | FE+BE |
| TC-FA-CF-549 | E2E | TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency | FE+BE |
| TC-FA-CF-550 | E2E | TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency | FE+BE |
| TC-FA-CF-551 | E2E | TC-FA-CF-E2E-143-sinkron-limit-system-dan-capability-role | FE+BE |
| TC-FA-CF-552 | E2E | TC-FA-CF-E2E-143-sinkron-limit-system-dan-capability-role | FE+BE |
| TC-FA-CF-553 | E2E | TC-FA-CF-E2E-143-sinkron-limit-system-dan-capability-role | FE+BE |
| TC-FA-CF-554 | E2E | TC-FA-CF-E2E-142-sinkron-general-settings-format-tanggal-dan-currency | FE+BE |
| TC-FA-CF-555 | E2E | TC-FA-CF-E2E-133-absence-log-request-ditolak-server-dan-suspended | FE+BE |
| TC-FA-CF-556 | E2E | TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | FE+BE |
| TC-FA-CF-557 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-558 | E2E | TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | FE+BE |
| TC-FA-CF-559 | E2E | TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | FE+BE |
| TC-FA-CF-560 | E2E | TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | FE+BE |
| TC-FA-CF-561 | E2E | TC-FA-CF-E2E-149-request-langsung-rbac-403-per-capability | FE+BE |
| TC-FA-CF-562 | E2E | TC-FA-CF-E2E-150-isolasi-tenant-dan-render-teks-xss | FE+BE |
| TC-FA-CF-563 | E2E | TC-FA-CF-E2E-150-isolasi-tenant-dan-render-teks-xss | FE+BE |
| TC-FA-CF-564 | E2E | TC-FA-CF-E2E-150-isolasi-tenant-dan-render-teks-xss | FE+BE |
| TC-FA-CF-565 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-566 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-567 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-568 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-569 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-570 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-571 | E2E | TC-FA-CF-E2E-151-request-langsung-validasi-422 | FE+BE |
| TC-FA-CF-572 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-573 | E2E | TC-FA-CF-E2E-181-request-langsung-validasi-opsi-duplikat-panjang-dan-kode-negara | FE+BE |
| TC-FA-CF-574 | E2E | TC-FA-CF-E2E-181-request-langsung-validasi-opsi-duplikat-panjang-dan-kode-negara | FE+BE |
| TC-FA-CF-575 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-576 | E2E | TC-FA-CF-E2E-132-absence-log-aksi-gagal-ditolak-validasi-request-ditolak-dan-ditolak-lisensi | FE+BE |
| TC-FA-CF-577 | E2E | TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | FE+BE |
| TC-FA-CF-578 | E2E | TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | FE+BE |
| TC-FA-CF-579 | E2E | TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | FE+BE |
| TC-FA-CF-580 | E2E | TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | FE+BE |
| TC-FA-CF-581 | E2E | TC-FA-CF-E2E-148-lisensi-fa7-dicabut-saat-dialog-terbuka | FE+BE |
| TC-FA-CF-582 | E2E | TC-FA-CF-E2E-148-lisensi-fa7-dicabut-saat-dialog-terbuka | FE+BE |
| TC-FA-CF-583 | E2E | TC-FA-CF-E2E-148-lisensi-fa7-dicabut-saat-dialog-terbuka | FE+BE |
| TC-FA-CF-584 | E2E | TC-FA-CF-E2E-133-absence-log-request-ditolak-server-dan-suspended | FE+BE |
| TC-FA-CF-585 | E2E | TC-FA-CF-E2E-152-state-tenant-suspended | FE+BE |
| TC-FA-CF-586 | E2E | TC-FA-CF-E2E-152-state-tenant-suspended | FE+BE |
| TC-FA-CF-587 | E2E | TC-FA-CF-E2E-152-state-tenant-suspended | FE+BE |
| TC-FA-CF-588 | E2E | TC-FA-CF-E2E-152-state-tenant-suspended | FE+BE |
| TC-FA-CF-589 | E2E | TC-FA-CF-E2E-153-state-tenant-expired | FE+BE |
| TC-FA-CF-590 | E2E | TC-FA-CF-E2E-153-state-tenant-expired | FE+BE |
| TC-FA-CF-591 | E2E | TC-FA-CF-E2E-153-state-tenant-expired | FE+BE |
| TC-FA-CF-592 | E2E | TC-FA-CF-E2E-152-state-tenant-suspended | FE+BE |
| TC-FA-CF-593 | E2E | TC-FA-CF-E2E-181-request-langsung-validasi-opsi-duplikat-panjang-dan-kode-negara | FE+BE |
| TC-FA-CF-594 | E2E | TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-595 | E2E | TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-596 | E2E | TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-597 | E2E | TC-FA-CF-E2E-156-izin-dicabut-saat-aksi-dan-deactivate-idempoten | FE+BE |
| TC-FA-CF-598 | E2E | TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log | FE+BE |
| TC-FA-CF-599 | E2E | TC-FA-CF-E2E-156-izin-dicabut-saat-aksi-dan-deactivate-idempoten | FE+BE |
| TC-FA-CF-600 | E2E | TC-FA-CF-E2E-156-izin-dicabut-saat-aksi-dan-deactivate-idempoten | FE+BE |
| TC-FA-CF-601 | E2E | TC-FA-CF-E2E-157-dialog-konfirmasi-baru-muncul-setelah-form-dibuka | FE+BE |
| TC-FA-CF-602 | E2E | TC-FA-CF-E2E-157-dialog-konfirmasi-baru-muncul-setelah-form-dibuka | FE+BE |
| TC-FA-CF-603 | E2E | TC-FA-CF-E2E-157-dialog-konfirmasi-baru-muncul-setelah-form-dibuka | FE+BE |
| TC-FA-CF-604 | E2E | TC-FA-CF-E2E-158-multi-konteks-race-dua-sesi-pada-kuota | FE+BE |
| TC-FA-CF-605 | E2E | TC-FA-CF-E2E-060-batas-cap-variasi-company-lisensi-dan-cap-diturunkan | FE+BE |
| TC-FA-CF-606 | E2E | TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log | FE+BE |
| TC-FA-CF-607 | E2E | TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log | FE+BE |
| TC-FA-CF-608 | E2E | TC-FA-CF-E2E-171-edit-asset-name-dihapus-aktor-lain-company-alpha | FE+BE |
| TC-FA-CF-609 | E2E | TC-FA-CF-E2E-160-resilience-gagal-muat-tabel-create-timeout-retry-dan-durasi-toast | FE+BE |
| TC-FA-CF-610 | E2E | TC-FA-CF-E2E-159-multi-konteks-edit-bersamaan-sinkron-tabel-dan-urutan-log | FE+BE |
| TC-FA-CF-611 | E2E | TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | FE+BE |
| TC-FA-CF-612 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-613 | E2E | TC-FA-CF-E2E-010-mobile-android-card-list-bottom-sheet-dan-selection-mode | FE+BE |
| TC-FA-CF-614 | E2E | TC-FA-CF-E2E-004-truncation-badge-klik-baris-tablet-dan-tinggi-baris | FE+BE |
| TC-FA-CF-615 | E2E | TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create | FE+BE |
| TC-FA-CF-616 | E2E | TC-FA-CF-E2E-009-guided-tooltip-navigasi-keyboard-overlay-dan-pemegang-create | FE+BE |
| TC-FA-CF-617 | E2E | TC-FA-CF-E2E-168-batas-plafon-sisa-kuota-terakhir-dan-stay-on-this-form | FE+BE |
| TC-FA-CF-618 | E2E | TC-FA-CF-E2E-044-global-value-currency | FE+BE |
| TC-FA-CF-619 | E2E | TC-FA-CF-E2E-044-global-value-currency | FE+BE |
| TC-FA-CF-620 | E2E | TC-FA-CF-E2E-043-global-value-date-dan-numeric | FE+BE |
| TC-FA-CF-621 | E2E | TC-FA-CF-E2E-080-menutup-form-edit-reload-clear-field-dan-cancel-popup | FE+BE |
| TC-FA-CF-622 | E2E | TC-FA-CF-E2E-068-cancel-remove-value-value-type-dan-change-scope | FE+BE |
| TC-FA-CF-623 | E2E | TC-FA-CF-E2E-088-kontrol-terkunci-selama-request-diproses | FE+BE |
| TC-FA-CF-624 | E2E | TC-FA-CF-E2E-063-edit-placeholder-dan-required | FE+BE |
| TC-FA-CF-625 | E2E | TC-FA-CF-E2E-072-edit-opsi-dropdown-validasi-dan-opsi-terakhir | FE+BE |
| TC-FA-CF-626 | E2E | TC-FA-CF-E2E-083-cap-per-asset-name-activate-single | FE+BE |
| TC-FA-CF-627 | E2E | TC-FA-CF-E2E-058-batas-plafon-total-master-data-count-limit | FE+BE |
| TC-FA-CF-628 | E2E | TC-FA-CF-E2E-087-klik-ganda-cepat-pada-konfirmasi-delete-dan-bulk-delete | FE+BE |
| TC-FA-CF-629 | E2E | TC-FA-CF-E2E-163-resilience-bulk-activate-deactivate-download-dan-changelog | FE+BE |
| TC-FA-CF-630 | E2E | TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated | FE+BE |
| TC-FA-CF-631 | E2E | TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume | FE+BE |
| TC-FA-CF-632 | E2E | TC-FA-CF-E2E-093-selection-limit-dan-checkbox-header-company-volume | FE+BE |
| TC-FA-CF-633 | E2E | TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi | FE+BE |
| TC-FA-CF-634 | E2E | TC-FA-CF-E2E-086-klik-ganda-cepat-pada-submit-save-dan-bulk-aksi | FE+BE |
| TC-FA-CF-635 | E2E | TC-FA-CF-E2E-091-bulk-activate-melewati-baris-cancel-dan-last-updated | FE+BE |
| TC-FA-CF-636 | E2E | TC-FA-CF-E2E-087-klik-ganda-cepat-pada-konfirmasi-delete-dan-bulk-delete | FE+BE |
| TC-FA-CF-637 | E2E | TC-FA-CF-E2E-098-search-sort-literal-dan-tie-breaker-company-nama-khusus | FE+BE |
| TC-FA-CF-638 | E2E | TC-FA-CF-E2E-101-filter-chip-clear-field-dan-hapus-centang | FE+BE |
| TC-FA-CF-639 | E2E | TC-FA-CF-E2E-103-filter-opsi-baru-kriteria-hilang-dan-format-tanggal | FE+BE |
| TC-FA-CF-640 | E2E | TC-FA-CF-E2E-006-empty-state-company-kosong-dan-create-pertama | FE+BE |
| TC-FA-CF-641 | E2E | TC-FA-CF-E2E-007-state-tabel-no-results-skeleton-dan-loading-filter | FE+BE |
| TC-FA-CF-642 | E2E | TC-FA-CF-E2E-103-filter-opsi-baru-kriteria-hilang-dan-format-tanggal | FE+BE |
| TC-FA-CF-643 | E2E | TC-FA-CF-E2E-103-filter-opsi-baru-kriteria-hilang-dan-format-tanggal | FE+BE |
| TC-FA-CF-644 | E2E | TC-FA-CF-E2E-122-changelog-setup-column | FE+BE |
| TC-FA-CF-645 | E2E | TC-FA-CF-E2E-104-interaksi-search-filter-sort-dengan-create-dan-edit | FE+BE |
| TC-FA-CF-646 | E2E | TC-FA-CF-E2E-104-interaksi-search-filter-sort-dengan-create-dan-edit | FE+BE |
| TC-FA-CF-647 | E2E | TC-FA-CF-E2E-128-log-edit-multi-properti-penggantian-data-type-dan-document | FE+BE |
| TC-FA-CF-648 | E2E | TC-FA-CF-E2E-140-asset-list-search-filter-teks-dropdown-dan-tanggal | FE+BE |
| TC-FA-CF-649 | E2E | TC-FA-CF-E2E-140-asset-list-search-filter-teks-dropdown-dan-tanggal | FE+BE |
| TC-FA-CF-650 | E2E | TC-FA-CF-E2E-140-asset-list-search-filter-teks-dropdown-dan-tanggal | FE+BE |
| TC-FA-CF-651 | E2E | TC-FA-CF-E2E-141-asset-list-filter-rentang-nilai-dan-custom-field-non-searchable | FE+BE |
| TC-FA-CF-652 | E2E | TC-FA-CF-E2E-141-asset-list-filter-rentang-nilai-dan-custom-field-non-searchable | FE+BE |
| TC-FA-CF-653 | E2E | TC-FA-CF-E2E-141-asset-list-filter-rentang-nilai-dan-custom-field-non-searchable | FE+BE |
| TC-FA-CF-654 | E2E | TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset | FE+BE |
| TC-FA-CF-655 | E2E | TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | FE+BE |
| TC-FA-CF-656 | E2E | TC-FA-CF-E2E-135-sinkron-asset-name-rename-linked-fields-dan-excess | FE+BE |
| TC-FA-CF-657 | E2E | TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | FE+BE |
| TC-FA-CF-658 | E2E | TC-FA-CF-E2E-138-form-registrasi-required-non-retroaktif-header-kolom-dan-input | FE+BE |
| TC-FA-CF-659 | E2E | TC-FA-CF-E2E-133-absence-log-request-ditolak-server-dan-suspended | FE+BE |
| TC-FA-CF-660 | E2E | TC-FA-CF-E2E-155-konflik-record-dihapus-aktor-lain | FE+BE |
| TC-FA-CF-661 | E2E | TC-FA-CF-E2E-154-plan-gating-happy-path-semua-tier | FE+BE |
| TC-FA-CF-662 | E2E | TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | FE+BE |
| TC-FA-CF-663 | E2E | TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali | FE+BE |
| TC-FA-CF-664 | E2E | TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali | FE+BE |
| TC-FA-CF-665 | E2E | TC-FA-CF-E2E-179-absence-log-request-ditolak-grace-period-dan-create-gagal-5xx | FE+BE |
| TC-FA-CF-666 | E2E | TC-FA-CF-E2E-179-absence-log-request-ditolak-grace-period-dan-create-gagal-5xx | FE+BE |
| TC-FA-CF-667 | E2E | TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | FE+BE |
| TC-FA-CF-668 | E2E | TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali | FE+BE |
| TC-FA-CF-669 | E2E | TC-FA-CF-E2E-146-grace-period-fa7-search-changelog-download-dan-lisensi-kembali | FE+BE |
| TC-FA-CF-670 | E2E | TC-FA-CF-E2E-180-grace-period-fa7-berakhir-tab-accounting-terkunci-dan-field-tidak-tampil | FE+BE |
| TC-FA-CF-671 | E2E | TC-FA-CF-E2E-174-filter-chip-opsi-terpilih-diringkas-menjadi-n-more | FE+BE |
| TC-FA-CF-672 | E2E | TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | FE+BE |
| TC-FA-CF-673 | E2E | TC-FA-CF-E2E-147-request-langsung-accounting-403-saat-fa7-tidak-aktif-dan-grace | FE+BE |
| TC-FA-CF-674 | E2E | TC-FA-CF-E2E-145-grace-period-fa7-tab-accounting-read-only-dan-aset | FE+BE |
| TC-FA-CF-675 | E2E | TC-FA-CF-E2E-144-lisensi-fa7-lapse-tab-accounting-dan-form-aset | FE+BE |
