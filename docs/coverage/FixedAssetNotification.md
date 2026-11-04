# Coverage E2E — Fixed Asset > Notification

Sumber: `fixed-asset/notification/TestCases/tc-notification.md` (466 TC granular aktif, `TC-FA-NOTIF-1`–`481`) dan `fixed-asset/notification/TestCases/tc-notification-backend.md` (hanya untuk mengenali TC kontrak API).
Suite: `specs/FixedAsset/Notification/`. Prefix Modul: `FA` + `NOTIF` (`TC-FA-NOTIF-E2E-*`). Status semua spec: `draft`, belum ada script.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 466 TC masuk 121 spec, 0 TC dilewati karena hanya-BE. `tc-notification-backend.md` disusun per endpoint dan tidak merujuk ID TC granular, sehingga tidak ada TC yang dapat dipastikan hanya-BE. TC kelas a dengan Expected respons API masuk spec FE+BE dengan butir K-1 di Notes (spec 100).

---

## 1. Pemetaan TC granular ke spec e2e (121 spec)

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-NOTIF-E2E-001-bell-icon-screening-badge-dan-buka-tutup-panel | Bell Icon: Screening, Badge Real-Time, serta Buka dan Tutup Dropdown Panel | FE+BE | 10 | 1, 4, 8 |
| TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | Dropdown Panel: Screening, State Item Unread dan Read, serta Batas Lima Item | FE+BE | 35 | 9, 10, 12, 13, 14, 15, 23 |
| TC-FA-NOTIF-E2E-003-variasi-data-badge-99-body-panjang-dan-tab-unread-kosong | Variasi Data Seed: Badge 99 dan 99+, Body Panjang, dan Empty State Tab Unread | FE+BE | 15 | 3, 11, 25 |
| TC-FA-NOTIF-E2E-004-empty-state-client-tanpa-notifikasi | Empty State Client Tanpa Notifikasi: Badge Hidden, Dropdown Panel, dan Notification Center | FE+BE | 11 | 2, 16, 24 |
| TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | Notification Center: Screening, Breadcrumb, dan Guard Lingkup V1 | FE+BE | 25 | 20, 21, 22, 29, 30, 31 |
| TC-FA-NOTIF-E2E-006-state-loading-dropdown-panel-dan-notification-center | State Loading Dropdown Panel dan Notification Center serta Tooltip Icon Toolbar | FE+BE | 15 | 17, 26, 58 |
| TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | Timestamp Relatif Item Notifikasi di Dropdown Panel dan Notification Center | FE+BE | 36 | 34, 35, 36, 37, 38, 39, 40 |
| TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings | Format Tanggal Mengikuti Date Format General Settings | FE+BE | 17 | 41, 42, 43, 44 |
| TC-FA-NOTIF-E2E-009-aksesibilitas-keyboard-dropdown-panel-dan-notification-center | Aksesibilitas Keyboard Dropdown Panel dan Notification Center | FE+BE | 14 | 32, 33 |
| TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | Guided Tooltip fa-notification: Kunjungan Pertama, Konten Step 1 sampai 3, dan Back | FE+BE | 26 | 45, 46, 47, 49, 53 |
| TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | Guided Tooltip: Menutup Tur lewat Done, Skip, Overlay, atau Navigasi Keluar dan Penyimpanan Flag Seen | FE+BE | 35 | 50, 51, 52, 428, 429 |
| TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi | Guided Tooltip: Resize Viewport, Keyboard, Varian Tanpa Notifikasi, dan Replay lewat Tombol Bantuan | FE+BE | 36 | 48, 54, 55, 56 |
| TC-FA-NOTIF-E2E-013-android-bell-dropdown-panel-dan-notification-center | Android: Dot Bell Icon, Dropdown Panel Bottom Sheet, dan Tata Letak Notification Center | FE+BE | 18 | 6, 385, 399 |
| TC-FA-NOTIF-E2E-014-android-dot-real-time-dan-guided-tooltip-step-2 | Android: Dot Bell Icon Real-Time via SSE dan Guided Tooltip Step 2 Tanpa Notifikasi | FE+BE | 12 | 7, 430 |
| TC-FA-NOTIF-E2E-015-role-matrix-visibilitas-elemen-total-control-dan-read-only | Role Matrix: Visibilitas Elemen Notifikasi Total Control dan Read Only | FE+BE | 8 | 59, 60 |
| TC-FA-NOTIF-E2E-016-role-matrix-visibilitas-elemen-group-manager-dan-staff | Role Matrix: Visibilitas Elemen Notifikasi Group Manager dan Staff | FE+BE | 8 | 61, 62 |
| TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | Role Matrix: Penerima Negatif Notifikasi Actionable Approval Borrow per Role | FE+BE | 12 | 63, 65, 67, 69, 410 |
| TC-FA-NOTIF-E2E-018-penerima-positif-per-role | Penerima Positif Notifikasi per Role: Subjek Transaksi, Approver, Group Manager, dan Borrower | FE+BE | 24 | 64, 66, 68, 70 |
| TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri | Penerima Notifikasi: Target Perubahan Akses, Tier Plan, dan Isolasi Notifikasi Milik Sendiri | FE+BE | 41 | 71, 72, 73, 322 |
| TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar | Mark as Read: Dropdown Panel dan Notification Center Dasar | FE+BE | 32 | 74, 75, 78, 80 |
| TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity | Mark as Read: Klik Area Item, Tab Unread, dan Severity Item | FE+BE | 31 | 81, 82, 83, 84 |
| TC-FA-NOTIF-E2E-022-state-tenant-client-suspended-atau-expired | State Tenant: Client Suspended atau Expired pada Detail dan Mark as Read | FE+BE | 16 | 365, 394 |
| TC-FA-NOTIF-E2E-023-klik-path-approvals-dan-detail-transaksi | Klik Path: Approvals dan Detail Transaksi per Kelompok Event | FE+BE | 16 | 85, 86 |
| TC-FA-NOTIF-E2E-024-klik-path-my-asset | Klik Path: My Asset Task, Borrowed, Assigned, dan Borrow List Ter-highlight | FE+BE | 30 | 87, 88, 89, 91 |
| TC-FA-NOTIF-E2E-025-klik-path-assignment-transfer-disposal | Klik Path: Detail Transaksi Assignment, Transfer, dan Disposal Reported | FE+BE | 28 | 90, 92, 93 |
| TC-FA-NOTIF-E2E-026-klik-path-asset-audit-dan-profil | Klik Path: Asset Detail, Task Audit, dan Halaman Profil | FE+BE | 21 | 96, 97, 98 |
| TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | Detail dan Klik Area Item Actionable: Navigasi Tanpa Mengubah Status Baca | FE+BE | 33 | 99, 105, 107, 381, 386 |
| TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | Dialog D-01 Transaction Resolved dari Dropdown Panel | FE+BE | 31 | 100, 102, 103, 108, 421 |
| TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center | Dialog D-01 Transaction Resolved dari Notification Center dan Penutupan dengan Esc | FE+BE | 38 | 101, 392, 422, 423 |
| TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan | Pre-check Detail: Kehilangan Role, Race 409, dan Validasi Submit di Halaman Tujuan | FE+BE | 50 | 104, 110, 363, 424 |
| TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | Auto-Read Borrow: Approve, Reject, Cancel Form, Navigasi Keluar, Detail Berulang, dan Atomisitas dengan Commit | FE+BE | 40 | 111, 112, 113, 114, 115, 161 |
| TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | Auto-Read Waiting Approval: Approve Assignment, Pembatalan Requester, Auto-Cancel, Override Group Manager, dan Almost Timeout | FE+BE | 25 | 117, 121, 122, 123, 372, 434 |
| TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | Auto-Read Multi-Approver AND, Scope Both Transfer, dan Dual-Group Disposal | FE+BE | 26 | 124, 125, 126, 127, 128 |
| TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | Auto-Read Approver Transfer, Disposal, dan Audit: Approve, Reject, Auto-Cancel, dan Pembatalan Requester | FE+BE | 39 | 118, 119, 120, 153, 154, 435, 436, 440 |
| TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | Auto-Read Borrower dan Assignee: Konfirmasi, Accept, Decline, Pembatalan, Kedaluwarsa, dan Tingkat Transaksi | FE+BE | 45 | 130, 131, 132, 133, 134, 135, 367, 368 |
| TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | Auto-Read Borrow untuk PIC Admin dan Borrower: Return, Extend, Handover, Cancel, dan Notifikasi View-Only | FE+BE | 27 | 136, 137, 138, 139, 155, 156 |
| TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed | Auto-Read assignment_accepted dan transfer_departed: Handover, Arrival, dan Pembatalan | FE+BE | 17 | 149, 150, 151, 152 |
| TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | Auto-Read Task Audit untuk Auditor: Finish Audit, Stop, Cancel, dan Perpindahan Status | FE+BE | 34 | 140, 141, 142, 143, 144, 369, 370, 371 |
| TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | Auto-Read Task Audit untuk Asset Admin dan Reminder Damaged dan Missing untuk Group Manager | FE+BE | 34 | 145, 146, 147, 148, 157, 158, 159, 160 |
| TC-FA-NOTIF-E2E-040-auto-read-tag-report | Auto-Read Event Tag: tag_report_created dan tag_report_open_reminder Read saat Laporan Ditutup | FE+BE | 20 | 468, 469, 470, 471, 478 |
| TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | Dedup Multi-Role: Satu Notifikasi per Event untuk Pengguna dengan Beberapa Peran | FE+BE | 40 | 162, 163, 164, 165, 166, 167, 168 |
| TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | Dua Event Bersamaan, Resubmit setelah Reject, dan Idempotensi Pembuatan Notifikasi | FE+BE | 29 | 169, 170, 171, 359, 362 |
| TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | SSE: Notifikasi Baru di Notification Center menurut Sort, Tab, Search, dan Filter | FE+BE | 35 | 172, 173, 174, 175, 176 |
| TC-FA-NOTIF-E2E-044-sse-badge-dan-dropdown-panel-real-time | SSE: Badge Bell Icon dan Dropdown Panel Real-Time | FE+BE | 23 | 180, 181, 182 |
| TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | Tab All dan Unread serta Search Dasar Notification Center | FE+BE | 36 | 183, 184, 185, 186, 187, 425 |
| TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan | Search Notification Center: Siklus Interaksi, Pencocokan, Enter, dan Trim Spasi | FE+BE | 49 | 188, 189, 190, 191 |
| TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter | Search Lanjutan: Input Kosong, Karakter Khusus, Timestamp Relatif, dan Irisan dengan Filter | FE+BE | 31 | 192, 193, 194, 195 |
| TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | Filter Panel: Screening dan Isi Opsi Event Type | FE+BE | 35 | 196, 197, 198, 199, 200, 393 |
| TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | Filter Event Type: Multi-Select, Chip, Opsi Real-Time, dan Varian Event | FE+BE | 33 | 201, 202, 203, 204, 215, 216 |
| TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | Filter Date: Satu Tanggal, Batas Hari, Zona Waktu Tenant, Kombinasi dengan Event Type, dan Empty State | FE+BE | 29 | 205, 206, 207, 208, 426 |
| TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik | Filter Panel: Draft Dibuang, Clear Field, dan Indikator Titik | FE+BE | 27 | 209, 210, 214, 427 |
| TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | Independensi Search, Filter, dan Sort, Pemulihan dari Empty State, serta Urutan Newest dan Oldest | FE+BE | 39 | 211, 212, 213, 217, 218 |
| TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol | Infinite Scroll dan Retensi State Notification Center setelah Back dan Refresh | FE+BE | 32 | 220, 221, 224, 225 |
| TC-FA-NOTIF-E2E-054-transisi-empty-state-notification-center | Transisi Empty State Notification Center: Tab Unread Kosong dan Notifikasi Pertama via SSE | FE+BE | 17 | 382, 383 |
| TC-FA-NOTIF-E2E-055-pencatatan-absence-activity-log | Absence Activity Log: Mark as Read dan Auto-Read Tidak Menambah Entri | FE+BE | 12 | 351 |
| TC-FA-NOTIF-E2E-056-borrow-menunggu-persetujuan-dan-hasil-keputusan | Penerimaan Notifikasi Borrow: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject | FE+BE | 43 | 229, 230, 231 |
| TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue | Penerimaan Notifikasi Borrow oleh Borrower: Konfirmasi, Handover, Due Soon, dan Overdue | FE+BE | 60 | 232, 233, 234, 236 |
| TC-FA-NOTIF-E2E-058-penerima-pic-admin-due-soon-overdue-dan-acceptance-expired | Penerimaan Notifikasi oleh PIC Admin: Due Soon, Overdue, dan Acceptance Expired | FE+BE | 46 | 235, 237, 245 |
| TC-FA-NOTIF-E2E-059-assignment-menunggu-persetujuan-dan-hasil-keputusan | Penerimaan Notifikasi Assignment: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject | FE+BE | 43 | 238, 239, 240 |
| TC-FA-NOTIF-E2E-060-assignment-penerimaan-assignee-handover-dan-expired | Penerimaan Notifikasi Assignment oleh Assignee: Acceptance Required, Expired, dan Handover Selesai | FE+BE | 42 | 241, 244, 246 |
| TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif | Penerimaan Notifikasi Assignment Declined dan Accepted serta Penerima yang Tidak Berhak | FE+BE | 55 | 242, 243, 406, 407 |
| TC-FA-NOTIF-E2E-062-transfer-menunggu-persetujuan-dan-hasil-keputusan | Penerimaan Notifikasi Transfer: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject | FE+BE | 44 | 247, 248, 249 |
| TC-FA-NOTIF-E2E-063-transfer-departed-dan-scope-approval | Penerimaan Notifikasi Transfer Departed dan Scope Approval Group Asal atau Group Tujuan | FE+BE | 40 | 250, 404, 405 |
| TC-FA-NOTIF-E2E-064-disposal-menunggu-persetujuan-dan-hasil-keputusan | Penerimaan Notifikasi Disposal: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject | FE+BE | 44 | 251, 252, 253 |
| TC-FA-NOTIF-E2E-065-disposal-reported-dan-penerima | Penerimaan Notifikasi Disposal Reported: Flag Ringan Report Disposal dan Bukan Waiting for Approval | FE+BE | 23 | 254, 411 |
| TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset | Penerimaan Notifikasi Damaged Repaired dan Missing Found serta Satu Notifikasi per Aset | FE+BE | 46 | 255, 256, 311, 312 |
| TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue | Penerimaan Notifikasi Audit Task: Started, Grace Period, dan Overdue | FE+BE | 59 | 257, 258, 259, 260 |
| TC-FA-NOTIF-E2E-068-audit-approval-dan-hasil-keputusan | Penerimaan Notifikasi Audit: Menunggu Persetujuan dan Hasil Keputusan Approve atau Reject | FE+BE | 44 | 261, 262, 263 |
| TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima | Penerimaan Notifikasi Perubahan Akses Dicabut: Total Control, Read Only, Group Manager, dan Kejadian Berulang | FE+BE | 53 | 264, 265, 266, 378 |
| TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran | Penerimaan Notifikasi Perubahan Akses Auto-Reverted: Edit CRUD dan Remove Peran pada Total Control dan Read Only | FE+BE | 59 | 267, 268, 269, 270 |
| TC-FA-NOTIF-E2E-071-perubahan-akses-auto-reverted-group-manager | Penerimaan Notifikasi Perubahan Akses Auto-Reverted Group Manager: Edit CRUD, Remove Peran, dan Home Group | FE+BE | 44 | 271, 272, 273 |
| TC-FA-NOTIF-E2E-072-perubahan-akses-auto-reverted-role-transaksi | Penerimaan Notifikasi Perubahan Akses Auto-Reverted Varian Role Transaksi pada Total Control dan Read Only | FE+BE | 29 | 480, 481 |
| TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | Penerimaan Notifikasi License: Kuota Low dan Full serta Kondisi yang Tidak Mengirim Notifikasi | FE+BE | 61 | 441, 442, 443, 444, 447 |
| TC-FA-NOTIF-E2E-074-license-pemulihan-kuota-dan-penerima | Penerimaan Notifikasi License: Pemulihan Kuota Setelah Top-Up dan Penerima yang Berhak | FE+BE | 48 | 445, 446 |
| TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | Notasi Jamak Notifikasi Borrow untuk Borrower: Satu Notifikasi per Transaksi dan Satu per Aset untuk Pengingat | FE+BE | 46 | 289, 290, 310, 313, 314 |
| TC-FA-NOTIF-E2E-076-notasi-jamak-assignment | Notasi Jamak Notifikasi Assignment yang Diterima Assignee: Acceptance Required, Handover Completed, dan Acceptance Expired | FE+BE | 24 | 291, 294, 396 |
| TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval | Notasi Jamak Notifikasi Waiting for Approval untuk Approver: Borrow, Assignment, Transfer, dan Disposal | FE+BE | 32 | 295, 296, 297, 298 |
| TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | Notasi Jamak Notifikasi Resolved Approved dan Transfer Departed untuk Asset Admin | FE+BE | 40 | 299, 300, 301, 302, 303 |
| TC-FA-NOTIF-E2E-079-notasi-jamak-almost-timeout-dan-auto-canceled | Notasi Jamak Notifikasi Almost Timeout Varian PIC Admin: Borrow, Transfer, dan Disposal | FE+BE | 24 | 304, 306, 308 |
| TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset | Resolusi Penerima Notifikasi Berdasarkan Pemegang Aset: Group Manager, Borrower, Assignee, dan PIC Admin | FE+BE | 30 | 315, 316, 317, 319 |
| TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01 | Peminjam Nonaktif: Penerima Pengganti Atasan Peminjam untuk Overdue, Due Soon, Confirmation Required, dan Handover Completed (EC-BRW-01) | FE+BE | 42 | 318, 401, 402, 403 |
| TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login | Assignee Nonaktif dan Peminjam Non-login: Penerima Pengganti Atasan Assignee dan Pengguna Perwakilan | FE+BE | 46 | 387, 388, 389, 398 |
| TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name | Notifikasi TAG Replacement Needed: Satu Notifikasi per Asset Name per Penerima dan Scope Pemegang Update | FE+BE | 62 | 449, 450, 451, 452 |
| TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder | Notifikasi TAG Reported dan TAG Report Still Open: Report TAG, Unreadable Otomatis, Laporan Ganda, dan Job Pengingat | FE+BE | 63 | 459, 460, 461, 462 |
| TC-FA-NOTIF-E2E-085-tag-report-declined-dan-canceled | Notifikasi TAG Report Declined dan TAG Report Canceled: Decline Report, Cancel Report, dan Pembatal Tidak Menerima | FE+BE | 48 | 476, 479, 477 |
| TC-FA-NOTIF-E2E-086-almost-timeout-borrow-penerima-approver-requester-pic | Almost Timeout Borrow: Penerima Approver, Requester, dan PIC Admin | FE+BE | 0 | 274, 275, 276 |
| TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat | Auto Canceled Transaksi Pra-Komitmen dan Almost Timeout PIC Admin pada Fase Lanjut | FE+BE | 27 | 277, 285, 373, 374 |
| TC-FA-NOTIF-E2E-088-almost-timeout-transfer-penerima-approver-requester-pic | Almost Timeout Transfer: Penerima Approver, Requester, dan PIC Admin | FE+BE | 0 | 278, 279, 280 |
| TC-FA-NOTIF-E2E-089-transfer-auto-canceled-dan-transit-overdue | Transfer Auto Canceled dan Transit Overdue | FE+BE | 16 | 281, 286 |
| TC-FA-NOTIF-E2E-090-almost-timeout-disposal-penerima-approver-requester-pic | Almost Timeout Disposal: Penerima Approver, Requester, dan PIC Admin | FE+BE | 0 | 282, 283, 284 |
| TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset | Reminder Damaged dan Missing: Diterima Group Manager dan PIC Aset | FE+BE | 0 | 287, 288, 408, 409 |
| TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | Interval Pengingat Damaged dan Missing: Batas Hari dan Pengaturan OFF | FE+BE | 18 | 431, 432, 433, 437, 438, 439 |
| TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | Ambang Due Soon Borrow: H-3, H-1, Hari-H, Date Format, dan Di Luar Ambang | FE+BE | 31 | 324, 325, 326, 350, 376 |
| TC-FA-NOTIF-E2E-094-due-soon-mundur-extend-dan-re-eksekusi-job | Due Soon: Ambang Terlewati saat Handover, Extend Due Date, dan Re-Eksekusi Job | FE+BE | 36 | 327, 328, 415 |
| TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | Overdue Borrow: Job Harian, Pengulangan Harian, Berhenti saat Return, dan Tidak Dikirim | FE+BE | 40 | 329, 330, 331, 332, 375 |
| TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | Almost Timeout Borrow: Batas Menit H-1 dan Satu Kali per Transaksi | FE+BE | 0 | 333, 334, 335, 336, 337, 417 |
| TC-FA-NOTIF-E2E-097-batas-auto-cancel-borrow-dan-transit-overdue-transfer | Batas Auto Cancel Borrow dan Transit Overdue Transfer | FE+BE | 34 | 338, 339, 342 |
| TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal | Siklus Pengingat Damaged dan Missing serta Flag Report Disposal | FE+BE | 28 | 343, 344, 345, 346 |
| TC-FA-NOTIF-E2E-099-perpindahan-status-task-audit-grace-period-nol-dan-period-rollover | Perpindahan Status Task Audit: Sekali per Perpindahan, Grace Period Nol, dan Period Rollover | FE+BE | 33 | 347, 348, 349 |
| TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | Defense-in-Depth: Request Langsung ke Server, Isolasi Kepemilikan Notifikasi, dan Payload XSS | FE+BE | 34 | 352, 353, 355, 357, 358, 400 |
| TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | Multi-Konteks: Multi-Tab Akun yang Sama dan Isolasi Push Antar User | FE+BE | 39 | 5, 79, 227, 356, 366 |
| TC-FA-NOTIF-E2E-102-multi-tab-approver-dan-flag-tooltip-lintas-perangkat | Multi-Konteks: Flag Guided Tooltip Lintas Perangkat dan Auto-Read Approver Lintas Tab | FE+BE | 35 | 57, 116, 384 |
| TC-FA-NOTIF-E2E-103-resilience-dropdown-panel-gagal-fetch-dan-pre-check | Resilience Dropdown Panel: Gagal Fetch Snapshot, Try Again, dan Gagal Pre-check Detail | FE+BE | 25 | 18, 19, 106 |
| TC-FA-NOTIF-E2E-104-resilience-notification-center-gagal-fetch-list-awal-dan-pre-check | Resilience Notification Center: Gagal Fetch List Awal, Try Again, dan Gagal Pre-check Detail | FE+BE | 26 | 27, 28, 380 |
| TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403 | Resilience Mark as Read: Gagal 5xx, Timeout Jaringan, dan Respons 403 | FE+BE | 28 | 76, 77, 354, 379 |
| TC-FA-NOTIF-E2E-106-resilience-sse-terputus-snapshot-dan-resync | Resilience SSE: Koneksi Terputus, Sinkron Snapshot, dan Pengambilan Ulang List dengan Kontrol Aktif | FE+BE | 28 | 177, 178, 179 |
| TC-FA-NOTIF-E2E-107-resilience-kegagalan-insert-notifikasi-di-server | Resilience Server: Kegagalan Insert Notifikasi pada Submit Borrow dan Job Terjadwal Borrow | FE+BE | 36 | 360, 361, 418 |
| TC-FA-NOTIF-E2E-110-klik-path-almost-timeout-dan-auto-canceled | Klik Path: Almost Timeout Approver, Almost Timeout Requester dan PIC Admin, serta Auto Canceled | FE+BE | 16 | 94, 95 |
| TC-FA-NOTIF-E2E-111-mark-as-read-tanpa-pre-check-dan-klik-area-item-di-notification-center | Mark as Read Tanpa Pre-check dan Klik Area Item View-Only di Notification Center | FE+BE | 20 | 109, 390, 391 |
| TC-FA-NOTIF-E2E-112-auto-read-multi-approver-almost-timeout-dan-approver-or-lintas-sesi | Auto-Read Multi-Approver: Almost Timeout hingga Auto-Cancel dan Task Diselesaikan Pihak Lain pada Approver OR | FE+BE | 19 | 129, 364 |
| TC-FA-NOTIF-E2E-113-kejadian-kedua-pada-aset-yang-sama-menghasilkan-notifikasi-baru | Kejadian Kedua pada Aset yang Sama Menghasilkan Notifikasi Baru: Damaged Repaired, Missing Found, dan Disposal Reported | FE+BE | 24 | 377, 412, 413 |
| TC-FA-NOTIF-E2E-114-reset-lewat-show-all-dan-kombinasi-empat-kontrol | Reset Kontrol lewat Show All dan Kombinasi Tab, Search, Filter, dan Sort | FE+BE | 20 | 226, 228 |
| TC-FA-NOTIF-E2E-115-tie-breaker-sort-notifikasi-bertimestamp-sama | Tie-Breaker Sort: Notifikasi Bertimestamp Sama Berurutan Deterministik | FE+BE | 12 | 219 |
| TC-FA-NOTIF-E2E-116-disposal-reported-penerima-monitoring-staff-dan-scope-group | Penerima Notifikasi Disposal Reported: Monitoring & Report Tidak Menerima, Staff dan Asset Admin Menerima, Approver di Luar Scope Tidak Menerima | FE+BE | 29 | 320, 321 |
| TC-FA-NOTIF-E2E-117-perubahan-akses-satu-notifikasi-per-group-yang-dilepas | Penerimaan Notifikasi Perubahan Akses Group Manager: Satu Notifikasi per Group yang Dilepas | FE+BE | 14 | 323, 414 |
| TC-FA-NOTIF-E2E-118-notasi-jamak-assignment-asset-admin-dan-group-manager | Notasi Jamak Notifikasi Assignment untuk Asset Admin dan Group Manager: Declined, Acceptance Expired, dan Accepted | FE+BE | 23 | 292, 397, 293 |
| TC-FA-NOTIF-E2E-119-notasi-jamak-auto-canceled-varian-pic-admin | Notasi Jamak Notifikasi Auto Canceled Varian PIC Admin: Borrow, Transfer, dan Disposal | FE+BE | 23 | 305, 307, 309 |
| TC-FA-NOTIF-E2E-120-task-audit-extend-dan-reject-notifikasi-siklus-berikutnya | Task Audit Extend dan Reject: Notifikasi Grace Period dan Overdue Siklus Berikutnya | FE+BE | 0 | 395, 420 |
| TC-FA-NOTIF-E2E-121-batas-acceptance-expired-assignment-48-jam-dan-idempotensi-job | Batas Acceptance Expired Assignment 48 Jam dan Idempotensi Job | FE+BE | 25 | 340, 341, 416 |
| TC-FA-NOTIF-E2E-122-resilience-kegagalan-insert-notifikasi-audit-dan-kuota-license | Resilience Server: Kegagalan Insert Notifikasi pada Task Audit dan Penilaian Kuota License | FE+BE | 29 | 419, 448 |
| TC-FA-NOTIF-E2E-123-resilience-notification-center-halaman-berikutnya-dan-refetch | Resilience Notification Center: Gagal Memuat Halaman Berikutnya dan Gagal Refetch Tab | FE+BE | 20 | 222, 223 |

