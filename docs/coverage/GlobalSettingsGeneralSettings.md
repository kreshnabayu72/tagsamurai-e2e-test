# Coverage E2E — Global Settings > General Settings

Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md` (canonical).
Referensi kontrak: `global-settings/general-settings/PRD/general-settings.md` dan `global-settings/general-settings/API/openapi.yaml`.
Klasifikasi backend: `global-settings/general-settings/TestCases/tc-general-settings-backend.md`.
Suite: `specs_dummy/GlobalSettings/GeneralSettings/`.
Prefix Modul: `GS` + `GSET` (`TC-GS-GSET-E2E-*`).
Status semua spec: `draft`, belum ada script (`web.test.ts`).

**Jumlah TC aktif di `tc-general-settings.md`: 182 baris (`TC-GS-GSET-01` s.d. `TC-GS-GSET-182`).**
Cakupan otomasi spec E2E: **100% (182 dari 182 TC masuk spec, 0 TC hanya-BE)**. Modul form
single-record ini tidak punya Section 6 (API Contract) dan tidak punya TC bertanda `FE Test: -`;
TC-FE merangkap, sehingga setiap TC menghasilkan spec. Total Spec E2E yang dihasilkan: **41 spec**.

---

## 1. Pemetaan TC Granular → Spec E2E (41 spec)

182 dari 182 TC aktif masuk spec. Setiap TC tercatat tepat satu kali pada satu spec.

| Spec | Isi / Judul | Mode | TC Sumber |
|---|---|:---:|---|
| TC-GS-GSET-E2E-001 | Screening halaman General Settings: header, body, footer | FE+BE | 01 |
| TC-GS-GSET-E2E-002 | State form: populated, seed default entitas baru, Time Zone default | FE+BE | 02, 11, 12 |
| TC-GS-GSET-E2E-003 | Resilience load: loading skeleton, error load, dan Try Again | mock | 03, 04, 05 |
| TC-GS-GSET-E2E-004 | Tooltip info dan opsi dropdown kelima field | FE+BE | 06, 07, 08, 09, 10 |
| TC-GS-GSET-E2E-005 | Preview Currency dan Date & Time live update | FE+BE | 30, 31, 32 |
| TC-GS-GSET-E2E-006 | Accessibility form: live region dan operasi keyboard | FE+BE | 13 |
| TC-GS-GSET-E2E-007 | Guided Tooltip: konten step, navigasi Back/Next/Done, replay, dan keyboard | FE+BE | 15, 16, 18 |
| TC-GS-GSET-E2E-008 | Guided Tooltip: trigger kunjungan pertama dan persistensi flag | FE+BE | 14, 17, 146, 147 |
| TC-GS-GSET-E2E-009 | Mobile: layout bottom sheet, tooltip tap, dan dialog | web: unsupported | 19, 20, 21, 148, 149 |
| TC-GS-GSET-E2E-010 | Role matrix: Total Control dan Read Only | FE+BE | 22, 23 |
| TC-GS-GSET-E2E-011 | Role matrix negatif: menu hidden dan akses URL langsung | FE+BE | 24, 25, 26, 27 |
| TC-GS-GSET-E2E-012 | Save button state, revert, dan Save sukses | FE+BE | 28, 29, 42 |
| TC-GS-GSET-E2E-013 | Save per field, saving state, dan guard klik ganda | FE+BE | 33, 34, 35, 36, 41, 44, 45 |
| TC-GS-GSET-E2E-014 | Save beberapa field sekaligus termasuk Currency | FE+BE | 43 |
| TC-GS-GSET-E2E-015 | Dialog Change Currency: screening, konfirmasi, Cancel/Esc, backdrop | FE+BE | 37, 38, 39, 40, 115 |
| TC-GS-GSET-E2E-016 | Resilience Save: 5xx, timeout, dan Currency gagal | mock | 46, 47, 48 |
| TC-GS-GSET-E2E-017 | Dialog Unsaved Changes: navigasi in-app dan beforeunload | FE+BE | 49, 50, 51, 52, 53, 114, 116 |
| TC-GS-GSET-E2E-018 | Entitas suspended/expired: write lockdown dan read | FE+BE | 54, 55, 56 |
| TC-GS-GSET-E2E-019 | Session Idle Timeout: tidak retroaktif, sesi baru, dan kebijakan sesi | FE+BE | 57, 58, 59 |
| TC-GS-GSET-E2E-020 | Changelog screening, empty state, default sort, tooltip, a11y | FE+BE | 60, 61, 63, 65, 85, 86, 96 |
| TC-GS-GSET-E2E-021 | Changelog search: interaksi, per kolom, dan guard | FE+BE | 66, 67, 68, 69, 70 |
| TC-GS-GSET-E2E-022 | Changelog filter panel: screening, opsi dinamis, loading, no data | FE+BE | 71, 72, 75, 80, 150, 174, 177, 178 |
| TC-GS-GSET-E2E-023 | Changelog filter: Apply, chip, Clear Field, dan overflow | FE+BE | 73, 74, 76, 77, 78, 79, 81, 158, 175, 176, 179 |
| TC-GS-GSET-E2E-024 | Changelog sorting 3-state dan header Actions tanpa sort | FE+BE | 82, 83, 160 |
| TC-GS-GSET-E2E-025 | Changelog Setup Column: panel, modal, pin, hide, reorder, reset, discard | FE+BE | 84, 87, 88, 89, 90, 91, 92, 93, 94, 95 |
| TC-GS-GSET-E2E-026 | Changelog Download: overlay CSV/XLSX, filter, dan unhide | FE+BE | 97, 98, 99, 100, 159 |
| TC-GS-GSET-E2E-027 | Changelog pagination: default, page size, navigasi, input, retensi | FE+BE | 102, 157, 180, 181 |
| TC-GS-GSET-E2E-028 | Changelog kombinasi Search + Filter + Sort + page size | FE+BE | 151, 152, 153, 154, 155, 156, 182 |
| TC-GS-GSET-E2E-029 | Changelog kolom khusus: Date format, hover, Old/New utuh | FE+BE | 103, 161, 162, 163 |
| TC-GS-GSET-E2E-030 | Resilience Changelog: loading, error load + Try Again, download gagal | mock | 62, 64, 101 |
| TC-GS-GSET-E2E-031 | Audit Log: pencatatan mutasi dan snapshot entri lama | FE+BE | 104, 105, 106, 107, 108, 109, 111 |
| TC-GS-GSET-E2E-032 | Asersi absence log: Currency Symbol, no-op, System Log | FE+BE | 110, 112, 113 |
| TC-GS-GSET-E2E-033 | Record belum ada: seed default dan Save pertama (upsert) | FE+BE | 117 |
| TC-GS-GSET-E2E-034 | Cross-Module SSE: propagate, isolasi, dan no auto-refresh form | FE+BE | 118, 119, 120, 121 |
| TC-GS-GSET-E2E-035 | Cross-Module timestamp mengikuti Time Zone entitas staff | FE+BE | 122 |
| TC-GS-GSET-E2E-036 | Parity tanpa plan gating di semua paket | FE+BE | 123 |
| TC-GS-GSET-E2E-037 | Defense gate direct API: RBAC, entitas suspended, dan isolasi | FE+BE | 124, 125, 126, 127, 128, 129, 130, 144 |
| TC-GS-GSET-E2E-038 | Security payload: derivasi simbol dan PUT identik no-op | FE+BE | 131, 132 |
| TC-GS-GSET-E2E-039 | Validasi PUT direct API: 422 per field | FE+BE | 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143 |
| TC-GS-GSET-E2E-040 | Bypass client DOM: error inline per field | FE+BE | 164, 165, 166, 167, 168, 169, 170, 171, 172, 173 |
| TC-GS-GSET-E2E-041 | Multi-konteks: konkurensi Save last-write-wins | FE+BE | 145 |

---

## 2. TC Hanya-BE (Tidak Masuk Spec E2E)

**Tidak ada.** `tc-general-settings.md` adalah file E2E murni; kontrak API murni dipisahkan ke
`tc-general-settings-backend.md` (di luar cakupan suite ini) dan Section 6 tidak dibuat
(`testcase-conventions.md` §B.3 item 6). Tidak ada TC bertanda `FE Test: -` / `PIC FE: -`.
Spec 037–040 adalah TC security/bypass yang tetap ditulis sebagai spec FE+BE dengan asersi pada
respons server dan state data (bukan UI murni), sesuai arahan konversi: setiap TC FE menjadi spec.
Konsekuensinya, cakupan spec = **182/182 (100%)**, 0 TC dialihkan ke integration test backend.

---

## 3. Sebaran per Section TC

| Section | Jumlah TC | Masuk Spec E2E | Hanya-BE |
|---|:---:|:---:|:---:|
| 1. Initial State & Halaman General Settings Flow | 25 | 25 | 0 |
| 2. Role & Capability Access Flow | 7 | 7 | 0 |
| 3. Core Edit Operations Flow | 31 | 31 | 0 |
| 4a. Tabel Utama (modul single-record) | — (N/A) | — | — |
| 4b. Modal Changelog — Table Rules | 67 | 67 | 0 |
| 5. Audit Log & Multi-Surface Sync | 14 | 14 | 0 |
| 6. API Contract & Direct Backend Verification | — (dihentikan) | — | — |
| 7. Cross-Module Sync & Foundation Cascading | 6 | 6 | 0 |
| 8. Security & Defense-in-Depth | 31 | 31 | 0 |
| 9. Edge Case Matrix & Concurrency Sisa | 1 | 1 | 0 |
| **Total** | **182** | **182** | **0** |

Section 4a dan 6 tidak ada di dokumen sumber: halaman utama berupa form single-record (PRD §4, §5),
dan Section 6 (API Contract) dihentikan (kontrak API dipindahkan ke file backend).

---

## 4. Lapisan per TC (182 Baris)

Kolom **Mode** mengikuti penanda `Mode: mock` di `## Prerequisites` spec (intercept respons / fixture
kegagalan); sisanya `FE+BE`. Spec mobile (009) ditandai `unsupported` untuk target web.

