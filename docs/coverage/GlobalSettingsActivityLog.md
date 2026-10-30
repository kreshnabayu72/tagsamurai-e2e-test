# Coverage E2E — Global Settings > Activity Log

Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md` (227 ID `TC-GS-ACTLOG-01`–`227`, seluruhnya aktif). Referensi: `global-settings/activity-log/PRD/activity-log.md`. Suite: `specs/GlobalSettings/ActivityLog/`. Prefix: `GS` + `ACTLOG` (`TC-GS-ACTLOG-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 227 TC aktif masuk spec, 0 TC hanya-BE (modul read-only; permintaan langsung TC-215 sampai TC-217 dijalankan sebagai spec defense-in-depth dan hanya mengasersi respons server). 62 spec (60 FE+BE, 2 mock). Setiap TC terpetakan ke tepat satu spec.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-ACTLOG-E2E-001-screening-layout-tab-default-breadcrumb-dan-tanpa-kontrol-tulis | Screening Layout, Tab Default, Breadcrumb, dan Tanpa Kontrol Tulis | FE+BE | 67 | 1, 2, 3, 221, 227 |
| TC-GS-ACTLOG-E2E-002-urutan-default-tie-break-dan-entri-tiba-tidak-berurutan | Urutan Default, Tie-break, dan Entri Tiba Tidak Berurutan | FE+BE | 18 | 10, 11, 214 |
| TC-GS-ACTLOG-E2E-003-tooltip-hover-dan-tampilan-sel-tabel | Tooltip Hover dan Tampilan Sel Tabel | FE+BE | 62 | 12, 13, 14, 15, 16 |
| TC-GS-ACTLOG-E2E-004-state-tabel-loading-empty-error-dan-try-again | State Tabel: Loading, Empty, Error, dan Try Again | mock | 41 | 4, 5, 8, 9 |
| TC-GS-ACTLOG-E2E-005-guided-tooltip-isi-dan-navigasi | Guided Tooltip: Isi dan Navigasi | FE+BE | 47 | 18, 21, 23 |
| TC-GS-ACTLOG-E2E-006-guided-tooltip-flag-seen-replay-dan-keluar-tanpa-selesai | Guided Tooltip: Flag Seen, Replay, dan Keluar Tanpa Selesai | FE+BE | 29 | 19, 20, 22 |
| TC-GS-ACTLOG-E2E-007-mobile-card-session-card-user-action-guided-step-2-dan-download | Mobile: Card Session, Card User Action, Guided Step 2, dan Download | FE+BE | 32 | 24, 25, 26, 140 |
| TC-GS-ACTLOG-E2E-008-ganti-bahasa-kolom-verbatim-dan-translatable | Ganti Bahasa: Kolom Verbatim dan Translatable | FE+BE | 17 | 27 |
| TC-GS-ACTLOG-E2E-009-role-matrix-visibilitas-dan-download-total-control-dan-read-only | Role Matrix: Visibilitas, Masking, dan Download Read Only | FE+BE | 23 | 28, 29, 37, 139 |
| TC-GS-ACTLOG-E2E-010-role-matrix-tanpa-akses-menu-dan-direct-url | Role Matrix: Tanpa Akses Menu dan Direct URL | FE+BE | 26 | 30, 31, 32, 33, 34 |
| TC-GS-ACTLOG-E2E-011-isolasi-entitas-client-principal-distributor-partner-dan-realtime-lintas-entitas | Isolasi Entitas: Client, Principal, Distributor, Partner, dan Realtime Lintas Entitas | FE+BE | 55 | 35, 36, 198 |
| TC-GS-ACTLOG-E2E-012-cakupan-isi-tab-session-dan-user-action | Cakupan Isi Tab Session dan User Action | FE+BE | 20 | 38, 39, 40 |
| TC-GS-ACTLOG-E2E-013-isi-kolom-tab-session-login-logout-status-nilai-kosong-ip-device | Isi Kolom Tab Session: Login, Logout, Status, Nilai Kosong, IP, Device | FE+BE | 37 | 41, 42, 43, 49, 50, 51, 52, 53 |
| TC-GS-ACTLOG-E2E-014-isi-kolom-tab-session-reset-password-change-password-session-force-logout | Isi Kolom Tab Session: Reset Password, Change Password, Session, Force-Logout | FE+BE | 31 | 44, 45, 46, 48, 226 |
| TC-GS-ACTLOG-E2E-015-absence-concurrent-limit-download-dan-aksi-sumber-gagal-tidak-tercatat | Absence: Concurrent Limit, Download, dan Aksi Sumber Gagal Tidak Tercatat | FE+BE | 36 | 47, 138, 212 |
| TC-GS-ACTLOG-E2E-016-snapshot-beku-setelah-data-diubah | Snapshot Beku Setelah Data Diubah | FE+BE | 22 | 54, 213 |
| TC-GS-ACTLOG-E2E-017-search-tab-session-kolom-teks-case-nama-trim-multi-kolom | Search Tab Session: Kolom Teks, Case, Nama, Trim, Multi-kolom | FE+BE | 32 | 56, 57, 58, 60, 63, 64 |
| TC-GS-ACTLOG-E2E-018-search-tab-session-status-date-visibilitas-kolom-siklus-kotak-search | Search Tab Session: Status, Date, Visibilitas Kolom, Siklus Kotak Search | FE+BE | 60 | 59, 61, 62, 65 |
| TC-GS-ACTLOG-E2E-019-filter-tab-session-struktur-or-and-search-dan-filter-berurutan | Filter Tab Session: Struktur, OR, AND, Search dan Filter Berurutan | FE+BE | 54 | 66, 67, 70, 71, 72, 73 |
| TC-GS-ACTLOG-E2E-020-filter-tab-session-activity-dan-status-sesuai-nilai-tampil | Filter Tab Session: Activity dan Status Sesuai Nilai Tampil | FE+BE | 16 | 68, 69 |
| TC-GS-ACTLOG-E2E-021-filter-tab-session-opsi-dari-data-pencarian-opsi-dan-chip-muncul | Filter Tab Session: Opsi dari Data, Pencarian Opsi, dan Chip Muncul | FE+BE | 22 | 78, 81, 82 |
| TC-GS-ACTLOG-E2E-022-filter-tab-session-hapus-chip-hapus-centang-dan-overflow-chip | Filter Tab Session: Hapus Chip, Hapus Centang, dan Overflow Chip | FE+BE | 25 | 83, 84, 85 |
| TC-GS-ACTLOG-E2E-023-sort-tab-session-semua-kolom | Sort Tab Session: Semua Kolom | FE+BE | 59 | 86, 87, 88, 89, 90, 91, 92 |
| TC-GS-ACTLOG-E2E-024-setup-column-tab-session-overlay-popup-sembunyikan-cancel-kolom-terakhir | Setup Column Tab Session: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir | FE+BE | 53 | 93, 94, 95, 96, 102, 103 |
| TC-GS-ACTLOG-E2E-025-setup-column-tab-session-urutan-dan-pin-satu-kolom | Setup Column Tab Session: Urutan dan Pin Satu Kolom | FE+BE | 25 | 97, 98 |
| TC-GS-ACTLOG-E2E-026-setup-column-tab-session-pin-tiga-kolom-kolom-ke-4-dan-reset | Setup Column Tab Session: Pin Tiga Kolom, Kolom Ke-4, dan Reset | FE+BE | 36 | 99, 100, 101 |
| TC-GS-ACTLOG-E2E-027-search-tab-user-action-kolom-teks-case-nama-trim-multi-kolom | Search Tab User Action: Kolom Teks, Case, Nama, Trim, Multi-kolom | FE+BE | 28 | 150, 151, 152, 153, 156, 157 |
| TC-GS-ACTLOG-E2E-028-search-tab-user-action-date-visibilitas-kolom-siklus-kotak-search | Search Tab User Action: Date, Visibilitas Kolom, Siklus Kotak Search | FE+BE | 47 | 154, 155, 158 |
| TC-GS-ACTLOG-E2E-029-filter-tab-user-action-struktur-or-and-search-dan-filter-berurutan | Filter Tab User Action: Struktur, OR, AND, Search dan Filter Berurutan | FE+BE | 46 | 159, 160, 161, 162, 163, 164 |
| TC-GS-ACTLOG-E2E-030-filter-tab-user-action-opsi-dari-data-object-action-modified-by-dan-pencarian-opsi | Filter Tab User Action: Opsi dari Data (Object, Action, Modified By) dan Pencarian Opsi | FE+BE | 28 | 165, 166, 167, 170 |
| TC-GS-ACTLOG-E2E-031-filter-tab-user-action-chip-hapus-chip-hapus-centang-dan-overflow | Filter Tab User Action: Chip, Hapus Chip, Hapus Centang, dan Overflow | FE+BE | 29 | 171, 172, 173, 174 |
| TC-GS-ACTLOG-E2E-032-sort-tab-user-action-semua-kolom | Sort Tab User Action: Semua Kolom | FE+BE | 9 | 175, 176, 177, 178, 179 |
| TC-GS-ACTLOG-E2E-033-setup-column-tab-user-action-overlay-popup-sembunyikan-cancel-kolom-terakhir | Setup Column Tab User Action: Overlay, Popup, Sembunyikan, Cancel, Kolom Terakhir | FE+BE | 49 | 180, 181, 182, 183, 189, 190 |
| TC-GS-ACTLOG-E2E-034-setup-column-tab-user-action-urutan-dan-pin-satu-kolom | Setup Column Tab User Action: Urutan dan Pin Satu Kolom | FE+BE | 22 | 184, 185 |
| TC-GS-ACTLOG-E2E-035-setup-column-tab-user-action-pin-tiga-kolom-kolom-ke-4-dan-reset | Setup Column Tab User Action: Pin Tiga Kolom, Kolom Ke-4, dan Reset | FE+BE | 32 | 186, 187, 188 |
| TC-GS-ACTLOG-E2E-036-pola-entri-user-action-create-edit-delete-dan-satu-save-banyak-field | Pola Entri User Action: Create, Edit, Delete, dan Satu Save Banyak Field | FE+BE | 29 | 141, 142, 143, 144 |
| TC-GS-ACTLOG-E2E-037-aksi-relasi-hardware-user-action-pair-assign-dan-add-access | Aksi Relasi Hardware di User Action: Pair/Unpair TAG, Assign/Unassign Handheld, Add/Remove Access, Audit TAG | FE+BE | 28 | 145, 148, 206 |
| TC-GS-ACTLOG-E2E-038-aksi-lain-user-action-permission-system-role-activate-dan-import | Aksi Lain di User Action: Edit Permission System Role, Activate/Deactivate, Import | FE+BE | 20 | 146, 147, 149 |
| TC-GS-ACTLOG-E2E-039-filter-date-batas-inklusif-rentang-terbalik-dan-sebagian-terisi | Filter Date Kedua Tab: Batas Inklusif, Rentang Terbalik, Sebagian Terisi | FE+BE | 27 | 74, 76, 77 |
| TC-GS-ACTLOG-E2E-040-format-tanggal-dan-zona-waktu-mengikuti-general-settings | Format Tanggal dan Zona Waktu Mengikuti General Settings | FE+BE | 40 | 75, 191, 192, 193, 194 |
| TC-GS-ACTLOG-E2E-041-kombinasi-search-filter-sort-dan-page-size-kedua-tab | Kombinasi Search, Filter, Sort, dan Page Size Kedua Tab | FE+BE | 54 | 104, 105, 106, 107 |
| TC-GS-ACTLOG-E2E-042-no-result-state-dan-kontrol-filter-panel-kedua-tab | No-result State dan Kontrol Filter Panel Kedua Tab | FE+BE | 51 | 6, 7, 108, 109, 110 |
| TC-GS-ACTLOG-E2E-043-kontrol-umum-filter-panel-visibilitas-kolom-keyboard-opsi-dan-header | Kontrol Umum Filter Panel: Visibilitas Kolom, Keyboard, Opsi Tanpa None, Header Kolom | FE+BE | 60 | 111, 112, 115, 116 |
| TC-GS-ACTLOG-E2E-044-opsi-filter-indikator-pemuatan-dan-sumber-kosong | Opsi Filter: Indikator Pemuatan dan Sumber Kosong | mock | 20 | 113, 114 |
| TC-GS-ACTLOG-E2E-045-independensi-dan-retensi-state-antar-tab-refresh-dan-klik-ulang-menu | Independensi dan Retensi State Antar Tab, Refresh, dan Klik Ulang Menu | FE+BE | 66 | 17, 117, 121, 126 |
| TC-GS-ACTLOG-E2E-046-pagination-page-size-navigasi-dan-reset-halaman-kedua-tab | Pagination Kedua Tab | FE+BE | 43 | 118, 119, 120 |
| TC-GS-ACTLOG-E2E-047-download-nama-berkas-format-nilai-kolom-dan-isi-sel | Download: Nama Berkas, Format Nilai, Kolom, dan Isi Sel | FE+BE | 52 | 125, 129, 130, 131, 133, 134 |
| TC-GS-ACTLOG-E2E-048-download-cakupan-baris-search-filter-kolom-tersembunyi-entitas-sort-dan-hasil-kosong | Download: Cakupan Baris, Search, Filter, Kolom Tersembunyi, Entitas, Sort, dan Hasil Kosong | FE+BE | 75 | 122, 123, 124, 127, 128, 135 |
| TC-GS-ACTLOG-E2E-049-download-gagal-toast-error-dengan-nama-berkas | Download Gagal: Toast Error dengan Nama Berkas | FE+BE | 10 | 132 |
| TC-GS-ACTLOG-E2E-050-download-di-atas-dan-tepat-pada-threshold-5000-baris | Download di Atas dan Tepat pada Threshold 5.000 Baris | FE+BE | 31 | 136, 137 |
| TC-GS-ACTLOG-E2E-051-realtime-baris-baru-saringan-aktif-dan-opsi-filter-bertambah | Realtime: Baris Baru, Saringan Aktif, dan Opsi Filter Bertambah | FE+BE | 34 | 79, 168, 195, 196, 197 |
| TC-GS-ACTLOG-E2E-052-sumber-user-action-user-role-permission-general-settings | Sumber User Action: User, Role dan Permission, General Settings | FE+BE | 31 | 199, 200, 201 |
| TC-GS-ACTLOG-E2E-053-sumber-user-action-brand-measurement-file-manager-permanently-delete | Sumber User Action: Brand, Measurement, File Manager, Permanently Delete | FE+BE | 37 | 202, 203, 204, 210 |
| TC-GS-ACTLOG-E2E-054-sumber-user-action-hardware-dan-tag-registry | Sumber User Action: Hardware (BLE Gateway) | FE+BE | 9 | 205 |
| TC-GS-ACTLOG-E2E-055-sumber-user-action-position-division-non-login-user | Sumber User Action: Position, Division, Non-Login User | FE+BE | 27 | 207, 208, 209 |
| TC-GS-ACTLOG-E2E-056-aksi-sistem-file-manager-modified-by-system | Aksi Sistem File Manager: Modified By System | FE+BE | 10 | 211 |
| TC-GS-ACTLOG-E2E-057-defense-in-depth-request-langsung-ke-endpoint-log | Defense-in-Depth: Request Langsung ke Endpoint Log | FE+BE | 13 | 215, 216, 217 |
| TC-GS-ACTLOG-E2E-058-defense-in-depth-payload-script-markup-dan-karakter-khusus-pencarian | Defense-in-Depth: Payload Script, Markup, dan Karakter Khusus Pencarian | FE+BE | 31 | 218, 219, 220 |
| TC-GS-ACTLOG-E2E-059-state-tenant-client-suspended-atau-expired | State Tenant: Client Suspended atau Expired | FE+BE | 27 | 222, 223 |
| TC-GS-ACTLOG-E2E-060-perilaku-identik-di-tiap-tier-plan | Perilaku Identik di Tiap Tier Plan | FE+BE | 22 | 224 |
| TC-GS-ACTLOG-E2E-061-log-lama-tanpa-batas-waktu-untuk-client-principal-distributor-partner | Log Lama Tanpa Batas Waktu untuk Client, Principal, Distributor, Partner | FE+BE | 11 | 225 |
| TC-GS-ACTLOG-E2E-062-filter-aktif-dan-snapshot-setelah-sumber-dihapus | Filter Aktif dan Snapshot Setelah Sumber Dihapus | FE+BE | 22 | 55, 80, 169 |

