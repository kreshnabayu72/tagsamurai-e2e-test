# Coverage E2E — Fixed Asset > Settings > Accounting > Chart of Accounts

Sumber: `fixed-asset/settings-chart-of-accounts/TestCases/tc-settings-chart-of-accounts.md` (365 TC `TC-FA-COA-1`–`367`, semua aktif; id 116 dan 139 tidak dipakai). Suite: `specs/FixedAsset/SettingsChartOfAccounts/`. Prefix: `FA` + `COA` (`TC-FA-COA-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`). Tidak ada `tc-settings-chart-of-accounts-backend.md`.

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 365 TC aktif masuk 103 spec (83 nomor rencana `001`–`083`, nomor cadangan `084`–`094`, dan spec absence `095`–`103`), tidak ada TC hanya-BE. Setiap TC terpetakan ke tepat satu spec, kecuali 22 TC yang terbelah antara spec asal dan satu spec absence (S-05, lihat bagian Pembagian TC lintas spec); tabel di bawah dibangkitkan dari frontmatter `sourceTc`.

## Cakupan

Halaman Chart of Accounts (tab keempat Settings > Accounting): tabel akun dengan Search, Filter, Sort, Pagination, Setup Column, dan Download; modal Add Account dan Edit Account; Activate dan Deactivate (single dan bulk); Delete (single dan bulk) beserta dialog blok; popup Used By; Modal Changelog dan pencatatan di tiga surface; Role Matrix; Guided Tooltip; tampilan Android; batas jumlah akun dan Selection Limit; state tenant; konflik dua sesi; defense-in-depth; ketahanan terhadap kegagalan server.

## TC hanya-BE (tidak masuk spec)

Tidak ada.

## TC yang dipindah ke nomor cadangan dari nomor rencana

Penulis memecah spec yang melewati ~35 langkah ke nomor cadangan. Nomor rencana tetap dipakai oleh TC sisanya.

| Spec cadangan | TC | Asal (nomor rencana) |
|---|---|---|
| 084 | TC-367 | 012 |
| 085 | TC-363, TC-364 | 005 |
| 086 | TC-33, TC-289 | 017 |
| 087 | TC-122, TC-123, TC-343 | 020 |
| 088 | TC-295, TC-297 | 030 |
| 089 | TC-168, TC-355 | 034 |
| 090 | TC-184, TC-185 | 040 |
| 091 | TC-173 | 045 |
| 092 | TC-191 | 052 |
| 093 | TC-203 | 059 |
| 094 | TC-281, TC-160 | 073 |

## Spec absence (095–103)

Spec kelas g yang memuat asersi "tidak ada log" untuk klausa yang sebelumnya tanpa rumah (temuan a, diputuskan D1 opsi 1). Nomor `095`–`100` dari rencana; `101` dan `102` adalah nomor cadangan slice 1 yang dipakai karena `098` (empat TC, 54 langkah) dan `100` (empat TC, 48 langkah) melewati ~35 langkah bila digabung; `103` memuat klausa "tanpa log" TC-56 dan TC-350.

| Spec absence | TC | Spec asal |
|---|---|---|
| 095 | TC-269, 270, 271 | 070 |
| 096 | TC-36, 124, 272 | 071 (TC-36, 124), 072 (TC-272) |
| 097 | TC-273, 274, 275 | 072 |
| 098 | TC-32, 302 | 066 |
| 099 | TC-65, 305, 71 | 068 |
| 100 | TC-304, 361 | 067 |
| 101 | TC-41, 303 | 066 |
| 102 | TC-300, 301 | 069 |
| 103 | TC-56, 350 | 029 (TC-56), 028 (TC-350) |

## Pembagian TC lintas spec

- 22 TC ada di `sourceTc` dua spec, spec asal dan spec absence (S-05 `[KEPUTUSAN 2026-11-02]`; `check-suite.py` C2 melaporkannya `[REVIEW]`): TC-32, 36, 41, 56, 65, 71, 124, 269–275, 300–305, 350, 361. Spec asal (`028`, `029`, `066`–`072`) hanya mengasersi tampilan, respons server, dan state data, dan menulis rujukan di `## Notes`; spec absence memuat pemicu yang sama dengan baseline Changelog, System Log aktor, dan Activity Log sendiri per TC.
- Spec absence `083` memuat asersi "tidak ada log" untuk TC-51, 52, 96, 118 (aksi no-op dan item bulk yang dilewati).
- Spec multi-konteks `073`–`078` dan `075` menulis asersi "tidak ada log" lewat baseline di spec asal (butir `P-1`).

## Kebutuhan lingkungan (tim FE)

- Env var password terdaftar yang dipakai: `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_DU_PASSWORD` (Default User), `FA_GM_PASSWORD`. Sudah terdaftar di `spectra.config.ts` dan `.env.example` dengan nilai kosong (2026-11-04; tim FE mengisi nilainya): `FA_MACC_READ_PASSWORD`, `FA_MACC_CREATE_PASSWORD`, `FA_MACC_UPDATE_PASSWORD`, `FA_MACC_DELETE_PASSWORD`, `FA_MACC_UPDDEL_PASSWORD`, `FA_GMNOACC_PASSWORD`. `FA_GM_PASSWORD` terdaftar sebagai Group Manager Gedung A (Activity Log); pemakaian di suite ini (Group Manager untuk TC-153) perlu dikonfirmasi tim FE.
- Fixture `fixtures/settings-chart-of-accounts.json` (belum ada; nama kunci ditetapkan tim FE) serta seed dan pemulihan akun lewat API.
- Kemampuan teknis lain mengikuti butir di `suite.md`.

## Temuan dan keputusan

Diputuskan pengguna pada run ini:

a. Klausa "tidak ada log" tanpa spec rumah: D1 opsi 1. Spec absence `095`–`103` ditambahkan (lihat bagian Spec absence); spec `028`, `029`, dan `066`–`072` tidak lagi memuat klausa itu.
b. Target Pre-setup bersama untuk permintaan langsung ditolak: D2 opsi 1. Spec `070`, `071`, `072`, `075`, `079`, dan spec absence men-seed akun miliknya (Code `DID<NNN>x`) di hook `before` dan membersihkannya di `after`.
c. Batas literal 15 karakter pada Account Code (Lampiran A tidak memuatnya): D3 opsi 1. Code literal maksimal 15 karakter, memuat nomor spec untuk akun milik spec; alasannya ditulis di `## Prerequisites`. Nilai Code dari TC untuk Create yang selalu gagal atau ditolak dipertahankan. Konvensi tidak diubah di run ini; usulan butir Lampiran A menunggu batch konvensi sesudah loop suite.
d. Spec di atas ~35 langkah: D4 opsi 1. 44 spec dipertahankan, alasan tiap spec ada di Notes (046 (67), 050 (56), 053 (56), 064 (60), 042 (51), 063 (50), dan lainnya); `066` (56) dan `069` (58) tetap di atas 35 langkah.

Masih terbuka:

e. Ditunda dengan syarat (keputusan pengguna 2026-11-04; bukan keputusan terbuka, melainkan ketergantungan ke tim FE/BE; spec belum bisa dijalankan sampai terpenuhi, permintaan: `prd-harness/work-items/settings-chart-of-accounts/permintaan-fe-be.md`). Fixture dan env yang perlu disediakan tim FE (lihat bagian kebutuhan lingkungan), termasuk kemampuan seed pada client Suspended (spec `079`), penyetelan nilai default company lewat seed (spec `072`, `097`), dan kemampuan baca jumlah entri Changelog, System Log aktor, dan Activity Log per Account Code (spec absence).
f. Jalur ekspor (J-06): ditunda dengan syarat (keputusan pengguna 2026-11-04). Syarat: tim BE menyediakan fixture ekspor Journal J-06; spec yang butuh akun terekspor aktif (antara lain `032`, `071`, `096`) dilengkapi setelah itu.
- Detail temuan TC-sumber per spec ada di Notes "Temuan untuk QA".

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-FA-COA-E2E-001-screening-halaman-chart-of-accounts-tab-tabel-loading-dan-search-kosong | Screening Halaman Chart of Accounts: Tab, Tabel, Loading, dan Search Kosong | FE+BE | 34 | 1, 3, 4, 138 |
| TC-FA-COA-E2E-002-tabel-kosong-client-tanpa-akun | Tabel Kosong Client Tanpa Akun | FE+BE | 3 | 2 |
| TC-FA-COA-E2E-003-accessibility-switch-status-fokus-modal-dan-atribut-aria-form | Accessibility: Switch Status, Fokus Modal, dan Atribut ARIA Form | FE+BE | 48 | 161, 162, 291, 292 |
| TC-FA-COA-E2E-004-role-matrix-visibilitas-elemen-role-read-per-role | Role Matrix: Visibilitas Elemen Role Read per Role | FE+BE | 39 | 6, 7, 8, 9 |
| TC-FA-COA-E2E-005-role-matrix-visibilitas-elemen-role-write-per-role | Role Matrix: Visibilitas Elemen Role Write per Role | FE+BE | 32 | 10, 11 |
| TC-FA-COA-E2E-006-role-matrix-positif-create-dan-update-sampai-toast-sukses | Role Matrix Positif: Create dan Update sampai Toast Sukses | FE+BE | 42 | 261, 262, 263, 264, 265, 266 |
| TC-FA-COA-E2E-007-role-matrix-positif-delete-sampai-toast-sukses | Role Matrix Positif: Delete sampai Toast Sukses | FE+BE | 12 | 267, 268 |
| TC-FA-COA-E2E-008-role-matrix-negatif-akses-tab-ditolak-dan-switch-status-disabled | Role Matrix Negatif: Akses Tab Ditolak dan Switch Status Disabled | FE+BE | 14 | 12, 163 |
| TC-FA-COA-E2E-009-guided-tooltip-kunjungan-pertama-dan-skip-done | Guided Tooltip: Kunjungan Pertama dan Skip Done | FE+BE | 35 | 105, 337, 340, 341 |
| TC-FA-COA-E2E-010-guided-tooltip-mulai-ulang-back-next-dan-keyboard | Guided Tooltip: Mulai Ulang, Back Next, dan Keyboard | FE+BE | 22 | 338, 339, 342 |
| TC-FA-COA-E2E-011-mobile-android-card-list-toolbar-bottom-sheet-role | Mobile Android: Card List, Toolbar, Bottom Sheet, Role | FE+BE | 37 | 98, 99, 100, 102, 103, 104 |
| TC-FA-COA-E2E-012-mobile-android-selection-mode-popup-used-by-dan-switch-disabled | Mobile Android: Selection Mode, Popup Used By, dan Switch Disabled | FE+BE | 31 | 101, 366, 344, 345 |
| TC-FA-COA-E2E-013-add-account-screening-modal-dropdown-function-popover-dan-clear-field | Add Account: Screening Modal, Dropdown Function, Popover, dan Clear Field | FE+BE | 39 | 13, 15, 16, 18 |
| TC-FA-COA-E2E-014-add-account-validasi-wajib-spasi-karakter-dan-emoji | Add Account: Validasi Wajib, Spasi, Karakter, dan Emoji | FE+BE | 31 | 19, 20, 21, 22, 24, 27 |
| TC-FA-COA-E2E-015-add-account-validasi-batas-panjang-dan-whitelist-account-code | Add Account: Validasi Batas Panjang dan Whitelist Account Code | FE+BE | 38 | 23, 25, 26, 359, 360 |
| TC-FA-COA-E2E-016-add-account-validasi-duplikat-code-dan-create-dengan-search-dan-filter | Add Account: Validasi Duplikat Code dan Create dengan Search dan Filter Aktif | FE+BE | 35 | 28, 29, 143 |
| TC-FA-COA-E2E-017-add-account-create-sukses-name-sama-trim-dan-stay-on-this-form | Add Account: Create Sukses, Name Sama, Trim, dan Stay on this Form | FE+BE | 32 | 14, 17, 30, 260 |
| TC-FA-COA-E2E-018-add-account-tutup-form-unsaved-changes-dan-nilai-dikembalikan | Add Account: Tutup Form, Unsaved Changes, dan Nilai Dikembalikan | FE+BE | 28 | 236, 237, 238, 239, 241 |
| TC-FA-COA-E2E-019-add-account-klik-backdrop-refresh-sidebar-dan-esc-pada-form-dirty | Add Account: Klik Backdrop, Refresh, Sidebar, dan Esc pada Form Dirty | FE+BE | 34 | 240, 242, 243, 244, 356 |
| TC-FA-COA-E2E-020-edit-account-screening-modal-kunci-field-dan-tooltip-kunci | Edit Account: Screening Modal, Kunci Field, dan Tooltip Kunci | FE+BE | 26 | 34, 35, 42 |
| TC-FA-COA-E2E-021-edit-account-validasi-field-diblokir | Edit Account: Validasi Field Diblokir | FE+BE | 31 | 253, 254, 255, 256, 257, 258 |
| TC-FA-COA-E2E-022-edit-account-duplikat-code-simpan-berhasil-no-op-trim-dan-perubahan | Edit Account: Duplikat Code, Simpan Berhasil, No-Op, Trim, dan Perubahan Huruf | FE+BE | 50 | 37, 38, 39, 40, 144, 259 |
| TC-FA-COA-E2E-023-edit-account-multi-field-log-akun-inactive-terekspor-double-save-dan | Edit Account: Multi-Field Log, Akun Inactive Terekspor, Double Save, dan Saving State | FE+BE | 49 | 145, 283, 290, 365 |
| TC-FA-COA-E2E-024-edit-account-tutup-form-unsaved-changes-dan-backdrop | Edit Account: Tutup Form, Unsaved Changes, dan Backdrop | FE+BE | 41 | 245, 246, 247, 248, 249, 250 |
| TC-FA-COA-E2E-025-edit-account-refresh-sidebar-dan-esc-pada-form-dirty | Edit Account: Refresh, Sidebar, dan Esc pada Form Dirty | FE+BE | 34 | 251, 252, 357 |
| TC-FA-COA-E2E-026-activate-deactivate-single-dialog-cancel-no-op-dan-double-click | Activate Deactivate Single: Dialog, Cancel, No-Op, dan Double Click | FE+BE | 18 | 46, 47, 285 |
| TC-FA-COA-E2E-027-deactivate-single-pernah-diekspor-akun-default-company-dan-spinner | Deactivate Single: Pernah Diekspor, Akun Default Company, dan Spinner | FE+BE | 38 | 48, 49, 50, 164, 286 |
| TC-FA-COA-E2E-028-bulk-activate-seleksi-campuran-dan-collapse-single | Bulk Activate: Seleksi, Campuran, dan Collapse Single | FE+BE | 43 | 53, 54, 298, 350 |
| TC-FA-COA-E2E-029-bulk-deactivate-semua-eligible-campuran-collapse-dan-d-03-satu-akun | Bulk Deactivate: Semua Eligible, Campuran, Collapse, dan D-03 Satu Akun | FE+BE | 40 | 55, 56, 299, 354 |
| TC-FA-COA-E2E-030-cancel-dialog-bulk-activate-deactivate-dan-delete | Cancel Dialog Bulk Activate, Deactivate, dan Delete | FE+BE | 36 | 293, 294, 296 |
| TC-FA-COA-E2E-031-blokir-deactivate-akun-dipakai-asset-class | Blokir Deactivate: Akun Dipakai Asset Class | FE+BE | 43 | 125, 126, 127, 128, 156 |
| TC-FA-COA-E2E-032-blokir-delete-single-akun-terekspor-dan-dipakai-asset-class | Blokir Delete Single: Akun Terekspor dan Dipakai Asset Class | FE+BE | 34 | 59, 60, 129, 130, 136 |
| TC-FA-COA-E2E-033-blokir-delete-single-akun-default-company | Blokir Delete Single: Akun Default Company | FE+BE | 35 | 165, 166, 167 |
| TC-FA-COA-E2E-034-blokir-bulk-delete-seluruh-seleksi-diblokir | Blokir Bulk Delete: Seluruh Seleksi Diblokir | FE+BE | 20 | 70, 131 |
| TC-FA-COA-E2E-035-bulk-delete-campuran-akun-eligible-dihapus-akun-terekspor-atau-dipakai | Bulk Delete Campuran: Akun Eligible Dihapus, Akun Terekspor atau Dipakai Asset Class Dilewati | FE+BE | 35 | 69, 115, 132 |
| TC-FA-COA-E2E-036-bulk-delete-campuran-dengan-akun-default-company | Bulk Delete Campuran dengan Akun Default Company | FE+BE | 23 | 169, 170 |
| TC-FA-COA-E2E-037-popup-used-by-daftar-asset-class-urutan-dan-loading | Popup Used By: Daftar Asset Class, Urutan, dan Loading | FE+BE | 45 | 133, 134, 135, 154, 155, 287 |
| TC-FA-COA-E2E-038-used-by-berubah-saat-asset-class-memakai-atau-melepas-akun | Used By Berubah Saat Asset Class Memakai atau Melepas Akun | FE+BE | 47 | 157, 158 |
| TC-FA-COA-E2E-039-delete-single-dan-bulk-delete-berhasil | Delete Single dan Bulk Delete Berhasil | FE+BE | 39 | 61, 62, 63, 67, 68, 284 |
| TC-FA-COA-E2E-040-search-tabel-per-kolom-hidden-dan-used-by | Search Tabel: Per Kolom, Hidden, dan Used By | FE+BE | 31 | 72, 73, 74, 183, 320 |
| TC-FA-COA-E2E-041-search-tabel-perilaku-kotak-search-dan-trim-spasi | Search Tabel: Perilaku Kotak Search dan Trim Spasi | FE+BE | 34 | 229, 316, 317, 318, 319 |
| TC-FA-COA-E2E-042-filter-panel-tabel-struktur-opsi-dan-multi-select | Filter Panel Tabel: Struktur, Opsi, dan Multi-Select | FE+BE | 51 | 75, 76, 180, 186, 322 |
| TC-FA-COA-E2E-043-filter-panel-tabel-periode-date-range-used-by-dan-kombinasi-and | Filter Panel Tabel: Periode, Date Range, Used By, dan Kombinasi AND | FE+BE | 40 | 77, 78, 181, 323, 324 |
| TC-FA-COA-E2E-044-filter-panel-tabel-tutup-panel-badge-indikator-chip-dan-dropdown | Filter Panel Tabel: Tutup Panel, Badge Indikator, Chip, dan Dropdown | FE+BE | 42 | 214, 215, 218, 329, 330, 331 |
| TC-FA-COA-E2E-045-sort-tabel-default-siklus-tiga-tahap-dan-kolom-teks-numerik | Sort Tabel: Default, Siklus Tiga Tahap pada Account Name, Account Code, Active, dan Used By | FE+BE | 39 | 80, 182, 174, 175 |
| TC-FA-COA-E2E-046-sort-tabel-last-used-last-updated-kolom-tanpa-sort-pindah-kolom-dan-tie | Sort Tabel: Last Used in Journal, Last Updated, Kolom Tanpa Sort, Pindah Kolom, dan Tie-Breaker | FE+BE | 67 | 176, 177, 178, 179, 220 |
| TC-FA-COA-E2E-047-kombinasi-search-filter-sort-paginasi-pada-tabel | Kombinasi Search, Filter, Sort, dan Paginasi pada Tabel | FE+BE | 38 | 79, 325, 326, 327 |
| TC-FA-COA-E2E-048-paginasi-tabel-dan-hapus-baris-terakhir | Paginasi Tabel: Reset Halaman, Input Halaman Tidak Valid, Ukuran Halaman, dan Hapus Baris Terakhir | FE+BE | 44 | 81, 225, 227, 228, 226 |
| TC-FA-COA-E2E-049-list-state-dan-independensi-filter-dari-column-visibility | List State dan Independensi Filter dari Column Visibility | FE+BE | 44 | 231, 232, 233, 234 |
| TC-FA-COA-E2E-050-row-action-dan-bulk-action-bar-seleksi-select-all-dan-clear | Row Action dan Bulk Action Bar: Seleksi, Select All, dan Clear | FE+BE | 56 | 306, 307, 308, 309, 310, 328 |
| TC-FA-COA-E2E-051-setup-column-tabel-quick-panel-popup-dan-kolom-default-hidden | Setup Column Tabel: Quick Panel, Popup, dan Kolom Default Hidden | FE+BE | 35 | 187, 188, 189, 193 |
| TC-FA-COA-E2E-052-setup-column-tabel-reorder-pin-dan-guard-pin-keempat | Setup Column Tabel: Reorder, Pin, dan Guard Pin Keempat | FE+BE | 39 | 190, 194, 332, 333 |
| TC-FA-COA-E2E-053-setup-column-tabel-pin-hidden-reset-to-default-dan-tutup-tanpa-save | Setup Column Tabel: Pin Hidden, Reset to Default, dan Tutup Tanpa Save | FE+BE | 56 | 82, 83, 192, 195, 196 |
| TC-FA-COA-E2E-054-format-tampilan-last-updated-modified-by-dan-date-changelog | Format Tampilan Last Updated, Modified By, dan Date Changelog | FE+BE | 32 | 311, 312, 313, 314, 315 |
| TC-FA-COA-E2E-055-download-tabel-isi-berkas-mengikuti-search-filter-sort-dan-kolom | Download Tabel: Isi Berkas mengikuti Search, Filter, Sort, dan Kolom | FE+BE | 43 | 84, 85, 86, 223, 224, 334 |
| TC-FA-COA-E2E-056-download-tabel-format-csv-bom-xlsx-sheet1-dan-lintas-halaman | Download Tabel: Format CSV BOM, XLSX Sheet1, dan Lintas Halaman | FE+BE | 24 | 221, 222, 358 |
| TC-FA-COA-E2E-057-modal-changelog-screening-loading-kosong-dan-sort | Modal Changelog: Screening, Loading, Kosong, dan Sort | FE+BE | 34 | 88, 89, 91, 197, 198, 199, 288 |
| TC-FA-COA-E2E-058-modal-changelog-search-per-kolom | Modal Changelog: Search per Kolom | FE+BE | 30 | 200, 201, 230, 321 |
| TC-FA-COA-E2E-059-modal-changelog-struktur-filter-opsi-date-range-dan-multi-select | Modal Changelog: Struktur Filter, Date Range, dan Multi-Select | FE+BE | 40 | 90, 202, 204, 205 |
| TC-FA-COA-E2E-060-modal-changelog-tutup-panel-filter-badge-paginasi-dan-download | Modal Changelog: Tutup Panel Filter, Badge, Paginasi, dan Download | FE+BE | 36 | 216, 217, 219, 335, 336 |
| TC-FA-COA-E2E-061-modal-changelog-setup-column-quick-panel-popup-checkbox-dan-guard | Modal Changelog: Setup Column Quick Panel, Popup, Checkbox, dan Guard | FE+BE | 29 | 206, 207, 208, 213 |
| TC-FA-COA-E2E-062-modal-changelog-setup-column-reorder-pin-reset-dan-tutup | Modal Changelog: Setup Column Reorder, Pin, Reset, dan Tutup | FE+BE | 36 | 209, 210, 211, 212 |
| TC-FA-COA-E2E-063-audit-log-create-dan-snapshot-tie-breaker-changelog | Audit Log: Create dan Snapshot, Tie-Breaker Changelog | FE+BE | 50 | 92, 97, 235 |
| TC-FA-COA-E2E-064-audit-log-edit-account-code-activate-deactivate-dan-delete | Audit Log: Edit Account Code, Activate Deactivate, dan Delete | FE+BE | 60 | 93, 94, 95 |
| TC-FA-COA-E2E-065-last-used-in-journal-hover-tanpa-input-manual-dan-jalur-api | Last Used in Journal: Hover, Tanpa Input Manual, dan Jalur API | FE+BE | 38 | 106, 117, 119, 120 |
| TC-FA-COA-E2E-066-resilience-create-dan-edit-gagal-5xx-dan-timeout | Resilience Create dan Edit Account: Respons 5xx dan Timeout Mempertahankan Modal dan Input | FE+BE | 56 | 32, 302, 41, 303 |
| TC-FA-COA-E2E-067-resilience-activate-dan-deactivate-single-gagal-dan-timeout | Resilience Activate dan Deactivate Single: Respons 5xx dan Timeout Mengembalikan Switch dan Mempertahankan Dialog | FE+BE | 36 | 57, 58, 304, 361 |
| TC-FA-COA-E2E-068-resilience-delete-single-dan-bulk-delete-gagal-dan-timeout | Resilience Delete Single dan Bulk Delete: Respons 5xx dan Timeout Mempertahankan Dialog dan Data | FE+BE | 32 | 65, 305, 71 |
| TC-FA-COA-E2E-069-resilience-bulk-gagal-timeout-dan-load-error-tabel | Resilience Bulk Activate dan Deactivate Gagal, Timeout, dan Error State Tabel | FE+BE | 58 | 5, 300, 301, 362 |
| TC-FA-COA-E2E-070-defense-in-depth-akses-langsung-per-role-ditolak-server | Defense-in-Depth: Akses Langsung per Role Ditolak Server | FE+BE | 36 | 107, 108, 153, 269, 270, 271 |
| TC-FA-COA-E2E-071-defense-in-depth-akses-langsung-atas-akun-terkunci-dan-lintas-client | Defense-in-Depth: Akses Langsung atas Akun Terkunci dan Lintas Client | FE+BE | 16 | 36, 109, 110, 111, 124 |
| TC-FA-COA-E2E-072-defense-in-depth-akses-langsung-atas-akun-terpakai-dan-default-company | Defense-in-Depth: Akses Langsung atas Akun Terpakai dan Default Company, serta Nama Berisi HTML | FE+BE | 23 | 121, 272, 273, 274, 275 |
| TC-FA-COA-E2E-073-multi-konteks-edit-serentak-kunci-berubah-dan-last-write-wins | Multi-Konteks: Edit Akun saat Kunci Berubah oleh Sesi Lain dan Edit Serentak Dua Sesi (Last-Write-Wins) | FE+BE | 31 | 43, 44, 45 |
| TC-FA-COA-E2E-074-multi-konteks-aksi-single-atas-akun-yang-berubah-oleh-sesi-lain | Multi-Konteks: Aksi Single (Save Edit, Activate, Deactivate) atas Akun yang Dihapus atau Sudah Berubah Status oleh Sesi Lain | FE+BE | 44 | 146, 147, 148, 150, 151 |
| TC-FA-COA-E2E-075-multi-konteks-delete-dan-guard-berubah-antara-dialog-dan-confirm | Multi-Konteks: Delete Single dan Guard Berubah antara Dialog Dibuka dan Confirm (Akun Dihapus, Diekspor, atau Dipakai Asset Class) | FE+BE | 34 | 64, 66, 137, 349 |
| TC-FA-COA-E2E-076-multi-konteks-bulk-aksi-atas-akun-sudah-dihapus-atau-sudah-berubah | Multi-Konteks: Bulk Activate dan Deactivate saat Seluruh Akun Terpilih Sudah Dihapus atau Sudah Berstatus Target oleh Sesi Lain | FE+BE | 41 | 149, 152, 351, 352 |
| TC-FA-COA-E2E-077-multi-konteks-bulk-sebagian-dihapus-sesi-lain | Multi-Konteks: Bulk Deactivate, Activate, dan Delete saat Sebagian Akun Terpilih Dihapus Sesi Lain, Akun Lain Tetap Diproses | FE+BE | 52 | 114, 171, 172, 353 |
| TC-FA-COA-E2E-078-multi-konteks-bulk-guard-berubah-antara-dialog-dan-confirm | Multi-Konteks: Bulk Deactivate dan Bulk Delete saat Guard Berubah antara Dialog Dibuka dan Confirm (Dipakai Asset Class atau Diekspor) | FE+BE | 43 | 346, 347, 348 |
| TC-FA-COA-E2E-079-state-tenant-suspended-expired-dan-plan-starter | State Tenant: Client Suspended atau Expired Menolak Aksi Tulis dan Plan Starter Menonaktifkan Menu Accounting | FE+BE | 40 | 112, 113, 277, 278, 279, 280, 142 |
| TC-FA-COA-E2E-080-batas-jumlah-akun-master-data-count-limit | Batas Jumlah Akun: Master Data Count Limit Memblokir Penambahan Akun | FE+BE | 28 | 31, 159, 282 |
| TC-FA-COA-E2E-081-selection-limit-batas-seleksi-100 | Selection Limit: Batas Seleksi 100 pada Select All, Seleksi Manual, dan Permintaan Langsung Bulk | FE+BE | 23 | 140, 141, 276 |
| TC-FA-COA-E2E-082-download-lebih-dari-5000-baris | Download Lebih dari 5.000 Baris: Loading Tampil sampai Berkas Siap | FE+BE | 5 | 87 |
| TC-FA-COA-E2E-083-absence-log-aksi-no-op-dan-item-bulk-yang-dilewati | Absence Log: Aksi No-Op dan Item Bulk yang Dilewati Tidak Menulis Log | FE+BE | 49 | 51, 52, 96, 118 |
| TC-FA-COA-E2E-084-mobile-android-selection-mode-setelah-bulk-commit-cancel-dan-dialog-blok | Mobile Android: Selection Mode Setelah Bulk Commit, Cancel, dan Dialog Blok | FE+BE | 22 | 367 |
| TC-FA-COA-E2E-085-role-matrix-visibilitas-elemen-update-delete-dan-default-user | Role Matrix: Visibilitas Elemen Update + Delete dan Default User | FE+BE | 34 | 363, 364 |
| TC-FA-COA-E2E-086-add-account-klik-ganda-submit-dan-saving-state | Add Account: Klik Ganda Submit dan Saving State | FE+BE | 17 | 33, 289 |
| TC-FA-COA-E2E-087-edit-account-tooltip-kunci-function-used-by-dan-last-used-in-journal | Edit Account: Tooltip Kunci Function karena Used By dan Last Used in Journal | FE+BE | 19 | 122, 123, 343 |
| TC-FA-COA-E2E-088-cancel-dialog-bulk-deactivate-dan-delete-campuran | Cancel Dialog Bulk Deactivate dan Delete Campuran (D-03 dan D-09) | FE+BE | 25 | 295, 297 |
| TC-FA-COA-E2E-089-blokir-bulk-delete-akun-default-company | Blokir Bulk Delete: Seluruh Seleksi Akun Default Company | FE+BE | 26 | 168, 355 |
| TC-FA-COA-E2E-090-search-tabel-modified-by-dan-guard-negatif | Search Tabel: Modified By dan Guard Negatif | FE+BE | 29 | 184, 185 |
| TC-FA-COA-E2E-091-sort-tabel-kolom-function-dan-modified-by | Sort Tabel: Siklus Tiga Tahap pada Kolom Function dan Modified By | FE+BE | 24 | 173 |
| TC-FA-COA-E2E-092-setup-column-tabel-pin-dan-unpin-kolom-default-visible | Setup Column Tabel: Pin dan Unpin Kolom Default Visible | FE+BE | 10 | 191 |
| TC-FA-COA-E2E-093-modal-changelog-isi-opsi-dropdown-filter | Modal Changelog: Isi Opsi Dropdown Filter | FE+BE | 24 | 203 |
| TC-FA-COA-E2E-094-multi-konteks-create-serentak-code-sama-dan-batas-akun-antara-klik-dan-submit | Multi-Konteks: Create Serentak Dua Sesi dengan Account Code Sama dan Batas Jumlah Akun Tercapai antara Klik dan Submit | FE+BE | 35 | 281, 160 |
| TC-FA-COA-E2E-095-absence-log-permintaan-langsung-ditolak-role-create-update-dan-delete | Absence Log: Permintaan Langsung Ditolak Role Create, Update, dan Delete Tidak Menulis Log | FE+BE | 25 | 269, 270, 271 |
| TC-FA-COA-E2E-096-absence-log-permintaan-langsung-atas-akun-terkunci-dan-akun-dipakai-asset-class-ditolak | Absence Log: Permintaan Langsung atas Akun Terekspor dan Akun Dipakai Asset Class Ditolak Tidak Menulis Log | FE+BE | 18 | 36, 124, 272 |
| TC-FA-COA-E2E-097-absence-log-permintaan-langsung-atas-akun-default-company-dan-bulk-campuran-ditolak | Absence Log: Permintaan Langsung Delete Akun Terpakai, Akun Default Company, dan Bulk Deactivate Campuran Tidak Menulis Log untuk Akun Terblokir | FE+BE | 18 | 273, 274, 275 |
| TC-FA-COA-E2E-098-absence-log-create-gagal-5xx-atau-timeout | Absence Log: Create Account Gagal 5xx atau Timeout Tidak Menulis Log | FE+BE | 26 | 32, 302 |
| TC-FA-COA-E2E-099-absence-log-delete-single-dan-bulk-delete-gagal-5xx-atau-timeout | Absence Log: Delete Single dan Bulk Delete Gagal 5xx atau Timeout Tidak Menulis Log | FE+BE | 35 | 65, 305, 71 |
| TC-FA-COA-E2E-100-absence-log-activate-dan-deactivate-single-gagal-5xx-atau-timeout | Absence Log: Activate dan Deactivate Single Timeout Tidak Menulis Log | FE+BE | 22 | 304, 361 |
| TC-FA-COA-E2E-101-absence-log-edit-gagal-5xx-atau-timeout | Absence Log: Save Edit Gagal 5xx atau Timeout Tidak Menulis Log | FE+BE | 28 | 41, 303 |
| TC-FA-COA-E2E-102-absence-log-bulk-activate-dan-deactivate-gagal-5xx | Absence Log: Bulk Activate dan Bulk Deactivate Gagal 5xx Tidak Menulis Log | FE+BE | 28 | 300, 301 |
| TC-FA-COA-E2E-103-absence-log-bulk-activate-dan-deactivate-seleksi-campuran | Absence Log: Bulk Deactivate dan Bulk Activate Seleksi Campuran Tidak Menulis Log untuk Akun yang Dilewati | FE+BE | 39 | 56, 350 |

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-FA-COA-1 | TC-FA-COA-E2E-001 | FE+BE |
| TC-FA-COA-2 | TC-FA-COA-E2E-002 | FE+BE |
| TC-FA-COA-3 | TC-FA-COA-E2E-001 | FE+BE |
| TC-FA-COA-4 | TC-FA-COA-E2E-001 | FE+BE |
| TC-FA-COA-5 | TC-FA-COA-E2E-069 | FE+BE |
| TC-FA-COA-6 | TC-FA-COA-E2E-004 | FE+BE |
| TC-FA-COA-7 | TC-FA-COA-E2E-004 | FE+BE |
| TC-FA-COA-8 | TC-FA-COA-E2E-004 | FE+BE |
| TC-FA-COA-9 | TC-FA-COA-E2E-004 | FE+BE |
| TC-FA-COA-10 | TC-FA-COA-E2E-005 | FE+BE |
| TC-FA-COA-11 | TC-FA-COA-E2E-005 | FE+BE |
| TC-FA-COA-12 | TC-FA-COA-E2E-008 | FE+BE |
| TC-FA-COA-13 | TC-FA-COA-E2E-013 | FE+BE |
| TC-FA-COA-14 | TC-FA-COA-E2E-017 | FE+BE |
| TC-FA-COA-15 | TC-FA-COA-E2E-013 | FE+BE |
| TC-FA-COA-16 | TC-FA-COA-E2E-013 | FE+BE |
| TC-FA-COA-17 | TC-FA-COA-E2E-017 | FE+BE |
| TC-FA-COA-18 | TC-FA-COA-E2E-013 | FE+BE |
| TC-FA-COA-19 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-20 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-21 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-22 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-23 | TC-FA-COA-E2E-015 | FE+BE |
| TC-FA-COA-24 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-25 | TC-FA-COA-E2E-015 | FE+BE |
| TC-FA-COA-26 | TC-FA-COA-E2E-015 | FE+BE |
| TC-FA-COA-27 | TC-FA-COA-E2E-014 | FE+BE |
| TC-FA-COA-28 | TC-FA-COA-E2E-016 | FE+BE |
| TC-FA-COA-29 | TC-FA-COA-E2E-016 | FE+BE |
| TC-FA-COA-30 | TC-FA-COA-E2E-017 | FE+BE |
| TC-FA-COA-31 | TC-FA-COA-E2E-080 | FE+BE |
| TC-FA-COA-32 | TC-FA-COA-E2E-066, TC-FA-COA-E2E-098 | FE+BE |
| TC-FA-COA-33 | TC-FA-COA-E2E-086 | FE+BE |
| TC-FA-COA-34 | TC-FA-COA-E2E-020 | FE+BE |
| TC-FA-COA-35 | TC-FA-COA-E2E-020 | FE+BE |
| TC-FA-COA-36 | TC-FA-COA-E2E-071, TC-FA-COA-E2E-096 | FE+BE |
| TC-FA-COA-37 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-38 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-39 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-40 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-41 | TC-FA-COA-E2E-066, TC-FA-COA-E2E-101 | FE+BE |
| TC-FA-COA-42 | TC-FA-COA-E2E-020 | FE+BE |
| TC-FA-COA-43 | TC-FA-COA-E2E-073 | FE+BE |
| TC-FA-COA-44 | TC-FA-COA-E2E-073 | FE+BE |
| TC-FA-COA-45 | TC-FA-COA-E2E-073 | FE+BE |
| TC-FA-COA-46 | TC-FA-COA-E2E-026 | FE+BE |
| TC-FA-COA-47 | TC-FA-COA-E2E-026 | FE+BE |
| TC-FA-COA-48 | TC-FA-COA-E2E-027 | FE+BE |
| TC-FA-COA-49 | TC-FA-COA-E2E-027 | FE+BE |
| TC-FA-COA-50 | TC-FA-COA-E2E-027 | FE+BE |
| TC-FA-COA-51 | TC-FA-COA-E2E-083 | FE+BE |
| TC-FA-COA-52 | TC-FA-COA-E2E-083 | FE+BE |
| TC-FA-COA-53 | TC-FA-COA-E2E-028 | FE+BE |
| TC-FA-COA-54 | TC-FA-COA-E2E-028 | FE+BE |
| TC-FA-COA-55 | TC-FA-COA-E2E-029 | FE+BE |
| TC-FA-COA-56 | TC-FA-COA-E2E-029, TC-FA-COA-E2E-103 | FE+BE |
| TC-FA-COA-57 | TC-FA-COA-E2E-067 | FE+BE |
| TC-FA-COA-58 | TC-FA-COA-E2E-067 | FE+BE |
| TC-FA-COA-59 | TC-FA-COA-E2E-032 | FE+BE |
| TC-FA-COA-60 | TC-FA-COA-E2E-032 | FE+BE |
| TC-FA-COA-61 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-62 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-63 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-64 | TC-FA-COA-E2E-075 | FE+BE |
| TC-FA-COA-65 | TC-FA-COA-E2E-068, TC-FA-COA-E2E-099 | FE+BE |
| TC-FA-COA-66 | TC-FA-COA-E2E-075 | FE+BE |
| TC-FA-COA-67 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-68 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-69 | TC-FA-COA-E2E-035 | FE+BE |
| TC-FA-COA-70 | TC-FA-COA-E2E-034 | FE+BE |
| TC-FA-COA-71 | TC-FA-COA-E2E-068, TC-FA-COA-E2E-099 | FE+BE |
| TC-FA-COA-72 | TC-FA-COA-E2E-040 | FE+BE |
| TC-FA-COA-73 | TC-FA-COA-E2E-040 | FE+BE |
| TC-FA-COA-74 | TC-FA-COA-E2E-040 | FE+BE |
| TC-FA-COA-75 | TC-FA-COA-E2E-042 | FE+BE |
| TC-FA-COA-76 | TC-FA-COA-E2E-042 | FE+BE |
| TC-FA-COA-77 | TC-FA-COA-E2E-043 | FE+BE |
| TC-FA-COA-78 | TC-FA-COA-E2E-043 | FE+BE |
| TC-FA-COA-79 | TC-FA-COA-E2E-047 | FE+BE |
| TC-FA-COA-80 | TC-FA-COA-E2E-045 | FE+BE |
| TC-FA-COA-81 | TC-FA-COA-E2E-048 | FE+BE |
| TC-FA-COA-82 | TC-FA-COA-E2E-053 | FE+BE |
| TC-FA-COA-83 | TC-FA-COA-E2E-053 | FE+BE |
| TC-FA-COA-84 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-85 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-86 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-87 | TC-FA-COA-E2E-082 | FE+BE |
| TC-FA-COA-88 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-89 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-90 | TC-FA-COA-E2E-059 | FE+BE |
| TC-FA-COA-91 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-92 | TC-FA-COA-E2E-063 | FE+BE |
| TC-FA-COA-93 | TC-FA-COA-E2E-064 | FE+BE |
| TC-FA-COA-94 | TC-FA-COA-E2E-064 | FE+BE |
| TC-FA-COA-95 | TC-FA-COA-E2E-064 | FE+BE |
| TC-FA-COA-96 | TC-FA-COA-E2E-083 | FE+BE |
| TC-FA-COA-97 | TC-FA-COA-E2E-063 | FE+BE |
| TC-FA-COA-98 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-99 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-100 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-101 | TC-FA-COA-E2E-012 | FE+BE |
| TC-FA-COA-102 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-103 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-104 | TC-FA-COA-E2E-011 | FE+BE |
| TC-FA-COA-105 | TC-FA-COA-E2E-009 | FE+BE |
| TC-FA-COA-106 | TC-FA-COA-E2E-065 | FE+BE |
| TC-FA-COA-107 | TC-FA-COA-E2E-070 | FE+BE |
| TC-FA-COA-108 | TC-FA-COA-E2E-070 | FE+BE |
| TC-FA-COA-109 | TC-FA-COA-E2E-071 | FE+BE |
| TC-FA-COA-110 | TC-FA-COA-E2E-071 | FE+BE |
| TC-FA-COA-111 | TC-FA-COA-E2E-071 | FE+BE |
| TC-FA-COA-112 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-113 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-114 | TC-FA-COA-E2E-077 | FE+BE |
| TC-FA-COA-115 | TC-FA-COA-E2E-035 | FE+BE |
| TC-FA-COA-117 | TC-FA-COA-E2E-065 | FE+BE |
| TC-FA-COA-118 | TC-FA-COA-E2E-083 | FE+BE |
| TC-FA-COA-119 | TC-FA-COA-E2E-065 | FE+BE |
| TC-FA-COA-120 | TC-FA-COA-E2E-065 | FE+BE |
| TC-FA-COA-121 | TC-FA-COA-E2E-072 | FE+BE |
| TC-FA-COA-122 | TC-FA-COA-E2E-087 | FE+BE |
| TC-FA-COA-123 | TC-FA-COA-E2E-087 | FE+BE |
| TC-FA-COA-124 | TC-FA-COA-E2E-071, TC-FA-COA-E2E-096 | FE+BE |
| TC-FA-COA-125 | TC-FA-COA-E2E-031 | FE+BE |
| TC-FA-COA-126 | TC-FA-COA-E2E-031 | FE+BE |
| TC-FA-COA-127 | TC-FA-COA-E2E-031 | FE+BE |
| TC-FA-COA-128 | TC-FA-COA-E2E-031 | FE+BE |
| TC-FA-COA-129 | TC-FA-COA-E2E-032 | FE+BE |
| TC-FA-COA-130 | TC-FA-COA-E2E-032 | FE+BE |
| TC-FA-COA-131 | TC-FA-COA-E2E-034 | FE+BE |
| TC-FA-COA-132 | TC-FA-COA-E2E-035 | FE+BE |
| TC-FA-COA-133 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-134 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-135 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-136 | TC-FA-COA-E2E-032 | FE+BE |
| TC-FA-COA-137 | TC-FA-COA-E2E-075 | FE+BE |
| TC-FA-COA-138 | TC-FA-COA-E2E-001 | FE+BE |
| TC-FA-COA-140 | TC-FA-COA-E2E-081 | FE+BE |
| TC-FA-COA-141 | TC-FA-COA-E2E-081 | FE+BE |
| TC-FA-COA-142 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-143 | TC-FA-COA-E2E-016 | FE+BE |
| TC-FA-COA-144 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-145 | TC-FA-COA-E2E-023 | FE+BE |
| TC-FA-COA-146 | TC-FA-COA-E2E-074 | FE+BE |
| TC-FA-COA-147 | TC-FA-COA-E2E-074 | FE+BE |
| TC-FA-COA-148 | TC-FA-COA-E2E-074 | FE+BE |
| TC-FA-COA-149 | TC-FA-COA-E2E-076 | FE+BE |
| TC-FA-COA-150 | TC-FA-COA-E2E-074 | FE+BE |
| TC-FA-COA-151 | TC-FA-COA-E2E-074 | FE+BE |
| TC-FA-COA-152 | TC-FA-COA-E2E-076 | FE+BE |
| TC-FA-COA-153 | TC-FA-COA-E2E-070 | FE+BE |
| TC-FA-COA-154 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-155 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-156 | TC-FA-COA-E2E-031 | FE+BE |
| TC-FA-COA-157 | TC-FA-COA-E2E-038 | FE+BE |
| TC-FA-COA-158 | TC-FA-COA-E2E-038 | FE+BE |
| TC-FA-COA-159 | TC-FA-COA-E2E-080 | FE+BE |
| TC-FA-COA-160 | TC-FA-COA-E2E-094 | FE+BE |
| TC-FA-COA-161 | TC-FA-COA-E2E-003 | FE+BE |
| TC-FA-COA-162 | TC-FA-COA-E2E-003 | FE+BE |
| TC-FA-COA-163 | TC-FA-COA-E2E-008 | FE+BE |
| TC-FA-COA-164 | TC-FA-COA-E2E-027 | FE+BE |
| TC-FA-COA-165 | TC-FA-COA-E2E-033 | FE+BE |
| TC-FA-COA-166 | TC-FA-COA-E2E-033 | FE+BE |
| TC-FA-COA-167 | TC-FA-COA-E2E-033 | FE+BE |
| TC-FA-COA-168 | TC-FA-COA-E2E-089 | FE+BE |
| TC-FA-COA-169 | TC-FA-COA-E2E-036 | FE+BE |
| TC-FA-COA-170 | TC-FA-COA-E2E-036 | FE+BE |
| TC-FA-COA-171 | TC-FA-COA-E2E-077 | FE+BE |
| TC-FA-COA-172 | TC-FA-COA-E2E-077 | FE+BE |
| TC-FA-COA-173 | TC-FA-COA-E2E-091 | FE+BE |
| TC-FA-COA-174 | TC-FA-COA-E2E-045 | FE+BE |
| TC-FA-COA-175 | TC-FA-COA-E2E-045 | FE+BE |
| TC-FA-COA-176 | TC-FA-COA-E2E-046 | FE+BE |
| TC-FA-COA-177 | TC-FA-COA-E2E-046 | FE+BE |
| TC-FA-COA-178 | TC-FA-COA-E2E-046 | FE+BE |
| TC-FA-COA-179 | TC-FA-COA-E2E-046 | FE+BE |
| TC-FA-COA-180 | TC-FA-COA-E2E-042 | FE+BE |
| TC-FA-COA-181 | TC-FA-COA-E2E-043 | FE+BE |
| TC-FA-COA-182 | TC-FA-COA-E2E-045 | FE+BE |
| TC-FA-COA-183 | TC-FA-COA-E2E-040 | FE+BE |
| TC-FA-COA-184 | TC-FA-COA-E2E-090 | FE+BE |
| TC-FA-COA-185 | TC-FA-COA-E2E-090 | FE+BE |
| TC-FA-COA-186 | TC-FA-COA-E2E-042 | FE+BE |
| TC-FA-COA-187 | TC-FA-COA-E2E-051 | FE+BE |
| TC-FA-COA-188 | TC-FA-COA-E2E-051 | FE+BE |
| TC-FA-COA-189 | TC-FA-COA-E2E-051 | FE+BE |
| TC-FA-COA-190 | TC-FA-COA-E2E-052 | FE+BE |
| TC-FA-COA-191 | TC-FA-COA-E2E-092 | FE+BE |
| TC-FA-COA-192 | TC-FA-COA-E2E-053 | FE+BE |
| TC-FA-COA-193 | TC-FA-COA-E2E-051 | FE+BE |
| TC-FA-COA-194 | TC-FA-COA-E2E-052 | FE+BE |
| TC-FA-COA-195 | TC-FA-COA-E2E-053 | FE+BE |
| TC-FA-COA-196 | TC-FA-COA-E2E-053 | FE+BE |
| TC-FA-COA-197 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-198 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-199 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-200 | TC-FA-COA-E2E-058 | FE+BE |
| TC-FA-COA-201 | TC-FA-COA-E2E-058 | FE+BE |
| TC-FA-COA-202 | TC-FA-COA-E2E-059 | FE+BE |
| TC-FA-COA-203 | TC-FA-COA-E2E-093 | FE+BE |
| TC-FA-COA-204 | TC-FA-COA-E2E-059 | FE+BE |
| TC-FA-COA-205 | TC-FA-COA-E2E-059 | FE+BE |
| TC-FA-COA-206 | TC-FA-COA-E2E-061 | FE+BE |
| TC-FA-COA-207 | TC-FA-COA-E2E-061 | FE+BE |
| TC-FA-COA-208 | TC-FA-COA-E2E-061 | FE+BE |
| TC-FA-COA-209 | TC-FA-COA-E2E-062 | FE+BE |
| TC-FA-COA-210 | TC-FA-COA-E2E-062 | FE+BE |
| TC-FA-COA-211 | TC-FA-COA-E2E-062 | FE+BE |
| TC-FA-COA-212 | TC-FA-COA-E2E-062 | FE+BE |
| TC-FA-COA-213 | TC-FA-COA-E2E-061 | FE+BE |
| TC-FA-COA-214 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-215 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-216 | TC-FA-COA-E2E-060 | FE+BE |
| TC-FA-COA-217 | TC-FA-COA-E2E-060 | FE+BE |
| TC-FA-COA-218 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-219 | TC-FA-COA-E2E-060 | FE+BE |
| TC-FA-COA-220 | TC-FA-COA-E2E-046 | FE+BE |
| TC-FA-COA-221 | TC-FA-COA-E2E-056 | FE+BE |
| TC-FA-COA-222 | TC-FA-COA-E2E-056 | FE+BE |
| TC-FA-COA-223 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-224 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-225 | TC-FA-COA-E2E-048 | FE+BE |
| TC-FA-COA-226 | TC-FA-COA-E2E-048 | FE+BE |
| TC-FA-COA-227 | TC-FA-COA-E2E-048 | FE+BE |
| TC-FA-COA-228 | TC-FA-COA-E2E-048 | FE+BE |
| TC-FA-COA-229 | TC-FA-COA-E2E-041 | FE+BE |
| TC-FA-COA-230 | TC-FA-COA-E2E-058 | FE+BE |
| TC-FA-COA-231 | TC-FA-COA-E2E-049 | FE+BE |
| TC-FA-COA-232 | TC-FA-COA-E2E-049 | FE+BE |
| TC-FA-COA-233 | TC-FA-COA-E2E-049 | FE+BE |
| TC-FA-COA-234 | TC-FA-COA-E2E-049 | FE+BE |
| TC-FA-COA-235 | TC-FA-COA-E2E-063 | FE+BE |
| TC-FA-COA-236 | TC-FA-COA-E2E-018 | FE+BE |
| TC-FA-COA-237 | TC-FA-COA-E2E-018 | FE+BE |
| TC-FA-COA-238 | TC-FA-COA-E2E-018 | FE+BE |
| TC-FA-COA-239 | TC-FA-COA-E2E-018 | FE+BE |
| TC-FA-COA-240 | TC-FA-COA-E2E-019 | FE+BE |
| TC-FA-COA-241 | TC-FA-COA-E2E-018 | FE+BE |
| TC-FA-COA-242 | TC-FA-COA-E2E-019 | FE+BE |
| TC-FA-COA-243 | TC-FA-COA-E2E-019 | FE+BE |
| TC-FA-COA-244 | TC-FA-COA-E2E-019 | FE+BE |
| TC-FA-COA-245 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-246 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-247 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-248 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-249 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-250 | TC-FA-COA-E2E-024 | FE+BE |
| TC-FA-COA-251 | TC-FA-COA-E2E-025 | FE+BE |
| TC-FA-COA-252 | TC-FA-COA-E2E-025 | FE+BE |
| TC-FA-COA-253 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-254 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-255 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-256 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-257 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-258 | TC-FA-COA-E2E-021 | FE+BE |
| TC-FA-COA-259 | TC-FA-COA-E2E-022 | FE+BE |
| TC-FA-COA-260 | TC-FA-COA-E2E-017 | FE+BE |
| TC-FA-COA-261 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-262 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-263 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-264 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-265 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-266 | TC-FA-COA-E2E-006 | FE+BE |
| TC-FA-COA-267 | TC-FA-COA-E2E-007 | FE+BE |
| TC-FA-COA-268 | TC-FA-COA-E2E-007 | FE+BE |
| TC-FA-COA-269 | TC-FA-COA-E2E-070, TC-FA-COA-E2E-095 | FE+BE |
| TC-FA-COA-270 | TC-FA-COA-E2E-070, TC-FA-COA-E2E-095 | FE+BE |
| TC-FA-COA-271 | TC-FA-COA-E2E-070, TC-FA-COA-E2E-095 | FE+BE |
| TC-FA-COA-272 | TC-FA-COA-E2E-072, TC-FA-COA-E2E-096 | FE+BE |
| TC-FA-COA-273 | TC-FA-COA-E2E-072, TC-FA-COA-E2E-097 | FE+BE |
| TC-FA-COA-274 | TC-FA-COA-E2E-072, TC-FA-COA-E2E-097 | FE+BE |
| TC-FA-COA-275 | TC-FA-COA-E2E-072, TC-FA-COA-E2E-097 | FE+BE |
| TC-FA-COA-276 | TC-FA-COA-E2E-081 | FE+BE |
| TC-FA-COA-277 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-278 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-279 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-280 | TC-FA-COA-E2E-079 | FE+BE |
| TC-FA-COA-281 | TC-FA-COA-E2E-094 | FE+BE |
| TC-FA-COA-282 | TC-FA-COA-E2E-080 | FE+BE |
| TC-FA-COA-283 | TC-FA-COA-E2E-023 | FE+BE |
| TC-FA-COA-284 | TC-FA-COA-E2E-039 | FE+BE |
| TC-FA-COA-285 | TC-FA-COA-E2E-026 | FE+BE |
| TC-FA-COA-286 | TC-FA-COA-E2E-027 | FE+BE |
| TC-FA-COA-287 | TC-FA-COA-E2E-037 | FE+BE |
| TC-FA-COA-288 | TC-FA-COA-E2E-057 | FE+BE |
| TC-FA-COA-289 | TC-FA-COA-E2E-086 | FE+BE |
| TC-FA-COA-290 | TC-FA-COA-E2E-023 | FE+BE |
| TC-FA-COA-291 | TC-FA-COA-E2E-003 | FE+BE |
| TC-FA-COA-292 | TC-FA-COA-E2E-003 | FE+BE |
| TC-FA-COA-293 | TC-FA-COA-E2E-030 | FE+BE |
| TC-FA-COA-294 | TC-FA-COA-E2E-030 | FE+BE |
| TC-FA-COA-295 | TC-FA-COA-E2E-088 | FE+BE |
| TC-FA-COA-296 | TC-FA-COA-E2E-030 | FE+BE |
| TC-FA-COA-297 | TC-FA-COA-E2E-088 | FE+BE |
| TC-FA-COA-298 | TC-FA-COA-E2E-028 | FE+BE |
| TC-FA-COA-299 | TC-FA-COA-E2E-029 | FE+BE |
| TC-FA-COA-300 | TC-FA-COA-E2E-069, TC-FA-COA-E2E-102 | FE+BE |
| TC-FA-COA-301 | TC-FA-COA-E2E-069, TC-FA-COA-E2E-102 | FE+BE |
| TC-FA-COA-302 | TC-FA-COA-E2E-066, TC-FA-COA-E2E-098 | FE+BE |
| TC-FA-COA-303 | TC-FA-COA-E2E-066, TC-FA-COA-E2E-101 | FE+BE |
| TC-FA-COA-304 | TC-FA-COA-E2E-067, TC-FA-COA-E2E-100 | FE+BE |
| TC-FA-COA-305 | TC-FA-COA-E2E-068, TC-FA-COA-E2E-099 | FE+BE |
| TC-FA-COA-306 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-307 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-308 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-309 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-310 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-311 | TC-FA-COA-E2E-054 | FE+BE |
| TC-FA-COA-312 | TC-FA-COA-E2E-054 | FE+BE |
| TC-FA-COA-313 | TC-FA-COA-E2E-054 | FE+BE |
| TC-FA-COA-314 | TC-FA-COA-E2E-054 | FE+BE |
| TC-FA-COA-315 | TC-FA-COA-E2E-054 | FE+BE |
| TC-FA-COA-316 | TC-FA-COA-E2E-041 | FE+BE |
| TC-FA-COA-317 | TC-FA-COA-E2E-041 | FE+BE |
| TC-FA-COA-318 | TC-FA-COA-E2E-041 | FE+BE |
| TC-FA-COA-319 | TC-FA-COA-E2E-041 | FE+BE |
| TC-FA-COA-320 | TC-FA-COA-E2E-040 | FE+BE |
| TC-FA-COA-321 | TC-FA-COA-E2E-058 | FE+BE |
| TC-FA-COA-322 | TC-FA-COA-E2E-042 | FE+BE |
| TC-FA-COA-323 | TC-FA-COA-E2E-043 | FE+BE |
| TC-FA-COA-324 | TC-FA-COA-E2E-043 | FE+BE |
| TC-FA-COA-325 | TC-FA-COA-E2E-047 | FE+BE |
| TC-FA-COA-326 | TC-FA-COA-E2E-047 | FE+BE |
| TC-FA-COA-327 | TC-FA-COA-E2E-047 | FE+BE |
| TC-FA-COA-328 | TC-FA-COA-E2E-050 | FE+BE |
| TC-FA-COA-329 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-330 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-331 | TC-FA-COA-E2E-044 | FE+BE |
| TC-FA-COA-332 | TC-FA-COA-E2E-052 | FE+BE |
| TC-FA-COA-333 | TC-FA-COA-E2E-052 | FE+BE |
| TC-FA-COA-334 | TC-FA-COA-E2E-055 | FE+BE |
| TC-FA-COA-335 | TC-FA-COA-E2E-060 | FE+BE |
| TC-FA-COA-336 | TC-FA-COA-E2E-060 | FE+BE |
| TC-FA-COA-337 | TC-FA-COA-E2E-009 | FE+BE |
| TC-FA-COA-338 | TC-FA-COA-E2E-010 | FE+BE |
| TC-FA-COA-339 | TC-FA-COA-E2E-010 | FE+BE |
| TC-FA-COA-340 | TC-FA-COA-E2E-009 | FE+BE |
| TC-FA-COA-341 | TC-FA-COA-E2E-009 | FE+BE |
| TC-FA-COA-342 | TC-FA-COA-E2E-010 | FE+BE |
| TC-FA-COA-343 | TC-FA-COA-E2E-087 | FE+BE |
| TC-FA-COA-344 | TC-FA-COA-E2E-012 | FE+BE |
| TC-FA-COA-345 | TC-FA-COA-E2E-012 | FE+BE |
| TC-FA-COA-346 | TC-FA-COA-E2E-078 | FE+BE |
| TC-FA-COA-347 | TC-FA-COA-E2E-078 | FE+BE |
| TC-FA-COA-348 | TC-FA-COA-E2E-078 | FE+BE |
| TC-FA-COA-349 | TC-FA-COA-E2E-075 | FE+BE |
| TC-FA-COA-350 | TC-FA-COA-E2E-028, TC-FA-COA-E2E-103 | FE+BE |
| TC-FA-COA-351 | TC-FA-COA-E2E-076 | FE+BE |
| TC-FA-COA-352 | TC-FA-COA-E2E-076 | FE+BE |
| TC-FA-COA-353 | TC-FA-COA-E2E-077 | FE+BE |
| TC-FA-COA-354 | TC-FA-COA-E2E-029 | FE+BE |
| TC-FA-COA-355 | TC-FA-COA-E2E-089 | FE+BE |
| TC-FA-COA-356 | TC-FA-COA-E2E-019 | FE+BE |
| TC-FA-COA-357 | TC-FA-COA-E2E-025 | FE+BE |
| TC-FA-COA-358 | TC-FA-COA-E2E-056 | FE+BE |
| TC-FA-COA-359 | TC-FA-COA-E2E-015 | FE+BE |
| TC-FA-COA-360 | TC-FA-COA-E2E-015 | FE+BE |
| TC-FA-COA-361 | TC-FA-COA-E2E-067, TC-FA-COA-E2E-100 | FE+BE |
| TC-FA-COA-362 | TC-FA-COA-E2E-069 | FE+BE |
| TC-FA-COA-363 | TC-FA-COA-E2E-085 | FE+BE |
| TC-FA-COA-364 | TC-FA-COA-E2E-085 | FE+BE |
| TC-FA-COA-365 | TC-FA-COA-E2E-023 | FE+BE |
| TC-FA-COA-366 | TC-FA-COA-E2E-012 | FE+BE |
| TC-FA-COA-367 | TC-FA-COA-E2E-084 | FE+BE |
