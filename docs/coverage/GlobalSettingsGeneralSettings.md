# Coverage E2E — Global Settings > General Settings

Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md` (183 TC, canonical; ID `TC-GS-GSET-01`–`183`, kontigu, seluruhnya aktif). Referensi kontrak: `global-settings/general-settings/PRD/general-settings.md`, `global-settings/general-settings/API/openapi.yaml`, dan `global-settings/general-settings/API/low-level-design.md`. Klasifikasi backend: `global-settings/general-settings/TestCases/tc-general-settings-backend.md` (namespace `TC-GS-GSET-BE-NNN`, 32 kasus kontrak API tanpa padanan di TC granular). Suite: `specs/GlobalSettings/GeneralSettings/`. Prefix: `GS` + `GSET` (`TC-GS-GSET-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 183 TC aktif masuk spec, 0 TC BE-only (tidak ada baris TC dengan `FE Test: -`; kasus direct-API TC-124 sampai TC-143 mengamati respons server dan state data sehingga tetap spec FE+BE, bagian 8b butir 1). Reconcile: 183 = 183 (spec) + 0 (BE-only). 54 spec, semuanya `Mode: FE+BE` (tidak ada `Mode: mock`; spec resilience 011, 020, 026 memakai `Spectra.intercept()` di atas backend nyata). Dua spec mobile (012, 013) berjalan di aplikasi Android dengan `coverage.mobile: automated`; 52 spec lain `coverage.web: automated`. Setiap TC terpetakan ke tepat satu spec. Dua alur dilebur karena permutasi data tanpa alur baru: TC-33 dan TC-183 di spec 014, TC-28 dan TC-36 di spec 015 (kedua id tetap di `sourceTc`, tiap Expected punya `Verifikasi` sendiri). Spec 053 dan 054 adalah hasil pemecahan spec 039 (79 langkah) dan 034 (54 langkah) atas persetujuan pengguna; id 034 dan 039 tidak diganti.

## TC granular → spec e2e

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-GSET-E2E-001-screening-halaman-nilai-tersimpan-dan-tooltip-info-label | Screening halaman, nilai tersimpan, tooltip ikon info | FE+BE | 37 | 1, 2, 6 |
| TC-GS-GSET-E2E-002-opsi-select-session-idle-timeout-date-format-dan-time-format | Opsi Select statis | FE+BE | 14 | 7, 8 |
| TC-GS-GSET-E2E-003-select-searchable-currency-time-zone-dan-keyboard-aria-live | Select Searchable + keyboard + aria-live | FE+BE | 29 | 9, 10, 13 |
| TC-GS-GSET-E2E-004-preview-currency-dan-date-time-update-langsung | Preview live | FE+BE | 23 | 30, 31, 32 |
| TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data | Entitas baru belum Save | FE+BE | 23 | 11, 12, 63, 178 |
| TC-GS-GSET-E2E-006-record-belum-ada-seed-default-dan-save-pertama | Record belum ada, Save pertama | FE+BE | 20 | 117 |
| TC-GS-GSET-E2E-007-role-matrix-visibilitas-elemen-total-control-dan-read-only | Role Matrix visibilitas (TC lalu RO) | FE+BE | 26 | 22, 23, 61 |
| TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | Role Matrix negatif | FE+BE | 16 | 24, 25, 26, 27 |
| TC-GS-GSET-E2E-009-guided-tooltip-konten-step-dan-navigasi | Guided Tooltip konten dan navigasi | FE+BE | 35 | 15, 16, 18 |
| TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan | Trigger, flag, penutupan | FE+BE | 36 | 14, 17, 146, 147 |
| TC-GS-GSET-E2E-011-resilience-baca-loading-error-dan-try-again | Resilience baca halaman | FE+BE | 19 | 3, 4, 5 |
| TC-GS-GSET-E2E-012-mobile-screening-bottom-sheet-tooltip-ketuk-dan-read-only | Mobile screening, bottom sheet, tooltip ketuk, Read Only | FE+BE | 31 | 19, 20, 21 |
| TC-GS-GSET-E2E-013-mobile-dialog-unsaved-changes-dan-change-currency | Mobile dialog | FE+BE | 22 | 148, 149 |
| TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field | Save per Field Date & Time: Time Zone (UTC), Date Format, dan Time Format | FE+BE | 39 | 33, 34, 35, 183 |
| TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda | Save Session Idle Timeout: Sukses, State Saving, dan Klik Ganda pada Save | FE+BE | 33 | 28, 36, 44, 45 |
| TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | Dialog Change Currency: Screening, Backdrop, Esc, Cancel, dan Revert Tanpa Menyimpan | FE+BE | 35 | 37, 39, 40, 42, 115 |
| TC-GS-GSET-E2E-017-save-currency-konfirmasi-multi-field-dan-tanpa-perubahan-currency | Save dengan Konfirmasi Change Currency, Multi Field, dan Save Tanpa Perubahan Currency | FE+BE | 29 | 38, 41, 43 |
| TC-GS-GSET-E2E-018-dialog-unsaved-changes-cancel-leave-esc-dan-backdrop | Dialog Unsaved Changes: Cancel, Leave, Esc, dan Klik Backdrop | FE+BE | 22 | 49, 50, 116 |
| TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | Button Save dan Navigasi Tanpa Dialog Unsaved Changes: Tanpa Perubahan, Revert, Reload, dan Setelah Save | FE+BE | 25 | 29, 51, 52, 53, 114 |
| TC-GS-GSET-E2E-020-resilience-save-5xx-timeout-dan-currency-gagal | Resilience Save: Gagal 5xx, Timeout, dan Gagal Setelah Konfirmasi Change Currency | FE+BE | 34 | 46, 47, 48 |
| TC-GS-GSET-E2E-021-state-tenant-save-ditolak-suspended-dan-expired | State Tenant: Save Ditolak saat Entitas Suspended dan Expired | FE+BE | 17 | 54, 55 |
| TC-GS-GSET-E2E-022-state-tenant-baca-saat-suspended | State Tenant: Halaman General Settings Tetap Dapat Dibaca saat Entitas Suspended | FE+BE | 4 | 56 |
| TC-GS-GSET-E2E-023-state-tenant-general-settings-identik-di-semua-plan | State Tenant: General Settings Tersedia dan Identik di Semua Plan Tanpa Gating | FE+BE | 32 | 123 |
| TC-GS-GSET-E2E-024-session-idle-timeout-tidak-retroaktif-dan-sesi-baru | Session Idle Timeout: Tidak Retroaktif pada Sesi Berjalan dan Berlaku pada Sesi Baru | FE+BE | 17 | 57, 58 |
| TC-GS-GSET-E2E-025-multi-konteks-kebijakan-satu-sesi-web | Multi-Konteks: Session Idle Timeout Tidak Mengubah Kebijakan Satu Sesi Web per Akun | FE+BE | 8 | 59 |
| TC-GS-GSET-E2E-026-resilience-changelog-loading-error-load-dan-download-gagal | Resilience Modal Changelog: Loading, Error Load, Try Again, dan Download Gagal | FE+BE | 20 | 62, 64, 101 |
| TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | Modal Changelog: Screening, Urutan Default, Tooltip, Klik Backdrop, dan Fokus Keyboard | FE+BE | 28 | 60, 65, 85, 86, 96 |
| TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | Modal Changelog: Search, Interaksi Kotak Search, Kolom Searchable, dan Kolom Hidden | FE+BE | 47 | 66, 67, 68, 69, 70 |
| TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | Modal Changelog: Screening Filter Panel dan Opsi Dropdown Filter Dinamis dari Data Tabel | FE+BE | 36 | 71, 72, 75, 150, 174 |
| TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | Modal Changelog: Filter Apply berdasarkan Field, Modified By, Rentang Date, dan Kombinasi | FE+BE | 31 | 73, 74, 76, 77, 78 |
| TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | Modal Changelog: Chip Filter, Overflow +N more, Pencarian Dropdown, dan Indikator Loading Dropdown | FE+BE | 43 | 79, 80, 175, 176, 177 |
| TC-GS-GSET-E2E-032-changelog-filter-clear-field-tutup-tanpa-apply-dan-kolom-hidden | Modal Changelog: Clear Field Tidak Melepas Search, Tutup Filter Tanpa Apply, dan Filter Independen dari Kolom Hidden | FE+BE | 25 | 81, 158, 179 |
| TC-GS-GSET-E2E-033-changelog-sorting-3-state-dan-header-actions | Modal Changelog: Sorting 3-State Kolom Date dan Kolom Teks serta Header Actions Tanpa Ikon Sort | FE+BE | 25 | 82, 83, 160 |
| TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal | Changelog General Settings: Panel Column Visibility, Setup Column Screening, Pencarian Kolom, dan Tutup Tanpa Simpan | FE+BE | 36 | 84, 87, 89, 94 |
| TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save | Changelog General Settings: Setup Column Pin/Unpin, Hide/Unhide, Reorder, dan Reset to Default dengan Save | FE+BE | 43 | 88, 90, 91, 93 |
| TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | Download Changelog General Settings: Overlay, Nama Berkas, dan Isi Berkas CSV dan XLSX | FE+BE | 32 | 97, 98, 99, 100, 159 |
| TC-GS-GSET-E2E-037-changelog-pagination-page-size-dan-nomor-halaman | Changelog General Settings: Pagination, Page Size, Navigasi Halaman, dan Input Nomor Halaman | FE+BE | 22 | 102, 180 |
| TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size | Changelog General Settings: Kombinasi Search, Filter, Sort, dan Page Size | FE+BE | 52 | 151, 152, 153, 154 |
| TC-GS-GSET-E2E-039-changelog-kombinasi-lanjutan-tanpa-hasil-reset-halaman-dan-buka-ulang | Changelog General Settings: Kombinasi Lanjutan, Tanpa Hasil, dan Reset Halaman ke Halaman 1 | FE+BE | 35 | 155, 156, 157 |
| TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone | Changelog General Settings: Kolom Date Mengikuti Format dan Time Zone, Hover Modified By, dan Old/New Value Time Zone Utuh | FE+BE | 43 | 103, 161, 162, 163 |
| TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | Log per field | FE+BE | 25 | 104, 105, 106, 107, 108 |
| TC-GS-GSET-E2E-042-pencatatan-changelog-dan-activity-log-multi-field-snapshot-dan-tanpa-perubahan | Log multi-field | FE+BE | 41 | 109, 111, 112 |
| TC-GS-GSET-E2E-043-absence-log-currency-symbol-dan-system-log-detail-user | Absence log | FE+BE | 32 | 110, 113 |
| TC-GS-GSET-E2E-044-multi-konteks-propagasi-sse-ke-tab-lain | SSE multi-tab | FE+BE | 29 | 118, 119, 120 |
| TC-GS-GSET-E2E-045-multi-konteks-konkurensi-dua-admin-last-write-wins | Dua admin | FE+BE | 14 | 145 |
| TC-GS-GSET-E2E-046-multi-konteks-isolasi-dua-tenant | Dua tenant | FE+BE | 9 | 121, 144 |
| TC-GS-GSET-E2E-047-lintas-modul-timestamp-mengikuti-entitas-staff-yang-login | Timestamp lintas produk | FE+BE | 5 | 122 |
| TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | Direct API RBAC | FE+BE | 15 | 124, 125, 126, 127, 128, 129, 130 |
| TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | PUT simbol, no-op, 422 A | FE+BE | 30 | 131, 132, 133, 134, 135, 136, 137 |
| TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | PUT 422 B | FE+BE | 14 | 138, 139, 140, 141, 142, 143 |
| TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone | Bypass DOM A | FE+BE | 19 | 164, 165, 166, 167 |
| TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | Bypass DOM B | FE+BE | 9 | 168, 169, 170, 171, 172, 173 |
| TC-GS-GSET-E2E-053-changelog-retensi-saringan-antar-halaman-dan-buka-ulang-kondisi-default | Changelog General Settings: Retensi Search, Filter, dan Sort Antar Halaman serta Modal Dibuka Kembali Tampil Kondisi Default | FE+BE | 45 | 181, 182 |
| TC-GS-GSET-E2E-054-changelog-setup-column-kolom-visible-terakhir-dan-reset-to-default-belum-disimpan | Changelog General Settings: Setup Column Kolom Visible Terakhir dan Hasil Reset to Default yang Belum Disimpan Dibuang | FE+BE | 19 | 92, 95 |