## Pembagian TC lintas spec

- Tidak ada TC yang terbelah: satu TC satu spec.
- **TC-GS-ACTLOG-47, 138, 212** (asersi tidak adanya baris atau entri) berada di spec `015` (kelas g) dengan anchor positif dan baseline per TC; pemicu 5xx TC-212 memakai pengecualian P-5.
- **TC-GS-ACTLOG-80, 169, 55** (data sumber dihapus) berada di spec `062`, yang berjalan paling akhir.
- **TC-GS-ACTLOG-198** (event entitas lain tidak muncul secara realtime) berada di spec `011` bersama isolasi entitas (kelas c, dua tenant); realtime satu tenant di spec `051`.
- **TC-GS-ACTLOG-6, 7** (no-result) berada di spec `042` bersama TC-108 yang memulihkan dari no-result.
- **TC-GS-ACTLOG-206** (Audit TAG, butuh simulasi hardware) berada di spec `037` bersama Pair/Unpair TAG dan Assign/Unassign Handheld; spec `054` hanya memuat TC-205.

## Kebutuhan lingkungan (tim FE)

- Env var password yang sudah ada di `.env.example` dan dipakai suite: `GS_CREATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_DISTRIBUTOR_TC_PASSWORD`, `GS_PLANENT_TC_PASSWORD`, `GS_PLANGROWTH_TC_PASSWORD`, `GS_PLANPRO_TC_PASSWORD`, `GS_PLANSTARTER_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_RO_PASSWORD`, `GS_TC2_PASSWORD`, `GS_TC_PASSWORD`, `GS_UPDATE_PASSWORD`, `LP_PASSWORD_WRONG`.
- Env var password baru yang belum terdaftar di `spectra.config.ts` dan `.env.example` (nilai dan akun ditetapkan tim FE): `ACTLOG_PASSWORD`, `ACTLOG_PASSWORD_NEW`, `GS_ACSEEALL_PASSWORD`, `GS_CLIENTALFA_TC_PASSWORD`, `GS_CLIENTBETA_TC_PASSWORD`, `GS_CLIENTVOL_TC_PASSWORD`, `GS_FULLCRUDBRAND_PASSWORD`, `GS_HENDRA_PASSWORD`, `GS_LIMITLOG_TC_PASSWORD`, `GS_NOCONCURRENT_TC_PASSWORD`, `GS_PARTNER_TC_PASSWORD`, `GS_SYSTEMROLE_PASSWORD`, `GS_WULANSARI_PASSWORD`, `GS_WULAN_PASSWORD`.
- Fixture data baru: `fixtures/` untuk modul Activity Log belum ada; kunci yang dirujuk spec ditandai di `## Prerequisites` tiap spec.
- Kemampuan teknis: seed BE untuk baris log (IP null, `status` internal, kedatangan tak berurutan, cap waktu tertentu, 5.001 baris, log tiga tahun lalu, auto-purge), intercept jaringan (500, tahan respons), dua sesi browser paralel, membaca berkas unduhan (CSV/XLSX), ubah plan dan status Client, ubah Date Format dan Time Zone General Settings, geser jam server, simulasi hardware (spec 037, 054), viewport mobile, klien HTTP untuk request langsung (spec 057). Mekanisme tiap seed ditulis tanpa endpoint di `## Prerequisites` spec yang memakainya.
- Log bersifat append-only dan dipakai bersama antar spec dan run; asersi eksklusivitas dibatasi ke baris subjek bersuffix. Asersi himpunan global (mis. opsi filter lengkap) butuh entitas log terisolasi.

