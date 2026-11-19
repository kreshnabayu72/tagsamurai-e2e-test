# Coverage E2E — Admin Console > Client

Sumber: `admin-console/client/TestCases/tc-client.md` (1022 TC, ID `TC-AC-ACC-1`–`1040` tidak kontigu, semua aktif). Suite: `specs/AdminConsole/Client/`. Prefix: `AC` + `ACC` (`TC-AC-ACC-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). `tc-client-backend.md` (namespace `TC-AC-ACC-BE-*`) tidak dipetakan di halaman ini.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 1022 TC aktif masuk 273 spec; tidak ada TC yang tertandai `FE Test = -`, jadi tidak ada TC yang berstatus hanya-BE dan dikeluarkan dari spec. Setiap TC terpetakan ke tepat satu spec, dengan satu pengecualian yang diputuskan pemilik (TC-AC-ACC-999, lihat bagian Pengecualian S-05). Seluruh spec bermode `FE+BE`.

Spec memakai `coverage.web: automated`, kecuali tiga spec Android native (024, 065, 228) yang memakai `coverage.mobile: automated` (keputusan pemilik: spec mobile tetap `automated` walau kolom Automation TC bertanda `Manual Only` untuk aplikasi native).

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | Screening List Client: Tiga Sub-tab, Kolom Default, Urutan A-Z, dan Row States | FE+BE | 79 | 1, 2, 3, 4, 7, 8, 19 |
| TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian | Badge Jumlah Sub-tab dan Empty State Hasil Pencarian List Client | FE+BE | 19 | 5, 6, 23, 24 |
| TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | Isi Sel Kolom List Client: Company Name, Managed By, Modified By, dan Kolom Opsional | FE+BE | 60 | 9, 10, 16, 17, 929 |
| TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | Isi Sel Badge Produk FAMS, SAMS, dan SIEM pada List Client | FE+BE | 56 | 12, 13, 14, 629, 630 |
| TC-AC-ACC-E2E-005-badge-produk-client-active-term-terakhir-archive | Badge Produk Client Active untuk Produk dengan Term Live yang Sudah Tidak Ada | FE+BE | 7 | 467 |
| TC-AC-ACC-E2E-006-sel-group-badge-primary-truncate-dan-hover-hierarki | Sel Group List Client: Badge Primary, Truncate 25 Karakter, dan Hover Hierarki Penuh | FE+BE | 13 | 11 |
| TC-AC-ACC-E2E-007-sel-pic-name-panjang-tidak-dipotong | Sel PIC Name 100 Karakter Tampil Utuh dan Client Code Teks Biasa pada List Client | FE+BE | 11 | 18 |
| TC-AC-ACC-E2E-008-empty-state-genuinely-kosong-tiga-sub-tab | Empty State Genuinely Kosong pada Tiga Sub-tab List Client | FE+BE | 10 | 20, 21, 22 |
| TC-AC-ACC-E2E-009-state-loading-dan-error-list-client | State Loading dan Error pada List Client | FE+BE | 13 | 25, 26 |
| TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | Sidebar Group Tree: Screening, Klik Node, Search Groups, Hierarchy Toggle, dan Collapse | FE+BE | 45 | 27, 28, 29, 30, 31, 32 |
| TC-AC-ACC-E2E-011-sidebar-group-tree-per-sub-tab-dan-assignment-berbeda | Sidebar Group Tree per Sub-tab bila Assignment Group Role Berbeda | FE+BE | 28 | 33, 34, 557 |
| TC-AC-ACC-E2E-012-navigasi-detail-dan-retensi-state-list | Navigasi ke Detail dari Row Action dan Retensi State List (Back dan F5) | FE+BE | 36 | 40, 41, 796 |
| TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal | Resolusi Group dan Managed By pada List Client untuk Viewer Principal | FE+BE | 25 | 35, 558, 566, 571 |
| TC-AC-ACC-E2E-014-pindah-group-distributor-memindahkan-group-client-langsung | Pindah Group Distributor Otomatis Memindahkan Group Client Distributor-langsung (Resolve Runtime) | FE+BE | 10 | 38 |
| TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | Resolusi Group, Managed By, dan Badge Produk pada List Client untuk Distributor PT Distribusi Nusantara | FE+BE | 39 | 15, 36, 559, 569, 570, 572, 927 |
| TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | Cakupan Client yang Terlihat Distributor PT Distribusi Nusantara pada List dan Detail | FE+BE | 39 | 58, 451, 574, 575, 576, 950 |
| TC-AC-ACC-E2E-017-resolusi-dan-cakupan-client-viewer-distributor-timur | Anchor, Group, dan Cakupan Client untuk Viewer Distributor PT Distribusi Timur | FE+BE | 14 | 567, 573, 928 |
| TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati | Resolusi Group dan Cakupan Client untuk Viewer Partner CV Mitra Sejati | FE+BE | 26 | 37, 59, 560, 909 |
| TC-AC-ACC-E2E-019-anchor-dan-group-viewer-partner-mitra-timur | Anchor dan Group Client Lintas Jaringan untuk Viewer Partner CV Mitra Timur | FE+BE | 6 | 568 |
| TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | Guided Tooltip Halaman Client List: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard | FE+BE | 72 | 39, 871, 872, 873, 878 |
| TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize | Guided Tooltip Halaman Client List: Skip, Klik Overlay, Berpindah Halaman, dan Resize Viewport | FE+BE | 29 | 874, 875, 876, 877 |
| TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | Guided Tooltip Halaman Client Detail: Kunjungan Pertama, Berikutnya, Replay, Navigasi, dan Keyboard | FE+BE | 72 | 879, 880, 881, 882, 887 |
| TC-AC-ACC-E2E-023-guided-tooltip-detail-skip-klik-overlay-berpindah-halaman-resize | Guided Tooltip Halaman Client Detail: Skip, Klik Overlay, Berpindah Halaman, dan Resize Viewport | FE+BE | 29 | 883, 884, 885, 886 |
| TC-AC-ACC-E2E-024-mobile-list-toolbar-card-dan-bottom-sheet-aksi | Mobile List Client: Toolbar, Card List, dan Bottom Sheet Aksi per Sub-tab | FE+BE | 40 | 417, 862, 863 |
| TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | Role Matrix Negatif: Menu Client Tersembunyi dan Akses URL Langsung Ditolak tanpa Capability | FE+BE | 44 | 42, 43, 44, 60, 453 |
| TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | Role Matrix Negatif: Akses URL Detail Client oleh Aktor Active-Read (403 Role Penaung dan 404 Netral di Luar Scope) | FE+BE | 49 | 61, 564, 565, 951, 954, 965 |
| TC-AC-ACC-E2E-027-role-matrix-negatif-akses-url-detail-aktor-archived-read | Role Matrix Negatif: Akses URL Detail Client oleh Aktor Archived-Read (403 per Status dan 404 Netral di Luar Scope) | FE+BE | 19 | 952, 953 |
| TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | Role Matrix: Visibilitas Elemen dan Aksi List dan Detail untuk Total Control dan Read Only | FE+BE | 65 | 45, 46, 57, 577, 581 |
| TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner | Role Matrix: Visibilitas Elemen dan Aksi List untuk Default User, Distributor, dan Partner | FE+BE | 44 | 56, 578, 579, 580 |
| TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Active Client (Read, Create, Update, Delete, Full) | FE+BE | 80 | 49, 50, 51, 52, 64 |
| TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client | Role Matrix: Visibilitas Elemen dan Aksi untuk Role Manage Archived Client (Read, Update, Delete) | FE+BE | 38 | 53, 54, 55, 583 |
| TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | Role Matrix: Group Manager (Scope Area Jakarta dan Descendant) pada Tree, List, per Sub-tab, dan Table Tools | FE+BE | 62 | 47, 48, 561, 562, 563, 582 |
| TC-AC-ACC-E2E-033-group-tree-pola-ancestor-disabled-dan-union-multi-node | Sidebar Group Tree: Pola Ancestor-disabled dan All Groups sebagai Union Node Assignment | FE+BE | 26 | 62, 63 |
| TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | Defense-in-depth: Aksi Tulis Langsung (Create/Edit/Suspend/Delete/Change Partner) tanpa Permission Ditolak Server | FE+BE | 51 | 450, 621, 622, 623, 624, 625 |
| TC-AC-ACC-E2E-035-defense-tulis-langsung-di-luar-scope-group-ditolak-404 | Defense-in-depth: Aksi Tulis Langsung ke Client di Luar Scope Group oleh Group Manager Ditolak 404 | FE+BE | 30 | 454, 987 |
| TC-AC-ACC-E2E-036-defense-injeksi-script-pada-address-client-disanitasi | Defense-in-depth: Input Script pada Address Client Disanitasi dan Tampil sebagai Teks Literal | FE+BE | 12 | 452 |
| TC-AC-ACC-E2E-041-create-screening-popup-cascading-dan-foto-af | Popup New Client: Screening, Cascading Country-State-City, dan Preview Photo (Active-Full) | FE+BE | 54 | 65, 121, 122 |
| TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | Validasi Create: Field Wajib, Format, dan Batas Karakter Diblokir (Active-Full) | FE+BE | 58 | 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 479, 480, 1044, 1046 |
| TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | Validasi Create: Filter Karakter, Newline, Emoji Fallback, dan Timing Pesan Error (Active-Full) | FE+BE | 76 | 78, 85, 493, 494, 495, 496, 497, 503, 504, 505, 506 |
| TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | Validasi Create: Duplikat Company Name, Client Code, dan Email Default User Ditolak (Active-Full) | FE+BE | 42 | 113, 114, 115, 118, 498, 942 |
| TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas | Create Client oleh Active-Full: Partner Dipilih dan Email Default User Sama dengan User Distributor, Partner, Principal | FE+BE | 31 | 66, 119, 501, 502 |
| TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit | Create Client oleh Active-Full: Client Code Kapital, Nama Dihapus Dipakai Ulang, Trim, dan Double-Submit | FE+BE | 37 | 116, 117, 120, 127 |
| TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af | Photo Client: Resize Foto Besar, Ganti, Hapus, dan Remove Staged (Active-Full) | FE+BE | 68 | 123, 162, 943, 966 |
| TC-AC-ACC-E2E-048-create-resilience-af-5xx-dan-geodata | Create Client: Resilience 5xx dan Geodata API Tidak Terjangkau (Active-Full) | FE+BE | 24 | 128, 129 |
| TC-AC-ACC-E2E-049-create-resilience-group-dihapus-dan-transaksi-atomik-tcp | Create Client: Group Dihapus Sebelum Submit dan Transaksi Atomik Gagal (Total Control) | FE+BE | 27 | 130, 507 |
| TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | Popup New Client: Footer, Opsi Industry, Opsi Partner, Tree Select Group, dan Perilaku Partner-Group (Total Control) | FE+BE | 46 | 481, 484, 485, 486, 487, 489 |
| TC-AC-ACC-E2E-051-create-aksesibilitas-popup-aria-dan-fokus-tcp | Aksesibilitas Popup New Client: aria-required, aria-describedby, dan Fokus Terkunci (Total Control) | FE+BE | 16 | 750, 751, 752 |
| TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | Create Client oleh Total Control: Stay on this Form, Direct, Dua Partner, Field Opsional, dan Saving State | FE+BE | 50 | 67, 70, 71, 490, 491, 749 |
| TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | Create Client: Nilai Tepat di Batas Karakter Diterima dan Spasi Ujung Tidak Dihitung (Total Control) | FE+BE | 52 | 475, 476, 477, 478, 1045, 1047 |
| TC-AC-ACC-E2E-054-create-pakai-ulang-client-code-dan-email-client-dihapus-tcp | Create Client: Client Code dan Email Default User Milik Client yang Sudah Dihapus Dipakai Ulang (Total Control) | FE+BE | 16 | 499, 500 |
| TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | Efek Lanjutan Create Client: Default User Not Yet Activated, Division, Position, dan Tiga Log (Total Control) | FE+BE | 33 | 131, 132, 133, 134, 492 |
| TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | Popup New Client: Clear Field, Esc, Klik Backdrop, Muat Ulang, dan Tombol Back (Total Control) | FE+BE | 78 | 72, 73, 74, 75, 488, 553, 554, 555, 556 |
| TC-AC-ACC-E2E-057-create-peran-partner-select-group-milik-partner | Create Client oleh Partner: Field Partner Tersembunyi dan Select Group Hanya Memuat Group Partner | FE+BE | 14 | 68 |
| TC-AC-ACC-E2E-058-create-peran-distributor-opsi-partner-dan-group-otomatis | Create Client oleh Distributor: Opsi Partner Jaringan, Partner Dipilih, dan Tanpa Partner | FE+BE | 23 | 69, 482, 483 |
| TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant | Group Manager: Create dan Edit Client di Node Descendant dengan Tree Select Group | FE+BE | 29 | 124, 541, 585, 587 |
| TC-AC-ACC-E2E-060-create-peran-active-create-only-tree-exact-match-dan-sukses | Active-Create-Only: Tree Select Group Exact-Match dan Create Client Sampai Sukses | FE+BE | 17 | 125, 584 |
| TC-AC-ACC-E2E-061-edit-peran-active-update-only-sukses-dan-tree-exact-match | Active-Update-Only: Edit Client Sampai Sukses dan Tree Select Group Exact-Match | FE+BE | 20 | 586, 588 |
| TC-AC-ACC-E2E-062-edit-client-archived-peran-archived-update-dan-read | Edit Client Archived: Pemegang Update Boleh Edit, Pemegang Read Tanpa Tombol Edit | FE+BE | 21 | 157, 546, 547 |
| TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | Defense: Create dan Edit Client dengan Request Dimanipulasi Ditolak Server | FE+BE | 69 | 126, 156, 159, 160, 947, 948 |
| TC-AC-ACC-E2E-064-create-balapan-dua-sesi-company-name-sama | Create Client: Dua Admin Menyimpan Company Name yang Sama Hampir Bersamaan (Dua Sesi) | FE+BE | 16 | 519 |
| TC-AC-ACC-E2E-065-mobile-popup-create-dan-edit-client-android-full-screen | Mobile Android: Form New Client dan Edit Client Full-Screen Satu Kolom dengan Footer Sticky | FE+BE | 17 | 888, 889 |
| TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | Popup Edit Client: Screening, Jalur Masuk, Field Reflected Derived, dan Aksi Client Suspended (Active-Full) | FE+BE | 56 | 135, 136, 138, 158, 161, 545, 946, 1007 |
| TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | Validasi Edit: Field Identitas Client Diblokir dan Duplikat Ditolak (Active-Full) | FE+BE | 44 | 142, 143, 144, 145, 146, 147, 148, 149, 523, 524, 525, 526, 529, 536, 537, 944 |
| TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | Validasi Edit Default User Not Yet Activated: Karakter, Email, Duplikat, dan Clear Field (Active-Full) | FE+BE | 75 | 521, 522, 527, 528, 530, 531, 532, 533 |
| TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | Edit Division dan Position Default User: Dropdown, Wajib, Stale, Dikosongkan, dan Changelog (Active-Full) | FE+BE | 62 | 150, 151, 152, 472, 473, 474, 542 |
| TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | Edit Client: Satu dan Banyak Field Tercatat di Changelog, No-Op, Double-Save, dan Identitas Default User (Active-Full) | FE+BE | 79 | 139, 140, 141, 165, 945 |
| TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | Popup Edit Client: Penutupan dengan ✕, Esc, Backdrop, F5, dan Tombol Back (Active-Full) | FE+BE | 66 | 166, 469, 470, 520, 548, 549, 550, 551, 552 |
| TC-AC-ACC-E2E-072-edit-activation-email-otomatis-saat-email-default-user-diubah-af | Edit Email Default User Not Yet Activated: Activation Email Otomatis Hanya Bila Ada Term Aktif atau Expired (Active-Full) | FE+BE | 33 | 633, 634, 635 |
| TC-AC-ACC-E2E-073-edit-resilience-5xx-dan-email-service-gagal-af | Edit Client: Resilience 5xx dan Email Service Gagal Saat Edit Email Default User (Active-Full) | FE+BE | 34 | 155, 164 |
| TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af | Edit Client dengan Perubahan Pelaku Kedua: Last-Write-Wins, Client Dihapus, Client Di-Suspend, dan Default User Diaktivasi (Active-Full) | FE+BE | 56 | 163, 544, 636, 637 |
| TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp | Edit Client Direct: Select Group Terisi, Wajib, Group Dihapus Sebelum Save, dan Perubahan Group Tercatat (Total Control) | FE+BE | 38 | 137, 538, 539, 540 |
| TC-AC-ACC-E2E-076-edit-email-default-user-lintas-entitas-pakai-ulang-dan-tidak-dapat-dinonaktifkan-tcp | Edit Email Default User: Email Lintas Entitas Diterima, Data Client Dihapus Dipakai Ulang, dan Default User Tidak Dapat Dinonaktifkan (Total Control) | FE+BE | 38 | 534, 535, 543 |
| TC-AC-ACC-E2E-077-edit-activation-email-ke-inbox-baru-tautan-lama-dan-term-pertama-tcp | Edit Email Default User: Activation Email Baru ke Inbox, Tautan Lama Tidak Berlaku, dan Pengiriman Saat Term Pertama Aktif (Total Control) | FE+BE | 30 | 153, 154 |
| TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | Popup Edit Client: Saving State, Aksesibilitas, dan Form Tidak Ter-Refresh oleh Perubahan Sesi Lain (Total Control) | FE+BE | 45 | 626, 753, 754, 755, 756 |
| TC-AC-ACC-E2E-079-edit-retry-activation-email-gagal-notifikasi-dan-dihentikan-tcp | Edit Email Default User: Retry Activation Email Gagal, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan (Total Control) | FE+BE | 77 | 959, 976, 984 |
| TC-AC-ACC-E2E-080-edit-retry-activation-email-notifikasi-default-user-principal | Notifikasi Kegagalan Activation Email Diterima Default User Principal Setelah Percobaan Ulang Ketiga | FE+BE | 20 | 973 |
| TC-AC-ACC-E2E-081-edit-retry-activation-email-penerima-notifikasi-empat-sesi | Notifikasi Kegagalan Activation Email: Total Control Menerima, Read Only, Group Manager, dan Active-Update-Only Tidak (Empat Sesi) | FE+BE | 25 | 977 |
| TC-AC-ACC-E2E-082-create-batas-pic-phone-dan-company-name-120-karakter-af | Create Client: PIC Phone 4 dan 15 Digit Diterima serta Company Name Tepat 120 Karakter (Active-Full) | FE+BE | 9 | 111, 112 |
| TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | Dialog Change Partner: Screening, Opsi [+ Add Partner], Badge Status Partner, dan Callout Group | FE+BE | 54 | 174, 508, 595, 596, 597, 995 |
| TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes | Dialog Change Partner: Penutupan lewat [✕] dan Esc, Dialog Unsaved Changes, dan Status [Confirm] | FE+BE | 46 | 180, 955, 956, 957 |
| TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag | Dialog Change Partner: Select Group Wajib Setelah Partner Terakhir di-Remove, Partner Ketiga, Aturan Drag, dan [Clear Field] | FE+BE | 51 | 179, 456, 457, 985 |
| TC-AC-ACC-E2E-114-change-partner-role-terbatas-tree-select-group-dan-sukses | Change Partner oleh Pemegang Update Manage Active Client dan Group Manager: Tree Select Group dan Add Partner Sukses | FE+BE | 40 | 590, 591, 594 |
| TC-AC-ACC-E2E-115-change-partner-oleh-distributor | Change Partner oleh Distributor: Relasi Distributor-langsung, Tree Select Group, Tambah Partner, Remove Anchor, dan Partner Terakhir Jaringan | FE+BE | 47 | 182, 592, 593, 601, 958 |
| TC-AC-ACC-E2E-116-change-partner-tambah-partner-principal-double-klik | Change Partner oleh Principal: Tambah Partner Tidak Mengubah Group, Relasi Suspended Tetap, dan Double-klik [Confirm] | FE+BE | 38 | 175, 598, 639 |
| TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag | Change Partner oleh Principal: Remove Anchor Memindahkan Group Otomatis dan Urutan List Menentukan Anchor | FE+BE | 40 | 176, 178, 599, 600 |
| TC-AC-ACC-E2E-118-change-partner-partner-terakhir-dan-ganti-partner-plan-owner | Change Partner oleh Principal: Remove Partner Terakhir Menjadi Direct dan Penggantian Partner Tidak Mengubah Plan Owner | FE+BE | 27 | 177, 185 |
| TC-AC-ACC-E2E-119-change-partner-kondisi-berubah-oleh-pelaku-lain | Change Partner: Group Dihapus, Dialog Tidak Ter-refresh, dan Client Dihapus oleh Pelaku Lain Sebelum Confirm | FE+BE | 30 | 188, 627, 638 |
| TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | Resend Activation Email: Hidden pada Client Tanpa Subscription Aktif, Archived, Activated, dan Sukses pada Active, Grace, Expired | FE+BE | 58 | 167, 168, 169, 663, 664, 665 |
| TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | Toggle Allow Self-Purchased Device Activation: Default Disabled, Dialog Enable, Cancel, Disable Tanpa Dialog, dan Nilai Sama | FE+BE | 37 | 246, 247, 248, 249, 251, 254 |
| TC-AC-ACC-E2E-122-toggle-byo-disabled-aktivasi-jalur-b-ditolak | Toggle BYO Disabled: Aktivasi Device Jalur B di Global Settings Hardware Ditolak dan Jalur A Tetap Berhasil | FE+BE | 7 | 255 |
| TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo | Role Matrix Positif: Resend Activation Email dan Toggle BYO oleh Pemegang Update, Distributor, dan Partner | FE+BE | 31 | 607, 608, 609, 617 |
| TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk | Double-klik Konfirmasi Suspend dan Unsuspend (Tunggal dan Bulk) Hanya Memproses Satu Kali | FE+BE | 77 | 647, 648, 649, 650 |
| TC-AC-ACC-E2E-125-double-klik-resend-toggle-byo-dan-delete | Double-klik Resend Activation Email, [Enable] Toggle BYO, dan [Delete] Hanya Memproses Satu Kali | FE+BE | 40 | 659, 660, 666 |
| TC-AC-ACC-E2E-126-double-klik-konfirmasi-lintas-aksi-tulis | Double-klik Tombol Konfirmasi Aksi Tulis (Suspend, Resend, Save, Delete) Tidak Memproses Ganda | FE+BE | 31 | 458 |
| TC-AC-ACC-E2E-127-delete-client-berfoto-dan-nama-dipakai-ulang | Delete Client Menghapus File Photo dan Nama Client yang Sudah Dihapus Dapat Dipakai Ulang | FE+BE | 25 | 231, 949 |
| TC-AC-ACC-E2E-128-resend-activation-email-inbox-dan-retry-otomatis | Resend Activation Email: Jumlah Email dan Log pada Dua Klik, Pembatalan Retry Otomatis, dan Pencatatan Send Activation Email | FE+BE | 58 | 908, 967, 968 |
| TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | Resilience Suspend dan Unsuspend (Tunggal dan Bulk): Global Settings Tidak Terjangkau dan Respons 5xx | FE+BE | 56 | 199, 200, 214, 460, 463 |
| TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | Resilience Change Partner, Resend Activation Email, Toggle BYO, dan Delete: 5xx, Email Service Gagal, Global Settings, dan State Basi | FE+BE | 52 | 171, 173, 186, 226, 227, 250 |
| TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | Defense-in-depth: Aksi Tulis pada Client Suspended dan Archived Hidden di UI dan Request Langsung Ditolak Server | FE+BE | 31 | 170, 183, 253, 906, 907 |
| TC-AC-ACC-E2E-132-defense-client-derived-request-langsung | Defense-in-depth: Change Partner, Suspend, dan Delete pada Client Derived Hidden di UI dan Request Langsung Ditolak Server | FE+BE | 15 | 184, 198, 228 |
| TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | Defense-in-depth: Request Langsung Tanpa Permission atau di Luar Jaringan Ditolak Server (Resend, Toggle BYO, Suspend, Delete, Change Partner) | FE+BE | 47 | 172, 181, 201, 232, 252, 962, 980 |
| TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | Defense-in-depth Delete: Request Langsung Ditolak Constraint D-03 dan D-14 pada Client Active, Suspended, dan Archived, serta Delete Suspended Tanpa Riwayat Diizinkan | FE+BE | 75 | 455, 465, 653, 654, 655, 978, 979, 981, 1025, 1026 |
| TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | Suspend dan Unsuspend Client: Screening Dialog, Cancel, Aksi Sukses, Subscription Tidak Berubah, dan Changelog | FE+BE | 60 | 189, 190, 191, 193, 194 |
| TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk | Pengamatan Total Control: Grace dan Expired Tetap di Sub-tab Active, Tanpa Aksi Archive, Archived Tanpa Bulk, dan Dialog Bulk Suspend 25 Client | FE+BE | 46 | 215, 640, 641, 642 |
| TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | Bulk Action Bar sub-tab Active: Screening, Counter, Checkbox Header, Menu Campuran, Cancel Bulk Suspend, dan Seleksi Dibersihkan Setelah Aksi | FE+BE | 45 | 202, 203, 204, 210, 216, 217 |
| TC-AC-ACC-E2E-138-bulk-suspend-unsuspend-semua-terpilih | Bulk Suspend dan Bulk Unsuspend: Dialog Gabungan Tanpa Jumlah, Toast Sukses, Badge Subscription Tidak Berubah, dan Changelog | FE+BE | 70 | 208, 209 |
| TC-AC-ACC-E2E-139-bulk-suspend-client-derived-campuran-dan-blok | Bulk Suspend dengan Client Derived: Dialog Campuran dengan [Continue] dan Dialog Blok D-15 Tanpa Toast Sukses | FE+BE | 45 | 212, 213 |
| TC-AC-ACC-E2E-140-bulk-selection-limit-dan-select-all-lintas-halaman | Bulk Selection: Select All Lintas Halaman Menjadi Unselect All dan Selection Limit 100 (Live-block dan Cap Select All) | FE+BE | 43 | 205, 206, 207 |
| TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend | Role Matrix Positif: Suspend, Unsuspend, dan Bulk Suspend oleh Pemegang Update Manage Active Client dan Group Manager | FE+BE | 52 | 602, 603, 604, 605 |
| TC-AC-ACC-E2E-142-suspend-subscription-tetap-bergulir-ke-expired | Subscription Tetap Bergulir ke Expired Selama Client Suspended (Job Scheduler Lifecycle dan Pengaturan Jam) | FE+BE | 17 | 195 |
| TC-AC-ACC-E2E-143-suspend-unsuspend-efek-ke-sesi-user-client | Suspend dan Unsuspend: Efek Read-only pada Sesi User Client di FAMS, Sesi Tidak Terputus, dan Override Dicabut | FE+BE | 35 | 192, 644, 960 |
| TC-AC-ACC-E2E-144-delete-efek-ke-sesi-dan-akses-default-user | Delete Client Archived: Efek ke Sesi Default User (Dialog Account no longer Active, Sesi Tetap Aktif) dan App Access Dicabut | FE+BE | 30 | 229, 230, 658 |
| TC-AC-ACC-E2E-145-suspend-unsuspend-dua-tab-idempoten | Suspend dan Unsuspend Race Dua Tab: Aksi Idempoten Tidak Menulis Changelog Baru dan Tidak Mengubah Last Updated | FE+BE | 35 | 196, 197 |
| TC-AC-ACC-E2E-146-dua-sesi-konflik-change-partner-dan-delete | Dua Sesi Admin: Konflik 409 pada Change Partner dan Delete Client yang Sudah Dihapus Sesi Lain Sukses Tanpa Baris Changelog Baru | FE+BE | 34 | 187, 961 |
| TC-AC-ACC-E2E-147-bulk-suspend-state-berubah-oleh-pelaku-lain | Suspend: Sebagian atau Semua Client Terpilih Sudah Disuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm | FE+BE | 53 | 211, 643, 645 |
| TC-AC-ACC-E2E-148-bulk-unsuspend-state-berubah-oleh-pelaku-lain | Unsuspend: Sebagian atau Semua Client Terpilih Sudah di-Unsuspend dan Client Dihapus oleh Pelaku Lain Sebelum Confirm | FE+BE | 51 | 461, 462, 646 |
| TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | Delete Client Archived: Dialog Konfirmasi D-05 dan Warning D-04, Tombol Delete Disabled Sampai Nama dan Checkbox Valid, Cancel, serta Delete Sukses | FE+BE | 51 | 218, 219, 220, 221, 651 |
| TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | Delete Client Active dan Suspended: Hidden bila Pernah Berlangganan, Tampil bila Tanpa Riwayat atau Hanya Rejected/Canceled, dan Delete Sukses | FE+BE | 85 | 223, 224, 466, 606, 652, 656, 657, 1027 |
| TC-AC-ACC-E2E-151-delete-diblok-subscription-ditambahkan-sesi-lain | Delete Diblok D-03 dan D-14 karena Subscription Ditambahkan Sesi Lain Tepat Sebelum Confirm (Archived, Active, dan Suspended) | FE+BE | 33 | 222, 225, 982 |
| TC-AC-ACC-E2E-152-delete-archived-diblok-trial-active-d03 | Delete Client Archived dengan Trial Active Diblok D-03 Seperti Term Paid Active | FE+BE | 9 | 1020 |
| TC-AC-ACC-E2E-153-delete-dialog-dan-izin-berubah-oleh-pelaku-lain | Dialog Delete: Tidak Ter-refresh oleh Perubahan Sesi Lain dan Delete Ditolak karena Izin Delete Dicabut Saat Dialog Terbuka | FE+BE | 21 | 628, 926 |
| TC-AC-ACC-E2E-171-screening-header-detail-client-active-full | Screening Header Detail Client dan Header Tanpa Suspend/Unsuspend (Active-Full) | FE+BE | 22 | 233, 869, 870 |
| TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | Header Detail Client: Tab, Sub-tab Awal, Client Derived, Badge Status, dan Badge Default User | FE+BE | 62 | 234, 235, 236, 239, 240 |
| TC-AC-ACC-E2E-173-section-parent-pengelola-dan-default-user | Section Parent / Pengelola dan Section Default User pada Detail Client | FE+BE | 36 | 798, 799 |
| TC-AC-ACC-E2E-174-default-user-tanpa-kontrol-nonaktif | Default User Tidak Dapat Dinonaktifkan dan Detail Client Tanpa Kontrolnya | FE+BE | 12 | 241, 459 |
| TC-AC-ACC-E2E-175-edit-client-default-user-activated-tidak-tertimpa | Edit Client dengan Default User Activated: Section Default User Tidak Tampil dan Nilai Tidak Tertimpa | FE+BE | 15 | 800 |
| TC-AC-ACC-E2E-176-client-derived-mengikuti-perubahan-partner-induk | Client Derived Mengikuti Perubahan Partner Induk: Address, Company Name, dan PIC Name | FE+BE | 24 | 237, 801 |
| TC-AC-ACC-E2E-177-default-user-detail-mengikuti-perubahan-global-settings | Default User di Detail Client Mengikuti Perubahan Global Settings Tanpa Muat Ulang | FE+BE | 13 | 238 |
| TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer | Role Matrix: Section Parent / Pengelola pada Detail Client per Viewer | FE+BE | 31 | 1010, 1011, 1030, 1031 |
| TC-AC-ACC-E2E-179-isolasi-tab-subscription-partner-cv-mitra-timur | Isolasi Plan Owner: Tab dan Sub-tab Subscription bagi Partner CV Mitra Timur | FE+BE | 25 | 275, 864, 865 |
| TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | Isolasi Plan Owner: Sub-tab Subscription, Changelog, dan Empty State per Viewer | FE+BE | 36 | 276, 277, 278, 279, 989, 990 |
| TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription | Role Matrix: Link dan Banner Tab Subscription per Role | FE+BE | 28 | 610, 611, 612, 613 |
| TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | Tab Subscription: Screening FAMS, Banner Read-only, Tanpa Aksi Write, dan Link Manage in Client Subscription | FE+BE | 31 | 256, 257, 258, 259, 802 |
| TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort | Tab Subscription: License Quota per Sub-tab, Nilai Ledger, Tanpa Baris Storage, dan Sort | FE+BE | 32 | 260, 261, 262, 809 |
| TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | Tab Subscription: Feature Entitlement per Sub-tab, Platform Core Client Free, dan Column Visibility | FE+BE | 38 | 263, 265, 266, 267, 803, 804, 805 |
| TC-AC-ACC-E2E-185-tab-subscription-feature-entitlement-source-plan | Tab Subscription: Source Feature Entitlement Plan Default dan Custom Plan | FE+BE | 22 | 264, 808 |
| TC-AC-ACC-E2E-186-tab-subscription-details-status-term-aktif-sampai-expired | Tab Subscription: Subscription Details untuk Status Active, Waiting for Approval, Pending, Grace, dan Expired | FE+BE | 31 | 268, 661 |
| TC-AC-ACC-E2E-187-tab-subscription-term-terakhir-archive-purge-deleted-dan-ditolak | Tab Subscription: Term Terakhir Archive, Purge, Deleted dan Client dengan Term Rejected atau Canceled | FE+BE | 24 | 936, 937 |
| TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup | License Quota dan Quota QR Bernilai 0 pada Term Expired, Archive, Waiting for Approval, Pending, dan Trial | FE+BE | 38 | 1005, 1009, 1034, 1037 |
| TC-AC-ACC-E2E-189-badge-produk-dan-kuota-term-trial | Term Trial: Badge Produk di List, Subscription Details Hasil Convert, dan Kuota Terpisah dari Term Paid | FE+BE | 20 | 1022, 1024 |
| TC-AC-ACC-E2E-190-total-quota-qr-tab-tag-dari-asset-license-term | Tab TAG: Total Quota QR dari Asset License Term Active dan Grace | FE+BE | 22 | 285, 996, 997 |
| TC-AC-ACC-E2E-191-quota-detail-mengikuti-perubahan-fams-asset-tag-dan-storage | Quota Detail Client Mengikuti Perubahan di FAMS: Used Asset dan TAG Bertambah, Footprint Storage Berkurang | FE+BE | 22 | 286, 301, 810 |
| TC-AC-ACC-E2E-192-rekonsiliasi-harian-mengoreksi-used-tag | Rekonsiliasi Harian Mengoreksi Used TAG saat Push Perubahan Terlewat | FE+BE | 10 | 816 |
| TC-AC-ACC-E2E-193-qty-hardware-list-bertambah-setelah-unit-diaktivasi | Qty Hardware List Bertambah setelah Unit Baru Diaktivasi di Global Settings | FE+BE | 8 | 817 |
| TC-AC-ACC-E2E-194-top-up-license-allocation-asset-dan-storage | Top-up Asset License dan Storage dari License Allocation Tercermin di Detail Client | FE+BE | 19 | 811, 815 |
| TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals | Perubahan Term dari Client Subscription dan Approvals: Reject Renewal, Renewal Expired/Grace, dan Cancel Term Terakhir | FE+BE | 33 | 269, 270, 271, 662 |
| TC-AC-ACC-E2E-196-tab-subscription-empty-state-nol-kuota-dan-term-archive | Tab Subscription: Empty State, Kuota Nol dengan Purchase History Kosong, dan Term Archive Tanpa Aksi Renew | FE+BE | 19 | 272, 273, 274 |
| TC-AC-ACC-E2E-197-purchase-history-license-screening-download-dan-filter-panel | Purchase History License: Screening Kolom, Panel Filter, dan Download Tab Subscription | FE+BE | 33 | 280, 282, 283 |
| TC-AC-ACC-E2E-198-purchase-history-license-search-semua-kolom | Purchase History License: Search per Kolom Teks, Numerik, dan Kolom Tanggal yang Tidak Dicari | FE+BE | 37 | 281, 757, 758 |
| TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | Purchase History License: Filter Kolom Dropdown, Range, Date, Kombinasi AND, dan Item serta Action by | FE+BE | 34 | 759, 760, 761, 762, 998 |
| TC-AC-ACC-E2E-200-purchase-history-license-sort-date-qty-duration | Purchase History License: Sort Kolom Date, Qty, dan Duration | FE+BE | 23 | 763, 764, 765 |
| TC-AC-ACC-E2E-201-purchase-history-license-plan-custom-dan-subscription-id | Purchase History License Client Custom Plan: Badge Plan Custom, Search Custom, dan Subscription ID | FE+BE | 18 | 806, 807, 938 |
| TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks | Purchase History License Client Custom Plan: Sort Kolom Subscription, Action by, Activation Date, Expired Date, dan Kolom Teks | FE+BE | 34 | 833, 834, 835, 939 |
| TC-AC-ACC-E2E-203-hover-nama-lengkap-action-by-dan-modified-by | Hover Action by dan Modified By Menampilkan Nama Lengkap pada Tabel Detail dan Modal Changelog | FE+BE | 31 | 812, 813 |
| TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | Tab TAG: Screening Quota dan Purchase History, Filter Panel, Download, dan Empty State | FE+BE | 35 | 284, 287, 288, 289, 471 |
| TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | Purchase History TAG: Search dan Filter per Kolom | FE+BE | 30 | 766, 767, 768, 769, 770 |
| TC-AC-ACC-E2E-206-sort-tabel-tab-tag-dan-storage-client-custom | Sort Tabel Tab TAG dan Purchase History Storage: Quota TAG, Purchase History TAG, dan Purchase History Storage | FE+BE | 33 | 836, 837, 841 |
| TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | Tab Hardware: Screening Hardware List, Toolbar per Section, Badge, Kolom Photo, Panel Filter, dan Empty State | FE+BE | 49 | 290, 291, 292, 294, 295, 297, 468 |
| TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort | Hardware List: Search per Kolom, Filter Dropdown, dan Sort Qty | FE+BE | 37 | 293, 781, 782, 784 |
| TC-AC-ACC-E2E-209-purchase-history-hardware-screening-filter-dan-download | Purchase History Hardware: Screening Filter dan Download CSV serta XLSX | FE+BE | 23 | 296, 785 |
| TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | Purchase History Hardware: Search dan Filter per Kolom | FE+BE | 30 | 771, 772, 773, 774, 775 |
| TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom | Tab Hardware Client Custom: Sort Hardware List, Quota, Purchase History dan Badge Category Terpotong | FE+BE | 46 | 783, 814, 839, 840 |
| TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | Tab Storage: Screening Quota, Breakdown Used, Read-only, Filter Panel, Download, dan Empty State | FE+BE | 41 | 298, 299, 300, 302, 303, 304, 786 |
| TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | Purchase History Storage: Search dan Filter per Kolom | FE+BE | 24 | 776, 777, 778, 779, 780 |
| TC-AC-ACC-E2E-214-sort-tabel-tab-subscription-quota-feature-dan-addon-client-custom | Tab Subscription Client Custom: Sort License Quota, Fixed Asset Module, dan Addon Features | FE+BE | 25 | 828, 829, 830 |
| TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | Column Visibility Tabel Sekunder Tab Subscription, TAG, Hardware, dan Storage | FE+BE | 72 | 818, 819, 820, 822, 823, 824 |
| TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | Empty State Hasil Search dan Filter Kosong pada Purchase History dan Hardware List Client Custom | FE+BE | 38 | 847, 848, 849, 850, 852 |
| TC-AC-ACC-E2E-217-pagination-purchase-history-license | Pagination Purchase History License: Page Size, Next, Previous, dan Input Nomor Halaman | FE+BE | 27 | 859, 860 |
| TC-AC-ACC-E2E-218-resilience-tabel-tab-subscription-tag-dan-hardware | Resilience: Error State dan Try Again pada Tabel Tab Subscription, TAG, dan Hardware | FE+BE | 37 | 853, 854 |
| TC-AC-ACC-E2E-219-loading-state-tabel-tab-detail | Loading State saat Data Tabel Tab Subscription, TAG, Hardware, Asset Control, dan Storage Diambil | FE+BE | 22 | 857 |
| TC-AC-ACC-E2E-220-tabel-kuota-dan-feature-entitlement-tanpa-search-dan-filter | Tabel Kuota, Feature Entitlement, Station Quota, dan Tablet List Tanpa Ikon Search dan Tombol Filter | FE+BE | 33 | 826 |
| TC-AC-ACC-E2E-221-aktivasi-term-pertama-preparing-access-dan-pending-ke-active | Aktivasi Term Pertama: Indikator Preparing Access dan Term Pending Menjadi Active pada Tanggal Mulai | FE+BE | 20 | 243, 245 |
| TC-AC-ACC-E2E-222-kegagalan-penyediaan-akses-notifikasi-dan-retry-manual | Kegagalan Penyediaan Akses Produk: Notifikasi setelah Percobaan Ketiga dan Retry Manual Berhasil atau Gagal Lagi | FE+BE | 65 | 244, 992, 1004 |
| TC-AC-ACC-E2E-223-notifikasi-kegagalan-penyediaan-akses-per-plan-owner | Notifikasi Kegagalan Penyediaan Akses per Plan Owner: Distributor Pemilik Plan Menerima, Read Only dan Distributor Luar Jaringan Tidak | FE+BE | 28 | 1006, 1032 |
| TC-AC-ACC-E2E-224-retry-akses-dari-tampilan-basi-dua-sesi | Retry Akses dari Tampilan Basi: Server Idempoten, Tidak Ada Rangkaian Kedua dan Tidak Ada Baris Log Baru | FE+BE | 14 | 1035 |
| TC-AC-ACC-E2E-225-role-matrix-retry-akses-tersembunyi-selain-total-control | Role Matrix: Tombol Retry pada Indikator Access Setup Failed Hidden untuk Read Only dan Active-Full | FE+BE | 12 | 993 |
| TC-AC-ACC-E2E-226-request-retry-akses-langsung-ditolak-server | Request Retry Akses Langsung Ditolak Server: Aktor Non-Total Control dan Aktor di Luar Jaringan Plan Owner | FE+BE | 12 | 1039 |
| TC-AC-ACC-E2E-227-retry-akses-gagal-diproses-toast-error | Retry Akses Gagal Diproses: Toast Error, Indikator Tetap Access Setup Failed, dan Tidak Ada Baris Changelog | FE+BE | 11 | 1008 |
| TC-AC-ACC-E2E-228-mobile-detail-client-android-card-list | Mobile Detail Client (Android): Card Subscription dan License Quota serta Card List Tab TAG, Hardware, Asset Control, dan Storage | FE+BE | 21 | 890, 891 |
| TC-AC-ACC-E2E-229-role-matrix-visibilitas-source-purchase-history-per-viewer | Role Matrix: Source pada Purchase History TAG, Hardware, dan Storage per Viewer Partner dan Distributor | FE+BE | 42 | 1014, 1015 |
| TC-AC-ACC-E2E-230-app-access-dan-activation-email-term-pertama-client | App Access Dibuat per Produk dan Activation Email Sekali pada Term Pertama Client, Tidak Lagi saat Renew | FE+BE | 11 | 242 |
| TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | Screening Tab Asset Control: Station Quota, Station List, Tablet List, Aksi Row, dan Download | FE+BE | 43 | 307, 308, 309, 310, 314, 338, 787, 788, 861 |
| TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | Tab Asset Control Tampil Tanpa Dibatasi Subscription dan Plan, Empty State, dan Reader Name Alias | FE+BE | 38 | 306, 337, 892, 893, 894 |
| TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader | Blokir Generate Enrollment QR karena Kuota Habis (D-08) dan Tidak Ada Smart Fixed Reader (D-17) | FE+BE | 41 | 305, 317, 940, 941 |
| TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | Generate Enrollment QR: Dialog, Pilihan SFR Otomatis, Token Active, Warning D-13, dan Changelog Asset Control | FE+BE | 69 | 315, 316, 318, 896, 916, 991 |
| TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit | TTL Token Enrollment QR 15 Menit: Expiry, Batas 14:59, 15:00, dan 15:01 | FE+BE | 42 | 321, 897, 898, 899 |
| TC-AC-ACC-E2E-236-role-matrix-positif-update-aksi-asset-control | Role Matrix Positif: Pemegang Update Manage Active Client Menjalankan Generate Enrollment QR, Revoke Tablet, dan Deactivate Station | FE+BE | 21 | 614, 615, 616 |
| TC-AC-ACC-E2E-237-defense-aksi-asset-control-client-archived-suspended-dan-role-read | Defense: Aksi Asset Control Hidden dan Request Langsung Ditolak Server untuk Client Archived, Suspended, dan Role Read | FE+BE | 49 | 335, 336, 905 |
| TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | Deactivate Station: Dialog, Batal, Hidden pada Station Deactivated, Sukses, Kuota Kembali, dan Klik Ganda | FE+BE | 73 | 324, 325, 326, 327, 328, 902, 917 |
| TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | Revoke Tablet: Dialog, Batal, Hidden pada Tablet Revoked, Sukses, Kuota Station Tetap, dan Klik Ganda | FE+BE | 53 | 329, 330, 331, 332, 901, 918 |
| TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog | Resilience Tab Asset Control: Generate Gagal, Deactivate dan Revoke Gagal, Error State Tabel, dan Error State Modal Changelog | FE+BE | 52 | 319, 333, 855, 856 |
| TC-AC-ACC-E2E-241-search-station-list-kolom-teks-dan-numerik | Search Station List: Kolom Teks (Reader Name, Reader Group, Reader ID, Reader Model, Status) dan Kolom Numerik (Ports) | FE+BE | 13 | 311, 789 |
| TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | Filter Station List: Screening Panel, Dropdown, Range Ports dan Tablets, Last Active, dan Empty State | FE+BE | 35 | 312, 790, 791, 792, 851 |
| TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | Sort Station List: Kolom Teks, Numerik, Last Active, dan Nilai Kosong Reader Group | FE+BE | 42 | 313, 793, 794, 795, 844 |
| TC-AC-ACC-E2E-244-sort-tablet-list-app-version-tanggal-dan-status | Sort Tablet List: Default Device Name, App Version Semantic, Enrolled Date, Last Active, dan Status | FE+BE | 23 | 845, 846 |
| TC-AC-ACC-E2E-245-column-visibility-dan-setup-column-tab-asset-control | Column Visibility Tiga Tabel dan Setup Column Station List pada Tab Asset Control | FE+BE | 33 | 821, 825 |
| TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat | Simulator Tablet Kiosk: Scan QR, Token Final Tidak Dapat Dipakai Ulang, Tablet Revoked Tidak Dapat Sync, dan Last Active Heartbeat | FE+BE | 36 | 322, 323, 895, 900 |
| TC-AC-ACC-E2E-247-dua-admin-generate-bersamaan-dan-aksi-basi-409 | Dua Admin: Generate Enrollment QR Bersamaan, Deactivate Station Basi, dan Revoke Tablet Basi (409) | FE+BE | 45 | 320, 974, 975 |
| TC-AC-ACC-E2E-248-sinkron-balik-global-settings-hardware-dua-sesi | Dua Sesi: Deactivate Station dan Revoke Tablet dari Global Settings Tampil di Tab Asset Control tanpa Reload | FE+BE | 19 | 903, 904 |
| TC-AC-ACC-E2E-249-deactivate-station-admin-console-tampil-di-global-settings-hardware | Deactivate Station dari Admin Console Tampil sebagai Deactivated di Global Settings > Hardware | FE+BE | 7 | 334 |
| TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | Modal Changelog: Client: Screening, Isi Kolom, Search per Kolom, dan Download | FE+BE | 49 | 339, 341, 342, 354, 722, 729, 970 |
| TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | Modal Changelog: Client: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong | FE+BE | 51 | 721, 723, 724, 725, 726, 727, 728 |
| TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download | Modal Changelog: Subscription: Screening, Format Kolom Subscription, Search per Kolom, dan Download | FE+BE | 28 | 344, 346, 347, 731 |
| TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | Modal Changelog: Subscription: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong | FE+BE | 44 | 730, 732, 733, 734, 735 |
| TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download | Modal Changelog: Asset Control: Screening, Isi Kolom Object dan Field, Search per Kolom, dan Download | FE+BE | 33 | 349, 351, 352, 355 |
| TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | Modal Changelog: Asset Control: Filter Panel, Filter per Kolom dan Rentang Date, serta Sort Date, Teks, dan Nilai Kosong | FE+BE | 37 | 736, 737, 738, 739, 740 |
| TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | Tiga Modal Changelog: Screening Column Visibility dan Setup Column, Tutup tanpa Save, Kolom Terakhir Disabled, dan Loading State | FE+BE | 35 | 741, 742, 747, 748, 858 |
| TC-AC-ACC-E2E-257-modal-changelog-setup-column-sembunyikan-dan-tampilkan-kolom-tersimpan | Tiga Modal Changelog: Ceklis dan Unceklis Kolom lalu Save, Muat Ulang, dan Tampilkan Kembali | FE+BE | 11 | 743 |
| TC-AC-ACC-E2E-258-modal-changelog-setup-column-drag-and-drop-urutan-kolom | Tiga Modal Changelog: Drag and Drop Urutan Kolom lalu Save dan Muat Ulang | FE+BE | 9 | 744 |
| TC-AC-ACC-E2E-259-modal-changelog-setup-column-pin-dan-unpin-kolom | Tiga Modal Changelog: Pin dan Unpin Kolom Membekukan Kolom saat Scroll Horizontal | FE+BE | 12 | 745 |
| TC-AC-ACC-E2E-260-modal-changelog-setup-column-reset-to-default | Tiga Modal Changelog: Reset to Default pada Modal Setup Column | FE+BE | 10 | 746 |
| TC-AC-ACC-E2E-261-modal-changelog-empty-state-genuinely-kosong-dan-hasil-search-kosong | Tiga Modal Changelog: Empty State Genuinely Kosong dan Hasil Search Kosong | FE+BE | 19 | 340, 345, 350 |
| TC-AC-ACC-E2E-262-modal-changelog-auto-refresh-diam-diam-lewat-sse | Tiga Modal Changelog: Auto-Refresh Diam-Diam lewat SSE saat Log Baru Masuk dari Sesi Lain | FE+BE | 8 | 343, 348, 353 |
| TC-AC-ACC-E2E-263-changelog-scope-baris-viewer-partner | Changelog Client dan Asset Control: Viewer Partner Hanya Melihat Baris yang Melibatkan Dirinya | FE+BE | 20 | 1012, 1016, 1023 |
| TC-AC-ACC-E2E-264-changelog-scope-baris-viewer-distributor | Changelog Client dan Asset Control: Viewer Distributor Hanya Melihat Baris Partner dalam Jaringannya | FE+BE | 14 | 1013, 1017 |
| TC-AC-ACC-E2E-265-changelog-dan-activity-log-retry-access-setup-principal-vs-distributor | Retry Access Setup: Baris Tampil bagi Principal di Changelog Client dan Activity Log, Disaring Seluruhnya bagi Distributor | FE+BE | 18 | 1040 |
| TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | Pencatatan Log Create, Edit, Change Partner, Perubahan Group, dan Satu Baris per Field di Changelog Client, System Log, dan Activity Log | FE+BE | 44 | 418, 419, 420, 430, 913, 914 |
| TC-AC-ACC-E2E-267-pencatatan-log-suspend-unsuspend-dan-bulk-suspend-di-tiga-surface | Pencatatan Log Suspend, Unsuspend, dan Bulk Suspend di Changelog Client, System Log, dan Activity Log | FE+BE | 35 | 421, 422, 915 |
| TC-AC-ACC-E2E-268-pencatatan-log-aksi-sistem-auto-archive-auto-reactivate-dan-send-activation-email | Pencatatan Log Aksi Sistem: Auto-Archive, Auto-Reactivate, dan Send Activation Email dengan Modified By System | FE+BE | 34 | 423, 424, 999 |
| TC-AC-ACC-E2E-269-pencatatan-log-resend-activation-email-dan-toggle-byo-di-tiga-surface | Pencatatan Log Resend Activation Email dan Toggle BYO Enabled dan Disabled di Changelog Client, System Log, dan Activity Log | FE+BE | 30 | 426, 428, 912 |
| TC-AC-ACC-E2E-270-pencatatan-log-generate-enrollment-qr-deactivate-station-dan-revoke-tablet-di-tiga-surface | Pencatatan Log Generate Enrollment QR, Deactivate Station, dan Revoke Tablet di Changelog Asset Control, System Log, dan Activity Log | FE+BE | 34 | 427, 910, 911 |
| TC-AC-ACC-E2E-271-pencatatan-log-delete-client-dan-pencabutan-app-access | Pencatatan Log Delete Client di Tiga Surface dan Pencabutan App Access Tercatat Terpisah di System Log | FE+BE | 24 | 425, 429 |
| TC-AC-ACC-E2E-272-absence-log-aksi-tanpa-perubahan-dan-aksi-sistem-tanpa-system-log | Absence Log: Edit No-Op, Bulk Suspend Baris yang Sudah Suspended, dan Aksi Sistem Send Activation Email Tidak Menulis Baris Log | FE+BE | 23 | 431, 999 |
| TC-AC-ACC-E2E-273-modified-by-snapshot-nama-aktor-saat-aksi | Modified By Changelog Client Adalah Snapshot Nama Aktor Saat Aksi dan Tidak Berubah Setelah Nama User Diganti | FE+BE | 11 | 432 |
| TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | Search Client List: Siklus Interaksi, Pencarian per Kolom, Kolom Last Updated Tidak Dicari, dan Input Literal | FE+BE | 43 | 356, 357, 358, 359, 360, 361, 362, 363, 364, 372, 373, 374, 717 |
| TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | Search Client List Terikat Visibilitas Kolom: Nilai Kolom Hidden Tidak Ditemukan, Ditemukan Setelah Kolom Ditampilkan | FE+BE | 19 | 365, 366, 367, 368, 369, 370, 371, 930 |
| TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown | Filter Client List: Screening Panel, Isi Opsi Dropdown, Cascading Country-State-City, dan Opsi Modified By System | FE+BE | 39 | 375, 388, 707, 932 |
| TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | Filter Client List: Hasil Filter per Field Partner, Distributor, Modified By, Industry, Country, State, dan City | FE+BE | 22 | 376, 377, 381, 383, 384, 385, 386 |
| TC-AC-ACC-E2E-285-filter-last-updated-rentang-tanggal | Filter Client List: Last Updated Date Range Picker Satu Field, Rentang Inklusif, dan Tanggal Mulai Sama dengan Tanggal Akhir | FE+BE | 11 | 382, 713 |
| TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem | Filter Client List: Placeholder dan Opsi Status FAMS, SAMS, SIEM Mengikuti Data Sub-tab, serta Hasil Filter | FE+BE | 44 | 378, 379, 380, 387 |
| TC-AC-ACC-E2E-287-filter-chip-dan-checkbox-sinkron | Filter Client List: Sinkronisasi Chip dan Centang Opsi pada Dropdown Multi-select | FE+BE | 14 | 714, 715 |
| TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | Filter Client List oleh Principal: Semantik Distributor (Transitif) dan Partner (Langsung), Relasi Transferred, Kombinasi AND dan OR | FE+BE | 52 | 389, 390, 618, 619, 620, 708, 933, 934, 969 |
| TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | Client List: Kombinasi Search, Filter, Sort, dan Pagination, Indikator Tombol Filter, serta Independensi Pelepasan Kontrol | FE+BE | 71 | 391, 392, 393, 678, 679, 709, 710, 711, 712 |
| TC-AC-ACC-E2E-290-distributor-filter-sort-sel-tanda-hubung | Client List oleh Distributor: Filter SAMS dan SIEM Tidak Mencocokkan Sel Tanda Hubung, dan Sort FAMS-SAMS-SIEM Menempatkan Tanda Hubung | FE+BE | 26 | 405, 686, 931 |
| TC-AC-ACC-E2E-291-opsi-filter-industry-diperbarui-setelah-edit | Filter Client List: Opsi Dropdown Industry Diperbarui Setelah Client Diedit Tanpa Reload | FE+BE | 13 | 716 |
| TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | Sort Client List: Siklus Tiga State Ascending, Descending, dan Nonaktif pada Kolom Default dan Managed By | FE+BE | 43 | 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 986 |
| TC-AC-ACC-E2E-293-sort-tujuh-kolom-hidden-default | Sort Client List: Siklus Tiga State pada Tujuh Kolom Curated Setelah Di-unhide | FE+BE | 11 | 404 |
| TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | Column Visibility Overlay dan Modal Setup Column Client List: Screening, Batas Pin, Penutupan Tanpa Simpan, Kolom Terakhir, Independensi Changelog, dan Reset to Default | FE+BE | 71 | 406, 407, 408, 687, 694, 695, 696, 697 |
| TC-AC-ACC-E2E-295-setup-column-centang-kolom-hideable | Setup Column Client List: Centang dan Hapus Centang Sepuluh Kolom Hideable, Simpan, dan Refresh | FE+BE | 9 | 688 |
| TC-AC-ACC-E2E-296-setup-column-centang-kolom-curated | Setup Column Client List: Centang dan Hapus Centang Tujuh Kolom Curated, Simpan, dan Refresh | FE+BE | 10 | 689 |
| TC-AC-ACC-E2E-297-setup-column-drag-and-drop-urutan-kolom | Setup Column Client List: Drag and Drop Urutan Kolom Hideable dan Curated, Simpan, dan Refresh | FE+BE | 15 | 690, 691 |
| TC-AC-ACC-E2E-298-setup-column-pin-kolom-membeku-saat-scroll | Setup Column Client List: Pin dan Unpin Kolom Hideable dan Curated Membekukan Kolom Saat Scroll Horizontal | FE+BE | 17 | 692, 693 |
| TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | Download Client List: Nama Berkas CSV dan XLSX, Tanpa Toast Sukses, serta Header Kolom Mengikuti Column Visibility | FE+BE | 23 | 409, 414, 698, 700, 701 |
| TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | Download Client List: Isi Sel Berkas CSV (Baris Sub-tab Aktif, Filter, Managed By, Group, Status Produk, Nilai Kosong, Last Updated) | FE+BE | 30 | 413, 699, 702, 703, 704, 705, 706 |
| TC-AC-ACC-E2E-301-download-volume-di-atas-5000-baris | Download Client List di Atas 5.000 Baris: Loading Screen Sampai Berkas Siap, Langsung Terunduh Tanpa Toast dan Tanpa Notifikasi | FE+BE | 13 | 935 |
| TC-AC-ACC-E2E-302-download-gagal-toast-error-resilience | Resilience Download: Kegagalan Ekspor List, Changelog Client, dan Tab Detail Menampilkan Toast Error dengan Nama Berkas | FE+BE | 14 | 410, 411, 412 |
| TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan | Client List: Pagination, Seleksi Manual Bertahan Saat Pindah Halaman, Berganti Search, dan Apply-Clear Filter | FE+BE | 63 | 415, 718, 719, 720 |
| TC-AC-ACC-E2E-304-sse-real-time-list-terfilter-dan-detail | SSE Real-time: Mutasi Subscription Memperbarui List Terfilter In-place dan Suspend Memperbarui Badge Detail Tanpa Muat Ulang | FE+BE | 16 | 416, 445 |
| TC-AC-ACC-E2E-305-sse-multi-tab-unsuspend-sesi-lain | SSE Real-time Dua Tab: Unsuspend dari Sesi Lain Memperbarui Badge Detail dan Sub-tab List Tanpa Muat Ulang | FE+BE | 12 | 676 |
| TC-AC-ACC-E2E-306-selection-limit-mengikuti-system-limits-terbaru | Selection Limit Client List Mengikuti System Limits Terbaru Tanpa Muat Ulang List (Volume Lebih dari 121 Baris) | FE+BE | 14 | 448 |
| TC-AC-ACC-E2E-307-race-auto-archive-term-baru-saat-evaluasi | Auto-Archive Dibatalkan Bila Term Baru Dibuat Saat Evaluasi Berjalan: Re-cek di Titik Commit | FE+BE | 9 | 435 |
| TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | Client List: Tooltip Ikon Toolbar, Tombol New Client, Ikon dan Severity Aksi Menu Row dan Bulk Action | FE+BE | 39 | 677, 680, 681, 682, 683, 684, 685 |
| TC-AC-ACC-E2E-309-auto-archive-via-cancel-term-terakhir | Auto-Archive Client Setelah Seluruh Term Terminal Lewat Cancel Subscription: Client Active, Client Suspended, dan Term Non-terminal | FE+BE | 27 | 433, 434, 436 |
| TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert | Auto-Archive Setelah Cancel Term Active Terakhir: Term Lama Purge atau Deleted, Trial Active, dan Successor Pending Hasil Convert | FE+BE | 49 | 971, 972, 1021, 1028 |
| TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | Client Suspended dengan Perubahan Subscription dan Cancel Predecessor: Status Entitas Independen, Add Subscription, Renewal, dan Successor Ikut Canceled | FE+BE | 54 | 438, 671, 673, 674, 675 |
| TC-AC-ACC-E2E-312-auto-reactivate-client-archived | Auto-Reactivate Client Archived: Add Subscription Mode New, Permintaan Di-Reject atau Di-Approve, dan Trial Tidak Memicu Reaktivasi | FE+BE | 49 | 437, 1018, 1019, 1029 |
| TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server | Job Lifecycle Otomatis dengan Jam Server Dimajukan: Auto-Archive Grace, Purge ke Deleted, Renewal Pending Menjadi Live, dan Trial Expired Lalu Delete | FE+BE | 53 | 669, 670, 964, 1033 |
| TC-AC-ACC-E2E-314-activation-email-dan-penyediaan-akses-gagal | Kegagalan Activation Email Otomatis dan Penyediaan Akses Produk: Toast Error, Notifikasi Setelah Percobaan Ketiga, dan Pengulangan Dihentikan Saat Suspend | FE+BE | 48 | 464, 963, 983 |
| TC-AC-ACC-E2E-315-approval-term-pertama-dan-notifikasi-requester | Approvals Term Pertama Mode New: Approve Menjadi Active dengan Activation Email, Reject Kembali ke No Subscription, dan Notifikasi ke Requester | FE+BE | 31 | 449, 667, 668 |
| TC-AC-ACC-E2E-316-add-own-subscription-client-derived | Add Own Subscription pada Detail Partner Membuat Satu Client Derived per Partner dengan Default User Bersama | FE+BE | 10 | 443 |
| TC-AC-ACC-E2E-317-entitas-induk-partner-suspend-unsuspend | Client Derived Saat Entitas Induk Partner Di-Suspend dan Di-Unsuspend: Tetap Active, Badge Derived, dan Aksi Menu | FE+BE | 23 | 1000 |
| TC-AC-ACC-E2E-318-entitas-induk-partner-delete | Client Derived Saat Entitas Induk Partner Di-Delete: Tidak Diblokir, Menjadi Direct, Dapat Diedit, Default User Bersama Tetap Ada, dan Jejak Log | FE+BE | 55 | 444, 1001, 1002 |
| TC-AC-ACC-E2E-319-entitas-induk-partner-promote-menjadi-distributor | Client Derived Saat Entitas Induk Partner Di-Promote Menjadi Distributor: Badge Derived Tetap, Managed By Pindah, dan Jejak Log | FE+BE | 22 | 1003 |
| TC-AC-ACC-E2E-320-change-partner-tercermin-di-tab-client-partner | Change Partner Tercermin di Tab Client Partner Lama dan Baru | FE+BE | 7 | 446 |
| TC-AC-ACC-E2E-321-format-tanggal-general-settings-pada-list-detail-changelog | Format Tanggal General Settings Diterapkan pada Last Updated List, Date Purchase History License Detail, dan Date Changelog Client | FE+BE | 9 | 447 |
| TC-AC-ACC-E2E-322-default-user-client-akses-produk-setelah-perubahan-status | Default User Client di Aplikasi Produk: Mode Read-only pada Produk Baru Client Suspended dan Override Dilepas Setelah Auto-Archive lalu Auto-Reactivate | FE+BE | 37 | 672, 994 |
| TC-AC-ACC-E2E-323-role-matrix-onboarding-opsi-new-client-tampil | Role Matrix: Opsi + New Client pada Field Client Form Add Subscription Tampil untuk Total Control, Active-Create + Allocation, dan Group Manager | FE+BE | 9 | 439, 924, 988 |
| TC-AC-ACC-E2E-324-role-matrix-onboarding-opsi-new-client-tidak-tampil-dan-bypass-ditolak | Role Matrix: Opsi + New Client Tidak Tampil untuk Active-Update + Allocation dan Active-Read + Allocation, dan Request Pembuatan Client Langsung Ditolak Server | FE+BE | 14 | 440, 925 |
| TC-AC-ACC-E2E-325-onboarding-screening-form-inline-dan-validasi-duplikat | One-step Onboarding: Screening Form Inline Tanpa Field Position, Company Name Duplikat, dan Email Default User Milik Client Lain Ditolak | FE+BE | 29 | 509, 516, 517 |
| TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan | One-step Onboarding Berhasil: Group Mengikuti Distributor Induk, Division Terseed Tanpa Position, Start Date Masa Depan Pending, dan Pencatatan Changelog serta Activity Log | FE+BE | 62 | 510, 513, 514, 515 |
| TC-AC-ACC-E2E-327-onboarding-form-inline-per-aktor-partner-distributor-active-full | One-step Onboarding per Aktor: Field Partner dan Select Group untuk Partner dan Distributor, serta Pembuatan Atomik oleh Active-Full | FE+BE | 35 | 441, 511, 512 |
| TC-AC-ACC-E2E-328-resilience-onboarding-geodata-dan-submit-5xx | Resilience One-step Onboarding: Geodata API Tidak Terjangkau dan Kegagalan 5xx Saat Submit Tidak Meninggalkan Client Parsial | FE+BE | 38 | 442, 518 |
| TC-AC-ACC-E2E-329-auto-archive-lalu-delete-client-dengan-trial-non-live | Auto-Archive Setelah Cancel Term Paid Terakhir dengan Trial Expired atau Waiting for Approval, Lalu Client Dihapus dari Sub-tab Archived | FE+BE | 34 | 1036, 1038 |

Spec dengan lebih dari sekitar 35 langkah memuat alasannya di `## Notes` masing-masing (tiap klausa Expected menjadi satu `Verifikasi`, S-01). Spec mobile (`coverage.mobile: automated`): 024, 065, 228; spec lain `coverage.web: automated`.

## Pengecualian S-05: TC-AC-ACC-999 di dua spec

TC-AC-ACC-999 ada di `sourceTc` spec `TC-AC-ACC-E2E-268` dan `TC-AC-ACC-E2E-272`. Keputusan pemilik: kedua spec dipertahankan. TC ini terbelah antara asersi presence (baris `Send Activation Email` di Changelog Client dan Activity Log, spec 268) dan asersi absence kelas g (tidak ada baris di System Log akun aktor, butir d, spec 272 dengan Client milik sendiri dan baseline sendiri, S-05). `check-suite.py` melaporkan satu temuan C2 untuk TC ini; temuan itu diterima sebagai pengecualian S-05, bukan kesalahan pemetaan. Pembagian ditulis di `## Notes` kedua spec.

## Kebutuhan lingkungan (tim FE/BE)

- Suite berjalan serial (`parallel: false`); hook suite (`suite.md`) menyatakan login aktor, flag Guided Tooltip, pemulihan preferensi Setup Column, pemulihan jam server dan Selection Limit, seeding ulang fixture Tabel A3, dan sesi API aktor.
- Env var password aktor: lihat tabel pemetaan di bawah. Hanya `AC_TC_PASSWORD` yang terdaftar di `spectra.config.ts` dan `.env.example`; nama kanonik lain didaftarkan tim FE pada tahap script (berkas itu tidak diubah oleh generate spec).
- Fixture BE (disediakan tim FE/BE, idempotent): seeding dan seeding ulang Client Pre-setup C-01…C-14 dan fixture Tabel A3 yang dikonsumsi atau diubah spec; seeding salinan fixture A3 bersuffix milik spec (pola `{runId}-NNN`); pembuatan Group sementara, Partner, dan Client lewat API; mekanisme seeding tidak disebut TC (lihat Temuan untuk QA).
- Sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web): dipakai 28 spec (035, 049, 069, 074, 075, 078, 119, 121, 130, 131, 132, 133, 134, 147, 148, 153, 177, 192, 193, 232, 262, 268, 272, 273, 304, 305, 306, 307).
- Manipulasi jam server (dan jam browser): 20 spec (079, 080, 081, 128, 142, 145, 221, 222, 223, 232, 234, 235, 236, 238, 246, 247, 270, 307, 313, 314). Pemulihan jam di langkah penghubung dan hook `after`.
- Mail-catcher untuk inbox Default User dengan baseline jumlah email: spec 055, 074, 077, 079, 128, 131, 230, 315, 327.
- Simulator reader, tablet, atau SFR Asset Control dan perangkat hardware: spec 122, 193, 207, 208, 209, 210, 211, 231, 232, 233, 234, 235, 236, 241, 242, 243, 246, 247, 270.
- Perangkat atau emulator Android native: spec 024, 065, 228. Pengubah ukuran viewport browser: spec 021, 023, 259, 298.
- `Spectra.intercept()` (respons 5xx, penahanan respons, kegagalan): 58 spec; yang memaksa 5xx: 009, 048, 049, 073, 079, 080, 081, 128, 129, 130, 218, 227, 240, 302, 314, 328.
- Dua sesi atau tab paralel (pelaku kedua): spec 064, 081, 143, 144, 146, 147, 148, 151, 224, 247, 248, 305, 306, 322.
- Reset flag Guided Tooltip untuk akun aktor: hook suite `before`/`after` (set true dan pulihkan); spec 020 sampai 023 menguji flag itu sendiri dan mengaturnya sesudah hook. Mekanisme reset flag disediakan tim FE/BE (TC/PRD tidak mendefinisikannya).
- Pemulihan preferensi Setup Column di browser (hapus preferensi, bukan `[Reset to Default]`): spec 052, 215, 245, 256, 257, 258, 259, 260, 282, 293, 294, 295, 296, 297, 298, 299, 300.
- Pemaksaan kegagalan sisi server (Global Settings tidak terjangkau, email service gagal, Geodata gagal): spec 048, 079, 080, 081, 128, 129, 130, 240, 314 (rincian di Prerequisites tiap spec).
- Volume data 5.001 Client Archived (`PT Volume Uji 0001`…`5001`) lewat skrip seed: spec 301. Foto upload: spec 047, 127.
- State global yang diubah dan dipulihkan: Selection Limit (spec 140, 306), Date Format General Settings (spec 321), permission role "Manage active client" (spec 153), jam server (di atas).
- Environment automation harus terisolasi dari aktivitas pengguna lain.

