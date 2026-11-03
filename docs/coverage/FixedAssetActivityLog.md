# Coverage E2E — Fixed Asset > Reports & Logs > Activity Log

Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md` (289 ID `TC-FA-FAAL-1`–`289`). Suite: `specs/FixedAsset/ActivityLog/`. Prefix: `FA` + `FAAL` (`TC-FA-FAAL-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 289 TC masuk spec, 0 TC hanya-BE (modul read-only; tidak ada `tc-activity-log-backend.md`). 92 spec, seluruhnya FE+BE (kegagalan dipicu intercept di atas backend nyata; tidak ada spec mock). Setiap TC terpetakan ke tepat satu spec. Nomor 001–062 dari rencana; 063–076 adalah nomor cadangan penulis untuk memecah spec yang melewati ~35 langkah; 077–080, 085–089, dan 095–099 adalah pecahan tambahan setelah lint pertama (13 temuan C6, disetujui pengguna). Nomor 081–084 dan 090–094 sengaja tidak dipakai (tidak direnumber). Judul spec asal yang dipecah dan spec pecahannya disesuaikan dengan isi TC masing-masing; tabel di bawah dibangkitkan dari frontmatter spec.

## Fix pass setelah e2e-audit

Setelah e2e-audit, TC sumber diedit (anchor positif, total baseline `Z0`, dan Filter Date Jendela Seed pada TC read-only); hash TC baru `fff68e21f2a4b178`. Spec terdampak diselaraskan ulang (lihat progress `Fix pass (audit)`); tabel di bawah dibangkitkan ulang dari frontmatter dan jumlah langkah terkini. Setiap TC tetap terpetakan ke tepat satu spec (289 TC, 90 spec).

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-FAAL-E2E-001-screening-halaman-dan-tooltip-toolbar | Screening Halaman Activity Log dan Tooltip Toolbar Kedua Tab | FE+BE | 29 | 1, 2 |
| TC-FA-FAAL-E2E-002-screening-tab-user-action-loading-dan-halaman-tanpa-kontrol-tulis | Screening Tab User Action, Urutan Default, dan Loading | FE+BE | 29 | 4, 6, 9 |
| TC-FA-FAAL-E2E-003-empty-state-kedua-tab | Empty State Kedua Tab pada Client Baru | FE+BE | 6 | 7, 8 |
| TC-FA-FAAL-E2E-004-error-load-dan-download-gagal | Kegagalan Server: Error Load Kedua Tab dan Download Gagal Tab Session | FE+BE | 33 | 10, 11, 171 |
| TC-FA-FAAL-E2E-005-sel-tab-session | Sel Tab Session: User, Device/Browser, Employee ID, Position, IP, Division, Note, Activity, Status | FE+BE | 34 | 12-19 |
| TC-FA-FAAL-E2E-006-sel-tab-user-action-bagian-a | Sel Tab User Action: Modified By, Name, dan Old/New Value Kosong (bagian A) | FE+BE | 18 | 20-24 |
| TC-FA-FAAL-E2E-007-sel-tab-user-action-bagian-b | Sel Tab User Action: Old/New Value, Field, dan Nilai Panjang (bagian B) | FE+BE | 17 | 25-29 |
| TC-FA-FAAL-E2E-008-android-card-list-infinite-scroll-dan-susunan-card | Android: Card List, Infinite Scroll, dan Susunan Card Tab Session dan User Action | FE+BE | 30 | 30-34 |
| TC-FA-FAAL-E2E-009-role-matrix-visibilitas-menu-activity-log | Role Matrix: Visibilitas Menu Activity Log (Total Control, Read Only, Default User) | FE+BE | 30 | 37-39 |
| TC-FA-FAAL-E2E-010-role-matrix-menu-tersembunyi-group-manager-dan-global-role | Role Matrix: Menu Activity Log Tersembunyi (Group Manager dan Global Role) | FE+BE | 6 | 40, 41 |
| TC-FA-FAAL-E2E-011-role-matrix-direct-url-per-role | Role Matrix: Buka URL Activity Log Langsung per Role | FE+BE | 17 | 44-47 |
| TC-FA-FAAL-E2E-012-role-matrix-data-yang-terlihat-per-role | Role Matrix: Seluruh Baris Kedua Tab untuk Total Control dan Read Only | FE+BE | 21 | 48-51 |
| TC-FA-FAAL-E2E-013-read-only-search-filter-download | Read Only: Search, Filter, dan Download | FE+BE | 25 | 52-54 |
| TC-FA-FAAL-E2E-014-perubahan-tier-akses-saat-halaman-terbuka | Perubahan Tier Akses: Dicabut dan Dipromosikan saat Halaman Terbuka | FE+BE | 24 | 55, 56 |
| TC-FA-FAAL-E2E-015-defense-in-depth-akses-ditolak-group-manager | Defense-in-Depth: Direct API, Download, dan SSE Group Manager Ditolak | FE+BE | 23 | 256-258 |
| TC-FA-FAAL-E2E-016-guided-tooltip-isi-replay-dan-keluar | Guided Tooltip: Isi, Kunjungan Pertama, Replay, dan Keluar | FE+BE | 36 | 197-199, 201 |
| TC-FA-FAAL-E2E-017-guided-tooltip-navigasi-dan-keyboard | Guided Tooltip: Navigasi Back/Next/Done/Skip dan Keyboard | FE+BE | 25 | 200, 202 |
| TC-FA-FAAL-E2E-018-format-tanggal-mengikuti-general-settings | Format Tanggal dan Jam Mengikuti General Settings Staf | FE+BE | 22 | 204-207 |
| TC-FA-FAAL-E2E-019-search-tab-session-reveal-dan-kolom-employee-position-division-user | Search Tab Session: Reveal Input dan Kolom Employee ID, Position, Division, serta User | FE+BE | 35 | 57, 59, 60 |
| TC-FA-FAAL-E2E-020-search-tab-session-kolom-activity-note-ip-status | Search Tab Session: Activity, Note, IP Address, Device/Browser, dan Status | FE+BE | 33 | 61-64 |
| TC-FA-FAAL-E2E-021-search-tab-session-date-tanpa-hasil-tersembunyi-dan-trim | Search Tab Session: Date, Tanpa Hasil, dan Kolom Tersembunyi | FE+BE | 26 | 65-67 |
| TC-FA-FAAL-E2E-022-volume-5001-baris-search-dan-download | Volume 5.000 dan 5.001 Baris: Download Ambang 5.000 serta Browsing dan Search Tanpa Loading Screen | FE+BE | 24 | 69, 182 |
| TC-FA-FAAL-E2E-023-filter-date-tab-session | Filter Date Tab Session: Screening Panel, Satu Hari, dan Rentang | FE+BE | 23 | 70-72 |
| TC-FA-FAAL-E2E-024-filter-date-hanya-mulai-atau-akhir-kedua-tab | Filter Date Hanya Tanggal Mulai atau Hanya Tanggal Akhir di Kedua Tab | FE+BE | 27 | 73, 74 |
| TC-FA-FAAL-E2E-025-filter-date-batas-hari-zona-waktu-staf | Filter Date pada Batas Hari, Zona Waktu Staf, dan Tie-Breaker Sort | FE+BE | 35 | 76, 106, 128, 208 |
| TC-FA-FAAL-E2E-026-filter-position-division-note-dan-opsi-dropdown | Filter Tab Session: Position, Division, Note, dan Opsi Dropdown | FE+BE | 25 | 77, 78 |
| TC-FA-FAAL-E2E-027-filter-user-tab-session-dan-search-internal | Filter User Tab Session: Opsi per Nama Lengkap, Dua Pengguna Bernama Sama, dan Search Internal | FE+BE | 22 | 81-83 |
| TC-FA-FAAL-E2E-028-filter-chip-or-and-tab-session | Filter Tab Session: Logika OR, Chip, dan Hapus Chip | FE+BE | 29 | 84-87 |
| TC-FA-FAAL-E2E-029-interaksi-search-filter-sort-tab-session | Interaksi Search dan Filter Tab Session: Irisan Dua Urutan, Pemulihan Empty State, dan Filter Tanpa Hasil | FE+BE | 28 | 90, 91, 96, 97 |
| TC-FA-FAAL-E2E-030-filter-panel-draft-badge-dan-keyboard-kedua-tab | Filter Panel Kedua Tab: Draft, Badge, Independen dari Kolom, dan Keyboard | FE+BE | 57 | 98-100, 286 |
| TC-FA-FAAL-E2E-031-sort-tab-session | Sort Tab Session: Date, User, IP Address, Activity, dan Status | FE+BE | 33 | 101, 102, 104, 105 |
| TC-FA-FAAL-E2E-032-setup-column-tab-session-sembunyi-tampil | Setup Column Tab Session: Screening Overlay dan Popup, Sembunyi/Tampil Kolom, dan Kolom Terakhir | FE+BE | 34 | 107-109, 115 |
| TC-FA-FAAL-E2E-033-setup-column-tab-session-urutan-dan-pin | Setup Column Tab Session: Drag Urutan dan Pin/Unpin Kolom | FE+BE | 23 | 110, 111 |
| TC-FA-FAAL-E2E-034-setup-column-tab-session-batas-pin-reset-dan-tutup | Setup Column Tab Session: Batas Pin, Overlay Langsung, Reset to Default, Tutup tanpa Save, dan Independensi Antar Tab | FE+BE | 46 | 112-114, 116, 117 |
| TC-FA-FAAL-E2E-035-search-tab-user-action-reveal-dan-kolom | Search Tab User Action: Reveal Input dan Pencarian Kolom Action, Object, Field, Name, Old Value, New Value, serta Modified By | FE+BE | 18 | 118-122 |
| TC-FA-FAAL-E2E-036-search-tab-user-action-date-tanpa-hasil-dan-tersembunyi | Search Tab User Action: Kolom Date Tidak Dicari, Tanpa Hasil, dan Kolom Field Tersembunyi | FE+BE | 16 | 123-125 |
| TC-FA-FAAL-E2E-037-filter-tab-user-action-date-dan-opsi | Filter Tab User Action: Screening Panel, Date, serta Action, Object, dan Field | FE+BE | 23 | 126, 127, 129 |
| TC-FA-FAAL-E2E-038-filter-tab-user-action-logika-dan-interaksi | Filter Tab User Action: Logika AND dan OR serta Interaksi Search dan Filter | FE+BE | 23 | 134-137 |
| TC-FA-FAAL-E2E-039-filter-tab-user-action-pemulihan-dan-tanpa-hasil | Filter Tab User Action: Kosongkan Search, Pemulihan Empty State, dan Tanpa Hasil | FE+BE | 21 | 140-142 |
| TC-FA-FAAL-E2E-040-sort-tab-user-action | Sort Tab User Action: Date, Teks, Modified By, Old/New Value | FE+BE | 34 | 143-146 |
| TC-FA-FAAL-E2E-041-setup-column-tab-user-action-screening-dan-kolom-terakhir | Setup Column Tab User Action: Screening Overlay dan Popup, serta Kolom Visible Terakhir | FE+BE | 24 | 147, 148, 154 |
| TC-FA-FAAL-E2E-042-setup-column-tab-user-action-urutan-reset-tutup | Setup Column Tab User Action: Reset to Default dan Tutup tanpa Save | FE+BE | 26 | 152, 153 |
| TC-FA-FAAL-E2E-043-paginasi-rows-per-page-dan-showing-kedua-tab | Paginasi: Rows per Page Default dan Navigasi Halaman di Kedua Tab | FE+BE | 31 | 155, 156 |
| TC-FA-FAAL-E2E-044-persistensi-search-filter-sort-antar-tab | Persistensi Search dan Filter Saat Pindah Tab | FE+BE | 27 | 190, 191 |
| TC-FA-FAAL-E2E-045-persistensi-refresh-f5-dan-reset-klik-ulang-menu | Persistensi Refresh F5 pada Search, Filter, Sort, Rows per Page, dan Tab Aktif | FE+BE | 19 | 194, 195 |
| TC-FA-FAAL-E2E-046-download-overlay-nama-berkas-dan-ekstensi | Download: Overlay Format serta Nama Berkas CSV/XLSX di Kedua Tab | FE+BE | 22 | 161-165, 170 |
| TC-FA-FAAL-E2E-047-download-cakupan-baris-kolom-dan-filter | Download: Seluruh Baris, Kolom Tersembunyi, Satu Kolom Tersisa, Hasil Kosong, serta Search dan Filter Aktif | FE+BE | 58 | 166-169, 184, 189 |
| TC-FA-FAAL-E2E-048-isi-berkas-download-tab-session | Isi Berkas Download Tab Session: Sel Date, User, Teks, Status, dan Device/Browser | FE+BE | 14 | 173-177 |
| TC-FA-FAAL-E2E-049-isi-berkas-download-tab-user-action | Isi Berkas Download Tab User Action: Sel, Format CSV dan XLSX, Urutan Baris dan Kolom | FE+BE | 30 | 178-181, 185-188 |
| TC-FA-FAAL-E2E-050-sse-tab-user-action-baris-baru-filter-dan-sort | SSE Tab User Action: Baris Baru, Filter Tidak Cocok, Halaman Lain, dan Sort | FE+BE | 32 | 264, 266-268 |
| TC-FA-FAAL-E2E-051-sse-tab-user-action-halaman-penuh-dan-reconnect | SSE Tab User Action: Halaman Penuh, Putus-Sambung Koneksi, dan Muat Ulang | FE+BE | 35 | 269-271 |
| TC-FA-FAAL-E2E-052-sse-tab-user-action-search-filter-role-dan-isolasi | SSE Tab User Action: Search/Filter Aktif, Default User, Empty State, Opsi Object Baru, dan Isolasi Client | FE+BE | 54 | 131, 263, 278, 280, 281, 288 |
| TC-FA-FAAL-E2E-053-sse-tab-session-baris-baru-dan-opsi-position | SSE Tab Session: Sesi Baru, Filter Aktif, dan Opsi Position Real-Time | FE+BE | 32 | 79, 265, 282, 283 |
| TC-FA-FAAL-E2E-054-state-tenant-client-suspended-subscription-expired-dan-retensi-plan-starter | State Tenant: Client Suspended, Subscription Expired, dan Retensi Baris pada Plan Starter | FE+BE | 32 | 273-275 |
| TC-FA-FAAL-E2E-055-pencatatan-tab-session-start-end-logout | Pencatatan Tab Session: Session started dan Session ended (Logout, Password, Keluar Produk) | FE+BE | 22 | 209, 210, 212, 213 |
| TC-FA-FAAL-E2E-056-pencatatan-tab-session-cabut-akses-concurrent-force-logout | Pencatatan Tab Session: Cabut Akses, Nonaktif, Concurrent Limit, dan Force Logout | FE+BE | 29 | 214-217 |
| TC-FA-FAAL-E2E-057-absence-log-tab-session-dan-user-action | Absence Log: Membaca Tidak Menulis Baris dan Edit Tanpa Perubahan | FE+BE | 27 | 203, 251 |
| TC-FA-FAAL-E2E-058-pencatatan-user-action-role-dan-akses | Pencatatan User Action: Assign dan Remove Role serta Access Level | FE+BE | 50 | 221-230 |
| TC-FA-FAAL-E2E-059-pencatatan-user-action-user-activate-resend-modified-by | Pencatatan User Action: Activate, Deactivate, Resend, Home Group, dan Modified By | FE+BE | 39 | 231-234, 253, 279 |
| TC-FA-FAAL-E2E-060-pencatatan-user-action-groups | Pencatatan User Action: Edit dan Delete Group serta Snapshot Name | FE+BE | 37 | 235, 236, 252, 254, 285 |
| TC-FA-FAAL-E2E-061-pencatatan-user-action-master-data | Pencatatan User Action: Category, Asset Name, Custom Asset ID, Label, dan Custom Field | FE+BE | 34 | 237-241, 243, 250 |
| TC-FA-FAAL-E2E-062-pencatatan-user-action-import-license-transaksi | Pencatatan User Action: Import Group, License, Disposal, Damaged, dan Finish Audit | FE+BE | 30 | 242, 244-249 |
| TC-FA-FAAL-E2E-063-screening-tab-session-dan-urutan-default | Screening Tab Session dan Urutan Default Tab Session | FE+BE | 19 | 3, 5 |
| TC-FA-FAAL-E2E-064-android-toolbar-dan-guided-tooltip | Android: Toolbar dan Guided Tooltip Mengikuti Tombol ⋯ | FE+BE | 13 | 36 |
| TC-FA-FAAL-E2E-065-role-matrix-menu-tersembunyi-group-role-dan-transaction-role | Role Matrix: Menu Activity Log Tersembunyi (Group Role dan Transaction Role) | FE+BE | 6 | 42, 43 |
| TC-FA-FAAL-E2E-066-defense-in-depth-xss-markup-dan-tulis-log-ditolak | Defense-in-Depth: Payload Skrip dan SQL, Markup, dan Tulis Log Ditolak | FE+BE | 27 | 259, 260, 262 |
| TC-FA-FAAL-E2E-067-search-siklus-enter-clear-collapse-kedua-tab | Search: Siklus Submit Enter, Clear, dan Collapse di Tab Session dan Tab User Action | FE+BE | 39 | 58 |
| TC-FA-FAAL-E2E-068-date-picker-filter-tanggal-akhir-tidak-sebelum-tanggal-mulai | Date Picker Filter: Tanggal Akhir Tidak Dapat Dipilih Sebelum Tanggal Mulai di Kedua Tab | FE+BE | 13 | 75 |
| TC-FA-FAAL-E2E-069-interaksi-search-filter-sort-kombinasi-irisan-tab-session | Kombinasi Filter, Search, Sort, dan Ukuran Halaman Tab Session: Pelepasan Kontrol dan Pindah Kolom Sort | FE+BE | 27 | 92-95 |
| TC-FA-FAAL-E2E-070-sort-tab-session-kolom-teks | Sort Tab Session: Kolom Teks Employee ID, Position, Division, Note, dan Device/Browser | FE+BE | 42 | 103 |
| TC-FA-FAAL-E2E-071-sembunyi-dan-tampil-kolom-tab-user-action | Setup Column Tab User Action: Sembunyikan dan Tampilkan Kolom | FE+BE | 17 | 149 |
| TC-FA-FAAL-E2E-072-pin-dan-unpin-kolom-tab-user-action | Setup Column Tab User Action: Pin dan Unpin Kolom | FE+BE | 16 | 151 |
| TC-FA-FAAL-E2E-073-perilaku-identik-di-semua-plan-tanpa-gating | State Tenant: Perilaku Activity Log Identik di Plan Starter, Growth, Professional, dan Enterprise | FE+BE | 11 | 276 |
| TC-FA-FAAL-E2E-074-subscription-archive-purge-deleted-akses-mengikuti-auth | State Tenant: Subscription Archive, Purge, dan Deleted, Akses Activity Log Mengikuti Auth | FE+BE | 15 | 289 |
| TC-FA-FAAL-E2E-075-pencatatan-tab-session-snapshot-perubahan-profil-user | Pencatatan Tab Session: Baris Lama Tidak Berubah Setelah Profil User Diubah | FE+BE | 26 | 220, 284 |
| TC-FA-FAAL-E2E-076-absence-log-tab-session-kedaluwarsa-force-logout-event-platform-dan-aksi-gagal | Absence Log: Session ended Kedaluwarsa, Force Logout, Event Platform, dan Aksi Edit Gagal | FE+BE | 35 | 211, 218, 219, 255 |
| TC-FA-FAAL-E2E-077-halaman-tanpa-kontrol-ubah-tab-user-action | Halaman Activity Log Tanpa Kontrol Ubah, Hapus, atau Buat (Tab User Action) | FE+BE | 12 | 261 |
| TC-FA-FAAL-E2E-078-download-gagal-tab-user-action | Kegagalan Server: Download Gagal Tab User Action | FE+BE | 10 | 172 |
| TC-FA-FAAL-E2E-079-android-card-tidak-dapat-diketuk | Android: Card Tab Session dan User Action Tidak Dapat Diketuk | FE+BE | 12 | 35 |
| TC-FA-FAAL-E2E-080-search-trim-spasi-kedua-tab | Search Men-trim Spasi Awal dan Akhir Query di Kedua Tab | FE+BE | 16 | 68 |
| TC-FA-FAAL-E2E-081-role-matrix-default-user-search-filter-dan-download | Role Matrix: Default User Melihat Seluruh Baris Kedua Tab dan Menjalankan Search, Filter, dan Download | FE+BE | 22 | 277 |
| TC-FA-FAAL-E2E-082-tier-dicabut-saat-sse-terbuka | Perubahan Tier Akses: Tier Dicabut saat SSE Terbuka Menutup Koneksi dan Menghentikan Event | FE+BE | 11 | 272 |
| TC-FA-FAAL-E2E-085-download-5001-baris-loading-screen-dan-berkas-terunduh | Volume 5.001 Baris: Download Menampilkan Loading Screen lalu Berkas Langsung Terunduh | FE+BE | 18 | 183 |
| TC-FA-FAAL-E2E-086-filter-tab-session-state-dropdown-position-loading-kosong-tanpa-hasil | Filter Tab Session: State Loading, Sumber Kosong, dan Tanpa Hasil pada Dropdown Position | FE+BE | 14 | 80 |
| TC-FA-FAAL-E2E-087-filter-tab-session-overflow-chip-dan-logika-and | Filter Tab Session: Overflow Chip +N more dan Logika AND | FE+BE | 13 | 88, 89 |
| TC-FA-FAAL-E2E-088-filter-tab-user-action-opsi-dropdown-dan-modified-by | Filter Tab User Action: Opsi Dropdown dan Filter Modified By | FE+BE | 23 | 130, 132, 133 |
| TC-FA-FAAL-E2E-089-filter-tab-user-action-kombinasi-filter-search-sort-dan-clear-field | Filter Tab User Action: Kombinasi Filter, Search, Sort, Ukuran Halaman, dan Clear Field | FE+BE | 18 | 138, 139 |
| TC-FA-FAAL-E2E-095-setup-column-tab-user-action-urutan-drag-per-kolom | Setup Column Tab User Action: Urutan Kolom Lewat Drag per Kolom | FE+BE | 13 | 150 |
| TC-FA-FAAL-E2E-096-paginasi-nomor-halaman-tidak-valid-rows-per-page-dan-sort-kedua-tab | Paginasi: Nomor Halaman Tidak Valid, Ganti Rows per Page, dan Ganti Sort di Kedua Tab | FE+BE | 33 | 157-159 |
| TC-FA-FAAL-E2E-097-paginasi-search-dan-apply-filter-mereset-ke-halaman-1 | Paginasi: Search dan Apply Filter Mereset ke Halaman 1 | FE+BE | 9 | 160 |
| TC-FA-FAAL-E2E-098-persistensi-sort-halaman-dan-rows-per-page-antar-tab | Persistensi Sort, Halaman, dan Rows per Page Saat Pindah Tab | FE+BE | 25 | 192, 193 |
| TC-FA-FAAL-E2E-099-persistensi-reset-klik-ulang-menu-dan-halaman-setelah-f5 | Persistensi Reset Klik Ulang Menu dan Halaman Aktif Setelah F5 | FE+BE | 21 | 196, 287 |

