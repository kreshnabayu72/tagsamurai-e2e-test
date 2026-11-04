# Coverage E2E — Admin Console > Plans & Licensing > Lifecycle Settings

Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md` (687 ID `TC-AC-LCS-1`–`687`, semua aktif). Suite: `specs/AdminConsole/PlansLicensingLifecycleSettings/`. Prefix: `AC` + `LCS` (`TC-AC-LCS-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Berkas `tc-plans-licensing-lifecycle-settings-backend.md` ada, tetapi bukan sumber spec ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: seluruh 687 TC masuk 194 spec (total 5.192 langkah), tidak ada TC hanya-BE yang dilewati. Nomor spec 001–184 mengikuti rencana; nomor cadangan 185–196 dipakai untuk pemecahan (nomor 188 dan 190 tidak terpakai, sehingga ada 194 spec, bukan 196). Slug, judul, dan `sourceTc` pada tabel di bawah mengikuti frontmatter spec, bukan rencana. Spec yang dipecah ke nomor cadangan: 002 (menjadi 185), 013 (186), 045 (187), 084 (189), 092 (191), 119 (192), 154 dan 155 (193, 194), 163 dan 164 (196), 183 dan 184 (195). Semua spec bermode FE+BE dengan `coverage.web: automated`; tidak ada spec mock dan tidak ada spec mobile.

## TC hanya-BE (tidak masuk spec)