## Pemetaan env var password aktor (nama lama → kanonik)

Writer memakai nama berbeda untuk akun yang sama. Pemetaan kanonik di bawah memakai prefix `AC_CLIENT_` untuk semua role selain Total Control, karena nama pendek (`AC_RO_PASSWORD`, `AC_DU_PASSWORD`, `AC_GM_PASSWORD`, `AC_DIST_PASSWORD`, `AC_PARTNER_PASSWORD`) sudah dipakai suite lain (ActivityLog, SettingsPrivacyPolicy) untuk akun berbeda; satu nama hanya boleh satu arti (bagian 5 konvensi). `AC_TC_PASSWORD` tetap. Nama berprefix `AC_CLIENT_` yang sudah seragam tidak diubah. Perubahan belum diterapkan ke spec.

| Akun | Nama kanonik | Nama lama (jumlah spec) |
|---|---|---|
| A-02 Read Only (Principal) | `AC_CLIENT_RO_PASSWORD` | `AC_RO_PASSWORD` (5), `AC_READONLY_PASSWORD` (1) |
| A-03 Group Manager Jakarta | `AC_CLIENT_GM_PASSWORD` | `AC_GM_PASSWORD` (3), `AC_GROUPMANAGER_PASSWORD` (5), `AC_GROUP_MANAGER_JAKARTA_PASSWORD` (1) |
| A-04 Active-Read | `AC_CLIENT_ACTIVE_READ_PASSWORD` | `AC_ACTIVEREAD_PASSWORD` (1), `AC_ACTIVE_READ_PASSWORD` (1) |
| A-05 Active-Create-Only | `AC_CLIENT_ACTIVE_CREATE_PASSWORD` | `AC_ACTIVECREATE_PASSWORD` (2) |
| A-06 Active-Update-Only | `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` | `AC_ACTIVEUPDATE_PASSWORD` (6), `AC_ACTIVE_UPDATE_PASSWORD` (1) |
| A-07 Active-Delete-Only | `AC_CLIENT_ACTIVE_DELETE_PASSWORD` | `AC_ACTIVEDELETE_PASSWORD` (5) |
| A-08 Archived-Read | `AC_CLIENT_ARCHIVED_READ_PASSWORD` | `AC_ARCHREAD_PASSWORD` (1), `AC_ARCHIVEDREAD_PASSWORD` (2) |
| A-09 Archived-Update-Only | `AC_CLIENT_ARCHIVED_UPDATE_PASSWORD` | `AC_ARCHIVEDUPDATE_PASSWORD` (2) |
| A-10 Archived-Delete-Only | `AC_CLIENT_ARCHIVED_DELETE_PASSWORD` | `AC_ARCHIVEDDELETE_PASSWORD` (5) |
| A-13 Distributor Total Control (PT Distribusi Nusantara) | `AC_CLIENT_DIST_TC_PASSWORD` | `AC_DIST_PASSWORD` (5), `AC_DIST_TC_PASSWORD` (3), `AC_DISTRIBUTOR_PASSWORD` (3), `AC_DISTRIBUTOR_TC_PASSWORD` (2), `AC_DISTRIBUTORTC_PASSWORD` (1), `AC_TOTAL_CONTROL_DISTRIBUTOR_PASSWORD` (2) |
| A-14 Partner Total Control (CV Mitra Sejati) | `AC_CLIENT_PARTNER_TC_PASSWORD` | `AC_PARTNER_PASSWORD` (5), `AC_PARTNER_TC_PASSWORD` (4), `AC_PARTNERTC_PASSWORD` (1), `AC_TOTAL_CONTROL_PARTNER_PASSWORD` (1) |
| A-15 Active-Full | `AC_CLIENT_ACTIVE_FULL_PASSWORD` | `AC_ACTIVEFULL_PASSWORD` (42), `AC_ACTIVE_FULL_PASSWORD` (9), `AC_ACTFULL_PASSWORD` (3), `AC_ACTIVE_FULL_JAKARTA_PASSWORD` (3) |
| A-16 Client Default User (PT Sejahtera Abadi) | `AC_CLIENT_DEFAULT_USER_PASSWORD` | `AC_CLIENTUSER_PASSWORD` (1) |
| A-ROL-3 Default User (Principal) | `AC_CLIENT_DU_PRINCIPAL_PASSWORD` | `AC_DU_PASSWORD` (1) |
| A-ROL-1 Distributor Total Control (PT Distribusi Timur) | `AC_CLIENT_DIST_TIMUR_TC_PASSWORD` | `AC_DIST_TIMUR_TC_PASSWORD` (1) |
| A-AST-1 Partner Total Control (CV Mitra Timur) | `AC_CLIENT_PARTNER_TIMUR_TC_PASSWORD` | `AC_PARTNERTIMUR_PASSWORD` (1), `AC_PARTNER_TIMUR_TC_PASSWORD` (1) |
| Partner Total Control CV Mitra Mandiri (tidak di Pre-setup TC) | `AC_CLIENT_PARTNER_MANDIRI_TC_PASSWORD` | `AC_PARTNERMANDIRI_PASSWORD` (1) |
| A-ROL-9 Active-Read + Allocation-Read | `AC_CLIENT_ACTIVE_READ_ALLOC_READ_PASSWORD` | `AC_ACTREADALLOC_PASSWORD` (1) |
| A-AST-7 Active-Read + Allocation Create/Read | `AC_CLIENT_ACTIVE_READ_ALLOC_JAKARTA_PASSWORD` | `AC_ACTIVE_READ_ALLOCATION_JAKARTA_PASSWORD` (1) |
| A-AST-6 Active-Create + Allocation | `AC_CLIENT_ACTIVE_CREATE_ALLOC_JAKARTA_PASSWORD` | `AC_ACTIVE_CREATE_ALLOCATION_JAKARTA_PASSWORD` (1) |
| A-W3CRE-1 Active-Update + Allocation | `AC_CLIENT_ACTIVE_UPDATE_ALLOC_JAKARTA_PASSWORD` | `AC_ACTIVE_UPDATE_ALLOCATION_JAKARTA_PASSWORD` (1) |
| Active-Full kedua (tidak di Pre-setup TC) | `AC_CLIENT_ACTIVE_FULL_B_PASSWORD` | `AC_ACTIVE_FULL_B_PASSWORD` (1) |
| Total Control tenant tanpa riwayat Changelog (tidak di Pre-setup TC) | `AC_CLIENT_TC_EMPTY_TENANT_PASSWORD` | `AC_TC_EMPTY_TENANT_PASSWORD` (1) |
| A-LIF-1 Client Default User (PT Berbagi Pengguna) | `AC_CLIENT_LIF1_PASSWORD` | `AC_LIF1_PASSWORD` (1) |
| A-LIF-2 Client Default User (PT Pengguna Tunggal) | `AC_CLIENT_LIF2_PASSWORD` | `AC_LIF2_PASSWORD` (1) |
| A-LIF-3 Client Default User (PT Suspend Tanpa Produk) | `AC_CLIENT_LIF3_PASSWORD` | `AC_LIF3_PASSWORD` (1), `AC_CLIENT_DEFAULT_USER_SUSPEND_TANPA_PRODUK_PASSWORD` (1) |
| A-W3LIF-1 Client Default User (PT Ditahan Uji Cabut) | `AC_CLIENT_W3LIF1_PASSWORD` | `AC_W3LIF1_PASSWORD` (1) |
| A-DTL-1 Client Default User (PT Uji Top-up) | `AC_CLIENT_TOPUP_DU_PASSWORD` | `AC_TOPUP_DU_PASSWORD` (2) |
| A-DTL-2 Client Default User (PT Uji Tabel Detail) | `AC_CLIENT_UTD_DU_PASSWORD` | `AC_UTD_DU_PASSWORD` (1) |