## TC hanya-BE yang dilewati

Tidak ada. Modul read-only dan tidak ada backend TC; permintaan langsung (defense-in-depth) dijalankan sebagai spec FE+BE yang mengasersi respons server.

## Pembagian TC lintas spec

- Tidak ada TC yang terbelah: satu TC satu spec (dicek skrip dari frontmatter `sourceTc`: 289 TC, tanpa yatim atau ganda).
- Spec 063–076 memecah spec rencana yang melewati ~35 langkah menurut kelas harness atau tab; spec 077–080, 085–089, 095–099 memecah lagi spec yang melanggar aturan C6 pada lint pertama. Pecahan membawa TC yang sama dengan yang direncanakan di spec asalnya, tanpa merenumber; lihat kolom TC sumber.
- TC pencatatan log yang asersinya "tidak tercatat" (absence) berada di spec 057 dan 076 dengan anchor positif dan baseline per TC.

## Kebutuhan lingkungan (tim FE)

- Env var password sudah terdaftar di `.env.example` dan `spectra.config.ts`: `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_DU_PASSWORD`.
- Env var password baru yang diusulkan spec dan belum terdaftar (nilai dan akun ditetapkan tim FE): `FA_GM_PASSWORD`, `FA_JOHNDOE_PASSWORD`, `FA_MIKETAN_PASSWORD`, `FA_RO_REVOKE_PASSWORD`, `FA_RO_STAFB_PASSWORD`, `FA_ROLEHOLDER_PASSWORD`, `FA_SITINURBAYA_PASSWORD`, `FA_TCBATAS_PASSWORD`, `FA_TCNEWGUIDE_PASSWORD`. TC sumber tidak menyebut nama env var; nama diusulkan dari butir "Env var" di `suite.md`.
- Fixture data: `fixtures/activity-log.json` belum ada; kunci yang dirujuk spec ditandai di `## Prerequisites` tiap spec dan ditetapkan tim FE.
- Kemampuan teknis: seed dan pemulihan log lewat API (log append-only), intercept jaringan (5xx, tahan respons), dua sesi browser paralel, SSE real-time, membaca berkas unduhan (CSV/XLSX), volume 5.001 baris, ubah Date Format dan Time Zone General Settings, ubah plan/status Client, geser jam server, flag Guided Tooltip per akun.
- Log bersifat append-only dan dipakai bersama antar spec dan run; urutan default (baris Pre-setup di halaman 1) hanya terjamin bila log dipulihkan ke Pre-setup sebelum tiap spec.

