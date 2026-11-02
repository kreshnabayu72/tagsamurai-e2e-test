# Coverage E2E — Global Settings > Hardware > Handheld Reader

Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (488 TC `TC-GS-HHR-1`–`489`, nomor `426` tidak ada di sumber, tanpa TC retired). Suite: `specs/GlobalSettings/HardwareHandheldReader/`. Prefix: `GS` + `HHR` (`TC-GS-HHR-E2E-*`). Status semua spec: `draft`, belum ada script (`web.test.ts`).

Seleksi sesuai `docs/e2e-conventions.md` bagian 2: 488 TC masuk 79 spec, 0 TC hanya-BE tidak masuk spec. Sembilan TC kandidat hanya-BE (TC-GS-HHR-417 sampai 423, 466, 474) tetap masuk sebagai spec FE+BE atas keputusan user (P-4). Setiap TC yang masuk terpetakan ke spec di `sourceTc` (diverifikasi skrip: 488 TC, 0 hilang, TC-GS-HHR-426 tidak ada di sumber maupun spec). Satu-satunya TC yang muncul di dua spec adalah 13 TC log-absence (TC-GS-HHR-229, 403 sampai 408, 413 sampai 416, 420, 474) yang asersinya terbelah antara spec asal (`012`, `013`, `049`) dan spec `079` menurut S-05; `check-suite.py` menandainya C2 (batasan skrip yang diketahui, bukan cacat), lihat Pembagian TC lintas spec.

Status revisi 2 (2026-11-02): Wave 1 dan Wave 2 selesai (79 spec). Revisi 2 menerapkan CV-03 opsi 3 (Expected relatif baseline untuk audit trail seed; 33 TC), perubahan TC Tahap 4 (BX-09, BY-01, BY-06, BY-27, BY-30, BY-31), dan Wave 2 sapuan Ringan (43 spec disunting, 36 tidak berubah); folder `036` berganti slug menjadi `TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort`.

## TC granular → spec e2e

Kolom Langkah = jumlah langkah bernomor nominal di `## Test Steps` (blok yang diulang per kolom atau per entri dihitung sekali). Dengan ekspansi iterasi: `068` 99, `070` sekitar 85, `040` 56, `041` 56, `042` 60, `045` 118, `066` 141 (80 + 61), `079` sekitar 165.