| TC ID | Spec E2E | Mode |
|---|---|:---:|
| TC-GS-GSET-01 | TC-GS-GSET-E2E-001-screening-halaman-general-settings | FE+BE |
| TC-GS-GSET-02 | TC-GS-GSET-E2E-002-state-form-populated-dan-seed-default | FE+BE |
| TC-GS-GSET-03 | TC-GS-GSET-E2E-003-resilience-loading-skeleton-error-load-dan-retry | mock |
| TC-GS-GSET-04 | TC-GS-GSET-E2E-003-resilience-loading-skeleton-error-load-dan-retry | mock |
| TC-GS-GSET-05 | TC-GS-GSET-E2E-003-resilience-loading-skeleton-error-load-dan-retry | mock |
| TC-GS-GSET-06 | TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field | FE+BE |
| TC-GS-GSET-07 | TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field | FE+BE |
| TC-GS-GSET-08 | TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field | FE+BE |
| TC-GS-GSET-09 | TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field | FE+BE |
| TC-GS-GSET-10 | TC-GS-GSET-E2E-004-tooltip-info-dan-opsi-dropdown-kelima-field | FE+BE |
| TC-GS-GSET-11 | TC-GS-GSET-E2E-002-state-form-populated-dan-seed-default | FE+BE |
| TC-GS-GSET-12 | TC-GS-GSET-E2E-002-state-form-populated-dan-seed-default | FE+BE |
| TC-GS-GSET-13 | TC-GS-GSET-E2E-006-accessibility-form-live-region-dan-keyboard | FE+BE |
| TC-GS-GSET-14 | TC-GS-GSET-E2E-008-guided-tooltip-trigger-dan-persistensi-flag | FE+BE |
| TC-GS-GSET-15 | TC-GS-GSET-E2E-007-guided-tooltip-konten-dan-navigasi-step | FE+BE |
| TC-GS-GSET-16 | TC-GS-GSET-E2E-007-guided-tooltip-konten-dan-navigasi-step | FE+BE |
| TC-GS-GSET-17 | TC-GS-GSET-E2E-008-guided-tooltip-trigger-dan-persistensi-flag | FE+BE |
| TC-GS-GSET-18 | TC-GS-GSET-E2E-007-guided-tooltip-konten-dan-navigasi-step | FE+BE |
| TC-GS-GSET-19 | TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog | unsupported |
| TC-GS-GSET-20 | TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog | unsupported |
| TC-GS-GSET-21 | TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog | unsupported |
| TC-GS-GSET-22 | TC-GS-GSET-E2E-010-role-matrix-total-control-dan-read-only | FE+BE |
| TC-GS-GSET-23 | TC-GS-GSET-E2E-010-role-matrix-total-control-dan-read-only | FE+BE |
| TC-GS-GSET-24 | TC-GS-GSET-E2E-011-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-25 | TC-GS-GSET-E2E-011-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-26 | TC-GS-GSET-E2E-011-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-27 | TC-GS-GSET-E2E-011-role-matrix-negatif-menu-hidden-dan-akses-url-langsung | FE+BE |
| TC-GS-GSET-28 | TC-GS-GSET-E2E-012-save-button-state-clean-dirty-revert-dan-save-sukses | FE+BE |
| TC-GS-GSET-29 | TC-GS-GSET-E2E-012-save-button-state-clean-dirty-revert-dan-save-sukses | FE+BE |
| TC-GS-GSET-30 | TC-GS-GSET-E2E-005-preview-currency-dan-date-time-live-update | FE+BE |
| TC-GS-GSET-31 | TC-GS-GSET-E2E-005-preview-currency-dan-date-time-live-update | FE+BE |
| TC-GS-GSET-32 | TC-GS-GSET-E2E-005-preview-currency-dan-date-time-live-update | FE+BE |
| TC-GS-GSET-33 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-34 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-35 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-36 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-37 | TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop | FE+BE |
| TC-GS-GSET-38 | TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop | FE+BE |
| TC-GS-GSET-39 | TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop | FE+BE |
| TC-GS-GSET-40 | TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop | FE+BE |
| TC-GS-GSET-41 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-42 | TC-GS-GSET-E2E-012-save-button-state-clean-dirty-revert-dan-save-sukses | FE+BE |
| TC-GS-GSET-43 | TC-GS-GSET-E2E-014-save-multi-field-termasuk-currency | FE+BE |
| TC-GS-GSET-44 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-45 | TC-GS-GSET-E2E-013-save-per-field-saving-state-dan-guard-klik-ganda | FE+BE |
| TC-GS-GSET-46 | TC-GS-GSET-E2E-016-resilience-save-5xx-timeout-dan-currency-gagal | mock |
| TC-GS-GSET-47 | TC-GS-GSET-E2E-016-resilience-save-5xx-timeout-dan-currency-gagal | mock |
| TC-GS-GSET-48 | TC-GS-GSET-E2E-016-resilience-save-5xx-timeout-dan-currency-gagal | mock |
| TC-GS-GSET-49 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-50 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-51 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-52 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-53 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-54 | TC-GS-GSET-E2E-018-state-tenant-suspended-expired-write-lockdown-dan-read | FE+BE |
| TC-GS-GSET-55 | TC-GS-GSET-E2E-018-state-tenant-suspended-expired-write-lockdown-dan-read | FE+BE |
| TC-GS-GSET-56 | TC-GS-GSET-E2E-018-state-tenant-suspended-expired-write-lockdown-dan-read | FE+BE |
| TC-GS-GSET-57 | TC-GS-GSET-E2E-019-session-idle-timeout-tidak-retroaktif-sesi-baru-dan-kebijakan-sesi | FE+BE |
| TC-GS-GSET-58 | TC-GS-GSET-E2E-019-session-idle-timeout-tidak-retroaktif-sesi-baru-dan-kebijakan-sesi | FE+BE |
| TC-GS-GSET-59 | TC-GS-GSET-E2E-019-session-idle-timeout-tidak-retroaktif-sesi-baru-dan-kebijakan-sesi | FE+BE |
| TC-GS-GSET-60 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-61 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-62 | TC-GS-GSET-E2E-030-resilience-changelog-loading-error-load-retry-dan-download-gagal | mock |
| TC-GS-GSET-63 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-64 | TC-GS-GSET-E2E-030-resilience-changelog-loading-error-load-retry-dan-download-gagal | mock |
| TC-GS-GSET-65 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-66 | TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard | FE+BE |
| TC-GS-GSET-67 | TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard | FE+BE |
| TC-GS-GSET-68 | TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard | FE+BE |
| TC-GS-GSET-69 | TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard | FE+BE |
| TC-GS-GSET-70 | TC-GS-GSET-E2E-021-changelog-search-interaksi-per-kolom-dan-guard | FE+BE |
| TC-GS-GSET-71 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-72 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-73 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-74 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-75 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-76 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-77 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-78 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-79 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-80 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-81 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-82 | TC-GS-GSET-E2E-024-changelog-sorting-3-state-dan-header-actions-tanpa-sort | FE+BE |
| TC-GS-GSET-83 | TC-GS-GSET-E2E-024-changelog-sorting-3-state-dan-header-actions-tanpa-sort | FE+BE |
| TC-GS-GSET-84 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-85 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-86 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-87 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-88 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-89 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-90 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-91 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-92 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-93 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-94 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-95 | TC-GS-GSET-E2E-025-changelog-setup-column-panel-modal-pin-hide-reorder-reset-dan-discard | FE+BE |
| TC-GS-GSET-96 | TC-GS-GSET-E2E-020-changelog-screening-empty-state-default-sort-tooltip-dan-a11y | FE+BE |
| TC-GS-GSET-97 | TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide | FE+BE |
| TC-GS-GSET-98 | TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide | FE+BE |
| TC-GS-GSET-99 | TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide | FE+BE |
| TC-GS-GSET-100 | TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide | FE+BE |
| TC-GS-GSET-101 | TC-GS-GSET-E2E-030-resilience-changelog-loading-error-load-retry-dan-download-gagal | mock |
| TC-GS-GSET-102 | TC-GS-GSET-E2E-027-changelog-pagination-default-page-size-navigasi-input-dan-retensi-kriteria | FE+BE |
| TC-GS-GSET-103 | TC-GS-GSET-E2E-029-changelog-kolom-date-format-self-reference-hover-modified-by-dan-old-new-utuh | FE+BE |
| TC-GS-GSET-104 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-105 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-106 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-107 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-108 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-109 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-110 | TC-GS-GSET-E2E-032-absence-log-currency-symbol-no-op-dan-system-log | FE+BE |
| TC-GS-GSET-111 | TC-GS-GSET-E2E-031-pencatatan-changelog-activity-log-mutasi-dan-snapshot | FE+BE |
| TC-GS-GSET-112 | TC-GS-GSET-E2E-032-absence-log-currency-symbol-no-op-dan-system-log | FE+BE |
| TC-GS-GSET-113 | TC-GS-GSET-E2E-032-absence-log-currency-symbol-no-op-dan-system-log | FE+BE |
| TC-GS-GSET-114 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-115 | TC-GS-GSET-E2E-015-dialog-change-currency-screening-konfirmasi-cancel-esc-backdrop | FE+BE |
| TC-GS-GSET-116 | TC-GS-GSET-E2E-017-dialog-unsaved-changes-navigasi-in-app-dan-beforeunload | FE+BE |
| TC-GS-GSET-117 | TC-GS-GSET-E2E-033-record-belum-ada-seed-default-dan-upsert-save-pertama | FE+BE |
| TC-GS-GSET-118 | TC-GS-GSET-E2E-034-cross-module-sse-propagate-isolasi-dan-no-autorefresh-form | FE+BE |
| TC-GS-GSET-119 | TC-GS-GSET-E2E-034-cross-module-sse-propagate-isolasi-dan-no-autorefresh-form | FE+BE |
| TC-GS-GSET-120 | TC-GS-GSET-E2E-034-cross-module-sse-propagate-isolasi-dan-no-autorefresh-form | FE+BE |
| TC-GS-GSET-121 | TC-GS-GSET-E2E-034-cross-module-sse-propagate-isolasi-dan-no-autorefresh-form | FE+BE |
| TC-GS-GSET-122 | TC-GS-GSET-E2E-035-cross-module-timestamp-mengikuti-entitas-staff-yang-login | FE+BE |
| TC-GS-GSET-123 | TC-GS-GSET-E2E-036-parity-tanpa-plan-gating-di-semua-paket | FE+BE |
| TC-GS-GSET-124 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-125 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-126 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-127 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-128 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-129 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-130 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-131 | TC-GS-GSET-E2E-038-security-derivasi-simbol-dan-payload-identik-no-op | FE+BE |
| TC-GS-GSET-132 | TC-GS-GSET-E2E-038-security-derivasi-simbol-dan-payload-identik-no-op | FE+BE |
| TC-GS-GSET-133 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-134 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-135 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-136 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-137 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-138 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-139 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-140 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-141 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-142 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-143 | TC-GS-GSET-E2E-039-security-validasi-422-direct-api-per-field | FE+BE |
| TC-GS-GSET-144 | TC-GS-GSET-E2E-037-security-defense-gate-direct-api-rbac-dan-isolasi-entitas | FE+BE |
| TC-GS-GSET-145 | TC-GS-GSET-E2E-041-multi-konteks-konkurensi-save-last-write-wins | FE+BE |
| TC-GS-GSET-146 | TC-GS-GSET-E2E-008-guided-tooltip-trigger-dan-persistensi-flag | FE+BE |
| TC-GS-GSET-147 | TC-GS-GSET-E2E-008-guided-tooltip-trigger-dan-persistensi-flag | FE+BE |
| TC-GS-GSET-148 | TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog | unsupported |
| TC-GS-GSET-149 | TC-GS-GSET-E2E-009-mobile-layout-bottom-sheet-tooltip-dan-dialog | unsupported |
| TC-GS-GSET-150 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-151 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-152 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-153 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-154 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-155 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-156 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |
| TC-GS-GSET-157 | TC-GS-GSET-E2E-027-changelog-pagination-default-page-size-navigasi-input-dan-retensi-kriteria | FE+BE |
| TC-GS-GSET-158 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-159 | TC-GS-GSET-E2E-026-changelog-download-overlay-csv-xlsx-filter-dan-unhide | FE+BE |
| TC-GS-GSET-160 | TC-GS-GSET-E2E-024-changelog-sorting-3-state-dan-header-actions-tanpa-sort | FE+BE |
| TC-GS-GSET-161 | TC-GS-GSET-E2E-029-changelog-kolom-date-format-self-reference-hover-modified-by-dan-old-new-utuh | FE+BE |
| TC-GS-GSET-162 | TC-GS-GSET-E2E-029-changelog-kolom-date-format-self-reference-hover-modified-by-dan-old-new-utuh | FE+BE |
| TC-GS-GSET-163 | TC-GS-GSET-E2E-029-changelog-kolom-date-format-self-reference-hover-modified-by-dan-old-new-utuh | FE+BE |
| TC-GS-GSET-164 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-165 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-166 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-167 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-168 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-169 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-170 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-171 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-172 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-173 | TC-GS-GSET-E2E-040-security-bypass-client-dom-error-inline-per-field | FE+BE |
| TC-GS-GSET-174 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-175 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-176 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-177 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-178 | TC-GS-GSET-E2E-022-changelog-filter-panel-screening-opsi-dinamis-loading-dan-no-data | FE+BE |
| TC-GS-GSET-179 | TC-GS-GSET-E2E-023-changelog-filter-apply-chip-clear-dan-overflow | FE+BE |
| TC-GS-GSET-180 | TC-GS-GSET-E2E-027-changelog-pagination-default-page-size-navigasi-input-dan-retensi-kriteria | FE+BE |
| TC-GS-GSET-181 | TC-GS-GSET-E2E-027-changelog-pagination-default-page-size-navigasi-input-dan-retensi-kriteria | FE+BE |
| TC-GS-GSET-182 | TC-GS-GSET-E2E-028-changelog-kombinasi-search-filter-sort-dan-page-size | FE+BE |