## Temuan yang masih terbuka

Temuan TC sumber (ambigu, kontradiktif, precondition kurang) ditulis per spec di butir "Temuan untuk QA" pada `## Notes` spec yang bersangkutan dan tidak diulang di sini. Ringkasan lintas spec:

- Nama env var password akun Pre-setup tertentu tidak disebut TC; nama diusulkan spec dan sudah didaftarkan di `.env.example` dan `spectra.config.ts`; nilai dan akun ditetapkan tim FE. Env var password client kedua TC-FA-FAAL-250 tidak ada di spec 061 dan ditetapkan tim FE. Pemilik: tim FE.
- Spec 018 dan 076 memakai pengecualian P-5 butir b (TC ringan satu topik); diterima pemilik.
- Perilaku Filter Panel setelah `[Apply]` (menutup sendiri atau tetap terbuka) tidak dinyatakan di TC dan tidak ditegaskan PRD §4.5; spec tidak mengasumsikan salah satunya dan hanya menutup panel secara eksplisit bila TC menyebutnya. Pemilik: TC/PRD.
- Jendela Seed (Tab Session 14/07/26 sampai 16/07/26, Tab User Action 18/06/26 sampai 18/06/26, Asia/Jakarta) diasumsikan spec sebagai Filter Date yang diterapkan pada TC read-only yang mengasersi total atau posisi baris seed; baris dari aksi lain bertanggal berjalan dan berada di luar jendela, dan TC penulis baris memakai baseline `Z0` yang dicatat sebelum aksi. Asumsi bergantung pada tanggal seed Pre-setup #11/#12 yang tetap dan belum diverifikasi di lingkungan. Pemilik: tim FE/BE.
- Pemulihan log ke Pre-setup sebelum tiap TC adalah kemampuan tim FE/BE yang belum ada (prasyarat eksternal); tanpa itu urutan dan jumlah baris tidak terjamin. Pemilik: tim FE/BE.
- Spec 012 dan 014 dipecah dengan spec 081 dan 082; spec 067 (39 langkah) bersumber satu TC (TC-FA-FAAL-58) sehingga tidak bisa dipecah di batas TC.

