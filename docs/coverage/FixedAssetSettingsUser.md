# Coverage E2E — Fixed Asset > Settings > User

Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md` (1128 TC granular aktif); tidak ada `tc-settings-user-backend.md`, jadi tidak ada TC hanya-BE.
Suite: `specs/FixedAsset/SettingsUser/`.
Prefix Modul: `FA` + `SU` (`TC-FA-SU-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (429 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-SU-E2E-001-screening-user-list-breadcrumb-tanpa-page-title-dan-tanpa-tombol-back | Screening User List: Breadcrumb, Tanpa Page Title, dan Tanpa Tombol Back | FE+BE | 26 | TC-FA-SU-1, TC-FA-SU-2, TC-FA-SU-3 |
| TC-FA-SU-E2E-002-sidebar-group-tree-screening-tombol-open-collapse-dan-pencarian-node | Sidebar Group Tree: Screening, Tombol Open/Collapse, dan Pencarian Node | FE+BE | 31 | TC-FA-SU-4, TC-FA-SU-5, TC-FA-SU-6 |
| TC-FA-SU-E2E-003-sidebar-group-tree-filter-user-list-per-node-dan-state-preservation | Sidebar Group Tree: Filter User List per Node dan State Preservation | FE+BE | 45 | TC-FA-SU-7, TC-FA-SU-8 |
| TC-FA-SU-E2E-004-sel-tabel-user-list-name-role-dan-home-group | Sel Tabel User List: Name, Role, dan Home Group | FE+BE | 34 | TC-FA-SU-9, TC-FA-SU-10, TC-FA-SU-11 |
| TC-FA-SU-E2E-005-sakelar-active-dan-menu-row-action-user-list | Sakelar Active dan Menu Row Action User List | FE+BE | 21 | TC-FA-SU-13, TC-FA-SU-14 |
| TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit | Guided Tooltip User List: Kunjungan Pertama, Navigasi, Replay, dan Exit | FE+BE | 56 | TC-FA-SU-17, TC-FA-SU-18, TC-FA-SU-19 |
| TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field | Screening Detail User: Header, General Information, dan Custom Field | FE+BE | 72 | TC-FA-SU-20, TC-FA-SU-21, TC-FA-SU-22, TC-FA-SU-29 |
| TC-FA-SU-E2E-008-user-type-detail-user-total-control-read-only-dan-group-manager | User Type Detail User: Total Control, Read Only, dan Group Manager | FE+BE | 24 | TC-FA-SU-23, TC-FA-SU-24, TC-FA-SU-25 |
| TC-FA-SU-E2E-009-user-type-detail-user-admin-basic-dan-prioritas-bila-beririsan | User Type Detail User: Admin, Basic, dan Prioritas Bila Beririsan | FE+BE | 33 | TC-FA-SU-26, TC-FA-SU-27, TC-FA-SU-28 |
| TC-FA-SU-E2E-010-screening-tab-role-dan-tab-responsibilities-detail-user-serta-banner-tab-role | Screening Tab Role dan Tab Responsibilities Detail User serta Banner Tab Role | FE+BE | 57 | TC-FA-SU-30, TC-FA-SU-31, TC-FA-SU-32 |
| TC-FA-SU-E2E-011-screening-tab-non-login-user-changelog-system-log-transaction-admin-log-dan-user-log | Screening Tab Non-Login User, Changelog, System Log, Transaction Admin Log, dan User Log | FE+BE | 31 | TC-FA-SU-33, TC-FA-SU-34 |
| TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list | Popup Role Count dan Empty State User List | FE+BE | 37 | TC-FA-SU-35, TC-FA-SU-36, TC-FA-SU-37, TC-FA-SU-38 |
| TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | Android: Kartu User List, Row Action, Toolbar, Seleksi, dan Drawer Group Tree | FE+BE | 33 | TC-FA-SU-39, TC-FA-SU-40, TC-FA-SU-41, TC-FA-SU-42, TC-FA-SU-43 |
| TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | Android: Detail User, Card List, Modal, Tooltip Disabled, Countdown Resend, dan Bottom Sheet | FE+BE | 69 | TC-FA-SU-44, TC-FA-SU-45, TC-FA-SU-46, TC-FA-SU-47, TC-FA-SU-48, TC-FA-SU-49 |
| TC-FA-SU-E2E-015-modified-by-last-updated-dan-pengguna-baru-tanpa-role-setelah-app-access | Kolom Modified By dan Last Updated serta Pengguna Baru Tanpa Role setelah App Access Diberikan | FE+BE | 36 | TC-FA-SU-12, TC-FA-SU-16 |
| TC-FA-SU-E2E-016-menu-row-action-baris-default-user-dan-self-termasuk-varian-pending | Menu Row Action Baris Default User dan Self Termasuk Varian Pending | FE+BE | 32 | TC-FA-SU-15 |
| TC-FA-SU-E2E-017-role-matrix-gate-sub-menu-settings-user-dan-visibilitas-elemen-ui-total-control | Role Matrix: Gate Sub-menu Settings > User dan Visibilitas Elemen UI Total Control | FE+BE. | 51 | TC-FA-SU-50, TC-FA-SU-51 |
| TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom | Role Matrix: Visibilitas Elemen UI Manage user & role Group, Group Manager, dan Kolom Checkbox | FE+BE. | 72 | TC-FA-SU-55, TC-FA-SU-56, TC-FA-SU-57, TC-FA-SU-86 |
| TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager | Row Scope Aktor Global, Aktor Ber-scope Grup, dan Group Manager | FE+BE. | 56 | TC-FA-SU-58, TC-FA-SU-59, TC-FA-SU-60, TC-FA-SU-69 |
| TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | Sidebar Group Tree Ber-scope, Direct URL Detail di Luar Scope, dan Log Disaring Scope | FE+BE. | 53 | TC-FA-SU-61, TC-FA-SU-62, TC-FA-SU-63, TC-FA-SU-64, TC-FA-SU-65 |
| TC-FA-SU-E2E-021-aktor-multi-sumber-global-role-manage-global-user-dan-role-vs-group-role-manage-user | Aktor Multi-sumber: Global Role Manage global user & role vs Group Role Manage user & role | FE+BE. | 37 | TC-FA-SU-66, TC-FA-SU-67, TC-FA-SU-68 |
| TC-FA-SU-E2E-022-kunci-target-default-user-diri-sendiri-dan-target-total-control-atau-read-only | Kunci Target: Default User, Diri Sendiri, dan Target Total Control atau Read Only | FE+BE. | 69 | TC-FA-SU-70, TC-FA-SU-71, TC-FA-SU-72 |
| TC-FA-SU-E2E-023-kunci-target-group-manager-dan-nonaktif-di-global-settings | Kunci Target: Group Manager dan Nonaktif di Global Settings | FE+BE. | 41 | TC-FA-SU-73, TC-FA-SU-74 |
| TC-FA-SU-E2E-024-kunci-target-tier-bagi-aktor-ber-scope-grup-dan-group-manager-deactivate-dan-bulk-skip | Kunci Target Tier bagi Aktor Ber-scope Grup dan Group Manager: Kontrol Disabled dan Bulk Deactivate Skip | FE+BE. | 42 | TC-FA-SU-1063 |
| TC-FA-SU-E2E-025-aktor-read-only-tab-role-read-only-dan-akses-detail-pengguna-di-luar-fams | Aktor Read Only: Tab Role Read-only dan Akses Tab Informasi Detail Pengguna | FE+BE. | 22 | TC-FA-SU-82, TC-FA-SU-83 |
| TC-FA-SU-E2E-026-katalog-peran-manage-global-user-dan-role-dan-manage-user-dan-role-serta-sel | Katalog Peran Manage global user & role dan Manage user & role, serta Sel Kapabilitas Role Matrix | FE+BE. | 10 | TC-FA-SU-84, TC-FA-SU-85 |
| TC-FA-SU-E2E-027-kunci-target-tier-bagi-aktor-global-ber-scope-grup-dan-group-manager-bulk-activate-skip | Kunci Target Tier bagi Aktor Global, Ber-scope Grup, dan Group Manager: Sakelar OFF Disabled dan Bulk Activate Skip | FE+BE. | 30 | TC-FA-SU-1065 |
| TC-FA-SU-E2E-028-role-matrix-visibilitas-elemen-ui-read-only-dan-manage-global-user-dan-role | Role Matrix: Visibilitas Elemen UI Read Only dan Manage global user & role (Update dan Read saja) | FE+BE. | 95 | TC-FA-SU-52, TC-FA-SU-53, TC-FA-SU-54 |
| TC-FA-SU-E2E-029-single-deactivate-dan-activate-dari-sakelar-baris-dialog-konfirmasi-toast-log-dan | Single Deactivate dan Activate dari Sakelar Baris: Dialog, Konfirmasi, Toast, dan Log | FE+BE. | 32 | TC-FA-SU-87, TC-FA-SU-88 |
| TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | Deactivate dari Header Detail dan Dialog Peringatan Aset Aktif, Approval Tertunda, Kedua Peringatan, dan Tanpa Peringatan | FE+BE. | 47 | TC-FA-SU-91, TC-FA-SU-92, TC-FA-SU-93, TC-FA-SU-94, TC-FA-SU-96 |
| TC-FA-SU-E2E-031-edit-bersamaan-status-aktif-oleh-dua-admin-dan-toggle-ke-nilai-yang-sudah-berlaku | Edit Bersamaan Status Aktif oleh Dua Admin dan Toggle ke Nilai yang Sudah Berlaku | FE+BE. | 17 | TC-FA-SU-99, TC-FA-SU-100 |
| TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan | Resilience Status Aktif Single: Server Error 5xx, Pemeriksaan Gagal, dan Kegagalan Penulisan Log | FE+BE. | 36 | TC-FA-SU-95, TC-FA-SU-101, TC-FA-SU-102, TC-FA-SU-103 |
| TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal | Resilience Bulk Status Aktif: Pemeriksaan Gagal, Sebagian Gagal, dan Seluruh Item Gagal | FE+BE. | 46 | TC-FA-SU-107, TC-FA-SU-118, TC-FA-SU-119, TC-FA-SU-134 |
| TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk | Bulk Deactivate dan Activate Seluruh Baris Eligible serta Dialog Bulk | FE+BE. | 36 | TC-FA-SU-104, TC-FA-SU-105, TC-FA-SU-106, TC-FA-SU-108 |
| TC-FA-SU-E2E-035-bulk-seleksi-campuran-dialog-dua-kelompok-skip-tier-dan-skip-nonaktif-global-settings | Bulk Seleksi Campuran: Dialog Dua Kelompok untuk Deactivate dan Activate serta Peringatan Aset pada Kelompok Deactivated | FE+BE. | 29 | TC-FA-SU-109, TC-FA-SU-110, TC-FA-SU-111 |
| TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | Bulk Tanpa Baris Eligible: Dialog Blok, Collapse ke Dialog Single, dan Cancel Bulk Activate | FE+BE. | 51 | TC-FA-SU-112, TC-FA-SU-113, TC-FA-SU-114, TC-FA-SU-115, TC-FA-SU-1049 |
| TC-FA-SU-E2E-037-bulk-actions-bar-counter-select-all-unselect-all-kondisi-tampil-aksi-dan-seleksi | Bulk Actions Bar: Counter, Select All, Unselect All, Kondisi Tampil Aksi, dan Seleksi Dipertahankan | FE+BE. | 42 | TC-FA-SU-120, TC-FA-SU-121, TC-FA-SU-122 |
| TC-FA-SU-E2E-038-aktor-manage-user-dan-role-group-dan-group-manager-pengguna-pending-activation-dan | Aktor Manage user & role Group dan Group Manager, Pengguna Pending Activation, dan Resolusi Approver | FE+BE. | 46 | TC-FA-SU-131, TC-FA-SU-132, TC-FA-SU-133 |
| TC-FA-SU-E2E-039-batal-deactivate-dan-activate-single-lewat-cancel-dan-tombol-close | Batal Deactivate dan Activate Single lewat Cancel dan Tombol Close: Sakelar Kembali Tanpa Perubahan | FE+BE. | 23 | TC-FA-SU-89, TC-FA-SU-90 |
| TC-FA-SU-E2E-040-bulk-skip-nonaktif-global-settings-skip-tier-dan-select-all-aktor-manage-user-dan-role | Bulk: Skip Nonaktif Global Settings, Skip Tier Total Control dan Read Only, dan Select All oleh Aktor Manage user & role | FE+BE. | 44 | TC-FA-SU-116, TC-FA-SU-117, TC-FA-SU-124 |
| TC-FA-SU-E2E-041-resend-activation-dan-confirmation-email-single-dari-row-action | Resend Activation dan Confirmation Email Single dari Row Action | FE+BE. | 32 | TC-FA-SU-135, TC-FA-SU-136 |
| TC-FA-SU-E2E-042-resend-dari-header-detail-user-tanpa-kunci-target-dan-pengguna-inactive-atau-pending | Resend dari Header Detail User, Tanpa Kunci Target, dan Pengguna Inactive atau Pending | FE+BE. | 32 | TC-FA-SU-137, TC-FA-SU-150, TC-FA-SU-151 |
| TC-FA-SU-E2E-043-cooldown-resend-hitung-mundur-60-sampai-1-dan-batas-tepat-t-60-detik | Cooldown Resend: Hitung Mundur 60 sampai 1 dan Batas Tepat T+60 Detik | FE+BE. | 26 | TC-FA-SU-138, TC-FA-SU-139 |
| TC-FA-SU-E2E-044-resend-penolakan-cooldown-dari-tampilan-basi-dan-status-berubah-setelah-halaman-dimuat | Resend: Penolakan Cooldown dari Tampilan Basi dan Status Berubah Setelah Halaman Dimuat | FE+BE. | 29 | TC-FA-SU-145, TC-FA-SU-149 |
| TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi | Bulk Resend Activation Email: Sukses, Sebagian Cooldown, Seluruh Cooldown, dan Seleksi Campuran | FE+BE. | 54 | TC-FA-SU-153, TC-FA-SU-154, TC-FA-SU-155, TC-FA-SU-157 |
| TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log | Resilience Resend: Gagal Kirim Email, Bulk Gagal, dan Kegagalan Penulisan Log | FE+BE. | 62 | TC-FA-SU-143, TC-FA-SU-144, TC-FA-SU-156, TC-FA-SU-158 |
| TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan | Screening Sub-tab Global Role dan Switch Global Role Pertama, Matikan, dan Nyalakan Kembali | FE+BE. | 40 | TC-FA-SU-159, TC-FA-SU-160, TC-FA-SU-161, TC-FA-SU-162 |
| TC-FA-SU-E2E-048-nyalakan-kembali-switch-ubah-checkbox-update-dan-checkbox-read-terkunci | Nyalakan Kembali Switch, Ubah Checkbox Update, dan Checkbox Read Terkunci | FE+BE. | 28 | TC-FA-SU-163, TC-FA-SU-164, TC-FA-SU-165 |
| TC-FA-SU-E2E-049-default-checkbox-switch-on-pertama-dan-indikator-loading-switch | Default Checkbox Switch ON Pertama dan Indikator Loading Switch | FE+BE. | 13 | TC-FA-SU-166, TC-FA-SU-172 |
| TC-FA-SU-E2E-050-no-op-switch-dan-checkbox-global-role-akibat-perubahan-sesi-lain | No-op Switch dan Checkbox Global Role Akibat Perubahan Sesi Lain | FE+BE. | 25 | TC-FA-SU-169, TC-FA-SU-170 |
| TC-FA-SU-E2E-051-resilience-global-role-switch-dan-checkbox-gagal-disimpan-serta-auto-revert-gagal | Resilience Global Role: Switch dan Checkbox Gagal Disimpan serta Auto-Revert Gagal | FE+BE. | 40 | TC-FA-SU-167, TC-FA-SU-168, TC-FA-SU-191 |
| TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | Auto-Revert Total Control pada Global Role: Dialog, Konfirmasi, Cancel, dan Switch Target Bertier | FE+BE. | 49 | TC-FA-SU-173, TC-FA-SU-174, TC-FA-SU-175, TC-FA-SU-177, TC-FA-SU-178 |
| TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain | Auto-Revert Read Only, Banner Tier, Banner Group Manager, dan Tier Dilepas Aktor Lain | FE+BE. | 45 | TC-FA-SU-176, TC-FA-SU-179, TC-FA-SU-180, TC-FA-SU-181 |
| TC-FA-SU-E2E-054-kunci-global-role-default-user-diri-sendiri-tier-aktor-ber-scope-grup-dan-aktor-tanpa | Kunci Global Role: Default User, Diri Sendiri, Tier, Aktor Ber-scope Grup, dan Aktor Tanpa Izin | FE+BE. | 37 | TC-FA-SU-182, TC-FA-SU-184, TC-FA-SU-185 |
| TC-FA-SU-E2E-055-eksklusivitas-global-role-manage-global-user-dan-role-vs-group-role-manage-user-dan | Eksklusivitas Global Role Manage global user & role vs Group Role Manage user & role | FE+BE. | 29 | TC-FA-SU-186, TC-FA-SU-187, TC-FA-SU-1054 |
| TC-FA-SU-E2E-056-cascade-total-control-terhadap-group-role-manage-user-dan-role-dan-sinkronisasi-dua | Cascade Total Control terhadap Group Role Manage user & role dan Sinkronisasi Dua Arah Global Role | FE+BE. | 26 | TC-FA-SU-189, TC-FA-SU-190, TC-FA-SU-1055 |
| TC-FA-SU-E2E-057-cooldown-resend-pengiriman-berulang-dan-pemisahan-per-pengguna-dan-jenis-email | Cooldown Resend: Pengiriman Berulang dan Pemisahan per Pengguna dan Jenis Email | FE+BE. | 29 | TC-FA-SU-140, TC-FA-SU-141, TC-FA-SU-142 |
| TC-FA-SU-E2E-058-visibilitas-aksi-resend-menurut-status-pengguna-di-menu-baris-dan-header-detail | Visibilitas Aksi Resend Menurut Status Pengguna di Menu Baris dan Header Detail | FE+BE. | 21 | TC-FA-SU-147 |
| TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role | Screening Sub-tab Group Role dan Popup Assign Group Role | FE+BE. | 30 | TC-FA-SU-192, TC-FA-SU-193, TC-FA-SU-194, TC-FA-SU-195 |
| TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role | Pilih Node Select Group, Cancel Popup, dan Tambah Grup ke Group Role | FE+BE. | 47 | TC-FA-SU-196, TC-FA-SU-197, TC-FA-SU-198, TC-FA-SU-199 |
| TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan | Hapus Grup, Ubah Checkbox CRUD, Save Campuran, dan Save Tanpa Perubahan | FE+BE. | 52 | TC-FA-SU-200, TC-FA-SU-201, TC-FA-SU-202, TC-FA-SU-203 |
| TC-FA-SU-E2E-062-tambah-lalu-hapus-sebelum-save-save-dengan-0-grup-dan-clear-field | Tambah Lalu Hapus Sebelum Save, Save dengan 0 Grup, dan Clear Field | FE+BE. | 34 | TC-FA-SU-204, TC-FA-SU-205, TC-FA-SU-206 |
| TC-FA-SU-E2E-063-dialog-unsaved-changes-dan-backdrop-popup-assign-group-role | Dialog Unsaved Changes dan Backdrop Popup Assign Group Role | FE+BE. | 21 | TC-FA-SU-207, TC-FA-SU-208 |
| TC-FA-SU-E2E-064-resilience-group-role-save-popup-assign-gagal-karena-server-error | Resilience Group Role: Save Popup Assign Gagal karena Server Error | FE+BE. | 14 | TC-FA-SU-211 |
| TC-FA-SU-E2E-065-group-manager-pada-group-role-dialog-remove-konfirmasi-dan-cancel | Group Manager pada Group Role: Dialog Remove, Konfirmasi, dan Cancel | FE+BE. | 37 | TC-FA-SU-212, TC-FA-SU-213, TC-FA-SU-214 |
| TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup | Group Manager: Save 0 Grup, Auto-Revert Beberapa Grup, dan Auto-Revert Tier dari Popup | FE+BE. | 57 | TC-FA-SU-215, TC-FA-SU-216, TC-FA-SU-217 |
| TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup | Kunci Baris Group Role: Target Group Manager, Default User, dan Aktor Ber-scope Grup | FE+BE. | 48 | TC-FA-SU-218, TC-FA-SU-219, TC-FA-SU-220, TC-FA-SU-221 |
| TC-FA-SU-E2E-068-detail-group-assignment-dan-group-dihapus-di-settings-groups | Detail Group Assignment dan Group Dihapus di Settings Groups | FE+BE. | 33 | TC-FA-SU-224, TC-FA-SU-225 |
| TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | Screening Sub-tab Transaction Role dan Modal Assign Transaction Role | FE+BE. | 45 | TC-FA-SU-228, TC-FA-SU-229, TC-FA-SU-230, TC-FA-SU-231, TC-FA-SU-232 |
| TC-FA-SU-E2E-070-modal-assign-transaction-role-ganti-transaction-label-group-dan-popup-tree-group | Modal Assign Transaction Role: Ganti Transaction, Label Group, dan Popup Tree Group | FE+BE. | 28 | TC-FA-SU-233, TC-FA-SU-234, TC-FA-SU-235 |
| TC-FA-SU-E2E-071-modal-assign-transaction-role-katalog-transaction-opsi-role-dan-opsi-disabled | Modal Assign Transaction Role: Katalog Transaction, Opsi Role, dan Opsi Disabled | FE+BE. | 22 | TC-FA-SU-236, TC-FA-SU-237, TC-FA-SU-238 |
| TC-FA-SU-E2E-072-validasi-submit-modal-assign-transaction-role-semua-kosong-sebagian-kosong-dan-clear | Validasi Submit Modal Assign Transaction Role: Semua Kosong, Sebagian Kosong, dan Clear Field | FE+BE. | 24 | TC-FA-SU-239, TC-FA-SU-240, TC-FA-SU-241 |
| TC-FA-SU-E2E-073-penutupan-modal-assign-transaction-role-dengan-isian-dan-aksesibilitas-modal | Penutupan Modal Assign Transaction Role dengan Isian dan Aksesibilitas Modal | FE+BE. | 22 | TC-FA-SU-242, TC-FA-SU-1046 |
| TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga | Assign Transaction Role: Satu Grup, Beberapa Grup, Stay on This Form, dan Naik Tangga | FE+BE. | 56 | TC-FA-SU-243, TC-FA-SU-244, TC-FA-SU-245, TC-FA-SU-246 |
| TC-FA-SU-E2E-075-turun-tangga-dialog-change-transaction-role-konfirmasi-atomik-dan-cancel | Turun Tangga: Dialog Change Transaction Role, Konfirmasi Atomik, dan Cancel | FE+BE. | 29 | TC-FA-SU-247, TC-FA-SU-248, TC-FA-SU-249 |
| TC-FA-SU-E2E-076-dialog-turun-tangga-role-berbeda-per-grup-approver-di-luar-tangga-dan-tangga-dua | Dialog Turun Tangga Role Berbeda per Grup, Approver di Luar Tangga, dan Tangga Dua Tingkat | FE+BE. | 26 | TC-FA-SU-250, TC-FA-SU-251, TC-FA-SU-252 |
| TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | Transaction Role: Save Identik, Guard Server Turun Tangga, Grup Dihapus, Edit Bersamaan, dan Sebagian Grup Identik | FE+BE. | 43 | TC-FA-SU-253, TC-FA-SU-254, TC-FA-SU-256, TC-FA-SU-278, TC-FA-SU-280 |
| TC-FA-SU-E2E-078-resilience-transaction-role-assign-gagal-bulk-remove-atomik-gagal-dan-kegagalan | Resilience Transaction Role: Assign Gagal, Bulk Remove Atomik Gagal, dan Kegagalan Penulisan Log | FE+BE. | 27 | TC-FA-SU-255, TC-FA-SU-269, TC-FA-SU-276 |
| TC-FA-SU-E2E-079-popup-assign-group-transaction-role-screening-tambah-grup-dan-cabut-grup | Popup Assign Group Transaction Role: Screening, Tambah Grup, dan Cabut Grup | FE+BE. | 27 | TC-FA-SU-257, TC-FA-SU-258, TC-FA-SU-259 |
| TC-FA-SU-E2E-080-popup-assign-group-tambah-dan-cabut-sekaligus-cabut-semua-dan-cancel-tanpa-unsaved | Popup Assign Group: Tambah dan Cabut Sekaligus, Cabut Semua, dan Cancel Tanpa Unsaved Changes | FE+BE. | 29 | TC-FA-SU-260, TC-FA-SU-261, TC-FA-SU-262 |
| TC-FA-SU-E2E-081-popup-assign-group-cancel-dialog-d-06-d-07-dan-node-disabled-already-assigned | Popup Assign Group: Cancel Dialog D-06 D-07 dan Node Tidak Disabled (Sudah Ter-assign, Ancestor, Descendant) | FE+BE. | 21 | TC-FA-SU-263, TC-FA-SU-264 |
| TC-FA-SU-E2E-082-remove-satu-baris-transaction-role-cancel-dialog-dan-empty-state-berganti | Remove Satu Baris Transaction Role, Cancel Dialog, dan Empty State Berganti | FE+BE. | 28 | TC-FA-SU-265, TC-FA-SU-266, TC-FA-SU-1050 |
| TC-FA-SU-E2E-083-bulk-remove-transaction-role-counter-dialog-plural-singular-dan-cancel-bulk | Bulk Remove Transaction Role: Counter, Dialog Plural, Singular, dan Cancel Bulk | FE+BE. | 26 | TC-FA-SU-267, TC-FA-SU-268, TC-FA-SU-1048 |
| TC-FA-SU-E2E-084-kunci-transaction-role-bagi-aktor-ber-scope-grup-dan-target-tier | Kunci Transaction Role bagi Aktor Ber-scope Grup dan Target Tier | FE+BE. | 27 | TC-FA-SU-271, TC-FA-SU-273, TC-FA-SU-1060 |
| TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden | Transaction Role: Selection Limit 5, Auto-Revert Tier dari Remove Baris Pola, dan Read Only Hidden | FE+BE. | 35 | TC-FA-SU-270, TC-FA-SU-274, TC-FA-SU-275 |
| TC-FA-SU-E2E-086-transaction-role-sinkronisasi-role-dan-permission-dan-katalog-tanpa-gating-addon | Transaction Role: Sinkronisasi Role & Permission dan Katalog Tanpa Gating Addon | FE+BE. | 21 | TC-FA-SU-277, TC-FA-SU-279 |
| TC-FA-SU-E2E-087-penugasan-grup-ganda-dan-grup-dihapus-sebelum-save-popup-assign-group-role | Penugasan Grup Ganda dan Grup Dihapus Sebelum Save pada Popup Assign Group Role | FE+BE. | 29 | TC-FA-SU-209, TC-FA-SU-210 |
| TC-FA-SU-E2E-088-sinkronisasi-dua-arah-group-role-dan-group-role-tanpa-switch | Sinkronisasi Dua Arah Group Role dan Group Role Tanpa Switch | FE+BE. | 21 | TC-FA-SU-226, TC-FA-SU-227 |
| TC-FA-SU-E2E-089-popup-select-home-group-singular-screening-tombol-select-dan-cancel | Popup Select Home Group Singular: Screening, Tombol Select, dan Cancel | FE+BE. | 33 | TC-FA-SU-281, TC-FA-SU-287, TC-FA-SU-289 |
| TC-FA-SU-E2E-090-role-matrix-visibilitas-edit-home-group-dan-field-home-group-di-detail-user-per-aktor | Role Matrix: Visibilitas Edit Home Group dan Field Home Group di Detail User per Aktor | FE+BE. | 51 | TC-FA-SU-282, TC-FA-SU-284 |
| TC-FA-SU-E2E-091-edit-home-group-single-row-action-ikon-edit-detail-dan-kosongkan-home-group | Edit Home Group Single: Row Action, Ikon Edit Detail, dan Kosongkan Home Group | FE+BE. | 43 | TC-FA-SU-285, TC-FA-SU-286, TC-FA-SU-288 |
| TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan | Constraint Home Group: Dialog Role Outside Constraint, Konfirmasi Revoke, Cancel, dan Pelepasan Constraint | FE+BE. | 50 | TC-FA-SU-290, TC-FA-SU-291, TC-FA-SU-292, TC-FA-SU-293 |
| TC-FA-SU-E2E-093-dialog-gabungan-group-manager-pada-edit-home-group-konfirmasi-cancel-dan-satu-grup | Dialog Gabungan Group Manager pada Edit Home Group: Konfirmasi, Cancel, dan Satu Grup | FE+BE. | 34 | TC-FA-SU-294, TC-FA-SU-295, TC-FA-SU-296 |
| TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage | Dialog Gabungan Beberapa Grup Group Manager, Kunci Baris, dan Notifikasi Auto-Revert | FE+BE. | 42 | TC-FA-SU-297, TC-FA-SU-298, TC-FA-SU-319 |
| TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | Edit Home Group: Grup Dihapus, No-op dari Sesi Lain, Edit Bersamaan, dan Kandidat Picker Role & Permission | FE+BE. | 63 | TC-FA-SU-300, TC-FA-SU-302, TC-FA-SU-316, TC-FA-SU-317, TC-FA-SU-318 |
| TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal | Resilience Edit Home Group: Server Error, Kegagalan Penulisan Log, Bulk Sebagian Gagal, dan Seluruh Gagal | FE+BE. | 50 | TC-FA-SU-301, TC-FA-SU-303, TC-FA-SU-310, TC-FA-SU-311 |
| TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh | Bulk Edit Home Group: Screening Popup Bulk, Sukses Serentak, Sebagian Skip, dan Seluruh Skip | FE+BE. | 51 | TC-FA-SU-306, TC-FA-SU-307, TC-FA-SU-308, TC-FA-SU-309 |
| TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel | Bulk Edit Home Group: Kosongkan, Dialog Gabungan per Pengguna, dan Hasil Cancel | FE+BE. | 54 | TC-FA-SU-312, TC-FA-SU-313, TC-FA-SU-314, TC-FA-SU-315 |
| TC-FA-SU-E2E-099-popup-assign-group-role-kolom-crud-dinamis-setup-column-dan-search | Popup Assign Group Role: Kolom CRUD Dinamis, Setup Column, dan Search | FE+BE. | 20 | TC-FA-SU-895, TC-FA-SU-896, TC-FA-SU-897 |
| TC-FA-SU-E2E-100-popup-select-group-screening-node-ter-assign-disabled-dan-search | Popup Select Group: Screening, Node Ter-assign Disabled, dan Search | FE+BE. | 21 | TC-FA-SU-898, TC-FA-SU-899, TC-FA-SU-900 |
| TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download | Popup Detail Group Assignment: Screening, Pencarian, Setup Column, dan Download | FE+BE. | 42 | TC-FA-SU-901, TC-FA-SU-902, TC-FA-SU-903, TC-FA-SU-1056 |
| TC-FA-SU-E2E-102-popup-select-home-group-role-count-dan-popup-tree-group-search-dan-restriksi-node | Popup Select Home Group, Role Count, dan Popup Tree Group: Search dan Restriksi Node | FE+BE. | 37 | TC-FA-SU-905, TC-FA-SU-906, TC-FA-SU-907 |
| TC-FA-SU-E2E-103-popup-select-home-group-bulk-dan-aksesibilitas-popup-select-home-group | Popup Select Home Group Bulk dan Aksesibilitas Popup Select Home Group | FE+BE. | 23 | TC-FA-SU-908, TC-FA-SU-1047 |
| TC-FA-SU-E2E-104-resilience-download-detail-group-assignment-gagal | Resilience Download Detail Group Assignment Gagal | FE+BE. | 6 | TC-FA-SU-904 |
| TC-FA-SU-E2E-105-edit-home-group-aktor-manage-global-user-dan-role-kunci-baris-group-manager-dan-dialog-gabungan | Edit Home Group oleh Aktor Manage global user & role: Kunci Baris Group Manager dan Dialog Gabungan | FE+BE. | 32 | TC-FA-SU-1068 |
| TC-FA-SU-E2E-106-edit-home-group-target-total-control-dan-read-only-oleh-default-user-dan-manage-global-user-dan-role | Edit Home Group Target Total Control dan Read Only oleh Default User dan Manage global user & role | FE+BE. | 50 | TC-FA-SU-299, TC-FA-SU-1069 |
| TC-FA-SU-E2E-107-kolom-curated-user-list-urutan-setelah-last-updated-dan-kolom-tag-pada-plan-starter | Kolom Curated User List: Urutan Setelah Last Updated dan Kolom TAG pada Plan Starter | FE+BE. | 9 | TC-FA-SU-366 |
| TC-FA-SU-E2E-108-label-role-count-modified-by-dan-last-updated-mengikuti-aksi-dan-temporary-until-non | Label Role Count pada User List: Dihitung per Assignment dan Mengikuti Assignment Baru | FE+BE. | 30 | TC-FA-SU-369, TC-FA-SU-370 |
| TC-FA-SU-E2E-109-pengguna-tanpa-app-access-atribut-identitas-read-only-dan-sidebar-group-tree-sebagai | Pengguna Tanpa App Access dan Atribut Identitas Read-only | FE+BE. | 26 | TC-FA-SU-373, TC-FA-SU-374 |
| TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all | Bulk Actions Bar User List: Screening Empat Elemen, Ikon Severity, dan Label Select All | FE+BE. | 37 | TC-FA-SU-1041, TC-FA-SU-1042, TC-FA-SU-1043 |
| TC-FA-SU-E2E-111-name-teks-panjang-header-satu-baris-dan-state-preservation-filter-status-dan-halaman | Name Teks Panjang, Header Satu Baris, dan State Preservation Filter Status dan Halaman | FE+BE. | 28 | TC-FA-SU-1051, TC-FA-SU-1052, TC-FA-SU-1057 |
| TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action | Setup Column Sub-tab Global Role dan Group Role, Sort Role, serta Tools Sub-tab Role | FE+BE. | 32 | TC-FA-SU-376, TC-FA-SU-379, TC-FA-SU-380, TC-FA-SU-381 |
| TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab | Group Summary Badge Sub-tab Group Role, Sort Kolom Group, Ikon Changelog Sub-tab Role, dan Ikon Row Action | FE+BE. | 38 | TC-FA-SU-377, TC-FA-SU-378, TC-FA-SU-382, TC-FA-SU-1044 |
| TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search | Tabel User List: Screening dan Search | FE+BE. | 26 | TC-FA-SU-320, TC-FA-SU-321, TC-FA-SU-322, TC-FA-SU-323 |
| TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1 | Tabel User List: Search (Bagian 1) | FE+BE. | 18 | TC-FA-SU-324, TC-FA-SU-325, TC-FA-SU-326, TC-FA-SU-327 |
| TC-FA-SU-E2E-116-tabel-user-list-search-bagian-2 | Tabel User List: Search (Bagian 2) | FE+BE. | 45 | TC-FA-SU-328, TC-FA-SU-329, TC-FA-SU-330 |
| TC-FA-SU-E2E-117-tabel-user-list-sort-bagian-1 | Tabel User List: Sort (Bagian 1) | FE+BE. | 21 | TC-FA-SU-331, TC-FA-SU-332, TC-FA-SU-333 |
| TC-FA-SU-E2E-118-tabel-user-list-sort-bagian-2 | Tabel User List: Sort (Bagian 2) | FE+BE. | 21 | TC-FA-SU-334, TC-FA-SU-335, TC-FA-SU-336 |
| TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3 | Tabel User List: Sort (Bagian 3) | FE+BE. | 26 | TC-FA-SU-337, TC-FA-SU-338, TC-FA-SU-339, TC-FA-SU-1053 |
| TC-FA-SU-E2E-120-tabel-user-list-filter-dan-kontrol-filter-bagian-1 | Tabel User List: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 29 | TC-FA-SU-340, TC-FA-SU-341, TC-FA-SU-342 |
| TC-FA-SU-E2E-121-tabel-user-list-filter-dan-kontrol-filter-bagian-2 | Tabel User List: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 21 | TC-FA-SU-343, TC-FA-SU-344, TC-FA-SU-345 |
| TC-FA-SU-E2E-122-tabel-user-list-filter-dan-kontrol-filter-bagian-3 | Tabel User List: Filter dan Kontrol Filter (Bagian 3) | FE+BE. | 48 | TC-FA-SU-346, TC-FA-SU-347, TC-FA-SU-348 |
| TC-FA-SU-E2E-123-tabel-user-list-filter-dan-kontrol-filter-dan-setup-column | Tabel User List: Chip Filter, Overlay Column Visibility, dan Screening Setup Column | FE+BE. | 29 | TC-FA-SU-349, TC-FA-SU-350, TC-FA-SU-351 |
| TC-FA-SU-E2E-124-tabel-user-list-setup-column-bagian-1 | Tabel User List: Setup Column (Bagian 1) | FE+BE. | 38 | TC-FA-SU-352, TC-FA-SU-353 |
| TC-FA-SU-E2E-125-tabel-user-list-setup-column-bagian-2 | Tabel User List: Setup Column (Bagian 2) | FE+BE. | 34 | TC-FA-SU-354, TC-FA-SU-355 |
| TC-FA-SU-E2E-126-tabel-user-list-setup-column-bagian-3 | Tabel User List: Setup Column (Bagian 3) | FE+BE. | 44 | TC-FA-SU-356, TC-FA-SU-357, TC-FA-SU-358 |
| TC-FA-SU-E2E-127-tabel-user-list-pagination-tooltip-icon-dan-download | Tabel User List: Pagination, Tooltip Icon, dan Download | FE+BE. | 38 | TC-FA-SU-359, TC-FA-SU-360, TC-FA-SU-364 |
| TC-FA-SU-E2E-128-tabel-user-list-download | Tabel User List: Download | FE+BE. | 20 | TC-FA-SU-361 |
| TC-FA-SU-E2E-129-modified-by-last-updated-mengikuti-aksi-dan-temporary-until-non-temporary-user-list | Modified By dan Last Updated Mengikuti Aksi Terakhir, dan Temporary Until Pengguna Non-temporary | FE+BE. | 28 | TC-FA-SU-371, TC-FA-SU-372 |
| TC-FA-SU-E2E-130-node-sidebar-group-tree-sebagai-kriteria-data-search-filter-seleksi-select-all-dan-download | Node Sidebar Group Tree sebagai Kriteria Data: Search, Filter, Seleksi, Select All, dan Download | FE+BE. | 25 | TC-FA-SU-375 |
| TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search | Sub-tab Transaction Role: Screening dan Search | FE+BE. | 62 | TC-FA-SU-383, TC-FA-SU-384, TC-FA-SU-385, TC-FA-SU-386 |
| TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | Sub-tab Transaction Role: Search, Sort, dan Filter dan Kontrol Filter | FE+BE. | 42 | TC-FA-SU-387, TC-FA-SU-388, TC-FA-SU-389, TC-FA-SU-390, TC-FA-SU-391 |
| TC-FA-SU-E2E-133-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-1 | Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 49 | TC-FA-SU-392, TC-FA-SU-393, TC-FA-SU-394 |
| TC-FA-SU-E2E-134-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-2 | Sub-tab Transaction Role: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 30 | TC-FA-SU-395 |
| TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column | Sub-tab Transaction Role: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 57 | TC-FA-SU-398, TC-FA-SU-399, TC-FA-SU-400, TC-FA-SU-409 |
| TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column | Sub-tab Transaction Role: Setup Column | FE+BE. | 86 | TC-FA-SU-401, TC-FA-SU-402, TC-FA-SU-403, TC-FA-SU-408 |
| TC-FA-SU-E2E-137-sub-tab-transaction-role-pagination-tooltip-icon-dan-state-per-sub-tab | Sub-tab Transaction Role: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 50 | TC-FA-SU-404, TC-FA-SU-405, TC-FA-SU-407 |
| TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search | Sub-tab Borrowed Assets: Screening dan Search | FE+BE. | 39 | TC-FA-SU-410, TC-FA-SU-411, TC-FA-SU-412, TC-FA-SU-413 |
| TC-FA-SU-E2E-139-sub-tab-borrowed-assets-search | Sub-tab Borrowed Assets: Search | FE+BE. | 47 | TC-FA-SU-414, TC-FA-SU-415, TC-FA-SU-416 |
| TC-FA-SU-E2E-140-sub-tab-borrowed-assets-sort | Sub-tab Borrowed Assets: Sort | FE+BE. | 20 | TC-FA-SU-417, TC-FA-SU-418, TC-FA-SU-419 |
| TC-FA-SU-E2E-141-sub-tab-borrowed-assets-sort-dan-filter-dan-kontrol-filter | Sub-tab Borrowed Assets: Sort dan Filter dan Kontrol Filter | FE+BE. | 29 | TC-FA-SU-420, TC-FA-SU-421, TC-FA-SU-422 |
| TC-FA-SU-E2E-142-sub-tab-borrowed-assets-filter-dan-kontrol-filter | Sub-tab Borrowed Assets: Filter dan Kontrol Filter | FE+BE. | 59 | TC-FA-SU-423, TC-FA-SU-424, TC-FA-SU-425 |
| TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column | Sub-tab Borrowed Assets: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 75 | TC-FA-SU-426, TC-FA-SU-427, TC-FA-SU-428, TC-FA-SU-429 |
| TC-FA-SU-E2E-144-sub-tab-borrowed-assets-setup-column-bagian-1 | Sub-tab Borrowed Assets: Setup Column (Bagian 1) | FE+BE. | 24 | TC-FA-SU-430, TC-FA-SU-431 |
| TC-FA-SU-E2E-145-sub-tab-borrowed-assets-setup-column-bagian-2 | Sub-tab Borrowed Assets: Setup Column (Bagian 2) | FE+BE. | 26 | TC-FA-SU-433 |
| TC-FA-SU-E2E-146-sub-tab-borrowed-assets-pagination-tooltip-icon-dan-state-per-sub-tab | Sub-tab Borrowed Assets: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 49 | TC-FA-SU-434, TC-FA-SU-439, TC-FA-SU-441 |
| TC-FA-SU-E2E-147-sub-tab-borrowed-assets-download | Sub-tab Borrowed Assets: Download | FE+BE. | 54 | TC-FA-SU-435, TC-FA-SU-436 |
| TC-FA-SU-E2E-148-sub-tab-borrowed-assets-setup-column-pin-dan-unpin | Sub-tab Borrowed Assets: Setup Column Pin dan Unpin | FE+BE. | 41 | TC-FA-SU-432 |
| TC-FA-SU-E2E-149-sub-tab-transaction-role-perilaku-filter-panel-dan-chip-dropdown-filter | Sub-tab Transaction Role: Perilaku Filter Panel dan Chip Dropdown Filter | FE+BE. | 55 | TC-FA-SU-396, TC-FA-SU-397 |
| TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search | Sub-tab Assigned Assets: Screening dan Search | FE+BE. | 41 | TC-FA-SU-442, TC-FA-SU-443, TC-FA-SU-444, TC-FA-SU-445 |
| TC-FA-SU-E2E-151-sub-tab-assigned-assets-search | Sub-tab Assigned Assets: Search | FE+BE. | 40 | TC-FA-SU-446, TC-FA-SU-447 |
| TC-FA-SU-E2E-152-sub-tab-assigned-assets-sort | Sub-tab Assigned Assets: Sort | FE+BE. | 18 | TC-FA-SU-448, TC-FA-SU-449, TC-FA-SU-450 |
| TC-FA-SU-E2E-153-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-1 | Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 23 | TC-FA-SU-451, TC-FA-SU-452 |
| TC-FA-SU-E2E-154-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-2 | Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 52 | TC-FA-SU-453, TC-FA-SU-454 |
| TC-FA-SU-E2E-155-sub-tab-assigned-assets-filter-dan-kontrol-filter-dan-setup-column | Sub-tab Assigned Assets: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 48 | TC-FA-SU-456, TC-FA-SU-457, TC-FA-SU-458 |
| TC-FA-SU-E2E-156-sub-tab-assigned-assets-setup-column-bagian-1 | Sub-tab Assigned Assets: Setup Column (Bagian 1) | FE+BE. | 41 | TC-FA-SU-459, TC-FA-SU-460 |
| TC-FA-SU-E2E-157-sub-tab-assigned-assets-setup-column-bagian-2 | Sub-tab Assigned Assets: Setup Column (Bagian 2) | FE+BE. | 55 | TC-FA-SU-461, TC-FA-SU-462 |
| TC-FA-SU-E2E-158-sub-tab-assigned-assets-pagination-tooltip-icon-dan-state-per-sub-tab | Sub-tab Assigned Assets: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 65 | TC-FA-SU-463, TC-FA-SU-468, TC-FA-SU-470 |
| TC-FA-SU-E2E-159-sub-tab-assigned-assets-download | Sub-tab Assigned Assets: Download | FE+BE. | 50 | TC-FA-SU-464, TC-FA-SU-465 |
| TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search | Sub-tab Pending Approvals: Screening dan Search | FE+BE. | 60 | TC-FA-SU-471, TC-FA-SU-472, TC-FA-SU-473, TC-FA-SU-474 |
| TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | Sub-tab Pending Approvals: Search dan Sort | FE+BE. | 23 | TC-FA-SU-475, TC-FA-SU-476, TC-FA-SU-477, TC-FA-SU-478, TC-FA-SU-479 |
| TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1 | Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 29 | TC-FA-SU-480, TC-FA-SU-481, TC-FA-SU-482, TC-FA-SU-483 |
| TC-FA-SU-E2E-163-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-2 | Sub-tab Pending Approvals: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 84 | TC-FA-SU-484, TC-FA-SU-485, TC-FA-SU-486 |
| TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column | Sub-tab Pending Approvals: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 75 | TC-FA-SU-487, TC-FA-SU-488, TC-FA-SU-489, TC-FA-SU-490 |
| TC-FA-SU-E2E-165-sub-tab-pending-approvals-setup-column | Sub-tab Pending Approvals: Setup Column | FE+BE. | 44 | TC-FA-SU-491, TC-FA-SU-493 |
| TC-FA-SU-E2E-166-sub-tab-pending-approvals-pagination-tooltip-icon-dan-state-per-sub-tab | Sub-tab Pending Approvals: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 65 | TC-FA-SU-494, TC-FA-SU-499, TC-FA-SU-501 |
| TC-FA-SU-E2E-167-sub-tab-pending-approvals-download | Sub-tab Pending Approvals: Download | FE+BE. | 50 | TC-FA-SU-495, TC-FA-SU-496 |
| TC-FA-SU-E2E-168-sub-tab-pending-approvals-pin-dan-unpin-setup-column | Sub-tab Pending Approvals: Pin dan Unpin Setup Column | FE+BE. | 25 | TC-FA-SU-492 |
| TC-FA-SU-E2E-169-sub-tab-assigned-assets-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | Sub-tab Assigned Assets: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong) | FE+BE. | 34 | TC-FA-SU-455 |
| TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | Sub-tab Pending Tasks: Screening dan Search | FE+BE. | 33 | TC-FA-SU-502, TC-FA-SU-503, TC-FA-SU-504, TC-FA-SU-505, TC-FA-SU-506, TC-FA-SU-507 |
| TC-FA-SU-E2E-171-sub-tab-pending-tasks-search | Sub-tab Pending Tasks: Search | FE+BE. | 43 | TC-FA-SU-508, TC-FA-SU-509, TC-FA-SU-510 |
| TC-FA-SU-E2E-172-sub-tab-pending-tasks-sort | Sub-tab Pending Tasks: Sort | FE+BE. | 19 | TC-FA-SU-511, TC-FA-SU-512, TC-FA-SU-513 |
| TC-FA-SU-E2E-173-sub-tab-pending-tasks-sort-dan-filter-dan-kontrol-filter | Sub-tab Pending Tasks: Sort dan Filter dan Kontrol Filter | FE+BE. | 29 | TC-FA-SU-514, TC-FA-SU-515, TC-FA-SU-516 |
| TC-FA-SU-E2E-174-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-1 | Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 32 | TC-FA-SU-517, TC-FA-SU-518, TC-FA-SU-519 |
| TC-FA-SU-E2E-175-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-2 | Sub-tab Pending Tasks: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 40 | TC-FA-SU-520, TC-FA-SU-521 |
| TC-FA-SU-E2E-176-sub-tab-pending-tasks-filter-dan-kontrol-filter-dan-setup-column | Sub-tab Pending Tasks: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 38 | TC-FA-SU-523, TC-FA-SU-524, TC-FA-SU-525 |
| TC-FA-SU-E2E-177-sub-tab-pending-tasks-setup-column-bagian-1 | Sub-tab Pending Tasks: Setup Column (Bagian 1) | FE+BE. | 24 | TC-FA-SU-526, TC-FA-SU-527 |
| TC-FA-SU-E2E-178-sub-tab-pending-tasks-setup-column-bagian-2 | Sub-tab Pending Tasks: Setup Column (Bagian 2) | FE+BE. | 45 | TC-FA-SU-528, TC-FA-SU-529 |
| TC-FA-SU-E2E-179-sub-tab-pending-tasks-pagination-tooltip-icon-dan-state-per-sub-tab | Sub-tab Pending Tasks: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 40 | TC-FA-SU-530, TC-FA-SU-535, TC-FA-SU-537 |
| TC-FA-SU-E2E-180-sub-tab-pending-tasks-download | Sub-tab Pending Tasks: Download | FE+BE. | 35 | TC-FA-SU-531, TC-FA-SU-532 |
| TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search | Tab Non-Login User: Screening dan Search | FE+BE. | 28 | TC-FA-SU-538, TC-FA-SU-539, TC-FA-SU-540, TC-FA-SU-541 |
| TC-FA-SU-E2E-182-tab-non-login-user-search | Tab Non-Login User: Search | FE+BE. | 45 | TC-FA-SU-542, TC-FA-SU-543, TC-FA-SU-544, TC-FA-SU-1058 |
| TC-FA-SU-E2E-183-tab-non-login-user-search-dan-sort | Tab Non-Login User: Search dan Sort | FE+BE. | 19 | TC-FA-SU-545, TC-FA-SU-546, TC-FA-SU-1033 |
| TC-FA-SU-E2E-184-tab-non-login-user-sort | Tab Non-Login User: Sort | FE+BE. | 35 | TC-FA-SU-547, TC-FA-SU-548, TC-FA-SU-549, TC-FA-SU-550, TC-FA-SU-1034 |
| TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1 | Tab Non-Login User: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 46 | TC-FA-SU-551, TC-FA-SU-552, TC-FA-SU-553, TC-FA-SU-554 |
| TC-FA-SU-E2E-186-tab-non-login-user-filter-dan-kontrol-filter-bagian-2 | Tab Non-Login User: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 41 | TC-FA-SU-555, TC-FA-SU-556 |
| TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column | Tab Non-Login User: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 46 | TC-FA-SU-558, TC-FA-SU-559, TC-FA-SU-560, TC-FA-SU-1035 |
| TC-FA-SU-E2E-188-tab-non-login-user-setup-column-bagian-1 | Tab Non-Login User: Setup Column (Bagian 1) | FE+BE. | 24 | TC-FA-SU-561, TC-FA-SU-562 |
| TC-FA-SU-E2E-189-tab-non-login-user-setup-column-bagian-2 | Tab Non-Login User: Setup Column (Bagian 2) | FE+BE. | 49 | TC-FA-SU-563, TC-FA-SU-564, TC-FA-SU-565 |
| TC-FA-SU-E2E-190-tab-non-login-user-setup-column-dan-pagination | Tab Non-Login User: Setup Column dan Pagination | FE+BE. | 51 | TC-FA-SU-566, TC-FA-SU-567, TC-FA-SU-568 |
| TC-FA-SU-E2E-191-tab-non-login-user-tooltip-icon-dan-download | Tab Non-Login User: Tooltip Icon dan Download | FE+BE. | 42 | TC-FA-SU-569, TC-FA-SU-570, TC-FA-SU-573 |
| TC-FA-SU-E2E-192-sub-tab-pending-tasks-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | Sub-tab Pending Tasks: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong) | FE+BE. | 26 | TC-FA-SU-522 |
| TC-FA-SU-E2E-193-tab-non-login-user-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | Tab Non-Login User: Perilaku Filter Panel (Tutup Tanpa Apply, Indikator Titik, dan Nilai Kosong) | FE+BE. | 28 | TC-FA-SU-557 |
| TC-FA-SU-E2E-194-tab-changelog-screening-dan-search | Tab Changelog: Screening dan Search | FE+BE. | 37 | TC-FA-SU-575, TC-FA-SU-576, TC-FA-SU-577, TC-FA-SU-578 |
| TC-FA-SU-E2E-195-tab-changelog-search-dan-sort | Tab Changelog: Search dan Sort | FE+BE. | 47 | TC-FA-SU-579, TC-FA-SU-580, TC-FA-SU-581, TC-FA-SU-582 |
| TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter | Tab Changelog: Sort dan Filter dan Kontrol Filter | FE+BE. | 43 | TC-FA-SU-583, TC-FA-SU-584, TC-FA-SU-585, TC-FA-SU-586 |
| TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1 | Tab Changelog: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 43 | TC-FA-SU-587, TC-FA-SU-588, TC-FA-SU-589, TC-FA-SU-590 |
| TC-FA-SU-E2E-198-tab-changelog-filter-dan-kontrol-filter-bagian-2 | Tab Changelog: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 67 | TC-FA-SU-591, TC-FA-SU-592, TC-FA-SU-593 |
| TC-FA-SU-E2E-199-tab-changelog-setup-column | Tab Changelog: Setup Column | FE+BE. | 38 | TC-FA-SU-594, TC-FA-SU-595, TC-FA-SU-596, TC-FA-SU-597 |
| TC-FA-SU-E2E-200-tab-changelog-setup-column-dan-pagination | Tab Changelog: Setup Column dan Pagination | FE+BE. | 36 | TC-FA-SU-599, TC-FA-SU-600 |
| TC-FA-SU-E2E-201-tab-changelog-tooltip-icon-dan-download | Tab Changelog: Tooltip Icon dan Download | FE+BE. | 46 | TC-FA-SU-601, TC-FA-SU-602, TC-FA-SU-605 |
| TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search | Modal Changelog User > Global Role: Screening dan Search | FE+BE. | 40 | TC-FA-SU-607, TC-FA-SU-608, TC-FA-SU-609, TC-FA-SU-610 |
| TC-FA-SU-E2E-203-modal-changelog-user-global-role-search | Modal Changelog User > Global Role: Search | FE+BE. | 42 | TC-FA-SU-611, TC-FA-SU-612, TC-FA-SU-1059 |
| TC-FA-SU-E2E-204-modal-changelog-user-global-role-search-dan-sort | Modal Changelog User > Global Role: Search dan Sort | FE+BE. | 34 | TC-FA-SU-613, TC-FA-SU-614, TC-FA-SU-615 |
| TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter | Modal Changelog User > Global Role: Sort dan Filter dan Kontrol Filter | FE+BE. | 36 | TC-FA-SU-616, TC-FA-SU-617, TC-FA-SU-618, TC-FA-SU-619 |
| TC-FA-SU-E2E-206-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-1 | Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 43 | TC-FA-SU-620, TC-FA-SU-621, TC-FA-SU-622 |
| TC-FA-SU-E2E-207-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-2 | Modal Changelog User > Global Role: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 67 | TC-FA-SU-623, TC-FA-SU-624, TC-FA-SU-625 |
| TC-FA-SU-E2E-208-modal-changelog-user-global-role-setup-column-bagian-1 | Modal Changelog User > Global Role: Setup Column (Bagian 1) | FE+BE. | 29 | TC-FA-SU-626, TC-FA-SU-627, TC-FA-SU-628 |
| TC-FA-SU-E2E-209-modal-changelog-user-global-role-setup-column-bagian-2 | Modal Changelog User > Global Role: Setup Column (Bagian 2) | FE+BE. | 9 | TC-FA-SU-629 |
| TC-FA-SU-E2E-210-modal-changelog-user-global-role-setup-column-pagination-dan-tooltip-icon | Modal Changelog User > Global Role: Setup Column, Pagination, dan Tooltip Icon | FE+BE. | 43 | TC-FA-SU-631, TC-FA-SU-632, TC-FA-SU-637 |
| TC-FA-SU-E2E-211-modal-changelog-user-global-role-download | Modal Changelog User > Global Role: Download | FE+BE. | 37 | TC-FA-SU-633, TC-FA-SU-634 |
| TC-FA-SU-E2E-212-tab-changelog-pin-dan-unpin-setup-column | Tab Changelog: Pin dan Unpin Setup Column | FE+BE. | 14 | TC-FA-SU-598 |
| TC-FA-SU-E2E-213-modal-changelog-user-global-role-pin-dan-unpin-setup-column | Modal Changelog User > Global Role: Pin dan Unpin Setup Column | FE+BE. | 14 | TC-FA-SU-630 |
| TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search | Modal Changelog User > Group Role: Screening dan Search | FE+BE. | 37 | TC-FA-SU-639, TC-FA-SU-640, TC-FA-SU-641, TC-FA-SU-642 |
| TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort | Modal Changelog User > Group Role: Search dan Sort | FE+BE. | 47 | TC-FA-SU-643, TC-FA-SU-644, TC-FA-SU-645, TC-FA-SU-646 |
| TC-FA-SU-E2E-216-modal-changelog-user-group-role-sort-dan-filter-dan-kontrol-filter | Modal Changelog User > Group Role: Sort dan Filter dan Kontrol Filter | FE+BE. | 42 | TC-FA-SU-647, TC-FA-SU-648, TC-FA-SU-649, TC-FA-SU-650 |
| TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1 | Modal Changelog User > Group Role: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 40 | TC-FA-SU-651, TC-FA-SU-652, TC-FA-SU-653, TC-FA-SU-654 |
| TC-FA-SU-E2E-218-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-2 | Modal Changelog User > Group Role: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 67 | TC-FA-SU-655, TC-FA-SU-656, TC-FA-SU-657 |
| TC-FA-SU-E2E-219-modal-changelog-user-group-role-setup-column | Modal Changelog User > Group Role: Setup Column | FE+BE. | 41 | TC-FA-SU-658, TC-FA-SU-659, TC-FA-SU-660, TC-FA-SU-661 |
| TC-FA-SU-E2E-220-modal-changelog-user-group-role-setup-column-dan-pagination | Modal Changelog User > Group Role: Setup Column dan Pagination | FE+BE. | 35 | TC-FA-SU-663, TC-FA-SU-664 |
| TC-FA-SU-E2E-221-modal-changelog-user-group-role-tooltip-icon-dan-download | Modal Changelog User > Group Role: Tooltip Icon dan Download | FE+BE. | 45 | TC-FA-SU-665, TC-FA-SU-666, TC-FA-SU-669 |
| TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search | Modal Changelog User > Transaction Role: Screening dan Search | FE+BE. | 37 | TC-FA-SU-671, TC-FA-SU-672, TC-FA-SU-673, TC-FA-SU-674 |
| TC-FA-SU-E2E-223-modal-changelog-user-transaction-role-search-dan-sort | Modal Changelog User > Transaction Role: Search dan Sort | FE+BE. | 47 | TC-FA-SU-675, TC-FA-SU-676, TC-FA-SU-677, TC-FA-SU-678 |
| TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter | Modal Changelog User > Transaction Role: Sort dan Filter dan Kontrol Filter | FE+BE. | 42 | TC-FA-SU-679, TC-FA-SU-680, TC-FA-SU-681, TC-FA-SU-682 |
| TC-FA-SU-E2E-225-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-1 | Modal Changelog User > Transaction Role: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 40 | TC-FA-SU-683, TC-FA-SU-684, TC-FA-SU-685, TC-FA-SU-686 |
| TC-FA-SU-E2E-226-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-2 | Modal Changelog User > Transaction Role: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 67 | TC-FA-SU-687, TC-FA-SU-688, TC-FA-SU-689 |
| TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column | Modal Changelog User > Transaction Role: Setup Column | FE+BE. | 41 | TC-FA-SU-690, TC-FA-SU-691, TC-FA-SU-692, TC-FA-SU-693 |
| TC-FA-SU-E2E-228-modal-changelog-user-transaction-role-setup-column-dan-pagination | Modal Changelog User > Transaction Role: Setup Column dan Pagination | FE+BE. | 35 | TC-FA-SU-695, TC-FA-SU-696 |
| TC-FA-SU-E2E-229-modal-changelog-user-transaction-role-tooltip-icon-dan-download | Modal Changelog User > Transaction Role: Tooltip Icon dan Download | FE+BE. | 45 | TC-FA-SU-697, TC-FA-SU-698, TC-FA-SU-701 |
| TC-FA-SU-E2E-230-modal-changelog-user-group-role-pin-dan-unpin-setup-column | Modal Changelog User > Group Role: Pin dan Unpin Setup Column | FE+BE. | 14 | TC-FA-SU-662 |
| TC-FA-SU-E2E-231-modal-changelog-user-transaction-role-pin-dan-unpin-setup-column | Modal Changelog User > Transaction Role: Pin dan Unpin Setup Column | FE+BE. | 14 | TC-FA-SU-694 |
| TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search | Modal Combined Changelog: User: Screening dan Search | FE+BE. | 40 | TC-FA-SU-703, TC-FA-SU-704, TC-FA-SU-705, TC-FA-SU-706 |
| TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort | Modal Combined Changelog: User: Search dan Sort | FE+BE. | 47 | TC-FA-SU-707, TC-FA-SU-708, TC-FA-SU-709, TC-FA-SU-710 |
| TC-FA-SU-E2E-234-modal-combined-changelog-user-sort | Modal Combined Changelog: User: Sort | FE+BE. | 37 | TC-FA-SU-711, TC-FA-SU-712, TC-FA-SU-713 |
| TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1 | Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 44 | TC-FA-SU-714, TC-FA-SU-715, TC-FA-SU-716, TC-FA-SU-717 |
| TC-FA-SU-E2E-236-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-2 | Modal Combined Changelog: User: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 64 | TC-FA-SU-718, TC-FA-SU-719, TC-FA-SU-720 |
| TC-FA-SU-E2E-237-modal-combined-changelog-user-filter-dan-kontrol-filter-dan-setup-column | Modal Combined Changelog: User: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 30 | TC-FA-SU-721, TC-FA-SU-722, TC-FA-SU-723 |
| TC-FA-SU-E2E-238-modal-combined-changelog-user-setup-column-bagian-1 | Modal Combined Changelog: User: Setup Column (Bagian 1) | FE+BE. | 20 | TC-FA-SU-724 |
| TC-FA-SU-E2E-239-modal-combined-changelog-user-setup-column-bagian-2 | Modal Combined Changelog: User: Setup Column (Bagian 2) | FE+BE. | 25 | TC-FA-SU-725, TC-FA-SU-727 |
| TC-FA-SU-E2E-240-modal-combined-changelog-user-pagination-tooltip-icon-dan-download | Modal Combined Changelog: User: Pagination, Tooltip Icon, dan Download | FE+BE. | 43 | TC-FA-SU-728, TC-FA-SU-729, TC-FA-SU-733 |
| TC-FA-SU-E2E-241-modal-combined-changelog-user-download | Modal Combined Changelog: User: Download | FE+BE. | 24 | TC-FA-SU-730 |
| TC-FA-SU-E2E-242-tab-system-log-screening-dan-search | Tab System Log: Screening dan Search | FE+BE. | 40 | TC-FA-SU-735, TC-FA-SU-736, TC-FA-SU-737 |
| TC-FA-SU-E2E-243-tab-system-log-search-dan-sort | Tab System Log: Search dan Sort | FE+BE. | 47 | TC-FA-SU-738, TC-FA-SU-739, TC-FA-SU-740, TC-FA-SU-741 |
| TC-FA-SU-E2E-244-tab-system-log-sort | Tab System Log: Sort | FE+BE. | 38 | TC-FA-SU-742, TC-FA-SU-743 |
| TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1 | Tab System Log: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 45 | TC-FA-SU-744, TC-FA-SU-745, TC-FA-SU-746, TC-FA-SU-747 |
| TC-FA-SU-E2E-246-tab-system-log-filter-dan-kontrol-filter-bagian-2 | Tab System Log: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 65 | TC-FA-SU-748, TC-FA-SU-749, TC-FA-SU-750 |
| TC-FA-SU-E2E-247-tab-system-log-filter-dan-kontrol-filter-dan-setup-column | Tab System Log: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 31 | TC-FA-SU-751, TC-FA-SU-752, TC-FA-SU-753 |
| TC-FA-SU-E2E-248-tab-system-log-setup-column-bagian-1 | Tab System Log: Setup Column (Bagian 1) | FE+BE. | 21 | TC-FA-SU-754 |
| TC-FA-SU-E2E-249-tab-system-log-setup-column-bagian-2 | Tab System Log: Setup Column (Bagian 2) | FE+BE. | 27 | TC-FA-SU-755, TC-FA-SU-757 |
| TC-FA-SU-E2E-250-tab-system-log-pagination-tooltip-icon-dan-download | Tab System Log: Pagination, Tooltip Icon, dan Download | FE+BE. | 44 | TC-FA-SU-758, TC-FA-SU-759, TC-FA-SU-763 |
| TC-FA-SU-E2E-251-tab-system-log-download | Tab System Log: Download | FE+BE. | 25 | TC-FA-SU-760 |
| TC-FA-SU-E2E-252-modal-combined-changelog-user-setup-column-pin-dan-unpin | Modal Combined Changelog: User: Setup Column Pin dan Unpin | FE+BE. | 13 | TC-FA-SU-726 |
| TC-FA-SU-E2E-253-tab-system-log-setup-column-pin-dan-unpin | Tab System Log: Setup Column Pin dan Unpin | FE+BE. | 14 | TC-FA-SU-756 |
| TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search | Tab Transaction Admin Log: Screening dan Search | FE+BE. | 38 | TC-FA-SU-765, TC-FA-SU-766, TC-FA-SU-767, TC-FA-SU-768 |
| TC-FA-SU-E2E-255-tab-transaction-admin-log-search | Tab Transaction Admin Log: Search | FE+BE. | 45 | TC-FA-SU-769, TC-FA-SU-770, TC-FA-SU-771 |
| TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter | Tab Transaction Admin Log: Sort dan Filter dan Kontrol Filter | FE+BE. | 42 | TC-FA-SU-772, TC-FA-SU-773, TC-FA-SU-774, TC-FA-SU-775 |
| TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1 | Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 1) | FE+BE. | 38 | TC-FA-SU-776, TC-FA-SU-777, TC-FA-SU-778 |
| TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2 | Tab Transaction Admin Log: Filter dan Kontrol Filter (Bagian 2) | FE+BE. | 62 | TC-FA-SU-779, TC-FA-SU-780, TC-FA-SU-781 |
| TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column | Tab Transaction Admin Log: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 50 | TC-FA-SU-782, TC-FA-SU-783, TC-FA-SU-784, TC-FA-SU-785 |
| TC-FA-SU-E2E-260-tab-transaction-admin-log-setup-column | Tab Transaction Admin Log: Setup Column (Drag Reorder dan Reset to Default) | FE+BE. | 26 | TC-FA-SU-786, TC-FA-SU-788 |
| TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-tooltip-icon-dan-state-per-sub-tab | Tab Transaction Admin Log: Pagination, Tooltip Icon, dan State per Sub-tab | FE+BE. | 51 | TC-FA-SU-789, TC-FA-SU-794, TC-FA-SU-796 |
| TC-FA-SU-E2E-262-tab-transaction-admin-log-download-dan-struktur-sub-tab | Tab Transaction Admin Log: Download dan Struktur Sub-tab | FE+BE. | 59 | TC-FA-SU-790, TC-FA-SU-791, TC-FA-SU-797 |
| TC-FA-SU-E2E-263-tab-transaction-admin-log-struktur-sub-tab-bagian-1 | Tab Transaction Admin Log: Struktur Sub-tab (Bagian 1) | FE+BE. | 48 | TC-FA-SU-798, TC-FA-SU-799 |
| TC-FA-SU-E2E-264-tab-transaction-admin-log-struktur-sub-tab-bagian-2 | Tab Transaction Admin Log: Struktur Sub-tab (Bagian 2) | FE+BE. | 48 | TC-FA-SU-800, TC-FA-SU-801 |
| TC-FA-SU-E2E-265-tab-transaction-admin-log-struktur-sub-tab-bagian-3 | Tab Transaction Admin Log: Struktur Sub-tab (Bagian 3) | FE+BE. | 48 | TC-FA-SU-802, TC-FA-SU-803 |
| TC-FA-SU-E2E-266-tab-transaction-admin-log-struktur-sub-tab-bagian-4 | Tab Transaction Admin Log: Struktur Sub-tab (Bagian 4) | FE+BE. | 25 | TC-FA-SU-804 |
| TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search | Tab User Log sub-tab Borrow: Screening dan Search | FE+BE. | 35 | TC-FA-SU-805, TC-FA-SU-806, TC-FA-SU-807, TC-FA-SU-808 |
| TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort | Tab User Log sub-tab Borrow: Search dan Sort | FE+BE. | 51 | TC-FA-SU-809, TC-FA-SU-810, TC-FA-SU-811, TC-FA-SU-812 |
| TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | Tab User Log sub-tab Borrow: Sort dan Filter dan Kontrol Filter | FE+BE. | 38 | TC-FA-SU-813, TC-FA-SU-814, TC-FA-SU-815, TC-FA-SU-816, TC-FA-SU-817 |
| TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter | Tab User Log sub-tab Borrow: Filter dan Kontrol Filter | FE+BE. | 53 | TC-FA-SU-818, TC-FA-SU-819, TC-FA-SU-820, TC-FA-SU-821 |
| TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column | Tab User Log sub-tab Borrow: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 55 | TC-FA-SU-822, TC-FA-SU-823, TC-FA-SU-824, TC-FA-SU-825 |
| TC-FA-SU-E2E-272-tab-user-log-sub-tab-borrow-setup-column | Tab User Log sub-tab Borrow: Setup Column (Ceklis dan Drag Reorder) | FE+BE. | 31 | TC-FA-SU-826, TC-FA-SU-827 |
| TC-FA-SU-E2E-273-tab-user-log-sub-tab-borrow-setup-column-pagination-dan-tooltip-icon | Tab User Log sub-tab Borrow: Setup Column, Pagination, dan Tooltip Icon | FE+BE. | 45 | TC-FA-SU-829, TC-FA-SU-830, TC-FA-SU-835 |
| TC-FA-SU-E2E-274-tab-user-log-sub-tab-borrow-state-per-sub-tab-dan-download | Tab User Log sub-tab Borrow: State per Sub-tab dan Download | FE+BE. | 55 | TC-FA-SU-831, TC-FA-SU-832, TC-FA-SU-837 |
| TC-FA-SU-E2E-275-tab-transaction-admin-log-pin-dan-unpin-setup-column | Tab Transaction Admin Log: Pin dan Unpin Setup Column | FE+BE. | 42 | TC-FA-SU-787 |
| TC-FA-SU-E2E-276-tab-user-log-sub-tab-borrow-pin-dan-unpin-setup-column | Tab User Log sub-tab Borrow: Pin dan Unpin Setup Column | FE+BE. | 39 | TC-FA-SU-828 |
| TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search | Tab User Log sub-tab Assignment: Screening dan Search | FE+BE. | 37 | TC-FA-SU-838, TC-FA-SU-839, TC-FA-SU-840, TC-FA-SU-841 |
| TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort | Tab User Log sub-tab Assignment: Search dan Sort | FE+BE. | 47 | TC-FA-SU-842, TC-FA-SU-843, TC-FA-SU-844, TC-FA-SU-845 |
| TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | Tab User Log sub-tab Assignment: Sort dan Filter dan Kontrol Filter | FE+BE. | 39 | TC-FA-SU-846, TC-FA-SU-847, TC-FA-SU-848, TC-FA-SU-849, TC-FA-SU-850 |
| TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter | Tab User Log sub-tab Assignment: Filter dan Kontrol Filter | FE+BE. | 52 | TC-FA-SU-851, TC-FA-SU-852, TC-FA-SU-853, TC-FA-SU-854 |
| TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column | Tab User Log sub-tab Assignment: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 54 | TC-FA-SU-855, TC-FA-SU-856, TC-FA-SU-857, TC-FA-SU-858 |
| TC-FA-SU-E2E-282-tab-user-log-sub-tab-assignment-setup-column | Tab User Log sub-tab Assignment: Setup Column | FE+BE. | 31 | TC-FA-SU-859, TC-FA-SU-860 |
| TC-FA-SU-E2E-283-tab-user-log-sub-tab-assignment-setup-column-pagination-dan-tooltip-icon | Tab User Log sub-tab Assignment: Setup Column, Pagination, dan Tooltip Icon | FE+BE. | 44 | TC-FA-SU-862, TC-FA-SU-863, TC-FA-SU-868 |
| TC-FA-SU-E2E-284-tab-user-log-sub-tab-assignment-state-per-sub-tab-dan-download | Tab User Log sub-tab Assignment: State per Sub-tab dan Download | FE+BE. | 61 | TC-FA-SU-864, TC-FA-SU-865, TC-FA-SU-870 |
| TC-FA-SU-E2E-285-tab-user-log-sub-tab-session-screening-dan-search | Tab User Log sub-tab Session: Screening dan Search | FE+BE. | 41 | TC-FA-SU-871, TC-FA-SU-872, TC-FA-SU-1045 |
| TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort | Tab User Log sub-tab Session: Search dan Sort | FE+BE. | 47 | TC-FA-SU-873, TC-FA-SU-874, TC-FA-SU-875, TC-FA-SU-876 |
| TC-FA-SU-E2E-287-tab-user-log-sub-tab-session-sort-dan-filter-dan-kontrol-filter | Tab User Log sub-tab Session: Sort dan Filter dan Kontrol Filter | FE+BE. | 40 | TC-FA-SU-877, TC-FA-SU-878 |
| TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column | Tab User Log sub-tab Session: Filter dan Kontrol Filter dan Setup Column | FE+BE. | 36 | TC-FA-SU-879, TC-FA-SU-880, TC-FA-SU-881, TC-FA-SU-882 |
| TC-FA-SU-E2E-289-tab-user-log-sub-tab-session-setup-column | Tab User Log sub-tab Session: Setup Column | FE+BE. | 31 | TC-FA-SU-883, TC-FA-SU-884 |
| TC-FA-SU-E2E-290-tab-user-log-sub-tab-session-setup-column-dan-pagination | Tab User Log sub-tab Session: Setup Column dan Pagination | FE+BE. | 36 | TC-FA-SU-886, TC-FA-SU-887 |
| TC-FA-SU-E2E-291-tab-user-log-sub-tab-session-tooltip-icon-state-per-sub-tab-dan-download | Tab User Log sub-tab Session: Tooltip Icon, State per Sub-tab, dan Download | FE+BE. | 42 | TC-FA-SU-888, TC-FA-SU-892, TC-FA-SU-894 |
| TC-FA-SU-E2E-292-tab-user-log-sub-tab-session-download | Tab User Log sub-tab Session: Download | FE+BE. | 24 | TC-FA-SU-889 |
| TC-FA-SU-E2E-293-tab-user-log-sub-tab-assignment-pin-dan-unpin-setup-column | Tab User Log sub-tab Assignment: Pin dan Unpin Setup Column | FE+BE. | 13 | TC-FA-SU-861 |
| TC-FA-SU-E2E-294-tab-user-log-sub-tab-session-pin-dan-unpin-setup-column | Tab User Log sub-tab Session: Pin dan Unpin Setup Column | FE+BE. | 13 | TC-FA-SU-885 |
| TC-FA-SU-E2E-295-log-activate-deactivate-dan-resend-activation-email-pada-tiga-surface-log | Log Activate, Deactivate, dan Resend Activation Email pada Tiga Surface Log | FE+BE. | 58 | TC-FA-SU-909, TC-FA-SU-910, TC-FA-SU-911 |
| TC-FA-SU-E2E-296-log-resend-confirmation-email-dan-edit-home-group-pada-tiga-surface-log | Log Resend Confirmation Email dan Edit Home Group pada Tiga Surface Log | FE+BE. | 57 | TC-FA-SU-912, TC-FA-SU-913, TC-FA-SU-914 |
| TC-FA-SU-E2E-297-log-assign-remove-dan-edit-global-role-pada-tiga-surface-log | Log Assign, Remove, dan Edit Global Role pada Tiga Surface Log | FE+BE. | 57 | TC-FA-SU-915, TC-FA-SU-916, TC-FA-SU-917 |
| TC-FA-SU-E2E-298-log-assign-edit-dan-remove-group-role-pada-tiga-surface-log | Log Assign, Edit, dan Remove Group Role pada Tiga Surface Log | FE+BE. | 57 | TC-FA-SU-918, TC-FA-SU-919, TC-FA-SU-920 |
| TC-FA-SU-E2E-299-log-assign-remove-dan-penggantian-transaction-role-pada-tiga-surface-log | Log Assign, Remove, dan Penggantian Transaction Role pada Tiga Surface Log | FE+BE. | 77 | TC-FA-SU-921, TC-FA-SU-922, TC-FA-SU-923 |
| TC-FA-SU-E2E-300-log-auto-revert-total-control-read-only-dan-group-manager-pada-tiga-surface-log | Log Auto-Revert Total Control, Read Only, dan Group Manager pada Tiga Surface Log | FE+BE. | 63 | TC-FA-SU-924, TC-FA-SU-925, TC-FA-SU-926 |
| TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group | Entri Lintas Modul, Cascade Tier, dan Log Delete Group | FE+BE. | 62 | TC-FA-SU-927, TC-FA-SU-928, TC-FA-SU-929, TC-FA-SU-930 |
| TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk | Creator Auto-Assign, Home Group Di-null, Zero-delta, dan Log per Pengguna pada Aksi Bulk | FE+BE. | 62 | TC-FA-SU-931, TC-FA-SU-932, TC-FA-SU-933, TC-FA-SU-934 |
| TC-FA-SU-E2E-303-notifikasi-auto-revert-struktur-kolom-tiga-surface-log-dan-object-action-pendek | Notifikasi Auto-Revert, Struktur Kolom Tiga Surface Log, dan Object Action Pendek | FE+BE. | 45 | TC-FA-SU-935, TC-FA-SU-936, TC-FA-SU-937 |
| TC-FA-SU-E2E-304-log-tanpa-peristiwa-pembuatan-atau-penghapusan-dan-snapshot-immutable | Log Tanpa Peristiwa Pembuatan atau Penghapusan dan Snapshot Immutable | FE+BE. | 26 | TC-FA-SU-938, TC-FA-SU-939 |
| TC-FA-SU-E2E-305-app-access-global-settings-pemberian-pencabutan-dan-pemberian-ulang | App Access Global Settings: Pemberian, Pencabutan, dan Pemberian Ulang | FE+BE. | 50 | TC-FA-SU-941, TC-FA-SU-942, TC-FA-SU-943 |
| TC-FA-SU-E2E-306-penghapusan-identitas-permanen-dan-perubahan-identitas-di-global-settings | Penghapusan Identitas Permanen dan Perubahan Identitas di Global Settings | FE+BE. | 23 | TC-FA-SU-944, TC-FA-SU-945 |
| TC-FA-SU-E2E-307-email-pending-dan-pengguna-nonaktif-di-global-settings | Email Pending dan Pengguna Nonaktif di Global Settings | FE+BE. | 27 | TC-FA-SU-946, TC-FA-SU-947, TC-FA-SU-948 |
| TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | Custom Field Pengguna: Accordion, Rename, Hapus, Tipe Date dan Phone, serta Filter Panel | FE+BE. | 48 | TC-FA-SU-949, TC-FA-SU-1036, TC-FA-SU-1037, TC-FA-SU-1038, TC-FA-SU-1039, TC-FA-SU-1040 |
| TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission | Format Tanggal General Settings, Pohon Grup Settings Groups, dan Pembaruan Peran dari Role & Permission | FE+BE. | 44 | TC-FA-SU-951, TC-FA-SU-960, TC-FA-SU-961, TC-FA-SU-962 |
| TC-FA-SU-E2E-310-fan-out-responsibilities-pending-approvals-pending-tasks-dan-non-login-user | Fan-out Responsibilities, Pending Approvals, Pending Tasks, dan Non-Login User | FE+BE. | 41 | TC-FA-SU-952, TC-FA-SU-953, TC-FA-SU-954 |
| TC-FA-SU-E2E-311-fan-out-transaction-admin-log-dan-satu-transaksi-menghasilkan-dua-baris-user-log | Fan-out Transaction Admin Log dan Satu Transaksi Menghasilkan Dua Baris User Log | FE+BE. | 22 | TC-FA-SU-955, TC-FA-SU-956 |
| TC-FA-SU-E2E-312-picker-peminjam-dan-penugasan-tetap-setelah-nonaktif | Picker PIC dan Peminjam serta Penugasan Tetap Setelah Nonaktif | FE+BE. | 35 | TC-FA-SU-957, TC-FA-SU-958 |
| TC-FA-SU-E2E-313-log-disaring-scope-aktor-ber-scope-grup-pada-modal-combined-changelog | Log Disaring Scope Aktor Ber-scope Grup pada Modal Combined Changelog | FE+BE. | 25 | TC-FA-SU-940 |
| TC-FA-SU-E2E-314-guard-state-basi-dan-direct-url-detail-di-luar-scope | Guard State Basi dan Direct URL Detail di Luar Scope | FE+BE. | 26 | TC-FA-SU-1005, TC-FA-SU-1006, TC-FA-SU-1007 |
| TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan | Resilience Jaringan Putus atau Timeout: Toggle Active, Bulk Deactivate, Switch dan Checkbox Global Role | FE+BE. | 40 | TC-FA-SU-1009, TC-FA-SU-1010, TC-FA-SU-1011, TC-FA-SU-1012 |
| TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend | Resilience Jaringan Putus atau Timeout: Save Group Role, Submit Transaction Role, Resend, dan Select Edit Home Group | FE+BE. | 45 | TC-FA-SU-1013, TC-FA-SU-1014, TC-FA-SU-1015, TC-FA-SU-1016 |
| TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal | Klik Ganda Sakelar, Double-submit, Klik Ganda Resend, dan Toast Tunggal | FE+BE. | 43 | TC-FA-SU-1017, TC-FA-SU-1018, TC-FA-SU-1019, TC-FA-SU-1024 |
| TC-FA-SU-E2E-318-refresh-form-kotor-state-tab-dan-sub-tab-default-dan-ordering-serta-esc-dialog | Refresh Form Kotor dan Esc Dialog Downgrade | FE+BE. | 29 | TC-FA-SU-1021, TC-FA-SU-1032 |
| TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi | Must NOT: Bulk Tanpa Eligible, Save Sebagian, Edit Global Role Beruntun, dan Deaktivasi Tanpa Hard-block | FE+BE. | 39 | TC-FA-SU-1027, TC-FA-SU-1028, TC-FA-SU-1029, TC-FA-SU-1030 |
| TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup | Konkurensi: Akses Dicabut Saat Popup Terbuka, Item Bulk Berubah, Dua Admin, dan Grup Dihapus Saat Tree Terbuka | FE+BE. | 48 | TC-FA-SU-1020, TC-FA-SU-1022, TC-FA-SU-1023, TC-FA-SU-1031 |
| TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | Defense-in-depth Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope | FE+BE. | 19 | TC-FA-SU-125, TC-FA-SU-126, TC-FA-SU-127, TC-FA-SU-128, TC-FA-SU-129 |
| TC-FA-SU-E2E-322-defense-in-depth-tier-deactivate-dan-activate-target-total-control-dan-read-only | Defense-in-depth Tier: Deactivate dan Activate Target Total Control dan Read Only (Tunggal dan Bulk) serta Assign Group Role | FE+BE. | 62 | TC-FA-SU-1064, TC-FA-SU-1066, TC-FA-SU-1067 |
| TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan | Defense-in-depth Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci | FE+BE. | 37 | TC-FA-SU-222, TC-FA-SU-223, TC-FA-SU-272, TC-FA-SU-1062 |
| TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | Defense-in-depth Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF | FE+BE. | 45 | TC-FA-SU-146, TC-FA-SU-148, TC-FA-SU-171, TC-FA-SU-183, TC-FA-SU-188, TC-FA-SU-1004 |
| TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role | Defense-in-depth Aktor Read Only: Activate, Deactivate, dan Global Role | FE+BE. | 12 | TC-FA-SU-964, TC-FA-SU-965, TC-FA-SU-966, TC-FA-SU-967 |
| TC-FA-SU-E2E-326-defense-in-depth-aktor-read-only-group-role-dan-transaction-role | Defense-in-depth Aktor Read Only: Group Role dan Transaction Role | FE+BE. | 9 | TC-FA-SU-968, TC-FA-SU-969, TC-FA-SU-970 |
| TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | Defense-in-depth Aktor Manage user & role Tanpa Update | FE+BE. | 15 | TC-FA-SU-971, TC-FA-SU-972, TC-FA-SU-973, TC-FA-SU-974, TC-FA-SU-975 |
| TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role | Defense-in-depth Entitas Suspended atau Expired: Activate, Global Role, dan Group Role | FE+BE. | 27 | TC-FA-SU-976, TC-FA-SU-977, TC-FA-SU-978, TC-FA-SU-979 |
| TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan | Defense-in-depth Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate | FE+BE. | 25 | TC-FA-SU-130, TC-FA-SU-304, TC-FA-SU-980, TC-FA-SU-981 |
| TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | Defense-in-depth Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group | FE+BE. | 24 | TC-FA-SU-305, TC-FA-SU-982, TC-FA-SU-983, TC-FA-SU-984, TC-FA-SU-985, TC-FA-SU-986 |
| TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role | Defense-in-depth Akun Sendiri sebagai Target: Deactivate, Global Role, dan Group Role | FE+BE. | 12 | TC-FA-SU-987, TC-FA-SU-988, TC-FA-SU-989, TC-FA-SU-990 |
| TC-FA-SU-E2E-332-defense-in-depth-akun-sendiri-sebagai-target-transaction-role-dan-edit-home-group | Defense-in-depth Akun Sendiri sebagai Target: Transaction Role dan Edit Home Group | FE+BE. | 6 | TC-FA-SU-991, TC-FA-SU-992 |
| TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role | Defense-in-depth Default User sebagai Target: Deactivate, Global Role, dan Group Role | FE+BE. | 12 | TC-FA-SU-993, TC-FA-SU-994, TC-FA-SU-995, TC-FA-SU-996 |
| TC-FA-SU-E2E-334-defense-in-depth-default-user-sebagai-target-transaction-role-dan-edit-home-group | Defense-in-depth Default User sebagai Target: Transaction Role dan Edit Home Group | FE+BE. | 6 | TC-FA-SU-997, TC-FA-SU-998 |
| TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | Defense-in-depth Baca Di Luar Scope, Bulk Langsung, Flag Aktif, 422 Duplikat, dan Turun Tangga Tanpa Konfirmasi | FE+BE. | 38 | TC-FA-SU-999, TC-FA-SU-1000, TC-FA-SU-1001, TC-FA-SU-1002, TC-FA-SU-1003 |
| TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | Absence Log Request Ditolak: Status Aktif: Akun Sendiri, Default User, Target Tier, Nonaktif Global Settings, dan Di Luar Scope | FE+BE. | 24 | TC-FA-SU-125, TC-FA-SU-126, TC-FA-SU-127, TC-FA-SU-128, TC-FA-SU-129 |
| TC-FA-SU-E2E-337-absence-log-request-ditolak-tier-deactivate-dan-activate-target-total-control-dan | Absence Log Request Ditolak: Tier: Deactivate dan Activate Target Total Control dan Read Only, serta Assign Group Role | FE+BE. | 13 | TC-FA-SU-1067 |
| TC-FA-SU-E2E-338-absence-log-request-ditolak-transaction-role-dan-group-role-target-tier-di-luar-scope | Absence Log Request Ditolak: Transaction Role dan Group Role: Target Tier, Di Luar Scope, dan Perubahan Baris Terkunci | FE+BE. | 21 | TC-FA-SU-222, TC-FA-SU-223, TC-FA-SU-272 |
| TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | Absence Log Request Ditolak: Resend dan Global Role: Cooldown, Status Tidak Valid, dan Switch OFF | FE+BE. | 38 | TC-FA-SU-146, TC-FA-SU-148, TC-FA-SU-171, TC-FA-SU-183, TC-FA-SU-1004 |
| TC-FA-SU-E2E-340-absence-log-request-ditolak-aktor-read-only-activate-deactivate-dan-global-role | Absence Log Request Ditolak: Aktor Read Only: Activate, Deactivate, dan Global Role | FE+BE. | 16 | TC-FA-SU-964, TC-FA-SU-965, TC-FA-SU-966, TC-FA-SU-967 |
| TC-FA-SU-E2E-341-absence-log-request-ditolak-aktor-read-only-group-role-dan-transaction-role | Absence Log Request Ditolak: Aktor Read Only: Group Role dan Transaction Role | FE+BE. | 12 | TC-FA-SU-968, TC-FA-SU-969, TC-FA-SU-970 |
| TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | Absence Log Request Ditolak: Aktor Manage user & role Tanpa Update | FE+BE. | 20 | TC-FA-SU-971, TC-FA-SU-972, TC-FA-SU-973, TC-FA-SU-974, TC-FA-SU-975 |
| TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan | Absence Log Request Ditolak: Entitas Suspended atau Expired: Activate, Global Role, dan Group Role | FE+BE. | 35 | TC-FA-SU-976, TC-FA-SU-977, TC-FA-SU-978, TC-FA-SU-979 |
| TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home | Absence Log Request Ditolak: Entitas Suspended atau Expired: Transaction Role, Edit Home Group, dan Activate | FE+BE. | 31 | TC-FA-SU-130, TC-FA-SU-304, TC-FA-SU-980, TC-FA-SU-981 |
| TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | Absence Log Request Ditolak: Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group (Bagian 1) | FE+BE. | 20 | TC-FA-SU-982, TC-FA-SU-983, TC-FA-SU-984, TC-FA-SU-985, TC-FA-SU-986 |
| TC-FA-SU-E2E-346-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | Absence Log Request Ditolak: Aktor Ber-scope Grup: Global Role Target, Di Luar Scope, dan Edit Home Group (Bagian 2) | FE+BE. | 10 | TC-FA-SU-305 |
| TC-FA-SU-E2E-347-absence-log-request-ditolak-akun-sendiri-sebagai-target-deactivate-global-role-dan | Absence Log Request Ditolak: Akun Sendiri sebagai Target: Deactivate, Global Role, dan Group Role | FE+BE. | 16 | TC-FA-SU-987, TC-FA-SU-988, TC-FA-SU-989, TC-FA-SU-990 |
| TC-FA-SU-E2E-348-absence-log-request-ditolak-akun-sendiri-sebagai-target-transaction-role-dan-edit | Absence Log Request Ditolak: Akun Sendiri sebagai Target: Transaction Role dan Edit Home Group | FE+BE. | 8 | TC-FA-SU-991, TC-FA-SU-992 |
| TC-FA-SU-E2E-349-absence-log-request-ditolak-default-user-sebagai-target-deactivate-global-role-dan | Absence Log Request Ditolak: Default User sebagai Target: Deactivate, Global Role, dan Group Role | FE+BE. | 16 | TC-FA-SU-993, TC-FA-SU-994, TC-FA-SU-995, TC-FA-SU-996 |
| TC-FA-SU-E2E-350-absence-log-request-ditolak-default-user-sebagai-target-transaction-role-dan-edit | Absence Log Request Ditolak: Default User sebagai Target: Transaction Role dan Edit Home Group | FE+BE. | 8 | TC-FA-SU-997, TC-FA-SU-998 |
| TC-FA-SU-E2E-351-state-tab-dan-sub-tab-detail-user-serta-default-dan-ordering | State Tab dan Sub-tab Detail User serta Default dan Ordering | FE+BE. | 42 | TC-FA-SU-1025, TC-FA-SU-1026 |
| TC-FA-SU-E2E-352-defense-in-depth-assign-transaction-role-target-total-control-dan-read-only | Defense-in-depth Transaction Role: Assign pada Target Total Control dan Read Only bagi Aktor Group dan Group Manager | FE+BE. | 23 | TC-FA-SU-1061 |
| TC-FA-SU-E2E-353-lockdown-tenant-tooltip-prioritas-user-list-suspended-transaction-role-suspended-dan | Tenant Suspended: User List dan Detail Read-only, Unsuspend, dan Tanpa Entri Log Perubahan Status | FE+BE. | 47 | TC-FA-SU-77, TC-FA-SU-80, TC-FA-SU-959 |
| TC-FA-SU-E2E-354-tenant-berubah-unsuspend-halaman-terbuka-saat-status-berubah-state-reflected-resend | Tenant Berubah: Halaman Terbuka Saat Status Client Berubah dan Prioritas Tooltip Disabled | FE+BE. | 45 | TC-FA-SU-81, TC-FA-SU-75 |
| TC-FA-SU-E2E-355-selection-limit-tooltip-disabled-checkbox-limit-1-auto-cap-dan-perubahan-limit-live | Selection Limit: Tooltip Disabled Lain dan Checkbox Limit+1 dengan Auto-cap | FE+BE. | 44 | TC-FA-SU-76, TC-FA-SU-123 |
| TC-FA-SU-E2E-356-download-user-list-lebih-dari-5-000-baris-loading-screen-unduhan-langsung-dan-tanpa | Volume Data: Download User List Lebih dari 5.000 Baris dan Perubahan Selection Limit Live | FE+BE. | 24 | TC-FA-SU-368, TC-FA-SU-950 |
| TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain | Multi-konteks: Sesi Target Terputus Saat Deactivate, Login Pengguna Nonaktif, Sesi Produk Lain Tetap Aktif, dan Sesi Aktor Berakhir | FE+BE. | 47 | TC-FA-SU-97, TC-FA-SU-98, TC-FA-SU-963, TC-FA-SU-1008 |
| TC-FA-SU-E2E-358-tenant-suspended-dan-expired-kontrol-tulis-sub-tab-role-dan-aksi-tulis-paksa | Tenant Suspended dan Expired: Kontrol Tulis Sub-tab Role dan Aksi Tulis Paksa | FE+BE. | 46 | TC-FA-SU-78, TC-FA-SU-79 |
| TC-FA-SU-E2E-359-tenant-suspended-visibilitas-resend-per-aktor-dan-edit-home-group-hidden | Tenant Suspended: Visibilitas Resend per Aktor dan Edit Home Group Hidden | FE+BE. | 48 | TC-FA-SU-152, TC-FA-SU-283 |
| TC-FA-SU-E2E-360-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-1 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 1) | FE+BE. | 28 | TC-FA-SU-406, TC-FA-SU-440 |
| TC-FA-SU-E2E-361-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-2 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 2) | FE+BE. | 42 | TC-FA-SU-469, TC-FA-SU-500, TC-FA-SU-536 |
| TC-FA-SU-E2E-362-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-3 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 3) | FE+BE. | 28 | TC-FA-SU-574, TC-FA-SU-606 |
| TC-FA-SU-E2E-363-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-4 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 4) | FE+BE. | 34 | TC-FA-SU-670, TC-FA-SU-702 |
| TC-FA-SU-E2E-364-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-5 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 5) | FE+BE. | 28 | TC-FA-SU-764, TC-FA-SU-795 |
| TC-FA-SU-E2E-365-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-6 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 6) | FE+BE. | 28 | TC-FA-SU-869, TC-FA-SU-893 |
| TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1 | Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 1) | FE+BE. | 35 | TC-FA-SU-363, TC-FA-SU-438, TC-FA-SU-467, TC-FA-SU-498 |
| TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2 | Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 2) | FE+BE. | 38 | TC-FA-SU-572, TC-FA-SU-604, TC-FA-SU-668, TC-FA-SU-700 |
| TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3 | Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 3) | FE+BE. | 37 | TC-FA-SU-732, TC-FA-SU-762, TC-FA-SU-793, TC-FA-SU-834 |
| TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4 | Resilience Download Gagal: Toast Error Tanpa Ekstensi per Surface Tabel (Bagian 4) | FE+BE. | 37 | TC-FA-SU-534, TC-FA-SU-636, TC-FA-SU-867, TC-FA-SU-891 |
| TC-FA-SU-E2E-370-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-1 | Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 1) | FE+BE. | 33 | TC-FA-SU-362, TC-FA-SU-437, TC-FA-SU-466 |
| TC-FA-SU-E2E-371-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-2 | Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 2) | FE+BE. | 33 | TC-FA-SU-497, TC-FA-SU-533, TC-FA-SU-571 |
| TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3 | Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 3) | FE+BE. | 35 | TC-FA-SU-603, TC-FA-SU-635, TC-FA-SU-667, TC-FA-SU-699 |
| TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4 | Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 4) | FE+BE. | 32 | TC-FA-SU-731, TC-FA-SU-761, TC-FA-SU-792, TC-FA-SU-833 |
| TC-FA-SU-E2E-374-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-5 | Isi Berkas Download: Transformasi Data per Tipe Kolom per Surface Tabel (Bagian 5) | FE+BE. | 15 | TC-FA-SU-866, TC-FA-SU-890 |
| TC-FA-SU-E2E-375-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-7 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 7) | FE+BE. | 30 | TC-FA-SU-365, TC-FA-SU-734 |
| TC-FA-SU-E2E-376-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-8 | Resilience Baca: Empty State, Loading, dan Error Load Surface Tabel (Bagian 8) | FE+BE. | 31 | TC-FA-SU-638, TC-FA-SU-836 |
| TC-FA-SU-E2E-377-kolom-dan-field-tag-tidak-tersedia-pada-plan-starter-dan-tersedia-pada-plan-professional | Kolom dan Field TAG: Tidak Tersedia pada Plan Starter dan Tersedia pada Plan Professional | FE+BE. | 17 | TC-FA-SU-367 |
| TC-FA-SU-E2E-378-auto-revert-tier-total-control-dari-popup-assign-group-role-edit-centang-crud | Auto-Revert Tier Total Control dari Popup Assign Group Role: Edit Centang CRUD | FE+BE. | 36 | TC-FA-SU-1076 |
| TC-FA-SU-E2E-379-auto-revert-tier-dari-popup-assign-group-role-tambah-grup-yang-menyimpangkan-pola | Auto-Revert Tier dari Popup Assign Group Role: Tambah Grup yang Menyimpangkan Pola | FE+BE. | 39 | TC-FA-SU-1078 |
| TC-FA-SU-E2E-380-auto-revert-tier-total-control-dari-modal-assign-transaction-role-cancel-remove-baris-pola-dan-turun-tangga | Auto-Revert Tier Total Control dari Modal Assign Transaction Role: Cancel Remove Baris Pola dan Turun Tangga | FE+BE. | 43 | TC-FA-SU-1073, TC-FA-SU-1070 |
| TC-FA-SU-E2E-381-screening-banner-tier-dan-baris-pola-sub-tab-transaction-role-dan-group-role-total-control-dan-read-only | Screening Banner Tier dan Baris Pola Sub-tab Transaction Role dan Group Role: Total Control dan Read Only | FE+BE. | 33 | TC-FA-SU-1072, TC-FA-SU-1080 |
| TC-FA-SU-E2E-382-tab-transaction-admin-log-user-total-control-tanpa-transaksi-empty-state | Tab Transaction Admin Log User Total Control Tanpa Transaksi: Empty State | FE+BE. | 14 | TC-FA-SU-1075 |
| TC-FA-SU-E2E-383-auto-revert-tier-read-only-dari-popup-assign-group-role-hapus-grup | Auto-Revert Tier Read Only dari Popup Assign Group Role: Hapus Grup | FE+BE. | 32 | TC-FA-SU-1077 |
| TC-FA-SU-E2E-384-cancel-dialog-auto-revert-dari-popup-assign-group-role-popup-kembali-utuh | Cancel Dialog Auto-Revert dari Popup Assign Group Role: Popup Kembali dengan Isi Utuh | FE+BE. | 50 | TC-FA-SU-1079 |
| TC-FA-SU-E2E-385-auto-revert-tier-read-only-dari-modal-assign-transaction-role-naik-tangga | Auto-Revert Tier Read Only dari Modal Assign Transaction Role: Naik Tangga | FE+BE. | 22 | TC-FA-SU-1071 |
| TC-FA-SU-E2E-386-banner-group-manager-per-sub-tab-role-tidak-tampil-di-transaction-role | Banner Group Manager per Sub-tab Role: Tampil di Global Role, Group Role, dan Transaction Role | FE+BE. | 18 | TC-FA-SU-1074 |
| TC-FA-SU-E2E-387-screening-banner-group-manager-dan-baris-pola-sub-tab-group-role-dan-transaction-role-target-group-manager | Screening Banner Group Manager dan Baris Pola Sub-tab Group Role dan Transaction Role: Target Group Manager | FE+BE. | 30 | TC-FA-SU-1081, TC-FA-SU-1088 |
| TC-FA-SU-E2E-388-kunci-baris-pola-group-role-target-group-manager-bagi-aktor-manage-user-dan-role-group-dan-baris-non-pola | Kunci Baris Pola Group Role Target Group Manager bagi Aktor Manage User & Role Group dan Baris Manage User & Role Non-pola | FE+BE. | 33 | TC-FA-SU-1085 |
| TC-FA-SU-E2E-389-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-user-dan-role-group | Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage User & Role Group | FE+BE. | 27 | TC-FA-SU-1089 |
| TC-FA-SU-E2E-390-kolom-role-popup-role-count-filter-dan-search-user-group-manager-baris-pola-tanpa-badge | Kolom Role, Popup Role Count, Filter, dan Search User Group Manager: Baris Pola Tanpa Badge | FE+BE. | 29 | TC-FA-SU-1096 |
| TC-FA-SU-E2E-391-remove-baris-grup-pola-group-manager-dari-popup-dan-perubahan-non-pola-tanpa-auto-revert | Remove Baris Grup Pola Group Manager dari Popup (Dialog D-05c) dan Perubahan Non-Pola Tanpa Auto-Revert | FE+BE. | 57 | TC-FA-SU-1083, TC-FA-SU-1084 |
| TC-FA-SU-E2E-392-edit-baris-pola-group-manager-pada-node-turunan-dialog-auto-revert | Edit Baris Pola Group Manager pada Node Turunan: Dialog Auto-Revert D-05c dan Baris Pola Dipertahankan sebagai Baris Biasa | FE+BE. | 34 | TC-FA-SU-1082 |
| TC-FA-SU-E2E-393-group-manager-bersarang-dialog-d-05c-satu-penugasan-dan-dialog-d-05d-dua-penugasan | Group Manager Bersarang: Dialog D-05c untuk Satu Penugasan dan Dialog D-05d untuk Dua Penugasan | FE+BE. | 48 | TC-FA-SU-1086, TC-FA-SU-1087 |
| TC-FA-SU-E2E-394-remove-baris-pola-transaction-role-target-group-manager-dialog-auto-revert-cancel-lalu-konfirmasi | Remove Baris Pola Transaction Role Target Group Manager: Dialog Auto-Revert, Cancel lalu Konfirmasi | FE+BE. | 35 | TC-FA-SU-1090 |
| TC-FA-SU-E2E-395-turun-tangga-modal-assign-transaction-role-target-group-manager-dialog-auto-revert-menggantikan-dialog-turun-tangga | Turun Tangga Modal Assign Transaction Role Target Group Manager: Dialog Auto-Revert Menggantikan Dialog Turun Tangga | FE+BE. | 30 | TC-FA-SU-1092 |
| TC-FA-SU-E2E-396-popup-assign-group-baris-pola-transaction-role-target-group-manager-tambah-grup-luar-subtree-dan-cabut-grup-dalam-subtree | Popup Assign Group Baris Pola Transaction Role Target Group Manager: Tambah Grup di Luar Subtree dan Cabut Grup dalam Subtree | FE+BE. | 32 | TC-FA-SU-1094 |
| TC-FA-SU-E2E-397-edit-home-group-yang-mencabut-baris-pola-group-manager-dialog-gabungan-dan-log-per-baris | Edit Home Group yang Mencabut Baris Pola Group Manager: Dialog Gabungan, Pencabutan Baris Pola, dan Log per Baris | FE+BE. | 40 | TC-FA-SU-1095 |
| TC-FA-SU-E2E-398-assign-group-manager-materialisasi-baris-pola-tampil-via-group-manager-hanya-di-modal-changelog-user | Assign Group Manager: Materialisasi Baris Pola Tampil sebagai Assign (via Group Manager) Hanya di Modal Changelog User | FE+BE. | 31 | TC-FA-SU-1097 |
| TC-FA-SU-E2E-399-defense-in-depth-baris-pola-group-manager-ditolak-403-baris-manage-user-role-diterima-dan-konfirmasi-auto-revert-409 | Defense-in-depth Baris Pola Group Manager: Ditolak 403, Baris Manage user & role Diterima, dan Konfirmasi Auto-Revert 409 | FE+BE. | 24 | TC-FA-SU-1099 |
| TC-FA-SU-E2E-400-absence-log-request-ditolak-baris-pola-group-manager-oleh-aktor-non-default-user-total-control | Absence Log Request Ditolak: Baris Pola Group Manager oleh Aktor Non-Default User dan Non-Total Control | FE+BE. | 11 | TC-FA-SU-1099 |
| TC-FA-SU-E2E-401-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-global-user-dan-role | Kunci Baris Pola Transaction Role Target Group Manager bagi Aktor Manage Global User & Role | FE+BE. | 24 | TC-FA-SU-1089 |
| TC-FA-SU-E2E-403-pelepasan-group-manager-remove-via-group-manager-hanya-di-modal-changelog-user | Pelepasan Group Manager: Tanpa Entri Remove (via Group Manager) per Baris Pola di Surface Mana Pun dan Tanpa Notifikasi Tambahan | FE+BE. | 43 | TC-FA-SU-1098 |
| TC-FA-SU-E2E-405-bulk-remove-transaction-role-target-group-manager-baris-non-pola-dan-baris-pola | Bulk Remove Transaction Role Target Group Manager: Baris Non-Pola dan Baris Pola | FE+BE. | 38 | TC-FA-SU-1091 |
| TC-FA-SU-E2E-406-save-campuran-modal-assign-transaction-role-target-group-manager-dialog-turun-tangga-lalu-auto-revert | Save Campuran Modal Assign Transaction Role Target Group Manager: Dialog Turun Tangga lalu Auto-Revert | FE+BE. | 39 | TC-FA-SU-1093 |
| TC-FA-SU-E2E-407-pasca-auto-revert-group-manager-lewat-group-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-status-gm-tidak-kembali | Pasca Auto-Revert Group Manager lewat Sub-tab Group Role: Baris Pola Dipertahankan, Label Role Tetap, Kunci S-16 Hilang, dan Status GM Tidak Kembali | FE+BE. | 36 | TC-FA-SU-1100 |
| TC-FA-SU-E2E-408-pasca-auto-revert-group-manager-lewat-transaction-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-remove-d-07a-biasa | Pasca Auto-Revert Group Manager lewat Sub-tab Transaction Role: Baris Pola Dipertahankan, Kunci S-16 Hilang, dan Remove Memakai Dialog D-07a Biasa | FE+BE. | 32 | TC-FA-SU-1101 |
| TC-FA-SU-E2E-409-preview-scope-di-modal-assign-transaction-role | Preview Scope di Modal Assign Transaction Role: Tampil Setelah Group Dipilih, Memuat Node Terpilih beserta Descendant, Read-only, dan Bukan Baris Tabel | FE+BE. | 24 | TC-FA-SU-1102 |
| TC-FA-SU-E2E-410-preview-scope-di-popup-assign-group-transaction-role | Preview Scope di Popup Assign Group Transaction Role: Hanya untuk Grup yang Baru Dicentang, Read-only, dan Cancel Membuangnya tanpa Dialog | FE+BE. | 29 | TC-FA-SU-1103 |
| TC-FA-SU-E2E-411-pohon-group-tanpa-node-disabled-karena-ancestor-atau-descendant-pada-modal-dan-popup | Pohon Group Tanpa Node Disabled karena Ancestor atau Descendant Pemegang Role pada Modal Assign dan Popup Assign Group | FE+BE. | 35 | TC-FA-SU-1104 |
| TC-FA-SU-E2E-412-baris-literal-sub-tab-transaction-role-tanpa-proyeksi-descendant | Baris Literal Sub-tab Transaction Role per Node Penugasan: Descendant yang Hanya Tercakup Tidak Diproyeksikan sebagai Baris atau Badge | FE+BE. | 16 | TC-FA-SU-1112 |
| TC-FA-SU-E2E-415-assign-overlap-di-node-turunan-role-lebih-rendah-dan-lebih-tinggi-tanpa-d-06-ancestor-tidak-berubah | Assign Overlap di Node Turunan: Role Lebih Rendah dan Lebih Tinggi Tersimpan Tanpa D-06 dan Baris Ancestor Tidak Berubah | FE+BE. | 39 | TC-FA-SU-1105, TC-FA-SU-1106 |
| TC-FA-SU-E2E-416-assign-overlap-ancestor-setelah-turunan-dan-assign-group-menambah-descendant | Assign Overlap: Penugasan Ancestor Setelah Turunan Tanpa D-06, dan Assign Group Menambah Descendant pada Baris yang Ancestor-nya Sudah Tersimpan | FE+BE. | 35 | TC-FA-SU-1107, TC-FA-SU-1110 |
| TC-FA-SU-E2E-417-dialog-d-06-hanya-node-yang-sama-node-lain-naik-tangga-dan-cancel-membatalkan-seluruh-save | Dialog D-06 Hanya Mendaftar Node yang Sama, Node Lain Naik Tangga Otomatis, dan Cancel Membatalkan Seluruh Save | FE+BE. | 32 | TC-FA-SU-1108 |
| TC-FA-SU-E2E-418-remove-baris-pada-node-ancestor-dialog-d-07a-generik-dan-satu-entri-log | Remove Baris pada Node Ancestor: Dialog D-07a Generik Tanpa Daftar Descendant, Hanya Node Itu Dicabut, dan Satu Entri Log | FE+BE. | 21 | TC-FA-SU-1111 |
| TC-FA-SU-E2E-421-label-role-dan-popup-role-count-literal-node-descendant-tercakup-tidak-dihitung | Label Role dan Popup Role Count Literal: Node Descendant yang Tercakup Tidak Dihitung | FE+BE. | 24 | TC-FA-SU-1113 |
| TC-FA-SU-E2E-422-defense-in-depth-guard-server-409-confirmation-required-hanya-node-yang-sama-assign-node-lain-tanpa-confirmdowngrade | Defense-in-depth Guard Server 409 confirmation_required Hanya untuk Turun Tangga pada Node yang Sama, Assign di Node Lain Tanpa confirmDowngrade | FE+BE. | 15 | TC-FA-SU-1109 |
| TC-FA-SU-E2E-423-pemilih-group-role-target-ber-constraint-node-dalam-dan-luar-constraint-dan-assign-ke-node-dalam | Popup Select Group Group Role Target Ber-constraint: Node Dalam dan Luar Constraint dan Assign ke Node Dalam Constraint | FE+BE. | 40 | TC-FA-SU-1114, TC-FA-SU-1115 |
| TC-FA-SU-E2E-424-modal-assign-dan-popup-assign-group-transaction-role-target-ber-constraint-node-disabled-dan-tooltip-s-45 | Modal Assign Transaction Role dan Popup Assign Group Transaction Role Target Ber-constraint: Node Disabled dan Tooltip S-45 | FE+BE. | 39 | TC-FA-SU-1117, TC-FA-SU-1118 |
| TC-FA-SU-E2E-425-ancestor-constraint-disabled-di-tiga-pemilih-dan-node-constraint-dapat-dicentang | Ancestor Constraint Disabled di Tiga Pemilih dan Node Constraint Dapat Dicentang | FE+BE. | 28 | TC-FA-SU-1124 |
| TC-FA-SU-E2E-426-target-tanpa-home-group-tiga-pemilih-tanpa-penyaringan-node | Target Tanpa Home Group: Pemilih Group Role, Modal Assign Transaction Role, dan Popup Assign Group Transaction Role Tanpa Penyaringan Node | FE+BE. | 31 | TC-FA-SU-1119 |
| TC-FA-SU-E2E-427-assign-transaction-role-ke-node-dalam-constraint-dan-penugasan-lama-di-luar-constraint-tidak-dimigrasi | Assign Transaction Role ke Node Dalam Constraint dan Penugasan Lama di Luar Constraint Tampil, Tercentang, dan Dapat Dicabut | FE+BE. | 33 | TC-FA-SU-1120, TC-FA-SU-1121 |
| TC-FA-SU-E2E-428-constraint-berubah-antara-modal-assign-dibuka-dan-submit-ditolak-422-dan-pilihan-stale-dibersihkan | Constraint Berubah antara Modal Assign Dibuka dan Submit: Server Menolak 422, Pilihan Stale Dibersihkan, dan Modal Tetap Terbuka | FE+BE. | 16 | TC-FA-SU-1123 |
| TC-FA-SU-E2E-430-defense-in-depth-assign-group-role-dan-transaction-role-di-luar-home-group-constraint-ditolak-422-v09 | Defense-in-depth: Permintaan Langsung Assign Group Role dan Assign Transaction Role ke Node di Luar Home Group Constraint Ditolak 422 dengan Copy V-09 dan Seluruh Save Batal | FE+BE. | 26 | TC-FA-SU-1116, TC-FA-SU-1122 |
| TC-FA-SU-E2E-431-absence-log-assign-group-role-dan-transaction-role-ditolak-gate-home-group-tanpa-entri-di-tiga-surface | Absence Log: Permintaan Langsung Assign Group Role dan Assign Transaction Role yang Ditolak Gate Home Group Tidak Menulis Entri di Tab Changelog, Tab System Log Aktor, dan Activity Log | FE+BE. | 37 | TC-FA-SU-1116, TC-FA-SU-1122 |
| TC-FA-SU-E2E-432-absence-log-submit-modal-assign-ditolak-akibat-constraint-berubah-tanpa-entri-assign-baru | Absence Log: Submit Modal Assign Transaction Role yang Ditolak karena Constraint Berubah Tidak Menulis Entri Assign Baru di Tab Changelog | FE+BE. | 15 | TC-FA-SU-1123 |
| TC-FA-SU-E2E-434-absence-pencabutan-silent-edit-home-group-tanpa-entri-remove-dan-tanpa-notifikasi | Absence: Pencabutan Silent Group Role dan Role Transaksi akibat Edit Home Group Tanpa Entri Remove di Surface Log dan Tanpa Notifikasi Gita Permata | FE+BE. | 33 | TC-FA-SU-1125 |
| TC-FA-SU-E2E-435-edit-home-group-mencabut-group-role-dan-role-transaksi-di-luar-constraint-silent | Edit Home Group Mencabut Group Role dan Role Transaksi di Luar Constraint (Silent) | FE+BE. | 12 | TC-FA-SU-1125 |
| TC-FA-SU-E2E-436-edit-home-group-pengguna-hanya-role-transaksi-dialog-d-10-dan-constraint-node-turunan | Edit Home Group Pengguna dengan Hanya Role Transaksi: Dialog D-10, Pencabutan Approver, dan Constraint ke Node Turunan | FE+BE. | 30 | TC-FA-SU-1126, TC-FA-SU-1127 |
| TC-FA-SU-E2E-437-bulk-edit-home-group-standard-dan-read-only-dialog-d-10-hanya-untuk-standard | Bulk Edit Home Group Pengguna Standard dan Read Only: Dialog D-10 Hanya untuk Standard dan Baris Pola Read Only Tetap | FE+BE. | 28 | TC-FA-SU-1128 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua TC masuk minimal satu spec E2E.

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-SU-1 | E2E | TC-FA-SU-E2E-001-screening-user-list-breadcrumb-tanpa-page-title-dan-tanpa-tombol-back | FE+BE |
| TC-FA-SU-2 | E2E | TC-FA-SU-E2E-001-screening-user-list-breadcrumb-tanpa-page-title-dan-tanpa-tombol-back | FE+BE |
| TC-FA-SU-3 | E2E | TC-FA-SU-E2E-001-screening-user-list-breadcrumb-tanpa-page-title-dan-tanpa-tombol-back | FE+BE |
| TC-FA-SU-4 | E2E | TC-FA-SU-E2E-002-sidebar-group-tree-screening-tombol-open-collapse-dan-pencarian-node | FE+BE |
| TC-FA-SU-5 | E2E | TC-FA-SU-E2E-002-sidebar-group-tree-screening-tombol-open-collapse-dan-pencarian-node | FE+BE |
| TC-FA-SU-6 | E2E | TC-FA-SU-E2E-002-sidebar-group-tree-screening-tombol-open-collapse-dan-pencarian-node | FE+BE |
| TC-FA-SU-7 | E2E | TC-FA-SU-E2E-003-sidebar-group-tree-filter-user-list-per-node-dan-state-preservation | FE+BE |
| TC-FA-SU-8 | E2E | TC-FA-SU-E2E-003-sidebar-group-tree-filter-user-list-per-node-dan-state-preservation | FE+BE |
| TC-FA-SU-9 | E2E | TC-FA-SU-E2E-004-sel-tabel-user-list-name-role-dan-home-group | FE+BE |
| TC-FA-SU-10 | E2E | TC-FA-SU-E2E-004-sel-tabel-user-list-name-role-dan-home-group | FE+BE |
| TC-FA-SU-11 | E2E | TC-FA-SU-E2E-004-sel-tabel-user-list-name-role-dan-home-group | FE+BE |
| TC-FA-SU-12 | E2E | TC-FA-SU-E2E-015-modified-by-last-updated-dan-pengguna-baru-tanpa-role-setelah-app-access | FE+BE |
| TC-FA-SU-13 | E2E | TC-FA-SU-E2E-005-sakelar-active-dan-menu-row-action-user-list | FE+BE |
| TC-FA-SU-14 | E2E | TC-FA-SU-E2E-005-sakelar-active-dan-menu-row-action-user-list | FE+BE |
| TC-FA-SU-15 | E2E | TC-FA-SU-E2E-016-menu-row-action-baris-default-user-dan-self-termasuk-varian-pending | FE+BE |
| TC-FA-SU-16 | E2E | TC-FA-SU-E2E-015-modified-by-last-updated-dan-pengguna-baru-tanpa-role-setelah-app-access | FE+BE |
| TC-FA-SU-17 | E2E | TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit | FE+BE |
| TC-FA-SU-18 | E2E | TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit | FE+BE |
| TC-FA-SU-19 | E2E | TC-FA-SU-E2E-006-guided-tooltip-user-list-kunjungan-pertama-navigasi-replay-dan-exit | FE+BE |
| TC-FA-SU-20 | E2E | TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field | FE+BE |
| TC-FA-SU-21 | E2E | TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field | FE+BE |
| TC-FA-SU-22 | E2E | TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field | FE+BE |
| TC-FA-SU-23 | E2E | TC-FA-SU-E2E-008-user-type-detail-user-total-control-read-only-dan-group-manager | FE+BE |
| TC-FA-SU-24 | E2E | TC-FA-SU-E2E-008-user-type-detail-user-total-control-read-only-dan-group-manager | FE+BE |
| TC-FA-SU-25 | E2E | TC-FA-SU-E2E-008-user-type-detail-user-total-control-read-only-dan-group-manager | FE+BE |
| TC-FA-SU-26 | E2E | TC-FA-SU-E2E-009-user-type-detail-user-admin-basic-dan-prioritas-bila-beririsan | FE+BE |
| TC-FA-SU-27 | E2E | TC-FA-SU-E2E-009-user-type-detail-user-admin-basic-dan-prioritas-bila-beririsan | FE+BE |
| TC-FA-SU-28 | E2E | TC-FA-SU-E2E-009-user-type-detail-user-admin-basic-dan-prioritas-bila-beririsan | FE+BE |
| TC-FA-SU-29 | E2E | TC-FA-SU-E2E-007-screening-detail-user-header-general-information-dan-custom-field | FE+BE |
| TC-FA-SU-30 | E2E | TC-FA-SU-E2E-010-screening-tab-role-dan-tab-responsibilities-detail-user-serta-banner-tab-role | FE+BE |
| TC-FA-SU-31 | E2E | TC-FA-SU-E2E-010-screening-tab-role-dan-tab-responsibilities-detail-user-serta-banner-tab-role | FE+BE |
| TC-FA-SU-32 | E2E | TC-FA-SU-E2E-010-screening-tab-role-dan-tab-responsibilities-detail-user-serta-banner-tab-role | FE+BE |
| TC-FA-SU-33 | E2E | TC-FA-SU-E2E-011-screening-tab-non-login-user-changelog-system-log-transaction-admin-log-dan-user-log | FE+BE |
| TC-FA-SU-34 | E2E | TC-FA-SU-E2E-011-screening-tab-non-login-user-changelog-system-log-transaction-admin-log-dan-user-log | FE+BE |
| TC-FA-SU-35 | E2E | TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list | FE+BE |
| TC-FA-SU-36 | E2E | TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list | FE+BE |
| TC-FA-SU-37 | E2E | TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list | FE+BE |
| TC-FA-SU-38 | E2E | TC-FA-SU-E2E-012-popup-role-count-dan-empty-state-user-list | FE+BE |
| TC-FA-SU-39 | E2E | TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | FE+BE |
| TC-FA-SU-40 | E2E | TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | FE+BE |
| TC-FA-SU-41 | E2E | TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | FE+BE |
| TC-FA-SU-42 | E2E | TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | FE+BE |
| TC-FA-SU-43 | E2E | TC-FA-SU-E2E-013-android-kartu-user-list-row-action-toolbar-seleksi-dan-drawer-group-tree | FE+BE |
| TC-FA-SU-44 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-45 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-46 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-47 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-48 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-49 | E2E | TC-FA-SU-E2E-014-android-detail-user-card-list-modal-tooltip-disabled-countdown-resend-dan-bottom-sheet | FE+BE |
| TC-FA-SU-50 | E2E | TC-FA-SU-E2E-017-role-matrix-gate-sub-menu-settings-user-dan-visibilitas-elemen-ui-total-control | FE+BE. |
| TC-FA-SU-51 | E2E | TC-FA-SU-E2E-017-role-matrix-gate-sub-menu-settings-user-dan-visibilitas-elemen-ui-total-control | FE+BE. |
| TC-FA-SU-52 | E2E | TC-FA-SU-E2E-028-role-matrix-visibilitas-elemen-ui-read-only-dan-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-53 | E2E | TC-FA-SU-E2E-028-role-matrix-visibilitas-elemen-ui-read-only-dan-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-54 | E2E | TC-FA-SU-E2E-028-role-matrix-visibilitas-elemen-ui-read-only-dan-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-55 | E2E | TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom | FE+BE. |
| TC-FA-SU-56 | E2E | TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom | FE+BE. |
| TC-FA-SU-57 | E2E | TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom | FE+BE. |
| TC-FA-SU-58 | E2E | TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager | FE+BE. |
| TC-FA-SU-59 | E2E | TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager | FE+BE. |
| TC-FA-SU-60 | E2E | TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager | FE+BE. |
| TC-FA-SU-61 | E2E | TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | FE+BE. |
| TC-FA-SU-62 | E2E | TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | FE+BE. |
| TC-FA-SU-63 | E2E | TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | FE+BE. |
| TC-FA-SU-64 | E2E | TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | FE+BE. |
| TC-FA-SU-65 | E2E | TC-FA-SU-E2E-020-sidebar-group-tree-ber-scope-direct-url-detail-di-luar-scope-dan-log-disaring-scope | FE+BE. |
| TC-FA-SU-66 | E2E | TC-FA-SU-E2E-021-aktor-multi-sumber-global-role-manage-global-user-dan-role-vs-group-role-manage-user | FE+BE. |
| TC-FA-SU-67 | E2E | TC-FA-SU-E2E-021-aktor-multi-sumber-global-role-manage-global-user-dan-role-vs-group-role-manage-user | FE+BE. |
| TC-FA-SU-68 | E2E | TC-FA-SU-E2E-021-aktor-multi-sumber-global-role-manage-global-user-dan-role-vs-group-role-manage-user | FE+BE. |
| TC-FA-SU-69 | E2E | TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager | FE+BE. |
| TC-FA-SU-70 | E2E | TC-FA-SU-E2E-022-kunci-target-default-user-diri-sendiri-dan-target-total-control-atau-read-only | FE+BE. |
| TC-FA-SU-71 | E2E | TC-FA-SU-E2E-022-kunci-target-default-user-diri-sendiri-dan-target-total-control-atau-read-only | FE+BE. |
| TC-FA-SU-72 | E2E | TC-FA-SU-E2E-022-kunci-target-default-user-diri-sendiri-dan-target-total-control-atau-read-only | FE+BE. |
| TC-FA-SU-73 | E2E | TC-FA-SU-E2E-023-kunci-target-group-manager-dan-nonaktif-di-global-settings | FE+BE. |
| TC-FA-SU-74 | E2E | TC-FA-SU-E2E-023-kunci-target-group-manager-dan-nonaktif-di-global-settings | FE+BE. |
| TC-FA-SU-75 | E2E | TC-FA-SU-E2E-354-tenant-berubah-unsuspend-halaman-terbuka-saat-status-berubah-state-reflected-resend | FE+BE. |
| TC-FA-SU-76 | E2E | TC-FA-SU-E2E-355-selection-limit-tooltip-disabled-checkbox-limit-1-auto-cap-dan-perubahan-limit-live | FE+BE. |
| TC-FA-SU-77 | E2E | TC-FA-SU-E2E-353-lockdown-tenant-tooltip-prioritas-user-list-suspended-transaction-role-suspended-dan | FE+BE. |
| TC-FA-SU-78 | E2E | TC-FA-SU-E2E-358-tenant-suspended-dan-expired-kontrol-tulis-sub-tab-role-dan-aksi-tulis-paksa | FE+BE. |
| TC-FA-SU-79 | E2E | TC-FA-SU-E2E-358-tenant-suspended-dan-expired-kontrol-tulis-sub-tab-role-dan-aksi-tulis-paksa | FE+BE. |
| TC-FA-SU-80 | E2E | TC-FA-SU-E2E-353-lockdown-tenant-tooltip-prioritas-user-list-suspended-transaction-role-suspended-dan | FE+BE. |
| TC-FA-SU-81 | E2E | TC-FA-SU-E2E-354-tenant-berubah-unsuspend-halaman-terbuka-saat-status-berubah-state-reflected-resend | FE+BE. |
| TC-FA-SU-82 | E2E | TC-FA-SU-E2E-025-aktor-read-only-tab-role-read-only-dan-akses-detail-pengguna-di-luar-fams | FE+BE. |
| TC-FA-SU-83 | E2E | TC-FA-SU-E2E-025-aktor-read-only-tab-role-read-only-dan-akses-detail-pengguna-di-luar-fams | FE+BE. |
| TC-FA-SU-84 | E2E | TC-FA-SU-E2E-026-katalog-peran-manage-global-user-dan-role-dan-manage-user-dan-role-serta-sel | FE+BE. |
| TC-FA-SU-85 | E2E | TC-FA-SU-E2E-026-katalog-peran-manage-global-user-dan-role-dan-manage-user-dan-role-serta-sel | FE+BE. |
| TC-FA-SU-86 | E2E | TC-FA-SU-E2E-018-role-matrix-visibilitas-elemen-ui-manage-user-dan-role-group-group-manager-dan-kolom | FE+BE. |
| TC-FA-SU-87 | E2E | TC-FA-SU-E2E-029-single-deactivate-dan-activate-dari-sakelar-baris-dialog-konfirmasi-toast-log-dan | FE+BE. |
| TC-FA-SU-88 | E2E | TC-FA-SU-E2E-029-single-deactivate-dan-activate-dari-sakelar-baris-dialog-konfirmasi-toast-log-dan | FE+BE. |
| TC-FA-SU-89 | E2E | TC-FA-SU-E2E-039-batal-deactivate-dan-activate-single-lewat-cancel-dan-tombol-close | FE+BE. |
| TC-FA-SU-90 | E2E | TC-FA-SU-E2E-039-batal-deactivate-dan-activate-single-lewat-cancel-dan-tombol-close | FE+BE. |
| TC-FA-SU-91 | E2E | TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | FE+BE. |
| TC-FA-SU-92 | E2E | TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | FE+BE. |
| TC-FA-SU-93 | E2E | TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | FE+BE. |
| TC-FA-SU-94 | E2E | TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | FE+BE. |
| TC-FA-SU-95 | E2E | TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-96 | E2E | TC-FA-SU-E2E-030-deactivate-dari-header-detail-dan-peringatan-aset-aktif-serta-approval-tertunda | FE+BE. |
| TC-FA-SU-97 | E2E | TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain | FE+BE. |
| TC-FA-SU-98 | E2E | TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain | FE+BE. |
| TC-FA-SU-99 | E2E | TC-FA-SU-E2E-031-edit-bersamaan-status-aktif-oleh-dua-admin-dan-toggle-ke-nilai-yang-sudah-berlaku | FE+BE. |
| TC-FA-SU-100 | E2E | TC-FA-SU-E2E-031-edit-bersamaan-status-aktif-oleh-dua-admin-dan-toggle-ke-nilai-yang-sudah-berlaku | FE+BE. |
| TC-FA-SU-101 | E2E | TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-102 | E2E | TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-103 | E2E | TC-FA-SU-E2E-032-resilience-status-aktif-single-server-error-5xx-pemeriksaan-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-104 | E2E | TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk | FE+BE. |
| TC-FA-SU-105 | E2E | TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk | FE+BE. |
| TC-FA-SU-106 | E2E | TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk | FE+BE. |
| TC-FA-SU-107 | E2E | TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal | FE+BE. |
| TC-FA-SU-108 | E2E | TC-FA-SU-E2E-034-bulk-deactivate-dan-activate-seluruh-baris-eligible-serta-dialog-bulk | FE+BE. |
| TC-FA-SU-109 | E2E | TC-FA-SU-E2E-035-bulk-seleksi-campuran-dialog-dua-kelompok-skip-tier-dan-skip-nonaktif-global-settings | FE+BE. |
| TC-FA-SU-110 | E2E | TC-FA-SU-E2E-035-bulk-seleksi-campuran-dialog-dua-kelompok-skip-tier-dan-skip-nonaktif-global-settings | FE+BE. |
| TC-FA-SU-111 | E2E | TC-FA-SU-E2E-035-bulk-seleksi-campuran-dialog-dua-kelompok-skip-tier-dan-skip-nonaktif-global-settings | FE+BE. |
| TC-FA-SU-112 | E2E | TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-113 | E2E | TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-114 | E2E | TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-115 | E2E | TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-116 | E2E | TC-FA-SU-E2E-040-bulk-skip-nonaktif-global-settings-skip-tier-dan-select-all-aktor-manage-user-dan-role | FE+BE. |
| TC-FA-SU-117 | E2E | TC-FA-SU-E2E-040-bulk-skip-nonaktif-global-settings-skip-tier-dan-select-all-aktor-manage-user-dan-role | FE+BE. |
| TC-FA-SU-118 | E2E | TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal | FE+BE. |
| TC-FA-SU-119 | E2E | TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal | FE+BE. |
| TC-FA-SU-120 | E2E | TC-FA-SU-E2E-037-bulk-actions-bar-counter-select-all-unselect-all-kondisi-tampil-aksi-dan-seleksi | FE+BE. |
| TC-FA-SU-121 | E2E | TC-FA-SU-E2E-037-bulk-actions-bar-counter-select-all-unselect-all-kondisi-tampil-aksi-dan-seleksi | FE+BE. |
| TC-FA-SU-122 | E2E | TC-FA-SU-E2E-037-bulk-actions-bar-counter-select-all-unselect-all-kondisi-tampil-aksi-dan-seleksi | FE+BE. |
| TC-FA-SU-123 | E2E | TC-FA-SU-E2E-355-selection-limit-tooltip-disabled-checkbox-limit-1-auto-cap-dan-perubahan-limit-live | FE+BE. |
| TC-FA-SU-124 | E2E | TC-FA-SU-E2E-040-bulk-skip-nonaktif-global-settings-skip-tier-dan-select-all-aktor-manage-user-dan-role | FE+BE. |
| TC-FA-SU-125 | E2E | TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | FE+BE. |
| TC-FA-SU-125 | E2E | TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | FE+BE. |
| TC-FA-SU-126 | E2E | TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | FE+BE. |
| TC-FA-SU-126 | E2E | TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | FE+BE. |
| TC-FA-SU-127 | E2E | TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | FE+BE. |
| TC-FA-SU-127 | E2E | TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | FE+BE. |
| TC-FA-SU-128 | E2E | TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | FE+BE. |
| TC-FA-SU-128 | E2E | TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | FE+BE. |
| TC-FA-SU-129 | E2E | TC-FA-SU-E2E-321-defense-in-depth-status-aktif-akun-sendiri-default-user-target-tier-nonaktif-global | FE+BE. |
| TC-FA-SU-129 | E2E | TC-FA-SU-E2E-336-absence-log-request-ditolak-status-aktif-akun-sendiri-default-user-target-tier | FE+BE. |
| TC-FA-SU-130 | E2E | TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan | FE+BE. |
| TC-FA-SU-130 | E2E | TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home | FE+BE. |
| TC-FA-SU-131 | E2E | TC-FA-SU-E2E-038-aktor-manage-user-dan-role-group-dan-group-manager-pengguna-pending-activation-dan | FE+BE. |
| TC-FA-SU-132 | E2E | TC-FA-SU-E2E-038-aktor-manage-user-dan-role-group-dan-group-manager-pengguna-pending-activation-dan | FE+BE. |
| TC-FA-SU-133 | E2E | TC-FA-SU-E2E-038-aktor-manage-user-dan-role-group-dan-group-manager-pengguna-pending-activation-dan | FE+BE. |
| TC-FA-SU-134 | E2E | TC-FA-SU-E2E-033-resilience-bulk-status-aktif-pemeriksaan-gagal-sebagian-gagal-dan-seluruh-item-gagal | FE+BE. |
| TC-FA-SU-135 | E2E | TC-FA-SU-E2E-041-resend-activation-dan-confirmation-email-single-dari-row-action | FE+BE. |
| TC-FA-SU-136 | E2E | TC-FA-SU-E2E-041-resend-activation-dan-confirmation-email-single-dari-row-action | FE+BE. |
| TC-FA-SU-137 | E2E | TC-FA-SU-E2E-042-resend-dari-header-detail-user-tanpa-kunci-target-dan-pengguna-inactive-atau-pending | FE+BE. |
| TC-FA-SU-138 | E2E | TC-FA-SU-E2E-043-cooldown-resend-hitung-mundur-60-sampai-1-dan-batas-tepat-t-60-detik | FE+BE. |
| TC-FA-SU-139 | E2E | TC-FA-SU-E2E-043-cooldown-resend-hitung-mundur-60-sampai-1-dan-batas-tepat-t-60-detik | FE+BE. |
| TC-FA-SU-140 | E2E | TC-FA-SU-E2E-057-cooldown-resend-pengiriman-berulang-dan-pemisahan-per-pengguna-dan-jenis-email | FE+BE. |
| TC-FA-SU-141 | E2E | TC-FA-SU-E2E-057-cooldown-resend-pengiriman-berulang-dan-pemisahan-per-pengguna-dan-jenis-email | FE+BE. |
| TC-FA-SU-142 | E2E | TC-FA-SU-E2E-057-cooldown-resend-pengiriman-berulang-dan-pemisahan-per-pengguna-dan-jenis-email | FE+BE. |
| TC-FA-SU-143 | E2E | TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log | FE+BE. |
| TC-FA-SU-144 | E2E | TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log | FE+BE. |
| TC-FA-SU-145 | E2E | TC-FA-SU-E2E-044-resend-penolakan-cooldown-dari-tampilan-basi-dan-status-berubah-setelah-halaman-dimuat | FE+BE. |
| TC-FA-SU-146 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-146 | E2E | TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | FE+BE. |
| TC-FA-SU-147 | E2E | TC-FA-SU-E2E-058-visibilitas-aksi-resend-menurut-status-pengguna-di-menu-baris-dan-header-detail | FE+BE. |
| TC-FA-SU-148 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-148 | E2E | TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | FE+BE. |
| TC-FA-SU-149 | E2E | TC-FA-SU-E2E-044-resend-penolakan-cooldown-dari-tampilan-basi-dan-status-berubah-setelah-halaman-dimuat | FE+BE. |
| TC-FA-SU-150 | E2E | TC-FA-SU-E2E-042-resend-dari-header-detail-user-tanpa-kunci-target-dan-pengguna-inactive-atau-pending | FE+BE. |
| TC-FA-SU-151 | E2E | TC-FA-SU-E2E-042-resend-dari-header-detail-user-tanpa-kunci-target-dan-pengguna-inactive-atau-pending | FE+BE. |
| TC-FA-SU-152 | E2E | TC-FA-SU-E2E-359-tenant-suspended-visibilitas-resend-per-aktor-dan-edit-home-group-hidden | FE+BE. |
| TC-FA-SU-153 | E2E | TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi | FE+BE. |
| TC-FA-SU-154 | E2E | TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi | FE+BE. |
| TC-FA-SU-155 | E2E | TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi | FE+BE. |
| TC-FA-SU-156 | E2E | TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log | FE+BE. |
| TC-FA-SU-157 | E2E | TC-FA-SU-E2E-045-bulk-resend-activation-email-sukses-sebagian-cooldown-seluruh-cooldown-dan-seleksi | FE+BE. |
| TC-FA-SU-158 | E2E | TC-FA-SU-E2E-046-resilience-resend-gagal-kirim-email-bulk-gagal-dan-kegagalan-penulisan-log | FE+BE. |
| TC-FA-SU-159 | E2E | TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan | FE+BE. |
| TC-FA-SU-160 | E2E | TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan | FE+BE. |
| TC-FA-SU-161 | E2E | TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan | FE+BE. |
| TC-FA-SU-162 | E2E | TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan | FE+BE. |
| TC-FA-SU-163 | E2E | TC-FA-SU-E2E-048-nyalakan-kembali-switch-ubah-checkbox-update-dan-checkbox-read-terkunci | FE+BE. |
| TC-FA-SU-164 | E2E | TC-FA-SU-E2E-048-nyalakan-kembali-switch-ubah-checkbox-update-dan-checkbox-read-terkunci | FE+BE. |
| TC-FA-SU-165 | E2E | TC-FA-SU-E2E-048-nyalakan-kembali-switch-ubah-checkbox-update-dan-checkbox-read-terkunci | FE+BE. |
| TC-FA-SU-166 | E2E | TC-FA-SU-E2E-049-default-checkbox-switch-on-pertama-dan-indikator-loading-switch | FE+BE. |
| TC-FA-SU-167 | E2E | TC-FA-SU-E2E-051-resilience-global-role-switch-dan-checkbox-gagal-disimpan-serta-auto-revert-gagal | FE+BE. |
| TC-FA-SU-168 | E2E | TC-FA-SU-E2E-051-resilience-global-role-switch-dan-checkbox-gagal-disimpan-serta-auto-revert-gagal | FE+BE. |
| TC-FA-SU-169 | E2E | TC-FA-SU-E2E-050-no-op-switch-dan-checkbox-global-role-akibat-perubahan-sesi-lain | FE+BE. |
| TC-FA-SU-170 | E2E | TC-FA-SU-E2E-050-no-op-switch-dan-checkbox-global-role-akibat-perubahan-sesi-lain | FE+BE. |
| TC-FA-SU-171 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-171 | E2E | TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | FE+BE. |
| TC-FA-SU-172 | E2E | TC-FA-SU-E2E-049-default-checkbox-switch-on-pertama-dan-indikator-loading-switch | FE+BE. |
| TC-FA-SU-173 | E2E | TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | FE+BE. |
| TC-FA-SU-174 | E2E | TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | FE+BE. |
| TC-FA-SU-175 | E2E | TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | FE+BE. |
| TC-FA-SU-176 | E2E | TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain | FE+BE. |
| TC-FA-SU-177 | E2E | TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | FE+BE. |
| TC-FA-SU-178 | E2E | TC-FA-SU-E2E-052-auto-revert-total-control-pada-global-role-dialog-konfirmasi-cancel-dan-switch-target | FE+BE. |
| TC-FA-SU-179 | E2E | TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain | FE+BE. |
| TC-FA-SU-180 | E2E | TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain | FE+BE. |
| TC-FA-SU-181 | E2E | TC-FA-SU-E2E-053-auto-revert-read-only-banner-tier-banner-group-manager-dan-tier-dilepas-aktor-lain | FE+BE. |
| TC-FA-SU-182 | E2E | TC-FA-SU-E2E-054-kunci-global-role-default-user-diri-sendiri-tier-aktor-ber-scope-grup-dan-aktor-tanpa | FE+BE. |
| TC-FA-SU-183 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-183 | E2E | TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | FE+BE. |
| TC-FA-SU-184 | E2E | TC-FA-SU-E2E-054-kunci-global-role-default-user-diri-sendiri-tier-aktor-ber-scope-grup-dan-aktor-tanpa | FE+BE. |
| TC-FA-SU-185 | E2E | TC-FA-SU-E2E-054-kunci-global-role-default-user-diri-sendiri-tier-aktor-ber-scope-grup-dan-aktor-tanpa | FE+BE. |
| TC-FA-SU-186 | E2E | TC-FA-SU-E2E-055-eksklusivitas-global-role-manage-global-user-dan-role-vs-group-role-manage-user-dan | FE+BE. |
| TC-FA-SU-187 | E2E | TC-FA-SU-E2E-055-eksklusivitas-global-role-manage-global-user-dan-role-vs-group-role-manage-user-dan | FE+BE. |
| TC-FA-SU-188 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-189 | E2E | TC-FA-SU-E2E-056-cascade-total-control-terhadap-group-role-manage-user-dan-role-dan-sinkronisasi-dua | FE+BE. |
| TC-FA-SU-190 | E2E | TC-FA-SU-E2E-056-cascade-total-control-terhadap-group-role-manage-user-dan-role-dan-sinkronisasi-dua | FE+BE. |
| TC-FA-SU-191 | E2E | TC-FA-SU-E2E-051-resilience-global-role-switch-dan-checkbox-gagal-disimpan-serta-auto-revert-gagal | FE+BE. |
| TC-FA-SU-192 | E2E | TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role | FE+BE. |
| TC-FA-SU-193 | E2E | TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role | FE+BE. |
| TC-FA-SU-194 | E2E | TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role | FE+BE. |
| TC-FA-SU-195 | E2E | TC-FA-SU-E2E-059-screening-sub-tab-group-role-dan-popup-assign-group-role | FE+BE. |
| TC-FA-SU-196 | E2E | TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role | FE+BE. |
| TC-FA-SU-197 | E2E | TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role | FE+BE. |
| TC-FA-SU-198 | E2E | TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role | FE+BE. |
| TC-FA-SU-199 | E2E | TC-FA-SU-E2E-060-pilih-node-select-group-cancel-popup-dan-tambah-grup-ke-group-role | FE+BE. |
| TC-FA-SU-200 | E2E | TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan | FE+BE. |
| TC-FA-SU-201 | E2E | TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan | FE+BE. |
| TC-FA-SU-202 | E2E | TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan | FE+BE. |
| TC-FA-SU-203 | E2E | TC-FA-SU-E2E-061-hapus-grup-ubah-checkbox-crud-save-campuran-dan-save-tanpa-perubahan | FE+BE. |
| TC-FA-SU-204 | E2E | TC-FA-SU-E2E-062-tambah-lalu-hapus-sebelum-save-save-dengan-0-grup-dan-clear-field | FE+BE. |
| TC-FA-SU-205 | E2E | TC-FA-SU-E2E-062-tambah-lalu-hapus-sebelum-save-save-dengan-0-grup-dan-clear-field | FE+BE. |
| TC-FA-SU-206 | E2E | TC-FA-SU-E2E-062-tambah-lalu-hapus-sebelum-save-save-dengan-0-grup-dan-clear-field | FE+BE. |
| TC-FA-SU-207 | E2E | TC-FA-SU-E2E-063-dialog-unsaved-changes-dan-backdrop-popup-assign-group-role | FE+BE. |
| TC-FA-SU-208 | E2E | TC-FA-SU-E2E-063-dialog-unsaved-changes-dan-backdrop-popup-assign-group-role | FE+BE. |
| TC-FA-SU-209 | E2E | TC-FA-SU-E2E-087-penugasan-grup-ganda-dan-grup-dihapus-sebelum-save-popup-assign-group-role | FE+BE. |
| TC-FA-SU-210 | E2E | TC-FA-SU-E2E-087-penugasan-grup-ganda-dan-grup-dihapus-sebelum-save-popup-assign-group-role | FE+BE. |
| TC-FA-SU-211 | E2E | TC-FA-SU-E2E-064-resilience-group-role-save-popup-assign-gagal-karena-server-error | FE+BE. |
| TC-FA-SU-212 | E2E | TC-FA-SU-E2E-065-group-manager-pada-group-role-dialog-remove-konfirmasi-dan-cancel | FE+BE. |
| TC-FA-SU-213 | E2E | TC-FA-SU-E2E-065-group-manager-pada-group-role-dialog-remove-konfirmasi-dan-cancel | FE+BE. |
| TC-FA-SU-214 | E2E | TC-FA-SU-E2E-065-group-manager-pada-group-role-dialog-remove-konfirmasi-dan-cancel | FE+BE. |
| TC-FA-SU-215 | E2E | TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup | FE+BE. |
| TC-FA-SU-216 | E2E | TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup | FE+BE. |
| TC-FA-SU-217 | E2E | TC-FA-SU-E2E-066-group-manager-save-0-grup-auto-revert-beberapa-grup-dan-auto-revert-tier-dari-popup | FE+BE. |
| TC-FA-SU-218 | E2E | TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup | FE+BE. |
| TC-FA-SU-219 | E2E | TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup | FE+BE. |
| TC-FA-SU-220 | E2E | TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup | FE+BE. |
| TC-FA-SU-221 | E2E | TC-FA-SU-E2E-067-kunci-baris-group-role-target-group-manager-default-user-dan-aktor-ber-scope-grup | FE+BE. |
| TC-FA-SU-222 | E2E | TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-222 | E2E | TC-FA-SU-E2E-338-absence-log-request-ditolak-transaction-role-dan-group-role-target-tier-di-luar-scope | FE+BE. |
| TC-FA-SU-223 | E2E | TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-223 | E2E | TC-FA-SU-E2E-338-absence-log-request-ditolak-transaction-role-dan-group-role-target-tier-di-luar-scope | FE+BE. |
| TC-FA-SU-224 | E2E | TC-FA-SU-E2E-068-detail-group-assignment-dan-group-dihapus-di-settings-groups | FE+BE. |
| TC-FA-SU-225 | E2E | TC-FA-SU-E2E-068-detail-group-assignment-dan-group-dihapus-di-settings-groups | FE+BE. |
| TC-FA-SU-226 | E2E | TC-FA-SU-E2E-088-sinkronisasi-dua-arah-group-role-dan-group-role-tanpa-switch | FE+BE. |
| TC-FA-SU-227 | E2E | TC-FA-SU-E2E-088-sinkronisasi-dua-arah-group-role-dan-group-role-tanpa-switch | FE+BE. |
| TC-FA-SU-228 | E2E | TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-229 | E2E | TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-230 | E2E | TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-231 | E2E | TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-232 | E2E | TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-233 | E2E | TC-FA-SU-E2E-070-modal-assign-transaction-role-ganti-transaction-label-group-dan-popup-tree-group | FE+BE. |
| TC-FA-SU-234 | E2E | TC-FA-SU-E2E-070-modal-assign-transaction-role-ganti-transaction-label-group-dan-popup-tree-group | FE+BE. |
| TC-FA-SU-235 | E2E | TC-FA-SU-E2E-070-modal-assign-transaction-role-ganti-transaction-label-group-dan-popup-tree-group | FE+BE. |
| TC-FA-SU-236 | E2E | TC-FA-SU-E2E-071-modal-assign-transaction-role-katalog-transaction-opsi-role-dan-opsi-disabled | FE+BE. |
| TC-FA-SU-237 | E2E | TC-FA-SU-E2E-071-modal-assign-transaction-role-katalog-transaction-opsi-role-dan-opsi-disabled | FE+BE. |
| TC-FA-SU-238 | E2E | TC-FA-SU-E2E-071-modal-assign-transaction-role-katalog-transaction-opsi-role-dan-opsi-disabled | FE+BE. |
| TC-FA-SU-239 | E2E | TC-FA-SU-E2E-072-validasi-submit-modal-assign-transaction-role-semua-kosong-sebagian-kosong-dan-clear | FE+BE. |
| TC-FA-SU-240 | E2E | TC-FA-SU-E2E-072-validasi-submit-modal-assign-transaction-role-semua-kosong-sebagian-kosong-dan-clear | FE+BE. |
| TC-FA-SU-241 | E2E | TC-FA-SU-E2E-072-validasi-submit-modal-assign-transaction-role-semua-kosong-sebagian-kosong-dan-clear | FE+BE. |
| TC-FA-SU-242 | E2E | TC-FA-SU-E2E-073-penutupan-modal-assign-transaction-role-dengan-isian-dan-aksesibilitas-modal | FE+BE. |
| TC-FA-SU-243 | E2E | TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga | FE+BE. |
| TC-FA-SU-244 | E2E | TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga | FE+BE. |
| TC-FA-SU-245 | E2E | TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga | FE+BE. |
| TC-FA-SU-246 | E2E | TC-FA-SU-E2E-074-assign-transaction-role-satu-grup-beberapa-grup-stay-on-this-form-dan-naik-tangga | FE+BE. |
| TC-FA-SU-247 | E2E | TC-FA-SU-E2E-075-turun-tangga-dialog-change-transaction-role-konfirmasi-atomik-dan-cancel | FE+BE. |
| TC-FA-SU-248 | E2E | TC-FA-SU-E2E-075-turun-tangga-dialog-change-transaction-role-konfirmasi-atomik-dan-cancel | FE+BE. |
| TC-FA-SU-249 | E2E | TC-FA-SU-E2E-075-turun-tangga-dialog-change-transaction-role-konfirmasi-atomik-dan-cancel | FE+BE. |
| TC-FA-SU-250 | E2E | TC-FA-SU-E2E-076-dialog-turun-tangga-role-berbeda-per-grup-approver-di-luar-tangga-dan-tangga-dua | FE+BE. |
| TC-FA-SU-251 | E2E | TC-FA-SU-E2E-076-dialog-turun-tangga-role-berbeda-per-grup-approver-di-luar-tangga-dan-tangga-dua | FE+BE. |
| TC-FA-SU-252 | E2E | TC-FA-SU-E2E-076-dialog-turun-tangga-role-berbeda-per-grup-approver-di-luar-tangga-dan-tangga-dua | FE+BE. |
| TC-FA-SU-253 | E2E | TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | FE+BE. |
| TC-FA-SU-254 | E2E | TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | FE+BE. |
| TC-FA-SU-255 | E2E | TC-FA-SU-E2E-078-resilience-transaction-role-assign-gagal-bulk-remove-atomik-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-256 | E2E | TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | FE+BE. |
| TC-FA-SU-257 | E2E | TC-FA-SU-E2E-079-popup-assign-group-transaction-role-screening-tambah-grup-dan-cabut-grup | FE+BE. |
| TC-FA-SU-258 | E2E | TC-FA-SU-E2E-079-popup-assign-group-transaction-role-screening-tambah-grup-dan-cabut-grup | FE+BE. |
| TC-FA-SU-259 | E2E | TC-FA-SU-E2E-079-popup-assign-group-transaction-role-screening-tambah-grup-dan-cabut-grup | FE+BE. |
| TC-FA-SU-260 | E2E | TC-FA-SU-E2E-080-popup-assign-group-tambah-dan-cabut-sekaligus-cabut-semua-dan-cancel-tanpa-unsaved | FE+BE. |
| TC-FA-SU-261 | E2E | TC-FA-SU-E2E-080-popup-assign-group-tambah-dan-cabut-sekaligus-cabut-semua-dan-cancel-tanpa-unsaved | FE+BE. |
| TC-FA-SU-262 | E2E | TC-FA-SU-E2E-080-popup-assign-group-tambah-dan-cabut-sekaligus-cabut-semua-dan-cancel-tanpa-unsaved | FE+BE. |
| TC-FA-SU-263 | E2E | TC-FA-SU-E2E-081-popup-assign-group-cancel-dialog-d-06-d-07-dan-node-disabled-already-assigned | FE+BE. |
| TC-FA-SU-264 | E2E | TC-FA-SU-E2E-081-popup-assign-group-cancel-dialog-d-06-d-07-dan-node-disabled-already-assigned | FE+BE. |
| TC-FA-SU-265 | E2E | TC-FA-SU-E2E-082-remove-satu-baris-transaction-role-cancel-dialog-dan-empty-state-berganti | FE+BE. |
| TC-FA-SU-266 | E2E | TC-FA-SU-E2E-082-remove-satu-baris-transaction-role-cancel-dialog-dan-empty-state-berganti | FE+BE. |
| TC-FA-SU-267 | E2E | TC-FA-SU-E2E-083-bulk-remove-transaction-role-counter-dialog-plural-singular-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-268 | E2E | TC-FA-SU-E2E-083-bulk-remove-transaction-role-counter-dialog-plural-singular-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-269 | E2E | TC-FA-SU-E2E-078-resilience-transaction-role-assign-gagal-bulk-remove-atomik-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-270 | E2E | TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden | FE+BE. |
| TC-FA-SU-271 | E2E | TC-FA-SU-E2E-084-kunci-transaction-role-bagi-aktor-ber-scope-grup-dan-target-tier | FE+BE. |
| TC-FA-SU-272 | E2E | TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-272 | E2E | TC-FA-SU-E2E-338-absence-log-request-ditolak-transaction-role-dan-group-role-target-tier-di-luar-scope | FE+BE. |
| TC-FA-SU-273 | E2E | TC-FA-SU-E2E-084-kunci-transaction-role-bagi-aktor-ber-scope-grup-dan-target-tier | FE+BE. |
| TC-FA-SU-274 | E2E | TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden | FE+BE. |
| TC-FA-SU-275 | E2E | TC-FA-SU-E2E-085-transaction-role-selection-limit-5-tanpa-auto-revert-tier-dan-read-only-hidden | FE+BE. |
| TC-FA-SU-276 | E2E | TC-FA-SU-E2E-078-resilience-transaction-role-assign-gagal-bulk-remove-atomik-gagal-dan-kegagalan | FE+BE. |
| TC-FA-SU-277 | E2E | TC-FA-SU-E2E-086-transaction-role-sinkronisasi-role-dan-permission-dan-katalog-tanpa-gating-addon | FE+BE. |
| TC-FA-SU-278 | E2E | TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | FE+BE. |
| TC-FA-SU-279 | E2E | TC-FA-SU-E2E-086-transaction-role-sinkronisasi-role-dan-permission-dan-katalog-tanpa-gating-addon | FE+BE. |
| TC-FA-SU-280 | E2E | TC-FA-SU-E2E-077-transaction-role-save-identik-guard-server-turun-tangga-grup-dihapus-edit-bersamaan | FE+BE. |
| TC-FA-SU-281 | E2E | TC-FA-SU-E2E-089-popup-select-home-group-singular-screening-tombol-select-dan-cancel | FE+BE. |
| TC-FA-SU-282 | E2E | TC-FA-SU-E2E-090-role-matrix-visibilitas-edit-home-group-dan-field-home-group-di-detail-user-per-aktor | FE+BE. |
| TC-FA-SU-283 | E2E | TC-FA-SU-E2E-359-tenant-suspended-visibilitas-resend-per-aktor-dan-edit-home-group-hidden | FE+BE. |
| TC-FA-SU-284 | E2E | TC-FA-SU-E2E-090-role-matrix-visibilitas-edit-home-group-dan-field-home-group-di-detail-user-per-aktor | FE+BE. |
| TC-FA-SU-285 | E2E | TC-FA-SU-E2E-091-edit-home-group-single-row-action-ikon-edit-detail-dan-kosongkan-home-group | FE+BE. |
| TC-FA-SU-286 | E2E | TC-FA-SU-E2E-091-edit-home-group-single-row-action-ikon-edit-detail-dan-kosongkan-home-group | FE+BE. |
| TC-FA-SU-287 | E2E | TC-FA-SU-E2E-089-popup-select-home-group-singular-screening-tombol-select-dan-cancel | FE+BE. |
| TC-FA-SU-288 | E2E | TC-FA-SU-E2E-091-edit-home-group-single-row-action-ikon-edit-detail-dan-kosongkan-home-group | FE+BE. |
| TC-FA-SU-289 | E2E | TC-FA-SU-E2E-089-popup-select-home-group-singular-screening-tombol-select-dan-cancel | FE+BE. |
| TC-FA-SU-290 | E2E | TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan | FE+BE. |
| TC-FA-SU-291 | E2E | TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan | FE+BE. |
| TC-FA-SU-292 | E2E | TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan | FE+BE. |
| TC-FA-SU-293 | E2E | TC-FA-SU-E2E-092-constraint-home-group-dialog-role-outside-constraint-konfirmasi-revoke-cancel-dan | FE+BE. |
| TC-FA-SU-294 | E2E | TC-FA-SU-E2E-093-dialog-gabungan-group-manager-pada-edit-home-group-konfirmasi-cancel-dan-satu-grup | FE+BE. |
| TC-FA-SU-295 | E2E | TC-FA-SU-E2E-093-dialog-gabungan-group-manager-pada-edit-home-group-konfirmasi-cancel-dan-satu-grup | FE+BE. |
| TC-FA-SU-296 | E2E | TC-FA-SU-E2E-093-dialog-gabungan-group-manager-pada-edit-home-group-konfirmasi-cancel-dan-satu-grup | FE+BE. |
| TC-FA-SU-297 | E2E | TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage | FE+BE. |
| TC-FA-SU-298 | E2E | TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage | FE+BE. |
| TC-FA-SU-299 | E2E | TC-FA-SU-E2E-106-edit-home-group-target-total-control-dan-read-only-oleh-default-user-dan-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-300 | E2E | TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | FE+BE. |
| TC-FA-SU-301 | E2E | TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal | FE+BE. |
| TC-FA-SU-302 | E2E | TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | FE+BE. |
| TC-FA-SU-303 | E2E | TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal | FE+BE. |
| TC-FA-SU-304 | E2E | TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan | FE+BE. |
| TC-FA-SU-304 | E2E | TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home | FE+BE. |
| TC-FA-SU-305 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-305 | E2E | TC-FA-SU-E2E-346-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-306 | E2E | TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh | FE+BE. |
| TC-FA-SU-307 | E2E | TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh | FE+BE. |
| TC-FA-SU-308 | E2E | TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh | FE+BE. |
| TC-FA-SU-309 | E2E | TC-FA-SU-E2E-097-bulk-edit-home-group-screening-popup-bulk-sukses-serentak-sebagian-skip-dan-seluruh | FE+BE. |
| TC-FA-SU-310 | E2E | TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal | FE+BE. |
| TC-FA-SU-311 | E2E | TC-FA-SU-E2E-096-resilience-edit-home-group-server-error-kegagalan-penulisan-log-bulk-sebagian-gagal | FE+BE. |
| TC-FA-SU-312 | E2E | TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel | FE+BE. |
| TC-FA-SU-313 | E2E | TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel | FE+BE. |
| TC-FA-SU-314 | E2E | TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel | FE+BE. |
| TC-FA-SU-315 | E2E | TC-FA-SU-E2E-098-bulk-edit-home-group-kosongkan-dialog-gabungan-per-pengguna-dan-hasil-cancel | FE+BE. |
| TC-FA-SU-316 | E2E | TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | FE+BE. |
| TC-FA-SU-317 | E2E | TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | FE+BE. |
| TC-FA-SU-318 | E2E | TC-FA-SU-E2E-095-edit-home-group-grup-dihapus-no-op-dari-sesi-lain-edit-bersamaan-dan-kandidat-picker | FE+BE. |
| TC-FA-SU-319 | E2E | TC-FA-SU-E2E-094-dialog-gabungan-beberapa-grup-group-manager-kunci-baris-notifikasi-dan-aktor-manage | FE+BE. |
| TC-FA-SU-320 | E2E | TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search | FE+BE. |
| TC-FA-SU-321 | E2E | TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search | FE+BE. |
| TC-FA-SU-322 | E2E | TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search | FE+BE. |
| TC-FA-SU-323 | E2E | TC-FA-SU-E2E-114-tabel-user-list-screening-dan-search | FE+BE. |
| TC-FA-SU-324 | E2E | TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1 | FE+BE. |
| TC-FA-SU-325 | E2E | TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1 | FE+BE. |
| TC-FA-SU-326 | E2E | TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1 | FE+BE. |
| TC-FA-SU-327 | E2E | TC-FA-SU-E2E-115-tabel-user-list-search-bagian-1 | FE+BE. |
| TC-FA-SU-328 | E2E | TC-FA-SU-E2E-116-tabel-user-list-search-bagian-2 | FE+BE. |
| TC-FA-SU-329 | E2E | TC-FA-SU-E2E-116-tabel-user-list-search-bagian-2 | FE+BE. |
| TC-FA-SU-330 | E2E | TC-FA-SU-E2E-116-tabel-user-list-search-bagian-2 | FE+BE. |
| TC-FA-SU-331 | E2E | TC-FA-SU-E2E-117-tabel-user-list-sort-bagian-1 | FE+BE. |
| TC-FA-SU-332 | E2E | TC-FA-SU-E2E-117-tabel-user-list-sort-bagian-1 | FE+BE. |
| TC-FA-SU-333 | E2E | TC-FA-SU-E2E-117-tabel-user-list-sort-bagian-1 | FE+BE. |
| TC-FA-SU-334 | E2E | TC-FA-SU-E2E-118-tabel-user-list-sort-bagian-2 | FE+BE. |
| TC-FA-SU-335 | E2E | TC-FA-SU-E2E-118-tabel-user-list-sort-bagian-2 | FE+BE. |
| TC-FA-SU-336 | E2E | TC-FA-SU-E2E-118-tabel-user-list-sort-bagian-2 | FE+BE. |
| TC-FA-SU-337 | E2E | TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3 | FE+BE. |
| TC-FA-SU-338 | E2E | TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3 | FE+BE. |
| TC-FA-SU-339 | E2E | TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3 | FE+BE. |
| TC-FA-SU-340 | E2E | TC-FA-SU-E2E-120-tabel-user-list-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-341 | E2E | TC-FA-SU-E2E-120-tabel-user-list-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-342 | E2E | TC-FA-SU-E2E-120-tabel-user-list-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-343 | E2E | TC-FA-SU-E2E-121-tabel-user-list-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-344 | E2E | TC-FA-SU-E2E-121-tabel-user-list-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-345 | E2E | TC-FA-SU-E2E-121-tabel-user-list-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-346 | E2E | TC-FA-SU-E2E-122-tabel-user-list-filter-dan-kontrol-filter-bagian-3 | FE+BE. |
| TC-FA-SU-347 | E2E | TC-FA-SU-E2E-122-tabel-user-list-filter-dan-kontrol-filter-bagian-3 | FE+BE. |
| TC-FA-SU-348 | E2E | TC-FA-SU-E2E-122-tabel-user-list-filter-dan-kontrol-filter-bagian-3 | FE+BE. |
| TC-FA-SU-349 | E2E | TC-FA-SU-E2E-123-tabel-user-list-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-350 | E2E | TC-FA-SU-E2E-123-tabel-user-list-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-351 | E2E | TC-FA-SU-E2E-123-tabel-user-list-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-352 | E2E | TC-FA-SU-E2E-124-tabel-user-list-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-353 | E2E | TC-FA-SU-E2E-124-tabel-user-list-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-354 | E2E | TC-FA-SU-E2E-125-tabel-user-list-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-355 | E2E | TC-FA-SU-E2E-125-tabel-user-list-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-356 | E2E | TC-FA-SU-E2E-126-tabel-user-list-setup-column-bagian-3 | FE+BE. |
| TC-FA-SU-357 | E2E | TC-FA-SU-E2E-126-tabel-user-list-setup-column-bagian-3 | FE+BE. |
| TC-FA-SU-358 | E2E | TC-FA-SU-E2E-126-tabel-user-list-setup-column-bagian-3 | FE+BE. |
| TC-FA-SU-359 | E2E | TC-FA-SU-E2E-127-tabel-user-list-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-360 | E2E | TC-FA-SU-E2E-127-tabel-user-list-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-361 | E2E | TC-FA-SU-E2E-128-tabel-user-list-download | FE+BE. |
| TC-FA-SU-362 | E2E | TC-FA-SU-E2E-370-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-363 | E2E | TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-364 | E2E | TC-FA-SU-E2E-127-tabel-user-list-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-365 | E2E | TC-FA-SU-E2E-375-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-7 | FE+BE. |
| TC-FA-SU-366 | E2E | TC-FA-SU-E2E-107-kolom-curated-user-list-urutan-setelah-last-updated-dan-kolom-tag-pada-plan-starter | FE+BE. |
| TC-FA-SU-367 | E2E | TC-FA-SU-E2E-377-kolom-dan-field-tag-tidak-tersedia-pada-plan-starter-dan-tersedia-pada-plan-professional | FE+BE. |
| TC-FA-SU-368 | E2E | TC-FA-SU-E2E-356-download-user-list-lebih-dari-5-000-baris-loading-screen-unduhan-langsung-dan-tanpa | FE+BE. |
| TC-FA-SU-369 | E2E | TC-FA-SU-E2E-108-label-role-count-modified-by-dan-last-updated-mengikuti-aksi-dan-temporary-until-non | FE+BE. |
| TC-FA-SU-370 | E2E | TC-FA-SU-E2E-108-label-role-count-modified-by-dan-last-updated-mengikuti-aksi-dan-temporary-until-non | FE+BE. |
| TC-FA-SU-371 | E2E | TC-FA-SU-E2E-129-modified-by-last-updated-mengikuti-aksi-dan-temporary-until-non-temporary-user-list | FE+BE. |
| TC-FA-SU-372 | E2E | TC-FA-SU-E2E-129-modified-by-last-updated-mengikuti-aksi-dan-temporary-until-non-temporary-user-list | FE+BE. |
| TC-FA-SU-373 | E2E | TC-FA-SU-E2E-109-pengguna-tanpa-app-access-atribut-identitas-read-only-dan-sidebar-group-tree-sebagai | FE+BE. |
| TC-FA-SU-374 | E2E | TC-FA-SU-E2E-109-pengguna-tanpa-app-access-atribut-identitas-read-only-dan-sidebar-group-tree-sebagai | FE+BE. |
| TC-FA-SU-375 | E2E | TC-FA-SU-E2E-130-node-sidebar-group-tree-sebagai-kriteria-data-search-filter-seleksi-select-all-dan-download | FE+BE. |
| TC-FA-SU-376 | E2E | TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action | FE+BE. |
| TC-FA-SU-377 | E2E | TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab | FE+BE. |
| TC-FA-SU-378 | E2E | TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab | FE+BE. |
| TC-FA-SU-379 | E2E | TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action | FE+BE. |
| TC-FA-SU-380 | E2E | TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action | FE+BE. |
| TC-FA-SU-381 | E2E | TC-FA-SU-E2E-112-setup-column-sub-tab-global-role-dan-group-role-serta-sort-dan-ikon-row-action | FE+BE. |
| TC-FA-SU-382 | E2E | TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab | FE+BE. |
| TC-FA-SU-383 | E2E | TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-384 | E2E | TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-385 | E2E | TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-386 | E2E | TC-FA-SU-E2E-131-sub-tab-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-387 | E2E | TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-388 | E2E | TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-389 | E2E | TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-390 | E2E | TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-391 | E2E | TC-FA-SU-E2E-132-sub-tab-transaction-role-search-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-392 | E2E | TC-FA-SU-E2E-133-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-393 | E2E | TC-FA-SU-E2E-133-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-394 | E2E | TC-FA-SU-E2E-133-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-395 | E2E | TC-FA-SU-E2E-134-sub-tab-transaction-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-396 | E2E | TC-FA-SU-E2E-149-sub-tab-transaction-role-perilaku-filter-panel-dan-chip-dropdown-filter | FE+BE. |
| TC-FA-SU-397 | E2E | TC-FA-SU-E2E-149-sub-tab-transaction-role-perilaku-filter-panel-dan-chip-dropdown-filter | FE+BE. |
| TC-FA-SU-398 | E2E | TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-399 | E2E | TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-400 | E2E | TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-401 | E2E | TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-402 | E2E | TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-403 | E2E | TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-404 | E2E | TC-FA-SU-E2E-137-sub-tab-transaction-role-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-405 | E2E | TC-FA-SU-E2E-137-sub-tab-transaction-role-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-406 | E2E | TC-FA-SU-E2E-360-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-407 | E2E | TC-FA-SU-E2E-137-sub-tab-transaction-role-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-408 | E2E | TC-FA-SU-E2E-136-sub-tab-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-409 | E2E | TC-FA-SU-E2E-135-sub-tab-transaction-role-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-410 | E2E | TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-411 | E2E | TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-412 | E2E | TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-413 | E2E | TC-FA-SU-E2E-138-sub-tab-borrowed-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-414 | E2E | TC-FA-SU-E2E-139-sub-tab-borrowed-assets-search | FE+BE. |
| TC-FA-SU-415 | E2E | TC-FA-SU-E2E-139-sub-tab-borrowed-assets-search | FE+BE. |
| TC-FA-SU-416 | E2E | TC-FA-SU-E2E-139-sub-tab-borrowed-assets-search | FE+BE. |
| TC-FA-SU-417 | E2E | TC-FA-SU-E2E-140-sub-tab-borrowed-assets-sort | FE+BE. |
| TC-FA-SU-418 | E2E | TC-FA-SU-E2E-140-sub-tab-borrowed-assets-sort | FE+BE. |
| TC-FA-SU-419 | E2E | TC-FA-SU-E2E-140-sub-tab-borrowed-assets-sort | FE+BE. |
| TC-FA-SU-420 | E2E | TC-FA-SU-E2E-141-sub-tab-borrowed-assets-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-421 | E2E | TC-FA-SU-E2E-141-sub-tab-borrowed-assets-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-422 | E2E | TC-FA-SU-E2E-141-sub-tab-borrowed-assets-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-423 | E2E | TC-FA-SU-E2E-142-sub-tab-borrowed-assets-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-424 | E2E | TC-FA-SU-E2E-142-sub-tab-borrowed-assets-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-425 | E2E | TC-FA-SU-E2E-142-sub-tab-borrowed-assets-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-426 | E2E | TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-427 | E2E | TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-428 | E2E | TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-429 | E2E | TC-FA-SU-E2E-143-sub-tab-borrowed-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-430 | E2E | TC-FA-SU-E2E-144-sub-tab-borrowed-assets-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-431 | E2E | TC-FA-SU-E2E-144-sub-tab-borrowed-assets-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-432 | E2E | TC-FA-SU-E2E-148-sub-tab-borrowed-assets-setup-column-pin-dan-unpin | FE+BE. |
| TC-FA-SU-433 | E2E | TC-FA-SU-E2E-145-sub-tab-borrowed-assets-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-434 | E2E | TC-FA-SU-E2E-146-sub-tab-borrowed-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-435 | E2E | TC-FA-SU-E2E-147-sub-tab-borrowed-assets-download | FE+BE. |
| TC-FA-SU-436 | E2E | TC-FA-SU-E2E-147-sub-tab-borrowed-assets-download | FE+BE. |
| TC-FA-SU-437 | E2E | TC-FA-SU-E2E-370-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-438 | E2E | TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-439 | E2E | TC-FA-SU-E2E-146-sub-tab-borrowed-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-440 | E2E | TC-FA-SU-E2E-360-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-441 | E2E | TC-FA-SU-E2E-146-sub-tab-borrowed-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-442 | E2E | TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-443 | E2E | TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-444 | E2E | TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-445 | E2E | TC-FA-SU-E2E-150-sub-tab-assigned-assets-screening-dan-search | FE+BE. |
| TC-FA-SU-446 | E2E | TC-FA-SU-E2E-151-sub-tab-assigned-assets-search | FE+BE. |
| TC-FA-SU-447 | E2E | TC-FA-SU-E2E-151-sub-tab-assigned-assets-search | FE+BE. |
| TC-FA-SU-448 | E2E | TC-FA-SU-E2E-152-sub-tab-assigned-assets-sort | FE+BE. |
| TC-FA-SU-449 | E2E | TC-FA-SU-E2E-152-sub-tab-assigned-assets-sort | FE+BE. |
| TC-FA-SU-450 | E2E | TC-FA-SU-E2E-152-sub-tab-assigned-assets-sort | FE+BE. |
| TC-FA-SU-451 | E2E | TC-FA-SU-E2E-153-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-452 | E2E | TC-FA-SU-E2E-153-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-453 | E2E | TC-FA-SU-E2E-154-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-454 | E2E | TC-FA-SU-E2E-154-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-455 | E2E | TC-FA-SU-E2E-169-sub-tab-assigned-assets-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | FE+BE. |
| TC-FA-SU-456 | E2E | TC-FA-SU-E2E-155-sub-tab-assigned-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-457 | E2E | TC-FA-SU-E2E-155-sub-tab-assigned-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-458 | E2E | TC-FA-SU-E2E-155-sub-tab-assigned-assets-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-459 | E2E | TC-FA-SU-E2E-156-sub-tab-assigned-assets-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-460 | E2E | TC-FA-SU-E2E-156-sub-tab-assigned-assets-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-461 | E2E | TC-FA-SU-E2E-157-sub-tab-assigned-assets-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-462 | E2E | TC-FA-SU-E2E-157-sub-tab-assigned-assets-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-463 | E2E | TC-FA-SU-E2E-158-sub-tab-assigned-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-464 | E2E | TC-FA-SU-E2E-159-sub-tab-assigned-assets-download | FE+BE. |
| TC-FA-SU-465 | E2E | TC-FA-SU-E2E-159-sub-tab-assigned-assets-download | FE+BE. |
| TC-FA-SU-466 | E2E | TC-FA-SU-E2E-370-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-467 | E2E | TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-468 | E2E | TC-FA-SU-E2E-158-sub-tab-assigned-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-469 | E2E | TC-FA-SU-E2E-361-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-470 | E2E | TC-FA-SU-E2E-158-sub-tab-assigned-assets-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-471 | E2E | TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search | FE+BE. |
| TC-FA-SU-472 | E2E | TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search | FE+BE. |
| TC-FA-SU-473 | E2E | TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search | FE+BE. |
| TC-FA-SU-474 | E2E | TC-FA-SU-E2E-160-sub-tab-pending-approvals-screening-dan-search | FE+BE. |
| TC-FA-SU-475 | E2E | TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | FE+BE. |
| TC-FA-SU-476 | E2E | TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | FE+BE. |
| TC-FA-SU-477 | E2E | TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | FE+BE. |
| TC-FA-SU-478 | E2E | TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | FE+BE. |
| TC-FA-SU-479 | E2E | TC-FA-SU-E2E-161-sub-tab-pending-approvals-search-dan-sort | FE+BE. |
| TC-FA-SU-480 | E2E | TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-481 | E2E | TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-482 | E2E | TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-483 | E2E | TC-FA-SU-E2E-162-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-484 | E2E | TC-FA-SU-E2E-163-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-485 | E2E | TC-FA-SU-E2E-163-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-486 | E2E | TC-FA-SU-E2E-163-sub-tab-pending-approvals-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-487 | E2E | TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-488 | E2E | TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-489 | E2E | TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-490 | E2E | TC-FA-SU-E2E-164-sub-tab-pending-approvals-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-491 | E2E | TC-FA-SU-E2E-165-sub-tab-pending-approvals-setup-column | FE+BE. |
| TC-FA-SU-492 | E2E | TC-FA-SU-E2E-168-sub-tab-pending-approvals-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-493 | E2E | TC-FA-SU-E2E-165-sub-tab-pending-approvals-setup-column | FE+BE. |
| TC-FA-SU-494 | E2E | TC-FA-SU-E2E-166-sub-tab-pending-approvals-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-495 | E2E | TC-FA-SU-E2E-167-sub-tab-pending-approvals-download | FE+BE. |
| TC-FA-SU-496 | E2E | TC-FA-SU-E2E-167-sub-tab-pending-approvals-download | FE+BE. |
| TC-FA-SU-497 | E2E | TC-FA-SU-E2E-371-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-498 | E2E | TC-FA-SU-E2E-366-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-1 | FE+BE. |
| TC-FA-SU-499 | E2E | TC-FA-SU-E2E-166-sub-tab-pending-approvals-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-500 | E2E | TC-FA-SU-E2E-361-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-501 | E2E | TC-FA-SU-E2E-166-sub-tab-pending-approvals-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-502 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-503 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-504 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-505 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-506 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-507 | E2E | TC-FA-SU-E2E-170-sub-tab-pending-tasks-screening-dan-search | FE+BE. |
| TC-FA-SU-508 | E2E | TC-FA-SU-E2E-171-sub-tab-pending-tasks-search | FE+BE. |
| TC-FA-SU-509 | E2E | TC-FA-SU-E2E-171-sub-tab-pending-tasks-search | FE+BE. |
| TC-FA-SU-510 | E2E | TC-FA-SU-E2E-171-sub-tab-pending-tasks-search | FE+BE. |
| TC-FA-SU-511 | E2E | TC-FA-SU-E2E-172-sub-tab-pending-tasks-sort | FE+BE. |
| TC-FA-SU-512 | E2E | TC-FA-SU-E2E-172-sub-tab-pending-tasks-sort | FE+BE. |
| TC-FA-SU-513 | E2E | TC-FA-SU-E2E-172-sub-tab-pending-tasks-sort | FE+BE. |
| TC-FA-SU-514 | E2E | TC-FA-SU-E2E-173-sub-tab-pending-tasks-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-515 | E2E | TC-FA-SU-E2E-173-sub-tab-pending-tasks-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-516 | E2E | TC-FA-SU-E2E-173-sub-tab-pending-tasks-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-517 | E2E | TC-FA-SU-E2E-174-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-518 | E2E | TC-FA-SU-E2E-174-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-519 | E2E | TC-FA-SU-E2E-174-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-520 | E2E | TC-FA-SU-E2E-175-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-521 | E2E | TC-FA-SU-E2E-175-sub-tab-pending-tasks-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-522 | E2E | TC-FA-SU-E2E-192-sub-tab-pending-tasks-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | FE+BE. |
| TC-FA-SU-523 | E2E | TC-FA-SU-E2E-176-sub-tab-pending-tasks-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-524 | E2E | TC-FA-SU-E2E-176-sub-tab-pending-tasks-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-525 | E2E | TC-FA-SU-E2E-176-sub-tab-pending-tasks-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-526 | E2E | TC-FA-SU-E2E-177-sub-tab-pending-tasks-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-527 | E2E | TC-FA-SU-E2E-177-sub-tab-pending-tasks-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-528 | E2E | TC-FA-SU-E2E-178-sub-tab-pending-tasks-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-529 | E2E | TC-FA-SU-E2E-178-sub-tab-pending-tasks-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-530 | E2E | TC-FA-SU-E2E-179-sub-tab-pending-tasks-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-531 | E2E | TC-FA-SU-E2E-180-sub-tab-pending-tasks-download | FE+BE. |
| TC-FA-SU-532 | E2E | TC-FA-SU-E2E-180-sub-tab-pending-tasks-download | FE+BE. |
| TC-FA-SU-533 | E2E | TC-FA-SU-E2E-371-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-534 | E2E | TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-535 | E2E | TC-FA-SU-E2E-179-sub-tab-pending-tasks-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-536 | E2E | TC-FA-SU-E2E-361-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-537 | E2E | TC-FA-SU-E2E-179-sub-tab-pending-tasks-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-538 | E2E | TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search | FE+BE. |
| TC-FA-SU-539 | E2E | TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search | FE+BE. |
| TC-FA-SU-540 | E2E | TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search | FE+BE. |
| TC-FA-SU-541 | E2E | TC-FA-SU-E2E-181-tab-non-login-user-screening-dan-search | FE+BE. |
| TC-FA-SU-542 | E2E | TC-FA-SU-E2E-182-tab-non-login-user-search | FE+BE. |
| TC-FA-SU-543 | E2E | TC-FA-SU-E2E-182-tab-non-login-user-search | FE+BE. |
| TC-FA-SU-544 | E2E | TC-FA-SU-E2E-182-tab-non-login-user-search | FE+BE. |
| TC-FA-SU-545 | E2E | TC-FA-SU-E2E-183-tab-non-login-user-search-dan-sort | FE+BE. |
| TC-FA-SU-546 | E2E | TC-FA-SU-E2E-183-tab-non-login-user-search-dan-sort | FE+BE. |
| TC-FA-SU-547 | E2E | TC-FA-SU-E2E-184-tab-non-login-user-sort | FE+BE. |
| TC-FA-SU-548 | E2E | TC-FA-SU-E2E-184-tab-non-login-user-sort | FE+BE. |
| TC-FA-SU-549 | E2E | TC-FA-SU-E2E-184-tab-non-login-user-sort | FE+BE. |
| TC-FA-SU-550 | E2E | TC-FA-SU-E2E-184-tab-non-login-user-sort | FE+BE. |
| TC-FA-SU-551 | E2E | TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-552 | E2E | TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-553 | E2E | TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-554 | E2E | TC-FA-SU-E2E-185-tab-non-login-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-555 | E2E | TC-FA-SU-E2E-186-tab-non-login-user-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-556 | E2E | TC-FA-SU-E2E-186-tab-non-login-user-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-557 | E2E | TC-FA-SU-E2E-193-tab-non-login-user-perilaku-filter-panel-tutup-tanpa-apply-indikator-titik-dan-nilai-kosong | FE+BE. |
| TC-FA-SU-558 | E2E | TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-559 | E2E | TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-560 | E2E | TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-561 | E2E | TC-FA-SU-E2E-188-tab-non-login-user-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-562 | E2E | TC-FA-SU-E2E-188-tab-non-login-user-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-563 | E2E | TC-FA-SU-E2E-189-tab-non-login-user-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-564 | E2E | TC-FA-SU-E2E-189-tab-non-login-user-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-565 | E2E | TC-FA-SU-E2E-189-tab-non-login-user-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-566 | E2E | TC-FA-SU-E2E-190-tab-non-login-user-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-567 | E2E | TC-FA-SU-E2E-190-tab-non-login-user-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-568 | E2E | TC-FA-SU-E2E-190-tab-non-login-user-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-569 | E2E | TC-FA-SU-E2E-191-tab-non-login-user-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-570 | E2E | TC-FA-SU-E2E-191-tab-non-login-user-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-571 | E2E | TC-FA-SU-E2E-371-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-572 | E2E | TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-573 | E2E | TC-FA-SU-E2E-191-tab-non-login-user-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-574 | E2E | TC-FA-SU-E2E-362-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-575 | E2E | TC-FA-SU-E2E-194-tab-changelog-screening-dan-search | FE+BE. |
| TC-FA-SU-576 | E2E | TC-FA-SU-E2E-194-tab-changelog-screening-dan-search | FE+BE. |
| TC-FA-SU-577 | E2E | TC-FA-SU-E2E-194-tab-changelog-screening-dan-search | FE+BE. |
| TC-FA-SU-578 | E2E | TC-FA-SU-E2E-194-tab-changelog-screening-dan-search | FE+BE. |
| TC-FA-SU-579 | E2E | TC-FA-SU-E2E-195-tab-changelog-search-dan-sort | FE+BE. |
| TC-FA-SU-580 | E2E | TC-FA-SU-E2E-195-tab-changelog-search-dan-sort | FE+BE. |
| TC-FA-SU-581 | E2E | TC-FA-SU-E2E-195-tab-changelog-search-dan-sort | FE+BE. |
| TC-FA-SU-582 | E2E | TC-FA-SU-E2E-195-tab-changelog-search-dan-sort | FE+BE. |
| TC-FA-SU-583 | E2E | TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-584 | E2E | TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-585 | E2E | TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-586 | E2E | TC-FA-SU-E2E-196-tab-changelog-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-587 | E2E | TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-588 | E2E | TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-589 | E2E | TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-590 | E2E | TC-FA-SU-E2E-197-tab-changelog-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-591 | E2E | TC-FA-SU-E2E-198-tab-changelog-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-592 | E2E | TC-FA-SU-E2E-198-tab-changelog-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-593 | E2E | TC-FA-SU-E2E-198-tab-changelog-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-594 | E2E | TC-FA-SU-E2E-199-tab-changelog-setup-column | FE+BE. |
| TC-FA-SU-595 | E2E | TC-FA-SU-E2E-199-tab-changelog-setup-column | FE+BE. |
| TC-FA-SU-596 | E2E | TC-FA-SU-E2E-199-tab-changelog-setup-column | FE+BE. |
| TC-FA-SU-597 | E2E | TC-FA-SU-E2E-199-tab-changelog-setup-column | FE+BE. |
| TC-FA-SU-598 | E2E | TC-FA-SU-E2E-212-tab-changelog-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-599 | E2E | TC-FA-SU-E2E-200-tab-changelog-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-600 | E2E | TC-FA-SU-E2E-200-tab-changelog-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-601 | E2E | TC-FA-SU-E2E-201-tab-changelog-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-602 | E2E | TC-FA-SU-E2E-201-tab-changelog-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-603 | E2E | TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-604 | E2E | TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-605 | E2E | TC-FA-SU-E2E-201-tab-changelog-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-606 | E2E | TC-FA-SU-E2E-362-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-607 | E2E | TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search | FE+BE. |
| TC-FA-SU-608 | E2E | TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search | FE+BE. |
| TC-FA-SU-609 | E2E | TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search | FE+BE. |
| TC-FA-SU-610 | E2E | TC-FA-SU-E2E-202-modal-changelog-user-global-role-screening-dan-search | FE+BE. |
| TC-FA-SU-611 | E2E | TC-FA-SU-E2E-203-modal-changelog-user-global-role-search | FE+BE. |
| TC-FA-SU-612 | E2E | TC-FA-SU-E2E-203-modal-changelog-user-global-role-search | FE+BE. |
| TC-FA-SU-613 | E2E | TC-FA-SU-E2E-204-modal-changelog-user-global-role-search-dan-sort | FE+BE. |
| TC-FA-SU-614 | E2E | TC-FA-SU-E2E-204-modal-changelog-user-global-role-search-dan-sort | FE+BE. |
| TC-FA-SU-615 | E2E | TC-FA-SU-E2E-204-modal-changelog-user-global-role-search-dan-sort | FE+BE. |
| TC-FA-SU-616 | E2E | TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-617 | E2E | TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-618 | E2E | TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-619 | E2E | TC-FA-SU-E2E-205-modal-changelog-user-global-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-620 | E2E | TC-FA-SU-E2E-206-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-621 | E2E | TC-FA-SU-E2E-206-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-622 | E2E | TC-FA-SU-E2E-206-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-623 | E2E | TC-FA-SU-E2E-207-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-624 | E2E | TC-FA-SU-E2E-207-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-625 | E2E | TC-FA-SU-E2E-207-modal-changelog-user-global-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-626 | E2E | TC-FA-SU-E2E-208-modal-changelog-user-global-role-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-627 | E2E | TC-FA-SU-E2E-208-modal-changelog-user-global-role-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-628 | E2E | TC-FA-SU-E2E-208-modal-changelog-user-global-role-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-629 | E2E | TC-FA-SU-E2E-209-modal-changelog-user-global-role-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-630 | E2E | TC-FA-SU-E2E-213-modal-changelog-user-global-role-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-631 | E2E | TC-FA-SU-E2E-210-modal-changelog-user-global-role-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-632 | E2E | TC-FA-SU-E2E-210-modal-changelog-user-global-role-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-633 | E2E | TC-FA-SU-E2E-211-modal-changelog-user-global-role-download | FE+BE. |
| TC-FA-SU-634 | E2E | TC-FA-SU-E2E-211-modal-changelog-user-global-role-download | FE+BE. |
| TC-FA-SU-635 | E2E | TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-636 | E2E | TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-637 | E2E | TC-FA-SU-E2E-210-modal-changelog-user-global-role-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-638 | E2E | TC-FA-SU-E2E-376-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-8 | FE+BE. |
| TC-FA-SU-639 | E2E | TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search | FE+BE. |
| TC-FA-SU-640 | E2E | TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search | FE+BE. |
| TC-FA-SU-641 | E2E | TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search | FE+BE. |
| TC-FA-SU-642 | E2E | TC-FA-SU-E2E-214-modal-changelog-user-group-role-screening-dan-search | FE+BE. |
| TC-FA-SU-643 | E2E | TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort | FE+BE. |
| TC-FA-SU-644 | E2E | TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort | FE+BE. |
| TC-FA-SU-645 | E2E | TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort | FE+BE. |
| TC-FA-SU-646 | E2E | TC-FA-SU-E2E-215-modal-changelog-user-group-role-search-dan-sort | FE+BE. |
| TC-FA-SU-647 | E2E | TC-FA-SU-E2E-216-modal-changelog-user-group-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-648 | E2E | TC-FA-SU-E2E-216-modal-changelog-user-group-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-649 | E2E | TC-FA-SU-E2E-216-modal-changelog-user-group-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-650 | E2E | TC-FA-SU-E2E-216-modal-changelog-user-group-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-651 | E2E | TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-652 | E2E | TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-653 | E2E | TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-654 | E2E | TC-FA-SU-E2E-217-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-655 | E2E | TC-FA-SU-E2E-218-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-656 | E2E | TC-FA-SU-E2E-218-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-657 | E2E | TC-FA-SU-E2E-218-modal-changelog-user-group-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-658 | E2E | TC-FA-SU-E2E-219-modal-changelog-user-group-role-setup-column | FE+BE. |
| TC-FA-SU-659 | E2E | TC-FA-SU-E2E-219-modal-changelog-user-group-role-setup-column | FE+BE. |
| TC-FA-SU-660 | E2E | TC-FA-SU-E2E-219-modal-changelog-user-group-role-setup-column | FE+BE. |
| TC-FA-SU-661 | E2E | TC-FA-SU-E2E-219-modal-changelog-user-group-role-setup-column | FE+BE. |
| TC-FA-SU-662 | E2E | TC-FA-SU-E2E-230-modal-changelog-user-group-role-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-663 | E2E | TC-FA-SU-E2E-220-modal-changelog-user-group-role-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-664 | E2E | TC-FA-SU-E2E-220-modal-changelog-user-group-role-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-665 | E2E | TC-FA-SU-E2E-221-modal-changelog-user-group-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-666 | E2E | TC-FA-SU-E2E-221-modal-changelog-user-group-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-667 | E2E | TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-668 | E2E | TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-669 | E2E | TC-FA-SU-E2E-221-modal-changelog-user-group-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-670 | E2E | TC-FA-SU-E2E-363-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-671 | E2E | TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-672 | E2E | TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-673 | E2E | TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-674 | E2E | TC-FA-SU-E2E-222-modal-changelog-user-transaction-role-screening-dan-search | FE+BE. |
| TC-FA-SU-675 | E2E | TC-FA-SU-E2E-223-modal-changelog-user-transaction-role-search-dan-sort | FE+BE. |
| TC-FA-SU-676 | E2E | TC-FA-SU-E2E-223-modal-changelog-user-transaction-role-search-dan-sort | FE+BE. |
| TC-FA-SU-677 | E2E | TC-FA-SU-E2E-223-modal-changelog-user-transaction-role-search-dan-sort | FE+BE. |
| TC-FA-SU-678 | E2E | TC-FA-SU-E2E-223-modal-changelog-user-transaction-role-search-dan-sort | FE+BE. |
| TC-FA-SU-679 | E2E | TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-680 | E2E | TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-681 | E2E | TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-682 | E2E | TC-FA-SU-E2E-224-modal-changelog-user-transaction-role-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-683 | E2E | TC-FA-SU-E2E-225-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-684 | E2E | TC-FA-SU-E2E-225-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-685 | E2E | TC-FA-SU-E2E-225-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-686 | E2E | TC-FA-SU-E2E-225-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-687 | E2E | TC-FA-SU-E2E-226-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-688 | E2E | TC-FA-SU-E2E-226-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-689 | E2E | TC-FA-SU-E2E-226-modal-changelog-user-transaction-role-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-690 | E2E | TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-691 | E2E | TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-692 | E2E | TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-693 | E2E | TC-FA-SU-E2E-227-modal-changelog-user-transaction-role-setup-column | FE+BE. |
| TC-FA-SU-694 | E2E | TC-FA-SU-E2E-231-modal-changelog-user-transaction-role-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-695 | E2E | TC-FA-SU-E2E-228-modal-changelog-user-transaction-role-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-696 | E2E | TC-FA-SU-E2E-228-modal-changelog-user-transaction-role-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-697 | E2E | TC-FA-SU-E2E-229-modal-changelog-user-transaction-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-698 | E2E | TC-FA-SU-E2E-229-modal-changelog-user-transaction-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-699 | E2E | TC-FA-SU-E2E-372-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-700 | E2E | TC-FA-SU-E2E-367-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-2 | FE+BE. |
| TC-FA-SU-701 | E2E | TC-FA-SU-E2E-229-modal-changelog-user-transaction-role-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-702 | E2E | TC-FA-SU-E2E-363-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-703 | E2E | TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search | FE+BE. |
| TC-FA-SU-704 | E2E | TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search | FE+BE. |
| TC-FA-SU-705 | E2E | TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search | FE+BE. |
| TC-FA-SU-706 | E2E | TC-FA-SU-E2E-232-modal-combined-changelog-user-screening-dan-search | FE+BE. |
| TC-FA-SU-707 | E2E | TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort | FE+BE. |
| TC-FA-SU-708 | E2E | TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort | FE+BE. |
| TC-FA-SU-709 | E2E | TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort | FE+BE. |
| TC-FA-SU-710 | E2E | TC-FA-SU-E2E-233-modal-combined-changelog-user-search-dan-sort | FE+BE. |
| TC-FA-SU-711 | E2E | TC-FA-SU-E2E-234-modal-combined-changelog-user-sort | FE+BE. |
| TC-FA-SU-712 | E2E | TC-FA-SU-E2E-234-modal-combined-changelog-user-sort | FE+BE. |
| TC-FA-SU-713 | E2E | TC-FA-SU-E2E-234-modal-combined-changelog-user-sort | FE+BE. |
| TC-FA-SU-714 | E2E | TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-715 | E2E | TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-716 | E2E | TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-717 | E2E | TC-FA-SU-E2E-235-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-718 | E2E | TC-FA-SU-E2E-236-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-719 | E2E | TC-FA-SU-E2E-236-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-720 | E2E | TC-FA-SU-E2E-236-modal-combined-changelog-user-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-721 | E2E | TC-FA-SU-E2E-237-modal-combined-changelog-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-722 | E2E | TC-FA-SU-E2E-237-modal-combined-changelog-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-723 | E2E | TC-FA-SU-E2E-237-modal-combined-changelog-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-724 | E2E | TC-FA-SU-E2E-238-modal-combined-changelog-user-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-725 | E2E | TC-FA-SU-E2E-239-modal-combined-changelog-user-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-726 | E2E | TC-FA-SU-E2E-252-modal-combined-changelog-user-setup-column-pin-dan-unpin | FE+BE. |
| TC-FA-SU-727 | E2E | TC-FA-SU-E2E-239-modal-combined-changelog-user-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-728 | E2E | TC-FA-SU-E2E-240-modal-combined-changelog-user-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-729 | E2E | TC-FA-SU-E2E-240-modal-combined-changelog-user-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-730 | E2E | TC-FA-SU-E2E-241-modal-combined-changelog-user-download | FE+BE. |
| TC-FA-SU-731 | E2E | TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-732 | E2E | TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-733 | E2E | TC-FA-SU-E2E-240-modal-combined-changelog-user-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-734 | E2E | TC-FA-SU-E2E-375-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-7 | FE+BE. |
| TC-FA-SU-735 | E2E | TC-FA-SU-E2E-242-tab-system-log-screening-dan-search | FE+BE. |
| TC-FA-SU-736 | E2E | TC-FA-SU-E2E-242-tab-system-log-screening-dan-search | FE+BE. |
| TC-FA-SU-737 | E2E | TC-FA-SU-E2E-242-tab-system-log-screening-dan-search | FE+BE. |
| TC-FA-SU-738 | E2E | TC-FA-SU-E2E-243-tab-system-log-search-dan-sort | FE+BE. |
| TC-FA-SU-739 | E2E | TC-FA-SU-E2E-243-tab-system-log-search-dan-sort | FE+BE. |
| TC-FA-SU-740 | E2E | TC-FA-SU-E2E-243-tab-system-log-search-dan-sort | FE+BE. |
| TC-FA-SU-741 | E2E | TC-FA-SU-E2E-243-tab-system-log-search-dan-sort | FE+BE. |
| TC-FA-SU-742 | E2E | TC-FA-SU-E2E-244-tab-system-log-sort | FE+BE. |
| TC-FA-SU-743 | E2E | TC-FA-SU-E2E-244-tab-system-log-sort | FE+BE. |
| TC-FA-SU-744 | E2E | TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-745 | E2E | TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-746 | E2E | TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-747 | E2E | TC-FA-SU-E2E-245-tab-system-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-748 | E2E | TC-FA-SU-E2E-246-tab-system-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-749 | E2E | TC-FA-SU-E2E-246-tab-system-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-750 | E2E | TC-FA-SU-E2E-246-tab-system-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-751 | E2E | TC-FA-SU-E2E-247-tab-system-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-752 | E2E | TC-FA-SU-E2E-247-tab-system-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-753 | E2E | TC-FA-SU-E2E-247-tab-system-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-754 | E2E | TC-FA-SU-E2E-248-tab-system-log-setup-column-bagian-1 | FE+BE. |
| TC-FA-SU-755 | E2E | TC-FA-SU-E2E-249-tab-system-log-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-756 | E2E | TC-FA-SU-E2E-253-tab-system-log-setup-column-pin-dan-unpin | FE+BE. |
| TC-FA-SU-757 | E2E | TC-FA-SU-E2E-249-tab-system-log-setup-column-bagian-2 | FE+BE. |
| TC-FA-SU-758 | E2E | TC-FA-SU-E2E-250-tab-system-log-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-759 | E2E | TC-FA-SU-E2E-250-tab-system-log-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-760 | E2E | TC-FA-SU-E2E-251-tab-system-log-download | FE+BE. |
| TC-FA-SU-761 | E2E | TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-762 | E2E | TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-763 | E2E | TC-FA-SU-E2E-250-tab-system-log-pagination-tooltip-icon-dan-download | FE+BE. |
| TC-FA-SU-764 | E2E | TC-FA-SU-E2E-364-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-5 | FE+BE. |
| TC-FA-SU-765 | E2E | TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search | FE+BE. |
| TC-FA-SU-766 | E2E | TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search | FE+BE. |
| TC-FA-SU-767 | E2E | TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search | FE+BE. |
| TC-FA-SU-768 | E2E | TC-FA-SU-E2E-254-tab-transaction-admin-log-screening-dan-search | FE+BE. |
| TC-FA-SU-769 | E2E | TC-FA-SU-E2E-255-tab-transaction-admin-log-search | FE+BE. |
| TC-FA-SU-770 | E2E | TC-FA-SU-E2E-255-tab-transaction-admin-log-search | FE+BE. |
| TC-FA-SU-771 | E2E | TC-FA-SU-E2E-255-tab-transaction-admin-log-search | FE+BE. |
| TC-FA-SU-772 | E2E | TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-773 | E2E | TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-774 | E2E | TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-775 | E2E | TC-FA-SU-E2E-256-tab-transaction-admin-log-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-776 | E2E | TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-777 | E2E | TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-778 | E2E | TC-FA-SU-E2E-257-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-1 | FE+BE. |
| TC-FA-SU-779 | E2E | TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-780 | E2E | TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-781 | E2E | TC-FA-SU-E2E-258-tab-transaction-admin-log-filter-dan-kontrol-filter-bagian-2 | FE+BE. |
| TC-FA-SU-782 | E2E | TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-783 | E2E | TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-784 | E2E | TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-785 | E2E | TC-FA-SU-E2E-259-tab-transaction-admin-log-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-786 | E2E | TC-FA-SU-E2E-260-tab-transaction-admin-log-setup-column | FE+BE. |
| TC-FA-SU-787 | E2E | TC-FA-SU-E2E-275-tab-transaction-admin-log-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-788 | E2E | TC-FA-SU-E2E-260-tab-transaction-admin-log-setup-column | FE+BE. |
| TC-FA-SU-789 | E2E | TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-790 | E2E | TC-FA-SU-E2E-262-tab-transaction-admin-log-download-dan-struktur-sub-tab | FE+BE. |
| TC-FA-SU-791 | E2E | TC-FA-SU-E2E-262-tab-transaction-admin-log-download-dan-struktur-sub-tab | FE+BE. |
| TC-FA-SU-792 | E2E | TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-793 | E2E | TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-794 | E2E | TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-795 | E2E | TC-FA-SU-E2E-364-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-5 | FE+BE. |
| TC-FA-SU-796 | E2E | TC-FA-SU-E2E-261-tab-transaction-admin-log-pagination-tooltip-icon-dan-state-per-sub-tab | FE+BE. |
| TC-FA-SU-797 | E2E | TC-FA-SU-E2E-262-tab-transaction-admin-log-download-dan-struktur-sub-tab | FE+BE. |
| TC-FA-SU-798 | E2E | TC-FA-SU-E2E-263-tab-transaction-admin-log-struktur-sub-tab-bagian-1 | FE+BE. |
| TC-FA-SU-799 | E2E | TC-FA-SU-E2E-263-tab-transaction-admin-log-struktur-sub-tab-bagian-1 | FE+BE. |
| TC-FA-SU-800 | E2E | TC-FA-SU-E2E-264-tab-transaction-admin-log-struktur-sub-tab-bagian-2 | FE+BE. |
| TC-FA-SU-801 | E2E | TC-FA-SU-E2E-264-tab-transaction-admin-log-struktur-sub-tab-bagian-2 | FE+BE. |
| TC-FA-SU-802 | E2E | TC-FA-SU-E2E-265-tab-transaction-admin-log-struktur-sub-tab-bagian-3 | FE+BE. |
| TC-FA-SU-803 | E2E | TC-FA-SU-E2E-265-tab-transaction-admin-log-struktur-sub-tab-bagian-3 | FE+BE. |
| TC-FA-SU-804 | E2E | TC-FA-SU-E2E-266-tab-transaction-admin-log-struktur-sub-tab-bagian-4 | FE+BE. |
| TC-FA-SU-805 | E2E | TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search | FE+BE. |
| TC-FA-SU-806 | E2E | TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search | FE+BE. |
| TC-FA-SU-807 | E2E | TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search | FE+BE. |
| TC-FA-SU-808 | E2E | TC-FA-SU-E2E-267-tab-user-log-sub-tab-borrow-screening-dan-search | FE+BE. |
| TC-FA-SU-809 | E2E | TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort | FE+BE. |
| TC-FA-SU-810 | E2E | TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort | FE+BE. |
| TC-FA-SU-811 | E2E | TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort | FE+BE. |
| TC-FA-SU-812 | E2E | TC-FA-SU-E2E-268-tab-user-log-sub-tab-borrow-search-dan-sort | FE+BE. |
| TC-FA-SU-813 | E2E | TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-814 | E2E | TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-815 | E2E | TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-816 | E2E | TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-817 | E2E | TC-FA-SU-E2E-269-tab-user-log-sub-tab-borrow-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-818 | E2E | TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-819 | E2E | TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-820 | E2E | TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-821 | E2E | TC-FA-SU-E2E-270-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-822 | E2E | TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-823 | E2E | TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-824 | E2E | TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-825 | E2E | TC-FA-SU-E2E-271-tab-user-log-sub-tab-borrow-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-826 | E2E | TC-FA-SU-E2E-272-tab-user-log-sub-tab-borrow-setup-column | FE+BE. |
| TC-FA-SU-827 | E2E | TC-FA-SU-E2E-272-tab-user-log-sub-tab-borrow-setup-column | FE+BE. |
| TC-FA-SU-828 | E2E | TC-FA-SU-E2E-276-tab-user-log-sub-tab-borrow-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-829 | E2E | TC-FA-SU-E2E-273-tab-user-log-sub-tab-borrow-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-830 | E2E | TC-FA-SU-E2E-273-tab-user-log-sub-tab-borrow-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-831 | E2E | TC-FA-SU-E2E-274-tab-user-log-sub-tab-borrow-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-832 | E2E | TC-FA-SU-E2E-274-tab-user-log-sub-tab-borrow-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-833 | E2E | TC-FA-SU-E2E-373-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-834 | E2E | TC-FA-SU-E2E-368-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-3 | FE+BE. |
| TC-FA-SU-835 | E2E | TC-FA-SU-E2E-273-tab-user-log-sub-tab-borrow-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-836 | E2E | TC-FA-SU-E2E-376-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-8 | FE+BE. |
| TC-FA-SU-837 | E2E | TC-FA-SU-E2E-274-tab-user-log-sub-tab-borrow-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-838 | E2E | TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search | FE+BE. |
| TC-FA-SU-839 | E2E | TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search | FE+BE. |
| TC-FA-SU-840 | E2E | TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search | FE+BE. |
| TC-FA-SU-841 | E2E | TC-FA-SU-E2E-277-tab-user-log-sub-tab-assignment-screening-dan-search | FE+BE. |
| TC-FA-SU-842 | E2E | TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort | FE+BE. |
| TC-FA-SU-843 | E2E | TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort | FE+BE. |
| TC-FA-SU-844 | E2E | TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort | FE+BE. |
| TC-FA-SU-845 | E2E | TC-FA-SU-E2E-278-tab-user-log-sub-tab-assignment-search-dan-sort | FE+BE. |
| TC-FA-SU-846 | E2E | TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-847 | E2E | TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-848 | E2E | TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-849 | E2E | TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-850 | E2E | TC-FA-SU-E2E-279-tab-user-log-sub-tab-assignment-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-851 | E2E | TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-852 | E2E | TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-853 | E2E | TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-854 | E2E | TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-855 | E2E | TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-856 | E2E | TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-857 | E2E | TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-858 | E2E | TC-FA-SU-E2E-281-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-859 | E2E | TC-FA-SU-E2E-282-tab-user-log-sub-tab-assignment-setup-column | FE+BE. |
| TC-FA-SU-860 | E2E | TC-FA-SU-E2E-282-tab-user-log-sub-tab-assignment-setup-column | FE+BE. |
| TC-FA-SU-861 | E2E | TC-FA-SU-E2E-293-tab-user-log-sub-tab-assignment-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-862 | E2E | TC-FA-SU-E2E-283-tab-user-log-sub-tab-assignment-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-863 | E2E | TC-FA-SU-E2E-283-tab-user-log-sub-tab-assignment-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-864 | E2E | TC-FA-SU-E2E-284-tab-user-log-sub-tab-assignment-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-865 | E2E | TC-FA-SU-E2E-284-tab-user-log-sub-tab-assignment-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-866 | E2E | TC-FA-SU-E2E-374-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-5 | FE+BE. |
| TC-FA-SU-867 | E2E | TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-868 | E2E | TC-FA-SU-E2E-283-tab-user-log-sub-tab-assignment-setup-column-pagination-dan-tooltip-icon | FE+BE. |
| TC-FA-SU-869 | E2E | TC-FA-SU-E2E-365-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-6 | FE+BE. |
| TC-FA-SU-870 | E2E | TC-FA-SU-E2E-284-tab-user-log-sub-tab-assignment-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-871 | E2E | TC-FA-SU-E2E-285-tab-user-log-sub-tab-session-screening-dan-search | FE+BE. |
| TC-FA-SU-872 | E2E | TC-FA-SU-E2E-285-tab-user-log-sub-tab-session-screening-dan-search | FE+BE. |
| TC-FA-SU-873 | E2E | TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort | FE+BE. |
| TC-FA-SU-874 | E2E | TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort | FE+BE. |
| TC-FA-SU-875 | E2E | TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort | FE+BE. |
| TC-FA-SU-876 | E2E | TC-FA-SU-E2E-286-tab-user-log-sub-tab-session-search-dan-sort | FE+BE. |
| TC-FA-SU-877 | E2E | TC-FA-SU-E2E-287-tab-user-log-sub-tab-session-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-878 | E2E | TC-FA-SU-E2E-287-tab-user-log-sub-tab-session-sort-dan-filter-dan-kontrol-filter | FE+BE. |
| TC-FA-SU-879 | E2E | TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-880 | E2E | TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-881 | E2E | TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-882 | E2E | TC-FA-SU-E2E-288-tab-user-log-sub-tab-session-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-883 | E2E | TC-FA-SU-E2E-289-tab-user-log-sub-tab-session-setup-column | FE+BE. |
| TC-FA-SU-884 | E2E | TC-FA-SU-E2E-289-tab-user-log-sub-tab-session-setup-column | FE+BE. |
| TC-FA-SU-885 | E2E | TC-FA-SU-E2E-294-tab-user-log-sub-tab-session-pin-dan-unpin-setup-column | FE+BE. |
| TC-FA-SU-886 | E2E | TC-FA-SU-E2E-290-tab-user-log-sub-tab-session-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-887 | E2E | TC-FA-SU-E2E-290-tab-user-log-sub-tab-session-setup-column-dan-pagination | FE+BE. |
| TC-FA-SU-888 | E2E | TC-FA-SU-E2E-291-tab-user-log-sub-tab-session-tooltip-icon-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-889 | E2E | TC-FA-SU-E2E-292-tab-user-log-sub-tab-session-download | FE+BE. |
| TC-FA-SU-890 | E2E | TC-FA-SU-E2E-374-isi-berkas-download-transformasi-data-per-tipe-kolom-per-surface-tabel-bagian-5 | FE+BE. |
| TC-FA-SU-891 | E2E | TC-FA-SU-E2E-369-resilience-download-gagal-toast-error-tanpa-ekstensi-per-surface-tabel-bagian-4 | FE+BE. |
| TC-FA-SU-892 | E2E | TC-FA-SU-E2E-291-tab-user-log-sub-tab-session-tooltip-icon-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-893 | E2E | TC-FA-SU-E2E-365-resilience-baca-empty-state-loading-dan-error-load-surface-tabel-bagian-6 | FE+BE. |
| TC-FA-SU-894 | E2E | TC-FA-SU-E2E-291-tab-user-log-sub-tab-session-tooltip-icon-state-per-sub-tab-dan-download | FE+BE. |
| TC-FA-SU-895 | E2E | TC-FA-SU-E2E-099-popup-assign-group-role-kolom-crud-dinamis-setup-column-dan-search | FE+BE. |
| TC-FA-SU-896 | E2E | TC-FA-SU-E2E-099-popup-assign-group-role-kolom-crud-dinamis-setup-column-dan-search | FE+BE. |
| TC-FA-SU-897 | E2E | TC-FA-SU-E2E-099-popup-assign-group-role-kolom-crud-dinamis-setup-column-dan-search | FE+BE. |
| TC-FA-SU-898 | E2E | TC-FA-SU-E2E-100-popup-select-group-screening-node-ter-assign-disabled-dan-search | FE+BE. |
| TC-FA-SU-899 | E2E | TC-FA-SU-E2E-100-popup-select-group-screening-node-ter-assign-disabled-dan-search | FE+BE. |
| TC-FA-SU-900 | E2E | TC-FA-SU-E2E-100-popup-select-group-screening-node-ter-assign-disabled-dan-search | FE+BE. |
| TC-FA-SU-901 | E2E | TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download | FE+BE. |
| TC-FA-SU-902 | E2E | TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download | FE+BE. |
| TC-FA-SU-903 | E2E | TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download | FE+BE. |
| TC-FA-SU-904 | E2E | TC-FA-SU-E2E-104-resilience-download-detail-group-assignment-gagal | FE+BE. |
| TC-FA-SU-905 | E2E | TC-FA-SU-E2E-102-popup-select-home-group-role-count-dan-popup-tree-group-search-dan-restriksi-node | FE+BE. |
| TC-FA-SU-906 | E2E | TC-FA-SU-E2E-102-popup-select-home-group-role-count-dan-popup-tree-group-search-dan-restriksi-node | FE+BE. |
| TC-FA-SU-907 | E2E | TC-FA-SU-E2E-102-popup-select-home-group-role-count-dan-popup-tree-group-search-dan-restriksi-node | FE+BE. |
| TC-FA-SU-908 | E2E | TC-FA-SU-E2E-103-popup-select-home-group-bulk-dan-aksesibilitas-popup-select-home-group | FE+BE. |
| TC-FA-SU-909 | E2E | TC-FA-SU-E2E-295-log-activate-deactivate-dan-resend-activation-email-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-910 | E2E | TC-FA-SU-E2E-295-log-activate-deactivate-dan-resend-activation-email-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-911 | E2E | TC-FA-SU-E2E-295-log-activate-deactivate-dan-resend-activation-email-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-912 | E2E | TC-FA-SU-E2E-296-log-resend-confirmation-email-dan-edit-home-group-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-913 | E2E | TC-FA-SU-E2E-296-log-resend-confirmation-email-dan-edit-home-group-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-914 | E2E | TC-FA-SU-E2E-296-log-resend-confirmation-email-dan-edit-home-group-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-915 | E2E | TC-FA-SU-E2E-297-log-assign-remove-dan-edit-global-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-916 | E2E | TC-FA-SU-E2E-297-log-assign-remove-dan-edit-global-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-917 | E2E | TC-FA-SU-E2E-297-log-assign-remove-dan-edit-global-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-918 | E2E | TC-FA-SU-E2E-298-log-assign-edit-dan-remove-group-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-919 | E2E | TC-FA-SU-E2E-298-log-assign-edit-dan-remove-group-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-920 | E2E | TC-FA-SU-E2E-298-log-assign-edit-dan-remove-group-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-921 | E2E | TC-FA-SU-E2E-299-log-assign-remove-dan-penggantian-transaction-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-922 | E2E | TC-FA-SU-E2E-299-log-assign-remove-dan-penggantian-transaction-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-923 | E2E | TC-FA-SU-E2E-299-log-assign-remove-dan-penggantian-transaction-role-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-924 | E2E | TC-FA-SU-E2E-300-log-auto-revert-total-control-read-only-dan-group-manager-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-925 | E2E | TC-FA-SU-E2E-300-log-auto-revert-total-control-read-only-dan-group-manager-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-926 | E2E | TC-FA-SU-E2E-300-log-auto-revert-total-control-read-only-dan-group-manager-pada-tiga-surface-log | FE+BE. |
| TC-FA-SU-927 | E2E | TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group | FE+BE. |
| TC-FA-SU-928 | E2E | TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group | FE+BE. |
| TC-FA-SU-929 | E2E | TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group | FE+BE. |
| TC-FA-SU-930 | E2E | TC-FA-SU-E2E-301-entri-lintas-modul-cascade-tier-dan-log-delete-group | FE+BE. |
| TC-FA-SU-931 | E2E | TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk | FE+BE. |
| TC-FA-SU-932 | E2E | TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk | FE+BE. |
| TC-FA-SU-933 | E2E | TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk | FE+BE. |
| TC-FA-SU-934 | E2E | TC-FA-SU-E2E-302-creator-auto-assign-home-group-di-null-zero-delta-dan-log-per-pengguna-pada-aksi-bulk | FE+BE. |
| TC-FA-SU-935 | E2E | TC-FA-SU-E2E-303-notifikasi-auto-revert-struktur-kolom-tiga-surface-log-dan-object-action-pendek | FE+BE. |
| TC-FA-SU-936 | E2E | TC-FA-SU-E2E-303-notifikasi-auto-revert-struktur-kolom-tiga-surface-log-dan-object-action-pendek | FE+BE. |
| TC-FA-SU-937 | E2E | TC-FA-SU-E2E-303-notifikasi-auto-revert-struktur-kolom-tiga-surface-log-dan-object-action-pendek | FE+BE. |
| TC-FA-SU-938 | E2E | TC-FA-SU-E2E-304-log-tanpa-peristiwa-pembuatan-atau-penghapusan-dan-snapshot-immutable | FE+BE. |
| TC-FA-SU-939 | E2E | TC-FA-SU-E2E-304-log-tanpa-peristiwa-pembuatan-atau-penghapusan-dan-snapshot-immutable | FE+BE. |
| TC-FA-SU-940 | E2E | TC-FA-SU-E2E-313-log-disaring-scope-aktor-ber-scope-grup-pada-modal-combined-changelog | FE+BE. |
| TC-FA-SU-941 | E2E | TC-FA-SU-E2E-305-app-access-global-settings-pemberian-pencabutan-dan-pemberian-ulang | FE+BE. |
| TC-FA-SU-942 | E2E | TC-FA-SU-E2E-305-app-access-global-settings-pemberian-pencabutan-dan-pemberian-ulang | FE+BE. |
| TC-FA-SU-943 | E2E | TC-FA-SU-E2E-305-app-access-global-settings-pemberian-pencabutan-dan-pemberian-ulang | FE+BE. |
| TC-FA-SU-944 | E2E | TC-FA-SU-E2E-306-penghapusan-identitas-permanen-dan-perubahan-identitas-di-global-settings | FE+BE. |
| TC-FA-SU-945 | E2E | TC-FA-SU-E2E-306-penghapusan-identitas-permanen-dan-perubahan-identitas-di-global-settings | FE+BE. |
| TC-FA-SU-946 | E2E | TC-FA-SU-E2E-307-email-pending-dan-pengguna-nonaktif-di-global-settings | FE+BE. |
| TC-FA-SU-947 | E2E | TC-FA-SU-E2E-307-email-pending-dan-pengguna-nonaktif-di-global-settings | FE+BE. |
| TC-FA-SU-948 | E2E | TC-FA-SU-E2E-307-email-pending-dan-pengguna-nonaktif-di-global-settings | FE+BE. |
| TC-FA-SU-949 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-950 | E2E | TC-FA-SU-E2E-356-download-user-list-lebih-dari-5-000-baris-loading-screen-unduhan-langsung-dan-tanpa | FE+BE. |
| TC-FA-SU-951 | E2E | TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission | FE+BE. |
| TC-FA-SU-952 | E2E | TC-FA-SU-E2E-310-fan-out-responsibilities-pending-approvals-pending-tasks-dan-non-login-user | FE+BE. |
| TC-FA-SU-953 | E2E | TC-FA-SU-E2E-310-fan-out-responsibilities-pending-approvals-pending-tasks-dan-non-login-user | FE+BE. |
| TC-FA-SU-954 | E2E | TC-FA-SU-E2E-310-fan-out-responsibilities-pending-approvals-pending-tasks-dan-non-login-user | FE+BE. |
| TC-FA-SU-955 | E2E | TC-FA-SU-E2E-311-fan-out-transaction-admin-log-dan-satu-transaksi-menghasilkan-dua-baris-user-log | FE+BE. |
| TC-FA-SU-956 | E2E | TC-FA-SU-E2E-311-fan-out-transaction-admin-log-dan-satu-transaksi-menghasilkan-dua-baris-user-log | FE+BE. |
| TC-FA-SU-957 | E2E | TC-FA-SU-E2E-312-picker-peminjam-dan-penugasan-tetap-setelah-nonaktif | FE+BE. |
| TC-FA-SU-958 | E2E | TC-FA-SU-E2E-312-picker-peminjam-dan-penugasan-tetap-setelah-nonaktif | FE+BE. |
| TC-FA-SU-959 | E2E | TC-FA-SU-E2E-353-lockdown-tenant-tooltip-prioritas-user-list-suspended-transaction-role-suspended-dan | FE+BE. |
| TC-FA-SU-960 | E2E | TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission | FE+BE. |
| TC-FA-SU-961 | E2E | TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission | FE+BE. |
| TC-FA-SU-962 | E2E | TC-FA-SU-E2E-309-format-tanggal-general-settings-pohon-grup-settings-groups-dan-pembaruan-peran-dari-role-permission | FE+BE. |
| TC-FA-SU-963 | E2E | TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain | FE+BE. |
| TC-FA-SU-964 | E2E | TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-964 | E2E | TC-FA-SU-E2E-340-absence-log-request-ditolak-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-965 | E2E | TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-965 | E2E | TC-FA-SU-E2E-340-absence-log-request-ditolak-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-966 | E2E | TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-966 | E2E | TC-FA-SU-E2E-340-absence-log-request-ditolak-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-967 | E2E | TC-FA-SU-E2E-325-defense-in-depth-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-967 | E2E | TC-FA-SU-E2E-340-absence-log-request-ditolak-aktor-read-only-activate-deactivate-dan-global-role | FE+BE. |
| TC-FA-SU-968 | E2E | TC-FA-SU-E2E-326-defense-in-depth-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-968 | E2E | TC-FA-SU-E2E-341-absence-log-request-ditolak-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-969 | E2E | TC-FA-SU-E2E-326-defense-in-depth-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-969 | E2E | TC-FA-SU-E2E-341-absence-log-request-ditolak-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-970 | E2E | TC-FA-SU-E2E-326-defense-in-depth-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-970 | E2E | TC-FA-SU-E2E-341-absence-log-request-ditolak-aktor-read-only-group-role-dan-transaction-role | FE+BE. |
| TC-FA-SU-971 | E2E | TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-971 | E2E | TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-972 | E2E | TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-972 | E2E | TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-973 | E2E | TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-973 | E2E | TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-974 | E2E | TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-974 | E2E | TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-975 | E2E | TC-FA-SU-E2E-327-defense-in-depth-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-975 | E2E | TC-FA-SU-E2E-342-absence-log-request-ditolak-aktor-manage-user-dan-role-tanpa-update | FE+BE. |
| TC-FA-SU-976 | E2E | TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-976 | E2E | TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan | FE+BE. |
| TC-FA-SU-977 | E2E | TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-977 | E2E | TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan | FE+BE. |
| TC-FA-SU-978 | E2E | TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-978 | E2E | TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan | FE+BE. |
| TC-FA-SU-979 | E2E | TC-FA-SU-E2E-328-defense-in-depth-entitas-suspended-atau-expired-activate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-979 | E2E | TC-FA-SU-E2E-343-absence-log-request-ditolak-entitas-suspended-atau-expired-activate-global-role-dan | FE+BE. |
| TC-FA-SU-980 | E2E | TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan | FE+BE. |
| TC-FA-SU-980 | E2E | TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home | FE+BE. |
| TC-FA-SU-981 | E2E | TC-FA-SU-E2E-329-defense-in-depth-entitas-suspended-atau-expired-transaction-role-edit-home-group-dan | FE+BE. |
| TC-FA-SU-981 | E2E | TC-FA-SU-E2E-344-absence-log-request-ditolak-entitas-suspended-atau-expired-transaction-role-edit-home | FE+BE. |
| TC-FA-SU-982 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-982 | E2E | TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-983 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-983 | E2E | TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-984 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-984 | E2E | TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-985 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-985 | E2E | TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-986 | E2E | TC-FA-SU-E2E-330-defense-in-depth-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan-edit-home | FE+BE. |
| TC-FA-SU-986 | E2E | TC-FA-SU-E2E-345-absence-log-request-ditolak-aktor-ber-scope-grup-global-role-target-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-987 | E2E | TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-987 | E2E | TC-FA-SU-E2E-347-absence-log-request-ditolak-akun-sendiri-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-988 | E2E | TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-988 | E2E | TC-FA-SU-E2E-347-absence-log-request-ditolak-akun-sendiri-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-989 | E2E | TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-989 | E2E | TC-FA-SU-E2E-347-absence-log-request-ditolak-akun-sendiri-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-990 | E2E | TC-FA-SU-E2E-331-defense-in-depth-akun-sendiri-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-990 | E2E | TC-FA-SU-E2E-347-absence-log-request-ditolak-akun-sendiri-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-991 | E2E | TC-FA-SU-E2E-332-defense-in-depth-akun-sendiri-sebagai-target-transaction-role-dan-edit-home-group | FE+BE. |
| TC-FA-SU-991 | E2E | TC-FA-SU-E2E-348-absence-log-request-ditolak-akun-sendiri-sebagai-target-transaction-role-dan-edit | FE+BE. |
| TC-FA-SU-992 | E2E | TC-FA-SU-E2E-332-defense-in-depth-akun-sendiri-sebagai-target-transaction-role-dan-edit-home-group | FE+BE. |
| TC-FA-SU-992 | E2E | TC-FA-SU-E2E-348-absence-log-request-ditolak-akun-sendiri-sebagai-target-transaction-role-dan-edit | FE+BE. |
| TC-FA-SU-993 | E2E | TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-993 | E2E | TC-FA-SU-E2E-349-absence-log-request-ditolak-default-user-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-994 | E2E | TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-994 | E2E | TC-FA-SU-E2E-349-absence-log-request-ditolak-default-user-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-995 | E2E | TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-995 | E2E | TC-FA-SU-E2E-349-absence-log-request-ditolak-default-user-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-996 | E2E | TC-FA-SU-E2E-333-defense-in-depth-default-user-sebagai-target-deactivate-global-role-dan-group-role | FE+BE. |
| TC-FA-SU-996 | E2E | TC-FA-SU-E2E-349-absence-log-request-ditolak-default-user-sebagai-target-deactivate-global-role-dan | FE+BE. |
| TC-FA-SU-997 | E2E | TC-FA-SU-E2E-334-defense-in-depth-default-user-sebagai-target-transaction-role-dan-edit-home-group | FE+BE. |
| TC-FA-SU-997 | E2E | TC-FA-SU-E2E-350-absence-log-request-ditolak-default-user-sebagai-target-transaction-role-dan-edit | FE+BE. |
| TC-FA-SU-998 | E2E | TC-FA-SU-E2E-334-defense-in-depth-default-user-sebagai-target-transaction-role-dan-edit-home-group | FE+BE. |
| TC-FA-SU-998 | E2E | TC-FA-SU-E2E-350-absence-log-request-ditolak-default-user-sebagai-target-transaction-role-dan-edit | FE+BE. |
| TC-FA-SU-999 | E2E | TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | FE+BE. |
| TC-FA-SU-1000 | E2E | TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | FE+BE. |
| TC-FA-SU-1001 | E2E | TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | FE+BE. |
| TC-FA-SU-1002 | E2E | TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | FE+BE. |
| TC-FA-SU-1003 | E2E | TC-FA-SU-E2E-335-defense-in-depth-baca-di-luar-scope-bulk-langsung-flag-aktif-422-duplikat-dan-turun | FE+BE. |
| TC-FA-SU-1004 | E2E | TC-FA-SU-E2E-324-defense-in-depth-resend-dan-global-role-cooldown-status-tidak-valid-dan-switch-off | FE+BE. |
| TC-FA-SU-1004 | E2E | TC-FA-SU-E2E-339-absence-log-request-ditolak-resend-dan-global-role-cooldown-status-tidak-valid-dan | FE+BE. |
| TC-FA-SU-1005 | E2E | TC-FA-SU-E2E-314-guard-state-basi-dan-direct-url-detail-di-luar-scope | FE+BE. |
| TC-FA-SU-1006 | E2E | TC-FA-SU-E2E-314-guard-state-basi-dan-direct-url-detail-di-luar-scope | FE+BE. |
| TC-FA-SU-1007 | E2E | TC-FA-SU-E2E-314-guard-state-basi-dan-direct-url-detail-di-luar-scope | FE+BE. |
| TC-FA-SU-1008 | E2E | TC-FA-SU-E2E-357-multi-konteks-sesi-target-terputus-saat-deactivate-login-pengguna-nonaktif-sesi-lain | FE+BE. |
| TC-FA-SU-1009 | E2E | TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan | FE+BE. |
| TC-FA-SU-1010 | E2E | TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan | FE+BE. |
| TC-FA-SU-1011 | E2E | TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan | FE+BE. |
| TC-FA-SU-1012 | E2E | TC-FA-SU-E2E-315-resilience-jaringan-putus-atau-timeout-toggle-active-bulk-deactivate-switch-dan | FE+BE. |
| TC-FA-SU-1013 | E2E | TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend | FE+BE. |
| TC-FA-SU-1014 | E2E | TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend | FE+BE. |
| TC-FA-SU-1015 | E2E | TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend | FE+BE. |
| TC-FA-SU-1016 | E2E | TC-FA-SU-E2E-316-resilience-jaringan-putus-atau-timeout-save-group-role-submit-transaction-role-resend | FE+BE. |
| TC-FA-SU-1017 | E2E | TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal | FE+BE. |
| TC-FA-SU-1018 | E2E | TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal | FE+BE. |
| TC-FA-SU-1019 | E2E | TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal | FE+BE. |
| TC-FA-SU-1020 | E2E | TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup | FE+BE. |
| TC-FA-SU-1021 | E2E | TC-FA-SU-E2E-318-refresh-form-kotor-state-tab-dan-sub-tab-default-dan-ordering-serta-esc-dialog | FE+BE. |
| TC-FA-SU-1022 | E2E | TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup | FE+BE. |
| TC-FA-SU-1023 | E2E | TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup | FE+BE. |
| TC-FA-SU-1024 | E2E | TC-FA-SU-E2E-317-klik-ganda-sakelar-double-submit-klik-ganda-resend-dan-toast-tunggal | FE+BE. |
| TC-FA-SU-1025 | E2E | TC-FA-SU-E2E-351-state-tab-dan-sub-tab-detail-user-serta-default-dan-ordering | FE+BE. |
| TC-FA-SU-1026 | E2E | TC-FA-SU-E2E-351-state-tab-dan-sub-tab-detail-user-serta-default-dan-ordering | FE+BE. |
| TC-FA-SU-1027 | E2E | TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi | FE+BE. |
| TC-FA-SU-1028 | E2E | TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi | FE+BE. |
| TC-FA-SU-1029 | E2E | TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi | FE+BE. |
| TC-FA-SU-1030 | E2E | TC-FA-SU-E2E-319-must-not-bulk-tanpa-eligible-save-sebagian-edit-global-role-beruntun-dan-deaktivasi | FE+BE. |
| TC-FA-SU-1031 | E2E | TC-FA-SU-E2E-320-konkurensi-akses-dicabut-saat-popup-terbuka-item-bulk-berubah-dua-admin-dan-grup | FE+BE. |
| TC-FA-SU-1032 | E2E | TC-FA-SU-E2E-318-refresh-form-kotor-state-tab-dan-sub-tab-default-dan-ordering-serta-esc-dialog | FE+BE. |
| TC-FA-SU-1033 | E2E | TC-FA-SU-E2E-183-tab-non-login-user-search-dan-sort | FE+BE. |
| TC-FA-SU-1034 | E2E | TC-FA-SU-E2E-184-tab-non-login-user-sort | FE+BE. |
| TC-FA-SU-1035 | E2E | TC-FA-SU-E2E-187-tab-non-login-user-filter-dan-kontrol-filter-dan-setup-column | FE+BE. |
| TC-FA-SU-1036 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-1037 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-1038 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-1039 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-1040 | E2E | TC-FA-SU-E2E-308-custom-field-pengguna-accordion-rename-hapus-tipe-date-dan-phone-serta-filter-panel | FE+BE. |
| TC-FA-SU-1041 | E2E | TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all | FE+BE. |
| TC-FA-SU-1042 | E2E | TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all | FE+BE. |
| TC-FA-SU-1043 | E2E | TC-FA-SU-E2E-110-bulk-actions-bar-user-list-screening-empat-elemen-ikon-severity-dan-label-select-all | FE+BE. |
| TC-FA-SU-1044 | E2E | TC-FA-SU-E2E-113-group-summary-badge-sub-tab-group-role-sort-kolom-group-dan-ikon-changelog-sub-tab | FE+BE. |
| TC-FA-SU-1045 | E2E | TC-FA-SU-E2E-285-tab-user-log-sub-tab-session-screening-dan-search | FE+BE. |
| TC-FA-SU-1046 | E2E | TC-FA-SU-E2E-073-penutupan-modal-assign-transaction-role-dengan-isian-dan-aksesibilitas-modal | FE+BE. |
| TC-FA-SU-1047 | E2E | TC-FA-SU-E2E-103-popup-select-home-group-bulk-dan-aksesibilitas-popup-select-home-group | FE+BE. |
| TC-FA-SU-1048 | E2E | TC-FA-SU-E2E-083-bulk-remove-transaction-role-counter-dialog-plural-singular-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-1049 | E2E | TC-FA-SU-E2E-036-bulk-tanpa-baris-eligible-dialog-blok-collapse-ke-dialog-single-dan-cancel-bulk | FE+BE. |
| TC-FA-SU-1050 | E2E | TC-FA-SU-E2E-082-remove-satu-baris-transaction-role-cancel-dialog-dan-empty-state-berganti | FE+BE. |
| TC-FA-SU-1051 | E2E | TC-FA-SU-E2E-111-name-teks-panjang-header-satu-baris-dan-state-preservation-filter-status-dan-halaman | FE+BE. |
| TC-FA-SU-1052 | E2E | TC-FA-SU-E2E-111-name-teks-panjang-header-satu-baris-dan-state-preservation-filter-status-dan-halaman | FE+BE. |
| TC-FA-SU-1053 | E2E | TC-FA-SU-E2E-119-tabel-user-list-sort-bagian-3 | FE+BE. |
| TC-FA-SU-1054 | E2E | TC-FA-SU-E2E-055-eksklusivitas-global-role-manage-global-user-dan-role-vs-group-role-manage-user-dan | FE+BE. |
| TC-FA-SU-1055 | E2E | TC-FA-SU-E2E-056-cascade-total-control-terhadap-group-role-manage-user-dan-role-dan-sinkronisasi-dua | FE+BE. |
| TC-FA-SU-1056 | E2E | TC-FA-SU-E2E-101-popup-detail-group-assignment-screening-pencarian-setup-column-dan-download | FE+BE. |
| TC-FA-SU-1057 | E2E | TC-FA-SU-E2E-111-name-teks-panjang-header-satu-baris-dan-state-preservation-filter-status-dan-halaman | FE+BE. |
| TC-FA-SU-1058 | E2E | TC-FA-SU-E2E-182-tab-non-login-user-search | FE+BE. |
| TC-FA-SU-1059 | E2E | TC-FA-SU-E2E-203-modal-changelog-user-global-role-search | FE+BE. |
| TC-FA-SU-1060 | E2E | TC-FA-SU-E2E-084-kunci-transaction-role-bagi-aktor-ber-scope-grup-dan-target-tier | FE+BE. |
| TC-FA-SU-1061 | E2E | TC-FA-SU-E2E-352-defense-in-depth-assign-transaction-role-target-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1062 | E2E | TC-FA-SU-E2E-323-defense-in-depth-transaction-role-dan-group-role-target-tier-di-luar-scope-dan | FE+BE. |
| TC-FA-SU-1063 | E2E | TC-FA-SU-E2E-024-kunci-target-tier-bagi-aktor-ber-scope-grup-dan-group-manager-deactivate-dan-bulk-skip | FE+BE. |
| TC-FA-SU-1064 | E2E | TC-FA-SU-E2E-322-defense-in-depth-tier-deactivate-dan-activate-target-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1065 | E2E | TC-FA-SU-E2E-027-kunci-target-tier-bagi-aktor-global-ber-scope-grup-dan-group-manager-bulk-activate-skip | FE+BE. |
| TC-FA-SU-1066 | E2E | TC-FA-SU-E2E-322-defense-in-depth-tier-deactivate-dan-activate-target-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1067 | E2E | TC-FA-SU-E2E-322-defense-in-depth-tier-deactivate-dan-activate-target-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1067 | E2E | TC-FA-SU-E2E-337-absence-log-request-ditolak-tier-deactivate-dan-activate-target-total-control-dan | FE+BE. |
| TC-FA-SU-1068 | E2E | TC-FA-SU-E2E-105-edit-home-group-aktor-manage-global-user-dan-role-kunci-baris-group-manager-dan-dialog-gabungan | FE+BE. |
| TC-FA-SU-1069 | E2E | TC-FA-SU-E2E-106-edit-home-group-target-total-control-dan-read-only-oleh-default-user-dan-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-1070 | E2E | TC-FA-SU-E2E-380-auto-revert-tier-total-control-dari-modal-assign-transaction-role-cancel-remove-baris-pola-dan-turun-tangga | FE+BE. |
| TC-FA-SU-1071 | E2E | TC-FA-SU-E2E-385-auto-revert-tier-read-only-dari-modal-assign-transaction-role-naik-tangga | FE+BE. |
| TC-FA-SU-1072 | E2E | TC-FA-SU-E2E-381-screening-banner-tier-dan-baris-pola-sub-tab-transaction-role-dan-group-role-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1073 | E2E | TC-FA-SU-E2E-380-auto-revert-tier-total-control-dari-modal-assign-transaction-role-cancel-remove-baris-pola-dan-turun-tangga | FE+BE. |
| TC-FA-SU-1074 | E2E | TC-FA-SU-E2E-386-banner-group-manager-per-sub-tab-role-tidak-tampil-di-transaction-role | FE+BE. |
| TC-FA-SU-1075 | E2E | TC-FA-SU-E2E-382-tab-transaction-admin-log-user-total-control-tanpa-transaksi-empty-state | FE+BE. |
| TC-FA-SU-1076 | E2E | TC-FA-SU-E2E-378-auto-revert-tier-total-control-dari-popup-assign-group-role-edit-centang-crud | FE+BE. |
| TC-FA-SU-1077 | E2E | TC-FA-SU-E2E-383-auto-revert-tier-read-only-dari-popup-assign-group-role-hapus-grup | FE+BE. |
| TC-FA-SU-1078 | E2E | TC-FA-SU-E2E-379-auto-revert-tier-dari-popup-assign-group-role-tambah-grup-yang-menyimpangkan-pola | FE+BE. |
| TC-FA-SU-1079 | E2E | TC-FA-SU-E2E-384-cancel-dialog-auto-revert-dari-popup-assign-group-role-popup-kembali-utuh | FE+BE. |
| TC-FA-SU-1080 | E2E | TC-FA-SU-E2E-381-screening-banner-tier-dan-baris-pola-sub-tab-transaction-role-dan-group-role-total-control-dan-read-only | FE+BE. |
| TC-FA-SU-1081 | E2E | TC-FA-SU-E2E-387-screening-banner-group-manager-dan-baris-pola-sub-tab-group-role-dan-transaction-role-target-group-manager | FE+BE. |
| TC-FA-SU-1082 | E2E | TC-FA-SU-E2E-392-edit-baris-pola-group-manager-pada-node-turunan-dialog-auto-revert | FE+BE. |
| TC-FA-SU-1083 | E2E | TC-FA-SU-E2E-391-remove-baris-grup-pola-group-manager-dari-popup-dan-perubahan-non-pola-tanpa-auto-revert | FE+BE. |
| TC-FA-SU-1084 | E2E | TC-FA-SU-E2E-391-remove-baris-grup-pola-group-manager-dari-popup-dan-perubahan-non-pola-tanpa-auto-revert | FE+BE. |
| TC-FA-SU-1085 | E2E | TC-FA-SU-E2E-388-kunci-baris-pola-group-role-target-group-manager-bagi-aktor-manage-user-dan-role-group-dan-baris-non-pola | FE+BE. |
| TC-FA-SU-1086 | E2E | TC-FA-SU-E2E-393-group-manager-bersarang-dialog-d-05c-satu-penugasan-dan-dialog-d-05d-dua-penugasan | FE+BE. |
| TC-FA-SU-1087 | E2E | TC-FA-SU-E2E-393-group-manager-bersarang-dialog-d-05c-satu-penugasan-dan-dialog-d-05d-dua-penugasan | FE+BE. |
| TC-FA-SU-1088 | E2E | TC-FA-SU-E2E-387-screening-banner-group-manager-dan-baris-pola-sub-tab-group-role-dan-transaction-role-target-group-manager | FE+BE. |
| TC-FA-SU-1089 | E2E | TC-FA-SU-E2E-389-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-user-dan-role-group | FE+BE. |
| TC-FA-SU-1089 | E2E | TC-FA-SU-E2E-401-kunci-baris-pola-transaction-role-target-group-manager-bagi-aktor-manage-global-user-dan-role | FE+BE. |
| TC-FA-SU-1090 | E2E | TC-FA-SU-E2E-394-remove-baris-pola-transaction-role-target-group-manager-dialog-auto-revert-cancel-lalu-konfirmasi | FE+BE. |
| TC-FA-SU-1091 | E2E | TC-FA-SU-E2E-405-bulk-remove-transaction-role-target-group-manager-baris-non-pola-dan-baris-pola | FE+BE. |
| TC-FA-SU-1092 | E2E | TC-FA-SU-E2E-395-turun-tangga-modal-assign-transaction-role-target-group-manager-dialog-auto-revert-menggantikan-dialog-turun-tangga | FE+BE. |
| TC-FA-SU-1093 | E2E | TC-FA-SU-E2E-406-save-campuran-modal-assign-transaction-role-target-group-manager-dialog-turun-tangga-lalu-auto-revert | FE+BE. |
| TC-FA-SU-1094 | E2E | TC-FA-SU-E2E-396-popup-assign-group-baris-pola-transaction-role-target-group-manager-tambah-grup-luar-subtree-dan-cabut-grup-dalam-subtree | FE+BE. |
| TC-FA-SU-1095 | E2E | TC-FA-SU-E2E-397-edit-home-group-yang-mencabut-baris-pola-group-manager-dialog-gabungan-dan-log-per-baris | FE+BE. |
| TC-FA-SU-1096 | E2E | TC-FA-SU-E2E-390-kolom-role-popup-role-count-filter-dan-search-user-group-manager-baris-pola-tanpa-badge | FE+BE. |
| TC-FA-SU-1097 | E2E | TC-FA-SU-E2E-398-assign-group-manager-materialisasi-baris-pola-tampil-via-group-manager-hanya-di-modal-changelog-user | FE+BE. |
| TC-FA-SU-1098 | E2E | TC-FA-SU-E2E-403-pelepasan-group-manager-remove-via-group-manager-hanya-di-modal-changelog-user | FE+BE. |
| TC-FA-SU-1099 | E2E | TC-FA-SU-E2E-399-defense-in-depth-baris-pola-group-manager-ditolak-403-baris-manage-user-role-diterima-dan-konfirmasi-auto-revert-409 | FE+BE. |
| TC-FA-SU-1099 | E2E | TC-FA-SU-E2E-400-absence-log-request-ditolak-baris-pola-group-manager-oleh-aktor-non-default-user-total-control | FE+BE. |
| TC-FA-SU-1100 | E2E | TC-FA-SU-E2E-407-pasca-auto-revert-group-manager-lewat-group-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-status-gm-tidak-kembali | FE+BE. |
| TC-FA-SU-1101 | E2E | TC-FA-SU-E2E-408-pasca-auto-revert-group-manager-lewat-transaction-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-remove-d-07a-biasa | FE+BE. |
| TC-FA-SU-1102 | E2E | TC-FA-SU-E2E-409-preview-scope-di-modal-assign-transaction-role | FE+BE. |
| TC-FA-SU-1103 | E2E | TC-FA-SU-E2E-410-preview-scope-di-popup-assign-group-transaction-role | FE+BE. |
| TC-FA-SU-1104 | E2E | TC-FA-SU-E2E-411-pohon-group-tanpa-node-disabled-karena-ancestor-atau-descendant-pada-modal-dan-popup | FE+BE. |
| TC-FA-SU-1105 | E2E | TC-FA-SU-E2E-415-assign-overlap-di-node-turunan-role-lebih-rendah-dan-lebih-tinggi-tanpa-d-06-ancestor-tidak-berubah | FE+BE. |
| TC-FA-SU-1106 | E2E | TC-FA-SU-E2E-415-assign-overlap-di-node-turunan-role-lebih-rendah-dan-lebih-tinggi-tanpa-d-06-ancestor-tidak-berubah | FE+BE. |
| TC-FA-SU-1107 | E2E | TC-FA-SU-E2E-416-assign-overlap-ancestor-setelah-turunan-dan-assign-group-menambah-descendant | FE+BE. |
| TC-FA-SU-1108 | E2E | TC-FA-SU-E2E-417-dialog-d-06-hanya-node-yang-sama-node-lain-naik-tangga-dan-cancel-membatalkan-seluruh-save | FE+BE. |
| TC-FA-SU-1109 | E2E | TC-FA-SU-E2E-422-defense-in-depth-guard-server-409-confirmation-required-hanya-node-yang-sama-assign-node-lain-tanpa-confirmdowngrade | FE+BE. |
| TC-FA-SU-1110 | E2E | TC-FA-SU-E2E-416-assign-overlap-ancestor-setelah-turunan-dan-assign-group-menambah-descendant | FE+BE. |
| TC-FA-SU-1111 | E2E | TC-FA-SU-E2E-418-remove-baris-pada-node-ancestor-dialog-d-07a-generik-dan-satu-entri-log | FE+BE. |
| TC-FA-SU-1112 | E2E | TC-FA-SU-E2E-412-baris-literal-sub-tab-transaction-role-tanpa-proyeksi-descendant | FE+BE. |
| TC-FA-SU-1113 | E2E | TC-FA-SU-E2E-421-label-role-dan-popup-role-count-literal-node-descendant-tercakup-tidak-dihitung | FE+BE. |
| TC-FA-SU-1114 | E2E | TC-FA-SU-E2E-423-pemilih-group-role-target-ber-constraint-node-dalam-dan-luar-constraint-dan-assign-ke-node-dalam | FE+BE. |
| TC-FA-SU-1115 | E2E | TC-FA-SU-E2E-423-pemilih-group-role-target-ber-constraint-node-dalam-dan-luar-constraint-dan-assign-ke-node-dalam | FE+BE. |
| TC-FA-SU-1116 | E2E | TC-FA-SU-E2E-430-defense-in-depth-assign-group-role-dan-transaction-role-di-luar-home-group-constraint-ditolak-422-v09 | FE+BE. |
| TC-FA-SU-1116 | E2E | TC-FA-SU-E2E-431-absence-log-assign-group-role-dan-transaction-role-ditolak-gate-home-group-tanpa-entri-di-tiga-surface | FE+BE. |
| TC-FA-SU-1117 | E2E | TC-FA-SU-E2E-424-modal-assign-dan-popup-assign-group-transaction-role-target-ber-constraint-node-disabled-dan-tooltip-s-45 | FE+BE. |
| TC-FA-SU-1118 | E2E | TC-FA-SU-E2E-424-modal-assign-dan-popup-assign-group-transaction-role-target-ber-constraint-node-disabled-dan-tooltip-s-45 | FE+BE. |
| TC-FA-SU-1119 | E2E | TC-FA-SU-E2E-426-target-tanpa-home-group-tiga-pemilih-tanpa-penyaringan-node | FE+BE. |
| TC-FA-SU-1120 | E2E | TC-FA-SU-E2E-427-assign-transaction-role-ke-node-dalam-constraint-dan-penugasan-lama-di-luar-constraint-tidak-dimigrasi | FE+BE. |
| TC-FA-SU-1121 | E2E | TC-FA-SU-E2E-427-assign-transaction-role-ke-node-dalam-constraint-dan-penugasan-lama-di-luar-constraint-tidak-dimigrasi | FE+BE. |
| TC-FA-SU-1122 | E2E | TC-FA-SU-E2E-430-defense-in-depth-assign-group-role-dan-transaction-role-di-luar-home-group-constraint-ditolak-422-v09 | FE+BE. |
| TC-FA-SU-1122 | E2E | TC-FA-SU-E2E-431-absence-log-assign-group-role-dan-transaction-role-ditolak-gate-home-group-tanpa-entri-di-tiga-surface | FE+BE. |
| TC-FA-SU-1123 | E2E | TC-FA-SU-E2E-428-constraint-berubah-antara-modal-assign-dibuka-dan-submit-ditolak-422-dan-pilihan-stale-dibersihkan | FE+BE. |
| TC-FA-SU-1123 | E2E | TC-FA-SU-E2E-432-absence-log-submit-modal-assign-ditolak-akibat-constraint-berubah-tanpa-entri-assign-baru | FE+BE. |
| TC-FA-SU-1124 | E2E | TC-FA-SU-E2E-425-ancestor-constraint-disabled-di-tiga-pemilih-dan-node-constraint-dapat-dicentang | FE+BE. |
| TC-FA-SU-1125 | E2E | TC-FA-SU-E2E-434-absence-pencabutan-silent-edit-home-group-tanpa-entri-remove-dan-tanpa-notifikasi | FE+BE. |
| TC-FA-SU-1125 | E2E | TC-FA-SU-E2E-435-edit-home-group-mencabut-group-role-dan-role-transaksi-di-luar-constraint-silent | FE+BE. |
| TC-FA-SU-1126 | E2E | TC-FA-SU-E2E-436-edit-home-group-pengguna-hanya-role-transaksi-dialog-d-10-dan-constraint-node-turunan | FE+BE. |
| TC-FA-SU-1127 | E2E | TC-FA-SU-E2E-436-edit-home-group-pengguna-hanya-role-transaksi-dialog-d-10-dan-constraint-node-turunan | FE+BE. |
| TC-FA-SU-1128 | E2E | TC-FA-SU-E2E-437-bulk-edit-home-group-standard-dan-read-only-dialog-d-10-hanya-untuk-standard | FE+BE. |

