# Coverage E2E — Fixed Asset > License

Sumber: `fixed-asset/license/TestCases/tc-license.md` (610 TC aktif, ID `TC-FA-LIC-1`–`617` tidak kontigu; ID 40-44, 502, dan 610 dihapus atau retired). Suite: `specs/FixedAsset/License/`. Prefix: `FA` + `LIC` (`TC-FA-LIC-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-license-backend.md`; kontrak REST murni tidak dipetakan di halaman ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 610 TC aktif masuk 153 spec; tidak ada TC yang dikeluarkan sebagai TC khusus backend. Setiap TC terpetakan ke tepat satu spec primer. Enam TC (440, 441, 445, 453, 549, 614) juga tercantum di `sourceTc` spec absence log penolakan request (S-05, lihat bagian Pengecualian S-05); spec absence itu tidak punya TC primer. Seluruh spec bermode `FE+BE`; tidak ada `Mode: mock`. Kegagalan 5xx dan timeout dipaksa lewat `Spectra.intercept()` di atas backend nyata. Semua spec memakai `coverage.web: automated`.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-LIC-E2E-001-screening-halaman-license-plan-paid-breadcrumb-tabs-bar | Screening Halaman License Plan Paid: Breadcrumb, Tabs Bar, dan Route Tab | FE+BE | 26 | TC-FA-LIC-1, TC-FA-LIC-2, TC-FA-LIC-587 |
| TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | Guided Tooltip: Konten, Back, Overlay, Resize, Skip, dan Done | FE+BE | 35 | TC-FA-LIC-4, TC-FA-LIC-5, TC-FA-LIC-6, TC-FA-LIC-8 |
| TC-FA-LIC-E2E-003-guided-tooltip-keyboard-trigger-hanya-tab-all-license | Guided Tooltip: Navigasi Keyboard, Trigger Hanya di Tab All License, dan Putar Ulang dengan [?] | FE+BE | 32 | TC-FA-LIC-7, TC-FA-LIC-9, TC-FA-LIC-592 |
| TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | Plan Starter: Tab, License Summary, Concurrent User, dan Akses Read Only | FE+BE | 36 | TC-FA-LIC-3, TC-FA-LIC-19, TC-FA-LIC-20, TC-FA-LIC-29, TC-FA-LIC-71, TC-FA-LIC-111, TC-FA-LIC-405, TC-FA-LIC-484 |
| TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional | Role Matrix: Plan Gating per Tier Starter, Growth, Professional, dan Enterprise | FE+BE | 33 | TC-FA-LIC-435, TC-FA-LIC-436, TC-FA-LIC-437, TC-FA-LIC-438 |
| TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | Empty State Client Tanpa Data dan Client Tanpa Alokasi | FE+BE | 31 | TC-FA-LIC-18, TC-FA-LIC-30, TC-FA-LIC-38, TC-FA-LIC-58, TC-FA-LIC-68, TC-FA-LIC-540, TC-FA-LIC-542, TC-FA-LIC-543, TC-FA-LIC-584 |
| TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | License Summary Plan Paid: Screening Kolom Asset, Addon, Not Available, Loading, dan Kolom Identik | FE+BE | 29 | TC-FA-LIC-12, TC-FA-LIC-13, TC-FA-LIC-14, TC-FA-LIC-15, TC-FA-LIC-16, TC-FA-LIC-21 |
| TC-FA-LIC-E2E-008-license-summary-setup-column-baris-unmanaged-dan-used | License Summary: Setup Column, Baris Unmanaged, dan Used Hanya Aset Active | FE+BE | 36 | TC-FA-LIC-17, TC-FA-LIC-23, TC-FA-LIC-595 |
| TC-FA-LIC-E2E-009-license-summary-term-trial-total-asset-addon-gating-tab | License Summary Term Trial: Total Asset, Addon, Concurrent User, dan Gating Tab | FE+BE | 23 | TC-FA-LIC-589, TC-FA-LIC-590, TC-FA-LIC-591 |
| TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | Screening Sub-Tab Subscription History: Kolom, Isi Baris, Status, Empty State, dan Loading | FE+BE | 35 | TC-FA-LIC-24, TC-FA-LIC-25, TC-FA-LIC-26, TC-FA-LIC-27, TC-FA-LIC-28, TC-FA-LIC-31, TC-FA-LIC-527 |
| TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | Screening Sub-Tab Allocation History: Kolom, Isi Baris, Filter Status dan License Type, serta Empty State | FE+BE | 34 | TC-FA-LIC-33, TC-FA-LIC-34, TC-FA-LIC-35, TC-FA-LIC-36, TC-FA-LIC-37, TC-FA-LIC-39 |
| TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | Tab Allocation Quota: Sidebar Group Tree, Header, Pencarian, Pemilihan Node, dan Toggle Collapse | FE+BE | 36 | TC-FA-LIC-47, TC-FA-LIC-48, TC-FA-LIC-56, TC-FA-LIC-57, TC-FA-LIC-539 |
| TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | Tab Allocation Quota: Context Header, Group Quota Summary, Badge Not Allocated, dan Remaining Grup Belum Beralokasi | FE+BE | 38 | TC-FA-LIC-45, TC-FA-LIC-46, TC-FA-LIC-49, TC-FA-LIC-50, TC-FA-LIC-51, TC-FA-LIC-61, TC-FA-LIC-538 |
| TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | Tab Allocation Quota: Tabel Group License Allocation, Kolom, Nilai, Group Name, dan Empty State | FE+BE | 34 | TC-FA-LIC-52, TC-FA-LIC-53, TC-FA-LIC-54, TC-FA-LIC-55, TC-FA-LIC-59, TC-FA-LIC-62, TC-FA-LIC-327 |
| TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | Screening Tab Concurrent User: Metric Summary Bar, Kolom, Isi Baris, Fokus Keyboard, dan Online Users | FE+BE | 37 | TC-FA-LIC-63, TC-FA-LIC-64, TC-FA-LIC-65, TC-FA-LIC-66, TC-FA-LIC-67, TC-FA-LIC-70, TC-FA-LIC-85, TC-FA-LIC-298 |
| TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | Mobile: Group Tree Drawer, Session Card, Card List, dan Group Quota Summary Scroll Horizontal | FE+BE | 22 | TC-FA-LIC-80, TC-FA-LIC-81, TC-FA-LIC-82, TC-FA-LIC-522 |
| TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai | Mobile: Filter Panel Bottom Sheet, Toolbar, Modal sebagai Bottom Sheet, dan Banner | FE+BE | 29 | TC-FA-LIC-79, TC-FA-LIC-520, TC-FA-LIC-521 |
| TC-FA-LIC-E2E-018-state-tenant-toggle-license-allocation-per-group-off | State Tenant: Toggle License Allocation per Group OFF | FE+BE | 24 | TC-FA-LIC-593, TC-FA-LIC-594 |
| TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari | Banner Renewal: Stage Notice, Reminder, dan Final Satu Hari | FE+BE | 36 | TC-FA-LIC-72, TC-FA-LIC-73, TC-FA-LIC-74, TC-FA-LIC-75 |
| TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | Banner Renewal: Stage Expired (Grace) dan Banner Tidak Dapat Ditutup | FE+BE | 37 | TC-FA-LIC-76, TC-FA-LIC-77, TC-FA-LIC-78, TC-FA-LIC-471, TC-FA-LIC-481, TC-FA-LIC-617 |
| TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | Banner Renewal: Batas N pada Hari Pengingat (31, 30, 8, 7, 2, 1, 0) | FE+BE | 24 | TC-FA-LIC-464, TC-FA-LIC-465, TC-FA-LIC-466, TC-FA-LIC-467, TC-FA-LIC-468, TC-FA-LIC-469, TC-FA-LIC-470 |
| TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | Banner Renewal: Isi Banner, Successor, Plan Owner, dan Term Terbaru | FE+BE | 27 | TC-FA-LIC-455, TC-FA-LIC-474, TC-FA-LIC-482, TC-FA-LIC-483 |
| TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss | Banner Renewal: Dismiss dan Penyimpanan State Dismiss | FE+BE | 35 | TC-FA-LIC-477, TC-FA-LIC-478, TC-FA-LIC-480, TC-FA-LIC-525 |
| TC-FA-LIC-E2E-024-banner-renewal-muat-ulang-saat-pindah-tab-fokus-jendela | Banner Renewal: Muat Ulang saat Pindah Tab, Fokus Jendela, dan Tab Browser Baru | FE+BE | 38 | TC-FA-LIC-475, TC-FA-LIC-476, TC-FA-LIC-479 |
| TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin | Sinkron Konfigurasi Banner terhadap Renewal di Admin Console, Lifecycle Settings, dan T-0 | FE+BE | 34 | TC-FA-LIC-417, TC-FA-LIC-418, TC-FA-LIC-419, TC-FA-LIC-611 |
| TC-FA-LIC-E2E-026-role-matrix-visibilitas-menu-license-dan-direct-url | Role Matrix: Visibilitas Menu License dan Akses URL Langsung per Role | FE+BE | 20 | TC-FA-LIC-88, TC-FA-LIC-89, TC-FA-LIC-90 |
| TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | Role Matrix: Elemen Baca License (Tab, Toolbar, Banner, dan Data) per Role | FE+BE | 38 | TC-FA-LIC-91, TC-FA-LIC-92, TC-FA-LIC-108, TC-FA-LIC-109, TC-FA-LIC-485 |
| TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | Role Matrix: Force Logout Show, Hidden, dan Eksekusi per Role | FE+BE | 44 | TC-FA-LIC-93, TC-FA-LIC-94, TC-FA-LIC-95, TC-FA-LIC-96, TC-FA-LIC-110, TC-FA-LIC-596 |
| TC-FA-LIC-E2E-029-role-matrix-tombol-edit-show-disabled-hidden-per-role | Role Matrix: Tombol Edit Show dan Hidden per Role | FE+BE | 27 | TC-FA-LIC-97, TC-FA-LIC-98 |
| TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license | Role Matrix: Scope Edit Descendant untuk Manage Asset License dan Group Manager | FE+BE | 41 | TC-FA-LIC-99, TC-FA-LIC-100, TC-FA-LIC-101, TC-FA-LIC-530 |
| TC-FA-LIC-E2E-031-role-matrix-edit-allocation-dieksekusi-per-role | Role Matrix: Edit Allocation Dieksekusi Sukses per Role | FE+BE | 23 | TC-FA-LIC-102, TC-FA-LIC-104, TC-FA-LIC-105 |
| TC-FA-LIC-E2E-032-role-matrix-remove-allocation-dengan-mengosongkan-field | Role Matrix: Mengosongkan Field Allocated Quota, Total Control dan Manage Global License Dapat, Read Only Tanpa Tombol Edit | FE+BE | 19 | TC-FA-LIC-107 |
| TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | Defense-in-Depth: Request Langsung Tanpa Hak Ditolak 403 | FE+BE | 26 | TC-FA-LIC-440, TC-FA-LIC-441, TC-FA-LIC-442, TC-FA-LIC-443, TC-FA-LIC-444, TC-FA-LIC-531 |
| TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | Defense-in-Depth: Sesi Sendiri, DOM Dipulihkan, Isolasi Tenant, dan Payload Tidak Valid | FE+BE | 29 | TC-FA-LIC-445, TC-FA-LIC-446, TC-FA-LIC-451, TC-FA-LIC-453, TC-FA-LIC-544 |
| TC-FA-LIC-E2E-035-state-tenant-client-suspended-expired-menolak-force-logout-dan-edit | State Tenant: Client Suspended Menolak Force Logout, Edit, dan Remove Allocation | FE+BE | 38 | TC-FA-LIC-447, TC-FA-LIC-448, TC-FA-LIC-449 |
| TC-FA-LIC-E2E-036-state-tenant-term-grace-expired-plan-starter-dan-toggle-off | State Tenant: Term Grace atau Expired, Plan Starter, dan Toggle Alokasi per Grup OFF | FE+BE | 34 | TC-FA-LIC-450, TC-FA-LIC-549, TC-FA-LIC-614 |
| TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | Screening Modal Edit Allocation: Grup Child, Level 1, dan Grup Belum Beralokasi | FE+BE | 31 | TC-FA-LIC-112, TC-FA-LIC-113, TC-FA-LIC-114, TC-FA-LIC-115, TC-FA-LIC-148 |
| TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol | Modal Edit Allocation: Tombol Saving, Copy Dinamis, Helper Level 1, dan Aksesibilitas | FE+BE | 41 | TC-FA-LIC-116, TC-FA-LIC-117, TC-FA-LIC-147, TC-FA-LIC-526 |
| TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir | Edit Allocation: Validasi Minimum Quota V-FALIC-01 Diblokir | FE+BE | 32 | TC-FA-LIC-124, TC-FA-LIC-125, TC-FA-LIC-126, TC-FA-LIC-137 |
| TC-FA-LIC-E2E-040-edit-allocation-minimum-quota-memasukkan-reserved | Edit Allocation: Minimum Quota Memasukkan Reserved dan Pemakaian Subtree | FE+BE | 27 | TC-FA-LIC-132, TC-FA-LIC-133 |
| TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | Edit Allocation: Validasi Maximum Quota V-FALIC-02 dan V-FALIC-03 | FE+BE | 38 | TC-FA-LIC-128, TC-FA-LIC-129, TC-FA-LIC-130, TC-FA-LIC-131, TC-FA-LIC-134 |
| TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja | Edit Allocation: Field Allocated Quota Hanya Menerima Digit dan Batas 15 Karakter | FE+BE | 32 | TC-FA-LIC-154, TC-FA-LIC-155, TC-FA-LIC-156, TC-FA-LIC-157 |
| TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat | Edit Allocation: Simpan Sukses Child, Remaining Parent, dan Muat Ulang Section | FE+BE | 38 | TC-FA-LIC-118, TC-FA-LIC-119, TC-FA-LIC-120, TC-FA-LIC-121 |
| TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | Edit Allocation: Nilai Batas Diterima (0, Minimum, Maximum, Enter, Double-click Save) | FE+BE | 40 | TC-FA-LIC-122, TC-FA-LIC-123, TC-FA-LIC-127, TC-FA-LIC-146, TC-FA-LIC-159 |
| TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit | Edit Allocation: Lewat Ikon Summary dan Edit Tanpa Perubahan (No-Op) | FE+BE | 30 | TC-FA-LIC-135, TC-FA-LIC-136, TC-FA-LIC-517, TC-FA-LIC-519 |
| TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih | Modal Edit Allocation: Clear Field, Menutup Bersih, dan Dialog Unsaved Changes | FE+BE | 32 | TC-FA-LIC-138, TC-FA-LIC-139, TC-FA-LIC-140, TC-FA-LIC-141 |
| TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh | Modal Edit Allocation: Backdrop, Nilai Dikembalikan, Refresh Browser, dan Navigasi Internal | FE+BE | 42 | TC-FA-LIC-142, TC-FA-LIC-143, TC-FA-LIC-144, TC-FA-LIC-145 |
| TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target | Edit dan Remove Allocation: Idempotensi, Parent Tidak Beralokasi, dan Grup Target Terhapus | FE+BE | 52 | TC-FA-LIC-151, TC-FA-LIC-153, TC-FA-LIC-166, TC-FA-LIC-461 |
| TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi | Remove Allocation: Ditolak bila Subgroup Beralokasi dan Kasus Boleh Dihapus | FE+BE | 35 | TC-FA-LIC-161, TC-FA-LIC-162, TC-FA-LIC-163, TC-FA-LIC-167 |
| TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | Remove Allocation: Sukses Tanpa Dialog, Remaining Leluhur, dan Double-click Save | FE+BE | 51 | TC-FA-LIC-160, TC-FA-LIC-164, TC-FA-LIC-168, TC-FA-LIC-496, TC-FA-LIC-518 |
| TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | Force Logout: Dialog, Cancel, Esc, Backdrop, Sukses, Sesi Idle, dan Sesi Berakhir | FE+BE | 60 | TC-FA-LIC-169, TC-FA-LIC-170, TC-FA-LIC-171, TC-FA-LIC-172, TC-FA-LIC-174, TC-FA-LIC-175, TC-FA-LIC-178 |
| TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | Resilience Baca: Kegagalan Memuat 500 pada Summary, Riwayat, Allocation Quota, Concurrent User, dan Banner | FE+BE | 48 | TC-FA-LIC-22, TC-FA-LIC-32, TC-FA-LIC-60, TC-FA-LIC-69, TC-FA-LIC-462, TC-FA-LIC-463 |
| TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | Resilience Tulis: Kegagalan 5xx dan Timeout pada Edit, Remove, dan Force Logout | FE+BE | 53 | TC-FA-LIC-149, TC-FA-LIC-150, TC-FA-LIC-165, TC-FA-LIC-176, TC-FA-LIC-177 |
| TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search | Download License Summary: Popover Dua Format, Kolom yang Tampil, dan Tidak Terpengaruh Search, Filter, serta Setup Column Riwayat | FE+BE | 24 | TC-FA-LIC-180, TC-FA-LIC-183, TC-FA-LIC-187, TC-FA-LIC-588 |
| TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | Isi Berkas Download: License Summary dan Riwayat (CSV UTF-8 BOM, XLSX Sheet1, Nilai Sel, dan Urutan Sort) | FE+BE | 48 | TC-FA-LIC-181, TC-FA-LIC-182, TC-FA-LIC-184, TC-FA-LIC-188, TC-FA-LIC-225, TC-FA-LIC-229 |
| TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter | Download Allocation Quota: Toolbar Section 2, Mengikuti Search dan Filter, serta Seluruh Baris yang Cocok | FE+BE | 31 | TC-FA-LIC-550, TC-FA-LIC-553, TC-FA-LIC-554, TC-FA-LIC-555 |
| TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node | Download Allocation Quota: Mengikuti Column Visibility dan Sort, Node Leaf, serta Search Tanpa Hasil | FE+BE | 35 | TC-FA-LIC-556, TC-FA-LIC-557, TC-FA-LIC-558, TC-FA-LIC-559 |
| TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx | Isi Berkas Download Allocation Quota: Dua Blok Ditumpuk (CSV dan XLSX), Nilai Sel, dan Blok Section 2 Kosong | FE+BE | 44 | TC-FA-LIC-551, TC-FA-LIC-552, TC-FA-LIC-560, TC-FA-LIC-563 |
| TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan | Download Riwayat Subscription dan Allocation: Cakupan Seluruh Baris, Mengikuti Search, dan Kolom yang Disembunyikan | FE+BE | 42 | TC-FA-LIC-222, TC-FA-LIC-223, TC-FA-LIC-226, TC-FA-LIC-227 |
| TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | Resilience Download: Toast Error Tanpa Ekstensi dan Nol Baris Tetap Mengunduh Header | FE+BE | 54 | TC-FA-LIC-185, TC-FA-LIC-224, TC-FA-LIC-228, TC-FA-LIC-361, TC-FA-LIC-561, TC-FA-LIC-583 |
| TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | Subscription History: Search (Reveal, Per Kelas Kolom, Guard Kolom Tanggal, dan Trim Spasi) | FE+BE | 32 | TC-FA-LIC-189, TC-FA-LIC-190, TC-FA-LIC-191, TC-FA-LIC-192, TC-FA-LIC-193 |
| TC-FA-LIC-E2E-062-subscription-history-search-terikat-column-visibility | Subscription History: Sort Default, Search Terikat Visibilitas Kolom, dan Berpindah Kolom Sort | FE+BE | 21 | TC-FA-LIC-194, TC-FA-LIC-197, TC-FA-LIC-198 |
| TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | Subscription History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip) | FE+BE | 44 | TC-FA-LIC-199, TC-FA-LIC-200, TC-FA-LIC-201, TC-FA-LIC-202, TC-FA-LIC-203 |
| TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari | Subscription History: Filter Date Range (Inklusif, Satu Hari, Tutup Panel Tanpa Apply, dan Independen dari Column Visibility) | FE+BE | 39 | TC-FA-LIC-204, TC-FA-LIC-205, TC-FA-LIC-523, TC-FA-LIC-524 |
| TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column | Subscription History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom | FE+BE | 34 | TC-FA-LIC-206, TC-FA-LIC-207, TC-FA-LIC-208, TC-FA-LIC-209 |
| TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | Subscription History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa) | FE+BE | 38 | TC-FA-LIC-210, TC-FA-LIC-211, TC-FA-LIC-212, TC-FA-LIC-213 |
| TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter | Subscription History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi | FE+BE | 52 | TC-FA-LIC-214, TC-FA-LIC-215, TC-FA-LIC-216, TC-FA-LIC-217 |
| TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab | Retensi State: Sub-tab Riwayat dan Tab License saat Berpindah Tab, serta Reset dari Menu License | FE+BE | 38 | TC-FA-LIC-218, TC-FA-LIC-219, TC-FA-LIC-221, TC-FA-LIC-536 |
| TC-FA-LIC-E2E-069-retensi-state-tab-allocation-quota-f5-mempertahankan-node | Retensi State Tab Allocation Quota: Muat Ulang (F5) Mempertahankan Node dan Pindah Tab Mereset Node | FE+BE | 24 | TC-FA-LIC-220, TC-FA-LIC-537 |
| TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity | Allocation History: Search (Reveal, Per Kelas Kolom, Quantity Numerik, dan Format Angka) | FE+BE | 26 | TC-FA-LIC-230, TC-FA-LIC-231, TC-FA-LIC-232, TC-FA-LIC-261 |
| TC-FA-LIC-E2E-071-allocation-history-search-non-searchable-trim-terikat | Allocation History: Search Guard Kolom Tanggal, Trim Spasi Tepi, dan Terikat Visibilitas Kolom | FE+BE | 17 | TC-FA-LIC-233, TC-FA-LIC-234, TC-FA-LIC-235 |
| TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | Allocation History: Filter Panel (Screening, Opsi per Kelas Dropdown, OR dan AND, serta Chip) | FE+BE | 46 | TC-FA-LIC-241, TC-FA-LIC-242, TC-FA-LIC-243, TC-FA-LIC-244, TC-FA-LIC-245 |
| TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | Allocation History: Sort Default, Berpindah Kolom Sort, Filter Date Range, dan Range Min-Max Quantity | FE+BE | 32 | TC-FA-LIC-239, TC-FA-LIC-240, TC-FA-LIC-246, TC-FA-LIC-247, TC-FA-LIC-248 |
| TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column | Allocation History: Overlay Column Visibility, Popup Setup Column, serta Ceklis dan Geser per Kolom | FE+BE | 34 | TC-FA-LIC-249, TC-FA-LIC-250, TC-FA-LIC-251, TC-FA-LIC-252 |
| TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | Allocation History: Setup Column (Pin dan Unpin per Kolom, Reset to Default, X atau Esc, dan Satu Kolom Tersisa) | FE+BE | 38 | TC-FA-LIC-253, TC-FA-LIC-254, TC-FA-LIC-255, TC-FA-LIC-256 |
| TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter | Allocation History: Paginasi dan Kombinasi Search, Filter, Sort, serta Paginasi | FE+BE | 52 | TC-FA-LIC-257, TC-FA-LIC-258, TC-FA-LIC-259, TC-FA-LIC-260 |
| TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non | Active Sessions: Search Reveal, Per Kelas Kolom, Kolom Tanggal Non-Searchable, dan Trim Spasi | FE+BE | 31 | TC-FA-LIC-262, TC-FA-LIC-263, TC-FA-LIC-264, TC-FA-LIC-265 |
| TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | Active Sessions: Search dan Sort Terikat Visibilitas Kolom, Kolom Curated | FE+BE | 40 | TC-FA-LIC-266, TC-FA-LIC-267, TC-FA-LIC-514, TC-FA-LIC-515, TC-FA-LIC-516 |
| TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | Active Sessions: Sort Siklus 3-State per Kelas Kolom, Default, Perpindahan Kolom, dan Navigasi Keyboard | FE+BE | 33 | TC-FA-LIC-86, TC-FA-LIC-268, TC-FA-LIC-269, TC-FA-LIC-270, TC-FA-LIC-271, TC-FA-LIC-272 |
| TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | Active Sessions: Filter Panel Screening, Opsi Dropdown, OR dan AND, serta Chip | FE+BE | 33 | TC-FA-LIC-273, TC-FA-LIC-274, TC-FA-LIC-275, TC-FA-LIC-276, TC-FA-LIC-277 |
| TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary | Active Sessions: Filter Date Range, Kolom Curated, Temporary Until, dan Badge Filter | FE+BE | 32 | TC-FA-LIC-278, TC-FA-LIC-279, TC-FA-LIC-280, TC-FA-LIC-281 |
| TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom | Active Sessions: Screening Column Visibility dan Setup Column, serta Ceklis, Unceklis, dan Geser Kolom Hideable Visible | FE+BE | 28 | TC-FA-LIC-282, TC-FA-LIC-283, TC-FA-LIC-284, TC-FA-LIC-285 |
| TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | Active Sessions: Setup Column Pin dan Unpin, Reset to Default, X atau Esc, dan Satu Kolom Tersisa | FE+BE | 31 | TC-FA-LIC-286, TC-FA-LIC-290, TC-FA-LIC-291, TC-FA-LIC-292 |
| TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible | Active Sessions: Setup Column Ceklis, Geser, dan Pin Kolom Curated Hidden Default | FE+BE | 29 | TC-FA-LIC-287, TC-FA-LIC-288, TC-FA-LIC-289 |
| TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort | Active Sessions: Paginasi serta Kombinasi Search, Filter, Sort, dan Page Size | FE+BE | 45 | TC-FA-LIC-294, TC-FA-LIC-295, TC-FA-LIC-296, TC-FA-LIC-297 |
| TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota | Group License Allocation: Search Reveal, Kolom Teks, Numerik Kuota, dan Numerik Addon | FE+BE | 24 | TC-FA-LIC-299, TC-FA-LIC-300, TC-FA-LIC-301, TC-FA-LIC-302 |
| TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | Group License Allocation: Sort Default, Search Trim dan Numerik, Sort Alfabetis, dan Perpindahan Kolom Sort | FE+BE | 28 | TC-FA-LIC-303, TC-FA-LIC-304, TC-FA-LIC-305, TC-FA-LIC-307, TC-FA-LIC-308, TC-FA-LIC-511 |
| TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | Group License Allocation: Sort Numerik, Nilai Kosong, Baris Bernilai Sama, dan Reset State Saat Ganti Node | FE+BE | 42 | TC-FA-LIC-306, TC-FA-LIC-309, TC-FA-LIC-310, TC-FA-LIC-311, TC-FA-LIC-512 |
| TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max | Group License Allocation: Filter Panel Screening, Range Min-Max per Kolom, dan Baris Bernilai Kosong | FE+BE | 18 | TC-FA-LIC-312, TC-FA-LIC-313, TC-FA-LIC-314, TC-FA-LIC-513 |
| TC-FA-LIC-E2E-090-group-license-allocation-column-visibility-dan-setup | Group License Allocation: Screening Column Visibility dan Setup Column, serta Ceklis dan Unceklis Kolom Hideable Visible | FE+BE | 20 | TC-FA-LIC-315, TC-FA-LIC-316, TC-FA-LIC-317 |
| TC-FA-LIC-E2E-091-group-license-allocation-setup-column-geser-pin-dan-unpin | Group License Allocation: Setup Column Geser (Drag), Pin, dan Unpin Kolom Hideable Visible Default | FE+BE | 17 | TC-FA-LIC-318, TC-FA-LIC-319 |
| TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu | Group License Allocation: Setup Column Satu Kolom Tersisa, X atau Esc, Reset to Default, dan Guard Tabel Summary | FE+BE | 30 | TC-FA-LIC-320, TC-FA-LIC-321, TC-FA-LIC-322, TC-FA-LIC-363 |
| TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search | Group License Allocation: Kombinasi Search, Filter, Sort, dan Page Size serta Paginasi | FE+BE | 47 | TC-FA-LIC-323, TC-FA-LIC-324, TC-FA-LIC-325, TC-FA-LIC-326 |
| TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | Modal Changelog Allocation Quota: Screening Popup, Penutupan, Isi Entri, Opsi Filter, dan Format Tanggal | FE+BE | 38 | TC-FA-LIC-328, TC-FA-LIC-329, TC-FA-LIC-330, TC-FA-LIC-348, TC-FA-LIC-362 |
| TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh | Modal Changelog Allocation Quota: Opsi Filter Group Name, Pemisahan dari Modal Concurrent User, Tanpa Pengaruh Node Sidebar, dan Download | FE+BE | 35 | TC-FA-LIC-360, TC-FA-LIC-383, TC-FA-LIC-486, TC-FA-LIC-600 |
| TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | Search Modal Changelog Allocation Quota: Reveal, Kolom Teks dan Angka, Guard Kolom Date, dan Trim Spasi | FE+BE | 37 | TC-FA-LIC-331, TC-FA-LIC-332, TC-FA-LIC-333, TC-FA-LIC-334, TC-FA-LIC-335 |
| TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | Sort Modal Changelog Allocation Quota: Siklus Tiga Klik per Kelas Kolom, Urutan Default, dan Pindah Kolom | FE+BE | 30 | TC-FA-LIC-336, TC-FA-LIC-337, TC-FA-LIC-338, TC-FA-LIC-339, TC-FA-LIC-340 |
| TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and | Filter Modal Changelog Allocation Quota: Screening Panel, Opsi per Dropdown, Aturan OR dan AND, dan Chip | FE+BE | 30 | TC-FA-LIC-341, TC-FA-LIC-342, TC-FA-LIC-343, TC-FA-LIC-344 |
| TC-FA-LIC-E2E-099-changelog-allocation-quota-chip-uncheck-date-range-satu | Filter Modal Changelog Allocation Quota: Chip Uncheck di Dropdown, Date Range Inklusif, dan Satu Hari | FE+BE | 19 | TC-FA-LIC-345, TC-FA-LIC-346, TC-FA-LIC-347 |
| TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup | Column Visibility dan Setup Column Modal Changelog Allocation Quota: Screening, Ceklis, dan Geser per Kolom | FE+BE | 25 | TC-FA-LIC-349, TC-FA-LIC-350, TC-FA-LIC-351, TC-FA-LIC-352 |
| TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | Setup Column Modal Changelog Allocation Quota: Pin dan Unpin per Kolom, Reset to Default, Tutup X atau Esc, dan Satu Kolom Tersisa | FE+BE | 37 | TC-FA-LIC-353, TC-FA-LIC-354, TC-FA-LIC-355, TC-FA-LIC-356 |
| TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | Modal Changelog Concurrent User: Screening Popup, Penutupan, Isi Entri Force Logout, Sort Kolom Bernilai Tunggal, dan Format Tanggal | FE+BE | 35 | TC-FA-LIC-564, TC-FA-LIC-565, TC-FA-LIC-566, TC-FA-LIC-571, TC-FA-LIC-585 |
| TC-FA-LIC-E2E-103-changelog-concurrent-user-search-dan-sort | Search Modal Changelog Concurrent User: Reveal, Kolom Searchable, dan Guard Date | FE+BE | 30 | TC-FA-LIC-567, TC-FA-LIC-568, TC-FA-LIC-586 |
| TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | Filter Modal Changelog Concurrent User: Single-Value Guard, Opsi Dropdown, OR dan AND, Date Range, dan Paginasi | FE+BE | 42 | TC-FA-LIC-572, TC-FA-LIC-573, TC-FA-LIC-574, TC-FA-LIC-575, TC-FA-LIC-581 |
| TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup | Column Visibility dan Setup Column Modal Changelog Concurrent User: Screening, Ceklis, dan Geser per Kolom | FE+BE | 25 | TC-FA-LIC-576, TC-FA-LIC-577, TC-FA-LIC-578, TC-FA-LIC-579 |
| TC-FA-LIC-E2E-106-changelog-concurrent-user-setup-column-pin-dan-unpin | Setup Column Modal Changelog Concurrent User: Pin dan Unpin per Kolom dan Download CSV serta XLSX | FE+BE | 24 | TC-FA-LIC-580, TC-FA-LIC-582 |
| TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | Pencatatan Log Edit Allocation di Changelog, System Log, dan Activity Log | FE+BE | 33 | TC-FA-LIC-364, TC-FA-LIC-365, TC-FA-LIC-366, TC-FA-LIC-370, TC-FA-LIC-371, TC-FA-LIC-372 |
| TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | Pencatatan Log Remove Allocation dan Force Logout di Changelog, System Log, dan Activity Log | FE+BE | 26 | TC-FA-LIC-367, TC-FA-LIC-368, TC-FA-LIC-369, TC-FA-LIC-373, TC-FA-LIC-374, TC-FA-LIC-375 |
| TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete | Pencatatan Log: Snapshot Immutability, Snapshot Nama Grup, dan Satu Aksi Satu Entri per Surface | FE+BE | 30 | TC-FA-LIC-379, TC-FA-LIC-380, TC-FA-LIC-381 |
| TC-FA-LIC-E2E-110-absence-log-no-op-force-logout-sesi-berakhir-validasi | Absence Log: Edit Tanpa Perubahan, Force Logout Sesi Berakhir, dan Validasi atau Kegagalan 5xx Tidak Menulis Entri | FE+BE | 39 | TC-FA-LIC-376, TC-FA-LIC-377, TC-FA-LIC-378 |
| TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | Absence Log: Request Langsung yang Ditolak Server Tidak Menulis Entri Log | FE+BE | 37 | TC-FA-LIC-440, TC-FA-LIC-441, TC-FA-LIC-445, TC-FA-LIC-453, TC-FA-LIC-549, TC-FA-LIC-614 |
| TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | Sinkron Lintas Modul: Settings Groups dan Admin Console Tercermin di Halaman License | FE+BE | 32 | TC-FA-LIC-412, TC-FA-LIC-413, TC-FA-LIC-414, TC-FA-LIC-415, TC-FA-LIC-416 |
| TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove | Konkurensi Dua Sesi Total Control: Edit dan Remove Allocation Bersamaan | FE+BE | 34 | TC-FA-LIC-152, TC-FA-LIC-158, TC-FA-LIC-456, TC-FA-LIC-458 |
| TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage | Konkurensi Pemeriksaan Kuota Grup: Dua Registrasi, Registrasi dengan Arrival Transfer, dan Aksi Manage | FE+BE | 37 | TC-FA-LIC-606, TC-FA-LIC-607, TC-FA-LIC-608 |
| TC-FA-LIC-E2E-115-sesi-lain-force-logout-ganda-sse-concurrent-user-seat | Concurrent User dengan Sesi Lain: Pembaruan SSE dan Dialog Log Out pada Pengguna yang Di-Force-Logout | FE+BE | 35 | TC-FA-LIC-179, TC-FA-LIC-615 |
| TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur | Registrasi Aset terhadap Kuota Grup: Ditolak Saat Penuh, Memakai Remaining Leluhur, dan Sisa Pool Organisasi | FE+BE | 39 | TC-FA-LIC-384, TC-FA-LIC-385, TC-FA-LIC-386, TC-FA-LIC-387 |
| TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used | Registrasi Massal dan Import: Pemeriksaan Kuota Sekali, All-or-Nothing, dan Batas Tepat Remaining | FE+BE | 48 | TC-FA-LIC-388, TC-FA-LIC-389, TC-FA-LIC-390, TC-FA-LIC-488 |
| TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | Transfer ke Grup Penuh Ditolak, Edit dan Remove Allocation Membuka Kembali Penerimaan Aset | FE+BE | 51 | TC-FA-LIC-391, TC-FA-LIC-490, TC-FA-LIC-534, TC-FA-LIC-392, TC-FA-LIC-393 |
| TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto | Approval Registrasi Aset: Submit Menahan Reserved, Approve, Reject, dan Auto-cancel | FE+BE | 32 | TC-FA-LIC-394, TC-FA-LIC-395, TC-FA-LIC-396, TC-FA-LIC-397 |
| TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | Aset Unmanaged, Transisi Manage, dan Konsistensi Used pada License Summary | FE+BE | 37 | TC-FA-LIC-401, TC-FA-LIC-402, TC-FA-LIC-403, TC-FA-LIC-404, TC-FA-LIC-493 |
| TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off | check_group_quota pada Plan Paid, Plan Starter, dan License allocation per group OFF | FE+BE | 36 | TC-FA-LIC-489, TC-FA-LIC-505, TC-FA-LIC-609, TC-FA-LIC-613 |
| TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | Aksi Manage Aset Unmanaged terhadap Kuota Grup: Batas Sisa Slot, Ditolak Seluruhnya, dan Reserved | FE+BE | 53 | TC-FA-LIC-497, TC-FA-LIC-498, TC-FA-LIC-499, TC-FA-LIC-500, TC-FA-LIC-501 |
| TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | Aksi Manage: Grup Tanpa Alokasi, Over-used, Gagal Diproses, dan Jeda managed_transition_time | FE+BE | 57 | TC-FA-LIC-503, TC-FA-LIC-504, TC-FA-LIC-506, TC-FA-LIC-507, TC-FA-LIC-508 |
| TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | Perhitungan Edge: Remaining Ditampilkan 0 Saat Over-used, Tingkat Full, dan Minimum Quota dengan Reserved | FE+BE | 54 | TC-FA-LIC-410, TC-FA-LIC-494, TC-FA-LIC-495, TC-FA-LIC-510, TC-FA-LIC-612 |
| TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | Peringatan Kuota Tenant: Ambang Low dan Full serta Transisi Penanda Tingkat | FE+BE | 31 | TC-FA-LIC-423, TC-FA-LIC-424, TC-FA-LIC-425, TC-FA-LIC-426, TC-FA-LIC-427 |
| TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | Peringatan Kuota Tenant: Job Per Jam, Penilaian Pasca-commit, dan Pencatatan oleh System | FE+BE | 64 | TC-FA-LIC-429, TC-FA-LIC-430, TC-FA-LIC-491, TC-FA-LIC-492, TC-FA-LIC-546, TC-FA-LIC-547 |
| TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | Peringatan Kuota Tenant: Cakupan Penerima, Penerima Nonaktif, Plan Starter, dan Penilaian Dilewati | FE+BE | 50 | TC-FA-LIC-431, TC-FA-LIC-432, TC-FA-LIC-433, TC-FA-LIC-434, TC-FA-LIC-487, TC-FA-LIC-533, TC-FA-LIC-548 |
| TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan | Peringatan Kuota Tenant: Aksi Manage, Starter Tanpa Ledger, Perubahan Cap Plan, dan Term Trial | FE+BE | 34 | TC-FA-LIC-509, TC-FA-LIC-603, TC-FA-LIC-604, TC-FA-LIC-605 |
| TC-FA-LIC-E2E-129-guard-struktural-tabel-license-tanpa-seleksi-kolom-audit-dan-kontrol-tulis | Guard Struktural Tabel License: Tanpa Seleksi, Tanpa Kolom Audit, dan Kontrol Tulis Terbatas | FE+BE | 29 | TC-FA-LIC-83, TC-FA-LIC-84, TC-FA-LIC-439 |
| TC-FA-LIC-E2E-130-tooltip-toolbar-tabel-license-search-filter-download-changelog-column-visibility | Tooltip Toolbar Tabel License: Search, Filter, Download, Changelog, dan Column Visibility | FE+BE | 16 | TC-FA-LIC-10, TC-FA-LIC-11 |
| TC-FA-LIC-E2E-131-banner-renewal-term-bukan-live-dan-term-trial | Banner Renewal: Term Bukan Live dan Term Trial | FE+BE | 23 | TC-FA-LIC-472, TC-FA-LIC-473 |
| TC-FA-LIC-E2E-132-format-tanggal-general-settings-dan-zona-waktu-banner | Format Tanggal General Settings pada Tabel, Modal Changelog, dan Zona Waktu Banner | FE+BE | 25 | TC-FA-LIC-420, TC-FA-LIC-421, TC-FA-LIC-422 |
| TC-FA-LIC-E2E-133-edit-allocation-urutan-penolakan-minimum-quota-menang-atas-maximum | Edit Allocation: Urutan Penolakan Saat Submit, Minimum Quota Menang atas Maximum Quota | FE+BE | 13 | TC-FA-LIC-545 |
| TC-FA-LIC-E2E-134-edit-allocation-save-tanpa-perubahan-pemakaian-melampaui-alokasi | Edit Allocation: Save Tanpa Perubahan pada Grup yang Pemakaiannya Melampaui Allocated Quota | FE+BE | 24 | TC-FA-LIC-598 |
| TC-FA-LIC-E2E-135-role-matrix-download-license-summary-read-only-group-manager | Role Matrix: Download License Summary Tersedia untuk Read Only dan Group Manager | FE+BE | 6 | TC-FA-LIC-186 |
| TC-FA-LIC-E2E-136-role-matrix-download-allocation-quota-read-only-group-manager-manage-asset-license | Role Matrix: Download Allocation Quota Tersedia untuk Read Only, Group Manager, dan Manage Asset License | FE+BE | 13 | TC-FA-LIC-562 |
| TC-FA-LIC-E2E-137-allocation-history-sort-siklus-3-state-per-kelas-kolom | Allocation History: Sort Siklus 3 State per Kelas Kolom (Alfabetis, Numerik, dan Tanggal) | FE+BE | 7 | TC-FA-LIC-236, TC-FA-LIC-237, TC-FA-LIC-238 |
| TC-FA-LIC-E2E-138-subscription-history-sort-siklus-3-state-per-kelas-kolom | Subscription History: Sort Siklus 3 State per Kelas Kolom (Alfabetis dan Tanggal) | FE+BE | 7 | TC-FA-LIC-195, TC-FA-LIC-196 |
| TC-FA-LIC-E2E-139-active-sessions-max-visible-columns-dan-siklus-hidup-custom-field | Active Sessions: Max Visible Columns Setup Column dan Kolom Custom Field Hilang Saat Deactivate atau Delete | FE+BE | 22 | TC-FA-LIC-293, TC-FA-LIC-541 |
| TC-FA-LIC-E2E-140-active-sessions-nilai-device-os-dan-browser-apa-adanya | Active Sessions: Nilai Device / OS dan Browser Apa Adanya, Kosong Tampil ke `—`, dan Opsi Filter DISTINCT | FE+BE | 10 | TC-FA-LIC-599 |
| TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri | Paginasi Modal Changelog Allocation Quota dengan 25 Entri: Page Size, Nomor Halaman, Sort, Search, dan Filter | FE+BE | 28 | TC-FA-LIC-357, TC-FA-LIC-358, TC-FA-LIC-359 |
| TC-FA-LIC-E2E-142-changelog-allocation-quota-contoh-prd-urutan-penanda-tingkat | Modal Changelog Allocation Quota: Contoh PRD Urutan Penanda Tingkat Normal, Low, Full, Normal Konsisten dengan License Summary | FE+BE | 13 | TC-FA-LIC-601 |
| TC-FA-LIC-E2E-143-pencatatan-log-cascade-delete-grup-beralokasi | Pencatatan Log Cascade-Delete Grup Beralokasi di Changelog, System Log Admin, dan Activity Log | FE+BE | 23 | TC-FA-LIC-382, TC-FA-LIC-602 |
| TC-FA-LIC-E2E-144-sinkron-lintas-modul-grup-terpilih-dihapus-saat-modal-edit-terbuka | Sinkron Lintas Modul: Node Sidebar Terpilih Dihapus Cascade Saat Modal Edit Allocation Terbuka | FE+BE | 11 | TC-FA-LIC-535 |
| TC-FA-LIC-E2E-145-peringatan-kuota-tenant-penanda-turun-setelah-top-up-dan-penurunan-berikutnya | Peringatan Kuota Tenant: Penanda Turun Setelah Top-up dan Penurunan Berikutnya Mengirim Low | FE+BE | 35 | TC-FA-LIC-428, TC-FA-LIC-532 |
| TC-FA-LIC-E2E-146-submit-tanpa-approval-delete-dispose-dan-draf-dihapus-pelepasan-kuota | Submit Tanpa Approval, Delete dan Dispose Aset, serta Draf Dihapus terhadap Used dan Reserved | FE+BE | 23 | TC-FA-LIC-398, TC-FA-LIC-399, TC-FA-LIC-400 |
| TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | State Tenant: Plan Turun ke Starter, Kembali ke Paid, dan Total Asset Capacity Lebih Kecil dari Total Allocated | FE+BE | 29 | TC-FA-LIC-406, TC-FA-LIC-407, TC-FA-LIC-408, TC-FA-LIC-409, TC-FA-LIC-411 |
| TC-FA-LIC-E2E-148-role-matrix-tombol-edit-disabled-manage-asset-license | Role Matrix: Tombol Edit Disabled untuk Manage Asset License | FE+BE | 20 | TC-FA-LIC-106, TC-FA-LIC-597 |
| TC-FA-LIC-E2E-167-defense-in-depth-markup-tampil-teks-dan-injeksi-dom-field-quota | Defense-in-Depth: Nama Bermarkup Tampil sebagai Teks dan Injeksi Karakter Terlarang ke Field Allocated Quota | FE+BE | 23 | TC-FA-LIC-452, TC-FA-LIC-454 |
| TC-FA-LIC-E2E-168-konkurensi-dua-sesi-registrasi-aset-remove-dan-pool-organisasi | Konkurensi Dua Sesi Total Control: Registrasi Aset, Remove Allocation, dan Pool Organisasi | FE+BE | 32 | TC-FA-LIC-457, TC-FA-LIC-459, TC-FA-LIC-616 |
| TC-FA-LIC-E2E-169-sesi-lain-online-users-force-logout-ganda-dan-pelepasan-seat | Concurrent User dengan Sesi Lain: Online Users Sinkron, Force Logout Ganda, dan Pelepasan Seat | FE+BE | 29 | TC-FA-LIC-87, TC-FA-LIC-173, TC-FA-LIC-460 |
| TC-FA-LIC-E2E-170-role-matrix-remove-allocation-manage-asset-license-group-manager-default-user | Role Matrix: Manage Asset License, Group Manager, dan Default User Menghapus Alokasi dengan Mengosongkan Field | FE+BE | 28 | TC-FA-LIC-103, TC-FA-LIC-528, TC-FA-LIC-529 |
| TC-FA-LIC-E2E-171-changelog-concurrent-user-sort-date-dan-siklus-tiga-klik | Sort Modal Changelog Concurrent User: Urutan Default Date dan Siklus Tiga Klik | FE+BE | 15 | TC-FA-LIC-569, TC-FA-LIC-570 |

