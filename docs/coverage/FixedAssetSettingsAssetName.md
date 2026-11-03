# Coverage E2E — Fixed Asset > Settings > Asset Master > Asset Name

Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md` (843 TC granular aktif); tidak ada `tc-settings-asset-name-backend.md`, jadi tidak ada TC hanya-BE.
Suite: `specs/FixedAsset/SettingsAssetName/`.
Prefix Modul: `FA` + `FAAM` (`TC-FA-FAAM-E2E-*`).
Status semua spec: `draft`.

Catatan pemetaan: TC-FA-FAAM-611 sampai TC-FA-FAAM-614 sengaja dipetakan ke dua spec, yaitu spec 231 (request langsung tanpa hak ditolak server, sisi presence: pengamat UI memastikan data tidak berubah) dan spec 247 (pencatatan log: sisi absence, tidak ada entri Changelog, System Log, dan Activity Log untuk request yang ditolak). Pemisahan presence/absence mengikuti S-05; kedua pemetaan dipertahankan dan tiap spec memverifikasi sisi yang berbeda.

---

## 1. Pemetaan TC Granular → Spec E2E (254 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | Screening Tab Asset Name: 3 Zona, Breadcrumb, Navigasi Masuk, dan Urutan Default | FE+BE | 33 | TC-FA-FAAM-1, TC-FA-FAAM-2, TC-FA-FAAM-3, TC-FA-FAAM-4, TC-FA-FAAM-5, TC-FA-FAAM-36 |
| TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman | Retensi State Search, Sort, Filter, dan Halaman (Pindah Tab, F5, Sidebar, Popup Detail) | FE+BE | 30 | TC-FA-FAAM-6, TC-FA-FAAM-7, TC-FA-FAAM-8, TC-FA-FAAM-9 |
| TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | Format Sel Kolom Skalar, Header Tanpa Wrap, Hover Nama, dan Menu Aksi Baris | FE+BE | 34 | TC-FA-FAAM-10, TC-FA-FAAM-11, TC-FA-FAAM-12, TC-FA-FAAM-13, TC-FA-FAAM-14, TC-FA-FAAM-15, TC-FA-FAAM-16, TC-FA-FAAM-17, TC-FA-FAAM-26, TC-FA-FAAM-29, TC-FA-FAAM-30, TC-FA-FAAM-31 |
| TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | Sel Multi-Nilai: Strip, Satu Badge, Dua Badge, +N more, dan Lima Icon TAG Type | FE+BE | 24 | TC-FA-FAAM-18, TC-FA-FAAM-19, TC-FA-FAAM-20, TC-FA-FAAM-21, TC-FA-FAAM-22 |
| TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update | Teks Panjang Tanpa Potongan, Truncation Badge 25 Karakter, dan Badge Needs Update | FE+BE | 26 | TC-FA-FAAM-23, TC-FA-FAAM-24, TC-FA-FAAM-25, TC-FA-FAAM-28 |
| TC-FA-FAAM-E2E-006-empty-state-no-results-dan-skeleton-loader | Empty State Katalog Kosong, Search Tanpa Hasil, dan Skeleton Loader | FE+BE | 17 | TC-FA-FAAM-32, TC-FA-FAAM-33, TC-FA-FAAM-34 |
| TC-FA-FAAM-E2E-007-propagasi-perubahan-sesi-lain-ke-list-dan-modal | Propagasi Perubahan Sesi Lain: List Auto-Refresh dan Modal Terbuka Tidak Berubah | FE+BE | 29 | TC-FA-FAAM-37, TC-FA-FAAM-38, TC-FA-FAAM-643 |
| TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Tab Asset Name per Role | FE+BE | 89 | TC-FA-FAAM-44, TC-FA-FAAM-45, TC-FA-FAAM-46, TC-FA-FAAM-47, TC-FA-FAAM-48, TC-FA-FAAM-49, TC-FA-FAAM-50 |
| TC-FA-FAAM-E2E-009-role-matrix-negatif-tanpa-role-dan-hak-dicabut | Role Matrix Negatif: Tanpa Role Ini dan Hak Dicabut Saat Modal Terbuka | FE+BE | 20 | TC-FA-FAAM-51, TC-FA-FAAM-617, TC-FA-FAAM-618 |
| TC-FA-FAAM-E2E-010-role-matrix-positif-create-only | Role Matrix Positif Create-Only: Create Sampai Sukses, Tombol [➕] Default Label, dan Sumber Dropdown | FE+BE | 24 | TC-FA-FAAM-52, TC-FA-FAAM-60, TC-FA-FAAM-63 |
| TC-FA-FAAM-E2E-011-role-matrix-positif-update-only-edit | Role Matrix Positif Update-Only: Edit Sampai Sukses dan Edit Category Locked | FE+BE | 11 | TC-FA-FAAM-53, TC-FA-FAAM-59 |
| TC-FA-FAAM-E2E-012-role-matrix-tombol-default-label-di-modal-edit | Role Matrix: Tombol [➕] Default Label di Modal Edit (Update-Only Hidden, Total Control Tampil) | FE+BE | 11 | TC-FA-FAAM-61, TC-FA-FAAM-62 |
| TC-FA-FAAM-E2E-013-role-matrix-positif-delete-only | Role Matrix Positif Delete-Only: Dialog Blok In-Use, Delete, dan Bulk Delete | FE+BE | 17 | TC-FA-FAAM-54, TC-FA-FAAM-55, TC-FA-FAAM-57 |
| TC-FA-FAAM-E2E-014-role-matrix-hak-gabungan-baca-dan-import-data | Role Matrix: Hak Gabungan Create-Delete, Hak Baca Permission Read, dan Import Data | FE+BE | 18 | TC-FA-FAAM-56, TC-FA-FAAM-64, TC-FA-FAAM-65 |
| TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | Asset Name Excess: Badge Over Plan Limit, Aksi Edit Hidden, Bulk Delete, dan Urutan Excess | FE+BE | 35 | TC-FA-FAAM-27, TC-FA-FAAM-58, TC-FA-FAAM-296, TC-FA-FAAM-311, TC-FA-FAAM-646, TC-FA-FAAM-705, TC-FA-FAAM-730 |
| TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | Asset Name Excess: Pelepasan Status, Delete, dan Blok In-Use pada Salinan Client Downgrade | FE+BE | 33 | TC-FA-FAAM-237, TC-FA-FAAM-272, TC-FA-FAAM-273, TC-FA-FAAM-686, TC-FA-FAAM-729 |
| TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog | Resilience Baca: Error Load List, Popup Detail, Changelog, dan Baca Setelah Tulis | FE+BE | 31 | TC-FA-FAAM-35, TC-FA-FAAM-314, TC-FA-FAAM-468, TC-FA-FAAM-644 |
| TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | Mobile: Card List, Bottom Sheet Detail, Toolbar, Truncation Badge, Tooltip Tap, dan Notice | FE+BE | 35 | TC-FA-FAAM-39, TC-FA-FAAM-40, TC-FA-FAAM-41, TC-FA-FAAM-42, TC-FA-FAAM-43, TC-FA-FAAM-706 |
| TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | Mobile: Long Press, Select All Card, Mode Seleksi, dan Dialog Delete | FE+BE | 34 | TC-FA-FAAM-297, TC-FA-FAAM-298, TC-FA-FAAM-299, TC-FA-FAAM-300, TC-FA-FAAM-301 |
| TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail | Mobile: Form Create-Edit Satu Kolom, Tree Picker, Changelog, dan Tabel Detail Bottom Sheet | FE+BE | 24 | TC-FA-FAAM-317, TC-FA-FAAM-328, TC-FA-FAAM-737, TC-FA-FAAM-738 |
| TC-FA-FAAM-E2E-021-excess-create-diblokir-sampai-jumlah-di-bawah-cap | Asset Name Excess: Create Baru Diblokir Selama Jumlah Sama dengan atau di Atas Cap, Diterima Setelah Jumlah di Bawah Cap | FE+BE | 19 | TC-FA-FAAM-645 |
| TC-FA-FAAM-E2E-022-resilience-baca-progres-kepatuhan-tag-type-popup-detail | Resilience Baca: Baris Progres Kepatuhan TAG Type Tidak Tampil Sebagian Saat Popup Detail Loading atau Gagal Dimuat | FE+BE | 17 | TC-FA-FAAM-837 |
| TC-FA-FAAM-E2E-023-create-screening-popup-aksesibilitas-dan-checkbox-stay | Create: Screening Popup 3 Zona, Aksesibilitas, dan Checkbox Stay Hanya di Mode Create | FE+BE | 27 | TC-FA-FAAM-66, TC-FA-FAAM-67, TC-FA-FAAM-153 |
| TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | Create: Error Required Tiap Field Wajib dan Submit Semua Field Kosong | FE+BE | 15 | TC-FA-FAAM-81, TC-FA-FAAM-101, TC-FA-FAAM-106, TC-FA-FAAM-127, TC-FA-FAAM-139, TC-FA-FAAM-142 |
| TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | Create: Validasi Asset Name (Spasi, Batas 120, Spasi Ujung, Emoji, Karakter Lain) | FE+BE | 24 | TC-FA-FAAM-82, TC-FA-FAAM-83, TC-FA-FAAM-84, TC-FA-FAAM-85, TC-FA-FAAM-91, TC-FA-FAAM-93 |
| TC-FA-FAAM-E2E-026-create-validasi-asset-name-duplikat-dan-debounce | Create: Validasi Asset Name Duplikat (Saat Mengetik, Beda Huruf Besar-Kecil, Debounce 500 ms) | FE+BE | 17 | TC-FA-FAAM-87, TC-FA-FAAM-88, TC-FA-FAAM-89 |
| TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | Create: Validasi Code (Batas 15, Format, Kapital Otomatis, Duplikat, Helper Text) | FE+BE | 18 | TC-FA-FAAM-94, TC-FA-FAAM-95, TC-FA-FAAM-96, TC-FA-FAAM-97, TC-FA-FAAM-98, TC-FA-FAAM-99 |
| TC-FA-FAAM-E2E-028-create-category-tree-picker-stale-dan-internal | Create: Pilih Category Leaf, Category Dihapus Sesi Lain, dan Berubah Menjadi Internal | FE+BE | 22 | TC-FA-FAAM-102, TC-FA-FAAM-103, TC-FA-FAAM-104 |
| TC-FA-FAAM-E2E-029-create-tag-type-opsi-dan-mutual-exclusion | Create: Opsi TAG Type dan Pilihan Non-TAG Saling Menggantikan | FE+BE | 14 | TC-FA-FAAM-107, TC-FA-FAAM-108, TC-FA-FAAM-109 |
| TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | Create: Chip TAG Type, Search Dropdown, dan Default Addon (Opsi, Disabled Non-TAG, Terkunci) | FE+BE | 26 | TC-FA-FAAM-114, TC-FA-FAAM-115, TC-FA-FAAM-116, TC-FA-FAAM-117, TC-FA-FAAM-118, TC-FA-FAAM-119 |
| TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | Create: Default Label, Tombol [➕], Modal Create Label, dan Label Dihapus Sesi Lain | FE+BE | 29 | TC-FA-FAAM-122, TC-FA-FAAM-123, TC-FA-FAAM-124, TC-FA-FAAM-125, TC-FA-FAAM-126 |
| TC-FA-FAAM-E2E-032-create-brand-tabel-model-per-brand | Create: Pilih Brand, Tabel Model/Type per Brand, Deselect, dan Brand Dihapus Sesi Lain | FE+BE | 21 | TC-FA-FAAM-128, TC-FA-FAAM-129, TC-FA-FAAM-130 |
| TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | Create: Input Model (Enter, Batas 120, Nama Sama Beda Brand, Emoji, Hapus Badge) | FE+BE | 22 | TC-FA-FAAM-131, TC-FA-FAAM-132, TC-FA-FAAM-134, TC-FA-FAAM-136, TC-FA-FAAM-138 |
| TC-FA-FAAM-E2E-034-create-model-duplikat-dan-no-model-default | Create: Model Duplikat dalam Brand dan Badge Default No Model | FE+BE | 29 | TC-FA-FAAM-133, TC-FA-FAAM-135 |
| TC-FA-FAAM-E2E-035-create-uom-opsi-dan-dihapus-sesi-lain | Create: Opsi UoM Single-Select dan UoM Dihapus Sesi Lain | FE+BE | 16 | TC-FA-FAAM-140, TC-FA-FAAM-141 |
| TC-FA-FAAM-E2E-036-create-clear-field-dan-error-inline | Create: Clear Field Mengosongkan Semua Field dan Menghapus Error Inline | FE+BE | 20 | TC-FA-FAAM-69, TC-FA-FAAM-70 |
| TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | Create: Penutupan Form Bersih dan Terisi, Dialog Unsaved Changes, Leave, Cancel, dan Esc | FE+BE | 29 | TC-FA-FAAM-71, TC-FA-FAAM-72, TC-FA-FAAM-73, TC-FA-FAAM-74, TC-FA-FAAM-75 |
| TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | Create: Backdrop, Field Dikembalikan, Reload F5, Navigasi Sidebar, dan Esc pada Tree Picker | FE+BE | 29 | TC-FA-FAAM-76, TC-FA-FAAM-77, TC-FA-FAAM-78, TC-FA-FAAM-79, TC-FA-FAAM-80 |
| TC-FA-FAAM-E2E-039-create-sukses-hanya-field-wajib | Create Sukses: Hanya Field Wajib dengan Code Auto-Generate | FE+BE | 22 | TC-FA-FAAM-143 |
| TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label | Create Sukses: Code Manual versus Auto, Trim Nama, dan Default Addon | FE+BE | 28 | TC-FA-FAAM-86, TC-FA-FAAM-100, TC-FA-FAAM-145, TC-FA-FAAM-146 |
| TC-FA-FAAM-E2E-041-create-sukses-dua-brand-dan-model | Create Sukses: Default Label Terisi dan Dua Brand dengan Model Berbeda | FE+BE | 18 | TC-FA-FAAM-147, TC-FA-FAAM-149 |
| TC-FA-FAAM-E2E-042-create-stay-on-this-form-reset-tutup-dan-nama-sama | Create: Stay on this Form Tercentang dan Tidak, serta Dua Create Nama Sama | FE+BE | 24 | TC-FA-FAAM-150, TC-FA-FAAM-151, TC-FA-FAAM-152 |
| TC-FA-FAAM-E2E-043-create-saving-state-dan-klik-ganda-submit | Create: Saving State Tombol Submit dan Klik Ganda Cepat Hanya Satu Record | FE+BE | 20 | TC-FA-FAAM-68, TC-FA-FAAM-167 |
| TC-FA-FAAM-E2E-044-create-changelog-create-dan-nama-sama-di-client-lain | Create: Entri Create di Changelog dan Asset Name Sama di Client Lain | FE+BE | 19 | TC-FA-FAAM-90, TC-FA-FAAM-169 |
| TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci | Create: Gating Plan (TAG Type Terkunci Starter, Paid, Paket Diturunkan) dan Satu di Bawah Kuota | FE+BE | 26 | TC-FA-FAAM-110, TC-FA-FAAM-111, TC-FA-FAAM-113, TC-FA-FAAM-155 |
| TC-FA-FAAM-E2E-046-create-kuota-paket-starter-dialog-dan-cta-upgrade | Create: Dialog Kuota Paket Starter, OK Mempertahankan Input, dan CTA Upgrade | FE+BE | 16 | TC-FA-FAAM-154, TC-FA-FAAM-156, TC-FA-FAAM-157 |
| TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | Create: Ceiling Master Data Count Limit pada Klik Tombol (D-07), Enterprise, dan Label Limit | FE+BE | 31 | TC-FA-FAAM-158, TC-FA-FAAM-160, TC-FA-FAAM-677, TC-FA-FAAM-719, TC-FA-FAAM-749 |
| TC-FA-FAAM-E2E-048-create-ceiling-satu-di-bawah-race-dan-per-katalog | Create: Ceiling Satu di Bawah (Race Tombol-Submit D-07 dan Penghitungan Per Katalog) | FE+BE | 23 | TC-FA-FAAM-159, TC-FA-FAAM-676 |
| TC-FA-FAAM-E2E-049-create-ceiling-model-type-d08-dan-no-model | Create: Ceiling Model/Type (D-08), No Model Dihitung, dan Edit di Ceiling | FE+BE | 35 | TC-FA-FAAM-161, TC-FA-FAAM-162, TC-FA-FAAM-164 |
| TC-FA-FAAM-E2E-050-create-rate-limit-cek-keunikan-429 | Create: Cek Keunikan Ditolak Batas Laju (429) pada Asset Name, Code, dan Nama Model | FE+BE | 23 | TC-FA-FAAM-683, TC-FA-FAAM-725, TC-FA-FAAM-726 |
| TC-FA-FAAM-E2E-051-resilience-create-5xx-timeout-dan-tabrakan-code | Resilience Create: Gagal 5xx, Timeout, dan Tabrakan Code Generator | FE+BE | 25 | TC-FA-FAAM-165, TC-FA-FAAM-166, TC-FA-FAAM-168 |
| TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | Defense-in-Depth Create: Request Langsung Category Excess, Opsi Terkunci, Addon, dan Emoji | FE+BE | 27 | TC-FA-FAAM-92, TC-FA-FAAM-105, TC-FA-FAAM-112, TC-FA-FAAM-120, TC-FA-FAAM-121, TC-FA-FAAM-137 |
| TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka | Generator Code: Dua Kata, Pemisah, Token Angka, dan Token Campuran | FE+BE | 8 | TC-FA-FAAM-329, TC-FA-FAAM-330, TC-FA-FAAM-331, TC-FA-FAAM-332 |
| TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | Generator Code: Fallback 6 Karakter dan AN, Suffix Sekuensial, Batas 15, dan Atomik dengan Penyimpanan | FE+BE | 16 | TC-FA-FAAM-333, TC-FA-FAAM-334, TC-FA-FAAM-335, TC-FA-FAAM-336, TC-FA-FAAM-337, TC-FA-FAAM-342 |
| TC-FA-FAAM-E2E-055-generator-code-pada-edit | Generator Code pada Edit: Code Dikosongkan, Nama Akhir, dan Cek Keunikan Mengecualikan Diri | FE+BE | 35 | TC-FA-FAAM-338, TC-FA-FAAM-339, TC-FA-FAAM-340, TC-FA-FAAM-341 |
| TC-FA-FAAM-E2E-056-create-ceiling-stay-hingga-ceiling | Create: Ceiling dengan Stay Aktif, Data ke-N Sukses dan ke-N+1 Ditolak (D-07) | FE+BE | 19 | TC-FA-FAAM-163 |
| TC-FA-FAAM-E2E-057-create-sukses-seluruh-field-opsional-dan-non-tag | Create Sukses: Seluruh Field Opsional Terisi dan TAG Type Non-TAG | FE+BE | 25 | TC-FA-FAAM-144, TC-FA-FAAM-148 |
| TC-FA-FAAM-E2E-058-edit-screening-clear-field-dan-aksesibilitas | Edit: Screening Popup Nilai Tersimpan, Clear Field Bukan Revert, dan Aksesibilitas | FE+BE | 36 | TC-FA-FAAM-170, TC-FA-FAAM-171, TC-FA-FAAM-172 |
| TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | Edit: Tutup Tanpa Perubahan, Unsaved Changes, Leave, Cancel, dan Esc pada Dialog | FE+BE | 30 | TC-FA-FAAM-174, TC-FA-FAAM-175, TC-FA-FAAM-176, TC-FA-FAAM-670, TC-FA-FAAM-671 |
| TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | Edit: Backdrop, Nilai Dikembalikan, Esc, Reload F5, Sidebar, dan Esc pada Tree Picker | FE+BE | 30 | TC-FA-FAAM-177, TC-FA-FAAM-178, TC-FA-FAAM-179, TC-FA-FAAM-180, TC-FA-FAAM-181, TC-FA-FAAM-742 |
| TC-FA-FAAM-E2E-061-edit-validasi-asset-name | Edit: Validasi Asset Name (Required, Batas 120, Trim, Duplikat, Nama Sendiri, Emoji) | FE+BE | 35 | TC-FA-FAAM-182, TC-FA-FAAM-183, TC-FA-FAAM-184, TC-FA-FAAM-185, TC-FA-FAAM-186, TC-FA-FAAM-187, TC-FA-FAAM-188 |
| TC-FA-FAAM-E2E-062-edit-validasi-code | Edit: Validasi Code (Batas 15, Karakter Tidak Valid, Duplikat, Kapitalisasi Sendiri) | FE+BE | 19 | TC-FA-FAAM-190, TC-FA-FAAM-191, TC-FA-FAAM-192, TC-FA-FAAM-193, TC-FA-FAAM-194 |
| TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal | Edit: Ganti Category, Category Dikosongkan, Dihapus Sesi Lain, dan Berubah Menjadi Internal | FE+BE | 34 | TC-FA-FAAM-195, TC-FA-FAAM-196, TC-FA-FAAM-197, TC-FA-FAAM-198 |
| TC-FA-FAAM-E2E-064-edit-category-locked-field-lain-dan-lepas-kunci | Edit Category Locked: Field Lain Tidak Memeriksa Ulang dan Category Leaf Baru Melepas Kunci | FE+BE | 17 | TC-FA-FAAM-199, TC-FA-FAAM-200 |
| TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset | Edit TAG Type Tanpa Aset: Kosong, Non-TAG, Mutual Exclusion, dan Penggantian Tipe | FE+BE | 27 | TC-FA-FAAM-201, TC-FA-FAAM-202, TC-FA-FAAM-203, TC-FA-FAAM-204 |
| TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | Edit: Brand dan UoM Dikosongkan serta Label, Brand, dan UoM Dihapus Sesi Lain | FE+BE | 39 | TC-FA-FAAM-211, TC-FA-FAAM-212, TC-FA-FAAM-213, TC-FA-FAAM-220, TC-FA-FAAM-221 |
| TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi | Edit: Validasi Nama Model (Duplikat, Batas 120, Emoji, Kapitalisasi Beda) | FE+BE | 22 | TC-FA-FAAM-215, TC-FA-FAAM-216, TC-FA-FAAM-217, TC-FA-FAAM-733 |
| TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model | Edit: Brand Baru, No Model Disisipkan, Hapus Badge Model, dan No Model Menjadi Model Nyata | FE+BE | 40 | TC-FA-FAAM-214, TC-FA-FAAM-218, TC-FA-FAAM-219, TC-FA-FAAM-746 |
| TC-FA-FAAM-E2E-069-edit-uom-dan-addon-grandfather-lisensi | Edit: Ganti UoM dan Addon Tersimpan Tanpa Lisensi Aktif (Grandfather) | FE+BE | 19 | TC-FA-FAAM-208, TC-FA-FAAM-222 |
| TC-FA-FAAM-E2E-070-edit-sukses-multi-field-dan-isolasi-field-lain | Edit Sukses: Beberapa Field Sekaligus, Satu Field Tidak Mengubah Field Lain, dan Submit Penuh | FE+BE | 32 | TC-FA-FAAM-227, TC-FA-FAAM-228, TC-FA-FAAM-229 |
| TC-FA-FAAM-E2E-071-edit-saving-state-klik-ganda-dan-save-tanpa-perubahan | Edit: Saving State Tombol Save, Klik Ganda Save, dan Save Tanpa Perubahan No-Op | FE+BE | 30 | TC-FA-FAAM-173, TC-FA-FAAM-223, TC-FA-FAAM-233 |
| TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus | Edit: No-Op Spasi Tepi, Code Dikosongkan, Kapitalisasi, dan Record Dihapus Pengguna Lain | FE+BE | 39 | TC-FA-FAAM-224, TC-FA-FAAM-225, TC-FA-FAAM-226, TC-FA-FAAM-230 |
| TC-FA-FAAM-E2E-073-edit-dialog-change-category | Edit Ber-Aset: Dialog Change Category (Jamak, Tunggal, Cancel, Save) | FE+BE | 34 | TC-FA-FAAM-238, TC-FA-FAAM-239, TC-FA-FAAM-240, TC-FA-FAAM-241 |
| TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil | Edit Ber-Aset: Dialog Change Default Label (Jamak, Tunggal, Klausa 0 Dihilangkan) | FE+BE | 29 | TC-FA-FAAM-242, TC-FA-FAAM-243, TC-FA-FAAM-681, TC-FA-FAAM-682 |
| TC-FA-FAAM-E2E-075-edit-dialog-change-default-label-save-dan-cancel | Edit Ber-Aset: Save Default Label Cascade dan Cancel Dialog Tunggal | FE+BE | 30 | TC-FA-FAAM-244, TC-FA-FAAM-744 |
| TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a | Edit Ber-Aset: Dialog Change Default Addon (Tambah, Hapus, Pengurangan Tanpa In Transaction, Tunggal) | FE+BE | 28 | TC-FA-FAAM-245, TC-FA-FAAM-246, TC-FA-FAAM-678, TC-FA-FAAM-679 |
| TC-FA-FAAM-E2E-077-edit-dialog-change-default-addon-tampil-b | Edit Ber-Aset: Dialog Change Default Addon (Pengurangan Tunggal, Pending Quota, Unenrolled) | FE+BE | 29 | TC-FA-FAAM-680, TC-FA-FAAM-720, TC-FA-FAAM-721 |
| TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save | Edit Ber-Aset: Save Default Addon (Enroll, Pending Quota dan Tag, Excluded, Draft, Pending Removal) | FE+BE | 44 | TC-FA-FAAM-247, TC-FA-FAAM-248, TC-FA-FAAM-249, TC-FA-FAAM-250 |
| TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil | Edit Ber-Aset: Dialog D-10 Tidak Tampil dan Judul Removing Tanpa Klausa | FE+BE | 43 | TC-FA-FAAM-707, TC-FA-FAAM-708, TC-FA-FAAM-709, TC-FA-FAAM-710 |
| TC-FA-FAAM-E2E-080-edit-dialog-default-addon-cancel-dan-hitungan-berubah | Edit Ber-Aset: Cancel Dialog Default Addon Tunggal dan Hitungan Berubah Sebelum Save | FE+BE | 36 | TC-FA-FAAM-728, TC-FA-FAAM-743 |
| TC-FA-FAAM-E2E-081-edit-dialog-berurutan-category-addon-label | Edit Ber-Aset: Dialog Dampak Berurutan, Cancel Dialog Ketiga, dan Total Asset Berubah | FE+BE | 40 | TC-FA-FAAM-251, TC-FA-FAAM-252, TC-FA-FAAM-253 |
| TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan | Edit Ber-Aset: Dialog Change TAG Type Konfirmasi Saja, Tanpa Input Tanggal, dan Field Lain | FE+BE | 22 | TC-FA-FAAM-647, TC-FA-FAAM-648, TC-FA-FAAM-652, TC-FA-FAAM-653 |
| TC-FA-FAAM-E2E-083-edit-dialog-change-tag-type-cancel-esc-dan-non-tag | Edit Ber-Aset: Cancel, Esc, dan Backdrop Dialog Change TAG Type serta Non-TAG Tanpa Addon | FE+BE | 30 | TC-FA-FAAM-650, TC-FA-FAAM-651, TC-FA-FAAM-655 |
| TC-FA-FAAM-E2E-084-edit-dialog-dampak-hanya-field-berubah-dan-cancel-berantai | Edit Ber-Aset: Dialog Hanya Field Berubah dan Cancel Setelah Category | FE+BE | 27 | TC-FA-FAAM-657, TC-FA-FAAM-658 |
| TC-FA-FAAM-E2E-085-edit-dialog-change-tag-type-save-dan-aset-baru | Edit Ber-Aset: Save Change TAG Type Satu Baris Log dan Aset Baru Terdaftar Antar Dialog | FE+BE | 23 | TC-FA-FAAM-649, TC-FA-FAAM-659 |
| TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | Edit: Blok Hapus Model dan Brand In-Use (Tooltip, Dialog Tunggal dan Jamak) serta Brand Bebas Dilepas | FE+BE | 36 | TC-FA-FAAM-254, TC-FA-FAAM-255, TC-FA-FAAM-256, TC-FA-FAAM-257, TC-FA-FAAM-258, TC-FA-FAAM-259 |
| TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type | Resilience Edit: Gagal 5xx, Timeout, Tabrakan Code, dan Save TAG Type Gagal | FE+BE | 47 | TC-FA-FAAM-231, TC-FA-FAAM-232, TC-FA-FAAM-234, TC-FA-FAAM-660 |
| TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | Defense-in-Depth Edit: Request Langsung Emoji, Addon, Melepas Model In-Use | FE+BE | 33 | TC-FA-FAAM-189, TC-FA-FAAM-209, TC-FA-FAAM-210, TC-FA-FAAM-260, TC-FA-FAAM-684 |
| TC-FA-FAAM-E2E-089-defense-in-depth-edit-request-langsung-plan-dan-excess | Defense-in-Depth Edit: Request Langsung Opsi TAG Terkunci dan Asset Name Excess | FE+BE | 0 | TC-FA-FAAM-207, TC-FA-FAAM-236 |
| TC-FA-FAAM-E2E-090-edit-dialog-dampak-non-tag-dan-empat-dialog-berurutan | Edit Ber-Aset: Non-TAG Memicu Dialog TAG Type lalu Default Addon dan Empat Dialog Berurutan | FE+BE | 29 | TC-FA-FAAM-654, TC-FA-FAAM-656 |
| TC-FA-FAAM-E2E-091-edit-tag-type-grandfather-chip-terkunci-client-starter | Edit TAG Type Grandfather: Chip Terkunci Tetap Tampil, Dapat Dilepas, dan Tidak Dapat Dipilih Lagi | FE+BE | 15 | TC-FA-FAAM-205, TC-FA-FAAM-206 |
| TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | Delete Single: Dialog Konfirmasi, Cancel, dan Dialog Blok In-Use (Jamak, Tunggal, Aset Draft dan Waiting for Approval) | FE+BE | 27 | TC-FA-FAAM-261, TC-FA-FAAM-263, TC-FA-FAAM-264, TC-FA-FAAM-265, TC-FA-FAAM-266 |
| TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope | Delete Single: Konfirmasi Menghapus, Aset Deleted dan Disposed, Klik Ganda, dan Scope Custom Field | FE+BE | 35 | TC-FA-FAAM-262, TC-FA-FAAM-267, TC-FA-FAAM-271, TC-FA-FAAM-275 |
| TC-FA-FAAM-E2E-094-delete-single-race-dan-record-sudah-terhapus-single-dan-bulk | Delete: Aset Baru Antar Dialog dan Konfirmasi, serta Record Sudah Terhapus oleh Sesi Lain (Single dan Bulk) | FE+BE | 29 | TC-FA-FAAM-268, TC-FA-FAAM-269, TC-FA-FAAM-290 |
| TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header | Bulk Action Bar: Screening, Counter, Checkbox Header, dan Cancel Dialog Tidak Mereset Seleksi | FE+BE | 31 | TC-FA-FAAM-276, TC-FA-FAAM-277, TC-FA-FAAM-278, TC-FA-FAAM-294 |
| TC-FA-FAAM-E2E-096-bulk-seleksi-lintas-halaman-select-all-dan-retensi | Bulk: Select All Lintas Halaman, Uncheck Satu Baris, dan Seleksi Bertahan | FE+BE | 26 | TC-FA-FAAM-279, TC-FA-FAAM-280, TC-FA-FAAM-295 |
| TC-FA-FAAM-E2E-097-bulk-selection-limit-live-block-dan-auto-cap | Bulk: Selection Limit Live-Block dan Auto-Cap Select All | FE+BE | 18 | TC-FA-FAAM-281, TC-FA-FAAM-282 |
| TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | Bulk Delete: Dialog Homogen, Campuran, Blok Semua In-Use, Seleksi Satu Baris, dan Cancel | FE+BE | 37 | TC-FA-FAAM-283, TC-FA-FAAM-285, TC-FA-FAAM-287, TC-FA-FAAM-288, TC-FA-FAAM-289, TC-FA-FAAM-672 |
| TC-FA-FAAM-E2E-099-bulk-delete-sukses-homogen-continue-dan-klik-ganda | Bulk Delete: Konfirmasi Homogen, Continue Campuran, dan Klik Ganda Menghapus Sekali | FE+BE | 35 | TC-FA-FAAM-284, TC-FA-FAAM-286, TC-FA-FAAM-673 |
| TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx | Resilience Delete: Gagal 5xx Single, Bulk Semua Gagal, Request Bulk Gagal, dan Bulk Sebagian Gagal | FE+BE | 37 | TC-FA-FAAM-270, TC-FA-FAAM-291, TC-FA-FAAM-292, TC-FA-FAAM-293 |
| TC-FA-FAAM-E2E-101-popup-detail-screening-buka-dan-tutup | Popup Detail: Screening, Buka dari Link dan Menu Aksi, dan Tutup Hanya Lewat [✕] | FE+BE | 19 | TC-FA-FAAM-302, TC-FA-FAAM-303, TC-FA-FAAM-304 |
| TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | Popup Detail: Tab Models per Brand, Linked Custom Fields, Empty State, dan Badge Status | FE+BE | 32 | TC-FA-FAAM-305, TC-FA-FAAM-306, TC-FA-FAAM-307, TC-FA-FAAM-312, TC-FA-FAAM-313 |
| TC-FA-FAAM-E2E-103-popup-detail-tautan-lintas-modul-dan-group-scope | Popup Detail: Tautan Lintas Modul, Hidden Tanpa Akses, dan Daftar Client-Wide pada Group Scope Terbatas | FE+BE | 25 | TC-FA-FAAM-308, TC-FA-FAAM-309, TC-FA-FAAM-310 |
| TC-FA-FAAM-E2E-104-popup-detail-retensi-state-tab-total-assets | Popup Detail: Pindah Tab Memulihkan State Tab Total Assets dan Buka Ulang Mereset | FE+BE | 31 | TC-FA-FAAM-315, TC-FA-FAAM-316 |
| TC-FA-FAAM-E2E-105-popup-detail-progres-kepatuhan-tag-type-format-dan-bentuk-tunggal | Popup Detail: Progres Kepatuhan TAG Type, Format Baris, Read-Only, Modal Edit Tanpa Progres, dan Bentuk Tunggal | FE+BE | 25 | TC-FA-FAAM-830, TC-FA-FAAM-832 |
| TC-FA-FAAM-E2E-106-popup-detail-progres-kepatuhan-per-role-dan-scope | Role Matrix: Progres Kepatuhan TAG Type Client-Wide pada Group Manager, Read Only, dan Permission Read | FE+BE | 20 | TC-FA-FAAM-831, TC-FA-FAAM-834 |
| TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | Tree Picker: Screening, Hanya Leaf Dipilih, Node Excess, dan Search | FE+BE | 27 | TC-FA-FAAM-318, TC-FA-FAAM-319, TC-FA-FAAM-320, TC-FA-FAAM-321, TC-FA-FAAM-322 |
| TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | Tree Picker: Cancel, Select, Urutan A-Z, Mulai dari Pilihan Tersimpan, dan Client Tanpa Kategori | FE+BE | 33 | TC-FA-FAAM-323, TC-FA-FAAM-324, TC-FA-FAAM-325, TC-FA-FAAM-326, TC-FA-FAAM-327 |
| TC-FA-FAAM-E2E-109-popup-detail-progres-kepatuhan-tag-type-tidak-tampil-dua-tipe-dan-non-tag | Popup Detail: Progres Kepatuhan TAG Type Tidak Tampil, Dua Tipe Wajib, dan Asset Name Non-TAG | FE+BE | 24 | TC-FA-FAAM-833, TC-FA-FAAM-835, TC-FA-FAAM-836 |
| TC-FA-FAAM-E2E-110-delete-single-halaman-terakhir-pindah-ke-halaman-sebelumnya | Delete Single: Menghapus Baris Terakhir di Halaman Terakhir Pindah ke Halaman Terakhir yang Masih Ada | FE+BE | 5 | TC-FA-FAAM-274 |
| TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | Search: Reveal Box, Mengetik Belum Menyaring, Enter, Clear, Collapse, dan Trim | FE+BE | 33 | TC-FA-FAAM-352, TC-FA-FAAM-353, TC-FA-FAAM-354, TC-FA-FAAM-355, TC-FA-FAAM-356, TC-FA-FAAM-357 |
| TC-FA-FAAM-E2E-112-search-kelas-kolom-teks-category-dan-tag-type | Search: Kelas Kolom Asset Name, Code, UoM, Category, dan TAG Type | FE+BE | 14 | TC-FA-FAAM-343, TC-FA-FAAM-344, TC-FA-FAAM-345 |
| TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | Search: Brand, Model/Type, Default Addon, Default Label, Total Asset, Modified By, Tanpa Hasil, dan Kolom Tanggal | FE+BE | 25 | TC-FA-FAAM-346, TC-FA-FAAM-347, TC-FA-FAAM-348, TC-FA-FAAM-349, TC-FA-FAAM-350 |
| TC-FA-FAAM-E2E-114-search-kolom-hidden-karakter-khusus-dan-markup | Search: Kolom Hidden, Keyword Khusus Literal, dan Nilai Sel Markup sebagai Teks | FE+BE | 24 | TC-FA-FAAM-351, TC-FA-FAAM-358, TC-FA-FAAM-359 |
| TC-FA-FAAM-E2E-115-filter-screening-opsi-distinct-dan-kelas-category | Filter: Screening Panel, Opsi DISTINCT Brand UoM Modified By, dan Kelas Category | FE+BE | 28 | TC-FA-FAAM-360, TC-FA-FAAM-361, TC-FA-FAAM-362 |
| TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | Filter: Kelas TAG Type, Default Addon, Default Label, Total Asset, dan Last Updated | FE+BE | 34 | TC-FA-FAAM-363, TC-FA-FAAM-364, TC-FA-FAAM-365, TC-FA-FAAM-366, TC-FA-FAAM-367 |
| TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | Filter: OR dalam Field dan AND Antar-Field, Chip, +N more, dan Search Dropdown | FE+BE | 33 | TC-FA-FAAM-368, TC-FA-FAAM-369, TC-FA-FAAM-370, TC-FA-FAAM-371, TC-FA-FAAM-372 |
| TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | Filter: Clear Field, Menutup Tanpa Apply, Indikator Titik, Baris Kosong, dan Reset Halaman | FE+BE | 35 | TC-FA-FAAM-375, TC-FA-FAAM-376, TC-FA-FAAM-377, TC-FA-FAAM-378, TC-FA-FAAM-379 |
| TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton | Filter: Opsi Dinamis (Client Kosong, Opsi Hilang, Brand Bertambah, Skeleton Dropdown) | FE+BE | 43 | TC-FA-FAAM-373, TC-FA-FAAM-374, TC-FA-FAAM-747, TC-FA-FAAM-748 |
| TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | Kombinasi Search, Filter, Sort, dan Pagination (Irisan, Clear, Pindah Sort) | FE+BE | 33 | TC-FA-FAAM-380, TC-FA-FAAM-381, TC-FA-FAAM-382, TC-FA-FAAM-383, TC-FA-FAAM-384 |
| TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data | Kombinasi: Tanpa Hasil Pulih, Seleksi Bertahan, serta Create dan Edit yang Tidak Cocok Filter | FE+BE | 31 | TC-FA-FAAM-385, TC-FA-FAAM-386, TC-FA-FAAM-387, TC-FA-FAAM-388 |
| TC-FA-FAAM-E2E-122-sort-kelas-teks-category-dan-tag-type | Sort: Siklus Tiga State Kelas Teks, Category, dan TAG Type | FE+BE | 18 | TC-FA-FAAM-389, TC-FA-FAAM-390, TC-FA-FAAM-391 |
| TC-FA-FAAM-E2E-123-sort-kelas-badge-addon-dan-total-asset | Sort: Kelas Brand, Model/Type, Default Label, Default Addon, dan Total Asset | FE+BE | 21 | TC-FA-FAAM-392, TC-FA-FAAM-393, TC-FA-FAAM-394 |
| TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | Sort: Last Updated, Modified By, Kolom Tanpa Sort, Urutan Badge, dan Tie-Breaker | FE+BE | 33 | TC-FA-FAAM-395, TC-FA-FAAM-396, TC-FA-FAAM-397, TC-FA-FAAM-398, TC-FA-FAAM-399, TC-FA-FAAM-400, TC-FA-FAAM-401 |
| TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset | Setup Column: Overlay Column Visibility, Popup, Reset to Default, Discard, dan Guard Pin | FE+BE | 31 | TC-FA-FAAM-402, TC-FA-FAAM-403, TC-FA-FAAM-426, TC-FA-FAAM-429 |
| TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category | Setup Column: Ceklis dan Geser Kelas Asset Name dan Category | FE+BE | 34 | TC-FA-FAAM-404, TC-FA-FAAM-405, TC-FA-FAAM-410, TC-FA-FAAM-411 |
| TC-FA-FAAM-E2E-127-setup-column-tag-type-ceklis-geser-dan-pin | Setup Column: Ceklis, Geser, dan Pin Kelas TAG Type | FE+BE | 28 | TC-FA-FAAM-413, TC-FA-FAAM-414, TC-FA-FAAM-415 |
| TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | Setup Column: Total Asset Geser dan Pin serta Last Updated | FE+BE | 46 | TC-FA-FAAM-420, TC-FA-FAAM-421, TC-FA-FAAM-422, TC-FA-FAAM-423, TC-FA-FAAM-424 |
| TC-FA-FAAM-E2E-129-setup-column-kelas-teks-ceklis-dan-geser | Setup Column: Kelas Code, UoM, Modified By (Ceklis dan Geser) | FE+BE | 19 | TC-FA-FAAM-407, TC-FA-FAAM-408 |
| TC-FA-FAAM-E2E-130-setup-column-kelas-teks-pin-dan-chip-ceklis | Setup Column: Kelas Teks Pin dan Kelas Chip +N more Ceklis | FE+BE | 27 | TC-FA-FAAM-409, TC-FA-FAAM-416 |
| TC-FA-FAAM-E2E-131-setup-column-kelas-chip-geser-dan-pin | Setup Column: Kelas Chip +N more Geser dan Pin | FE+BE | 38 | TC-FA-FAAM-417, TC-FA-FAAM-418 |
| TC-FA-FAAM-E2E-132-setup-column-independen-filter-bertahan-dan-viewport | Setup Column: Independen Antar Tabel, Filter Bertahan, dan Sel Satu Baris Saat Viewport Dipersempit | FE+BE | 26 | TC-FA-FAAM-430, TC-FA-FAAM-431, TC-FA-FAAM-669 |
| TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | Paginasi: Default 10, Page Size, Next-Prev, Nomor Halaman, dan Reset oleh Search-Filter | FE+BE | 23 | TC-FA-FAAM-432, TC-FA-FAAM-433, TC-FA-FAAM-434, TC-FA-FAAM-435, TC-FA-FAAM-436 |
| TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | Tooltip, Hover, dan Popover +N more Tabel Utama | FE+BE | 49 | TC-FA-FAAM-437, TC-FA-FAAM-438, TC-FA-FAAM-439, TC-FA-FAAM-440, TC-FA-FAAM-441, TC-FA-FAAM-442, TC-FA-FAAM-443, TC-FA-FAAM-444, TC-FA-FAAM-445 |
| TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | Notice Category Locked: Bentuk Jamak, Hitungan Seluruh Katalog, Show only these, Clear Filter, dan Chip | FE+BE | 41 | TC-FA-FAAM-687, TC-FA-FAAM-690, TC-FA-FAAM-691, TC-FA-FAAM-693, TC-FA-FAAM-694 |
| TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan | Notice Category Locked: Quick Filter AND dengan Search-Filter, Clear Terpisah, Seleksi, dan Urutan Elemen | FE+BE | 50 | TC-FA-FAAM-695, TC-FA-FAAM-696, TC-FA-FAAM-702, TC-FA-FAAM-724 |
| TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | Notice Category Locked: Retensi Pindah Tab, F5, Popup Detail, Sidebar, dan Hitungan Selama Loading | FE+BE | 31 | TC-FA-FAAM-697, TC-FA-FAAM-698, TC-FA-FAAM-699, TC-FA-FAAM-700, TC-FA-FAAM-732 |
| TC-FA-FAAM-E2E-138-notice-category-locked-bentuk-tunggal | Notice Category Locked: Bentuk Tunggal dan Show only this | FE+BE | 9 | TC-FA-FAAM-688, TC-FA-FAAM-692 |
| TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol | Notice Category Locked: Hitungan Menjadi 0 lewat Edit, Sesi Lain, atau Delete serta Hitungan 0 Sejak Awal | FE+BE | 30 | TC-FA-FAAM-689, TC-FA-FAAM-703, TC-FA-FAAM-704, TC-FA-FAAM-727 |
| TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | Download List: Isi Berkas Kelas Teks, Category, TAG Type, Brand, dan Default Addon-Label | FE+BE | 19 | TC-FA-FAAM-446, TC-FA-FAAM-447, TC-FA-FAAM-448, TC-FA-FAAM-449, TC-FA-FAAM-450 |
| TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | Download List: Isi Berkas Total Asset, Modified By, Last Updated, Nilai Kosong, BOM-Kutip CSV, dan Last Updated CSV Tab Total Assets | FE+BE | 32 | TC-FA-FAAM-451, TC-FA-FAAM-452, TC-FA-FAAM-453, TC-FA-FAAM-454, TC-FA-FAAM-460, TC-FA-FAAM-846 |
| TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | Download List: Cakupan Search-Filter, Kolom Hidden, Nama Berkas, Nol Baris, dan Quick Filter | FE+BE | 35 | TC-FA-FAAM-455, TC-FA-FAAM-456, TC-FA-FAAM-457, TC-FA-FAAM-459, TC-FA-FAAM-701 |
| TC-FA-FAAM-E2E-143-download-lebih-dari-5000-baris | Download List: Lebih dari 5.000 Baris Memakai Loading Screen | FE+BE | 5 | TC-FA-FAAM-461 |
| TC-FA-FAAM-E2E-144-resilience-download-gagal-list-changelog-total-assets | Resilience Download Gagal: Toast Error dengan Nama Berkas pada List, Changelog, dan Tab Total Assets | FE+BE | 19 | TC-FA-FAAM-458, TC-FA-FAAM-498, TC-FA-FAAM-524 |
| TC-FA-FAAM-E2E-145-setup-column-guard-satu-kolom-batas-pin-dan-reset-to-default | Setup Column: Guard Satu Kolom Tersisa, Batas Pin Tiga Kolom, dan Reset to Default | FE+BE | 20 | TC-FA-FAAM-425, TC-FA-FAAM-427, TC-FA-FAAM-428 |
| TC-FA-FAAM-E2E-146-setup-column-pin-asset-name-category-dan-total-asset-ceklis | Setup Column: Pin Kelas Asset Name dan Category serta Ceklis Total Asset | FE+BE | 32 | TC-FA-FAAM-406, TC-FA-FAAM-412, TC-FA-FAAM-419 |
| TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | Modal Changelog: Screening, Tutup Hanya [✕] atau Esc, Format Kolom, dan Empty State | FE+BE | 32 | TC-FA-FAAM-462, TC-FA-FAAM-463, TC-FA-FAAM-464, TC-FA-FAAM-465, TC-FA-FAAM-467 |
| TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | Modal Changelog: Search Kelas Kolom, Modified By Nama Lengkap, Tanpa Kolom Date, dan Kolom Hidden | FE+BE | 28 | TC-FA-FAAM-470, TC-FA-FAAM-471, TC-FA-FAAM-472, TC-FA-FAAM-473, TC-FA-FAAM-745 |
| TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | Modal Changelog: Filter Panel, Date Range Inklusif, Dropdown DISTINCT, dan Kombinasi dengan Search | FE+BE | 45 | TC-FA-FAAM-474, TC-FA-FAAM-475, TC-FA-FAAM-476, TC-FA-FAAM-477, TC-FA-FAAM-478, TC-FA-FAAM-479 |
| TC-FA-FAAM-E2E-150-changelog-sort-kelas-kolom | Modal Changelog: Sort Kelas Date, Old-New Value, dan Modified By | FE+BE | 22 | TC-FA-FAAM-480, TC-FA-FAAM-482, TC-FA-FAAM-483 |
| TC-FA-FAAM-E2E-151-changelog-setup-column-kelas-date | Modal Changelog Setup Column: Kelas Date (Ceklis, Geser, Pin) | FE+BE | 34 | TC-FA-FAAM-484, TC-FA-FAAM-485, TC-FA-FAAM-486 |
| TC-FA-FAAM-E2E-152-changelog-setup-column-kelas-modified-by | Modal Changelog Setup Column: Kelas Modified By (Ceklis, Geser, Pin) | FE+BE | 34 | TC-FA-FAAM-490, TC-FA-FAAM-491, TC-FA-FAAM-492 |
| TC-FA-FAAM-E2E-153-changelog-setup-column-kelas-teks-ceklis-dan-geser | Modal Changelog Setup Column: Kelas Action, Asset Name, Field, Old-New Value (Ceklis dan Geser) | FE+BE | 22 | TC-FA-FAAM-487, TC-FA-FAAM-488 |
| TC-FA-FAAM-E2E-154-changelog-setup-column-pin-dan-screening-popup | Modal Changelog Setup Column: Pin Kelas Teks dan Screening Overlay-Popup | FE+BE | 22 | TC-FA-FAAM-489, TC-FA-FAAM-493 |
| TC-FA-FAAM-E2E-155-changelog-setup-column-reset-independen-dan-paginasi | Modal Changelog: Reset to Default, Discard, Guard Satu Kolom, Independen dari Tabel Utama, dan Paginasi | FE+BE | 29 | TC-FA-FAAM-494, TC-FA-FAAM-495, TC-FA-FAAM-496 |
| TC-FA-FAAM-E2E-156-changelog-download-nama-berkas-format-dan-isi | Modal Changelog Download: Nama Berkas, Format, Cakupan, dan Modified By Nama Lengkap | FE+BE | 22 | TC-FA-FAAM-497, TC-FA-FAAM-499 |
| TC-FA-FAAM-E2E-157-changelog-snapshot-rename-dan-format-tanggal | Modal Changelog: Entri Lama Tidak Berubah Setelah Rename dan Format Tanggal General Settings | FE+BE | 19 | TC-FA-FAAM-469, TC-FA-FAAM-500 |
| TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | Tab Models per Brand: Screening, Sort Brand dan Model/Type, No Model, dan Hover Badge | FE+BE | 31 | TC-FA-FAAM-542, TC-FA-FAAM-543, TC-FA-FAAM-544, TC-FA-FAAM-545, TC-FA-FAAM-668 |
| TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort | Tab Linked Custom Fields: Screening dan Sort Kelas Field Name, Data Type, Global Value | FE+BE | 28 | TC-FA-FAAM-546, TC-FA-FAAM-547, TC-FA-FAAM-548, TC-FA-FAAM-549 |
| TC-FA-FAAM-E2E-160-tab-linked-custom-fields-tautan-dan-penambahan-scope | Tab Linked Custom Fields: Tautan Open in Custom Fields dan Penambahan Custom Field Berscope | FE+BE | 13 | TC-FA-FAAM-550, TC-FA-FAAM-551 |
| TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand | Setup Column Tab Models per Brand: Kolom Actions, Ceklis, Geser, dan Pin | FE+BE | 41 | TC-FA-FAAM-552, TC-FA-FAAM-553, TC-FA-FAAM-554, TC-FA-FAAM-555 |
| TC-FA-FAAM-E2E-162-setup-column-tab-linked-custom-fields-ceklis | Setup Column Tab Linked Custom Fields: Kolom Actions dan Ceklis | FE+BE | 24 | TC-FA-FAAM-556, TC-FA-FAAM-557 |
| TC-FA-FAAM-E2E-163-setup-column-tab-linked-custom-fields-geser-dan-pin | Setup Column Tab Linked Custom Fields: Geser dan Pin | FE+BE | 27 | TC-FA-FAAM-558, TC-FA-FAAM-559 |
| TC-FA-FAAM-E2E-164-changelog-sort-kelas-action-asset-name-dan-field | Modal Changelog: Sort Kelas Action, Asset Name, dan Field | FE+BE | 9 | TC-FA-FAAM-481 |
| TC-FA-FAAM-E2E-165-changelog-empty-state-client-tanpa-entri | Modal Changelog: Empty State pada Client Tanpa Entri Changelog | FE+BE | 2 | TC-FA-FAAM-466 |
| TC-FA-FAAM-E2E-166-total-assets-screening-format-sel-himpunan-dan-status | Tab Total Assets: Screening, Format Sel, Himpunan Aset, dan Badge Status | FE+BE | 28 | TC-FA-FAAM-501, TC-FA-FAAM-502, TC-FA-FAAM-504 |
| TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi | Tab Total Assets: Hover Badge, Strip Brand-Model Kosong, Tampilan Kolom Label, dan Paginasi | FE+BE | 34 | TC-FA-FAAM-522, TC-FA-FAAM-667, TC-FA-FAAM-685, TC-FA-FAAM-717 |
| TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | Tab Total Assets Search: Tanpa Hasil, Name, Asset ID, Brand, Model/Type, Group, Status, dan Last Updated | FE+BE | 25 | TC-FA-FAAM-506, TC-FA-FAAM-507, TC-FA-FAAM-508, TC-FA-FAAM-509, TC-FA-FAAM-510 |
| TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal | Tab Total Assets Search: Kolom Hidden, Label, Tanggal Last Scanned-Warranty, dan Kelas Category | FE+BE | 0 | TC-FA-FAAM-541, TC-FA-FAAM-711, TC-FA-FAAM-761, TC-FA-FAAM-754 |
| TC-FA-FAAM-E2E-170-total-assets-search-measurement-dan-tag | Tab Total Assets Search: Kelas Measurement dan Kelas TAG | FE+BE | 30 | TC-FA-FAAM-758, TC-FA-FAAM-801 |
| TC-FA-FAAM-E2E-171-total-assets-search-transactional-policy-dan-asset-value | Tab Total Assets Search: Kelas Transactional Policy dan Asset Value Commercial | FE+BE | 0 | TC-FA-FAAM-802, TC-FA-FAAM-809 |
| TC-FA-FAAM-E2E-172-total-assets-filter-screening-brand-model-group | Tab Total Assets Filter: Screening Panel, Opsi Brand-Model DISTINCT, dan Group | FE+BE | 28 | TC-FA-FAAM-511, TC-FA-FAAM-512, TC-FA-FAAM-513 |
| TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and | Tab Total Assets Filter: Status, Last Updated, AND Brand-Group, dan Filter Brand-Model Service Vehicle | FE+BE | 21 | TC-FA-FAAM-514, TC-FA-FAAM-515, TC-FA-FAAM-516, TC-FA-FAAM-666 |
| TC-FA-FAAM-E2E-174-total-assets-filter-label-tag-dan-measurement | Tab Total Assets Filter: Label OR, TAG, dan Measurement | FE+BE | 28 | TC-FA-FAAM-712, TC-FA-FAAM-753, TC-FA-FAAM-759 |
| TC-FA-FAAM-E2E-175-total-assets-filter-category-policy-dan-last-scanned | Tab Total Assets Filter: Category Tree Picker, Transactional Policy, dan Last Scanned | FE+BE | 33 | TC-FA-FAAM-762, TC-FA-FAAM-764, TC-FA-FAAM-769 |
| TC-FA-FAAM-E2E-176-total-assets-sort-name-asset-id-dan-brand-model-group | Tab Total Assets Sort: Name, Asset ID, Brand, Model/Type, dan Group | FE+BE | 19 | TC-FA-FAAM-517, TC-FA-FAAM-518, TC-FA-FAAM-519 |
| TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag | Tab Total Assets Sort: Status, Last Updated, Label, dan TAG | FE+BE | 30 | TC-FA-FAAM-520, TC-FA-FAAM-521, TC-FA-FAAM-713, TC-FA-FAAM-752 |
| TC-FA-FAAM-E2E-178-total-assets-sort-kolom-seragam-last-scanned-warranty-dan-asset-value | Tab Total Assets Sort: Last Scanned, Warranty Expiry, dan Asset Value (Commercial) | FE+BE | 0 | TC-FA-FAAM-768, TC-FA-FAAM-772, TC-FA-FAAM-776 |
| TC-FA-FAAM-E2E-179-total-assets-download-scope-status-dan-label | Tab Total Assets Download: Cakupan Search-Filter, Kolom Status, dan Kolom Label | FE+BE | 24 | TC-FA-FAAM-523, TC-FA-FAAM-525, TC-FA-FAAM-718 |
| TC-FA-FAAM-E2E-180-total-assets-download-tag-measurement-category-policy | Tab Total Assets Download: Kolom TAG, Measurement, Category, Transactional Policy, dan Last Scanned | FE+BE | 23 | TC-FA-FAAM-756, TC-FA-FAAM-766, TC-FA-FAAM-770 |
| TC-FA-FAAM-E2E-181-total-assets-download-asset-value-warranty-dan-no-access | Tab Total Assets Download: Asset Value, Warranty Expiry, dan Teks No access | FE+BE | 0 | TC-FA-FAAM-774, TC-FA-FAAM-778, TC-FA-FAAM-793 |
| TC-FA-FAAM-E2E-182-total-assets-setup-column-screening-reset-dan-search-hidden | Tab Total Assets Setup Column: Screening Overlay-Popup, Reset to Default, Discard, dan Guard | FE+BE | 25 | TC-FA-FAAM-526, TC-FA-FAAM-527, TC-FA-FAAM-540 |
| TC-FA-FAAM-E2E-183-total-assets-setup-column-name-asset-id-ceklis-geser-pin | Tab Total Assets Setup Column: Kelas Name dan Asset ID (Ceklis, Geser, Pin) | FE+BE | 32 | TC-FA-FAAM-528, TC-FA-FAAM-529, TC-FA-FAAM-530 |
| TC-FA-FAAM-E2E-184-total-assets-setup-column-badge-ceklis-dan-geser | Tab Total Assets Setup Column: Kelas Brand, Model/Type, Group (Ceklis dan Geser) | FE+BE | 27 | TC-FA-FAAM-531, TC-FA-FAAM-532 |
| TC-FA-FAAM-E2E-185-total-assets-setup-column-badge-pin-dan-status | Tab Total Assets Setup Column: Badge Pin dan Kelas Status (Ceklis, Geser) | FE+BE | 29 | TC-FA-FAAM-533, TC-FA-FAAM-534, TC-FA-FAAM-535 |
| TC-FA-FAAM-E2E-186-total-assets-setup-column-status-pin-dan-last-updated | Tab Total Assets Setup Column: Status Pin dan Last Updated (Ceklis, Geser) | FE+BE | 23 | TC-FA-FAAM-536, TC-FA-FAAM-537, TC-FA-FAAM-538 |
| TC-FA-FAAM-E2E-187-total-assets-setup-column-last-updated-pin-dan-label-ceklis | Tab Total Assets Setup Column: Last Updated Pin dan Kelas Label (Default Tersembunyi, Ceklis) | FE+BE | 19 | TC-FA-FAAM-539, TC-FA-FAAM-714 |
| TC-FA-FAAM-E2E-188-total-assets-setup-column-label-geser-pin-dan-tag | Tab Total Assets Setup Column: Label Geser dan Pin serta Kelas TAG | FE+BE | 27 | TC-FA-FAAM-715, TC-FA-FAAM-716, TC-FA-FAAM-755 |
| TC-FA-FAAM-E2E-189-total-assets-kolom-urutan-setup-column-dan-tag | Tab Total Assets: Urutan Kolom Setup Column Sesuai Tabel dan Kolom TAG Tanpa Tag Code | FE+BE | 0 | TC-FA-FAAM-750, TC-FA-FAAM-751 |
| TC-FA-FAAM-E2E-190-total-assets-kolom-measurement-dan-category | Tab Total Assets: Kolom Measurement (Symbol) dan Kolom Category Curated | FE+BE | 20 | TC-FA-FAAM-757, TC-FA-FAAM-760 |
| TC-FA-FAAM-E2E-191-total-assets-kolom-transactional-policy-dan-last-scanned | Tab Total Assets: Kolom Transactional Policy dan Last Scanned | FE+BE | 22 | TC-FA-FAAM-763, TC-FA-FAAM-767 |
| TC-FA-FAAM-E2E-192-total-assets-kolom-asset-value-dan-warranty-expiry | Tab Total Assets: Kolom Asset Value Commercial dan Warranty Expiry Curated | FE+BE | 17 | TC-FA-FAAM-771, TC-FA-FAAM-775 |
| TC-FA-FAAM-E2E-193-total-assets-kolom-custom-field-daftar-scope-dan-purchasing | Tab Total Assets: Kolom Custom Field (Daftar Aktif, Scope General, Di Luar Scope) | FE+BE | 31 | TC-FA-FAAM-779, TC-FA-FAAM-780, TC-FA-FAAM-781 |
| TC-FA-FAAM-E2E-194-total-assets-kolom-custom-field-purchasing-numerik-dan-setup | Tab Total Assets: Kolom Custom Field Purchasing Numerik dan Setup Column Custom Field | FE+BE | 28 | TC-FA-FAAM-782, TC-FA-FAAM-783 |
| TC-FA-FAAM-E2E-195-total-assets-kolom-asset-id-retensi-state-dan-full-value | Tab Total Assets: Asset ID Tidak Filterable, Pindah Tab Memulihkan State Kolom Curated, dan Aktor Full Value Access | FE+BE | 0 | TC-FA-FAAM-788, TC-FA-FAAM-796, TC-FA-FAAM-808 |
| TC-FA-FAAM-E2E-196-total-assets-custom-field-dropdown-dan-date | Tab Total Assets Custom Field: Dropdown, Multi-Dropdown, Date, dan DateTime | FE+BE | 34 | TC-FA-FAAM-810, TC-FA-FAAM-811 |
| TC-FA-FAAM-E2E-197-total-assets-custom-field-numerik-teks-dan-formula | Tab Total Assets Custom Field: Numeric, Currency, Percentage, Text, Text Area, Phone, Email, URL, dan Document | FE+BE | 25 | TC-FA-FAAM-812, TC-FA-FAAM-813 |
| TC-FA-FAAM-E2E-198-total-assets-formula-dan-filter-range-nilai-full-value | Tab Total Assets: Custom Field Formula dan Filter Range Asset Value-Warranty (Full Value Access) | FE+BE | 27 | TC-FA-FAAM-773, TC-FA-FAAM-777, TC-FA-FAAM-814 |
| TC-FA-FAAM-E2E-199-total-assets-asset-value-commercial-fiscal-dua-kolom-tetap | Tab Total Assets: Asset Value Dua Kolom Tetap Commercial dan Fiscal serta Not Depreciated | FE+BE | 27 | TC-FA-FAAM-823, TC-FA-FAAM-824, TC-FA-FAAM-825 |
| TC-FA-FAAM-E2E-200-total-assets-asset-value-fiscal-gerbang-dan-sort-filter | Tab Total Assets: Gerbang No access pada Dua Kolom Asset Value serta Sort-Filter-Search Fiscal | FE+BE | 0 | TC-FA-FAAM-826, TC-FA-FAAM-827 |
| TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari | Tab Total Assets: Penanda Warranty Expiry (Lewat, Hari Ini, Hari ke-30, Hari ke-31) | FE+BE | 22 | TC-FA-FAAM-816, TC-FA-FAAM-817, TC-FA-FAAM-818, TC-FA-FAAM-819 |
| TC-FA-FAAM-E2E-202-total-assets-penanda-masa-garansi-strip-time-zone-dan-netral | Tab Total Assets: Penanda Garansi Strip-No access, Time Zone Client, dan Tidak Memengaruhi Sort-Filter-Search | FE+BE | 0 | TC-FA-FAAM-820, TC-FA-FAAM-821, TC-FA-FAAM-822 |
| TC-FA-FAAM-E2E-203-total-assets-gerbang-asset-value-ho-sel-dan-sort | Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Sel dan Sort No access Paling Akhir) | FE+BE | 0 | TC-FA-FAAM-784, TC-FA-FAAM-790 |
| TC-FA-FAAM-E2E-204-total-assets-gerbang-asset-value-ho-filter-dan-lintas-group | Tab Total Assets Gerbang Akses: Aktor Asset Value HO (Filter dan Baris Lintas Group) | FE+BE | 0 | TC-FA-FAAM-795, TC-FA-FAAM-791 |
| TC-FA-FAAM-E2E-205-total-assets-gerbang-purchase-ho-sel-tooltip-dan-search | Tab Total Assets Gerbang Akses: Aktor Purchase HO (Sel, Tooltip, dan Search) | FE+BE | 23 | TC-FA-FAAM-786, TC-FA-FAAM-789, TC-FA-FAAM-792 |
| TC-FA-FAAM-E2E-206-total-assets-gerbang-purchase-ho-custom-field-purchasing | Tab Total Assets Gerbang Akses: Aktor Purchase HO (Custom Field Purchasing di Luar Scope dan Filter) | FE+BE | 12 | TC-FA-FAAM-803, TC-FA-FAAM-815 |
| TC-FA-FAAM-E2E-207-total-assets-gerbang-tanpa-hak-nilai-sensitif | Tab Total Assets Gerbang Akses: Aktor Tanpa Hak Nilai Sensitif (Kolom, Ketersediaan, dan Respons Data) | FE+BE | 27 | TC-FA-FAAM-787, TC-FA-FAAM-794, TC-FA-FAAM-800 |
| TC-FA-FAAM-E2E-208-total-assets-gerbang-accounting-global-dan-lisensi-fa7 | Tab Total Assets Gerbang Akses: Aktor Accounting Global dan Lisensi FA-7 Grace Period atau Tidak Aktif | FE+BE | 0 | TC-FA-FAAM-785, TC-FA-FAAM-806, TC-FA-FAAM-807 |
| TC-FA-FAAM-E2E-209-total-assets-hak-tier-role-matrix-global-dan-group-manager | Tab Total Assets Gerbang Akses: Hak Tier Total Control, Default User, Read Only, dan Group Manager | FE+BE | 28 | TC-FA-FAAM-804, TC-FA-FAAM-805 |
| TC-FA-FAAM-E2E-210-total-assets-himpunan-aset-dan-empty-state-tanpa-aset | Tab Total Assets: Himpunan Aset Draft-Waiting-Active dan Empty State Tanpa Aset | FE+BE | 9 | TC-FA-FAAM-503, TC-FA-FAAM-505 |
| TC-FA-FAAM-E2E-211-total-assets-sort-kolom-seragam-measurement-category-dan-policy | Tab Total Assets Sort: Kolom Bernilai Seragam (Measurement, Category, Transactional Policy) | FE+BE | 11 | TC-FA-FAAM-765 |
| TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | Pencatatan Changelog Edit: Field Asset Name, Code, Category, TAG Type, dan Brand | FE+BE | 36 | TC-FA-FAAM-560, TC-FA-FAAM-561, TC-FA-FAAM-562, TC-FA-FAAM-563, TC-FA-FAAM-564 |
| TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | Pencatatan Changelog Edit: Field Model/Type, Brand Dilepas, UoM, Default Addon, dan Default Label | FE+BE | 39 | TC-FA-FAAM-565, TC-FA-FAAM-566, TC-FA-FAAM-567, TC-FA-FAAM-568, TC-FA-FAAM-569 |
| TC-FA-FAAM-E2E-214-changelog-edit-beberapa-field-multi-nilai-dan-isolasi | Pencatatan Changelog Edit: Beberapa Field Sekaligus, Field Tidak Berubah, dan Urutan Old-New Multi-Nilai | FE+BE | 29 | TC-FA-FAAM-570, TC-FA-FAAM-571, TC-FA-FAAM-587 |
| TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi | Pencatatan Changelog: Create, Delete, Bulk Delete, dan Jejak Delete | FE+BE | 32 | TC-FA-FAAM-572, TC-FA-FAAM-573, TC-FA-FAAM-574, TC-FA-FAAM-583 |
| TC-FA-FAAM-E2E-216-pencatatan-absence-tanpa-baris-log | Pencatatan Absence: Tanpa Baris Log untuk Delete Tidak Ada, Record Lain, dan Delete Label Diblokir | FE+BE | 40 | TC-FA-FAAM-575, TC-FA-FAAM-588, TC-FA-FAAM-593 |
| TC-FA-FAAM-E2E-217-log-system-activity-create-dan-aksi-aktor | Log Multi-Surface: System Log Aktor dan Activity Log FAMS untuk Create dan Aksi Aktor | FE+BE | 22 | TC-FA-FAAM-579, TC-FA-FAAM-580, TC-FA-FAAM-734 |
| TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron | Log Multi-Surface: Name Sama, Tiga Surface Tersinkron, Delete, dan Bulk Delete | FE+BE | 52 | TC-FA-FAAM-581, TC-FA-FAAM-582, TC-FA-FAAM-735, TC-FA-FAAM-736 |
| TC-FA-FAAM-E2E-219-log-import-dan-modified-by-last-updated-mengikuti-changelog | Pencatatan: Asset Name Hasil Import Action Create dan Modified By-Last Updated Mengikuti Changelog | FE+BE | 23 | TC-FA-FAAM-578, TC-FA-FAAM-584 |
| TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | Sinkron Lintas Modul: Rename Category, Brand, UoM, Label dan Blok Delete Master Data yang Dipakai | FE+BE | 47 | TC-FA-FAAM-589, TC-FA-FAAM-590, TC-FA-FAAM-591, TC-FA-FAAM-592, TC-FA-FAAM-594, TC-FA-FAAM-595, TC-FA-FAAM-596 |
| TC-FA-FAAM-E2E-221-sinkron-locked-live-custom-id-scope-dan-cascade-aset | Sinkron Lintas Modul: Code ke Custom Asset ID, Rename ke Detail Aset, dan Delete Melepas Scope Custom Field | FE+BE | 32 | TC-FA-FAAM-600, TC-FA-FAAM-601, TC-FA-FAAM-603 |
| TC-FA-FAAM-E2E-222-sinkron-registrasi-aset-dropdown-asset-name-dan-excess | Sinkron Registrasi Aset: Dropdown Asset Name Tanpa Category Locked dan Asset Name Baru dengan Baris Policy Tersemai | FE+BE | 24 | TC-FA-FAAM-598, TC-FA-FAAM-599 |
| TC-FA-FAAM-E2E-223-paritas-import-edit-dan-delete-asset-name | Paritas Import: Asset Name Hasil Import Dapat Di-Edit dan Dihapus Mengikuti Guard In-Use | FE+BE | 20 | TC-FA-FAAM-604, TC-FA-FAAM-605 |
| TC-FA-FAAM-E2E-224-import-kuota-paket-dan-penyemaian-policy | Import: Ditolak Kuota Paket Growth dan Penyemaian Policy Transaksi ke Registrasi Aset | FE+BE | 33 | TC-FA-FAAM-606, TC-FA-FAAM-741 |
| TC-FA-FAAM-E2E-225-format-tanggal-zona-waktu-general-settings | Format Tanggal dan Zona Waktu General Settings pada Tabel Utama, Filter Last Updated, dan Tab Total Assets | FE+BE | 20 | TC-FA-FAAM-607, TC-FA-FAAM-608 |
| TC-FA-FAAM-E2E-226-sinkron-kolom-policy-custom-field-dan-last-scanned | Sinkron ke Tab Total Assets: Policy Transaksi, Nilai-Status Custom Field, dan Pemindaian Audit | FE+BE | 29 | TC-FA-FAAM-797, TC-FA-FAAM-798, TC-FA-FAAM-799 |
| TC-FA-FAAM-E2E-227-transisi-otomatis-default-addon-eventual-60-detik | Transisi Otomatis Default Addon (Eventual, Polling 60 Detik): Pending Tag, Pending Removal, dan Pelepasan Roster | FE+BE | 23 | TC-FA-FAAM-722, TC-FA-FAAM-723, TC-FA-FAAM-731 |
| TC-FA-FAAM-E2E-228-tag-type-non-standard-di-tag-dan-cancel-dialog | TAG Type Ber-Aset: Tag Bertipe Lama Menjadi Non-Standard di tag/ dan Cancel Dialog Tidak Mengubahnya | FE+BE | 33 | TC-FA-FAAM-665, TC-FA-FAAM-828 |
| TC-FA-FAAM-E2E-229-tag-type-tanpa-aset-dan-progres-kepatuhan-berubah | TAG Type: Tanpa Aset Tidak Menambah Non-Standard dan Progres Kepatuhan Popup Detail Berubah Lalu Dipulihkan | FE+BE | 39 | TC-FA-FAAM-664, TC-FA-FAAM-838 |
| TC-FA-FAAM-E2E-230-progres-kepatuhan-replace-dan-pair-tag-hardware-reader | Progres Kepatuhan TAG Type: Replace TAG dengan Reader USB, Popup Tidak Auto-Refresh | FE+BE | 33 | TC-FA-FAAM-839, TC-FA-FAAM-840 |
| TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | Defense-in-Depth: Request Langsung Create-Edit-Delete-Bulk-Baca-Import Tanpa Hak Ditolak Server | FE+BE | 28 | TC-FA-FAAM-611, TC-FA-FAAM-612, TC-FA-FAAM-613, TC-FA-FAAM-614, TC-FA-FAAM-615, TC-FA-FAAM-616 |
| TC-FA-FAAM-E2E-232-defense-in-depth-payload-dan-aturan-server | Defense-in-Depth: Payload Script-SQL pada Create dan Search Dirender atau Diperlakukan sebagai Teks | FE+BE | 31 | TC-FA-FAAM-625, TC-FA-FAAM-626, TC-FA-FAAM-627 |
| TC-FA-FAAM-E2E-233-state-tenant-suspended-expired-aksi-tulis-ditolak | State Tenant Suspended dan Expired: Create dan Edit Ditolak Server | FE+BE | 23 | TC-FA-FAAM-619, TC-FA-FAAM-620 |
| TC-FA-FAAM-E2E-234-state-tenant-pembacaan-tetap-berfungsi-dan-transisi-addon | State Tenant Suspended dan Expired: Pembacaan Tetap Berfungsi dan Transisi Otomatis Addon Berjalan | FE+BE | 20 | TC-FA-FAAM-610, TC-FA-FAAM-624 |
| TC-FA-FAAM-E2E-235-multi-konteks-dua-create-bersamaan | Multi-Konteks: Dua Create Bersamaan pada Nama dan Code yang Sama | FE+BE | 25 | TC-FA-FAAM-633, TC-FA-FAAM-634 |
| TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan | Multi-Konteks: Edit-Delete-Bulk Delete Bersamaan dengan Sesi Lain (Record Dihapus, Aset Baru, Kategori Internal) | FE+BE | 34 | TC-FA-FAAM-637, TC-FA-FAAM-638, TC-FA-FAAM-639, TC-FA-FAAM-640 |
| TC-FA-FAAM-E2E-237-multi-konteks-dua-edit-last-write-wins | Multi-Konteks: Dua Edit Bersamaan pada Record yang Sama (Last-Write-Wins dan Keunikan Tetap Ditolak) | FE+BE | 41 | TC-FA-FAAM-235, TC-FA-FAAM-641, TC-FA-FAAM-642 |
| TC-FA-FAAM-E2E-238-plan-tier-tanpa-gating-empat-plan | Plan Tier: Menu dan Aksi Create-Edit-Delete Tanpa Gating pada Starter, Growth, Professional, dan Enterprise | FE+BE | 18 | TC-FA-FAAM-674 |
| TC-FA-FAAM-E2E-239-changelog-opsi-filter-field-dan-action | Modal Changelog: Opsi Filter Field dan Action Memuat Nilai yang Tercatat | FE+BE | 10 | TC-FA-FAAM-585, TC-FA-FAAM-586 |
| TC-FA-FAAM-E2E-240-pencatatan-absence-tiga-surface-log | Pencatatan Absence: Edit Tanpa Perubahan dan Cascade Tidak Menulis Entri di Tiga Surface Log | FE+BE | 47 | TC-FA-FAAM-576, TC-FA-FAAM-577 |
| TC-FA-FAAM-E2E-241-sinkron-category-locked-live-subcategory | Sinkron Lintas Modul: Subcategory Menambah dan Menghapus Kunci Category Locked Asset Name Secara Live | FE+BE | 17 | TC-FA-FAAM-597 |
| TC-FA-FAAM-E2E-242-sinkron-cascade-category-ke-aset-dan-lisensi-addon | Sinkron Lintas Modul: Cascade Category ke Aset dan Lisensi Addon Berakhir Setelah Tersimpan | FE+BE | 15 | TC-FA-FAAM-602, TC-FA-FAAM-609 |
| TC-FA-FAAM-E2E-243-sinkron-registrasi-aset-asset-name-menjadi-excess | Sinkron Registrasi Aset: Asset Name yang Menjadi Excess Setelah Dipilih Ditolak Server saat Submit | FE+BE | 12 | TC-FA-FAAM-675 |
| TC-FA-FAAM-E2E-244-sinkron-dropdown-registrasi-aset-rename-dan-delete | Sinkron Registrasi Aset: Rename Asset Name Terlihat di Dropdown dan Policy, Asset Name Dihapus Hilang dari Dropdown | FE+BE | 31 | TC-FA-FAAM-739, TC-FA-FAAM-740 |
| TC-FA-FAAM-E2E-245-tag-type-tanpa-objek-tugas-dan-pending-changes | TAG Type Ber-Aset: Edit Tidak Membuat Objek Tugas atau Dokumen dan Menu TAG Tanpa Pending Changes | FE+BE | 19 | TC-FA-FAAM-829 |
| TC-FA-FAAM-E2E-246-progres-kepatuhan-pair-tag-hardware-reader | Progres Kepatuhan TAG Type: Pair TAG pada Aset Not Paired Yet dengan Reader USB | FE+BE | 18 | TC-FA-FAAM-841 |
| TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak | Pencatatan Absence: Request Langsung Tanpa Hak (Create, Edit, Delete, Bulk Delete) yang Ditolak Server Tidak Menulis Entri di Changelog | FE+BE | 30 | TC-FA-FAAM-611, TC-FA-FAAM-612, TC-FA-FAAM-613, TC-FA-FAAM-614 |
| TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | Defense-in-Depth: Request Langsung Category Internal, Non-TAG Bersama Tipe TAG, Delete In-Use, dan Category Tidak Ada Ditolak Server | FE+BE | 23 | TC-FA-FAAM-628, TC-FA-FAAM-629, TC-FA-FAAM-630, TC-FA-FAAM-631, TC-FA-FAAM-632 |
| TC-FA-FAAM-E2E-249-multi-konteks-dua-create-slot-kuota-dan-ceiling | Multi-Konteks: Dua Create Bersamaan pada Slot Kuota Terakhir dan Slot Ceiling Terakhir | FE+BE | 30 | TC-FA-FAAM-635, TC-FA-FAAM-636 |
| TC-FA-FAAM-E2E-250-state-tenant-suspended-expired-delete-bulk-dan-import-ditolak | State Tenant Suspended dan Expired: Delete, Bulk Delete, dan Import Ditolak Server | FE+BE | 25 | TC-FA-FAAM-621, TC-FA-FAAM-622, TC-FA-FAAM-623 |
| TC-FA-FAAM-E2E-251-pencatatan-absence-bulk-delete-langsung-semua-in-use | Pencatatan Absence: Request Bulk Delete Langsung Semua In-Use Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 35 | TC-FA-FAAM-844 |
| TC-FA-FAAM-E2E-252-pencatatan-absence-request-create-langsung-ditolak | Pencatatan Absence: Request Create Langsung yang Ditolak Server (Category Excess, TAG Type Terkunci Paket, Default Addon pada Non-TAG, Addon Tanpa Lisensi) Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 75 | TC-FA-FAAM-845 |
| TC-FA-FAAM-E2E-253-pencatatan-absence-create-edit-ditolak-suspended-expired | Pencatatan Absence: Create dan Edit yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 51 | TC-FA-FAAM-842 |
| TC-FA-FAAM-E2E-254-pencatatan-absence-delete-bulk-delete-import-ditolak-suspended-expired | Pencatatan Absence: Delete, Bulk Delete, dan Import yang Ditolak Saat Client Suspended atau Expired Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 73 | TC-FA-FAAM-843 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua TC masuk ke spec E2E; hanya TC-FA-FAAM-611 sampai TC-FA-FAAM-614 yang muncul di dua spec (alasan di atas).

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-FAAM-1 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-2 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-3 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-4 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-5 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-6 | E2E | TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman | FE+BE |
| TC-FA-FAAM-7 | E2E | TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman | FE+BE |
| TC-FA-FAAM-8 | E2E | TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman | FE+BE |
| TC-FA-FAAM-9 | E2E | TC-FA-FAAM-E2E-002-retensi-state-search-sort-filter-dan-halaman | FE+BE |
| TC-FA-FAAM-10 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-11 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-12 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-13 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-14 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-15 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-16 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-17 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-18 | E2E | TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | FE+BE |
| TC-FA-FAAM-19 | E2E | TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | FE+BE |
| TC-FA-FAAM-20 | E2E | TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | FE+BE |
| TC-FA-FAAM-21 | E2E | TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | FE+BE |
| TC-FA-FAAM-22 | E2E | TC-FA-FAAM-E2E-004-sel-multi-nilai-badge-strip-dan-lima-icon-tag-type | FE+BE |
| TC-FA-FAAM-23 | E2E | TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update | FE+BE |
| TC-FA-FAAM-24 | E2E | TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update | FE+BE |
| TC-FA-FAAM-25 | E2E | TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update | FE+BE |
| TC-FA-FAAM-26 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-27 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-28 | E2E | TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update | FE+BE |
| TC-FA-FAAM-29 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-30 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-31 | E2E | TC-FA-FAAM-E2E-003-format-sel-kolom-skalar-dan-interaksi-baris | FE+BE |
| TC-FA-FAAM-32 | E2E | TC-FA-FAAM-E2E-006-empty-state-no-results-dan-skeleton-loader | FE+BE |
| TC-FA-FAAM-33 | E2E | TC-FA-FAAM-E2E-006-empty-state-no-results-dan-skeleton-loader | FE+BE |
| TC-FA-FAAM-34 | E2E | TC-FA-FAAM-E2E-006-empty-state-no-results-dan-skeleton-loader | FE+BE |
| TC-FA-FAAM-35 | E2E | TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog | FE+BE |
| TC-FA-FAAM-36 | E2E | TC-FA-FAAM-E2E-001-screening-tab-asset-name-breadcrumb-dan-navigasi | FE+BE |
| TC-FA-FAAM-37 | E2E | TC-FA-FAAM-E2E-007-propagasi-perubahan-sesi-lain-ke-list-dan-modal | FE+BE |
| TC-FA-FAAM-38 | E2E | TC-FA-FAAM-E2E-007-propagasi-perubahan-sesi-lain-ke-list-dan-modal | FE+BE |
| TC-FA-FAAM-39 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-40 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-41 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-42 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-43 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-44 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-45 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-46 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-47 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-48 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-49 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-50 | E2E | TC-FA-FAAM-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-FA-FAAM-51 | E2E | TC-FA-FAAM-E2E-009-role-matrix-negatif-tanpa-role-dan-hak-dicabut | FE+BE |
| TC-FA-FAAM-52 | E2E | TC-FA-FAAM-E2E-010-role-matrix-positif-create-only | FE+BE |
| TC-FA-FAAM-53 | E2E | TC-FA-FAAM-E2E-011-role-matrix-positif-update-only-edit | FE+BE |
| TC-FA-FAAM-54 | E2E | TC-FA-FAAM-E2E-013-role-matrix-positif-delete-only | FE+BE |
| TC-FA-FAAM-55 | E2E | TC-FA-FAAM-E2E-013-role-matrix-positif-delete-only | FE+BE |
| TC-FA-FAAM-56 | E2E | TC-FA-FAAM-E2E-014-role-matrix-hak-gabungan-baca-dan-import-data | FE+BE |
| TC-FA-FAAM-57 | E2E | TC-FA-FAAM-E2E-013-role-matrix-positif-delete-only | FE+BE |
| TC-FA-FAAM-58 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-59 | E2E | TC-FA-FAAM-E2E-011-role-matrix-positif-update-only-edit | FE+BE |
| TC-FA-FAAM-60 | E2E | TC-FA-FAAM-E2E-010-role-matrix-positif-create-only | FE+BE |
| TC-FA-FAAM-61 | E2E | TC-FA-FAAM-E2E-012-role-matrix-tombol-default-label-di-modal-edit | FE+BE |
| TC-FA-FAAM-62 | E2E | TC-FA-FAAM-E2E-012-role-matrix-tombol-default-label-di-modal-edit | FE+BE |
| TC-FA-FAAM-63 | E2E | TC-FA-FAAM-E2E-010-role-matrix-positif-create-only | FE+BE |
| TC-FA-FAAM-64 | E2E | TC-FA-FAAM-E2E-014-role-matrix-hak-gabungan-baca-dan-import-data | FE+BE |
| TC-FA-FAAM-65 | E2E | TC-FA-FAAM-E2E-014-role-matrix-hak-gabungan-baca-dan-import-data | FE+BE |
| TC-FA-FAAM-66 | E2E | TC-FA-FAAM-E2E-023-create-screening-popup-aksesibilitas-dan-checkbox-stay | FE+BE |
| TC-FA-FAAM-67 | E2E | TC-FA-FAAM-E2E-023-create-screening-popup-aksesibilitas-dan-checkbox-stay | FE+BE |
| TC-FA-FAAM-68 | E2E | TC-FA-FAAM-E2E-043-create-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-FA-FAAM-69 | E2E | TC-FA-FAAM-E2E-036-create-clear-field-dan-error-inline | FE+BE |
| TC-FA-FAAM-70 | E2E | TC-FA-FAAM-E2E-036-create-clear-field-dan-error-inline | FE+BE |
| TC-FA-FAAM-71 | E2E | TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | FE+BE |
| TC-FA-FAAM-72 | E2E | TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | FE+BE |
| TC-FA-FAAM-73 | E2E | TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | FE+BE |
| TC-FA-FAAM-74 | E2E | TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | FE+BE |
| TC-FA-FAAM-75 | E2E | TC-FA-FAAM-E2E-037-create-penutupan-form-unsaved-changes | FE+BE |
| TC-FA-FAAM-76 | E2E | TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-77 | E2E | TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-78 | E2E | TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-79 | E2E | TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-80 | E2E | TC-FA-FAAM-E2E-038-create-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-81 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-82 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-83 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-84 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-85 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-86 | E2E | TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label | FE+BE |
| TC-FA-FAAM-87 | E2E | TC-FA-FAAM-E2E-026-create-validasi-asset-name-duplikat-dan-debounce | FE+BE |
| TC-FA-FAAM-88 | E2E | TC-FA-FAAM-E2E-026-create-validasi-asset-name-duplikat-dan-debounce | FE+BE |
| TC-FA-FAAM-89 | E2E | TC-FA-FAAM-E2E-026-create-validasi-asset-name-duplikat-dan-debounce | FE+BE |
| TC-FA-FAAM-90 | E2E | TC-FA-FAAM-E2E-044-create-changelog-create-dan-nama-sama-di-client-lain | FE+BE |
| TC-FA-FAAM-91 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-92 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-93 | E2E | TC-FA-FAAM-E2E-025-create-validasi-asset-name-spasi-panjang-emoji-dan-karakter | FE+BE |
| TC-FA-FAAM-94 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-95 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-96 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-97 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-98 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-99 | E2E | TC-FA-FAAM-E2E-027-create-validasi-code-batas-format-dan-helper | FE+BE |
| TC-FA-FAAM-100 | E2E | TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label | FE+BE |
| TC-FA-FAAM-101 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-102 | E2E | TC-FA-FAAM-E2E-028-create-category-tree-picker-stale-dan-internal | FE+BE |
| TC-FA-FAAM-103 | E2E | TC-FA-FAAM-E2E-028-create-category-tree-picker-stale-dan-internal | FE+BE |
| TC-FA-FAAM-104 | E2E | TC-FA-FAAM-E2E-028-create-category-tree-picker-stale-dan-internal | FE+BE |
| TC-FA-FAAM-105 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-106 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-107 | E2E | TC-FA-FAAM-E2E-029-create-tag-type-opsi-dan-mutual-exclusion | FE+BE |
| TC-FA-FAAM-108 | E2E | TC-FA-FAAM-E2E-029-create-tag-type-opsi-dan-mutual-exclusion | FE+BE |
| TC-FA-FAAM-109 | E2E | TC-FA-FAAM-E2E-029-create-tag-type-opsi-dan-mutual-exclusion | FE+BE |
| TC-FA-FAAM-110 | E2E | TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci | FE+BE |
| TC-FA-FAAM-111 | E2E | TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci | FE+BE |
| TC-FA-FAAM-112 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-113 | E2E | TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci | FE+BE |
| TC-FA-FAAM-114 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-115 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-116 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-117 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-118 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-119 | E2E | TC-FA-FAAM-E2E-030-create-chip-tag-type-search-dan-default-addon | FE+BE |
| TC-FA-FAAM-120 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-121 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-122 | E2E | TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | FE+BE |
| TC-FA-FAAM-123 | E2E | TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | FE+BE |
| TC-FA-FAAM-124 | E2E | TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | FE+BE |
| TC-FA-FAAM-125 | E2E | TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | FE+BE |
| TC-FA-FAAM-126 | E2E | TC-FA-FAAM-E2E-031-create-default-label-dan-modal-create-label | FE+BE |
| TC-FA-FAAM-127 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-128 | E2E | TC-FA-FAAM-E2E-032-create-brand-tabel-model-per-brand | FE+BE |
| TC-FA-FAAM-129 | E2E | TC-FA-FAAM-E2E-032-create-brand-tabel-model-per-brand | FE+BE |
| TC-FA-FAAM-130 | E2E | TC-FA-FAAM-E2E-032-create-brand-tabel-model-per-brand | FE+BE |
| TC-FA-FAAM-131 | E2E | TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | FE+BE |
| TC-FA-FAAM-132 | E2E | TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | FE+BE |
| TC-FA-FAAM-133 | E2E | TC-FA-FAAM-E2E-034-create-model-duplikat-dan-no-model-default | FE+BE |
| TC-FA-FAAM-134 | E2E | TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | FE+BE |
| TC-FA-FAAM-135 | E2E | TC-FA-FAAM-E2E-034-create-model-duplikat-dan-no-model-default | FE+BE |
| TC-FA-FAAM-136 | E2E | TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | FE+BE |
| TC-FA-FAAM-137 | E2E | TC-FA-FAAM-E2E-052-defense-in-depth-create-request-langsung | FE+BE |
| TC-FA-FAAM-138 | E2E | TC-FA-FAAM-E2E-033-create-input-model-batas-karakter-dan-emoji | FE+BE |
| TC-FA-FAAM-139 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-140 | E2E | TC-FA-FAAM-E2E-035-create-uom-opsi-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-141 | E2E | TC-FA-FAAM-E2E-035-create-uom-opsi-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-142 | E2E | TC-FA-FAAM-E2E-024-create-required-semua-field-wajib | FE+BE |
| TC-FA-FAAM-143 | E2E | TC-FA-FAAM-E2E-039-create-sukses-hanya-field-wajib | FE+BE |
| TC-FA-FAAM-144 | E2E | TC-FA-FAAM-E2E-057-create-sukses-seluruh-field-opsional-dan-non-tag | FE+BE |
| TC-FA-FAAM-145 | E2E | TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label | FE+BE |
| TC-FA-FAAM-146 | E2E | TC-FA-FAAM-E2E-040-create-sukses-code-manual-addon-dan-label | FE+BE |
| TC-FA-FAAM-147 | E2E | TC-FA-FAAM-E2E-041-create-sukses-dua-brand-dan-model | FE+BE |
| TC-FA-FAAM-148 | E2E | TC-FA-FAAM-E2E-057-create-sukses-seluruh-field-opsional-dan-non-tag | FE+BE |
| TC-FA-FAAM-149 | E2E | TC-FA-FAAM-E2E-041-create-sukses-dua-brand-dan-model | FE+BE |
| TC-FA-FAAM-150 | E2E | TC-FA-FAAM-E2E-042-create-stay-on-this-form-reset-tutup-dan-nama-sama | FE+BE |
| TC-FA-FAAM-151 | E2E | TC-FA-FAAM-E2E-042-create-stay-on-this-form-reset-tutup-dan-nama-sama | FE+BE |
| TC-FA-FAAM-152 | E2E | TC-FA-FAAM-E2E-042-create-stay-on-this-form-reset-tutup-dan-nama-sama | FE+BE |
| TC-FA-FAAM-153 | E2E | TC-FA-FAAM-E2E-023-create-screening-popup-aksesibilitas-dan-checkbox-stay | FE+BE |
| TC-FA-FAAM-154 | E2E | TC-FA-FAAM-E2E-046-create-kuota-paket-starter-dialog-dan-cta-upgrade | FE+BE |
| TC-FA-FAAM-155 | E2E | TC-FA-FAAM-E2E-045-create-gating-plan-kuota-starter-dan-tag-type-terkunci | FE+BE |
| TC-FA-FAAM-156 | E2E | TC-FA-FAAM-E2E-046-create-kuota-paket-starter-dialog-dan-cta-upgrade | FE+BE |
| TC-FA-FAAM-157 | E2E | TC-FA-FAAM-E2E-046-create-kuota-paket-starter-dialog-dan-cta-upgrade | FE+BE |
| TC-FA-FAAM-158 | E2E | TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | FE+BE |
| TC-FA-FAAM-159 | E2E | TC-FA-FAAM-E2E-048-create-ceiling-satu-di-bawah-race-dan-per-katalog | FE+BE |
| TC-FA-FAAM-160 | E2E | TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | FE+BE |
| TC-FA-FAAM-161 | E2E | TC-FA-FAAM-E2E-049-create-ceiling-model-type-d08-dan-no-model | FE+BE |
| TC-FA-FAAM-162 | E2E | TC-FA-FAAM-E2E-049-create-ceiling-model-type-d08-dan-no-model | FE+BE |
| TC-FA-FAAM-163 | E2E | TC-FA-FAAM-E2E-056-create-ceiling-stay-hingga-ceiling | FE+BE |
| TC-FA-FAAM-164 | E2E | TC-FA-FAAM-E2E-049-create-ceiling-model-type-d08-dan-no-model | FE+BE |
| TC-FA-FAAM-165 | E2E | TC-FA-FAAM-E2E-051-resilience-create-5xx-timeout-dan-tabrakan-code | FE+BE |
| TC-FA-FAAM-166 | E2E | TC-FA-FAAM-E2E-051-resilience-create-5xx-timeout-dan-tabrakan-code | FE+BE |
| TC-FA-FAAM-167 | E2E | TC-FA-FAAM-E2E-043-create-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-FA-FAAM-168 | E2E | TC-FA-FAAM-E2E-051-resilience-create-5xx-timeout-dan-tabrakan-code | FE+BE |
| TC-FA-FAAM-169 | E2E | TC-FA-FAAM-E2E-044-create-changelog-create-dan-nama-sama-di-client-lain | FE+BE |
| TC-FA-FAAM-170 | E2E | TC-FA-FAAM-E2E-058-edit-screening-clear-field-dan-aksesibilitas | FE+BE |
| TC-FA-FAAM-171 | E2E | TC-FA-FAAM-E2E-058-edit-screening-clear-field-dan-aksesibilitas | FE+BE |
| TC-FA-FAAM-172 | E2E | TC-FA-FAAM-E2E-058-edit-screening-clear-field-dan-aksesibilitas | FE+BE |
| TC-FA-FAAM-173 | E2E | TC-FA-FAAM-E2E-071-edit-saving-state-klik-ganda-dan-save-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-174 | E2E | TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | FE+BE |
| TC-FA-FAAM-175 | E2E | TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | FE+BE |
| TC-FA-FAAM-176 | E2E | TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | FE+BE |
| TC-FA-FAAM-177 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-178 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-179 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-180 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-181 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-182 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-183 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-184 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-185 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-186 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-187 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-188 | E2E | TC-FA-FAAM-E2E-061-edit-validasi-asset-name | FE+BE |
| TC-FA-FAAM-189 | E2E | TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | FE+BE |
| TC-FA-FAAM-190 | E2E | TC-FA-FAAM-E2E-062-edit-validasi-code | FE+BE |
| TC-FA-FAAM-191 | E2E | TC-FA-FAAM-E2E-062-edit-validasi-code | FE+BE |
| TC-FA-FAAM-192 | E2E | TC-FA-FAAM-E2E-062-edit-validasi-code | FE+BE |
| TC-FA-FAAM-193 | E2E | TC-FA-FAAM-E2E-062-edit-validasi-code | FE+BE |
| TC-FA-FAAM-194 | E2E | TC-FA-FAAM-E2E-062-edit-validasi-code | FE+BE |
| TC-FA-FAAM-195 | E2E | TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal | FE+BE |
| TC-FA-FAAM-196 | E2E | TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal | FE+BE |
| TC-FA-FAAM-197 | E2E | TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal | FE+BE |
| TC-FA-FAAM-198 | E2E | TC-FA-FAAM-E2E-063-edit-category-tree-picker-wajib-stale-dan-internal | FE+BE |
| TC-FA-FAAM-199 | E2E | TC-FA-FAAM-E2E-064-edit-category-locked-field-lain-dan-lepas-kunci | FE+BE |
| TC-FA-FAAM-200 | E2E | TC-FA-FAAM-E2E-064-edit-category-locked-field-lain-dan-lepas-kunci | FE+BE |
| TC-FA-FAAM-201 | E2E | TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset | FE+BE |
| TC-FA-FAAM-202 | E2E | TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset | FE+BE |
| TC-FA-FAAM-203 | E2E | TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset | FE+BE |
| TC-FA-FAAM-204 | E2E | TC-FA-FAAM-E2E-065-edit-tag-type-tanpa-aset | FE+BE |
| TC-FA-FAAM-205 | E2E | TC-FA-FAAM-E2E-091-edit-tag-type-grandfather-chip-terkunci-client-starter | FE+BE |
| TC-FA-FAAM-206 | E2E | TC-FA-FAAM-E2E-091-edit-tag-type-grandfather-chip-terkunci-client-starter | FE+BE |
| TC-FA-FAAM-207 | E2E | TC-FA-FAAM-E2E-089-defense-in-depth-edit-request-langsung-plan-dan-excess | FE+BE |
| TC-FA-FAAM-208 | E2E | TC-FA-FAAM-E2E-069-edit-uom-dan-addon-grandfather-lisensi | FE+BE |
| TC-FA-FAAM-209 | E2E | TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | FE+BE |
| TC-FA-FAAM-210 | E2E | TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | FE+BE |
| TC-FA-FAAM-211 | E2E | TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-212 | E2E | TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-213 | E2E | TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-214 | E2E | TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model | FE+BE |
| TC-FA-FAAM-215 | E2E | TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi | FE+BE |
| TC-FA-FAAM-216 | E2E | TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi | FE+BE |
| TC-FA-FAAM-217 | E2E | TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi | FE+BE |
| TC-FA-FAAM-218 | E2E | TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model | FE+BE |
| TC-FA-FAAM-219 | E2E | TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model | FE+BE |
| TC-FA-FAAM-220 | E2E | TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-221 | E2E | TC-FA-FAAM-E2E-066-edit-label-brand-uom-wajib-dan-dihapus-sesi-lain | FE+BE |
| TC-FA-FAAM-222 | E2E | TC-FA-FAAM-E2E-069-edit-uom-dan-addon-grandfather-lisensi | FE+BE |
| TC-FA-FAAM-223 | E2E | TC-FA-FAAM-E2E-071-edit-saving-state-klik-ganda-dan-save-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-224 | E2E | TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus | FE+BE |
| TC-FA-FAAM-225 | E2E | TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus | FE+BE |
| TC-FA-FAAM-226 | E2E | TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus | FE+BE |
| TC-FA-FAAM-227 | E2E | TC-FA-FAAM-E2E-070-edit-sukses-multi-field-dan-isolasi-field-lain | FE+BE |
| TC-FA-FAAM-228 | E2E | TC-FA-FAAM-E2E-070-edit-sukses-multi-field-dan-isolasi-field-lain | FE+BE |
| TC-FA-FAAM-229 | E2E | TC-FA-FAAM-E2E-070-edit-sukses-multi-field-dan-isolasi-field-lain | FE+BE |
| TC-FA-FAAM-230 | E2E | TC-FA-FAAM-E2E-072-edit-no-op-spasi-code-kosong-kapitalisasi-dan-record-dihapus | FE+BE |
| TC-FA-FAAM-231 | E2E | TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type | FE+BE |
| TC-FA-FAAM-232 | E2E | TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type | FE+BE |
| TC-FA-FAAM-233 | E2E | TC-FA-FAAM-E2E-071-edit-saving-state-klik-ganda-dan-save-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-234 | E2E | TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type | FE+BE |
| TC-FA-FAAM-235 | E2E | TC-FA-FAAM-E2E-237-multi-konteks-dua-edit-last-write-wins | FE+BE |
| TC-FA-FAAM-236 | E2E | TC-FA-FAAM-E2E-089-defense-in-depth-edit-request-langsung-plan-dan-excess | FE+BE |
| TC-FA-FAAM-237 | E2E | TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | FE+BE |
| TC-FA-FAAM-238 | E2E | TC-FA-FAAM-E2E-073-edit-dialog-change-category | FE+BE |
| TC-FA-FAAM-239 | E2E | TC-FA-FAAM-E2E-073-edit-dialog-change-category | FE+BE |
| TC-FA-FAAM-240 | E2E | TC-FA-FAAM-E2E-073-edit-dialog-change-category | FE+BE |
| TC-FA-FAAM-241 | E2E | TC-FA-FAAM-E2E-073-edit-dialog-change-category | FE+BE |
| TC-FA-FAAM-242 | E2E | TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil | FE+BE |
| TC-FA-FAAM-243 | E2E | TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil | FE+BE |
| TC-FA-FAAM-244 | E2E | TC-FA-FAAM-E2E-075-edit-dialog-change-default-label-save-dan-cancel | FE+BE |
| TC-FA-FAAM-245 | E2E | TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a | FE+BE |
| TC-FA-FAAM-246 | E2E | TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a | FE+BE |
| TC-FA-FAAM-247 | E2E | TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save | FE+BE |
| TC-FA-FAAM-248 | E2E | TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save | FE+BE |
| TC-FA-FAAM-249 | E2E | TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save | FE+BE |
| TC-FA-FAAM-250 | E2E | TC-FA-FAAM-E2E-078-edit-dialog-default-addon-cascade-save | FE+BE |
| TC-FA-FAAM-251 | E2E | TC-FA-FAAM-E2E-081-edit-dialog-berurutan-category-addon-label | FE+BE |
| TC-FA-FAAM-252 | E2E | TC-FA-FAAM-E2E-081-edit-dialog-berurutan-category-addon-label | FE+BE |
| TC-FA-FAAM-253 | E2E | TC-FA-FAAM-E2E-081-edit-dialog-berurutan-category-addon-label | FE+BE |
| TC-FA-FAAM-254 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-255 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-256 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-257 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-258 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-259 | E2E | TC-FA-FAAM-E2E-086-edit-blok-hapus-model-dan-brand-in-use | FE+BE |
| TC-FA-FAAM-260 | E2E | TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | FE+BE |
| TC-FA-FAAM-261 | E2E | TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | FE+BE |
| TC-FA-FAAM-262 | E2E | TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope | FE+BE |
| TC-FA-FAAM-263 | E2E | TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | FE+BE |
| TC-FA-FAAM-264 | E2E | TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | FE+BE |
| TC-FA-FAAM-265 | E2E | TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | FE+BE |
| TC-FA-FAAM-266 | E2E | TC-FA-FAAM-E2E-092-delete-single-dialog-cancel-dan-blok-in-use | FE+BE |
| TC-FA-FAAM-267 | E2E | TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope | FE+BE |
| TC-FA-FAAM-268 | E2E | TC-FA-FAAM-E2E-094-delete-single-race-dan-record-sudah-terhapus-single-dan-bulk | FE+BE |
| TC-FA-FAAM-269 | E2E | TC-FA-FAAM-E2E-094-delete-single-race-dan-record-sudah-terhapus-single-dan-bulk | FE+BE |
| TC-FA-FAAM-270 | E2E | TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx | FE+BE |
| TC-FA-FAAM-271 | E2E | TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope | FE+BE |
| TC-FA-FAAM-272 | E2E | TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | FE+BE |
| TC-FA-FAAM-273 | E2E | TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | FE+BE |
| TC-FA-FAAM-274 | E2E | TC-FA-FAAM-E2E-110-delete-single-halaman-terakhir-pindah-ke-halaman-sebelumnya | FE+BE |
| TC-FA-FAAM-275 | E2E | TC-FA-FAAM-E2E-093-delete-single-sukses-aset-deleted-disposed-dan-scope | FE+BE |
| TC-FA-FAAM-276 | E2E | TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header | FE+BE |
| TC-FA-FAAM-277 | E2E | TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header | FE+BE |
| TC-FA-FAAM-278 | E2E | TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header | FE+BE |
| TC-FA-FAAM-279 | E2E | TC-FA-FAAM-E2E-096-bulk-seleksi-lintas-halaman-select-all-dan-retensi | FE+BE |
| TC-FA-FAAM-280 | E2E | TC-FA-FAAM-E2E-096-bulk-seleksi-lintas-halaman-select-all-dan-retensi | FE+BE |
| TC-FA-FAAM-281 | E2E | TC-FA-FAAM-E2E-097-bulk-selection-limit-live-block-dan-auto-cap | FE+BE |
| TC-FA-FAAM-282 | E2E | TC-FA-FAAM-E2E-097-bulk-selection-limit-live-block-dan-auto-cap | FE+BE |
| TC-FA-FAAM-283 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-284 | E2E | TC-FA-FAAM-E2E-099-bulk-delete-sukses-homogen-continue-dan-klik-ganda | FE+BE |
| TC-FA-FAAM-285 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-286 | E2E | TC-FA-FAAM-E2E-099-bulk-delete-sukses-homogen-continue-dan-klik-ganda | FE+BE |
| TC-FA-FAAM-287 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-288 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-289 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-290 | E2E | TC-FA-FAAM-E2E-094-delete-single-race-dan-record-sudah-terhapus-single-dan-bulk | FE+BE |
| TC-FA-FAAM-291 | E2E | TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx | FE+BE |
| TC-FA-FAAM-292 | E2E | TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx | FE+BE |
| TC-FA-FAAM-293 | E2E | TC-FA-FAAM-E2E-100-resilience-delete-single-dan-bulk-5xx | FE+BE |
| TC-FA-FAAM-294 | E2E | TC-FA-FAAM-E2E-095-bulk-action-bar-seleksi-counter-dan-checkbox-header | FE+BE |
| TC-FA-FAAM-295 | E2E | TC-FA-FAAM-E2E-096-bulk-seleksi-lintas-halaman-select-all-dan-retensi | FE+BE |
| TC-FA-FAAM-296 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-297 | E2E | TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | FE+BE |
| TC-FA-FAAM-298 | E2E | TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | FE+BE |
| TC-FA-FAAM-299 | E2E | TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | FE+BE |
| TC-FA-FAAM-300 | E2E | TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | FE+BE |
| TC-FA-FAAM-301 | E2E | TC-FA-FAAM-E2E-019-mobile-seleksi-bulk-long-press | FE+BE |
| TC-FA-FAAM-302 | E2E | TC-FA-FAAM-E2E-101-popup-detail-screening-buka-dan-tutup | FE+BE |
| TC-FA-FAAM-303 | E2E | TC-FA-FAAM-E2E-101-popup-detail-screening-buka-dan-tutup | FE+BE |
| TC-FA-FAAM-304 | E2E | TC-FA-FAAM-E2E-101-popup-detail-screening-buka-dan-tutup | FE+BE |
| TC-FA-FAAM-305 | E2E | TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | FE+BE |
| TC-FA-FAAM-306 | E2E | TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | FE+BE |
| TC-FA-FAAM-307 | E2E | TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | FE+BE |
| TC-FA-FAAM-308 | E2E | TC-FA-FAAM-E2E-103-popup-detail-tautan-lintas-modul-dan-group-scope | FE+BE |
| TC-FA-FAAM-309 | E2E | TC-FA-FAAM-E2E-103-popup-detail-tautan-lintas-modul-dan-group-scope | FE+BE |
| TC-FA-FAAM-310 | E2E | TC-FA-FAAM-E2E-103-popup-detail-tautan-lintas-modul-dan-group-scope | FE+BE |
| TC-FA-FAAM-311 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-312 | E2E | TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | FE+BE |
| TC-FA-FAAM-313 | E2E | TC-FA-FAAM-E2E-102-popup-detail-isi-tab-badge-dan-empty-state | FE+BE |
| TC-FA-FAAM-314 | E2E | TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog | FE+BE |
| TC-FA-FAAM-315 | E2E | TC-FA-FAAM-E2E-104-popup-detail-retensi-state-tab-total-assets | FE+BE |
| TC-FA-FAAM-316 | E2E | TC-FA-FAAM-E2E-104-popup-detail-retensi-state-tab-total-assets | FE+BE |
| TC-FA-FAAM-317 | E2E | TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail | FE+BE |
| TC-FA-FAAM-318 | E2E | TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | FE+BE |
| TC-FA-FAAM-319 | E2E | TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | FE+BE |
| TC-FA-FAAM-320 | E2E | TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | FE+BE |
| TC-FA-FAAM-321 | E2E | TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | FE+BE |
| TC-FA-FAAM-322 | E2E | TC-FA-FAAM-E2E-107-tree-picker-screening-leaf-excess-dan-search | FE+BE |
| TC-FA-FAAM-323 | E2E | TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | FE+BE |
| TC-FA-FAAM-324 | E2E | TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | FE+BE |
| TC-FA-FAAM-325 | E2E | TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | FE+BE |
| TC-FA-FAAM-326 | E2E | TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | FE+BE |
| TC-FA-FAAM-327 | E2E | TC-FA-FAAM-E2E-108-tree-picker-client-kosong-cancel-select-urutan-dan-edit | FE+BE |
| TC-FA-FAAM-328 | E2E | TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail | FE+BE |
| TC-FA-FAAM-329 | E2E | TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka | FE+BE |
| TC-FA-FAAM-330 | E2E | TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka | FE+BE |
| TC-FA-FAAM-331 | E2E | TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka | FE+BE |
| TC-FA-FAAM-332 | E2E | TC-FA-FAAM-E2E-053-generator-code-token-pemisah-dan-angka | FE+BE |
| TC-FA-FAAM-333 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-334 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-335 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-336 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-337 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-338 | E2E | TC-FA-FAAM-E2E-055-generator-code-pada-edit | FE+BE |
| TC-FA-FAAM-339 | E2E | TC-FA-FAAM-E2E-055-generator-code-pada-edit | FE+BE |
| TC-FA-FAAM-340 | E2E | TC-FA-FAAM-E2E-055-generator-code-pada-edit | FE+BE |
| TC-FA-FAAM-341 | E2E | TC-FA-FAAM-E2E-055-generator-code-pada-edit | FE+BE |
| TC-FA-FAAM-342 | E2E | TC-FA-FAAM-E2E-054-generator-code-fallback-dedup-dan-batas-15 | FE+BE |
| TC-FA-FAAM-343 | E2E | TC-FA-FAAM-E2E-112-search-kelas-kolom-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-344 | E2E | TC-FA-FAAM-E2E-112-search-kelas-kolom-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-345 | E2E | TC-FA-FAAM-E2E-112-search-kelas-kolom-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-346 | E2E | TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | FE+BE |
| TC-FA-FAAM-347 | E2E | TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | FE+BE |
| TC-FA-FAAM-348 | E2E | TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | FE+BE |
| TC-FA-FAAM-349 | E2E | TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | FE+BE |
| TC-FA-FAAM-350 | E2E | TC-FA-FAAM-E2E-113-search-kelas-kolom-badge-total-asset-dan-modified-by | FE+BE |
| TC-FA-FAAM-351 | E2E | TC-FA-FAAM-E2E-114-search-kolom-hidden-karakter-khusus-dan-markup | FE+BE |
| TC-FA-FAAM-352 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-353 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-354 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-355 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-356 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-357 | E2E | TC-FA-FAAM-E2E-111-search-perilaku-box-enter-clear-dan-trim | FE+BE |
| TC-FA-FAAM-358 | E2E | TC-FA-FAAM-E2E-114-search-kolom-hidden-karakter-khusus-dan-markup | FE+BE |
| TC-FA-FAAM-359 | E2E | TC-FA-FAAM-E2E-114-search-kolom-hidden-karakter-khusus-dan-markup | FE+BE |
| TC-FA-FAAM-360 | E2E | TC-FA-FAAM-E2E-115-filter-screening-opsi-distinct-dan-kelas-category | FE+BE |
| TC-FA-FAAM-361 | E2E | TC-FA-FAAM-E2E-115-filter-screening-opsi-distinct-dan-kelas-category | FE+BE |
| TC-FA-FAAM-362 | E2E | TC-FA-FAAM-E2E-115-filter-screening-opsi-distinct-dan-kelas-category | FE+BE |
| TC-FA-FAAM-363 | E2E | TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | FE+BE |
| TC-FA-FAAM-364 | E2E | TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | FE+BE |
| TC-FA-FAAM-365 | E2E | TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | FE+BE |
| TC-FA-FAAM-366 | E2E | TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | FE+BE |
| TC-FA-FAAM-367 | E2E | TC-FA-FAAM-E2E-116-filter-kelas-tag-type-addon-label-total-asset-last-updated | FE+BE |
| TC-FA-FAAM-368 | E2E | TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | FE+BE |
| TC-FA-FAAM-369 | E2E | TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | FE+BE |
| TC-FA-FAAM-370 | E2E | TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | FE+BE |
| TC-FA-FAAM-371 | E2E | TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | FE+BE |
| TC-FA-FAAM-372 | E2E | TC-FA-FAAM-E2E-117-filter-or-and-chip-dan-search-dropdown | FE+BE |
| TC-FA-FAAM-373 | E2E | TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton | FE+BE |
| TC-FA-FAAM-374 | E2E | TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton | FE+BE |
| TC-FA-FAAM-375 | E2E | TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | FE+BE |
| TC-FA-FAAM-376 | E2E | TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | FE+BE |
| TC-FA-FAAM-377 | E2E | TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | FE+BE |
| TC-FA-FAAM-378 | E2E | TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | FE+BE |
| TC-FA-FAAM-379 | E2E | TC-FA-FAAM-E2E-118-filter-clear-field-discard-indikator-dan-apply | FE+BE |
| TC-FA-FAAM-380 | E2E | TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-FA-FAAM-381 | E2E | TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-FA-FAAM-382 | E2E | TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-FA-FAAM-383 | E2E | TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-FA-FAAM-384 | E2E | TC-FA-FAAM-E2E-120-kombinasi-search-filter-sort-dan-pagination | FE+BE |
| TC-FA-FAAM-385 | E2E | TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data | FE+BE |
| TC-FA-FAAM-386 | E2E | TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data | FE+BE |
| TC-FA-FAAM-387 | E2E | TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data | FE+BE |
| TC-FA-FAAM-388 | E2E | TC-FA-FAAM-E2E-121-kombinasi-search-filter-seleksi-dan-mutasi-data | FE+BE |
| TC-FA-FAAM-389 | E2E | TC-FA-FAAM-E2E-122-sort-kelas-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-390 | E2E | TC-FA-FAAM-E2E-122-sort-kelas-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-391 | E2E | TC-FA-FAAM-E2E-122-sort-kelas-teks-category-dan-tag-type | FE+BE |
| TC-FA-FAAM-392 | E2E | TC-FA-FAAM-E2E-123-sort-kelas-badge-addon-dan-total-asset | FE+BE |
| TC-FA-FAAM-393 | E2E | TC-FA-FAAM-E2E-123-sort-kelas-badge-addon-dan-total-asset | FE+BE |
| TC-FA-FAAM-394 | E2E | TC-FA-FAAM-E2E-123-sort-kelas-badge-addon-dan-total-asset | FE+BE |
| TC-FA-FAAM-395 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-396 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-397 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-398 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-399 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-400 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-401 | E2E | TC-FA-FAAM-E2E-124-sort-last-updated-modified-by-dan-urutan-badge | FE+BE |
| TC-FA-FAAM-402 | E2E | TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset | FE+BE |
| TC-FA-FAAM-403 | E2E | TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset | FE+BE |
| TC-FA-FAAM-404 | E2E | TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category | FE+BE |
| TC-FA-FAAM-405 | E2E | TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category | FE+BE |
| TC-FA-FAAM-406 | E2E | TC-FA-FAAM-E2E-146-setup-column-pin-asset-name-category-dan-total-asset-ceklis | FE+BE |
| TC-FA-FAAM-407 | E2E | TC-FA-FAAM-E2E-129-setup-column-kelas-teks-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-408 | E2E | TC-FA-FAAM-E2E-129-setup-column-kelas-teks-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-409 | E2E | TC-FA-FAAM-E2E-130-setup-column-kelas-teks-pin-dan-chip-ceklis | FE+BE |
| TC-FA-FAAM-410 | E2E | TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category | FE+BE |
| TC-FA-FAAM-411 | E2E | TC-FA-FAAM-E2E-126-setup-column-asset-name-dan-category | FE+BE |
| TC-FA-FAAM-412 | E2E | TC-FA-FAAM-E2E-146-setup-column-pin-asset-name-category-dan-total-asset-ceklis | FE+BE |
| TC-FA-FAAM-413 | E2E | TC-FA-FAAM-E2E-127-setup-column-tag-type-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAM-414 | E2E | TC-FA-FAAM-E2E-127-setup-column-tag-type-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAM-415 | E2E | TC-FA-FAAM-E2E-127-setup-column-tag-type-ceklis-geser-dan-pin | FE+BE |
| TC-FA-FAAM-416 | E2E | TC-FA-FAAM-E2E-130-setup-column-kelas-teks-pin-dan-chip-ceklis | FE+BE |
| TC-FA-FAAM-417 | E2E | TC-FA-FAAM-E2E-131-setup-column-kelas-chip-geser-dan-pin | FE+BE |
| TC-FA-FAAM-418 | E2E | TC-FA-FAAM-E2E-131-setup-column-kelas-chip-geser-dan-pin | FE+BE |
| TC-FA-FAAM-419 | E2E | TC-FA-FAAM-E2E-146-setup-column-pin-asset-name-category-dan-total-asset-ceklis | FE+BE |
| TC-FA-FAAM-420 | E2E | TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-421 | E2E | TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-422 | E2E | TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-423 | E2E | TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-424 | E2E | TC-FA-FAAM-E2E-128-setup-column-total-asset-geser-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-425 | E2E | TC-FA-FAAM-E2E-145-setup-column-guard-satu-kolom-batas-pin-dan-reset-to-default | FE+BE |
| TC-FA-FAAM-426 | E2E | TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset | FE+BE |
| TC-FA-FAAM-427 | E2E | TC-FA-FAAM-E2E-145-setup-column-guard-satu-kolom-batas-pin-dan-reset-to-default | FE+BE |
| TC-FA-FAAM-428 | E2E | TC-FA-FAAM-E2E-145-setup-column-guard-satu-kolom-batas-pin-dan-reset-to-default | FE+BE |
| TC-FA-FAAM-429 | E2E | TC-FA-FAAM-E2E-125-setup-column-overlay-popup-guard-dan-reset | FE+BE |
| TC-FA-FAAM-430 | E2E | TC-FA-FAAM-E2E-132-setup-column-independen-filter-bertahan-dan-viewport | FE+BE |
| TC-FA-FAAM-431 | E2E | TC-FA-FAAM-E2E-132-setup-column-independen-filter-bertahan-dan-viewport | FE+BE |
| TC-FA-FAAM-432 | E2E | TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | FE+BE |
| TC-FA-FAAM-433 | E2E | TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | FE+BE |
| TC-FA-FAAM-434 | E2E | TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | FE+BE |
| TC-FA-FAAM-435 | E2E | TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | FE+BE |
| TC-FA-FAAM-436 | E2E | TC-FA-FAAM-E2E-133-paginasi-default-navigasi-dan-nomor-halaman | FE+BE |
| TC-FA-FAAM-437 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-438 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-439 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-440 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-441 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-442 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-443 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-444 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-445 | E2E | TC-FA-FAAM-E2E-134-tooltip-hover-dan-popover-more-tabel-utama | FE+BE |
| TC-FA-FAAM-446 | E2E | TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | FE+BE |
| TC-FA-FAAM-447 | E2E | TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | FE+BE |
| TC-FA-FAAM-448 | E2E | TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | FE+BE |
| TC-FA-FAAM-449 | E2E | TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | FE+BE |
| TC-FA-FAAM-450 | E2E | TC-FA-FAAM-E2E-140-download-isi-berkas-teks-category-tag-type | FE+BE |
| TC-FA-FAAM-451 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
| TC-FA-FAAM-452 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
| TC-FA-FAAM-453 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
| TC-FA-FAAM-454 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
| TC-FA-FAAM-455 | E2E | TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | FE+BE |
| TC-FA-FAAM-456 | E2E | TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | FE+BE |
| TC-FA-FAAM-457 | E2E | TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | FE+BE |
| TC-FA-FAAM-458 | E2E | TC-FA-FAAM-E2E-144-resilience-download-gagal-list-changelog-total-assets | FE+BE |
| TC-FA-FAAM-459 | E2E | TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | FE+BE |
| TC-FA-FAAM-460 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
| TC-FA-FAAM-461 | E2E | TC-FA-FAAM-E2E-143-download-lebih-dari-5000-baris | FE+BE |
| TC-FA-FAAM-462 | E2E | TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | FE+BE |
| TC-FA-FAAM-463 | E2E | TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | FE+BE |
| TC-FA-FAAM-464 | E2E | TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | FE+BE |
| TC-FA-FAAM-465 | E2E | TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | FE+BE |
| TC-FA-FAAM-466 | E2E | TC-FA-FAAM-E2E-165-changelog-empty-state-client-tanpa-entri | FE+BE |
| TC-FA-FAAM-467 | E2E | TC-FA-FAAM-E2E-147-changelog-screening-tutup-format-kolom-dan-empty-state | FE+BE |
| TC-FA-FAAM-468 | E2E | TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog | FE+BE |
| TC-FA-FAAM-469 | E2E | TC-FA-FAAM-E2E-157-changelog-snapshot-rename-dan-format-tanggal | FE+BE |
| TC-FA-FAAM-470 | E2E | TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | FE+BE |
| TC-FA-FAAM-471 | E2E | TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | FE+BE |
| TC-FA-FAAM-472 | E2E | TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | FE+BE |
| TC-FA-FAAM-473 | E2E | TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | FE+BE |
| TC-FA-FAAM-474 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-475 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-476 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-477 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-478 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-479 | E2E | TC-FA-FAAM-E2E-149-changelog-filter-panel-date-range-dan-dropdown | FE+BE |
| TC-FA-FAAM-480 | E2E | TC-FA-FAAM-E2E-150-changelog-sort-kelas-kolom | FE+BE |
| TC-FA-FAAM-481 | E2E | TC-FA-FAAM-E2E-164-changelog-sort-kelas-action-asset-name-dan-field | FE+BE |
| TC-FA-FAAM-482 | E2E | TC-FA-FAAM-E2E-150-changelog-sort-kelas-kolom | FE+BE |
| TC-FA-FAAM-483 | E2E | TC-FA-FAAM-E2E-150-changelog-sort-kelas-kolom | FE+BE |
| TC-FA-FAAM-484 | E2E | TC-FA-FAAM-E2E-151-changelog-setup-column-kelas-date | FE+BE |
| TC-FA-FAAM-485 | E2E | TC-FA-FAAM-E2E-151-changelog-setup-column-kelas-date | FE+BE |
| TC-FA-FAAM-486 | E2E | TC-FA-FAAM-E2E-151-changelog-setup-column-kelas-date | FE+BE |
| TC-FA-FAAM-487 | E2E | TC-FA-FAAM-E2E-153-changelog-setup-column-kelas-teks-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-488 | E2E | TC-FA-FAAM-E2E-153-changelog-setup-column-kelas-teks-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-489 | E2E | TC-FA-FAAM-E2E-154-changelog-setup-column-pin-dan-screening-popup | FE+BE |
| TC-FA-FAAM-490 | E2E | TC-FA-FAAM-E2E-152-changelog-setup-column-kelas-modified-by | FE+BE |
| TC-FA-FAAM-491 | E2E | TC-FA-FAAM-E2E-152-changelog-setup-column-kelas-modified-by | FE+BE |
| TC-FA-FAAM-492 | E2E | TC-FA-FAAM-E2E-152-changelog-setup-column-kelas-modified-by | FE+BE |
| TC-FA-FAAM-493 | E2E | TC-FA-FAAM-E2E-154-changelog-setup-column-pin-dan-screening-popup | FE+BE |
| TC-FA-FAAM-494 | E2E | TC-FA-FAAM-E2E-155-changelog-setup-column-reset-independen-dan-paginasi | FE+BE |
| TC-FA-FAAM-495 | E2E | TC-FA-FAAM-E2E-155-changelog-setup-column-reset-independen-dan-paginasi | FE+BE |
| TC-FA-FAAM-496 | E2E | TC-FA-FAAM-E2E-155-changelog-setup-column-reset-independen-dan-paginasi | FE+BE |
| TC-FA-FAAM-497 | E2E | TC-FA-FAAM-E2E-156-changelog-download-nama-berkas-format-dan-isi | FE+BE |
| TC-FA-FAAM-498 | E2E | TC-FA-FAAM-E2E-144-resilience-download-gagal-list-changelog-total-assets | FE+BE |
| TC-FA-FAAM-499 | E2E | TC-FA-FAAM-E2E-156-changelog-download-nama-berkas-format-dan-isi | FE+BE |
| TC-FA-FAAM-500 | E2E | TC-FA-FAAM-E2E-157-changelog-snapshot-rename-dan-format-tanggal | FE+BE |
| TC-FA-FAAM-501 | E2E | TC-FA-FAAM-E2E-166-total-assets-screening-format-sel-himpunan-dan-status | FE+BE |
| TC-FA-FAAM-502 | E2E | TC-FA-FAAM-E2E-166-total-assets-screening-format-sel-himpunan-dan-status | FE+BE |
| TC-FA-FAAM-503 | E2E | TC-FA-FAAM-E2E-210-total-assets-himpunan-aset-dan-empty-state-tanpa-aset | FE+BE |
| TC-FA-FAAM-504 | E2E | TC-FA-FAAM-E2E-166-total-assets-screening-format-sel-himpunan-dan-status | FE+BE |
| TC-FA-FAAM-505 | E2E | TC-FA-FAAM-E2E-210-total-assets-himpunan-aset-dan-empty-state-tanpa-aset | FE+BE |
| TC-FA-FAAM-506 | E2E | TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | FE+BE |
| TC-FA-FAAM-507 | E2E | TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | FE+BE |
| TC-FA-FAAM-508 | E2E | TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | FE+BE |
| TC-FA-FAAM-509 | E2E | TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | FE+BE |
| TC-FA-FAAM-510 | E2E | TC-FA-FAAM-E2E-168-total-assets-search-dasar-name-brand-group-dan-status | FE+BE |
| TC-FA-FAAM-511 | E2E | TC-FA-FAAM-E2E-172-total-assets-filter-screening-brand-model-group | FE+BE |
| TC-FA-FAAM-512 | E2E | TC-FA-FAAM-E2E-172-total-assets-filter-screening-brand-model-group | FE+BE |
| TC-FA-FAAM-513 | E2E | TC-FA-FAAM-E2E-172-total-assets-filter-screening-brand-model-group | FE+BE |
| TC-FA-FAAM-514 | E2E | TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and | FE+BE |
| TC-FA-FAAM-515 | E2E | TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and | FE+BE |
| TC-FA-FAAM-516 | E2E | TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and | FE+BE |
| TC-FA-FAAM-517 | E2E | TC-FA-FAAM-E2E-176-total-assets-sort-name-asset-id-dan-brand-model-group | FE+BE |
| TC-FA-FAAM-518 | E2E | TC-FA-FAAM-E2E-176-total-assets-sort-name-asset-id-dan-brand-model-group | FE+BE |
| TC-FA-FAAM-519 | E2E | TC-FA-FAAM-E2E-176-total-assets-sort-name-asset-id-dan-brand-model-group | FE+BE |
| TC-FA-FAAM-520 | E2E | TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag | FE+BE |
| TC-FA-FAAM-521 | E2E | TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag | FE+BE |
| TC-FA-FAAM-522 | E2E | TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi | FE+BE |
| TC-FA-FAAM-523 | E2E | TC-FA-FAAM-E2E-179-total-assets-download-scope-status-dan-label | FE+BE |
| TC-FA-FAAM-524 | E2E | TC-FA-FAAM-E2E-144-resilience-download-gagal-list-changelog-total-assets | FE+BE |
| TC-FA-FAAM-525 | E2E | TC-FA-FAAM-E2E-179-total-assets-download-scope-status-dan-label | FE+BE |
| TC-FA-FAAM-526 | E2E | TC-FA-FAAM-E2E-182-total-assets-setup-column-screening-reset-dan-search-hidden | FE+BE |
| TC-FA-FAAM-527 | E2E | TC-FA-FAAM-E2E-182-total-assets-setup-column-screening-reset-dan-search-hidden | FE+BE |
| TC-FA-FAAM-528 | E2E | TC-FA-FAAM-E2E-183-total-assets-setup-column-name-asset-id-ceklis-geser-pin | FE+BE |
| TC-FA-FAAM-529 | E2E | TC-FA-FAAM-E2E-183-total-assets-setup-column-name-asset-id-ceklis-geser-pin | FE+BE |
| TC-FA-FAAM-530 | E2E | TC-FA-FAAM-E2E-183-total-assets-setup-column-name-asset-id-ceklis-geser-pin | FE+BE |
| TC-FA-FAAM-531 | E2E | TC-FA-FAAM-E2E-184-total-assets-setup-column-badge-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-532 | E2E | TC-FA-FAAM-E2E-184-total-assets-setup-column-badge-ceklis-dan-geser | FE+BE |
| TC-FA-FAAM-533 | E2E | TC-FA-FAAM-E2E-185-total-assets-setup-column-badge-pin-dan-status | FE+BE |
| TC-FA-FAAM-534 | E2E | TC-FA-FAAM-E2E-185-total-assets-setup-column-badge-pin-dan-status | FE+BE |
| TC-FA-FAAM-535 | E2E | TC-FA-FAAM-E2E-185-total-assets-setup-column-badge-pin-dan-status | FE+BE |
| TC-FA-FAAM-536 | E2E | TC-FA-FAAM-E2E-186-total-assets-setup-column-status-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-537 | E2E | TC-FA-FAAM-E2E-186-total-assets-setup-column-status-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-538 | E2E | TC-FA-FAAM-E2E-186-total-assets-setup-column-status-pin-dan-last-updated | FE+BE |
| TC-FA-FAAM-539 | E2E | TC-FA-FAAM-E2E-187-total-assets-setup-column-last-updated-pin-dan-label-ceklis | FE+BE |
| TC-FA-FAAM-540 | E2E | TC-FA-FAAM-E2E-182-total-assets-setup-column-screening-reset-dan-search-hidden | FE+BE |
| TC-FA-FAAM-541 | E2E | TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal | FE+BE |
| TC-FA-FAAM-542 | E2E | TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | FE+BE |
| TC-FA-FAAM-543 | E2E | TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | FE+BE |
| TC-FA-FAAM-544 | E2E | TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | FE+BE |
| TC-FA-FAAM-545 | E2E | TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | FE+BE |
| TC-FA-FAAM-546 | E2E | TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort | FE+BE |
| TC-FA-FAAM-547 | E2E | TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort | FE+BE |
| TC-FA-FAAM-548 | E2E | TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort | FE+BE |
| TC-FA-FAAM-549 | E2E | TC-FA-FAAM-E2E-159-tab-linked-custom-fields-screening-dan-sort | FE+BE |
| TC-FA-FAAM-550 | E2E | TC-FA-FAAM-E2E-160-tab-linked-custom-fields-tautan-dan-penambahan-scope | FE+BE |
| TC-FA-FAAM-551 | E2E | TC-FA-FAAM-E2E-160-tab-linked-custom-fields-tautan-dan-penambahan-scope | FE+BE |
| TC-FA-FAAM-552 | E2E | TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand | FE+BE |
| TC-FA-FAAM-553 | E2E | TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand | FE+BE |
| TC-FA-FAAM-554 | E2E | TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand | FE+BE |
| TC-FA-FAAM-555 | E2E | TC-FA-FAAM-E2E-161-setup-column-tab-models-per-brand | FE+BE |
| TC-FA-FAAM-556 | E2E | TC-FA-FAAM-E2E-162-setup-column-tab-linked-custom-fields-ceklis | FE+BE |
| TC-FA-FAAM-557 | E2E | TC-FA-FAAM-E2E-162-setup-column-tab-linked-custom-fields-ceklis | FE+BE |
| TC-FA-FAAM-558 | E2E | TC-FA-FAAM-E2E-163-setup-column-tab-linked-custom-fields-geser-dan-pin | FE+BE |
| TC-FA-FAAM-559 | E2E | TC-FA-FAAM-E2E-163-setup-column-tab-linked-custom-fields-geser-dan-pin | FE+BE |
| TC-FA-FAAM-560 | E2E | TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | FE+BE |
| TC-FA-FAAM-561 | E2E | TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | FE+BE |
| TC-FA-FAAM-562 | E2E | TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | FE+BE |
| TC-FA-FAAM-563 | E2E | TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | FE+BE |
| TC-FA-FAAM-564 | E2E | TC-FA-FAAM-E2E-212-changelog-edit-field-asset-name-code-category-tag-type-brand | FE+BE |
| TC-FA-FAAM-565 | E2E | TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | FE+BE |
| TC-FA-FAAM-566 | E2E | TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | FE+BE |
| TC-FA-FAAM-567 | E2E | TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | FE+BE |
| TC-FA-FAAM-568 | E2E | TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | FE+BE |
| TC-FA-FAAM-569 | E2E | TC-FA-FAAM-E2E-213-changelog-edit-field-model-uom-addon-label-dan-brand-dilepas | FE+BE |
| TC-FA-FAAM-570 | E2E | TC-FA-FAAM-E2E-214-changelog-edit-beberapa-field-multi-nilai-dan-isolasi | FE+BE |
| TC-FA-FAAM-571 | E2E | TC-FA-FAAM-E2E-214-changelog-edit-beberapa-field-multi-nilai-dan-isolasi | FE+BE |
| TC-FA-FAAM-572 | E2E | TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi | FE+BE |
| TC-FA-FAAM-573 | E2E | TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi | FE+BE |
| TC-FA-FAAM-574 | E2E | TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi | FE+BE |
| TC-FA-FAAM-575 | E2E | TC-FA-FAAM-E2E-216-pencatatan-absence-tanpa-baris-log | FE+BE |
| TC-FA-FAAM-576 | E2E | TC-FA-FAAM-E2E-240-pencatatan-absence-tiga-surface-log | FE+BE |
| TC-FA-FAAM-577 | E2E | TC-FA-FAAM-E2E-240-pencatatan-absence-tiga-surface-log | FE+BE |
| TC-FA-FAAM-578 | E2E | TC-FA-FAAM-E2E-219-log-import-dan-modified-by-last-updated-mengikuti-changelog | FE+BE |
| TC-FA-FAAM-579 | E2E | TC-FA-FAAM-E2E-217-log-system-activity-create-dan-aksi-aktor | FE+BE |
| TC-FA-FAAM-580 | E2E | TC-FA-FAAM-E2E-217-log-system-activity-create-dan-aksi-aktor | FE+BE |
| TC-FA-FAAM-581 | E2E | TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron | FE+BE |
| TC-FA-FAAM-582 | E2E | TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron | FE+BE |
| TC-FA-FAAM-583 | E2E | TC-FA-FAAM-E2E-215-changelog-create-delete-bulk-dan-filter-opsi | FE+BE |
| TC-FA-FAAM-584 | E2E | TC-FA-FAAM-E2E-219-log-import-dan-modified-by-last-updated-mengikuti-changelog | FE+BE |
| TC-FA-FAAM-585 | E2E | TC-FA-FAAM-E2E-239-changelog-opsi-filter-field-dan-action | FE+BE |
| TC-FA-FAAM-586 | E2E | TC-FA-FAAM-E2E-239-changelog-opsi-filter-field-dan-action | FE+BE |
| TC-FA-FAAM-587 | E2E | TC-FA-FAAM-E2E-214-changelog-edit-beberapa-field-multi-nilai-dan-isolasi | FE+BE |
| TC-FA-FAAM-588 | E2E | TC-FA-FAAM-E2E-216-pencatatan-absence-tanpa-baris-log | FE+BE |
| TC-FA-FAAM-589 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-590 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-591 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-592 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-593 | E2E | TC-FA-FAAM-E2E-216-pencatatan-absence-tanpa-baris-log | FE+BE |
| TC-FA-FAAM-594 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-595 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-596 | E2E | TC-FA-FAAM-E2E-220-sinkron-rename-dan-blok-delete-master-data-lintas-modul | FE+BE |
| TC-FA-FAAM-597 | E2E | TC-FA-FAAM-E2E-241-sinkron-category-locked-live-subcategory | FE+BE |
| TC-FA-FAAM-598 | E2E | TC-FA-FAAM-E2E-222-sinkron-registrasi-aset-dropdown-asset-name-dan-excess | FE+BE |
| TC-FA-FAAM-599 | E2E | TC-FA-FAAM-E2E-222-sinkron-registrasi-aset-dropdown-asset-name-dan-excess | FE+BE |
| TC-FA-FAAM-600 | E2E | TC-FA-FAAM-E2E-221-sinkron-locked-live-custom-id-scope-dan-cascade-aset | FE+BE |
| TC-FA-FAAM-601 | E2E | TC-FA-FAAM-E2E-221-sinkron-locked-live-custom-id-scope-dan-cascade-aset | FE+BE |
| TC-FA-FAAM-602 | E2E | TC-FA-FAAM-E2E-242-sinkron-cascade-category-ke-aset-dan-lisensi-addon | FE+BE |
| TC-FA-FAAM-603 | E2E | TC-FA-FAAM-E2E-221-sinkron-locked-live-custom-id-scope-dan-cascade-aset | FE+BE |
| TC-FA-FAAM-604 | E2E | TC-FA-FAAM-E2E-223-paritas-import-edit-dan-delete-asset-name | FE+BE |
| TC-FA-FAAM-605 | E2E | TC-FA-FAAM-E2E-223-paritas-import-edit-dan-delete-asset-name | FE+BE |
| TC-FA-FAAM-606 | E2E | TC-FA-FAAM-E2E-224-import-kuota-paket-dan-penyemaian-policy | FE+BE |
| TC-FA-FAAM-607 | E2E | TC-FA-FAAM-E2E-225-format-tanggal-zona-waktu-general-settings | FE+BE |
| TC-FA-FAAM-608 | E2E | TC-FA-FAAM-E2E-225-format-tanggal-zona-waktu-general-settings | FE+BE |
| TC-FA-FAAM-609 | E2E | TC-FA-FAAM-E2E-242-sinkron-cascade-category-ke-aset-dan-lisensi-addon | FE+BE |
| TC-FA-FAAM-610 | E2E | TC-FA-FAAM-E2E-234-state-tenant-pembacaan-tetap-berfungsi-dan-transisi-addon | FE+BE |
| TC-FA-FAAM-611 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-611 | E2E | TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak | FE+BE |
| TC-FA-FAAM-612 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-612 | E2E | TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak | FE+BE |
| TC-FA-FAAM-613 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-613 | E2E | TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak | FE+BE |
| TC-FA-FAAM-614 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-614 | E2E | TC-FA-FAAM-E2E-247-pencatatan-absence-request-langsung-ditolak | FE+BE |
| TC-FA-FAAM-615 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-616 | E2E | TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server | FE+BE |
| TC-FA-FAAM-617 | E2E | TC-FA-FAAM-E2E-009-role-matrix-negatif-tanpa-role-dan-hak-dicabut | FE+BE |
| TC-FA-FAAM-618 | E2E | TC-FA-FAAM-E2E-009-role-matrix-negatif-tanpa-role-dan-hak-dicabut | FE+BE |
| TC-FA-FAAM-619 | E2E | TC-FA-FAAM-E2E-233-state-tenant-suspended-expired-aksi-tulis-ditolak | FE+BE |
| TC-FA-FAAM-620 | E2E | TC-FA-FAAM-E2E-233-state-tenant-suspended-expired-aksi-tulis-ditolak | FE+BE |
| TC-FA-FAAM-621 | E2E | TC-FA-FAAM-E2E-250-state-tenant-suspended-expired-delete-bulk-dan-import-ditolak | FE+BE |
| TC-FA-FAAM-622 | E2E | TC-FA-FAAM-E2E-250-state-tenant-suspended-expired-delete-bulk-dan-import-ditolak | FE+BE |
| TC-FA-FAAM-623 | E2E | TC-FA-FAAM-E2E-250-state-tenant-suspended-expired-delete-bulk-dan-import-ditolak | FE+BE |
| TC-FA-FAAM-624 | E2E | TC-FA-FAAM-E2E-234-state-tenant-pembacaan-tetap-berfungsi-dan-transisi-addon | FE+BE |
| TC-FA-FAAM-625 | E2E | TC-FA-FAAM-E2E-232-defense-in-depth-payload-dan-aturan-server | FE+BE |
| TC-FA-FAAM-626 | E2E | TC-FA-FAAM-E2E-232-defense-in-depth-payload-dan-aturan-server | FE+BE |
| TC-FA-FAAM-627 | E2E | TC-FA-FAAM-E2E-232-defense-in-depth-payload-dan-aturan-server | FE+BE |
| TC-FA-FAAM-628 | E2E | TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | FE+BE |
| TC-FA-FAAM-629 | E2E | TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | FE+BE |
| TC-FA-FAAM-630 | E2E | TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | FE+BE |
| TC-FA-FAAM-631 | E2E | TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | FE+BE |
| TC-FA-FAAM-632 | E2E | TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server | FE+BE |
| TC-FA-FAAM-633 | E2E | TC-FA-FAAM-E2E-235-multi-konteks-dua-create-bersamaan | FE+BE |
| TC-FA-FAAM-634 | E2E | TC-FA-FAAM-E2E-235-multi-konteks-dua-create-bersamaan | FE+BE |
| TC-FA-FAAM-635 | E2E | TC-FA-FAAM-E2E-249-multi-konteks-dua-create-slot-kuota-dan-ceiling | FE+BE |
| TC-FA-FAAM-636 | E2E | TC-FA-FAAM-E2E-249-multi-konteks-dua-create-slot-kuota-dan-ceiling | FE+BE |
| TC-FA-FAAM-637 | E2E | TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan | FE+BE |
| TC-FA-FAAM-638 | E2E | TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan | FE+BE |
| TC-FA-FAAM-639 | E2E | TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan | FE+BE |
| TC-FA-FAAM-640 | E2E | TC-FA-FAAM-E2E-236-multi-konteks-edit-delete-bulk-kategori-bersamaan | FE+BE |
| TC-FA-FAAM-641 | E2E | TC-FA-FAAM-E2E-237-multi-konteks-dua-edit-last-write-wins | FE+BE |
| TC-FA-FAAM-642 | E2E | TC-FA-FAAM-E2E-237-multi-konteks-dua-edit-last-write-wins | FE+BE |
| TC-FA-FAAM-643 | E2E | TC-FA-FAAM-E2E-007-propagasi-perubahan-sesi-lain-ke-list-dan-modal | FE+BE |
| TC-FA-FAAM-644 | E2E | TC-FA-FAAM-E2E-017-resilience-baca-list-detail-changelog | FE+BE |
| TC-FA-FAAM-645 | E2E | TC-FA-FAAM-E2E-021-excess-create-diblokir-sampai-jumlah-di-bawah-cap | FE+BE |
| TC-FA-FAAM-646 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-647 | E2E | TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-648 | E2E | TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-649 | E2E | TC-FA-FAAM-E2E-085-edit-dialog-change-tag-type-save-dan-aset-baru | FE+BE |
| TC-FA-FAAM-650 | E2E | TC-FA-FAAM-E2E-083-edit-dialog-change-tag-type-cancel-esc-dan-non-tag | FE+BE |
| TC-FA-FAAM-651 | E2E | TC-FA-FAAM-E2E-083-edit-dialog-change-tag-type-cancel-esc-dan-non-tag | FE+BE |
| TC-FA-FAAM-652 | E2E | TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-653 | E2E | TC-FA-FAAM-E2E-082-edit-dialog-change-tag-type-tampil-dan-tanpa-perubahan | FE+BE |
| TC-FA-FAAM-654 | E2E | TC-FA-FAAM-E2E-090-edit-dialog-dampak-non-tag-dan-empat-dialog-berurutan | FE+BE |
| TC-FA-FAAM-655 | E2E | TC-FA-FAAM-E2E-083-edit-dialog-change-tag-type-cancel-esc-dan-non-tag | FE+BE |
| TC-FA-FAAM-656 | E2E | TC-FA-FAAM-E2E-090-edit-dialog-dampak-non-tag-dan-empat-dialog-berurutan | FE+BE |
| TC-FA-FAAM-657 | E2E | TC-FA-FAAM-E2E-084-edit-dialog-dampak-hanya-field-berubah-dan-cancel-berantai | FE+BE |
| TC-FA-FAAM-658 | E2E | TC-FA-FAAM-E2E-084-edit-dialog-dampak-hanya-field-berubah-dan-cancel-berantai | FE+BE |
| TC-FA-FAAM-659 | E2E | TC-FA-FAAM-E2E-085-edit-dialog-change-tag-type-save-dan-aset-baru | FE+BE |
| TC-FA-FAAM-660 | E2E | TC-FA-FAAM-E2E-087-resilience-edit-5xx-timeout-tabrakan-code-dan-save-tag-type | FE+BE |
| TC-FA-FAAM-664 | E2E | TC-FA-FAAM-E2E-229-tag-type-tanpa-aset-dan-progres-kepatuhan-berubah | FE+BE |
| TC-FA-FAAM-665 | E2E | TC-FA-FAAM-E2E-228-tag-type-non-standard-di-tag-dan-cancel-dialog | FE+BE |
| TC-FA-FAAM-666 | E2E | TC-FA-FAAM-E2E-173-total-assets-filter-status-last-updated-dan-and | FE+BE |
| TC-FA-FAAM-667 | E2E | TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi | FE+BE |
| TC-FA-FAAM-668 | E2E | TC-FA-FAAM-E2E-158-tab-models-per-brand-screening-sort-no-model-dan-hover | FE+BE |
| TC-FA-FAAM-669 | E2E | TC-FA-FAAM-E2E-132-setup-column-independen-filter-bertahan-dan-viewport | FE+BE |
| TC-FA-FAAM-670 | E2E | TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | FE+BE |
| TC-FA-FAAM-671 | E2E | TC-FA-FAAM-E2E-059-edit-penutupan-form-unsaved-changes-dan-esc | FE+BE |
| TC-FA-FAAM-672 | E2E | TC-FA-FAAM-E2E-098-bulk-delete-dialog-homogen-campuran-blok-dan-cancel | FE+BE |
| TC-FA-FAAM-673 | E2E | TC-FA-FAAM-E2E-099-bulk-delete-sukses-homogen-continue-dan-klik-ganda | FE+BE |
| TC-FA-FAAM-674 | E2E | TC-FA-FAAM-E2E-238-plan-tier-tanpa-gating-empat-plan | FE+BE |
| TC-FA-FAAM-675 | E2E | TC-FA-FAAM-E2E-243-sinkron-registrasi-aset-asset-name-menjadi-excess | FE+BE |
| TC-FA-FAAM-676 | E2E | TC-FA-FAAM-E2E-048-create-ceiling-satu-di-bawah-race-dan-per-katalog | FE+BE |
| TC-FA-FAAM-677 | E2E | TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | FE+BE |
| TC-FA-FAAM-678 | E2E | TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a | FE+BE |
| TC-FA-FAAM-679 | E2E | TC-FA-FAAM-E2E-076-edit-dialog-change-default-addon-tampil-a | FE+BE |
| TC-FA-FAAM-680 | E2E | TC-FA-FAAM-E2E-077-edit-dialog-change-default-addon-tampil-b | FE+BE |
| TC-FA-FAAM-681 | E2E | TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil | FE+BE |
| TC-FA-FAAM-682 | E2E | TC-FA-FAAM-E2E-074-edit-dialog-change-default-label-tampil | FE+BE |
| TC-FA-FAAM-683 | E2E | TC-FA-FAAM-E2E-050-create-rate-limit-cek-keunikan-429 | FE+BE |
| TC-FA-FAAM-684 | E2E | TC-FA-FAAM-E2E-088-defense-in-depth-edit-request-langsung-validasi | FE+BE |
| TC-FA-FAAM-685 | E2E | TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi | FE+BE |
| TC-FA-FAAM-686 | E2E | TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | FE+BE |
| TC-FA-FAAM-687 | E2E | TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | FE+BE |
| TC-FA-FAAM-688 | E2E | TC-FA-FAAM-E2E-138-notice-category-locked-bentuk-tunggal | FE+BE |
| TC-FA-FAAM-689 | E2E | TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol | FE+BE |
| TC-FA-FAAM-690 | E2E | TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | FE+BE |
| TC-FA-FAAM-691 | E2E | TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | FE+BE |
| TC-FA-FAAM-692 | E2E | TC-FA-FAAM-E2E-138-notice-category-locked-bentuk-tunggal | FE+BE |
| TC-FA-FAAM-693 | E2E | TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | FE+BE |
| TC-FA-FAAM-694 | E2E | TC-FA-FAAM-E2E-135-notice-category-locked-show-only-dan-chip | FE+BE |
| TC-FA-FAAM-695 | E2E | TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan | FE+BE |
| TC-FA-FAAM-696 | E2E | TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan | FE+BE |
| TC-FA-FAAM-697 | E2E | TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | FE+BE |
| TC-FA-FAAM-698 | E2E | TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | FE+BE |
| TC-FA-FAAM-699 | E2E | TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | FE+BE |
| TC-FA-FAAM-700 | E2E | TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | FE+BE |
| TC-FA-FAAM-701 | E2E | TC-FA-FAAM-E2E-142-download-cakupan-nama-berkas-kolom-dan-quick-filter | FE+BE |
| TC-FA-FAAM-702 | E2E | TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan | FE+BE |
| TC-FA-FAAM-703 | E2E | TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol | FE+BE |
| TC-FA-FAAM-704 | E2E | TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol | FE+BE |
| TC-FA-FAAM-705 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-706 | E2E | TC-FA-FAAM-E2E-018-mobile-list-card-bottom-sheet-toolbar-dan-notice | FE+BE |
| TC-FA-FAAM-707 | E2E | TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil | FE+BE |
| TC-FA-FAAM-708 | E2E | TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil | FE+BE |
| TC-FA-FAAM-709 | E2E | TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil | FE+BE |
| TC-FA-FAAM-710 | E2E | TC-FA-FAAM-E2E-079-edit-dialog-d10-tidak-tampil | FE+BE |
| TC-FA-FAAM-711 | E2E | TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal | FE+BE |
| TC-FA-FAAM-712 | E2E | TC-FA-FAAM-E2E-174-total-assets-filter-label-tag-dan-measurement | FE+BE |
| TC-FA-FAAM-713 | E2E | TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag | FE+BE |
| TC-FA-FAAM-714 | E2E | TC-FA-FAAM-E2E-187-total-assets-setup-column-last-updated-pin-dan-label-ceklis | FE+BE |
| TC-FA-FAAM-715 | E2E | TC-FA-FAAM-E2E-188-total-assets-setup-column-label-geser-pin-dan-tag | FE+BE |
| TC-FA-FAAM-716 | E2E | TC-FA-FAAM-E2E-188-total-assets-setup-column-label-geser-pin-dan-tag | FE+BE |
| TC-FA-FAAM-717 | E2E | TC-FA-FAAM-E2E-167-total-assets-hover-strip-kolom-label-dan-paginasi | FE+BE |
| TC-FA-FAAM-718 | E2E | TC-FA-FAAM-E2E-179-total-assets-download-scope-status-dan-label | FE+BE |
| TC-FA-FAAM-719 | E2E | TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | FE+BE |
| TC-FA-FAAM-720 | E2E | TC-FA-FAAM-E2E-077-edit-dialog-change-default-addon-tampil-b | FE+BE |
| TC-FA-FAAM-721 | E2E | TC-FA-FAAM-E2E-077-edit-dialog-change-default-addon-tampil-b | FE+BE |
| TC-FA-FAAM-722 | E2E | TC-FA-FAAM-E2E-227-transisi-otomatis-default-addon-eventual-60-detik | FE+BE |
| TC-FA-FAAM-723 | E2E | TC-FA-FAAM-E2E-227-transisi-otomatis-default-addon-eventual-60-detik | FE+BE |
| TC-FA-FAAM-724 | E2E | TC-FA-FAAM-E2E-136-notice-category-locked-kombinasi-and-clear-dan-urutan | FE+BE |
| TC-FA-FAAM-725 | E2E | TC-FA-FAAM-E2E-050-create-rate-limit-cek-keunikan-429 | FE+BE |
| TC-FA-FAAM-726 | E2E | TC-FA-FAAM-E2E-050-create-rate-limit-cek-keunikan-429 | FE+BE |
| TC-FA-FAAM-727 | E2E | TC-FA-FAAM-E2E-139-notice-category-locked-hitungan-menjadi-nol | FE+BE |
| TC-FA-FAAM-728 | E2E | TC-FA-FAAM-E2E-080-edit-dialog-default-addon-cancel-dan-hitungan-berubah | FE+BE |
| TC-FA-FAAM-729 | E2E | TC-FA-FAAM-E2E-016-excess-pelepasan-status-dan-mutasi-katalog | FE+BE |
| TC-FA-FAAM-730 | E2E | TC-FA-FAAM-E2E-015-excess-tampilan-dan-aksi-client-downgrade | FE+BE |
| TC-FA-FAAM-731 | E2E | TC-FA-FAAM-E2E-227-transisi-otomatis-default-addon-eventual-60-detik | FE+BE |
| TC-FA-FAAM-732 | E2E | TC-FA-FAAM-E2E-137-notice-category-locked-retensi-sidebar-dan-loading | FE+BE |
| TC-FA-FAAM-733 | E2E | TC-FA-FAAM-E2E-067-edit-validasi-model-dan-kapitalisasi | FE+BE |
| TC-FA-FAAM-734 | E2E | TC-FA-FAAM-E2E-217-log-system-activity-create-dan-aksi-aktor | FE+BE |
| TC-FA-FAAM-735 | E2E | TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron | FE+BE |
| TC-FA-FAAM-736 | E2E | TC-FA-FAAM-E2E-218-log-system-activity-rename-delete-dan-sinkron | FE+BE |
| TC-FA-FAAM-737 | E2E | TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail | FE+BE |
| TC-FA-FAAM-738 | E2E | TC-FA-FAAM-E2E-020-mobile-form-tree-picker-changelog-dan-tabel-detail | FE+BE |
| TC-FA-FAAM-739 | E2E | TC-FA-FAAM-E2E-244-sinkron-dropdown-registrasi-aset-rename-dan-delete | FE+BE |
| TC-FA-FAAM-740 | E2E | TC-FA-FAAM-E2E-244-sinkron-dropdown-registrasi-aset-rename-dan-delete | FE+BE |
| TC-FA-FAAM-741 | E2E | TC-FA-FAAM-E2E-224-import-kuota-paket-dan-penyemaian-policy | FE+BE |
| TC-FA-FAAM-742 | E2E | TC-FA-FAAM-E2E-060-edit-penutupan-backdrop-reload-sidebar-dan-tree-picker | FE+BE |
| TC-FA-FAAM-743 | E2E | TC-FA-FAAM-E2E-080-edit-dialog-default-addon-cancel-dan-hitungan-berubah | FE+BE |
| TC-FA-FAAM-744 | E2E | TC-FA-FAAM-E2E-075-edit-dialog-change-default-label-save-dan-cancel | FE+BE |
| TC-FA-FAAM-745 | E2E | TC-FA-FAAM-E2E-148-changelog-search-kelas-kolom-dan-placeholder | FE+BE |
| TC-FA-FAAM-746 | E2E | TC-FA-FAAM-E2E-068-edit-brand-baru-no-model-dan-badge-model | FE+BE |
| TC-FA-FAAM-747 | E2E | TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton | FE+BE |
| TC-FA-FAAM-748 | E2E | TC-FA-FAAM-E2E-119-filter-opsi-dinamis-client-kosong-stale-dan-skeleton | FE+BE |
| TC-FA-FAAM-749 | E2E | TC-FA-FAAM-E2E-047-create-ceiling-klik-tombol-dialog-d07-dan-label-limit | FE+BE |
| TC-FA-FAAM-750 | E2E | TC-FA-FAAM-E2E-189-total-assets-kolom-urutan-setup-column-dan-tag | FE+BE |
| TC-FA-FAAM-751 | E2E | TC-FA-FAAM-E2E-189-total-assets-kolom-urutan-setup-column-dan-tag | FE+BE |
| TC-FA-FAAM-752 | E2E | TC-FA-FAAM-E2E-177-total-assets-sort-status-last-updated-label-dan-tag | FE+BE |
| TC-FA-FAAM-753 | E2E | TC-FA-FAAM-E2E-174-total-assets-filter-label-tag-dan-measurement | FE+BE |
| TC-FA-FAAM-754 | E2E | TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal | FE+BE |
| TC-FA-FAAM-755 | E2E | TC-FA-FAAM-E2E-188-total-assets-setup-column-label-geser-pin-dan-tag | FE+BE |
| TC-FA-FAAM-756 | E2E | TC-FA-FAAM-E2E-180-total-assets-download-tag-measurement-category-policy | FE+BE |
| TC-FA-FAAM-757 | E2E | TC-FA-FAAM-E2E-190-total-assets-kolom-measurement-dan-category | FE+BE |
| TC-FA-FAAM-758 | E2E | TC-FA-FAAM-E2E-170-total-assets-search-measurement-dan-tag | FE+BE |
| TC-FA-FAAM-759 | E2E | TC-FA-FAAM-E2E-174-total-assets-filter-label-tag-dan-measurement | FE+BE |
| TC-FA-FAAM-760 | E2E | TC-FA-FAAM-E2E-190-total-assets-kolom-measurement-dan-category | FE+BE |
| TC-FA-FAAM-761 | E2E | TC-FA-FAAM-E2E-169-total-assets-search-kolom-hidden-label-tag-dan-tanggal | FE+BE |
| TC-FA-FAAM-762 | E2E | TC-FA-FAAM-E2E-175-total-assets-filter-category-policy-dan-last-scanned | FE+BE |
| TC-FA-FAAM-763 | E2E | TC-FA-FAAM-E2E-191-total-assets-kolom-transactional-policy-dan-last-scanned | FE+BE |
| TC-FA-FAAM-764 | E2E | TC-FA-FAAM-E2E-175-total-assets-filter-category-policy-dan-last-scanned | FE+BE |
| TC-FA-FAAM-765 | E2E | TC-FA-FAAM-E2E-211-total-assets-sort-kolom-seragam-measurement-category-dan-policy | FE+BE |
| TC-FA-FAAM-766 | E2E | TC-FA-FAAM-E2E-180-total-assets-download-tag-measurement-category-policy | FE+BE |
| TC-FA-FAAM-767 | E2E | TC-FA-FAAM-E2E-191-total-assets-kolom-transactional-policy-dan-last-scanned | FE+BE |
| TC-FA-FAAM-768 | E2E | TC-FA-FAAM-E2E-178-total-assets-sort-kolom-seragam-last-scanned-warranty-dan-asset-value | FE+BE |
| TC-FA-FAAM-769 | E2E | TC-FA-FAAM-E2E-175-total-assets-filter-category-policy-dan-last-scanned | FE+BE |
| TC-FA-FAAM-770 | E2E | TC-FA-FAAM-E2E-180-total-assets-download-tag-measurement-category-policy | FE+BE |
| TC-FA-FAAM-771 | E2E | TC-FA-FAAM-E2E-192-total-assets-kolom-asset-value-dan-warranty-expiry | FE+BE |
| TC-FA-FAAM-772 | E2E | TC-FA-FAAM-E2E-178-total-assets-sort-kolom-seragam-last-scanned-warranty-dan-asset-value | FE+BE |
| TC-FA-FAAM-773 | E2E | TC-FA-FAAM-E2E-198-total-assets-formula-dan-filter-range-nilai-full-value | FE+BE |
| TC-FA-FAAM-774 | E2E | TC-FA-FAAM-E2E-181-total-assets-download-asset-value-warranty-dan-no-access | FE+BE |
| TC-FA-FAAM-775 | E2E | TC-FA-FAAM-E2E-192-total-assets-kolom-asset-value-dan-warranty-expiry | FE+BE |
| TC-FA-FAAM-776 | E2E | TC-FA-FAAM-E2E-178-total-assets-sort-kolom-seragam-last-scanned-warranty-dan-asset-value | FE+BE |
| TC-FA-FAAM-777 | E2E | TC-FA-FAAM-E2E-198-total-assets-formula-dan-filter-range-nilai-full-value | FE+BE |
| TC-FA-FAAM-778 | E2E | TC-FA-FAAM-E2E-181-total-assets-download-asset-value-warranty-dan-no-access | FE+BE |
| TC-FA-FAAM-779 | E2E | TC-FA-FAAM-E2E-193-total-assets-kolom-custom-field-daftar-scope-dan-purchasing | FE+BE |
| TC-FA-FAAM-780 | E2E | TC-FA-FAAM-E2E-193-total-assets-kolom-custom-field-daftar-scope-dan-purchasing | FE+BE |
| TC-FA-FAAM-781 | E2E | TC-FA-FAAM-E2E-193-total-assets-kolom-custom-field-daftar-scope-dan-purchasing | FE+BE |
| TC-FA-FAAM-782 | E2E | TC-FA-FAAM-E2E-194-total-assets-kolom-custom-field-purchasing-numerik-dan-setup | FE+BE |
| TC-FA-FAAM-783 | E2E | TC-FA-FAAM-E2E-194-total-assets-kolom-custom-field-purchasing-numerik-dan-setup | FE+BE |
| TC-FA-FAAM-784 | E2E | TC-FA-FAAM-E2E-203-total-assets-gerbang-asset-value-ho-sel-dan-sort | FE+BE |
| TC-FA-FAAM-785 | E2E | TC-FA-FAAM-E2E-208-total-assets-gerbang-accounting-global-dan-lisensi-fa7 | FE+BE |
| TC-FA-FAAM-786 | E2E | TC-FA-FAAM-E2E-205-total-assets-gerbang-purchase-ho-sel-tooltip-dan-search | FE+BE |
| TC-FA-FAAM-787 | E2E | TC-FA-FAAM-E2E-207-total-assets-gerbang-tanpa-hak-nilai-sensitif | FE+BE |
| TC-FA-FAAM-788 | E2E | TC-FA-FAAM-E2E-195-total-assets-kolom-asset-id-retensi-state-dan-full-value | FE+BE |
| TC-FA-FAAM-789 | E2E | TC-FA-FAAM-E2E-205-total-assets-gerbang-purchase-ho-sel-tooltip-dan-search | FE+BE |
| TC-FA-FAAM-790 | E2E | TC-FA-FAAM-E2E-203-total-assets-gerbang-asset-value-ho-sel-dan-sort | FE+BE |
| TC-FA-FAAM-791 | E2E | TC-FA-FAAM-E2E-204-total-assets-gerbang-asset-value-ho-filter-dan-lintas-group | FE+BE |
| TC-FA-FAAM-792 | E2E | TC-FA-FAAM-E2E-205-total-assets-gerbang-purchase-ho-sel-tooltip-dan-search | FE+BE |
| TC-FA-FAAM-793 | E2E | TC-FA-FAAM-E2E-181-total-assets-download-asset-value-warranty-dan-no-access | FE+BE |
| TC-FA-FAAM-794 | E2E | TC-FA-FAAM-E2E-207-total-assets-gerbang-tanpa-hak-nilai-sensitif | FE+BE |
| TC-FA-FAAM-795 | E2E | TC-FA-FAAM-E2E-204-total-assets-gerbang-asset-value-ho-filter-dan-lintas-group | FE+BE |
| TC-FA-FAAM-796 | E2E | TC-FA-FAAM-E2E-195-total-assets-kolom-asset-id-retensi-state-dan-full-value | FE+BE |
| TC-FA-FAAM-797 | E2E | TC-FA-FAAM-E2E-226-sinkron-kolom-policy-custom-field-dan-last-scanned | FE+BE |
| TC-FA-FAAM-798 | E2E | TC-FA-FAAM-E2E-226-sinkron-kolom-policy-custom-field-dan-last-scanned | FE+BE |
| TC-FA-FAAM-799 | E2E | TC-FA-FAAM-E2E-226-sinkron-kolom-policy-custom-field-dan-last-scanned | FE+BE |
| TC-FA-FAAM-800 | E2E | TC-FA-FAAM-E2E-207-total-assets-gerbang-tanpa-hak-nilai-sensitif | FE+BE |
| TC-FA-FAAM-801 | E2E | TC-FA-FAAM-E2E-170-total-assets-search-measurement-dan-tag | FE+BE |
| TC-FA-FAAM-802 | E2E | TC-FA-FAAM-E2E-171-total-assets-search-transactional-policy-dan-asset-value | FE+BE |
| TC-FA-FAAM-803 | E2E | TC-FA-FAAM-E2E-206-total-assets-gerbang-purchase-ho-custom-field-purchasing | FE+BE |
| TC-FA-FAAM-804 | E2E | TC-FA-FAAM-E2E-209-total-assets-hak-tier-role-matrix-global-dan-group-manager | FE+BE |
| TC-FA-FAAM-805 | E2E | TC-FA-FAAM-E2E-209-total-assets-hak-tier-role-matrix-global-dan-group-manager | FE+BE |
| TC-FA-FAAM-806 | E2E | TC-FA-FAAM-E2E-208-total-assets-gerbang-accounting-global-dan-lisensi-fa7 | FE+BE |
| TC-FA-FAAM-807 | E2E | TC-FA-FAAM-E2E-208-total-assets-gerbang-accounting-global-dan-lisensi-fa7 | FE+BE |
| TC-FA-FAAM-808 | E2E | TC-FA-FAAM-E2E-195-total-assets-kolom-asset-id-retensi-state-dan-full-value | FE+BE |
| TC-FA-FAAM-809 | E2E | TC-FA-FAAM-E2E-171-total-assets-search-transactional-policy-dan-asset-value | FE+BE |
| TC-FA-FAAM-810 | E2E | TC-FA-FAAM-E2E-196-total-assets-custom-field-dropdown-dan-date | FE+BE |
| TC-FA-FAAM-811 | E2E | TC-FA-FAAM-E2E-196-total-assets-custom-field-dropdown-dan-date | FE+BE |
| TC-FA-FAAM-812 | E2E | TC-FA-FAAM-E2E-197-total-assets-custom-field-numerik-teks-dan-formula | FE+BE |
| TC-FA-FAAM-813 | E2E | TC-FA-FAAM-E2E-197-total-assets-custom-field-numerik-teks-dan-formula | FE+BE |
| TC-FA-FAAM-814 | E2E | TC-FA-FAAM-E2E-198-total-assets-formula-dan-filter-range-nilai-full-value | FE+BE |
| TC-FA-FAAM-815 | E2E | TC-FA-FAAM-E2E-206-total-assets-gerbang-purchase-ho-custom-field-purchasing | FE+BE |
| TC-FA-FAAM-816 | E2E | TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari | FE+BE |
| TC-FA-FAAM-817 | E2E | TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari | FE+BE |
| TC-FA-FAAM-818 | E2E | TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari | FE+BE |
| TC-FA-FAAM-819 | E2E | TC-FA-FAAM-E2E-201-total-assets-penanda-masa-garansi-batas-hari | FE+BE |
| TC-FA-FAAM-820 | E2E | TC-FA-FAAM-E2E-202-total-assets-penanda-masa-garansi-strip-time-zone-dan-netral | FE+BE |
| TC-FA-FAAM-821 | E2E | TC-FA-FAAM-E2E-202-total-assets-penanda-masa-garansi-strip-time-zone-dan-netral | FE+BE |
| TC-FA-FAAM-822 | E2E | TC-FA-FAAM-E2E-202-total-assets-penanda-masa-garansi-strip-time-zone-dan-netral | FE+BE |
| TC-FA-FAAM-823 | E2E | TC-FA-FAAM-E2E-199-total-assets-asset-value-commercial-fiscal-dua-kolom-tetap | FE+BE |
| TC-FA-FAAM-824 | E2E | TC-FA-FAAM-E2E-199-total-assets-asset-value-commercial-fiscal-dua-kolom-tetap | FE+BE |
| TC-FA-FAAM-825 | E2E | TC-FA-FAAM-E2E-199-total-assets-asset-value-commercial-fiscal-dua-kolom-tetap | FE+BE |
| TC-FA-FAAM-826 | E2E | TC-FA-FAAM-E2E-200-total-assets-asset-value-fiscal-gerbang-dan-sort-filter | FE+BE |
| TC-FA-FAAM-827 | E2E | TC-FA-FAAM-E2E-200-total-assets-asset-value-fiscal-gerbang-dan-sort-filter | FE+BE |
| TC-FA-FAAM-828 | E2E | TC-FA-FAAM-E2E-228-tag-type-non-standard-di-tag-dan-cancel-dialog | FE+BE |
| TC-FA-FAAM-829 | E2E | TC-FA-FAAM-E2E-245-tag-type-tanpa-objek-tugas-dan-pending-changes | FE+BE |
| TC-FA-FAAM-830 | E2E | TC-FA-FAAM-E2E-105-popup-detail-progres-kepatuhan-tag-type-format-dan-bentuk-tunggal | FE+BE |
| TC-FA-FAAM-831 | E2E | TC-FA-FAAM-E2E-106-popup-detail-progres-kepatuhan-per-role-dan-scope | FE+BE |
| TC-FA-FAAM-832 | E2E | TC-FA-FAAM-E2E-105-popup-detail-progres-kepatuhan-tag-type-format-dan-bentuk-tunggal | FE+BE |
| TC-FA-FAAM-833 | E2E | TC-FA-FAAM-E2E-109-popup-detail-progres-kepatuhan-tag-type-tidak-tampil-dua-tipe-dan-non-tag | FE+BE |
| TC-FA-FAAM-834 | E2E | TC-FA-FAAM-E2E-106-popup-detail-progres-kepatuhan-per-role-dan-scope | FE+BE |
| TC-FA-FAAM-835 | E2E | TC-FA-FAAM-E2E-109-popup-detail-progres-kepatuhan-tag-type-tidak-tampil-dua-tipe-dan-non-tag | FE+BE |
| TC-FA-FAAM-836 | E2E | TC-FA-FAAM-E2E-109-popup-detail-progres-kepatuhan-tag-type-tidak-tampil-dua-tipe-dan-non-tag | FE+BE |
| TC-FA-FAAM-837 | E2E | TC-FA-FAAM-E2E-022-resilience-baca-progres-kepatuhan-tag-type-popup-detail | FE+BE |
| TC-FA-FAAM-838 | E2E | TC-FA-FAAM-E2E-229-tag-type-tanpa-aset-dan-progres-kepatuhan-berubah | FE+BE |
| TC-FA-FAAM-839 | E2E | TC-FA-FAAM-E2E-230-progres-kepatuhan-replace-dan-pair-tag-hardware-reader | FE+BE |
| TC-FA-FAAM-840 | E2E | TC-FA-FAAM-E2E-230-progres-kepatuhan-replace-dan-pair-tag-hardware-reader | FE+BE |
| TC-FA-FAAM-841 | E2E | TC-FA-FAAM-E2E-246-progres-kepatuhan-pair-tag-hardware-reader | FE+BE |
| TC-FA-FAAM-842 | E2E | TC-FA-FAAM-E2E-253-pencatatan-absence-create-edit-ditolak-suspended-expired | FE+BE |
| TC-FA-FAAM-843 | E2E | TC-FA-FAAM-E2E-254-pencatatan-absence-delete-bulk-delete-import-ditolak-suspended-expired | FE+BE |
| TC-FA-FAAM-844 | E2E | TC-FA-FAAM-E2E-251-pencatatan-absence-bulk-delete-langsung-semua-in-use | FE+BE |
| TC-FA-FAAM-845 | E2E | TC-FA-FAAM-E2E-252-pencatatan-absence-request-create-langsung-ditolak | FE+BE |
| TC-FA-FAAM-846 | E2E | TC-FA-FAAM-E2E-141-download-isi-berkas-total-asset-tanggal-kosong-dan-bom | FE+BE |