Tidak ada (0). Permintaan langsung ke server (kelas a, spec 168–183) tetap ditulis sebagai spec FE+BE karena hasilnya diamati di UI (nilai field, modal Changelog) lewat sesi API aktor.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-LCS-E2E-001-screening-tab-trial-free-license | Screening Halaman Lifecycle Settings: Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 38 | 1, 2, 3 |
| TC-AC-LCS-E2E-002-screening-tab-lifecycle-recycle | Screening Tab Client Lifecycle dan Recycle Bin | FE+BE | 28 | 4, 5 |
| TC-AC-LCS-E2E-003-deep-link-tab-trial-sampai-client-lifecycle | Deep Link Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle | FE+BE | 26 | 8, 9, 10, 11 |
| TC-AC-LCS-E2E-004-deep-link-tab-recycle-approval-limits | Deep Link Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 21 | 12, 13, 14 |
| TC-AC-LCS-E2E-005-refresh-riwayat-browser-dan-loading-awal | Refresh F5, Tombol Back dan Forward, dan State Loading Awal | FE+BE | 23 | 15, 16, 24 |
| TC-AC-LCS-E2E-006-breadcrumb-navigasi-dan-segmen | Breadcrumb Lifecycle Settings: Navigasi, State Aktif, dan Segmen Bukan Link | FE+BE | 28 | 17, 18, 19 |
| TC-AC-LCS-E2E-007-pindah-tab-dan-dirty-state-antar-tab | Pindah Tab Mempertahankan Perubahan dan Independensi Dirty State Antar Tab | FE+BE | 23 | 20, 21 |
| TC-AC-LCS-E2E-008-aksesibilitas-tab-bar-dan-viewport-sempit | Aksesibilitas Tab Bar dan Scroll Horizontal pada Viewport Sempit | FE+BE | 18 | 22, 23 |
| TC-AC-LCS-E2E-009-resilience-error-load-tab-trial-sampai-client-lifecycle | Resilience Error Load 500 Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle | FE+BE | 28 | 25, 26, 27, 28 |
| TC-AC-LCS-E2E-010-resilience-error-load-tab-recycle-approval-limits-dan-muat-ulang | Resilience Error Load 500 Tab Recycle Bin, Approval Settings, System Limits, dan Muat Ulang dari State Gagal | FE+BE | 27 | 29, 30, 31, 32 |
| TC-AC-LCS-E2E-011-nilai-default-instalasi-baru-trial-free-license | Nilai Default Instalasi Baru: Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 27 | 33, 34, 35 |
| TC-AC-LCS-E2E-012-nilai-default-instalasi-baru-lifecycle-recycle-approval-limits | Nilai Default Instalasi Baru: Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits | FE+BE | 41 | 36, 37, 38, 39 |
| TC-AC-LCS-E2E-013-tooltip-label-field-trial-free-license | Tooltip Label Field: Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 22 | 40, 41, 42 |
| TC-AC-LCS-E2E-014-tooltip-label-field-recycle-approval-limits-dan-addon | Tooltip Label Field Recycle Bin, Approval Settings, System Limits, Fokus Keyboard, dan Addon Satuan | FE+BE | 29 | 44, 45, 46, 47, 48 |
| TC-AC-LCS-E2E-015-guided-tooltip-alur-walkthrough | Guided Tooltip: Kunjungan Pertama dan Walkthrough Next, Back, serta Skip | FE+BE | 35 | 49, 50, 51, 52 |
| TC-AC-LCS-E2E-016-guided-tooltip-penutupan-dan-mulai-ulang | Guided Tooltip: Penutupan lewat Overlay dan Esc, Mulai Ulang lewat [?], dan Navigasi Keluar | FE+BE | 41 | 53, 54, 55, 56 |
| TC-AC-LCS-E2E-017-guided-tooltip-read-only | Guided Tooltip: Walkthrough Read Only Melewati Step Reset to Default dan Save | FE+BE | 10 | 57 |
| TC-AC-LCS-E2E-018-role-matrix-positif-sidebar-dan-halaman | Role Matrix Positif: Item Sidebar dan Halaman Lifecycle Settings Terbuka per Role | FE+BE | 26 | 58, 59, 60, 61 |
| TC-AC-LCS-E2E-019-role-matrix-negatif-sidebar-hidden | Role Matrix Negatif: Item Sidebar Hidden untuk Principal Tanpa Capability, Distributor, Partner, dan Client | FE+BE | 18 | 62, 64, 66, 68 |
| TC-AC-LCS-E2E-020-role-matrix-negatif-akses-langsung-url | Role Matrix Negatif: Akses Langsung URL Ditolak untuk Principal Tanpa Capability, Distributor, Partner, dan Client | FE+BE | 26 | 63, 65, 67, 69 |
| TC-AC-LCS-E2E-021-role-matrix-read-only-trial-free-license | Role Matrix: Read Only pada Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 37 | 70, 71, 72 |
| TC-AC-LCS-E2E-022-role-matrix-read-only-lifecycle-recycle | Role Matrix: Read Only pada Tab Client Lifecycle dan Recycle Bin | FE+BE | 32 | 73, 74 |
| TC-AC-LCS-E2E-023-role-matrix-read-only-approval-limits | Role Matrix: Read Only pada Tab Approval Settings dan System Limits | FE+BE | 26 | 75, 76 |
| TC-AC-LCS-E2E-024-role-matrix-positif-manage-plans-trial-free-license | Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 29 | 77, 78, 79, 80, 81, 82 |
| TC-AC-LCS-E2E-025-role-matrix-positif-manage-plans-lifecycle-recycle | Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Client Lifecycle dan Recycle Bin | FE+BE | 20 | 83, 84, 85, 86 |
| TC-AC-LCS-E2E-026-role-matrix-positif-manage-plans-approval-limits | Role Matrix Positif: Manage Plans & Licensing Mengeksekusi Save dan Reset Tab Approval Settings dan System Limits | FE+BE | 20 | 87, 88, 89, 90 |
| TC-AC-LCS-E2E-027-role-matrix-positif-default-user-free-plan | Role Matrix Positif: Default User Mengeksekusi Save dan Reset Tab Free Plan Settings | FE+BE | 9 | 91, 92 |
| TC-AC-LCS-E2E-028-capability-dicabut-saat-form-terbuka | Capability Update Dicabut Saat Form Terbuka: Save Trial Settings dan Reset Recycle Bin Ditolak | FE+BE | 24 | 93, 94 |
| TC-AC-LCS-E2E-029-validasi-field-max-trial-duration | Validasi Field Max Trial Duration | FE+BE | 29 | 95, 96, 97, 98, 99 |
| TC-AC-LCS-E2E-030-validasi-field-max-trial-asset-quota | Validasi Field Max Trial Asset Quota | FE+BE | 29 | 100, 101, 102, 103, 104 |
| TC-AC-LCS-E2E-031-validasi-field-max-trial-concurrent-user-quota | Validasi Field Max Trial Concurrent User Quota | FE+BE | 29 | 105, 106, 107, 108, 109 |
| TC-AC-LCS-E2E-032-validasi-field-first-notification | Validasi Field First Notification | FE+BE | 32 | 110, 111, 112, 113, 114 |
| TC-AC-LCS-E2E-033-validasi-field-second-notification | Validasi Field Second Notification | FE+BE | 22 | 115, 116, 117, 118 |
| TC-AC-LCS-E2E-034-trial-dirty-state-save-seluruh-field | Tab Trial Settings: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah | FE+BE | 33 | 119, 120, 128 |
| TC-AC-LCS-E2E-035-trial-save-minimum-dan-switch-require-approval | Tab Trial Settings: Save Nilai Minimum dan Switch Require Approval for Trial Activation | FE+BE | 29 | 121, 292, 293, 294 |
| TC-AC-LCS-E2E-036-trial-reset-dan-klik-ganda | Tab Trial Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 33 | 123, 124, 126, 127 |
| TC-AC-LCS-E2E-037-trial-validasi-relasi-notification | Tab Trial Settings: Validasi Relasi First Notification dan Second Notification | FE+BE | 21 | 295, 296, 297, 298 |
| TC-AC-LCS-E2E-038-input-angka-tempel-dan-normalisasi | Input Angka: Tempel Teks Campuran, Normalisasi Awalan Nol, dan Batas Karakter Hard Cap | FE+BE | 17 | 673, 674, 685 |
| TC-AC-LCS-E2E-039-validasi-field-free-plan-duration | Validasi Field Free Plan Duration | FE+BE | 30 | 129, 130, 131, 132, 133 |
| TC-AC-LCS-E2E-040-free-plan-dirty-state-save-dan-koreksi | Tab Free Plan Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah | FE+BE | 30 | 134, 135, 136, 143 |
| TC-AC-LCS-E2E-041-free-plan-reset-dan-klik-ganda | Tab Free Plan Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 138, 139, 141, 142 |
| TC-AC-LCS-E2E-042-validasi-field-managed-transition-time | Validasi Field Managed Transition Time | FE+BE | 28 | 144, 145, 146, 147, 148 |
| TC-AC-LCS-E2E-043-validasi-field-managed-action-retry-delay | Validasi Field Managed Action Retry Delay | FE+BE | 28 | 149, 150, 151, 152, 153 |
| TC-AC-LCS-E2E-044-validasi-field-addon-reactivation-delay | Validasi Field Addon Reactivation Delay | FE+BE | 28 | 154, 155, 156, 157, 158 |
| TC-AC-LCS-E2E-045-license-timing-dirty-state-save-dan-koreksi | Tab License Timing: Dirty State, Save Seluruh Field, dan Koreksi Nilai Salah | FE+BE | 28 | 159, 160, 168 |
| TC-AC-LCS-E2E-046-license-timing-reset-dan-klik-ganda | Tab License Timing: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 163, 164, 166, 167 |
| TC-AC-LCS-E2E-047-validasi-field-notify-plan-owner-before-event | Validasi Field Notify Plan Owner Before Event | FE+BE | 28 | 169, 170, 171, 172, 173 |
| TC-AC-LCS-E2E-048-validasi-field-first-reminder-before-event | Validasi Field First Reminder Before Event | FE+BE | 30 | 174, 175, 176, 177, 178 |
| TC-AC-LCS-E2E-049-validasi-field-second-reminder-before-event | Validasi Field Second Reminder Before Event | FE+BE | 24 | 179, 180, 181, 182 |
| TC-AC-LCS-E2E-050-validasi-field-final-reminder-before-event | Validasi Field Final Reminder Before Event | FE+BE | 22 | 183, 184, 185, 186 |
| TC-AC-LCS-E2E-051-validasi-field-grace-period-duration | Validasi Field Grace Period Duration | FE+BE | 28 | 187, 188, 189, 190, 191 |
| TC-AC-LCS-E2E-052-validasi-field-archive-period-duration | Validasi Field Archive Period Duration | FE+BE | 31 | 192, 193, 194, 195, 196 |
| TC-AC-LCS-E2E-053-validasi-field-purge-warning-email | Validasi Field Purge Warning Email | FE+BE | 31 | 197, 198, 199, 200, 201 |
| TC-AC-LCS-E2E-054-validasi-field-purge-urgent-warning-email | Validasi Field Purge Urgent Warning Email | FE+BE | 22 | 202, 203, 204, 205 |
| TC-AC-LCS-E2E-055-validasi-field-post-purge-retention | Validasi Field Post-Purge Retention: Non-numerik, Kosong, Di Bawah Minimum, dan Batas Karakter | FE+BE | 23 | 206, 207, 208, 209 |
| TC-AC-LCS-E2E-056-post-purge-retention-batas-atas-3650 | Post-Purge Retention: Batas Atas 3650 Ditolak di Atas dan Diterima pada Maksimum | FE+BE | 22 | 210, 211, 314, 327 |
| TC-AC-LCS-E2E-057-client-lifecycle-dirty-state-save-seluruh-field | Tab Client Lifecycle: Dirty State dan Save Seluruh Sembilan Field | FE+BE | 32 | 212, 213 |
| TC-AC-LCS-E2E-058-client-lifecycle-save-minimum-dan-koreksi | Tab Client Lifecycle: Save Nilai Minimum dan Koreksi Nilai Salah | FE+BE | 23 | 214, 221 |
| TC-AC-LCS-E2E-059-client-lifecycle-reset-dan-klik-ganda | Tab Client Lifecycle: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 216, 217, 219, 220 |
| TC-AC-LCS-E2E-060-client-lifecycle-validasi-relasi-reminder | Tab Client Lifecycle: Validasi Relasi Reminder First, Second, dan Final | FE+BE | 33 | 300, 301, 302, 303, 304, 305 |
| TC-AC-LCS-E2E-061-client-lifecycle-validasi-relasi-purge-warning | Tab Client Lifecycle: Validasi Relasi Purge Warning Email dan Purge Urgent Warning Email | FE+BE | 27 | 306, 307, 308, 346 |
| TC-AC-LCS-E2E-062-client-lifecycle-validasi-relasi-archive-period | Tab Client Lifecycle: Validasi Relasi Archive Period Duration terhadap Purge Warning Email dan Purge Urgent Warning Email | FE+BE | 22 | 309, 310, 311, 312 |
| TC-AC-LCS-E2E-063-field-tanpa-validasi-relasi | Field Tanpa Validasi Relasi: Max Trial dan Notify Plan Owner Before Event | FE+BE | 18 | 299, 313 |
| TC-AC-LCS-E2E-064-warning-note-client-lifecycle-notify-sampai-final | Warning Note Client Lifecycle: Notify Plan Owner sampai Final Reminder Before Event | FE+BE | 17 | 315, 316, 317, 318 |
| TC-AC-LCS-E2E-065-warning-note-client-lifecycle-grace-sampai-purge-urgent | Warning Note Client Lifecycle: Grace Period, Archive Period, Purge Warning, dan Purge Urgent Warning | FE+BE | 17 | 319, 320, 321, 322 |
| TC-AC-LCS-E2E-066-warning-note-client-lifecycle-hilang-dan-tidak-tampil | Warning Note Client Lifecycle: Post-Purge Retention, Nilai Dikembalikan, Save, Muat, dan Reset | FE+BE | 22 | 323, 324, 325, 326 |
| TC-AC-LCS-E2E-067-validasi-field-permanently-delete-recycle-bin | Validasi Field Permanently Delete Recycle Bin | FE+BE | 27 | 222, 223, 224, 225, 226 |
| TC-AC-LCS-E2E-068-recycle-bin-dirty-state-save-dan-koreksi | Tab Recycle Bin: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah | FE+BE | 28 | 227, 228, 229, 236 |
| TC-AC-LCS-E2E-069-recycle-bin-reset-dan-klik-ganda | Tab Recycle Bin: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 231, 232, 234, 235 |
| TC-AC-LCS-E2E-070-warning-note-recycle-bin | Warning Note Recycle Bin: Muncul, Bertahan Saat Save Gagal, dan Hilang Setelah Save atau Reset | FE+BE | 22 | 328, 329, 330 |
| TC-AC-LCS-E2E-071-warning-note-tab-tanpa-warning | Warning Note: Tab Tanpa Warning (Trial Settings, Free Plan, License Timing, Approval Settings, System Limits) | FE+BE | 29 | 331, 332, 333, 334, 335 |
| TC-AC-LCS-E2E-072-validasi-field-approval-timeout | Validasi Field Approval Timeout | FE+BE | 28 | 237, 238, 239, 240, 241 |
| TC-AC-LCS-E2E-073-approval-settings-dirty-state-save-dan-koreksi | Tab Approval Settings: Dirty State, Save Seluruh Field, Nilai Minimum, dan Koreksi Nilai Salah | FE+BE | 28 | 242, 243, 244, 251 |
| TC-AC-LCS-E2E-074-approval-settings-reset-dan-klik-ganda | Tab Approval Settings: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 246, 247, 249, 250 |
| TC-AC-LCS-E2E-075-validasi-field-bulk-transaction-row-limit | Validasi Field Bulk Transaction Row Limit | FE+BE | 28 | 252, 253, 254, 255, 256 |
| TC-AC-LCS-E2E-076-validasi-field-selection-limit | Validasi Field Selection Limit | FE+BE | 28 | 257, 258, 259, 260, 261 |
| TC-AC-LCS-E2E-077-validasi-field-register-asset-bulk-limit | Validasi Field Register Asset Bulk Limit | FE+BE | 28 | 262, 263, 264, 265, 266 |
| TC-AC-LCS-E2E-078-validasi-field-hierarchy-depth-limit | Validasi Field Hierarchy Depth Limit | FE+BE | 28 | 267, 268, 269, 270, 271 |
| TC-AC-LCS-E2E-079-validasi-field-master-data-count-limit | Validasi Field Master Data Count Limit | FE+BE | 28 | 272, 273, 274, 275, 276 |
| TC-AC-LCS-E2E-080-validasi-field-max-visible-columns | Validasi Field Max Visible Columns | FE+BE | 28 | 277, 278, 279, 280, 281 |
| TC-AC-LCS-E2E-081-system-limits-dirty-state-save-seluruh-field | Tab System Limits: Dirty State dan Save Seluruh Enam Field | FE+BE | 26 | 282, 283 |
| TC-AC-LCS-E2E-082-system-limits-save-minimum-dan-koreksi | Tab System Limits: Save Nilai Minimum dan Koreksi Nilai Salah | FE+BE | 23 | 284, 291 |
| TC-AC-LCS-E2E-083-system-limits-reset-dan-klik-ganda | Tab System Limits: Reset to Default dan Klik Ganda Cepat pada Save serta Reset | FE+BE | 34 | 286, 287, 289, 290 |
| TC-AC-LCS-E2E-084-resilience-save-500-trial-dan-free-plan | Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab Trial Settings dan Free Plan Settings | FE+BE | 18 | 122, 137 |
| TC-AC-LCS-E2E-085-resilience-save-500-recycle-approval-limits | Resilience Save 500 pada Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 28 | 230, 245, 285 |
| TC-AC-LCS-E2E-086-resilience-reset-500-trial-sampai-client-lifecycle | Resilience Reset to Default 500 pada Tab Trial, Free Plan, License Timing, dan Client Lifecycle | FE+BE | 29 | 125, 140, 165, 218 |
| TC-AC-LCS-E2E-087-resilience-reset-500-recycle-approval-limits | Resilience Reset to Default 500 pada Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 22 | 233, 248, 288 |
| TC-AC-LCS-E2E-088-resilience-save-gagal-dan-timeout | Resilience Save: Respons Gagal Mengembalikan Field Enabled, dan Timeout pada Save serta Reset Trial Settings | FE+BE | 29 | 349, 353, 354 |
| TC-AC-LCS-E2E-089-unsaved-changes-dialog-sidebar-dan-state-bersih | Dialog Unsaved Changes: Menu Sidebar, Tab Lain Dirty, Tanpa Perubahan, Nilai Dikembalikan, dan Setelah Save | FE+BE | 34 | 336, 337, 338, 339, 340 |
| TC-AC-LCS-E2E-090-unsaved-changes-back-backdrop-dan-refresh | Proteksi Keluar Halaman: Tombol Back Browser, Backdrop Dialog, dan Konfirmasi Bawaan Browser pada Refresh F5 | FE+BE | 26 | 341, 342, 343, 344, 345 |
| TC-AC-LCS-E2E-091-state-in-flight-save-dan-reset | State In-Flight Save dan Reset: Field, Switch, Save, dan Reset Disabled Selama Permintaan Berjalan | FE+BE | 23 | 347, 348 |
| TC-AC-LCS-E2E-092-independensi-antar-tab-save-in-flight-dan-save-berhasil | Independensi Antar Tab: Save In-Flight dan Save Berhasil Tidak Memengaruhi Tab Lain | FE+BE | 27 | 350, 351 |
| TC-AC-LCS-E2E-093-screening-modal-changelog-trial-free-license | Screening Modal Changelog Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 15 | 355, 357, 359 |
| TC-AC-LCS-E2E-094-screening-modal-changelog-lifecycle-recycle-approval-limits | Screening Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits | FE+BE | 15 | 361, 363, 365, 367 |
| TC-AC-LCS-E2E-095-empty-state-modal-changelog-trial-free-license | Empty State Modal Changelog Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 6 | 356, 358, 360 |
| TC-AC-LCS-E2E-096-empty-state-modal-changelog-lifecycle-recycle-approval-limits | Empty State Modal Changelog Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits | FE+BE | 6 | 362, 364, 366, 368 |
| TC-AC-LCS-E2E-097-modal-changelog-isolasi-penutupan-dan-icon | Modal Changelog: Isolasi Riwayat per Tab, Penutupan Modal, dan Icon Changelog Membuka Tab Aktif | FE+BE | 30 | 369, 370, 371 |
| TC-AC-LCS-E2E-098-search-modal-changelog-reveal-dan-siklus | Search Modal Changelog: Reveal Search Box, Siklus Interaksi, dan Panah Penutup | FE+BE | 23 | 372, 373, 374 |
| TC-AC-LCS-E2E-099-search-modal-changelog-pencocokan-per-kolom | Search Modal Changelog: Pencocokan per Kolom Action, Field, Old Value, New Value, Modified By, dan Kolom Date | FE+BE | 24 | 375, 376, 377, 378, 379, 380 |
| TC-AC-LCS-E2E-100-search-modal-changelog-normalisasi-literal-dan-hide | Search Modal Changelog: Case Insensitive, Spasi, Karakter Khusus, Tanpa Hasil, dan Kolom Tersembunyi | FE+BE | 25 | 381, 382, 383, 384, 385 |
| TC-AC-LCS-E2E-101-modal-changelog-search-filter-trial-dan-free | Modal Changelog Tab Trial Settings dan Free Plan Settings: Search dan Filter pada Dataset Kecil | FE+BE | 27 | 658, 659, 660, 661, 662 |
| TC-AC-LCS-E2E-102-modal-changelog-search-filter-license-dan-recycle | Modal Changelog Tab License Timing dan Recycle Bin: Search dan Filter pada Dataset Kecil | FE+BE | 28 | 663, 664, 665, 666, 667 |
| TC-AC-LCS-E2E-103-modal-changelog-search-filter-approval-dan-limits | Modal Changelog Tab Approval Settings dan System Limits: Search dan Filter pada Dataset Kecil | FE+BE | 28 | 668, 669, 670, 671, 672 |
| TC-AC-LCS-E2E-104-filter-modal-changelog-screening-dan-opsi | Filter Panel Modal Changelog: Screening, Opsi Dropdown Field dan Modified By, serta Search dalam Dropdown | FE+BE | 24 | 386, 387, 388, 389 |
| TC-AC-LCS-E2E-105-filter-modal-changelog-field-modified-by-date | Filter Modal Changelog: Field, Modified By, Rentang Date, dan Satu Hari | FE+BE | 28 | 390, 391, 392, 393, 394 |
| TC-AC-LCS-E2E-106-filter-modal-changelog-kombinasi-clear-dan-tutup | Filter Modal Changelog: Kombinasi AND, Tanpa Hasil, Clear Field, dan Tutup Tanpa Apply | FE+BE | 25 | 395, 396, 397, 398 |
| TC-AC-LCS-E2E-107-sort-modal-changelog-default-date-field-action | Sort Modal Changelog: Urutan Default, Siklus Tiga Klik Date, Field, dan Action | FE+BE | 24 | 399, 400, 401, 402 |
| TC-AC-LCS-E2E-108-sort-modal-changelog-nilai-modified-by-dan-perpindahan | Sort Modal Changelog: Old Value, New Value, Modified By, dan Perpindahan Kolom Sort | FE+BE | 24 | 403, 404, 405, 406 |
| TC-AC-LCS-E2E-109-column-visibility-modal-changelog | Column Visibility Modal Changelog: Screening Overlay, Perubahan Langsung, dan Guard Kolom Terakhir | FE+BE | 26 | 407, 408, 409 |
| TC-AC-LCS-E2E-110-setup-column-modal-changelog | Setup Column Modal Changelog: Popup, Preview, Save, Tutup, Reset to Default, dan Cache per Tab | FE+BE | 42 | 410, 411, 412, 413, 414 |
| TC-AC-LCS-E2E-111-pagination-modal-changelog-default-dan-navigasi | Pagination Modal Changelog: Ukuran Halaman Default, Navigasi, dan Penggantian Page Size | FE+BE | 28 | 432, 433, 434 |
| TC-AC-LCS-E2E-112-pagination-modal-changelog-reset-halaman-dan-kombinasi | Pagination Modal Changelog: Reset Halaman oleh Search dan Filter, Sort, dan Kombinasi Kontrol | FE+BE | 26 | 435, 436, 437 |
| TC-AC-LCS-E2E-113-download-changelog-screening-dan-csv-trial-free-license | Download Changelog: Screening Overlay dan CSV Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 16 | 415, 416, 417, 418 |
| TC-AC-LCS-E2E-114-download-changelog-csv-client-lifecycle-recycle-approval-limits | Download Changelog CSV Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits | FE+BE | 8 | 419, 420, 421, 422 |
| TC-AC-LCS-E2E-115-download-changelog-xlsx-dan-mengikuti-search-dan-kolom-visible | Download Changelog XLSX dan Download Mengikuti Search serta Kolom Visible | FE+BE | 21 | 423, 424 |
| TC-AC-LCS-E2E-116-download-changelog-di-atas-5000-baris | Download Changelog di Atas 5.000 Baris: Loading Screen lalu Langsung Terunduh | FE+BE | 10 | 684 |
| TC-AC-LCS-E2E-117-resilience-download-gagal-trial-sampai-client-lifecycle | Resilience Download Changelog Gagal: Toast Error Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle | FE+BE | 10 | 425, 426, 427, 428 |
| TC-AC-LCS-E2E-118-resilience-download-gagal-recycle-approval-limits | Resilience Download Changelog Gagal: Toast Error Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 10 | 429, 430, 431 |
| TC-AC-LCS-E2E-119-changelog-client-lifecycle-sembilan-entri | Isi Entri Changelog Client Lifecycle: Save Sembilan Field Mencatat Sembilan Entri | FE+BE | 28 | 469 |
| TC-AC-LCS-E2E-120-changelog-multi-field-trial-dan-free | Isi Entri Changelog: Save Enam Field Trial Settings dan Satu Field Free Plan Settings | FE+BE | 34 | 466, 467 |
| TC-AC-LCS-E2E-121-changelog-multi-field-license-recycle-approval | Isi Entri Changelog: Save Tiga Field License Timing, Satu Field Recycle Bin, dan Satu Field Approval Settings | FE+BE | 30 | 468, 470, 471 |
| TC-AC-LCS-E2E-122-changelog-multi-field-system-limits-dan-parsial-trial | Isi Entri Changelog: Save Enam Field System Limits dan Dua dari Enam Field Trial Settings | FE+BE | 35 | 472, 473 |
| TC-AC-LCS-E2E-123-changelog-parsial-berulang-dan-modified-by | Isi Entri Changelog: Save Parsial Client Lifecycle, Save Berulang pada Field Sama, dan Format Modified By | FE+BE | 38 | 474, 475, 476 |
| TC-AC-LCS-E2E-124-changelog-isi-entri-trial-field-1-sampai-4 | Isi Entri Changelog per Field Tab Trial Settings: Max Trial Duration, Max Trial Asset Quota, Concurrent User Quota, dan First Notification | FE+BE | 13 | 439, 440, 441, 442 |
| TC-AC-LCS-E2E-125-changelog-isi-entri-second-notification-free-dan-switch | Isi Entri Changelog: Second Notification, Free Plan Duration, dan Switch Require Approval | FE+BE | 26 | 443, 444, 465 |
| TC-AC-LCS-E2E-126-changelog-isi-entri-license-timing | Isi Entri Changelog per Field Tab License Timing | FE+BE | 29 | 445, 446, 447 |
| TC-AC-LCS-E2E-127-changelog-isi-entri-client-lifecycle-notify-sampai-grace | Isi Entri Changelog per Field Tab Client Lifecycle: Notify Plan Owner sampai Final Reminder | FE+BE | 39 | 448, 449, 450, 451 |
| TC-AC-LCS-E2E-128-changelog-isi-entri-client-lifecycle-grace-sampai-purge-urgent | Isi Entri Changelog per Field Tab Client Lifecycle: Grace Period Duration sampai Purge Urgent Warning Email | FE+BE | 39 | 452, 453, 454, 455 |
| TC-AC-LCS-E2E-129-changelog-isi-entri-post-purge-recycle-approval | Isi Entri Changelog: Post-Purge Retention, Permanently Delete Recycle Bin, dan Approval Timeout | FE+BE | 29 | 456, 457, 458 |
| TC-AC-LCS-E2E-130-changelog-isi-entri-system-limits-bulk-sampai-hierarchy | Isi Entri Changelog per Field Tab System Limits: Bulk Transaction Row Limit sampai Hierarchy Depth Limit | FE+BE | 39 | 459, 460, 461, 462 |
| TC-AC-LCS-E2E-131-changelog-isi-entri-master-data-dan-max-visible-columns | Isi Entri Changelog: Master Data Count Limit dan Max Visible Columns | FE+BE | 17 | 463, 464 |
| TC-AC-LCS-E2E-132-log-save-trial-free-license | Pencatatan Log: Save Tab Trial Settings, Free Plan Settings, dan License Timing Menulis Entri di System Log dan Activity Log | FE+BE | 31 | 478, 479, 480 |
| TC-AC-LCS-E2E-133-log-save-lifecycle-recycle-approval-limits | Pencatatan Log: Save Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Menulis Entri di System Log dan Activity Log | FE+BE | 43 | 481, 482, 483, 484 |
| TC-AC-LCS-E2E-134-log-reset-trial-sampai-client-lifecycle | Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle | FE+BE | 50 | 485, 486, 487, 488 |
| TC-AC-LCS-E2E-135-log-reset-recycle-approval-limits | Pencatatan Log Reset to Default: Edit per Field pada Tiga Surface Log Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 38 | 489, 490, 491 |
| TC-AC-LCS-E2E-136-format-tanggal-dan-waktu-general-settings | Format Tanggal dan Waktu General Settings pada Kolom Date Modal Changelog, System Log, dan Activity Log | FE+BE | 33 | 492, 493, 494, 495, 496, 497 |
| TC-AC-LCS-E2E-137-absence-changelog-penolakan-read-only | Absence Log: Penolakan Server Read Only pada Save Setiap Tab Tidak Menambah Entri Changelog | FE+BE | 41 | 586, 588, 590, 592, 594, 596, 598 |
| TC-AC-LCS-E2E-138-absence-changelog-penolakan-rentang-trial-free-license | Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Trial, Free Plan, dan License Timing Tidak Menambah Entri Changelog | FE+BE | 32 | 610, 611, 614, 615, 618, 619 |
| TC-AC-LCS-E2E-139-absence-changelog-penolakan-rentang-lifecycle-recycle-approval-limits | Absence Log: Penolakan Server atas Nilai di Atas dan di Bawah Rentang Tab Client Lifecycle, Recycle Bin, Approval Settings, dan System Limits Tidak Menambah Entri Changelog | FE+BE | 43 | 622, 623, 626, 627, 630, 631, 634, 635 |
| TC-AC-LCS-E2E-140-absence-log-reset-default-dan-penulisan-log-gagal | Absence Log: Reset to Default Saat Seluruh Field Default dan Kegagalan Penulisan Log Tidak Menulis Entri | FE+BE | 22 | 477, 686 |
| TC-AC-LCS-E2E-141-konsumen-free-plan-duration | Konsumen Free Plan Duration: Perubahan Memengaruhi Subscription Free Baru dan Tidak Mengubah yang Sudah Ada | FE+BE | 8 | 498 |
| TC-AC-LCS-E2E-142-konsumen-trial-ceiling-form-activate-trial | Konsumen Trial: Ceiling Max Trial Duration, Asset Quota, dan Concurrent User Quota pada Form Activate Trial | FE+BE | 56 | 499, 500, 501 |
| TC-AC-LCS-E2E-143-konsumen-trial-require-approval | Konsumen Trial: Switch Require Approval for Trial Activation pada Aktivasi Trial Distributor dan Principal | FE+BE | 37 | 502, 503, 504, 505 |
| TC-AC-LCS-E2E-144-konsumen-trial-jadwal-pengingat | Konsumen Trial: Perubahan First Notification dan Second Notification Mengubah Jadwal Pengingat | FE+BE | 22 | 506, 507 |
| TC-AC-LCS-E2E-145-approval-adopter-timeout-dan-recalculation | Approval Settings Konsumen: Timeout Auto-Cancel, Recalculation Batas, dan Warning H-24 pada Device Allocation | FE+BE | 56 | 508, 509, 510, 511 |
| TC-AC-LCS-E2E-146-approval-adopter-warning-ulang-dan-status-final | Approval Settings Konsumen: Pengiriman Ulang Warning, Recalculation Berurutan, Reset, Progress Approver AND, dan Pengajuan Trial Activation | FE+BE | 67 | 512, 513, 514, 515, 516, 517 |
| TC-AC-LCS-E2E-147-approval-adopter-race-pembatalan-dan-job | Approval Settings Konsumen: Pembatalan Manual Bersamaan dengan Job Timeout | FE+BE | 13 | 518 |
| TC-AC-LCS-E2E-148-timer-client-lifecycle-grace-diperpendek | Recalculation Timer Client Lifecycle: Grace Period Duration Diperpendek dan Batas Hari ke-14 dan ke-15 | FE+BE | 45 | 519, 520, 521, 522, 523 |
| TC-AC-LCS-E2E-149-timer-client-lifecycle-save-reset-dan-job-gagal | Recalculation Timer Client Lifecycle: Save Post-Purge Saja, Reset, Save Berurutan, dan Job Per-Save Gagal | FE+BE | 51 | 524, 525, 526, 527 |
| TC-AC-LCS-E2E-150-post-purge-retention-company-archive-dan-hard-purge | Post-Purge Retention: Company dalam Archive Tidak Terpengaruh dan Hard Purge Memakai Retention Baru | FE+BE | 25 | 528, 529 |
| TC-AC-LCS-E2E-151-banner-pengingat-perpanjangan-severity | Banner Pengingat Perpanjangan: First Reminder, Severity pada Second dan Final Reminder Before Event | FE+BE | 31 | 530, 531, 532 |
| TC-AC-LCS-E2E-152-email-trigger-reminder-dan-grace-period-end | Email Trigger Engine: First Reminder, Second Reminder, Final Reminder, dan Grace Period End | FE+BE | 32 | 533, 534, 535, 536 |
| TC-AC-LCS-E2E-153-email-trigger-purge-warning-urgent-dan-confirmation | Email Trigger Engine: Purge Warning, Purge Urgent Warning, dan Purge Confirmation | FE+BE | 24 | 537, 538, 539 |
| TC-AC-LCS-E2E-154-notifikasi-plan-owner-penerima-dan-deduplikasi | Notifikasi Plan Owner dalam Aplikasi: Penerima per Level, Deduplikasi, dan Client Direct | FE+BE | 42 | 540, 541, 542 |
| TC-AC-LCS-E2E-155-email-engine-kegagalan-layanan-dan-job | Email Trigger Engine: Email Service Gagal dan Kegagalan Cold Storage pada Transisi Grace ke Archive | FE+BE | 27 | 546, 676 |
| TC-AC-LCS-E2E-156-email-engine-job-terlambat-dan-tahapan-dilewati | Email Trigger Engine: Job Terlambat, Konfigurasi Berubah, Tahapan Sebelum Pembuatan Subscription, dan Eksekusi Terlewat | FE+BE | 27 | 547, 548, 549, 550, 678 |
| TC-AC-LCS-E2E-157-state-machine-downgrade-dan-notifikasi-kedaluwarsa | Scheduled Downgrade dan Transisi Active ke Expired pada T-0: Pengingat, Notifikasi Kedaluwarsa, Downgrade, dan Daftar Penerima Kosong | FE+BE | 43 | 551, 552, 553, 554, 555 |
| TC-AC-LCS-E2E-158-state-machine-perpanjangan-renew-dan-downgrade-paralel | State Machine Lifecycle: Perpanjangan Membatalkan Lifecycle, Renew, Downgrade Paralel, dan Tanpa Aksi Renew pada Archive | FE+BE | 42 | 556, 557, 558, 559, 560, 687 |
| TC-AC-LCS-E2E-159-post-purge-archive-indeks-dan-pencocokan | Post-Purge Archive Matching: Indeks Arsip, Pencocokan Email Client Baru, dan Masa Retensi | FE+BE | 46 | 561, 562, 563, 564, 565 |
| TC-AC-LCS-E2E-160-post-purge-archive-notifikasi-dan-visibilitas | Post-Purge Archive Matching: Principal Berizin, Notifikasi Gagal, Visibilitas Penanda, True Hard Delete, dan Principal di Luar Rantai Group | FE+BE | 45 | 566, 567, 568, 569, 681 |
| TC-AC-LCS-E2E-161-landing-page-subscription-expired-archive | Landing Page Subscription Expired untuk Client yang Login pada Archive Period | FE+BE | 8 | 570 |
| TC-AC-LCS-E2E-162-jalur-cancel-subscription-archive-notice-dan-purge | Jalur Cancel Subscription: Archive Notice, Pelacak Purge Warning, dan Email Purge Confirmation ke Penerima Tersimpan | FE+BE | 26 | 680, 682, 683 |
| TC-AC-LCS-E2E-163-recycle-bin-countdown-reset-job-durasi | Countdown Reset Job Recycle Bin: Durasi Diperpendek, Diperpanjang, dan Reset to Default dari Nilai 60 | FE+BE | 24 | 571, 572, 573 |
| TC-AC-LCS-E2E-164-recycle-bin-countdown-reset-job-ketahanan | Countdown Reset Job Recycle Bin: Reset pada Nilai 30, Respons Save Tanpa Menunggu Job, dan Schema Client Terhapus | FE+BE | 29 | 574, 575, 576 |
| TC-AC-LCS-E2E-165-konsumen-hierarchy-depth-limit-add-subgroup | Konsumen Hierarchy Depth Limit pada Add Subgroup Settings Group | FE+BE | 29 | 579, 580, 581 |
| TC-AC-LCS-E2E-166-konsumen-selection-limit-seleksi-dan-select-all | Konsumen Selection Limit: Seleksi Manual, Select All pada 150 Baris, dan Pembacaan Live | FE+BE | 25 | 582, 583, 584 |
| TC-AC-LCS-E2E-167-bypass-selection-limit-bulk-delete-ditolak-server | Bypass Guard UI Selection Limit: Bulk Delete 101 Baris Ditolak Server | FE+BE | 7 | 585 |
| TC-AC-LCS-E2E-168-otorisasi-server-read-only-trial-free-license | Otorisasi Server: Read Only Save dan Reset Tab Trial Settings, Free Plan Settings, dan License Timing Ditolak | FE+BE | 29 | 586, 587, 588, 589, 590, 591 |
| TC-AC-LCS-E2E-169-otorisasi-server-read-only-lifecycle-recycle-approval | Otorisasi Server: Read Only Save dan Reset Tab Client Lifecycle, Recycle Bin, dan Approval Settings Ditolak | FE+BE | 29 | 592, 593, 594, 595, 596, 597 |
| TC-AC-LCS-E2E-170-otorisasi-server-read-only-system-limits-dan-tanpa-capability | Otorisasi Server: Read Only Save dan Reset System Limits serta Principal Tanpa Capability Baca dan Save Ditolak | FE+BE | 17 | 598, 599, 609 |
| TC-AC-LCS-E2E-171-otorisasi-server-entity-baca-dan-save-trial | Otorisasi Server: Baca dan Save Trial Settings oleh Distributor, Partner, dan Client Ditolak | FE+BE | 21 | 600, 601, 603, 604, 606, 607 |
| TC-AC-LCS-E2E-172-otorisasi-server-entity-reset-trial | Otorisasi Server: Reset to Default Trial Settings oleh Distributor, Partner, dan Client Ditolak | FE+BE | 13 | 602, 605, 608 |
| TC-AC-LCS-E2E-173-validasi-server-trial-settings | Validasi Server-Side Trial Settings: Max Trial Duration dan Relasi Notification | FE+BE | 20 | 610, 611, 612, 613, 638 |
| TC-AC-LCS-E2E-174-validasi-server-free-plan-settings | Validasi Server-Side Free Plan Settings: Free Plan Duration | FE+BE | 16 | 614, 615, 616, 617 |
| TC-AC-LCS-E2E-175-validasi-server-license-timing | Validasi Server-Side License Timing: Managed Transition Time | FE+BE | 16 | 618, 619, 620, 621 |
| TC-AC-LCS-E2E-176-validasi-server-client-lifecycle-notify | Validasi Server-Side Client Lifecycle: Notify Plan Owner Before Event | FE+BE | 16 | 622, 623, 624, 625 |
| TC-AC-LCS-E2E-177-validasi-server-client-lifecycle-relasi | Validasi Server-Side Client Lifecycle: Relasi Reminder, Purge Warning, dan Archive Period | FE+BE | 20 | 639, 640, 641, 642, 643 |
| TC-AC-LCS-E2E-178-validasi-server-recycle-bin | Validasi Server-Side Recycle Bin: Permanently Delete Recycle Bin | FE+BE | 16 | 626, 627, 628, 629 |
| TC-AC-LCS-E2E-179-validasi-server-approval-settings | Validasi Server-Side Approval Settings: Approval Timeout | FE+BE | 16 | 630, 631, 632, 633 |
| TC-AC-LCS-E2E-180-validasi-server-system-limits | Validasi Server-Side System Limits: Bulk Transaction Row Limit | FE+BE | 16 | 634, 635, 636, 637 |
| TC-AC-LCS-E2E-181-save-no-op-trial-free-license-client-lifecycle | Save Identik No-Op Lewat Permintaan Langsung: Tab Trial Settings, Free Plan Settings, License Timing, dan Client Lifecycle | FE+BE | 32 | 644, 645, 646, 647 |
| TC-AC-LCS-E2E-182-save-no-op-recycle-approval-limits | Save Identik No-Op Lewat Permintaan Langsung: Tab Recycle Bin, Approval Settings, dan System Limits | FE+BE | 24 | 648, 649, 650 |
| TC-AC-LCS-E2E-183-konkurensi-dua-admin-trial-free-plan-dan-license-timing | Konkurensi Dua Admin: Save Bersamaan Tab Trial Settings, Free Plan Settings, dan License Timing | FE+BE | 34 | 651, 652, 653 |
| TC-AC-LCS-E2E-184-konkurensi-dua-admin-client-lifecycle-recycle-dan-approval | Konkurensi Dua Admin: Save Bersamaan Tab Client Lifecycle, Recycle Bin, dan Approval Settings | FE+BE | 35 | 654, 655, 656 |
| TC-AC-LCS-E2E-185-screening-tab-approval-limits | Screening Tab Approval Settings dan System Limits | FE+BE | 23 | 6, 7 |
| TC-AC-LCS-E2E-186-tooltip-label-field-client-lifecycle | Tooltip Label Field Tab Client Lifecycle | FE+BE | 19 | 43 |
| TC-AC-LCS-E2E-187-license-timing-save-nilai-minimum | Tab License Timing: Save Nilai Minimum | FE+BE | 9 | 161 |
| TC-AC-LCS-E2E-189-resilience-save-500-license-timing-dan-client-lifecycle | Resilience Save 500: Toast Error, Form Tetap, dan Data Tidak Berubah pada Tab License Timing dan Client Lifecycle | FE+BE | 19 | 162, 215 |
| TC-AC-LCS-E2E-191-independensi-antar-tab-reset-tidak-menyentuh-tab-lain | Independensi Antar Tab: Reset to Default Tab Free Plan Settings Tidak Menyentuh Tab Trial Settings | FE+BE | 15 | 352 |
| TC-AC-LCS-E2E-192-changelog-client-lifecycle-entri-terbaru-di-atas | Isi Entri Changelog Client Lifecycle: Entri Terbaru di Atas Setelah Save Baru pada Dataset L | FE+BE | 10 | 438 |
| TC-AC-LCS-E2E-193-notifikasi-plan-owner-level-tanpa-pengguna-dan-daftar-kosong | Notifikasi Plan Owner dalam Aplikasi: Level Tanpa Pengguna Berizin dan Daftar Penerima Kosong | FE+BE | 25 | 543, 544, 545 |
| TC-AC-LCS-E2E-194-email-engine-hard-purge-gagal-dan-email-tetap-gagal | Email Trigger Engine: Hard Purge Gagal dan Email Service Tetap Tidak Terjangkau Setelah Percobaan Habis | FE+BE | 26 | 677, 679 |
| TC-AC-LCS-E2E-195-konkurensi-dua-admin-system-limits-dan-save-identik | Konkurensi Dua Admin: Save Bersamaan Tab System Limits dan Save Identik Akibat Save Admin Lain | FE+BE | 22 | 657, 675 |
| TC-AC-LCS-E2E-196-recycle-bin-countdown-reset-job-sweep-dan-item-terhapus | Countdown Reset Job Recycle Bin: Job Per-Save Gagal dengan Daily Sweep dan Item Terhapus Permanen | FE+BE | 20 | 577, 578 |

