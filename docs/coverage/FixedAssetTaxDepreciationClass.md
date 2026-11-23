# Coverage E2E — Fixed Asset > Settings > Accounting > Tax Depreciation Class

Sumber: `fixed-asset/tax-depreciation-class/TestCases/tc-tax-depreciation-class.md` (963 TC aktif `TC-FA-TDC-1`–`967` tanpa TC-349, 581, 582, dan 745 yang dihapus pada 2026-11-20; TC-935 s/d TC-961 (27 TC, perubahan 2026-11-11) dipetakan ke spec 279-289 pada 2026-11-23, sha256 `6877ccc3838448cd438904e8246ef9fca5a68d0075a4530e0250f537fe3621df`). Suite: `specs/FixedAsset/TaxDepreciationClass/`. Prefix: `FA` + `TDC` (`TC-FA-TDC-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-tax-depreciation-class-backend.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 963 TC (dari 963 TC aktif) masuk 287 spec (226 nomor rencana 001-226, 30 dari 32 nomor cadangan 227-258, 2 cadangan tidak terpakai: 230, 254, dan 31 nomor tambahan 259-289: 259-263 dari keputusan user 2026-11-04, 264 dari fix pass 1, 265-274 dari fix pass 2, 275-278 dari sinkronisasi TC 2026-11-20 untuk TC-962 s/d TC-967, dan 279-289 dari pemetaan TC-935 s/d TC-961 pada 2026-11-23), tidak ada TC hanya-BE. Setiap TC terpetakan satu spec primer (diverifikasi dengan skrip: tidak ada TC hilang atau ID asing); 76 TC juga muncul di `sourceTc` satu spec absence (15 spec: 260-263, 265-274, dan 288, ditambah spec 253 untuk TC-962; TC-964 di spec 270) untuk klausa "tidak ada entri log baru" (lihat "Pembagian TC lintas spec"), dan "Lapisan per TC" menunjuk spec primer. Semua spec bermode FE+BE. Kegagalan 5xx, timeout, dan 429 dipaksa lewat `Spectra.intercept()` di atas backend nyata karena asersinya memuat state server (Q-06). Spec 185 dan 186 (TC Android) memakai `coverage.mobile` saja; spec lain `coverage.web`. Kolom TC sumber memakai nomor TC (`TC-FA-TDC-n`); urutan TC dalam satu spec mengikuti `## Test Steps`, yang kadang berbeda dari urutan nomor.

## TC hanya-BE (tidak masuk spec)

Tidak ada. File backend TC tidak ada. TC request langsung (Role Matrix, bypass UI, isolasi client) tetap masuk spec FE+BE dengan butir K-1 lewat sesi API aktor.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-TDC-E2E-001-screening-halaman-breadcrumb-tab-bar-dan-toolbar | Screening Halaman Tax Depreciation Class: Breadcrumb, Tab Bar, dan Toolbar | FE+BE | 31 | 1, 2, 3, 4 |
| TC-FA-TDC-E2E-002-loading-dan-kegagalan-muat-tabel | Loading dan Kegagalan Muat Tabel Tax Depreciation Class | FE+BE | 24 | 5, 6, 7 |
| TC-FA-TDC-E2E-003-empty-state-hasil-search-dan-filter-serta-pemulihan | Empty State Hasil Search dan Filter serta Pemulihan Tabel | FE+BE | 27 | 9, 10, 11, 12 |
| TC-FA-TDC-E2E-004-restore-default-classes-tidak-tersedia-bila-masih-ada-class | Restore Default Classes Tidak Tersedia Selama Masih Ada Class | FE+BE | 40 | 13, 316, 317, 318 |
| TC-FA-TDC-E2E-005-tampilan-kolom-active-class-code-class-name-asset-type-useful-life-dan-rate | Tampilan Kolom Active, Class Code, Class Name, Asset Type, Useful Life, dan Rate | FE+BE | 29 | 16, 17, 18, 19, 20 |
| TC-FA-TDC-E2E-006-tampilan-kolom-allowed-methods-used-by-effective-from-dan-regulation-reference | Tampilan Kolom Allowed Methods, Used By, Effective From, dan Regulation Reference | FE+BE | 27 | 21, 22, 23, 24, 25, 26, 27 |
| TC-FA-TDC-E2E-007-tampilan-kolom-modified-by-last-updated-baris-example-data-dan-row-action | Tampilan Kolom Modified By, Last Updated, Baris Example Data, dan Row Action | FE+BE | 33 | 28, 29, 30, 31, 33 |
| TC-FA-TDC-E2E-008-tooltip-icon-toolbar-header-actions-dan-akses-keyboard | Tooltip Icon Toolbar, Header Actions, dan Akses Keyboard | FE+BE | 18 | 15, 35 |
| TC-FA-TDC-E2E-009-aksesibilitas-keyboard-toggle-active-dan-fokus-popup-used-by | Aksesibilitas Keyboard Toggle Active dan Fokus Popup Used By | FE+BE | 28 | 34, 36, 366, 378 |
| TC-FA-TDC-E2E-010-aksesibilitas-fokus-ter-trap-dialog-konfirmasi-d-01-d-03-d-06-dan-campuran-d-14-d-15 | Aksesibilitas Fokus Ter-trap Dialog Konfirmasi D-01, D-03, D-06 dan Dialog Campuran D-14, D-15 | FE+BE | 32 | 916, 917 |
| TC-FA-TDC-E2E-011-aksesibilitas-fokus-ter-trap-dialog-d-09-d-10-dan-d-12 | Aksesibilitas Fokus Ter-trap Dialog D-09, D-10, dan D-12 | FE+BE | 23 | 293 |
| TC-FA-TDC-E2E-012-role-matrix-akses-penuh-total-control-dan-default-user | Role Matrix: Akses Penuh Total Control dan Default User pada Tab Tax Depreciation Class | FE+BE | 29 | 38, 39, 40 |
| TC-FA-TDC-E2E-013-role-matrix-baca-read-only-read-capability-selalu-disertai-read-dan-data-seluruh-client | Role Matrix: Akses Baca Read Only, Read, Capability Selalu Disertai Read, dan Data Berlaku Seluruh Client | FE+BE | 35 | 41, 42, 43, 46 |
| TC-FA-TDC-E2E-014-role-matrix-negatif-tanpa-capability-menu-accounting-dan-url-langsung | Role Matrix Negatif: Tanpa Capability Menu Accounting dan URL Langsung | FE+BE | 13 | 44, 45 |
| TC-FA-TDC-E2E-015-role-matrix-visibilitas-elemen-baca-dan-drawer-baca-semua-aktor | Role Matrix: Visibilitas Elemen Baca dan Drawer Baca untuk Semua Aktor | FE+BE | 22 | 47, 48 |
| TC-FA-TDC-E2E-016-role-matrix-positif-create-row-action-dan-toggle-active | Role Matrix Positif: Tombol Create, Menu Row Action, dan Toggle Active | FE+BE | 41 | 49, 53, 54, 55, 57 |
| TC-FA-TDC-E2E-017-role-matrix-negatif-create-restore-dan-tombol-baris-tanpa-hak | Role Matrix Negatif: Tombol Create, Restore default classes, dan Tombol Baris Tanpa Hak | FE+BE | 14 | 50, 52, 56 |
| TC-FA-TDC-E2E-018-role-matrix-negatif-toggle-active-checkbox-bulk-dan-field-drawer | Role Matrix Negatif: Toggle Active, Checkbox Bulk, dan Field Drawer tanpa Hak Update | FE+BE | 29 | 58, 62, 64 |
| TC-FA-TDC-E2E-019-role-matrix-positif-bulk-field-drawer-cancel-scheduled-dan-popup-versions | Role Matrix Positif: Bulk Action Bar, Field Drawer Edit, Cancel Scheduled Version, dan Popup Versions | FE+BE | 46 | 59, 60, 61, 63, 65, 67 |
| TC-FA-TDC-E2E-020-role-matrix-negatif-alert-versi-scheduled-dan-popup-versions-tanpa-update | Role Matrix Negatif: Alert Versi Scheduled dan Popup Versions tanpa Hak Update | FE+BE | 11 | 66, 68 |
| TC-FA-TDC-E2E-021-role-matrix-gabungan-update-delete-dan-create-update | Role Matrix: Gabungan Capability Update+Delete dan Create+Update | FE+BE | 32 | 69, 70 |
| TC-FA-TDC-E2E-022-aktor-create-only-membuat-class-dan-memulihkan-seed | Aktor Create-Only: Membuat Class dan Memulihkan Seed lewat Restore default classes | FE+BE | 25 | 71, 72, 323 |
| TC-FA-TDC-E2E-023-aktor-update-only-edit-dan-toggle-active | Aktor Update-Only: Edit Class dan Toggle Active | FE+BE | 33 | 73, 74, 75, 76, 77 |
| TC-FA-TDC-E2E-024-aktor-update-only-dialog-blok-dan-membatalkan-versi-scheduled | Aktor Update-Only: Dialog Blok Deactivate dan Membatalkan Versi Scheduled | FE+BE | 42 | 78, 79, 80, 81, 313 |
| TC-FA-TDC-E2E-025-aktor-update-only-bulk-activate-deactivate-dan-cancel-version-dari-alert | Aktor Update-Only: Bulk Activate, Bulk Deactivate, dan Cancel Version dari Alert | FE+BE | 38 | 85, 86, 87, 301 |
| TC-FA-TDC-E2E-026-aktor-delete-only-delete-single-dan-dialog-blok-guard | Aktor Delete-Only: Delete Single dan Dialog Blok Guard | FE+BE | 18 | 82, 83, 84 |
| TC-FA-TDC-E2E-027-aktor-delete-only-bulk-delete-lolos-campuran-dan-diblokir | Aktor Delete-Only: Bulk Delete Lolos, Campuran, dan Diblokir | FE+BE | 21 | 88, 89, 90 |
| TC-FA-TDC-E2E-028-aktor-read-membuka-mencari-memfilter-mengunduh-dan-popup | Aktor Read: Membuka Tab, Mencari, Memfilter, Mengunduh, dan Membuka Popup | FE+BE | 32 | 91, 92, 93, 94, 95, 96, 97 |
| TC-FA-TDC-E2E-029-plan-starter-menu-accounting-disabled-dan-tab-penuh-growth-professional-enterprise | Plan Starter: Menu Accounting Disabled dan Akses Langsung Ditolak, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise | FE+BE | 22 | 98, 100, 764, 765 |
| TC-FA-TDC-E2E-030-plan-data-class-tetap-tersimpan-setelah-downgrade-starter-dan-upgrade | Plan: Data Class Tetap Tersimpan Setelah Downgrade ke Starter dan Upgrade, Tab Tersedia Penuh pada Plan Growth, Professional, dan Enterprise | FE+BE | 20 | 99, 766, 767, 768, 769 |
| TC-FA-TDC-E2E-031-state-tenant-suspended-expired-aksi-baca-tetap-tersedia | State Tenant Suspended dan Expired: Aksi Baca Tabel, Search, Used By, Changelog, dan Drawer Edit Tetap Tersedia | FE+BE | 31 | 889, 890 |
| TC-FA-TDC-E2E-032-suspended-aksi-single-activate-deactivate-delete-ditolak-toast-baku | Entitas Suspended: Aksi Single Activate, Deactivate, dan Delete Ditolak dengan Toast Baku | FE+BE | 26 | 874, 875, 876 |
| TC-FA-TDC-E2E-033-suspended-aksi-bulk-activate-deactivate-delete-ditolak-toast-baku | Entitas Suspended: Aksi Bulk Activate, Deactivate, dan Delete Ditolak dengan Toast Baku | FE+BE | 29 | 877, 878, 879 |
| TC-FA-TDC-E2E-034-expired-aksi-activate-deactivate-delete-dan-bulk-delete-ditolak-toast-baku | Entitas Expired: Aksi Activate, Deactivate, Delete, dan Bulk Delete Ditolak dengan Toast Baku | FE+BE | 37 | 880, 881, 882, 883 |
| TC-FA-TDC-E2E-035-suspended-create-edit-cancel-version-dan-restore-ditolak-toast-baku | Entitas Suspended: Create, Edit, Cancel Scheduled Version, dan Restore Default Classes Ditolak dengan Toast Baku | FE+BE | 46 | 884, 885, 886, 887 |
| TC-FA-TDC-E2E-036-job-latar-j-01-j-02-j-03-tetap-berjalan-saat-suspended-atau-expired | Job Latar J-01, J-02, dan J-03 Tetap Berjalan saat Entitas Suspended atau Expired | FE+BE | 46 | 891, 892, 893, 894, 360 |
| TC-FA-TDC-E2E-037-batas-master-data-count-limit-dialog-d-07-screening-ok-esc-dan-fokus | Batas Master Data Count Limit: Dialog D-07 Tax Depreciation Class Limit Reached, Screening, Tombol OK, Esc, dan Fokus | FE+BE | 26 | 126, 127, 128, 129, 919 |
| TC-FA-TDC-E2E-038-batas-master-data-count-limit-inactive-ikut-dihitung-dan-berlaku-di-semua-plan | Batas Master Data Count Limit: Class Inactive Ikut Dihitung dan Batas Berlaku pada Plan Growth, Professional, dan Enterprise | FE+BE | 16 | 131, 759, 760, 761, 762 |
| TC-FA-TDC-E2E-039-batas-selection-limit-select-all-dan-live-block-checkbox | Batas Selection Limit: Select All Melebihi Batas Memotong Seleksi dan Live-Block Checkbox Baris | FE+BE | 19 | 423, 424 |
| TC-FA-TDC-E2E-040-drawer-create-screening-opsi-asset-type-satu-form-tanpa-tab-dan-aksesibilitas | Drawer Create - Screening, Opsi Asset Type, Satu Form Tanpa Tab, dan Aksesibilitas | FE+BE | 31 | 103, 104, 915, 176 |
| TC-FA-TDC-E2E-041-create-class-sukses-non-building-building-dan-land | Create Class Sukses - Non-building, Building, dan Land | FE+BE | 33 | 105, 106, 107 |
| TC-FA-TDC-E2E-042-create-sukses-varian-metode-straight-line-saja-dan-declining-balance-saja | Create Sukses - Varian Metode Straight Line Saja dan Declining Balance Saja | FE+BE | 21 | 108, 109 |
| TC-FA-TDC-E2E-043-create-stay-on-form-checkbox-default-dan-dipertahankan | Create dengan Checkbox Stay on This Form - Form Kosong dan Status Checkbox | FE+BE | 32 | 111, 112 |
| TC-FA-TDC-E2E-044-create-saving-state-gagal-5xx-dan-klik-ganda-submit | Create - Saving State, Gagal 5xx, dan Klik Ganda Submit | FE+BE | 32 | 114, 115, 116 |
| TC-FA-TDC-E2E-045-create-validasi-class-code-kosong-panjang-dan-whitelist | Create - Validasi Class Code Kosong, Panjang, dan Whitelist Karakter | FE+BE | 33 | 135, 136, 137, 138, 139 |
| TC-FA-TDC-E2E-046-create-validasi-class-code-duplikat-debounce-dan-trim | Create - Validasi Class Code Duplikat, Debounce, dan Trim | FE+BE | 29 | 140, 141, 142, 143, 174, 175 |
| TC-FA-TDC-E2E-047-create-validasi-class-name-kosong-panjang-dan-emoji | Create - Validasi Class Name Kosong, Panjang, dan Emoji | FE+BE | 30 | 144, 145, 146, 147, 148 |
| TC-FA-TDC-E2E-048-create-class-name-trim-duplikat-diizinkan-dan-regulation-reference-kosong | Create - Class Name Ter-trim, Duplikat Diizinkan, dan Regulation Reference Kosong | FE+BE | 23 | 149, 150, 151 |
| TC-FA-TDC-E2E-049-create-validasi-regulation-reference-asset-type-dan-useful-life-kosong | Create - Validasi Regulation Reference, Asset Type, dan Useful Life Kosong | FE+BE | 26 | 152, 153, 154, 155, 156 |
| TC-FA-TDC-E2E-050-create-validasi-useful-life-batas-dan-allowed-methods-kosong | Create - Validasi Batas Useful Life dan Allowed Methods Kosong | FE+BE | 21 | 157, 158, 159 |
| TC-FA-TDC-E2E-051-create-pilih-asset-type-land-building-non-building-mengatur-field-dan-opsi | Create - Pilih Asset Type Land, Building, dan Non-building Mengatur Field dan Opsi | FE+BE | 29 | 162, 163, 164 |
| TC-FA-TDC-E2E-052-create-rate-tampil-mengikuti-metode-read-only-dan-batas-seratus | Create - Rate Tampil Mengikuti Metode, Read-only, dan Batas 100 | FE+BE | 34 | 165, 166, 167, 171 |
| TC-FA-TDC-E2E-053-create-rate-bulat-pembulatan-dua-desimal-half-up-dan-useful-life-maksimum | Create - Rate Bulat, Pembulatan Dua Desimal Half-up, dan Useful Life Maksimum | FE+BE | 35 | 168, 169, 170, 172 |
| TC-FA-TDC-E2E-054-create-menutup-drawer-ikon-esc-backdrop-leave-dan-cancel-dialog | Create - Menutup Drawer Lewat Ikon, Esc, Backdrop, Leave, dan Cancel Dialog | FE+BE | 32 | 118, 119, 120, 121, 122 |
| TC-FA-TDC-E2E-055-create-field-dikembalikan-kosong-reload-dan-konfirmasi-bawaan-browser | Create - Field Dikembalikan Kosong, Reload, dan Konfirmasi Bawaan Browser | FE+BE | 22 | 123, 124, 125 |
| TC-FA-TDC-E2E-056-drawer-edit-screening-header-dan-buka-lewat-row-action | Drawer Edit: Screening Tiga Zona dan Buka Lewat Row Action | FE+BE | 28 | 177, 178 |
| TC-FA-TDC-E2E-057-drawer-edit-field-disabled-class-code-terkunci-class-land-building-dan-inactive | Drawer Edit: Last Posted Tax Year, Class Code Terkunci, Class Inactive, dan Asset Type Disabled | FE+BE | 43 | 180, 181, 182, 183, 185, 186 |
| TC-FA-TDC-E2E-058-drawer-edit-layout-tablet-rate-hitung-ulang-pre-fill-versi-scheduled-dan-aksesibilitas | Drawer Edit: Layout Tablet, Rate Dihitung Ulang, Pre-fill Versi Scheduled, dan Aksesibilitas Keyboard | FE+BE | 41 | 37, 187, 188, 247 |
| TC-FA-TDC-E2E-059-edit-langsung-class-name-regulation-reference-class-code-dan-gabungan | Edit Langsung Tanpa Versi Baru: Class Name dan Regulation Reference | FE+BE | 25 | 189, 190 |
| TC-FA-TDC-E2E-060-edit-kapitalisasi-no-op-class-code-sendiri-bukan-duplikat-dan-versi-baru-class-terkunci | Edit: Kapitalisasi Class Code, Edit No-Op, Class Code Sendiri Bukan Duplikat, dan Versi Baru Class Terkunci | FE+BE | 41 | 193, 194, 195, 196, 218 |
| TC-FA-TDC-E2E-061-edit-class-code-terkunci-regulation-reference-dan-versi-scheduled | Edit: Class Code Terkunci, Regulation Reference, dan Edit pada Class dengan Versi Scheduled | FE+BE | 42 | 184, 215, 216, 217 |
| TC-FA-TDC-E2E-062-edit-class-inactive-saving-state-gagal-5xx-dan-klik-ganda-save | Edit: Saving State, Klik Ganda Save, Gagal 5xx, dan Class Inactive Dapat Diedit | FE+BE | 38 | 197, 198, 199, 219 |
| TC-FA-TDC-E2E-063-edit-menutup-drawer-tanpa-perubahan-ikon-esc-backdrop-leave-dan-cancel | Edit: Menutup Drawer dengan Ikon Tutup, Esc, Backdrop, Leave, dan Cancel | FE+BE | 33 | 203, 204, 205, 206, 207 |
| TC-FA-TDC-E2E-064-edit-clear-field-field-dikembalikan-dan-reload-bawaan-browser | Edit: Clear Field, Field Dikembalikan Dianggap Bersih, dan Reload Bawaan Browser | FE+BE | 33 | 200, 208, 209 |
| TC-FA-TDC-E2E-065-edit-validasi-class-code-kosong-panjang-dan-whitelist | Edit: Validasi Class Code Kosong, Batas Panjang 15 Karakter, dan Whitelist Karakter | FE+BE | 28 | 220, 221, 222, 223, 224 |
| TC-FA-TDC-E2E-066-edit-validasi-class-code-duplikat-trim-dan-class-name-kosong | Edit: Validasi Class Code Duplikat, Class Name Kosong, dan Class Code Disimpan Ter-trim | FE+BE | 25 | 225, 226, 227, 228, 229 |
| TC-FA-TDC-E2E-067-edit-validasi-class-name-panjang-emoji-trim-dan-duplikat-diizinkan | Edit: Validasi Class Name Batas Panjang 120 Karakter, Emoji, Trim, dan Nama Duplikat Diizinkan | FE+BE | 36 | 230, 231, 232, 233, 234, 235 |
| TC-FA-TDC-E2E-068-edit-validasi-regulation-reference-dan-useful-life-kosong | Edit: Validasi Regulation Reference (Kosong, 255 Karakter, Trim) dan Useful Life Kosong | FE+BE | 30 | 236, 237, 238, 239, 240 |
| TC-FA-TDC-E2E-069-edit-validasi-useful-life-batas-allowed-methods-kosong-dan-debounce | Edit: Validasi Batas Useful Life 1 sampai 100, Allowed Methods Kosong, dan Debounce Keunikan Class Code | FE+BE | 22 | 241, 242, 243, 246 |
| TC-FA-TDC-E2E-070-d-09-screening-dialog-save-changes-dan-pratinjau-dampak | Screening Dialog Save Changes D-09 dan Pratinjau Dampak Jumlah Asset Class dan Aset Aktif | FE+BE | 27 | 248, 249, 250 |
| TC-FA-TDC-E2E-071-d-09-pratinjau-angka-hitung-ulang-shimmer-dan-apply-disabled | Pratinjau Dampak D-09: Daftar Asset Class Terdampak, Angka Bernilai Strip, Hitung Ulang, dan Shimmer dengan Apply Disabled | FE+BE | 30 | 251, 252, 254, 255 |
| TC-FA-TDC-E2E-072-d-09-pilihan-effective-from-tahun-pajak-berjalan-sampai-lima-tahun | Pilihan Effective From pada D-09: Tahun Pajak Berjalan sampai Lima Tahun Setelahnya dan Mulai dari Versi Terakhir Bertanggal | FE+BE | 25 | 256, 257 |
| TC-FA-TDC-E2E-073-d-09-tahun-pajak-closed-soft-closed-dan-open-ditawarkan-atau-tidak | Pilihan Effective From pada D-09: Tahun Pajak yang Seluruh Bulannya Sudah Diekspor Tidak Ditawarkan, Sebagian atau Belum Diekspor Tetap Ditawarkan | FE+BE | 26 | 259, 260, 261 |
| TC-FA-TDC-E2E-074-d-09-effective-from-kosong-cancel-dan-esc | Dialog Save Changes D-09: Cancel dan Esc Menutup Tanpa Menyimpan, Effective From Kosong Ditolak dengan Caption V-19 | FE+BE | 30 | 262, 265, 266 |
| TC-FA-TDC-E2E-075-tahun-pajak-tertutup-menolak-effective-from-dan-pilihan-fiscal-year-start | Tahun Pajak Tertutup pada Pilihan Effective From D-09: Seluruh Bulan Diekspor Tidak Ditawarkan, Sebagian Diekspor Ditawarkan, dan Apply Ditolak dengan Caption V-21 | FE+BE | 35 | 756, 757, 758, 934 |
| TC-FA-TDC-E2E-076-apply-effective-from-hari-ini-dan-masa-depan-membentuk-versi-current-atau-scheduled | Apply Effective From Hari Ini Langsung Membentuk Versi Current dan Effective From Masa Depan Membentuk Versi Scheduled | FE+BE | 35 | 267, 268 |
| TC-FA-TDC-E2E-077-apply-effective-from-sama-dengan-versi-current-atau-scheduled-dan-versi-pertama | Apply Effective From Sama dengan Versi Current atau Scheduled Menggantikan Versi Itu, dan Versi Terakhir Adalah Versi Pertama | FE+BE | 40 | 269, 270, 271 |
| TC-FA-TDC-E2E-078-apply-versi-cancelled-lebih-dari-satu-scheduled-dan-regulation-reference-versi | Apply D-09: Versi Cancelled Tidak Dihitung Versi Terakhir, Lebih dari Satu Versi Scheduled, dan Regulation Reference Menjadi Milik Versi Baru | FE+BE | 41 | 272, 273, 274 |
| TC-FA-TDC-E2E-079-apply-regulation-reference-class-name-dan-allowed-methods-membentuk-versi | Apply D-09: Regulation Reference Diwarisi, Class Name Ditulis Langsung, dan Perubahan Allowed Methods Tanpa Guard Persempit | FE+BE | 39 | 275, 276, 277, 278 |
| TC-FA-TDC-E2E-080-apply-gagal-5xx-klik-ganda-dan-saving-state | Apply D-09: Gagal 5xx Mempertahankan Input, Klik Ganda Hanya Membentuk Satu Versi, dan Tombol Apply Masuk Saving State | FE+BE | 31 | 279, 280, 281 |
| TC-FA-TDC-E2E-081-d-08-blok-persempit-allowed-methods-screening-ok-dan-esc | Dialog D-08 Blok Persempit Allowed Methods: Screening untuk Lebih dari Satu Asset Class, Tombol OK, dan Esc | FE+BE | 25 | 283, 286, 287 |
| TC-FA-TDC-E2E-082-d-08-persempit-bersamaan-useful-life-diganti-metode-dan-semua-effective-from | Guard Persempit D-08: Bersamaan dengan Useful Life Diubah, Mengganti Metode, Metode Tidak Dipakai Tidak Diblokir, dan Berlaku untuk Semua Effective From | FE+BE | 35 | 288, 289, 290, 292 |
| TC-FA-TDC-E2E-083-alert-versi-scheduled-screening-dan-dialog-cancel-scheduled-version-d-10 | Alert Versi Scheduled pada Drawer Edit dan Screening Dialog Cancel Scheduled Version (D-10) | FE+BE | 24 | 294, 295, 296, 297 |
| TC-FA-TDC-E2E-084-cancel-version-dari-modal-versions-back-esc-dan-hasil-cancelled | Cancel Version: Entri dari Modal Versions, Back dan Esc Tidak Membatalkan, serta Hasil Cancelled | FE+BE | 28 | 298, 299, 300, 302 |
| TC-FA-TDC-E2E-085-cancel-version-versi-paling-awal-alert-berikutnya-dan-versi-tidak-berubah | Cancel Version pada Dua Versi Scheduled: Alert Berpindah ke Versi Berikutnya dan Versi Terbentuk Tidak Berubah | FE+BE | 33 | 303, 304, 314 |
| TC-FA-TDC-E2E-086-cancel-version-gagal-5xx-dan-klik-ganda | Cancel Version: Gagal 5xx Mempertahankan D-10 dan Klik Ganda Hanya Membatalkan Satu Kali | FE+BE | 15 | 305, 312 |
| TC-FA-TDC-E2E-087-restore-default-classes-screening-empty-state-dan-dialog-d-12 | Restore Default Classes: Screening Empty State, Posisi Tombol, dan Dialog D-12 (Cancel dan Esc) | FE+BE | 30 | 8, 315, 319, 321, 322 |
| TC-FA-TDC-E2E-088-restore-default-classes-gagal-5xx-saving-state-dan-klik-ganda | Restore Default Classes: Gagal 5xx, Saving State Tombol Restore, dan Klik Ganda Tidak Membuat Class Dobel | FE+BE | 21 | 333, 334, 335 |
| TC-FA-TDC-E2E-089-seed-aktivasi-pertama-modul-akuntansi-tujuh-class-aktif | Seed Aktivasi Pertama Modul Akuntansi: Tujuh Class Aktif dan Tidak Dibuat Ulang Saat Diaktifkan Kembali | FE+BE | 37 | 336, 337, 338, 339 |
| TC-FA-TDC-E2E-090-cancel-version-batas-tahun-pajak-dan-time-zone-entitas | Cancel Version: Batas Tahun Pajak Dimulai Menurut Time Zone Entitas | FE+BE | 33 | 307, 308, 309, 310 |
| TC-FA-TDC-E2E-091-seed-gagal-dan-job-j-01-harian-time-zone-entitas | Job J-01 Harian: Seed Tidak Dibuat Ulang Setelah Dihapus, Dicoba Ulang Setelah Gagal, pada 00:00 Menurut Time Zone Entitas | FE+BE | 26 | 340, 341, 342 |
| TC-FA-TDC-E2E-092-job-j-02-menerapkan-versi-scheduled-pada-effective-from | Job J-02: Menerapkan Versi Scheduled Menjadi Current pada 00:00 Effective From Menurut Time Zone Entitas | FE+BE | 33 | 343, 344, 345, 346 |
| TC-FA-TDC-E2E-093-job-j-02-class-inactive-dan-job-gagal-dicoba-lagi | Job J-02: Class Inactive dan Job Gagal Dicoba Lagi | FE+BE | 16 | 347, 348 |
| TC-FA-TDC-E2E-094-hari-ini-menurut-time-zone-entitas-bukan-utc-dan-versi-pertama | Hari Ini Menurut Time Zone Entitas Menentukan Versi Current atau Scheduled dan Versi Pertama Tidak Mengunci Fiscal Year Start | FE+BE | 26 | 350, 351, 352 |
| TC-FA-TDC-E2E-095-job-j-03-last-posted-tax-year-memajukan-nilai-dan-kunci-class-code | Job J-03: Posting Penyusutan Fiskal Memajukan Last Posted Tax Year dan Mengunci Class Code | FE+BE | 26 | 353, 354, 355, 356, 357 |
| TC-FA-TDC-E2E-096-log-job-j-02-j-03-modified-by-system-dan-job-dua-kali | Log Job J-02 (L-08) dan J-03 (L-10): Modified By System di Changelog dan Activity Log, Tidak di System Log, serta J-02 Dua Kali Tidak Menulis Log Ganda | FE+BE | 49 | 690, 691, 692, 693, 913 |
| TC-FA-TDC-E2E-097-activate-single-screening-cancel-esc-backdrop-dan-row-action-inactive | Activate Single: Screening Dialog, Cancel, Esc, Backdrop, dan Row Action Class Inactive | FE+BE | 30 | 361, 363, 364, 365, 372 |
| TC-FA-TDC-E2E-098-deactivate-single-screening-cancel-esc-dan-backdrop | Deactivate Single: Screening Dialog, Cancel, Esc, dan Backdrop | FE+BE | 24 | 373, 375, 376, 377 |
| TC-FA-TDC-E2E-099-deactivate-single-dialog-blok-used-by-ok-dan-esc | Deactivate Single: Dialog Blok Used By, OK, dan Esc | FE+BE | 22 | 379, 380, 381, 382 |
| TC-FA-TDC-E2E-100-deactivate-single-alert-class-active-terakhir-per-asset-type | Deactivate Single: Alert Class Active Terakhir per Asset Type | FE+BE | 17 | 383, 384, 385, 386 |
| TC-FA-TDC-E2E-101-delete-single-screening-cancel-esc-backdrop-lalu-delete-class | Delete Single: Screening Dialog, Cancel, Esc, Backdrop, lalu Delete Class | FE+BE | 37 | 393, 396, 397, 398, 394, 395 |
| TC-FA-TDC-E2E-102-delete-single-dialog-blok-guard-1-dan-guard-2 | Delete Single: Dialog Blok Guard 1 dan Guard 2 | FE+BE | 17 | 399, 400, 401, 402 |
| TC-FA-TDC-E2E-103-delete-single-tombol-ok-dan-esc-pada-dialog-blok | Delete Single: Tombol OK dan Esc pada Dialog Blok | FE+BE | 28 | 403, 404, 405, 406 |
| TC-FA-TDC-E2E-104-klik-ganda-cepat-pada-konfirmasi-activate-deactivate-dan-delete-single | Klik Ganda Cepat pada Konfirmasi Activate, Deactivate, dan Delete Single | FE+BE | 28 | 371, 392, 412 |
| TC-FA-TDC-E2E-105-resilience-activate-deactivate-single-5xx-dan-timeout | Resilience Activate dan Deactivate Single: Gagal 5xx dan Timeout | FE+BE | 40 | 369, 370, 390, 391 |
| TC-FA-TDC-E2E-106-resilience-delete-single-5xx-timeout-dan-retry-activate-deactivate | Resilience Delete Single: Gagal 5xx dan Timeout, serta Retry Activate dan Deactivate | FE+BE | 43 | 410, 411, 899, 900 |
| TC-FA-TDC-E2E-107-resilience-bulk-deactivate-dan-activate-5xx-timeout | Resilience Bulk Deactivate dan Bulk Activate: Gagal 5xx dan Timeout | FE+BE | 38 | 481, 482, 483 |
| TC-FA-TDC-E2E-108-resilience-bulk-activate-delete-5xx-timeout-dan-retry-delete | Resilience Bulk Activate dan Bulk Delete: Timeout, Gagal 5xx, dan Retry Delete | FE+BE | 50 | 484, 485, 486, 901 |
| TC-FA-TDC-E2E-109-class-yang-pernah-diposting-siklus-deactivate-activate-dan-edit-lalu-delete | Class yang Pernah Diposting, Siklus Deactivate dan Activate, serta Edit lalu Delete Class Inactive | FE+BE | 35 | 902, 903, 904, 908 |
| TC-FA-TDC-E2E-110-bulk-action-bar-screening-seleksi-select-all-dan-aksi-per-status | Bulk Action Bar Screening Seleksi Select All dan Aksi per Status | FE+BE | 38 | 413, 414, 415, 416, 417, 418, 419 |
| TC-FA-TDC-E2E-111-bulk-action-bar-unselect-all-icon-seleksi-dipertahankan-saat-filter | Bulk Action Bar Unselect All Icon dan Seleksi Dipertahankan saat Filter | FE+BE | 29 | 420, 421, 422, 425 |
| TC-FA-TDC-E2E-112-dialog-bulk-screening-deactivate-jamak-campuran-dan-blok | Dialog Bulk Screening Deactivate Jamak Campuran dan Blok | FE+BE | 28 | 426, 427, 428 |
| TC-FA-TDC-E2E-113-dialog-bulk-screening-activate-delete-jamak-campuran-dan-blok | Dialog Bulk Screening Activate Delete Jamak Campuran dan Blok | FE+BE | 35 | 429, 430, 431, 432 |
| TC-FA-TDC-E2E-114-dialog-bulk-cancel-deactivate-jamak-dan-campuran-mempertahankan-seleksi | Dialog Bulk Cancel Deactivate Jamak dan Campuran Mempertahankan Seleksi | FE+BE | 28 | 433, 434 |
| TC-FA-TDC-E2E-115-dialog-bulk-cancel-delete-campuran-dan-tombol-ok-deactivate-jamak-blok | Dialog Bulk Cancel Delete Campuran dan Tombol OK Deactivate Jamak Blok | FE+BE | 28 | 437, 438 |
| TC-FA-TDC-E2E-116-dialog-bulk-esc-deactivate-activate-dan-delete-jamak | Dialog Bulk Esc Deactivate Activate dan Delete Jamak | FE+BE | 33 | 441, 442, 443 |
| TC-FA-TDC-E2E-117-dialog-bulk-esc-campuran-dan-backdrop-d-14-d-15 | Dialog Bulk Esc Campuran dan Backdrop D-14 D-15 | FE+BE | 35 | 444, 445, 446 |
| TC-FA-TDC-E2E-118-matriks-bulk-deactivate-1-sampai-4a | Matriks Bulk Deactivate 1 sampai 4a | FE+BE | 32 | 447, 448, 449, 450 |
| TC-FA-TDC-E2E-119-matriks-bulk-deactivate-4b-4c-dan-5-collapse-ke-dialog-single | Matriks Bulk Deactivate 4b 4c dan 5 Collapse ke Dialog Single | FE+BE | 36 | 451, 452, 453, 454, 455 |
| TC-FA-TDC-E2E-120-matriks-bulk-deactivate-6-habis-asset-type-dan-bulk-activate | Matriks Bulk Deactivate 6 Habis Asset Type dan Bulk Activate | FE+BE | 46 | 456, 457, 458, 459, 460, 461 |
| TC-FA-TDC-E2E-121-matriks-bulk-delete-9-sampai-11 | Matriks Bulk Delete 9 sampai 11 | FE+BE | 36 | 462, 463, 464, 465, 466 |
| TC-FA-TDC-E2E-122-matriks-bulk-delete-12-satu-baris-lintas-halaman-dan-menghapus-seluruh-class | Matriks Bulk Delete 12 Satu Baris Lintas Halaman dan Menghapus Seluruh Class | FE+BE | 47 | 467, 468, 469, 905, 906, 907 |
| TC-FA-TDC-E2E-123-konflik-dua-admin-create-class-code-sama-batas-tercapai-dan-batas-dinaikkan | Konflik Dua Admin: Create Class Code Sama, Batas Tercapai, dan Batas Dinaikkan | FE+BE | 40 | 117, 132, 763 |
| TC-FA-TDC-E2E-124-konflik-dua-admin-edit-class-name-dan-class-dihapus-saat-save | Konflik Dua Admin: Edit Class Name Bersamaan dan Class Dihapus Saat Save | FE+BE | 23 | 201, 202 |
| TC-FA-TDC-E2E-125-konflik-d-13-class-code-terkunci-saat-drawer-terbuka | Konflik D-13: Class Code Terkunci Saat Drawer Edit Terbuka, Penolakan Save, Screening Dialog, dan Tombol OK | FE+BE | 22 | 210, 211, 212 |
| TC-FA-TDC-E2E-126-konflik-d-13-esc-save-tanpa-ubah-class-code-dan-fokus | Konflik D-13: Esc dan Fokus Dialog serta Save Tanpa Mengubah Class Code Tetap Berhasil | FE+BE | 22 | 213, 214, 921 |
| TC-FA-TDC-E2E-127-konflik-d-09-tahun-pajak-tertutup-dan-effective-from-lebih-awal-dari-versi-terakhir | Konflik D-09: Tahun Pajak yang Baru Ditutup dan Effective From Lebih Awal dari Versi Terakhir yang Baru Dibentuk | FE+BE | 29 | 263, 264 |
| TC-FA-TDC-E2E-128-konflik-cancel-version-versi-berubah-atau-class-dihapus | Konflik Cancel Version: Versi Sudah Dibatalkan Sesi Lain atau Class Dihapus Sesi Lain | FE+BE | 20 | 306, 311 |
| TC-FA-TDC-E2E-129-konflik-restore-tabel-basi-pratinjau-reaktivasi-dan-dilewati | Konflik Restore Default Classes: Tabel Basi, Pratinjau Reaktivasi dan Dilewati, serta Nilai Tidak Ditimpa | FE+BE | 38 | 320, 325, 326 |
| TC-FA-TDC-E2E-130-konflik-restore-kapitalisasi-all-exist-dan-seed-dibuat-admin-lain | Konflik Restore Default Classes: Kapitalisasi Class Code, Semua Seed Sudah Ada, dan Seed Dibuat Admin Lain Antara Pratinjau dan Restore | FE+BE | 28 | 327, 328, 332 |
| TC-FA-TDC-E2E-131-konflik-restore-d-07-batas-terlampaui-saat-restore | Konflik Restore Default Classes: Batas Master Data Count Limit Terlampaui Saat Klik Restore atau Konfirmasi | FE+BE | 24 | 329, 330, 331 |
| TC-FA-TDC-E2E-132-konflik-activate-deactivate-single-class-berubah-saat-dialog-terbuka | Konflik Activate dan Deactivate Single: Class Berubah Saat Dialog Konfirmasi Terbuka | FE+BE | 45 | 367, 368, 387, 388, 389 |
| TC-FA-TDC-E2E-133-konflik-delete-single-class-berubah-saat-dialog-terbuka | Konflik Delete Single: Class Berubah Saat Dialog Delete Terbuka | FE+BE | 42 | 407, 408, 409, 895 |
| TC-FA-TDC-E2E-134-konflik-dua-sesi-deactivate-class-name-dan-bulk-delete | Konflik Dua Sesi: Deactivate dan Edit Class Name pada Class yang Sama, Bulk Delete Setelah Sesi Lain Menonaktifkan, dan Deactivate Class Terakhir bertipe Land | FE+BE | 32 | 896, 897, 898 |
| TC-FA-TDC-E2E-135-konflik-bulk-deactivate-delete-class-menjadi-dipakai-atau-diposting | Konflik Bulk Deactivate dan Bulk Delete: Class Menjadi Dipakai Asset Class Antara Dialog Dibuka dan Konfirmasi | FE+BE | 51 | 470, 471, 472, 473 |
| TC-FA-TDC-E2E-136-konflik-bulk-deactivate-activate-delete-sebagian-class-dihapus-sesi-lain | Konflik Bulk: Class Diposting, Sebagian atau Seluruh Class Dihapus Sesi Lain Saat Confirm Bulk Delete, Deactivate, dan Activate | FE+BE | 45 | 474, 475, 476, 477 |
| TC-FA-TDC-E2E-137-konflik-bulk-delete-activate-class-dihapus-sesi-lain | Konflik Bulk Delete dan Bulk Activate: Sebagian atau Seluruh Class Sudah Dihapus Sesi Lain Saat Confirm | FE+BE | 35 | 478, 479, 480 |
| TC-FA-TDC-E2E-138-konflik-popup-used-by-kosong-dan-log-activate-deactivate-idempoten | Konflik Dua Sesi: Popup Used By Kosong pada Data Usang dan Log Activate serta Deactivate yang Idempoten | FE+BE | 39 | 586, 720, 721 |
| TC-FA-TDC-E2E-139-konflik-konfigurasi-kolom-per-browser-dan-tab-baru | Multi-Konteks: Konfigurasi Kolom Tersimpan per Browser dan Tab Browser Baru Memulai dari State Default | FE+BE | 22 | 551, 563 |
| TC-FA-TDC-E2E-140-konflik-capability-diubah-saat-user-lain-login | Konflik Capability: Update dan Delete pada Manage accounting Diberikan atau Dicabut Saat User Lain Sedang Login | FE+BE | 38 | 771, 772, 773 |
| TC-FA-TDC-E2E-141-konflik-capability-delete-dicabut-dan-tingkat-akses-berubah | Konflik Capability: Delete Dicabut dari Manage accounting dan Tingkat Akses User Berubah Saat User Sedang Login | FE+BE | 43 | 774, 775, 776 |
| TC-FA-TDC-E2E-142-isolasi-data-antar-client-daftar-baca-dan-class-code-sama | Isolasi Data Antar Client: Daftar Class, Request Baca, Deactivate, Delete, dan Bulk Deactivate Lintas Client Ditolak serta Class Code yang Sama Boleh Dipakai di Dua Client | FE+BE | 32 | 859, 860, 861, 862, 863, 864 |
| TC-FA-TDC-E2E-143-search-siklus-interaksi-kolom-teks-dan-tidak-case-sensitive | Search: Siklus Interaksi, Kolom Teks, dan Tidak Case-Sensitive | FE+BE | 39 | 489, 490, 491, 492 |
| TC-FA-TDC-E2E-144-search-kolom-hidden-regulation-reference-modified-by-dan-class-name | Search: Kolom Hidden Mengikuti Visibilitas Kolom | FE+BE | 31 | 493, 494, 495 |
| TC-FA-TDC-E2E-145-search-trim-teks-biasa-hasil-kosong-dan-irisan-dengan-filter | Search: Trim, Teks Biasa, Hasil Kosong, dan Irisan dengan Filter | FE+BE | 34 | 498, 499, 500, 501, 502 |
| TC-FA-TDC-E2E-146-kombinasi-search-filter-sort-dan-pagination-berlaku-bersamaan | Kombinasi Search, Filter, Sort, dan Pagination Berlaku Bersamaan | FE+BE | 51 | 503, 504, 505, 506 |
| TC-FA-TDC-E2E-147-filter-panel-screening-guard-field-dan-opsi-dropdown | Filter Panel: Screening, Guard Field, dan Opsi Dropdown | FE+BE | 38 | 507, 508, 509, 510 |
| TC-FA-TDC-E2E-148-filter-multi-select-or-allowed-methods-dan-range-numerik | Filter: Multi-Select, Logika OR, Allowed Methods, dan Range Numerik | FE+BE | 40 | 511, 512, 513, 514, 515 |
| TC-FA-TDC-E2E-149-filter-date-and-search-dropdown-chip-dan-hapus-opsi | Filter: Date Range, Logika AND, Search Dropdown, Chip, dan Hapus Opsi | FE+BE | 40 | 516, 517, 518, 519, 520, 521 |
| TC-FA-TDC-E2E-150-filter-chip-sinkron-overflow-clear-all-dan-menutup-tanpa-apply | Filter: Sinkron Chip, Overflow +N more, Clear All, dan Menutup Panel Tanpa Apply | FE+BE | 35 | 522, 523, 524, 525 |
| TC-FA-TDC-E2E-151-sort-default-siklus-tiga-tahap-teks-dan-numerik | Sort: Urutan Default, Siklus Tiga Tahap, Kolom Teks, dan Kolom Numerik | FE+BE | 44 | 14, 528, 529, 530, 531 |
| TC-FA-TDC-E2E-152-sort-active-effective-from-last-updated-guard-dan-urutan-deterministik | Sort: Active, Effective From, Last Updated, Guard Kolom, dan Urutan Deterministik | FE+BE | 42 | 532, 533, 534, 535, 536, 537, 538 |
| TC-FA-TDC-E2E-153-setup-column-tabel-utama-screening-overlay-popup-dan-kolom-default-tampil | Setup Column Tabel Utama: Screening Overlay dan Popup, serta Kolom Default Tampil | FE+BE | 32 | 539, 540, 541 |
| TC-FA-TDC-E2E-154-setup-column-tabel-utama-geser-dan-pin-kolom-default-tampil | Setup Column Tabel Utama: Geser dan Pin Kolom yang Tampil Secara Default | FE+BE | 27 | 542, 543 |
| TC-FA-TDC-E2E-155-setup-column-tabel-utama-kolom-tersembunyi-default-dan-reset | Setup Column Tabel Utama: Kolom Tersembunyi Secara Default dan Reset to Default | FE+BE | 57 | 544, 545, 546, 547 |
| TC-FA-TDC-E2E-156-setup-column-tabel-utama-tutup-tanpa-save-guard-panel-cepat-dan-lintas-popup | Setup Column Tabel Utama: Tutup Tanpa Save, Guard Satu Kolom, Panel Cepat, dan Independensi Lintas Popup | FE+BE | 73 | 548, 549, 550, 552, 553 |
| TC-FA-TDC-E2E-157-pagination-page-size-navigasi-input-halaman-dan-ganti-page-size | Pagination: Page Size, Navigasi, Input Nomor Halaman, dan Penggantian Page Size | FE+BE | 39 | 554, 555, 556, 557, 558 |
| TC-FA-TDC-E2E-158-pagination-halaman-terakhir-dan-state-tabel-dipertahankan-atau-direset | Pagination: State Tabel Dipertahankan atau Direset dan Halaman Terakhir Sesudah Delete | FE+BE | 47 | 559, 560, 561, 562, 931 |
| TC-FA-TDC-E2E-159-download-tabel-overlay-nama-berkas-cakupan-baris-dan-tanpa-aksi-export | Download Tabel: Overlay, Nama Berkas, Cakupan Baris, dan Tanpa Aksi Export | FE+BE | 36 | 564, 565, 566, 567, 568, 914 |
| TC-FA-TDC-E2E-160-download-isi-berkas-kolom-tampil-teks-active-strip-format-effective-from-dan-angka | Download Isi Berkas: Kolom Tampil, Teks Active, Strip, Format Effective From, dan Angka | FE+BE | 32 | 569, 570, 571, 572, 573 |
| TC-FA-TDC-E2E-161-download-isi-berkas-modified-by-bom-escaping-urutan-dan-hasil-kosong | Download Isi Berkas: Modified By, BOM, Escaping, Urutan, dan Hasil Kosong | FE+BE | 30 | 574, 575, 576, 577 |
| TC-FA-TDC-E2E-162-download-gagal-toast-error-tabel-used-by-dan-changelog | Download Gagal: Toast Error Tabel, Used By, dan Changelog | FE+BE | 24 | 578, 594, 930 |
| TC-FA-TDC-E2E-163-popup-used-by-screening-dan-isi-kolom | Popup Used By: Screening dan Isi Kolom | FE+BE | 16 | 579, 580 |
| TC-FA-TDC-E2E-164-popup-used-by-search-sort-pagination-dan-empty-state-hasil | Popup Used By: Search, Sort, Pagination, dan Empty State Hasil | FE+BE | 31 | 583, 584, 585, 587, 588 |
| TC-FA-TDC-E2E-165-popup-used-by-menutup-dan-hanya-dibuka-dari-angka-lebih-dari-nol | Popup Used By: Menutup dan Hanya Dibuka dari Angka Lebih dari Nol | FE+BE | 13 | 589, 590 |
| TC-FA-TDC-E2E-166-popup-used-by-download-opsi-nama-berkas-dan-isi-berkas | Popup Used By Download: Opsi, Nama Berkas, dan Isi Berkas | FE+BE | 38 | 591, 592, 593, 929 |
| TC-FA-TDC-E2E-167-popup-used-by-column-visibility-dan-setup-column-screening-reset-dan-tutup-tanpa-save | Popup Used By: Column Visibility, Setup Column Screening, Reset, dan Tutup Tanpa Save | FE+BE | 40 | 595, 596, 600, 601 |
| TC-FA-TDC-E2E-168-popup-used-by-setup-column-ceklis-unceklis-dan-guard-satu-kolom-tersisa | Popup Used By Setup Column: Ceklis dan Unceklis serta Guard Satu Kolom Tersisa | FE+BE | 33 | 597, 602 |
| TC-FA-TDC-E2E-169-popup-versions-screening-badge-status-isi-kolom-dan-class-land | Popup Versions: Screening, Badge Status, Isi Kolom, dan Class Land | FE+BE | 32 | 603, 604, 605, 606 |
| TC-FA-TDC-E2E-170-popup-versions-urutan-tetap-tanpa-sort-search-download-dan-paginasi | Popup Versions: Urutan Tetap, Tanpa Sort, Search, Download, dan Pagination | FE+BE | 27 | 607, 608, 609, 610 |
| TC-FA-TDC-E2E-171-popup-versions-menutup-satu-versi-current | Popup Versions: Menutup dan Satu Versi Current | FE+BE | 17 | 611, 612 |
| TC-FA-TDC-E2E-172-popup-changelog-screening-tooltip-toolbar-dan-kolom-date-action-class-code | Popup Changelog: Screening, Tooltip Toolbar, serta Kolom Date, Action, dan Class Code | FE+BE | 23 | 613, 614, 619, 620 |
| TC-FA-TDC-E2E-173-popup-changelog-download-nama-berkas-dan-filter-aktif | Popup Changelog Download: Overlay, Nama Berkas, dan Filter Aktif | FE+BE | 24 | 615, 616, 617, 618 |
| TC-FA-TDC-E2E-174-popup-changelog-kolom-old-new-value-modified-by-urutan-bawaan-dan-sort-date | Popup Changelog: Kolom Old Value, New Value, Modified By, Urutan Bawaan, dan Sort Date | FE+BE | 29 | 621, 622, 623, 624 |
| TC-FA-TDC-E2E-175-popup-changelog-sort-campuran-modified-by-dan-search-per-kolom | Popup Changelog: Sort Kolom Campuran, Sort Modified By, dan Search per Kolom | FE+BE | 34 | 625, 626, 627, 628 |
| TC-FA-TDC-E2E-176-popup-changelog-filter-panel-opsi-multi-select-or-date-dan-and | Popup Changelog Filter Panel: Screening, Opsi, Multi-Select, OR, Date, dan AND | FE+BE | 40 | 629, 630, 631, 632, 633, 634 |
| TC-FA-TDC-E2E-177-popup-changelog-search-filter-bersamaan-empty-state-paginasi-dan-menutup | Popup Changelog: Search dan Filter Bersamaan, Empty State, Paginasi, dan Menutup Popup | FE+BE | 40 | 635, 636, 637, 638, 639 |
| TC-FA-TDC-E2E-178-popup-changelog-setup-column-screening-overlay-popup-dan-kolom-default | Popup Changelog Setup Column: Screening Overlay, Popup, dan Kolom Default | FE+BE | 19 | 640, 641 |
| TC-FA-TDC-E2E-179-popup-changelog-setup-column-geser-urutan-kolom | Popup Changelog Setup Column: Geser Urutan Kolom | FE+BE | 15 | 643 |
| TC-FA-TDC-E2E-180-popup-changelog-setup-column-tutup-tanpa-save-dan-guard | Popup Changelog Setup Column: Reset to Default, Tutup Tanpa Save, dan Guard Satu Kolom Tersisa | FE+BE | 39 | 645, 646, 647 |
| TC-FA-TDC-E2E-181-guided-tooltip-isi-enam-langkah-kunjungan-pertama-dan-empty-state | Guided Tooltip: Isi Enam Langkah, Kunjungan Pertama, dan Empty State | FE+BE | 32 | 648, 649, 650, 651 |
| TC-FA-TDC-E2E-182-guided-tooltip-replay-skip-dan-tombol-back | Guided Tooltip: Replay, Skip, dan Tombol Back | FE+BE | 33 | 652, 653, 654, 655 |
| TC-FA-TDC-E2E-183-guided-tooltip-done-resize-viewport-dan-navigasi-halaman | Guided Tooltip: Done, Resize Viewport, dan Navigasi Halaman | FE+BE | 27 | 656, 657, 658 |
| TC-FA-TDC-E2E-184-guided-tooltip-keyboard-dan-replay-melewati-kolom-tersembunyi | Guided Tooltip: Keyboard dan Replay Melewati Kolom Tersembunyi | FE+BE | 39 | 659, 933 |
| TC-FA-TDC-E2E-185-android-tabel-card-list-toggle-dialog-drawer-dan-popup | Android: Card List, Toggle Active, Dialog Bottom Sheet, Form Halaman Penuh, dan Popup Used By | FE+BE | 22 | 660, 661, 663, 664, 665 |
| TC-FA-TDC-E2E-186-android-toolbar-aksi-baris-restore-guided-tooltip-dan-akses-read-only | Android: Toolbar, Aksi Baris, Restore Default Classes, Guided Tooltip, dan Akses Read Only | FE+BE | 40 | 666, 667, 669, 670, 671, 662, 668 |
| TC-FA-TDC-E2E-187-log-l-01-create-seed-j-01-l-09-cancel-version-dan-l-11 | Pencatatan Log L-01, L-09, dan L-11 pada Changelog, System Log, dan Activity Log: Seed J-01, Create Class, Cancel Scheduled Version, dan Penggantian Versi Scheduled | FE+BE | 75 | 673, 672, 688, 689 |
| TC-FA-TDC-E2E-188-log-l-02-edit-class-name-regulation-reference-dan-class-code | Pencatatan Log L-02 pada Tiga Surface: Edit Class Name, Regulation Reference, dan Class Code | FE+BE | 55 | 675, 676, 677 |
| TC-FA-TDC-E2E-189-log-l-02-class-code-tidak-diperbarui-ulang-edit-sekaligus-dan-kapitalisasi | Pencatatan Log L-02 pada Tiga Surface: Class Code Tidak Diperbarui Ulang, Edit Tiga Field Sekaligus, dan Perubahan Kapitalisasi | FE+BE | 61 | 678, 679, 680 |
| TC-FA-TDC-E2E-190-log-l-03-versi-baru-allowed-methods-dan-effective-from-sama | Pencatatan Log L-03: Versi Baru dari Useful Life, Allowed Methods, Regulation Reference, dan Effective From Sama dengan Versi Current | FE+BE | 76 | 682, 683, 684, 932 |
| TC-FA-TDC-E2E-191-log-l-03-old-value-strip-penggantian-versi-dan-record-scheduled | Pencatatan Log L-03 dan L-11: Old Value Effective From Strip, Penggantian Versi dengan Effective From Sama, dan Record Scheduled | FE+BE | 44 | 685, 686, 687 |
| TC-FA-TDC-E2E-192-log-activate-deactivate-single-tiga-surface | Pencatatan Log L-04 Activate dan Deactivate Single: Changelog, System Log, dan Activity Log | FE+BE | 30 | 698, 699, 700, 701, 702 |
| TC-FA-TDC-E2E-193-log-deactivate-activity-log-dan-delete-single-tiga-surface | Pencatatan Log L-04 Deactivate pada Activity Log dan L-05 Delete Single: Changelog, System Log, dan Activity Log | FE+BE | 26 | 703, 704, 705, 706 |
| TC-FA-TDC-E2E-194-log-bulk-deactivate-dan-bulk-activate-satu-kejadian-per-class | Pencatatan Log L-04 Bulk Deactivate dan Bulk Activate: Satu Kejadian per Class di Tiga Surface | FE+BE | 37 | 707, 708, 709, 710, 711 |
| TC-FA-TDC-E2E-195-log-bulk-activate-activity-log-dan-bulk-delete-satu-kejadian-per-class | Pencatatan Log L-04 Bulk Activate pada Activity Log dan L-05 Bulk Delete: Satu Kejadian per Class di Tiga Surface | FE+BE | 32 | 712, 713, 714, 715 |
| TC-FA-TDC-E2E-196-log-entri-class-dihapus-utuh-modified-by-hover-dan-system-log-aktor | Pencatatan Log: Entri Lama Tidak Berubah, Modified By Hover Nama Lengkap, dan Isolasi System Log per Aktor | FE+BE | 49 | 787, 723, 724, 722 |
| TC-FA-TDC-E2E-197-absence-log-edit-no-op-posting-lebih-lama-dan-batas-d-07 | Absence Log: Edit No-Op, Posting Tahun Pajak Sama atau Lebih Lama, dan Batas D-07 Tidak Menulis Entri | FE+BE | 36 | 681, 694, 134 |
| TC-FA-TDC-E2E-198-absence-log-kejadian-system-dan-aksi-dilewati-atau-diblokir | Absence Log: Kejadian System Tidak Ditulis ke System Log, Aksi Bulk Dilewati, dan Aksi yang Diblokir Dialog | FE+BE | 86 | 719, 718, 716, 717, 697 |
| TC-FA-TDC-E2E-199-asset-class-dropdown-hanya-class-active-serta-aktivasi-deaktivasi-dan-penghapusan-class | Asset Class: Dropdown Tax Depreciation Class Hanya Memuat Class Active dan Mengikuti Aktivasi, Deaktivasi, dan Penghapusan | FE+BE | 39 | 725, 726, 727, 728 |
| TC-FA-TDC-E2E-200-asset-class-tax-method-useful-life-rate-dan-opsi-land | Asset Class: Opsi Tax Method, Useful Life dan Rate, serta Opsi Class Land | FE+BE | 32 | 733, 734, 735, 736, 737, 738, 739 |
| TC-FA-TDC-E2E-201-used-by-bertambah-berkurang-dihapus-inactive-dan-banyak-asset-name | Used By: Bertambah, Berkurang, Asset Class Dihapus, Asset Class Inactive, dan Banyak Asset Name | FE+BE | 45 | 740, 741, 742, 743, 744 |
| TC-FA-TDC-E2E-202-used-by-guard-deactivate-delete-lolos-dan-label-modal | Used By: Guard Deactivate dan Delete Menjadi Lolos, dan Label Modal Mengikuti Class Name | FE+BE | 37 | 746, 747, 748 |
| TC-FA-TDC-E2E-203-fiscal-year-start-terkunci-oleh-versi-bertanggal | Preferences: Fiscal Year Start Terkunci oleh Versi Bertanggal dan Tidak Terkunci oleh Versi Pertama | FE+BE | 41 | 749, 750, 751, 752 |
| TC-FA-TDC-E2E-204-fiscal-year-start-terbuka-kembali-dan-pilihan-effective-from-mengikuti | Preferences: Fiscal Year Start Terbuka Kembali dan Pilihan Effective From Mengikuti Fiscal Year Start | FE+BE | 68 | 753, 754, 755, 924, 925 |
| TC-FA-TDC-E2E-205-sinkron-tab-asset-class-activity-log-approval-dan-lifecycle-aset | Sinkronisasi Lintas Modul: Tab Asset Class, Activity Log, Approvals, Asset Name, dan Lifecycle Aset | FE+BE | 59 | 770, 777, 778, 784, 785, 786 |
| TC-FA-TDC-E2E-206-general-settings-format-tanggal-jam-dan-zona-waktu-changelog-dan-last-updated | General Settings: Format Tanggal, Jam, dan Zona Waktu pada Changelog, Date Filter, Last Updated, dan Effective From | FE+BE | 37 | 779, 780, 781, 782, 783 |
| TC-FA-TDC-E2E-207-role-matrix-request-langsung-activate-ditolak | Role Matrix Negatif: Request Langsung Activate Ditolak | FE+BE | 6 | 791, 792, 793, 794 |
| TC-FA-TDC-E2E-208-role-matrix-request-langsung-deactivate-ditolak | Role Matrix Negatif: Request Langsung Deactivate Ditolak | FE+BE | 6 | 795, 796, 797, 798 |
| TC-FA-TDC-E2E-209-role-matrix-request-langsung-delete-ditolak | Role Matrix Negatif: Request Langsung Delete Ditolak | FE+BE | 7 | 799, 800, 801, 802 |
| TC-FA-TDC-E2E-210-role-matrix-request-langsung-bulk-activate-ditolak | Role Matrix Negatif: Request Langsung Bulk Activate Ditolak | FE+BE | 6 | 803, 804, 805, 806 |
| TC-FA-TDC-E2E-211-role-matrix-request-langsung-bulk-deactivate-ditolak | Role Matrix Negatif: Request Langsung Bulk Deactivate Ditolak | FE+BE | 6 | 807, 808, 809, 810 |
| TC-FA-TDC-E2E-212-role-matrix-request-langsung-bulk-delete-ditolak | Role Matrix Negatif: Request Langsung Bulk Delete Ditolak | FE+BE | 6 | 811, 812, 813, 814 |
| TC-FA-TDC-E2E-213-role-matrix-request-langsung-create-ditolak | Role Matrix Negatif: Request Langsung Create Ditolak | FE+BE | 7 | 815, 816, 817, 818 |
| TC-FA-TDC-E2E-214-role-matrix-request-langsung-edit-ditolak | Role Matrix Negatif: Request Langsung Edit Ditolak | FE+BE | 6 | 819, 820, 821, 822 |
| TC-FA-TDC-E2E-215-role-matrix-request-langsung-cancel-scheduled-version-ditolak | Role Matrix Negatif: Request Langsung Cancel Scheduled Version Ditolak | FE+BE | 6 | 823, 824, 825, 826 |
| TC-FA-TDC-E2E-216-role-matrix-request-langsung-restore-default-classes-ditolak | Role Matrix Negatif: Request Langsung Restore default classes Ditolak | FE+BE | 7 | 827, 828, 829, 830 |
| TC-FA-TDC-E2E-217-request-langsung-starter-suspended-bypass-ui-dan-rate-dari-klien-diabaikan | Request Langsung: Plan Starter dan Entitas Suspended Ditolak serta Rate dari Klien Diabaikan | FE+BE | 27 | 173, 831, 888 |
| TC-FA-TDC-E2E-218-request-langsung-pemanggil-terotorisasi-tercatat-di-tiga-surface | Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Create, Deactivate, dan Delete | FE+BE | 36 | 832, 833, 909 |
| TC-FA-TDC-E2E-219-request-langsung-guard-deactivate-delete-dan-bulk-hanya-yang-lolos | Request Langsung: Guard Deactivate dan Delete serta Bulk Memproses Hanya Class yang Lolos | FE+BE | 31 | 834, 835, 836, 837, 838 |
| TC-FA-TDC-E2E-220-request-langsung-asset-type-class-code-terkunci-persempit-land-building | Request Langsung: Asset Type, Class Code Terkunci, Persempit Allowed Methods, serta Land dan Building Ditolak | FE+BE | 32 | 839, 840, 841, 842, 843, 964 |
| TC-FA-TDC-E2E-221-request-langsung-class-code-kembar-effective-from-dan-cancel-version | Request Langsung: Class Code Kembar, Effective From Tidak Valid, dan Cancel Version Ditolak | FE+BE | 29 | 844, 845, 846, 847, 848, 849 |
| TC-FA-TDC-E2E-222-request-langsung-validasi-class-name-class-code-dan-regulation-reference | Request Langsung: Validasi Class Name, Class Code, dan Regulation Reference Ditolak Server | FE+BE | 25 | 851, 852, 853, 854, 855 |
| TC-FA-TDC-E2E-223-request-langsung-validasi-useful-life-field-wajib-dan-rentang-effective-from | Request Langsung: Validasi Useful Life, Field Wajib, dan Rentang Effective From | FE+BE | 31 | 856, 857, 858, 926, 927, 928 |
| TC-FA-TDC-E2E-224-bypass-ui-create-building-dan-land-ditolak-server-dan-rate-klien-diabaikan | Bypass UI Create: Building dan Land Ditolak Server serta Rate dari Klien Diabaikan | FE+BE | 38 | 160, 161, 850 |
| TC-FA-TDC-E2E-225-injeksi-script-class-name-tampil-sebagai-teks-di-tabel-dialog-dan-drawer | Injeksi Script pada Class Name Tampil sebagai Teks di Tabel, Dialog, dan Drawer | FE+BE | 21 | 865, 866, 867, 868, 869 |
| TC-FA-TDC-E2E-226-injeksi-script-sql-dropdown-asset-class-changelog-regulation-reference | Injeksi Script dan SQL: Dropdown Asset Class, Changelog, dan Regulation Reference Tampil sebagai Teks | FE+BE | 35 | 870, 871, 872, 873 |
| TC-FA-TDC-E2E-227-aksesibilitas-fokus-ter-trap-dialog-blok-d-02-d-04-d-05-dan-d-08 | Aksesibilitas Fokus Ter-trap Dialog Blok D-02, D-04, D-05 dan D-08 | FE+BE | 31 | 918, 920 |
| TC-FA-TDC-E2E-228-aksesibilitas-fokus-ter-trap-modal-versions-dan-popup-changelog | Aksesibilitas Fokus Ter-trap Modal Versions dan Popup Changelog | FE+BE | 12 | 922, 923 |
| TC-FA-TDC-E2E-229-role-matrix-positif-restore-default-classes-di-empty-state-pemegang-create | Role Matrix Positif: Restore default classes di Empty State bagi Pemegang Create | FE+BE | 5 | 51 |
| TC-FA-TDC-E2E-231-state-tenant-suspended-expired-search-changelog-dan-download-csv-tetap-tersedia | State Tenant Suspended dan Expired: Search, Popup Changelog, dan Download CSV Tetap Tersedia | FE+BE | 25 | 101 |
| TC-FA-TDC-E2E-232-batas-master-data-count-limit-slot-terakhir-dan-stay-on-form-hingga-batas | Batas Master Data Count Limit: Create pada Slot Terakhir Diizinkan, lalu Ditolak D-07, Termasuk Create Berulang dengan Stay on This Form | FE+BE | 32 | 130, 133 |
| TC-FA-TDC-E2E-233-create-berhasil-mengosongkan-search-clear-filter-dan-sort-default-di-halaman-dua | Create Berhasil Mengosongkan Search, Meng-clear Filter Panel, dan Memuat Ulang Tabel di Sort Default | FE+BE | 15 | 110 |
| TC-FA-TDC-E2E-234-create-tombol-clear-field-mengosongkan-semua-field-tanpa-menutup-drawer | Create - Tombol Clear Field Mengosongkan Semua Field Tanpa Menutup Drawer | FE+BE | 19 | 113 |
| TC-FA-TDC-E2E-235-drawer-edit-header-badge-status-dan-effective-from-versi-current | Drawer Edit: Effective From Versi Current Read-Only dan Header Badge Status | FE+BE | 21 | 32, 179 |
| TC-FA-TDC-E2E-236-edit-langsung-class-code-dan-gabungan-tiga-field | Edit Langsung Tanpa Versi Baru: Class Code dan Gabungan Class Code, Class Name, Regulation Reference | FE+BE | 26 | 191, 192 |
| TC-FA-TDC-E2E-237-d-08-teks-satu-asset-class-pemakai-dan-metode-straight-line-yang-dihapus | Dialog D-08: Teks untuk Tepat Satu Asset Class Pemakai dan Penyebutan Straight Line sebagai Metode yang Dihapus | FE+BE | 23 | 284, 285 |
| TC-FA-TDC-E2E-238-d-09-pilihan-effective-from-berlabel-bulan-fiscal-year-start-april | Pilihan Effective From pada D-09 Berlabel Bulan Fiscal Year Start Non-Januari (April) | FE+BE | 13 | 258 |
| TC-FA-TDC-E2E-239-restore-default-classes-hasil-nilai-class-sama-dengan-seed | Restore Default Classes: Nilai Class Hasil Restore Sama dengan Nilai Seed | FE+BE | 17 | 324 |
| TC-FA-TDC-E2E-240-last-posted-tax-year-tidak-dapat-diubah-dan-tahun-pajak-fiscal-year-start-april | Last Posted Tax Year Tidak Dapat Diubah dari UI dan Dicatat sebagai Tahun Kalender Awal Tahun Pajak (Fiscal Year Start April) | FE+BE | 15 | 358, 359 |
| TC-FA-TDC-E2E-241-activate-dan-deactivate-single-confirm-sukses-loading-dan-toast | Activate dan Deactivate Single: Konfirmasi Sukses, Loading, dan Toast | FE+BE | 20 | 362, 374 |
| TC-FA-TDC-E2E-242-klik-ganda-cepat-pada-konfirmasi-deactivate-dan-delete-bulk | Klik Ganda Cepat pada Konfirmasi Deactivate dan Delete Bulk | FE+BE | 22 | 488, 487 |
| TC-FA-TDC-E2E-243-dialog-bulk-cancel-activate-dan-delete-jamak-mempertahankan-seleksi | Dialog Bulk Cancel Activate dan Delete Jamak Mempertahankan Seleksi | FE+BE | 28 | 435, 436 |
| TC-FA-TDC-E2E-244-dialog-bulk-tombol-ok-delete-jamak-blok-dan-esc-deactivate-jamak | Dialog Bulk Tombol OK Delete Jamak Blok dan Esc Deactivate Jamak | FE+BE | 25 | 439, 440 |
| TC-FA-TDC-E2E-245-konflik-d-09-d-08-apply-class-dihapus-dan-asset-class-berubah-antara-save-dan-apply | Konflik D-09 dan D-08: Apply pada Class yang Dihapus dan Asset Class Berubah Antara Save dan Apply | FE+BE | 30 | 282, 291 |
| TC-FA-TDC-E2E-246-konflik-restore-default-classes-log-changelog-system-log-dan-activity-log | Konflik Restore Default Classes: Log Create per Class Dibuat dan Edit per Class Diaktifkan Kembali di Tiga Surface Log | FE+BE | 20 | 674 |
| TC-FA-TDC-E2E-247-search-kolom-non-searchable-effective-from-last-updated-dan-active | Search: Kolom Non-Searchable Effective From, Last Updated, dan Active | FE+BE | 22 | 496, 497 |
| TC-FA-TDC-E2E-248-filter-baris-bernilai-kosong-dan-independen-dari-visibilitas-kolom | Filter: Baris Bernilai Kosong dan Independen dari Visibilitas Kolom | FE+BE | 24 | 526, 527 |
| TC-FA-TDC-E2E-249-popup-used-by-setup-column-geser-urutan-kolom | Popup Used By Setup Column: Geser Urutan Kolom | FE+BE | 16 | 598 |
| TC-FA-TDC-E2E-250-popup-used-by-setup-column-pin-dan-unpin-kolom | Popup Used By Setup Column: Pin dan Unpin Kolom | FE+BE | 18 | 599 |
| TC-FA-TDC-E2E-251-popup-changelog-setup-column-ceklis-dan-unceklis-tujuh-kolom-default | Popup Changelog Setup Column: Ceklis dan Unceklis Tujuh Kolom Default | FE+BE | 16 | 642 |
| TC-FA-TDC-E2E-252-popup-changelog-setup-column-pin-dan-unpin-tujuh-kolom-default | Popup Changelog Setup Column: Pin dan Unpin Tujuh Kolom Default | FE+BE | 18 | 644 |
| TC-FA-TDC-E2E-253-absence-log-submit-save-ditolak-validasi-dan-d-08 | Absence Log: Submit dan Save yang Ditolak (Validasi Create dan Edit, Dialog D-08) Tidak Menulis Entri | FE+BE | 54 | 695, 696, 962 |
| TC-FA-TDC-E2E-255-asset-class-dropdown-class-baru-nama-diubah-restore-dan-disabled-tanpa-class-active | Asset Class: Dropdown Tax Depreciation Class Mengikuti Class Baru, Nama Diubah, Restore, dan Disabled Tanpa Class Active | FE+BE | 47 | 729, 730, 731, 732 |
| TC-FA-TDC-E2E-256-versi-baru-current-scheduled-dan-allowed-methods-dipersempit-pada-asset-class-pemakai | Asset Class Pemakai: Versi Current dan Scheduled Memengaruhi Useful Life dan Rate, serta Allowed Methods Dipersempit | FE+BE | 37 | 788, 789, 790 |
| TC-FA-TDC-E2E-257-bypass-ui-edit-building-declining-balance-dan-land-terisi-ditolak-server | Bypass UI Edit: Building dengan Declining Balance dan Land Terisi Ditolak Server | FE+BE | 16 | 244, 245 |
| TC-FA-TDC-E2E-258-request-langsung-pemanggil-terotorisasi-tercatat-di-tiga-surface-edit-cancel-version-dan-restore | Request Langsung Pemanggil Terotorisasi Tercatat di Tiga Surface: Edit, Cancel Scheduled Version, dan Restore default classes | FE+BE | 44 | 910, 911, 912 |
| TC-FA-TDC-E2E-259-pratinjau-angka-penyusutan-fiskal-dan-nilai-sisa-buku-d-09-menunggu-mesin-kalkulasi | Pratinjau Dampak D-09 Menampilkan Angka Penyusutan Fiskal dan Nilai Sisa Buku Sebelum → Sesudah (Menunggu Mesin Kalkulasi, OI-03 b) | FE+BE | 14 | 253 |
| TC-FA-TDC-E2E-260-absence-log-request-langsung-role-matrix-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Activate dan Deactivate yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 12 | 791, 792, 793, 794, 795, 796, 797, 798 |
| TC-FA-TDC-E2E-261-absence-log-request-langsung-guard-data-dan-effective-from-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Guard Data (Used By, Last Posted Tax Year, Asset Type, Class Code) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 30 | 834, 835, 836, 839, 840 |
| TC-FA-TDC-E2E-262-absence-log-request-langsung-create-tidak-valid-state-tenant-dan-periode-ditolak-tidak-menulis-entri | Absence Log: Request Langsung pada Plan Starter, Entitas Suspended, dan Tahun Pajak Tertutup yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 26 | 831, 888, 847 |
| TC-FA-TDC-E2E-263-absence-log-bypass-ui-create-dan-edit-ditolak-server-tidak-menulis-entri | Absence Log: Create Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 34 | 160, 161 |
| TC-FA-TDC-E2E-264-expired-edit-lewat-form-ditolak-toast-baku | Entitas Expired: Edit lewat Form Ditolak dengan Toast Baku | FE+BE | 10 | 102 |
| TC-FA-TDC-E2E-265-absence-log-request-langsung-role-matrix-delete-dan-bulk-delete-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Delete dan Bulk Delete yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 12 | 799, 800, 801, 802, 811, 812, 813, 814 |
| TC-FA-TDC-E2E-266-absence-log-request-langsung-role-matrix-bulk-activate-dan-bulk-deactivate-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Bulk Activate dan Bulk Deactivate yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 12 | 803, 804, 805, 806, 807, 808, 809, 810 |
| TC-FA-TDC-E2E-267-absence-log-request-langsung-role-matrix-create-dan-edit-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Create dan Edit yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 12 | 815, 816, 817, 818, 819, 820, 821, 822 |
| TC-FA-TDC-E2E-268-absence-log-request-langsung-role-matrix-cancel-scheduled-version-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Cancel Scheduled Version yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 6 | 823, 824, 825, 826 |
| TC-FA-TDC-E2E-269-absence-log-request-langsung-role-matrix-restore-default-classes-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Role Matrix Restore Default Classes pada Tabel Kosong yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 8 | 827, 828, 829, 830 |
| TC-FA-TDC-E2E-270-absence-log-request-langsung-effective-from-dan-allowed-methods-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Allowed Methods dan Effective From Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 38 | 841, 845, 846, 927, 964 |
| TC-FA-TDC-E2E-271-absence-log-request-langsung-cancel-version-dan-effective-from-sebelum-tahun-pajak-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Cancel Version dan Effective From Sebelum Tahun Pajak Berjalan yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 22 | 848, 849, 928 |
| TC-FA-TDC-E2E-272-absence-log-request-langsung-create-payload-tidak-valid-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Create dengan Payload Tidak Valid yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 6 | 851, 852, 853, 854, 855, 856, 857, 858 |
| TC-FA-TDC-E2E-273-absence-log-request-langsung-create-melanggar-aturan-data-ditolak-tidak-menulis-entri | Absence Log: Request Langsung Create yang Melanggar Aturan Data (Land, Building, Class Code Kembar) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 18 | 842, 843, 844 |
| TC-FA-TDC-E2E-274-absence-log-bypass-ui-edit-ditolak-server-tidak-menulis-entri | Absence Log: Edit Hasil Bypass UI (Building dengan Declining Balance dan Land Terisi) yang Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 20 | 244, 245 |
| TC-FA-TDC-E2E-275-d-08-versi-scheduled-asset-class-blok-save-dan-daftar-satu-kali-per-asset-class | Dialog D-08 karena Versi Scheduled Asset Class: Blok Save dan Daftar Satu Kali per Asset Class | FE+BE | 27 | 962, 965 |
| TC-FA-TDC-E2E-276-konflik-d-09-d-08-versi-scheduled-asset-class-terbentuk-antara-save-dan-apply | Konflik D-09 dan D-08: Versi Scheduled Asset Class Terbentuk Antara Save dan Apply | FE+BE | 18 | 963 |
| TC-FA-TDC-E2E-277-picker-tax-method-asset-class-disabled-dan-tooltip-karena-versi-scheduled | Picker Tax Method Asset Class: Metode yang Dibuang Versi Scheduled Disabled dengan Tooltip | FE+BE | 23 | 966 |
| TC-FA-TDC-E2E-278-picker-tax-method-asset-class-pulih-setelah-cancel-scheduled-version | Picker Tax Method Asset Class: Metode yang Semula Disabled Dapat Dipilih Lagi Setelah Cancel Scheduled Version | FE+BE | 26 | 967 |
| TC-FA-TDC-E2E-279-screening-field-declining-balance-rate-dan-end-of-life-treatment-di-create-dan-nilai-seed-di-edit | Screening Field End-of-Life Treatment di Drawer Create (Wajib, Tiga Opsi, Tidak Dapat Dikosongkan, Reset) dan Nilai Declining Balance Rate serta End-of-Life Treatment Tiap Class Seed | FE+BE | 60 | 935, 943, 952 |
| TC-FA-TDC-E2E-280-create-helper-equivalent-declining-balance-rate-faktor-pembulatan-hitung-ulang-dan-tidak-valid | Drawer Create: Helper Equivalent Declining Balance Rate (Faktor, Pembulatan Half-Up, Hitung Ulang Seketika, dan Keadaan Tidak Valid) | FE+BE | 56 | 939, 940, 941, 942 |
| TC-FA-TDC-E2E-281-validasi-declining-balance-rate-kosong-dan-di-luar-rentang-create-dan-edit-ditolak | Validasi Declining Balance Rate: Create Kosong serta Edit Kosong dan di Luar Rentang Ditolak Tanpa Entri Log Baru | FE+BE | 45 | 936, 950 |
| TC-FA-TDC-E2E-282-create-sukses-declining-balance-rate-batas-0-01-dan-100-serta-tarif-50-tidak-diturunkan-dari-useful-life | Create Sukses: Declining Balance Rate Batas Valid 0.01 dan 100 serta Tarif 50 pada Useful Life 10 Tersimpan Apa Adanya | FE+BE | 42 | 937, 938 |
| TC-FA-TDC-E2E-283-create-sukses-straight-line-saja-tanpa-rate-dan-end-of-life-treatment-keep-depreciating-dan-switch-to-straight-line | Create Sukses: Class Straight Line Saja Tidak Menyimpan Declining Balance Rate dan End-of-Life Treatment serta Pilihan Keep depreciating dan Switch to straight-line Tersimpan | FE+BE | 36 | 944, 945 |
| TC-FA-TDC-E2E-284-edit-versi-baru-declining-balance-rate-end-of-life-treatment-dan-useful-life-lewat-d-09 | Edit: Perubahan Declining Balance Rate, End-of-Life Treatment, atau Useful Life Membentuk Versi Baru Lewat Dialog D-09 dan Rate Tersimpan Tidak Dihitung Ulang | FE+BE | 44 | 946, 947, 949 |
| TC-FA-TDC-E2E-285-edit-allowed-methods-menambah-dan-melepas-declining-balance-versi-baru-dan-nilai-awal-rate | Edit Allowed Methods: Menambah Declining Balance pada Class Straight Line Saja dan Melepas Declining Balance Membentuk Versi Baru | FE+BE | 39 | 948, 951 |
| TC-FA-TDC-E2E-286-log-l-03-declining-balance-rate-dan-end-of-life-treatment-serta-log-class-hasil-request-langsung | Pencatatan Log: Perubahan Declining Balance Rate dan End-of-Life Treatment (L-03) serta Log Class Hasil Request Langsung di Changelog, System Log, dan Activity Log | FE+BE | 93 | 953, 954, 958, 960 |
| TC-FA-TDC-E2E-287-request-langsung-declining-balance-rate-end-of-life-treatment-dan-land-ditolak | Request Langsung: Declining Balance Rate Kosong atau di Luar Rentang, End-of-Life Treatment Kosong atau di Luar Opsi, serta Land dengan Rate Terisi Ditolak | FE+BE | 26 | 955, 956, 957, 959 |
| TC-FA-TDC-E2E-288-absence-log-request-langsung-declining-balance-rate-end-of-life-treatment-dan-land-ditolak-tidak-menulis-entri | Absence Log: Request Langsung dengan Declining Balance Rate, End-of-Life Treatment, atau Land yang Tidak Valid dan Ditolak Tidak Menulis Entri di Changelog, System Log, dan Activity Log | FE+BE | 30 | 955, 956, 957, 959 |
| TC-FA-TDC-E2E-289-perlakuan-akhir-masa-manfaat-end-of-life-treatment-menunggu-mesin-penyusutan | Perlakuan Akhir Masa Manfaat Dieksekusi Mesin Penyusutan Menurut End-of-Life Treatment Class (Menunggu Mesin Penyusutan, OI-03 f) | FE+BE | 7 | 961 |

## Pembagian TC lintas spec

Nomor cadangan terpakai (30): 227-229, 231-253, 255-258. Nomor cadangan tidak terpakai: 230, 254. Nomor tambahan 259-274: 259 (TC-253 menunggu OI-03 b) dan 260-263 (spec absence kelas g) dari keputusan user 2026-11-04; 264 (TC-102, edit lewat form ditolak pada entitas Expired) dari fix pass 1; 265-274 (spec absence kelas g tambahan, hasil pemecahan spec absence supaya baseline per TC) dari fix pass 2. Tabel di atas dan "Lapisan per TC" mengikuti `sourceTc` spec (sumber kebenaran), bukan rencana. Perubahan terhadap rencana yang dicatat penulis slice (TC pindah dari spec rencana ke nomor cadangan supaya spec tidak lebih panjang, atau slug/`sourceTc` berubah):

- Slice 1: TC 918, 920 ke 227; TC 922, 923 ke 228; 010 memuat 916, 917; 011 memuat 293 (slug 010 dan 011 berubah).
- Slice 2: TC 51 ke 229 (butuh tabel tanpa class).
- Slice 3: TC 101 ke 231; TC 130, 133 ke 232 (slug 038 berubah).
- Slice 4: TC 110 ke 233; TC 113 ke 234 (slug 042 dan 043 berubah).
- Slice 5: TC 32, 179 ke 235; TC 191, 192 ke 236.
- Slice 6: TC 284, 285 ke 237; TC 258 ke 238.
- Slice 7: TC 324 ke 239 (slug 088 berubah); TC 358, 359 ke 240 (slug 095 berubah).
- Slice 8: TC 362, 374 ke 241; TC 488, 487 ke 242 (slug 097, 098, 104 berubah).
- Slice 9: TC 435, 436 ke 243; TC 439, 440 ke 244 (slug 114 dan 115 berubah).
- Slice 10: TC 282, 291 ke 245; TC 674 ke 246 (slug 127 dan 138 berubah).
- Slice 11: TC 496, 497 ke 247; TC 526, 527 ke 248 (slug 144 dan 150 berubah).
- Slice 12: TC 598 ke 249; TC 599 ke 250 (slug 167 dan 168 berubah; TC 597, 600, 601, 602 dipetakan ulang).
- Slice 13: TC 642 ke 251; TC 644 ke 252; 179 memuat 643; 180 memuat 645, 646, 647; 178 memuat 640, 641 (slug 179 berubah).
- Slice 14: TC 695, 696 ke 253 (slug 197 berubah).
- Slice 15: TC 729-732 ke 255; TC 788-790 ke 256 (slug 199 dan 202 berubah).
- Slice 16: TC 244, 245 ke 257; TC 910, 911, 912 ke 258.
- TC-935 s/d TC-961 (27 TC, tidak ada TC hanya-BE) dipetakan ke 11 spec baru 279-289: 279 (935, 943, 952), 280 (939-942), 281 (936, 950), 282 (937, 938), 283 (944, 945), 284 (946, 947, 949), 285 (948, 951), 286 (953, 954, 958, 960), 287 (955-957, 959; request langsung kelas a), 288 (955-957, 959; spec absence kelas g), 289 (961, `[DEFERRED]` OI-03 f, `coverage.web: unsupported`). TC-955, 956, 957, dan 959 muncul di `sourceTc` spec 287 (primer) dan 288 (absence, S-05; C2 `[REVIEW]`); TC-958 dan TC-960 (request langsung dengan Expected pencatatan log) berada di spec 286 (P-5 butir b). Kode class `DBE-*`, `R-API*`, dan `LAND3` memakai literal TC (Class Code maksimal 15 karakter, seeding idempotent, kode berbeda antar spec).
- TC-253 (`[DEFERRED]`, OI-03 b) berada di spec 259 dengan `coverage.web: unsupported` (Q-17); spec 070 memuat TC 248, 249, 250.
- Spec absence kelas g untuk klausa "tidak ada entri log baru" atas request langsung kelas a yang ditolak (Q-19). TC tetap primer di spec asalnya dan muncul juga di `sourceTc` spec absence (S-05; `check-suite` C2 `[REVIEW]`, satu per pasangan spec asal dan spec absence). Ada 15 spec absence (260-263, 265-274, dan 288) yang mencakup 74 TC kelas a (ditambah 955-957 dan 959 di spec 288): 160-161, 244-245, 791-831, 834-836, 839-849, 851-858, 888, 927-928. Baseline log dibaca lewat kemampuan baca log fixture BE (disediakan tim FE/BE) pada tiga surface log (Changelog, System Log akun pemanggil, Activity Log), baseline per TC (satu baseline sebelum aksi tiap TC, tidak dibagi antar TC), dengan anchor positif penolakan server. Deviasi sebelumnya "baseline per blok" beserta usulan pengecualian konvensinya DIBATALKAN pada fix pass 2:
  - 260 (8 TC, 12 langkah): 791-798; spec asal 207, 208.
  - 261 (5 TC, 30 langkah): 834-836, 839-840; spec asal 219, 220.
  - 262 (3 TC, 26 langkah): 831, 847, 888; spec asal 217, 221.
  - 263 (2 TC, 34 langkah): 160-161; spec asal 224.
  - 265 (8 TC, 12 langkah): 799-802, 811-814; spec asal 209, 212.
  - 266 (8 TC, 12 langkah): 803-810; spec asal 210, 211.
  - 267 (8 TC, 12 langkah): 815-822; spec asal 213, 214.
  - 268 (4 TC, 6 langkah): 823-826; spec asal 215.
  - 269 (4 TC, 8 langkah): 827-830; spec asal 216.
  - 270 (4 TC, 30 langkah): 841, 845-846, 927; spec asal 220, 221, 223.
  - 271 (3 TC, 22 langkah): 848-849, 928; spec asal 221, 223.
  - 272 (8 TC, 6 langkah): 851-858; spec asal 222, 223.
  - 273 (3 TC, 18 langkah): 842-844; spec asal 220, 221.
  - 274 (2 TC, 20 langkah): 244-245; spec asal 257.
  - 288 (4 TC, 30 langkah): 955-957, 959; spec asal 287.
  - Klausa log kelas a yang tidak dicakup: tidak ada dari daftar Q-19 (TC 926 tidak memuat klausa log). TC non-kelas-a dengan klausa "tidak ada entri log baru" (mis. TC 102, 210, 291, 364-479, 758, 777, 861, 863, 874-887) tetap diasersi di spec asalnya masing-masing.
- Fix pass 1 (2026-11-04):
  - TC-102 dipindah dari 034 ke spec baru 264 (`TC-FA-TDC-E2E-264-expired-edit-lewat-form-ditolak-toast-baku`); 034 kini memuat 880, 881, 882, 883 (37 langkah).
  - TC-46 dipindah dari 014 ke 013; 013 memuat 41, 42, 43, 46 (35 langkah nominal), 014 memuat 44, 45 (13 langkah).
  - Rename folder dan id: 034 menjadi `...-034-expired-aksi-activate-deactivate-delete-dan-bulk-delete-ditolak-toast-baku`; 013 menjadi `...-013-role-matrix-baca-read-only-read-capability-selalu-disertai-read-dan-data-seluruh-client`; 014 menjadi `...-014-role-matrix-negatif-tanpa-capability-menu-accounting-dan-url-langsung`.
- Fix pass 2 (2026-11-04): spec absence 260-263 ditulis ulang dengan satu baseline per TC dan 10 spec absence baru 265-274 menampung TC kelas a yang semula berbagi baseline; alokasi TC ada di daftar absence di atas (sumber: `sourceTc` tiap spec). Jumlah langkah banyak spec berubah; angka di tabel diambil dari `## Test Steps` spec.
- Urutan TC dalam spec diubah di banyak spec (aksi yang menghapus atau mengubah state ditaruh terakhir); alasan di Notes tiap spec.

## Spec yang melewati ~35 langkah

Jumlah langkah dihitung dari baris bernomor pada `## Test Steps` (nominal; perulangan idiom 8b.7 tidak diekspansi). 88 dari 287 spec melewati ~35 langkah, terutama karena S-01 (satu `Verifikasi` per klausa Expected) membuat langkah jauh di atas perkiraan Est rencana, sedangkan nomor cadangan tiap slice sudah habis. Alasan tertulis di Notes tiap spec; ringkasannya:

| Spec | Langkah | Alasan penulis |
|---|:---:|---|
| 286 | 93 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 198 | 86 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 190 | 76 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 187 | 75 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 156 | 73 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 204 | 68 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 189 | 61 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 279 | 60 | satu topik layar field Declining Balance Rate dan End-of-Life Treatment tanpa membuat atau mengubah data; blok per class seed berpola sama |
| 205 | 59 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 155 | 57 | perulangan per kolom/field (8b.7), satu topik |
| 280 | 56 | satu form Create dipakai berulang tanpa Submit (halaman yang sama dipakai berulang); satu topik helper dan blok berdiri sendiri |
| 188 | 55 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 253 | 54 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 135 | 51 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 146 | 51 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 108 | 50 | kelas b (kegagalan dipaksa): satu klausa per Verifikasi, blok berdiri sendiri |
| 096 | 49 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 196 | 49 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 122 | 47 | alasan tertulis di Notes spec |
| 158 | 47 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 255 | 47 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 019 | 46 | Role Matrix positif per role, blok berdiri sendiri |
| 035 | 46 | kelas h (write-lockdown): asersi penolakan sama, blok berdiri sendiri |
| 036 | 46 | kelas h (write-lockdown): asersi penolakan sama, blok berdiri sendiri |
| 120 | 46 | alasan tertulis di Notes spec |
| 132 | 45 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 136 | 45 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 201 | 45 | perulangan per kolom/field (8b.7), satu topik |
| 281 | 45 | satu topik validasi ditolak dan blok berdiri sendiri; blok catat dan baca jumlah entri log tidak dihitung (prinsip 13) |
| 151 | 44 | perulangan per kolom/field (8b.7), satu topik |
| 191 | 44 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 258 | 44 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 284 | 44 | satu topik Edit versi baru lewat D-09 dan blok berdiri sendiri; langkah berulang berupa navigasi dan baca ulang per class |
| 057 | 43 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 106 | 43 | kelas b (kegagalan dipaksa): satu klausa per Verifikasi, blok berdiri sendiri |
| 141 | 43 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 024 | 42 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 061 | 42 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 133 | 42 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 152 | 42 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 282 | 42 | satu topik Create sukses dan blok berdiri sendiri; langkah berulang berupa isi form dan baca ulang per class |
| 016 | 41 | Role Matrix positif per role, blok berdiri sendiri |
| 058 | 41 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 060 | 41 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 078 | 41 | alasan tertulis di Notes spec |
| 203 | 41 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 004 | 40 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 077 | 40 | alasan tertulis di Notes spec |
| 105 | 40 | kelas b (kegagalan dipaksa): satu klausa per Verifikasi, blok berdiri sendiri |
| 123 | 40 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 148 | 40 | perulangan per kolom/field (8b.7), satu topik |
| 149 | 40 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 167 | 40 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 176 | 40 | perulangan per kolom/field (8b.7), satu topik |
| 177 | 40 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 186 | 40 | kelas mobile: satu layar, blok berdiri sendiri |
| 079 | 39 | alasan tertulis di Notes spec |
| 138 | 39 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 143 | 39 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 157 | 39 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 180 | 39 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 184 | 39 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 199 | 39 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 285 | 39 | satu topik Edit Allowed Methods dan blok berdiri sendiri; langkah berulang berupa navigasi dan baca ulang per class |
| 025 | 38 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 062 | 38 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 107 | 38 | kelas b (kegagalan dipaksa): satu klausa per Verifikasi, blok berdiri sendiri |
| 110 | 38 | alasan tertulis di Notes spec |
| 129 | 38 | kelas c (dua sesi): blok berdiri sendiri dengan seed ulang |
| 140 | 38 | alasan tertulis di Notes spec |
| 147 | 38 | satu topik; satu Verifikasi per klausa (S-01); blok berdiri sendiri |
| 166 | 38 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 224 | 38 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 270 | 38 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 202 | 37 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 034 | 37 | kelas h (write-lockdown): asersi penolakan sama, blok berdiri sendiri |
| 089 | 37 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 101 | 37 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 194 | 37 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 206 | 37 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 256 | 37 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 067 | 36 | alasan tertulis di Notes spec |
| 119 | 36 | alasan tertulis di Notes spec |
| 121 | 36 | alasan tertulis di Notes spec |
| 159 | 36 | satu topik dan blok berdiri sendiri; langkah berulang berupa navigasi/seeding |
| 197 | 36 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 218 | 36 | blok baca-log berpola pada tiga surface log; satu topik pencatatan log |
| 283 | 36 | satu topik Create sukses dan blok berdiri sendiri; langkah berulang berupa isi form dan baca ulang per class |

Beberapa spec memakai perulangan 8b.7 yang bila diekspansi jauh lebih panjang (mis. 251: 100, 179: 93, 252: 114, 176: 69, 154: sekitar 270 langkah). Saran penulis bila pemilik ingin spec <= ~45 langkah: tambah nomor cadangan; kandidat pecahan: 204 (924, 925 | 753, 754, 755), 205 (785, 770 | 777, 778 | 784, 786), 201 (740, 744, 743 | 741, 742), 108 (484 | 485, 486, 901), 153-156 (Setup Column tabel utama). Angka perulangan dan kandidat pecahan di atas adalah catatan penulis sebelum fix pass 1 dan 2 dan tidak dihitung ulang (langkah nominal sekarang: 251: 16, 179: 15, 252: 18, 176: 40, 154: 27, 204: 68, 205: 59, 201: 45, 108: 50). Keputusan: Q-20 (pecah 034 saja, sisanya diterima).

## Kebutuhan lingkungan (tim FE/BE)

Kebutuhan data, akun, env var password, fixture BE, kendali jam dan modul pemilik/konsumen tertulis di `## Prerequisites` tiap spec dan `suite.md`. Ringkasan hasil skrip atas seluruh suite:

- Env var password yang dipakai spec (jumlah spec pemakai di dalam kurung):
  - `FA_TC_PASSWORD` (258)
  - `FA_DELETEONLY_PASSWORD` (22)
  - `FA_RO_PASSWORD` (23)
  - `FA_CREATEONLY_PASSWORD` (21)
  - `FA_READ_PASSWORD` (22)
  - `FA_TC_B_PASSWORD` (17)
  - `FA_UPDATEONLY_PASSWORD` (15)
  - `FA_SITI_PASSWORD` (2)
  - `FA_TCNEWACC_PASSWORD` (2)
  - `FA_BUDI_PASSWORD` (1)
  - `FA_CREUPD_PASSWORD` (1)
  - `FA_DU_PASSWORD` (1)
  - `FA_GM_PASSWORD` (1)
  - `FA_NOCAP_PASSWORD` (1)
  - `FA_READ_HGB_PASSWORD` (1)
  - `FA_TC_CLIENTB_PASSWORD` (1)
  - `FA_UPDDEL_PASSWORD` (1)
- Kunci fixture di `fixtures/fixedAssetTaxDepreciationClass.json` (belum ada; jumlah spec pemakai di dalam kurung):
  - `Fixture.fixedAssetTaxDepreciationClass.exampleData` (50)
  - `Fixture.fixedAssetTaxDepreciationClass.seedClasses` (26)
  - `Fixture.fixedAssetTaxDepreciationClass.regulationReference` (21)
  - `Fixture.fixedAssetTaxDepreciationClass.exampleDataChangelog` (11)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset110` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset111` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset112` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset113` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset114` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset115` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset116` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset117` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset118` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset119` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset120` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset121` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset122` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset243` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.dataset244` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.exampleDataClasses` (1)
  - `Fixture.fixedAssetTaxDepreciationClass.tabUrl` (1)
- Kunci fixture lain yang hanya muncul sebagai nama bebas di prosa Prerequisites (slice 15 dan 16: `assetClassLaptop`, `assetClassMesin`, `assetClassBaru`, `approvalsPending`, `changelogStatusNb4`, `generalSettingsFormat`, `nbOld`, `nbOld2`, `nb3`, `nb4`, `nb2`, `nbKhs`, `nb1`, `bldNp`, `nb9`, `land2`, `bldX`, `seedTujuh`, `tabelKosong`, `assetClassPemakai`, `periode2025`, `periode2026`, `khsJ4a`, `khsJ2028`; spec 260-263 memakai nama yang sama dengan spec asal) belum seragam dengan kunci di atas; lihat Q-16.
- Kemampuan BE/FE yang dibutuhkan dan belum ada: seed dan pemulihan class lewat API (7 seed, 9 Example Data, tabel 21/25/26/999 class, tabel kosong), sesi API aktor, kendali jam server dan browser, penahanan dan pemicu job J-01/J-02/J-03, fault injection (`Spectra.intercept()`), pembacaan jumlah entri Changelog/System Log/Activity Log, perubahan plan dan status company (Starter, Suspended, Expired), company baru sebelum aktivasi modul akuntansi, penimpaan riwayat Changelog 16 entri Example Data, pembukaan berkas unduhan CSV/XLSX, flag Guided Tooltip, perangkat atau emulator Android. Spec 185 dan 186 memakai `coverage.mobile` saja.

## Temuan sumber TC (konsolidasi catatan penulis)

Temuan per TC ada di bagian "Temuan untuk QA" pada `## Notes` tiap spec dan di `work-items/fa-tax-depreciation-class/slice-<n>-writer-notes.md`. Dikelompokkan menurut tema:

- Akun aktor: Pre-setup TC tidak punya nomor Pre-setup #N, email, atau company; kolom ACC hanya memuat nama role (semua spec). Role tanpa nama ("role lain tanpa capability", TC 44, 45) dan ACC kosong (TC 43-70, 98, 100, 586 dan lainnya) diambil dari Precondition butir a.
- Post Condition dan klausa tanpa langkah observasi: entri log (L-01..L-11), "tidak ada entri log baru", "tidak ada versi baru", "tidak ada yang tersimpan" tanpa surface dan tanpa langkah baca (mis. TC 71-73, 82-84, 88-90, 189-196, 220-243, 248-286, 362, 374, 384, 394-398, 433-448, 460-463, 840-858). Spec memakai baseline selisih entri lewat kemampuan baca log yang disediakan tim BE/FE, atau tidak mengasersi klausa tanpa langkah.
- Langkah atau nilai hilang/ambigu: nilai field "form valid" (TC 110-125, 130, 133, 173), `[N]` tanpa nilai (TC 413, 907), tanggal tanpa nilai persis (TC 29, 345-347, 516, 841), tombol penutup dialog/popup tidak disebut (TC 290-292, 790, 647, 920), label `Confirm` di TC versus label PRD (TC 726-732, 786), aksi "Kosongkan Search/Filter" tanpa cara (TC 489-492, 583).
- Langkah yang tidak dapat dijalankan atau saling bertentangan: TC 50 (klik `+ Class` saat tombol Hidden), TC 552 (kolom Used By disembunyikan lalu diklik), TC 541 versus guard TC 549, TC 385 versus Example Data/TC 379 (BLD-P Inactive vs Active), TC 588 (BLD-NP 12 pemakai versus Used By 0), TC 360 (label Manual Only Suspended vs Precondition Expired), TC 162 versus 103/165/166 (rate Land `Disabled` vs `tidak tampil`), TC 69 (Restore default classes pada tabel berisi class), TC 25 versus 26, TC 591/593 duplikat, TC 453/454 berlabel sama.
- Data uji tidak lengkap atau tidak ada di Example Data: NB-OLD, NB-OLD2, NB-3, NB-SL, KHS-* bukan seed bawaan (TC 131, 483-486, 710-712, 759); isi tabel berbeda antar TC (7 seed vs 9 Example Data vs 21/25/26 class); TC 523 butuh enam user Modified By berbeda; TC 510 butuh tabel hanya NB-1..4 Active; TC 134 butuh 993 class tambahan.
- Aktor dan mekanisme tidak disebut: Rina Puspita/Pratama/Putri/P, Siti Rahmawati, Budi Santoso, Client B tanpa email; "Manual Only: dua sesi paralel" pada TC yang langkahnya satu sesi (TC 307); mekanisme "kirim ulang request" (TC 160, 161, 244, 245), data basi versus request langsung (TC 262), fault injection dan reset company (TC 339-342), "server menolak" tanpa status HTTP (TC 834-858, 860-863).
- Interpretasi UI yang ambigu: "bergaya danger" tanpa atribut visual (TC 426, 427, 430, 431), severity badge (TC 604), tooltip hover tanpa langkah hover (TC 489), `-` berkas versus `—` UI (TC 571), header `Column Visibility (⋯)` versus `Actions` (TC 579, 595-601, 613, 640-647), penomoran Expected bergeser (TC 635), seleksi bertahan setelah Esc (TC 917), keadaan Drawer setelah penolakan (TC 884, 885, 102, 688, 695, 696), reset seleksi setelah bulk.
- Jumlah absolut pada audit trail permanen (S-12): 14 baris seed (TC 673), 16 entri Popup Changelog (TC 613-647), 1000 class (TC 117, 132, 329-331), hanya deterministik pada company yang riwayat lognya direset; Lampiran A tidak punya pengecualian modul ini.
- Label Manual Only tidak dijadikan alasan mengeluarkan TC (konvensi bagian 2); TC Android semuanya bertanda Manual Only namun spec tetap `coverage.mobile: automated` (spec 185, 186).

## Konsistensi nama (hasil grep read-only)

Skrip grep atas seluruh spec tidak menemukan nama env yang bertabrakan makna, tetapi: (1) hanya `FA_TC_PASSWORD` dipakai konsisten di 258 spec; (2) 16 env lain bersifat usulan penulis dan belum terdaftar, dengan penamaan pelaku kedua yang tidak seragam (`FA_TC_B_PASSWORD`, `FA_TC_CLIENTB_PASSWORD`, `FA_TCNEWACC_PASSWORD`, `FA_SITI_PASSWORD`, `FA_BUDI_PASSWORD`); (3) kunci fixture `dataset110`..`dataset122`, `dataset243`, `dataset244` per spec (slice 9) tidak sejalan dengan kunci bersama `exampleData`, `seedClasses`, `regulationReference`; (4) variasi nama `exampleData`, `exampleDataClasses`, `exampleDataChangelog`, `exampleDataPlusNb3`, `exampleDataPlus17`, `exampleDataBldNpVersions`, `exampleDataBldNp12Versions`, `exampleDataWithSeedBldP`; (5) kunci akun per Pre-setup tidak ada karena TC tidak memuat Pre-setup #N.

## Pertanyaan terbuka

- Q-01 [DILEWATI 2026-11-04: dependensi eksekusi, tidak diminta ke tim] Akun aktor: ACC indeks hanya memuat nama role tanpa nomor Pre-setup #N, email, atau company. Perlu daftar akun per role dan company uji dari QA/FE; nama env password usulan tertulis di Prerequisites tiap spec.
- Q-02 [DILEWATI 2026-11-04: dependensi eksekusi, tidak diminta ke tim] Fixture `fixtures/fixedAssetTaxDepreciationClass.json` perlu disediakan tim FE; TC tidak memiliki tabel Data Uji Pre-setup/Dinamis terpisah, data ada pada kolom Precondition dan Data Uji tiap TC.
- Q-03 [DITERIMA 2026-11-04: keputusan desain final] TC ber-ACC kosong (TC 43-70, 98, 100, 586 dan lainnya): role diuji dibaca dari Precondition butir a.
- Q-04 [DITERIMA 2026-11-04: mengikuti Open Item OI-03/OI-06] TC-252 (pratinjau angka penyusutan `-` selama mesin kalkulasi belum tersedia, OI-03 b), TC-263 dan 758 (OI-03 e), TC-914 (OI-06 k): ditulis sesuai Expected saat ini. TC-253 `[DEFERRED]` ada di spec 259 dengan `coverage.web: unsupported` (Q-17).
- Q-05 [DITERIMA 2026-11-04: keputusan desain final] TC-102 (HINT g,h) ditempatkan di spec h (Expired), bukan spec absence kelas g; sejak fix pass 1 di spec 264 (dipecah dari 034, Q-20).
- Q-06 [DITERIMA 2026-11-04: keputusan desain final] Semua spec resilience (5xx, timeout, 429) bermode `FE+BE` dengan `Spectra.intercept()` karena asersi memuat state server; versi `mock` murni bukan bagian rencana.
- Q-07 [DITERIMA 2026-11-04: keputusan desain final] TC ber-ACC dua sesi (sekitar 40 TC) dikelompokkan sebagai kelas c; sesi API aktor dipakai bila hasil sesi kedua tidak diasersi, sesi UI kedua bila diasersi.
- Q-08 [DITERIMA 2026-11-04: keputusan desain final] Kelas e: Master Data Count Limit 1000 butuh 999 class; Selection Limit (TC 423, 424) di Admin Console > Plans & Licensing > Lifecycle Settings. QA dapat menurunkannya menjadi fungsional bila di bawah ambang kelas e.
- Q-09 [DITERIMA 2026-11-04: keputusan desain final] TC-94 (Read mengunduh CSV): hanya nama berkas dan unduhan; isi berkas diuji pada kelas f (TC 565-577).
- Q-10 [DILEWATI 2026-11-04: dependensi eksekusi, tidak diminta ke tim] TC-660 sampai 671 (Android native) membutuhkan perangkat/emulator dari tim FE; `coverage.mobile: automated`.
- Q-11 [DITERIMA 2026-11-04: keputusan desain final] Tabel 21, 25, dan 26 class di-seed lewat API; di bawah ambang kelas e.
- Q-12 [DITERIMA 2026-11-04: keputusan desain final] HINT lead (g untuk Cancel/Esc/backdrop, b untuk debounce 500 ms) tidak dipakai sebagai kelas.
- Q-13 [DITERIMA 2026-11-04: keputusan desain final] Perubahan Fiscal Year Start (TC 749-755, 924, 925) dilakukan di Settings > Accounting > Preferences (modul tetangga); langkah mengikuti TC tanpa mengarang endpoint.
- Q-14 [DIALIHKAN 2026-11-04: usulan diserahkan ke pemilik konvensi] Class Code maksimal 15 karakter (TC 136, 137): suffix `-{runId}-<NNN>` (S-12) tidak muat pada kode class seperti `KHS-D1`. Sebagian besar spec memakai kode literal TC dengan seed idempotent, cleanup oleh spec, dan suite serial; sebagian spec (mis. 011, 227, 095, 161) tetap menulis suffix yang mungkin melewati batas. Keputusan user 2026-11-04: butir Lampiran A diusulkan, konvensi tidak diubah. Teks usulan: `work-items/fa-tax-depreciation-class/proposal-lampiran-a-tdc.md` (status USULAN, belum menjadi butir Lampiran A). Kode `TDC-01`..`TDC-17` yang sama dipakai empat spec (146, 152, 157, 158).
- Q-15 [DILEWATI 2026-11-04: dependensi eksekusi, tidak diminta ke tim] Nama env baru belum terdaftar di `.env.example` dan `executionConfig.environmentVariables` (daftar di bagian Kebutuhan lingkungan, di luar `FA_TC_PASSWORD`).
- Q-16 [DILEWATI 2026-11-04: dependensi eksekusi, tidak diminta ke tim] Kunci fixture dan kemampuan BE disediakan tim FE/BE: nama kunci belum seragam antar slice (lihat Konsistensi nama); tim FE perlu menetapkan satu daftar kunci dan menyatukan `dataset<NNN>` dan nama bebas.
- Q-17 [SELESAI 2026-11-04] TC-253 `[DEFERRED]`: dipindah dari spec 070 ke spec 259 dengan `coverage.web: unsupported` sampai OI-03 (b) diputuskan; Notes spec 259 memuat apa yang diganti saat OI-03 diputuskan.
- Q-18 [DIALIHKAN 2026-11-04: ke audit-testcase (pemilik TC)] TC-258 tidak dapat dipenuhi pada data TC: Expected c menyebut baris pratinjau, tetapi Precondition d memakai class Used By 0 (TC-248: pratinjau tidak tampil). Spec 238 mengikuti data yang ada; QA perlu memperbaiki TC.
- Q-19 [SELESAI 2026-11-04] Klausa "tidak ada entri log baru" untuk request langsung kelas a yang ditolak diasersi di 14 spec absence (260-263 dan 265-274; 70 TC: 791-831, 834-836, 839-849, 851-858, 888, 927, 928, 160, 161, 244, 245), dengan aksi nyata, baseline per TC lewat kemampuan baca log fixture BE, dan anchor positif; Notes spec asal merujuk spec absence. Sisa kebutuhan: kemampuan baca log fixture BE dari tim FE/BE dan perubahan state tenant/periode yang tidak menulis ke tiga surface log (spec 262 dan 273). Deviasi "baseline per blok" dan usulan pengecualian konvensi dibatalkan pada fix pass 2.
- Q-20 [DIPUTUSKAN 2026-11-04: pecah 034, alasan jujur lainnya; sisanya diterima] Spec 034 dipecah (TC-102 ke spec 264) dan panjang spec dinilai ulang pada fix pass 2; spec lain yang melewati ~35 langkah (lihat daftar di atas) diterima dengan alasan tertulis di Notes tiap spec. Nomor baru berikutnya mulai 275.

## Fix pass 1

Setelah `e2e-audit` (2026-11-04) spec diperbaiki dalam satu fix pass: temuan, keputusan, dan hasil ada di `work-items/fa-tax-depreciation-class/report-e2e-audit.md`. Dampak pada halaman ini: spec baru 264 (TC-102 dipindah dari 034), TC-46 dipindah dari 014 ke 013, rename folder dan id 013, 014, 034, jumlah langkah banyak spec berubah, total 262 spec (261 + 264). Tabel spec, daftar spec > ~35 langkah, dan "Lapisan per TC" dibuat ulang dari frontmatter dan `## Test Steps` spec.

## Fix pass 2

Setelah audit ulang, spec diperbaiki dalam fix pass kedua: temuan, keputusan, dan hasil ada di `work-items/fa-tax-depreciation-class/report-e2e-audit-delta-1.md`. Dampak pada halaman ini: spec absence 260-263 ditulis ulang dengan satu baseline per TC, 10 spec absence baru 265-274, total 272 spec (262 + 10), banyak jumlah langkah berubah (79 spec melewati ~35 langkah). Tabel spec, daftar spec > ~35 langkah, dan "Lapisan per TC" dibuat ulang dari frontmatter dan `## Test Steps` spec.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-TDC-1 | TC-FA-TDC-E2E-001 | FE+BE |
| TC-FA-TDC-2 | TC-FA-TDC-E2E-001 | FE+BE |
| TC-FA-TDC-3 | TC-FA-TDC-E2E-001 | FE+BE |
| TC-FA-TDC-4 | TC-FA-TDC-E2E-001 | FE+BE |
| TC-FA-TDC-5 | TC-FA-TDC-E2E-002 | FE+BE |
| TC-FA-TDC-6 | TC-FA-TDC-E2E-002 | FE+BE |
| TC-FA-TDC-7 | TC-FA-TDC-E2E-002 | FE+BE |
| TC-FA-TDC-8 | TC-FA-TDC-E2E-087 | FE+BE |
| TC-FA-TDC-9 | TC-FA-TDC-E2E-003 | FE+BE |
| TC-FA-TDC-10 | TC-FA-TDC-E2E-003 | FE+BE |
| TC-FA-TDC-11 | TC-FA-TDC-E2E-003 | FE+BE |
| TC-FA-TDC-12 | TC-FA-TDC-E2E-003 | FE+BE |
| TC-FA-TDC-13 | TC-FA-TDC-E2E-004 | FE+BE |
| TC-FA-TDC-14 | TC-FA-TDC-E2E-151 | FE+BE |
| TC-FA-TDC-15 | TC-FA-TDC-E2E-008 | FE+BE |
| TC-FA-TDC-16 | TC-FA-TDC-E2E-005 | FE+BE |
| TC-FA-TDC-17 | TC-FA-TDC-E2E-005 | FE+BE |
| TC-FA-TDC-18 | TC-FA-TDC-E2E-005 | FE+BE |
| TC-FA-TDC-19 | TC-FA-TDC-E2E-005 | FE+BE |
| TC-FA-TDC-20 | TC-FA-TDC-E2E-005 | FE+BE |
| TC-FA-TDC-21 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-22 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-23 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-24 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-25 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-26 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-27 | TC-FA-TDC-E2E-006 | FE+BE |
| TC-FA-TDC-28 | TC-FA-TDC-E2E-007 | FE+BE |
| TC-FA-TDC-29 | TC-FA-TDC-E2E-007 | FE+BE |
| TC-FA-TDC-30 | TC-FA-TDC-E2E-007 | FE+BE |
| TC-FA-TDC-31 | TC-FA-TDC-E2E-007 | FE+BE |
| TC-FA-TDC-32 | TC-FA-TDC-E2E-235 | FE+BE |
| TC-FA-TDC-33 | TC-FA-TDC-E2E-007 | FE+BE |
| TC-FA-TDC-34 | TC-FA-TDC-E2E-009 | FE+BE |
| TC-FA-TDC-35 | TC-FA-TDC-E2E-008 | FE+BE |
| TC-FA-TDC-36 | TC-FA-TDC-E2E-009 | FE+BE |
| TC-FA-TDC-37 | TC-FA-TDC-E2E-058 | FE+BE |
| TC-FA-TDC-38 | TC-FA-TDC-E2E-012 | FE+BE |
| TC-FA-TDC-39 | TC-FA-TDC-E2E-012 | FE+BE |
| TC-FA-TDC-40 | TC-FA-TDC-E2E-012 | FE+BE |
| TC-FA-TDC-41 | TC-FA-TDC-E2E-013 | FE+BE |
| TC-FA-TDC-42 | TC-FA-TDC-E2E-013 | FE+BE |
| TC-FA-TDC-43 | TC-FA-TDC-E2E-013 | FE+BE |
| TC-FA-TDC-44 | TC-FA-TDC-E2E-014 | FE+BE |
| TC-FA-TDC-45 | TC-FA-TDC-E2E-014 | FE+BE |
| TC-FA-TDC-46 | TC-FA-TDC-E2E-013 | FE+BE |
| TC-FA-TDC-47 | TC-FA-TDC-E2E-015 | FE+BE |
| TC-FA-TDC-48 | TC-FA-TDC-E2E-015 | FE+BE |
| TC-FA-TDC-49 | TC-FA-TDC-E2E-016 | FE+BE |
| TC-FA-TDC-50 | TC-FA-TDC-E2E-017 | FE+BE |
| TC-FA-TDC-51 | TC-FA-TDC-E2E-229 | FE+BE |
| TC-FA-TDC-52 | TC-FA-TDC-E2E-017 | FE+BE |
| TC-FA-TDC-53 | TC-FA-TDC-E2E-016 | FE+BE |
| TC-FA-TDC-54 | TC-FA-TDC-E2E-016 | FE+BE |
| TC-FA-TDC-55 | TC-FA-TDC-E2E-016 | FE+BE |
| TC-FA-TDC-56 | TC-FA-TDC-E2E-017 | FE+BE |
| TC-FA-TDC-57 | TC-FA-TDC-E2E-016 | FE+BE |
| TC-FA-TDC-58 | TC-FA-TDC-E2E-018 | FE+BE |
| TC-FA-TDC-59 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-60 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-61 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-62 | TC-FA-TDC-E2E-018 | FE+BE |
| TC-FA-TDC-63 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-64 | TC-FA-TDC-E2E-018 | FE+BE |
| TC-FA-TDC-65 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-66 | TC-FA-TDC-E2E-020 | FE+BE |
| TC-FA-TDC-67 | TC-FA-TDC-E2E-019 | FE+BE |
| TC-FA-TDC-68 | TC-FA-TDC-E2E-020 | FE+BE |
| TC-FA-TDC-69 | TC-FA-TDC-E2E-021 | FE+BE |
| TC-FA-TDC-70 | TC-FA-TDC-E2E-021 | FE+BE |
| TC-FA-TDC-71 | TC-FA-TDC-E2E-022 | FE+BE |
| TC-FA-TDC-72 | TC-FA-TDC-E2E-022 | FE+BE |
| TC-FA-TDC-73 | TC-FA-TDC-E2E-023 | FE+BE |
| TC-FA-TDC-74 | TC-FA-TDC-E2E-023 | FE+BE |
| TC-FA-TDC-75 | TC-FA-TDC-E2E-023 | FE+BE |
| TC-FA-TDC-76 | TC-FA-TDC-E2E-023 | FE+BE |
| TC-FA-TDC-77 | TC-FA-TDC-E2E-023 | FE+BE |
| TC-FA-TDC-78 | TC-FA-TDC-E2E-024 | FE+BE |
| TC-FA-TDC-79 | TC-FA-TDC-E2E-024 | FE+BE |
| TC-FA-TDC-80 | TC-FA-TDC-E2E-024 | FE+BE |
| TC-FA-TDC-81 | TC-FA-TDC-E2E-024 | FE+BE |
| TC-FA-TDC-82 | TC-FA-TDC-E2E-026 | FE+BE |
| TC-FA-TDC-83 | TC-FA-TDC-E2E-026 | FE+BE |
| TC-FA-TDC-84 | TC-FA-TDC-E2E-026 | FE+BE |
| TC-FA-TDC-85 | TC-FA-TDC-E2E-025 | FE+BE |
| TC-FA-TDC-86 | TC-FA-TDC-E2E-025 | FE+BE |
| TC-FA-TDC-87 | TC-FA-TDC-E2E-025 | FE+BE |
| TC-FA-TDC-88 | TC-FA-TDC-E2E-027 | FE+BE |
| TC-FA-TDC-89 | TC-FA-TDC-E2E-027 | FE+BE |
| TC-FA-TDC-90 | TC-FA-TDC-E2E-027 | FE+BE |
| TC-FA-TDC-91 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-92 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-93 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-94 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-95 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-96 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-97 | TC-FA-TDC-E2E-028 | FE+BE |
| TC-FA-TDC-98 | TC-FA-TDC-E2E-029 | FE+BE |
| TC-FA-TDC-99 | TC-FA-TDC-E2E-030 | FE+BE |
| TC-FA-TDC-100 | TC-FA-TDC-E2E-029 | FE+BE |
| TC-FA-TDC-101 | TC-FA-TDC-E2E-231 | FE+BE |
| TC-FA-TDC-102 | TC-FA-TDC-E2E-264 | FE+BE |
| TC-FA-TDC-103 | TC-FA-TDC-E2E-040 | FE+BE |
| TC-FA-TDC-104 | TC-FA-TDC-E2E-040 | FE+BE |
| TC-FA-TDC-105 | TC-FA-TDC-E2E-041 | FE+BE |
| TC-FA-TDC-106 | TC-FA-TDC-E2E-041 | FE+BE |
| TC-FA-TDC-107 | TC-FA-TDC-E2E-041 | FE+BE |
| TC-FA-TDC-108 | TC-FA-TDC-E2E-042 | FE+BE |
| TC-FA-TDC-109 | TC-FA-TDC-E2E-042 | FE+BE |
| TC-FA-TDC-110 | TC-FA-TDC-E2E-233 | FE+BE |
| TC-FA-TDC-111 | TC-FA-TDC-E2E-043 | FE+BE |
| TC-FA-TDC-112 | TC-FA-TDC-E2E-043 | FE+BE |
| TC-FA-TDC-113 | TC-FA-TDC-E2E-234 | FE+BE |
| TC-FA-TDC-114 | TC-FA-TDC-E2E-044 | FE+BE |
| TC-FA-TDC-115 | TC-FA-TDC-E2E-044 | FE+BE |
| TC-FA-TDC-116 | TC-FA-TDC-E2E-044 | FE+BE |
| TC-FA-TDC-117 | TC-FA-TDC-E2E-123 | FE+BE |
| TC-FA-TDC-118 | TC-FA-TDC-E2E-054 | FE+BE |
| TC-FA-TDC-119 | TC-FA-TDC-E2E-054 | FE+BE |
| TC-FA-TDC-120 | TC-FA-TDC-E2E-054 | FE+BE |
| TC-FA-TDC-121 | TC-FA-TDC-E2E-054 | FE+BE |
| TC-FA-TDC-122 | TC-FA-TDC-E2E-054 | FE+BE |
| TC-FA-TDC-123 | TC-FA-TDC-E2E-055 | FE+BE |
| TC-FA-TDC-124 | TC-FA-TDC-E2E-055 | FE+BE |
| TC-FA-TDC-125 | TC-FA-TDC-E2E-055 | FE+BE |
| TC-FA-TDC-126 | TC-FA-TDC-E2E-037 | FE+BE |
| TC-FA-TDC-127 | TC-FA-TDC-E2E-037 | FE+BE |
| TC-FA-TDC-128 | TC-FA-TDC-E2E-037 | FE+BE |
| TC-FA-TDC-129 | TC-FA-TDC-E2E-037 | FE+BE |
| TC-FA-TDC-130 | TC-FA-TDC-E2E-232 | FE+BE |
| TC-FA-TDC-131 | TC-FA-TDC-E2E-038 | FE+BE |
| TC-FA-TDC-132 | TC-FA-TDC-E2E-123 | FE+BE |
| TC-FA-TDC-133 | TC-FA-TDC-E2E-232 | FE+BE |
| TC-FA-TDC-134 | TC-FA-TDC-E2E-197 | FE+BE |
| TC-FA-TDC-135 | TC-FA-TDC-E2E-045 | FE+BE |
| TC-FA-TDC-136 | TC-FA-TDC-E2E-045 | FE+BE |
| TC-FA-TDC-137 | TC-FA-TDC-E2E-045 | FE+BE |
| TC-FA-TDC-138 | TC-FA-TDC-E2E-045 | FE+BE |
| TC-FA-TDC-139 | TC-FA-TDC-E2E-045 | FE+BE |
| TC-FA-TDC-140 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-141 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-142 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-143 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-144 | TC-FA-TDC-E2E-047 | FE+BE |
| TC-FA-TDC-145 | TC-FA-TDC-E2E-047 | FE+BE |
| TC-FA-TDC-146 | TC-FA-TDC-E2E-047 | FE+BE |
| TC-FA-TDC-147 | TC-FA-TDC-E2E-047 | FE+BE |
| TC-FA-TDC-148 | TC-FA-TDC-E2E-047 | FE+BE |
| TC-FA-TDC-149 | TC-FA-TDC-E2E-048 | FE+BE |
| TC-FA-TDC-150 | TC-FA-TDC-E2E-048 | FE+BE |
| TC-FA-TDC-151 | TC-FA-TDC-E2E-048 | FE+BE |
| TC-FA-TDC-152 | TC-FA-TDC-E2E-049 | FE+BE |
| TC-FA-TDC-153 | TC-FA-TDC-E2E-049 | FE+BE |
| TC-FA-TDC-154 | TC-FA-TDC-E2E-049 | FE+BE |
| TC-FA-TDC-155 | TC-FA-TDC-E2E-049 | FE+BE |
| TC-FA-TDC-156 | TC-FA-TDC-E2E-049 | FE+BE |
| TC-FA-TDC-157 | TC-FA-TDC-E2E-050 | FE+BE |
| TC-FA-TDC-158 | TC-FA-TDC-E2E-050 | FE+BE |
| TC-FA-TDC-159 | TC-FA-TDC-E2E-050 | FE+BE |
| TC-FA-TDC-160 | TC-FA-TDC-E2E-224 | FE+BE |
| TC-FA-TDC-161 | TC-FA-TDC-E2E-224 | FE+BE |
| TC-FA-TDC-162 | TC-FA-TDC-E2E-051 | FE+BE |
| TC-FA-TDC-163 | TC-FA-TDC-E2E-051 | FE+BE |
| TC-FA-TDC-164 | TC-FA-TDC-E2E-051 | FE+BE |
| TC-FA-TDC-165 | TC-FA-TDC-E2E-052 | FE+BE |
| TC-FA-TDC-166 | TC-FA-TDC-E2E-052 | FE+BE |
| TC-FA-TDC-167 | TC-FA-TDC-E2E-052 | FE+BE |
| TC-FA-TDC-168 | TC-FA-TDC-E2E-053 | FE+BE |
| TC-FA-TDC-169 | TC-FA-TDC-E2E-053 | FE+BE |
| TC-FA-TDC-170 | TC-FA-TDC-E2E-053 | FE+BE |
| TC-FA-TDC-171 | TC-FA-TDC-E2E-052 | FE+BE |
| TC-FA-TDC-172 | TC-FA-TDC-E2E-053 | FE+BE |
| TC-FA-TDC-173 | TC-FA-TDC-E2E-217 | FE+BE |
| TC-FA-TDC-174 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-175 | TC-FA-TDC-E2E-046 | FE+BE |
| TC-FA-TDC-176 | TC-FA-TDC-E2E-040 | FE+BE |
| TC-FA-TDC-177 | TC-FA-TDC-E2E-056 | FE+BE |
| TC-FA-TDC-178 | TC-FA-TDC-E2E-056 | FE+BE |
| TC-FA-TDC-179 | TC-FA-TDC-E2E-235 | FE+BE |
| TC-FA-TDC-180 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-181 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-182 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-183 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-184 | TC-FA-TDC-E2E-061 | FE+BE |
| TC-FA-TDC-185 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-186 | TC-FA-TDC-E2E-057 | FE+BE |
| TC-FA-TDC-187 | TC-FA-TDC-E2E-058 | FE+BE |
| TC-FA-TDC-188 | TC-FA-TDC-E2E-058 | FE+BE |
| TC-FA-TDC-189 | TC-FA-TDC-E2E-059 | FE+BE |
| TC-FA-TDC-190 | TC-FA-TDC-E2E-059 | FE+BE |
| TC-FA-TDC-191 | TC-FA-TDC-E2E-236 | FE+BE |
| TC-FA-TDC-192 | TC-FA-TDC-E2E-236 | FE+BE |
| TC-FA-TDC-193 | TC-FA-TDC-E2E-060 | FE+BE |
| TC-FA-TDC-194 | TC-FA-TDC-E2E-060 | FE+BE |
| TC-FA-TDC-195 | TC-FA-TDC-E2E-060 | FE+BE |
| TC-FA-TDC-196 | TC-FA-TDC-E2E-060 | FE+BE |
| TC-FA-TDC-197 | TC-FA-TDC-E2E-062 | FE+BE |
| TC-FA-TDC-198 | TC-FA-TDC-E2E-062 | FE+BE |
| TC-FA-TDC-199 | TC-FA-TDC-E2E-062 | FE+BE |
| TC-FA-TDC-200 | TC-FA-TDC-E2E-064 | FE+BE |
| TC-FA-TDC-201 | TC-FA-TDC-E2E-124 | FE+BE |
| TC-FA-TDC-202 | TC-FA-TDC-E2E-124 | FE+BE |
| TC-FA-TDC-203 | TC-FA-TDC-E2E-063 | FE+BE |
| TC-FA-TDC-204 | TC-FA-TDC-E2E-063 | FE+BE |
| TC-FA-TDC-205 | TC-FA-TDC-E2E-063 | FE+BE |
| TC-FA-TDC-206 | TC-FA-TDC-E2E-063 | FE+BE |
| TC-FA-TDC-207 | TC-FA-TDC-E2E-063 | FE+BE |
| TC-FA-TDC-208 | TC-FA-TDC-E2E-064 | FE+BE |
| TC-FA-TDC-209 | TC-FA-TDC-E2E-064 | FE+BE |
| TC-FA-TDC-210 | TC-FA-TDC-E2E-125 | FE+BE |
| TC-FA-TDC-211 | TC-FA-TDC-E2E-125 | FE+BE |
| TC-FA-TDC-212 | TC-FA-TDC-E2E-125 | FE+BE |
| TC-FA-TDC-213 | TC-FA-TDC-E2E-126 | FE+BE |
| TC-FA-TDC-214 | TC-FA-TDC-E2E-126 | FE+BE |
| TC-FA-TDC-215 | TC-FA-TDC-E2E-061 | FE+BE |
| TC-FA-TDC-216 | TC-FA-TDC-E2E-061 | FE+BE |
| TC-FA-TDC-217 | TC-FA-TDC-E2E-061 | FE+BE |
| TC-FA-TDC-218 | TC-FA-TDC-E2E-060 | FE+BE |
| TC-FA-TDC-219 | TC-FA-TDC-E2E-062 | FE+BE |
| TC-FA-TDC-220 | TC-FA-TDC-E2E-065 | FE+BE |
| TC-FA-TDC-221 | TC-FA-TDC-E2E-065 | FE+BE |
| TC-FA-TDC-222 | TC-FA-TDC-E2E-065 | FE+BE |
| TC-FA-TDC-223 | TC-FA-TDC-E2E-065 | FE+BE |
| TC-FA-TDC-224 | TC-FA-TDC-E2E-065 | FE+BE |
| TC-FA-TDC-225 | TC-FA-TDC-E2E-066 | FE+BE |
| TC-FA-TDC-226 | TC-FA-TDC-E2E-066 | FE+BE |
| TC-FA-TDC-227 | TC-FA-TDC-E2E-066 | FE+BE |
| TC-FA-TDC-228 | TC-FA-TDC-E2E-066 | FE+BE |
| TC-FA-TDC-229 | TC-FA-TDC-E2E-066 | FE+BE |
| TC-FA-TDC-230 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-231 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-232 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-233 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-234 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-235 | TC-FA-TDC-E2E-067 | FE+BE |
| TC-FA-TDC-236 | TC-FA-TDC-E2E-068 | FE+BE |
| TC-FA-TDC-237 | TC-FA-TDC-E2E-068 | FE+BE |
| TC-FA-TDC-238 | TC-FA-TDC-E2E-068 | FE+BE |
| TC-FA-TDC-239 | TC-FA-TDC-E2E-068 | FE+BE |
| TC-FA-TDC-240 | TC-FA-TDC-E2E-068 | FE+BE |
| TC-FA-TDC-241 | TC-FA-TDC-E2E-069 | FE+BE |
| TC-FA-TDC-242 | TC-FA-TDC-E2E-069 | FE+BE |
| TC-FA-TDC-243 | TC-FA-TDC-E2E-069 | FE+BE |
| TC-FA-TDC-244 | TC-FA-TDC-E2E-257 | FE+BE |
| TC-FA-TDC-245 | TC-FA-TDC-E2E-257 | FE+BE |
| TC-FA-TDC-246 | TC-FA-TDC-E2E-069 | FE+BE |
| TC-FA-TDC-247 | TC-FA-TDC-E2E-058 | FE+BE |
| TC-FA-TDC-248 | TC-FA-TDC-E2E-070 | FE+BE |
| TC-FA-TDC-249 | TC-FA-TDC-E2E-070 | FE+BE |
| TC-FA-TDC-250 | TC-FA-TDC-E2E-070 | FE+BE |
| TC-FA-TDC-251 | TC-FA-TDC-E2E-071 | FE+BE |
| TC-FA-TDC-252 | TC-FA-TDC-E2E-071 | FE+BE |
| TC-FA-TDC-253 | TC-FA-TDC-E2E-259 | FE+BE |
| TC-FA-TDC-254 | TC-FA-TDC-E2E-071 | FE+BE |
| TC-FA-TDC-255 | TC-FA-TDC-E2E-071 | FE+BE |
| TC-FA-TDC-256 | TC-FA-TDC-E2E-072 | FE+BE |
| TC-FA-TDC-257 | TC-FA-TDC-E2E-072 | FE+BE |
| TC-FA-TDC-258 | TC-FA-TDC-E2E-238 | FE+BE |
| TC-FA-TDC-259 | TC-FA-TDC-E2E-073 | FE+BE |
| TC-FA-TDC-260 | TC-FA-TDC-E2E-073 | FE+BE |
| TC-FA-TDC-261 | TC-FA-TDC-E2E-073 | FE+BE |
| TC-FA-TDC-262 | TC-FA-TDC-E2E-074 | FE+BE |
| TC-FA-TDC-263 | TC-FA-TDC-E2E-127 | FE+BE |
| TC-FA-TDC-264 | TC-FA-TDC-E2E-127 | FE+BE |
| TC-FA-TDC-265 | TC-FA-TDC-E2E-074 | FE+BE |
| TC-FA-TDC-266 | TC-FA-TDC-E2E-074 | FE+BE |
| TC-FA-TDC-267 | TC-FA-TDC-E2E-076 | FE+BE |
| TC-FA-TDC-268 | TC-FA-TDC-E2E-076 | FE+BE |
| TC-FA-TDC-269 | TC-FA-TDC-E2E-077 | FE+BE |
| TC-FA-TDC-270 | TC-FA-TDC-E2E-077 | FE+BE |
| TC-FA-TDC-271 | TC-FA-TDC-E2E-077 | FE+BE |
| TC-FA-TDC-272 | TC-FA-TDC-E2E-078 | FE+BE |
| TC-FA-TDC-273 | TC-FA-TDC-E2E-078 | FE+BE |
| TC-FA-TDC-274 | TC-FA-TDC-E2E-078 | FE+BE |
| TC-FA-TDC-275 | TC-FA-TDC-E2E-079 | FE+BE |
| TC-FA-TDC-276 | TC-FA-TDC-E2E-079 | FE+BE |
| TC-FA-TDC-277 | TC-FA-TDC-E2E-079 | FE+BE |
| TC-FA-TDC-278 | TC-FA-TDC-E2E-079 | FE+BE |
| TC-FA-TDC-279 | TC-FA-TDC-E2E-080 | FE+BE |
| TC-FA-TDC-280 | TC-FA-TDC-E2E-080 | FE+BE |
| TC-FA-TDC-281 | TC-FA-TDC-E2E-080 | FE+BE |
| TC-FA-TDC-282 | TC-FA-TDC-E2E-245 | FE+BE |
| TC-FA-TDC-283 | TC-FA-TDC-E2E-081 | FE+BE |
| TC-FA-TDC-284 | TC-FA-TDC-E2E-237 | FE+BE |
| TC-FA-TDC-285 | TC-FA-TDC-E2E-237 | FE+BE |
| TC-FA-TDC-286 | TC-FA-TDC-E2E-081 | FE+BE |
| TC-FA-TDC-287 | TC-FA-TDC-E2E-081 | FE+BE |
| TC-FA-TDC-288 | TC-FA-TDC-E2E-082 | FE+BE |
| TC-FA-TDC-289 | TC-FA-TDC-E2E-082 | FE+BE |
| TC-FA-TDC-290 | TC-FA-TDC-E2E-082 | FE+BE |
| TC-FA-TDC-291 | TC-FA-TDC-E2E-245 | FE+BE |
| TC-FA-TDC-292 | TC-FA-TDC-E2E-082 | FE+BE |
| TC-FA-TDC-293 | TC-FA-TDC-E2E-011 | FE+BE |
| TC-FA-TDC-294 | TC-FA-TDC-E2E-083 | FE+BE |
| TC-FA-TDC-295 | TC-FA-TDC-E2E-083 | FE+BE |
| TC-FA-TDC-296 | TC-FA-TDC-E2E-083 | FE+BE |
| TC-FA-TDC-297 | TC-FA-TDC-E2E-083 | FE+BE |
| TC-FA-TDC-298 | TC-FA-TDC-E2E-084 | FE+BE |
| TC-FA-TDC-299 | TC-FA-TDC-E2E-084 | FE+BE |
| TC-FA-TDC-300 | TC-FA-TDC-E2E-084 | FE+BE |
| TC-FA-TDC-301 | TC-FA-TDC-E2E-025 | FE+BE |
| TC-FA-TDC-302 | TC-FA-TDC-E2E-084 | FE+BE |
| TC-FA-TDC-303 | TC-FA-TDC-E2E-085 | FE+BE |
| TC-FA-TDC-304 | TC-FA-TDC-E2E-085 | FE+BE |
| TC-FA-TDC-305 | TC-FA-TDC-E2E-086 | FE+BE |
| TC-FA-TDC-306 | TC-FA-TDC-E2E-128 | FE+BE |
| TC-FA-TDC-307 | TC-FA-TDC-E2E-090 | FE+BE |
| TC-FA-TDC-308 | TC-FA-TDC-E2E-090 | FE+BE |
| TC-FA-TDC-309 | TC-FA-TDC-E2E-090 | FE+BE |
| TC-FA-TDC-310 | TC-FA-TDC-E2E-090 | FE+BE |
| TC-FA-TDC-311 | TC-FA-TDC-E2E-128 | FE+BE |
| TC-FA-TDC-312 | TC-FA-TDC-E2E-086 | FE+BE |
| TC-FA-TDC-313 | TC-FA-TDC-E2E-024 | FE+BE |
| TC-FA-TDC-314 | TC-FA-TDC-E2E-085 | FE+BE |
| TC-FA-TDC-315 | TC-FA-TDC-E2E-087 | FE+BE |
| TC-FA-TDC-316 | TC-FA-TDC-E2E-004 | FE+BE |
| TC-FA-TDC-317 | TC-FA-TDC-E2E-004 | FE+BE |
| TC-FA-TDC-318 | TC-FA-TDC-E2E-004 | FE+BE |
| TC-FA-TDC-319 | TC-FA-TDC-E2E-087 | FE+BE |
| TC-FA-TDC-320 | TC-FA-TDC-E2E-129 | FE+BE |
| TC-FA-TDC-321 | TC-FA-TDC-E2E-087 | FE+BE |
| TC-FA-TDC-322 | TC-FA-TDC-E2E-087 | FE+BE |
| TC-FA-TDC-323 | TC-FA-TDC-E2E-022 | FE+BE |
| TC-FA-TDC-324 | TC-FA-TDC-E2E-239 | FE+BE |
| TC-FA-TDC-325 | TC-FA-TDC-E2E-129 | FE+BE |
| TC-FA-TDC-326 | TC-FA-TDC-E2E-129 | FE+BE |
| TC-FA-TDC-327 | TC-FA-TDC-E2E-130 | FE+BE |
| TC-FA-TDC-328 | TC-FA-TDC-E2E-130 | FE+BE |
| TC-FA-TDC-329 | TC-FA-TDC-E2E-131 | FE+BE |
| TC-FA-TDC-330 | TC-FA-TDC-E2E-131 | FE+BE |
| TC-FA-TDC-331 | TC-FA-TDC-E2E-131 | FE+BE |
| TC-FA-TDC-332 | TC-FA-TDC-E2E-130 | FE+BE |
| TC-FA-TDC-333 | TC-FA-TDC-E2E-088 | FE+BE |
| TC-FA-TDC-334 | TC-FA-TDC-E2E-088 | FE+BE |
| TC-FA-TDC-335 | TC-FA-TDC-E2E-088 | FE+BE |
| TC-FA-TDC-336 | TC-FA-TDC-E2E-089 | FE+BE |
| TC-FA-TDC-337 | TC-FA-TDC-E2E-089 | FE+BE |
| TC-FA-TDC-338 | TC-FA-TDC-E2E-089 | FE+BE |
| TC-FA-TDC-339 | TC-FA-TDC-E2E-089 | FE+BE |
| TC-FA-TDC-340 | TC-FA-TDC-E2E-091 | FE+BE |
| TC-FA-TDC-341 | TC-FA-TDC-E2E-091 | FE+BE |
| TC-FA-TDC-342 | TC-FA-TDC-E2E-091 | FE+BE |
| TC-FA-TDC-343 | TC-FA-TDC-E2E-092 | FE+BE |
| TC-FA-TDC-344 | TC-FA-TDC-E2E-092 | FE+BE |
| TC-FA-TDC-345 | TC-FA-TDC-E2E-092 | FE+BE |
| TC-FA-TDC-346 | TC-FA-TDC-E2E-092 | FE+BE |
| TC-FA-TDC-347 | TC-FA-TDC-E2E-093 | FE+BE |
| TC-FA-TDC-348 | TC-FA-TDC-E2E-093 | FE+BE |
| TC-FA-TDC-350 | TC-FA-TDC-E2E-094 | FE+BE |
| TC-FA-TDC-351 | TC-FA-TDC-E2E-094 | FE+BE |
| TC-FA-TDC-352 | TC-FA-TDC-E2E-094 | FE+BE |
| TC-FA-TDC-353 | TC-FA-TDC-E2E-095 | FE+BE |
| TC-FA-TDC-354 | TC-FA-TDC-E2E-095 | FE+BE |
| TC-FA-TDC-355 | TC-FA-TDC-E2E-095 | FE+BE |
| TC-FA-TDC-356 | TC-FA-TDC-E2E-095 | FE+BE |
| TC-FA-TDC-357 | TC-FA-TDC-E2E-095 | FE+BE |
| TC-FA-TDC-358 | TC-FA-TDC-E2E-240 | FE+BE |
| TC-FA-TDC-359 | TC-FA-TDC-E2E-240 | FE+BE |
| TC-FA-TDC-360 | TC-FA-TDC-E2E-036 | FE+BE |
| TC-FA-TDC-361 | TC-FA-TDC-E2E-097 | FE+BE |
| TC-FA-TDC-362 | TC-FA-TDC-E2E-241 | FE+BE |
| TC-FA-TDC-363 | TC-FA-TDC-E2E-097 | FE+BE |
| TC-FA-TDC-364 | TC-FA-TDC-E2E-097 | FE+BE |
| TC-FA-TDC-365 | TC-FA-TDC-E2E-097 | FE+BE |
| TC-FA-TDC-366 | TC-FA-TDC-E2E-009 | FE+BE |
| TC-FA-TDC-367 | TC-FA-TDC-E2E-132 | FE+BE |
| TC-FA-TDC-368 | TC-FA-TDC-E2E-132 | FE+BE |
| TC-FA-TDC-369 | TC-FA-TDC-E2E-105 | FE+BE |
| TC-FA-TDC-370 | TC-FA-TDC-E2E-105 | FE+BE |
| TC-FA-TDC-371 | TC-FA-TDC-E2E-104 | FE+BE |
| TC-FA-TDC-372 | TC-FA-TDC-E2E-097 | FE+BE |
| TC-FA-TDC-373 | TC-FA-TDC-E2E-098 | FE+BE |
| TC-FA-TDC-374 | TC-FA-TDC-E2E-241 | FE+BE |
| TC-FA-TDC-375 | TC-FA-TDC-E2E-098 | FE+BE |
| TC-FA-TDC-376 | TC-FA-TDC-E2E-098 | FE+BE |
| TC-FA-TDC-377 | TC-FA-TDC-E2E-098 | FE+BE |
| TC-FA-TDC-378 | TC-FA-TDC-E2E-009 | FE+BE |
| TC-FA-TDC-379 | TC-FA-TDC-E2E-099 | FE+BE |
| TC-FA-TDC-380 | TC-FA-TDC-E2E-099 | FE+BE |
| TC-FA-TDC-381 | TC-FA-TDC-E2E-099 | FE+BE |
| TC-FA-TDC-382 | TC-FA-TDC-E2E-099 | FE+BE |
| TC-FA-TDC-383 | TC-FA-TDC-E2E-100 | FE+BE |
| TC-FA-TDC-384 | TC-FA-TDC-E2E-100 | FE+BE |
| TC-FA-TDC-385 | TC-FA-TDC-E2E-100 | FE+BE |
| TC-FA-TDC-386 | TC-FA-TDC-E2E-100 | FE+BE |
| TC-FA-TDC-387 | TC-FA-TDC-E2E-132 | FE+BE |
| TC-FA-TDC-388 | TC-FA-TDC-E2E-132 | FE+BE |
| TC-FA-TDC-389 | TC-FA-TDC-E2E-132 | FE+BE |
| TC-FA-TDC-390 | TC-FA-TDC-E2E-105 | FE+BE |
| TC-FA-TDC-391 | TC-FA-TDC-E2E-105 | FE+BE |
| TC-FA-TDC-392 | TC-FA-TDC-E2E-104 | FE+BE |
| TC-FA-TDC-393 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-394 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-395 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-396 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-397 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-398 | TC-FA-TDC-E2E-101 | FE+BE |
| TC-FA-TDC-399 | TC-FA-TDC-E2E-102 | FE+BE |
| TC-FA-TDC-400 | TC-FA-TDC-E2E-102 | FE+BE |
| TC-FA-TDC-401 | TC-FA-TDC-E2E-102 | FE+BE |
| TC-FA-TDC-402 | TC-FA-TDC-E2E-102 | FE+BE |
| TC-FA-TDC-403 | TC-FA-TDC-E2E-103 | FE+BE |
| TC-FA-TDC-404 | TC-FA-TDC-E2E-103 | FE+BE |
| TC-FA-TDC-405 | TC-FA-TDC-E2E-103 | FE+BE |
| TC-FA-TDC-406 | TC-FA-TDC-E2E-103 | FE+BE |
| TC-FA-TDC-407 | TC-FA-TDC-E2E-133 | FE+BE |
| TC-FA-TDC-408 | TC-FA-TDC-E2E-133 | FE+BE |
| TC-FA-TDC-409 | TC-FA-TDC-E2E-133 | FE+BE |
| TC-FA-TDC-410 | TC-FA-TDC-E2E-106 | FE+BE |
| TC-FA-TDC-411 | TC-FA-TDC-E2E-106 | FE+BE |
| TC-FA-TDC-412 | TC-FA-TDC-E2E-104 | FE+BE |
| TC-FA-TDC-413 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-414 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-415 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-416 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-417 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-418 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-419 | TC-FA-TDC-E2E-110 | FE+BE |
| TC-FA-TDC-420 | TC-FA-TDC-E2E-111 | FE+BE |
| TC-FA-TDC-421 | TC-FA-TDC-E2E-111 | FE+BE |
| TC-FA-TDC-422 | TC-FA-TDC-E2E-111 | FE+BE |
| TC-FA-TDC-423 | TC-FA-TDC-E2E-039 | FE+BE |
| TC-FA-TDC-424 | TC-FA-TDC-E2E-039 | FE+BE |
| TC-FA-TDC-425 | TC-FA-TDC-E2E-111 | FE+BE |
| TC-FA-TDC-426 | TC-FA-TDC-E2E-112 | FE+BE |
| TC-FA-TDC-427 | TC-FA-TDC-E2E-112 | FE+BE |
| TC-FA-TDC-428 | TC-FA-TDC-E2E-112 | FE+BE |
| TC-FA-TDC-429 | TC-FA-TDC-E2E-113 | FE+BE |
| TC-FA-TDC-430 | TC-FA-TDC-E2E-113 | FE+BE |
| TC-FA-TDC-431 | TC-FA-TDC-E2E-113 | FE+BE |
| TC-FA-TDC-432 | TC-FA-TDC-E2E-113 | FE+BE |
| TC-FA-TDC-433 | TC-FA-TDC-E2E-114 | FE+BE |
| TC-FA-TDC-434 | TC-FA-TDC-E2E-114 | FE+BE |
| TC-FA-TDC-435 | TC-FA-TDC-E2E-243 | FE+BE |
| TC-FA-TDC-436 | TC-FA-TDC-E2E-243 | FE+BE |
| TC-FA-TDC-437 | TC-FA-TDC-E2E-115 | FE+BE |
| TC-FA-TDC-438 | TC-FA-TDC-E2E-115 | FE+BE |
| TC-FA-TDC-439 | TC-FA-TDC-E2E-244 | FE+BE |
| TC-FA-TDC-440 | TC-FA-TDC-E2E-244 | FE+BE |
| TC-FA-TDC-441 | TC-FA-TDC-E2E-116 | FE+BE |
| TC-FA-TDC-442 | TC-FA-TDC-E2E-116 | FE+BE |
| TC-FA-TDC-443 | TC-FA-TDC-E2E-116 | FE+BE |
| TC-FA-TDC-444 | TC-FA-TDC-E2E-117 | FE+BE |
| TC-FA-TDC-445 | TC-FA-TDC-E2E-117 | FE+BE |
| TC-FA-TDC-446 | TC-FA-TDC-E2E-117 | FE+BE |
| TC-FA-TDC-447 | TC-FA-TDC-E2E-118 | FE+BE |
| TC-FA-TDC-448 | TC-FA-TDC-E2E-118 | FE+BE |
| TC-FA-TDC-449 | TC-FA-TDC-E2E-118 | FE+BE |
| TC-FA-TDC-450 | TC-FA-TDC-E2E-118 | FE+BE |
| TC-FA-TDC-451 | TC-FA-TDC-E2E-119 | FE+BE |
| TC-FA-TDC-452 | TC-FA-TDC-E2E-119 | FE+BE |
| TC-FA-TDC-453 | TC-FA-TDC-E2E-119 | FE+BE |
| TC-FA-TDC-454 | TC-FA-TDC-E2E-119 | FE+BE |
| TC-FA-TDC-455 | TC-FA-TDC-E2E-119 | FE+BE |
| TC-FA-TDC-456 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-457 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-458 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-459 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-460 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-461 | TC-FA-TDC-E2E-120 | FE+BE |
| TC-FA-TDC-462 | TC-FA-TDC-E2E-121 | FE+BE |
| TC-FA-TDC-463 | TC-FA-TDC-E2E-121 | FE+BE |
| TC-FA-TDC-464 | TC-FA-TDC-E2E-121 | FE+BE |
| TC-FA-TDC-465 | TC-FA-TDC-E2E-121 | FE+BE |
| TC-FA-TDC-466 | TC-FA-TDC-E2E-121 | FE+BE |
| TC-FA-TDC-467 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-468 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-469 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-470 | TC-FA-TDC-E2E-135 | FE+BE |
| TC-FA-TDC-471 | TC-FA-TDC-E2E-135 | FE+BE |
| TC-FA-TDC-472 | TC-FA-TDC-E2E-135 | FE+BE |
| TC-FA-TDC-473 | TC-FA-TDC-E2E-135 | FE+BE |
| TC-FA-TDC-474 | TC-FA-TDC-E2E-136 | FE+BE |
| TC-FA-TDC-475 | TC-FA-TDC-E2E-136 | FE+BE |
| TC-FA-TDC-476 | TC-FA-TDC-E2E-136 | FE+BE |
| TC-FA-TDC-477 | TC-FA-TDC-E2E-136 | FE+BE |
| TC-FA-TDC-478 | TC-FA-TDC-E2E-137 | FE+BE |
| TC-FA-TDC-479 | TC-FA-TDC-E2E-137 | FE+BE |
| TC-FA-TDC-480 | TC-FA-TDC-E2E-137 | FE+BE |
| TC-FA-TDC-481 | TC-FA-TDC-E2E-107 | FE+BE |
| TC-FA-TDC-482 | TC-FA-TDC-E2E-107 | FE+BE |
| TC-FA-TDC-483 | TC-FA-TDC-E2E-107 | FE+BE |
| TC-FA-TDC-484 | TC-FA-TDC-E2E-108 | FE+BE |
| TC-FA-TDC-485 | TC-FA-TDC-E2E-108 | FE+BE |
| TC-FA-TDC-486 | TC-FA-TDC-E2E-108 | FE+BE |
| TC-FA-TDC-487 | TC-FA-TDC-E2E-242 | FE+BE |
| TC-FA-TDC-488 | TC-FA-TDC-E2E-242 | FE+BE |
| TC-FA-TDC-489 | TC-FA-TDC-E2E-143 | FE+BE |
| TC-FA-TDC-490 | TC-FA-TDC-E2E-143 | FE+BE |
| TC-FA-TDC-491 | TC-FA-TDC-E2E-143 | FE+BE |
| TC-FA-TDC-492 | TC-FA-TDC-E2E-143 | FE+BE |
| TC-FA-TDC-493 | TC-FA-TDC-E2E-144 | FE+BE |
| TC-FA-TDC-494 | TC-FA-TDC-E2E-144 | FE+BE |
| TC-FA-TDC-495 | TC-FA-TDC-E2E-144 | FE+BE |
| TC-FA-TDC-496 | TC-FA-TDC-E2E-247 | FE+BE |
| TC-FA-TDC-497 | TC-FA-TDC-E2E-247 | FE+BE |
| TC-FA-TDC-498 | TC-FA-TDC-E2E-145 | FE+BE |
| TC-FA-TDC-499 | TC-FA-TDC-E2E-145 | FE+BE |
| TC-FA-TDC-500 | TC-FA-TDC-E2E-145 | FE+BE |
| TC-FA-TDC-501 | TC-FA-TDC-E2E-145 | FE+BE |
| TC-FA-TDC-502 | TC-FA-TDC-E2E-145 | FE+BE |
| TC-FA-TDC-503 | TC-FA-TDC-E2E-146 | FE+BE |
| TC-FA-TDC-504 | TC-FA-TDC-E2E-146 | FE+BE |
| TC-FA-TDC-505 | TC-FA-TDC-E2E-146 | FE+BE |
| TC-FA-TDC-506 | TC-FA-TDC-E2E-146 | FE+BE |
| TC-FA-TDC-507 | TC-FA-TDC-E2E-147 | FE+BE |
| TC-FA-TDC-508 | TC-FA-TDC-E2E-147 | FE+BE |
| TC-FA-TDC-509 | TC-FA-TDC-E2E-147 | FE+BE |
| TC-FA-TDC-510 | TC-FA-TDC-E2E-147 | FE+BE |
| TC-FA-TDC-511 | TC-FA-TDC-E2E-148 | FE+BE |
| TC-FA-TDC-512 | TC-FA-TDC-E2E-148 | FE+BE |
| TC-FA-TDC-513 | TC-FA-TDC-E2E-148 | FE+BE |
| TC-FA-TDC-514 | TC-FA-TDC-E2E-148 | FE+BE |
| TC-FA-TDC-515 | TC-FA-TDC-E2E-148 | FE+BE |
| TC-FA-TDC-516 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-517 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-518 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-519 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-520 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-521 | TC-FA-TDC-E2E-149 | FE+BE |
| TC-FA-TDC-522 | TC-FA-TDC-E2E-150 | FE+BE |
| TC-FA-TDC-523 | TC-FA-TDC-E2E-150 | FE+BE |
| TC-FA-TDC-524 | TC-FA-TDC-E2E-150 | FE+BE |
| TC-FA-TDC-525 | TC-FA-TDC-E2E-150 | FE+BE |
| TC-FA-TDC-526 | TC-FA-TDC-E2E-248 | FE+BE |
| TC-FA-TDC-527 | TC-FA-TDC-E2E-248 | FE+BE |
| TC-FA-TDC-528 | TC-FA-TDC-E2E-151 | FE+BE |
| TC-FA-TDC-529 | TC-FA-TDC-E2E-151 | FE+BE |
| TC-FA-TDC-530 | TC-FA-TDC-E2E-151 | FE+BE |
| TC-FA-TDC-531 | TC-FA-TDC-E2E-151 | FE+BE |
| TC-FA-TDC-532 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-533 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-534 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-535 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-536 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-537 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-538 | TC-FA-TDC-E2E-152 | FE+BE |
| TC-FA-TDC-539 | TC-FA-TDC-E2E-153 | FE+BE |
| TC-FA-TDC-540 | TC-FA-TDC-E2E-153 | FE+BE |
| TC-FA-TDC-541 | TC-FA-TDC-E2E-153 | FE+BE |
| TC-FA-TDC-542 | TC-FA-TDC-E2E-154 | FE+BE |
| TC-FA-TDC-543 | TC-FA-TDC-E2E-154 | FE+BE |
| TC-FA-TDC-544 | TC-FA-TDC-E2E-155 | FE+BE |
| TC-FA-TDC-545 | TC-FA-TDC-E2E-155 | FE+BE |
| TC-FA-TDC-546 | TC-FA-TDC-E2E-155 | FE+BE |
| TC-FA-TDC-547 | TC-FA-TDC-E2E-155 | FE+BE |
| TC-FA-TDC-548 | TC-FA-TDC-E2E-156 | FE+BE |
| TC-FA-TDC-549 | TC-FA-TDC-E2E-156 | FE+BE |
| TC-FA-TDC-550 | TC-FA-TDC-E2E-156 | FE+BE |
| TC-FA-TDC-551 | TC-FA-TDC-E2E-139 | FE+BE |
| TC-FA-TDC-552 | TC-FA-TDC-E2E-156 | FE+BE |
| TC-FA-TDC-553 | TC-FA-TDC-E2E-156 | FE+BE |
| TC-FA-TDC-554 | TC-FA-TDC-E2E-157 | FE+BE |
| TC-FA-TDC-555 | TC-FA-TDC-E2E-157 | FE+BE |
| TC-FA-TDC-556 | TC-FA-TDC-E2E-157 | FE+BE |
| TC-FA-TDC-557 | TC-FA-TDC-E2E-157 | FE+BE |
| TC-FA-TDC-558 | TC-FA-TDC-E2E-157 | FE+BE |
| TC-FA-TDC-559 | TC-FA-TDC-E2E-158 | FE+BE |
| TC-FA-TDC-560 | TC-FA-TDC-E2E-158 | FE+BE |
| TC-FA-TDC-561 | TC-FA-TDC-E2E-158 | FE+BE |
| TC-FA-TDC-562 | TC-FA-TDC-E2E-158 | FE+BE |
| TC-FA-TDC-563 | TC-FA-TDC-E2E-139 | FE+BE |
| TC-FA-TDC-564 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-565 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-566 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-567 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-568 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-569 | TC-FA-TDC-E2E-160 | FE+BE |
| TC-FA-TDC-570 | TC-FA-TDC-E2E-160 | FE+BE |
| TC-FA-TDC-571 | TC-FA-TDC-E2E-160 | FE+BE |
| TC-FA-TDC-572 | TC-FA-TDC-E2E-160 | FE+BE |
| TC-FA-TDC-573 | TC-FA-TDC-E2E-160 | FE+BE |
| TC-FA-TDC-574 | TC-FA-TDC-E2E-161 | FE+BE |
| TC-FA-TDC-575 | TC-FA-TDC-E2E-161 | FE+BE |
| TC-FA-TDC-576 | TC-FA-TDC-E2E-161 | FE+BE |
| TC-FA-TDC-577 | TC-FA-TDC-E2E-161 | FE+BE |
| TC-FA-TDC-578 | TC-FA-TDC-E2E-162 | FE+BE |
| TC-FA-TDC-579 | TC-FA-TDC-E2E-163 | FE+BE |
| TC-FA-TDC-580 | TC-FA-TDC-E2E-163 | FE+BE |
| TC-FA-TDC-583 | TC-FA-TDC-E2E-164 | FE+BE |
| TC-FA-TDC-584 | TC-FA-TDC-E2E-164 | FE+BE |
| TC-FA-TDC-585 | TC-FA-TDC-E2E-164 | FE+BE |
| TC-FA-TDC-586 | TC-FA-TDC-E2E-138 | FE+BE |
| TC-FA-TDC-587 | TC-FA-TDC-E2E-164 | FE+BE |
| TC-FA-TDC-588 | TC-FA-TDC-E2E-164 | FE+BE |
| TC-FA-TDC-589 | TC-FA-TDC-E2E-165 | FE+BE |
| TC-FA-TDC-590 | TC-FA-TDC-E2E-165 | FE+BE |
| TC-FA-TDC-591 | TC-FA-TDC-E2E-166 | FE+BE |
| TC-FA-TDC-592 | TC-FA-TDC-E2E-166 | FE+BE |
| TC-FA-TDC-593 | TC-FA-TDC-E2E-166 | FE+BE |
| TC-FA-TDC-594 | TC-FA-TDC-E2E-162 | FE+BE |
| TC-FA-TDC-595 | TC-FA-TDC-E2E-167 | FE+BE |
| TC-FA-TDC-596 | TC-FA-TDC-E2E-167 | FE+BE |
| TC-FA-TDC-597 | TC-FA-TDC-E2E-168 | FE+BE |
| TC-FA-TDC-598 | TC-FA-TDC-E2E-249 | FE+BE |
| TC-FA-TDC-599 | TC-FA-TDC-E2E-250 | FE+BE |
| TC-FA-TDC-600 | TC-FA-TDC-E2E-167 | FE+BE |
| TC-FA-TDC-601 | TC-FA-TDC-E2E-167 | FE+BE |
| TC-FA-TDC-602 | TC-FA-TDC-E2E-168 | FE+BE |
| TC-FA-TDC-603 | TC-FA-TDC-E2E-169 | FE+BE |
| TC-FA-TDC-604 | TC-FA-TDC-E2E-169 | FE+BE |
| TC-FA-TDC-605 | TC-FA-TDC-E2E-169 | FE+BE |
| TC-FA-TDC-606 | TC-FA-TDC-E2E-169 | FE+BE |
| TC-FA-TDC-607 | TC-FA-TDC-E2E-170 | FE+BE |
| TC-FA-TDC-608 | TC-FA-TDC-E2E-170 | FE+BE |
| TC-FA-TDC-609 | TC-FA-TDC-E2E-170 | FE+BE |
| TC-FA-TDC-610 | TC-FA-TDC-E2E-170 | FE+BE |
| TC-FA-TDC-611 | TC-FA-TDC-E2E-171 | FE+BE |
| TC-FA-TDC-612 | TC-FA-TDC-E2E-171 | FE+BE |
| TC-FA-TDC-613 | TC-FA-TDC-E2E-172 | FE+BE |
| TC-FA-TDC-614 | TC-FA-TDC-E2E-172 | FE+BE |
| TC-FA-TDC-615 | TC-FA-TDC-E2E-173 | FE+BE |
| TC-FA-TDC-616 | TC-FA-TDC-E2E-173 | FE+BE |
| TC-FA-TDC-617 | TC-FA-TDC-E2E-173 | FE+BE |
| TC-FA-TDC-618 | TC-FA-TDC-E2E-173 | FE+BE |
| TC-FA-TDC-619 | TC-FA-TDC-E2E-172 | FE+BE |
| TC-FA-TDC-620 | TC-FA-TDC-E2E-172 | FE+BE |
| TC-FA-TDC-621 | TC-FA-TDC-E2E-174 | FE+BE |
| TC-FA-TDC-622 | TC-FA-TDC-E2E-174 | FE+BE |
| TC-FA-TDC-623 | TC-FA-TDC-E2E-174 | FE+BE |
| TC-FA-TDC-624 | TC-FA-TDC-E2E-174 | FE+BE |
| TC-FA-TDC-625 | TC-FA-TDC-E2E-175 | FE+BE |
| TC-FA-TDC-626 | TC-FA-TDC-E2E-175 | FE+BE |
| TC-FA-TDC-627 | TC-FA-TDC-E2E-175 | FE+BE |
| TC-FA-TDC-628 | TC-FA-TDC-E2E-175 | FE+BE |
| TC-FA-TDC-629 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-630 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-631 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-632 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-633 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-634 | TC-FA-TDC-E2E-176 | FE+BE |
| TC-FA-TDC-635 | TC-FA-TDC-E2E-177 | FE+BE |
| TC-FA-TDC-636 | TC-FA-TDC-E2E-177 | FE+BE |
| TC-FA-TDC-637 | TC-FA-TDC-E2E-177 | FE+BE |
| TC-FA-TDC-638 | TC-FA-TDC-E2E-177 | FE+BE |
| TC-FA-TDC-639 | TC-FA-TDC-E2E-177 | FE+BE |
| TC-FA-TDC-640 | TC-FA-TDC-E2E-178 | FE+BE |
| TC-FA-TDC-641 | TC-FA-TDC-E2E-178 | FE+BE |
| TC-FA-TDC-642 | TC-FA-TDC-E2E-251 | FE+BE |
| TC-FA-TDC-643 | TC-FA-TDC-E2E-179 | FE+BE |
| TC-FA-TDC-644 | TC-FA-TDC-E2E-252 | FE+BE |
| TC-FA-TDC-645 | TC-FA-TDC-E2E-180 | FE+BE |
| TC-FA-TDC-646 | TC-FA-TDC-E2E-180 | FE+BE |
| TC-FA-TDC-647 | TC-FA-TDC-E2E-180 | FE+BE |
| TC-FA-TDC-648 | TC-FA-TDC-E2E-181 | FE+BE |
| TC-FA-TDC-649 | TC-FA-TDC-E2E-181 | FE+BE |
| TC-FA-TDC-650 | TC-FA-TDC-E2E-181 | FE+BE |
| TC-FA-TDC-651 | TC-FA-TDC-E2E-181 | FE+BE |
| TC-FA-TDC-652 | TC-FA-TDC-E2E-182 | FE+BE |
| TC-FA-TDC-653 | TC-FA-TDC-E2E-182 | FE+BE |
| TC-FA-TDC-654 | TC-FA-TDC-E2E-182 | FE+BE |
| TC-FA-TDC-655 | TC-FA-TDC-E2E-182 | FE+BE |
| TC-FA-TDC-656 | TC-FA-TDC-E2E-183 | FE+BE |
| TC-FA-TDC-657 | TC-FA-TDC-E2E-183 | FE+BE |
| TC-FA-TDC-658 | TC-FA-TDC-E2E-183 | FE+BE |
| TC-FA-TDC-659 | TC-FA-TDC-E2E-184 | FE+BE |
| TC-FA-TDC-660 | TC-FA-TDC-E2E-185 | FE+BE |
| TC-FA-TDC-661 | TC-FA-TDC-E2E-185 | FE+BE |
| TC-FA-TDC-662 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-663 | TC-FA-TDC-E2E-185 | FE+BE |
| TC-FA-TDC-664 | TC-FA-TDC-E2E-185 | FE+BE |
| TC-FA-TDC-665 | TC-FA-TDC-E2E-185 | FE+BE |
| TC-FA-TDC-666 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-667 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-668 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-669 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-670 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-671 | TC-FA-TDC-E2E-186 | FE+BE |
| TC-FA-TDC-672 | TC-FA-TDC-E2E-187 | FE+BE |
| TC-FA-TDC-673 | TC-FA-TDC-E2E-187 | FE+BE |
| TC-FA-TDC-674 | TC-FA-TDC-E2E-246 | FE+BE |
| TC-FA-TDC-675 | TC-FA-TDC-E2E-188 | FE+BE |
| TC-FA-TDC-676 | TC-FA-TDC-E2E-188 | FE+BE |
| TC-FA-TDC-677 | TC-FA-TDC-E2E-188 | FE+BE |
| TC-FA-TDC-678 | TC-FA-TDC-E2E-189 | FE+BE |
| TC-FA-TDC-679 | TC-FA-TDC-E2E-189 | FE+BE |
| TC-FA-TDC-680 | TC-FA-TDC-E2E-189 | FE+BE |
| TC-FA-TDC-681 | TC-FA-TDC-E2E-197 | FE+BE |
| TC-FA-TDC-682 | TC-FA-TDC-E2E-190 | FE+BE |
| TC-FA-TDC-683 | TC-FA-TDC-E2E-190 | FE+BE |
| TC-FA-TDC-684 | TC-FA-TDC-E2E-190 | FE+BE |
| TC-FA-TDC-685 | TC-FA-TDC-E2E-191 | FE+BE |
| TC-FA-TDC-686 | TC-FA-TDC-E2E-191 | FE+BE |
| TC-FA-TDC-687 | TC-FA-TDC-E2E-191 | FE+BE |
| TC-FA-TDC-688 | TC-FA-TDC-E2E-187 | FE+BE |
| TC-FA-TDC-689 | TC-FA-TDC-E2E-187 | FE+BE |
| TC-FA-TDC-690 | TC-FA-TDC-E2E-096 | FE+BE |
| TC-FA-TDC-691 | TC-FA-TDC-E2E-096 | FE+BE |
| TC-FA-TDC-692 | TC-FA-TDC-E2E-096 | FE+BE |
| TC-FA-TDC-693 | TC-FA-TDC-E2E-096 | FE+BE |
| TC-FA-TDC-694 | TC-FA-TDC-E2E-197 | FE+BE |
| TC-FA-TDC-695 | TC-FA-TDC-E2E-253 | FE+BE |
| TC-FA-TDC-696 | TC-FA-TDC-E2E-253 | FE+BE |
| TC-FA-TDC-697 | TC-FA-TDC-E2E-198 | FE+BE |
| TC-FA-TDC-698 | TC-FA-TDC-E2E-192 | FE+BE |
| TC-FA-TDC-699 | TC-FA-TDC-E2E-192 | FE+BE |
| TC-FA-TDC-700 | TC-FA-TDC-E2E-192 | FE+BE |
| TC-FA-TDC-701 | TC-FA-TDC-E2E-192 | FE+BE |
| TC-FA-TDC-702 | TC-FA-TDC-E2E-192 | FE+BE |
| TC-FA-TDC-703 | TC-FA-TDC-E2E-193 | FE+BE |
| TC-FA-TDC-704 | TC-FA-TDC-E2E-193 | FE+BE |
| TC-FA-TDC-705 | TC-FA-TDC-E2E-193 | FE+BE |
| TC-FA-TDC-706 | TC-FA-TDC-E2E-193 | FE+BE |
| TC-FA-TDC-707 | TC-FA-TDC-E2E-194 | FE+BE |
| TC-FA-TDC-708 | TC-FA-TDC-E2E-194 | FE+BE |
| TC-FA-TDC-709 | TC-FA-TDC-E2E-194 | FE+BE |
| TC-FA-TDC-710 | TC-FA-TDC-E2E-194 | FE+BE |
| TC-FA-TDC-711 | TC-FA-TDC-E2E-194 | FE+BE |
| TC-FA-TDC-712 | TC-FA-TDC-E2E-195 | FE+BE |
| TC-FA-TDC-713 | TC-FA-TDC-E2E-195 | FE+BE |
| TC-FA-TDC-714 | TC-FA-TDC-E2E-195 | FE+BE |
| TC-FA-TDC-715 | TC-FA-TDC-E2E-195 | FE+BE |
| TC-FA-TDC-716 | TC-FA-TDC-E2E-198 | FE+BE |
| TC-FA-TDC-717 | TC-FA-TDC-E2E-198 | FE+BE |
| TC-FA-TDC-718 | TC-FA-TDC-E2E-198 | FE+BE |
| TC-FA-TDC-719 | TC-FA-TDC-E2E-198 | FE+BE |
| TC-FA-TDC-720 | TC-FA-TDC-E2E-138 | FE+BE |
| TC-FA-TDC-721 | TC-FA-TDC-E2E-138 | FE+BE |
| TC-FA-TDC-722 | TC-FA-TDC-E2E-196 | FE+BE |
| TC-FA-TDC-723 | TC-FA-TDC-E2E-196 | FE+BE |
| TC-FA-TDC-724 | TC-FA-TDC-E2E-196 | FE+BE |
| TC-FA-TDC-725 | TC-FA-TDC-E2E-199 | FE+BE |
| TC-FA-TDC-726 | TC-FA-TDC-E2E-199 | FE+BE |
| TC-FA-TDC-727 | TC-FA-TDC-E2E-199 | FE+BE |
| TC-FA-TDC-728 | TC-FA-TDC-E2E-199 | FE+BE |
| TC-FA-TDC-729 | TC-FA-TDC-E2E-255 | FE+BE |
| TC-FA-TDC-730 | TC-FA-TDC-E2E-255 | FE+BE |
| TC-FA-TDC-731 | TC-FA-TDC-E2E-255 | FE+BE |
| TC-FA-TDC-732 | TC-FA-TDC-E2E-255 | FE+BE |
| TC-FA-TDC-733 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-734 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-735 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-736 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-737 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-738 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-739 | TC-FA-TDC-E2E-200 | FE+BE |
| TC-FA-TDC-740 | TC-FA-TDC-E2E-201 | FE+BE |
| TC-FA-TDC-741 | TC-FA-TDC-E2E-201 | FE+BE |
| TC-FA-TDC-742 | TC-FA-TDC-E2E-201 | FE+BE |
| TC-FA-TDC-743 | TC-FA-TDC-E2E-201 | FE+BE |
| TC-FA-TDC-744 | TC-FA-TDC-E2E-201 | FE+BE |
| TC-FA-TDC-746 | TC-FA-TDC-E2E-202 | FE+BE |
| TC-FA-TDC-747 | TC-FA-TDC-E2E-202 | FE+BE |
| TC-FA-TDC-748 | TC-FA-TDC-E2E-202 | FE+BE |
| TC-FA-TDC-749 | TC-FA-TDC-E2E-203 | FE+BE |
| TC-FA-TDC-750 | TC-FA-TDC-E2E-203 | FE+BE |
| TC-FA-TDC-751 | TC-FA-TDC-E2E-203 | FE+BE |
| TC-FA-TDC-752 | TC-FA-TDC-E2E-203 | FE+BE |
| TC-FA-TDC-753 | TC-FA-TDC-E2E-204 | FE+BE |
| TC-FA-TDC-754 | TC-FA-TDC-E2E-204 | FE+BE |
| TC-FA-TDC-755 | TC-FA-TDC-E2E-204 | FE+BE |
| TC-FA-TDC-756 | TC-FA-TDC-E2E-075 | FE+BE |
| TC-FA-TDC-757 | TC-FA-TDC-E2E-075 | FE+BE |
| TC-FA-TDC-758 | TC-FA-TDC-E2E-075 | FE+BE |
| TC-FA-TDC-759 | TC-FA-TDC-E2E-038 | FE+BE |
| TC-FA-TDC-760 | TC-FA-TDC-E2E-038 | FE+BE |
| TC-FA-TDC-761 | TC-FA-TDC-E2E-038 | FE+BE |
| TC-FA-TDC-762 | TC-FA-TDC-E2E-038 | FE+BE |
| TC-FA-TDC-763 | TC-FA-TDC-E2E-123 | FE+BE |
| TC-FA-TDC-764 | TC-FA-TDC-E2E-029 | FE+BE |
| TC-FA-TDC-765 | TC-FA-TDC-E2E-029 | FE+BE |
| TC-FA-TDC-766 | TC-FA-TDC-E2E-030 | FE+BE |
| TC-FA-TDC-767 | TC-FA-TDC-E2E-030 | FE+BE |
| TC-FA-TDC-768 | TC-FA-TDC-E2E-030 | FE+BE |
| TC-FA-TDC-769 | TC-FA-TDC-E2E-030 | FE+BE |
| TC-FA-TDC-770 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-771 | TC-FA-TDC-E2E-140 | FE+BE |
| TC-FA-TDC-772 | TC-FA-TDC-E2E-140 | FE+BE |
| TC-FA-TDC-773 | TC-FA-TDC-E2E-140 | FE+BE |
| TC-FA-TDC-774 | TC-FA-TDC-E2E-141 | FE+BE |
| TC-FA-TDC-775 | TC-FA-TDC-E2E-141 | FE+BE |
| TC-FA-TDC-776 | TC-FA-TDC-E2E-141 | FE+BE |
| TC-FA-TDC-777 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-778 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-779 | TC-FA-TDC-E2E-206 | FE+BE |
| TC-FA-TDC-780 | TC-FA-TDC-E2E-206 | FE+BE |
| TC-FA-TDC-781 | TC-FA-TDC-E2E-206 | FE+BE |
| TC-FA-TDC-782 | TC-FA-TDC-E2E-206 | FE+BE |
| TC-FA-TDC-783 | TC-FA-TDC-E2E-206 | FE+BE |
| TC-FA-TDC-784 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-785 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-786 | TC-FA-TDC-E2E-205 | FE+BE |
| TC-FA-TDC-787 | TC-FA-TDC-E2E-196 | FE+BE |
| TC-FA-TDC-788 | TC-FA-TDC-E2E-256 | FE+BE |
| TC-FA-TDC-789 | TC-FA-TDC-E2E-256 | FE+BE |
| TC-FA-TDC-790 | TC-FA-TDC-E2E-256 | FE+BE |
| TC-FA-TDC-791 | TC-FA-TDC-E2E-207 | FE+BE |
| TC-FA-TDC-792 | TC-FA-TDC-E2E-207 | FE+BE |
| TC-FA-TDC-793 | TC-FA-TDC-E2E-207 | FE+BE |
| TC-FA-TDC-794 | TC-FA-TDC-E2E-207 | FE+BE |
| TC-FA-TDC-795 | TC-FA-TDC-E2E-208 | FE+BE |
| TC-FA-TDC-796 | TC-FA-TDC-E2E-208 | FE+BE |
| TC-FA-TDC-797 | TC-FA-TDC-E2E-208 | FE+BE |
| TC-FA-TDC-798 | TC-FA-TDC-E2E-208 | FE+BE |
| TC-FA-TDC-799 | TC-FA-TDC-E2E-209 | FE+BE |
| TC-FA-TDC-800 | TC-FA-TDC-E2E-209 | FE+BE |
| TC-FA-TDC-801 | TC-FA-TDC-E2E-209 | FE+BE |
| TC-FA-TDC-802 | TC-FA-TDC-E2E-209 | FE+BE |
| TC-FA-TDC-803 | TC-FA-TDC-E2E-210 | FE+BE |
| TC-FA-TDC-804 | TC-FA-TDC-E2E-210 | FE+BE |
| TC-FA-TDC-805 | TC-FA-TDC-E2E-210 | FE+BE |
| TC-FA-TDC-806 | TC-FA-TDC-E2E-210 | FE+BE |
| TC-FA-TDC-807 | TC-FA-TDC-E2E-211 | FE+BE |
| TC-FA-TDC-808 | TC-FA-TDC-E2E-211 | FE+BE |
| TC-FA-TDC-809 | TC-FA-TDC-E2E-211 | FE+BE |
| TC-FA-TDC-810 | TC-FA-TDC-E2E-211 | FE+BE |
| TC-FA-TDC-811 | TC-FA-TDC-E2E-212 | FE+BE |
| TC-FA-TDC-812 | TC-FA-TDC-E2E-212 | FE+BE |
| TC-FA-TDC-813 | TC-FA-TDC-E2E-212 | FE+BE |
| TC-FA-TDC-814 | TC-FA-TDC-E2E-212 | FE+BE |
| TC-FA-TDC-815 | TC-FA-TDC-E2E-213 | FE+BE |
| TC-FA-TDC-816 | TC-FA-TDC-E2E-213 | FE+BE |
| TC-FA-TDC-817 | TC-FA-TDC-E2E-213 | FE+BE |
| TC-FA-TDC-818 | TC-FA-TDC-E2E-213 | FE+BE |
| TC-FA-TDC-819 | TC-FA-TDC-E2E-214 | FE+BE |
| TC-FA-TDC-820 | TC-FA-TDC-E2E-214 | FE+BE |
| TC-FA-TDC-821 | TC-FA-TDC-E2E-214 | FE+BE |
| TC-FA-TDC-822 | TC-FA-TDC-E2E-214 | FE+BE |
| TC-FA-TDC-823 | TC-FA-TDC-E2E-215 | FE+BE |
| TC-FA-TDC-824 | TC-FA-TDC-E2E-215 | FE+BE |
| TC-FA-TDC-825 | TC-FA-TDC-E2E-215 | FE+BE |
| TC-FA-TDC-826 | TC-FA-TDC-E2E-215 | FE+BE |
| TC-FA-TDC-827 | TC-FA-TDC-E2E-216 | FE+BE |
| TC-FA-TDC-828 | TC-FA-TDC-E2E-216 | FE+BE |
| TC-FA-TDC-829 | TC-FA-TDC-E2E-216 | FE+BE |
| TC-FA-TDC-830 | TC-FA-TDC-E2E-216 | FE+BE |
| TC-FA-TDC-831 | TC-FA-TDC-E2E-217 | FE+BE |
| TC-FA-TDC-832 | TC-FA-TDC-E2E-218 | FE+BE |
| TC-FA-TDC-833 | TC-FA-TDC-E2E-218 | FE+BE |
| TC-FA-TDC-834 | TC-FA-TDC-E2E-219 | FE+BE |
| TC-FA-TDC-835 | TC-FA-TDC-E2E-219 | FE+BE |
| TC-FA-TDC-836 | TC-FA-TDC-E2E-219 | FE+BE |
| TC-FA-TDC-837 | TC-FA-TDC-E2E-219 | FE+BE |
| TC-FA-TDC-838 | TC-FA-TDC-E2E-219 | FE+BE |
| TC-FA-TDC-839 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-840 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-841 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-842 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-843 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-844 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-845 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-846 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-847 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-848 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-849 | TC-FA-TDC-E2E-221 | FE+BE |
| TC-FA-TDC-850 | TC-FA-TDC-E2E-224 | FE+BE |
| TC-FA-TDC-851 | TC-FA-TDC-E2E-222 | FE+BE |
| TC-FA-TDC-852 | TC-FA-TDC-E2E-222 | FE+BE |
| TC-FA-TDC-853 | TC-FA-TDC-E2E-222 | FE+BE |
| TC-FA-TDC-854 | TC-FA-TDC-E2E-222 | FE+BE |
| TC-FA-TDC-855 | TC-FA-TDC-E2E-222 | FE+BE |
| TC-FA-TDC-856 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-857 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-858 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-859 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-860 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-861 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-862 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-863 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-864 | TC-FA-TDC-E2E-142 | FE+BE |
| TC-FA-TDC-865 | TC-FA-TDC-E2E-225 | FE+BE |
| TC-FA-TDC-866 | TC-FA-TDC-E2E-225 | FE+BE |
| TC-FA-TDC-867 | TC-FA-TDC-E2E-225 | FE+BE |
| TC-FA-TDC-868 | TC-FA-TDC-E2E-225 | FE+BE |
| TC-FA-TDC-869 | TC-FA-TDC-E2E-225 | FE+BE |
| TC-FA-TDC-870 | TC-FA-TDC-E2E-226 | FE+BE |
| TC-FA-TDC-871 | TC-FA-TDC-E2E-226 | FE+BE |
| TC-FA-TDC-872 | TC-FA-TDC-E2E-226 | FE+BE |
| TC-FA-TDC-873 | TC-FA-TDC-E2E-226 | FE+BE |
| TC-FA-TDC-874 | TC-FA-TDC-E2E-032 | FE+BE |
| TC-FA-TDC-875 | TC-FA-TDC-E2E-032 | FE+BE |
| TC-FA-TDC-876 | TC-FA-TDC-E2E-032 | FE+BE |
| TC-FA-TDC-877 | TC-FA-TDC-E2E-033 | FE+BE |
| TC-FA-TDC-878 | TC-FA-TDC-E2E-033 | FE+BE |
| TC-FA-TDC-879 | TC-FA-TDC-E2E-033 | FE+BE |
| TC-FA-TDC-880 | TC-FA-TDC-E2E-034 | FE+BE |
| TC-FA-TDC-881 | TC-FA-TDC-E2E-034 | FE+BE |
| TC-FA-TDC-882 | TC-FA-TDC-E2E-034 | FE+BE |
| TC-FA-TDC-883 | TC-FA-TDC-E2E-034 | FE+BE |
| TC-FA-TDC-884 | TC-FA-TDC-E2E-035 | FE+BE |
| TC-FA-TDC-885 | TC-FA-TDC-E2E-035 | FE+BE |
| TC-FA-TDC-886 | TC-FA-TDC-E2E-035 | FE+BE |
| TC-FA-TDC-887 | TC-FA-TDC-E2E-035 | FE+BE |
| TC-FA-TDC-888 | TC-FA-TDC-E2E-217 | FE+BE |
| TC-FA-TDC-889 | TC-FA-TDC-E2E-031 | FE+BE |
| TC-FA-TDC-890 | TC-FA-TDC-E2E-031 | FE+BE |
| TC-FA-TDC-891 | TC-FA-TDC-E2E-036 | FE+BE |
| TC-FA-TDC-892 | TC-FA-TDC-E2E-036 | FE+BE |
| TC-FA-TDC-893 | TC-FA-TDC-E2E-036 | FE+BE |
| TC-FA-TDC-894 | TC-FA-TDC-E2E-036 | FE+BE |
| TC-FA-TDC-895 | TC-FA-TDC-E2E-133 | FE+BE |
| TC-FA-TDC-896 | TC-FA-TDC-E2E-134 | FE+BE |
| TC-FA-TDC-897 | TC-FA-TDC-E2E-134 | FE+BE |
| TC-FA-TDC-898 | TC-FA-TDC-E2E-134 | FE+BE |
| TC-FA-TDC-899 | TC-FA-TDC-E2E-106 | FE+BE |
| TC-FA-TDC-900 | TC-FA-TDC-E2E-106 | FE+BE |
| TC-FA-TDC-901 | TC-FA-TDC-E2E-108 | FE+BE |
| TC-FA-TDC-902 | TC-FA-TDC-E2E-109 | FE+BE |
| TC-FA-TDC-903 | TC-FA-TDC-E2E-109 | FE+BE |
| TC-FA-TDC-904 | TC-FA-TDC-E2E-109 | FE+BE |
| TC-FA-TDC-905 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-906 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-907 | TC-FA-TDC-E2E-122 | FE+BE |
| TC-FA-TDC-908 | TC-FA-TDC-E2E-109 | FE+BE |
| TC-FA-TDC-909 | TC-FA-TDC-E2E-218 | FE+BE |
| TC-FA-TDC-910 | TC-FA-TDC-E2E-258 | FE+BE |
| TC-FA-TDC-911 | TC-FA-TDC-E2E-258 | FE+BE |
| TC-FA-TDC-912 | TC-FA-TDC-E2E-258 | FE+BE |
| TC-FA-TDC-913 | TC-FA-TDC-E2E-096 | FE+BE |
| TC-FA-TDC-914 | TC-FA-TDC-E2E-159 | FE+BE |
| TC-FA-TDC-915 | TC-FA-TDC-E2E-040 | FE+BE |
| TC-FA-TDC-916 | TC-FA-TDC-E2E-010 | FE+BE |
| TC-FA-TDC-917 | TC-FA-TDC-E2E-010 | FE+BE |
| TC-FA-TDC-918 | TC-FA-TDC-E2E-227 | FE+BE |
| TC-FA-TDC-919 | TC-FA-TDC-E2E-037 | FE+BE |
| TC-FA-TDC-920 | TC-FA-TDC-E2E-227 | FE+BE |
| TC-FA-TDC-921 | TC-FA-TDC-E2E-126 | FE+BE |
| TC-FA-TDC-922 | TC-FA-TDC-E2E-228 | FE+BE |
| TC-FA-TDC-923 | TC-FA-TDC-E2E-228 | FE+BE |
| TC-FA-TDC-924 | TC-FA-TDC-E2E-204 | FE+BE |
| TC-FA-TDC-925 | TC-FA-TDC-E2E-204 | FE+BE |
| TC-FA-TDC-926 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-927 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-928 | TC-FA-TDC-E2E-223 | FE+BE |
| TC-FA-TDC-929 | TC-FA-TDC-E2E-166 | FE+BE |
| TC-FA-TDC-930 | TC-FA-TDC-E2E-162 | FE+BE |
| TC-FA-TDC-931 | TC-FA-TDC-E2E-158 | FE+BE |
| TC-FA-TDC-932 | TC-FA-TDC-E2E-190 | FE+BE |
| TC-FA-TDC-933 | TC-FA-TDC-E2E-184 | FE+BE |
| TC-FA-TDC-934 | TC-FA-TDC-E2E-075 | FE+BE |
| TC-FA-TDC-935 | TC-FA-TDC-E2E-279 | FE+BE |
| TC-FA-TDC-936 | TC-FA-TDC-E2E-281 | FE+BE |
| TC-FA-TDC-937 | TC-FA-TDC-E2E-282 | FE+BE |
| TC-FA-TDC-938 | TC-FA-TDC-E2E-282 | FE+BE |
| TC-FA-TDC-939 | TC-FA-TDC-E2E-280 | FE+BE |
| TC-FA-TDC-940 | TC-FA-TDC-E2E-280 | FE+BE |
| TC-FA-TDC-941 | TC-FA-TDC-E2E-280 | FE+BE |
| TC-FA-TDC-942 | TC-FA-TDC-E2E-280 | FE+BE |
| TC-FA-TDC-943 | TC-FA-TDC-E2E-279 | FE+BE |
| TC-FA-TDC-944 | TC-FA-TDC-E2E-283 | FE+BE |
| TC-FA-TDC-945 | TC-FA-TDC-E2E-283 | FE+BE |
| TC-FA-TDC-946 | TC-FA-TDC-E2E-284 | FE+BE |
| TC-FA-TDC-947 | TC-FA-TDC-E2E-284 | FE+BE |
| TC-FA-TDC-948 | TC-FA-TDC-E2E-285 | FE+BE |
| TC-FA-TDC-949 | TC-FA-TDC-E2E-284 | FE+BE |
| TC-FA-TDC-950 | TC-FA-TDC-E2E-281 | FE+BE |
| TC-FA-TDC-951 | TC-FA-TDC-E2E-285 | FE+BE |
| TC-FA-TDC-952 | TC-FA-TDC-E2E-279 | FE+BE |
| TC-FA-TDC-953 | TC-FA-TDC-E2E-286 | FE+BE |
| TC-FA-TDC-954 | TC-FA-TDC-E2E-286 | FE+BE |
| TC-FA-TDC-955 | TC-FA-TDC-E2E-287 | FE+BE |
| TC-FA-TDC-956 | TC-FA-TDC-E2E-287 | FE+BE |
| TC-FA-TDC-957 | TC-FA-TDC-E2E-287 | FE+BE |
| TC-FA-TDC-958 | TC-FA-TDC-E2E-286 | FE+BE |
| TC-FA-TDC-959 | TC-FA-TDC-E2E-287 | FE+BE |
| TC-FA-TDC-960 | TC-FA-TDC-E2E-286 | FE+BE |
| TC-FA-TDC-961 | TC-FA-TDC-E2E-289 | FE+BE |
| TC-FA-TDC-962 | TC-FA-TDC-E2E-275 | FE+BE |
| TC-FA-TDC-963 | TC-FA-TDC-E2E-276 | FE+BE |
| TC-FA-TDC-964 | TC-FA-TDC-E2E-220 | FE+BE |
| TC-FA-TDC-965 | TC-FA-TDC-E2E-275 | FE+BE |
| TC-FA-TDC-966 | TC-FA-TDC-E2E-277 | FE+BE |
| TC-FA-TDC-967 | TC-FA-TDC-E2E-278 | FE+BE |
