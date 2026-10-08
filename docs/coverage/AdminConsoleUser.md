# Coverage E2E — Admin Console > Settings > User

Sumber: `admin-console/settings-user/TestCases/tc-settings-user.md` (260 TC granular aktif) dan `admin-console/settings-user/TestCases/tc-settings-user-backend.md`.
Suite: `specs_dummy/AdminConsole/User/` (Disiapkan untuk promosi ke `specs/AdminConsole/User/`).
Prefix Modul: `AC` + `SU` (`TC-AC-SU-E2E-*`).
Status semua spec: `draft`.
Arsitektur Otomasi: 53 Spec Atomik Terisolasi Tinggi (Harness-Separated per e2e-conventions.md §13).

---

## 1. Pemetaan TC Granular → Spec E2E (53 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-AC-SU-E2E-001-screening-halaman-user-list-dan-struktur-kolom | Screening halaman User List, breadcrumb, header, struktur kolom tabel, baris Default User dan Self | FE+BE | TC-AC-SU-1, TC-AC-SU-2, TC-AC-SU-3, TC-AC-SU-4, TC-AC-SU-5, TC-AC-SU-6, TC-AC-SU-7, TC-AC-SU-8, TC-AC-SU-9, TC-AC-SU-12, TC-AC-SU-163, TC-AC-SU-165, TC-AC-SU-264, TC-AC-SU-265, TC-AC-SU-266 |
| TC-AC-SU-E2E-002-empty-state-loading-dan-read-failure-resilience | Loading state, simulasi error fetch 500, pemulihan via Try Again, dan empty state no results found | mock | TC-AC-SU-10, TC-AC-SU-11 |
| TC-AC-SU-E2E-003-guided-tooltip-walkthrough-dan-siklus-navigasi | Guided Tooltip walkthrough 5 step, auto-trigger kunjungan pertama, manual replay, dan keyboard navigation | FE+BE | TC-AC-SU-228, TC-AC-SU-229, TC-AC-SU-267, TC-AC-SU-268 |
| TC-AC-SU-E2E-004-user-list-setup-column-dan-curated-columns | Setup Column User List, toggle visibilitas 4 kolom curated, render badge format, dan sorting | FE+BE | TC-AC-SU-260 |
| TC-AC-SU-E2E-005-user-list-search-toolbar-per-kolom-dan-guard | Pencarian toolbar User List per kolom teks dan guard kolom non-searchable | FE+BE | TC-AC-SU-13, TC-AC-SU-14, TC-AC-SU-234, TC-AC-SU-235, TC-AC-SU-236, TC-AC-SU-237, TC-AC-SU-238 |
| TC-AC-SU-E2E-006-user-list-filter-panel-multi-select-dan-dropdown-populate | Filter Panel User List, multi-select searchable, populate dropdown dinamis, dan enum hardcode | FE+BE | TC-AC-SU-15, TC-AC-SU-16, TC-AC-SU-17, TC-AC-SU-18, TC-AC-SU-226, TC-AC-SU-269, TC-AC-SU-270, TC-AC-SU-272 |
| TC-AC-SU-E2E-007-user-list-filter-date-range-dan-format-general-settings | Filter rentang tanggal Last Updated dan Temporary Until serta kepatuhan format General Settings | FE+BE | TC-AC-SU-271, TC-AC-SU-273, TC-AC-SU-285 |
| TC-AC-SU-E2E-008-user-list-sorting-3-state-dan-guard-kolom-non-sortable | Sorting 3-state pada 12 kolom sortable User List, transisi header sort, dan guard kolom non-sortable | FE+BE | TC-AC-SU-19, TC-AC-SU-274, TC-AC-SU-275, TC-AC-SU-276 |
| TC-AC-SU-E2E-009-user-list-sidebar-group-tree-dan-state-collapse | Navigasi Sidebar Group tree hirarki, filtering user per group, dan persistensi state collapse | FE+BE | TC-AC-SU-20, TC-AC-SU-293 |
| TC-AC-SU-E2E-010-user-list-export-csv-xlsx-wysiwyg-dan-transformasi-teks | Export CSV dan XLSX User List, format WYSIWYG kolom terfilter, transformasi representasi teks, dan penanganan error | FE+BE | TC-AC-SU-22, TC-AC-SU-277, TC-AC-SU-278, TC-AC-SU-279 |
| TC-AC-SU-E2E-011-user-list-export-failure-resilience-dan-toast-error | Ketahanan ekspor User List: simulasi kegagalan server 500 dan toast error feedback | mock | TC-AC-SU-280 |
| TC-AC-SU-E2E-012-modal-changelog-list-toolbar-filter-column-visibility | Modal Changelog User List, Search, Filter Panel, Column Visibility terpisah, dan export CSV | FE+BE | TC-AC-SU-23, TC-AC-SU-24, TC-AC-SU-25, TC-AC-SU-227 |
| TC-AC-SU-E2E-013-user-list-state-preservation-dan-pagination-controls | Persistensi state filter dan search saat tab switching dan refresh F5, pagination page size, serta Clear Filter | FE+BE | TC-AC-SU-232, TC-AC-SU-233, TC-AC-SU-281, TC-AC-SU-282, TC-AC-SU-283, TC-AC-SU-284 |
| TC-AC-SU-E2E-014-row-action-activate-user-dan-dialog-konfirmasi | Aktivasi user baris tunggal (OFF ke ON), dialog konfirmasi info, Cancel path, dan aktivasi sukses | FE+BE | TC-AC-SU-26, TC-AC-SU-223 |
| TC-AC-SU-E2E-015-row-action-deactivate-user-dialog-konfirmasi-dan-focus-trap | Deaktivasi user baris tunggal (ON ke OFF), dialog konfirmasi danger, focus trap a11y, Cancel path, dan toast sukses | FE+BE | TC-AC-SU-28, TC-AC-SU-29, TC-AC-SU-291 |
| TC-AC-SU-E2E-016-row-action-deactivate-user-dual-session-real-time-force-logout | Terminasi Sesi Real-Time dan Force Logout Saat Deaktivasi User Target | FE+BE | TC-AC-SU-27 |
| TC-AC-SU-E2E-017-guard-proteksi-switch-active-default-user-self-edit-dan-tier | Guard Proteksi Switch Active: Default User, Self-Edit, Suspended, dan Tier Locked | FE+BE | TC-AC-SU-30, TC-AC-SU-31, TC-AC-SU-32, TC-AC-SU-33, TC-AC-SU-34, TC-AC-SU-35, TC-AC-SU-36, TC-AC-SU-160 |
| TC-AC-SU-E2E-018-bulk-action-bar-local-selection-dan-batch-commands | Bulk Action Bar Interaksi Lokal, Counter Dinamis, dan Batch Commands | FE+BE | TC-AC-SU-37, TC-AC-SU-38, TC-AC-SU-224, TC-AC-SU-225, TC-AC-SU-287, TC-AC-SU-288 |
| TC-AC-SU-E2E-019-bulk-action-bar-server-select-all-cross-page-dan-partial-skip | Bulk Action Bar Server Select All Lintas Halaman dan Partial Skip User Non-Eligible | FE+BE | TC-AC-SU-214, TC-AC-SU-249 |
| TC-AC-SU-E2E-020-bulk-action-bar-single-row-collapse-dialog-format | Bulk Action Bar dengan 1 Baris Terpilih Collapse ke Format Dialog Baris Tunggal | FE+BE | TC-AC-SU-230, TC-AC-SU-231 |
| TC-AC-SU-E2E-021-bulk-selection-limit-1000-rows-dan-live-block-disabled | Batas Seleksi Maksimum 1000 Baris dan Live Block Disabled Checkbox | FE+BE | TC-AC-SU-39, TC-AC-SU-222 |
| TC-AC-SU-E2E-022-resilience-error-5xx-optimistic-rollback-dan-conflict-409 | Resiliensi Error 5xx Optimistic Rollback dan Penanganan 409 Conflict pada Switch Active | mock | TC-AC-SU-41, TC-AC-SU-174, TC-AC-SU-219, TC-AC-SU-263 |
| TC-AC-SU-E2E-023-row-action-resend-activation-mail-cooldown-timer-ui | Row Action Resend Activation Email dan Cooldown Timer UI 60 Detik | FE+BE | TC-AC-SU-42, TC-AC-SU-43, TC-AC-SU-44, TC-AC-SU-47, TC-AC-SU-286 |
| TC-AC-SU-E2E-024-bulk-resend-activation-mail-partial-skip-dan-batch-delivery | Bulk Resend Activation Email: Partial Skip Non-Pending dan Partial Skip Cooldown | FE+BE | TC-AC-SU-46, TC-AC-SU-258, TC-AC-SU-289 |
| TC-AC-SU-E2E-025-row-action-resend-confirmation-mail-cooldown-timer-ui | Row Action Resend Confirmation Email, Cooldown 60 Detik, dan Guard Ketiadaan di Bulk Bar | FE+BE | TC-AC-SU-48, TC-AC-SU-49, TC-AC-SU-50, TC-AC-SU-51, TC-AC-SU-292 |
| TC-AC-SU-E2E-026-resend-emails-mail-catcher-payload-dan-token-inspection | Verifikasi Payload Email Aktivasi dan Konfirmasi via Mail-Catcher API | FE+BE | TC-AC-SU-217, TC-AC-SU-218 |
| TC-AC-SU-E2E-027-resilience-resend-email-server-error-5xx-preserve-cooldown | Resiliensi Server Error 5xx pada Resend Activation dan Confirmation Email Tanpa Membakar Cooldown | mock | TC-AC-SU-178, TC-AC-SU-220 |
| TC-AC-SU-E2E-028-detail-user-header-readonly-badge-user-type-dan-general-info | Detail User: Header Read-Only, Avatar, Badge User Type, dan General Information | FE+BE | TC-AC-SU-54, TC-AC-SU-55, TC-AC-SU-57, TC-AC-SU-58, TC-AC-SU-59, TC-AC-SU-60, TC-AC-SU-62, TC-AC-SU-63 |
| TC-AC-SU-E2E-029-tab-role-global-role-toggle-autosave-crud-dan-sync-role-permission | Detail User Tab Role: Global Role Toggle, Autosave CRUD per Cell, dan Sinkronisasi 2-Arah | FE+BE | TC-AC-SU-64, TC-AC-SU-65, TC-AC-SU-66, TC-AC-SU-67, TC-AC-SU-68 |
| TC-AC-SU-E2E-030-tab-role-global-role-permission-guards-dan-modal-changelog | Guard Hak Akses Global Role (Default User, Self-Edit, Tier Lock) dan Modal Changelog | FE+BE | TC-AC-SU-69, TC-AC-SU-71, TC-AC-SU-72, TC-AC-SU-73, TC-AC-SU-161 |
| TC-AC-SU-E2E-031-tab-role-global-role-crud-autosave-error-5xx-rollback-resilience | Resiliensi Autosave CRUD Global Role Terhadap Error Jaringan 5xx dan Visual Rollback | mock | TC-AC-SU-176, TC-AC-SU-252 |
| TC-AC-SU-E2E-032-tab-role-group-role-catalog-summary-badge-dan-revoke-group | Tab Role Sub-tab Group Role: Katalog Role, Group Summary Badge, dan Revoke Akses | FE+BE | TC-AC-SU-74, TC-AC-SU-75, TC-AC-SU-76, TC-AC-SU-77, TC-AC-SU-80, TC-AC-SU-81, TC-AC-SU-82, TC-AC-SU-85 |
| TC-AC-SU-E2E-033-tab-role-group-role-guards-modal-detail-assignment-dan-changelog | Guard Sub-tab Group Role (Default User, Self-Edit), Modal Detail Assignment, dan Changelog | FE+BE | TC-AC-SU-84, TC-AC-SU-162, TC-AC-SU-221, TC-AC-SU-261 |
| TC-AC-SU-E2E-034-popup-assign-group-role-tree-hierarchy-picker-dan-scope-restriction | Popup Assign Group Role: Tree Picker Hirarki, Scope Restriction, dan Proteksi Duplikat | FE+BE | TC-AC-SU-86, TC-AC-SU-87, TC-AC-SU-90, TC-AC-SU-91, TC-AC-SU-93, TC-AC-SU-256 |
| TC-AC-SU-E2E-035-popup-assign-group-role-save-put-replace-lifecycle | Assign Group Role: Alur Penyimpanan Save Replace PUT dan Verifikasi No-Op | FE+BE | TC-AC-SU-78, TC-AC-SU-96, TC-AC-SU-250, TC-AC-SU-257 |
| TC-AC-SU-E2E-036-popup-assign-group-role-clear-field-unsaved-dan-zero-group-guard | Assign Group Role: Siklus Clear Field, Guard Unsaved Changes, dan Dialog Blokir 0 Group | FE+BE | TC-AC-SU-79, TC-AC-SU-99, TC-AC-SU-101, TC-AC-SU-251, TC-AC-SU-259 |
| TC-AC-SU-E2E-037-popup-assign-group-role-network-error-5xx-dan-conflict-409 | Resiliensi Error Jaringan 5xx dan 409 Conflict pada Popup Assign Group Role | mock | TC-AC-SU-97, TC-AC-SU-98, TC-AC-SU-177 |
| TC-AC-SU-E2E-038-tab-role-banner-tier-total-control-read-only-group-manager | Banner Indikator Tier pada Tab Role (Total Control, Read Only, Group Manager) | FE+BE | TC-AC-SU-102, TC-AC-SU-103, TC-AC-SU-104, TC-AC-SU-105 |
| TC-AC-SU-E2E-039-auto-revert-tier-total-control-dan-group-manager-divergence-lifecycle | Siklus Auto-Revert Tier Total Control dan Group Manager Saat Konfigurasi Role Menyimpang | FE+BE | TC-AC-SU-70, TC-AC-SU-107, TC-AC-SU-108, TC-AC-SU-110, TC-AC-SU-112, TC-AC-SU-262, TC-AC-SU-290 |
| TC-AC-SU-E2E-040-detail-user-tab-responsibilities-pending-approvals-setup-column-dan-export | Detail User Tab Responsibilities: Pending Approvals, Setup Column, dan Export CSV | FE+BE | TC-AC-SU-116, TC-AC-SU-117, TC-AC-SU-119, TC-AC-SU-120, TC-AC-SU-121, TC-AC-SU-122, TC-AC-SU-123, TC-AC-SU-253 |
| TC-AC-SU-E2E-041-detail-user-tab-changelog-user-search-filter-column-visibility-dan-export | Detail User Tab Changelog: Riwayat Mutasi User, Search, Filter Rentang Tanggal, dan Export | FE+BE | TC-AC-SU-124, TC-AC-SU-126, TC-AC-SU-127, TC-AC-SU-128, TC-AC-SU-129, TC-AC-SU-130, TC-AC-SU-131, TC-AC-SU-132, TC-AC-SU-133 |
| TC-AC-SU-E2E-042-detail-user-tab-system-log-scoping-per-app-dan-export-csv | Detail User Tab System Log: Log Aktivitas User Sebagai Aktor Lintas Aplikasi dan Export | FE+BE | TC-AC-SU-134, TC-AC-SU-135, TC-AC-SU-137, TC-AC-SU-138, TC-AC-SU-139, TC-AC-SU-141 |
| TC-AC-SU-E2E-043-detail-user-tab-user-log-session-history-force-logout-dan-export-csv | Detail User Tab User Log: Riwayat Sesi Login, Event Force Logout, dan Export CSV | FE+BE | TC-AC-SU-240, TC-AC-SU-241, TC-AC-SU-242, TC-AC-SU-244, TC-AC-SU-245, TC-AC-SU-246 |
| TC-AC-SU-E2E-044-in-app-notification-delivery-on-access-removal-dan-auto-revert | Pengiriman Notifikasi In-App Saat Pencabutan Akses dan Terjadinya Auto-Revert | FE+BE | TC-AC-SU-204, TC-AC-SU-205, TC-AC-SU-206, TC-AC-SU-208, TC-AC-SU-209, TC-AC-SU-210, TC-AC-SU-247 |
| TC-AC-SU-E2E-045-in-app-notification-absence-assertion-on-access-grant-dan-group-delete | Asersi Ketiadaan Notifikasi In-App pada Penugasan Akses Baru dan Penghapusan Grup | FE+BE | TC-AC-SU-211, TC-AC-SU-212, TC-AC-SU-248 |
| TC-AC-SU-E2E-046-role-matrix-positive-access-menu-settings-user-dan-full-write-controls | Role Matrix Positif: Akses Menu Settings User dan Kontrol Write Penuh | FE+BE | TC-AC-SU-150 |
| TC-AC-SU-E2E-047-role-matrix-negative-sidebar-hidden-dan-direct-url-unauthorized-guard | Role Matrix Negatif: Penolakan Sidebar Menu dan Direct URL Unauthorized Guard | FE+BE | TC-AC-SU-21, TC-AC-SU-153, TC-AC-SU-154, TC-AC-SU-239 |
| TC-AC-SU-E2E-048-multi-tenant-data-isolation-antara-entitas-distributor | Multi-Tenant Data Isolation Antara Entitas Distributor Terpisah | FE+BE | TC-AC-SU-151 |
| TC-AC-SU-E2E-049-multi-tenant-entity-suspended-blanket-lockdown-resilience | Penegakan Status Entitas Suspended: Blanket Read-Only Lockdown Lintas Modul | FE+BE | TC-AC-SU-40, TC-AC-SU-159 |
| TC-AC-SU-E2E-050-concurrency-race-condition-deactivate-vs-assign-role-dan-auto-revert | Resiliensi Concurrency Race Condition 2 Aktor: Deactivate vs Assign Group Role dan Auto-Revert | FE+BE | TC-AC-SU-215, TC-AC-SU-216 |
| TC-AC-SU-E2E-051-accessibility-wcag21-aa-keyboard-navigation-dan-aria-live-polite | Aksesibilitas WCAG 2.1 AA: Navigasi Keyboard Penuh, Focus Trap, dan ARIA-Live Polite | FE+BE | TC-AC-SU-196, TC-AC-SU-197, TC-AC-SU-198 |
| TC-AC-SU-E2E-052-license-and-plan-gating-feature-lockout-parity-verification | Verifikasi Ketiadaan Plan Gating dan Paritas Fitur Lengkap di Seluruh Tingkat Langganan | FE+BE | TC-AC-SU-202, TC-AC-SU-203 |
| TC-AC-SU-E2E-053-cross-module-sync-profile-picture-global-settings-dan-approvals-fan-out | Sinkronisasi Lintas Modul: Pembaruan Foto Profil di Global Settings dan Fan-Out ke Approvals | FE+BE | TC-AC-SU-56, TC-AC-SU-185, TC-AC-SU-186 |