| Spec | Judul | Mode | Langkah | TC sumber |
|---|---|:---:|:---:|---|
| TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras | Screening Halaman Handheld Reader: Layout Tiga Zona, Urutan Default Device Name A-Z, Navigasi Keyboard Row Action, dan Kontras Teks WCAG 4.5:1 | FE+BE | 44 | 1, 2, 463, 464 |
| TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | Format Isi Sel Kolom Daftar Reader: Text Link Device Name, Nilai Kosong, Reader Power, Badge, Tanggal, dan Kolom Curated lewat Column Visibility | FE+BE | 89 | 3–14 |
| TC-GS-HHR-E2E-003-kartu-kuota-dan-empty-state-client-khusus | License Counter Cards Used of Kuota dan Remaining, Kartu Kuota Habis Client Q, dan Empty State Client E | FE+BE | 27 | 15–17 |
| TC-GS-HHR-E2E-004-resilience-baca-loading-dan-error-load-tabel-kartu | Resilience Baca Halaman Handheld Reader: State Loading, Error Load Tabel, dan Error Load License Counter Cards dengan Try Again | mock | 23 | 20–22 |
| TC-GS-HHR-E2E-005-guided-tooltip-konten-navigasi-keyboard | Guided Tooltip Halaman Handheld Reader: Konten Tiga Step, Navigasi Back di Step 1 dan 2, dan Navigasi Keyboard | FE+BE | 39 | 23, 28, 30 |
| TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | Guided Tooltip Halaman Handheld Reader: Muncul Otomatis, Done, Skip, Klik Overlay Menandai Seen, Replay lewat [?], serta Resize dan Navigasi Keluar Tidak Menandai Seen | FE+BE | 44 | 24–27, 29, 453 |
| TC-GS-HHR-E2E-007-guided-tooltip-langkah-dilewati-read-only-dan-kolom-tersembunyi | Guided Tooltip Halaman Handheld Reader: Step 3 Dilewati saat Kolom Device Name Disembunyikan dan Step 2 Dilewati untuk Read Only | FE+BE | 23 | 31, 32 |
| TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | Role Matrix: Visibilitas Elemen Handheld Reader per Role | FE+BE | 138 | 33, 34, 36–41, 201–206 |
| TC-GS-HHR-E2E-009-role-matrix-negatif-akses-langsung-url | Role Matrix Negatif: Akses Langsung URL Handheld Reader oleh Akun Tanpa Capability | FE+BE | 5 | 35 |
| TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | Role Matrix Positif: Eksekusi Aksi Handheld Reader per Capability Manage hardware | FE+BE | 36 | 43–49 |
| TC-GS-HHR-E2E-011-capability-dicabut-saat-aksi-berjalan | Capability Manage hardware Dicabut Saat Sesi Berjalan: Aksi Tulis Ditolak Server dan UI Di-refresh | FE+BE | 11 | 50 |
| TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server | Defense-in-Depth: Aksi Tulis Handheld Reader Tanpa Izin atau pada Reader Waiting for Approval Ditolak Server | FE+BE | 65 | 403–416 |
| TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | Defense-in-Depth: Validasi Payload Aktivasi, Alias Name, dan Reader Power Lewat Request Langsung ke Server | FE+BE | 90 | 417–425, 448, 449, 482, 483 |
| TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | Pintu Masuk Activate Reader: Overlay Select Range Type, Penutupan Overlay, Popup Menunggu Sync, dan Resolusi Minimum 1280x720 | FE+BE | 49 | 51–53, 57, 444 |
| TC-GS-HHR-E2E-015-activate-gate-kuota-habis-dan-kuota-terlampaui | Gate Kuota Activate Reader: Insufficient License Quota saat Kuota Habis dan Kuota Terlampaui akibat Downgrade | FE+BE | 32 | 54–56 |
| TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | Sync Activate Reader: Spinner, Driver Tidak Terpasang, Reader Mati, Kabel Dicabut, Dua Reader Tersambung, dan Sync Ulang yang Gagal | FE+BE | 48 | 58–62, 465 |
| TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | Aktivasi Jalur A (Official): Hasil Sync, Submit Long Range dan Short Range, Default Reader Power 30 dBm, Reader Power Disesuaikan, Alias Name, dan Aktivasi oleh Manage hardware Create | FE+BE | 90 | 42, 63–68 |
| TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | Aktivasi Jalur B (Self-Purchased): Field, Pemilih Device Name dan SKU, Validasi Submit, Batas 120 Karakter, dan Default Reader Power 30 dBm | FE+BE | 95 | 69, 71, 74, 445, 479–481, 484, 485 |
| TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | Aktivasi Jalur B Berhasil: Source Self-Purchased, Penomoran Device Name per ID, Brand Baru, Model/Type Kosong, Stay on Form, dan Counter yang Tidak Dipakai Ulang | FE+BE | 112 | 70, 72, 73, 486, 487 |
| TC-GS-HHR-E2E-020-activate-jalur-b-toggle-byo-nonaktif | Aktivasi Jalur B saat Toggle Self-Purchased Device Activation Nonaktif: Ditolak saat Sync, Pulih dengan Reader Stok, dan Ditolak saat Submit setelah Toggle Dimatikan | FE+BE | 45 | 75, 76, 473 |
| TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | Activate Reader: Collision Lintas Tenant, Serial Duplikat, Ketidaksesuaian Range Type, dan Jalur Berubah antara Sync dan Submit | FE+BE | 107 | 77–80, 477, 478 |
| TC-GS-HHR-E2E-022-activate-sync-ulang-dan-reader-dicabut | Activate Reader: Sync Ulang dengan Reader yang Sama atau Berbeda dan Reader Dicabut setelah Sync | FE+BE | 30 | 82–84 |
| TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | Activate Reader: Clear Field, Penutupan Popup (X, Esc, Backdrop, Dialog Cancel Activation), dan Reload Halaman | FE+BE | 94 | 85–94, 102 |
| TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | Activate Reader: Validasi Alias Name (Batas 120, Emoji), Trim Alias, Brand, dan Model/Type, serta Checkbox Stay on this form | FE+BE | 76 | 99–101, 446, 447, 467, 468 |
| TC-GS-HHR-E2E-025-activate-saving-state-dan-klik-ganda-submit | Activate Reader: Saving State Tombol Submit dan Klik Ganda Cepat pada Submit | FE+BE | 30 | 95, 98 |
| TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | Resilience Tulis: Aktivasi, Edit Alias Name, dan Edit Reader Power saat Kegagalan Server 5xx dan Timeout, Retry setelah Timeout | FE+BE (intercept) | 122 | 96, 97, 121, 122, 137, 368, 436 |
| TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | Resilience Tulis: Mark as, Delete, Cancel Request, dan Aksi Bulk saat Kegagalan Server 5xx serta Tidak Ada Entri Log Baru | FE+BE (intercept) | 89 | 147, 155, 160, 225, 226, 352 |
| TC-GS-HHR-E2E-028-resilience-download-daftar-usage-dan-changelog | Resilience Download: Kegagalan Unduh Daftar Reader, Tab Usage, Modal Changelog, dan Popup Event Log Activate | FE+BE (intercept) | 33 | 184, 315, 339 |
| TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | Edit Alias Name: Screening Dialog, Clear Field, Navigasi Keyboard, Emoji Diblok dan Ditolak Server, Batas 120 dan 121 Karakter, Alias Sama Diperbolehkan | FE+BE | 61 | 103, 109–114, 462 |
| TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | Edit Alias Name Sukses: Save Tanpa Perubahan dan Kapitalisasi (No-Op), Alias Baru, Trim Spasi, Saving State, Klik Ganda Save, Search Aktif, dan Mengosongkan Alias | FE+BE | 74 | 104–108, 120, 123, 124 |
| TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | Edit Alias Name: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, Tutup Tanpa Perubahan, dan Nilai Dikembalikan Tidak Dirty | FE+BE | 28 | 115–119 |
| TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | Edit Reader Power: Screening Dialog, Step Slider 1 dBm, Save Tanpa Perubahan, Row Action Short Range, dan Clear Field | FE+BE | 50 | 125, 129–132 |
| TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | Edit Reader Power Sukses: Nilai Baru, Batas 5 dan 30 dBm, Reader Damaged, Saving State, dan Klik Ganda Save | FE+BE | 46 | 126–128, 133, 451, 457 |
| TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes | Edit Reader Power: Dialog Unsaved Changes (Cancel dan Leave), Klik Backdrop, dan Tutup Tanpa Perubahan | FE+BE | 22 | 134–136, 450 |
| TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | Popup Handheld Reader Detail: Pembukaan, Screening, Nilai Kosong, Penutupan, Reader Waiting for Approval dan Jalur B, serta State Tab | FE+BE | 56 | 163–168, 472, 489 |
| TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | Tab Usage Popup Detail: Screening, Isi Baris, Badge Product, Search, Filter Panel, Sort 3-State, serta Empty State | FE+BE | 99 | 169–178 |
| TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi | Tab Usage: Transaction ID sebagai Tautan atau Teks Biasa Menurut Akses Produk, Strip untuk Event Global Settings, dan Isolasi Client | FE+BE | 20 | 179–182 |
| TC-GS-HHR-E2E-038-last-scanned-dari-usage-event-produk-lain | Last Scanned, Last Scanned In, Last User, dan Tab Usage Diperbarui dari Sesi Audit Fixed Asset dan Pair TAG Global Settings | FE+BE | 23 | 185, 186 |
| TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | Mark as Damaged, Missing, dan Available: Screening Dialog, Cancel, Esc, dan Row Action per Status | FE+BE | 23 | 138, 140, 142, 144, 146, 148 |
| TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | Mark as Damaged, Missing, dan Available Berhasil Mengubah Status, Row Action Mengikuti Status Baru, dan Klik Ganda Hanya Sekali | FE+BE | 23 | 139, 141, 143, 145, 459 |
| TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | Cancel Request Reader Waiting for Approval: Row Action Terkunci, Dialog, Go Back, Pembatalan Jalur A dan B, dan Klik Ganda | FE+BE | 39 | 156–159, 161, 162, 460 |
| TC-GS-HHR-E2E-042-delete-reader-single | Delete Reader Tunggal: Dialog, Cancel, Delete Jalur A dan B pada Status Available, Damaged, Missing, dan Klik Ganda | FE+BE | 29 | 149–154, 458 |
| TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | Bulk Action Bar dan Protokol Seleksi: Elemen Bar, Checkbox Header, Checkbox Disabled, Select All Lintas Halaman, Retensi Seleksi, dan Ikon × | FE+BE | 69 | 189–194 |
| TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | Bulk Action: Opsi yang Tampil Mengikuti Status Seluruh Reader Terpilih | FE+BE | 23 | 196–200 |
| TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | Bulk Mark as Damaged, Missing, dan Available: Dialog, Cancel, Esc, Eksekusi, Dialog Tunggal, Pencatatan Log per Reader, dan Klik Ganda | FE+BE | 83 | 207–213, 218, 219, 461 |
| TC-GS-HHR-E2E-046-bulk-delete-reader | Bulk Delete Reader: Screening Dialog, Cancel, Delete Jalur A dan B, Pengembalian Kuota, dan Pencatatan Log per Reader | FE+BE | 57 | 214–216, 220 |
| TC-GS-HHR-E2E-047-bulk-selection-limit-client-sl | Selection Limit Bulk Reader Client SL: Checkbox ke-(Limit+1) Disabled dan Select All Dipotong ke Limit | FE+BE | 17 | 221, 222 |
| TC-GS-HHR-E2E-048-bulk-status-berubah-sebelum-konfirmasi | Multi-Konteks: Bulk Mark as Damaged saat Sebagian atau Seluruh Reader Terpilih Sudah Diubah Admin Lain Sebelum Konfirmasi | FE+BE | 53 | 223, 224 |
| TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server | Defense-in-Depth: Request Bulk Langsung ke Server dengan Status Tidak Sah, Hasil Campuran, dan oleh Read Only | FE+BE | 40 | 228, 229, 466, 474 |
| TC-GS-HHR-E2E-050-search-daftar-reader | Search Daftar Reader Handheld Reader: Siklus Interaksi, Kelas Kolom, Hasil Kosong, Trim, Karakter Khusus, dan Visibilitas Kolom | FE+BE | 67 | 230–238, 455, 476 |
| TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | Filter Daftar Reader Handheld Reader: Screening Panel, Opsi DISTINCT, Multi-select OR, Antar Field AND, Chip, dan Indikator | FE+BE | 114 | 239–242, 250–254, 257–259 |
| TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | Filter Rentang Daftar Reader Handheld Reader: Reader Power Min/Max Inklusif, Last Scanned, dan Activated At | FE+BE | 53 | 243–249 |
| TC-GS-HHR-E2E-053-sort-daftar-reader | Sort Daftar Reader Handheld Reader: Siklus 3 Klik, Nilai Kosong, Numerik, Label Badge, Nama Pengguna, Tanggal, dan Kolom Actions | FE+BE | 53 | 269–276 |
| TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | Kombinasi Search, Filter, Sort, dan Pagination Daftar Reader Handheld Reader: Irisan, Clear, Empty State, Reset Filters, dan Retensi State | FE+BE | 151 | 18, 19, 260–268 |
| TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | Overlay Column Visibility dan Setup Column Daftar Reader Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, dan Persistensi | FE+BE | 202 | 277–291 |
| TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | Setup Column Tabel Sekunder Handheld Reader: Screening, Hide/Show, Reorder, Pin, Reset to Default, Tutup Tanpa Simpan, dan Kolom Terakhir pada Modal Changelog, Tab Usage, Popup Event Log Activate, dan Tab Changelog | FE+BE | 150 | 292–305 |
| TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | Download Daftar Reader Handheld Reader: CSV dan XLSX, Seluruh Baris, Search dan Filter Aktif, Kolom Visible, dan Hasil Nol Baris | FE+BE | 63 | 306–311, 313 |
| TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | Isi File Download Daftar Reader Handheld Reader: Transformasi Nilai Sel XLSX, Escape CSV dengan BOM, Download Tab Usage, Kolom Checkbox pada Export, dan Download Modal serta Tab Changelog | FE+BE | 74 | 312, 314, 183, 195, 338, 454 |
| TC-GS-HHR-E2E-059-download-lebih-dari-5000-baris | Download Daftar Reader Lebih dari 5.000 Baris pada Client Large: Loading Screen dan Unduhan Langsung | FE+BE (intercept) | 12 | 316 |
| TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | Pagination Tabel Utama dan Sekunder Handheld Reader: Navigasi, Rows per Page, Input Halaman, Reset ke Halaman 1, Sort, dan Hapus Baris Terakhir | FE+BE | 65 | 317–325 |
| TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | Modal Changelog Handheld Reader: Screening, Isi Baris, Search, Filter, Sort 3-State, dan Empty State Client E | FE+BE | 102 | 326–336 |
| TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | Tab Changelog Popup Detail dan Modal Changelog: Kolom, Filter Panel, Search Tanpa Hasil, Empty State, Hover Nama Pengguna, dan Penutupan Modal | FE+BE | 52 | 337, 340–342, 469, 470 |
| TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | Pencatatan Log per Aksi pada Tiga Surface: Edit Alias Name, Edit Reader Power, Mark as, Cancel Request, Delete, dan Snapshot Nama Reader | FE+BE | 170 | 345–351, 353 |
| TC-GS-HHR-E2E-064-pencatatan-log-aktivasi-jalur-a-dan-collision | Pencatatan Log Aktivasi Jalur A pada Tiga Surface: Status Available dan Collision Waiting for Approval | FE+BE | 45 | 343, 344 |
| TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | Absence Log: Last Scanned, Usage Event, Edit No-Op, Kegagalan Driver, dan Penolakan Client Suspended Tidak Menghasilkan Entri | FE+BE | 83 | 187, 188, 354, 355, 369, 370 |
| TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | Popup Event Log Activate: Screening, Isi Baris, Search, Filter, Sort 3-State, Download, dan Empty State Client E | FE+BE | 80 | 356–363 |
| TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi | Event Log Activate: Pencatatan Baris Activated, Waiting for Approval, dan Failed (V-04 dan V-10) | FE+BE | 63 | 364–367 |
| TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | Sinkron Admin Console Hardware Stock: Efek Mark as, Bulk, Delete, Bulk Delete, dan Cancel Request pada Unit | FE+BE | 83 | 217, 376–383 |
| TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | Keputusan Approval Principal atas Collision: Approve, Reject, Cancel Request, Pencatatan Log, dan Isolasi Tenant Lain | FE+BE | 84 | 371, 372, 385–389 |
| TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | State Tenant: Plan Starter sampai Enterprise, Client Suspended dan Expired Menolak Tulis, dan Toggle Self-Purchased Device Activation | FE+BE | 67 | 227, 390, 391, 399–402 |
| TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | Format Tanggal, Jam, dan Zona Waktu General Settings Tercermin pada Semua Surface Tanggal Handheld Reader | FE+BE | 39 | 392–396 |
| TC-GS-HHR-E2E-072-sinkron-device-allocation-dan-rename-device-name | Sinkron Admin Console: Alokasi Device Allocation pada Kartu Kuota dan Rename Device Name pada Nama Dasar Reader Jalur B | FE+BE | 31 | 397, 398, 488 |
| TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | Konkurensi Dua Admin: Edit Alias Name, Edit Reader Power, Mark as Damaged, dan Edit pada Reader yang Dihapus | FE+BE | 58 | 427, 428, 430, 431, 452 |
| TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin | Konkurensi: Cancel Request Setelah Principal Memutuskan atau Admin Lain Membatalkan, dan Delete Reader yang Sudah Dihapus | FE+BE | 38 | 429, 432, 433, 475 |
| TC-GS-HHR-E2E-075-konkurensi-aktivasi-kuota-terakhir-dan-serial-sama | Konkurensi Aktivasi: Kuota Habis Sebelum Submit, Dua Admin pada Slot Kuota Terakhir, dan Serial Number yang Sama | FE+BE | 47 | 81, 434, 435 |
| TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | Mobile (Viewport di Bawah 768px): Layout Card List, Toolbar Ikon, Selection Mode, Bottom Sheet, dan Activate Reader Disembunyikan | FE+BE (mobile) | 67 | 437–443, 471 |
| TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb | Sinkron Admin Console Hardware Stock: Efek Aktivasi Reader USB pada Unit dan Current Power Dibaca saat Aktivasi | FE+BE | 39 | 373–375, 384 |
| TC-GS-HHR-E2E-078-filter-opsi-dropdown-dinamis-dan-perubahan-data-live | Filter Daftar Reader Handheld Reader: Opsi Dropdown Device Name Bertambah Setelah Aktivasi, Opsi Aktif Dibersihkan Setelah Reader Dihapus Admin Lain, dan Loading serta No options available pada Client Tanpa Reader | FE+BE | 39 | 255, 256, 456 |
| TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | Absence Log: Request Langsung ke Server yang Ditolak Tidak Menambah Entri Changelog Handheld Reader, System Log Aktor, Activity Log, dan Event Log | FE+BE | 47 | 229, 403–408, 413–416, 420, 474 |