## Pembagian TC lintas spec: asersi absence Changelog (S-05)

21 TC berada di `sourceTc` dua spec sekaligus, sehingga `check-suite.py` melaporkan 21 temuan C2. Ini disengaja (S-05, `P-5` butir a): asersi absence murni "Tidak ada entri Changelog baru" (kelas g) dipisah ke spec absence dengan baseline sendiri, sedangkan butir status respons (`403` atau `422`) dan nilai field tetap diasersi di spec kelas a. Id TC tetap di `sourceTc` kedua spec. Spec absence yang terlibat ada tiga (137, 138, 139), bukan dua:

- Spec `137` (Read Only): TC 586, 588, 590 (spec 168), TC 592, 594, 596 (spec 169), TC 598 (spec 170).
- Spec `138` (rentang Trial Settings, Free Plan Settings, License Timing): TC 610, 611 (spec 173), TC 614, 615 (spec 174), TC 618, 619 (spec 175).
- Spec `139` (rentang Client Lifecycle, Recycle Bin, Approval Settings, System Limits): TC 622, 623 (spec 176), TC 626, 627 (spec 178), TC 630, 631 (spec 179), TC 634, 635 (spec 180).
- Spec `140` (absence log Reset to Default dan penulisan log gagal) berdiri sendiri tanpa tumpang tindih.

