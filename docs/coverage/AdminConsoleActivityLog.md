# Coverage E2E — Admin Console > Activity Log

Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (186 TC granular aktif, `TC-AC-ACAL-01`–`186`) dan `admin-console/activity-log/TestCases/tc-activity-log-backend.md` (hanya untuk mengenali TC kontrak API).
Suite: `specs/AdminConsole/ActivityLog/`. Prefix Modul: `AC` + `ACAL` (`TC-AC-ACAL-E2E-*`). Status semua spec: `draft`, belum ada script.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 184 TC masuk 55 spec, 2 TC dilewati karena hanya-BE (182, 183). Halaman coverage versi lama (238 TC, 42 spec) tidak berlaku lagi dan penomoran E2E lamanya tidak dipakai ulang.

---

## 1. Pemetaan TC granular ke spec e2e (55 spec)

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-AC-ACAL-E2E-001-screening-layout-3-zona-tab-session-dan-baris-tabel-tidak-dapat-diklik | Screening Layout 3 Zona Tab Session dan Baris Tabel Tidak Dapat Diklik | FE+BE | 36 | 01, 16 |
| TC-AC-ACAL-E2E-002-urutan-default-dan-tie-break-kedua-tab | Urutan Default dan Tie-break Kedua Tab | FE+BE | 16 | 11, 12, 174 |
| TC-AC-ACAL-E2E-003-empty-state-genuinely-kosong-kedua-tab | Empty State Genuinely Kosong Kedua Tab | FE+BE | 10 | 05, 06 |
| TC-AC-ACAL-E2E-004-loading-state-dan-no-result-akibat-search-dan-filter | Loading State dan No-result Akibat Search dan Filter | FE+BE | 25 | 04, 07, 08 |
| TC-AC-ACAL-E2E-005-tampilan-sel-nama-singkat-teks-panjang-dan-tooltip-group | Tampilan Sel: Nama Singkat, Teks Panjang, dan Tooltip Group | FE+BE | 43 | 14, 15, 165, 181 |
| TC-AC-ACAL-E2E-006-guided-tooltip-isi-dan-navigasi | Guided Tooltip: Isi dan Navigasi | FE+BE | 35 | 18, 20, 24 |
| TC-AC-ACAL-E2E-007-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai | Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai | FE+BE | 47 | 19, 21, 22, 23 |
| TC-AC-ACAL-E2E-008-independensi-state-antar-tab-dan-tab-aktif-setelah-refresh | Independensi State Antar Tab dan Tab Aktif Setelah Refresh | FE+BE | 26 | 112, 115 |
| TC-AC-ACAL-E2E-009-pagination-info-page-size-navigasi-dan-reset-halaman | Pagination: Info, Page Size, Navigasi, dan Reset Halaman | FE+BE | 32 | 116, 117 |
| TC-AC-ACAL-E2E-010-kombinasi-search-filter-sort-pagination-dan-pemulihan-no-result | Kombinasi Search, Filter, Sort, Pagination, dan Pemulihan dari No-result | FE+BE | 25 | 118, 119 |
| TC-AC-ACAL-E2E-011-resilience-error-load-try-again-dan-download-gagal | Resilience: Error Load Tabel, Try Again, dan Download Gagal | mock | 30 | 09, 10, 131, 132 |
| TC-AC-ACAL-E2E-012-role-matrix-akses-dan-download-total-control-read-only-default-user | Role Matrix: Akses, Toolbar, dan Download Total Control, Read Only, Default User | FE+BE | 38 | 25, 26, 27 |
| TC-AC-ACAL-E2E-013-role-matrix-tanpa-akses-menu-direct-url-dan-client-tanpa-akses | Role Matrix: Tanpa Akses Menu, Direct URL, dan Client Tanpa Akses | FE+BE | 20 | 28, 29, 30, 31, 32 |
| TC-AC-ACAL-E2E-014-isolasi-scope-tab-user-action-principal-distributor-partner | Isolasi Scope Tab User Action: Principal, Distributor, Partner | FE+BE | 44 | 33, 34, 35, 36, 168 |
| TC-AC-ACAL-E2E-015-isolasi-scope-tab-session-principal-distributor-partner | Isolasi Scope Tab Session: Principal, Distributor, Partner | FE+BE | 19 | 37, 38, 39 |
| TC-AC-ACAL-E2E-016-scope-read-only-tanpa-masking-dan-opsi-filter-ter-scope | Scope Read Only, Tanpa Masking, dan Opsi Filter Ter-scope | FE+BE | 29 | 40, 41, 43 |
| TC-AC-ACAL-E2E-017-state-tenant-entitas-suspended-baca-dan-aksi-tercatat | State Tenant: Entitas Suspended Tetap Dapat Membaca dan Aksi Tercatat | FE+BE | 21 | 42, 157 |
| TC-AC-ACAL-E2E-018-perubahan-hubungan-entitas-reassign-partner-dan-pindah-staf | Perubahan Hubungan Entitas: Reassign Partner dan Pindah Staf | FE+BE | 36 | 149, 162, 169 |
| TC-AC-ACAL-E2E-019-isolasi-realtime-lintas-entitas-tidak-menerima-event | Isolasi Real-time Lintas Entitas: Tidak Menerima Event Entitas Lain | FE+BE | 16 | 154, 160 |
| TC-AC-ACAL-E2E-020-defense-in-depth-request-langsung-dan-teks-literal | Defense-in-depth: Request Langsung ke Endpoint Log dan Teks Literal | FE+BE | 37 | 150, 151, 152, 153, 156 |
| TC-AC-ACAL-E2E-021-absence-event-platform-dan-download-tidak-tercatat | Absence: Event Platform dan Download Tidak Tercatat | FE+BE | 26 | 48, 133 |
| TC-AC-ACAL-E2E-022-isi-kolom-tab-session-nilai-kosong-ip-dan-device | Isi Kolom Tab Session: Plain Text, Nilai Kosong, IP, dan Device | FE+BE | 27 | 44, 45, 46, 47 |
| TC-AC-ACAL-E2E-023-search-tab-session-kolom-nama-status-date-visibilitas-dan-siklus-kotak | Search Tab Session: Kolom, Nama Lengkap, Status, Date, Visibilitas Kolom, dan Siklus Kotak | FE+BE | 49 | 49, 50, 51, 52, 53, 54 |
| TC-AC-ACAL-E2E-024-filter-tab-session-struktur-opsi-or-and-dan-nama-ganda | Filter Tab Session: Struktur, Opsi, OR/AND, dan Nama Ganda | FE+BE | 48 | 55, 56, 57, 58, 172, 173 |
| TC-AC-ACAL-E2E-025-sort-tab-session-semua-kolom-dan-perpindahan-target | Sort Tab Session: Semua Kolom dan Perpindahan Target | FE+BE | 55 | 74, 75, 76, 77, 78, 79 |
| TC-AC-ACAL-E2E-026-setup-column-tab-session-overlay-popup-sembunyikan-dan-kolom-terakhir | Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir | FE+BE | 51 | 80, 81, 82, 86, 87 |
| TC-AC-ACAL-E2E-027-setup-column-tab-session-urutan-pin-batas-tiga-dan-reset | Setup Column Tab Session: Urutan, Pin, Batas Tiga Kolom, dan Reset | FE+BE | 34 | 83, 84, 85 |
| TC-AC-ACAL-E2E-028-isi-kolom-tab-user-action-pola-per-jenis-aksi-dan-description | Isi Kolom Tab User Action: Pola Per Jenis Aksi dan Kolom Description | FE+BE | 16 | 88, 184 |
| TC-AC-ACAL-E2E-029-search-tab-user-action-siklus-kotak-modified-by-kolom-date-dan-nilai-di-luar-kolom | Search Tab User Action: Siklus Kotak, Modified By, Kolom Date, dan Nilai di Luar Kolom | FE+BE | 29 | 89, 91, 92, 94 |
| TC-AC-ACAL-E2E-030-filter-tab-user-action-struktur-opsi-or-and-dan-nama-ganda | Filter Tab User Action: Struktur, Opsi Dinamis, OR/AND, dan Nama Ganda | FE+BE | 44 | 95, 96, 97, 98, 176 |
| TC-AC-ACAL-E2E-031-sort-tab-user-action-kolom-modified-by-dan-tipe-campuran | Sort Tab User Action: Kolom, Modified By, dan Tipe Campuran | FE+BE | 30 | 100, 101, 102, 103 |
| TC-AC-ACAL-E2E-032-setup-column-tab-user-action-overlay-popup-sembunyikan-dan-kolom-terakhir | Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, dan Kolom Terakhir | FE+BE | 52 | 104, 105, 106, 110, 111 |
| TC-AC-ACAL-E2E-033-setup-column-tab-user-action-urutan-pin-batas-tiga-dan-reset | Setup Column Tab User Action: Urutan, Pin, Batas Tiga Kolom, dan Reset | FE+BE | 35 | 107, 108, 109 |
| TC-AC-ACAL-E2E-034-filter-date-batas-inklusif-satu-sisi-dan-rentang-terbalik-kedua-tab | Filter Date: Batas Inklusif, Satu Sisi, dan Rentang Terbalik Kedua Tab | FE+BE | 28 | 59, 61, 62, 63, 99 |
| TC-AC-ACAL-E2E-035-kontrol-filter-panel-pencarian-opsi-chip-overflow-clear-dan-indikator | Kontrol Filter Panel: Pencarian Opsi, Chip, Overflow, Tutup Tanpa Apply, Clear, dan Indikator | FE+BE | 59 | 64, 65, 66, 67, 68, 69, 70 |
| TC-AC-ACAL-E2E-036-kontrol-filter-panel-kolom-hidden-sumber-kosong-keyboard-dan-loading-opsi | Kontrol Filter Panel: Kolom Hidden, Sumber Kosong, Keyboard, dan Loading Opsi | FE+BE | 39 | 71, 72, 73, 167 |
| TC-AC-ACAL-E2E-037-format-tanggal-dan-zona-waktu-general-settings-entitas-staf-login | Format Tanggal dan Zona Waktu Mengikuti General Settings Entitas Staf Login | FE+BE | 31 | 60, 135, 136 |
| TC-AC-ACAL-E2E-038-bahasa-pengguna-kolom-translatable-dan-label-opsi-filter | Bahasa Pengguna: Kolom Translatable dan Label Opsi Filter | FE+BE | 33 | 170, 180 |
| TC-AC-ACAL-E2E-039-download-nama-berkas-header-cakupan-baris-filter-dan-kolom-hidden | Download: Nama Berkas, Header, Cakupan Baris, Mengikuti Filter, Kolom Hidden, dan Hasil Kosong | FE+BE | 49 | 121, 122, 123, 124, 125, 126, 128 |
| TC-AC-ACAL-E2E-040-isi-sel-berkas-download-format-tanggal-nilai-kosong-status-description-field | Isi Sel Berkas Download: Format Tanggal, Nilai Kosong, Status, Description, dan Field | FE+BE | 32 | 127, 134, 179, 186 |
| TC-AC-ACAL-E2E-041-download-threshold-5000-5001-baris-loading-screen-dan-gagal | Download: Threshold 5.000 dan 5.001 Baris, Loading Screen, dan Gagal di Atas Threshold | FE+BE | 18 | 129, 130, 164 |
| TC-AC-ACAL-E2E-042-volume-besar-download-1048577-baris-retensi-lintas-tahun-dan-browsing-10000 | Volume Besar: Download 1.048.577 Baris, Retensi Lintas Tahun, dan Browsing 10.000 Entri | FE+BE | 26 | 158, 159, 171 |
| TC-AC-ACAL-E2E-043-realtime-baris-baru-saringan-aktif-opsi-filter-bertambah-dan-halaman-lebih-dari-satu | Real-time: Baris Baru, Saringan Aktif, Opsi Filter Bertambah, dan Halaman Lebih dari Satu | FE+BE | 56 | 137, 138, 139, 148, 166, 177 |
| TC-AC-ACAL-E2E-044-koneksi-realtime-ditutup-server-dan-putus-sambung | Koneksi Real-time: Ditutup Server dan Putus lalu Tersambung Kembali | FE+BE | 30 | 155, 161, 178 |
| TC-AC-ACAL-E2E-045-pencatatan-aksi-modul-ac-create-edit-tiga-field-delete-dan-event-sesi | Pencatatan Aksi Modul AC: Create, Edit Tiga Field, Delete, dan Event Sesi | FE+BE | 40 | 143, 144, 145, 147 |
| TC-AC-ACAL-E2E-046-snapshot-identitas-beku-pelaku-terhapus-dan-perubahan-nama | Snapshot Identitas Beku, Pelaku Terhapus, dan Perubahan Nama | FE+BE | 40 | 140, 141, 142 |
| TC-AC-ACAL-E2E-047-screening-layout-tab-user-action-dan-tanpa-kontrol-tulis | Screening Layout 3 Zona Tab User Action dan Tanpa Kontrol Tulis | FE+BE | 32 | 02, 17 |
| TC-AC-ACAL-E2E-048-breadcrumb-route-per-tab-dan-tab-session-saat-masuk-dari-sidebar | Breadcrumb Per Tab, Route Per Tab, dan Tab Session Saat Masuk dari Sidebar | FE+BE | 21 | 03 |
| TC-AC-ACAL-E2E-049-tooltip-ikon-table-tools-dan-header-column-visibility-kedua-tab | Tooltip Ikon Table Tools dan Header Column Visibility, Kedua Tab | FE+BE | 20 | 13 |
| TC-AC-ACAL-E2E-050-klik-ulang-menu-activity-log-mereset-kedua-tab-ke-default | Klik Ulang Menu Activity Log Mereset Kedua Tab ke Default | FE+BE | 22 | 113 |
| TC-AC-ACAL-E2E-051-refresh-mempertahankan-state-dan-setup-column-independen-antar-tab | Refresh Mempertahankan State dan Setup Column Independen Antar Tab | FE+BE | 32 | 114, 120 |
| TC-AC-ACAL-E2E-052-absence-aksi-dibatalkan-dan-gagal-di-modul-sumber-tidak-tercatat | Absence: Aksi Dibatalkan dan Gagal di Modul Sumber Tidak Tercatat | FE+BE | 28 | 146, 175 |
| TC-AC-ACAL-E2E-053-absence-aksi-modul-fams-sams-siem-dan-global-settings-tidak-masuk-tab-user-action | Absence: Aksi di Modul FAMS, SAMS, SIEM, dan Global Settings Tidak Masuk Tab User Action | FE+BE | 16 | 163 |
| TC-AC-ACAL-E2E-054-search-tab-user-action-substring-per-kolom-dan-kolom-hidden | Search Tab User Action: Substring per Kolom dan Kolom Hidden | FE+BE | 16 | 90, 93 |
| TC-AC-ACAL-E2E-055-search-dan-sort-kolom-description-tab-user-action | Search dan Sort Kolom Description Tab User Action | FE+BE | 20 | 185 |

