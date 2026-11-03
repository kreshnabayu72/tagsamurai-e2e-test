# Coverage E2E — Admin Console > Plans & Licensing > Plans & Features

Sumber: `admin-console/plans-licensing-plans-features/TestCases/tc-plans-licensing-plans-features.md` (810 TC granular aktif) dan `admin-console/plans-licensing-plans-features/TestCases/tc-plans-licensing-plans-features-backend.md` (tidak merujuk satu pun TC granular, tidak dipetakan satu per satu).
Suite: `specs/AdminConsole/PlansLicensingPlansFeatures/`.
Prefix Modul: `AC` + `PF` (`TC-AC-PF-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (224 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default | Screening Plans List Tab Default Sub-tab Active dan Archive serta Urutan Default | FE+BE | 29 | TC-AC-PF-1, TC-AC-PF-2, TC-AC-PF-5, TC-AC-PF-6 |
| TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | Row Action, Kolom Clients, dan Membuka Plan Detail dari Plans List | FE+BE | 45 | TC-AC-PF-9, TC-AC-PF-10, TC-AC-PF-11, TC-AC-PF-12, TC-AC-PF-13, TC-AC-PF-14, TC-AC-PF-15, TC-AC-PF-16 |
| TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | Empty State Genuinely Kosong (Dataset Plan E) pada Plans List dan Tiga Modal Changelog | FE+BE | 34 | TC-AC-PF-19, TC-AC-PF-20, TC-AC-PF-21, TC-AC-PF-22, TC-AC-PF-23, TC-AC-PF-493, TC-AC-PF-519, TC-AC-PF-678 |
| TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | Loading State Tabel Plans List, Tab Assigned Clients, dan Tiga Modal Changelog | FE+BE | 37 | TC-AC-PF-17, TC-AC-PF-684, TC-AC-PF-685, TC-AC-PF-686, TC-AC-PF-687 |
| TC-AC-PF-E2E-005-plan-detail-header-info-plan-dan-badge-archived | Plan Detail: Header, Info Plan, Tab, dan Badge Archived | FE+BE | 27 | TC-AC-PF-25, TC-AC-PF-26, TC-AC-PF-27 |
| TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type | Plan Detail Tab Overview: Feature Matrix per Product dan Pricing Type | FE+BE | 24 | TC-AC-PF-32, TC-AC-PF-33, TC-AC-PF-34, TC-AC-PF-35 |
| TC-AC-PF-E2E-007-breadcrumb-plan-detail-tab-default-sub-tab-active-dan-archive | Breadcrumb Plan Detail Tab Default Sub-tab Active dan Archive | FE+BE | 29 | TC-AC-PF-28, TC-AC-PF-29 |
| TC-AC-PF-E2E-008-breadcrumb-plan-detail-tab-custom-sub-tab-active-dan-archive | Breadcrumb Plan Detail Tab Custom Sub-tab Active dan Archive | FE+BE | 30 | TC-AC-PF-30, TC-AC-PF-31 |
| TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | Navigasi Tab dan Sub-tab: Redirect, Refresh, Back, State Sub-tab, dan Klik Segmen Breadcrumb | FE+BE | 42 | TC-AC-PF-36, TC-AC-PF-37, TC-AC-PF-38, TC-AC-PF-39, TC-AC-PF-612 |
| TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar | Preservasi State List saat Kembali dari Plan Detail, Refresh, dan Reset Lewat Sidebar (Dataset 120 Custom Plan) | FE+BE | 38 | TC-AC-PF-40, TC-AC-PF-41, TC-AC-PF-42, TC-AC-PF-43 |
| TC-AC-PF-E2E-011-isolasi-state-halaman-dan-filter-antar-sub-tab-active-dan-archive-tab-default | Isolasi State Halaman dan Filter antar Sub-tab Active dan Archive Tab Default | FE+BE | 14 | TC-AC-PF-708, TC-AC-PF-709 |
| TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1 | Isolasi State Halaman dan Filter Tab Default vs Custom serta Reset Halaman ke 1 (Volume 120 Plan) | FE+BE | 31 | TC-AC-PF-710, TC-AC-PF-711, TC-AC-PF-712, TC-AC-PF-713 |
| TC-AC-PF-E2E-013-konkurensi-dua-admin-create-custom-default-plan-bersamaan-dan-ceiling-paid | Konkurensi Dua Admin: Create Custom Plan dan Default Plan Bersamaan serta Ceiling Paid | FE+BE | 36 | TC-AC-PF-587, TC-AC-PF-588, TC-AC-PF-589 |
| TC-AC-PF-E2E-014-konkurensi-edit-vs-edit-dan-save-global-settings-bersamaan | Konkurensi Edit vs Edit Custom dan Default Plan serta Save Global Settings Bersamaan (Last-Write-Wins) | FE+BE | 44 | TC-AC-PF-590, TC-AC-PF-591, TC-AC-PF-592 |
| TC-AC-PF-E2E-015-konkurensi-archive-dan-retry-archive-oleh-sesi-lain-edit-plan-yang-di-archive | Konkurensi Archive: Client Baru Ter-assign, Retry Archive, dan Edit Plan yang Di-archive Sesi Lain | FE+BE | 41 | TC-AC-PF-593, TC-AC-PF-594, TC-AC-PF-598 |
| TC-AC-PF-E2E-016-konkurensi-retry-delete-plan-name-diklik-setelah-plan-dihapus-sesi-lain | Konkurensi Delete: Retry Delete Custom dan Default Plan serta Plan Name Diklik Setelah Plan Dihapus Sesi Lain | FE+BE | 38 | TC-AC-PF-595, TC-AC-PF-596, TC-AC-PF-781 |
| TC-AC-PF-E2E-017-konkurensi-push-update-ke-client-terbaru-dan-template-di-archive-sesi-lain | Konkurensi: Template Di-archive Sesudah Form Create Dibuka dan Push Update ke Client yang Sudah Terbaru | FE+BE | 37 | TC-AC-PF-597, TC-AC-PF-599 |
| TC-AC-PF-E2E-018-aksesibilitas-aria-required-form-create-custom-plan | Aksesibilitas: Field Wajib Form Create Custom Plan Memiliki aria-required | FE+BE | 6 | TC-AC-PF-787 |
| TC-AC-PF-E2E-019-aksesibilitas-aria-required-form-edit-custom-plan-dan-edit-default-plan | Aksesibilitas: Field Wajib Form Edit Custom Plan dan Edit Default Plan Memiliki aria-required | FE+BE | 6 | TC-AC-PF-789 |
| TC-AC-PF-E2E-020-aksesibilitas-aria-required-form-create-default-plan-dan-tab-global-settings | Aksesibilitas: Field Wajib Form Create Default Plan dan Tab Global Settings Memiliki aria-required | FE+BE | 11 | TC-AC-PF-788, TC-AC-PF-790 |
| TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon | Aksesibilitas: aria-describedby Pesan Error Form Create dan Global Settings serta Nama Aksesibel Ikon Tanpa Teks | FE+BE | 47 | TC-AC-PF-791, TC-AC-PF-792, TC-AC-PF-793, TC-AC-PF-798 |
| TC-AC-PF-E2E-022-aksesibilitas-focus-trap-dialog-archive-delete-dan-cannot-archive-plan | Aksesibilitas: Focus Trap Dialog Archive Plan, Delete Plan, dan Cannot Archive Plan | FE+BE | 28 | TC-AC-PF-794, TC-AC-PF-795 |
| TC-AC-PF-E2E-023-aksesibilitas-focus-trap-dialog-push-plan-update-dan-unsaved-changes | Aksesibilitas: Focus Trap Dialog Push Plan Update dan Unsaved Changes | FE+BE | 26 | TC-AC-PF-796, TC-AC-PF-797 |
| TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default | Screening Plans List Tab Custom Sub-tab Active dan Archive serta Urutan Default | FE+BE | 25 | TC-AC-PF-3, TC-AC-PF-4, TC-AC-PF-7, TC-AC-PF-8 |
| TC-AC-PF-E2E-025-konkurensi-capability-dicabut-dan-entitas-suspended-saat-form-dialog-terbuka | Konkurensi: Capability Update Dicabut Saat Form Edit Terbuka dan Entitas Distributor Suspended Saat Dialog Archive Terbuka | FE+BE | 30 | TC-AC-PF-567, TC-AC-PF-79 |
| TC-AC-PF-E2E-026-guided-tooltip-tur-empat-step-skip-dan-back | Guided Tooltip - Tur Empat Step, Skip, dan Back | FE+BE | 33 | TC-AC-PF-44, TC-AC-PF-45, TC-AC-PF-46 |
| TC-AC-PF-E2E-027-guided-tooltip-replay-navigasi-resize-kolom-clients | Guided Tooltip - Replay Tombol [?], Navigasi, Resize, dan Kolom Clients Disembunyikan | FE+BE | 31 | TC-AC-PF-47, TC-AC-PF-48, TC-AC-PF-49 |
| TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | Role Matrix - Visibilitas Menu Sidebar dan Akses Langsung ke URL Plans & Features | FE+BE | 35 | TC-AC-PF-50, TC-AC-PF-51, TC-AC-PF-52, TC-AC-PF-53, TC-AC-PF-54, TC-AC-PF-55, TC-AC-PF-56 |
| TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan | Role Matrix - UI Visibility Principal Total Control dan Default User | FE+BE | 37 | TC-AC-PF-57, TC-AC-PF-58, TC-AC-PF-59, TC-AC-PF-78 |
| TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | Role Matrix - UI Visibility Principal Read Only, Create-Only, Update-Only, dan Delete-Only | FE+BE | 45 | TC-AC-PF-60, TC-AC-PF-61, TC-AC-PF-62, TC-AC-PF-63, TC-AC-PF-64 |
| TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | Role Matrix - UI Visibility Total Control Distributor dan Total Control Partner | FE+BE | 34 | TC-AC-PF-65, TC-AC-PF-66, TC-AC-PF-67, TC-AC-PF-68, TC-AC-PF-69 |
| TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | Role Matrix - UI Visibility Distributor dan Partner Read Only, Create-Only, Update-Only, dan Delete-Only | FE+BE | 49 | TC-AC-PF-70, TC-AC-PF-71, TC-AC-PF-72, TC-AC-PF-73, TC-AC-PF-74 |
| TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | Gate Status Entitas - Aktor Distributor Suspended, Partner Expired, dan Client Suspended pada Aksi Tulis | FE+BE | 35 | TC-AC-PF-24, TC-AC-PF-75, TC-AC-PF-76, TC-AC-PF-77, TC-AC-PF-281 |
| TC-AC-PF-E2E-034-capability-tunggal-principal-create-only-membuat-custom | Capability Tunggal Principal Create-Only - Membuat Custom Plan dan Default Plan | FE+BE | 17 | TC-AC-PF-80, TC-AC-PF-84 |
| TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push | Capability Tunggal Principal Update-Only - Edit Custom Plan, Rename Default Plan, Push Update, dan Save Global Settings | FE+BE | 34 | TC-AC-PF-81, TC-AC-PF-85, TC-AC-PF-88, TC-AC-PF-89 |
| TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan | Capability Tunggal Principal Delete-Only - Archive dan Delete Custom Plan dan Default Plan | FE+BE | 31 | TC-AC-PF-82, TC-AC-PF-83, TC-AC-PF-86, TC-AC-PF-87 |
| TC-AC-PF-E2E-037-capability-tunggal-distributor-create-only-update-only | Capability Tunggal Distributor - Create-Only, Update-Only, dan Delete-Only pada Custom Plan Milik Sendiri | FE+BE | 24 | TC-AC-PF-90, TC-AC-PF-91, TC-AC-PF-92 |
| TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | Row Scope Data per Entitas - Principal, Distributor, dan Partner | FE+BE | 34 | TC-AC-PF-93, TC-AC-PF-94, TC-AC-PF-95, TC-AC-PF-96, TC-AC-PF-97, TC-AC-PF-98 |
| TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | Masking Assigned Clients per Baris Group Role - Zero Access, Read Only, CRUD, dan Hak Parsial | FE+BE | 28 | TC-AC-PF-99, TC-AC-PF-100, TC-AC-PF-101, TC-AC-PF-102, TC-AC-PF-103, TC-AC-PF-106 |
| TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | Masking Assigned Clients - Total Control, Read Only Account-Wide, Dialog Cannot Archive Plan, Download, dan Navigasi Client Detail | FE+BE | 34 | TC-AC-PF-104, TC-AC-PF-105, TC-AC-PF-107, TC-AC-PF-108, TC-AC-PF-109 |
| TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | Tampilan List - Plan Name 120 Karakter, Tanpa Back to dan Page Title, serta Baris Archive Tanpa Muted | FE+BE | 38 | TC-AC-PF-603, TC-AC-PF-726, TC-AC-PF-727, TC-AC-PF-728, TC-AC-PF-729, TC-AC-PF-749, TC-AC-PF-750 |
| TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab | Tooltip Ikon Toolbar Plans List per Tab dan Sub-tab | FE+BE | 26 | TC-AC-PF-692, TC-AC-PF-693, TC-AC-PF-694, TC-AC-PF-695 |
| TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog | Tooltip Ikon Filter Tab Assigned Clients dan Ikon Toolbar Tiga Modal Changelog | FE+BE | 27 | TC-AC-PF-696, TC-AC-PF-697, TC-AC-PF-698, TC-AC-PF-699 |
| TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | Plan Name sebagai Tautan - Tab Baru, Klik Area Baris, Drag-Select, Keyboard, dan Klik Ganda | FE+BE | 35 | TC-AC-PF-777, TC-AC-PF-778, TC-AC-PF-779, TC-AC-PF-780, TC-AC-PF-782 |
| TC-AC-PF-E2E-045-guided-tooltip-indikator-step-keyboard-dan-penutupan-overlay | Guided Tooltip - Indikator Step, Keyboard, Penutupan Lewat Overlay dan Esc | FE+BE | 21 | TC-AC-PF-645 |
| TC-AC-PF-E2E-046-tooltip-keyboard-focus-dan-wrap-teks-panjang | Tooltip Dapat Diakses Lewat Keyboard Focus dan Teks Panjang Wrap pada Lebar Maksimum 400px | FE+BE | 22 | TC-AC-PF-644 |
| TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | Screening Form Create Custom Plan, Dropdown Product, dan Template | FE+BE | 32 | TC-AC-PF-110, TC-AC-PF-123, TC-AC-PF-124, TC-AC-PF-125, TC-AC-PF-126 |
| TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template | Validasi Required Create Custom Plan: Plan Name, Product, dan Template | FE+BE | 26 | TC-AC-PF-111, TC-AC-PF-112, TC-AC-PF-113, TC-AC-PF-127 |
| TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | Plan Name Create Custom Plan: Batas Panjang, Trim, Emoji, dan Fallback Server | FE+BE | 28 | TC-AC-PF-114, TC-AC-PF-115, TC-AC-PF-116, TC-AC-PF-121, TC-AC-PF-122 |
| TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan | Keunikan Plan Name Create Custom Plan | FE+BE | 26 | TC-AC-PF-117, TC-AC-PF-118, TC-AC-PF-119, TC-AC-PF-120 |
| TC-AC-PF-E2E-051-pemilihan-template-mengisi-capacity-binary-feature-suites | Pemilihan Template Mengisi Capacity, Binary, Feature Suites, dan Opsi Dropdown | FE+BE | 32 | TC-AC-PF-128, TC-AC-PF-129 |
| TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom | Open API dan API Call Quota Create Custom Plan: Kunci, Wajib, dan Batas Custom | FE+BE | 29 | TC-AC-PF-130, TC-AC-PF-131, TC-AC-PF-132, TC-AC-PF-133 |
| TC-AC-PF-E2E-053-api-call-quota-custom-spinner-kelipatan-dan-awalan-preset | API Call Quota Custom: Spinner, Nilai Bukan Kelipatan, dan Awalan Nilai Preset | FE+BE | 32 | TC-AC-PF-134, TC-AC-PF-135, TC-AC-PF-746 |
| TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | Dependency D-2 dan D-4 pada Create Custom Plan | FE+BE | 34 | TC-AC-PF-136, TC-AC-PF-137, TC-AC-PF-138, TC-AC-PF-139, TC-AC-PF-140 |
| TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal | Estimated Reference Price dan Estimated Total Create Custom Plan oleh Principal | FE+BE | 33 | TC-AC-PF-141, TC-AC-PF-142, TC-AC-PF-144, TC-AC-PF-145 |
| TC-AC-PF-E2E-056-estimated-reference-price-edit-custom-plan-serta-create-dan-edit-default-plan | Estimated Reference Price pada Edit Custom Plan serta Create dan Edit Default Plan | FE+BE | 30 | TC-AC-PF-217, TC-AC-PF-609, TC-AC-PF-610 |
| TC-AC-PF-E2E-057-submit-create-custom-plan-oleh-principal-dan-nilai-hasil-ubah-dari-template | Submit Create Custom Plan oleh Principal dan Nilai Hasil Ubah dari Template | FE+BE | 24 | TC-AC-PF-146, TC-AC-PF-149 |
| TC-AC-PF-E2E-058-create-custom-plan-product-sams-dan-siem-memakai-payload-fitur-fams | Create Custom Plan Product SAMS dan SIEM Memakai Payload Fitur FAMS | FE+BE | 18 | TC-AC-PF-150, TC-AC-PF-151 |
| TC-AC-PF-E2E-059-submit-create-custom-plan-oleh-distributor-dan-partner | Submit Create Custom Plan oleh Distributor dan Partner | FE+BE | 29 | TC-AC-PF-147, TC-AC-PF-148 |
| TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan | Submit Create: State Submitting dan Klik Ganda Cepat pada Custom dan Default Plan | FE+BE | 32 | TC-AC-PF-162, TC-AC-PF-163, TC-AC-PF-194, TC-AC-PF-700 |
| TC-AC-PF-E2E-061-clear-field-create-custom-plan | Clear Field Create Custom Plan | FE+BE | 22 | TC-AC-PF-153, TC-AC-PF-154, TC-AC-PF-618 |
| TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | Unsaved Changes Create Custom Plan: Breadcrumb, Sidebar, Back, dan Form Bersih | FE+BE | 24 | TC-AC-PF-155, TC-AC-PF-156, TC-AC-PF-157, TC-AC-PF-158, TC-AC-PF-159 |
| TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | Create Plan: Form Identik, F5, Auto-Focus, Enter, dan Esc | FE+BE | 32 | TC-AC-PF-160, TC-AC-PF-161, TC-AC-PF-704, TC-AC-PF-731, TC-AC-PF-736, TC-AC-PF-741 |
| TC-AC-PF-E2E-064-estimated-reference-price-create-custom-plan-aktor-distributor-sell-reference-price | Estimated Reference Price Create Custom Plan oleh Distributor Memakai Sell Reference Price Wallet | FE+BE | 8 | TC-AC-PF-143 |
| TC-AC-PF-E2E-065-template-tidak-disimpan-sebagai-relasi-perubahan-default-plan-tidak-mengubah-custom | Template Tidak Disimpan sebagai Relasi: Perubahan Default Plan Tidak Mengubah Custom Plan | FE+BE | 15 | TC-AC-PF-152 |
| TC-AC-PF-E2E-066-screening-form-create-default-plan-dan-nilai-awal | Screening Form Create Default Plan dan Nilai Awal | FE+BE | 30 | TC-AC-PF-166, TC-AC-PF-167, TC-AC-PF-168 |
| TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan | Pricing Type Create Default Plan: Radio Tersaring dan Helper Text | FE+BE | 23 | TC-AC-PF-173, TC-AC-PF-174, TC-AC-PF-175, TC-AC-PF-176 |
| TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | Asset Cap Create Default Plan: Kondisi Muncul dan Validasi | FE+BE | 31 | TC-AC-PF-177, TC-AC-PF-178, TC-AC-PF-179, TC-AC-PF-180, TC-AC-PF-181 |
| TC-AC-PF-E2E-069-asset-cap-0-dan-feature-suites-free-terkunci-pada-create | Asset Cap 0 dan Feature Suites Free Terkunci pada Create Default Plan | FE+BE | 17 | TC-AC-PF-182, TC-AC-PF-183 |
| TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120 | Plan Name Create Default Plan: Validasi Kosong, Emoji, Keunikan, dan Batas 120 Karakter | FE+BE | 28 | TC-AC-PF-169, TC-AC-PF-170, TC-AC-PF-171, TC-AC-PF-614 |
| TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template | Submit Sukses Create Default Plan: Tier, Ceiling Paid, dan Template | FE+BE | 34 | TC-AC-PF-185, TC-AC-PF-186, TC-AC-PF-188, TC-AC-PF-189 |
| TC-AC-PF-E2E-072-clear-field-dan-unsaved-changes-dasar-create-default-plan | Clear Field dan Unsaved Changes Dasar pada Create Default Plan | FE+BE | 34 | TC-AC-PF-190, TC-AC-PF-191, TC-AC-PF-643 |
| TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | Unsaved Changes, Auto-Focus, Enter, dan Esc pada Create Default Plan | FE+BE | 33 | TC-AC-PF-668, TC-AC-PF-671, TC-AC-PF-732, TC-AC-PF-737, TC-AC-PF-742 |
| TC-AC-PF-E2E-074-create-default-plan-open-api-off-dan-open-api-on-dengan | Create Default Plan: Open API OFF Mengunci API Call Quota dan Open API ON Tanpa Quota Ditolak | FE+BE | 28 | TC-AC-PF-751, TC-AC-PF-752 |
| TC-AC-PF-E2E-075-create-default-plan-batas-api-call-quota-dan-dependency-d | Create Default Plan: Batas Custom API Call Quota dan Dependency D-2 dan D-4 | FE+BE | 34 | TC-AC-PF-753, TC-AC-PF-754 |
| TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama | Submit Sukses Create Default Plan: Free FAMS, Nama Ter-trim, dan Nama Sama Lintas Product | FE+BE | 31 | TC-AC-PF-172, TC-AC-PF-184, TC-AC-PF-187, TC-AC-PF-613 |
| TC-AC-PF-E2E-077-form-bersih-dan-refresh-create-default-plan | Form Create Default Plan Bersih Tanpa Dialog dan Refresh F5 saat Dirty | FE+BE | 15 | TC-AC-PF-192, TC-AC-PF-664 |
| TC-AC-PF-E2E-078-screening-dan-akses-form-edit-custom-plan | Screening dan Akses Form Edit Custom Plan | FE+BE | 34 | TC-AC-PF-195, TC-AC-PF-196, TC-AC-PF-733 |
| TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | Plan Name Edit Custom Plan: Validasi, Keunikan, Trim, dan Emoji | FE+BE | 37 | TC-AC-PF-197, TC-AC-PF-198, TC-AC-PF-199, TC-AC-PF-200, TC-AC-PF-201, TC-AC-PF-202 |
| TC-AC-PF-E2E-080-edit-custom-plan-edit-nilai-fitur-dan-versi | Edit Custom Plan: Edit Nilai Fitur, Rename, dan Versi | FE+BE | 38 | TC-AC-PF-203, TC-AC-PF-204, TC-AC-PF-205 |
| TC-AC-PF-E2E-081-edit-custom-plan-no-op-kapitalisasi-nilai-turun | Edit Custom Plan: No-Op, Kapitalisasi Nama, dan Nilai Turun | FE+BE | 30 | TC-AC-PF-206, TC-AC-PF-207, TC-AC-PF-208 |
| TC-AC-PF-E2E-082-edit-custom-plan-dependency-d-2-open-api-off-open-api-on | Edit Custom Plan: Dependency D-2, Open API OFF, dan Open API ON Tanpa Quota | FE+BE | 31 | TC-AC-PF-209, TC-AC-PF-210, TC-AC-PF-211 |
| TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes | Edit Custom Plan: Clear Field dan Unsaved Changes | FE+BE | 38 | TC-AC-PF-212, TC-AC-PF-213, TC-AC-PF-214, TC-AC-PF-660 |
| TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | Edit Custom Plan: Refresh F5, Sidebar, Back Browser, dan Esc | FE+BE | 36 | TC-AC-PF-665, TC-AC-PF-669, TC-AC-PF-672, TC-AC-PF-738, TC-AC-PF-743 |
| TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda | Edit Custom dan Default Plan: State Submitting dan Klik Ganda pada Save | FE+BE | 42 | TC-AC-PF-216, TC-AC-PF-608, TC-AC-PF-701, TC-AC-PF-702 |
| TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | Screening Form Edit Default Plan: Free, Paid, Feature Suites, dan Fokus | FE+BE | 35 | TC-AC-PF-218, TC-AC-PF-219, TC-AC-PF-228, TC-AC-PF-232, TC-AC-PF-734 |
| TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | Plan Name Edit Default Plan: Validasi, Keunikan, Batas Karakter, dan Trim | FE+BE | 39 | TC-AC-PF-220, TC-AC-PF-221, TC-AC-PF-615, TC-AC-PF-616, TC-AC-PF-617 |
| TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified | Edit Default Plan: Nilai Fitur, Rename, No-Op, dan Last Modified | FE+BE | 33 | TC-AC-PF-222, TC-AC-PF-230, TC-AC-PF-231, TC-AC-PF-236 |
| TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free | Validasi Asset cap Edit Default Plan Free | FE+BE | 20 | TC-AC-PF-224, TC-AC-PF-225, TC-AC-PF-226, TC-AC-PF-227 |
| TC-AC-PF-E2E-090-edit-default-plan-open-api-off-on-dan-dependency-d-2-d-4 | Edit Default Plan: Open API OFF dan ON serta Dependency D-2 dan D-4 | FE+BE | 40 | TC-AC-PF-756, TC-AC-PF-757, TC-AC-PF-758 |
| TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5 | Edit Default Plan: Clear Field dan Dialog Unsaved Changes | FE+BE | 36 | TC-AC-PF-233, TC-AC-PF-234, TC-AC-PF-661, TC-AC-PF-663 |
| TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | Edit Default Plan: Refresh F5, Sidebar, Back Browser, dan Esc | FE+BE | 35 | TC-AC-PF-666, TC-AC-PF-670, TC-AC-PF-673, TC-AC-PF-739, TC-AC-PF-744 |
| TC-AC-PF-E2E-093-edit-api-call-quota-custom-bernilai-sama-dengan-preset | Edit Custom Plan: API call quota Custom Bernilai Sama dengan Preset | FE+BE | 26 | TC-AC-PF-648 |
| TC-AC-PF-E2E-094-edit-default-plan-api-call-quota-custom-sama-dengan-preset-dan-format-changelog | Edit Default Plan Growth: API call quota Custom Sama dengan Preset dan Format Nilai Changelog | FE+BE | 29 | TC-AC-PF-649 |
| TC-AC-PF-E2E-095-edit-default-plan-asset-cap-free-dan-product-siem | Edit Default Plan: Asset cap Free dan Product SIEM | FE+BE | 21 | TC-AC-PF-223, TC-AC-PF-229 |
| TC-AC-PF-E2E-096-dialog-archive-plan-screening-dan-cancel-custom-dan-default | Dialog Archive Plan: Screening dan Cancel pada Custom Plan dan Default Plan | FE+BE | 29 | TC-AC-PF-237, TC-AC-PF-238, TC-AC-PF-239 |
| TC-AC-PF-E2E-097-archive-custom-plan-sukses-header-plan-detail-klik-ganda | Archive Custom Plan: Sukses dari Row Action, Header Plan Detail, dan Klik Ganda | FE+BE | 38 | TC-AC-PF-240, TC-AC-PF-253, TC-AC-PF-675 |
| TC-AC-PF-E2E-098-archive-default-plan-pergeseran-tier | Archive Default Plan: Pergeseran Tier saat Archive Plan Free dan Paid Tengah | FE+BE | 32 | TC-AC-PF-241, TC-AC-PF-242 |
| TC-AC-PF-E2E-099-archive-default-plan-header-plan-detail-plan-terakhir | Archive Default Plan: Header Plan Detail, Plan Terakhir, dan Template dengan Custom Plan Turunan | FE+BE | 50 | TC-AC-PF-254, TC-AC-PF-730, TC-AC-PF-764 |
| TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace | Guard Cannot Archive Plan: Subscription Waiting for Approval, Pending, Active, dan Grace | FE+BE | 38 | TC-AC-PF-246, TC-AC-PF-247, TC-AC-PF-248, TC-AC-PF-249 |
| TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar | Guard Cannot Archive Plan: Status yang Tidak Menahan, Daftar Banyak Client, dan Dialog Backdrop | FE+BE | 38 | TC-AC-PF-250, TC-AC-PF-251, TC-AC-PF-252, TC-AC-PF-706 |
| TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | Dialog Delete Plan: Screening, Cancel, Guard Plan yang Pernah Dipakai, dan Row Action Plan Active | FE+BE | 42 | TC-AC-PF-256, TC-AC-PF-257, TC-AC-PF-260, TC-AC-PF-261, TC-AC-PF-263, TC-AC-PF-607 |
| TC-AC-PF-E2E-103-delete-plan-archived-sukses-klik-ganda-bekas-template | Delete Plan Archived: Sukses, Nama Dibebaskan, dan Klik Ganda | FE+BE | 34 | TC-AC-PF-258, TC-AC-PF-259, TC-AC-PF-676 |
| TC-AC-PF-E2E-104-delete-plan-archived-yang-seluruh-term-nya-deleted | Delete Plan Archived yang Seluruh Term-nya Deleted | FE+BE | 26 | TC-AC-PF-799 |
| TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain | Push Update: Eligibilitas Client Berdasarkan Status Subscription dan Versi | FE+BE | 35 | TC-AC-PF-264, TC-AC-PF-265, TC-AC-PF-266, TC-AC-PF-267 |
| TC-AC-PF-E2E-106-push-update-delta-downgrade-per-client-delta-net-kosong | Push Update: Delta Downgrade, Eligibilitas per Client, dan Delta Net Kosong | FE+BE | 24 | TC-AC-PF-268, TC-AC-PF-269, TC-AC-PF-270 |
| TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi | Push Update: Teks Jumlah Client Outdated dan Ketiadaan Aksi Massal | FE+BE | 24 | TC-AC-PF-271, TC-AC-PF-272, TC-AC-PF-282, TC-AC-PF-283 |
| TC-AC-PF-E2E-108-push-update-kepemilikan-principal-dan-distributor | Push Update: Kepemilikan Principal dan Distributor | FE+BE | 20 | TC-AC-PF-273, TC-AC-PF-274 |
| TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel | Dialog Push Plan Update: Screening, Tabel Diff, Cancel, Backdrop, dan Esc | FE+BE | 40 | TC-AC-PF-275, TC-AC-PF-276, TC-AC-PF-277, TC-AC-PF-705 |
| TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda | Confirm Push Update: Sukses, Plan Free, Tabel Diff API Call Quota, dan Klik Ganda | FE+BE | 50 | TC-AC-PF-278, TC-AC-PF-279, TC-AC-PF-650, TC-AC-PF-677 |
| TC-AC-PF-E2E-111-archive-default-plan-tier-tertinggi-terendah-dan-last-modified-tergeser | Archive Default Plan: Tier Tertinggi, Tier Terendah, dan Last Modified Plan yang Tergeser | FE+BE | 37 | TC-AC-PF-243, TC-AC-PF-244, TC-AC-PF-245 |
| TC-AC-PF-E2E-112-delete-default-plan-archived-bekas-template-custom-turunan-tidak-berubah | Delete Default Plan Archived Bekas Template: Custom Plan Turunan Tidak Berubah | FE+BE | 20 | TC-AC-PF-765 |
| TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | Global Settings: Screening Tab dan Validasi Angka Max custom fields dan Max depreciation methods | FE+BE | 32 | TC-AC-PF-284, TC-AC-PF-285, TC-AC-PF-286, TC-AC-PF-287, TC-AC-PF-288, TC-AC-PF-289 |
| TC-AC-PF-E2E-114-global-settings-nilai-kosong-dan-clear-field-dengan-error | Global Settings: Nilai Kosong Ditolak dan Clear Field Menghapus Pesan Error | FE+BE | 36 | TC-AC-PF-637, TC-AC-PF-638, TC-AC-PF-662 |
| TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op | Global Settings: Save Berhasil Per Setting dan Sekaligus serta Save Tanpa Perubahan (No-Op) | FE+BE | 35 | TC-AC-PF-290, TC-AC-PF-291, TC-AC-PF-292, TC-AC-PF-293 |
| TC-AC-PF-E2E-116-global-settings-clear-field-dan-unsaved-changes-pindah-tab-dan-breadcrumb | Global Settings: Clear Field dan Dialog Unsaved Changes Saat Pindah Tab dan Klik Breadcrumb | FE+BE | 30 | TC-AC-PF-294, TC-AC-PF-295, TC-AC-PF-296 |
| TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc | Global Settings: Refresh F5, Tombol Back, dan Esc Saat Form Dirty atau Bersih | FE+BE | 27 | TC-AC-PF-667, TC-AC-PF-674, TC-AC-PF-740, TC-AC-PF-745 |
| TC-AC-PF-E2E-118-global-settings-auto-focus-enter-dan-unsaved-changes-sesudah-save | Global Settings: Auto-Focus, Enter Tidak Men-Submit, dan Unsaved Changes Sesudah Save atau Pengembalian Nilai | FE+BE | 25 | TC-AC-PF-735, TC-AC-PF-762, TC-AC-PF-763 |
| TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | Format Tanggal, Time Format 12-hour, dan Time Zone General Settings pada List, Assigned Clients, dan Changelog | FE+BE | 28 | TC-AC-PF-549, TC-AC-PF-767, TC-AC-PF-768, TC-AC-PF-769, TC-AC-PF-770 |
| TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | Kotak Input Date Range Filter Panel Mengikuti Date Format General Settings pada Enam Surface | FE+BE | 45 | TC-AC-PF-771, TC-AC-PF-772, TC-AC-PF-773, TC-AC-PF-774, TC-AC-PF-775, TC-AC-PF-776 |
| TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | Isi Entri Changelog: Create Custom dan Default Plan, Edit Satu atau Beberapa Field, serta Rename | FE+BE | 60 | TC-AC-PF-520, TC-AC-PF-521, TC-AC-PF-522, TC-AC-PF-523, TC-AC-PF-524 |
| TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | Isi Entri Changelog: Archive, Delete, dan Push Update | FE+BE | 48 | TC-AC-PF-525, TC-AC-PF-526, TC-AC-PF-527, TC-AC-PF-528, TC-AC-PF-530 |
| TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan | Snapshot Changelog: Entri Tetap Terbaca Sesudah Plan Dihapus atau Akun Dihapus, Rename Dua Kali, dan Dua Edit Beruntun | FE+BE | 48 | TC-AC-PF-529, TC-AC-PF-539, TC-AC-PF-540, TC-AC-PF-541 |
| TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | System Log Aktor dan Activity Log untuk Aksi Plan dan Global Settings serta Konsistensi Tiga Surface | FE+BE | 48 | TC-AC-PF-532, TC-AC-PF-533, TC-AC-PF-534, TC-AC-PF-535, TC-AC-PF-536, TC-AC-PF-537 |
| TC-AC-PF-E2E-125-aksi-ditolak-tidak-menulis-entri-log-di-surface-mana-pun | Absence Log: Aksi yang Ditolak Validasi atau Guard Tidak Menulis Entri di Changelog, Activity Log, dan System Log | FE+BE | 23 | TC-AC-PF-538 |
| TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | Efek Lintas Modul ke Allocation: Dropdown Plan Subscription, Versi Grandfathering, Renewal, dan Push Update | FE+BE | 62 | TC-AC-PF-542, TC-AC-PF-543, TC-AC-PF-544, TC-AC-PF-545, TC-AC-PF-546 |
| TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission | Lintas Modul: Cap Custom Field FAMS dan Perubahan Role dan Permission Berlaku pada Pemuatan Berikutnya | FE+BE | 31 | TC-AC-PF-547, TC-AC-PF-548, TC-AC-PF-550, TC-AC-PF-551 |
| TC-AC-PF-E2E-128-global-settings-klik-ganda-save-state-submitting-dan-isi-entri-changelog | Global Settings: Klik Ganda Save, State Submitting, dan Isi Entri Changelog Global Settings | FE+BE | 38 | TC-AC-PF-300, TC-AC-PF-703, TC-AC-PF-531 |
| TC-AC-PF-E2E-129-global-settings-unsaved-changes-klik-menu-sidebar-dan-buka-changelog-saat-dirty | Global Settings: Unsaved Changes Saat Klik Menu Sidebar dan Buka Modal Changelog Saat Form Dirty | FE+BE | 20 | TC-AC-PF-297, TC-AC-PF-298 |
| TC-AC-PF-E2E-130-search-tab-default-active-siklus-trim-tanpa-hasil | Search Tab Default Active Siklus Input, Trim, dan Tanpa Hasil | FE+BE | 30 | TC-AC-PF-301, TC-AC-PF-302, TC-AC-PF-303 |
| TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | Search Tab Default Active Kelas Kolom dan Visibilitas Kolom | FE+BE | 22 | TC-AC-PF-304, TC-AC-PF-305, TC-AC-PF-306, TC-AC-PF-307, TC-AC-PF-308 |
| TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | Filter Tab Default Active Screening, Product, Pricing Type, Clients, dan Last Modified | FE+BE | 33 | TC-AC-PF-309, TC-AC-PF-310, TC-AC-PF-311, TC-AC-PF-312, TC-AC-PF-313, TC-AC-PF-314 |
| TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | Filter Tab Default Active Logika AND, Opsi Distinct, Chip, dan Tutup Panel | FE+BE | 30 | TC-AC-PF-315, TC-AC-PF-316, TC-AC-PF-317, TC-AC-PF-318, TC-AC-PF-319 |
| TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | Filter Tab Default Active Indikator, Kolom Clients Tersembunyi, Tanpa Hasil, dan Alur Search dengan Filter | FE+BE | 34 | TC-AC-PF-320, TC-AC-PF-321, TC-AC-PF-322, TC-AC-PF-323, TC-AC-PF-324 |
| TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | Sort Tab Default Active per Kolom | FE+BE | 34 | TC-AC-PF-325, TC-AC-PF-326, TC-AC-PF-327, TC-AC-PF-328, TC-AC-PF-330 |
| TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active | Kombinasi Search, Filter, Sort, dan Clear Tab Default Active | FE+BE | 22 | TC-AC-PF-329, TC-AC-PF-331, TC-AC-PF-332, TC-AC-PF-333 |
| TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser | Setup Column Tab Default Active Screening, Ceklis, dan Geser Urutan | FE+BE | 34 | TC-AC-PF-335, TC-AC-PF-336, TC-AC-PF-337, TC-AC-PF-338 |
| TC-AC-PF-E2E-138-setup-column-tab-default-active-pin-reset-to-default-tutup | Setup Column Tab Default Active Pin, Reset to Default, dan Tutup Popup | FE+BE | 24 | TC-AC-PF-339, TC-AC-PF-340, TC-AC-PF-341 |
| TC-AC-PF-E2E-139-setup-column-tab-default-active-guard-satu-kolom-batas-pin | Setup Column Tab Default Active Guard Satu Kolom, Batas Pin, dan Independensi Cache | FE+BE | 25 | TC-AC-PF-342, TC-AC-PF-343, TC-AC-PF-344 |
| TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | Pagination Tab Default Active dan Archive Baris Terakhir di Halaman Terakhir | FE+BE | 39 | TC-AC-PF-345, TC-AC-PF-346, TC-AC-PF-347, TC-AC-PF-348, TC-AC-PF-349, TC-AC-PF-641 |
| TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | Download Plans List Tab Default Nama Berkas, Search, Column Visibility, dan Lintas Halaman | FE+BE | 35 | TC-AC-PF-350, TC-AC-PF-353, TC-AC-PF-354, TC-AC-PF-355, TC-AC-PF-361, TC-AC-PF-688 |
| TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | Download Plans List Tab Custom Nama Berkas, Search, Column Visibility, dan Hasil Kosong | FE+BE | 31 | TC-AC-PF-365, TC-AC-PF-401, TC-AC-PF-404, TC-AC-PF-405, TC-AC-PF-406 |
| TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | Isi Berkas Download Plans List Tab Default BOM, Sheet, Tipe Sel, dan Format Tanggal | FE+BE | 28 | TC-AC-PF-351, TC-AC-PF-352, TC-AC-PF-635, TC-AC-PF-642, TC-AC-PF-766 |
| TC-AC-PF-E2E-144-isi-berkas-download-plans-list-tab-custom-bom-sheet-kutip | Isi Berkas Download Plans List Tab Custom BOM, Sheet, dan Kutip pada Plan Name | FE+BE | 14 | TC-AC-PF-402, TC-AC-PF-403, TC-AC-PF-715 |
| TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | Search, Filter, dan Sort Sub-tab Archive Default dan Custom | FE+BE | 42 | TC-AC-PF-357, TC-AC-PF-358, TC-AC-PF-359, TC-AC-PF-360, TC-AC-PF-362, TC-AC-PF-363, TC-AC-PF-364, TC-AC-PF-724 |
| TC-AC-PF-E2E-146-search-tab-custom-active-siklus-trim-tanpa-hasil | Search Tab Custom Active Siklus Input, Trim, dan Tanpa Hasil | FE+BE | 31 | TC-AC-PF-366, TC-AC-PF-367, TC-AC-PF-368 |
| TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas | Search Tab Custom Active Kelas Kolom dan Visibilitas Kolom Created By | FE+BE | 26 | TC-AC-PF-369, TC-AC-PF-370, TC-AC-PF-371, TC-AC-PF-372 |
| TC-AC-PF-E2E-148-filter-tab-custom-active | Filter Tab Custom Active | FE+BE | 32 | TC-AC-PF-373, TC-AC-PF-374, TC-AC-PF-375, TC-AC-PF-376, TC-AC-PF-377, TC-AC-PF-378, TC-AC-PF-379 |
| TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol | Sort Tab Custom Active per Kolom | FE+BE | 32 | TC-AC-PF-380, TC-AC-PF-381, TC-AC-PF-382, TC-AC-PF-383 |
| TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser | Setup Column Tab Custom Active Screening, Ceklis, dan Geser Urutan | FE+BE | 39 | TC-AC-PF-384, TC-AC-PF-385, TC-AC-PF-386, TC-AC-PF-387 |
| TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | Setup Column Tab Custom Active Pin, Reset to Default, Tutup Popup, dan Kolom Created By | FE+BE | 34 | TC-AC-PF-388, TC-AC-PF-389, TC-AC-PF-390, TC-AC-PF-393, TC-AC-PF-394 |
| TC-AC-PF-E2E-152-setup-column-tab-custom-active-guard-satu-kolom-dan-batas | Setup Column Tab Custom Active Guard Satu Kolom dan Batas Pin | FE+BE | 19 | TC-AC-PF-391, TC-AC-PF-392 |
| TC-AC-PF-E2E-153-setup-column-default-archive-custom-archive-modal | Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Ceklis, Geser, dan Pin | FE+BE | 21 | TC-AC-PF-622, TC-AC-PF-623, TC-AC-PF-624 |
| TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal | Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom Reset, Tutup, Guard, dan Batas Pin | FE+BE | 38 | TC-AC-PF-625, TC-AC-PF-626, TC-AC-PF-627, TC-AC-PF-628 |
| TC-AC-PF-E2E-155-screening-overlay-dan-popup-setup-column-default-archive | Screening Overlay Column Visibility dan Popup Setup Column Default Archive, Custom Archive, dan Modal Changelog Custom | FE+BE | 30 | TC-AC-PF-630, TC-AC-PF-631 |
| TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | Pagination Tab Custom Active Volume 120 Plan | FE+BE | 35 | TC-AC-PF-395, TC-AC-PF-396, TC-AC-PF-397, TC-AC-PF-398, TC-AC-PF-399, TC-AC-PF-400 |
| TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai | Download Plan Detail Nama Berkas, Baris Kondisional, dan Nilai API Call Quota | FE+BE | 33 | TC-AC-PF-604, TC-AC-PF-605, TC-AC-PF-636, TC-AC-PF-647 |
| TC-AC-PF-E2E-158-create-default-plan-saat-tabel-default-active-terfilter | Create Default Plan Baru Saat Tabel Default Active Masih Terfilter | FE+BE | 8 | TC-AC-PF-334 |
| TC-AC-PF-E2E-159-kombinasi-kontrol-dan-pemulihan-empty-state-tab-custom-active | Kombinasi Kontrol dan Pemulihan Empty State Tab Custom Active | FE+BE | 18 | TC-AC-PF-408, TC-AC-PF-409 |
| TC-AC-PF-E2E-160-screening-tab-assigned-clients-dan-format-sel | Screening Tab Assigned Clients: toolbar, kolom, urutan default, footer, dan format sel | FE+BE | 27 | TC-AC-PF-410, TC-AC-PF-453 |
| TC-AC-PF-E2E-161-search-tab-assigned-clients-siklus-trim-tanpa-hasil | Search Tab Assigned Clients: siklus input, trim spasi, dan tanpa hasil | FE+BE | 33 | TC-AC-PF-411, TC-AC-PF-412, TC-AC-PF-413 |
| TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas | Search Tab Assigned Clients: kelas kolom dan keterikatan pada visibilitas kolom | FE+BE | 23 | TC-AC-PF-414, TC-AC-PF-415, TC-AC-PF-416, TC-AC-PF-417 |
| TC-AC-PF-E2E-163-filter-tab-assigned-clients-screening-subscription-status | Filter Tab Assigned Clients: screening Filter Panel, Subscription Status, Assigned By, dan Plan Version | FE+BE | 21 | TC-AC-PF-418, TC-AC-PF-419, TC-AC-PF-420 |
| TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa | Filter Tab Assigned Clients: Assigned Date inklusif, kombinasi dengan Search, isi opsi dropdown, dan tanpa hasil | FE+BE | 25 | TC-AC-PF-421, TC-AC-PF-422, TC-AC-PF-423, TC-AC-PF-424 |
| TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | Sort Tab Assigned Clients dan warna badge Subscription Status | FE+BE | 33 | TC-AC-PF-425, TC-AC-PF-426, TC-AC-PF-427, TC-AC-PF-428, TC-AC-PF-725 |
| TC-AC-PF-E2E-166-setup-column-tab-assigned-clients-screening-ceklis | Setup Column Tab Assigned Clients: screening overlay dan popup, ceklis kolom | FE+BE | 31 | TC-AC-PF-429, TC-AC-PF-430, TC-AC-PF-431 |
| TC-AC-PF-E2E-167-setup-column-tab-assigned-clients-geser-pin-reset | Setup Column Tab Assigned Clients: geser urutan, Pin dan Unpin, dan Reset to Default | FE+BE | 34 | TC-AC-PF-432, TC-AC-PF-433, TC-AC-PF-434 |
| TC-AC-PF-E2E-168-setup-column-tab-assigned-clients-tutup-guard-batas-pin | Setup Column Tab Assigned Clients: tutup tanpa Save, guard satu kolom, dan batas pin tiga kolom | FE+BE | 34 | TC-AC-PF-435, TC-AC-PF-436, TC-AC-PF-437 |
| TC-AC-PF-E2E-169-pagination-tab-assigned-clients-default-dan-navigasi | Pagination Tab Assigned Clients: default 10 baris, opsi page size, dan navigasi halaman | FE+BE | 18 | TC-AC-PF-439, TC-AC-PF-440 |
| TC-AC-PF-E2E-170-pagination-tab-assigned-clients-nomor-tidak-valid-page | Pagination Tab Assigned Clients: nomor halaman tidak valid, ganti page size, dan reset halaman | FE+BE | 23 | TC-AC-PF-441, TC-AC-PF-442, TC-AC-PF-443 |
| TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column | Download Tab Assigned Clients: nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong | FE+BE | 32 | TC-AC-PF-444, TC-AC-PF-447, TC-AC-PF-448, TC-AC-PF-449 |
| TC-AC-PF-E2E-172-isi-berkas-download-tab-assigned-clients-bom-sheet-plan | Isi berkas Download Tab Assigned Clients: BOM, sheet XLSX, dan format kolom Plan Version | FE+BE | 24 | TC-AC-PF-445, TC-AC-PF-446, TC-AC-PF-639 |
| TC-AC-PF-E2E-173-tab-assigned-clients-term-terminal-term-campuran-term | Tab Assigned Clients: client yang hanya punya term terminal tidak dirender dan tidak dihitung | FE+BE | 21 | TC-AC-PF-633, TC-AC-PF-634 |
| TC-AC-PF-E2E-174-created-by-dan-assigned-by-sebagai-snapshot-saat-akun | Created By dan Assigned By sebagai nilai tersimpan saat akun pembuat atau pemberi tugas dihapus atau dinonaktifkan | FE+BE | 33 | TC-AC-PF-807, TC-AC-PF-808, TC-AC-PF-809 |
| TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail | Tab Assigned Clients: empty state, subscription baru dari Allocation, dan navigasi ke Client Detail | FE+BE | 26 | TC-AC-PF-451, TC-AC-PF-552, TC-AC-PF-611, TC-AC-PF-783 |
| TC-AC-PF-E2E-176-setup-column-tab-assigned-clients-independensi-cache | Setup Column Tab Assigned Clients: cache terpisah dari tabel Plans List | FE+BE | 11 | TC-AC-PF-438 |
| TC-AC-PF-E2E-177-tab-assigned-clients-term-campuran-dan-term-trial | Tab Assigned Clients: client bertermin campuran dan term Trial | FE+BE | 35 | TC-AC-PF-640, TC-AC-PF-747, TC-AC-PF-748 |
| TC-AC-PF-E2E-178-modal-changelog-default-buka-screening-tutup | Modal Changelog Default dibuka dari sub-tab Active dan Archive, screening isi modal, dan penutupan lewat icon (X) atau Esc | FE+BE | 29 | TC-AC-PF-454, TC-AC-PF-455, TC-AC-PF-456 |
| TC-AC-PF-E2E-179-modal-changelog-custom-screening-dan-scope-data-per-entitas | Modal Changelog Custom screening isi modal dan hanya memuat log custom plan milik entitas aktor | FE+BE | 22 | TC-AC-PF-495, TC-AC-PF-496 |
| TC-AC-PF-E2E-180-search-modal-changelog-default-siklus-trim-tanpa-hasil | Search modal Changelog Default siklus interaksi, trim spasi, dan empty state tanpa hasil | FE+BE | 30 | TC-AC-PF-457, TC-AC-PF-458, TC-AC-PF-459 |
| TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas | Search modal Changelog Default per kelas kolom, tidak mencocokkan Date, dan terikat visibilitas kolom | FE+BE | 24 | TC-AC-PF-460, TC-AC-PF-461, TC-AC-PF-462, TC-AC-PF-463 |
| TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select | Filter modal Changelog Default screening Filter Panel, multi-select, dan rentang Date inklusif | FE+BE | 16 | TC-AC-PF-464, TC-AC-PF-465, TC-AC-PF-466, TC-AC-PF-467 |
| TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | Filter modal Changelog Default opsi dropdown, kombinasi Filter AND Search, tanpa hasil, dan chip +N more Modified By | FE+BE | 32 | TC-AC-PF-468, TC-AC-PF-469, TC-AC-PF-470, TC-AC-PF-784, TC-AC-PF-785 |
| TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | Sort modal Changelog Default dan Custom per kolom, tipe campuran, dan nilai kosong | FE+BE | 33 | TC-AC-PF-471, TC-AC-PF-472, TC-AC-PF-473, TC-AC-PF-474, TC-AC-PF-714, TC-AC-PF-810 |
| TC-AC-PF-E2E-185-setup-column-modal-changelog-default-screening-ceklis | Setup Column modal Changelog Default screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom | FE+BE | 28 | TC-AC-PF-475, TC-AC-PF-476, TC-AC-PF-477 |
| TC-AC-PF-E2E-186-setup-column-modal-changelog-default-geser-pin-reset | Setup Column modal Changelog Default geser urutan, Pin dan Unpin, dan Reset to Default | FE+BE | 36 | TC-AC-PF-478, TC-AC-PF-479, TC-AC-PF-480 |
| TC-AC-PF-E2E-187-setup-column-modal-changelog-default-tutup-guard-batas-pin | Setup Column modal Changelog Default tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom | FE+BE | 33 | TC-AC-PF-481, TC-AC-PF-482, TC-AC-PF-483 |
| TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column | Download modal Changelog Default nama berkas, mengikuti Search dan Column Visibility, dan hasil kosong | FE+BE | 34 | TC-AC-PF-486, TC-AC-PF-489, TC-AC-PF-490, TC-AC-PF-491 |
| TC-AC-PF-E2E-189-isi-berkas-download-modal-changelog-default-bom-sheet | Isi berkas Download modal Changelog Default CSV dan XLSX, encoding BOM, nama sheet, dan format sel | FE+BE | 30 | TC-AC-PF-487, TC-AC-PF-488, TC-AC-PF-651 |
| TC-AC-PF-E2E-190-isi-berkas-download-modal-changelog-custom-dan-global | Isi berkas Download modal Changelog Custom dan Global Settings, nilai tersimpan, kolom, dan hasil Filter lintas halaman | FE+BE | 28 | TC-AC-PF-652, TC-AC-PF-653 |
| TC-AC-PF-E2E-191-download-modal-changelog-custom-dan-global-settings-nama | Download modal Changelog Custom dan Global Settings nama berkas dan jumlah baris | FE+BE | 18 | TC-AC-PF-499, TC-AC-PF-517 |
| TC-AC-PF-E2E-192-search-filter-sort-dan-setup-column-modal-changelog-custom | Search, Filter, Sort, dan Setup Column modal Changelog Custom berfungsi sama dengan modal Default | FE+BE | 23 | TC-AC-PF-497, TC-AC-PF-498 |
| TC-AC-PF-E2E-193-search-dan-filter-modal-changelog-custom-per-anggota | Search dan Filter modal Changelog Custom per anggota kolom | FE+BE | 25 | TC-AC-PF-619, TC-AC-PF-620 |
| TC-AC-PF-E2E-194-sort-modal-changelog-custom-per-anggota-dan-search-tanpa | Sort modal Changelog Custom per anggota kolom dan Search tanpa hasil | FE+BE | 16 | TC-AC-PF-621, TC-AC-PF-680 |
| TC-AC-PF-E2E-195-modal-changelog-global-settings-filter-dan-search | Filter dan Search modal Changelog Global Settings per kolom dan rentang Date inklusif | FE+BE | 23 | TC-AC-PF-502, TC-AC-PF-503, TC-AC-PF-504 |
| TC-AC-PF-E2E-196-modal-changelog-global-settings-sort | Sort modal Changelog Global Settings numerik natural, Date, Modified By, Field, dan Action | FE+BE | 22 | TC-AC-PF-505, TC-AC-PF-506, TC-AC-PF-654 |
| TC-AC-PF-E2E-197-setup-column-modal-changelog-global-settings-screening | Setup Column modal Changelog Global Settings screening Overlay Column Visibility, Popup Setup Column, dan ceklis kolom | FE+BE | 30 | TC-AC-PF-507, TC-AC-PF-508, TC-AC-PF-509 |
| TC-AC-PF-E2E-198-setup-column-modal-changelog-global-settings-geser-pin | Setup Column modal Changelog Global Settings Reset to Default, Pin dan Unpin, dan geser urutan kolom | FE+BE | 40 | TC-AC-PF-510, TC-AC-PF-511, TC-AC-PF-512 |
| TC-AC-PF-E2E-199-setup-column-modal-changelog-global-settings-tutup-guard | Setup Column modal Changelog Global Settings tutup popup tanpa Save, guard satu kolom tersisa, dan batas pin tiga kolom | FE+BE | 34 | TC-AC-PF-513, TC-AC-PF-514, TC-AC-PF-515 |
| TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris | Pagination modal Changelog Default dan Download lintas halaman dengan volume 120 baris | FE+BE | 33 | TC-AC-PF-485, TC-AC-PF-689, TC-AC-PF-690, TC-AC-PF-691 |
| TC-AC-PF-E2E-201-ambang-download-modal-changelog-default-5-000-dan-5-001 | Ambang Download modal Changelog Default pada 5.000 dan 5.001 entri | FE+BE | 16 | TC-AC-PF-601, TC-AC-PF-602 |
| TC-AC-PF-E2E-202-pagination-modal-changelog-global-settings-dan-archive | Pagination modal Changelog Global Settings, Default Archive, Custom Archive, dan modal Changelog Custom | FE+BE | 26 | TC-AC-PF-516, TC-AC-PF-629 |
| TC-AC-PF-E2E-203-screening-dan-filter-panel-modal-changelog-global-settings | Screening modal Changelog Global Settings dan Filter Panel tanpa field Action | FE+BE | 21 | TC-AC-PF-500, TC-AC-PF-501 |
| TC-AC-PF-E2E-204-cache-setup-column-independen-dan-esc-berlapis-modal-changelog-default | Cache Setup Column modal Changelog Default independen dari modal Custom dan Global Settings, dan Esc berlapis | FE+BE | 22 | TC-AC-PF-484, TC-AC-PF-707 |
| TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive | Defense-in-depth: Server Menolak Distributor Total Control untuk Create, Edit, Archive, dan Delete Default Plan | FE+BE | 20 | TC-AC-PF-553, TC-AC-PF-554, TC-AC-PF-555, TC-AC-PF-556 |
| TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete | Defense-in-depth: Server Menolak Partner Total Control untuk Create, Edit, Archive, dan Delete Default Plan | FE+BE | 16 | TC-AC-PF-557, TC-AC-PF-656, TC-AC-PF-657, TC-AC-PF-658 |
| TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan | Defense-in-depth: Server Menolak Distributor atas Custom Plan Milik Principal dan Principal atas Custom Plan Milik Distributor | FE+BE | 18 | TC-AC-PF-558, TC-AC-PF-559, TC-AC-PF-560, TC-AC-PF-561 |
| TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca | Defense-in-depth: Server Menolak Aksi Tulis Distributor Suspended, Save Global Settings oleh Read Only dan Distributor, serta Baca Global Settings | FE+BE | 23 | TC-AC-PF-562, TC-AC-PF-563, TC-AC-PF-564, TC-AC-PF-646 |
| TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin | Defense-in-depth: Server Menolak Push Update dan Client Detail Tanpa Izin Group, Filter Pricing Type Custom Diabaikan, dan Payload Script pada Plan Name | FE+BE | 34 | TC-AC-PF-565, TC-AC-PF-566, TC-AC-PF-568, TC-AC-PF-569 |
| TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | Defense-in-depth: Invarian Server Default Plan: Slot Free dan Paid, Posisi Tier, Asset Cap, dan Feature Suites Plan Free | FE+BE | 33 | TC-AC-PF-570, TC-AC-PF-571, TC-AC-PF-572, TC-AC-PF-573, TC-AC-PF-574, TC-AC-PF-575, TC-AC-PF-576, TC-AC-PF-577 |
| TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | Defense-in-depth: Validasi Server Template Custom Plan, Edit Plan Archived, Delete Plan Belum Archived atau Pernah Dipakai | FE+BE | 29 | TC-AC-PF-579, TC-AC-PF-580, TC-AC-PF-581, TC-AC-PF-582, TC-AC-PF-583, TC-AC-PF-800 |
| TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | Defense-in-depth: Validasi Server API Call Quota dan Open API pada Create dan Edit Plan | FE+BE | 24 | TC-AC-PF-578, TC-AC-PF-659, TC-AC-PF-755, TC-AC-PF-759, TC-AC-PF-760, TC-AC-PF-761 |
| TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | Defense-in-depth: Validasi Server Push Update: Downgrade, Status Non-Eligible, Delta Kosong, Client Expired, dan Term Trial | FE+BE | 29 | TC-AC-PF-584, TC-AC-PF-585, TC-AC-PF-586, TC-AC-PF-655, TC-AC-PF-786 |
| TC-AC-PF-E2E-214-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Custom Plan dan Create Default Plan | FE+BE | 20 | TC-AC-PF-801, TC-AC-PF-802, TC-AC-PF-803 |
| TC-AC-PF-E2E-215-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | Defense-in-depth: Validasi Server Dependency D-2 dan D-4 serta Nilai Capacity di Luar Daftar Opsi pada Create Default Plan dan Edit Plan | FE+BE | 27 | TC-AC-PF-804, TC-AC-PF-805, TC-AC-PF-806 |
| TC-AC-PF-E2E-216-resilience-create-custom-plan-5xx-dan-tanpa-respons | Resilience: Create Custom Plan Gagal 5xx, Tanpa Respons, dan Retry Setelah Timeout | FE+BE | 34 | TC-AC-PF-164, TC-AC-PF-165, TC-AC-PF-716 |
| TC-AC-PF-E2E-217-resilience-edit-custom-plan-5xx-tanpa-respons-dan-timing-toast | Resilience: Edit Custom Plan Gagal 5xx dan Tanpa Respons serta Timing Toast Sukses, Error, dan Pengganti | FE+BE | 46 | TC-AC-PF-215, TC-AC-PF-718, TC-AC-PF-600 |
| TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons | Resilience: Archive dan Delete Gagal 5xx dan Tanpa Respons pada Custom Plan | FE+BE | 38 | TC-AC-PF-255, TC-AC-PF-262, TC-AC-PF-722, TC-AC-PF-723 |
| TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan | Resilience: Push Update dan Save Global Settings Gagal 5xx dan Tanpa Respons | FE+BE | 40 | TC-AC-PF-280, TC-AC-PF-299, TC-AC-PF-720, TC-AC-PF-721 |
| TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again | Resilience: Error Load Tabel Plans List pada Empat Sub-tab dan Try Again | FE+BE | 31 | TC-AC-PF-18, TC-AC-PF-681, TC-AC-PF-682, TC-AC-PF-683 |
| TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal | Resilience: Error Load Tab Assigned Clients dan Tiga Modal Changelog serta Try Again | FE+BE | 33 | TC-AC-PF-452, TC-AC-PF-494, TC-AC-PF-679, TC-AC-PF-632 |
| TC-AC-PF-E2E-222-resilience-download-gagal-tabel-plans-list-dan-plan-detail | Resilience: Download Gagal pada Tabel Default, Tabel Custom, dan Plan Detail: Toast Error dengan Nama Berkas | FE+BE | 24 | TC-AC-PF-356, TC-AC-PF-407, TC-AC-PF-606 |
| TC-AC-PF-E2E-223-resilience-download-gagal-tab-assigned-clients-dan-modal-changelog | Resilience: Download Gagal pada Tab Assigned Clients dan Modal Changelog: Toast Error dengan Nama Berkas | FE+BE | 27 | TC-AC-PF-450, TC-AC-PF-492, TC-AC-PF-518 |
| TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons | Resilience: Create dan Edit Default Plan Gagal 5xx dan Tanpa Respons | FE+BE | 43 | TC-AC-PF-193, TC-AC-PF-717, TC-AC-PF-235, TC-AC-PF-719 |

## 2. Daftar TC hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Seluruh TC granular memiliki langkah UI dan dicakup spec E2E. TC backend (`TC-AC-PF-BE-NNN`) tidak merujuk TC granular.

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-PF-1 | E2E | TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default | FE+BE |
| TC-AC-PF-2 | E2E | TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default | FE+BE |
| TC-AC-PF-3 | E2E | TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default | FE+BE |
| TC-AC-PF-4 | E2E | TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default | FE+BE |
| TC-AC-PF-5 | E2E | TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default | FE+BE |
| TC-AC-PF-6 | E2E | TC-AC-PF-E2E-001-screening-plans-list-tab-default-dan-urutan-default | FE+BE |
| TC-AC-PF-7 | E2E | TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default | FE+BE |
| TC-AC-PF-8 | E2E | TC-AC-PF-E2E-024-screening-plans-list-tab-custom-dan-urutan-default | FE+BE |
| TC-AC-PF-9 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-10 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-11 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-12 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-13 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-14 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-15 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-16 | E2E | TC-AC-PF-E2E-002-row-action-kolom-clients-dan-buka-plan-detail-dari-plans-list | FE+BE |
| TC-AC-PF-17 | E2E | TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-18 | E2E | TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again | FE+BE |
| TC-AC-PF-19 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-20 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-21 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-22 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-23 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-24 | E2E | TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | FE+BE |
| TC-AC-PF-25 | E2E | TC-AC-PF-E2E-005-plan-detail-header-info-plan-dan-badge-archived | FE+BE |
| TC-AC-PF-26 | E2E | TC-AC-PF-E2E-005-plan-detail-header-info-plan-dan-badge-archived | FE+BE |
| TC-AC-PF-27 | E2E | TC-AC-PF-E2E-005-plan-detail-header-info-plan-dan-badge-archived | FE+BE |
| TC-AC-PF-28 | E2E | TC-AC-PF-E2E-007-breadcrumb-plan-detail-tab-default-sub-tab-active-dan-archive | FE+BE |
| TC-AC-PF-29 | E2E | TC-AC-PF-E2E-007-breadcrumb-plan-detail-tab-default-sub-tab-active-dan-archive | FE+BE |
| TC-AC-PF-30 | E2E | TC-AC-PF-E2E-008-breadcrumb-plan-detail-tab-custom-sub-tab-active-dan-archive | FE+BE |
| TC-AC-PF-31 | E2E | TC-AC-PF-E2E-008-breadcrumb-plan-detail-tab-custom-sub-tab-active-dan-archive | FE+BE |
| TC-AC-PF-32 | E2E | TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type | FE+BE |
| TC-AC-PF-33 | E2E | TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type | FE+BE |
| TC-AC-PF-34 | E2E | TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type | FE+BE |
| TC-AC-PF-35 | E2E | TC-AC-PF-E2E-006-plan-detail-tab-overview-feature-matrix-per-product-dan-pricing-type | FE+BE |
| TC-AC-PF-36 | E2E | TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | FE+BE |
| TC-AC-PF-37 | E2E | TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | FE+BE |
| TC-AC-PF-38 | E2E | TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | FE+BE |
| TC-AC-PF-39 | E2E | TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | FE+BE |
| TC-AC-PF-40 | E2E | TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar | FE+BE |
| TC-AC-PF-41 | E2E | TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar | FE+BE |
| TC-AC-PF-42 | E2E | TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar | FE+BE |
| TC-AC-PF-43 | E2E | TC-AC-PF-E2E-010-preservasi-state-list-saat-kembali-dari-plan-detail-refresh-dan-reset-sidebar | FE+BE |
| TC-AC-PF-44 | E2E | TC-AC-PF-E2E-026-guided-tooltip-tur-empat-step-skip-dan-back | FE+BE |
| TC-AC-PF-45 | E2E | TC-AC-PF-E2E-026-guided-tooltip-tur-empat-step-skip-dan-back | FE+BE |
| TC-AC-PF-46 | E2E | TC-AC-PF-E2E-026-guided-tooltip-tur-empat-step-skip-dan-back | FE+BE |
| TC-AC-PF-47 | E2E | TC-AC-PF-E2E-027-guided-tooltip-replay-navigasi-resize-kolom-clients | FE+BE |
| TC-AC-PF-48 | E2E | TC-AC-PF-E2E-027-guided-tooltip-replay-navigasi-resize-kolom-clients | FE+BE |
| TC-AC-PF-49 | E2E | TC-AC-PF-E2E-027-guided-tooltip-replay-navigasi-resize-kolom-clients | FE+BE |
| TC-AC-PF-50 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-51 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-52 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-53 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-54 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-55 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-56 | E2E | TC-AC-PF-E2E-028-role-matrix-visibilitas-menu-sidebar-dan-akses-langsung | FE+BE |
| TC-AC-PF-57 | E2E | TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan | FE+BE |
| TC-AC-PF-58 | E2E | TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan | FE+BE |
| TC-AC-PF-59 | E2E | TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan | FE+BE |
| TC-AC-PF-60 | E2E | TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | FE+BE |
| TC-AC-PF-61 | E2E | TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | FE+BE |
| TC-AC-PF-62 | E2E | TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | FE+BE |
| TC-AC-PF-63 | E2E | TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | FE+BE |
| TC-AC-PF-64 | E2E | TC-AC-PF-E2E-030-role-matrix-ui-visibility-principal-read-only-create-only | FE+BE |
| TC-AC-PF-65 | E2E | TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | FE+BE |
| TC-AC-PF-66 | E2E | TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | FE+BE |
| TC-AC-PF-67 | E2E | TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | FE+BE |
| TC-AC-PF-68 | E2E | TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | FE+BE |
| TC-AC-PF-69 | E2E | TC-AC-PF-E2E-031-role-matrix-ui-visibility-distributor-dan-partner-total | FE+BE |
| TC-AC-PF-70 | E2E | TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | FE+BE |
| TC-AC-PF-71 | E2E | TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | FE+BE |
| TC-AC-PF-72 | E2E | TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | FE+BE |
| TC-AC-PF-73 | E2E | TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | FE+BE |
| TC-AC-PF-74 | E2E | TC-AC-PF-E2E-032-role-matrix-ui-visibility-distributor-dan-partner-read | FE+BE |
| TC-AC-PF-75 | E2E | TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | FE+BE |
| TC-AC-PF-76 | E2E | TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | FE+BE |
| TC-AC-PF-77 | E2E | TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | FE+BE |
| TC-AC-PF-78 | E2E | TC-AC-PF-E2E-029-role-matrix-ui-visibility-principal-total-control-dan | FE+BE |
| TC-AC-PF-79 | E2E | TC-AC-PF-E2E-025-konkurensi-capability-dicabut-dan-entitas-suspended-saat-form-dialog-terbuka | FE+BE |
| TC-AC-PF-80 | E2E | TC-AC-PF-E2E-034-capability-tunggal-principal-create-only-membuat-custom | FE+BE |
| TC-AC-PF-81 | E2E | TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push | FE+BE |
| TC-AC-PF-82 | E2E | TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan | FE+BE |
| TC-AC-PF-83 | E2E | TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan | FE+BE |
| TC-AC-PF-84 | E2E | TC-AC-PF-E2E-034-capability-tunggal-principal-create-only-membuat-custom | FE+BE |
| TC-AC-PF-85 | E2E | TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push | FE+BE |
| TC-AC-PF-86 | E2E | TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan | FE+BE |
| TC-AC-PF-87 | E2E | TC-AC-PF-E2E-036-capability-tunggal-principal-delete-only-archive-dan | FE+BE |
| TC-AC-PF-88 | E2E | TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push | FE+BE |
| TC-AC-PF-89 | E2E | TC-AC-PF-E2E-035-capability-tunggal-principal-update-only-edit-rename-push | FE+BE |
| TC-AC-PF-90 | E2E | TC-AC-PF-E2E-037-capability-tunggal-distributor-create-only-update-only | FE+BE |
| TC-AC-PF-91 | E2E | TC-AC-PF-E2E-037-capability-tunggal-distributor-create-only-update-only | FE+BE |
| TC-AC-PF-92 | E2E | TC-AC-PF-E2E-037-capability-tunggal-distributor-create-only-update-only | FE+BE |
| TC-AC-PF-93 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-94 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-95 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-96 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-97 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-98 | E2E | TC-AC-PF-E2E-038-row-scope-data-per-entitas-principal-distributor-partner | FE+BE |
| TC-AC-PF-99 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-100 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-101 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-102 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-103 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-104 | E2E | TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | FE+BE |
| TC-AC-PF-105 | E2E | TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | FE+BE |
| TC-AC-PF-106 | E2E | TC-AC-PF-E2E-039-masking-assigned-clients-per-baris-group-role-zero-access | FE+BE |
| TC-AC-PF-107 | E2E | TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | FE+BE |
| TC-AC-PF-108 | E2E | TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | FE+BE |
| TC-AC-PF-109 | E2E | TC-AC-PF-E2E-040-masking-assigned-clients-total-control-read-only-account | FE+BE |
| TC-AC-PF-110 | E2E | TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | FE+BE |
| TC-AC-PF-111 | E2E | TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template | FE+BE |
| TC-AC-PF-112 | E2E | TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template | FE+BE |
| TC-AC-PF-113 | E2E | TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template | FE+BE |
| TC-AC-PF-114 | E2E | TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | FE+BE |
| TC-AC-PF-115 | E2E | TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | FE+BE |
| TC-AC-PF-116 | E2E | TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | FE+BE |
| TC-AC-PF-117 | E2E | TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan | FE+BE |
| TC-AC-PF-118 | E2E | TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan | FE+BE |
| TC-AC-PF-119 | E2E | TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan | FE+BE |
| TC-AC-PF-120 | E2E | TC-AC-PF-E2E-050-keunikan-plan-name-create-custom-plan | FE+BE |
| TC-AC-PF-121 | E2E | TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | FE+BE |
| TC-AC-PF-122 | E2E | TC-AC-PF-E2E-049-plan-name-create-custom-plan-batas-panjang-trim-emoji-dan-fallback-server | FE+BE |
| TC-AC-PF-123 | E2E | TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | FE+BE |
| TC-AC-PF-124 | E2E | TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | FE+BE |
| TC-AC-PF-125 | E2E | TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | FE+BE |
| TC-AC-PF-126 | E2E | TC-AC-PF-E2E-047-screening-form-create-custom-plan-dan-dropdown-product-dan-template | FE+BE |
| TC-AC-PF-127 | E2E | TC-AC-PF-E2E-048-validasi-required-create-custom-plan-plan-name-product-dan-template | FE+BE |
| TC-AC-PF-128 | E2E | TC-AC-PF-E2E-051-pemilihan-template-mengisi-capacity-binary-feature-suites | FE+BE |
| TC-AC-PF-129 | E2E | TC-AC-PF-E2E-051-pemilihan-template-mengisi-capacity-binary-feature-suites | FE+BE |
| TC-AC-PF-130 | E2E | TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom | FE+BE |
| TC-AC-PF-131 | E2E | TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom | FE+BE |
| TC-AC-PF-132 | E2E | TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom | FE+BE |
| TC-AC-PF-133 | E2E | TC-AC-PF-E2E-052-open-api-dan-api-call-quota-create-custom-kunci-wajib-dan-batas-custom | FE+BE |
| TC-AC-PF-134 | E2E | TC-AC-PF-E2E-053-api-call-quota-custom-spinner-kelipatan-dan-awalan-preset | FE+BE |
| TC-AC-PF-135 | E2E | TC-AC-PF-E2E-053-api-call-quota-custom-spinner-kelipatan-dan-awalan-preset | FE+BE |
| TC-AC-PF-136 | E2E | TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | FE+BE |
| TC-AC-PF-137 | E2E | TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | FE+BE |
| TC-AC-PF-138 | E2E | TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | FE+BE |
| TC-AC-PF-139 | E2E | TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | FE+BE |
| TC-AC-PF-140 | E2E | TC-AC-PF-E2E-054-dependency-d-2-dan-d-4-pada-create-custom-plan | FE+BE |
| TC-AC-PF-141 | E2E | TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal | FE+BE |
| TC-AC-PF-142 | E2E | TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal | FE+BE |
| TC-AC-PF-143 | E2E | TC-AC-PF-E2E-064-estimated-reference-price-create-custom-plan-aktor-distributor-sell-reference-price | FE+BE |
| TC-AC-PF-144 | E2E | TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal | FE+BE |
| TC-AC-PF-145 | E2E | TC-AC-PF-E2E-055-estimated-reference-price-dan-estimated-total-create-custom-plan-principal | FE+BE |
| TC-AC-PF-146 | E2E | TC-AC-PF-E2E-057-submit-create-custom-plan-oleh-principal-dan-nilai-hasil-ubah-dari-template | FE+BE |
| TC-AC-PF-147 | E2E | TC-AC-PF-E2E-059-submit-create-custom-plan-oleh-distributor-dan-partner | FE+BE |
| TC-AC-PF-148 | E2E | TC-AC-PF-E2E-059-submit-create-custom-plan-oleh-distributor-dan-partner | FE+BE |
| TC-AC-PF-149 | E2E | TC-AC-PF-E2E-057-submit-create-custom-plan-oleh-principal-dan-nilai-hasil-ubah-dari-template | FE+BE |
| TC-AC-PF-150 | E2E | TC-AC-PF-E2E-058-create-custom-plan-product-sams-dan-siem-memakai-payload-fitur-fams | FE+BE |
| TC-AC-PF-151 | E2E | TC-AC-PF-E2E-058-create-custom-plan-product-sams-dan-siem-memakai-payload-fitur-fams | FE+BE |
| TC-AC-PF-152 | E2E | TC-AC-PF-E2E-065-template-tidak-disimpan-sebagai-relasi-perubahan-default-plan-tidak-mengubah-custom | FE+BE |
| TC-AC-PF-153 | E2E | TC-AC-PF-E2E-061-clear-field-create-custom-plan | FE+BE |
| TC-AC-PF-154 | E2E | TC-AC-PF-E2E-061-clear-field-create-custom-plan | FE+BE |
| TC-AC-PF-155 | E2E | TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | FE+BE |
| TC-AC-PF-156 | E2E | TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | FE+BE |
| TC-AC-PF-157 | E2E | TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | FE+BE |
| TC-AC-PF-158 | E2E | TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | FE+BE |
| TC-AC-PF-159 | E2E | TC-AC-PF-E2E-062-unsaved-changes-create-custom-plan-breadcrumb-sidebar-back-dan-form-bersih | FE+BE |
| TC-AC-PF-160 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-161 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-162 | E2E | TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan | FE+BE |
| TC-AC-PF-163 | E2E | TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan | FE+BE |
| TC-AC-PF-164 | E2E | TC-AC-PF-E2E-216-resilience-create-custom-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-165 | E2E | TC-AC-PF-E2E-216-resilience-create-custom-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-166 | E2E | TC-AC-PF-E2E-066-screening-form-create-default-plan-dan-nilai-awal | FE+BE |
| TC-AC-PF-167 | E2E | TC-AC-PF-E2E-066-screening-form-create-default-plan-dan-nilai-awal | FE+BE |
| TC-AC-PF-168 | E2E | TC-AC-PF-E2E-066-screening-form-create-default-plan-dan-nilai-awal | FE+BE |
| TC-AC-PF-169 | E2E | TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120 | FE+BE |
| TC-AC-PF-170 | E2E | TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120 | FE+BE |
| TC-AC-PF-171 | E2E | TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120 | FE+BE |
| TC-AC-PF-172 | E2E | TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama | FE+BE |
| TC-AC-PF-173 | E2E | TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan | FE+BE |
| TC-AC-PF-174 | E2E | TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan | FE+BE |
| TC-AC-PF-175 | E2E | TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan | FE+BE |
| TC-AC-PF-176 | E2E | TC-AC-PF-E2E-067-pricing-type-create-default-plan-radio-tersaring-dan | FE+BE |
| TC-AC-PF-177 | E2E | TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | FE+BE |
| TC-AC-PF-178 | E2E | TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | FE+BE |
| TC-AC-PF-179 | E2E | TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | FE+BE |
| TC-AC-PF-180 | E2E | TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | FE+BE |
| TC-AC-PF-181 | E2E | TC-AC-PF-E2E-068-asset-cap-create-default-plan-kondisi-muncul-dan-validasi | FE+BE |
| TC-AC-PF-182 | E2E | TC-AC-PF-E2E-069-asset-cap-0-dan-feature-suites-free-terkunci-pada-create | FE+BE |
| TC-AC-PF-183 | E2E | TC-AC-PF-E2E-069-asset-cap-0-dan-feature-suites-free-terkunci-pada-create | FE+BE |
| TC-AC-PF-184 | E2E | TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama | FE+BE |
| TC-AC-PF-185 | E2E | TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template | FE+BE |
| TC-AC-PF-186 | E2E | TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template | FE+BE |
| TC-AC-PF-187 | E2E | TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama | FE+BE |
| TC-AC-PF-188 | E2E | TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template | FE+BE |
| TC-AC-PF-189 | E2E | TC-AC-PF-E2E-071-submit-sukses-create-default-plan-tier-ceiling-template | FE+BE |
| TC-AC-PF-190 | E2E | TC-AC-PF-E2E-072-clear-field-dan-unsaved-changes-dasar-create-default-plan | FE+BE |
| TC-AC-PF-191 | E2E | TC-AC-PF-E2E-072-clear-field-dan-unsaved-changes-dasar-create-default-plan | FE+BE |
| TC-AC-PF-192 | E2E | TC-AC-PF-E2E-077-form-bersih-dan-refresh-create-default-plan | FE+BE |
| TC-AC-PF-193 | E2E | TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-194 | E2E | TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan | FE+BE |
| TC-AC-PF-195 | E2E | TC-AC-PF-E2E-078-screening-dan-akses-form-edit-custom-plan | FE+BE |
| TC-AC-PF-196 | E2E | TC-AC-PF-E2E-078-screening-dan-akses-form-edit-custom-plan | FE+BE |
| TC-AC-PF-197 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-198 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-199 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-200 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-201 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-202 | E2E | TC-AC-PF-E2E-079-plan-name-edit-custom-plan-validasi-keunikan-trim-emoji | FE+BE |
| TC-AC-PF-203 | E2E | TC-AC-PF-E2E-080-edit-custom-plan-edit-nilai-fitur-dan-versi | FE+BE |
| TC-AC-PF-204 | E2E | TC-AC-PF-E2E-080-edit-custom-plan-edit-nilai-fitur-dan-versi | FE+BE |
| TC-AC-PF-205 | E2E | TC-AC-PF-E2E-080-edit-custom-plan-edit-nilai-fitur-dan-versi | FE+BE |
| TC-AC-PF-206 | E2E | TC-AC-PF-E2E-081-edit-custom-plan-no-op-kapitalisasi-nilai-turun | FE+BE |
| TC-AC-PF-207 | E2E | TC-AC-PF-E2E-081-edit-custom-plan-no-op-kapitalisasi-nilai-turun | FE+BE |
| TC-AC-PF-208 | E2E | TC-AC-PF-E2E-081-edit-custom-plan-no-op-kapitalisasi-nilai-turun | FE+BE |
| TC-AC-PF-209 | E2E | TC-AC-PF-E2E-082-edit-custom-plan-dependency-d-2-open-api-off-open-api-on | FE+BE |
| TC-AC-PF-210 | E2E | TC-AC-PF-E2E-082-edit-custom-plan-dependency-d-2-open-api-off-open-api-on | FE+BE |
| TC-AC-PF-211 | E2E | TC-AC-PF-E2E-082-edit-custom-plan-dependency-d-2-open-api-off-open-api-on | FE+BE |
| TC-AC-PF-212 | E2E | TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-PF-213 | E2E | TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-PF-214 | E2E | TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-PF-215 | E2E | TC-AC-PF-E2E-217-resilience-edit-custom-plan-5xx-tanpa-respons-dan-timing-toast | FE+BE |
| TC-AC-PF-216 | E2E | TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda | FE+BE |
| TC-AC-PF-217 | E2E | TC-AC-PF-E2E-056-estimated-reference-price-edit-custom-plan-serta-create-dan-edit-default-plan | FE+BE |
| TC-AC-PF-218 | E2E | TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | FE+BE |
| TC-AC-PF-219 | E2E | TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | FE+BE |
| TC-AC-PF-220 | E2E | TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | FE+BE |
| TC-AC-PF-221 | E2E | TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | FE+BE |
| TC-AC-PF-222 | E2E | TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified | FE+BE |
| TC-AC-PF-223 | E2E | TC-AC-PF-E2E-095-edit-default-plan-asset-cap-free-dan-product-siem | FE+BE |
| TC-AC-PF-224 | E2E | TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free | FE+BE |
| TC-AC-PF-225 | E2E | TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free | FE+BE |
| TC-AC-PF-226 | E2E | TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free | FE+BE |
| TC-AC-PF-227 | E2E | TC-AC-PF-E2E-089-validasi-asset-cap-edit-default-plan-free | FE+BE |
| TC-AC-PF-228 | E2E | TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | FE+BE |
| TC-AC-PF-229 | E2E | TC-AC-PF-E2E-095-edit-default-plan-asset-cap-free-dan-product-siem | FE+BE |
| TC-AC-PF-230 | E2E | TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified | FE+BE |
| TC-AC-PF-231 | E2E | TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified | FE+BE |
| TC-AC-PF-232 | E2E | TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | FE+BE |
| TC-AC-PF-233 | E2E | TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5 | FE+BE |
| TC-AC-PF-234 | E2E | TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5 | FE+BE |
| TC-AC-PF-235 | E2E | TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-236 | E2E | TC-AC-PF-E2E-088-edit-default-plan-nilai-fitur-rename-no-op-last-modified | FE+BE |
| TC-AC-PF-237 | E2E | TC-AC-PF-E2E-096-dialog-archive-plan-screening-dan-cancel-custom-dan-default | FE+BE |
| TC-AC-PF-238 | E2E | TC-AC-PF-E2E-096-dialog-archive-plan-screening-dan-cancel-custom-dan-default | FE+BE |
| TC-AC-PF-239 | E2E | TC-AC-PF-E2E-096-dialog-archive-plan-screening-dan-cancel-custom-dan-default | FE+BE |
| TC-AC-PF-240 | E2E | TC-AC-PF-E2E-097-archive-custom-plan-sukses-header-plan-detail-klik-ganda | FE+BE |
| TC-AC-PF-241 | E2E | TC-AC-PF-E2E-098-archive-default-plan-pergeseran-tier | FE+BE |
| TC-AC-PF-242 | E2E | TC-AC-PF-E2E-098-archive-default-plan-pergeseran-tier | FE+BE |
| TC-AC-PF-243 | E2E | TC-AC-PF-E2E-111-archive-default-plan-tier-tertinggi-terendah-dan-last-modified-tergeser | FE+BE |
| TC-AC-PF-244 | E2E | TC-AC-PF-E2E-111-archive-default-plan-tier-tertinggi-terendah-dan-last-modified-tergeser | FE+BE |
| TC-AC-PF-245 | E2E | TC-AC-PF-E2E-111-archive-default-plan-tier-tertinggi-terendah-dan-last-modified-tergeser | FE+BE |
| TC-AC-PF-246 | E2E | TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace | FE+BE |
| TC-AC-PF-247 | E2E | TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace | FE+BE |
| TC-AC-PF-248 | E2E | TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace | FE+BE |
| TC-AC-PF-249 | E2E | TC-AC-PF-E2E-100-guard-cannot-archive-plan-waiting-pending-active-grace | FE+BE |
| TC-AC-PF-250 | E2E | TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar | FE+BE |
| TC-AC-PF-251 | E2E | TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar | FE+BE |
| TC-AC-PF-252 | E2E | TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar | FE+BE |
| TC-AC-PF-253 | E2E | TC-AC-PF-E2E-097-archive-custom-plan-sukses-header-plan-detail-klik-ganda | FE+BE |
| TC-AC-PF-254 | E2E | TC-AC-PF-E2E-099-archive-default-plan-header-plan-detail-plan-terakhir | FE+BE |
| TC-AC-PF-255 | E2E | TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-256 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-257 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-258 | E2E | TC-AC-PF-E2E-103-delete-plan-archived-sukses-klik-ganda-bekas-template | FE+BE |
| TC-AC-PF-259 | E2E | TC-AC-PF-E2E-103-delete-plan-archived-sukses-klik-ganda-bekas-template | FE+BE |
| TC-AC-PF-260 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-261 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-262 | E2E | TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-263 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-264 | E2E | TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain | FE+BE |
| TC-AC-PF-265 | E2E | TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain | FE+BE |
| TC-AC-PF-266 | E2E | TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain | FE+BE |
| TC-AC-PF-267 | E2E | TC-AC-PF-E2E-105-push-update-eligibilitas-client-active-grace-status-lain | FE+BE |
| TC-AC-PF-268 | E2E | TC-AC-PF-E2E-106-push-update-delta-downgrade-per-client-delta-net-kosong | FE+BE |
| TC-AC-PF-269 | E2E | TC-AC-PF-E2E-106-push-update-delta-downgrade-per-client-delta-net-kosong | FE+BE |
| TC-AC-PF-270 | E2E | TC-AC-PF-E2E-106-push-update-delta-downgrade-per-client-delta-net-kosong | FE+BE |
| TC-AC-PF-271 | E2E | TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi | FE+BE |
| TC-AC-PF-272 | E2E | TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi | FE+BE |
| TC-AC-PF-273 | E2E | TC-AC-PF-E2E-108-push-update-kepemilikan-principal-dan-distributor | FE+BE |
| TC-AC-PF-274 | E2E | TC-AC-PF-E2E-108-push-update-kepemilikan-principal-dan-distributor | FE+BE |
| TC-AC-PF-275 | E2E | TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel | FE+BE |
| TC-AC-PF-276 | E2E | TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel | FE+BE |
| TC-AC-PF-277 | E2E | TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel | FE+BE |
| TC-AC-PF-278 | E2E | TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda | FE+BE |
| TC-AC-PF-279 | E2E | TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda | FE+BE |
| TC-AC-PF-280 | E2E | TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan | FE+BE |
| TC-AC-PF-281 | E2E | TC-AC-PF-E2E-033-gate-status-entitas-suspended-dan-expired-aksi-tulis | FE+BE |
| TC-AC-PF-282 | E2E | TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi | FE+BE |
| TC-AC-PF-283 | E2E | TC-AC-PF-E2E-107-push-update-teks-jumlah-client-outdated-dan-ketiadaan-aksi | FE+BE |
| TC-AC-PF-284 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-285 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-286 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-287 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-288 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-289 | E2E | TC-AC-PF-E2E-113-global-settings-screening-dan-validasi-angka | FE+BE |
| TC-AC-PF-290 | E2E | TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op | FE+BE |
| TC-AC-PF-291 | E2E | TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op | FE+BE |
| TC-AC-PF-292 | E2E | TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op | FE+BE |
| TC-AC-PF-293 | E2E | TC-AC-PF-E2E-115-global-settings-save-berhasil-dua-setting-dan-save-no-op | FE+BE |
| TC-AC-PF-294 | E2E | TC-AC-PF-E2E-116-global-settings-clear-field-dan-unsaved-changes-pindah-tab-dan-breadcrumb | FE+BE |
| TC-AC-PF-295 | E2E | TC-AC-PF-E2E-116-global-settings-clear-field-dan-unsaved-changes-pindah-tab-dan-breadcrumb | FE+BE |
| TC-AC-PF-296 | E2E | TC-AC-PF-E2E-116-global-settings-clear-field-dan-unsaved-changes-pindah-tab-dan-breadcrumb | FE+BE |
| TC-AC-PF-297 | E2E | TC-AC-PF-E2E-129-global-settings-unsaved-changes-klik-menu-sidebar-dan-buka-changelog-saat-dirty | FE+BE |
| TC-AC-PF-298 | E2E | TC-AC-PF-E2E-129-global-settings-unsaved-changes-klik-menu-sidebar-dan-buka-changelog-saat-dirty | FE+BE |
| TC-AC-PF-299 | E2E | TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan | FE+BE |
| TC-AC-PF-300 | E2E | TC-AC-PF-E2E-128-global-settings-klik-ganda-save-state-submitting-dan-isi-entri-changelog | FE+BE |
| TC-AC-PF-301 | E2E | TC-AC-PF-E2E-130-search-tab-default-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-302 | E2E | TC-AC-PF-E2E-130-search-tab-default-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-303 | E2E | TC-AC-PF-E2E-130-search-tab-default-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-304 | E2E | TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-305 | E2E | TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-306 | E2E | TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-307 | E2E | TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-308 | E2E | TC-AC-PF-E2E-131-search-tab-default-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-309 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-310 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-311 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-312 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-313 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-314 | E2E | TC-AC-PF-E2E-132-filter-tab-default-active-screening-product-pricing-type | FE+BE |
| TC-AC-PF-315 | E2E | TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | FE+BE |
| TC-AC-PF-316 | E2E | TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | FE+BE |
| TC-AC-PF-317 | E2E | TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | FE+BE |
| TC-AC-PF-318 | E2E | TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | FE+BE |
| TC-AC-PF-319 | E2E | TC-AC-PF-E2E-133-filter-tab-default-active-and-opsi-distinct-chip-tutup | FE+BE |
| TC-AC-PF-320 | E2E | TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | FE+BE |
| TC-AC-PF-321 | E2E | TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | FE+BE |
| TC-AC-PF-322 | E2E | TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | FE+BE |
| TC-AC-PF-323 | E2E | TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | FE+BE |
| TC-AC-PF-324 | E2E | TC-AC-PF-E2E-134-filter-tab-default-active-indikator-clients-tersembunyi | FE+BE |
| TC-AC-PF-325 | E2E | TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | FE+BE |
| TC-AC-PF-326 | E2E | TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | FE+BE |
| TC-AC-PF-327 | E2E | TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | FE+BE |
| TC-AC-PF-328 | E2E | TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | FE+BE |
| TC-AC-PF-329 | E2E | TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active | FE+BE |
| TC-AC-PF-330 | E2E | TC-AC-PF-E2E-135-sort-tab-default-active-per-kolom | FE+BE |
| TC-AC-PF-331 | E2E | TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active | FE+BE |
| TC-AC-PF-332 | E2E | TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active | FE+BE |
| TC-AC-PF-333 | E2E | TC-AC-PF-E2E-136-kombinasi-search-filter-sort-dan-clear-tab-default-active | FE+BE |
| TC-AC-PF-334 | E2E | TC-AC-PF-E2E-158-create-default-plan-saat-tabel-default-active-terfilter | FE+BE |
| TC-AC-PF-335 | E2E | TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-336 | E2E | TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-337 | E2E | TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-338 | E2E | TC-AC-PF-E2E-137-setup-column-tab-default-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-339 | E2E | TC-AC-PF-E2E-138-setup-column-tab-default-active-pin-reset-to-default-tutup | FE+BE |
| TC-AC-PF-340 | E2E | TC-AC-PF-E2E-138-setup-column-tab-default-active-pin-reset-to-default-tutup | FE+BE |
| TC-AC-PF-341 | E2E | TC-AC-PF-E2E-138-setup-column-tab-default-active-pin-reset-to-default-tutup | FE+BE |
| TC-AC-PF-342 | E2E | TC-AC-PF-E2E-139-setup-column-tab-default-active-guard-satu-kolom-batas-pin | FE+BE |
| TC-AC-PF-343 | E2E | TC-AC-PF-E2E-139-setup-column-tab-default-active-guard-satu-kolom-batas-pin | FE+BE |
| TC-AC-PF-344 | E2E | TC-AC-PF-E2E-139-setup-column-tab-default-active-guard-satu-kolom-batas-pin | FE+BE |
| TC-AC-PF-345 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-346 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-347 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-348 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-349 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-350 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-351 | E2E | TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | FE+BE |
| TC-AC-PF-352 | E2E | TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | FE+BE |
| TC-AC-PF-353 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-354 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-355 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-356 | E2E | TC-AC-PF-E2E-222-resilience-download-gagal-tabel-plans-list-dan-plan-detail | FE+BE |
| TC-AC-PF-357 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-358 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-359 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-360 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-361 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-362 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-363 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-364 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-365 | E2E | TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | FE+BE |
| TC-AC-PF-366 | E2E | TC-AC-PF-E2E-146-search-tab-custom-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-367 | E2E | TC-AC-PF-E2E-146-search-tab-custom-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-368 | E2E | TC-AC-PF-E2E-146-search-tab-custom-active-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-369 | E2E | TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-370 | E2E | TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-371 | E2E | TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-372 | E2E | TC-AC-PF-E2E-147-search-tab-custom-active-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-373 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-374 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-375 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-376 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-377 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-378 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-379 | E2E | TC-AC-PF-E2E-148-filter-tab-custom-active | FE+BE |
| TC-AC-PF-380 | E2E | TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol | FE+BE |
| TC-AC-PF-381 | E2E | TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol | FE+BE |
| TC-AC-PF-382 | E2E | TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol | FE+BE |
| TC-AC-PF-383 | E2E | TC-AC-PF-E2E-149-sort-tab-custom-active-dan-kombinasi-kontrol | FE+BE |
| TC-AC-PF-384 | E2E | TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-385 | E2E | TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-386 | E2E | TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-387 | E2E | TC-AC-PF-E2E-150-setup-column-tab-custom-active-screening-ceklis-geser | FE+BE |
| TC-AC-PF-388 | E2E | TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | FE+BE |
| TC-AC-PF-389 | E2E | TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | FE+BE |
| TC-AC-PF-390 | E2E | TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | FE+BE |
| TC-AC-PF-391 | E2E | TC-AC-PF-E2E-152-setup-column-tab-custom-active-guard-satu-kolom-dan-batas | FE+BE |
| TC-AC-PF-392 | E2E | TC-AC-PF-E2E-152-setup-column-tab-custom-active-guard-satu-kolom-dan-batas | FE+BE |
| TC-AC-PF-393 | E2E | TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | FE+BE |
| TC-AC-PF-394 | E2E | TC-AC-PF-E2E-151-setup-column-tab-custom-active-pin-reset-tutup-kolom | FE+BE |
| TC-AC-PF-395 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-396 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-397 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-398 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-399 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-400 | E2E | TC-AC-PF-E2E-156-pagination-tab-custom-active-volume-120-plan | FE+BE |
| TC-AC-PF-401 | E2E | TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | FE+BE |
| TC-AC-PF-402 | E2E | TC-AC-PF-E2E-144-isi-berkas-download-plans-list-tab-custom-bom-sheet-kutip | FE+BE |
| TC-AC-PF-403 | E2E | TC-AC-PF-E2E-144-isi-berkas-download-plans-list-tab-custom-bom-sheet-kutip | FE+BE |
| TC-AC-PF-404 | E2E | TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | FE+BE |
| TC-AC-PF-405 | E2E | TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | FE+BE |
| TC-AC-PF-406 | E2E | TC-AC-PF-E2E-142-download-plans-list-tab-custom-nama-berkas-search-column | FE+BE |
| TC-AC-PF-407 | E2E | TC-AC-PF-E2E-222-resilience-download-gagal-tabel-plans-list-dan-plan-detail | FE+BE |
| TC-AC-PF-408 | E2E | TC-AC-PF-E2E-159-kombinasi-kontrol-dan-pemulihan-empty-state-tab-custom-active | FE+BE |
| TC-AC-PF-409 | E2E | TC-AC-PF-E2E-159-kombinasi-kontrol-dan-pemulihan-empty-state-tab-custom-active | FE+BE |
| TC-AC-PF-410 | E2E | TC-AC-PF-E2E-160-screening-tab-assigned-clients-dan-format-sel | FE+BE |
| TC-AC-PF-411 | E2E | TC-AC-PF-E2E-161-search-tab-assigned-clients-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-412 | E2E | TC-AC-PF-E2E-161-search-tab-assigned-clients-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-413 | E2E | TC-AC-PF-E2E-161-search-tab-assigned-clients-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-414 | E2E | TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-415 | E2E | TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-416 | E2E | TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-417 | E2E | TC-AC-PF-E2E-162-search-tab-assigned-clients-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-418 | E2E | TC-AC-PF-E2E-163-filter-tab-assigned-clients-screening-subscription-status | FE+BE |
| TC-AC-PF-419 | E2E | TC-AC-PF-E2E-163-filter-tab-assigned-clients-screening-subscription-status | FE+BE |
| TC-AC-PF-420 | E2E | TC-AC-PF-E2E-163-filter-tab-assigned-clients-screening-subscription-status | FE+BE |
| TC-AC-PF-421 | E2E | TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa | FE+BE |
| TC-AC-PF-422 | E2E | TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa | FE+BE |
| TC-AC-PF-423 | E2E | TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa | FE+BE |
| TC-AC-PF-424 | E2E | TC-AC-PF-E2E-164-filter-tab-assigned-clients-assigned-date-and-opsi-tanpa | FE+BE |
| TC-AC-PF-425 | E2E | TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | FE+BE |
| TC-AC-PF-426 | E2E | TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | FE+BE |
| TC-AC-PF-427 | E2E | TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | FE+BE |
| TC-AC-PF-428 | E2E | TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | FE+BE |
| TC-AC-PF-429 | E2E | TC-AC-PF-E2E-166-setup-column-tab-assigned-clients-screening-ceklis | FE+BE |
| TC-AC-PF-430 | E2E | TC-AC-PF-E2E-166-setup-column-tab-assigned-clients-screening-ceklis | FE+BE |
| TC-AC-PF-431 | E2E | TC-AC-PF-E2E-166-setup-column-tab-assigned-clients-screening-ceklis | FE+BE |
| TC-AC-PF-432 | E2E | TC-AC-PF-E2E-167-setup-column-tab-assigned-clients-geser-pin-reset | FE+BE |
| TC-AC-PF-433 | E2E | TC-AC-PF-E2E-167-setup-column-tab-assigned-clients-geser-pin-reset | FE+BE |
| TC-AC-PF-434 | E2E | TC-AC-PF-E2E-167-setup-column-tab-assigned-clients-geser-pin-reset | FE+BE |
| TC-AC-PF-435 | E2E | TC-AC-PF-E2E-168-setup-column-tab-assigned-clients-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-436 | E2E | TC-AC-PF-E2E-168-setup-column-tab-assigned-clients-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-437 | E2E | TC-AC-PF-E2E-168-setup-column-tab-assigned-clients-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-438 | E2E | TC-AC-PF-E2E-176-setup-column-tab-assigned-clients-independensi-cache | FE+BE |
| TC-AC-PF-439 | E2E | TC-AC-PF-E2E-169-pagination-tab-assigned-clients-default-dan-navigasi | FE+BE |
| TC-AC-PF-440 | E2E | TC-AC-PF-E2E-169-pagination-tab-assigned-clients-default-dan-navigasi | FE+BE |
| TC-AC-PF-441 | E2E | TC-AC-PF-E2E-170-pagination-tab-assigned-clients-nomor-tidak-valid-page | FE+BE |
| TC-AC-PF-442 | E2E | TC-AC-PF-E2E-170-pagination-tab-assigned-clients-nomor-tidak-valid-page | FE+BE |
| TC-AC-PF-443 | E2E | TC-AC-PF-E2E-170-pagination-tab-assigned-clients-nomor-tidak-valid-page | FE+BE |
| TC-AC-PF-444 | E2E | TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column | FE+BE |
| TC-AC-PF-445 | E2E | TC-AC-PF-E2E-172-isi-berkas-download-tab-assigned-clients-bom-sheet-plan | FE+BE |
| TC-AC-PF-446 | E2E | TC-AC-PF-E2E-172-isi-berkas-download-tab-assigned-clients-bom-sheet-plan | FE+BE |
| TC-AC-PF-447 | E2E | TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column | FE+BE |
| TC-AC-PF-448 | E2E | TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column | FE+BE |
| TC-AC-PF-449 | E2E | TC-AC-PF-E2E-171-download-tab-assigned-clients-nama-berkas-search-column | FE+BE |
| TC-AC-PF-450 | E2E | TC-AC-PF-E2E-223-resilience-download-gagal-tab-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-451 | E2E | TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail | FE+BE |
| TC-AC-PF-452 | E2E | TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal | FE+BE |
| TC-AC-PF-453 | E2E | TC-AC-PF-E2E-160-screening-tab-assigned-clients-dan-format-sel | FE+BE |
| TC-AC-PF-454 | E2E | TC-AC-PF-E2E-178-modal-changelog-default-buka-screening-tutup | FE+BE |
| TC-AC-PF-455 | E2E | TC-AC-PF-E2E-178-modal-changelog-default-buka-screening-tutup | FE+BE |
| TC-AC-PF-456 | E2E | TC-AC-PF-E2E-178-modal-changelog-default-buka-screening-tutup | FE+BE |
| TC-AC-PF-457 | E2E | TC-AC-PF-E2E-180-search-modal-changelog-default-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-458 | E2E | TC-AC-PF-E2E-180-search-modal-changelog-default-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-459 | E2E | TC-AC-PF-E2E-180-search-modal-changelog-default-siklus-trim-tanpa-hasil | FE+BE |
| TC-AC-PF-460 | E2E | TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-461 | E2E | TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-462 | E2E | TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-463 | E2E | TC-AC-PF-E2E-181-search-modal-changelog-default-kelas-kolom-dan-visibilitas | FE+BE |
| TC-AC-PF-464 | E2E | TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select | FE+BE |
| TC-AC-PF-465 | E2E | TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select | FE+BE |
| TC-AC-PF-466 | E2E | TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select | FE+BE |
| TC-AC-PF-467 | E2E | TC-AC-PF-E2E-182-filter-modal-changelog-default-screening-dan-multi-select | FE+BE |
| TC-AC-PF-468 | E2E | TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | FE+BE |
| TC-AC-PF-469 | E2E | TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | FE+BE |
| TC-AC-PF-470 | E2E | TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | FE+BE |
| TC-AC-PF-471 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |
| TC-AC-PF-472 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |
| TC-AC-PF-473 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |
| TC-AC-PF-474 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |
| TC-AC-PF-475 | E2E | TC-AC-PF-E2E-185-setup-column-modal-changelog-default-screening-ceklis | FE+BE |
| TC-AC-PF-476 | E2E | TC-AC-PF-E2E-185-setup-column-modal-changelog-default-screening-ceklis | FE+BE |
| TC-AC-PF-477 | E2E | TC-AC-PF-E2E-185-setup-column-modal-changelog-default-screening-ceklis | FE+BE |
| TC-AC-PF-478 | E2E | TC-AC-PF-E2E-186-setup-column-modal-changelog-default-geser-pin-reset | FE+BE |
| TC-AC-PF-479 | E2E | TC-AC-PF-E2E-186-setup-column-modal-changelog-default-geser-pin-reset | FE+BE |
| TC-AC-PF-480 | E2E | TC-AC-PF-E2E-186-setup-column-modal-changelog-default-geser-pin-reset | FE+BE |
| TC-AC-PF-481 | E2E | TC-AC-PF-E2E-187-setup-column-modal-changelog-default-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-482 | E2E | TC-AC-PF-E2E-187-setup-column-modal-changelog-default-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-483 | E2E | TC-AC-PF-E2E-187-setup-column-modal-changelog-default-tutup-guard-batas-pin | FE+BE |
| TC-AC-PF-484 | E2E | TC-AC-PF-E2E-204-cache-setup-column-independen-dan-esc-berlapis-modal-changelog-default | FE+BE |
| TC-AC-PF-485 | E2E | TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris | FE+BE |
| TC-AC-PF-486 | E2E | TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-487 | E2E | TC-AC-PF-E2E-189-isi-berkas-download-modal-changelog-default-bom-sheet | FE+BE |
| TC-AC-PF-488 | E2E | TC-AC-PF-E2E-189-isi-berkas-download-modal-changelog-default-bom-sheet | FE+BE |
| TC-AC-PF-489 | E2E | TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-490 | E2E | TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-491 | E2E | TC-AC-PF-E2E-188-download-modal-changelog-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-492 | E2E | TC-AC-PF-E2E-223-resilience-download-gagal-tab-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-493 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-494 | E2E | TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal | FE+BE |
| TC-AC-PF-495 | E2E | TC-AC-PF-E2E-179-modal-changelog-custom-screening-dan-scope-data-per-entitas | FE+BE |
| TC-AC-PF-496 | E2E | TC-AC-PF-E2E-179-modal-changelog-custom-screening-dan-scope-data-per-entitas | FE+BE |
| TC-AC-PF-497 | E2E | TC-AC-PF-E2E-192-search-filter-sort-dan-setup-column-modal-changelog-custom | FE+BE |
| TC-AC-PF-498 | E2E | TC-AC-PF-E2E-192-search-filter-sort-dan-setup-column-modal-changelog-custom | FE+BE |
| TC-AC-PF-499 | E2E | TC-AC-PF-E2E-191-download-modal-changelog-custom-dan-global-settings-nama | FE+BE |
| TC-AC-PF-500 | E2E | TC-AC-PF-E2E-203-screening-dan-filter-panel-modal-changelog-global-settings | FE+BE |
| TC-AC-PF-501 | E2E | TC-AC-PF-E2E-203-screening-dan-filter-panel-modal-changelog-global-settings | FE+BE |
| TC-AC-PF-502 | E2E | TC-AC-PF-E2E-195-modal-changelog-global-settings-filter-dan-search | FE+BE |
| TC-AC-PF-503 | E2E | TC-AC-PF-E2E-195-modal-changelog-global-settings-filter-dan-search | FE+BE |
| TC-AC-PF-504 | E2E | TC-AC-PF-E2E-195-modal-changelog-global-settings-filter-dan-search | FE+BE |
| TC-AC-PF-505 | E2E | TC-AC-PF-E2E-196-modal-changelog-global-settings-sort | FE+BE |
| TC-AC-PF-506 | E2E | TC-AC-PF-E2E-196-modal-changelog-global-settings-sort | FE+BE |
| TC-AC-PF-507 | E2E | TC-AC-PF-E2E-197-setup-column-modal-changelog-global-settings-screening | FE+BE |
| TC-AC-PF-508 | E2E | TC-AC-PF-E2E-197-setup-column-modal-changelog-global-settings-screening | FE+BE |
| TC-AC-PF-509 | E2E | TC-AC-PF-E2E-197-setup-column-modal-changelog-global-settings-screening | FE+BE |
| TC-AC-PF-510 | E2E | TC-AC-PF-E2E-198-setup-column-modal-changelog-global-settings-geser-pin | FE+BE |
| TC-AC-PF-511 | E2E | TC-AC-PF-E2E-198-setup-column-modal-changelog-global-settings-geser-pin | FE+BE |
| TC-AC-PF-512 | E2E | TC-AC-PF-E2E-198-setup-column-modal-changelog-global-settings-geser-pin | FE+BE |
| TC-AC-PF-513 | E2E | TC-AC-PF-E2E-199-setup-column-modal-changelog-global-settings-tutup-guard | FE+BE |
| TC-AC-PF-514 | E2E | TC-AC-PF-E2E-199-setup-column-modal-changelog-global-settings-tutup-guard | FE+BE |
| TC-AC-PF-515 | E2E | TC-AC-PF-E2E-199-setup-column-modal-changelog-global-settings-tutup-guard | FE+BE |
| TC-AC-PF-516 | E2E | TC-AC-PF-E2E-202-pagination-modal-changelog-global-settings-dan-archive | FE+BE |
| TC-AC-PF-517 | E2E | TC-AC-PF-E2E-191-download-modal-changelog-custom-dan-global-settings-nama | FE+BE |
| TC-AC-PF-518 | E2E | TC-AC-PF-E2E-223-resilience-download-gagal-tab-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-519 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-520 | E2E | TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | FE+BE |
| TC-AC-PF-521 | E2E | TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | FE+BE |
| TC-AC-PF-522 | E2E | TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | FE+BE |
| TC-AC-PF-523 | E2E | TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | FE+BE |
| TC-AC-PF-524 | E2E | TC-AC-PF-E2E-121-isi-entri-changelog-create-edit-dan-rename | FE+BE |
| TC-AC-PF-525 | E2E | TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | FE+BE |
| TC-AC-PF-526 | E2E | TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | FE+BE |
| TC-AC-PF-527 | E2E | TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | FE+BE |
| TC-AC-PF-528 | E2E | TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | FE+BE |
| TC-AC-PF-529 | E2E | TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan | FE+BE |
| TC-AC-PF-530 | E2E | TC-AC-PF-E2E-122-isi-entri-changelog-archive-delete-push-update | FE+BE |
| TC-AC-PF-531 | E2E | TC-AC-PF-E2E-128-global-settings-klik-ganda-save-state-submitting-dan-isi-entri-changelog | FE+BE |
| TC-AC-PF-532 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-533 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-534 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-535 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-536 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-537 | E2E | TC-AC-PF-E2E-124-system-log-aktor-dan-activity-log-untuk-aksi-plan | FE+BE |
| TC-AC-PF-538 | E2E | TC-AC-PF-E2E-125-aksi-ditolak-tidak-menulis-entri-log-di-surface-mana-pun | FE+BE |
| TC-AC-PF-539 | E2E | TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan | FE+BE |
| TC-AC-PF-540 | E2E | TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan | FE+BE |
| TC-AC-PF-541 | E2E | TC-AC-PF-E2E-123-snapshot-changelog-dan-persistensi-entri-sesudah-plan | FE+BE |
| TC-AC-PF-542 | E2E | TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | FE+BE |
| TC-AC-PF-543 | E2E | TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | FE+BE |
| TC-AC-PF-544 | E2E | TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | FE+BE |
| TC-AC-PF-545 | E2E | TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | FE+BE |
| TC-AC-PF-546 | E2E | TC-AC-PF-E2E-126-efek-lintas-modul-dropdown-plan-subscription-versi | FE+BE |
| TC-AC-PF-547 | E2E | TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission | FE+BE |
| TC-AC-PF-548 | E2E | TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission | FE+BE |
| TC-AC-PF-549 | E2E | TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | FE+BE |
| TC-AC-PF-550 | E2E | TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission | FE+BE |
| TC-AC-PF-551 | E2E | TC-AC-PF-E2E-127-lintas-modul-cap-custom-field-fams-dan-perubahan-role-permission | FE+BE |
| TC-AC-PF-552 | E2E | TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail | FE+BE |
| TC-AC-PF-553 | E2E | TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive | FE+BE |
| TC-AC-PF-554 | E2E | TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive | FE+BE |
| TC-AC-PF-555 | E2E | TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive | FE+BE |
| TC-AC-PF-556 | E2E | TC-AC-PF-E2E-205-server-menolak-distributor-untuk-create-edit-archive | FE+BE |
| TC-AC-PF-557 | E2E | TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete | FE+BE |
| TC-AC-PF-558 | E2E | TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan | FE+BE |
| TC-AC-PF-559 | E2E | TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan | FE+BE |
| TC-AC-PF-560 | E2E | TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan | FE+BE |
| TC-AC-PF-561 | E2E | TC-AC-PF-E2E-207-server-menolak-distributor-atas-custom-plan-principal-dan | FE+BE |
| TC-AC-PF-562 | E2E | TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca | FE+BE |
| TC-AC-PF-563 | E2E | TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca | FE+BE |
| TC-AC-PF-564 | E2E | TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca | FE+BE |
| TC-AC-PF-565 | E2E | TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin | FE+BE |
| TC-AC-PF-566 | E2E | TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin | FE+BE |
| TC-AC-PF-567 | E2E | TC-AC-PF-E2E-025-konkurensi-capability-dicabut-dan-entitas-suspended-saat-form-dialog-terbuka | FE+BE |
| TC-AC-PF-568 | E2E | TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin | FE+BE |
| TC-AC-PF-569 | E2E | TC-AC-PF-E2E-209-server-menolak-push-update-dan-client-detail-tanpa-izin | FE+BE |
| TC-AC-PF-570 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-571 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-572 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-573 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-574 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-575 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-576 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-577 | E2E | TC-AC-PF-E2E-210-invarian-server-default-plan-slot-free-paid-posisi-tier | FE+BE |
| TC-AC-PF-578 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-579 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-580 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-581 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-582 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-583 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-584 | E2E | TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | FE+BE |
| TC-AC-PF-585 | E2E | TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | FE+BE |
| TC-AC-PF-586 | E2E | TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | FE+BE |
| TC-AC-PF-587 | E2E | TC-AC-PF-E2E-013-konkurensi-dua-admin-create-custom-default-plan-bersamaan-dan-ceiling-paid | FE+BE |
| TC-AC-PF-588 | E2E | TC-AC-PF-E2E-013-konkurensi-dua-admin-create-custom-default-plan-bersamaan-dan-ceiling-paid | FE+BE |
| TC-AC-PF-589 | E2E | TC-AC-PF-E2E-013-konkurensi-dua-admin-create-custom-default-plan-bersamaan-dan-ceiling-paid | FE+BE |
| TC-AC-PF-590 | E2E | TC-AC-PF-E2E-014-konkurensi-edit-vs-edit-dan-save-global-settings-bersamaan | FE+BE |
| TC-AC-PF-591 | E2E | TC-AC-PF-E2E-014-konkurensi-edit-vs-edit-dan-save-global-settings-bersamaan | FE+BE |
| TC-AC-PF-592 | E2E | TC-AC-PF-E2E-014-konkurensi-edit-vs-edit-dan-save-global-settings-bersamaan | FE+BE |
| TC-AC-PF-593 | E2E | TC-AC-PF-E2E-015-konkurensi-archive-dan-retry-archive-oleh-sesi-lain-edit-plan-yang-di-archive | FE+BE |
| TC-AC-PF-594 | E2E | TC-AC-PF-E2E-015-konkurensi-archive-dan-retry-archive-oleh-sesi-lain-edit-plan-yang-di-archive | FE+BE |
| TC-AC-PF-595 | E2E | TC-AC-PF-E2E-016-konkurensi-retry-delete-plan-name-diklik-setelah-plan-dihapus-sesi-lain | FE+BE |
| TC-AC-PF-596 | E2E | TC-AC-PF-E2E-016-konkurensi-retry-delete-plan-name-diklik-setelah-plan-dihapus-sesi-lain | FE+BE |
| TC-AC-PF-597 | E2E | TC-AC-PF-E2E-017-konkurensi-push-update-ke-client-terbaru-dan-template-di-archive-sesi-lain | FE+BE |
| TC-AC-PF-598 | E2E | TC-AC-PF-E2E-015-konkurensi-archive-dan-retry-archive-oleh-sesi-lain-edit-plan-yang-di-archive | FE+BE |
| TC-AC-PF-599 | E2E | TC-AC-PF-E2E-017-konkurensi-push-update-ke-client-terbaru-dan-template-di-archive-sesi-lain | FE+BE |
| TC-AC-PF-600 | E2E | TC-AC-PF-E2E-217-resilience-edit-custom-plan-5xx-tanpa-respons-dan-timing-toast | FE+BE |
| TC-AC-PF-601 | E2E | TC-AC-PF-E2E-201-ambang-download-modal-changelog-default-5-000-dan-5-001 | FE+BE |
| TC-AC-PF-602 | E2E | TC-AC-PF-E2E-201-ambang-download-modal-changelog-default-5-000-dan-5-001 | FE+BE |
| TC-AC-PF-603 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-604 | E2E | TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai | FE+BE |
| TC-AC-PF-605 | E2E | TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai | FE+BE |
| TC-AC-PF-606 | E2E | TC-AC-PF-E2E-222-resilience-download-gagal-tabel-plans-list-dan-plan-detail | FE+BE |
| TC-AC-PF-607 | E2E | TC-AC-PF-E2E-102-dialog-delete-plan-screening-cancel-guard-clients-row | FE+BE |
| TC-AC-PF-608 | E2E | TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda | FE+BE |
| TC-AC-PF-609 | E2E | TC-AC-PF-E2E-056-estimated-reference-price-edit-custom-plan-serta-create-dan-edit-default-plan | FE+BE |
| TC-AC-PF-610 | E2E | TC-AC-PF-E2E-056-estimated-reference-price-edit-custom-plan-serta-create-dan-edit-default-plan | FE+BE |
| TC-AC-PF-611 | E2E | TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail | FE+BE |
| TC-AC-PF-612 | E2E | TC-AC-PF-E2E-009-navigasi-tab-sub-tab-redirect-refresh-back-dan-klik-segmen-breadcrumb | FE+BE |
| TC-AC-PF-613 | E2E | TC-AC-PF-E2E-076-submit-sukses-create-default-plan-free-nama-trim-dan-nama-sama | FE+BE |
| TC-AC-PF-614 | E2E | TC-AC-PF-E2E-070-plan-name-create-default-plan-validasi-keunikan-emoji-dan-batas-120 | FE+BE |
| TC-AC-PF-615 | E2E | TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | FE+BE |
| TC-AC-PF-616 | E2E | TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | FE+BE |
| TC-AC-PF-617 | E2E | TC-AC-PF-E2E-087-plan-name-edit-default-plan-validasi-keunikan-batas-trim | FE+BE |
| TC-AC-PF-618 | E2E | TC-AC-PF-E2E-061-clear-field-create-custom-plan | FE+BE |
| TC-AC-PF-619 | E2E | TC-AC-PF-E2E-193-search-dan-filter-modal-changelog-custom-per-anggota | FE+BE |
| TC-AC-PF-620 | E2E | TC-AC-PF-E2E-193-search-dan-filter-modal-changelog-custom-per-anggota | FE+BE |
| TC-AC-PF-621 | E2E | TC-AC-PF-E2E-194-sort-modal-changelog-custom-per-anggota-dan-search-tanpa | FE+BE |
| TC-AC-PF-622 | E2E | TC-AC-PF-E2E-153-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-623 | E2E | TC-AC-PF-E2E-153-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-624 | E2E | TC-AC-PF-E2E-153-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-625 | E2E | TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-626 | E2E | TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-627 | E2E | TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-628 | E2E | TC-AC-PF-E2E-154-setup-column-default-archive-custom-archive-modal | FE+BE |
| TC-AC-PF-629 | E2E | TC-AC-PF-E2E-202-pagination-modal-changelog-global-settings-dan-archive | FE+BE |
| TC-AC-PF-630 | E2E | TC-AC-PF-E2E-155-screening-overlay-dan-popup-setup-column-default-archive | FE+BE |
| TC-AC-PF-631 | E2E | TC-AC-PF-E2E-155-screening-overlay-dan-popup-setup-column-default-archive | FE+BE |
| TC-AC-PF-632 | E2E | TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal | FE+BE |
| TC-AC-PF-633 | E2E | TC-AC-PF-E2E-173-tab-assigned-clients-term-terminal-term-campuran-term | FE+BE |
| TC-AC-PF-634 | E2E | TC-AC-PF-E2E-173-tab-assigned-clients-term-terminal-term-campuran-term | FE+BE |
| TC-AC-PF-635 | E2E | TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | FE+BE |
| TC-AC-PF-636 | E2E | TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai | FE+BE |
| TC-AC-PF-637 | E2E | TC-AC-PF-E2E-114-global-settings-nilai-kosong-dan-clear-field-dengan-error | FE+BE |
| TC-AC-PF-638 | E2E | TC-AC-PF-E2E-114-global-settings-nilai-kosong-dan-clear-field-dengan-error | FE+BE |
| TC-AC-PF-639 | E2E | TC-AC-PF-E2E-172-isi-berkas-download-tab-assigned-clients-bom-sheet-plan | FE+BE |
| TC-AC-PF-640 | E2E | TC-AC-PF-E2E-177-tab-assigned-clients-term-campuran-dan-term-trial | FE+BE |
| TC-AC-PF-641 | E2E | TC-AC-PF-E2E-140-pagination-tab-default-active-dan-archive-baris-terakhir | FE+BE |
| TC-AC-PF-642 | E2E | TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | FE+BE |
| TC-AC-PF-643 | E2E | TC-AC-PF-E2E-072-clear-field-dan-unsaved-changes-dasar-create-default-plan | FE+BE |
| TC-AC-PF-644 | E2E | TC-AC-PF-E2E-046-tooltip-keyboard-focus-dan-wrap-teks-panjang | FE+BE |
| TC-AC-PF-645 | E2E | TC-AC-PF-E2E-045-guided-tooltip-indikator-step-keyboard-dan-penutupan-overlay | FE+BE |
| TC-AC-PF-646 | E2E | TC-AC-PF-E2E-208-server-menolak-suspended-distributor-read-only-dan-baca | FE+BE |
| TC-AC-PF-647 | E2E | TC-AC-PF-E2E-157-download-plan-detail-nama-berkas-baris-kondisional-nilai | FE+BE |
| TC-AC-PF-648 | E2E | TC-AC-PF-E2E-093-edit-api-call-quota-custom-bernilai-sama-dengan-preset | FE+BE |
| TC-AC-PF-649 | E2E | TC-AC-PF-E2E-094-edit-default-plan-api-call-quota-custom-sama-dengan-preset-dan-format-changelog | FE+BE |
| TC-AC-PF-650 | E2E | TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda | FE+BE |
| TC-AC-PF-651 | E2E | TC-AC-PF-E2E-189-isi-berkas-download-modal-changelog-default-bom-sheet | FE+BE |
| TC-AC-PF-652 | E2E | TC-AC-PF-E2E-190-isi-berkas-download-modal-changelog-custom-dan-global | FE+BE |
| TC-AC-PF-653 | E2E | TC-AC-PF-E2E-190-isi-berkas-download-modal-changelog-custom-dan-global | FE+BE |
| TC-AC-PF-654 | E2E | TC-AC-PF-E2E-196-modal-changelog-global-settings-sort | FE+BE |
| TC-AC-PF-655 | E2E | TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | FE+BE |
| TC-AC-PF-656 | E2E | TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete | FE+BE |
| TC-AC-PF-657 | E2E | TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete | FE+BE |
| TC-AC-PF-658 | E2E | TC-AC-PF-E2E-206-server-menolak-partner-untuk-create-edit-archive-delete | FE+BE |
| TC-AC-PF-659 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-660 | E2E | TC-AC-PF-E2E-083-edit-custom-plan-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-PF-661 | E2E | TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5 | FE+BE |
| TC-AC-PF-662 | E2E | TC-AC-PF-E2E-114-global-settings-nilai-kosong-dan-clear-field-dengan-error | FE+BE |
| TC-AC-PF-663 | E2E | TC-AC-PF-E2E-091-edit-default-plan-clear-field-unsaved-changes-refresh-f5 | FE+BE |
| TC-AC-PF-664 | E2E | TC-AC-PF-E2E-077-form-bersih-dan-refresh-create-default-plan | FE+BE |
| TC-AC-PF-665 | E2E | TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | FE+BE |
| TC-AC-PF-666 | E2E | TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | FE+BE |
| TC-AC-PF-667 | E2E | TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc | FE+BE |
| TC-AC-PF-668 | E2E | TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | FE+BE |
| TC-AC-PF-669 | E2E | TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | FE+BE |
| TC-AC-PF-670 | E2E | TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | FE+BE |
| TC-AC-PF-671 | E2E | TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | FE+BE |
| TC-AC-PF-672 | E2E | TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | FE+BE |
| TC-AC-PF-673 | E2E | TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | FE+BE |
| TC-AC-PF-674 | E2E | TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc | FE+BE |
| TC-AC-PF-675 | E2E | TC-AC-PF-E2E-097-archive-custom-plan-sukses-header-plan-detail-klik-ganda | FE+BE |
| TC-AC-PF-676 | E2E | TC-AC-PF-E2E-103-delete-plan-archived-sukses-klik-ganda-bekas-template | FE+BE |
| TC-AC-PF-677 | E2E | TC-AC-PF-E2E-110-confirm-push-update-sukses-plan-free-diff-preset-klik-ganda | FE+BE |
| TC-AC-PF-678 | E2E | TC-AC-PF-E2E-003-empty-state-genuinely-kosong-dataset-e-pada-list-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-679 | E2E | TC-AC-PF-E2E-221-resilience-error-load-tab-assigned-clients-dan-modal | FE+BE |
| TC-AC-PF-680 | E2E | TC-AC-PF-E2E-194-sort-modal-changelog-custom-per-anggota-dan-search-tanpa | FE+BE |
| TC-AC-PF-681 | E2E | TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again | FE+BE |
| TC-AC-PF-682 | E2E | TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again | FE+BE |
| TC-AC-PF-683 | E2E | TC-AC-PF-E2E-220-resilience-error-load-tabel-plans-list-dan-try-again | FE+BE |
| TC-AC-PF-684 | E2E | TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-685 | E2E | TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-686 | E2E | TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-687 | E2E | TC-AC-PF-E2E-004-loading-state-tabel-plans-list-assigned-clients-dan-tiga-modal-changelog | FE+BE |
| TC-AC-PF-688 | E2E | TC-AC-PF-E2E-141-download-plans-list-tab-default-nama-berkas-search-column | FE+BE |
| TC-AC-PF-689 | E2E | TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris | FE+BE |
| TC-AC-PF-690 | E2E | TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris | FE+BE |
| TC-AC-PF-691 | E2E | TC-AC-PF-E2E-200-download-lintas-halaman-dan-pagination-volume-120-baris | FE+BE |
| TC-AC-PF-692 | E2E | TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab | FE+BE |
| TC-AC-PF-693 | E2E | TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab | FE+BE |
| TC-AC-PF-694 | E2E | TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab | FE+BE |
| TC-AC-PF-695 | E2E | TC-AC-PF-E2E-042-tooltip-ikon-toolbar-plans-list-per-tab-dan-sub-tab | FE+BE |
| TC-AC-PF-696 | E2E | TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-697 | E2E | TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-698 | E2E | TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-699 | E2E | TC-AC-PF-E2E-043-tooltip-ikon-filter-assigned-clients-dan-modal-changelog | FE+BE |
| TC-AC-PF-700 | E2E | TC-AC-PF-E2E-060-submit-create-state-submitting-dan-klik-ganda-cepat-custom-dan-default-plan | FE+BE |
| TC-AC-PF-701 | E2E | TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda | FE+BE |
| TC-AC-PF-702 | E2E | TC-AC-PF-E2E-085-edit-custom-dan-default-plan-state-submitting-dan-klik-ganda | FE+BE |
| TC-AC-PF-703 | E2E | TC-AC-PF-E2E-128-global-settings-klik-ganda-save-state-submitting-dan-isi-entri-changelog | FE+BE |
| TC-AC-PF-704 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-705 | E2E | TC-AC-PF-E2E-109-dialog-push-plan-update-screening-tabel-diff-cancel | FE+BE |
| TC-AC-PF-706 | E2E | TC-AC-PF-E2E-101-guard-cannot-archive-plan-status-tidak-menahan-daftar | FE+BE |
| TC-AC-PF-707 | E2E | TC-AC-PF-E2E-204-cache-setup-column-independen-dan-esc-berlapis-modal-changelog-default | FE+BE |
| TC-AC-PF-708 | E2E | TC-AC-PF-E2E-011-isolasi-state-halaman-dan-filter-antar-sub-tab-active-dan-archive-tab-default | FE+BE |
| TC-AC-PF-709 | E2E | TC-AC-PF-E2E-011-isolasi-state-halaman-dan-filter-antar-sub-tab-active-dan-archive-tab-default | FE+BE |
| TC-AC-PF-710 | E2E | TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1 | FE+BE |
| TC-AC-PF-711 | E2E | TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1 | FE+BE |
| TC-AC-PF-712 | E2E | TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1 | FE+BE |
| TC-AC-PF-713 | E2E | TC-AC-PF-E2E-012-isolasi-state-halaman-dan-filter-default-vs-custom-dan-reset-halaman-ke-1 | FE+BE |
| TC-AC-PF-714 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |
| TC-AC-PF-715 | E2E | TC-AC-PF-E2E-144-isi-berkas-download-plans-list-tab-custom-bom-sheet-kutip | FE+BE |
| TC-AC-PF-716 | E2E | TC-AC-PF-E2E-216-resilience-create-custom-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-717 | E2E | TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-718 | E2E | TC-AC-PF-E2E-217-resilience-edit-custom-plan-5xx-tanpa-respons-dan-timing-toast | FE+BE |
| TC-AC-PF-719 | E2E | TC-AC-PF-E2E-224-resilience-create-dan-edit-default-plan-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-720 | E2E | TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan | FE+BE |
| TC-AC-PF-721 | E2E | TC-AC-PF-E2E-219-resilience-push-update-dan-save-global-settings-5xx-dan | FE+BE |
| TC-AC-PF-722 | E2E | TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-723 | E2E | TC-AC-PF-E2E-218-resilience-archive-dan-delete-5xx-dan-tanpa-respons | FE+BE |
| TC-AC-PF-724 | E2E | TC-AC-PF-E2E-145-search-filter-sort-sub-tab-archive-default-dan-custom | FE+BE |
| TC-AC-PF-725 | E2E | TC-AC-PF-E2E-165-sort-tab-assigned-clients-dan-warna-badge-subscription | FE+BE |
| TC-AC-PF-726 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-727 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-728 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-729 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-730 | E2E | TC-AC-PF-E2E-099-archive-default-plan-header-plan-detail-plan-terakhir | FE+BE |
| TC-AC-PF-731 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-732 | E2E | TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | FE+BE |
| TC-AC-PF-733 | E2E | TC-AC-PF-E2E-078-screening-dan-akses-form-edit-custom-plan | FE+BE |
| TC-AC-PF-734 | E2E | TC-AC-PF-E2E-086-screening-form-edit-default-plan-free-dan-paid-dan-feature | FE+BE |
| TC-AC-PF-735 | E2E | TC-AC-PF-E2E-118-global-settings-auto-focus-enter-dan-unsaved-changes-sesudah-save | FE+BE |
| TC-AC-PF-736 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-737 | E2E | TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | FE+BE |
| TC-AC-PF-738 | E2E | TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | FE+BE |
| TC-AC-PF-739 | E2E | TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | FE+BE |
| TC-AC-PF-740 | E2E | TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc | FE+BE |
| TC-AC-PF-741 | E2E | TC-AC-PF-E2E-063-create-plan-form-dikembalikan-identik-f5-auto-focus-enter-dan-esc | FE+BE |
| TC-AC-PF-742 | E2E | TC-AC-PF-E2E-073-unsaved-changes-create-default-plan-sidebar-back-esc-auto | FE+BE |
| TC-AC-PF-743 | E2E | TC-AC-PF-E2E-084-edit-custom-plan-refresh-f5-sidebar-back-esc | FE+BE |
| TC-AC-PF-744 | E2E | TC-AC-PF-E2E-092-edit-default-plan-sidebar-back-esc | FE+BE |
| TC-AC-PF-745 | E2E | TC-AC-PF-E2E-117-global-settings-refresh-f5-back-esc | FE+BE |
| TC-AC-PF-746 | E2E | TC-AC-PF-E2E-053-api-call-quota-custom-spinner-kelipatan-dan-awalan-preset | FE+BE |
| TC-AC-PF-747 | E2E | TC-AC-PF-E2E-177-tab-assigned-clients-term-campuran-dan-term-trial | FE+BE |
| TC-AC-PF-748 | E2E | TC-AC-PF-E2E-177-tab-assigned-clients-term-campuran-dan-term-trial | FE+BE |
| TC-AC-PF-749 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-750 | E2E | TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page | FE+BE |
| TC-AC-PF-751 | E2E | TC-AC-PF-E2E-074-create-default-plan-open-api-off-dan-open-api-on-dengan | FE+BE |
| TC-AC-PF-752 | E2E | TC-AC-PF-E2E-074-create-default-plan-open-api-off-dan-open-api-on-dengan | FE+BE |
| TC-AC-PF-753 | E2E | TC-AC-PF-E2E-075-create-default-plan-batas-api-call-quota-dan-dependency-d | FE+BE |
| TC-AC-PF-754 | E2E | TC-AC-PF-E2E-075-create-default-plan-batas-api-call-quota-dan-dependency-d | FE+BE |
| TC-AC-PF-755 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-756 | E2E | TC-AC-PF-E2E-090-edit-default-plan-open-api-off-on-dan-dependency-d-2-d-4 | FE+BE |
| TC-AC-PF-757 | E2E | TC-AC-PF-E2E-090-edit-default-plan-open-api-off-on-dan-dependency-d-2-d-4 | FE+BE |
| TC-AC-PF-758 | E2E | TC-AC-PF-E2E-090-edit-default-plan-open-api-off-on-dan-dependency-d-2-d-4 | FE+BE |
| TC-AC-PF-759 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-760 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-761 | E2E | TC-AC-PF-E2E-212-validasi-server-api-call-quota-dan-open-api-create-edit | FE+BE |
| TC-AC-PF-762 | E2E | TC-AC-PF-E2E-118-global-settings-auto-focus-enter-dan-unsaved-changes-sesudah-save | FE+BE |
| TC-AC-PF-763 | E2E | TC-AC-PF-E2E-118-global-settings-auto-focus-enter-dan-unsaved-changes-sesudah-save | FE+BE |
| TC-AC-PF-764 | E2E | TC-AC-PF-E2E-099-archive-default-plan-header-plan-detail-plan-terakhir | FE+BE |
| TC-AC-PF-765 | E2E | TC-AC-PF-E2E-112-delete-default-plan-archived-bekas-template-custom-turunan-tidak-berubah | FE+BE |
| TC-AC-PF-766 | E2E | TC-AC-PF-E2E-143-isi-berkas-download-plans-list-tab-default-bom-sheet-tipe | FE+BE |
| TC-AC-PF-767 | E2E | TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | FE+BE |
| TC-AC-PF-768 | E2E | TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | FE+BE |
| TC-AC-PF-769 | E2E | TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | FE+BE |
| TC-AC-PF-770 | E2E | TC-AC-PF-E2E-119-format-tanggal-time-format-12-hour-dan-time-zone-pada-list-dan-changelog | FE+BE |
| TC-AC-PF-771 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-772 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-773 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-774 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-775 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-776 | E2E | TC-AC-PF-E2E-120-kotak-input-date-range-filter-panel-mengikuti-date-format | FE+BE |
| TC-AC-PF-777 | E2E | TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | FE+BE |
| TC-AC-PF-778 | E2E | TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | FE+BE |
| TC-AC-PF-779 | E2E | TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | FE+BE |
| TC-AC-PF-780 | E2E | TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | FE+BE |
| TC-AC-PF-781 | E2E | TC-AC-PF-E2E-016-konkurensi-retry-delete-plan-name-diklik-setelah-plan-dihapus-sesi-lain | FE+BE |
| TC-AC-PF-782 | E2E | TC-AC-PF-E2E-044-plan-name-sebagai-tautan-tab-baru-klik-area-baris-drag | FE+BE |
| TC-AC-PF-783 | E2E | TC-AC-PF-E2E-175-tab-assigned-clients-empty-state-navigasi-client-detail | FE+BE |
| TC-AC-PF-784 | E2E | TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | FE+BE |
| TC-AC-PF-785 | E2E | TC-AC-PF-E2E-183-filter-modal-changelog-default-opsi-and-tanpa-hasil | FE+BE |
| TC-AC-PF-786 | E2E | TC-AC-PF-E2E-213-validasi-server-push-update-downgrade-status-delta-kosong | FE+BE |
| TC-AC-PF-787 | E2E | TC-AC-PF-E2E-018-aksesibilitas-aria-required-form-create-custom-plan | FE+BE |
| TC-AC-PF-788 | E2E | TC-AC-PF-E2E-020-aksesibilitas-aria-required-form-create-default-plan-dan-tab-global-settings | FE+BE |
| TC-AC-PF-789 | E2E | TC-AC-PF-E2E-019-aksesibilitas-aria-required-form-edit-custom-plan-dan-edit-default-plan | FE+BE |
| TC-AC-PF-790 | E2E | TC-AC-PF-E2E-020-aksesibilitas-aria-required-form-create-default-plan-dan-tab-global-settings | FE+BE |
| TC-AC-PF-791 | E2E | TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon | FE+BE |
| TC-AC-PF-792 | E2E | TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon | FE+BE |
| TC-AC-PF-793 | E2E | TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon | FE+BE |
| TC-AC-PF-794 | E2E | TC-AC-PF-E2E-022-aksesibilitas-focus-trap-dialog-archive-delete-dan-cannot-archive-plan | FE+BE |
| TC-AC-PF-795 | E2E | TC-AC-PF-E2E-022-aksesibilitas-focus-trap-dialog-archive-delete-dan-cannot-archive-plan | FE+BE |
| TC-AC-PF-796 | E2E | TC-AC-PF-E2E-023-aksesibilitas-focus-trap-dialog-push-plan-update-dan-unsaved-changes | FE+BE |
| TC-AC-PF-797 | E2E | TC-AC-PF-E2E-023-aksesibilitas-focus-trap-dialog-push-plan-update-dan-unsaved-changes | FE+BE |
| TC-AC-PF-798 | E2E | TC-AC-PF-E2E-021-aksesibilitas-aria-describedby-pesan-error-dan-nama-aksesibel-ikon | FE+BE |
| TC-AC-PF-799 | E2E | TC-AC-PF-E2E-104-delete-plan-archived-yang-seluruh-term-nya-deleted | FE+BE |
| TC-AC-PF-800 | E2E | TC-AC-PF-E2E-211-validasi-server-template-plan-archived-delete-belum | FE+BE |
| TC-AC-PF-801 | E2E | TC-AC-PF-E2E-214-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-802 | E2E | TC-AC-PF-E2E-214-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-803 | E2E | TC-AC-PF-E2E-214-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-804 | E2E | TC-AC-PF-E2E-215-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-805 | E2E | TC-AC-PF-E2E-215-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-806 | E2E | TC-AC-PF-E2E-215-validasi-server-dependency-d-2-d-4-dan-capacity-di-luar | FE+BE |
| TC-AC-PF-807 | E2E | TC-AC-PF-E2E-174-created-by-dan-assigned-by-sebagai-snapshot-saat-akun | FE+BE |
| TC-AC-PF-808 | E2E | TC-AC-PF-E2E-174-created-by-dan-assigned-by-sebagai-snapshot-saat-akun | FE+BE |
| TC-AC-PF-809 | E2E | TC-AC-PF-E2E-174-created-by-dan-assigned-by-sebagai-snapshot-saat-akun | FE+BE |
| TC-AC-PF-810 | E2E | TC-AC-PF-E2E-184-sort-modal-changelog-default-dan-custom | FE+BE |

## 4. Catatan

- Seluruh spec bermode FE+BE; tidak ada spec `Mode: mock`. Kegagalan server (5xx, timeout, error load) memakai intercept parsial di atas backend nyata.
- Pemetaan akhir menyimpang dari rencana awal: dua nomor cadangan per slice seluruhnya terpakai (nomor 001–224 terisi); sejumlah TC berpindah spec dan slug diubah mengikuti isi (nomor tidak berubah). Tabel di atas adalah pemetaan yang berlaku.
- Pengecualian S-06/S-12 untuk data Pre-setup literal mengikuti Lampiran A butir A-6 (`docs/e2e-conventions.md`); pemulihan Dataset bergantung pada fixture backend yang disediakan tim FE/BE.
- Temuan untuk QA (kontradiksi Dataset, langkah atau Expected TC yang ambigu, Post Condition tanpa langkah observasi) dicatat di `## Notes` tiap spec, tidak ditambal diam-diam.
