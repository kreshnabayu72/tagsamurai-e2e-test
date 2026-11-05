# Coverage E2E — Fixed Asset > Settings > Role & Permission

Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (1226 TC granular aktif); tidak ada `tc-settings-role-permission-backend.md`, jadi tidak ada TC hanya-BE.
Suite: `specs/FixedAsset/RolePermission/`.
Prefix Modul: `FA` + `RP` (`TC-FA-RP-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (389 Spec)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (1/2) | FE+BE | 38 | TC-FA-RP-1, TC-FA-RP-2, TC-FA-RP-4, TC-FA-RP-5, TC-FA-RP-6 |
| TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | Screening Tab Total Control, Read Only, Group Manager, System, dan loading state (2/2) | FE+BE | 34 | TC-FA-RP-12, TC-FA-RP-13, TC-FA-RP-14, TC-FA-RP-73, TC-FA-RP-74 |
| TC-FA-RP-E2E-003-screening-tab-transaction-role-dan-panel-sub-tab-1 | Screening Tab Transaction Role dan panel sub-tab (1/2) | FE+BE | 24 | TC-FA-RP-7, TC-FA-RP-8, TC-FA-RP-9 |
| TC-FA-RP-E2E-004-screening-tab-transaction-role-dan-panel-sub-tab-2 | Screening Tab Transaction Role dan panel sub-tab (2/2) | FE+BE | 23 | TC-FA-RP-10, TC-FA-RP-11, TC-FA-RP-63 |
| TC-FA-RP-E2E-005-screening-detail-role-matriks-crud-global-role-dan-group-role-1 | Screening Detail Role: matriks CRUD Global Role dan Group Role (1/4) | FE+BE | 13 | TC-FA-RP-16, TC-FA-RP-17, TC-FA-RP-18 |
| TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2 | Screening Detail Role: matriks CRUD Global Role dan Group Role (2/4) | FE+BE | 13 | TC-FA-RP-19, TC-FA-RP-20, TC-FA-RP-21, TC-FA-RP-22 |
| TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | Screening Detail Role: matriks CRUD Global Role dan Group Role (3/4) | FE+BE | 40 | TC-FA-RP-23, TC-FA-RP-24, TC-FA-RP-25, TC-FA-RP-26, TC-FA-RP-27 |
| TC-FA-RP-E2E-008-screening-detail-role-matriks-crud-global-role-dan-group-role-4 | Screening Detail Role: matriks CRUD Global Role dan Group Role (4/4) | FE+BE | 18 | TC-FA-RP-28 |
| TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1 | Sidebar Group Tree: elemen, state, pencarian, dan empty state (1/2) | FE+BE | 33 | TC-FA-RP-29, TC-FA-RP-30, TC-FA-RP-31 |
| TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2 | Sidebar Group Tree: elemen, state, pencarian, dan empty state (2/2) | FE+BE | 14 | TC-FA-RP-32, TC-FA-RP-33, TC-FA-RP-34 |
| TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1 | Screening popup Assign dan mekanik Table User Picker dasar (1/3) | FE+BE | 30 | TC-FA-RP-35, TC-FA-RP-36, TC-FA-RP-37, TC-FA-RP-38 |
| TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2 | Screening popup Assign dan mekanik Table User Picker dasar (2/3) | FE+BE | 31 | TC-FA-RP-39, TC-FA-RP-40, TC-FA-RP-41, TC-FA-RP-42 |
| TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3 | Screening popup Assign dan mekanik Table User Picker dasar (3/3) | FE+BE | 28 | TC-FA-RP-43, TC-FA-RP-44, TC-FA-RP-45 |
| TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | Empty state genuinely pada client tanpa data | FE+BE | 22 | TC-FA-RP-15, TC-FA-RP-46, TC-FA-RP-48, TC-FA-RP-49, TC-FA-RP-50, TC-FA-RP-51, TC-FA-RP-53, TC-FA-RP-54 |
| TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | Empty state hasil pencarian kosong per permukaan (1/2) | FE+BE | 23 | TC-FA-RP-47, TC-FA-RP-55, TC-FA-RP-56, TC-FA-RP-57, TC-FA-RP-58 |
| TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2 | Empty state hasil pencarian kosong per permukaan (2/2) | FE+BE | 21 | TC-FA-RP-59, TC-FA-RP-60, TC-FA-RP-61, TC-FA-RP-62 |
| TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | Resilience baca: Error load dan Try Again per permukaan (1/2) | FE+BE | 36 | TC-FA-RP-64, TC-FA-RP-65, TC-FA-RP-66, TC-FA-RP-67, TC-FA-RP-68 |
| TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2 | Resilience baca: Error load dan Try Again per permukaan (2/2) | FE+BE | 27 | TC-FA-RP-69, TC-FA-RP-70, TC-FA-RP-71 |
| TC-FA-RP-E2E-019-role-matrix-negatif-peran-tanpa-akses-modul | Role Matrix Negatif: peran tanpa akses modul | FE+BE | 10 | TC-FA-RP-75, TC-FA-RP-76 |
| TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | Role Matrix: menu Role & Permission dan tab awal per peran (1/2) | FE+BE | 20 | TC-FA-RP-3, TC-FA-RP-77, TC-FA-RP-78, TC-FA-RP-79, TC-FA-RP-82 |
| TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2 | Role Matrix: menu Role & Permission dan tab awal per peran (2/2) | FE+BE | 14 | TC-FA-RP-80, TC-FA-RP-81, TC-FA-RP-83 |
| TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1 | Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (1/3) | FE+BE | 29 | TC-FA-RP-84, TC-FA-RP-85, TC-FA-RP-86 |
| TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2 | Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (2/3) | FE+BE | 36 | TC-FA-RP-87, TC-FA-RP-88, TC-FA-RP-89 |
| TC-FA-RP-E2E-024-role-matrix-kontrol-tab-total-control-read-only-dan-group-3 | Role Matrix: kontrol Tab Total Control, Read Only, dan Group Manager per peran (3/3) | FE+BE | 17 | TC-FA-RP-90 |
| TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1 | Role Matrix: kontrol Detail Role Global Role per peran (1/2) | FE+BE | 27 | TC-FA-RP-91, TC-FA-RP-92, TC-FA-RP-93 |
| TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2 | Role Matrix: kontrol Detail Role Global Role per peran (2/2) | FE+BE | 35 | TC-FA-RP-94, TC-FA-RP-95, TC-FA-RP-96, TC-FA-RP-97 |
| TC-FA-RP-E2E-027-role-matrix-kontrol-detail-role-group-role-per-peran-1 | Role Matrix: kontrol Detail Role Group Role per peran (1/3) | FE+BE | 35 | TC-FA-RP-98, TC-FA-RP-99, TC-FA-RP-100 |
| TC-FA-RP-E2E-028-role-matrix-kontrol-detail-role-group-role-per-peran-2 | Role Matrix: kontrol Detail Role Group Role per peran (2/3) | FE+BE | 35 | TC-FA-RP-101, TC-FA-RP-102, TC-FA-RP-103 |
| TC-FA-RP-E2E-029-role-matrix-kontrol-detail-role-group-role-per-peran-3 | Role Matrix: kontrol Detail Role Group Role per peran (3/3) | FE+BE | 11 | TC-FA-RP-104 |
| TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1 | Role Matrix: kontrol Tab Transaction Role per peran (1/2) | FE+BE | 37 | TC-FA-RP-105, TC-FA-RP-106, TC-FA-RP-107, TC-FA-RP-108 |
| TC-FA-RP-E2E-031-role-matrix-kontrol-tab-transaction-role-per-peran-2 | Role Matrix: kontrol Tab Transaction Role per peran (2/2) | FE+BE | 30 | TC-FA-RP-109, TC-FA-RP-110, TC-FA-RP-111 |
| TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1 | Role Matrix: Panel Approval Settings Registration per peran (1/2) | FE+BE | 24 | TC-FA-RP-112, TC-FA-RP-113, TC-FA-RP-114, TC-FA-RP-115 |
| TC-FA-RP-E2E-033-role-matrix-panel-approval-settings-registration-per-peran-2 | Role Matrix: Panel Approval Settings Registration per peran (2/2) | FE+BE | 19 | TC-FA-RP-116, TC-FA-RP-117, TC-FA-RP-118 |
| TC-FA-RP-E2E-034-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-1 | Role Matrix: Changelog dan Download terfilter ke cakupan group per peran (1/2) | FE+BE | 17 | TC-FA-RP-120, TC-FA-RP-121 |
| TC-FA-RP-E2E-035-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-2 | Role Matrix: Download Tab Total Control dan Read Only terfilter ke cakupan Home Group (2/2) | FE+BE | 26 | TC-FA-RP-1110, TC-FA-RP-1114 |
| TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (1/2) | FE+BE | 34 | TC-FA-RP-122, TC-FA-RP-123, TC-FA-RP-124, TC-FA-RP-127, TC-FA-RP-128 |
| TC-FA-RP-E2E-037-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-2 | Role Matrix: Sidebar Group Tree dan data tabel sesuai cakupan peran (2/2) | FE+BE | 10 | TC-FA-RP-125, TC-FA-RP-126, TC-FA-RP-1018 |
| TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (1/2) | FE+BE | 16 | TC-FA-RP-129, TC-FA-RP-130, TC-FA-RP-131, TC-FA-RP-132, TC-FA-RP-133 |
| TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | Role Matrix: guard target terlindungi oleh Manage global user & role (Update) (2/2) | FE+BE | 25 | TC-FA-RP-134, TC-FA-RP-135, TC-FA-RP-136, TC-FA-RP-137, TC-FA-RP-138 |
| TC-FA-RP-E2E-040-role-matrix-guard-target-terlindungi-oleh-group-manager-1 | Role Matrix: guard target terlindungi oleh Group Manager (1/2) | FE+BE | 12 | TC-FA-RP-139, TC-FA-RP-140, TC-FA-RP-141 |
| TC-FA-RP-E2E-041-role-matrix-guard-target-terlindungi-oleh-group-manager-2 | Role Matrix: guard target terlindungi oleh Group Manager (2/2) | FE+BE | 22 | TC-FA-RP-142, TC-FA-RP-143, TC-FA-RP-144 |
| TC-FA-RP-E2E-042-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-1 | Role Matrix: guard target terlindungi oleh Manage user & role (Group, Update) (1/2) | FE+BE | 12 | TC-FA-RP-145, TC-FA-RP-146, TC-FA-RP-147 |
| TC-FA-RP-E2E-043-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-2 | Role Matrix: guard target terlindungi oleh Manage user & role (Group, Update) (2/2) | FE+BE | 22 | TC-FA-RP-148, TC-FA-RP-149, TC-FA-RP-150 |
| TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | Role Matrix: guard target terlindungi oleh Total Control dan Default User (1/2) | FE+BE | 25 | TC-FA-RP-151, TC-FA-RP-152, TC-FA-RP-153, TC-FA-RP-154, TC-FA-RP-155 |
| TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2 | Role Matrix: guard target terlindungi oleh Total Control dan Default User (2/2) | FE+BE | 24 | TC-FA-RP-156, TC-FA-RP-157, TC-FA-RP-158, TC-FA-RP-159 |
| TC-FA-RP-E2E-046-role-matrix-gating-remove-tabel-role-transaksi-per-peran | Role Matrix: gating Remove tabel Role Transaksi per peran | FE+BE | 35 | TC-FA-RP-160, TC-FA-RP-161, TC-FA-RP-162 |
| TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (1/2) | FE+BE | 34 | TC-FA-RP-163, TC-FA-RP-164, TC-FA-RP-165, TC-FA-RP-166 |
| TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage global user & role (Update) (2/2) | FE+BE | 20 | TC-FA-RP-167, TC-FA-RP-168, TC-FA-RP-169, TC-FA-RP-170 |
| TC-FA-RP-E2E-049-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage user & role (Group, Update) (1/2) | FE+BE | 35 | TC-FA-RP-171, TC-FA-RP-172, TC-FA-RP-173, TC-FA-RP-174 |
| TC-FA-RP-E2E-050-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Manage user & role (Group, Update) (2/2) | FE+BE | 20 | TC-FA-RP-175, TC-FA-RP-176, TC-FA-RP-177, TC-FA-RP-178 |
| TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Group Manager (1/2) | FE+BE | 35 | TC-FA-RP-179, TC-FA-RP-180, TC-FA-RP-181, TC-FA-RP-182 |
| TC-FA-RP-E2E-052-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-2 | Role Matrix Positif: eksekusi aksi sampai sukses oleh Group Manager (2/2) | FE+BE | 20 | TC-FA-RP-183, TC-FA-RP-184, TC-FA-RP-185, TC-FA-RP-186 |
| TC-FA-RP-E2E-053-aktor-ganda-group-manager-dan-manage-user-dan-role-pada-scope | Role Matrix: Aktor ganda Group Manager dan Manage user & role pada scope berbeda | FE+BE | 13 | TC-FA-RP-1026 |
| TC-FA-RP-E2E-054-changelog-dan-download-entri-remove-group-deleted-per-cakupan-1 | Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (1/3) | FE+BE | 22 | TC-FA-RP-1111, TC-FA-RP-1115 |
| TC-FA-RP-E2E-055-changelog-dan-download-entri-remove-group-deleted-per-cakupan-2 | Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (2/3) | FE+BE | 37 | TC-FA-RP-1112, TC-FA-RP-1116, TC-FA-RP-1120 |
| TC-FA-RP-E2E-056-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-1 | Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (1/3) | FE+BE | 40 | TC-FA-RP-187, TC-FA-RP-188, TC-FA-RP-189 |
| TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2 | Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (2/3) | FE+BE | 53 | TC-FA-RP-190, TC-FA-RP-191, TC-FA-RP-192, TC-FA-RP-199 |
| TC-FA-RP-E2E-058-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-3 | Assign Total Control: satu atau banyak user, timpa parsial, dan upgrade dari Read Only (3/3) | FE+BE | 34 | TC-FA-RP-1085, TC-FA-RP-1139 |
| TC-FA-RP-E2E-059-assign-read-only-1 | Assign Read Only (1/2) | FE+BE | 53 | TC-FA-RP-193, TC-FA-RP-194, TC-FA-RP-195, TC-FA-RP-196 |
| TC-FA-RP-E2E-060-assign-read-only-2 | Assign Read Only (2/2) | FE+BE | 45 | TC-FA-RP-197, TC-FA-RP-198, TC-FA-RP-200 |
| TC-FA-RP-E2E-061-remove-total-control-1 | Remove Total Control (1/3) | FE+BE | 41 | TC-FA-RP-205, TC-FA-RP-206, TC-FA-RP-208, TC-FA-RP-209, TC-FA-RP-210 |
| TC-FA-RP-E2E-062-remove-total-control-2 | Remove Total Control (2/3) | FE+BE | 45 | TC-FA-RP-217, TC-FA-RP-1086, TC-FA-RP-1127, TC-FA-RP-1129 |
| TC-FA-RP-E2E-063-remove-total-control-3 | Remove Total Control (3/3) | FE+BE | 25 | TC-FA-RP-1131, TC-FA-RP-1133 |
| TC-FA-RP-E2E-064-remove-read-only-1 | Remove Read Only (1/2) | FE+BE | 43 | TC-FA-RP-211, TC-FA-RP-212, TC-FA-RP-214, TC-FA-RP-215, TC-FA-RP-216 |
| TC-FA-RP-E2E-065-remove-read-only-2 | Remove Read Only (2/2) | FE+BE | 36 | TC-FA-RP-218, TC-FA-RP-1128, TC-FA-RP-1132 |
| TC-FA-RP-E2E-066-assign-group-manager-1 | Assign Group Manager (1/4) | FE+BE | 43 | TC-FA-RP-219, TC-FA-RP-220, TC-FA-RP-221, TC-FA-RP-222 |
| TC-FA-RP-E2E-067-assign-group-manager-2 | Assign Group Manager (2/4) | FE+BE | 43 | TC-FA-RP-223, TC-FA-RP-224, TC-FA-RP-225, TC-FA-RP-226, TC-FA-RP-227 |
| TC-FA-RP-E2E-068-assign-group-manager-3 | Assign Group Manager (3/4) | FE+BE | 46 | TC-FA-RP-228, TC-FA-RP-229, TC-FA-RP-231, TC-FA-RP-234, TC-FA-RP-1037 |
| TC-FA-RP-E2E-069-assign-group-manager-4 | Assign Group Manager (4/4) | FE+BE | 17 | TC-FA-RP-232, TC-FA-RP-233 |
| TC-FA-RP-E2E-070-remove-group-manager-1 | Remove Group Manager (1/2) | FE+BE | 46 | TC-FA-RP-235, TC-FA-RP-236, TC-FA-RP-237, TC-FA-RP-240, TC-FA-RP-1017 |
| TC-FA-RP-E2E-071-remove-group-manager-2 | Remove Group Manager (2/2) | FE+BE | 36 | TC-FA-RP-238, TC-FA-RP-1036 |
| TC-FA-RP-E2E-072-assign-user-ke-global-role-di-detail-role | Assign User ke Global Role di Detail Role (1/2) | FE+BE | 24 | TC-FA-RP-241, TC-FA-RP-242, TC-FA-RP-243 |
| TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | Assign User ke Group Role di Detail Role (1/4) | FE+BE | 54 | TC-FA-RP-247, TC-FA-RP-248, TC-FA-RP-249, TC-FA-RP-250, TC-FA-RP-251, TC-FA-RP-252 |
| TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | Assign User ke Group Role di Detail Role (2/4) | FE+BE | 22 | TC-FA-RP-255, TC-FA-RP-256, TC-FA-RP-257, TC-FA-RP-258, TC-FA-RP-259, TC-FA-RP-260 |
| TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | Assign User ke Group Role di Detail Role (3/4) | FE+BE | 52 | TC-FA-RP-261, TC-FA-RP-263, TC-FA-RP-1087, TC-FA-RP-1088, TC-FA-RP-1141 |
| TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4 | Assign User ke Group Role di Detail Role (4/4) | FE+BE | 39 | TC-FA-RP-253, TC-FA-RP-254, TC-FA-RP-262, TC-FA-RP-1142 |
| TC-FA-RP-E2E-077-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-1 | Eksklusivitas Manage user & role dan Manage global user & role (1/2) | FE+BE | 43 | TC-FA-RP-1043, TC-FA-RP-1044, TC-FA-RP-1046 |
| TC-FA-RP-E2E-078-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-2 | Eksklusivitas Manage user & role dan Manage global user & role (2/2) | FE+BE | 31 | TC-FA-RP-1047, TC-FA-RP-1048, TC-FA-RP-1049 |
| TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1 | Edit matriks CRUD Detail Role (1/3) | FE+BE | 37 | TC-FA-RP-265, TC-FA-RP-266, TC-FA-RP-267, TC-FA-RP-268 |
| TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | Edit matriks CRUD Detail Role (2/3) | FE+BE | 45 | TC-FA-RP-269, TC-FA-RP-270, TC-FA-RP-271, TC-FA-RP-272, TC-FA-RP-273 |
| TC-FA-RP-E2E-081-edit-matriks-crud-detail-role-3 | Edit matriks CRUD Detail Role (3/3) | FE+BE | 15 | TC-FA-RP-277, TC-FA-RP-278 |
| TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1 | Remove baris peran satu per satu (1/2) | FE+BE | 25 | TC-FA-RP-279, TC-FA-RP-280, TC-FA-RP-281, TC-FA-RP-282 |
| TC-FA-RP-E2E-083-remove-baris-peran-satu-per-satu-2 | Remove baris peran satu per satu (2/2) | FE+BE | 23 | TC-FA-RP-283, TC-FA-RP-1016 |
| TC-FA-RP-E2E-084-checkbox-seleksi-baris-terlindungi | Checkbox seleksi baris terlindungi | FE+BE | 20 | TC-FA-RP-292, TC-FA-RP-293, TC-FA-RP-294 |
| TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | Bulk Remove: dialog, hasil, dan Cancel (1/2) | FE+BE | 47 | TC-FA-RP-295, TC-FA-RP-296, TC-FA-RP-297, TC-FA-RP-298, TC-FA-RP-301 |
| TC-FA-RP-E2E-086-bulk-remove-dialog-hasil-dan-cancel-2 | Bulk Remove: dialog, hasil, dan Cancel (2/2) | FE+BE | 28 | TC-FA-RP-304, TC-FA-RP-1010 |
| TC-FA-RP-E2E-087-volume-data-company-volume-seleksi-bulk-selection-limit-dan-1 | Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (1/4) | FE+BE | 34 | TC-FA-RP-286, TC-FA-RP-287, TC-FA-RP-288 |
| TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (2/4) | FE+BE | 35 | TC-FA-RP-289, TC-FA-RP-290, TC-FA-RP-291, TC-FA-RP-420, TC-FA-RP-657 |
| TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3 | Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (3/4) | FE+BE | 48 | TC-FA-RP-658, TC-FA-RP-659, TC-FA-RP-660, TC-FA-RP-792 |
| TC-FA-RP-E2E-090-volume-data-company-volume-seleksi-bulk-selection-limit-dan-4 | Volume data Company Volume: seleksi Bulk, Selection Limit, dan pagination Detail Role (4/4) | FE+BE | 10 | TC-FA-RP-943, TC-FA-RP-944, TC-FA-RP-971 |
| TC-FA-RP-E2E-091-volume-data-company-export-download-changelog-di-atas-5-000 | Volume data Company Export: Download Changelog di atas 5.000 baris | FE+BE | 10 | TC-FA-RP-755 |
| TC-FA-RP-E2E-092-mobile-mode-checkbox-floating-bottom-bulk-bar-dan-select-all | Mobile: mode checkbox, Floating Bottom Bulk Bar, dan Select All | FE+BE | 24 | TC-FA-RP-305, TC-FA-RP-306, TC-FA-RP-307 |
| TC-FA-RP-E2E-093-mobile-chip-group-dan-tooltip-elemen-disabled | Mobile: chip Group dan tooltip elemen Disabled | FE+BE | 16 | TC-FA-RP-1028, TC-FA-RP-1099 |
| TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | Assign Role Transaksi: pemilihan role dan kandidat picker (1/4) | FE+BE | 33 | TC-FA-RP-308, TC-FA-RP-309, TC-FA-RP-310, TC-FA-RP-311, TC-FA-RP-312 |
| TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2 | Assign Role Transaksi: pemilihan role dan kandidat picker (2/4) | FE+BE | 48 | TC-FA-RP-313, TC-FA-RP-314, TC-FA-RP-315, TC-FA-RP-316 |
| TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3 | Assign Role Transaksi: pemilihan role dan kandidat picker (3/4) | FE+BE | 46 | TC-FA-RP-317, TC-FA-RP-319, TC-FA-RP-1121, TC-FA-RP-1122 |
| TC-FA-RP-E2E-097-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-4 | Assign Role Transaksi: pemilihan role dan kandidat picker (4/4) | FE+BE | 47 | TC-FA-RP-1123, TC-FA-RP-1124 |
| TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1 | Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (1/2) | FE+BE | 31 | TC-FA-RP-320, TC-FA-RP-321, TC-FA-RP-322, TC-FA-RP-323 |
| TC-FA-RP-E2E-099-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-2 | Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (2/2) | FE+BE | 18 | TC-FA-RP-324, TC-FA-RP-325, TC-FA-RP-1117 |
| TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1 | Role Transaksi: node exact, sub-tab, dan Remove (1/2) | FE+BE | 35 | TC-FA-RP-326, TC-FA-RP-327, TC-FA-RP-328, TC-FA-RP-329 |
| TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2 | Role Transaksi: node exact, sub-tab, dan Remove (2/2) | FE+BE | 21 | TC-FA-RP-330, TC-FA-RP-331, TC-FA-RP-332, TC-FA-RP-335 |
| TC-FA-RP-E2E-102-require-approval-transaction-role-prasyarat-aktivasi-1 | Require Approval Transaction Role: prasyarat aktivasi (1/2) | FE+BE | 19 | TC-FA-RP-336, TC-FA-RP-338, TC-FA-RP-339 |
| TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2 | Require Approval Transaction Role: prasyarat aktivasi (2/2) | FE+BE | 26 | TC-FA-RP-340, TC-FA-RP-341, TC-FA-RP-342, TC-FA-RP-1094 |
| TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1 | Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (1/3) | FE+BE | 28 | TC-FA-RP-337, TC-FA-RP-343, TC-FA-RP-344, TC-FA-RP-346 |
| TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2 | Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (2/3) | FE+BE | 24 | TC-FA-RP-348, TC-FA-RP-349, TC-FA-RP-355, TC-FA-RP-360 |
| TC-FA-RP-E2E-106-approval-scope-sub-tab-transfer-1 | Approval Scope sub-tab Transfer (1/2) | FE+BE | 32 | TC-FA-RP-356, TC-FA-RP-357, TC-FA-RP-359 |
| TC-FA-RP-E2E-107-approval-scope-sub-tab-transfer-2 | Approval Scope sub-tab Transfer (2/2) | FE+BE | 28 | TC-FA-RP-1019, TC-FA-RP-1020, TC-FA-RP-1021 |
| TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | Persetujuan registrasi aset: aktivasi toggle dan prasyarat (1/2) | FE+BE | 24 | TC-FA-RP-361, TC-FA-RP-362, TC-FA-RP-363, TC-FA-RP-364, TC-FA-RP-371 |
| TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2 | Persetujuan registrasi aset: aktivasi toggle dan prasyarat (2/2) | FE+BE | 36 | TC-FA-RP-1031, TC-FA-RP-1032, TC-FA-RP-1033, TC-FA-RP-1034 |
| TC-FA-RP-E2E-110-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-1 | Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (1/2) | FE+BE | 27 | TC-FA-RP-374, TC-FA-RP-375, TC-FA-RP-376 |
| TC-FA-RP-E2E-111-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-2 | Persetujuan registrasi aset: D-09 saat uncheck Update dan Remove pemegang Update (2/2) | FE+BE | 33 | TC-FA-RP-377, TC-FA-RP-378, TC-FA-RP-379 |
| TC-FA-RP-E2E-112-auto-revert-total-control-1 | Auto-Revert Total Control (1/3) | FE+BE | 29 | TC-FA-RP-380, TC-FA-RP-381, TC-FA-RP-382 |
| TC-FA-RP-E2E-113-auto-revert-total-control-2 | Auto-Revert Total Control (2/3) | FE+BE | 48 | TC-FA-RP-383, TC-FA-RP-384, TC-FA-RP-390, TC-FA-RP-394 |
| TC-FA-RP-E2E-114-auto-revert-total-control-3 | Auto-Revert Total Control (3/3) | FE+BE | 19 | TC-FA-RP-393, TC-FA-RP-1137 |
| TC-FA-RP-E2E-115-auto-revert-read-only-1 | Auto-Revert Read Only (1/2) | FE+BE | 29 | TC-FA-RP-385, TC-FA-RP-386, TC-FA-RP-387 |
| TC-FA-RP-E2E-116-auto-revert-read-only-2 | Auto-Revert Read Only (2/2) | FE+BE | 28 | TC-FA-RP-388, TC-FA-RP-389 |
| TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1 | Auto-Revert Group Manager dan pola subset baris eksplisit (1/2) | FE+BE | 38 | TC-FA-RP-395, TC-FA-RP-396, TC-FA-RP-398 |
| TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2 | Auto-Revert Group Manager dan pola subset baris eksplisit (2/2) | FE+BE | 39 | TC-FA-RP-399, TC-FA-RP-400, TC-FA-RP-401, TC-FA-RP-1042 |
| TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | Home Group constraint: dialog D-10 dan pencabutan assignment (1/3) | FE+BE | 42 | TC-FA-RP-402, TC-FA-RP-403, TC-FA-RP-404, TC-FA-RP-405, TC-FA-RP-406 |
| TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | Home Group constraint: dialog D-10 dan pencabutan assignment (2/3) | FE+BE | 55 | TC-FA-RP-407, TC-FA-RP-408, TC-FA-RP-409, TC-FA-RP-410, TC-FA-RP-412, TC-FA-RP-1039 |
| TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3 | Home Group constraint: dialog D-10 dan pencabutan assignment (3/3) | FE+BE | 51 | TC-FA-RP-411, TC-FA-RP-1040, TC-FA-RP-1041, TC-FA-RP-1097 |
| TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1 | Table User Picker: kontrak submit stale dan tidak eligible (1/2) | FE+BE | 36 | TC-FA-RP-413, TC-FA-RP-414, TC-FA-RP-415, TC-FA-RP-416 |
| TC-FA-RP-E2E-123-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-2 | Table User Picker: kontrak submit stale dan tidak eligible (2/2) | FE+BE | 25 | TC-FA-RP-417, TC-FA-RP-418, TC-FA-RP-419 |
| TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | Popup Assign: penutupan, Saving state, dan aksesibilitas | FE+BE | 38 | TC-FA-RP-421, TC-FA-RP-422, TC-FA-RP-423, TC-FA-RP-424, TC-FA-RP-425 |
| TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (1/4) | FE+BE | 43 | TC-FA-RP-426, TC-FA-RP-427, TC-FA-RP-428, TC-FA-RP-429, TC-FA-RP-430 |
| TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (2/4) | FE+BE | 46 | TC-FA-RP-431, TC-FA-RP-432, TC-FA-RP-433, TC-FA-RP-434, TC-FA-RP-435 |
| TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3 | Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (3/4) | FE+BE | 40 | TC-FA-RP-436, TC-FA-RP-437, TC-FA-RP-438, TC-FA-RP-439 |
| TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4 | Popup Assign per jenis: alert tanpa seleksi, stale, dan tidak eligible (4/4) | FE+BE | 36 | TC-FA-RP-440, TC-FA-RP-1089, TC-FA-RP-1090, TC-FA-RP-1091 |
| TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | Penugasan otomatis pembuat Group | FE+BE | 29 | TC-FA-RP-442, TC-FA-RP-443, TC-FA-RP-444, TC-FA-RP-445, TC-FA-RP-446 |
| TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait | Delete Group: pelepasan penugasan dan nilai terkait | FE+BE | 35 | TC-FA-RP-448, TC-FA-RP-449, TC-FA-RP-469, TC-FA-RP-470 |
| TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (1/3) | FE+BE | 41 | TC-FA-RP-450, TC-FA-RP-451, TC-FA-RP-452, TC-FA-RP-453, TC-FA-RP-454, TC-FA-RP-455 |
| TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (2/3) | FE+BE | 38 | TC-FA-RP-456, TC-FA-RP-457, TC-FA-RP-458, TC-FA-RP-459, TC-FA-RP-460 |
| TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | Konfirmasi Remove last approver D-09 pada Role Transaksi dan Group Manager (3/3) | FE+BE | 48 | TC-FA-RP-1011, TC-FA-RP-1012, TC-FA-RP-1095, TC-FA-RP-1096, TC-FA-RP-1138 |
| TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | Sub-tab Addon dengan lisensi nonaktif dan aktif | FE+BE | 34 | TC-FA-RP-462, TC-FA-RP-463, TC-FA-RP-464, TC-FA-RP-465, TC-FA-RP-466, TC-FA-RP-467 |
| TC-FA-RP-E2E-135-tab-total-control-search-1 | Tab Total Control: Search (1/4) | FE+BE | 22 | TC-FA-RP-471 |
| TC-FA-RP-E2E-136-tab-total-control-search-2 | Tab Total Control: Search (2/4) | FE+BE | 41 | TC-FA-RP-472, TC-FA-RP-473 |
| TC-FA-RP-E2E-137-tab-total-control-search-3 | Tab Total Control: Search (3/4) | FE+BE | 37 | TC-FA-RP-474, TC-FA-RP-475, TC-FA-RP-476, TC-FA-RP-477, TC-FA-RP-478 |
| TC-FA-RP-E2E-138-tab-total-control-search-4 | Tab Total Control: Search (4/4) | FE+BE | 31 | TC-FA-RP-479, TC-FA-RP-1060, TC-FA-RP-1061, TC-FA-RP-1104 |
| TC-FA-RP-E2E-139-tab-total-control-filter-1 | Tab Total Control: Filter (1/4) | FE+BE | 16 | TC-FA-RP-480, TC-FA-RP-481, TC-FA-RP-482 |
| TC-FA-RP-E2E-140-tab-total-control-filter-2 | Tab Total Control: Filter (2/4) | FE+BE | 37 | TC-FA-RP-483, TC-FA-RP-484, TC-FA-RP-485, TC-FA-RP-486 |
| TC-FA-RP-E2E-141-tab-total-control-filter-3 | Tab Total Control: Filter (3/4) | FE+BE | 30 | TC-FA-RP-487, TC-FA-RP-488, TC-FA-RP-489, TC-FA-RP-490, TC-FA-RP-491 |
| TC-FA-RP-E2E-142-tab-total-control-filter-4 | Tab Total Control: Filter (4/4) | FE+BE | 35 | TC-FA-RP-492, TC-FA-RP-493, TC-FA-RP-494, TC-FA-RP-495 |
| TC-FA-RP-E2E-143-tab-total-control-sort-1 | Tab Total Control: Sort (1/2) | FE+BE | 19 | TC-FA-RP-496, TC-FA-RP-497, TC-FA-RP-498, TC-FA-RP-499 |
| TC-FA-RP-E2E-144-tab-total-control-sort-2 | Tab Total Control: Sort (2/2) | FE+BE | 17 | TC-FA-RP-500, TC-FA-RP-501, TC-FA-RP-502, TC-FA-RP-1059 |
| TC-FA-RP-E2E-145-tab-total-control-setup-column-1 | Tab Total Control: Setup Column (1/5) | FE+BE | 24 | TC-FA-RP-503, TC-FA-RP-504, TC-FA-RP-505 |
| TC-FA-RP-E2E-146-tab-total-control-setup-column-2 | Tab Total Control: Setup Column (2/5) | FE+BE | 24 | TC-FA-RP-506, TC-FA-RP-507 |
| TC-FA-RP-E2E-147-tab-total-control-setup-column-3 | Tab Total Control: Setup Column (3/5) | FE+BE | 26 | TC-FA-RP-508, TC-FA-RP-509 |
| TC-FA-RP-E2E-148-tab-total-control-setup-column-4 | Tab Total Control: Setup Column (4/5) | FE+BE | 30 | TC-FA-RP-510, TC-FA-RP-511, TC-FA-RP-512 |
| TC-FA-RP-E2E-149-tab-total-control-setup-column-5 | Tab Total Control: Setup Column (5/5) | FE+BE | 10 | TC-FA-RP-513, TC-FA-RP-514 |
| TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman | Tab Total Control: Pagination dan state halaman | FE+BE | 37 | TC-FA-RP-515, TC-FA-RP-516, TC-FA-RP-517, TC-FA-RP-518 |
| TC-FA-RP-E2E-151-tab-total-control-download-1 | Tab Total Control: Download (1/2) | FE+BE | 21 | TC-FA-RP-519, TC-FA-RP-520, TC-FA-RP-521 |
| TC-FA-RP-E2E-152-tab-total-control-download-2 | Tab Total Control: Download (2/2) | FE+BE | 16 | TC-FA-RP-522, TC-FA-RP-524, TC-FA-RP-526 |
| TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | Tab Total Control: kombinasi Search, Filter, Sort, Pagination | FE+BE | 28 | TC-FA-RP-527, TC-FA-RP-528, TC-FA-RP-529, TC-FA-RP-530, TC-FA-RP-531 |
| TC-FA-RP-E2E-154-tab-total-control-isi-sel-dan-badge-1 | Tab Total Control: isi sel dan badge (1/2) | FE+BE | 27 | TC-FA-RP-1014, TC-FA-RP-1022, TC-FA-RP-1023 |
| TC-FA-RP-E2E-155-tab-total-control-isi-sel-dan-badge-2 | Tab Total Control: isi sel dan badge (2/2) | FE+BE | 19 | TC-FA-RP-1100, TC-FA-RP-1101 |
| TC-FA-RP-E2E-156-tab-read-only-search-filter-sort-download-setup-column-dan-1 | Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (1/2) | FE+BE | 20 | TC-FA-RP-532, TC-FA-RP-533, TC-FA-RP-534 |
| TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2 | Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (2/2) | FE+BE | 24 | TC-FA-RP-535, TC-FA-RP-536, TC-FA-RP-537, TC-FA-RP-538 |
| TC-FA-RP-E2E-158-tab-group-manager-search-1 | Tab Group Manager: Search (1/3) | FE+BE | 29 | TC-FA-RP-539, TC-FA-RP-540, TC-FA-RP-541 |
| TC-FA-RP-E2E-159-tab-group-manager-search-2 | Tab Group Manager: Search (2/3) | FE+BE | 26 | TC-FA-RP-542, TC-FA-RP-543, TC-FA-RP-544, TC-FA-RP-1064 |
| TC-FA-RP-E2E-160-tab-group-manager-search-3 | Tab Group Manager: Search (3/3) | FE+BE | 26 | TC-FA-RP-1065, TC-FA-RP-1093, TC-FA-RP-1105 |
| TC-FA-RP-E2E-161-tab-group-manager-filter-1 | Tab Group Manager: Filter (1/2) | FE+BE | 17 | TC-FA-RP-545, TC-FA-RP-546, TC-FA-RP-547 |
| TC-FA-RP-E2E-162-tab-group-manager-filter-2 | Tab Group Manager: Filter (2/2) | FE+BE | 17 | TC-FA-RP-548, TC-FA-RP-1066, TC-FA-RP-1067 |
| TC-FA-RP-E2E-163-tab-group-manager-sort | Tab Group Manager: Sort | FE+BE | 12 | TC-FA-RP-549, TC-FA-RP-550, TC-FA-RP-1062, TC-FA-RP-1063 |
| TC-FA-RP-E2E-164-tab-group-manager-setup-column-1 | Tab Group Manager: Setup Column (1/5) | FE+BE | 22 | TC-FA-RP-551, TC-FA-RP-552, TC-FA-RP-553 |
| TC-FA-RP-E2E-165-tab-group-manager-setup-column-2 | Tab Group Manager: Setup Column (2/5) | FE+BE | 20 | TC-FA-RP-554, TC-FA-RP-555 |
| TC-FA-RP-E2E-166-tab-group-manager-setup-column-3 | Tab Group Manager: Setup Column (3/5) | FE+BE | 21 | TC-FA-RP-556, TC-FA-RP-557 |
| TC-FA-RP-E2E-167-tab-group-manager-setup-column-4 | Tab Group Manager: Setup Column (4/5) | FE+BE | 35 | TC-FA-RP-558, TC-FA-RP-559, TC-FA-RP-560, TC-FA-RP-561 |
| TC-FA-RP-E2E-168-tab-group-manager-setup-column-5 | Tab Group Manager: Setup Column (5/5) | FE+BE | 36 | TC-FA-RP-562, TC-FA-RP-1068, TC-FA-RP-1069, TC-FA-RP-1070 |
| TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman | Tab Group Manager: Pagination dan state halaman | FE+BE | 33 | TC-FA-RP-563, TC-FA-RP-564, TC-FA-RP-565, TC-FA-RP-566 |
| TC-FA-RP-E2E-170-tab-group-manager-download-1 | Tab Group Manager: Download (1/2) | FE+BE | 20 | TC-FA-RP-567, TC-FA-RP-568, TC-FA-RP-569, TC-FA-RP-570 |
| TC-FA-RP-E2E-171-tab-group-manager-download-2 | Tab Group Manager: Download (2/2) | FE+BE | 24 | TC-FA-RP-572, TC-FA-RP-574, TC-FA-RP-1004 |
| TC-FA-RP-E2E-172-tab-group-manager-sidebar-group-tree-dan-menu-baris | Tab Group Manager: Sidebar Group Tree dan menu baris | FE+BE | 12 | TC-FA-RP-575, TC-FA-RP-576 |
| TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1 | Tab System: Search, Setup Column, Download, dan state (1/4) | FE+BE | 35 | TC-FA-RP-577, TC-FA-RP-578, TC-FA-RP-579, TC-FA-RP-580 |
| TC-FA-RP-E2E-174-tab-system-search-setup-column-download-dan-state-2 | Tab System: Search, Setup Column, Download, dan state (2/4) | FE+BE | 26 | TC-FA-RP-581, TC-FA-RP-582, TC-FA-RP-583 |
| TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3 | Tab System: Search, Setup Column, Download, dan state (3/4) | FE+BE | 34 | TC-FA-RP-584, TC-FA-RP-585, TC-FA-RP-586, TC-FA-RP-587 |
| TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4 | Tab System: Search, Setup Column, Download, dan state (4/4) | FE+BE | 26 | TC-FA-RP-588, TC-FA-RP-589, TC-FA-RP-590, TC-FA-RP-592 |
| TC-FA-RP-E2E-177-tabel-role-transaksi-search-filter-dan-sort-1 | Tabel Role Transaksi: Search, Filter, dan Sort (1/4) | FE+BE | 34 | TC-FA-RP-593, TC-FA-RP-594, TC-FA-RP-595 |
| TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2 | Tabel Role Transaksi: Search, Filter, dan Sort (2/4) | FE+BE | 21 | TC-FA-RP-596, TC-FA-RP-597, TC-FA-RP-598, TC-FA-RP-599 |
| TC-FA-RP-E2E-179-tabel-role-transaksi-search-filter-dan-sort-3 | Tabel Role Transaksi: Search, Filter, dan Sort (3/4) | FE+BE | 16 | TC-FA-RP-1071, TC-FA-RP-1072 |
| TC-FA-RP-E2E-180-tabel-role-transaksi-search-filter-dan-sort-4 | Tabel Role Transaksi: Search, Filter, dan Sort (4/4) | FE+BE | 21 | TC-FA-RP-1073, TC-FA-RP-1106 |
| TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1 | Tabel Role Transaksi: Setup Column (1/5) | FE+BE | 36 | TC-FA-RP-600, TC-FA-RP-601, TC-FA-RP-602, TC-FA-RP-603 |
| TC-FA-RP-E2E-182-tabel-role-transaksi-setup-column-2 | Tabel Role Transaksi: Setup Column (2/5) | FE+BE | 28 | TC-FA-RP-604, TC-FA-RP-605 |
| TC-FA-RP-E2E-183-tabel-role-transaksi-setup-column-3 | Tabel Role Transaksi: Setup Column (3/5) | FE+BE | 33 | TC-FA-RP-606, TC-FA-RP-607, TC-FA-RP-608 |
| TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4 | Tabel Role Transaksi: Setup Column (4/5) | FE+BE | 39 | TC-FA-RP-609, TC-FA-RP-610, TC-FA-RP-611, TC-FA-RP-1074 |
| TC-FA-RP-E2E-185-tabel-role-transaksi-setup-column-5 | Tabel Role Transaksi: Setup Column (5/5) | FE+BE | 25 | TC-FA-RP-1075, TC-FA-RP-1076 |
| TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (1/3) | FE+BE | 37 | TC-FA-RP-612, TC-FA-RP-613, TC-FA-RP-614, TC-FA-RP-1013, TC-FA-RP-1027 |
| TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2 | Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (2/3) | FE+BE | 39 | TC-FA-RP-1050, TC-FA-RP-1051, TC-FA-RP-1052, TC-FA-RP-1053 |
| TC-FA-RP-E2E-188-tabel-role-transaksi-tampilan-section-header-keterangan-3 | Tabel Role Transaksi: tampilan section, header, keterangan approver, dan state (3/3) | FE+BE | 24 | TC-FA-RP-1054, TC-FA-RP-1109 |
| TC-FA-RP-E2E-189-detail-role-search-1 | Detail Role: Search (1/3) | FE+BE | 34 | TC-FA-RP-617, TC-FA-RP-618 |
| TC-FA-RP-E2E-190-detail-role-search-2 | Detail Role: Search (2/3) | FE+BE | 33 | TC-FA-RP-619, TC-FA-RP-620, TC-FA-RP-621, TC-FA-RP-622 |
| TC-FA-RP-E2E-191-detail-role-search-3 | Detail Role: Search (3/3) | FE+BE | 27 | TC-FA-RP-623, TC-FA-RP-624, TC-FA-RP-1077, TC-FA-RP-1107 |
| TC-FA-RP-E2E-192-detail-role-filter-1 | Detail Role: Filter (1/4) | FE+BE | 33 | TC-FA-RP-625, TC-FA-RP-626, TC-FA-RP-627, TC-FA-RP-628 |
| TC-FA-RP-E2E-193-detail-role-filter-2 | Detail Role: Filter (2/4) | FE+BE | 29 | TC-FA-RP-629, TC-FA-RP-630, TC-FA-RP-631, TC-FA-RP-632 |
| TC-FA-RP-E2E-194-detail-role-filter-3 | Detail Role: Filter (3/4) | FE+BE | 30 | TC-FA-RP-633, TC-FA-RP-634, TC-FA-RP-635, TC-FA-RP-636 |
| TC-FA-RP-E2E-195-detail-role-filter-4 | Detail Role: Filter (4/4) | FE+BE | 47 | TC-FA-RP-637, TC-FA-RP-638, TC-FA-RP-639, TC-FA-RP-640, TC-FA-RP-1078 |
| TC-FA-RP-E2E-196-detail-role-sort | Detail Role: Sort | FE+BE | 28 | TC-FA-RP-641, TC-FA-RP-642, TC-FA-RP-643, TC-FA-RP-1079 |
| TC-FA-RP-E2E-197-detail-role-setup-column-1 | Detail Role: Setup Column (1/5) | FE+BE | 27 | TC-FA-RP-644, TC-FA-RP-645, TC-FA-RP-646 |
| TC-FA-RP-E2E-198-detail-role-setup-column-2 | Detail Role: Setup Column (2/5) | FE+BE | 23 | TC-FA-RP-647, TC-FA-RP-648 |
| TC-FA-RP-E2E-199-detail-role-setup-column-3 | Detail Role: Setup Column (3/5) | FE+BE | 23 | TC-FA-RP-649, TC-FA-RP-650 |
| TC-FA-RP-E2E-200-detail-role-setup-column-4 | Detail Role: Setup Column (4/5) | FE+BE | 35 | TC-FA-RP-651, TC-FA-RP-652, TC-FA-RP-653 |
| TC-FA-RP-E2E-201-detail-role-setup-column-5 | Detail Role: Setup Column (5/5) | FE+BE | 30 | TC-FA-RP-654, TC-FA-RP-655, TC-FA-RP-656, TC-FA-RP-1006 |
| TC-FA-RP-E2E-202-detail-role-download-1 | Detail Role: Download (1/2) | FE+BE | 30 | TC-FA-RP-661, TC-FA-RP-662, TC-FA-RP-663, TC-FA-RP-664 |
| TC-FA-RP-E2E-203-detail-role-download-2 | Detail Role: Download (2/2) | FE+BE | 27 | TC-FA-RP-666, TC-FA-RP-668, TC-FA-RP-670, TC-FA-RP-1005 |
| TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | Detail Role: kombinasi dan state halaman (1/2) | FE+BE | 39 | TC-FA-RP-671, TC-FA-RP-672, TC-FA-RP-673, TC-FA-RP-674, TC-FA-RP-675 |
| TC-FA-RP-E2E-205-detail-role-kombinasi-dan-state-halaman-2 | Detail Role: kombinasi dan state halaman (2/2) | FE+BE | 19 | TC-FA-RP-676, TC-FA-RP-677, TC-FA-RP-1025 |
| TC-FA-RP-E2E-206-table-user-picker-search-filter-dan-sort-1 | Table User Picker: Search, Filter, dan Sort (1/5) | FE+BE | 28 | TC-FA-RP-678, TC-FA-RP-679 |
| TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2 | Table User Picker: Search, Filter, dan Sort (2/5) | FE+BE | 35 | TC-FA-RP-680, TC-FA-RP-681, TC-FA-RP-682, TC-FA-RP-683 |
| TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3 | Table User Picker: Search, Filter, dan Sort (3/5) | FE+BE | 30 | TC-FA-RP-684, TC-FA-RP-685, TC-FA-RP-686, TC-FA-RP-687 |
| TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4 | Table User Picker: Search, Filter, dan Sort (4/5) | FE+BE | 28 | TC-FA-RP-688, TC-FA-RP-689, TC-FA-RP-1080, TC-FA-RP-1081 |
| TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5 | Table User Picker: Search, Filter, dan Sort (5/5) | FE+BE | 34 | TC-FA-RP-1082, TC-FA-RP-1083, TC-FA-RP-1092, TC-FA-RP-1108 |
| TC-FA-RP-E2E-211-table-user-picker-setup-column-1 | Table User Picker: Setup Column (1/5) | FE+BE | 23 | TC-FA-RP-690, TC-FA-RP-691, TC-FA-RP-692 |
| TC-FA-RP-E2E-212-table-user-picker-setup-column-2 | Table User Picker: Setup Column (2/5) | FE+BE | 24 | TC-FA-RP-693, TC-FA-RP-694 |
| TC-FA-RP-E2E-213-table-user-picker-setup-column-3 | Table User Picker: Setup Column (3/5) | FE+BE | 22 | TC-FA-RP-695, TC-FA-RP-696 |
| TC-FA-RP-E2E-214-table-user-picker-setup-column-4 | Table User Picker: Setup Column (4/5) | FE+BE | 36 | TC-FA-RP-697, TC-FA-RP-698, TC-FA-RP-699 |
| TC-FA-RP-E2E-215-table-user-picker-setup-column-5 | Table User Picker: Setup Column (5/5) | FE+BE | 13 | TC-FA-RP-700, TC-FA-RP-701 |
| TC-FA-RP-E2E-216-table-user-picker-pagination-state-dan-kombinasi-1 | Table User Picker: Pagination, state, dan kombinasi (1/2) | FE+BE | 28 | TC-FA-RP-702, TC-FA-RP-703, TC-FA-RP-704 |
| TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2 | Table User Picker: Pagination, state, dan kombinasi (2/2) | FE+BE | 28 | TC-FA-RP-705, TC-FA-RP-706, TC-FA-RP-707, TC-FA-RP-708 |
| TC-FA-RP-E2E-218-modal-changelog-search-dan-filter-1 | Modal Changelog: Search dan Filter (1/6) | FE+BE | 34 | TC-FA-RP-709, TC-FA-RP-710 |
| TC-FA-RP-E2E-219-modal-changelog-search-dan-filter-2 | Modal Changelog: Search dan Filter (2/6) | FE+BE | 25 | TC-FA-RP-711, TC-FA-RP-712, TC-FA-RP-713 |
| TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | Modal Changelog: Search dan Filter (3/6) | FE+BE | 24 | TC-FA-RP-714, TC-FA-RP-715, TC-FA-RP-716, TC-FA-RP-717, TC-FA-RP-718 |
| TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4 | Modal Changelog: Search dan Filter (4/6) | FE+BE | 27 | TC-FA-RP-719, TC-FA-RP-720, TC-FA-RP-721, TC-FA-RP-722 |
| TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5 | Modal Changelog: Search dan Filter (5/6) | FE+BE | 26 | TC-FA-RP-723, TC-FA-RP-724, TC-FA-RP-725, TC-FA-RP-726 |
| TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6 | Modal Changelog: Search dan Filter (6/6) | FE+BE | 30 | TC-FA-RP-727, TC-FA-RP-728, TC-FA-RP-729, TC-FA-RP-730 |
| TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1 | Modal Changelog: Sort dan Setup Column (1/4) | FE+BE | 19 | TC-FA-RP-731, TC-FA-RP-732, TC-FA-RP-733, TC-FA-RP-734 |
| TC-FA-RP-E2E-225-modal-changelog-sort-dan-setup-column-2 | Modal Changelog: Sort dan Setup Column (2/4) | FE+BE | 19 | TC-FA-RP-735, TC-FA-RP-736 |
| TC-FA-RP-E2E-226-modal-changelog-sort-dan-setup-column-3 | Modal Changelog: Sort dan Setup Column (3/4) | FE+BE | 24 | TC-FA-RP-737, TC-FA-RP-738 |
| TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4 | Modal Changelog: Sort dan Setup Column (4/4) | FE+BE | 33 | TC-FA-RP-739, TC-FA-RP-740, TC-FA-RP-741, TC-FA-RP-742 |
| TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1 | Modal Changelog: Pagination, Download, kombinasi, dan varian (1/5) | FE+BE | 36 | TC-FA-RP-743, TC-FA-RP-744, TC-FA-RP-745, TC-FA-RP-746 |
| TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2 | Modal Changelog: Pagination, Download, kombinasi, dan varian (2/5) | FE+BE | 27 | TC-FA-RP-747, TC-FA-RP-748, TC-FA-RP-749, TC-FA-RP-750 |
| TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | Modal Changelog: Pagination, Download, kombinasi, dan varian (3/5) | FE+BE | 30 | TC-FA-RP-752, TC-FA-RP-754, TC-FA-RP-756, TC-FA-RP-757, TC-FA-RP-758 |
| TC-FA-RP-E2E-231-modal-changelog-pagination-download-kombinasi-dan-varian-4 | Modal Changelog: Pagination, Download, kombinasi, dan varian (4/5) | FE+BE | 13 | TC-FA-RP-759, TC-FA-RP-760 |
| TC-FA-RP-E2E-232-modal-changelog-pagination-download-kombinasi-dan-varian-5 | Modal Changelog: Pagination, Download, kombinasi, dan varian (5/5) | FE+BE | 27 | TC-FA-RP-762, TC-FA-RP-763, TC-FA-RP-1084 |
| TC-FA-RP-E2E-233-isi-berkas-download-csv-dan-xlsx-1 | Isi berkas Download CSV dan XLSX (1/2) | FE+BE | 33 | TC-FA-RP-525, TC-FA-RP-573, TC-FA-RP-667 |
| TC-FA-RP-E2E-234-isi-berkas-download-csv-dan-xlsx-2 | Isi berkas Download CSV dan XLSX (2/2) | FE+BE | 35 | TC-FA-RP-669, TC-FA-RP-753, TC-FA-RP-1024 |
| TC-FA-RP-E2E-235-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-1 | Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (1/2) | FE+BE | 33 | TC-FA-RP-765, TC-FA-RP-766, TC-FA-RP-767 |
| TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2 | Guided Tooltip: langkah, kunjungan pertama, replay, Skip, Back, dan keyboard (2/2) | FE+BE | 35 | TC-FA-RP-768, TC-FA-RP-769, TC-FA-RP-770, TC-FA-RP-771 |
| TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | Format tanggal dan waktu mengikuti General Settings | FE+BE | 30 | TC-FA-RP-773, TC-FA-RP-774, TC-FA-RP-775, TC-FA-RP-776, TC-FA-RP-777 |
| TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | Tooltip, hover, truncation, dan tampilan baris (1/2) | FE+BE | 32 | TC-FA-RP-778, TC-FA-RP-779, TC-FA-RP-780, TC-FA-RP-781, TC-FA-RP-782 |
| TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | Tooltip, hover, truncation, dan tampilan baris (2/2) | FE+BE | 19 | TC-FA-RP-783, TC-FA-RP-784, TC-FA-RP-785, TC-FA-RP-786, TC-FA-RP-972 |
| TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1 | State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (1/2) | FE+BE | 30 | TC-FA-RP-787, TC-FA-RP-788, TC-FA-RP-789, TC-FA-RP-790 |
| TC-FA-RP-E2E-241-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-2 | State halaman: tab, node Sidebar Group Tree, dan klik ulang menu (2/2) | FE+BE | 33 | TC-FA-RP-791, TC-FA-RP-793, TC-FA-RP-1029 |
| TC-FA-RP-E2E-242-aksesibilitas-keyboard-fokus-dialog-dan-slot-toast | Aksesibilitas keyboard, fokus dialog, dan slot toast | FE+BE | 26 | TC-FA-RP-1007, TC-FA-RP-1008, TC-FA-RP-1015 |
| TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1 | Changelog Tab Total Control, Read Only, dan Group Manager (1/2) | FE+BE | 30 | TC-FA-RP-794, TC-FA-RP-795, TC-FA-RP-796, TC-FA-RP-797 |
| TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2 | Changelog Tab Total Control, Read Only, dan Group Manager (2/2) | FE+BE | 34 | TC-FA-RP-802, TC-FA-RP-803, TC-FA-RP-804, TC-FA-RP-805 |
| TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | Changelog Detail Role Global Role (1/3) | FE+BE | 31 | TC-FA-RP-806, TC-FA-RP-807, TC-FA-RP-808, TC-FA-RP-809, TC-FA-RP-810 |
| TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | Changelog Detail Role Global Role (2/3) | FE+BE | 41 | TC-FA-RP-811, TC-FA-RP-812, TC-FA-RP-813, TC-FA-RP-814, TC-FA-RP-1130 |
| TC-FA-RP-E2E-247-changelog-detail-role-global-role-3 | Changelog Detail Role Global Role (3/3) | FE+BE | 44 | TC-FA-RP-1134, TC-FA-RP-1135, TC-FA-RP-1136 |
| TC-FA-RP-E2E-248-changelog-detail-role-group-role | Changelog Detail Role Group Role | FE+BE | 38 | TC-FA-RP-815, TC-FA-RP-816, TC-FA-RP-817, TC-FA-RP-818, TC-FA-RP-819 |
| TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | Changelog Tab System dan Approval Config (1/2) | FE+BE | 35 | TC-FA-RP-820, TC-FA-RP-821, TC-FA-RP-822, TC-FA-RP-823, TC-FA-RP-824 |
| TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | Changelog Tab System dan Approval Config (2/2) | FE+BE | 33 | TC-FA-RP-825, TC-FA-RP-826, TC-FA-RP-827, TC-FA-RP-828, TC-FA-RP-829 |
| TC-FA-RP-E2E-251-changelog-transaction-role | Changelog Transaction Role | FE+BE | 28 | TC-FA-RP-830, TC-FA-RP-831, TC-FA-RP-832, TC-FA-RP-833 |
| TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | System Log dan Activity Log: Assign, Remove, dan Edit (1/5) | FE+BE | 40 | TC-FA-RP-834, TC-FA-RP-835, TC-FA-RP-836, TC-FA-RP-837, TC-FA-RP-838 |
| TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | System Log dan Activity Log: Assign, Remove, dan Edit (2/5) | FE+BE | 41 | TC-FA-RP-839, TC-FA-RP-840, TC-FA-RP-841, TC-FA-RP-842, TC-FA-RP-843 |
| TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | System Log dan Activity Log: Assign, Remove, dan Edit (3/5) | FE+BE | 44 | TC-FA-RP-844, TC-FA-RP-845, TC-FA-RP-846, TC-FA-RP-847, TC-FA-RP-848 |
| TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | System Log dan Activity Log: Assign, Remove, dan Edit (4/5) | FE+BE | 43 | TC-FA-RP-849, TC-FA-RP-850, TC-FA-RP-851, TC-FA-RP-852, TC-FA-RP-853 |
| TC-FA-RP-E2E-256-system-log-dan-activity-log-assign-remove-dan-edit-5 | System Log dan Activity Log: Assign, Remove, dan Edit (5/5) | FE+BE | 9 | TC-FA-RP-854 |
| TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | System Log dan Activity Log: konfigurasi approval dan Modified By | FE+BE | 50 | TC-FA-RP-855, TC-FA-RP-856, TC-FA-RP-857, TC-FA-RP-1055, TC-FA-RP-1056, TC-FA-RP-1057, TC-FA-RP-1058 |
| TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1 | Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (1/5) | FE+BE | 32 | TC-FA-RP-858, TC-FA-RP-859, TC-FA-RP-860, TC-FA-RP-862 |
| TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2 | Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (2/5) | FE+BE | 27 | TC-FA-RP-866, TC-FA-RP-869, TC-FA-RP-870, TC-FA-RP-871 |
| TC-FA-RP-E2E-260-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-3 | Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (3/5) | FE+BE | 36 | TC-FA-RP-865, TC-FA-RP-1035 |
| TC-FA-RP-E2E-261-absence-log-aksi-yang-tidak-menulis-entri-log | Absence log: aksi yang tidak menulis entri log | FE+BE | 38 | TC-FA-RP-867, TC-FA-RP-868, TC-FA-RP-873 |
| TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | Multi-konteks: notifikasi in-app ke akun target (1/3) | FE+BE | 40 | TC-FA-RP-875, TC-FA-RP-876, TC-FA-RP-877, TC-FA-RP-878, TC-FA-RP-879 |
| TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | Multi-konteks: notifikasi in-app ke akun target (2/3) | FE+BE | 49 | TC-FA-RP-880, TC-FA-RP-881, TC-FA-RP-882, TC-FA-RP-883, TC-FA-RP-884 |
| TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3 | Multi-konteks: notifikasi in-app ke akun target (3/3) | FE+BE | 31 | TC-FA-RP-885, TC-FA-RP-886, TC-FA-RP-887, TC-FA-RP-888 |
| TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | Sinkronisasi Detail Role dan Tab Role Settings > User (1/2) | FE+BE | 50 | TC-FA-RP-889, TC-FA-RP-890, TC-FA-RP-891, TC-FA-RP-892, TC-FA-RP-893, TC-FA-RP-894, TC-FA-RP-895 |
| TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2 | Sinkronisasi Detail Role dan Tab Role Settings > User (2/2) | FE+BE | 39 | TC-FA-RP-897, TC-FA-RP-898, TC-FA-RP-899, TC-FA-RP-911 |
| TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | Efek status user, App Access, dan cascade lintas modul (1/2) | FE+BE | 48 | TC-FA-RP-900, TC-FA-RP-901, TC-FA-RP-902, TC-FA-RP-904, TC-FA-RP-905, TC-FA-RP-906 |
| TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | Efek status user, App Access, dan cascade lintas modul (2/2) | FE+BE | 54 | TC-FA-RP-907, TC-FA-RP-908, TC-FA-RP-909, TC-FA-RP-910, TC-FA-RP-912, TC-FA-RP-1102, TC-FA-RP-1103 |
| TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | Defense-in-depth: penolakan server atas permintaan langsung (1/9) | FE+BE | 19 | TC-FA-RP-913, TC-FA-RP-914, TC-FA-RP-915, TC-FA-RP-916, TC-FA-RP-948, TC-FA-RP-968 |
| TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | Defense-in-depth: penolakan server atas permintaan langsung (2/9) | FE+BE | 20 | TC-FA-RP-921, TC-FA-RP-923, TC-FA-RP-924, TC-FA-RP-927, TC-FA-RP-936, TC-FA-RP-967 |
| TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | Defense-in-depth: penolakan server atas permintaan langsung (3/9) | FE+BE | 24 | TC-FA-RP-917, TC-FA-RP-922, TC-FA-RP-925, TC-FA-RP-926, TC-FA-RP-928, TC-FA-RP-965, TC-FA-RP-966, TC-FA-RP-970 |
| TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | Defense-in-depth: penolakan server atas permintaan langsung (4/9) | FE+BE | 20 | TC-FA-RP-918, TC-FA-RP-919, TC-FA-RP-920, TC-FA-RP-929, TC-FA-RP-930, TC-FA-RP-931 |
| TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | Defense-in-depth: penolakan server atas permintaan langsung (5/9) | FE+BE | 23 | TC-FA-RP-932, TC-FA-RP-933, TC-FA-RP-934, TC-FA-RP-935, TC-FA-RP-937, TC-FA-RP-939, TC-FA-RP-940 |
| TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | Defense-in-depth: penolakan server atas permintaan langsung (6/9) | FE+BE | 21 | TC-FA-RP-941, TC-FA-RP-942, TC-FA-RP-945, TC-FA-RP-946, TC-FA-RP-947, TC-FA-RP-949, TC-FA-RP-950 |
| TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | Defense-in-depth: penolakan server atas permintaan langsung (7/9) | FE+BE | 22 | TC-FA-RP-951, TC-FA-RP-952, TC-FA-RP-953, TC-FA-RP-954, TC-FA-RP-955, TC-FA-RP-956, TC-FA-RP-958 |
| TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | Defense-in-depth: penolakan server atas permintaan langsung (8/9) | FE+BE | 25 | TC-FA-RP-959, TC-FA-RP-960, TC-FA-RP-962, TC-FA-RP-1038, TC-FA-RP-1045, TC-FA-RP-1098, TC-FA-RP-1125 |
| TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | Defense-in-depth: penolakan server atas permintaan langsung (9/9) | FE+BE | 24 | TC-FA-RP-938, TC-FA-RP-957, TC-FA-RP-961, TC-FA-RP-963, TC-FA-RP-964, TC-FA-RP-1126, TC-FA-RP-1143 |
| TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1 | State tenant: Client Suspended dan Expired menolak aksi tulis (1/3) | FE+BE | 43 | TC-FA-RP-969, TC-FA-RP-973, TC-FA-RP-974, TC-FA-RP-975, TC-FA-RP-976, TC-FA-RP-977 |
| TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2 | State tenant: Client Suspended dan Expired menolak aksi tulis (2/3) | FE+BE | 39 | TC-FA-RP-978, TC-FA-RP-979, TC-FA-RP-980, TC-FA-RP-981, TC-FA-RP-982, TC-FA-RP-983 |
| TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | State tenant: Client Suspended dan Expired menolak aksi tulis (3/3) | FE+BE | 46 | TC-FA-RP-984, TC-FA-RP-985, TC-FA-RP-986, TC-FA-RP-987, TC-FA-RP-988, TC-FA-RP-989 |
| TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1 | State tenant: plan tier dan Approval Workflow (1/2) | FE+BE | 34 | TC-FA-RP-990, TC-FA-RP-991, TC-FA-RP-992, TC-FA-RP-993 |
| TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | Multi-konteks: konflik dua admin pada objek yang sama | FE+BE | 41 | TC-FA-RP-995, TC-FA-RP-996, TC-FA-RP-997, TC-FA-RP-998, TC-FA-RP-999 |
| TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat | Klik ganda dan ketuk ganda cepat | FE+BE | 29 | TC-FA-RP-1000, TC-FA-RP-1001, TC-FA-RP-1002, TC-FA-RP-1003 |
| TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (1/2) | FE+BE | 59 | TC-FA-RP-201, TC-FA-RP-202, TC-FA-RP-203, TC-FA-RP-204, TC-FA-RP-230 |
| TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (2/2) | FE+BE | 49 | TC-FA-RP-264, TC-FA-RP-274, TC-FA-RP-275, TC-FA-RP-441, TC-FA-RP-447 |
| TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (1/2) | FE+BE | 49 | TC-FA-RP-207, TC-FA-RP-213, TC-FA-RP-239, TC-FA-RP-284, TC-FA-RP-285 |
| TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2 | Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (2/2) | FE+BE | 41 | TC-FA-RP-302, TC-FA-RP-303, TC-FA-RP-333, TC-FA-RP-334 |
| TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1 | Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (1/2) | FE+BE | 30 | TC-FA-RP-351, TC-FA-RP-352, TC-FA-RP-353, TC-FA-RP-358 |
| TC-FA-RP-E2E-289-resilience-kegagalan-pada-require-approval-approval-scope-dan-2 | Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (2/2) | FE+BE | 29 | TC-FA-RP-373, TC-FA-RP-391, TC-FA-RP-392 |
| TC-FA-RP-E2E-290-resilience-download-gagal | Resilience: Download gagal | FE+BE | 39 | TC-FA-RP-523, TC-FA-RP-571, TC-FA-RP-591, TC-FA-RP-665, TC-FA-RP-751, TC-FA-RP-764 |
| TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui | Absence log: aksi no-op atau ditolak UI | FE+BE | 58 | TC-FA-RP-283, TC-FA-RP-300, TC-FA-RP-357, TC-FA-RP-413, TC-FA-RP-461, TC-FA-RP-1041 |
| TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | Absence log: permintaan langsung yang ditolak | FE+BE | 23 | TC-FA-RP-913, TC-FA-RP-957, TC-FA-RP-961, TC-FA-RP-983, TC-FA-RP-1098 |
| TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | Absence log: aksi ditolak karena state tenant (1/2) | FE+BE | 46 | TC-FA-RP-973, TC-FA-RP-974, TC-FA-RP-975, TC-FA-RP-976, TC-FA-RP-977, TC-FA-RP-978 |
| TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2 | Absence log: aksi ditolak karena state tenant (2/2) | FE+BE | 29 | TC-FA-RP-979, TC-FA-RP-980, TC-FA-RP-981, TC-FA-RP-982 |
| TC-FA-RP-E2E-295-loading-state-shimmer-tabel-total-control-dan-detail-role | Loading state tabel memakai Shimmer pada Tab Total Control dan Detail Role | FE+BE | 11 | TC-FA-RP-72 |
| TC-FA-RP-E2E-296-dua-sesi-total-control-toast-netral-untuk-nilai-sama | Dua sesi Total Control: edit, toggle, dan toggle registrasi bernilai sama menampilkan toast netral | FE+BE | 41 | TC-FA-RP-276, TC-FA-RP-350, TC-FA-RP-372 |
| TC-FA-RP-E2E-297-role-matrix-ikon-download-dan-changelog-tampil-per-peran | Role Matrix: ikon Download dan Changelog tampil dan berfungsi per peran | FE+BE | 17 | TC-FA-RP-119 |
| TC-FA-RP-E2E-298-role-matrix-changelog-tab-total-control-dan-read-only-bagi-group-manager | Role Matrix: Changelog Tab Total Control dan Read Only bagi Group Manager tanpa entri tingkat akses dan Global Role | FE+BE | 17 | TC-FA-RP-1113 |
| TC-FA-RP-E2E-299-changelog-dan-download-entri-remove-group-deleted-per-cakupan-3 | Changelog dan Download entri Remove (Group Deleted) per cakupan aktor (3/3) | FE+BE | 24 | TC-FA-RP-1118, TC-FA-RP-1119 |
| TC-FA-RP-E2E-300-assign-user-ke-global-role-di-detail-role-2 | Assign User ke Global Role di Detail Role (2/2) | FE+BE | 28 | TC-FA-RP-244, TC-FA-RP-245, TC-FA-RP-246 |
| TC-FA-RP-E2E-301-assign-role-transaksi-kandidat-picker-bagi-pemegang-manage-user-dan-role | Assign Role Transaksi: kandidat picker bagi pemegang Manage user & role | FE+BE | 9 | TC-FA-RP-318 |
| TC-FA-RP-E2E-302-bulk-remove-hasil-parsial-dan-diblok-oleh-admin-lain | Bulk Remove: hasil parsial dan diblok oleh admin lain | FE+BE | 22 | TC-FA-RP-299, TC-FA-RP-300 |
| TC-FA-RP-E2E-303-require-approval-transaction-role-toggle-radio-aturan-dan-3 | Require Approval Transaction Role: toggle, radio aturan, dan pewarisan nilai (3/3) | FE+BE | 13 | TC-FA-RP-345, TC-FA-RP-347 |
| TC-FA-RP-E2E-304-require-approval-prasyarat-aktivasi-dicek-ulang-approver-terakhir-dilepas | Require Approval Transaction Role: prasyarat aktivasi dicek ulang saat approver terakhir dilepas admin lain | FE+BE | 9 | TC-FA-RP-354 |
| TC-FA-RP-E2E-305-remove-role-transaksi-baris-sudah-dihapus-sesi-lain | Remove Role Transaksi atas baris yang sudah dihapus sesi lain | FE+BE | 7 | TC-FA-RP-461 |
| TC-FA-RP-E2E-306-identitas-user-dihapus-permanen-cascade-tanpa-entri-log-group-manager | Identitas user dihapus permanen: seluruh baris FAMS dihapus cascade tanpa entri log per role (Group Manager) | FE+BE | 12 | TC-FA-RP-1144 |
| TC-FA-RP-E2E-311-modal-changelog-title-kolom-object-dan-placeholder-per-varian | Modal Changelog: Title, kolom Object, dan placeholder tiap varian | FE+BE | 12 | TC-FA-RP-761 |
| TC-FA-RP-E2E-312-modal-changelog-transaction-role-terpisah-per-jenis-transaksi | Modal Changelog Transaction Role terpisah per jenis transaksi | FE+BE | 19 | TC-FA-RP-1030 |
| TC-FA-RP-E2E-313-aksesibilitas-dialog-konfirmasi-fokus-terkunci-dan-esc-setara-cancel | Aksesibilitas dialog konfirmasi: fokus terkunci dan Esc setara Cancel | FE+BE | 24 | TC-FA-RP-1009 |
| TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert | Changelog Tab Read Only dan Group Manager: Assign, Remove, dan Auto-Revert | FE+BE | 29 | TC-FA-RP-798, TC-FA-RP-799, TC-FA-RP-800, TC-FA-RP-801 |
| TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4 | Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (4/5) | FE+BE | 32 | TC-FA-RP-861, TC-FA-RP-863, TC-FA-RP-864, TC-FA-RP-874 |
| TC-FA-RP-E2E-316-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-5 | Pencatatan lintas surface: cascade, atomik, dan konsistensi entri (5/5) | FE+BE | 31 | TC-FA-RP-872, TC-FA-RP-1140 |
| TC-FA-RP-E2E-317-state-tenant-plan-tier-dan-approval-workflow-2 | State tenant: plan tier dan Approval Workflow (2/2) | FE+BE | 26 | TC-FA-RP-994 |
| TC-FA-RP-E2E-318-assign-total-control-dan-read-only-menulis-baris-pola-transaction-role | Assign Total Control dan Read Only menulis baris pola Transaction Role pada semua Jenis Transaksi × Group | FE+BE | 35 | TC-FA-RP-1145, TC-FA-RP-1146 |
| TC-FA-RP-E2E-319-assign-total-control-dan-read-only-menulis-baris-pola-group-role | Assign Total Control ke user Standard menulis baris pola Group Role pada semua group dengan CRUD penuh sesuai kolom berlaku | FE+BE | 28 | TC-FA-RP-1169 |
| TC-FA-RP-E2E-320-remove-total-control-dan-read-only-menghapus-baris-pola-transaction-role | Remove Total Control dan Read Only menghapus baris pola Transaction Role pada semua sub-tab dan node | FE+BE | 22 | TC-FA-RP-1148, TC-FA-RP-1149 |
| TC-FA-RP-E2E-321-role-matrix-gating-remove-baris-pola-transaction-role-per-peran | Role Matrix: gating Remove baris pola Transaction Role per peran | FE+BE | 33 | TC-FA-RP-1150 |
| TC-FA-RP-E2E-322-auto-revert-group-role-pola-lewat-edit-crud-dan-remove-baris | Auto-revert tier lewat edit CRUD dan Remove baris pola Group Role: dialog D-04, tier lepas, role lain utuh | FE+BE | 32 | TC-FA-RP-1171, TC-FA-RP-1172 |
| TC-FA-RP-E2E-323-bulk-remove-baris-group-role-target-total-control-dan-read-only | Bulk Remove baris Group Role target Total Control dan Read Only: dialog D-07 dengan anotasi tier, Confirm melepas kedua tier | FE+BE | 19 | TC-FA-RP-1173 |
| TC-FA-RP-E2E-324-auto-revert-role-transaksi-remove-baris-pola-target-total-control-dan-read-only | Auto-Revert Role Transaksi: Remove Baris Pola Target Total Control | FE+BE | 32 | TC-FA-RP-1151 |
| TC-FA-RP-E2E-325-auto-revert-role-transaksi-turun-dan-naik-tangga-dari-popup-assign | Auto-Revert Role Transaksi: Turun dan Naik Tangga dari Popup Assign | FE+BE | 34 | TC-FA-RP-1152, TC-FA-RP-1153 |
| TC-FA-RP-E2E-326-auto-revert-role-transaksi-submit-campuran-dua-dialog-berurutan | Auto-Revert Role Transaksi: Submit Campuran Dua Dialog Berurutan | FE+BE | 29 | TC-FA-RP-1154 |
| TC-FA-RP-E2E-327-pengecualian-dialog-role-transaksi-default-user-dan-d-09-pada-remove-approver-pola | Pengecualian Dialog Role Transaksi: Default User dan D-09 pada Remove Approver Pola | FE+BE | 23 | TC-FA-RP-1155, TC-FA-RP-1160 |
| TC-FA-RP-E2E-328-efek-deactivate-dan-app-access-pada-baris-pola-transaction-role | Efek Deactivate user Total Control pada baris pola Transaction Role | FE+BE | 23 | TC-FA-RP-1156 |
| TC-FA-RP-E2E-329-sub-tab-addon-tanpa-dan-dengan-lisensi-baris-pola-tidak-dihitung | Sub-tab Addon tanpa dan dengan lisensi, baris pola tidak dihitung | FE+BE | 24 | TC-FA-RP-1161, TC-FA-RP-1162 |
| TC-FA-RP-E2E-330-group-baru-subgroup-level-one-dan-import-menulis-baris-pola | Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Transaction Role Total Control dan Read Only | FE+BE | 31 | TC-FA-RP-1157, TC-FA-RP-1158 |
| TC-FA-RP-E2E-331-home-group-constraint-diabaikan-untuk-total-control-dan-read-only | Home Group constraint diabaikan untuk Total Control dan Read Only | FE+BE | 19 | TC-FA-RP-1175 |
| TC-FA-RP-E2E-332-delete-group-menghapus-baris-pola-transaction-role-dan-group-role | Delete Group menghapus baris pola Transaction Role dan Group Role pada node dan descendant dengan log Remove (Group Deleted) per baris | FE+BE | 33 | TC-FA-RP-1159, TC-FA-RP-1176 |
| TC-FA-RP-E2E-333-detail-role-group-role-checkbox-pagination-dan-select-all-baris-pola | Detail Role Group Role: pagination 41 baris All Groups dan checkbox serta Select All dengan baris pola | FE+BE | 46 | TC-FA-RP-1177, TC-FA-RP-1178 |
| TC-FA-RP-E2E-334-header-section-role-transaksi-menghitung-baris-pola-saat-baris-melebihi-10 | Header section Role Transaksi menghitung seluruh baris termasuk baris pola saat jumlah baris melebihi 10, dan seluruh baris tampil tanpa pagination | FE+BE | 26 | TC-FA-RP-1167 |
| TC-FA-RP-E2E-335-changelog-transaction-role-per-baris-pola-assign-remove-dan-auto-revert | Changelog Transaction Role per baris pola: Assign, Remove, dan Auto-Revert Total Control | FE+BE | 31 | TC-FA-RP-1163 |
| TC-FA-RP-E2E-336-multi-konteks-notifikasi-auto-revert-varian-role-transaksi | Multi-konteks: notifikasi auto-revert varian Role Transaksi untuk Total Control dan Read Only | FE+BE | 22 | TC-FA-RP-1164 |
| TC-FA-RP-E2E-337-assign-total-control-ke-user-standard-pemegang-peran-tangga-lama | Assign Total Control ke user Standard pemegang peran tangga lama: peran lama diganti baris pola tanpa duplikat | FE+BE | 28 | TC-FA-RP-1147 |
| TC-FA-RP-E2E-338-assign-read-only-menulis-baris-pola-group-role-dan-changelog-user | Assign Read Only ke user Standard menulis baris pola Group Role pada semua group dengan Read saja | FE+BE | 35 | TC-FA-RP-1170 |
| TC-FA-RP-E2E-341-auto-revert-role-transaksi-remove-baris-pola-target-read-only | Auto-Revert Role Transaksi: Remove Baris Pola Target Read Only | FE+BE | 26 | TC-FA-RP-1165 |
| TC-FA-RP-E2E-342-submit-campuran-cancel-dialog-kedua-membatalkan-seluruh-submit | Auto-Revert Role Transaksi: Cancel Dialog Kedua Membatalkan Seluruh Submit | FE+BE | 32 | TC-FA-RP-1168 |
| TC-FA-RP-E2E-343-app-access-dicabut-baris-pola-dormant-dan-group-baru-tetap-dibuatkan-baris | App Access FAMS dicabut, baris pola dormant dan Group baru tetap dibuatkan baris | FE+BE | 34 | TC-FA-RP-1166 |
| TC-FA-RP-E2E-345-group-baru-menulis-baris-pola-group-role-detail-role-changelog-dan-notifikasi | Group baru (Subgroup, level 1, dan hasil Import) menulis baris pola Group Role dengan log Assign biasa dan tanpa notifikasi | FE+BE | 21 | TC-FA-RP-1174 |
| TC-FA-RP-E2E-346-assign-gm-menulis-baris-pola-group-role-tanpa-global-role | Assign Group Manager menulis baris pola Group Role pada node penugasan dan descendant, tanpa baris Global Role | FE+BE | 29 | TC-FA-RP-1179 |
| TC-FA-RP-E2E-347-assign-gm-menggantikan-peran-tangga-lain-dengan-asset-admin | Assign Group Manager menggantikan peran tangga lain pada Jenis Transaksi dan node yang sama dengan Asset Admin | FE+BE | 20 | TC-FA-RP-1182 |
| TC-FA-RP-E2E-348-assign-total-control-di-atas-gm-hapus-pola-gm-dulu | Assign Total Control ke target Group Manager: baris pola GM dihapus lebih dulu (log per baris) lalu baris pola Total Control ditulis dalam satu transaksi | FE+BE | 35 | TC-FA-RP-1198 |
| TC-FA-RP-E2E-349-log-assign-gm-per-baris-pola-changelog-bukan-system-activity-log | Log Assign Group Manager per baris pola: Assign (via Group Manager) di Changelog, tidak di System Log dan Activity Log, tanpa notifikasi | FE+BE | 36 | TC-FA-RP-1181 |
| TC-FA-RP-E2E-350-remove-gm-bersarang-pelepasan-penugasan-ancestor-baris-pola-tercakup-dipertahankan | Remove Group Manager bersarang: melepas penugasan ancestor menghapus baris pola di luar cakupan dan mempertahankan baris pola yang masih tercakup penugasan lain | FE+BE | 17 | TC-FA-RP-1186 |
| TC-FA-RP-E2E-351-home-group-constraint-pada-gm-mencabut-penugasan-dan-baris-pola-per-baris | Home Group constraint pada Group Manager mencabut penugasan dan baris pola per baris, bukan pencabutan silent | FE+BE | 45 | TC-FA-RP-1199 |
| TC-FA-RP-E2E-352-subgroup-baru-di-bawah-node-gm-menulis-baris-pola-dan-group-level-one-tidak | Subgroup baru di bawah node Group Manager menulis baris pola GM dengan log Assign biasa, sedangkan Group level-one tidak | FE+BE | 32 | TC-FA-RP-1183 |
| TC-FA-RP-E2E-353-delete-group-di-bawah-penugasan-gm-hapus-baris-pola-per-baris | Delete Group di bawah penugasan Group Manager menghapus baris pola pada node dan descendant dengan Remove (Group Deleted) per baris | FE+BE | 35 | TC-FA-RP-1201 |
| TC-FA-RP-E2E-354-auto-revert-gm-lewat-edit-crud-dan-remove-baris-pola-descendant | Edit CRUD baris pola GM pada node descendant memicu auto-revert D-05: GM lepas, seluruh baris pola dipertahankan | FE+BE | 33 | TC-FA-RP-1189 |
| TC-FA-RP-E2E-355-auto-revert-gm-bersarang-baris-pola-bersama-dan-notifikasi | Auto-revert pada baris pola bersama penugasan GM bersarang: seluruh penugasan GM lepas, satu entri Auto-Revert dan satu notifikasi per penugasan | FE+BE | 38 | TC-FA-RP-1188 |
| TC-FA-RP-E2E-356-assign-staff-ke-gm-turun-tangga-dialog-d05-varian-role-transaksi | Assign Staff (turun tangga) ke target Group Manager pada node di subtree GM-nya: satu dialog auto-revert D-05 varian Role Transaksi, D-13 tidak tampil, Staff dipertahankan | FE+BE | 41 | TC-FA-RP-1191 |
| TC-FA-RP-E2E-357-bulk-remove-baris-pola-gm-dan-baris-non-pola-gm-tidak-terkunci | Baris non-pola milik target GM tidak terkunci, dan Bulk Remove yang memuat baris pola GM dan baris Standard memicu dialog D-07 dengan anotasi Group Manager | FE+BE | 46 | TC-FA-RP-1190, TC-FA-RP-1194 |
| TC-FA-RP-E2E-358-role-matrix-kontrol-baris-pola-gm-terkunci-bagi-group-manager | Role Matrix: kontrol baris pola GM terkunci pada node descendant dan tabel Role Transaksi bagi Group Manager (1/2) | FE+BE | 27 | TC-FA-RP-1195 |
| TC-FA-RP-E2E-359-baris-pola-gm-tidak-dihitung-approver-registrasi-dan-pemegang-update | Baris pola GM (Approver dan Manage asset & TAG Update) tidak dihitung: GM nonaktif tidak membuka prasyarat aktivasi registrasi dan Disposal | FE+BE | 13 | TC-FA-RP-1202 |
| TC-FA-RP-E2E-360-defense-in-depth-penolakan-server-permintaan-langsung-target-gm | Defense-in-depth: penolakan server atas permintaan langsung yang menyasar target Group Manager | FE+BE | 16 | TC-FA-RP-1197 |
| TC-FA-RP-E2E-361-assign-gm-menulis-baris-pola-role-transaksi-asset-admin-dan-approver | Assign Group Manager menulis baris pola Role Transaksi (Asset Admin dan Approver) pada setiap Jenis Transaksi di node penugasan dan descendant | FE+BE | 31 | TC-FA-RP-1180 |
| TC-FA-RP-E2E-362-assign-gm-bersarang-satu-set-baris-pola-tanpa-duplikasi | Assign Group Manager bersarang untuk user yang sama: satu set baris pola bersama tanpa duplikasi dan tanpa entri log ganda | FE+BE | 31 | TC-FA-RP-1185 |
| TC-FA-RP-E2E-363-remove-gm-bersarang-pelepasan-penugasan-terakhir-role-transaksi-dan-notifikasi | Remove Group Manager bersarang: melepas penugasan terakhir menghapus baris pola bersama Group Role dan Role Transaksi dengan satu notifikasi | FE+BE | 25 | TC-FA-RP-1186 |
| TC-FA-RP-E2E-364-remove-gm-menghapus-baris-pola-role-transaksi-di-subtree-tanpa-menyentuh-luar-subtree | Remove Group Manager menghapus baris pola Role Transaksi pada node penugasan dan descendant tanpa menyentuh penugasan Role Transaksi di luar subtree | FE+BE | 31 | TC-FA-RP-1187 |
| TC-FA-RP-E2E-365-auto-revert-gm-lewat-remove-baris-approver-pola-descendant | Remove baris Approver pola GM pada node descendant: dialog auto-revert D-05 varian Role Transaksi, Cancel tanpa perubahan, Confirm melepas GM | FE+BE | 29 | TC-FA-RP-1192 |
| TC-FA-RP-E2E-366-submit-campuran-tiga-dialog-d13-d04-d05-assign-role-transaksi | Submit campuran target Standard turun tangga, Total Control, dan Group Manager: tiga dialog berurutan D-13, D-04, D-05; Cancel pada dialog terakhir membatalkan seluruh Submit | FE+BE | 51 | TC-FA-RP-1193 |
| TC-FA-RP-E2E-367-role-matrix-kontrol-baris-pola-gm-terkunci-bagi-manage-user-dan-role-group-update | Role Matrix: kontrol baris pola GM terkunci pada node descendant dan tabel Role Transaksi bagi Manage user & role Group Update (2/2) | FE+BE | 27 | TC-FA-RP-1195 |
| TC-FA-RP-E2E-368-role-matrix-picker-role-transaksi-kandidat-gm-disaring-bagi-group-manager-dan-total-control | Role Matrix: picker Assign Role Transaksi menyaring kandidat Group Manager pada subtree penugasannya bagi Group Manager dan tidak bagi Total Control | FE+BE | 22 | TC-FA-RP-1196 |
| TC-FA-RP-E2E-369-home-group-constraint-yang-mencakup-node-gm-tidak-mencabut-apa-pun | Home Group constraint yang mencakup node penugasan Group Manager tidak mencabut penugasan maupun baris pola | FE+BE | 20 | TC-FA-RP-1200 |
| TC-FA-RP-E2E-370-group-hasil-import-di-bawah-node-gm-menulis-baris-pola | Group hasil Import di bawah node Group Manager menulis baris pola GM dengan log Assign biasa tanpa pewarisan Standard | FE+BE | 17 | TC-FA-RP-1184 |
| TC-FA-RP-E2E-371-aktivasi-require-approval-menghitung-baris-approver-dan-update-gm-yang-dipertahankan-setelah-auto-revert | Setelah auto-revert Group Manager, baris Approver dan Manage asset & TAG Update yang dipertahankan dihitung sebagai approver terdaftar saat aktivasi Require Approval | FE+BE | 21 | TC-FA-RP-1203 |
| TC-FA-RP-E2E-372-baris-gm-yang-dipertahankan-menjadi-penugasan-individual-biasa-edit-tanpa-d05-dan-remove-d03 | Baris yang dipertahankan setelah auto-revert Group Manager menjadi penugasan individual biasa: edit tanpa D-05 dan Remove memakai D-03 | FE+BE | 18 | TC-FA-RP-1204 |
| TC-FA-RP-E2E-373-remove-baris-group-role-target-gm-di-node-gm-nya-dialog-d05-varian-remove-baris | Remove baris Group Role target Group Manager di node GM-nya: dialog D-05 varian Remove baris, GM lepas, baris pola lain dipertahankan | FE+BE | 19 | TC-FA-RP-397 |
| TC-FA-RP-E2E-374-preview-scope-popup-assign-role-transaksi-node-induk-pada-keempat-role | Preview scope popup Assign Role Transaksi pada node induk menampilkan node terpilih beserta seluruh descendant pada keempat role | FE+BE | 19 | TC-FA-RP-1205 |
| TC-FA-RP-E2E-375-preview-scope-mengikuti-node-dan-sidebar-tanpa-node-disabled | Preview scope mengikuti node terpilih dan Sidebar Group Tree tanpa node disabled walau ancestor atau descendant memegang penugasan | FE+BE | 32 | TC-FA-RP-1206, TC-FA-RP-1207 |
| TC-FA-RP-E2E-376-assign-role-sama-pada-node-turunan-atau-induk-saat-overlap-diizinkan | Assign role yang sama pada node turunan atau node induk saat penugasan overlap diizinkan | FE+BE | 22 | TC-FA-RP-1208, TC-FA-RP-1209 |
| TC-FA-RP-E2E-377-assign-tangga-rendah-atau-tinggi-di-node-turunan-tidak-menyentuh-ancestor | Assign role tangga lebih rendah atau lebih tinggi di node turunan tidak mengurangi atau menggantikan penugasan ancestor | FE+BE | 25 | TC-FA-RP-1210, TC-FA-RP-1211 |
| TC-FA-RP-E2E-378-d13-hanya-pada-node-sama-dan-approver-ancestor-descendant-berdampingan | Dialog D-13 hanya pada node yang sama dan Approver di ancestor dan descendant berdampingan | FE+BE | 28 | TC-FA-RP-1212, TC-FA-RP-1213 |
| TC-FA-RP-E2E-379-approver-ancestor-dihitung-aktivasi-toggle-descendant-dan-descendant-tidak-dihitung-bagi-ancestor | Approver di ancestor dihitung untuk aktivasi toggle Require Approval node descendant, sedangkan Approver di descendant tidak dihitung bagi ancestor | FE+BE | 23 | TC-FA-RP-1214, TC-FA-RP-1215 |
| TC-FA-RP-E2E-380-approver-di-ancestor-tidak-mengubah-toggle-descendant | Penugasan Approver di node ancestor tidak mengubah nilai toggle Require Approval node descendant | FE+BE | 17 | TC-FA-RP-1216 |
| TC-FA-RP-E2E-381-d09-jamak-remove-approver-ancestor-dan-d02-remove-gm-dengan-fallback-approver-ancestor | Remove Approver di ancestor menampilkan D-09 jamak berisi group terdampak, dan Remove Group Manager dengan fallback Approver ancestor memakai D-02 | FE+BE | 32 | TC-FA-RP-1217, TC-FA-RP-1218, TC-FA-RP-1221 |
| TC-FA-RP-E2E-382-remove-approver-ancestor-d08-dan-remove-approver-descendant-tanpa-d09 | Remove Approver di ancestor tanpa group terdampak memakai D-08, dan Remove Approver di descendant dengan Approver ancestor tanpa D-09 | FE+BE | 17 | TC-FA-RP-1219, TC-FA-RP-1220 |
| TC-FA-RP-E2E-383-absence-log-assign-overlap-tidak-menghapus-ancestor-dan-satu-entri-per-penugasan | Absence log: Assign Role Transaksi overlap tidak mencatat Remove untuk penugasan ancestor dan dicatat satu entri per penugasan | FE+BE | 34 | TC-FA-RP-1210, TC-FA-RP-1211, TC-FA-RP-1223 |
| TC-FA-RP-E2E-384-delete-group-melepas-penugasan-role-transaksi-node-dan-descendant | Delete Group melepas penugasan Role Transaksi pada node yang dihapus dan descendant tanpa menyentuh penugasan ancestor | FE+BE | 21 | TC-FA-RP-1222 |
| TC-FA-RP-E2E-385-defense-in-depth-overlap-diterima-dan-role-sama-node-sama-ditolak-server | Defense-in-depth: Assign Role Transaksi tumpang tindih ancestor dan descendant diterima server, role sama pada node sama ditolak | FE+BE | 12 | TC-FA-RP-1224 |
| TC-FA-RP-E2E-386-picker-asset-admin-ber-constraint-node-sama-dan-descendant-ya-sibling-dan-ancestor-tidak | Picker Asset Admin untuk user ber-constraint: node sama dan descendant ya, sibling dan ancestor tidak | FE+BE | 20 | TC-FA-RP-1225, TC-FA-RP-1225, TC-FA-RP-1225 |
| TC-FA-RP-E2E-387-picker-user-tanpa-constraint-muncul-di-empat-role-pada-node-mana-pun | Picker Role Transaksi: user tanpa constraint muncul di keempat role pada node mana pun | FE+BE | 22 | TC-FA-RP-1226, TC-FA-RP-1226, TC-FA-RP-1226 |
| TC-FA-RP-E2E-388-gate-menilai-node-penugasan-baris-literal-descendant-tetap-eligible-di-luar-constraint-tidak | Gate menilai node penugasan: baris literal, descendant tetap eligible, node di luar constraint tidak | FE+BE | 21 | TC-FA-RP-1227, TC-FA-RP-1227, TC-FA-RP-1227 |
| TC-FA-RP-E2E-389-gate-sama-pada-picker-monitoring-report-staff-dan-approver | Gate Home Group yang sama berlaku pada picker Monitoring & Report, Staff, dan Approver | FE+BE | 26 | TC-FA-RP-1228, TC-FA-RP-1228 |
| TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint | Assign Total Control dan Read Only ke user ber-Home Group menulis baris pola Role Transaksi di semua group tanpa memeriksa constraint | FE+BE | 33 | TC-FA-RP-1229, TC-FA-RP-1230, TC-FA-RP-1229, TC-FA-RP-1230 |
| TC-FA-RP-E2E-391-baris-pola-gm-role-transaksi-tidak-dikecualikan-hanya-di-dalam-constraint | Baris pola Group Manager Role Transaksi tidak dikecualikan dari gate: penugasan di dalam constraint menulis baris pola hanya di dalam constraint | FE+BE | 21 | TC-FA-RP-1237, TC-FA-RP-1237, TC-FA-RP-1237 |
| TC-FA-RP-E2E-392-d-10-plural-group-role-role-transaksi-group-manager-dan-cancel | Dialog D-10 bentuk jamak memuat Group Role, Role Transaksi, dan Group Manager sekaligus, dan Cancel mempertahankan penugasan | FE+BE | 18 | TC-FA-RP-1231, TC-FA-RP-1232, TC-FA-RP-1232 |
| TC-FA-RP-E2E-393-absence-log-pencabutan-role-transaksi-via-d-10-silent-tanpa-notifikasi-dan-tanpa-entri-log | Absence log: pencabutan Role Transaksi lewat D-10 bersifat silent, tanpa notifikasi dan tanpa entri log | FE+BE | 33 | TC-FA-RP-1233, TC-FA-RP-1233, TC-FA-RP-1233 |
| TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog | Baris pola Total Control dan Read Only tidak didaftar D-10, dan constraint tanpa Role Transaksi di luar constraint tidak menampilkan dialog | FE+BE | 33 | TC-FA-RP-1234, TC-FA-RP-1235, TC-FA-RP-1234, TC-FA-RP-1235, TC-FA-RP-1234, TC-FA-RP-1234 |
| TC-FA-RP-E2E-395-tanpa-migrasi-penugasan-role-transaksi-lama-tetap-dan-assign-baru-tidak-tersedia | Tanpa migrasi: penugasan Role Transaksi lama di luar constraint tetap berlaku, sedangkan assign baru di luar constraint tidak tersedia | FE+BE | 8 | TC-FA-RP-1236, TC-FA-RP-1236 |
| TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima | Defense-in-depth: request langsung Assign Role Transaksi ke ancestor atau sibling constraint ditolak 422, ke node dalam constraint atau user tanpa constraint diterima | FE+BE | 16 | TC-FA-RP-1238, TC-FA-RP-1239, TC-FA-RP-1238, TC-FA-RP-1239, TC-FA-RP-1239 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua TC masuk minimal satu spec E2E.

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-RP-1 | E2E | TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | FE+BE |
| TC-FA-RP-2 | E2E | TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | FE+BE |
| TC-FA-RP-3 | E2E | TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | FE+BE |
| TC-FA-RP-4 | E2E | TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | FE+BE |
| TC-FA-RP-5 | E2E | TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | FE+BE |
| TC-FA-RP-6 | E2E | TC-FA-RP-E2E-001-screening-tab-total-control-read-only-group-manager-system-1 | FE+BE |
| TC-FA-RP-7 | E2E | TC-FA-RP-E2E-003-screening-tab-transaction-role-dan-panel-sub-tab-1 | FE+BE |
| TC-FA-RP-8 | E2E | TC-FA-RP-E2E-003-screening-tab-transaction-role-dan-panel-sub-tab-1 | FE+BE |
| TC-FA-RP-9 | E2E | TC-FA-RP-E2E-003-screening-tab-transaction-role-dan-panel-sub-tab-1 | FE+BE |
| TC-FA-RP-10 | E2E | TC-FA-RP-E2E-004-screening-tab-transaction-role-dan-panel-sub-tab-2 | FE+BE |
| TC-FA-RP-11 | E2E | TC-FA-RP-E2E-004-screening-tab-transaction-role-dan-panel-sub-tab-2 | FE+BE |
| TC-FA-RP-12 | E2E | TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | FE+BE |
| TC-FA-RP-13 | E2E | TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | FE+BE |
| TC-FA-RP-14 | E2E | TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | FE+BE |
| TC-FA-RP-15 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-16 | E2E | TC-FA-RP-E2E-005-screening-detail-role-matriks-crud-global-role-dan-group-role-1 | FE+BE |
| TC-FA-RP-17 | E2E | TC-FA-RP-E2E-005-screening-detail-role-matriks-crud-global-role-dan-group-role-1 | FE+BE |
| TC-FA-RP-18 | E2E | TC-FA-RP-E2E-005-screening-detail-role-matriks-crud-global-role-dan-group-role-1 | FE+BE |
| TC-FA-RP-19 | E2E | TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2 | FE+BE |
| TC-FA-RP-20 | E2E | TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2 | FE+BE |
| TC-FA-RP-21 | E2E | TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2 | FE+BE |
| TC-FA-RP-22 | E2E | TC-FA-RP-E2E-006-screening-detail-role-matriks-crud-global-role-dan-group-role-2 | FE+BE |
| TC-FA-RP-23 | E2E | TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | FE+BE |
| TC-FA-RP-24 | E2E | TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | FE+BE |
| TC-FA-RP-25 | E2E | TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | FE+BE |
| TC-FA-RP-26 | E2E | TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | FE+BE |
| TC-FA-RP-27 | E2E | TC-FA-RP-E2E-007-screening-detail-role-matriks-crud-global-role-dan-group-role-3 | FE+BE |
| TC-FA-RP-28 | E2E | TC-FA-RP-E2E-008-screening-detail-role-matriks-crud-global-role-dan-group-role-4 | FE+BE |
| TC-FA-RP-29 | E2E | TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1 | FE+BE |
| TC-FA-RP-30 | E2E | TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1 | FE+BE |
| TC-FA-RP-31 | E2E | TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1 | FE+BE |
| TC-FA-RP-32 | E2E | TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2 | FE+BE |
| TC-FA-RP-33 | E2E | TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2 | FE+BE |
| TC-FA-RP-34 | E2E | TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2 | FE+BE |
| TC-FA-RP-35 | E2E | TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1 | FE+BE |
| TC-FA-RP-36 | E2E | TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1 | FE+BE |
| TC-FA-RP-37 | E2E | TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1 | FE+BE |
| TC-FA-RP-38 | E2E | TC-FA-RP-E2E-011-screening-popup-assign-dan-mekanik-table-user-picker-dasar-1 | FE+BE |
| TC-FA-RP-39 | E2E | TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2 | FE+BE |
| TC-FA-RP-40 | E2E | TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2 | FE+BE |
| TC-FA-RP-41 | E2E | TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2 | FE+BE |
| TC-FA-RP-42 | E2E | TC-FA-RP-E2E-012-screening-popup-assign-dan-mekanik-table-user-picker-dasar-2 | FE+BE |
| TC-FA-RP-43 | E2E | TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3 | FE+BE |
| TC-FA-RP-44 | E2E | TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3 | FE+BE |
| TC-FA-RP-45 | E2E | TC-FA-RP-E2E-013-screening-popup-assign-dan-mekanik-table-user-picker-dasar-3 | FE+BE |
| TC-FA-RP-46 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-47 | E2E | TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | FE+BE |
| TC-FA-RP-48 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-49 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-50 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-51 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-53 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-54 | E2E | TC-FA-RP-E2E-014-empty-state-genuinely-pada-client-tanpa-data | FE+BE |
| TC-FA-RP-55 | E2E | TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | FE+BE |
| TC-FA-RP-56 | E2E | TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | FE+BE |
| TC-FA-RP-57 | E2E | TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | FE+BE |
| TC-FA-RP-58 | E2E | TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1 | FE+BE |
| TC-FA-RP-59 | E2E | TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2 | FE+BE |
| TC-FA-RP-60 | E2E | TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2 | FE+BE |
| TC-FA-RP-61 | E2E | TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2 | FE+BE |
| TC-FA-RP-62 | E2E | TC-FA-RP-E2E-016-empty-state-hasil-pencarian-kosong-per-permukaan-2 | FE+BE |
| TC-FA-RP-63 | E2E | TC-FA-RP-E2E-004-screening-tab-transaction-role-dan-panel-sub-tab-2 | FE+BE |
| TC-FA-RP-64 | E2E | TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | FE+BE |
| TC-FA-RP-65 | E2E | TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | FE+BE |
| TC-FA-RP-66 | E2E | TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | FE+BE |
| TC-FA-RP-67 | E2E | TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | FE+BE |
| TC-FA-RP-68 | E2E | TC-FA-RP-E2E-017-resilience-baca-error-load-dan-try-again-per-permukaan-1 | FE+BE |
| TC-FA-RP-69 | E2E | TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2 | FE+BE |
| TC-FA-RP-70 | E2E | TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2 | FE+BE |
| TC-FA-RP-71 | E2E | TC-FA-RP-E2E-018-resilience-baca-error-load-dan-try-again-per-permukaan-2 | FE+BE |
| TC-FA-RP-72 | E2E | TC-FA-RP-E2E-295-loading-state-shimmer-tabel-total-control-dan-detail-role | FE+BE |
| TC-FA-RP-73 | E2E | TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | FE+BE |
| TC-FA-RP-74 | E2E | TC-FA-RP-E2E-002-screening-tab-total-control-read-only-group-manager-system-2 | FE+BE |
| TC-FA-RP-75 | E2E | TC-FA-RP-E2E-019-role-matrix-negatif-peran-tanpa-akses-modul | FE+BE |
| TC-FA-RP-76 | E2E | TC-FA-RP-E2E-019-role-matrix-negatif-peran-tanpa-akses-modul | FE+BE |
| TC-FA-RP-77 | E2E | TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | FE+BE |
| TC-FA-RP-78 | E2E | TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | FE+BE |
| TC-FA-RP-79 | E2E | TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | FE+BE |
| TC-FA-RP-80 | E2E | TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2 | FE+BE |
| TC-FA-RP-81 | E2E | TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2 | FE+BE |
| TC-FA-RP-82 | E2E | TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1 | FE+BE |
| TC-FA-RP-83 | E2E | TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2 | FE+BE |
| TC-FA-RP-84 | E2E | TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1 | FE+BE |
| TC-FA-RP-85 | E2E | TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1 | FE+BE |
| TC-FA-RP-86 | E2E | TC-FA-RP-E2E-022-role-matrix-kontrol-tab-total-control-read-only-dan-group-1 | FE+BE |
| TC-FA-RP-87 | E2E | TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2 | FE+BE |
| TC-FA-RP-88 | E2E | TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2 | FE+BE |
| TC-FA-RP-89 | E2E | TC-FA-RP-E2E-023-role-matrix-kontrol-tab-total-control-read-only-dan-group-2 | FE+BE |
| TC-FA-RP-90 | E2E | TC-FA-RP-E2E-024-role-matrix-kontrol-tab-total-control-read-only-dan-group-3 | FE+BE |
| TC-FA-RP-91 | E2E | TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1 | FE+BE |
| TC-FA-RP-92 | E2E | TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1 | FE+BE |
| TC-FA-RP-93 | E2E | TC-FA-RP-E2E-025-role-matrix-kontrol-detail-role-global-role-per-peran-1 | FE+BE |
| TC-FA-RP-94 | E2E | TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2 | FE+BE |
| TC-FA-RP-95 | E2E | TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2 | FE+BE |
| TC-FA-RP-96 | E2E | TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2 | FE+BE |
| TC-FA-RP-97 | E2E | TC-FA-RP-E2E-026-role-matrix-kontrol-detail-role-global-role-per-peran-2 | FE+BE |
| TC-FA-RP-98 | E2E | TC-FA-RP-E2E-027-role-matrix-kontrol-detail-role-group-role-per-peran-1 | FE+BE |
| TC-FA-RP-99 | E2E | TC-FA-RP-E2E-027-role-matrix-kontrol-detail-role-group-role-per-peran-1 | FE+BE |
| TC-FA-RP-100 | E2E | TC-FA-RP-E2E-027-role-matrix-kontrol-detail-role-group-role-per-peran-1 | FE+BE |
| TC-FA-RP-101 | E2E | TC-FA-RP-E2E-028-role-matrix-kontrol-detail-role-group-role-per-peran-2 | FE+BE |
| TC-FA-RP-102 | E2E | TC-FA-RP-E2E-028-role-matrix-kontrol-detail-role-group-role-per-peran-2 | FE+BE |
| TC-FA-RP-103 | E2E | TC-FA-RP-E2E-028-role-matrix-kontrol-detail-role-group-role-per-peran-2 | FE+BE |
| TC-FA-RP-104 | E2E | TC-FA-RP-E2E-029-role-matrix-kontrol-detail-role-group-role-per-peran-3 | FE+BE |
| TC-FA-RP-105 | E2E | TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1 | FE+BE |
| TC-FA-RP-106 | E2E | TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1 | FE+BE |
| TC-FA-RP-107 | E2E | TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1 | FE+BE |
| TC-FA-RP-108 | E2E | TC-FA-RP-E2E-030-role-matrix-kontrol-tab-transaction-role-per-peran-1 | FE+BE |
| TC-FA-RP-109 | E2E | TC-FA-RP-E2E-031-role-matrix-kontrol-tab-transaction-role-per-peran-2 | FE+BE |
| TC-FA-RP-110 | E2E | TC-FA-RP-E2E-031-role-matrix-kontrol-tab-transaction-role-per-peran-2 | FE+BE |
| TC-FA-RP-111 | E2E | TC-FA-RP-E2E-031-role-matrix-kontrol-tab-transaction-role-per-peran-2 | FE+BE |
| TC-FA-RP-112 | E2E | TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1 | FE+BE |
| TC-FA-RP-113 | E2E | TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1 | FE+BE |
| TC-FA-RP-114 | E2E | TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1 | FE+BE |
| TC-FA-RP-115 | E2E | TC-FA-RP-E2E-032-role-matrix-panel-approval-settings-registration-per-peran-1 | FE+BE |
| TC-FA-RP-116 | E2E | TC-FA-RP-E2E-033-role-matrix-panel-approval-settings-registration-per-peran-2 | FE+BE |
| TC-FA-RP-117 | E2E | TC-FA-RP-E2E-033-role-matrix-panel-approval-settings-registration-per-peran-2 | FE+BE |
| TC-FA-RP-118 | E2E | TC-FA-RP-E2E-033-role-matrix-panel-approval-settings-registration-per-peran-2 | FE+BE |
| TC-FA-RP-119 | E2E | TC-FA-RP-E2E-297-role-matrix-ikon-download-dan-changelog-tampil-per-peran | FE+BE |
| TC-FA-RP-120 | E2E | TC-FA-RP-E2E-034-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-1 | FE+BE |
| TC-FA-RP-121 | E2E | TC-FA-RP-E2E-034-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-1 | FE+BE |
| TC-FA-RP-122 | E2E | TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | FE+BE |
| TC-FA-RP-123 | E2E | TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | FE+BE |
| TC-FA-RP-124 | E2E | TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | FE+BE |
| TC-FA-RP-125 | E2E | TC-FA-RP-E2E-037-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-2 | FE+BE |
| TC-FA-RP-126 | E2E | TC-FA-RP-E2E-037-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-2 | FE+BE |
| TC-FA-RP-127 | E2E | TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | FE+BE |
| TC-FA-RP-128 | E2E | TC-FA-RP-E2E-036-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-1 | FE+BE |
| TC-FA-RP-129 | E2E | TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | FE+BE |
| TC-FA-RP-130 | E2E | TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | FE+BE |
| TC-FA-RP-131 | E2E | TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | FE+BE |
| TC-FA-RP-132 | E2E | TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | FE+BE |
| TC-FA-RP-133 | E2E | TC-FA-RP-E2E-038-role-matrix-guard-target-terlindungi-oleh-manage-global-user-1 | FE+BE |
| TC-FA-RP-134 | E2E | TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | FE+BE |
| TC-FA-RP-135 | E2E | TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | FE+BE |
| TC-FA-RP-136 | E2E | TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | FE+BE |
| TC-FA-RP-137 | E2E | TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | FE+BE |
| TC-FA-RP-138 | E2E | TC-FA-RP-E2E-039-role-matrix-guard-target-terlindungi-oleh-manage-global-user-2 | FE+BE |
| TC-FA-RP-139 | E2E | TC-FA-RP-E2E-040-role-matrix-guard-target-terlindungi-oleh-group-manager-1 | FE+BE |
| TC-FA-RP-140 | E2E | TC-FA-RP-E2E-040-role-matrix-guard-target-terlindungi-oleh-group-manager-1 | FE+BE |
| TC-FA-RP-141 | E2E | TC-FA-RP-E2E-040-role-matrix-guard-target-terlindungi-oleh-group-manager-1 | FE+BE |
| TC-FA-RP-142 | E2E | TC-FA-RP-E2E-041-role-matrix-guard-target-terlindungi-oleh-group-manager-2 | FE+BE |
| TC-FA-RP-143 | E2E | TC-FA-RP-E2E-041-role-matrix-guard-target-terlindungi-oleh-group-manager-2 | FE+BE |
| TC-FA-RP-144 | E2E | TC-FA-RP-E2E-041-role-matrix-guard-target-terlindungi-oleh-group-manager-2 | FE+BE |
| TC-FA-RP-145 | E2E | TC-FA-RP-E2E-042-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-1 | FE+BE |
| TC-FA-RP-146 | E2E | TC-FA-RP-E2E-042-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-1 | FE+BE |
| TC-FA-RP-147 | E2E | TC-FA-RP-E2E-042-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-1 | FE+BE |
| TC-FA-RP-148 | E2E | TC-FA-RP-E2E-043-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-2 | FE+BE |
| TC-FA-RP-149 | E2E | TC-FA-RP-E2E-043-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-2 | FE+BE |
| TC-FA-RP-150 | E2E | TC-FA-RP-E2E-043-role-matrix-guard-target-terlindungi-oleh-manage-user-dan-2 | FE+BE |
| TC-FA-RP-151 | E2E | TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | FE+BE |
| TC-FA-RP-152 | E2E | TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | FE+BE |
| TC-FA-RP-153 | E2E | TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | FE+BE |
| TC-FA-RP-154 | E2E | TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | FE+BE |
| TC-FA-RP-155 | E2E | TC-FA-RP-E2E-044-role-matrix-guard-target-terlindungi-oleh-total-control-dan-1 | FE+BE |
| TC-FA-RP-156 | E2E | TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2 | FE+BE |
| TC-FA-RP-157 | E2E | TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2 | FE+BE |
| TC-FA-RP-158 | E2E | TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2 | FE+BE |
| TC-FA-RP-159 | E2E | TC-FA-RP-E2E-045-role-matrix-guard-target-terlindungi-oleh-total-control-dan-2 | FE+BE |
| TC-FA-RP-160 | E2E | TC-FA-RP-E2E-046-role-matrix-gating-remove-tabel-role-transaksi-per-peran | FE+BE |
| TC-FA-RP-161 | E2E | TC-FA-RP-E2E-046-role-matrix-gating-remove-tabel-role-transaksi-per-peran | FE+BE |
| TC-FA-RP-162 | E2E | TC-FA-RP-E2E-046-role-matrix-gating-remove-tabel-role-transaksi-per-peran | FE+BE |
| TC-FA-RP-163 | E2E | TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-164 | E2E | TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-165 | E2E | TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-166 | E2E | TC-FA-RP-E2E-047-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-167 | E2E | TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-168 | E2E | TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-169 | E2E | TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-170 | E2E | TC-FA-RP-E2E-048-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-171 | E2E | TC-FA-RP-E2E-049-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-172 | E2E | TC-FA-RP-E2E-049-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-173 | E2E | TC-FA-RP-E2E-049-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-174 | E2E | TC-FA-RP-E2E-049-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-1 | FE+BE |
| TC-FA-RP-175 | E2E | TC-FA-RP-E2E-050-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-176 | E2E | TC-FA-RP-E2E-050-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-177 | E2E | TC-FA-RP-E2E-050-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-178 | E2E | TC-FA-RP-E2E-050-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-manage-2 | FE+BE |
| TC-FA-RP-179 | E2E | TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1 | FE+BE |
| TC-FA-RP-180 | E2E | TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1 | FE+BE |
| TC-FA-RP-181 | E2E | TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1 | FE+BE |
| TC-FA-RP-182 | E2E | TC-FA-RP-E2E-051-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-1 | FE+BE |
| TC-FA-RP-183 | E2E | TC-FA-RP-E2E-052-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-2 | FE+BE |
| TC-FA-RP-184 | E2E | TC-FA-RP-E2E-052-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-2 | FE+BE |
| TC-FA-RP-185 | E2E | TC-FA-RP-E2E-052-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-2 | FE+BE |
| TC-FA-RP-186 | E2E | TC-FA-RP-E2E-052-role-matrix-positif-eksekusi-aksi-sampai-sukses-oleh-group-2 | FE+BE |
| TC-FA-RP-187 | E2E | TC-FA-RP-E2E-056-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-1 | FE+BE |
| TC-FA-RP-188 | E2E | TC-FA-RP-E2E-056-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-1 | FE+BE |
| TC-FA-RP-189 | E2E | TC-FA-RP-E2E-056-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-1 | FE+BE |
| TC-FA-RP-190 | E2E | TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2 | FE+BE |
| TC-FA-RP-191 | E2E | TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2 | FE+BE |
| TC-FA-RP-192 | E2E | TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2 | FE+BE |
| TC-FA-RP-193 | E2E | TC-FA-RP-E2E-059-assign-read-only-1 | FE+BE |
| TC-FA-RP-194 | E2E | TC-FA-RP-E2E-059-assign-read-only-1 | FE+BE |
| TC-FA-RP-195 | E2E | TC-FA-RP-E2E-059-assign-read-only-1 | FE+BE |
| TC-FA-RP-196 | E2E | TC-FA-RP-E2E-059-assign-read-only-1 | FE+BE |
| TC-FA-RP-197 | E2E | TC-FA-RP-E2E-060-assign-read-only-2 | FE+BE |
| TC-FA-RP-198 | E2E | TC-FA-RP-E2E-060-assign-read-only-2 | FE+BE |
| TC-FA-RP-199 | E2E | TC-FA-RP-E2E-057-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-2 | FE+BE |
| TC-FA-RP-200 | E2E | TC-FA-RP-E2E-060-assign-read-only-2 | FE+BE |
| TC-FA-RP-201 | E2E | TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | FE+BE |
| TC-FA-RP-202 | E2E | TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | FE+BE |
| TC-FA-RP-203 | E2E | TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | FE+BE |
| TC-FA-RP-204 | E2E | TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | FE+BE |
| TC-FA-RP-205 | E2E | TC-FA-RP-E2E-061-remove-total-control-1 | FE+BE |
| TC-FA-RP-206 | E2E | TC-FA-RP-E2E-061-remove-total-control-1 | FE+BE |
| TC-FA-RP-207 | E2E | TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | FE+BE |
| TC-FA-RP-208 | E2E | TC-FA-RP-E2E-061-remove-total-control-1 | FE+BE |
| TC-FA-RP-209 | E2E | TC-FA-RP-E2E-061-remove-total-control-1 | FE+BE |
| TC-FA-RP-210 | E2E | TC-FA-RP-E2E-061-remove-total-control-1 | FE+BE |
| TC-FA-RP-211 | E2E | TC-FA-RP-E2E-064-remove-read-only-1 | FE+BE |
| TC-FA-RP-212 | E2E | TC-FA-RP-E2E-064-remove-read-only-1 | FE+BE |
| TC-FA-RP-213 | E2E | TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | FE+BE |
| TC-FA-RP-214 | E2E | TC-FA-RP-E2E-064-remove-read-only-1 | FE+BE |
| TC-FA-RP-215 | E2E | TC-FA-RP-E2E-064-remove-read-only-1 | FE+BE |
| TC-FA-RP-216 | E2E | TC-FA-RP-E2E-064-remove-read-only-1 | FE+BE |
| TC-FA-RP-217 | E2E | TC-FA-RP-E2E-062-remove-total-control-2 | FE+BE |
| TC-FA-RP-218 | E2E | TC-FA-RP-E2E-065-remove-read-only-2 | FE+BE |
| TC-FA-RP-219 | E2E | TC-FA-RP-E2E-066-assign-group-manager-1 | FE+BE |
| TC-FA-RP-220 | E2E | TC-FA-RP-E2E-066-assign-group-manager-1 | FE+BE |
| TC-FA-RP-221 | E2E | TC-FA-RP-E2E-066-assign-group-manager-1 | FE+BE |
| TC-FA-RP-222 | E2E | TC-FA-RP-E2E-066-assign-group-manager-1 | FE+BE |
| TC-FA-RP-223 | E2E | TC-FA-RP-E2E-067-assign-group-manager-2 | FE+BE |
| TC-FA-RP-224 | E2E | TC-FA-RP-E2E-067-assign-group-manager-2 | FE+BE |
| TC-FA-RP-225 | E2E | TC-FA-RP-E2E-067-assign-group-manager-2 | FE+BE |
| TC-FA-RP-226 | E2E | TC-FA-RP-E2E-067-assign-group-manager-2 | FE+BE |
| TC-FA-RP-227 | E2E | TC-FA-RP-E2E-067-assign-group-manager-2 | FE+BE |
| TC-FA-RP-228 | E2E | TC-FA-RP-E2E-068-assign-group-manager-3 | FE+BE |
| TC-FA-RP-229 | E2E | TC-FA-RP-E2E-068-assign-group-manager-3 | FE+BE |
| TC-FA-RP-230 | E2E | TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1 | FE+BE |
| TC-FA-RP-231 | E2E | TC-FA-RP-E2E-068-assign-group-manager-3 | FE+BE |
| TC-FA-RP-232 | E2E | TC-FA-RP-E2E-069-assign-group-manager-4 | FE+BE |
| TC-FA-RP-233 | E2E | TC-FA-RP-E2E-069-assign-group-manager-4 | FE+BE |
| TC-FA-RP-234 | E2E | TC-FA-RP-E2E-068-assign-group-manager-3 | FE+BE |
| TC-FA-RP-235 | E2E | TC-FA-RP-E2E-070-remove-group-manager-1 | FE+BE |
| TC-FA-RP-236 | E2E | TC-FA-RP-E2E-070-remove-group-manager-1 | FE+BE |
| TC-FA-RP-237 | E2E | TC-FA-RP-E2E-070-remove-group-manager-1 | FE+BE |
| TC-FA-RP-238 | E2E | TC-FA-RP-E2E-071-remove-group-manager-2 | FE+BE |
| TC-FA-RP-239 | E2E | TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | FE+BE |
| TC-FA-RP-240 | E2E | TC-FA-RP-E2E-070-remove-group-manager-1 | FE+BE |
| TC-FA-RP-241 | E2E | TC-FA-RP-E2E-072-assign-user-ke-global-role-di-detail-role | FE+BE |
| TC-FA-RP-242 | E2E | TC-FA-RP-E2E-072-assign-user-ke-global-role-di-detail-role | FE+BE |
| TC-FA-RP-243 | E2E | TC-FA-RP-E2E-072-assign-user-ke-global-role-di-detail-role | FE+BE |
| TC-FA-RP-244 | E2E | TC-FA-RP-E2E-300-assign-user-ke-global-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-245 | E2E | TC-FA-RP-E2E-300-assign-user-ke-global-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-246 | E2E | TC-FA-RP-E2E-300-assign-user-ke-global-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-247 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-248 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-249 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-250 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-251 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-252 | E2E | TC-FA-RP-E2E-073-assign-user-ke-group-role-di-detail-role-1 | FE+BE |
| TC-FA-RP-253 | E2E | TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4 | FE+BE |
| TC-FA-RP-254 | E2E | TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4 | FE+BE |
| TC-FA-RP-255 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-256 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-257 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-258 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-259 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-260 | E2E | TC-FA-RP-E2E-074-assign-user-ke-group-role-di-detail-role-2 | FE+BE |
| TC-FA-RP-261 | E2E | TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | FE+BE |
| TC-FA-RP-262 | E2E | TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4 | FE+BE |
| TC-FA-RP-263 | E2E | TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | FE+BE |
| TC-FA-RP-264 | E2E | TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | FE+BE |
| TC-FA-RP-265 | E2E | TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1 | FE+BE |
| TC-FA-RP-266 | E2E | TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1 | FE+BE |
| TC-FA-RP-267 | E2E | TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1 | FE+BE |
| TC-FA-RP-268 | E2E | TC-FA-RP-E2E-079-edit-matriks-crud-detail-role-1 | FE+BE |
| TC-FA-RP-269 | E2E | TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | FE+BE |
| TC-FA-RP-270 | E2E | TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | FE+BE |
| TC-FA-RP-271 | E2E | TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | FE+BE |
| TC-FA-RP-272 | E2E | TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | FE+BE |
| TC-FA-RP-273 | E2E | TC-FA-RP-E2E-080-edit-matriks-crud-detail-role-2 | FE+BE |
| TC-FA-RP-274 | E2E | TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | FE+BE |
| TC-FA-RP-275 | E2E | TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | FE+BE |
| TC-FA-RP-276 | E2E | TC-FA-RP-E2E-296-dua-sesi-total-control-toast-netral-untuk-nilai-sama | FE+BE |
| TC-FA-RP-277 | E2E | TC-FA-RP-E2E-081-edit-matriks-crud-detail-role-3 | FE+BE |
| TC-FA-RP-278 | E2E | TC-FA-RP-E2E-081-edit-matriks-crud-detail-role-3 | FE+BE |
| TC-FA-RP-279 | E2E | TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1 | FE+BE |
| TC-FA-RP-280 | E2E | TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1 | FE+BE |
| TC-FA-RP-281 | E2E | TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1 | FE+BE |
| TC-FA-RP-282 | E2E | TC-FA-RP-E2E-082-remove-baris-peran-satu-per-satu-1 | FE+BE |
| TC-FA-RP-283 | E2E | TC-FA-RP-E2E-083-remove-baris-peran-satu-per-satu-2; TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui | FE+BE |
| TC-FA-RP-284 | E2E | TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | FE+BE |
| TC-FA-RP-285 | E2E | TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1 | FE+BE |
| TC-FA-RP-286 | E2E | TC-FA-RP-E2E-087-volume-data-company-volume-seleksi-bulk-selection-limit-dan-1 | FE+BE |
| TC-FA-RP-287 | E2E | TC-FA-RP-E2E-087-volume-data-company-volume-seleksi-bulk-selection-limit-dan-1 | FE+BE |
| TC-FA-RP-288 | E2E | TC-FA-RP-E2E-087-volume-data-company-volume-seleksi-bulk-selection-limit-dan-1 | FE+BE |
| TC-FA-RP-289 | E2E | TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | FE+BE |
| TC-FA-RP-290 | E2E | TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | FE+BE |
| TC-FA-RP-291 | E2E | TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | FE+BE |
| TC-FA-RP-292 | E2E | TC-FA-RP-E2E-084-checkbox-seleksi-baris-terlindungi | FE+BE |
| TC-FA-RP-293 | E2E | TC-FA-RP-E2E-084-checkbox-seleksi-baris-terlindungi | FE+BE |
| TC-FA-RP-294 | E2E | TC-FA-RP-E2E-084-checkbox-seleksi-baris-terlindungi | FE+BE |
| TC-FA-RP-295 | E2E | TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | FE+BE |
| TC-FA-RP-296 | E2E | TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | FE+BE |
| TC-FA-RP-297 | E2E | TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | FE+BE |
| TC-FA-RP-298 | E2E | TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | FE+BE |
| TC-FA-RP-299 | E2E | TC-FA-RP-E2E-302-bulk-remove-hasil-parsial-dan-diblok-oleh-admin-lain | FE+BE |
| TC-FA-RP-300 | E2E | TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui; TC-FA-RP-E2E-302-bulk-remove-hasil-parsial-dan-diblok-oleh-admin-lain | FE+BE |
| TC-FA-RP-301 | E2E | TC-FA-RP-E2E-085-bulk-remove-dialog-hasil-dan-cancel-1 | FE+BE |
| TC-FA-RP-302 | E2E | TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2 | FE+BE |
| TC-FA-RP-303 | E2E | TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2 | FE+BE |
| TC-FA-RP-304 | E2E | TC-FA-RP-E2E-086-bulk-remove-dialog-hasil-dan-cancel-2 | FE+BE |
| TC-FA-RP-305 | E2E | TC-FA-RP-E2E-092-mobile-mode-checkbox-floating-bottom-bulk-bar-dan-select-all | FE+BE |
| TC-FA-RP-306 | E2E | TC-FA-RP-E2E-092-mobile-mode-checkbox-floating-bottom-bulk-bar-dan-select-all | FE+BE |
| TC-FA-RP-307 | E2E | TC-FA-RP-E2E-092-mobile-mode-checkbox-floating-bottom-bulk-bar-dan-select-all | FE+BE |
| TC-FA-RP-308 | E2E | TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | FE+BE |
| TC-FA-RP-309 | E2E | TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | FE+BE |
| TC-FA-RP-310 | E2E | TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | FE+BE |
| TC-FA-RP-311 | E2E | TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | FE+BE |
| TC-FA-RP-312 | E2E | TC-FA-RP-E2E-094-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-1 | FE+BE |
| TC-FA-RP-313 | E2E | TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2 | FE+BE |
| TC-FA-RP-314 | E2E | TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2 | FE+BE |
| TC-FA-RP-315 | E2E | TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2 | FE+BE |
| TC-FA-RP-316 | E2E | TC-FA-RP-E2E-095-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-2 | FE+BE |
| TC-FA-RP-317 | E2E | TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3 | FE+BE |
| TC-FA-RP-318 | E2E | TC-FA-RP-E2E-301-assign-role-transaksi-kandidat-picker-bagi-pemegang-manage-user-dan-role | FE+BE |
| TC-FA-RP-319 | E2E | TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3 | FE+BE |
| TC-FA-RP-320 | E2E | TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1 | FE+BE |
| TC-FA-RP-321 | E2E | TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1 | FE+BE |
| TC-FA-RP-322 | E2E | TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1 | FE+BE |
| TC-FA-RP-323 | E2E | TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1 | FE+BE |
| TC-FA-RP-324 | E2E | TC-FA-RP-E2E-099-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-2 | FE+BE |
| TC-FA-RP-325 | E2E | TC-FA-RP-E2E-099-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-2 | FE+BE |
| TC-FA-RP-326 | E2E | TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1 | FE+BE |
| TC-FA-RP-327 | E2E | TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1 | FE+BE |
| TC-FA-RP-328 | E2E | TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1 | FE+BE |
| TC-FA-RP-329 | E2E | TC-FA-RP-E2E-100-role-transaksi-node-exact-sub-tab-dan-remove-1 | FE+BE |
| TC-FA-RP-330 | E2E | TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2 | FE+BE |
| TC-FA-RP-331 | E2E | TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2 | FE+BE |
| TC-FA-RP-332 | E2E | TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2 | FE+BE |
| TC-FA-RP-333 | E2E | TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2 | FE+BE |
| TC-FA-RP-334 | E2E | TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2 | FE+BE |
| TC-FA-RP-335 | E2E | TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2 | FE+BE |
| TC-FA-RP-336 | E2E | TC-FA-RP-E2E-102-require-approval-transaction-role-prasyarat-aktivasi-1 | FE+BE |
| TC-FA-RP-337 | E2E | TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1 | FE+BE |
| TC-FA-RP-338 | E2E | TC-FA-RP-E2E-102-require-approval-transaction-role-prasyarat-aktivasi-1 | FE+BE |
| TC-FA-RP-339 | E2E | TC-FA-RP-E2E-102-require-approval-transaction-role-prasyarat-aktivasi-1 | FE+BE |
| TC-FA-RP-340 | E2E | TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2 | FE+BE |
| TC-FA-RP-341 | E2E | TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2 | FE+BE |
| TC-FA-RP-342 | E2E | TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2 | FE+BE |
| TC-FA-RP-343 | E2E | TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1 | FE+BE |
| TC-FA-RP-344 | E2E | TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1 | FE+BE |
| TC-FA-RP-345 | E2E | TC-FA-RP-E2E-303-require-approval-transaction-role-toggle-radio-aturan-dan-3 | FE+BE |
| TC-FA-RP-346 | E2E | TC-FA-RP-E2E-104-require-approval-transaction-role-toggle-radio-aturan-dan-1 | FE+BE |
| TC-FA-RP-347 | E2E | TC-FA-RP-E2E-303-require-approval-transaction-role-toggle-radio-aturan-dan-3 | FE+BE |
| TC-FA-RP-348 | E2E | TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2 | FE+BE |
| TC-FA-RP-349 | E2E | TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2 | FE+BE |
| TC-FA-RP-350 | E2E | TC-FA-RP-E2E-296-dua-sesi-total-control-toast-netral-untuk-nilai-sama | FE+BE |
| TC-FA-RP-351 | E2E | TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1 | FE+BE |
| TC-FA-RP-352 | E2E | TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1 | FE+BE |
| TC-FA-RP-353 | E2E | TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1 | FE+BE |
| TC-FA-RP-354 | E2E | TC-FA-RP-E2E-304-require-approval-prasyarat-aktivasi-dicek-ulang-approver-terakhir-dilepas | FE+BE |
| TC-FA-RP-355 | E2E | TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2 | FE+BE |
| TC-FA-RP-356 | E2E | TC-FA-RP-E2E-106-approval-scope-sub-tab-transfer-1 | FE+BE |
| TC-FA-RP-357 | E2E | TC-FA-RP-E2E-106-approval-scope-sub-tab-transfer-1; TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui | FE+BE |
| TC-FA-RP-358 | E2E | TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1 | FE+BE |
| TC-FA-RP-359 | E2E | TC-FA-RP-E2E-106-approval-scope-sub-tab-transfer-1 | FE+BE |
| TC-FA-RP-360 | E2E | TC-FA-RP-E2E-105-require-approval-transaction-role-toggle-radio-aturan-dan-2 | FE+BE |
| TC-FA-RP-361 | E2E | TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | FE+BE |
| TC-FA-RP-362 | E2E | TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | FE+BE |
| TC-FA-RP-363 | E2E | TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | FE+BE |
| TC-FA-RP-364 | E2E | TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | FE+BE |
| TC-FA-RP-371 | E2E | TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1 | FE+BE |
| TC-FA-RP-372 | E2E | TC-FA-RP-E2E-296-dua-sesi-total-control-toast-netral-untuk-nilai-sama | FE+BE |
| TC-FA-RP-373 | E2E | TC-FA-RP-E2E-289-resilience-kegagalan-pada-require-approval-approval-scope-dan-2 | FE+BE |
| TC-FA-RP-374 | E2E | TC-FA-RP-E2E-110-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-1 | FE+BE |
| TC-FA-RP-375 | E2E | TC-FA-RP-E2E-110-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-1 | FE+BE |
| TC-FA-RP-376 | E2E | TC-FA-RP-E2E-110-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-1 | FE+BE |
| TC-FA-RP-377 | E2E | TC-FA-RP-E2E-111-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-2 | FE+BE |
| TC-FA-RP-378 | E2E | TC-FA-RP-E2E-111-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-2 | FE+BE |
| TC-FA-RP-379 | E2E | TC-FA-RP-E2E-111-persetujuan-registrasi-aset-d-09-saat-uncheck-update-dan-2 | FE+BE |
| TC-FA-RP-380 | E2E | TC-FA-RP-E2E-112-auto-revert-total-control-1 | FE+BE |
| TC-FA-RP-381 | E2E | TC-FA-RP-E2E-112-auto-revert-total-control-1 | FE+BE |
| TC-FA-RP-382 | E2E | TC-FA-RP-E2E-112-auto-revert-total-control-1 | FE+BE |
| TC-FA-RP-383 | E2E | TC-FA-RP-E2E-113-auto-revert-total-control-2 | FE+BE |
| TC-FA-RP-384 | E2E | TC-FA-RP-E2E-113-auto-revert-total-control-2 | FE+BE |
| TC-FA-RP-385 | E2E | TC-FA-RP-E2E-115-auto-revert-read-only-1 | FE+BE |
| TC-FA-RP-386 | E2E | TC-FA-RP-E2E-115-auto-revert-read-only-1 | FE+BE |
| TC-FA-RP-387 | E2E | TC-FA-RP-E2E-115-auto-revert-read-only-1 | FE+BE |
| TC-FA-RP-388 | E2E | TC-FA-RP-E2E-116-auto-revert-read-only-2 | FE+BE |
| TC-FA-RP-389 | E2E | TC-FA-RP-E2E-116-auto-revert-read-only-2 | FE+BE |
| TC-FA-RP-390 | E2E | TC-FA-RP-E2E-113-auto-revert-total-control-2 | FE+BE |
| TC-FA-RP-391 | E2E | TC-FA-RP-E2E-289-resilience-kegagalan-pada-require-approval-approval-scope-dan-2 | FE+BE |
| TC-FA-RP-392 | E2E | TC-FA-RP-E2E-289-resilience-kegagalan-pada-require-approval-approval-scope-dan-2 | FE+BE |
| TC-FA-RP-393 | E2E | TC-FA-RP-E2E-114-auto-revert-total-control-3 | FE+BE |
| TC-FA-RP-394 | E2E | TC-FA-RP-E2E-113-auto-revert-total-control-2 | FE+BE |
| TC-FA-RP-395 | E2E | TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1 | FE+BE |
| TC-FA-RP-396 | E2E | TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1 | FE+BE |
| TC-FA-RP-397 | E2E | TC-FA-RP-E2E-373-remove-baris-group-role-target-gm-di-node-gm-nya-dialog-d05-varian-remove-baris | FE+BE |
| TC-FA-RP-398 | E2E | TC-FA-RP-E2E-117-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-1 | FE+BE |
| TC-FA-RP-399 | E2E | TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2 | FE+BE |
| TC-FA-RP-400 | E2E | TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2 | FE+BE |
| TC-FA-RP-401 | E2E | TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2 | FE+BE |
| TC-FA-RP-402 | E2E | TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | FE+BE |
| TC-FA-RP-403 | E2E | TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | FE+BE |
| TC-FA-RP-404 | E2E | TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | FE+BE |
| TC-FA-RP-405 | E2E | TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | FE+BE |
| TC-FA-RP-406 | E2E | TC-FA-RP-E2E-119-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-1 | FE+BE |
| TC-FA-RP-407 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-408 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-409 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-410 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-411 | E2E | TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3 | FE+BE |
| TC-FA-RP-412 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-413 | E2E | TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1; TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui | FE+BE |
| TC-FA-RP-414 | E2E | TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1 | FE+BE |
| TC-FA-RP-415 | E2E | TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1 | FE+BE |
| TC-FA-RP-416 | E2E | TC-FA-RP-E2E-122-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-1 | FE+BE |
| TC-FA-RP-417 | E2E | TC-FA-RP-E2E-123-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-2 | FE+BE |
| TC-FA-RP-418 | E2E | TC-FA-RP-E2E-123-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-2 | FE+BE |
| TC-FA-RP-419 | E2E | TC-FA-RP-E2E-123-table-user-picker-kontrak-submit-stale-dan-tidak-eligible-2 | FE+BE |
| TC-FA-RP-420 | E2E | TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | FE+BE |
| TC-FA-RP-421 | E2E | TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | FE+BE |
| TC-FA-RP-422 | E2E | TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | FE+BE |
| TC-FA-RP-423 | E2E | TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | FE+BE |
| TC-FA-RP-424 | E2E | TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | FE+BE |
| TC-FA-RP-425 | E2E | TC-FA-RP-E2E-124-popup-assign-penutupan-saving-state-dan-aksesibilitas | FE+BE |
| TC-FA-RP-426 | E2E | TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | FE+BE |
| TC-FA-RP-427 | E2E | TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | FE+BE |
| TC-FA-RP-428 | E2E | TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | FE+BE |
| TC-FA-RP-429 | E2E | TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | FE+BE |
| TC-FA-RP-430 | E2E | TC-FA-RP-E2E-125-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-1 | FE+BE |
| TC-FA-RP-431 | E2E | TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | FE+BE |
| TC-FA-RP-432 | E2E | TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | FE+BE |
| TC-FA-RP-433 | E2E | TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | FE+BE |
| TC-FA-RP-434 | E2E | TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | FE+BE |
| TC-FA-RP-435 | E2E | TC-FA-RP-E2E-126-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-2 | FE+BE |
| TC-FA-RP-436 | E2E | TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3 | FE+BE |
| TC-FA-RP-437 | E2E | TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3 | FE+BE |
| TC-FA-RP-438 | E2E | TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3 | FE+BE |
| TC-FA-RP-439 | E2E | TC-FA-RP-E2E-127-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-3 | FE+BE |
| TC-FA-RP-440 | E2E | TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4 | FE+BE |
| TC-FA-RP-441 | E2E | TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | FE+BE |
| TC-FA-RP-442 | E2E | TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | FE+BE |
| TC-FA-RP-443 | E2E | TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | FE+BE |
| TC-FA-RP-444 | E2E | TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | FE+BE |
| TC-FA-RP-445 | E2E | TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | FE+BE |
| TC-FA-RP-446 | E2E | TC-FA-RP-E2E-129-penugasan-otomatis-pembuat-group | FE+BE |
| TC-FA-RP-447 | E2E | TC-FA-RP-E2E-285-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-2 | FE+BE |
| TC-FA-RP-448 | E2E | TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait | FE+BE |
| TC-FA-RP-449 | E2E | TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait | FE+BE |
| TC-FA-RP-450 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-451 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-452 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-453 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-454 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-455 | E2E | TC-FA-RP-E2E-131-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-1 | FE+BE |
| TC-FA-RP-456 | E2E | TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | FE+BE |
| TC-FA-RP-457 | E2E | TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | FE+BE |
| TC-FA-RP-458 | E2E | TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | FE+BE |
| TC-FA-RP-459 | E2E | TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | FE+BE |
| TC-FA-RP-460 | E2E | TC-FA-RP-E2E-132-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-2 | FE+BE |
| TC-FA-RP-461 | E2E | TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui; TC-FA-RP-E2E-305-remove-role-transaksi-baris-sudah-dihapus-sesi-lain | FE+BE |
| TC-FA-RP-462 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-463 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-464 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-465 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-466 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-467 | E2E | TC-FA-RP-E2E-134-sub-tab-addon-dengan-lisensi-nonaktif-dan-aktif | FE+BE |
| TC-FA-RP-469 | E2E | TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait | FE+BE |
| TC-FA-RP-470 | E2E | TC-FA-RP-E2E-130-delete-group-pelepasan-penugasan-dan-nilai-terkait | FE+BE |
| TC-FA-RP-471 | E2E | TC-FA-RP-E2E-135-tab-total-control-search-1 | FE+BE |
| TC-FA-RP-472 | E2E | TC-FA-RP-E2E-136-tab-total-control-search-2 | FE+BE |
| TC-FA-RP-473 | E2E | TC-FA-RP-E2E-136-tab-total-control-search-2 | FE+BE |
| TC-FA-RP-474 | E2E | TC-FA-RP-E2E-137-tab-total-control-search-3 | FE+BE |
| TC-FA-RP-475 | E2E | TC-FA-RP-E2E-137-tab-total-control-search-3 | FE+BE |
| TC-FA-RP-476 | E2E | TC-FA-RP-E2E-137-tab-total-control-search-3 | FE+BE |
| TC-FA-RP-477 | E2E | TC-FA-RP-E2E-137-tab-total-control-search-3 | FE+BE |
| TC-FA-RP-478 | E2E | TC-FA-RP-E2E-137-tab-total-control-search-3 | FE+BE |
| TC-FA-RP-479 | E2E | TC-FA-RP-E2E-138-tab-total-control-search-4 | FE+BE |
| TC-FA-RP-480 | E2E | TC-FA-RP-E2E-139-tab-total-control-filter-1 | FE+BE |
| TC-FA-RP-481 | E2E | TC-FA-RP-E2E-139-tab-total-control-filter-1 | FE+BE |
| TC-FA-RP-482 | E2E | TC-FA-RP-E2E-139-tab-total-control-filter-1 | FE+BE |
| TC-FA-RP-483 | E2E | TC-FA-RP-E2E-140-tab-total-control-filter-2 | FE+BE |
| TC-FA-RP-484 | E2E | TC-FA-RP-E2E-140-tab-total-control-filter-2 | FE+BE |
| TC-FA-RP-485 | E2E | TC-FA-RP-E2E-140-tab-total-control-filter-2 | FE+BE |
| TC-FA-RP-486 | E2E | TC-FA-RP-E2E-140-tab-total-control-filter-2 | FE+BE |
| TC-FA-RP-487 | E2E | TC-FA-RP-E2E-141-tab-total-control-filter-3 | FE+BE |
| TC-FA-RP-488 | E2E | TC-FA-RP-E2E-141-tab-total-control-filter-3 | FE+BE |
| TC-FA-RP-489 | E2E | TC-FA-RP-E2E-141-tab-total-control-filter-3 | FE+BE |
| TC-FA-RP-490 | E2E | TC-FA-RP-E2E-141-tab-total-control-filter-3 | FE+BE |
| TC-FA-RP-491 | E2E | TC-FA-RP-E2E-141-tab-total-control-filter-3 | FE+BE |
| TC-FA-RP-492 | E2E | TC-FA-RP-E2E-142-tab-total-control-filter-4 | FE+BE |
| TC-FA-RP-493 | E2E | TC-FA-RP-E2E-142-tab-total-control-filter-4 | FE+BE |
| TC-FA-RP-494 | E2E | TC-FA-RP-E2E-142-tab-total-control-filter-4 | FE+BE |
| TC-FA-RP-495 | E2E | TC-FA-RP-E2E-142-tab-total-control-filter-4 | FE+BE |
| TC-FA-RP-496 | E2E | TC-FA-RP-E2E-143-tab-total-control-sort-1 | FE+BE |
| TC-FA-RP-497 | E2E | TC-FA-RP-E2E-143-tab-total-control-sort-1 | FE+BE |
| TC-FA-RP-498 | E2E | TC-FA-RP-E2E-143-tab-total-control-sort-1 | FE+BE |
| TC-FA-RP-499 | E2E | TC-FA-RP-E2E-143-tab-total-control-sort-1 | FE+BE |
| TC-FA-RP-500 | E2E | TC-FA-RP-E2E-144-tab-total-control-sort-2 | FE+BE |
| TC-FA-RP-501 | E2E | TC-FA-RP-E2E-144-tab-total-control-sort-2 | FE+BE |
| TC-FA-RP-502 | E2E | TC-FA-RP-E2E-144-tab-total-control-sort-2 | FE+BE |
| TC-FA-RP-503 | E2E | TC-FA-RP-E2E-145-tab-total-control-setup-column-1 | FE+BE |
| TC-FA-RP-504 | E2E | TC-FA-RP-E2E-145-tab-total-control-setup-column-1 | FE+BE |
| TC-FA-RP-505 | E2E | TC-FA-RP-E2E-145-tab-total-control-setup-column-1 | FE+BE |
| TC-FA-RP-506 | E2E | TC-FA-RP-E2E-146-tab-total-control-setup-column-2 | FE+BE |
| TC-FA-RP-507 | E2E | TC-FA-RP-E2E-146-tab-total-control-setup-column-2 | FE+BE |
| TC-FA-RP-508 | E2E | TC-FA-RP-E2E-147-tab-total-control-setup-column-3 | FE+BE |
| TC-FA-RP-509 | E2E | TC-FA-RP-E2E-147-tab-total-control-setup-column-3 | FE+BE |
| TC-FA-RP-510 | E2E | TC-FA-RP-E2E-148-tab-total-control-setup-column-4 | FE+BE |
| TC-FA-RP-511 | E2E | TC-FA-RP-E2E-148-tab-total-control-setup-column-4 | FE+BE |
| TC-FA-RP-512 | E2E | TC-FA-RP-E2E-148-tab-total-control-setup-column-4 | FE+BE |
| TC-FA-RP-513 | E2E | TC-FA-RP-E2E-149-tab-total-control-setup-column-5 | FE+BE |
| TC-FA-RP-514 | E2E | TC-FA-RP-E2E-149-tab-total-control-setup-column-5 | FE+BE |
| TC-FA-RP-515 | E2E | TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-516 | E2E | TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-517 | E2E | TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-518 | E2E | TC-FA-RP-E2E-150-tab-total-control-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-519 | E2E | TC-FA-RP-E2E-151-tab-total-control-download-1 | FE+BE |
| TC-FA-RP-520 | E2E | TC-FA-RP-E2E-151-tab-total-control-download-1 | FE+BE |
| TC-FA-RP-521 | E2E | TC-FA-RP-E2E-151-tab-total-control-download-1 | FE+BE |
| TC-FA-RP-522 | E2E | TC-FA-RP-E2E-152-tab-total-control-download-2 | FE+BE |
| TC-FA-RP-523 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-524 | E2E | TC-FA-RP-E2E-152-tab-total-control-download-2 | FE+BE |
| TC-FA-RP-525 | E2E | TC-FA-RP-E2E-233-isi-berkas-download-csv-dan-xlsx-1 | FE+BE |
| TC-FA-RP-526 | E2E | TC-FA-RP-E2E-152-tab-total-control-download-2 | FE+BE |
| TC-FA-RP-527 | E2E | TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-FA-RP-528 | E2E | TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-FA-RP-529 | E2E | TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-FA-RP-530 | E2E | TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-FA-RP-531 | E2E | TC-FA-RP-E2E-153-tab-total-control-kombinasi-search-filter-sort-pagination | FE+BE |
| TC-FA-RP-532 | E2E | TC-FA-RP-E2E-156-tab-read-only-search-filter-sort-download-setup-column-dan-1 | FE+BE |
| TC-FA-RP-533 | E2E | TC-FA-RP-E2E-156-tab-read-only-search-filter-sort-download-setup-column-dan-1 | FE+BE |
| TC-FA-RP-534 | E2E | TC-FA-RP-E2E-156-tab-read-only-search-filter-sort-download-setup-column-dan-1 | FE+BE |
| TC-FA-RP-535 | E2E | TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2 | FE+BE |
| TC-FA-RP-536 | E2E | TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2 | FE+BE |
| TC-FA-RP-537 | E2E | TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2 | FE+BE |
| TC-FA-RP-538 | E2E | TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2 | FE+BE |
| TC-FA-RP-539 | E2E | TC-FA-RP-E2E-158-tab-group-manager-search-1 | FE+BE |
| TC-FA-RP-540 | E2E | TC-FA-RP-E2E-158-tab-group-manager-search-1 | FE+BE |
| TC-FA-RP-541 | E2E | TC-FA-RP-E2E-158-tab-group-manager-search-1 | FE+BE |
| TC-FA-RP-542 | E2E | TC-FA-RP-E2E-159-tab-group-manager-search-2 | FE+BE |
| TC-FA-RP-543 | E2E | TC-FA-RP-E2E-159-tab-group-manager-search-2 | FE+BE |
| TC-FA-RP-544 | E2E | TC-FA-RP-E2E-159-tab-group-manager-search-2 | FE+BE |
| TC-FA-RP-545 | E2E | TC-FA-RP-E2E-161-tab-group-manager-filter-1 | FE+BE |
| TC-FA-RP-546 | E2E | TC-FA-RP-E2E-161-tab-group-manager-filter-1 | FE+BE |
| TC-FA-RP-547 | E2E | TC-FA-RP-E2E-161-tab-group-manager-filter-1 | FE+BE |
| TC-FA-RP-548 | E2E | TC-FA-RP-E2E-162-tab-group-manager-filter-2 | FE+BE |
| TC-FA-RP-549 | E2E | TC-FA-RP-E2E-163-tab-group-manager-sort | FE+BE |
| TC-FA-RP-550 | E2E | TC-FA-RP-E2E-163-tab-group-manager-sort | FE+BE |
| TC-FA-RP-551 | E2E | TC-FA-RP-E2E-164-tab-group-manager-setup-column-1 | FE+BE |
| TC-FA-RP-552 | E2E | TC-FA-RP-E2E-164-tab-group-manager-setup-column-1 | FE+BE |
| TC-FA-RP-553 | E2E | TC-FA-RP-E2E-164-tab-group-manager-setup-column-1 | FE+BE |
| TC-FA-RP-554 | E2E | TC-FA-RP-E2E-165-tab-group-manager-setup-column-2 | FE+BE |
| TC-FA-RP-555 | E2E | TC-FA-RP-E2E-165-tab-group-manager-setup-column-2 | FE+BE |
| TC-FA-RP-556 | E2E | TC-FA-RP-E2E-166-tab-group-manager-setup-column-3 | FE+BE |
| TC-FA-RP-557 | E2E | TC-FA-RP-E2E-166-tab-group-manager-setup-column-3 | FE+BE |
| TC-FA-RP-558 | E2E | TC-FA-RP-E2E-167-tab-group-manager-setup-column-4 | FE+BE |
| TC-FA-RP-559 | E2E | TC-FA-RP-E2E-167-tab-group-manager-setup-column-4 | FE+BE |
| TC-FA-RP-560 | E2E | TC-FA-RP-E2E-167-tab-group-manager-setup-column-4 | FE+BE |
| TC-FA-RP-561 | E2E | TC-FA-RP-E2E-167-tab-group-manager-setup-column-4 | FE+BE |
| TC-FA-RP-562 | E2E | TC-FA-RP-E2E-168-tab-group-manager-setup-column-5 | FE+BE |
| TC-FA-RP-563 | E2E | TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-564 | E2E | TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-565 | E2E | TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-566 | E2E | TC-FA-RP-E2E-169-tab-group-manager-pagination-dan-state-halaman | FE+BE |
| TC-FA-RP-567 | E2E | TC-FA-RP-E2E-170-tab-group-manager-download-1 | FE+BE |
| TC-FA-RP-568 | E2E | TC-FA-RP-E2E-170-tab-group-manager-download-1 | FE+BE |
| TC-FA-RP-569 | E2E | TC-FA-RP-E2E-170-tab-group-manager-download-1 | FE+BE |
| TC-FA-RP-570 | E2E | TC-FA-RP-E2E-170-tab-group-manager-download-1 | FE+BE |
| TC-FA-RP-571 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-572 | E2E | TC-FA-RP-E2E-171-tab-group-manager-download-2 | FE+BE |
| TC-FA-RP-573 | E2E | TC-FA-RP-E2E-233-isi-berkas-download-csv-dan-xlsx-1 | FE+BE |
| TC-FA-RP-574 | E2E | TC-FA-RP-E2E-171-tab-group-manager-download-2 | FE+BE |
| TC-FA-RP-575 | E2E | TC-FA-RP-E2E-172-tab-group-manager-sidebar-group-tree-dan-menu-baris | FE+BE |
| TC-FA-RP-576 | E2E | TC-FA-RP-E2E-172-tab-group-manager-sidebar-group-tree-dan-menu-baris | FE+BE |
| TC-FA-RP-577 | E2E | TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1 | FE+BE |
| TC-FA-RP-578 | E2E | TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1 | FE+BE |
| TC-FA-RP-579 | E2E | TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1 | FE+BE |
| TC-FA-RP-580 | E2E | TC-FA-RP-E2E-173-tab-system-search-setup-column-download-dan-state-1 | FE+BE |
| TC-FA-RP-581 | E2E | TC-FA-RP-E2E-174-tab-system-search-setup-column-download-dan-state-2 | FE+BE |
| TC-FA-RP-582 | E2E | TC-FA-RP-E2E-174-tab-system-search-setup-column-download-dan-state-2 | FE+BE |
| TC-FA-RP-583 | E2E | TC-FA-RP-E2E-174-tab-system-search-setup-column-download-dan-state-2 | FE+BE |
| TC-FA-RP-584 | E2E | TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3 | FE+BE |
| TC-FA-RP-585 | E2E | TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3 | FE+BE |
| TC-FA-RP-586 | E2E | TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3 | FE+BE |
| TC-FA-RP-587 | E2E | TC-FA-RP-E2E-175-tab-system-search-setup-column-download-dan-state-3 | FE+BE |
| TC-FA-RP-588 | E2E | TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4 | FE+BE |
| TC-FA-RP-589 | E2E | TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4 | FE+BE |
| TC-FA-RP-590 | E2E | TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4 | FE+BE |
| TC-FA-RP-591 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-592 | E2E | TC-FA-RP-E2E-176-tab-system-search-setup-column-download-dan-state-4 | FE+BE |
| TC-FA-RP-593 | E2E | TC-FA-RP-E2E-177-tabel-role-transaksi-search-filter-dan-sort-1 | FE+BE |
| TC-FA-RP-594 | E2E | TC-FA-RP-E2E-177-tabel-role-transaksi-search-filter-dan-sort-1 | FE+BE |
| TC-FA-RP-595 | E2E | TC-FA-RP-E2E-177-tabel-role-transaksi-search-filter-dan-sort-1 | FE+BE |
| TC-FA-RP-596 | E2E | TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-597 | E2E | TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-598 | E2E | TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-599 | E2E | TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-600 | E2E | TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1 | FE+BE |
| TC-FA-RP-601 | E2E | TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1 | FE+BE |
| TC-FA-RP-602 | E2E | TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1 | FE+BE |
| TC-FA-RP-603 | E2E | TC-FA-RP-E2E-181-tabel-role-transaksi-setup-column-1 | FE+BE |
| TC-FA-RP-604 | E2E | TC-FA-RP-E2E-182-tabel-role-transaksi-setup-column-2 | FE+BE |
| TC-FA-RP-605 | E2E | TC-FA-RP-E2E-182-tabel-role-transaksi-setup-column-2 | FE+BE |
| TC-FA-RP-606 | E2E | TC-FA-RP-E2E-183-tabel-role-transaksi-setup-column-3 | FE+BE |
| TC-FA-RP-607 | E2E | TC-FA-RP-E2E-183-tabel-role-transaksi-setup-column-3 | FE+BE |
| TC-FA-RP-608 | E2E | TC-FA-RP-E2E-183-tabel-role-transaksi-setup-column-3 | FE+BE |
| TC-FA-RP-609 | E2E | TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4 | FE+BE |
| TC-FA-RP-610 | E2E | TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4 | FE+BE |
| TC-FA-RP-611 | E2E | TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4 | FE+BE |
| TC-FA-RP-612 | E2E | TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | FE+BE |
| TC-FA-RP-613 | E2E | TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | FE+BE |
| TC-FA-RP-614 | E2E | TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | FE+BE |
| TC-FA-RP-617 | E2E | TC-FA-RP-E2E-189-detail-role-search-1 | FE+BE |
| TC-FA-RP-618 | E2E | TC-FA-RP-E2E-189-detail-role-search-1 | FE+BE |
| TC-FA-RP-619 | E2E | TC-FA-RP-E2E-190-detail-role-search-2 | FE+BE |
| TC-FA-RP-620 | E2E | TC-FA-RP-E2E-190-detail-role-search-2 | FE+BE |
| TC-FA-RP-621 | E2E | TC-FA-RP-E2E-190-detail-role-search-2 | FE+BE |
| TC-FA-RP-622 | E2E | TC-FA-RP-E2E-190-detail-role-search-2 | FE+BE |
| TC-FA-RP-623 | E2E | TC-FA-RP-E2E-191-detail-role-search-3 | FE+BE |
| TC-FA-RP-624 | E2E | TC-FA-RP-E2E-191-detail-role-search-3 | FE+BE |
| TC-FA-RP-625 | E2E | TC-FA-RP-E2E-192-detail-role-filter-1 | FE+BE |
| TC-FA-RP-626 | E2E | TC-FA-RP-E2E-192-detail-role-filter-1 | FE+BE |
| TC-FA-RP-627 | E2E | TC-FA-RP-E2E-192-detail-role-filter-1 | FE+BE |
| TC-FA-RP-628 | E2E | TC-FA-RP-E2E-192-detail-role-filter-1 | FE+BE |
| TC-FA-RP-629 | E2E | TC-FA-RP-E2E-193-detail-role-filter-2 | FE+BE |
| TC-FA-RP-630 | E2E | TC-FA-RP-E2E-193-detail-role-filter-2 | FE+BE |
| TC-FA-RP-631 | E2E | TC-FA-RP-E2E-193-detail-role-filter-2 | FE+BE |
| TC-FA-RP-632 | E2E | TC-FA-RP-E2E-193-detail-role-filter-2 | FE+BE |
| TC-FA-RP-633 | E2E | TC-FA-RP-E2E-194-detail-role-filter-3 | FE+BE |
| TC-FA-RP-634 | E2E | TC-FA-RP-E2E-194-detail-role-filter-3 | FE+BE |
| TC-FA-RP-635 | E2E | TC-FA-RP-E2E-194-detail-role-filter-3 | FE+BE |
| TC-FA-RP-636 | E2E | TC-FA-RP-E2E-194-detail-role-filter-3 | FE+BE |
| TC-FA-RP-637 | E2E | TC-FA-RP-E2E-195-detail-role-filter-4 | FE+BE |
| TC-FA-RP-638 | E2E | TC-FA-RP-E2E-195-detail-role-filter-4 | FE+BE |
| TC-FA-RP-639 | E2E | TC-FA-RP-E2E-195-detail-role-filter-4 | FE+BE |
| TC-FA-RP-640 | E2E | TC-FA-RP-E2E-195-detail-role-filter-4 | FE+BE |
| TC-FA-RP-641 | E2E | TC-FA-RP-E2E-196-detail-role-sort | FE+BE |
| TC-FA-RP-642 | E2E | TC-FA-RP-E2E-196-detail-role-sort | FE+BE |
| TC-FA-RP-643 | E2E | TC-FA-RP-E2E-196-detail-role-sort | FE+BE |
| TC-FA-RP-644 | E2E | TC-FA-RP-E2E-197-detail-role-setup-column-1 | FE+BE |
| TC-FA-RP-645 | E2E | TC-FA-RP-E2E-197-detail-role-setup-column-1 | FE+BE |
| TC-FA-RP-646 | E2E | TC-FA-RP-E2E-197-detail-role-setup-column-1 | FE+BE |
| TC-FA-RP-647 | E2E | TC-FA-RP-E2E-198-detail-role-setup-column-2 | FE+BE |
| TC-FA-RP-648 | E2E | TC-FA-RP-E2E-198-detail-role-setup-column-2 | FE+BE |
| TC-FA-RP-649 | E2E | TC-FA-RP-E2E-199-detail-role-setup-column-3 | FE+BE |
| TC-FA-RP-650 | E2E | TC-FA-RP-E2E-199-detail-role-setup-column-3 | FE+BE |
| TC-FA-RP-651 | E2E | TC-FA-RP-E2E-200-detail-role-setup-column-4 | FE+BE |
| TC-FA-RP-652 | E2E | TC-FA-RP-E2E-200-detail-role-setup-column-4 | FE+BE |
| TC-FA-RP-653 | E2E | TC-FA-RP-E2E-200-detail-role-setup-column-4 | FE+BE |
| TC-FA-RP-654 | E2E | TC-FA-RP-E2E-201-detail-role-setup-column-5 | FE+BE |
| TC-FA-RP-655 | E2E | TC-FA-RP-E2E-201-detail-role-setup-column-5 | FE+BE |
| TC-FA-RP-656 | E2E | TC-FA-RP-E2E-201-detail-role-setup-column-5 | FE+BE |
| TC-FA-RP-657 | E2E | TC-FA-RP-E2E-088-volume-data-company-volume-seleksi-bulk-selection-limit-dan-2 | FE+BE |
| TC-FA-RP-658 | E2E | TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3 | FE+BE |
| TC-FA-RP-659 | E2E | TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3 | FE+BE |
| TC-FA-RP-660 | E2E | TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3 | FE+BE |
| TC-FA-RP-661 | E2E | TC-FA-RP-E2E-202-detail-role-download-1 | FE+BE |
| TC-FA-RP-662 | E2E | TC-FA-RP-E2E-202-detail-role-download-1 | FE+BE |
| TC-FA-RP-663 | E2E | TC-FA-RP-E2E-202-detail-role-download-1 | FE+BE |
| TC-FA-RP-664 | E2E | TC-FA-RP-E2E-202-detail-role-download-1 | FE+BE |
| TC-FA-RP-665 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-666 | E2E | TC-FA-RP-E2E-203-detail-role-download-2 | FE+BE |
| TC-FA-RP-667 | E2E | TC-FA-RP-E2E-233-isi-berkas-download-csv-dan-xlsx-1 | FE+BE |
| TC-FA-RP-668 | E2E | TC-FA-RP-E2E-203-detail-role-download-2 | FE+BE |
| TC-FA-RP-669 | E2E | TC-FA-RP-E2E-234-isi-berkas-download-csv-dan-xlsx-2 | FE+BE |
| TC-FA-RP-670 | E2E | TC-FA-RP-E2E-203-detail-role-download-2 | FE+BE |
| TC-FA-RP-671 | E2E | TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | FE+BE |
| TC-FA-RP-672 | E2E | TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | FE+BE |
| TC-FA-RP-673 | E2E | TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | FE+BE |
| TC-FA-RP-674 | E2E | TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | FE+BE |
| TC-FA-RP-675 | E2E | TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1 | FE+BE |
| TC-FA-RP-676 | E2E | TC-FA-RP-E2E-205-detail-role-kombinasi-dan-state-halaman-2 | FE+BE |
| TC-FA-RP-677 | E2E | TC-FA-RP-E2E-205-detail-role-kombinasi-dan-state-halaman-2 | FE+BE |
| TC-FA-RP-678 | E2E | TC-FA-RP-E2E-206-table-user-picker-search-filter-dan-sort-1 | FE+BE |
| TC-FA-RP-679 | E2E | TC-FA-RP-E2E-206-table-user-picker-search-filter-dan-sort-1 | FE+BE |
| TC-FA-RP-680 | E2E | TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-681 | E2E | TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-682 | E2E | TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-683 | E2E | TC-FA-RP-E2E-207-table-user-picker-search-filter-dan-sort-2 | FE+BE |
| TC-FA-RP-684 | E2E | TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-685 | E2E | TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-686 | E2E | TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-687 | E2E | TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-688 | E2E | TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-689 | E2E | TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-690 | E2E | TC-FA-RP-E2E-211-table-user-picker-setup-column-1 | FE+BE |
| TC-FA-RP-691 | E2E | TC-FA-RP-E2E-211-table-user-picker-setup-column-1 | FE+BE |
| TC-FA-RP-692 | E2E | TC-FA-RP-E2E-211-table-user-picker-setup-column-1 | FE+BE |
| TC-FA-RP-693 | E2E | TC-FA-RP-E2E-212-table-user-picker-setup-column-2 | FE+BE |
| TC-FA-RP-694 | E2E | TC-FA-RP-E2E-212-table-user-picker-setup-column-2 | FE+BE |
| TC-FA-RP-695 | E2E | TC-FA-RP-E2E-213-table-user-picker-setup-column-3 | FE+BE |
| TC-FA-RP-696 | E2E | TC-FA-RP-E2E-213-table-user-picker-setup-column-3 | FE+BE |
| TC-FA-RP-697 | E2E | TC-FA-RP-E2E-214-table-user-picker-setup-column-4 | FE+BE |
| TC-FA-RP-698 | E2E | TC-FA-RP-E2E-214-table-user-picker-setup-column-4 | FE+BE |
| TC-FA-RP-699 | E2E | TC-FA-RP-E2E-214-table-user-picker-setup-column-4 | FE+BE |
| TC-FA-RP-700 | E2E | TC-FA-RP-E2E-215-table-user-picker-setup-column-5 | FE+BE |
| TC-FA-RP-701 | E2E | TC-FA-RP-E2E-215-table-user-picker-setup-column-5 | FE+BE |
| TC-FA-RP-702 | E2E | TC-FA-RP-E2E-216-table-user-picker-pagination-state-dan-kombinasi-1 | FE+BE |
| TC-FA-RP-703 | E2E | TC-FA-RP-E2E-216-table-user-picker-pagination-state-dan-kombinasi-1 | FE+BE |
| TC-FA-RP-704 | E2E | TC-FA-RP-E2E-216-table-user-picker-pagination-state-dan-kombinasi-1 | FE+BE |
| TC-FA-RP-705 | E2E | TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2 | FE+BE |
| TC-FA-RP-706 | E2E | TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2 | FE+BE |
| TC-FA-RP-707 | E2E | TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2 | FE+BE |
| TC-FA-RP-708 | E2E | TC-FA-RP-E2E-217-table-user-picker-pagination-state-dan-kombinasi-2 | FE+BE |
| TC-FA-RP-709 | E2E | TC-FA-RP-E2E-218-modal-changelog-search-dan-filter-1 | FE+BE |
| TC-FA-RP-710 | E2E | TC-FA-RP-E2E-218-modal-changelog-search-dan-filter-1 | FE+BE |
| TC-FA-RP-711 | E2E | TC-FA-RP-E2E-219-modal-changelog-search-dan-filter-2 | FE+BE |
| TC-FA-RP-712 | E2E | TC-FA-RP-E2E-219-modal-changelog-search-dan-filter-2 | FE+BE |
| TC-FA-RP-713 | E2E | TC-FA-RP-E2E-219-modal-changelog-search-dan-filter-2 | FE+BE |
| TC-FA-RP-714 | E2E | TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | FE+BE |
| TC-FA-RP-715 | E2E | TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | FE+BE |
| TC-FA-RP-716 | E2E | TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | FE+BE |
| TC-FA-RP-717 | E2E | TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | FE+BE |
| TC-FA-RP-718 | E2E | TC-FA-RP-E2E-220-modal-changelog-search-dan-filter-3 | FE+BE |
| TC-FA-RP-719 | E2E | TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4 | FE+BE |
| TC-FA-RP-720 | E2E | TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4 | FE+BE |
| TC-FA-RP-721 | E2E | TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4 | FE+BE |
| TC-FA-RP-722 | E2E | TC-FA-RP-E2E-221-modal-changelog-search-dan-filter-4 | FE+BE |
| TC-FA-RP-723 | E2E | TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5 | FE+BE |
| TC-FA-RP-724 | E2E | TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5 | FE+BE |
| TC-FA-RP-725 | E2E | TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5 | FE+BE |
| TC-FA-RP-726 | E2E | TC-FA-RP-E2E-222-modal-changelog-search-dan-filter-5 | FE+BE |
| TC-FA-RP-727 | E2E | TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6 | FE+BE |
| TC-FA-RP-728 | E2E | TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6 | FE+BE |
| TC-FA-RP-729 | E2E | TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6 | FE+BE |
| TC-FA-RP-730 | E2E | TC-FA-RP-E2E-223-modal-changelog-search-dan-filter-6 | FE+BE |
| TC-FA-RP-731 | E2E | TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1 | FE+BE |
| TC-FA-RP-732 | E2E | TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1 | FE+BE |
| TC-FA-RP-733 | E2E | TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1 | FE+BE |
| TC-FA-RP-734 | E2E | TC-FA-RP-E2E-224-modal-changelog-sort-dan-setup-column-1 | FE+BE |
| TC-FA-RP-735 | E2E | TC-FA-RP-E2E-225-modal-changelog-sort-dan-setup-column-2 | FE+BE |
| TC-FA-RP-736 | E2E | TC-FA-RP-E2E-225-modal-changelog-sort-dan-setup-column-2 | FE+BE |
| TC-FA-RP-737 | E2E | TC-FA-RP-E2E-226-modal-changelog-sort-dan-setup-column-3 | FE+BE |
| TC-FA-RP-738 | E2E | TC-FA-RP-E2E-226-modal-changelog-sort-dan-setup-column-3 | FE+BE |
| TC-FA-RP-739 | E2E | TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4 | FE+BE |
| TC-FA-RP-740 | E2E | TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4 | FE+BE |
| TC-FA-RP-741 | E2E | TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4 | FE+BE |
| TC-FA-RP-742 | E2E | TC-FA-RP-E2E-227-modal-changelog-sort-dan-setup-column-4 | FE+BE |
| TC-FA-RP-743 | E2E | TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1 | FE+BE |
| TC-FA-RP-744 | E2E | TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1 | FE+BE |
| TC-FA-RP-745 | E2E | TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1 | FE+BE |
| TC-FA-RP-746 | E2E | TC-FA-RP-E2E-228-modal-changelog-pagination-download-kombinasi-dan-varian-1 | FE+BE |
| TC-FA-RP-747 | E2E | TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2 | FE+BE |
| TC-FA-RP-748 | E2E | TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2 | FE+BE |
| TC-FA-RP-749 | E2E | TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2 | FE+BE |
| TC-FA-RP-750 | E2E | TC-FA-RP-E2E-229-modal-changelog-pagination-download-kombinasi-dan-varian-2 | FE+BE |
| TC-FA-RP-751 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-752 | E2E | TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | FE+BE |
| TC-FA-RP-753 | E2E | TC-FA-RP-E2E-234-isi-berkas-download-csv-dan-xlsx-2 | FE+BE |
| TC-FA-RP-754 | E2E | TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | FE+BE |
| TC-FA-RP-755 | E2E | TC-FA-RP-E2E-091-volume-data-company-export-download-changelog-di-atas-5-000 | FE+BE |
| TC-FA-RP-756 | E2E | TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | FE+BE |
| TC-FA-RP-757 | E2E | TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | FE+BE |
| TC-FA-RP-758 | E2E | TC-FA-RP-E2E-230-modal-changelog-pagination-download-kombinasi-dan-varian-3 | FE+BE |
| TC-FA-RP-759 | E2E | TC-FA-RP-E2E-231-modal-changelog-pagination-download-kombinasi-dan-varian-4 | FE+BE |
| TC-FA-RP-760 | E2E | TC-FA-RP-E2E-231-modal-changelog-pagination-download-kombinasi-dan-varian-4 | FE+BE |
| TC-FA-RP-761 | E2E | TC-FA-RP-E2E-311-modal-changelog-title-kolom-object-dan-placeholder-per-varian | FE+BE |
| TC-FA-RP-762 | E2E | TC-FA-RP-E2E-232-modal-changelog-pagination-download-kombinasi-dan-varian-5 | FE+BE |
| TC-FA-RP-763 | E2E | TC-FA-RP-E2E-232-modal-changelog-pagination-download-kombinasi-dan-varian-5 | FE+BE |
| TC-FA-RP-764 | E2E | TC-FA-RP-E2E-290-resilience-download-gagal | FE+BE |
| TC-FA-RP-765 | E2E | TC-FA-RP-E2E-235-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-1 | FE+BE |
| TC-FA-RP-766 | E2E | TC-FA-RP-E2E-235-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-1 | FE+BE |
| TC-FA-RP-767 | E2E | TC-FA-RP-E2E-235-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-1 | FE+BE |
| TC-FA-RP-768 | E2E | TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2 | FE+BE |
| TC-FA-RP-769 | E2E | TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2 | FE+BE |
| TC-FA-RP-770 | E2E | TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2 | FE+BE |
| TC-FA-RP-771 | E2E | TC-FA-RP-E2E-236-guided-tooltip-langkah-kunjungan-pertama-replay-skip-back-dan-2 | FE+BE |
| TC-FA-RP-773 | E2E | TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | FE+BE |
| TC-FA-RP-774 | E2E | TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | FE+BE |
| TC-FA-RP-775 | E2E | TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | FE+BE |
| TC-FA-RP-776 | E2E | TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | FE+BE |
| TC-FA-RP-777 | E2E | TC-FA-RP-E2E-237-format-tanggal-dan-waktu-mengikuti-general-settings | FE+BE |
| TC-FA-RP-778 | E2E | TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | FE+BE |
| TC-FA-RP-779 | E2E | TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | FE+BE |
| TC-FA-RP-780 | E2E | TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | FE+BE |
| TC-FA-RP-781 | E2E | TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | FE+BE |
| TC-FA-RP-782 | E2E | TC-FA-RP-E2E-238-tooltip-hover-truncation-dan-tampilan-baris-1 | FE+BE |
| TC-FA-RP-783 | E2E | TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | FE+BE |
| TC-FA-RP-784 | E2E | TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | FE+BE |
| TC-FA-RP-785 | E2E | TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | FE+BE |
| TC-FA-RP-786 | E2E | TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | FE+BE |
| TC-FA-RP-787 | E2E | TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1 | FE+BE |
| TC-FA-RP-788 | E2E | TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1 | FE+BE |
| TC-FA-RP-789 | E2E | TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1 | FE+BE |
| TC-FA-RP-790 | E2E | TC-FA-RP-E2E-240-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-1 | FE+BE |
| TC-FA-RP-791 | E2E | TC-FA-RP-E2E-241-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-2 | FE+BE |
| TC-FA-RP-792 | E2E | TC-FA-RP-E2E-089-volume-data-company-volume-seleksi-bulk-selection-limit-dan-3 | FE+BE |
| TC-FA-RP-793 | E2E | TC-FA-RP-E2E-241-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-2 | FE+BE |
| TC-FA-RP-794 | E2E | TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1 | FE+BE |
| TC-FA-RP-795 | E2E | TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1 | FE+BE |
| TC-FA-RP-796 | E2E | TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1 | FE+BE |
| TC-FA-RP-797 | E2E | TC-FA-RP-E2E-243-changelog-tab-total-control-read-only-dan-group-manager-1 | FE+BE |
| TC-FA-RP-798 | E2E | TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert | FE+BE |
| TC-FA-RP-799 | E2E | TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert | FE+BE |
| TC-FA-RP-800 | E2E | TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert | FE+BE |
| TC-FA-RP-801 | E2E | TC-FA-RP-E2E-314-changelog-tab-read-only-dan-group-manager-assign-remove-dan-auto-revert | FE+BE |
| TC-FA-RP-802 | E2E | TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2 | FE+BE |
| TC-FA-RP-803 | E2E | TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2 | FE+BE |
| TC-FA-RP-804 | E2E | TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2 | FE+BE |
| TC-FA-RP-805 | E2E | TC-FA-RP-E2E-244-changelog-tab-total-control-read-only-dan-group-manager-2 | FE+BE |
| TC-FA-RP-806 | E2E | TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | FE+BE |
| TC-FA-RP-807 | E2E | TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | FE+BE |
| TC-FA-RP-808 | E2E | TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | FE+BE |
| TC-FA-RP-809 | E2E | TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | FE+BE |
| TC-FA-RP-810 | E2E | TC-FA-RP-E2E-245-changelog-detail-role-global-role-1 | FE+BE |
| TC-FA-RP-811 | E2E | TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | FE+BE |
| TC-FA-RP-812 | E2E | TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | FE+BE |
| TC-FA-RP-813 | E2E | TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | FE+BE |
| TC-FA-RP-814 | E2E | TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | FE+BE |
| TC-FA-RP-815 | E2E | TC-FA-RP-E2E-248-changelog-detail-role-group-role | FE+BE |
| TC-FA-RP-816 | E2E | TC-FA-RP-E2E-248-changelog-detail-role-group-role | FE+BE |
| TC-FA-RP-817 | E2E | TC-FA-RP-E2E-248-changelog-detail-role-group-role | FE+BE |
| TC-FA-RP-818 | E2E | TC-FA-RP-E2E-248-changelog-detail-role-group-role | FE+BE |
| TC-FA-RP-819 | E2E | TC-FA-RP-E2E-248-changelog-detail-role-group-role | FE+BE |
| TC-FA-RP-820 | E2E | TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | FE+BE |
| TC-FA-RP-821 | E2E | TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | FE+BE |
| TC-FA-RP-822 | E2E | TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | FE+BE |
| TC-FA-RP-823 | E2E | TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | FE+BE |
| TC-FA-RP-824 | E2E | TC-FA-RP-E2E-249-changelog-tab-system-dan-approval-config-1 | FE+BE |
| TC-FA-RP-825 | E2E | TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | FE+BE |
| TC-FA-RP-826 | E2E | TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | FE+BE |
| TC-FA-RP-827 | E2E | TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | FE+BE |
| TC-FA-RP-828 | E2E | TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | FE+BE |
| TC-FA-RP-829 | E2E | TC-FA-RP-E2E-250-changelog-tab-system-dan-approval-config-2 | FE+BE |
| TC-FA-RP-830 | E2E | TC-FA-RP-E2E-251-changelog-transaction-role | FE+BE |
| TC-FA-RP-831 | E2E | TC-FA-RP-E2E-251-changelog-transaction-role | FE+BE |
| TC-FA-RP-832 | E2E | TC-FA-RP-E2E-251-changelog-transaction-role | FE+BE |
| TC-FA-RP-833 | E2E | TC-FA-RP-E2E-251-changelog-transaction-role | FE+BE |
| TC-FA-RP-834 | E2E | TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | FE+BE |
| TC-FA-RP-835 | E2E | TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | FE+BE |
| TC-FA-RP-836 | E2E | TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | FE+BE |
| TC-FA-RP-837 | E2E | TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | FE+BE |
| TC-FA-RP-838 | E2E | TC-FA-RP-E2E-252-system-log-dan-activity-log-assign-remove-dan-edit-1 | FE+BE |
| TC-FA-RP-839 | E2E | TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | FE+BE |
| TC-FA-RP-840 | E2E | TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | FE+BE |
| TC-FA-RP-841 | E2E | TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | FE+BE |
| TC-FA-RP-842 | E2E | TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | FE+BE |
| TC-FA-RP-843 | E2E | TC-FA-RP-E2E-253-system-log-dan-activity-log-assign-remove-dan-edit-2 | FE+BE |
| TC-FA-RP-844 | E2E | TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | FE+BE |
| TC-FA-RP-845 | E2E | TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | FE+BE |
| TC-FA-RP-846 | E2E | TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | FE+BE |
| TC-FA-RP-847 | E2E | TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | FE+BE |
| TC-FA-RP-848 | E2E | TC-FA-RP-E2E-254-system-log-dan-activity-log-assign-remove-dan-edit-3 | FE+BE |
| TC-FA-RP-849 | E2E | TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | FE+BE |
| TC-FA-RP-850 | E2E | TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | FE+BE |
| TC-FA-RP-851 | E2E | TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | FE+BE |
| TC-FA-RP-852 | E2E | TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | FE+BE |
| TC-FA-RP-853 | E2E | TC-FA-RP-E2E-255-system-log-dan-activity-log-assign-remove-dan-edit-4 | FE+BE |
| TC-FA-RP-854 | E2E | TC-FA-RP-E2E-256-system-log-dan-activity-log-assign-remove-dan-edit-5 | FE+BE |
| TC-FA-RP-855 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-856 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-857 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-858 | E2E | TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1 | FE+BE |
| TC-FA-RP-859 | E2E | TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1 | FE+BE |
| TC-FA-RP-860 | E2E | TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1 | FE+BE |
| TC-FA-RP-861 | E2E | TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4 | FE+BE |
| TC-FA-RP-862 | E2E | TC-FA-RP-E2E-258-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-1 | FE+BE |
| TC-FA-RP-863 | E2E | TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4 | FE+BE |
| TC-FA-RP-864 | E2E | TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4 | FE+BE |
| TC-FA-RP-865 | E2E | TC-FA-RP-E2E-260-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-3 | FE+BE |
| TC-FA-RP-866 | E2E | TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2 | FE+BE |
| TC-FA-RP-867 | E2E | TC-FA-RP-E2E-261-absence-log-aksi-yang-tidak-menulis-entri-log | FE+BE |
| TC-FA-RP-868 | E2E | TC-FA-RP-E2E-261-absence-log-aksi-yang-tidak-menulis-entri-log | FE+BE |
| TC-FA-RP-869 | E2E | TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2 | FE+BE |
| TC-FA-RP-870 | E2E | TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2 | FE+BE |
| TC-FA-RP-871 | E2E | TC-FA-RP-E2E-259-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-2 | FE+BE |
| TC-FA-RP-872 | E2E | TC-FA-RP-E2E-316-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-5 | FE+BE |
| TC-FA-RP-873 | E2E | TC-FA-RP-E2E-261-absence-log-aksi-yang-tidak-menulis-entri-log | FE+BE |
| TC-FA-RP-874 | E2E | TC-FA-RP-E2E-315-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-4 | FE+BE |
| TC-FA-RP-875 | E2E | TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | FE+BE |
| TC-FA-RP-876 | E2E | TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | FE+BE |
| TC-FA-RP-877 | E2E | TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | FE+BE |
| TC-FA-RP-878 | E2E | TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | FE+BE |
| TC-FA-RP-879 | E2E | TC-FA-RP-E2E-262-multi-konteks-notifikasi-in-app-ke-akun-target-1 | FE+BE |
| TC-FA-RP-880 | E2E | TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | FE+BE |
| TC-FA-RP-881 | E2E | TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | FE+BE |
| TC-FA-RP-882 | E2E | TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | FE+BE |
| TC-FA-RP-883 | E2E | TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | FE+BE |
| TC-FA-RP-884 | E2E | TC-FA-RP-E2E-263-multi-konteks-notifikasi-in-app-ke-akun-target-2 | FE+BE |
| TC-FA-RP-885 | E2E | TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3 | FE+BE |
| TC-FA-RP-886 | E2E | TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3 | FE+BE |
| TC-FA-RP-887 | E2E | TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3 | FE+BE |
| TC-FA-RP-888 | E2E | TC-FA-RP-E2E-264-multi-konteks-notifikasi-in-app-ke-akun-target-3 | FE+BE |
| TC-FA-RP-889 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-890 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-891 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-892 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-893 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-894 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-895 | E2E | TC-FA-RP-E2E-265-sinkronisasi-detail-role-dan-tab-role-settings-user-1 | FE+BE |
| TC-FA-RP-897 | E2E | TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2 | FE+BE |
| TC-FA-RP-898 | E2E | TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2 | FE+BE |
| TC-FA-RP-899 | E2E | TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2 | FE+BE |
| TC-FA-RP-900 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-901 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-902 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-904 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-905 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-906 | E2E | TC-FA-RP-E2E-267-efek-status-user-app-access-dan-cascade-lintas-modul-1 | FE+BE |
| TC-FA-RP-907 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-908 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-909 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-910 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-911 | E2E | TC-FA-RP-E2E-266-sinkronisasi-detail-role-dan-tab-role-settings-user-2 | FE+BE |
| TC-FA-RP-912 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-913 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1; TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | FE+BE |
| TC-FA-RP-914 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | FE+BE |
| TC-FA-RP-915 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | FE+BE |
| TC-FA-RP-916 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | FE+BE |
| TC-FA-RP-917 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-918 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-919 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-920 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-921 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-922 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-923 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-924 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-925 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-926 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-927 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-928 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-929 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-930 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-931 | E2E | TC-FA-RP-E2E-272-defense-in-depth-penolakan-server-atas-permintaan-langsung-4 | FE+BE |
| TC-FA-RP-932 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-933 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-934 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-935 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-936 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-937 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-938 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | FE+BE |
| TC-FA-RP-939 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-940 | E2E | TC-FA-RP-E2E-273-defense-in-depth-penolakan-server-atas-permintaan-langsung-5 | FE+BE |
| TC-FA-RP-941 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-942 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-943 | E2E | TC-FA-RP-E2E-090-volume-data-company-volume-seleksi-bulk-selection-limit-dan-4 | FE+BE |
| TC-FA-RP-944 | E2E | TC-FA-RP-E2E-090-volume-data-company-volume-seleksi-bulk-selection-limit-dan-4 | FE+BE |
| TC-FA-RP-945 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-946 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-947 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-948 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | FE+BE |
| TC-FA-RP-949 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-950 | E2E | TC-FA-RP-E2E-274-defense-in-depth-penolakan-server-atas-permintaan-langsung-6 | FE+BE |
| TC-FA-RP-951 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-952 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-953 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-954 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-955 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-956 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-957 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9; TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | FE+BE |
| TC-FA-RP-958 | E2E | TC-FA-RP-E2E-275-defense-in-depth-penolakan-server-atas-permintaan-langsung-7 | FE+BE |
| TC-FA-RP-959 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-960 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-961 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9; TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | FE+BE |
| TC-FA-RP-962 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-963 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | FE+BE |
| TC-FA-RP-964 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | FE+BE |
| TC-FA-RP-965 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-966 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-967 | E2E | TC-FA-RP-E2E-270-defense-in-depth-penolakan-server-atas-permintaan-langsung-2 | FE+BE |
| TC-FA-RP-968 | E2E | TC-FA-RP-E2E-269-defense-in-depth-penolakan-server-atas-permintaan-langsung-1 | FE+BE |
| TC-FA-RP-969 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1 | FE+BE |
| TC-FA-RP-970 | E2E | TC-FA-RP-E2E-271-defense-in-depth-penolakan-server-atas-permintaan-langsung-3 | FE+BE |
| TC-FA-RP-971 | E2E | TC-FA-RP-E2E-090-volume-data-company-volume-seleksi-bulk-selection-limit-dan-4 | FE+BE |
| TC-FA-RP-972 | E2E | TC-FA-RP-E2E-239-tooltip-hover-truncation-dan-tampilan-baris-2 | FE+BE |
| TC-FA-RP-973 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-974 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-975 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-976 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-977 | E2E | TC-FA-RP-E2E-278-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-1; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-978 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-293-absence-log-aksi-ditolak-karena-state-tenant-1 | FE+BE |
| TC-FA-RP-979 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2 | FE+BE |
| TC-FA-RP-980 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2 | FE+BE |
| TC-FA-RP-981 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2 | FE+BE |
| TC-FA-RP-982 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-294-absence-log-aksi-ditolak-karena-state-tenant-2 | FE+BE |
| TC-FA-RP-983 | E2E | TC-FA-RP-E2E-279-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-2; TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | FE+BE |
| TC-FA-RP-984 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-985 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-986 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-987 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-988 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-989 | E2E | TC-FA-RP-E2E-280-state-tenant-client-suspended-dan-expired-menolak-aksi-tulis-3 | FE+BE |
| TC-FA-RP-990 | E2E | TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1 | FE+BE |
| TC-FA-RP-991 | E2E | TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1 | FE+BE |
| TC-FA-RP-992 | E2E | TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1 | FE+BE |
| TC-FA-RP-993 | E2E | TC-FA-RP-E2E-281-state-tenant-plan-tier-dan-approval-workflow-1 | FE+BE |
| TC-FA-RP-994 | E2E | TC-FA-RP-E2E-317-state-tenant-plan-tier-dan-approval-workflow-2 | FE+BE |
| TC-FA-RP-995 | E2E | TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | FE+BE |
| TC-FA-RP-996 | E2E | TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | FE+BE |
| TC-FA-RP-997 | E2E | TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | FE+BE |
| TC-FA-RP-998 | E2E | TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | FE+BE |
| TC-FA-RP-999 | E2E | TC-FA-RP-E2E-282-multi-konteks-konflik-dua-admin-pada-objek-yang-sama | FE+BE |
| TC-FA-RP-1000 | E2E | TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat | FE+BE |
| TC-FA-RP-1001 | E2E | TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat | FE+BE |
| TC-FA-RP-1002 | E2E | TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat | FE+BE |
| TC-FA-RP-1003 | E2E | TC-FA-RP-E2E-283-klik-ganda-dan-ketuk-ganda-cepat | FE+BE |
| TC-FA-RP-1004 | E2E | TC-FA-RP-E2E-171-tab-group-manager-download-2 | FE+BE |
| TC-FA-RP-1005 | E2E | TC-FA-RP-E2E-203-detail-role-download-2 | FE+BE |
| TC-FA-RP-1006 | E2E | TC-FA-RP-E2E-201-detail-role-setup-column-5 | FE+BE |
| TC-FA-RP-1007 | E2E | TC-FA-RP-E2E-242-aksesibilitas-keyboard-fokus-dialog-dan-slot-toast | FE+BE |
| TC-FA-RP-1008 | E2E | TC-FA-RP-E2E-242-aksesibilitas-keyboard-fokus-dialog-dan-slot-toast | FE+BE |
| TC-FA-RP-1009 | E2E | TC-FA-RP-E2E-313-aksesibilitas-dialog-konfirmasi-fokus-terkunci-dan-esc-setara-cancel | FE+BE |
| TC-FA-RP-1010 | E2E | TC-FA-RP-E2E-086-bulk-remove-dialog-hasil-dan-cancel-2 | FE+BE |
| TC-FA-RP-1011 | E2E | TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | FE+BE |
| TC-FA-RP-1012 | E2E | TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | FE+BE |
| TC-FA-RP-1013 | E2E | TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | FE+BE |
| TC-FA-RP-1014 | E2E | TC-FA-RP-E2E-154-tab-total-control-isi-sel-dan-badge-1 | FE+BE |
| TC-FA-RP-1015 | E2E | TC-FA-RP-E2E-242-aksesibilitas-keyboard-fokus-dialog-dan-slot-toast | FE+BE |
| TC-FA-RP-1016 | E2E | TC-FA-RP-E2E-083-remove-baris-peran-satu-per-satu-2 | FE+BE |
| TC-FA-RP-1017 | E2E | TC-FA-RP-E2E-070-remove-group-manager-1 | FE+BE |
| TC-FA-RP-1018 | E2E | TC-FA-RP-E2E-037-role-matrix-sidebar-group-tree-dan-data-tabel-sesuai-cakupan-2 | FE+BE |
| TC-FA-RP-1019 | E2E | TC-FA-RP-E2E-107-approval-scope-sub-tab-transfer-2 | FE+BE |
| TC-FA-RP-1020 | E2E | TC-FA-RP-E2E-107-approval-scope-sub-tab-transfer-2 | FE+BE |
| TC-FA-RP-1021 | E2E | TC-FA-RP-E2E-107-approval-scope-sub-tab-transfer-2 | FE+BE |
| TC-FA-RP-1022 | E2E | TC-FA-RP-E2E-154-tab-total-control-isi-sel-dan-badge-1 | FE+BE |
| TC-FA-RP-1023 | E2E | TC-FA-RP-E2E-154-tab-total-control-isi-sel-dan-badge-1 | FE+BE |
| TC-FA-RP-1024 | E2E | TC-FA-RP-E2E-234-isi-berkas-download-csv-dan-xlsx-2 | FE+BE |
| TC-FA-RP-1025 | E2E | TC-FA-RP-E2E-205-detail-role-kombinasi-dan-state-halaman-2 | FE+BE |
| TC-FA-RP-1026 | E2E | TC-FA-RP-E2E-053-aktor-ganda-group-manager-dan-manage-user-dan-role-pada-scope | FE+BE |
| TC-FA-RP-1027 | E2E | TC-FA-RP-E2E-186-tabel-role-transaksi-tampilan-section-header-keterangan-1 | FE+BE |
| TC-FA-RP-1028 | E2E | TC-FA-RP-E2E-093-mobile-chip-group-dan-tooltip-elemen-disabled | FE+BE |
| TC-FA-RP-1029 | E2E | TC-FA-RP-E2E-241-state-halaman-tab-node-sidebar-group-tree-dan-klik-ulang-menu-2 | FE+BE |
| TC-FA-RP-1030 | E2E | TC-FA-RP-E2E-312-modal-changelog-transaction-role-terpisah-per-jenis-transaksi | FE+BE |
| TC-FA-RP-1031 | E2E | TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2 | FE+BE |
| TC-FA-RP-1032 | E2E | TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2 | FE+BE |
| TC-FA-RP-1033 | E2E | TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2 | FE+BE |
| TC-FA-RP-1034 | E2E | TC-FA-RP-E2E-109-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-2 | FE+BE |
| TC-FA-RP-1035 | E2E | TC-FA-RP-E2E-260-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-3 | FE+BE |
| TC-FA-RP-1036 | E2E | TC-FA-RP-E2E-071-remove-group-manager-2 | FE+BE |
| TC-FA-RP-1037 | E2E | TC-FA-RP-E2E-068-assign-group-manager-3 | FE+BE |
| TC-FA-RP-1038 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-1039 | E2E | TC-FA-RP-E2E-120-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-2 | FE+BE |
| TC-FA-RP-1040 | E2E | TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3 | FE+BE |
| TC-FA-RP-1041 | E2E | TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3; TC-FA-RP-E2E-291-absence-log-aksi-no-op-atau-ditolak-ui | FE+BE |
| TC-FA-RP-1042 | E2E | TC-FA-RP-E2E-118-auto-revert-group-manager-dan-pola-subset-baris-eksplisit-2 | FE+BE |
| TC-FA-RP-1043 | E2E | TC-FA-RP-E2E-077-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-1 | FE+BE |
| TC-FA-RP-1044 | E2E | TC-FA-RP-E2E-077-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-1 | FE+BE |
| TC-FA-RP-1045 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-1046 | E2E | TC-FA-RP-E2E-077-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-1 | FE+BE |
| TC-FA-RP-1047 | E2E | TC-FA-RP-E2E-078-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-2 | FE+BE |
| TC-FA-RP-1048 | E2E | TC-FA-RP-E2E-078-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-2 | FE+BE |
| TC-FA-RP-1049 | E2E | TC-FA-RP-E2E-078-eksklusivitas-manage-user-dan-role-dan-manage-global-user-dan-2 | FE+BE |
| TC-FA-RP-1050 | E2E | TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2 | FE+BE |
| TC-FA-RP-1051 | E2E | TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2 | FE+BE |
| TC-FA-RP-1052 | E2E | TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2 | FE+BE |
| TC-FA-RP-1053 | E2E | TC-FA-RP-E2E-187-tabel-role-transaksi-tampilan-section-header-keterangan-2 | FE+BE |
| TC-FA-RP-1054 | E2E | TC-FA-RP-E2E-188-tabel-role-transaksi-tampilan-section-header-keterangan-3 | FE+BE |
| TC-FA-RP-1055 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-1056 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-1057 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-1058 | E2E | TC-FA-RP-E2E-257-system-log-dan-activity-log-konfigurasi-approval-dan-modified | FE+BE |
| TC-FA-RP-1059 | E2E | TC-FA-RP-E2E-144-tab-total-control-sort-2 | FE+BE |
| TC-FA-RP-1060 | E2E | TC-FA-RP-E2E-138-tab-total-control-search-4 | FE+BE |
| TC-FA-RP-1061 | E2E | TC-FA-RP-E2E-138-tab-total-control-search-4 | FE+BE |
| TC-FA-RP-1062 | E2E | TC-FA-RP-E2E-163-tab-group-manager-sort | FE+BE |
| TC-FA-RP-1063 | E2E | TC-FA-RP-E2E-163-tab-group-manager-sort | FE+BE |
| TC-FA-RP-1064 | E2E | TC-FA-RP-E2E-159-tab-group-manager-search-2 | FE+BE |
| TC-FA-RP-1065 | E2E | TC-FA-RP-E2E-160-tab-group-manager-search-3 | FE+BE |
| TC-FA-RP-1066 | E2E | TC-FA-RP-E2E-162-tab-group-manager-filter-2 | FE+BE |
| TC-FA-RP-1067 | E2E | TC-FA-RP-E2E-162-tab-group-manager-filter-2 | FE+BE |
| TC-FA-RP-1068 | E2E | TC-FA-RP-E2E-168-tab-group-manager-setup-column-5 | FE+BE |
| TC-FA-RP-1069 | E2E | TC-FA-RP-E2E-168-tab-group-manager-setup-column-5 | FE+BE |
| TC-FA-RP-1070 | E2E | TC-FA-RP-E2E-168-tab-group-manager-setup-column-5 | FE+BE |
| TC-FA-RP-1071 | E2E | TC-FA-RP-E2E-179-tabel-role-transaksi-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-1072 | E2E | TC-FA-RP-E2E-179-tabel-role-transaksi-search-filter-dan-sort-3 | FE+BE |
| TC-FA-RP-1073 | E2E | TC-FA-RP-E2E-180-tabel-role-transaksi-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-1074 | E2E | TC-FA-RP-E2E-184-tabel-role-transaksi-setup-column-4 | FE+BE |
| TC-FA-RP-1075 | E2E | TC-FA-RP-E2E-185-tabel-role-transaksi-setup-column-5 | FE+BE |
| TC-FA-RP-1076 | E2E | TC-FA-RP-E2E-185-tabel-role-transaksi-setup-column-5 | FE+BE |
| TC-FA-RP-1077 | E2E | TC-FA-RP-E2E-191-detail-role-search-3 | FE+BE |
| TC-FA-RP-1078 | E2E | TC-FA-RP-E2E-195-detail-role-filter-4 | FE+BE |
| TC-FA-RP-1079 | E2E | TC-FA-RP-E2E-196-detail-role-sort | FE+BE |
| TC-FA-RP-1080 | E2E | TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-1081 | E2E | TC-FA-RP-E2E-209-table-user-picker-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-1082 | E2E | TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5 | FE+BE |
| TC-FA-RP-1083 | E2E | TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5 | FE+BE |
| TC-FA-RP-1084 | E2E | TC-FA-RP-E2E-232-modal-changelog-pagination-download-kombinasi-dan-varian-5 | FE+BE |
| TC-FA-RP-1085 | E2E | TC-FA-RP-E2E-058-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-3 | FE+BE |
| TC-FA-RP-1086 | E2E | TC-FA-RP-E2E-062-remove-total-control-2 | FE+BE |
| TC-FA-RP-1087 | E2E | TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | FE+BE |
| TC-FA-RP-1088 | E2E | TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | FE+BE |
| TC-FA-RP-1089 | E2E | TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4 | FE+BE |
| TC-FA-RP-1090 | E2E | TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4 | FE+BE |
| TC-FA-RP-1091 | E2E | TC-FA-RP-E2E-128-popup-assign-per-jenis-alert-tanpa-seleksi-stale-dan-tidak-4 | FE+BE |
| TC-FA-RP-1092 | E2E | TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5 | FE+BE |
| TC-FA-RP-1093 | E2E | TC-FA-RP-E2E-160-tab-group-manager-search-3 | FE+BE |
| TC-FA-RP-1094 | E2E | TC-FA-RP-E2E-103-require-approval-transaction-role-prasyarat-aktivasi-2 | FE+BE |
| TC-FA-RP-1095 | E2E | TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | FE+BE |
| TC-FA-RP-1096 | E2E | TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | FE+BE |
| TC-FA-RP-1097 | E2E | TC-FA-RP-E2E-121-home-group-constraint-dialog-d-10-dan-pencabutan-assignment-3 | FE+BE |
| TC-FA-RP-1098 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8; TC-FA-RP-E2E-292-absence-log-permintaan-langsung-yang-ditolak | FE+BE |
| TC-FA-RP-1099 | E2E | TC-FA-RP-E2E-093-mobile-chip-group-dan-tooltip-elemen-disabled | FE+BE |
| TC-FA-RP-1100 | E2E | TC-FA-RP-E2E-155-tab-total-control-isi-sel-dan-badge-2 | FE+BE |
| TC-FA-RP-1101 | E2E | TC-FA-RP-E2E-155-tab-total-control-isi-sel-dan-badge-2 | FE+BE |
| TC-FA-RP-1102 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-1103 | E2E | TC-FA-RP-E2E-268-efek-status-user-app-access-dan-cascade-lintas-modul-2 | FE+BE |
| TC-FA-RP-1104 | E2E | TC-FA-RP-E2E-138-tab-total-control-search-4 | FE+BE |
| TC-FA-RP-1105 | E2E | TC-FA-RP-E2E-160-tab-group-manager-search-3 | FE+BE |
| TC-FA-RP-1106 | E2E | TC-FA-RP-E2E-180-tabel-role-transaksi-search-filter-dan-sort-4 | FE+BE |
| TC-FA-RP-1107 | E2E | TC-FA-RP-E2E-191-detail-role-search-3 | FE+BE |
| TC-FA-RP-1108 | E2E | TC-FA-RP-E2E-210-table-user-picker-search-filter-dan-sort-5 | FE+BE |
| TC-FA-RP-1109 | E2E | TC-FA-RP-E2E-188-tabel-role-transaksi-tampilan-section-header-keterangan-3 | FE+BE |
| TC-FA-RP-1110 | E2E | TC-FA-RP-E2E-035-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-2 | FE+BE |
| TC-FA-RP-1111 | E2E | TC-FA-RP-E2E-054-changelog-dan-download-entri-remove-group-deleted-per-cakupan-1 | FE+BE |
| TC-FA-RP-1112 | E2E | TC-FA-RP-E2E-055-changelog-dan-download-entri-remove-group-deleted-per-cakupan-2 | FE+BE |
| TC-FA-RP-1113 | E2E | TC-FA-RP-E2E-298-role-matrix-changelog-tab-total-control-dan-read-only-bagi-group-manager | FE+BE |
| TC-FA-RP-1114 | E2E | TC-FA-RP-E2E-035-role-matrix-ikon-download-dan-changelog-serta-cakupan-group-2 | FE+BE |
| TC-FA-RP-1115 | E2E | TC-FA-RP-E2E-054-changelog-dan-download-entri-remove-group-deleted-per-cakupan-1 | FE+BE |
| TC-FA-RP-1116 | E2E | TC-FA-RP-E2E-055-changelog-dan-download-entri-remove-group-deleted-per-cakupan-2 | FE+BE |
| TC-FA-RP-1117 | E2E | TC-FA-RP-E2E-099-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-2 | FE+BE |
| TC-FA-RP-1118 | E2E | TC-FA-RP-E2E-299-changelog-dan-download-entri-remove-group-deleted-per-cakupan-3 | FE+BE |
| TC-FA-RP-1119 | E2E | TC-FA-RP-E2E-299-changelog-dan-download-entri-remove-group-deleted-per-cakupan-3 | FE+BE |
| TC-FA-RP-1120 | E2E | TC-FA-RP-E2E-055-changelog-dan-download-entri-remove-group-deleted-per-cakupan-2 | FE+BE |
| TC-FA-RP-1121 | E2E | TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3 | FE+BE |
| TC-FA-RP-1122 | E2E | TC-FA-RP-E2E-096-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-3 | FE+BE |
| TC-FA-RP-1123 | E2E | TC-FA-RP-E2E-097-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-4 | FE+BE |
| TC-FA-RP-1124 | E2E | TC-FA-RP-E2E-097-assign-role-transaksi-pemilihan-role-dan-kandidat-picker-4 | FE+BE |
| TC-FA-RP-1125 | E2E | TC-FA-RP-E2E-276-defense-in-depth-penolakan-server-atas-permintaan-langsung-8 | FE+BE |
| TC-FA-RP-1126 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | FE+BE |
| TC-FA-RP-1127 | E2E | TC-FA-RP-E2E-062-remove-total-control-2 | FE+BE |
| TC-FA-RP-1128 | E2E | TC-FA-RP-E2E-065-remove-read-only-2 | FE+BE |
| TC-FA-RP-1129 | E2E | TC-FA-RP-E2E-062-remove-total-control-2 | FE+BE |
| TC-FA-RP-1130 | E2E | TC-FA-RP-E2E-246-changelog-detail-role-global-role-2 | FE+BE |
| TC-FA-RP-1131 | E2E | TC-FA-RP-E2E-063-remove-total-control-3 | FE+BE |
| TC-FA-RP-1132 | E2E | TC-FA-RP-E2E-065-remove-read-only-2 | FE+BE |
| TC-FA-RP-1133 | E2E | TC-FA-RP-E2E-063-remove-total-control-3 | FE+BE |
| TC-FA-RP-1134 | E2E | TC-FA-RP-E2E-247-changelog-detail-role-global-role-3 | FE+BE |
| TC-FA-RP-1135 | E2E | TC-FA-RP-E2E-247-changelog-detail-role-global-role-3 | FE+BE |
| TC-FA-RP-1136 | E2E | TC-FA-RP-E2E-247-changelog-detail-role-global-role-3 | FE+BE |
| TC-FA-RP-1137 | E2E | TC-FA-RP-E2E-114-auto-revert-total-control-3 | FE+BE |
| TC-FA-RP-1138 | E2E | TC-FA-RP-E2E-133-konfirmasi-remove-last-approver-d-09-pada-role-transaksi-dan-3 | FE+BE |
| TC-FA-RP-1139 | E2E | TC-FA-RP-E2E-058-assign-total-control-satu-atau-banyak-user-timpa-parsial-dan-3 | FE+BE |
| TC-FA-RP-1140 | E2E | TC-FA-RP-E2E-316-pencatatan-lintas-surface-cascade-atomik-dan-konsistensi-entri-5 | FE+BE |
| TC-FA-RP-1141 | E2E | TC-FA-RP-E2E-075-assign-user-ke-group-role-di-detail-role-3 | FE+BE |
| TC-FA-RP-1142 | E2E | TC-FA-RP-E2E-076-assign-user-ke-group-role-di-detail-role-4 | FE+BE |
| TC-FA-RP-1143 | E2E | TC-FA-RP-E2E-277-defense-in-depth-penolakan-server-atas-permintaan-langsung-9 | FE+BE |
| TC-FA-RP-1144 | E2E | TC-FA-RP-E2E-306-identitas-user-dihapus-permanen-cascade-tanpa-entri-log-group-manager | FE+BE |
| TC-FA-RP-1145 | E2E | TC-FA-RP-E2E-318-assign-total-control-dan-read-only-menulis-baris-pola-transaction-role | FE+BE |
| TC-FA-RP-1146 | E2E | TC-FA-RP-E2E-318-assign-total-control-dan-read-only-menulis-baris-pola-transaction-role | FE+BE |
| TC-FA-RP-1147 | E2E | TC-FA-RP-E2E-337-assign-total-control-ke-user-standard-pemegang-peran-tangga-lama | FE+BE |
| TC-FA-RP-1148 | E2E | TC-FA-RP-E2E-320-remove-total-control-dan-read-only-menghapus-baris-pola-transaction-role | FE+BE |
| TC-FA-RP-1149 | E2E | TC-FA-RP-E2E-320-remove-total-control-dan-read-only-menghapus-baris-pola-transaction-role | FE+BE |
| TC-FA-RP-1150 | E2E | TC-FA-RP-E2E-321-role-matrix-gating-remove-baris-pola-transaction-role-per-peran | FE+BE |
| TC-FA-RP-1151 | E2E | TC-FA-RP-E2E-324-auto-revert-role-transaksi-remove-baris-pola-target-total-control-dan-read-only | FE+BE |
| TC-FA-RP-1152 | E2E | TC-FA-RP-E2E-325-auto-revert-role-transaksi-turun-dan-naik-tangga-dari-popup-assign | FE+BE |
| TC-FA-RP-1153 | E2E | TC-FA-RP-E2E-325-auto-revert-role-transaksi-turun-dan-naik-tangga-dari-popup-assign | FE+BE |
| TC-FA-RP-1154 | E2E | TC-FA-RP-E2E-326-auto-revert-role-transaksi-submit-campuran-dua-dialog-berurutan | FE+BE |
| TC-FA-RP-1155 | E2E | TC-FA-RP-E2E-327-pengecualian-dialog-role-transaksi-default-user-dan-d-09-pada-remove-approver-pola | FE+BE |
| TC-FA-RP-1156 | E2E | TC-FA-RP-E2E-328-efek-deactivate-dan-app-access-pada-baris-pola-transaction-role | FE+BE |
| TC-FA-RP-1157 | E2E | TC-FA-RP-E2E-330-group-baru-subgroup-level-one-dan-import-menulis-baris-pola | FE+BE |
| TC-FA-RP-1158 | E2E | TC-FA-RP-E2E-330-group-baru-subgroup-level-one-dan-import-menulis-baris-pola | FE+BE |
| TC-FA-RP-1159 | E2E | TC-FA-RP-E2E-332-delete-group-menghapus-baris-pola-transaction-role-dan-group-role | FE+BE |
| TC-FA-RP-1160 | E2E | TC-FA-RP-E2E-327-pengecualian-dialog-role-transaksi-default-user-dan-d-09-pada-remove-approver-pola | FE+BE |
| TC-FA-RP-1161 | E2E | TC-FA-RP-E2E-329-sub-tab-addon-tanpa-dan-dengan-lisensi-baris-pola-tidak-dihitung | FE+BE |
| TC-FA-RP-1162 | E2E | TC-FA-RP-E2E-329-sub-tab-addon-tanpa-dan-dengan-lisensi-baris-pola-tidak-dihitung | FE+BE |
| TC-FA-RP-1163 | E2E | TC-FA-RP-E2E-335-changelog-transaction-role-per-baris-pola-assign-remove-dan-auto-revert | FE+BE |
| TC-FA-RP-1164 | E2E | TC-FA-RP-E2E-336-multi-konteks-notifikasi-auto-revert-varian-role-transaksi | FE+BE |
| TC-FA-RP-1165 | E2E | TC-FA-RP-E2E-341-auto-revert-role-transaksi-remove-baris-pola-target-read-only | FE+BE |
| TC-FA-RP-1166 | E2E | TC-FA-RP-E2E-343-app-access-dicabut-baris-pola-dormant-dan-group-baru-tetap-dibuatkan-baris | FE+BE |
| TC-FA-RP-1167 | E2E | TC-FA-RP-E2E-334-header-section-role-transaksi-menghitung-baris-pola-saat-baris-melebihi-10 | FE+BE |
| TC-FA-RP-1168 | E2E | TC-FA-RP-E2E-342-submit-campuran-cancel-dialog-kedua-membatalkan-seluruh-submit | FE+BE |
| TC-FA-RP-1169 | E2E | TC-FA-RP-E2E-319-assign-total-control-dan-read-only-menulis-baris-pola-group-role | FE+BE |
| TC-FA-RP-1170 | E2E | TC-FA-RP-E2E-338-assign-read-only-menulis-baris-pola-group-role-dan-changelog-user | FE+BE |
| TC-FA-RP-1171 | E2E | TC-FA-RP-E2E-322-auto-revert-group-role-pola-lewat-edit-crud-dan-remove-baris | FE+BE |
| TC-FA-RP-1172 | E2E | TC-FA-RP-E2E-322-auto-revert-group-role-pola-lewat-edit-crud-dan-remove-baris | FE+BE |
| TC-FA-RP-1173 | E2E | TC-FA-RP-E2E-323-bulk-remove-baris-group-role-target-total-control-dan-read-only | FE+BE |
| TC-FA-RP-1174 | E2E | TC-FA-RP-E2E-345-group-baru-menulis-baris-pola-group-role-detail-role-changelog-dan-notifikasi | FE+BE |
| TC-FA-RP-1175 | E2E | TC-FA-RP-E2E-331-home-group-constraint-diabaikan-untuk-total-control-dan-read-only | FE+BE |
| TC-FA-RP-1176 | E2E | TC-FA-RP-E2E-332-delete-group-menghapus-baris-pola-transaction-role-dan-group-role | FE+BE |
| TC-FA-RP-1177 | E2E | TC-FA-RP-E2E-333-detail-role-group-role-checkbox-pagination-dan-select-all-baris-pola | FE+BE |
| TC-FA-RP-1178 | E2E | TC-FA-RP-E2E-333-detail-role-group-role-checkbox-pagination-dan-select-all-baris-pola | FE+BE |
| TC-FA-RP-1179 | E2E | TC-FA-RP-E2E-346-assign-gm-menulis-baris-pola-group-role-tanpa-global-role | FE+BE |
| TC-FA-RP-1180 | E2E | TC-FA-RP-E2E-361-assign-gm-menulis-baris-pola-role-transaksi-asset-admin-dan-approver | FE+BE |
| TC-FA-RP-1181 | E2E | TC-FA-RP-E2E-349-log-assign-gm-per-baris-pola-changelog-bukan-system-activity-log | FE+BE |
| TC-FA-RP-1182 | E2E | TC-FA-RP-E2E-347-assign-gm-menggantikan-peran-tangga-lain-dengan-asset-admin | FE+BE |
| TC-FA-RP-1183 | E2E | TC-FA-RP-E2E-352-subgroup-baru-di-bawah-node-gm-menulis-baris-pola-dan-group-level-one-tidak | FE+BE |
| TC-FA-RP-1184 | E2E | TC-FA-RP-E2E-370-group-hasil-import-di-bawah-node-gm-menulis-baris-pola | FE+BE |
| TC-FA-RP-1185 | E2E | TC-FA-RP-E2E-362-assign-gm-bersarang-satu-set-baris-pola-tanpa-duplikasi | FE+BE |
| TC-FA-RP-1186 | E2E | TC-FA-RP-E2E-350-remove-gm-bersarang-pelepasan-penugasan-ancestor-baris-pola-tercakup-dipertahankan | FE+BE |
| TC-FA-RP-1186 | E2E | TC-FA-RP-E2E-363-remove-gm-bersarang-pelepasan-penugasan-terakhir-role-transaksi-dan-notifikasi | FE+BE |
| TC-FA-RP-1187 | E2E | TC-FA-RP-E2E-364-remove-gm-menghapus-baris-pola-role-transaksi-di-subtree-tanpa-menyentuh-luar-subtree | FE+BE |
| TC-FA-RP-1188 | E2E | TC-FA-RP-E2E-355-auto-revert-gm-bersarang-baris-pola-bersama-dan-notifikasi | FE+BE |
| TC-FA-RP-1189 | E2E | TC-FA-RP-E2E-354-auto-revert-gm-lewat-edit-crud-dan-remove-baris-pola-descendant | FE+BE |
| TC-FA-RP-1190 | E2E | TC-FA-RP-E2E-357-bulk-remove-baris-pola-gm-dan-baris-non-pola-gm-tidak-terkunci | FE+BE |
| TC-FA-RP-1191 | E2E | TC-FA-RP-E2E-356-assign-staff-ke-gm-turun-tangga-dialog-d05-varian-role-transaksi | FE+BE |
| TC-FA-RP-1192 | E2E | TC-FA-RP-E2E-365-auto-revert-gm-lewat-remove-baris-approver-pola-descendant | FE+BE |
| TC-FA-RP-1193 | E2E | TC-FA-RP-E2E-366-submit-campuran-tiga-dialog-d13-d04-d05-assign-role-transaksi | FE+BE |
| TC-FA-RP-1194 | E2E | TC-FA-RP-E2E-357-bulk-remove-baris-pola-gm-dan-baris-non-pola-gm-tidak-terkunci | FE+BE |
| TC-FA-RP-1195 | E2E | TC-FA-RP-E2E-358-role-matrix-kontrol-baris-pola-gm-terkunci-bagi-group-manager | FE+BE |
| TC-FA-RP-1195 | E2E | TC-FA-RP-E2E-367-role-matrix-kontrol-baris-pola-gm-terkunci-bagi-manage-user-dan-role-group-update | FE+BE |
| TC-FA-RP-1196 | E2E | TC-FA-RP-E2E-368-role-matrix-picker-role-transaksi-kandidat-gm-disaring-bagi-group-manager-dan-total-control | FE+BE |
| TC-FA-RP-1197 | E2E | TC-FA-RP-E2E-360-defense-in-depth-penolakan-server-permintaan-langsung-target-gm | FE+BE |
| TC-FA-RP-1198 | E2E | TC-FA-RP-E2E-348-assign-total-control-di-atas-gm-hapus-pola-gm-dulu | FE+BE |
| TC-FA-RP-1199 | E2E | TC-FA-RP-E2E-351-home-group-constraint-pada-gm-mencabut-penugasan-dan-baris-pola-per-baris | FE+BE |
| TC-FA-RP-1200 | E2E | TC-FA-RP-E2E-369-home-group-constraint-yang-mencakup-node-gm-tidak-mencabut-apa-pun | FE+BE |
| TC-FA-RP-1201 | E2E | TC-FA-RP-E2E-353-delete-group-di-bawah-penugasan-gm-hapus-baris-pola-per-baris | FE+BE |
| TC-FA-RP-1202 | E2E | TC-FA-RP-E2E-359-baris-pola-gm-tidak-dihitung-approver-registrasi-dan-pemegang-update | FE+BE |
| TC-FA-RP-1203 | E2E | TC-FA-RP-E2E-371-aktivasi-require-approval-menghitung-baris-approver-dan-update-gm-yang-dipertahankan-setelah-auto-revert | FE+BE |
| TC-FA-RP-1204 | E2E | TC-FA-RP-E2E-372-baris-gm-yang-dipertahankan-menjadi-penugasan-individual-biasa-edit-tanpa-d05-dan-remove-d03 | FE+BE |
| TC-FA-RP-1205 | E2E | TC-FA-RP-E2E-374-preview-scope-popup-assign-role-transaksi-node-induk-pada-keempat-role | FE+BE |
| TC-FA-RP-1206 | E2E | TC-FA-RP-E2E-375-preview-scope-mengikuti-node-dan-sidebar-tanpa-node-disabled | FE+BE |
| TC-FA-RP-1207 | E2E | TC-FA-RP-E2E-375-preview-scope-mengikuti-node-dan-sidebar-tanpa-node-disabled | FE+BE |
| TC-FA-RP-1208 | E2E | TC-FA-RP-E2E-376-assign-role-sama-pada-node-turunan-atau-induk-saat-overlap-diizinkan | FE+BE |
| TC-FA-RP-1209 | E2E | TC-FA-RP-E2E-376-assign-role-sama-pada-node-turunan-atau-induk-saat-overlap-diizinkan | FE+BE |
| TC-FA-RP-1210 | E2E | TC-FA-RP-E2E-377-assign-tangga-rendah-atau-tinggi-di-node-turunan-tidak-menyentuh-ancestor; TC-FA-RP-E2E-383-absence-log-assign-overlap-tidak-menghapus-ancestor-dan-satu-entri-per-penugasan | FE+BE |
| TC-FA-RP-1211 | E2E | TC-FA-RP-E2E-377-assign-tangga-rendah-atau-tinggi-di-node-turunan-tidak-menyentuh-ancestor; TC-FA-RP-E2E-383-absence-log-assign-overlap-tidak-menghapus-ancestor-dan-satu-entri-per-penugasan | FE+BE |
| TC-FA-RP-1212 | E2E | TC-FA-RP-E2E-378-d13-hanya-pada-node-sama-dan-approver-ancestor-descendant-berdampingan | FE+BE |
| TC-FA-RP-1213 | E2E | TC-FA-RP-E2E-378-d13-hanya-pada-node-sama-dan-approver-ancestor-descendant-berdampingan | FE+BE |
| TC-FA-RP-1214 | E2E | TC-FA-RP-E2E-379-approver-ancestor-dihitung-aktivasi-toggle-descendant-dan-descendant-tidak-dihitung-bagi-ancestor | FE+BE |
| TC-FA-RP-1215 | E2E | TC-FA-RP-E2E-379-approver-ancestor-dihitung-aktivasi-toggle-descendant-dan-descendant-tidak-dihitung-bagi-ancestor | FE+BE |
| TC-FA-RP-1216 | E2E | TC-FA-RP-E2E-380-approver-di-ancestor-tidak-mengubah-toggle-descendant | FE+BE |
| TC-FA-RP-1217 | E2E | TC-FA-RP-E2E-381-d09-jamak-remove-approver-ancestor-dan-d02-remove-gm-dengan-fallback-approver-ancestor | FE+BE |
| TC-FA-RP-1218 | E2E | TC-FA-RP-E2E-381-d09-jamak-remove-approver-ancestor-dan-d02-remove-gm-dengan-fallback-approver-ancestor | FE+BE |
| TC-FA-RP-1219 | E2E | TC-FA-RP-E2E-382-remove-approver-ancestor-d08-dan-remove-approver-descendant-tanpa-d09 | FE+BE |
| TC-FA-RP-1220 | E2E | TC-FA-RP-E2E-382-remove-approver-ancestor-d08-dan-remove-approver-descendant-tanpa-d09 | FE+BE |
| TC-FA-RP-1221 | E2E | TC-FA-RP-E2E-381-d09-jamak-remove-approver-ancestor-dan-d02-remove-gm-dengan-fallback-approver-ancestor | FE+BE |
| TC-FA-RP-1222 | E2E | TC-FA-RP-E2E-384-delete-group-melepas-penugasan-role-transaksi-node-dan-descendant | FE+BE |
| TC-FA-RP-1223 | E2E | TC-FA-RP-E2E-383-absence-log-assign-overlap-tidak-menghapus-ancestor-dan-satu-entri-per-penugasan | FE+BE |
| TC-FA-RP-1224 | E2E | TC-FA-RP-E2E-385-defense-in-depth-overlap-diterima-dan-role-sama-node-sama-ditolak-server | FE+BE |
| TC-FA-RP-1225 | E2E | TC-FA-RP-E2E-386-picker-asset-admin-ber-constraint-node-sama-dan-descendant-ya-sibling-dan-ancestor-tidak; TC-FA-RP-E2E-386-picker-asset-admin-ber-constraint-node-sama-dan-descendant-ya-sibling-dan-ancestor-tidak; TC-FA-RP-E2E-386-picker-asset-admin-ber-constraint-node-sama-dan-descendant-ya-sibling-dan-ancestor-tidak | FE+BE |
| TC-FA-RP-1226 | E2E | TC-FA-RP-E2E-387-picker-user-tanpa-constraint-muncul-di-empat-role-pada-node-mana-pun; TC-FA-RP-E2E-387-picker-user-tanpa-constraint-muncul-di-empat-role-pada-node-mana-pun; TC-FA-RP-E2E-387-picker-user-tanpa-constraint-muncul-di-empat-role-pada-node-mana-pun | FE+BE |
| TC-FA-RP-1227 | E2E | TC-FA-RP-E2E-388-gate-menilai-node-penugasan-baris-literal-descendant-tetap-eligible-di-luar-constraint-tidak; TC-FA-RP-E2E-388-gate-menilai-node-penugasan-baris-literal-descendant-tetap-eligible-di-luar-constraint-tidak; TC-FA-RP-E2E-388-gate-menilai-node-penugasan-baris-literal-descendant-tetap-eligible-di-luar-constraint-tidak | FE+BE |
| TC-FA-RP-1228 | E2E | TC-FA-RP-E2E-389-gate-sama-pada-picker-monitoring-report-staff-dan-approver; TC-FA-RP-E2E-389-gate-sama-pada-picker-monitoring-report-staff-dan-approver | FE+BE |
| TC-FA-RP-1229 | E2E | TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint; TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint | FE+BE |
| TC-FA-RP-1230 | E2E | TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint; TC-FA-RP-E2E-390-pola-total-control-dan-read-only-menulis-baris-pola-role-transaksi-tanpa-cek-constraint | FE+BE |
| TC-FA-RP-1231 | E2E | TC-FA-RP-E2E-392-d-10-plural-group-role-role-transaksi-group-manager-dan-cancel | FE+BE |
| TC-FA-RP-1232 | E2E | TC-FA-RP-E2E-392-d-10-plural-group-role-role-transaksi-group-manager-dan-cancel; TC-FA-RP-E2E-392-d-10-plural-group-role-role-transaksi-group-manager-dan-cancel | FE+BE |
| TC-FA-RP-1233 | E2E | TC-FA-RP-E2E-393-absence-log-pencabutan-role-transaksi-via-d-10-silent-tanpa-notifikasi-dan-tanpa-entri-log; TC-FA-RP-E2E-393-absence-log-pencabutan-role-transaksi-via-d-10-silent-tanpa-notifikasi-dan-tanpa-entri-log; TC-FA-RP-E2E-393-absence-log-pencabutan-role-transaksi-via-d-10-silent-tanpa-notifikasi-dan-tanpa-entri-log | FE+BE |
| TC-FA-RP-1234 | E2E | TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog; TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog; TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog; TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog | FE+BE |
| TC-FA-RP-1235 | E2E | TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog; TC-FA-RP-E2E-394-pola-total-control-read-only-tidak-didaftar-d-10-dan-constraint-tanpa-dialog | FE+BE |
| TC-FA-RP-1236 | E2E | TC-FA-RP-E2E-395-tanpa-migrasi-penugasan-role-transaksi-lama-tetap-dan-assign-baru-tidak-tersedia; TC-FA-RP-E2E-395-tanpa-migrasi-penugasan-role-transaksi-lama-tetap-dan-assign-baru-tidak-tersedia | FE+BE |
| TC-FA-RP-1237 | E2E | TC-FA-RP-E2E-391-baris-pola-gm-role-transaksi-tidak-dikecualikan-hanya-di-dalam-constraint; TC-FA-RP-E2E-391-baris-pola-gm-role-transaksi-tidak-dikecualikan-hanya-di-dalam-constraint; TC-FA-RP-E2E-391-baris-pola-gm-role-transaksi-tidak-dikecualikan-hanya-di-dalam-constraint | FE+BE |
| TC-FA-RP-1238 | E2E | TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima; TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima | FE+BE |
| TC-FA-RP-1239 | E2E | TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima; TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima; TC-FA-RP-E2E-396-defense-in-depth-request-langsung-role-transaksi-ancestor-sibling-ditolak-dalam-constraint-diterima | FE+BE |

---

## 4. Catatan Penulisan

- Nomor TC yang tidak ada di file TC (dilewati sesuai rencana): 52, 365-370, 468, 615, 616, 772, 896, 903.
- Sebagian spec memakai nomor cadangan (295-317) untuk memecah spec yang melewati sekitar 35 langkah; pemetaan TC ke spec di bagian 1 dan 3 mengikuti hasil akhir, bukan tabel rencana awal.
- TC yang sengaja ada di dua spec (spec asal dan spec absence kelas g, S-05): 283, 300, 357, 413, 461, 913, 957, 961, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 1041, 1098, 1210, 1211. `check-suite.py` menandai ini sebagai C2; itu disengaja.
- Spec yang melewati 35 langkah memuat alasan di Notes (C6); sebagian besar karena ekspansi blok berulang per kolom atau per data.
- Fixture `Fixture.*` untuk modul ini, akun tenant khusus dan nama env password baru belum ada; ditandai di Prerequisites tiap spec sebagai disediakan tim FE/BE dan dicatat di Temuan untuk QA.
- Spec 318-338, 341-343, dan 345 ditambahkan untuk TC-FA-RP-1145 sampai 1178 (Group Role dan Transaction Role masuk pola tier Total Control/Read Only). Nomor cadangan dipakai untuk memecah spec yang melewati sekitar 35 langkah (337, 338, 341, 342, 343, 345); nomor 339, 340, 344, 346 sampai 350 tidak dipakai. Setiap TC baru muncul di tepat satu spec.
- Spec 346-370 (25 spec) ditambahkan untuk TC-FA-RP-1179 sampai 1202 (pola Group Manager: Assign/Remove menulis dan menghapus baris pola, auto-revert, Home Group constraint, Delete Group, kontrol UI, defense-in-depth). Nomor cadangan 361-368 dan nomor berikutnya (369, 370) dipakai untuk memecah spec yang melewati sekitar 35 langkah; nomor 344 tidak dipakai. TC yang sengaja ada di dua spec (pemecahan): 1186, 1195; `check-suite.py` menandai ini sebagai C2. Spec yang tetap melewati 35 langkah memuat alasan di Notes. Hal ambigu (Open Item #7c, nama Action `via Group Manager`, copy usulan, seed Kevin Susanto) dicatat di Temuan untuk QA tiap spec.
- Fix pass 2 (TC pola Group Manager berubah): jumlah langkah diperbarui untuk spec lama yang diedit: -068-as (40 menjadi 46), -070-re (43 menjadi 46), -071-re (30 menjadi 36), -075-as (44 menjadi 52), -076-as (31 menjadi 39), -117-au (41 menjadi 42), -260-pe (29 menjadi 36), -277-de (23 menjadi 24).
- Fix pass 4 (GM auto-revert mempertahankan baris; TC 395, 396, 397, 399, 400, 1188 sampai 1193 diubah, TC-FA-RP-1203 dan TC-FA-RP-1204 baru): spec 117, 118, 354, 355, 356, 357, 365, dan 366 diperbarui; jumlah langkah: -117-au (42 menjadi 38), -354-au (34 menjadi 33), -355-au (30 menjadi 38), -356-as (39 menjadi 41), -357-ba (42 menjadi 46), -365-au (23 menjadi 29), -366-su (50 menjadi 51); -118-au tetap 39 (hanya teks dialog). TC-FA-RP-397 dipindah dari spec 117 ke spec 373; spec 371 (TC-FA-RP-1203), 372 (TC-FA-RP-1204), dan 373 (TC-FA-RP-397) ditambahkan.
- Spec 374-385 (12 spec) ditambahkan untuk TC-FA-RP-1205 sampai 1224 (Role Transaksi mencakup node + descendant: preview scope, overlap, tangga, D-13, Approver ancestor, D-09 jamak, absence log, Delete Group, defense-in-depth). Nomor cadangan 386-391 tidak dipakai. TC-FA-RP-1210 dan 1211 ada di dua spec (377 fungsional, 383 absence log klausa c, S-05).
- Fix pass 5 (Role Transaksi mencakup node + descendant; TC 308-311, 326, 338-342, 455, 459, 460, 901, 957, 1012, 1094, 1096, 1202, 1203 diubah): spec 094, 100, 102, 103, 129 (Notes), 131, 132, 133, 267, 277, 292, 359, dan 371 diperbarui; spec 096, 097, dan 304 diperiksa dan tidak usang. Jumlah langkah: -100-ro (31 menjadi 35); lainnya tetap. Slug lama (mis. node-exact) tidak diubah.
- Spec 386-396 (11 spec) ditambahkan untuk TC-FA-RP-1225 sampai 1239 (Home Group constraint pada Role Transaksi: picker kandidat, pola Total Control/Read Only/GM, D-10 jamak dan silent, tanpa migrasi, defense-in-depth). Nomor cadangan 397-404 tidak dipakai; tiap TC ada di tepat satu spec.
- Fix pass 6 (Home Group constraint Role Transaksi; TC 313, 314, 409, 953, 954, 1124, 1209 diubah): spec 095, 097, 120, 275, 376, dan 384 diperbarui; spec 094, 119, 121, 351, 369, 012, 013, 206-217, 262-264 diperiksa dan tidak usang. Jumlah langkah: -095 (46 menjadi 48), -120 (51 menjadi 55); lainnya tetap.