## TC hanya-BE (tidak masuk spec)

Tidak ada. Semua 488 TC masuk spec. TC-GS-HHR-417 sampai 423, 466, dan 474 (kandidat hanya-BE pada rencana) tetap FE+BE atas keputusan user: spec 013 (417 sampai 423) dan spec 049 (466, 474) menjalankannya lewat klien HTTP pada backend nyata dengan pembacaan state akhir di UI (kelas defense-in-depth); pengecekan jumlah entri log atas request langsung yang ditolak (TC-229, 403 sampai 408, 413 sampai 416, 420, 474) ada di spec 079.

## Ringkasan Mode

- `mock`: 1 spec, `004` (resilience baca tabel dan kartu kuota; TC-GS-HHR-20 sampai 22). Asersi yang menyangkut state backend nyata tidak teruji pada mode itu.
- FE+BE dengan intercept parsial di atas backend nyata: 4 spec, `026`, `027`, `028`, `059`.
- FE+BE viewport Mobile: `076`.
- FE+BE lainnya: 73 spec (79 total - 1 mock - 4 intercept parsial - 1 mobile), termasuk spec baru `077`, `078`, `079`.

## Kebutuhan kemampuan khusus per spec

Ringkasan; sumber resmi tiap spec adalah `## Prerequisites`-nya.

- **Simulator reader USB dan driver lokal (Sync, cabut kabel, pergantian reader):** `014` sampai `026`, `038`, `064`, `065` (TC-369, 370), `067`, `070`, `075`, `077`, `078` (TC-456). `010`, `013`, dan `068` tidak membutuhkannya; TC-42 ada di `017` dan blok USB Hardware Stock ada di `077`. Banyak TC berlabel Manual Only (b) di TC sumber (`021` sampai `025` seluruhnya) tetapi tetap ditulis (konvensi bagian 2).
- **Intercept jaringan (5xx, timeout, penundaan respons):** `004` (mock), `025`, `026`, `027`, `028`, `030` dan `033` (hanya menahan respons untuk saving state), `059`, `078` (TC-255).
- **Klien HTTP / request langsung ke server:** `012`, `013`, `049`, `079`.
- **Sesi API pelaku kedua (tidak dihitung sebagai konteks kedua):** Admin B (Nadia Pratama, `GS_TC2_PASSWORD`) di `048`, `073`, `074`, `075`, `078` (TC-256); Total Control Client A Sari Dewi (bukan Admin B) di `011`; Principal di `020`, `021`, `070`; perubahan General Settings dan Device Allocation lewat sesi API di `071`, `072`.
- **Dua sesi UI (konteks browser kedua):** `073` dan `075` (Admin B); `068`, `069`, `072`, `077` (Principal di Admin Console). `075` dan `077` memadukannya dengan simulator USB menurut `P-7`.
- **Principal / Admin Console (Hardware Stock, Approvals, Device Allocation, Device Name, toggle BYO):** `020`, `021`, `068`, `069`, `070`, `072`, `074`, `077`.
- **Sesi audit Fixed Asset dan Pair TAG (produk lain):** `038`, `065`.
- **Pembaca berkas unduhan CSV/XLSX (isi, BOM, tipe sel):** `057`, `058` (termasuk TC-183, 195, 338, 454), `066`; keberadaan atau nama berkas unduhan saja: `059`, `070` (TC-402).
- **Kontrol viewport, pembacaan geometri elemen, fokus keyboard:** `001`, `005`, `006`, `014`, `055`, `056`, `076`; pemeriksa kontras WCAG (`axe-core`): `001` (TC-464).
- **Volume data besar:** `059` (Client Large, lebih dari 5.000 reader); 26 dan 21 reader: `043`, `054`, `057`, `060` (Client L dan L2).
- **Client khusus:** B (`020`, `023`, `067`, `070`; email `totalControl_automated_qaTeam2@...`, diketahui), C (`069` login, `012` hanya target data; email `..._qaTeam3@...`, diketahui), D (`065`, `070`), X, S, P, N (`070`), E (`003`, `061`, `066`, `076`, `078`), L (`043`, `054`, `057`, `060`), L2 (`060`), SL (`047`), Q (`003`, `015`), O (`015` saja), Large (`059`).
- **Akun Manage hardware (`GS_HW_*_PASSWORD`):** `008` (Read, Create, Update, Delete), `010` (Update, Delete), `011` (Update), `012` (Create, Update), `017` (Create, blok TC-42, Rina Lestari).
- **Akun Read Only Maya Putri (`GS_RO_PASSWORD`):** `007`, `008`, `012`, `037`, `049`, `079` (blok TC-403 sampai 408 dan TC-229).
- **Mengubah state global:** format tanggal dan zona waktu General Settings (`071`); capability role (`011`); toggle BYO (`020`, `070`); Selection Limit Client SL (`047`); alokasi Device Allocation (`072`).
- **Flag Guided Tooltip:** `005`, `006`, `007`, `076` (pengecualian hook suite).

## Catatan ukuran spec

- Spec ≤ 35 langkah nominal (20 spec): `003`, `004`, `007`, `009`, `011`, `015`, `022`, `025`, `028`, `031`, `034`, `037`, `038`, `039`, `040`, `042`, `044`, `047`, `059`, `072`.
- Spec di atas 35 langkah (59 spec): alasan tertulis di `## Notes` tiap spec (satu kelas harness, satu akun, satu dataset, blok per TC yang saling pulih). Terbesar: `055` (202), `063` (170), `054` (151), `056` (150), `008` (138), `026` (122), `051` (114), `019` (112), `021` (107), `061` (102). Yang berubah pada revisi: `051` menyusut dari 149 ke 114 (TC-255, 256, 456 pindah), `046` 65 ke 57, `068` 100 ke 83 (99 dengan ekspansi), `010` 45 ke 36, `012` 76 ke 65, `013` 87 ke 90, `026` 116 ke 122, `059` 10 ke 12; spec baru `077` (39), `078` (39), `079` (47, sekitar 165 dengan ekspansi). Revisi 2: `071` 32 ke 39 (kini di atas 35), `035` 54 ke 56, `036` 92 ke 99, `061` 88 ke 102, `066` 72 ke 80, `002` 82 ke 89, `019` 107 ke 112, `014` 45 ke 49, `058` 72 ke 74, `024` 74 ke 76. Titik pisah yang disarankan penulis tercatat di Notes sebagai opsi saat script ditulis.
- Spec `076` (67 langkah) berisi satu kelas (Mobile), satu akun, tanpa aksi yang mengubah data; alasannya ada di `## Notes`.

## Pembagian TC lintas spec