Kolom Langkah adalah jumlah baris langkah bernomor di `## Test Steps` (cara hitung `scripts/check-suite.py`). Spec dengan langkah berulang per baris tabel Prerequisites (007, 012, 033, 041, 048, 049, 050, 051, 052) lebih panjang bila ekspansi dihitung; angkanya ada di bagian "Temuan yang masih terbuka".

## Pembagian TC lintas spec

- **TC-GS-GSET-33 dan 183** (Save Time Zone) dilebur menjadi satu alur di spec `014` (Time Zone `UTC`); baris Changelog Time Zone diasersi lewat Expected e TC-183 dengan baseline jumlah sebelum aksi. **TC-GS-GSET-28 dan 36** dilebur di spec `015`.
- **Alias "Time Zone Lain"** (TC-33, 43, 74, 79, 80, 103, 105, 163 dan lainnya) dipetakan ke `UTC`, satu-satunya opsi selain `Asia/Jakarta` yang labelnya dikunci PRD §4.3a (`(UTC+00:00) UTC, Reykjavik, Accra`). Alias `teks label opsi USD`/`EUR` dibaca dari dropdown saat memilih.
- **TC-GS-GSET-124 sampai 130** (direct API RBAC) di spec `048`; TC-131 sampai 137 di `049`; TC-138 sampai 143 di `050`. Aktor RO, SR, CI diamati lewat respons dan GET dengan token Total Control, bukan lewat sesi UI mereka (sesuai langkah 2 TC-125 dan TC-126).
- **TC-GS-GSET-46** (Expected c): nilai server dibaca lewat GET API di spec `020`, sesuai langkah 5 TC.
- **Asersi absence** (TC-110, 112, 113 dan butir "tanpa log" di spec lain): hanya TC-110 dan TC-113 di spec absence `043` dengan aksi dan baseline sendiri; TC-111 dan TC-112 di spec `042` (Save disabled sehingga tanpa request) dengan baseline jumlah entri; TC-132 di spec `049` hanya mengasersi respons 200 dan jumlah baris log.
- **Seeding Changelog**: spec Changelog (026 sampai 040, 053, 054) men-seed baris lewat PUT API di `before`; spec 036 mensyaratkan sedikitnya 11 baris, spec 037 sedikitnya 26 baris, spec 039 dan 053 sedikitnya 11 baris (17 baris dua aktor; 053 menyalin seeding 039 beserta jeda menit untuk TC-182).
- **Entitas non-Client A**: Client Baru dan Client Negara Lain (spec 005), Client Tanpa Record (006), Client Suspended (021, 022, 048), Client Expired (021), Client Starter/Growth/Professional/Enterprise (023), Client Satu Riwayat (029), Client Lain (046), PT Maju Bersama dan PT Sentosa Abadi (047).

