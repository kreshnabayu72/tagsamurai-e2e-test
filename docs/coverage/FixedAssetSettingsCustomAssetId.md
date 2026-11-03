# Coverage E2E — Fixed Asset > Settings > Custom Asset ID

Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md` (343 TC) dan `tc-settings-custom-asset-id-backend.md` (namespace `TC-FAID-BE-*`, tidak memuat ID FE; tidak ada TC hanya-BE).
Suite: `specs/FixedAsset/SettingsCustomAssetId/`.
Prefix Modul: `FA` + `CAID` (`TC-FA-CAID-E2E-*`).
Status semua spec: `draft`.

---

## 1. Pemetaan TC Granular → Spec E2E (97 Spec Atomik)

| Spec | Isi / Judul | Mode | Langkah | TC Sumber |
|---|---|:---:|:---:|---|
| TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | Screening Tab Custom Asset ID: Tampilan Awal, Breadcrumb, dan Refresh | FE+BE | 37 | TC-FA-CAID-1, TC-FA-CAID-2, TC-FA-CAID-3, TC-FA-CAID-4, TC-FA-CAID-5 |
| TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | Screening Form Konfigurasi Tersimpan: Nilai, Tooltip, Baris Initial Company, dan Daftar Segmen | FE+BE | 33 | TC-FA-CAID-7, TC-FA-CAID-8, TC-FA-CAID-9, TC-FA-CAID-10, TC-FA-CAID-11 |
| TC-FA-CAID-E2E-003-screening-company-kosong-dan-empty-state | Company Kosong: Nilai Default Form dan Empty State Modal | FE+BE | 16 | TC-FA-CAID-6, TC-FA-CAID-158, TC-FA-CAID-228 |
| TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi | Guided Tooltip: Konten, Kunjungan Pertama, Ulang, dan Navigasi Step | FE+BE | 45 | TC-FA-CAID-13, TC-FA-CAID-14, TC-FA-CAID-15, TC-FA-CAID-16 |
| TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | Guided Tooltip: Skip, Overlay, Resize, Keyboard, dan Flag per User | FE+BE | 40 | TC-FA-CAID-17, TC-FA-CAID-18, TC-FA-CAID-19, TC-FA-CAID-20, TC-FA-CAID-21 |
| TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | Role Matrix: Visibilitas Elemen Tab Custom Asset ID per Role | FE+BE | 25 | TC-FA-CAID-22, TC-FA-CAID-23, TC-FA-CAID-24, TC-FA-CAID-25, TC-FA-CAID-26 |
| TC-FA-CAID-E2E-007-role-matrix-read-only-modal-dan-download | Role Matrix: Read Only Membuka Modal, Tooltip Disabled, dan Download Code List | FE+BE | 24 | TC-FA-CAID-27, TC-FA-CAID-28, TC-FA-CAID-157 |
| TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | Role Matrix: Pemegang Manage asset ID configuration: Tabs Bar, Account Codes, Save, Toggle, dan Pelaku Log | FE+BE | 34 | TC-FA-CAID-29, TC-FA-CAID-43, TC-FA-CAID-30, TC-FA-CAID-31, TC-FA-CAID-251 |
| TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung | Capability Dicabut Saat Tab Terbuka dan URL Langsung Tanpa Akses | FE+BE | 32 | TC-FA-CAID-39, TC-FA-CAID-40, TC-FA-CAID-41, TC-FA-CAID-42 |
| TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | Plan Starter: Tab Terkunci, Banner Upgrade Plan, dan Plan Non-Starter | FE+BE | 32 | TC-FA-CAID-32, TC-FA-CAID-33, TC-FA-CAID-34, TC-FA-CAID-35, TC-FA-CAID-36, TC-FA-CAID-37, TC-FA-CAID-38 |
| TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade | Plan Tier: Registrasi Starter, Downgrade, dan Upgrade | FE+BE | 42 | TC-FA-CAID-267, TC-FA-CAID-268, TC-FA-CAID-269, TC-FA-CAID-270 |
| TC-FA-CAID-E2E-012-state-tenant-plan-diturunkan-saat-form-terbuka | State Tenant: Plan Diturunkan ke Starter Saat Form Terbuka | FE+BE | 16 | TC-FA-CAID-314, TC-FA-CAID-315 |
| TC-FA-CAID-E2E-014-plan-starter-guard-pembaruan-otomatis | Plan Starter: Guard Pembaruan Otomatis Asset ID Saat Transfer, Edit Asset, dan Mutasi Division | FE+BE | 29 | TC-FA-CAID-335 |
| TC-FA-CAID-E2E-015-create-pertama-company-kosong | Create Konfigurasi Pertama pada Company Kosong: Save, Separator, Initial Company, dan Toggle | FE+BE | 34 | TC-FA-CAID-44, TC-FA-CAID-45, TC-FA-CAID-46, TC-FA-CAID-47 |
| TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter | Initial Company: Checkbox, Kapital Otomatis, dan Batas 5 Karakter | FE+BE | 35 | TC-FA-CAID-48, TC-FA-CAID-49, TC-FA-CAID-50, TC-FA-CAID-51 |
| TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview | Initial Company: Paste, Karakter Terlarang, dan Live Preview Kosong | FE+BE | 28 | TC-FA-CAID-52, TC-FA-CAID-53, TC-FA-CAID-54, TC-FA-CAID-58 |
| TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | Initial Company: Validasi Kosong Diblokir dan Save Nilai Valid | FE+BE | 42 | TC-FA-CAID-57, TC-FA-CAID-55, TC-FA-CAID-56, TC-FA-CAID-59, TC-FA-CAID-60 |
| TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview | Daftar Segmen: Asset Increment Terkunci, Centang Segmen, dan Live Preview | FE+BE | 35 | TC-FA-CAID-61, TC-FA-CAID-62, TC-FA-CAID-63, TC-FA-CAID-64 |
| TC-FA-CAID-E2E-020-segmen-reorder-drag-keyboard-dan-aria-live | Daftar Segmen: Reorder Drag, Keyboard, dan Aria-Live Live Preview | FE+BE | 19 | TC-FA-CAID-65, TC-FA-CAID-66, TC-FA-CAID-67 |
| TC-FA-CAID-E2E-021-separator-dan-state-tombol-save | Dropdown Separator dan State Tombol Save Pristine | FE+BE | 27 | TC-FA-CAID-68, TC-FA-CAID-69, TC-FA-CAID-70, TC-FA-CAID-71 |
| TC-FA-CAID-E2E-022-perilaku-tombol-save | Perilaku Tombol Save: Spinner, Klik Ganda, dan Pristine Setelah Sukses | FE+BE | 24 | TC-FA-CAID-73, TC-FA-CAID-74, TC-FA-CAID-75 |
| TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial | Retroactive Mass Update A: Separator, Division, Account, dan Initial Company | FE+BE | 35 | TC-FA-CAID-76, TC-FA-CAID-77, TC-FA-CAID-78, TC-FA-CAID-79 |
| TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus | Retroactive Mass Update B: Urutan Segmen, Multi Perubahan, Space, dan None | FE+BE | 38 | TC-FA-CAID-80, TC-FA-CAID-81, TC-FA-CAID-82, TC-FA-CAID-83 |
| TC-FA-CAID-E2E-025-retroactive-update-increment-polos-dan-urutan-unchecked | Retroactive Mass Update C: Hanya Asset Increment, Urutan Segmen Unchecked, dan Toggle ke ON | FE+BE | 36 | TC-FA-CAID-84, TC-FA-CAID-85, TC-FA-CAID-99 |
| TC-FA-CAID-E2E-026-defense-in-depth-otorisasi-request-langsung | Defense-in-Depth: Request Save dan Toggle Langsung Tanpa Capability dan pada Plan Starter | FE+BE | 24 | TC-FA-CAID-303, TC-FA-CAID-304, TC-FA-CAID-305 |
| TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung | Defense-in-Depth: Request Save Langsung dengan Segmen Kosong, Tanpa Increment, Tanpa Separator, dan Initial Company Kosong | FE+BE | 32 | TC-FA-CAID-306, TC-FA-CAID-307, TC-FA-CAID-308, TC-FA-CAID-309 |
| TC-FA-CAID-E2E-028-defense-in-depth-initial-company-request-langsung | Defense-in-Depth: Request Save Langsung dengan Initial Company Berkarakter Terlarang dan Lebih dari 5 Karakter | FE+BE | 14 | TC-FA-CAID-337, TC-FA-CAID-338 |
| TC-FA-CAID-E2E-029-defense-in-depth-save-saat-master-switch-off | Defense-in-Depth: Request Save Langsung Saat Master Switch OFF Diproses Seperti Save Biasa | FE+BE | 24 | TC-FA-CAID-333 |
| TC-FA-CAID-E2E-030-registrasi-pertama-company-kosong-increment-polos | Registrasi Aset pada Company Kosong Tanpa Konfigurasi Memakai Increment Polos | FE+BE | 9 | TC-FA-CAID-262 |
| TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter | V-07 pada Save: Batas 63, 64, dan 65 Karakter serta Rollback Transaksi | FE+BE | 33 | TC-FA-CAID-86, TC-FA-CAID-87, TC-FA-CAID-88, TC-FA-CAID-89 |
| TC-FA-CAID-E2E-032-v07-alert-inline-hilang-dan-slot-alert-bersama | V-07: Alert Inline Hilang dan Slot Alert Bersama D-03 dan D-06 | FE+BE | 26 | TC-FA-CAID-90, TC-FA-CAID-91, TC-FA-CAID-334 |
| TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | Master Switch: Dialog D-02, Cancel, Esc, Backdrop, dan Konfirmasi Disable | FE+BE | 39 | TC-FA-CAID-94, TC-FA-CAID-95, TC-FA-CAID-96, TC-FA-CAID-97, TC-FA-CAID-98 |
| TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock | Master Switch: OFF lalu ON, Form Dirty, Lock Selama Request, dan Dim Saat OFF | FE+BE | 38 | TC-FA-CAID-100, TC-FA-CAID-101, TC-FA-CAID-102, TC-FA-CAID-103 |
| TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | Dialog D-01 Unsaved Changes: Judul, Cancel, Leave, Breadcrumb, dan Sidebar | FE+BE | 30 | TC-FA-CAID-104, TC-FA-CAID-105, TC-FA-CAID-106, TC-FA-CAID-107, TC-FA-CAID-108 |
| TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | Dialog D-01: Esc, Backdrop, Form Pristine, Setelah Save, Nilai Dikembalikan, dan Refresh | FE+BE | 38 | TC-FA-CAID-109, TC-FA-CAID-110, TC-FA-CAID-111, TC-FA-CAID-112, TC-FA-CAID-113, TC-FA-CAID-114, TC-FA-CAID-115 |
| TC-FA-CAID-E2E-037-pencatatan-log-create-company-kosong | Pencatatan Log Create pada Company Kosong: Save Pertama dan Toggle Pertama | FE+BE | 44 | TC-FA-CAID-233, TC-FA-CAID-234, TC-FA-CAID-235 |
| TC-FA-CAID-E2E-038-pencatatan-log-edit-status-separator-segmen | Pencatatan Log Edit: Status dan Separator | FE+BE | 34 | TC-FA-CAID-236, TC-FA-CAID-237, TC-FA-CAID-238 |
| TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company | Pencatatan Log Edit: Segments Formula Dicentang dan Perubahan Initial Company | FE+BE | 44 | TC-FA-CAID-239, TC-FA-CAID-240, TC-FA-CAID-241, TC-FA-CAID-242 |
| TC-FA-CAID-E2E-040-pencatatan-log-edit-urutan-dan-multi-perubahan | Pencatatan Log Edit: Segments Order, Multi Perubahan, dan Satu Entri per Field | FE+BE | 38 | TC-FA-CAID-243, TC-FA-CAID-244, TC-FA-CAID-245 |
| TC-FA-CAID-E2E-041-pencatatan-log-snapshot-dan-kolom-surface | Pencatatan Log: Snapshot Immutable, Kolom Object dan Name, serta Opsi Filter Object | FE+BE | 23 | TC-FA-CAID-248, TC-FA-CAID-249, TC-FA-CAID-250 |
| TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri | Pencatatan Log Absence: Zero-Delta, No-Op, Mass Update, dan Save Ditolak Tanpa Entri | FE+BE | 54 | TC-FA-CAID-72, TC-FA-CAID-246, TC-FA-CAID-247, TC-FA-CAID-252 |
| TC-FA-CAID-E2E-043-multi-konteks-isolasi-dua-tenant | Multi-Konteks: Isolasi Dua Tenant pada Form, Code List, dan Changelog | FE+BE | 19 | TC-FA-CAID-310, TC-FA-CAID-311 |
| TC-FA-CAID-E2E-044-multi-konteks-dua-admin-bersamaan | Multi-Konteks: Dua Admin Registrasi dan Save Konfigurasi Bersamaan, Last-Write-Wins | FE+BE | 26 | TC-FA-CAID-324, TC-FA-CAID-326, TC-FA-CAID-327 |
| TC-FA-CAID-E2E-045-multi-konteks-race-dengan-mass-update | Multi-Konteks: Registrasi, Transfer, Edit Asset, dan Mutasi Division Saat Mass Update Berjalan | FE+BE | 33 | TC-FA-CAID-330, TC-FA-CAID-331 |
| TC-FA-CAID-E2E-046-volume-10000-aset-save-sinkron-dan-rollback | Volume 10.000 Aset: Save Sinkron Atomik dan Kegagalan Server Membatalkan Transaksi | FE+BE | 27 | TC-FA-CAID-322, TC-FA-CAID-323 |
| TC-FA-CAID-E2E-047-v07-toggle-on-ditolak-dan-berhasil-setelah-code-division-diperpendek | V-07: Toggle ON Ditolak lalu Berhasil Setelah Code Division Diperpendek | FE+BE | 17 | TC-FA-CAID-92, TC-FA-CAID-93 |
| TC-FA-CAID-E2E-048-multi-konteks-dua-admin-status-sama-dan-sinkron-surface | Multi-Konteks: Dua Admin Toggle ke Status Sama dan Sinkron Surface Sesi Lain | FE+BE | 25 | TC-FA-CAID-328, TC-FA-CAID-329 |
| TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris | Modal View Code List: Screening, Isi Tab, dan Aturan Baris | FE+BE | 32 | TC-FA-CAID-116, TC-FA-CAID-117, TC-FA-CAID-118, TC-FA-CAID-119 |
| TC-FA-CAID-E2E-050-code-list-dataset-khusus-teks-literal-dan-nama-panjang | Modal View Code List: Teks Literal, Nama 120 Karakter, dan Toolbar Tanpa Filter | FE+BE | 20 | TC-FA-CAID-127, TC-FA-CAID-162, TC-FA-CAID-163 |
| TC-FA-CAID-E2E-051-code-list-search-siklus-interaksi-dan-empty-state | Modal View Code List: Siklus Interaksi Search dan Empty State | FE+BE | 24 | TC-FA-CAID-121, TC-FA-CAID-124 |
| TC-FA-CAID-E2E-052-code-list-search-trim-kolom-tersembunyi-dan-sort-tidak-mereset | Modal View Code List: Search Trim, Visibilitas Kolom, dan Sort Tidak Mereset Search | FE+BE | 24 | TC-FA-CAID-125, TC-FA-CAID-126, TC-FA-CAID-131 |
| TC-FA-CAID-E2E-053-code-list-sort-tiga-state | Modal View Code List: Sort 3-State per Kolom | FE+BE | 39 | TC-FA-CAID-128, TC-FA-CAID-129, TC-FA-CAID-130 |
| TC-FA-CAID-E2E-054-code-list-pagination-default-input-halaman-dan-state-per-tab | Modal View Code List: Pagination 120 Baris per Tab, State per Tab, dan Input Halaman | FE+BE | 48 | TC-FA-CAID-120, TC-FA-CAID-142, TC-FA-CAID-143 |
| TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset | Modal View Code List: Halaman Tidak Valid, Ganti Page Size, Sort, dan Search Mereset Halaman | FE+BE | 24 | TC-FA-CAID-144, TC-FA-CAID-145, TC-FA-CAID-146, TC-FA-CAID-147 |
| TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag | Modal View Code List: Setup Column Screening, Hide, dan Drag Reorder | FE+BE | 32 | TC-FA-CAID-132, TC-FA-CAID-133, TC-FA-CAID-134, TC-FA-CAID-135 |
| TC-FA-CAID-E2E-057-code-list-setup-column-pin-reset-to-default-dan-penutupan-popup | Modal View Code List: Setup Column Pin, Reset to Default, dan Penutupan Popup | FE+BE | 29 | TC-FA-CAID-136, TC-FA-CAID-137, TC-FA-CAID-138 |
| TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | Modal View Code List: Download Overlay, Nama Berkas, Search Aktif, dan Kolom Tersembunyi | FE+BE | 34 | TC-FA-CAID-148, TC-FA-CAID-149, TC-FA-CAID-151, TC-FA-CAID-153, TC-FA-CAID-154 |
| TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx | Download: Isi Berkas CSV dan XLSX Code List dan Changelog | FE+BE | 33 | TC-FA-CAID-150, TC-FA-CAID-152, TC-FA-CAID-221, TC-FA-CAID-222 |
| TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | Modal Code List dan Changelog: Penutupan, Esc Berlapis, Back Browser, dan Aksesibilitas Fokus | FE+BE | 34 | TC-FA-CAID-160, TC-FA-CAID-161, TC-FA-CAID-231, TC-FA-CAID-232, TC-FA-CAID-343 |
| TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | Resilience A: Error Load Config, Code List, dan Changelog serta Toggle 5xx dan Koneksi Terputus | FE+BE | 59 | TC-FA-CAID-12, TC-FA-CAID-159, TC-FA-CAID-230, TC-FA-CAID-317, TC-FA-CAID-321 |
| TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | Resilience B: Save 5xx, Koneksi Terputus, Respons Detik ke-59, dan Download Gagal | FE+BE | 66 | TC-FA-CAID-316, TC-FA-CAID-319, TC-FA-CAID-340, TC-FA-CAID-155, TC-FA-CAID-226 |
| TC-FA-CAID-E2E-063-resilience-timeout-60-detik-toggle-dan-edit-asset-gagal | Resilience C: Save dan Toggle Melewati 60 Detik serta Edit Asset Gagal di Server | FE+BE | 48 | TC-FA-CAID-318, TC-FA-CAID-320, TC-FA-CAID-332 |
| TC-FA-CAID-E2E-064-code-list-search-kelas-nama-hierarki-dan-kelas-nama-datar | Modal View Code List: Search Kelas Nama Hierarki dan Kelas Nama Datar | FE+BE | 26 | TC-FA-CAID-122, TC-FA-CAID-123 |
| TC-FA-CAID-E2E-065-code-list-setup-column-guard-satu-kolom-semua-tab-dan-independen | Modal View Code List: Setup Column Guard Satu Kolom, Perilaku Semua Tab, dan Konfigurasi Independen per Tab | FE+BE | 32 | TC-FA-CAID-139, TC-FA-CAID-140, TC-FA-CAID-141 |
| TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | Modal Changelog: Screening, Format Sel, dan Format Tanggal General Settings | FE+BE | 36 | TC-FA-CAID-164, TC-FA-CAID-165, TC-FA-CAID-166, TC-FA-CAID-341, TC-FA-CAID-342 |
| TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai | Modal Changelog: Search Siklus, Placeholder, Kelas Enum, dan Nilai Campuran | FE+BE | 35 | TC-FA-CAID-167, TC-FA-CAID-168, TC-FA-CAID-169, TC-FA-CAID-170 |
| TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | Modal Changelog: Search Modified By, Kolom Date, Trim, Empty State, dan Visibilitas Kolom | FE+BE | 24 | TC-FA-CAID-171, TC-FA-CAID-172, TC-FA-CAID-173, TC-FA-CAID-174, TC-FA-CAID-175, TC-FA-CAID-176 |
| TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and | Modal Changelog: Filter Panel, Rentang Date, Dropdown OR, dan Logika AND | FE+BE | 40 | TC-FA-CAID-177, TC-FA-CAID-178, TC-FA-CAID-179, TC-FA-CAID-180 |
| TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search | Modal Changelog: Chip Filter dan Kombinasi Search dengan Filter | FE+BE | 25 | TC-FA-CAID-181, TC-FA-CAID-182, TC-FA-CAID-183, TC-FA-CAID-184 |
| TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | Modal Changelog: Clear Field, Pemulihan Empty State, Draft Filter, dan Badge | FE+BE | 34 | TC-FA-CAID-185, TC-FA-CAID-186, TC-FA-CAID-187, TC-FA-CAID-188, TC-FA-CAID-189 |
| TC-FA-CAID-E2E-072-changelog-filter-independen-kolom-tanpa-filter-dan-tanpa-hasil | Modal Changelog: Filter Independen Column Visibility, Kolom Tanpa Filter, dan Filter Tanpa Hasil | FE+BE | 14 | TC-FA-CAID-190, TC-FA-CAID-191, TC-FA-CAID-229 |
| TC-FA-CAID-E2E-073-changelog-sort-tiga-state | Modal Changelog: Urutan Default dan Sort 3-State per Kolom | FE+BE | 35 | TC-FA-CAID-192, TC-FA-CAID-193, TC-FA-CAID-194, TC-FA-CAID-195, TC-FA-CAID-196, TC-FA-CAID-197 |
| TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | Modal Changelog: Setup Column Screening dan Kelas Date | FE+BE | 36 | TC-FA-CAID-198, TC-FA-CAID-199, TC-FA-CAID-200, TC-FA-CAID-201, TC-FA-CAID-202 |
| TC-FA-CAID-E2E-075-changelog-setup-column-kelas-teks-pendek | Modal Changelog: Setup Column Kelas Teks Pendek | FE+BE | 19 | TC-FA-CAID-203, TC-FA-CAID-204, TC-FA-CAID-205 |
| TC-FA-CAID-E2E-076-changelog-setup-column-kelas-nilai-campuran | Modal Changelog: Setup Column Kelas Nilai Campuran | FE+BE | 19 | TC-FA-CAID-206, TC-FA-CAID-207, TC-FA-CAID-208 |
| TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | Modal Changelog: Batas Pin, Reset to Default, Close, Guard Satu Kolom, dan Cache Independen | FE+BE | 28 | TC-FA-CAID-209, TC-FA-CAID-210, TC-FA-CAID-211, TC-FA-CAID-212, TC-FA-CAID-213 |
| TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | Modal Changelog: Pagination 5.001 Entri, Input Halaman, Ganti Page Size, Sort, dan Filter | FE+BE | 31 | TC-FA-CAID-214, TC-FA-CAID-215, TC-FA-CAID-216, TC-FA-CAID-217, TC-FA-CAID-218, TC-FA-CAID-219 |
| TC-FA-CAID-E2E-079-changelog-download-nama-header-dan-hasil-kosong | Modal Changelog: Download Overlay, Hasil Kosong, dan Kolom Tersembunyi | FE+BE | 15 | TC-FA-CAID-220, TC-FA-CAID-224, TC-FA-CAID-225 |
| TC-FA-CAID-E2E-080-download-volume-di-atas-5000-baris | Download di Atas 5.000 Baris: Loading Screen Tanpa Job Background dan Cakupan Seluruh Halaman | FE+BE | 27 | TC-FA-CAID-156, TC-FA-CAID-223, TC-FA-CAID-227 |
| TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | Registrasi Aset: Increment Berurutan, Resolusi Segmen, Separator, dan Legacy Register | FE+BE | 34 | TC-FA-CAID-256, TC-FA-CAID-257, TC-FA-CAID-258, TC-FA-CAID-259, TC-FA-CAID-260 |
| TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter | Registrasi Aset: Approval Tanpa Increment Baru, Fallback Master Switch OFF, dan Counter Switch OFF/ON | FE+BE | 38 | TC-FA-CAID-261, TC-FA-CAID-263, TC-FA-CAID-264 |
| TC-FA-CAID-E2E-085-increment-melewati-pergantian-tahun | Increment Melewati Pergantian Tahun Tanpa Reset Counter | FE+BE | 8 | TC-FA-CAID-339 |
| TC-FA-CAID-E2E-086-v07-registrasi-dan-legacy-register | V-07 pada Registrasi: Quick Register, Legacy Register, dan Counter Setelah Penolakan | FE+BE | 34 | TC-FA-CAID-271, TC-FA-CAID-272, TC-FA-CAID-325 |
| TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer | V-07 pada Data Update, Edit Draft, Hapus Division, dan Transfer | FE+BE | 40 | TC-FA-CAID-284, TC-FA-CAID-291, TC-FA-CAID-336, TC-FA-CAID-276 |
| TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade | Transfer Group: Update Segmen Group Code, Dilewati, dan Log Cascade | FE+BE | 41 | TC-FA-CAID-273, TC-FA-CAID-274, TC-FA-CAID-275, TC-FA-CAID-253 |
| TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen | Purchase Date: Diisi Pertama Kali, Log Cascade, Idempotent, dan Diubah | FE+BE | 29 | TC-FA-CAID-277, TC-FA-CAID-278, TC-FA-CAID-254, TC-FA-CAID-283 |
| TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade | Edit Asset dan Edit Code Division: Tidak Memperbarui Asset ID Sampai Save Berikutnya | FE+BE | 30 | TC-FA-CAID-279, TC-FA-CAID-280, TC-FA-CAID-289, TC-FA-CAID-290 |
| TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade | Edit Code Group, Category, dan Asset Name: Tidak Memperbarui Asset ID Sampai Save Berikutnya | FE+BE | 19 | TC-FA-CAID-292, TC-FA-CAID-293, TC-FA-CAID-294, TC-FA-CAID-295 |
| TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten | Mutasi Division: Isi, Ganti, Log Cascade, dan Idempoten | FE+BE | 28 | TC-FA-CAID-285, TC-FA-CAID-255, TC-FA-CAID-286, TC-FA-CAID-302 |
| TC-FA-CAID-E2E-093-hapus-division-mengosongkan-segmen-division | Hapus Division dari Master: Segmen Division Menjadi 0000 | FE+BE | 10 | TC-FA-CAID-288 |
| TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id | Asset ID di All Assets, Detail Aset, dan Riwayat Asset ID | FE+BE | 32 | TC-FA-CAID-296, TC-FA-CAID-298, TC-FA-CAID-299, TC-FA-CAID-300 |
| TC-FA-CAID-E2E-095-asset-id-di-modul-konsumen | Asset ID di Daftar Modul Konsumen: Available, Borrow, Damaged, Missing, Disposal, Assignment, Transfer | FE+BE | 22 | TC-FA-CAID-297 |
| TC-FA-CAID-E2E-096-registrasi-hapus-draft-dan-counter-setelah-save | Registrasi Aset: Increment Tidak Dipakai Ulang Setelah Hapus Draft dan Counter Setelah Save | FE+BE | 18 | TC-FA-CAID-265, TC-FA-CAID-266 |
| TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division | Cascade Dilewati: Purchase Date dan Division saat Formula Tanpa Segmen atau Master Switch OFF | FE+BE | 32 | TC-FA-CAID-281, TC-FA-CAID-282, TC-FA-CAID-287, TC-FA-CAID-301 |
| TC-FA-CAID-E2E-098-pencatatan-log-absence-request-otorisasi-ditolak | Pencatatan Log Absence: Request Save dan Toggle Langsung Ditolak Tanpa Entri Log | FE+BE | 33 | TC-FA-CAID-303, TC-FA-CAID-304, TC-FA-CAID-305 |
| TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | Pencatatan Log Absence: Request Save dengan Payload Tidak Valid Ditolak Tanpa Entri Log | FE+BE | 90 | TC-FA-CAID-306, TC-FA-CAID-307, TC-FA-CAID-308, TC-FA-CAID-309, TC-FA-CAID-337, TC-FA-CAID-338 |
| TC-FA-CAID-E2E-100-pencatatan-log-absence-state-tenant-suspended-expired | Pencatatan Log Absence: Save dan Toggle Ditolak Saat Entitas Suspended atau Expired Tanpa Entri Log | FE+BE | 40 | TC-FA-CAID-312, TC-FA-CAID-313 |

---

## 2. Daftar TC Hanya-BE (Excluded dari E2E — 0 TC)

Tidak ada. Semua 343 TC masuk minimal satu spec E2E (TC defense-in-depth 303-309, 333, 337, 338 tetap di E2E menurut K-1).

---

## 3. Lapisan per TC (Traceability Matrix)

| TC ID | Lapisan | Spec E2E | Mode |
|---|---|---|:---:|
| TC-FA-CAID-1 | E2E | TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | FE+BE |
| TC-FA-CAID-2 | E2E | TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | FE+BE |
| TC-FA-CAID-3 | E2E | TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | FE+BE |
| TC-FA-CAID-4 | E2E | TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | FE+BE |
| TC-FA-CAID-5 | E2E | TC-FA-CAID-E2E-001-screening-tab-dan-navigasi | FE+BE |
| TC-FA-CAID-6 | E2E | TC-FA-CAID-E2E-003-screening-company-kosong-dan-empty-state | FE+BE |
| TC-FA-CAID-7 | E2E | TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | FE+BE |
| TC-FA-CAID-8 | E2E | TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | FE+BE |
| TC-FA-CAID-9 | E2E | TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | FE+BE |
| TC-FA-CAID-10 | E2E | TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | FE+BE |
| TC-FA-CAID-11 | E2E | TC-FA-CAID-E2E-002-screening-form-konfigurasi-tersimpan | FE+BE |
| TC-FA-CAID-12 | E2E | TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | FE+BE |
| TC-FA-CAID-13 | E2E | TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi | FE+BE |
| TC-FA-CAID-14 | E2E | TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi | FE+BE |
| TC-FA-CAID-15 | E2E | TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi | FE+BE |
| TC-FA-CAID-16 | E2E | TC-FA-CAID-E2E-004-guided-tooltip-konten-dan-navigasi | FE+BE |
| TC-FA-CAID-17 | E2E | TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | FE+BE |
| TC-FA-CAID-18 | E2E | TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | FE+BE |
| TC-FA-CAID-19 | E2E | TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | FE+BE |
| TC-FA-CAID-20 | E2E | TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | FE+BE |
| TC-FA-CAID-21 | E2E | TC-FA-CAID-E2E-005-guided-tooltip-skip-overlay-keyboard | FE+BE |
| TC-FA-CAID-22 | E2E | TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | FE+BE |
| TC-FA-CAID-23 | E2E | TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | FE+BE |
| TC-FA-CAID-24 | E2E | TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | FE+BE |
| TC-FA-CAID-25 | E2E | TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | FE+BE |
| TC-FA-CAID-26 | E2E | TC-FA-CAID-E2E-006-role-matrix-visibilitas-elemen | FE+BE |
| TC-FA-CAID-27 | E2E | TC-FA-CAID-E2E-007-role-matrix-read-only-modal-dan-download | FE+BE |
| TC-FA-CAID-28 | E2E | TC-FA-CAID-E2E-007-role-matrix-read-only-modal-dan-download | FE+BE |
| TC-FA-CAID-29 | E2E | TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | FE+BE |
| TC-FA-CAID-30 | E2E | TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | FE+BE |
| TC-FA-CAID-31 | E2E | TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | FE+BE |
| TC-FA-CAID-32 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-33 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-34 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-35 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-36 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-37 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-38 | E2E | TC-FA-CAID-E2E-010-plan-starter-gating-tab-dan-banner | FE+BE |
| TC-FA-CAID-39 | E2E | TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung | FE+BE |
| TC-FA-CAID-40 | E2E | TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung | FE+BE |
| TC-FA-CAID-41 | E2E | TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung | FE+BE |
| TC-FA-CAID-42 | E2E | TC-FA-CAID-E2E-009-capability-dicabut-dan-url-langsung | FE+BE |
| TC-FA-CAID-43 | E2E | TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | FE+BE |
| TC-FA-CAID-44 | E2E | TC-FA-CAID-E2E-015-create-pertama-company-kosong | FE+BE |
| TC-FA-CAID-45 | E2E | TC-FA-CAID-E2E-015-create-pertama-company-kosong | FE+BE |
| TC-FA-CAID-46 | E2E | TC-FA-CAID-E2E-015-create-pertama-company-kosong | FE+BE |
| TC-FA-CAID-47 | E2E | TC-FA-CAID-E2E-015-create-pertama-company-kosong | FE+BE |
| TC-FA-CAID-48 | E2E | TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter | FE+BE |
| TC-FA-CAID-49 | E2E | TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter | FE+BE |
| TC-FA-CAID-50 | E2E | TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter | FE+BE |
| TC-FA-CAID-51 | E2E | TC-FA-CAID-E2E-016-initial-company-input-dan-batas-karakter | FE+BE |
| TC-FA-CAID-52 | E2E | TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview | FE+BE |
| TC-FA-CAID-53 | E2E | TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview | FE+BE |
| TC-FA-CAID-54 | E2E | TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview | FE+BE |
| TC-FA-CAID-55 | E2E | TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | FE+BE |
| TC-FA-CAID-56 | E2E | TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | FE+BE |
| TC-FA-CAID-57 | E2E | TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | FE+BE |
| TC-FA-CAID-58 | E2E | TC-FA-CAID-E2E-017-initial-company-paste-karakter-terlarang-dan-preview | FE+BE |
| TC-FA-CAID-59 | E2E | TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | FE+BE |
| TC-FA-CAID-60 | E2E | TC-FA-CAID-E2E-018-initial-company-save-dan-validasi | FE+BE |
| TC-FA-CAID-61 | E2E | TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview | FE+BE |
| TC-FA-CAID-62 | E2E | TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview | FE+BE |
| TC-FA-CAID-63 | E2E | TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview | FE+BE |
| TC-FA-CAID-64 | E2E | TC-FA-CAID-E2E-019-segmen-checkbox-dan-live-preview | FE+BE |
| TC-FA-CAID-65 | E2E | TC-FA-CAID-E2E-020-segmen-reorder-drag-keyboard-dan-aria-live | FE+BE |
| TC-FA-CAID-66 | E2E | TC-FA-CAID-E2E-020-segmen-reorder-drag-keyboard-dan-aria-live | FE+BE |
| TC-FA-CAID-67 | E2E | TC-FA-CAID-E2E-020-segmen-reorder-drag-keyboard-dan-aria-live | FE+BE |
| TC-FA-CAID-68 | E2E | TC-FA-CAID-E2E-021-separator-dan-state-tombol-save | FE+BE |
| TC-FA-CAID-69 | E2E | TC-FA-CAID-E2E-021-separator-dan-state-tombol-save | FE+BE |
| TC-FA-CAID-70 | E2E | TC-FA-CAID-E2E-021-separator-dan-state-tombol-save | FE+BE |
| TC-FA-CAID-71 | E2E | TC-FA-CAID-E2E-021-separator-dan-state-tombol-save | FE+BE |
| TC-FA-CAID-72 | E2E | TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri | FE+BE |
| TC-FA-CAID-73 | E2E | TC-FA-CAID-E2E-022-perilaku-tombol-save | FE+BE |
| TC-FA-CAID-74 | E2E | TC-FA-CAID-E2E-022-perilaku-tombol-save | FE+BE |
| TC-FA-CAID-75 | E2E | TC-FA-CAID-E2E-022-perilaku-tombol-save | FE+BE |
| TC-FA-CAID-76 | E2E | TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial | FE+BE |
| TC-FA-CAID-77 | E2E | TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial | FE+BE |
| TC-FA-CAID-78 | E2E | TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial | FE+BE |
| TC-FA-CAID-79 | E2E | TC-FA-CAID-E2E-023-retroactive-update-separator-division-account-initial | FE+BE |
| TC-FA-CAID-80 | E2E | TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus | FE+BE |
| TC-FA-CAID-81 | E2E | TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus | FE+BE |
| TC-FA-CAID-82 | E2E | TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus | FE+BE |
| TC-FA-CAID-83 | E2E | TC-FA-CAID-E2E-024-retroactive-update-urutan-multi-perubahan-separator-khusus | FE+BE |
| TC-FA-CAID-84 | E2E | TC-FA-CAID-E2E-025-retroactive-update-increment-polos-dan-urutan-unchecked | FE+BE |
| TC-FA-CAID-85 | E2E | TC-FA-CAID-E2E-025-retroactive-update-increment-polos-dan-urutan-unchecked | FE+BE |
| TC-FA-CAID-86 | E2E | TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter | FE+BE |
| TC-FA-CAID-87 | E2E | TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter | FE+BE |
| TC-FA-CAID-88 | E2E | TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter | FE+BE |
| TC-FA-CAID-89 | E2E | TC-FA-CAID-E2E-031-v07-save-batas-63-64-65-karakter | FE+BE |
| TC-FA-CAID-90 | E2E | TC-FA-CAID-E2E-032-v07-alert-inline-hilang-dan-slot-alert-bersama | FE+BE |
| TC-FA-CAID-91 | E2E | TC-FA-CAID-E2E-032-v07-alert-inline-hilang-dan-slot-alert-bersama | FE+BE |
| TC-FA-CAID-92 | E2E | TC-FA-CAID-E2E-047-v07-toggle-on-ditolak-dan-berhasil-setelah-code-division-diperpendek | FE+BE |
| TC-FA-CAID-93 | E2E | TC-FA-CAID-E2E-047-v07-toggle-on-ditolak-dan-berhasil-setelah-code-division-diperpendek | FE+BE |
| TC-FA-CAID-94 | E2E | TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | FE+BE |
| TC-FA-CAID-95 | E2E | TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | FE+BE |
| TC-FA-CAID-96 | E2E | TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | FE+BE |
| TC-FA-CAID-97 | E2E | TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | FE+BE |
| TC-FA-CAID-98 | E2E | TC-FA-CAID-E2E-033-toggle-dialog-d02-dan-konfirmasi-disable | FE+BE |
| TC-FA-CAID-99 | E2E | TC-FA-CAID-E2E-025-retroactive-update-increment-polos-dan-urutan-unchecked | FE+BE |
| TC-FA-CAID-100 | E2E | TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock | FE+BE |
| TC-FA-CAID-101 | E2E | TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock | FE+BE |
| TC-FA-CAID-102 | E2E | TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock | FE+BE |
| TC-FA-CAID-103 | E2E | TC-FA-CAID-E2E-034-toggle-off-on-state-dan-lock | FE+BE |
| TC-FA-CAID-104 | E2E | TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | FE+BE |
| TC-FA-CAID-105 | E2E | TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | FE+BE |
| TC-FA-CAID-106 | E2E | TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | FE+BE |
| TC-FA-CAID-107 | E2E | TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | FE+BE |
| TC-FA-CAID-108 | E2E | TC-FA-CAID-E2E-035-dialog-unsaved-changes-d01-navigasi | FE+BE |
| TC-FA-CAID-109 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-110 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-111 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-112 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-113 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-114 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-115 | E2E | TC-FA-CAID-E2E-036-dialog-unsaved-changes-d01-esc-backdrop-pristine-dan-refresh | FE+BE |
| TC-FA-CAID-116 | E2E | TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris | FE+BE |
| TC-FA-CAID-117 | E2E | TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris | FE+BE |
| TC-FA-CAID-118 | E2E | TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris | FE+BE |
| TC-FA-CAID-119 | E2E | TC-FA-CAID-E2E-049-code-list-screening-isi-tab-dan-aturan-baris | FE+BE |
| TC-FA-CAID-120 | E2E | TC-FA-CAID-E2E-054-code-list-pagination-default-input-halaman-dan-state-per-tab | FE+BE |
| TC-FA-CAID-121 | E2E | TC-FA-CAID-E2E-051-code-list-search-siklus-interaksi-dan-empty-state | FE+BE |
| TC-FA-CAID-122 | E2E | TC-FA-CAID-E2E-064-code-list-search-kelas-nama-hierarki-dan-kelas-nama-datar | FE+BE |
| TC-FA-CAID-123 | E2E | TC-FA-CAID-E2E-064-code-list-search-kelas-nama-hierarki-dan-kelas-nama-datar | FE+BE |
| TC-FA-CAID-124 | E2E | TC-FA-CAID-E2E-051-code-list-search-siklus-interaksi-dan-empty-state | FE+BE |
| TC-FA-CAID-125 | E2E | TC-FA-CAID-E2E-052-code-list-search-trim-kolom-tersembunyi-dan-sort-tidak-mereset | FE+BE |
| TC-FA-CAID-126 | E2E | TC-FA-CAID-E2E-052-code-list-search-trim-kolom-tersembunyi-dan-sort-tidak-mereset | FE+BE |
| TC-FA-CAID-127 | E2E | TC-FA-CAID-E2E-050-code-list-dataset-khusus-teks-literal-dan-nama-panjang | FE+BE |
| TC-FA-CAID-128 | E2E | TC-FA-CAID-E2E-053-code-list-sort-tiga-state | FE+BE |
| TC-FA-CAID-129 | E2E | TC-FA-CAID-E2E-053-code-list-sort-tiga-state | FE+BE |
| TC-FA-CAID-130 | E2E | TC-FA-CAID-E2E-053-code-list-sort-tiga-state | FE+BE |
| TC-FA-CAID-131 | E2E | TC-FA-CAID-E2E-052-code-list-search-trim-kolom-tersembunyi-dan-sort-tidak-mereset | FE+BE |
| TC-FA-CAID-132 | E2E | TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag | FE+BE |
| TC-FA-CAID-133 | E2E | TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag | FE+BE |
| TC-FA-CAID-134 | E2E | TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag | FE+BE |
| TC-FA-CAID-135 | E2E | TC-FA-CAID-E2E-056-code-list-setup-column-screening-hide-drag | FE+BE |
| TC-FA-CAID-136 | E2E | TC-FA-CAID-E2E-057-code-list-setup-column-pin-reset-to-default-dan-penutupan-popup | FE+BE |
| TC-FA-CAID-137 | E2E | TC-FA-CAID-E2E-057-code-list-setup-column-pin-reset-to-default-dan-penutupan-popup | FE+BE |
| TC-FA-CAID-138 | E2E | TC-FA-CAID-E2E-057-code-list-setup-column-pin-reset-to-default-dan-penutupan-popup | FE+BE |
| TC-FA-CAID-139 | E2E | TC-FA-CAID-E2E-065-code-list-setup-column-guard-satu-kolom-semua-tab-dan-independen | FE+BE |
| TC-FA-CAID-140 | E2E | TC-FA-CAID-E2E-065-code-list-setup-column-guard-satu-kolom-semua-tab-dan-independen | FE+BE |
| TC-FA-CAID-141 | E2E | TC-FA-CAID-E2E-065-code-list-setup-column-guard-satu-kolom-semua-tab-dan-independen | FE+BE |
| TC-FA-CAID-142 | E2E | TC-FA-CAID-E2E-054-code-list-pagination-default-input-halaman-dan-state-per-tab | FE+BE |
| TC-FA-CAID-143 | E2E | TC-FA-CAID-E2E-054-code-list-pagination-default-input-halaman-dan-state-per-tab | FE+BE |
| TC-FA-CAID-144 | E2E | TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset | FE+BE |
| TC-FA-CAID-145 | E2E | TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset | FE+BE |
| TC-FA-CAID-146 | E2E | TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset | FE+BE |
| TC-FA-CAID-147 | E2E | TC-FA-CAID-E2E-055-code-list-pagination-halaman-tidak-valid-dan-reset | FE+BE |
| TC-FA-CAID-148 | E2E | TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | FE+BE |
| TC-FA-CAID-149 | E2E | TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | FE+BE |
| TC-FA-CAID-150 | E2E | TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CAID-151 | E2E | TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | FE+BE |
| TC-FA-CAID-152 | E2E | TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CAID-153 | E2E | TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | FE+BE |
| TC-FA-CAID-154 | E2E | TC-FA-CAID-E2E-058-code-list-download-nama-berkas-dan-kolom | FE+BE |
| TC-FA-CAID-155 | E2E | TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | FE+BE |
| TC-FA-CAID-156 | E2E | TC-FA-CAID-E2E-080-download-volume-di-atas-5000-baris | FE+BE |
| TC-FA-CAID-157 | E2E | TC-FA-CAID-E2E-007-role-matrix-read-only-modal-dan-download | FE+BE |
| TC-FA-CAID-158 | E2E | TC-FA-CAID-E2E-003-screening-company-kosong-dan-empty-state | FE+BE |
| TC-FA-CAID-159 | E2E | TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | FE+BE |
| TC-FA-CAID-160 | E2E | TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | FE+BE |
| TC-FA-CAID-161 | E2E | TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | FE+BE |
| TC-FA-CAID-162 | E2E | TC-FA-CAID-E2E-050-code-list-dataset-khusus-teks-literal-dan-nama-panjang | FE+BE |
| TC-FA-CAID-163 | E2E | TC-FA-CAID-E2E-050-code-list-dataset-khusus-teks-literal-dan-nama-panjang | FE+BE |
| TC-FA-CAID-164 | E2E | TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | FE+BE |
| TC-FA-CAID-165 | E2E | TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | FE+BE |
| TC-FA-CAID-166 | E2E | TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | FE+BE |
| TC-FA-CAID-167 | E2E | TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai | FE+BE |
| TC-FA-CAID-168 | E2E | TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai | FE+BE |
| TC-FA-CAID-169 | E2E | TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai | FE+BE |
| TC-FA-CAID-170 | E2E | TC-FA-CAID-E2E-067-changelog-search-siklus-enum-dan-nilai | FE+BE |
| TC-FA-CAID-171 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-172 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-173 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-174 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-175 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-176 | E2E | TC-FA-CAID-E2E-068-changelog-search-modified-by-date-trim-dan-visibilitas | FE+BE |
| TC-FA-CAID-177 | E2E | TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and | FE+BE |
| TC-FA-CAID-178 | E2E | TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and | FE+BE |
| TC-FA-CAID-179 | E2E | TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and | FE+BE |
| TC-FA-CAID-180 | E2E | TC-FA-CAID-E2E-069-changelog-filter-panel-date-dropdown-dan-and | FE+BE |
| TC-FA-CAID-181 | E2E | TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search | FE+BE |
| TC-FA-CAID-182 | E2E | TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search | FE+BE |
| TC-FA-CAID-183 | E2E | TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search | FE+BE |
| TC-FA-CAID-184 | E2E | TC-FA-CAID-E2E-070-changelog-filter-chip-dan-kombinasi-search | FE+BE |
| TC-FA-CAID-185 | E2E | TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | FE+BE |
| TC-FA-CAID-186 | E2E | TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | FE+BE |
| TC-FA-CAID-187 | E2E | TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | FE+BE |
| TC-FA-CAID-188 | E2E | TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | FE+BE |
| TC-FA-CAID-189 | E2E | TC-FA-CAID-E2E-071-changelog-filter-clear-field-pemulihan-draft-dan-badge | FE+BE |
| TC-FA-CAID-190 | E2E | TC-FA-CAID-E2E-072-changelog-filter-independen-kolom-tanpa-filter-dan-tanpa-hasil | FE+BE |
| TC-FA-CAID-191 | E2E | TC-FA-CAID-E2E-072-changelog-filter-independen-kolom-tanpa-filter-dan-tanpa-hasil | FE+BE |
| TC-FA-CAID-192 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-193 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-194 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-195 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-196 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-197 | E2E | TC-FA-CAID-E2E-073-changelog-sort-tiga-state | FE+BE |
| TC-FA-CAID-198 | E2E | TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | FE+BE |
| TC-FA-CAID-199 | E2E | TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | FE+BE |
| TC-FA-CAID-200 | E2E | TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | FE+BE |
| TC-FA-CAID-201 | E2E | TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | FE+BE |
| TC-FA-CAID-202 | E2E | TC-FA-CAID-E2E-074-changelog-setup-column-screening-dan-kelas-date | FE+BE |
| TC-FA-CAID-203 | E2E | TC-FA-CAID-E2E-075-changelog-setup-column-kelas-teks-pendek | FE+BE |
| TC-FA-CAID-204 | E2E | TC-FA-CAID-E2E-075-changelog-setup-column-kelas-teks-pendek | FE+BE |
| TC-FA-CAID-205 | E2E | TC-FA-CAID-E2E-075-changelog-setup-column-kelas-teks-pendek | FE+BE |
| TC-FA-CAID-206 | E2E | TC-FA-CAID-E2E-076-changelog-setup-column-kelas-nilai-campuran | FE+BE |
| TC-FA-CAID-207 | E2E | TC-FA-CAID-E2E-076-changelog-setup-column-kelas-nilai-campuran | FE+BE |
| TC-FA-CAID-208 | E2E | TC-FA-CAID-E2E-076-changelog-setup-column-kelas-nilai-campuran | FE+BE |
| TC-FA-CAID-209 | E2E | TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | FE+BE |
| TC-FA-CAID-210 | E2E | TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | FE+BE |
| TC-FA-CAID-211 | E2E | TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | FE+BE |
| TC-FA-CAID-212 | E2E | TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | FE+BE |
| TC-FA-CAID-213 | E2E | TC-FA-CAID-E2E-077-changelog-setup-column-batas-pin-reset-guard-dan-cache | FE+BE |
| TC-FA-CAID-214 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-215 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-216 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-217 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-218 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-219 | E2E | TC-FA-CAID-E2E-078-changelog-pagination-volume-5001-entri | FE+BE |
| TC-FA-CAID-220 | E2E | TC-FA-CAID-E2E-079-changelog-download-nama-header-dan-hasil-kosong | FE+BE |
| TC-FA-CAID-221 | E2E | TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CAID-222 | E2E | TC-FA-CAID-E2E-059-download-isi-berkas-csv-xlsx | FE+BE |
| TC-FA-CAID-223 | E2E | TC-FA-CAID-E2E-080-download-volume-di-atas-5000-baris | FE+BE |
| TC-FA-CAID-224 | E2E | TC-FA-CAID-E2E-079-changelog-download-nama-header-dan-hasil-kosong | FE+BE |
| TC-FA-CAID-225 | E2E | TC-FA-CAID-E2E-079-changelog-download-nama-header-dan-hasil-kosong | FE+BE |
| TC-FA-CAID-226 | E2E | TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | FE+BE |
| TC-FA-CAID-227 | E2E | TC-FA-CAID-E2E-080-download-volume-di-atas-5000-baris | FE+BE |
| TC-FA-CAID-228 | E2E | TC-FA-CAID-E2E-003-screening-company-kosong-dan-empty-state | FE+BE |
| TC-FA-CAID-229 | E2E | TC-FA-CAID-E2E-072-changelog-filter-independen-kolom-tanpa-filter-dan-tanpa-hasil | FE+BE |
| TC-FA-CAID-230 | E2E | TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | FE+BE |
| TC-FA-CAID-231 | E2E | TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | FE+BE |
| TC-FA-CAID-232 | E2E | TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | FE+BE |
| TC-FA-CAID-233 | E2E | TC-FA-CAID-E2E-037-pencatatan-log-create-company-kosong | FE+BE |
| TC-FA-CAID-234 | E2E | TC-FA-CAID-E2E-037-pencatatan-log-create-company-kosong | FE+BE |
| TC-FA-CAID-235 | E2E | TC-FA-CAID-E2E-037-pencatatan-log-create-company-kosong | FE+BE |
| TC-FA-CAID-236 | E2E | TC-FA-CAID-E2E-038-pencatatan-log-edit-status-separator-segmen | FE+BE |
| TC-FA-CAID-237 | E2E | TC-FA-CAID-E2E-038-pencatatan-log-edit-status-separator-segmen | FE+BE |
| TC-FA-CAID-238 | E2E | TC-FA-CAID-E2E-038-pencatatan-log-edit-status-separator-segmen | FE+BE |
| TC-FA-CAID-239 | E2E | TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company | FE+BE |
| TC-FA-CAID-240 | E2E | TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company | FE+BE |
| TC-FA-CAID-241 | E2E | TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company | FE+BE |
| TC-FA-CAID-242 | E2E | TC-FA-CAID-E2E-039-pencatatan-log-edit-segments-formula-dan-initial-company | FE+BE |
| TC-FA-CAID-243 | E2E | TC-FA-CAID-E2E-040-pencatatan-log-edit-urutan-dan-multi-perubahan | FE+BE |
| TC-FA-CAID-244 | E2E | TC-FA-CAID-E2E-040-pencatatan-log-edit-urutan-dan-multi-perubahan | FE+BE |
| TC-FA-CAID-245 | E2E | TC-FA-CAID-E2E-040-pencatatan-log-edit-urutan-dan-multi-perubahan | FE+BE |
| TC-FA-CAID-246 | E2E | TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri | FE+BE |
| TC-FA-CAID-247 | E2E | TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri | FE+BE |
| TC-FA-CAID-248 | E2E | TC-FA-CAID-E2E-041-pencatatan-log-snapshot-dan-kolom-surface | FE+BE |
| TC-FA-CAID-249 | E2E | TC-FA-CAID-E2E-041-pencatatan-log-snapshot-dan-kolom-surface | FE+BE |
| TC-FA-CAID-250 | E2E | TC-FA-CAID-E2E-041-pencatatan-log-snapshot-dan-kolom-surface | FE+BE |
| TC-FA-CAID-251 | E2E | TC-FA-CAID-E2E-008-role-matrix-pemegang-manage-config-tabs-save-toggle-dan-pelaku-log | FE+BE |
| TC-FA-CAID-252 | E2E | TC-FA-CAID-E2E-042-pencatatan-log-absence-tanpa-entri | FE+BE |
| TC-FA-CAID-253 | E2E | TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade | FE+BE |
| TC-FA-CAID-254 | E2E | TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen | FE+BE |
| TC-FA-CAID-255 | E2E | TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten | FE+BE |
| TC-FA-CAID-256 | E2E | TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | FE+BE |
| TC-FA-CAID-257 | E2E | TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | FE+BE |
| TC-FA-CAID-258 | E2E | TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | FE+BE |
| TC-FA-CAID-259 | E2E | TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | FE+BE |
| TC-FA-CAID-260 | E2E | TC-FA-CAID-E2E-083-registrasi-increment-dan-resolusi-segmen | FE+BE |
| TC-FA-CAID-261 | E2E | TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter | FE+BE |
| TC-FA-CAID-262 | E2E | TC-FA-CAID-E2E-030-registrasi-pertama-company-kosong-increment-polos | FE+BE |
| TC-FA-CAID-263 | E2E | TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter | FE+BE |
| TC-FA-CAID-264 | E2E | TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter | FE+BE |
| TC-FA-CAID-265 | E2E | TC-FA-CAID-E2E-096-registrasi-hapus-draft-dan-counter-setelah-save | FE+BE |
| TC-FA-CAID-266 | E2E | TC-FA-CAID-E2E-096-registrasi-hapus-draft-dan-counter-setelah-save | FE+BE |
| TC-FA-CAID-267 | E2E | TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade | FE+BE |
| TC-FA-CAID-268 | E2E | TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade | FE+BE |
| TC-FA-CAID-269 | E2E | TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade | FE+BE |
| TC-FA-CAID-270 | E2E | TC-FA-CAID-E2E-011-plan-starter-registrasi-downgrade-upgrade | FE+BE |
| TC-FA-CAID-271 | E2E | TC-FA-CAID-E2E-086-v07-registrasi-dan-legacy-register | FE+BE |
| TC-FA-CAID-272 | E2E | TC-FA-CAID-E2E-086-v07-registrasi-dan-legacy-register | FE+BE |
| TC-FA-CAID-273 | E2E | TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade | FE+BE |
| TC-FA-CAID-274 | E2E | TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade | FE+BE |
| TC-FA-CAID-275 | E2E | TC-FA-CAID-E2E-088-transfer-group-update-segmen-dan-log-cascade | FE+BE |
| TC-FA-CAID-276 | E2E | TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer | FE+BE |
| TC-FA-CAID-277 | E2E | TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen | FE+BE |
| TC-FA-CAID-278 | E2E | TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen | FE+BE |
| TC-FA-CAID-279 | E2E | TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade | FE+BE |
| TC-FA-CAID-280 | E2E | TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade | FE+BE |
| TC-FA-CAID-281 | E2E | TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division | FE+BE |
| TC-FA-CAID-282 | E2E | TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division | FE+BE |
| TC-FA-CAID-283 | E2E | TC-FA-CAID-E2E-089-purchase-date-diisi-update-segmen | FE+BE |
| TC-FA-CAID-284 | E2E | TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer | FE+BE |
| TC-FA-CAID-285 | E2E | TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten | FE+BE |
| TC-FA-CAID-286 | E2E | TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten | FE+BE |
| TC-FA-CAID-287 | E2E | TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division | FE+BE |
| TC-FA-CAID-288 | E2E | TC-FA-CAID-E2E-093-hapus-division-mengosongkan-segmen-division | FE+BE |
| TC-FA-CAID-289 | E2E | TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade | FE+BE |
| TC-FA-CAID-290 | E2E | TC-FA-CAID-E2E-090-edit-asset-dan-code-division-tanpa-cascade | FE+BE |
| TC-FA-CAID-291 | E2E | TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer | FE+BE |
| TC-FA-CAID-292 | E2E | TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade | FE+BE |
| TC-FA-CAID-293 | E2E | TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade | FE+BE |
| TC-FA-CAID-294 | E2E | TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade | FE+BE |
| TC-FA-CAID-295 | E2E | TC-FA-CAID-E2E-091-edit-code-group-category-asset-name-tanpa-cascade | FE+BE |
| TC-FA-CAID-296 | E2E | TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id | FE+BE |
| TC-FA-CAID-297 | E2E | TC-FA-CAID-E2E-095-asset-id-di-modul-konsumen | FE+BE |
| TC-FA-CAID-298 | E2E | TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id | FE+BE |
| TC-FA-CAID-299 | E2E | TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id | FE+BE |
| TC-FA-CAID-300 | E2E | TC-FA-CAID-E2E-094-asset-id-di-all-assets-detail-dan-riwayat-asset-id | FE+BE |
| TC-FA-CAID-301 | E2E | TC-FA-CAID-E2E-097-cascade-dilewati-purchase-date-dan-division | FE+BE |
| TC-FA-CAID-302 | E2E | TC-FA-CAID-E2E-092-mutasi-division-segmen-isi-ganti-dan-idempoten | FE+BE |
| TC-FA-CAID-303 | E2E | TC-FA-CAID-E2E-026-defense-in-depth-otorisasi-request-langsung | FE+BE |
| TC-FA-CAID-303 | E2E | TC-FA-CAID-E2E-098-pencatatan-log-absence-request-otorisasi-ditolak | FE+BE |
| TC-FA-CAID-304 | E2E | TC-FA-CAID-E2E-026-defense-in-depth-otorisasi-request-langsung | FE+BE |
| TC-FA-CAID-304 | E2E | TC-FA-CAID-E2E-098-pencatatan-log-absence-request-otorisasi-ditolak | FE+BE |
| TC-FA-CAID-305 | E2E | TC-FA-CAID-E2E-026-defense-in-depth-otorisasi-request-langsung | FE+BE |
| TC-FA-CAID-305 | E2E | TC-FA-CAID-E2E-098-pencatatan-log-absence-request-otorisasi-ditolak | FE+BE |
| TC-FA-CAID-306 | E2E | TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung | FE+BE |
| TC-FA-CAID-306 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-307 | E2E | TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung | FE+BE |
| TC-FA-CAID-307 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-308 | E2E | TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung | FE+BE |
| TC-FA-CAID-308 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-309 | E2E | TC-FA-CAID-E2E-027-defense-in-depth-validasi-request-langsung | FE+BE |
| TC-FA-CAID-309 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-310 | E2E | TC-FA-CAID-E2E-043-multi-konteks-isolasi-dua-tenant | FE+BE |
| TC-FA-CAID-311 | E2E | TC-FA-CAID-E2E-043-multi-konteks-isolasi-dua-tenant | FE+BE |
| TC-FA-CAID-312 | E2E | TC-FA-CAID-E2E-100-pencatatan-log-absence-state-tenant-suspended-expired | FE+BE |
| TC-FA-CAID-313 | E2E | TC-FA-CAID-E2E-100-pencatatan-log-absence-state-tenant-suspended-expired | FE+BE |
| TC-FA-CAID-314 | E2E | TC-FA-CAID-E2E-012-state-tenant-plan-diturunkan-saat-form-terbuka | FE+BE |
| TC-FA-CAID-315 | E2E | TC-FA-CAID-E2E-012-state-tenant-plan-diturunkan-saat-form-terbuka | FE+BE |
| TC-FA-CAID-316 | E2E | TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | FE+BE |
| TC-FA-CAID-317 | E2E | TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | FE+BE |
| TC-FA-CAID-318 | E2E | TC-FA-CAID-E2E-063-resilience-timeout-60-detik-toggle-dan-edit-asset-gagal | FE+BE |
| TC-FA-CAID-319 | E2E | TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | FE+BE |
| TC-FA-CAID-320 | E2E | TC-FA-CAID-E2E-063-resilience-timeout-60-detik-toggle-dan-edit-asset-gagal | FE+BE |
| TC-FA-CAID-321 | E2E | TC-FA-CAID-E2E-061-resilience-load-error-dan-toggle-5xx | FE+BE |
| TC-FA-CAID-322 | E2E | TC-FA-CAID-E2E-046-volume-10000-aset-save-sinkron-dan-rollback | FE+BE |
| TC-FA-CAID-323 | E2E | TC-FA-CAID-E2E-046-volume-10000-aset-save-sinkron-dan-rollback | FE+BE |
| TC-FA-CAID-324 | E2E | TC-FA-CAID-E2E-044-multi-konteks-dua-admin-bersamaan | FE+BE |
| TC-FA-CAID-325 | E2E | TC-FA-CAID-E2E-086-v07-registrasi-dan-legacy-register | FE+BE |
| TC-FA-CAID-326 | E2E | TC-FA-CAID-E2E-044-multi-konteks-dua-admin-bersamaan | FE+BE |
| TC-FA-CAID-327 | E2E | TC-FA-CAID-E2E-044-multi-konteks-dua-admin-bersamaan | FE+BE |
| TC-FA-CAID-328 | E2E | TC-FA-CAID-E2E-048-multi-konteks-dua-admin-status-sama-dan-sinkron-surface | FE+BE |
| TC-FA-CAID-329 | E2E | TC-FA-CAID-E2E-048-multi-konteks-dua-admin-status-sama-dan-sinkron-surface | FE+BE |
| TC-FA-CAID-330 | E2E | TC-FA-CAID-E2E-045-multi-konteks-race-dengan-mass-update | FE+BE |
| TC-FA-CAID-331 | E2E | TC-FA-CAID-E2E-045-multi-konteks-race-dengan-mass-update | FE+BE |
| TC-FA-CAID-332 | E2E | TC-FA-CAID-E2E-063-resilience-timeout-60-detik-toggle-dan-edit-asset-gagal | FE+BE |
| TC-FA-CAID-333 | E2E | TC-FA-CAID-E2E-029-defense-in-depth-save-saat-master-switch-off | FE+BE |
| TC-FA-CAID-334 | E2E | TC-FA-CAID-E2E-032-v07-alert-inline-hilang-dan-slot-alert-bersama | FE+BE |
| TC-FA-CAID-335 | E2E | TC-FA-CAID-E2E-014-plan-starter-guard-pembaruan-otomatis | FE+BE |
| TC-FA-CAID-336 | E2E | TC-FA-CAID-E2E-087-v07-data-update-edit-draft-hapus-division-dan-transfer | FE+BE |
| TC-FA-CAID-337 | E2E | TC-FA-CAID-E2E-028-defense-in-depth-initial-company-request-langsung | FE+BE |
| TC-FA-CAID-337 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-338 | E2E | TC-FA-CAID-E2E-028-defense-in-depth-initial-company-request-langsung | FE+BE |
| TC-FA-CAID-338 | E2E | TC-FA-CAID-E2E-099-pencatatan-log-absence-request-validasi-ditolak | FE+BE |
| TC-FA-CAID-339 | E2E | TC-FA-CAID-E2E-085-increment-melewati-pergantian-tahun | FE+BE |
| TC-FA-CAID-340 | E2E | TC-FA-CAID-E2E-062-resilience-save-5xx-koneksi-terputus-dan-download-gagal | FE+BE |
| TC-FA-CAID-341 | E2E | TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | FE+BE |
| TC-FA-CAID-342 | E2E | TC-FA-CAID-E2E-066-changelog-screening-format-sel-dan-tanggal | FE+BE |
| TC-FA-CAID-343 | E2E | TC-FA-CAID-E2E-060-modal-penutupan-esc-back-dan-aksesibilitas | FE+BE |