Ketiga spec absence hanya memuat butir absence tersebut dan dipertahankan terpisah karena memisahkan baseline Changelog dari spec pemicu permintaan.

## Spec di atas ±35 langkah yang dipertahankan

25 dari 194 spec melewati ±35 langkah menurut hitungan Langkah Uji: 001 (38), 012 (41), 016 (41), 021 (37), 110 (42), 123 (38), 127 (39), 128 (39), 130 (39), 133 (43), 134 (50), 135 (38), 137 (41), 139 (43), 142 (56), 143 (37), 145 (56), 146 (67), 148 (45), 149 (51), 154 (42), 157 (43), 158 (42), 159 (46), 160 (45). Fix pass audit 2026-11-03 menambah langkah penghubung (pemulihan, baseline, Search, blur, catat waktu, tunggu) sehingga 123, 127, 128, 130, 142, 143, 145, 146, 148, 149, 154, 157, 158, 159 kini melewati batas; masing-masing menulis alasan di `## Notes`. Spec 093, 094, 121, 124, dan 166 yang sempat diperkirakan melewati batas ternyata 15, 15, 30, 13, dan 25 langkah. Spec 134 (50 langkah) paling panjang. Alasan di `## Notes` tiap spec seragam: tiap klausa Expected menjadi satu `Verifikasi` (S-01); seluruh blok satu kelas harness dan satu pola (screening landing, nilai default, Guided Tooltip, Role Matrix Read Only, Setup Column Changelog, pencatatan log, absence, atau konsumen lintas modul); dan tiap blok berdiri sendiri (tab, akun, state diseed ulang, atau baseline sendiri) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Khusus spec 110, state konfigurasi kolom Setup Column Changelog menyambung antar blok (hasil Save TC-AC-LCS-411 menjadi precondition TC-AC-LCS-413). Spec 160 mencatat bahwa pemecahan hanya menggandakan pola ganti akun yang sama.

## Kebutuhan lingkungan (tim FE)

