# Coverage E2E — Fixed Asset > Settings > Accounting Preferences

Sumber: `fixed-asset/settings-accounting-preferences/TestCases/tc-settings-accounting-preferences.md` (617 TC aktif `TC-FA-PREF-1`–`621`; TC 326, 399, 400 dan 620 retired). Suite: `specs/FixedAsset/SettingsAccountingPreferences/`. Prefix: `FA` + `PREF` (`TC-FA-PREF-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-settings-accounting-preferences-backend.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 617 TC aktif masuk 173 spec (154 nomor rencana, 17 nomor cadangan, dan 2 nomor tambahan 175-176), tidak ada TC hanya-BE. Setiap TC yang masuk terpetakan ke tepat satu spec.

## TC hanya-BE (tidak masuk spec)

Tidak ada. File backend TC tidak ada. TC defense-in-depth dengan Expected respons API tetap masuk spec FE+BE dengan butir K-1.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-PREF-E2E-001-screening-tab-preferences-initial-state-dan-sectioncard-general-capitalization-depreciation | Screening Tab Preferences: Initial State dan SectionCard General, Capitalization, Depreciation dengan Nilai Awal | FE+BE | 29 | 1, 3, 4, 5 |
| TC-FA-PREF-E2E-002-screening-sectioncard-disposal-chart-of-accounts-journal-export-urutan-dan-nilai-awal | Screening SectionCard Disposal, Chart of Accounts, Journal Export, Urutan SectionCard, dan Nilai Awal Seluruh Setting | FE+BE | 30 | 6, 7, 8, 21, 22 |
| TC-FA-PREF-E2E-003-anchor-sticky-klik-anchor-menggulir-form-ke-sectioncard | Daftar Anchor Sticky: Klik Anchor Menggulir Form ke SectionCard | FE+BE | 24 | 9, 10, 11, 12, 13, 14 |
| TC-FA-PREF-E2E-004-navigasi-tab-preferences-tautan-langsung-entri-sidebar-form-company-dan-layout-tablet | Navigasi Tab Preferences: Klik Tab, Tautan Langsung, Entri Sidebar, Form Company Langsung, dan Layout Tablet | FE+BE | 21 | 15, 16, 17, 601, 67 |
| TC-FA-PREF-E2E-005-opsi-select-dan-multiselect-fiscal-year-start-first-accounting-period-in-service-depreciation-month-journal-grouping | Opsi Select dan MultiSelect: Fiscal Year Start, First Accounting Period, In-service Date Source, Depreciation in Disposal Month, Journal Grouping | FE+BE | 33 | 23, 24, 25, 26, 164, 165, 596 |
| TC-FA-PREF-E2E-006-tooltip-ikon-info-setting-set-01-sampai-set-07 | Tooltip Ikon Info ⓘ Setting SET-01 sampai SET-07 | FE+BE | 14 | 29, 30, 31, 32, 33, 34, 35 |
| TC-FA-PREF-E2E-007-tooltip-set-08-set-09-set-11-set-12-format-opsi-dan-placeholder-select | Tooltip Ikon Info ⓘ SET-08, SET-09, SET-11, SET-12, Format Opsi Select Akun, dan Placeholder Select Saat Nilai Kosong | FE+BE | 23 | 36, 37, 38, 39, 46, 47, 48, 49, 50 |
| TC-FA-PREF-E2E-008-helper-text-disposal-documents-per-jenis-dokumen | Helper Text Disposal Documents per Jenis Dokumen | FE+BE | 13 | 40, 41, 42, 43, 44, 45 |
| TC-FA-PREF-E2E-009-guided-tooltip-kunjungan-pertama-step-1-sampai-4 | Guided Tooltip Preferences: Kunjungan Pertama Menampilkan Step 1 sampai Step 4 | FE+BE | 26 | 52, 53, 54, 55 |
| TC-FA-PREF-E2E-010-guided-tooltip-back-done-skip-dan-replay | Guided Tooltip Preferences: [Back], [Done], [Skip], dan Replay Lewat [?] | FE+BE | 32 | 56, 57, 58, 59 |
| TC-FA-PREF-E2E-011-aksesibilitas-keyboard-fokus-trap-label-dan-tooltip | Aksesibilitas: navigasi keyboard, fokus ter-trap dialog D-01 dan modal Changelog, label titik peringatan, tooltip keyboard | FE+BE | 28 | 60, 61, 62, 63, 64, 65 |
| TC-FA-PREF-E2E-012-android-form-halaman-penuh-header-bottom-sheet-changelog | Android: form halaman penuh, ikon View history di header, dialog Save Changes bottom sheet, modal Changelog card list | FE+BE | 17 | 68, 69, 70, 71 |
| TC-FA-PREF-E2E-013-android-dialog-d03-d04-bottom-sheet-dan-tooltip-disabled | Android: dialog D-03 dan D-04 sebagai bottom sheet, tooltip elemen Disabled bagi Read Only | FE+BE | 24 | 72, 606, 607 |
| TC-FA-PREF-E2E-014-shimmer-form-preferences-dan-modal-changelog | Shimmer: form Preferences dan modal Changelog saat data dimuat | FE+BE | 15 | 73, 295 |
| TC-FA-PREF-E2E-015-banner-setup-incomplete-dan-titik-peringatan-sectioncard | Banner Setup Incomplete dan titik peringatan SectionCard: isi, tidak dapat ditutup, tidak tampil bila lengkap | FE+BE | 15 | 76, 77, 78, 79, 81, 82 |
| TC-FA-PREF-E2E-016-banner-setup-incomplete-hilang-setelah-setting-wajib-disimpan | Banner Setup Incomplete hilang setelah setting wajib terakhir disimpan dan memuat setting kosong menurut urutan SectionCard | FE+BE | 18 | 80, 397, 398 |
| TC-FA-PREF-E2E-017-kunci-fiscal-year-start-dan-first-accounting-period-gembok-tooltip | Kunci Fiscal Year Start dan First Accounting Period: gembok, tooltip, field lain tetap Enabled | FE+BE | 24 | 83, 84, 85, 86, 87, 124 |
| TC-FA-PREF-E2E-018-helper-peringatan-akun-default-inactive | Helper peringatan akun default Inactive pada keempat Select akun | FE+BE | 11 | 91, 92, 93, 94, 95 |
| TC-FA-PREF-E2E-019-spinner-saving-save-changes-tanpa-d01 | Spinner Saving pada [Save changes] saat Save tanpa dialog D-01 diproses | FE+BE | 20 | 89, 283 |
| TC-FA-PREF-E2E-020-spinner-saving-save-pada-dialog-d01 | Spinner Saving pada [Save] di dialog Save Changes D-01 | FE+BE | 21 | 90, 284 |
| TC-FA-PREF-E2E-021-kontrol-tidak-tersedia-pada-tab-preferences | Kontrol yang tidak disediakan tab Preferences: Create, Delete, Search, Filter, bulk action, Download, paginasi, setting keterangan jurnal | FE+BE | 18 | 2, 594, 595, 608 |
| TC-FA-PREF-E2E-022-role-matrix-visibilitas-total-control-default-user-read-only | Role Matrix: Visibilitas dan Kontrol Preferences untuk Total Control, Default User, dan Read Only | FE+BE | 28 | 96, 97, 98 |
| TC-FA-PREF-E2E-023-role-matrix-visibilitas-manage-accounting-read-dan-read-update | Role Matrix: Visibilitas Preferences untuk Manage accounting Read dan Read + Update, termasuk tombol tersembunyi | FE+BE | 31 | 99, 100, 229, 561 |
| TC-FA-PREF-E2E-024-role-matrix-visibilitas-manage-accounting-create-dan-shortcut-create-account | Role Matrix: Visibilitas Preferences untuk Manage accounting Read + Create dan Read + Create + Update, shortcut Create account | FE+BE | 32 | 101, 102, 122, 123 |
| TC-FA-PREF-E2E-025-role-matrix-positif-save-cancel-view-history | Role Matrix Positif: Read + Update Menjalankan Save dan Cancel, Read dan Read Only Membuka View History, Read Only Melihat Nilai Tanpa Masking | FE+BE | 32 | 118, 119, 120, 121, 548 |
| TC-FA-PREF-E2E-026-role-matrix-negatif-tab-preferences-tidak-tersedia | Role Matrix Negatif: Tab Preferences Tidak Tersedia di Menu untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain | FE+BE | 24 | 103, 104, 105, 106, 107 |
| TC-FA-PREF-E2E-027-role-matrix-negatif-akses-url-langsung-ditolak | Role Matrix Negatif: Akses Langsung URL Preferences Ditolak untuk Update Saja, Create Saja, Delete Saja, Group Manager, dan Role Lain | FE+BE | 33 | 108, 109, 110, 111, 112 |
| TC-FA-PREF-E2E-028-role-matrix-tooltip-st-05-st-08-field-disabled-atau-terkunci | Role Matrix: Visibilitas Tooltip ST-05 dan ST-08 pada Field Disabled atau Terkunci untuk Read Only dan Read + Update | FE+BE | 26 | 51, 66, 88, 245, 246, 247 |
| TC-FA-PREF-E2E-029-gating-plan-starter-tab-preferences-tidak-terjangkau | Gating Plan Starter: Entri Accounting Disabled dengan Chip Upgrade dan Tab Preferences Tidak Terjangkau | FE+BE | 19 | 113, 114, 277, 569, 570 |
| TC-FA-PREF-E2E-030-perubahan-plan-save-ditolak-starter-dan-nilai-dipertahankan | Perubahan Plan: Request Langsung Save pada Starter Ditolak dan Nilai Preferences Dipertahankan setelah Downgrade lalu Upgrade | FE+BE | 18 | 571, 572 |
| TC-FA-PREF-E2E-031-validasi-v-01-setting-wajib-kosong | Validasi V-01 Setting Wajib Kosong: Save Menampilkan Caption dan Titik Peringatan | FE+BE | 35 | 125, 126, 127, 550 |
| TC-FA-PREF-E2E-032-validasi-v-01-first-accounting-period-bulan-kosong-dan-titik-peringatan | Validasi V-01: First Accounting Period Bulan Kosong, Caption Hilang Saat Field Terisi, dan Titik Peringatan Section | FE+BE | 25 | 130, 131, 132 |
| TC-FA-PREF-E2E-033-first-accounting-period-tahun-berjalan-dan-bulan-setelah-bulan-berjalan | First Accounting Period: Tahun Berjalan Mengosongkan Bulan Setelah Bulan Berjalan dan Bulan Setelah Bulan Berjalan Tidak Dapat Dipilih | FE+BE | 28 | 128, 129, 148, 149 |
| TC-FA-PREF-E2E-034-first-accounting-period-bulan-berjalan-dan-pv-04-mengikuti-time-zone | First Accounting Period: Bulan Berjalan dan Bulan Sebelumnya Dapat Dipilih, Jumlah Periode PV-04 Mengikuti Time Zone Entitas | FE+BE | 23 | 146, 147, 609, 610 |
| TC-FA-PREF-E2E-035-bulan-berjalan-mengikuti-time-zone-entitas-pada-pergantian-bulan | Bulan Berjalan First Accounting Period Mengikuti Time Zone Entitas (Jakarta dan Honolulu) pada Pergantian Bulan | FE+BE | 25 | 150, 151, 599, 600 |
| TC-FA-PREF-E2E-036-default-capitalization-threshold-validasi-batas-v-02-dan-v-03 | Default Capitalization Threshold: Nilai Minus, Batas 0, 16 Digit, 17 Digit, Validasi V-02 dan V-03 | FE+BE | 28 | 133, 134, 135, 136, 137 |
| TC-FA-PREF-E2E-037-default-capitalization-threshold-format-tampil-setelah-blur | Default Capitalization Threshold: Format Tampil Setelah Blur, Desimal, dan Digit Desimal Ketiga Diblok | FE+BE | 19 | 138, 139, 140, 141 |
| TC-FA-PREF-E2E-038-default-capitalization-threshold-sisa-edge-matrix | Default Capitalization Threshold sisa edge matrix: V-01, V-02, V-03, digit desimal ketiga, nilai 0, dan 16 digit dengan 2 desimal | FE+BE | 33 | 551, 552, 553, 554, 555 |
| TC-FA-PREF-E2E-039-caption-v-02-v-03-v-04-tanpa-titik-peringatan-sectioncard | Caption V-02, V-03, V-04 tidak menampilkan titik peringatan SectionCard; V-09 dan V-10 tidak menyalakan titik General | FE+BE | 28 | 615, 616, 617, 619 |
| TC-FA-PREF-E2E-040-validasi-v-04-akun-default-berubah-sesi-lain-dengan-dialog | Validasi V-04: akun Default Gain menjadi Inactive dan akun Default Loss dihapus oleh sesi lain sebelum Save (dengan dialog Save Changes) | FE+BE | 24 | 142, 143 |
| TC-FA-PREF-E2E-041-save-ditolak-akun-default-berubah-sebelum-save-versi-dialog | Save ditolak karena akun Default Gain atau Loss on Disposal berubah sebelum Save (alur Save dengan dialog D-01) | FE+BE | 24 | 214, 215 |
| TC-FA-PREF-E2E-042-save-ditolak-akun-inactive-setelah-d-01-terbuka-dan-akun-tersimpan-inactive | Save ditolak akun Inactive setelah dialog D-01 terbuka; akun tersimpan Inactive tidak memblokir Save setting lain | FE+BE | 21 | 218, 556 |
| TC-FA-PREF-E2E-043-validasi-v-09-fiscal-year-start-versi-tax-depreciation-class-alur-edit | Validasi V-09: perubahan Fiscal Year Start ditolak saat ada versi Tax Depreciation Class ber-Effective From (alur edit) | FE+BE | 33 | 152, 153, 154, 578 |
| TC-FA-PREF-E2E-044-validasi-v-09-first-accounting-period-tidak-terpengaruh-versi-tdc | Validasi V-09: hanya First Accounting Period tidak terpengaruh; versi pertama tanpa Effective From tidak menghalangi Fiscal Year Start | FE+BE | 32 | 219, 220, 579, 580 |
| TC-FA-PREF-E2E-045-validasi-v-10-first-accounting-period-transaksi-bertanggal-paling-awal | Validasi V-10: First Accounting Period terhadap transaksi bertanggal paling awal (satu bulan sebelum, sama, dan sesudah) | FE+BE | 23 | 155, 156, 157 |
| TC-FA-PREF-E2E-046-first-accounting-period-batas-transaksi-bertanggal-paling-awal-seri-pb | Save First Accounting Period terhadap transaksi bertanggal paling awal: batas satu bulan sebelum, sama, dan sesudah (seri PB) | FE+BE | 35 | 222, 223, 224, 226 |
| TC-FA-PREF-E2E-047-first-accounting-period-batas-transaksi-bertanggal-15-mei-2026-seri-pc | First Accounting Period terhadap transaksi bertanggal paling awal 15 Mei 2026: April, Mei, dan Juni (seri PC) | FE+BE | 23 | 585, 586, 587 |
| TC-FA-PREF-E2E-048-versi-tdc-dan-transaksi-bertanggal-dibuat-setelah-dialog-save-terbuka | Versi Tax Depreciation Class dan transaksi bertanggal dibuat setelah dialog D-01 terbuka menolak Save | FE+BE | 19 | 221, 225 |
| TC-FA-PREF-E2E-049-select-disposal-documents-sell-scrap-lost-hanya-required-dan-optional | Select Disposal Documents jenis Sell, Scrap, dan Lost hanya berisi Required dan Optional dan tidak dapat dikosongkan | FE+BE | 30 | 158, 159, 160 |
| TC-FA-PREF-E2E-050-select-disposal-documents-donate-trade-in-write-off-hanya-required-dan-optional | Select Disposal Documents jenis Donate, Trade-in, dan Write-off hanya berisi Required dan Optional dan tidak dapat dikosongkan | FE+BE | 30 | 161, 162, 163 |
| TC-FA-PREF-E2E-051-journal-grouping-dikosongkan-ketiga-dimensi-dan-cancel-mengembalikan-nilai-tersimpan | Journal Grouping dikosongkan, memilih ketiga dimensi, dan Cancel mengembalikan Select akun dan MultiSelect ke nilai tersimpan | FE+BE | 24 | 166, 167, 275 |
| TC-FA-PREF-E2E-052-shortcut-create-account-gain-loss-dan-akun-sama-pada-gain-dan-loss | Select akun Default Gain dan Loss: akun sama dapat dipilih pada Gain dan Loss, serta shortcut + Create account membuat akun baru yang langsung terpilih | FE+BE | 30 | 168, 169, 175 |
| TC-FA-PREF-E2E-053-opsi-select-akun-active-function-dan-urut-kode-a-z-seri-pa-dan-pc | Opsi Select akun hanya memuat akun Active sesuai function dan berurutan menurut kode A-Z (seri PA dan PC) | FE+BE | 35 | 171, 172, 173, 174, 588, 589, 590, 591 |
| TC-FA-PREF-E2E-054-save-tanpa-dialog-setting-tidak-berdampak | Save Tanpa Dialog: In-service Date Source, Default Capitalization Offset, Found Asset Credit Account, Journal Grouping | FE+BE | 36 | 176, 178, 179, 180 |
| TC-FA-PREF-E2E-055-save-disposal-documents-required-dan-toast-hilang-4-detik | Save Semua Jenis Disposal Documents Required; Toast Sukses Hilang Otomatis 4 Detik | FE+BE | 24 | 177, 182 |
| TC-FA-PREF-E2E-056-save-lima-setting-tidak-berdampak-dan-threshold-kosong-ditolak | Save Threshold Kosong Ditolak Tanpa Dialog; Save Lima Setting Tidak Berdampak Sekaligus | FE+BE | 32 | 181, 213, 584 |
| TC-FA-PREF-E2E-057-save-campuran-dan-berlaku-langsung-tanpa-approval-notifikasi | Save Campuran Setting Berdampak dan Tidak Berdampak; Save Berlaku Langsung Tanpa Approval dan Notifikasi | FE+BE | 35 | 583, 593 |
| TC-FA-PREF-E2E-058-d01-screening-dan-hitungan-pv01-asset-class-threshold-default | D-01 Screening dan Hitungan PV-01 (Asset Class Memakai Threshold Default) | FE+BE | 33 | 183, 184, 185, 186 |
| TC-FA-PREF-E2E-059-d01-pv02-akun-gain-dan-loss-default-pelepasan-belum-diposting | D-01 PV-02: Asset Class Akun Gain dan Loss Default, Pelepasan Belum Diposting | FE+BE | 32 | 187, 188, 189, 190 |
| TC-FA-PREF-E2E-060-d01-pv02-bentuk-tunggal-nol-dan-asset-class-inactive | D-01 PV-02 Bentuk Tunggal dan Nol; Asset Class Inactive Tidak Dihitung | FE+BE | 29 | 611, 612, 621 |
| TC-FA-PREF-E2E-061-d01-pv03-pelepasan-menunggu-posting | D-01 PV-03: Pelepasan Menunggu Posting (Jamak, Tunggal, Nol) | FE+BE | 24 | 191, 192, 193 |
| TC-FA-PREF-E2E-062-d01-pv04-pv05-pembangunan-ulang-periode-dan-awal-tahun-fiskal | D-01 PV-04 dan PV-05: Pembangunan Ulang Periode dan Awal Tahun Fiskal | FE+BE | 32 | 194, 195, 196, 197 |
| TC-FA-PREF-E2E-063-d01-baris-dampak-berurutan-save-dan-cancel | D-01 Baris Dampak Berurutan, Klik [Save] D-01 Menyimpan, [Cancel] D-01 | FE+BE | 29 | 198, 200, 201 |
| TC-FA-PREF-E2E-064-d01-esc-klik-luar-dialog-dan-save-campuran | D-01 Esc, Klik Luar Dialog Tidak Menutup, Save Campuran Lewat D-01 | FE+BE | 26 | 199, 202, 203 |
| TC-FA-PREF-E2E-065-save-lewat-d01-membangun-ulang-periode-dan-depreciation-in-disposal-month | Save Lewat D-01 Membangun Ulang Periode: Fiscal Year Start, First Accounting Period, Depreciation in Disposal Month | FE+BE | 34 | 207, 208, 209 |
| TC-FA-PREF-E2E-066-save-lewat-d01-default-gain-loss-dan-akun-ber-function-silang | Save Lewat D-01: Default Gain, Default Loss, Akun Ber-function Silang | FE+BE | 30 | 210, 211, 212 |
| TC-FA-PREF-E2E-067-kunci-fiscal-year-start-dan-first-accounting-period-setelah-posting-atau-periode-ditutup | Kunci Fiscal Year Start dan First Accounting Period Setelah Posting Penyusutan atau Periode Soft Closed/Closed | FE+BE | 34 | 238, 239, 240 |
| TC-FA-PREF-E2E-068-kunci-terbuka-kembali-save-fiscal-year-start-dan-kunci-aktif-setelah-muat-ulang | Kunci Terbuka Kembali Setelah Periode Dibuka Kembali; Save Fiscal Year Start Berhasil; Kunci Aktif Setelah Muat Ulang | FE+BE | 27 | 241, 242, 243, 248 |
| TC-FA-PREF-E2E-069-d03-tampil-saat-kunci-terjadi-setelah-form-dibuka | D-03 Tampil Saat Kunci Terjadi Setelah Form Dibuka (Posting Pertama, Soft Closed, Closed) | FE+BE | 33 | 251, 252, 253 |
| TC-FA-PREF-E2E-070-d03-klik-ok-klik-luar-dialog-dan-d03-menang-atas-v09-v10-v04 | D-03: Klik [OK] Memuat Ulang Form, Klik Luar Tidak Menutup, D-03 Menang atas V-09, V-10, V-04 | FE+BE | 34 | 254, 255, 256 |
| TC-FA-PREF-E2E-071-v09-v10-v04-tampil-bersamaan-saat-tidak-terkunci | V-09, V-10, V-04 Tampil Bersamaan Saat Tidak Terkunci | FE+BE | 15 | 257 |
| TC-FA-PREF-E2E-072-d03-posting-pertama-setelah-dialog-save-changes | D-03: Posting Penyusutan Pertama Setelah Dialog Save Changes Terbuka pada Fiscal Year Start dan First Accounting Period | FE+BE | 39 | 557, 558 |
| TC-FA-PREF-E2E-073-d04-tampil-saat-sidebar-back-browser-tab-chart-of-accounts-dan-cancel | D-04: Dialog Unsaved Changes Tampil Saat Sidebar, Back Browser, dan Tab Chart of Accounts dengan Form Dirty; [Cancel] Tetap pada Tab Preferences | FE+BE | 27 | 258, 259, 260, 263 |
| TC-FA-PREF-E2E-074-d04-leave-melanjutkan-perpindahan-dan-membuang-perubahan-cancel-back-browser | D-04: [Leave] Melanjutkan Perpindahan (Tab, Sidebar, Back Browser) dan Membuang Perubahan; [Cancel] pada Back Browser | FE+BE | 34 | 261, 262, 613, 614 |
| TC-FA-PREF-E2E-075-form-pristine-tidak-menampilkan-d04-perpindahan-setelah-save-atau-perubahan-dikembalikan | Form Pristine Tidak Menampilkan D-04; Perpindahan Setelah Save atau Setelah Perubahan Dikembalikan Tidak Menampilkan Dialog | FE+BE | 26 | 266, 267, 268, 269, 576 |
| TC-FA-PREF-E2E-076-muat-ulang-f5-dan-tutup-tab-konfirmasi-bawaan-browser-dan-d04 | Muat Ulang F5 dan Tutup Tab: Konfirmasi Bawaan Browser Hanya untuk Form Dirty dan Tidak Memunculkan D-04 | FE+BE | 27 | 270, 271, 272, 273, 575 |
| TC-FA-PREF-E2E-077-defense-in-depth-role-matrix-negatif-save-ditolak-read-only-read-read-create-create | Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Read Only, Manage accounting - Read, Read + Create, dan Create | FE+BE | 35 | 230, 511, 512, 513, 514 |
| TC-FA-PREF-E2E-078-defense-in-depth-role-matrix-negatif-save-ditolak-delete-update-group-manager-role-lain | Defense-in-Depth Role Matrix Negatif: Request Langsung Save Preferences Ditolak Server 403 untuk Delete saja, Update saja, Group Manager, dan Role Lain | FE+BE | 28 | 515, 516, 517, 518 |
| TC-FA-PREF-E2E-079-defense-in-depth-request-langsung-mengubah-field-terkunci-ditolak | Defense-in-Depth: Request Langsung Mengubah Fiscal Year Start dan First Accounting Period yang Terkunci Ditolak Server | FE+BE | 35 | 249, 250, 519, 520, 521 |
| TC-FA-PREF-E2E-080-defense-in-depth-first-accounting-period-di-luar-rentang-v-09-v-10-lewat-request-langsung | Defense-in-Depth: First Accounting Period di Luar Rentang, V-09 Versi Tax Depreciation Class, dan V-10 Transaksi Bertanggal Ditolak Lewat Request Langsung | FE+BE | 35 | 236, 237, 522, 523, 524, 525 |
| TC-FA-PREF-E2E-081-defense-in-depth-default-capitalization-threshold-negatif-17-digit-3-desimal-lewat-request-langsung | Defense-in-Depth: Default Capitalization Threshold Negatif, 17 Digit, dan 3 Desimal Ditolak Server Lewat Request Langsung | FE+BE | 32 | 233, 234, 235, 526, 527, 528 |
| TC-FA-PREF-E2E-082-defense-in-depth-setting-wajib-kosong-ditolak-dan-found-asset-credit-account-tanpa-filter-function-diterima | Defense-in-Depth: Setting Wajib Kosong Ditolak Server Lewat Request Langsung dan Found Asset Credit Account Active Tanpa Filter Function Diterima | FE+BE | 30 | 531, 532, 533, 534, 535, 541 |
| TC-FA-PREF-E2E-083-defense-in-depth-akun-default-tidak-ditemukan-inactive-function-salah-dan-disposal-documents-tidak-valid | Defense-in-Depth: Akun Default Tidak Ditemukan, Inactive, atau Function Salah dan Disposal Documents Tidak Valid Ditolak Server Lewat Request Langsung | FE+BE | 36 | 536, 537, 538, 539, 540, 542, 543 |
| TC-FA-PREF-E2E-084-defense-in-depth-save-langsung-tanpa-perubahan-create-dan-delete-preferences-ditolak | Defense-in-depth: Save Langsung Tanpa Perubahan Nilai Berhasil, Create dan Delete Preferences oleh User Ditolak Server | FE+BE | 29 | 232, 544, 545 |
| TC-FA-PREF-E2E-085-isolasi-tenant-tab-dan-request-langsung-hanya-berlaku-untuk-company-client-aktor | Isolasi Tenant: Tab Preferences dan Request Langsung Hanya Berlaku untuk Company Client Aktor | FE+BE | 13 | 546, 547 |
| TC-FA-PREF-E2E-086-dua-admin-menyimpan-journal-grouping-bersamaan-last-write-wins-dan-tiap-save-dicatat | Dua Admin Menyimpan Journal Grouping Bersamaan: Last-Write-Wins dan Tiap Save Dicatat | FE+BE | 22 | 287 |
| TC-FA-PREF-E2E-087-absence-log-save-tanpa-perubahan-dan-penguncian-tidak-menulis-entri-log | Absence Log: Save Tanpa Perubahan dan Penguncian Tidak Menulis Entri Log | FE+BE | 35 | 231, 244, 382, 602 |
| TC-FA-PREF-E2E-088-absence-log-save-ditolak-cancel-dialog-save-changes-dan-j-01-tanpa-aktor-tidak-menulis-log | Absence Log: Save Ditolak Server, Cancel pada Dialog Save Changes, dan J-01 Tanpa User Aktor Tidak Menulis Log | FE+BE | 42 | 386, 387, 427 |
| TC-FA-PREF-E2E-089-absence-log-cancel-mengembalikan-form-tanpa-dialog-toast-atau-log | Absence Log: Klik [Cancel] Mengembalikan Form ke Nilai Tersimpan Tanpa Dialog, Toast, atau Log | FE+BE | 26 | 274, 577 |
| TC-FA-PREF-E2E-090-state-tenant-suspended-dan-expired-save-ditolak-toast-baku-tab-tetap-dapat-dibaca | State Tenant Suspended dan Expired: Save Ditolak dengan Toast Baku dan Tab Preferences Tetap Dapat Dibaca | FE+BE | 35 | 227, 228, 563, 566 |
| TC-FA-PREF-E2E-091-state-tenant-suspended-dan-expired-baca-preferences-dan-changelog-tetap-tersedia-request-langsung-save-403 | State Tenant Suspended dan Expired: Baca Preferences dan Changelog Tetap Tersedia, Request Langsung Save Ditolak 403 | FE+BE | 33 | 564, 565, 567, 568 |
| TC-FA-PREF-E2E-092-resilience-save-5xx-form-dan-dialog-tetap-terbuka-input-dipertahankan-toast-gagal-retry-berhasil | Resilience Save 5xx: Form dan Dialog D-01 Tetap Terbuka, Input Dipertahankan, Toast Gagal Tampil, Retry Berhasil | FE+BE | 34 | 278, 279, 282 |
| TC-FA-PREF-E2E-093-resilience-save-timeout-input-dipertahankan-tombol-enabled-toast-connection-problem | Resilience Save Timeout: Input Dipertahankan, Tombol Enabled, Toast Connection Problem | FE+BE | 41 | 280, 281, 574 |
| TC-FA-PREF-E2E-094-resilience-pembangunan-ulang-periode-gagal-penulisan-log-gagal-dan-save-d-01-5xx-membatalkan-save | Resilience: Pembangunan Ulang Periode Gagal, Penulisan Log Gagal, dan Save Dialog Save Changes 5xx Membatalkan Save | FE+BE | 41 | 288, 392, 573 |
| TC-FA-PREF-E2E-095-resilience-errorstate-pemuatan-form-dan-pratinjau-d-01-gagal-try-again-memuat-ulang | Resilience ErrorState: Pemuatan Form dan Pratinjau D-01 Gagal, Try Again Memuat Ulang | FE+BE | 30 | 74, 75, 205, 206 |
| TC-FA-PREF-E2E-096-resilience-errorstate-modal-changelog-download-gagal-tombol-save-d-01-saat-hitungan-gagal-dan-konsumen-gagal-membaca-preferences | Resilience ErrorState: Modal Changelog Gagal, Download Gagal, Tombol Save D-01 saat Hitungan Gagal, dan Konsumen Gagal Membaca Preferences | FE+BE | 28 | 296, 361, 598, 508 |
| TC-FA-PREF-E2E-097-modal-changelog-screening-isi-9-baris-contoh-dan-hover-modified-by | Modal Changelog: Screening, Isi 9 Baris Contoh, dan Hover Modified By | FE+BE | 32 | 289, 290, 291 |
| TC-FA-PREF-E2E-098-modal-changelog-urutan-default-date-newest-first-nilai-kosong-tanda-strip-tutup-modal-dan-empty-state | Modal Changelog: Urutan Default Date Newest First, Nilai Kosong Tanda Strip, Tutup Lewat X, Esc, Klik Luar, dan Empty State | FE+BE | 24 | 27, 28, 292, 293, 294, 297 |
| TC-FA-PREF-E2E-099-changelog-search-siklus-interaksi-dan-kecocokan-sebagian-pada-enam-kolom | Changelog Search: Siklus Interaksi, Kecocokan Sebagian pada Enam Kolom Searchable | FE+BE | 23 | 298, 299 |
| TC-FA-PREF-E2E-100-changelog-search-case-insensitive-enam-kolom-kolom-date-tidak-dicari-dan-tanpa-hasil | Changelog Search: Case-Insensitive pada Enam Kolom, Kolom Date Tidak Dicari, dan Tanpa Hasil | FE+BE | 12 | 300, 301, 302 |
| TC-FA-PREF-E2E-101-changelog-search-kolom-tersembunyi-trim-spasi-serta-kombinasi-search-dan-filter | Changelog Search: Kolom Tersembunyi Tidak Dicari, Trim Spasi, serta Kombinasi Search dan Filter | FE+BE | 34 | 303, 304, 318, 319 |
| TC-FA-PREF-E2E-102-changelog-filter-panel-screening-sumber-opsi-dan-filter-satu-opsi | Changelog Filter Panel: screening, sumber opsi dropdown, filter satu opsi pada empat dropdown | FE+BE | 35 | 305, 306, 307 |
| TC-FA-PREF-E2E-103-changelog-filter-logika-or-dan-and-rentang-date-inklusif-dan-filter-section | Changelog Filter: logika OR dalam dropdown, AND antar dropdown, rentang Date inklusif, filter Section menyaring baris tanpa Section | FE+BE | 30 | 308, 309, 310, 311 |
| TC-FA-PREF-E2E-104-changelog-filter-kotak-cari-dropdown-chip-uncheck-dan-tutup-panel-tanpa-apply | Changelog Filter: kotak cari di dropdown, hapus chip, uncheck opsi, tutup panel tanpa Apply | FE+BE | 31 | 312, 313, 314, 315 |
| TC-FA-PREF-E2E-105-changelog-filter-titik-indikator-kolom-tersembunyi-dan-clear-field-tidak-mereset-search-sort | Changelog Filter: titik indikator ikon Filter, filter pada kolom tersembunyi, Clear Field tidak mereset Search dan Sort | FE+BE | 29 | 316, 317, 320 |
| TC-FA-PREF-E2E-106-changelog-mengosongkan-search-tidak-mereset-filter-dan-hasil-kosong-pulih | Changelog: mengosongkan Search tidak mereset Filter dan Sort, hasil kosong dari Search dan Filter pulih saat salah satu dilepas | FE+BE | 14 | 321, 322 |
| TC-FA-PREF-E2E-107-changelog-sort-default-siklus-tiga-state-date-dan-kolom-teks-kolom-actions-tanpa-sort | Changelog Sort: urutan bawaan Date Newest First, siklus tiga state kolom Date dan kolom teks, kolom Actions tanpa sort | FE+BE | 34 | 323, 324, 325, 331 |
| TC-FA-PREF-E2E-108-changelog-sort-old-value-new-value-modified-by-dan-pindah-kolom-sort-tidak-mereset-search-filter | Changelog Sort: Old Value, New Value, Modified By, dan berpindah kolom sort tidak mereset Search dan Filter | FE+BE | 30 | 327, 328, 329, 330 |
| TC-FA-PREF-E2E-109-changelog-column-visibility-dan-screening-setup-column | Changelog Column Visibility dan screening modal Setup Column | FE+BE | 25 | 332, 333, 334 |
| TC-FA-PREF-E2E-110-changelog-setup-column-hapus-centang-dan-centang-kembali-tujuh-kolom | Changelog Setup Column: hapus centang lalu centang kembali tujuh kolom | FE+BE | 9 | 335 |
| TC-FA-PREF-E2E-111-changelog-setup-column-geser-tujuh-kolom-reset-to-default-dan-tutup-lewat-x-tanpa-save | Changelog Setup Column: geser tujuh kolom, Reset to Default, tutup lewat ✕ tanpa Save | FE+BE | 29 | 336, 338, 339 |
| TC-FA-PREF-E2E-112-changelog-setup-column-tutup-lewat-esc-dan-kolom-terakhir-tidak-dapat-dihapus-centangnya | Changelog Setup Column: tutup lewat Esc membuang perubahan, kolom terakhir tidak dapat dihapus centangnya | FE+BE | 15 | 340, 341 |
| TC-FA-PREF-E2E-113-changelog-paginasi-105-entri-ukuran-halaman-dan-input-nomor-halaman | Changelog paginasi 105 entri: ukuran halaman dan input nomor halaman | FE+BE | 27 | 342, 343, 344, 345, 346 |
| TC-FA-PREF-E2E-114-changelog-paginasi-105-entri-search-filter-sort-dan-paginasi-saling-mempengaruhi | Changelog paginasi 105 entri: Search, Filter, Sort, dan paginasi saling mempengaruhi | FE+BE | 24 | 347, 348, 349 |
| TC-FA-PREF-E2E-115-changelog-download-menu-format-csv-xlsx-dan-mengikuti-filter | Changelog Download: menu pilihan format, berkas CSV, berkas XLSX, dan mengikuti Filter | FE+BE | 26 | 350, 351, 352, 353 |
| TC-FA-PREF-E2E-116-changelog-download-mengikuti-search-kolom-tersembunyi-dan-hasil-kosong | Changelog Download: mengikuti Search, tidak memuat kolom tersembunyi, memuat kembali kolom yang ditampilkan, hasil Search kosong | FE+BE | 31 | 354, 356, 357, 358 |
| TC-FA-PREF-E2E-117-changelog-download-isi-berkas-isi-sel-urutan-baris-dan-105-baris | Changelog Download isi berkas: isi sel, urutan baris mengikuti Sort, dan 105 baris | FE+BE | 22 | 355, 359, 360 |
| TC-FA-PREF-E2E-118-log-tiga-surface-save-fiscal-year-start-dan-first-accounting-period | Log tiga surface: Save perubahan Fiscal Year Start dan First Accounting Period tercatat di Changelog, System Log, dan Activity Log | FE+BE | 46 | 362, 363 |
| TC-FA-PREF-E2E-119-log-tiga-surface-save-default-capitalization-threshold-dan-in-service-date-source | Log tiga surface: Save perubahan Default Capitalization Threshold dan In-service Date Source tercatat di Changelog, System Log, dan Activity Log | FE+BE | 43 | 364, 365 |
| TC-FA-PREF-E2E-120-log-tiga-surface-save-depreciation-in-disposal-month-dan-default-gain-on-disposal | Log tiga surface: Save perubahan Depreciation in Disposal Month dan Default Gain on Disposal tercatat di Changelog, System Log, dan Activity Log | FE+BE | 46 | 366, 367 |
| TC-FA-PREF-E2E-121-log-tiga-surface-save-default-loss-dan-disposal-documents-sell | Log Tiga Surface: Save Default Loss on Disposal dan Disposal Documents Sell | FE+BE | 38 | 368, 369 |
| TC-FA-PREF-E2E-122-log-tiga-surface-disposal-documents-scrap-lost-donate | Log Tiga Surface: Disposal Documents Scrap, Lost, dan Donate | FE+BE | 54 | 370, 371, 372 |
| TC-FA-PREF-E2E-123-log-tiga-surface-disposal-documents-trade-in-write-off-dan-default-capitalization-offset | Log Tiga Surface: Disposal Documents Trade-in, Write-off, dan Default Capitalization Offset | FE+BE | 54 | 373, 374, 375 |
| TC-FA-PREF-E2E-124-log-tiga-surface-found-asset-credit-account-journal-grouping-dan-urutan-tetap-journal-grouping | Log Tiga Surface: Found Asset Credit Account, Journal Grouping, dan Urutan Tetap Journal Grouping | FE+BE | 46 | 376, 377, 388 |
| TC-FA-PREF-E2E-125-log-save-dua-field-sekaligus-menulis-dua-baris-log | Log: Save Dua Field Sekaligus Menulis Dua Baris Log di Tiga Surface | FE+BE | 43 | 378, 379 |
| TC-FA-PREF-E2E-126-log-field-tidak-berubah-tidak-menulis-baris-dan-entri-lama-tidak-berubah | Log: Field Tidak Berubah Tidak Menulis Baris dan Entri Changelog Lama Tidak Berubah | FE+BE | 43 | 380, 381 |
| TC-FA-PREF-E2E-127-log-modified-by-pelaku-read-update-kolom-system-log-dan-activity-log | Log: Kolom System Log dan Activity Log serta Modified By Pelaku Manage accounting - Read + Update | FE+BE | 41 | 383, 384, 385 |
| TC-FA-PREF-E2E-128-log-journal-grouping-kosong-dan-nominal-threshold-desimal | Log: Journal Grouping Dikosongkan atau Diisi dari Kosong dan Nominal Threshold Desimal | FE+BE | 48 | 389, 390, 391 |
| TC-FA-PREF-E2E-129-log-request-api-langsung-oleh-pemanggil-terotorisasi-menulis-log-l-02-di-tiga-surface | Log: Request API Langsung oleh Pemanggil Terotorisasi Menulis Log L-02 di Tiga Surface | FE+BE | 17 | 549 |
| TC-FA-PREF-E2E-130-sinkronisasi-asset-class-dan-tax-depreciation-class-threshold-dan-awal-tahun-pajak | Sinkronisasi ke Asset Class dan Tax Depreciation Class: Threshold dan Awal Tahun Pajak | FE+BE | 35 | 393, 396, 409 |
| TC-FA-PREF-E2E-131-sinkronisasi-accounting-period-save-fiscal-year-start-dan-first-accounting-period-membangun-ulang-periode | Sinkronisasi ke Accounting Period: Save Fiscal Year Start dan First Accounting Period Membangun Ulang Periode | FE+BE | 21 | 394, 395 |
| TC-FA-PREF-E2E-132-sinkronisasi-chart-of-accounts-nama-akun-inactive-dan-function-berubah | Sinkronisasi Chart of Accounts: Nama Akun, Akun Inactive, dan Function Akun Berubah pada Select Akun Preferences | FE+BE | 32 | 401, 402, 403, 405 |
| TC-FA-PREF-E2E-133-sinkronisasi-akun-default-tidak-dapat-dihapus-riwayat-log-tidak-berubah-mata-uang-dan-format-tanggal-changelog | Sinkronisasi: Akun Default Tidak Dapat Dihapus, Riwayat Log Tidak Berubah, Mata Uang, dan Format Tanggal Changelog | FE+BE | 35 | 404, 406, 407, 408 |
| TC-FA-PREF-E2E-134-deferred-aktivasi-pertama-modul-akuntansi-membuat-preferences-periode-awal-changelog-tanpa-offset | [DEFERRED] Aktivasi Pertama Modul Akuntansi Membuat Preferences, Periode Awal, dan Changelog tanpa Offset | FE+BE | 36 | 411, 412, 413, 414, 415 |
| TC-FA-PREF-E2E-135-deferred-upgrade-paket-aktivasi-ulang-dan-aktivasi-yang-gagal | [DEFERRED] Upgrade Paket, Aktivasi Ulang, dan Aktivasi yang Gagal | FE+BE | 28 | 416, 417, 418 |
| TC-FA-PREF-E2E-136-deferred-aktivasi-dan-j-01-pada-entitas-suspended-dan-expired | [DEFERRED] Aktivasi dan Job J-01 pada Entitas Suspended dan Expired | FE+BE | 31 | 419, 420, 429, 430 |
| TC-FA-PREF-E2E-137-deferred-rekonsiliasi-j-01-membuat-preferences-periode-paling-awal-dan-field-terkunci | [DEFERRED] Rekonsiliasi J-01: Membuat Preferences, Periode Paling Awal sebagai First Accounting Period, dan Field Terkunci | FE+BE | 35 | 421, 422, 423, 424 |
| TC-FA-PREF-E2E-138-deferred-j-01-changelog-dan-activity-log-dengan-modified-by-system-dan-retry-putaran-berikutnya | [DEFERRED] J-01: Changelog dan Activity Log dengan Modified By System serta Retry pada Putaran Berikutnya | FE+BE | 26 | 425, 426, 428 |
| TC-FA-PREF-E2E-139-deferred-in-service-date-source-activation-date-dan-manual-by-accounting | [DEFERRED] In-service Date Source: Activation Date dan Manual by Accounting | FE+BE | 31 | 431, 432, 433, 434, 440 |
| TC-FA-PREF-E2E-140-deferred-in-service-date-source-aset-terdaftar-sebelum-tepat-dan-setelah-waktu-save | [DEFERRED] Perubahan In-service Date Source terhadap aset terdaftar sebelum, tepat, dan setelah waktu Save | FE+BE | 28 | 435, 436, 437 |
| TC-FA-PREF-E2E-141-deferred-depreciation-in-disposal-month-aset-dijual-15-agustus-dan-perubahan-setting | [DEFERRED] Depreciation in Disposal Month pada aset dijual 15 Agustus dan perubahan setting terhadap pelepasan terposting | FE+BE | 26 | 441, 442, 443, 444 |
| TC-FA-PREF-E2E-142-deferred-akun-gain-dan-loss-default-pada-asset-class-dan-jurnal-pelepasan | [DEFERRED] Akun Gain dan Loss default pada Asset Class dan jurnal pelepasan | FE+BE | 35 | 445, 446, 447, 448, 453 |
| TC-FA-PREF-E2E-143-deferred-jurnal-pelepasan-ditahan-saat-akun-kosong-gain-loss-donate-dan-trade-in | [DEFERRED] Jurnal pelepasan ditahan saat akun kosong (Gain, Loss, Donate, Trade-in) | FE+BE | 25 | 449, 450, 451, 452 |
| TC-FA-PREF-E2E-144-deferred-jurnal-ditahan-dapat-diekspor-dan-pelepasan-belum-diposting-memakai-akun-default-baru | [DEFERRED] Jurnal ditahan dapat diekspor setelah akun diisi dan pelepasan belum diposting memakai akun default baru | FE+BE | 23 | 454, 455 |
| TC-FA-PREF-E2E-145-deferred-disposal-documents-field-dokumen-dan-submit-ditolak-saat-required | [DEFERRED] Disposal Documents: field dokumen dan Submit ditolak saat Required | FE+BE | 14 | 458, 459, 460, 461, 462, 463, 464, 465 |
| TC-FA-PREF-E2E-146-deferred-disposal-documents-submit-saat-optional-tidak-memblokir-posting-dan-transaksi-sebelum-sesudah-save | [DEFERRED] Disposal Documents: Submit saat Optional, tidak memblokir posting, transaksi sebelum dan sesudah Save | FE+BE | 32 | 466, 467, 468, 469, 470 |
| TC-FA-PREF-E2E-147-deferred-default-capitalization-offset-prompt-kapitalisasi-pertama-pengisian-dan-log-l-03 | [DEFERRED] Default Capitalization Offset: prompt kapitalisasi pertama, pengisian, dan log L-03 | FE+BE | 37 | 471, 472, 473, 474, 475 |
| TC-FA-PREF-E2E-148-deferred-default-capitalization-offset-kapitalisasi-berikutnya-akun-tidak-valid-dan-prompt-ditutup | [DEFERRED] Default Capitalization Offset: kapitalisasi berikutnya, akun tidak valid, dan prompt ditutup | FE+BE | 32 | 476, 477, 478, 479, 480 |
| TC-FA-PREF-E2E-149-deferred-default-capitalization-offset-dikosongkan-perubahan-dipakai-gagal-dan-pembelian-di-bawah-threshold | [DEFERRED] Default Capitalization Offset: dikosongkan kembali, perubahan dipakai, kapitalisasi gagal, dan pembelian di bawah threshold | FE+BE | 36 | 481, 482, 483, 605 |
| TC-FA-PREF-E2E-150-deferred-found-asset-credit-account-pada-jurnal-aset-temuan | [DEFERRED] Found Asset Credit Account pada jurnal aset temuan | FE+BE | 29 | 484, 485, 486, 487 |
| TC-FA-PREF-E2E-151-deferred-export-journal-jumlah-baris-menurut-journal-grouping-dan-group-assignable | [DEFERRED] Export Journal: jumlah baris menurut Journal Grouping dan Group Assignable | FE+BE | 28 | 488, 489, 490, 491, 492 |
| TC-FA-PREF-E2E-152-deferred-export-journal-isi-berkas-sheet-header-kolom-tipe-sel-dimensi-tanggal-dan-description | [DEFERRED] Export Journal isi berkas (1): sheet, header, kolom, tipe sel, dimensi, tanggal, dan Description | FE+BE | 14 | 493, 494, 495, 496, 497, 498 |
| TC-FA-PREF-E2E-153-deferred-export-journal-isi-berkas-debit-credit-transaksi-transaction-number-account-code-dan-tanpa-dimensi | [DEFERRED] Export Journal isi berkas (2): Debit dan Credit, minimal 2 baris, Transaction Number, Account Code, dan tanpa dimensi | FE+BE | 14 | 499, 500, 501, 502, 503 |
| TC-FA-PREF-E2E-154-deferred-konsumen-depreciation-run-dan-export-journal-setup-incomplete-pembacaan-preferences-dan-label-tahun-fiskal | [DEFERRED] Konsumen: Depreciation Run dan Export Journal terblokir saat Setup Incomplete, pembacaan Preferences, dan label tahun fiskal | FE+BE | 34 | 504, 505, 506, 507, 509, 510 |
| TC-FA-PREF-E2E-155-status-tombol-save-changes-dan-cancel-pada-form-pristine-dan-berubah | Status Tombol [Save changes] dan [Cancel]: Disabled pada Form Pristine, Enabled saat Berubah, Kembali Disabled saat Dikembalikan | FE+BE | 19 | 18, 19, 20 |
| TC-FA-PREF-E2E-157-shimmer-pratinjau-d01-save-tetap-enabled | Shimmer pratinjau dampak dialog D-01: tombol Save tetap Enabled saat hitungan dimuat | FE+BE | 19 | 204, 597 |
| TC-FA-PREF-E2E-158-klik-ganda-cepat-save-changes-dan-save-d01 | Klik ganda cepat pada [Save changes] dan [Save] di D-01 hanya mengirim satu permintaan Save | FE+BE | 28 | 285, 286 |
| TC-FA-PREF-E2E-159-gating-plan-growth-professional-enterprise-tab-preferences-tersedia | Gating Plan: Growth, Professional, dan Enterprise Memiliki Tab Preferences dengan Akses Penuh | FE+BE | 25 | 115, 116, 117 |
| TC-FA-PREF-E2E-160-select-setting-wajib-tanpa-kontrol-pengosongan | Select Setting Wajib Tidak Menyediakan Kontrol atau Opsi Kosong untuk Mengosongkan Nilainya | FE+BE | 26 | 618 |
| TC-FA-PREF-E2E-161-validasi-v-04-akun-default-berubah-sesi-lain-tanpa-dialog | Validasi V-04: function Default Capitalization Offset berubah dan Found Asset Credit Account menjadi Inactive oleh sesi lain sebelum Save (tanpa dialog) | FE+BE | 20 | 144, 145 |
| TC-FA-PREF-E2E-162-select-offset-dan-found-asset-tanpa-shortcut-dan-save-akun-gabungan-gain-loss | Select Default Capitalization Offset dan Found Asset Credit Account tanpa shortcut Create account, dan akun gabungan Gain dan Loss disimpan lewat dialog | FE+BE | 21 | 170, 592 |
| TC-FA-PREF-E2E-163-periode-dibuka-kembali-kunci-terbuka-atau-tetap-terkunci | Periode yang Dibuka Kembali: Kunci Terbuka Tanpa Posting Penyusutan dan Tetap Terkunci Bila Posting Sudah Ada | FE+BE | 14 | 603, 604 |
| TC-FA-PREF-E2E-164-save-fiscal-year-start-ditolak-d03-saat-soft-closed-muncul-di-d01 | Save Fiscal Year Start Ditolak D-03 Saat Periode Soft Closed Muncul Setelah D-01 Terbuka | FE+BE | 25 | 559 |
| TC-FA-PREF-E2E-165-d04-tombol-esc-setara-cancel-dan-klik-di-luar-dialog-tidak-menutup | D-04: Tombol Esc Setara [Cancel] dan Klik Area di Luar Dialog Tidak Menutup Dialog | FE+BE | 12 | 264, 265 |
| TC-FA-PREF-E2E-166-defense-in-depth-default-capitalization-threshold-teks-atau-script-lewat-request-langsung | Defense-in-Depth: Default Capitalization Threshold Berisi Teks atau Script Ditolak Server dan Tidak Tercatat di Changelog | FE+BE | 23 | 529, 530 |
| TC-FA-PREF-E2E-167-defense-in-depth-company-tanpa-baris-preferences-ditolak-server-forbidden | Defense-in-depth: Company Tanpa Baris Preferences Ditolak Server dengan Forbidden pada Request Langsung dan Pembukaan Tab | FE+BE | 9 | 276, 562 |
| TC-FA-PREF-E2E-168-dua-admin-menyimpan-default-capitalization-threshold-bersamaan-last-write-wins-dan-tiap-save-dicatat | Dua Admin Menyimpan Default Capitalization Threshold Bersamaan: Last-Write-Wins dan Tiap Save Dicatat | FE+BE | 21 | 560 |
| TC-FA-PREF-E2E-169-changelog-setup-column-pin-dan-unpin-tujuh-kolom | Changelog Setup Column: Pin dan unpin tujuh kolom | FE+BE | 12 | 337 |
| TC-FA-PREF-E2E-171-sinkronisasi-save-preferences-tidak-mengubah-data-asset-class-dan-periode-diposting | Sinkronisasi: Save Preferences Tidak Mengubah Data Asset Class dan Periode yang Sudah Diposting | FE+BE | 14 | 410 |
| TC-FA-PREF-E2E-173-deferred-in-service-date-source-aset-berpindah-ke-active-setelah-save | [DEFERRED] In-service Date Source: aset yang berpindah ke Active setelah Save memakai sumber menurut waktu pendaftaran | FE+BE | 23 | 438, 439 |
| TC-FA-PREF-E2E-174-deferred-jurnal-pelepasan-terposting-belum-dan-sudah-diekspor-saat-akun-default-diganti | [DEFERRED] Jurnal pelepasan terposting: belum diekspor memakai akun yang berlaku saat ekspor, sudah diekspor tidak berubah | FE+BE | 23 | 456, 457 |
| TC-FA-PREF-E2E-175-save-ditolak-akun-capitalization-offset-dan-found-asset-credit-berubah-sebelum-save-tanpa-dialog | Save ditolak karena akun Default Capitalization Offset atau Found Asset Credit Account berubah sebelum Save (alur Save tanpa dialog) | FE+BE | 18 | 216, 217 |
| TC-FA-PREF-E2E-176-versi-tdc-dan-transaksi-bertanggal-dibuat-saat-dialog-save-changes-terbuka-menolak-save | Versi Tax Depreciation Class dan transaksi bertanggal dibuat saat dialog Save Changes terbuka menolak Save | FE+BE | 21 | 581, 582 |

## Pembagian TC lintas spec

Nomor cadangan terpakai (17): 155, 157-169, 171, 173, 174. Beberapa TC pindah dari spec rencana ke nomor cadangan supaya spec tidak melewati ~35 langkah: TC 115-117 ke 159, TC 618 ke 160, TC 170 dan 592 ke 162, TC 603-604 ke 163, TC 559 ke 164, TC 264-265 ke 165, TC 529-530 ke 166, TC 276 dan 562 ke 167, TC 560 ke 168, TC 337 ke 169, TC 410 ke 171, TC 438-439 ke 173, TC 456-457 ke 174, TC 216-217 ke 175, TC 581-582 ke 176. TC 541 pindah dari 083 ke 082. Tabel di atas dan "Lapisan per TC" mengikuti `sourceTc` spec.

## Kebutuhan lingkungan (tim FE)

Kebutuhan data, akun, env var password, fixture BE, kendali jam (28 Oktober 2026) dan modul pemilik/konsumen tertulis di `## Prerequisites` tiap spec dan `suite.md`. Env var password belum terdaftar di `spectra.config.ts` dan `.env.example`. `fixtures/settings-accounting-preferences.json` belum ada. Spec 012 dan 013 (TC Android) memakai `coverage.mobile` saja.

## Temuan yang masih terbuka

Temuan sumber TC per spec ada di bagian "Temuan untuk QA" pada `## Notes` tiap spec. Keputusan terbuka dicatat di `work-items/settings-accounting-preferences/progress-e2e-generate-spec.md`.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-PREF-1 | TC-FA-PREF-E2E-001 | FE+BE |
| TC-FA-PREF-2 | TC-FA-PREF-E2E-021 | FE+BE |
| TC-FA-PREF-3 | TC-FA-PREF-E2E-001 | FE+BE |
| TC-FA-PREF-4 | TC-FA-PREF-E2E-001 | FE+BE |
| TC-FA-PREF-5 | TC-FA-PREF-E2E-001 | FE+BE |
| TC-FA-PREF-6 | TC-FA-PREF-E2E-002 | FE+BE |
| TC-FA-PREF-7 | TC-FA-PREF-E2E-002 | FE+BE |
| TC-FA-PREF-8 | TC-FA-PREF-E2E-002 | FE+BE |
| TC-FA-PREF-9 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-10 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-11 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-12 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-13 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-14 | TC-FA-PREF-E2E-003 | FE+BE |
| TC-FA-PREF-15 | TC-FA-PREF-E2E-004 | FE+BE |
| TC-FA-PREF-16 | TC-FA-PREF-E2E-004 | FE+BE |
| TC-FA-PREF-17 | TC-FA-PREF-E2E-004 | FE+BE |
| TC-FA-PREF-18 | TC-FA-PREF-E2E-155 | FE+BE |
| TC-FA-PREF-19 | TC-FA-PREF-E2E-155 | FE+BE |
| TC-FA-PREF-20 | TC-FA-PREF-E2E-155 | FE+BE |
| TC-FA-PREF-21 | TC-FA-PREF-E2E-002 | FE+BE |
| TC-FA-PREF-22 | TC-FA-PREF-E2E-002 | FE+BE |
| TC-FA-PREF-23 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-24 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-25 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-26 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-27 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-28 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-29 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-30 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-31 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-32 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-33 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-34 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-35 | TC-FA-PREF-E2E-006 | FE+BE |
| TC-FA-PREF-36 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-37 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-38 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-39 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-40 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-41 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-42 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-43 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-44 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-45 | TC-FA-PREF-E2E-008 | FE+BE |
| TC-FA-PREF-46 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-47 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-48 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-49 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-50 | TC-FA-PREF-E2E-007 | FE+BE |
| TC-FA-PREF-51 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-52 | TC-FA-PREF-E2E-009 | FE+BE |
| TC-FA-PREF-53 | TC-FA-PREF-E2E-009 | FE+BE |
| TC-FA-PREF-54 | TC-FA-PREF-E2E-009 | FE+BE |
| TC-FA-PREF-55 | TC-FA-PREF-E2E-009 | FE+BE |
| TC-FA-PREF-56 | TC-FA-PREF-E2E-010 | FE+BE |
| TC-FA-PREF-57 | TC-FA-PREF-E2E-010 | FE+BE |
| TC-FA-PREF-58 | TC-FA-PREF-E2E-010 | FE+BE |
| TC-FA-PREF-59 | TC-FA-PREF-E2E-010 | FE+BE |
| TC-FA-PREF-60 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-61 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-62 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-63 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-64 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-65 | TC-FA-PREF-E2E-011 | FE+BE |
| TC-FA-PREF-66 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-67 | TC-FA-PREF-E2E-004 | FE+BE |
| TC-FA-PREF-68 | TC-FA-PREF-E2E-012 | FE+BE |
| TC-FA-PREF-69 | TC-FA-PREF-E2E-012 | FE+BE |
| TC-FA-PREF-70 | TC-FA-PREF-E2E-012 | FE+BE |
| TC-FA-PREF-71 | TC-FA-PREF-E2E-012 | FE+BE |
| TC-FA-PREF-72 | TC-FA-PREF-E2E-013 | FE+BE |
| TC-FA-PREF-73 | TC-FA-PREF-E2E-014 | FE+BE |
| TC-FA-PREF-74 | TC-FA-PREF-E2E-095 | FE+BE |
| TC-FA-PREF-75 | TC-FA-PREF-E2E-095 | FE+BE |
| TC-FA-PREF-76 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-77 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-78 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-79 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-80 | TC-FA-PREF-E2E-016 | FE+BE |
| TC-FA-PREF-81 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-82 | TC-FA-PREF-E2E-015 | FE+BE |
| TC-FA-PREF-83 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-84 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-85 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-86 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-87 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-88 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-89 | TC-FA-PREF-E2E-019 | FE+BE |
| TC-FA-PREF-90 | TC-FA-PREF-E2E-020 | FE+BE |
| TC-FA-PREF-91 | TC-FA-PREF-E2E-018 | FE+BE |
| TC-FA-PREF-92 | TC-FA-PREF-E2E-018 | FE+BE |
| TC-FA-PREF-93 | TC-FA-PREF-E2E-018 | FE+BE |
| TC-FA-PREF-94 | TC-FA-PREF-E2E-018 | FE+BE |
| TC-FA-PREF-95 | TC-FA-PREF-E2E-018 | FE+BE |
| TC-FA-PREF-96 | TC-FA-PREF-E2E-022 | FE+BE |
| TC-FA-PREF-97 | TC-FA-PREF-E2E-022 | FE+BE |
| TC-FA-PREF-98 | TC-FA-PREF-E2E-022 | FE+BE |
| TC-FA-PREF-99 | TC-FA-PREF-E2E-023 | FE+BE |
| TC-FA-PREF-100 | TC-FA-PREF-E2E-023 | FE+BE |
| TC-FA-PREF-101 | TC-FA-PREF-E2E-024 | FE+BE |
| TC-FA-PREF-102 | TC-FA-PREF-E2E-024 | FE+BE |
| TC-FA-PREF-103 | TC-FA-PREF-E2E-026 | FE+BE |
| TC-FA-PREF-104 | TC-FA-PREF-E2E-026 | FE+BE |
| TC-FA-PREF-105 | TC-FA-PREF-E2E-026 | FE+BE |
| TC-FA-PREF-106 | TC-FA-PREF-E2E-026 | FE+BE |
| TC-FA-PREF-107 | TC-FA-PREF-E2E-026 | FE+BE |
| TC-FA-PREF-108 | TC-FA-PREF-E2E-027 | FE+BE |
| TC-FA-PREF-109 | TC-FA-PREF-E2E-027 | FE+BE |
| TC-FA-PREF-110 | TC-FA-PREF-E2E-027 | FE+BE |
| TC-FA-PREF-111 | TC-FA-PREF-E2E-027 | FE+BE |
| TC-FA-PREF-112 | TC-FA-PREF-E2E-027 | FE+BE |
| TC-FA-PREF-113 | TC-FA-PREF-E2E-029 | FE+BE |
| TC-FA-PREF-114 | TC-FA-PREF-E2E-029 | FE+BE |
| TC-FA-PREF-115 | TC-FA-PREF-E2E-159 | FE+BE |
| TC-FA-PREF-116 | TC-FA-PREF-E2E-159 | FE+BE |
| TC-FA-PREF-117 | TC-FA-PREF-E2E-159 | FE+BE |
| TC-FA-PREF-118 | TC-FA-PREF-E2E-025 | FE+BE |
| TC-FA-PREF-119 | TC-FA-PREF-E2E-025 | FE+BE |
| TC-FA-PREF-120 | TC-FA-PREF-E2E-025 | FE+BE |
| TC-FA-PREF-121 | TC-FA-PREF-E2E-025 | FE+BE |
| TC-FA-PREF-122 | TC-FA-PREF-E2E-024 | FE+BE |
| TC-FA-PREF-123 | TC-FA-PREF-E2E-024 | FE+BE |
| TC-FA-PREF-124 | TC-FA-PREF-E2E-017 | FE+BE |
| TC-FA-PREF-125 | TC-FA-PREF-E2E-031 | FE+BE |
| TC-FA-PREF-126 | TC-FA-PREF-E2E-031 | FE+BE |
| TC-FA-PREF-127 | TC-FA-PREF-E2E-031 | FE+BE |
| TC-FA-PREF-128 | TC-FA-PREF-E2E-033 | FE+BE |
| TC-FA-PREF-129 | TC-FA-PREF-E2E-033 | FE+BE |
| TC-FA-PREF-130 | TC-FA-PREF-E2E-032 | FE+BE |
| TC-FA-PREF-131 | TC-FA-PREF-E2E-032 | FE+BE |
| TC-FA-PREF-132 | TC-FA-PREF-E2E-032 | FE+BE |
| TC-FA-PREF-133 | TC-FA-PREF-E2E-036 | FE+BE |
| TC-FA-PREF-134 | TC-FA-PREF-E2E-036 | FE+BE |
| TC-FA-PREF-135 | TC-FA-PREF-E2E-036 | FE+BE |
| TC-FA-PREF-136 | TC-FA-PREF-E2E-036 | FE+BE |
| TC-FA-PREF-137 | TC-FA-PREF-E2E-036 | FE+BE |
| TC-FA-PREF-138 | TC-FA-PREF-E2E-037 | FE+BE |
| TC-FA-PREF-139 | TC-FA-PREF-E2E-037 | FE+BE |
| TC-FA-PREF-140 | TC-FA-PREF-E2E-037 | FE+BE |
| TC-FA-PREF-141 | TC-FA-PREF-E2E-037 | FE+BE |
| TC-FA-PREF-142 | TC-FA-PREF-E2E-040 | FE+BE |
| TC-FA-PREF-143 | TC-FA-PREF-E2E-040 | FE+BE |
| TC-FA-PREF-144 | TC-FA-PREF-E2E-161 | FE+BE |
| TC-FA-PREF-145 | TC-FA-PREF-E2E-161 | FE+BE |
| TC-FA-PREF-146 | TC-FA-PREF-E2E-034 | FE+BE |
| TC-FA-PREF-147 | TC-FA-PREF-E2E-034 | FE+BE |
| TC-FA-PREF-148 | TC-FA-PREF-E2E-033 | FE+BE |
| TC-FA-PREF-149 | TC-FA-PREF-E2E-033 | FE+BE |
| TC-FA-PREF-150 | TC-FA-PREF-E2E-035 | FE+BE |
| TC-FA-PREF-151 | TC-FA-PREF-E2E-035 | FE+BE |
| TC-FA-PREF-152 | TC-FA-PREF-E2E-043 | FE+BE |
| TC-FA-PREF-153 | TC-FA-PREF-E2E-043 | FE+BE |
| TC-FA-PREF-154 | TC-FA-PREF-E2E-043 | FE+BE |
| TC-FA-PREF-155 | TC-FA-PREF-E2E-045 | FE+BE |
| TC-FA-PREF-156 | TC-FA-PREF-E2E-045 | FE+BE |
| TC-FA-PREF-157 | TC-FA-PREF-E2E-045 | FE+BE |
| TC-FA-PREF-158 | TC-FA-PREF-E2E-049 | FE+BE |
| TC-FA-PREF-159 | TC-FA-PREF-E2E-049 | FE+BE |
| TC-FA-PREF-160 | TC-FA-PREF-E2E-049 | FE+BE |
| TC-FA-PREF-161 | TC-FA-PREF-E2E-050 | FE+BE |
| TC-FA-PREF-162 | TC-FA-PREF-E2E-050 | FE+BE |
| TC-FA-PREF-163 | TC-FA-PREF-E2E-050 | FE+BE |
| TC-FA-PREF-164 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-165 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-166 | TC-FA-PREF-E2E-051 | FE+BE |
| TC-FA-PREF-167 | TC-FA-PREF-E2E-051 | FE+BE |
| TC-FA-PREF-168 | TC-FA-PREF-E2E-052 | FE+BE |
| TC-FA-PREF-169 | TC-FA-PREF-E2E-052 | FE+BE |
| TC-FA-PREF-170 | TC-FA-PREF-E2E-162 | FE+BE |
| TC-FA-PREF-171 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-172 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-173 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-174 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-175 | TC-FA-PREF-E2E-052 | FE+BE |
| TC-FA-PREF-176 | TC-FA-PREF-E2E-054 | FE+BE |
| TC-FA-PREF-177 | TC-FA-PREF-E2E-055 | FE+BE |
| TC-FA-PREF-178 | TC-FA-PREF-E2E-054 | FE+BE |
| TC-FA-PREF-179 | TC-FA-PREF-E2E-054 | FE+BE |
| TC-FA-PREF-180 | TC-FA-PREF-E2E-054 | FE+BE |
| TC-FA-PREF-181 | TC-FA-PREF-E2E-056 | FE+BE |
| TC-FA-PREF-182 | TC-FA-PREF-E2E-055 | FE+BE |
| TC-FA-PREF-183 | TC-FA-PREF-E2E-058 | FE+BE |
| TC-FA-PREF-184 | TC-FA-PREF-E2E-058 | FE+BE |
| TC-FA-PREF-185 | TC-FA-PREF-E2E-058 | FE+BE |
| TC-FA-PREF-186 | TC-FA-PREF-E2E-058 | FE+BE |
| TC-FA-PREF-187 | TC-FA-PREF-E2E-059 | FE+BE |
| TC-FA-PREF-188 | TC-FA-PREF-E2E-059 | FE+BE |
| TC-FA-PREF-189 | TC-FA-PREF-E2E-059 | FE+BE |
| TC-FA-PREF-190 | TC-FA-PREF-E2E-059 | FE+BE |
| TC-FA-PREF-191 | TC-FA-PREF-E2E-061 | FE+BE |
| TC-FA-PREF-192 | TC-FA-PREF-E2E-061 | FE+BE |
| TC-FA-PREF-193 | TC-FA-PREF-E2E-061 | FE+BE |
| TC-FA-PREF-194 | TC-FA-PREF-E2E-062 | FE+BE |
| TC-FA-PREF-195 | TC-FA-PREF-E2E-062 | FE+BE |
| TC-FA-PREF-196 | TC-FA-PREF-E2E-062 | FE+BE |
| TC-FA-PREF-197 | TC-FA-PREF-E2E-062 | FE+BE |
| TC-FA-PREF-198 | TC-FA-PREF-E2E-063 | FE+BE |
| TC-FA-PREF-199 | TC-FA-PREF-E2E-064 | FE+BE |
| TC-FA-PREF-200 | TC-FA-PREF-E2E-063 | FE+BE |
| TC-FA-PREF-201 | TC-FA-PREF-E2E-063 | FE+BE |
| TC-FA-PREF-202 | TC-FA-PREF-E2E-064 | FE+BE |
| TC-FA-PREF-203 | TC-FA-PREF-E2E-064 | FE+BE |
| TC-FA-PREF-204 | TC-FA-PREF-E2E-157 | FE+BE |
| TC-FA-PREF-205 | TC-FA-PREF-E2E-095 | FE+BE |
| TC-FA-PREF-206 | TC-FA-PREF-E2E-095 | FE+BE |
| TC-FA-PREF-207 | TC-FA-PREF-E2E-065 | FE+BE |
| TC-FA-PREF-208 | TC-FA-PREF-E2E-065 | FE+BE |
| TC-FA-PREF-209 | TC-FA-PREF-E2E-065 | FE+BE |
| TC-FA-PREF-210 | TC-FA-PREF-E2E-066 | FE+BE |
| TC-FA-PREF-211 | TC-FA-PREF-E2E-066 | FE+BE |
| TC-FA-PREF-212 | TC-FA-PREF-E2E-066 | FE+BE |
| TC-FA-PREF-213 | TC-FA-PREF-E2E-056 | FE+BE |
| TC-FA-PREF-214 | TC-FA-PREF-E2E-041 | FE+BE |
| TC-FA-PREF-215 | TC-FA-PREF-E2E-041 | FE+BE |
| TC-FA-PREF-216 | TC-FA-PREF-E2E-175 | FE+BE |
| TC-FA-PREF-217 | TC-FA-PREF-E2E-175 | FE+BE |
| TC-FA-PREF-218 | TC-FA-PREF-E2E-042 | FE+BE |
| TC-FA-PREF-219 | TC-FA-PREF-E2E-044 | FE+BE |
| TC-FA-PREF-220 | TC-FA-PREF-E2E-044 | FE+BE |
| TC-FA-PREF-221 | TC-FA-PREF-E2E-048 | FE+BE |
| TC-FA-PREF-222 | TC-FA-PREF-E2E-046 | FE+BE |
| TC-FA-PREF-223 | TC-FA-PREF-E2E-046 | FE+BE |
| TC-FA-PREF-224 | TC-FA-PREF-E2E-046 | FE+BE |
| TC-FA-PREF-225 | TC-FA-PREF-E2E-048 | FE+BE |
| TC-FA-PREF-226 | TC-FA-PREF-E2E-046 | FE+BE |
| TC-FA-PREF-227 | TC-FA-PREF-E2E-090 | FE+BE |
| TC-FA-PREF-228 | TC-FA-PREF-E2E-090 | FE+BE |
| TC-FA-PREF-229 | TC-FA-PREF-E2E-023 | FE+BE |
| TC-FA-PREF-230 | TC-FA-PREF-E2E-077 | FE+BE |
| TC-FA-PREF-231 | TC-FA-PREF-E2E-087 | FE+BE |
| TC-FA-PREF-232 | TC-FA-PREF-E2E-084 | FE+BE |
| TC-FA-PREF-233 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-234 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-235 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-236 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-237 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-238 | TC-FA-PREF-E2E-067 | FE+BE |
| TC-FA-PREF-239 | TC-FA-PREF-E2E-067 | FE+BE |
| TC-FA-PREF-240 | TC-FA-PREF-E2E-067 | FE+BE |
| TC-FA-PREF-241 | TC-FA-PREF-E2E-068 | FE+BE |
| TC-FA-PREF-242 | TC-FA-PREF-E2E-068 | FE+BE |
| TC-FA-PREF-243 | TC-FA-PREF-E2E-068 | FE+BE |
| TC-FA-PREF-244 | TC-FA-PREF-E2E-087 | FE+BE |
| TC-FA-PREF-245 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-246 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-247 | TC-FA-PREF-E2E-028 | FE+BE |
| TC-FA-PREF-248 | TC-FA-PREF-E2E-068 | FE+BE |
| TC-FA-PREF-249 | TC-FA-PREF-E2E-079 | FE+BE |
| TC-FA-PREF-250 | TC-FA-PREF-E2E-079 | FE+BE |
| TC-FA-PREF-251 | TC-FA-PREF-E2E-069 | FE+BE |
| TC-FA-PREF-252 | TC-FA-PREF-E2E-069 | FE+BE |
| TC-FA-PREF-253 | TC-FA-PREF-E2E-069 | FE+BE |
| TC-FA-PREF-254 | TC-FA-PREF-E2E-070 | FE+BE |
| TC-FA-PREF-255 | TC-FA-PREF-E2E-070 | FE+BE |
| TC-FA-PREF-256 | TC-FA-PREF-E2E-070 | FE+BE |
| TC-FA-PREF-257 | TC-FA-PREF-E2E-071 | FE+BE |
| TC-FA-PREF-258 | TC-FA-PREF-E2E-073 | FE+BE |
| TC-FA-PREF-259 | TC-FA-PREF-E2E-073 | FE+BE |
| TC-FA-PREF-260 | TC-FA-PREF-E2E-073 | FE+BE |
| TC-FA-PREF-261 | TC-FA-PREF-E2E-074 | FE+BE |
| TC-FA-PREF-262 | TC-FA-PREF-E2E-074 | FE+BE |
| TC-FA-PREF-263 | TC-FA-PREF-E2E-073 | FE+BE |
| TC-FA-PREF-264 | TC-FA-PREF-E2E-165 | FE+BE |
| TC-FA-PREF-265 | TC-FA-PREF-E2E-165 | FE+BE |
| TC-FA-PREF-266 | TC-FA-PREF-E2E-075 | FE+BE |
| TC-FA-PREF-267 | TC-FA-PREF-E2E-075 | FE+BE |
| TC-FA-PREF-268 | TC-FA-PREF-E2E-075 | FE+BE |
| TC-FA-PREF-269 | TC-FA-PREF-E2E-075 | FE+BE |
| TC-FA-PREF-270 | TC-FA-PREF-E2E-076 | FE+BE |
| TC-FA-PREF-271 | TC-FA-PREF-E2E-076 | FE+BE |
| TC-FA-PREF-272 | TC-FA-PREF-E2E-076 | FE+BE |
| TC-FA-PREF-273 | TC-FA-PREF-E2E-076 | FE+BE |
| TC-FA-PREF-274 | TC-FA-PREF-E2E-089 | FE+BE |
| TC-FA-PREF-275 | TC-FA-PREF-E2E-051 | FE+BE |
| TC-FA-PREF-276 | TC-FA-PREF-E2E-167 | FE+BE |
| TC-FA-PREF-277 | TC-FA-PREF-E2E-029 | FE+BE |
| TC-FA-PREF-278 | TC-FA-PREF-E2E-092 | FE+BE |
| TC-FA-PREF-279 | TC-FA-PREF-E2E-092 | FE+BE |
| TC-FA-PREF-280 | TC-FA-PREF-E2E-093 | FE+BE |
| TC-FA-PREF-281 | TC-FA-PREF-E2E-093 | FE+BE |
| TC-FA-PREF-282 | TC-FA-PREF-E2E-092 | FE+BE |
| TC-FA-PREF-283 | TC-FA-PREF-E2E-019 | FE+BE |
| TC-FA-PREF-284 | TC-FA-PREF-E2E-020 | FE+BE |
| TC-FA-PREF-285 | TC-FA-PREF-E2E-158 | FE+BE |
| TC-FA-PREF-286 | TC-FA-PREF-E2E-158 | FE+BE |
| TC-FA-PREF-287 | TC-FA-PREF-E2E-086 | FE+BE |
| TC-FA-PREF-288 | TC-FA-PREF-E2E-094 | FE+BE |
| TC-FA-PREF-289 | TC-FA-PREF-E2E-097 | FE+BE |
| TC-FA-PREF-290 | TC-FA-PREF-E2E-097 | FE+BE |
| TC-FA-PREF-291 | TC-FA-PREF-E2E-097 | FE+BE |
| TC-FA-PREF-292 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-293 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-294 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-295 | TC-FA-PREF-E2E-014 | FE+BE |
| TC-FA-PREF-296 | TC-FA-PREF-E2E-096 | FE+BE |
| TC-FA-PREF-297 | TC-FA-PREF-E2E-098 | FE+BE |
| TC-FA-PREF-298 | TC-FA-PREF-E2E-099 | FE+BE |
| TC-FA-PREF-299 | TC-FA-PREF-E2E-099 | FE+BE |
| TC-FA-PREF-300 | TC-FA-PREF-E2E-100 | FE+BE |
| TC-FA-PREF-301 | TC-FA-PREF-E2E-100 | FE+BE |
| TC-FA-PREF-302 | TC-FA-PREF-E2E-100 | FE+BE |
| TC-FA-PREF-303 | TC-FA-PREF-E2E-101 | FE+BE |
| TC-FA-PREF-304 | TC-FA-PREF-E2E-101 | FE+BE |
| TC-FA-PREF-305 | TC-FA-PREF-E2E-102 | FE+BE |
| TC-FA-PREF-306 | TC-FA-PREF-E2E-102 | FE+BE |
| TC-FA-PREF-307 | TC-FA-PREF-E2E-102 | FE+BE |
| TC-FA-PREF-308 | TC-FA-PREF-E2E-103 | FE+BE |
| TC-FA-PREF-309 | TC-FA-PREF-E2E-103 | FE+BE |
| TC-FA-PREF-310 | TC-FA-PREF-E2E-103 | FE+BE |
| TC-FA-PREF-311 | TC-FA-PREF-E2E-103 | FE+BE |
| TC-FA-PREF-312 | TC-FA-PREF-E2E-104 | FE+BE |
| TC-FA-PREF-313 | TC-FA-PREF-E2E-104 | FE+BE |
| TC-FA-PREF-314 | TC-FA-PREF-E2E-104 | FE+BE |
| TC-FA-PREF-315 | TC-FA-PREF-E2E-104 | FE+BE |
| TC-FA-PREF-316 | TC-FA-PREF-E2E-105 | FE+BE |
| TC-FA-PREF-317 | TC-FA-PREF-E2E-105 | FE+BE |
| TC-FA-PREF-318 | TC-FA-PREF-E2E-101 | FE+BE |
| TC-FA-PREF-319 | TC-FA-PREF-E2E-101 | FE+BE |
| TC-FA-PREF-320 | TC-FA-PREF-E2E-105 | FE+BE |
| TC-FA-PREF-321 | TC-FA-PREF-E2E-106 | FE+BE |
| TC-FA-PREF-322 | TC-FA-PREF-E2E-106 | FE+BE |
| TC-FA-PREF-323 | TC-FA-PREF-E2E-107 | FE+BE |
| TC-FA-PREF-324 | TC-FA-PREF-E2E-107 | FE+BE |
| TC-FA-PREF-325 | TC-FA-PREF-E2E-107 | FE+BE |
| TC-FA-PREF-327 | TC-FA-PREF-E2E-108 | FE+BE |
| TC-FA-PREF-328 | TC-FA-PREF-E2E-108 | FE+BE |
| TC-FA-PREF-329 | TC-FA-PREF-E2E-108 | FE+BE |
| TC-FA-PREF-330 | TC-FA-PREF-E2E-108 | FE+BE |
| TC-FA-PREF-331 | TC-FA-PREF-E2E-107 | FE+BE |
| TC-FA-PREF-332 | TC-FA-PREF-E2E-109 | FE+BE |
| TC-FA-PREF-333 | TC-FA-PREF-E2E-109 | FE+BE |
| TC-FA-PREF-334 | TC-FA-PREF-E2E-109 | FE+BE |
| TC-FA-PREF-335 | TC-FA-PREF-E2E-110 | FE+BE |
| TC-FA-PREF-336 | TC-FA-PREF-E2E-111 | FE+BE |
| TC-FA-PREF-337 | TC-FA-PREF-E2E-169 | FE+BE |
| TC-FA-PREF-338 | TC-FA-PREF-E2E-111 | FE+BE |
| TC-FA-PREF-339 | TC-FA-PREF-E2E-111 | FE+BE |
| TC-FA-PREF-340 | TC-FA-PREF-E2E-112 | FE+BE |
| TC-FA-PREF-341 | TC-FA-PREF-E2E-112 | FE+BE |
| TC-FA-PREF-342 | TC-FA-PREF-E2E-113 | FE+BE |
| TC-FA-PREF-343 | TC-FA-PREF-E2E-113 | FE+BE |
| TC-FA-PREF-344 | TC-FA-PREF-E2E-113 | FE+BE |
| TC-FA-PREF-345 | TC-FA-PREF-E2E-113 | FE+BE |
| TC-FA-PREF-346 | TC-FA-PREF-E2E-113 | FE+BE |
| TC-FA-PREF-347 | TC-FA-PREF-E2E-114 | FE+BE |
| TC-FA-PREF-348 | TC-FA-PREF-E2E-114 | FE+BE |
| TC-FA-PREF-349 | TC-FA-PREF-E2E-114 | FE+BE |
| TC-FA-PREF-350 | TC-FA-PREF-E2E-115 | FE+BE |
| TC-FA-PREF-351 | TC-FA-PREF-E2E-115 | FE+BE |
| TC-FA-PREF-352 | TC-FA-PREF-E2E-115 | FE+BE |
| TC-FA-PREF-353 | TC-FA-PREF-E2E-115 | FE+BE |
| TC-FA-PREF-354 | TC-FA-PREF-E2E-116 | FE+BE |
| TC-FA-PREF-355 | TC-FA-PREF-E2E-117 | FE+BE |
| TC-FA-PREF-356 | TC-FA-PREF-E2E-116 | FE+BE |
| TC-FA-PREF-357 | TC-FA-PREF-E2E-116 | FE+BE |
| TC-FA-PREF-358 | TC-FA-PREF-E2E-116 | FE+BE |
| TC-FA-PREF-359 | TC-FA-PREF-E2E-117 | FE+BE |
| TC-FA-PREF-360 | TC-FA-PREF-E2E-117 | FE+BE |
| TC-FA-PREF-361 | TC-FA-PREF-E2E-096 | FE+BE |
| TC-FA-PREF-362 | TC-FA-PREF-E2E-118 | FE+BE |
| TC-FA-PREF-363 | TC-FA-PREF-E2E-118 | FE+BE |
| TC-FA-PREF-364 | TC-FA-PREF-E2E-119 | FE+BE |
| TC-FA-PREF-365 | TC-FA-PREF-E2E-119 | FE+BE |
| TC-FA-PREF-366 | TC-FA-PREF-E2E-120 | FE+BE |
| TC-FA-PREF-367 | TC-FA-PREF-E2E-120 | FE+BE |
| TC-FA-PREF-368 | TC-FA-PREF-E2E-121 | FE+BE |
| TC-FA-PREF-369 | TC-FA-PREF-E2E-121 | FE+BE |
| TC-FA-PREF-370 | TC-FA-PREF-E2E-122 | FE+BE |
| TC-FA-PREF-371 | TC-FA-PREF-E2E-122 | FE+BE |
| TC-FA-PREF-372 | TC-FA-PREF-E2E-122 | FE+BE |
| TC-FA-PREF-373 | TC-FA-PREF-E2E-123 | FE+BE |
| TC-FA-PREF-374 | TC-FA-PREF-E2E-123 | FE+BE |
| TC-FA-PREF-375 | TC-FA-PREF-E2E-123 | FE+BE |
| TC-FA-PREF-376 | TC-FA-PREF-E2E-124 | FE+BE |
| TC-FA-PREF-377 | TC-FA-PREF-E2E-124 | FE+BE |
| TC-FA-PREF-378 | TC-FA-PREF-E2E-125 | FE+BE |
| TC-FA-PREF-379 | TC-FA-PREF-E2E-125 | FE+BE |
| TC-FA-PREF-380 | TC-FA-PREF-E2E-126 | FE+BE |
| TC-FA-PREF-381 | TC-FA-PREF-E2E-126 | FE+BE |
| TC-FA-PREF-382 | TC-FA-PREF-E2E-087 | FE+BE |
| TC-FA-PREF-383 | TC-FA-PREF-E2E-127 | FE+BE |
| TC-FA-PREF-384 | TC-FA-PREF-E2E-127 | FE+BE |
| TC-FA-PREF-385 | TC-FA-PREF-E2E-127 | FE+BE |
| TC-FA-PREF-386 | TC-FA-PREF-E2E-088 | FE+BE |
| TC-FA-PREF-387 | TC-FA-PREF-E2E-088 | FE+BE |
| TC-FA-PREF-388 | TC-FA-PREF-E2E-124 | FE+BE |
| TC-FA-PREF-389 | TC-FA-PREF-E2E-128 | FE+BE |
| TC-FA-PREF-390 | TC-FA-PREF-E2E-128 | FE+BE |
| TC-FA-PREF-391 | TC-FA-PREF-E2E-128 | FE+BE |
| TC-FA-PREF-392 | TC-FA-PREF-E2E-094 | FE+BE |
| TC-FA-PREF-393 | TC-FA-PREF-E2E-130 | FE+BE |
| TC-FA-PREF-394 | TC-FA-PREF-E2E-131 | FE+BE |
| TC-FA-PREF-395 | TC-FA-PREF-E2E-131 | FE+BE |
| TC-FA-PREF-396 | TC-FA-PREF-E2E-130 | FE+BE |
| TC-FA-PREF-397 | TC-FA-PREF-E2E-016 | FE+BE |
| TC-FA-PREF-398 | TC-FA-PREF-E2E-016 | FE+BE |
| TC-FA-PREF-401 | TC-FA-PREF-E2E-132 | FE+BE |
| TC-FA-PREF-402 | TC-FA-PREF-E2E-132 | FE+BE |
| TC-FA-PREF-403 | TC-FA-PREF-E2E-132 | FE+BE |
| TC-FA-PREF-404 | TC-FA-PREF-E2E-133 | FE+BE |
| TC-FA-PREF-405 | TC-FA-PREF-E2E-132 | FE+BE |
| TC-FA-PREF-406 | TC-FA-PREF-E2E-133 | FE+BE |
| TC-FA-PREF-407 | TC-FA-PREF-E2E-133 | FE+BE |
| TC-FA-PREF-408 | TC-FA-PREF-E2E-133 | FE+BE |
| TC-FA-PREF-409 | TC-FA-PREF-E2E-130 | FE+BE |
| TC-FA-PREF-410 | TC-FA-PREF-E2E-171 | FE+BE |
| TC-FA-PREF-411 | TC-FA-PREF-E2E-134 | FE+BE |
| TC-FA-PREF-412 | TC-FA-PREF-E2E-134 | FE+BE |
| TC-FA-PREF-413 | TC-FA-PREF-E2E-134 | FE+BE |
| TC-FA-PREF-414 | TC-FA-PREF-E2E-134 | FE+BE |
| TC-FA-PREF-415 | TC-FA-PREF-E2E-134 | FE+BE |
| TC-FA-PREF-416 | TC-FA-PREF-E2E-135 | FE+BE |
| TC-FA-PREF-417 | TC-FA-PREF-E2E-135 | FE+BE |
| TC-FA-PREF-418 | TC-FA-PREF-E2E-135 | FE+BE |
| TC-FA-PREF-419 | TC-FA-PREF-E2E-136 | FE+BE |
| TC-FA-PREF-420 | TC-FA-PREF-E2E-136 | FE+BE |
| TC-FA-PREF-421 | TC-FA-PREF-E2E-137 | FE+BE |
| TC-FA-PREF-422 | TC-FA-PREF-E2E-137 | FE+BE |
| TC-FA-PREF-423 | TC-FA-PREF-E2E-137 | FE+BE |
| TC-FA-PREF-424 | TC-FA-PREF-E2E-137 | FE+BE |
| TC-FA-PREF-425 | TC-FA-PREF-E2E-138 | FE+BE |
| TC-FA-PREF-426 | TC-FA-PREF-E2E-138 | FE+BE |
| TC-FA-PREF-427 | TC-FA-PREF-E2E-088 | FE+BE |
| TC-FA-PREF-428 | TC-FA-PREF-E2E-138 | FE+BE |
| TC-FA-PREF-429 | TC-FA-PREF-E2E-136 | FE+BE |
| TC-FA-PREF-430 | TC-FA-PREF-E2E-136 | FE+BE |
| TC-FA-PREF-431 | TC-FA-PREF-E2E-139 | FE+BE |
| TC-FA-PREF-432 | TC-FA-PREF-E2E-139 | FE+BE |
| TC-FA-PREF-433 | TC-FA-PREF-E2E-139 | FE+BE |
| TC-FA-PREF-434 | TC-FA-PREF-E2E-139 | FE+BE |
| TC-FA-PREF-435 | TC-FA-PREF-E2E-140 | FE+BE |
| TC-FA-PREF-436 | TC-FA-PREF-E2E-140 | FE+BE |
| TC-FA-PREF-437 | TC-FA-PREF-E2E-140 | FE+BE |
| TC-FA-PREF-438 | TC-FA-PREF-E2E-173 | FE+BE |
| TC-FA-PREF-439 | TC-FA-PREF-E2E-173 | FE+BE |
| TC-FA-PREF-440 | TC-FA-PREF-E2E-139 | FE+BE |
| TC-FA-PREF-441 | TC-FA-PREF-E2E-141 | FE+BE |
| TC-FA-PREF-442 | TC-FA-PREF-E2E-141 | FE+BE |
| TC-FA-PREF-443 | TC-FA-PREF-E2E-141 | FE+BE |
| TC-FA-PREF-444 | TC-FA-PREF-E2E-141 | FE+BE |
| TC-FA-PREF-445 | TC-FA-PREF-E2E-142 | FE+BE |
| TC-FA-PREF-446 | TC-FA-PREF-E2E-142 | FE+BE |
| TC-FA-PREF-447 | TC-FA-PREF-E2E-142 | FE+BE |
| TC-FA-PREF-448 | TC-FA-PREF-E2E-142 | FE+BE |
| TC-FA-PREF-449 | TC-FA-PREF-E2E-143 | FE+BE |
| TC-FA-PREF-450 | TC-FA-PREF-E2E-143 | FE+BE |
| TC-FA-PREF-451 | TC-FA-PREF-E2E-143 | FE+BE |
| TC-FA-PREF-452 | TC-FA-PREF-E2E-143 | FE+BE |
| TC-FA-PREF-453 | TC-FA-PREF-E2E-142 | FE+BE |
| TC-FA-PREF-454 | TC-FA-PREF-E2E-144 | FE+BE |
| TC-FA-PREF-455 | TC-FA-PREF-E2E-144 | FE+BE |
| TC-FA-PREF-456 | TC-FA-PREF-E2E-174 | FE+BE |
| TC-FA-PREF-457 | TC-FA-PREF-E2E-174 | FE+BE |
| TC-FA-PREF-458 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-459 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-460 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-461 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-462 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-463 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-464 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-465 | TC-FA-PREF-E2E-145 | FE+BE |
| TC-FA-PREF-466 | TC-FA-PREF-E2E-146 | FE+BE |
| TC-FA-PREF-467 | TC-FA-PREF-E2E-146 | FE+BE |
| TC-FA-PREF-468 | TC-FA-PREF-E2E-146 | FE+BE |
| TC-FA-PREF-469 | TC-FA-PREF-E2E-146 | FE+BE |
| TC-FA-PREF-470 | TC-FA-PREF-E2E-146 | FE+BE |
| TC-FA-PREF-471 | TC-FA-PREF-E2E-147 | FE+BE |
| TC-FA-PREF-472 | TC-FA-PREF-E2E-147 | FE+BE |
| TC-FA-PREF-473 | TC-FA-PREF-E2E-147 | FE+BE |
| TC-FA-PREF-474 | TC-FA-PREF-E2E-147 | FE+BE |
| TC-FA-PREF-475 | TC-FA-PREF-E2E-147 | FE+BE |
| TC-FA-PREF-476 | TC-FA-PREF-E2E-148 | FE+BE |
| TC-FA-PREF-477 | TC-FA-PREF-E2E-148 | FE+BE |
| TC-FA-PREF-478 | TC-FA-PREF-E2E-148 | FE+BE |
| TC-FA-PREF-479 | TC-FA-PREF-E2E-148 | FE+BE |
| TC-FA-PREF-480 | TC-FA-PREF-E2E-148 | FE+BE |
| TC-FA-PREF-481 | TC-FA-PREF-E2E-149 | FE+BE |
| TC-FA-PREF-482 | TC-FA-PREF-E2E-149 | FE+BE |
| TC-FA-PREF-483 | TC-FA-PREF-E2E-149 | FE+BE |
| TC-FA-PREF-484 | TC-FA-PREF-E2E-150 | FE+BE |
| TC-FA-PREF-485 | TC-FA-PREF-E2E-150 | FE+BE |
| TC-FA-PREF-486 | TC-FA-PREF-E2E-150 | FE+BE |
| TC-FA-PREF-487 | TC-FA-PREF-E2E-150 | FE+BE |
| TC-FA-PREF-488 | TC-FA-PREF-E2E-151 | FE+BE |
| TC-FA-PREF-489 | TC-FA-PREF-E2E-151 | FE+BE |
| TC-FA-PREF-490 | TC-FA-PREF-E2E-151 | FE+BE |
| TC-FA-PREF-491 | TC-FA-PREF-E2E-151 | FE+BE |
| TC-FA-PREF-492 | TC-FA-PREF-E2E-151 | FE+BE |
| TC-FA-PREF-493 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-494 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-495 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-496 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-497 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-498 | TC-FA-PREF-E2E-152 | FE+BE |
| TC-FA-PREF-499 | TC-FA-PREF-E2E-153 | FE+BE |
| TC-FA-PREF-500 | TC-FA-PREF-E2E-153 | FE+BE |
| TC-FA-PREF-501 | TC-FA-PREF-E2E-153 | FE+BE |
| TC-FA-PREF-502 | TC-FA-PREF-E2E-153 | FE+BE |
| TC-FA-PREF-503 | TC-FA-PREF-E2E-153 | FE+BE |
| TC-FA-PREF-504 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-505 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-506 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-507 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-508 | TC-FA-PREF-E2E-096 | FE+BE |
| TC-FA-PREF-509 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-510 | TC-FA-PREF-E2E-154 | FE+BE |
| TC-FA-PREF-511 | TC-FA-PREF-E2E-077 | FE+BE |
| TC-FA-PREF-512 | TC-FA-PREF-E2E-077 | FE+BE |
| TC-FA-PREF-513 | TC-FA-PREF-E2E-077 | FE+BE |
| TC-FA-PREF-514 | TC-FA-PREF-E2E-077 | FE+BE |
| TC-FA-PREF-515 | TC-FA-PREF-E2E-078 | FE+BE |
| TC-FA-PREF-516 | TC-FA-PREF-E2E-078 | FE+BE |
| TC-FA-PREF-517 | TC-FA-PREF-E2E-078 | FE+BE |
| TC-FA-PREF-518 | TC-FA-PREF-E2E-078 | FE+BE |
| TC-FA-PREF-519 | TC-FA-PREF-E2E-079 | FE+BE |
| TC-FA-PREF-520 | TC-FA-PREF-E2E-079 | FE+BE |
| TC-FA-PREF-521 | TC-FA-PREF-E2E-079 | FE+BE |
| TC-FA-PREF-522 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-523 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-524 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-525 | TC-FA-PREF-E2E-080 | FE+BE |
| TC-FA-PREF-526 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-527 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-528 | TC-FA-PREF-E2E-081 | FE+BE |
| TC-FA-PREF-529 | TC-FA-PREF-E2E-166 | FE+BE |
| TC-FA-PREF-530 | TC-FA-PREF-E2E-166 | FE+BE |
| TC-FA-PREF-531 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-532 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-533 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-534 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-535 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-536 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-537 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-538 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-539 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-540 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-541 | TC-FA-PREF-E2E-082 | FE+BE |
| TC-FA-PREF-542 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-543 | TC-FA-PREF-E2E-083 | FE+BE |
| TC-FA-PREF-544 | TC-FA-PREF-E2E-084 | FE+BE |
| TC-FA-PREF-545 | TC-FA-PREF-E2E-084 | FE+BE |
| TC-FA-PREF-546 | TC-FA-PREF-E2E-085 | FE+BE |
| TC-FA-PREF-547 | TC-FA-PREF-E2E-085 | FE+BE |
| TC-FA-PREF-548 | TC-FA-PREF-E2E-025 | FE+BE |
| TC-FA-PREF-549 | TC-FA-PREF-E2E-129 | FE+BE |
| TC-FA-PREF-550 | TC-FA-PREF-E2E-031 | FE+BE |
| TC-FA-PREF-551 | TC-FA-PREF-E2E-038 | FE+BE |
| TC-FA-PREF-552 | TC-FA-PREF-E2E-038 | FE+BE |
| TC-FA-PREF-553 | TC-FA-PREF-E2E-038 | FE+BE |
| TC-FA-PREF-554 | TC-FA-PREF-E2E-038 | FE+BE |
| TC-FA-PREF-555 | TC-FA-PREF-E2E-038 | FE+BE |
| TC-FA-PREF-556 | TC-FA-PREF-E2E-042 | FE+BE |
| TC-FA-PREF-557 | TC-FA-PREF-E2E-072 | FE+BE |
| TC-FA-PREF-558 | TC-FA-PREF-E2E-072 | FE+BE |
| TC-FA-PREF-559 | TC-FA-PREF-E2E-164 | FE+BE |
| TC-FA-PREF-560 | TC-FA-PREF-E2E-168 | FE+BE |
| TC-FA-PREF-561 | TC-FA-PREF-E2E-023 | FE+BE |
| TC-FA-PREF-562 | TC-FA-PREF-E2E-167 | FE+BE |
| TC-FA-PREF-563 | TC-FA-PREF-E2E-090 | FE+BE |
| TC-FA-PREF-564 | TC-FA-PREF-E2E-091 | FE+BE |
| TC-FA-PREF-565 | TC-FA-PREF-E2E-091 | FE+BE |
| TC-FA-PREF-566 | TC-FA-PREF-E2E-090 | FE+BE |
| TC-FA-PREF-567 | TC-FA-PREF-E2E-091 | FE+BE |
| TC-FA-PREF-568 | TC-FA-PREF-E2E-091 | FE+BE |
| TC-FA-PREF-569 | TC-FA-PREF-E2E-029 | FE+BE |
| TC-FA-PREF-570 | TC-FA-PREF-E2E-029 | FE+BE |
| TC-FA-PREF-571 | TC-FA-PREF-E2E-030 | FE+BE |
| TC-FA-PREF-572 | TC-FA-PREF-E2E-030 | FE+BE |
| TC-FA-PREF-573 | TC-FA-PREF-E2E-094 | FE+BE |
| TC-FA-PREF-574 | TC-FA-PREF-E2E-093 | FE+BE |
| TC-FA-PREF-575 | TC-FA-PREF-E2E-076 | FE+BE |
| TC-FA-PREF-576 | TC-FA-PREF-E2E-075 | FE+BE |
| TC-FA-PREF-577 | TC-FA-PREF-E2E-089 | FE+BE |
| TC-FA-PREF-578 | TC-FA-PREF-E2E-043 | FE+BE |
| TC-FA-PREF-579 | TC-FA-PREF-E2E-044 | FE+BE |
| TC-FA-PREF-580 | TC-FA-PREF-E2E-044 | FE+BE |
| TC-FA-PREF-581 | TC-FA-PREF-E2E-176 | FE+BE |
| TC-FA-PREF-582 | TC-FA-PREF-E2E-176 | FE+BE |
| TC-FA-PREF-583 | TC-FA-PREF-E2E-057 | FE+BE |
| TC-FA-PREF-584 | TC-FA-PREF-E2E-056 | FE+BE |
| TC-FA-PREF-585 | TC-FA-PREF-E2E-047 | FE+BE |
| TC-FA-PREF-586 | TC-FA-PREF-E2E-047 | FE+BE |
| TC-FA-PREF-587 | TC-FA-PREF-E2E-047 | FE+BE |
| TC-FA-PREF-588 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-589 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-590 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-591 | TC-FA-PREF-E2E-053 | FE+BE |
| TC-FA-PREF-592 | TC-FA-PREF-E2E-162 | FE+BE |
| TC-FA-PREF-593 | TC-FA-PREF-E2E-057 | FE+BE |
| TC-FA-PREF-594 | TC-FA-PREF-E2E-021 | FE+BE |
| TC-FA-PREF-595 | TC-FA-PREF-E2E-021 | FE+BE |
| TC-FA-PREF-596 | TC-FA-PREF-E2E-005 | FE+BE |
| TC-FA-PREF-597 | TC-FA-PREF-E2E-157 | FE+BE |
| TC-FA-PREF-598 | TC-FA-PREF-E2E-096 | FE+BE |
| TC-FA-PREF-599 | TC-FA-PREF-E2E-035 | FE+BE |
| TC-FA-PREF-600 | TC-FA-PREF-E2E-035 | FE+BE |
| TC-FA-PREF-601 | TC-FA-PREF-E2E-004 | FE+BE |
| TC-FA-PREF-602 | TC-FA-PREF-E2E-087 | FE+BE |
| TC-FA-PREF-603 | TC-FA-PREF-E2E-163 | FE+BE |
| TC-FA-PREF-604 | TC-FA-PREF-E2E-163 | FE+BE |
| TC-FA-PREF-605 | TC-FA-PREF-E2E-149 | FE+BE |
| TC-FA-PREF-606 | TC-FA-PREF-E2E-013 | FE+BE |
| TC-FA-PREF-607 | TC-FA-PREF-E2E-013 | FE+BE |
| TC-FA-PREF-608 | TC-FA-PREF-E2E-021 | FE+BE |
| TC-FA-PREF-609 | TC-FA-PREF-E2E-034 | FE+BE |
| TC-FA-PREF-610 | TC-FA-PREF-E2E-034 | FE+BE |
| TC-FA-PREF-611 | TC-FA-PREF-E2E-060 | FE+BE |
| TC-FA-PREF-612 | TC-FA-PREF-E2E-060 | FE+BE |
| TC-FA-PREF-613 | TC-FA-PREF-E2E-074 | FE+BE |
| TC-FA-PREF-614 | TC-FA-PREF-E2E-074 | FE+BE |
| TC-FA-PREF-615 | TC-FA-PREF-E2E-039 | FE+BE |
| TC-FA-PREF-616 | TC-FA-PREF-E2E-039 | FE+BE |
| TC-FA-PREF-617 | TC-FA-PREF-E2E-039 | FE+BE |
| TC-FA-PREF-618 | TC-FA-PREF-E2E-160 | FE+BE |
| TC-FA-PREF-619 | TC-FA-PREF-E2E-039 | FE+BE |
| TC-FA-PREF-621 | TC-FA-PREF-E2E-060 | FE+BE |