## Selisih dengan keputusan modul lain

- **D-008 (Setup Column berlaku setelah `[Save]`, modul Privacy Policy):** TC Client (mis. TC-AC-ACC-743 sampai 746, 821, 825) meminta kolom yang di-uncheck langsung hilang dari tabel di balik modal sebelum `[Save]`. Diputuskan user 2026-11-02: spec Setup Column Client mengikuti D-008 (tabel di balik popup tidak berubah sampai `[Save]`; tutup tanpa Save membuang perubahan). Spec yang berubah: 245, 256 (Notes), 257, 258, 260, 294, 295, 296, 297; selisih TC dicatat di Temuan untuk QA spec tersebut (TC tidak diubah).
- **D-015 (URL langsung tanpa capability diarahkan ke halaman no-access, tanpa toast):** TC-AC-ACC-42, 43, 44, 60, 951, 952 dan PRD Client §9.3 meminta toast `You don't have permission to do this.` tanpa redirect. Diputuskan user 2026-11-02: spec mengikuti D-015 (menggantikan pilihan Q1 sebelumnya): URL langsung tanpa capability diasersi sebagai halaman no-access tampil, tanpa toast, tanpa data Client; toast untuk aksi ditolak di halaman yang boleh dibuka tidak berubah. Spec yang berubah: 025, 026 (TC-951), 027; selisih TC dicatat di Temuan untuk QA spec tersebut (TC tidak diubah).

