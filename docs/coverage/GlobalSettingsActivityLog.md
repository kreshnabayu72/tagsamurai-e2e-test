# Coverage E2E — Global Settings > Activity Log

Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (215 TC aktif pasca pencabutan 5 TC mobile web-only) dan `global-settings/activity-log/TestCases/tc-activity-log-backend.md`.
Referensi: `global-settings/activity-log/TestCases/tc-activity-log-frontend.md`.
Suite: `specs/GlobalSettings/ActivityLog/`.
Prefix Modul: `GS` + `ACTLOG` (`TC-GS-ACTLOG-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (49 Spec Atomik)

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-ACTLOG-E2E-001 | Screening 3 Zona, navigasi tab Session dan User Action, serta perilaku baris non-interaktif | FE+BE | TC-GS-ACTLOG-01, 02, 03, 240 |
| TC-GS-ACTLOG-E2E-002 | Loading skeleton dan ketahanan terhadap kegagalan pembacaan data di kedua tab | mock | TC-GS-ACTLOG-04, 05, 10, 11 |
| TC-GS-ACTLOG-E2E-003 | Tampilan empty state genuinely kosong saat entitas baru belum memiliki riwayat aktivitas | FE+BE | TC-GS-ACTLOG-06, 07 |
| TC-GS-ACTLOG-E2E-004 | Tampilan no-result state saat pencarian atau penyaringan tidak menghasilkan data | FE+BE | TC-GS-ACTLOG-08, 09 |
| TC-GS-ACTLOG-E2E-005 | Default sort Date descending dan format timestamp mengikuti konfigurasi General Settings | FE+BE | TC-GS-ACTLOG-12, 13, 220, 221 |
| TC-GS-ACTLOG-E2E-006 | Hover tooltip pada icon table tools dan teks lengkap untuk nama yang terpotong | mock | TC-GS-ACTLOG-18, 19 |
| TC-GS-ACTLOG-E2E-007 | Siklus lengkap Guided Tooltip walkthrough, navigasi, auto-trigger, dan manual replay | mock | TC-GS-ACTLOG-20, 21, 22, 23, 24 |
| TC-GS-ACTLOG-E2E-008 | Role Matrix Positif: Total Control dan Read Only memiliki akses baca penuh dan UI identik | FE+BE | TC-GS-ACTLOG-26, 27 |
| TC-GS-ACTLOG-E2E-009 | Role Matrix Negatif: Pengguna tanpa akses tidak melihat menu Activity Log dan direct URL ditolak 403 | FE+BE | TC-GS-ACTLOG-28, 29 |
| TC-GS-ACTLOG-E2E-010 | Isolasi data log per tenant tanpa kebocoran data atau opsi agregasi lintas entitas | FE+BE | TC-GS-ACTLOG-30 |
| TC-GS-ACTLOG-E2E-011 | Tab Session: Pencarian per kolom untuk 9 kolom teks dan guard Date tidak searchable | FE+BE | TC-GS-ACTLOG-31, 32, 33, 34, 35, 36, 37, 38, 39, 40 |
| TC-GS-ACTLOG-E2E-012 | Tab Session: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse | FE+BE | TC-GS-ACTLOG-41 |
| TC-GS-ACTLOG-E2E-013 | Tab Session: Struktur 6 field Filter Panel dan penerapan filter individual | FE+BE | TC-GS-ACTLOG-42, 43, 44, 45, 46, 47, 48, 49, 241 |
| TC-GS-ACTLOG-E2E-014 | Tab Session: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference | FE+BE | TC-GS-ACTLOG-50, 51, 52, 53, 54, 56, 57, 58 |
| TC-GS-ACTLOG-E2E-015 | Tab Session: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah | FE+BE | TC-GS-ACTLOG-59, 60, 61, 62, 63, 64, 65, 222 |
| TC-GS-ACTLOG-E2E-016 | Tab Session: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state | FE+BE | TC-GS-ACTLOG-66, 67, 68, 69, 70, 71, 72, 73 |
| TC-GS-ACTLOG-E2E-017 | Tab Session: Guard ketiadaan checkbox seleksi dan aksi bulk karena modul read-only murni | FE+BE | TC-GS-ACTLOG-74 |
| TC-GS-ACTLOG-E2E-018 | Tab Session: Sorting 3-state untuk 10 kolom tabel dan penempatan nilai kosong di akhir | FE+BE | TC-GS-ACTLOG-76, 77, 78, 79, 80, 81, 82, 83, 84, 85 |
| TC-GS-ACTLOG-E2E-019 | Tab Session: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible | FE+BE | TC-GS-ACTLOG-86, 87, 89 |
| TC-GS-ACTLOG-E2E-020 | Tab Session: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5 | FE+BE | TC-GS-ACTLOG-88, 90, 91, 92, 93, 94, 95, 96, 97 |
| TC-GS-ACTLOG-E2E-021 | Tab Session: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5 | FE+BE | TC-GS-ACTLOG-98, 99, 100, 101, 102, 103, 104, 105, 106, 107 |
| TC-GS-ACTLOG-E2E-022 | Tab Session: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column | FE+BE | TC-GS-ACTLOG-108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119 |
| TC-GS-ACTLOG-E2E-023 | Tab Session: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server | FE+BE | TC-GS-ACTLOG-120, 121 |
| TC-GS-ACTLOG-E2E-024 | Tab Session: Download log >5.000 baris memicu operasi background, toast persiapan, dan notifikasi in-app | FE+BE | TC-GS-ACTLOG-122 |
| TC-GS-ACTLOG-E2E-025 | Tab Session: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi | FE+BE | TC-GS-ACTLOG-200 |
| TC-GS-ACTLOG-E2E-026 | Tab User Action: Pencarian per kolom untuk 7 kolom teks, guard Date, dan pencarian multi-kolom | FE+BE | TC-GS-ACTLOG-123, 124, 125, 126, 127, 128, 129, 130, 131 |
| TC-GS-ACTLOG-E2E-027 | Tab User Action: Pola interaksi toolbar Search Box reveal, clear tanpa reset, submit, dan collapse | FE+BE | TC-GS-ACTLOG-132 |
| TC-GS-ACTLOG-E2E-028 | Tab User Action: Struktur 4 field Filter Panel dan penerapan filter individual | FE+BE | TC-GS-ACTLOG-133, 134, 135, 136, 137 |
| TC-GS-ACTLOG-E2E-029 | Tab User Action: Sumber opsi dropdown filter terpopulasi dari data log aktual dan penanganan stale reference | FE+BE | TC-GS-ACTLOG-138, 139, 140, 142, 143, 144 |
| TC-GS-ACTLOG-E2E-030 | Tab User Action: Search internal dropdown, logika OR dalam satu field, dan siklus chip seleksi 2-arah | FE+BE | TC-GS-ACTLOG-145, 146, 147, 148, 149, 150, 151, 223 |
| TC-GS-ACTLOG-E2E-031 | Tab User Action: Kombinasi multi-field filter (AND), alur Search dan Filter, independensi reset, dan pemulihan empty state | FE+BE | TC-GS-ACTLOG-152, 153, 154, 155, 156, 157, 158, 159 |
| TC-GS-ACTLOG-E2E-032 | Tab User Action: Sorting 3-state untuk 8 kolom tabel dan penempatan baris Import/Create kosong di akhir | FE+BE | TC-GS-ACTLOG-161, 162, 163, 164, 165, 166, 167, 168 |
| TC-GS-ACTLOG-E2E-033 | Tab User Action: Screening Setup Column overlay, popup modal live preview, dan guard minimal 1 kolom visible | FE+BE | TC-GS-ACTLOG-169, 170, 172 |
| TC-GS-ACTLOG-E2E-034 | Tab User Action: Pengaturan visibilitas kolom hideable pada Setup Column dan persistensi refresh F5 | FE+BE | TC-GS-ACTLOG-171, 173, 174, 175, 176, 177, 178 |
| TC-GS-ACTLOG-E2E-035 | Tab User Action: Pengaturan urutan kolom tabel via drag-and-drop Setup Column dan persistensi refresh F5 | FE+BE | TC-GS-ACTLOG-179, 180, 181, 182, 183, 184, 185, 186 |
| TC-GS-ACTLOG-E2E-036 | Tab User Action: Pembekuan kolom sticky pin/unpin, reset ke default, dan pembatalan perubahan Setup Column | FE+BE | TC-GS-ACTLOG-187, 188, 189, 190, 191, 192, 193, 194, 195, 196 |
| TC-GS-ACTLOG-E2E-037 | Tab User Action: Download log CSV/XLSX sesuai filter aktif (≤5.000 baris) dan penanganan kegagalan server | FE+BE | TC-GS-ACTLOG-197, 198 |
| TC-GS-ACTLOG-E2E-038 | Tab User Action: Download log >5.000 baris memicu operasi background, toast persiapan, dan notifikasi in-app | FE+BE | TC-GS-ACTLOG-199 |
| TC-GS-ACTLOG-E2E-039 | Tab User Action: Pergantian page size pagination 25/50/100 baris menampilkan jumlah data presisi | FE+BE | TC-GS-ACTLOG-201 |
| TC-GS-ACTLOG-E2E-040 | Sinkronisasi real-time SSE: Entri baru di Tab Session dan Tab User Action muncul otomatis tanpa reload | FE+BE | TC-GS-ACTLOG-224, 225 |
| TC-GS-ACTLOG-E2E-041 | Sinkronisasi real-time SSE: Opsi dropdown Filter Panel terupdate otomatis saat entitas baru tercatat | FE+BE | TC-GS-ACTLOG-55, 141 |
| TC-GS-ACTLOG-E2E-042 | Sinkronisasi real-time SSE saat tabel terfilter mengecualikan event baru yang tidak cocok kriteria | FE+BE | TC-GS-ACTLOG-75, 160 |
| TC-GS-ACTLOG-E2E-043 | Sinkronisasi 2-arah sesi Global Settings Dual-Role mencatat event Session started dan Session ended | FE+BE | TC-GS-ACTLOG-226 |
| TC-GS-ACTLOG-E2E-044 | Sanitasi input XSS pada Search Box dan penegasan IP Address ditampilkan penuh tanpa masking | FE+BE | TC-GS-ACTLOG-230, 231 |
| TC-GS-ACTLOG-E2E-045 | D1 Client Suspended/Expired tetap dapat mengakses dan melihat riwayat log Activity Log | FE+BE | TC-GS-ACTLOG-232 |
| TC-GS-ACTLOG-E2E-046 | D3 Snapshot Immutability data historis log terhadap mutasi nama pengguna atau admin di masa kini | FE+BE | TC-GS-ACTLOG-234, 235 |
| TC-GS-ACTLOG-E2E-047 | D5 Opsi filter None tidak muncul pada dropdown Activity dan Action karena kolom non-nullable | FE+BE | TC-GS-ACTLOG-236 |
| TC-GS-ACTLOG-E2E-048 | D9 Multi-field edit dalam satu kali simpan menghasilkan N entri changelog terpisah bertimestamp identik | FE+BE | TC-GS-ACTLOG-238 |
| TC-GS-ACTLOG-E2E-049 | 8d-1 Seluruh fitur dan perilaku Activity Log berlaku identik di seluruh tier lisensi plan | FE+BE | TC-GS-ACTLOG-239 |

---

## 2. Alasan TC Hanya-BE (Tidak Masuk Spec E2E)

| TC ID | Skenario | Alasan Tidak Masuk Spec E2E |
|---|---|---|
| TC-GS-ACTLOG-233 | D1 — Ingestion Tetap Tercatat Meski Client Suspended | Menguji job otomatis ingestion background tetap mencatat audit trail saat client suspended (`PIC FE: -`, `PIC BE: v`); verifikasi langsung pada database/endpoint backend. |
| TC-GS-ACTLOG-237 | D7 — Ingestion Out-of-Order Tetap Terurut by Timestamp | Menguji ketahanan mekanisme ingestion server menyusun event yang tiba acak karena network delay (`PIC FE: -`, `PIC BE: v`); diuji via backend concurrency injection. |

---

## 3. Lapisan per TC (Seluruh 215 TC Granular Aktif)

| TC ID | Skenario | Prioritas | Lapisan | Spec E2E | Mode | Catatan |
|---|---|:---:|:---:|---|:---:|---|
| TC-GS-ACTLOG-01 | Screening 3 Zona — Tab Session | Filter \ | E2E | TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab | FE+BE | |
| TC-GS-ACTLOG-02 | Screening 3 Zona — Tab User Action | Filter \ | E2E | TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab | FE+BE | |
| TC-GS-ACTLOG-03 | Tab switch — Filter & Search independen per tab | P1 | E2E | TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab | FE+BE | |
| TC-GS-ACTLOG-04 | Loading state — Tab Session | P2 | E2E | TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-ACTLOG-05 | Loading state — Tab User Action | P2 | E2E | TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-ACTLOG-06 | Empty state genuinely kosong — Tab Session | P1 | E2E | TC-GS-ACTLOG-E2E-003-empty-state-genuinely-kosong | FE+BE | |
| TC-GS-ACTLOG-07 | Empty state genuinely kosong — Tab User Action | P1 | E2E | TC-GS-ACTLOG-E2E-003-empty-state-genuinely-kosong | FE+BE | |
| TC-GS-ACTLOG-08 | No-result state — Tab Session, Search/Filter tanpa hasil | P1 | E2E | TC-GS-ACTLOG-E2E-004-no-result-state-pencarian-tanpa-hasil | FE+BE | |
| TC-GS-ACTLOG-09 | No-result state — Tab User Action, Search/Filter tanpa hasil | P1 | E2E | TC-GS-ACTLOG-E2E-004-no-result-state-pencarian-tanpa-hasil | FE+BE | |
| TC-GS-ACTLOG-10 | Read-failure resilience — Tab Session | P2 | E2E | TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-ACTLOG-11 | Read-failure resilience — Tab User Action | P2 | E2E | TC-GS-ACTLOG-E2E-002-loading-skeleton-dan-read-failure-resilience | mock | |
| TC-GS-ACTLOG-12 | Default sort Date descending — Tab Session | P1 | E2E | TC-GS-ACTLOG-E2E-005-default-sort-dan-format-timestamp-general-settings | FE+BE | |
| TC-GS-ACTLOG-13 | Default sort Date descending — Tab User Action | P1 | E2E | TC-GS-ACTLOG-E2E-005-default-sort-dan-format-timestamp-general-settings | FE+BE | |
| TC-GS-ACTLOG-18 | Hover Tooltip — Icon Table Tools (Search, Filter, Download, Setup Column) | P2 | E2E | TC-GS-ACTLOG-E2E-006-hover-tooltip-toolbar-dan-teks-terpotong | mock | |
| TC-GS-ACTLOG-19 | Hover Tooltip — Nama User/Modified By terpotong | P2 | E2E | TC-GS-ACTLOG-E2E-006-hover-tooltip-toolbar-dan-teks-terpotong | mock | |
| TC-GS-ACTLOG-20 | Guided Tooltip — Screening Konten 2 Step Verbatim | P2 | E2E | TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough | mock | |
| TC-GS-ACTLOG-21 | Guided Tooltip — Trigger Auto First Visit & Tidak Muncul Lagi | P2 | E2E | TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough | mock | |
| TC-GS-ACTLOG-22 | Guided Tooltip — Trigger Manual Replay via `[?]` | P2 | E2E | TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough | mock | |
| TC-GS-ACTLOG-23 | Guided Tooltip — Siklus Navigasi Skip/Back/Next/Done | P2 | E2E | TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough | mock | |
| TC-GS-ACTLOG-24 | Guided Tooltip — Exit Tanpa Selesai (Resize/Navigasi Keluar) | P2 | E2E | TC-GS-ACTLOG-E2E-007-guided-tooltip-walkthrough | mock | |
| TC-GS-ACTLOG-26 | Matriks Visibilitas — Total Control | P0 | E2E | TC-GS-ACTLOG-E2E-008-role-matrix-positif-total-control-dan-read-only | FE+BE | |
| TC-GS-ACTLOG-27 | Matriks Visibilitas — Read Only (identik Total Control) | P0 | E2E | TC-GS-ACTLOG-E2E-008-role-matrix-positif-total-control-dan-read-only | FE+BE | |
| TC-GS-ACTLOG-28 | Matriks Visibilitas — Role/Capability Lain (Tidak Ada Akses) | P1 | E2E | TC-GS-ACTLOG-E2E-009-role-matrix-negatif-pengguna-tanpa-akses | FE+BE | |
| TC-GS-ACTLOG-29 | Direct URL Access — Tanpa Izin | P1 | E2E | TC-GS-ACTLOG-E2E-009-role-matrix-negatif-pengguna-tanpa-akses | FE+BE | |
| TC-GS-ACTLOG-30 | Data Visibility — Scope Entitas Aktif, Tidak Ada Agregasi Lintas-Entitas | P0 | E2E | TC-GS-ACTLOG-E2E-010-tenant-scoping-dan-isolasi-data | FE+BE | |
| TC-GS-ACTLOG-31 | Search — User | P0 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-32 | Search — Employee ID | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-33 | Search — Position | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-34 | Search — Division | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-35 | Search — Activity | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-36 | Search — Status | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-37 | Search — Note | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-38 | Search — IP Address | P2 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-39 | Search — Device / Browser | P2 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-40 | Guard — Date TIDAK Searchable via Search Box | P1 | E2E | TC-GS-ACTLOG-E2E-011-tab-session-search-per-kolom-dan-guard-date | FE+BE | |
| TC-GS-ACTLOG-41 | Pola Interaksi Search Box Toolbar — Reveal/Clear/Collapse | P2 | E2E | TC-GS-ACTLOG-E2E-012-tab-session-pola-interaksi-search-box-toolbar | FE+BE | |
| TC-GS-ACTLOG-42 | Screening Struktur Filter Panel — Tab Session (6 field) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-43 | Filter — Date (1 field, bukan range) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-44 | Filter — User (multi-select, searchable) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-45 | Filter — Position (multi-select, searchable, FK) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-46 | Filter — Division (multi-select, searchable, FK) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-47 | Filter — Activity (multi-select) | P0 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-48 | Filter — Activity = Session (GS Dual-Role) | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-241 | Filter — Activity = Change Password | P1 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-49 | Filter — Status (multi-select, guard Logout/Session tidak ikut match) | P0 | E2E | TC-GS-ACTLOG-E2E-013-tab-session-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-50 | Screening Isi Opsi — User (Populate) | P1 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-51 | Screening Isi Opsi — Position (Populate, Scope dari Log) | P1 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-52 | Screening Isi Opsi — Division (Populate, Scope dari Log) | P1 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-53 | Screening Isi Opsi — Activity (Populate dari Data Tabel) | Session` — `Change Password`/`Reset Password` **tidak tampil** karena belum genuinely muncul di data tabel saat ini (`prd-conventions.md` §9.8, bukan enum statis penuh) | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-54 | Screening Isi Opsi — Status (Populate dari Data Tabel) | P1 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-55 | Populate — Update Real-time Opsi User | P2 | E2E | TC-GS-ACTLOG-E2E-041-sinkronisasi-real-time-sse-update-opsi-dropdown-filter | FE+BE | |
| TC-GS-ACTLOG-56 | Populate — Loading State Dropdown | P2 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-57 | Populate — Empty Source | P2 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-58 | Populate — Stale Reference pada Kriteria Filter Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-014-tab-session-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-59 | Search-within-Dropdown — Field User | P2 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-60 | OR-Logic dalam Field — Activity (>1 opsi dalam 1 field) | P1 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-61 | Kemunculan Chip — Field User | P2 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-62 | Removal via `(X)` per Chip — Field User (arah chip→checkbox) | P1 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-63 | Removal via Uncheck di DALAM Dropdown Terbuka — Field User (arah checkbox→chip) | P1 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-64 | Overflow Banyak Chip — Field User | P3 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-65 | Kondensasi — Chip Removal 2-Arah & Overflow untuk Position/Division/Activity/Status | P2 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-66 | Kombinasi Multi-Field Filter (AND) | P1 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-67 | Alur Search → Filter | P1 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-68 | Alur Filter → Search | P1 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-69 | Kombinasi Penuh 4 Kontrol (Search + Filter + Sort + Pagination) | P2 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-70 | Clear Filter saat Search & Sort Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-71 | Clear Search saat Filter & Sort Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-72 | Transisi Target Sort saat Search & Filter Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-73 | Pemulihan Empty State (Recovery) | P2 | E2E | TC-GS-ACTLOG-E2E-016-tab-session-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-74 | Retensi Seleksi Checkbox — TIDAK APPLICABLE | P3 | E2E | TC-GS-ACTLOG-E2E-017-tab-session-guard-ketiadaan-seleksi-checkbox | FE+BE | |
| TC-GS-ACTLOG-75 | Mutasi Real-time saat Tabel Terfilter | P2 | E2E | TC-GS-ACTLOG-E2E-042-sinkronisasi-real-time-sse-tabel-terfilter-mengecualikan-event-non-matching | FE+BE | |
| TC-GS-ACTLOG-76 | Sorting 3-State — kolom Date (default sort) | P1 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-77 | Sorting 3-State — kolom User (nama lengkap, bukan badge terpotong) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-78 | Sorting 3-State — kolom Employee ID (kosong di akhir) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-79 | Sorting 3-State — kolom Position (kosong di akhir) | P1 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-80 | Sorting 3-State — kolom Division (kosong di akhir) | P1 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-81 | Sorting 3-State — kolom Activity (alfabetis, tidak pernah kosong) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-82 | Sorting 3-State — kolom Status (`—` Logout/Session di akhir) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-83 | Sorting 3-State — kolom Note (kosong di akhir) | P1 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-84 | Sorting 3-State — kolom IP Address (string-based, bukan numeric per-oktet) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-85 | Sorting 3-State — kolom Device/Browser (tidak terparse di akhir) | P2 | E2E | TC-GS-ACTLOG-E2E-018-tab-session-sorting-3-state-10-kolom | FE+BE | |
| TC-GS-ACTLOG-86 | Setup Column — Screening Overlay 10 Kolom | P1 | E2E | TC-GS-ACTLOG-E2E-019-tab-session-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-87 | Setup Column — Screening Popup Modal & Live Preview | P2 | E2E | TC-GS-ACTLOG-E2E-019-tab-session-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-88 | Kolom `Date` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-89 | Kolom `User` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-ACTLOG-E2E-019-tab-session-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-90 | Kolom `Employee ID` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-91 | Kolom `Position` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-92 | Kolom `Division` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-93 | Kolom `Activity` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-94 | Kolom `Status` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-95 | Kolom `Note` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-96 | Kolom `IP Address` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-97 | Kolom `Device / Browser` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-020-tab-session-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-98 | Kolom `Date` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-99 | Kolom `User` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-100 | Kolom `Employee ID` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-101 | Kolom `Position` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-102 | Kolom `Division` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-103 | Kolom `Activity` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-104 | Kolom `Status` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-105 | Kolom `Note` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-106 | Kolom `IP Address` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-107 | Kolom `Device / Browser` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-021-tab-session-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-108 | Kolom `Date` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-109 | Kolom `User` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-110 | Kolom `Employee ID` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-111 | Kolom `Position` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-112 | Kolom `Division` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-113 | Kolom `Activity` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-114 | Kolom `Status` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-115 | Kolom `Note` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-116 | Kolom `IP Address` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-117 | Kolom `Device / Browser` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-118 | Tombol `[Reset to Default]` — Tab Session | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-119 | Tombol `[Cancel]`/Icon Silang `(X)` — Discard, Tab Session | P2 | E2E | TC-GS-ACTLOG-E2E-022-tab-session-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-120 | Download Tab Session — CSV/XLSX Sesuai Filter Aktif | P1 | E2E | TC-GS-ACTLOG-E2E-023-tab-session-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-ACTLOG-121 | Download Tab Session — Gagal | P2 | E2E | TC-GS-ACTLOG-E2E-023-tab-session-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-ACTLOG-122 | Download Tab Session — >5.000 Baris (Long-Running Background Operation) | P2 | E2E | TC-GS-ACTLOG-E2E-024-tab-session-download-background-operation-diatas-5000-baris | FE+BE | |
| TC-GS-ACTLOG-200 | Pagination — Page Size 25/50/100 Menampilkan Jumlah Baris Sesuai Pilihan — Tab Session | P1 | E2E | TC-GS-ACTLOG-E2E-025-tab-session-pagination-page-size-25-50-100 | FE+BE | |
| TC-GS-ACTLOG-123 | Search — Action | P0 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-124 | Search — Object | P0 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-125 | Search — Name | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-126 | Search — Field | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-127 | Search — Old Value | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-128 | Search — New Value | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-129 | Search — Modified By | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-130 | Guard — Date TIDAK Searchable via Search Box | P1 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-131 | Search — 1 Keyword Match Banyak Kolom Sekaligus | P2 | E2E | TC-GS-ACTLOG-E2E-026-tab-user-action-search-per-kolom-dan-multi-kolom | FE+BE | |
| TC-GS-ACTLOG-132 | Pola Interaksi Search Box Toolbar — Reveal/Clear/Collapse | P2 | E2E | TC-GS-ACTLOG-E2E-027-tab-user-action-pola-interaksi-search-box-toolbar | FE+BE | |
| TC-GS-ACTLOG-133 | Screening Struktur Filter Panel — Tab User Action (4 field) | P1 | E2E | TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-134 | Filter — Date (1 field, bukan range) | P1 | E2E | TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-135 | Filter — Action (multi-select) | P0 | E2E | TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-136 | Filter — Object (multi-select) | P0 | E2E | TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-137 | Filter — Modified By (multi-select, searchable) | P1 | E2E | TC-GS-ACTLOG-E2E-028-tab-user-action-struktur-filter-panel-dan-filter-individual | FE+BE | |
| TC-GS-ACTLOG-138 | Screening Isi Opsi — Action (Populate, Scope dari Log — BUKAN Seluruh Enum) | P1 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-139 | Screening Isi Opsi — Object (Populate, Scope dari Log) | P1 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-140 | Screening Isi Opsi — Modified By (Populate) | P1 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-141 | Populate — Update Real-time Opsi Action | P2 | E2E | TC-GS-ACTLOG-E2E-041-sinkronisasi-real-time-sse-update-opsi-dropdown-filter | FE+BE | |
| TC-GS-ACTLOG-142 | Populate — Loading State Dropdown | P2 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-143 | Populate — Empty Source | P2 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-144 | Populate — Stale Reference pada Kriteria Filter Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-029-tab-user-action-populate-opsi-filter-dari-data-log | FE+BE | |
| TC-GS-ACTLOG-145 | Search-within-Dropdown — Field Modified By | P2 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-146 | OR-Logic dalam Field — Action (>1 opsi dalam 1 field) | P1 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-147 | Kemunculan Chip — Field Action | P2 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-148 | Removal via `(X)` per Chip — Field Action (arah chip→checkbox) | P1 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-149 | Removal via Uncheck di DALAM Dropdown Terbuka — Field Action (arah checkbox→chip) | P1 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-150 | Overflow Banyak Chip — Field Action | P3 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-151 | Kondensasi — Chip Removal 2-Arah & Overflow untuk Object/Modified By | P2 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-152 | Kombinasi Multi-Field Filter (AND) | P1 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-153 | Alur Search → Filter | P1 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-154 | Alur Filter → Search | P1 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-155 | Kombinasi Penuh 4 Kontrol (Search + Filter + Sort + Pagination) | P2 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-156 | Clear Filter saat Search & Sort Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-157 | Clear Search saat Filter & Sort Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-158 | Transisi Target Sort saat Search & Filter Aktif | P2 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-159 | Pemulihan Empty State (Recovery) | P2 | E2E | TC-GS-ACTLOG-E2E-031-tab-user-action-kombinasi-multi-filter-alur-search-dan-recovery | FE+BE | |
| TC-GS-ACTLOG-160 | Mutasi Real-time saat Tabel Terfilter | P2 | E2E | TC-GS-ACTLOG-E2E-042-sinkronisasi-real-time-sse-tabel-terfilter-mengecualikan-event-non-matching | FE+BE | |
| TC-GS-ACTLOG-161 | Sorting 3-State — kolom Date (default sort) | P1 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-162 | Sorting 3-State — kolom Action (alfabetis) | P2 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-163 | Sorting 3-State — kolom Object (alfabetis) | P2 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-164 | Sorting 3-State — kolom Name (Import bulk `—` di akhir) | P1 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-165 | Sorting 3-State — kolom Field (kosong Create/Delete di akhir) | P1 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-166 | Sorting 3-State — kolom Old Value (kolom campuran tipe) | P2 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-167 | Sorting 3-State — kolom New Value (kolom campuran tipe) | P2 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-168 | Sorting 3-State — kolom Modified By (nama lengkap, bukan badge terpotong) | P2 | E2E | TC-GS-ACTLOG-E2E-032-tab-user-action-sorting-3-state-8-kolom | FE+BE | |
| TC-GS-ACTLOG-169 | Setup Column — Screening Overlay 8 Kolom | P1 | E2E | TC-GS-ACTLOG-E2E-033-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-170 | Setup Column — Screening Popup Modal & Live Preview | P2 | E2E | TC-GS-ACTLOG-E2E-033-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-171 | Kolom `Date` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-172 | Kolom `Action` — guard generik minimal 1 kolom visible (§9.3 `prd-conventions.md`) | P2 | E2E | TC-GS-ACTLOG-E2E-033-tab-user-action-setup-column-screening-dan-guard-minimal-1-kolom | FE+BE | |
| TC-GS-ACTLOG-173 | Kolom `Object` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-174 | Kolom `Name` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-175 | Kolom `Field` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-176 | Kolom `Old Value` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-177 | Kolom `New Value` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-178 | Kolom `Modified By` (☑ Hideable) — Ceklis/Unceklis di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-034-tab-user-action-setup-column-visibilitas-kolom-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-179 | Kolom `Date` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-180 | Kolom `Action` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-181 | Kolom `Object` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-182 | Kolom `Name` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-183 | Kolom `Field` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-184 | Kolom `Old Value` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-185 | Kolom `New Value` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-186 | Kolom `Modified By` (☑ Hideable) — Geser di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-035-tab-user-action-setup-column-urutan-drag-drop-dan-persistensi-f5 | FE+BE | |
| TC-GS-ACTLOG-187 | Kolom `Date` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-188 | Kolom `Action` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-189 | Kolom `Object` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-190 | Kolom `Name` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-191 | Kolom `Field` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-192 | Kolom `Old Value` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-193 | Kolom `New Value` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-194 | Kolom `Modified By` (☑ Hideable) — Pin/Unpin di Popup Modal | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-195 | Tombol `[Reset to Default]` — Tab User Action | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-196 | Tombol `[Cancel]`/Icon Silang `(X)` — Discard, Tab User Action | P2 | E2E | TC-GS-ACTLOG-E2E-036-tab-user-action-setup-column-pin-sticky-reset-default-dan-cancel | FE+BE | |
| TC-GS-ACTLOG-197 | Download Tab User Action — CSV/XLSX Sesuai Filter Aktif | P1 | E2E | TC-GS-ACTLOG-E2E-037-tab-user-action-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-ACTLOG-198 | Download Tab User Action — Gagal | P2 | E2E | TC-GS-ACTLOG-E2E-037-tab-user-action-download-csv-xlsx-dan-penanganan-error | FE+BE | |
| TC-GS-ACTLOG-199 | Download Tab User Action — >5.000 Baris (Long-Running Background Operation) | P2 | E2E | TC-GS-ACTLOG-E2E-038-tab-user-action-download-background-operation-diatas-5000-baris | FE+BE | |
| TC-GS-ACTLOG-201 | Pagination — Page Size 25/50/100 Menampilkan Jumlah Baris Sesuai Pilihan — Tab User Action | P1 | E2E | TC-GS-ACTLOG-E2E-039-tab-user-action-pagination-page-size-25-50-100 | FE+BE | |
| TC-GS-ACTLOG-220 | Date/Time Format — Kolom Timestamp Tab Session Ikut General Settings | P1 | E2E | TC-GS-ACTLOG-E2E-005-default-sort-dan-format-timestamp-general-settings | FE+BE | |
| TC-GS-ACTLOG-221 | Date/Time Format — Kolom Timestamp Tab User Action Ikut General Settings | P1 | E2E | TC-GS-ACTLOG-E2E-005-default-sort-dan-format-timestamp-general-settings | FE+BE | |
| TC-GS-ACTLOG-222 | Date/Time Format — Isian Input Date Filter Tab Session | P2 | E2E | TC-GS-ACTLOG-E2E-015-tab-session-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-223 | Date/Time Format — Isian Input Date Filter Tab User Action | P2 | E2E | TC-GS-ACTLOG-E2E-030-tab-user-action-search-dropdown-logika-or-dan-chip-removal | FE+BE | |
| TC-GS-ACTLOG-224 | Sinkronisasi Real-time (SSE) — Entri Baru Tab User Action | P1 | E2E | TC-GS-ACTLOG-E2E-040-sinkronisasi-real-time-sse-entri-baru-kedua-tab | FE+BE | |
| TC-GS-ACTLOG-225 | Sinkronisasi Real-time (SSE) — Entri Baru Tab Session | P1 | E2E | TC-GS-ACTLOG-E2E-040-sinkronisasi-real-time-sse-entri-baru-kedua-tab | FE+BE | |
| TC-GS-ACTLOG-226 | Sinkronisasi 2 Arah — Event Buka/Tutup GS Sendiri (Dual-Role) | P1 | E2E | TC-GS-ACTLOG-E2E-043-sinkronisasi-2-arah-sesi-global-settings-dual-role | FE+BE | |
| TC-GS-ACTLOG-230 | XSS — Payload Script di Search Box Tersanitasi | P1 | E2E | TC-GS-ACTLOG-E2E-044-sanitasi-xss-search-box-dan-kolom-ip-address-tanpa-masking | FE+BE | |
| TC-GS-ACTLOG-231 | IP Address Tidak Di-mask (Keputusan Eksplisit) | P2 | E2E | TC-GS-ACTLOG-E2E-044-sanitasi-xss-search-box-dan-kolom-ip-address-tanpa-masking | FE+BE | |
| TC-GS-ACTLOG-232 | D1 — View Tetap Berfungsi saat Client Suspended/Expired | P2 | E2E | TC-GS-ACTLOG-E2E-045-client-suspended-tetap-dapat-melihat-riwayat-log | FE+BE | |
| TC-GS-ACTLOG-233 | D1 — Ingestion Tetap Tercatat Meski Client Suspended | P2 | BE | — | — | Backend ingestion murni |
| TC-GS-ACTLOG-234 | D3 — Snapshot Immutability Tab Session | P1 | E2E | TC-GS-ACTLOG-E2E-046-snapshot-immutability-data-historis-log-terhadap-mutasi-nama | FE+BE | |
| TC-GS-ACTLOG-235 | D3 — Snapshot Immutability Tab User Action | P1 | E2E | TC-GS-ACTLOG-E2E-046-snapshot-immutability-data-historis-log-terhadap-mutasi-nama | FE+BE | |
| TC-GS-ACTLOG-236 | D5 — Opsi Filter "None" Tidak Muncul pada Kolom Tanpa Null | P2 | E2E | TC-GS-ACTLOG-E2E-047-opsi-filter-none-tidak-muncul-pada-kolom-non-null | FE+BE | |
| TC-GS-ACTLOG-237 | D7 — Ingestion Out-of-Order Tetap Terurut by Timestamp | P2 | BE | — | — | Backend ingestion murni |
| TC-GS-ACTLOG-238 | D9 — 1 Save Ubah N Field Menghasilkan N Entri | P1 | E2E | TC-GS-ACTLOG-E2E-048-multi-field-edit-menghasilkan-n-entri-terpisah-timestamp-identik | FE+BE | |
| TC-GS-ACTLOG-239 | 8d-1 — Tidak Ada Plan Gating, Identik Lintas Semua Tier | P2 | E2E | TC-GS-ACTLOG-E2E-049-absennya-plan-gating-seluruh-fitur-identik-lintas-tier-plan | FE+BE | |
| TC-GS-ACTLOG-240 | Row Tidak Bisa Diklik (Purely Informational) | P2 | E2E | TC-GS-ACTLOG-E2E-001-screening-3-zona-dan-navigasi-tab | FE+BE | |