- Env var password: sembilan nama akun suite ini (`AC_TC_PASSWORD`, `AC_DU_PASSWORD`, `AC_RO_PASSWORD`, `AC_MPL_PASSWORD`, `AC_NOCAP_PASSWORD`, `AC_DIST_PASSWORD`, `AC_PARTNER_PASSWORD`, `AC_CLIENT_PASSWORD`, `AC_DUCLIENT_PASSWORD`) sudah terdaftar di `spectra.config.ts` dan `.env.example` (nilai password dikelola tim FE). Email Default User Client PT Maju Jaya kini di Pre-setup 13 (usulan; keberadaan akun dikonfirmasi tim FE); akun Pre-setup 14-15 belum punya env password terdaftar dan disediakan tim FE.
- Penamaan env: `AC_DU_PASSWORD` (Default User Admin Console) dan `AC_DUCLIENT_PASSWORD` (Default User di client console PT Maju Jaya) adalah dua akun berbeda, jadi namanya tidak disatukan; `AC_MPL_PASSWORD` untuk akun Manage plans & licensing.
- Fixture modul `fixtures/lifecycle-settings.json` sudah ada (identitas akun, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dan dirujuk lewat `Fixture.lifecycleSettings.<kunci>`; nilai uji tetap ditulis persis seperti TC (S-02).
- Mekanisme Fixture BE tidak didefinisikan di TC, PRD, maupun LLD: pemulihan ketujuh tab dan General Settings, keadaan "tab belum pernah disimpan", seed ulang dan pengosongan dataset Changelog, pembacaan jumlah entri System Log dan Activity Log, pengatur jam server, pemicu dan pembacaan job lifecycle, pembacaan notifikasi dan email, pembuatan pohon Group, serta pemaksaan kegagalan penulisan log. Semua ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
- Kemampuan teknis lain: `Spectra.intercept()` (500, timeout, penundaan respons, intercept bersyarat per permintaan), login API password akun aktor tanpa mengusir sesi UI (spec 168–183), dua sesi browser paralel (spec 183, 184, 195), mail-catcher, jam server dan jam browser, penangkap unduhan Changelog, dan clipboard.
- Dialog `beforeunload`: TC 343, 344, dan 345 (spec 090) bergantung pada kemampuan menangani dialog `beforeunload` bawaan browser pada F5 saat form dirty. Teks dan tombol konfirmasi ditentukan browser, jadi spec hanya mengasersi tampil atau tidaknya konfirmasi. Bila tim FE belum dapat, spec 090 ditandai `coverage.web: unsupported`, bukan dihapus.
- Hook `beforeEach` suite (membuka Plans & Licensing > Lifecycle Settings sebagai Total Control) dikecualikan untuk spec 018, 019, 020, dan 161; pengecualiannya sudah dinyatakan di `suite.md` dan di Prerequisites tiap spec.
- Suite berjalan serial (`parallel: false`): ketujuh tab adalah satu set pengaturan platform-wide; Changelog, System Log, dan Activity Log permanen sehingga spec memakai baseline jumlah entri, bukan angka absolut (S-12).

## Temuan untuk QA (ringkasan dari `## Notes` spec)

Rincian ada di butir "Temuan untuk QA" tiap spec; yang berulang atau berdampak:

- Mekanisme precondition dan pengamatan tidak didefinisikan di TC, PRD, atau LLD sehingga ditulis sebagai kemampuan tim FE/BE (S-13): keadaan "tab belum pernah disimpan" (spec 011, 012), "Changelog tab kosong" padahal Changelog permanen (spec 119–131), cara membaca jumlah entri System Log dan Activity Log (spec 134, 135), jam server (spec 136), job lifecycle, notifikasi, dan email (spec 141–166), pohon Group (spec 165), dan kegagalan penulisan log (spec 140).
- Post Condition ("Tidak ada perubahan data", "tersimpan", "entri Changelog per field") tidak punya langkah observasi di TC sehingga tidak diasersi terpisah (S-01); berulang di sebagian besar spec, mis. 133–135 dan 137–139.
- Expected bertipe absence di TC (TC 16 butir d, TC 25 butir c dan d, TC 52 sampai 54 "tidak tampil lagi") ditulis dengan `Verifikasi` anchor positif lebih dulu (spec 005, 009, 015, 016).
- "Pesan error rentang" tanpa teks pesan (TC 128, 143, 168, 221, 236, 251, 291): spec hanya mengasersi keberadaan pesan (S-02). TC 132 mengetik `10000` dengan pesan "Value must be between 1 and 9,999" yang perlu dicek ke PRD (spec 039).
- State loading tombol dan "tepat satu permintaan" (TC 126/127, 141/142, 166/167, 219/220, 234/235, 249/250, 289/290) menuntut pengamatan permintaan jaringan yang tidak didefinisikan TC (spec 036, 041, 046, 059, 069, 074, 083).
- TC 94 menyebut "tersimpan tetap `30`" padahal `30` adalah nilai default sehingga Reset yang berhasil tidak terbedakan dari yang ditolak (spec 028); TC 93 dan 94 menyebut "sesi administrator kedua" tanpa akun dan sarana.
- TC 32 menyebut "tombol muat ulang" sedangkan TC 25 sampai 31 `[Try Again]`, dan butir a "Loading component tampil sesaat" rawan terlewat (spec 010).
- TC 46 memuat catatan editorial "(token nilai batas diganti nilai tersimpan 1000)" dan TC 50 memuat emoji pada teks target spotlight (spec 014, 015).
- Hook `beforeEach` bertabrakan dengan precondition TC 58 sampai 61 dan akun tanpa capability (spec 018, 019, 020, 161); pengecualiannya sudah dinyatakan di `suite.md`.
- TC 343 sampai 345 butuh penanganan `beforeunload` dan TC 341 butir d tidak menyebut cara menyiapkan riwayat browser (spec 090).
- TC 349 tumpang tindih dengan TC 122 (Save 500 tab Trial Settings); TC 353 dan 354 "pulihkan jaringan" tanpa mekanisme (spec 088).
- TC 424: judul menyebut "Search dan Filter aktif" tetapi hanya Search dan kolom visible yang diuji (spec 115). TC 381 sampai 383, 397, dan 398 menomori Expected "Langkah n" tidak sama dengan Langkah Uji (spec 100, 106).
- TC 644 sampai 650 mengasersi `1–1 of 1` absolut yang bertentangan dengan S-12 (spec 181, 182); TC 651 sampai 657 dan 675 bertanda Manual Only tetapi ditulis sebagai spec kelas c dengan kebutuhan dua sesi (spec 183, 184, 195).
- Data Pre-setup: Pre-setup 13-15 kini memuat Default User Client PT Maju Jaya, User Client PT Baru Mandiri, dan akun berizin Pre-setup 11 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE; env password selain `AC_DUCLIENT_PASSWORD` belum terdaftar); email pengguna Total Control produk terdampak, inisiator trial, kontak klien, requester, dan approver masih tidak tertulis; Pre-setup 9 tanpa Field entri seed (spec 137–139); Dataset L tidak memuat entri 10 May 26 pukul 23:30 UTC yang disyaratkan TC 497 (spec 136).
- TC 584 mengklaim seleksi manual berhenti pada baris ke-121 dan TC 583 tidak menyebut lokasi tautan Select All (spec 166).
- TC 142 mengulang `+ Activate Trial` untuk PT Cahaya Baru tanpa menyebut apakah aktivasi pertama menghalangi yang kedua; TC 546 dan 676 "percobaan ulang terbatas" tanpa jumlah (spec 142, 155, 194).

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-LCS-1 | TC-AC-LCS-E2E-001 | FE+BE |
| TC-AC-LCS-2 | TC-AC-LCS-E2E-001 | FE+BE |
| TC-AC-LCS-3 | TC-AC-LCS-E2E-001 | FE+BE |
| TC-AC-LCS-4 | TC-AC-LCS-E2E-002 | FE+BE |
| TC-AC-LCS-5 | TC-AC-LCS-E2E-002 | FE+BE |
| TC-AC-LCS-6 | TC-AC-LCS-E2E-185 | FE+BE |
| TC-AC-LCS-7 | TC-AC-LCS-E2E-185 | FE+BE |
| TC-AC-LCS-8 | TC-AC-LCS-E2E-003 | FE+BE |
| TC-AC-LCS-9 | TC-AC-LCS-E2E-003 | FE+BE |
| TC-AC-LCS-10 | TC-AC-LCS-E2E-003 | FE+BE |
| TC-AC-LCS-11 | TC-AC-LCS-E2E-003 | FE+BE |
| TC-AC-LCS-12 | TC-AC-LCS-E2E-004 | FE+BE |
| TC-AC-LCS-13 | TC-AC-LCS-E2E-004 | FE+BE |
| TC-AC-LCS-14 | TC-AC-LCS-E2E-004 | FE+BE |
| TC-AC-LCS-15 | TC-AC-LCS-E2E-005 | FE+BE |
| TC-AC-LCS-16 | TC-AC-LCS-E2E-005 | FE+BE |
| TC-AC-LCS-17 | TC-AC-LCS-E2E-006 | FE+BE |
| TC-AC-LCS-18 | TC-AC-LCS-E2E-006 | FE+BE |
| TC-AC-LCS-19 | TC-AC-LCS-E2E-006 | FE+BE |
| TC-AC-LCS-20 | TC-AC-LCS-E2E-007 | FE+BE |
| TC-AC-LCS-21 | TC-AC-LCS-E2E-007 | FE+BE |
| TC-AC-LCS-22 | TC-AC-LCS-E2E-008 | FE+BE |
| TC-AC-LCS-23 | TC-AC-LCS-E2E-008 | FE+BE |
| TC-AC-LCS-24 | TC-AC-LCS-E2E-005 | FE+BE |
| TC-AC-LCS-25 | TC-AC-LCS-E2E-009 | FE+BE |
| TC-AC-LCS-26 | TC-AC-LCS-E2E-009 | FE+BE |
| TC-AC-LCS-27 | TC-AC-LCS-E2E-009 | FE+BE |
| TC-AC-LCS-28 | TC-AC-LCS-E2E-009 | FE+BE |
| TC-AC-LCS-29 | TC-AC-LCS-E2E-010 | FE+BE |
| TC-AC-LCS-30 | TC-AC-LCS-E2E-010 | FE+BE |
| TC-AC-LCS-31 | TC-AC-LCS-E2E-010 | FE+BE |
| TC-AC-LCS-32 | TC-AC-LCS-E2E-010 | FE+BE |
| TC-AC-LCS-33 | TC-AC-LCS-E2E-011 | FE+BE |
| TC-AC-LCS-34 | TC-AC-LCS-E2E-011 | FE+BE |
| TC-AC-LCS-35 | TC-AC-LCS-E2E-011 | FE+BE |
| TC-AC-LCS-36 | TC-AC-LCS-E2E-012 | FE+BE |
| TC-AC-LCS-37 | TC-AC-LCS-E2E-012 | FE+BE |
| TC-AC-LCS-38 | TC-AC-LCS-E2E-012 | FE+BE |
| TC-AC-LCS-39 | TC-AC-LCS-E2E-012 | FE+BE |
| TC-AC-LCS-40 | TC-AC-LCS-E2E-013 | FE+BE |
| TC-AC-LCS-41 | TC-AC-LCS-E2E-013 | FE+BE |
| TC-AC-LCS-42 | TC-AC-LCS-E2E-013 | FE+BE |
| TC-AC-LCS-43 | TC-AC-LCS-E2E-186 | FE+BE |
| TC-AC-LCS-44 | TC-AC-LCS-E2E-014 | FE+BE |
| TC-AC-LCS-45 | TC-AC-LCS-E2E-014 | FE+BE |
| TC-AC-LCS-46 | TC-AC-LCS-E2E-014 | FE+BE |
| TC-AC-LCS-47 | TC-AC-LCS-E2E-014 | FE+BE |
| TC-AC-LCS-48 | TC-AC-LCS-E2E-014 | FE+BE |
| TC-AC-LCS-49 | TC-AC-LCS-E2E-015 | FE+BE |
| TC-AC-LCS-50 | TC-AC-LCS-E2E-015 | FE+BE |
| TC-AC-LCS-51 | TC-AC-LCS-E2E-015 | FE+BE |
| TC-AC-LCS-52 | TC-AC-LCS-E2E-015 | FE+BE |
| TC-AC-LCS-53 | TC-AC-LCS-E2E-016 | FE+BE |
| TC-AC-LCS-54 | TC-AC-LCS-E2E-016 | FE+BE |
| TC-AC-LCS-55 | TC-AC-LCS-E2E-016 | FE+BE |
| TC-AC-LCS-56 | TC-AC-LCS-E2E-016 | FE+BE |
| TC-AC-LCS-57 | TC-AC-LCS-E2E-017 | FE+BE |
| TC-AC-LCS-58 | TC-AC-LCS-E2E-018 | FE+BE |
| TC-AC-LCS-59 | TC-AC-LCS-E2E-018 | FE+BE |
| TC-AC-LCS-60 | TC-AC-LCS-E2E-018 | FE+BE |
| TC-AC-LCS-61 | TC-AC-LCS-E2E-018 | FE+BE |
| TC-AC-LCS-62 | TC-AC-LCS-E2E-019 | FE+BE |
| TC-AC-LCS-63 | TC-AC-LCS-E2E-020 | FE+BE |
| TC-AC-LCS-64 | TC-AC-LCS-E2E-019 | FE+BE |
| TC-AC-LCS-65 | TC-AC-LCS-E2E-020 | FE+BE |
| TC-AC-LCS-66 | TC-AC-LCS-E2E-019 | FE+BE |
| TC-AC-LCS-67 | TC-AC-LCS-E2E-020 | FE+BE |
| TC-AC-LCS-68 | TC-AC-LCS-E2E-019 | FE+BE |
| TC-AC-LCS-69 | TC-AC-LCS-E2E-020 | FE+BE |
| TC-AC-LCS-70 | TC-AC-LCS-E2E-021 | FE+BE |
| TC-AC-LCS-71 | TC-AC-LCS-E2E-021 | FE+BE |
| TC-AC-LCS-72 | TC-AC-LCS-E2E-021 | FE+BE |
| TC-AC-LCS-73 | TC-AC-LCS-E2E-022 | FE+BE |
| TC-AC-LCS-74 | TC-AC-LCS-E2E-022 | FE+BE |
| TC-AC-LCS-75 | TC-AC-LCS-E2E-023 | FE+BE |
| TC-AC-LCS-76 | TC-AC-LCS-E2E-023 | FE+BE |
| TC-AC-LCS-77 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-78 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-79 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-80 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-81 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-82 | TC-AC-LCS-E2E-024 | FE+BE |
| TC-AC-LCS-83 | TC-AC-LCS-E2E-025 | FE+BE |
| TC-AC-LCS-84 | TC-AC-LCS-E2E-025 | FE+BE |
| TC-AC-LCS-85 | TC-AC-LCS-E2E-025 | FE+BE |
| TC-AC-LCS-86 | TC-AC-LCS-E2E-025 | FE+BE |
| TC-AC-LCS-87 | TC-AC-LCS-E2E-026 | FE+BE |
| TC-AC-LCS-88 | TC-AC-LCS-E2E-026 | FE+BE |
| TC-AC-LCS-89 | TC-AC-LCS-E2E-026 | FE+BE |
| TC-AC-LCS-90 | TC-AC-LCS-E2E-026 | FE+BE |
| TC-AC-LCS-91 | TC-AC-LCS-E2E-027 | FE+BE |
| TC-AC-LCS-92 | TC-AC-LCS-E2E-027 | FE+BE |
| TC-AC-LCS-93 | TC-AC-LCS-E2E-028 | FE+BE |
| TC-AC-LCS-94 | TC-AC-LCS-E2E-028 | FE+BE |
| TC-AC-LCS-95 | TC-AC-LCS-E2E-029 | FE+BE |
| TC-AC-LCS-96 | TC-AC-LCS-E2E-029 | FE+BE |
| TC-AC-LCS-97 | TC-AC-LCS-E2E-029 | FE+BE |
| TC-AC-LCS-98 | TC-AC-LCS-E2E-029 | FE+BE |
| TC-AC-LCS-99 | TC-AC-LCS-E2E-029 | FE+BE |
| TC-AC-LCS-100 | TC-AC-LCS-E2E-030 | FE+BE |
| TC-AC-LCS-101 | TC-AC-LCS-E2E-030 | FE+BE |
| TC-AC-LCS-102 | TC-AC-LCS-E2E-030 | FE+BE |
| TC-AC-LCS-103 | TC-AC-LCS-E2E-030 | FE+BE |
| TC-AC-LCS-104 | TC-AC-LCS-E2E-030 | FE+BE |
| TC-AC-LCS-105 | TC-AC-LCS-E2E-031 | FE+BE |
| TC-AC-LCS-106 | TC-AC-LCS-E2E-031 | FE+BE |
| TC-AC-LCS-107 | TC-AC-LCS-E2E-031 | FE+BE |
| TC-AC-LCS-108 | TC-AC-LCS-E2E-031 | FE+BE |
| TC-AC-LCS-109 | TC-AC-LCS-E2E-031 | FE+BE |
| TC-AC-LCS-110 | TC-AC-LCS-E2E-032 | FE+BE |
| TC-AC-LCS-111 | TC-AC-LCS-E2E-032 | FE+BE |
| TC-AC-LCS-112 | TC-AC-LCS-E2E-032 | FE+BE |
| TC-AC-LCS-113 | TC-AC-LCS-E2E-032 | FE+BE |
| TC-AC-LCS-114 | TC-AC-LCS-E2E-032 | FE+BE |
| TC-AC-LCS-115 | TC-AC-LCS-E2E-033 | FE+BE |
| TC-AC-LCS-116 | TC-AC-LCS-E2E-033 | FE+BE |
| TC-AC-LCS-117 | TC-AC-LCS-E2E-033 | FE+BE |
| TC-AC-LCS-118 | TC-AC-LCS-E2E-033 | FE+BE |
| TC-AC-LCS-119 | TC-AC-LCS-E2E-034 | FE+BE |
| TC-AC-LCS-120 | TC-AC-LCS-E2E-034 | FE+BE |
| TC-AC-LCS-121 | TC-AC-LCS-E2E-035 | FE+BE |
| TC-AC-LCS-122 | TC-AC-LCS-E2E-084 | FE+BE |
| TC-AC-LCS-123 | TC-AC-LCS-E2E-036 | FE+BE |
| TC-AC-LCS-124 | TC-AC-LCS-E2E-036 | FE+BE |
| TC-AC-LCS-125 | TC-AC-LCS-E2E-086 | FE+BE |
| TC-AC-LCS-126 | TC-AC-LCS-E2E-036 | FE+BE |
| TC-AC-LCS-127 | TC-AC-LCS-E2E-036 | FE+BE |
| TC-AC-LCS-128 | TC-AC-LCS-E2E-034 | FE+BE |
| TC-AC-LCS-129 | TC-AC-LCS-E2E-039 | FE+BE |
| TC-AC-LCS-130 | TC-AC-LCS-E2E-039 | FE+BE |
| TC-AC-LCS-131 | TC-AC-LCS-E2E-039 | FE+BE |
| TC-AC-LCS-132 | TC-AC-LCS-E2E-039 | FE+BE |
| TC-AC-LCS-133 | TC-AC-LCS-E2E-039 | FE+BE |
| TC-AC-LCS-134 | TC-AC-LCS-E2E-040 | FE+BE |
| TC-AC-LCS-135 | TC-AC-LCS-E2E-040 | FE+BE |
| TC-AC-LCS-136 | TC-AC-LCS-E2E-040 | FE+BE |
| TC-AC-LCS-137 | TC-AC-LCS-E2E-084 | FE+BE |
| TC-AC-LCS-138 | TC-AC-LCS-E2E-041 | FE+BE |
| TC-AC-LCS-139 | TC-AC-LCS-E2E-041 | FE+BE |
| TC-AC-LCS-140 | TC-AC-LCS-E2E-086 | FE+BE |
| TC-AC-LCS-141 | TC-AC-LCS-E2E-041 | FE+BE |
| TC-AC-LCS-142 | TC-AC-LCS-E2E-041 | FE+BE |
| TC-AC-LCS-143 | TC-AC-LCS-E2E-040 | FE+BE |
| TC-AC-LCS-144 | TC-AC-LCS-E2E-042 | FE+BE |
| TC-AC-LCS-145 | TC-AC-LCS-E2E-042 | FE+BE |
| TC-AC-LCS-146 | TC-AC-LCS-E2E-042 | FE+BE |
| TC-AC-LCS-147 | TC-AC-LCS-E2E-042 | FE+BE |
| TC-AC-LCS-148 | TC-AC-LCS-E2E-042 | FE+BE |
| TC-AC-LCS-149 | TC-AC-LCS-E2E-043 | FE+BE |
| TC-AC-LCS-150 | TC-AC-LCS-E2E-043 | FE+BE |
| TC-AC-LCS-151 | TC-AC-LCS-E2E-043 | FE+BE |
| TC-AC-LCS-152 | TC-AC-LCS-E2E-043 | FE+BE |
| TC-AC-LCS-153 | TC-AC-LCS-E2E-043 | FE+BE |
| TC-AC-LCS-154 | TC-AC-LCS-E2E-044 | FE+BE |
| TC-AC-LCS-155 | TC-AC-LCS-E2E-044 | FE+BE |
| TC-AC-LCS-156 | TC-AC-LCS-E2E-044 | FE+BE |
| TC-AC-LCS-157 | TC-AC-LCS-E2E-044 | FE+BE |
| TC-AC-LCS-158 | TC-AC-LCS-E2E-044 | FE+BE |
| TC-AC-LCS-159 | TC-AC-LCS-E2E-045 | FE+BE |
| TC-AC-LCS-160 | TC-AC-LCS-E2E-045 | FE+BE |
| TC-AC-LCS-161 | TC-AC-LCS-E2E-187 | FE+BE |
| TC-AC-LCS-162 | TC-AC-LCS-E2E-189 | FE+BE |
| TC-AC-LCS-163 | TC-AC-LCS-E2E-046 | FE+BE |
| TC-AC-LCS-164 | TC-AC-LCS-E2E-046 | FE+BE |
| TC-AC-LCS-165 | TC-AC-LCS-E2E-086 | FE+BE |
| TC-AC-LCS-166 | TC-AC-LCS-E2E-046 | FE+BE |
| TC-AC-LCS-167 | TC-AC-LCS-E2E-046 | FE+BE |
| TC-AC-LCS-168 | TC-AC-LCS-E2E-045 | FE+BE |
| TC-AC-LCS-169 | TC-AC-LCS-E2E-047 | FE+BE |
| TC-AC-LCS-170 | TC-AC-LCS-E2E-047 | FE+BE |
| TC-AC-LCS-171 | TC-AC-LCS-E2E-047 | FE+BE |
| TC-AC-LCS-172 | TC-AC-LCS-E2E-047 | FE+BE |
| TC-AC-LCS-173 | TC-AC-LCS-E2E-047 | FE+BE |
| TC-AC-LCS-174 | TC-AC-LCS-E2E-048 | FE+BE |
| TC-AC-LCS-175 | TC-AC-LCS-E2E-048 | FE+BE |
| TC-AC-LCS-176 | TC-AC-LCS-E2E-048 | FE+BE |
| TC-AC-LCS-177 | TC-AC-LCS-E2E-048 | FE+BE |
| TC-AC-LCS-178 | TC-AC-LCS-E2E-048 | FE+BE |
| TC-AC-LCS-179 | TC-AC-LCS-E2E-049 | FE+BE |
| TC-AC-LCS-180 | TC-AC-LCS-E2E-049 | FE+BE |
| TC-AC-LCS-181 | TC-AC-LCS-E2E-049 | FE+BE |
| TC-AC-LCS-182 | TC-AC-LCS-E2E-049 | FE+BE |
| TC-AC-LCS-183 | TC-AC-LCS-E2E-050 | FE+BE |
| TC-AC-LCS-184 | TC-AC-LCS-E2E-050 | FE+BE |
| TC-AC-LCS-185 | TC-AC-LCS-E2E-050 | FE+BE |
| TC-AC-LCS-186 | TC-AC-LCS-E2E-050 | FE+BE |
| TC-AC-LCS-187 | TC-AC-LCS-E2E-051 | FE+BE |
| TC-AC-LCS-188 | TC-AC-LCS-E2E-051 | FE+BE |
| TC-AC-LCS-189 | TC-AC-LCS-E2E-051 | FE+BE |
| TC-AC-LCS-190 | TC-AC-LCS-E2E-051 | FE+BE |
| TC-AC-LCS-191 | TC-AC-LCS-E2E-051 | FE+BE |
| TC-AC-LCS-192 | TC-AC-LCS-E2E-052 | FE+BE |
| TC-AC-LCS-193 | TC-AC-LCS-E2E-052 | FE+BE |
| TC-AC-LCS-194 | TC-AC-LCS-E2E-052 | FE+BE |
| TC-AC-LCS-195 | TC-AC-LCS-E2E-052 | FE+BE |
| TC-AC-LCS-196 | TC-AC-LCS-E2E-052 | FE+BE |
| TC-AC-LCS-197 | TC-AC-LCS-E2E-053 | FE+BE |
| TC-AC-LCS-198 | TC-AC-LCS-E2E-053 | FE+BE |
| TC-AC-LCS-199 | TC-AC-LCS-E2E-053 | FE+BE |
| TC-AC-LCS-200 | TC-AC-LCS-E2E-053 | FE+BE |
| TC-AC-LCS-201 | TC-AC-LCS-E2E-053 | FE+BE |
| TC-AC-LCS-202 | TC-AC-LCS-E2E-054 | FE+BE |
| TC-AC-LCS-203 | TC-AC-LCS-E2E-054 | FE+BE |
| TC-AC-LCS-204 | TC-AC-LCS-E2E-054 | FE+BE |
| TC-AC-LCS-205 | TC-AC-LCS-E2E-054 | FE+BE |
| TC-AC-LCS-206 | TC-AC-LCS-E2E-055 | FE+BE |
| TC-AC-LCS-207 | TC-AC-LCS-E2E-055 | FE+BE |
| TC-AC-LCS-208 | TC-AC-LCS-E2E-055 | FE+BE |
| TC-AC-LCS-209 | TC-AC-LCS-E2E-055 | FE+BE |
| TC-AC-LCS-210 | TC-AC-LCS-E2E-056 | FE+BE |
| TC-AC-LCS-211 | TC-AC-LCS-E2E-056 | FE+BE |
| TC-AC-LCS-212 | TC-AC-LCS-E2E-057 | FE+BE |
| TC-AC-LCS-213 | TC-AC-LCS-E2E-057 | FE+BE |
| TC-AC-LCS-214 | TC-AC-LCS-E2E-058 | FE+BE |
| TC-AC-LCS-215 | TC-AC-LCS-E2E-189 | FE+BE |
| TC-AC-LCS-216 | TC-AC-LCS-E2E-059 | FE+BE |
| TC-AC-LCS-217 | TC-AC-LCS-E2E-059 | FE+BE |
| TC-AC-LCS-218 | TC-AC-LCS-E2E-086 | FE+BE |
| TC-AC-LCS-219 | TC-AC-LCS-E2E-059 | FE+BE |
| TC-AC-LCS-220 | TC-AC-LCS-E2E-059 | FE+BE |
| TC-AC-LCS-221 | TC-AC-LCS-E2E-058 | FE+BE |
| TC-AC-LCS-222 | TC-AC-LCS-E2E-067 | FE+BE |
| TC-AC-LCS-223 | TC-AC-LCS-E2E-067 | FE+BE |
| TC-AC-LCS-224 | TC-AC-LCS-E2E-067 | FE+BE |
| TC-AC-LCS-225 | TC-AC-LCS-E2E-067 | FE+BE |
| TC-AC-LCS-226 | TC-AC-LCS-E2E-067 | FE+BE |
| TC-AC-LCS-227 | TC-AC-LCS-E2E-068 | FE+BE |
| TC-AC-LCS-228 | TC-AC-LCS-E2E-068 | FE+BE |
| TC-AC-LCS-229 | TC-AC-LCS-E2E-068 | FE+BE |
| TC-AC-LCS-230 | TC-AC-LCS-E2E-085 | FE+BE |
| TC-AC-LCS-231 | TC-AC-LCS-E2E-069 | FE+BE |
| TC-AC-LCS-232 | TC-AC-LCS-E2E-069 | FE+BE |
| TC-AC-LCS-233 | TC-AC-LCS-E2E-087 | FE+BE |
| TC-AC-LCS-234 | TC-AC-LCS-E2E-069 | FE+BE |
| TC-AC-LCS-235 | TC-AC-LCS-E2E-069 | FE+BE |
| TC-AC-LCS-236 | TC-AC-LCS-E2E-068 | FE+BE |
| TC-AC-LCS-237 | TC-AC-LCS-E2E-072 | FE+BE |
| TC-AC-LCS-238 | TC-AC-LCS-E2E-072 | FE+BE |
| TC-AC-LCS-239 | TC-AC-LCS-E2E-072 | FE+BE |
| TC-AC-LCS-240 | TC-AC-LCS-E2E-072 | FE+BE |
| TC-AC-LCS-241 | TC-AC-LCS-E2E-072 | FE+BE |
| TC-AC-LCS-242 | TC-AC-LCS-E2E-073 | FE+BE |
| TC-AC-LCS-243 | TC-AC-LCS-E2E-073 | FE+BE |
| TC-AC-LCS-244 | TC-AC-LCS-E2E-073 | FE+BE |
| TC-AC-LCS-245 | TC-AC-LCS-E2E-085 | FE+BE |
| TC-AC-LCS-246 | TC-AC-LCS-E2E-074 | FE+BE |
| TC-AC-LCS-247 | TC-AC-LCS-E2E-074 | FE+BE |
| TC-AC-LCS-248 | TC-AC-LCS-E2E-087 | FE+BE |
| TC-AC-LCS-249 | TC-AC-LCS-E2E-074 | FE+BE |
| TC-AC-LCS-250 | TC-AC-LCS-E2E-074 | FE+BE |
| TC-AC-LCS-251 | TC-AC-LCS-E2E-073 | FE+BE |
| TC-AC-LCS-252 | TC-AC-LCS-E2E-075 | FE+BE |
| TC-AC-LCS-253 | TC-AC-LCS-E2E-075 | FE+BE |
| TC-AC-LCS-254 | TC-AC-LCS-E2E-075 | FE+BE |
| TC-AC-LCS-255 | TC-AC-LCS-E2E-075 | FE+BE |
| TC-AC-LCS-256 | TC-AC-LCS-E2E-075 | FE+BE |
| TC-AC-LCS-257 | TC-AC-LCS-E2E-076 | FE+BE |
| TC-AC-LCS-258 | TC-AC-LCS-E2E-076 | FE+BE |
| TC-AC-LCS-259 | TC-AC-LCS-E2E-076 | FE+BE |
| TC-AC-LCS-260 | TC-AC-LCS-E2E-076 | FE+BE |
| TC-AC-LCS-261 | TC-AC-LCS-E2E-076 | FE+BE |
| TC-AC-LCS-262 | TC-AC-LCS-E2E-077 | FE+BE |
| TC-AC-LCS-263 | TC-AC-LCS-E2E-077 | FE+BE |
| TC-AC-LCS-264 | TC-AC-LCS-E2E-077 | FE+BE |
| TC-AC-LCS-265 | TC-AC-LCS-E2E-077 | FE+BE |
| TC-AC-LCS-266 | TC-AC-LCS-E2E-077 | FE+BE |
| TC-AC-LCS-267 | TC-AC-LCS-E2E-078 | FE+BE |
| TC-AC-LCS-268 | TC-AC-LCS-E2E-078 | FE+BE |
| TC-AC-LCS-269 | TC-AC-LCS-E2E-078 | FE+BE |
| TC-AC-LCS-270 | TC-AC-LCS-E2E-078 | FE+BE |
| TC-AC-LCS-271 | TC-AC-LCS-E2E-078 | FE+BE |
| TC-AC-LCS-272 | TC-AC-LCS-E2E-079 | FE+BE |
| TC-AC-LCS-273 | TC-AC-LCS-E2E-079 | FE+BE |
| TC-AC-LCS-274 | TC-AC-LCS-E2E-079 | FE+BE |
| TC-AC-LCS-275 | TC-AC-LCS-E2E-079 | FE+BE |
| TC-AC-LCS-276 | TC-AC-LCS-E2E-079 | FE+BE |
| TC-AC-LCS-277 | TC-AC-LCS-E2E-080 | FE+BE |
| TC-AC-LCS-278 | TC-AC-LCS-E2E-080 | FE+BE |
| TC-AC-LCS-279 | TC-AC-LCS-E2E-080 | FE+BE |
| TC-AC-LCS-280 | TC-AC-LCS-E2E-080 | FE+BE |
| TC-AC-LCS-281 | TC-AC-LCS-E2E-080 | FE+BE |
| TC-AC-LCS-282 | TC-AC-LCS-E2E-081 | FE+BE |
| TC-AC-LCS-283 | TC-AC-LCS-E2E-081 | FE+BE |
| TC-AC-LCS-284 | TC-AC-LCS-E2E-082 | FE+BE |
| TC-AC-LCS-285 | TC-AC-LCS-E2E-085 | FE+BE |
| TC-AC-LCS-286 | TC-AC-LCS-E2E-083 | FE+BE |
| TC-AC-LCS-287 | TC-AC-LCS-E2E-083 | FE+BE |
| TC-AC-LCS-288 | TC-AC-LCS-E2E-087 | FE+BE |
| TC-AC-LCS-289 | TC-AC-LCS-E2E-083 | FE+BE |
| TC-AC-LCS-290 | TC-AC-LCS-E2E-083 | FE+BE |
| TC-AC-LCS-291 | TC-AC-LCS-E2E-082 | FE+BE |
| TC-AC-LCS-292 | TC-AC-LCS-E2E-035 | FE+BE |
| TC-AC-LCS-293 | TC-AC-LCS-E2E-035 | FE+BE |
| TC-AC-LCS-294 | TC-AC-LCS-E2E-035 | FE+BE |
| TC-AC-LCS-295 | TC-AC-LCS-E2E-037 | FE+BE |
| TC-AC-LCS-296 | TC-AC-LCS-E2E-037 | FE+BE |
| TC-AC-LCS-297 | TC-AC-LCS-E2E-037 | FE+BE |
| TC-AC-LCS-298 | TC-AC-LCS-E2E-037 | FE+BE |
| TC-AC-LCS-299 | TC-AC-LCS-E2E-063 | FE+BE |
| TC-AC-LCS-300 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-301 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-302 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-303 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-304 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-305 | TC-AC-LCS-E2E-060 | FE+BE |
| TC-AC-LCS-306 | TC-AC-LCS-E2E-061 | FE+BE |
| TC-AC-LCS-307 | TC-AC-LCS-E2E-061 | FE+BE |
| TC-AC-LCS-308 | TC-AC-LCS-E2E-061 | FE+BE |
| TC-AC-LCS-309 | TC-AC-LCS-E2E-062 | FE+BE |
| TC-AC-LCS-310 | TC-AC-LCS-E2E-062 | FE+BE |
| TC-AC-LCS-311 | TC-AC-LCS-E2E-062 | FE+BE |
| TC-AC-LCS-312 | TC-AC-LCS-E2E-062 | FE+BE |
| TC-AC-LCS-313 | TC-AC-LCS-E2E-063 | FE+BE |
| TC-AC-LCS-314 | TC-AC-LCS-E2E-056 | FE+BE |
| TC-AC-LCS-315 | TC-AC-LCS-E2E-064 | FE+BE |
| TC-AC-LCS-316 | TC-AC-LCS-E2E-064 | FE+BE |
| TC-AC-LCS-317 | TC-AC-LCS-E2E-064 | FE+BE |
| TC-AC-LCS-318 | TC-AC-LCS-E2E-064 | FE+BE |
| TC-AC-LCS-319 | TC-AC-LCS-E2E-065 | FE+BE |
| TC-AC-LCS-320 | TC-AC-LCS-E2E-065 | FE+BE |
| TC-AC-LCS-321 | TC-AC-LCS-E2E-065 | FE+BE |
| TC-AC-LCS-322 | TC-AC-LCS-E2E-065 | FE+BE |
| TC-AC-LCS-323 | TC-AC-LCS-E2E-066 | FE+BE |
| TC-AC-LCS-324 | TC-AC-LCS-E2E-066 | FE+BE |
| TC-AC-LCS-325 | TC-AC-LCS-E2E-066 | FE+BE |
| TC-AC-LCS-326 | TC-AC-LCS-E2E-066 | FE+BE |
| TC-AC-LCS-327 | TC-AC-LCS-E2E-056 | FE+BE |
| TC-AC-LCS-328 | TC-AC-LCS-E2E-070 | FE+BE |
| TC-AC-LCS-329 | TC-AC-LCS-E2E-070 | FE+BE |
| TC-AC-LCS-330 | TC-AC-LCS-E2E-070 | FE+BE |
| TC-AC-LCS-331 | TC-AC-LCS-E2E-071 | FE+BE |
| TC-AC-LCS-332 | TC-AC-LCS-E2E-071 | FE+BE |
| TC-AC-LCS-333 | TC-AC-LCS-E2E-071 | FE+BE |
| TC-AC-LCS-334 | TC-AC-LCS-E2E-071 | FE+BE |
| TC-AC-LCS-335 | TC-AC-LCS-E2E-071 | FE+BE |
| TC-AC-LCS-336 | TC-AC-LCS-E2E-089 | FE+BE |
| TC-AC-LCS-337 | TC-AC-LCS-E2E-089 | FE+BE |
| TC-AC-LCS-338 | TC-AC-LCS-E2E-089 | FE+BE |
| TC-AC-LCS-339 | TC-AC-LCS-E2E-089 | FE+BE |
| TC-AC-LCS-340 | TC-AC-LCS-E2E-089 | FE+BE |
| TC-AC-LCS-341 | TC-AC-LCS-E2E-090 | FE+BE |
| TC-AC-LCS-342 | TC-AC-LCS-E2E-090 | FE+BE |
| TC-AC-LCS-343 | TC-AC-LCS-E2E-090 | FE+BE |
| TC-AC-LCS-344 | TC-AC-LCS-E2E-090 | FE+BE |
| TC-AC-LCS-345 | TC-AC-LCS-E2E-090 | FE+BE |
| TC-AC-LCS-346 | TC-AC-LCS-E2E-061 | FE+BE |
| TC-AC-LCS-347 | TC-AC-LCS-E2E-091 | FE+BE |
| TC-AC-LCS-348 | TC-AC-LCS-E2E-091 | FE+BE |
| TC-AC-LCS-349 | TC-AC-LCS-E2E-088 | FE+BE |
| TC-AC-LCS-350 | TC-AC-LCS-E2E-092 | FE+BE |
| TC-AC-LCS-351 | TC-AC-LCS-E2E-092 | FE+BE |
| TC-AC-LCS-352 | TC-AC-LCS-E2E-191 | FE+BE |
| TC-AC-LCS-353 | TC-AC-LCS-E2E-088 | FE+BE |
| TC-AC-LCS-354 | TC-AC-LCS-E2E-088 | FE+BE |
| TC-AC-LCS-355 | TC-AC-LCS-E2E-093 | FE+BE |
| TC-AC-LCS-356 | TC-AC-LCS-E2E-095 | FE+BE |
| TC-AC-LCS-357 | TC-AC-LCS-E2E-093 | FE+BE |
| TC-AC-LCS-358 | TC-AC-LCS-E2E-095 | FE+BE |
| TC-AC-LCS-359 | TC-AC-LCS-E2E-093 | FE+BE |
| TC-AC-LCS-360 | TC-AC-LCS-E2E-095 | FE+BE |
| TC-AC-LCS-361 | TC-AC-LCS-E2E-094 | FE+BE |
| TC-AC-LCS-362 | TC-AC-LCS-E2E-096 | FE+BE |
| TC-AC-LCS-363 | TC-AC-LCS-E2E-094 | FE+BE |
| TC-AC-LCS-364 | TC-AC-LCS-E2E-096 | FE+BE |
| TC-AC-LCS-365 | TC-AC-LCS-E2E-094 | FE+BE |
| TC-AC-LCS-366 | TC-AC-LCS-E2E-096 | FE+BE |
| TC-AC-LCS-367 | TC-AC-LCS-E2E-094 | FE+BE |
| TC-AC-LCS-368 | TC-AC-LCS-E2E-096 | FE+BE |
| TC-AC-LCS-369 | TC-AC-LCS-E2E-097 | FE+BE |
| TC-AC-LCS-370 | TC-AC-LCS-E2E-097 | FE+BE |
| TC-AC-LCS-371 | TC-AC-LCS-E2E-097 | FE+BE |
| TC-AC-LCS-372 | TC-AC-LCS-E2E-098 | FE+BE |
| TC-AC-LCS-373 | TC-AC-LCS-E2E-098 | FE+BE |
| TC-AC-LCS-374 | TC-AC-LCS-E2E-098 | FE+BE |
| TC-AC-LCS-375 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-376 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-377 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-378 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-379 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-380 | TC-AC-LCS-E2E-099 | FE+BE |
| TC-AC-LCS-381 | TC-AC-LCS-E2E-100 | FE+BE |
| TC-AC-LCS-382 | TC-AC-LCS-E2E-100 | FE+BE |
| TC-AC-LCS-383 | TC-AC-LCS-E2E-100 | FE+BE |
| TC-AC-LCS-384 | TC-AC-LCS-E2E-100 | FE+BE |
| TC-AC-LCS-385 | TC-AC-LCS-E2E-100 | FE+BE |
| TC-AC-LCS-386 | TC-AC-LCS-E2E-104 | FE+BE |
| TC-AC-LCS-387 | TC-AC-LCS-E2E-104 | FE+BE |
| TC-AC-LCS-388 | TC-AC-LCS-E2E-104 | FE+BE |
| TC-AC-LCS-389 | TC-AC-LCS-E2E-104 | FE+BE |
| TC-AC-LCS-390 | TC-AC-LCS-E2E-105 | FE+BE |
| TC-AC-LCS-391 | TC-AC-LCS-E2E-105 | FE+BE |
| TC-AC-LCS-392 | TC-AC-LCS-E2E-105 | FE+BE |
| TC-AC-LCS-393 | TC-AC-LCS-E2E-105 | FE+BE |
| TC-AC-LCS-394 | TC-AC-LCS-E2E-105 | FE+BE |
| TC-AC-LCS-395 | TC-AC-LCS-E2E-106 | FE+BE |
| TC-AC-LCS-396 | TC-AC-LCS-E2E-106 | FE+BE |
| TC-AC-LCS-397 | TC-AC-LCS-E2E-106 | FE+BE |
| TC-AC-LCS-398 | TC-AC-LCS-E2E-106 | FE+BE |
| TC-AC-LCS-399 | TC-AC-LCS-E2E-107 | FE+BE |
| TC-AC-LCS-400 | TC-AC-LCS-E2E-107 | FE+BE |
| TC-AC-LCS-401 | TC-AC-LCS-E2E-107 | FE+BE |
| TC-AC-LCS-402 | TC-AC-LCS-E2E-107 | FE+BE |
| TC-AC-LCS-403 | TC-AC-LCS-E2E-108 | FE+BE |
| TC-AC-LCS-404 | TC-AC-LCS-E2E-108 | FE+BE |
| TC-AC-LCS-405 | TC-AC-LCS-E2E-108 | FE+BE |
| TC-AC-LCS-406 | TC-AC-LCS-E2E-108 | FE+BE |
| TC-AC-LCS-407 | TC-AC-LCS-E2E-109 | FE+BE |
| TC-AC-LCS-408 | TC-AC-LCS-E2E-109 | FE+BE |
| TC-AC-LCS-409 | TC-AC-LCS-E2E-109 | FE+BE |
| TC-AC-LCS-410 | TC-AC-LCS-E2E-110 | FE+BE |
| TC-AC-LCS-411 | TC-AC-LCS-E2E-110 | FE+BE |
| TC-AC-LCS-412 | TC-AC-LCS-E2E-110 | FE+BE |
| TC-AC-LCS-413 | TC-AC-LCS-E2E-110 | FE+BE |
| TC-AC-LCS-414 | TC-AC-LCS-E2E-110 | FE+BE |
| TC-AC-LCS-415 | TC-AC-LCS-E2E-113 | FE+BE |
| TC-AC-LCS-416 | TC-AC-LCS-E2E-113 | FE+BE |
| TC-AC-LCS-417 | TC-AC-LCS-E2E-113 | FE+BE |
| TC-AC-LCS-418 | TC-AC-LCS-E2E-113 | FE+BE |
| TC-AC-LCS-419 | TC-AC-LCS-E2E-114 | FE+BE |
| TC-AC-LCS-420 | TC-AC-LCS-E2E-114 | FE+BE |
| TC-AC-LCS-421 | TC-AC-LCS-E2E-114 | FE+BE |
| TC-AC-LCS-422 | TC-AC-LCS-E2E-114 | FE+BE |
| TC-AC-LCS-423 | TC-AC-LCS-E2E-115 | FE+BE |
| TC-AC-LCS-424 | TC-AC-LCS-E2E-115 | FE+BE |
| TC-AC-LCS-425 | TC-AC-LCS-E2E-117 | FE+BE |
| TC-AC-LCS-426 | TC-AC-LCS-E2E-117 | FE+BE |
| TC-AC-LCS-427 | TC-AC-LCS-E2E-117 | FE+BE |
| TC-AC-LCS-428 | TC-AC-LCS-E2E-117 | FE+BE |
| TC-AC-LCS-429 | TC-AC-LCS-E2E-118 | FE+BE |
| TC-AC-LCS-430 | TC-AC-LCS-E2E-118 | FE+BE |
| TC-AC-LCS-431 | TC-AC-LCS-E2E-118 | FE+BE |
| TC-AC-LCS-432 | TC-AC-LCS-E2E-111 | FE+BE |
| TC-AC-LCS-433 | TC-AC-LCS-E2E-111 | FE+BE |
| TC-AC-LCS-434 | TC-AC-LCS-E2E-111 | FE+BE |
| TC-AC-LCS-435 | TC-AC-LCS-E2E-112 | FE+BE |
| TC-AC-LCS-436 | TC-AC-LCS-E2E-112 | FE+BE |
| TC-AC-LCS-437 | TC-AC-LCS-E2E-112 | FE+BE |
| TC-AC-LCS-438 | TC-AC-LCS-E2E-192 | FE+BE |
| TC-AC-LCS-439 | TC-AC-LCS-E2E-124 | FE+BE |
| TC-AC-LCS-440 | TC-AC-LCS-E2E-124 | FE+BE |
| TC-AC-LCS-441 | TC-AC-LCS-E2E-124 | FE+BE |
| TC-AC-LCS-442 | TC-AC-LCS-E2E-124 | FE+BE |
| TC-AC-LCS-443 | TC-AC-LCS-E2E-125 | FE+BE |
| TC-AC-LCS-444 | TC-AC-LCS-E2E-125 | FE+BE |
| TC-AC-LCS-445 | TC-AC-LCS-E2E-126 | FE+BE |
| TC-AC-LCS-446 | TC-AC-LCS-E2E-126 | FE+BE |
| TC-AC-LCS-447 | TC-AC-LCS-E2E-126 | FE+BE |
| TC-AC-LCS-448 | TC-AC-LCS-E2E-127 | FE+BE |
| TC-AC-LCS-449 | TC-AC-LCS-E2E-127 | FE+BE |
| TC-AC-LCS-450 | TC-AC-LCS-E2E-127 | FE+BE |
| TC-AC-LCS-451 | TC-AC-LCS-E2E-127 | FE+BE |
| TC-AC-LCS-452 | TC-AC-LCS-E2E-128 | FE+BE |
| TC-AC-LCS-453 | TC-AC-LCS-E2E-128 | FE+BE |
| TC-AC-LCS-454 | TC-AC-LCS-E2E-128 | FE+BE |
| TC-AC-LCS-455 | TC-AC-LCS-E2E-128 | FE+BE |
| TC-AC-LCS-456 | TC-AC-LCS-E2E-129 | FE+BE |
| TC-AC-LCS-457 | TC-AC-LCS-E2E-129 | FE+BE |
| TC-AC-LCS-458 | TC-AC-LCS-E2E-129 | FE+BE |
| TC-AC-LCS-459 | TC-AC-LCS-E2E-130 | FE+BE |
| TC-AC-LCS-460 | TC-AC-LCS-E2E-130 | FE+BE |
| TC-AC-LCS-461 | TC-AC-LCS-E2E-130 | FE+BE |
| TC-AC-LCS-462 | TC-AC-LCS-E2E-130 | FE+BE |
| TC-AC-LCS-463 | TC-AC-LCS-E2E-131 | FE+BE |
| TC-AC-LCS-464 | TC-AC-LCS-E2E-131 | FE+BE |
| TC-AC-LCS-465 | TC-AC-LCS-E2E-125 | FE+BE |
| TC-AC-LCS-466 | TC-AC-LCS-E2E-120 | FE+BE |
| TC-AC-LCS-467 | TC-AC-LCS-E2E-120 | FE+BE |
| TC-AC-LCS-468 | TC-AC-LCS-E2E-121 | FE+BE |
| TC-AC-LCS-469 | TC-AC-LCS-E2E-119 | FE+BE |
| TC-AC-LCS-470 | TC-AC-LCS-E2E-121 | FE+BE |
| TC-AC-LCS-471 | TC-AC-LCS-E2E-121 | FE+BE |
| TC-AC-LCS-472 | TC-AC-LCS-E2E-122 | FE+BE |
| TC-AC-LCS-473 | TC-AC-LCS-E2E-122 | FE+BE |
| TC-AC-LCS-474 | TC-AC-LCS-E2E-123 | FE+BE |
| TC-AC-LCS-475 | TC-AC-LCS-E2E-123 | FE+BE |
| TC-AC-LCS-476 | TC-AC-LCS-E2E-123 | FE+BE |
| TC-AC-LCS-477 | TC-AC-LCS-E2E-140 | FE+BE |
| TC-AC-LCS-478 | TC-AC-LCS-E2E-132 | FE+BE |
| TC-AC-LCS-479 | TC-AC-LCS-E2E-132 | FE+BE |
| TC-AC-LCS-480 | TC-AC-LCS-E2E-132 | FE+BE |
| TC-AC-LCS-481 | TC-AC-LCS-E2E-133 | FE+BE |
| TC-AC-LCS-482 | TC-AC-LCS-E2E-133 | FE+BE |
| TC-AC-LCS-483 | TC-AC-LCS-E2E-133 | FE+BE |
| TC-AC-LCS-484 | TC-AC-LCS-E2E-133 | FE+BE |
| TC-AC-LCS-485 | TC-AC-LCS-E2E-134 | FE+BE |
| TC-AC-LCS-486 | TC-AC-LCS-E2E-134 | FE+BE |
| TC-AC-LCS-487 | TC-AC-LCS-E2E-134 | FE+BE |
| TC-AC-LCS-488 | TC-AC-LCS-E2E-134 | FE+BE |
| TC-AC-LCS-489 | TC-AC-LCS-E2E-135 | FE+BE |
| TC-AC-LCS-490 | TC-AC-LCS-E2E-135 | FE+BE |
| TC-AC-LCS-491 | TC-AC-LCS-E2E-135 | FE+BE |
| TC-AC-LCS-492 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-493 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-494 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-495 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-496 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-497 | TC-AC-LCS-E2E-136 | FE+BE |
| TC-AC-LCS-498 | TC-AC-LCS-E2E-141 | FE+BE |
| TC-AC-LCS-499 | TC-AC-LCS-E2E-142 | FE+BE |
| TC-AC-LCS-500 | TC-AC-LCS-E2E-142 | FE+BE |
| TC-AC-LCS-501 | TC-AC-LCS-E2E-142 | FE+BE |
| TC-AC-LCS-502 | TC-AC-LCS-E2E-143 | FE+BE |
| TC-AC-LCS-503 | TC-AC-LCS-E2E-143 | FE+BE |
| TC-AC-LCS-504 | TC-AC-LCS-E2E-143 | FE+BE |
| TC-AC-LCS-505 | TC-AC-LCS-E2E-143 | FE+BE |
| TC-AC-LCS-506 | TC-AC-LCS-E2E-144 | FE+BE |
| TC-AC-LCS-507 | TC-AC-LCS-E2E-144 | FE+BE |
| TC-AC-LCS-508 | TC-AC-LCS-E2E-145 | FE+BE |
| TC-AC-LCS-509 | TC-AC-LCS-E2E-145 | FE+BE |
| TC-AC-LCS-510 | TC-AC-LCS-E2E-145 | FE+BE |
| TC-AC-LCS-511 | TC-AC-LCS-E2E-145 | FE+BE |
| TC-AC-LCS-512 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-513 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-514 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-515 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-516 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-517 | TC-AC-LCS-E2E-146 | FE+BE |
| TC-AC-LCS-518 | TC-AC-LCS-E2E-147 | FE+BE |
| TC-AC-LCS-519 | TC-AC-LCS-E2E-148 | FE+BE |
| TC-AC-LCS-520 | TC-AC-LCS-E2E-148 | FE+BE |
| TC-AC-LCS-521 | TC-AC-LCS-E2E-148 | FE+BE |
| TC-AC-LCS-522 | TC-AC-LCS-E2E-148 | FE+BE |
| TC-AC-LCS-523 | TC-AC-LCS-E2E-148 | FE+BE |
| TC-AC-LCS-524 | TC-AC-LCS-E2E-149 | FE+BE |
| TC-AC-LCS-525 | TC-AC-LCS-E2E-149 | FE+BE |
| TC-AC-LCS-526 | TC-AC-LCS-E2E-149 | FE+BE |
| TC-AC-LCS-527 | TC-AC-LCS-E2E-149 | FE+BE |
| TC-AC-LCS-528 | TC-AC-LCS-E2E-150 | FE+BE |
| TC-AC-LCS-529 | TC-AC-LCS-E2E-150 | FE+BE |
| TC-AC-LCS-530 | TC-AC-LCS-E2E-151 | FE+BE |
| TC-AC-LCS-531 | TC-AC-LCS-E2E-151 | FE+BE |
| TC-AC-LCS-532 | TC-AC-LCS-E2E-151 | FE+BE |
| TC-AC-LCS-533 | TC-AC-LCS-E2E-152 | FE+BE |
| TC-AC-LCS-534 | TC-AC-LCS-E2E-152 | FE+BE |
| TC-AC-LCS-535 | TC-AC-LCS-E2E-152 | FE+BE |
| TC-AC-LCS-536 | TC-AC-LCS-E2E-152 | FE+BE |
| TC-AC-LCS-537 | TC-AC-LCS-E2E-153 | FE+BE |
| TC-AC-LCS-538 | TC-AC-LCS-E2E-153 | FE+BE |
| TC-AC-LCS-539 | TC-AC-LCS-E2E-153 | FE+BE |
| TC-AC-LCS-540 | TC-AC-LCS-E2E-154 | FE+BE |
| TC-AC-LCS-541 | TC-AC-LCS-E2E-154 | FE+BE |
| TC-AC-LCS-542 | TC-AC-LCS-E2E-154 | FE+BE |
| TC-AC-LCS-543 | TC-AC-LCS-E2E-193 | FE+BE |
| TC-AC-LCS-544 | TC-AC-LCS-E2E-193 | FE+BE |
| TC-AC-LCS-545 | TC-AC-LCS-E2E-193 | FE+BE |
| TC-AC-LCS-546 | TC-AC-LCS-E2E-155 | FE+BE |
| TC-AC-LCS-547 | TC-AC-LCS-E2E-156 | FE+BE |
| TC-AC-LCS-548 | TC-AC-LCS-E2E-156 | FE+BE |
| TC-AC-LCS-549 | TC-AC-LCS-E2E-156 | FE+BE |
| TC-AC-LCS-550 | TC-AC-LCS-E2E-156 | FE+BE |
| TC-AC-LCS-551 | TC-AC-LCS-E2E-157 | FE+BE |
| TC-AC-LCS-552 | TC-AC-LCS-E2E-157 | FE+BE |
| TC-AC-LCS-553 | TC-AC-LCS-E2E-157 | FE+BE |
| TC-AC-LCS-554 | TC-AC-LCS-E2E-157 | FE+BE |
| TC-AC-LCS-555 | TC-AC-LCS-E2E-157 | FE+BE |
| TC-AC-LCS-556 | TC-AC-LCS-E2E-158 | FE+BE |
| TC-AC-LCS-557 | TC-AC-LCS-E2E-158 | FE+BE |
| TC-AC-LCS-558 | TC-AC-LCS-E2E-158 | FE+BE |
| TC-AC-LCS-559 | TC-AC-LCS-E2E-158 | FE+BE |
| TC-AC-LCS-560 | TC-AC-LCS-E2E-158 | FE+BE |
| TC-AC-LCS-561 | TC-AC-LCS-E2E-159 | FE+BE |
| TC-AC-LCS-562 | TC-AC-LCS-E2E-159 | FE+BE |
| TC-AC-LCS-563 | TC-AC-LCS-E2E-159 | FE+BE |
| TC-AC-LCS-564 | TC-AC-LCS-E2E-159 | FE+BE |
| TC-AC-LCS-565 | TC-AC-LCS-E2E-159 | FE+BE |
| TC-AC-LCS-566 | TC-AC-LCS-E2E-160 | FE+BE |
| TC-AC-LCS-567 | TC-AC-LCS-E2E-160 | FE+BE |
| TC-AC-LCS-568 | TC-AC-LCS-E2E-160 | FE+BE |
| TC-AC-LCS-569 | TC-AC-LCS-E2E-160 | FE+BE |
| TC-AC-LCS-570 | TC-AC-LCS-E2E-161 | FE+BE |
| TC-AC-LCS-571 | TC-AC-LCS-E2E-163 | FE+BE |
| TC-AC-LCS-572 | TC-AC-LCS-E2E-163 | FE+BE |
| TC-AC-LCS-573 | TC-AC-LCS-E2E-163 | FE+BE |
| TC-AC-LCS-574 | TC-AC-LCS-E2E-164 | FE+BE |
| TC-AC-LCS-575 | TC-AC-LCS-E2E-164 | FE+BE |
| TC-AC-LCS-576 | TC-AC-LCS-E2E-164 | FE+BE |
| TC-AC-LCS-577 | TC-AC-LCS-E2E-196 | FE+BE |
| TC-AC-LCS-578 | TC-AC-LCS-E2E-196 | FE+BE |
| TC-AC-LCS-579 | TC-AC-LCS-E2E-165 | FE+BE |
| TC-AC-LCS-580 | TC-AC-LCS-E2E-165 | FE+BE |
| TC-AC-LCS-581 | TC-AC-LCS-E2E-165 | FE+BE |
| TC-AC-LCS-582 | TC-AC-LCS-E2E-166 | FE+BE |
| TC-AC-LCS-583 | TC-AC-LCS-E2E-166 | FE+BE |
| TC-AC-LCS-584 | TC-AC-LCS-E2E-166 | FE+BE |
| TC-AC-LCS-585 | TC-AC-LCS-E2E-167 | FE+BE |
| TC-AC-LCS-586 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-586 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-587 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-588 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-588 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-589 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-590 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-590 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-591 | TC-AC-LCS-E2E-168 | FE+BE |
| TC-AC-LCS-592 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-592 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-593 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-594 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-594 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-595 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-596 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-596 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-597 | TC-AC-LCS-E2E-169 | FE+BE |
| TC-AC-LCS-598 | TC-AC-LCS-E2E-137 | FE+BE |
| TC-AC-LCS-598 | TC-AC-LCS-E2E-170 | FE+BE |
| TC-AC-LCS-599 | TC-AC-LCS-E2E-170 | FE+BE |
| TC-AC-LCS-600 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-601 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-602 | TC-AC-LCS-E2E-172 | FE+BE |
| TC-AC-LCS-603 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-604 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-605 | TC-AC-LCS-E2E-172 | FE+BE |
| TC-AC-LCS-606 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-607 | TC-AC-LCS-E2E-171 | FE+BE |
| TC-AC-LCS-608 | TC-AC-LCS-E2E-172 | FE+BE |
| TC-AC-LCS-609 | TC-AC-LCS-E2E-170 | FE+BE |
| TC-AC-LCS-610 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-610 | TC-AC-LCS-E2E-173 | FE+BE |
| TC-AC-LCS-611 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-611 | TC-AC-LCS-E2E-173 | FE+BE |
| TC-AC-LCS-612 | TC-AC-LCS-E2E-173 | FE+BE |
| TC-AC-LCS-613 | TC-AC-LCS-E2E-173 | FE+BE |
| TC-AC-LCS-614 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-614 | TC-AC-LCS-E2E-174 | FE+BE |
| TC-AC-LCS-615 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-615 | TC-AC-LCS-E2E-174 | FE+BE |
| TC-AC-LCS-616 | TC-AC-LCS-E2E-174 | FE+BE |
| TC-AC-LCS-617 | TC-AC-LCS-E2E-174 | FE+BE |
| TC-AC-LCS-618 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-618 | TC-AC-LCS-E2E-175 | FE+BE |
| TC-AC-LCS-619 | TC-AC-LCS-E2E-138 | FE+BE |
| TC-AC-LCS-619 | TC-AC-LCS-E2E-175 | FE+BE |
| TC-AC-LCS-620 | TC-AC-LCS-E2E-175 | FE+BE |
| TC-AC-LCS-621 | TC-AC-LCS-E2E-175 | FE+BE |
| TC-AC-LCS-622 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-622 | TC-AC-LCS-E2E-176 | FE+BE |
| TC-AC-LCS-623 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-623 | TC-AC-LCS-E2E-176 | FE+BE |
| TC-AC-LCS-624 | TC-AC-LCS-E2E-176 | FE+BE |
| TC-AC-LCS-625 | TC-AC-LCS-E2E-176 | FE+BE |
| TC-AC-LCS-626 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-626 | TC-AC-LCS-E2E-178 | FE+BE |
| TC-AC-LCS-627 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-627 | TC-AC-LCS-E2E-178 | FE+BE |
| TC-AC-LCS-628 | TC-AC-LCS-E2E-178 | FE+BE |
| TC-AC-LCS-629 | TC-AC-LCS-E2E-178 | FE+BE |
| TC-AC-LCS-630 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-630 | TC-AC-LCS-E2E-179 | FE+BE |
| TC-AC-LCS-631 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-631 | TC-AC-LCS-E2E-179 | FE+BE |
| TC-AC-LCS-632 | TC-AC-LCS-E2E-179 | FE+BE |
| TC-AC-LCS-633 | TC-AC-LCS-E2E-179 | FE+BE |
| TC-AC-LCS-634 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-634 | TC-AC-LCS-E2E-180 | FE+BE |
| TC-AC-LCS-635 | TC-AC-LCS-E2E-139 | FE+BE |
| TC-AC-LCS-635 | TC-AC-LCS-E2E-180 | FE+BE |
| TC-AC-LCS-636 | TC-AC-LCS-E2E-180 | FE+BE |
| TC-AC-LCS-637 | TC-AC-LCS-E2E-180 | FE+BE |
| TC-AC-LCS-638 | TC-AC-LCS-E2E-173 | FE+BE |
| TC-AC-LCS-639 | TC-AC-LCS-E2E-177 | FE+BE |
| TC-AC-LCS-640 | TC-AC-LCS-E2E-177 | FE+BE |
| TC-AC-LCS-641 | TC-AC-LCS-E2E-177 | FE+BE |
| TC-AC-LCS-642 | TC-AC-LCS-E2E-177 | FE+BE |
| TC-AC-LCS-643 | TC-AC-LCS-E2E-177 | FE+BE |
| TC-AC-LCS-644 | TC-AC-LCS-E2E-181 | FE+BE |
| TC-AC-LCS-645 | TC-AC-LCS-E2E-181 | FE+BE |
| TC-AC-LCS-646 | TC-AC-LCS-E2E-181 | FE+BE |
| TC-AC-LCS-647 | TC-AC-LCS-E2E-181 | FE+BE |
| TC-AC-LCS-648 | TC-AC-LCS-E2E-182 | FE+BE |
| TC-AC-LCS-649 | TC-AC-LCS-E2E-182 | FE+BE |
| TC-AC-LCS-650 | TC-AC-LCS-E2E-182 | FE+BE |
| TC-AC-LCS-651 | TC-AC-LCS-E2E-183 | FE+BE |
| TC-AC-LCS-652 | TC-AC-LCS-E2E-183 | FE+BE |
| TC-AC-LCS-653 | TC-AC-LCS-E2E-183 | FE+BE |
| TC-AC-LCS-654 | TC-AC-LCS-E2E-184 | FE+BE |
| TC-AC-LCS-655 | TC-AC-LCS-E2E-184 | FE+BE |
| TC-AC-LCS-656 | TC-AC-LCS-E2E-184 | FE+BE |
| TC-AC-LCS-657 | TC-AC-LCS-E2E-195 | FE+BE |
| TC-AC-LCS-658 | TC-AC-LCS-E2E-101 | FE+BE |
| TC-AC-LCS-659 | TC-AC-LCS-E2E-101 | FE+BE |
| TC-AC-LCS-660 | TC-AC-LCS-E2E-101 | FE+BE |
| TC-AC-LCS-661 | TC-AC-LCS-E2E-101 | FE+BE |
| TC-AC-LCS-662 | TC-AC-LCS-E2E-101 | FE+BE |
| TC-AC-LCS-663 | TC-AC-LCS-E2E-102 | FE+BE |
| TC-AC-LCS-664 | TC-AC-LCS-E2E-102 | FE+BE |
| TC-AC-LCS-665 | TC-AC-LCS-E2E-102 | FE+BE |
| TC-AC-LCS-666 | TC-AC-LCS-E2E-102 | FE+BE |
| TC-AC-LCS-667 | TC-AC-LCS-E2E-102 | FE+BE |
| TC-AC-LCS-668 | TC-AC-LCS-E2E-103 | FE+BE |
| TC-AC-LCS-669 | TC-AC-LCS-E2E-103 | FE+BE |
| TC-AC-LCS-670 | TC-AC-LCS-E2E-103 | FE+BE |
| TC-AC-LCS-671 | TC-AC-LCS-E2E-103 | FE+BE |
| TC-AC-LCS-672 | TC-AC-LCS-E2E-103 | FE+BE |
| TC-AC-LCS-673 | TC-AC-LCS-E2E-038 | FE+BE |
| TC-AC-LCS-674 | TC-AC-LCS-E2E-038 | FE+BE |
| TC-AC-LCS-675 | TC-AC-LCS-E2E-195 | FE+BE |
| TC-AC-LCS-676 | TC-AC-LCS-E2E-155 | FE+BE |
| TC-AC-LCS-677 | TC-AC-LCS-E2E-194 | FE+BE |
| TC-AC-LCS-678 | TC-AC-LCS-E2E-156 | FE+BE |
| TC-AC-LCS-679 | TC-AC-LCS-E2E-194 | FE+BE |
| TC-AC-LCS-680 | TC-AC-LCS-E2E-162 | FE+BE |
| TC-AC-LCS-681 | TC-AC-LCS-E2E-160 | FE+BE |
| TC-AC-LCS-682 | TC-AC-LCS-E2E-162 | FE+BE |
| TC-AC-LCS-683 | TC-AC-LCS-E2E-162 | FE+BE |
| TC-AC-LCS-684 | TC-AC-LCS-E2E-116 | FE+BE |
| TC-AC-LCS-685 | TC-AC-LCS-E2E-038 | FE+BE |
| TC-AC-LCS-686 | TC-AC-LCS-E2E-140 | FE+BE |
| TC-AC-LCS-687 | TC-AC-LCS-E2E-158 | FE+BE |