## Temuan untuk QA (terkonsolidasi)

Sumber: butir "Temuan untuk QA" di `## Notes` tiap spec (492 butir dari 270 spec; 1 butir "tidak ada temuan baru" tidak dihitung). Pengelompokan otomatis berdasarkan kata kunci; teks lengkap ada di Notes spec yang dirujuk. Format rujukan: nomor spec (nomor TC).

| Kategori | Butir | Rujukan |
|---|:---:|---|
| A. Selisih dengan keputusan modul lain (D-008 diputuskan user 2026-11-02: spec mengikuti D-008; D-015 diputuskan user 2026-11-02: spec 025, 026, 027 mengikuti D-015) | 10 | 025; 026; 027; 245 (TC 825); 256 (TC 741, 742); 257 (TC 743); 258 (TC 744); 260 (TC 746); 294 (TC 695, 696, 697); 295 (TC 688) |
| B. Kontradiksi TC, Tabel Data Uji, atau antar-TC | 3 | 188 (TC 1034); 212 (TC 300); 316 (TC 443) |
| C. Post Condition tanpa langkah observasi (tidak diasersi) | 83 | 006 (TC 11); 007 (TC 18); 045; 046 (TC 117); 047 (TC 123, 943, 966); 057; 059; 060; 061; 062; 075 (TC 540); 076 (TC 534); 077 (TC 154); 114; 118 (TC 185); 122 (TC 255); 123 (TC 608, 609); 127 (TC 231); 141 (TC 602, 603); 149 (TC 218); 171 (TC 233); 172 (TC 239); 173 (TC 798); 174 (TC 241); 178; 179 (TC 275); 180 (TC 279); 181 (TC 610, 611, 612); 182; 183; 184 (TC 263, 267); 185 (TC 264); 186 (TC 268); 187 (TC 937); 189; 190 (TC 285); 191 (TC 301); 194; 195 (TC 270); 196 (TC 272); 197 (TC 283); 198 (TC 758); 199 (TC 998); 200; 201; 202; 203 (TC 813); 204 (TC 284); 205; 206; 207 (TC 292); 208; 209; 210; 211; 213; 214; 215 (TC 818); 217; 218 (TC 853, 854); 219; 220 (TC 826); 221 (TC 243); 222 (TC 244); 223 (TC 1006, 1032); 224 (TC 1035); 225; 226; 227 (TC 1008); 228 (TC 890, 891); 229; 230 (TC 242); 232 (TC 892, 893); 234 (TC 315, 316); 236 (TC 614, 616); 238 (TC 328); 239 (TC 330); 249 (TC 334); 270 (TC 910, 911); 271 (TC 425, 429); 273 (TC 432); 282 (TC 930); 305 (TC 676) |
| D. Cara, endpoint, atau kemampuan teknis tidak disebut TC (seeding, jam, mail, reset) | 58 | 004 (TC 12); 009 (TC 25, 26); 015 (TC 559); 020 (TC 871, 872); 022 (TC 879, 887); 036 (TC 452); 045 (TC 119, 501, 502); 047 (TC 162); 049 (TC 507); 055; 066 (TC 161); 069 (TC 152, 474, 472, 473); 079 (TC 959, 976); 080 (TC 973); 081 (TC 977); 111 (TC 595); 113 (TC 179); 119 (TC 188); 120 (TC 663, 664, 167); 121 (TC 251, 254, 249); 131 (TC 183); 134 (TC 455); 136 (TC 642); 139 (TC 213); 142 (TC 195); 143 (TC 192); 144 (TC 229, 230); 151 (TC 225); 152 (TC 1020); 175 (TC 800); 177 (TC 238); 192 (TC 816); 193 (TC 817); 246 (TC 322, 323); 247 (TC 320, 974, 975); 261 (TC 340); 262 (TC 343, 348); 273 (TC 432); 285 (TC 382); 291 (TC 716); 302 (TC 410, 411, 412); 311 (TC 671, 673); 313 (TC 669, 670); 314 (TC 464); 318 (TC 1002, 444); 321 (TC 447); 322 (TC 672); 324 (TC 440, 925); 326 (TC 513, 514); 328 (TC 442) |
| E. Precondition, akun, atau data uji kurang atau tidak tertulis | 51 | 001 (TC 8); 003 (TC 17); 005 (TC 467); 008 (TC 20, 22); 016 (TC 58); 024 (TC 417); 033 (TC 63); 036 (TC 452); 072 (TC 634, 635); 079 (TC 959, 976); 117 (TC 176); 120 (TC 167); 123 (TC 617); 127 (TC 231); 149 (TC 219); 151 (TC 225); 153 (TC 926); 232 (TC 337); 246 (TC 322, 323); 266 (TC 418); 267; 269 (TC 426); 270; 271; 281 (TC 358); 283 (TC 375); 284 (TC 376, 377, 381, 383, 384, 385, 386); 286 (TC 379); 288 (TC 389, 390); 289 (TC 392, 393); 293 (TC 404); 300 (TC 413, 699, 704); 303 (TC 415); 304 (TC 416, 445); 307 (TC 435); 312 (TC 437, 1018); 314 (TC 963, 983); 317 (TC 1000); 318 (TC 1001, 1002); 319 (TC 1003); 320 (TC 446); 325 (TC 509); 327 (TC 441, 511) |
| F. Expected tidak menyebut nilai, wujud, atau jumlah pasti | 111 | 001 (TC 19); 002 (TC 5); 003 (TC 16, 9); 004 (TC 14); 006 (TC 11); 007 (TC 18); 010 (TC 32); 013 (TC 566); 014 (TC 38); 016 (TC 451); 018 (TC 59); 021 (TC 876, 877); 023 (TC 885, 886); 025 (TC 42, 43, 44); 026 (TC 61, 564, 565, 954, 965); 030 (TC 49); 031 (TC 53, 54, 55); 034 (TC 450, 621, 625); 041 (TC 121); 044 (TC 115, 118); 046 (TC 127); 048 (TC 129); 049 (TC 507); 052 (TC 70); 054 (TC 499, 500); 055 (TC 132); 056 (TC 72, 556); 064 (TC 519); 068 (TC 521); 072 (TC 633, 635); 073 (TC 164); 076 (TC 543); 077 (TC 153, 154); 081; 113 (TC 457); 114 (TC 590); 115 (TC 592); 117 (TC 178); 118 (TC 185); 120 (TC 168); 122 (TC 255); 126 (TC 458); 129 (TC 199, 200, 214, 463); 130 (TC 173, 227, 250, 171); 131 (TC 907, 906); 132 (TC 184, 228); 133 (TC 172, 252, 962, 201, 232, 181); 134 (TC 653, 654, 655, 465); 135 (TC 190, 194); 136 (TC 641); 137 (TC 203, 204, 217); 145 (TC 196, 197); 150 (TC 224); 151 (TC 222); 153 (TC 926); 176 (TC 237); 231 (TC 314, 338, 309); 237 (TC 905, 336); 238 (TC 326, 324); 239 (TC 331, 329); 240 (TC 319); 241 (TC 311, 789); 242 (TC 312); 243 (TC 313); 244 (TC 845); 245 (TC 821); 248 (TC 903, 904); 250 (TC 354); 252 (TC 731); 253 (TC 735); 254 (TC 355); 256 (TC 858); 259 (TC 745); 262 (TC 343, 348, 353); 263 (TC 1012, 1023); 264 (TC 1013, 1017); 266 (TC 419, 420, 913, 914); 267 (TC 421, 422); 268 (TC 423, 424); 271 (TC 429); 281 (TC 362, 373); 289 (TC 391); 302 (TC 412); 304 (TC 445); 307 (TC 435); 309 (TC 436, 433, 434); 310 (TC 1028); 311 (TC 438, 674, 675); 322 (TC 994); 329 (TC 1036, 1038) |
| G. Lain-lain (TC tumpang tindih, ruang lingkup tidak dinyatakan, nilai diturunkan dari tabel) | 176 | 001 (TC 1); 002 (TC 6); 005 (TC 467); 010 (TC 27, 28, 32); 011 (TC 557); 012 (TC 40); 013 (TC 558); 015 (TC 570); 016 (TC 58, 576); 017 (TC 567, 928); 020 (TC 39); 022 (TC 879); 023 (TC 886); 024 (TC 417, 862, 863); 025 (TC 453, 44); 026 (TC 954); 028 (TC 45, 46, 581); 029 (TC 578, 579, 580, 56); 030 (TC 51); 032 (TC 47); 034 (TC 621, 622); 035 (TC 987, 454); 036 (TC 452); 042 (TC 479, 480); 043 (TC 503, 78, 495, 85, 493, 494); 044 (TC 113); 047; 050 (TC 485); 051 (TC 750); 052 (TC 67, 70); 053 (TC 476, 478); 055 (TC 131, 134); 056 (TC 72); 057; 058 (TC 69); 060 (TC 126); 063 (TC 156, 159, 948); 065 (TC 888, 889); 066 (TC 1007); 067 (TC 144, 148, 523); 068 (TC 522); 069 (TC 150); 070 (TC 141, 139, 140); 071 (TC 469); 073 (TC 155); 074 (TC 163, 636, 637); 077 (TC 153, 154); 078 (TC 754); 080 (TC 973); 082 (TC 112); 111 (TC 174); 112 (TC 180); 114 (TC 591, 594); 115 (TC 182); 116 (TC 175); 118 (TC 185); 119 (TC 627); 122 (TC 255); 124 (TC 647, 648); 125 (TC 666); 126 (TC 458); 128 (TC 967, 968, 908); 129 (TC 199, 463); 131; 132; 133; 134 (TC 465); 135 (TC 191); 137 (TC 203, 204); 138 (TC 208, 209); 140 (TC 205, 206); 142 (TC 195); 143 (TC 192, 644); 146 (TC 187, 961); 147 (TC 643, 645); 148 (TC 462); 149 (TC 219); 150 (TC 223, 656); 153 (TC 628); 216 (TC 849); 231 (TC 310); 232 (TC 306); 233 (TC 305, 317); 234 (TC 315, 318); 235 (TC 899, 897); 237 (TC 335); 240 (TC 855); 242 (TC 790); 244 (TC 846); 246 (TC 900); 248 (TC 903); 250 (TC 722, 339, 341); 251 (TC 726, 727, 723); 252 (TC 344); 253 (TC 734, 735); 254 (TC 349); 255 (TC 739, 740); 257 (TC 743); 258 (TC 744); 261 (TC 345, 350); 265 (TC 1040); 266 (TC 430); 268 (TC 999); 270 (TC 427); 272 (TC 431, 999); 281 (TC 364, 360); 283 (TC 707); 284 (TC 376, 386); 290 (TC 686, 405); 291 (TC 716); 292 (TC 986, 397); 294 (TC 408, 407); 298 (TC 692, 693); 299 (TC 414, 701); 301 (TC 935); 303 (TC 719, 720); 306 (TC 448); 308 (TC 684, 685); 309 (TC 434); 313 (TC 964); 314 (TC 983); 315 (TC 449, 667); 319 (TC 1003); 322 (TC 994); 323 (TC 924, 988); 324 (TC 440, 925); 325 (TC 517); 326 (TC 510, 515); 328 (TC 518) |