## Kebutuhan lingkungan (tim FE)

- Env var password yang dipakai spec dan sudah terdaftar di `.env.example` dan `spectra.config.ts`: `GS_TC_PASSWORD` (Total Control Client A, Budi Santoso). `GS_RO_PASSWORD` dan `GS_NOCAP_PASSWORD` sudah ada di `.env.example` tetapi merujuk akun suite lain (`readOnly_automated_qaTeam1`, `noCapability_automated_qaTeam1`), bukan akun Pre-setup GSET No 3 dan No 5; spec GSET tidak memakainya (satu nama env var, satu arti).
- Env var password baru yang belum terdaftar di `spectra.config.ts` dan `.env.example` (ditunda ke tahap script, keputusan D-05; nilai diisi tim FE):

  | Env var | Akun | Spec |
  |---|---|---|
  | `GS_TCB_PASSWORD` | Total Control kedua Client A, Andi Wijaya (`Andi W`, Pre-setup No 2, `totalControlGlobalSettingsB_automated_{namaCompany}`) | 024, 028, 030, 031, 033, 038, 039, 044, 045, 053 |
  | `GS_GSET_RO_PASSWORD` | Read Only (Pre-setup No 3, `readOnlyGlobalSettings_automated_{namaCompany}`) | 007, 012, 048 |
  | `GS_GSET_SR_PASSWORD` | System Role (Pre-setup No 5, `noCapabilityGlobalSettings_automated_{namaCompany}`) | 008, 048 |
  | `GS_GSET_CI_PASSWORD` | Capability Individual (Pre-setup No 4, `manageUserRoleRead_automated_{namaCompany}`) | 008, 048 |
  | `GS_NEWCLIENT_TC_PASSWORD` | Total Control staf Client Baru (No 14) | 005 |
  | `GS_OTHERCOUNTRY_TC_PASSWORD` | Total Control staf Client Negara Lain (No 15) | 005 |
  | `GS_NORECORD_TC_PASSWORD` | Total Control staf Client Tanpa Record (No 24) | 006 |
  | `GS_SUSPENDED_TC_PASSWORD` | Total Control staf Client Suspended (No 16) | 021, 022, 048 |
  | `GS_EXPIRED_TC_PASSWORD` | Total Control staf Client Expired (No 17) | 021 |
  | `GS_STARTER_TC_PASSWORD`, `GS_GROWTH_TC_PASSWORD`, `GS_PROFESSIONAL_TC_PASSWORD`, `GS_ENTERPRISE_TC_PASSWORD` | Total Control staf Client Starter/Growth/Professional/Enterprise (No 20 sampai 23) | 023 |
  | `GS_ONEHIST_TC_PASSWORD`, `GS_ONEHIST_TCB_PASSWORD` | Total Control Budi Santoso dan Andi Wijaya pada Client Satu Riwayat (No 25) | 029 |
  | `GS_CLIENTLAIN_TC_PASSWORD` | Total Control staf Client Lain (No 18) | 046 |
  | `GS_MAJU_TC_PASSWORD`, `GS_SENTOSA_TC_PASSWORD` | Total Control staf PT Maju Bersama (No 6) dan PT Sentosa Abadi (No 7) | 047 |

  Harmonisasi lintas spec (satu env var, satu arti): nama password Read Only disatukan menjadi `GS_GSET_RO_PASSWORD` (spec 007 dan 012 semula `GS_RO_PASSWORD`), System Role `GS_GSET_SR_PASSWORD` dan Capability Individual `GS_GSET_CI_PASSWORD` (spec 008 semula `GS_NOCAP_PASSWORD` dan `GS_USERROLEREAD_PASSWORD`), Client Suspended `GS_SUSPENDED_TC_PASSWORD` (spec 048 semula `GS_CLIENTSUSP_TC_PASSWORD`). Email akun staf entitas di atas tidak tertulis di Pre-setup TC dan "disediakan tim FE".
- Fixture baru yang belum ada: `fixtures/generalSettings.json` (`pageUrl`, `payloadBaseline`, `payloadIdle60`, `payloadIdle60TzUtc`, `payloadIdle60TzUtcDateMdy`, `payloadIdle120DateMdy`, `payloadIdle120TzUtcDateMdy`, `payloadTimeFormat12h`, `payloadTzJakarta`, `payloadAllFieldsChanged`, `totalControl`, `totalControlB`); spec yang memakainya menandai "fixture belum ada" (001, 002, 005, 006, 008, 026 sampai 040, 053, 054).
- Kemampuan teknis yang belum terdaftar dan disediakan tim FE/BE (tanpa endpoint karangan, S-13): membaca dan menyetel/menghapus flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` per akun; klien HTTP dengan penangkapan token sesi API (PUT/GET `/v2/enterprise-management/general-settings`, daftar Changelog `/v2/analytics-reporting/change-logs/list`, `/options`, `/export` dengan path mengikuti `global-settings/activity-log/API/openapi.yaml` dan perlu dikonfirmasi); intercept jaringan (tahan respons, 500, timeout, penghitung request); penanganan konfirmasi bawaan browser `beforeunload` (konfirmasi otomatis; batalkan di spec 019); mengatur jam server absolut dan jam browser bersama (spec 024); dua konteks browser paralel dan dua tab (025, 044, 045, 046); penghapusan record General Settings lewat database oleh tim BE (006); pengembalian entitas ke keadaan awal (Client Baru, Client Negara Lain, Client Tanpa Record, Client Satu Riwayat); status Client Suspended/Expired dan plan tier yang sudah berlaku di environment (021 sampai 023); membaca pesan SSE yang diterima halaman (046); membaca timestamp UTC sumber di Client List dan FAMS (047); menangkap dan membaca berkas unduhan CSV/XLSX serta total entri Changelog (036); membaca dan menghapus preferensi kolom di penyimpanan browser (028, 032, 034, 035, 036, 054); mengubah lebar viewport dan drag-and-drop (010, 031, 035); injeksi nilai langsung ke elemen Select lewat DOM (051, 052); perangkat atau emulator Android bersama (012, 013).
- Environment automation harus terisolasi dari aktivitas pengguna lain agar asersi himpunan (opsi filter Modified By, baseline jumlah entri) stabil, dan suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_gs-general-settings`, baseline record Client A (Pre-setup No 10), dan `beforeEach` pembuka halaman diatur sekali di hook suite (`suite.md`, bagian Hook suite); spec 009, 010, 012, 013 mengatur flag sendiri, dan `beforeEach` tidak membuka General Settings untuk spec 008, 022, 023, 047.

## Temuan yang masih terbuka