- Spec melewati batas ~35 langkah dengan alasan di `## Notes`: 047 (58), 030 (57), 052 (54), 058 (50), 034 (46), 070 (42), 059 (39), 067 (39), 060 (37), 016 (36); 058, 059 dan 060 berisi TC berurutan dengan ketergantungan yang dicatat di Notes tiap spec.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-FAAL-1 | TC-FA-FAAL-E2E-001 | FE+BE |
| TC-FA-FAAL-2 | TC-FA-FAAL-E2E-001 | FE+BE |
| TC-FA-FAAL-3 | TC-FA-FAAL-E2E-063 | FE+BE |
| TC-FA-FAAL-4 | TC-FA-FAAL-E2E-002 | FE+BE |
| TC-FA-FAAL-5 | TC-FA-FAAL-E2E-063 | FE+BE |
| TC-FA-FAAL-6 | TC-FA-FAAL-E2E-002 | FE+BE |
| TC-FA-FAAL-7 | TC-FA-FAAL-E2E-003 | FE+BE |
| TC-FA-FAAL-8 | TC-FA-FAAL-E2E-003 | FE+BE |
| TC-FA-FAAL-9 | TC-FA-FAAL-E2E-002 | FE+BE |
| TC-FA-FAAL-10 | TC-FA-FAAL-E2E-004 | FE+BE |
| TC-FA-FAAL-11 | TC-FA-FAAL-E2E-004 | FE+BE |
| TC-FA-FAAL-12 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-13 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-14 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-15 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-16 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-17 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-18 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-19 | TC-FA-FAAL-E2E-005 | FE+BE |
| TC-FA-FAAL-20 | TC-FA-FAAL-E2E-006 | FE+BE |
| TC-FA-FAAL-21 | TC-FA-FAAL-E2E-006 | FE+BE |
| TC-FA-FAAL-22 | TC-FA-FAAL-E2E-006 | FE+BE |
| TC-FA-FAAL-23 | TC-FA-FAAL-E2E-006 | FE+BE |
| TC-FA-FAAL-24 | TC-FA-FAAL-E2E-006 | FE+BE |
| TC-FA-FAAL-25 | TC-FA-FAAL-E2E-007 | FE+BE |
| TC-FA-FAAL-26 | TC-FA-FAAL-E2E-007 | FE+BE |
| TC-FA-FAAL-27 | TC-FA-FAAL-E2E-007 | FE+BE |
| TC-FA-FAAL-28 | TC-FA-FAAL-E2E-007 | FE+BE |
| TC-FA-FAAL-29 | TC-FA-FAAL-E2E-007 | FE+BE |
| TC-FA-FAAL-30 | TC-FA-FAAL-E2E-008 | FE+BE |
| TC-FA-FAAL-31 | TC-FA-FAAL-E2E-008 | FE+BE |
| TC-FA-FAAL-32 | TC-FA-FAAL-E2E-008 | FE+BE |
| TC-FA-FAAL-33 | TC-FA-FAAL-E2E-008 | FE+BE |
| TC-FA-FAAL-34 | TC-FA-FAAL-E2E-008 | FE+BE |
| TC-FA-FAAL-35 | TC-FA-FAAL-E2E-079 | FE+BE |
| TC-FA-FAAL-36 | TC-FA-FAAL-E2E-064 | FE+BE |
| TC-FA-FAAL-37 | TC-FA-FAAL-E2E-009 | FE+BE |
| TC-FA-FAAL-38 | TC-FA-FAAL-E2E-009 | FE+BE |
| TC-FA-FAAL-39 | TC-FA-FAAL-E2E-009 | FE+BE |
| TC-FA-FAAL-40 | TC-FA-FAAL-E2E-010 | FE+BE |
| TC-FA-FAAL-41 | TC-FA-FAAL-E2E-010 | FE+BE |
| TC-FA-FAAL-42 | TC-FA-FAAL-E2E-065 | FE+BE |
| TC-FA-FAAL-43 | TC-FA-FAAL-E2E-065 | FE+BE |
| TC-FA-FAAL-44 | TC-FA-FAAL-E2E-011 | FE+BE |
| TC-FA-FAAL-45 | TC-FA-FAAL-E2E-011 | FE+BE |
| TC-FA-FAAL-46 | TC-FA-FAAL-E2E-011 | FE+BE |
| TC-FA-FAAL-47 | TC-FA-FAAL-E2E-011 | FE+BE |
| TC-FA-FAAL-48 | TC-FA-FAAL-E2E-012 | FE+BE |
| TC-FA-FAAL-49 | TC-FA-FAAL-E2E-012 | FE+BE |
| TC-FA-FAAL-50 | TC-FA-FAAL-E2E-012 | FE+BE |
| TC-FA-FAAL-51 | TC-FA-FAAL-E2E-012 | FE+BE |
| TC-FA-FAAL-52 | TC-FA-FAAL-E2E-013 | FE+BE |
| TC-FA-FAAL-53 | TC-FA-FAAL-E2E-013 | FE+BE |
| TC-FA-FAAL-54 | TC-FA-FAAL-E2E-013 | FE+BE |
| TC-FA-FAAL-55 | TC-FA-FAAL-E2E-014 | FE+BE |
| TC-FA-FAAL-56 | TC-FA-FAAL-E2E-014 | FE+BE |
| TC-FA-FAAL-57 | TC-FA-FAAL-E2E-019 | FE+BE |
| TC-FA-FAAL-58 | TC-FA-FAAL-E2E-067 | FE+BE |
| TC-FA-FAAL-59 | TC-FA-FAAL-E2E-019 | FE+BE |
| TC-FA-FAAL-60 | TC-FA-FAAL-E2E-019 | FE+BE |
| TC-FA-FAAL-61 | TC-FA-FAAL-E2E-020 | FE+BE |
| TC-FA-FAAL-62 | TC-FA-FAAL-E2E-020 | FE+BE |
| TC-FA-FAAL-63 | TC-FA-FAAL-E2E-020 | FE+BE |
| TC-FA-FAAL-64 | TC-FA-FAAL-E2E-020 | FE+BE |
| TC-FA-FAAL-65 | TC-FA-FAAL-E2E-021 | FE+BE |
| TC-FA-FAAL-66 | TC-FA-FAAL-E2E-021 | FE+BE |
| TC-FA-FAAL-67 | TC-FA-FAAL-E2E-021 | FE+BE |
| TC-FA-FAAL-68 | TC-FA-FAAL-E2E-080 | FE+BE |
| TC-FA-FAAL-69 | TC-FA-FAAL-E2E-022 | FE+BE |
| TC-FA-FAAL-70 | TC-FA-FAAL-E2E-023 | FE+BE |
| TC-FA-FAAL-71 | TC-FA-FAAL-E2E-023 | FE+BE |
| TC-FA-FAAL-72 | TC-FA-FAAL-E2E-023 | FE+BE |
| TC-FA-FAAL-73 | TC-FA-FAAL-E2E-024 | FE+BE |
| TC-FA-FAAL-74 | TC-FA-FAAL-E2E-024 | FE+BE |
| TC-FA-FAAL-75 | TC-FA-FAAL-E2E-068 | FE+BE |
| TC-FA-FAAL-76 | TC-FA-FAAL-E2E-025 | FE+BE |
| TC-FA-FAAL-77 | TC-FA-FAAL-E2E-026 | FE+BE |
| TC-FA-FAAL-78 | TC-FA-FAAL-E2E-026 | FE+BE |
| TC-FA-FAAL-79 | TC-FA-FAAL-E2E-053 | FE+BE |
| TC-FA-FAAL-80 | TC-FA-FAAL-E2E-086 | FE+BE |
| TC-FA-FAAL-81 | TC-FA-FAAL-E2E-027 | FE+BE |
| TC-FA-FAAL-82 | TC-FA-FAAL-E2E-027 | FE+BE |
| TC-FA-FAAL-83 | TC-FA-FAAL-E2E-027 | FE+BE |
| TC-FA-FAAL-84 | TC-FA-FAAL-E2E-028 | FE+BE |
| TC-FA-FAAL-85 | TC-FA-FAAL-E2E-028 | FE+BE |
| TC-FA-FAAL-86 | TC-FA-FAAL-E2E-028 | FE+BE |
| TC-FA-FAAL-87 | TC-FA-FAAL-E2E-028 | FE+BE |
| TC-FA-FAAL-88 | TC-FA-FAAL-E2E-087 | FE+BE |
| TC-FA-FAAL-89 | TC-FA-FAAL-E2E-087 | FE+BE |
| TC-FA-FAAL-90 | TC-FA-FAAL-E2E-029 | FE+BE |
| TC-FA-FAAL-91 | TC-FA-FAAL-E2E-029 | FE+BE |
| TC-FA-FAAL-92 | TC-FA-FAAL-E2E-069 | FE+BE |
| TC-FA-FAAL-93 | TC-FA-FAAL-E2E-069 | FE+BE |
| TC-FA-FAAL-94 | TC-FA-FAAL-E2E-069 | FE+BE |
| TC-FA-FAAL-95 | TC-FA-FAAL-E2E-069 | FE+BE |
| TC-FA-FAAL-96 | TC-FA-FAAL-E2E-029 | FE+BE |
| TC-FA-FAAL-97 | TC-FA-FAAL-E2E-029 | FE+BE |
| TC-FA-FAAL-98 | TC-FA-FAAL-E2E-030 | FE+BE |
| TC-FA-FAAL-99 | TC-FA-FAAL-E2E-030 | FE+BE |
| TC-FA-FAAL-100 | TC-FA-FAAL-E2E-030 | FE+BE |
| TC-FA-FAAL-101 | TC-FA-FAAL-E2E-031 | FE+BE |
| TC-FA-FAAL-102 | TC-FA-FAAL-E2E-031 | FE+BE |
| TC-FA-FAAL-103 | TC-FA-FAAL-E2E-070 | FE+BE |
| TC-FA-FAAL-104 | TC-FA-FAAL-E2E-031 | FE+BE |
| TC-FA-FAAL-105 | TC-FA-FAAL-E2E-031 | FE+BE |
| TC-FA-FAAL-106 | TC-FA-FAAL-E2E-025 | FE+BE |
| TC-FA-FAAL-107 | TC-FA-FAAL-E2E-032 | FE+BE |
| TC-FA-FAAL-108 | TC-FA-FAAL-E2E-032 | FE+BE |
| TC-FA-FAAL-109 | TC-FA-FAAL-E2E-032 | FE+BE |
| TC-FA-FAAL-110 | TC-FA-FAAL-E2E-033 | FE+BE |
| TC-FA-FAAL-111 | TC-FA-FAAL-E2E-033 | FE+BE |
| TC-FA-FAAL-112 | TC-FA-FAAL-E2E-034 | FE+BE |
| TC-FA-FAAL-113 | TC-FA-FAAL-E2E-034 | FE+BE |
| TC-FA-FAAL-114 | TC-FA-FAAL-E2E-034 | FE+BE |
| TC-FA-FAAL-115 | TC-FA-FAAL-E2E-032 | FE+BE |
| TC-FA-FAAL-116 | TC-FA-FAAL-E2E-034 | FE+BE |
| TC-FA-FAAL-117 | TC-FA-FAAL-E2E-034 | FE+BE |
| TC-FA-FAAL-118 | TC-FA-FAAL-E2E-035 | FE+BE |
| TC-FA-FAAL-119 | TC-FA-FAAL-E2E-035 | FE+BE |
| TC-FA-FAAL-120 | TC-FA-FAAL-E2E-035 | FE+BE |
| TC-FA-FAAL-121 | TC-FA-FAAL-E2E-035 | FE+BE |
| TC-FA-FAAL-122 | TC-FA-FAAL-E2E-035 | FE+BE |
| TC-FA-FAAL-123 | TC-FA-FAAL-E2E-036 | FE+BE |
| TC-FA-FAAL-124 | TC-FA-FAAL-E2E-036 | FE+BE |
| TC-FA-FAAL-125 | TC-FA-FAAL-E2E-036 | FE+BE |
| TC-FA-FAAL-126 | TC-FA-FAAL-E2E-037 | FE+BE |
| TC-FA-FAAL-127 | TC-FA-FAAL-E2E-037 | FE+BE |
| TC-FA-FAAL-128 | TC-FA-FAAL-E2E-025 | FE+BE |
| TC-FA-FAAL-129 | TC-FA-FAAL-E2E-037 | FE+BE |
| TC-FA-FAAL-130 | TC-FA-FAAL-E2E-088 | FE+BE |
| TC-FA-FAAL-131 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-132 | TC-FA-FAAL-E2E-088 | FE+BE |
| TC-FA-FAAL-133 | TC-FA-FAAL-E2E-088 | FE+BE |
| TC-FA-FAAL-134 | TC-FA-FAAL-E2E-038 | FE+BE |
| TC-FA-FAAL-135 | TC-FA-FAAL-E2E-038 | FE+BE |
| TC-FA-FAAL-136 | TC-FA-FAAL-E2E-038 | FE+BE |
| TC-FA-FAAL-137 | TC-FA-FAAL-E2E-038 | FE+BE |
| TC-FA-FAAL-138 | TC-FA-FAAL-E2E-089 | FE+BE |
| TC-FA-FAAL-139 | TC-FA-FAAL-E2E-089 | FE+BE |
| TC-FA-FAAL-140 | TC-FA-FAAL-E2E-039 | FE+BE |
| TC-FA-FAAL-141 | TC-FA-FAAL-E2E-039 | FE+BE |
| TC-FA-FAAL-142 | TC-FA-FAAL-E2E-039 | FE+BE |
| TC-FA-FAAL-143 | TC-FA-FAAL-E2E-040 | FE+BE |
| TC-FA-FAAL-144 | TC-FA-FAAL-E2E-040 | FE+BE |
| TC-FA-FAAL-145 | TC-FA-FAAL-E2E-040 | FE+BE |
| TC-FA-FAAL-146 | TC-FA-FAAL-E2E-040 | FE+BE |
| TC-FA-FAAL-147 | TC-FA-FAAL-E2E-041 | FE+BE |
| TC-FA-FAAL-148 | TC-FA-FAAL-E2E-041 | FE+BE |
| TC-FA-FAAL-149 | TC-FA-FAAL-E2E-071 | FE+BE |
| TC-FA-FAAL-150 | TC-FA-FAAL-E2E-095 | FE+BE |
| TC-FA-FAAL-151 | TC-FA-FAAL-E2E-072 | FE+BE |
| TC-FA-FAAL-152 | TC-FA-FAAL-E2E-042 | FE+BE |
| TC-FA-FAAL-153 | TC-FA-FAAL-E2E-042 | FE+BE |
| TC-FA-FAAL-154 | TC-FA-FAAL-E2E-041 | FE+BE |
| TC-FA-FAAL-155 | TC-FA-FAAL-E2E-043 | FE+BE |
| TC-FA-FAAL-156 | TC-FA-FAAL-E2E-043 | FE+BE |
| TC-FA-FAAL-157 | TC-FA-FAAL-E2E-096 | FE+BE |
| TC-FA-FAAL-158 | TC-FA-FAAL-E2E-096 | FE+BE |
| TC-FA-FAAL-159 | TC-FA-FAAL-E2E-096 | FE+BE |
| TC-FA-FAAL-160 | TC-FA-FAAL-E2E-097 | FE+BE |
| TC-FA-FAAL-161 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-162 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-163 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-164 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-165 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-166 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-167 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-168 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-169 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-170 | TC-FA-FAAL-E2E-046 | FE+BE |
| TC-FA-FAAL-171 | TC-FA-FAAL-E2E-004 | FE+BE |
| TC-FA-FAAL-172 | TC-FA-FAAL-E2E-078 | FE+BE |
| TC-FA-FAAL-173 | TC-FA-FAAL-E2E-048 | FE+BE |
| TC-FA-FAAL-174 | TC-FA-FAAL-E2E-048 | FE+BE |
| TC-FA-FAAL-175 | TC-FA-FAAL-E2E-048 | FE+BE |
| TC-FA-FAAL-176 | TC-FA-FAAL-E2E-048 | FE+BE |
| TC-FA-FAAL-177 | TC-FA-FAAL-E2E-048 | FE+BE |
| TC-FA-FAAL-178 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-179 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-180 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-181 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-182 | TC-FA-FAAL-E2E-022 | FE+BE |
| TC-FA-FAAL-183 | TC-FA-FAAL-E2E-085 | FE+BE |
| TC-FA-FAAL-184 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-185 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-186 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-187 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-188 | TC-FA-FAAL-E2E-049 | FE+BE |
| TC-FA-FAAL-189 | TC-FA-FAAL-E2E-047 | FE+BE |
| TC-FA-FAAL-190 | TC-FA-FAAL-E2E-044 | FE+BE |
| TC-FA-FAAL-191 | TC-FA-FAAL-E2E-044 | FE+BE |
| TC-FA-FAAL-192 | TC-FA-FAAL-E2E-098 | FE+BE |
| TC-FA-FAAL-193 | TC-FA-FAAL-E2E-098 | FE+BE |
| TC-FA-FAAL-194 | TC-FA-FAAL-E2E-045 | FE+BE |
| TC-FA-FAAL-195 | TC-FA-FAAL-E2E-045 | FE+BE |
| TC-FA-FAAL-196 | TC-FA-FAAL-E2E-099 | FE+BE |
| TC-FA-FAAL-197 | TC-FA-FAAL-E2E-016 | FE+BE |
| TC-FA-FAAL-198 | TC-FA-FAAL-E2E-016 | FE+BE |
| TC-FA-FAAL-199 | TC-FA-FAAL-E2E-016 | FE+BE |
| TC-FA-FAAL-200 | TC-FA-FAAL-E2E-017 | FE+BE |
| TC-FA-FAAL-201 | TC-FA-FAAL-E2E-016 | FE+BE |
| TC-FA-FAAL-202 | TC-FA-FAAL-E2E-017 | FE+BE |
| TC-FA-FAAL-203 | TC-FA-FAAL-E2E-057 | FE+BE |
| TC-FA-FAAL-204 | TC-FA-FAAL-E2E-018 | FE+BE |
| TC-FA-FAAL-205 | TC-FA-FAAL-E2E-018 | FE+BE |
| TC-FA-FAAL-206 | TC-FA-FAAL-E2E-018 | FE+BE |
| TC-FA-FAAL-207 | TC-FA-FAAL-E2E-018 | FE+BE |
| TC-FA-FAAL-208 | TC-FA-FAAL-E2E-025 | FE+BE |
| TC-FA-FAAL-209 | TC-FA-FAAL-E2E-055 | FE+BE |
| TC-FA-FAAL-210 | TC-FA-FAAL-E2E-055 | FE+BE |
| TC-FA-FAAL-211 | TC-FA-FAAL-E2E-076 | FE+BE |
| TC-FA-FAAL-212 | TC-FA-FAAL-E2E-055 | FE+BE |
| TC-FA-FAAL-213 | TC-FA-FAAL-E2E-055 | FE+BE |
| TC-FA-FAAL-214 | TC-FA-FAAL-E2E-056 | FE+BE |
| TC-FA-FAAL-215 | TC-FA-FAAL-E2E-056 | FE+BE |
| TC-FA-FAAL-216 | TC-FA-FAAL-E2E-056 | FE+BE |
| TC-FA-FAAL-217 | TC-FA-FAAL-E2E-056 | FE+BE |
| TC-FA-FAAL-218 | TC-FA-FAAL-E2E-076 | FE+BE |
| TC-FA-FAAL-219 | TC-FA-FAAL-E2E-076 | FE+BE |
| TC-FA-FAAL-220 | TC-FA-FAAL-E2E-075 | FE+BE |
| TC-FA-FAAL-221 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-222 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-223 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-224 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-225 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-226 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-227 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-228 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-229 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-230 | TC-FA-FAAL-E2E-058 | FE+BE |
| TC-FA-FAAL-231 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-232 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-233 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-234 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-235 | TC-FA-FAAL-E2E-060 | FE+BE |
| TC-FA-FAAL-236 | TC-FA-FAAL-E2E-060 | FE+BE |
| TC-FA-FAAL-237 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-238 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-239 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-240 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-241 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-242 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-243 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-244 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-245 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-246 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-247 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-248 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-249 | TC-FA-FAAL-E2E-062 | FE+BE |
| TC-FA-FAAL-250 | TC-FA-FAAL-E2E-061 | FE+BE |
| TC-FA-FAAL-251 | TC-FA-FAAL-E2E-057 | FE+BE |
| TC-FA-FAAL-252 | TC-FA-FAAL-E2E-060 | FE+BE |
| TC-FA-FAAL-253 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-254 | TC-FA-FAAL-E2E-060 | FE+BE |
| TC-FA-FAAL-255 | TC-FA-FAAL-E2E-076 | FE+BE |
| TC-FA-FAAL-256 | TC-FA-FAAL-E2E-015 | FE+BE |
| TC-FA-FAAL-257 | TC-FA-FAAL-E2E-015 | FE+BE |
| TC-FA-FAAL-258 | TC-FA-FAAL-E2E-015 | FE+BE |
| TC-FA-FAAL-259 | TC-FA-FAAL-E2E-066 | FE+BE |
| TC-FA-FAAL-260 | TC-FA-FAAL-E2E-066 | FE+BE |
| TC-FA-FAAL-261 | TC-FA-FAAL-E2E-077 | FE+BE |
| TC-FA-FAAL-262 | TC-FA-FAAL-E2E-066 | FE+BE |
| TC-FA-FAAL-263 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-264 | TC-FA-FAAL-E2E-050 | FE+BE |
| TC-FA-FAAL-265 | TC-FA-FAAL-E2E-053 | FE+BE |
| TC-FA-FAAL-266 | TC-FA-FAAL-E2E-050 | FE+BE |
| TC-FA-FAAL-267 | TC-FA-FAAL-E2E-050 | FE+BE |
| TC-FA-FAAL-268 | TC-FA-FAAL-E2E-050 | FE+BE |
| TC-FA-FAAL-269 | TC-FA-FAAL-E2E-051 | FE+BE |
| TC-FA-FAAL-270 | TC-FA-FAAL-E2E-051 | FE+BE |
| TC-FA-FAAL-271 | TC-FA-FAAL-E2E-051 | FE+BE |
| TC-FA-FAAL-272 | TC-FA-FAAL-E2E-082 | FE+BE |
| TC-FA-FAAL-273 | TC-FA-FAAL-E2E-054 | FE+BE |
| TC-FA-FAAL-274 | TC-FA-FAAL-E2E-054 | FE+BE |
| TC-FA-FAAL-275 | TC-FA-FAAL-E2E-054 | FE+BE |
| TC-FA-FAAL-276 | TC-FA-FAAL-E2E-073 | FE+BE |
| TC-FA-FAAL-277 | TC-FA-FAAL-E2E-081 | FE+BE |
| TC-FA-FAAL-278 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-279 | TC-FA-FAAL-E2E-059 | FE+BE |
| TC-FA-FAAL-280 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-281 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-282 | TC-FA-FAAL-E2E-053 | FE+BE |
| TC-FA-FAAL-283 | TC-FA-FAAL-E2E-053 | FE+BE |
| TC-FA-FAAL-284 | TC-FA-FAAL-E2E-075 | FE+BE |
| TC-FA-FAAL-285 | TC-FA-FAAL-E2E-060 | FE+BE |
| TC-FA-FAAL-286 | TC-FA-FAAL-E2E-030 | FE+BE |
| TC-FA-FAAL-287 | TC-FA-FAAL-E2E-099 | FE+BE |
| TC-FA-FAAL-288 | TC-FA-FAAL-E2E-052 | FE+BE |
| TC-FA-FAAL-289 | TC-FA-FAAL-E2E-074 | FE+BE |