Butir yang paling berdampak (kontradiksi dan selisih keputusan):

- Spec 188: TC-1034 Precondition dan Langkah menyebut "PT Trial Habis Tanpa Paid" berstatus Active dan memakai sub-tab Active, sedangkan Tabel A3 (C-FX18-2) menyatakan Client berstatus Archived ("Client otomatis Archived"); spec mengikuti Langkah TC (sub-tab `Active`) dan kontradiksi ini perlu dikonfirmasi QA. Post Condition seluruh TC `-` sehingga tidak diasersi.
- Spec 212: TC-300 Expected "Tab Storage tampil; empty state bila tanpa kuota" bertentangan dengan TC-304 (Client yang sama "PT Baru Daftar": Quota Total/Used/Available 0 dan "empty state kuota tidak tampil", hanya Purchase History yang empty state); spec mengikuti TC-304 untuk Quota dan tidak mengasersi frasa bersyarat "empty state bila tanpa kuota". TC-302 Expected hanya "Tidak ada aksi write"; anchor positif adalah Quota yang...
- Spec 316: TC-AC-ACC-443: Precondition `Detail Partner CV Mitra Sejati` bertentangan dengan Tabel A (C-06 sudah Derived dari CV Mitra Sejati sehingga `satu Client Derived terbentuk` tidak dapat diamati). Langkah `Ulangi dengan subscription kedua` tanpa data. Expected `Default User dipakai bersama` tidak punya langkah cek; spec memakai section Default User di Detail Client.
- TC-AC-ACC-999 Expected a (N1 = 0) hanya benar pada run pertama karena Changelog adalah audit trail permanen (spec 268).

## Pertanyaan terbuka