- **TC-GS-HHR-183, 195, 338, 454** (isi berkas unduhan, kelas f) seluruhnya di spec `058`. Tiap TC punya klausa fungsional (nama berkas, tanpa toast sukses, Overlay Column Visibility) dan klausa isi berkas, sehingga satu rumah terbersih adalah `058`; `sourceTc` `036`, `043`, `062` tidak memuatnya. TC-GS-HHR-469 (hover nama pengguna) tetap di `062`.
- **TC-GS-HHR-217** (Bulk Delete Jalur A, unit kembali `Available` di Hardware Stock) ada di spec `068`; `046` memuat TC-214, 215, 216, 220.
- **TC-GS-HHR-373, 374, 375, 384** (aktivasi dan Current Power di Hardware Stock, reader USB bersama sesi Principal, `P-7`) ada di spec `077`; Mark as, Bulk, Delete, Bulk Delete, dan Cancel Request di Hardware Stock (TC-GS-HHR-217, 376 sampai 383) ada di `068`.
- **TC-GS-HHR-255, 256, 456** (opsi dropdown filter dinamis dan perubahan data live) ada di spec `078`; `051` memuat 12 TC filter lainnya.
- **TC-GS-HHR-42** (aktivasi Jalur A oleh Manage hardware Create) ada di spec `017` sebagai blok terakhir dengan ganti akun ke Rina Lestari; `010` memuat TC-GS-HHR-43 sampai 49.
- **TC-GS-HHR-229** (defense-in-depth bulk oleh Read Only, S-05) ada di spec `049` (respons 403 Forbidden dan kedua reader tetap ada) dan di spec `079` (jumlah entri log atas request bulk Delete yang ditolak, blok Read Only dengan baseline tiga surface dan request langsung sendiri); perilaku FE untuk penolakan izin dicakup spec `008` sampai `012`.
- **TC-GS-HHR-229, 403 sampai 408, 413 sampai 416, 420, 474 (S-05, 13 TC di dua spec):** asersi respons, pesan, dan state data ada di spec asal (`012` untuk 403 sampai 408 dan 413 sampai 416; `013` untuk 420; `049` untuk 229 dan 474), yaitu TC-403 sampai 408 butir a (403 Forbidden tanpa mengubah data), butir b (elemen yang tidak berhak tetap Hidden sesudah muat ulang), dan butir c (data tidak berubah). Jumlah entri log sebelum dan sesudah request langsung (Changelog Handheld Reader, System Log aktor, dan Activity Log; untuk TC-420 Event Log) diasersi di spec `079`. TC-229 butir a (403 Forbidden tanpa menghapus reader) dan klausa pertama butir b (kedua reader tetap ada) ada di `049`. Karena itu 13 TC itu muncul di `sourceTc` dua spec dan `check-suite.py` menandainya C2 (13 pasangan); ini pengecualian S-05, bukan cacat.
- **TC-GS-HHR-477 butir d** (Event Log tidak bertambah) tetap di spec `021` dengan `P-1` (state berat: Sync USB dan perubahan jalur Principal yang dibangun langkah sebelumnya).
- **TC-GS-HHR-350** (Cancel Request): Action `Cancel Request` hanya di Activity Log, `Delete` di Changelog dan System Log.
- **TC-GS-HHR-81** (kuota terakhir) di spec `075` bersama TC-434, 435 (konkurensi + USB, `P-7`); TC-77, 78 di `021`.
- **TC-GS-HHR-185, 186** (Last Scanned dari produk lain) di spec `038`; TC-187, 188 (absence) di spec `065`.
- Seed Reader A dipakai bersama sebagai target aksi tulis (S-06) di banyak spec (mis. `010`, `012`, `013`, `026`, `029` sampai `034`, `039` sampai `046`, `048`, `049`, `079`); reader milik spec tidak dapat ditambahkan karena kuota `Long Range` Client A terpakai 5 dari 6. Pemulihan Seed Reader A lewat fixture backend yang disediakan tim FE/BE.

## Kebutuhan lingkungan (tim FE)

Rincian usulan ada di `work-items/gs-hardware-handheld-reader/proposal-e2e-fixtures-env.md` (repo harness). Suite folder dan halaman ini tidak mengubah `spectra.config.ts`, `.env.example`, atau `fixtures/`.

- **Sudah terdaftar dan dipakai spec HHR:** `GS_TC_PASSWORD`, `GS_TC2_PASSWORD` (Admin B, Nadia Pratama, `totalControlSecond_automated_qaTeam1@qwertysystem.net`; diketahui), `GS_RO_PASSWORD`, `GS_NOCAP_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`, `GS_CLIENTB_TC_PASSWORD` (Client B, `totalControl_automated_qaTeam2@...`), `GS_CLIENTC_TC_PASSWORD` (Client C, `totalControl_automated_qaTeam3@...`).
- **Nama baru akun Manage hardware (Q1, didaftarkan FE):** `GS_HW_READ_PASSWORD` (`008`), `GS_HW_CREATE_PASSWORD` (`008`, `012`, `017`), `GS_HW_UPDATE_PASSWORD` (`008`, `010`, `011`, `012`), `GS_HW_DELETE_PASSWORD` (`008`, `010`). `GS_READ/CREATE/UPDATE/DELETE_PASSWORD` yang sudah terdaftar dipakai suite Brand untuk akun `readCapability_...` dan tidak dipakai spec HHR.
- **Skema `GS_CLIENT<NAMA>_TC_PASSWORD` yang perlu didaftarkan baru (12 nama):** `GS_CLIENTD_TC_PASSWORD`, `GS_CLIENTE_TC_PASSWORD`, `GS_CLIENTL_TC_PASSWORD`, `GS_CLIENTL2_TC_PASSWORD`, `GS_CLIENTLARGE_TC_PASSWORD`, `GS_CLIENTN_TC_PASSWORD`, `GS_CLIENTO_TC_PASSWORD`, `GS_CLIENTP_TC_PASSWORD`, `GS_CLIENTQ_TC_PASSWORD`, `GS_CLIENTS_TC_PASSWORD`, `GS_CLIENTSL_TC_PASSWORD`, `GS_CLIENTX_TC_PASSWORD`; tabel final ada di proposal di atas. `GS_BUDI_PASSWORD` (spec `038`, login Budi Santoso di hook `before`) menunggu penentuan akun dan perannya.
- **Fixture baru:** berkas `fixtures/hardwareHandheldReader.json` dengan kunci `Fixture.hardwareHandheldReader.*` yang dirujuk spec (`seedReaderA`, `seedChangelogClientA`, `seedEventLogClientA`, `seedUsageDd01`, dan kunci per spec); rujukan pertama pada tiap spec ditandai "(fixture baru)" sesuai plan.
- **Email diketahui dari Pre-setup TC (kandidat dari modul Import, konfirmasi tim FE):** Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`; Client E `totalControl_automated_qaTeam5@qwertysystem.net`, Client D `..._qaTeam9@...`, Client X `..._qaTeam11@...`, Client P `..._qaTeam12@...`, Client N `..._qaTeam13@...`.
- **Belum diketahui (menunggu FE):** email Client L, L2, Large, O, Q, S, SL ("disediakan tim FE"; sebagian spec masih menulis pola `totalControl_automated_{namaClient}@qwertysystem.net`; spec 054 dan 070 menulis "disediakan tim FE"); pendaftaran semua env di atas (termasuk `GS_CLIENTE_TC_PASSWORD`, belum tentu terdaftar); folder `hooks/`; peran akun Budi Santoso.
- **Kemampuan fixture audit trail:** fixture backend harus dapat menulis entri Changelog, Event Log, dan Usage Event bertanggal Juni 2026 (`Date` masa lalu); audit trail permanen tidak dipulihkan, jadi spec membaca relatif terhadap baseline N0 dan Filter `Date` seed. Reader DD-04 (Tab Usage) dan DD-08 (Tab Changelog) harus tanpa event pada awal spec yang membacanya (reset tingkat reader; belum ada keputusan FE/BE).
- Kemampuan teknis: lihat bagian Kebutuhan kemampuan khusus per spec dan bagian Kemampuan reset dan pemulihan di `suite.md`.
- Suite berjalan serial (`parallel: false`). Spec yang menghapus data (`042`, `046`, `068`, `060` TC-324, `049`) berjalan sesudah spec lain. Environment automation harus terisolasi dari aktivitas pengguna lain.

## Keputusan (semua terselesaikan, user 2026-10-30)

Tidak ada keputusan terbuka. Kelima keputusan dijawab user lewat klik:

1. **Isi berkas unduhan (kelas f): PINDAH ke spec `058`.** TC-183 (dari `036`), TC-195 (dari `043`), TC-338 dan TC-454 (dari `062`) dipindah seluruhnya ke `058` (lihat Pembagian TC lintas spec). `sourceTc` keempat spec diperbarui; langkah dinomori ulang; tiap TC tetap di tepat satu spec.
2. **Pengecualian Population S-12 untuk nama literal Seed Reader A: DICATAT sebagai pengecualian di `suite.md`** (bagian "Pengecualian Population S-12 (Seed Reader A)", alasan: asersi bergantung pada nama persis, isi opsi, dan jumlah). Pengecualian yang sama kini juga tertulis di `docs/e2e-conventions.md` Lampiran A butir A-5.
3. **Pelaku kedua (Admin B, Principal): TETAP sesi API.** Spec `011`, `020`, `048`, `073`, `074`, `075`, dan `078` memakai sesi API sebagai pelaku yang hanya memicu state (bukan konteks kedua).
4. **Env var: DISERAGAMKAN ke skema `GS_CLIENT<NAMA>_TC_PASSWORD`.** Nama diganti di seluruh spec (46 kemunculan, 15 spec, satu `edits apply`); nama yang sudah terdaftar tidak berubah. `proposal-e2e-fixtures-env.md` memuat tabel nama final. `spectra.config.ts`, `.env.example`, dan `fixtures/` tetap tidak disentuh (tim FE mendaftarkan 12 nama baru dan fixture). `GS_BUDI_PASSWORD` (spec `038`) belum diganti karena akun Budi Santoso belum ditentukan (tindak lanjut tim FE, bukan keputusan terbuka).
5. **Label Manual Only (USB simulator): DITERIMA sebagai keterbatasan yang diketahui** (diterima user 2026-10-30; spec tetap, prasyarat disediakan tim FE; tandai `coverage.web: unsupported` di tahap script bila perlu).

Revisi terarah 2026-10-30 (plan `plan-e2e-spec-revision.md`, disetujui user): Q1 nama env Manage hardware `GS_HW_*_PASSWORD`; Q2 TC-42 pindah ke `017` sebagai blok terakhir; Q3 TC-217 pindah ke `068`; Q4 slug `068` dan `062` diganti (`036` pada Wave 2); Q5 TC-474 ikut `079`, TC-477 d tetap di `021` dengan `P-1`; Q6 baca terbatas path endpoint di `API/openapi.yaml`; Q7 `026` dan `014` tidak dipecah, alasan jujur di Notes tanpa id pengecualian palsu; Q8 penulis menilai tiap situs penutupan popup Activate. Konvensi CV-01, 02, 04 sampai 11 terapan (K-1, P-7, S-08, format alias `<Alias>-{runId}-<NNN>`). CV-03 opsi 3 (Expected relatif baseline) terapan pada revisi 2; BX-09, BY-01, BY-06, BY-27, BY-30, BY-31 terapan. Pengecualian S-05: 13 TC log-absence ada di `sourceTc` dua spec (`012`/`013`/`049` dan `079`); temuan `check-suite.py` C2 untuk 13 TC itu adalah batasan skrip yang diketahui, bukan cacat.


## Temuan untuk QA (gabungan dari `## Notes` spec)