Nomor spec 108–123 adalah nomor cadangan yang dipakai writer untuk memecah spec yang terlalu panjang; nomor yang direncanakan tidak dirapikan ulang. Spec dengan sekitar 35 langkah atau lebih memuat alasannya di `## Notes`.

## 2. Pemetaan TC ke spec (kebalikan)

| TC | Spec | Lapisan |
|---|---|---|
| TC-FA-NOTIF-1 | TC-FA-NOTIF-E2E-001-bell-icon-screening-badge-dan-buka-tutup-panel | FE+BE |
| TC-FA-NOTIF-2 | TC-FA-NOTIF-E2E-004-empty-state-client-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-3 | TC-FA-NOTIF-E2E-003-variasi-data-badge-99-body-panjang-dan-tab-unread-kosong | FE+BE |
| TC-FA-NOTIF-4 | TC-FA-NOTIF-E2E-001-bell-icon-screening-badge-dan-buka-tutup-panel | FE+BE |
| TC-FA-NOTIF-5 | TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | FE+BE |
| TC-FA-NOTIF-6 | TC-FA-NOTIF-E2E-013-android-bell-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-7 | TC-FA-NOTIF-E2E-014-android-dot-real-time-dan-guided-tooltip-step-2 | FE+BE |
| TC-FA-NOTIF-8 | TC-FA-NOTIF-E2E-001-bell-icon-screening-badge-dan-buka-tutup-panel | FE+BE |
| TC-FA-NOTIF-9 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-10 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-11 | TC-FA-NOTIF-E2E-003-variasi-data-badge-99-body-panjang-dan-tab-unread-kosong | FE+BE |
| TC-FA-NOTIF-12 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-13 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-14 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-15 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-16 | TC-FA-NOTIF-E2E-004-empty-state-client-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-17 | TC-FA-NOTIF-E2E-006-state-loading-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-18 | TC-FA-NOTIF-E2E-103-resilience-dropdown-panel-gagal-fetch-dan-pre-check | FE+BE |
| TC-FA-NOTIF-19 | TC-FA-NOTIF-E2E-103-resilience-dropdown-panel-gagal-fetch-dan-pre-check | FE+BE |
| TC-FA-NOTIF-20 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-21 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-22 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-23 | TC-FA-NOTIF-E2E-002-dropdown-panel-screening-item-tombol-dan-batas-lima | FE+BE |
| TC-FA-NOTIF-24 | TC-FA-NOTIF-E2E-004-empty-state-client-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-25 | TC-FA-NOTIF-E2E-003-variasi-data-badge-99-body-panjang-dan-tab-unread-kosong | FE+BE |
| TC-FA-NOTIF-26 | TC-FA-NOTIF-E2E-006-state-loading-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-27 | TC-FA-NOTIF-E2E-104-resilience-notification-center-gagal-fetch-list-awal-dan-pre-check | FE+BE |
| TC-FA-NOTIF-28 | TC-FA-NOTIF-E2E-104-resilience-notification-center-gagal-fetch-list-awal-dan-pre-check | FE+BE |
| TC-FA-NOTIF-29 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-30 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-31 | TC-FA-NOTIF-E2E-005-notification-center-screening-breadcrumb-dan-guard-lingkup-v1 | FE+BE |
| TC-FA-NOTIF-32 | TC-FA-NOTIF-E2E-009-aksesibilitas-keyboard-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-33 | TC-FA-NOTIF-E2E-009-aksesibilitas-keyboard-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-34 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-35 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-36 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-37 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-38 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-39 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-40 | TC-FA-NOTIF-E2E-007-timestamp-relatif-item-notifikasi | FE+BE |
| TC-FA-NOTIF-41 | TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings | FE+BE |
| TC-FA-NOTIF-42 | TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings | FE+BE |
| TC-FA-NOTIF-43 | TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings | FE+BE |
| TC-FA-NOTIF-44 | TC-FA-NOTIF-E2E-008-format-tanggal-mengikuti-date-format-general-settings | FE+BE |
| TC-FA-NOTIF-45 | TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | FE+BE |
| TC-FA-NOTIF-46 | TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | FE+BE |
| TC-FA-NOTIF-47 | TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | FE+BE |
| TC-FA-NOTIF-48 | TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-49 | TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | FE+BE |
| TC-FA-NOTIF-50 | TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | FE+BE |
| TC-FA-NOTIF-51 | TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | FE+BE |
| TC-FA-NOTIF-52 | TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | FE+BE |
| TC-FA-NOTIF-53 | TC-FA-NOTIF-E2E-010-guided-tooltip-konten-step-1-sampai-3 | FE+BE |
| TC-FA-NOTIF-54 | TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-55 | TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-56 | TC-FA-NOTIF-E2E-012-guided-tooltip-keyboard-replay-dan-varian-tanpa-notifikasi | FE+BE |
| TC-FA-NOTIF-57 | TC-FA-NOTIF-E2E-102-multi-tab-approver-dan-flag-tooltip-lintas-perangkat | FE+BE |
| TC-FA-NOTIF-58 | TC-FA-NOTIF-E2E-006-state-loading-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-59 | TC-FA-NOTIF-E2E-015-role-matrix-visibilitas-elemen-total-control-dan-read-only | FE+BE |
| TC-FA-NOTIF-60 | TC-FA-NOTIF-E2E-015-role-matrix-visibilitas-elemen-total-control-dan-read-only | FE+BE |
| TC-FA-NOTIF-61 | TC-FA-NOTIF-E2E-016-role-matrix-visibilitas-elemen-group-manager-dan-staff | FE+BE |
| TC-FA-NOTIF-62 | TC-FA-NOTIF-E2E-016-role-matrix-visibilitas-elemen-group-manager-dan-staff | FE+BE |
| TC-FA-NOTIF-63 | TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | FE+BE |
| TC-FA-NOTIF-64 | TC-FA-NOTIF-E2E-018-penerima-positif-per-role | FE+BE |
| TC-FA-NOTIF-65 | TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | FE+BE |
| TC-FA-NOTIF-66 | TC-FA-NOTIF-E2E-018-penerima-positif-per-role | FE+BE |
| TC-FA-NOTIF-67 | TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | FE+BE |
| TC-FA-NOTIF-68 | TC-FA-NOTIF-E2E-018-penerima-positif-per-role | FE+BE |
| TC-FA-NOTIF-69 | TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | FE+BE |
| TC-FA-NOTIF-70 | TC-FA-NOTIF-E2E-018-penerima-positif-per-role | FE+BE |
| TC-FA-NOTIF-71 | TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri | FE+BE |
| TC-FA-NOTIF-72 | TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri | FE+BE |
| TC-FA-NOTIF-73 | TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri | FE+BE |
| TC-FA-NOTIF-74 | TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar | FE+BE |
| TC-FA-NOTIF-75 | TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar | FE+BE |
| TC-FA-NOTIF-76 | TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403 | FE+BE |
| TC-FA-NOTIF-77 | TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403 | FE+BE |
| TC-FA-NOTIF-78 | TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar | FE+BE |
| TC-FA-NOTIF-79 | TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | FE+BE |
| TC-FA-NOTIF-80 | TC-FA-NOTIF-E2E-020-mark-as-read-dropdown-dan-center-dasar | FE+BE |
| TC-FA-NOTIF-81 | TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity | FE+BE |
| TC-FA-NOTIF-82 | TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity | FE+BE |
| TC-FA-NOTIF-83 | TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity | FE+BE |
| TC-FA-NOTIF-84 | TC-FA-NOTIF-E2E-021-mark-as-read-area-item-tab-unread-dan-severity | FE+BE |
| TC-FA-NOTIF-85 | TC-FA-NOTIF-E2E-023-klik-path-approvals-dan-detail-transaksi | FE+BE |
| TC-FA-NOTIF-86 | TC-FA-NOTIF-E2E-023-klik-path-approvals-dan-detail-transaksi | FE+BE |
| TC-FA-NOTIF-87 | TC-FA-NOTIF-E2E-024-klik-path-my-asset | FE+BE |
| TC-FA-NOTIF-88 | TC-FA-NOTIF-E2E-024-klik-path-my-asset | FE+BE |
| TC-FA-NOTIF-89 | TC-FA-NOTIF-E2E-024-klik-path-my-asset | FE+BE |
| TC-FA-NOTIF-90 | TC-FA-NOTIF-E2E-025-klik-path-assignment-transfer-disposal | FE+BE |
| TC-FA-NOTIF-91 | TC-FA-NOTIF-E2E-024-klik-path-my-asset | FE+BE |
| TC-FA-NOTIF-92 | TC-FA-NOTIF-E2E-025-klik-path-assignment-transfer-disposal | FE+BE |
| TC-FA-NOTIF-93 | TC-FA-NOTIF-E2E-025-klik-path-assignment-transfer-disposal | FE+BE |
| TC-FA-NOTIF-94 | TC-FA-NOTIF-E2E-110-klik-path-almost-timeout-dan-auto-canceled | FE+BE |
| TC-FA-NOTIF-95 | TC-FA-NOTIF-E2E-110-klik-path-almost-timeout-dan-auto-canceled | FE+BE |
| TC-FA-NOTIF-96 | TC-FA-NOTIF-E2E-026-klik-path-asset-audit-dan-profil | FE+BE |
| TC-FA-NOTIF-97 | TC-FA-NOTIF-E2E-026-klik-path-asset-audit-dan-profil | FE+BE |
| TC-FA-NOTIF-98 | TC-FA-NOTIF-E2E-026-klik-path-asset-audit-dan-profil | FE+BE |
| TC-FA-NOTIF-99 | TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | FE+BE |
| TC-FA-NOTIF-100 | TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | FE+BE |
| TC-FA-NOTIF-101 | TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center | FE+BE |
| TC-FA-NOTIF-102 | TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | FE+BE |
| TC-FA-NOTIF-103 | TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | FE+BE |
| TC-FA-NOTIF-104 | TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan | FE+BE |
| TC-FA-NOTIF-105 | TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | FE+BE |
| TC-FA-NOTIF-106 | TC-FA-NOTIF-E2E-103-resilience-dropdown-panel-gagal-fetch-dan-pre-check | FE+BE |
| TC-FA-NOTIF-107 | TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | FE+BE |
| TC-FA-NOTIF-108 | TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | FE+BE |
| TC-FA-NOTIF-109 | TC-FA-NOTIF-E2E-111-mark-as-read-tanpa-pre-check-dan-klik-area-item-di-notification-center | FE+BE |
| TC-FA-NOTIF-110 | TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan | FE+BE |
| TC-FA-NOTIF-111 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-112 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-113 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-114 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-115 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-116 | TC-FA-NOTIF-E2E-102-multi-tab-approver-dan-flag-tooltip-lintas-perangkat | FE+BE |
| TC-FA-NOTIF-117 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-118 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-119 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-120 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-121 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-122 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-123 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-124 | TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | FE+BE |
| TC-FA-NOTIF-125 | TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | FE+BE |
| TC-FA-NOTIF-126 | TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | FE+BE |
| TC-FA-NOTIF-127 | TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | FE+BE |
| TC-FA-NOTIF-128 | TC-FA-NOTIF-E2E-033-auto-read-multi-approver-and-scope-both-dan-dual-group | FE+BE |
| TC-FA-NOTIF-129 | TC-FA-NOTIF-E2E-112-auto-read-multi-approver-almost-timeout-dan-approver-or-lintas-sesi | FE+BE |
| TC-FA-NOTIF-130 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-131 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-132 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-133 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-134 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-135 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-136 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-137 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-138 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-139 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-140 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-141 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-142 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-143 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-144 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-145 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-146 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-147 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-148 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-149 | TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-150 | TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-151 | TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-152 | TC-FA-NOTIF-E2E-037-auto-read-assignment-accepted-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-153 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-154 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-155 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-156 | TC-FA-NOTIF-E2E-036-auto-read-view-only-pic-handover-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-157 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-158 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-159 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-160 | TC-FA-NOTIF-E2E-039-auto-read-task-audit-admin-dan-reminder-damaged-missing | FE+BE |
| TC-FA-NOTIF-161 | TC-FA-NOTIF-E2E-031-auto-read-borrow-approve-reject-cancel-dan-navigasi-keluar | FE+BE |
| TC-FA-NOTIF-162 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-163 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-164 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-165 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-166 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-167 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-168 | TC-FA-NOTIF-E2E-041-dedup-multi-role-satu-notifikasi-per-event | FE+BE |
| TC-FA-NOTIF-169 | TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | FE+BE |
| TC-FA-NOTIF-170 | TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | FE+BE |
| TC-FA-NOTIF-171 | TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | FE+BE |
| TC-FA-NOTIF-172 | TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | FE+BE |
| TC-FA-NOTIF-173 | TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | FE+BE |
| TC-FA-NOTIF-174 | TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | FE+BE |
| TC-FA-NOTIF-175 | TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | FE+BE |
| TC-FA-NOTIF-176 | TC-FA-NOTIF-E2E-043-sse-notifikasi-baru-di-notification-center | FE+BE |
| TC-FA-NOTIF-177 | TC-FA-NOTIF-E2E-106-resilience-sse-terputus-snapshot-dan-resync | FE+BE |
| TC-FA-NOTIF-178 | TC-FA-NOTIF-E2E-106-resilience-sse-terputus-snapshot-dan-resync | FE+BE |
| TC-FA-NOTIF-179 | TC-FA-NOTIF-E2E-106-resilience-sse-terputus-snapshot-dan-resync | FE+BE |
| TC-FA-NOTIF-180 | TC-FA-NOTIF-E2E-044-sse-badge-dan-dropdown-panel-real-time | FE+BE |
| TC-FA-NOTIF-181 | TC-FA-NOTIF-E2E-044-sse-badge-dan-dropdown-panel-real-time | FE+BE |
| TC-FA-NOTIF-182 | TC-FA-NOTIF-E2E-044-sse-badge-dan-dropdown-panel-real-time | FE+BE |
| TC-FA-NOTIF-183 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-184 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-185 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-186 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-187 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-188 | TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan | FE+BE |
| TC-FA-NOTIF-189 | TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan | FE+BE |
| TC-FA-NOTIF-190 | TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan | FE+BE |
| TC-FA-NOTIF-191 | TC-FA-NOTIF-E2E-046-search-siklus-interaksi-dan-pencocokan | FE+BE |
| TC-FA-NOTIF-192 | TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter | FE+BE |
| TC-FA-NOTIF-193 | TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter | FE+BE |
| TC-FA-NOTIF-194 | TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter | FE+BE |
| TC-FA-NOTIF-195 | TC-FA-NOTIF-E2E-047-search-lanjutan-karakter-khusus-dan-irisan-filter | FE+BE |
| TC-FA-NOTIF-196 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-197 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-198 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-199 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-200 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-201 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-202 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-203 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-204 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-205 | TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | FE+BE |
| TC-FA-NOTIF-206 | TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | FE+BE |
| TC-FA-NOTIF-207 | TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | FE+BE |
| TC-FA-NOTIF-208 | TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | FE+BE |
| TC-FA-NOTIF-209 | TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik | FE+BE |
| TC-FA-NOTIF-210 | TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik | FE+BE |
| TC-FA-NOTIF-211 | TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | FE+BE |
| TC-FA-NOTIF-212 | TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | FE+BE |
| TC-FA-NOTIF-213 | TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | FE+BE |
| TC-FA-NOTIF-214 | TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik | FE+BE |
| TC-FA-NOTIF-215 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-216 | TC-FA-NOTIF-E2E-049-filter-event-type-multi-select-dan-chip | FE+BE |
| TC-FA-NOTIF-217 | TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | FE+BE |
| TC-FA-NOTIF-218 | TC-FA-NOTIF-E2E-052-independensi-search-filter-sort-dan-tie-breaker | FE+BE |
| TC-FA-NOTIF-219 | TC-FA-NOTIF-E2E-115-tie-breaker-sort-notifikasi-bertimestamp-sama | FE+BE |
| TC-FA-NOTIF-220 | TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol | FE+BE |
| TC-FA-NOTIF-221 | TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol | FE+BE |
| TC-FA-NOTIF-222 | TC-FA-NOTIF-E2E-123-resilience-notification-center-halaman-berikutnya-dan-refetch | FE+BE |
| TC-FA-NOTIF-223 | TC-FA-NOTIF-E2E-123-resilience-notification-center-halaman-berikutnya-dan-refetch | FE+BE |
| TC-FA-NOTIF-224 | TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol | FE+BE |
| TC-FA-NOTIF-225 | TC-FA-NOTIF-E2E-053-infinite-scroll-retensi-state-dan-kombinasi-kontrol | FE+BE |
| TC-FA-NOTIF-226 | TC-FA-NOTIF-E2E-114-reset-lewat-show-all-dan-kombinasi-empat-kontrol | FE+BE |
| TC-FA-NOTIF-227 | TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | FE+BE |
| TC-FA-NOTIF-228 | TC-FA-NOTIF-E2E-114-reset-lewat-show-all-dan-kombinasi-empat-kontrol | FE+BE |
| TC-FA-NOTIF-229 | TC-FA-NOTIF-E2E-056-borrow-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-230 | TC-FA-NOTIF-E2E-056-borrow-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-231 | TC-FA-NOTIF-E2E-056-borrow-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-232 | TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue | FE+BE |
| TC-FA-NOTIF-233 | TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue | FE+BE |
| TC-FA-NOTIF-234 | TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue | FE+BE |
| TC-FA-NOTIF-235 | TC-FA-NOTIF-E2E-058-penerima-pic-admin-due-soon-overdue-dan-acceptance-expired | FE+BE |
| TC-FA-NOTIF-236 | TC-FA-NOTIF-E2E-057-borrow-penerima-borrower-konfirmasi-handover-due-soon-overdue | FE+BE |
| TC-FA-NOTIF-237 | TC-FA-NOTIF-E2E-058-penerima-pic-admin-due-soon-overdue-dan-acceptance-expired | FE+BE |
| TC-FA-NOTIF-238 | TC-FA-NOTIF-E2E-059-assignment-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-239 | TC-FA-NOTIF-E2E-059-assignment-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-240 | TC-FA-NOTIF-E2E-059-assignment-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-241 | TC-FA-NOTIF-E2E-060-assignment-penerimaan-assignee-handover-dan-expired | FE+BE |
| TC-FA-NOTIF-242 | TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif | FE+BE |
| TC-FA-NOTIF-243 | TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif | FE+BE |
| TC-FA-NOTIF-244 | TC-FA-NOTIF-E2E-060-assignment-penerimaan-assignee-handover-dan-expired | FE+BE |
| TC-FA-NOTIF-245 | TC-FA-NOTIF-E2E-058-penerima-pic-admin-due-soon-overdue-dan-acceptance-expired | FE+BE |
| TC-FA-NOTIF-246 | TC-FA-NOTIF-E2E-060-assignment-penerimaan-assignee-handover-dan-expired | FE+BE |
| TC-FA-NOTIF-247 | TC-FA-NOTIF-E2E-062-transfer-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-248 | TC-FA-NOTIF-E2E-062-transfer-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-249 | TC-FA-NOTIF-E2E-062-transfer-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-250 | TC-FA-NOTIF-E2E-063-transfer-departed-dan-scope-approval | FE+BE |
| TC-FA-NOTIF-251 | TC-FA-NOTIF-E2E-064-disposal-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-252 | TC-FA-NOTIF-E2E-064-disposal-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-253 | TC-FA-NOTIF-E2E-064-disposal-menunggu-persetujuan-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-254 | TC-FA-NOTIF-E2E-065-disposal-reported-dan-penerima | FE+BE |
| TC-FA-NOTIF-255 | TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset | FE+BE |
| TC-FA-NOTIF-256 | TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset | FE+BE |
| TC-FA-NOTIF-257 | TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue | FE+BE |
| TC-FA-NOTIF-258 | TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue | FE+BE |
| TC-FA-NOTIF-259 | TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue | FE+BE |
| TC-FA-NOTIF-260 | TC-FA-NOTIF-E2E-067-audit-task-lifecycle-started-grace-period-dan-overdue | FE+BE |
| TC-FA-NOTIF-261 | TC-FA-NOTIF-E2E-068-audit-approval-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-262 | TC-FA-NOTIF-E2E-068-audit-approval-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-263 | TC-FA-NOTIF-E2E-068-audit-approval-dan-hasil-keputusan | FE+BE |
| TC-FA-NOTIF-264 | TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima | FE+BE |
| TC-FA-NOTIF-265 | TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima | FE+BE |
| TC-FA-NOTIF-266 | TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima | FE+BE |
| TC-FA-NOTIF-267 | TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran | FE+BE |
| TC-FA-NOTIF-268 | TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran | FE+BE |
| TC-FA-NOTIF-269 | TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran | FE+BE |
| TC-FA-NOTIF-270 | TC-FA-NOTIF-E2E-070-perubahan-akses-auto-reverted-edit-crud-dan-remove-peran | FE+BE |
| TC-FA-NOTIF-271 | TC-FA-NOTIF-E2E-071-perubahan-akses-auto-reverted-group-manager | FE+BE |
| TC-FA-NOTIF-272 | TC-FA-NOTIF-E2E-071-perubahan-akses-auto-reverted-group-manager | FE+BE |
| TC-FA-NOTIF-273 | TC-FA-NOTIF-E2E-071-perubahan-akses-auto-reverted-group-manager | FE+BE |
| TC-FA-NOTIF-274 | TC-FA-NOTIF-E2E-086-almost-timeout-borrow-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-275 | TC-FA-NOTIF-E2E-086-almost-timeout-borrow-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-276 | TC-FA-NOTIF-E2E-086-almost-timeout-borrow-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-277 | TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat | FE+BE |
| TC-FA-NOTIF-278 | TC-FA-NOTIF-E2E-088-almost-timeout-transfer-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-279 | TC-FA-NOTIF-E2E-088-almost-timeout-transfer-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-280 | TC-FA-NOTIF-E2E-088-almost-timeout-transfer-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-281 | TC-FA-NOTIF-E2E-089-transfer-auto-canceled-dan-transit-overdue | FE+BE |
| TC-FA-NOTIF-282 | TC-FA-NOTIF-E2E-090-almost-timeout-disposal-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-283 | TC-FA-NOTIF-E2E-090-almost-timeout-disposal-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-284 | TC-FA-NOTIF-E2E-090-almost-timeout-disposal-penerima-approver-requester-pic | FE+BE |
| TC-FA-NOTIF-285 | TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat | FE+BE |
| TC-FA-NOTIF-286 | TC-FA-NOTIF-E2E-089-transfer-auto-canceled-dan-transit-overdue | FE+BE |
| TC-FA-NOTIF-287 | TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset | FE+BE |
| TC-FA-NOTIF-288 | TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset | FE+BE |
| TC-FA-NOTIF-289 | TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | FE+BE |
| TC-FA-NOTIF-290 | TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | FE+BE |
| TC-FA-NOTIF-291 | TC-FA-NOTIF-E2E-076-notasi-jamak-assignment | FE+BE |
| TC-FA-NOTIF-292 | TC-FA-NOTIF-E2E-118-notasi-jamak-assignment-asset-admin-dan-group-manager | FE+BE |
| TC-FA-NOTIF-293 | TC-FA-NOTIF-E2E-118-notasi-jamak-assignment-asset-admin-dan-group-manager | FE+BE |
| TC-FA-NOTIF-294 | TC-FA-NOTIF-E2E-076-notasi-jamak-assignment | FE+BE |
| TC-FA-NOTIF-295 | TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval | FE+BE |
| TC-FA-NOTIF-296 | TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval | FE+BE |
| TC-FA-NOTIF-297 | TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval | FE+BE |
| TC-FA-NOTIF-298 | TC-FA-NOTIF-E2E-077-notasi-jamak-waiting-approval | FE+BE |
| TC-FA-NOTIF-299 | TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-300 | TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-301 | TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-302 | TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-303 | TC-FA-NOTIF-E2E-078-notasi-jamak-resolved-dan-transfer-departed | FE+BE |
| TC-FA-NOTIF-304 | TC-FA-NOTIF-E2E-079-notasi-jamak-almost-timeout-dan-auto-canceled | FE+BE |
| TC-FA-NOTIF-305 | TC-FA-NOTIF-E2E-119-notasi-jamak-auto-canceled-varian-pic-admin | FE+BE |
| TC-FA-NOTIF-306 | TC-FA-NOTIF-E2E-079-notasi-jamak-almost-timeout-dan-auto-canceled | FE+BE |
| TC-FA-NOTIF-307 | TC-FA-NOTIF-E2E-119-notasi-jamak-auto-canceled-varian-pic-admin | FE+BE |
| TC-FA-NOTIF-308 | TC-FA-NOTIF-E2E-079-notasi-jamak-almost-timeout-dan-auto-canceled | FE+BE |
| TC-FA-NOTIF-309 | TC-FA-NOTIF-E2E-119-notasi-jamak-auto-canceled-varian-pic-admin | FE+BE |
| TC-FA-NOTIF-310 | TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | FE+BE |
| TC-FA-NOTIF-311 | TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset | FE+BE |
| TC-FA-NOTIF-312 | TC-FA-NOTIF-E2E-066-damaged-repaired-missing-found-dan-satu-notifikasi-per-aset | FE+BE |
| TC-FA-NOTIF-313 | TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | FE+BE |
| TC-FA-NOTIF-314 | TC-FA-NOTIF-E2E-075-notasi-jamak-borrower | FE+BE |
| TC-FA-NOTIF-315 | TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset | FE+BE |
| TC-FA-NOTIF-316 | TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset | FE+BE |
| TC-FA-NOTIF-317 | TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset | FE+BE |
| TC-FA-NOTIF-318 | TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01 | FE+BE |
| TC-FA-NOTIF-319 | TC-FA-NOTIF-E2E-080-resolusi-penerima-berdasarkan-pemegang-aset | FE+BE |
| TC-FA-NOTIF-320 | TC-FA-NOTIF-E2E-116-disposal-reported-penerima-monitoring-staff-dan-scope-group | FE+BE |
| TC-FA-NOTIF-321 | TC-FA-NOTIF-E2E-116-disposal-reported-penerima-monitoring-staff-dan-scope-group | FE+BE |
| TC-FA-NOTIF-322 | TC-FA-NOTIF-E2E-019-penerima-target-perubahan-akses-tier-plan-dan-isolasi-milik-sendiri | FE+BE |
| TC-FA-NOTIF-323 | TC-FA-NOTIF-E2E-117-perubahan-akses-satu-notifikasi-per-group-yang-dilepas | FE+BE |
| TC-FA-NOTIF-324 | TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | FE+BE |
| TC-FA-NOTIF-325 | TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | FE+BE |
| TC-FA-NOTIF-326 | TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | FE+BE |
| TC-FA-NOTIF-327 | TC-FA-NOTIF-E2E-094-due-soon-mundur-extend-dan-re-eksekusi-job | FE+BE |
| TC-FA-NOTIF-328 | TC-FA-NOTIF-E2E-094-due-soon-mundur-extend-dan-re-eksekusi-job | FE+BE |
| TC-FA-NOTIF-329 | TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | FE+BE |
| TC-FA-NOTIF-330 | TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | FE+BE |
| TC-FA-NOTIF-331 | TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | FE+BE |
| TC-FA-NOTIF-332 | TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | FE+BE |
| TC-FA-NOTIF-333 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-334 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-335 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-336 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-337 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-338 | TC-FA-NOTIF-E2E-097-batas-auto-cancel-borrow-dan-transit-overdue-transfer | FE+BE |
| TC-FA-NOTIF-339 | TC-FA-NOTIF-E2E-097-batas-auto-cancel-borrow-dan-transit-overdue-transfer | FE+BE |
| TC-FA-NOTIF-340 | TC-FA-NOTIF-E2E-121-batas-acceptance-expired-assignment-48-jam-dan-idempotensi-job | FE+BE |
| TC-FA-NOTIF-341 | TC-FA-NOTIF-E2E-121-batas-acceptance-expired-assignment-48-jam-dan-idempotensi-job | FE+BE |
| TC-FA-NOTIF-342 | TC-FA-NOTIF-E2E-097-batas-auto-cancel-borrow-dan-transit-overdue-transfer | FE+BE |
| TC-FA-NOTIF-343 | TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal | FE+BE |
| TC-FA-NOTIF-344 | TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal | FE+BE |
| TC-FA-NOTIF-345 | TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal | FE+BE |
| TC-FA-NOTIF-346 | TC-FA-NOTIF-E2E-098-siklus-pengingat-damaged-missing-dan-flag-report-disposal | FE+BE |
| TC-FA-NOTIF-347 | TC-FA-NOTIF-E2E-099-perpindahan-status-task-audit-grace-period-nol-dan-period-rollover | FE+BE |
| TC-FA-NOTIF-348 | TC-FA-NOTIF-E2E-099-perpindahan-status-task-audit-grace-period-nol-dan-period-rollover | FE+BE |
| TC-FA-NOTIF-349 | TC-FA-NOTIF-E2E-099-perpindahan-status-task-audit-grace-period-nol-dan-period-rollover | FE+BE |
| TC-FA-NOTIF-350 | TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | FE+BE |
| TC-FA-NOTIF-351 | TC-FA-NOTIF-E2E-055-pencatatan-absence-activity-log | FE+BE |
| TC-FA-NOTIF-352 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-353 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-354 | TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403 | FE+BE |
| TC-FA-NOTIF-355 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-356 | TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | FE+BE |
| TC-FA-NOTIF-357 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-358 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-359 | TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | FE+BE |
| TC-FA-NOTIF-360 | TC-FA-NOTIF-E2E-107-resilience-kegagalan-insert-notifikasi-di-server | FE+BE |
| TC-FA-NOTIF-361 | TC-FA-NOTIF-E2E-107-resilience-kegagalan-insert-notifikasi-di-server | FE+BE |
| TC-FA-NOTIF-362 | TC-FA-NOTIF-E2E-042-kejadian-berulang-baru-bersamaan-dan-idempotensi | FE+BE |
| TC-FA-NOTIF-363 | TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan | FE+BE |
| TC-FA-NOTIF-364 | TC-FA-NOTIF-E2E-112-auto-read-multi-approver-almost-timeout-dan-approver-or-lintas-sesi | FE+BE |
| TC-FA-NOTIF-365 | TC-FA-NOTIF-E2E-022-state-tenant-client-suspended-atau-expired | FE+BE |
| TC-FA-NOTIF-366 | TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user | FE+BE |
| TC-FA-NOTIF-367 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-368 | TC-FA-NOTIF-E2E-035-auto-read-borrower-assignee-konfirmasi-dan-penerimaan | FE+BE |
| TC-FA-NOTIF-369 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-370 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-371 | TC-FA-NOTIF-E2E-038-auto-read-task-audit-auditor | FE+BE |
| TC-FA-NOTIF-372 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-373 | TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat | FE+BE |
| TC-FA-NOTIF-374 | TC-FA-NOTIF-E2E-087-auto-canceled-dan-almost-timeout-fase-lanjut-pic-pembuat | FE+BE |
| TC-FA-NOTIF-375 | TC-FA-NOTIF-E2E-095-overdue-borrow-job-harian | FE+BE |
| TC-FA-NOTIF-376 | TC-FA-NOTIF-E2E-093-ambang-due-soon-borrow-h3-h1-hari-h | FE+BE |
| TC-FA-NOTIF-377 | TC-FA-NOTIF-E2E-113-kejadian-kedua-pada-aset-yang-sama-menghasilkan-notifikasi-baru | FE+BE |
| TC-FA-NOTIF-378 | TC-FA-NOTIF-E2E-069-perubahan-akses-dicabut-dan-aktor-tidak-menerima | FE+BE |
| TC-FA-NOTIF-379 | TC-FA-NOTIF-E2E-105-resilience-mark-as-read-5xx-timeout-dan-403 | FE+BE |
| TC-FA-NOTIF-380 | TC-FA-NOTIF-E2E-104-resilience-notification-center-gagal-fetch-list-awal-dan-pre-check | FE+BE |
| TC-FA-NOTIF-381 | TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | FE+BE |
| TC-FA-NOTIF-382 | TC-FA-NOTIF-E2E-054-transisi-empty-state-notification-center | FE+BE |
| TC-FA-NOTIF-383 | TC-FA-NOTIF-E2E-054-transisi-empty-state-notification-center | FE+BE |
| TC-FA-NOTIF-384 | TC-FA-NOTIF-E2E-102-multi-tab-approver-dan-flag-tooltip-lintas-perangkat | FE+BE |
| TC-FA-NOTIF-385 | TC-FA-NOTIF-E2E-013-android-bell-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-386 | TC-FA-NOTIF-E2E-027-detail-dan-klik-area-item-actionable | FE+BE |
| TC-FA-NOTIF-387 | TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login | FE+BE |
| TC-FA-NOTIF-388 | TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login | FE+BE |
| TC-FA-NOTIF-389 | TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login | FE+BE |
| TC-FA-NOTIF-390 | TC-FA-NOTIF-E2E-111-mark-as-read-tanpa-pre-check-dan-klik-area-item-di-notification-center | FE+BE |
| TC-FA-NOTIF-391 | TC-FA-NOTIF-E2E-111-mark-as-read-tanpa-pre-check-dan-klik-area-item-di-notification-center | FE+BE |
| TC-FA-NOTIF-392 | TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center | FE+BE |
| TC-FA-NOTIF-393 | TC-FA-NOTIF-E2E-048-filter-panel-screening-dan-opsi-event-type | FE+BE |
| TC-FA-NOTIF-394 | TC-FA-NOTIF-E2E-022-state-tenant-client-suspended-atau-expired | FE+BE |
| TC-FA-NOTIF-395 | TC-FA-NOTIF-E2E-120-task-audit-extend-dan-reject-notifikasi-siklus-berikutnya | FE+BE |
| TC-FA-NOTIF-396 | TC-FA-NOTIF-E2E-076-notasi-jamak-assignment | FE+BE |
| TC-FA-NOTIF-397 | TC-FA-NOTIF-E2E-118-notasi-jamak-assignment-asset-admin-dan-group-manager | FE+BE |
| TC-FA-NOTIF-398 | TC-FA-NOTIF-E2E-082-assignee-nonaktif-dan-peminjam-non-login | FE+BE |
| TC-FA-NOTIF-399 | TC-FA-NOTIF-E2E-013-android-bell-dropdown-panel-dan-notification-center | FE+BE |
| TC-FA-NOTIF-400 | TC-FA-NOTIF-E2E-100-defense-in-depth-request-langsung-isolasi-dan-xss | FE+BE |
| TC-FA-NOTIF-401 | TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01 | FE+BE |
| TC-FA-NOTIF-402 | TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01 | FE+BE |
| TC-FA-NOTIF-403 | TC-FA-NOTIF-E2E-081-peminjam-nonaktif-penerima-pengganti-ec-brw-01 | FE+BE |
| TC-FA-NOTIF-404 | TC-FA-NOTIF-E2E-063-transfer-departed-dan-scope-approval | FE+BE |
| TC-FA-NOTIF-405 | TC-FA-NOTIF-E2E-063-transfer-departed-dan-scope-approval | FE+BE |
| TC-FA-NOTIF-406 | TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif | FE+BE |
| TC-FA-NOTIF-407 | TC-FA-NOTIF-E2E-061-assignment-decline-accepted-dan-penerima-negatif | FE+BE |
| TC-FA-NOTIF-408 | TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset | FE+BE |
| TC-FA-NOTIF-409 | TC-FA-NOTIF-E2E-091-reminder-damaged-missing-diterima-gm-dan-pic-aset | FE+BE |
| TC-FA-NOTIF-410 | TC-FA-NOTIF-E2E-017-penerima-negatif-actionable-approval-per-role | FE+BE |
| TC-FA-NOTIF-411 | TC-FA-NOTIF-E2E-065-disposal-reported-dan-penerima | FE+BE |
| TC-FA-NOTIF-412 | TC-FA-NOTIF-E2E-113-kejadian-kedua-pada-aset-yang-sama-menghasilkan-notifikasi-baru | FE+BE |
| TC-FA-NOTIF-413 | TC-FA-NOTIF-E2E-113-kejadian-kedua-pada-aset-yang-sama-menghasilkan-notifikasi-baru | FE+BE |
| TC-FA-NOTIF-414 | TC-FA-NOTIF-E2E-117-perubahan-akses-satu-notifikasi-per-group-yang-dilepas | FE+BE |
| TC-FA-NOTIF-415 | TC-FA-NOTIF-E2E-094-due-soon-mundur-extend-dan-re-eksekusi-job | FE+BE |
| TC-FA-NOTIF-416 | TC-FA-NOTIF-E2E-121-batas-acceptance-expired-assignment-48-jam-dan-idempotensi-job | FE+BE |
| TC-FA-NOTIF-417 | TC-FA-NOTIF-E2E-096-batas-almost-timeout-h1-satu-kali-per-transaksi | FE+BE |
| TC-FA-NOTIF-418 | TC-FA-NOTIF-E2E-107-resilience-kegagalan-insert-notifikasi-di-server | FE+BE |
| TC-FA-NOTIF-419 | TC-FA-NOTIF-E2E-122-resilience-kegagalan-insert-notifikasi-audit-dan-kuota-license | FE+BE |
| TC-FA-NOTIF-420 | TC-FA-NOTIF-E2E-120-task-audit-extend-dan-reject-notifikasi-siklus-berikutnya | FE+BE |
| TC-FA-NOTIF-421 | TC-FA-NOTIF-E2E-028-dialog-d01-dari-dropdown-panel | FE+BE |
| TC-FA-NOTIF-422 | TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center | FE+BE |
| TC-FA-NOTIF-423 | TC-FA-NOTIF-E2E-029-dialog-d01-dari-notification-center | FE+BE |
| TC-FA-NOTIF-424 | TC-FA-NOTIF-E2E-030-pre-check-kehilangan-role-race-409-dan-halaman-tujuan | FE+BE |
| TC-FA-NOTIF-425 | TC-FA-NOTIF-E2E-045-tab-dan-search-dasar | FE+BE |
| TC-FA-NOTIF-426 | TC-FA-NOTIF-E2E-050-filter-date-satu-tanggal-zona-waktu-dan-kombinasi | FE+BE |
| TC-FA-NOTIF-427 | TC-FA-NOTIF-E2E-051-filter-panel-draft-clear-dan-indikator-titik | FE+BE |
| TC-FA-NOTIF-428 | TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | FE+BE |
| TC-FA-NOTIF-429 | TC-FA-NOTIF-E2E-011-guided-tooltip-menutup-tur-done-skip-overlay-resize-navigasi | FE+BE |
| TC-FA-NOTIF-430 | TC-FA-NOTIF-E2E-014-android-dot-real-time-dan-guided-tooltip-step-2 | FE+BE |
| TC-FA-NOTIF-431 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-432 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-433 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-434 | TC-FA-NOTIF-E2E-032-auto-read-pembatalan-requester-override-dan-assignment | FE+BE |
| TC-FA-NOTIF-435 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-436 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-437 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-438 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-439 | TC-FA-NOTIF-E2E-092-interval-pengingat-damaged-missing-batas-dan-pengaturan-off | FE+BE |
| TC-FA-NOTIF-440 | TC-FA-NOTIF-E2E-034-auto-read-transfer-disposal-audit-approver | FE+BE |
| TC-FA-NOTIF-441 | TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | FE+BE |
| TC-FA-NOTIF-442 | TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | FE+BE |
| TC-FA-NOTIF-443 | TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | FE+BE |
| TC-FA-NOTIF-444 | TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | FE+BE |
| TC-FA-NOTIF-445 | TC-FA-NOTIF-E2E-074-license-pemulihan-kuota-dan-penerima | FE+BE |
| TC-FA-NOTIF-446 | TC-FA-NOTIF-E2E-074-license-pemulihan-kuota-dan-penerima | FE+BE |
| TC-FA-NOTIF-447 | TC-FA-NOTIF-E2E-073-license-kuota-low-dan-full | FE+BE |
| TC-FA-NOTIF-448 | TC-FA-NOTIF-E2E-122-resilience-kegagalan-insert-notifikasi-audit-dan-kuota-license | FE+BE |
| TC-FA-NOTIF-449 | TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name | FE+BE |
| TC-FA-NOTIF-450 | TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name | FE+BE |
| TC-FA-NOTIF-451 | TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name | FE+BE |
| TC-FA-NOTIF-452 | TC-FA-NOTIF-E2E-083-tag-replacement-needed-satu-notifikasi-per-asset-name | FE+BE |
| TC-FA-NOTIF-459 | TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder | FE+BE |
| TC-FA-NOTIF-460 | TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder | FE+BE |
| TC-FA-NOTIF-461 | TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder | FE+BE |
| TC-FA-NOTIF-462 | TC-FA-NOTIF-E2E-084-tag-report-created-dan-reminder | FE+BE |
| TC-FA-NOTIF-468 | TC-FA-NOTIF-E2E-040-auto-read-tag-report | FE+BE |
| TC-FA-NOTIF-469 | TC-FA-NOTIF-E2E-040-auto-read-tag-report | FE+BE |
| TC-FA-NOTIF-470 | TC-FA-NOTIF-E2E-040-auto-read-tag-report | FE+BE |
| TC-FA-NOTIF-471 | TC-FA-NOTIF-E2E-040-auto-read-tag-report | FE+BE |
| TC-FA-NOTIF-476 | TC-FA-NOTIF-E2E-085-tag-report-declined-dan-canceled | FE+BE |
| TC-FA-NOTIF-477 | TC-FA-NOTIF-E2E-085-tag-report-declined-dan-canceled | FE+BE |
| TC-FA-NOTIF-478 | TC-FA-NOTIF-E2E-040-auto-read-tag-report | FE+BE |
| TC-FA-NOTIF-479 | TC-FA-NOTIF-E2E-085-tag-report-declined-dan-canceled | FE+BE |
| TC-FA-NOTIF-480 | TC-FA-NOTIF-E2E-072-perubahan-akses-auto-reverted-role-transaksi | FE+BE |
| TC-FA-NOTIF-481 | TC-FA-NOTIF-E2E-072-perubahan-akses-auto-reverted-role-transaksi | FE+BE |