## Temuan yang masih terbuka

Temuan TC sumber (ambigu, kontradiktif, precondition kurang) ditulis per spec di butir "Temuan untuk QA" pada `## Notes` spec yang bersangkutan dan tidak diulang di sini. Temuan lintas spec:

- Perilaku `[Apply]` Filter Panel (apakah panel menutup) dan state Search saat user meninggalkan lalu kembali ke Activity Log belum ditetapkan PRD; spec mengikuti TC dan mencatatnya di Notes (pemilik: PRD).
- TC-94, 102, 181, 189 masih menulis `[Cancel]` pada Setup Column, sedangkan modal Setup Column tidak punya `[Cancel]` (`prd-conventions.md` §24.1); spec 024 dan 033 mengikuti §24.1 (pemilik: TC).
- TC-48 (spec 014): Expected menyatakan baris `Logged out by admin` tampil, sedangkan Coverage Ledger TC dan NC-10 menyatakan nilai itu tidak pernah muncul di Global Settings; spec mengikuti Expected TC.
- Pemetaan Client Alfa dan Client Beta di TC ke Client A/B di `.env.example` belum terkonfirmasi (spec 011). Entitas log-terbatas, Admin Hendra/Wulan/Wulan Sari, dan akun Partner, See-All, System Role, Full CRUD Brand adalah fixture baru yang disediakan tim FE.
- Singkatan Modified By aktor Total Control Client A ditulis `Sari D` (turunan format `John D`) di spec yang memakai aktor itu; perlu konfirmasi.
- TC-51, 136, 137, 211, 214, 225 bertanda Manual Only; tetap ditulis sebagai spec dengan kebutuhan teknis di Prerequisites (bagian 2 konvensi).
- TC-222 berjudul "suspended atau expired" tetapi Precondition dan langkahnya hanya Suspended (spec 059); kondisi Expired tidak diuji.
- Hook suite Guided Tooltip menyetel flag hanya untuk akun aktor suite; akun lain (Read Only, Principal, entitas log-terbatas, dan seterusnya) memerlukan flag yang disetel tim FE/BE.
- Spec melewati batas ±35 langkah dengan satu kelas harness dan alasan di Notes: 048 (75), 001 (67), 045 (66), 003 (62), 018 (60), 043 (60), 023 (59), 011 (55), 019 (54), 041 (54), 024 (53), 047 (52), 042 (51), 033 (49), 005 (47), 028 (47), 029 (46), 046 (43), 004 (41), 040 (40), 013 (37), 053 (37), 015 (36), 026 (36). Kolom Langkah memakai hitungan nominal; langkah yang diulang per baris tabel ditulis sekali, dan hitungan ekspansi tiap spec ada di Notes.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-ACTLOG-01 | TC-GS-ACTLOG-E2E-001 | FE+BE |
| TC-GS-ACTLOG-02 | TC-GS-ACTLOG-E2E-001 | FE+BE |
| TC-GS-ACTLOG-03 | TC-GS-ACTLOG-E2E-001 | FE+BE |
| TC-GS-ACTLOG-04 | TC-GS-ACTLOG-E2E-004 | mock |
| TC-GS-ACTLOG-05 | TC-GS-ACTLOG-E2E-004 | mock |
| TC-GS-ACTLOG-06 | TC-GS-ACTLOG-E2E-042 | FE+BE |
| TC-GS-ACTLOG-07 | TC-GS-ACTLOG-E2E-042 | FE+BE |
| TC-GS-ACTLOG-08 | TC-GS-ACTLOG-E2E-004 | mock |
| TC-GS-ACTLOG-09 | TC-GS-ACTLOG-E2E-004 | mock |
| TC-GS-ACTLOG-10 | TC-GS-ACTLOG-E2E-002 | FE+BE |
| TC-GS-ACTLOG-11 | TC-GS-ACTLOG-E2E-002 | FE+BE |
| TC-GS-ACTLOG-12 | TC-GS-ACTLOG-E2E-003 | FE+BE |
| TC-GS-ACTLOG-13 | TC-GS-ACTLOG-E2E-003 | FE+BE |
| TC-GS-ACTLOG-14 | TC-GS-ACTLOG-E2E-003 | FE+BE |
| TC-GS-ACTLOG-15 | TC-GS-ACTLOG-E2E-003 | FE+BE |
| TC-GS-ACTLOG-16 | TC-GS-ACTLOG-E2E-003 | FE+BE |
| TC-GS-ACTLOG-17 | TC-GS-ACTLOG-E2E-045 | FE+BE |
| TC-GS-ACTLOG-18 | TC-GS-ACTLOG-E2E-005 | FE+BE |
| TC-GS-ACTLOG-19 | TC-GS-ACTLOG-E2E-006 | FE+BE |
| TC-GS-ACTLOG-20 | TC-GS-ACTLOG-E2E-006 | FE+BE |
| TC-GS-ACTLOG-21 | TC-GS-ACTLOG-E2E-005 | FE+BE |
| TC-GS-ACTLOG-22 | TC-GS-ACTLOG-E2E-006 | FE+BE |
| TC-GS-ACTLOG-23 | TC-GS-ACTLOG-E2E-005 | FE+BE |
| TC-GS-ACTLOG-24 | TC-GS-ACTLOG-E2E-007 | FE+BE |
| TC-GS-ACTLOG-25 | TC-GS-ACTLOG-E2E-007 | FE+BE |
| TC-GS-ACTLOG-26 | TC-GS-ACTLOG-E2E-007 | FE+BE |
| TC-GS-ACTLOG-27 | TC-GS-ACTLOG-E2E-008 | FE+BE |
| TC-GS-ACTLOG-28 | TC-GS-ACTLOG-E2E-009 | FE+BE |
| TC-GS-ACTLOG-29 | TC-GS-ACTLOG-E2E-009 | FE+BE |
| TC-GS-ACTLOG-30 | TC-GS-ACTLOG-E2E-010 | FE+BE |
| TC-GS-ACTLOG-31 | TC-GS-ACTLOG-E2E-010 | FE+BE |
| TC-GS-ACTLOG-32 | TC-GS-ACTLOG-E2E-010 | FE+BE |
| TC-GS-ACTLOG-33 | TC-GS-ACTLOG-E2E-010 | FE+BE |
| TC-GS-ACTLOG-34 | TC-GS-ACTLOG-E2E-010 | FE+BE |
| TC-GS-ACTLOG-35 | TC-GS-ACTLOG-E2E-011 | FE+BE |
| TC-GS-ACTLOG-36 | TC-GS-ACTLOG-E2E-011 | FE+BE |
| TC-GS-ACTLOG-37 | TC-GS-ACTLOG-E2E-009 | FE+BE |
| TC-GS-ACTLOG-38 | TC-GS-ACTLOG-E2E-012 | FE+BE |
| TC-GS-ACTLOG-39 | TC-GS-ACTLOG-E2E-012 | FE+BE |
| TC-GS-ACTLOG-40 | TC-GS-ACTLOG-E2E-012 | FE+BE |
| TC-GS-ACTLOG-41 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-42 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-43 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-44 | TC-GS-ACTLOG-E2E-014 | FE+BE |
| TC-GS-ACTLOG-45 | TC-GS-ACTLOG-E2E-014 | FE+BE |
| TC-GS-ACTLOG-46 | TC-GS-ACTLOG-E2E-014 | FE+BE |
| TC-GS-ACTLOG-47 | TC-GS-ACTLOG-E2E-015 | FE+BE |
| TC-GS-ACTLOG-48 | TC-GS-ACTLOG-E2E-014 | FE+BE |
| TC-GS-ACTLOG-49 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-50 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-51 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-52 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-53 | TC-GS-ACTLOG-E2E-013 | FE+BE |
| TC-GS-ACTLOG-54 | TC-GS-ACTLOG-E2E-016 | FE+BE |
| TC-GS-ACTLOG-55 | TC-GS-ACTLOG-E2E-062 | FE+BE |
| TC-GS-ACTLOG-56 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-57 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-58 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-59 | TC-GS-ACTLOG-E2E-018 | FE+BE |
| TC-GS-ACTLOG-60 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-61 | TC-GS-ACTLOG-E2E-018 | FE+BE |
| TC-GS-ACTLOG-62 | TC-GS-ACTLOG-E2E-018 | FE+BE |
| TC-GS-ACTLOG-63 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-64 | TC-GS-ACTLOG-E2E-017 | FE+BE |
| TC-GS-ACTLOG-65 | TC-GS-ACTLOG-E2E-018 | FE+BE |
| TC-GS-ACTLOG-66 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-67 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-68 | TC-GS-ACTLOG-E2E-020 | FE+BE |
| TC-GS-ACTLOG-69 | TC-GS-ACTLOG-E2E-020 | FE+BE |
| TC-GS-ACTLOG-70 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-71 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-72 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-73 | TC-GS-ACTLOG-E2E-019 | FE+BE |
| TC-GS-ACTLOG-74 | TC-GS-ACTLOG-E2E-039 | FE+BE |
| TC-GS-ACTLOG-75 | TC-GS-ACTLOG-E2E-040 | FE+BE |
| TC-GS-ACTLOG-76 | TC-GS-ACTLOG-E2E-039 | FE+BE |
| TC-GS-ACTLOG-77 | TC-GS-ACTLOG-E2E-039 | FE+BE |
| TC-GS-ACTLOG-78 | TC-GS-ACTLOG-E2E-021 | FE+BE |
| TC-GS-ACTLOG-79 | TC-GS-ACTLOG-E2E-051 | FE+BE |
| TC-GS-ACTLOG-80 | TC-GS-ACTLOG-E2E-062 | FE+BE |
| TC-GS-ACTLOG-81 | TC-GS-ACTLOG-E2E-021 | FE+BE |
| TC-GS-ACTLOG-82 | TC-GS-ACTLOG-E2E-021 | FE+BE |
| TC-GS-ACTLOG-83 | TC-GS-ACTLOG-E2E-022 | FE+BE |
| TC-GS-ACTLOG-84 | TC-GS-ACTLOG-E2E-022 | FE+BE |
| TC-GS-ACTLOG-85 | TC-GS-ACTLOG-E2E-022 | FE+BE |
| TC-GS-ACTLOG-86 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-87 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-88 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-89 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-90 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-91 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-92 | TC-GS-ACTLOG-E2E-023 | FE+BE |
| TC-GS-ACTLOG-93 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-94 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-95 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-96 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-97 | TC-GS-ACTLOG-E2E-025 | FE+BE |
| TC-GS-ACTLOG-98 | TC-GS-ACTLOG-E2E-025 | FE+BE |
| TC-GS-ACTLOG-99 | TC-GS-ACTLOG-E2E-026 | FE+BE |
| TC-GS-ACTLOG-100 | TC-GS-ACTLOG-E2E-026 | FE+BE |
| TC-GS-ACTLOG-101 | TC-GS-ACTLOG-E2E-026 | FE+BE |
| TC-GS-ACTLOG-102 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-103 | TC-GS-ACTLOG-E2E-024 | FE+BE |
| TC-GS-ACTLOG-104 | TC-GS-ACTLOG-E2E-041 | FE+BE |
| TC-GS-ACTLOG-105 | TC-GS-ACTLOG-E2E-041 | FE+BE |
| TC-GS-ACTLOG-106 | TC-GS-ACTLOG-E2E-041 | FE+BE |
| TC-GS-ACTLOG-107 | TC-GS-ACTLOG-E2E-041 | FE+BE |
| TC-GS-ACTLOG-108 | TC-GS-ACTLOG-E2E-042 | FE+BE |
| TC-GS-ACTLOG-109 | TC-GS-ACTLOG-E2E-042 | FE+BE |
| TC-GS-ACTLOG-110 | TC-GS-ACTLOG-E2E-042 | FE+BE |
| TC-GS-ACTLOG-111 | TC-GS-ACTLOG-E2E-043 | FE+BE |
| TC-GS-ACTLOG-112 | TC-GS-ACTLOG-E2E-043 | FE+BE |
| TC-GS-ACTLOG-113 | TC-GS-ACTLOG-E2E-044 | mock |
| TC-GS-ACTLOG-114 | TC-GS-ACTLOG-E2E-044 | mock |
| TC-GS-ACTLOG-115 | TC-GS-ACTLOG-E2E-043 | FE+BE |
| TC-GS-ACTLOG-116 | TC-GS-ACTLOG-E2E-043 | FE+BE |
| TC-GS-ACTLOG-117 | TC-GS-ACTLOG-E2E-045 | FE+BE |
| TC-GS-ACTLOG-118 | TC-GS-ACTLOG-E2E-046 | FE+BE |
| TC-GS-ACTLOG-119 | TC-GS-ACTLOG-E2E-046 | FE+BE |
| TC-GS-ACTLOG-120 | TC-GS-ACTLOG-E2E-046 | FE+BE |
| TC-GS-ACTLOG-121 | TC-GS-ACTLOG-E2E-045 | FE+BE |
| TC-GS-ACTLOG-122 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-123 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-124 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-125 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-126 | TC-GS-ACTLOG-E2E-045 | FE+BE |
| TC-GS-ACTLOG-127 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-128 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-129 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-130 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-131 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-132 | TC-GS-ACTLOG-E2E-049 | FE+BE |
| TC-GS-ACTLOG-133 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-134 | TC-GS-ACTLOG-E2E-047 | FE+BE |
| TC-GS-ACTLOG-135 | TC-GS-ACTLOG-E2E-048 | FE+BE |
| TC-GS-ACTLOG-136 | TC-GS-ACTLOG-E2E-050 | FE+BE |
| TC-GS-ACTLOG-137 | TC-GS-ACTLOG-E2E-050 | FE+BE |
| TC-GS-ACTLOG-138 | TC-GS-ACTLOG-E2E-015 | FE+BE |
| TC-GS-ACTLOG-139 | TC-GS-ACTLOG-E2E-009 | FE+BE |
| TC-GS-ACTLOG-140 | TC-GS-ACTLOG-E2E-007 | FE+BE |
| TC-GS-ACTLOG-141 | TC-GS-ACTLOG-E2E-036 | FE+BE |
| TC-GS-ACTLOG-142 | TC-GS-ACTLOG-E2E-036 | FE+BE |
| TC-GS-ACTLOG-143 | TC-GS-ACTLOG-E2E-036 | FE+BE |
| TC-GS-ACTLOG-144 | TC-GS-ACTLOG-E2E-036 | FE+BE |
| TC-GS-ACTLOG-145 | TC-GS-ACTLOG-E2E-037 | FE+BE |
| TC-GS-ACTLOG-146 | TC-GS-ACTLOG-E2E-038 | FE+BE |
| TC-GS-ACTLOG-147 | TC-GS-ACTLOG-E2E-038 | FE+BE |
| TC-GS-ACTLOG-148 | TC-GS-ACTLOG-E2E-037 | FE+BE |
| TC-GS-ACTLOG-149 | TC-GS-ACTLOG-E2E-038 | FE+BE |
| TC-GS-ACTLOG-150 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-151 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-152 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-153 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-154 | TC-GS-ACTLOG-E2E-028 | FE+BE |
| TC-GS-ACTLOG-155 | TC-GS-ACTLOG-E2E-028 | FE+BE |
| TC-GS-ACTLOG-156 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-157 | TC-GS-ACTLOG-E2E-027 | FE+BE |
| TC-GS-ACTLOG-158 | TC-GS-ACTLOG-E2E-028 | FE+BE |
| TC-GS-ACTLOG-159 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-160 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-161 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-162 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-163 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-164 | TC-GS-ACTLOG-E2E-029 | FE+BE |
| TC-GS-ACTLOG-165 | TC-GS-ACTLOG-E2E-030 | FE+BE |
| TC-GS-ACTLOG-166 | TC-GS-ACTLOG-E2E-030 | FE+BE |
| TC-GS-ACTLOG-167 | TC-GS-ACTLOG-E2E-030 | FE+BE |
| TC-GS-ACTLOG-168 | TC-GS-ACTLOG-E2E-051 | FE+BE |
| TC-GS-ACTLOG-169 | TC-GS-ACTLOG-E2E-062 | FE+BE |
| TC-GS-ACTLOG-170 | TC-GS-ACTLOG-E2E-030 | FE+BE |
| TC-GS-ACTLOG-171 | TC-GS-ACTLOG-E2E-031 | FE+BE |
| TC-GS-ACTLOG-172 | TC-GS-ACTLOG-E2E-031 | FE+BE |
| TC-GS-ACTLOG-173 | TC-GS-ACTLOG-E2E-031 | FE+BE |
| TC-GS-ACTLOG-174 | TC-GS-ACTLOG-E2E-031 | FE+BE |
| TC-GS-ACTLOG-175 | TC-GS-ACTLOG-E2E-032 | FE+BE |
| TC-GS-ACTLOG-176 | TC-GS-ACTLOG-E2E-032 | FE+BE |
| TC-GS-ACTLOG-177 | TC-GS-ACTLOG-E2E-032 | FE+BE |
| TC-GS-ACTLOG-178 | TC-GS-ACTLOG-E2E-032 | FE+BE |
| TC-GS-ACTLOG-179 | TC-GS-ACTLOG-E2E-032 | FE+BE |
| TC-GS-ACTLOG-180 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-181 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-182 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-183 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-184 | TC-GS-ACTLOG-E2E-034 | FE+BE |
| TC-GS-ACTLOG-185 | TC-GS-ACTLOG-E2E-034 | FE+BE |
| TC-GS-ACTLOG-186 | TC-GS-ACTLOG-E2E-035 | FE+BE |
| TC-GS-ACTLOG-187 | TC-GS-ACTLOG-E2E-035 | FE+BE |
| TC-GS-ACTLOG-188 | TC-GS-ACTLOG-E2E-035 | FE+BE |
| TC-GS-ACTLOG-189 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-190 | TC-GS-ACTLOG-E2E-033 | FE+BE |
| TC-GS-ACTLOG-191 | TC-GS-ACTLOG-E2E-040 | FE+BE |
| TC-GS-ACTLOG-192 | TC-GS-ACTLOG-E2E-040 | FE+BE |
| TC-GS-ACTLOG-193 | TC-GS-ACTLOG-E2E-040 | FE+BE |
| TC-GS-ACTLOG-194 | TC-GS-ACTLOG-E2E-040 | FE+BE |
| TC-GS-ACTLOG-195 | TC-GS-ACTLOG-E2E-051 | FE+BE |
| TC-GS-ACTLOG-196 | TC-GS-ACTLOG-E2E-051 | FE+BE |
| TC-GS-ACTLOG-197 | TC-GS-ACTLOG-E2E-051 | FE+BE |
| TC-GS-ACTLOG-198 | TC-GS-ACTLOG-E2E-011 | FE+BE |
| TC-GS-ACTLOG-199 | TC-GS-ACTLOG-E2E-052 | FE+BE |
| TC-GS-ACTLOG-200 | TC-GS-ACTLOG-E2E-052 | FE+BE |
| TC-GS-ACTLOG-201 | TC-GS-ACTLOG-E2E-052 | FE+BE |
| TC-GS-ACTLOG-202 | TC-GS-ACTLOG-E2E-053 | FE+BE |
| TC-GS-ACTLOG-203 | TC-GS-ACTLOG-E2E-053 | FE+BE |
| TC-GS-ACTLOG-204 | TC-GS-ACTLOG-E2E-053 | FE+BE |
| TC-GS-ACTLOG-205 | TC-GS-ACTLOG-E2E-054 | FE+BE |
| TC-GS-ACTLOG-206 | TC-GS-ACTLOG-E2E-037 | FE+BE |
| TC-GS-ACTLOG-207 | TC-GS-ACTLOG-E2E-055 | FE+BE |
| TC-GS-ACTLOG-208 | TC-GS-ACTLOG-E2E-055 | FE+BE |
| TC-GS-ACTLOG-209 | TC-GS-ACTLOG-E2E-055 | FE+BE |
| TC-GS-ACTLOG-210 | TC-GS-ACTLOG-E2E-053 | FE+BE |
| TC-GS-ACTLOG-211 | TC-GS-ACTLOG-E2E-056 | FE+BE |
| TC-GS-ACTLOG-212 | TC-GS-ACTLOG-E2E-015 | FE+BE |
| TC-GS-ACTLOG-213 | TC-GS-ACTLOG-E2E-016 | FE+BE |
| TC-GS-ACTLOG-214 | TC-GS-ACTLOG-E2E-002 | FE+BE |
| TC-GS-ACTLOG-215 | TC-GS-ACTLOG-E2E-057 | FE+BE |
| TC-GS-ACTLOG-216 | TC-GS-ACTLOG-E2E-057 | FE+BE |
| TC-GS-ACTLOG-217 | TC-GS-ACTLOG-E2E-057 | FE+BE |
| TC-GS-ACTLOG-218 | TC-GS-ACTLOG-E2E-058 | FE+BE |
| TC-GS-ACTLOG-219 | TC-GS-ACTLOG-E2E-058 | FE+BE |
| TC-GS-ACTLOG-220 | TC-GS-ACTLOG-E2E-058 | FE+BE |
| TC-GS-ACTLOG-221 | TC-GS-ACTLOG-E2E-001 | FE+BE |
| TC-GS-ACTLOG-222 | TC-GS-ACTLOG-E2E-059 | FE+BE |
| TC-GS-ACTLOG-223 | TC-GS-ACTLOG-E2E-059 | FE+BE |
| TC-GS-ACTLOG-224 | TC-GS-ACTLOG-E2E-060 | FE+BE |
| TC-GS-ACTLOG-225 | TC-GS-ACTLOG-E2E-061 | FE+BE |
| TC-GS-ACTLOG-226 | TC-GS-ACTLOG-E2E-014 | FE+BE |
| TC-GS-ACTLOG-227 | TC-GS-ACTLOG-E2E-001 | FE+BE |