---

## 4. Catatan Penulisan

- Nomor TC yang tidak ada di file TC: tidak ada.
- Nomor cadangan dipakai oleh banyak slice untuk memecah spec yang melewati sekitar 35 langkah; pemetaan TC ke spec di bagian 1 dan 3 mengikuti hasil akhir (sourceTc di frontmatter), bukan tabel rencana awal. Slug beberapa spec (mis. 004, 005, 043, 353-356) tidak lagi persis sama dengan isinya karena TC dipindah ke nomor cadangan.
- TC yang sengaja ada di dua spec (spec asal dan spec absence kelas g, S-05): 125, 126, 127, 128, 129, 130, 146, 148, 171, 183, 222, 223, 272, 304, 305, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993, 994, 995, 996, 997, 998, 1004, 1067, 1089 (dibagi per aktor Sinta dan Qori: 389 dan 401), 1099 (399 fungsional dan 400 absence). `check-suite.py` menandai ini sebagai C2; itu disengaja.
- Banyak spec melewati 35 langkah dan memuat alasan di Notes (C6); penyebab utama: satu `Verifikasi` per klausa Expected (S-01) dan ekspansi blok berulang per kolom.
- Fixture `Fixture.*`, akun tenant khusus, kemampuan seed/baca log/notifikasi/berkas, serta nama env password baru belum ada; ditandai di Prerequisites tiap spec sebagai disediakan tim FE/BE dan dicatat di Temuan untuk QA.