Diringkas dari bagian "Temuan untuk QA" 79 spec setelah revisi 2; angka dalam kurung adalah nomor spec. Butir yang sudah dibereskan perubahan TC (BX, BY, CV-03 terapan) atau kini fakta di spec sudah gugur. Tidak ada TC, PRD, atau fixture yang diubah.

### A. TC kontradiktif atau tidak konsisten

- Nama kolom `⋯`: `Column Visibility (⋯)` (TC-169) lawan `Actions (⋯)` (TC-5, 8) dan tooltip header `Column Visibility` (TC-277) (002, 036).
- TC-131 Expected a menyebut default 30 dBm, nilai tersimpan DD-03 adalah 25 dBm (032).
- TC-148 Expected b tidak menyebut `Edit Reader Power` untuk DD-04 (Short Range), sesuai PRD §4.2d (039).
- TC-196 (severity `danger` untuk semua) lawan TC-197 (`Mark as Available` dark, `Delete` danger); TC-198, 199, 200 tanpa severity (044).
- TC-421 menamai baris `Failed` `Chainway C72` tanpa ` - [N]`, TC-448 dan 449 memakai `Zebra RFID Reader (SKU-HHR-01)` (013).
- Judul identik: TC-142 dan 144, TC-143 dan 145 (dibedakan Data Uji DD-03 lawan DD-04) (039, 040).
- Judul tidak sesuai isi: TC-241 "dua opsi" hanya satu opsi (051); TC-304 "X atau Esc" hanya `[✕]` (056); TC-34 judul menyebut dua role, Precondition hanya Read Only (008).
- Expected tidak sesuai langkah: TC-173 ("seluruh Filter" dikosongkan, langkah hanya Search) (036); TC-268 ("filter kosong" tanpa Filter diterapkan, keadaan panel dan indikator pada ikon tertutup tidak dinyatakan) (054).
- TC-193 Langkah Uji 6 mengklik ikon Filter lagi sebelum `[Clear Field]` padahal panel tetap terbuka sesudah `[Apply]` (043).
- Seed Event Log menulis EL-04 `11/06/26` sebelum EL-05 `17/06/26` padahal urutan tampil mengikuti Date (066).
- TC-229 Expected b memuat dua klausa yang diasersi di dua spec: kedua reader tetap ada (`049`) dan jumlah entri log tidak bertambah (`079`); TC tidak menyatakan apakah Read Only dapat membuka tiga surface log (079).
- TC-474 Expected b menggabungkan jumlah entri tiga surface dengan `Status` `Damaged`/`Waiting for Approval` dalam satu butir; Status diasersi di `049`, jumlah entri di `079` (049, 079).
- TC-121 dan 137 menutup dialog edit dengan `✕` dan `[Leave]` (dialog `Unsaved Changes`), tetapi teks dialog tidak ada di TC; langkah 11 dan 22 di spec 026 tidak memverifikasi isi dialog (026).

### B. Precondition atau data kurang

- Email akun Client L, L2, Large, O, Q, S, SL belum diketahui (pola `totalControl_automated_{namaClient}@qwertysystem.net` atau "disediakan tim FE") dan env passwordnya belum terdaftar (003, 015, 043, 047, 054, 057, 059, 060, 070). Email Client D, E, X, P, N dan Principal kini kandidat dari Pre-setup TC (lihat Kebutuhan lingkungan; konfirmasi FE). `GS_CLIENTE_TC_PASSWORD` (061) belum tentu terdaftar. Admin B (Nadia Pratama), Client B (`qaTeam2`), dan Client C (`qaTeam3`) sudah diketahui dan terdaftar. Akun Budi Santoso (038) tidak ada di Pre-setup TC.
- Status dan Range Type reader Client L, data reader Client S, P, N, nama tiga reader Short Range Client O, katalog Device Name Client B (TC-391), Seed Changelog DD-03 (`cl_values`), seed task audit Fixed Asset `TSK-202606-0014`, SKU/Brand/Model/Current Power unit TC-477/478 tidak dirinci (015, 021, 035, 037, 054, 057, 060, 070).
- Nilai request yang tidak disebut: Reader Power TC-417; Range Type TC-421 sampai 423, 482, 483; ID Device Name yang tidak ada di katalog TC-483; payload TC-403 dan nilai request TC-413 sampai 416; rentang tanggal TC-393 dan 395; serial dan Device Name reader Admin B pada TC-81 (012, 013, 071, 075, 079).
- Reader `Missing` (DD-04) memindai di TC-185: perlu dikonfirmasi apakah reader Missing boleh memindai (038).
- Kolom curated (`Brand`, `Model/Type`, `Last Scanned In`, `Last User`) diasumsikan tersembunyi secara bawaan; TC-234 dan 269 tidak menyebutnya (050, 053).
- Pemulihan Seed Reader A, kuota `Long Range` 5 dari 6, dan counter `N` Device Name antar-TC dalam satu spec tidak dinyatakan TC (017, 019, 021, 024, 025, 026, 064, 067); stok `SN-HHR-00302` setelah TC-477/478 (021); pembersihan Brand baru TC-73 (019).
- TC yang menyasar Seed Reader A bersama padahal S-06 mewajibkan data milik spec; request ditolak sehingga data hanya dibaca (012, 013, 079).

### C. Mekanisme tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE/BE)

- Simulator reader USB dan driver lokal (014 sampai 026, 038, 064, 065, 067, 070, 075, 077, 078).
- Reset flag Guided Tooltip (005, 006, 007, 076).
- Pemulihan Seed Reader A, stok Hardware Stock, counter Device Name (banyak spec); pembuatan entri seed Changelog, Event Log, dan Usage Event bertanggal Juni 2026 (audit trail tidak dipulihkan; 035, 036, 037, 058, 061, 062, 066, 071).
- Pencabutan capability (011), sesi API Admin B dan Principal, toggle BYO, Device Allocation, General Settings, Selection Limit Client SL (011, 020, 047, 048, 070 sampai 075, 078).
- Seeding sesi audit Fixed Asset dan Pair TAG (038, 065); Seed Usage Event (036, 037).
- Penghapusan preferensi kolom di browser, pembacaan posisi kolom, pembacaan berkas unduhan, pembacaan notifikasi in-app dan job latar belakang (055, 056, 057, 058, 059).
- Endpoint request opsi filter dan unduh untuk intercept (028, 059, 078 TC-255); injeksi nilai langsung ke DOM dan status 422 (029, TC-113).
- Kode status penolakan server tidak disebut (TC-409 sampai 411, 417, 422, 228, 229, 466, 474): spec mengasersi "status penolakan, bukan 2xx" (012, 013, 049).

### D. Expected atau Post Condition tanpa cara pengamatan