---

## 2. TC Granular Hanya-BE (Pure Backend Contract — Tidak Masuk Spec E2E UI)

| TC ID | Skenario | Alasan Pengecualian E2E UI |
|---|---|---|
| TC-AC-SU-53 | Email Confirmed tidak menghasilkan log di modul ini | Event konfirmasi email dicatat penuh di Global Settings, AC tidak menulis log redundan |
| TC-AC-SU-83 | Multi-group CRUD resolution exact match tanpa pewarisan | Logika resolusi query otorisasi database level backend |
| TC-AC-SU-106 | Assign Total Control dari Role & Permission bulk-write peran | Penugasan tier via backend batch write ke tabel peran |
| TC-AC-SU-109 | Remove Total Control reset peran individual | Logika cascade reset peran di tingkat database backend |
| TC-AC-SU-111 | Assign GM materialize Group Role di group target | Materialisasi role assignment di tingkat database backend |
| TC-AC-SU-113 | Mutual-exclusive Total Control/Read Only vs Group Manager | Validasi constraint entitas di backend API validator |
| TC-AC-SU-115 | Remove GM otomatis saat Group dihapus | Database cascade trigger penghapusan group di Settings > Group |
| TC-AC-SU-118 | Sumber baris Pending Approvals target user | Resolusi query backend untuk approver eligibility |
| TC-AC-SU-125 | 1 write tersinkronisasi ke modal dan tab | Integritas database single source of truth |
| TC-AC-SU-136 | System Log per-app tidak dikonsolidasikan | Isolasi scoping database per aplikasi backend |
| TC-AC-SU-142..149 | Logging 6-Surface Sync (8 TC) | Komitmen transaksi atomik database 6 surface logging |
| TC-AC-SU-152 | 1 email = 1 akun = 1 entitas | Model constraint level database backend |
| TC-AC-SU-175 | Bulk Activate/Deactivate partial commit | Logika commit parsial transaksi database |
| TC-AC-SU-180 | GS cabut App Access hapus baris user_module_status | Sinkronisasi grant modul pada skema database backend |
| TC-AC-SU-181 | GS guard tidak bisa cabut App Access AC Default User | Guard pencegahan di sisi modul Global Settings |
| TC-AC-SU-182 | GS hapus user cascade hard-delete role tables | Database cascade trigger saat soft-delete user di GS |
| TC-AC-SU-183 | Settings > Group hapus group cascade assignment | Database cascade trigger penghapusan role assignment |
| TC-AC-SU-184 | Onboarding Default User otomatis Total Control | Seeding data inisialisasi entitas baru di backend |
| TC-AC-SU-187 | Schema migration penambahan role di masa depan | Script migrasi database skema platform |
| TC-AC-SU-207 | Auto-Revert TC dipicu dari Role & Permission | Notifikasi trigger event origin Role & Permission |
| TC-AC-SU-213 | Auto-Revert GM multi-group boundary notifikasi | Logika percabangan notifikasi multi-group di backend |
| TC-AC-SU-243 | User Log per-app tidak dikonsolidasikan ke GS | Isolasi scoping database sesi per aplikasi backend |