Mode: `FE+BE` = backend nyata. Spec 011 `mock` (resilience: perilaku FE atas respons mock). Spec 003, 004, 036, 041, 052 memakai intercept parsial di atas backend nyata dan tetap `FE+BE` (alasan di `## Prerequisites` tiap spec). Kolom TC sumber memakai nomor `TC-AC-ACAL-NN`.

## 2. Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-AC-ACAL-01 | TC-AC-ACAL-E2E-001 | FE+BE |
| TC-AC-ACAL-02 | TC-AC-ACAL-E2E-047 | FE+BE |
| TC-AC-ACAL-03 | TC-AC-ACAL-E2E-048 | FE+BE |
| TC-AC-ACAL-04 | TC-AC-ACAL-E2E-004 | FE+BE |
| TC-AC-ACAL-05 | TC-AC-ACAL-E2E-003 | FE+BE |
| TC-AC-ACAL-06 | TC-AC-ACAL-E2E-003 | FE+BE |
| TC-AC-ACAL-07 | TC-AC-ACAL-E2E-004 | FE+BE |
| TC-AC-ACAL-08 | TC-AC-ACAL-E2E-004 | FE+BE |
| TC-AC-ACAL-09 | TC-AC-ACAL-E2E-011 | mock |
| TC-AC-ACAL-10 | TC-AC-ACAL-E2E-011 | mock |
| TC-AC-ACAL-11 | TC-AC-ACAL-E2E-002 | FE+BE |
| TC-AC-ACAL-12 | TC-AC-ACAL-E2E-002 | FE+BE |
| TC-AC-ACAL-13 | TC-AC-ACAL-E2E-049 | FE+BE |
| TC-AC-ACAL-14 | TC-AC-ACAL-E2E-005 | FE+BE |
| TC-AC-ACAL-15 | TC-AC-ACAL-E2E-005 | FE+BE |
| TC-AC-ACAL-16 | TC-AC-ACAL-E2E-001 | FE+BE |
| TC-AC-ACAL-17 | TC-AC-ACAL-E2E-047 | FE+BE |
| TC-AC-ACAL-18 | TC-AC-ACAL-E2E-006 | FE+BE |
| TC-AC-ACAL-19 | TC-AC-ACAL-E2E-007 | FE+BE |
| TC-AC-ACAL-20 | TC-AC-ACAL-E2E-006 | FE+BE |
| TC-AC-ACAL-21 | TC-AC-ACAL-E2E-007 | FE+BE |
| TC-AC-ACAL-22 | TC-AC-ACAL-E2E-007 | FE+BE |
| TC-AC-ACAL-23 | TC-AC-ACAL-E2E-007 | FE+BE |
| TC-AC-ACAL-24 | TC-AC-ACAL-E2E-006 | FE+BE |
| TC-AC-ACAL-25 | TC-AC-ACAL-E2E-012 | FE+BE |
| TC-AC-ACAL-26 | TC-AC-ACAL-E2E-012 | FE+BE |
| TC-AC-ACAL-27 | TC-AC-ACAL-E2E-012 | FE+BE |
| TC-AC-ACAL-28 | TC-AC-ACAL-E2E-013 | FE+BE |
| TC-AC-ACAL-29 | TC-AC-ACAL-E2E-013 | FE+BE |
| TC-AC-ACAL-30 | TC-AC-ACAL-E2E-013 | FE+BE |
| TC-AC-ACAL-31 | TC-AC-ACAL-E2E-013 | FE+BE |
| TC-AC-ACAL-32 | TC-AC-ACAL-E2E-013 | FE+BE |
| TC-AC-ACAL-33 | TC-AC-ACAL-E2E-014 | FE+BE |
| TC-AC-ACAL-34 | TC-AC-ACAL-E2E-014 | FE+BE |
| TC-AC-ACAL-35 | TC-AC-ACAL-E2E-014 | FE+BE |
| TC-AC-ACAL-36 | TC-AC-ACAL-E2E-014 | FE+BE |
| TC-AC-ACAL-37 | TC-AC-ACAL-E2E-015 | FE+BE |
| TC-AC-ACAL-38 | TC-AC-ACAL-E2E-015 | FE+BE |
| TC-AC-ACAL-39 | TC-AC-ACAL-E2E-015 | FE+BE |
| TC-AC-ACAL-40 | TC-AC-ACAL-E2E-016 | FE+BE |
| TC-AC-ACAL-41 | TC-AC-ACAL-E2E-016 | FE+BE |
| TC-AC-ACAL-42 | TC-AC-ACAL-E2E-017 | FE+BE |
| TC-AC-ACAL-43 | TC-AC-ACAL-E2E-016 | FE+BE |
| TC-AC-ACAL-44 | TC-AC-ACAL-E2E-022 | FE+BE |
| TC-AC-ACAL-45 | TC-AC-ACAL-E2E-022 | FE+BE |
| TC-AC-ACAL-46 | TC-AC-ACAL-E2E-022 | FE+BE |
| TC-AC-ACAL-47 | TC-AC-ACAL-E2E-022 | FE+BE |
| TC-AC-ACAL-48 | TC-AC-ACAL-E2E-021 | FE+BE |
| TC-AC-ACAL-49 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-50 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-51 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-52 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-53 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-54 | TC-AC-ACAL-E2E-023 | FE+BE |
| TC-AC-ACAL-55 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-56 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-57 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-58 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-59 | TC-AC-ACAL-E2E-034 | FE+BE |
| TC-AC-ACAL-60 | TC-AC-ACAL-E2E-037 | FE+BE |
| TC-AC-ACAL-61 | TC-AC-ACAL-E2E-034 | FE+BE |
| TC-AC-ACAL-62 | TC-AC-ACAL-E2E-034 | FE+BE |
| TC-AC-ACAL-63 | TC-AC-ACAL-E2E-034 | FE+BE |
| TC-AC-ACAL-64 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-65 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-66 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-67 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-68 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-69 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-70 | TC-AC-ACAL-E2E-035 | FE+BE |
| TC-AC-ACAL-71 | TC-AC-ACAL-E2E-036 | FE+BE |
| TC-AC-ACAL-72 | TC-AC-ACAL-E2E-036 | FE+BE |
| TC-AC-ACAL-73 | TC-AC-ACAL-E2E-036 | FE+BE |
| TC-AC-ACAL-74 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-75 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-76 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-77 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-78 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-79 | TC-AC-ACAL-E2E-025 | FE+BE |
| TC-AC-ACAL-80 | TC-AC-ACAL-E2E-026 | FE+BE |
| TC-AC-ACAL-81 | TC-AC-ACAL-E2E-026 | FE+BE |
| TC-AC-ACAL-82 | TC-AC-ACAL-E2E-026 | FE+BE |
| TC-AC-ACAL-83 | TC-AC-ACAL-E2E-027 | FE+BE |
| TC-AC-ACAL-84 | TC-AC-ACAL-E2E-027 | FE+BE |
| TC-AC-ACAL-85 | TC-AC-ACAL-E2E-027 | FE+BE |
| TC-AC-ACAL-86 | TC-AC-ACAL-E2E-026 | FE+BE |
| TC-AC-ACAL-87 | TC-AC-ACAL-E2E-026 | FE+BE |
| TC-AC-ACAL-88 | TC-AC-ACAL-E2E-028 | FE+BE |
| TC-AC-ACAL-89 | TC-AC-ACAL-E2E-029 | FE+BE |
| TC-AC-ACAL-90 | TC-AC-ACAL-E2E-054 | FE+BE |
| TC-AC-ACAL-91 | TC-AC-ACAL-E2E-029 | FE+BE |
| TC-AC-ACAL-92 | TC-AC-ACAL-E2E-029 | FE+BE |
| TC-AC-ACAL-93 | TC-AC-ACAL-E2E-054 | FE+BE |
| TC-AC-ACAL-94 | TC-AC-ACAL-E2E-029 | FE+BE |
| TC-AC-ACAL-95 | TC-AC-ACAL-E2E-030 | FE+BE |
| TC-AC-ACAL-96 | TC-AC-ACAL-E2E-030 | FE+BE |
| TC-AC-ACAL-97 | TC-AC-ACAL-E2E-030 | FE+BE |
| TC-AC-ACAL-98 | TC-AC-ACAL-E2E-030 | FE+BE |
| TC-AC-ACAL-99 | TC-AC-ACAL-E2E-034 | FE+BE |
| TC-AC-ACAL-100 | TC-AC-ACAL-E2E-031 | FE+BE |
| TC-AC-ACAL-101 | TC-AC-ACAL-E2E-031 | FE+BE |
| TC-AC-ACAL-102 | TC-AC-ACAL-E2E-031 | FE+BE |
| TC-AC-ACAL-103 | TC-AC-ACAL-E2E-031 | FE+BE |
| TC-AC-ACAL-104 | TC-AC-ACAL-E2E-032 | FE+BE |
| TC-AC-ACAL-105 | TC-AC-ACAL-E2E-032 | FE+BE |
| TC-AC-ACAL-106 | TC-AC-ACAL-E2E-032 | FE+BE |
| TC-AC-ACAL-107 | TC-AC-ACAL-E2E-033 | FE+BE |
| TC-AC-ACAL-108 | TC-AC-ACAL-E2E-033 | FE+BE |
| TC-AC-ACAL-109 | TC-AC-ACAL-E2E-033 | FE+BE |
| TC-AC-ACAL-110 | TC-AC-ACAL-E2E-032 | FE+BE |
| TC-AC-ACAL-111 | TC-AC-ACAL-E2E-032 | FE+BE |
| TC-AC-ACAL-112 | TC-AC-ACAL-E2E-008 | FE+BE |
| TC-AC-ACAL-113 | TC-AC-ACAL-E2E-050 | FE+BE |
| TC-AC-ACAL-114 | TC-AC-ACAL-E2E-051 | FE+BE |
| TC-AC-ACAL-115 | TC-AC-ACAL-E2E-008 | FE+BE |
| TC-AC-ACAL-116 | TC-AC-ACAL-E2E-009 | FE+BE |
| TC-AC-ACAL-117 | TC-AC-ACAL-E2E-009 | FE+BE |
| TC-AC-ACAL-118 | TC-AC-ACAL-E2E-010 | FE+BE |
| TC-AC-ACAL-119 | TC-AC-ACAL-E2E-010 | FE+BE |
| TC-AC-ACAL-120 | TC-AC-ACAL-E2E-051 | FE+BE |
| TC-AC-ACAL-121 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-122 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-123 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-124 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-125 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-126 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-127 | TC-AC-ACAL-E2E-040 | FE+BE |
| TC-AC-ACAL-128 | TC-AC-ACAL-E2E-039 | FE+BE |
| TC-AC-ACAL-129 | TC-AC-ACAL-E2E-041 | FE+BE |
| TC-AC-ACAL-130 | TC-AC-ACAL-E2E-041 | FE+BE |
| TC-AC-ACAL-131 | TC-AC-ACAL-E2E-011 | mock |
| TC-AC-ACAL-132 | TC-AC-ACAL-E2E-011 | mock |
| TC-AC-ACAL-133 | TC-AC-ACAL-E2E-021 | FE+BE |
| TC-AC-ACAL-134 | TC-AC-ACAL-E2E-040 | FE+BE |
| TC-AC-ACAL-135 | TC-AC-ACAL-E2E-037 | FE+BE |
| TC-AC-ACAL-136 | TC-AC-ACAL-E2E-037 | FE+BE |
| TC-AC-ACAL-137 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-138 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-139 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-140 | TC-AC-ACAL-E2E-046 | FE+BE |
| TC-AC-ACAL-141 | TC-AC-ACAL-E2E-046 | FE+BE |
| TC-AC-ACAL-142 | TC-AC-ACAL-E2E-046 | FE+BE |
| TC-AC-ACAL-143 | TC-AC-ACAL-E2E-045 | FE+BE |
| TC-AC-ACAL-144 | TC-AC-ACAL-E2E-045 | FE+BE |
| TC-AC-ACAL-145 | TC-AC-ACAL-E2E-045 | FE+BE |
| TC-AC-ACAL-146 | TC-AC-ACAL-E2E-052 | FE+BE |
| TC-AC-ACAL-147 | TC-AC-ACAL-E2E-045 | FE+BE |
| TC-AC-ACAL-148 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-149 | TC-AC-ACAL-E2E-018 | FE+BE |
| TC-AC-ACAL-150 | TC-AC-ACAL-E2E-020 | FE+BE |
| TC-AC-ACAL-151 | TC-AC-ACAL-E2E-020 | FE+BE |
| TC-AC-ACAL-152 | TC-AC-ACAL-E2E-020 | FE+BE |
| TC-AC-ACAL-153 | TC-AC-ACAL-E2E-020 | FE+BE |
| TC-AC-ACAL-154 | TC-AC-ACAL-E2E-019 | FE+BE |
| TC-AC-ACAL-155 | TC-AC-ACAL-E2E-044 | FE+BE |
| TC-AC-ACAL-156 | TC-AC-ACAL-E2E-020 | FE+BE |
| TC-AC-ACAL-157 | TC-AC-ACAL-E2E-017 | FE+BE |
| TC-AC-ACAL-158 | TC-AC-ACAL-E2E-042 | FE+BE |
| TC-AC-ACAL-159 | TC-AC-ACAL-E2E-042 | FE+BE |
| TC-AC-ACAL-160 | TC-AC-ACAL-E2E-019 | FE+BE |
| TC-AC-ACAL-161 | TC-AC-ACAL-E2E-044 | FE+BE |
| TC-AC-ACAL-162 | TC-AC-ACAL-E2E-018 | FE+BE |
| TC-AC-ACAL-163 | TC-AC-ACAL-E2E-053 | FE+BE |
| TC-AC-ACAL-164 | TC-AC-ACAL-E2E-041 | FE+BE |
| TC-AC-ACAL-165 | TC-AC-ACAL-E2E-005 | FE+BE |
| TC-AC-ACAL-166 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-167 | TC-AC-ACAL-E2E-036 | FE+BE |
| TC-AC-ACAL-168 | TC-AC-ACAL-E2E-014 | FE+BE |
| TC-AC-ACAL-169 | TC-AC-ACAL-E2E-018 | FE+BE |
| TC-AC-ACAL-170 | TC-AC-ACAL-E2E-038 | FE+BE |
| TC-AC-ACAL-171 | TC-AC-ACAL-E2E-042 | FE+BE |
| TC-AC-ACAL-172 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-173 | TC-AC-ACAL-E2E-024 | FE+BE |
| TC-AC-ACAL-174 | TC-AC-ACAL-E2E-002 | FE+BE |
| TC-AC-ACAL-175 | TC-AC-ACAL-E2E-052 | FE+BE |
| TC-AC-ACAL-176 | TC-AC-ACAL-E2E-030 | FE+BE |
| TC-AC-ACAL-177 | TC-AC-ACAL-E2E-043 | FE+BE |
| TC-AC-ACAL-178 | TC-AC-ACAL-E2E-044 | FE+BE |
| TC-AC-ACAL-179 | TC-AC-ACAL-E2E-040 | FE+BE |
| TC-AC-ACAL-180 | TC-AC-ACAL-E2E-038 | FE+BE |
| TC-AC-ACAL-181 | TC-AC-ACAL-E2E-005 | FE+BE |
| TC-AC-ACAL-184 | TC-AC-ACAL-E2E-028 | FE+BE |
| TC-AC-ACAL-185 | TC-AC-ACAL-E2E-055 | FE+BE |
| TC-AC-ACAL-186 | TC-AC-ACAL-E2E-040 | FE+BE |