## Ketergantungan eksternal yang diterima (2026-11-02)

Tiga ketergantungan berikut diterima user pada tanggal ini sebagai prasyarat eksternal, bukan sebagai temuan yang sudah terselesaikan. Suite belum bisa dijalankan penuh sebelum ketiganya tersedia.

- **Fixture BE:** kontrak kemampuan (pemulihan konfigurasi tujuh tab dan General Settings, seed nilai non-default, seed Dataset L dan Changelog kosong, seed lebih dari 5.000 entri, atur dan bekukan jam server, picu job dan baca log job, paksa gagal log, email, cold storage, dan purge, cabut capability di tengah aksi, ubah status subscription client, sesi API pelaku kedua) belum didefinisikan di TC, PRD, atau LLD. Spec menulisnya sebagai disediakan tim FE/BE (S-13).
- **Akun Pre-setup 13 sampai 15:** email memakai pola Pre-setup 6 sebagai usulan; keberadaan akun dan env password akun Pre-setup 14 dan 15 menunggu konfirmasi tim FE. Email pengguna Total Control produk terdampak, inisiator trial, kontak client, requester, approver, dan pengguna A dan B (TC 681) belum tertulis di Pre-setup TC.
- **Dialog `beforeunload` (spec 090, TC 343 sampai 345):** spec tetap `coverage.web: automated` dengan kemampuan menangani dialog itu tertulis di Prerequisites sebagai disediakan tim FE. API-nya tidak ditemukan di `@testspectra` saat dicek dan belum terverifikasi; bila ternyata tidak ada, spec 090 diubah menjadi `unsupported`.