---

## 3. TC Superseded / Dicabut

- **TC-AC-SU-52:** Superseded (Bulk Resend Confirmation Email dihapus, disamakan dengan GS).
- **TC-AC-SU-92:** Superseded (Model aktor group scope dihapus).
- **TC-AC-SU-140:** Superseded (Session Log digantikan Tab User Log Kategori X).
- **TC-AC-SU-155, 157, 158:** Superseded (Global Role entity-wide, dialog safeguard dihapus).
- **TC-AC-SU-199, 200, 201, 254, 255:** Dicabut (Skenario mobile/responsive dihapus sesuai konvensi web-only).

---

## 4. Rekapitulasi Cakupan Lengkap

- **Total TC Granular Aktif:** 260 TC
- **Total TC Terpetakan ke E2E Specs:** 226 TC (100% dari seluruh TC FE yang dapat diotomasi)
- **Total TC Hanya-BE:** 29 TC (11 TC single + 8 TC Kategori N Logging + 10 TC integrasi data backend)
- **Total TC Superseded/Dicabut:** 11 TC
- **Total Spec E2E:** 53 Spec Atomik Terisolasi Tinggi (1 Suite: `suite-admin-console-user`)
- **Status Linter TestSpectra:** 0 error (`npx spectra lint --strict specs_dummy/AdminConsole/User` lolos 100%)