1. D-008: diputuskan user 2026-11-02, spec Setup Column Client mengikuti D-008; tidak ada keputusan tertunda. TC Client masih menulis kolom berubah langsung sebelum `[Save]` (pemilik TC dapat menyesuaikan).
2. D-015: diputuskan user 2026-11-02, spec 025, 026, 027 mengikuti D-015 (halaman no-access tanpa toast); tidak ada keputusan tertunda. Teks/elemen pasti halaman no-access belum tercatat (perlu dari tim FE); Expected TC-42/43/44/60/951/952 dan PRD Client §9.3 masih menulis toast (pemilik TC/PRD dapat menyesuaikan).
3. Penamaan env var: persetujuan pemetaan kanonik `AC_CLIENT_*` di atas (alternatif: nama pendek `AC_<ROLE>_PASSWORD` bila akunnya dikonfirmasi sama dengan suite lain). Tim FE mendaftarkan nama di `spectra.config.ts` dan `.env.example`.
4. Akun yang tidak ada di Pre-setup TC dan disediakan tim FE: Partner Total Control CV Mitra Mandiri (spec 178), Active-Full kedua (spec 247), Total Control tenant tanpa riwayat Changelog (spec 261), Client Default User PT Uji Tabel Detail (spec 177, email bersuffix).
5. Spec mobile 024, 065, 228 memakai `coverage.mobile: automated` walau kolom Automation TC bertanda `Manual Only` (aplikasi native Android); perangkat/emulator disediakan tim FE.
6. TC-AC-ACC-999 di dua spec (268 dan 272) diterima sebagai pengecualian S-05; temuan C2 `check-suite.py` tetap muncul.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-ACC-1 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-2 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-3 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-4 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-5 | TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian | FE+BE |
| TC-AC-ACC-6 | TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian | FE+BE |
| TC-AC-ACC-7 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-8 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-9 | TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | FE+BE |
| TC-AC-ACC-10 | TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | FE+BE |
| TC-AC-ACC-11 | TC-AC-ACC-E2E-006-sel-group-badge-primary-truncate-dan-hover-hierarki | FE+BE |
| TC-AC-ACC-12 | TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-13 | TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-14 | TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-15 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-16 | TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | FE+BE |
| TC-AC-ACC-17 | TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | FE+BE |
| TC-AC-ACC-18 | TC-AC-ACC-E2E-007-sel-pic-name-panjang-tidak-dipotong | FE+BE |
| TC-AC-ACC-19 | TC-AC-ACC-E2E-001-screening-list-tiga-sub-tab-kolom-dan-row-states | FE+BE |
| TC-AC-ACC-20 | TC-AC-ACC-E2E-008-empty-state-genuinely-kosong-tiga-sub-tab | FE+BE |
| TC-AC-ACC-21 | TC-AC-ACC-E2E-008-empty-state-genuinely-kosong-tiga-sub-tab | FE+BE |
| TC-AC-ACC-22 | TC-AC-ACC-E2E-008-empty-state-genuinely-kosong-tiga-sub-tab | FE+BE |
| TC-AC-ACC-23 | TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian | FE+BE |
| TC-AC-ACC-24 | TC-AC-ACC-E2E-002-badge-jumlah-sub-tab-dan-empty-state-hasil-pencarian | FE+BE |
| TC-AC-ACC-25 | TC-AC-ACC-E2E-009-state-loading-dan-error-list-client | FE+BE |
| TC-AC-ACC-26 | TC-AC-ACC-E2E-009-state-loading-dan-error-list-client | FE+BE |
| TC-AC-ACC-27 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-28 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-29 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-30 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-31 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-32 | TC-AC-ACC-E2E-010-sidebar-group-tree-screening-dan-interaksi | FE+BE |
| TC-AC-ACC-33 | TC-AC-ACC-E2E-011-sidebar-group-tree-per-sub-tab-dan-assignment-berbeda | FE+BE |
| TC-AC-ACC-34 | TC-AC-ACC-E2E-011-sidebar-group-tree-per-sub-tab-dan-assignment-berbeda | FE+BE |
| TC-AC-ACC-35 | TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal | FE+BE |
| TC-AC-ACC-36 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-37 | TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati | FE+BE |
| TC-AC-ACC-38 | TC-AC-ACC-E2E-014-pindah-group-distributor-memindahkan-group-client-langsung | FE+BE |
| TC-AC-ACC-39 | TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-40 | TC-AC-ACC-E2E-012-navigasi-detail-dan-retensi-state-list | FE+BE |
| TC-AC-ACC-41 | TC-AC-ACC-E2E-012-navigasi-detail-dan-retensi-state-list | FE+BE |
| TC-AC-ACC-42 | TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | FE+BE |
| TC-AC-ACC-43 | TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | FE+BE |
| TC-AC-ACC-44 | TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | FE+BE |
| TC-AC-ACC-45 | TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | FE+BE |
| TC-AC-ACC-46 | TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | FE+BE |
| TC-AC-ACC-47 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-48 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-49 | TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | FE+BE |
| TC-AC-ACC-50 | TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | FE+BE |
| TC-AC-ACC-51 | TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | FE+BE |
| TC-AC-ACC-52 | TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | FE+BE |
| TC-AC-ACC-53 | TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client | FE+BE |
| TC-AC-ACC-54 | TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client | FE+BE |
| TC-AC-ACC-55 | TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client | FE+BE |
| TC-AC-ACC-56 | TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner | FE+BE |
| TC-AC-ACC-57 | TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | FE+BE |
| TC-AC-ACC-58 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-59 | TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati | FE+BE |
| TC-AC-ACC-60 | TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | FE+BE |
| TC-AC-ACC-61 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-62 | TC-AC-ACC-E2E-033-group-tree-pola-ancestor-disabled-dan-union-multi-node | FE+BE |
| TC-AC-ACC-63 | TC-AC-ACC-E2E-033-group-tree-pola-ancestor-disabled-dan-union-multi-node | FE+BE |
| TC-AC-ACC-64 | TC-AC-ACC-E2E-030-role-matrix-visibilitas-aksi-manage-active-client | FE+BE |
| TC-AC-ACC-65 | TC-AC-ACC-E2E-041-create-screening-popup-cascading-dan-foto-af | FE+BE |
| TC-AC-ACC-66 | TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas | FE+BE |
| TC-AC-ACC-67 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-68 | TC-AC-ACC-E2E-057-create-peran-partner-select-group-milik-partner | FE+BE |
| TC-AC-ACC-69 | TC-AC-ACC-E2E-058-create-peran-distributor-opsi-partner-dan-group-otomatis | FE+BE |
| TC-AC-ACC-70 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-71 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-72 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-73 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-74 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-75 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-76 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-77 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-78 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-79 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-80 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-81 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-82 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-83 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-84 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-85 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-86 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-87 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-88 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-89 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-90 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-91 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-92 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-93 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-94 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-95 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-96 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-97 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-98 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-99 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-100 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-101 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-102 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-103 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-104 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-105 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-106 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-107 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-108 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-109 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-110 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-111 | TC-AC-ACC-E2E-082-create-batas-pic-phone-dan-company-name-120-karakter-af | FE+BE |
| TC-AC-ACC-112 | TC-AC-ACC-E2E-082-create-batas-pic-phone-dan-company-name-120-karakter-af | FE+BE |
| TC-AC-ACC-113 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-114 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-115 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-116 | TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit | FE+BE |
| TC-AC-ACC-117 | TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit | FE+BE |
| TC-AC-ACC-118 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-119 | TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas | FE+BE |
| TC-AC-ACC-120 | TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit | FE+BE |
| TC-AC-ACC-121 | TC-AC-ACC-E2E-041-create-screening-popup-cascading-dan-foto-af | FE+BE |
| TC-AC-ACC-122 | TC-AC-ACC-E2E-041-create-screening-popup-cascading-dan-foto-af | FE+BE |
| TC-AC-ACC-123 | TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af | FE+BE |
| TC-AC-ACC-124 | TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant | FE+BE |
| TC-AC-ACC-125 | TC-AC-ACC-E2E-060-create-peran-active-create-only-tree-exact-match-dan-sukses | FE+BE |
| TC-AC-ACC-126 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-127 | TC-AC-ACC-E2E-046-create-sukses-af-normalisasi-input-pakai-ulang-dan-double-submit | FE+BE |
| TC-AC-ACC-128 | TC-AC-ACC-E2E-048-create-resilience-af-5xx-dan-geodata | FE+BE |
| TC-AC-ACC-129 | TC-AC-ACC-E2E-048-create-resilience-af-5xx-dan-geodata | FE+BE |
| TC-AC-ACC-130 | TC-AC-ACC-E2E-049-create-resilience-group-dihapus-dan-transaksi-atomik-tcp | FE+BE |
| TC-AC-ACC-131 | TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | FE+BE |
| TC-AC-ACC-132 | TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | FE+BE |
| TC-AC-ACC-133 | TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | FE+BE |
| TC-AC-ACC-134 | TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | FE+BE |
| TC-AC-ACC-135 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-136 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-137 | TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp | FE+BE |
| TC-AC-ACC-138 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-139 | TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | FE+BE |
| TC-AC-ACC-140 | TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | FE+BE |
| TC-AC-ACC-141 | TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | FE+BE |
| TC-AC-ACC-142 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-143 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-144 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-145 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-146 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-147 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-148 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-149 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-150 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-151 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-152 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-153 | TC-AC-ACC-E2E-077-edit-activation-email-ke-inbox-baru-tautan-lama-dan-term-pertama-tcp | FE+BE |
| TC-AC-ACC-154 | TC-AC-ACC-E2E-077-edit-activation-email-ke-inbox-baru-tautan-lama-dan-term-pertama-tcp | FE+BE |
| TC-AC-ACC-155 | TC-AC-ACC-E2E-073-edit-resilience-5xx-dan-email-service-gagal-af | FE+BE |
| TC-AC-ACC-156 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-157 | TC-AC-ACC-E2E-062-edit-client-archived-peran-archived-update-dan-read | FE+BE |
| TC-AC-ACC-158 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-159 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-160 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-161 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-162 | TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af | FE+BE |
| TC-AC-ACC-163 | TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af | FE+BE |
| TC-AC-ACC-164 | TC-AC-ACC-E2E-073-edit-resilience-5xx-dan-email-service-gagal-af | FE+BE |
| TC-AC-ACC-165 | TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | FE+BE |
| TC-AC-ACC-166 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-167 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-168 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-169 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-170 | TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | FE+BE |
| TC-AC-ACC-171 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-172 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-173 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-174 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-175 | TC-AC-ACC-E2E-116-change-partner-tambah-partner-principal-double-klik | FE+BE |
| TC-AC-ACC-176 | TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag | FE+BE |
| TC-AC-ACC-177 | TC-AC-ACC-E2E-118-change-partner-partner-terakhir-dan-ganti-partner-plan-owner | FE+BE |
| TC-AC-ACC-178 | TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag | FE+BE |
| TC-AC-ACC-179 | TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag | FE+BE |
| TC-AC-ACC-180 | TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes | FE+BE |
| TC-AC-ACC-181 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-182 | TC-AC-ACC-E2E-115-change-partner-oleh-distributor | FE+BE |
| TC-AC-ACC-183 | TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | FE+BE |
| TC-AC-ACC-184 | TC-AC-ACC-E2E-132-defense-client-derived-request-langsung | FE+BE |
| TC-AC-ACC-185 | TC-AC-ACC-E2E-118-change-partner-partner-terakhir-dan-ganti-partner-plan-owner | FE+BE |
| TC-AC-ACC-186 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-187 | TC-AC-ACC-E2E-146-dua-sesi-konflik-change-partner-dan-delete | FE+BE |
| TC-AC-ACC-188 | TC-AC-ACC-E2E-119-change-partner-kondisi-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-189 | TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | FE+BE |
| TC-AC-ACC-190 | TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | FE+BE |
| TC-AC-ACC-191 | TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | FE+BE |
| TC-AC-ACC-192 | TC-AC-ACC-E2E-143-suspend-unsuspend-efek-ke-sesi-user-client | FE+BE |
| TC-AC-ACC-193 | TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | FE+BE |
| TC-AC-ACC-194 | TC-AC-ACC-E2E-135-suspend-unsuspend-dialog-dan-aksi-sukses | FE+BE |
| TC-AC-ACC-195 | TC-AC-ACC-E2E-142-suspend-subscription-tetap-bergulir-ke-expired | FE+BE |
| TC-AC-ACC-196 | TC-AC-ACC-E2E-145-suspend-unsuspend-dua-tab-idempoten | FE+BE |
| TC-AC-ACC-197 | TC-AC-ACC-E2E-145-suspend-unsuspend-dua-tab-idempoten | FE+BE |
| TC-AC-ACC-198 | TC-AC-ACC-E2E-132-defense-client-derived-request-langsung | FE+BE |
| TC-AC-ACC-199 | TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | FE+BE |
| TC-AC-ACC-200 | TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | FE+BE |
| TC-AC-ACC-201 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-202 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-203 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-204 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-205 | TC-AC-ACC-E2E-140-bulk-selection-limit-dan-select-all-lintas-halaman | FE+BE |
| TC-AC-ACC-206 | TC-AC-ACC-E2E-140-bulk-selection-limit-dan-select-all-lintas-halaman | FE+BE |
| TC-AC-ACC-207 | TC-AC-ACC-E2E-140-bulk-selection-limit-dan-select-all-lintas-halaman | FE+BE |
| TC-AC-ACC-208 | TC-AC-ACC-E2E-138-bulk-suspend-unsuspend-semua-terpilih | FE+BE |
| TC-AC-ACC-209 | TC-AC-ACC-E2E-138-bulk-suspend-unsuspend-semua-terpilih | FE+BE |
| TC-AC-ACC-210 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-211 | TC-AC-ACC-E2E-147-bulk-suspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-212 | TC-AC-ACC-E2E-139-bulk-suspend-client-derived-campuran-dan-blok | FE+BE |
| TC-AC-ACC-213 | TC-AC-ACC-E2E-139-bulk-suspend-client-derived-campuran-dan-blok | FE+BE |
| TC-AC-ACC-214 | TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | FE+BE |
| TC-AC-ACC-215 | TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk | FE+BE |
| TC-AC-ACC-216 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-217 | TC-AC-ACC-E2E-137-bulk-action-bar-seleksi-dan-bulk-suspend-batal | FE+BE |
| TC-AC-ACC-218 | TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | FE+BE |
| TC-AC-ACC-219 | TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | FE+BE |
| TC-AC-ACC-220 | TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | FE+BE |
| TC-AC-ACC-221 | TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | FE+BE |
| TC-AC-ACC-222 | TC-AC-ACC-E2E-151-delete-diblok-subscription-ditambahkan-sesi-lain | FE+BE |
| TC-AC-ACC-223 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-224 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-225 | TC-AC-ACC-E2E-151-delete-diblok-subscription-ditambahkan-sesi-lain | FE+BE |
| TC-AC-ACC-226 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-227 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-228 | TC-AC-ACC-E2E-132-defense-client-derived-request-langsung | FE+BE |
| TC-AC-ACC-229 | TC-AC-ACC-E2E-144-delete-efek-ke-sesi-dan-akses-default-user | FE+BE |
| TC-AC-ACC-230 | TC-AC-ACC-E2E-144-delete-efek-ke-sesi-dan-akses-default-user | FE+BE |
| TC-AC-ACC-231 | TC-AC-ACC-E2E-127-delete-client-berfoto-dan-nama-dipakai-ulang | FE+BE |
| TC-AC-ACC-232 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-233 | TC-AC-ACC-E2E-171-screening-header-detail-client-active-full | FE+BE |
| TC-AC-ACC-234 | TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | FE+BE |
| TC-AC-ACC-235 | TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | FE+BE |
| TC-AC-ACC-236 | TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | FE+BE |
| TC-AC-ACC-237 | TC-AC-ACC-E2E-176-client-derived-mengikuti-perubahan-partner-induk | FE+BE |
| TC-AC-ACC-238 | TC-AC-ACC-E2E-177-default-user-detail-mengikuti-perubahan-global-settings | FE+BE |
| TC-AC-ACC-239 | TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | FE+BE |
| TC-AC-ACC-240 | TC-AC-ACC-E2E-172-header-detail-badge-tab-dan-client-derived | FE+BE |
| TC-AC-ACC-241 | TC-AC-ACC-E2E-174-default-user-tanpa-kontrol-nonaktif | FE+BE |
| TC-AC-ACC-242 | TC-AC-ACC-E2E-230-app-access-dan-activation-email-term-pertama-client | FE+BE |
| TC-AC-ACC-243 | TC-AC-ACC-E2E-221-aktivasi-term-pertama-preparing-access-dan-pending-ke-active | FE+BE |
| TC-AC-ACC-244 | TC-AC-ACC-E2E-222-kegagalan-penyediaan-akses-notifikasi-dan-retry-manual | FE+BE |
| TC-AC-ACC-245 | TC-AC-ACC-E2E-221-aktivasi-term-pertama-preparing-access-dan-pending-ke-active | FE+BE |
| TC-AC-ACC-246 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-247 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-248 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-249 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-250 | TC-AC-ACC-E2E-130-resilience-change-partner-resend-byo-dan-delete | FE+BE |
| TC-AC-ACC-251 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-252 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-253 | TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | FE+BE |
| TC-AC-ACC-254 | TC-AC-ACC-E2E-121-toggle-byo-dialog-apply-dan-default | FE+BE |
| TC-AC-ACC-255 | TC-AC-ACC-E2E-122-toggle-byo-disabled-aktivasi-jalur-b-ditolak | FE+BE |
| TC-AC-ACC-256 | TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | FE+BE |
| TC-AC-ACC-257 | TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | FE+BE |
| TC-AC-ACC-258 | TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | FE+BE |
| TC-AC-ACC-259 | TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | FE+BE |
| TC-AC-ACC-260 | TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort | FE+BE |
| TC-AC-ACC-261 | TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort | FE+BE |
| TC-AC-ACC-262 | TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort | FE+BE |
| TC-AC-ACC-263 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-264 | TC-AC-ACC-E2E-185-tab-subscription-feature-entitlement-source-plan | FE+BE |
| TC-AC-ACC-265 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-266 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-267 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-268 | TC-AC-ACC-E2E-186-tab-subscription-details-status-term-aktif-sampai-expired | FE+BE |
| TC-AC-ACC-269 | TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals | FE+BE |
| TC-AC-ACC-270 | TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals | FE+BE |
| TC-AC-ACC-271 | TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals | FE+BE |
| TC-AC-ACC-272 | TC-AC-ACC-E2E-196-tab-subscription-empty-state-nol-kuota-dan-term-archive | FE+BE |
| TC-AC-ACC-273 | TC-AC-ACC-E2E-196-tab-subscription-empty-state-nol-kuota-dan-term-archive | FE+BE |
| TC-AC-ACC-274 | TC-AC-ACC-E2E-196-tab-subscription-empty-state-nol-kuota-dan-term-archive | FE+BE |
| TC-AC-ACC-275 | TC-AC-ACC-E2E-179-isolasi-tab-subscription-partner-cv-mitra-timur | FE+BE |
| TC-AC-ACC-276 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-277 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-278 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-279 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-280 | TC-AC-ACC-E2E-197-purchase-history-license-screening-download-dan-filter-panel | FE+BE |
| TC-AC-ACC-281 | TC-AC-ACC-E2E-198-purchase-history-license-search-semua-kolom | FE+BE |
| TC-AC-ACC-282 | TC-AC-ACC-E2E-197-purchase-history-license-screening-download-dan-filter-panel | FE+BE |
| TC-AC-ACC-283 | TC-AC-ACC-E2E-197-purchase-history-license-screening-download-dan-filter-panel | FE+BE |
| TC-AC-ACC-284 | TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-285 | TC-AC-ACC-E2E-190-total-quota-qr-tab-tag-dari-asset-license-term | FE+BE |
| TC-AC-ACC-286 | TC-AC-ACC-E2E-191-quota-detail-mengikuti-perubahan-fams-asset-tag-dan-storage | FE+BE |
| TC-AC-ACC-287 | TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-288 | TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-289 | TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-290 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-291 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-292 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-293 | TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort | FE+BE |
| TC-AC-ACC-294 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-295 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-296 | TC-AC-ACC-E2E-209-purchase-history-hardware-screening-filter-dan-download | FE+BE |
| TC-AC-ACC-297 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-298 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-299 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-300 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-301 | TC-AC-ACC-E2E-191-quota-detail-mengikuti-perubahan-fams-asset-tag-dan-storage | FE+BE |
| TC-AC-ACC-302 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-303 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-304 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-305 | TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader | FE+BE |
| TC-AC-ACC-306 | TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | FE+BE |
| TC-AC-ACC-307 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-308 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-309 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-310 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-311 | TC-AC-ACC-E2E-241-search-station-list-kolom-teks-dan-numerik | FE+BE |
| TC-AC-ACC-312 | TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | FE+BE |
| TC-AC-ACC-313 | TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | FE+BE |
| TC-AC-ACC-314 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-315 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-316 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-317 | TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader | FE+BE |
| TC-AC-ACC-318 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-319 | TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog | FE+BE |
| TC-AC-ACC-320 | TC-AC-ACC-E2E-247-dua-admin-generate-bersamaan-dan-aksi-basi-409 | FE+BE |
| TC-AC-ACC-321 | TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit | FE+BE |
| TC-AC-ACC-322 | TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat | FE+BE |
| TC-AC-ACC-323 | TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat | FE+BE |
| TC-AC-ACC-324 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-325 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-326 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-327 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-328 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-329 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-330 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-331 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-332 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-333 | TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog | FE+BE |
| TC-AC-ACC-334 | TC-AC-ACC-E2E-249-deactivate-station-admin-console-tampil-di-global-settings-hardware | FE+BE |
| TC-AC-ACC-335 | TC-AC-ACC-E2E-237-defense-aksi-asset-control-client-archived-suspended-dan-role-read | FE+BE |
| TC-AC-ACC-336 | TC-AC-ACC-E2E-237-defense-aksi-asset-control-client-archived-suspended-dan-role-read | FE+BE |
| TC-AC-ACC-337 | TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | FE+BE |
| TC-AC-ACC-338 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-339 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-340 | TC-AC-ACC-E2E-261-modal-changelog-empty-state-genuinely-kosong-dan-hasil-search-kosong | FE+BE |
| TC-AC-ACC-341 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-342 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-343 | TC-AC-ACC-E2E-262-modal-changelog-auto-refresh-diam-diam-lewat-sse | FE+BE |
| TC-AC-ACC-344 | TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download | FE+BE |
| TC-AC-ACC-345 | TC-AC-ACC-E2E-261-modal-changelog-empty-state-genuinely-kosong-dan-hasil-search-kosong | FE+BE |
| TC-AC-ACC-346 | TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download | FE+BE |
| TC-AC-ACC-347 | TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download | FE+BE |
| TC-AC-ACC-348 | TC-AC-ACC-E2E-262-modal-changelog-auto-refresh-diam-diam-lewat-sse | FE+BE |
| TC-AC-ACC-349 | TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-350 | TC-AC-ACC-E2E-261-modal-changelog-empty-state-genuinely-kosong-dan-hasil-search-kosong | FE+BE |
| TC-AC-ACC-351 | TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-352 | TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-353 | TC-AC-ACC-E2E-262-modal-changelog-auto-refresh-diam-diam-lewat-sse | FE+BE |
| TC-AC-ACC-354 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-355 | TC-AC-ACC-E2E-254-modal-changelog-asset-control-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-356 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-357 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-358 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-359 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-360 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-361 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-362 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-363 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-364 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-365 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-366 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-367 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-368 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-369 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-370 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-371 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-372 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-373 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-374 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-375 | TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown | FE+BE |
| TC-AC-ACC-376 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-377 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-378 | TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-379 | TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-380 | TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-381 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-382 | TC-AC-ACC-E2E-285-filter-last-updated-rentang-tanggal | FE+BE |
| TC-AC-ACC-383 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-384 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-385 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-386 | TC-AC-ACC-E2E-284-filter-hasil-per-field-partner-distributor-modified-by-lokasi | FE+BE |
| TC-AC-ACC-387 | TC-AC-ACC-E2E-286-filter-status-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-388 | TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown | FE+BE |
| TC-AC-ACC-389 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-390 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-391 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-392 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-393 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-394 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-395 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-396 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-397 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-398 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-399 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-400 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-401 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-402 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-403 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-404 | TC-AC-ACC-E2E-293-sort-tujuh-kolom-hidden-default | FE+BE |
| TC-AC-ACC-405 | TC-AC-ACC-E2E-290-distributor-filter-sort-sel-tanda-hubung | FE+BE |
| TC-AC-ACC-406 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-407 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-408 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-409 | TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | FE+BE |
| TC-AC-ACC-410 | TC-AC-ACC-E2E-302-download-gagal-toast-error-resilience | FE+BE |
| TC-AC-ACC-411 | TC-AC-ACC-E2E-302-download-gagal-toast-error-resilience | FE+BE |
| TC-AC-ACC-412 | TC-AC-ACC-E2E-302-download-gagal-toast-error-resilience | FE+BE |
| TC-AC-ACC-413 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-414 | TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | FE+BE |
| TC-AC-ACC-415 | TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan | FE+BE |
| TC-AC-ACC-416 | TC-AC-ACC-E2E-304-sse-real-time-list-terfilter-dan-detail | FE+BE |
| TC-AC-ACC-417 | TC-AC-ACC-E2E-024-mobile-list-toolbar-card-dan-bottom-sheet-aksi | FE+BE |
| TC-AC-ACC-418 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-419 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-420 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-421 | TC-AC-ACC-E2E-267-pencatatan-log-suspend-unsuspend-dan-bulk-suspend-di-tiga-surface | FE+BE |
| TC-AC-ACC-422 | TC-AC-ACC-E2E-267-pencatatan-log-suspend-unsuspend-dan-bulk-suspend-di-tiga-surface | FE+BE |
| TC-AC-ACC-423 | TC-AC-ACC-E2E-268-pencatatan-log-aksi-sistem-auto-archive-auto-reactivate-dan-send-activation-email | FE+BE |
| TC-AC-ACC-424 | TC-AC-ACC-E2E-268-pencatatan-log-aksi-sistem-auto-archive-auto-reactivate-dan-send-activation-email | FE+BE |
| TC-AC-ACC-425 | TC-AC-ACC-E2E-271-pencatatan-log-delete-client-dan-pencabutan-app-access | FE+BE |
| TC-AC-ACC-426 | TC-AC-ACC-E2E-269-pencatatan-log-resend-activation-email-dan-toggle-byo-di-tiga-surface | FE+BE |
| TC-AC-ACC-427 | TC-AC-ACC-E2E-270-pencatatan-log-generate-enrollment-qr-deactivate-station-dan-revoke-tablet-di-tiga-surface | FE+BE |
| TC-AC-ACC-428 | TC-AC-ACC-E2E-269-pencatatan-log-resend-activation-email-dan-toggle-byo-di-tiga-surface | FE+BE |
| TC-AC-ACC-429 | TC-AC-ACC-E2E-271-pencatatan-log-delete-client-dan-pencabutan-app-access | FE+BE |
| TC-AC-ACC-430 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-431 | TC-AC-ACC-E2E-272-absence-log-aksi-tanpa-perubahan-dan-aksi-sistem-tanpa-system-log | FE+BE |
| TC-AC-ACC-432 | TC-AC-ACC-E2E-273-modified-by-snapshot-nama-aktor-saat-aksi | FE+BE |
| TC-AC-ACC-433 | TC-AC-ACC-E2E-309-auto-archive-via-cancel-term-terakhir | FE+BE |
| TC-AC-ACC-434 | TC-AC-ACC-E2E-309-auto-archive-via-cancel-term-terakhir | FE+BE |
| TC-AC-ACC-435 | TC-AC-ACC-E2E-307-race-auto-archive-term-baru-saat-evaluasi | FE+BE |
| TC-AC-ACC-436 | TC-AC-ACC-E2E-309-auto-archive-via-cancel-term-terakhir | FE+BE |
| TC-AC-ACC-437 | TC-AC-ACC-E2E-312-auto-reactivate-client-archived | FE+BE |
| TC-AC-ACC-438 | TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | FE+BE |
| TC-AC-ACC-439 | TC-AC-ACC-E2E-323-role-matrix-onboarding-opsi-new-client-tampil | FE+BE |
| TC-AC-ACC-440 | TC-AC-ACC-E2E-324-role-matrix-onboarding-opsi-new-client-tidak-tampil-dan-bypass-ditolak | FE+BE |
| TC-AC-ACC-441 | TC-AC-ACC-E2E-327-onboarding-form-inline-per-aktor-partner-distributor-active-full | FE+BE |
| TC-AC-ACC-442 | TC-AC-ACC-E2E-328-resilience-onboarding-geodata-dan-submit-5xx | FE+BE |
| TC-AC-ACC-443 | TC-AC-ACC-E2E-316-add-own-subscription-client-derived | FE+BE |
| TC-AC-ACC-444 | TC-AC-ACC-E2E-318-entitas-induk-partner-delete | FE+BE |
| TC-AC-ACC-445 | TC-AC-ACC-E2E-304-sse-real-time-list-terfilter-dan-detail | FE+BE |
| TC-AC-ACC-446 | TC-AC-ACC-E2E-320-change-partner-tercermin-di-tab-client-partner | FE+BE |
| TC-AC-ACC-447 | TC-AC-ACC-E2E-321-format-tanggal-general-settings-pada-list-detail-changelog | FE+BE |
| TC-AC-ACC-448 | TC-AC-ACC-E2E-306-selection-limit-mengikuti-system-limits-terbaru | FE+BE |
| TC-AC-ACC-449 | TC-AC-ACC-E2E-315-approval-term-pertama-dan-notifikasi-requester | FE+BE |
| TC-AC-ACC-450 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-451 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-452 | TC-AC-ACC-E2E-036-defense-injeksi-script-pada-address-client-disanitasi | FE+BE |
| TC-AC-ACC-453 | TC-AC-ACC-E2E-025-role-matrix-negatif-menu-client-tersembunyi-dan-url-ditolak | FE+BE |
| TC-AC-ACC-454 | TC-AC-ACC-E2E-035-defense-tulis-langsung-di-luar-scope-group-ditolak-404 | FE+BE |
| TC-AC-ACC-455 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-456 | TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag | FE+BE |
| TC-AC-ACC-457 | TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag | FE+BE |
| TC-AC-ACC-458 | TC-AC-ACC-E2E-126-double-klik-konfirmasi-lintas-aksi-tulis | FE+BE |
| TC-AC-ACC-459 | TC-AC-ACC-E2E-174-default-user-tanpa-kontrol-nonaktif | FE+BE |
| TC-AC-ACC-460 | TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | FE+BE |
| TC-AC-ACC-461 | TC-AC-ACC-E2E-148-bulk-unsuspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-462 | TC-AC-ACC-E2E-148-bulk-unsuspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-463 | TC-AC-ACC-E2E-129-resilience-suspend-unsuspend-gs-dan-5xx | FE+BE |
| TC-AC-ACC-464 | TC-AC-ACC-E2E-314-activation-email-dan-penyediaan-akses-gagal | FE+BE |
| TC-AC-ACC-465 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-466 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-467 | TC-AC-ACC-E2E-005-badge-produk-client-active-term-terakhir-archive | FE+BE |
| TC-AC-ACC-468 | TC-AC-ACC-E2E-207-tab-hardware-screening-hardware-list-dan-empty-state | FE+BE |
| TC-AC-ACC-469 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-470 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-471 | TC-AC-ACC-E2E-204-tab-tag-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-472 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-473 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-474 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-475 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |
| TC-AC-ACC-476 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |
| TC-AC-ACC-477 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |
| TC-AC-ACC-478 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |
| TC-AC-ACC-479 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-480 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-481 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-482 | TC-AC-ACC-E2E-058-create-peran-distributor-opsi-partner-dan-group-otomatis | FE+BE |
| TC-AC-ACC-483 | TC-AC-ACC-E2E-058-create-peran-distributor-opsi-partner-dan-group-otomatis | FE+BE |
| TC-AC-ACC-484 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-485 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-486 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-487 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-488 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-489 | TC-AC-ACC-E2E-050-create-screening-opsi-partner-dan-select-group-tcp | FE+BE |
| TC-AC-ACC-490 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-491 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-492 | TC-AC-ACC-E2E-055-create-efek-lanjutan-default-user-division-position-dan-log-tcp | FE+BE |
| TC-AC-ACC-493 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-494 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-495 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-496 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-497 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-498 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-499 | TC-AC-ACC-E2E-054-create-pakai-ulang-client-code-dan-email-client-dihapus-tcp | FE+BE |
| TC-AC-ACC-500 | TC-AC-ACC-E2E-054-create-pakai-ulang-client-code-dan-email-client-dihapus-tcp | FE+BE |
| TC-AC-ACC-501 | TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas | FE+BE |
| TC-AC-ACC-502 | TC-AC-ACC-E2E-045-create-sukses-af-partner-dan-email-lintas-entitas | FE+BE |
| TC-AC-ACC-503 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-504 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-505 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-506 | TC-AC-ACC-E2E-043-create-validasi-karakter-dan-timing-af | FE+BE |
| TC-AC-ACC-507 | TC-AC-ACC-E2E-049-create-resilience-group-dihapus-dan-transaksi-atomik-tcp | FE+BE |
| TC-AC-ACC-508 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-509 | TC-AC-ACC-E2E-325-onboarding-screening-form-inline-dan-validasi-duplikat | FE+BE |
| TC-AC-ACC-510 | TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan | FE+BE |
| TC-AC-ACC-511 | TC-AC-ACC-E2E-327-onboarding-form-inline-per-aktor-partner-distributor-active-full | FE+BE |
| TC-AC-ACC-512 | TC-AC-ACC-E2E-327-onboarding-form-inline-per-aktor-partner-distributor-active-full | FE+BE |
| TC-AC-ACC-513 | TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan | FE+BE |
| TC-AC-ACC-514 | TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan | FE+BE |
| TC-AC-ACC-515 | TC-AC-ACC-E2E-326-onboarding-sukses-group-division-pending-dan-pencatatan | FE+BE |
| TC-AC-ACC-516 | TC-AC-ACC-E2E-325-onboarding-screening-form-inline-dan-validasi-duplikat | FE+BE |
| TC-AC-ACC-517 | TC-AC-ACC-E2E-325-onboarding-screening-form-inline-dan-validasi-duplikat | FE+BE |
| TC-AC-ACC-518 | TC-AC-ACC-E2E-328-resilience-onboarding-geodata-dan-submit-5xx | FE+BE |
| TC-AC-ACC-519 | TC-AC-ACC-E2E-064-create-balapan-dua-sesi-company-name-sama | FE+BE |
| TC-AC-ACC-520 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-521 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-522 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-523 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-524 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-525 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-526 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-527 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-528 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-529 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-530 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-531 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-532 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-533 | TC-AC-ACC-E2E-068-edit-validasi-default-user-belum-aktif-dan-clear-field-af | FE+BE |
| TC-AC-ACC-534 | TC-AC-ACC-E2E-076-edit-email-default-user-lintas-entitas-pakai-ulang-dan-tidak-dapat-dinonaktifkan-tcp | FE+BE |
| TC-AC-ACC-535 | TC-AC-ACC-E2E-076-edit-email-default-user-lintas-entitas-pakai-ulang-dan-tidak-dapat-dinonaktifkan-tcp | FE+BE |
| TC-AC-ACC-536 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-537 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-538 | TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp | FE+BE |
| TC-AC-ACC-539 | TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp | FE+BE |
| TC-AC-ACC-540 | TC-AC-ACC-E2E-075-edit-group-client-direct-select-group-wajib-stale-dan-log-tcp | FE+BE |
| TC-AC-ACC-541 | TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant | FE+BE |
| TC-AC-ACC-542 | TC-AC-ACC-E2E-069-edit-division-position-default-user-master-data-af | FE+BE |
| TC-AC-ACC-543 | TC-AC-ACC-E2E-076-edit-email-default-user-lintas-entitas-pakai-ulang-dan-tidak-dapat-dinonaktifkan-tcp | FE+BE |
| TC-AC-ACC-544 | TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af | FE+BE |
| TC-AC-ACC-545 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-546 | TC-AC-ACC-E2E-062-edit-client-archived-peran-archived-update-dan-read | FE+BE |
| TC-AC-ACC-547 | TC-AC-ACC-E2E-062-edit-client-archived-peran-archived-update-dan-read | FE+BE |
| TC-AC-ACC-548 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-549 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-550 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-551 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-552 | TC-AC-ACC-E2E-071-edit-penutupan-popup-esc-backdrop-muat-ulang-dan-back-af | FE+BE |
| TC-AC-ACC-553 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-554 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-555 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-556 | TC-AC-ACC-E2E-056-create-clear-field-dan-penutupan-popup-tcp | FE+BE |
| TC-AC-ACC-557 | TC-AC-ACC-E2E-011-sidebar-group-tree-per-sub-tab-dan-assignment-berbeda | FE+BE |
| TC-AC-ACC-558 | TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal | FE+BE |
| TC-AC-ACC-559 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-560 | TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati | FE+BE |
| TC-AC-ACC-561 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-562 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-563 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-564 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-565 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-566 | TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal | FE+BE |
| TC-AC-ACC-567 | TC-AC-ACC-E2E-017-resolusi-dan-cakupan-client-viewer-distributor-timur | FE+BE |
| TC-AC-ACC-568 | TC-AC-ACC-E2E-019-anchor-dan-group-viewer-partner-mitra-timur | FE+BE |
| TC-AC-ACC-569 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-570 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-571 | TC-AC-ACC-E2E-013-resolusi-group-managed-by-viewer-principal | FE+BE |
| TC-AC-ACC-572 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-573 | TC-AC-ACC-E2E-017-resolusi-dan-cakupan-client-viewer-distributor-timur | FE+BE |
| TC-AC-ACC-574 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-575 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-576 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-577 | TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | FE+BE |
| TC-AC-ACC-578 | TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner | FE+BE |
| TC-AC-ACC-579 | TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner | FE+BE |
| TC-AC-ACC-580 | TC-AC-ACC-E2E-029-role-matrix-visibilitas-aksi-default-user-distributor-partner | FE+BE |
| TC-AC-ACC-581 | TC-AC-ACC-E2E-028-role-matrix-visibilitas-aksi-total-control-dan-read-only | FE+BE |
| TC-AC-ACC-582 | TC-AC-ACC-E2E-032-role-matrix-group-manager-scope-descendant-dan-aksi | FE+BE |
| TC-AC-ACC-583 | TC-AC-ACC-E2E-031-role-matrix-visibilitas-aksi-manage-archived-client | FE+BE |
| TC-AC-ACC-584 | TC-AC-ACC-E2E-060-create-peran-active-create-only-tree-exact-match-dan-sukses | FE+BE |
| TC-AC-ACC-585 | TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant | FE+BE |
| TC-AC-ACC-586 | TC-AC-ACC-E2E-061-edit-peran-active-update-only-sukses-dan-tree-exact-match | FE+BE |
| TC-AC-ACC-587 | TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant | FE+BE |
| TC-AC-ACC-588 | TC-AC-ACC-E2E-061-edit-peran-active-update-only-sukses-dan-tree-exact-match | FE+BE |
| TC-AC-ACC-590 | TC-AC-ACC-E2E-114-change-partner-role-terbatas-tree-select-group-dan-sukses | FE+BE |
| TC-AC-ACC-591 | TC-AC-ACC-E2E-114-change-partner-role-terbatas-tree-select-group-dan-sukses | FE+BE |
| TC-AC-ACC-592 | TC-AC-ACC-E2E-115-change-partner-oleh-distributor | FE+BE |
| TC-AC-ACC-593 | TC-AC-ACC-E2E-115-change-partner-oleh-distributor | FE+BE |
| TC-AC-ACC-594 | TC-AC-ACC-E2E-114-change-partner-role-terbatas-tree-select-group-dan-sukses | FE+BE |
| TC-AC-ACC-595 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-596 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-597 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-598 | TC-AC-ACC-E2E-116-change-partner-tambah-partner-principal-double-klik | FE+BE |
| TC-AC-ACC-599 | TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag | FE+BE |
| TC-AC-ACC-600 | TC-AC-ACC-E2E-117-change-partner-remove-anchor-dan-urutan-drag | FE+BE |
| TC-AC-ACC-601 | TC-AC-ACC-E2E-115-change-partner-oleh-distributor | FE+BE |
| TC-AC-ACC-602 | TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend | FE+BE |
| TC-AC-ACC-603 | TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend | FE+BE |
| TC-AC-ACC-604 | TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend | FE+BE |
| TC-AC-ACC-605 | TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend | FE+BE |
| TC-AC-ACC-606 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-607 | TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo | FE+BE |
| TC-AC-ACC-608 | TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo | FE+BE |
| TC-AC-ACC-609 | TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo | FE+BE |
| TC-AC-ACC-610 | TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription | FE+BE |
| TC-AC-ACC-611 | TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription | FE+BE |
| TC-AC-ACC-612 | TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription | FE+BE |
| TC-AC-ACC-613 | TC-AC-ACC-E2E-181-role-matrix-link-dan-banner-tab-subscription | FE+BE |
| TC-AC-ACC-614 | TC-AC-ACC-E2E-236-role-matrix-positif-update-aksi-asset-control | FE+BE |
| TC-AC-ACC-615 | TC-AC-ACC-E2E-236-role-matrix-positif-update-aksi-asset-control | FE+BE |
| TC-AC-ACC-616 | TC-AC-ACC-E2E-236-role-matrix-positif-update-aksi-asset-control | FE+BE |
| TC-AC-ACC-617 | TC-AC-ACC-E2E-123-role-matrix-positif-resend-dan-toggle-byo | FE+BE |
| TC-AC-ACC-618 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-619 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-620 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-621 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-622 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-623 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-624 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-625 | TC-AC-ACC-E2E-034-defense-tulis-langsung-tanpa-permission-ditolak-server | FE+BE |
| TC-AC-ACC-626 | TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | FE+BE |
| TC-AC-ACC-627 | TC-AC-ACC-E2E-119-change-partner-kondisi-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-628 | TC-AC-ACC-E2E-153-delete-dialog-dan-izin-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-629 | TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-630 | TC-AC-ACC-E2E-004-isi-sel-badge-produk-fams-sams-siem | FE+BE |
| TC-AC-ACC-633 | TC-AC-ACC-E2E-072-edit-activation-email-otomatis-saat-email-default-user-diubah-af | FE+BE |
| TC-AC-ACC-634 | TC-AC-ACC-E2E-072-edit-activation-email-otomatis-saat-email-default-user-diubah-af | FE+BE |
| TC-AC-ACC-635 | TC-AC-ACC-E2E-072-edit-activation-email-otomatis-saat-email-default-user-diubah-af | FE+BE |
| TC-AC-ACC-636 | TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af | FE+BE |
| TC-AC-ACC-637 | TC-AC-ACC-E2E-074-edit-konkurensi-pelaku-kedua-api-last-write-dihapus-suspend-aktivasi-af | FE+BE |
| TC-AC-ACC-638 | TC-AC-ACC-E2E-119-change-partner-kondisi-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-639 | TC-AC-ACC-E2E-116-change-partner-tambah-partner-principal-double-klik | FE+BE |
| TC-AC-ACC-640 | TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk | FE+BE |
| TC-AC-ACC-641 | TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk | FE+BE |
| TC-AC-ACC-642 | TC-AC-ACC-E2E-136-suspend-unsuspend-pengamatan-sub-tab-dan-menu-bulk | FE+BE |
| TC-AC-ACC-643 | TC-AC-ACC-E2E-147-bulk-suspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-644 | TC-AC-ACC-E2E-143-suspend-unsuspend-efek-ke-sesi-user-client | FE+BE |
| TC-AC-ACC-645 | TC-AC-ACC-E2E-147-bulk-suspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-646 | TC-AC-ACC-E2E-148-bulk-unsuspend-state-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-647 | TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk | FE+BE |
| TC-AC-ACC-648 | TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk | FE+BE |
| TC-AC-ACC-649 | TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk | FE+BE |
| TC-AC-ACC-650 | TC-AC-ACC-E2E-124-double-klik-suspend-unsuspend-tunggal-dan-bulk | FE+BE |
| TC-AC-ACC-651 | TC-AC-ACC-E2E-149-delete-client-archived-dialog-validasi-dan-sukses | FE+BE |
| TC-AC-ACC-652 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-653 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-654 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-655 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-656 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-657 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-658 | TC-AC-ACC-E2E-144-delete-efek-ke-sesi-dan-akses-default-user | FE+BE |
| TC-AC-ACC-659 | TC-AC-ACC-E2E-125-double-klik-resend-toggle-byo-dan-delete | FE+BE |
| TC-AC-ACC-660 | TC-AC-ACC-E2E-125-double-klik-resend-toggle-byo-dan-delete | FE+BE |
| TC-AC-ACC-661 | TC-AC-ACC-E2E-186-tab-subscription-details-status-term-aktif-sampai-expired | FE+BE |
| TC-AC-ACC-662 | TC-AC-ACC-E2E-195-perubahan-term-lewat-client-subscription-dan-approvals | FE+BE |
| TC-AC-ACC-663 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-664 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-665 | TC-AC-ACC-E2E-120-resend-activation-email-hidden-dan-sukses | FE+BE |
| TC-AC-ACC-666 | TC-AC-ACC-E2E-125-double-klik-resend-toggle-byo-dan-delete | FE+BE |
| TC-AC-ACC-667 | TC-AC-ACC-E2E-315-approval-term-pertama-dan-notifikasi-requester | FE+BE |
| TC-AC-ACC-668 | TC-AC-ACC-E2E-315-approval-term-pertama-dan-notifikasi-requester | FE+BE |
| TC-AC-ACC-669 | TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server | FE+BE |
| TC-AC-ACC-670 | TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server | FE+BE |
| TC-AC-ACC-671 | TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | FE+BE |
| TC-AC-ACC-672 | TC-AC-ACC-E2E-322-default-user-client-akses-produk-setelah-perubahan-status | FE+BE |
| TC-AC-ACC-673 | TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | FE+BE |
| TC-AC-ACC-674 | TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | FE+BE |
| TC-AC-ACC-675 | TC-AC-ACC-E2E-311-client-suspended-subscription-dan-cancel-predecessor | FE+BE |
| TC-AC-ACC-676 | TC-AC-ACC-E2E-305-sse-multi-tab-unsuspend-sesi-lain | FE+BE |
| TC-AC-ACC-677 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-678 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-679 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-680 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-681 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-682 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-683 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-684 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-685 | TC-AC-ACC-E2E-308-toolbar-ikon-tooltip-dan-aksi-menu-severity | FE+BE |
| TC-AC-ACC-686 | TC-AC-ACC-E2E-290-distributor-filter-sort-sel-tanda-hubung | FE+BE |
| TC-AC-ACC-687 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-688 | TC-AC-ACC-E2E-295-setup-column-centang-kolom-hideable | FE+BE |
| TC-AC-ACC-689 | TC-AC-ACC-E2E-296-setup-column-centang-kolom-curated | FE+BE |
| TC-AC-ACC-690 | TC-AC-ACC-E2E-297-setup-column-drag-and-drop-urutan-kolom | FE+BE |
| TC-AC-ACC-691 | TC-AC-ACC-E2E-297-setup-column-drag-and-drop-urutan-kolom | FE+BE |
| TC-AC-ACC-692 | TC-AC-ACC-E2E-298-setup-column-pin-kolom-membeku-saat-scroll | FE+BE |
| TC-AC-ACC-693 | TC-AC-ACC-E2E-298-setup-column-pin-kolom-membeku-saat-scroll | FE+BE |
| TC-AC-ACC-694 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-695 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-696 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-697 | TC-AC-ACC-E2E-294-column-visibility-overlay-dan-guard-setup-column | FE+BE |
| TC-AC-ACC-698 | TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | FE+BE |
| TC-AC-ACC-699 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-700 | TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | FE+BE |
| TC-AC-ACC-701 | TC-AC-ACC-E2E-299-download-nama-berkas-format-header-kolom | FE+BE |
| TC-AC-ACC-702 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-703 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-704 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-705 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-706 | TC-AC-ACC-E2E-300-download-isi-sel-berkas-list | FE+BE |
| TC-AC-ACC-707 | TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown | FE+BE |
| TC-AC-ACC-708 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-709 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-710 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-711 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-712 | TC-AC-ACC-E2E-289-kombinasi-search-filter-sort-pagination-dan-indikator-filter | FE+BE |
| TC-AC-ACC-713 | TC-AC-ACC-E2E-285-filter-last-updated-rentang-tanggal | FE+BE |
| TC-AC-ACC-714 | TC-AC-ACC-E2E-287-filter-chip-dan-checkbox-sinkron | FE+BE |
| TC-AC-ACC-715 | TC-AC-ACC-E2E-287-filter-chip-dan-checkbox-sinkron | FE+BE |
| TC-AC-ACC-716 | TC-AC-ACC-E2E-291-opsi-filter-industry-diperbarui-setelah-edit | FE+BE |
| TC-AC-ACC-717 | TC-AC-ACC-E2E-281-search-per-kolom-dan-siklus-interaksi | FE+BE |
| TC-AC-ACC-718 | TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan | FE+BE |
| TC-AC-ACC-719 | TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan | FE+BE |
| TC-AC-ACC-720 | TC-AC-ACC-E2E-303-pagination-dan-seleksi-manual-bertahan | FE+BE |
| TC-AC-ACC-721 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-722 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-723 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-724 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-725 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-726 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-727 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-728 | TC-AC-ACC-E2E-251-modal-changelog-client-filter-dan-sort | FE+BE |
| TC-AC-ACC-729 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-730 | TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | FE+BE |
| TC-AC-ACC-731 | TC-AC-ACC-E2E-252-modal-changelog-subscription-screening-search-dan-download | FE+BE |
| TC-AC-ACC-732 | TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | FE+BE |
| TC-AC-ACC-733 | TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | FE+BE |
| TC-AC-ACC-734 | TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | FE+BE |
| TC-AC-ACC-735 | TC-AC-ACC-E2E-253-modal-changelog-subscription-filter-dan-sort | FE+BE |
| TC-AC-ACC-736 | TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | FE+BE |
| TC-AC-ACC-737 | TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | FE+BE |
| TC-AC-ACC-738 | TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | FE+BE |
| TC-AC-ACC-739 | TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | FE+BE |
| TC-AC-ACC-740 | TC-AC-ACC-E2E-255-modal-changelog-asset-control-filter-dan-sort | FE+BE |
| TC-AC-ACC-741 | TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | FE+BE |
| TC-AC-ACC-742 | TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | FE+BE |
| TC-AC-ACC-743 | TC-AC-ACC-E2E-257-modal-changelog-setup-column-sembunyikan-dan-tampilkan-kolom-tersimpan | FE+BE |
| TC-AC-ACC-744 | TC-AC-ACC-E2E-258-modal-changelog-setup-column-drag-and-drop-urutan-kolom | FE+BE |
| TC-AC-ACC-745 | TC-AC-ACC-E2E-259-modal-changelog-setup-column-pin-dan-unpin-kolom | FE+BE |
| TC-AC-ACC-746 | TC-AC-ACC-E2E-260-modal-changelog-setup-column-reset-to-default | FE+BE |
| TC-AC-ACC-747 | TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | FE+BE |
| TC-AC-ACC-748 | TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | FE+BE |
| TC-AC-ACC-749 | TC-AC-ACC-E2E-052-create-sukses-tcp-stay-direct-partner-ganda-opsional-dan-saving-state | FE+BE |
| TC-AC-ACC-750 | TC-AC-ACC-E2E-051-create-aksesibilitas-popup-aria-dan-fokus-tcp | FE+BE |
| TC-AC-ACC-751 | TC-AC-ACC-E2E-051-create-aksesibilitas-popup-aria-dan-fokus-tcp | FE+BE |
| TC-AC-ACC-752 | TC-AC-ACC-E2E-051-create-aksesibilitas-popup-aria-dan-fokus-tcp | FE+BE |
| TC-AC-ACC-753 | TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | FE+BE |
| TC-AC-ACC-754 | TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | FE+BE |
| TC-AC-ACC-755 | TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | FE+BE |
| TC-AC-ACC-756 | TC-AC-ACC-E2E-078-edit-popup-saving-state-aksesibilitas-dan-form-tidak-ter-refresh-tcp | FE+BE |
| TC-AC-ACC-757 | TC-AC-ACC-E2E-198-purchase-history-license-search-semua-kolom | FE+BE |
| TC-AC-ACC-758 | TC-AC-ACC-E2E-198-purchase-history-license-search-semua-kolom | FE+BE |
| TC-AC-ACC-759 | TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | FE+BE |
| TC-AC-ACC-760 | TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | FE+BE |
| TC-AC-ACC-761 | TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | FE+BE |
| TC-AC-ACC-762 | TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | FE+BE |
| TC-AC-ACC-763 | TC-AC-ACC-E2E-200-purchase-history-license-sort-date-qty-duration | FE+BE |
| TC-AC-ACC-764 | TC-AC-ACC-E2E-200-purchase-history-license-sort-date-qty-duration | FE+BE |
| TC-AC-ACC-765 | TC-AC-ACC-E2E-200-purchase-history-license-sort-date-qty-duration | FE+BE |
| TC-AC-ACC-766 | TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | FE+BE |
| TC-AC-ACC-767 | TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | FE+BE |
| TC-AC-ACC-768 | TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | FE+BE |
| TC-AC-ACC-769 | TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | FE+BE |
| TC-AC-ACC-770 | TC-AC-ACC-E2E-205-purchase-history-tag-search-dan-filter | FE+BE |
| TC-AC-ACC-771 | TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | FE+BE |
| TC-AC-ACC-772 | TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | FE+BE |
| TC-AC-ACC-773 | TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | FE+BE |
| TC-AC-ACC-774 | TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | FE+BE |
| TC-AC-ACC-775 | TC-AC-ACC-E2E-210-purchase-history-hardware-search-dan-filter | FE+BE |
| TC-AC-ACC-776 | TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | FE+BE |
| TC-AC-ACC-777 | TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | FE+BE |
| TC-AC-ACC-778 | TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | FE+BE |
| TC-AC-ACC-779 | TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | FE+BE |
| TC-AC-ACC-780 | TC-AC-ACC-E2E-213-purchase-history-storage-search-dan-filter | FE+BE |
| TC-AC-ACC-781 | TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort | FE+BE |
| TC-AC-ACC-782 | TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort | FE+BE |
| TC-AC-ACC-783 | TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom | FE+BE |
| TC-AC-ACC-784 | TC-AC-ACC-E2E-208-hardware-list-search-filter-dan-sort | FE+BE |
| TC-AC-ACC-785 | TC-AC-ACC-E2E-209-purchase-history-hardware-screening-filter-dan-download | FE+BE |
| TC-AC-ACC-786 | TC-AC-ACC-E2E-212-tab-storage-screening-quota-purchase-history-dan-download | FE+BE |
| TC-AC-ACC-787 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-788 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-789 | TC-AC-ACC-E2E-241-search-station-list-kolom-teks-dan-numerik | FE+BE |
| TC-AC-ACC-790 | TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | FE+BE |
| TC-AC-ACC-791 | TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | FE+BE |
| TC-AC-ACC-792 | TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | FE+BE |
| TC-AC-ACC-793 | TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | FE+BE |
| TC-AC-ACC-794 | TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | FE+BE |
| TC-AC-ACC-795 | TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | FE+BE |
| TC-AC-ACC-796 | TC-AC-ACC-E2E-012-navigasi-detail-dan-retensi-state-list | FE+BE |
| TC-AC-ACC-798 | TC-AC-ACC-E2E-173-section-parent-pengelola-dan-default-user | FE+BE |
| TC-AC-ACC-799 | TC-AC-ACC-E2E-173-section-parent-pengelola-dan-default-user | FE+BE |
| TC-AC-ACC-800 | TC-AC-ACC-E2E-175-edit-client-default-user-activated-tidak-tertimpa | FE+BE |
| TC-AC-ACC-801 | TC-AC-ACC-E2E-176-client-derived-mengikuti-perubahan-partner-induk | FE+BE |
| TC-AC-ACC-802 | TC-AC-ACC-E2E-182-tab-subscription-screening-banner-dan-link | FE+BE |
| TC-AC-ACC-803 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-804 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-805 | TC-AC-ACC-E2E-184-tab-subscription-feature-entitlement-platform-core | FE+BE |
| TC-AC-ACC-806 | TC-AC-ACC-E2E-201-purchase-history-license-plan-custom-dan-subscription-id | FE+BE |
| TC-AC-ACC-807 | TC-AC-ACC-E2E-201-purchase-history-license-plan-custom-dan-subscription-id | FE+BE |
| TC-AC-ACC-808 | TC-AC-ACC-E2E-185-tab-subscription-feature-entitlement-source-plan | FE+BE |
| TC-AC-ACC-809 | TC-AC-ACC-E2E-183-tab-subscription-license-quota-nilai-dan-sort | FE+BE |
| TC-AC-ACC-810 | TC-AC-ACC-E2E-191-quota-detail-mengikuti-perubahan-fams-asset-tag-dan-storage | FE+BE |
| TC-AC-ACC-811 | TC-AC-ACC-E2E-194-top-up-license-allocation-asset-dan-storage | FE+BE |
| TC-AC-ACC-812 | TC-AC-ACC-E2E-203-hover-nama-lengkap-action-by-dan-modified-by | FE+BE |
| TC-AC-ACC-813 | TC-AC-ACC-E2E-203-hover-nama-lengkap-action-by-dan-modified-by | FE+BE |
| TC-AC-ACC-814 | TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom | FE+BE |
| TC-AC-ACC-815 | TC-AC-ACC-E2E-194-top-up-license-allocation-asset-dan-storage | FE+BE |
| TC-AC-ACC-816 | TC-AC-ACC-E2E-192-rekonsiliasi-harian-mengoreksi-used-tag | FE+BE |
| TC-AC-ACC-817 | TC-AC-ACC-E2E-193-qty-hardware-list-bertambah-setelah-unit-diaktivasi | FE+BE |
| TC-AC-ACC-818 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-819 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-820 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-821 | TC-AC-ACC-E2E-245-column-visibility-dan-setup-column-tab-asset-control | FE+BE |
| TC-AC-ACC-822 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-823 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-824 | TC-AC-ACC-E2E-215-column-visibility-tabel-sekunder-tab-detail | FE+BE |
| TC-AC-ACC-825 | TC-AC-ACC-E2E-245-column-visibility-dan-setup-column-tab-asset-control | FE+BE |
| TC-AC-ACC-826 | TC-AC-ACC-E2E-220-tabel-kuota-dan-feature-entitlement-tanpa-search-dan-filter | FE+BE |
| TC-AC-ACC-828 | TC-AC-ACC-E2E-214-sort-tabel-tab-subscription-quota-feature-dan-addon-client-custom | FE+BE |
| TC-AC-ACC-829 | TC-AC-ACC-E2E-214-sort-tabel-tab-subscription-quota-feature-dan-addon-client-custom | FE+BE |
| TC-AC-ACC-830 | TC-AC-ACC-E2E-214-sort-tabel-tab-subscription-quota-feature-dan-addon-client-custom | FE+BE |
| TC-AC-ACC-833 | TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks | FE+BE |
| TC-AC-ACC-834 | TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks | FE+BE |
| TC-AC-ACC-835 | TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks | FE+BE |
| TC-AC-ACC-836 | TC-AC-ACC-E2E-206-sort-tabel-tab-tag-dan-storage-client-custom | FE+BE |
| TC-AC-ACC-837 | TC-AC-ACC-E2E-206-sort-tabel-tab-tag-dan-storage-client-custom | FE+BE |
| TC-AC-ACC-839 | TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom | FE+BE |
| TC-AC-ACC-840 | TC-AC-ACC-E2E-211-sort-tabel-tab-hardware-dan-badge-category-client-custom | FE+BE |
| TC-AC-ACC-841 | TC-AC-ACC-E2E-206-sort-tabel-tab-tag-dan-storage-client-custom | FE+BE |
| TC-AC-ACC-844 | TC-AC-ACC-E2E-243-sort-station-list-teks-numerik-last-active-dan-nilai-kosong | FE+BE |
| TC-AC-ACC-845 | TC-AC-ACC-E2E-244-sort-tablet-list-app-version-tanggal-dan-status | FE+BE |
| TC-AC-ACC-846 | TC-AC-ACC-E2E-244-sort-tablet-list-app-version-tanggal-dan-status | FE+BE |
| TC-AC-ACC-847 | TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | FE+BE |
| TC-AC-ACC-848 | TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | FE+BE |
| TC-AC-ACC-849 | TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | FE+BE |
| TC-AC-ACC-850 | TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | FE+BE |
| TC-AC-ACC-851 | TC-AC-ACC-E2E-242-filter-station-list-panel-dropdown-range-dan-empty-state | FE+BE |
| TC-AC-ACC-852 | TC-AC-ACC-E2E-216-empty-state-search-dan-filter-tabel-sekunder-client-custom | FE+BE |
| TC-AC-ACC-853 | TC-AC-ACC-E2E-218-resilience-tabel-tab-subscription-tag-dan-hardware | FE+BE |
| TC-AC-ACC-854 | TC-AC-ACC-E2E-218-resilience-tabel-tab-subscription-tag-dan-hardware | FE+BE |
| TC-AC-ACC-855 | TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog | FE+BE |
| TC-AC-ACC-856 | TC-AC-ACC-E2E-240-resilience-asset-control-generate-aksi-tabel-dan-changelog | FE+BE |
| TC-AC-ACC-857 | TC-AC-ACC-E2E-219-loading-state-tabel-tab-detail | FE+BE |
| TC-AC-ACC-858 | TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state | FE+BE |
| TC-AC-ACC-859 | TC-AC-ACC-E2E-217-pagination-purchase-history-license | FE+BE |
| TC-AC-ACC-860 | TC-AC-ACC-E2E-217-pagination-purchase-history-license | FE+BE |
| TC-AC-ACC-861 | TC-AC-ACC-E2E-231-screening-tab-asset-control-kuota-station-tablet | FE+BE |
| TC-AC-ACC-862 | TC-AC-ACC-E2E-024-mobile-list-toolbar-card-dan-bottom-sheet-aksi | FE+BE |
| TC-AC-ACC-863 | TC-AC-ACC-E2E-024-mobile-list-toolbar-card-dan-bottom-sheet-aksi | FE+BE |
| TC-AC-ACC-864 | TC-AC-ACC-E2E-179-isolasi-tab-subscription-partner-cv-mitra-timur | FE+BE |
| TC-AC-ACC-865 | TC-AC-ACC-E2E-179-isolasi-tab-subscription-partner-cv-mitra-timur | FE+BE |
| TC-AC-ACC-869 | TC-AC-ACC-E2E-171-screening-header-detail-client-active-full | FE+BE |
| TC-AC-ACC-870 | TC-AC-ACC-E2E-171-screening-header-detail-client-active-full | FE+BE |
| TC-AC-ACC-871 | TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-872 | TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-873 | TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-874 | TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-875 | TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-876 | TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-877 | TC-AC-ACC-E2E-021-guided-tooltip-list-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-878 | TC-AC-ACC-E2E-020-guided-tooltip-list-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-879 | TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-880 | TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-881 | TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-882 | TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-883 | TC-AC-ACC-E2E-023-guided-tooltip-detail-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-884 | TC-AC-ACC-E2E-023-guided-tooltip-detail-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-885 | TC-AC-ACC-E2E-023-guided-tooltip-detail-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-886 | TC-AC-ACC-E2E-023-guided-tooltip-detail-skip-klik-overlay-berpindah-halaman-resize | FE+BE |
| TC-AC-ACC-887 | TC-AC-ACC-E2E-022-guided-tooltip-detail-akun-satu-kunjungan-replay-navigasi-keyboard | FE+BE |
| TC-AC-ACC-888 | TC-AC-ACC-E2E-065-mobile-popup-create-dan-edit-client-android-full-screen | FE+BE |
| TC-AC-ACC-889 | TC-AC-ACC-E2E-065-mobile-popup-create-dan-edit-client-android-full-screen | FE+BE |
| TC-AC-ACC-890 | TC-AC-ACC-E2E-228-mobile-detail-client-android-card-list | FE+BE |
| TC-AC-ACC-891 | TC-AC-ACC-E2E-228-mobile-detail-client-android-card-list | FE+BE |
| TC-AC-ACC-892 | TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | FE+BE |
| TC-AC-ACC-893 | TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | FE+BE |
| TC-AC-ACC-894 | TC-AC-ACC-E2E-232-tab-asset-control-kondisi-data-client | FE+BE |
| TC-AC-ACC-895 | TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat | FE+BE |
| TC-AC-ACC-896 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-897 | TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit | FE+BE |
| TC-AC-ACC-898 | TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit | FE+BE |
| TC-AC-ACC-899 | TC-AC-ACC-E2E-235-ttl-token-enrollment-qr-batas-15-menit | FE+BE |
| TC-AC-ACC-900 | TC-AC-ACC-E2E-246-simulator-tablet-kiosk-scan-qr-token-final-revoked-dan-heartbeat | FE+BE |
| TC-AC-ACC-901 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-902 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-903 | TC-AC-ACC-E2E-248-sinkron-balik-global-settings-hardware-dua-sesi | FE+BE |
| TC-AC-ACC-904 | TC-AC-ACC-E2E-248-sinkron-balik-global-settings-hardware-dua-sesi | FE+BE |
| TC-AC-ACC-905 | TC-AC-ACC-E2E-237-defense-aksi-asset-control-client-archived-suspended-dan-role-read | FE+BE |
| TC-AC-ACC-906 | TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | FE+BE |
| TC-AC-ACC-907 | TC-AC-ACC-E2E-131-defense-client-suspended-dan-archived-request-langsung | FE+BE |
| TC-AC-ACC-908 | TC-AC-ACC-E2E-128-resend-activation-email-inbox-dan-retry-otomatis | FE+BE |
| TC-AC-ACC-909 | TC-AC-ACC-E2E-018-resolusi-dan-cakupan-client-viewer-partner-mitra-sejati | FE+BE |
| TC-AC-ACC-910 | TC-AC-ACC-E2E-270-pencatatan-log-generate-enrollment-qr-deactivate-station-dan-revoke-tablet-di-tiga-surface | FE+BE |
| TC-AC-ACC-911 | TC-AC-ACC-E2E-270-pencatatan-log-generate-enrollment-qr-deactivate-station-dan-revoke-tablet-di-tiga-surface | FE+BE |
| TC-AC-ACC-912 | TC-AC-ACC-E2E-269-pencatatan-log-resend-activation-email-dan-toggle-byo-di-tiga-surface | FE+BE |
| TC-AC-ACC-913 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-914 | TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface | FE+BE |
| TC-AC-ACC-915 | TC-AC-ACC-E2E-267-pencatatan-log-suspend-unsuspend-dan-bulk-suspend-di-tiga-surface | FE+BE |
| TC-AC-ACC-916 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-917 | TC-AC-ACC-E2E-238-deactivate-station-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-918 | TC-AC-ACC-E2E-239-revoke-tablet-dialog-batal-sukses-dan-klik-ganda | FE+BE |
| TC-AC-ACC-924 | TC-AC-ACC-E2E-323-role-matrix-onboarding-opsi-new-client-tampil | FE+BE |
| TC-AC-ACC-925 | TC-AC-ACC-E2E-324-role-matrix-onboarding-opsi-new-client-tidak-tampil-dan-bypass-ditolak | FE+BE |
| TC-AC-ACC-926 | TC-AC-ACC-E2E-153-delete-dialog-dan-izin-berubah-oleh-pelaku-lain | FE+BE |
| TC-AC-ACC-927 | TC-AC-ACC-E2E-015-resolusi-group-managed-by-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-928 | TC-AC-ACC-E2E-017-resolusi-dan-cakupan-client-viewer-distributor-timur | FE+BE |
| TC-AC-ACC-929 | TC-AC-ACC-E2E-003-isi-sel-kolom-company-managed-by-modified-by | FE+BE |
| TC-AC-ACC-930 | TC-AC-ACC-E2E-282-search-kolom-hidden-tidak-dicari | FE+BE |
| TC-AC-ACC-931 | TC-AC-ACC-E2E-290-distributor-filter-sort-sel-tanda-hubung | FE+BE |
| TC-AC-ACC-932 | TC-AC-ACC-E2E-283-filter-screening-panel-dan-opsi-dropdown | FE+BE |
| TC-AC-ACC-933 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-934 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-935 | TC-AC-ACC-E2E-301-download-volume-di-atas-5000-baris | FE+BE |
| TC-AC-ACC-936 | TC-AC-ACC-E2E-187-tab-subscription-term-terakhir-archive-purge-deleted-dan-ditolak | FE+BE |
| TC-AC-ACC-937 | TC-AC-ACC-E2E-187-tab-subscription-term-terakhir-archive-purge-deleted-dan-ditolak | FE+BE |
| TC-AC-ACC-938 | TC-AC-ACC-E2E-201-purchase-history-license-plan-custom-dan-subscription-id | FE+BE |
| TC-AC-ACC-939 | TC-AC-ACC-E2E-202-purchase-history-license-sort-subscription-action-by-tanggal-teks | FE+BE |
| TC-AC-ACC-940 | TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader | FE+BE |
| TC-AC-ACC-941 | TC-AC-ACC-E2E-233-blokir-generate-enrollment-qr-kuota-dan-reader | FE+BE |
| TC-AC-ACC-942 | TC-AC-ACC-E2E-044-create-duplikat-ditolak-dan-spasi-client-code-af | FE+BE |
| TC-AC-ACC-943 | TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af | FE+BE |
| TC-AC-ACC-944 | TC-AC-ACC-E2E-067-edit-validasi-field-client-default-user-activated-af | FE+BE |
| TC-AC-ACC-945 | TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af | FE+BE |
| TC-AC-ACC-946 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-947 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-948 | TC-AC-ACC-E2E-063-defense-create-dan-edit-bypass-fe-ditolak-server | FE+BE |
| TC-AC-ACC-949 | TC-AC-ACC-E2E-127-delete-client-berfoto-dan-nama-dipakai-ulang | FE+BE |
| TC-AC-ACC-950 | TC-AC-ACC-E2E-016-cakupan-client-terlihat-viewer-distributor-nusantara | FE+BE |
| TC-AC-ACC-951 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-952 | TC-AC-ACC-E2E-027-role-matrix-negatif-akses-url-detail-aktor-archived-read | FE+BE |
| TC-AC-ACC-953 | TC-AC-ACC-E2E-027-role-matrix-negatif-akses-url-detail-aktor-archived-read | FE+BE |
| TC-AC-ACC-954 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-955 | TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes | FE+BE |
| TC-AC-ACC-956 | TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes | FE+BE |
| TC-AC-ACC-957 | TC-AC-ACC-E2E-112-change-partner-penutupan-dialog-unsaved-changes | FE+BE |
| TC-AC-ACC-958 | TC-AC-ACC-E2E-115-change-partner-oleh-distributor | FE+BE |
| TC-AC-ACC-959 | TC-AC-ACC-E2E-079-edit-retry-activation-email-gagal-notifikasi-dan-dihentikan-tcp | FE+BE |
| TC-AC-ACC-960 | TC-AC-ACC-E2E-143-suspend-unsuspend-efek-ke-sesi-user-client | FE+BE |
| TC-AC-ACC-961 | TC-AC-ACC-E2E-146-dua-sesi-konflik-change-partner-dan-delete | FE+BE |
| TC-AC-ACC-962 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-963 | TC-AC-ACC-E2E-314-activation-email-dan-penyediaan-akses-gagal | FE+BE |
| TC-AC-ACC-964 | TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server | FE+BE |
| TC-AC-ACC-965 | TC-AC-ACC-E2E-026-role-matrix-negatif-akses-url-detail-aktor-active-read | FE+BE |
| TC-AC-ACC-966 | TC-AC-ACC-E2E-047-foto-client-create-edit-dan-remove-af | FE+BE |
| TC-AC-ACC-967 | TC-AC-ACC-E2E-128-resend-activation-email-inbox-dan-retry-otomatis | FE+BE |
| TC-AC-ACC-968 | TC-AC-ACC-E2E-128-resend-activation-email-inbox-dan-retry-otomatis | FE+BE |
| TC-AC-ACC-969 | TC-AC-ACC-E2E-288-filter-distributor-partner-semantik-principal | FE+BE |
| TC-AC-ACC-970 | TC-AC-ACC-E2E-250-modal-changelog-client-screening-isi-kolom-search-dan-download | FE+BE |
| TC-AC-ACC-971 | TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert | FE+BE |
| TC-AC-ACC-972 | TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert | FE+BE |
| TC-AC-ACC-973 | TC-AC-ACC-E2E-080-edit-retry-activation-email-notifikasi-default-user-principal | FE+BE |
| TC-AC-ACC-974 | TC-AC-ACC-E2E-247-dua-admin-generate-bersamaan-dan-aksi-basi-409 | FE+BE |
| TC-AC-ACC-975 | TC-AC-ACC-E2E-247-dua-admin-generate-bersamaan-dan-aksi-basi-409 | FE+BE |
| TC-AC-ACC-976 | TC-AC-ACC-E2E-079-edit-retry-activation-email-gagal-notifikasi-dan-dihentikan-tcp | FE+BE |
| TC-AC-ACC-977 | TC-AC-ACC-E2E-081-edit-retry-activation-email-penerima-notifikasi-empat-sesi | FE+BE |
| TC-AC-ACC-978 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-979 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-980 | TC-AC-ACC-E2E-133-defense-tanpa-izin-atau-di-luar-jaringan-request-langsung | FE+BE |
| TC-AC-ACC-981 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-982 | TC-AC-ACC-E2E-151-delete-diblok-subscription-ditambahkan-sesi-lain | FE+BE |
| TC-AC-ACC-983 | TC-AC-ACC-E2E-314-activation-email-dan-penyediaan-akses-gagal | FE+BE |
| TC-AC-ACC-984 | TC-AC-ACC-E2E-079-edit-retry-activation-email-gagal-notifikasi-dan-dihentikan-tcp | FE+BE |
| TC-AC-ACC-985 | TC-AC-ACC-E2E-113-change-partner-clear-field-select-group-wajib-drag | FE+BE |
| TC-AC-ACC-986 | TC-AC-ACC-E2E-292-sort-tiga-state-kolom-default | FE+BE |
| TC-AC-ACC-987 | TC-AC-ACC-E2E-035-defense-tulis-langsung-di-luar-scope-group-ditolak-404 | FE+BE |
| TC-AC-ACC-988 | TC-AC-ACC-E2E-323-role-matrix-onboarding-opsi-new-client-tampil | FE+BE |
| TC-AC-ACC-989 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-990 | TC-AC-ACC-E2E-180-isolasi-sub-tab-subscription-per-viewer-lintas-jaringan | FE+BE |
| TC-AC-ACC-991 | TC-AC-ACC-E2E-234-generate-enrollment-qr-dialog-token-dan-changelog | FE+BE |
| TC-AC-ACC-992 | TC-AC-ACC-E2E-222-kegagalan-penyediaan-akses-notifikasi-dan-retry-manual | FE+BE |
| TC-AC-ACC-993 | TC-AC-ACC-E2E-225-role-matrix-retry-akses-tersembunyi-selain-total-control | FE+BE |
| TC-AC-ACC-994 | TC-AC-ACC-E2E-322-default-user-client-akses-produk-setelah-perubahan-status | FE+BE |
| TC-AC-ACC-995 | TC-AC-ACC-E2E-111-change-partner-screening-opsi-badge-callout | FE+BE |
| TC-AC-ACC-996 | TC-AC-ACC-E2E-190-total-quota-qr-tab-tag-dari-asset-license-term | FE+BE |
| TC-AC-ACC-997 | TC-AC-ACC-E2E-190-total-quota-qr-tab-tag-dari-asset-license-term | FE+BE |
| TC-AC-ACC-998 | TC-AC-ACC-E2E-199-purchase-history-license-filter-semua-kolom | FE+BE |
| TC-AC-ACC-999 | TC-AC-ACC-E2E-268-pencatatan-log-aksi-sistem-auto-archive-auto-reactivate-dan-send-activation-email | FE+BE |
| TC-AC-ACC-999 | TC-AC-ACC-E2E-272-absence-log-aksi-tanpa-perubahan-dan-aksi-sistem-tanpa-system-log | FE+BE |
| TC-AC-ACC-1000 | TC-AC-ACC-E2E-317-entitas-induk-partner-suspend-unsuspend | FE+BE |
| TC-AC-ACC-1001 | TC-AC-ACC-E2E-318-entitas-induk-partner-delete | FE+BE |
| TC-AC-ACC-1002 | TC-AC-ACC-E2E-318-entitas-induk-partner-delete | FE+BE |
| TC-AC-ACC-1003 | TC-AC-ACC-E2E-319-entitas-induk-partner-promote-menjadi-distributor | FE+BE |
| TC-AC-ACC-1004 | TC-AC-ACC-E2E-222-kegagalan-penyediaan-akses-notifikasi-dan-retry-manual | FE+BE |
| TC-AC-ACC-1005 | TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup | FE+BE |
| TC-AC-ACC-1006 | TC-AC-ACC-E2E-223-notifikasi-kegagalan-penyediaan-akses-per-plan-owner | FE+BE |
| TC-AC-ACC-1007 | TC-AC-ACC-E2E-066-edit-screening-popup-status-client-dan-field-reflected-af | FE+BE |
| TC-AC-ACC-1008 | TC-AC-ACC-E2E-227-retry-akses-gagal-diproses-toast-error | FE+BE |
| TC-AC-ACC-1009 | TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup | FE+BE |
| TC-AC-ACC-1010 | TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer | FE+BE |
| TC-AC-ACC-1011 | TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer | FE+BE |
| TC-AC-ACC-1012 | TC-AC-ACC-E2E-263-changelog-scope-baris-viewer-partner | FE+BE |
| TC-AC-ACC-1013 | TC-AC-ACC-E2E-264-changelog-scope-baris-viewer-distributor | FE+BE |
| TC-AC-ACC-1014 | TC-AC-ACC-E2E-229-role-matrix-visibilitas-source-purchase-history-per-viewer | FE+BE |
| TC-AC-ACC-1015 | TC-AC-ACC-E2E-229-role-matrix-visibilitas-source-purchase-history-per-viewer | FE+BE |
| TC-AC-ACC-1016 | TC-AC-ACC-E2E-263-changelog-scope-baris-viewer-partner | FE+BE |
| TC-AC-ACC-1017 | TC-AC-ACC-E2E-264-changelog-scope-baris-viewer-distributor | FE+BE |
| TC-AC-ACC-1018 | TC-AC-ACC-E2E-312-auto-reactivate-client-archived | FE+BE |
| TC-AC-ACC-1019 | TC-AC-ACC-E2E-312-auto-reactivate-client-archived | FE+BE |
| TC-AC-ACC-1020 | TC-AC-ACC-E2E-152-delete-archived-diblok-trial-active-d03 | FE+BE |
| TC-AC-ACC-1021 | TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert | FE+BE |
| TC-AC-ACC-1022 | TC-AC-ACC-E2E-189-badge-produk-dan-kuota-term-trial | FE+BE |
| TC-AC-ACC-1023 | TC-AC-ACC-E2E-263-changelog-scope-baris-viewer-partner | FE+BE |
| TC-AC-ACC-1024 | TC-AC-ACC-E2E-189-badge-produk-dan-kuota-term-trial | FE+BE |
| TC-AC-ACC-1025 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-1026 | TC-AC-ACC-E2E-134-defense-delete-constraint-d03-d14-request-langsung | FE+BE |
| TC-AC-ACC-1027 | TC-AC-ACC-E2E-150-delete-client-active-suspended-tanpa-riwayat-subscription | FE+BE |
| TC-AC-ACC-1028 | TC-AC-ACC-E2E-310-auto-archive-varian-term-lama-trial-dan-convert | FE+BE |
| TC-AC-ACC-1029 | TC-AC-ACC-E2E-312-auto-reactivate-client-archived | FE+BE |
| TC-AC-ACC-1030 | TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer | FE+BE |
| TC-AC-ACC-1031 | TC-AC-ACC-E2E-178-role-matrix-parent-pengelola-per-viewer | FE+BE |
| TC-AC-ACC-1032 | TC-AC-ACC-E2E-223-notifikasi-kegagalan-penyediaan-akses-per-plan-owner | FE+BE |
| TC-AC-ACC-1033 | TC-AC-ACC-E2E-313-job-scheduler-lifecycle-jam-server | FE+BE |
| TC-AC-ACC-1034 | TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup | FE+BE |
| TC-AC-ACC-1035 | TC-AC-ACC-E2E-224-retry-akses-dari-tampilan-basi-dua-sesi | FE+BE |
| TC-AC-ACC-1036 | TC-AC-ACC-E2E-329-auto-archive-lalu-delete-client-dengan-trial-non-live | FE+BE |
| TC-AC-ACC-1037 | TC-AC-ACC-E2E-188-license-quota-dan-quota-qr-nol-pada-term-tidak-hidup | FE+BE |
| TC-AC-ACC-1038 | TC-AC-ACC-E2E-329-auto-archive-lalu-delete-client-dengan-trial-non-live | FE+BE |
| TC-AC-ACC-1039 | TC-AC-ACC-E2E-226-request-retry-akses-langsung-ditolak-server | FE+BE |
| TC-AC-ACC-1040 | TC-AC-ACC-E2E-265-changelog-dan-activity-log-retry-access-setup-principal-vs-distributor | FE+BE |
| TC-AC-ACC-1044 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-1045 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |
| TC-AC-ACC-1046 | TC-AC-ACC-E2E-042-create-validasi-field-wajib-format-dan-batas-af | FE+BE |
| TC-AC-ACC-1047 | TC-AC-ACC-E2E-053-create-batas-nilai-tepat-diterima-tcp | FE+BE |

## TC hanya-BE

Tidak ada. Semua 1022 TC tidak bertanda `FE Test = -` (869 `Need API`, 153 `UI Only`), dan header `tc-client.md` menyatakan kontrak REST murni ada di `tc-client-backend.md`. Kandidat yang terlihat BE (permintaan langsung ke server) tetap masuk sebagai spec kelas defense-in-depth FE+BE.