---

## 5. Temuan terhadap Dokumen Sumber

1. **Tidak ada kurung ID yang kosong di rentang 01–182.** Berbeda dari versi TC lama (148 baris),
   dokumen canonical saat ini padat dari 01 s.d. 182 tanpa nomor bolong.
2. **Nama field currency adalah `Currency Code`**, bukan "Currency". Dipakai di form, kolom
   changelog, dan filter.
3. **Cancel dialog "Change Currency" tidak mereset nilai baru.** TC-39: setelah Cancel, form tetap
   dirty dengan currency baru (mis. USD) dan Button "Save" tetap aktif. Revert manual diuji terpisah
   di TC-42 (masuk spec 012).
4. **Guard bypass dialog di TC-41.** Bila currency tidak berubah tetapi field lain berubah, Save
   langsung hit `PUT` tanpa dialog "Change Currency".
5. **Modal changelog punya 7 kolom**, termasuk kolom `Actions (⋯)` terakhir yang tidak ada di
   checklist Setup Column (statis, selalu rightmost) — TC-84 (spec 025).
6. **Filter panel changelog tidak punya filter Action**; hanya Date, Field, dan Modified By. Opsi
   Field dan Modified By populates dari data tabel (NC-18), bukan daftar tetap.
7. **Section 6 (API Contract) dan Section 4a (Tabel Utama) tidak ada** karena modul single-record.
   Kontrak API murni ada di `tc-general-settings-backend.md` (di luar cakupan suite ini).
