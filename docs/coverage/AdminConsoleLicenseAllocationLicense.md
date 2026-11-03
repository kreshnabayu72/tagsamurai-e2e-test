# Coverage E2E — Admin Console > Allocation > License Allocation

Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md` (531 TC granular aktif). Modul tidak punya `tc-license-allocation-license-backend.md`, `API/`, maupun LLD.
Suite: `specs/AdminConsole/LicenseAllocationLicense/` (beserta `suite.md`).
Prefix Modul: `AC` + `LA` (`TC-AC-LA-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (139 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-AC-LA-E2E-001-screening-list-tab-current-history-dan-tooltip | Screening List License Allocation: Tab Current, Tab History, dan Tooltip Table Tools | FE+BE | 31 | TC-AC-LA-1, TC-AC-LA-2, TC-AC-LA-3 |
| TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status | Screening Baris List: Allocation ID, Client, Allocated By, dan Badge Status | FE+BE | 40 | TC-AC-LA-4, TC-AC-LA-5, TC-AC-LA-6, TC-AC-LA-7 |
| TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | Ragam Baris Example Data: Principal, Distributor, Station, Storage, dan App | FE+BE | 41 | TC-AC-LA-18, TC-AC-LA-19, TC-AC-LA-20, TC-AC-LA-21, TC-AC-LA-22 |
| TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | Ragam Baris Example Data: Cost Snapshot, Term Pending, Expired, dan Plan Snapshot | FE+BE | 35 | TC-AC-LA-23, TC-AC-LA-24, TC-AC-LA-25, TC-AC-LA-26, TC-AC-LA-27 |
| TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | State List: Loading, Empty, Empty Filtered, Pemulihan, dan Tab Awal | FE+BE | 33 | TC-AC-LA-10, TC-AC-LA-11, TC-AC-LA-12, TC-AC-LA-13, TC-AC-LA-16, TC-AC-LA-17 |
| TC-AC-LA-E2E-006-isi-tab-current-dan-history-serta-toolbar | Isi Tab Current dan History: Status per Tab dan Toolbar per Tab | FE+BE | 34 | TC-AC-LA-28, TC-AC-LA-29, TC-AC-LA-34 |
| TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol | State per Tab: Pemulihan Search Filter Sort, Independensi Tab, dan Aksi di Row List | FE+BE | 44 | TC-AC-LA-35, TC-AC-LA-36, TC-AC-LA-37, TC-AC-LA-38 |
| TC-AC-LA-E2E-008-row-action-menu-per-status | Row Action Menu per Status: Ikon, Urutan, dan Aksi yang Tersedia | FE+BE | 20 | TC-AC-LA-8, TC-AC-LA-9, TC-AC-LA-33 |
| TC-AC-LA-E2E-009-screening-modal-allocation-log | Screening Modal Allocation Log: Isi, Copy ID, Scroll, Empty State, dan Cara Tutup | FE+BE | 39 | TC-AC-LA-39, TC-AC-LA-40, TC-AC-LA-41, TC-AC-LA-42, TC-AC-LA-43 |
| TC-AC-LA-E2E-010-modal-allocation-log-loading-dan-immutability | Modal Allocation Log: Loading dan Immutability Entri | FE+BE | 17 | TC-AC-LA-45, TC-AC-LA-414 |
| TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi | Guided Tooltip: Walkthrough Pertama Kali, Replay, Navigasi, dan Skip | FE+BE | 43 | TC-AC-LA-47, TC-AC-LA-48, TC-AC-LA-49, TC-AC-LA-50 |
| TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain | Guided Tooltip: Resize, Target Permanen, Keyboard, dan Halaman Approvals | FE+BE | 34 | TC-AC-LA-51, TC-AC-LA-52, TC-AC-LA-53, TC-AC-LA-54 |
| TC-AC-LA-E2E-013-role-matrix-entity-gate | Role Matrix: Entity Gate Menu License Allocation per Entitas | FE+BE | 29 | TC-AC-LA-55, TC-AC-LA-56, TC-AC-LA-57, TC-AC-LA-58, TC-AC-LA-59 |
| TC-AC-LA-E2E-014-role-matrix-visibilitas-menu | Role Matrix: Visibilitas Menu License Allocation dan Approvals per Role | FE+BE | 51 | TC-AC-LA-60, TC-AC-LA-61, TC-AC-LA-62 |
| TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog | Role Matrix: Visibilitas Tombol + Allocation, Row Action Allocation Log, Download, dan Changelog | FE+BE | 35 | TC-AC-LA-63, TC-AC-LA-64, TC-AC-LA-44, TC-AC-LA-69 |
| TC-AC-LA-E2E-016-role-matrix-visibilitas-row-action-cancel-dan-edit | Role Matrix: Visibilitas Row Action Cancel dan Edit | FE+BE | 38 | TC-AC-LA-65, TC-AC-LA-66 |
| TC-AC-LA-E2E-017-role-matrix-visibilitas-row-action-resubmit-dan-review | Role Matrix: Visibilitas Row Action Resubmit dan Tombol Review di Approvals | FE+BE | 49 | TC-AC-LA-67, TC-AC-LA-68 |
| TC-AC-LA-E2E-018-role-matrix-negatif-access-level-read-only | Role Matrix Negatif: Access Level Read Only Tidak Dapat Mengubah | FE+BE | 24 | TC-AC-LA-70, TC-AC-LA-71 |
| TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | Role Matrix Positif: Allocate License per Capability dan Peran | FE+BE | 43 | TC-AC-LA-72, TC-AC-LA-80, TC-AC-LA-83, TC-AC-LA-84, TC-AC-LA-85 |
| TC-AC-LA-E2E-020-role-matrix-positif-edit-cancel-resubmit-capability-create-update | Role Matrix Positif: Edit, Cancel, dan Resubmit per Capability Create dan Update | FE+BE | 28 | TC-AC-LA-73, TC-AC-LA-74, TC-AC-LA-481 |
| TC-AC-LA-E2E-021-role-matrix-positif-cancel-pending-dan-approve-per-peran | Role Matrix Positif: Cancel Pending dan Approve oleh Group Manager, Total Control, dan Additional Approver | FE+BE | 29 | TC-AC-LA-78, TC-AC-LA-79, TC-AC-LA-81 |
| TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | Scope Data READ dan WRITE: Distributor, Partner, dan Principal | FE+BE | 41 | TC-AC-LA-86, TC-AC-LA-87, TC-AC-LA-97, TC-AC-LA-88, TC-AC-LA-89 |
| TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | Scope Group Role: Zero Access dan Group A, B, C pada Satu Akun | FE+BE | 30 | TC-AC-LA-90, TC-AC-LA-91, TC-AC-LA-92, TC-AC-LA-93, TC-AC-LA-96 |
| TC-AC-LA-E2E-024-scope-group-manager-hierarki-dan-read-only-detail | Scope Group Manager Hierarki, Cancel Pending Lintas Partner, dan Tab License Detail Read Only | FE+BE | 31 | TC-AC-LA-94, TC-AC-LA-95, TC-AC-LA-507 |
| TC-AC-LA-E2E-025-job-expiry-station-dan-storage-tetap-active | Job Expiry Transition: Station dan Storage Tetap Active di Tab Current | FE+BE | 21 | TC-AC-LA-30 |
| TC-AC-LA-E2E-026-perpindahan-baris-antar-tab-cancel-dan-resubmit | Perpindahan Baris Antar Tab: Cancel dan Resubmit | FE+BE | 23 | TC-AC-LA-31, TC-AC-LA-32 |
| TC-AC-LA-E2E-027-screening-form-allocate-per-mode | Screening Form Allocate License per Mode: Principal, Concurrent User, App, Station, Storage, dan Loading | FE+BE | 34 | TC-AC-LA-99, TC-AC-LA-100, TC-AC-LA-101, TC-AC-LA-102, TC-AC-LA-103, TC-AC-LA-107 |
| TC-AC-LA-E2E-028-screening-payment-distributor-dan-partner | Screening Section Payment: Distributor dan Partner (Pay From) | FE+BE | 27 | TC-AC-LA-104, TC-AC-LA-105, TC-AC-LA-106 |
| TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | Validasi Field Wajib Form Allocate: Type, Client, Target, Pesan Inline, dan Aksesibilitas | FE+BE | 24 | TC-AC-LA-108, TC-AC-LA-109, TC-AC-LA-110, TC-AC-LA-118, TC-AC-LA-119 |
| TC-AC-LA-E2E-030-validasi-additional-quantity | Validasi Additional Quantity: Kosong, Nol, Non-Digit, dan Lebih dari 15 Karakter | FE+BE | 20 | TC-AC-LA-111, TC-AC-LA-112, TC-AC-LA-114, TC-AC-LA-116 |
| TC-AC-LA-E2E-031-additional-quantity-batas-valid-submit-sukses | Additional Quantity Batas Valid: Nilai 1 dan 15 Digit Submit Sukses | FE+BE | 19 | TC-AC-LA-113, TC-AC-LA-509 |
| TC-AC-LA-E2E-032-validasi-pay-from-dan-saldo-partner | Validasi Payment Partner: Pay From Kosong dan Saldo Kantong Kurang | FE+BE | 20 | TC-AC-LA-117, TC-AC-LA-144 |
| TC-AC-LA-E2E-033-validasi-harga-belum-diset-dan-batas-saldo-distributor | Validasi Payment Distributor: Harga Belum Di-set dan Batas Saldo Wallet 15 Digit | FE+BE | 16 | TC-AC-LA-146, TC-AC-LA-510 |
| TC-AC-LA-E2E-034-dropdown-client | Dropdown Client: Opsi Eligible, Search, dan Badge Status Suspended Expired | FE+BE | 28 | TC-AC-LA-120, TC-AC-LA-121, TC-AC-LA-122 |
| TC-AC-LA-E2E-035-opsi-target-term-eligible | Opsi Target: Term Paid Active dan Pending, Client-wide, Free, Trial, dan Callout | FE+BE | 34 | TC-AC-LA-123, TC-AC-LA-124, TC-AC-LA-125, TC-AC-LA-126, TC-AC-LA-127, TC-AC-LA-128 |
| TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | Opsi Type per Target dan Current Quota: FAMS, SIEM, SAMS, dan Asset Control App | FE+BE | 33 | TC-AC-LA-129, TC-AC-LA-130, TC-AC-LA-131, TC-AC-LA-132, TC-AC-LA-133, TC-AC-LA-134, TC-AC-LA-135 |
| TC-AC-LA-E2E-037-reset-berantai-ganti-client-target-type | Reset Berantai Form Allocate: Ganti Client, Target, dan Type | FE+BE | 22 | TC-AC-LA-136, TC-AC-LA-137, TC-AC-LA-138 |
| TC-AC-LA-E2E-038-preview-cost-concurrent-user-prorata | Preview Cost Concurrent User: Prorata Hari, Term Pending, dan Real-time | FE+BE | 14 | TC-AC-LA-140, TC-AC-LA-142, TC-AC-LA-152 |
| TC-AC-LA-E2E-039-preview-cost-per-jenis-license | Preview Cost per Jenis License: Asset Control App, Storage, dan Station | FE+BE | 25 | TC-AC-LA-148, TC-AC-LA-149, TC-AC-LA-150, TC-AC-LA-511 |
| TC-AC-LA-E2E-040-cost-terkunci-pembulatan-dan-cost-nol | Cost Terkunci: Pembulatan Half-up, Cost Nol, dan Nominal Sama dari Preview sampai Capture | FE+BE | 35 | TC-AC-LA-143, TC-AC-LA-151, TC-AC-LA-513 |
| TC-AC-LA-E2E-041-skeleton-preview-pay-from-dan-cross-distributor | Skeleton Preview, Harga dan Saldo per Pay From, dan Cross-Distributor Sourcing | FE+BE | 29 | TC-AC-LA-147, TC-AC-LA-153, TC-AC-LA-506 |
| TC-AC-LA-E2E-042-submit-concurrent-user-asset-log-source-addon | Submit Allocate: Concurrent User, Asset License, dan Log Source | FE+BE | 38 | TC-AC-LA-155, TC-AC-LA-156, TC-AC-LA-157 |
| TC-AC-LA-E2E-043-submit-asset-control-app-station-storage | Submit Allocate: Asset Control App, Station, dan Storage | FE+BE | 33 | TC-AC-LA-159, TC-AC-LA-160, TC-AC-LA-161, TC-AC-LA-516 |
| TC-AC-LA-E2E-044-submit-status-awal-toggle-approval-requester-distributor | Submit Allocate: Status Awal Berdasarkan Toggle Approval dan Target Pending (Distributor) | FE+BE | 39 | TC-AC-LA-162, TC-AC-LA-165, TC-AC-LA-166 |
| TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner | Submit Allocate: Status Awal Requester Group Manager, Default User, Partner, dan Principal | FE+BE | 47 | TC-AC-LA-163, TC-AC-LA-164, TC-AC-LA-530, TC-AC-LA-173 |
| TC-AC-LA-E2E-046-submit-properti-record-end-date-successor-dan-kantong-distributor | Submit Allocate: End Date Snapshot, Term Successor, dan Kantong Tunggal Distributor | FE+BE | 30 | TC-AC-LA-167, TC-AC-LA-170, TC-AC-LA-172 |
| TC-AC-LA-E2E-047-submit-allocation-id-top-up-dan-pay-from-partner | Submit Allocate: Format Allocation ID, Top-up Berulang, dan Pay From Partner | FE+BE | 33 | TC-AC-LA-168, TC-AC-LA-169, TC-AC-LA-171 |
| TC-AC-LA-E2E-048-notifikasi-submit-plan-owner-dan-approver | Notifikasi In-App akibat Submit: Plan Owner dan Approver Pool | FE+BE | 32 | TC-AC-LA-174, TC-AC-LA-505, TC-AC-LA-175 |
| TC-AC-LA-E2E-049-notifikasi-edit-pending | Notifikasi In-App akibat Edit Pending | FE+BE | 22 | TC-AC-LA-438, TC-AC-LA-495 |
| TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | Dirty-Guard Form Allocate: Tutup Bersih, Tutup Dirty, Cancel Dialog, dan Backdrop | FE+BE | 29 | TC-AC-LA-176, TC-AC-LA-531, TC-AC-LA-177, TC-AC-LA-178, TC-AC-LA-179 |
| TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field | Dirty-Guard Navigasi, Refresh F5, dan Clear Field Form Allocate | FE+BE | 37 | TC-AC-LA-180, TC-AC-LA-181, TC-AC-LA-183, TC-AC-LA-184 |
| TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state | Form Resubmit Pre-filled, Stay on this Form, Tanpa Stay, dan Saving State | FE+BE | 37 | TC-AC-LA-182, TC-AC-LA-185, TC-AC-LA-186, TC-AC-LA-187 |
| TC-AC-LA-E2E-053-preview-cost-hari-terakhir-dan-zona-waktu-plan-owner | Preview Cost Hari Terakhir Term dan Zona Waktu Plan Owner | FE+BE | 18 | TC-AC-LA-141, TC-AC-LA-154 |
| TC-AC-LA-E2E-054-submit-addon-fams-lima-jenis | Submit Allocate: Addon FAMS (Audit, Maintenance, Tracking, Maps, IT Inventory) ke Target Paid Active | FE+BE | 6 | TC-AC-LA-158 |
| TC-AC-LA-E2E-055-edit-screening-save-disabled-dan-clear-field | Edit Allocation: Screening Popup Edit, Save Disabled, dan Clear Field | FE+BE | 22 | TC-AC-LA-188, TC-AC-LA-189, TC-AC-LA-210 |
| TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target | Edit Allocation: Dirty-Guard, Cancel D-02, Reset Type Saat Ganti Target, dan Asset Control App | FE+BE | 27 | TC-AC-LA-209, TC-AC-LA-486, TC-AC-LA-194, TC-AC-LA-195 |
| TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | Edit Allocation Waiting for Approval: Quantity, Snapshot Harga, Ganti Target, dan Klik Ganda Save | FE+BE | 44 | TC-AC-LA-190, TC-AC-LA-191, TC-AC-LA-192, TC-AC-LA-193, TC-AC-LA-487 |
| TC-AC-LA-E2E-058-edit-record-pending | Edit Allocation Pending dengan Require Approval ON: Kembali ke Waiting for Approval, D-04, dan Requester Bypass | FE+BE | 33 | TC-AC-LA-211, TC-AC-LA-212, TC-AC-LA-214 |
| TC-AC-LA-E2E-059-edit-blokir-saldo-dan-app-kedua | Edit Allocation Ditolak karena Kondisi Data: Saldo Tidak Cukup dan Asset Control App Kedua | FE+BE | 17 | TC-AC-LA-196, TC-AC-LA-204 |
| TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | Cancel Allocation: Dialog D-03, Go Back, Klik Ganda, dan Cancel oleh Requester | FE+BE | 47 | TC-AC-LA-217, TC-AC-LA-218, TC-AC-LA-228, TC-AC-LA-219, TC-AC-LA-220 |
| TC-AC-LA-E2E-061-cancel-pending-total-control-dan-default-user | Cancel Allocation Pending oleh Total Control Tanpa Refund dan Default User Principal | FE+BE | 23 | TC-AC-LA-221, TC-AC-LA-227 |
| TC-AC-LA-E2E-062-resubmit-alur-utama | Resubmit: Form Pre-filled, Record Baru, Snapshot Harga Baru, Stay on Form, dan Klik Ganda | FE+BE | 61 | TC-AC-LA-229, TC-AC-LA-239, TC-AC-LA-230, TC-AC-LA-232, TC-AC-LA-488, TC-AC-LA-231, TC-AC-LA-240, TC-AC-LA-237 |
| TC-AC-LA-E2E-063-resubmit-blokir-saldo-dan-app-kedua | Resubmit Ditolak karena Kondisi Data: Saldo Kurang dan Asset Control App Kedua | FE+BE | 20 | TC-AC-LA-521, TC-AC-LA-522 |
| TC-AC-LA-E2E-064-approve-screening-detail-approval-dan-hasil-active | Approve: Screening Detail Approval, Hasil Active, dan Target Pending | FE+BE | 33 | TC-AC-LA-241, TC-AC-LA-242, TC-AC-LA-243 |
| TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage | Approve: Term Pending Menjadi Active, Snapshot Harga, Asset Control App, Station, dan Storage | FE+BE | 32 | TC-AC-LA-244, TC-AC-LA-245, TC-AC-LA-246, TC-AC-LA-247 |
| TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated | Approve dan Reject dari Approvals: Reject, Last Updated, Tanpa Inline, dan Notifikasi | FE+BE | 55 | TC-AC-LA-259, TC-AC-LA-260, TC-AC-LA-248, TC-AC-LA-262 |
| TC-AC-LA-E2E-067-approve-reject-oleh-group-manager | Approve dan Reject oleh Group Manager: Approve-only dan Scope Region Jawa | FE+BE | 48 | TC-AC-LA-476, TC-AC-LA-477, TC-AC-LA-478 |
| TC-AC-LA-E2E-068-approve-reject-oleh-additional-approver-dan-principal | Approve dan Reject oleh Additional Approver dan Total Control Principal | FE+BE | 28 | TC-AC-LA-480, TC-AC-LA-261 |
| TC-AC-LA-E2E-069-approve-blokir-gate-target-dan-app-ganda | Approve Ditolak karena Kondisi Data: Target Tidak Eligible, Gate Station Storage, dan App Ganda | FE+BE | 29 | TC-AC-LA-250, TC-AC-LA-251, TC-AC-LA-252 |
| TC-AC-LA-E2E-070-edit-validasi-field-form | Edit Allocation: Validasi Field Type, Target, dan Additional Quantity | FE+BE | 31 | TC-AC-LA-205, TC-AC-LA-206, TC-AC-LA-207, TC-AC-LA-208 |
| TC-AC-LA-E2E-071-edit-record-pending-toggle-off | Edit Allocation Pending dengan Require Approval OFF: Tetap Pending atau Active dengan Capture | FE+BE | 30 | TC-AC-LA-213, TC-AC-LA-215, TC-AC-LA-216 |
| TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | Job Sistem Timeout Auto-Cancel dan Warning H-24 | FE+BE | 71 | TC-AC-LA-263, TC-AC-LA-264, TC-AC-LA-265, TC-AC-LA-266, TC-AC-LA-484, TC-AC-LA-279 |
| TC-AC-LA-E2E-073-job-timeout-vs-approve | Job Timeout Auto-Cancel vs Approve pada Batas SLA | FE+BE | 32 | TC-AC-LA-465, TC-AC-LA-485 |
| TC-AC-LA-E2E-074-job-activation-transition | Job Sistem Activation Transition | FE+BE | 28 | TC-AC-LA-267, TC-AC-LA-268 |
| TC-AC-LA-E2E-075-job-expiry-transition | Job Sistem Expiry Transition | FE+BE | 63 | TC-AC-LA-269, TC-AC-LA-270, TC-AC-LA-271, TC-AC-LA-272, TC-AC-LA-273 |
| TC-AC-LA-E2E-076-job-pada-client-suspended | Job Sistem pada Alokasi Milik Client Suspended | FE+BE | 33 | TC-AC-LA-278, TC-AC-LA-523, TC-AC-LA-524 |
| TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | Cancel Term: Dampak ke Alokasi Active, Pending, Station, Storage, dan Log | FE+BE | 52 | TC-AC-LA-274, TC-AC-LA-275, TC-AC-LA-276, TC-AC-LA-277, TC-AC-LA-397, TC-AC-LA-527 |
| TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | State Tenant: Entitas Pengalokasi Suspended Menolak Seluruh Aksi Tulis | FE+BE | 40 | TC-AC-LA-469, TC-AC-LA-496, TC-AC-LA-497, TC-AC-LA-498, TC-AC-LA-499, TC-AC-LA-500 |
| TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | State Tenant: Client Suspended dan Expired sebagai Penerima Alokasi | FE+BE | 41 | TC-AC-LA-467, TC-AC-LA-468, TC-AC-LA-470, TC-AC-LA-501, TC-AC-LA-502, TC-AC-LA-503, TC-AC-LA-504, TC-AC-LA-238 |
| TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate | Konkurensi Form Allocate: Client Dihapus, Gate Station Storage, dan App Ganda | FE+BE | 35 | TC-AC-LA-461, TC-AC-LA-462, TC-AC-LA-463, TC-AC-LA-464 |
| TC-AC-LA-E2E-081-konkurensi-form-allocate-target-submit-serentak | Konkurensi Form Allocate: Term Target Berubah dan Submit Serentak | FE+BE | 29 | TC-AC-LA-139, TC-AC-LA-466, TC-AC-LA-474 |
| TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | Konkurensi Edit, Cancel, dan Resubmit: Alokasi Diputus Pihak Lain dan Target Berubah | FE+BE | 66 | TC-AC-LA-201, TC-AC-LA-202, TC-AC-LA-203, TC-AC-LA-225, TC-AC-LA-235 |
| TC-AC-LA-E2E-083-konkurensi-approve-reject | Konkurensi Approve dan Reject: Keputusan Ganda, Cancel dan Edit Saat Review Terbuka | FE+BE | 33 | TC-AC-LA-255, TC-AC-LA-256, TC-AC-LA-257, TC-AC-LA-258 |
| TC-AC-LA-E2E-084-konkurensi-notifikasi-approver | Konkurensi Notifikasi Approver: Race Notifikasi dan Notifikasi Basi | FE+BE | 18 | TC-AC-LA-440, TC-AC-LA-515 |
| TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | Resilience Baca: Error Load List, Allocation Log, Modal Changelog, dan Download Gagal | FE+BE | 44 | TC-AC-LA-14, TC-AC-LA-15, TC-AC-LA-46, TC-AC-LA-347, TC-AC-LA-358, TC-AC-LA-381 |
| TC-AC-LA-E2E-086-resilience-aksi-tulis | Resilience Aksi Tulis: Edit, Cancel, Resubmit, Allocate, Timeout Jaringan, dan Reject Gagal | FE+BE | 62 | TC-AC-LA-197, TC-AC-LA-224, TC-AC-LA-236, TC-AC-LA-471, TC-AC-LA-472, TC-AC-LA-249 |
| TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | Defense-in-Depth: Validasi Server atas Submit Request Langsung (Distributor) | FE+BE | 19 | TC-AC-LA-443, TC-AC-LA-446, TC-AC-LA-447, TC-AC-LA-448, TC-AC-LA-449, TC-AC-LA-456 |
| TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | Defense-in-Depth: Quantity Non-bulat, Saldo, Edit Request Langsung, dan Markup Nama Client | FE+BE | 26 | TC-AC-LA-115, TC-AC-LA-145, TC-AC-LA-483, TC-AC-LA-508, TC-AC-LA-457 |
| TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability | Defense-in-Depth: Akses Ditolak untuk Zero Access dan Aktor Tanpa Capability | FE+BE | 16 | TC-AC-LA-444, TC-AC-LA-445, TC-AC-LA-98, TC-AC-LA-458 |
| TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | Defense-in-Depth: Capability Dicabut, Aktor Dinonaktifkan, dan Client Dipindah Binding | FE+BE | 24 | TC-AC-LA-450, TC-AC-LA-451, TC-AC-LA-452, TC-AC-LA-455, TC-AC-LA-529, TC-AC-LA-459 |
| TC-AC-LA-E2E-091-defense-peran-create-dan-update | Defense-in-Depth: Penolakan Server untuk Peran Create Saja dan Update Saja | FE+BE | 24 | TC-AC-LA-75, TC-AC-LA-76, TC-AC-LA-77 |
| TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver | Defense-in-Depth: Approve dan Reject oleh Bukan Approver, Self-Approval, dan Request ke Alokasi Non-Waiting | FE+BE | 20 | TC-AC-LA-253, TC-AC-LA-482, TC-AC-LA-254, TC-AC-LA-460 |
| TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | Defense-in-Depth: Edit, Cancel, dan Resubmit Milik Orang Lain dan pada Status Final | FE+BE | 28 | TC-AC-LA-82, TC-AC-LA-222, TC-AC-LA-199, TC-AC-LA-233, TC-AC-LA-200, TC-AC-LA-223, TC-AC-LA-234 |
| TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal | Absence Log: Pembukaan Modal, Request Langsung Ditolak, Edit Tanpa Perubahan, Cancel Ulang, dan Aksi Tulis Gagal | FE+BE | 81 | TC-AC-LA-413, TC-AC-LA-198, TC-AC-LA-226, TC-AC-LA-419 |
| TC-AC-LA-E2E-095-defense-approver-dicabut-dan-group-manager-luar-scope | Defense-in-Depth: Approver yang Wewenangnya Dicabut dan Group Manager di Luar Scope Group | FE+BE | 14 | TC-AC-LA-453, TC-AC-LA-454, TC-AC-LA-479 |
| TC-AC-LA-E2E-096-sort-list-payment-pindah-kolom-dan-default | Sort List: Payment, Pindah Kolom, dan Default Sort | FE+BE | 18 | TC-AC-LA-309, TC-AC-LA-310, TC-AC-LA-311 |
| TC-AC-LA-E2E-097-search-list-teks-dan-kolom-status-quantity | Search List: Siklus Interaksi, Allocated By, dan Status | FE+BE | 32 | TC-AC-LA-280, TC-AC-LA-282, TC-AC-LA-283 |
| TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | Search List: Kolom Opsional, Guard Last Updated, Visibilitas Kolom, Trim, dan Tab History | FE+BE | 48 | TC-AC-LA-285, TC-AC-LA-286, TC-AC-LA-287, TC-AC-LA-288, TC-AC-LA-289, TC-AC-LA-290 |
| TC-AC-LA-E2E-099-filter-list-screening-dan-opsi | Filter List: Screening Panel, Opsi Status, Opsi DISTINCT, dan Number Range | FE+BE | 51 | TC-AC-LA-291, TC-AC-LA-293, TC-AC-LA-294, TC-AC-LA-295 |
| TC-AC-LA-E2E-100-filter-list-eksekusi-tanggal-dan-logika | Filter List: Tanggal Last Updated dan Logika OR AND | FE+BE | 27 | TC-AC-LA-296, TC-AC-LA-297 |
| TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | Filter List: Chip, Search Dropdown, Clear Field, Kolom Disembunyikan, Reset Halaman, dan Tab History | FE+BE | 56 | TC-AC-LA-298, TC-AC-LA-299, TC-AC-LA-300, TC-AC-LA-301, TC-AC-LA-302, TC-AC-LA-303 |
| TC-AC-LA-E2E-102-sort-list-siklus-dan-alfabetis | Sort List: Siklus Tiga Tahap dan Sort Alfabetis dengan atau Tanpa Nilai Kosong | FE+BE | 40 | TC-AC-LA-304, TC-AC-LA-305, TC-AC-LA-306 |
| TC-AC-LA-E2E-103-sort-list-numerik-allocated-by-payment-dan-default | Sort List: Numerik Quantity dan Cost serta Allocated By | FE+BE | 19 | TC-AC-LA-307, TC-AC-LA-308 |
| TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | Kombinasi Search, Filter, Sort, dan Pagination pada List serta Mutasi Saat Terfilter | FE+BE | 68 | TC-AC-LA-312, TC-AC-LA-313, TC-AC-LA-314, TC-AC-LA-315, TC-AC-LA-316, TC-AC-LA-317, TC-AC-LA-319, TC-AC-LA-318 |
| TC-AC-LA-E2E-105-setup-column-list-screening-dan-ceklis | Setup Column List: Screening Overlay dan Popup, serta Ceklis Kolom Hideable | FE+BE | 35 | TC-AC-LA-320, TC-AC-LA-321, TC-AC-LA-322 |
| TC-AC-LA-E2E-106-setup-column-list-drag-dan-pin | Setup Column List: Drag Urutan dan Pin Kolom Hideable | FE+BE | 29 | TC-AC-LA-323, TC-AC-LA-324 |
| TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard | Setup Column List: Kolom Curated, Reset to Default, dan Discard | FE+BE | 48 | TC-AC-LA-325, TC-AC-LA-326, TC-AC-LA-327, TC-AC-LA-328 |
| TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | Setup Column List: Guard Satu Kolom, Guard Pin Keempat, Konfigurasi Antar Tab, dan Cache Changelog | FE+BE | 50 | TC-AC-LA-329, TC-AC-LA-330, TC-AC-LA-331, TC-AC-LA-332, TC-AC-LA-333, TC-AC-LA-334 |
| TC-AC-LA-E2E-109-pagination-list | Pagination List: Ukuran Halaman, Navigasi, Reset Halaman, dan Tanpa Pagination Allocation Log | FE+BE | 32 | TC-AC-LA-335, TC-AC-LA-336, TC-AC-LA-337, TC-AC-LA-338, TC-AC-LA-339 |
| TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom | Download List: Seluruh Baris, Baris Terfilter, Nama Berkas History, dan Kolom Disembunyikan | FE+BE | 27 | TC-AC-LA-340, TC-AC-LA-341, TC-AC-LA-342, TC-AC-LA-343 |
| TC-AC-LA-E2E-111-download-list-isi-berkas-binary | Download List: Isi Berkas CSV dan XLSX, BOM, Urutan Baris, dan Tanggal Mengikuti General Settings | FE+BE | 35 | TC-AC-LA-344, TC-AC-LA-345, TC-AC-LA-346, TC-AC-LA-423 |
| TC-AC-LA-E2E-112-download-list-volume-lebih-5000-baris | Download List: Volume Lebih dari 5.000 Baris | FE+BE | 6 | TC-AC-LA-348 |
| TC-AC-LA-E2E-113-preservasi-state-list | Preservasi State List: Refresh F5, Kembali dari Client Detail, Klik Menu, dan Allocation Log | FE+BE | 39 | TC-AC-LA-349, TC-AC-LA-350, TC-AC-LA-351, TC-AC-LA-353 |
| TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | Modal Changelog: Screening, Cakupan Seluruh Alokasi, Format Sel, Empty State, dan Tutup | FE+BE | 38 | TC-AC-LA-354, TC-AC-LA-355, TC-AC-LA-356, TC-AC-LA-357, TC-AC-LA-359 |
| TC-AC-LA-E2E-115-changelog-search-dan-filter | Modal Changelog: Search dan Filter Panel | FE+BE | 85 | TC-AC-LA-360, TC-AC-LA-361, TC-AC-LA-362, TC-AC-LA-363, TC-AC-LA-364, TC-AC-LA-365, TC-AC-LA-366, TC-AC-LA-367 |
| TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | Modal Changelog: Sort, Pagination, dan Download | FE+BE | 62 | TC-AC-LA-368, TC-AC-LA-369, TC-AC-LA-370, TC-AC-LA-371, TC-AC-LA-372, TC-AC-LA-379, TC-AC-LA-380 |
| TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | Modal Changelog Setup Column: Screening, Ceklis, Reset, Guard, dan Cache | FE+BE | 59 | TC-AC-LA-373, TC-AC-LA-374, TC-AC-LA-375, TC-AC-LA-376, TC-AC-LA-377, TC-AC-LA-378 |
| TC-AC-LA-E2E-118-changelog-setup-column-drag-dan-pin | Modal Changelog Setup Column: Drag Urutan dan Pin Kolom Hideable | FE+BE | 33 | TC-AC-LA-489, TC-AC-LA-490 |
| TC-AC-LA-E2E-119-search-list-kolom-teks-dan-quantity | Search List: Kelas Teks Kolom Tampil dan Kolom Quantity | FE+BE | 13 | TC-AC-LA-281, TC-AC-LA-284 |
| TC-AC-LA-E2E-120-filter-list-multi-select-per-field | Filter List: Eksekusi Multi-select Delapan Field | FE+BE | 15 | TC-AC-LA-292 |
| TC-AC-LA-E2E-121-log-create-distributor-concurrent-user-station-storage-addon | Log Create oleh Distributor di Tiga Surface: Concurrent User, Station, Storage, dan Addon | FE+BE | 73 | TC-AC-LA-383, TC-AC-LA-385, TC-AC-LA-386 |
| TC-AC-LA-E2E-122-log-create-distributor-cost-dua-desimal-dan-waiting | Log Create oleh Distributor di Tiga Surface: Cost Dua Desimal, Pemisah Ribuan, dan Waiting for Approval | FE+BE | 66 | TC-AC-LA-512, TC-AC-LA-514, TC-AC-LA-387 |
| TC-AC-LA-E2E-123-log-create-principal-dan-event-created | Log Create oleh Principal: New Value Free dan Event Allocation created | FE+BE | 35 | TC-AC-LA-384, TC-AC-LA-518 |
| TC-AC-LA-E2E-124-log-edit-tiga-surface | Log Edit di Tiga Surface: Type dan Quantity, Pending ke Waiting for Approval, dan Pending ke Active | FE+BE | 59 | TC-AC-LA-388, TC-AC-LA-389, TC-AC-LA-390 |
| TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | Log Approve dan Reject: System Log, Activity Log, Allocation Log, dan Bukan Changelog | FE+BE | 56 | TC-AC-LA-393, TC-AC-LA-394, TC-AC-LA-411, TC-AC-LA-402, TC-AC-LA-403 |
| TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | Log Job Sistem: Timeout Auto-Cancel, Auto-Expire, dan Auto-Activate | FE+BE | 37 | TC-AC-LA-395, TC-AC-LA-396, TC-AC-LA-398, TC-AC-LA-406, TC-AC-LA-407 |
| TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | Log Job Sistem: Event Expired, Entri Allocation Log Tanpa PIC, dan Notifikasi Timeout | FE+BE | 49 | TC-AC-LA-408, TC-AC-LA-412, TC-AC-LA-525, TC-AC-LA-526, TC-AC-LA-437 |
| TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | Event Allocation Log Aksi Requester: Created, Edited, Canceled, Resubmitted, Station, Storage, dan App | FE+BE | 108 | TC-AC-LA-401, TC-AC-LA-404, TC-AC-LA-405, TC-AC-LA-409, TC-AC-LA-410, TC-AC-LA-519, TC-AC-LA-520 |
| TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | Integritas Log: Satu Baris per Field, Tidak Nyasar, Snapshot Immutability, Ringkasan Trigger, dan Rename Client | FE+BE | 98 | TC-AC-LA-415, TC-AC-LA-416, TC-AC-LA-417, TC-AC-LA-400, TC-AC-LA-418 |
| TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | Format Tanggal, Waktu, dan Zona Waktu per Surface Mengikuti General Settings | FE+BE | 28 | TC-AC-LA-420, TC-AC-LA-421, TC-AC-LA-422, TC-AC-LA-424, TC-AC-LA-382 |
| TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release | Konsumen Wallet: Reserve, Capture, Release, dan Transaction History | FE+BE | 66 | TC-AC-LA-427, TC-AC-LA-493, TC-AC-LA-494, TC-AC-LA-428 |
| TC-AC-LA-E2E-132-konsumen-subscription-detail-quota-aksi-ui | Konsumen Subscription Detail: License Quota setelah Approve dan Cancel Term | FE+BE | 20 | TC-AC-LA-425, TC-AC-LA-492 |
| TC-AC-LA-E2E-133-konsumen-subscription-detail-quota-setelah-job | Konsumen Subscription Detail: License Quota setelah Activation dan Expiry | FE+BE | 11 | TC-AC-LA-426, TC-AC-LA-491 |
| TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | Konsumen Lain: Approvals, Dropdown Client Baru, Asset Control App dan Station, serta Rename Client | FE+BE | 57 | TC-AC-LA-429, TC-AC-LA-430, TC-AC-LA-431, TC-AC-LA-528, TC-AC-LA-432 |
| TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | Notifikasi In-App: Waiting for Approval, License Allocated, Reject, Cancel, dan Unread Actionable | FE+BE | 35 | TC-AC-LA-433, TC-AC-LA-439, TC-AC-LA-435, TC-AC-LA-434, TC-AC-LA-436 |
| TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live | Konfigurasi Platform Dibaca Live: Product Price, Toggle Approval, dan Plan Berbeda | FE+BE | 84 | TC-AC-LA-441, TC-AC-LA-475, TC-AC-LA-442, TC-AC-LA-473 |
| TC-AC-LA-E2E-137-log-cancel-dan-resubmit-tiga-surface | Log Cancel dan Resubmit di Tiga Surface: Cancel Waiting for Approval, Resubmit sebagai Create Baru, dan Cancel Pending oleh Total Control | FE+BE | 52 | TC-AC-LA-391, TC-AC-LA-399, TC-AC-LA-392 |
| TC-AC-LA-E2E-138-approve-approver-entitas-berbeda-activity-log | Approve oleh Approver Entitas Berbeda dari Plan Owner: Satu Entri Activity Log di Dua Entitas dan Changelog Tidak Bertambah | FE+BE | 18 | TC-AC-LA-517 |
| TC-AC-LA-E2E-139-preservasi-state-list-tab-browser-baru-dan-sesi-baru | Preservasi State List Multi-Konteks: Tab Browser Baru dan Sesi Login Baru Memulai dari Default | FE+BE | 16 | TC-AC-LA-352 |

Ringkasan mode: FE+BE 139. Spec 095 dan 096 memakai nomor cadangan slice 4 (hasil pemisahan spec 092 dan 103 yang melewati 35 langkah); nomor 025, 026, 053, 054, 070, 071, 119, 120, 137, 138 juga terpakai sebagai cadangan, nomor 139 dipakai untuk TC-AC-LA-352 yang dipisah dari spec 113 (kelas multi-konteks), nomor yang tidak ada di tabel dibiarkan kosong (tanpa renumber).

Pembagian TC lintas spec (satu TC tetap dimiliki satu spec lewat `sourceTc`, C2): butir absence log TC-AC-LA-482 c, TC-AC-LA-479 c, dan klausa log TC-AC-LA-471 c diasersi di spec 094 (milik: 092, 095, 086). TC-AC-LA-419 seluruhnya di spec 094 dan TC-AC-LA-352 seluruhnya di spec 139.

## 2. Daftar TC hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Seluruh TC granular memiliki langkah UI atau dicakup spec FE+BE. TC kelas a (defense-in-depth) yang Expected-nya respons API tetap masuk spec FE+BE dengan pengecualian K-1; modul ini tidak punya TC backend.

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-AC-LA-1 | E2E | TC-AC-LA-E2E-001-screening-list-tab-current-history-dan-tooltip | FE+BE |
| TC-AC-LA-2 | E2E | TC-AC-LA-E2E-001-screening-list-tab-current-history-dan-tooltip | FE+BE |
| TC-AC-LA-3 | E2E | TC-AC-LA-E2E-001-screening-list-tab-current-history-dan-tooltip | FE+BE |
| TC-AC-LA-4 | E2E | TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status | FE+BE |
| TC-AC-LA-5 | E2E | TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status | FE+BE |
| TC-AC-LA-6 | E2E | TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status | FE+BE |
| TC-AC-LA-7 | E2E | TC-AC-LA-E2E-002-screening-baris-allocation-id-client-allocated-by-status | FE+BE |
| TC-AC-LA-8 | E2E | TC-AC-LA-E2E-008-row-action-menu-per-status | FE+BE |
| TC-AC-LA-9 | E2E | TC-AC-LA-E2E-008-row-action-menu-per-status | FE+BE |
| TC-AC-LA-10 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-11 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-12 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-13 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-14 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-15 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-16 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-17 | E2E | TC-AC-LA-E2E-005-state-list-loading-empty-filtered-dan-tab-awal | FE+BE |
| TC-AC-LA-18 | E2E | TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | FE+BE |
| TC-AC-LA-19 | E2E | TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | FE+BE |
| TC-AC-LA-20 | E2E | TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | FE+BE |
| TC-AC-LA-21 | E2E | TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | FE+BE |
| TC-AC-LA-22 | E2E | TC-AC-LA-E2E-003-ragam-baris-example-data-principal-distributor-station-app | FE+BE |
| TC-AC-LA-23 | E2E | TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | FE+BE |
| TC-AC-LA-24 | E2E | TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | FE+BE |
| TC-AC-LA-25 | E2E | TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | FE+BE |
| TC-AC-LA-26 | E2E | TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | FE+BE |
| TC-AC-LA-27 | E2E | TC-AC-LA-E2E-004-ragam-baris-example-data-cost-pending-expired-snapshot | FE+BE |
| TC-AC-LA-28 | E2E | TC-AC-LA-E2E-006-isi-tab-current-dan-history-serta-toolbar | FE+BE |
| TC-AC-LA-29 | E2E | TC-AC-LA-E2E-006-isi-tab-current-dan-history-serta-toolbar | FE+BE |
| TC-AC-LA-30 | E2E | TC-AC-LA-E2E-025-job-expiry-station-dan-storage-tetap-active | FE+BE |
| TC-AC-LA-31 | E2E | TC-AC-LA-E2E-026-perpindahan-baris-antar-tab-cancel-dan-resubmit | FE+BE |
| TC-AC-LA-32 | E2E | TC-AC-LA-E2E-026-perpindahan-baris-antar-tab-cancel-dan-resubmit | FE+BE |
| TC-AC-LA-33 | E2E | TC-AC-LA-E2E-008-row-action-menu-per-status | FE+BE |
| TC-AC-LA-34 | E2E | TC-AC-LA-E2E-006-isi-tab-current-dan-history-serta-toolbar | FE+BE |
| TC-AC-LA-35 | E2E | TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol | FE+BE |
| TC-AC-LA-36 | E2E | TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol | FE+BE |
| TC-AC-LA-37 | E2E | TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol | FE+BE |
| TC-AC-LA-38 | E2E | TC-AC-LA-E2E-007-state-per-tab-dan-independensi-kontrol | FE+BE |
| TC-AC-LA-39 | E2E | TC-AC-LA-E2E-009-screening-modal-allocation-log | FE+BE |
| TC-AC-LA-40 | E2E | TC-AC-LA-E2E-009-screening-modal-allocation-log | FE+BE |
| TC-AC-LA-41 | E2E | TC-AC-LA-E2E-009-screening-modal-allocation-log | FE+BE |
| TC-AC-LA-42 | E2E | TC-AC-LA-E2E-009-screening-modal-allocation-log | FE+BE |
| TC-AC-LA-43 | E2E | TC-AC-LA-E2E-009-screening-modal-allocation-log | FE+BE |
| TC-AC-LA-44 | E2E | TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog | FE+BE |
| TC-AC-LA-45 | E2E | TC-AC-LA-E2E-010-modal-allocation-log-loading-dan-immutability | FE+BE |
| TC-AC-LA-46 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-47 | E2E | TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi | FE+BE |
| TC-AC-LA-48 | E2E | TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi | FE+BE |
| TC-AC-LA-49 | E2E | TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi | FE+BE |
| TC-AC-LA-50 | E2E | TC-AC-LA-E2E-011-guided-tooltip-pertama-kali-dan-navigasi | FE+BE |
| TC-AC-LA-51 | E2E | TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain | FE+BE |
| TC-AC-LA-52 | E2E | TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain | FE+BE |
| TC-AC-LA-53 | E2E | TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain | FE+BE |
| TC-AC-LA-54 | E2E | TC-AC-LA-E2E-012-guided-tooltip-interupsi-keyboard-dan-halaman-lain | FE+BE |
| TC-AC-LA-55 | E2E | TC-AC-LA-E2E-013-role-matrix-entity-gate | FE+BE |
| TC-AC-LA-56 | E2E | TC-AC-LA-E2E-013-role-matrix-entity-gate | FE+BE |
| TC-AC-LA-57 | E2E | TC-AC-LA-E2E-013-role-matrix-entity-gate | FE+BE |
| TC-AC-LA-58 | E2E | TC-AC-LA-E2E-013-role-matrix-entity-gate | FE+BE |
| TC-AC-LA-59 | E2E | TC-AC-LA-E2E-013-role-matrix-entity-gate | FE+BE |
| TC-AC-LA-60 | E2E | TC-AC-LA-E2E-014-role-matrix-visibilitas-menu | FE+BE |
| TC-AC-LA-61 | E2E | TC-AC-LA-E2E-014-role-matrix-visibilitas-menu | FE+BE |
| TC-AC-LA-62 | E2E | TC-AC-LA-E2E-014-role-matrix-visibilitas-menu | FE+BE |
| TC-AC-LA-63 | E2E | TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog | FE+BE |
| TC-AC-LA-64 | E2E | TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog | FE+BE |
| TC-AC-LA-65 | E2E | TC-AC-LA-E2E-016-role-matrix-visibilitas-row-action-cancel-dan-edit | FE+BE |
| TC-AC-LA-66 | E2E | TC-AC-LA-E2E-016-role-matrix-visibilitas-row-action-cancel-dan-edit | FE+BE |
| TC-AC-LA-67 | E2E | TC-AC-LA-E2E-017-role-matrix-visibilitas-row-action-resubmit-dan-review | FE+BE |
| TC-AC-LA-68 | E2E | TC-AC-LA-E2E-017-role-matrix-visibilitas-row-action-resubmit-dan-review | FE+BE |
| TC-AC-LA-69 | E2E | TC-AC-LA-E2E-015-role-matrix-visibilitas-tombol-allocation-log-download-changelog | FE+BE |
| TC-AC-LA-70 | E2E | TC-AC-LA-E2E-018-role-matrix-negatif-access-level-read-only | FE+BE |
| TC-AC-LA-71 | E2E | TC-AC-LA-E2E-018-role-matrix-negatif-access-level-read-only | FE+BE |
| TC-AC-LA-72 | E2E | TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | FE+BE |
| TC-AC-LA-73 | E2E | TC-AC-LA-E2E-020-role-matrix-positif-edit-cancel-resubmit-capability-create-update | FE+BE |
| TC-AC-LA-74 | E2E | TC-AC-LA-E2E-020-role-matrix-positif-edit-cancel-resubmit-capability-create-update | FE+BE |
| TC-AC-LA-75 | E2E | TC-AC-LA-E2E-091-defense-peran-create-dan-update | FE+BE |
| TC-AC-LA-76 | E2E | TC-AC-LA-E2E-091-defense-peran-create-dan-update | FE+BE |
| TC-AC-LA-77 | E2E | TC-AC-LA-E2E-091-defense-peran-create-dan-update | FE+BE |
| TC-AC-LA-78 | E2E | TC-AC-LA-E2E-021-role-matrix-positif-cancel-pending-dan-approve-per-peran | FE+BE |
| TC-AC-LA-79 | E2E | TC-AC-LA-E2E-021-role-matrix-positif-cancel-pending-dan-approve-per-peran | FE+BE |
| TC-AC-LA-80 | E2E | TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | FE+BE |
| TC-AC-LA-81 | E2E | TC-AC-LA-E2E-021-role-matrix-positif-cancel-pending-dan-approve-per-peran | FE+BE |
| TC-AC-LA-82 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-83 | E2E | TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | FE+BE |
| TC-AC-LA-84 | E2E | TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | FE+BE |
| TC-AC-LA-85 | E2E | TC-AC-LA-E2E-019-role-matrix-positif-allocate-per-capability | FE+BE |
| TC-AC-LA-86 | E2E | TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | FE+BE |
| TC-AC-LA-87 | E2E | TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | FE+BE |
| TC-AC-LA-88 | E2E | TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | FE+BE |
| TC-AC-LA-89 | E2E | TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | FE+BE |
| TC-AC-LA-90 | E2E | TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | FE+BE |
| TC-AC-LA-91 | E2E | TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | FE+BE |
| TC-AC-LA-92 | E2E | TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | FE+BE |
| TC-AC-LA-93 | E2E | TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | FE+BE |
| TC-AC-LA-94 | E2E | TC-AC-LA-E2E-024-scope-group-manager-hierarki-dan-read-only-detail | FE+BE |
| TC-AC-LA-95 | E2E | TC-AC-LA-E2E-024-scope-group-manager-hierarki-dan-read-only-detail | FE+BE |
| TC-AC-LA-96 | E2E | TC-AC-LA-E2E-023-scope-group-role-zero-access-dan-group-abc | FE+BE |
| TC-AC-LA-97 | E2E | TC-AC-LA-E2E-022-scope-data-read-write-distributor-partner-principal | FE+BE |
| TC-AC-LA-98 | E2E | TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability | FE+BE |
| TC-AC-LA-99 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-100 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-101 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-102 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-103 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-104 | E2E | TC-AC-LA-E2E-028-screening-payment-distributor-dan-partner | FE+BE |
| TC-AC-LA-105 | E2E | TC-AC-LA-E2E-028-screening-payment-distributor-dan-partner | FE+BE |
| TC-AC-LA-106 | E2E | TC-AC-LA-E2E-028-screening-payment-distributor-dan-partner | FE+BE |
| TC-AC-LA-107 | E2E | TC-AC-LA-E2E-027-screening-form-allocate-per-mode | FE+BE |
| TC-AC-LA-108 | E2E | TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | FE+BE |
| TC-AC-LA-109 | E2E | TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | FE+BE |
| TC-AC-LA-110 | E2E | TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | FE+BE |
| TC-AC-LA-111 | E2E | TC-AC-LA-E2E-030-validasi-additional-quantity | FE+BE |
| TC-AC-LA-112 | E2E | TC-AC-LA-E2E-030-validasi-additional-quantity | FE+BE |
| TC-AC-LA-113 | E2E | TC-AC-LA-E2E-031-additional-quantity-batas-valid-submit-sukses | FE+BE |
| TC-AC-LA-114 | E2E | TC-AC-LA-E2E-030-validasi-additional-quantity | FE+BE |
| TC-AC-LA-115 | E2E | TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | FE+BE |
| TC-AC-LA-116 | E2E | TC-AC-LA-E2E-030-validasi-additional-quantity | FE+BE |
| TC-AC-LA-117 | E2E | TC-AC-LA-E2E-032-validasi-pay-from-dan-saldo-partner | FE+BE |
| TC-AC-LA-118 | E2E | TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | FE+BE |
| TC-AC-LA-119 | E2E | TC-AC-LA-E2E-029-validasi-field-wajib-dan-pesan-inline | FE+BE |
| TC-AC-LA-120 | E2E | TC-AC-LA-E2E-034-dropdown-client | FE+BE |
| TC-AC-LA-121 | E2E | TC-AC-LA-E2E-034-dropdown-client | FE+BE |
| TC-AC-LA-122 | E2E | TC-AC-LA-E2E-034-dropdown-client | FE+BE |
| TC-AC-LA-123 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-124 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-125 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-126 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-127 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-128 | E2E | TC-AC-LA-E2E-035-opsi-target-term-eligible | FE+BE |
| TC-AC-LA-129 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-130 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-131 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-132 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-133 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-134 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-135 | E2E | TC-AC-LA-E2E-036-opsi-type-per-target-dan-current-quota | FE+BE |
| TC-AC-LA-136 | E2E | TC-AC-LA-E2E-037-reset-berantai-ganti-client-target-type | FE+BE |
| TC-AC-LA-137 | E2E | TC-AC-LA-E2E-037-reset-berantai-ganti-client-target-type | FE+BE |
| TC-AC-LA-138 | E2E | TC-AC-LA-E2E-037-reset-berantai-ganti-client-target-type | FE+BE |
| TC-AC-LA-139 | E2E | TC-AC-LA-E2E-081-konkurensi-form-allocate-target-submit-serentak | FE+BE |
| TC-AC-LA-140 | E2E | TC-AC-LA-E2E-038-preview-cost-concurrent-user-prorata | FE+BE |
| TC-AC-LA-141 | E2E | TC-AC-LA-E2E-053-preview-cost-hari-terakhir-dan-zona-waktu-plan-owner | FE+BE |
| TC-AC-LA-142 | E2E | TC-AC-LA-E2E-038-preview-cost-concurrent-user-prorata | FE+BE |
| TC-AC-LA-143 | E2E | TC-AC-LA-E2E-040-cost-terkunci-pembulatan-dan-cost-nol | FE+BE |
| TC-AC-LA-144 | E2E | TC-AC-LA-E2E-032-validasi-pay-from-dan-saldo-partner | FE+BE |
| TC-AC-LA-145 | E2E | TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | FE+BE |
| TC-AC-LA-146 | E2E | TC-AC-LA-E2E-033-validasi-harga-belum-diset-dan-batas-saldo-distributor | FE+BE |
| TC-AC-LA-147 | E2E | TC-AC-LA-E2E-041-skeleton-preview-pay-from-dan-cross-distributor | FE+BE |
| TC-AC-LA-148 | E2E | TC-AC-LA-E2E-039-preview-cost-per-jenis-license | FE+BE |
| TC-AC-LA-149 | E2E | TC-AC-LA-E2E-039-preview-cost-per-jenis-license | FE+BE |
| TC-AC-LA-150 | E2E | TC-AC-LA-E2E-039-preview-cost-per-jenis-license | FE+BE |
| TC-AC-LA-151 | E2E | TC-AC-LA-E2E-040-cost-terkunci-pembulatan-dan-cost-nol | FE+BE |
| TC-AC-LA-152 | E2E | TC-AC-LA-E2E-038-preview-cost-concurrent-user-prorata | FE+BE |
| TC-AC-LA-153 | E2E | TC-AC-LA-E2E-041-skeleton-preview-pay-from-dan-cross-distributor | FE+BE |
| TC-AC-LA-154 | E2E | TC-AC-LA-E2E-053-preview-cost-hari-terakhir-dan-zona-waktu-plan-owner | FE+BE |
| TC-AC-LA-155 | E2E | TC-AC-LA-E2E-042-submit-concurrent-user-asset-log-source-addon | FE+BE |
| TC-AC-LA-156 | E2E | TC-AC-LA-E2E-042-submit-concurrent-user-asset-log-source-addon | FE+BE |
| TC-AC-LA-157 | E2E | TC-AC-LA-E2E-042-submit-concurrent-user-asset-log-source-addon | FE+BE |
| TC-AC-LA-158 | E2E | TC-AC-LA-E2E-054-submit-addon-fams-lima-jenis | FE+BE |
| TC-AC-LA-159 | E2E | TC-AC-LA-E2E-043-submit-asset-control-app-station-storage | FE+BE |
| TC-AC-LA-160 | E2E | TC-AC-LA-E2E-043-submit-asset-control-app-station-storage | FE+BE |
| TC-AC-LA-161 | E2E | TC-AC-LA-E2E-043-submit-asset-control-app-station-storage | FE+BE |
| TC-AC-LA-162 | E2E | TC-AC-LA-E2E-044-submit-status-awal-toggle-approval-requester-distributor | FE+BE |
| TC-AC-LA-163 | E2E | TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner | FE+BE |
| TC-AC-LA-164 | E2E | TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner | FE+BE |
| TC-AC-LA-165 | E2E | TC-AC-LA-E2E-044-submit-status-awal-toggle-approval-requester-distributor | FE+BE |
| TC-AC-LA-166 | E2E | TC-AC-LA-E2E-044-submit-status-awal-toggle-approval-requester-distributor | FE+BE |
| TC-AC-LA-167 | E2E | TC-AC-LA-E2E-046-submit-properti-record-end-date-successor-dan-kantong-distributor | FE+BE |
| TC-AC-LA-168 | E2E | TC-AC-LA-E2E-047-submit-allocation-id-top-up-dan-pay-from-partner | FE+BE |
| TC-AC-LA-169 | E2E | TC-AC-LA-E2E-047-submit-allocation-id-top-up-dan-pay-from-partner | FE+BE |
| TC-AC-LA-170 | E2E | TC-AC-LA-E2E-046-submit-properti-record-end-date-successor-dan-kantong-distributor | FE+BE |
| TC-AC-LA-171 | E2E | TC-AC-LA-E2E-047-submit-allocation-id-top-up-dan-pay-from-partner | FE+BE |
| TC-AC-LA-172 | E2E | TC-AC-LA-E2E-046-submit-properti-record-end-date-successor-dan-kantong-distributor | FE+BE |
| TC-AC-LA-173 | E2E | TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner | FE+BE |
| TC-AC-LA-174 | E2E | TC-AC-LA-E2E-048-notifikasi-submit-plan-owner-dan-approver | FE+BE |
| TC-AC-LA-175 | E2E | TC-AC-LA-E2E-048-notifikasi-submit-plan-owner-dan-approver | FE+BE |
| TC-AC-LA-176 | E2E | TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | FE+BE |
| TC-AC-LA-177 | E2E | TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | FE+BE |
| TC-AC-LA-178 | E2E | TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | FE+BE |
| TC-AC-LA-179 | E2E | TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | FE+BE |
| TC-AC-LA-180 | E2E | TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field | FE+BE |
| TC-AC-LA-181 | E2E | TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field | FE+BE |
| TC-AC-LA-182 | E2E | TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state | FE+BE |
| TC-AC-LA-183 | E2E | TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field | FE+BE |
| TC-AC-LA-184 | E2E | TC-AC-LA-E2E-051-dirty-guard-navigasi-refresh-dan-clear-field | FE+BE |
| TC-AC-LA-185 | E2E | TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state | FE+BE |
| TC-AC-LA-186 | E2E | TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state | FE+BE |
| TC-AC-LA-187 | E2E | TC-AC-LA-E2E-052-form-resubmit-prefilled-stay-on-form-dan-saving-state | FE+BE |
| TC-AC-LA-188 | E2E | TC-AC-LA-E2E-055-edit-screening-save-disabled-dan-clear-field | FE+BE |
| TC-AC-LA-189 | E2E | TC-AC-LA-E2E-055-edit-screening-save-disabled-dan-clear-field | FE+BE |
| TC-AC-LA-190 | E2E | TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | FE+BE |
| TC-AC-LA-191 | E2E | TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | FE+BE |
| TC-AC-LA-192 | E2E | TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | FE+BE |
| TC-AC-LA-193 | E2E | TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | FE+BE |
| TC-AC-LA-194 | E2E | TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target | FE+BE |
| TC-AC-LA-195 | E2E | TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target | FE+BE |
| TC-AC-LA-196 | E2E | TC-AC-LA-E2E-059-edit-blokir-saldo-dan-app-kedua | FE+BE |
| TC-AC-LA-197 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-198 | E2E | TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal | FE+BE |
| TC-AC-LA-199 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-200 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-201 | E2E | TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | FE+BE |
| TC-AC-LA-202 | E2E | TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | FE+BE |
| TC-AC-LA-203 | E2E | TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | FE+BE |
| TC-AC-LA-204 | E2E | TC-AC-LA-E2E-059-edit-blokir-saldo-dan-app-kedua | FE+BE |
| TC-AC-LA-205 | E2E | TC-AC-LA-E2E-070-edit-validasi-field-form | FE+BE |
| TC-AC-LA-206 | E2E | TC-AC-LA-E2E-070-edit-validasi-field-form | FE+BE |
| TC-AC-LA-207 | E2E | TC-AC-LA-E2E-070-edit-validasi-field-form | FE+BE |
| TC-AC-LA-208 | E2E | TC-AC-LA-E2E-070-edit-validasi-field-form | FE+BE |
| TC-AC-LA-209 | E2E | TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target | FE+BE |
| TC-AC-LA-210 | E2E | TC-AC-LA-E2E-055-edit-screening-save-disabled-dan-clear-field | FE+BE |
| TC-AC-LA-211 | E2E | TC-AC-LA-E2E-058-edit-record-pending | FE+BE |
| TC-AC-LA-212 | E2E | TC-AC-LA-E2E-058-edit-record-pending | FE+BE |
| TC-AC-LA-213 | E2E | TC-AC-LA-E2E-071-edit-record-pending-toggle-off | FE+BE |
| TC-AC-LA-214 | E2E | TC-AC-LA-E2E-058-edit-record-pending | FE+BE |
| TC-AC-LA-215 | E2E | TC-AC-LA-E2E-071-edit-record-pending-toggle-off | FE+BE |
| TC-AC-LA-216 | E2E | TC-AC-LA-E2E-071-edit-record-pending-toggle-off | FE+BE |
| TC-AC-LA-217 | E2E | TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | FE+BE |
| TC-AC-LA-218 | E2E | TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | FE+BE |
| TC-AC-LA-219 | E2E | TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | FE+BE |
| TC-AC-LA-220 | E2E | TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | FE+BE |
| TC-AC-LA-221 | E2E | TC-AC-LA-E2E-061-cancel-pending-total-control-dan-default-user | FE+BE |
| TC-AC-LA-222 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-223 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-224 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-225 | E2E | TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | FE+BE |
| TC-AC-LA-226 | E2E | TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal | FE+BE |
| TC-AC-LA-227 | E2E | TC-AC-LA-E2E-061-cancel-pending-total-control-dan-default-user | FE+BE |
| TC-AC-LA-228 | E2E | TC-AC-LA-E2E-060-cancel-dialog-dan-pembatalan-requester | FE+BE |
| TC-AC-LA-229 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-230 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-231 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-232 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-233 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-234 | E2E | TC-AC-LA-E2E-093-defense-edit-cancel-resubmit-milik-orang-lain-dan-status-final | FE+BE |
| TC-AC-LA-235 | E2E | TC-AC-LA-E2E-082-konkurensi-edit-cancel-resubmit | FE+BE |
| TC-AC-LA-236 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-237 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-238 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-239 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-240 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-241 | E2E | TC-AC-LA-E2E-064-approve-screening-detail-approval-dan-hasil-active | FE+BE |
| TC-AC-LA-242 | E2E | TC-AC-LA-E2E-064-approve-screening-detail-approval-dan-hasil-active | FE+BE |
| TC-AC-LA-243 | E2E | TC-AC-LA-E2E-064-approve-screening-detail-approval-dan-hasil-active | FE+BE |
| TC-AC-LA-244 | E2E | TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage | FE+BE |
| TC-AC-LA-245 | E2E | TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage | FE+BE |
| TC-AC-LA-246 | E2E | TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage | FE+BE |
| TC-AC-LA-247 | E2E | TC-AC-LA-E2E-065-approve-snapshot-harga-app-station-storage | FE+BE |
| TC-AC-LA-248 | E2E | TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated | FE+BE |
| TC-AC-LA-249 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-250 | E2E | TC-AC-LA-E2E-069-approve-blokir-gate-target-dan-app-ganda | FE+BE |
| TC-AC-LA-251 | E2E | TC-AC-LA-E2E-069-approve-blokir-gate-target-dan-app-ganda | FE+BE |
| TC-AC-LA-252 | E2E | TC-AC-LA-E2E-069-approve-blokir-gate-target-dan-app-ganda | FE+BE |
| TC-AC-LA-253 | E2E | TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver | FE+BE |
| TC-AC-LA-254 | E2E | TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver | FE+BE |
| TC-AC-LA-255 | E2E | TC-AC-LA-E2E-083-konkurensi-approve-reject | FE+BE |
| TC-AC-LA-256 | E2E | TC-AC-LA-E2E-083-konkurensi-approve-reject | FE+BE |
| TC-AC-LA-257 | E2E | TC-AC-LA-E2E-083-konkurensi-approve-reject | FE+BE |
| TC-AC-LA-258 | E2E | TC-AC-LA-E2E-083-konkurensi-approve-reject | FE+BE |
| TC-AC-LA-259 | E2E | TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated | FE+BE |
| TC-AC-LA-260 | E2E | TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated | FE+BE |
| TC-AC-LA-261 | E2E | TC-AC-LA-E2E-068-approve-reject-oleh-additional-approver-dan-principal | FE+BE |
| TC-AC-LA-262 | E2E | TC-AC-LA-E2E-066-approve-reject-dari-approvals-dan-last-updated | FE+BE |
| TC-AC-LA-263 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-264 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-265 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-266 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-267 | E2E | TC-AC-LA-E2E-074-job-activation-transition | FE+BE |
| TC-AC-LA-268 | E2E | TC-AC-LA-E2E-074-job-activation-transition | FE+BE |
| TC-AC-LA-269 | E2E | TC-AC-LA-E2E-075-job-expiry-transition | FE+BE |
| TC-AC-LA-270 | E2E | TC-AC-LA-E2E-075-job-expiry-transition | FE+BE |
| TC-AC-LA-271 | E2E | TC-AC-LA-E2E-075-job-expiry-transition | FE+BE |
| TC-AC-LA-272 | E2E | TC-AC-LA-E2E-075-job-expiry-transition | FE+BE |
| TC-AC-LA-273 | E2E | TC-AC-LA-E2E-075-job-expiry-transition | FE+BE |
| TC-AC-LA-274 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-275 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-276 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-277 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-278 | E2E | TC-AC-LA-E2E-076-job-pada-client-suspended | FE+BE |
| TC-AC-LA-279 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-280 | E2E | TC-AC-LA-E2E-097-search-list-teks-dan-kolom-status-quantity | FE+BE |
| TC-AC-LA-281 | E2E | TC-AC-LA-E2E-119-search-list-kolom-teks-dan-quantity | FE+BE |
| TC-AC-LA-282 | E2E | TC-AC-LA-E2E-097-search-list-teks-dan-kolom-status-quantity | FE+BE |
| TC-AC-LA-283 | E2E | TC-AC-LA-E2E-097-search-list-teks-dan-kolom-status-quantity | FE+BE |
| TC-AC-LA-284 | E2E | TC-AC-LA-E2E-119-search-list-kolom-teks-dan-quantity | FE+BE |
| TC-AC-LA-285 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-286 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-287 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-288 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-289 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-290 | E2E | TC-AC-LA-E2E-098-search-list-kolom-opsional-guard-dan-tab-history | FE+BE |
| TC-AC-LA-291 | E2E | TC-AC-LA-E2E-099-filter-list-screening-dan-opsi | FE+BE |
| TC-AC-LA-292 | E2E | TC-AC-LA-E2E-120-filter-list-multi-select-per-field | FE+BE |
| TC-AC-LA-293 | E2E | TC-AC-LA-E2E-099-filter-list-screening-dan-opsi | FE+BE |
| TC-AC-LA-294 | E2E | TC-AC-LA-E2E-099-filter-list-screening-dan-opsi | FE+BE |
| TC-AC-LA-295 | E2E | TC-AC-LA-E2E-099-filter-list-screening-dan-opsi | FE+BE |
| TC-AC-LA-296 | E2E | TC-AC-LA-E2E-100-filter-list-eksekusi-tanggal-dan-logika | FE+BE |
| TC-AC-LA-297 | E2E | TC-AC-LA-E2E-100-filter-list-eksekusi-tanggal-dan-logika | FE+BE |
| TC-AC-LA-298 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-299 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-300 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-301 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-302 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-303 | E2E | TC-AC-LA-E2E-101-filter-list-chip-dropdown-clear-dan-tab-history | FE+BE |
| TC-AC-LA-304 | E2E | TC-AC-LA-E2E-102-sort-list-siklus-dan-alfabetis | FE+BE |
| TC-AC-LA-305 | E2E | TC-AC-LA-E2E-102-sort-list-siklus-dan-alfabetis | FE+BE |
| TC-AC-LA-306 | E2E | TC-AC-LA-E2E-102-sort-list-siklus-dan-alfabetis | FE+BE |
| TC-AC-LA-307 | E2E | TC-AC-LA-E2E-103-sort-list-numerik-allocated-by-payment-dan-default | FE+BE |
| TC-AC-LA-308 | E2E | TC-AC-LA-E2E-103-sort-list-numerik-allocated-by-payment-dan-default | FE+BE |
| TC-AC-LA-309 | E2E | TC-AC-LA-E2E-096-sort-list-payment-pindah-kolom-dan-default | FE+BE |
| TC-AC-LA-310 | E2E | TC-AC-LA-E2E-096-sort-list-payment-pindah-kolom-dan-default | FE+BE |
| TC-AC-LA-311 | E2E | TC-AC-LA-E2E-096-sort-list-payment-pindah-kolom-dan-default | FE+BE |
| TC-AC-LA-312 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-313 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-314 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-315 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-316 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-317 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-318 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-319 | E2E | TC-AC-LA-E2E-104-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-AC-LA-320 | E2E | TC-AC-LA-E2E-105-setup-column-list-screening-dan-ceklis | FE+BE |
| TC-AC-LA-321 | E2E | TC-AC-LA-E2E-105-setup-column-list-screening-dan-ceklis | FE+BE |
| TC-AC-LA-322 | E2E | TC-AC-LA-E2E-105-setup-column-list-screening-dan-ceklis | FE+BE |
| TC-AC-LA-323 | E2E | TC-AC-LA-E2E-106-setup-column-list-drag-dan-pin | FE+BE |
| TC-AC-LA-324 | E2E | TC-AC-LA-E2E-106-setup-column-list-drag-dan-pin | FE+BE |
| TC-AC-LA-325 | E2E | TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard | FE+BE |
| TC-AC-LA-326 | E2E | TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard | FE+BE |
| TC-AC-LA-327 | E2E | TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard | FE+BE |
| TC-AC-LA-328 | E2E | TC-AC-LA-E2E-107-setup-column-list-curated-reset-dan-discard | FE+BE |
| TC-AC-LA-329 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-330 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-331 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-332 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-333 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-334 | E2E | TC-AC-LA-E2E-108-setup-column-list-guard-dan-independensi | FE+BE |
| TC-AC-LA-335 | E2E | TC-AC-LA-E2E-109-pagination-list | FE+BE |
| TC-AC-LA-336 | E2E | TC-AC-LA-E2E-109-pagination-list | FE+BE |
| TC-AC-LA-337 | E2E | TC-AC-LA-E2E-109-pagination-list | FE+BE |
| TC-AC-LA-338 | E2E | TC-AC-LA-E2E-109-pagination-list | FE+BE |
| TC-AC-LA-339 | E2E | TC-AC-LA-E2E-109-pagination-list | FE+BE |
| TC-AC-LA-340 | E2E | TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom | FE+BE |
| TC-AC-LA-341 | E2E | TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom | FE+BE |
| TC-AC-LA-342 | E2E | TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom | FE+BE |
| TC-AC-LA-343 | E2E | TC-AC-LA-E2E-110-download-list-baris-nama-berkas-dan-kolom | FE+BE |
| TC-AC-LA-344 | E2E | TC-AC-LA-E2E-111-download-list-isi-berkas-binary | FE+BE |
| TC-AC-LA-345 | E2E | TC-AC-LA-E2E-111-download-list-isi-berkas-binary | FE+BE |
| TC-AC-LA-346 | E2E | TC-AC-LA-E2E-111-download-list-isi-berkas-binary | FE+BE |
| TC-AC-LA-347 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-348 | E2E | TC-AC-LA-E2E-112-download-list-volume-lebih-5000-baris | FE+BE |
| TC-AC-LA-349 | E2E | TC-AC-LA-E2E-113-preservasi-state-list | FE+BE |
| TC-AC-LA-350 | E2E | TC-AC-LA-E2E-113-preservasi-state-list | FE+BE |
| TC-AC-LA-351 | E2E | TC-AC-LA-E2E-113-preservasi-state-list | FE+BE |
| TC-AC-LA-352 | E2E | TC-AC-LA-E2E-139-preservasi-state-list-tab-browser-baru-dan-sesi-baru | FE+BE |
| TC-AC-LA-353 | E2E | TC-AC-LA-E2E-113-preservasi-state-list | FE+BE |
| TC-AC-LA-354 | E2E | TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-LA-355 | E2E | TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-LA-356 | E2E | TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-LA-357 | E2E | TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-LA-358 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-359 | E2E | TC-AC-LA-E2E-114-changelog-screening-state-dan-format-sel | FE+BE |
| TC-AC-LA-360 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-361 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-362 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-363 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-364 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-365 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-366 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-367 | E2E | TC-AC-LA-E2E-115-changelog-search-dan-filter | FE+BE |
| TC-AC-LA-368 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-369 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-370 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-371 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-372 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-373 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-374 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-375 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-376 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-377 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-378 | E2E | TC-AC-LA-E2E-117-changelog-setup-column-screening-dan-ceklis | FE+BE |
| TC-AC-LA-379 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-380 | E2E | TC-AC-LA-E2E-116-changelog-sort-pagination-dan-download | FE+BE |
| TC-AC-LA-381 | E2E | TC-AC-LA-E2E-085-resilience-baca-list-log-dan-download | FE+BE |
| TC-AC-LA-382 | E2E | TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | FE+BE |
| TC-AC-LA-383 | E2E | TC-AC-LA-E2E-121-log-create-distributor-concurrent-user-station-storage-addon | FE+BE |
| TC-AC-LA-384 | E2E | TC-AC-LA-E2E-123-log-create-principal-dan-event-created | FE+BE |
| TC-AC-LA-385 | E2E | TC-AC-LA-E2E-121-log-create-distributor-concurrent-user-station-storage-addon | FE+BE |
| TC-AC-LA-386 | E2E | TC-AC-LA-E2E-121-log-create-distributor-concurrent-user-station-storage-addon | FE+BE |
| TC-AC-LA-387 | E2E | TC-AC-LA-E2E-122-log-create-distributor-cost-dua-desimal-dan-waiting | FE+BE |
| TC-AC-LA-388 | E2E | TC-AC-LA-E2E-124-log-edit-tiga-surface | FE+BE |
| TC-AC-LA-389 | E2E | TC-AC-LA-E2E-124-log-edit-tiga-surface | FE+BE |
| TC-AC-LA-390 | E2E | TC-AC-LA-E2E-124-log-edit-tiga-surface | FE+BE |
| TC-AC-LA-391 | E2E | TC-AC-LA-E2E-137-log-cancel-dan-resubmit-tiga-surface | FE+BE |
| TC-AC-LA-392 | E2E | TC-AC-LA-E2E-137-log-cancel-dan-resubmit-tiga-surface | FE+BE |
| TC-AC-LA-393 | E2E | TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | FE+BE |
| TC-AC-LA-394 | E2E | TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | FE+BE |
| TC-AC-LA-395 | E2E | TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | FE+BE |
| TC-AC-LA-396 | E2E | TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | FE+BE |
| TC-AC-LA-397 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-398 | E2E | TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | FE+BE |
| TC-AC-LA-399 | E2E | TC-AC-LA-E2E-137-log-cancel-dan-resubmit-tiga-surface | FE+BE |
| TC-AC-LA-400 | E2E | TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | FE+BE |
| TC-AC-LA-401 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-402 | E2E | TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | FE+BE |
| TC-AC-LA-403 | E2E | TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | FE+BE |
| TC-AC-LA-404 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-405 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-406 | E2E | TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | FE+BE |
| TC-AC-LA-407 | E2E | TC-AC-LA-E2E-126-log-job-sistem-timeout-activation-expiry | FE+BE |
| TC-AC-LA-408 | E2E | TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | FE+BE |
| TC-AC-LA-409 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-410 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-411 | E2E | TC-AC-LA-E2E-125-log-approve-reject-dan-event-keputusan | FE+BE |
| TC-AC-LA-412 | E2E | TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | FE+BE |
| TC-AC-LA-413 | E2E | TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal | FE+BE |
| TC-AC-LA-414 | E2E | TC-AC-LA-E2E-010-modal-allocation-log-loading-dan-immutability | FE+BE |
| TC-AC-LA-415 | E2E | TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | FE+BE |
| TC-AC-LA-416 | E2E | TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | FE+BE |
| TC-AC-LA-417 | E2E | TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | FE+BE |
| TC-AC-LA-418 | E2E | TC-AC-LA-E2E-129-integritas-log-dan-ringkasan-trigger | FE+BE |
| TC-AC-LA-419 | E2E | TC-AC-LA-E2E-094-absence-log-no-op-dan-pembukaan-modal | FE+BE |
| TC-AC-LA-420 | E2E | TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | FE+BE |
| TC-AC-LA-421 | E2E | TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | FE+BE |
| TC-AC-LA-422 | E2E | TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | FE+BE |
| TC-AC-LA-423 | E2E | TC-AC-LA-E2E-111-download-list-isi-berkas-binary | FE+BE |
| TC-AC-LA-424 | E2E | TC-AC-LA-E2E-130-format-tanggal-waktu-dan-zona-waktu | FE+BE |
| TC-AC-LA-425 | E2E | TC-AC-LA-E2E-132-konsumen-subscription-detail-quota-aksi-ui | FE+BE |
| TC-AC-LA-426 | E2E | TC-AC-LA-E2E-133-konsumen-subscription-detail-quota-setelah-job | FE+BE |
| TC-AC-LA-427 | E2E | TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release | FE+BE |
| TC-AC-LA-428 | E2E | TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release | FE+BE |
| TC-AC-LA-429 | E2E | TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | FE+BE |
| TC-AC-LA-430 | E2E | TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | FE+BE |
| TC-AC-LA-431 | E2E | TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | FE+BE |
| TC-AC-LA-432 | E2E | TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | FE+BE |
| TC-AC-LA-433 | E2E | TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | FE+BE |
| TC-AC-LA-434 | E2E | TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | FE+BE |
| TC-AC-LA-435 | E2E | TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | FE+BE |
| TC-AC-LA-436 | E2E | TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | FE+BE |
| TC-AC-LA-437 | E2E | TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | FE+BE |
| TC-AC-LA-438 | E2E | TC-AC-LA-E2E-049-notifikasi-edit-pending | FE+BE |
| TC-AC-LA-439 | E2E | TC-AC-LA-E2E-135-notifikasi-keputusan-dan-cancel | FE+BE |
| TC-AC-LA-440 | E2E | TC-AC-LA-E2E-084-konkurensi-notifikasi-approver | FE+BE |
| TC-AC-LA-441 | E2E | TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live | FE+BE |
| TC-AC-LA-442 | E2E | TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live | FE+BE |
| TC-AC-LA-443 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-444 | E2E | TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability | FE+BE |
| TC-AC-LA-445 | E2E | TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability | FE+BE |
| TC-AC-LA-446 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-447 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-448 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-449 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-450 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-451 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-452 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-453 | E2E | TC-AC-LA-E2E-095-defense-approver-dicabut-dan-group-manager-luar-scope | FE+BE |
| TC-AC-LA-454 | E2E | TC-AC-LA-E2E-095-defense-approver-dicabut-dan-group-manager-luar-scope | FE+BE |
| TC-AC-LA-455 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-456 | E2E | TC-AC-LA-E2E-087-defense-validasi-submit-request-langsung-distributor | FE+BE |
| TC-AC-LA-457 | E2E | TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | FE+BE |
| TC-AC-LA-458 | E2E | TC-AC-LA-E2E-089-defense-akses-ditolak-zero-access-dan-tanpa-capability | FE+BE |
| TC-AC-LA-459 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-460 | E2E | TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver | FE+BE |
| TC-AC-LA-461 | E2E | TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate | FE+BE |
| TC-AC-LA-462 | E2E | TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate | FE+BE |
| TC-AC-LA-463 | E2E | TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate | FE+BE |
| TC-AC-LA-464 | E2E | TC-AC-LA-E2E-080-konkurensi-form-allocate-client-target-dan-gate | FE+BE |
| TC-AC-LA-465 | E2E | TC-AC-LA-E2E-073-job-timeout-vs-approve | FE+BE |
| TC-AC-LA-466 | E2E | TC-AC-LA-E2E-081-konkurensi-form-allocate-target-submit-serentak | FE+BE |
| TC-AC-LA-467 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-468 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-469 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-470 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-471 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-472 | E2E | TC-AC-LA-E2E-086-resilience-aksi-tulis | FE+BE |
| TC-AC-LA-473 | E2E | TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live | FE+BE |
| TC-AC-LA-474 | E2E | TC-AC-LA-E2E-081-konkurensi-form-allocate-target-submit-serentak | FE+BE |
| TC-AC-LA-475 | E2E | TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live | FE+BE |
| TC-AC-LA-476 | E2E | TC-AC-LA-E2E-067-approve-reject-oleh-group-manager | FE+BE |
| TC-AC-LA-477 | E2E | TC-AC-LA-E2E-067-approve-reject-oleh-group-manager | FE+BE |
| TC-AC-LA-478 | E2E | TC-AC-LA-E2E-067-approve-reject-oleh-group-manager | FE+BE |
| TC-AC-LA-479 | E2E | TC-AC-LA-E2E-095-defense-approver-dicabut-dan-group-manager-luar-scope | FE+BE |
| TC-AC-LA-480 | E2E | TC-AC-LA-E2E-068-approve-reject-oleh-additional-approver-dan-principal | FE+BE |
| TC-AC-LA-481 | E2E | TC-AC-LA-E2E-020-role-matrix-positif-edit-cancel-resubmit-capability-create-update | FE+BE |
| TC-AC-LA-482 | E2E | TC-AC-LA-E2E-092-defense-approve-reject-oleh-bukan-approver | FE+BE |
| TC-AC-LA-483 | E2E | TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | FE+BE |
| TC-AC-LA-484 | E2E | TC-AC-LA-E2E-072-job-timeout-auto-cancel-dan-warning-h24 | FE+BE |
| TC-AC-LA-485 | E2E | TC-AC-LA-E2E-073-job-timeout-vs-approve | FE+BE |
| TC-AC-LA-486 | E2E | TC-AC-LA-E2E-056-edit-dirty-guard-dan-penyesuaian-type-target | FE+BE |
| TC-AC-LA-487 | E2E | TC-AC-LA-E2E-057-edit-waiting-for-approval-sukses | FE+BE |
| TC-AC-LA-488 | E2E | TC-AC-LA-E2E-062-resubmit-alur-utama | FE+BE |
| TC-AC-LA-489 | E2E | TC-AC-LA-E2E-118-changelog-setup-column-drag-dan-pin | FE+BE |
| TC-AC-LA-490 | E2E | TC-AC-LA-E2E-118-changelog-setup-column-drag-dan-pin | FE+BE |
| TC-AC-LA-491 | E2E | TC-AC-LA-E2E-133-konsumen-subscription-detail-quota-setelah-job | FE+BE |
| TC-AC-LA-492 | E2E | TC-AC-LA-E2E-132-konsumen-subscription-detail-quota-aksi-ui | FE+BE |
| TC-AC-LA-493 | E2E | TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release | FE+BE |
| TC-AC-LA-494 | E2E | TC-AC-LA-E2E-131-konsumen-wallet-reserve-capture-release | FE+BE |
| TC-AC-LA-495 | E2E | TC-AC-LA-E2E-049-notifikasi-edit-pending | FE+BE |
| TC-AC-LA-496 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-497 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-498 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-499 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-500 | E2E | TC-AC-LA-E2E-078-tenant-entitas-pengalokasi-suspended | FE+BE |
| TC-AC-LA-501 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-502 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-503 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-504 | E2E | TC-AC-LA-E2E-079-tenant-client-suspended-expired-sebagai-penerima | FE+BE |
| TC-AC-LA-505 | E2E | TC-AC-LA-E2E-048-notifikasi-submit-plan-owner-dan-approver | FE+BE |
| TC-AC-LA-506 | E2E | TC-AC-LA-E2E-041-skeleton-preview-pay-from-dan-cross-distributor | FE+BE |
| TC-AC-LA-507 | E2E | TC-AC-LA-E2E-024-scope-group-manager-hierarki-dan-read-only-detail | FE+BE |
| TC-AC-LA-508 | E2E | TC-AC-LA-E2E-088-defense-validasi-request-langsung-quantity-saldo-edit-dan-markup | FE+BE |
| TC-AC-LA-509 | E2E | TC-AC-LA-E2E-031-additional-quantity-batas-valid-submit-sukses | FE+BE |
| TC-AC-LA-510 | E2E | TC-AC-LA-E2E-033-validasi-harga-belum-diset-dan-batas-saldo-distributor | FE+BE |
| TC-AC-LA-511 | E2E | TC-AC-LA-E2E-039-preview-cost-per-jenis-license | FE+BE |
| TC-AC-LA-512 | E2E | TC-AC-LA-E2E-122-log-create-distributor-cost-dua-desimal-dan-waiting | FE+BE |
| TC-AC-LA-513 | E2E | TC-AC-LA-E2E-040-cost-terkunci-pembulatan-dan-cost-nol | FE+BE |
| TC-AC-LA-514 | E2E | TC-AC-LA-E2E-122-log-create-distributor-cost-dua-desimal-dan-waiting | FE+BE |
| TC-AC-LA-515 | E2E | TC-AC-LA-E2E-084-konkurensi-notifikasi-approver | FE+BE |
| TC-AC-LA-516 | E2E | TC-AC-LA-E2E-043-submit-asset-control-app-station-storage | FE+BE |
| TC-AC-LA-517 | E2E | TC-AC-LA-E2E-138-approve-approver-entitas-berbeda-activity-log | FE+BE |
| TC-AC-LA-518 | E2E | TC-AC-LA-E2E-123-log-create-principal-dan-event-created | FE+BE |
| TC-AC-LA-519 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-520 | E2E | TC-AC-LA-E2E-128-event-allocation-log-aksi-requester | FE+BE |
| TC-AC-LA-521 | E2E | TC-AC-LA-E2E-063-resubmit-blokir-saldo-dan-app-kedua | FE+BE |
| TC-AC-LA-522 | E2E | TC-AC-LA-E2E-063-resubmit-blokir-saldo-dan-app-kedua | FE+BE |
| TC-AC-LA-523 | E2E | TC-AC-LA-E2E-076-job-pada-client-suspended | FE+BE |
| TC-AC-LA-524 | E2E | TC-AC-LA-E2E-076-job-pada-client-suspended | FE+BE |
| TC-AC-LA-525 | E2E | TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | FE+BE |
| TC-AC-LA-526 | E2E | TC-AC-LA-E2E-127-log-job-sistem-event-dan-notifikasi-timeout | FE+BE |
| TC-AC-LA-527 | E2E | TC-AC-LA-E2E-077-cancel-term-dampak-ke-alokasi-dan-log | FE+BE |
| TC-AC-LA-528 | E2E | TC-AC-LA-E2E-134-konsumen-approvals-dropdown-client-app-station-dan-rename | FE+BE |
| TC-AC-LA-529 | E2E | TC-AC-LA-E2E-090-defense-capability-dicabut-dan-client-dipindah | FE+BE |
| TC-AC-LA-530 | E2E | TC-AC-LA-E2E-045-submit-status-awal-requester-group-manager-default-user-partner | FE+BE |
| TC-AC-LA-531 | E2E | TC-AC-LA-E2E-050-dirty-guard-form-allocate-tutup-dan-batal | FE+BE |

## 4. Pertanyaan terbuka dan Temuan untuk QA

Spec yang memuat butir "Temuan untuk QA" di Notes: 139 dari seluruh spec. Temuan ditulis di Notes tiap spec dan diringkas di sini menurut tema; TC sumber tidak ditambal diam-diam.

### 4.1 Pertanyaan terbuka dari rencana (butuh keputusan QA/FE)

1. Scope kosong (TC-11, 12, 52, 357): Pre-setup #54 men-seed minimal 30 alokasi di scope Principal #1, padahal TC mensyaratkan empty state Current/History, Current tanpa baris, dan Principal tanpa entri Changelog. Tidak ada akun/tenant kosong di Pre-setup. Spec memakai respons list yang di-intercept kosong atau tenant kosong yang disediakan tim FE.
2. Job sistem (TC-263 sampai 279, 395 sampai 398, 406 sampai 408, 412, 426, 437, 484, 491, 523 sampai 526) berprecondition "Tidak ada aktor login" dan akun pengamat log/notifikasi tidak konsisten (TC-426 dan TC-491 tidak menyebut akun).
3. Pelaku kedua "sesi lain" pada TC konkurensi dan pemicu perubahan state (TC-244 term Pending menjadi Active, TC-465 SLA batas) tidak menyebut akun atau mekanisme; spec memakai sesi API akun aktor/approver dan menulis mekanisme pemicu sebagai disediakan tim FE.
4. TC-450 sampai 455 dan 529: pencabutan capability, penonaktifan aktor, dan pemindahan binding Client tidak menyebut akun admin pelaku maupun mekanismenya (termasuk TC-453/454 pada spec 095).
5. TC-393, 394, 411, 395, 412: asersi "tidak masuk Changelog / tanpa System Log" diperlakukan sebagai scope exclusion dengan anchor positif di spec pencatatan; bila QA menganggapnya kelas g murni, pindahkan ke spec absence 094.
6. TC-418 dan 528 me-rename Client Pre-setup #19 (PT Sejahtera); TC-469 dan 496 sampai 500 men-suspend entitas pengalokasi yang dipakai aktor lain. Perubahan Pre-setup bersama ini menuntut pemulihan fixture backend (S-06 pengecualian 2026-10-30) dan suite serial; akun/mekanisme rename dan suspend tidak ditulis di TC.
7. Nama env password akun #1 sampai #18 dan #56 (`AC_LA_*_PASSWORD`, usulan) belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; `Fixture.license-allocation-license` (`fixtures/license-allocation-license.json`) belum ada. Keduanya di luar lingkup edit tahap ini dan disediakan tim FE sebelum script.
8. TC-348 (5.100 baris), TC-421 sampai 424 dan 382 (Date Format/Time Zone General Settings), TC-441 dan 442 (harga dan toggle approval) mengubah state global; pemulihan lewat fixture disediakan tim FE dan suite serial.
9. Nomor TC 507 muncul di Section 2e di antara TC-96 dan TC-97, dan 481 sampai 531 tersebar; urutan TC di dokumen tidak monoton. Tidak memengaruhi pemetaan (memakai id TC).
10. TC-97: Changelog dan Download mengikuti row scope READ dengan HINT harness binary; diperlakukan sebagai asersi jumlah baris (13f 2026-10-30), bukan isi berkas.

### 4.2 Tema Temuan untuk QA dari penulisan spec

- Scope kosong lewat intercept: spec empty state memakai respons list yang di-intercept kosong, bukan data nyata, karena seed Pre-setup selalu berisi alokasi.
- Aktor dan mekanisme tidak bernama: akun admin pencabut wewenang, pelaku "sesi lain", pemicu perubahan state/jam, dan pengamat log/notifikasi tidak disebut di TC; spec menulis "disediakan tim FE" tanpa mengarang endpoint (S-13).
- State bersama pada suite serial: toggle Require Approval, Approval Timeout, General Settings, harga Product Price, status Suspended/Expired, capability role, dan flag Guided Tooltip diubah oleh sebagian spec; pemulihan di hook `after` dan fixture backend (S-06).
- Fixture dan env belum terdaftar: `Fixture.license-allocation-license` (proposed) dan nama `Spectra.env.AC_LA_*_PASSWORD` (proposed) belum ada di `spectra.config.ts`, `.env.example`, maupun `fixtures/`; spec dan script belum bisa dijalankan sampai tim FE mendaftarkannya.
- Ketidakkonsistenan TC sumber yang dicatat penulis di Notes: ukuran halaman tidak disebut pada TC sort/search (TC-307, 309; spec memakai 100 agar nilai distinct teramati), "respons error generik" tanpa kode HTTP (TC-253, 482, 254, 460, 453, 454, 479; asersi tanpa kode), Precondition TC-479 menyebut `Hadi Setiawan` di Region Jawa sedangkan PT Sejahtera di luar Region Jawa, TC-254 Langkah 1 menggabungkan Approve dan Reject dalam satu langkah, TC-307 butir b hanya menyebut Cost ascending, TC-311 tidak menyebut reset sort tab History, serta TC-308 tidak menyebut cara membaca nama lengkap. Temuan lain ada di Notes tiap spec.

### 4.3 Status keputusan (2026-11-02)

Diputuskan pengguna, belum diterapkan ke spec (menunggu prasyarat):

- Butir 1 (scope kosong): tenant kosong dari tim FE, bukan intercept; spec empty state diganti lewat fix pass setelah tenant tersedia.
- Butir 5 (asersi bukan Changelog): dipertahankan sebagai scope exclusion dengan anchor positif.
- Butir 6 dan 8 (state bersama): suite serial dengan fixture restore backend.
- Butir 2, 3, 4 (aktor dan mekanisme tak bernama): TC direvisi lebih dulu, lalu fix pass.
- Ketidakkonsistenan TC sumber (4.2): ditangani di sesi terpisah (gap-check lalu audit/generate-testcase), lalu fix pass.
- Butir 7 (fixture dan env `AC_LA_*`): tetap terbuka, tugas tim FE.
- Butir 9 dan 10: informasi, tanpa tindakan.

Fix pass e2e-generate-spec (2026-11-02), keputusan pengguna diterapkan pada spec 086, 092, 094, 095, 113, 124, 128, 129, 135, 137, dan spec baru 139:

- Absence log aksi gagal dan request langsung ditolak: asersi TC-AC-LA-419, 482 c, 479 c, dan klausa log 471 c ada di spec 094 dengan baseline dan anchor sendiri.
- TC-AC-LA-352 (tab browser baru sebagai objek asersi, kelas c) dipisah ke spec 139.
- Spec 128 menulis kemampuan fixture FE untuk menonaktifkan Pre-setup #53 sebelum blok TC-AC-LA-520 dan memulihkannya di hook `after`; `suite.md` memuat penonaktifan dan pemulihan #53 di daftar fixture restore backend (S-06), sehingga tidak ada lagi bentrok.
- Spec 124, 129, 135, 137 menambah langkah "Tunggu aksi selesai" (8b butir 8).
- Spec 099 dan 104 ditahan sampai TC direvisi (belum disentuh).

Fix pass e2e-generate-spec delta-1 (2026-11-02): kolom Mode, Langkah, dan TC Sumber pada tabel Bagian 1 dihitung ulang dari frontmatter dan Test Steps seluruh 139 spec (N-R7); `suite.md` memuat penonaktifan dan pemulihan #53 (N-R12).

Fix pass e2e-generate-spec 2 dan 3 selesai (2026-11-02); sisa delta 2 yang diterima sudah diproses. Kolom Mode, Langkah, dan TC Sumber tabel Bagian 1 dihitung ulang dari seluruh 139 spec (selisih langkah pada spec 048, 072, 075, 077, 082, 094, 137 dikoreksi).