## 3. TC hanya-BE (dilewati)

Tidak ada. Alasan: lihat paragraf pembuka.

## 4. Temuan untuk QA (ringkasan)

Gabungan butir "Temuan untuk QA" di `## Notes` setiap spec (rincian per spec ada di spec itu). Kelompok utama:

- **Akun dan password.** Banyak TC menulis role (Asset Admin, Approver, Borrower, Assignee, Auditor, Staff) tanpa nomor Pre-setup; spec memetakan ke tabel Pre-setup (mis. Approver Borrowing & Assignment #4, Asset Admin #8) dan mencatatnya. Nama env var password dan kunci `fixtures/fixedAssetNotification.json` adalah usulan dan belum terdaftar di `spectra.config.ts`, `.env.example` maupun fixture.
- **Kemampuan fixture BE.** TC, PRD, dan LLD tidak mendefinisikan cara menukar varian seed notifikasi (#17/#18), memicu event, menjalankan job terjadwal, menggeser jam server, memaksa kegagalan insert, membaca flag seen, atau mengubah status client. Spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13).
- **Pelaku pemicu tidak disebut.** Pelaku Cancel, Return, Extend, Approve, Handover, Reject dan sejenisnya tidak disebut di banyak TC; spec memakai sesi API aktor.
- **Data tidak disebut TC.** Title dan Body per event, tanggal job, jam pasti job, label tombol, jalur membuka Notification Center, dan cara mencabut role tidak ditulis; spec memilih nilai dan mencatatnya.
- **Expected kosong atau tidak teramati.** Post Condition banyak TC kosong dan tidak diasersi; beberapa Expected (mis. TC-394 status 403, TC-222 "tanpa mengulang halaman pertama") tidak teramati dari UI sehingga diasersi lewat cara lain yang dicatat di Notes.
- **Kontradiksi dan ketidakjelasan TC.** TC-354 berjudul akses notifikasi user lain tetapi langkahnya intercept 403; TC-99/105/107/381 meminta BRW-2026-0341 Waiting for Approval padahal seed N-06 menulisnya Rejected; TC-399 menyebut menu `[⋯]` memuat Filter tetapi memilih Sort; TC-72 mencakup empat client plan dalam satu TC; TC-330/331 punya precondition yang bertabrakan dengan langkahnya.
- **Bersyarat Open Item #6 PRD / belum final.** TC 311, 312, 315, 316, 317, 398 dan TC dengan copy NC-07; TC-386 menunggu pemilik modul tujuan.
- **Klasifikasi Manual Only (d).** TC 100, 101, 108, 363, 392, 110 ditandai Manual Only (d) tetapi dapat diotomasi lewat sesi API dan intercept SSE; spec mengotomasikannya.
- **Perangkat.** Spec 013 dan 014 (Android) butuh perangkat atau emulator; bila tidak tersedia, tandai `coverage.mobile: unsupported`.
- **Tanggal fixture.** Tanggal acuan fixture 18/06/26; TC-41 dan 42 bergantung pada tahun berjalan fixture, bukan tahun nyata.
- **Panjang spec.** Estimasi langkah di plan terlalu rendah karena belum menghitung pemulihan seed dan baseline per TC; beberapa spec melewati sekitar 35 langkah dengan alasan di Notes. Dua nomor cadangan per slice sudah habis.

## 5. Hasil check-suite


`python scripts/check-suite.py specs/FixedAsset/Notification ../fixed-asset/notification/TestCases/tc-notification.md docs/coverage/FixedAssetNotification.md`: 121 spec, 466 TC, 466 TC tercakup, 0 temuan.

`node_modules/.bin/spectra lint --strict specs/FixedAsset/Notification`: 121 spec dan 1 suite terverifikasi, 0 error lint. Halaman ini dibangkitkan ulang setelah fix pass 7 (jumlah langkah nominal dari spec).