8. **TC mobile (19–21, 148, 149) ditulis sebagai satu spec (009) dengan `coverage.web: unsupported`**;
   eksekusi mobile ditangani target mobile terpisah.
9. **Mode `mock` dipilih dari kebutuhan intercept/fixture**, bukan dari kolom `FE Test`: spec `003`
   (skeleton + error load + retry), `016` (save 5xx/timeout/currency gagal), `030` (changelog
   loading/error/retry + download gagal). Faktor pemersatu: butuh kontrol penuh atas respons server.
10. **Spec terbesar** (11 TC): `023`, `025` (10), `028` (7), `039` (11), `040` (10). Bila `web.test.ts`
    melewati batas langkah/token, pecah per blok field/kolom tanpa mengubah `sourceTc`.

---

## 6. Kebutuhan Environment

Semua kebutuhan ditulis di `## Prerequisites` spec masing-masing.

| Kebutuhan | Spec | Alasan |
|---|---|---|
| Kredensial login via env | semua | Tidak menulis kredensial di spec/fixture. |
| Intercept respons per endpoint | 003, 016, 030 | Simulasi backend down, timeout, dan download error. |
| Akun 5 aktor Tabel Data Uji (Total Control, Admin B, Read Only, Capability individual, System Role) | 010, 011, 017, 018, 037, 041 | Role matrix, dialog, dan direct API. |
| Token sesi per aktor | 037, 038, 039 | Request API langsung (defense-in-depth). |
| Dua sesi browser simultan | 034, 041 | SSE cross-tab dan konkurensi Save. |
| SSE server-event yang bisa dikirim ke test client | 034 | Propagate format dan isolasi tenant. |
| Entitas kedua untuk isolasi | 034, 037 | Channel SSE dan record lintas entitas. |
| Entitas suspended/expired | 018 | Write lockdown D1. |
| Entitas `Client Tanpa Record` (record dihapus via DB) | 033 | Row belum ada / upsert. |
| Data changelog historis (>100 baris) | 027, 028 | Pagination 10/25/50/100 dan kombinasi filter. |
| Manipulasi waktu idle (Auth) | 019 | Verifikasi tidak retroaktif dan sesi baru. |
| Viewport mobile | 009 | Layout bottom sheet (target mobile). |

---

## 7. Verifikasi Silang

Pemetaan dihitung terhadap 182 baris TC di `tc-general-settings.md`:

- 182 ID TC unik tercatat, masing-masing tepat satu kali.
- 0 ID dobel dalam `sourceTc`.
- 0 ID yang tidak ada di `tc-general-settings.md`.
- 0 TC yang tidak masuk spec (hanya-BE = 0).
- Sebaran spec: 41 spec; `mock` = 3 spec (003, 016, 030); `unsupported` = 1 spec (009); sisanya FE+BE.

`spectra lint` tidak memvalidasi isi `sourceTc`, jadi pengecekan ini diulang setiap kali spec
bertambah atau berubah.