Ringkasan di bawah ini dikumpulkan dari `## Notes` ("Temuan untuk QA") tiap spec. Satu-satunya butir yang masih terbuka adalah keputusan ukuran spec (bagian pertama). Temuan Q-01, 02, 03, 04, 05, 07, dan 11 sudah diselesaikan (bagian "Temuan yang sudah diselesaikan"); Q-06, 08, dan 10 adalah kemampuan atau prasyarat tim FE/BE dan Q-09 keputusan programmer, bukan temuan terbuka. Butir lain adalah catatan QA non-blocking.

### Ukuran spec (keputusan terbuka)

Spec berikut melewati batas ±35 langkah dengan satu kelas harness dan alasan tertulis di Notes (jumlah nominal; ekspansi baris berulang disebut di kurung): 038 (52), 028 (47), 053 (45), 031 (43), 035 (43), 040 (43), 007 (26; 46 dengan ekspansi), 012 (31; 40 dengan ekspansi), 001 (37), 041 (25; 58 dengan ekspansi, 40 langkah baca-log berpola), 042 (41, termasuk 18 langkah baca-log berpola), 048 (15; 33 dengan ekspansi), 051 (19; 36 dengan ekspansi), 014 (39), 010 (36), 029 (36), 034 (36), 033 (25; 43 dengan ekspansi), 049 (30; 50 dengan ekspansi), 050 (14; 49 dengan ekspansi), 052 (9; 49 dengan ekspansi). Pemecahan spec 039 (79 langkah) menjadi 039 (35) dan 053 (45), serta spec 034 (54 langkah) menjadi 034 (36) dan 054 (19), dilakukan atas persetujuan pengguna (progress tahap e2e-generate-spec, Approval 2). Alasan potongan: 053 membawa blok TC-181 dan TC-182 (reset halaman dan buka ulang modal) dengan seeding dan hook salinan 039; 054 membawa blok TC-92 dan TC-95 karena keduanya membuka Modal Setup Column sendiri, sedangkan TC-94 melanjutkan modal dari blok TC-87 sehingga tetap di 034. Sisa 053 (45) dan 034 (36) melewati ±35 langkah dengan alasan di Notes masing-masing (TC-181 memverifikasi tiga kondisi pada dua halaman; 034 tanpa ekspansi dan satu kelas harness).

### Akun, entitas, dan mekanisme yang tidak didefinisikan sumber (prasyarat tim FE/BE dan catatan QA non-blocking)

- **Akun di luar Pre-setup**: email staf Client Baru dan Client Negara Lain (TC-11, 12, 63, 178), Client Tanpa Record (TC-117), Client Suspended dan Client Expired (TC-54, 55, 56, 130), Client Starter/Growth/Professional/Enterprise (TC-123), Budi Santoso di Client Satu Riwayat (TC-72, 75, 150, 174), Client Lain (TC-121, 144), PT Maju Bersama dan PT Sentosa Abadi (TC-122), nama user Read Only (TC-20, 21, 23, 61), dan Total Control baru tanpa flag Pre-setup No 8 (TC-14 sampai 18, 146, 147; spec memakai akun No 1 dengan flag dihapus). Email SR Pre-setup No 5 berbeda dari akun yang dikaitkan `GS_NOCAP_PASSWORD` di `.env.example` (TC-24 sampai 27).
- **Reset entitas ke keadaan awal (Q-06; kemampuan tim FE/BE, tercatat di Prerequisites spec terkait)**: Client Satu Riwayat harus tepat satu baris (TC-72, 75, 150, 174) tetapi TC-150 menambah baris sehingga run kedua gagal tanpa pengembalian; hal yang sama untuk Client Baru (TC-11, 63, 178) dan Client Tanpa Record (TC-117, termasuk "1 baris" Expected d yang tidak bisa diasersi sebagai angka absolut karena audit trail permanen, S-12).
- **Flag Guided Tooltip (Q-10; kemampuan tim FE/BE, tercatat di Prerequisites spec terkait)**: mekanisme menghapus/membaca flag tidak ada di TC, PRD, atau LLD (TC-14 sampai 18, 146, 147). TC-18 langkah 2 ("→ (atau Enter)") ambigu; TC-147 tidak menyebut ukuran viewport (spec memakai 1280 px ke 1024 px, data uji); TC-14 langkah 4 tidak menyebut menu tujuan (spec memakai Global Settings > Activity Log).
- **Pelaku perubahan status/plan** (TC-54, 55, 56, 123) tidak disebut; precondition record baseline entitas tidak ditulis (TC-56, 123).
- **Manipulasi jam dan sesi (Q-08; kemampuan tim FE/BE, tercatat di Prerequisites spec terkait)**: cara membaca waktu terbit/aktivitas terakhir sesi dan mengatur jam server tidak didefinisikan (TC-57, 58); tombol pada Dialog Session Expired tidak disebut; TC-58 tidak menyebut 61 menit dihitung dari login atau dari aktivitas terakhir. TC-52, 57, 58, 59, 117 bertanda `Manual Only` tetapi tetap spec.
- **Endpoint Modal Changelog**: list, options, dan export Modal Changelog General Settings tidak tertulis di `openapi.yaml`/`low-level-design.md` General Settings; path mengikuti kontrak Activity Log dan perlu dikonfirmasi (TC-62, 64, 101, 177). TC-64 menyebut `GET`, sedangkan kontrak list memakai `POST`.

### Temuan yang sudah diselesaikan dan catatan TC non-blocking

