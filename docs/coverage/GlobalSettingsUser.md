# Coverage E2E — Global Settings > User > User List dan User Detail

Sumber: `global-settings/user/TestCases/tc-user.md` (1086 ID aktif `TC-GS-USER-1`–`1088`; `TC-GS-USER-956` dan `TC-GS-USER-957` retired dan tidak ada di berkas). Referensi kontrak: `global-settings/user/PRD/user.md`. Suite: `specs/GlobalSettings/User/`. Prefix: `GS` + `USER` (`TC-GS-USER-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 1086 TC aktif masuk spec, 0 TC hanya-BE (kolom PIC FE seluruh TC bernilai `v`; TC request-langsung Section 8 tetap spec karena asersinya respons server dan state data). 159 spec (155 FE+BE, 4 mock). Setiap TC terpetakan ke tepat satu spec (`sourceTc`); tidak ada TC yang terbelah antar `sourceTc`, pembagian asersi lintas spec dicatat di bagian berikut.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | Screening User List: Layout, Tab, Breadcrumb, Sort Default Name A-Z, Loading Skeleton, dan Tooltip Toolbar | FE+BE | 61 | 1–8, 25, 1043 |
| TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | Rendering Kolom User List: Badge Name, Position Kosong, Modified By, Last Update, Access, dan Popup Access | FE+BE | 37 | 14–22 |
| TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | Interaksi Baris User List: Klik Area Non-Name, Hover Name, Warna Toggle, Overlay Row Action, Fokus Keyboard, dan Navigasi ke User Detail | FE+BE | 37 | 11–13, 24, 26–28, 40 |
| TC-GS-USER-E2E-004-empty-state-client-baru-hanya-default-user | Empty State Client Baru: Hanya Baris Default User Tanpa Ilustrasi, Toggle dan Checkbox Disabled | FE+BE | 7 | 9 |
| TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | Guided Tooltip Halaman User: Isi 5 Step, Back, Next, Done, dan Navigasi Keyboard | FE+BE | 39 | 29–33, 36, 39 |
| TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar | Guided Tooltip Halaman User: Flag Seen, Skip, Done, Replay Tombol [?], dan Navigasi Keluar Tanpa Selesai | FE+BE | 34 | 34–35, 37–38 |
| TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | Resilience Baca User: Error Load User List, Modal Changelog, dan Tab System Log User Detail dengan Try Again | FE+BE | 43 | 23, 994–995, 1069–1070 |
| TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | Role Matrix: Visibilitas Menu User di Sidebar Global Settings dan Direct URL per Role | FE+BE | 32 | 41–46 |
| TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | Role Matrix Negatif: Kontrol User List dan User Detail untuk Read Only (Create, Checkbox, Aksi Tulis, Header, dan Tab Role Tidak Tersedia) | FE+BE | 58 | 47–48, 81, 1000, 1002, 1071 |
| TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | Role Matrix: Kontrol Baris User List untuk Aktor Total Control per Target (Normal, Default User, Self, Tier Total Control, Tier Read Only) | FE+BE | 40 | 49–53 |
| TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | Role Matrix: Kontrol Baris User List untuk Aktor Manage user and role (Full CRUD) per Target (Normal, Holder Biasa, Default User, Self, Tier Total Control, Tier Read Only) | FE+BE | 70 | 54–59 |
| TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor | Role Matrix: Default User sebagai Aktor atas Target Bertier (Total Control, Read Only), Target Normal, dan Baris Sendiri | FE+BE | 25 | 60–62, 996 |
| TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | Role Matrix: Kontrol User List untuk Holder Manage user and role Create-Only, Update-Only, Delete-Only, dan Read-Only role terhadap Target Normal | FE+BE | 23 | 63–66, 1004 |
| TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | Role Matrix Positif: Aksi Tulis Holder Scoped (Create-Only, Update-Only, Delete-Only) untuk Create, Edit, Toggle Active, Resend, Bulk Activate, Delete, dan Bulk Delete | FE+BE | 56 | 67–73 |
| TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | Role Matrix: Kontrol Header dan Section User Detail untuk Aktor Total Control dan Full CRUD terhadap Target Default User, Self, Tier Total Control, Tier Read Only, dan Normal | FE+BE | 140 | 74–80 |
| TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | Role Matrix Negatif: Reset Authenticator, Hover Avatar, dan Menu Header User Detail untuk Holder Full CRUD, Delete-Only, dan Create-Only | FE+BE | 31 | 997–999, 1003, 1072 |
| TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role | Role Matrix: Target Default User untuk Inline Edit Custom Field, Tab Role, dan Resend Confirmation Email oleh Total Control dan Full CRUD | FE+BE | 35 | 82, 1001, 1046–1047 |
| TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | Aksi pada Akun Sendiri: Edit dari Row Action dan Edit Profile, Kunci Access dan Temporary User, Resend Confirmation Email, Scan dan Unpair TAG, serta Edit Foto Profil | FE+BE | 64 | 83–84, 1029–1030, 1073–1074 |
| TC-GS-USER-E2E-019-isolasi-entitas-visibilitas-data-staff-distributor-dan-opsi-access-principal | Isolasi Entitas: User Client Lain Tidak Tampil, User List Distributor Tanpa Staff Partner, dan Opsi Access Create User Principal Hanya Admin Console dan Global Settings | FE+BE | 20 | 85–87 |
| TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas | Create User: Screening Popup, Opsi Access, Opsi Position dan Division dari Master Data, dan Fokus Terkunci | FE+BE | 41 | 88–90, 148 |
| TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | Create User: Validasi Required dan Batas 120 Karakter First Name, Last Name, Employee ID, dan Email | mock | 79 | 91–100 |
| TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | Create User: Validasi Emoji First Name dan Last Name, Format Email, Temporary Until, dan Custom Field Emergency Phone | FE+BE | 67 | 105–108, 110–111, 121–124, 158–159 |
| TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | Create User: Validasi Duplikat Email Lintas Client dan Employee ID Real-Time, Termasuk Trim Spasi dan Sensitivitas Huruf | FE+BE | 33 | 112, 114, 1031–1033 |
| TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access | Create User Sukses: Field Wajib Saja, Semua Field Opsional Terisi, Access Global Settings Saja, dan Access Fixed Asset + Supply Asset | FE+BE | 69 | 117–120 |
| TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | Create User: Trim Spasi Awal/Akhir First Name, Last Name, Employee ID, dan Email lewat Stay on this form | FE+BE | 39 | 101–104, 137 |
| TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | Create: nilai khusus, Temporary besok, reuse Email dan Employee ID milik user terhapus | FE+BE | 42 | 109, 113, 115–116, 125, 138 |
| TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | Create: foto profil (hover, file picker, kompres, batas ukuran, tutup tanpa Submit) | FE+BE | 41 | 126–130, 1040 |
| TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | Create: penutupan Popup, [Clear Field], backdrop, dan Unsaved Changes | mock | 46 | 139–143, 1005, 1062 |
| TC-GS-USER-E2E-029-create-saving-state-dan-klik-ganda-submit | Create: saving state tombol [Submit] dan klik ganda | FE+BE | 18 | 144–145 |
| TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir | Create: Master Data Count Limit, kuota gabungan Login + Non-Login, dan slot terakhir | FE+BE | 57 | 149–151, 986 |
| TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | Create: Position/Division/Custom Field dihapus atau di-rename sesi lain sebelum Submit | FE+BE | 45 | 153–157 |
| TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | Edit User: Screening Popup Pre-filled, Default User (Access Disabled dan Edit Position), Access Otomatis Produk Baru, dan Aksesibilitas Popup | FE+BE | 49 | 160–163, 240 |
| TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | Edit User: Validasi Required, Batas 120 Karakter Real-Time, dan Uncheck Semua Access Ditolak | FE+BE | 64 | 164–172 |
| TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | Edit User: Validasi Emoji, Duplikat Email dan Employee ID, dan Format Email Tidak Valid | FE+BE | 39 | 176–183 |
| TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | Edit User Sukses: No-Op, Trim Spasi, Happy Path Nama, Klik Ganda [Save], dan Saving State | FE+BE | 65 | 173–175, 184–185, 192–193 |
| TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | Edit User: [Clear Field], Backdrop, Reload, Dialog Unsaved Changes (Cancel dan Leave), serta Penutupan Popup Tanpa Perubahan | mock | 41 | 186–191, 1007, 1063 |
| TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | Edit User: Temporary User (Set, Uncheck, Batas Tanggal Hari Ini dan Kemarin, Tanggal Kosong, dan Temporary-Expired) | FE+BE | 50 | 198–204 |
| TC-GS-USER-E2E-038-edit-foto-profil-hapus-ganti-dan-tutup-tanpa-save | Edit User: Foto Profil (Tutup Tanpa Save, Ganti Foto Auto-Transition, dan Hapus Ditandai Sampai Save) | FE+BE | 40 | 205–207 |
| TC-GS-USER-E2E-039-edit-tambah-access-dan-produk-kehilangan-subscription | Edit User: Tambah Access Produk Baru Tanpa Dialog dan Produk Kehilangan Subscription | FE+BE | 23 | 196–197 |
| TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | Edit: Position, Division, dan Custom Field Dropdown atau Multi-Dropdown Dihapus atau Di-rename Sesi Lain sebelum Save | FE+BE | 55 | 213–217 |
| TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | Pairing TAG di Popup Create dan Edit: Scan Ditolak, Scan Valid Verified, Unpair, Cancel Unpair, dan Re-pair | FE+BE | 65 | 131–136, 209–211 |
| TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade | Gating Plan Starter: Field User TAG Tidak Dirender di Popup Create, Popup Edit, dan Detail, serta Downgrade Mencabut Pairing TAG Tanpa Log | FE+BE | 33 | 152, 212, 323–324 |
| TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | Remove Access Produk: Dialog Peringatan Aset atau Approval (Screening, Cancel, Dua Produk, Lanjut Mencabut) dan Tanpa Dialog untuk Produk Tanpa Aset | FE+BE | 52 | 218–222, 1008 |
| TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | Remove Access Global Settings: Dialog Role & Permission untuk Tier dan Holder N Role, Pencabutan Tier, Relasi Represented By Tetap, dan User Basic Tanpa Dialog | FE+BE | 53 | 223–227, 1009 |
| TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | Edit Email User Activated: Pending Email Change, Email Pending Dicadangkan, Edit Email Ulang, dan Dialog Cancel Pending Email Change | FE+BE | 84 | 228–230, 233–235, 1080, 1082 |
| TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password | Konfirmasi Email via Link: Email Resmi Pindah, Link Reset Password Lama Tidak Berlaku, Link Bentrok dan Link Kedaluwarsa Ditolak Tanpa Mengubah Email Pending | FE+BE | 29 | 231–232, 968, 1081 |
| TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | Toggle Active Single: Dialog Deactivate dan Activate, Cancel, Posisi Toggle Per-Produk, Modified By, dan Header Detail | FE+BE | 78 | 241–242, 244, 246–248, 250–251, 1087 |
| TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | Reactivate Temporary User: Dialog, Cancel, Validasi Tanggal Kosong, Hari Ini, dan Kemarin, Extend Period, Make Permanent, dan Header Detail | FE+BE | 61 | 252–258, 1039 |
| TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | Temporary Auto-Inactive: Aktif sampai 23.59, Job 00.00, Zona Waktu Client, Non-Login User, Modified By System, dan Pencatatan Log Auto-Deactivate | FE+BE | 61 | 259–260, 907, 1012–1014, 1088 |
| TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | Delete User Single: Screening Dialog, Cancel, Cascade Aset dan Approval, Non-Login User, TAG, dan Foto, Klik Ganda, serta dari Header Detail | FE+BE | 79 | 261–270, 272 |
| TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | Bulk Action Bar: Screening, Counter, Checkbox Header, Select All Lintas Halaman, dan Retensi Seleksi | FE+BE | 52 | 274–281 |
| TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | Opsi Bulk Action per Kombinasi Status Seleksi: Activate, Deactivate, Delete, dan Resend Activation Email | FE+BE | 44 | 285–290, 1045 |
| TC-GS-USER-E2E-053-bulk-selection-limit-checkbox-dan-select-all | Selection Limit Bulk Action: Checkbox Melewati Batas Disabled, Select All Dibatasi dengan Toast Error Persist, dan Nilai Dibaca Live | FE+BE | 34 | 282–284 |
| TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | Bulk Activate dan Deactivate: Dialog Satu Daftar dan Dua Kelompok, Baris yang Di-skip, Toast Ringkasan, Collapse ke Dialog Single, Cancel, dan Reset Seleksi | FE+BE | 97 | 291–293, 295–298, 304, 1027, 1035–1036 |
| TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel | Bulk Delete: Cancel Tidak Menghapus, Dialog Gabungan Aset dan Approval, NLU Terdampak, dan Semua Berhasil | FE+BE | 32 | 299–301, 1028 |
| TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | Resend Activation/Confirmation Email: Cooldown 60 Detik dengan Jam Server dan Browser, Tombol Resend di Detail, Edit Email Pending Activation, dan Bulk Resend dengan Baris Cooldown Di-skip | FE+BE | 95 | 238–239, 302–303, 305–307, 309, 311–312 |
| TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | User Detail: Sub-section User TAG (Screening, Penolakan Scan TAG-NEW-0001, TAG-4F7K2XQ9, dan TAG-OBJ-0001, Re-pair, Unpair, dan Scan TAG-USR-0001 Berhasil) | FE+BE | 40 | 313–319, 321 |
| TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | User Detail: Reset Authenticator (Screening Enrolled dan Not enrolled yet, Guard Default User dan Akun Sendiri, Dialog, Cancel, Reset Berhasil, dan Holder Update-Only) | FE+BE | 42 | 325–329, 332–334 |
| TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | User Detail: Foto Profil (Hover Avatar, Dialog Remove Photo dan Cancel, Upload, Ganti ke Recycle Bin, Berkas Korup Ditolak, Hapus dengan Klik Ganda, dan Hapus dengan Deleter Admin) | FE+BE | 65 | 335–338, 340–341, 343, 1017, 1041 |
| TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | User Detail: Section Custom Fields (Screening, Collapse, Format Phone, Inline Edit Simpan, Batal, Multi-aktif, Validasi Required dan Min. 4 Characters, Saving State, Akun Sendiri, dan Holder Update-Only) | FE+BE | 75 | 344–350, 352, 354–355, 1077 |
| TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | User Detail: Header, Badge Status, User Type, Info Temporary, Pending Email Change, Tab Role Aktif Default, Edit Profile, serta Retensi State User List lewat Back Browser dan F5 | FE+BE | 74 | 273, 356–366, 1018, 1054 |
| TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi | User Detail: Product Selector (Default Global Settings, Opsi Fixed Asset dan Supply Asset, Produk yang Pernah Dicabut, Hidden bagi Aktor tanpa Hak Read, dan Navigasi Penuh ke Fixed Asset) | FE+BE | 28 | 367–370 |
| TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | User Detail Tab Role: Screening User Non-Tier, Role Belum Di-assign, Banner Total Control dan Read Only, Read Baseline Disabled, Checkbox Akun Sendiri Disabled, Urutan Baris Tetap, dan Column Visibility | FE+BE | 57 | 371–375, 382, 871–872, 1051 |
| TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | User Detail Tab Role: Auto-save per Cell, Assign Role, Dialog Remove Access (Cancel dan Remove), dan Auto-revert Tier Total Control dan Read Only, serta Edit oleh Holder Update-Only | FE+BE | 55 | 376–377, 379–381, 383, 1020 |
| TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | User Detail Tab Responsibilities: Screening Client FAMS Aktif, Empty State Global, Sinkron Modul Sumber, Client tanpa Subscription FAMS, dan Entitas Principal | FE+BE | 39 | 384–386, 399, 1019 |
| TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | Resilience Tulis User: Create, Edit, dan Delete Gagal 5xx dengan Form Dipertahankan, Tanpa Foto Yatim dan Tanpa Perubahan Foto Akibat Rollback, serta Retry Create setelah Timeout Tidak Menggandakan User | FE+BE | 78 | 146–147, 194, 208, 271, 987 |
| TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | Resilience Tulis User: Toggle Active, Bulk Activate dan Deactivate, Resend Activation dan Confirmation Email, serta Bulk Resend Gagal 5xx Total atau Sebagian dengan Cooldown Tidak Dimulai | FE+BE | 112 | 245, 249, 294, 308, 310, 1037–1038, 1048–1050 |
| TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | Resilience Tulis User: Cancel Pending Email Change, Pair dan Unpair TAG, Reset Authenticator, Ganti dan Hapus Foto Avatar, Inline Edit Custom Field, dan Auto-Save Tab Role Gagal 5xx dengan State Dikembalikan | FE+BE | 72 | 236, 320, 322, 330, 339, 342, 351, 378 |
| TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | Resilience Download User: Toast Error dengan Nama Berkas pada User List, Modal Changelog User, Modal Changelog User > Role, serta Tab Changelog, System Log, User Log, dan Non-Login User Detail | FE+BE | 53 | 460, 1055–1060 |
| TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | Multi-Konteks Dua Admin: Email Kembar saat Create, Last-Write-Wins pada Edit, Toggle, dan Inline Custom Field, Race Cancel Change, serta Record Dihapus Sesi Lain pada Edit, Toggle, Delete, dan Bulk Delete | FE+BE | 97 | 195, 237, 353, 985, 1006, 1010–1011, 1015–1016 |
| TC-GS-USER-E2E-071-user-list-screening-dan-search | User List: State Kosong dan Search (Reveal, Clear, Trim, Substring per Kolom, Kolom Tanggal, Active Exact, Kolom Hidden) | FE+BE | 120 | 10, 413–420, 1034 |
| TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | User List: Filter Panel (Screening Field, Opsi dari Tabel, Multi-Select, OR, Pencarian Dropdown, Chip, Rentang Tanggal, dan AND) | FE+BE | 173 | 421–429 |
| TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | User List: Kombinasi Search dan Filter (Irisan, Clear dengan Sort Aktif, Filter Kolom Hidden, Nol Baris, Custom Field, dan Create Tidak Cocok Filter) | FE+BE | 90 | 430–434, 463–464 |
| TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | User List: Sort 3-State per Kelas Kolom, Pagination, Kombinasi Search+Filter+Sort+Pagination, Badge Temporary User, dan Nilai Phone | FE+BE | 137 | 435–440, 458–459, 1061, 1068, 1078 |
| TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | User List: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin per Kolom, Reset to Default, Tutup Tanpa Simpan, Kolom Terakhir, dan Batas 3 Pin) | mock | 385 | 441–452 |
| TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | User List: Download CSV/XLSX (Menu, Isi Berkas Seluruh Baris, Cakupan Search, Kolom Hidden, Nilai Kosong, Access/Active, dan Nilai Phone) | FE+BE | 58 | 453–457, 461, 1079 |
| TC-GS-USER-E2E-077-user-list-download-lebih-dari-5000-baris-background-job | User List: Download Lebih dari 5.000 Baris Berjalan sebagai Background Job (Toast Informasional dan Notifikasi dengan Tombol Download) | FE+BE | 7 | 462 |
| TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | Modal Changelog User: Screening, State Kosong, dan Search Substring, Trim, Kolom Non-Searchable, serta Kolom Hidden | FE+BE | 82 | 465–476 |
| TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | Modal Changelog User: Filter Panel (Opsi Dropdown, Multi-Select per Field, Logika OR, Search Dropdown, Chip, Rentang Date, dan Logika AND) | FE+BE | 83 | 477–485 |
| TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Modal Changelog User: Kombinasi Search dan Filter, Clear Filter saat Search dan Sort Aktif, Filter Kolom Hidden, dan Nol Baris | FE+BE | 47 | 486–490 |
| TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | Modal Changelog User: Sort 3-State Semua Kolom, Pagination, dan Kombinasi Search, Filter, Sort, serta Pagination | FE+BE | 69 | 491–493, 508–509 |
| TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | Modal Changelog User: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin/Unpin, Reset to Default, Guard Kolom Terakhir, dan Batas 3 Pin) | FE+BE | 206 | 494–502 |
| TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | Modal Changelog User: Download CSV dan XLSX (Isi Berkas Seluruh Data, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 29 | 503–507 |
| TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | Modal Changelog Role: screening, state kosong, dan Search | FE+BE | 74 | 510–517, 1053 |
| TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | Modal Changelog Role: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND) | FE+BE | 79 | 518–526 |
| TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Modal Changelog Role: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris | FE+BE | 51 | 527–531 |
| TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | Modal Changelog Role: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination | FE+BE | 64 | 532–534, 549–550 |
| TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | Modal Changelog Role: Setup Column (overlay, popup, hide, reorder, pin, reset, guard) | FE+BE | 193 | 535–543 |
| TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | Modal Changelog Role: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong) | FE+BE | 27 | 544–548 |
| TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | Tab Changelog Detail: Screening, State Kosong, dan Search | FE+BE | 71 | 405, 551–557 |
| TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | Tab Changelog Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND) | FE+BE | 69 | 558–566 |
| TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Tab Changelog Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris | FE+BE | 45 | 567–571 |
| TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | Tab Changelog Detail: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination | FE+BE | 77 | 572–574, 589–590 |
| TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | Tab Changelog Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, dan Guard) | FE+BE | 196 | 575–583 |
| TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | Tab Changelog Detail: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 32 | 406, 584–588 |
| TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | Tab System Log Detail: Screening, Empty State, dan Search pada Kolom Searchable, Kolom Date, Kolom Hidden, serta No Results | FE+BE | 86 | 407, 591–597, 1042 |
| TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | Tab System Log Detail: Filter Panel (Field, Opsi Dropdown, Multi-Select, OR, Search Dropdown, Chip, Rentang Date, dan AND) | FE+BE | 77 | 598–606 |
| TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Tab System Log Detail: Kombinasi Search dan Filter (Irisan, Clear Filter, Filter Kolom Hidden, dan Nol Baris) | FE+BE | 51 | 607–611 |
| TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | Tab System Log Detail: Sort 3-State (Date, Kolom Teks, Old/New Value), Pagination, dan Kombinasi Search, Filter, Sort, Pagination | FE+BE | 63 | 612–614, 629–630 |
| TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | Tab System Log Detail: Setup Column (Overlay, Popup, Guard Kolom Terakhir, Maksimal 3 Pin, Tutup dengan X, Hide/Unhide, Reorder, Pin/Unpin, dan Reset to Default) | FE+BE | 181 | 615–623 |
| TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | Tab System Log Detail: Download CSV/XLSX (Nama Berkas, Seluruh Baris, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 44 | 408, 624–628 |
| TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | Tab User Log Detail: Screening, Device Tidak Terparse, Search, dan Empty State | FE+BE | 72 | 409, 411–412, 631–637 |
| TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | Tab User Log Detail: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang Tanggal, dan AND) | FE+BE | 93 | 638–646 |
| TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Tab User Log Detail: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris | FE+BE | 77 | 647–651 |
| TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | Tab User Log Detail: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination | FE+BE | 78 | 652–654, 669–670 |
| TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | Tab User Log Detail: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Tutup, dan Guard) | FE+BE | 226 | 655–663 |
| TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | Tab User Log Detail: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 43 | 410, 664–668 |
| TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | Tab Non-Login User Detail: screening, state kosong, dan Search | FE+BE | 112 | 400–403, 671–677 |
| TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | Tab Non-Login User Detail: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND) | FE+BE | 109 | 678–686 |
| TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Tab Non-Login User Detail: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris | FE+BE | 71 | 687–691 |
| TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | Tab Non-Login User Detail: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination | FE+BE | 101 | 692–696, 714–715 |
| TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | Tab Non-Login User Detail: Setup Column (overlay, popup, hide, reorder, pin, reset, guard) | FE+BE | 343 | 697–708 |
| TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | Tab Non-Login User Detail: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong) | FE+BE | 46 | 404, 709–713 |
| TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | Sub-tab Borrowed Assets: screening, state kosong, dan Search | FE+BE | 87 | 387–388, 716–721 |
| TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | Sub-tab Borrowed Assets: Filter Panel (opsi, multi-select, OR, dropdown search, chip, rentang, AND) | FE+BE | 97 | 722–730 |
| TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Sub-tab Borrowed Assets: kombinasi Search dan Filter, Clear, filter kolom hidden, nol baris | FE+BE | 59 | 731–735 |
| TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | Sub-tab Borrowed Assets: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination | FE+BE | 80 | 736–738, 753–754 |
| TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | Sub-tab Borrowed Assets: Setup Column (overlay, popup, hide, reorder, pin, reset, guard) | FE+BE | 287 | 739–747 |
| TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | Sub-tab Borrowed Assets: Download CSV/XLSX (isi berkas, cakupan Search/Filter, kolom hidden, nilai kosong) | FE+BE | 43 | 389, 748–752 |
| TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | Sub-tab Assigned Assets: Screening, Empty State, dan Search (Reveal, Clear, Trim, Kolom Searchable, dan Kolom Hidden) | FE+BE | 76 | 390–391, 755–760 |
| TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | Sub-tab Assigned Assets: Filter Panel (Opsi, Multi-Select, OR, Pencarian Dropdown, Chip, dan AND) | FE+BE | 77 | 761–768 |
| TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Sub-tab Assigned Assets: Kombinasi Search dan Filter, Clear Filter, Filter Kolom Hidden, dan Nol Baris | FE+BE | 60 | 769–773 |
| TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi | Sub-tab Assigned Assets: Sort 3-State, Pagination, dan Kombinasi Search, Filter, Sort, Pagination | FE+BE | 76 | 774–775, 790–791 |
| TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | Sub-tab Assigned Assets: Setup Column (Overlay, Popup, Hide/Unhide, Reorder, Pin, Reset to Default, dan Guard) | FE+BE | 150 | 776–784 |
| TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | Sub-tab Assigned Assets: Download CSV/XLSX (Nama Berkas, Isi, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 44 | 392, 785–789 |
| TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | Sub-tab Pending Approvals: Screening, State Kosong, dan Search | FE+BE | 86 | 393–394, 792–797 |
| TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | Sub-tab Pending Approvals: Filter Panel (Opsi, Multi-Select, OR, Dropdown Search, Chip, Rentang, AND) | FE+BE | 99 | 798–806 |
| TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Sub-tab Pending Approvals: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris | FE+BE | 72 | 807–811 |
| TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi | Sub-tab Pending Approvals: Sort 3-State, Pagination, dan Kombinasi Search+Filter+Sort+Pagination | FE+BE | 56 | 812–813, 828–829 |
| TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | Sub-tab Pending Approvals: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard) | FE+BE | 156 | 814–822 |
| TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | Sub-tab Pending Approvals: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, Nilai Kosong) | FE+BE | 44 | 395, 823–827 |
| TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | Sub-tab Pending Tasks: Screening, State Kosong, dan Search | FE+BE | 99 | 396–397, 830–836 |
| TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | Sub-tab Pending Tasks: Filter Panel (Opsi, Multi-select, OR, Dropdown Search, Chip, Rentang, AND) | FE+BE | 120 | 837–846 |
| TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | Sub-tab Pending Tasks: Kombinasi Search dan Filter, Clear, Filter Kolom Hidden, dan Nol Baris | FE+BE | 66 | 847–851 |
| TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | Sub-tab Pending Tasks: Sort 3-state, Pagination, dan Kombinasi Search, Filter, Sort, dan Pagination | FE+BE | 79 | 852–854, 869–870 |
| TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | Sub-tab Pending Tasks: Setup Column (Overlay, Popup, Hide, Reorder, Pin, Reset, Guard) | FE+BE | 175 | 855–863 |
| TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | Sub-tab Pending Tasks: Download CSV/XLSX (Isi Berkas, Cakupan Search, Kolom Hidden, dan Nilai Kosong) | FE+BE | 43 | 398, 864–868 |
| TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | Pencatatan Create, Edit Position, Edit Photo, Edit Represented By, dan Delete User di Modal Changelog User, Tab Changelog Detail, Tab System Log, dan Activity Log | FE+BE | 94 | 873–877 |
| TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | Pencatatan Changelog User: Seed Default User, Edit Multi-Field Menjadi Dua Baris, Edit Position dengan Remove Access, Inline Edit Custom Field, Set Temporary User pada Perubahan Temporary Until, Snapshot Beku dan Rename Position, Hapus Foto dari Avatar dan File Manager, serta Delete User dengan TAG | FE+BE | 92 | 909–911, 916–918, 921–922, 1044, 1076 |
| TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | Pencatatan Activate dan Deactivate (Status Global dan Fixed Asset), Set dan Remove Temporary User, serta Reactivate Temporary Extend dan Make Permanent di Changelog, System Log, dan Activity Log | FE+BE | 121 | 878–881, 892–893, 912–913 |
| TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | Pencatatan Resend Activation Email, Resend Confirmation Email, Pending Email Change, Cancel Email Change, Email Updated, dan Email Confirmed di Changelog, System Log, dan Activity Log | FE+BE | 97 | 882–883, 894–896, 908 |
| TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | Pencatatan Add Access, Remove Access, Remove Access Global Settings, Pair TAG, Unpair TAG, dan Reset Authenticator di Changelog, System Log, dan Activity Log | FE+BE | 99 | 884–887, 897, 924 |
| TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in | Pencatatan Assign Handheld, Check Out Handheld, Check In Handheld, dan Unassign Handheld di Changelog, System Log, dan Activity Log | FE+BE | 63 | 888–891 |
| TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | Pencatatan Assign dan Remove Access Level, Permission Individual, Auto-Revert Tier, dan Assign dari Tab Role di Changelog, System Log, dan Activity Log | FE+BE | 170 | 898–906, 1052 |
| TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove | Pencatatan Modal Changelog User > Role: Edit Permission, Assign Role, dan Remove Role pada Satu User | FE+BE | 20 | 926–928 |
| TC-GS-USER-E2E-146-pencatatan-bulk-resend-dan-bulk-delete-satu-baris-per-user | Pencatatan Bulk Resend Activation Email dan Bulk Delete: Satu Baris Log per User yang Diproses | FE+BE | 17 | 914–915 |
| TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | Absence Log: Edit No-Op, Aksi Lintas User, Pair TAG dari Create, Product Selector, Entry Per-Role Assign dan Remove Tier, Reset Authenticator, dan Aksi Admin Console Tidak Menulis Log | FE+BE | 99 | 919–920, 923, 925, 929–932, 942–943 |
| TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | Tab User Log: Login Success dan Failed, Logout, Change Password Success dan Failed, Reset Password Success dan Failed, serta Session started dan ended | FE+BE | 63 | 933–941 |
| TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked | Tab User Log: Note Lock Change Password 15 Menit, 1 Jam, Perlu Reset, dan Account locked | FE+BE | 110 | 1083–1086 |
| TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | Sinkron Position dan Division (Create, Edit, Delete) ke Form dan List User | FE+BE | 45 | 944–949 |
| TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | Sinkron Custom Field (Create, Deactivate, Activate, Delete, Ubah Data Type, Required) ke User Existing | FE+BE | 69 | 950–955 |
| TC-GS-USER-E2E-152-sinkron-custom-field-deactivate-dan-delete-saat-kolom-curated-dan-filter-aktif | Sinkron Custom Field Deactivate, Activate, dan Delete saat Kolom Curated Tampil dan Filter Aktif di User List | FE+BE | 66 | 1064–1066 |
| TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | Sinkron ke Fixed Asset, Admin Console, My Profile, All Tags, dan File Manager | FE+BE | 55 | 958–964 |
| TC-GS-USER-E2E-154-format-tanggal-general-settings-di-user-list-changelog-dan-detail | Format Tanggal General Settings di User List, Modal Changelog, dan User Detail | FE+BE | 28 | 965–967 |
| TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | Defense-in-Depth: Request Langsung Tanpa Wewenang Ditolak 403, Payload Script, dan Karakter Khusus Search | FE+BE | 69 | 969–983, 1067, 1075 |
| TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | State Tenant: Write-Lockdown Client Suspended dan Expired | FE+BE | 53 | 984, 1021–1026 |
| TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses | Siklus Aktivasi dan Login: Status Activated, Link Kedaluwarsa, Effective Active, dan Deactivate Memutus Login | FE+BE | 39 | 988–991 |
| TC-GS-USER-E2E-158-isolasi-subtab-login-non-login-dan-persistensi-setup-column | Isolasi Sub-tab Login User dan Non-Login User serta Persistensi Setup Column Terpisah | FE+BE | 20 | 992–993 |
| TC-GS-USER-E2E-159-multi-konteks-sesi-user-target-setelah-aksi-admin-deactivate-dan-reset-authenticator | Multi-Konteks: Sesi Browser User Target Berakhir Setelah Admin Deactivate dan Tetap Berjalan Setelah Admin Reset Authenticator | FE+BE | 23 | 243, 331 |

## Pembagian TC lintas spec

- **TC-GS-USER-897 butir f** (Reset Authenticator tidak tercatat di Tab User Log): TC-897 di spec `142`; asersi absence lewat TC-942 di spec `147` (kelas g, aksi Reset Authenticator dan baseline sendiri).
- **TC-GS-USER-905 dan 906 (klausa tidak tampil di Modal Changelog User > Role)** di spec `144` dan **TC-GS-USER-914 (tidak ada baris untuk Mike Tan)** di spec `146`: ditulis sebagai `Verifikasi` berbaseline di spec asal dengan butir `P-1` di Notes; TC-nya tidak ada di `sourceTc` spec `147`.
- **TC-GS-USER-244 dan 907**: klausa log berbaseline dengan `P-1` di spec `047` dan `049`; spec absence `147` tidak memuat aksi untuk TC itu.
- **TC-GS-USER-919, 920, 923, 925, 929–932, 942, 943**: asersi absence di spec `147`; spec asal (`138`, `139`, `142`) mencatat rujukan di Notes dan asersi "tepat N baris" berbaseline.
- **TC-GS-USER-1043** (Modified By Default User seed `System`) di spec `001` dan **TC-GS-USER-1044** (baris Changelog paling awal `Create` oleh `System`) di spec `139`: dijalankan sebelum spec yang mengedit Default User (`017`, `032`); suite berjalan serial.
- **TC-GS-USER-243 dan 331** (sesi browser user target setelah admin Deactivate / Reset Authenticator) seluruhnya di spec `159` (kelas c, hasil di jendela kedua diasersi); spec `047` dan `058` mencatat rujukan di Notes.
- **TC-GS-USER-462** (Download lebih dari 5.000 baris) berdiri sendiri di spec `077` (kelas e, seed volume).

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec (jumlah spec pemakai): `AC_STAFF_PASSWORD` (1), `GS_BASIC_PASSWORD` (1), `GS_CLIENTB_TC_PASSWORD` (2), `GS_CLIENTEXP_TC_PASSWORD` (1), `GS_CLIENTSUSP_TC_PASSWORD` (1), `GS_CREATE_PASSWORD` (3), `GS_DEFAULT_PASSWORD` (3), `GS_DELETE_PASSWORD` (3), `GS_DISTRIBUTOR_TC_PASSWORD` (1), `GS_FULLCRUD_PASSWORD` (24), `GS_LIMIT_TC_PASSWORD` (1), `GS_NOFAMS_TC_PASSWORD` (1), `GS_NOSUPPLY_TC_PASSWORD` (1), `GS_PLANGROWTH_TC_PASSWORD` (1), `GS_PLANSTARTER_TC_PASSWORD` (1), `GS_PRINCIPAL_TC_PASSWORD` (4), `GS_READ_PASSWORD` (2), `GS_RO_PASSWORD` (3), `GS_TC2_PASSWORD` (6), `GS_TC_PASSWORD` (157), `GS_UPDATE_PASSWORD` (6), `USER_PASSWORD` (18), `USER_PASSWORD_NEW` (7), `USER_PASSWORD_WRONG` (2). Nama baru milik suite ini (`GS_DEFAULT_PASSWORD`, `GS_FULLCRUD_PASSWORD`, `GS_BASIC_PASSWORD`, `GS_NOFAMS_TC_PASSWORD`, `GS_NOSUPPLY_TC_PASSWORD`, `AC_STAFF_PASSWORD`, `USER_PASSWORD`, `USER_PASSWORD_NEW`, `USER_PASSWORD_WRONG`) sudah didaftarkan di `spectra.config.ts` dan `.env.example`; password aktual diisi tim FE.
- Akun di luar Tabel Pre-setup TC User (disediakan tim FE): Total Control admin kedua (`GS_TC2_PASSWORD`), Client B, Principal, Distributor, Client Limit, Client Suspended, Client Expired, Client plan Starter dan Growth, Client tanpa FAMS, Client tanpa Supply Asset, Admin FAMS, staff Principal Admin Console, serta Default User client baru.
- Seeding lewat API tanpa endpoint di TC, PRD, atau LLD: user dan Non-Login User milik spec (suffix `{runId}-NNN`), data Responsibilities FAMS (borrowed, assigned, approval, task), Handheld, tier dan role individual, Custom Field, Master Data, event User Log dengan IP dan User-Agent tertentu, foto, dan populasi volume (5.001 user).
- Kemampuan teknis: intercept jaringan (5xx, timeout, tahan respons, download gagal), dua sesi browser, sesi API admin kedua, mail-catcher, manipulasi jam server dan jam browser, picu job auto-deactivate, simulasi scan TAG, mengubah System Limits (Master Data Count Limit, Selection Limit), plan dan status Client, General Settings, membaca dan menyetel flag Guided Tooltip `gs-user`, menangkap dan membaca berkas CSV/XLSX, drag and drop, viewport sempit, dan membaca atau menghapus preferensi Setup Column di browser.
- Environment automation terisolasi dari aktivitas pengguna lain dan suite berjalan serial (`parallel: false`); spec yang menghapus data (Delete, Bulk Delete, Remove Access) dijalankan sesudah spec lain.
- Baris Pre-setup yang terpaksa diubah lalu dipulihkan (Last Update dan Modified By tidak dapat dipulihkan): Default User (spec `017`, `032`), John Doe (spec `041`, `057`), Siti Nurhaliza (spec `018` Position, pending email, TAG; spec `060` Blood Type), foto Fajar Nugroho (spec `018`), opsi Custom Field `Blood Type` dan `Skills` (spec `031`, opsi bersuffix). State global yang diubah dan dipulihkan: subscription Client (spec `020`, `039`), Required `Emergency Phone` (spec `024`, `025`); diterima atas keputusan user 2026-10-21 (S-06: pulihkan dan catat efeknya).

## Temuan yang masih terbuka

- Spec melewati batas ±35 langkah (134 spec), masing-masing dengan alasan di Notes (satu layar, satu kelas, blok berdiri sendiri; langkah menjadi banyak karena satu `Verifikasi` per klausa Expected, S-01, dan siklus Save + F5 per kolom di spec Setup Column). Terbesar: 075 (385), 112 (343), 118 (287), 106 (226), 082 (206), 094 (196), 088 (193), 100 (181), 136 (175), 072 (173), 144 (170), 130 (156), 124 (150), 015 (140), 074 (137), 140 (121), 071 (120), 133 (120), 067 (112), 108 (112). Diterima atas keputusan user 2026-10-21 (alasan sah di Notes; tidak dipecah).
- Spec Setup Column tiap permukaan (075, 082, 088, 094, 100, 106, 112, 118, 124, 130, 136) mengulang siklus Save dan F5 per kolom; pemecahan per aksi (hide, reorder, pin) menunggu keputusan.
- TC "uncheck lalu check, Save, F5" (Setup Column) tidak menghasilkan konfigurasi yang berbeda dari default; spec memakai urutan hide, Save, F5, lalu unhide dan mencatat tafsirannya di Notes.
- TC-462 meminta toast informasional dan notifikasi `[Download]` untuk ekspor >5.000 baris, sedangkan `error-handling-convention.md` §10.1 menyatakan tidak ada job background; spec `077` mengikuti TC.
- TC memakai user Pre-setup (Dewi Lestari, John Doe, Ahmad Fauzi, Joko Susilo) sebagai target tulis atau pemilik log; spec memakai padanan seed bersuffix (S-06). Nilai Expected TC yang memuat nama Pre-setup diganti nama bersuffix.
- Custom Field `Emergency Phone` (Required, Pre-setup No. 24) tidak diisi di sebagian TC Create/Edit; spec `024` dan `025` mensyaratkan Required dimatikan, spec lain mengisinya.
- Mekanisme yang tidak didefinisikan TC, PRD, atau LLD ditulis sebagai kemampuan "disediakan tim FE/BE" tanpa mengarang endpoint (daftar di bagian Kebutuhan lingkungan).
- Post Condition tanpa langkah observasi tidak diasersi; dicatat di "Temuan untuk QA" tiap spec.
- Header kolom aksi bernama `Actions (⋯)` di sebagian TC dan `Column Visibility (⋯)` di TC lain; spec memakai `Column Visibility (⋯)`.
- Spec `042` (gating plan Starter, downgrade plan): kemampuan mengubah plan ditulis "disediakan tim FE" sesuai S-13; tetap `coverage.web: automated`.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-USER-1 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-2 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-3 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-4 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-5 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-6 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-7 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-8 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-9 | TC-GS-USER-E2E-004-empty-state-client-baru-hanya-default-user | FE+BE |
| TC-GS-USER-10 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-11 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-12 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-13 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-14 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-15 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-16 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-17 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-18 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-19 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-20 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-21 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-22 | TC-GS-USER-E2E-002-rendering-kolom-user-list-badge-modified-by-last-update-dan-popup-access | FE+BE |
| TC-GS-USER-23 | TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | FE+BE |
| TC-GS-USER-24 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-25 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-26 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-27 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-28 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-29 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-30 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-31 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-32 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-33 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-34 | TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-USER-35 | TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-USER-36 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-37 | TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-USER-38 | TC-GS-USER-E2E-006-guided-tooltip-flag-skip-done-replay-dan-navigasi-keluar | FE+BE |
| TC-GS-USER-39 | TC-GS-USER-E2E-005-guided-tooltip-konten-navigasi-dan-keyboard | FE+BE |
| TC-GS-USER-40 | TC-GS-USER-E2E-003-interaksi-baris-user-list-klik-name-hover-toggle-row-action-dan-fokus-keyboard | FE+BE |
| TC-GS-USER-41 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-42 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-43 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-44 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-45 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-46 | TC-GS-USER-E2E-008-role-matrix-visibilitas-menu-user-dan-direct-url | FE+BE |
| TC-GS-USER-47 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-48 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-49 | TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | FE+BE |
| TC-GS-USER-50 | TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | FE+BE |
| TC-GS-USER-51 | TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | FE+BE |
| TC-GS-USER-52 | TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | FE+BE |
| TC-GS-USER-53 | TC-GS-USER-E2E-010-role-matrix-kontrol-baris-aktor-total-control-per-target | FE+BE |
| TC-GS-USER-54 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-55 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-56 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-57 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-58 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-59 | TC-GS-USER-E2E-011-role-matrix-kontrol-baris-aktor-full-crud-per-target | FE+BE |
| TC-GS-USER-60 | TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor | FE+BE |
| TC-GS-USER-61 | TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor | FE+BE |
| TC-GS-USER-62 | TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor | FE+BE |
| TC-GS-USER-63 | TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | FE+BE |
| TC-GS-USER-64 | TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | FE+BE |
| TC-GS-USER-65 | TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | FE+BE |
| TC-GS-USER-66 | TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | FE+BE |
| TC-GS-USER-67 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-68 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-69 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-70 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-71 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-72 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-73 | TC-GS-USER-E2E-014-role-matrix-positif-aksi-tulis-holder-scoped | FE+BE |
| TC-GS-USER-74 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-75 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-76 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-77 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-78 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-79 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-80 | TC-GS-USER-E2E-015-role-matrix-detail-kontrol-header-dan-section-per-target | FE+BE |
| TC-GS-USER-81 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-82 | TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role | FE+BE |
| TC-GS-USER-83 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-84 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-85 | TC-GS-USER-E2E-019-isolasi-entitas-visibilitas-data-staff-distributor-dan-opsi-access-principal | FE+BE |
| TC-GS-USER-86 | TC-GS-USER-E2E-019-isolasi-entitas-visibilitas-data-staff-distributor-dan-opsi-access-principal | FE+BE |
| TC-GS-USER-87 | TC-GS-USER-E2E-019-isolasi-entitas-visibilitas-data-staff-distributor-dan-opsi-access-principal | FE+BE |
| TC-GS-USER-88 | TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas | FE+BE |
| TC-GS-USER-89 | TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas | FE+BE |
| TC-GS-USER-90 | TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas | FE+BE |
| TC-GS-USER-91 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-92 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-93 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-94 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-95 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-96 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-97 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-98 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-99 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-100 | TC-GS-USER-E2E-021-create-validasi-required-dan-batas-karakter | mock |
| TC-GS-USER-101 | TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | FE+BE |
| TC-GS-USER-102 | TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | FE+BE |
| TC-GS-USER-103 | TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | FE+BE |
| TC-GS-USER-104 | TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | FE+BE |
| TC-GS-USER-105 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-106 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-107 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-108 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-109 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-110 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-111 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-112 | TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | FE+BE |
| TC-GS-USER-113 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-114 | TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | FE+BE |
| TC-GS-USER-115 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-116 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-117 | TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access | FE+BE |
| TC-GS-USER-118 | TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access | FE+BE |
| TC-GS-USER-119 | TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access | FE+BE |
| TC-GS-USER-120 | TC-GS-USER-E2E-024-create-sukses-field-wajib-semua-field-dan-variasi-access | FE+BE |
| TC-GS-USER-121 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-122 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-123 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-124 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-125 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-126 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-127 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-128 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-129 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-130 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-131 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-132 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-133 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-134 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-135 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-136 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-137 | TC-GS-USER-E2E-025-create-trim-spasi-first-last-employee-id-dan-email-via-stay-on-form | FE+BE |
| TC-GS-USER-138 | TC-GS-USER-E2E-026-create-nilai-khusus-employee-id-temporary-besok-dan-reuse-email-user-terhapus | FE+BE |
| TC-GS-USER-139 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-140 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-141 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-142 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-143 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-144 | TC-GS-USER-E2E-029-create-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-GS-USER-145 | TC-GS-USER-E2E-029-create-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-GS-USER-146 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-147 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-148 | TC-GS-USER-E2E-020-create-screening-popup-opsi-access-position-division-dan-aksesibilitas | FE+BE |
| TC-GS-USER-149 | TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir | FE+BE |
| TC-GS-USER-150 | TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir | FE+BE |
| TC-GS-USER-151 | TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir | FE+BE |
| TC-GS-USER-152 | TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade | FE+BE |
| TC-GS-USER-153 | TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-154 | TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-155 | TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-156 | TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-157 | TC-GS-USER-E2E-031-create-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-158 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-159 | TC-GS-USER-E2E-022-create-validasi-emoji-format-email-temporary-until-dan-custom-field | FE+BE |
| TC-GS-USER-160 | TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | FE+BE |
| TC-GS-USER-161 | TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | FE+BE |
| TC-GS-USER-162 | TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | FE+BE |
| TC-GS-USER-163 | TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | FE+BE |
| TC-GS-USER-164 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-165 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-166 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-167 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-168 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-169 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-170 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-171 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-172 | TC-GS-USER-E2E-033-edit-validasi-required-batas-karakter-dan-uncheck-semua-access | FE+BE |
| TC-GS-USER-173 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-174 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-175 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-176 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-177 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-178 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-179 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-180 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-181 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-182 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-183 | TC-GS-USER-E2E-034-edit-validasi-emoji-duplikat-dan-format-email | FE+BE |
| TC-GS-USER-184 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-185 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-186 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-187 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-188 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-189 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-190 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-191 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-192 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-193 | TC-GS-USER-E2E-035-edit-sukses-no-op-trim-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-USER-194 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-195 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-196 | TC-GS-USER-E2E-039-edit-tambah-access-dan-produk-kehilangan-subscription | FE+BE |
| TC-GS-USER-197 | TC-GS-USER-E2E-039-edit-tambah-access-dan-produk-kehilangan-subscription | FE+BE |
| TC-GS-USER-198 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-199 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-200 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-201 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-202 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-203 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-204 | TC-GS-USER-E2E-037-edit-temporary-user-set-uncheck-batas-tanggal-dan-expired | FE+BE |
| TC-GS-USER-205 | TC-GS-USER-E2E-038-edit-foto-profil-hapus-ganti-dan-tutup-tanpa-save | FE+BE |
| TC-GS-USER-206 | TC-GS-USER-E2E-038-edit-foto-profil-hapus-ganti-dan-tutup-tanpa-save | FE+BE |
| TC-GS-USER-207 | TC-GS-USER-E2E-038-edit-foto-profil-hapus-ganti-dan-tutup-tanpa-save | FE+BE |
| TC-GS-USER-208 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-209 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-210 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-211 | TC-GS-USER-E2E-041-pairing-tag-di-popup-create-dan-edit | FE+BE |
| TC-GS-USER-212 | TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade | FE+BE |
| TC-GS-USER-213 | TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-214 | TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-215 | TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-216 | TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-217 | TC-GS-USER-E2E-040-edit-referensi-position-division-custom-field-berubah-sesi-lain | FE+BE |
| TC-GS-USER-218 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-219 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-220 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-221 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-222 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-223 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-224 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-225 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-226 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-227 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-228 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-229 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-230 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-231 | TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password | FE+BE |
| TC-GS-USER-232 | TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password | FE+BE |
| TC-GS-USER-233 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-234 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-235 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-236 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-237 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-238 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-239 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-240 | TC-GS-USER-E2E-032-edit-screening-popup-prefilled-default-user-dan-aksesibilitas | FE+BE |
| TC-GS-USER-241 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-242 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-243 | TC-GS-USER-E2E-159-multi-konteks-sesi-user-target-setelah-aksi-admin-deactivate-dan-reset-authenticator | FE+BE |
| TC-GS-USER-244 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-245 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-246 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-247 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-248 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-249 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-250 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-251 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-252 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-253 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-254 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-255 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-256 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-257 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-258 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-259 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-260 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-261 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-262 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-263 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-264 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-265 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-266 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-267 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-268 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-269 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-270 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-271 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-272 | TC-GS-USER-E2E-050-delete-single-screening-cancel-cascade-aset-nlu-tag-foto-dan-klik-ganda | FE+BE |
| TC-GS-USER-273 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-274 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-275 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-276 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-277 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-278 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-279 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-280 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-281 | TC-GS-USER-E2E-051-bulk-action-bar-seleksi-select-all-dan-retensi | FE+BE |
| TC-GS-USER-282 | TC-GS-USER-E2E-053-bulk-selection-limit-checkbox-dan-select-all | FE+BE |
| TC-GS-USER-283 | TC-GS-USER-E2E-053-bulk-selection-limit-checkbox-dan-select-all | FE+BE |
| TC-GS-USER-284 | TC-GS-USER-E2E-053-bulk-selection-limit-checkbox-dan-select-all | FE+BE |
| TC-GS-USER-285 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-286 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-287 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-288 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-289 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-290 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-291 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-292 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-293 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-294 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-295 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-296 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-297 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-298 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-299 | TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel | FE+BE |
| TC-GS-USER-300 | TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel | FE+BE |
| TC-GS-USER-301 | TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel | FE+BE |
| TC-GS-USER-302 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-303 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-304 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-305 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-306 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-307 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-308 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-309 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-310 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-311 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-312 | TC-GS-USER-E2E-056-resend-activation-confirmation-email-cooldown-dan-bulk-resend | FE+BE |
| TC-GS-USER-313 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-314 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-315 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-316 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-317 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-318 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-319 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-320 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-321 | TC-GS-USER-E2E-057-detail-tag-pair-unpair-scan-tolak-dan-re-pair | FE+BE |
| TC-GS-USER-322 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-323 | TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade | FE+BE |
| TC-GS-USER-324 | TC-GS-USER-E2E-042-gating-plan-starter-field-user-tag-dan-downgrade | FE+BE |
| TC-GS-USER-325 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-326 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-327 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-328 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-329 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-330 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-331 | TC-GS-USER-E2E-159-multi-konteks-sesi-user-target-setelah-aksi-admin-deactivate-dan-reset-authenticator | FE+BE |
| TC-GS-USER-332 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-333 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-334 | TC-GS-USER-E2E-058-detail-reset-authenticator-dialog-guard-dan-sesi-target | FE+BE |
| TC-GS-USER-335 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-336 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-337 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-338 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-339 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-340 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-341 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-342 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-343 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-344 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-345 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-346 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-347 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-348 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-349 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-350 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-351 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-352 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-353 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-354 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-355 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-356 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-357 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-358 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-359 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-360 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-361 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-362 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-363 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-364 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-365 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-366 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-367 | TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi | FE+BE |
| TC-GS-USER-368 | TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi | FE+BE |
| TC-GS-USER-369 | TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi | FE+BE |
| TC-GS-USER-370 | TC-GS-USER-E2E-062-detail-product-selector-opsi-dan-navigasi | FE+BE |
| TC-GS-USER-371 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-372 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-373 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-374 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-375 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-376 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-377 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-378 | TC-GS-USER-E2E-068-resilience-tulis-tag-authenticator-foto-detail-inline-email-dan-tab-role | FE+BE |
| TC-GS-USER-379 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-380 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-381 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-382 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-383 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-384 | TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | FE+BE |
| TC-GS-USER-385 | TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | FE+BE |
| TC-GS-USER-386 | TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | FE+BE |
| TC-GS-USER-387 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-388 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-389 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-390 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-391 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-392 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-393 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-394 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-395 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-396 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-397 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-398 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-399 | TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | FE+BE |
| TC-GS-USER-400 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-401 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-402 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-403 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-404 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-405 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-406 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-407 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-408 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-409 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-410 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-411 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-412 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-413 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-414 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-415 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-416 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-417 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-418 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-419 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-420 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-421 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-422 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-423 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-424 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-425 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-426 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-427 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-428 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-429 | TC-GS-USER-E2E-072-user-list-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-430 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-431 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-432 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-433 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-434 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-435 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-436 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-437 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-438 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-439 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-440 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-441 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-442 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-443 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-444 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-445 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-446 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-447 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-448 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-449 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-450 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-451 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-452 | TC-GS-USER-E2E-075-user-list-setup-column-overlay-popup-hide-reorder-pin-reset | mock |
| TC-GS-USER-453 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-454 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-455 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-456 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-457 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-458 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-459 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-460 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-461 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-462 | TC-GS-USER-E2E-077-user-list-download-lebih-dari-5000-baris-background-job | FE+BE |
| TC-GS-USER-463 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-464 | TC-GS-USER-E2E-073-user-list-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-465 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-466 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-467 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-468 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-469 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-470 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-471 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-472 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-473 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-474 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-475 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-476 | TC-GS-USER-E2E-078-modal-changelog-user-screening-dan-search | FE+BE |
| TC-GS-USER-477 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-478 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-479 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-480 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-481 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-482 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-483 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-484 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-485 | TC-GS-USER-E2E-079-modal-changelog-user-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-486 | TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-487 | TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-488 | TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-489 | TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-490 | TC-GS-USER-E2E-080-modal-changelog-user-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-491 | TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-492 | TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-493 | TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-494 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-495 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-496 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-497 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-498 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-499 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-500 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-501 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-502 | TC-GS-USER-E2E-082-modal-changelog-user-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-503 | TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-504 | TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-505 | TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-506 | TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-507 | TC-GS-USER-E2E-083-modal-changelog-user-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-508 | TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-509 | TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-510 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-511 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-512 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-513 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-514 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-515 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-516 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-517 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-518 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-519 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-520 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-521 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-522 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-523 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-524 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-525 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-526 | TC-GS-USER-E2E-085-modal-changelog-user-role-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-527 | TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-528 | TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-529 | TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-530 | TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-531 | TC-GS-USER-E2E-086-modal-changelog-user-role-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-532 | TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-533 | TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-534 | TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-535 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-536 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-537 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-538 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-539 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-540 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-541 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-542 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-543 | TC-GS-USER-E2E-088-modal-changelog-user-role-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-544 | TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-545 | TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-546 | TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-547 | TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-548 | TC-GS-USER-E2E-089-modal-changelog-user-role-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-549 | TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-550 | TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-551 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-552 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-553 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-554 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-555 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-556 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-557 | TC-GS-USER-E2E-090-tab-changelog-detail-screening-dan-search | FE+BE |
| TC-GS-USER-558 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-559 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-560 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-561 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-562 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-563 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-564 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-565 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-566 | TC-GS-USER-E2E-091-tab-changelog-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-567 | TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-568 | TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-569 | TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-570 | TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-571 | TC-GS-USER-E2E-092-tab-changelog-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-572 | TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-573 | TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-574 | TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-575 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-576 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-577 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-578 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-579 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-580 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-581 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-582 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-583 | TC-GS-USER-E2E-094-tab-changelog-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-584 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-585 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-586 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-587 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-588 | TC-GS-USER-E2E-095-tab-changelog-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-589 | TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-590 | TC-GS-USER-E2E-093-tab-changelog-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-591 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-592 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-593 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-594 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-595 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-596 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-597 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-598 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-599 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-600 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-601 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-602 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-603 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-604 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-605 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-606 | TC-GS-USER-E2E-097-tab-system-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-607 | TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-608 | TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-609 | TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-610 | TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-611 | TC-GS-USER-E2E-098-tab-system-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-612 | TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-613 | TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-614 | TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-615 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-616 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-617 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-618 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-619 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-620 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-621 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-622 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-623 | TC-GS-USER-E2E-100-tab-system-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-624 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-625 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-626 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-627 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-628 | TC-GS-USER-E2E-101-tab-system-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-629 | TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-630 | TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-631 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-632 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-633 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-634 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-635 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-636 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-637 | TC-GS-USER-E2E-102-tab-user-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-638 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-639 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-640 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-641 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-642 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-643 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-644 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-645 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-646 | TC-GS-USER-E2E-103-tab-user-log-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-647 | TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-648 | TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-649 | TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-650 | TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-651 | TC-GS-USER-E2E-104-tab-user-log-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-652 | TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-653 | TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-654 | TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-655 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-656 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-657 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-658 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-659 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-660 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-661 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-662 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-663 | TC-GS-USER-E2E-106-tab-user-log-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-664 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-665 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-666 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-667 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-668 | TC-GS-USER-E2E-107-tab-user-log-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-669 | TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-670 | TC-GS-USER-E2E-105-tab-user-log-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-671 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-672 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-673 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-674 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-675 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-676 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-677 | TC-GS-USER-E2E-108-tab-non-login-user-detail-screening-dan-search | FE+BE |
| TC-GS-USER-678 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-679 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-680 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-681 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-682 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-683 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-684 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-685 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-686 | TC-GS-USER-E2E-109-tab-non-login-user-detail-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-687 | TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-688 | TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-689 | TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-690 | TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-691 | TC-GS-USER-E2E-110-tab-non-login-user-detail-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-692 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-693 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-694 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-695 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-696 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-697 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-698 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-699 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-700 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-701 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-702 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-703 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-704 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-705 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-706 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-707 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-708 | TC-GS-USER-E2E-112-tab-non-login-user-detail-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-709 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-710 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-711 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-712 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-713 | TC-GS-USER-E2E-113-tab-non-login-user-detail-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-714 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-715 | TC-GS-USER-E2E-111-tab-non-login-user-detail-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-716 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-717 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-718 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-719 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-720 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-721 | TC-GS-USER-E2E-114-subtab-borrowed-assets-screening-dan-search | FE+BE |
| TC-GS-USER-722 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-723 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-724 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-725 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-726 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-727 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-728 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-729 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-730 | TC-GS-USER-E2E-115-subtab-borrowed-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-731 | TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-732 | TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-733 | TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-734 | TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-735 | TC-GS-USER-E2E-116-subtab-borrowed-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-736 | TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-737 | TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-738 | TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-739 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-740 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-741 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-742 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-743 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-744 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-745 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-746 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-747 | TC-GS-USER-E2E-118-subtab-borrowed-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-748 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-749 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-750 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-751 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-752 | TC-GS-USER-E2E-119-subtab-borrowed-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-753 | TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-754 | TC-GS-USER-E2E-117-subtab-borrowed-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-755 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-756 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-757 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-758 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-759 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-760 | TC-GS-USER-E2E-120-subtab-assigned-assets-screening-dan-search | FE+BE |
| TC-GS-USER-761 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-762 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-763 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-764 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-765 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-766 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-767 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-768 | TC-GS-USER-E2E-121-subtab-assigned-assets-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-769 | TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-770 | TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-771 | TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-772 | TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-773 | TC-GS-USER-E2E-122-subtab-assigned-assets-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-774 | TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-775 | TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-776 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-777 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-778 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-779 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-780 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-781 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-782 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-783 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-784 | TC-GS-USER-E2E-124-subtab-assigned-assets-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-785 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-786 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-787 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-788 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-789 | TC-GS-USER-E2E-125-subtab-assigned-assets-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-790 | TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-791 | TC-GS-USER-E2E-123-subtab-assigned-assets-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-792 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-793 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-794 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-795 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-796 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-797 | TC-GS-USER-E2E-126-subtab-pending-approvals-screening-dan-search | FE+BE |
| TC-GS-USER-798 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-799 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-800 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-801 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-802 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-803 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-804 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-805 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-806 | TC-GS-USER-E2E-127-subtab-pending-approvals-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-807 | TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-808 | TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-809 | TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-810 | TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-811 | TC-GS-USER-E2E-128-subtab-pending-approvals-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-812 | TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-813 | TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-814 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-815 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-816 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-817 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-818 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-819 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-820 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-821 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-822 | TC-GS-USER-E2E-130-subtab-pending-approvals-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-823 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-824 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-825 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-826 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-827 | TC-GS-USER-E2E-131-subtab-pending-approvals-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-828 | TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-829 | TC-GS-USER-E2E-129-subtab-pending-approvals-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-830 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-831 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-832 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-833 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-834 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-835 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-836 | TC-GS-USER-E2E-132-subtab-pending-tasks-screening-dan-search | FE+BE |
| TC-GS-USER-837 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-838 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-839 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-840 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-841 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-842 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-843 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-844 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-845 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-846 | TC-GS-USER-E2E-133-subtab-pending-tasks-filter-panel-opsi-multi-select-or-chip-dan-and | FE+BE |
| TC-GS-USER-847 | TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-848 | TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-849 | TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-850 | TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-851 | TC-GS-USER-E2E-134-subtab-pending-tasks-kombinasi-search-filter-clear-dan-filter-kolom-hidden | FE+BE |
| TC-GS-USER-852 | TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-853 | TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-854 | TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-855 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-856 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-857 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-858 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-859 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-860 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-861 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-862 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-863 | TC-GS-USER-E2E-136-subtab-pending-tasks-setup-column-overlay-popup-hide-reorder-pin-reset | FE+BE |
| TC-GS-USER-864 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-865 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-866 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-867 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-868 | TC-GS-USER-E2E-137-subtab-pending-tasks-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-869 | TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-870 | TC-GS-USER-E2E-135-subtab-pending-tasks-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-871 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-872 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-873 | TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-GS-USER-874 | TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-GS-USER-875 | TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-GS-USER-876 | TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-GS-USER-877 | TC-GS-USER-E2E-138-pencatatan-create-edit-delete-field-di-changelog-system-log-dan-activity-log | FE+BE |
| TC-GS-USER-878 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-879 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-880 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-881 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-882 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-883 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-884 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-885 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-886 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-887 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-888 | TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in | FE+BE |
| TC-GS-USER-889 | TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in | FE+BE |
| TC-GS-USER-890 | TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in | FE+BE |
| TC-GS-USER-891 | TC-GS-USER-E2E-143-pencatatan-handheld-assign-unassign-check-out-check-in | FE+BE |
| TC-GS-USER-892 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-893 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-894 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-895 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-896 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-897 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-898 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-899 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-900 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-901 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-902 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-903 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-904 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-905 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-906 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-907 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-908 | TC-GS-USER-E2E-141-pencatatan-email-resend-pending-cancel-dan-email-confirmed | FE+BE |
| TC-GS-USER-909 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-910 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-911 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-912 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-913 | TC-GS-USER-E2E-140-pencatatan-status-global-per-produk-dan-temporary-user | FE+BE |
| TC-GS-USER-914 | TC-GS-USER-E2E-146-pencatatan-bulk-resend-dan-bulk-delete-satu-baris-per-user | FE+BE |
| TC-GS-USER-915 | TC-GS-USER-E2E-146-pencatatan-bulk-resend-dan-bulk-delete-satu-baris-per-user | FE+BE |
| TC-GS-USER-916 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-917 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-918 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-919 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-920 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-921 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-922 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-923 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-924 | TC-GS-USER-E2E-142-pencatatan-add-remove-access-pair-unpair-tag-dan-reset-authenticator | FE+BE |
| TC-GS-USER-925 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-926 | TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove | FE+BE |
| TC-GS-USER-927 | TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove | FE+BE |
| TC-GS-USER-928 | TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove | FE+BE |
| TC-GS-USER-929 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-930 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-931 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-932 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-933 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-934 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-935 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-936 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-937 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-938 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-939 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-940 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-941 | TC-GS-USER-E2E-148-user-log-login-logout-change-password-reset-password-dan-session | FE+BE |
| TC-GS-USER-942 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-943 | TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role | FE+BE |
| TC-GS-USER-944 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-945 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-946 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-947 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-948 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-949 | TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user | FE+BE |
| TC-GS-USER-950 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-951 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-952 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-953 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-954 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-955 | TC-GS-USER-E2E-151-sinkron-custom-field-lifecycle-ke-user-existing | FE+BE |
| TC-GS-USER-958 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-959 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-960 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-961 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-962 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-963 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-964 | TC-GS-USER-E2E-153-sinkron-produk-fams-admin-console-my-profile-tag-registry-dan-file-manager | FE+BE |
| TC-GS-USER-965 | TC-GS-USER-E2E-154-format-tanggal-general-settings-di-user-list-changelog-dan-detail | FE+BE |
| TC-GS-USER-966 | TC-GS-USER-E2E-154-format-tanggal-general-settings-di-user-list-changelog-dan-detail | FE+BE |
| TC-GS-USER-967 | TC-GS-USER-E2E-154-format-tanggal-general-settings-di-user-list-changelog-dan-detail | FE+BE |
| TC-GS-USER-968 | TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password | FE+BE |
| TC-GS-USER-969 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-970 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-971 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-972 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-973 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-974 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-975 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-976 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-977 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-978 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-979 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-980 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-981 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-982 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-983 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-984 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-985 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-986 | TC-GS-USER-E2E-030-create-limit-master-data-count-stay-on-form-dan-slot-terakhir | FE+BE |
| TC-GS-USER-987 | TC-GS-USER-E2E-066-resilience-tulis-create-edit-delete-foto-5xx-dan-timeout | FE+BE |
| TC-GS-USER-988 | TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses | FE+BE |
| TC-GS-USER-989 | TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses | FE+BE |
| TC-GS-USER-990 | TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses | FE+BE |
| TC-GS-USER-991 | TC-GS-USER-E2E-157-siklus-aktivasi-login-link-kedaluwarsa-dan-deactivate-memutus-akses | FE+BE |
| TC-GS-USER-992 | TC-GS-USER-E2E-158-isolasi-subtab-login-non-login-dan-persistensi-setup-column | FE+BE |
| TC-GS-USER-993 | TC-GS-USER-E2E-158-isolasi-subtab-login-non-login-dan-persistensi-setup-column | FE+BE |
| TC-GS-USER-994 | TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | FE+BE |
| TC-GS-USER-995 | TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | FE+BE |
| TC-GS-USER-996 | TC-GS-USER-E2E-012-role-matrix-default-user-sebagai-aktor | FE+BE |
| TC-GS-USER-997 | TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | FE+BE |
| TC-GS-USER-998 | TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | FE+BE |
| TC-GS-USER-999 | TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | FE+BE |
| TC-GS-USER-1000 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-1001 | TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role | FE+BE |
| TC-GS-USER-1002 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-1003 | TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | FE+BE |
| TC-GS-USER-1004 | TC-GS-USER-E2E-013-role-matrix-kontrol-list-holder-scoped-create-update-delete-read | FE+BE |
| TC-GS-USER-1005 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-1006 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-1007 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-1008 | TC-GS-USER-E2E-043-remove-access-dialog-produk-dengan-aset-atau-approval | FE+BE |
| TC-GS-USER-1009 | TC-GS-USER-E2E-044-remove-access-global-settings-tier-role-dan-represented-by | FE+BE |
| TC-GS-USER-1010 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-1011 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-1012 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-1013 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-1014 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
| TC-GS-USER-1015 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-1016 | TC-GS-USER-E2E-070-multi-konteks-dua-admin-race-last-write-wins-dan-record-dihapus-sesi-lain | FE+BE |
| TC-GS-USER-1017 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-1018 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-1019 | TC-GS-USER-E2E-065-detail-tab-responsibilities-entitas-subscription-fams-dan-sinkron-modul-sumber | FE+BE |
| TC-GS-USER-1020 | TC-GS-USER-E2E-064-detail-tab-role-auto-save-assign-remove-dan-auto-revert-tier | FE+BE |
| TC-GS-USER-1021 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1022 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1023 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1024 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1025 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1026 | TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired | FE+BE |
| TC-GS-USER-1027 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-1028 | TC-GS-USER-E2E-055-bulk-delete-homogen-campuran-dan-cancel | FE+BE |
| TC-GS-USER-1029 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-1030 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-1031 | TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | FE+BE |
| TC-GS-USER-1032 | TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | FE+BE |
| TC-GS-USER-1033 | TC-GS-USER-E2E-023-create-validasi-duplikat-email-dan-employee-id | FE+BE |
| TC-GS-USER-1034 | TC-GS-USER-E2E-071-user-list-screening-dan-search | FE+BE |
| TC-GS-USER-1035 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-1036 | TC-GS-USER-E2E-054-bulk-activate-dan-deactivate-dialog-skip-dan-ringkasan | FE+BE |
| TC-GS-USER-1037 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-1038 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-1039 | TC-GS-USER-E2E-048-reactivate-temporary-user-extend-make-permanent-dan-batas-tanggal | FE+BE |
| TC-GS-USER-1040 | TC-GS-USER-E2E-027-create-foto-profil-hover-file-picker-kompres-dan-batas-ukuran | FE+BE |
| TC-GS-USER-1041 | TC-GS-USER-E2E-059-detail-foto-hover-upload-ganti-hapus-dan-berkas-korup | FE+BE |
| TC-GS-USER-1042 | TC-GS-USER-E2E-096-tab-system-log-detail-screening-dan-search | FE+BE |
| TC-GS-USER-1043 | TC-GS-USER-E2E-001-screening-user-list-layout-tab-sort-default-dan-tooltip-toolbar | FE+BE |
| TC-GS-USER-1044 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-1045 | TC-GS-USER-E2E-052-bulk-opsi-aksi-per-kombinasi-seleksi | FE+BE |
| TC-GS-USER-1046 | TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role | FE+BE |
| TC-GS-USER-1047 | TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role | FE+BE |
| TC-GS-USER-1048 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-1049 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-1050 | TC-GS-USER-E2E-067-resilience-tulis-status-bulk-dan-resend-5xx-dan-sebagian-gagal | FE+BE |
| TC-GS-USER-1051 | TC-GS-USER-E2E-063-detail-tab-role-screening-state-banner-self-dan-column-visibility | FE+BE |
| TC-GS-USER-1052 | TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert | FE+BE |
| TC-GS-USER-1053 | TC-GS-USER-E2E-084-modal-changelog-user-role-screening-dan-search | FE+BE |
| TC-GS-USER-1054 | TC-GS-USER-E2E-061-detail-header-badge-user-type-info-temporary-dan-retensi-state-list | FE+BE |
| TC-GS-USER-1055 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1056 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1057 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1058 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1059 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1060 | TC-GS-USER-E2E-069-resilience-download-gagal-toast-error-semua-permukaan | FE+BE |
| TC-GS-USER-1061 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-1062 | TC-GS-USER-E2E-028-create-penutupan-popup-clear-field-backdrop-dan-unsaved-changes | mock |
| TC-GS-USER-1063 | TC-GS-USER-E2E-036-edit-penutupan-popup-clear-field-unsaved-changes-dan-reload | mock |
| TC-GS-USER-1064 | TC-GS-USER-E2E-152-sinkron-custom-field-deactivate-dan-delete-saat-kolom-curated-dan-filter-aktif | FE+BE |
| TC-GS-USER-1065 | TC-GS-USER-E2E-152-sinkron-custom-field-deactivate-dan-delete-saat-kolom-curated-dan-filter-aktif | FE+BE |
| TC-GS-USER-1066 | TC-GS-USER-E2E-152-sinkron-custom-field-deactivate-dan-delete-saat-kolom-curated-dan-filter-aktif | FE+BE |
| TC-GS-USER-1067 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-1068 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-1069 | TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | FE+BE |
| TC-GS-USER-1070 | TC-GS-USER-E2E-007-resilience-baca-error-load-try-again-list-changelog-dan-tab-detail | FE+BE |
| TC-GS-USER-1071 | TC-GS-USER-E2E-009-role-matrix-negatif-read-only-kontrol-list-dan-detail | FE+BE |
| TC-GS-USER-1072 | TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header | FE+BE |
| TC-GS-USER-1073 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-1074 | TC-GS-USER-E2E-018-aksi-pada-akun-sendiri-edit-foto-resend-scan-tag-dan-kunci-access | FE+BE |
| TC-GS-USER-1075 | TC-GS-USER-E2E-155-defense-in-depth-request-langsung-tanpa-wewenang-xss-dan-karakter-khusus | FE+BE |
| TC-GS-USER-1076 | TC-GS-USER-E2E-139-pencatatan-multi-field-snapshot-foto-admin-override-dan-seed-default-user | FE+BE |
| TC-GS-USER-1077 | TC-GS-USER-E2E-060-detail-inline-edit-custom-field-screening-simpan-batal-dan-validasi | FE+BE |
| TC-GS-USER-1078 | TC-GS-USER-E2E-074-user-list-sort-3-state-pagination-dan-kombinasi | FE+BE |
| TC-GS-USER-1079 | TC-GS-USER-E2E-076-user-list-download-isi-file-csv-xlsx | FE+BE |
| TC-GS-USER-1080 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-1081 | TC-GS-USER-E2E-046-konfirmasi-email-via-link-kedaluwarsa-dan-invalidasi-link-reset-password | FE+BE |
| TC-GS-USER-1082 | TC-GS-USER-E2E-045-edit-email-pending-email-change-sisi-admin | FE+BE |
| TC-GS-USER-1083 | TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked | FE+BE |
| TC-GS-USER-1084 | TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked | FE+BE |
| TC-GS-USER-1085 | TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked | FE+BE |
| TC-GS-USER-1086 | TC-GS-USER-E2E-149-user-log-note-lock-change-password-dan-account-locked | FE+BE |
| TC-GS-USER-1087 | TC-GS-USER-E2E-047-toggle-active-single-deactivate-activate-dan-header-detail | FE+BE |
| TC-GS-USER-1088 | TC-GS-USER-E2E-049-temporary-auto-inactive-jam-server-dan-job-terjadwal | FE+BE |