- Post Condition tanpa langkah observasi dan tidak diasersi: TC-64 (017), 104 (030), 139 sampai 145 (040), 151 sampai 154 (042), 157, 159 (041), 208, 210, 212 (045), 216 (046), 217 butir b (068), 488 (072).
- Penanda yang tidak teramati: "status validasi pristine" (TC-85, 023), "tidak ada script berjalan" (TC-425, 013), "tampilan identik" antar plan (TC-399, 070), "terpotong dan dapat diklik" (TC-57, 014), indikator Step N of M (TC-23, 005), "tidak ada tooltip izin" dan "berfungsi" (TC-37 c/d, 008), elemen yang dicek setelah refresh (TC-35, 50: 009, 011).
- Toast sukses tidak disebut di Expected (TC-56, 84, 105, 324, 343, 344, 352, 363, 365, 390) sehingga tidak diasersi (015, 022, 027, 030, 060, 064, 066, 067, 070).
- "Tidak ada baris baru" atau "tidak ada efek tambahan" tanpa pembanding (TC-62, 79, 80, 187, 379, 381, 420, 421, 423, 429, 430, 431, 432, 477, 482, 483): spec memakai baseline jumlah (013, 016, 021, 065, 068, 073, 074, 079).
- Absence log (kelas g) tanpa anchor di TC: TC-100, 187; spec memakai anchor sendiri (024, 065).
- Entri baru di Changelog kumulatif tanpa cara menemukannya (TC-457, 458, 459, 460, 461): spec memakai selisih jumlah entri (033, 040, 041, 042, 045).

### E. Perilaku UI yang tidak dinyatakan TC (diambil dari TC lain atau PRD)

- Keadaan Filter Panel sesudah `[Apply]`: model "tetap terbuka" dari TC-258 (052, 036); keadaan panel pada TC-268 dan TC-193 (054, 043).
- Teks dialog `Unsaved Changes` tidak ada di TC-121/137 (026); nama tombol dialog Mark as Missing dan Mark as Available mengikuti pola `[Mark as Damaged]` (068).
- Cara menutup Overlay, dialog, atau Filter Panel (`Esc`, `✕`, `[Cancel]`) tidak disebut pada beberapa TC (027, 028, 053, 057, 061, 062, 076).
- Popup Activate yang ditutup sesudah penolakan V-10 langsung tertutup tanpa dialog `Cancel Activation` (S-08): spec 070 menulisnya tanpa langkah bersyarat. Spec 067 dan 065 (TC-370) memverifikasi dialog `Cancel Activation` (TC-89).
- DD-01 dan DD-06 sama-sama bernama `Zebra RFID Reader - 1`: spec membedakan lewat Serial Number (026, 035, 065).
- TC-434 dan 435: hasil "sesi lain" bergantung pada urutan di server; spec memakai `Verifikasi` deterministik "tepat satu sesi berhasil" (075). TC-432: posisi Approve Principal sesudah dialog dibuka (074).
- TC-229 dan TC-403 sampai 408 membuka tiga surface log sebagai Read Only tanpa menyebut path dan hak akses (079).

### F. Penempatan dan konvensi

- Kelas f (isi berkas) TC-183, 195, 338, 454 di spec 058.
- Pengecualian Population S-12 untuk nama literal Seed Reader A dicatat di `suite.md` dan di `docs/e2e-conventions.md` Lampiran A butir A-5.
- Pengecualian harness: `P-7` (simulator USB bersama konteks lain) di 075 dan 077; `P-1` (state berat) di 016 (TC-62 c) dan 021 (TC-477 d); `P-5` di 024 dan 079; `K-1` di 012, 013, 049.
- Dua kelas dalam satu spec tanpa pengecualian: 026 (fault injection + USB, tidak dipecah) dan 014 (screening + USB TC-53/57).
- TC-473 menyebut "sesi kedua" Principal; spec memakai sesi API (020).
- TC-GS-HHR-229, 403 sampai 408, 413 sampai 416, 420, 474 ada di dua spec menurut S-05 (C2, 13 pasangan).

### G. Temuan baru revisi 2 dan tindak lanjut FE/BE

Temuan baru (revisi 2):

- **Filter `Date` server-side dan inklusif:** TC-326 sampai 336 (061), 356 sampai 362 (066), 393 sampai 395 (071) bergantung pada Filter `Date` yang bekerja pada seluruh data di server dan inklusif kedua ujung; tidak didefinisikan di TC, PRD, atau LLD.
- **Fixture menulis entri Juni 2026:** fixture backend harus dapat menulis entri Changelog, Event Log, dan Usage Event dengan `Date` masa lalu (Juni 2026); tidak ada spec yang menggeser jam mundur.
- **Nol absolut TC-172 dan TC-341:** empty state Tab Usage DD-04 (036) dan Tab Changelog DD-08 (062) bergantung pada reset tingkat reader atau urutan eksekusi (spec 038 dan 065 menulis event DD-04); belum ada keputusan FE/BE. TC-185 dan TC-186 (038) tetap absolut sebagai prasyarat Tab Usage kosong DD-04/DD-07.
- **Label Time Zone TC-396:** `(UTC+00:00) UTC, Reykjavik, Accra` disalin dari TC dan belum dicocokkan dengan opsi UI General Settings (071).
- **Date picker `MM/dd/yyyy`:** format teks field date picker (036, 066, 071) belum diverifikasi pada UI.
- **`GS_CLIENTE_TC_PASSWORD`** (061) belum tentu terdaftar.
- **TC-106 butir b** (030): TC hanya menulis "bukan toast sukses" tanpa teks toast sukses.

Tindak lanjut FE/BE: pendaftaran env di `.env.example` dan `spectra.config.ts`, `fixtures/hardwareHandheldReader.json`, folder `hooks/`, peran akun Budi Santoso, mekanisme simulator USB dan pemulihan, konfirmasi email kandidat (Principal, Client E, D, X, P, N) dan email Client L, L2, Large, O, Q, S, SL.

Butir terbuka untuk audit (tidak diubah; di luar plan revisi 2):

- Folder `036` berganti nama (slug `-dan-download` dibuang); rujukan nama lama di luar suite ini tidak diperiksa.

## Tindak lanjut di luar stage ini

- **Tim FE:** menerapkan `proposal-e2e-fixtures-env.md` (fixture dan env var, termasuk `GS_HW_*_PASSWORD`), mengisi email akun yang belum ada di Pre-setup TC, dan menyediakan kemampuan pemulihan dan simulator di bagian Kemampuan reset dan pemulihan pada `suite.md`.
- **QA:** meninjau Temuan untuk QA bagian A sampai G (Keputusan 1 sampai 5 sudah dijawab user; butir terbuka di bagian G menunggu).
- **Tooling:** `pnpm exec spectra lint --strict` gagal sebelum lint berjalan karena pengecekan dependensi `pnpm install` berhenti pada `ERR_PNPM_IGNORED_BUILDS` (esbuild, msw) di lingkungan ini; lint dijalankan lewat `node_modules/.bin/spectra lint --strict`. Tim FE perlu menjalankan `pnpm approve-builds` bila `pnpm exec` dipakai.

## Lapisan per TC

TC yang muncul di dua spec (S-05) menyebut kedua spec pada satu baris.