Kolom BE per TC belum dapat diisi: `tc-activity-log-backend.md` disusun dari kontrak API dan tidak merujuk ID TC granular (konvensi bagian 8).

## 3. TC hanya-BE (dilewati)

| TC | Alasan |
|---|---|
| TC-AC-ACAL-182 | Bagian "6. Backend API Contract": filter `userId` dan `product` pada list Session tidak ada di Filter Panel UI (field UI hanya Date, User, Position, Division). Kontrak API murni (bagian 2); diliput TC BE (BE-002, BE-007, BE-008, BE-010). |
| TC-AC-ACAL-183 | Sama untuk User Action: filter `logTable`, `createdById`, `objectName`, dan `product` tidak ada di UI. Diliput TC BE (BE-015 list, BE-020 dan BE-021 options, BE-023 export). |

Keduanya tidak punya jalur UI; bila QA menilai filter API-only perlu bukti UI, keputusan diambil di luar halaman ini (opsi: tambah sebagai request langsung di spec defense-in-depth 020).

## 4. Temuan untuk QA (ringkasan)

Gabungan butir "Temuan untuk QA" di `## Notes` 55 spec (263 butir; rincian per spec ada di spec itu). Kelompok utama:

- **Akun dan password.** Email Pre-setup memuat placeholder `{namaCompany}` tanpa nilai; `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; nama lain yang dipakai spec (pola `AC_<ROLE>_PASSWORD`, `AC_<ENTITAS>_<ROLE>_PASSWORD`, `AC_DYN_PASSWORD`; daftar di `suite.md`) adalah usulan tim FE dan belum terdaftar. Email akun Principal mengikuti `.env.example` baris 28 (asumsi terbuka, FE mengonfirmasi saat login pertama).
- **Seeding data log.** TC, PRD, dan LLD tidak mendefinisikan cara membuat entri log bertanggal tertentu, stempel identik, volume 35 / 5.000 / 5.001 / 10.000 / 1.048.577, atau snapshot identitas. Kemampuan ini diminta dari tim FE/BE; spec tidak mengarang endpoint (S-13).
- **Entri audit trail permanen.** Beberapa TC mensyaratkan total mutlak (mis. TC-116 "35 entri per tab") atau "belum pernah ada log Object `Wallet`" (TC-166, kini entitas atau akun Principal segar per run); log tidak dapat dihapus sehingga spec mengasersi relatif terhadap baseline, memakai nama bersuffix, atau akun segar per run (S-12).
- **Data tidak disebut TC.** Banyak TC menyebut "menu lain", "kolom", "nama berkas", "posisi tujuan drag", "lebar viewport", route URL, atau nilai filter tanpa nilai; spec memilih nilai dan mencatatnya sebagai pilihan spec.
- **Expected kosong atau ambigu.** Expected bernilai `-` (TC-155, 157, 161, 147) tidak diasersi; Expected bersyarat (TC-54) hanya sebagian diasersi.
- **Perilaku belum ditetapkan PRD/TC.** Apakah [Apply] menutup Filter Panel, apakah Overlay Column Visibility menyimpan, kode status error export (TC-164), dan apakah stream SSE ikut gagal pada 5xx List.
- **Sumber hilang.** `auth/_foundation/auth-foundation.md` (aturan event buka/tutup sesi dan reset/change password) dirujuk TC-48 dan TC-147 tetapi tidak ada di workspace; asersi absence/event sesi dibuat dari TC saja.
- **Overlap data uji antar TC.** TC-53, 92, 98 memakai tanggal `18 Jun 2026` yang sama dengan Filter Date TC-59/99 (spec 034): lihat konflik asersi "hanya" di laporan hasil run.

## 5. Hasil check-suite

`python scripts/check-suite.py specs/AdminConsole/ActivityLog ../admin-console/activity-log/TestCases/tc-activity-log.md docs/coverage/AdminConsoleActivityLog.md`: 55 spec, 186 TC, 184 TC tercakup, 0 temuan `[FINDING]`, 0 `[REVIEW]` (exit 0).

`node_modules/.bin/spectra lint --strict specs/AdminConsole/ActivityLog`: 55 spec dan 1 suite terverifikasi, 0 error lint. Folder dan `id` spec 001, 008, 021, 022, 029, dan 046 disamakan dengan isinya (nomor tetap; 022 dan 046 diganti slug-nya setelah e2e-audit). Spec 011 (mock) memuat path, method, dan skema respons dari `API/openapi.yaml`; endpoint stream SSE tidak ada di dokumen API (Temuan untuk QA).

Cek R-01..R-21 dilaporkan ke user sebagai keputusan terpisah. Spec dengan lebih dari 35 langkah nominal yang dipertahankan (19 spec, aturan hitung check-suite C6 = langkah nominal): 001, 005, 007, 012, 014, 018, 020, 023, 024, 025, 026, 030, 032, 035, 036, 039, 043, 045, 046. Spec yang baru melewati 35 langkah setelah perulangan diperluas (8b.7) menulis alasannya di `## Notes`. Spec 001, 008, 021, dan 029 dipecah menjadi spec berukuran 35 langkah atau kurang (id baru 047 sampai 055).