## Pengecualian S-05: TC di dua spec

- TC-FA-LIC-440: TC-FA-LIC-E2E-033, TC-FA-LIC-E2E-111
- TC-FA-LIC-441: TC-FA-LIC-E2E-033, TC-FA-LIC-E2E-111
- TC-FA-LIC-445: TC-FA-LIC-E2E-034, TC-FA-LIC-E2E-111
- TC-FA-LIC-453: TC-FA-LIC-E2E-034, TC-FA-LIC-E2E-111
- TC-FA-LIC-549: TC-FA-LIC-E2E-036, TC-FA-LIC-E2E-111
- TC-FA-LIC-614: TC-FA-LIC-E2E-036, TC-FA-LIC-E2E-111

Spec absence memuat klausa absence log (tanpa entri) dengan penolakan request sebagai pemicu; spec asal mengasersi status respons dan state data. Aturan C2 `check-suite.py` mengizinkan ini karena folder absence dan butir S-05 ada di kedua spec.

## Kebutuhan lingkungan (tim FE/BE)

- Berkas `fixtures/` untuk Pre-setup License (`Fixture.fixedAssetLicense.*`) belum ada; disediakan tim FE.
- Fixture BE pemulih dan penyetel state (hierarki dan kuota #12, riwayat #13, sesi aktif #14 dan #26, riwayat Changelog #27 dan #31, aset #20 dan #28, tanggal banner #15, plan dan toggle #16, jam job per jam) disediakan tim FE/BE; endpoint tidak dikarang (`suite.md`).
- Env var password aktor berprefiks `FA_` (mis. `FA_TC_PASSWORD`) perlu didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Akun tanpa email di Pre-setup (Budi Santoso #14, Total Control client Suspended/Expired #18, term Trial #24, rantai Renewal #25) dan pemicu aksi Manage (#28) ditulis "disediakan tim FE/BE".
- Sesi API aktor (login API dengan token yang tidak dihitung sebagai sesi web), pembaca berkas unduhan CSV dan XLSX, serta pemulihan konfigurasi kolom disediakan tim FE/BE.

## Pertanyaan terbuka

- Prefix `LIC`: `foundation/tc-prefix-registry.md` hanya memuat `FALIC` sebagai reserved; registry perlu diperbarui di luar tahap ini.
- Butir Lampiran A untuk Fixed Asset > License belum ada; pola pemulihan Pre-setup oleh fixture BE pada suite serial menunggu keputusan.
- Aksi Manage (PRD `asset/` belum ditulis) menjadi pemicu beberapa spec; tetap `automated` dengan pemicu "disediakan tim FE".
- Temuan TC sumber (TC-173 meminta login ke FAMS, TC-179 mengasersi konteks kedua, TC-390 meminta Import di modul lain) dicatat di `## Notes` spec terkait.
- Konvensi `docs/e2e-conventions.md` berubah di tengah run (S-03, S-06, S-08, S-12, bagian 3); dampak pada spec dicatat di `work-items/fixed-asset-license/progress-e2e-generate-spec.md`.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-LIC-1 | TC-FA-LIC-E2E-001-screening-halaman-license-plan-paid-breadcrumb-tabs-bar | FE+BE |
| TC-FA-LIC-2 | TC-FA-LIC-E2E-001-screening-halaman-license-plan-paid-breadcrumb-tabs-bar | FE+BE |
| TC-FA-LIC-3 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-4 | TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | FE+BE |
| TC-FA-LIC-5 | TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | FE+BE |
| TC-FA-LIC-6 | TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | FE+BE |
| TC-FA-LIC-7 | TC-FA-LIC-E2E-003-guided-tooltip-keyboard-trigger-hanya-tab-all-license | FE+BE |
| TC-FA-LIC-8 | TC-FA-LIC-E2E-002-guided-tooltip-konten-skip-done-back-dan-overlay | FE+BE |
| TC-FA-LIC-9 | TC-FA-LIC-E2E-003-guided-tooltip-keyboard-trigger-hanya-tab-all-license | FE+BE |
| TC-FA-LIC-10 | TC-FA-LIC-E2E-130-tooltip-toolbar-tabel-license-search-filter-download-changelog-column-visibility | FE+BE |
| TC-FA-LIC-11 | TC-FA-LIC-E2E-130-tooltip-toolbar-tabel-license-search-filter-download-changelog-column-visibility | FE+BE |
| TC-FA-LIC-12 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-13 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-14 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-15 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-16 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-17 | TC-FA-LIC-E2E-008-license-summary-setup-column-baris-unmanaged-dan-used | FE+BE |
| TC-FA-LIC-18 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-19 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-20 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-21 | TC-FA-LIC-E2E-007-license-summary-plan-paid-screening-kolom-asset-addon-not | FE+BE |
| TC-FA-LIC-22 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-23 | TC-FA-LIC-E2E-008-license-summary-setup-column-baris-unmanaged-dan-used | FE+BE |
| TC-FA-LIC-24 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-25 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-26 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-27 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-28 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-29 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-30 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-31 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-32 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-33 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-34 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-35 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-36 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-37 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-38 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-39 | TC-FA-LIC-E2E-011-screening-sub-tab-allocation-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-45 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-46 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-47 | TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | FE+BE |
| TC-FA-LIC-48 | TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | FE+BE |
| TC-FA-LIC-49 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-50 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-51 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-52 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-53 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-54 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-55 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-56 | TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | FE+BE |
| TC-FA-LIC-57 | TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | FE+BE |
| TC-FA-LIC-58 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-59 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-60 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-61 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-62 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-63 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-64 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-65 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-66 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-67 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-68 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-69 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-70 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-71 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-72 | TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari | FE+BE |
| TC-FA-LIC-73 | TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari | FE+BE |
| TC-FA-LIC-74 | TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari | FE+BE |
| TC-FA-LIC-75 | TC-FA-LIC-E2E-019-banner-renewal-stage-notice-reminder-final-satu-hari | FE+BE |
| TC-FA-LIC-76 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |
| TC-FA-LIC-77 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |
| TC-FA-LIC-78 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |
| TC-FA-LIC-79 | TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai | FE+BE |
| TC-FA-LIC-80 | TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | FE+BE |
| TC-FA-LIC-81 | TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | FE+BE |
| TC-FA-LIC-82 | TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | FE+BE |
| TC-FA-LIC-83 | TC-FA-LIC-E2E-129-guard-struktural-tabel-license-tanpa-seleksi-kolom-audit-dan-kontrol-tulis | FE+BE |
| TC-FA-LIC-84 | TC-FA-LIC-E2E-129-guard-struktural-tabel-license-tanpa-seleksi-kolom-audit-dan-kontrol-tulis | FE+BE |
| TC-FA-LIC-85 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-86 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-87 | TC-FA-LIC-E2E-169-sesi-lain-online-users-force-logout-ganda-dan-pelepasan-seat | FE+BE |
| TC-FA-LIC-88 | TC-FA-LIC-E2E-026-role-matrix-visibilitas-menu-license-dan-direct-url | FE+BE |
| TC-FA-LIC-89 | TC-FA-LIC-E2E-026-role-matrix-visibilitas-menu-license-dan-direct-url | FE+BE |
| TC-FA-LIC-90 | TC-FA-LIC-E2E-026-role-matrix-visibilitas-menu-license-dan-direct-url | FE+BE |
| TC-FA-LIC-91 | TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | FE+BE |
| TC-FA-LIC-92 | TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | FE+BE |
| TC-FA-LIC-93 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-94 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-95 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-96 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-97 | TC-FA-LIC-E2E-029-role-matrix-tombol-edit-show-disabled-hidden-per-role | FE+BE |
| TC-FA-LIC-98 | TC-FA-LIC-E2E-029-role-matrix-tombol-edit-show-disabled-hidden-per-role | FE+BE |
| TC-FA-LIC-99 | TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license | FE+BE |
| TC-FA-LIC-100 | TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license | FE+BE |
| TC-FA-LIC-101 | TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license | FE+BE |
| TC-FA-LIC-102 | TC-FA-LIC-E2E-031-role-matrix-edit-allocation-dieksekusi-per-role | FE+BE |
| TC-FA-LIC-103 | TC-FA-LIC-E2E-170-role-matrix-remove-allocation-manage-asset-license-group-manager-default-user | FE+BE |
| TC-FA-LIC-104 | TC-FA-LIC-E2E-031-role-matrix-edit-allocation-dieksekusi-per-role | FE+BE |
| TC-FA-LIC-105 | TC-FA-LIC-E2E-031-role-matrix-edit-allocation-dieksekusi-per-role | FE+BE |
| TC-FA-LIC-106 | TC-FA-LIC-E2E-148-role-matrix-tombol-edit-disabled-manage-asset-license | FE+BE |
| TC-FA-LIC-107 | TC-FA-LIC-E2E-032-role-matrix-remove-allocation-dengan-mengosongkan-field | FE+BE |
| TC-FA-LIC-108 | TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | FE+BE |
| TC-FA-LIC-109 | TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | FE+BE |
| TC-FA-LIC-110 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-111 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-112 | TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | FE+BE |
| TC-FA-LIC-113 | TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | FE+BE |
| TC-FA-LIC-114 | TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | FE+BE |
| TC-FA-LIC-115 | TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | FE+BE |
| TC-FA-LIC-116 | TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol | FE+BE |
| TC-FA-LIC-117 | TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol | FE+BE |
| TC-FA-LIC-118 | TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat | FE+BE |
| TC-FA-LIC-119 | TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat | FE+BE |
| TC-FA-LIC-120 | TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat | FE+BE |
| TC-FA-LIC-121 | TC-FA-LIC-E2E-043-edit-allocation-simpan-sukses-child-remaining-parent-muat | FE+BE |
| TC-FA-LIC-122 | TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | FE+BE |
| TC-FA-LIC-123 | TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | FE+BE |
| TC-FA-LIC-124 | TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir | FE+BE |
| TC-FA-LIC-125 | TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir | FE+BE |
| TC-FA-LIC-126 | TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir | FE+BE |
| TC-FA-LIC-127 | TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | FE+BE |
| TC-FA-LIC-128 | TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | FE+BE |
| TC-FA-LIC-129 | TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | FE+BE |
| TC-FA-LIC-130 | TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | FE+BE |
| TC-FA-LIC-131 | TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | FE+BE |
| TC-FA-LIC-132 | TC-FA-LIC-E2E-040-edit-allocation-minimum-quota-memasukkan-reserved | FE+BE |
| TC-FA-LIC-133 | TC-FA-LIC-E2E-040-edit-allocation-minimum-quota-memasukkan-reserved | FE+BE |
| TC-FA-LIC-134 | TC-FA-LIC-E2E-041-edit-allocation-validasi-maximum-quota-v-falic-02-03 | FE+BE |
| TC-FA-LIC-135 | TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit | FE+BE |
| TC-FA-LIC-136 | TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit | FE+BE |
| TC-FA-LIC-137 | TC-FA-LIC-E2E-039-edit-allocation-validasi-minimum-quota-v-falic-01-diblokir | FE+BE |
| TC-FA-LIC-138 | TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih | FE+BE |
| TC-FA-LIC-139 | TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih | FE+BE |
| TC-FA-LIC-140 | TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih | FE+BE |
| TC-FA-LIC-141 | TC-FA-LIC-E2E-046-modal-edit-allocation-clear-field-menutup-bersih | FE+BE |
| TC-FA-LIC-142 | TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh | FE+BE |
| TC-FA-LIC-143 | TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh | FE+BE |
| TC-FA-LIC-144 | TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh | FE+BE |
| TC-FA-LIC-145 | TC-FA-LIC-E2E-047-modal-edit-allocation-backdrop-nilai-dikembalikan-refresh | FE+BE |
| TC-FA-LIC-146 | TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | FE+BE |
| TC-FA-LIC-147 | TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol | FE+BE |
| TC-FA-LIC-148 | TC-FA-LIC-E2E-037-modal-edit-allocation-screening-grup-child-level-1-belum | FE+BE |
| TC-FA-LIC-149 | TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | FE+BE |
| TC-FA-LIC-150 | TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | FE+BE |
| TC-FA-LIC-151 | TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target | FE+BE |
| TC-FA-LIC-152 | TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove | FE+BE |
| TC-FA-LIC-153 | TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target | FE+BE |
| TC-FA-LIC-154 | TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja | FE+BE |
| TC-FA-LIC-155 | TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja | FE+BE |
| TC-FA-LIC-156 | TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja | FE+BE |
| TC-FA-LIC-157 | TC-FA-LIC-E2E-042-edit-allocation-input-field-allocated-quota-digit-saja | FE+BE |
| TC-FA-LIC-158 | TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove | FE+BE |
| TC-FA-LIC-159 | TC-FA-LIC-E2E-044-edit-allocation-nilai-batas-diterima-0-minimum-maximum | FE+BE |
| TC-FA-LIC-160 | TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | FE+BE |
| TC-FA-LIC-161 | TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi | FE+BE |
| TC-FA-LIC-162 | TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi | FE+BE |
| TC-FA-LIC-163 | TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi | FE+BE |
| TC-FA-LIC-164 | TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | FE+BE |
| TC-FA-LIC-165 | TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | FE+BE |
| TC-FA-LIC-166 | TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target | FE+BE |
| TC-FA-LIC-167 | TC-FA-LIC-E2E-049-remove-allocation-ditolak-bila-subgroup-beralokasi | FE+BE |
| TC-FA-LIC-168 | TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | FE+BE |
| TC-FA-LIC-169 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-170 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-171 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-172 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-173 | TC-FA-LIC-E2E-169-sesi-lain-online-users-force-logout-ganda-dan-pelepasan-seat | FE+BE |
| TC-FA-LIC-174 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-175 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-176 | TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | FE+BE |
| TC-FA-LIC-177 | TC-FA-LIC-E2E-053-resilience-tulis-kegagalan-5xx-dan-timeout-pada-edit | FE+BE |
| TC-FA-LIC-178 | TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi | FE+BE |
| TC-FA-LIC-179 | TC-FA-LIC-E2E-115-sesi-lain-force-logout-ganda-sse-concurrent-user-seat | FE+BE |
| TC-FA-LIC-180 | TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search | FE+BE |
| TC-FA-LIC-181 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-182 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-183 | TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search | FE+BE |
| TC-FA-LIC-184 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-185 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-186 | TC-FA-LIC-E2E-135-role-matrix-download-license-summary-read-only-group-manager | FE+BE |
| TC-FA-LIC-187 | TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search | FE+BE |
| TC-FA-LIC-188 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-189 | TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-190 | TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-191 | TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-192 | TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-193 | TC-FA-LIC-E2E-061-subscription-history-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-194 | TC-FA-LIC-E2E-062-subscription-history-search-terikat-column-visibility | FE+BE |
| TC-FA-LIC-195 | TC-FA-LIC-E2E-138-subscription-history-sort-siklus-3-state-per-kelas-kolom | FE+BE |
| TC-FA-LIC-196 | TC-FA-LIC-E2E-138-subscription-history-sort-siklus-3-state-per-kelas-kolom | FE+BE |
| TC-FA-LIC-197 | TC-FA-LIC-E2E-062-subscription-history-search-terikat-column-visibility | FE+BE |
| TC-FA-LIC-198 | TC-FA-LIC-E2E-062-subscription-history-search-terikat-column-visibility | FE+BE |
| TC-FA-LIC-199 | TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-200 | TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-201 | TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-202 | TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-203 | TC-FA-LIC-E2E-063-subscription-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-204 | TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari | FE+BE |
| TC-FA-LIC-205 | TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari | FE+BE |
| TC-FA-LIC-206 | TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-207 | TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-208 | TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-209 | TC-FA-LIC-E2E-065-subscription-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-210 | TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-211 | TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-212 | TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-213 | TC-FA-LIC-E2E-066-subscription-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-214 | TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-215 | TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-216 | TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-217 | TC-FA-LIC-E2E-067-subscription-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-218 | TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab | FE+BE |
| TC-FA-LIC-219 | TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab | FE+BE |
| TC-FA-LIC-220 | TC-FA-LIC-E2E-069-retensi-state-tab-allocation-quota-f5-mempertahankan-node | FE+BE |
| TC-FA-LIC-221 | TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab | FE+BE |
| TC-FA-LIC-222 | TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan | FE+BE |
| TC-FA-LIC-223 | TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan | FE+BE |
| TC-FA-LIC-224 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-225 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-226 | TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan | FE+BE |
| TC-FA-LIC-227 | TC-FA-LIC-E2E-059-download-riwayat-subscription-dan-allocation-cakupan | FE+BE |
| TC-FA-LIC-228 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-229 | TC-FA-LIC-E2E-055-isi-berkas-license-summary-dan-riwayat-csv-bom-xlsx | FE+BE |
| TC-FA-LIC-230 | TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity | FE+BE |
| TC-FA-LIC-231 | TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity | FE+BE |
| TC-FA-LIC-232 | TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity | FE+BE |
| TC-FA-LIC-233 | TC-FA-LIC-E2E-071-allocation-history-search-non-searchable-trim-terikat | FE+BE |
| TC-FA-LIC-234 | TC-FA-LIC-E2E-071-allocation-history-search-non-searchable-trim-terikat | FE+BE |
| TC-FA-LIC-235 | TC-FA-LIC-E2E-071-allocation-history-search-non-searchable-trim-terikat | FE+BE |
| TC-FA-LIC-236 | TC-FA-LIC-E2E-137-allocation-history-sort-siklus-3-state-per-kelas-kolom | FE+BE |
| TC-FA-LIC-237 | TC-FA-LIC-E2E-137-allocation-history-sort-siklus-3-state-per-kelas-kolom | FE+BE |
| TC-FA-LIC-238 | TC-FA-LIC-E2E-137-allocation-history-sort-siklus-3-state-per-kelas-kolom | FE+BE |
| TC-FA-LIC-239 | TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | FE+BE |
| TC-FA-LIC-240 | TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | FE+BE |
| TC-FA-LIC-241 | TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-242 | TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-243 | TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-244 | TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-245 | TC-FA-LIC-E2E-072-allocation-history-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-246 | TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | FE+BE |
| TC-FA-LIC-247 | TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | FE+BE |
| TC-FA-LIC-248 | TC-FA-LIC-E2E-073-allocation-history-sort-default-filter-date-range-dan-min | FE+BE |
| TC-FA-LIC-249 | TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-250 | TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-251 | TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-252 | TC-FA-LIC-E2E-074-allocation-history-column-visibility-dan-setup-column | FE+BE |
| TC-FA-LIC-253 | TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-254 | TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-255 | TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-256 | TC-FA-LIC-E2E-075-allocation-history-setup-column-pin-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-257 | TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-258 | TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-259 | TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-260 | TC-FA-LIC-E2E-076-allocation-history-paginasi-dan-kombinasi-search-filter | FE+BE |
| TC-FA-LIC-261 | TC-FA-LIC-E2E-070-allocation-history-search-reveal-per-kelas-kolom-quantity | FE+BE |
| TC-FA-LIC-262 | TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-263 | TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-264 | TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-265 | TC-FA-LIC-E2E-077-active-sessions-search-reveal-per-kelas-kolom-non | FE+BE |
| TC-FA-LIC-266 | TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | FE+BE |
| TC-FA-LIC-267 | TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | FE+BE |
| TC-FA-LIC-268 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-269 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-270 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-271 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-272 | TC-FA-LIC-E2E-079-active-sessions-sort-siklus-3-state-default-perpindahan | FE+BE |
| TC-FA-LIC-273 | TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-274 | TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-275 | TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-276 | TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-277 | TC-FA-LIC-E2E-080-active-sessions-filter-screening-opsi-or-and-chip | FE+BE |
| TC-FA-LIC-278 | TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary | FE+BE |
| TC-FA-LIC-279 | TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary | FE+BE |
| TC-FA-LIC-280 | TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary | FE+BE |
| TC-FA-LIC-281 | TC-FA-LIC-E2E-081-active-sessions-filter-date-range-kolom-curated-temporary | FE+BE |
| TC-FA-LIC-282 | TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom | FE+BE |
| TC-FA-LIC-283 | TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom | FE+BE |
| TC-FA-LIC-284 | TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom | FE+BE |
| TC-FA-LIC-285 | TC-FA-LIC-E2E-082-active-sessions-column-visibility-dan-setup-column-kolom | FE+BE |
| TC-FA-LIC-286 | TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | FE+BE |
| TC-FA-LIC-287 | TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible | FE+BE |
| TC-FA-LIC-288 | TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible | FE+BE |
| TC-FA-LIC-289 | TC-FA-LIC-E2E-084-active-sessions-setup-column-kolom-curated-max-visible | FE+BE |
| TC-FA-LIC-290 | TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | FE+BE |
| TC-FA-LIC-291 | TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | FE+BE |
| TC-FA-LIC-292 | TC-FA-LIC-E2E-083-active-sessions-setup-column-kolom-hideable-pin-reset-x | FE+BE |
| TC-FA-LIC-293 | TC-FA-LIC-E2E-139-active-sessions-max-visible-columns-dan-siklus-hidup-custom-field | FE+BE |
| TC-FA-LIC-294 | TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort | FE+BE |
| TC-FA-LIC-295 | TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort | FE+BE |
| TC-FA-LIC-296 | TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort | FE+BE |
| TC-FA-LIC-297 | TC-FA-LIC-E2E-085-active-sessions-paginasi-dan-kombinasi-search-filter-sort | FE+BE |
| TC-FA-LIC-298 | TC-FA-LIC-E2E-015-screening-tab-concurrent-user-metric-summary-bar-kolom | FE+BE |
| TC-FA-LIC-299 | TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota | FE+BE |
| TC-FA-LIC-300 | TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota | FE+BE |
| TC-FA-LIC-301 | TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota | FE+BE |
| TC-FA-LIC-302 | TC-FA-LIC-E2E-086-group-license-allocation-search-reveal-teks-numerik-kuota | FE+BE |
| TC-FA-LIC-303 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-304 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-305 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-306 | TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | FE+BE |
| TC-FA-LIC-307 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-308 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-309 | TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | FE+BE |
| TC-FA-LIC-310 | TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | FE+BE |
| TC-FA-LIC-311 | TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | FE+BE |
| TC-FA-LIC-312 | TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max | FE+BE |
| TC-FA-LIC-313 | TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max | FE+BE |
| TC-FA-LIC-314 | TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max | FE+BE |
| TC-FA-LIC-315 | TC-FA-LIC-E2E-090-group-license-allocation-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-316 | TC-FA-LIC-E2E-090-group-license-allocation-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-317 | TC-FA-LIC-E2E-090-group-license-allocation-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-318 | TC-FA-LIC-E2E-091-group-license-allocation-setup-column-geser-pin-dan-unpin | FE+BE |
| TC-FA-LIC-319 | TC-FA-LIC-E2E-091-group-license-allocation-setup-column-geser-pin-dan-unpin | FE+BE |
| TC-FA-LIC-320 | TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-321 | TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-322 | TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-323 | TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search | FE+BE |
| TC-FA-LIC-324 | TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search | FE+BE |
| TC-FA-LIC-325 | TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search | FE+BE |
| TC-FA-LIC-326 | TC-FA-LIC-E2E-093-group-license-allocation-paginasi-dan-kombinasi-search | FE+BE |
| TC-FA-LIC-327 | TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom | FE+BE |
| TC-FA-LIC-328 | TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | FE+BE |
| TC-FA-LIC-329 | TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | FE+BE |
| TC-FA-LIC-330 | TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | FE+BE |
| TC-FA-LIC-331 | TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | FE+BE |
| TC-FA-LIC-332 | TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | FE+BE |
| TC-FA-LIC-333 | TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | FE+BE |
| TC-FA-LIC-334 | TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | FE+BE |
| TC-FA-LIC-335 | TC-FA-LIC-E2E-096-changelog-allocation-quota-search-reveal-per-kelas-kolom | FE+BE |
| TC-FA-LIC-336 | TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | FE+BE |
| TC-FA-LIC-337 | TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | FE+BE |
| TC-FA-LIC-338 | TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | FE+BE |
| TC-FA-LIC-339 | TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | FE+BE |
| TC-FA-LIC-340 | TC-FA-LIC-E2E-097-changelog-allocation-quota-sort-per-kelas-kolom-default | FE+BE |
| TC-FA-LIC-341 | TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and | FE+BE |
| TC-FA-LIC-342 | TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and | FE+BE |
| TC-FA-LIC-343 | TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and | FE+BE |
| TC-FA-LIC-344 | TC-FA-LIC-E2E-098-changelog-allocation-quota-filter-screening-opsi-or-and | FE+BE |
| TC-FA-LIC-345 | TC-FA-LIC-E2E-099-changelog-allocation-quota-chip-uncheck-date-range-satu | FE+BE |
| TC-FA-LIC-346 | TC-FA-LIC-E2E-099-changelog-allocation-quota-chip-uncheck-date-range-satu | FE+BE |
| TC-FA-LIC-347 | TC-FA-LIC-E2E-099-changelog-allocation-quota-chip-uncheck-date-range-satu | FE+BE |
| TC-FA-LIC-348 | TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | FE+BE |
| TC-FA-LIC-349 | TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-350 | TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-351 | TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-352 | TC-FA-LIC-E2E-100-changelog-allocation-quota-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-353 | TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | FE+BE |
| TC-FA-LIC-354 | TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | FE+BE |
| TC-FA-LIC-355 | TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | FE+BE |
| TC-FA-LIC-356 | TC-FA-LIC-E2E-101-changelog-allocation-quota-setup-column-pin-reset-x-esc | FE+BE |
| TC-FA-LIC-357 | TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri | FE+BE |
| TC-FA-LIC-358 | TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri | FE+BE |
| TC-FA-LIC-359 | TC-FA-LIC-E2E-141-changelog-allocation-quota-paginasi-25-entri | FE+BE |
| TC-FA-LIC-360 | TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh | FE+BE |
| TC-FA-LIC-361 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-362 | TC-FA-LIC-E2E-094-changelog-allocation-quota-screening-popup-tutup-isi | FE+BE |
| TC-FA-LIC-363 | TC-FA-LIC-E2E-092-group-license-allocation-setup-column-reset-x-esc-satu | FE+BE |
| TC-FA-LIC-364 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-365 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-366 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-367 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-368 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-369 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-370 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-371 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-372 | TC-FA-LIC-E2E-107-pencatatan-log-edit-allocation-di-changelog-system-log | FE+BE |
| TC-FA-LIC-373 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-374 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-375 | TC-FA-LIC-E2E-108-pencatatan-log-remove-allocation-dan-force-logout-di-tiga | FE+BE |
| TC-FA-LIC-376 | TC-FA-LIC-E2E-110-absence-log-no-op-force-logout-sesi-berakhir-validasi | FE+BE |
| TC-FA-LIC-377 | TC-FA-LIC-E2E-110-absence-log-no-op-force-logout-sesi-berakhir-validasi | FE+BE |
| TC-FA-LIC-378 | TC-FA-LIC-E2E-110-absence-log-no-op-force-logout-sesi-berakhir-validasi | FE+BE |
| TC-FA-LIC-379 | TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete | FE+BE |
| TC-FA-LIC-380 | TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete | FE+BE |
| TC-FA-LIC-381 | TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete | FE+BE |
| TC-FA-LIC-382 | TC-FA-LIC-E2E-143-pencatatan-log-cascade-delete-grup-beralokasi | FE+BE |
| TC-FA-LIC-383 | TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh | FE+BE |
| TC-FA-LIC-384 | TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur | FE+BE |
| TC-FA-LIC-385 | TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur | FE+BE |
| TC-FA-LIC-386 | TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur | FE+BE |
| TC-FA-LIC-387 | TC-FA-LIC-E2E-116-registrasi-aset-terhadap-kuota-grup-ditolak-penuh-leluhur | FE+BE |
| TC-FA-LIC-388 | TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used | FE+BE |
| TC-FA-LIC-389 | TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used | FE+BE |
| TC-FA-LIC-390 | TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used | FE+BE |
| TC-FA-LIC-391 | TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | FE+BE |
| TC-FA-LIC-392 | TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | FE+BE |
| TC-FA-LIC-393 | TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | FE+BE |
| TC-FA-LIC-394 | TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto | FE+BE |
| TC-FA-LIC-395 | TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto | FE+BE |
| TC-FA-LIC-396 | TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto | FE+BE |
| TC-FA-LIC-397 | TC-FA-LIC-E2E-119-approval-submit-menahan-reserved-approve-reject-auto | FE+BE |
| TC-FA-LIC-398 | TC-FA-LIC-E2E-146-submit-tanpa-approval-delete-dispose-dan-draf-dihapus-pelepasan-kuota | FE+BE |
| TC-FA-LIC-399 | TC-FA-LIC-E2E-146-submit-tanpa-approval-delete-dispose-dan-draf-dihapus-pelepasan-kuota | FE+BE |
| TC-FA-LIC-400 | TC-FA-LIC-E2E-146-submit-tanpa-approval-delete-dispose-dan-draf-dihapus-pelepasan-kuota | FE+BE |
| TC-FA-LIC-401 | TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | FE+BE |
| TC-FA-LIC-402 | TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | FE+BE |
| TC-FA-LIC-403 | TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | FE+BE |
| TC-FA-LIC-404 | TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | FE+BE |
| TC-FA-LIC-405 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-406 | TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | FE+BE |
| TC-FA-LIC-407 | TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | FE+BE |
| TC-FA-LIC-408 | TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | FE+BE |
| TC-FA-LIC-409 | TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | FE+BE |
| TC-FA-LIC-410 | TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | FE+BE |
| TC-FA-LIC-411 | TC-FA-LIC-E2E-147-state-tenant-plan-starter-paid-kuota-grup-dan-total-asset-capacity | FE+BE |
| TC-FA-LIC-412 | TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | FE+BE |
| TC-FA-LIC-413 | TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | FE+BE |
| TC-FA-LIC-414 | TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | FE+BE |
| TC-FA-LIC-415 | TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | FE+BE |
| TC-FA-LIC-416 | TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console | FE+BE |
| TC-FA-LIC-417 | TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin | FE+BE |
| TC-FA-LIC-418 | TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin | FE+BE |
| TC-FA-LIC-419 | TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin | FE+BE |
| TC-FA-LIC-420 | TC-FA-LIC-E2E-132-format-tanggal-general-settings-dan-zona-waktu-banner | FE+BE |
| TC-FA-LIC-421 | TC-FA-LIC-E2E-132-format-tanggal-general-settings-dan-zona-waktu-banner | FE+BE |
| TC-FA-LIC-422 | TC-FA-LIC-E2E-132-format-tanggal-general-settings-dan-zona-waktu-banner | FE+BE |
| TC-FA-LIC-423 | TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | FE+BE |
| TC-FA-LIC-424 | TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | FE+BE |
| TC-FA-LIC-425 | TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | FE+BE |
| TC-FA-LIC-426 | TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | FE+BE |
| TC-FA-LIC-427 | TC-FA-LIC-E2E-125-peringatan-kuota-tenant-ambang-low-dan-full-transisi | FE+BE |
| TC-FA-LIC-428 | TC-FA-LIC-E2E-145-peringatan-kuota-tenant-penanda-turun-setelah-top-up-dan-penurunan-berikutnya | FE+BE |
| TC-FA-LIC-429 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-430 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-431 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-432 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-433 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-434 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-435 | TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional | FE+BE |
| TC-FA-LIC-436 | TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional | FE+BE |
| TC-FA-LIC-437 | TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional | FE+BE |
| TC-FA-LIC-438 | TC-FA-LIC-E2E-005-plan-gating-per-tier-starter-growth-professional | FE+BE |
| TC-FA-LIC-439 | TC-FA-LIC-E2E-129-guard-struktural-tabel-license-tanpa-seleksi-kolom-audit-dan-kontrol-tulis | FE+BE |
| TC-FA-LIC-440 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-440 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-441 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-441 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-442 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-443 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-444 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-445 | TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | FE+BE |
| TC-FA-LIC-445 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-446 | TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | FE+BE |
| TC-FA-LIC-447 | TC-FA-LIC-E2E-035-state-tenant-client-suspended-expired-menolak-force-logout-dan-edit | FE+BE |
| TC-FA-LIC-448 | TC-FA-LIC-E2E-035-state-tenant-client-suspended-expired-menolak-force-logout-dan-edit | FE+BE |
| TC-FA-LIC-449 | TC-FA-LIC-E2E-035-state-tenant-client-suspended-expired-menolak-force-logout-dan-edit | FE+BE |
| TC-FA-LIC-450 | TC-FA-LIC-E2E-036-state-tenant-term-grace-expired-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-451 | TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | FE+BE |
| TC-FA-LIC-452 | TC-FA-LIC-E2E-167-defense-in-depth-markup-tampil-teks-dan-injeksi-dom-field-quota | FE+BE |
| TC-FA-LIC-453 | TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | FE+BE |
| TC-FA-LIC-453 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-454 | TC-FA-LIC-E2E-167-defense-in-depth-markup-tampil-teks-dan-injeksi-dom-field-quota | FE+BE |
| TC-FA-LIC-455 | TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | FE+BE |
| TC-FA-LIC-456 | TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove | FE+BE |
| TC-FA-LIC-457 | TC-FA-LIC-E2E-168-konkurensi-dua-sesi-registrasi-aset-remove-dan-pool-organisasi | FE+BE |
| TC-FA-LIC-458 | TC-FA-LIC-E2E-113-konkurensi-dua-sesi-total-control-edit-remove | FE+BE |
| TC-FA-LIC-459 | TC-FA-LIC-E2E-168-konkurensi-dua-sesi-registrasi-aset-remove-dan-pool-organisasi | FE+BE |
| TC-FA-LIC-460 | TC-FA-LIC-E2E-169-sesi-lain-online-users-force-logout-ganda-dan-pelepasan-seat | FE+BE |
| TC-FA-LIC-461 | TC-FA-LIC-E2E-048-edit-remove-allocation-parent-tidak-beralokasi-target | FE+BE |
| TC-FA-LIC-462 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-463 | TC-FA-LIC-E2E-052-resilience-baca-kegagalan-memuat-500-pada-summary-riwayat | FE+BE |
| TC-FA-LIC-464 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-465 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-466 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-467 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-468 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-469 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-470 | TC-FA-LIC-E2E-021-banner-renewal-batas-n-pada-hari-pengingat-31-30-8-7-2-1-0 | FE+BE |
| TC-FA-LIC-471 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |
| TC-FA-LIC-472 | TC-FA-LIC-E2E-131-banner-renewal-term-bukan-live-dan-term-trial | FE+BE |
| TC-FA-LIC-473 | TC-FA-LIC-E2E-131-banner-renewal-term-bukan-live-dan-term-trial | FE+BE |
| TC-FA-LIC-474 | TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | FE+BE |
| TC-FA-LIC-475 | TC-FA-LIC-E2E-024-banner-renewal-muat-ulang-saat-pindah-tab-fokus-jendela | FE+BE |
| TC-FA-LIC-476 | TC-FA-LIC-E2E-024-banner-renewal-muat-ulang-saat-pindah-tab-fokus-jendela | FE+BE |
| TC-FA-LIC-477 | TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss | FE+BE |
| TC-FA-LIC-478 | TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss | FE+BE |
| TC-FA-LIC-479 | TC-FA-LIC-E2E-024-banner-renewal-muat-ulang-saat-pindah-tab-fokus-jendela | FE+BE |
| TC-FA-LIC-480 | TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss | FE+BE |
| TC-FA-LIC-481 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |
| TC-FA-LIC-482 | TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | FE+BE |
| TC-FA-LIC-483 | TC-FA-LIC-E2E-022-banner-renewal-isi-banner-successor-plan-owner-dan-term-terbaru | FE+BE |
| TC-FA-LIC-484 | TC-FA-LIC-E2E-004-plan-starter-tab-summary-concurrent-user-dan-akses-read | FE+BE |
| TC-FA-LIC-485 | TC-FA-LIC-E2E-027-role-matrix-elemen-baca-license-tab-toolbar-banner-data | FE+BE |
| TC-FA-LIC-486 | TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh | FE+BE |
| TC-FA-LIC-487 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-488 | TC-FA-LIC-E2E-117-registrasi-massal-all-or-nothing-import-dan-used | FE+BE |
| TC-FA-LIC-489 | TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-490 | TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | FE+BE |
| TC-FA-LIC-491 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-492 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-493 | TC-FA-LIC-E2E-120-unmanaged-transisi-manage-dan-konsistensi-used | FE+BE |
| TC-FA-LIC-494 | TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | FE+BE |
| TC-FA-LIC-495 | TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | FE+BE |
| TC-FA-LIC-496 | TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | FE+BE |
| TC-FA-LIC-497 | TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | FE+BE |
| TC-FA-LIC-498 | TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | FE+BE |
| TC-FA-LIC-499 | TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | FE+BE |
| TC-FA-LIC-500 | TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | FE+BE |
| TC-FA-LIC-501 | TC-FA-LIC-E2E-122-aksi-manage-aset-unmanaged-kuota-grup-batas-sisa-slot | FE+BE |
| TC-FA-LIC-503 | TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | FE+BE |
| TC-FA-LIC-504 | TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | FE+BE |
| TC-FA-LIC-505 | TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-506 | TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | FE+BE |
| TC-FA-LIC-507 | TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | FE+BE |
| TC-FA-LIC-508 | TC-FA-LIC-E2E-123-aksi-manage-grup-tanpa-alokasi-over-used-gagal-diproses | FE+BE |
| TC-FA-LIC-509 | TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan | FE+BE |
| TC-FA-LIC-510 | TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | FE+BE |
| TC-FA-LIC-511 | TC-FA-LIC-E2E-087-group-license-allocation-search-numerik-trim-sort | FE+BE |
| TC-FA-LIC-512 | TC-FA-LIC-E2E-088-group-license-allocation-sort-numerik-nilai-kosong-baris | FE+BE |
| TC-FA-LIC-513 | TC-FA-LIC-E2E-089-group-license-allocation-filter-screening-range-min-max | FE+BE |
| TC-FA-LIC-514 | TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | FE+BE |
| TC-FA-LIC-515 | TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | FE+BE |
| TC-FA-LIC-516 | TC-FA-LIC-E2E-078-active-sessions-search-terikat-visibilitas-search | FE+BE |
| TC-FA-LIC-517 | TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit | FE+BE |
| TC-FA-LIC-518 | TC-FA-LIC-E2E-050-remove-allocation-sukses-tanpa-dialog-remaining-leluhur | FE+BE |
| TC-FA-LIC-519 | TC-FA-LIC-E2E-045-edit-allocation-lewat-ikon-summary-dan-edit | FE+BE |
| TC-FA-LIC-520 | TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai | FE+BE |
| TC-FA-LIC-521 | TC-FA-LIC-E2E-017-mobile-filter-panel-bottom-sheet-toolbar-modal-sebagai | FE+BE |
| TC-FA-LIC-522 | TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group | FE+BE |
| TC-FA-LIC-523 | TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari | FE+BE |
| TC-FA-LIC-524 | TC-FA-LIC-E2E-064-subscription-history-filter-date-range-satu-hari | FE+BE |
| TC-FA-LIC-525 | TC-FA-LIC-E2E-023-banner-renewal-dismiss-penyimpanan-state-dismiss | FE+BE |
| TC-FA-LIC-526 | TC-FA-LIC-E2E-038-modal-edit-allocation-copy-dinamis-helper-level-1-tombol | FE+BE |
| TC-FA-LIC-527 | TC-FA-LIC-E2E-010-screening-sub-tab-subscription-history-kolom-isi-baris | FE+BE |
| TC-FA-LIC-528 | TC-FA-LIC-E2E-170-role-matrix-remove-allocation-manage-asset-license-group-manager-default-user | FE+BE |
| TC-FA-LIC-529 | TC-FA-LIC-E2E-170-role-matrix-remove-allocation-manage-asset-license-group-manager-default-user | FE+BE |
| TC-FA-LIC-530 | TC-FA-LIC-E2E-030-role-matrix-scope-edit-descendant-manage-asset-license | FE+BE |
| TC-FA-LIC-531 | TC-FA-LIC-E2E-033-defense-in-depth-request-langsung-tanpa-hak-ditolak-403 | FE+BE |
| TC-FA-LIC-532 | TC-FA-LIC-E2E-145-peringatan-kuota-tenant-penanda-turun-setelah-top-up-dan-penurunan-berikutnya | FE+BE |
| TC-FA-LIC-533 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-534 | TC-FA-LIC-E2E-118-transfer-ke-grup-penuh-edit-remove-allocation-membuka | FE+BE |
| TC-FA-LIC-535 | TC-FA-LIC-E2E-144-sinkron-lintas-modul-grup-terpilih-dihapus-saat-modal-edit-terbuka | FE+BE |
| TC-FA-LIC-536 | TC-FA-LIC-E2E-068-retensi-state-sub-tab-riwayat-dan-tab-license-pindah-tab | FE+BE |
| TC-FA-LIC-537 | TC-FA-LIC-E2E-069-retensi-state-tab-allocation-quota-f5-mempertahankan-node | FE+BE |
| TC-FA-LIC-538 | TC-FA-LIC-E2E-013-tab-allocation-quota-context-header-group-quota-summary | FE+BE |
| TC-FA-LIC-539 | TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle | FE+BE |
| TC-FA-LIC-540 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-541 | TC-FA-LIC-E2E-139-active-sessions-max-visible-columns-dan-siklus-hidup-custom-field | FE+BE |
| TC-FA-LIC-542 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-543 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-544 | TC-FA-LIC-E2E-034-defense-in-depth-sesi-sendiri-dom-dipulihkan-isolasi | FE+BE |
| TC-FA-LIC-545 | TC-FA-LIC-E2E-133-edit-allocation-urutan-penolakan-minimum-quota-menang-atas-maximum | FE+BE |
| TC-FA-LIC-546 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-547 | TC-FA-LIC-E2E-126-peringatan-kuota-tenant-job-per-jam-penilaian-pasca | FE+BE |
| TC-FA-LIC-548 | TC-FA-LIC-E2E-127-peringatan-kuota-tenant-penerima-nonaktif-starter-total-0 | FE+BE |
| TC-FA-LIC-549 | TC-FA-LIC-E2E-036-state-tenant-term-grace-expired-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-549 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-550 | TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter | FE+BE |
| TC-FA-LIC-551 | TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx | FE+BE |
| TC-FA-LIC-552 | TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx | FE+BE |
| TC-FA-LIC-553 | TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter | FE+BE |
| TC-FA-LIC-554 | TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter | FE+BE |
| TC-FA-LIC-555 | TC-FA-LIC-E2E-056-download-allocation-quota-toolbar-section-2-search-filter | FE+BE |
| TC-FA-LIC-556 | TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node | FE+BE |
| TC-FA-LIC-557 | TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node | FE+BE |
| TC-FA-LIC-558 | TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node | FE+BE |
| TC-FA-LIC-559 | TC-FA-LIC-E2E-057-download-allocation-quota-column-visibility-sort-node | FE+BE |
| TC-FA-LIC-560 | TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx | FE+BE |
| TC-FA-LIC-561 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-562 | TC-FA-LIC-E2E-136-role-matrix-download-allocation-quota-read-only-group-manager-manage-asset-license | FE+BE |
| TC-FA-LIC-563 | TC-FA-LIC-E2E-058-isi-berkas-allocation-quota-dua-blok-ditumpuk-xlsx | FE+BE |
| TC-FA-LIC-564 | TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | FE+BE |
| TC-FA-LIC-565 | TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | FE+BE |
| TC-FA-LIC-566 | TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | FE+BE |
| TC-FA-LIC-567 | TC-FA-LIC-E2E-103-changelog-concurrent-user-search-dan-sort | FE+BE |
| TC-FA-LIC-568 | TC-FA-LIC-E2E-103-changelog-concurrent-user-search-dan-sort | FE+BE |
| TC-FA-LIC-569 | TC-FA-LIC-E2E-171-changelog-concurrent-user-sort-date-dan-siklus-tiga-klik | FE+BE |
| TC-FA-LIC-570 | TC-FA-LIC-E2E-171-changelog-concurrent-user-sort-date-dan-siklus-tiga-klik | FE+BE |
| TC-FA-LIC-571 | TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | FE+BE |
| TC-FA-LIC-572 | TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | FE+BE |
| TC-FA-LIC-573 | TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | FE+BE |
| TC-FA-LIC-574 | TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | FE+BE |
| TC-FA-LIC-575 | TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | FE+BE |
| TC-FA-LIC-576 | TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-577 | TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-578 | TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-579 | TC-FA-LIC-E2E-105-changelog-concurrent-user-column-visibility-dan-setup | FE+BE |
| TC-FA-LIC-580 | TC-FA-LIC-E2E-106-changelog-concurrent-user-setup-column-pin-dan-unpin | FE+BE |
| TC-FA-LIC-581 | TC-FA-LIC-E2E-104-changelog-concurrent-user-filter-single-value-guard-opsi | FE+BE |
| TC-FA-LIC-582 | TC-FA-LIC-E2E-106-changelog-concurrent-user-setup-column-pin-dan-unpin | FE+BE |
| TC-FA-LIC-583 | TC-FA-LIC-E2E-060-resilience-download-toast-error-tanpa-ekstensi | FE+BE |
| TC-FA-LIC-584 | TC-FA-LIC-E2E-006-empty-state-client-tanpa-data-21-dan-client-tanpa-alokasi | FE+BE |
| TC-FA-LIC-585 | TC-FA-LIC-E2E-102-changelog-concurrent-user-screening-popup-tutup-isi-entri | FE+BE |
| TC-FA-LIC-586 | TC-FA-LIC-E2E-103-changelog-concurrent-user-search-dan-sort | FE+BE |
| TC-FA-LIC-587 | TC-FA-LIC-E2E-001-screening-halaman-license-plan-paid-breadcrumb-tabs-bar | FE+BE |
| TC-FA-LIC-588 | TC-FA-LIC-E2E-054-download-license-summary-popover-mengabaikan-search | FE+BE |
| TC-FA-LIC-589 | TC-FA-LIC-E2E-009-license-summary-term-trial-total-asset-addon-gating-tab | FE+BE |
| TC-FA-LIC-590 | TC-FA-LIC-E2E-009-license-summary-term-trial-total-asset-addon-gating-tab | FE+BE |
| TC-FA-LIC-591 | TC-FA-LIC-E2E-009-license-summary-term-trial-total-asset-addon-gating-tab | FE+BE |
| TC-FA-LIC-592 | TC-FA-LIC-E2E-003-guided-tooltip-keyboard-trigger-hanya-tab-all-license | FE+BE |
| TC-FA-LIC-593 | TC-FA-LIC-E2E-018-state-tenant-toggle-license-allocation-per-group-off | FE+BE |
| TC-FA-LIC-594 | TC-FA-LIC-E2E-018-state-tenant-toggle-license-allocation-per-group-off | FE+BE |
| TC-FA-LIC-595 | TC-FA-LIC-E2E-008-license-summary-setup-column-baris-unmanaged-dan-used | FE+BE |
| TC-FA-LIC-596 | TC-FA-LIC-E2E-028-role-matrix-force-logout-show-hidden-dan-eksekusi-per-role | FE+BE |
| TC-FA-LIC-597 | TC-FA-LIC-E2E-148-role-matrix-tombol-edit-disabled-manage-asset-license | FE+BE |
| TC-FA-LIC-598 | TC-FA-LIC-E2E-134-edit-allocation-save-tanpa-perubahan-pemakaian-melampaui-alokasi | FE+BE |
| TC-FA-LIC-599 | TC-FA-LIC-E2E-140-active-sessions-nilai-device-os-dan-browser-apa-adanya | FE+BE |
| TC-FA-LIC-600 | TC-FA-LIC-E2E-095-changelog-allocation-quota-empty-state-tanpa-pengaruh | FE+BE |
| TC-FA-LIC-601 | TC-FA-LIC-E2E-142-changelog-allocation-quota-contoh-prd-urutan-penanda-tingkat | FE+BE |
| TC-FA-LIC-602 | TC-FA-LIC-E2E-143-pencatatan-log-cascade-delete-grup-beralokasi | FE+BE |
| TC-FA-LIC-603 | TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan | FE+BE |
| TC-FA-LIC-604 | TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan | FE+BE |
| TC-FA-LIC-605 | TC-FA-LIC-E2E-128-peringatan-kuota-tenant-starter-tanpa-ledger-perubahan | FE+BE |
| TC-FA-LIC-606 | TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage | FE+BE |
| TC-FA-LIC-607 | TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage | FE+BE |
| TC-FA-LIC-608 | TC-FA-LIC-E2E-114-konkurensi-registrasi-arrival-transfer-dan-aksi-manage | FE+BE |
| TC-FA-LIC-609 | TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-611 | TC-FA-LIC-E2E-025-sinkron-konfigurasi-banner-terhadap-renewal-di-admin | FE+BE |
| TC-FA-LIC-612 | TC-FA-LIC-E2E-124-perhitungan-edge-remaining-0-saat-over-used-dan-minimum | FE+BE |
| TC-FA-LIC-613 | TC-FA-LIC-E2E-121-check-group-quota-saat-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-614 | TC-FA-LIC-E2E-036-state-tenant-term-grace-expired-plan-starter-dan-toggle-off | FE+BE |
| TC-FA-LIC-614 | TC-FA-LIC-E2E-111-absence-log-penolakan-request-langsung-403-dan-penolakan | FE+BE |
| TC-FA-LIC-615 | TC-FA-LIC-E2E-115-sesi-lain-force-logout-ganda-sse-concurrent-user-seat | FE+BE |
| TC-FA-LIC-616 | TC-FA-LIC-E2E-168-konkurensi-dua-sesi-registrasi-aset-remove-dan-pool-organisasi | FE+BE |
| TC-FA-LIC-617 | TC-FA-LIC-E2E-020-banner-renewal-stage-expired-grace-dan-banner-tidak-dapat-ditutup | FE+BE |

## TC hanya-BE

Tidak ada. Tidak ada `tc-license-backend.md`, dan seluruh 610 TC masuk spec FE+BE. TC kelas defense-in-depth (permintaan langsung) tetap masuk spec FE+BE dengan butir K-1 di `## Notes`.