- **Diselesaikan, Q-01 (TC-125, 126)**: langkah 2 TC kini membaca nilai tersimpan lewat GET dengan token sesi Total Control (bukan sesi SR atau CI yang ditolak 403, TC-26 dan 27); precondition d menambah token itu. Spec 048 sesuai TC. Sisa non-blocking: TC-130 langkah 2 tidak menyebut akun pengamat (spec memakai GET dari staf `Client Suspended`).
- **Diselesaikan, Q-02 (TC-46)**: langkah 5 dan Expected c TC kini membaca nilai tersimpan lewat GET (state server), tanpa tab kedua. Spec 020 sesuai TC.
- **Diselesaikan, Q-03 (TC-118)**: surface konsumen di Admin Console adalah Client List, kolom Last Updated (konsisten dengan TC-122). Spec 044 sesuai TC. Sisa non-blocking: TC-119 aksi di tab 2 dan tampilan "sesi tetap aktif" tidak disebut; "tidak di-reset" untuk timer idle tidak punya cara observasi. TC-120: spec memakai sesi API Admin B karena hasil di sesi itu tidak diasersi.
- **Diselesaikan, Q-04 (TC-163)**: Time Zone tujuan adalah `UTC` (selisih tetap 7 jam dari `Asia/Jakarta`); Expected menyatakan tanggal dan jam baris sesudah Save = nilai sebelum Save dikurangi 7 jam, tanpa percabangan. Spec 040 sesuai TC. Sisa non-blocking: Post Condition (baris `Time Zone` di Changelog) tanpa langkah observasi; cara memilih baris bila ada beberapa tidak disebut. TC-162 langkah 1 bergantung pada baris dari TC lain (spec 040 membuat baris itu sendiri, S-04). TC-103: tanggal uji dapat berbulan/berhari dua digit sehingga "tanpa nol di depan" tidak terbukti; label opsi Date/Time Format tidak disebut.
- **Diselesaikan, Q-05 (TC-59)**: judul kini hanya sesi web; langkah 2 memilih `Confirm` pada Dialog Confirmation Duplicate Login Attempt; Expected: Dialog Logged Out muncul di browser 1 (`auth-foundation.md` §6 menetapkan Dialog Logged Out untuk sesi lama pada Duplicate Login Attempt; Dialog Session Expired di §7 adalah untuk idle timeout). Spec 025 sesuai TC. Sisa non-blocking: aktor penyimpan Session Idle Timeout `1 hour` tidak disebut.
- **Diselesaikan, Q-07 (TC-132)**: Expected a kini hanya response 200 (tanpa asersi toast UI); spec 049 sesuai TC. Sisa non-blocking: TC-131 memakai properti `placement` yang tidak ada di `PutGeneralSettingsBody`. TC-133 sampai 137 dan 138, 140, 142 tidak menyebut bentuk nilai "kosong" (spec: string kosong `""`; `null` untuk TC-142). TC-137 bergantung pada NC-05 (hanya opsi kurasi diterima server) sedangkan LLD menyebut semua IANA valid. TC-143 memberi satu pesan untuk tiga nilai (`45`, `0`, `"Never"`) dan `"Never"` (string) dapat ditolak dengan pesan tipe data berbeda.
- **TC-01**: Expected menulis kunci `Asia/Jakarta`/`IDR` sedangkan yang tampil adalah label opsi (PRD §4.3a); "Button Save berwarna success (hijau)" tanpa cara mengamati warna.
- **TC-60, 66, 67, 69, 74, 77, 80, 81, 85, 96**: Search/Filter/Tooltip: placeholder Search hanya terlihat sesudah icon Search diklik (TC-60); TC-66 langkah 8 dan TC-67/74 tanpa baris pembanding (spec men-seed baris Field `Date Format` sebagai penanda); TC-66 Expected f tidak dapat dibedakan dari keadaan sebelumnya; TC-69 Expected tanpa langkah observasi dan tanpa cara memperoleh teks tanggal; TC-77 b mengasumsikan rentang kemarin tanpa baris padahal Changelog audit trail permanen; TC-80 Expected a (pencarian `Time` menyempit ke `Time Zone` dan `Time Format`) tidak terpenuhi bila pencarian dropdown berbasis substring karena `Session Idle Timeout` ikut cocok; TC-81 (seluruh baris Action `Edit` sehingga keyword `Edit` tidak menyaring apa pun); TC-85 posisi tooltip tidak disebut; TC-96 jumlah tekan Tab tidak disebut.
- **TC-82, 83, 160**: TC-82 meminta indikator sort tetapi Expected hanya urutan; urutan nilai berawalan angka/kurung tidak disebut; TC-83 klik 2 dan klik 3 menghasilkan urutan sama (beda hanya indikator); cara membuktikan "Oldest First" bila sepuluh baris pertama bertanggal menit sama tidak disebut.
- **TC-84, 88, 92, 93, 94, 95**: TC-84 bentuk kontrol show/hide dan reorder tidak disebut; TC-88 lebar viewport scroll horizontal dan cara mengamati status pin tidak disebut; TC-92 kolom yang tersisa tidak disebut; TC-93 langkah 1 sudah terpenuhi bila dijalankan sesudah TC-91; TC-94/95 cara mengembalikan konfigurasi kolom tidak disebut.
- **TC-97 sampai 100, 159**: cara menangkap dan membaca berkas unduhan serta total entri tidak disebut; TC-98 memakai format default sehingga asersi tidak membedakan format yang diikuti; nilai kolom `Modified By` di berkas tidak disebut (hanya header yang diasersi); TC-101 tidak punya Expected untuk state modal sesudah gagal.
- **TC-102, 180, 151 sampai 157, 181, 182**: TC-102 langkah 4 (25, 50, 100) tanpa Expected dan cara mengenali halaman aktif tidak disebut; TC-180 posisi/label input nomor halaman tidak disebut; TC-151 sampai 154 tidak menyebut pelaku dan nilai yang menjamin lebih dari satu nilai Field/Modified By (spec men-seed delapan perubahan dua aktor; TC-152 butuh baris tambahan `30 minutes` ke `15 minutes` agar filter `hour` terbukti); TC-153 kriteria bila nilai Field sama tidak disebut; TC-156 butuh baris Field `Currency Code` agar opsi filter ada; TC-157/181 butuh sedikitnya 11 baris; TC-182 butuh jeda antar-Save agar dua Date berbeda.
- **TC-175 sampai 177, 179, 150, 174, 75**: TC-176 nilai N pada lebar 1280 px tidak disebut; TC-177 tidak menyebut apakah opsi di-fetch ulang tiap dropdown dibuka; TC-179 Expected b tidak menyebut apakah panel dibuka kembali; TC-150 menyebut Admin B menyimpan lewat UI sedangkan konvensi memakai sesi API, dan nilai awal Time Format Client Satu Riwayat tidak tertulis; TC-75 b dan TC-174 d bergantung pada urutan TC-150.
- **TC-28, 33 sampai 36, 38, 43, 149**: Post Condition (Changelog dan Activity Log mencatat perubahan, event `general_settings.updated`, konsumen format menampilkan nilai baru) tanpa langkah observasi di TC, sehingga tidak diasersi; TC-183 langkah 1 mencatat label opsi tanpa Expected; TC-43 Expected a "sekali" diasersi dengan dialog tidak muncul lagi sesudah `[Change Currency]`; TC-149 Post Condition tidak diasersi.
- **TC-37, 39, 42, 45, 47, 48, 49, 52, 53, 54, 55**: TC-37/42/45 butuh penghitung request (intercept) dan TC tidak menyebut caranya; TC-39 langkah 4 dan TC-48, 54, 55 memuat ulang halaman dengan form dirty sehingga muncul konfirmasi bawaan `beforeunload` yang tidak disebut TC (spec mengonfirmasi otomatis); TC-47 durasi timeout klien tidak disebut; TC-49 judul Dialog Unsaved Changes tidak disebut PRD (judul tidak diasersi); TC-52 "membatalkan reload" tanpa cara membatalkan; TC-53 "hingga toast sukses" tanpa Expected terpisah.
- **TC-03, 04, 08, 10, 13, 178**: TC-03/04 tidak menyebut endpoint (spec memakai GET `/v2/enterprise-management/general-settings`); TC-04 "bukan empty state" tanpa teks empty state halaman form; TC-08 langkah 2 ("Tutup") tanpa cara menutup dropdown (spec: `Esc`); TC-10 "salah satu nama kota di label" tanpa nama (spec: `Bangkok`, `Hanoi`); TC-13 atribut `aria-live` tanpa nilai (hanya keberadaan atribut diasersi); TC-178 Expected a dipecah menjadi satu `Verifikasi` setelah teks "No options available" (teks ini dirujuk ke `prd-conventions.md` §9.8, tidak ada di PRD modul).
- **TC-19 sampai 23, 61, 148**: TC-19 cara menutup bottom sheet tanpa memilih tidak disebut; TC-21 menyebut `Setup Column...` tanpa Panel Column Visibility (PRD §4.1 baris #4); TC-23 Expected f tooltip tanpa teks; TC-61 tanpa jumlah baris/nilai; TC-148 Expected c halaman tujuan setelah `[Leave]` tidak disebut.
- **Log, multi-konteks, dan role negatif (TC-104, 105, 109, 110, 113, 121, 122, 145, 26, 27)**: Modified By Activity Log `[nama aktor singkat]` diganti `Budi S` (TC-104, 105); TC-109 Expected a "tepat 3 baris baru" tanpa urutan dan Expected b tanpa Modified By (tidak diasersi); TC-110 Expected b bergantung pada opsi filter yang diisi dari data tabel (NC-18); TC-113 anchor tanpa kolom/nilai Action dan cara mengenali entri System Log (spec: Search `General Settings`); TC-145 Old Value baris Save kedua tidak disebut; TC-121 "tidak menerima event" tanpa cara mengamati dan Date Format awal Client Lain tidak disebut; TC-122 langkah 2 tidak menyebut halaman/kolom FAMS dan Time Zone `PT Sentosa Abadi` UTC+08:00 (Pre-setup No 19) bukan salah satu dari dua opsi PRD §4.3a (NC-09); TC-26/27 Expected "elemen halaman tidak ditampilkan" tanpa menyebut apa yang tampil selain toast 403.
- **TC-164 sampai 173**: "form tetap unsaved" tanpa elemen yang diamati (spec: tombol `[Save]` tetap aktif); TC-164/165 memuat langkah `[Change Currency]` sedangkan TC-166/167 tidak (konsisten `GSET-LOGIC-04a`); cara injeksi nilai ke komponen Select bergantung pada implementasi (disediakan tim FE); label opsi Date Format pada Expected memakai kode format.
- **Label opsi (Q-09; keputusan programmer, NC-09/NC-10)**: label opsi Currency (kecuali `IDR` = `Rp - Indonesian Rupiah`) dan opsi Time Zone (kecuali dua opsi PRD §4.3a) ditentukan programmer; spec membaca teks label dari dropdown saat memilih dan memakainya pada asersi berikutnya (TC-09, 30, 31, 32, 38, 43, 104, 105, 110, 175 dan lainnya).
- **Nilai bertanda `PRD?`** (TC-03, 44, 45, 58, 62, 103, 177): sudah disposisi di rencana (durasi tahan respons 5 detik adalah data uji, bukan aturan PRD; TC-45 "1 request" konsisten dengan double-submit guard; TC-58 margin 61/60 menit dihitung absolut; TC-103 "12 jam" konsisten dengan `hh:mm a`). Tidak ada nilai TC yang bertentangan dengan PRD.
- **Diselesaikan, Q-11**: baris `GSET` di `foundation/tc-prefix-registry.md` kini mencatat rentang `TC-GS-GSET-01`–`183` (183 TC) beserta satu entri changelog registry.
- **Untuk tahap berikut**: `spectra lint` tidak memvalidasi isi `sourceTc`; pengecekan TC-ke-spec dilakukan `scripts/check-suite.py` dan skill audit.

## Lapisan per TC

| TC | Spec | Mode |
|---|---|---|
| TC-GS-GSET-01 | TC-GS-GSET-E2E-001-screening-halaman-nilai-tersimpan-dan-tooltip-info-label | FE+BE |
| TC-GS-GSET-02 | TC-GS-GSET-E2E-001-screening-halaman-nilai-tersimpan-dan-tooltip-info-label | FE+BE |
| TC-GS-GSET-03 | TC-GS-GSET-E2E-011-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-GSET-04 | TC-GS-GSET-E2E-011-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-GSET-05 | TC-GS-GSET-E2E-011-resilience-baca-loading-error-dan-try-again | FE+BE |
| TC-GS-GSET-06 | TC-GS-GSET-E2E-001-screening-halaman-nilai-tersimpan-dan-tooltip-info-label | FE+BE |
| TC-GS-GSET-07 | TC-GS-GSET-E2E-002-opsi-select-session-idle-timeout-date-format-dan-time-format | FE+BE |
| TC-GS-GSET-08 | TC-GS-GSET-E2E-002-opsi-select-session-idle-timeout-date-format-dan-time-format | FE+BE |
| TC-GS-GSET-09 | TC-GS-GSET-E2E-003-select-searchable-currency-time-zone-dan-keyboard-aria-live | FE+BE |
| TC-GS-GSET-10 | TC-GS-GSET-E2E-003-select-searchable-currency-time-zone-dan-keyboard-aria-live | FE+BE |
| TC-GS-GSET-11 | TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data | FE+BE |
| TC-GS-GSET-12 | TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data | FE+BE |
| TC-GS-GSET-13 | TC-GS-GSET-E2E-003-select-searchable-currency-time-zone-dan-keyboard-aria-live | FE+BE |
| TC-GS-GSET-14 | TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan | FE+BE |
| TC-GS-GSET-15 | TC-GS-GSET-E2E-009-guided-tooltip-konten-step-dan-navigasi | FE+BE |
| TC-GS-GSET-16 | TC-GS-GSET-E2E-009-guided-tooltip-konten-step-dan-navigasi | FE+BE |
| TC-GS-GSET-17 | TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan | FE+BE |
| TC-GS-GSET-18 | TC-GS-GSET-E2E-009-guided-tooltip-konten-step-dan-navigasi | FE+BE |
| TC-GS-GSET-19 | TC-GS-GSET-E2E-012-mobile-screening-bottom-sheet-tooltip-ketuk-dan-read-only | FE+BE |
| TC-GS-GSET-20 | TC-GS-GSET-E2E-012-mobile-screening-bottom-sheet-tooltip-ketuk-dan-read-only | FE+BE |
| TC-GS-GSET-21 | TC-GS-GSET-E2E-012-mobile-screening-bottom-sheet-tooltip-ketuk-dan-read-only | FE+BE |
| TC-GS-GSET-22 | TC-GS-GSET-E2E-007-role-matrix-visibilitas-elemen-total-control-dan-read-only | FE+BE |
| TC-GS-GSET-23 | TC-GS-GSET-E2E-007-role-matrix-visibilitas-elemen-total-control-dan-read-only | FE+BE |
| TC-GS-GSET-24 | TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-25 | TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-26 | TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-27 | TC-GS-GSET-E2E-008-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-28 | TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-GSET-29 | TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | FE+BE |
| TC-GS-GSET-30 | TC-GS-GSET-E2E-004-preview-currency-dan-date-time-update-langsung | FE+BE |
| TC-GS-GSET-31 | TC-GS-GSET-E2E-004-preview-currency-dan-date-time-update-langsung | FE+BE |
| TC-GS-GSET-32 | TC-GS-GSET-E2E-004-preview-currency-dan-date-time-update-langsung | FE+BE |
| TC-GS-GSET-33 | TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field | FE+BE |
| TC-GS-GSET-34 | TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field | FE+BE |
| TC-GS-GSET-35 | TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field | FE+BE |
| TC-GS-GSET-36 | TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-GSET-37 | TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | FE+BE |
| TC-GS-GSET-38 | TC-GS-GSET-E2E-017-save-currency-konfirmasi-multi-field-dan-tanpa-perubahan-currency | FE+BE |
| TC-GS-GSET-39 | TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | FE+BE |
| TC-GS-GSET-40 | TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | FE+BE |
| TC-GS-GSET-41 | TC-GS-GSET-E2E-017-save-currency-konfirmasi-multi-field-dan-tanpa-perubahan-currency | FE+BE |
| TC-GS-GSET-42 | TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | FE+BE |
| TC-GS-GSET-43 | TC-GS-GSET-E2E-017-save-currency-konfirmasi-multi-field-dan-tanpa-perubahan-currency | FE+BE |
| TC-GS-GSET-44 | TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-GSET-45 | TC-GS-GSET-E2E-015-save-session-idle-timeout-sukses-saving-state-dan-klik-ganda | FE+BE |
| TC-GS-GSET-46 | TC-GS-GSET-E2E-020-resilience-save-5xx-timeout-dan-currency-gagal | FE+BE |
| TC-GS-GSET-47 | TC-GS-GSET-E2E-020-resilience-save-5xx-timeout-dan-currency-gagal | FE+BE |
| TC-GS-GSET-48 | TC-GS-GSET-E2E-020-resilience-save-5xx-timeout-dan-currency-gagal | FE+BE |
| TC-GS-GSET-49 | TC-GS-GSET-E2E-018-dialog-unsaved-changes-cancel-leave-esc-dan-backdrop | FE+BE |
| TC-GS-GSET-50 | TC-GS-GSET-E2E-018-dialog-unsaved-changes-cancel-leave-esc-dan-backdrop | FE+BE |
| TC-GS-GSET-51 | TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | FE+BE |
| TC-GS-GSET-52 | TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | FE+BE |
| TC-GS-GSET-53 | TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | FE+BE |
| TC-GS-GSET-54 | TC-GS-GSET-E2E-021-state-tenant-save-ditolak-suspended-dan-expired | FE+BE |
| TC-GS-GSET-55 | TC-GS-GSET-E2E-021-state-tenant-save-ditolak-suspended-dan-expired | FE+BE |
| TC-GS-GSET-56 | TC-GS-GSET-E2E-022-state-tenant-baca-saat-suspended | FE+BE |
| TC-GS-GSET-57 | TC-GS-GSET-E2E-024-session-idle-timeout-tidak-retroaktif-dan-sesi-baru | FE+BE |
| TC-GS-GSET-58 | TC-GS-GSET-E2E-024-session-idle-timeout-tidak-retroaktif-dan-sesi-baru | FE+BE |
| TC-GS-GSET-59 | TC-GS-GSET-E2E-025-multi-konteks-kebijakan-satu-sesi-web | FE+BE |
| TC-GS-GSET-60 | TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | FE+BE |
| TC-GS-GSET-61 | TC-GS-GSET-E2E-007-role-matrix-visibilitas-elemen-total-control-dan-read-only | FE+BE |
| TC-GS-GSET-62 | TC-GS-GSET-E2E-026-resilience-changelog-loading-error-load-dan-download-gagal | FE+BE |
| TC-GS-GSET-63 | TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data | FE+BE |
| TC-GS-GSET-64 | TC-GS-GSET-E2E-026-resilience-changelog-loading-error-load-dan-download-gagal | FE+BE |
| TC-GS-GSET-65 | TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | FE+BE |
| TC-GS-GSET-66 | TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-67 | TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-68 | TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-69 | TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-70 | TC-GS-GSET-E2E-028-changelog-search-interaksi-kolom-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-71 | TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | FE+BE |
| TC-GS-GSET-72 | TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | FE+BE |
| TC-GS-GSET-73 | TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | FE+BE |
| TC-GS-GSET-74 | TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | FE+BE |
| TC-GS-GSET-75 | TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | FE+BE |
| TC-GS-GSET-76 | TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | FE+BE |
| TC-GS-GSET-77 | TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | FE+BE |
| TC-GS-GSET-78 | TC-GS-GSET-E2E-030-changelog-filter-apply-field-modified-by-date-dan-kombinasi | FE+BE |
| TC-GS-GSET-79 | TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | FE+BE |
| TC-GS-GSET-80 | TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | FE+BE |
| TC-GS-GSET-81 | TC-GS-GSET-E2E-032-changelog-filter-clear-field-tutup-tanpa-apply-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-82 | TC-GS-GSET-E2E-033-changelog-sorting-3-state-dan-header-actions | FE+BE |
| TC-GS-GSET-83 | TC-GS-GSET-E2E-033-changelog-sorting-3-state-dan-header-actions | FE+BE |
| TC-GS-GSET-84 | TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal | FE+BE |
| TC-GS-GSET-85 | TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | FE+BE |
| TC-GS-GSET-86 | TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | FE+BE |
| TC-GS-GSET-87 | TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal | FE+BE |
| TC-GS-GSET-88 | TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save | FE+BE |
| TC-GS-GSET-89 | TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal | FE+BE |
| TC-GS-GSET-90 | TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save | FE+BE |
| TC-GS-GSET-91 | TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save | FE+BE |
| TC-GS-GSET-92 | TC-GS-GSET-E2E-054-changelog-setup-column-kolom-visible-terakhir-dan-reset-to-default-belum-disimpan | FE+BE |
| TC-GS-GSET-93 | TC-GS-GSET-E2E-035-changelog-setup-column-pin-hide-reorder-dan-reset-dengan-save | FE+BE |
| TC-GS-GSET-94 | TC-GS-GSET-E2E-034-changelog-column-visibility-dan-setup-column-screening-pencarian-batal | FE+BE |
| TC-GS-GSET-95 | TC-GS-GSET-E2E-054-changelog-setup-column-kolom-visible-terakhir-dan-reset-to-default-belum-disimpan | FE+BE |
| TC-GS-GSET-96 | TC-GS-GSET-E2E-027-changelog-screening-urutan-default-tooltip-backdrop-dan-fokus | FE+BE |
| TC-GS-GSET-97 | TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | FE+BE |
| TC-GS-GSET-98 | TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | FE+BE |
| TC-GS-GSET-99 | TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | FE+BE |
| TC-GS-GSET-100 | TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | FE+BE |
| TC-GS-GSET-101 | TC-GS-GSET-E2E-026-resilience-changelog-loading-error-load-dan-download-gagal | FE+BE |
| TC-GS-GSET-102 | TC-GS-GSET-E2E-037-changelog-pagination-page-size-dan-nomor-halaman | FE+BE |
| TC-GS-GSET-103 | TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone | FE+BE |
| TC-GS-GSET-104 | TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | FE+BE |
| TC-GS-GSET-105 | TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | FE+BE |
| TC-GS-GSET-106 | TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | FE+BE |
| TC-GS-GSET-107 | TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | FE+BE |
| TC-GS-GSET-108 | TC-GS-GSET-E2E-041-pencatatan-changelog-dan-activity-log-save-per-field | FE+BE |
| TC-GS-GSET-109 | TC-GS-GSET-E2E-042-pencatatan-changelog-dan-activity-log-multi-field-snapshot-dan-tanpa-perubahan | FE+BE |
| TC-GS-GSET-110 | TC-GS-GSET-E2E-043-absence-log-currency-symbol-dan-system-log-detail-user | FE+BE |
| TC-GS-GSET-111 | TC-GS-GSET-E2E-042-pencatatan-changelog-dan-activity-log-multi-field-snapshot-dan-tanpa-perubahan | FE+BE |
| TC-GS-GSET-112 | TC-GS-GSET-E2E-042-pencatatan-changelog-dan-activity-log-multi-field-snapshot-dan-tanpa-perubahan | FE+BE |
| TC-GS-GSET-113 | TC-GS-GSET-E2E-043-absence-log-currency-symbol-dan-system-log-detail-user | FE+BE |
| TC-GS-GSET-114 | TC-GS-GSET-E2E-019-navigasi-tanpa-dialog-unsaved-revert-beforeunload-dan-setelah-save | FE+BE |
| TC-GS-GSET-115 | TC-GS-GSET-E2E-016-dialog-change-currency-screening-cancel-esc-backdrop-dan-revert | FE+BE |
| TC-GS-GSET-116 | TC-GS-GSET-E2E-018-dialog-unsaved-changes-cancel-leave-esc-dan-backdrop | FE+BE |
| TC-GS-GSET-117 | TC-GS-GSET-E2E-006-record-belum-ada-seed-default-dan-save-pertama | FE+BE |
| TC-GS-GSET-118 | TC-GS-GSET-E2E-044-multi-konteks-propagasi-sse-ke-tab-lain | FE+BE |
| TC-GS-GSET-119 | TC-GS-GSET-E2E-044-multi-konteks-propagasi-sse-ke-tab-lain | FE+BE |
| TC-GS-GSET-120 | TC-GS-GSET-E2E-044-multi-konteks-propagasi-sse-ke-tab-lain | FE+BE |
| TC-GS-GSET-121 | TC-GS-GSET-E2E-046-multi-konteks-isolasi-dua-tenant | FE+BE |
| TC-GS-GSET-122 | TC-GS-GSET-E2E-047-lintas-modul-timestamp-mengikuti-entitas-staff-yang-login | FE+BE |
| TC-GS-GSET-123 | TC-GS-GSET-E2E-023-state-tenant-general-settings-identik-di-semua-plan | FE+BE |
| TC-GS-GSET-124 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-125 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-126 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-127 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-128 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-129 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-130 | TC-GS-GSET-E2E-048-defense-in-depth-rbac-put-dan-get-langsung | FE+BE |
| TC-GS-GSET-131 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-132 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-133 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-134 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-135 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-136 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-137 | TC-GS-GSET-E2E-049-defense-in-depth-put-simbol-no-op-dan-422-currency-time-zone | FE+BE |
| TC-GS-GSET-138 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-139 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-140 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-141 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-142 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-143 | TC-GS-GSET-E2E-050-defense-in-depth-put-422-date-format-time-format-dan-session-idle-timeout | FE+BE |
| TC-GS-GSET-144 | TC-GS-GSET-E2E-046-multi-konteks-isolasi-dua-tenant | FE+BE |
| TC-GS-GSET-145 | TC-GS-GSET-E2E-045-multi-konteks-konkurensi-dua-admin-last-write-wins | FE+BE |
| TC-GS-GSET-146 | TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan | FE+BE |
| TC-GS-GSET-147 | TC-GS-GSET-E2E-010-guided-tooltip-kunjungan-pertama-flag-seen-dan-penutupan-tanpa-simpan | FE+BE |
| TC-GS-GSET-148 | TC-GS-GSET-E2E-013-mobile-dialog-unsaved-changes-dan-change-currency | FE+BE |
| TC-GS-GSET-149 | TC-GS-GSET-E2E-013-mobile-dialog-unsaved-changes-dan-change-currency | FE+BE |
| TC-GS-GSET-150 | TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | FE+BE |
| TC-GS-GSET-151 | TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-152 | TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-153 | TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-154 | TC-GS-GSET-E2E-038-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-155 | TC-GS-GSET-E2E-039-changelog-kombinasi-lanjutan-tanpa-hasil-reset-halaman-dan-buka-ulang | FE+BE |
| TC-GS-GSET-156 | TC-GS-GSET-E2E-039-changelog-kombinasi-lanjutan-tanpa-hasil-reset-halaman-dan-buka-ulang | FE+BE |
| TC-GS-GSET-157 | TC-GS-GSET-E2E-039-changelog-kombinasi-lanjutan-tanpa-hasil-reset-halaman-dan-buka-ulang | FE+BE |
| TC-GS-GSET-158 | TC-GS-GSET-E2E-032-changelog-filter-clear-field-tutup-tanpa-apply-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-159 | TC-GS-GSET-E2E-036-changelog-download-overlay-nama-file-dan-isi-csv-xlsx | FE+BE |
| TC-GS-GSET-160 | TC-GS-GSET-E2E-033-changelog-sorting-3-state-dan-header-actions | FE+BE |
| TC-GS-GSET-161 | TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone | FE+BE |
| TC-GS-GSET-162 | TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone | FE+BE |
| TC-GS-GSET-163 | TC-GS-GSET-E2E-040-changelog-kolom-date-self-reference-hover-modified-by-dan-old-new-time-zone | FE+BE |
| TC-GS-GSET-164 | TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone | FE+BE |
| TC-GS-GSET-165 | TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone | FE+BE |
| TC-GS-GSET-166 | TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone | FE+BE |
| TC-GS-GSET-167 | TC-GS-GSET-E2E-051-defense-in-depth-bypass-client-error-inline-currency-dan-time-zone | FE+BE |
| TC-GS-GSET-168 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-169 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-170 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-171 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-172 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-173 | TC-GS-GSET-E2E-052-defense-in-depth-bypass-client-error-inline-date-time-format-dan-session-idle | FE+BE |
| TC-GS-GSET-174 | TC-GS-GSET-E2E-029-changelog-filter-panel-screening-dan-opsi-dinamis | FE+BE |
| TC-GS-GSET-175 | TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | FE+BE |
| TC-GS-GSET-176 | TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | FE+BE |
| TC-GS-GSET-177 | TC-GS-GSET-E2E-031-changelog-filter-chip-overflow-dan-dropdown | FE+BE |
| TC-GS-GSET-178 | TC-GS-GSET-E2E-005-entitas-baru-seed-default-changelog-kosong-dan-dropdown-tanpa-data | FE+BE |
| TC-GS-GSET-179 | TC-GS-GSET-E2E-032-changelog-filter-clear-field-tutup-tanpa-apply-dan-kolom-hidden | FE+BE |
| TC-GS-GSET-180 | TC-GS-GSET-E2E-037-changelog-pagination-page-size-dan-nomor-halaman | FE+BE |
| TC-GS-GSET-181 | TC-GS-GSET-E2E-053-changelog-retensi-saringan-antar-halaman-dan-buka-ulang-kondisi-default | FE+BE |
| TC-GS-GSET-182 | TC-GS-GSET-E2E-053-changelog-retensi-saringan-antar-halaman-dan-buka-ulang-kondisi-default | FE+BE |
| TC-GS-GSET-183 | TC-GS-GSET-E2E-014-save-time-zone-date-format-dan-time-format-per-field | FE+BE |

## TC hanya-BE yang dilewati

Tidak ada (0). Alasan: (1) tidak ada TC granular dengan `FE Test: -` atau `PIC FE: -`; (2) `tc-general-settings-backend.md` memakai ID `TC-GS-GSET-BE-NNN` (kontrak API: 401/503/400 header layanan, `/internal/general-settings`, kegagalan DB dan penulisan log, JSON rusak, urutan `error[]` multi-kesalahan) yang tidak memetakan ke ID granular dan tidak punya padanan di 183 TC; (3) TC-124 sampai TC-143 punya langkah dan Expected yang bisa diamati dari sisi FE/E2E (respons dan state tersimpan), sehingga tetap spec FE+BE (konvensi bagian 2 dan 8b butir 1).