| TC | Spec | Mode |
|---|---|:---:|
| TC-GS-HHR-1 | TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras | FE+BE |
| TC-GS-HHR-2 | TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras | FE+BE |
| TC-GS-HHR-463 | TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras | FE+BE |
| TC-GS-HHR-464 | TC-GS-HHR-E2E-001-screening-tabel-layout-urutan-default-dan-kontras | FE+BE |
| TC-GS-HHR-3 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-4 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-5 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-6 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-7 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-8 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-9 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-10 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-11 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-12 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-13 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-14 | TC-GS-HHR-E2E-002-format-isi-sel-kolom-badge-tanggal-dan-kolom-curated | FE+BE |
| TC-GS-HHR-15 | TC-GS-HHR-E2E-003-kartu-kuota-dan-empty-state-client-khusus | FE+BE |
| TC-GS-HHR-16 | TC-GS-HHR-E2E-003-kartu-kuota-dan-empty-state-client-khusus | FE+BE |
| TC-GS-HHR-17 | TC-GS-HHR-E2E-003-kartu-kuota-dan-empty-state-client-khusus | FE+BE |
| TC-GS-HHR-20 | TC-GS-HHR-E2E-004-resilience-baca-loading-dan-error-load-tabel-kartu | mock |
| TC-GS-HHR-21 | TC-GS-HHR-E2E-004-resilience-baca-loading-dan-error-load-tabel-kartu | mock |
| TC-GS-HHR-22 | TC-GS-HHR-E2E-004-resilience-baca-loading-dan-error-load-tabel-kartu | mock |
| TC-GS-HHR-23 | TC-GS-HHR-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-HHR-28 | TC-GS-HHR-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-HHR-30 | TC-GS-HHR-E2E-005-guided-tooltip-konten-navigasi-keyboard | FE+BE |
| TC-GS-HHR-24 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-25 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-26 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-27 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-29 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-453 | TC-GS-HHR-E2E-006-guided-tooltip-flag-seen-dan-dismiss | FE+BE |
| TC-GS-HHR-31 | TC-GS-HHR-E2E-007-guided-tooltip-langkah-dilewati-read-only-dan-kolom-tersembunyi | FE+BE |
| TC-GS-HHR-32 | TC-GS-HHR-E2E-007-guided-tooltip-langkah-dilewati-read-only-dan-kolom-tersembunyi | FE+BE |
| TC-GS-HHR-33 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-34 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-36 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-37 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-38 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-39 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-40 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-41 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-201 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-202 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-203 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-204 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-205 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-206 | TC-GS-HHR-E2E-008-role-matrix-visibilitas-elemen-per-role | FE+BE |
| TC-GS-HHR-35 | TC-GS-HHR-E2E-009-role-matrix-negatif-akses-langsung-url | FE+BE |
| TC-GS-HHR-43 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-44 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-45 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-46 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-47 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-48 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-49 | TC-GS-HHR-E2E-010-role-matrix-positif-eksekusi-per-capability | FE+BE |
| TC-GS-HHR-50 | TC-GS-HHR-E2E-011-capability-dicabut-saat-aksi-berjalan | FE+BE |
| TC-GS-HHR-403 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-404 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-405 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-406 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-407 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-408 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-409 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server | FE+BE |
| TC-GS-HHR-410 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server | FE+BE |
| TC-GS-HHR-411 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server | FE+BE |
| TC-GS-HHR-412 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server | FE+BE |
| TC-GS-HHR-413 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-414 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-415 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-416 | TC-GS-HHR-E2E-012-defense-in-depth-izin-aksi-tulis-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-417 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-418 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-419 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-420 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-421 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-422 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-423 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-424 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-425 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-448 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-449 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-482 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-483 | TC-GS-HHR-E2E-013-defense-in-depth-validasi-payload-aktivasi-alias-dan-power | FE+BE |
| TC-GS-HHR-51 | TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | FE+BE |
| TC-GS-HHR-52 | TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | FE+BE |
| TC-GS-HHR-53 | TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | FE+BE |
| TC-GS-HHR-57 | TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | FE+BE |
| TC-GS-HHR-444 | TC-GS-HHR-E2E-014-activate-pintu-masuk-overlay-range-type-dan-resolusi-minimum | FE+BE |
| TC-GS-HHR-54 | TC-GS-HHR-E2E-015-activate-gate-kuota-habis-dan-kuota-terlampaui | FE+BE |
| TC-GS-HHR-55 | TC-GS-HHR-E2E-015-activate-gate-kuota-habis-dan-kuota-terlampaui | FE+BE |
| TC-GS-HHR-56 | TC-GS-HHR-E2E-015-activate-gate-kuota-habis-dan-kuota-terlampaui | FE+BE |
| TC-GS-HHR-58 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-59 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-60 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-61 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-62 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-465 | TC-GS-HHR-E2E-016-activate-sync-kegagalan-driver-dan-reader | FE+BE |
| TC-GS-HHR-42 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-63 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-64 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-65 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-66 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-67 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-68 | TC-GS-HHR-E2E-017-activate-jalur-a-official-sync-submit-dan-power | FE+BE |
| TC-GS-HHR-69 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-71 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-74 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-445 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-479 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-480 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-481 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-484 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-485 | TC-GS-HHR-E2E-018-activate-jalur-b-field-pemilih-dan-validasi | FE+BE |
| TC-GS-HHR-70 | TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | FE+BE |
| TC-GS-HHR-72 | TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | FE+BE |
| TC-GS-HHR-73 | TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | FE+BE |
| TC-GS-HHR-486 | TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | FE+BE |
| TC-GS-HHR-487 | TC-GS-HHR-E2E-019-activate-jalur-b-submit-sukses-penomoran-dan-brand-baru | FE+BE |
| TC-GS-HHR-75 | TC-GS-HHR-E2E-020-activate-jalur-b-toggle-byo-nonaktif | FE+BE |
| TC-GS-HHR-76 | TC-GS-HHR-E2E-020-activate-jalur-b-toggle-byo-nonaktif | FE+BE |
| TC-GS-HHR-473 | TC-GS-HHR-E2E-020-activate-jalur-b-toggle-byo-nonaktif | FE+BE |
| TC-GS-HHR-77 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-78 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-79 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-80 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-477 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-478 | TC-GS-HHR-E2E-021-activate-collision-duplikat-dan-ketidaksesuaian-range-type | FE+BE |
| TC-GS-HHR-82 | TC-GS-HHR-E2E-022-activate-sync-ulang-dan-reader-dicabut | FE+BE |
| TC-GS-HHR-83 | TC-GS-HHR-E2E-022-activate-sync-ulang-dan-reader-dicabut | FE+BE |
| TC-GS-HHR-84 | TC-GS-HHR-E2E-022-activate-sync-ulang-dan-reader-dicabut | FE+BE |
| TC-GS-HHR-85 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-86 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-87 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-88 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-89 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-90 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-91 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-92 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-93 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-94 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-102 | TC-GS-HHR-E2E-023-activate-clear-field-penutupan-popup-dan-reload | FE+BE |
| TC-GS-HHR-99 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-100 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-101 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-446 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-447 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-467 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-468 | TC-GS-HHR-E2E-024-activate-validasi-alias-trim-dan-stay-on-form | FE+BE |
| TC-GS-HHR-95 | TC-GS-HHR-E2E-025-activate-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-GS-HHR-98 | TC-GS-HHR-E2E-025-activate-saving-state-dan-klik-ganda-submit | FE+BE |
| TC-GS-HHR-96 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-97 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-121 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-122 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-137 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-368 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-436 | TC-GS-HHR-E2E-026-resilience-tulis-aktivasi-edit-alias-dan-power | FE+BE (intercept) |
| TC-GS-HHR-147 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-155 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-160 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-225 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-226 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-352 | TC-GS-HHR-E2E-027-resilience-tulis-status-delete-cancel-dan-bulk | FE+BE (intercept) |
| TC-GS-HHR-184 | TC-GS-HHR-E2E-028-resilience-download-daftar-usage-dan-changelog | FE+BE (intercept) |
| TC-GS-HHR-315 | TC-GS-HHR-E2E-028-resilience-download-daftar-usage-dan-changelog | FE+BE (intercept) |
| TC-GS-HHR-339 | TC-GS-HHR-E2E-028-resilience-download-daftar-usage-dan-changelog | FE+BE (intercept) |
| TC-GS-HHR-103 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-109 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-110 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-111 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-112 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-113 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-114 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-462 | TC-GS-HHR-E2E-029-edit-alias-name-screening-validasi-dan-clear-field | FE+BE |
| TC-GS-HHR-104 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-105 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-106 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-107 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-108 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-120 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-123 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-124 | TC-GS-HHR-E2E-030-edit-alias-name-sukses-no-op-trim-dan-guard-save | FE+BE |
| TC-GS-HHR-115 | TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-116 | TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-117 | TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-118 | TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-119 | TC-GS-HHR-E2E-031-edit-alias-name-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-125 | TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | FE+BE |
| TC-GS-HHR-129 | TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | FE+BE |
| TC-GS-HHR-130 | TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | FE+BE |
| TC-GS-HHR-131 | TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | FE+BE |
| TC-GS-HHR-132 | TC-GS-HHR-E2E-032-edit-reader-power-screening-slider-dan-guard | FE+BE |
| TC-GS-HHR-126 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-127 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-128 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-133 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-451 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-457 | TC-GS-HHR-E2E-033-edit-reader-power-sukses-batas-dan-guard-save | FE+BE |
| TC-GS-HHR-134 | TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-135 | TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-136 | TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-450 | TC-GS-HHR-E2E-034-edit-reader-power-penutupan-form-dan-unsaved-changes | FE+BE |
| TC-GS-HHR-163 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-164 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-165 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-166 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-167 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-168 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-472 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-489 | TC-GS-HHR-E2E-035-popup-detail-reader-screening-dan-pembukaan | FE+BE |
| TC-GS-HHR-169 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-170 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-171 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-172 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-173 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-174 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-175 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-176 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-177 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-178 | TC-GS-HHR-E2E-036-tab-usage-screening-search-filter-dan-sort | FE+BE |
| TC-GS-HHR-179 | TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi | FE+BE |
| TC-GS-HHR-180 | TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi | FE+BE |
| TC-GS-HHR-181 | TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi | FE+BE |
| TC-GS-HHR-182 | TC-GS-HHR-E2E-037-tab-usage-transaction-id-akses-produk-dan-isolasi | FE+BE |
| TC-GS-HHR-185 | TC-GS-HHR-E2E-038-last-scanned-dari-usage-event-produk-lain | FE+BE |
| TC-GS-HHR-186 | TC-GS-HHR-E2E-038-last-scanned-dari-usage-event-produk-lain | FE+BE |
| TC-GS-HHR-138 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-140 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-142 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-144 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-146 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-148 | TC-GS-HHR-E2E-039-mark-as-screening-dialog-esc-dan-row-action-per-status | FE+BE |
| TC-GS-HHR-139 | TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | FE+BE |
| TC-GS-HHR-141 | TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | FE+BE |
| TC-GS-HHR-143 | TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | FE+BE |
| TC-GS-HHR-145 | TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | FE+BE |
| TC-GS-HHR-459 | TC-GS-HHR-E2E-040-mark-as-sukses-damaged-missing-available | FE+BE |
| TC-GS-HHR-156 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-157 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-158 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-159 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-161 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-162 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-460 | TC-GS-HHR-E2E-041-cancel-request-waiting-for-approval | FE+BE |
| TC-GS-HHR-149 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-150 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-151 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-152 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-153 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-154 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-458 | TC-GS-HHR-E2E-042-delete-reader-single | FE+BE |
| TC-GS-HHR-189 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-190 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-191 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-192 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-193 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-194 | TC-GS-HHR-E2E-043-bulk-action-bar-protokol-seleksi | FE+BE |
| TC-GS-HHR-196 | TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | FE+BE |
| TC-GS-HHR-197 | TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | FE+BE |
| TC-GS-HHR-198 | TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | FE+BE |
| TC-GS-HHR-199 | TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | FE+BE |
| TC-GS-HHR-200 | TC-GS-HHR-E2E-044-bulk-eligibility-opsi-per-status | FE+BE |
| TC-GS-HHR-207 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-208 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-209 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-210 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-211 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-212 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-213 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-218 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-219 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-461 | TC-GS-HHR-E2E-045-bulk-mark-as-damaged-missing-available | FE+BE |
| TC-GS-HHR-214 | TC-GS-HHR-E2E-046-bulk-delete-reader | FE+BE |
| TC-GS-HHR-215 | TC-GS-HHR-E2E-046-bulk-delete-reader | FE+BE |
| TC-GS-HHR-216 | TC-GS-HHR-E2E-046-bulk-delete-reader | FE+BE |
| TC-GS-HHR-220 | TC-GS-HHR-E2E-046-bulk-delete-reader | FE+BE |
| TC-GS-HHR-221 | TC-GS-HHR-E2E-047-bulk-selection-limit-client-sl | FE+BE |
| TC-GS-HHR-222 | TC-GS-HHR-E2E-047-bulk-selection-limit-client-sl | FE+BE |
| TC-GS-HHR-223 | TC-GS-HHR-E2E-048-bulk-status-berubah-sebelum-konfirmasi | FE+BE |
| TC-GS-HHR-224 | TC-GS-HHR-E2E-048-bulk-status-berubah-sebelum-konfirmasi | FE+BE |
| TC-GS-HHR-228 | TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server | FE+BE |
| TC-GS-HHR-229 | TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-466 | TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server | FE+BE |
| TC-GS-HHR-474 | TC-GS-HHR-E2E-049-defense-in-depth-bulk-langsung-ke-server dan TC-GS-HHR-E2E-079-absence-log-request-langsung-ditolak | FE+BE |
| TC-GS-HHR-230 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-231 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-232 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-233 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-234 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-235 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-236 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-237 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-238 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-455 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-476 | TC-GS-HHR-E2E-050-search-daftar-reader | FE+BE |
| TC-GS-HHR-239 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-240 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-241 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-242 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-250 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-251 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-252 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-253 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-254 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-257 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-258 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-259 | TC-GS-HHR-E2E-051-filter-multi-select-chip-dan-logika | FE+BE |
| TC-GS-HHR-243 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-244 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-245 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-246 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-247 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-248 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-249 | TC-GS-HHR-E2E-052-filter-rentang-reader-power-dan-tanggal | FE+BE |
| TC-GS-HHR-269 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-270 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-271 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-272 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-273 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-274 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-275 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-276 | TC-GS-HHR-E2E-053-sort-daftar-reader | FE+BE |
| TC-GS-HHR-18 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-19 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-260 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-261 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-262 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-263 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-264 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-265 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-266 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-267 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-268 | TC-GS-HHR-E2E-054-kombinasi-search-filter-sort-pagination-empty-state-dan-retensi | FE+BE |
| TC-GS-HHR-277 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-278 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-279 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-280 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-281 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-282 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-283 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-284 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-285 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-286 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-287 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-288 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-289 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-290 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-291 | TC-GS-HHR-E2E-055-overlay-column-visibility-dan-setup-column-daftar | FE+BE |
| TC-GS-HHR-292 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-293 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-294 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-295 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-296 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-297 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-298 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-299 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-300 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-301 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-302 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-303 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-304 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-305 | TC-GS-HHR-E2E-056-setup-column-tabel-sekunder | FE+BE |
| TC-GS-HHR-306 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-307 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-308 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-309 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-310 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-311 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-313 | TC-GS-HHR-E2E-057-download-csv-xlsx-daftar-reader | FE+BE |
| TC-GS-HHR-312 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-314 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-183 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-195 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-338 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-454 | TC-GS-HHR-E2E-058-download-isi-file-csv-xlsx-binary-buffer | FE+BE |
| TC-GS-HHR-316 | TC-GS-HHR-E2E-059-download-lebih-dari-5000-baris | FE+BE (intercept) |
| TC-GS-HHR-317 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-318 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-319 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-320 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-321 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-322 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-323 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-324 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-325 | TC-GS-HHR-E2E-060-pagination-tabel-utama-dan-sekunder | FE+BE |
| TC-GS-HHR-326 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-327 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-328 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-329 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-330 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-331 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-332 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-333 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-334 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-335 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-336 | TC-GS-HHR-E2E-061-changelog-modal-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-337 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-340 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-341 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-342 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-469 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-470 | TC-GS-HHR-E2E-062-changelog-modal-penutupan-dan-tab-changelog-detail | FE+BE |
| TC-GS-HHR-345 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-346 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-347 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-348 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-349 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-350 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-351 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-353 | TC-GS-HHR-E2E-063-pencatatan-log-per-aksi-tiga-surface | FE+BE |
| TC-GS-HHR-343 | TC-GS-HHR-E2E-064-pencatatan-log-aktivasi-jalur-a-dan-collision | FE+BE |
| TC-GS-HHR-344 | TC-GS-HHR-E2E-064-pencatatan-log-aktivasi-jalur-a-dan-collision | FE+BE |
| TC-GS-HHR-187 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-188 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-354 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-355 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-369 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-370 | TC-GS-HHR-E2E-065-absence-log-last-scanned-usage-event-no-op-dan-event-log | FE+BE |
| TC-GS-HHR-356 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-357 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-358 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-359 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-360 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-361 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-362 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-363 | TC-GS-HHR-E2E-066-event-log-activate-popup-screening-search-filter-sort | FE+BE |
| TC-GS-HHR-364 | TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi | FE+BE |
| TC-GS-HHR-365 | TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi | FE+BE |
| TC-GS-HHR-366 | TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi | FE+BE |
| TC-GS-HHR-367 | TC-GS-HHR-E2E-067-event-log-activate-pencatatan-hasil-aktivasi | FE+BE |
| TC-GS-HHR-217 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-376 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-377 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-378 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-379 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-380 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-381 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-382 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-383 | TC-GS-HHR-E2E-068-sinkron-hardware-stock-status-delete-cancel-dan-bulk-delete | FE+BE |
| TC-GS-HHR-371 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-372 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-385 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-386 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-387 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-388 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-389 | TC-GS-HHR-E2E-069-approval-principal-collision-dan-log | FE+BE |
| TC-GS-HHR-227 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-390 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-391 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-399 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-400 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-401 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-402 | TC-GS-HHR-E2E-070-state-tenant-suspended-expired-plan-dan-toggle-byo | FE+BE |
| TC-GS-HHR-392 | TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | FE+BE |
| TC-GS-HHR-393 | TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | FE+BE |
| TC-GS-HHR-394 | TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | FE+BE |
| TC-GS-HHR-395 | TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | FE+BE |
| TC-GS-HHR-396 | TC-GS-HHR-E2E-071-format-general-settings-dan-zona-waktu | FE+BE |
| TC-GS-HHR-397 | TC-GS-HHR-E2E-072-sinkron-device-allocation-dan-rename-device-name | FE+BE |
| TC-GS-HHR-398 | TC-GS-HHR-E2E-072-sinkron-device-allocation-dan-rename-device-name | FE+BE |
| TC-GS-HHR-488 | TC-GS-HHR-E2E-072-sinkron-device-allocation-dan-rename-device-name | FE+BE |
| TC-GS-HHR-427 | TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | FE+BE |
| TC-GS-HHR-428 | TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | FE+BE |
| TC-GS-HHR-430 | TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | FE+BE |
| TC-GS-HHR-431 | TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | FE+BE |
| TC-GS-HHR-452 | TC-GS-HHR-E2E-073-konkurensi-edit-dan-status-dua-admin | FE+BE |
| TC-GS-HHR-429 | TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin | FE+BE |
| TC-GS-HHR-432 | TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin | FE+BE |
| TC-GS-HHR-433 | TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin | FE+BE |
| TC-GS-HHR-475 | TC-GS-HHR-E2E-074-konkurensi-delete-dan-cancel-request-dua-admin | FE+BE |
| TC-GS-HHR-81 | TC-GS-HHR-E2E-075-konkurensi-aktivasi-kuota-terakhir-dan-serial-sama | FE+BE |
| TC-GS-HHR-434 | TC-GS-HHR-E2E-075-konkurensi-aktivasi-kuota-terakhir-dan-serial-sama | FE+BE |
| TC-GS-HHR-435 | TC-GS-HHR-E2E-075-konkurensi-aktivasi-kuota-terakhir-dan-serial-sama | FE+BE |
| TC-GS-HHR-437 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-438 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-439 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-440 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-441 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-442 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-443 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-471 | TC-GS-HHR-E2E-076-mobile-layout-card-list-selection-mode-dan-bottom-sheet | FE+BE (mobile) |
| TC-GS-HHR-373 | TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb | FE+BE |
| TC-GS-HHR-374 | TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb | FE+BE |
| TC-GS-HHR-375 | TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb | FE+BE |
| TC-GS-HHR-384 | TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb | FE+BE |
| TC-GS-HHR-255 | TC-GS-HHR-E2E-078-filter-opsi-dropdown-dinamis-dan-perubahan-data-live | FE+BE |
| TC-GS-HHR-256 | TC-GS-HHR-E2E-078-filter-opsi-dropdown-dinamis-dan-perubahan-data-live | FE+BE |
| TC-GS-HHR-456 | TC-GS-HHR-E2E-078-filter-opsi-dropdown-dinamis-dan-perubahan-data-live | FE+BE |
