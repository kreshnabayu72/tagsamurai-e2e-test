# Coverage E2E — Admin Console > Allocation > Client Subscription

Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md` (636 TC granular aktif) dan `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription-backend.md` (126 kasus BE, tidak dipetakan satu per satu).
Suite: `specs/AdminConsole/LicenseAllocationSubscription/`.
Prefix Modul: `AC` + `CS` (`TC-AC-CS-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (160 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | List: Screening Tab Current dan History | FE+BE | 40 | TC-AC-CS-1, TC-AC-CS-2, TC-AC-CS-3, TC-AC-CS-4, TC-AC-CS-7 |
| TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon | List: Toolbar dan Label Aksesibel Ikon | FE+BE | 33 | TC-AC-CS-583, TC-AC-CS-586, TC-AC-CS-35, TC-AC-CS-569 |
| TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | List: Keadaan Kosong Distributor Tanpa Data | FE+BE | 25 | TC-AC-CS-5, TC-AC-CS-6, TC-AC-CS-581, TC-AC-CS-347, TC-AC-CS-400 |
| TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | List: Baris Aktif, Kedaluwarsa, dan Grace | FE+BE | 31 | TC-AC-CS-11, TC-AC-CS-12, TC-AC-CS-13, TC-AC-CS-15, TC-AC-CS-16 |
| TC-AC-CS-E2E-005-list-baris-riwayat-sel-plan-dan-sel-plan-owner | List: Baris Riwayat, Sel Plan, dan Sel Plan Owner | FE+BE | 36 | TC-AC-CS-25, TC-AC-CS-26, TC-AC-CS-17 |
| TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | List: Tanggal Kosong, Navigasi Baris, dan Masuk dari Client Detail | FE+BE | 32 | TC-AC-CS-27, TC-AC-CS-28, TC-AC-CS-29, TC-AC-CS-31, TC-AC-CS-32 |
| TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client | List: Format Subscription ID dan Perilaku Anchor Nama Client | FE+BE | 46 | TC-AC-CS-24, TC-AC-CS-565, TC-AC-CS-566, TC-AC-CS-567 |
| TC-AC-CS-E2E-008-list-baris-requester-distributor | List: Baris Requester Distributor | FE+BE | 21 | TC-AC-CS-9, TC-AC-CS-14, TC-AC-CS-39, TC-AC-CS-52 |
| TC-AC-CS-E2E-009-list-baris-requester-group-manager-dan-partner | List: Baris Requester Group Manager dan Partner | FE+BE | 0 | TC-AC-CS-10, TC-AC-CS-18, TC-AC-CS-53 |
| TC-AC-CS-E2E-010-detail-subscription-info | Detail: Subscription Info | FE+BE | 42 | TC-AC-CS-36, TC-AC-CS-582, TC-AC-CS-57, TC-AC-CS-37, TC-AC-CS-40, TC-AC-CS-38, TC-AC-CS-58 |
| TC-AC-CS-E2E-011-detail-license-quota | Detail: License Quota | FE+BE | 39 | TC-AC-CS-41, TC-AC-CS-636, TC-AC-CS-42, TC-AC-CS-43, TC-AC-CS-44, TC-AC-CS-59 |
| TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | Detail: Feature Entitlement, Addon Features, dan State Loading | FE+BE | 38 | TC-AC-CS-45, TC-AC-CS-48, TC-AC-CS-46, TC-AC-CS-47, TC-AC-CS-49 |
| TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action | Detail: Tombol Aksi mengikuti Row Action | FE+BE | 0 | TC-AC-CS-51, TC-AC-CS-585, TC-AC-CS-54, TC-AC-CS-55 |
| TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama | Guided Tooltip: Isi dan Kunjungan Pertama | FE+BE | 44 | TC-AC-CS-60, TC-AC-CS-61, TC-AC-CS-62, TC-AC-CS-63 |
| TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | Guided Tooltip: Skip, Resize, dan Keyboard | FE+BE | 0 | TC-AC-CS-64, TC-AC-CS-65, TC-AC-CS-66, TC-AC-CS-67, TC-AC-CS-68 |
| TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | Role Matrix: Akses Menu dan URL Langsung per Entitas | FE+BE | 0 | TC-AC-CS-69, TC-AC-CS-71, TC-AC-CS-72, TC-AC-CS-70, TC-AC-CS-73 |
| TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager | Role Matrix: Visibilitas Elemen Role Principal dan Group Manager | FE+BE | 0 | TC-AC-CS-74, TC-AC-CS-30, TC-AC-CS-75, TC-AC-CS-76 |
| TC-AC-CS-E2E-018-role-matrix-visibilitas-elemen-hak-parsial | Role Matrix: Visibilitas Elemen Hak Parsial | FE+BE | 0 | TC-AC-CS-77, TC-AC-CS-78, TC-AC-CS-79 |
| TC-AC-CS-E2E-019-role-matrix-visibilitas-elemen-group-role-a-dan-b | Role Matrix: Visibilitas Elemen Group Role A dan B | FE+BE | 0 | TC-AC-CS-80, TC-AC-CS-330, TC-AC-CS-81 |
| TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client | Zero Access Group C: List, Tooltip, dan Tab Subscription Client Detail | FE+BE | 34 | TC-AC-CS-82, TC-AC-CS-100, TC-AC-CS-564, TC-AC-CS-634 |
| TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses | Capability Create: Add, Activate Trial, Renew, dan Convert sampai Sukses | FE+BE | 35 | TC-AC-CS-83, TC-AC-CS-84, TC-AC-CS-85, TC-AC-CS-86 |
| TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses | Capability: Edit, Cancel Request, Resubmit, dan Cancel Subscription sampai Sukses | FE+BE | 0 | TC-AC-CS-87, TC-AC-CS-88, TC-AC-CS-89, TC-AC-CS-90 |
| TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | Scope Baca per Entitas dan Plan Owner | FE+BE | 0 | TC-AC-CS-91, TC-AC-CS-92, TC-AC-CS-93, TC-AC-CS-393, TC-AC-CS-431, TC-AC-CS-465 |
| TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match | Scope Tulis: Dropdown Client dan Plan Owner Exact Match | FE+BE | 0 | TC-AC-CS-94, TC-AC-CS-95, TC-AC-CS-96, TC-AC-CS-97 |
| TC-AC-CS-E2E-025-scope-tulis-group-manager-descendant-dan-opsi-new-client | Scope Tulis: Group Manager Descendant dan Opsi New Client | FE+BE | 28 | TC-AC-CS-98, TC-AC-CS-99 |
| TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | Form Add: Screening dan Blok Payment | FE+BE | 42 | TC-AC-CS-101, TC-AC-CS-618, TC-AC-CS-534, TC-AC-CS-139, TC-AC-CS-102 |
| TC-AC-CS-E2E-027-form-renew-dan-convert-screening | Form Renew dan Convert: Screening | FE+BE | 43 | TC-AC-CS-103, TC-AC-CS-104, TC-AC-CS-105, TC-AC-CS-131, TC-AC-CS-106 |
| TC-AC-CS-E2E-028-form-add-opsi-dropdown-client-dan-product | Form Add: Opsi Dropdown Client dan Product | FE+BE | 25 | TC-AC-CS-107, TC-AC-CS-108, TC-AC-CS-111 |
| TC-AC-CS-E2E-029-form-add-opsi-plan-dan-pay-from-distributor-dan-partner | Form Add: Opsi Plan dan Pay From Distributor dan Partner | FE+BE | 29 | TC-AC-CS-109, TC-AC-CS-110, TC-AC-CS-556 |
| TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | Form Add: Validasi Client, Product, Plan | FE+BE | 39 | TC-AC-CS-112, TC-AC-CS-113, TC-AC-CS-114, TC-AC-CS-115, TC-AC-CS-116 |
| TC-AC-CS-E2E-031-form-add-validasi-duration | Form Add: Validasi Duration | FE+BE | 20 | TC-AC-CS-117, TC-AC-CS-118, TC-AC-CS-119, TC-AC-CS-120 |
| TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from | Form Add: Validasi Start Date dan Pay From | FE+BE | 27 | TC-AC-CS-121, TC-AC-CS-122, TC-AC-CS-123, TC-AC-CS-124 |
| TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | Form Renew: Validasi dan Preview Renewal | FE+BE | 41 | TC-AC-CS-125, TC-AC-CS-126, TC-AC-CS-127, TC-AC-CS-128, TC-AC-CS-129, TC-AC-CS-130, TC-AC-CS-137, TC-AC-CS-138 |
| TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | Payment Preview: Estimated Cost dan Saldo Kantong | FE+BE | 35 | TC-AC-CS-132, TC-AC-CS-133, TC-AC-CS-134, TC-AC-CS-136, TC-AC-CS-135 |
| TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager | Add: Alert Info dan Bypass Group Manager | FE+BE | 34 | TC-AC-CS-140, TC-AC-CS-141, TC-AC-CS-144, TC-AC-CS-143 |
| TC-AC-CS-E2E-036-add-group-manager-ancestor-dan-start-date-29-februari | Add: Group Manager Ancestor dan Start Date 29 Februari | FE+BE | 26 | TC-AC-CS-554, TC-AC-CS-579, TC-AC-CS-580 |
| TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email | Add: Principal, SIEM, dan Checkbox Stay on this Form | FE+BE | 33 | TC-AC-CS-160, TC-AC-CS-161, TC-AC-CS-145, TC-AC-CS-154 |
| TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | Add dan Renew: Requester dengan Toggle Approval | FE+BE | 47 | TC-AC-CS-146, TC-AC-CS-486, TC-AC-CS-142, TC-AC-CS-147, TC-AC-CS-151 |
| TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new | Add: Distributor Biaya Nol, Renewal Rank Lebih Rendah, dan New Client | FE+BE | 50 | TC-AC-CS-155, TC-AC-CS-153, TC-AC-CS-174, TC-AC-CS-175 |
| TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan | Renew: Efek Langsung, Terjadwal, dan Change Plan | FE+BE | 43 | TC-AC-CS-149, TC-AC-CS-150, TC-AC-CS-152, TC-AC-CS-148 |
| TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | Renew: Blokir, Clear Field, dan Nilai Clean | FE+BE | 37 | TC-AC-CS-163, TC-AC-CS-167, TC-AC-CS-159, TC-AC-CS-158, TC-AC-CS-157 |
| TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | Form Add: Clear Field dan Unsaved Changes | FE+BE | 32 | TC-AC-CS-164, TC-AC-CS-162, TC-AC-CS-166, TC-AC-CS-561, TC-AC-CS-165 |
| TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer | Form: Dirty Guard Backdrop, Reload, Route, dan Footer | FE+BE | 28 | TC-AC-CS-168, TC-AC-CS-169, TC-AC-CS-170, TC-AC-CS-635 |
| TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial | Form: State Submitting dan Klik Ganda Add dan Activate Trial | FE+BE | 39 | TC-AC-CS-171, TC-AC-CS-522, TC-AC-CS-621, TC-AC-CS-523 |
| TC-AC-CS-E2E-045-aksesibilitas-form-add-activate-trial-dan-edit | Aksesibilitas Form Add, Activate Trial, dan Edit | FE+BE | 33 | TC-AC-CS-568, TC-AC-CS-622, TC-AC-CS-623 |
| TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | Activate Trial: Screening dan Nilai Awal | FE+BE | 41 | TC-AC-CS-176, TC-AC-CS-181, TC-AC-CS-177, TC-AC-CS-180, TC-AC-CS-182 |
| TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas | Activate Trial: Opsi Plan dan Eligibilitas | FE+BE | 31 | TC-AC-CS-178, TC-AC-CS-179, TC-AC-CS-194, TC-AC-CS-195 |
| TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan | Activate Trial: Validasi Client, Product, Plan | FE+BE | 28 | TC-AC-CS-183, TC-AC-CS-184, TC-AC-CS-185, TC-AC-CS-186 |
| TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | Activate Trial: Ceiling dan Input Digit | FE+BE | 38 | TC-AC-CS-187, TC-AC-CS-188, TC-AC-CS-211, TC-AC-CS-572, TC-AC-CS-192 |
| TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah | Activate Trial: Kuota Kosong dan Batas Bawah | FE+BE | 38 | TC-AC-CS-189, TC-AC-CS-190, TC-AC-CS-191, TC-AC-CS-193 |
| TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | Activate Trial: Principal dan Inisialisasi Kuota | FE+BE | 44 | TC-AC-CS-199, TC-AC-CS-203, TC-AC-CS-204, TC-AC-CS-205, TC-AC-CS-206 |
| TC-AC-CS-E2E-052-activate-trial-toggle-approval-distributor-dan-partner | Activate Trial: Toggle Approval Distributor dan Partner | FE+BE | 31 | TC-AC-CS-200, TC-AC-CS-201, TC-AC-CS-202 |
| TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | Activate Trial: Form Dirty dan Backdrop | FE+BE | 28 | TC-AC-CS-207, TC-AC-CS-208, TC-AC-CS-542, TC-AC-CS-558, TC-AC-CS-574 |
| TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | State Tenant: Client Suspended dan Expired pada Add, Renew, Activate Trial | FE+BE | 37 | TC-AC-CS-196, TC-AC-CS-197, TC-AC-CS-198, TC-AC-CS-528, TC-AC-CS-529 |
| TC-AC-CS-E2E-055-state-tenant-cancel-job-dan-suspend-trial-pada-client | State Tenant: Cancel, Job, dan Suspend Trial pada Client Suspended atau Expired | FE+BE | 23 | TC-AC-CS-549, TC-AC-CS-268, TC-AC-CS-531 |
| TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada | State Tenant: Approve Trial, Cancel Request, dan Resubmit pada Client Suspended | FE+BE | 33 | TC-AC-CS-305, TC-AC-CS-279, TC-AC-CS-530, TC-AC-CS-612 |
| TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | Edit: Screening dan Field Terkunci | FE+BE | 34 | TC-AC-CS-212, TC-AC-CS-213, TC-AC-CS-214, TC-AC-CS-215, TC-AC-CS-236 |
| TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | Edit: Validasi Duration, Start Date, dan Ceiling Trial | FE+BE | 34 | TC-AC-CS-217, TC-AC-CS-218, TC-AC-CS-220, TC-AC-CS-221, TC-AC-CS-222, TC-AC-CS-620 |
| TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo | Edit: Hasil Re-Approval dan Saldo | FE+BE | 46 | TC-AC-CS-223, TC-AC-CS-224, TC-AC-CS-229, TC-AC-CS-230 |
| TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi | Edit: Tanpa Perubahan, Trial, dan Alokasi | FE+BE | 34 | TC-AC-CS-232, TC-AC-CS-233, TC-AC-CS-234, TC-AC-CS-550 |
| TC-AC-CS-E2E-061-edit-group-manager-bypass | Edit: Group Manager Bypass | FE+BE | 39 | TC-AC-CS-219, TC-AC-CS-225, TC-AC-CS-226, TC-AC-CS-227, TC-AC-CS-228 |
| TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes | Edit: Dirty Guard dan Unsaved Changes | FE+BE | 26 | TC-AC-CS-237, TC-AC-CS-543, TC-AC-CS-544, TC-AC-CS-559 |
| TC-AC-CS-E2E-063-convert-trial-row-action-dan-dialog-instan-atau-request | Convert Trial: Row Action dan Dialog Instan atau Request | FE+BE | 41 | TC-AC-CS-239, TC-AC-CS-240, TC-AC-CS-241 |
| TC-AC-CS-E2E-064-convert-trial-group-manager-jalur-instan | Convert Trial: Group Manager Jalur Instan | FE+BE | 34 | TC-AC-CS-243, TC-AC-CS-245, TC-AC-CS-255 |
| TC-AC-CS-E2E-065-convert-trial-requester-jalur-request | Convert Trial: Requester Jalur Request | FE+BE | 31 | TC-AC-CS-244, TC-AC-CS-246, TC-AC-CS-256 |
| TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa | Convert Trial: Principal, Trial Expired, dan Dialog Tanpa Estimated Cost | FE+BE | 35 | TC-AC-CS-242, TC-AC-CS-552, TC-AC-CS-248, TC-AC-CS-247 |
| TC-AC-CS-E2E-067-convert-trial-data-asset-dan-rantai-trial | Convert Trial: Data Asset dan Rantai Trial | FE+BE | 25 | TC-AC-CS-249, TC-AC-CS-250, TC-AC-CS-251 |
| TC-AC-CS-E2E-068-cancel-subscription-dialog | Cancel Subscription: Dialog | FE+BE | 36 | TC-AC-CS-259, TC-AC-CS-261, TC-AC-CS-260, TC-AC-CS-269, TC-AC-CS-560 |
| TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi | Cancel Subscription: Efek dan Alokasi | FE+BE | 42 | TC-AC-CS-263, TC-AC-CS-264, TC-AC-CS-265, TC-AC-CS-262 |
| TC-AC-CS-E2E-070-cancel-request-requester | Cancel Request: Requester | FE+BE | 41 | TC-AC-CS-270, TC-AC-CS-545, TC-AC-CS-272, TC-AC-CS-273, TC-AC-CS-275 |
| TC-AC-CS-E2E-071-cancel-request-perubahan-status-dan-pending-diedit | Cancel Request: Perubahan Status dan Pending Diedit | FE+BE | 30 | TC-AC-CS-276, TC-AC-CS-547, TC-AC-CS-632 |
| TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | Cancel Request: Group Manager dan Total Control | FE+BE | 51 | TC-AC-CS-271, TC-AC-CS-274, TC-AC-CS-555, TC-AC-CS-624, TC-AC-CS-278, TC-AC-CS-536 |
| TC-AC-CS-E2E-073-resubmit-partner-timeout-auto-cancel | Resubmit: Partner Timeout Auto-Cancel | FE+BE | 37 | TC-AC-CS-280, TC-AC-CS-285, TC-AC-CS-23 |
| TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | Resubmit dan Edit Renewal: Partner Trial | FE+BE | 37 | TC-AC-CS-282, TC-AC-CS-286, TC-AC-CS-615, TC-AC-CS-210, TC-AC-CS-216 |
| TC-AC-CS-E2E-075-resubmit-distributor-dan-principal | Resubmit: Distributor dan Principal | FE+BE | 36 | TC-AC-CS-281, TC-AC-CS-284, TC-AC-CS-283 |
| TC-AC-CS-E2E-076-job-scheduled-flip | Job: Scheduled Flip | FE+BE | 32 | TC-AC-CS-287, TC-AC-CS-535, TC-AC-CS-288 |
| TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire | Job: Flip Lanjutan dan Race Auto-Expire | FE+BE | 32 | TC-AC-CS-20, TC-AC-CS-289, TC-AC-CS-481, TC-AC-CS-254 |
| TC-AC-CS-E2E-078-job-pre-timeout-warning-dan-timeout-auto-cancel | Job: Pre-timeout Warning dan Timeout Auto-Cancel | FE+BE | 43 | TC-AC-CS-292, TC-AC-CS-625, TC-AC-CS-294 |
| TC-AC-CS-E2E-079-job-timeout-auto-cancel-lanjutan | Job: Timeout Auto-Cancel Lanjutan | FE+BE | 34 | TC-AC-CS-293, TC-AC-CS-296, TC-AC-CS-295 |
| TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new | Approvals: Approve dan Reject Mode New | FE+BE | 40 | TC-AC-CS-297, TC-AC-CS-298, TC-AC-CS-299, TC-AC-CS-310 |
| TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal | Approvals: Approve dan Reject Renewal | FE+BE | 44 | TC-AC-CS-301, TC-AC-CS-302, TC-AC-CS-551, TC-AC-CS-21 |
| TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | Approvals: Approve dan Reject Convert | FE+BE | 57 | TC-AC-CS-306, TC-AC-CS-307, TC-AC-CS-308, TC-AC-CS-309, TC-AC-CS-300 |
| TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal | Approvals: Trial Activation oleh Additional Approver Principal | FE+BE | 46 | TC-AC-CS-303, TC-AC-CS-304, TC-AC-CS-557, TC-AC-CS-553 |
| TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas | List Search: Reveal, Enter, dan Kolom Identitas | FE+BE | 35 | TC-AC-CS-311, TC-AC-CS-312, TC-AC-CS-313, TC-AC-CS-314 |
| TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | List Search: Kolom Plan, Product, Status, dan Tanggal | FE+BE | 24 | TC-AC-CS-315, TC-AC-CS-316, TC-AC-CS-317, TC-AC-CS-318, TC-AC-CS-324 |
| TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | List Search: Visibilitas Kolom, Tab, dan Karakter Khusus | FE+BE | 29 | TC-AC-CS-319, TC-AC-CS-320, TC-AC-CS-321, TC-AC-CS-322, TC-AC-CS-323 |
| TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | List Filter: Screening dan Opsi Dropdown | FE+BE | 36 | TC-AC-CS-325, TC-AC-CS-326, TC-AC-CS-327, TC-AC-CS-328, TC-AC-CS-329 |
| TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | List Filter: Opsi Status dan Perilaku per Kelas | FE+BE | 36 | TC-AC-CS-331, TC-AC-CS-332, TC-AC-CS-333, TC-AC-CS-334, TC-AC-CS-335 |
| TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and | List Filter: Date Range, Grace End, OR dan AND | FE+BE | 16 | TC-AC-CS-336, TC-AC-CS-337, TC-AC-CS-338, TC-AC-CS-339 |
| TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip | List Filter: Pencarian dalam Dropdown dan Chip | FE+BE | 28 | TC-AC-CS-340, TC-AC-CS-341, TC-AC-CS-342, TC-AC-CS-343 |
| TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | List Filter: Chip Lanjutan dan Pemulihan Opsi | FE+BE | 25 | TC-AC-CS-344, TC-AC-CS-345, TC-AC-CS-346, TC-AC-CS-575, TC-AC-CS-576, TC-AC-CS-348 |
| TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | List Sort: Default dan Siklus Kolom | FE+BE | 31 | TC-AC-CS-349, TC-AC-CS-350, TC-AC-CS-351, TC-AC-CS-352, TC-AC-CS-353 |
| TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker | List Sort: Tanggal, Nilai Kosong, dan Tie-breaker | FE+BE | 22 | TC-AC-CS-354, TC-AC-CS-355, TC-AC-CS-356, TC-AC-CS-357 |
| TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination | List: Kombinasi Search Filter Sort Pagination | FE+BE | 29 | TC-AC-CS-358, TC-AC-CS-359, TC-AC-CS-360, TC-AC-CS-364 |
| TC-AC-CS-E2E-095-list-clear-filter-dan-clear-search-saat-kombinasi-aktif | List: Clear Filter dan Clear Search Saat Kombinasi Aktif | FE+BE | 22 | TC-AC-CS-361, TC-AC-CS-362, TC-AC-CS-363 |
| TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | List Setup Column: Screening, Hide, Curated, Urutan, Pin | FE+BE | 42 | TC-AC-CS-365, TC-AC-CS-366, TC-AC-CS-367, TC-AC-CS-368, TC-AC-CS-369, TC-AC-CS-370 |
| TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama | List Setup Column: Overlay, Guard, dan Cache Bersama | FE+BE | 32 | TC-AC-CS-376, TC-AC-CS-373, TC-AC-CS-374, TC-AC-CS-375 |
| TC-AC-CS-E2E-098-list-setup-column-anggota-hideable-lain | List Setup Column: Anggota Hideable Lain | FE+BE | 25 | TC-AC-CS-626, TC-AC-CS-627, TC-AC-CS-628 |
| TC-AC-CS-E2E-099-list-pagination | List Pagination | FE+BE | 36 | TC-AC-CS-377, TC-AC-CS-378, TC-AC-CS-379, TC-AC-CS-380, TC-AC-CS-381, TC-AC-CS-382 |
| TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | List Download: Cakupan, Filter, Kolom, dan Volume 5.001 Baris | FE+BE | 33 | TC-AC-CS-383, TC-AC-CS-384, TC-AC-CS-385, TC-AC-CS-386, TC-AC-CS-388, TC-AC-CS-392 |
| TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx | List Download: Isi Berkas CSV dan XLSX | FE+BE | 24 | TC-AC-CS-389, TC-AC-CS-390, TC-AC-CS-391, TC-AC-CS-472 |
| TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar | List State Preservation: Detail, F5, dan Sidebar | FE+BE | 30 | TC-AC-CS-394, TC-AC-CS-395, TC-AC-CS-396, TC-AC-CS-397 |
| TC-AC-CS-E2E-103-list-state-preservation-memori-per-tab | List State Preservation: Memori per Tab | FE+BE | 26 | TC-AC-CS-33, TC-AC-CS-34, TC-AC-CS-56 |
| TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | Changelog: Screening, State, dan Format Sel | FE+BE | 46 | TC-AC-CS-398, TC-AC-CS-399, TC-AC-CS-401, TC-AC-CS-403, TC-AC-CS-404, TC-AC-CS-405 |
| TC-AC-CS-E2E-105-changelog-search | Changelog: Search | FE+BE | 26 | TC-AC-CS-406, TC-AC-CS-407, TC-AC-CS-408, TC-AC-CS-409 |
| TC-AC-CS-E2E-106-changelog-filter-panel-1 | Changelog: Filter Panel (1) | FE+BE | 28 | TC-AC-CS-410, TC-AC-CS-411, TC-AC-CS-412, TC-AC-CS-413, TC-AC-CS-414 |
| TC-AC-CS-E2E-107-changelog-filter-panel-2 | Changelog: Filter Panel (2) | FE+BE | 22 | TC-AC-CS-415, TC-AC-CS-416, TC-AC-CS-417, TC-AC-CS-418 |
| TC-AC-CS-E2E-108-changelog-sort | Changelog: Sort | FE+BE | 26 | TC-AC-CS-419, TC-AC-CS-420, TC-AC-CS-421 |
| TC-AC-CS-E2E-109-changelog-setup-column | Changelog: Setup Column | FE+BE | 29 | TC-AC-CS-422, TC-AC-CS-423, TC-AC-CS-424, TC-AC-CS-425, TC-AC-CS-426, TC-AC-CS-427 |
| TC-AC-CS-E2E-110-changelog-setup-column-anggota-hideable-lain | Changelog: Setup Column Anggota Hideable Lain | FE+BE | 22 | TC-AC-CS-629, TC-AC-CS-630, TC-AC-CS-631 |
| TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit | Log Aksi: Add, Activate Trial, Convert, dan Activate akibat Edit | FE+BE | 34 | TC-AC-CS-432, TC-AC-CS-433, TC-AC-CS-434, TC-AC-CS-440 |
| TC-AC-CS-E2E-112-log-aksi-renew | Log Aksi: Renew | FE+BE | 33 | TC-AC-CS-435, TC-AC-CS-437, TC-AC-CS-613, TC-AC-CS-436 |
| TC-AC-CS-E2E-113-log-aksi-job-sistem | Log Aksi: Job Sistem | FE+BE | 49 | TC-AC-CS-438, TC-AC-CS-439, TC-AC-CS-441, TC-AC-CS-453, TC-AC-CS-456 |
| TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date | Log Aksi: Edit Duration, Pending, dan Start Date | FE+BE | 33 | TC-AC-CS-444, TC-AC-CS-446, TC-AC-CS-447, TC-AC-CS-445 |
| TC-AC-CS-E2E-115-log-aksi-edit-trial | Log Aksi: Edit Trial | FE+BE | 23 | TC-AC-CS-448, TC-AC-CS-449, TC-AC-CS-450 |
| TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request | Log Aksi: Cancel dan Cancel Request | FE+BE | 35 | TC-AC-CS-451, TC-AC-CS-452, TC-AC-CS-614, TC-AC-CS-455 |
| TC-AC-CS-E2E-117-log-aksi-resubmit | Log Aksi: Resubmit | FE+BE | 23 | TC-AC-CS-454, TC-AC-CS-457, TC-AC-CS-616 |
| TC-AC-CS-E2E-118-log-absence-tanpa-perubahan-dan-lintas-record | Log Absence: Tanpa Perubahan dan Lintas Record | FE+BE | 29 | TC-AC-CS-231, TC-AC-CS-458, TC-AC-CS-464 |
| TC-AC-CS-E2E-119-log-absence-approve-dan-reject | Log Absence: Approve dan Reject | FE+BE | 32 | TC-AC-CS-442, TC-AC-CS-443, TC-AC-CS-617 |
| TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | Integritas Log: Entri per Field dan per Term | FE+BE | 56 | TC-AC-CS-459, TC-AC-CS-460, TC-AC-CS-463, TC-AC-CS-461, TC-AC-CS-462 |
| TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete | Integritas Log: Entri Lama, Format, dan Tanpa Delete | FE+BE | 39 | TC-AC-CS-466, TC-AC-CS-467, TC-AC-CS-468, TC-AC-CS-469 |
| TC-AC-CS-E2E-122-subscription-log-modal-dan-header | Subscription Log: Modal dan Header | FE+BE | 49 | TC-AC-CS-587, TC-AC-CS-588, TC-AC-CS-589 |
| TC-AC-CS-E2E-123-subscription-log-entri-detail-dan-role | Subscription Log: Entri Detail dan Role | FE+BE | 35 | TC-AC-CS-591, TC-AC-CS-592 |
| TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | Subscription Log: Katalog Created, Approved, Rejected, Edited | FE+BE | 42 | TC-AC-CS-594, TC-AC-CS-595, TC-AC-CS-596, TC-AC-CS-597, TC-AC-CS-598 |
| TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated | Subscription Log: Katalog Canceled, Archived, Activated | FE+BE | 43 | TC-AC-CS-599, TC-AC-CS-600, TC-AC-CS-601, TC-AC-CS-605 |
| TC-AC-CS-E2E-126-subscription-log-entri-hasil-job | Subscription Log: Entri Hasil Job | FE+BE | 46 | TC-AC-CS-602, TC-AC-CS-603, TC-AC-CS-604 |
| TC-AC-CS-E2E-127-subscription-log-katalog-renew-convert-resubmit-urutan | Subscription Log: Katalog Renew, Convert, Resubmit, Urutan | FE+BE | 38 | TC-AC-CS-606, TC-AC-CS-607, TC-AC-CS-608 |
| TC-AC-CS-E2E-128-format-tanggal-general-settings-dan-zona-waktu-plan-owner | Format Tanggal General Settings dan Zona Waktu Plan Owner | FE+BE | 29 | TC-AC-CS-470, TC-AC-CS-471, TC-AC-CS-473 |
| TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation | Modul Konsumen: Client Detail, Dashboard, dan License Allocation | FE+BE | 29 | TC-AC-CS-474, TC-AC-CS-476, TC-AC-CS-479, TC-AC-CS-475 |
| TC-AC-CS-E2E-130-wallet-dan-pengajuan-di-approvals | Wallet dan Pengajuan di Approvals | FE+BE | 42 | TC-AC-CS-477, TC-AC-CS-478, TC-AC-CS-482 |
| TC-AC-CS-E2E-131-notifikasi-in-app-approver | Notifikasi In-App: Approver | FE+BE | 35 | TC-AC-CS-488, TC-AC-CS-489, TC-AC-CS-492, TC-AC-CS-570, TC-AC-CS-493 |
| TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role | Notifikasi In-App: Requester dan Multi-role | FE+BE | 18 | TC-AC-CS-490, TC-AC-CS-491, TC-AC-CS-571, TC-AC-CS-494 |
| TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | Defense-in-Depth: Request Langsung Aksi Trial, Add, Renew, Convert | FE+BE | 28 | TC-AC-CS-498, TC-AC-CS-499, TC-AC-CS-500, TC-AC-CS-501, TC-AC-CS-502, TC-AC-CS-503, TC-AC-CS-504, TC-AC-CS-505 |
| TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | Defense-in-Depth: Cancel, Markup, Payload, dan Detail | FE+BE | 42 | TC-AC-CS-506, TC-AC-CS-573, TC-AC-CS-611, TC-AC-CS-514, TC-AC-CS-619 |
| TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | Defense-in-Depth: Zero Access dan Read Only | FE+BE | 28 | TC-AC-CS-495, TC-AC-CS-496, TC-AC-CS-610, TC-AC-CS-497, TC-AC-CS-513 |
| TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | Defense-in-Depth: Requester dan Scope Distributor | FE+BE | 27 | TC-AC-CS-507, TC-AC-CS-511, TC-AC-CS-510, TC-AC-CS-508, TC-AC-CS-509, TC-AC-CS-512 |
| TC-AC-CS-E2E-137-multi-konteks-dua-admin-sesi-bersamaan-principal | Multi-konteks: Dua Admin Sesi Bersamaan Principal | FE+BE | 26 | TC-AC-CS-483, TC-AC-CS-515 |
| TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan | Multi-konteks: Approver dan Requester Bersamaan | FE+BE | 50 | TC-AC-CS-518, TC-AC-CS-519, TC-AC-CS-520, TC-AC-CS-578 |
| TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | Resilience: Gagal Baca List, Detail, Log, dan Download | FE+BE | 46 | TC-AC-CS-8, TC-AC-CS-50, TC-AC-CS-593, TC-AC-CS-402, TC-AC-CS-387, TC-AC-CS-430 |
| TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel | Resilience: Gagal Tulis Add, Renew, Activate Trial, Cancel Subscription | FE+BE | 43 | TC-AC-CS-172, TC-AC-CS-173, TC-AC-CS-209, TC-AC-CS-266 |
| TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request | Resilience: Gagal Tulis Edit, Convert, Cancel Request | FE+BE | 45 | TC-AC-CS-235, TC-AC-CS-277, TC-AC-CS-257, TC-AC-CS-258 |
| TC-AC-CS-E2E-142-klik-ganda-cancel-subscription-dan-convert | Klik Ganda Cancel Subscription dan Convert | FE+BE | 35 | TC-AC-CS-524, TC-AC-CS-527, TC-AC-CS-267 |
| TC-AC-CS-E2E-143-klik-ganda-cancel-request-dan-save-edit-state-submitting-save | Klik Ganda Cancel Request dan Save Edit, State Submitting Save | FE+BE | 25 | TC-AC-CS-525, TC-AC-CS-526, TC-AC-CS-238 |
| TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | Kondisi Sisa: Ceiling, Back Browser, Plan Archive, Tier, Toast | FE+BE | 47 | TC-AC-CS-537, TC-AC-CS-538, TC-AC-CS-539, TC-AC-CS-540, TC-AC-CS-562 |
| TC-AC-CS-E2E-145-list-ikon-dan-color-role-row-action | List: Ikon dan Color Role Row Action | FE+BE | 0 | TC-AC-CS-541 |
| TC-AC-CS-E2E-146-list-baris-trial-riwayat-dan-client-archive | List: Baris Trial Riwayat dan Client Archive di Dropdown | FE+BE | 0 | TC-AC-CS-22, TC-AC-CS-19 |
| TC-AC-CS-E2E-147-edit-duration-start-date-29-februari | Edit Duration: Start Date 29 Februari Menghitung Ulang End Date | FE+BE | 19 | TC-AC-CS-584 |
| TC-AC-CS-E2E-148-activation-email-dan-app-access-pada-term-pertama | Add: Activation Email dan App Access Hanya pada Term Pertama Client | FE+BE | 23 | TC-AC-CS-156 |
| TC-AC-CS-E2E-149-convert-trial-plan-free-dan-predecessor-bersuccessor | Convert Trial: Plan Free dan Predecessor Bersuccessor | FE+BE | 13 | TC-AC-CS-252, TC-AC-CS-253 |
| TC-AC-CS-E2E-150-state-tenant-trial-expired-pada-dropdown-convert-dan-activate-trial | State Tenant: Trial Expired pada Dropdown, Convert, dan Activate Trial | FE+BE | 30 | TC-AC-CS-532, TC-AC-CS-533 |
| TC-AC-CS-E2E-151-job-flip-dilewati-dan-race-cancel-request | Job: Flip Dilewati dan Race Cancel Request | FE+BE | 34 | TC-AC-CS-290, TC-AC-CS-291, TC-AC-CS-546 |
| TC-AC-CS-E2E-152-job-timeout-auto-cancel-convert-dan-edit | Job: Timeout Auto-Cancel Term Convert dan Edit | FE+BE | 21 | TC-AC-CS-548, TC-AC-CS-633 |
| TC-AC-CS-E2E-153-changelog-pagination-dan-download | Changelog: Pagination dan Download | FE+BE | 14 | TC-AC-CS-428, TC-AC-CS-429 |
| TC-AC-CS-E2E-154-list-setup-column-reset-dan-discard | List Setup Column: Reset dan Discard | FE+BE | 14 | TC-AC-CS-371, TC-AC-CS-372 |
| TC-AC-CS-E2E-155-subscription-log-row-action-semua-status | Subscription Log: Row Action pada Semua Status | FE+BE | 15 | TC-AC-CS-590 |
| TC-AC-CS-E2E-156-subscription-log-urutan-immutability-dan-edit-no-op | Subscription Log: Urutan, Immutability, dan Edit No-Op | FE+BE | 21 | TC-AC-CS-609 |
| TC-AC-CS-E2E-160-konfigurasi-platform-live-push-update-ceiling-trial-dan-approval-timeout | Konfigurasi Platform Live: Push Update Plan, Ceiling Trial, dan Approval Timeout | FE+BE | 27 | TC-AC-CS-484, TC-AC-CS-485, TC-AC-CS-487 |
| TC-AC-CS-E2E-161-auto-archive-client-setelah-cancel-subscription-terakhir | Modul Konsumen: Auto-Archive Client setelah Cancel Subscription Terakhir | FE+BE | 20 | TC-AC-CS-480 |
| TC-AC-CS-E2E-162-multi-konteks-race-add-cancel-renew-dan-convert-ganda | Multi-konteks: Race Add, Cancel dan Renew, serta Convert Ganda | FE+BE | 39 | TC-AC-CS-516, TC-AC-CS-517, TC-AC-CS-577 |
| TC-AC-CS-E2E-163-resilience-retry-setelah-timeout-dan-toast-error-bertahan | Resilience: Retry Setelah Timeout dan Toast Error Bertahan | FE+BE | 23 | TC-AC-CS-521, TC-AC-CS-563 |

## 2. Daftar TC hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Seluruh TC granular memiliki langkah UI dan dicakup spec E2E. TC backend (`TC-AC-CS-BE-NNN`) tidak merujuk TC granular.

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-CS-1 | E2E | TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | FE+BE |
| TC-AC-CS-2 | E2E | TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | FE+BE |
| TC-AC-CS-3 | E2E | TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | FE+BE |
| TC-AC-CS-4 | E2E | TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | FE+BE |
| TC-AC-CS-5 | E2E | TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | FE+BE |
| TC-AC-CS-6 | E2E | TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | FE+BE |
| TC-AC-CS-7 | E2E | TC-AC-CS-E2E-001-list-screening-tab-current-dan-history | FE+BE |
| TC-AC-CS-8 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-9 | E2E | TC-AC-CS-E2E-008-list-baris-requester-distributor | FE+BE |
| TC-AC-CS-10 | E2E | TC-AC-CS-E2E-009-list-baris-requester-group-manager-dan-partner | FE+BE |
| TC-AC-CS-11 | E2E | TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | FE+BE |
| TC-AC-CS-12 | E2E | TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | FE+BE |
| TC-AC-CS-13 | E2E | TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | FE+BE |
| TC-AC-CS-14 | E2E | TC-AC-CS-E2E-008-list-baris-requester-distributor | FE+BE |
| TC-AC-CS-15 | E2E | TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | FE+BE |
| TC-AC-CS-16 | E2E | TC-AC-CS-E2E-004-list-baris-aktif-kedaluwarsa-dan-grace | FE+BE |
| TC-AC-CS-17 | E2E | TC-AC-CS-E2E-005-list-baris-riwayat-sel-plan-dan-sel-plan-owner | FE+BE |
| TC-AC-CS-18 | E2E | TC-AC-CS-E2E-009-list-baris-requester-group-manager-dan-partner | FE+BE |
| TC-AC-CS-19 | E2E | TC-AC-CS-E2E-146-list-baris-trial-riwayat-dan-client-archive | FE+BE |
| TC-AC-CS-20 | E2E | TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire | FE+BE |
| TC-AC-CS-21 | E2E | TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal | FE+BE |
| TC-AC-CS-22 | E2E | TC-AC-CS-E2E-146-list-baris-trial-riwayat-dan-client-archive | FE+BE |
| TC-AC-CS-23 | E2E | TC-AC-CS-E2E-073-resubmit-partner-timeout-auto-cancel | FE+BE |
| TC-AC-CS-24 | E2E | TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client | FE+BE |
| TC-AC-CS-25 | E2E | TC-AC-CS-E2E-005-list-baris-riwayat-sel-plan-dan-sel-plan-owner | FE+BE |
| TC-AC-CS-26 | E2E | TC-AC-CS-E2E-005-list-baris-riwayat-sel-plan-dan-sel-plan-owner | FE+BE |
| TC-AC-CS-27 | E2E | TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | FE+BE |
| TC-AC-CS-28 | E2E | TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | FE+BE |
| TC-AC-CS-29 | E2E | TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | FE+BE |
| TC-AC-CS-30 | E2E | TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager | FE+BE |
| TC-AC-CS-31 | E2E | TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | FE+BE |
| TC-AC-CS-32 | E2E | TC-AC-CS-E2E-006-list-tanggal-kosong-navigasi-baris-dan-masuk-dari-client-detail | FE+BE |
| TC-AC-CS-33 | E2E | TC-AC-CS-E2E-103-list-state-preservation-memori-per-tab | FE+BE |
| TC-AC-CS-34 | E2E | TC-AC-CS-E2E-103-list-state-preservation-memori-per-tab | FE+BE |
| TC-AC-CS-35 | E2E | TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon | FE+BE |
| TC-AC-CS-36 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-37 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-38 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-39 | E2E | TC-AC-CS-E2E-008-list-baris-requester-distributor | FE+BE |
| TC-AC-CS-40 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-41 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |
| TC-AC-CS-42 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |
| TC-AC-CS-43 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |
| TC-AC-CS-44 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |
| TC-AC-CS-45 | E2E | TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | FE+BE |
| TC-AC-CS-46 | E2E | TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | FE+BE |
| TC-AC-CS-47 | E2E | TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | FE+BE |
| TC-AC-CS-48 | E2E | TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | FE+BE |
| TC-AC-CS-49 | E2E | TC-AC-CS-E2E-012-detail-feature-entitlement-addon-features-dan-state-loading | FE+BE |
| TC-AC-CS-50 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-51 | E2E | TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action | FE+BE |
| TC-AC-CS-52 | E2E | TC-AC-CS-E2E-008-list-baris-requester-distributor | FE+BE |
| TC-AC-CS-53 | E2E | TC-AC-CS-E2E-009-list-baris-requester-group-manager-dan-partner | FE+BE |
| TC-AC-CS-54 | E2E | TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action | FE+BE |
| TC-AC-CS-55 | E2E | TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action | FE+BE |
| TC-AC-CS-56 | E2E | TC-AC-CS-E2E-103-list-state-preservation-memori-per-tab | FE+BE |
| TC-AC-CS-57 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-58 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-59 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |
| TC-AC-CS-60 | E2E | TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama | FE+BE |
| TC-AC-CS-61 | E2E | TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama | FE+BE |
| TC-AC-CS-62 | E2E | TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama | FE+BE |
| TC-AC-CS-63 | E2E | TC-AC-CS-E2E-014-guided-tooltip-isi-dan-kunjungan-pertama | FE+BE |
| TC-AC-CS-64 | E2E | TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | FE+BE |
| TC-AC-CS-65 | E2E | TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | FE+BE |
| TC-AC-CS-66 | E2E | TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | FE+BE |
| TC-AC-CS-67 | E2E | TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | FE+BE |
| TC-AC-CS-68 | E2E | TC-AC-CS-E2E-015-guided-tooltip-skip-resize-dan-keyboard | FE+BE |
| TC-AC-CS-69 | E2E | TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | FE+BE |
| TC-AC-CS-70 | E2E | TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | FE+BE |
| TC-AC-CS-71 | E2E | TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | FE+BE |
| TC-AC-CS-72 | E2E | TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | FE+BE |
| TC-AC-CS-73 | E2E | TC-AC-CS-E2E-016-role-matrix-akses-menu-dan-url-langsung-per-entitas | FE+BE |
| TC-AC-CS-74 | E2E | TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager | FE+BE |
| TC-AC-CS-75 | E2E | TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager | FE+BE |
| TC-AC-CS-76 | E2E | TC-AC-CS-E2E-017-role-matrix-visibilitas-elemen-role-principal-dan-group-manager | FE+BE |
| TC-AC-CS-77 | E2E | TC-AC-CS-E2E-018-role-matrix-visibilitas-elemen-hak-parsial | FE+BE |
| TC-AC-CS-78 | E2E | TC-AC-CS-E2E-018-role-matrix-visibilitas-elemen-hak-parsial | FE+BE |
| TC-AC-CS-79 | E2E | TC-AC-CS-E2E-018-role-matrix-visibilitas-elemen-hak-parsial | FE+BE |
| TC-AC-CS-80 | E2E | TC-AC-CS-E2E-019-role-matrix-visibilitas-elemen-group-role-a-dan-b | FE+BE |
| TC-AC-CS-81 | E2E | TC-AC-CS-E2E-019-role-matrix-visibilitas-elemen-group-role-a-dan-b | FE+BE |
| TC-AC-CS-82 | E2E | TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client | FE+BE |
| TC-AC-CS-83 | E2E | TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses | FE+BE |
| TC-AC-CS-84 | E2E | TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses | FE+BE |
| TC-AC-CS-85 | E2E | TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses | FE+BE |
| TC-AC-CS-86 | E2E | TC-AC-CS-E2E-021-capability-create-add-activate-trial-renew-convert-sampai-sukses | FE+BE |
| TC-AC-CS-87 | E2E | TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses | FE+BE |
| TC-AC-CS-88 | E2E | TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses | FE+BE |
| TC-AC-CS-89 | E2E | TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses | FE+BE |
| TC-AC-CS-90 | E2E | TC-AC-CS-E2E-022-capability-edit-cancel-request-resubmit-cancel-subscription-sampai-sukses | FE+BE |
| TC-AC-CS-91 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-92 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-93 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-94 | E2E | TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match | FE+BE |
| TC-AC-CS-95 | E2E | TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match | FE+BE |
| TC-AC-CS-96 | E2E | TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match | FE+BE |
| TC-AC-CS-97 | E2E | TC-AC-CS-E2E-024-scope-tulis-dropdown-client-dan-plan-owner-exact-match | FE+BE |
| TC-AC-CS-98 | E2E | TC-AC-CS-E2E-025-scope-tulis-group-manager-descendant-dan-opsi-new-client | FE+BE |
| TC-AC-CS-99 | E2E | TC-AC-CS-E2E-025-scope-tulis-group-manager-descendant-dan-opsi-new-client | FE+BE |
| TC-AC-CS-100 | E2E | TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client | FE+BE |
| TC-AC-CS-101 | E2E | TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | FE+BE |
| TC-AC-CS-102 | E2E | TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | FE+BE |
| TC-AC-CS-103 | E2E | TC-AC-CS-E2E-027-form-renew-dan-convert-screening | FE+BE |
| TC-AC-CS-104 | E2E | TC-AC-CS-E2E-027-form-renew-dan-convert-screening | FE+BE |
| TC-AC-CS-105 | E2E | TC-AC-CS-E2E-027-form-renew-dan-convert-screening | FE+BE |
| TC-AC-CS-106 | E2E | TC-AC-CS-E2E-027-form-renew-dan-convert-screening | FE+BE |
| TC-AC-CS-107 | E2E | TC-AC-CS-E2E-028-form-add-opsi-dropdown-client-dan-product | FE+BE |
| TC-AC-CS-108 | E2E | TC-AC-CS-E2E-028-form-add-opsi-dropdown-client-dan-product | FE+BE |
| TC-AC-CS-109 | E2E | TC-AC-CS-E2E-029-form-add-opsi-plan-dan-pay-from-distributor-dan-partner | FE+BE |
| TC-AC-CS-110 | E2E | TC-AC-CS-E2E-029-form-add-opsi-plan-dan-pay-from-distributor-dan-partner | FE+BE |
| TC-AC-CS-111 | E2E | TC-AC-CS-E2E-028-form-add-opsi-dropdown-client-dan-product | FE+BE |
| TC-AC-CS-112 | E2E | TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | FE+BE |
| TC-AC-CS-113 | E2E | TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | FE+BE |
| TC-AC-CS-114 | E2E | TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | FE+BE |
| TC-AC-CS-115 | E2E | TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | FE+BE |
| TC-AC-CS-116 | E2E | TC-AC-CS-E2E-030-form-add-validasi-client-product-plan | FE+BE |
| TC-AC-CS-117 | E2E | TC-AC-CS-E2E-031-form-add-validasi-duration | FE+BE |
| TC-AC-CS-118 | E2E | TC-AC-CS-E2E-031-form-add-validasi-duration | FE+BE |
| TC-AC-CS-119 | E2E | TC-AC-CS-E2E-031-form-add-validasi-duration | FE+BE |
| TC-AC-CS-120 | E2E | TC-AC-CS-E2E-031-form-add-validasi-duration | FE+BE |
| TC-AC-CS-121 | E2E | TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from | FE+BE |
| TC-AC-CS-122 | E2E | TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from | FE+BE |
| TC-AC-CS-123 | E2E | TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from | FE+BE |
| TC-AC-CS-124 | E2E | TC-AC-CS-E2E-032-form-add-validasi-start-date-dan-pay-from | FE+BE |
| TC-AC-CS-125 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-126 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-127 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-128 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-129 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-130 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-131 | E2E | TC-AC-CS-E2E-027-form-renew-dan-convert-screening | FE+BE |
| TC-AC-CS-132 | E2E | TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | FE+BE |
| TC-AC-CS-133 | E2E | TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | FE+BE |
| TC-AC-CS-134 | E2E | TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | FE+BE |
| TC-AC-CS-135 | E2E | TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | FE+BE |
| TC-AC-CS-136 | E2E | TC-AC-CS-E2E-034-payment-preview-estimated-cost-dan-saldo-kantong | FE+BE |
| TC-AC-CS-137 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-138 | E2E | TC-AC-CS-E2E-033-form-renew-validasi-dan-preview-renewal | FE+BE |
| TC-AC-CS-139 | E2E | TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | FE+BE |
| TC-AC-CS-140 | E2E | TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager | FE+BE |
| TC-AC-CS-141 | E2E | TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager | FE+BE |
| TC-AC-CS-142 | E2E | TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | FE+BE |
| TC-AC-CS-143 | E2E | TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager | FE+BE |
| TC-AC-CS-144 | E2E | TC-AC-CS-E2E-035-add-alert-info-dan-bypass-group-manager | FE+BE |
| TC-AC-CS-145 | E2E | TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email | FE+BE |
| TC-AC-CS-146 | E2E | TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | FE+BE |
| TC-AC-CS-147 | E2E | TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | FE+BE |
| TC-AC-CS-148 | E2E | TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan | FE+BE |
| TC-AC-CS-149 | E2E | TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan | FE+BE |
| TC-AC-CS-150 | E2E | TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan | FE+BE |
| TC-AC-CS-151 | E2E | TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | FE+BE |
| TC-AC-CS-152 | E2E | TC-AC-CS-E2E-040-renew-efek-langsung-terjadwal-dan-change-plan | FE+BE |
| TC-AC-CS-153 | E2E | TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new | FE+BE |
| TC-AC-CS-154 | E2E | TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email | FE+BE |
| TC-AC-CS-155 | E2E | TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new | FE+BE |
| TC-AC-CS-156 | E2E | TC-AC-CS-E2E-148-activation-email-dan-app-access-pada-term-pertama | FE+BE |
| TC-AC-CS-157 | E2E | TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | FE+BE |
| TC-AC-CS-158 | E2E | TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | FE+BE |
| TC-AC-CS-159 | E2E | TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | FE+BE |
| TC-AC-CS-160 | E2E | TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email | FE+BE |
| TC-AC-CS-161 | E2E | TC-AC-CS-E2E-037-add-principal-stay-on-this-form-dan-activation-email | FE+BE |
| TC-AC-CS-162 | E2E | TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-CS-163 | E2E | TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | FE+BE |
| TC-AC-CS-164 | E2E | TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-CS-165 | E2E | TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-CS-166 | E2E | TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-CS-167 | E2E | TC-AC-CS-E2E-041-renew-blokir-clear-field-dan-nilai-clean | FE+BE |
| TC-AC-CS-168 | E2E | TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer | FE+BE |
| TC-AC-CS-169 | E2E | TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer | FE+BE |
| TC-AC-CS-170 | E2E | TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer | FE+BE |
| TC-AC-CS-171 | E2E | TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial | FE+BE |
| TC-AC-CS-172 | E2E | TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel | FE+BE |
| TC-AC-CS-173 | E2E | TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel | FE+BE |
| TC-AC-CS-174 | E2E | TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new | FE+BE |
| TC-AC-CS-175 | E2E | TC-AC-CS-E2E-039-add-distributor-biaya-nol-renewal-rank-lebih-rendah-dan-new | FE+BE |
| TC-AC-CS-176 | E2E | TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | FE+BE |
| TC-AC-CS-177 | E2E | TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | FE+BE |
| TC-AC-CS-178 | E2E | TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas | FE+BE |
| TC-AC-CS-179 | E2E | TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas | FE+BE |
| TC-AC-CS-180 | E2E | TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | FE+BE |
| TC-AC-CS-181 | E2E | TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | FE+BE |
| TC-AC-CS-182 | E2E | TC-AC-CS-E2E-046-activate-trial-screening-dan-nilai-awal | FE+BE |
| TC-AC-CS-183 | E2E | TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan | FE+BE |
| TC-AC-CS-184 | E2E | TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan | FE+BE |
| TC-AC-CS-185 | E2E | TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan | FE+BE |
| TC-AC-CS-186 | E2E | TC-AC-CS-E2E-048-activate-trial-validasi-client-product-plan | FE+BE |
| TC-AC-CS-187 | E2E | TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | FE+BE |
| TC-AC-CS-188 | E2E | TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | FE+BE |
| TC-AC-CS-189 | E2E | TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah | FE+BE |
| TC-AC-CS-190 | E2E | TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah | FE+BE |
| TC-AC-CS-191 | E2E | TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah | FE+BE |
| TC-AC-CS-192 | E2E | TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | FE+BE |
| TC-AC-CS-193 | E2E | TC-AC-CS-E2E-050-activate-trial-kuota-kosong-dan-batas-bawah | FE+BE |
| TC-AC-CS-194 | E2E | TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas | FE+BE |
| TC-AC-CS-195 | E2E | TC-AC-CS-E2E-047-activate-trial-opsi-plan-dan-eligibilitas | FE+BE |
| TC-AC-CS-196 | E2E | TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | FE+BE |
| TC-AC-CS-197 | E2E | TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | FE+BE |
| TC-AC-CS-198 | E2E | TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | FE+BE |
| TC-AC-CS-199 | E2E | TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | FE+BE |
| TC-AC-CS-200 | E2E | TC-AC-CS-E2E-052-activate-trial-toggle-approval-distributor-dan-partner | FE+BE |
| TC-AC-CS-201 | E2E | TC-AC-CS-E2E-052-activate-trial-toggle-approval-distributor-dan-partner | FE+BE |
| TC-AC-CS-202 | E2E | TC-AC-CS-E2E-052-activate-trial-toggle-approval-distributor-dan-partner | FE+BE |
| TC-AC-CS-203 | E2E | TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | FE+BE |
| TC-AC-CS-204 | E2E | TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | FE+BE |
| TC-AC-CS-205 | E2E | TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | FE+BE |
| TC-AC-CS-206 | E2E | TC-AC-CS-E2E-051-activate-trial-principal-dan-inisialisasi-kuota | FE+BE |
| TC-AC-CS-207 | E2E | TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | FE+BE |
| TC-AC-CS-208 | E2E | TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | FE+BE |
| TC-AC-CS-209 | E2E | TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel | FE+BE |
| TC-AC-CS-210 | E2E | TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | FE+BE |
| TC-AC-CS-211 | E2E | TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | FE+BE |
| TC-AC-CS-212 | E2E | TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | FE+BE |
| TC-AC-CS-213 | E2E | TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | FE+BE |
| TC-AC-CS-214 | E2E | TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | FE+BE |
| TC-AC-CS-215 | E2E | TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | FE+BE |
| TC-AC-CS-216 | E2E | TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | FE+BE |
| TC-AC-CS-217 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-218 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-219 | E2E | TC-AC-CS-E2E-061-edit-group-manager-bypass | FE+BE |
| TC-AC-CS-220 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-221 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-222 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-223 | E2E | TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo | FE+BE |
| TC-AC-CS-224 | E2E | TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo | FE+BE |
| TC-AC-CS-225 | E2E | TC-AC-CS-E2E-061-edit-group-manager-bypass | FE+BE |
| TC-AC-CS-226 | E2E | TC-AC-CS-E2E-061-edit-group-manager-bypass | FE+BE |
| TC-AC-CS-227 | E2E | TC-AC-CS-E2E-061-edit-group-manager-bypass | FE+BE |
| TC-AC-CS-228 | E2E | TC-AC-CS-E2E-061-edit-group-manager-bypass | FE+BE |
| TC-AC-CS-229 | E2E | TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo | FE+BE |
| TC-AC-CS-230 | E2E | TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo | FE+BE |
| TC-AC-CS-231 | E2E | TC-AC-CS-E2E-118-log-absence-tanpa-perubahan-dan-lintas-record | FE+BE |
| TC-AC-CS-232 | E2E | TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi | FE+BE |
| TC-AC-CS-233 | E2E | TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi | FE+BE |
| TC-AC-CS-234 | E2E | TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi | FE+BE |
| TC-AC-CS-235 | E2E | TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request | FE+BE |
| TC-AC-CS-236 | E2E | TC-AC-CS-E2E-057-edit-screening-dan-field-terkunci | FE+BE |
| TC-AC-CS-237 | E2E | TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes | FE+BE |
| TC-AC-CS-238 | E2E | TC-AC-CS-E2E-143-klik-ganda-cancel-request-dan-save-edit-state-submitting-save | FE+BE |
| TC-AC-CS-239 | E2E | TC-AC-CS-E2E-063-convert-trial-row-action-dan-dialog-instan-atau-request | FE+BE |
| TC-AC-CS-240 | E2E | TC-AC-CS-E2E-063-convert-trial-row-action-dan-dialog-instan-atau-request | FE+BE |
| TC-AC-CS-241 | E2E | TC-AC-CS-E2E-063-convert-trial-row-action-dan-dialog-instan-atau-request | FE+BE |
| TC-AC-CS-242 | E2E | TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa | FE+BE |
| TC-AC-CS-243 | E2E | TC-AC-CS-E2E-064-convert-trial-group-manager-jalur-instan | FE+BE |
| TC-AC-CS-244 | E2E | TC-AC-CS-E2E-065-convert-trial-requester-jalur-request | FE+BE |
| TC-AC-CS-245 | E2E | TC-AC-CS-E2E-064-convert-trial-group-manager-jalur-instan | FE+BE |
| TC-AC-CS-246 | E2E | TC-AC-CS-E2E-065-convert-trial-requester-jalur-request | FE+BE |
| TC-AC-CS-247 | E2E | TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa | FE+BE |
| TC-AC-CS-248 | E2E | TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa | FE+BE |
| TC-AC-CS-249 | E2E | TC-AC-CS-E2E-067-convert-trial-data-asset-dan-rantai-trial | FE+BE |
| TC-AC-CS-250 | E2E | TC-AC-CS-E2E-067-convert-trial-data-asset-dan-rantai-trial | FE+BE |
| TC-AC-CS-251 | E2E | TC-AC-CS-E2E-067-convert-trial-data-asset-dan-rantai-trial | FE+BE |
| TC-AC-CS-252 | E2E | TC-AC-CS-E2E-149-convert-trial-plan-free-dan-predecessor-bersuccessor | FE+BE |
| TC-AC-CS-253 | E2E | TC-AC-CS-E2E-149-convert-trial-plan-free-dan-predecessor-bersuccessor | FE+BE |
| TC-AC-CS-254 | E2E | TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire | FE+BE |
| TC-AC-CS-255 | E2E | TC-AC-CS-E2E-064-convert-trial-group-manager-jalur-instan | FE+BE |
| TC-AC-CS-256 | E2E | TC-AC-CS-E2E-065-convert-trial-requester-jalur-request | FE+BE |
| TC-AC-CS-257 | E2E | TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request | FE+BE |
| TC-AC-CS-258 | E2E | TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request | FE+BE |
| TC-AC-CS-259 | E2E | TC-AC-CS-E2E-068-cancel-subscription-dialog | FE+BE |
| TC-AC-CS-260 | E2E | TC-AC-CS-E2E-068-cancel-subscription-dialog | FE+BE |
| TC-AC-CS-261 | E2E | TC-AC-CS-E2E-068-cancel-subscription-dialog | FE+BE |
| TC-AC-CS-262 | E2E | TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi | FE+BE |
| TC-AC-CS-263 | E2E | TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi | FE+BE |
| TC-AC-CS-264 | E2E | TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi | FE+BE |
| TC-AC-CS-265 | E2E | TC-AC-CS-E2E-069-cancel-subscription-efek-dan-alokasi | FE+BE |
| TC-AC-CS-266 | E2E | TC-AC-CS-E2E-140-resilience-gagal-tulis-add-renew-activate-trial-cancel | FE+BE |
| TC-AC-CS-267 | E2E | TC-AC-CS-E2E-142-klik-ganda-cancel-subscription-dan-convert | FE+BE |
| TC-AC-CS-268 | E2E | TC-AC-CS-E2E-055-state-tenant-cancel-job-dan-suspend-trial-pada-client | FE+BE |
| TC-AC-CS-269 | E2E | TC-AC-CS-E2E-068-cancel-subscription-dialog | FE+BE |
| TC-AC-CS-270 | E2E | TC-AC-CS-E2E-070-cancel-request-requester | FE+BE |
| TC-AC-CS-271 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-272 | E2E | TC-AC-CS-E2E-070-cancel-request-requester | FE+BE |
| TC-AC-CS-273 | E2E | TC-AC-CS-E2E-070-cancel-request-requester | FE+BE |
| TC-AC-CS-274 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-275 | E2E | TC-AC-CS-E2E-070-cancel-request-requester | FE+BE |
| TC-AC-CS-276 | E2E | TC-AC-CS-E2E-071-cancel-request-perubahan-status-dan-pending-diedit | FE+BE |
| TC-AC-CS-277 | E2E | TC-AC-CS-E2E-141-resilience-gagal-tulis-edit-convert-cancel-request | FE+BE |
| TC-AC-CS-278 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-279 | E2E | TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada | FE+BE |
| TC-AC-CS-280 | E2E | TC-AC-CS-E2E-073-resubmit-partner-timeout-auto-cancel | FE+BE |
| TC-AC-CS-281 | E2E | TC-AC-CS-E2E-075-resubmit-distributor-dan-principal | FE+BE |
| TC-AC-CS-282 | E2E | TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | FE+BE |
| TC-AC-CS-283 | E2E | TC-AC-CS-E2E-075-resubmit-distributor-dan-principal | FE+BE |
| TC-AC-CS-284 | E2E | TC-AC-CS-E2E-075-resubmit-distributor-dan-principal | FE+BE |
| TC-AC-CS-285 | E2E | TC-AC-CS-E2E-073-resubmit-partner-timeout-auto-cancel | FE+BE |
| TC-AC-CS-286 | E2E | TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | FE+BE |
| TC-AC-CS-287 | E2E | TC-AC-CS-E2E-076-job-scheduled-flip | FE+BE |
| TC-AC-CS-288 | E2E | TC-AC-CS-E2E-076-job-scheduled-flip | FE+BE |
| TC-AC-CS-289 | E2E | TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire | FE+BE |
| TC-AC-CS-290 | E2E | TC-AC-CS-E2E-151-job-flip-dilewati-dan-race-cancel-request | FE+BE |
| TC-AC-CS-291 | E2E | TC-AC-CS-E2E-151-job-flip-dilewati-dan-race-cancel-request | FE+BE |
| TC-AC-CS-292 | E2E | TC-AC-CS-E2E-078-job-pre-timeout-warning-dan-timeout-auto-cancel | FE+BE |
| TC-AC-CS-293 | E2E | TC-AC-CS-E2E-079-job-timeout-auto-cancel-lanjutan | FE+BE |
| TC-AC-CS-294 | E2E | TC-AC-CS-E2E-078-job-pre-timeout-warning-dan-timeout-auto-cancel | FE+BE |
| TC-AC-CS-295 | E2E | TC-AC-CS-E2E-079-job-timeout-auto-cancel-lanjutan | FE+BE |
| TC-AC-CS-296 | E2E | TC-AC-CS-E2E-079-job-timeout-auto-cancel-lanjutan | FE+BE |
| TC-AC-CS-297 | E2E | TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new | FE+BE |
| TC-AC-CS-298 | E2E | TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new | FE+BE |
| TC-AC-CS-299 | E2E | TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new | FE+BE |
| TC-AC-CS-300 | E2E | TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | FE+BE |
| TC-AC-CS-301 | E2E | TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal | FE+BE |
| TC-AC-CS-302 | E2E | TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal | FE+BE |
| TC-AC-CS-303 | E2E | TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal | FE+BE |
| TC-AC-CS-304 | E2E | TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal | FE+BE |
| TC-AC-CS-305 | E2E | TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada | FE+BE |
| TC-AC-CS-306 | E2E | TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | FE+BE |
| TC-AC-CS-307 | E2E | TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | FE+BE |
| TC-AC-CS-308 | E2E | TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | FE+BE |
| TC-AC-CS-309 | E2E | TC-AC-CS-E2E-082-approvals-approve-dan-reject-convert | FE+BE |
| TC-AC-CS-310 | E2E | TC-AC-CS-E2E-080-approvals-approve-dan-reject-mode-new | FE+BE |
| TC-AC-CS-311 | E2E | TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas | FE+BE |
| TC-AC-CS-312 | E2E | TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas | FE+BE |
| TC-AC-CS-313 | E2E | TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas | FE+BE |
| TC-AC-CS-314 | E2E | TC-AC-CS-E2E-084-list-search-reveal-enter-dan-kolom-identitas | FE+BE |
| TC-AC-CS-315 | E2E | TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | FE+BE |
| TC-AC-CS-316 | E2E | TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | FE+BE |
| TC-AC-CS-317 | E2E | TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | FE+BE |
| TC-AC-CS-318 | E2E | TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | FE+BE |
| TC-AC-CS-319 | E2E | TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | FE+BE |
| TC-AC-CS-320 | E2E | TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | FE+BE |
| TC-AC-CS-321 | E2E | TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | FE+BE |
| TC-AC-CS-322 | E2E | TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | FE+BE |
| TC-AC-CS-323 | E2E | TC-AC-CS-E2E-086-list-search-visibilitas-kolom-tab-dan-karakter-khusus | FE+BE |
| TC-AC-CS-324 | E2E | TC-AC-CS-E2E-085-list-search-kolom-plan-product-status-dan-tanggal | FE+BE |
| TC-AC-CS-325 | E2E | TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | FE+BE |
| TC-AC-CS-326 | E2E | TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | FE+BE |
| TC-AC-CS-327 | E2E | TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | FE+BE |
| TC-AC-CS-328 | E2E | TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | FE+BE |
| TC-AC-CS-329 | E2E | TC-AC-CS-E2E-087-list-filter-screening-dan-opsi-dropdown | FE+BE |
| TC-AC-CS-330 | E2E | TC-AC-CS-E2E-019-role-matrix-visibilitas-elemen-group-role-a-dan-b | FE+BE |
| TC-AC-CS-331 | E2E | TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | FE+BE |
| TC-AC-CS-332 | E2E | TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | FE+BE |
| TC-AC-CS-333 | E2E | TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | FE+BE |
| TC-AC-CS-334 | E2E | TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | FE+BE |
| TC-AC-CS-335 | E2E | TC-AC-CS-E2E-088-list-filter-opsi-status-dan-perilaku-per-kelas | FE+BE |
| TC-AC-CS-336 | E2E | TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and | FE+BE |
| TC-AC-CS-337 | E2E | TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and | FE+BE |
| TC-AC-CS-338 | E2E | TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and | FE+BE |
| TC-AC-CS-339 | E2E | TC-AC-CS-E2E-089-list-filter-date-range-grace-end-or-dan-and | FE+BE |
| TC-AC-CS-340 | E2E | TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip | FE+BE |
| TC-AC-CS-341 | E2E | TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip | FE+BE |
| TC-AC-CS-342 | E2E | TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip | FE+BE |
| TC-AC-CS-343 | E2E | TC-AC-CS-E2E-090-list-filter-pencarian-dalam-dropdown-dan-chip | FE+BE |
| TC-AC-CS-344 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-345 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-346 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-347 | E2E | TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | FE+BE |
| TC-AC-CS-348 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-349 | E2E | TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | FE+BE |
| TC-AC-CS-350 | E2E | TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | FE+BE |
| TC-AC-CS-351 | E2E | TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | FE+BE |
| TC-AC-CS-352 | E2E | TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | FE+BE |
| TC-AC-CS-353 | E2E | TC-AC-CS-E2E-092-list-sort-default-dan-siklus-kolom | FE+BE |
| TC-AC-CS-354 | E2E | TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker | FE+BE |
| TC-AC-CS-355 | E2E | TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker | FE+BE |
| TC-AC-CS-356 | E2E | TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker | FE+BE |
| TC-AC-CS-357 | E2E | TC-AC-CS-E2E-093-list-sort-tanggal-nilai-kosong-dan-tie-breaker | FE+BE |
| TC-AC-CS-358 | E2E | TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-CS-359 | E2E | TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-CS-360 | E2E | TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-CS-361 | E2E | TC-AC-CS-E2E-095-list-clear-filter-dan-clear-search-saat-kombinasi-aktif | FE+BE |
| TC-AC-CS-362 | E2E | TC-AC-CS-E2E-095-list-clear-filter-dan-clear-search-saat-kombinasi-aktif | FE+BE |
| TC-AC-CS-363 | E2E | TC-AC-CS-E2E-095-list-clear-filter-dan-clear-search-saat-kombinasi-aktif | FE+BE |
| TC-AC-CS-364 | E2E | TC-AC-CS-E2E-094-list-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-CS-365 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-366 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-367 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-368 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-369 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-370 | E2E | TC-AC-CS-E2E-096-list-setup-column-screening-hide-curated-urutan-pin | FE+BE |
| TC-AC-CS-371 | E2E | TC-AC-CS-E2E-154-list-setup-column-reset-dan-discard | FE+BE |
| TC-AC-CS-372 | E2E | TC-AC-CS-E2E-154-list-setup-column-reset-dan-discard | FE+BE |
| TC-AC-CS-373 | E2E | TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama | FE+BE |
| TC-AC-CS-374 | E2E | TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama | FE+BE |
| TC-AC-CS-375 | E2E | TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama | FE+BE |
| TC-AC-CS-376 | E2E | TC-AC-CS-E2E-097-list-setup-column-overlay-guard-cache-bersama | FE+BE |
| TC-AC-CS-377 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-378 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-379 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-380 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-381 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-382 | E2E | TC-AC-CS-E2E-099-list-pagination | FE+BE |
| TC-AC-CS-383 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-384 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-385 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-386 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-387 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-388 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-389 | E2E | TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx | FE+BE |
| TC-AC-CS-390 | E2E | TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx | FE+BE |
| TC-AC-CS-391 | E2E | TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx | FE+BE |
| TC-AC-CS-392 | E2E | TC-AC-CS-E2E-100-list-download-cakupan-filter-kolom-dan-volume-5-001-baris | FE+BE |
| TC-AC-CS-393 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-394 | E2E | TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar | FE+BE |
| TC-AC-CS-395 | E2E | TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar | FE+BE |
| TC-AC-CS-396 | E2E | TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar | FE+BE |
| TC-AC-CS-397 | E2E | TC-AC-CS-E2E-102-list-state-preservation-detail-f5-dan-sidebar | FE+BE |
| TC-AC-CS-398 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-399 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-400 | E2E | TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | FE+BE |
| TC-AC-CS-401 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-402 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-403 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-404 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-405 | E2E | TC-AC-CS-E2E-104-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-CS-406 | E2E | TC-AC-CS-E2E-105-changelog-search | FE+BE |
| TC-AC-CS-407 | E2E | TC-AC-CS-E2E-105-changelog-search | FE+BE |
| TC-AC-CS-408 | E2E | TC-AC-CS-E2E-105-changelog-search | FE+BE |
| TC-AC-CS-409 | E2E | TC-AC-CS-E2E-105-changelog-search | FE+BE |
| TC-AC-CS-410 | E2E | TC-AC-CS-E2E-106-changelog-filter-panel-1 | FE+BE |
| TC-AC-CS-411 | E2E | TC-AC-CS-E2E-106-changelog-filter-panel-1 | FE+BE |
| TC-AC-CS-412 | E2E | TC-AC-CS-E2E-106-changelog-filter-panel-1 | FE+BE |
| TC-AC-CS-413 | E2E | TC-AC-CS-E2E-106-changelog-filter-panel-1 | FE+BE |
| TC-AC-CS-414 | E2E | TC-AC-CS-E2E-106-changelog-filter-panel-1 | FE+BE |
| TC-AC-CS-415 | E2E | TC-AC-CS-E2E-107-changelog-filter-panel-2 | FE+BE |
| TC-AC-CS-416 | E2E | TC-AC-CS-E2E-107-changelog-filter-panel-2 | FE+BE |
| TC-AC-CS-417 | E2E | TC-AC-CS-E2E-107-changelog-filter-panel-2 | FE+BE |
| TC-AC-CS-418 | E2E | TC-AC-CS-E2E-107-changelog-filter-panel-2 | FE+BE |
| TC-AC-CS-419 | E2E | TC-AC-CS-E2E-108-changelog-sort | FE+BE |
| TC-AC-CS-420 | E2E | TC-AC-CS-E2E-108-changelog-sort | FE+BE |
| TC-AC-CS-421 | E2E | TC-AC-CS-E2E-108-changelog-sort | FE+BE |
| TC-AC-CS-422 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-423 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-424 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-425 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-426 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-427 | E2E | TC-AC-CS-E2E-109-changelog-setup-column | FE+BE |
| TC-AC-CS-428 | E2E | TC-AC-CS-E2E-153-changelog-pagination-dan-download | FE+BE |
| TC-AC-CS-429 | E2E | TC-AC-CS-E2E-153-changelog-pagination-dan-download | FE+BE |
| TC-AC-CS-430 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-431 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-432 | E2E | TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit | FE+BE |
| TC-AC-CS-433 | E2E | TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit | FE+BE |
| TC-AC-CS-434 | E2E | TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit | FE+BE |
| TC-AC-CS-435 | E2E | TC-AC-CS-E2E-112-log-aksi-renew | FE+BE |
| TC-AC-CS-436 | E2E | TC-AC-CS-E2E-112-log-aksi-renew | FE+BE |
| TC-AC-CS-437 | E2E | TC-AC-CS-E2E-112-log-aksi-renew | FE+BE |
| TC-AC-CS-438 | E2E | TC-AC-CS-E2E-113-log-aksi-job-sistem | FE+BE |
| TC-AC-CS-439 | E2E | TC-AC-CS-E2E-113-log-aksi-job-sistem | FE+BE |
| TC-AC-CS-440 | E2E | TC-AC-CS-E2E-111-log-aksi-add-activate-trial-convert-dan-activate-akibat-edit | FE+BE |
| TC-AC-CS-441 | E2E | TC-AC-CS-E2E-113-log-aksi-job-sistem | FE+BE |
| TC-AC-CS-442 | E2E | TC-AC-CS-E2E-119-log-absence-approve-dan-reject | FE+BE |
| TC-AC-CS-443 | E2E | TC-AC-CS-E2E-119-log-absence-approve-dan-reject | FE+BE |
| TC-AC-CS-444 | E2E | TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date | FE+BE |
| TC-AC-CS-445 | E2E | TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date | FE+BE |
| TC-AC-CS-446 | E2E | TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date | FE+BE |
| TC-AC-CS-447 | E2E | TC-AC-CS-E2E-114-log-aksi-edit-duration-pending-dan-start-date | FE+BE |
| TC-AC-CS-448 | E2E | TC-AC-CS-E2E-115-log-aksi-edit-trial | FE+BE |
| TC-AC-CS-449 | E2E | TC-AC-CS-E2E-115-log-aksi-edit-trial | FE+BE |
| TC-AC-CS-450 | E2E | TC-AC-CS-E2E-115-log-aksi-edit-trial | FE+BE |
| TC-AC-CS-451 | E2E | TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request | FE+BE |
| TC-AC-CS-452 | E2E | TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request | FE+BE |
| TC-AC-CS-453 | E2E | TC-AC-CS-E2E-113-log-aksi-job-sistem | FE+BE |
| TC-AC-CS-454 | E2E | TC-AC-CS-E2E-117-log-aksi-resubmit | FE+BE |
| TC-AC-CS-455 | E2E | TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request | FE+BE |
| TC-AC-CS-456 | E2E | TC-AC-CS-E2E-113-log-aksi-job-sistem | FE+BE |
| TC-AC-CS-457 | E2E | TC-AC-CS-E2E-117-log-aksi-resubmit | FE+BE |
| TC-AC-CS-458 | E2E | TC-AC-CS-E2E-118-log-absence-tanpa-perubahan-dan-lintas-record | FE+BE |
| TC-AC-CS-459 | E2E | TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | FE+BE |
| TC-AC-CS-460 | E2E | TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | FE+BE |
| TC-AC-CS-461 | E2E | TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | FE+BE |
| TC-AC-CS-462 | E2E | TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | FE+BE |
| TC-AC-CS-463 | E2E | TC-AC-CS-E2E-120-integritas-log-entri-per-field-dan-per-term | FE+BE |
| TC-AC-CS-464 | E2E | TC-AC-CS-E2E-118-log-absence-tanpa-perubahan-dan-lintas-record | FE+BE |
| TC-AC-CS-465 | E2E | TC-AC-CS-E2E-023-scope-baca-per-entitas-dan-plan-owner | FE+BE |
| TC-AC-CS-466 | E2E | TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete | FE+BE |
| TC-AC-CS-467 | E2E | TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete | FE+BE |
| TC-AC-CS-468 | E2E | TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete | FE+BE |
| TC-AC-CS-469 | E2E | TC-AC-CS-E2E-121-integritas-log-entri-lama-format-dan-tanpa-delete | FE+BE |
| TC-AC-CS-470 | E2E | TC-AC-CS-E2E-128-format-tanggal-general-settings-dan-zona-waktu-plan-owner | FE+BE |
| TC-AC-CS-471 | E2E | TC-AC-CS-E2E-128-format-tanggal-general-settings-dan-zona-waktu-plan-owner | FE+BE |
| TC-AC-CS-472 | E2E | TC-AC-CS-E2E-101-list-download-isi-berkas-csv-dan-xlsx | FE+BE |
| TC-AC-CS-473 | E2E | TC-AC-CS-E2E-128-format-tanggal-general-settings-dan-zona-waktu-plan-owner | FE+BE |
| TC-AC-CS-474 | E2E | TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation | FE+BE |
| TC-AC-CS-475 | E2E | TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation | FE+BE |
| TC-AC-CS-476 | E2E | TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation | FE+BE |
| TC-AC-CS-477 | E2E | TC-AC-CS-E2E-130-wallet-dan-pengajuan-di-approvals | FE+BE |
| TC-AC-CS-478 | E2E | TC-AC-CS-E2E-130-wallet-dan-pengajuan-di-approvals | FE+BE |
| TC-AC-CS-479 | E2E | TC-AC-CS-E2E-129-modul-konsumen-client-detail-dashboard-dan-license-allocation | FE+BE |
| TC-AC-CS-480 | E2E | TC-AC-CS-E2E-161-auto-archive-client-setelah-cancel-subscription-terakhir | FE+BE |
| TC-AC-CS-481 | E2E | TC-AC-CS-E2E-077-job-flip-lanjutan-dan-race-auto-expire | FE+BE |
| TC-AC-CS-482 | E2E | TC-AC-CS-E2E-130-wallet-dan-pengajuan-di-approvals | FE+BE |
| TC-AC-CS-483 | E2E | TC-AC-CS-E2E-137-multi-konteks-dua-admin-sesi-bersamaan-principal | FE+BE |
| TC-AC-CS-484 | E2E | TC-AC-CS-E2E-160-konfigurasi-platform-live-push-update-ceiling-trial-dan-approval-timeout | FE+BE |
| TC-AC-CS-485 | E2E | TC-AC-CS-E2E-160-konfigurasi-platform-live-push-update-ceiling-trial-dan-approval-timeout | FE+BE |
| TC-AC-CS-486 | E2E | TC-AC-CS-E2E-038-add-dan-renew-requester-dengan-toggle-approval | FE+BE |
| TC-AC-CS-487 | E2E | TC-AC-CS-E2E-160-konfigurasi-platform-live-push-update-ceiling-trial-dan-approval-timeout | FE+BE |
| TC-AC-CS-488 | E2E | TC-AC-CS-E2E-131-notifikasi-in-app-approver | FE+BE |
| TC-AC-CS-489 | E2E | TC-AC-CS-E2E-131-notifikasi-in-app-approver | FE+BE |
| TC-AC-CS-490 | E2E | TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role | FE+BE |
| TC-AC-CS-491 | E2E | TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role | FE+BE |
| TC-AC-CS-492 | E2E | TC-AC-CS-E2E-131-notifikasi-in-app-approver | FE+BE |
| TC-AC-CS-493 | E2E | TC-AC-CS-E2E-131-notifikasi-in-app-approver | FE+BE |
| TC-AC-CS-494 | E2E | TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role | FE+BE |
| TC-AC-CS-495 | E2E | TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | FE+BE |
| TC-AC-CS-496 | E2E | TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | FE+BE |
| TC-AC-CS-497 | E2E | TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | FE+BE |
| TC-AC-CS-498 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-499 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-500 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-501 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-502 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-503 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-504 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-505 | E2E | TC-AC-CS-E2E-133-defense-in-depth-request-langsung-aksi-trial-add-renew-convert | FE+BE |
| TC-AC-CS-506 | E2E | TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | FE+BE |
| TC-AC-CS-507 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-508 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-509 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-510 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-511 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-512 | E2E | TC-AC-CS-E2E-136-defense-in-depth-requester-dan-scope-distributor | FE+BE |
| TC-AC-CS-513 | E2E | TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | FE+BE |
| TC-AC-CS-514 | E2E | TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | FE+BE |
| TC-AC-CS-515 | E2E | TC-AC-CS-E2E-137-multi-konteks-dua-admin-sesi-bersamaan-principal | FE+BE |
| TC-AC-CS-516 | E2E | TC-AC-CS-E2E-162-multi-konteks-race-add-cancel-renew-dan-convert-ganda | FE+BE |
| TC-AC-CS-517 | E2E | TC-AC-CS-E2E-162-multi-konteks-race-add-cancel-renew-dan-convert-ganda | FE+BE |
| TC-AC-CS-518 | E2E | TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan | FE+BE |
| TC-AC-CS-519 | E2E | TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan | FE+BE |
| TC-AC-CS-520 | E2E | TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan | FE+BE |
| TC-AC-CS-521 | E2E | TC-AC-CS-E2E-163-resilience-retry-setelah-timeout-dan-toast-error-bertahan | FE+BE |
| TC-AC-CS-522 | E2E | TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial | FE+BE |
| TC-AC-CS-523 | E2E | TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial | FE+BE |
| TC-AC-CS-524 | E2E | TC-AC-CS-E2E-142-klik-ganda-cancel-subscription-dan-convert | FE+BE |
| TC-AC-CS-525 | E2E | TC-AC-CS-E2E-143-klik-ganda-cancel-request-dan-save-edit-state-submitting-save | FE+BE |
| TC-AC-CS-526 | E2E | TC-AC-CS-E2E-143-klik-ganda-cancel-request-dan-save-edit-state-submitting-save | FE+BE |
| TC-AC-CS-527 | E2E | TC-AC-CS-E2E-142-klik-ganda-cancel-subscription-dan-convert | FE+BE |
| TC-AC-CS-528 | E2E | TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | FE+BE |
| TC-AC-CS-529 | E2E | TC-AC-CS-E2E-054-state-tenant-client-suspended-dan-expired-pada-add-renew | FE+BE |
| TC-AC-CS-530 | E2E | TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada | FE+BE |
| TC-AC-CS-531 | E2E | TC-AC-CS-E2E-055-state-tenant-cancel-job-dan-suspend-trial-pada-client | FE+BE |
| TC-AC-CS-532 | E2E | TC-AC-CS-E2E-150-state-tenant-trial-expired-pada-dropdown-convert-dan-activate-trial | FE+BE |
| TC-AC-CS-533 | E2E | TC-AC-CS-E2E-150-state-tenant-trial-expired-pada-dropdown-convert-dan-activate-trial | FE+BE |
| TC-AC-CS-534 | E2E | TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | FE+BE |
| TC-AC-CS-535 | E2E | TC-AC-CS-E2E-076-job-scheduled-flip | FE+BE |
| TC-AC-CS-536 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-537 | E2E | TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | FE+BE |
| TC-AC-CS-538 | E2E | TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | FE+BE |
| TC-AC-CS-539 | E2E | TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | FE+BE |
| TC-AC-CS-540 | E2E | TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | FE+BE |
| TC-AC-CS-541 | E2E | TC-AC-CS-E2E-145-list-ikon-dan-color-role-row-action | FE+BE |
| TC-AC-CS-542 | E2E | TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | FE+BE |
| TC-AC-CS-543 | E2E | TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes | FE+BE |
| TC-AC-CS-544 | E2E | TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes | FE+BE |
| TC-AC-CS-545 | E2E | TC-AC-CS-E2E-070-cancel-request-requester | FE+BE |
| TC-AC-CS-546 | E2E | TC-AC-CS-E2E-151-job-flip-dilewati-dan-race-cancel-request | FE+BE |
| TC-AC-CS-547 | E2E | TC-AC-CS-E2E-071-cancel-request-perubahan-status-dan-pending-diedit | FE+BE |
| TC-AC-CS-548 | E2E | TC-AC-CS-E2E-152-job-timeout-auto-cancel-convert-dan-edit | FE+BE |
| TC-AC-CS-549 | E2E | TC-AC-CS-E2E-055-state-tenant-cancel-job-dan-suspend-trial-pada-client | FE+BE |
| TC-AC-CS-550 | E2E | TC-AC-CS-E2E-060-edit-tanpa-perubahan-trial-dan-alokasi | FE+BE |
| TC-AC-CS-551 | E2E | TC-AC-CS-E2E-081-approvals-approve-dan-reject-renewal | FE+BE |
| TC-AC-CS-552 | E2E | TC-AC-CS-E2E-066-convert-trial-principal-trial-expired-dan-dialog-tanpa | FE+BE |
| TC-AC-CS-553 | E2E | TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal | FE+BE |
| TC-AC-CS-554 | E2E | TC-AC-CS-E2E-036-add-group-manager-ancestor-dan-start-date-29-februari | FE+BE |
| TC-AC-CS-555 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-556 | E2E | TC-AC-CS-E2E-029-form-add-opsi-plan-dan-pay-from-distributor-dan-partner | FE+BE |
| TC-AC-CS-557 | E2E | TC-AC-CS-E2E-083-approvals-trial-activation-oleh-additional-approver-principal | FE+BE |
| TC-AC-CS-558 | E2E | TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | FE+BE |
| TC-AC-CS-559 | E2E | TC-AC-CS-E2E-062-edit-dirty-guard-dan-unsaved-changes | FE+BE |
| TC-AC-CS-560 | E2E | TC-AC-CS-E2E-068-cancel-subscription-dialog | FE+BE |
| TC-AC-CS-561 | E2E | TC-AC-CS-E2E-042-form-add-clear-field-dan-unsaved-changes | FE+BE |
| TC-AC-CS-562 | E2E | TC-AC-CS-E2E-144-kondisi-sisa-ceiling-back-browser-plan-archive-tier-toast | FE+BE |
| TC-AC-CS-563 | E2E | TC-AC-CS-E2E-163-resilience-retry-setelah-timeout-dan-toast-error-bertahan | FE+BE |
| TC-AC-CS-564 | E2E | TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client | FE+BE |
| TC-AC-CS-565 | E2E | TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client | FE+BE |
| TC-AC-CS-566 | E2E | TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client | FE+BE |
| TC-AC-CS-567 | E2E | TC-AC-CS-E2E-007-list-format-subscription-id-dan-perilaku-anchor-nama-client | FE+BE |
| TC-AC-CS-568 | E2E | TC-AC-CS-E2E-045-aksesibilitas-form-add-activate-trial-dan-edit | FE+BE |
| TC-AC-CS-569 | E2E | TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon | FE+BE |
| TC-AC-CS-570 | E2E | TC-AC-CS-E2E-131-notifikasi-in-app-approver | FE+BE |
| TC-AC-CS-571 | E2E | TC-AC-CS-E2E-132-notifikasi-in-app-requester-dan-multi-role | FE+BE |
| TC-AC-CS-572 | E2E | TC-AC-CS-E2E-049-activate-trial-ceiling-dan-input-digit | FE+BE |
| TC-AC-CS-573 | E2E | TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | FE+BE |
| TC-AC-CS-574 | E2E | TC-AC-CS-E2E-053-activate-trial-form-dirty-dan-backdrop | FE+BE |
| TC-AC-CS-575 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-576 | E2E | TC-AC-CS-E2E-091-list-filter-chip-lanjutan-dan-pemulihan-opsi | FE+BE |
| TC-AC-CS-577 | E2E | TC-AC-CS-E2E-162-multi-konteks-race-add-cancel-renew-dan-convert-ganda | FE+BE |
| TC-AC-CS-578 | E2E | TC-AC-CS-E2E-138-multi-konteks-approver-dan-requester-bersamaan | FE+BE |
| TC-AC-CS-579 | E2E | TC-AC-CS-E2E-036-add-group-manager-ancestor-dan-start-date-29-februari | FE+BE |
| TC-AC-CS-580 | E2E | TC-AC-CS-E2E-036-add-group-manager-ancestor-dan-start-date-29-februari | FE+BE |
| TC-AC-CS-581 | E2E | TC-AC-CS-E2E-003-list-keadaan-kosong-distributor-tanpa-data | FE+BE |
| TC-AC-CS-582 | E2E | TC-AC-CS-E2E-010-detail-subscription-info | FE+BE |
| TC-AC-CS-583 | E2E | TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon | FE+BE |
| TC-AC-CS-584 | E2E | TC-AC-CS-E2E-147-edit-duration-start-date-29-februari | FE+BE |
| TC-AC-CS-585 | E2E | TC-AC-CS-E2E-013-detail-tombol-aksi-mengikuti-row-action | FE+BE |
| TC-AC-CS-586 | E2E | TC-AC-CS-E2E-002-list-toolbar-dan-label-aksesibel-ikon | FE+BE |
| TC-AC-CS-587 | E2E | TC-AC-CS-E2E-122-subscription-log-modal-dan-header | FE+BE |
| TC-AC-CS-588 | E2E | TC-AC-CS-E2E-122-subscription-log-modal-dan-header | FE+BE |
| TC-AC-CS-589 | E2E | TC-AC-CS-E2E-122-subscription-log-modal-dan-header | FE+BE |
| TC-AC-CS-590 | E2E | TC-AC-CS-E2E-155-subscription-log-row-action-semua-status | FE+BE |
| TC-AC-CS-591 | E2E | TC-AC-CS-E2E-123-subscription-log-entri-detail-dan-role | FE+BE |
| TC-AC-CS-592 | E2E | TC-AC-CS-E2E-123-subscription-log-entri-detail-dan-role | FE+BE |
| TC-AC-CS-593 | E2E | TC-AC-CS-E2E-139-resilience-gagal-baca-list-detail-log-dan-download | FE+BE |
| TC-AC-CS-594 | E2E | TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | FE+BE |
| TC-AC-CS-595 | E2E | TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | FE+BE |
| TC-AC-CS-596 | E2E | TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | FE+BE |
| TC-AC-CS-597 | E2E | TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | FE+BE |
| TC-AC-CS-598 | E2E | TC-AC-CS-E2E-124-subscription-log-katalog-created-approved-rejected-edited | FE+BE |
| TC-AC-CS-599 | E2E | TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated | FE+BE |
| TC-AC-CS-600 | E2E | TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated | FE+BE |
| TC-AC-CS-601 | E2E | TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated | FE+BE |
| TC-AC-CS-602 | E2E | TC-AC-CS-E2E-126-subscription-log-entri-hasil-job | FE+BE |
| TC-AC-CS-603 | E2E | TC-AC-CS-E2E-126-subscription-log-entri-hasil-job | FE+BE |
| TC-AC-CS-604 | E2E | TC-AC-CS-E2E-126-subscription-log-entri-hasil-job | FE+BE |
| TC-AC-CS-605 | E2E | TC-AC-CS-E2E-125-subscription-log-katalog-canceled-archived-activated | FE+BE |
| TC-AC-CS-606 | E2E | TC-AC-CS-E2E-127-subscription-log-katalog-renew-convert-resubmit-urutan | FE+BE |
| TC-AC-CS-607 | E2E | TC-AC-CS-E2E-127-subscription-log-katalog-renew-convert-resubmit-urutan | FE+BE |
| TC-AC-CS-608 | E2E | TC-AC-CS-E2E-127-subscription-log-katalog-renew-convert-resubmit-urutan | FE+BE |
| TC-AC-CS-609 | E2E | TC-AC-CS-E2E-156-subscription-log-urutan-immutability-dan-edit-no-op | FE+BE |
| TC-AC-CS-610 | E2E | TC-AC-CS-E2E-135-defense-in-depth-zero-access-dan-read-only | FE+BE |
| TC-AC-CS-611 | E2E | TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | FE+BE |
| TC-AC-CS-612 | E2E | TC-AC-CS-E2E-056-state-tenant-approve-trial-cancel-request-dan-resubmit-pada | FE+BE |
| TC-AC-CS-613 | E2E | TC-AC-CS-E2E-112-log-aksi-renew | FE+BE |
| TC-AC-CS-614 | E2E | TC-AC-CS-E2E-116-log-aksi-cancel-dan-cancel-request | FE+BE |
| TC-AC-CS-615 | E2E | TC-AC-CS-E2E-074-resubmit-dan-edit-renewal-partner-trial | FE+BE |
| TC-AC-CS-616 | E2E | TC-AC-CS-E2E-117-log-aksi-resubmit | FE+BE |
| TC-AC-CS-617 | E2E | TC-AC-CS-E2E-119-log-absence-approve-dan-reject | FE+BE |
| TC-AC-CS-618 | E2E | TC-AC-CS-E2E-026-form-add-screening-dan-blok-payment | FE+BE |
| TC-AC-CS-619 | E2E | TC-AC-CS-E2E-134-defense-in-depth-cancel-markup-payload-dan-detail | FE+BE |
| TC-AC-CS-620 | E2E | TC-AC-CS-E2E-058-edit-validasi-duration-start-date-dan-ceiling-trial | FE+BE |
| TC-AC-CS-621 | E2E | TC-AC-CS-E2E-044-form-state-submitting-dan-klik-ganda-add-dan-activate-trial | FE+BE |
| TC-AC-CS-622 | E2E | TC-AC-CS-E2E-045-aksesibilitas-form-add-activate-trial-dan-edit | FE+BE |
| TC-AC-CS-623 | E2E | TC-AC-CS-E2E-045-aksesibilitas-form-add-activate-trial-dan-edit | FE+BE |
| TC-AC-CS-624 | E2E | TC-AC-CS-E2E-072-cancel-request-group-manager-dan-total-control | FE+BE |
| TC-AC-CS-625 | E2E | TC-AC-CS-E2E-078-job-pre-timeout-warning-dan-timeout-auto-cancel | FE+BE |
| TC-AC-CS-626 | E2E | TC-AC-CS-E2E-098-list-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-627 | E2E | TC-AC-CS-E2E-098-list-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-628 | E2E | TC-AC-CS-E2E-098-list-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-629 | E2E | TC-AC-CS-E2E-110-changelog-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-630 | E2E | TC-AC-CS-E2E-110-changelog-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-631 | E2E | TC-AC-CS-E2E-110-changelog-setup-column-anggota-hideable-lain | FE+BE |
| TC-AC-CS-632 | E2E | TC-AC-CS-E2E-071-cancel-request-perubahan-status-dan-pending-diedit | FE+BE |
| TC-AC-CS-633 | E2E | TC-AC-CS-E2E-152-job-timeout-auto-cancel-convert-dan-edit | FE+BE |
| TC-AC-CS-634 | E2E | TC-AC-CS-E2E-020-zero-access-group-c-list-tooltip-dan-tab-subscription-client | FE+BE |
| TC-AC-CS-635 | E2E | TC-AC-CS-E2E-043-form-dirty-guard-backdrop-reload-route-dan-footer | FE+BE |
| TC-AC-CS-636 | E2E | TC-AC-CS-E2E-011-detail-license-quota | FE+BE |

## 4. Prasyarat Eksekusi dan Asumsi yang Diterima

Semua spec berstatus `draft`: penulisan selesai, tetapi belum dapat dijalankan sebelum prasyarat berikut disediakan. Lihat `paket-tindak-lanjut-e2e.md` di work item untuk daftar lengkap per pemilik.

- Fixture `Fixture.license-allocation-subscription`, sesi API actor, kontrol jam, job trigger, mail-catcher, pembaca Wallet, notifikasi dan App Access, fixture restore baseline, serta klik tersinkron antar-konteks: disediakan tim FE/BE (belum ada).
- Env password `AC_SUB_*` didaftarkan tim FE di `spectra.config.ts` dan `.env.example`, termasuk `AC_SUB_RO_DIST_PASSWORD` dan `AC_SUB_TC_B_PASSWORD`.
- Resilience memakai `Spectra.intercept()` parsial di atas backend nyata (modul tanpa openapi.yaml atau LLD); hasil race TC 517 dan 519 ditegaskan sebagai salah satu dari dua kemungkinan; TC Manual Only (d) diotomasi dengan klik tersinkron.
- Spec di atas 35 langkah dipertahankan dengan alasan di Notes; pemecahan menunggu hasil `e2e-audit`.
- Masalah sumber TC dicatat di bagian Temuan untuk QA tiap spec dan ditunda ke pemilik TC.
